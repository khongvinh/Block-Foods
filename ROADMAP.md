# Lộ trình phát triển Block Foods

Trạng thái: ✅ đã chốt · 🧪 đã làm, chờ chủ game chơi thử và chốt · ⏳ chưa làm

Quy ước: làm lần lượt. Khi chủ game chốt xong một phần thì gợi ý làm phần tiếp theo trong danh sách.

## Đã làm xong

| Nhóm | Nội dung |
|---|---|
| Lối chơi gốc | Thớt 8×8, kéo thả 3 khối, xóa hàng/cột, combo, thưởng "Đồng bộ", 5 cái đĩa (vỡ đĩa khi thớt đầy) |
| Mở quán | Khách vào gọi món (8 khách), món mới mở dần, "Mời khách khác", 12 món |
| Nấu ăn (ý tưởng 1) | 3 mini game: chạm đúng lúc, giữ lửa, xếp thứ tự |
| Bán hàng (ý tưởng 2) | Thối tiền bằng xu và thỏi vàng, thanh kiên nhẫn, tiền boa, doanh thu |
| Đánh giá | Khách chấm 1–5 sao kèm lý do. Menu quán hiện độ ưa chuộng, bấm vào xem danh sách đánh giá |
| Chợ vô tận | Chơi tính điểm, lưu kỷ lục |
| Tài khoản | Bắt buộc đăng nhập, tiến trình lưu theo tài khoản, bảng xếp hạng chung (Chợ vô tận / Đánh giá / Doanh thu) |
| Âm thanh | Nhạc nền vui nhộn, hiệu ứng, rung (giọng nói đã bỏ theo yêu cầu) |
| Hình ảnh | Toàn bộ emoji đã thay bằng hình vẽ, nền gian bếp cho mọi màn, nút gỗ. Đợt 3: 12 món quốc tế, xu, khách vẽ lại |
| Bản quốc tế | 6 ngôn ngữ (English mặc định), món ăn quốc tế, tiền xu, không phát hành tại Việt Nam |

## Chưa làm – chọn hướng tiếp theo

| # | Ý tưởng | Trạng thái |
|---|---------|------------|
| 1 | Nấu nướng sau khi gom đủ nguyên liệu | ✅ Đã chốt |
| 2 | Khách gọi món, giao món và tính tiền thối | ✅ Đã chốt |
| 3 | Nâng cấp quán ăn bằng tiền kiếm được | ⏳ |
| 4 | Đi chợ mỗi sáng | ⏳ |
| 5 | Thử thách hằng ngày và theo sự kiện | ⏳ |
| 6 | Bản đồ ẩm thực thế giới | ⏳ |
| 7 | Chợ: Kho nguyên liệu, nối chợ với quán | ⏳ đề xuất |
| 8 | Chợ: Khách sỉ đặt hàng giữa phiên | ⏳ |
| 9 | Chợ: Ô đặc biệt (tươi, hư, đông lạnh, gia vị) | ⏳ |
| 10 | Chợ: Thử thách chợ hằng ngày, cùng thứ tự khối | ⏳ đề xuất |
| 11 | Chợ: Phiên chợ giới hạn thời gian | ⏳ |
| 12 | Vật phẩm hỗ trợ: dao, chảo, đổi khay, hoàn tác | ⏳ (gộp được với 3) |
| 13 | Bộ sưu tập và huy hiệu | ⏳ |
| 14 | Thách đấu bạn bè | ⏳ |
| 15 | Hình tùy chọn: biểu cảm khách, đồng xu, khung và nền | ⏳ chờ hình |

## 1. Nấu nướng (✅ đã chốt)
Gom đủ nguyên liệu thì vào bước nấu ngắn, khoảng 8–15 giây. Mỗi món dùng một trong ba kiểu:
- **Chạm đúng lúc:** chạm khi kim chạy vào vùng xanh, làm 3 lần, mỗi lần kim nhanh hơn và vùng xanh hẹp hơn.
- **Giữ lửa:** nhấn giữ để tăng lửa, thả ra để hạ lửa, giữ kim trong vùng xanh đang trôi. Kéo dài 8 giây.
- **Xếp đúng thứ tự:** chạm nguyên liệu theo thứ tự trong 10 giây. Chạm sai bị trừ điểm.

Kiểu nấu của từng món nằm trong `COOK_TYPE` (`index.html`). Điểm nấu từ 85 là ✨ Hoàn hảo, từ 55 là 😋 Ngon, dưới 55 là 😅 Hơi khét. Món khét vẫn qua màn, chỉ ít tiền boa hơn.

## 2. Khách gọi món và tính tiền (✅ đã chốt)
- Bấm "Open Shop" thì khách vào gọi món luôn. Món mới mở khóa được gọi trước. Có nút "Mời khách khác" để đổi order. Cùng một vị khách gọi món và trả tiền.
- 8 khách: Student, Delivery rider, Office worker, Grandma, Tourist, Builder, Little Mia, Farmer. Khách nhận xét theo chất lượng món.
- Giá món từ 25 đến 60 xu. Khách trả bằng xu hoặc thỏi vàng (50, 100, 200, 500). Người chơi chạm xu 5, 10, 20, 50 và thỏi 100/200/500 để đếm tiền thối, chạm xu đã đếm để bỏ ra, hoặc bấm "Đếm lại".
- Khách có thanh kiên nhẫn 15 giây, mỗi lần thối sai bị trừ 3 giây. Hết kiên nhẫn thì khách bỏ đi, không boa.
- **Tiền boa:** Hoàn hảo 20% giá món, Ngon 10%, Hơi khét 0%. Thối nhanh boa nhiều hơn, mỗi lần thối sai mất 30% tiền boa.
- Khách chấm 1–5 sao (quy tắc xem README). Menu quán hiện độ ưa chuộng từng món. Doanh thu lưu theo tài khoản, bảng xếp hạng có tab Doanh thu.

## 3. Nâng cấp quán ăn (⏳ đề xuất làm sau khi lên Google Play)
Dùng doanh thu để nâng quán từ xe đẩy (food cart) lên quán nhỏ, rồi quán có mái, rồi nhà hàng. Mua thêm đồ: bếp tốt (thêm 1 đĩa), dao bén (xóa 1 ô), chảo lớn (xóa vùng 3×3), tủ lạnh (giữ 1 khối), đồ trang trí.
Lưu ý kỹ thuật: hiện chỉ lưu tổng doanh thu, con số này chỉ tăng. Khi có chi tiêu phải lưu thêm số tiền đã tiêu.

## 4. Đi chợ mỗi sáng (⏳)
Mỗi ngày có một phiên chợ với giá thay đổi. Nguyên liệu tươi mua ở chợ được tính gấp đôi khi xóa hàng.

## 5. Thử thách hằng ngày và theo sự kiện (⏳)
Bữa tiệc (nấu 3 món trên cùng một thớt), món theo mùa (Halloween, Giáng sinh, Tết Âm lịch), bảng xếp hạng "Hôm nay".

## 6. Bản đồ ẩm thực thế giới (⏳)
Màn chơi chia theo vùng (Á, Âu, Mỹ…), mỗi vùng có nền và nguyên liệu đặc trưng.

## Giai đoạn Google Play (🚧 đang chuẩn bị)
Xem hướng dẫn chi tiết trong [PLAYSTORE.md](PLAYSTORE.md).
