"""Cắt bảng hình tổng hợp (sprite sheet) thành từng file webp trong assets/.

Chạy: python3 tools/cut_sheet.py <đường_dẫn_bảng_hình.png>
Tọa độ (x0, y0, x1, y1) tính trên ảnh gốc 1792×2400.
"""
import os, sys
import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets")
CREAM = np.array([255, 243, 219])

# tên file: (hộp cắt, chiều rộng tối đa, số mảnh cần tách theo chiều ngang)
ITEMS = {
    # nguyên liệu
    "ing-trung": ((98, 194, 216, 340), 160, 1), "ing-hanh": ((272, 185, 440, 346), 160, 1),
    "ing-dualeo": ((476, 193, 632, 342), 160, 1), "ing-banhmi": ((669, 196, 837, 338), 160, 1),
    "ing-banhpho": ((68, 428, 246, 583), 160, 1), "ing-rauthom": ((278, 422, 437, 585), 160, 1),
    "ing-banhtrang": ((467, 435, 641, 579), 160, 1), "ing-tom2": ((672, 339, 834, 585), 160, 1),
    "ing-thom": ((92, 653, 220, 826), 160, 1), "ing-botgao": ((276, 661, 436, 823), 160, 1),
    "ing-nuocmau": ((508, 655, 598, 828), 160, 1), "ing-chanh": ((671, 662, 834, 822), 160, 1),
    # món ăn
    "dish-trungchien": ((932, 203, 1128, 340), 260, 1), "dish-comtam": ((1136, 197, 1338, 344), 260, 1),
    "dish-banhmi": ((1349, 193, 1537, 341), 260, 1), "dish-pho": ((1554, 169, 1743, 392), 260, 1),
    "dish-buncha": ((937, 432, 1123, 587), 260, 1), "dish-goicuon": ((1137, 432, 1336, 585), 260, 1),
    "dish-canhchua": ((1350, 431, 1536, 587), 260, 1), "dish-banhxeo": ((1549, 435, 1747, 587), 260, 1),
    "dish-cakho": ((930, 673, 1130, 819), 260, 1), "dish-bunbo": ((1141, 661, 1332, 826), 260, 1),
    "dish-canhnam": ((1350, 666, 1536, 823), 260, 1), "dish-comchien": ((1545, 672, 1751, 822), 260, 1),
    # khách
    "cus-sv": ((61, 1059, 249, 1262), 240, 1), "cus-xeom": ((278, 1058, 434, 1265), 240, 1),
    "cus-vp": ((482, 1057, 650, 1262), 240, 1), "cus-ba": ((699, 1064, 845, 1266), 240, 1),
    "cus-tay": ((90, 1352, 243, 1568), 240, 1), "cus-chuba": ((274, 1338, 487, 1568), 240, 1),
    "cus-tho": ((490, 1353, 663, 1565), 240, 1), "cus-na": ((667, 1404, 824, 1565), 240, 1),
    # màn nấu
    "cook-dia": ((970, 1082, 1168, 1218), 220, 1), "cook-dia-vo": ((1230, 1076, 1424, 1217), 220, 1),
    "cook-met": ((1492, 1068, 1702, 1224), 220, 1), "cook-lua": ((1136, 1262, 1281, 1378), 160, 1),
    "cook-chao": ((1510, 1261, 1749, 1412), 240, 1),
    # tiền
    "bill-20k": ((73, 1820, 329, 1967), 300, 1), "bill-50k": ((347, 1819, 601, 1964), 300, 1),
    "bill-100k": ((69, 1990, 333, 2139), 300, 1), "bill-200k": ((347, 1989, 608, 2137), 300, 1),
    "bill-5k": ((623, 1993, 855, 2134), 300, 1), "bill-500k": ((69, 2168, 339, 2320), 300, 1),
    # icon
    "ui-star*": ((941, 1590, 1122, 1684), 96, 2), "ui-money": ((1163, 1579, 1270, 1704), 128, 1),
    "ui-crown": ((1327, 1590, 1438, 1692), 128, 1), "ui-trophy": ((1468, 1585, 1585, 1702), 128, 1),
    "ui-order": ((1612, 1585, 1714, 1704), 128, 1), "ui-trophy2": ((971, 1775, 1088, 1892), 128, 1),
    "ui-medal*": ((1111, 1781, 1337, 1893), 96, 3), "ui-lock*": ((1364, 1775, 1538, 1890), 128, 2),
    "ui-smile": ((1591, 1765, 1732, 1888), 128, 1), "ui-knife": ((968, 1965, 1094, 2094), 128, 1),
    "ui-dizzy": ((1136, 1964, 1294, 2090), 128, 1), "ui-crown-new": ((1304, 1973, 1430, 2085), 128, 1),
    "ui-chef": ((1442, 1965, 1578, 2090), 128, 1), "ui-login": ((1621, 1968, 1726, 2088), 128, 1),
    "ui-cloud": ((959, 2173, 1103, 2272), 128, 1), "ui-wifi": ((1163, 2170, 1284, 2276), 128, 1),
    "btn-back": ((1318, 2160, 1552, 2295), 160, 1), "ui-check": ((1609, 2172, 1725, 2277), 128, 1),
}
SPLIT_NAMES = {"ui-star*": ["ui-star", "ui-star-off"], "ui-medal*": ["ui-medal-1", "ui-medal-2", "ui-medal-3"],
               "ui-lock*": ["ui-lock", "ui-unlock"]}


def cutout(crop):
    a = np.asarray(crop).astype(int)
    near = np.abs(a - CREAM).sum(2) < 42
    near |= (a.min(2) > 238)  # trắng/kem rất sáng
    lab, _ = ndimage.label(near)
    border = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))) - {0}
    bg = ndimage.binary_dilation(np.isin(lab, list(border)), iterations=1)
    fg = ~bg
    # bỏ mảnh nhỏ (chữ chú thích, vụn)
    fl, n = ndimage.label(fg)
    if n:
        sizes = ndimage.sum(fg, fl, range(1, n + 1))
        keep = [i + 1 for i, sz in enumerate(sizes) if sz >= 0.06 * sizes.max()]
        fg = np.isin(fl, keep)
    fg = ndimage.binary_fill_holes(fg) | (fg)
    alpha = Image.fromarray((fg * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.8))
    out = crop.convert("RGBA"); out.putalpha(alpha)
    return out, fg


def save(img, name, w):
    img = img.crop(img.getbbox())
    if img.width > w:
        img = img.resize((w, round(img.height * w / img.width)), Image.LANCZOS)
    img.save(os.path.join(OUT, name + ".webp"), "WEBP", quality=88, method=6)
    return img.size


def main(path):
    sheet = Image.open(path).convert("RGB")
    os.makedirs(OUT, exist_ok=True)
    for name, (box, w, parts) in ITEMS.items():
        img, fg = cutout(sheet.crop(box))
        if parts == 1:
            print(name, save(img, name, w)); continue
        # tách theo cột trống giữa các mảnh
        cols = fg.any(0); runs = []; x = 0
        while x < len(cols):
            if cols[x]:
                s = x
                while x < len(cols) and cols[x]: x += 1
                runs.append((s, x))
            x += 1
        runs = sorted(runs, key=lambda r: r[1] - r[0], reverse=True)[:parts]
        for (s, e), nm in zip(sorted(runs), SPLIT_NAMES[name]):
            print(nm, save(img.crop((s, 0, e, img.height)), nm, w))


if __name__ == "__main__":
    main(sys.argv[1])
