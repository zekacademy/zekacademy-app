// Deneme karnesi okuma: modelin çıktısının doğrulanması (koçun gönderdiği gerçek örneklerden)
import { test } from "node:test";
import assert from "node:assert/strict";
import { karneDuzelt, karneIstegi, BOLUM } from "../functions/karne.js";

const BUGUN = "2026-11-10";

test("kurum karnesi (Hangi Kaynak, 3D TG TYT-1): ana satırlardan D/Y, net doğrulanır, geçmiş satırları ayrı", () => {
  const r = { okunabildi: true, belgeTuru: "karne", denemeler: [
    { tur: "TYT", yayin: "3D", sinavAdi: "3D TG TYT 1 2027", tarih: "2026-11-01", kaynak: "ana",
      bolumler: { turkce: { d: 33, y: 4, b: 3, net: 32 }, sosyal: { d: 20, y: 0, b: 0, net: 20 }, mat: { d: 35, y: 1, b: 4, net: 34.75 }, fen: { d: 18, y: 1, b: 1, net: 17.75 } },
      toplamNet: 104.5, puan: 442.9, siralama: "1.198/85.472", emin: true,
      yanlislar: [{ ders: "Matematik", no: 3, konu: "Rasyonel Sayılar", eslesen: "Rasyonel Sayılar", durum: "yanlis" }, { ders: "Kimya", no: 13, konu: "Atomun Yapısı", eslesen: "Atom ve Yapısı", durum: "yanlis" }, { ders: "Matematik", no: 1, konu: "Sayı Basamakları", eslesen: "Sayı Basamakları", durum: "bos" }] },
    { tur: "TYT", yayin: "Bilgi Sarmal", tarih: "2026-07-26", kaynak: "gecmis", bolumler: { turkce: { net: 30.25 }, sosyal: { net: 20 }, mat: { net: 30.25 }, fen: { net: 15 } }, toplamNet: 95.5 },
    { tur: "TYT", yayin: "3D", tarih: "2026-11-01", kaynak: "gecmis", bolumler: { turkce: { net: 32 }, sosyal: { net: 20 }, mat: { net: 34.75 }, fen: { net: 17.75 } }, toplamNet: 104.5 },
  ] };
  const o = karneDuzelt(r, BUGUN);
  assert.equal(o.denemeler.length, 2, "ana deneme geçmişte tekrar ediyorsa bir kez");
  const a = o.denemeler[0];
  assert.equal(a.kaynak, "ana"); assert.equal(a.toplam, 104.5); assert.deepEqual(a.bolumler.mat, { d: 35, y: 1 }); assert.equal(a.emin, true);
  assert.equal(a.yanlislar.filter(x => x.durum === "yanlis").length, 2);
  assert.deepEqual(o.denemeler[1].bolumler.turkce, { net: 30.25 }); assert.equal(o.denemeler[1].toplam, 95.5);
});

test("model ORT sütununu ya da yanlış neti okuduysa yakalanır", () => {
  const o = karneDuzelt({ denemeler: [{ tur: "TYT", bolumler: { turkce: { d: 37, y: 1, net: 27.87 } } }] }, BUGUN);
  assert.equal(o.denemeler[0].emin, false); assert.match(o.denemeler[0].notlar.join(), /hesaplanan 36.75/);
  assert.deepEqual(o.denemeler[0].bolumler.turkce, { d: 37, y: 1 });
});

test("el yazısı (Iceberg kapağı): yalnız net, toplam tutuyor", () => {
  const o = karneDuzelt({ belgeTuru: "el-yazisi", denemeler: [{ tur: "TYT", yayin: "Iceberg", tarih: null, bolumler: { turkce: { net: 35.25 }, sosyal: { net: 11.75 }, mat: { net: 30 }, fen: { net: 17.75 } }, toplamNet: 94.75 }] }, BUGUN);
  const d = o.denemeler[0]; assert.equal(d.toplam, 94.75); assert.equal(d.emin, true); assert.equal(d.tarih, null); assert.deepEqual(d.bolumler.fen, { net: 17.75 });
});

test("el yazısında toplam tutmazsa emin değil", () => {
  const o = karneDuzelt({ denemeler: [{ tur: "TYT", bolumler: { turkce: { net: 35.25 }, sosyal: { net: 11.75 }, mat: { net: 36 }, fen: { net: 17.75 } }, toplamNet: 94.75 }] }, BUGUN);
  assert.equal(o.denemeler[0].emin, false);
});

test("tablo (birden çok deneme, yalnız net): her satır ayrı; virgüllü sayı ve gelecek tarih düzeltilir", () => {
  const o = karneDuzelt({ belgeTuru: "tablo", denemeler: [
    { tur: "TYT", yayin: "345", sinavAdi: "345 son prova", tarih: "2026-08-20", bolumler: { turkce: { net: "36,25" }, sosyal: { net: 17.5 }, mat: { net: 26 }, fen: { net: 17.5 } }, toplamNet: 97.25 },
    { tur: "TYT", yayin: "Özdebir", tarih: "2026-09-16", bolumler: { turkce: { net: 32.5 }, sosyal: { net: 14 }, mat: { net: 23.25 }, fen: { net: 15.25 } }, toplamNet: 85 },
    { tur: "TYT", yayin: "Bilgi Sarmal", tarih: "2026-09-20", bolumler: { turkce: { net: 35 }, sosyal: { net: 12.5 }, mat: { net: 32.75 }, fen: { net: 16.25 } }, toplamNet: 96.5 },
    { tur: "TYT", yayin: "Limit", tarih: "2026-12-02", bolumler: { turkce: { net: 26.5 }, sosyal: { net: 12.25 }, mat: { net: 31.25 }, fen: { net: 13.75 } }, toplamNet: 83.75 },
  ] }, BUGUN);
  assert.equal(o.denemeler.length, 4);
  assert.deepEqual(o.denemeler.map(d => d.toplam).sort((a, b) => a - b), [83.75, 85, 96.5, 97.25]);
  const limit = o.denemeler.find(d => d.yayin === "Limit"); assert.equal(limit.tarih, "2025-12-02");
  assert.ok(o.denemeler.every(d => d.emin));
});

test("geçersiz sayılar ayıklanır, boş deneme atılır, okunamayan belge", () => {
  const o = karneDuzelt({ denemeler: [{ tur: "TYT", bolumler: { fen: { d: 25, y: 0 } } }, { tur: "AYT", bolumler: {} }] }, BUGUN);
  assert.equal(o.denemeler.length, 0);
  const o2 = karneDuzelt({ okunabildi: false, uyarilar: ["Fotoğraf çok bulanık"] }, BUGUN);
  assert.equal(o2.okunabildi, false); assert.deepEqual(o2.uyarilar, ["Fotoğraf çok bulanık"]); assert.equal(o2.denemeler.length, 0);
});

test("AYT bölümleri", () => {
  const o = karneDuzelt({ denemeler: [{ tur: "AYT", yayin: "Limit", tarih: "2026-11-01", bolumler: { mat: { d: 20, y: 8 }, fen: { d: 25, y: 4 }, sos1: null, sos2: null } }] }, BUGUN);
  assert.deepEqual(Object.keys(o.denemeler[0].bolumler), ["mat", "fen"]); assert.equal(o.denemeler[0].toplam, 42);
  assert.equal(BOLUM.AYT.length, 4);
});

test("istek metni: kritik kurallar ve konu listesi", () => {
  const t = karneIstegi({ bugun: BUGUN, alan: "SAY", sinif: "Mezun", konular: { TYT: { Kimya: ["Atom ve Yapısı", "Karışımlar"] } } });
  assert.match(t, /ORT/); assert.match(t, /SON N SINAVIN SONUÇLARI/); assert.match(t, /Atom ve Yapısı \| Karışımlar/); assert.match(t, /BUGÜN: 2026-11-10/);
  assert.match(t, /kurum adı .* yayın DEĞİLDİR/);
});

test("yalnız konu analizi sayfası: netler yanlış/boş/iptal listesinden sayılır", () => {
  const y = [
    ...[4, 9, 16].map(no => ({ ders: "Türkçe", no, konu: "x", durum: "yanlis" })), { ders: "Türkçe", no: 10, konu: "Çekim Ekleri", durum: "bos" },
    { ders: "Matematik", no: 3, konu: "Rasyonel Sayılar", eslesen: "Rasyonel Sayılar", durum: "yanlis" }, { ders: "Geometri", no: 33, konu: "Açı Kenar", durum: "yanlis" },
    { ders: "Matematik", no: 18, konu: "İPTAL", durum: "iptal" }, { ders: "Matematik", no: 1, konu: "Sayı Basamakları", durum: "bos" },
    { ders: "Tarih", no: 3, konu: "Kavimler Göçü", durum: "yanlis" }, { ders: "Kimya", no: 10, konu: "Asit", eslesen: "Asitler, Bazlar ve Tuzlar", durum: "yanlis" } ];
  const o = karneDuzelt({ belgeTuru: "konu-analizi", denemeler: [{ tur: "TYT", yayin: null, tarih: null, bolumler: {}, dersler: ["Türkçe", "Matematik", "Geometri", "Tarih", "Coğrafya", "Felsefe", "Din Kültürü", "Fizik", "Kimya", "Biyoloji"], yanlislar: y }] }, BUGUN);
  const d = o.denemeler[0];
  assert.equal(d.konudan, true);
  assert.deepEqual(d.bolumler.turkce, { d: 36, y: 3 }); assert.deepEqual(d.bolumler.mat, { d: 36, y: 2 }); assert.deepEqual(d.bolumler.sosyal, { d: 19, y: 1 }); assert.deepEqual(d.bolumler.fen, { d: 19, y: 1 });
  assert.match(d.notlar.join(), /iptal/); assert.match(d.notlar[0], /konu analizinden/);
});

test("konu analizi sayfasında bazı dersler yoksa o bölüm hesaplanmaz, yanlışlar yine gelir", () => {
  const o = karneDuzelt({ denemeler: [{ tur: "TYT", bolumler: {}, dersler: ["Türkçe", "Fizik"], yanlislar: [{ ders: "Türkçe", no: 2, durum: "yanlis" }, { ders: "Fizik", no: 1, durum: "yanlis", eslesen: "Basınç" }] }] }, BUGUN);
  const d = o.denemeler[0]; assert.deepEqual(Object.keys(d.bolumler), ["turkce"]); assert.equal(d.yanlislar.length, 2); assert.match(d.notlar.join(), /Fen Bilimleri: sayfada bütün/);
});

test("model kademesi: düzenli karne/tablo ucuz modelde kalır; el yazısı, konu analizi, tutarsızlık güçlü modele", async () => {
  const { karneZoraGec } = await import("../functions/karne.js");
  const tablo = { okunabildi: true, belgeTuru: "tablo", denemeler: [{ tur: "TYT", yayin: "345", tarih: "2026-08-20", bolumler: { turkce: { net: 36.25 }, sosyal: { net: 17.5 }, mat: { net: 26 }, fen: { net: 17.5 } }, toplamNet: 97.25 }] };
  assert.equal(karneZoraGec(tablo, karneDuzelt(tablo, BUGUN), "end_turn"), null);
  const karne = { okunabildi: true, belgeTuru: "karne", denemeler: [{ tur: "TYT", bolumler: { turkce: { d: 33, y: 4, net: 32 }, sosyal: { d: 20, y: 0, net: 20 }, mat: { d: 35, y: 1, net: 34.75 }, fen: { d: 18, y: 1, net: 17.75 } }, toplamNet: 104.5 }] };
  assert.equal(karneZoraGec(karne, karneDuzelt(karne, BUGUN)), null);
  const yanlisNet = { okunabildi: true, belgeTuru: "karne", denemeler: [{ tur: "TYT", bolumler: { turkce: { d: 33, y: 4, net: 30.23 } } }] };
  assert.equal(karneZoraGec(yanlisNet, karneDuzelt(yanlisNet, BUGUN)), "tutarsiz");
  const el = { okunabildi: true, belgeTuru: "el-yazisi", denemeler: [{ tur: "TYT", bolumler: { turkce: { net: 35.25 } } }] };
  assert.equal(karneZoraGec(el, karneDuzelt(el, BUGUN)), "zor-belge");
  const konu = { okunabildi: true, belgeTuru: "karne", denemeler: [{ tur: "TYT", bolumler: { turkce: { d: 33, y: 4 } }, yanlislar: [{ ders: "Türkçe", durum: "yanlis" }] }] };
  assert.equal(karneZoraGec(konu, karneDuzelt(konu, BUGUN)), "konu-esleme");
  assert.equal(karneZoraGec(null, null), "json-yok");
  assert.equal(karneZoraGec(tablo, karneDuzelt(tablo, BUGUN), "max_tokens"), "kesildi");
  assert.equal(karneZoraGec({ okunabildi: false }, karneDuzelt({ okunabildi: false }, BUGUN)), "okunamadi");
});
