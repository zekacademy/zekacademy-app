import sys,os,json
HD=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,os.path.join(HD,'..'))
from ortak import *
import gorsel as G
from fractions import Fraction as Fr
def fm(x):
    x=Fr(x).limit_denominator(10**6); n=x<0; x=abs(x)
    if x.denominator==1: s=str(x.numerator)
    else:
        d=x.denominator
        while d%2==0: d//=2
        while d%5==0: d//=5
        assert d==1,'ondalik degil'
        s=f'{float(x):.6f}'.rstrip('0').rstrip('.').replace('.',',')
    return ('−' if n else '')+s
KARTLAR=[]; KONU=''
def kart(id,alt,fikir,tuzak,zorluk,kalip,adim,tipId,tip,kaynak):
    KARTLAR.append(dict(id=id,konu=KONU,alt=alt,fikir=fikir,tuzak=tuzak,zorluk=zorluk,kalip=kalip,adim=adim,tipId=tipId,tip=tip,kaynak=kaynak))
def mk(P,no,metin=None,dogru=None,yan=None,istenen=None,ad=None,sekil=None,sira=None,ip=None,bilgi=None,puf=None,kisa=None,
       tipId=None,tip=None,z=None,alt=None,kaz=None,kalip=None,adim=None,kart=None):
    vals=[dogru]+[y[0] for y in yan]; assert len(vals)==5 and len(ip)==1
    if all(not isinstance(v,str) for v in vals):
        fv=[Fr(v).limit_denominator(10**6) for v in vals]; assert len(set(fv))==5
        order=sorted(range(5),key=lambda i:fv[i]); siklar=[fm(vals[i]) for i in order]
        pos={i:'ABCDE'[j] for j,i in enumerate(order)}
    else:
        assert sira and sorted(sira)==sorted(vals) and len(set(sira))==5,(sira,vals)
        siklar=list(sira); pos={i:'ABCDE'[sira.index(vals[i])] for i in range(5)}
    sik=pos[0]
    cel={pos[i+1]:y[1] for i,y in enumerate(yan)}; tur={pos[i+1]:y[2] for i,y in enumerate(yan)}
    P.R(no,tipId,tip,z,alt,kaz,kalip,adim,kart,metin,siklar,sik,istenen,ip,bilgi,ad,puf,cel,tur,kisa=kisa,sekil=sekil)
def bitir(P,onek,k):
    HV=os.path.join(HD,'..')
    for q in P.ANA: q['kardes']=None
    P.yaz(os.path.join(HD,f'{onek}-1.json'),f'/tmp/bos-{onek}.json')
    tipler={}
    for c in KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=k))['kartlar'].append(c['id'])
    json.dump(dict(konu=P.konu_adi,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 TYT Kimya çıkmış soruları, MEB 9–10. sınıf müfredatı.',kartlar=KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar',f'{onek}.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler))
def T(x,y,s,**k): return G._t(x,y,s,**k)
def svg(w,h,body): return G._svg(w,h,body)
def L(x1,y1,x2,y2,w=1.6,extra=''): return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke-width="{w}" {extra}/>'
def Rc(x,y,w,h,fill=0.0,sw=2,acc=False):
    st=f'style="fill:currentColor;fill-opacity:{fill}"' if not acc else f'style="fill:{G.ACC};fill-opacity:{fill};stroke:{G.ACC}"'
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" stroke-width="{sw}" {st}/>'
def ok(x1,y1,x2,y2,renk=None,w=2):
    import math
    a=math.atan2(y2-y1,x2-x1); s=renk or 'currentColor'
    p1=(x2-8*math.cos(a-0.4),y2-8*math.sin(a-0.4)); p2=(x2-8*math.cos(a+0.4),y2-8*math.sin(a+0.4))
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke-width="{w}" style="stroke:{s}"/><path d="M{x2:.1f} {y2:.1f} L{p1[0]:.1f} {p1[1]:.1f} M{x2:.1f} {y2:.1f} L{p2[0]:.1f} {p2[1]:.1f}" stroke-width="{w}" style="stroke:{s}"/>'

# ---- kimya yardımcıları ----
def _fark(isim,x,acik,dogru_mu):
    return acik
def onc(durum,secenekler):
    """durum: {'I':(bool,açıklama)}; secenekler: etiket demetleri listesi (5 adet). Tam bir seçenek doğru kümeye eşit olmalı."""
    T=frozenset(k for k,v in durum.items() if v[0])
    ad=lambda s: ('Yalnız '+s[0]) if len(s)==1 else (' ve '.join(s) if len(s)==2 else ', '.join(s[:-1])+' ve '+s[-1])
    ops=[tuple(s) for s in secenekler]; assert len(ops)==5 and len(set(ops))==5
    eş=[o for o in ops if frozenset(o)==T]; assert len(eş)==1,(T,ops)
    sira=[ad(o) for o in ops]; yan=[]
    for o in ops:
        if frozenset(o)==T: continue
        W=frozenset(o); p=[]
        for x in sorted(W-T): p.append(f'{x} öncülünü doğru sanmış; oysa {durum[x][1]}')
        for x in sorted(T-W): p.append(f'{x} öncülünü yanlış sanmış; oysa {durum[x][1]}')
        yan.append((ad(o),'. '.join(p)+'.' ,'bilgi'))
    return dict(dogru=ad(eş[0]),yan=yan,sira=sira)
def tek(secenekler,hedef=True,tur='bilgi'):
    """secenekler: [(metin,bool,neden)] 5 adet; hedef=True: tek doğru ifade aranır, False: tek yanlış ifade aranır."""
    assert len(secenekler)==5
    h=[s for s in secenekler if s[1]==hedef]; assert len(h)==1,[s[0] for s in h]
    yan=[]
    for m,b,n in secenekler:
        if b==hedef: continue
        yan.append((m,(f'Bu ifadeyi doğru sanmış; oysa {n}' if hedef else f'Bu ifadeyi yanlış sanmış; oysa doğrudur: {n}'),tur))
    return dict(dogru=h[0][0],yan=yan,sira=[s[0] for s in secenekler])
def etk(durum):
    return ' · '.join(f'{k}: '+('doğru' if v[0] else 'yanlış') for k,v in durum.items())
def kab(Z):
    """Z<=20 için katman elektron dizilimi."""
    k=[];r=Z
    for c in (2,8,8,2):
        t=min(r,c);
        if t>0:k.append(t);r-=t
    assert r==0; return k
def sembol(Z): return ['','H','He','Li','Be','B','C','N','O','F','Ne','Na','Mg','Al','Si','P','S','Cl','Ar','K','Ca'][Z]
def yer(Z):
    k=kab(Z); return len(k),k[-1]   # periyot, değerlik (A grubu)
