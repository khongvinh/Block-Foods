# Block Foods 🍜

Game xếp khối (block puzzle 8×8). Mỗi khối là một **nguyên liệu** của món ăn Việt. Lấp đầy hàng hoặc cột để "sơ chế" và gom nguyên liệu, gom đủ thì nấu xong món.

Cách chơi: mở `index.html` bằng trình duyệt (điện thoại hoặc máy tính). Toàn bộ game nằm trong một file, không cần cài đặt gì.

## Thiết kế game

### Lối chơi chính
- Bảng 8×8 là **cái thớt gỗ**. Mỗi lượt có 3 khối nguyên liệu ở khay bên dưới.
- Kéo khối thả vào thớt. Khi một hàng hoặc cột đầy thì nó được xóa, và các nguyên liệu trong đó bay vào công thức.
- Đặt xong cả 3 khối thì có 3 khối mới. Hết chỗ đặt thì thua (khối nào không còn chỗ đặt sẽ bị làm mờ).
- Khay luôn có ít nhất 1 khối đặt được tại thời điểm sinh ra, để người chơi không bị kẹt oan.

### Chế độ 🍳 Mở quán
Không có màn chọn món. Mỗi lượt có một khách vào quán gọi món. Món mới mở khóa thì khách sẽ gọi món đó trước, sau đó khách ưu tiên gọi những món còn ít sao. Có thể bấm "Mời khách khác" để đổi order. Cùng một vị khách sẽ gọi món và trả tiền. Mỗi món cần gom đủ số lượng từng nguyên liệu:

| # | Món (EN) | Nguyên liệu cần |
|---|-----|-----------------|
| 1 | Green Onion Omelette | Trứng 16 · Hành lá 12 |
| 2 | Egg Fried Rice | Cơm 20 · Trứng 16 · Hành lá 12 |
| 3 | Grilled Meat Sandwich | Baguette 20 · Thịt 16 · Dưa leo 12 · Ớt 10 |
| 4 | Ramen | Mì 24 · Thịt 20 · Trứng 16 · Hành lá 16 |
| 5 | Pad Thai | Sợi gạo 24 · Tôm 20 · Giá 16 · Đậu hũ 16 · Chanh 12 |
| 6 | Tacos | Tortilla 20 · Thịt 20 · Cà chua 16 · Xà lách 16 · Ớt 12 |
| 7 | Tom Yum Soup | Tôm 24 · Nấm 20 · Chanh 16 · Ớt 16 · Cà chua 12 |
| 8 | Spaghetti with Meat Sauce | Mì Ý 28 · Thịt 20 · Cà chua 20 · Hành lá 16 · Tỏi 12 |
| 9 | Teriyaki Fish | Cá 28 · Nước tương 20 · Tỏi 16 · Cơm 16 |
| 10 | Sweet & Sour Stir-fry | Sườn 28 · Thơm 20 · Cà chua 20 · Hành lá 16 |
| 11 | Mapo Tofu | Đậu hũ 28 · Thịt 20 · Ớt 20 · Tỏi 16 · Hành lá 12 |
| 12 | Bibimbap | Cơm 32 · Trứng 24 · Giá 20 · Thịt 20 · Xà lách 16 · Ớt 12 |

- **Nguyên liệu nhiễu:** khoảng 30% khối là nguyên liệu không thuộc món (càng về sau càng nhiều loại). Chúng vẫn xóa được nhưng không được tính vào công thức.
- Khối mới ưu tiên những nguyên liệu còn thiếu nhiều nhất.
- **5 cái đĩa 🍽️ mỗi lần nấu:** thớt hết chỗ thì vỡ 1 đĩa. Thớt được dọn sạch, nguyên liệu đã gom và điểm vẫn giữ nguyên. Vỡ hết 5 đĩa thì phải nấu lại món từ đầu.
- **Khách đánh giá 1–5 sao** sau mỗi order, lấy mức thấp nhất trong các điều kiện: nấu hoàn hảo được 5★, món ngon 4★, hơi khét 3★; vỡ 1 đĩa hoặc nấu sai thứ tự còn 2★; vỡ từ 2 đĩa, nấu chậm, thối sai tiền hoặc để khách chờ lâu chỉ được 1★.
- **Menu quán** hiện giá và độ ưa chuộng của từng món (điểm trung bình các đánh giá). Món ít được ưa chuộng sẽ được khách gọi nhiều hơn để bạn gỡ điểm. Bảng xếp hạng có tab **⭐ Đánh giá**, xếp theo tổng số sao khách chấm.
- **Nấu và bán:** gom đủ nguyên liệu thì vào bước nấu (chạm đúng lúc, giữ lửa hoặc xếp đúng thứ tự), rồi mang món ra cho khách và đếm tiền thối. Tiền thu về và tiền boa cộng vào doanh thu của tài khoản. Chi tiết xem [ROADMAP.md](ROADMAP.md).
- Nấu xong một món thì mở món kế tiếp, và công thức (kèm giới thiệu món) được ghi vào **📋 Menu quán**.

### Chế độ ♾️ Chợ vô tận
- Chơi kiểu cổ điển: có 7 nguyên liệu ngẫu nhiên, chơi đến khi hết chỗ, lưu kỷ lục.

### Ngôn ngữ và tiền
- 6 ngôn ngữ: English (mặc định), Español, Português (Brasil), Bahasa Indonesia, हिन्दी, Tiếng Việt. Lần đầu mở, game tự chọn theo ngôn ngữ của máy. Đổi bằng nút 🌐 ở trang chủ.
- Toàn bộ chữ nằm trong `i18n.js`. Muốn thêm ngôn ngữ thì thêm một cột vào file này.
- Tiền là **xu** (có hình đồng xu, thỏi vàng) (5, 10, 20, 50 xu và thỏi 100, 200, 500). Game không dùng tiền thật của quốc gia nào.
- Game **không phát hành tại Việt Nam**. Nội dung không dùng món ăn, tiền hay hình ảnh đặc trưng Việt Nam (hình đã vẽ lại toàn bộ ở đợt 3, xem `ASSETS_TODO.md`).

### Âm thanh
- **Hiệu ứng và rung (🔊):** đặt khối, xóa hàng, vỡ đĩa, chiên xèo xèo, dao chặt, chuông cửa khi khách vào, đếm tờ tiền, "ka-ching" khi thối đúng, còi báo khi thối sai. Điện thoại Android rung kèm, iPhone không hỗ trợ rung.
- **Nhạc nền (🎵):** nhạc bếp vui nhộn (Đô trưởng, nhịp 150, có trống, vỗ tay, hi-hat, hợp âm nảy), tạo trực tiếp trong trình duyệt.

### Tính điểm
- Đặt khối: +1 điểm mỗi ô.
- Xóa n đường (hàng + cột) cùng lúc: +10·n² và +1 điểm mỗi ô bị xóa.
- **Combo:** xóa liên tiếp mà không cách quá 2 lượt thì được +10 cho mỗi bậc combo.
- **Đồng bộ:** một hàng hoặc cột chỉ gồm một loại nguyên liệu được +40.

### Phong cách
- Nền gỗ, thớt gỗ tối màu. Mỗi ô nguyên liệu có màu riêng kèm emoji để dễ nhận ra.
- Có hiệu ứng nguyên liệu bay vào công thức, chữ khen kiểu Việt ("Ngon bá cháy!", "Đỉnh của chóp!"), và âm thanh tạo bằng WebAudio (có thể tắt).
- Tiến độ, số sao, kỷ lục và cài đặt âm thanh lưu trong `localStorage`.

## Hướng phát triển
Xem [ROADMAP.md](ROADMAP.md).

## Bản Android (Google Play)
- Thư mục `app/` đóng gói `index.html` thành app Android bằng Capacitor. Bản app chơi như khách (không cần đăng nhập), bảng xếp hạng chạy bằng Firebase.
- Hướng dẫn đầy đủ: [PLAYSTORE.md](PLAYSTORE.md). Nội dung trang cửa hàng: [STORE_LISTING.md](STORE_LISTING.md). Chính sách quyền riêng tư: `privacy.html`.
