"""Xóa nền trắng nối với mép ảnh, cắt sát, thu nhỏ, lưu webp vào assets/."""
import os
import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage

SRC = "/root/.claude/uploads/fe3c434f-9f1a-531f-a524-614d9442f84e"
OUT = "/home/user/Block-Foods/assets"
os.makedirs(OUT, exist_ok=True)

# (file id, output name, max width, crop box fraction to drop watermark or None)
JOBS = [
    ("16adbc87", "panel-light", 900, None),
    ("e4da9ac3", "plank", 900, None),
    ("b7a5d8a7", "food-com", 320, None),
    ("ead870bb", "food-ot", 320, None),
    ("771b93e1", "food-tom", 320, None),
    ("7104afa0", "food-banhmi", 320, None),
    ("0ac11030", "food-pho", 320, None),
    ("5b5df00a", "tray", 900, (0, 0, 0.965, 0.93)),
    ("c6a5abc8", "icon-sound", 160, None),
    ("338b27aa", "icon-music", 160, None),
    ("2f0fbba1", "btn-rank", 720, None),
    ("9be8715e", "btn-menu", 720, None),
    ("99066121", "btn-endless", 720, None),
    ("f61334a4", "btn-cook", 720, None),
    ("f110e06d", "logo", 760, None),
]


def cutout(im):
    a = np.asarray(im.convert("RGB")).astype(np.int16)
    mx, mn = a.max(2), a.min(2)
    whiteish = (mn > 228) & ((mx - mn) < 22)
    lab, _ = ndimage.label(whiteish)
    border = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))) - {0}
    bg = np.isin(lab, list(border))
    bg = ndimage.binary_dilation(bg, iterations=1)  # ăn nhẹ viền trắng răng cưa
    alpha = np.where(bg, 0, 255).astype(np.uint8)
    am = Image.fromarray(alpha).filter(ImageFilter.GaussianBlur(1.2))
    out = im.convert("RGBA"); out.putalpha(am)
    return out


for fid, name, w, crop in JOBS:
    im = Image.open(f"{SRC}/{fid}-image.png")
    if crop:
        W, H = im.size
        # chỉ cần xóa ngôi sao góc phải dưới: tô trắng vùng đó trước khi tách nền
        x0, y0 = int(W * crop[2]), int(H * crop[3])
        px = im.load()
        for x in range(x0, W):
            for y in range(y0, H):
                px[x, y] = (255, 255, 255)
    out = cutout(im)
    out = out.crop(out.getbbox())
    if out.width > w:
        out = out.resize((w, round(out.height * w / out.width)), Image.LANCZOS)
    out.save(f"{OUT}/{name}.webp", "WEBP", quality=86, method=6)
    print(name, out.size, os.path.getsize(f"{OUT}/{name}.webp") // 1024, "KB")

# Nền gian bếp: cắt bỏ ngôi sao góc phải dưới, thu nhỏ
bg = Image.open(f"{SRC}/2795c7a0-image.png").convert("RGB")
W, H = bg.size
bg = bg.crop((0, 0, W, int(H * 0.955)))
bg = bg.resize((720, round(bg.height * 720 / bg.width)), Image.LANCZOS)
bg.save(f"{OUT}/bg-kitchen.webp", "WEBP", quality=78, method=6)
print("bg-kitchen", bg.size, os.path.getsize(f"{OUT}/bg-kitchen.webp") // 1024, "KB")
