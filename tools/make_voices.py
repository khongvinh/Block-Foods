"""Tạo giọng khách cho Block Foods bằng espeak-ng.

Chạy: python3 tools/make_voices.py
- Đọc tên món từ index.html
- Thu âm từng câu thoại của từng khách vào voice/<khách>/<mã>.mp3
- Ghi dữ liệu câu thoại vào index.html (giữa hai dấu VOICE_DATA) để chữ và tiếng luôn khớp nhau
Cần: espeak-ng, ffmpeg (libmp3lame).
"""
import json, os, re, subprocess, tempfile, unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML = os.path.join(ROOT, "index.html")
OUT = os.path.join(ROOT, "voice")

# v: giọng espeak-ng (+biến thể), p: cao độ 0-99, s: tốc độ (từ/phút)
CUSTOMERS = [
    {"id": "sv",   "e": "👩‍🎓", "n": "Cô sinh viên",    "v": "vi+f2",              "p": 72, "s": 165, "hi": "Cho em một phần {d} nha!"},
    {"id": "xeom", "e": "🧔",   "n": "Bác xe ôm",       "v": "vi-vn-x-south+m3",  "p": 28, "s": 150, "hi": "Làm cho chú một phần {d}, nhanh nhanh nghen!"},
    {"id": "vp",   "e": "👨‍💼", "n": "Anh văn phòng",   "v": "vi+m1",              "p": 48, "s": 185, "hi": "Một phần {d} mang đi nhé, anh đang vội."},
    {"id": "ba",   "e": "👵",   "n": "Bà ngoại",        "v": "vi-vn-x-central+f4", "p": 55, "s": 125, "hi": "Cho bà một phần {d} nhé cháu."},
    {"id": "tay",  "e": "👱‍♂️", "n": "Anh Tây du lịch", "v": "en-us+m3",           "p": 50, "s": 145, "hi": "Hello! One {d}, please. Cảm ơn!", "foreign": True},
    {"id": "tho",  "e": "👷",   "n": "Chú thợ hồ",      "v": "vi-vn-x-south+m1",  "p": 36, "s": 160, "hi": "Cho chú phần {d}, nhiều nhiều chút nghe!"},
    {"id": "na",   "e": "👧",   "n": "Bé Na",           "v": "vi+f5",              "p": 99, "s": 160, "hi": "Con muốn ăn {d} ạ!"},
]
REACT = {
    "perfect": ["Trời ơi ngon tuyệt cú mèo!", "Ngon quá trời luôn!"],
    "good": ["Ngon đó nha!", "Vừa miệng lắm!"],
    "burnt": ["Hơi khét chút ha.", "Cũng được, lần sau nấu kỹ hơn nha."],
}
PAY_ASK = "Tính tiền giúp nha!"
REVIEW = {"5": "Tuyệt vời! Nhất định sẽ quay lại!", "4": "Ngon lắm, cảm ơn quán!", "3": "Cũng được.",
          "2": "Hơi thất vọng chút.", "1": "Chán quá, chắc không quay lại."}
LINES = {"wless": "Ơ, thối thiếu rồi kìa!", "wmore": "Ơ, thối dư rồi nè!", "out": "Thôi khỏi thối, tôi vội lắm!",
         "oktip": "Cảm ơn nha, gửi thêm chút tiền boa nè!", "ok": "Cảm ơn nha!"}


def strip(t):
    t = t.replace("đ", "d").replace("Đ", "D")
    return "".join(c for c in unicodedata.normalize("NFD", t) if unicodedata.category(c) != "Mn")


def say(c, text, path):
    spoken = strip(text) if c.get("foreign") else text
    with tempfile.NamedTemporaryFile(suffix=".wav") as w:
        subprocess.run(["espeak-ng", "-v", c["v"], "-p", str(c["p"]), "-s", str(c["s"]), "-w", w.name, spoken], check=True)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", w.name,
                        "-af", "silenceremove=start_periods=1:start_threshold=-50dB,loudnorm=I=-15:TP=-1.5",
                        "-ac", "1", "-ar", "22050", "-b:a", "40k", path], check=True)


def main():
    html = open(HTML, encoding="utf-8").read()
    dishes = re.findall(r'\{id:"(\w+)", e:"[^"]*",(?: badge:"[^"]*",)? n:"([^"]+)"', html)
    assert len(dishes) == 12, dishes
    n = 0
    for c in CUSTOMERS:
        d = os.path.join(OUT, c["id"]); os.makedirs(d, exist_ok=True)
        for did, dn in dishes:
            say(c, c["hi"].replace("{d}", dn), os.path.join(d, f"g_{did}.mp3")); n += 1
        for k, arr in REACT.items():
            for i, t in enumerate(arr):
                say(c, f"{t} {PAY_ASK}", os.path.join(d, f"r_{k}_{i}.mp3")); n += 1
        for k, t in REVIEW.items():
            say(c, t, os.path.join(d, f"v_{k}.mp3")); n += 1
        for k, t in LINES.items():
            say(c, t, os.path.join(d, f"{k}.mp3")); n += 1
    data = {"customers": [{k: c[k] for k in ("id", "e", "n", "hi")} for c in CUSTOMERS],
            "react": REACT, "payAsk": PAY_ASK, "review": REVIEW, "lines": LINES}
    block = "/*VOICE_DATA*/const VOICE_DATA=" + json.dumps(data, ensure_ascii=False) + ";/*END_VOICE_DATA*/"
    html2, k = re.subn(r"/\*VOICE_DATA\*/.*?/\*END_VOICE_DATA\*/", lambda m: block, html, flags=re.S)
    assert k == 1, "missing VOICE_DATA marker"
    open(HTML, "w", encoding="utf-8").write(html2)
    print(f"{n} clips")


if __name__ == "__main__":
    main()
