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
const GUNK = ["Pzt", "Sal", "Çar", "Per", "Cum", "Cmt", "Paz"];
const gunlukDk = (s, d) => (s.gunluk || {})[d] || 0;
/* Bir haftanın (pazartesi başlangıçlı) özeti; gorusmeler: o haftaki görüşme kayıtları, sinav: YKS tarihi, bugun: rapor günü */
export function veliOzet(s, bas, { gorusmeler = [], sinav = "", bugun = "" } = {}){
  let dk = 0, gun = 0, hepsi = 0, biten = 0, onceDk = 0; const gunler = [];
  for (let i = 0; i < 7; i++){ const d = addDays(bas, i), m = gunlukDk(s, d); dk += m; if (m >= 30) gun++; gunler.push({ g: GUNK[i], dk: m });
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
const ONERI = { harika: "Emeğini fark ettiğinizi söylemeniz, bu tempoyu korumasına çok yardımcı olur.", iyi: "Küçük bir tebrik ve güzel bir dinlenme molası motivasyonunu artırır.", yavas: "Baskı yerine nasıl hissettiğini sormanız ve birlikte küçük bir hedef koymanız iyi gelir.", "kayit-yok": "Uygulamaya süresini girmesini hatırlatmanız yeterli olur." };
const esc = x => String(x).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
const virgul = n => String(n).replace(".", ",");
const farkYaz = f => f == null ? "" : ` (${f >= 0 ? "+" : ""}${virgul(f)})`;
/* E-posta içeriği: konu, düz metin ve HTML */
export function veliEposta(s, o, { sira = 0, kocAd = "Zekeriya Hoca" } = {}){
  const ad = ilkAd(s.name), aralik = `${tarihYaz(o.bas)} – ${tarihYaz(o.bit)}`, hitap = "Merhaba değerli velim,";
  const degisim = o.onceDk ? Math.round(o.dk - o.onceDk) : null;
  const satir = [
    ["Toplam çalışma", o.dk ? sureYaz(o.dk) : "Kayıt yok"],
    ...(o.dk ? [["Günlük ortalama", sureYaz(o.dk / 7)]] : []),
    ...(degisim != null && Math.abs(degisim) >= 30 ? [["Geçen haftaya göre", `${degisim > 0 ? "+" : "−"}${sureYaz(Math.abs(degisim))}`]] : []),
    ["Çalıştığı gün", `${o.gun} / 7`],
    ...(o.enIyi ? [["En verimli günü", `${o.enIyi.g} · ${sureYaz(o.enIyi.dk)}`]] : []),
    ...(o.gorev.hepsi ? [["Tamamlanan görev", `${o.gorev.biten} / ${o.gorev.hepsi} (%${o.uyum})`]] : []),
    ...(o.gorusme ? [["Koçuyla haftalık görüşme", "Yapıldı ✓"]] : []),
    ...(sira ? [["Sınıf sıralaması", `Bu hafta sınıfında ${sira}. oldu 🏆`]] : []),
    ...(o.kalan != null ? [["YKS'ye kalan", `${o.kalan} gün`]] : [])];
  const den = o.denemeler.map(d => `${d.tur} denemesi${d.ad ? ` (${d.ad})` : ""}: ${virgul(d.net)} net${farkYaz(d.fark)}`);
  const hed = o.hedefler.map(h => `${h.ders}: ${h.konu}${h.done ? " ✓" : ""}`);
  const hedOzet = o.hedefler.length ? `${o.hedefler.filter(h => h.done).length} / ${o.hedefler.length} tamamlandı` : "";
  const maxDk = Math.max(60, ...o.gunler.map(g => g.dk));
  const konu = `${ad}'in haftalık özeti (${aralik})`, kapanis = `Bu özeti ${ad} kendi isteğiyle açtı ve uygulamadan istediği zaman kapatabilir.`;
  const text = [hitap, "", `${ad}'in Zekacademy'deki ${aralik} haftasının özeti:`, "", ...satir.map(([k, v]) => `• ${k}: ${v}`),
    "", "Günlük çalışma:", ...o.gunler.map(g => `  ${g.g}: ${g.dk ? sureYaz(g.dk) : "—"}`),
    ...(den.length ? ["", "Bu haftaki denemeler:", ...den.map(x => "  " + x)] : []),
    ...(hed.length ? ["", `Haftalık konu hedefleri (${hedOzet}):`, ...hed.map(x => "  " + x)] : []),
    "", `Genel durum: ${DURUM[o.durum]}`, ONERI[o.durum], "", "Sevgiler,", `${kocAd} · Zekacademy`, "", kapanis].join("\n");
  const td = 'style="padding:8px 0;color:#4B5E54;border-bottom:1px solid #EEF6F0"', tdv = 'style="padding:8px 0;text-align:right;font-weight:700;border-bottom:1px solid #EEF6F0"';
  const baslik = t => `<div style="font-size:13px;font-weight:700;color:#14532D;margin:20px 0 8px;text-transform:uppercase;letter-spacing:.4px">${t}</div>`;
  const bar = `<table style="width:100%;border-collapse:collapse;table-layout:fixed"><tr>${o.gunler.map(g => { const h = Math.round(g.dk / maxDk * 80);
    return `<td style="vertical-align:bottom;text-align:center;padding:0 3px"><div style="font-size:11px;color:#4B5E54;margin-bottom:4px">${g.dk ? (g.dk >= 60 ? virgul(Math.round(g.dk / 6) / 10) + " sa" : Math.round(g.dk) + " dk") : "–"}</div><div style="height:${Math.max(h, 3)}px;background:${g.dk >= 30 ? "#15803D" : "#DCE7DF"};border-radius:4px 4px 0 0"></div></td>`; }).join("")}</tr>
<tr>${o.gunler.map(g => `<td style="text-align:center;font-size:12px;color:#4B5E54;padding-top:6px">${g.g}</td>`).join("")}</tr></table>`;
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
<p style="margin:20px 0 0;font-size:14px;line-height:1.5"><b>Sizin için küçük bir not:</b> ${esc(ONERI[o.durum])}</p>
<p style="margin:18px 0 0">Sevgiler,<br>${esc(kocAd)} · Zekacademy</p>
<p style="margin:16px 0 0;font-size:12px;color:#6B7C72">${esc(kapanis)}</p></div></div>`;
  return { konu, text, html }; }
