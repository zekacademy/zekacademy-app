/* Soru Çözüm Merkezi: saf mantık (model seçimi, hak, bütçe, bonus). Testleri: tests/soru.test.js */
import { addDays, dayTasks } from "./logic.js";

export const AI_VARSAYILAN = {
  acik: "kapali",            // "kapali" | "pilot" | "herkes"
  pilot: [],                 // pilot modunda açık öğrenci id'leri
  aylikHak: 120,             // öğrenci başı aylık soru hakkı
  tavan: 50,                 // ayda en fazla harcanacak dolar
  yedek: 5,                  // bonus dağıtırken dokunulmayan pay ($)
  uyari: 40,                 // bu tutara gelince koça bildirim ($)
  takipGunluk: 15,           // günlük "anlamadım / benzer soru" sınırı
  bonusAcik: true,
  bonusUyum: 70,             // bonus için en az haftalık program uyumu (%)
  bonusDakika: 180,          // ya da günlük ortalama çalışma (dk)
  bonusKullanim: 0.7,        // hakkının en az bu oranını kullanmış olmalı
  bonusTavan: 30,            // bir öğrenciye haftalık en fazla bonus
  modelKolay: "claude-haiku-5-5",
  modelZor: "claude-sonnet-5-5",
  fiyat: { kolay: { in: 0.10, out: 0.50 }, zor: { in: 2.00, out: 10.00 } }, // $ / 1M token
  hakKolay: 1, hakZor: 3, hakTekrar: 2,
};
export function aiCfg(settings = {}){ const x = settings.ai || {}; return { ...AI_VARSAYILAN, ...x, fiyat: { ...AI_VARSAYILAN.fiyat, ...(x.fiyat || {}) } }; }

/* Öğrenci için açık mı? */
export function aiAcikMi(c, sid){ return c.acik === "herkes" || (c.acik === "pilot" && (c.pilot || []).includes(sid)); }

/* Ay anahtarı (İstanbul tarihi YYYY-MM-DD'den) */
export const ayOf = date => String(date).slice(0, 7);
export const kullanimId = (ay, sid) => `${ay}_${sid}`;

/* Bir isteğin dolar maliyeti */
export function maliyet(c, tur, usage){ const f = c.fiyat[tur] || c.fiyat.kolay; const u = usage || {};
  return ((u.input_tokens || 0) * f.in + (u.output_tokens || 0) * f.out + (u.cache_creation_input_tokens || 0) * f.in * 1.25 + (u.cache_read_input_tokens || 0) * f.in * 0.1) / 1e6; }

/* Kalan hak */
export function kalanHak(c, k = {}){ return Math.max(0, (c.aylikHak + (k.bonus || 0) + (k.ekHak || 0)) - (k.kullanilan || 0)); }
export function toplamHak(c, k = {}){ return c.aylikHak + (k.bonus || 0) + (k.ekHak || 0); }

/* Haiku'nun çözümünden sonra Sonnet'e geçilmeli mi? */
export function zoraGec(r, anahtar){
  if (!r || typeof r !== "object") return "okunamadı-json";
  if (r.okunabildi === false) return null;                       // fotoğraf okunmadı: büyük model de okuyamaz, öğrenciye net fotoğraf iste
  if (r.emin === false) return "emin-degil";
  if (String(r.zorluk || "").toLowerCase() === "zor") return "zor";
  const k = String(anahtar || "").trim().toUpperCase();
  const s = String((r.cevap && r.cevap.sik) || "").trim().toUpperCase();
  if (k && s && k !== s) return "anahtar-uyusmuyor";
  if (!Array.isArray(r.adimlar) || !r.adimlar.length) return "adim-yok";
  return null;
}

/* Model yanıtından JSON çıkar (tolerant) */
export function jsonCikar(text){
  const t = String(text || "").trim();
  try { return JSON.parse(t); } catch (e) {}
  const f = t.match(/```(?:json)?\s*([\s\S]*?)```/); if (f) { try { return JSON.parse(f[1]); } catch (e) {} }
  const a = t.indexOf("{"), b = t.lastIndexOf("}");
  if (a >= 0 && b > a) { try { return JSON.parse(t.slice(a, b + 1)); } catch (e) {} }
  return null;
}

/* Cevap anahtarı son kontrol: modelin söylediğine değil gerçek karşılaştırmaya güven */
export function anahtarDurumu(r, anahtar){
  const k = String(anahtar || "").trim().toUpperCase(); if (!k) return "yok";
  const s = String((r && r.cevap && r.cevap.sik) || "").trim().toUpperCase();
  return s && s === k ? "uyumlu" : "uyumsuz";
}

/* Ay sonu tahmini: şu ana kadarki günlük ortalama ile */
export function aySonuTahmini(harcanan, date){
  const [y, m, d] = date.split("-").map(Number); const gunSayisi = new Date(Date.UTC(y, m, 0)).getUTCDate();
  const gecen = Math.max(1, d); return { tahmin: harcanan / gecen * gunSayisi, gunSayisi, gecen };
}

/* Son 7 günün program uyumu (%) ve günlük ortalama çalışma (dk) */
export function haftalikPerformans(s, date){
  let all = 0, done = 0, dk = 0;
  for (let i = 1; i <= 7; i++) { const d = addDays(date, -i); const l = dayTasks(s, d); all += l.length; done += l.filter(t => t && t.done).length; dk += (s.gunluk || {})[d] || 0; }
  return { uyum: all ? Math.round(done / all * 100) : null, gunlukDk: Math.round(dk / 7), gorev: all };
}

/* Haftalık bonus: tavanın altında kalan payın yarısını hak eden öğrencilere böl */
export function bonusDagit(c, { harcanan, date, ogrenciler }){
  const { tahmin } = aySonuTahmini(harcanan, date);
  const pay = (c.tavan - c.yedek) - tahmin;
  if (!c.bonusAcik || pay <= 0.5) return { pay, tahmin, dagitim: [] };
  const hakDolar = Math.max(0.005, (c.tavan - c.yedek) / Math.max(1, ogrenciler.length) / Math.max(1, c.aylikHak));
  const hakEden = ogrenciler.filter(o => {
    const top = toplamHak(c, o.k), kul = (o.k && o.k.kullanilan) || 0;
    const caliskan = (o.perf.uyum != null && o.perf.uyum >= c.bonusUyum) || o.perf.gunlukDk >= c.bonusDakika;
    return top > 0 && kul / top >= c.bonusKullanim && caliskan;
  });
  if (!hakEden.length) return { pay, tahmin, dagitim: [] };
  const kisiBasi = Math.min(c.bonusTavan, Math.floor(pay * 0.5 / hakDolar / hakEden.length));
  if (kisiBasi < 3) return { pay, tahmin, dagitim: [] };
  return { pay, tahmin, dagitim: hakEden.map(o => ({ sid: o.sid, hak: kisiBasi, uyum: o.perf.uyum, gunlukDk: o.perf.gunlukDk })) };
}

/* Bonus mesajı */
export function bonusMesaj(b){
  const neden = b.uyum != null && b.uyum >= 0 ? `Bu hafta programına %${b.uyum} uydun` : `Bu hafta günde ortalama ${b.gunlukDk} dk çalıştın`;
  return `🎉 ${neden}, +${b.hak} bonus soru hakkı kazandın!`;
}

/* Model talimatları */
export const SISTEM = [
  "Sen Zekacademy koçluk uygulamasının YKS Soru Çözüm Koçusun. Kullanıcıların çoğu 16-19 yaşında, YKS'ye (TYT/AYT) hazırlanan lise öğrencisi ya da mezun.",
  "Sadece ders, soru çözümü, konu anlatımı ve sınav stratejisi konularında yardım et. Ders dışı istekleri kibarca derse geri yönlendir. Romantik, cinsel, şiddet içeren ya da yaşa uygun olmayan içeriğe hiçbir durumda girme.",
  "Öğrenci üzgün, çaresiz ya da kendine zarar verme düşüncesi içinde görünürse kısa ve şefkatli bir cümleyle güvendiği bir yetişkinle ve koçuyla konuşmasını öner; ciddi bir risk sezersen 112'yi aramasını söyle.",
  "Kişisel bilgi (TC, adres, telefon) isteme. Deneme sınavı sırasında kopya amaçlı kullanıma yardım etme.",
  "Türkçe, sıcak, sade ve cesaret verici yaz; küçümseme. Cümlelerin kısa olsun. Uzun LaTeX kullanma; x², √2, π, ≤, × gibi okunur yaz.",
].join("\n");

export const SEMA = [
  "Soruyu çöz ve YALNIZCA şu biçimde bir JSON nesnesi döndür (başka metin yok). İlk alan 'kontrol': çözümü orada kısaca kontrol et, öğrenci bunu görmez.",
  "{",
  ' "kontrol": "kısa hesap kontrolü",',
  ' "okunabildi": true,',
  ' "sorun": "",',
  ' "soru": "Sorunun kısa özeti, en fazla 2 cümle",',
  ' "siklar": {"A":"...","B":"...","C":"...","D":"...","E":"..."},',
  ' "ders": "TYT Matematik",',
  ' "konu": "Sayılar · Tek-Çift",',
  ' "zorluk": "kolay | orta | zor",',
  ' "istenen": "Ne istendiğini anlatan tek, sade cümle",',
  ' "bilgi": [{"ad":"Kısa ad","ifade":"tek × tek = tek"}],',
  ' "ipuclari": ["ilk küçük ipucu","biraz daha açık ipucu","neredeyse çözüm ipucu"],',
  ' "adimlar": [{"baslik":"3-6 kelimelik başlık","aciklama":"En fazla 2 kısa cümle; önemli sayıları **kalın** yaz","islem":"13 × 13 = 169"}],',
  ' "cevap": {"sik":"C","deger":"120"},',
  ' "emin": true,',
  ' "puf": "Sınavda zaman kazandıran yol ya da sık yapılan hata, 1-2 cümle"',
  "}",
  "Kurallar: siklar yoksa null; bilgi 0-2 tane; ipuclari cevabı söylemeden 3 tane; adimlar 3-6 tane, her adımda tek iş, islem yoksa \"\".",
  "Fotoğraf bulanık, soru kesik ya da şıklar okunmuyorsa tahmin yürütme: okunabildi=false yap ve sorun alanına neyin okunmadığını yaz.",
  "Zorluk: AYT matematik/fizik/kimya ya da çok adımlı akıl yürütme gerektiren sorular için \"zor\". Çözümünden tam emin değilsen emin=false yap; yanlış bir çözümü asla emin gibi sunma.",
].join("\n");

export function cozIstegi({ metin, anahtar, tekrar }){
  return SEMA
    + (metin ? `\n\nÖğrencinin notu / soru metni: ${String(metin).slice(0, 1500)}` : "")
    + (anahtar ? `\n\nCevap anahtarına göre doğru cevap: ${anahtar} şıkkı. Çözümünü buna göre kontrol et; uyuşmuyorsa soruyu baştan farklı bir yoldan tekrar çöz, yine uyuşmuyorsa emin=false yap ve kendi bulduğun en doğru çözümü göster.` : "\n\nCevap anahtarı verilmedi.")
    + (tekrar ? `\n\nÖğrenci önceki çözümün yanlış olabileceğini söyledi. Önceki çözüm özeti: ${String(tekrar).slice(0, 2000)}\nSoruyu baştan, çok dikkatli çöz.` : "");
}

export function takipIstegi(tur, baglam, metin, adim){
  const b = `Üzerinde çalıştığımız soru: ${String(baglam || "").slice(0, 6000)}`;
  if (tur === "adim") return `${b}\n\nÖğrenci ${adim}. adımı anlamadı. Sadece bu adımı daha basit ve somut anlat: en fazla 4 kısa cümle, gerekiyorsa küçük sayılarla bir örnek ver. Başlık kullanma, paragraf yazma.`;
  if (tur === "benzer") return `${b}\n\nAynı mantıkta, YKS tarzında YENİ bir soru yaz (sayıları ve durumu değiştir, zorluk aynı kalsın). Cevabı mutlaka kendin kontrol et. YALNIZCA şu JSON: {"soru":"...","siklar":{"A":"..","B":"..","C":"..","D":"..","E":".."},"dogru":"B","cozum":["kısa adım 1","kısa adım 2","kısa adım 3"]}`;
  return `${b}\n\nÖğrencinin sorusu: ${String(metin || "").slice(0, 1500)}\n\nKısa ve ferah yaz: en fazla 6 kısa cümle ya da 5 maddelik liste, paragraf yığını yok, önemli sayıları **kalın** yaz.`;
}
