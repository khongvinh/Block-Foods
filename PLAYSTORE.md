# Đưa Block Foods lên Google Play

Bản web (claude.ai) và bản Android dùng **chung một file game** `index.html`. Thư mục `app/` đóng gói file đó thành app Android bằng Capacitor.

## 1. Đã làm sẵn trong code

| Việc | Ở đâu |
|---|---|
| Chơi ngay như **khách**, không bắt đăng nhập (bản claude.ai vẫn đăng nhập như cũ) | `index.html` → `startAppBackend` |
| Bảng xếp hạng chạy bằng **Firebase** (đăng nhập ẩn danh + Firestore) | `app/src/firebase-backend.js` |
| Chưa có cấu hình Firebase hoặc mất mạng thì vẫn chơi bình thường, chỉ ẩn bảng xếp hạng | `app/src/firebase-config.js` |
| **Tên đầu bếp tự sinh** (vd. "Chef Tomato #1234"), bấm 🎲 để đổi. Không cho gõ tên tự do nên không dính chính sách nội dung do người dùng tạo (UGC) | `index.html` → `newNick`, `nickModal` |
| Nút **"Xóa tôi khỏi bảng xếp hạng"** (Google yêu cầu có cách xóa dữ liệu) | Bấm vào tên ở trang chủ |
| **Nút Back** của Android: đóng hộp thoại, tạm dừng ván, về trang chủ, thoát app | `index.html` cuối file |
| Tắt âm thanh khi ẩn app, bật lại khi quay lại | `visibilitychange` |
| Khóa màn hình dọc, quyền rung, icon app, màn hình chờ | `app/android/...`, `tools/make_app_icons.py` |
| Luật bảo mật Firestore (mỗi người chỉ sửa được điểm của mình, chặn số liệu vô lý) | `app/firestore.rules` |
| Trang chính sách quyền riêng tư (tiếng Anh) | `privacy.html` |
| Icon 512, ảnh bìa 1024×500, 5 ảnh chụp màn hình 1080×2160 | `store/` |
| Nội dung trang cửa hàng (mô tả ngắn, mô tả đầy đủ, bảng An toàn dữ liệu) | `STORE_LISTING.md` |

Đã kiểm tra tự động: bản app chạy offline, bản app có bảng xếp hạng (dùng máy chủ giả), đổi tên, xóa khỏi bảng xếp hạng, và toàn bộ test cũ của bản web.

## 2. Việc anh cần tự làm (cần tài khoản của anh)

### Bước 1. Tài khoản Google Play Console
- Đăng ký tại play.google.com/console, phí **25 USD một lần**, xác minh danh tính (CCCD/hộ chiếu).
- Tài khoản **cá nhân** mới phải chạy **thử nghiệm kín với ít nhất 12 người trong 14 ngày** liên tục trước khi được phát hành công khai. Nên gom sẵn 12+ người (bạn bè, người thân) có Gmail và điện thoại Android.
- Tài khoản **tổ chức** (cần mã số D-U-N-S) không bị yêu cầu này.

### Bước 2. Tạo Firebase (miễn phí, gói Spark là đủ lúc đầu)
1. Vào console.firebase.google.com → **Add project** → đặt tên `block-foods` (tắt Google Analytics cho gọn).
2. **Build → Authentication → Get started → Sign-in method → Anonymous → Enable.**
3. **Build → Firestore Database → Create database** → chọn vùng gần người chơi (vd. `asia-southeast1` hoặc `us-central1`) → **Production mode**.
4. Tab **Rules**: xóa hết, dán nội dung file `app/firestore.rules` → **Publish**.
5. **Project settings (bánh răng) → Your apps → biểu tượng `</>` (Web)** → đặt tên → **Register app**. Copy khối `firebaseConfig` và dán vào `app/src/firebase-config.js` (thay dòng `window.FIREBASE_CONFIG = null;`).

Cấu hình Firebase web không phải mật khẩu, để trong code là bình thường. Dữ liệu được bảo vệ bằng luật ở bước 4.

### Bước 3. Đổi mã app (chỉ làm trước lần tải lên đầu tiên)
Mã app hiện là `com.blockfoods.game`. Mã này **không đổi được sau khi đã tải lên Play** và phải không trùng với app nào khác. Nên đổi thành mã riêng, vd. `com.<tên-anh>.blockfoods`. Báo tôi mã anh chọn, tôi đổi ở mọi chỗ cần đổi.

### Bước 4. Build file AAB trên máy tính
Cần: Node.js 22+, **Android Studio** (bản mới nhất).
```bash
git clone <repo> && cd Block-Foods/app
npm install
npm run sync          # tạo www/ từ index.html rồi chép vào project Android
npm run open          # mở Android Studio
```
Trong Android Studio: **Build → Generate Signed App Bundle or APK → Android App Bundle → Create new keystore**.
- **Giữ file keystore và mật khẩu thật kỹ** (sao lưu 2 nơi). Mất là không cập nhật app được nữa. Khi tải lên Play, bật **Play App Signing** (mặc định) để Google giữ khóa ký chính.
- File ra: `app/android/app/release/app-release.aab`.
- Mỗi lần cập nhật: tăng `versionCode` (1, 2, 3…) và `versionName` trong `app/android/app/build.gradle`.

Muốn thử nhanh trên điện thoại: cắm điện thoại (bật USB debugging) rồi bấm ▶ Run trong Android Studio.

### Bước 5. Điền thông tin trên Play Console
- **Store listing:** chép từ `STORE_LISTING.md`, tải lên hình trong `store/`.
- **Privacy policy:** cần một đường link công khai. Cách dễ nhất: bật **GitHub Pages** cho repo, link sẽ là `https://<user>.github.io/Block-Foods/privacy.html`. Nhớ sửa các chỗ `[DATE]`, `[DEVELOPER NAME]`, `[CONTACT EMAIL]` trong file.
- **App content:**
  - Ads: **No**. In-app purchases: không có.
  - Target audience: đề xuất chọn **13+** (13–15, 16–17, 18+). Nếu chọn dưới 13 tuổi, app phải tuân theo chính sách Families, kèm nhiều yêu cầu thêm.
  - Content rating (IARC): game giải đố, không bạo lực, không cờ bạc, có bảng xếp hạng nhưng không chat → thường ra **Everyone / PEGI 3**.
  - Data safety: điền theo bảng trong `STORE_LISTING.md`.
- **Countries / regions:** chọn tất cả rồi **bỏ Việt Nam** (theo quyết định không phát hành tại VN).
- **Release:** Internal testing (thử nhanh) → **Closed testing** (12 người × 14 ngày) → Apply for production.

## 3. Nên làm thêm (tôi làm được khi anh muốn)
1. **Icon chính thức:** icon hiện là tô ramen trên nền cam (tạm). Có thể vẽ icon riêng 1024×1024 rồi chạy lại `python3 tools/make_app_icons.py`.
2. **Đăng nhập Google để giữ tiến trình khi đổi máy:** hiện tiến trình lưu trên máy và điểm lưu theo mã khách. Gỡ app là mất tiến trình (điểm cũ trên bảng xếp hạng vẫn còn).
3. **Tối ưu bảng xếp hạng khi đông người:** hiện mỗi lần mở app đọc tối đa 1.000 dòng điểm. Gói miễn phí cho 50.000 lượt đọc/ngày, tức khoảng 50 lần mở app/ngày khi bảng đã đủ 1.000 người. Khi đông hơn nên đổi sang chỉ đọc top 100 của từng tab.
4. **Firebase App Check:** chặn người dùng gửi điểm giả bằng công cụ bên ngoài.
5. **Dịch trang cửa hàng** sang 5 ngôn ngữ còn lại.
6. **Build APK ngay trên máy chủ này:** cần mở quyền truy cập `dl.google.com` (tải Android SDK). Khi đó tôi build được file APK để anh cài thử lên điện thoại mà không cần Android Studio.
