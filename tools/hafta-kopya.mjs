/* Tek seferlik (koçun isteği, 15 Kasım 2026): 16–22 Kasım'ı her öğrencide bir önceki haftanın aynısıyla doldurur.
   Gün gün çalışır: 16 Kasım'a 9 Kasım'ın, 17'ye 10'unun ... görevleri gelir (uygulamadaki "Geçen haftanın programını aktar" ile aynı biçimde,
   işaretler sıfır). O günün çalışma süresi hedefi ve haftanın hedef konuları da aktarılır.
   Hiçbir şeyin üstüne yazılmaz: yeni haftada dolu olan gün / süre / hedef olduğu gibi kalır. Yalnızca ilgili alanlar güncellenir.
   KIP=kuru → sadece rapor; KIP=uygula → yazar (bir kez; system/temizlik işaretiyle kilitlenir). */
import { createRequire } from "node:module";
import { randomBytes } from "node:crypto";
import { pStart, addDays } from "../functions/logic.js";
const require = createRequire(new URL("../functions/package.json", import.meta.url));
const FA = process.env.PROJE ? { ...require("firebase-admin/app"), ...require("firebase-admin/firestore") } : {};
const { initializeApp, getFirestore, FieldPath } = FA;
const db = process.env.PROJE ? (initializeApp({ projectId: process.env.PROJE }), getFirestore()) : null, KIP = process.env.KIP || "kuru", isaret = db && db.doc("system/temizlik"), ANAHTAR = "hafta-kopya-2026-11-16";
const BAS = "2026-11-16", GUN = ["Pzt","Sal","Çar","Per","Cum","Cmt","Paz"];
if (db && KIP === "uygula" && ((await isaret.get()).data() || {})[ANAHTAR]) { console.log("::notice::16–22 Kasım kopyası daha önce yapılmış; atlandı."); process.exit(0); }
const dDiff = (a, b) => Math.round((Date.parse(b + "T12:00:00Z") - Date.parse(a + "T12:00:00Z")) / 864e5);
const pIdx = (s, d) => dDiff(pStart(s, d), d);
const gorevler = (s, d) => ((s.weeks || {})[pStart(s, d)] || {})[pIdx(s, d)] || [];
const plan = (s, w) => (s.plan || {})[w] || {};
const taskText = t => t.d ? [t.d, t.t, t.soru ? t.soru + " soru" : ""].filter(Boolean).join(" · ") : (t.t || "");
const uid = () => randomBytes(6).toString("hex");
const bos = v => v == null || v === "";
/* Bir öğrenci için yazılacaklar: [[yol dizisi, değer], ...] ve özet */
export function kopyaPlani(s){
  const yaz = [], ozet = { gorev: 0, gun: 0, dolu: [], saat: 0, hedef: 0 };
  for (let i = 0; i < 7; i++) {
    const x = addDays(BAS, i), k = addDays(x, -7), src = gorevler(s, k), dst = gorevler(s, x);
    const wx = pStart(s, x), ix = pIdx(s, x), wk = pStart(s, k), ik = pIdx(s, k);
    if (dst.length) { ozet.dolu.push(GUN[i]); }
    else if (src.length) { yaz.push([["weeks", wx, String(ix)], src.map(t => ({ id: uid(), t: taskText(t), done: false, doneAt: null }))]); ozet.gorev += src.length; ozet.gun++; }
    const sv = (plan(s, wk).saat || {})[ik];
    if (!bos(sv) && bos((plan(s, wx).saat || {})[ix])) { yaz.push([["plan", wx, "saat", String(ix)], sv]); ozet.saat++; }
  }
  const yeniHaftalar = [...new Set([...Array(7)].map((_, i) => pStart(s, addDays(BAS, i))))];
  for (const w of yeniHaftalar) {
    const eskiW = pStart(s, addDays(w < BAS ? BAS : w, -7)), H = plan(s, eskiW).hedef || {}, mevcut = plan(s, w).hedef || {};
    for (const [d, v] of Object.entries(H)) if (v && v.konu && !(mevcut[d] && mevcut[d].konu)) { yaz.push([["plan", w, "hedef", d], { konu: v.konu, done: false }]); ozet.hedef++; }
  }
  return { yaz, ozet };
}
if (process.env.PROJE) {
const satir = []; let topGorev = 0, topOgr = 0;
for (const doc of (await db.collection("students").get()).docs) {
  const s = doc.data(), ad = s.name || doc.id, { yaz: Y, ozet } = kopyaPlani(s), yaz = Y.flatMap(([p, v]) => [new FieldPath(...p), v]);
  if (!yaz.length) { satir.push(`${ad}: değişiklik yok${ozet.dolu.length ? ` (dolu günler: ${ozet.dolu.join(",")})` : " (önceki hafta boş)"}`); continue; }
  topGorev += ozet.gorev; topOgr++;
  satir.push(`${ad}: ${ozet.gun} gün / ${ozet.gorev} görev, ${ozet.saat} süre hedefi, ${ozet.hedef} hedef konu${ozet.dolu.length ? `; dolu bırakılan: ${ozet.dolu.join(",")}` : ""}`);
  if (KIP === "uygula") await doc.ref.update(...yaz, "programYeni", new Date().toISOString());
}
if (KIP === "uygula") await isaret.set({ [ANAHTAR]: { at: new Date().toISOString(), ogrenci: topOgr, gorev: topGorev } }, { merge: true });
const baslik = KIP === "uygula" ? "16–22 Kasım YAZILDI" : "16–22 Kasım KURU DENEME (yazılmadı)";
console.log(`::notice title=${baslik}::${topOgr} öğrenci, ${topGorev} görev%0A` + satir.join("%0A"));
}
