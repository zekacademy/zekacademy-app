"""Sözel dersler (coğrafya, felsefe) için kompakt soru tanımlama yardımcısı. Parti/ortak.py üzerine kuruludur."""
import sys,os,json,glob
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
from ortak import *
from collections import Counter
import gorsel as G
def _num(t):
    try: return Fr(t.replace('−','-').replace(',','.').strip())
    except Exception: return None
def _opts(o):
    if all(_num(x[0]) is not None for x in o): o=sorted(o,key=lambda x:_num(x[0]))
    L='ABCDE'; assert len(o)==5
    sik=[L[i] for i,x in enumerate(o) if x[1] is None]; assert len(sik)==1,sik
    return [x[0] for x in o],sik[0],{L[i]:x[1] for i,x in enumerate(o) if x[1] is not None},{L[i]:x[2] for i,x in enumerate(o) if x[1] is not None}
def O(L,dogru,yanlis):
    """L: doğru şıkkın harfi; yanlis: 4 adet (metin,cel,tur) – verilen sırayla kalan konumlara yerleşir."""
    assert len(yanlis)==4; y=list(yanlis); o=[]
    for h in 'ABCDE': o.append((dogru,None,None) if h==L else y.pop(0))
    return o
ON=[('Yalnız I',),('Yalnız II',),('Yalnız III',),('I ve II',),('I ve III',),('II ve III',),('I, II ve III',)]
def OC(dogru,cel):
    """Öncüllü şıklar: dogru = 'I ve III' gibi; cel: {şık metni: (açıklama, tür)}; 5 şık = doğru + cel anahtarları (4)."""
    assert len(cel)==4 and dogru not in cel
    sira=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
    tum=[dogru]+list(cel); assert all(t in sira for t in tum),tum
    tum.sort(key=sira.index)
    return [(t,None,None) if t==dogru else (t,cel[t][0],cel[t][1]) for t in tum]
def iklim_grafik(sic,yag,ad=''):
    """12 aylık sıcaklık (çizgi, °C) ve yağış (çubuk, mm) grafiği."""
    W,Hh=330,190; x0,y0,x1,y1=38,20,300,140; ay='OŞMNMHTAESEK'
    ay=['O','Ş','M','N','M','H','T','A','E','E','K','A']
    b=[f'<line x1="{x0}" y1="{y1}" x2="{x1}" y2="{y1}" stroke-width="1.2"/><line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y1}" stroke-width="1.2"/>']
    mx=max(max(yag),1); w=(x1-x0)/12
    for i,v in enumerate(yag):
        h=(y1-y0)*v/(mx*1.0); b.append(f'<rect x="{x0+i*w+3:.1f}" y="{y1-h:.1f}" width="{w-6:.1f}" height="{h:.1f}" stroke-width="1" opacity=".55" style="fill:currentColor"/>')
        b.append(G._t(x0+i*w+w/2,y1+14,ay[i],size=10))
    lo,hi=min(sic)-2,max(sic)+2
    pts=' '.join(f'{x0+i*w+w/2:.1f},{y1-(y1-y0)*(t-lo)/(hi-lo):.1f}' for i,t in enumerate(sic))
    b.append(f'<polyline points="{pts}" stroke-width="2.2" style="stroke:{G.ACC}"/>')
    for i,t in enumerate(sic): b.append(f'<circle cx="{x0+i*w+w/2:.1f}" cy="{y1-(y1-y0)*(t-lo)/(hi-lo):.1f}" r="2.6" style="fill:{G.ACC};stroke:none"/>')
    b.append(G._t(x0-4,y0+4,f'{mx} mm',anchor='end',size=10)); b.append(G._t(x0-4,y1,'0',anchor='end',size=10))
    b.append(G._t(W/2,Hh-8,(ad+' · ' if ad else '')+'çubuk: yağış (mm) · çizgi: sıcaklık (°C)',size=11))
    return G._svg(W,Hh,''.join(b))
def piramit(etiketler,erkek,kadin,ad=''):
    """Yaş grupları (alttan üste) için yüzde çubukları; erkek solda, kadın sağda."""
    W,n=330,len(etiketler); sat=24; Hh=n*sat+50; cx=165; mx=max(max(erkek),max(kadin)); k=110/mx; b=[]
    for i,(e,f,t) in enumerate(zip(erkek,kadin,etiketler)):
        y=Hh-34-(i+1)*sat+3
        b.append(f'<rect x="{cx-e*k:.1f}" y="{y}" width="{e*k:.1f}" height="{sat-6}" stroke-width="1" opacity=".5" style="fill:currentColor"/>')
        b.append(f'<rect x="{cx}" y="{y}" width="{f*k:.1f}" height="{sat-6}" stroke-width="1" style="fill:{G.ACC};opacity:.7"/>')
        b.append(G._t(cx,y+sat-9,t,size=9,renk='currentColor') if False else G._t(8,y+sat-9,t,anchor='start',size=10))
    b.append(f'<line x1="{cx}" y1="6" x2="{cx}" y2="{Hh-34}" stroke-width="1"/>')
    b.append(G._t(cx-55,Hh-18,'Erkek (%)',size=11)); b.append(G._t(cx+55,Hh-18,'Kadın (%)',size=11))
    if ad: b.append(G._t(cx,Hh-4,ad,size=11))
    return G._svg(W,Hh,''.join(b))
class Konu:
    def __init__(s,klasor,onek,konu_adi,uyg,ders,idon,pre,n_ana,kaynak):
        s.klasor=klasor; s.onek=onek; s.P=Parti(onek,konu_adi,uyg,ders=ders,idon=idon); s.pre=pre; s.n=n_ana; s.kart=[]; s.uyg=uyg; s.konu=konu_adi; s.kaynak=kaynak; s.L=[]
    def Q(s,no,tipId,tip,zor,alt,kaz,kalip,adim,fikir,tuzak,bilgi,puf,ip,a,k,degisti='yeni kurgu ve ögeler',ozet=None):
        assert tipId.islower() and len(ip)==3 and len(bilgi)<=3
        kid=f'K-{s.pre}-{int(no):02d}'
        s.kart.append(dict(id=kid,konu=s.konu,alt=alt,fikir=fikir,tuzak=tuzak,zorluk=zor,kalip=kalip,adim=adim,tipId=tipId,tip=tip,kaynak=s.kaynak))
        for d in (a,k):
            for x in d['ad']: assert isinstance(x,dict)
        sk,c,cel,tur=_opts(a['o'])
        s.P.R(no,tipId,tip,zor,alt,kaz,kalip,adim,f'{kid} ({ozet or fikir[:48]}) · {degisti}',a['m'],sk,c,a['i'],ip,bilgi,a['ad'],puf,cel,tur,sekil=a.get('sek'))
        sk2,c2,cel2,tur2=_opts(k['o'])
        s.P.K(no,k['m'],sk2,c2,k.get('i',a['i']),ip,k.get('bilgi',bilgi),k['ad'],puf,cel2,tur2,sekil=k.get('sek'))
        s.L.append((c,c2))
    def bitir(s):
        P=s.P; assert len(P.ANA)==s.n==len(P.KAR),(len(P.ANA),s.n,len(P.KAR))
        var_id=set(); var_tip=set(); kendi=os.path.join(H,'kartlar',s.onek+'.json')
        for f in glob.glob(os.path.join(H,'kartlar','*.json')):
            if f==kendi: continue
            d=json.load(open(f))
            for k in d.get('kartlar',[]): var_id.add(k['id'])
            for t in d.get('tipler',[]): var_tip.add(t['tipId'])
        tipler={}
        for k in s.kart:
            assert k['id'] not in var_id and k['tipId'] not in var_tip,('çakışma',k['id'],k['tipId'])
            tipler.setdefault(k['tipId'],dict(tipId=k['tipId'],ad=k['tip'],kartlar=[],uygulamaKonu=s.uyg))['kartlar'].append(k['id'])
        json.dump(dict(konu=s.konu,surum=1,kartlar=s.kart,tipler=list(tipler.values())),open(kendi,'w'),ensure_ascii=False,indent=1)
        P.yaz(os.path.join(H,s.klasor,s.onek+'-1.json'),os.path.join(H,s.klasor,s.onek+'-1-kardes.json'))
        print(s.onek,'tipler',len(tipler),Counter(q['zorluk'] for q in P.ANA))
def COG(onek,konu,uyg,pre,n): return Konu('tyt-cog',onek,konu,uyg,'TYT Coğrafya','tytcog',pre,n,'ÖSYM 2018–2026 TYT Coğrafya dağılımı · MEB lise coğrafya kitapları')
def FEL(onek,konu,uyg,pre,n): return Konu('tyt-fel',onek,konu,uyg,'TYT Felsefe','tytfel',pre,n,'ÖSYM 2018–2026 TYT Felsefe dağılımı · MEB lise felsefe kitapları')
