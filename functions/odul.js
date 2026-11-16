/* Sınıf sıralaması ve ödüller: saf mantık (testleri: tests/odul.test.js).
   Günün 1.'si her sabah, haftanın ilk 5'i pazartesi sabahı açıklanır; çalışma arkadaşları da yarışır ama ödül sadece gerçek öğrenciye işler. */
import { ZEK, zekGunDk } from "./zek.js";
export const ODUL_BASLA = "2026-11-16"; /* yarış bu pazartesi başlar: önceki günler sayılmaz */
export const ODUL = { gun: [3], hafta: [20, 10, 10, 5, 5] };            /* ekstra soru hakkı: sıraya göre */
export const UNVAN = ["Haftanın Şampiyonu", "Haftanın 2.'si", "Haftanın 3.'sü", "İlk 5", "İlk 5"];
export const gunEkle = (d, n) => new Date(Date.parse(d + "T12:00:00Z") + n * 864e5).toISOString().slice(0, 10);
export const haftaGunu = d => new Date(d + "T12:00:00Z").getUTCDay();   /* 0 pazar, 1 pazartesi */
export const zekVar = g => !!(g && g.oto && g.zek !== false);
/* Canlı özetten bir günün dakikası (bugünse bugunDk, değilse 13 günlük geçmişten) */
export const uyeDk = (c, d) => c.gun === d ? (c.bugunDk || 0) : ((c.gunler || {})[d] || 0);
/* Grubun yarışanları: gerçek üyeler (canlı özeti olanlar) + otomatik sınıfta çalışma arkadaşları */
export function yarisanlar(g, canli){ const U = new Set(g.uyeler || []), L = [];
  for (const [uid, c] of canli) if (U.has(uid) && c.takma) L.push({ uid, takma: c.takma, zek: false, dk: d => uyeDk(c, d) });
  if (zekVar(g)) ZEK.forEach((z, i) => L.push({ uid: "__zek" + i, takma: z[0], zek: true, dk: d => zekGunDk(i, d) }));
  return L; }
/* Günler boyunca toplam dakikaya göre sıralı ilk n (0 dakika olanlar dışarıda; eşitlikte takma ad) */
export function siralama(L, gunler, n){
  return L.map(x => ({ uid: x.uid, takma: x.takma, zek: x.zek, dk: Math.round(gunler.reduce((a, d) => a + x.dk(d), 0)) }))
    .filter(x => x.dk > 0).sort((a, b) => b.dk - a.dk || a.takma.localeCompare(b.takma, "tr")).slice(0, n); }
export const sureYaz = dk => { const h = Math.floor(dk / 60), m = dk % 60; return h ? `${h} sa${m ? ` ${m} dk` : ""}` : `${m} dk`; };
export function tebrikMetni(tur, sira, dk, hak){ const ek = hak ? ` +${hak} soru hakkı kazandın.` : "";
  if (tur === "gun") return `Dün sınıfının birincisi sendin! ${sureYaz(dk)} çalıştın 👏${ek}`;
  return `Bu hafta sınıfında ${sira}. oldun! ${["🥇", "🥈", "🥉", "🏆", "🏆"][sira - 1]} ${sureYaz(dk)} çalıştın.${ek} Böyle devam 💪`; }
export function duyuruMetni(tur, liste){
  if (tur === "gun") return `🏆 Dünün birincisi: ${liste[0].takma} (${sureYaz(liste[0].dk)}). Bugün sıra sende!`;
  return `📊 Haftanın ilk 5'i: ${liste.map((x, i) => `${i + 1}. ${x.takma}`).join(" · ")}`; }
