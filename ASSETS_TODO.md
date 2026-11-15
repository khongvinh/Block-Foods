# Hình cần vẽ thêm – Đợt 2

> ✅ **Đã nhận đợt 2:** đủ 10 nguyên liệu, tờ 10k, món khét, nút chơi lại, 4 nút trơn. Toàn bộ mục A, B1–B3 và C (cách 1) đã xong.
> Còn lại là phần **tùy chọn**: B4–B8 (biểu cảm khách, đồng xu, đồng hồ cát, hơi nóng) và mục D (khung, nền).

Đợt 1 đã ghép **66 hình** vào game: 14 nguyên liệu, 12 món ăn, 8 khách, 5 đồ nấu, 6 tờ tiền, 21 icon, cùng logo, 4 nút trang chủ, nền gian bếp và 5 món trang trí.
Dưới đây là những thứ **còn thiếu**. Chỗ nào chưa có hình, game tạm dùng emoji hoặc nút vẽ bằng CSS.

**Quy cách:** cùng phong cách hoạt hình viền nâu. Gửi dạng **bảng hình** như đợt 1 là được: mỗi hình một ô, nền kem hoặc trắng, có chữ chú thích bên dưới. Mình dùng `tools/cut_sheet.py` cắt ra từng hình.

---

## A. Nguyên liệu còn thiếu (10 hình), ưu tiên cao nhất
Hiện trên ô thớt cỡ nhỏ, nên vẽ dáng đơn giản, màu rõ.

| # | Đang dùng | Nguyên liệu | Gợi ý |
|---|---|---|---|
| 1 | 🍖 | Sườn nướng | Miếng sườn cốt lết nướng vàng |
| 2 | 🥩 | Thịt | Miếng thịt bò hoặc heo tươi, thớ đỏ hồng |
| 3 | 🍝 | Bún | Vắt bún trắng, sợi tròn nhỏ (khác vắt bánh phở dẹt) |
| 4 | 🥬 | Rau sống | Bó xà lách và rau thơm |
| 5 | 🐟 | Cá | Con cá lóc hoặc cá basa |
| 6 | 🍅 | Cà chua | Quả cà chua đỏ, có cuống |
| 7 | 🌱 | Giá đỗ | Nắm giá trắng, mầm vàng |
| 8 | 🧄 | Tỏi | Củ tỏi trắng |
| 9 | 🍄 | Nấm | Cụm nấm rơm hoặc nấm đông cô |
| 10 | 🧈 | Đậu hũ | Miếng đậu hũ trắng hoặc vàng |

## B. Tiền và icon còn thiếu (8 hình)

| # | Đang dùng | Hình | Ghi chú |
|---|---|---|---|
| 1 | ô màu vàng | **Tờ 10.000đ** | Màu vàng nâu, ghi "10k". Tờ trong đợt 1 bị ghi "100k" |
| 2 | 😅 | **Món hơi khét** | Mặt cười méo hoặc chảo bốc khói đen |
| 3 | ↻ | **Nút chơi lại** | Icon gỗ vuông, mũi tên xoay tròn, cùng kiểu nút nhạc |
| 4 | — | **Mặt khách vui** | Không bắt buộc. 8 khách × biểu cảm vui, dùng khi khách chấm 5★ |
| 5 | — | **Mặt khách buồn** | Không bắt buộc. 8 khách × biểu cảm buồn, dùng khi khách chấm 1–2★ |
| 6 | — | **Đồng xu / tiền boa** | Bay lên khi khách boa |
| 7 | — | **Đồng hồ cát** | Cho thanh kiên nhẫn của khách |
| 8 | — | **Hơi nóng bốc lên** | Làn khói trắng, dùng khi món nấu xong |

## C. Nút chức năng (nút chữ trong các hộp thoại)
Hiện là nút vẽ bằng CSS. Có **2 cách** làm hình:

**Cách 1 (nên dùng): 4 nút trơn không chữ.** Mình tự chèn chữ lên, nên dùng được cho mọi nút và sau này đổi chữ cũng không cần vẽ lại.

| Nút trơn | Màu | Dùng cho |
|---|---|---|
| btn-plain-green | Xanh lá (giống nút Chợ vô tận nhưng không chữ, không ∞) | Hành động chính: Nhận order, Mang ra cho khách, Đưa tiền thối, Mời khách tiếp theo, Dọn thớt nấu tiếp, Nấu tiếp, Chơi lại, Nấu lại từ đầu |
| btn-plain-orange | Cam đỏ (giống nút Mở quán, không chữ) | Chạm!, Giữ để tăng lửa, Bảng xếp hạng, Mời khách khác |
| btn-plain-brown | Nâu gỗ (giống nút Menu quán, không chữ) | Về quán, Thoát, Đếm lại, Bỏ order về quán |
| btn-plain-gold | Vàng (giống nút Bảng xếp hạng, không chữ) | Tab đang chọn trên bảng xếp hạng |

**Cách 2: nút có chữ sẵn** (như 4 nút trang chủ). Cần vẽ đủ **17 nút**:

| Màu | Nút |
|---|---|
| Xanh lá | Nhận order › · Mang ra cho khách › · Đưa tiền thối · Mời khách tiếp theo › · Dọn thớt, nấu tiếp · Nấu tiếp · Chơi lại · Nấu lại từ đầu · Chơi tạm, đồng bộ sau |
| Cam | Chạm! · Giữ để tăng lửa · Mời khách khác · Xem bảng xếp hạng |
| Nâu | Về quán · Thoát · Đếm lại · Bỏ order, về quán |

## D. Khung và nền (6 hình, không bắt buộc nhưng giúp game đồng bộ)

| # | Hình | Dùng ở đâu |
|---|---|---|
| 1 | **Thớt gỗ vuông** (mặt thớt tròn góc, có vân gỗ, không kẻ ô) | Bàn chơi 8×8. Mình tự kẻ ô lên |
| 2 | **Thẻ giấy kem có viền gỗ** (đứng dọc, trống) | Thẻ khách gọi món, màn nấu, màn tính tiền, các hộp thoại |
| 3 | **Bong bóng hội thoại** (trống, có đuôi chỉ sang trái) | Lời khách nói |
| 4 | **Ô nguyên liệu trên thanh công thức** (ô vuông nhỏ giấy kem) | Thanh đếm nguyên liệu ở đầu màn chơi |
| 5 | **Tab gỗ** (một tấm sáng và một tấm tối) | Tab Chợ vô tận / Đánh giá / Doanh thu |
| 6 | **Bảng điểm** (2 khung: tím cho Kỷ lục, nâu viền vàng cho Điểm) | Đầu màn Chợ vô tận |

---

### Tổng cộng
| Nhóm | Số hình | Ưu tiên |
|---|---|---|
| A. Nguyên liệu | 10 | ⭐⭐⭐ |
| B. Tiền và icon | 4 bắt buộc + 4 tùy chọn | ⭐⭐ |
| C. Nút chức năng | 4 nút trơn (hoặc 17 nút có chữ) | ⭐⭐ |
| D. Khung và nền | 6 | ⭐ |
