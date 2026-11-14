# Block Foods – Bếp Việt 🍜

Game xếp khối (block puzzle 8×8). Mỗi khối là một **nguyên liệu** của món ăn Việt. Lấp đầy hàng hoặc cột để "sơ chế" và gom nguyên liệu, gom đủ thì nấu xong món.

Cách chơi: mở `index.html` bằng trình duyệt (điện thoại hoặc máy tính). Toàn bộ game nằm trong một file, không cần cài đặt gì.

## Thiết kế game

### Lối chơi chính
- Bảng 8×8 là **cái thớt gỗ**. Mỗi lượt có 3 khối nguyên liệu ở khay bên dưới.
- Kéo khối thả vào thớt. Khi một hàng hoặc cột đầy thì nó được xóa, và các nguyên liệu trong đó bay vào công thức.
- Đặt xong cả 3 khối thì có 3 khối mới. Hết chỗ đặt thì thua (khối nào không còn chỗ đặt sẽ bị làm mờ).
- Khay luôn có ít nhất 1 khối đặt được tại thời điểm sinh ra, để người chơi không bị kẹt oan.

### Chế độ 🍳 Vào bếp (theo màn)
Mỗi màn là một món ăn, cần gom đủ số lượng từng nguyên liệu:

| # | Món | Nguyên liệu cần |
|---|-----|-----------------|
| 1 | Trứng chiên hành | 🥚16 · 🧅12 |
| 2 | Cơm tấm sườn | 🍚20 · 🍖16 · 🥚12 |
| 3 | Bánh mì thịt | 🥖20 · 🥩16 · 🥒12 · 🌶️10 |
| 4 | Phở bò | 🍜24 · 🥩20 · 🧅16 · 🌿16 |
| 5 | Bún chả | 🍝24 · 🍖20 · 🥬16 · 🌶️12 |
| 6 | Gỏi cuốn | 🫓20 · 🦐20 · 🍝16 · 🥬16 |
| 7 | Canh chua cá | 🐟24 · 🍅20 · 🍍16 · 🌿16 |
| 8 | Bánh xèo | 🌾24 · 🦐20 · 🥩16 · 🌱20 |
| 9 | Cá kho tộ | 🐟28 · 🍯20 · 🧄16 · 🌶️16 |
| 10 | Bún bò Huế | 🍝28 · 🥩24 · 🌶️20 · 🍋16 · 🥬16 |
| 11 | Canh nấm đậu hũ | 🍄24 · 🧈24 · 🧅20 · 🍅16 |
| 12 | Cơm chiên dương châu | 🍚32 · 🥚24 · 🦐20 · 🧅20 · 🥩16 |

- **Nguyên liệu nhiễu:** khoảng 30% khối là nguyên liệu không thuộc món (càng về sau càng nhiều loại). Chúng vẫn xóa được nhưng không được tính vào công thức.
- Khối mới ưu tiên những nguyên liệu còn thiếu nhiều nhất.
- **5 mạng mỗi lần nấu:** thớt hết chỗ thì mất 1 mạng. Thớt được dọn sạch, nguyên liệu đã gom và điểm vẫn giữ nguyên. Hết cả 5 mạng thì phải nấu lại món từ đầu.
- **Sao theo số mạng bị mất:** không mất mạng nào được 3★, mất 1 mạng được 2★, mất từ 2 mạng trở lên được 1★.
- Nấu xong một món thì mở món kế tiếp, và công thức (kèm giới thiệu món) được ghi vào **📖 Sổ công thức**.

### Chế độ ♾️ Chợ vô tận
- Chơi kiểu cổ điển: có 7 nguyên liệu ngẫu nhiên, chơi đến khi hết chỗ, lưu kỷ lục.

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
- Vật phẩm hỗ trợ: 🔪 Dao (xóa 1 ô), 🍳 Chảo (xóa vùng 3×3), 🔄 Đổi khay.
- Ô "đặc biệt" trên thớt: ô đá lạnh cần xóa 2 lần, ô gia vị nhân đôi nguyên liệu.
- Bản đồ vùng miền (Bắc, Trung, Nam) với đặc sản từng tỉnh.
- Nhiệm vụ hằng ngày: "Mâm cơm gia đình" (nấu 3 món trong một màn).
