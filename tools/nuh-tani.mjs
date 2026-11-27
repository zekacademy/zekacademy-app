/* Salt okuma: Nuh Emir'in program haftaları (teşhis). Hiçbir şey yazmaz. */
import { createRequire } from "node:module";
import { pStart } from "../functions/logic.js";
const require = createRequire(new URL("../functions/package.json", import.meta.url));
const { initializeApp } = require("firebase-admin/app");
const { getFirestore } = require("firebase-admin/firestore");
const db = getFirestore(initializeApp({ projectId: process.env.PROJE }, "tani"));
let q = await db.collection("students").where("kullanici", "==", "nuhemiryetis").get();
if (q.size !== 1) q = await db.collection("students").where("name", "==", "Nuh Emir Yetiş").get();
if (q.size !== 1) { console.log(`::error::Nuh bulunamadı (${q.size})`); process.exit(0); }
const s = q.docs[0].data(), bugun = new Date().toLocaleDateString("sv-SE", { timeZone: "Europe/Istanbul" });
console.log(`::notice::id=${q.docs[0].id} donem=${JSON.stringify(s.donem||[])} bugun=${bugun} pStart(bugun)=${pStart(s, bugun)}`);
Object.keys(s.weeks||{}).filter(w=>w>="2026-11-02").sort().forEach(w=>{ const W = s.weeks[w]; console.log(`::notice::hafta ${w}: ` + Object.keys(W).sort().map(i=>`${i}:${(W[i]||[]).length}/${(W[i]||[]).filter(t=>t.done).length}${(W[i]||[]).some(t=>t.tekrar)?"T":""}`).join(" ")); });
console.log(`::notice::plan anahtarları: ${Object.keys(s.plan||{}).filter(w=>w>="2026-11-02").sort().join(", ")}`);
const cn = (await db.doc(`coachNotes/${q.docs[0].id}`).get()).data() || {}; console.log(`::notice::duzen=${JSON.stringify(cn.duzen||null)} gorusmesiz=${!!cn.gorusmesiz}`);
const g = await db.collection("gorusmeler").where("sid", "==", q.docs[0].id).get(); console.log(`::notice::görüşmeler: ` + g.docs.map(d=>d.data()).filter(x=>(x.tarih||"")>="2026-11-10").map(x=>`${x.tarih} ${x.saat||""} ${x.tur||""} ${x.durum||""} ${x.kaynak||""}`).sort().join(" | "));
