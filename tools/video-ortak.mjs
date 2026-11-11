/* Video Kütüphanesi: saf yardımcılar (ağ yok). youtube-listeler.mjs ve testler kullanır. */

/* Uygulamadaki video dersleri ve konu listesindeki ders anahtarları (TYT / AYT / Maarif dk) */
export const VDERS = {
  mat: { TYT: ["mat", "prob", "matd"], AYT: ["amat"], M: ["mat"], re: /matematik|problem/ },
  geo: { TYT: ["geo"], AYT: ["geo"], M: [], re: /geometri/ },
  fiz: { TYT: ["fiz"], AYT: ["afiz"], M: ["fiz"], re: /fizik/ },
  kim: { TYT: ["kim"], AYT: ["akim"], M: ["kim"], re: /kimya/ },
  bio: { TYT: ["bio"], AYT: ["abio"], M: ["bio"], re: /biyoloji/ },
  tr: { TYT: ["tr"], AYT: [], M: [], yok: ["AYT"], re: /turkce|paragraf|dil ?bilgisi/ },
  ede: { TYT: [], AYT: ["aede"], M: ["tde"], yok: ["TYT"], re: /edebiyat/ },
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
/* Adında sınav geçmeyen liste: Türkçe → TYT, Edebiyat → AYT */
const VARSAYILAN = { tr: ["TYT"], ede: ["AYT"] };

/* Liste adının yıl puanı: 2027 ya da 2026-2027 en güncel (3), 2026 (2), daha eski (0) */
export function yilPuan(ad, tarih) {
  const n = String(ad || "");
  if (/2027/.test(n)) return 3;
  if (/2026/.test(n)) return 2;
  if (/20(1\d|2[0-5])/.test(n)) return 0;   /* adında eski yıl var */
  /* Adında yıl yoksa listenin açıldığı tarihe bak: 2026 yazından sonra açılan 2027 sezonu, öncesindeki yıl 2026 sezonu */
  const t = String(tarih || "");
  if (t >= "2026-06") return 3;
  if (t >= "2025-06") return 2;
  return 0;
}

const DISLA = /\b[5-8] ?(?:\.|inci|nci)? ?sinif|lgs|ortaokul|kpss|\bags\b|oabt|sorular|soru ?coz|soru bankasi|deneme|shorts|tanitim|motivasyon|canli|kitap|taktik|tekrar(?! kampi)|ozet|son tekrar/;

/* Bir kanalın oynatma listelerinden, eksik sınavlar için en güncel konu anlatımı listesini seç.
   L: [{id, ad, sayi, tarih}], ders: VDERS anahtarı, sabit: elle seçilmiş listelerin kapsadığı sınavlar */
export const ALT_SINIF = /\b[5-8] ?(?:\.|inci|nci)? ?sinif|lgs|ortaokul/;
export function listeSec(L, ders, sabit = [], filtre = "") {
  const re = VDERS[ders].re, f = sade(filtre), secim = {};
  for (const p of L) {
    const n = sade(p.ad);
    if (!re.test(n) || (DISLA.test(n) && !/konu anlatim/.test(n)) || (f && !n.includes(f)) || (p.sayi != null && p.sayi < 3)) continue;
    const yp = yilPuan(p.ad, p.tarih); if (!yp) continue;
    const SL = sinavlar(p.ad); for (const s of (SL.length ? SL : VARSAYILAN[ders] || [])) {
      if (sabit.includes(s)) continue;
      if (s.startsWith("M") ? !VDERS[ders].M.length : (VDERS[ders].yok || []).includes(s)) continue;
      if (!s.startsWith("M") && /20(2[89]|3\d)/.test(p.ad)) continue;   /* 2028 ve sonrası YKS listeleri bugünkü TYT/AYT değil (Maarif öğrencileri için) */
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
export const kelime = x => sade(x).split(" ").filter(w => w && !BOS.has(w) && !/^\d+$/.test(w));
const kok = w => w.slice(0, Math.min(w.length, 5));
/* İki söz aynı kökten mi: kısa olan uzunun başı (en az 3 harf) ya da ilk 5 harf aynı */
/* Konudaki söz (a) ile başlıktaki söz (b) aynı kökten mi: b, a'nın ek almış hali; ya da b a'nın kısa hali (en çok 3 harflik ek farkı); ya da ortak başlangıç uzun */
const ayniKok = (a, b) => { if (a.length < 3 || b.length < 3) return a === b; if (b.startsWith(a)) return true; if (a.startsWith(b)) return a.length - b.length <= 3;
  const k = Math.min(a.length, b.length); let o = 0; while (o < k && a[o] === b[o]) o++; return o >= 5 && o >= 0.75 * k; };
/* Hocaların aynı konuya verdiği başka adlar (TYT) */
export const DIGER_AD = {
  "Denklem Çözme": ["Birinci Dereceden Denklemler", "Bilinmeyenli Denklemler", "Denklemler", "Denklem Kurma"],
  "Bölme ve Bölünebilme": ["Bölünebilme Kuralları", "Bölme Bölünebilme"],
  "Kümeler-Kartezyen Çarpım": ["Kümeler", "Kartezyen Çarpım"],
  "Permütasyon ve Kombinasyon": ["Permütasyon", "Kombinasyon"],
  "Veri – İstatistik": ["Veri Analizi", "Veri ve Grafik", "İstatistik"],
  "Hareket Hız Problemleri": ["Hareket Problemleri", "Hız Problemleri"],
  "İşçi Emek Problemleri": ["İşçi Problemleri", "Havuz Problemleri"],
  "Rutin Olmayan Problemleri": ["Rutin Olmayan"],
  "2.Dereceden Denklemler": ["İkinci Dereceden Denklemler", "2. Dereceden Denklem"],
  "Eşlik ve Benzerlik": ["Benzerlik"],
  "Özel Dörtgenler": ["Paralelkenar", "Eşkenar Dörtgen", "Yamuk", "Deltoid", "Dikdörtgen"],
  "Çemberde Uzun": ["Çemberde Uzunluk", "Çemberde Teğet"],
  "Dairede Çevre ve Alan": ["Dairenin Alanı", "Dairede Alan", "Dairede Çevre"],
  "Dönüşüm Geometrisi": ["Dönüşümler", "Öteleme", "Yansıma"],
  "Çemberin Analitiği": ["Çemberin Analitik", "Çemberin Denklemi"],
  "Noktanın Analitiği": ["Noktanın Analitik"], "Doğrunun Analitiği": ["Doğrunun Analitik", "Doğrunun Denklemi"],
  "Katı Cisimler": ["Katı Cisim"], "Özel Üçgenler": ["Özel Açılı Üçgen", "Dik Üçgen", "Pisagor", "Eşkenar Üçgen", "İkizkenar Üçgen"],
  "Üçgende Alan": ["Üçgenin Alanı"], "Açı Kenar Bağıntıları": ["Açı Kenar"], "Doğruda Açılar": ["Doğruda Açı", "Açı Çeşitleri"],
  "Sıvıların Kaldırma Kuvveti": ["Kaldırma Kuvveti"], "Isı, Sıcaklık ve Genleşme": ["Isı ve Sıcaklık", "Genleşme"],
  "Dinamik": ["Newton'un Hareket Yasaları", "Hareket Yasaları"], "İş, Güç ve Enerji": ["İş Güç Enerji", "İş ve Enerji", "Enerji Dönüşümleri"],
  "Hareket ve Kuvvet": ["Doğrusal Hareket", "Hareket"], "Madde ve Özellikleri": ["Özkütle", "Dayanıklılık", "Madde ve Özellik"],
  "Optik": ["Aydınlanma", "Gölge", "Düzlem Ayna", "Küresel Ayna", "Işığın Kırılması", "Mercekler"],
  "Atom ve Yapısı": ["Atom Modelleri", "Atom Altı Parçacıklar", "Atomun Yapısı"], "Periyodik Sistem": ["Periyodik Cetvel", "Periyodik Tablo", "Periyodik Özellikler"],
  "Kimyasal Türler Arası Etkileşimler": ["İyonik Bağ", "Kovalent Bağ", "Metalik Bağ", "Zayıf Etkileşimler", "Güçlü Etkileşimler"],
  "Kimyanın Temel Kanunları": ["Temel Kanunlar", "Kütlenin Korunumu", "Sabit Oranlar"], "Asitler, Bazlar ve Tuzlar": ["Asitler ve Bazlar", "Asit Baz"],
  "Endüstride ve Canlılarda Enerji": ["Canlılarda Enerji", "Endüstride Enerji"], "Kimya Her Yerde": ["Hayatımızda Kimya", "Yaygın Günlük Hayat Kimyasalları"],
  "Canlıların Ortak Özellikleri": ["Karakteristik Özellikleri", "Canlıların Ortak"], "Canlıların Temel Bileşenleri": ["İnorganik Bileşikler", "Organik Bileşikler", "Karbohidratlar", "Proteinler", "Lipitler", "Nükleik Asitler"],
  "Hücre ve Organeller – Madde Geçişleri": ["Hücre Organelleri", "Organeller", "Madde Geçişleri", "Madde Alışverişi", "Hücre Zarı"],
  "Hücrede Bölünme – Üreme": ["Mitoz", "Mayoz", "Hücre Bölünmesi", "Eşeyli Üreme", "Eşeysiz Üreme"], "Canlıların Sınıflandırılması": ["Sınıflandırma"],
  "Söz Yorumu": ["Söz Yorum"], "Sözcükte Yapı/Ekler": ["Yapı Bilgisi", "Sözcüğün Yapısı", "Kök ve Ek", "Yapım Ekleri"],
  "Sözcük Türleri": ["Sıfatlar", "Zamirler", "Zarflar", "Edat Bağlaç Ünlem"], "Fiiller-Fiilimsiler-Ek Fiiller-Çatı": ["Fiiller", "Fiilimsiler", "Ek Fiil", "Fiilde Çatı"],
  "Sözcük Grupları": ["Söz Öbekleri", "Söz Grupları", "İsim Tamlaması", "Sıfat Tamlaması", "Tamlamalar"],
  "Atmosfer ve Sıcaklık": ["Atmosfer", "İklim Elemanları Sıcaklık"], "Basınç ve Rüzgarlar": ["Basınç", "Rüzgarlar"], "Nem, Yağış ve Buharlaşma": ["Nem ve Yağış", "Yağış"],
  "Su – Toprak ve Bitkiler": ["Su Kaynakları", "Toprak", "Bitki Örtüsü"], "Türkiye’nin Yer Şekilleri": ["Yer Şekilleri"],
  "İlk Türk İslam Devletleri": ["Türklerin İslamiyeti Kabulü", "Devletleşme Sürecinde Selçuklu"],
  "Osmanlı Devletinde Arayış Yılları": ["Arayış Yılları", "Değişen Dünya Dengeleri Karşısında Osmanlı"],
  "18. Yüzyılda Değişim ve Diplomasi": ["Uluslararası İlişkilerde Denge Stratejisi", "Değişim ve Diplomasi"],
  "En Uzun Yüzyıl": ["Devrimler Çağında Değişen Devlet", "Değişen Sosyoekonomik Hayat"],
  "Osmanlı Kültür ve Medeniyeti": ["Klasik Çağda Osmanlı Toplum Düzeni", "Osmanlı Medeniyeti"],
  "20. Yüzyılda Osmanlı Devleti": ["20. Yüzyıl Başlarında Osmanlı"],
  "Mondros Ateşkesi, İşgaller ve Cemiyetler": ["Milli Mücadele", "Mondros"], "Kurtuluş Savaşına Hazırlık Dönemi": ["Milli Mücadele", "Hazırlık Dönemi"],
  "I. TBMM Dönemi": ["Milli Mücadele", "Birinci TBMM"], "Kurtuluş Savaşı ve Antlaşmalar": ["Milli Mücadele", "Kurtuluş Savaşı"],
  "II. TBMM Dönemi ve Çok Partili Hayata Geçiş": ["Atatürkçülük ve Türk İnkılabı", "Çok Partili Hayat"], "Atatürk İlkeleri": ["Atatürkçülük"],
  "Atatürk Dönemi Türk Dış Politikası": ["İki Savaş Arasındaki Dönemde Türkiye", "İki Küresel Savaş Arasında Türkiye", "Dış Politika"],
  "Kimya Bilimi": ["Simyadan Kimyaya", "Kimyanın Alt Disiplinleri"], "Maddenin Halleri": ["Hal Değişimi", "Katılar", "Sıvılar", "Gazlar"],
  "Ekosistem": ["Ekoloji", "Madde Döngüleri", "Besin Zinciri"], "Deyimler ve Atasözleri": ["Deyimler", "Atasözleri", "Söz Öbeklerinde Anlam"],
  "geo|Temel Kavramlar": ["Temel Kavramlar", "Doğruda Açılar"],
  "Sayı Problemleri": ["Sayı Problemi"], "İş, Güç ve Enerji": ["İş Güç", "Enerji"],
};
export function benzerlik(konu, baslik) {
  const K = kelime(konu), B = kelime(baslik);
  if (!K.length || !B.length) return 0;
  const bit = sade(baslik).replace(/ /g, ""), kb = K.join("");
  if (kb.length >= 6 && bit.includes(kb)) return 1 - (B.length > K.length + 6 ? 0.03 : 0);
  const tut = K.filter(w => B.some(b => ayniKok(w, b))).length;
  return tut / K.length - (B.length > K.length + 4 ? 0.05 : 0);
}
const SORU_RE = /soru coz|sorular|test|deneme|checkpoint|yaklasim|tekrar|bitirme|efisinado|kitap tanitim/;
const adlar = (ad, k) => [ad, ...(DIGER_AD[k] || DIGER_AD[ad] || [])];
const puan = (ad, baslik, k) => Math.max(...adlar(ad, k).map((a, i) => benzerlik(a, baslik) - (i ? 0.02 : 0)));

/* Konuları videolara eşle. konular: [{k, ad}], videolar: [[id, başlık, süre, bölümler]] → {k: [[id, sn], ...]}
   Konunun bütün konu anlatımı videoları sırayla alınır (soru çözümü videoları ancak konu anlatımı yoksa); hiçbiri yoksa uzun videonun bölümü. */
export function eslestir(konular, videolar, esik = 0.75) {
  const out = {};
  for (const { k, ad } of konular) {
    const tut = videolar.map((v, i) => ({ v, i, p: puan(ad, v[1], k) })).filter(x => x.p >= esik);
    const konu = tut.filter(x => !SORU_RE.test(sade(x.v[1])));
    const L = (konu.length ? konu : tut);
    if (L.length) { const en = Math.max(...L.map(x => x.p)); out[k] = L.filter(x => x.p >= en - 0.26).slice(0, 12).map(x => [x.v[0], 0]); continue; }
    let en = null;
    for (const v of videolar) for (const [sn, bad] of v[3] || []) { const q = puan(ad, bad, k) - 0.01 - (kelime(bad).length > kelime(ad).length + 2 ? 0.15 : 0); if (q >= 0.85 && (!en || q > en.p)) en = { p: q, v: [v[0], sn] }; }
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

/* Aramayla bulunan kanal hocanın kanalı mı: adındaki özel bir söz kanal adında geçmeli (ör. "Kolay Fizik" ≠ "Altuğ Güneş FİZİK") */
const GENEL = new Set("hoca hocam hocasi fizik matematik kimya biyoloji tarih cografya felsefe edebiyat turkce akademi ders dersleri yks tyt ayt ile".split(" "));
export function kanalUygun(hoca, kanalAdi) {
  const H = sade(hoca).split(" ").filter(w => w.length > 2 && !GENEL.has(w)), K = sade(kanalAdi).split(" ").map(kok);
  return !H.length || H.some(w => K.includes(kok(w)));
}
