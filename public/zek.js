/* Zek AI çalışma arkadaşları: tarih + kimlikten hesaplanan çalışma düzeni.
   Bu dosyanın aynısı functions/zek.js'de (sunucu sıralama ve ödüller için); tests/zek.test.js ikisinin aynı olduğunu denetler. */
const strHash = x => [...String(x)].reduce((a,c)=>(a*31+c.charCodeAt(0))>>>0, 7);
export const ZEK = [["Sabahçı","e",410,["mat","fiz","geo"],"pc",7.5,{sac:"kisa",aks:"kulaklik",giy:"kapus"}],["Lavanta","k",360,["bio","kim","tr"],"tel",9.3,{sac:"basortu",giy:"kazak"}],
  ["Kuzey","e",300,["mat","tar","cog"],"tab",13.5,{sac:"fade",sakal:"hafif"}],["Nehir","k",455,["mat","fiz","kim"],"pc",8.4,{sac:"uzun",aks:"gozluk"}],
  ["Tıpçı34","e",480,["bio","kim","mat"],"pc",7.6,{sac:"yan",aks:"gozluk",giy:"gomlek"}],["Asel","k",250,["tr","ede","tar"],"tel",14.5,{sac:"orgu"}],
  ["Rüzgar","e",330,["geo","mat","fiz"],"tel",11.5,{sac:"kivircik"}],["Elif.k","k",390,["mat","tr","bio"],"tab",8.8,{sac:"bob",giy:"forma"}],
  ["Hedef_ODTÜ","e",430,["mat","fiz","den"],"pc",9.0,{sac:"undercut",giy:"kapus"}],["Mavi","k",280,["kim","bio","cog"],"tel",12.5,{sac:"sal",giy:"kazak"}]];
export function zekRng(seed){ let a = strHash(seed) || 1; return ()=>{ a = (a + 0x6D2B79F5) >>> 0; let t = a; t = Math.imul(t ^ t>>>15, t | 1); t ^= t + Math.imul(t ^ t>>>7, t | 61); return ((t ^ t>>>14) >>> 0) / 4294967296; }; }
/* Bir botun bir günlük oturumları: [[başlangıçDk, bitişDk, ders], ...] (gece yarısından itibaren dakika) */
export function zekGun(i, d){ const [, , taban, dersler, , bas] = ZEK[i], r = zekRng("zek"+i+":"+d);
  if(r() < 0.1) return []; const hedef = taban*(0.72 + r()*0.5), O = []; let t = Math.round(bas*60 + r()*70 - 25), top = 0, n = 0;
  while(top < hedef && t < 23*60+20){ const uz = Math.round(Math.min(hedef - top + 5, 38 + r()*80)); if(uz < 15) break; const bit = Math.min(t+uz, 23*60+40);
    O.push([t, bit, dersler[(n + Math.floor(r()*3)) % dersler.length]]); top += bit - t; n++;
    t = bit + Math.round(n%2===0 ? 50 + r()*80 : 12 + r()*30); }
  return O; }
/* Bir arkadaşın bir günde çalıştığı toplam dakika */
export const zekGunDk = (i, d) => zekGun(i, d).reduce((a,[b,e])=>a+e-b, 0);
