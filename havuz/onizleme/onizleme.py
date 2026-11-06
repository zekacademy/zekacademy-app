import json,html,re
Q=json.load(open(__import__('sys').argv[1]))
def kesir(e): return re.sub(r'(?<![\d/])(\d+)/(\d+)(?![\d/])',r'<span class="kesir"><span>\1</span><span>\2</span></span>',e)
def metin_html(t):
    sat=t.split('\n'); out=[]
    for k,x in enumerate(sat):
        e=html.escape(x)
        e=re.sub(r' ([+−×÷=<>≤≥]) ','\u00a0\\1\u00a0',e)
        kok=k>=len(sat)-2 and re.match(r'(Buna göre|.*olduğuna göre|.*hangisi|.*kaçtır|ifadelerinden)',x)
        madde=re.match(r'\s*(•|[IVX]+\.)',x)
        formul=(not kok and not madde and re.search(r'[=<>≤≥□]',x) and len(x)<40 and not re.search(r'[a-zçğıöşü]{6,}',x))
        e=kesir(e)
        if not kok and x.strip().startswith('Buna göre') and len(x)<14: kok=True
        cls='kok' if kok else 'madde' if madde else 'formul' if formul else ''
        out.append(f'<p class="{cls}">{e}</p>')
    return ''.join(out)
def md(s): return re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',html.escape(s))
cards=[]
for i,q in enumerate(Q,1):
    ch=''.join(f'<li data-k="{k}" class="{"ok" if k==q["cevap"]["sik"] else ""}"><span class="h">{k})</span> {kesir(html.escape(v))}</li>' for k,v in q['siklar'].items())
    L=max(len(v) for v in q['siklar'].values()); duzen='sira' if L<=7 else ('osym' if L<=20 else 'alt')
    st=''.join(f'<li><div class="ab">{html.escape(a["baslik"])}</div><div class="aa">{kesir(md(a["aciklama"]))}</div><div class="ai">{kesir(html.escape(a["islem"]))}</div></li>' for a in q['adimlar'])
    ip=''.join(f'<li>{html.escape(x)}</li>' for x in q['ipuclari'])
    bi=''.join(f'<span class="bil"><b>{html.escape(b["ad"])}</b>{html.escape(b["ifade"])}</span>' for b in q['bilgi'])
    cards.append(f'''<article class="card" id="q{i}">
<header><span class="no">{i}</span><span class="tag">{html.escape(q["konu"])}</span><span class="tag z-{q["zorluk"]}">{q["zorluk"]}</span><span class="tag">{q["kalip"]}</span><span class="tag">{q["adimSayisi"]} adım</span></header>
<div class="metin">{metin_html(q["metin"])}</div>
{f'<div class="sekil">{q["sekil"]}</div>' if q["sekil"] else ''}
<ol class="siklar {duzen}">{ch}</ol>
<details><summary>Çözümü göster</summary>
<div class="coz">
<div class="ist"><span>Ne isteniyor?</span>{html.escape(q["istenen"])}</div>
{f'<div class="bilgiler">{bi}</div>' if bi else ''}
<ol class="yol">{st}</ol>
<div class="cvp"><span>Cevap</span><b>{q["cevap"]["sik"]})</b> {kesir(html.escape(q["cevap"]["deger"]))}</div>
<div class="puf"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 18h6M10 21h4M12 3a6 6 0 0 0-3.6 10.8c.6.5 1 1.2 1 2V16h5.2v-.2c0-.8.4-1.5 1-2A6 6 0 0 0 12 3z"/></svg><div><b>Püf noktası</b>{html.escape(q["puf"])}</div></div>
<details class="ipd"><summary>İpuçlarına bak</summary><ol class="ipl">{ip}</ol></details>
<p class="kart">{html.escape(q["kaynakKart"])}</p>
</div></details>
<div class="karar"><button data-v="onay">✓ Onay</button><button data-v="duzelt">✎ Düzeltilsin</button><button data-v="at">✕ At</button>
<textarea placeholder="Not (isteğe bağlı)"></textarea></div></article>''')
page=f'''<!DOCTYPE html><html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Soru Havuzu · Pilot Parti 1 · Sayı Kümeleri</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
:root{{--bg:#f6f7f5;--fg:#1d2420;--mut:#5d6b63;--card:#fff;--line:#dfe4e0;--acc:#1f8a5b;--accbg:#e6f4ec}}
:root[data-tema=koyu]{{--bg:#121614;--fg:#e8ece9;--mut:#9aa8a0;--card:#1b211e;--line:#2c3631;--acc:#4cc38a;--accbg:#18382a}}
.bas{{display:flex;align-items:flex-start;gap:12px}}.bas h1{{flex:1}}
.tema{{flex:none;display:flex;border:1.5px solid var(--line);border-radius:999px;padding:3px;background:var(--card);margin-top:4px}}
.tema button{{border:0;background:none;color:var(--mut);font:600 13px "Plus Jakarta Sans",system-ui,sans-serif;padding:6px 12px;border-radius:999px;cursor:pointer}}
.tema button[aria-pressed=true]{{background:var(--fg);color:var(--card)}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--fg);font:500 16px/1.55 "Plus Jakarta Sans",system-ui,sans-serif}}
main{{max-width:760px;margin:0 auto;padding:20px 14px 80px}}h1{{font-size:1.35rem;margin:.2em 0}}.lead{{color:var(--mut);margin:0 0 18px}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:16px;margin:0 0 16px}}
header{{display:flex;flex-wrap:wrap;gap:6px;align-items:center;margin-bottom:10px}}.no{{background:var(--acc);color:#fff;border-radius:8px;padding:0 9px;font-weight:700}}
.tag{{font-size:.78rem;border:1px solid var(--line);border-radius:999px;padding:1px 9px;color:var(--mut)}}.z-zor{{color:#c0392b}}.z-orta{{color:#b7791f}}.z-kolay{{color:var(--acc)}}
.metin{{margin:14px 2px 6px;font:500 17px/1.6 "Plus Jakarta Sans",system-ui,sans-serif;max-width:36em}}
.metin p{{margin:0 0 .85em}}.metin p.kok{{font-weight:700;margin-top:1.1em}}
.metin p.madde{{margin:0 0 .35em;padding-left:1.4em}}.metin p.formul{{text-align:center;margin:.9em 0;white-space:nowrap}}.sekil{{color:var(--fg);max-width:420px;margin:6px 0}}.sekil svg{{width:100%;height:auto}}
.siklar{{list-style:none;padding:0;margin:14px 2px 6px;font:500 17px/1.5 "Plus Jakarta Sans",system-ui,sans-serif}}
.siklar .h{{font-weight:700;margin-right:.25em}}.siklar li{{border-radius:6px;padding:2px 4px}}
.siklar.sira{{display:flex;flex-wrap:wrap;column-gap:1.6em;row-gap:.5em}}
.siklar.osym{{display:grid;grid-template-columns:1fr 1fr;row-gap:.6em;column-gap:1.2em}}
.siklar.osym li[data-k=C]{{grid-column:1 / span 2;justify-self:center}}.siklar.osym li[data-k=D]{{grid-row:3}}
.siklar.alt{{display:grid;row-gap:.5em}}
details[open] ~ * .x,details[open]{{}} .card.acik .siklar li.ok{{background:var(--accbg);box-shadow:inset 0 0 0 1.5px var(--acc)}}
summary{{cursor:pointer;color:var(--acc);font-weight:600;margin:8px 0}}.adim{{padding-left:20px}}.adim li{{margin:0 0 10px}}.sb{{font-weight:700}}
code{{display:inline-block;background:var(--bg);border-radius:6px;padding:2px 8px;margin-top:3px;font-size:.92rem}}
.puf{{background:var(--accbg);border-radius:10px;padding:8px 10px}}.kart{{color:var(--mut);font-size:.82rem}}.bil{{font-size:.9rem;color:var(--mut)}}
.karar{{display:flex;flex-wrap:wrap;gap:8px;margin-top:10px;border-top:1px dashed var(--line);padding-top:10px}}
.karar button{{border:1px solid var(--line);background:var(--bg);color:var(--fg);border-radius:9px;padding:6px 12px;font:inherit;cursor:pointer}}
.karar button.sec[data-v=onay]{{background:var(--acc);color:#fff;border-color:var(--acc)}}.karar button.sec[data-v=duzelt]{{background:#b7791f;color:#fff}}.karar button.sec[data-v=at]{{background:#c0392b;color:#fff}}
textarea{{flex:1 1 100%;min-height:38px;border:1px solid var(--line);border-radius:9px;background:var(--bg);color:var(--fg);font:inherit;padding:6px 9px}}
.alt{{position:sticky;bottom:0;background:var(--card);border:1px solid var(--line);border-radius:14px;padding:10px 14px;display:flex;gap:10px;align-items:center;justify-content:space-between}}
.alt button{{background:var(--acc);color:#fff;border:0;border-radius:9px;padding:8px 14px;font:inherit;font-weight:600;cursor:pointer}}

.kesir{{display:inline-flex;flex-direction:column;vertical-align:middle;text-align:center;font-size:.86em;line-height:1.15;margin:0 .12em}}
.kesir span:first-child{{border-bottom:1.2px solid currentColor;padding:0 .15em}}
.coz{{margin-top:6px}}
.ist{{background:var(--accbg);border-radius:14px;padding:12px 14px;font-size:15px;line-height:1.45}}
.ist span{{display:block;font-weight:700;color:var(--acc);font-size:13px;margin-bottom:2px}}
.bilgiler{{display:flex;flex-wrap:wrap;gap:8px;margin:12px 0 0}}
.bil{{border:1.5px solid var(--line);border-radius:12px;padding:6px 10px;font-size:14px;color:var(--fg)}}
.bil b{{display:block;font-size:12px;color:var(--mut);font-weight:600}}
.yol{{list-style:none;margin:18px 0 0;padding:0;counter-reset:y}}
.yol li{{position:relative;padding:0 0 20px 46px;counter-increment:y}}
.yol li::before{{content:counter(y);position:absolute;left:0;top:-2px;width:32px;height:32px;border-radius:50%;background:var(--acc);color:#fff;display:grid;place-items:center;font-weight:800;font-size:15px}}
.yol li::after{{content:"";position:absolute;left:15.5px;top:34px;bottom:2px;width:2px;background:repeating-linear-gradient(var(--acc) 0 4px,transparent 4px 8px);opacity:.45}}
.yol li:last-child::after{{display:none}}
.ab{{font-weight:800;font-size:16px;line-height:1.3}}
.aa{{color:var(--mut);font-size:15px;margin-top:2px;line-height:1.45}}.aa b{{color:var(--fg)}}
.ai{{margin-top:9px;display:inline-block;font:19px/1.4 "Plus Jakarta Sans",system-ui,sans-serif;background:var(--bg);border-radius:10px;padding:8px 14px;border-left:3px solid var(--acc)}}
.cvp{{display:flex;align-items:center;gap:10px;margin:2px 0 14px 0;padding:12px 16px;border-radius:14px;border:2px solid var(--acc);font:20px "Plus Jakarta Sans",system-ui,sans-serif}}
.cvp span{{font:700 13px "Plus Jakarta Sans",system-ui,sans-serif;color:var(--acc);margin-right:4px}}
.puf{{display:flex;gap:12px;align-items:flex-start;background:var(--fg);color:var(--card);border-radius:14px;padding:13px 15px;font-size:15px;line-height:1.45}}
.puf svg{{flex:none;width:22px;height:22px;fill:none;stroke:#F5C04A;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round;margin-top:1px}}
.puf b{{display:block;color:#F5C04A;font-size:13px;margin-bottom:2px}}
.ipd{{margin-top:12px}}.ipd summary{{font-size:14px}}.ipl{{margin:6px 0 0;padding-left:20px;font-size:15px;color:var(--mut)}}.ipl li+li{{margin-top:4px}}
</style></head><body><main>
<div class="bas"><h1>Pilot · Parti 1 — Sayı Kümeleri (12 soru)</h1><div class="tema" role="group" aria-label="Tema"><button data-t="acik" aria-pressed="true">Açık</button><button data-t="koyu" aria-pressed="false">Koyu</button></div></div>
<p class="lead">Her soru kodla doğrulandı (cevap yeniden hesaplandı, gerekenlerde tüm olasılıklar tarandı). Her karta Onay / Düzeltilsin / At işaretle, istersen not yaz; en alttaki düğmeyle kararlarını kopyalayıp sohbete yapıştır.</p>
{''.join(cards)}
<div class="alt"><span id="say">0 / {len(Q)} işaretlendi</span><button id="kop">Kararları kopyala</button></div>
</main><script>
(function(){{let t='acik';try{{t=localStorage.getItem('pilot-tema')||'acik'}}catch(e){{}}
const uygula=x=>{{document.documentElement.dataset.tema=x;document.querySelectorAll('.tema button').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.t===x)));try{{localStorage.setItem('pilot-tema',x)}}catch(e){{}}}};
uygula(t);document.querySelectorAll('.tema button').forEach(b=>b.onclick=()=>uygula(b.dataset.t));}})();
const ids={json.dumps([q['id'] for q in Q])};const st={{}};
let mem={{}};try{{mem=JSON.parse(localStorage.getItem('pilot1')||'{{}}')}}catch(e){{}}
document.querySelectorAll('.card').forEach((c,i)=>{{const d=c.querySelector('details');d.addEventListener('toggle',()=>c.classList.toggle('acik',d.open));
 const ta=c.querySelector('textarea');const bs=c.querySelectorAll('.karar button');
 const set=v=>{{st[i]=st[i]||{{}};st[i].v=v;bs.forEach(b=>b.classList.toggle('sec',b.dataset.v===v));upd()}};
 bs.forEach(b=>b.onclick=()=>set(b.dataset.v));ta.oninput=()=>{{st[i]=st[i]||{{}};st[i].n=ta.value;upd()}};
 if(mem[i]){{if(mem[i].n)ta.value=mem[i].n;st[i]={{n:mem[i].n}};if(mem[i].v)set(mem[i].v)}}}});
function upd(){{document.getElementById('say').textContent=Object.values(st).filter(x=>x.v).length+' / {len(Q)} işaretlendi';try{{localStorage.setItem('pilot1',JSON.stringify(st))}}catch(e){{}}}}
document.getElementById('kop').onclick=async()=>{{const ad={{onay:'ONAY',duzelt:'DÜZELT',at:'AT'}};
 const t='Pilot parti 1 kararları:\\n'+ids.map((id,i)=>`${{i+1}}. ${{id}}: ${{st[i]&&st[i].v?ad[st[i].v]:'—'}}${{st[i]&&st[i].n?' — '+st[i].n:''}}`).join('\\n');
 const b=document.getElementById('kop');try{{await navigator.clipboard.writeText(t);b.textContent='Kopyalandı ✓'}}catch(e){{b.textContent='Kopyalanamadı'}};setTimeout(()=>b.textContent='Kararları kopyala',2000)}};
</script></body></html>'''
open(__import__('sys').argv[2],'w').write(page); print(len(page))
