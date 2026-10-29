// Bildirim mantığı testleri (sabah/akşam mesaj seçimi)
import { test } from "node:test";
import assert from "node:assert/strict";
import { morningText, eveningText, due, DEF_SABAH } from "../functions/logic.js";

const ayse = { name: "Ayşe Yılmaz", weeks: { "2026-10-26": { "3": [{ t: "Problem 20 soru", done: true }, { t: "Paragraf", done: false }] } }, gunluk: {} };

test("sabah mesajında öğrencinin adı geçer ve ayarlar kapalıysa gönderilmez", () => {
  const m = morningText({}, ayse, "uid1", "2026-10-29");
  assert.ok(m.startsWith("Hayırlı sabahlar Ayşe"));
  assert.ok(DEF_SABAH.map(x => x.replace("{Ad}", "Ayşe")).includes(m));
  assert.equal(morningText({ sabahAcik: false }, ayse, "uid1", "2026-10-29"), null);
});

test("akşam: eksiği olmayana mesaj gitmez", () => {
  const tamam = { ...ayse, weeks: { "2026-10-26": { "3": [{ t: "x", done: true }] } }, gunluk: { "2026-10-29": 120 } };
  assert.equal(eveningText({}, tamam, "2026-10-29"), null);
});

test("akşam: eksiğe göre doğru mesaj grubu seçilir", () => {
  const set = { aksam: { sure: ["SURE {Ad}"], gorev: ["GOREV {Ad}"], ikisi: ["IKISI {Ad}"] } };
  assert.equal(eveningText(set, ayse, "2026-10-29"), "IKISI Ayşe");
  assert.equal(eveningText(set, { ...ayse, gunluk: { "2026-10-29": 30 } }, "2026-10-29"), "GOREV Ayşe");
  const isaretli = { ...ayse, weeks: { "2026-10-26": { "3": [{ t: "x", done: true }] } } };
  assert.equal(eveningText(set, isaretli, "2026-10-29"), "SURE Ayşe");
});

test("hafta başı görüşme gününden başlıyorsa doğru günün görevleri okunur", () => {
  const s = { name: "Ali Veli", donem: ["2026-10-28"], weeks: { "2026-10-28": { "1": [{ t: "x", done: false }] } }, gunluk: { "2026-10-29": 10 } };
  const set = { aksam: { sure: ["S"], gorev: ["G"], ikisi: ["I"] } };
  assert.equal(eveningText(set, s, "2026-10-29"), "G");
});

test("gönderim zamanı: saatten itibaren 1 saat içinde ve günde bir kez", () => {
  assert.equal(due("08:30", 8 * 60 + 29, "", "2026-10-29"), false);
  assert.equal(due("08:30", 8 * 60 + 30, "", "2026-10-29"), true);
  assert.equal(due("08:30", 9 * 60 + 45, "", "2026-10-29"), false);
  assert.equal(due("08:30", 8 * 60 + 45, "2026-10-29", "2026-10-29"), false);
});

test("ödeme hatırlatması: ödeme günü ve 5 gün sonra, ödendiyse ya da taslaksa gitmez", async () => {
  const L = await import("../functions/logic.js");
  const o = { bas: "2026-09-15", periyot: "ay", odenen: { "2026-09-15": { t: "2026-09-15" } } };
  assert.equal(L.odemeHatirlat(o, "2026-10-15"), "2026-10-15");
  assert.equal(L.odemeHatirlat(o, "2026-10-20"), "2026-10-15");
  assert.equal(L.odemeHatirlat(o, "2026-10-17"), null);
  assert.equal(L.odemeHatirlat(o, "2026-09-20"), null); /* ödenmiş */
  assert.equal(L.odemeHatirlat({ ...o, odenen: { ...o.odenen, "2026-10-15": {} } }, "2026-10-20"), null);
  assert.equal(L.odemeHatirlat({ ...o, taslak: true }, "2026-10-15"), null);
  assert.equal(L.addMonthsISO("2026-01-31", 1), "2026-02-28");
  assert.equal(L.vadeler({ bas: "2026-01-01", periyot: "hafta4" }, "2026-02-26").join(","), "2026-01-01,2026-01-29,2026-02-26");
});
