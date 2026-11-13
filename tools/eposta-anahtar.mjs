/* GitHub sırlarındaki Gmail adresi ve uygulama şifresini Firestore system/eposta belgesine yazar (istemciler okuyamaz). Şifreyi asla ekrana yazmaz. */
import { createRequire } from "node:module";
const require = createRequire(new URL("../functions/package.json", import.meta.url));
const { initializeApp } = require("firebase-admin/app");
const { getFirestore } = require("firebase-admin/firestore");
const kullanici = (process.env.GMAIL_USER || "").trim(), sifre = (process.env.GMAIL_APP_PASSWORD || "").replace(/\s+/g, "");
if (!kullanici || !sifre) { console.log("::notice::GMAIL_USER / GMAIL_APP_PASSWORD sırrı yok; veli e-postası hesabı yazılmadı."); process.exit(0); }
if (!/^[^\s@]+@[^\s@]+$/.test(kullanici) || sifre.length !== 16) { console.log("::error::GMAIL_USER bir e-posta adresi, GMAIL_APP_PASSWORD 16 harfli uygulama şifresi olmalı."); process.exit(1); }
initializeApp({ projectId: process.env.PROJE });
await getFirestore().doc("system/eposta").set({ kullanici, sifre, guncelleme: new Date().toISOString() }, { merge: true });
console.log("::notice::Veli e-postası hesabı sunucuya yazıldı (" + kullanici + ").");
