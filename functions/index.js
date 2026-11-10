/* Zekacademy sunucu fonksiyonları (Cloud Functions 2. nesil, Frankfurt) */
import { setGlobalOptions } from "firebase-functions/v2";
import { onSchedule } from "firebase-functions/v2/scheduler";
import { onCall, onRequest, HttpsError } from "firebase-functions/v2/https";
import { randomBytes, timingSafeEqual } from "node:crypto";
import { onDocumentCreated } from "firebase-functions/v2/firestore";
import { onMessagePublished } from "firebase-functions/v2/pubsub";
import { logger } from "firebase-functions";
import { initializeApp } from "firebase-admin/app";
import { getFirestore, FieldValue, FieldPath } from "firebase-admin/firestore";
import { getAuth } from "firebase-admin/auth";
import { getMessaging } from "firebase-admin/messaging";
import { GoogleAuth } from "google-auth-library";
import { morningText, eveningText, due, cfg, odemeHatirlat, gunGorusmeleri, hatirlatilacak } from "./logic.js";
import { getStorage } from "firebase-admin/storage";
import { KARNE_SISTEM, karneIstegi, karneDuzelt, karneZoraGec } from "./karne.js";
import { aiCfg, aiAcikMi, ayOf, kullanimId, maliyet, kalanHak, toplamHak, zoraGec, jsonCikar, anahtarDurumu, haftalikPerformans, bonusDagit, bonusMesaj, SISTEM, cozIstegi, takipIstegi } from "./soru.js";

initializeApp();
setGlobalOptions({ region: "europe-west3", maxInstances: 2, memory: "256MiB" });
const db = getFirestore();
const COACH_EMAIL = "zekacademy@app.zekacademy.com";
const PROJECT = process.env.GCLOUD_PROJECT || "zekacademy-59b2f";
const TZ = "Europe/Istanbul";

/* İstanbul saatine göre bugünün tarihi (YYYY-MM-DD) ve dakikası */
function istanbulNow(){
  const p = Object.fromEntries(new Intl.DateTimeFormat("en-CA", { timeZone: TZ, year: "numeric", month: "2-digit", day: "2-digit", hour: "2-digit", minute: "2-digit", hourCycle: "h23" })
    .formatToParts(new Date()).map(x => [x.type, x.value]));
  return { date: `${p.year}-${p.month}-${p.day}`, minutes: (+p.hour) * 60 + (+p.minute) };
}

/* Bir öğrencinin cihazlarına bildirim gönderir, geçersiz cihaz anahtarlarını temizler */
async function pushTo(tokens, title, body, link = "/", mid = ""){
  const list = [...new Set(tokens)].filter(Boolean);
  if (!list.length) return { sent: 0, bad: [] };
  const res = await getMessaging().sendEachForMulticast({
    tokens: list,
    data: { title, body, link, ...(mid ? { mid } : {}) },
    webpush: { headers: { Urgency: "high", TTL: "21600" }, fcmOptions: { link } },
  });
  const bad = [], errors = [];
  res.responses.forEach((r, i) => {
    const code = r.error && r.error.code; if (code) errors.push(code);
    if (code === "messaging/registration-token-not-registered" || code === "messaging/invalid-registration-token" || code === "messaging/invalid-argument") bad.push(list[i]);
  });
  return { sent: res.successCount, bad, errors };
}
/* Koç bildirimlerinin son durumu (Ayarlar → Bildirim testi'nde görünür) */
const yeniMid = () => Math.random().toString(36).slice(2, 10) + Date.now().toString(36);
async function kocBildirimDurum(tur, tokens, r, mid = ""){
  const kayit = { at: new Date().toISOString(), tur, mid, cihaz: [...new Set(tokens)].filter(Boolean).length, gonderildi: r.sent || 0, hatalar: r.errors || [], silinen: (r.bad || []).length };
  logger.info("koç bildirimi", kayit);
  const ref = db.doc("koc/bildirim"); const eski = ((await ref.get().catch(() => null))?.data() || {}).gecmis || [];
  await ref.set({ son: kayit, gecmis: [...eski, kayit].slice(-20) }).catch(e => logger.warn("bildirim durumu", e.message));
}
const studentTokens = s => Object.keys((s.bildirim && s.bildirim.tokens) || {});
async function dropBadStudentTokens(id, bad){
  if (!bad.length) return;
  const args = []; bad.forEach(t => { args.push(new FieldPath("bildirim", "tokens", t), FieldValue.delete()); });
  await db.doc(`students/${id}`).update(...args).catch(e => logger.warn("token temizleme", id, e.message));
}
async function coachTokens(){ return (await db.collection("coachDevices").get()).docs.map(d => d.data().token).filter(Boolean); }

/* Her 15 dakikada bir: ayarlardaki sabah/akşam saati geldiyse bir kez gönderir */
export const zamanliBildirim = onSchedule({ schedule: "*/15 * * * *", timeZone: TZ, retryCount: 0 }, async () => {
  const { date, minutes } = istanbulNow();
  const settings = (await db.doc("settings/main").get()).data() || {};
  const c = cfg(settings);
  const markRef = db.doc("system/gonderim");
  const mark = (await markRef.get()).data() || {};
  const jobs = [];
  if (c.sabahAcik && due(c.sabahSaat, minutes, mark.sabah, date)) jobs.push("sabah");
  if (c.aksamAcik && due(c.aksamSaat, minutes, mark.aksam, date)) jobs.push("aksam");
  const odemeVakti = c.odemeAcik && due(c.odemeSaat, minutes, mark.odeme, date);
  const waKeys = Array.isArray(settings.paketler) ? settings.paketler.filter(p => p.tur === "whatsapp").map(p => p.k) : ["whatsapp"];
  await formNabizKontrol().catch(e => logger.error("form nabız kontrol", e));
  if (c.gorusmeHatirlat) await gorusmeHatirlatmalari(date, minutes, waKeys).catch(e => logger.error("görüşme hatırlatma", e));
  if (!jobs.length && !odemeVakti) return;
  if (odemeVakti) { await markRef.set({ odeme: date }, { merge: true }); await odemeBildirimleri(c, date); }
  if (!jobs.length) return;
  await markRef.set(Object.fromEntries(jobs.map(j => [j, date])), { merge: true });
  const students = await db.collection("students").get();
  let sent = 0;
  for (const d of students.docs) {
    const s = d.data(), tokens = studentTokens(s);
    if (!tokens.length) continue;
    for (const job of jobs) {
      const text = job === "sabah" ? morningText(settings, s, d.id, date) : eveningText(settings, s, date);
      if (!text) continue;
      const title = job === "sabah" ? "Günün mesajı" : "Koçundan hatırlatma";
      const r = await pushTo(tokens, title, text, job === "sabah" ? "/" : "/?ac=program");
      sent += r.sent; await dropBadStudentTokens(d.id, r.bad);
    }
  }
  logger.info(`Bildirim (${jobs.join(", ")}): ${sent} gönderildi`, { date });
});

/* Görüşmeden 1 saat önce öğrenciye bildirim (her görüşme için bir kez) */
async function gorusmeHatirlatmalari(date, minutes, waKeys){
  if (minutes < 6 * 60 || minutes > 23 * 60) return;
  const [st, cn, gr] = await Promise.all([db.collection("students").get(), db.collection("coachNotes").get(), db.collection("gorusmeler").where("tarih", "==", date).get()]);
  const students = Object.fromEntries(st.docs.map(d => [d.id, d.data()])), notes = Object.fromEntries(cn.docs.map(d => [d.id, d.data()]));
  const list = gunGorusmeleri(students, notes, gr.docs.map(d => ({ id: d.id, ...d.data() })), date, waKeys);
  const markRef = db.doc("system/gorusmeHatirlatma"), mark = (await markRef.get()).data() || {};
  const gonderilen = mark.tarih === date ? (mark.anahtarlar || {}) : {};
  const simdi = hatirlatilacak(list, minutes, gonderilen); if (!simdi.length) return;
  for (const g of simdi) gonderilen[g.key] = true;
  await markRef.set({ tarih: date, anahtarlar: gonderilen });
  let sent = 0;
  for (const g of simdi) { const s = students[g.sid]; if (!s) continue; const tokens = studentTokens(s); if (!tokens.length) continue;
    const ad = String(s.name || "").trim().split(/\s+/)[0] || "";
    const r = await pushTo(tokens, "Görüşmen 1 saat sonra ⏰", `${ad ? ad.charAt(0).toLocaleUpperCase("tr") + ad.slice(1).toLocaleLowerCase("tr") + ", " : ""}bugün saat ${g.saat}'te görüşmemiz var. Programını yanında hazır tut 💪`, "/");
    sent += r.sent; await dropBadStudentTokens(g.sid, r.bad); }
  logger.info(`Görüşme hatırlatması: ${simdi.length} görüşme, ${sent} bildirim`, { date });
}

/* Haftalık yedek: her pazar 03:30, tüm veriler Storage'a JSON olarak (son 12 hafta tutulur) */
export const haftalikYedek = onSchedule({ schedule: "30 3 * * 0", timeZone: TZ, retryCount: 1, memory: "512MiB", timeoutSeconds: 300 }, async () => {
  const { date } = istanbulNow();
  const kol = ["students", "coachNotes", "notifs", "gorusmeler", "settings"], veri = { tarih: new Date().toISOString() };
  for (const k of kol) veri[k] = Object.fromEntries((await db.collection(k).get()).docs.filter(d => !(k === "settings" && d.id === "foto")).map(d => [d.id, d.data()]));
  const bucket = getStorage().bucket(), ad = `yedekler/zekacademy-${date}.json`, icerik = JSON.stringify(veri);
  await bucket.file(ad).save(icerik, { contentType: "application/json", resumable: false });
  const [dosyalar] = await bucket.getFiles({ prefix: "yedekler/" });
  const eski = dosyalar.map(f => f.name).sort().slice(0, -12);
  for (const n of eski) await bucket.file(n).delete().catch(() => {});
  await db.doc("settings/yedek").set({ son: date, boyutKB: Math.round(icerik.length / 1024), ogrenci: Object.keys(veri.students).length });
  logger.info(`Yedek alındı: ${ad} (${Math.round(icerik.length / 1024)} KB)`);
});

/* Ödeme günü ve 5 gün sonrası 18:00: ödemesi yapılmamış öğrenciye hatırlatma */
async function odemeBildirimleri(c, date){
  const notes = await db.collection("coachNotes").get();
  let sent = 0, kisi = 0;
  for (const n of notes.docs) {
    const vade = odemeHatirlat(n.data().odeme, date); if (!vade) continue;
    const sd = await db.doc(`students/${n.id}`).get(); if (!sd.exists) continue;
    const tokens = studentTokens(sd.data()); kisi++;
    if (!tokens.length) continue;
    const r = await pushTo(tokens, "Aylık döngü hatırlatması", c.odemeMesaj, "/");
    sent += r.sent; await dropBadStudentTokens(n.id, r.bad);
  }
  logger.info(`Ödeme hatırlatması: ${kisi} öğrenci, ${sent} bildirim`, { date });
}

/* Yeni öğrenci kaydı veya Google Form başvurusu → koça bildirim */
export const yeniKayitBildirimi = onDocumentCreated("notifs/{id}", async (event) => {
  const n = event.data && event.data.data(); if (!n || !["kayit", "basvuru"].includes(n.type) || n.sessiz) return;
  const tokens = await coachTokens(), mid = yeniMid();
  const r = n.type === "basvuru"
    ? await pushTo(tokens, "🟢 Yeni başvuru · Google Form", [n.name || "Yeni başvuru", n.hizmet, n.alan].filter(Boolean).join(" · "), "/?ac=bildirim", mid)
    : await pushTo(tokens, "Yeni öğrenci kaydı", `${n.name || "Bir öğrenci"} kaydoldu${n.alan ? ` · ${n.alan}` : ""}${n.sinif ? ` · ${n.sinif}` : ""}`, "/?ac=bildirim", mid);
  for (const t of r.bad) await db.collection("coachDevices").where("token", "==", t).get().then(q => Promise.all(q.docs.map(x => x.ref.delete())));
  await kocBildirimDurum(n.type === "basvuru" ? "Yeni başvuru" : "Yeni kayıt", tokens, r, mid);
});

/* Bildirim telefona ulaştı mı? Service worker bildirimi gösterince buraya haber verir (sadece son gönderilen mesajlar kabul edilir) */
export const bildirimAlindi = onRequest({ cors: false, maxInstances: 2, invoker: "public" }, async (req, res) => {
  if (req.method !== "POST") { res.status(405).send("POST"); return; }
  const b = req.body || {}, mid = String(b.mid || "").replace(/[^a-z0-9]/g, "").slice(0, 40);
  const ref = db.doc("koc/bildirim"), d = (await ref.get()).data() || {};
  if (!mid || !(d.gecmis || []).some(g => g.mid === mid)) { res.status(204).send(""); return; }
  const ua = cut(b.ua, 160), cihaz = /iphone|ipad/i.test(ua) ? "iPhone" : /android/i.test(ua) ? "Android" : /mac/i.test(ua) ? "Mac" : /windows/i.test(ua) ? "Windows" : "Cihaz";
  const alindi = [...(d.alindi || []), { mid, cihaz, at: new Date().toISOString(), izin: cut(b.izin, 20) }].slice(-40);
  await ref.set({ alindi }, { merge: true }); res.status(204).send("");
});
/* Form bağlantısı 36 saatten uzun sinyal vermediyse koça bir kez bildirim */
async function formNabizKontrol(){
  const ref = db.doc("koc/form"), f = (await ref.get()).data(); if (!f || !f.sonNabiz) return; /* henüz yeni koda geçilmediyse sessiz */
  const saat = (Date.now() - Date.parse(f.sonNabiz)) / 36e5; if (saat < 36 || f.uyarildi) return;
  const tokens = await coachTokens();
  const r = await pushTo(tokens, "⚠️ Form bağlantısı durmuş olabilir", "Google Form'dan " + Math.floor(saat) + " saattir sinyal gelmedi. Ayarlar → Google Form bağlantısı'ndan kontrol et.", "/?ac=ayarlar");
  await kocBildirimDurum("Form uyarısı", tokens, r);
  await ref.set({ uyarildi: new Date().toISOString() }, { merge: true });
}
/* Koç: bildirim testi — kayıtlı cihazlara deneme bildirimi gönderir, sonucu döndürür */
export const bildirimTest = onCall(async (req) => {
  requireCoach(req);
  const docs = (await db.collection("coachDevices").get()).docs;
  const tokens = docs.map(d => d.data().token).filter(Boolean);
  const mid = yeniMid();
  const r = await pushTo(tokens, "🔔 Test bildirimi", "Bildirimler bu cihaza ulaşıyor 👍", "/?ac=bildirim", mid);
  for (const t of r.bad) await db.collection("coachDevices").where("token", "==", t).get().then(q => Promise.all(q.docs.map(x => x.ref.delete())));
  await kocBildirimDurum("Test", tokens, r, mid);
  const son = ((await db.doc("koc/bildirim").get()).data() || {}).gecmis || [];
  return { mid, cihazlar: docs.map(d => ({ at: d.data().at || "", ua: d.data().ua || "", silindi: r.bad.includes(d.data().token) })), gonderildi: r.sent, hatalar: r.errors, gecmis: son.slice(-8).reverse() };
});

/* Sadece koçun çağırabileceği işlemler */
function requireCoach(req){
  if (!req.auth || req.auth.token.email !== COACH_EMAIL) throw new HttpsError("permission-denied", "Bu işlemi sadece koç yapabilir.");
}
export const sifreSifirla = onCall(async (req) => {
  requireCoach(req);
  const { uid, sifre } = req.data || {};
  if (typeof uid !== "string" || !uid) throw new HttpsError("invalid-argument", "Öğrenci seçilmedi.");
  if (typeof sifre !== "string" || sifre.length < 6) throw new HttpsError("invalid-argument", "Şifre en az 6 karakter olmalı.");
  const user = await getAuth().getUser(uid).catch(() => null);
  if (!user) throw new HttpsError("not-found", "Bu öğrencinin giriş hesabı bulunamadı.");
  if (user.email === COACH_EMAIL) throw new HttpsError("permission-denied", "Koç hesabı buradan değiştirilemez.");
  await getAuth().updateUser(uid, { password: sifre });
  await getAuth().revokeRefreshTokens(uid);
  await db.doc(`students/${uid}`).set({ ilkSifre: true }, { merge: true });
  return { ok: true };
});
export const ogrenciSil = onCall(async (req) => {
  requireCoach(req);
  const { uid } = req.data || {};
  if (typeof uid !== "string" || !uid) throw new HttpsError("invalid-argument", "Öğrenci seçilmedi.");
  const user = await getAuth().getUser(uid).catch(() => null);
  if (user && user.email === COACH_EMAIL) throw new HttpsError("permission-denied", "Koç hesabı silinemez.");
  if (user) await getAuth().deleteUser(uid);
  await db.doc(`students/${uid}`).delete();
  await db.doc(`coachNotes/${uid}`).delete();
  return { ok: true, hesapSilindi: !!user };
});

/* Bütçe sigortası: bütçe aşılırsa projenin ödeme bağlantısını keser (uygulama çalışmaya devam eder, ücretli özellikler durur) */
export const butceSigortasi = onMessagePublished("butce-uyari", async (event) => {
  const msg = event.data.message.json || {};
  const cost = Number(msg.costAmount || 0), budget = Number(msg.budgetAmount || 0);
  logger.info("Bütçe bildirimi", { cost, budget, currency: msg.currencyCode });
  if (!budget || cost < budget) return;
  const auth = new GoogleAuth({ scopes: ["https://www.googleapis.com/auth/cloud-billing"] });
  const client = await auth.getClient();
  const url = `https://cloudbilling.googleapis.com/v1/projects/${PROJECT}/billingInfo`;
  const info = (await client.request({ url })).data;
  if (!info.billingEnabled) { logger.info("Ödeme zaten kapalı"); return; }
  await client.request({ url, method: "PUT", data: { billingAccountName: "" } });
  logger.warn(`Bütçe aşıldı (${cost}/${budget} ${msg.currencyCode}); ödeme bağlantısı kesildi.`);
});

/* ---------- Google Form başvuruları ---------- */
const FORM_URL = `https://europe-west3-${PROJECT}.cloudfunctions.net/formBasvuru`;
/* Koç: Apps Script'e yapıştırılacak gizli anahtarı verir (yoksa oluşturur) */
export const formAnahtari = onCall(async (req) => {
  requireCoach(req);
  const ref = db.doc("system/form"), cur = (await ref.get()).data() || {};
  let anahtar = cur.anahtar;
  if (!anahtar || (req.data && req.data.yenile)) { anahtar = randomBytes(24).toString("hex"); await ref.set({ anahtar, olusturma: new Date().toISOString() }, { merge: true }); }
  return { anahtar, url: FORM_URL };
});
const esit = (a, b) => { const x = Buffer.from(String(a || "")), y = Buffer.from(String(b || "")); return x.length === y.length && x.length > 0 && timingSafeEqual(x, y); };
const cut = (v, n) => String(v == null ? "" : v).slice(0, n);
/* Google Form gönderildiğinde Apps Script buraya yollar → koça yeşil bildirim */
export const formBasvuru = onRequest({ cors: false, maxInstances: 2, invoker: "public" }, async (req, res) => {
  if (req.method !== "POST") { res.status(405).send("POST"); return; }
  const b = req.body || {};
  const kayitli = ((await db.doc("system/form").get()).data() || {}).anahtar;
  /* Sinyal anahtarı ayrı alanda gelir: eski sunucu sinyali başvuru sanmasın diye (orada 403 alır) */
  if (!esit(b.nabiz ? (b.nabizAnahtar || b.anahtar) : b.anahtar, kayitli)) { res.status(403).send("anahtar"); return; }
  /* Formdaki script düzenli "çalışıyorum" sinyali yollar; koç uygulamasında durum ve uyarı için */
  const nabizYaz = (ek) => db.doc("koc/form").set({ sonNabiz: new Date().toISOString(), ...(b.nabiz ? { tetikleyici: b.tetikleyici ?? null, kontrol: b.kontrol ?? null } : {}), ...ek }, { merge: true }).catch(e => logger.warn("form nabız", e.message));
  if (b.nabiz) { await nabizYaz({ uyarildi: null }); res.status(200).json({ ok: true, nabiz: true }); return; }
  const cevaplar = (Array.isArray(b.cevaplar) ? b.cevaplar : []).slice(0, 40).map(x => ({ s: cut(x && x.s, 200), c: cut(x && x.c, 2000) })).filter(x => x.s);
  const bul = re => (cevaplar.find(x => re.test(x.s)) || {}).c || "";
  /* Formdaki gönderim zamanı (eski başvurular aktarılırken korunur) */
  const z = Date.parse(b.zaman), now = Date.now();
  const at = Number.isFinite(z) && z <= now + 60000 && z > now - 2 * 365 * 864e5 ? new Date(z).toISOString() : new Date().toISOString();
  const doc = {
    type: "basvuru", at, read: !!b.sessiz, deneme: !!b.deneme, sessiz: !!b.sessiz,
    name: cut(bul(/İsim|isim|ad[ıi]? ?soyad|adınız/i), 120),
    tel: cut(bul(/telefon|numara|gsm/i), 40),
    eposta: cut(bul(/mail|e-posta|eposta/i) || b.eposta, 120),
    alan: cut(bul(/alan/i), 60),
    hizmet: cut(bul(/hizmet|paket/i), 120),
    cevaplar,
  };
  /* Aynı form yanıtı iki kez gelirse ikinci kez eklenmez (süreç bilgisi korunur) */
  const yid = String(b.yanitId || "").replace(/[^A-Za-z0-9_-]/g, "").slice(0, 120);
  if (yid) {
    try { await db.doc(`notifs/f_${yid}`).create(doc); }
    catch (e) { if (e.code === 6 || /already exists/i.test(e.message)) { res.status(200).json({ ok: true, zatenVar: true }); return; } throw e; }
  } else await db.collection("notifs").add(doc);
  if (!b.sessiz && !b.deneme) await nabizYaz({ sonBasvuru: new Date().toISOString(), uyarildi: null });
  res.status(200).json({ ok: true });
});


/* ===================== Soru Çözüm Merkezi (Claude) ===================== */
let AI_ANAHTAR = { v: "", at: 0 };
async function aiAnahtar(){
  if (AI_ANAHTAR.v && Date.now() - AI_ANAHTAR.at < 5 * 60e3) return AI_ANAHTAR.v;
  const v = ((await db.doc("system/ai").get()).data() || {}).anahtar || ""; AI_ANAHTAR = { v, at: Date.now() }; return v;
}
async function claude(model, content, maxTokens, sistem = SISTEM){
  const key = await aiAnahtar(); if (!key) throw new HttpsError("failed-precondition", "anahtar-yok");
  const r = await fetch("https://api.anthropic.com/v1/messages", { method: "POST",
    headers: { "x-api-key": key, "anthropic-version": "2023-06-01", "content-type": "application/json" },
    body: JSON.stringify({ model, max_tokens: maxTokens, system: sistem, messages: [{ role: "user", content }] }) });
  const j = await r.json().catch(() => ({}));
  if (!r.ok) { logger.error("claude hata", r.status, j && j.error); throw new HttpsError("unavailable", "yapay-zeka-hata"); }
  const text = (j.content || []).filter(c => c.type === "text").map(c => c.text).join("");
  return { text, usage: j.usage || {}, stop: j.stop_reason };
}
async function aiBaglam(req){
  if (!req.auth) throw new HttpsError("unauthenticated", "giris");
  const sid = req.auth.uid, koc = req.auth.token.email === COACH_EMAIL;
  const settings = (await db.doc("settings/main").get()).data() || {}, c = aiCfg(settings);
  if (!koc && !aiAcikMi(c, sid)) throw new HttpsError("failed-precondition", "kapali");
  const date = istanbulNow().date, ay = ayOf(date);
  return { sid, koc, c, date, ay, kRef: db.doc(`aiKullanim/${kullanimId(ay, sid)}`), gRef: db.doc(`aiKullanim/${ay}_genel`) };
}
async function aiKaydet(x, { hak = 0, dolar = 0, soru = 0, zor = 0, takip = 0 }){
  const { kRef, gRef, sid, ay, date, c } = x;
  const inc = FieldValue.increment;
  await kRef.set({ sid, ay, kullanilan: inc(hak), dolar: inc(dolar), soru: inc(soru), zor: inc(zor), son: new Date().toISOString(), ...(takip ? { takip: { [date]: inc(takip) } } : {}) }, { merge: true });
  await gRef.set({ ay, dolar: inc(dolar), soru: inc(soru), zor: inc(zor), gun: { [date]: inc(dolar) } }, { merge: true });
  const g = (await gRef.get()).data() || {};
  if (g.dolar >= c.uyari && !g.uyarildi) {
    await gRef.set({ uyarildi: true }, { merge: true });
    const tokens = await coachTokens(), mid = yeniMid();
    const r = await pushTo(tokens, "⚠️ Soru Çözüm bütçesi", `Bu ay ${g.dolar.toFixed(2)} $ harcandı (tavan ${c.tavan} $). ${c.tavan} $'a gelince sistem duracak.`, "/?ac=ayarlar", mid);
    await kocBildirimDurum("Soru Çözüm bütçe uyarısı", tokens, r, mid);
  }
  return g;
}

/* Öğrenci soruyu gönderir: önce kolay model, gerekirse güçlü model */
export const soruCoz = onCall({ timeoutSeconds: 180, memory: "512MiB", maxInstances: 5 }, async (req) => {
  const x = await aiBaglam(req), { c, kRef, gRef } = x, d = req.data || {};
  const resim = typeof d.resim === "string" && d.resim.startsWith("data:image/jpeg;base64,") ? d.resim.slice(23) : "";
  const metin = String(d.metin || "").slice(0, 1500), anahtar = /^[A-E]$/.test(d.anahtar || "") ? d.anahtar : "", tekrar = d.tekrar ? String(d.tekrar).slice(0, 2000) : "";
  if (!resim && !metin) throw new HttpsError("invalid-argument", "soru-yok");
  if (resim.length > 800000) throw new HttpsError("invalid-argument", "resim-buyuk");
  const [kS, gS] = await Promise.all([kRef.get(), gRef.get()]); const k = kS.data() || {}, g = gS.data() || {};
  if (!x.koc && kalanHak(c, k) <= 0) throw new HttpsError("resource-exhausted", "hak");
  if ((g.dolar || 0) >= c.tavan) throw new HttpsError("resource-exhausted", "butce");
  const icerik = [...(resim ? [{ type: "image", source: { type: "base64", media_type: "image/jpeg", data: resim } }] : []), { type: "text", text: cozIstegi({ metin, anahtar, tekrar }) }];
  let dolar = 0, model = "kolay", r = null, neden = tekrar ? "ogrenci-yanlis-dedi" : null;
  if (!tekrar) {
    const a = await claude(c.modelKolay, icerik, 2500); dolar += maliyet(c, "kolay", a.usage); r = jsonCikar(a.text);
    neden = zoraGec(r, anahtar);
  }
  if (neden) {
    try { const b = await claude(c.modelZor, icerik, 3500); dolar += maliyet(c, "zor", b.usage); const r2 = jsonCikar(b.text); if (r2) { r = r2; model = "zor"; } }
    catch (e) { logger.warn("güçlü model", e.message); if (!r) throw e; }
  }
  if (!r) { await aiKaydet(x, { dolar }); throw new HttpsError("unavailable", "cozum-okunamadi"); }
  delete r.kontrol; r.anahtar = anahtarDurumu(r, anahtar); if (r.anahtar === "uyumsuz") r.emin = false;
  const hak = r.okunabildi === false ? 0 : tekrar ? c.hakTekrar : model === "zor" ? c.hakZor : c.hakKolay;
  await aiKaydet(x, { hak, dolar, soru: 1, zor: model === "zor" ? 1 : 0 });
  const kucuk = typeof d.kucuk === "string" && d.kucuk.startsWith("data:image/jpeg;base64,") && d.kucuk.length < 60000 ? d.kucuk : null;
  const ref = await db.collection("aiSorular").add({ sid: x.sid, ay: x.ay, at: new Date().toISOString(), ders: r.ders || "", konu: r.konu || "", zorluk: r.zorluk || "", soru: String(r.soru || "").slice(0, 400),
    cevap: (r.cevap && r.cevap.sik) || "", anahtar: r.anahtar, emin: r.emin !== false, model, neden: neden || null, hak, dolar: Math.round(dolar * 1e5) / 1e5, kucuk, okunabildi: r.okunabildi !== false });
  const k2 = (await kRef.get()).data() || {};
  return { cozum: r, id: ref.id, model, hak, kalan: kalanHak(c, k2), toplam: toplamHak(c, k2) };
});

/* Takip: adımı açıkla / benzer soru / soru sor (kolay model, günlük sınırlı, hak düşmez) */
export const soruTakip = onCall({ timeoutSeconds: 120, maxInstances: 5 }, async (req) => {
  const x = await aiBaglam(req), { c, kRef, gRef, date } = x, d = req.data || {};
  const tur = ["adim", "benzer", "sohbet"].includes(d.tur) ? d.tur : "sohbet";
  const [kS, gS] = await Promise.all([kRef.get(), gRef.get()]); const k = kS.data() || {}, g = gS.data() || {};
  if (!x.koc && ((k.takip || {})[date] || 0) >= c.takipGunluk) throw new HttpsError("resource-exhausted", "takip");
  if ((g.dolar || 0) >= c.tavan) throw new HttpsError("resource-exhausted", "butce");
  const istek = [{ type: "text", text: takipIstegi(tur, d.baglam, d.metin, Number(d.adim) || 1) }];
  let a = await claude(c.modelKolay, istek, tur === "benzer" ? 1500 : 800), dolar = maliyet(c, "kolay", a.usage);
  if (!a.text.trim()) { logger.warn("takip boş yanıt", tur, a.stop); a = await claude(c.modelZor, istek, tur === "benzer" ? 1500 : 900); dolar += maliyet(c, "zor", a.usage); } /* boş geldiyse güçlü model */
  await aiKaydet(x, { dolar, takip: 1 });
  if (!a.text.trim()) throw new HttpsError("unavailable", "bos-yanit");
  if (tur === "benzer") { const q = jsonCikar(a.text); if (!q || !q.soru || !q.siklar) throw new HttpsError("unavailable", "benzer-okunamadi"); return { benzer: q }; }
  return { metin: a.text };
});

/* Deneme karnesi okuma: öğrenci karnesinin fotoğrafını / PDF'ini yükler, deneme formu dolar.
   Soru hakkından düşmez; aylık genel bütçeye yazılır, öğrenci başına günlük sınır var. */
export const denemeOku = onCall({ timeoutSeconds: 180, memory: "512MiB", maxInstances: 5 }, async (req) => {
  if (!req.auth) throw new HttpsError("unauthenticated", "giris");
  const sid = req.auth.uid, koc = req.auth.token.email === COACH_EMAIL, d = req.data || {};
  const settings = (await db.doc("settings/main").get()).data() || {}, c = aiCfg(settings);
  const date = istanbulNow().date, ay = ayOf(date), gunluk = Number(c.karneGunluk) || 10;
  const kRef = db.doc(`aiKullanim/${kullanimId(ay, sid)}`), gRef = db.doc(`aiKullanim/${ay}_genel`);
  const dosyalar = (Array.isArray(d.dosyalar) ? d.dosyalar : []).slice(0, 6), icerik = []; let boyut = 0;
  for (const f of dosyalar) {
    const v = String((f && f.veri) || ""), m = v.match(/^data:(image\/jpeg|image\/png|application\/pdf);base64,([A-Za-z0-9+/=]+)$/);
    if (!m) throw new HttpsError("invalid-argument", "dosya-gecersiz");
    boyut += m[2].length; if (m[2].length > (m[1] === "application/pdf" ? 7e6 : 1.6e6) || boyut > 9e6) throw new HttpsError("invalid-argument", "dosya-buyuk");
    icerik.push(m[1] === "application/pdf" ? { type: "document", source: { type: "base64", media_type: "application/pdf", data: m[2] } } : { type: "image", source: { type: "base64", media_type: m[1], data: m[2] } });
  }
  if (!icerik.length) throw new HttpsError("invalid-argument", "dosya-yok");
  const [kS, gS, sS] = await Promise.all([kRef.get(), gRef.get(), db.doc(`students/${sid}`).get()]);
  const k = kS.data() || {}, g = gS.data() || {}, ogr = sS.data() || {};
  if (!koc && !sS.exists) throw new HttpsError("permission-denied", "ogrenci-yok");
  if (!koc && ((k.karne || {})[date] || 0) >= gunluk) throw new HttpsError("resource-exhausted", "karne-gunluk");
  if ((g.dolar || 0) >= c.tavan) throw new HttpsError("resource-exhausted", "butce");
  /* öğrencinin uygulamadaki konu listesi (eşleme için): { TYT: { Ders: [konu, ...] }, AYT: {...} } */
  const konular = {};
  for (const ex of ["TYT", "AYT"]) { const x = (d.konular || {})[ex]; if (!x || typeof x !== "object") continue; konular[ex] = {};
    for (const [ders, ts] of Object.entries(x).slice(0, 20)) konular[ex][String(ders).slice(0, 40)] = (Array.isArray(ts) ? ts : []).slice(0, 80).map(t => String(t).slice(0, 80)); }
  icerik.push({ type: "text", text: karneIstegi({ bugun: date, alan: ogr.alan, sinif: ogr.sinif, konular }) });
  /* Önce ucuz model; düzenli belgede sayılar tutarsa yeter. El yazısı, konu analizi ya da tutarsızlıkta güçlü model. */
  let dolar = 0, model = "kolay", neden = null, a = null, r = null, out = null;
  try { a = await claude(c.modelKolay, icerik, 8000, KARNE_SISTEM); dolar += maliyet(c, "kolay", a.usage); r = jsonCikar(a.text); out = r ? karneDuzelt(r, date) : null; neden = karneZoraGec(r, out, a.stop); }
  catch (e) { logger.warn("karne ucuz model", e.message); neden = "hata"; }
  if (neden) {
    try { const b = await claude(c.modelZor, icerik, 8000, KARNE_SISTEM); dolar += maliyet(c, "zor", b.usage); const r2 = jsonCikar(b.text); if (r2) { a = b; r = r2; out = karneDuzelt(r2, date); model = "zor"; } else if (!r) a = b; }
    catch (e) { logger.warn("karne güçlü model", e.message); if (!r) throw e; }
  }
  const inc = FieldValue.increment;
  await kRef.set({ sid, ay, dolar: inc(dolar), karne: { [date]: inc(1) }, son: new Date().toISOString() }, { merge: true });
  await gRef.set({ ay, dolar: inc(dolar), karne: inc(1), gun: { [date]: inc(dolar) } }, { merge: true });
  if (!r || !out) { logger.warn("karne json yok", a && a.stop, a && a.text.slice(0, 300)); throw new HttpsError("unavailable", "karne-okunamadi"); }
  await db.collection("aiKarne").add({ sid, ay, at: new Date().toISOString(), model, neden, belge: out.belgeTuru, n: out.denemeler.length, okunabildi: out.okunabildi,
    emin: out.denemeler.every(x => x.emin), dosya: icerik.length - 1, dolar: Math.round(dolar * 1e5) / 1e5, kesildi: a.stop === "max_tokens" }).catch(() => {});
  if (a.stop === "max_tokens") out.uyarilar.push("Belge çok uzundu; bazı konular okunamamış olabilir.");
  return out;
});

/* Her gece: bütçe tahmini; pazartesi: çalışkanlara bonus hak */
export const aiGunluk = onSchedule({ schedule: "20 3 * * *", timeZone: TZ, retryCount: 0, timeoutSeconds: 300 }, async () => {
  const settings = (await db.doc("settings/main").get()).data() || {}, c = aiCfg(settings);
  if (c.acik === "kapali") return;
  const { date } = istanbulNow(), ay = ayOf(date), gRef = db.doc(`aiKullanim/${ay}_genel`);
  const g = (await gRef.get()).data() || {};
  const pazartesi = new Date(date + "T12:00:00Z").getUTCDay() === 1;
  if (!pazartesi || !c.bonusAcik || g.bonusTarih === date) return;
  const studs = (await db.collection("students").get()).docs.filter(s => aiAcikMi(c, s.id));
  const ks = await Promise.all(studs.map(s => db.doc(`aiKullanim/${kullanimId(ay, s.id)}`).get()));
  const ogrenciler = studs.map((s, i) => ({ sid: s.id, s: s.data(), k: ks[i].data() || {}, perf: haftalikPerformans(s.data(), date) }));
  const sonuc = bonusDagit(c, { harcanan: g.dolar || 0, date, ogrenciler });
  logger.info("ai bonus", { date, pay: sonuc.pay, tahmin: sonuc.tahmin, kisi: sonuc.dagitim.length });
  for (const b of sonuc.dagitim) {
    const mesaj = bonusMesaj(b), o = ogrenciler.find(z => z.sid === b.sid);
    await db.doc(`aiKullanim/${kullanimId(ay, b.sid)}`).set({ sid: b.sid, ay, bonus: FieldValue.increment(b.hak) }, { merge: true });
    await db.doc(`students/${b.sid}`).update({ aiBonus: { hak: b.hak, mesaj, at: new Date().toISOString() } }).catch(() => {});
    const r = await pushTo(studentTokens(o.s), "Soru Çözüm 🎉", mesaj, "/?ac=socoz"); await dropBadStudentTokens(b.sid, r.bad);
  }
  await gRef.set({ bonusTarih: date, bonusGecmis: FieldValue.arrayUnion({ date, kisi: sonuc.dagitim.length, hak: sonuc.dagitim.reduce((a, b) => a + b.hak, 0), tahmin: Math.round(sonuc.tahmin * 100) / 100 }) }, { merge: true });
});
