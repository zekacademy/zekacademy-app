/* Video Kütüphanesi listelerini hazırlar.
   node tools/youtube-listeler.mjs            → sadece derler (önbellek + elle eşleme → public/video/<ders>.json)
   node tools/youtube-listeler.mjs --cek      → önce YouTube Data API v3'ten çeker (YOUTUBE_API_KEY gerekli), sonra derler
   node tools/youtube-listeler.mjs --cek --ders mat,fiz   → sadece bu dersler
   Anahtar asla dosyaya ya da çıktıya yazılmaz. */
import fs from "node:fs";
import path from "node:path";
import { VDERS, ALT_SINIF, sade, kanalUygun, listeSec, sureSn, bolumler, eslestir, bolumEkle } from "./video-ortak.mjs";

const KOK = path.resolve(path.dirname(new URL(import.meta.url).pathname), "..");
const oku = (p, yoksa) => { try { return JSON.parse(fs.readFileSync(path.join(KOK, p), "utf8")); } catch { return yoksa; } };
const yaz = (p, v, girinti) => { fs.mkdirSync(path.dirname(path.join(KOK, p)), { recursive: true }); fs.writeFileSync(path.join(KOK, p), JSON.stringify(v, null, girinti) + "\n"); };
const arg = process.argv.slice(2), CEK = arg.includes("--cek");
const SADECE = (arg[arg.indexOf("--ders") + 1] || "").split(",").filter(x => arg.includes("--ders") && x);

const KAYNAK = oku("data/video-kaynak.json").dersler;
const ELLE = oku("data/video-eslestirme.json", { konular: {}, kanallar: {} });
const KANAL = oku("data/video-kanallar.json", {});

/* Uygulamadaki konu listeleri (CUR ve MAARIF), app.js'ten okunur */
const APP = fs.readFileSync(path.join(KOK, "public/app.js"), "utf8");
const CUR = JSON.parse(APP.match(/^const CUR = (\{.*\});$/m)[1]);
const MAARIF = JSON.parse(APP.match(/^const MAARIF = (\[.*\]);$/m)[1]);
function konuListesi(ders, sinav) {
  const V = VDERS[ders], L = [];
  if (sinav === "TYT" || sinav === "AYT") CUR[sinav].filter(s => V[sinav].includes(s.k)).forEach(s => s.t.forEach(ad => L.push({ k: s.k + "|" + ad, ad })));
  else { const sn = +sinav.slice(1); MAARIF.filter(x => x.s === sn && V.M.includes(x.dk)).forEach(x => x.t.forEach(([, t], i) => t.forEach(ad => L.push({ k: `m${x.s}${x.dk}${i + 1}|${ad}`, ad })))); }
  return L;
}

/* ---------- YouTube Data API v3 ---------- */
let BIRIM = 0;
const ANAHTAR = process.env.YOUTUBE_API_KEY || "";
async function yt(yol, p, birim = 1) {
  const u = new URL("https://www.googleapis.com/youtube/v3/" + yol);
  Object.entries({ ...p, key: ANAHTAR }).forEach(([k, v]) => u.searchParams.set(k, v));
  for (let deneme = 0; deneme < 3; deneme++) {
    const r = await fetch(u); BIRIM += birim;
    if (r.ok) return r.json();
    const j = await r.json().catch(() => ({})), neden = j?.error?.errors?.[0]?.reason || r.status;
    if (neden === "quotaExceeded" || neden === "dailyLimitExceeded") throw new Error("Günlük YouTube kotası doldu; yarın tekrar çalıştır.");
    if (neden === "keyInvalid" || neden === "badRequest" && /key/i.test(j?.error?.message || "")) throw new Error("YOUTUBE_API_KEY geçersiz görünüyor (Cloud Console'da anahtarı ve YouTube Data API v3 kısıtını kontrol et).");
    if (neden === "accessNotConfigured" || r.status === 403 && /not been used|disabled/i.test(j?.error?.message || "")) throw new Error("Bu projede YouTube Data API v3 etkin değil (Cloud Console → API'ler → YouTube Data API v3 → Etkinleştir).");
    if (r.status === 404 || neden === "playlistNotFound" || neden === "channelNotFound") return { items: [] };
    if (r.status < 500) throw new Error(`YouTube ${yol}: ${neden}`);
    await new Promise(z => setTimeout(z, 1500 * (deneme + 1)));
  }
  throw new Error(`YouTube ${yol}: sunucu yanıt vermedi`);
}
async function tumSayfalar(yol, p, max = 20) { const L = []; let token = "";
  for (let i = 0; i < max; i++) { const j = await yt(yol, { ...p, maxResults: 50, ...(token ? { pageToken: token } : {}) }); L.push(...(j.items || [])); token = j.nextPageToken; if (!token) break; }
  return L; }
const gecerliId = id => /^(PL|UU|OL|FL)[A-Za-z0-9_-]{16,}$/.test(id || "") && id.length >= 18 && id.length !== 13;

async function kanalBul(h) {
  if (h.kanalId) { KANAL[h.ad] = { id: h.kanalId, nasil: "kimlik" }; return h.kanalId; }
  const yanlis = h.yanlisKanal || [];
  if (KANAL[h.ad]?.id && !yanlis.includes(KANAL[h.ad].id) && (KANAL[h.ad].nasil !== "arama" || kanalUygun(h.ad, KANAL[h.ad].ad))) return KANAL[h.ad].id;
  delete KANAL[h.ad];
  let id = "", nasil = "";
  if (h.kanal) { const j = await yt("channels", { part: "id,snippet", forHandle: h.kanal }); id = j.items?.[0]?.id || ""; nasil = "@ad"; }
  if (!id) { const sabit = (h.listeler || []).find(l => gecerliId(l.id)); if (sabit) { const j = await yt("playlists", { part: "snippet", id: sabit.id }); id = j.items?.[0]?.snippet?.channelId || ""; nasil = "liste"; } }
  if (!id && h.ara) { const j = await yt("search", { part: "snippet", type: "channel", q: h.ara, maxResults: 3, regionCode: "TR", relevanceLanguage: "tr" }, 100); const it = (j.items || []).find(x => !yanlis.includes(x.id?.channelId) && kanalUygun(h.ad, x.snippet.channelTitle)); id = it?.id?.channelId || ""; nasil = "arama"; if (it) KANAL[h.ad] = { id, ad: it.snippet.channelTitle, nasil, kontrol: true }; }
  if (id && !KANAL[h.ad]) KANAL[h.ad] = { id, nasil };
  return id;
}
async function videolar(listeId) {
  const items = await tumSayfalar("playlistItems", { part: "contentDetails,snippet", playlistId: listeId });
  const ids = [...new Set(items.map(i => i.contentDetails?.videoId).filter(Boolean))], V = new Map();
  for (let i = 0; i < ids.length; i += 50) {
    const j = await yt("videos", { part: "contentDetails,snippet,status", id: ids.slice(i, i + 50).join(",") });
    for (const v of j.items || []) { if (v.status?.privacyStatus === "private") continue; const s = sureSn(v.contentDetails?.duration);
      V.set(v.id, [v.id, v.snippet.title, s, bolumler(v.snippet.description, s), v.status?.embeddable === false ? 0 : 1]); }
  }
  return ids.filter(id => V.has(id)).map(id => V.get(id));
}
async function dersCek(ders) {
  const onb = oku(`data/youtube/${ders}.json`, {}), rapor = [];
  for (const h of KAYNAK[ders].hocalar) {
    try {
      const kid = await kanalBul(h);
      if (!kid) { delete onb[h.ad]; rapor.push(`- ${h.ad}: kanal bulunamadı (data/video-kaynak.json'a "kanal": "@..." ekle)`); continue; }
      const sabit = h.listeler || [], kapsanan = sabit.flatMap(l => l.sinav || []);
      let kanalListeleri = null;
      const kanalL = async () => kanalListeleri ??= (await tumSayfalar("playlists", { part: "snippet,contentDetails", channelId: kid }, 6)).map(p => ({ id: p.id, ad: p.snippet.title, sayi: p.contentDetails?.itemCount, tarih: p.snippet.publishedAt }));
      const secilen = [];
      for (const l of sabit) { let id = gecerliId(l.id) ? l.id : ""; if (!id) { const k = (await kanalL()).find(p => p.ad.trim() === l.ad.trim()) || (await kanalL()).find(p => p.ad.toLocaleLowerCase("tr").includes(l.ad.toLocaleLowerCase("tr").slice(0, 18))); id = k?.id || ""; }
        if (id) secilen.push({ id, ad: l.ad, sinav: l.sinav, elle: true }); else rapor.push(`- ${h.ad}: "${l.ad}" listesi kanalda bulunamadı`); }
      secilen.push(...listeSec(await kanalL(), ders, kapsanan, h.filtre || ""));
      const L = [];
      for (const l of secilen) { const v = await videolar(l.id); if (v.length) L.push({ ...l, v }); }
      onb[h.ad] = { kanal: kid, at: new Date().toISOString().slice(0, 10), listeler: L, kanaldakiler: (kanalListeleri || []).map(p => [p.id, p.ad, p.sayi, (p.tarih || "").slice(0, 10)]) };
      rapor.push(`- ${h.ad}: ${L.map(l => `${l.ad} [${l.sinav.join("/")}] · ${l.v.length} video`).join("; ") || "uygun güncel liste yok"}${KANAL[h.ad]?.kontrol ? ` ⚠️ kanal aramayla bulundu (${KANAL[h.ad].ad}), kontrol et` : ""}`);
    } catch (e) { if (/kota|anahtar|API v3/i.test(e.message)) throw e; rapor.push(`- ${h.ad}: hata (${e.message})`); }
  }
  yaz(`data/youtube/${ders}.json`, onb);
  return rapor;
}

/* ---------- Derleme: uygulamanın okuduğu public/video/<ders>.json ---------- */
const SINAV_SIRA = ["TYT", "AYT", "M9", "M10", "M11"];
function derle(ders) {
  const K = KAYNAK[ders], onb = oku(`data/youtube/${ders}.json`, {}), ozet = [];
  const hocalar = K.hocalar.map(h => {
    let listeler = (onb[h.ad]?.listeler || []).filter(l => l.elle || !ALT_SINIF.test(sade(l.ad))).map(l => ({ id: l.id, ad: l.ad, s: l.sinav, v: l.v.filter(v => !/#shorts/i.test(v[1]) && !(v[2] && v[2] < 90)).map(v => v.slice(0, 4).concat(v[4] === 0 ? [0] : [])) }));
    /* Elle eşleme (önceki çalışma): konu → video */
    const elle = Object.entries(ELLE.konular).filter(([k, x]) => x.hoca === h.ad && SINAV_SIRA.slice(0, 2).some(s => VDERS[ders][s].includes(k.split("|")[0]) || (ders === "tr" && k.startsWith("tr|"))));
    if (!listeler.length && elle.length) { /* API verisi gelene kadar elle eşlenen videolardan liste */
      const gruplar = {}; elle.forEach(([, x]) => x.parca.forEach(p => { const g = gruplar[x.kaynak] = gruplar[x.kaynak] || []; if (!g.some(v => v[0] === p[0])) g.push([p[0], p[1], 0, []]); }));
      listeler = Object.entries(gruplar).map(([ad, v]) => ({ id: "", ad, s: /geometri/i.test(ad) ? ["TYT", "AYT"] : ["TYT"], v }));
    }
    const tum = listeler.flatMap(l => l.v), konu = {};
    for (const s of SINAV_SIRA) { const ls = listeler.filter(l => l.s.includes(s)); if (!ls.length) continue; Object.assign(konu, eslestir(konuListesi(ders, s), ls.flatMap(l => l.v))); }
    /* Bir sınavın listesinde olmayan konu, hocanın öbür sınav listesinde varsa oradan (ör. TYT Polinomlar → AYT listesi) */
    for (const s of ["TYT", "AYT"]) { if (!listeler.some(l => l.s.includes(s))) continue; const eksik = konuListesi(ders, s).filter(x => !konu[x.k]); const obur = listeler.filter(l => !l.s.includes(s)).flatMap(l => l.v); if (eksik.length && obur.length) Object.assign(konu, eslestir(eksik, obur)); }
    /* AYT Felsefe Grubu: konu = dersin kendisi (Psikoloji, Sosyoloji, Mantık…). Adı liste adında geçiyorsa o listenin videoları; Felsefe = "Felsefe Grubu" listesi ya da TYT felsefe konu listesi */
    if (ders === "fel" && listeler.length) { delete konu["afel|Felsefe"]; delete konu["afel|Din"];
      for (const { k, ad } of konuListesi("fel", "AYT")) { const a = sade(ad);
        const l = listeler.find(l => l.s.includes("AYT") && sade(l.ad).includes(a) && !/felsefe grubu/.test(sade(l.ad))) || (ad === "Felsefe" && (listeler.find(l => /felsefe grubu/.test(sade(l.ad))) || listeler.find(l => l.s.includes("TYT") && /felsefe/.test(sade(l.ad)) && !/soru/.test(sade(l.ad)))));
        if (l) konu[k] = l.v.slice(0, 30).map(v => [v[0], 0]); } }
    for (const [k, x] of elle) konu[k] = bolumEkle(k.split("|")[1], x.parca.map(p => [p[0], p[3] ? p[3] * 60 : 0]), tum);
    const toplam = SINAV_SIRA.filter(s => listeler.some(l => l.s.includes(s))).reduce((a, s) => a + konuListesi(ders, s).length, 0);
    ozet.push(`- ${h.ad}: ${listeler.length} liste, ${tum.length} video, ${Object.keys(konu).length}/${toplam} konu eşlendi`);
    return { ad: h.ad, rol: h.rol, ...(h.kanal ? { kanal: h.kanal } : {}), listeler, konu };
  });
  yaz(`public/video/${ders}.json`, { ders, ad: K.ad, guncel: new Date().toISOString().slice(0, 10), hocalar });
  return ozet;
}

const dersler = Object.keys(KAYNAK).filter(d => !SADECE.length || SADECE.includes(d));
let md = `# Video Kütüphanesi raporu (${new Date().toISOString().slice(0, 10)})\n\n`;
if (CEK) {
  if (!ANAHTAR) { console.error("::error::YOUTUBE_API_KEY sırrı yok. GitHub → Settings → Secrets and variables → Actions → New repository secret: adı YOUTUBE_API_KEY. Ekledikten sonra iş akışını yeniden çalıştır."); process.exit(2); }
  for (const d of dersler) { md += `## ${KAYNAK[d].ad} (çekilen)\n${(await dersCek(d)).join("\n")}\n\n`; yaz("data/video-kanallar.json", KANAL, 1); }
  md += `Kullanılan kota: ~${BIRIM} birim (günlük sınır 10.000)\n\n`;
}
for (const d of Object.keys(KAYNAK)) md += `## ${KAYNAK[d].ad}\n${derle(d).join("\n")}\n\n`;
fs.writeFileSync(path.join(KOK, "data/video-rapor.md"), md);
console.log(md);
