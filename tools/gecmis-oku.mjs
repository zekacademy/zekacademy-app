/* Kurtarma yedeği: TÜM öğrencilerin 16 Kasım sonrası haftalarını geçmiş zamanlardan (Firestore readTime, en fazla 1 saat geri) okur ve
   yalnız sunucunun erişebildiği "kurtarma" koleksiyonuna yazar. Öğrenci kayıtlarına dokunmaz; günlüğe veri yazmaz. */
import { createRequire } from "node:module";
const require = createRequire(new URL("../functions/package.json", import.meta.url));
const { initializeApp } = require("firebase-admin/app");
const { getFirestore, Timestamp } = require("firebase-admin/firestore");
const db = getFirestore(initializeApp({ projectId: process.env.PROJE }, "kurtarma"));
const now = Date.now(), ids = (await db.collection("students").select().get()).docs.map(d=>d.id);
for (const dk of [59.4, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5]) { const t = now - dk*60e3, iso = new Date(t).toISOString(); let n = 0;
  try { const snap = await db.runTransaction(tx => tx.getAll(...ids.map(i=>db.doc("students/"+i))), { readOnly: true, readTime: Timestamp.fromMillis(t) });
    const b = db.batch(); snap.forEach(d=>{ const x = d.data(); if(!x) return; const W = {}, P = {}; Object.keys(x.weeks||{}).filter(w=>w>="2026-11-16").forEach(w=>W[w]=x.weeks[w]); Object.keys(x.plan||{}).filter(w=>w>="2026-11-16").forEach(w=>P[w]=x.plan[w]);
      b.set(db.doc(`kurtarma/${iso}_${d.id}`), {sid:d.id, an:iso, donem:x.donem||[], weeks:W, plan:P}); n++; }); await b.commit(); console.log(`::notice::${iso}: ${n} öğrenci yedeklendi`); }
  catch (e) { console.log(`::notice::${iso}: okunamadı (${String(e.code||"")})`); } }
