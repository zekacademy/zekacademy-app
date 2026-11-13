/* Haftalık veli özeti: öğrencinin kendi isteğiyle velisine giden, ayrıntıya girmeyen e-posta (testleri: tests/veli.test.js) */
import { addDays, dayTasks } from "./logic.js";
const num = v => { if (v == null || v === "") return null; const n = typeof v === "number" ? v : parseFloat(String(v).replace(",", ".")); return Number.isFinite(n) ? n : null; };
const netOf = v => v == null ? null : typeof v === "number" ? v : typeof v === "object" ? ((num(v.d) || 0) - (num(v.y) || 0) / 4) : num(v);
const ALAN = { TYT: ["turkce", "sosyal", "mat", "fen"], AYT: ["mat", "fen", "sos1", "sos2"] };
export const denemeNet = d => Math.round((ALAN[d.tur] || []).reduce((a, k) => a + (netOf(d[k]) || 0), 0) * 100) / 100;
export const epostaGecerli = e => /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(String(e || "").trim());
export const sureYaz = dk => { dk = Math.round(dk); const h = Math.floor(dk / 60), m = dk % 60; return h ? `${h} saat${m ? ` ${m} dakika` : ""}` : `${m} dakika`; };
const AY = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"];
export const tarihYaz = d => { const [, m, g] = d.split("-").map(Number); return `${g} ${AY[m - 1]}`; };
export const ilkAd = n => String(n || "").trim().split(/\s+/)[0] || "Öğrenciniz";
/* Bir haftanın (pazartesi başlangıçlı) özeti */
export function veliOzet(s, bas){
  let dk = 0, gun = 0, hepsi = 0, biten = 0;
  for (let i = 0; i < 7; i++){ const d = addDays(bas, i), m = (s.gunluk || {})[d] || 0; dk += m; if (m >= 30) gun++;
    const l = dayTasks(s, d); hepsi += l.length; biten += l.filter(t => t && t.done).length; }
  const bit = addDays(bas, 6), D = (s.denemeler || []).filter(d => d && d.tur && d.tarih).sort((a, b) => a.tarih < b.tarih ? -1 : 1);
  const bu = D.filter(d => d.tarih >= bas && d.tarih <= bit), son = bu[bu.length - 1];
  let deneme = null;
  if (son){ const once = D.filter(d => d.tur === son.tur && d.tarih < son.tarih).pop(); deneme = { tur: son.tur, net: denemeNet(son), fark: once ? Math.round((denemeNet(son) - denemeNet(once)) * 100) / 100 : null, sayi: bu.length }; }
  const ort = dk / 7;
  const durum = dk === 0 ? "kayit-yok" : ort >= 240 && gun >= 6 ? "harika" : ort >= 150 && gun >= 4 ? "iyi" : "yavas";
  return { bas, bit, dk, gun, uyum: hepsi ? Math.round(biten / hepsi * 100) : null, deneme, durum }; }
const DURUM = { harika: "Harika bir hafta geçirdi 🌟", iyi: "İyi gidiyor 👍", yavas: "Bu hafta biraz yavaşladı; desteğiniz iyi gelir 🤝", "kayit-yok": "Bu hafta uygulamaya çalışma kaydı girilmedi." };
const esc = x => String(x).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
/* E-posta içeriği: konu, düz metin ve HTML */
export function veliEposta(s, o, { veliAd = "", sira = 0, kocAd = "Zekeriya Hoca" } = {}){
  const ad = ilkAd(s.name), aralik = `${tarihYaz(o.bas)} – ${tarihYaz(o.bit)}`;
  const satir = [
    ["Toplam çalışma", o.dk ? `${sureYaz(o.dk)} (günde ortalama ${sureYaz(o.dk / 7)})` : "Kayıt yok"],
    ["Çalıştığı gün", `${o.gun} / 7`],
    ...(o.uyum != null ? [["Programa uyum", `%${o.uyum}`]] : []),
    ...(o.deneme ? [[`Son ${o.deneme.tur} denemesi`, `${String(o.deneme.net).replace(".", ",")} net${o.deneme.fark != null ? ` (${o.deneme.fark >= 0 ? "+" : ""}${String(o.deneme.fark).replace(".", ",")})` : ""}`]] : []),
    ...(sira ? [["Sınıf sıralaması", `Bu hafta sınıfında ${sira}. oldu 🏆`]] : [])];
  const konu = `${ad}'in haftalık özeti (${aralik})`;
  const hitap = veliAd ? `Merhaba ${veliAd},` : "Merhaba,";
  const kapanis = `Bu özeti ${ad} kendi isteğiyle açtı ve uygulamadan istediği zaman kapatabilir.`;
  const text = [hitap, "", `${ad}'in Zekacademy'deki ${aralik} haftası:`, "", ...satir.map(([k, v]) => `• ${k}: ${v}`), "", `Genel durum: ${DURUM[o.durum]}`, "", `Sevgiler,`, `${kocAd} · Zekacademy`, "", kapanis].join("\n");
  const html = `<div style="font-family:Arial,Helvetica,sans-serif;max-width:520px;margin:0 auto;color:#0F2A1D">
<div style="background:#14532D;color:#fff;padding:18px 22px;border-radius:14px 14px 0 0"><div style="font-size:13px;opacity:.85">Zekacademy · Haftalık özet</div><div style="font-size:20px;font-weight:700;margin-top:4px">${esc(ad)} · ${esc(aralik)}</div></div>
<div style="border:1px solid #DCE7DF;border-top:0;border-radius:0 0 14px 14px;padding:18px 22px">
<p style="margin:0 0 14px">${esc(hitap)}</p>
<table style="width:100%;border-collapse:collapse;font-size:15px">${satir.map(([k, v]) => `<tr><td style="padding:8px 0;color:#4B5E54;border-bottom:1px solid #EEF6F0">${esc(k)}</td><td style="padding:8px 0;text-align:right;font-weight:700;border-bottom:1px solid #EEF6F0">${esc(v)}</td></tr>`).join("")}</table>
<p style="margin:16px 0 0;padding:12px 14px;background:#EEF6F0;border-radius:10px;font-weight:700">${esc(DURUM[o.durum])}</p>
<p style="margin:18px 0 0">Sevgiler,<br>${esc(kocAd)} · Zekacademy</p>
<p style="margin:16px 0 0;font-size:12px;color:#6B7C72">${esc(kapanis)}</p></div></div>`;
  return { konu, text, html }; }
