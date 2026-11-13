import { test } from "node:test";
import assert from "node:assert/strict";
import { veliOzet, veliEposta, epostaGecerli, denemeNet } from "../functions/veli.js";
const s = { name: "Elif Demo", gunluk: { "2026-11-09": 320, "2026-11-10": 300, "2026-11-11": 310, "2026-11-12": 330, "2026-11-13": 305, "2026-11-14": 360, "2026-11-08": 999 },
  denemeler: [{ tur: "TYT", tarih: "2026-11-01", turkce: 30, sosyal: 12, mat: 20, fen: 10 }, { tur: "TYT", tarih: "2026-11-14", turkce: { d: 33, y: 4 }, sosyal: "13,5", mat: 22, fen: 11 }] };
test("e-posta adresi denetimi", () => { assert.ok(epostaGecerli("veli@ornek.com")); assert.ok(!epostaGecerli("veli@")); assert.ok(!epostaGecerli("")); });
test("deneme neti", () => { assert.equal(denemeNet(s.denemeler[1]), 78.5); });
test("haftalık özet", () => {
  const o = veliOzet(s, "2026-11-09");
  assert.equal(o.dk, 1925); assert.equal(o.gun, 6); assert.equal(o.durum, "harika");
  assert.equal(o.deneme.net, 78.5); assert.equal(o.deneme.fark, 6.5); assert.equal(o.enIyi.g, "Cmt"); assert.equal(o.gunler.length, 7);
  assert.equal(veliOzet({ name: "X" }, "2026-11-09").durum, "kayit-yok");
});
test("e-posta metni ayrıntıya girmez, sıralamayı yazar", () => {
  const e = veliEposta(s, veliOzet(s, "2026-11-09"), { sira: 2 });
  assert.equal(e.konu, "Elif'in haftalık özeti (9 Kasım – 15 Kasım)");
  assert.match(e.text, /Merhaba değerli velim,/); assert.match(e.text, /32 saat 5 dakika/); assert.match(e.text, /78,5 net \(\+6,5\)/); assert.match(e.text, /sınıfında 2\. oldu/);
  assert.match(e.html, /Zekacademy/); assert.doesNotMatch(e.text, /yanlış|konu/i);
});
test("görüşme ve YKS'ye kalan gün", () => {
  const o = veliOzet(s, "2026-11-09", { gorusmeler: [{ durum: "yapildi", tur: "seans" }], sinav: "2027-06-19", bugun: "2026-11-16" });
  assert.equal(o.gorusme, "yapildi"); assert.equal(o.kalan, 215);
  const e = veliEposta(s, o); assert.match(e.text, /Koçuyla haftalık görüşme: Yapıldı/); assert.match(e.text, /YKS'ye kalan: 215 gün/);
});
