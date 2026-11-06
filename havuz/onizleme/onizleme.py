import json
Q=json.load(open(__import__('sys').argv[1]))
data=json.dumps([{k:q[k] for k in ('id','konu','zorluk','metin','sekil','siklar','cevap','istenen','bilgi','ipuclari','adimlar','puf','celdiriciler','kaynakKart','kalip','adimSayisi')} for q in Q],ensure_ascii=False)
html=r'''<!DOCTYPE html>
<html lang="tr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Soru Havuzu · Pilot Parti 1 · Sayı Kümeleri</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;0,8..60,700;1,8..60,400&display=swap" rel="stylesheet">
<style>
:root{--zemin:#EEF0F3;--kagit:#FFFFFF;--murekkep:#0F1217;--kursun:#5E6573;--silik:#959BA6;--cizgi:#E3E6EB;
--yesil:#16A34A;--yesil-zemin:#E3F6EA;--kirmizi:#D93636;--kirmizi-zemin:#FDECEC;--sari:#E08A00;--sari-zemin:#FFF1D9;--karalama:#2B3038}
@media (prefers-color-scheme:dark){:root{--zemin:#0A0B0E;--kagit:#14161B;--murekkep:#F2F4F7;--kursun:#A3A9B5;--silik:#6D7380;--cizgi:#262A33;
--yesil:#3DD47A;--yesil-zemin:#11291B;--kirmizi:#FF6B6B;--kirmizi-zemin:#331616;--sari:#F5B13D;--sari-zemin:#2E2210;--karalama:#D6DAE1}}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--zemin);color:var(--murekkep);font:500 16px/1.5 "Plus Jakarta Sans",system-ui,sans-serif}
button{font:inherit;color:inherit}
.ekran{max-width:520px;margin:0 auto;min-height:100vh;display:flex;flex-direction:column;background:var(--kagit)}
@media(min-width:560px){.ekran{margin:24px auto;min-height:auto;border-radius:28px;box-shadow:0 1px 0 var(--cizgi),0 30px 60px -30px rgba(15,18,23,.25)}}
/* üst */
.ust{display:flex;align-items:center;gap:12px;padding:18px 20px 10px}
.konu{font-weight:700;font-size:15px}
.konu small{display:block;font-weight:500;color:var(--kursun);font-size:13px}
.sayac{margin-left:auto;font-variant-numeric:tabular-nums;color:var(--kursun);font-size:14px}
.ilerleme{height:4px;margin:0 20px;background:var(--cizgi);border-radius:4px;overflow:hidden}
.ilerleme i{display:block;height:100%;background:var(--yesil);border-radius:4px;transition:width .4s ease}
/* soru kâğıdı */
.kagit{padding:26px 22px 8px 22px;display:grid;grid-template-columns:44px 1fr;column-gap:10px}
.no{font:700 46px/0.9 "Source Serif 4",serif;color:var(--murekkep);font-variant-numeric:lining-nums;padding-top:4px}
.metin{font:400 19px/1.62 "Source Serif 4",Georgia,serif;letter-spacing:.002em;max-width:34em}
.metin p{margin:0 0 .55em}
.metin p.kok{font-weight:700;margin-top:.8em}
.metin p.madde{padding-left:1.1em;text-indent:-1.1em}
.metin p.formul{text-align:center;font-size:21px;margin:.7em 0;font-variant-numeric:tabular-nums;white-space:nowrap}
.sekil{grid-column:2;color:var(--murekkep);margin:4px 0 6px}
.sekil svg{width:100%;height:auto;max-width:360px;display:block}
/* optik şıklar */
.siklar{list-style:none;margin:10px 0 0;padding:0 16px 4px 16px;display:grid;gap:2px}
.sik{display:flex;align-items:center;gap:14px;width:100%;text-align:left;background:none;border:0;border-radius:16px;padding:10px 12px;cursor:pointer;min-height:50px;transition:background .2s}
.sik:hover{background:var(--zemin)}
.sik:focus-visible{outline:2px solid var(--yesil);outline-offset:2px}
.balon{position:relative;flex:none;width:34px;height:34px;border-radius:50%;border:1.6px solid var(--kursun);display:grid;place-items:center;font:700 14px "Plus Jakarta Sans";color:var(--kursun);overflow:hidden}
.balon svg{position:absolute;inset:0;width:100%;height:100%;opacity:0}
.balon svg path{stroke:var(--karalama);stroke-width:5;fill:none;stroke-linecap:round;stroke-dasharray:240;stroke-dashoffset:240}
.deger{font:400 19px "Source Serif 4",serif;font-variant-numeric:tabular-nums}
.sik.secili .balon svg{opacity:1}.sik.secili .balon svg path{animation:karala .55s ease-out forwards}
@keyframes karala{to{stroke-dashoffset:0}}
.sik.dogru .balon{border-color:var(--yesil);background:var(--yesil);color:#fff;transition:background .25s .45s,border-color .25s .45s}
.sik.dogru .balon svg{opacity:0;transition:opacity .2s .45s}
.sik.dogru .deger{font-weight:600}
.sik.yanlis .balon{border-color:var(--kirmizi)}.sik.yanlis .balon svg path{stroke:var(--kirmizi)}
.sik.goster .balon{border-color:var(--yesil);color:var(--yesil);border-width:2.4px}
.cozuldu .sik{cursor:default}.cozuldu .sik:hover{background:none}
.cozuldu .sik:not(.dogru):not(.yanlis):not(.goster){opacity:.45}
/* geri bildirim */
.not{margin:6px 22px 0 66px;font-size:15px;line-height:1.45;border-radius:14px;padding:12px 14px;display:none}
.not.acik{display:block;animation:belir .3s ease-out}
.not.iyi{background:var(--yesil-zemin)}.not.kotu{background:var(--kirmizi-zemin)}
.not b{display:block;font-size:16px;margin-bottom:2px}
@keyframes belir{from{opacity:0;transform:translateY(-4px)}}
/* ipucu ve çözüm */
.eylemler{display:flex;gap:10px;padding:18px 20px 8px}
.btn{flex:1;border-radius:14px;padding:13px 14px;font-weight:700;font-size:15px;cursor:pointer;border:1.5px solid var(--cizgi);background:var(--kagit)}
.btn.ana{background:var(--murekkep);color:var(--kagit);border-color:var(--murekkep)}
.btn:disabled{opacity:.4;cursor:default}
.btn:focus-visible{outline:2px solid var(--yesil);outline-offset:2px}
.ipucu{margin:8px 20px 0;background:var(--sari-zemin);border-radius:14px;padding:12px 14px;font-size:15px;display:none}
.ipucu.acik{display:block;animation:belir .3s ease-out}
.ipucu ol{margin:0;padding-left:20px}.ipucu li+li{margin-top:6px}
.cozum{display:none;padding:6px 20px 8px}.cozum.acik{display:block}
.istenen{font-size:15px;color:var(--kursun);margin:10px 0 12px}
.istenen strong{color:var(--murekkep)}
.bilgi{border-left:3px solid var(--yesil);padding:6px 0 6px 12px;margin:0 0 14px;font-size:15px}
.bilgi div+div{margin-top:4px}
.adimlar{list-style:none;margin:0;padding:0;counter-reset:a}
.adim{position:relative;padding:0 0 18px 44px;counter-increment:a;display:none}
.adim.acik{display:block;animation:belir .35s ease-out}
.adim::before{content:counter(a);position:absolute;left:0;top:0;width:30px;height:30px;border-radius:50%;background:var(--zemin);display:grid;place-items:center;font-weight:800;font-size:14px}
.adim::after{content:"";position:absolute;left:14.5px;top:34px;bottom:4px;width:1.5px;background:var(--cizgi)}
.adim:last-child::after{display:none}
.adim h4{margin:3px 0 2px;font-size:16px}
.adim p{margin:0;color:var(--kursun);font-size:15px}.adim p b{color:var(--murekkep)}
.islem{margin-top:8px;font:600 18px/1.4 "Source Serif 4",serif;font-variant-numeric:tabular-nums;background:var(--zemin);border-radius:12px;padding:9px 12px;display:inline-block}
.puf{display:none;margin:4px 0 6px;border-radius:16px;padding:14px 16px;background:var(--murekkep);color:var(--kagit);font-size:15px}
.puf.acik{display:block;animation:belir .35s ease-out}.puf b{display:block;margin-bottom:2px}
.gezinti{display:flex;justify-content:space-between;gap:10px;padding:14px 20px 18px;margin-top:auto}
.gezinti .btn{flex:0 0 auto;padding:12px 18px}
/* koç şeridi */
.koc{border-top:1px dashed var(--cizgi);padding:12px 20px 18px;background:var(--zemin)}
.koc-ust{display:flex;align-items:center;gap:8px;font-size:13px;color:var(--kursun);margin-bottom:8px}
.koc-ust span{margin-left:auto}
.kararlar{display:flex;gap:8px}
.karar{flex:1;border:1.5px solid var(--cizgi);background:var(--kagit);border-radius:12px;padding:9px 6px;font-weight:700;font-size:14px;cursor:pointer}
.karar[aria-pressed=true][data-v=onay]{background:var(--yesil);border-color:var(--yesil);color:#fff}
.karar[aria-pressed=true][data-v=duzelt]{background:var(--sari);border-color:var(--sari);color:#fff}
.karar[aria-pressed=true][data-v=at]{background:var(--kirmizi);border-color:var(--kirmizi);color:#fff}
.koc textarea{width:100%;margin-top:8px;min-height:40px;border:1.5px solid var(--cizgi);border-radius:12px;background:var(--kagit);color:var(--murekkep);font:inherit;font-size:14px;padding:8px 10px;resize:vertical}
.koc .kopyala{margin-top:8px;width:100%}
.kaynak{font-size:12px;color:var(--silik);margin-top:6px}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}.sik.secili .balon svg path{stroke-dashoffset:0}}
</style></head><body>
<main class="ekran" id="ekran">
 <div class="ust"><div class="konu" id="konu"></div><div class="sayac" id="sayac"></div></div>
 <div class="ilerleme"><i id="cubuk"></i></div>
 <section class="kagit" aria-live="polite"><div class="no" id="no"></div><div class="metin" id="metin"></div><div class="sekil" id="sekil"></div></section>
 <ol class="siklar" id="siklar"></ol>
 <div class="not" id="not"></div>
 <div class="eylemler"><button class="btn" id="ipucuBtn">İpucu al</button><button class="btn ana" id="cozumBtn">Çözümü gör</button></div>
 <div class="ipucu" id="ipucu"><ol id="ipucuList"></ol></div>
 <section class="cozum" id="cozum">
  <p class="istenen" id="istenen"></p><div class="bilgi" id="bilgi"></div>
  <ol class="adimlar" id="adimlar"></ol>
  <div class="puf" id="puf"></div>
 </section>
 <div class="gezinti"><button class="btn" id="geri">Önceki</button><button class="btn" id="ileri">Sonraki soru</button></div>
 <section class="koc" aria-label="Koç değerlendirmesi">
  <div class="koc-ust">Koç alanı, öğrenci görmez<span id="isaretli"></span></div>
  <div class="kararlar"><button class="karar" data-v="onay" aria-pressed="false">Onay</button><button class="karar" data-v="duzelt" aria-pressed="false">Düzeltilsin</button><button class="karar" data-v="at" aria-pressed="false">At</button></div>
  <textarea id="kocNot" placeholder="Not: neyi değiştireyim?"></textarea>
  <button class="btn kopyala" id="kopyala">Kararları kopyala</button>
  <div class="kaynak" id="kaynak"></div>
 </section>
</main>
<script>
const Q=__DATA__;
const $=id=>document.getElementById(id);
const esc=s=>s.replace(/&/g,'&amp;').replace(/</g,'&lt;');
const kalin=s=>esc(s).replace(/\*\*(.+?)\*\*/g,'<b>$1</b>');
const KARALAMA='<svg viewBox="0 0 34 34" aria-hidden="true"><path d="M9 12 L24 9 M7 17 L27 13 M7 22 L27 18 M9 26 L25 23"/></svg>';
let i=0, durum=Q.map(()=>({secim:null,ipucu:0,adim:0})), koc={};
try{koc=JSON.parse(localStorage.getItem('pilot1-koc')||'{}')}catch(e){}
function metinHTML(t){
  const satirlar=t.split('\n'); const son=satirlar.length-1;
  return satirlar.map((s,k)=>{
    const kok=/^(Buna göre|.*olduğuna göre|.*hangisi|.*kaçtır|.*ifadelerinden)/.test(s)&&k>=son-1;
    const madde=/^(•|[IVX]+\.)/.test(s.trim());
    const formul=!madde&&!kok&&/[=<>≤≥]/.test(s)&&s.length<40&&!/[a-zçğıöşü]{5,}/.test(s.replace(/\bve\b/g,''));
    const t=esc(s).replace(/ ([+−×÷=<>≤≥]) /g,'\u00a0$1\u00a0');
    return `<p class="${kok?'kok':''}${madde?' madde':''}${formul?' formul':''}">${t}</p>`}).join('');
}
function goster(){
  const q=Q[i], d=durum[i];
  $('konu').innerHTML=esc(q.konu.split(' · ')[1]||q.konu)+'<small>'+esc(q.konu.split(' · ')[0])+'</small>';
  $('sayac').textContent=(i+1)+' / '+Q.length;
  $('cubuk').style.width=((i+1)/Q.length*100)+'%';
  $('no').textContent=i+1; $('metin').innerHTML=metinHTML(q.metin);
  $('sekil').innerHTML=q.sekil||''; $('sekil').style.display=q.sekil?'block':'none';
  $('siklar').innerHTML=Object.entries(q.siklar).map(([h,v])=>`<li><button class="sik" data-h="${h}" aria-label="${h} şıkkı: ${esc(v)}"><span class="balon">${h}${KARALAMA}</span><span class="deger">${esc(v)}</span></button></li>`).join('');
  $('siklar').classList.remove('cozuldu');
  document.querySelectorAll('.sik').forEach(b=>b.onclick=()=>sec(b.dataset.h));
  $('not').className='not';
  $('ipucuList').innerHTML=''; $('ipucu').className='ipucu'; $('ipucuBtn').disabled=false; $('ipucuBtn').textContent='İpucu al';
  $('istenen').innerHTML='<strong>Ne isteniyor?</strong> '+esc(q.istenen);
  $('bilgi').innerHTML=q.bilgi.map(b=>`<div><b>${esc(b.ad)}:</b> ${esc(b.ifade)}</div>`).join(''); $('bilgi').style.display=q.bilgi.length?'block':'none';
  $('adimlar').innerHTML=q.adimlar.map(a=>`<li class="adim"><h4>${esc(a.baslik)}</h4><p>${kalin(a.aciklama)}</p><div class="islem">${esc(a.islem)}</div></li>`).join('');
  $('puf').innerHTML='<b>Püf noktası</b>'+esc(q.puf); $('puf').className='puf';
  $('cozum').className='cozum'; $('cozumBtn').textContent='Çözümü gör'; $('cozumBtn').disabled=false;
  $('geri').disabled=i===0; $('ileri').textContent=i===Q.length-1?'Başa dön':'Sonraki soru';
  // durumu geri yükle
  for(let k=0;k<d.ipucu;k++) ipucuEkle(false);
  if(d.secim) sec(d.secim,true);
  for(let k=0;k<d.adim;k++) adimAc(false);
  // koç
  const c=koc[q.id]||{}; document.querySelectorAll('.karar').forEach(b=>b.setAttribute('aria-pressed',String(c.v===b.dataset.v)));
  $('kocNot').value=c.n||''; $('kaynak').textContent='Kart: '+q.kaynakKart+' · '+q.zorluk+' · '+q.adimSayisi+' adım';
  sayKoc();
}
function sec(h,sessiz){
  const q=Q[i], d=durum[i]; if(d.secim&&!sessiz) return; d.secim=h;
  const dogru=q.cevap.sik; $('siklar').classList.add('cozuldu');
  document.querySelectorAll('.sik').forEach(b=>{const x=b.dataset.h;
    if(x===h) b.classList.add('secili', x===dogru?'dogru':'yanlis');
    else if(x===dogru) setTimeout(()=>b.classList.add('goster'),sessiz?0:450);});
  const n=$('not');
  if(h===dogru){n.className='not iyi acik';n.innerHTML='<b>Doğru: '+esc(q.cevap.deger)+'</b>'+(i<Q.length-1?'İstersen çözüm adımlarına da bak.':'Partinin son sorusu.');}
  else{n.className='not kotu acik';n.innerHTML='<b>Doğru cevap '+dogru+' olacaktı.</b>'+esc(q.celdiriciler[h]||'');}
}
function ipucuEkle(kaydet=true){
  const q=Q[i], d=durum[i], k=$('ipucuList').children.length; if(k>=q.ipuclari.length) return;
  const li=document.createElement('li'); li.textContent=q.ipuclari[k]; $('ipucuList').appendChild(li); $('ipucu').className='ipucu acik';
  if(kaydet) d.ipucu=k+1;
  const kalan=q.ipuclari.length-k-1; $('ipucuBtn').textContent=kalan?'Bir ipucu daha':'İpuçları bitti'; $('ipucuBtn').disabled=!kalan;
}
function adimAc(kaydet=true){
  const q=Q[i], d=durum[i], adimlar=[...document.querySelectorAll('.adim')], k=adimlar.findIndex(a=>!a.classList.contains('acik'));
  $('cozum').className='cozum acik';
  if(k===-1){return}
  adimlar[k].classList.add('acik'); if(kaydet) d.adim=k+1;
  if(k===adimlar.length-1){$('puf').className='puf acik';$('cozumBtn').textContent='Çözüm tamam';$('cozumBtn').disabled=true}
  else $('cozumBtn').textContent='Sonraki adım';
  if(kaydet) adimlar[k].scrollIntoView({behavior:matchMedia('(prefers-reduced-motion:reduce)').matches?'auto':'smooth',block:'nearest'});
}
$('ipucuBtn').onclick=()=>ipucuEkle(); $('cozumBtn').onclick=()=>adimAc();
$('geri').onclick=()=>{if(i>0){i--;goster();scrollTo(0,0)}};
$('ileri').onclick=()=>{i=(i+1)%Q.length;goster();scrollTo(0,0)};
document.addEventListener('keydown',e=>{if(e.target.tagName==='TEXTAREA')return;
  if(e.key==='ArrowRight')$('ileri').click(); if(e.key==='ArrowLeft')$('geri').click();
  const h=e.key.toUpperCase(); if('ABCDE'.includes(h)&&h.length===1) sec(h);});
function kaydetKoc(){try{localStorage.setItem('pilot1-koc',JSON.stringify(koc))}catch(e){} sayKoc()}
function sayKoc(){$('isaretli').textContent=Object.values(koc).filter(c=>c.v).length+' / '+Q.length+' işaretli'}
document.querySelectorAll('.karar').forEach(b=>b.onclick=()=>{const id=Q[i].id; koc[id]=koc[id]||{}; koc[id].v=b.dataset.v;
  document.querySelectorAll('.karar').forEach(x=>x.setAttribute('aria-pressed',String(x===b))); kaydetKoc()});
$('kocNot').oninput=e=>{const id=Q[i].id; koc[id]=koc[id]||{}; koc[id].n=e.target.value; kaydetKoc()};
$('kopyala').onclick=async()=>{const ad={onay:'ONAY',duzelt:'DÜZELT',at:'AT'};
  const t='Pilot parti 1 kararları:\n'+Q.map((q,k)=>{const c=koc[q.id]||{};return `${k+1}. ${q.id}: ${c.v?ad[c.v]:'—'}${c.n?' — '+c.n:''}`}).join('\n');
  const b=$('kopyala'); try{await navigator.clipboard.writeText(t);b.textContent='Kopyalandı'}catch(e){b.textContent='Kopyalanamadı'} setTimeout(()=>b.textContent='Kararları kopyala',2000)};
goster();
</script></body></html>'''
html=html.replace('__DATA__',data)
open(__import__('sys').argv[2],'w').write(html); print(len(html))
