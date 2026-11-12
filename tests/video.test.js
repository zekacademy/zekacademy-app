// Video Kütüphanesi yardımcıları: liste seçimi, bölümler, konu eşleştirme
import { test } from "node:test";
import assert from "node:assert/strict";
import { kanalUygun, listeSec, sinavlar, sureSn, bolumler, eslestir, bolumEkle } from "../tools/video-ortak.mjs";

test("sınav ve yıl: en güncel TYT/AYT konu anlatımı listesi seçilir, soru çözümü ve eski yıllar elenir", () => {
  const L = [
    { id: "PL_a", ad: "2026 TYT Matematik Kampı", sayi: 40 },
    { id: "PL_b", ad: "TYT Matematik Konu Anlatımı 2027", sayi: 45 },
    { id: "PL_c", ad: "2027 TYT Matematik Soru Çözümü", sayi: 60 },
    { id: "PL_d", ad: "AYT Matematik Kampı 2025", sayi: 50 },
    { id: "PL_e", ad: "2026-2027 AYT Matematik Konu Anlatımı", sayi: 55 },
    { id: "PL_f", ad: "9. Sınıf Matematik Maarif 2026", sayi: 20 },
    { id: "PL_g", ad: "TYT Fizik 2027", sayi: 30 },
  ];
  const s = listeSec(L, "mat");
  assert.deepEqual(s.map(x => [x.id, x.sinav]), [["PL_b", ["TYT"]], ["PL_e", ["AYT"]], ["PL_f", ["M9"]]]);
  assert.deepEqual(listeSec(L, "mat", ["TYT", "AYT"]).map(x => x.id), ["PL_f"]);
  assert.deepEqual(sinavlar("TYT-AYT Geometri Konu Anlatımı - 2027"), ["TYT", "AYT"]);
});

test("aynı kanalda birden çok hoca varsa filtre uygulanır", () => {
  const L = [{ id: "PL_1", ad: "2027 TYT Kimya - Ahmet Hoca", sayi: 30 }, { id: "PL_2", ad: "2027 / TYT Kimya Konu Anlatım Videoları - Görkem ŞAHİN", sayi: 25 }];
  assert.deepEqual(listeSec(L, "kim", [], "Görkem").map(x => x.id), ["PL_2"]);
});

test("süre ve açıklamadaki zaman damgalarından bölümler", () => {
  assert.equal(sureSn("PT1H2M3S"), 3723);
  assert.equal(sureSn("PT45M"), 2700);
  const d = "Merhaba\n00:00 Giriş\n03:15 - Sayı Problemleri\n(12:40) Kesir Problemleri\n1:05:00 Yaş Problemleri\nabone ol";
  assert.deepEqual(bolumler(d, 5000), [[0, "Giriş"], [195, "Sayı Problemleri"], [760, "Kesir Problemleri"], [3900, "Yaş Problemleri"]]);
  assert.deepEqual(bolumler("tek 00:00 yok\n02:00 Bir", 100), []);
});

test("konu ↔ video eşleştirme: başlıktan ya da uzun videonun bölümünden", () => {
  const V = [["v1", "Üslü Sayılar Konu Anlatımı | TYT 2027", 1800, []], ["v2", "Problemler Part-1", 7200, [[0, "Giriş"], [600, "Sayı Problemleri"], [1900, "Kesir Problemleri"]]]];
  const K = [{ k: "mat|Üslü Sayılar", ad: "Üslü Sayılar" }, { k: "prob|Kesir Problemleri", ad: "Kesir Problemleri" }, { k: "mat|Mutlak Değer", ad: "Mutlak Değer" }];
  assert.deepEqual(eslestir(K, V), { "mat|Üslü Sayılar": [["v1", 0]], "prob|Kesir Problemleri": [["v2", 1900]] });
  assert.deepEqual(bolumEkle("Sayı Problemleri", [["v2", 0]], V), [["v2", 600]]);
});

test("aramayla bulunan kanal hocanın adını taşımalı; Türkçe'de AYT listesi olmaz", () => {
  assert.equal(kanalUygun("Kolay Fizik", "Altuğ Güneş FİZİK"), false);
  assert.equal(kanalUygun("Kenan Kara", "Kenan Kara ile Geometri"), true);
  assert.equal(kanalUygun("Önder Hoca", "Kimya Rehberi"), false);
  assert.deepEqual(listeSec([{ id: "PL_t", ad: "2027 YKS | Dil Bilgisinin Ritmi | Yeni Kamp", sayi: 17 }], "tr", ["TYT"]), []);
  assert.equal(listeSec([{ id: "PL_d", ad: "2027 / TYT - AYT Din Kültürü ve Ahlak Bilgisi - Konu Anlatım Videoları", sayi: 16 }], "din").length, 1);
  assert.deepEqual(listeSec([{ id: "PL_y", ad: "40 Günde TYT Matematik Uçuş Kampı", sayi: 40, tarih: "2026-07-10T00:00:00Z" }, { id: "PL_z", ad: "TYT Matematik 2024", sayi: 40, tarih: "2026-07-10T00:00:00Z" }], "mat").map(x => x.id), ["PL_y"]);
  assert.deepEqual(listeSec([{ id: "PL_28", ad: "2028 TYT Matematik Kampı | Maarif Model 1. Aşama (9-10. Sınıf)", sayi: 100, tarih: "2026-08-01" }], "mat").map(x => x.sinav), [["M10"]]);
  assert.deepEqual(listeSec([{ id: "PL_sb", ad: "2028 YKS İçin Maarif Türkçe Kampı Soru Bankası Çözümleri", sayi: 100, tarih: "2026-08-01" }], "tr"), []);
  assert.deepEqual(listeSec([{ id: "PL_k", ad: "2026 KPSS - AYT TARİH DERSLERİ", sayi: 70 }], "tar"), []);
});

test("hocaların farklı konu adları: tarih yeni ünite adları, geometri temel kavramlar, konunun bütün videoları", () => {
  const V = [["a", "Doğruda Açılar-1 | 60 Günde Geometri", 1800, []], ["b", "Doğruda Açılar-2 | 60 Günde Geometri", 1800, []], ["c", "Üçgende Açı | 2.Hafta", 1800, []],
    ["d", "Türklerin İslamiyeti Kabulü - Konu Anlatımı", 1800, []], ["e", "Türklerin İslamiyeti Kabulü - Soru Çözümü", 1800, []], ["f", "KENARORTAY | 5.Hafta", 1800, []], ["g", "KENAR AÇI KENAR | 6.Hafta", 1800, []]];
  const E = eslestir([{ k: "geo|Temel Kavramlar", ad: "Temel Kavramlar" }, { k: "tar|İlk Türk İslam Devletleri", ad: "İlk Türk İslam Devletleri" }, { k: "geo|Kenarortay", ad: "Kenarortay" }, { k: "geo|Üçgende Açılar", ad: "Üçgende Açılar" }], V);
  assert.deepEqual(E["geo|Temel Kavramlar"], [["a", 0], ["b", 0]]);
  assert.deepEqual(E["tar|İlk Türk İslam Devletleri"], [["d", 0], ["e", 0]]);   /* konunun ardından gelen soru çözümü de alınır */
  assert.deepEqual(E["geo|Kenarortay"], [["f", 0]]);
  assert.deepEqual(E["geo|Üçgende Açılar"], [["c", 0]]);
});

test("güncel seri yoksa hocanın en son eski serisi alınır; güncel varsa o seçilir", () => {
  const L = [{ id: "PL_o1", ad: "2024 TYT TARİH KONU ANLATIM", sayi: 40, tarih: "2023-09-01" }, { id: "PL_o2", ad: "2022 TYT Tarih Konu Anlatımı", sayi: 40, tarih: "2021-09-01" }];
  assert.deepEqual(listeSec(L, "tar").map(x => [x.id, x.eski]), [["PL_o1", true]]);
  assert.deepEqual(listeSec([...L, { id: "PL_n", ad: "TYT Tarih Kampı 2027", sayi: 20, tarih: "2026-08-01" }], "tar").map(x => [x.id, x.eski]), [["PL_n", undefined]]);
  assert.deepEqual(listeSec([{ id: "PL_g", ad: "TYT - FİZİK - GENEL TEKRAR", sayi: 14, tarih: "2026-04-13" }], "fiz", [], "", "genel tekrar").map(x => x.id), ["PL_g"]);
});
