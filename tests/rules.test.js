// Firestore güvenlik kuralları testleri (emülatörde çalışır)
import { test, before, after, beforeEach } from "node:test";
import { readFileSync } from "node:fs";
import { initializeTestEnvironment, assertFails, assertSucceeds } from "@firebase/rules-unit-testing";
import { doc, getDoc, setDoc, updateDoc, getDocs, collection, deleteDoc } from "firebase/firestore";

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
