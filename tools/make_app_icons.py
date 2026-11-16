"""Tạo icon và màn hình chờ (splash) cho bản Android từ hình trong assets/.
Chạy: python3 tools/make_app_icons.py   (sau khi đã có app/android)
"""
import os, glob
from PIL import Image, ImageDraw

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RES = os.path.join(ROOT, "app/android/app/src/main/res")
BG = (255, 181, 71)        # nền icon: cam ấm
SPLASH_BG = (253, 243, 225)

dish = Image.open(f"{ROOT}/assets/dish-ramen.webp").convert("RGBA")
logo = Image.open(f"{ROOT}/assets/logo-title.webp").convert("RGBA")

def fit(img, box):
    s = min(box / img.width, box / img.height)
    return img.resize((round(img.width * s), round(img.height * s)), Image.LANCZOS)

def paste_center(canvas, img, dy=0):
    canvas.alpha_composite(img, ((canvas.width - img.width) // 2, (canvas.height - img.height) // 2 + dy))

def foreground(size):                      # lớp trước của adaptive icon (108dp, vùng an toàn 66dp)
    c = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    paste_center(c, fit(dish, size * 0.60))
    return c

def legacy(size, round_=False):            # icon cho máy Android cũ
    c = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    m = Image.new("L", (size, size), 0)
    d = ImageDraw.Draw(m)
    (d.ellipse if round_ else lambda b, fill: d.rounded_rectangle(b, radius=size * 0.22, fill=fill))((0, 0, size - 1, size - 1), fill=255)
    bg = Image.new("RGBA", (size, size), BG + (255,))
    c.paste(bg, (0, 0), m)
    paste_center(c, fit(dish, size * 0.78))
    return c

DPI = {"mdpi": 1, "hdpi": 1.5, "xhdpi": 2, "xxhdpi": 3, "xxxhdpi": 4}
for name, k in DPI.items():
    d = f"{RES}/mipmap-{name}"
    legacy(round(48 * k)).save(f"{d}/ic_launcher.png")
    legacy(round(48 * k), True).save(f"{d}/ic_launcher_round.png")
    foreground(round(108 * k)).save(f"{d}/ic_launcher_foreground.png")

with open(f"{RES}/values/ic_launcher_background.xml", "w") as f:
    f.write('<?xml version="1.0" encoding="utf-8"?>\n<resources>\n    <color name="ic_launcher_background">#%02X%02X%02X</color>\n</resources>\n' % BG)

# màn hình chờ: giữ đúng kích thước các file splash.png Capacitor tạo sẵn
for p in glob.glob(f"{RES}/drawable*/splash.png"):
    w, h = Image.open(p).size
    c = Image.new("RGBA", (w, h), SPLASH_BG + (255,))
    paste_center(c, fit(logo, min(w, h) * 0.7))
    c.convert("RGB").save(p)

# icon 512×512 cho trang Google Play
os.makedirs(f"{ROOT}/store", exist_ok=True)
ic = Image.new("RGBA", (512, 512), BG + (255,))
paste_center(ic, fit(dish, 400))
ic.convert("RGB").save(f"{ROOT}/store/icon-512.png")
print("xong")
