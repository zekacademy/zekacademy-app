"""TYT Kimya üretim yardımcıları (tyt-kim klasörü)."""
import sys,os,json,re
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,os.path.join(H,'..'))
from ortak import *
from collections import Counter
KAYNAK='ÖSYM 2018–2026 TYT Kimya soru dağılımı · MEB 9–10. sınıf kimya'
TUR={'b':'bilgi','i':'islem','d':'dikkat'}
def _nk(t):
    m=re.match(r'^([−-]?\d+(?:,\d+)?)(.*)$',t.strip())
    if not m: return None
    return Fr(m.group(1).replace('−','-').replace(',','.')),m.group(2)
def _opts(d,y,pos='C',sira=None):
    o=[(d,None,None)]+[(t,c,TUR[u]) for t,c,u in y]; assert len(o)==5 and len({x[0] for x in o})==5,[x[0] for x in o]
    ks=[_nk(x[0]) for x in o]
    if sira:
        assert sorted(sira)==sorted(x[0] for x in o),(sira,[x[0] for x in o]); m={x[0]:x for x in o}; o=[m[t] for t in sira]
    elif all(k is not None for k in ks) and len({k[1] for k in ks})==1:
        o=[x for _,x in sorted(zip([k[0] for k in ks],o),key=lambda z:z[0])]
    else:
        idx='ABCDE'.index(pos); rest=o[1:]; o=rest[:idx]+[o[0]]+rest[idx:]
    L='ABCDE'; sik=[L[i] for i,x in enumerate(o) if x[1] is None]; assert len(sik)==1
    return [x[0] for x in o],sik[0],{L[i]:x[1] for i,x in enumerate(o) if x[1] is not None},{L[i]:x[2] for i,x in enumerate(o) if x[1] is not None}
class Kim:
    def __init__(s,onek,konu,uyg,pre):
        s.P=Parti(onek,konu,uyg,ders='TYT Kimya',idon='tytkim'); s.onek=onek; s.konu=konu; s.uyg=uyg; s.pre=pre; s.KART=[]
    def Q(s,no,tipId,tip,zor,alt,kaz,kalip,adim,fikir,tuzak,bilgi,puf,a,k,ozet,degisti,_x=None,kisa=None):
        kid=f'K-{s.pre}-{int(no):02d}'
        s.KART.append(dict(id=kid,konu=s.konu,alt=alt,fikir=fikir,tuzak=tuzak,zorluk=zor,kalip=kalip,adim=adim,tipId=tipId,tip=tip,kaynak=KAYNAK))
        sz,c,cel,tur=_opts(a['d'],a['y'],a.get('pos','C'),a.get('sira'))
        s.P.R(no,tipId,tip,zor,alt,kaz,kalip,adim,f'{kid} ({ozet}) · {degisti}',a['m'],sz,c,a['i'],a['ip'],bilgi,a['ad'],puf,cel,tur,kisa=kisa,sekil=a.get('sekil'))
        sz,c,cel,tur=_opts(k['d'],k['y'],k.get('pos','C'),k.get('sira'))
        s.P.K(no,k['m'],sz,c,k.get('i',a['i']),k.get('ip',a['ip']),k.get('bilgi',bilgi),k['ad'],k.get('puf',puf),cel,tur,kisa=k.get('kisa',kisa),sekil=k.get('sekil'))
    def bitir(s,n_ana):
        P=s.P; assert len(P.ANA)==n_ana==len(P.KAR),(len(P.ANA),len(P.KAR))
        tipler={}
        for k in s.KART: tipler.setdefault(k['tipId'],dict(tipId=k['tipId'],ad=k['tip'],kartlar=[],uygulamaKonu=s.uyg))['kartlar'].append(k['id'])
        json.dump(dict(konu=s.konu,surum=1,not_='Kart = fikir; soru metni içermez.',kartlar=s.KART,tipler=list(tipler.values())),open(os.path.join(H,'..','kartlar',s.onek+'.json'),'w'),ensure_ascii=False,indent=1)
        P.yaz(os.path.join(H,s.onek+'-1.json'),os.path.join(H,s.onek+'-1-kardes.json'))
        print('zorluk',dict(Counter(q['zorluk'] for q in P.ANA)),'tipler',len(tipler))
def mol(g,M): return Fr(g)/Fr(M)
def fs(x):
    """Fraction/sayı → Türkçe ondalık metin"""
    x=Fr(x); n=x<0; x=abs(x)
    if x.denominator==1: s=str(x.numerator)
    else:
        d=x.denominator
        while d%2==0: d//=2
        while d%5==0: d//=5
        assert d==1,'ondalık değil'
        s=f'{float(x):.6f}'.rstrip('0').rstrip('.').replace('.',',')
    return ('−' if n else '')+s
