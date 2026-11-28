/* Salt okuma: Müberra'nın 27 Kasım haftasını geçmiş zamanlardan okuyup günlüğe JSON olarak yazar (kurtarma için). Hiçbir şey yazmaz. */
import { createRequire } from "node:module";
const require = createRequire(new URL("../functions/package.json", import.meta.url));
const { initializeApp } = require("firebase-admin/app");
const { getFirestore, Timestamp } = require("firebase-admin/firestore");
const db = getFirestore(initializeApp({ projectId: process.env.PROJE }, "gecmis"));
const ref = db.doc("students/eFT3ckPmSjeNCDPrS2lyawAIKTP2"), now = Date.now();
for (const dk of [59.5, 58, 55, 50, 45, 40, 30, 20, 10]) { const t = now - dk*60e3;
  try { const d = (await db.runTransaction(tx => tx.get(ref), { readOnly: true, readTime: Timestamp.fromMillis(t) })).data() || {};
    console.log(`KURTARMA ${new Date(t).toISOString()} ` + JSON.stringify({ weeks: (d.weeks||{})["2026-11-27"], plan: (d.plan||{})["2026-11-27"] })); }
  catch (e) { console.log(`KURTARMA ${new Date(t).toISOString()} HATA ${e.message}`); } }
