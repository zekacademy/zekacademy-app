/* Bildirim seçimi için saf mantık (uygulamadaki kurallarla birebir aynı). Testleri: tests/logic.test.js */
export const DEF_SABAH = [
"Hayırlı sabahlar {Ad}, sabahın bereketini yakalamanı istiyorum. Bugün sağlam bir gün seni bekliyor.",
"Hayırlı sabahlar {Ad}, bugün senden sağlam bir kronometre bekliyorum.",
"Hayırlı sabahlar {Ad}, bugün ciddi anlamda sağlam bir çalışma bekliyorum.",
"Hayırlı sabahlar {Ad}, bugün programımızı eksiksiz tamamlamaya çalışalım.",
"Hayırlı sabahlar {Ad}, erken başlayan günün bereketi başka olur. Hadi ilk görevle açalım.",
"Hayırlı sabahlar {Ad}, bugün programdaki her satırı tek tek kapatalım inşallah.",
"Hayırlı sabahlar {Ad}, bugün odaklı ve verimli bir gün geçirmeni istiyorum.",
"Hayırlı sabahlar {Ad}, dünü geride bıraktık. Bugün yeni ve sağlam bir sayfa açıyoruz.",
"Hayırlı sabahlar {Ad}, bugün kronometreyi erkenden başlatmanı bekliyorum.",
"Hayırlı sabahlar {Ad}, hedefe bir gün daha yaklaşıyoruz. Bugünü boş geçirmeyelim.",
"Hayırlı sabahlar {Ad}, bugün paragrafla güne başlayalım, gerisi kendiliğinden gelir.",
"Hayırlı sabahlar {Ad}, bugün senden disiplinli bir çalışma bekliyorum. Sana güveniyorum.",
"Hayırlı sabahlar {Ad}, bugün emek verdiğin her saat haziranda karşılığını verecek inşallah.",
"Hayırlı sabahlar {Ad}, telefonu bir kenara koyup sağlam bir ilk oturumla başlayalım.",
"Hayırlı sabahlar {Ad}, bugün programı eksiksiz bitirip akşam rahat bir kafayla yatalım.",
"Hayırlı sabahlar {Ad}, bugün yanlışlarımızdan öğrenip netlerimizi büyüteceğiz.",
"Hayırlı sabahlar {Ad}, bugün sağlam bir tempo tutturmanı istiyorum. Hadi bakalım.",
"Hayırlı sabahlar {Ad}, sabahın ilk saatleri en verimli saatler. Onları iyi değerlendirelim.",
"Hayırlı sabahlar {Ad}, bugün hedef saatini doldurmanı bekliyorum.",
"Hayırlı sabahlar {Ad}, bugün de azimle çalışalım. Emeğimiz boşa gitmeyecek inşallah.",
"Hayırlı sabahlar {Ad}, bugün branş denemeni ciddiyetle çöz, analizini de ihmal etme.",
"Hayırlı sabahlar {Ad}, bugünün programı hazır. Sana düşen tek şey başlamak.",
"Hayırlı sabahlar {Ad}, bugün dünden daha iyi bir kronometre görmek istiyorum.",
"Hayırlı sabahlar {Ad}, bugün yavaş da olsa istikrarlı ilerleyelim. Asıl kazanç istikrarda.",
"Hayırlı sabahlar {Ad}, hayalindeki bölüm için bugün de sağlam bir adım atalım.",
"Hayırlı sabahlar {Ad}, bugün dikkatini dağıtacak her şeyi uzak tutup programa odaklanalım.",
"Hayırlı sabahlar {Ad}, bugün zorlandığın konunun üstüne gitmeni istiyorum. Üstesinden gelirsin.",
"Hayırlı sabahlar {Ad}, Allah kolaylık versin. Bugün de verimli bir gün olsun inşallah.",
"Hayırlı sabahlar {Ad}, bugün yapılacakları bitirip akşam kendinle gurur duyalım.",
"Hayırlı sabahlar {Ad}, yeni bir gün, yeni bir fırsat. Bugün de sağlam bir çalışma bekliyorum."];
export const DEF_AKSAM_LIST = [
"Hayırlı akşamlar {Ad}, eğer kronometreyi ve programı hâlâ girmediysek mutlaka uygulamaya kaydedelim inşallah.",
"Hayırlı akşamlar {Ad}, bugün yoğun bir gündü. Ne kadar çalışırsak çalışalım, takip açısından kronometremizi ve yaptıklarımızı uygulamaya kaydedelim; sadece 1 dakika sürer.",
"Hayırlı akşamlar {Ad}, günü kapatmadan programdaki tamamladığın görevleri işaretleyelim.",
"Hayırlı akşamlar {Ad}, bugünkü çalışma süreni henüz göremiyorum. Yatmadan önce kronometreye kaydedelim.",
"Hayırlı akşamlar {Ad}, bugünün emeği kayıtlara geçsin. Programı ve süreyi girmeyi unutmayalım.",
"Hayırlı akşamlar {Ad}, az ya da çok fark etmez; bugün yaptıklarını mutlaka uygulamaya işleyelim.",
"Hayırlı akşamlar {Ad}, programda işaretlenmemiş görevlerin görünüyor. Bitirdiklerini işaretleyip günü kapatalım.",
"Hayırlı akşamlar {Ad}, kronometreyi kullanmadıysan sorun değil; bugünkü süreni elle ekleyelim, 1 dakikanı alır.",
"Hayırlı akşamlar {Ad}, takibimizi düzenli yapalım ki yarın programı daha doğru planlayalım. Bugünü kaydetmeyi unutma.",
"Hayırlı akşamlar {Ad}, bugünü kayda geçirip iyi bir uykuya dalalım. Yarın yeni bir gün inşallah."];
export const DEF_AKSAM = {sure:[DEF_AKSAM_LIST[3],DEF_AKSAM_LIST[7]], gorev:[DEF_AKSAM_LIST[2],DEF_AKSAM_LIST[6]], ikisi:[0,1,4,5,8,9].map(i=>DEF_AKSAM_LIST[i])};

const iso = d => { const x = new Date(d); x.setMinutes(x.getMinutes()-x.getTimezoneOffset()); return x.toISOString().slice(0,10); };
export const addDays = (s,n) => { const x = new Date(s+"T12:00:00Z"); x.setUTCDate(x.getUTCDate()+n); return x.toISOString().slice(0,10); };
const dIdx = s => (new Date(s+"T12:00:00Z").getUTCDay()+6)%7;
const monday = d => addDays(d, -dIdx(d));
const dDiff = (a,b) => Math.round((new Date(b+"T12:00:00Z")-new Date(a+"T12:00:00Z"))/864e5);
export const dayNo = d => Math.floor(new Date(d+"T12:00:00Z").getTime()/864e5);
export const strHash = x => [...String(x)].reduce((a,c)=>(a*31+c.charCodeAt(0))>>>0, 7);
const firstName = n => (n||"").split(" ")[0];
export const fillName = (m, s) => String(m).replace("{Ad}", firstName(s.name));
export const hm = x => { const [h,m] = String(x||"0:0").split(":").map(Number); return (h||0)*60+(m||0); };

export function cfg(x = {}){ return {
  sabahAcik: x.sabahAcik !== false, sabahSaat: x.sabahSaat || "08:30", sabah: x.sabah || DEF_SABAH,
  aksamAcik: x.aksamAcik !== false, aksamSaat: x.aksamSaat || "22:00", aksam: x.aksam || DEF_AKSAM, kurum: x.kurum || "zekacademy",
  odemeAcik: x.odemeAcik !== false, odemeSaat: x.odemeSaat || "18:00", odemeMesaj: x.odemeMesaj || DEF_ODEME_MESAJ,
  gorusmeHatirlat: x.gorusmeHatirlat !== false }; }

const anchors = s => (s.donem||[]).slice().sort();
export function pStart(s, d){ const an = anchors(s).filter(a=>a<=d); if(!an.length) return monday(d); const a = an[an.length-1]; return addDays(a, Math.floor(dDiff(a,d)/7)*7); }
const pIdx = (s, d) => dDiff(pStart(s,d), d);
export const dayTasks = (s, date) => ((s.weeks||{})[pStart(s,date)]||{})[pIdx(s,date)] || [];
export function minutes(s, date, nowMs = Date.now()){ let m = (s.gunluk||{})[date]||0; if(s.timer && s.timer.start && iso(new Date(s.timer.start))===date) m += (nowMs - s.timer.start)/60000; return m; }

/** Sabah mesajı: uygulamadaki kartla aynı mesaj (gün + öğrenci kimliğine göre sırayla döner). */
export function morningText(settings, student, id, date){
  const c = cfg(settings); if(!c.sabahAcik) return null;
  const L = c.sabah.filter(Boolean); if(!L.length) return null;
  return fillName(L[(dayNo(date) + strHash(id)) % L.length], student);
}
/** Akşam mesajı: sadece o gün görevi işaretlenmemiş veya süresi girilmemiş öğrenciye. */
export function eveningText(settings, student, date, nowMs = Date.now()){
  const c = cfg(settings); if(!c.aksamAcik) return null;
  const tl = dayTasks(student, date), missTasks = tl.some(x=>!x.done), missTime = minutes(student, date, nowMs)===0;
  if(!missTasks && !missTime) return null;
  const pool = (missTasks && missTime ? c.aksam.ikisi : missTime ? c.aksam.sure : c.aksam.gorev).filter(Boolean);
  const any = pool.length ? pool : [...c.aksam.ikisi, ...c.aksam.sure, ...c.aksam.gorev].filter(Boolean); if(!any.length) return null;
  return fillName(any[dayNo(date) % any.length], student);
}
/** Gönderim zamanı geldi mi? (hedef saatten itibaren 60 dk içinde ve bugün henüz gönderilmediyse) */
export function due(target, nowMinutes, lastSentDate, date){ return lastSentDate !== date && nowMinutes >= hm(target) && nowMinutes < hm(target) + 60; }

/* ---------- Ödeme hatırlatması ---------- */
export const DEF_ODEME_MESAJ = "Merhaba, bu mesaj aylık döngümüzü hatırlatma mesajıdır. Ödememizi yaptıysak bu mesajı dikkate almayalım, dekontu Zekeriya hocaya iletmen yeterli. Eğer önemli veya acil bir durum varsa Zekeriya hocaya rahatça söyleyebilirsin.";
export function addMonthsISO(d, n){ const [y,m,g] = d.split("-").map(Number); const t = new Date(Date.UTC(y, m-1+n, 1, 12)); const last = new Date(Date.UTC(t.getUTCFullYear(), t.getUTCMonth()+1, 0)).getUTCDate(); t.setUTCDate(Math.min(g,last)); return t.toISOString().slice(0,10); }
/* Ödeme günleri: başlangıçtan son tarihe kadar (uygulamadaki ile aynı hesap) */
export function vadeler(o, son){ if(!o || !o.bas) return []; const out = [];
  for(let i=0; i<240; i++){ const d = o.periyot==="hafta4" ? addDays(o.bas, 28*i) : addMonthsISO(o.bas, i); if(d > son) break; out.push(d); } return out; }
/* Bugün hatırlatma gidecek mi? Ödeme günü ve 5 gün sonrası; ödendiyse ya da taslak veriyse gitmez */
export function odemeHatirlat(o, date){ if(!o || !o.bas || o.taslak) return null; const paid = o.odenen || {};
  return vadeler(o, date).find(d => !paid[d] && (d === date || addDays(d, 5) === date)) || null; }

/* ---------- Görüşme hatırlatması (uygulamadaki gunGorusme ile aynı hesap) ---------- */
const gIdx = d => (new Date(d+"T12:00:00Z").getUTCDay()+6)%7;
const mondayOf = d => addDays(d, -gIdx(d));
const hmDk = t => { const [h,m] = String(t||"0:0").split(":").map(Number); return h*60+(m||0); };
/* Bir günün planlı görüşmeleri: students {id: s}, notes {id: coachNote}, gorusmeler [{id,...}] */
export function gunGorusmeleri(students, notes, gorusmeler, d, waKeys = ["whatsapp"]){
  const w = mondayOf(d), out = gorusmeler.filter(g=>g.tarih===d && g.sid && g.saat && g.tur!=="rapor").map(g=>({key:g.id, sid:g.sid, saat:g.saat, durum:g.durum||"planli"}));
  for(const [sid, s] of Object.entries(students)){ const z = (notes[sid]||{}).duzen; if(!z || !z.saat || waKeys.includes(s.paket)) continue;
    const gunu = (z.gun!=null && z.gun!=="") ? z.gun===gIdx(d) : pStart(s, d)===d; if(!gunu || (z.bas && d < z.bas)) continue;
    if(gorusmeler.some(g=>g.sid===sid && g.kaynak==="duzen" && (g.hafta || mondayOf(g.tarih))===w)) continue;
    out.push({key:`v:${sid}:${d}`, sid, saat:z.saat, durum:"planli"}); }
  return out; }
/* Şu an hatırlatılacaklar: başlangıcına 0-60 dk kalan, planlı ve daha önce gönderilmemiş */
export function hatirlatilacak(list, nowMinutes, gonderilen){ return list.filter(g=>g.durum==="planli" && !gonderilen[g.key] && hmDk(g.saat)-nowMinutes > 0 && hmDk(g.saat)-nowMinutes <= 60); }
