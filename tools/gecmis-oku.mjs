/* Salt okuma raporu: kurtarma yedeğindeki en eski hâl (11.19) ile şimdiki hâli karşılaştırır. Günlüğe yalnız baş harfler ve sayılar yazılır. */
import { createRequire } from "node:module";
const require = createRequire(new URL("../functions/package.json", import.meta.url));
const { initializeApp } = require("firebase-admin/app");
const { getFirestore } = require("firebase-admin/firestore");
const db = getFirestore(initializeApp({ projectId: process.env.PROJE }, "rapor"));
const K = (await db.collection("kurtarma").get()).docs.map(d=>d.data()), enEski = {};
K.forEach(k=>{ if(!enEski[k.sid] || k.an < enEski[k.sid].an) enEski[k.sid] = k; });
const bas = n => String(n||"?").split(/\s+/).map(p=>p[0]).join("");
const S = await db.collection("students").get(); let n = 0;
for (const d of S.docs) { const x = d.data(); if (x.silindi) continue; const e = enEski[d.id]; if (!e) continue; const satir = [];
  const W = new Set([...Object.keys(x.weeks||{}), ...Object.keys(e.weeks||{})].filter(w=>w>="2026-11-23"));
  for (const w of [...W].sort()) { const a = (e.weeks||{})[w]||{}, b = (x.weeks||{})[w]||{};
    for (const i of new Set([...Object.keys(a), ...Object.keys(b)])) { const A = a[i]||[], B = b[i]||[]; const metin = L => L.map(t=>t.t).join("|");
      const eskiTekrar = A.some(t=>t.tekrar), simdiTekrar = B.some(t=>t.tekrar);
      if (metin(A) !== metin(B)) satir.push(`${w.slice(5)}[${i}] 11.19:${A.length}${eskiTekrar?"T":""}→şimdi:${B.length}${simdiTekrar?"T":""}`);
      else if (simdiTekrar) satir.push(`${w.slice(5)}[${i}] tekrar(11.19'dan önce)`); } }
  if (satir.length) { n++; console.log(`::notice::${bas(x.name)}: ${satir.join(" · ")}`); } }
console.log(`::notice::Etkilenen öğrenci: ${n}`);
