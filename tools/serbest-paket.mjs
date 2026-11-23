/* Tek seferlik (koçun isteği, 23 Kasım 2026): "Serbest Paket" ekle — sabit ücret yok, öğrenci başı tutar ödeme planından elle girilir.
   Var olan paketlere ve ödemelere dokunulmaz. Bir kez çalışır (system/temizlik işaretiyle kilitlenir). */
import { createRequire } from "node:module";
const require = createRequire(new URL("../functions/package.json", import.meta.url));
const { initializeApp } = require("firebase-admin/app");
const { getFirestore } = require("firebase-admin/firestore");
const ANAHTAR = "serbest-paket-2026-11-23";
const db = getFirestore(initializeApp({ projectId: process.env.PROJE }, "serbest")), isaret = db.doc("system/temizlik");
if (((await isaret.get()).data() || {})[ANAHTAR]) { console.log("::notice::Serbest paket daha önce eklenmiş; atlandı."); process.exit(0); }
const ref = db.doc("settings/main"), ayar = (await ref.get()).data() || {};
const DEF = [{ k: "super", n: "Premium Koçluk", tur: "seans", fiyat: 6900 }, { k: "whatsapp", n: "Uygulama Koçluğu", tur: "whatsapp", fiyat: 3900 }];
const L = (Array.isArray(ayar.paketler) && ayar.paketler.length ? ayar.paketler : DEF).map(p => ({ ...p }));
if (!L.some(p => p.k === "serbest")) L.push({ k: "serbest", n: "Serbest Paket", tur: "seans", fiyat: null });
await ref.set({ paketler: L }, { merge: true });
await isaret.set({ [ANAHTAR]: new Date().toISOString() }, { merge: true });
console.log(`::notice::Serbest Paket eklendi (${L.length} paket).`);
