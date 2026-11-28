/* Salt okuma denetimi: tüm öğrencilerin bu haftası. Hiçbir şey yazmaz. Herkese açık günlüğe yalnız baş harfler ve sayılar yazılır. */
import { createRequire } from "node:module";
import { pStart, addDays } from "../functions/logic.js";
const require = createRequire(new URL("../functions/package.json", import.meta.url));
const { initializeApp } = require("firebase-admin/app");
const { getFirestore } = require("firebase-admin/firestore");
const db = getFirestore(initializeApp({ projectId: process.env.PROJE }, "denetim"));
const bugun = new Date().toLocaleDateString("sv-SE", { timeZone: "Europe/Istanbul" }), GUN = ["Pzt","Sal","Çar","Per","Cum","Cmt","Paz"];
const dIdx = d => (new Date(d + "T12:00:00Z").getUTCDay() + 6) % 7, dDiff = (a, b) => Math.round((Date.parse(b + "T12:00:00Z") - Date.parse(a + "T12:00:00Z")) / 864e5);
const bas = n => String(n || "?").trim().split(/\s+/).map(p => p[0].toLocaleUpperCase("tr")).join("");
const [S, C] = await Promise.all([db.collection("students").get(), db.collection("coachNotes").get()]); const cn = Object.fromEntries(C.docs.map(d => [d.id, d.data()]));
let sorunlu = 0, toplam = 0; const tumu = [];
for (const d of S.docs) { const s = d.data(); if (s.silindi) continue; toplam++; const w = pStart(s, bugun), an = (s.donem || []).slice().sort(), sonraki = an.find(a => a > w), len = sonraki ? Math.min(7, dDiff(w, sonraki)) : 7;
  const W = (s.weeks || {})[w] || {}, gunler = [...Array(len)].map((_, i) => W[i] || []), bos = gunler.map((L, i) => L.length ? null : GUN[dIdx(addDays(w, i))]).filter(Boolean);
  const tekrar = gunler.map((L, i) => L.some(t => t.tekrar) ? GUN[dIdx(addDays(w, i))] : null).filter(Boolean);
  const z = (cn[d.id] || {}).duzen || {}, gg = z.gun != null && z.gun !== "" ? +z.gun : null, kayma = gg != null && dIdx(w) !== gg;
  const kisa = len < 7, hic = gunler.every(L => !L.length), onceki = (s.weeks || {})[pStart(s, addDays(w, -1))] || {};
  const kopya = !hic && gunler.every((L, i) => JSON.stringify(L.map(t => t.t)) === JSON.stringify((onceki[i] || []).map(t => t.t)));
  const notlar = []; if (hic) notlar.push("BU HAFTA HİÇ GÖREV YOK"); else if (bos.length) notlar.push(`boş gün: ${bos.join(",")}`);
  if (tekrar.length) notlar.push(`otomatik kopya: ${tekrar.join(",")}`); if (kayma) notlar.push(`hafta ${GUN[dIdx(w)]} başlıyor, görüşme günü ${GUN[gg]}`);
  if (kisa) notlar.push(`kısa hafta (${len} gün)`); if (kopya) notlar.push("geçen haftanın aynısı");
  tumu.push(`${bas(s.name)}(${(s.sinif || "").replace(". sınıf", "")})`);
  if (notlar.length) { sorunlu++; console.log(`::notice::${bas(s.name)} [${s.sinif || ""}] hafta ${w.slice(5)}: ${notlar.join(" · ")}`); } }
console.log(`::notice::Toplam ${toplam} aktif öğrenci, ${sorunlu} öğrencide not var.`);
