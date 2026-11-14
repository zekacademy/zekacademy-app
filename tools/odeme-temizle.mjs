/* Tek seferlik (koçun isteği, 14 Kasım 2026): Drive/Notion aktarımında Claude'un "ödendi" olarak girdiği kayıtları siler.
   Yalnızca hâlâ aktarıldığı gibi duran kayıtlara dokunur (tarih ve tutar aynıysa); koçun değiştirdiği/eklediği ödemeler korunur.
   Ücret ve başlangıç tarihi değişmez. Bir kez çalışır (system/temizlik belgesi işaretlenir). */
import { createRequire } from "node:module";
import { readFileSync } from "node:fs";
const require = createRequire(new URL("../functions/package.json", import.meta.url));
const { initializeApp } = require("firebase-admin/app");
const { getFirestore, FieldValue, FieldPath } = require("firebase-admin/firestore");
initializeApp({ projectId: process.env.PROJE });
const db = getFirestore(), isaret = db.doc("system/temizlik"), ANAHTAR = "odenen-2026-11-14";
if (((await isaret.get()).data() || {})[ANAHTAR]) { console.log("::notice::Ödeme temizliği daha önce yapılmış; atlandı."); process.exit(0); }
const L = JSON.parse(readFileSync(new URL("./odeme-temizle-liste.json", import.meta.url)));
let silinen = 0, korunan = 0, yok = [];
for (const x of L) {
  const q = await db.collection("students").where("kullanici", "==", x.u).get();
  if (q.empty) { yok.push(x.ad); continue; }
  for (const d of q.docs) {
    const ref = db.doc(`coachNotes/${d.id}`), od = (((await ref.get()).data() || {}).odeme || {}).odenen || {};
    const sil = [];
    for (const [k, v] of Object.entries(x.odenen)) { const c = od[k];
      if (c && c.t === v.t && Number(c.tutar) === Number(v.tutar)) sil.push(k); else if (c) korunan++; }
    if (sil.length) { const args = sil.flatMap(k => [new FieldPath("odeme", "odenen", k), FieldValue.delete()]); await ref.update(...args); silinen += sil.length; }
    console.log(`${x.ad}: ${sil.length} kayıt silindi`);
  }
}
await isaret.set({ [ANAHTAR]: { at: new Date().toISOString(), silinen, korunan } }, { merge: true });
console.log(`::notice::Ödeme temizliği: ${silinen} "ödendi" kaydı silindi, ${korunan} değişmiş kayıt korundu${yok.length ? `; uygulamada bulunamayan: ${yok.join(", ")}` : ""}.`);
