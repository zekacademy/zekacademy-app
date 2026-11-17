/* Haftalık veli özeti: öğrencinin kendi isteğiyle velisine giden, ayrıntıya girmeyen e-posta (testleri: tests/veli.test.js) */
import { addDays, dayTasks, pStart } from "./logic.js";
const num = v => { if (v == null || v === "") return null; const n = typeof v === "number" ? v : parseFloat(String(v).replace(",", ".")); return Number.isFinite(n) ? n : null; };
const netOf = v => v == null ? null : typeof v === "number" ? v : typeof v === "object" ? ((num(v.d) || 0) - (num(v.y) || 0) / 4) : num(v);
const ALAN = { TYT: ["turkce", "sosyal", "mat", "fen"], AYT: ["mat", "fen", "sos1", "sos2"] };
export const denemeNet = d => Math.round((ALAN[d.tur] || []).reduce((a, k) => a + (netOf(d[k]) || 0), 0) * 100) / 100;
export const epostaGecerli = e => /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(String(e || "").trim());
export const sureYaz = dk => { dk = Math.round(dk); const h = Math.floor(dk / 60), m = dk % 60; return h ? `${h} saat${m ? ` ${m} dakika` : ""}` : `${m} dakika`; };
const AY = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"];
export const tarihYaz = d => { const [, m, g] = d.split("-").map(Number); return `${g} ${AY[m - 1]}`; };
export const ilkAd = n => String(n || "").trim().split(/\s+/)[0] || "Öğrenciniz";
const GUNK = ["Pzt", "Sal", "Çar", "Per", "Cum", "Cmt", "Paz"], GUNT = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"];
const gunlukDk = (s, d) => (s.gunluk || {})[d] || 0;
/* Bir haftanın (pazartesi başlangıçlı) özeti; gorusmeler: o haftaki görüşme kayıtları, sinav: YKS tarihi, bugun: rapor günü */
export function veliOzet(s, bas, { gorusmeler = [], sinav = "", bugun = "" } = {}){
  let dk = 0, gun = 0, hepsi = 0, biten = 0, onceDk = 0; const gunler = [];
  for (let i = 0; i < 7; i++){ const d = addDays(bas, i), m = gunlukDk(s, d); dk += m; if (m >= 30) gun++; gunler.push({ g: GUNK[i], tam: GUNT[i], tarih: d, dk: m });
    onceDk += gunlukDk(s, addDays(bas, i - 7));
    const l = dayTasks(s, d); hepsi += l.length; biten += l.filter(t => t && t.done).length; }
  const bit = addDays(bas, 6), D = (s.denemeler || []).filter(d => d && d.tur && d.tarih).sort((a, b) => a.tarih < b.tarih ? -1 : 1);
  const denemeler = D.filter(d => d.tarih >= bas && d.tarih <= bit).map(d => { const once = D.filter(x => x.tur === d.tur && x.tarih < d.tarih).pop();
    return { tur: d.tur, tarih: d.tarih, ad: d.ad || d.yayin || "", net: denemeNet(d), fark: once ? Math.round((denemeNet(d) - denemeNet(once)) * 100) / 100 : null }; });
  const son = denemeler[denemeler.length - 1], deneme = son ? { ...son, sayi: denemeler.length } : null;
  const enIyi = gunler.reduce((a, x) => x.dk > a.dk ? x : a, { dk: 0 });
  const hedefler = Object.entries(((s.plan || {})[pStart(s, addDays(bas, 3))] || {}).hedef || {}).filter(([, v]) => v && v.konu).map(([ders, v]) => ({ ders, konu: v.konu, done: !!v.done }));
  const gorusme = gorusmeler.some(g => g && g.durum === "yapildi" && g.tur !== "rapor") ? "yapildi" : null;
  const kalan = sinav && bugun ? Math.max(0, Math.round((Date.parse(sinav + "T12:00:00Z") - Date.parse(bugun + "T12:00:00Z")) / 864e5)) : null;
  const ort = dk / 7;
  const durum = dk === 0 ? "kayit-yok" : ort >= 240 && gun >= 6 ? "harika" : ort >= 150 && gun >= 4 ? "iyi" : "yavas";
  return { bas, bit, dk, onceDk, gun, gunler, enIyi: enIyi.dk ? enIyi : null, gorev: { hepsi, biten }, uyum: hepsi ? Math.round(biten / hepsi * 100) : null, deneme, denemeler, hedefler, gorusme, kalan, durum }; }
const DURUM = { harika: "Harika bir hafta geçirdi 🌟", iyi: "İyi gidiyor 👍", yavas: "Bu hafta biraz yavaşladı; desteğiniz iyi gelir 🤝", "kayit-yok": "Bu hafta uygulamaya çalışma kaydı girilmedi." };
/* Veliye küçük not: haftanın durumuna göre hazır notlardan biri otomatik seçilir (koç yazmaz); her hafta sırayla değişir, aynı not üst üste gelmez */
const ONERI = {
  harika: ["Emeğini fark ettiğinizi söylemeniz, bu tempoyu korumasına çok yardımcı olur.", "Bu hafta gösterdiği istikrar için küçük bir sürpriz ya da birlikte güzel bir akşam onu çok mutlu eder.", "Çok çalıştığı haftalarda iyi uyuması ve dinlenmesi de en az çalışmak kadar önemli; bunu hatırlatmanız yeterli."],
  iyi: ["Küçük bir tebrik ve güzel bir dinlenme molası motivasyonunu artırır.", "Doğru yolda; \"seninle gurur duyuyorum\" demeniz bu haftaki emeğini taçlandırır.", "Haftanın nasıl geçtiğini merakla sormanız, ona yalnız olmadığını hissettirir."],
  yavas: ["Baskı yerine nasıl hissettiğini sormanız ve birlikte küçük bir hedef koymanız iyi gelir.", "Yavaş haftalar herkeste olur; anlayışla yaklaşmanız ve küçük bir adımı bile takdir etmeniz çok değerli.", "Çalışma ortamının sessiz ve düzenli olmasına yardımcı olmanız, yeniden ritmini bulmasını kolaylaştırır."],
  "kayit-yok": ["Uygulamaya süresini girmesini hatırlatmanız yeterli olur.", "Çalıştığı süreleri uygulamaya girmesini nazikçe hatırlatırsanız gelişimini birlikte daha iyi görebiliriz.", "Bu hafta kayıt girilmemiş; nasıl olduğunu sormanız ve uygulamayı kullanmasını hatırlatmanız yeterli."] };
export const oneriSec = (durum, bas) => { const L = ONERI[durum] || ONERI.iyi, h = Math.floor(Date.parse(bas + "T12:00:00Z") / (7 * 864e5)); return L[((h % L.length) + L.length) % L.length]; };
const esc = x => String(x).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
const virgul = n => String(n).replace(".", ",");
const farkYaz = f => f == null ? "" : ` (${f >= 0 ? "+" : ""}${virgul(f)})`;
/* E-posta içeriği: konu, düz metin ve HTML */
export function veliEposta(s, o, { kocAd = "Zekeriya Hoca" } = {}){
  const ad = ilkAd(s.name), aralik = `${tarihYaz(o.bas)} – ${tarihYaz(o.bit)}`, hitap = "Merhaba değerli velim,";
  const degisim = o.onceDk ? Math.round(o.dk - o.onceDk) : null;
  const satir = [
    ["Toplam çalışma", o.dk ? sureYaz(o.dk) : "Kayıt yok"],
    ...(o.dk ? [["Günlük ortalama", sureYaz(o.dk / 7)]] : []),
    ...(degisim != null && Math.abs(degisim) >= 30 ? [["Geçen haftaya göre", `${degisim > 0 ? "+" : "−"}${sureYaz(Math.abs(degisim))}`]] : []),
    ["Çalıştığı gün", `${o.gun} / 7`],
    ...(o.enIyi ? [["En verimli günü", `${o.enIyi.tam} · ${sureYaz(o.enIyi.dk)}`]] : []),
    ...(o.gorev.hepsi ? [["Tamamlanan görev", `${o.gorev.biten} / ${o.gorev.hepsi} (%${o.uyum})`]] : []),
    ...(o.gorusme ? [["Koçuyla haftalık görüşme", "Yapıldı ✓"]] : []),
    ...(o.kalan != null ? [["YKS'ye kalan", `${o.kalan} gün`]] : [])];
  const den = o.denemeler.map(d => `${d.tur} denemesi${d.ad ? ` (${d.ad})` : ""}: ${virgul(d.net)} net${farkYaz(d.fark)}`);
  const hed = o.hedefler.map(h => `${h.ders}: ${h.konu}${h.done ? " ✓" : ""}`);
  const hedOzet = o.hedefler.length ? `${o.hedefler.filter(h => h.done).length} / ${o.hedefler.length} tamamlandı` : "";
  const maxDk = Math.max(60, ...o.gunler.map(g => g.dk)), oneri = oneriSec(o.durum, o.bas);
  const konu = `${ad}'in haftalık özeti (${aralik})`, kapanis = `Bu özeti ${ad} kendi isteğiyle açtı ve uygulamadan istediği zaman kapatabilir.`;
  const text = [hitap, "", `${ad}'in Zekacademy'deki ${aralik} haftasının özeti:`, "", ...satir.map(([k, v]) => `• ${k}: ${v}`),
    "", "Günlük çalışma süresi:", ...o.gunler.map(g => `  ${g.tam} (${tarihYaz(g.tarih)}): ${g.dk ? sureYaz(g.dk) : "çalışma kaydı yok"}`),
    ...(den.length ? ["", "Bu haftaki denemeler:", ...den.map(x => "  " + x)] : []),
    ...(hed.length ? ["", `Haftalık konu hedefleri (${hedOzet}):`, ...hed.map(x => "  " + x)] : []),
    "", `Genel durum: ${DURUM[o.durum]}`, oneri, "", "Sevgiler,", `${kocAd} · Zekacademy`, "", kapanis].join("\n");
  const td = 'style="padding:8px 0;color:#4B5E54;border-bottom:1px solid #EEF6F0"', tdv = 'style="padding:8px 0;text-align:right;font-weight:700;border-bottom:1px solid #EEF6F0"';
  const baslik = t => `<div style="font-size:13px;font-weight:700;color:#14532D;margin:20px 0 8px;text-transform:uppercase;letter-spacing:.4px">${t}</div>`;
  const bar = `<table style="width:100%;border-collapse:collapse;font-size:14px">${o.gunler.map(g => { const w = Math.round(g.dk / maxDk * 100);
    return `<tr><td style="padding:7px 0;color:#4B5E54;border-bottom:1px solid #EEF6F0;white-space:nowrap">${g.tam} <span style="color:#8A9A90;font-size:12px">${tarihYaz(g.tarih)}</span></td><td style="padding:7px 10px;border-bottom:1px solid #EEF6F0;width:40%"><div style="height:8px;background:#EEF6F0;border-radius:4px"><div style="height:8px;width:${Math.max(w, g.dk ? 3 : 0)}%;background:${g.dk >= 30 ? "#15803D" : "#9BBFA6"};border-radius:4px"></div></div></td><td style="padding:7px 0;text-align:right;font-weight:700;border-bottom:1px solid #EEF6F0;white-space:nowrap">${g.dk ? esc(sureYaz(g.dk)) : '<span style="color:#8A9A90;font-weight:400">—</span>'}</td></tr>`; }).join("")}</table>`;
  const liste = L => `<table style="width:100%;border-collapse:collapse;font-size:14px">${L.map(([k, v]) => `<tr><td ${td}>${esc(k)}</td><td ${tdv}>${esc(v)}</td></tr>`).join("")}</table>`;
  const html = `<div style="font-family:Arial,Helvetica,sans-serif;max-width:560px;margin:0 auto;color:#0F2A1D">
<div style="background:#14532D;color:#fff;padding:18px 22px;border-radius:14px 14px 0 0"><div style="font-size:13px;opacity:.85">Zekacademy · Haftalık veli özeti</div><div style="font-size:20px;font-weight:700;margin-top:4px">${esc(ad)} · ${esc(aralik)}</div></div>
<div style="border:1px solid #DCE7DF;border-top:0;border-radius:0 0 14px 14px;padding:18px 22px">
<p style="margin:0 0 6px">${esc(hitap)}</p><p style="margin:0 0 4px;color:#4B5E54;font-size:14px">${esc(ad)}'in geçen haftasının kısa özetini paylaşıyorum.</p>
<p style="margin:14px 0 0;padding:12px 14px;background:#EEF6F0;border-radius:10px;font-weight:700">${esc(DURUM[o.durum])}</p>
${baslik("Haftanın özeti")}${liste(satir)}
${baslik("Günlük çalışma süresi")}${bar}
${o.denemeler.length ? baslik("Bu haftaki denemeler") + liste(o.denemeler.map(d => [`${d.tur}${d.ad ? " · " + d.ad : ""}`, `${virgul(d.net)} net${farkYaz(d.fark)}`])) : ""}
${o.hedefler.length ? baslik(`Haftalık konu hedefleri · ${hedOzet}`) + liste(o.hedefler.map(h => [h.ders, `${h.konu}${h.done ? " ✓" : ""}`])) : ""}
<p style="margin:20px 0 0;font-size:14px;line-height:1.5"><b>Sizin için küçük bir not:</b> ${esc(oneri)}</p>
<p style="margin:18px 0 0">Sevgiler,<br>${esc(kocAd)} · Zekacademy</p>
<p style="margin:16px 0 0;font-size:12px;color:#6B7C72">${esc(kapanis)}</p></div></div>`;
  return { konu, text, html }; }
