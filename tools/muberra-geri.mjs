/* Tek seferlik (28 Kasım 2026, koçun isteği): Müberra'nın 27 Kasım haftası, otomatik doldurma üzerine yazmadan önceki hâline (kurtarma yedeği, 11.19) döner.
   O saatten sonra öğrencinin işaretlediği görevler aynı adlı göreve taşınır. Bir kez çalışır (system/temizlik). */
import { createRequire } from "node:module";
const require = createRequire(new URL("../functions/package.json", import.meta.url));
const { initializeApp } = require("firebase-admin/app");
const { getFirestore } = require("firebase-admin/firestore");
const SID = "eFT3ckPmSjeNCDPrS2lyawAIKTP2", W = "2026-11-27", ANAHTAR = "muberra-geri-2026-11-28";
const db = getFirestore(initializeApp({ projectId: process.env.PROJE }, "mgeri")), isaret = db.doc("system/temizlik");
if (((await isaret.get()).data() || {})[ANAHTAR]) { console.log("::notice::Müberra geri yükleme daha önce yapılmış; atlandı."); process.exit(0); }
const K = (await db.collection("kurtarma").where("sid", "==", SID).get()).docs.map(d => d.data()).sort((a, b) => a.an < b.an ? -1 : 1)[0];
if (!K || !(K.weeks || {})[W]) { console.log("::error::Kurtarma yedeği bulunamadı"); process.exit(0); }
const ref = db.doc("students/" + SID), s = (await ref.get()).data() || {}, simdi = (s.weeks || {})[W] || {}, eski = K.weeks[W];
const yeni = {}; let tasinan = 0;
for (const i of Object.keys(eski)) { const isaretli = new Map((simdi[i] || []).filter(t => t.done).map(t => [t.t, t]));
  yeni[i] = (eski[i] || []).map(t => { const m = isaretli.get(t.t); if (m && !t.done) { tasinan++; return { ...t, done: true, doneAt: m.doneAt || null }; } return t; }); }
const upd = { [`weeks.${W}`]: yeni }; if ((K.plan || {})[W]) upd[`plan.${W}`] = K.plan[W];
await ref.update(upd); await isaret.set({ [ANAHTAR]: new Date().toISOString() }, { merge: true });
console.log(`::notice::Müberra: ${W} haftası ${K.an} hâline döndü (${Object.keys(yeni).length} gün; ${tasinan} işaret korundu).`);
