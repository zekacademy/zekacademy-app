/* Tek seferlik (koçun isteği, 21 Kasım 2026): yeni paket fiyatları — Premium Koçluk 6.900 TL, Uygulama Koçluğu 3.900 TL.
   Mevcut öğrenciler AYNI fiyattan devam eder (ödeme planlarındaki tutara dokunulmaz); yeni fiyat yalnız Zehra Güler'in ödeme planına yazılır.
   Bir kez çalışır (system/temizlik işaretiyle kilitlenir). Tutarlar ekrana yazılmaz. */
import { createRequire } from "node:module";
const require = createRequire(new URL("../functions/package.json", import.meta.url));
const { initializeApp } = require("firebase-admin/app");
const { getFirestore, FieldPath } = require("firebase-admin/firestore");
const ANAHTAR = "fiyat-2026-11-21", PREMIUM = 6900, UYGULAMA = 3900;
const DEF = [{ k: "super", n: "Süper Koçluk", tur: "seans", fiyat: 6000 }, { k: "whatsapp", n: "WhatsApp Koçluğu", tur: "whatsapp", fiyat: null }];
const db = getFirestore(initializeApp({ projectId: process.env.PROJE }, "fiyat")), isaret = db.doc("system/temizlik");
if (((await isaret.get()).data() || {})[ANAHTAR]) { console.log("::notice::Fiyat güncellemesi daha önce yapılmış; atlandı."); process.exit(0); }
/* 1) Paket adları ve fiyatları */
const ayarRef = db.doc("settings/main"), ayar = (await ayarRef.get()).data() || {};
const L = (Array.isArray(ayar.paketler) && ayar.paketler.length ? ayar.paketler : DEF).map(p => ({ ...p }));
const prem = L.find(p => p.k === "super") || L.find(p => p.tur !== "whatsapp"), uyg = L.find(p => p.k === "whatsapp") || L.find(p => p.tur === "whatsapp");
if (prem) { prem.n = "Premium Koçluk"; prem.fiyat = PREMIUM; }
if (uyg) { uyg.n = "Uygulama Koçluğu"; uyg.fiyat = UYGULAMA; }
await ayarRef.set({ paketler: L }, { merge: true });
/* 2) Zehra Güler: yeni fiyat ödeme planına */
const norm = t => String(t || "").toLocaleLowerCase("tr").replace(/\s+/g, " ").trim();
const ogr = (await db.collection("students").get()).docs.filter(d => norm(d.data().name) === "zehra güler" && !d.data().silindi);
let zehra = "bulunamadı";
if (ogr.length === 1) {
  const d = ogr[0], pk = d.data().paket, paket = L.find(p => p.k === pk) || prem, fiyat = paket && paket.tur === "whatsapp" ? UYGULAMA : PREMIUM;
  const cn = db.doc(`coachNotes/${d.id}`), o = ((await cn.get()).data() || {}).odeme;
  if (o && o.bas) { await cn.update(new FieldPath("odeme", "tutar"), fiyat); zehra = `ödeme planı ${paket ? paket.n : "paket"} yeni fiyatına güncellendi`; }
  else zehra = "ödeme planı yok; tutar koç tarafından girilecek";
} else if (ogr.length > 1) zehra = `${ogr.length} kayıt bulundu; dokunulmadı`;
await isaret.set({ [ANAHTAR]: { at: new Date().toISOString(), zehra } }, { merge: true });
console.log(`::notice title=Yeni fiyatlar::Paketler güncellendi (Premium Koçluk, Uygulama Koçluğu). Diğer öğrencilerin ödeme planlarına dokunulmadı. Zehra Güler: ${zehra}.`);
