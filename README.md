# Block Foods – Bếp Việt 🍜

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

| # | Món | Nguyên liệu cần |
|---|-----|-----------------|
| 1 | Trứng chiên hành | 🥚16 · 🧅12 |
| 2 | Cơm tấm sườn | 🍚20 · 🍖16 · 🥚12 |
| 3 | Bánh mì thịt | 🥖20 · 🥩16 · 🥒12 · 🌶️10 |
| 4 | Phở bò | 🍜24 · 🥩20 · 🧅16 · 🌿16 |
| 5 | Bún chả 🍢 | 🍝24 · 🍖20 · 🥬16 · 🌶️12 |
| 6 | Gỏi cuốn | 🫓20 · 🦐20 · 🍝16 · 🥬16 |
| 7 | Canh chua cá | 🐟24 · 🍅20 · 🍍16 · 🌿16 |
| 8 | Bánh xèo | 🌾24 · 🦐20 · 🥩16 · 🌱20 |
| 9 | Cá kho tộ | 🐟28 · 🍯20 · 🧄16 · 🌶️16 |
| 10 | Bún bò Huế 🍜🌶️ | 🍝28 · 🥩24 · 🌶️20 · 🍋16 · 🥬16 |
| 11 | Canh nấm đậu hũ | 🍄24 · 🧈24 · 🧅20 · 🍅16 |
| 12 | Cơm chiên dương châu | 🍚32 · 🥚24 · 🦐20 · 🧅20 · 🥩16 |

- **Nguyên liệu nhiễu:** khoảng 30% khối là nguyên liệu không thuộc món (càng về sau càng nhiều loại). Chúng vẫn xóa được nhưng không được tính vào công thức.
- Khối mới ưu tiên những nguyên liệu còn thiếu nhiều nhất.
- **5 cái đĩa 🍽️ mỗi lần nấu:** thớt hết chỗ thì vỡ 1 đĩa. Thớt được dọn sạch, nguyên liệu đã gom và điểm vẫn giữ nguyên. Vỡ hết 5 đĩa thì phải nấu lại món từ đầu.
- **Khách đánh giá 1–5 sao** sau mỗi order, lấy mức thấp nhất trong các điều kiện: nấu hoàn hảo được 5★, món ngon 4★, hơi khét 3★; vỡ 1 đĩa hoặc nấu sai thứ tự còn 2★; vỡ từ 2 đĩa, nấu chậm, thối sai tiền hoặc để khách chờ lâu chỉ được 1★.
- **Menu quán** hiện giá và độ ưa chuộng của từng món (điểm trung bình các đánh giá). Món ít được ưa chuộng sẽ được khách gọi nhiều hơn để bạn gỡ điểm. Bảng xếp hạng có tab **⭐ Đánh giá**, xếp theo tổng số sao khách chấm.
- **Nấu và bán:** gom đủ nguyên liệu thì vào bước nấu (chạm đúng lúc, giữ lửa hoặc xếp đúng thứ tự), rồi mang món ra cho khách và đếm tiền thối. Tiền thu về và tiền boa cộng vào doanh thu của tài khoản. Chi tiết xem [ROADMAP.md](ROADMAP.md).
- Nấu xong một món thì mở món kế tiếp, và công thức (kèm giới thiệu món) được ghi vào **📋 Menu quán**.

### Chế độ ♾️ Chợ vô tận
- Chơi kiểu cổ điển: có 7 nguyên liệu ngẫu nhiên, chơi đến khi hết chỗ, lưu kỷ lục.

### Âm thanh
- **Hiệu ứng và rung (🔊):** đặt khối, xóa hàng, vỡ đĩa, chiên xèo xèo, dao chặt, chuông cửa khi khách vào, đếm tờ tiền, "ka-ching" khi thối đúng, còi báo khi thối sai. Điện thoại Android rung kèm, iPhone không hỗ trợ rung.
- **Nhạc nền (🎵):** giai điệu ngũ cung tiếng gảy kiểu đàn tranh, tạo trực tiếp trong trình duyệt. Phát ở trang chủ, Menu và Bảng xếp hạng, tắt khi vào bếp.
- **Giọng khách (🗣️):** 196 câu thoại thu sẵn trong `voice/`, mỗi khách một giọng riêng (nam/nữ, già/trẻ, giọng Bắc/Trung/Nam). Anh Tây du lịch dùng giọng tiếng Anh đọc tiếng Việt. Tạo lại bằng `python3 tools/make_voices.py` (cần espeak-ng và ffmpeg). Muốn sửa câu thoại thì sửa trong file đó, game sẽ tự khớp chữ với tiếng.

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
