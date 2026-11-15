"""Đợt 2: tách nền và lưu các hình bổ sung vào assets/ (dùng chung hàm cutout với make_assets.py)."""
import os, sys
import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage

SRC = sys.argv[1] if len(sys.argv) > 1 else "/root/.claude/uploads/fe3c434f-9f1a-531f-a524-614d9442f84e"
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets")
JOBS = [("eb2630d6", "btn-restart", 160), ("4d45d170", "ui-burnt", 200), ("4456d88a", "bill-10k", 300),
        ("96d1f5e2", "btn-plain-gold", 900), ("2fa09865", "btn-plain-brown", 900), ("38d3a920", "btn-plain-orange", 900),
        ("14d7dcb2", "btn-plain-green", 900), ("485ff14c", "ing-dauhu", 200), ("4142f42b", "ing-nam", 200),
        ("3d5cc4c4", "ing-toi", 200), ("1d032f0b", "ing-gia", 200), ("fc816a31", "ing-cachua", 200),
        ("f8f6188b", "ing-ca", 200), ("f16b4674", "ing-rausong", 200), ("f00e5125", "ing-bun", 200),
        ("955418ac", "ing-thit", 200), ("c6ecd8b2", "ing-suon", 200)]


def cutout(im):
    a = np.asarray(im.convert("RGB")).astype(np.int16)
    mx, mn = a.max(2), a.min(2)
    lab, _ = ndimage.label((mn > 226) & ((mx - mn) < 24))
    border = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))) - {0}
    fg = ~ndimage.binary_dilation(np.isin(lab, list(border)), iterations=1)
    fl, n = ndimage.label(fg)
    if n:
        sizes = ndimage.sum(fg, fl, range(1, n + 1))
        fg = np.isin(fl, [i + 1 for i, s in enumerate(sizes) if s >= 0.02 * sizes.max()])
    out = im.convert("RGBA")
    out.putalpha(Image.fromarray((fg * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.2)))
    return out.crop(out.getbbox())


for fid, name, w in JOBS:
    out = cutout(Image.open(f"{SRC}/{fid}-image.png"))
    if out.width > w:
        out = out.resize((w, round(out.height * w / out.width)), Image.LANCZOS)
    out.save(f"{OUT}/{name}.webp", "WEBP", quality=88, method=6)
    print(name, out.size)
