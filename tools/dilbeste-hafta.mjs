/* Tek seferlik (koçun isteği, 16 Kasım 2026): Dilbeste Doğru'nun 16–22 Kasım programı, Drive dosyasındaki "Bu hafta" sekmesi yerine
   "DİLBESTE" sekmesinden (tools/dilbeste-hafta.json) alınır. Gün gün yazılır (Pazartesi 16 … Pazar 22), o günün çalışma süresi
   hedefi ve haftanın hedef konuları da değişir. Öğrencinin bu hafta işaretlediği görevler kaybolmaz: aynı adlı yeni göreve işaret taşınır,
   eşi yoksa görev o güne eklenir. Bir kez çalışır (system/temizlik işaretiyle kilitlenir). */
import { createRequire } from "node:module";
import { randomBytes } from "node:crypto";
import { readFileSync } from "node:fs";
import { pStart, addDays } from "../functions/logic.js";
const require = createRequire(new URL("../functions/package.json", import.meta.url));
const { initializeApp } = require("firebase-admin/app");
const { getFirestore, FieldPath } = require("firebase-admin/firestore");
const BAS = "2026-11-16", ANAHTAR = "dilbeste-hafta-2026-11-16";
const V = JSON.parse(readFileSync(new URL("./dilbeste-hafta.json", import.meta.url), "utf8"));
const db = getFirestore(initializeApp({ projectId: process.env.PROJE }, "dilbeste")), isaret = db.doc("system/temizlik");
if (((await isaret.get()).data() || {})[ANAHTAR]) { console.log("::notice::Dilbeste haftası daha önce düzeltilmiş; atlandı."); process.exit(0); }
let q = await db.collection("students").where("kullanici", "==", "dilbestedogru").get();
if (q.size !== 1) q = await db.collection("students").where("name", "==", "Dilbeste Doğru").get();
if (q.size !== 1) { console.log(`::error::Dilbeste bulunamadı (${q.size})`); process.exit(0); }
const ref = q.docs[0].ref, s = q.docs[0].data();
const dDiff = (a, b) => Math.round((Date.parse(b + "T12:00:00Z") - Date.parse(a + "T12:00:00Z")) / 864e5);
const norm = t => String(t || "").toLocaleLowerCase("tr").replace(/\s+/g, " ").trim();
const taskText = t => t.d ? [t.d, t.t, t.soru ? t.soru + " soru" : ""].filter(Boolean).join(" · ") : (t.t || "");
const uid = () => randomBytes(6).toString("hex");
const args = []; let gorev = 0, tasinan = 0, eklenen = 0;
const haftalar = new Set();
for (let i = 0; i < 7; i++) {
  const x = addDays(BAS, i), w = pStart(s, x), ix = String(dDiff(w, x)); haftalar.add(w);
  const eski = (((s.weeks || {})[w] || {})[ix]) || [];
  const yeni = V.gunler[i].map(t => ({ id: uid(), t, done: false, doneAt: null }));
  for (const e of eski.filter(t => t && t.done)) {
    const es = yeni.find(n => !n.done && norm(n.t) === norm(taskText(e)));
    if (es) { es.done = true; es.doneAt = e.doneAt || x; tasinan++; } else { yeni.push({ ...e }); eklenen++; }
  }
  gorev += V.gunler[i].length;
  args.push(new FieldPath("weeks", w, ix), yeni);
  if (V.saat[i] != null) args.push(new FieldPath("plan", w, "saat", ix), V.saat[i]);
}
for (const w of haftalar) args.push(new FieldPath("plan", w, "hedef"), Object.fromEntries(Object.entries(V.hedef).map(([d, k]) => [d, { konu: k, done: false }])));
args.push("programYeni", new Date().toISOString());
await ref.update(...args);
await isaret.set({ [ANAHTAR]: { at: new Date().toISOString(), gorev, tasinan, eklenen, haftalar: [...haftalar] } }, { merge: true });
console.log(`::notice title=Dilbeste 16–22 Kasım::Program 'DİLBESTE' sekmesinden yazıldı: ${gorev} görev, ${Object.keys(V.hedef).length} hedef konu; işaretli görev taşınan ${tasinan}, eklenen ${eklenen}; hafta(lar) ${[...haftalar].join(", ")}.`);
