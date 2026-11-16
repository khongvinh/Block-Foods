"""Đợt 3 (bản quốc tế): tách nền, cắt bảng hình, lưu webp vào assets/.
Chạy: python3 tools/make_round3.py   (ảnh nguồn nằm trong art_inbox/)
"""
import os
import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INBOX, OUT = os.path.join(ROOT, "art_inbox"), os.path.join(ROOT, "assets")


def cutout(im):
    a = np.asarray(im.convert("RGB")).astype(np.int16)
    mx, mn = a.max(2), a.min(2)
    lab, _ = ndimage.label((mn > 226) & ((mx - mn) < 24))
    border = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))) - {0}
    fg = ~ndimage.binary_dilation(np.isin(lab, list(border)), iterations=1)
    fl, n = ndimage.label(fg)
    if n:
        sizes = ndimage.sum(fg, fl, range(1, n + 1))
        fg = np.isin(fl, [i + 1 for i, s in enumerate(sizes) if s >= 0.004 * sizes.max()])
    out = im.convert("RGBA")
    out.putalpha(Image.fromarray((fg * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.2)))
    return out.crop(out.getbbox())


def save(img, name, w):
    if img.width > w:
        img = img.resize((w, round(img.height * w / img.width)), Image.LANCZOS)
    img.save(os.path.join(OUT, name + ".webp"), "WEBP", quality=88, method=6)
    print(name, img.size)


# 10 món vẽ lẻ
for n in ["eggfriedrice", "omelette", "padthai", "ramen", "sandwich", "spaghetti", "sweetsour", "tacos", "teriyaki", "tomyum"]:
    save(cutout(Image.open(f"{INBOX}/dish-{n}.webp")), f"dish-{n}", 300)

# bảng hình: (tên, hộp cắt x0,y0,x1,y1, chiều rộng tối đa)
SHEETS = {
    "sheet-dishes-coins": [("dish-mapotofu", (55, 120, 729, 650), 300), ("dish-bibimbap", (782, 140, 1438, 650), 300),
        ("coin-5", (43, 840, 381, 1200), 140), ("coin-10", (392, 840, 730, 1200), 140), ("coin-20", (741, 840, 1079, 1200), 140),
        ("coin-50", (1092, 820, 1456, 1210), 150), ("coin-bar", (56, 1430, 535, 1850), 200), ("ui-coin", (604, 1505, 889, 1815), 96),
        ("ui-coinbag", (985, 1350, 1436, 1862), 140)],
    "sheet-customers-ingredients": [("cus-sv", (40, 180, 513, 820), 240), ("cus-ba", (534, 175, 959, 818), 240),
        ("cus-chuba", (979, 150, 1457, 815), 240), ("ing-spaghetti", (578, 1095, 968, 1715), 200),
        ("ing-tortilla", (32, 1175, 546, 1640), 200), ("ing-flour", (1024, 1125, 1436, 1680), 200)],
    "sheet-home": [("tray", (30, 220, 1462, 572), 900), ("food-ramen", (82, 754, 485, 1167), 260), ("food-taco", (570, 812, 928, 1159), 260),
        ("food-sushi", (1018, 831, 1429, 1141), 260), ("food-donut", (227, 1399, 625, 1731), 260), ("food-burger", (862, 1361, 1255, 1746), 260)],
}
for sheet, items in SHEETS.items():
    src = Image.open(f"{INBOX}/{sheet}.webp").convert("RGB")
    for name, box, w in items:
        save(cutout(src.crop(box)), name, w)

# nền bếp mới
bg = Image.open(f"{INBOX}/bg-kitchen.webp").convert("RGB")
bg = bg.resize((720, round(bg.height * 720 / bg.width)), Image.LANCZOS)
bg.save(f"{OUT}/bg-kitchen.webp", "WEBP", quality=80, method=6)
print("bg-kitchen", bg.size)
