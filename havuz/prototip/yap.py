import json
D=json.load(open('veri.json'))
html=r'''<!DOCTYPE html><html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Zekacademy · Videodan sonra test (tasarım prototipi)</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
:root{--bg:#F3F5F4;--card:#fff;--fg:#14191A;--mut:#5d6b63;--line:#E1E6E3;--acc:#1f8a5b;--accbg:#E6F4EC;--bad:#D93636;--badbg:#FDECEC;--warn:#C27A00;--warnbg:#FFF3DC}
:root[data-tema=koyu]{--bg:#0E1211;--card:#171D1B;--fg:#E8ECE9;--mut:#9AA8A0;--line:#2A3430;--acc:#4CC38A;--accbg:#173528;--bad:#FF6B6B;--badbg:#3A1A1A;--warn:#F5B13D;--warnbg:#33260D}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:500 16px/1.55 "Plus Jakarta Sans",system-ui,sans-serif}
button{font:inherit;color:inherit;cursor:pointer}
.tel{max-width:460px;margin:0 auto;min-height:100vh;background:var(--bg);padding-bottom:40px}
.not{background:var(--warnbg);color:var(--fg);font-size:13px;padding:8px 14px;display:flex;gap:10px;align-items:center}
.not span{flex:1}.tema{display:flex;border:1px solid var(--line);border-radius:99px;padding:2px;background:var(--card)}
.tema button{border:0;background:none;font-size:12px;font-weight:700;padding:4px 10px;border-radius:99px;color:var(--mut)}.tema button[aria-pressed=true]{background:var(--fg);color:var(--card)}
.ust{display:flex;align-items:center;gap:10px;padding:14px 16px 10px}.ust b{display:block;font-size:17px}.ust small{color:var(--mut);font-size:13px}
.geri{width:36px;height:36px;border-radius:12px;border:1px solid var(--line);background:var(--card);display:grid;place-items:center}
.video{margin:0 16px;aspect-ratio:16/9;border-radius:18px;background:linear-gradient(135deg,#123526,#0b1712);display:grid;place-items:center;position:relative;overflow:hidden;color:#fff}
.video .oyn{width:62px;height:62px;border-radius:50%;background:rgba(255,255,255,.16);display:grid;place-items:center}
.video .alt{position:absolute;left:14px;right:14px;bottom:12px;font-size:13px;display:flex;justify-content:space-between;opacity:.9}
.video .bar{position:absolute;left:0;bottom:0;height:4px;width:100%;background:rgba(255,255,255,.2)}.video .bar i{display:block;height:100%;width:100%;background:#4CC38A}
.sek{display:flex;gap:6px;padding:14px 16px 6px;overflow-x:auto}
.sek button{border:1px solid var(--line);background:var(--card);border-radius:99px;padding:7px 14px;font-weight:700;font-size:14px;color:var(--mut);white-space:nowrap}
.sek button[aria-selected=true]{background:var(--fg);color:var(--card);border-color:var(--fg)}
.sek .rozet{background:var(--bad);color:#fff;border-radius:99px;font-size:11px;padding:1px 7px;margin-left:6px}
.alan{padding:10px 16px}
.kart{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:16px;margin-bottom:12px}
h2{font-size:20px;margin:0 0 6px}p{margin:0 0 8px}.mut{color:var(--mut)}.kucuk{font-size:14px}
.btn{border:1.5px solid var(--line);background:var(--card);border-radius:14px;padding:12px 16px;font-weight:700;width:100%}
.btn.pri{background:var(--acc);border-color:var(--acc);color:#fff}.btn+.btn{margin-top:8px}
.anahtar{display:flex;align-items:center;gap:12px;border:1.5px solid var(--line);border-radius:14px;padding:12px 14px;margin:12px 0;background:var(--card);width:100%;text-align:left}
.anahtar .s{width:46px;height:28px;border-radius:99px;background:var(--line);position:relative;flex:none;transition:background .2s}
.anahtar .s::after{content:"";position:absolute;top:3px;left:3px;width:22px;height:22px;border-radius:50%;background:#fff;transition:left .2s;box-shadow:0 1px 2px rgba(0,0,0,.2)}
.anahtar[aria-pressed=true] .s{background:var(--acc)}.anahtar[aria-pressed=true] .s::after{left:21px}
.anahtar div{flex:1}.anahtar small{display:block;color:var(--mut);font-size:13px}
.ilerle{display:flex;gap:5px;margin:0 0 12px}.ilerle i{flex:1;height:5px;border-radius:5px;background:var(--line)}.ilerle i.d{background:var(--acc)}.ilerle i.y{background:var(--bad)}.ilerle i.s{background:var(--fg)}
.qbas{display:flex;align-items:center;gap:6px;flex-wrap:wrap;margin-bottom:10px}
.cip{font-size:12px;font-weight:700;border-radius:99px;padding:3px 10px;border:1px solid var(--line);color:var(--mut)}
.cip.tip{color:var(--acc);border-color:var(--acc)}.cip.osym{background:var(--warnbg);border-color:transparent;color:var(--warn)}
.sure{margin-left:auto;font-variant-numeric:tabular-nums;font-weight:800;font-size:14px}.sure.az{color:var(--bad)}
.metin{font-size:17px;line-height:1.6}.metin p{margin:0 0 .8em}.metin .kok{font-weight:700;margin-top:1em}.metin .madde{padding-left:1.3em;margin-bottom:.35em}.metin .formul{text-align:center;font-size:18px}
.kesir{display:inline-flex;flex-direction:column;vertical-align:middle;text-align:center;font-size:.86em;line-height:1.15;margin:0 .12em}.kesir span:first-child{border-bottom:1.2px solid currentColor;padding:0 .15em}
.siklar{display:grid;gap:8px;margin-top:6px}.siklar.sira{grid-template-columns:repeat(auto-fill,minmax(72px,1fr))}.siklar.osym{grid-template-columns:1fr 1fr}.siklar.osym [data-h=C]{grid-column:1/span 2;justify-self:center;min-width:48%}
.sik{display:flex;align-items:center;gap:8px;border:1.5px solid var(--line);background:var(--card);border-radius:12px;padding:9px 12px;text-align:left;font-size:16px;min-height:46px}
.sik b{font-weight:800}.sik:disabled{cursor:default}.sik.dogru{border-color:var(--acc);background:var(--accbg)}.sik.yanlis{border-color:var(--bad);background:var(--badbg)}.sik.soluk{opacity:.5}
.geri-b{border-radius:14px;padding:12px 14px;margin-top:12px;font-size:15px}.geri-b b{display:block;font-size:16px;margin-bottom:2px}.geri-b.iyi{background:var(--accbg)}.geri-b.kotu{background:var(--badbg)}
.eyl{display:flex;gap:8px;margin-top:12px}.eyl .btn{flex:1;width:auto;padding:11px 10px;font-size:15px}
.kardes{border:2px solid var(--acc);border-radius:18px;padding:14px;margin-top:14px;background:var(--card);animation:gir .35s ease-out}
.kbas{display:flex;align-items:center;gap:8px;margin-bottom:10px;font-weight:800;color:var(--acc)}.kbas svg{width:20px;height:20px}
@keyframes gir{from{opacity:0;transform:translateY(6px)}}
.coz{margin-top:12px}.bilgiler{border:1.5px solid var(--line);border-radius:14px;padding:12px 14px;display:grid;gap:6px;font-size:14px}.bilgiler>span{font-weight:800;font-size:13px;color:var(--acc)}.bilgiler b{display:block;font-size:13px;color:var(--mut)}
.yol{list-style:none;margin:14px 0 0;padding:0;counter-reset:y}.yol li{position:relative;padding:0 0 16px 42px;counter-increment:y}
.yol li::before{content:counter(y);position:absolute;left:0;top:-1px;width:30px;height:30px;border-radius:50%;background:var(--acc);color:#fff;display:grid;place-items:center;font-weight:800;font-size:14px}
.yol li::after{content:"";position:absolute;left:14.5px;top:32px;bottom:2px;width:2px;background:repeating-linear-gradient(var(--acc) 0 4px,transparent 4px 8px);opacity:.45}.yol li:last-child::after{display:none}
.yol .b{font-weight:800}.yol .a{color:var(--mut);font-size:14px}.yol .a b{color:var(--fg)}
.yol .i{display:inline-block;margin-top:6px;background:var(--bg);border-left:3px solid var(--acc);border-radius:10px;padding:6px 12px;font-size:16px}.yol .i span{display:block}
.cvp{border:2px solid var(--acc);border-radius:14px;padding:10px 14px;font-size:17px;margin:4px 0 10px}.cvp span{font-size:12px;font-weight:800;color:var(--acc);margin-right:8px}
.puf{background:var(--fg);color:var(--card);border-radius:14px;padding:12px 14px;font-size:14px}.puf b{display:block;color:#F5C04A;font-size:12px}
.hizli{margin-top:10px;border-radius:14px;padding:12px 14px;font-size:14px;background:var(--warnbg)}.hizli b{display:flex;align-items:center;gap:6px;font-size:13px;color:var(--warn);margin-bottom:2px}.hizli svg{width:16px;height:16px}
.ozet-sayi{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;text-align:center;margin:12px 0}.ozet-sayi div{background:var(--bg);border-radius:12px;padding:10px 4px}.ozet-sayi b{display:block;font-size:22px}.ozet-sayi small{color:var(--mut);font-size:12px}
.tekrar{display:grid;gap:8px;margin-top:8px}.trow{display:flex;align-items:center;gap:10px;border:1px solid var(--line);border-radius:14px;padding:10px 12px;background:var(--card);width:100%;text-align:left}
.trow .ic{width:34px;height:34px;border-radius:10px;display:grid;place-items:center;flex:none;font-weight:800}.trow .ic.ok{background:var(--accbg);color:var(--acc)}.trow .ic.no{background:var(--badbg);color:var(--bad)}
.trow div{flex:1;min-width:0}.trow small{display:block;color:var(--mut);font-size:13px}
.gunler{display:flex;gap:6px;margin-top:6px;flex-wrap:wrap}.gun{font-size:12px;font-weight:700;border-radius:8px;padding:3px 8px;background:var(--bg);color:var(--mut)}.gun.bugun{background:var(--acc);color:#fff}
.ok-i{width:18px;height:18px}
</style></head><body><div class="tel" id="app"></div>
<script>
const D=__DATA__;
const TEST=D.test, KAR=D.kardes, OSYM=D.osym;
let tema='acik';try{tema=localStorage.getItem('proto-tema')||'acik'}catch(e){}
const S={sek:'test',faz:'giris',sureli:false,kalan:450,i:0,cev:{},kcev:{},acik:{},kacik:{},kardesAcik:{},bas:0,bitis:0,tim:null};
const $=s=>document.querySelector(s);
const esc=s=>String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;');
const kesir=e=>e.replace(/(^|[^\d/])(\d+)\/(\d+)(?![\d/])/g,'$1<span class="kesir"><span>$2</span><span>$3</span></span>');
const kalin=s=>kesir(esc(s)).replace(/\*\*(.+?)\*\*/g,'<b>$1</b>');
const nb=s=>s.replace(/ ([=+−×<>⇒]) /g,' $1 ');
const IK={yildirim:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><path d="M13 2L4 14h7l-1 8 9-12h-7z"/></svg>',kardes:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 4v6h6M20 20v-6h-6"/><path d="M20 10A8 8 0 0 0 6.3 5.3L4 8M4 14a8 8 0 0 0 13.7 4.7L20 16"/></svg>',play:'<svg width="26" height="26" viewBox="0 0 24 24" fill="#fff"><path d="M8 5v14l11-7z"/></svg>'};
function metin(t){const L=t.split('\n');return L.map((x,k)=>{let c='';const kok=k>=L.length-2&&/(Buna göre|olduğuna göre|hangisi|kaçtır|ifadelerinden)/.test(x)||(/^Buna göre$/.test(x.trim()));const madde=/^\s*(•|[IVX]+\.)/.test(x);const formul=!kok&&!madde&&/[=<>□]/.test(x)&&x.length<40&&!/[a-zçğıöşü]{6,}/.test(x);c=kok?'kok':madde?'madde':formul?'formul':'';return `<p class="${c}">${nb(kesir(esc(x)))}</p>`}).join('')}
function duzen(s){const m=Math.max(...Object.values(s).map(v=>v.length));return m<=7?'sira':m<=20?'osym':''}
const ZAD={kolay:'Kolay',orta:'Orta',zor:'Zor'};
function osymCip(t){const y=OSYM[t];return y&&y.length?`<span class="cip osym">ÖSYM’de çıktı: ${y.slice(-3).join(', ')}${y.length>3?' +'+(y.length-3):''}</span>`:''}
function cozum(q){const bi=q.bilgi&&q.bilgi.length?`<div class="bilgiler"><span>Bilmen gereken</span>${q.bilgi.map(b=>`<div><b>${esc(b.ad)}</b>${kesir(esc(b.ifade))}</div>`).join('')}</div>`:'';
 return `<div class="coz">${bi}<ol class="yol">${q.adimlar.map(a=>`<li><div class="b">${esc(a.baslik)}</div><div class="a">${nb(kalin(a.aciklama))}</div><div class="i">${a.islem.split(' · ').map(p=>`<span>${nb(kesir(esc(p)))}</span>`).join('')}</div>${a.gorsel?`<div style="margin-top:8px;max-width:340px">${a.gorsel}</div>`:''}</li>`).join('')}</ol>
 <div class="cvp"><span>Cevap</span><b>${q.cevap.sik})</b> ${kesir(esc(q.cevap.deger))}</div><div class="puf"><b>Püf noktası</b>${esc(q.puf)}</div>${q.kisaYol?`<div class="hizli"><b>${IK.yildirim}Sınavda hızlı yol</b>${nb(kesir(esc(q.kisaYol)))}</div>`:''}</div>`}
function soru(q,cev,acik,on){const d=duzen(q.siklar);return `<div class="metin">${metin(q.metin)}</div><div class="siklar ${d}">${Object.entries(q.siklar).map(([h,v])=>{let c='';if(cev){c=h===q.cevap.sik?'dogru':h===cev?'yanlis':'soluk'}return `<button class="sik ${c}" data-on="${on}" data-h="${h}" ${cev?'disabled':''}><b>${h})</b> ${kesir(esc(v))}</button>`}).join('')}</div>
 ${cev?`<div class="geri-b ${cev===q.cevap.sik?'iyi':'kotu'}"><b>${cev===q.cevap.sik?'Doğru!':'Doğru cevap '+q.cevap.sik+') olacaktı.'}</b>${cev===q.cevap.sik?(q.kisaYol?'Sınavda daha hızlı bir yol da var; çözümde göreceksin.':'Çözüme bakmak istersen aşağıda.'):esc(q.celdiriciler[cev]||'')}</div>`:''}
 ${acik?cozum(q):''}`}
function sureYaz(s){s=Math.max(0,s);return Math.floor(s/60)+':'+String(s%60).padStart(2,'0')}
function ciz(){document.documentElement.dataset.tema=tema;
 const yanlisTip=TEST.filter(q=>S.cev[q.id]&&S.cev[q.id]!==q.cevap.sik);
 $('#app').innerHTML=`<div class="not"><span>Tasarım prototipi · gerçek sorular, kardeşler kodla doğrulandı</span><div class="tema"><button data-tema="acik" aria-pressed="${tema==='acik'}">Açık</button><button data-tema="koyu" aria-pressed="${tema==='koyu'}">Koyu</button></div></div>
 <div class="ust"><button class="geri" aria-label="Geri"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M15 18l-6-6 6-6"/></svg></button><div><b>Temel Kavramlar</b><small>49 Günde TYT Matematik Kampı · 1. ders</small></div></div>
 <div class="video"><div class="oyn">${IK.play}</div><div class="alt"><span>Temel Kavramlar 1</span><span>İzlendi ✓</span></div><div class="bar"><i></i></div></div>
 <div class="sek" role="tablist">${[['ozet','Özet'],['test','Test'],['hata','Hata Defteri']].map(([v,l])=>`<button role="tab" data-sek="${v}" aria-selected="${S.sek===v}">${l}${v==='hata'&&yanlisTip.length?`<span class="rozet">${yanlisTip.length}</span>`:''}</button>`).join('')}</div>
 <div class="alan">${S.sek==='test'?testCiz():S.sek==='hata'?hataCiz(yanlisTip):ozetCiz()}</div>`;
 bagla();}
function ozetCiz(){return `<div class="kart"><h2>Özet</h2><p class="mut kucuk">Bu prototipte Özet sekmesi uygulamadaki gibi kalır; asıl değişiklik Test ve Hata Defteri’nde.</p></div>`}
function testCiz(){
 if(S.faz==='giris') return `<div class="kart"><h2>Videoyu bitirdin, şimdi pekiştir</h2><p class="mut">Bu konudan ${TEST.length} soru: farklı soru tiplerinden, kolay ve orta. Yanlış yaparsan aynı tipten bir kardeş soruyla hemen tekrar dene.</p>
  <button class="anahtar" id="sureli" aria-pressed="${S.sureli}"><div><b>Süreli çöz</b><small>ÖSYM temposu: ${TEST.length} soru için ${sureYaz(S.kalan)}</small></div><span class="s"></span></button>
  <button class="btn pri" id="basla">Teste başla</button></div>`;
 if(S.faz==='sonuc') return sonucCiz();
 const q=TEST[S.i], cev=S.cev[q.id], k=KAR[q.kardes], kc=S.kcev[k.id];
 return `<div class="ilerle">${TEST.map((x,j)=>`<i class="${S.cev[x.id]?(S.cev[x.id]===x.cevap.sik?'d':'y'):j===S.i?'s':''}"></i>`).join('')}</div>
 <div class="kart"><div class="qbas"><b>${S.i+1}.</b><span class="cip tip">${esc(q.tip)}</span><span class="cip">${ZAD[q.zorluk]}</span>${osymCip(q.tipId)}${S.sureli?`<span class="sure ${S.kalan<60?'az':''}" id="sure">${sureYaz(S.kalan)}</span>`:''}</div>
 ${soru(q,cev,S.acik[q.id],'ana')}
 ${cev?`<div class="eyl"><button class="btn" id="cozBtn">${S.acik[q.id]?'Çözümü gizle':'Çözümü gör'}</button>${cev!==q.cevap.sik&&!S.kardesAcik[q.id]?`<button class="btn pri" id="kardesBtn">Kardeş soruyu dene</button>`:`<button class="btn pri" id="sonraki">${S.i<TEST.length-1?'Sonraki soru':'Sonucu gör'}</button>`}</div>`:''}
 ${S.kardesAcik[q.id]?`<div class="kardes"><div class="kbas">${IK.kardes}Kardeş soru · aynı tip, yeni sayılar</div>${soru(k,kc,S.kacik[k.id],'kardes')}
   ${kc?`<div class="eyl"><button class="btn" id="kcozBtn">${S.kacik[k.id]?'Çözümü gizle':'Çözümü gör'}</button><button class="btn pri" id="sonraki">${S.i<TEST.length-1?'Sonraki soru':'Sonucu gör'}</button></div>`:''}</div>`:''}
 </div>`}
function gunEkle(n){const d=new Date();d.setDate(d.getDate()+n);return d.toLocaleDateString('tr-TR',{day:'numeric',month:'short'})}
function plan(){return `<div class="gunler">${[[1,'yarın'],[3,'3 gün'],[7,'1 hafta'],[14,'2 hafta']].map(([n,l],j)=>`<span class="gun">${l} · ${gunEkle(n)}</span>`).join('')}</div>`}
function sonucCiz(){const d=TEST.filter(q=>S.cev[q.id]===q.cevap.sik).length,y=TEST.filter(q=>S.cev[q.id]&&S.cev[q.id]!==q.cevap.sik).length,b=TEST.length-d-y,net=d-y/4,sure=Math.round((S.bitis-S.bas)/1000);
 return `<div class="kart"><h2>${d===TEST.length?'Konuyu kapmışsın':'Test bitti'}</h2>
 <div class="ozet-sayi"><div><b>${d}</b><small>Doğru</small></div><div><b style="color:var(--bad)">${y}</b><small>Yanlış</small></div><div><b>${b}</b><small>Boş</small></div><div><b style="color:var(--acc)">${String(net).replace('.',',')}</b><small>Net</small></div></div>
 <p class="kucuk mut">Süren ${sureYaz(sure)}${S.sureli?' · ÖSYM temposu '+sureYaz(450):''}</p>
 <h3 style="font-size:16px;margin:14px 0 4px">Soru tiplerin</h3>
 <div class="tekrar">${TEST.map(q=>{const ok=S.cev[q.id]===q.cevap.sik;return `<div class="trow"><span class="ic ${ok?'ok':'no'}">${ok?'✓':'!'}</span><div><b>${esc(q.tip)}</b><small>${ok?'Tamam. Karışık testlerde arada bir karşına çıkacak.':'Bu tipten yeni bir soru şu günlerde karşına çıkacak:'}</small>${ok?'':plan()}</div></div>`}).join('')}</div>
 <button class="btn pri" style="margin-top:12px" data-sek="hata">Hata Defteri’ne git</button><button class="btn" id="yeniden">Testi baştan çöz</button></div>`}
function hataCiz(L){if(!L.length) return `<div class="kart"><h2>Hata Defteri</h2><p class="mut">Henüz yanlışın yok. Testte yanlış yaptığın soru tipleri burada, tekrar günleriyle birlikte görünür.</p></div>`;
 return `<div class="kart"><h2>Hata Defteri</h2><p class="mut kucuk">Yanlış yaptığın <b>soru tipleri</b> 1, 3, 7 ve 14 gün sonra karşına <b>aynı soruyla değil, o tipten yeni bir soruyla</b> çıkar. Böylece ezber değil, öğrenme ölçülür.</p>
 <div class="tekrar">${L.map(q=>`<div class="trow"><span class="ic no">!</span><div><b>${esc(q.tip)}</b><small>Sıradaki tekrar yarın · ${gunEkle(1)}</small>${plan()}</div></div>`).join('')}</div></div>`}
function bagla(){
 document.querySelectorAll('[data-tema]').forEach(b=>b.onclick=()=>{tema=b.dataset.tema;try{localStorage.setItem('proto-tema',tema)}catch(e){}ciz()});
 document.querySelectorAll('[data-sek]').forEach(b=>b.onclick=()=>{S.sek=b.dataset.sek;ciz();scrollTo(0,0)});
 const su=$('#sureli');if(su)su.onclick=()=>{S.sureli=!S.sureli;ciz()};
 const ba=$('#basla');if(ba)ba.onclick=()=>{S.faz='soru';S.bas=Date.now();if(S.sureli){clearInterval(S.tim);S.tim=setInterval(()=>{S.kalan--;const e=$('#sure');if(e){e.textContent=sureYaz(S.kalan);e.classList.toggle('az',S.kalan<60)}if(S.kalan<=0){clearInterval(S.tim);bitir()}},1000)}ciz()};
 document.querySelectorAll('.sik[data-on]').forEach(b=>b.onclick=()=>{const q=TEST[S.i];if(b.dataset.on==='ana'){S.cev[q.id]=b.dataset.h}else{S.kcev[q.kardes]=b.dataset.h}ciz()});
 const cz=$('#cozBtn');if(cz)cz.onclick=()=>{const q=TEST[S.i];S.acik[q.id]=!S.acik[q.id];ciz()};
 const kz=$('#kcozBtn');if(kz)kz.onclick=()=>{const k=TEST[S.i].kardes;S.kacik[k]=!S.kacik[k];ciz()};
 const kb=$('#kardesBtn');if(kb)kb.onclick=()=>{S.kardesAcik[TEST[S.i].id]=true;ciz()};
 const sn=$('#sonraki');if(sn)sn.onclick=()=>{if(S.i<TEST.length-1){S.i++;ciz();scrollTo(0,0)}else bitir()};
 const yd=$('#yeniden');if(yd)yd.onclick=()=>{Object.assign(S,{faz:'giris',i:0,cev:{},kcev:{},acik:{},kacik:{},kardesAcik:{},kalan:450});ciz()};
}
function bitir(){clearInterval(S.tim);S.bitis=Date.now();S.faz='sonuc';ciz();scrollTo(0,0)}
ciz();
</script></body></html>'''
open('prototip.html','w').write(html.replace('__DATA__',json.dumps(D,ensure_ascii=False)))
print('ok')
