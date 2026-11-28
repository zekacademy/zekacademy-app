/* Salt okuma: Müberra Alas'ın son haftaları (teşhis). Hiçbir şey yazmaz. */
import { createRequire } from "node:module";
import { pStart } from "../functions/logic.js";
const require = createRequire(new URL("../functions/package.json", import.meta.url));
const { initializeApp } = require("firebase-admin/app");
const { getFirestore } = require("firebase-admin/firestore");
const db = getFirestore(initializeApp({ projectId: process.env.PROJE }, "tani3"));
const bugun = new Date().toLocaleDateString("sv-SE", { timeZone: "Europe/Istanbul" });
const q = await db.collection("students").get();
for (const d of q.docs) { const s = d.data(); if (!/müberra/i.test(s.name || "")) continue;
  console.log(`::notice::${s.name} id=${d.id} donem=${JSON.stringify(s.donem || [])} pStart=${pStart(s, bugun)}`);
  Object.keys(s.weeks || {}).filter(w => w >= "2026-11-13").sort().forEach(w => { const W = s.weeks[w];
    console.log(`::notice::hafta ${w}: ` + Object.keys(W).sort().map(i => `${i}=${(W[i] || []).length}/${(W[i] || []).filter(t => t.done).length}${(W[i] || []).some(t => t.tekrar) ? "T" : ""}`).join(" "));
    Object.keys(W).sort().slice(0, 2).forEach(i => console.log(`::notice::   ${w}[${i}]: ` + (W[i] || []).slice(0, 4).map(t => (t.t || "").slice(0, 28)).join(" | "))); });
  console.log(`::notice::plan: ` + Object.keys(s.plan || {}).filter(w => w >= "2026-11-13").sort().map(w => `${w}:${Object.keys((s.plan[w] || {}).hedef || {}).length}h`).join(", "));
  const cn = (await db.doc(`coachNotes/${d.id}`).get()).data() || {}; console.log(`::notice::duzen=${JSON.stringify(cn.duzen || null)}`); }
