// Tạo thư mục www/ cho Capacitor từ bản web ở thư mục gốc.
import { build } from "esbuild";
import fs from "node:fs";
import path from "node:path";

const ROOT = path.resolve(import.meta.dirname, "..");
const WWW = path.resolve(import.meta.dirname, "www");
fs.rmSync(WWW, { recursive: true, force: true });
fs.mkdirSync(WWW, { recursive: true });

// 1. Hình và chữ
fs.cpSync(path.join(ROOT, "assets"), path.join(WWW, "assets"), { recursive: true });
fs.copyFileSync(path.join(ROOT, "i18n.js"), path.join(WWW, "i18n.js"));

// 2. Gói Firebase + Capacitor App
await build({
  entryPoints: [path.join(import.meta.dirname, "src/app-entry.js")],
  bundle: true, minify: true, format: "iife", target: "es2020",
  outfile: path.join(WWW, "app.bundle.js"), legalComments: "none"
});
for (const f of ["firebase-config.js", "firebase-backend.js"])
  fs.copyFileSync(path.join(import.meta.dirname, "src", f), path.join(WWW, f));

// 3. index.html: nạp các file trên trước script của game
let html = fs.readFileSync(path.join(ROOT, "index.html"), "utf8");
const tag = '<script src="i18n.js"></script>';
if (!html.includes(tag)) throw new Error("index.html: không tìm thấy " + tag);
html = html.replace(tag,
  '<script src="app.bundle.js"></script>\n<script src="firebase-config.js"></script>\n<script src="firebase-backend.js"></script>\n' + tag);
html = html.replace(/<meta name="viewport"[^>]*>/,
  '<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no,viewport-fit=cover">');
fs.writeFileSync(path.join(WWW, "index.html"), html);

// 4. Chỉ giữ hình mà game thật sự dùng
const used = new Set();
const src = html + fs.readFileSync(path.join(ROOT, "i18n.js"), "utf8");
for (const f of fs.readdirSync(path.join(WWW, "assets"))) {
  const n = f.replace(/\.webp$/, "");
  if (src.includes(n) || n.startsWith("cus-") || n.startsWith("ing-") || n.startsWith("food-")) used.add(f);
  else fs.rmSync(path.join(WWW, "assets", f));
}
const kb = d => Math.round(fs.readdirSync(d, { recursive: true }).reduce((a, f) => {
  const p = path.join(d, f); return a + (fs.statSync(p).isFile() ? fs.statSync(p).size : 0); }, 0) / 1024);
console.log(`www/ xong: ${used.size} hình, tổng ${kb(WWW)} KB`);
