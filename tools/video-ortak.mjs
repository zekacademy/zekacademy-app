/* Video Kütüphanesi: saf yardımcılar (ağ yok). youtube-listeler.mjs ve testler kullanır. */

/* Uygulamadaki video dersleri ve konu listesindeki ders anahtarları (TYT / AYT / Maarif dk) */
export const VDERS = {
  mat: { TYT: ["mat", "prob", "matd"], AYT: ["amat"], M: ["mat"], re: /matematik|problem/ },
  geo: { TYT: ["geo"], AYT: ["geo"], M: [], re: /geometri/ },
  fiz: { TYT: ["fiz"], AYT: ["afiz"], M: ["fiz"], re: /fizik/ },
  kim: { TYT: ["kim"], AYT: ["akim"], M: ["kim"], re: /kimya/ },
  bio: { TYT: ["bio"], AYT: ["abio"], M: ["bio"], re: /biyoloji/ },
  tr: { TYT: ["tr"], AYT: [], M: [], re: /turkce|paragraf|dil ?bilgisi/ },
  ede: { TYT: [], AYT: ["aede"], M: ["tde"], re: /edebiyat/ },
  tar: { TYT: ["tar"], AYT: ["atar"], M: ["tar"], re: /tarih|inkilap/ },
  cog: { TYT: ["cog"], AYT: ["acog"], M: ["cog"], re: /cografya/ },
  fel: { TYT: ["fel"], AYT: ["afel"], M: ["fel"], re: /felsefe|mantik|psikoloji|sosyoloji/ },
  din: { TYT: [], AYT: [], M: [], re: /din kulturu|din\b/ },
};

/* Türkçe harfleri sadeleştirip küçült */
export function sade(x) {
  return String(x || "").toLocaleLowerCase("tr")
    .replace(/ı/g, "i").replace(/ş/g, "s").replace(/ğ/g, "g").replace(/ü/g, "u").replace(/ö/g, "o").replace(/ç/g, "c").replace(/â/g, "a").replace(/î/g, "i").replace(/û/g, "u")
    .replace(/[^a-z0-9]+/g, " ").trim();
}

/* Liste adından sınav: TYT, AYT, M9, M10, M11 */
export function sinavlar(ad) {
  const n = sade(ad), L = [];
  if (/\btyt\b/.test(n)) L.push("TYT");
  if (/\bayt\b/.test(n)) L.push("AYT");
  const m = n.match(/\b(9|10|11)\s*(?:\.|uncu|nci|ncu)?\s*sinif/);
  if (m) L.push("M" + m[1]);
  if (!L.length && /\byks\b/.test(n)) L.push("TYT", "AYT");
  return L;
}

/* Liste adının yıl puanı: 2027 ya da 2026-2027 en güncel (3), 2026 (2), daha eski (0) */
export function yilPuan(ad) {
  const n = String(ad || "");
  if (/2027/.test(n)) return 3;
  if (/2026/.test(n)) return 2;
  return 0;
}

const DISLA = /soru ?coz|soru bankasi|deneme|shorts|tanitim|motivasyon|canli|kitap|taktik|tekrar(?! kampi)|ozet|son tekrar/;

/* Bir kanalın oynatma listelerinden, eksik sınavlar için en güncel konu anlatımı listesini seç.
   L: [{id, ad, sayi, tarih}], ders: VDERS anahtarı, sabit: elle seçilmiş listelerin kapsadığı sınavlar */
export function listeSec(L, ders, sabit = [], filtre = "") {
  const re = VDERS[ders].re, f = sade(filtre), secim = {};
  for (const p of L) {
    const n = sade(p.ad);
    if (!re.test(n) || (DISLA.test(n) && !/konu anlatim|kamp/.test(n)) || (f && !n.includes(f)) || (p.sayi != null && p.sayi < 3)) continue;
    const yp = yilPuan(p.ad); if (!yp) continue;
    for (const s of sinavlar(p.ad)) {
      if (sabit.includes(s)) continue;
      if (s.startsWith("M") && !VDERS[ders].M.length) continue;
      const puan = yp * 1000 + (/konu|kamp|anlatim/.test(n) ? 300 : 0) + Math.min(200, p.sayi || 0) + (p.tarih ? Date.parse(p.tarih) / 1e12 : 0);
      if (!secim[s] || puan > secim[s].puan) secim[s] = { ...p, puan };
    }
  }
  /* Aynı liste birden çok sınavı kapsıyorsa tek kayıt */
  const out = {};
  for (const [s, p] of Object.entries(secim)) { (out[p.id] = out[p.id] || { id: p.id, ad: p.ad, sinav: [] }).sinav.push(s); }
  return Object.values(out);
}

/* ISO 8601 süre → saniye */
export function sureSn(iso) {
  const m = String(iso || "").match(/P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?/);
  if (!m) return 0;
  return (+m[1] || 0) * 86400 + (+m[2] || 0) * 3600 + (+m[3] || 0) * 60 + (+m[4] || 0);
}

/* Açıklamadaki zaman damgalarından bölümler: [[saniye, "ad"], ...] (en az 2 bölüm, artan sırada) */
export function bolumler(aciklama, sure = 0) {
  const out = [];
  for (const satir of String(aciklama || "").split(/\r?\n/)) {
    const m = satir.match(/^\s*[\[(]?((?:\d{1,2}:)?\d{1,2}:\d{2})[\])]?\s*(?:[-–—:|.)]\s*)?(.{2,90}?)\s*$/);
    if (!m) continue;
    const p = m[1].split(":").map(Number), sn = p.length === 3 ? p[0] * 3600 + p[1] * 60 + p[2] : p[0] * 60 + p[1];
    const ad = m[2].replace(/^[-–—:|.\s]+/, "").trim();
    if (!ad || (sure && sn >= sure) || (out.length && sn <= out[out.length - 1][0])) continue;
    out.push([sn, ad]);
  }
  return out.length >= 2 ? out : [];
}

/* Konu adı ↔ video/bölüm adı eşleştirme */
const BOS = new Set("konu anlatimi anlatim tyt ayt yks 2027 2026 2025 kampi kamp gun gunde ders dersi video pdf tek videolar full ozet ve ile part bolum hoca hocam soru cozumu kodlarla 1 2 3 4 5 i ii iii giris".split(" "));
export const kelime = x => sade(x).split(" ").filter(w => w && !BOS.has(w));
const kok = w => w.slice(0, Math.min(w.length, 5));
export function benzerlik(konu, baslik) {
  const K = kelime(konu), B = kelime(baslik).map(kok);
  if (!K.length || !B.length) return 0;
  const tut = K.filter(w => B.includes(kok(w))).length;
  return tut / K.length - (B.length > K.length + 4 ? 0.05 : 0);
}

/* Konuları videolara eşle. konular: [{k, ad}], videolar: [[id, başlık, süre, bölümler]] → {k: [[id, sn]]} */
export function eslestir(konular, videolar, esik = 0.75) {
  const out = {};
  for (const { k, ad } of konular) {
    let en = null;
    for (const v of videolar) {
      const p = benzerlik(ad, v[1]);
      if (p >= esik && (!en || p > en.p)) en = { p, v: [v[0], 0] };
      for (const [sn, bad] of v[3] || []) {
        const q = benzerlik(ad, bad) - 0.01;
        if (q >= esik && (!en || q > en.p)) en = { p: q, v: [v[0], sn] };
      }
    }
    if (en) out[k] = [en.v];
  }
  return out;
}

/* Elle eşlenmiş videoyu (konu → video) bölüm dakikasıyla zenginleştir: uzun videoda konunun bölümü varsa oradan başlasın */
export function bolumEkle(ad, parca, videolar) {
  return parca.map(([id, sn]) => {
    if (sn) return [id, sn];
    const v = videolar.find(x => x[0] === id); if (!v || !(v[3] || []).length) return [id, 0];
    let en = null; for (const [s, b] of v[3]) { const p = benzerlik(ad, b); if (p >= 0.75 && (!en || p > en.p)) en = { p, s }; }
    return [id, en ? en.s : 0];
  });
}
