import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { yarisanlar, siralama, uyeDk, ODUL, tebrikMetni, duyuruMetni, gunEkle, haftaGunu } from "../functions/odul.js";

test("zek.js uygulama ve sunucuda aynı", () => {
  assert.equal(readFileSync(new URL("../public/zek.js", import.meta.url), "utf8"), readFileSync(new URL("../functions/zek.js", import.meta.url), "utf8"));
});
test("canlı özetten günün dakikası", () => {
  const c = { gun: "2026-11-12", bugunDk: 300, gunler: { "2026-11-11": 120 } };
  assert.equal(uyeDk(c, "2026-11-12"), 300); assert.equal(uyeDk(c, "2026-11-11"), 120); assert.equal(uyeDk(c, "2026-11-10"), 0);
});
test("sıralama: çalışmayan dışarıda, en çok çalışan önde; çalışma arkadaşları otomatik sınıfta yarışır", () => {
  const canli = new Map([["a", { takma: "Ali", gun: "2026-11-12", bugunDk: 900 }], ["b", { takma: "Ayşe", gun: "2026-11-12", bugunDk: 0 }], ["x", { takma: "Yabancı", gun: "2026-11-12", bugunDk: 999 }]]);
  const L = yarisanlar({ uyeler: ["a", "b"], oto: true }, canli);
  assert.equal(L.filter(x => x.zek).length, 10);
  const s = siralama(L, ["2026-11-12"], 5);
  assert.equal(s[0].uid, "a"); assert.ok(!s.some(x => x.uid === "b" || x.uid === "x")); assert.equal(s.length, 5);
  assert.equal(yarisanlar({ uyeler: ["a"], oto: true, zek: false }, canli).length, 1);
  assert.equal(yarisanlar({ uyeler: ["a"] }, canli).length, 1);
});
test("ödüller ve metinler", () => {
  assert.deepEqual(ODUL.hafta, [20, 10, 10, 5, 5]); assert.equal(ODUL.gun[0], 3);
  assert.match(tebrikMetni("gun", 1, 455, 3), /birincisi sendin! 7 sa 35 dk.*\+3 soru/);
  assert.match(tebrikMetni("hafta", 2, 600, 10), /2\. oldun! 🥈 10 sa/);
  assert.equal(duyuruMetni("hafta", [{ takma: "A", dk: 1 }, { takma: "B", dk: 1 }]), "📊 Haftanın ilk 5'i: 1. A · 2. B");
  assert.equal(gunEkle("2026-11-16", -7), "2026-11-09"); assert.equal(haftaGunu("2026-11-16"), 1);
});

test("yarış başlangıcı", async () => { const m = await import("../functions/odul.js"); assert.equal(m.ODUL_BASLA, "2026-11-16"); });
