// Soru Çözüm Merkezi: model seçimi, hak, bütçe ve bonus testleri
import { test } from "node:test";
import assert from "node:assert/strict";
import { aiCfg, aiAcikMi, maliyet, kalanHak, zoraGec, jsonCikar, anahtarDurumu, aySonuTahmini, haftalikPerformans, bonusDagit, bonusMesaj } from "../functions/soru.js";

const c = aiCfg({});
const iyi = { okunabildi: true, emin: true, zorluk: "kolay", cevap: { sik: "C" }, adimlar: [{ baslik: "x" }] };

test("varsayılanlar: kapalı, 120 hak, 100 $ tavan; ayarlar üzerine yazar", () => {
  assert.equal(c.acik, "kapali"); assert.equal(c.aylikHak, 120); assert.equal(c.tavan, 100);
  const c2 = aiCfg({ ai: { aylikHak: 80, fiyat: { zor: { in: 3, out: 15 } } } });
  assert.equal(c2.aylikHak, 80); assert.equal(c2.fiyat.zor.out, 15); assert.equal(c2.fiyat.kolay.in, 0.10);
});

test("açık mı: kapalı / pilot / herkes", () => {
  assert.equal(aiAcikMi(c, "a"), false);
  assert.equal(aiAcikMi({ ...c, acik: "pilot", pilot: ["a"] }, "a"), true);
  assert.equal(aiAcikMi({ ...c, acik: "pilot", pilot: ["a"] }, "b"), false);
  assert.equal(aiAcikMi({ ...c, acik: "herkes" }, "b"), true);
});

test("maliyet: token fiyatlarına göre dolar", () => {
  assert.ok(Math.abs(maliyet(c, "kolay", { input_tokens: 2500, output_tokens: 3500 }) - 0.002) < 1e-9);
  assert.ok(Math.abs(maliyet(c, "zor", { input_tokens: 2500, output_tokens: 3500 }) - 0.04) < 1e-9);
});

test("kalan hak: aylık + bonus + ek − kullanılan, eksiye düşmez", () => {
  assert.equal(kalanHak(c, {}), 120);
  assert.equal(kalanHak(c, { kullanilan: 30, bonus: 20, ekHak: 10 }), 120);
  assert.equal(kalanHak(c, { kullanilan: 500 }), 0);
});

test("güçlü modele geçiş kuralları", () => {
  assert.equal(zoraGec(iyi, ""), null);
  assert.equal(zoraGec(iyi, "C"), null);
  assert.equal(zoraGec(iyi, "B"), "anahtar-uyusmuyor");
  assert.equal(zoraGec({ ...iyi, emin: false }, ""), "emin-degil");
  assert.equal(zoraGec({ ...iyi, zorluk: "zor" }, ""), "zor");
  assert.equal(zoraGec({ ...iyi, adimlar: [] }, ""), "adim-yok");
  assert.equal(zoraGec(null, ""), "okunamadı-json");
  assert.equal(zoraGec({ okunabildi: false }, ""), null, "okunamayan fotoğraf için pahalı modele gitme");
});

test("JSON çıkarma: düz, kod bloğu ve metin içinde", () => {
  assert.deepEqual(jsonCikar('{"a":1}'), { a: 1 });
  assert.deepEqual(jsonCikar('```json\n{"a":2}\n```'), { a: 2 });
  assert.deepEqual(jsonCikar('İşte çözüm: {"a":3} umarım yardımcı olur'), { a: 3 });
  assert.equal(jsonCikar("bozuk"), null);
});

test("cevap anahtarı durumu gerçek karşılaştırmayla belirlenir", () => {
  assert.equal(anahtarDurumu(iyi, ""), "yok");
  assert.equal(anahtarDurumu(iyi, "c"), "uyumlu");
  assert.equal(anahtarDurumu(iyi, "D"), "uyumsuz");
});

test("ay sonu tahmini günlük ortalamayla", () => {
  const t = aySonuTahmini(15, "2026-11-10"); assert.equal(t.gunSayisi, 30); assert.equal(Math.round(t.tahmin), 45);
});

test("haftalık performans: son 7 günün uyumu ve çalışma süresi", () => {
  const s = { weeks: { "2026-11-02": { "0": [{ done: true }, { done: true }], "1": [{ done: true }, { done: false }] } }, gunluk: { "2026-11-02": 210, "2026-11-03": 210 } };
  const p = haftalikPerformans(s, "2026-11-09");
  assert.equal(p.uyum, 75); assert.equal(p.gunlukDk, 60); assert.equal(p.gorev, 4);
});

test("bonus: pay varsa hakkını kullanmış çalışkan öğrenciye, tavanı aşmadan", () => {
  const cc = { ...c, acik: "herkes" };
  const ogr = [
    { sid: "a", k: { kullanilan: 100 }, perf: { uyum: 85, gunlukDk: 120 } },  // hak eder
    { sid: "b", k: { kullanilan: 100 }, perf: { uyum: 40, gunlukDk: 60 } },   // çalışkan değil
    { sid: "c", k: { kullanilan: 10 }, perf: { uyum: 95, gunlukDk: 300 } },   // hakkını kullanmamış
    { sid: "d", k: { kullanilan: 90 }, perf: { uyum: null, gunlukDk: 200 } }, // süreyle hak eder
  ];
  const r = bonusDagit(cc, { harcanan: 6, date: "2026-11-16", ogrenciler: ogr });
  assert.deepEqual(r.dagitim.map(x => x.sid), ["a", "d"]);
  assert.ok(r.dagitim.every(x => x.hak > 0 && x.hak <= cc.bonusTavan));
  assert.equal(bonusDagit(cc, { harcanan: 80, date: "2026-11-16", ogrenciler: ogr }).dagitim.length, 0, "tahmin tavana yakınsa bonus yok");
  assert.equal(bonusDagit({ ...cc, bonusAcik: false }, { harcanan: 1, date: "2026-11-16", ogrenciler: ogr }).dagitim.length, 0);
  assert.match(bonusMesaj({ hak: 20, uyum: 85 }), /%85 uydun, \+20 bonus/);
  assert.match(bonusMesaj({ hak: 12, uyum: null, gunlukDk: 200 }), /200 dk/);
});
