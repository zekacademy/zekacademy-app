/* Deneme karnesi okuma (fotoğraf / PDF → deneme kayıtları). Saf mantık; testleri: tests/karne.test.js
   Senaryolar: kurum karnesi (ders analizi D/Y/B/Net + alt dersler), konu analizi sayfası (soru soru DC/ÖC/SO),
   kırpılmış karne (sınav adı yok → "son N sınav" tablosundan), el yazısı netler, birden çok denemeli tablo (yalnız net). */

export const BOLUM = {
  TYT: [["turkce", "Türkçe", 40], ["sosyal", "Sosyal Bilimler", 20], ["mat", "Temel Matematik", 40], ["fen", "Fen Bilimleri", 20]],
  AYT: [["mat", "Matematik", 40], ["fen", "Fen Bilimleri", 40], ["sos1", "Edebiyat-Sosyal 1", 40], ["sos2", "Sosyal Bilimler 2", 40]],
};

export const KARNE_SISTEM = [
  "Sen bir YKS deneme sınavı sonuç belgesi okuyucususun. Görevin, öğrencinin yüklediği fotoğraf ya da PDF'teki deneme sonuçlarını hatasız ve uydurmadan yapılandırılmış JSON'a çevirmek.",
  "Sadece belgede gerçekten yazanı aktar. Okuyamadığın ya da belgede olmayan değer için null yaz; asla tahmin edip sayı uydurma.",
  "Yanıtın yalnızca tek bir JSON nesnesi olsun; açıklama, markdown ya da kod bloğu ekleme.",
].join("\n");

const ISTEK = `Belgeyi oku ve aşağıdaki JSON biçiminde yanıt ver.

{
  "okunabildi": true,
  "belgeTuru": "karne" | "konu-analizi" | "el-yazisi" | "tablo" | "diger",
  "denemeler": [
    {
      "tur": "TYT" | "AYT",
      "yayin": "yayınevi adı (kısa)",
      "sinavAdi": "belgede yazan sınav adı ya da null",
      "tarih": "YYYY-MM-DD ya da null",
      "kaynak": "ana" | "gecmis",
      "bolumler": { "<bolum>": { "d": sayı|null, "y": sayı|null, "b": sayı|null, "net": sayı|null } },
      "altDersler": { "<ders>": { "d": sayı|null, "y": sayı|null, "net": sayı|null } },
      "toplamNet": sayı|null,
      "puan": sayı|null,
      "siralama": "metin ya da null",
      "yanlislar": [ { "ders": "Matematik", "no": 3, "konu": "belgedeki konu adı", "eslesen": "listeden tam konu adı ya da null", "durum": "yanlis" | "bos" } ],
      "emin": true | false,
      "notlar": ["kısa Türkçe not"]
    }
  ],
  "uyarilar": ["öğrenciye gösterilecek kısa Türkçe uyarı"]
}

BÖLÜMLER (bolumler anahtarları):
- TYT: "turkce" (40 soru), "sosyal" (20 soru: tarih 5 + coğrafya 5 + felsefe 5 + din 5), "mat" (40 soru: matematik 30 + geometri 10), "fen" (20 soru: fizik 7 + kimya 7 + biyoloji 6).
- AYT: "mat" (40 soru: matematik + geometri), "fen" (40 soru: fizik 14 + kimya 13 + biyoloji 13), "sos1" (Türk Dili ve Edebiyatı-Sosyal Bilimler 1: edebiyat 24 + tarih-1 10 + coğrafya-1 6), "sos2" (Sosyal Bilimler 2: tarih-2 11 + coğrafya-2 11 + felsefe grubu 12 + din 6).
- altDersler anahtarları: "tarih","cografya","felsefe","din","matematik","geometri","fizik","kimya","biyoloji","edebiyat","tarih1","cografya1","tarih2","cografya2","felsefeGrubu". Belgede yoksa altDersler'i boş bırak.

KURALLAR:
1. Kurum karnelerinde (ör. "DERS ANALİZİ" tablosu) ana satırlar "TYT-TÜRKÇE", "TYT-SOSYAL BİLİMLER", "TYT-MATEMATİK", "TYT-FEN BİLİMLERİ" gibi kalın satırlardır. DİKKAT: alt ders satırları (TARİH, COĞRAFYA, FELSEFE, DİN; MATEMATİK, GEOMETRİ; FİZİK, KİMYA, BİYOLOJİ) kendi ana satırlarının ÜSTÜNDE yer alabilir. Ör. TARİH/COĞRAFYA/FELSEFE/DİN satırları "TYT-TÜRKÇE" ile "TYT-SOSYAL BİLİMLER" arasındaysa SOSYAL'e aittir; MATEMATİK/GEOMETRİ satırları "TYT-MATEMATİK"in, FİZİK/KİMYA/BİYOLOJİ satırları "TYT-FEN BİLİMLERİ"nin üstündedir. Soru sayıları (5+5+5+5=20 gibi) ile doğrula.
2. Bölüm değerlerini ana satırlardan al (d, y, b, net). Boş hücre 0 demektir ancak satırın tamamı yoksa null yaz. "ORT" (ortalama) sütununu ASLA kullanma; o kurum ortalamasıdır, öğrencinin değil.
3. Öğrencinin netini kontrol et: net = doğru − yanlış/4. Belgedeki net bu formüle uymuyorsa belgedekini yaz ve notlar'a ekle.
4. "Sınav Adı" içinde yayın geçer: "3D TG TYT 1 2027" → yayin "3D"; "PARAF TG TYT-1" → "Paraf"; "ÖZDEBİR TYT-1" → "Özdebir"; "BİLGİ SARMAL TG TYT 2" → "Bilgi Sarmal"; "SIFIR POZİTİF" → "Sıfır Pozitif"; "345 son prova" → "345". Belgenin başlığındaki kurum adı (ör. "Model VİP Özel Öğretim Kurumu", "Hangi Kaynak") yayın DEĞİLDİR. Kitapçık kapağındaki yayın logosu/adı (ör. "ICEBERG") yayındır.
5. Sınav adı kırpılmış ya da görünmüyorsa, belgedeki "SON N SINAVIN SONUÇLARI" tablosunda aynı tarihli satırdan sınav adını ve yayını al; tarih de yoksa toplam net eşleşen satırı kullan. Bulamazsan yayin null.
6. "SON N SINAVIN SONUÇLARI" gibi geçmiş tablosundaki DİĞER satırları da ayrı denemeler olarak ekle, kaynak "gecmis" olsun. Bu satırlarda yalnız netler vardır: bolumler'de d ve y null, net dolu olsun (TYT-TRK → turkce, TYT-SOS "T" sütunu → sosyal, TYT-MAT "T" → mat, TYT-FEN "T" → fen). Alt ders netlerini (TRH, COG, FLS, DIN, MAT, GEO, FZK, KMY, BIO) altDersler'e yaz. Asıl belgedeki deneme (karnenin konusu olan) kaynak "ana"dır ve geçmiş tablosunda tekrar ediyorsa bir kez yaz.
7. Konu analizi sayfasında her soru için "DC" doğru cevap, "ÖC" öğrencinin cevabı, "SO" sonuçtur: "+" doğru, "-" yanlış, boş hücre boş bırakılmış demektir. "İPTAL" sorular hesaba girmez. yanlislar listesine "-" olan soruları durum "yanlis", ÖC boş olanları durum "bos" olarak ekle. Ders adı tablodaki başlıktır (Türkçe, Matematik, Geometri, Tarih, Coğrafya, Felsefe, Din Kültürü, Fizik, Kimya, Biyoloji, Edebiyat...).
8. Her yanlış/boş sorunun konusunu, aşağıda verilen UYGULAMA KONU LİSTESİ'nden en uygun konuyla eşle ve listedeki adı AYNEN "eslesen"e yaz (ör. "Atomun Yapısı" → "Atom ve Yapısı", "Asitlerin ve Bazların Tepkimeleri" → "Asitler, Bazlar ve Tuzlar", "Üçgende Açı-Kenar Bağıntıları" → "Açı Kenar Bağıntıları", "Paragrafın Ana Düşüncesi" gibi paragraf soruları için listede paragraf yoksa null). Emin değilsen null yaz; zorla eşleme.
9. Konu analizi sayfası ile karne sayfası aynı denemeye aitse (aynı belge grubunda) tek deneme olarak birleştir: netler karneden, yanlislar konu analizinden.
10. Elle yazılmış netler (ör. "Türkçe = 35,25  Sos = 11,75  Mat = 30  Fen = 17,75") için yalnız net doldur, d/y null. Toplamı kontrol et; tutmuyorsa notlar'a yaz. Basılı ve el yazısı rakamları karıştırma; el yazısında 1/7, 3/8, 5/6 karışabilir, toplamla doğrula, emin değilsen emin:false.
11. Bir tabloda (ör. "YAYIN/TARİH | TOPLAM | TÜRKÇE | SOSYAL | MATEMATİK | FEN") birden çok deneme varsa her satırı ayrı deneme yaz (kaynak "ana"). "345 son prova/ 20 ağustos" gibi hücrelerde yayın ve tarihi ayır. Boş satırları atla.
12. Tarihleri YYYY-MM-DD yaz. Yıl yazmıyorsa BUGÜN'den önceki en yakın tarihi seç (gelecekte bir deneme tarihi olamaz). Tarih hiç yoksa null.
13. Ondalık ayırıcı virgül ya da nokta olabilir; sayıları JSON sayısı olarak yaz (32,50 → 32.5).
14. TYT mi AYT mi: başlık, sınav adı ve bölüm adlarından anla ("TYT-TÜRKÇE" → TYT; "TDE-SB1", "AYT MATEMATİK" → AYT).
15. Belge bir deneme sonucu değilse ya da okunamıyorsa okunabildi:false ve uyarilar'a nedenini yaz.
16. Eğik, gölgeli, bulanık fotoğraflarda okuduğun her sayıyı soru sayısı ve toplamlarla çapraz kontrol et; tutarsızlık varsa emin:false ve notlar'a ne olduğunu yaz.`;

/* İstek metni: öğrenci bağlamı + konu listesi */
export function karneIstegi({ bugun, alan, sinif, konular }){
  const liste = Object.entries(konular || {}).map(([ex, dersler]) =>
    `${ex}:\n` + Object.entries(dersler || {}).map(([d, ts]) => `- ${d}: ${(ts || []).slice(0, 80).join(" | ")}`).join("\n")).join("\n\n");
  return `${ISTEK}\n\nBUGÜN: ${bugun}\nÖĞRENCİ: ${sinif || "?"} · alan ${alan || "?"}\n\nUYGULAMA KONU LİSTESİ (eslesen için yalnız bunlar):\n${liste || "(liste yok)"}`;
}

const sayi = v => { if (v == null || v === "") return null; const n = typeof v === "number" ? v : Number(String(v).replace(",", ".").replace(/[^\d.\-]/g, "")); return Number.isFinite(n) ? n : null; };
const yuvarla = n => Math.round(n * 100) / 100;

/* Modelin çıktısını doğrula ve uygulamanın deneme kaydına yakın biçime getir */
export function karneDuzelt(r, bugun){
  const out = { okunabildi: !!(r && r.okunabildi !== false), belgeTuru: (r && r.belgeTuru) || "diger", denemeler: [], uyarilar: [] };
  if (!r || !Array.isArray(r.denemeler)) { if (r && Array.isArray(r.uyarilar)) out.uyarilar = r.uyarilar.map(String).slice(0, 5); return out; }
  out.uyarilar = (Array.isArray(r.uyarilar) ? r.uyarilar : []).map(x => String(x).slice(0, 200)).slice(0, 5);
  for (const d0 of r.denemeler.slice(0, 20)) {
    const tur = d0 && String(d0.tur).toUpperCase() === "AYT" ? "AYT" : "TYT", B = BOLUM[tur];
    const notlar = (Array.isArray(d0.notlar) ? d0.notlar : []).map(x => String(x).slice(0, 200)).slice(0, 5);
    let emin = d0.emin !== false;
    const bolumler = {};
    for (const [k, ad, mx] of B) {
      const v = (d0.bolumler || {})[k]; if (!v) continue;
      let d = sayi(v.d), y = sayi(v.y), net = sayi(v.net);
      if (d != null && (d < 0 || d > mx)) { notlar.push(`${ad}: doğru sayısı (${d}) geçersiz`); d = null; emin = false; }
      if (y != null && (y < 0 || y > mx)) { notlar.push(`${ad}: yanlış sayısı (${y}) geçersiz`); y = null; emin = false; }
      if (d != null && y != null && d + y > mx) { notlar.push(`${ad}: doğru + yanlış ${mx} soruyu aşıyor`); emin = false; }
      if (d != null && y == null) y = 0;
      if (d != null) { const h = yuvarla(d - y / 4); if (net != null && Math.abs(h - net) > 0.01) { notlar.push(`${ad}: belgedeki net ${net}, hesaplanan ${h}`); emin = false; } net = h; }
      if (net != null && (net < -mx / 4 || net > mx)) { notlar.push(`${ad}: net (${net}) geçersiz`); net = null; emin = false; }
      if (d == null && net == null) continue;
      bolumler[k] = d != null ? { d, y } : { net };
    }
    if (!Object.keys(bolumler).length) continue;
    const toplam = yuvarla(Object.values(bolumler).reduce((a, v) => a + (v.net != null ? v.net : v.d - v.y / 4), 0));
    const tn = sayi(d0.toplamNet);
    if (tn != null && Object.keys(bolumler).length === B.length && Math.abs(tn - toplam) > 0.01) { notlar.push(`Toplam net belgede ${tn}, derslerin toplamı ${toplam}`); emin = false; }
    let tarih = /^\d{4}-\d{2}-\d{2}$/.test(d0.tarih || "") ? d0.tarih : null;
    if (tarih && bugun && tarih > bugun) { const geri = tarih.replace(/^(\d{4})/, (m, yy) => String(+yy - 1)); tarih = geri <= bugun ? geri : null; notlar.push("Tarih gelecekte görünüyordu, düzeltildi"); }
    const yanlislar = (Array.isArray(d0.yanlislar) ? d0.yanlislar : []).slice(0, 160).map(x => ({
      ders: String(x.ders || "").slice(0, 40), no: sayi(x.no), konu: String(x.konu || "").slice(0, 120),
      eslesen: x.eslesen ? String(x.eslesen).slice(0, 120) : null, durum: x.durum === "bos" ? "bos" : "yanlis" }));
    out.denemeler.push({ tur, yayin: d0.yayin ? String(d0.yayin).slice(0, 60) : "", sinavAdi: d0.sinavAdi ? String(d0.sinavAdi).slice(0, 160) : "",
      tarih, kaynak: d0.kaynak === "gecmis" ? "gecmis" : "ana", bolumler, toplam,
      altDersler: d0.altDersler && typeof d0.altDersler === "object" ? Object.fromEntries(Object.entries(d0.altDersler).slice(0, 16).map(([k, v]) => [k, { d: sayi(v && v.d), y: sayi(v && v.y), net: sayi(v && v.net) }])) : {},
      puan: sayi(d0.puan), siralama: d0.siralama ? String(d0.siralama).slice(0, 40) : "", yanlislar, emin, notlar });
  }
  /* aynı deneme iki kez geldiyse (ana + geçmiş) tek tut */
  const seen = new Map();
  out.denemeler = out.denemeler.filter(x => { const k = `${x.tur}|${x.tarih || ""}|${x.toplam}`; if (seen.has(k)) { const o = seen.get(k); if (o.kaynak === "gecmis" && x.kaynak === "ana") Object.assign(o, x); return false; } seen.set(k, x); return true; });
  out.denemeler.sort((a, b) => (a.kaynak === "ana" ? 0 : 1) - (b.kaynak === "ana" ? 0 : 1) || String(b.tarih || "").localeCompare(String(a.tarih || "")));
  return out;
}
