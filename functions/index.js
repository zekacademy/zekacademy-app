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
import { morningText, eveningText, due, cfg } from "./logic.js";

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
async function pushTo(tokens, title, body, link = "/"){
  const list = [...new Set(tokens)].filter(Boolean);
  if (!list.length) return { sent: 0, bad: [] };
  const res = await getMessaging().sendEachForMulticast({
    tokens: list,
    data: { title, body, link },
    webpush: { headers: { Urgency: "high", TTL: "21600" }, fcmOptions: { link } },
  });
  const bad = [];
  res.responses.forEach((r, i) => {
    const code = r.error && r.error.code;
    if (code === "messaging/registration-token-not-registered" || code === "messaging/invalid-registration-token" || code === "messaging/invalid-argument") bad.push(list[i]);
  });
  return { sent: res.successCount, bad };
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

/* Yeni öğrenci kaydı veya Google Form başvurusu → koça bildirim */
export const yeniKayitBildirimi = onDocumentCreated("notifs/{id}", async (event) => {
  const n = event.data && event.data.data(); if (!n || !["kayit", "basvuru"].includes(n.type)) return;
  const tokens = await coachTokens();
  const r = n.type === "basvuru"
    ? await pushTo(tokens, "🟢 Yeni başvuru · Google Form", [n.name || "Yeni başvuru", n.hizmet, n.alan].filter(Boolean).join(" · "), "/?ac=bildirim")
    : await pushTo(tokens, "Yeni öğrenci kaydı", `${n.name || "Bir öğrenci"} kaydoldu${n.alan ? ` · ${n.alan}` : ""}${n.sinif ? ` · ${n.sinif}` : ""}`, "/?ac=bildirim");
  for (const t of r.bad) await db.collection("coachDevices").where("token", "==", t).get().then(q => Promise.all(q.docs.map(x => x.ref.delete())));
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
  if (!esit(b.anahtar, kayitli)) { res.status(403).send("anahtar"); return; }
  const cevaplar = (Array.isArray(b.cevaplar) ? b.cevaplar : []).slice(0, 40).map(x => ({ s: cut(x && x.s, 200), c: cut(x && x.c, 2000) })).filter(x => x.s);
  const bul = re => (cevaplar.find(x => re.test(x.s)) || {}).c || "";
  const doc = {
    type: "basvuru", at: new Date().toISOString(), read: false, deneme: !!b.deneme,
    name: cut(bul(/İsim|isim|ad[ıi]? ?soyad|adınız/i), 120),
    tel: cut(bul(/telefon|numara|gsm/i), 40),
    eposta: cut(bul(/mail|e-posta|eposta/i) || b.eposta, 120),
    alan: cut(bul(/alan/i), 60),
    hizmet: cut(bul(/hizmet|paket/i), 120),
    cevaplar,
  };
  await db.collection("notifs").add(doc);
  res.status(200).json({ ok: true });
});
