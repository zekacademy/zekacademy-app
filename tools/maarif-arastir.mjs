/* Maarif (9, 10, 11. sınıf ve 2028 1. Aşama) oynatma listesi araştırması: YouTube'da ders ders arar, kanal + liste + video sayısı raporu yazar.
   node tools/maarif-arastir.mjs   (YOUTUBE_API_KEY gerekli; ~4.500 birim) */
import fs from "node:fs";
const KEY = process.env.YOUTUBE_API_KEY; if (!KEY) { console.error("::error::YOUTUBE_API_KEY yok"); process.exit(2); }
let birim = 0;
async function yt(yol, p, b = 1) { const u = new URL("https://www.googleapis.com/youtube/v3/" + yol); Object.entries({ ...p, key: KEY }).forEach(([k, v]) => u.searchParams.set(k, v));
  const r = await fetch(u); birim += b; const j = await r.json(); if (!r.ok) throw new Error(j?.error?.errors?.[0]?.reason || r.status); return j; }
const DERS = { Matematik: "matematik", Fizik: "fizik", Kimya: "kimya", Biyoloji: "biyoloji", Edebiyat: "türk dili ve edebiyatı", Tarih: "tarih", "Coğrafya": "coğrafya", Felsefe: "felsefe" };
const SORGU = [["9", d => `9. sınıf ${d} maarif model konu anlatımı`], ["10", d => `10. sınıf ${d} maarif model konu anlatımı`], ["11", d => `11. sınıf ${d} maarif model konu anlatımı 2026-2027`], ["1A", d => `2028 maarif model 1. aşama ${d} kampı`]];
const EK = ["Yaşar Hoca MathMan maarif", "Sinan İhtiyaroğlu maarif", "2028 YKS maarif model TYT kampı", "maarif model 1. oturum kampı 9 10. sınıf"];
const L = new Map(), hata = [];
async function ara(q, ders, sinif) { try { const j = await yt("search", { part: "snippet", type: "playlist", q, maxResults: 50, regionCode: "TR", relevanceLanguage: "tr" }, 100);
  for (const it of j.items || []) { const id = it.id?.playlistId; if (!id) continue; const x = L.get(id) || { id, ad: it.snippet.title, kanal: it.snippet.channelTitle, kanalId: it.snippet.channelId, tarih: (it.snippet.publishedAt || "").slice(0, 10), bulundu: [] }; x.bulundu.push(`${ders}/${sinif}`); L.set(id, x); } } catch (e) { hata.push(`${q}: ${e.message}`); } }
for (const [ders, d] of Object.entries(DERS)) for (const [s, f] of SORGU) { if (ders === "Felsefe" && s === "9") continue; await ara(f(d), ders, s); }
for (const q of EK) await ara(q, "ek", "-");
const ids = [...L.keys()];
for (let i = 0; i < ids.length; i += 50) { try { const j = await yt("playlists", { part: "contentDetails,snippet", id: ids.slice(i, i + 50).join(","), maxResults: 50 }); for (const p of j.items || []) { const x = L.get(p.id); x.sayi = p.contentDetails?.itemCount; x.ad = p.snippet.title; } } catch (e) { hata.push("playlists: " + e.message); } }
const sade = x => String(x || "").toLocaleLowerCase("tr");
const sinifOf = ad => { const n = sade(ad), S = []; for (const g of ["9", "10", "11"]) if (new RegExp(`(^|[^0-9])${g}\\s*\\.?\\s*s[ıi]n[ıi]f`).test(n)) S.push(g); if (/2028|1\.?\s*(aşama|oturum)|ilk aşama/.test(n)) S.push("1A"); return S; };
const dersOf = ad => { const n = sade(ad); return Object.entries({ Matematik: /matemat|geometri/, Fizik: /fizik/, Kimya: /kimya/, Biyoloji: /biyoloji/, Edebiyat: /edebiyat|türkçe|paragraf|dil bilgisi/, Tarih: /tarih|inkılap/, "Coğrafya": /coğrafya/, Felsefe: /felsefe/ }).filter(([, r]) => r.test(n)).map(([k]) => k); };
const R = [...L.values()].map(x => ({ ...x, sinif: sinifOf(x.ad), ders: dersOf(x.ad) })).filter(x => x.sinif.length && x.ders.length && (x.sayi || 0) >= 5 && x.tarih >= "2024-08" && !/\b[5-8]\s*\.?\s*s[ıi]n[ıi]f|lgs|kpss|ags/.test(sade(x.ad)));
fs.writeFileSync("data/maarif-arastirma.json", JSON.stringify({ at: new Date().toISOString(), birim, hata, listeler: R }, null, 1));
let md = `# Maarif oynatma listesi araştırması (${new Date().toISOString().slice(0, 10)})\n\n${R.length} liste, ${new Set(R.map(x => x.kanalId)).size} kanal. Kota: ~${birim} birim.${hata.length ? "\n\nHatalar: " + hata.join("; ") : ""}\n`;
for (const ders of Object.keys(DERS)) { md += `\n## ${ders}\n| Kanal | Sınıf | Liste | Video | Açılış |\n|---|---|---|---|---|\n`;
  for (const x of R.filter(x => x.ders.includes(ders)).sort((a, b) => a.kanal.localeCompare(b.kanal, "tr") || a.sinif[0].localeCompare(b.sinif[0], "tr", { numeric: true }))) md += `| ${x.kanal} | ${x.sinif.join(", ")} | ${x.ad.replace(/\|/g, "/")} | ${x.sayi} | ${x.tarih} |\n`; }
fs.writeFileSync("data/maarif-arastirma.md", md); console.log(md.slice(0, 3000));
