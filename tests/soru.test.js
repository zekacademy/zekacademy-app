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

test("adil kullanım: günlük ve aylık kalan soru (sınırsız düzen)", async () => {
  const { aiCfg, adilKalan } = await import("../functions/soru.js");
  const c = aiCfg({});
  assert.equal(c.sinirsiz, true); assert.equal(c.gunlukSoru, 30); assert.equal(c.aylikSoru, 600);
  assert.deepEqual(adilKalan(c, { soru: 100, gunSoru: { "2026-11-16": 28 } }, "2026-11-16"), { gun: 2, ay: 500 });
  assert.deepEqual(adilKalan(c, { soru: 600, ekHak: 10, gunSoru: {} }, "2026-11-16"), { gun: 30, ay: 10 });
  assert.equal(adilKalan(c, { soru: 5, gunSoru: { "2026-11-16": 30 } }, "2026-11-16").gun, 0);
});

test("şekilli sorular: geometri/grafik ve kolay olmayan soru güçlü modele geçer, okuma kuralları istekte", async () => {
  const { zoraGec, cozIstegi } = await import("../functions/soru.js");
  const tamam = { okunabildi: true, emin: true, zorluk: "orta", adimlar: [{ baslik: "x" }], cevap: { sik: "C" } };
  assert.equal(zoraGec({ ...tamam, sekil: { var: true, tur: "geometri", okunan: ["AB = 6"] } }, ""), "sekil");
  assert.equal(zoraGec({ ...tamam, zorluk: "kolay", sekil: { var: true, tur: "geometri" } }, ""), null);
  assert.equal(zoraGec({ ...tamam, ders: "TYT Coğrafya", sekil: { var: true, tur: "tablo" } }, ""), null, "sözelde tablo tek başına güçlü modele götürmez");
  assert.equal(zoraGec({ ...tamam, ders: "TYT Matematik", sekil: { var: true, tur: "tablo" } }, ""), "sekil", "sayısalda şekilli/tablolu yeni nesil soru güçlüye");
  assert.equal(zoraGec({ ...tamam, ders: "TYT Matematik", zorluk: "kolay", sekil: { var: true, tur: "gorsel" } }, ""), null);
  assert.equal(zoraGec({ ...tamam, ders: "AYT Fizik" }, ""), "ayt-fen"); assert.equal(zoraGec({ ...tamam, ders: "AYT Kimya" }, ""), "ayt-fen");
  assert.equal(zoraGec({ ...tamam, ders: "TYT Fizik" }, ""), null);
  assert.equal(zoraGec({ ...tamam, sekil: { var: false, tur: "yok" } }, ""), null);
  const q = cozIstegi({}); assert.match(q, /ŞEKİL VE RESİM OKUMA/); assert.match(q, /ölçekli değildir/); assert.match(q, /"sekil"/);
});

test("çözüm akışı: talimat önbellek için sabit/değişken ayrımı, beceriler, ikinci bakış", async () => {
  const { COZ_SABIT, cozDegisken, sozelMi } = await import("../functions/soru.js");
  const { COZUM_BILGI } = await import("../functions/cozum-bilgi.js");
  assert.ok(COZ_SABIT.includes(COZUM_BILGI)); assert.match(COZ_SABIT, /ŞEKİL VE RESİM OKUMA/); assert.match(COZ_SABIT, /EN YAKIN rakip şık/);
  assert.ok(COZUM_BILGI.split(/\s+/).length < 1800, "beceri metni kısa kalmalı (her istekte gidiyor)");
  assert.doesNotMatch(cozDegisken({}), /ŞEKİL VE RESİM/); /* değişken kısım sabiti tekrar etmez */
  assert.match(cozDegisken({ anahtar: "C" }), /C şıkkı/); assert.match(cozDegisken({ ikinci: true }), /E'den A'ya/);
  assert.equal(sozelMi("TYT Türkçe"), true); assert.equal(sozelMi("TYT Coğrafya"), true); assert.equal(sozelMi("TYT Matematik"), false); assert.equal(sozelMi("AYT Fizik"), false);
});

test("hakem ve anahtar seçimi", async () => {
  const { hakemSonucu, anahtarlaSec } = await import("../functions/soru.js");
  const H = { cevap: { sik: "B" }, emin: true, ad: "h" }, G = { cevap: { sik: "D" }, emin: true, ad: "g" };
  assert.equal(hakemSonucu(H, G, { sik: "D", emin: true }).r.ad, "g");
  const h1 = hakemSonucu(H, G, { sik: "B", emin: true }); assert.equal(h1.r.ad, "h"); assert.equal(h1.kim, "hizli");
  const h2 = hakemSonucu(H, G, { sik: "A" }); assert.equal(h2.r.ad, "g"); assert.equal(h2.r.emin, false);
  assert.equal(hakemSonucu(H, G, null).r.emin, false);
  assert.equal(anahtarlaSec(H, G, "B").r.ad, "h"); assert.equal(anahtarlaSec(H, G, "D").r.ad, "g");
  const a3 = anahtarlaSec(H, G, "E"); assert.equal(a3.r.ad, "g"); assert.equal(a3.r.emin, false);
});

test("Türkçe becerisi: yalnız Türkçe sorularında, sabit kısımdan ayrı ve sınırlı uzunlukta", async () => {
  const { turkceMi, TURKCE_BECERI, COZ_SABIT } = await import("../functions/soru.js");
  assert.equal(turkceMi("TYT Türkçe"), true); assert.equal(turkceMi("Paragraf"), true);
  assert.equal(turkceMi("TYT Tarih"), false); assert.equal(turkceMi("TYT Matematik"), false); assert.equal(turkceMi(undefined), false);
  assert.match(TURKCE_BECERI, /HER ŞIKKI ETİKETLE/); assert.match(TURKCE_BECERI, /KARAR VERMEDEN ÖNCE TARA/);
  assert.ok(!COZ_SABIT.includes(TURKCE_BECERI), "beceri her soruda değil, yalnız Türkçede gider");
  assert.ok(TURKCE_BECERI.split(/\s+/).length < 2000, "Türkçe becerisi kısa kalmalı");
});

test("hakem: daha güçlü model, modele göre değil gerekçeye göre karar", async () => {
  const { aiCfg, hakemIstegi, maliyet } = await import("../functions/soru.js");
  const c = aiCfg({}); assert.match(c.modelHakem, /opus/); assert.ok(c.fiyat.hakem.in > c.fiyat.zor.in);
  const q = hakemIstegi({ cevap: { sik: "A" } }, { cevap: { sik: "B" } }, "");
  assert.match(q, /kendin baştan çöz/); assert.doesNotMatch(q, /genelde daha güvenilirdir/);
  assert.ok(maliyet(c, "hakem", { input_tokens: 1e6 }) === 5);
});
