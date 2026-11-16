/* Tek seferlik düzeltme (koçun isteği, 14 Kasım 2026): odeme-temizle.mjs'in sildiği "ödendi" kayıtlarından Kasım öncesine ait olanları geri yazar.
   Kasım (2026-11) kayıtları silinmiş kalır. O tarihte koçun girdiği bir kayıt varsa üstüne yazılmaz. Bir kez çalışır. */
import { createRequire } from "node:module";
import { readFileSync } from "node:fs";
const require = createRequire(new URL("../functions/package.json", import.meta.url));
const { initializeApp } = require("firebase-admin/app");
const { getFirestore, FieldPath } = require("firebase-admin/firestore");
initializeApp({ projectId: process.env.PROJE });
const db = getFirestore(), isaret = db.doc("system/temizlik"), ANAHTAR = "odenen-geri-2026-11-14";
if (((await isaret.get()).data() || {})[ANAHTAR]) { console.log("::notice::Ödeme geri yükleme daha önce yapılmış; atlandı."); process.exit(0); }
const L = JSON.parse(readFileSync(new URL("./odeme-temizle-liste.json", import.meta.url)));
let yazilan = 0, vardi = 0; const detay = [];
for (const x of L) {
  const q = await db.collection("students").where("kullanici", "==", x.u).get();
  for (const d of q.docs) {
    const ref = db.doc(`coachNotes/${d.id}`), od = (((await ref.get()).data() || {}).odeme || {}).odenen || {};
    const yaz = Object.entries(x.odenen).filter(([k]) => k < "2026-11-01" && !(k in od) ? true : (k < "2026-11-01" && (vardi++, false)));
    if (yaz.length) { await ref.update(...yaz.flatMap(([k, v]) => [new FieldPath("odeme", "odenen", k), v])); yazilan += yaz.length; detay.push(`${x.ad} ${yaz.length}`); }
  }
}
await isaret.set({ [ANAHTAR]: { at: new Date().toISOString(), yazilan, vardi, detay } }, { merge: true });
console.log(`::notice::Ödeme geri yükleme: Kasım öncesi ${yazilan} "ödendi" kaydı geri yazıldı, ${vardi} kayıt zaten vardı. Kasım kayıtları silinmiş kaldı.`);
