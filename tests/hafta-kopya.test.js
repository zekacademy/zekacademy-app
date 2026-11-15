import { test } from "node:test";
import assert from "node:assert/strict";
import { kopyaPlani } from "../tools/hafta-kopya.mjs";
const a = { weeks: { "2026-11-09": { 0: [{ id: "x", t: "Paragraf 20 soru", done: true }], 3: [{ id: "y", d: "Matematik", t: "Türev", soru: 40 }] } },
  plan: { "2026-11-09": { saat: { 0: 6, 3: 7 }, hedef: { Matematik: { konu: "Türev", done: true } } } } };
test("önceki haftanın günleri aynı güne, işaretsiz kopyalanır", () => {
  const { yaz, ozet } = kopyaPlani(a), m = Object.fromEntries(yaz.map(([p, v]) => [p.join("/"), v]));
  assert.deepEqual(ozet, { gorev: 2, gun: 2, dolu: [], saat: 2, hedef: 1 });
  assert.equal(m["weeks/2026-11-16/0"][0].t, "Paragraf 20 soru"); assert.equal(m["weeks/2026-11-16/0"][0].done, false);
  assert.equal(m["weeks/2026-11-16/3"][0].t, "Matematik · Türev · 40 soru");
  assert.equal(m["plan/2026-11-16/saat/3"], 7); assert.deepEqual(m["plan/2026-11-16/hedef/Matematik"], { konu: "Türev", done: false });
});
test("yeni haftada dolu olan hiçbir şeyin üstüne yazılmaz", () => {
  const b = { ...a, weeks: { ...a.weeks, "2026-11-16": { 0: [{ t: "Koçun girdiği" }] } }, plan: { ...a.plan, "2026-11-16": { saat: { 0: 9 }, hedef: { Matematik: { konu: "İntegral" } } } } };
  const yollar = kopyaPlani(b).yaz.map(([p]) => p.join("/"));
  assert.deepEqual(yollar, ["weeks/2026-11-16/3", "plan/2026-11-16/saat/3"]);
});
test("perşembe başlayan program haftası", () => {
  const c = { donem: ["2026-11-05", "2026-11-12"], weeks: { "2026-11-12": { 0: [{ t: "Per" }], 4: [{ t: "Pzt" }] } }, plan: { "2026-11-12": { hedef: { Fizik: { konu: "Optik" } } } } };
  const yollar = kopyaPlani(c).yaz.map(([p]) => p.join("/"));
  assert.deepEqual(yollar, ["weeks/2026-11-19/0", "plan/2026-11-19/hedef/Fizik"]);
});
test("önceki haftası boş öğrenciye bir şey yazılmaz", () => { assert.equal(kopyaPlani({}).yaz.length, 0); });
