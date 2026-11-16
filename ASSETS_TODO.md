# Hình vẽ – trạng thái

**Đợt 3 (bản quốc tế): đã xong và đã ghép vào game.**

- 12 món quốc tế: dish-omelette, dish-eggfriedrice, dish-sandwich, dish-ramen, dish-padthai, dish-tacos, dish-tomyum, dish-spaghetti, dish-teriyaki, dish-sweetsour, dish-mapotofu, dish-bibimbap
- Nguyên liệu: ing-tortilla, ing-spaghetti, ing-flour
- Tiền xu: coin-5, coin-10, coin-20, coin-50, coin-bar (100/200/500), ui-coin, ui-coinbag
- Khách vẽ lại: cus-sv (Student), cus-ba (Grandma), cus-chuba (Farmer)
- Trang chủ: tray, food-ramen, food-taco, food-sushi, food-donut, food-burger, bg-kitchen

Ảnh gốc nằm trong `art_inbox/`. Cắt và tách nền bằng `python3 tools/make_round3.py`.
Kiểm tra hình tràn khung: `node tools/audit_images.js`.

Hình cũ mang chi tiết Việt Nam (tiền giấy, phở, bánh mì, bánh tráng, nút cũ…) đã xóa khỏi `assets/`.

## Còn có thể vẽ thêm (không bắt buộc)
- Hình cho các nguyên liệu vẫn đang dùng emoji (xem `ING_IMG` trong `index.html`).
