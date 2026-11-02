import { initializeApp, applicationDefault } from "firebase-admin/app";
import { getFirestore } from "firebase-admin/firestore";
initializeApp({ credential: applicationDefault(), projectId: "zekacademy-59b2f" });
const db = getFirestore();
const dev = await db.collection("coachDevices").get();
console.log("KOÇ CİHAZLARI:", dev.size);
dev.docs.forEach(d => { const x = d.data(); console.log(" -", d.id.slice(0,6), "token:", x.token ? "var" : "yok", "yenilendi:", x.at || "-", "|", (x.ua || "").slice(0,90)); });
const n = await db.collection("notifs").get();
const L = n.docs.map(d => ({id:d.id, ...d.data()})).filter(x => ["kayit","basvuru"].includes(x.type)).sort((a,b) => String(b.at||"").localeCompare(String(a.at||""))).slice(0,12);
console.log("SON KAYIT/BAŞVURU BİLDİRİMLERİ (belge zamanı = formdaki gönderim):");
L.forEach(x => console.log(" -", x.at, x.type, "id:", x.id.slice(0,14), "sessiz:", !!x.sessiz, "deneme:", !!x.deneme, "ad:", (x.name||"").split(" ")[0]));
for (const k of ["koc/bildirim","koc/form","system/form"]) { const d = (await db.doc(k).get()).data(); console.log(k.toUpperCase()+":", d ? JSON.stringify(k==="system/form" ? {anahtarVar: !!d.anahtar, ...Object.fromEntries(Object.entries(d).filter(([a])=>a!=="anahtar"))} : d).slice(0,1500) : "yok"); }
