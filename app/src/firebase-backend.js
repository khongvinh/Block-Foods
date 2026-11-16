// Nơi lưu điểm cho bản app. Game gọi BF_BACKEND.init() và dùng db/user giống bản claude.ai:
//   db.collection("scores").limit(n).onSnapshot(...), db.collection("scores").doc(id).set(...)
// Người chơi đăng nhập ẩn danh (khách), không cần tài khoản Google.
window.BF_BACKEND = (function () {
  var cfg = window.FIREBASE_CONFIG;
  if (!cfg || !cfg.apiKey || !window.firebase) return null; // chưa cấu hình: chơi offline
  return {
    kind: "firebase",
    init: async function () {
      if (!firebase.apps.length) firebase.initializeApp(cfg);
      var auth = firebase.auth();
      var u = await new Promise(function (res) {
        var off = auth.onAuthStateChanged(function (x) { off(); res(x); });
      });
      if (!u) u = (await auth.signInAnonymously()).user;
      var db = firebase.firestore();
      return {
        db: db,
        user: {
          id: async function () { return u.uid; },
          me: async function () { return {}; },
          can: async function () { return true; },
          profiles: async function () { return {}; } // tên lấy từ trường nk trong bảng điểm
        }
      };
    }
  };
})();
