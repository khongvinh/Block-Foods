# Danh sách hình cần vẽ cho Block Foods

Thay toàn bộ emoji trong game bằng hình vẽ cùng phong cách với bộ hình trang chủ: hoạt hình, viền nâu đậm, bóng nhẹ.

**Quy cách chung**
- Nền trắng hoặc trong suốt đều được, script `tools/make_assets.py` sẽ tự tách nền.
- Hình vuông 1024×1024 trở lên. Vật nằm giữa, chừa lề khoảng 10%.
- Không chèn chữ vào hình, trừ khi có ghi chú riêng.
- Đặt tên file theo cột "Tên file" để mình ghép vào game cho nhanh.

Trạng thái: ✅ đã có · ⬜ chưa có

---

## 1. Nguyên liệu trên thớt (24 hình), quan trọng nhất
Hiện trên mỗi ô của thớt 8×8, trong khay khối và trên thanh công thức. Hình phải **rõ ở cỡ nhỏ (~40px)**: dáng đơn giản, màu tươi, dễ phân biệt với nhau.

| # | Emoji | Nguyên liệu | Tên file | Trạng thái |
|---|---|---|---|---|
| 1 | 🥚 | Trứng | ing-trung | ⬜ |
| 2 | 🧅 | Hành (hành lá + củ hành) | ing-hanh | ⬜ |
| 3 | 🍚 | Cơm (chén cơm) | ing-com | ✅ dùng hình chén cơm |
| 4 | 🍖 | Sườn nướng | ing-suon | ⬜ |
| 5 | 🥒 | Dưa leo | ing-dualeo | ⬜ |
| 6 | 🥖 | Bánh mì (ổ không nhân) | ing-banhmi | ⬜ |
| 7 | 🥩 | Thịt (thịt bò hoặc heo sống) | ing-thit | ⬜ |
| 8 | 🌶️ | Ớt | ing-ot | ✅ dùng hình quả ớt |
| 9 | 🍜 | Bánh phở (vắt bánh phở trắng) | ing-banhpho | ⬜ |
| 10 | 🌿 | Rau thơm (húng, ngò) | ing-rauthom | ⬜ |
| 11 | 🍝 | Bún (vắt bún tươi) | ing-bun | ⬜ |
| 12 | 🥬 | Rau sống (xà lách) | ing-rausong | ⬜ |
| 13 | 🫓 | Bánh tráng | ing-banhtrang | ⬜ |
| 14 | 🦐 | Tôm | ing-tom | ✅ dùng hình con tôm |
| 15 | 🐟 | Cá | ing-ca | ⬜ |
| 16 | 🍅 | Cà chua | ing-cachua | ⬜ |
| 17 | 🍍 | Thơm (dứa) | ing-thom | ⬜ |
| 18 | 🌾 | Bột gạo (bao hoặc chén bột) | ing-botgao | ⬜ |
| 19 | 🌱 | Giá đỗ | ing-gia | ⬜ |
| 20 | 🧄 | Tỏi | ing-toi | ⬜ |
| 21 | 🍯 | Nước màu (chén nước màu caramel) | ing-nuocmau | ⬜ |
| 22 | 🍋 | Chanh (chanh xanh Việt Nam) | ing-chanh | ⬜ |
| 23 | 🍄 | Nấm | ing-nam | ⬜ |
| 24 | 🧈 | Đậu hũ (miếng đậu vàng) | ing-dauhu | ⬜ |

## 2. Món ăn hoàn chỉnh (12 hình)
Hiện ở thẻ khách gọi món, màn nấu, màn thanh toán, Menu quán và thanh tiêu đề. Cỡ lớn (~70–120px) nên vẽ chi tiết được.

| # | Emoji hiện tại | Món | Tên file | Trạng thái |
|---|---|---|---|---|
| 1 | 🍳 | Trứng chiên hành | dish-trungchien | ⬜ |
| 2 | 🍛 | Cơm tấm sườn (đĩa cơm, sườn, chả trứng, đồ chua) | dish-comtam | ⬜ |
| 3 | 🥪 | Bánh mì thịt | dish-banhmi | ✅ dùng hình bánh mì kẹp |
| 4 | 🍜 | Phở bò | dish-pho | ✅ dùng hình tô phở |
| 5 | 🍢 | Bún chả (mẹt bún, chả, chén nước chấm) | dish-buncha | ⬜ |
| 6 | 🌯 | Gỏi cuốn (đĩa cuốn + chén tương) | dish-goicuon | ⬜ |
| 7 | 🥣 | Canh chua cá | dish-canhchua | ⬜ |
| 8 | 🥞 | Bánh xèo | dish-banhxeo | ⬜ |
| 9 | 🍲 | Cá kho tộ (niêu đất) | dish-cakho | ⬜ |
| 10 | 🍜🌶️ | Bún bò Huế (tô bún nước đỏ, sả, chả) | dish-bunbo | ⬜ |
| 11 | 🍵 | Canh nấm đậu hũ | dish-canhnam | ⬜ |
| 12 | 🍚 | Cơm chiên dương châu | dish-comchien | ⬜ |

## 3. Khách hàng (7 hình)
Chân dung từ ngực trở lên, mặt vui vẻ. Nếu được thì vẽ thêm 2 biểu cảm cho mỗi khách: **vui** (5★) và **buồn** (1–2★), đặt tên thêm `-vui` hoặc `-buon`.

| # | Emoji | Khách | Gợi ý tạo hình | Tên file | Trạng thái |
|---|---|---|---|---|---|
| 1 | 👩‍🎓 | Cô sinh viên | Tóc dài, áo sơ mi trắng, balo | cus-sv | ⬜ |
| 2 | 🧔 | Bác xe ôm | Áo khoác, mũ bảo hiểm, râu | cus-xeom | ⬜ |
| 3 | 👨‍💼 | Anh văn phòng | Áo sơ mi, cà vạt, đeo kính | cus-vp | ⬜ |
| 4 | 👵 | Bà ngoại | Tóc bạc búi, áo bà ba | cus-ba | ⬜ |
| 5 | 👱‍♂️ | Anh Tây du lịch | Tóc vàng, nón lá, máy ảnh | cus-tay | ⬜ |
| 6 | 👷 | Chú thợ hồ | Nón bảo hộ, áo lao động | cus-tho | ⬜ |
| 7 | 👧 | Bé Na | Tóc hai bím, áo đầm | cus-na | ⬜ |

## 4. Màn nấu ăn (3 hình)
Các món còn lại dùng hình món ăn ở mục 2.

| Emoji | Dùng cho | Tên file | Trạng thái |
|---|---|---|---|
| 🍽️ | Đĩa trống (bày cơm tấm), cũng dùng làm "đĩa" thay cho mạng chơi | cook-dia | ⬜ |
| 💥🍽️ | Đĩa vỡ (khi thớt đầy) | cook-dia-vo | ⬜ |
| 🥢 | Mẹt tre trống (bày bún chả) | cook-met | ⬜ |
| 🔥 | Ngọn lửa (mini game giữ lửa) | cook-lua | ⬜ |
| 🍳 | Chảo trống (chiên trứng, bánh xèo, cơm chiên) | cook-chao | ⬜ |

## 5. Tiền Việt Nam ở quầy tính tiền (7 hình)
Hiện đang là ô màu có chữ số. Vẽ tờ tiền **cách điệu**, có mệnh giá và màu gần giống thật nhưng **không sao chép y hệt** tờ tiền thật. Hình chữ nhật nằm ngang, tỉ lệ khoảng 2:1, **có ghi số mệnh giá**.

| Mệnh giá | Màu gợi ý | Tên file | Trạng thái |
|---|---|---|---|
| 500.000 | Xanh ngọc | bill-500k | ⬜ |
| 200.000 | Đỏ nâu | bill-200k | ⬜ |
| 100.000 | Xanh lá | bill-100k | ⬜ |
| 50.000 | Hồng tím | bill-50k | ⬜ |
| 20.000 | Xanh dương | bill-20k | ⬜ |
| 10.000 | Vàng nâu | bill-10k | ⬜ |
| 5.000 | Tím | bill-5k | ⬜ |

## 6. Biểu tượng giao diện (khoảng 20 hình, cỡ nhỏ)
Có thể vẽ kiểu icon gỗ giống nút nhạc và nút loa, hoặc kiểu sticker.

| Emoji | Dùng ở đâu | Tên file | Trạng thái |
|---|---|---|---|
| ⭐ ★ | Sao đánh giá (vẽ 2 hình: sao vàng và sao xám) | ui-star, ui-star-off | ⬜ |
| 💰 | Tiền, doanh thu | ui-money | ⬜ |
| 👑 | Kỷ lục | ui-crown | ⬜ |
| 🏆 | Bảng xếp hạng | ui-trophy | ⬜ |
| 🥇 🥈 🥉 | Hạng 1, 2, 3 | ui-medal-1/2/3 | ⬜ |
| 🧾 | Order của khách | ui-order | ⬜ |
| 🔓 🔒 | Mở khóa món, món chưa mở | ui-unlock, ui-lock | ⬜ |
| ✨ 😋 😅 | Chất lượng món: Hoàn hảo, Ngon, Hơi khét | ui-q-perfect/good/burnt | ⬜ |
| 🔪 | Hết chỗ (Chợ vô tận) | ui-knife | ⬜ |
| 😵‍💫 | Vỡ hết đĩa | ui-dizzy | ⬜ |
| 🎉 | Kỷ lục mới | ui-party | ⬜ |
| 🧑‍🍳 | Đầu bếp (màn tạm nghỉ) | ui-chef | ⬜ |
| 🔐 | Màn yêu cầu đăng nhập | ui-login | ⬜ |
| ☁️ | Lưu theo tài khoản | ui-cloud | ⬜ |
| 📶 | Mạng chậm | ui-wifi | ⬜ |
| ‹ ↻ | Nút quay lại, chơi lại (icon gỗ vuông giống nút nhạc) | btn-back, btn-restart | ⬜ |
| ♾️ | Chợ vô tận | đã có trong nút | ✅ |
| ✓ | Dấu tick khi gom đủ nguyên liệu | ui-check | ⬜ |
| 👌 👍 😬 🟢 🟡 🔴 ⚪ | Phản hồi trong mini game nấu | Có thể giữ emoji, không bắt buộc | — |

## 7. Khung và nền (không phải emoji, nhưng làm game đồng bộ hơn)

| Thứ | Dùng ở đâu | Tên file | Trạng thái |
|---|---|---|---|
| Thớt gỗ 8×8 có ô kẻ | Bàn chơi chính | frame-thot | ⬜ |
| Thẻ giấy kem có viền gỗ (dọc) | Thẻ khách gọi món, màn nấu, màn thanh toán, popup | frame-card | ⬜ |
| Bong bóng hội thoại | Lời khách nói | frame-bubble | ⬜ |
| Nền quầy ăn hoặc mặt tiền quán | Màn khách vào quán | bg-quan | ⬜ |
| Nền bếp tối hơn, ít chi tiết | Màn chơi xếp khối, để không rối mắt | bg-game | ⬜ |
| Nút xanh lá, cam, nâu không có chữ | Các nút trong popup (Nhận order, Đưa tiền thối…) | btn-green, btn-orange, btn-brown | ⬜ |

---

### Tổng kết
| Nhóm | Số hình | Ưu tiên |
|---|---|---|
| Nguyên liệu | 24 (đã có 3) | ⭐⭐⭐ |
| Món ăn | 12 (đã có 2) | ⭐⭐⭐ |
| Khách hàng | 7 (×3 nếu có biểu cảm) | ⭐⭐ |
| Màn nấu ăn | 5 | ⭐⭐ |
| Tiền Việt Nam | 7 | ⭐⭐ |
| Icon giao diện | khoảng 25 | ⭐ |
| Khung và nền | khoảng 8 | ⭐ |
