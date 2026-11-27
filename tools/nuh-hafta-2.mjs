/* Tek seferlik (koçun isteği, 27 Kasım 2026): Nuh Emir'in bu haftası boş görünüyordu (bugüne fazladan "hafta başı" düşmüş).
   Bu haftanın her gününe, geçen haftanın AYNI GÜNÜNDEKİ görevler işaretsiz yazılır (Cuma'ya Cuma …). Dolu ve öğrencinin işaretlediği günlere dokunulmaz;
   yalnız otomatik "ilk gün tekrarı" ile yanlış güne gelmiş, hiç işaretlenmemiş görevler değiştirilir. Çalışma süresi hedefi ve boşsa hedef konular da gelir.
   Bir kez çalışır (system/temizlik işaretiyle kilitlenir). Hafta başı tarihlerine (donem) dokunulmaz. */
import { createRequire } from "node:module";
import { randomBytes } from "node:crypto";
import { pStart, addDays, dayTasks } from "../functions/logic.js";
const require = createRequire(new URL("../functions/package.json", import.meta.url));
const { initializeApp } = require("firebase-admin/app");
const { getFirestore } = require("firebase-admin/firestore");
const ANAHTAR = "nuh-hafta-2026-11-27";
const db = getFirestore(initializeApp({ projectId: process.env.PROJE }, "nuh2")), isaret = db.doc("system/temizlik");
if (((await isaret.get()).data() || {})[ANAHTAR]) { console.log("::notice::Nuh (27 Kasım) daha önce düzeltilmiş; atlandı."); process.exit(0); }
let q = await db.collection("students").where("kullanici", "==", "nuhemiryetis").get();
if (q.size !== 1) q = await db.collection("students").where("name", "==", "Nuh Emir Yetiş").get();
if (q.size !== 1) { console.log(`::error::Nuh bulunamadı (${q.size})`); process.exit(0); }
const ref = q.docs[0].ref, s = q.docs[0].data();
const dDiff = (a, b) => Math.round((Date.parse(b + "T12:00:00Z") - Date.parse(a + "T12:00:00Z")) / 864e5);
const bugun = new Date().toLocaleDateString("sv-SE", { timeZone: "Europe/Istanbul" }), w = pStart(s, bugun);
const an = (s.donem || []).slice().sort(), sonraki = an.find(a => a > w), len = sonraki ? Math.min(7, dDiff(w, sonraki)) : 7;
const id = () => randomBytes(6).toString("hex"), rapor = [];
s.weeks = s.weeks || {}; s.weeks[w] = s.weeks[w] || {}; s.plan = s.plan || {}; const P = s.plan[w] = s.plan[w] || {}; P.saat = P.saat || {};
for (let i = 0; i < len; i++) { const d = addDays(w, i), mevcut = s.weeks[w][i] || [];
  const degisir = !mevcut.length || (mevcut.every(t => t.tekrar && !t.done));
  if (!degisir) { rapor.push(`${d}: dolu, dokunulmadı`); continue; }
  let src = null; for (const k of [7, 14]) { const sd = addDays(d, -k), L = dayTasks(s, sd); if (L.length) { src = sd; break; } }
  if (!src) { rapor.push(`${d}: geçen haftalarda bu gün boş`); continue; }
  s.weeks[w][i] = dayTasks(s, src).map(t => { const k = { ...t, id: id(), done: false, doneAt: null }; delete k.dk; delete k.tekrar; return k; });
  const sw = pStart(s, src), si = dDiff(sw, src), sv = ((s.plan[sw] || {}).saat || {})[si]; if (sv != null && sv !== "" && (P.saat[i] == null || P.saat[i] === "")) P.saat[i] = sv;
  rapor.push(`${d}: ${src} gününden ${s.weeks[w][i].length} görev`); }
if (!P.hedef || !Object.keys(P.hedef).length) { const sw = pStart(s, addDays(bugun, -7)), h = (s.plan[sw] || {}).hedef; if (h && Object.keys(h).length) { P.hedef = Object.fromEntries(Object.entries(h).map(([k, v]) => [k, { ...v, done: false }])); rapor.push(`hedef konular ${sw} haftasından`); } }
await ref.update({ [`weeks.${w}`]: s.weeks[w], [`plan.${w}`]: P });
await isaret.set({ [ANAHTAR]: new Date().toISOString() }, { merge: true });
console.log(`::notice::Nuh Emir · hafta ${w} (${len} gün): ` + rapor.join(" · "));
