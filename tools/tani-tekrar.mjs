/* Salt okuma: bu haftası otomatik tekrarla (tekrar:true) dolmuş öğrenciler. Hiçbir şey yazmaz. */
import { createRequire } from "node:module";
import { pStart } from "../functions/logic.js";
const require = createRequire(new URL("../functions/package.json", import.meta.url));
const { initializeApp } = require("firebase-admin/app");
const { getFirestore } = require("firebase-admin/firestore");
const db = getFirestore(initializeApp({ projectId: process.env.PROJE }, "tani2"));
const bugun = new Date().toLocaleDateString("sv-SE", { timeZone: "Europe/Istanbul" });
const q = await db.collection("students").get(); let n = 0;
for (const d of q.docs) { const s = d.data(); if (s.silindi) continue; const w = pStart(s, bugun), W = (s.weeks || {})[w] || {};
  const T = Object.entries(W).map(([i, L]) => [i, (L || []).length, (L || []).filter(t => t.tekrar).length]); const tek = T.reduce((a, x) => a + x[2], 0); if (!tek) continue; n++;
  console.log(`::notice::${s.name} · hafta ${w} · donem son: ${(s.donem || []).slice(-3).join(",")} · gün(görev/tekrar): ${T.map(x => x.join(":").replace(/^(\d+):/, "$1=")).join(" ")}`);
  const ilk = W[Object.keys(W)[0]] || []; console.log(`::notice::  örnek: ${ilk.slice(0, 3).map(t => (t.t || "").slice(0, 30) + (t.tekrar ? "*" : "")).join(" | ")}`); }
console.log(`::notice::Tekrarla dolan öğrenci: ${n}`);
