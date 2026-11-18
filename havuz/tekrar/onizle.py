import json,html,re,sys
from collections import Counter
S=sys.argv[1]; src=open(sys.argv[2]).read()
css=src[src.index('<style>')+7:src.index('</style>')]
C=json.load(open('tekrar/kartlar.json'))
ders={'mat':'Matematik','prob':'Problemler','matd':'Kümeler · Olasılık · Veri','geo':'Geometri','fiz':'Fizik','kim':'Kimya','bio':'Biyoloji'}
def md(s): return re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',html.escape(s or ''))
N=Counter(v for v in json.load(open('tekrar/soru-kart.json')).values() if v)
P=[]
for c in C:
    p,konu=c['k'].split('|',1)
    fig=f'<figure>{c["sekil"]}</figure>' if c.get('sekil') else ''
    fo=f'<div class="formula">{html.escape(c["formul"])}</div>' if c.get('formul') else ''
    ad=''.join(f'<li><span>{md(a)}</span></li>' for a in c['ornek']['adimlar'])
    P.append(f'''<article class="phone" data-d="{p}"><div class="top"><span class="crumb">TYT {ders.get(p,p)} · {html.escape(konu)} · {N[c['id']]} soru</span><h2>{html.escape(c['baslik'])}</h2></div><div class="body">
<section class="block why"><span class="label">Bu soru neyi ölçüyordu?</span><p>{md(c['olcer'])}</p></section>
<section class="block rule"><span class="label">Temel kural</span>{fig}{fo}<p>{md(c['kural'])}</p></section>
<section class="ex"><span class="label">Mini örnek · çözümlü</span><p class="q">{md(c['ornek']['soru'])}</p><ol class="steps">{ad}<li><span><b>Cevap:</b> {md(c['ornek']['cevap'])}</span></li></ol></section>
<section class="block trap"><span class="label">Sık yapılan hata</span><p>{md(c['hata'])}</p></section>
<section class="block memo"><span class="label">Aklında kalsın</span><p>“{html.escape(c['akilda'])}”</p></section></div></article>''')
opts=''.join(f'<option value="{k}">{v} ({sum(1 for c in C if c["k"].startswith(k+"|"))})</option>' for k,v in ders.items())
page=f'''<title>Konu Tekrarı Kartları</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Lexend:wght@400;500;600;700&family=JetBrains+Mono:wght@500&display=swap">
<style>{css}
.bar{{display:flex;flex-wrap:wrap;gap:10px;align-items:center}}
select{{font:inherit;padding:8px 12px;border-radius:10px;border:1px solid var(--line);background:var(--card);color:var(--ink)}}
.phone figure svg{{max-width:300px}}
</style>
<div class="wrap" style="max-width:1100px">
<header><h1>Konu Tekrarı Kartları</h1><p>TYT Matematik, Geometri ve Fen için {len(C)} kart. Havuzdaki her soru bu kartlardan birine bağlı; öğrenci yanlış yaptığı sorunun çözümüne bakınca ilgili kart açılır.</p>
<div class="bar"><label for="ders">Ders:</label><select id="ders">{opts}</select></div></header>
<div class="phones" id="liste">{''.join(P)}</div></div>
<script>
const s=document.getElementById('ders');
function f(){{document.querySelectorAll('#liste .phone').forEach(e=>e.hidden=e.dataset.d!==s.value)}}
s.addEventListener('change',f);f();
</script>'''
open(S,'w').write(page);print(len(page)//1024,'KB')
