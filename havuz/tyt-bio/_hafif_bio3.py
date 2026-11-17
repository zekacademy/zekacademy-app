"""3. paket (kalitimuc, hucreuc) için ortak yardımcılar: öncüllü kurucu, tek doğru kurucu, kesir şıkları, soyağacı çözücü/çizici."""
import itertools
from _hafif_bio import *
KANON=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
def _ad(s): return KANON[[ 'I','II','III'].index(list(s)[0])] if False else None
def kume_ad(s):
    s=sorted(s,key=['I','II','III'].index)
    if len(s)==1: return 'Yalnız '+s[0]
    if len(s)==3: return 'I, II ve III'
    return ' ve '.join(s)
def onc(d,deger,harf):
    """d={'I':(bool,açıklama)}; deger True → doğru olanlar, False → yanlış olanlar istenir; harf: doğru şıkkın harfi."""
    T=frozenset(k for k,v in d.items() if v[0]==deger); assert T and len(T)<len(d)+1
    tum=[frozenset(x) for x in [('I',),('II',),('III',),('I','II'),('I','III'),('II','III'),('I','II','III')]]
    adlar=[kume_ad(x) for x in tum]; assert T in tum
    aday=[]
    for sub in itertools.combinations(range(7),5):
        if tum.index(T) in sub and sub.index(tum.index(T))=='ABCDE'.index(harf): aday.append(sub)
    assert aday,(T,harf)
    sub=aday[0]; sira=[adlar[i] for i in sub]; dogru=kume_ad(T); yan=[]
    for i in sub:
        S=tum[i]
        if S==T: continue
        c=[]
        for s in sorted(S-T,key=['I','II','III'].index): c.append(f'{s} gereksiz seçilmiş: {d[s][1]}')
        for s in sorted(T-S,key=['I','II','III'].index): c.append(f'{s} atlanmış: {d[s][1]}')
        yan.append((adlar[i],' · '.join(c),'bilgi'))
    return dict(dogru=dogru,yan=yan,sira=sira,T=T)
def adim_onc(d,s,ad=None):
    v=d[s][0]; return A(f'{s}. yargıyı değerlendir',d[s][1],f'{s}: '+('doğru' if v else 'yanlış'))
def sonuc(r,deger,ne='Doğru'):
    return A('Sonucu birleştir',('Doğru yargılar' if deger else 'Yanlış yargılar')+' yukarıdaki değerlendirmeden alınır.','Cevap: '+r['dogru'])
def yer(harf,dogru,yanlar):
    sira=[None]*5; sira['ABCDE'.index(harf)]=dogru; it=iter(yanlar)
    for i in range(5):
        if sira[i] is None: sira[i]=next(it)
    assert sorted(sira)==sorted([dogru]+list(yanlar)) and len(set(sira))==5; return sira
def kesirler(dogru,yanlar):
    """kesir/olasılık şıkları: Fraction → 'a/b', küçükten büyüğe sıralı sira döndürür"""
    v=[Fr(dogru)]+[Fr(y[0]) for y in yanlar]; assert len(set(v))==5
    f=lambda x:(str(x.numerator) if x.denominator==1 else f'{x.numerator}/{x.denominator}')
    sira=[f(x) for x in sorted(v)]
    return f(Fr(dogru)),[(f(Fr(y[0])),y[1],y[2]) for y in yanlar],sira
def tablo_dar(bas,sat):
    n=len(bas); gen=[max(54,7*max(len(str(x)) for x in [bas[j]]+[r[j] for r in sat])+14) for j in range(n)]
    W=sum(gen)+4; h=26; Hh=h*(len(sat)+1)+4; b=[]; xs=[2]
    for g in gen: xs.append(xs[-1]+g)
    b.append(f'<rect x="2" y="2" width="{W-4}" height="{h}" style="fill:currentColor;stroke:none" fill-opacity=".08"/>')
    for j,s in enumerate(bas): b.append(G._t((xs[j]+xs[j+1])/2,2+h/2+4,str(s),size=11,bold=True))
    for i,row in enumerate(sat):
        y=2+h*(i+1)
        for j,s in enumerate(row): b.append(G._t((xs[j]+xs[j+1])/2,y+h/2+4,str(s),size=11,bold=(j==0)))
    for i in range(len(sat)+2): b.append(f'<line x1="2" y1="{2+h*i}" x2="{W-2}" y2="{2+h*i}" stroke-width="{1.4 if i in (0,1,len(sat)+1) else 1}"/>')
    for x in xs: b.append(f'<line x1="{x}" y1="2" x2="{x}" y2="{2+h*(len(sat)+1)}" stroke-width="1"/>')
    assert W<=360,W
    return G._svg(W,Hh,''.join(b))
def tk(body,scale=1.0): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small,scale=%s]\n%s\n\\end{tikzpicture}'%(scale,body))
OKU='-{Stealth[length=2.3mm,width=1.9mm]}'
# ---------------- soyağacı ----------------
def allel(g): return {0:[0],1:[0,1],2:[1]}[g]
def tara(KISI,model):
    X=model in('XR','XD'); dom=model in('AD','XD'); ad=list(KISI); out=[]
    def sec(a):
        s,h,_,_=KISI[a]; gs=[0,1] if (X and s=='E') else [0,1,2]; r=[]
        for g in gs:
            if X and s=='E': aff=(g==1)
            else: aff=(g>=1) if dom else (g==2)
            if X and s=='K' and not dom: aff=(g==2)
            if aff==bool(h): r.append(g)
        return r
    for tup in itertools.product(*[sec(a) for a in ad]):
        G=dict(zip(ad,tup)); ok=True
        for a in ad:
            s,h,an,ba=KISI[a]
            if an is None: continue
            if X:
                iz={x for x in allel(G[an])} if s=='E' else {x+G[ba] for x in allel(G[an])}
            else: iz={x+y for x in allel(G[an]) for y in allel(G[ba])}
            if G[a] not in iz: ok=False;break
        if ok: out.append(G)
    return out
def pedciz(KISI,XY,evl,R=.3,etiket=None):
    """evl: [(anne,baba,[cocuklar],ybar)] ; XY: ad→(x,y)"""
    b=[]
    for a,(x,y) in XY.items():
        s,h,_,_=KISI[a]; fl='fill=black' if h else ''
        b.append(f'\\draw[line width=1.1pt,{fl}] ({x-R},{y-R}) rectangle ({x+R},{y+R});' if s=='E' else f'\\draw[line width=1.1pt,{fl}] ({x},{y}) circle ({R});')
        b.append(f'\\node[font=\\small] at ({x},{y-.58}) {{{a.split("-")[1]}}};')
    for e1,e2,cs,yb in evl:
        (x1,y),(x2,_)=XY[e1],XY[e2]
        if x1>x2: x1,x2=x2,x1
        b.append(f'\\draw[line width=1.1pt] ({x1+R},{y})--({x2-R},{y});'); m=(x1+x2)/2
        if cs:
            xs=[XY[c][0] for c in cs]; yc=XY[cs[0]][1]
            if len(cs)==1 and abs(xs[0]-m)<1e-9: b.append(f'\\draw[line width=1.1pt] ({m},{y})--({m},{yc+R});')
            else:
                b.append(f'\\draw[line width=1.1pt] ({m},{y})--({m},{yb});\\draw[line width=1.1pt] ({min(xs+[m])},{yb})--({max(xs+[m])},{yb});')
                for x in xs: b.append(f'\\draw[line width=1.1pt] ({x},{yb})--({x},{yc+R});')
    ys=sorted({y for x,y in XY.values()},reverse=True)
    for r,y in zip(['I','II','III','IV'],ys): b.append(f'\\node[font=\\normalsize\\bfseries] at ({min(x for x,_ in XY.values())-1.0},{y}) {{{r}}};')
    return '\n'.join(b)
