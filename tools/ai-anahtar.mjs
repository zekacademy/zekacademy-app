/* GitHub sırrındaki Anthropic API anahtarını Firestore system/ai belgesine yazar (istemciler okuyamaz). Anahtarı asla ekrana yazmaz. */
import { createRequire } from "node:module";
const require = createRequire(new URL("../functions/package.json", import.meta.url));
const { initializeApp } = require("firebase-admin/app");
const { getFirestore } = require("firebase-admin/firestore");
const anahtar = (process.env.ANTHROPIC_API_KEY || "").trim();
if (!anahtar) { console.log("::notice::ANTHROPIC_API_KEY sırrı yok; Soru Çözüm anahtarı yazılmadı."); process.exit(0); }
if (!anahtar.startsWith("sk-ant-")) { console.log("::error::ANTHROPIC_API_KEY beklenen biçimde değil (sk-ant- ile başlamalı)."); process.exit(1); }
initializeApp({ projectId: process.env.PROJE });
await getFirestore().doc("system/ai").set({ anahtar, guncelleme: new Date().toISOString() }, { merge: true });
console.log("::notice::Soru Çözüm API anahtarı sunucuya yazıldı (son 4 hane: " + anahtar.slice(-4) + ").");
