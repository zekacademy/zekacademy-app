/* Salt okuma: Müberra'nın kaydını geçmiş zamanlarda okumayı dener (Firestore readTime). Hiçbir şey yazmaz. */
import { createRequire } from "node:module";
const require = createRequire(new URL("../functions/package.json", import.meta.url));
const { initializeApp } = require("firebase-admin/app");
const { getFirestore, Timestamp } = require("firebase-admin/firestore");
const db = getFirestore(initializeApp({ projectId: process.env.PROJE }, "gecmis"));
const ref = db.doc("students/eFT3ckPmSjeNCDPrS2lyawAIKTP2"), now = Date.now();
const anlar = [now - 58*60e3, Date.parse("2026-11-28T06:00:00Z"), Date.parse("2026-11-28T04:00:00Z"), Date.parse("2026-11-27T21:00:00Z"), Date.parse("2026-11-27T18:00:00Z")];
const ozet = s => { const W = ((s||{}).weeks||{})["2026-11-27"]||{}; return Object.keys(W).sort().map(i=>`${i}=${(W[i]||[]).length}`).join(" ") + " | " + ((W[0]||[]).slice(0,3).map(t=>(t.t||"").slice(0,26)).join(" · ")); };
const simdi = (await ref.get()).data(); console.log(`::notice::ŞİMDİ: ${ozet(simdi)}`);
for (const t of anlar) { try { const snap = await db.runTransaction(tx => tx.get(ref), { readOnly: true, readTime: Timestamp.fromMillis(t) });
    const d = snap.data(), ayni = JSON.stringify(((d||{}).weeks||{})["2026-11-27"]) === JSON.stringify(((simdi||{}).weeks||{})["2026-11-27"]);
    console.log(`::notice::${new Date(t).toISOString()} → ${ayni ? "AYNI" : "FARKLI"}: ${ozet(d)}`); }
  catch (e) { console.log(`::notice::${new Date(t).toISOString()} → okunamadı: ${String(e.message).slice(0,120)}`); } }
