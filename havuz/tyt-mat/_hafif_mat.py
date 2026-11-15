"""TYT Matematik hafif mod yardımcısı (tyt-fiz/_hafif.py kopyası): kardeş yok, ipucu 1, sayısal şıklar küçükten büyüğe sıralanır.
Kullanım: P=Parti(onek,konu,k); kart(...); mk(P,no,...); bitir(P,onek,k) → tyt-mat/<onek>-1.json + kartlar/<onek>.json"""
import sys,os,json
HD=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,os.path.join(HD,'..'))
from ortak import *
import gorsel as G
try:
    from cizim import tikz_svg   # TikZ ile şekil (bkz. havuz/URETIM-SEKIL.md)
except Exception:
    tikz_svg=None
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
    json.dump(dict(konu=P.konu_adi,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 TYT Matematik çıkmış soruları ve yayın soru bankaları (yalnız mantık), MEB 9–10. sınıf müfredatı.',kartlar=KARTLAR,tipler=list(tipler.values())),
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
def tablo_svg(bas,sat):
    """Basit tablo SVG'si (sekil alanı için). bas: başlık listesi; sat: satır listeleri (hücreler metin). Sütun genişliği içeriğe göre."""
    n=len(bas); assert all(len(r)==n for r in sat)
    gen=[max(54,8*max(len(str(x)) for x in [bas[j]]+[r[j] for r in sat])+18) for j in range(n)]
    W=sum(gen)+4; assert W<=640,'tablo çok geniş'; h=26; Hh=h*(len(sat)+1)+4; b=[]; xs=[2]
    for g in gen: xs.append(xs[-1]+g)
    b.append(f'<rect x="2" y="2" width="{W-4}" height="{h}" style="fill:currentColor;stroke:none" fill-opacity=".08"/>')
    for j,s in enumerate(bas): b.append(G._t((xs[j]+xs[j+1])/2,2+h/2+4,str(s),size=11,bold=True))
    for i,row in enumerate(sat):
        y=2+h*(i+1)
        for j,s in enumerate(row): b.append(G._t((xs[j]+xs[j+1])/2,y+h/2+4,str(s),size=11,bold=(j==0)))
    for i in range(len(sat)+2): b.append(f'<line x1="2" y1="{2+h*i}" x2="{W-2}" y2="{2+h*i}" stroke-width="{1.4 if i in (0,1,len(sat)+1) else 1}"/>')
    for x in xs: b.append(f'<line x1="{x}" y1="2" x2="{x}" y2="{2+h*(len(sat)+1)}" stroke-width="1"/>')
    return G._svg(W,Hh,''.join(b))
