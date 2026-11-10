"""TYT Coğrafya hafif mod yardımcıları (iklim, atmosfer, rüzgâr, nem, su-toprak-bitki, dünya hareketleri).
Her şıkka etiket, tek doğru şık assert; öncüllü sorularda şıklar ifade doğruluğundan hesaplanır; SVG çizimleri."""
import sys,os,json,math
HD=os.path.dirname(os.path.abspath(__file__)); HAVUZ=os.path.join(HD,'..')
sys.path.insert(0,HAVUZ)
from ortak import *
import gorsel as G
from collections import Counter
ROM=['I','II','III','IV']
class Konu:
    def __init__(s,onek,konu_adi,k,n,kartlar,tipler,zdagilim):
        s.P=Parti(onek,konu_adi,k,ders='TYT Coğrafya',idon='tytcog'); s.onek=onek; s.konu_adi=konu_adi; s.k=k; s.n=n
        s.kartlar=kartlar; s.tipler=tipler; s.zd=zdagilim
        for kid,c in kartlar.items(): assert c['tipId'] in tipler
    def _yaz(s,no,kart,zor,kazanim,adim,kalip,metin,siklar,harf,istenen,ip,bilgi,adimlar,puf,cel,tur,sekil=None,kisa=None):
        c=s.kartlar[kart]; assert isinstance(ip,str) and 3<=len(adimlar)<=7
        s.P.R(no,c['tipId'],s.tipler[c['tipId']],zor,c['alt'],kazanim,kalip,adim,f"{kart} ({c['alt']}) · özgün kurgu",metin,siklar,harf,istenen,[ip],bilgi,adimlar,puf,cel,tur,kisa=kisa,sekil=sekil)
    def soru(s,no,kart,zor,kazanim,adim,kalip,metin,opts,harf,pred,istenen,ip,bilgi,adimlar,puf,sekil=None):
        """opts: A–E sırasıyla 5 adet (şık metni, etiket, cel, tur). pred(etiket) tam bir şık için doğru olmalı ve o şık harf olmalı."""
        assert len(opts)==5
        ok=[i for i,o in enumerate(opts) if pred(o[1])]
        assert len(ok)==1 and 'ABCDE'[ok[0]]==harf,(no,ok,harf)
        assert len({o[0] for o in opts})==5,no
        cel={};tur={}
        for i,o in enumerate(opts):
            if i==ok[0]: continue
            assert o[2] and len(o[2])>=12 and o[3] in TURLER,(no,o[0]); cel['ABCDE'[i]]=o[2]; tur['ABCDE'[i]]=o[3]
        s._yaz(no,kart,zor,kazanim,adim,kalip,metin,[o[0] for o in opts],harf,istenen,ip,bilgi,adimlar,puf,cel,tur,sekil)
    def oncul(s,no,kart,zor,kazanim,adim,giris,stmts,kok,secenekler,harf,dogru_mu,istenen,ip,bilgi,adimlar,puf,sekil=None):
        """stmts: (metin, doğru_mu, gerekçe). dogru_mu=True: kök 'doğru olanlar'; False: 'yanlış olanlar'. secenekler: 5 şık metni."""
        n=len(stmts); hedef={i for i,x in enumerate(stmts) if x[1]==dogru_mu}
        def ayir(t):
            if t.startswith('Yalnız'): return {ROM.index(t.split()[1])}
            return {ROM.index(x.strip()) for x in t.replace(' ve ',',').split(',')}
        ok=[i for i,t in enumerate(secenekler) if ayir(t)==hedef]
        assert len(ok)==1 and 'ABCDE'[ok[0]]==harf and len(set(secenekler))==5,(no,ok,hedef)
        metin=(giris+'\n' if giris else '')+'\n'.join(f'{ROM[i]}. {x[0]}' for i,x in enumerate(stmts))+'\n'+kok
        cel={};tur={}
        for i,t in enumerate(secenekler):
            if i==ok[0]: continue
            S=ayir(t); p=[]
            for j in sorted(S-hedef): p.append(f'{ROM[j]}. ifade koşulu sağlamaz: {stmts[j][2]}')
            for j in sorted(hedef-S): p.append(f'{ROM[j]}. ifade de koşulu sağlar ama seçenekte yok: {stmts[j][2]}')
            cel['ABCDE'[i]]=' '.join(p); tur['ABCDE'[i]]='bilgi' if S-hedef else 'dikkat'
        s._yaz(no,kart,zor,kazanim,adim,'öncüllü',metin,secenekler,harf,istenen,ip,bilgi,adimlar,puf,cel,tur,sekil)
    def bitir(s):
        for q in s.P.ANA: q['kardes']=None
        assert len(s.P.ANA)==s.n,(len(s.P.ANA),s.n)
        z=Counter(q['zorluk'] for q in s.P.ANA); assert dict(z)==s.zd,(dict(z),s.zd)
        used={q['tipId'] for q in s.P.ANA}; assert used==set(s.tipler),'her tip en az 1 soru'
        kl=[dict(id=kid,konu=s.konu_adi,alt=c['alt'],fikir=c['fikir'],tuzak=c['tuzak'],zorluk=c['zorluk'],kalip=c['kalip'],adim=c['adim'],tipId=c['tipId'],tip=s.tipler[c['tipId']],kaynak=c['kaynak']) for kid,c in s.kartlar.items()]
        tl=[dict(tipId=t,ad=ad,kartlar=[k for k,c in s.kartlar.items() if c['tipId']==t],uygulamaKonu=s.k) for t,ad in s.tipler.items()]
        json.dump(dict(konu=s.konu_adi,surum=1,kartlar=kl,tipler=tl),open(f'{HAVUZ}/kartlar/{s.onek}.json','w'),ensure_ascii=False,indent=1)
        s.P.yaz(f'{HD}/{s.onek}-1.json',f'/tmp/bos-{s.onek}.json')
        open(f'{HD}/{s.onek}-1.HAZIR','w').close()
# ---------- SVG ----------
AYLAR=['Oca','Şub','Mar','Nis','May','Haz','Tem','Ağu','Eyl','Eki','Kas','Ara']
def klimograf(T,P,tmax=30,tstep=10,pmax=300,pstep=100):
    """Aylık sıcaklık (çizgi, sol eksen °C) ve yağış (sütun, sağ eksen mm)."""
    assert len(T)==len(P)==12
    W,H_,x0,x1,y0,y1=340,230,38,302,24,176; d=(x1-x0)/12
    b=[G._t(x0-4,14,'°C',anchor='end',size=10),G._t(x1+4,14,'mm',anchor='start',size=10)]
    t=0
    while t<=tmax:
        y=y1-(y1-y0)*t/tmax; b.append(f'<line x1="{x0}" y1="{y:.1f}" x2="{x1}" y2="{y:.1f}" stroke-width=".6" opacity=".25"/>'); b.append(G._t(x0-5,y+4,str(t),anchor='end',size=10)); t+=tstep
    p=0
    while p<=pmax:
        y=y1-(y1-y0)*p/pmax; b.append(G._t(x1+5,y+4,str(p),anchor='start',size=10)); p+=pstep
    pts=[]
    for i in range(12):
        cx=x0+d*(i+.5); h=(y1-y0)*P[i]/pmax
        b.append(f'<rect x="{cx-d*.32:.1f}" y="{y1-h:.1f}" width="{d*.64:.1f}" height="{h:.1f}" stroke-width="1" style="fill:currentColor;fill-opacity:.22"/>')
        b.append(G._t(cx,y1+13,AYLAR[i],size=8.5)); pts.append((cx,y1-(y1-y0)*T[i]/tmax))
    b.append(f'<line x1="{x0}" y1="{y1}" x2="{x1}" y2="{y1}" stroke-width="1.5"/><line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y1}" stroke-width="1.5"/><line x1="{x1}" y1="{y0}" x2="{x1}" y2="{y1}" stroke-width="1.5"/>')
    b.append('<polyline points="'+' '.join(f'{x:.1f},{y:.1f}' for x,y in pts)+f'" stroke-width="2.4" style="stroke:{G.ACC}"/>')
    for x,y in pts: b.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.6" style="fill:{G.ACC};stroke:none"/>')
    b.append(f'<line x1="{x0+10}" y1="{H_-14}" x2="{x0+34}" y2="{H_-14}" stroke-width="2.4" style="stroke:{G.ACC}"/>'+G._t(x0+40,H_-10,'Sıcaklık',anchor='start',size=10))
    b.append(f'<rect x="{x0+112}" y="{H_-21}" width="14" height="10" stroke-width="1" style="fill:currentColor;fill-opacity:.22"/>'+G._t(x0+132,H_-10,'Yağış',anchor='start',size=10))
    return G._svg(W,H_,''.join(b))
def cubuk(V,vmax,vstep,birim,renk_ay=None):
    W,H_,x0,x1,y0,y1=340,210,44,320,22,170; d=(x1-x0)/12
    b=[G._t(x0-4,14,birim,anchor='end',size=10)]
    v=0
    while v<=vmax:
        y=y1-(y1-y0)*v/vmax; b.append(f'<line x1="{x0}" y1="{y:.1f}" x2="{x1}" y2="{y:.1f}" stroke-width=".6" opacity=".25"/>'+G._t(x0-5,y+4,str(v),anchor='end',size=10)); v+=vstep
    for i in range(12):
        cx=x0+d*(i+.5); h=(y1-y0)*V[i]/vmax
        b.append(f'<rect x="{cx-d*.32:.1f}" y="{y1-h:.1f}" width="{d*.64:.1f}" height="{h:.1f}" stroke-width="1" style="fill:{G.ACC};fill-opacity:.55"/>'+G._t(cx,y1+13,AYLAR[i],size=8.5))
    b.append(f'<line x1="{x0}" y1="{y1}" x2="{x1}" y2="{y1}" stroke-width="1.5"/><line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y1}" stroke-width="1.5"/>')
    return G._svg(W,H_,''.join(b))
