# Hình cần vẽ – Đợt 3 (bản quốc tế)

Game đã chuyển sang **món ăn quốc tế, tiền xu, 6 ngôn ngữ**. Những hình dưới đây cần vẽ mới hoặc vẽ lại để bỏ hết chi tiết đặc trưng Việt Nam. Trong lúc chờ, game tạm dùng emoji, hình cũ có dáng chung chung, hoặc đồng xu vẽ bằng CSS.

**Quy cách:** giống đợt 1 và 2 (hoạt hình, viền nâu, nền trắng). **Không vẽ chữ vào hình**, vì game có 6 ngôn ngữ và chữ được chèn bằng code.

## A. 12 món ăn (ưu tiên cao nhất)
| # | Tên file | Món | Gợi ý hình | Đang tạm dùng |
|---|---|---|---|---|
| 1 | dish-omelette | Green Onion Omelette | Đĩa trứng chiên vàng có hành lá | Tranh trứng chiên cũ |
| 2 | dish-eggfriedrice | Egg Fried Rice | Đĩa cơm chiên trứng, hành lá | Tranh cơm chiên cũ |
| 3 | dish-sandwich | Grilled Meat Sandwich | Bánh baguette kẹp thịt nướng, dưa leo | Tranh bánh mì cũ |
| 4 | dish-ramen | Ramen | Tô mì, lát thịt, trứng lòng đào, hành, rong biển | Tranh tô phở cũ |
| 5 | dish-padthai | Pad Thai | Đĩa sợi gạo xào, tôm, giá, lát chanh | 🥡 |
| 6 | dish-tacos | Tacos | 2–3 cái tacos kẹp thịt, cà chua, xà lách | 🌮 |
| 7 | dish-tomyum | Tom Yum Soup | Tô súp đỏ cam, tôm, nấm, lá chanh | Tranh canh chua cũ |
| 8 | dish-spaghetti | Spaghetti with Meat Sauce | Đĩa mì Ý sốt thịt cà chua | 🍝 |
| 9 | dish-teriyaki | Teriyaki Fish | Miếng cá phủ sốt bóng, chén cơm | 🍱 |
| 10 | dish-sweetsour | Sweet & Sour Stir-fry | Đĩa sườn xào với thơm, cà chua, hành | 🍖 |
| 11 | dish-mapotofu | Mapo Tofu | Đĩa đậu hũ sốt đỏ cay, thịt băm | 🥘 |
| 12 | dish-bibimbap | Bibimbap | Tô cơm có trứng, thịt, giá, rau xếp theo ô màu | 🥗 |

## B. Nguyên liệu (3 hình)
| Tên file | Nguyên liệu | Ghi chú |
|---|---|---|
| ing-tortilla | Tortilla | Chồng bánh tortilla vàng nhạt có đốm nướng. Đang tạm dùng hình bánh tráng |
| ing-spaghetti | Spaghetti | Bó mì Ý vàng (khác mì ramen trắng). Đang dùng 🍝 |
| ing-flour | Flour | Bao bột **không có chữ "RICE"** (không bắt buộc, chỉ dùng ở Chợ vô tận) |

## C. Tiền xu (5–7 hình)
Đang vẽ bằng CSS: xu đồng (5), xu bạc (10), xu vàng (20, 50), thỏi vàng (100, 200, 500).
| Tên file | Hình |
|---|---|
| coin-5, coin-10, coin-20, coin-50 | Đồng xu đồng, bạc, vàng, vàng lớn. **Để trống giữa**, game tự ghi số |
| coin-bar | Thỏi vàng, dùng chung cho 100/200/500 |
| ui-coin | Icon 1 đồng xu nhỏ, thay cho 🪙 cạnh giá tiền |
| ui-coinbag | Túi xu **không có ký hiệu $**, thay hình túi tiền hiện tại |

## D. Khách hàng (vẽ lại 3 hình)
| Tên file | Khách mới | Vấn đề hình cũ |
|---|---|---|
| cus-sv | Student | Đang mặc đồng phục, quàng khăn đỏ kiểu Việt Nam. Vẽ áo hoodie, balo |
| cus-ba | Grandma | Áo bà ba. Vẽ áo len, kính |
| cus-chuba | Farmer | Nón lá. Vẽ mũ rơm, áo yếm |
| cus-xeom | Delivery rider | Có thể giữ hình (mũ bảo hiểm, áo khoác giao hàng) |

## E. Trang chủ
| Tên file | Hình | Ghi chú |
|---|---|---|
| tray | Khay gỗ bày 5 món quốc tế | Mẹt tre hiện tại có tô phở và bánh mì |
| food-* (5 hình bay) | Ví dụ ramen, tacos, sandwich, spaghetti, sushi… | Đang dùng phở, bánh mì, tôm, ớt, cơm |
| bg-kitchen | Nền bếp (không bắt buộc) | Bếp quê hiện tại khá chung chung, có thể giữ |

## Đã xử lý bằng code, không cần vẽ
- Logo đã bỏ dòng chữ tiếng Việt. Dòng giới thiệu nằm trên tấm ván riêng và đổi theo ngôn ngữ.
- 4 nút trang chủ dùng nút trơn, chữ đổi theo ngôn ngữ.
