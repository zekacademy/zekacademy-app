/* Tek seferlik (koçun isteği, 15 Kasım 2026): Safanur Akgül'ün 16–22 Kasım haftasındaki "yazılı haftası" programı kaldırılır,
   yerine 9–15 Kasım haftasının aynısı (işaretsiz) konur. Haftada işaretlenmiş görev varsa hiçbir şey yapmaz. */
import { createRequire } from "node:module";
import { kopyaPlani } from "./hafta-kopya.mjs";
const require = createRequire(new URL("../functions/package.json", import.meta.url));
const { initializeApp } = require("firebase-admin/app");
const { getFirestore, FieldPath } = require("firebase-admin/firestore");
const W = "2026-11-16";
const db = getFirestore(initializeApp({ projectId: process.env.PROJE }, "safanur")), isaret = db.doc("system/temizlik"), ANAHTAR = "safanur-hafta-2026-11-16";
if (((await isaret.get()).data() || {})[ANAHTAR]) { console.log("::notice::Safanur haftası daha önce düzeltilmiş; atlandı."); process.exit(0); }
const q = await db.collection("students").where("kullanici", "==", "safanurakgul").get();
if (q.size !== 1) { console.log(`::error::Safanur bulunamadı (${q.size})`); process.exit(0); }
const ref = q.docs[0].ref, s = q.docs[0].data(), hafta = (s.weeks || {})[W];
if (!(s.weeks || {})[W] && !(s.plan || {})[W]) console.log("::notice::Safanur'un 16 Kasım haftası zaten boş.");
if (Object.values(hafta || {}).some(L => (L || []).some(t => t && t.done))) { console.log("::error::Safanur 16 Kasım haftasında işaretli görev var; dokunulmadı."); process.exit(0); }
const temiz = { ...s, weeks: { ...(s.weeks || {}) }, plan: { ...(s.plan || {}) } }; delete temiz.weeks[W]; delete temiz.plan[W];
const { yaz, ozet } = kopyaPlani(temiz);
const yeniHafta = {}, yeniPlan = { saat: {}, hedef: {} };
for (const [p, v] of yaz) {
  if (p[1] !== W) { console.log(`::error::Beklenmeyen hafta ${p.join("/")}; dokunulmadı.`); process.exit(0); }
  if (p[0] === "weeks") yeniHafta[p[2]] = v; else yeniPlan[p[2]][p[3]] = v;
}
await ref.update(new FieldPath("weeks", W), yeniHafta, new FieldPath("plan", W), yeniPlan, "programYeni", new Date().toISOString());
await isaret.set({ [ANAHTAR]: { at: new Date().toISOString(), ...ozet } }, { merge: true });
console.log(`::notice title=Safanur 16–22 Kasım::Yazılı haftası kaldırıldı; ${ozet.gun} gün / ${ozet.gorev} görev, ${ozet.saat} süre hedefi, ${ozet.hedef} hedef konu 9–15 Kasım'dan kopyalandı.`);
