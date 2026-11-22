/* Salt okuma: koç açılışında inen koleksiyonların belge sayısı ve boyutu (isim yazılmaz). */
import { createRequire } from "node:module";
const require = createRequire(new URL("../functions/package.json", import.meta.url));
const { initializeApp } = require("firebase-admin/app");
const { getFirestore } = require("firebase-admin/firestore");
const db = getFirestore(initializeApp({ projectId: process.env.PROJE }, "olcum"));
const kb = o => Buffer.byteLength(JSON.stringify(o)) / 1024;
for (const c of ["students", "notifs", "coachNotes", "gorusmeler", "gruplar", "sorular"]) {
  const t0 = Date.now(), s = await db.collection(c).get(), ms = Date.now() - t0;
  const b = s.docs.map(d => kb(d.data())).sort((a, z) => z - a), top = b.reduce((a, v) => a + v, 0);
  console.log(`::notice::${c}: ${s.size} belge, toplam ${top.toFixed(0)} KB, en büyük ${(b[0]||0).toFixed(0)} KB, ilk 3: ${b.slice(0,3).map(x=>x.toFixed(0)).join("/")} KB, ${ms} ms`);
  if (c === "students") { const alan = {}; s.docs.forEach(d => Object.entries(d.data()).forEach(([k, v]) => alan[k] = (alan[k] || 0) + kb(v ?? null)));
    console.log("::notice::students alanları (KB): " + Object.entries(alan).sort((a, z) => z[1] - a[1]).slice(0, 12).map(([k, v]) => `${k}=${v.toFixed(0)}`).join(", ")); }
  if (c === "notifs") { const tur = {}; let eski = 0, okun = 0; const sin = Date.now() - 30 * 864e5;
    s.docs.forEach(d => { const x = d.data(); tur[x.type || "?"] = (tur[x.type || "?"] || 0) + 1; if (x.at && Date.parse(x.at) < sin) eski++; if (x.read) okun++; });
    console.log(`::notice::notifs: 30 günden eski ${eski}, okunmuş ${okun}; türler: ${Object.entries(tur).map(([k, v]) => k + "=" + v).join(", ")}`); }
}
const ay = (await db.doc("settings/main").get()).data() || {};
console.log(`::notice::settings/main: ${kb(ay).toFixed(0)} KB; büyük alanlar: ${Object.entries(ay).map(([k, v]) => [k, kb(v ?? null)]).sort((a, z) => z[1] - a[1]).slice(0, 6).map(([k, v]) => k + "=" + v.toFixed(0)).join(", ")}`);
