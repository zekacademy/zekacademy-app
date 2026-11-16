/* Zek AI gerçek hatalarını (aiHatalar, anonim) eğitim için dışa aktarır: son 60 günün kayıtları → ai-hatalar/hatalar.json.
   Öğrenci kimliği yok; küçük soru görseli (kucuk) ayrı dosyalara yazılır. Çalıştıran: .github/workflows/ai-hatalar.yml */
import { createRequire } from "node:module";
import { mkdirSync, writeFileSync } from "node:fs";
const require = createRequire(new URL("../functions/package.json", import.meta.url));
const { initializeApp } = require("firebase-admin/app");
const { getFirestore } = require("firebase-admin/firestore");
initializeApp({ projectId: process.env.PROJE });
const db = getFirestore(), sinir = new Date(Date.now() - 60 * 864e5).toISOString(), out = process.argv[2] || "ai-hatalar";
const q = await db.collection("aiHatalar").where("at", ">=", sinir).get();
mkdirSync(`${out}/gorsel`, { recursive: true });
const L = q.docs.map(d => { const x = d.data(), { kucuk, ...geri } = x;
  if (kucuk && kucuk.startsWith("data:image/jpeg;base64,")) writeFileSync(`${out}/gorsel/${d.id}.jpg`, Buffer.from(kucuk.slice(23), "base64"));
  return { id: d.id, ...geri, gorsel: kucuk ? `gorsel/${d.id}.jpg` : null }; }).sort((a, b) => a.at < b.at ? 1 : -1);
writeFileSync(`${out}/hatalar.json`, JSON.stringify({ guncelleme: new Date().toISOString(), adet: L.length, hatalar: L }, null, 1));
console.log(`::notice::aiHatalar: ${L.length} kayıt dışa aktarıldı`);
