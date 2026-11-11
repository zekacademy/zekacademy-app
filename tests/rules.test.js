// Firestore güvenlik kuralları testleri (emülatörde çalışır)
import { test, before, after, beforeEach } from "node:test";
import { readFileSync } from "node:fs";
import { initializeTestEnvironment, assertFails, assertSucceeds } from "@firebase/rules-unit-testing";
import { doc, getDoc, setDoc, updateDoc, getDocs, collection, deleteDoc, query, where } from "firebase/firestore";

let env;
const COACH = { email: "zekacademy@app.zekacademy.com" };
const coach = () => env.authenticatedContext("coach", COACH).firestore();
const ali = () => env.authenticatedContext("ali", { email: "ali@app.zekacademy.com" }).firestore();
const ayse = () => env.authenticatedContext("ayse", { email: "ayse@app.zekacademy.com" }).firestore();
const anon = () => env.unauthenticatedContext().firestore();
const base = { name: "Ali Veli", kullanici: "ali", weeks: {}, plan: {}, koctanNot: null, ilkSifre: false };

before(async () => {
  env = await initializeTestEnvironment({ projectId: "demo-zekacademy", firestore: { rules: readFileSync("firestore.rules", "utf8") } });
});
after(async () => { await env.cleanup(); });
beforeEach(async () => {
  await env.clearFirestore();
  await env.withSecurityRulesDisabled(async ctx => {
    const db = ctx.firestore();
    await setDoc(doc(db, "students/ali"), base);
    await setDoc(doc(db, "students/ayse"), { ...base, name: "Ayşe", kullanici: "ayse" });
    await setDoc(doc(db, "coachNotes/ali"), { not: "gizli" });
    await setDoc(doc(db, "settings/main"), { kurum: "zekacademy" });
    await setDoc(doc(db, "notifs/n1"), { type: "kayit", sid: "ali", read: false });
  });
});

test("koç her şeyi okur ve yazar", async () => {
  await assertSucceeds(getDocs(collection(coach(), "students")));
  await assertSucceeds(getDoc(doc(coach(), "coachNotes/ali")));
  await assertSucceeds(updateDoc(doc(coach(), "students/ali"), { koctanNot: { text: "aferin" } }));
  await assertSucceeds(setDoc(doc(coach(), "settings/main"), { kurum: "x" }));
  await assertSucceeds(deleteDoc(doc(coach(), "students/ayse")));
});

test("öğrenci sadece kendi kaydını okur", async () => {
  await assertSucceeds(getDoc(doc(ali(), "students/ali")));
  await assertFails(getDoc(doc(ali(), "students/ayse")));
  await assertFails(getDocs(collection(ali(), "students")));
});

test("öğrenci koçun özel notlarını okuyamaz", async () => {
  await assertFails(getDoc(doc(ali(), "coachNotes/ali")));
  await assertFails(setDoc(doc(ali(), "coachNotes/ali"), { not: "x" }));
});

test("öğrenci kendi görevini işaretler ama koça ait alanları değiştiremez", async () => {
  await assertSucceeds(updateDoc(doc(ali(), "students/ali"), { "weeks.2026-10-26.0": [{ id: "a", t: "x", done: true }] }));
  await assertFails(updateDoc(doc(ali(), "students/ali"), { koctanNot: { text: "kendime not" } }));
  await assertFails(updateDoc(doc(ali(), "students/ali"), { donem: ["2026-10-28"] }));
  await assertFails(updateDoc(doc(ali(), "students/ali"), { kullanici: "baskasi" }));
  await assertFails(updateDoc(doc(ali(), "students/ayse"), { name: "x" }));
  await assertFails(deleteDoc(doc(ali(), "students/ali")));
});

test("öğrenci ayarları okur, değiştiremez", async () => {
  await assertSucceeds(getDoc(doc(ali(), "settings/main")));
  await assertFails(setDoc(doc(ali(), "settings/main"), { kurum: "x" }));
});

test("kayıt: öğrenci kendi kaydını oluşturur, başkasınınkini oluşturamaz", async () => {
  const yeni = () => env.authenticatedContext("yeni", { email: "yeni@app.zekacademy.com" }).firestore();
  await assertFails(setDoc(doc(yeni(), "students/yeni"), { ...base, kullanici: "yeni", donem: ["2026-10-28"] }));
  await assertSucceeds(setDoc(doc(yeni(), "students/yeni"), { ...base, kullanici: "yeni" }));
  await assertFails(setDoc(doc(yeni(), "students/baska"), { ...base }));
});

test("bildirimler: öğrenci sadece kendi kayıt bildirimini oluşturur, okuyamaz", async () => {
  await assertSucceeds(setDoc(doc(ali(), "notifs/n2"), { type: "kayit", sid: "ali", read: false, name: "Ali" }));
  await assertFails(setDoc(doc(ali(), "notifs/n3"), { type: "kayit", sid: "ayse", read: false }));
  await assertSucceeds(setDoc(doc(coach(), "gorusmeler/g1"), { sid: "ali", tarih: "2026-11-02", saat: "18:00", sure: 15 }));
  await assertFails(getDoc(doc(ali(), "gorusmeler/g1")));
  await assertFails(setDoc(doc(ali(), "gorusmeler/g2"), { sid: "ali" }));
  await assertSucceeds(setDoc(doc(coach(), "notifs/b1"), { type: "basvuru", read: true, deneme: true, name: "Deneme" }));
  await assertFails(setDoc(doc(ali(), "notifs/b2"), { type: "basvuru", sid: "ali", read: false }));
  await assertFails(getDoc(doc(ali(), "notifs/n1")));
  await assertSucceeds(getDoc(doc(coach(), "notifs/n1")));
});

test("giriş yapmamış kullanıcı hiçbir şeye erişemez", async () => {
  await assertFails(getDoc(doc(anon(), "students/ali")));
  await assertFails(getDoc(doc(anon(), "settings/main")));
  await assertFails(setDoc(doc(anon(), "notifs/x"), { type: "kayit", sid: "x", read: false }));
});

test("koçun cihaz kayıtları sadece koça açık", async () => {
  await assertSucceeds(setDoc(doc(coach(), "coachDevices/d1"), { token: "t" }));
  await assertFails(getDoc(doc(ali(), "coachDevices/d1")));
  await assertFails(setDoc(doc(ali(), "coachDevices/d2"), { token: "t" }));
  await assertFails(getDoc(doc(coach(), "system/gonderim")));
});

test("öğrenci kendi bildirim cihazını kaydedebilir", async () => {
  await assertSucceeds(updateDoc(doc(ali(), "students/ali"), { "bildirim.izin": "granted" }));
});

test("takıldığım sorular: öğrenci kendi sorusunu yönetir, başkasınınkini göremez; koç notunu sadece koç yazar", async () => {
  await assertSucceeds(setDoc(doc(ali(), "sorular/q1"), { sid: "ali", ders: "Fizik", durum: "bekliyor", thumb: "x" }));
  await assertSucceeds(setDoc(doc(ali(), "soruFoto/q1"), { sid: "ali", data: "data:image/jpeg;base64,xx" }));
  await assertFails(setDoc(doc(ali(), "sorular/q2"), { sid: "ayse", ders: "Fizik" }));
  await assertSucceeds(getDoc(doc(ali(), "sorular/q1")));
  await assertSucceeds(getDoc(doc(ali(), "soruFoto/q1")));
  await assertSucceeds(updateDoc(doc(ali(), "sorular/q1"), { durum: "cozuldu" }));
  await assertFails(updateDoc(doc(ali(), "sorular/q1"), { kocNot: "kendi notum" }));
  await assertSucceeds(updateDoc(doc(coach(), "sorular/q1"), { kocNot: "Görüşmede çözdük" }));
  await assertSucceeds(setDoc(doc(coach(), "sorular/q9"), { sid: "ayse", ders: "Kimya" }));
  await assertFails(getDoc(doc(ali(), "sorular/q9")));
  await assertSucceeds(deleteDoc(doc(ali(), "sorular/q1")));
  await assertSucceeds(deleteDoc(doc(ali(), "soruFoto/q1")));
});

test("koç bildirim durumu sadece koç tarafından okunur, kimse yazamaz", async () => {
  await assertSucceeds(getDoc(doc(coach(), "koc/bildirim")));
  await assertFails(getDoc(doc(ali(), "koc/bildirim")));
  await assertFails(setDoc(doc(coach(), "koc/bildirim"), { son: {} }));
});

test("soru çözüm: öğrenci kendi kullanımını ve sorularını okur, başkasınınkini ve geneli okuyamaz, hiçbirini yazamaz", async () => {
  await env.withSecurityRulesDisabled(async ctx => {
    const db = ctx.firestore();
    await setDoc(doc(db, "aiKullanim/2026-11_ali"), { sid: "ali", kullanilan: 3 });
    await setDoc(doc(db, "aiKullanim/2026-11_ayse"), { sid: "ayse", kullanilan: 5 });
    await setDoc(doc(db, "aiKullanim/2026-11_genel"), { dolar: 3.2 });
    await setDoc(doc(db, "aiSorular/q1"), { sid: "ali", ders: "TYT Matematik" });
    await setDoc(doc(db, "aiSorular/q2"), { sid: "ayse", ders: "Fizik" });
  });
  await assertSucceeds(getDoc(doc(ali(), "aiKullanim/2026-11_ali")));
  await assertFails(getDoc(doc(ali(), "aiKullanim/2026-11_ayse")));
  await assertFails(getDoc(doc(ali(), "aiKullanim/2026-11_genel")));
  await assertFails(setDoc(doc(ali(), "aiKullanim/2026-11_ali"), { sid: "ali", kullanilan: 0 }));
  await assertSucceeds(getDoc(doc(ali(), "aiSorular/q1")));
  await assertFails(getDoc(doc(ali(), "aiSorular/q2")));
  await assertFails(setDoc(doc(ali(), "aiSorular/q3"), { sid: "ali" }));
  await assertSucceeds(getDoc(doc(coach(), "aiKullanim/2026-11_genel")));
  await assertSucceeds(setDoc(doc(coach(), "aiKullanim/2026-11_ali"), { sid: "ali", ekHak: 10 }, { merge: true }));
  await assertFails(updateDoc(doc(ali(), "students/ali"), { aiBonus: { hak: 999 } }));
  await assertFails(updateDoc(doc(ali(), "students/ali"), { vhoca: { Matematik: "Başka Hoca" } }));
});

test("çalışma grupları: üye grubu ve canlı özetleri okur, sadece kendi özetini yazar; üye olmayan göremez", async () => {
  const veli = () => env.authenticatedContext("veli", { email: "veli@app.zekacademy.com" }).firestore();
  const ozet = { takma: "Kartal", basla: null, ders: "", gun: "2026-11-09", bugunDk: 30, gunler: {}, at: 1 };
  await env.withSecurityRulesDisabled(async ctx => {
    const db = ctx.firestore();
    await setDoc(doc(db, "gruplar/g1"), { ad: "Hedef Tıp", uyeler: ["ali", "ayse"] });
    await setDoc(doc(db, "gruplar/g1/canli/ayse"), { ...ozet, takma: "Papatya" });
  });
  await assertSucceeds(getDoc(doc(ali(), "gruplar/g1")));
  await assertSucceeds(getDocs(query(collection(ali(), "gruplar"), where("uyeler", "array-contains", "ali"))));
  await assertSucceeds(getDocs(collection(ali(), "gruplar/g1/canli")));
  await assertSucceeds(setDoc(doc(ali(), "gruplar/g1/canli/ali"), ozet));
  await assertFails(setDoc(doc(ali(), "gruplar/g1/canli/ayse"), ozet));
  await assertFails(setDoc(doc(ali(), "gruplar/g1/canli/ali"), { ...ozet, name: "Ali Veli" }));
  await assertFails(setDoc(doc(ali(), "gruplar/g1"), { ad: "x", uyeler: ["ali"] }));
  await assertFails(getDoc(doc(veli(), "gruplar/g1")));
  await assertFails(getDocs(collection(veli(), "gruplar/g1/canli")));
  await assertFails(setDoc(doc(veli(), "gruplar/g1/canli/veli"), ozet));
  await assertSucceeds(setDoc(doc(coach(), "gruplar/g2"), { ad: "Mezunlar", uyeler: ["veli"] }));
  await assertSucceeds(getDocs(collection(coach(), "gruplar/g1/canli")));
  await assertSucceeds(updateDoc(doc(ali(), "students/ali"), { takma: "Kartal" }));
});
