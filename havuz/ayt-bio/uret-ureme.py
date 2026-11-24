"""AYT Biyoloji · Üreme Sistemi ve Embriyonik Gelişim · 20 soru. Hücre/kromozom/kromatit sayıları, hormon eğrileri ve olasılıklar Python'da
hesaplanır; her öncülün doğru/yanlış değeri tek yerde tanımlanır, her cevap ve çeldirici assert edilir. Şekiller TikZ/pgfplots (cizim.tikz_svg)."""
import sys,os,json,math,itertools
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-bio')); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
import _hafif_bio as H
from _hafif_bio import *
from cizim import tikz_svg
import gorsel as G
KONU='Üreme Sistemi ve Embriyonik Gelişim'; H.KONU=KONU
P=Parti('ureme',KONU,'abio|'+KONU,ders='AYT Biyoloji',idon='aytbio')
KY='ÖSYM AYT 2018–2026 Biyoloji (Üreme Sistemi ve Embriyonik Gelişim) soruları (yalnız mantık) · MEB 11–12. sınıf biyoloji'
TIPAD={'ur-erkek':'Erkek üreme sistemi ve hormonal kontrol','ur-gamet':'Gametogenez (spermatogenez, oogenez)','ur-dongu':'Menstrüasyon döngüsü ve hormon grafikleri',
       'ur-disi':'Dişi üreme sistemi','ur-dollenme':'Döllenme ve ilk evreler','ur-tabaka':'Embriyonik tabakalar, zarlar ve plasenta','ur-ikiz':'İkizler ve kalıtım'}
NK=[0]
def Q(tipId,z,alt,fikir,tuzak,kalip,metin,istenen,ip,bilgi,ad,puf,sekil=None,dogru=None,yan=None,sira=None,kaz=None,kisa=None):
    tip=TIPAD[tipId]; NK[0]+=1; n=NK[0]; no=f'{n:04d}'; kid=f'K-ABUR-{n:02d}'
    kart(kid,alt,fikir,tuzak,z,kalip,len(ad),tipId,tip,KY)
    mk(P,no,ad=ad,adim=len(ad),tipId=tipId,tip=tip,z=z,alt=alt,kaz=kaz or alt+' konusunda yorum yapar.',kart=f'{kid} ({alt}) · özgün kurgu',kalip=kalip,
       metin=metin,dogru=dogru,yan=yan,istenen=istenen,ip=[ip],bilgi=bilgi,puf=puf,sekil=sekil,sira=sira,kisa=kisa)
RM=['I','II','III']
OS=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
OSET={'Yalnız I':{0},'Yalnız II':{1},'Yalnız III':{2},'I ve II':{0,1},'I ve III':{0,2},'II ve III':{1,2},'I, II ve III':{0,1,2}}
def onc(truth,neden,harf,yanlis_sor=False):
    """truth: 3 bool; neden: her öncülün neden doğru/yanlış olduğunu anlatan cümle parçası; harf: doğru şık konumu."""
    T={i for i in range(3) if truth[i]}
    anahtar={i for i in range(3) if not truth[i]} if yanlis_sor else T
    dog=[s for s in OS if OSET[s]==anahtar]; assert len(dog)==1; dog=dog[0]; p='ABCDE'.index(harf); ix=OS.index(dog)
    for comb in itertools.combinations(range(7),5):
        if ix in comb and comb.index(ix)==p: sec=[OS[j] for j in comb]; break
    else: raise AssertionError(('şık konumu mümkün değil',dog,harf))
    yan=[]
    for s_ in sec:
        if s_==dog: continue
        S_=OSET[s_]; parca=[]
        for i in sorted(S_^anahtar):
            sanilan=(i in S_) if not yanlis_sor else (i not in S_)
            assert sanilan!=truth[i]
            parca.append(f'{RM[i]}. öncülü '+('doğru' if sanilan else 'yanlış')+f' sanmış; oysa {neden[i]}.')
        yan.append((s_,' '.join(parca),'bilgi'))
    return dog,yan,sec
def oadim(truth,neden):
    return [A(f'{RM[i]}. öncülü incele',neden[i][0].upper()+neden[i][1:]+'.',f'{RM[i]}: '+('doğru' if truth[i] else 'yanlış')) for i in range(3)]
def etiket_oncul(a,b_,c): return f'I. {a}\nII. {b_}\nIII. {c}\n'
def yer(dogru,digerler,harf):
    i='ABCDE'.index(harf); d=list(digerler); assert len(d)==4
    return d[:i]+[dogru]+d[i:]
def tk(body,scale=1.0): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small,scale=%s]\n%s\n\\end{tikzpicture}'%(scale,body))
def sayi(x,y,n,extra=''):
    return f'\\node[circle,draw,inner sep=1.3pt,fill=white,font=\\small\\bfseries{extra}] at ({x:.2f},{y:.2f}) {{{n}}};'
def pgf(govde,w='7cm',h='5.4cm',ek=''):
    return tikz_svg('\\begin{tikzpicture}[font=\\small]\n\\begin{axis}[width='+w+',height='+h+',tick label style={font=\\small},label style={font=\\small},'+ek+']\n'+govde+'\n\\end{axis}\n\\end{tikzpicture}')
def tab(bas,sat,cw=6.3,ilk_kalin=True):
    """Tablo SVG'si; yazı 11 px, sütun genişliği içeriğe göre."""
    n=len(bas); assert all(len(r)==n for r in sat)
    gen=[int(cw*max(len(str(x)) for x in [bas[j]]+[r[j] for r in sat])+22) for j in range(n)]
    W=sum(gen)+4; assert W<=500,('tablo çok geniş',W); h=27; Hh=h*(len(sat)+1)+4; b=[]; xs=[2]
    for g in gen: xs.append(xs[-1]+g)
    b.append(f'<rect x="2" y="2" width="{W-4}" height="{h}" style="fill:currentColor;stroke:none" fill-opacity=".08"/>')
    for j,s in enumerate(bas): b.append(G._t((xs[j]+xs[j+1])/2,2+h/2+4,str(s),size=11.5,bold=True))
    for i,row in enumerate(sat):
        y=2+h*(i+1)
        for j,s in enumerate(row): b.append(G._t((xs[j]+xs[j+1])/2,y+h/2+4,str(s),size=11.5,bold=(j==0 and ilk_kalin)))
    for i in range(len(sat)+2): b.append(f'<line x1="2" y1="{2+h*i}" x2="{W-2}" y2="{2+h*i}" stroke-width="{1.4 if i in (0,1,len(sat)+1) else 1}"/>')
    for x in xs: b.append(f'<line x1="{x}" y1="2" x2="{x}" y2="{2+h*(len(sat)+1)}" stroke-width="1"/>')
    return G._svg(W,Hh,''.join(b))

# =============== kromozom çizimi (2n=4: bir uzun, bir kısa homolog çifti) ===============
def krom(cx,cy,dup,uz,s=1.0,dx=0):
    """tek kromozom: dup=True ise iki kromatit + sentromer."""
    h=(.42 if uz else .26)*s; x=cx+dx
    if dup:
        return (f'\\draw[line width=1.5pt] ({x-.05*s:.2f},{cy-h:.2f})--({x-.05*s:.2f},{cy+h:.2f});\\draw[line width=1.5pt] ({x+.05*s:.2f},{cy-h:.2f})--({x+.05*s:.2f},{cy+h:.2f});'
                f'\\fill ({x:.2f},{cy:.2f}) circle (0.045);')
    return f'\\draw[line width=1.5pt] ({x:.2f},{cy-h:.2f})--({x:.2f},{cy+h:.2f});\\fill ({x:.2f},{cy:.2f}) circle (0.04);'
def hucre(cx,cy,r,kr,s=1.0):
    """kr: [(uzun mu, dup mu)] ; kromozomlar hücre içinde ortalanır"""
    b=[f'\\draw[line width=1pt,fill=vurgu!10] ({cx:.2f},{cy:.2f}) circle ({r});']
    n=len(kr); sp=.26*s
    for i,(uz,dup) in enumerate(kr): b.append(krom(cx,cy,dup,uz,s,dx=(i-(n-1)/2)*sp))
    return '\n'.join(b)

# ===== Kromozom/DNA sayımı (2n=4): hücre başına kromozom ve kromatit =====
def say(kr): return len(kr),sum(2 if d else 1 for _,d in kr)
SG=[(1,0),(1,0),(0,0),(0,0)]; BS=[(1,1),(1,1),(0,1),(0,1)]; IS=[(1,1),(0,1)]; ST=[(1,0),(0,0)]
assert say(SG)==(4,4) and say(BS)==(4,8) and say(IS)==(2,4) and say(ST)==(2,2)

# =============== ŞEKİL 1 · erkek üreme sistemi (ön görünüş, şematik) ===============
def sek_erkek(no):
    """no: dict ad->numara"""
    b=[]
    # mesane
    b.append('\\draw[line width=1pt,fill=vurgu!8] (0,3.9) ellipse (1.0 and 0.75);')
    # sperm kanalları (mesane üzerinden geçer) ve epididim, testis
    for sg in (-1,1):
        b.append(f'\\draw[line width=1.3pt] ({sg*2.0},0.95) .. controls ({sg*2.6},2.0) and ({sg*1.9},4.6) .. ({sg*0.7},3.3) .. controls ({sg*0.45},2.9) and ({sg*0.3},2.6) .. ({sg*0.2},2.3);')
        b.append(f'\\draw[line width=1pt,fill=vurgu!14,rotate around={{{-sg*12}:({sg*1.9},0.2)}}] ({sg*1.9},0.2) ellipse (0.62 and 0.98);')
        b.append(f'\\draw[line width=2.2pt,line cap=round] ({sg*2.18},0.95) .. controls ({sg*2.7},0.5) and ({sg*2.6},-0.3) .. ({sg*2.05},-0.62);')
        b.append(f'\\draw[line width=1pt,fill=vurgu!14] ({sg*1.0},3.0) ellipse (0.28 and 0.55);')
    # prostat
    b.append('\\draw[line width=1pt,fill=vurgu!22] (0,2.25) ellipse (0.62 and 0.45);')
    # üretra
    b.append('\\draw[line width=2.4pt,line cap=round] (0,2.7)--(0,2.0)--(0,-0.9);')
    b.append('\\draw[line width=1pt] (-.35,2.0)--(-.35,-.9) (.35,2.0)--(.35,-.9);')
    # numaralar (sağ taraftaki yapılar)
    lab=[('testis',(1.75,0.2),(3.4,0.2)),('epididim',(2.62,0.15),(3.4,-.7)),('sperm',(2.21,2.17),(3.4,1.75)),('vezikul',(1.0,3.0),(3.4,3.1)),('prostat',(0.5,2.25),(3.4,2.5)),('uretra',(0.18,0.3),(3.4,-1.6))]
    for ad,(x,y),(lx,ly) in lab:
        b.append(f'\\draw[line width=.6pt] ({x},{y})--({lx-.2},{ly});')
        b.append(sayi(lx,ly,no[ad]))
    b[-1]=b[-1].replace('(3.4,-1.6)','(3.4,-1.6)')
    return tk('\n'.join(b),.9)

# =============== ŞEKİL 2 · dişi üreme sistemi (ön görünüş) ===============
def sek_disi(no):
    b=[]
    b.append('\\draw[line width=1pt,fill=vurgu!10] (-0.75,2.45) .. controls (-1.35,2.6) and (-1.35,1.2) .. (-0.55,0.55) -- (-0.35,0.15) -- (0.35,0.15) -- (0.55,0.55) .. controls (1.35,1.2) and (1.35,2.6) .. (0.75,2.45) .. controls (0.3,2.9) and (-0.3,2.9) .. cycle;')
    b.append('\\draw[line width=1pt,fill=vurgu!22] (-0.34,0.15) rectangle (0.34,-0.12);')   # serviks
    b.append('\\draw[line width=1pt,fill=vurgu!6] (-0.34,-0.12) -- (-0.5,-1.5) -- (0.5,-1.5) -- (0.34,-0.12);')
    for sg in (-1,1):
        b.append(f'\\draw[line width=2pt,line cap=round] ({sg*0.95},2.35) .. controls ({sg*1.8},2.9) and ({sg*2.4},3.0) .. ({sg*2.75},2.45);')
        b.append(f'\\draw[line width=1pt] ({sg*2.75},2.45) -- ({sg*2.95},2.7) ({sg*2.75},2.45) -- ({sg*3.0},2.4) ({sg*2.75},2.45) -- ({sg*2.9},2.1);')
        b.append(f'\\draw[line width=1pt,fill=vurgu!28,rotate around={{{sg*20}:({sg*2.75},1.45)}}] ({sg*2.75},1.45) ellipse (0.42 and 0.62);')
    lab=[('tuba',(2.0,2.8),(3.9,3.3)),('yumurtalik',(3.0,1.4),(3.9,1.4)),('uterus',(1.05,1.5),(3.9,0.2)),('serviks',(0.3,0.0),(3.9,-.7)),('vajina',(0.4,-.9),(3.9,-1.5))]
    for ad,(x,y),(lx,ly) in lab:
        b.append(f'\\draw[line width=.6pt] ({x},{y})--({lx-.2},{ly});')
        b.append(sayi(lx,ly,no[ad]))
    return tk('\n'.join(b),.95)

# =============== ŞEKİL 3 · spermatogenez hücreleri (2n=4) ===============
def sek_spermatogenez(no):
    """no: aşama -> numara. aşamalar: sg, bs, is, st, sp"""
    xs={'sg':0,'bs':3.4,'is':6.8,'st':10.2,'sp':13.6}; b=[]
    for a,kr in (('sg',SG),('bs',BS),('is',IS),('st',ST)):
        b.append(hucre(xs[a],0,.85,kr,.9))
    x=xs['sp']
    b.append(f'\\draw[line width=1pt,fill=vurgu!10] ({x-.15},0) ellipse (0.55 and 0.4);')
    b.append(f'\\draw[line width=1.2pt] ({x+.4},0) .. controls ({x+.8},.3) and ({x+1.0},-.3) .. ({x+1.5},0);')
    b.append(krom(x-.15,0,False,True,.9,dx=-.12)); b.append(krom(x-.15,0,False,False,.9,dx=.12))
    for a in ('sg','bs','is','st'): b.append(sayi(xs[a],-1.45,no[a]))
    b.append(sayi(xs['sp']+.4,-1.45,no['sp']))
    for a1,a2,t in (('sg','bs','büyüme'),('bs','is','mayoz\\\\I'),('is','st','mayoz\\\\II'),('st','sp','farklı-\\\\laşma')):
        xe=xs[a2]-.95 if a2!='sp' else xs[a2]-.8
        b.append(f'\\draw[-{{Stealth[length=2.2mm]}},line width=.9pt] ({xs[a1]+.95},0)--({xe},0);')
        b.append(f'\\node[font=\\footnotesize,above,align=center,inner sep=1pt] at ({(xs[a1]+.95+xe)/2},.02) {{{t}}};')
    return tk('\n'.join(b),.7)

# =============== ŞEKİL 4 · oogenez hücreleri (2n=4) ===============
def sek_oogenez(no):
    """no: oog, bo, io, k1, ot, k2"""
    b=[]
    b.append(hucre(0,0,.85,SG,.9)); b.append(hucre(3.2,0,.85,BS,.9)); b.append(hucre(6.4,.7,.85,IS,.9)); b.append(hucre(6.4,-1.7,.42,IS,.5))
    b.append(hucre(9.6,.7,.85,ST,.9)); b.append(hucre(9.6,-1.7,.42,ST,.5))
    pos={'oog':(0,-1.35),'bo':(3.2,-1.35),'io':(6.4,1.95),'k1':(7.1,-1.7),'ot':(9.6,1.95),'k2':(10.3,-1.7)}
    for a,(x,y) in pos.items(): b.append(sayi(x,y,no[a]))
    A_='\\draw[-{Stealth[length=2.2mm]},line width=.9pt]'
    b.append(A_+' (.95,0)--(2.25,0);\\node[font=\\footnotesize,above] at (1.6,.02) {büyüme};')
    b.append(A_+' (4.0,.25)--(5.5,.6);\\node[font=\\footnotesize,above] at (4.55,.55) {mayoz I};')
    b.append(A_+' (3.9,-.4)--(5.9,-1.5);')
    b.append(A_+' (7.3,.7)--(8.6,.7);\\node[font=\\footnotesize,above,align=center,inner sep=1pt] at (7.95,.75) {mayoz\\\\II};')
    b.append(A_+' (7.2,.15)--(9.1,-1.4);')
    return tk('\n'.join(b),.7)

# =============== ŞEKİL 5 · zigottan blastosiste evreler ===============
def sek_evre(no):
    """no: zig, iki, dort, mor, bla"""
    b=[]; xs=[0,2.5,5.0,7.5,10.0]; R=.95
    for x in xs: b.append(f'\\draw[line width=1pt,dash pattern=on 2pt off 1.5pt] ({x},0) circle ({R+.12});')
    b.append(f'\\draw[line width=1pt,fill=vurgu!12] (0,0) circle (.75);\\fill (0,0) circle (.14);')
    b.append('\\draw[line width=1pt,fill=vurgu!12] (-.38,0) circle (.38);\\draw[line width=1pt,fill=vurgu!12] (.38,0) circle (.38);'.replace('(-.38,0)','(2.12,0)').replace('(.38,0)','(2.88,0)'))
    for dx,dy in ((-.38,.38),(.38,.38),(-.38,-.38),(.38,-.38)):
        b.append(f'\\draw[line width=1pt,fill=vurgu!12] ({5.0+dx:.2f},{dy:.2f}) circle (.37);')
    r=.3; pts=[(0,0)]+[(.6*math.cos(a),.6*math.sin(a)) for a in [i*math.pi/3 for i in range(6)]]+[(.82*math.cos(a+math.pi/6),.82*math.sin(a+math.pi/6)) for a in [i*2*math.pi/5 for i in range(5)]]
    for dx,dy in [(0,0)]+[(.45*math.cos(a),.45*math.sin(a)) for a in [i*math.pi/3 for i in range(6)]]+[(.72*math.cos(a+math.pi/6),.72*math.sin(a+math.pi/6)) for a in [i*math.pi/3 for i in range(6)]][:0]:
        b.append(f'\\draw[line width=.9pt,fill=vurgu!12] ({7.5+dx:.2f},{dy:.2f}) circle (.28);')
    for i in range(6):
        a=i*math.pi/3+math.pi/6; b.append(f'\\draw[line width=.9pt,fill=vurgu!12] ({7.5+.78*math.cos(a):.2f},{.78*math.sin(a):.2f}) circle (.17);')
    # blastosist: dış halka (trofoblast) + iç hücre kitlesi
    for i in range(14):
        a=i*2*math.pi/14; b.append(f'\\draw[line width=.9pt,fill=vurgu!12] ({10+.78*math.cos(a):.2f},{.78*math.sin(a):.2f}) circle (.14);')
    for dx,dy in ((-.45,.2),(-.28,.42),(-.5,-.02),(-.25,.1)):
        b.append(f'\\draw[line width=.9pt,fill=vurgu!45] ({10+dx:.2f},{dy:.2f}) circle (.17);')
    for a,x in zip(('zig','iki','dort','mor','bla'),xs): b.append(sayi(x,-1.5,no[a]))
    for i in range(4): b.append(f'\\draw[-{{Stealth[length=2.2mm]}},line width=.9pt] ({xs[i]+1.18},0)--({xs[i+1]-1.18},0);')
    return tk('\n'.join(b),.8)

# =============== HORMON EĞRİLERİ (28 günlük döngü; göreli derişim 0–10) ===============
def g(x,mu,s): return math.exp(-((x-mu)/s)**2/2)
GUN=[i/2 for i in range(0,57)]
def FSH(x): return .6+3.0*g(x,5,4)+2.2*g(x,14,1.4)
def LH(x): return 1.0+8.5*g(x,13.5,1.0)+.6*g(x,21,3)
def EST(x): return 1.0+5.6*g(x,12.5,3.2)+2.6*g(x,21,3.5)
def PRO(x): return .3+8.0*g(x,21,3.0)
def tepe(f,a=0,b=28): return max((x for x in GUN if a<=x<=b),key=f)
assert tepe(FSH)==5 and tepe(LH)==13.5 and tepe(EST)==12.5 and tepe(PRO)==21
assert tepe(LH)>tepe(EST) and tepe(LH)<tepe(PRO) and PRO(10)<.4 and PRO(13.5)<1
assert max(EST(x) for x in GUN)<max(LH(x) for x in GUN) and max(EST(x) for x in GUN if x>16)<max(EST(x) for x in GUN if x<16)
def pts(f,x0=0,x1=28,adim=1):
    xs=sorted(set([x0+i*adim for i in range(int(round((x1-x0)/adim))+1)]+[x for x in (11.5,12.5,13.5,14.5) if x0<=x<=x1]))
    return [(x,f(x)) for x in xs]
def egri(pt,stil): return '\\addplot[smooth,line width=1.5pt,%s] coordinates {%s};'%(stil,' '.join(f'({x:.2f},{y:.3f})' for x,y in pt))
def dugum(x,y,t,ek=''): return f'\\node[font=\\small\\bfseries{ek}] at (axis cs:{x},{y}) {{{t}}};'
def sek_hormon4(ad):
    """ad: hormon -> harf. FSH, LH, EST, PRO"""
    b=[egri(pts(PRO),'vurgu'),egri(pts(LH),'black'),egri(pts(EST),'black,dashed'),egri(pts(FSH),'black,dotted')]
    b.append(dugum(tepe(PRO)+2.3,PRO(tepe(PRO))-.2,ad['PRO'])); b.append(dugum(tepe(LH)+1.4,LH(tepe(LH))-.3,ad['LH']))
    b.append(dugum(tepe(EST)-2.6,EST(tepe(EST))+.4,ad['EST'])); b.append(dugum(1.6,FSH(1.5)+.9,ad['FSH']))
    return pgf('\n'.join(b),w='7.6cm',h='5.4cm',ek='xmin=0,xmax=28,ymin=0,ymax=10.5,xtick={0,7,14,21,28},ytick=\\empty,axis lines=left,xlabel={Menstrüasyon döngüsünün günleri},ylabel={Kandaki derişim}')
# Endometriyum kalınlığı (mm) — parça parça, gün
ENDO=[(0,6.0),(1,5.2),(3,3.0),(5,1.6),(8,2.4),(11,3.6),(14,5.0),(17,6.4),(21,7.8),(24,8.0),(26,6.8),(28,5.4)]
def lin(pt,x):
    for (x0,y0),(x1,y1) in zip(pt,pt[1:]):
        if x0<=x<=x1: return y0+(y1-y0)*(x-x0)/(x1-x0)
    raise ValueError(x)
def sek_endo():
    b=[egri(ENDO,'vurgu'),egri(pts(PRO),'black,dashed')]
    for xv in (5,14,21): b.append(f'\\draw[densely dotted] (axis cs:{xv},0) -- (axis cs:{xv},10.4);')
    for xm,r in ((2.5,'I'),(9.5,'II'),(17.5,'III'),(24.5,'IV')): b.append(dugum(xm,9.7,r))
    b.append('\\draw[line width=1.5pt,vurgu] (axis cs:0.6,8.4)--(axis cs:2.6,8.4);\\node[font=\\small,anchor=west] at (axis cs:3.0,8.4) {Endometriyum kalınlığı};')
    b.append('\\draw[line width=1.5pt,dashed] (axis cs:0.6,7.3)--(axis cs:2.6,7.3);\\node[font=\\small,anchor=west] at (axis cs:3.0,7.3) {Progesteron derişimi};')
    return pgf('\n'.join(b),w='7.6cm',h='5.4cm',ek='xmin=0,xmax=28,ymin=0,ymax=10.6,xtick={0,7,14,21,28},ytick=\\empty,axis lines=left,xlabel={Menstrüasyon döngüsünün günleri},ylabel={Göreli değer}')
# --- gebelik karşılaştırma ---
def PRO_K(x): return PRO(x) if x<=35 else .3
def PRO_L(x): return PRO(x) if x<=21 else 8.3+.075*(x-21)
def HCG(x): return 9.5/(1+math.exp(-(x-27)/2.2))
GUN35=sorted(set(list(range(0,36,2))+[19,21,23,35]))
def sek_gebelik():
    eks='xmin=0,xmax=35,ymin=0,ymax=11,xtick={0,7,14,21,28,35},ytick=\\empty,axis lines=left,xlabel={Gün}'
    k=[(x,PRO_K(x)) for x in GUN35]; l=[(x,PRO_L(x)) for x in GUN35]; h=[(x,HCG(x)) for x in GUN35]
    ax1=('\\begin{axis}[name=a,width=5.9cm,height=5cm,tick label style={font=\\small},label style={font=\\small},title={\\bfseries K kadını},ylabel={Kandaki derişim},'+eks+']\n'
         +egri(k,'vurgu')+'\n\\node[font=\\small,anchor=west] at (axis cs:21,10.2) {Progesteron};\\end{axis}')
    ax2=('\\begin{axis}[at={(a.east)},xshift=.9cm,anchor=west,width=5.9cm,height=5cm,tick label style={font=\\small},label style={font=\\small},title={\\bfseries L kadını},'+eks+']\n'
         +egri(l,'vurgu')+'\n'+egri(h,'black,dashed')+'\n\\node[font=\\small,anchor=east] at (axis cs:30,10.5) {Progesteron};\\node[font=\\small,anchor=east] at (axis cs:34.5,3.6) {hCG};\\end{axis}')
    return tikz_svg('\\begin{tikzpicture}[font=\\small]\n'+ax1+'\n'+ax2+'\n\\end{tikzpicture}')

# =============== ŞEKİL · ikiz oluşumu şeması ===============
def sek_ikiz():
    b=[]
    def yum(x,y): return f'\\draw[line width=1pt,fill=vurgu!14] ({x},{y}) circle (.5);\\fill ({x},{y}) circle (.12);'
    def spe(x,y): return f'\\draw[line width=1pt,fill=vurgu!14] ({x},{y}) ellipse (.22 and .15);\\draw[line width=1pt] ({x+.22},{y}) .. controls ({x+.45},{y+.15}) and ({x+.55},{y-.15}) .. ({x+.8},{y});'
    def zig(x,y): return f'\\draw[line width=1pt,fill=vurgu!14] ({x},{y}) circle (.5);\\fill ({x},{y}) circle (.12);'
    def emb(x,y): return f'\\draw[line width=1pt,fill=vurgu!30] ({x},{y}) circle (.4);'
    AR='\\draw[-{Stealth[length=2.2mm]},line width=.9pt]'
    # K çifti
    b.append('\\node[font=\\bfseries] at (-1.2,3.0) {K};')
    b.append(yum(0,3.0)+spe(1.0,3.0)+'\\node[font=\\large] at (.65,3.0) {+};'.replace('.65','.5').replace('3.0','3.0')) if False else None
    b.append(yum(0,3.0)); b.append(spe(1.45,3.0)); b.append('\\node at (.78,3.0) {+};')
    b.append(AR+' (2.35,3.0)--(3.3,3.0);'); b.append(zig(3.95,3.0))
    b.append(AR+' (4.6,3.0)--(5.5,3.45);'); b.append(AR+' (4.6,3.0)--(5.5,2.55);'); b.append(emb(6.0,3.5)); b.append(emb(6.0,2.5))
    # L çifti
    b.append('\\node[font=\\bfseries] at (-1.2,0.0) {L};')
    for y in (.6,-.6):
        b.append(yum(0,y)); b.append(spe(1.45,y)); b.append(f'\\node at (.78,{y}) {{+}};'); b.append(AR+f' (2.35,{y})--(3.3,{y});'); b.append(zig(3.95,y)); b.append(AR+f' (4.6,{y})--(5.55,{y});'); b.append(emb(6.0,y))
    for x,t in ((0,'yumurta'),(1.7,'sperm'),(3.95,'zigot'),(6.0,'embriyo')):
        b.append(f'\\node[font=\\footnotesize] at ({x},-1.5) {{{t}}};')
    b.append('\\draw[densely dotted] (-1.6,1.75)--(6.7,1.75);')
    return tk('\n'.join(x for x in b if x),.85)

# =============== ŞEKİL · soyağacı (ikizli aile) ===============
def sek_soyagaci():
    b=[]
    def kare(x,y,dolu=False): return f'\\draw[line width=1.1pt,fill={"black" if dolu else "white"}] ({x-.32},{y-.32}) rectangle ({x+.32},{y+.32});'
    def daire(x,y,dolu=False): return f'\\draw[line width=1.1pt,fill={"black" if dolu else "white"}] ({x},{y}) circle (.34);'
    b.append(kare(-1.3,2.4)); b.append(daire(1.3,2.4)); b.append('\\draw[line width=1.1pt] (-.98,2.4)--(.96,2.4);')
    b.append('\\draw[line width=1.1pt] (0,2.4)--(0,1.4);\\draw[line width=1.1pt] (-2.3,1.4)--(3.0,1.4);')
    b.append('\\draw[line width=1.1pt] (-2.3,1.4)--(-2.3,.8);'); b.append(daire(-2.3,.45,True))
    b.append('\\draw[line width=1.1pt] (.5,1.4)--(.5,.8);\\draw[line width=1.1pt] (2.1,1.4)--(2.1,.8);')
    b.append(kare(.5,.45)); b.append(daire(2.1,.45))
    b.append('\\node[font=\\small\\bfseries] at (.5,-.2) {X};\\node[font=\\small\\bfseries] at (2.1,-.2) {Y};')
    b.append('\\node[font=\\small,anchor=west] at (3.6,2.4) {\\tikz[baseline=-.5ex]\\draw[line width=1.1pt] (0,0) rectangle (.3,.3); Erkek};')
    b.append('\\node[font=\\small,anchor=west] at (3.6,1.8) {\\tikz[baseline=-.5ex]\\draw[line width=1.1pt] (.15,.15) circle (.15); Kadın};')
    b.append('\\node[font=\\small,anchor=west] at (3.6,1.2) {\\tikz[baseline=-.5ex]\\draw[line width=1.1pt,fill=black] (.15,.15) circle (.15); Albino};')
    return tk('\n'.join(b),.95)

# ===== SORULAR =====
def ayarla(n,hedef,kur):
    """1..n numaralarının bir sıralamasını bulur: doğru şık, sıralı şıklar arasında 'ABCDE'[hedef] konumunda olsun. kur(N)->(dogru,[yanlışlar])"""
    for perm in itertools.permutations(range(1,n+1)):
        N=dict(zip(sorted(range(n)),perm)); d,y=kur(perm)
        if len(set(y+[d]))==5 and sorted(y+[d]).index(d)=='ABCDE'.index(hedef): return perm
    raise AssertionError('numaralama bulunamadı')
def cevap_etiketi(q): return q['cevap']['sik']

# ================= 01 · erkek üreme sistemi · kolay · şekilli =================
AN1=['sperm','prostat','testis','uretra','epididim','vezikul']
def k1(p):
    N=dict(zip(AN1,p)); return f"{N['epididim']} – {N['vezikul']}",[f"{N['testis']} – {N['vezikul']}",f"{N['epididim']} – {N['prostat']}",f"{N['sperm']} – {N['vezikul']}",f"{N['testis']} – {N['prostat']}"]
N1=dict(zip(AN1,ayarla(6,'A',k1)))
d1,y1=k1([N1[a] for a in AN1])
sk1=sek_erkek(N1)
Q('ur-erkek','kolay','Erkek üreme sistemi yapıları','Sperm üretimi (testis), olgunlaşma–depolama (epididim), taşınma (sperm kanalı) ve sıvı salgılayan bezler ayrı yapılardır; her yapının görevi ayrı bilinmelidir.','Sperm üretildiği yerde olgunlaşıp depolandığını sanmak; prostat ile seminal veziküli karıştırmak.','şekilli',
 'Erkek üreme sisteminin yapıları şekilde numaralandırılarak gösterilmiştir.\nSpermatogenezle oluşan sperm hücreleri, hareket yeteneğini kazandıkları ve bir süre depolandıkları bir yapıdan geçer. Sperm hücrelerinin enerji kaynağı olan fruktozca zengin sıvı ise yardımcı bezlerden biri tarafından salgılanır.\nBuna göre, sırasıyla bu iki yapı şekildeki hangi numaralarla gösterilmiştir?',
 'Spermlerin olgunlaştığı ve depolandığı yapı ile fruktozca zengin sıvıyı salgılayan yapının numaraları.','Önce spermin üretildiği yerden dışarı çıktığı yola kadar yapıları sırala; sonra meni sıvısını salgılayan bezleri ayrı düşün.',
 [B('Sperm yolu ve meni sıvısı','Sperm hücreleri testislerdeki seminifer tübüllerde üretilir. Sperm kanalı, spermleri üretraya taşıyan borudur. Yardımcı bezlerin salgıları spermlerle birlikte meniyi oluşturur. Örnek: Leydig hücreleri seminifer tübüllerin arasında bulunur ve testosteron salgılar')],
 [A('Yapıları tanı',f'Şekildeki {N1["testis"]} testis, {N1["epididim"]} epididim, {N1["sperm"]} sperm kanalı, {N1["vezikul"]} seminal vezikül, {N1["prostat"]} prostat, {N1["uretra"]} üretradır.',f'testis {N1["testis"]} · epididim {N1["epididim"]} · vezikül {N1["vezikul"]}'),
  A('Olgunlaşma ve depolanma','Testiste üretilen spermler epididime geçer; hareket yeteneğini orada kazanır ve orada depolanır.',f'epididim: {N1["epididim"]}'),
  A('Fruktozlu sıvı','Spermlerin enerji kaynağı olan fruktozu seminal vezikül salgılar; prostat ise alkali bir sıvı salgılar.',f'seminal vezikül: {N1["vezikul"]}'),
  A('Sonuç','İki yapının numaraları sırasıyla yazılır.',d1)],
 'Yapıları üretimden çıkışa doğru sırala; bezlerin salgısını ayrı düşün.',sekil=sk1,dogru=d1,
 yan=[(y1[0],'Spermin üretildiği testisi, olgunlaştığı ve depolandığı yapı sanmış; oysa sperm üretimi testisteki seminifer tübüllerde, olgunlaşma ve depolanma ise epididimde olur.','bilgi'),
      (y1[1],'Fruktozlu sıvıyı prostatın salgıladığını sanmış; oysa prostat alkali sıvı salgılar, fruktozu seminal vezikül verir.','bilgi'),
      (y1[2],'Sperm kanalını depolama yeri sanmış ve fruktozu seminal veziküle doğru atfetmiş; oysa spermler epididimde olgunlaşıp depolanır, sperm kanalı yalnız taşıma görevi yapar.','bilgi'),
      (y1[3],'Hem sperm üretildiği testiste olgunlaştığını hem de fruktozun prostatta oluştuğunu sanmış; iki yapıyı da yanlış eşleştirmiştir.','bilgi')],
 sira=sorted([d1]+y1))
# ================= 02 · sperm hücresi · orta · öncüllü =================
T2=[True,True,False]
n2=['akrozom, sperm başında bulunan ve hidrolitik enzimler içeren bir keseciktir; bu enzimler yumurtanın dış katmanlarının çözülmesini sağlar',
    'orta kısımdaki mitokondriler ATP üretir ve bu ATP kuyruğun hareketi için kullanılır',
    'spermatitin sperme farklılaşması mayoz değildir; kromozom sayısı n olarak kalır, hücre yalnızca biçim ve organel düzeni bakımından değişir']
d2,y2,s2=onc(T2,n2,'D')
Q('ur-erkek','orta','Sperm hücresinin yapısı ve farklılaşma','Akrozom enzimleri, orta kısımdaki mitokondriler ve spermatitin farklılaşması (mayoz değildir) birlikte değerlendirilir.','Farklılaşmayı mayoz sanıp kromozom sayısının değiştiğini düşünmek.','öncüllü',
 'İnsanda spermatogenezin son basamağında spermatit evresindeki hücre, sitoplazmasının büyük bölümünü atar; çekirdek baş kısmında toplanır, organeller yeniden düzenlenir ve hücre kamçı kazanır. Bu süreçte oluşan sperm hücresi baş, orta kısım ve kuyruktan oluşur.\n'
 +etiket_oncul('Sperm başındaki akrozom, yumurtanın dış katmanlarını çözen enzimler içerir.','Orta kısımdaki mitokondriler, kuyruğun hareketi için gereken ATP’yi üretir.','Spermatitin sperme farklılaşması sırasında kromozom sayısı yarıya iner.')+'Buna göre, yukarıdaki yargılardan hangileri doğrudur?',
 'Sperm hücresinin yapısı ve oluşumuyla ilgili doğru yargılar.','Her yargıda hangi yapının ya da sürecin anlatıldığını belirle; sonra spermatitin farklılaşmasında hangi bölünmenin gerçekleştiğini hatırla.',
 [B('Sperm hücresinin yapısı','Sperm hücresi baş, orta kısım ve kuyruktan oluşur. Mayoz, kromozom sayısını yarıya indiren bölünmedir; mitoz ise kromozom sayısını korur. Örnek: Bir deri hücresi mitozla bölündüğünde yavru hücreler ana hücreyle aynı sayıda kromozom taşır')],
 oadim(T2,n2)+[A('Sonuç','Doğru yargılar I ve II’dir.','I ve II')],'Her yargıdaki yapıyı ya da süreci ayrı ayrı değerlendir.',sekil=None,dogru=d2,yan=y2,sira=s2)
# ================= 03 · erkek hormonları · orta · olumsuz =================
D3='Leydig hücreleri seminifer tübüllerin içinde bulunur ve mayoz bölünme geçirerek sperm hücrelerini oluşturur.'
Y3=[('FSH, seminifer tübüllerdeki Sertoli hücrelerini etkileyerek spermatogenezi destekler.','FSH’nin Sertoli hücrelerini uyararak spermatogenezi desteklediğini bilmeyip ifadeyi yanlış sanmış; oysa bu ifade doğrudur.','bilgi'),
    ('LH, Leydig hücrelerinden testosteron salgılanmasını uyarır.','LH’nin Leydig hücrelerini uyardığını karıştırıp ifadeyi yanlış sanmış; oysa bu ifade doğrudur.','bilgi'),
    ('Kanda testosteron derişimi arttığında hipotalamus ve hipofiz üzerinde negatif geri bildirim etkisi oluşur.','Testosteronun hipotalamus ve hipofizi baskıladığını bilmeyip ifadeyi yanlış sanmış; oysa negatif geri bildirim bu ifadedeki gibi işler.','bilgi'),
    ('Testosteron, erkeğe özgü ikincil eşey karakterlerinin gelişimini sağlar.','Testosteronun ikincil eşey karakterlerini geliştirdiğini yanlış sanmış; oysa bu ifade doğrudur.','bilgi')]
Q('ur-erkek','orta','Erkekte hormonal kontrol','FSH Sertoli hücrelerini, LH Leydig hücrelerini uyarır; testosteron negatif geri bildirimle hipofizi baskılar. Leydig hücreleri tübüllerin dışında, aralarında bulunur.','Leydig hücrelerini sperm üreten hücre saymak.','düz',
 'Erkekte hipotalamus, GnRH hormonuyla hipofizin FSH ve LH salgılamasını düzenler. Hipofiz hormonları testisteki farklı hücre gruplarını uyararak hem sperm üretimini hem de testosteron salgısını kontrol eder.\nBuna göre, erkekte üreme sisteminin hormonal kontrolüyle ilgili aşağıdakilerden hangisi yanlıştır?',
 'Erkekte hormonal kontrolle ilgili yanlış ifade.','Testisteki iki hücre grubunun (Sertoli ve Leydig) yerini ve görevini ayrı ayrı hatırla.',
 [B('Testisteki hücre grupları','Testis iki işlev görür: sperm üretir ve hormon salgılar. Bu işlevler testiste farklı hücre grupları tarafından yürütülür. Örnek: Pankreas hem sindirim enzimi hem hormon üretir')],
 [A('Hücre gruplarını ayır','Seminifer tübüllerde Sertoli hücreleri ve mayoz geçiren germ hücreleri bulunur; Leydig hücreleri tübüllerin arasındadır.','Sertoli: tübül içi · Leydig: tübül arası'),
  A('Hormon–hücre eşleşmesi','FSH Sertoli hücrelerine, LH Leydig hücrelerine etki eder; testosteron geri bildirimle bu salgıyı sınırlar.','FSH→Sertoli · LH→Leydig'),
  A('İfadeleri tara','Dört ifade bu bilgilerle uyumludur; Leydig hücrelerinin tübül içinde sperm oluşturduğunu söyleyen ifade çelişir.','1 ifade yanlış'),
  A('Sonuç','Leydig hücrelerini tübül içinde sperm oluşturan hücre olarak gösteren ifade yanlıştır.','yanlış ifade: Leydig')],
 'Hormonun hangi hücreyi uyardığını ve o hücrenin testisteki yerini ayrı düşün.',sekil=None,dogru=D3,yan=Y3,sira=yer(D3,[y[0] for y in Y3],'E'))
# ================= 04 · deney tablosu · zor · öncüllü =================
T4=[False,True,True]
n4=['tabloda testosteronu veren grupta LH derişimi normale dönüyor; testosteron LH salgısını artırmaz, baskılar (negatif geri bildirim)',
    'testis alınınca testosteron derişimi düşer, hipofizin baskılanması kalkar ve LH derişimi artar',
    'hipofiz alınınca LH kalmaz ve testosteron derişimi düşer; testis, testosteron üretmek için hipofizden gelen LH’ye gereksinim duyar']
d4,y4,s4=onc(T4,n4,'D')
sk4=tab(['Grup','Uygulama','LH','Testosteron'],[['K','Uygulama yapılmamış','Normal','Normal'],['1','Testisler alınmış','Yüksek','Çok düşük'],['2','Testisler alınmış + testosteron verilmiş','Normal','Normal'],['3','Hipofiz alınmış','Çok düşük','Düşük']])
Q('ur-erkek','zor','Erkekte geri bildirim deneyi','Organ çıkarma ve hormon verme gruplarını karşılaştırarak hormonların kaynağını ve negatif geri bildirimi yorumlamak.','Testosteronun LH’yi artırdığını sanmak; hipofiz–testis ilişkisini tersine yorumlamak.','tablo',
 'Aynı yaş ve kütledeki erkek sıçanlar dört gruba ayrılmıştır. Kontrol grubuna (K) uygulama yapılmamış; diğer gruplara tabloda belirtilen uygulamalar yapılmıştır. 2. gruptaki sıçanlara verilen testosteron miktarı, kandaki derişimi kontrol grubundaki düzeye getirecek ölçüdedir. Gruplarda ölçülen LH ve testosteron derişimleri tabloda verilmiştir.\n'
 +etiket_oncul('Testosteron, LH salgısını artıran bir geri bildirim mekanizmasında görev yapar.','Testislerin çıkarılması, hipofiz üzerindeki baskılayıcı etkiyi ortadan kaldırarak LH derişimini artırır.','Testosteron üretiminin sürmesi için hipofizden gelen LH gereklidir.')+'Buna göre, yukarıdaki yargılardan hangileri doğrudur?',
 'Deney sonuçlarından çıkarılabilecek doğru yargılar.','Her grupta hangi organ ya da hormon ortadan kalktığında diğer hormonun nasıl değiştiğine bak; geri bildirimin yönünü ayrıca değerlendir.',
 [B('Negatif geri bildirim','Bir hormonun derişimi artınca onu salgılatan uyarıyı azaltması negatif geri bildirimdir; derişim düşünce bu baskı ortadan kalkar. Örnek: Ortam ısındığında kapanan bir termostat, ısıtıcının çalışmasını sınırlar')],
 oadim(T4,n4)+[A('Sonuç','Doğru yargılar II ve III’tür.','II ve III')],'Organı çıkar, hormonu ver: hangi hormon değişiyorsa onun kaynağı ve baskılayıcısı o grupta görünür.',sekil=sk4,dogru=d4,yan=y4,sira=s4,kaz='Hormonal kontrol deneylerini yorumlar.')
# ================= 05 · spermatogenez hücreleri · orta · şekilli =================
HUC={'sg':(4,4),'bs':(4,8),'is':(2,4),'st':(2,2),'sp':(2,2)}   # (kromozom, kromatit=DNA miktarı)
assert HUC=={a:say(k) for a,k in (('sg',SG),('bs',BS),('is',IS),('st',ST),('sp',ST))}
def cift(a,b_,N): return ' ve '.join(map(str,sorted((N[a],N[b_]))))
def esit(a,b_): return (HUC[a][0]==HUC[b_][0],HUC[a][1]==HUC[b_][1])
assert esit('st','sp')==(True,True) and esit('sg','bs')==(True,False) and esit('is','st')==(True,False) and esit('sg','is')==(False,True) and esit('bs','is')==(False,False)
assert [c for c in itertools.combinations(HUC,2) if esit(*c)==(True,True)]==[('st','sp')]
AN5=['sg','bs','is','st','sp']
def k5(p):
    N=dict(zip(AN5,p)); return cift('st','sp',N),[cift('sg','is',N),cift('sg','bs',N),cift('is','st',N),cift('bs','is',N)]
N5=dict(zip(AN5,ayarla(5,'C',k5))); d5,y5=k5([N5[a] for a in AN5])
sk5=sek_spermatogenez(N5)
Q('ur-gamet','orta','Spermatogenezde kromozom ve DNA miktarı','Mayoz sırasında kromozom sayısı ile DNA (kromatit) miktarı ayrı ayrı izlenir; eşlenme sayıyı değil kromatit sayısını artırır.','Kromozom sayısı eşit olan hücrelerin DNA miktarlarının da eşit olduğunu sanmak (ve tersi).','şekilli',
 'Şekilde, kromozom sayısı 2n = 4 olan bir erkek canlıda spermatogenezin farklı evrelerindeki hücreler, oluşum sırasına göre soldan sağa gösterilmiştir. Hücrelerin çekirdeklerindeki DNA miktarı, kromatit sayısıyla orantılıdır.\nBuna göre, numaralanmış hücrelerden hangi ikisinde hem kromozom sayısı hem de DNA miktarı birbirine eşittir?',
 'Kromozom sayısı ve DNA miktarı birlikte eşit olan hücre çifti.','Her hücre için önce kromozom sayısını, sonra kromatit sayısını yaz; iki ölçütü birlikte karşılaştır.',
 [B('Kromozom ve kromatit','Eşlenmiş bir kromozom, sentromerle bağlı iki kardeş kromatitten oluşur; DNA miktarı kromatit sayısıyla orantılıdır. Mayoz I homolog kromozomları, mayoz II kardeş kromatitleri ayırır. Örnek: Eşlenmiş tek bir kromozom iki DNA molekülü taşır')],
 [A('Hücreleri say',f'{N5["sg"]}: 4 kromozom, 4 kromatit · {N5["bs"]}: 4 kromozom, 8 kromatit · {N5["is"]}: 2 kromozom, 4 kromatit · {N5["st"]} ve {N5["sp"]}: 2 kromozom, 2 kromatit.',f'kromozom/kromatit: {N5["sg"]}:4/4 · {N5["bs"]}:4/8 · {N5["is"]}:2/4 · {N5["st"]}:2/2 · {N5["sp"]}:2/2'),
  A('Çiftleri karşılaştır','Kromozom sayıları eşit olanlar bulunur; bunların kromatit sayıları da kontrol edilir.','kromozom eşit çiftlerin DNA’sı farklı olanları ele'),
  A('Yalnız bir çift kalır',f'Yalnız {N5["st"]} ve {N5["sp"]} numaralı hücrelerde her iki ölçüt de eşittir; sperm, spermatitin farklılaşmasıyla oluştuğundan kromozom ve DNA değişmez.',d5)],
 'Kromozom sayısını ve kromatit sayısını ayrı ayrı yaz; ikisi birden eşit olanı seç.',sekil=sk5,dogru=d5,
 yan=[(y5[0],'DNA miktarları eşit olan, kromozom sayıları farklı olan çifti seçmiş; oysa kromozom sayıları 4 ve 2’dir.','dikkat'),
      (y5[1],'Yalnız kromozom sayısının eşit olmasına bakmış; oysa bu iki hücrenin DNA miktarları 4 ve 8 kromatit olarak farklıdır.','dikkat'),
      (y5[2],'Yalnız kromozom sayısının eşit olmasına bakmış; oysa bu iki hücrenin DNA miktarları 4 ve 2 kromatit olarak farklıdır.','dikkat'),
      (y5[3],'Kromozom sayısı ve DNA miktarı iki hücrede de aynı oranda yarıya iniyor diye eşit saymış; oysa 4’e 2 ve 8’e 4 eşitlik değildir.','bilgi')],
 sira=sorted([d5]+y5))
# ================= 06 · mayoz sayımı · zor · düz =================
NM=2; KROM2N=8
sg6=2**NM; bs6=sg6; kb6=bs6*KROM2N; st6=bs6*4; ks6=st6*(KROM2N//2); fark6=ks6-kb6
assert (sg6,kb6,st6,ks6,fark6)==(4,32,16,64,32)
w_a=ks6
sg_y=NM; kb_y=sg_y*KROM2N; ks_y=sg_y*4*(KROM2N//2); w_b=ks_y-kb_y; assert w_b==16
w_c=kb6+ks6; w_d=0; assert w_c==96
Q('ur-gamet','orta','Mitoz ve mayozla oluşan hücrelerin kromozom sayımı','Mitoz hücre sayısını, mayoz hücre başına kromozom sayısını değiştirir; toplam kromozom sayısı adım adım hesaplanır.','Mayozda toplam kromozom sayısının değişmediğini sanmak; mitoz sayısını hücre sayısıyla karıştırmak.','düz',
 'Kromozom sayısı 2n = 8 olan bir erkek canlıda bir spermatogonyum art arda 2 kez mitoz geçirir. Oluşan hücrelerin tamamı büyüyerek birincil spermatosit olur ve her biri mayozu eksiksiz tamamlayarak spermatitleri oluşturur.\nBuna göre, oluşan spermatitlerin toplam kromozom sayısı, birincil spermatositlerin toplam kromozom sayısından kaç fazladır?',
 'Spermatitlerle birincil spermatositlerin toplam kromozom sayıları arasındaki fark.','Önce mitozlarla kaç hücre oluştuğunu bul; sonra her birincil spermatositten kaç spermatit çıktığını ve hücre başına kromozom sayısını hesapla.',
 [B('Hücre ve kromozom sayısı','Her mitoz hücre sayısını iki katına çıkarır. Bir birincil spermatosit mayoz sonunda 4 spermatit verir ve spermatitler n kromozomludur. Örnek: 3 mitozla bir hücreden 8 hücre oluşur')],
 [A('Mitozla hücre sayısı','İki ardışık mitozda hücre sayısı her seferinde ikiye katlanır.',f'2² = {sg6} hücre'),
  A('Birincil spermatositler',f'{bs6} birincil spermatositin her biri 2n = 8 kromozom taşır.',f'{bs6} × 8 = {kb6}'),
  A('Spermatit sayısı ve kromozomu',f'Her birincil spermatosit 4 spermatit verir; spermatitlerde n = 4 kromozom bulunur.',f'{bs6} × 4 = {st6} hücre · {st6} × 4 = {ks6}'),
  A('Fark',f'Spermatitlerin toplam kromozomundan birincil spermatositlerin toplamı çıkarılır.',f'{ks6} − {kb6} = {fark6}')],
 'Hücre sayısını ve hücre başına kromozomu ayrı ayrı çarp; sonra çıkar.',dogru=fark6,
 yan=[(w_d,'Mayozda kromozom sayısının yarıya inmesini hücre sayısındaki artışla dengelenmiş sanıp toplamın değişmediğini düşünmüş; oysa hücre sayısı 4 kat artarken hücre başına kromozom yarıya iner, toplam iki katına çıkar.','bilgi'),
      (w_b,'Yalnız tek mitoz geçirdiğini varsaymış: 2 birincil spermatosit (16 kromozom) ve 8 spermatit (32 kromozom) bulup farkı 16 saymıştır.','dikkat'),
      (w_a,'Yalnız spermatitlerin toplam kromozom sayısını bulmuş ve birincil spermatositlerin toplamını çıkarmayı unutmuş.','dikkat'),
      (w_c,'Fark yerine iki toplam kromozom sayısını toplamış.','islem')])
# ================= 07 · oogenez · orta · şekilli · öncüllü =================
HO={'oog':(4,4),'bo':(4,8),'io':(2,4),'k1':(2,4),'ot':(2,2),'k2':(2,2)}
assert HO=={'oog':say(SG),'bo':say(BS),'io':say(IS),'k1':say(IS),'ot':say(ST),'k2':say(ST)}
N7={'oog':5,'bo':1,'io':4,'k1':2,'ot':6,'k2':3}
sk7=sek_oogenez(N7)
T7=[False,True,False]
assert HO['bo'][1]==2*HO['io'][1] and HO['k2'][1]==HO['k2'][0]
n7=[f'{N7["io"]} numaralı ikincil oosit, mayoz II’yi sperm hücresi içine girdikten sonra tamamlar; ootit bu bölünmeyle oluşur',
    f'{N7["bo"]} numaralı hücre eşlenmiş 4 kromozom (8 kromatit), {N7["io"]} numaralı hücre 2 kromozom (4 kromatit) taşır; DNA miktarı yarıya iner',
    f'{N7["k2"]} numaralı hücre mayoz II sonunda oluştuğundan kromozomları tek kromatitlidir']
d7,y7,s7=onc(T7,n7,'B')
Q('ur-gamet','orta','Oogenez evreleri','İkincil oosit mayoz II’de bekler ve sperm girişiyle tamamlar; kutup hücreleri mayoz bölünmelerin yan ürünüdür; kromatit sayısıyla DNA miktarı izlenir.','Ootitin sperm girişinden önce oluştuğunu sanmak; kutup hücrelerinin eşlenmiş kromozom taşıdığını düşünmek.','şekilli',
 f'Şekilde, kromozom sayısı 2n = 4 olan bir dişi canlıda oogenez sırasında oluşan hücreler gösterilmiştir. Oklar hücrelerin oluşum yönünü gösterir; hücrelerin DNA miktarı kromatit sayısıyla orantılıdır.\n'
 +etiket_oncul(f'{N7["ot"]} numaralı hücre, sperm hücresi oosite girmeden önce mayoz II’yi tamamlayarak oluşmuştur.',f'{N7["bo"]} numaralı hücrenin DNA miktarı, {N7["io"]} numaralı hücrenin DNA miktarının iki katıdır.',f'{N7["k2"]} numaralı hücrenin kromozomları iki kromatitlidir.')+'Buna göre, yukarıdaki yargılardan hangileri doğrudur?',
 'Oogenez şemasına göre doğru yargılar.','Her hücrenin hangi bölünme sonucunda oluştuğunu şemadan izle; kromozomların kromatit sayısını çizimden say.',
 [B('Oogenezde mayoz ve döllenme','Dişide mayoz I tamamlandığında bir ikincil oosit ve sitoplazması çok az bir kutup hücresi oluşur. Örnek: Eşlenmiş bir kromozom iki kromatitli, eşlenmemiş bir kromozom tek kromatitlidir')],
 oadim(T7,n7)+[A('Sonuç','Doğru yargı yalnız II’dir.','Yalnız II')],'Şemada hücreyi oluşturan bölünmeyi ve kromatit sayısını izle.',sekil=sk7,dogru=d7,yan=y7,sira=s7)
# ================= 08 · spermatogenez–oogenez tablosu · orta · tablo · öncüllü =================
T8=[False,False,True]
n8=['mayoz, erkekte ergenlikte başlar; dişide ise embriyonik dönemde, doğumdan önce başlar',
    'ikincil oosit mayoz II’yi sperm girişiyle tamamlar; spermatogenezde ise mayoz II döllenmeye bağlı değildir',
    'bir birincil spermatositten 4 sperm, bir birincil oositten 1 yumurta (ootit) oluşur']
sk8=tab(['Satır','Özellik','Spermatogenez','Oogenez'],[['I','Mayoza başlama zamanı','Doğum öncesi','Ergenlik'],['II','Mayoz II için sperm girişi','Gerekli','Gerekli değil'],['III','Bir mayozla oluşan gamet sayısı','4','1']])
d8,y8,s8=onc(T8,n8,'C')
Q('ur-gamet','orta','Spermatogenez ve oogenez karşılaştırması','İki gametogenez sürecinin başlangıç zamanı, mayoz II’nin tamamlanması ve ürün sayısı karşılaştırılır.','Mayozun iki cinste de ergenlikte başladığını ya da mayoz II’nin spermatogenezde döllenmeye bağlı olduğunu sanmak.','tablo',
 'İnsanda gamet oluşumunu sağlayan spermatogenez ve oogenez, birbirinden bazı yönlerle ayrılır. Tabloda bu iki sürecin bazı özellikleri karşılaştırılmıştır.\nBuna göre, tablodaki satırlardan hangilerinde verilen bilgiler doğrudur?',
 'Bilgileri doğru olan satırlar.','Her satır için önce spermatogenezde, sonra oogenezde ilgili olayın ne zaman ve nasıl gerçekleştiğini ayrı ayrı hatırla.',
 [B('Gametogenezin zamanlaması','Gamet oluşumu mayozla gerçekleşir; erkekte bu sürece spermatogenez, dişide oogenez denir. Örnek: Mayoz, art arda gerçekleşen iki bölünmeden oluşur')],
 oadim(T8,n8)+[A('Sonuç','Doğru bilgi yalnız III. satırdadır.','Yalnız III')],'Spermatogenez ve oogenezi başlangıç, bekleme ve ürün sayısı yönünden ayrı ayrı sırala.',sekil=sk8,dogru=d8,yan=y8,sira=s8)
# ================= 09 · hormon grafiği (4 eğri) · orta · öncüllü =================
HAR={'PRO':'X','LH':'Y','EST':'Z','FSH':'T'}
sk9=sek_hormon4(HAR)
T9=[True,False,True]
assert tepe(EST)<tepe(LH) and tepe(FSH)<tepe(LH)<tepe(PRO)
n9=['X eğrisi, ovulasyondan sonra yükselen progesterona aittir; progesteronu ovulasyon sonrasında oluşan korpus luteum salgılar',
    'Z eğrisi östrojene aittir ve en yüksek değerine ani LH artışından, yani ovulasyondan önce ulaşır',
    'T eğrisi FSH’ye aittir; FSH’nin yüksek olduğu dönemde yumurtalıkta foliküller gelişir']
d9,y9,s9=onc(T9,n9,'C')
Q('ur-dongu','orta','Menstrüasyon döngüsünde dört hormon','FSH, LH, östrojen ve progesteron eğrilerinin biçiminden hormonu tanımak: ani tepe LH, ovulasyondan sonra yükselen progesteron.','Östrojenin ovulasyondan sonra en yüksek değerine ulaştığını sanmak; korpus luteumun kaynağını karıştırmak.','grafik',
 'Sağlıklı bir kadında 28 günlük menstrüasyon döngüsü boyunca kandaki FSH, LH, östrojen ve progesteron derişimlerindeki değişim grafikte X, Y, Z ve T harfleriyle gösterilmiştir. Eğrilerin hangi hormona ait olduğu ve ovulasyon günü grafikte belirtilmemiştir.\n'
 +etiket_oncul('X ile gösterilen hormon, ovulasyondan sonra oluşan korpus luteum tarafından salgılanır.','Z ile gösterilen hormonun derişimi en yüksek değerine ovulasyondan sonraki dönemde ulaşır.','T ile gösterilen hormonun derişiminin yüksek olduğu dönemde yumurtalıkta folikül gelişimi gerçekleşir.')+'Buna göre, yukarıdaki yargılardan hangileri doğrudur?',
 'Grafiğe göre doğru yargılar.','Önce ani artış gösteren eğriyi bulup ovulasyon gününü belirle; sonra diğer eğrileri bu güne göre konumlandır.',
 [B('Döngü hormonları','Menstrüasyon döngüsü, hipofizden salgılanan FSH ve LH ile yumurtalıktan salgılanan östrojen ve progesteronun birlikte çalışmasıyla yürür. Örnek: Bir hormonun kandaki derişimi zamana göre grafikle izlenir')],
 oadim(T9,n9)+[A('Sonuç','Doğru yargılar I ve III’tür.','I ve III')],'Ani tepe veren hormon ovulasyon günü hakkında ipucu verir.',sekil=sk9,dogru=d9,yan=y9,sira=s9)
# ================= 10 · endometriyum grafiği · orta · olumsuz =================
assert all(lin(ENDO,a)>lin(ENDO,b) for a,b in zip(range(0,5),range(1,6)))
assert all(lin(ENDO,a)<lin(ENDO,b) for a,b in zip(range(5,21),range(6,22)))
assert all(PRO(a)<PRO(b) for a,b in zip(range(14,21),range(15,22))) and all(PRO(a)>PRO(b) for a,b in zip(range(21,28),range(22,29))) and max(PRO(x) for x in range(5,14))<1
sk10=sek_endo()
D10='II. aralıkta kandaki progesteron derişimi, korpus luteumun etkisiyle döngünün en yüksek değerine ulaşır.'
Y10=[('I. aralıkta endometriyum kalınlığının azalması, uterus duvarının kanamayla dökülmesiyle ilgilidir.','Menstrüasyonun I. aralıkta endometriyum kalınlığını azalttığını bilmeyip ifadeyi yanlış sanmış; oysa bu ifade doğrudur.','bilgi'),
     ('II. aralıkta endometriyumun kalınlaşması, folikül hücrelerinin salgıladığı östrojenin etkisiyle gerçekleşir.','Östrojenin foliküler fazda endometriyumu kalınlaştırdığını bilmeyip ifadeyi yanlış sanmış; oysa bu ifade doğrudur.','bilgi'),
     ('III. aralıkta progesteron derişimi artar ve endometriyum embriyonun tutunmasına uygun biçimde gelişir.','Progesteronun endometriyumu embriyoya hazırladığını bilmeyip ifadeyi yanlış sanmış; oysa bu ifade doğrudur.','bilgi'),
     ('IV. aralıkta progesteron derişiminin düşmesi, korpus luteumun dejenere olduğunu gösterir.','Döllenme olmayınca korpus luteumun dejenere olup progesteronun düştüğünü bilmeyip ifadeyi yanlış sanmış; oysa bu ifade doğrudur.','bilgi')]
Q('ur-dongu','orta','Endometriyum ve progesteron grafiği','Endometriyumun dönemlerini (menstrüasyon, östrojenle kalınlaşma, progesteronla hazırlanma, korpus luteum dejenerasyonu) ve hormonların kaynağını grafikten okumak.','Korpus luteumun ovulasyondan önce de bulunduğunu ve progesteron salgıladığını sanmak.','grafik',
 'Döllenmenin gerçekleşmediği sağlıklı bir kadında 28 günlük menstrüasyon döngüsü boyunca endometriyum kalınlığındaki ve kandaki progesteron derişimindeki değişim grafikte verilmiştir. Döngünün ilk günü kanamanın başladığı gündür; döngü, kesikli çizgilerle I, II, III ve IV aralıklarına ayrılmıştır.\nBuna göre, aşağıdakilerden hangisi yanlıştır?',
 'Grafiğe göre yanlış ifade.','Progesteronun hangi aralıkta yükselip hangi aralıkta düştüğünü, kaynağı olan yapıyla birlikte düşün.',
 [B('Endometriyum ve hormonlar','Endometriyum, menstrüasyonda dökülür; östrojen onu yeniden kalınlaştırır, progesteron ise bezlerini embriyoya uygun hâle getirir. Örnek: Kalınlaşan endometriyum, uterus iç yüzeyini kaplayan zengin damarlı bir dokudur')],
 [A('Aralıkları oku','I: kanama ve kalınlık azalması · II: kalınlık artışı, progesteron düşük · III: progesteron yükselir · IV: progesteron düşer.','I, II, III, IV özeti'),
  A('Hormon kaynakları','Östrojeni gelişen folikül, progesteronu ovulasyondan sonra oluşan korpus luteum salgılar.','folikül → östrojen · korpus luteum → progesteron'),
  A('İfadeleri sına','Dört ifade grafikle ve bu kaynaklarla uyumludur; II. aralıkta progesteronun en yüksek olduğunu söyleyen ifade grafikle çelişir.','1 ifade çelişir'),
  A('Sonuç','II. aralıkta korpus luteum henüz oluşmamıştır, progesteron düşüktür; bu yüzden yanlış ifade budur.','yanlış ifade: II. aralık')],
 'Progesteronun kaynağını ve hangi aralıkta oluştuğunu grafikte işaretle.',sekil=sk10,dogru=D10,yan=Y10,sira=yer(D10,[y[0] for y in Y10],'A'))
# ================= 11 · gebelik grafiği · zor =================
assert PRO_K(28)<PRO_K(21)-5 and PRO_L(35)>PRO_L(28)>7 and HCG(21)<.6 and HCG(35)>9 and PRO_K(35)<1
sk11=sek_gebelik()
D11='L kadınında progesteronun 28. günden sonra da yüksek kalması, hCG’nin korpus luteumun işlevini sürdürmesini sağlamasıyla ilişkilidir.'
Y11=[('K kadınında 21. günden sonra progesteronun azalması, hCG salgısındaki artışın sonucudur.','K kadınında hCG bulunmadığını gözden kaçırmış; oysa K’de progesteron, döllenme olmadığı için korpus luteumun dejenere olmasıyla azalır.','dikkat'),
     ('L kadınında progesteronun 28. günden sonra yüksek kalması, ovulasyonun ikinci kez gerçekleşmesiyle açıklanabilir.','Progesteronun yüksek kalmasını yeni bir ovulasyona bağlamış; oysa gebelikte ovulasyonlar durur, korpus luteum hCG ile korunur.','bilgi'),
     ('L kadınında hCG, hipofizden salgılanarak FSH ve LH salgısını artırır.','hCG’nin kaynağını hipofiz sanmış; oysa hCG embriyodan köken alan hücrelerce salgılanır ve korpus luteumu korur.','bilgi'),
     ('K kadınında progesteronun artması, endometriyumun dökülmesini başlatan etkenlerden biridir.','Progesteronun yükselmesini kanamaya neden olan etken sanmış; oysa kanamayı başlatan, progesteron derişiminin düşmesidir.','bilgi')]
Q('ur-dongu','orta','Gebelikte hormon grafiği','Gebelikte embriyonun salgıladığı hCG korpus luteumu korur; progesteron yüksek kalır ve endometriyum dökülmez. Gebe olmayan kadında progesteron düşer.','hCG’yi hipofiz ya da yumurtalık hormonu sanmak; progesteronun düşüşünü kanamanın sonucu saymak.','grafik',
 'K ve L kadınlarının her ikisinde de döngünün ilk günü kanamanın başladığı gündür ve ovulasyon 14. günde gerçekleşmiştir. L kadınında döllenme olmuş, embriyo uterus duvarına tutunmuştur. Kadınların kanındaki progesteron derişimi ve L kadınında ayrıca hCG derişimi 35 gün boyunca izlenmiş, sonuçlar grafiklerde verilmiştir.\nBuna göre, aşağıdakilerden hangisi söylenebilir?',
 'Grafiklere göre söylenebilecek ifade.','İki kadının progesteron eğrilerini 21. günden sonra karşılaştır; hCG’nin ortaya çıktığı günü ve ne işe yaradığını düşün.',
 [B('Gebelikte hormonlar','Progesteron endometriyumu embriyoya uygun tutar; derişimi düşerse endometriyum dökülür. Gebelik testleri kanda ya da idrarda hCG hormonunu arar. Örnek: Bir yapıyı uyaran hormon kesilirse o yapı küçülür')],
 [A('K kadınının eğrisi','Progesteron 21. günde en yüksek değere ulaşır, sonra düşer; döllenme olmadığından korpus luteum dejenere olur.','K: düşüş → menstrüasyon'),
  A('L kadınının eğrisi','Progesteron 28. günden sonra da yüksek kalır; hCG yaklaşık 24. günden itibaren yükselir.','L: progesteron yüksek, hCG artar'),
  A('Neden–sonuç','hCG embriyodan gelir ve korpus luteumu korur; korpus luteum progesteron salgılamaya devam eder, endometriyum dökülmez.','hCG → korpus luteum → progesteron'),
  A('Seçenekleri ele','Diğer seçenekler hCG’nin kaynağını, ovulasyonu ya da progesteronun etkisini yanlış anlatır.','doğru ifade: hCG–korpus luteum ilişkisi')],
 'İki eğriyi 21. günden sonra karşılaştır, hormonların kaynağını düşün.',sekil=sk11,dogru=D11,yan=Y11,sira=yer(D11,[y[0] for y in Y11],'E'))
# ================= 12 · döngü süresi · kolay · hikâyeli =================
DONGU=32; LUT=14
ov=DONGU-LUT; assert ov==18 and ov+LUT==DONGU
alt12=DONGU//2; kural28=14; sayim_a=DONGU-LUT+1; sayim_b=DONGU-LUT-1
assert (alt12,kural28,sayim_a,sayim_b)==(16,14,19,17) and len({ov,alt12,kural28,sayim_a,sayim_b})==5
Q('ur-dongu','kolay','Ovulasyon gününün hesaplanması','Ovulasyondan sonraki evre (korpus luteum evresi) kabaca sabit sürelidir; ovulasyon günü döngü süresinden bu süre çıkarılarak bulunur.','Ovulasyonun her zaman 14. günde ya da döngünün tam ortasında olduğunu sanmak.','hikâyeli',
 'Düzenli menstrüasyon döngüsüne sahip bir kadında döngü süresi 32 gündür; döngünün ilk günü kanamanın başladığı gündür. Kadının izlem kaydına göre ovulasyondan sonra bir sonraki kanamaya kadar geçen süre, yani ovulasyondan sonraki 14. gün döngünün son günüdür.\nBuna göre, bu kadında ovulasyon döngünün kaçıncı günü gerçekleşmiştir?',
 'Ovulasyonun gerçekleştiği gün.','Döngünün son gününden, ovulasyondan sonraki gün sayısını geriye doğru say.',
 [B('Döngünün evreleri','Döngü, ovulasyondan önceki foliküler faz ve ovulasyondan sonraki luteal (korpus luteum) faz olarak iki bölümde incelenir. Örnek: 28 günlük döngüde luteal faz da yaklaşık 14 gündür')],
 [A('Veriyi yaz','Döngü 32 gündür; ovulasyondan sonraki 14. gün döngünün son günüdür.',f'döngü = {DONGU} · ovulasyon sonrası = {LUT}'),
  A('Geriye say',f'Ovulasyon günü, son günden ovulasyon sonrası gün sayısı kadar geridedir.',f'{DONGU} − {LUT} = {ov}'),
  A('Kontrol',f'{ov}. gün ovulasyon olursa, {LUT}. gün sonra yani {ov} + {LUT} = {DONGU}. gün döngü biter.',f'{ov} + {LUT} = {DONGU}')],
 'Döngü sonundan ovulasyon sonrası süreyi çıkar.',dogru=ov,
 yan=[(kural28,'Ovulasyonun her kadında 14. günde olduğunu sanmış; oysa bu, yalnız 28 günlük döngüler için geçerlidir.','bilgi'),
      (alt12,'Ovulasyonun döngünün tam ortasında olduğunu varsaymış (32 / 2 = 16).','bilgi'),
      (sayim_b,'Ovulasyondan sonraki 14 günün yanı sıra bir gün daha çıkarmış (32 − 14 − 1 = 17).','islem'),
      (sayim_a,'Ovulasyon gününü luteal evreye dahil sayarak 13 gün çıkarmış (32 − 13 = 19).','islem')])
# ================= 13 · dişi üreme sistemi · kolay · şekilli =================
AN13=['tuba','yumurtalik','uterus','serviks','vajina']
def k13(p):
    N=dict(zip(AN13,p)); return f"{N['tuba']} – {N['uterus']}",[f"{N['yumurtalik']} – {N['uterus']}",f"{N['tuba']} – {N['serviks']}",f"{N['yumurtalik']} – {N['tuba']}",f"{N['tuba']} – {N['vajina']}"]
N13=dict(zip(AN13,ayarla(5,'B',k13))); d13,y13=k13([N13[a] for a in AN13])
sk13=sek_disi(N13)
Q('ur-disi','kolay','Dişi üreme sistemi yapıları','Döllenme tubada gerçekleşir; embriyo blastosist evresinde uterus duvarına (endometriyum) tutunur.','Döllenmenin yumurtalıkta ya da uterusta gerçekleştiğini sanmak.','şekilli',
 'İnsan dişi üreme sisteminin yapıları şekilde numaralandırılarak gösterilmiştir.\nYumurtalıktan atılan ikincil oosit, bir sperm hücresiyle karşılaşarak döllenir ve oluşan zigot mitozla bölünerek ilerler. Blastosist evresine ulaşan embriyo, daha sonra gelişimini sürdüreceği yere tutunur.\nBuna göre, döllenmenin gerçekleştiği yapı ile embriyonun tutunduğu yapı sırasıyla şekildeki hangi numaralı yapılardır?',
 'Döllenme yeri ile embriyonun tutunma yerinin numaraları.','Yumurtanın yumurtalıktan atıldıktan sonra izlediği yolu sırala; embriyonun gelişeceği organı ayrıca düşün.',
 [B('Dişi üreme sisteminin yapıları','Yumurtalık yumurta hücrelerini üretir. Tuba (yumurta kanalı) yumurtayı uterusa taşır. Uterus, gelişen embriyoyu barındırır. Serviks, uterusun alt ucunu vajinaya bağlar. Örnek: Meni sıvısı vajinaya bırakılır')],
 [A('Yapıları tanı',f'Şekildeki {N13["tuba"]} tuba, {N13["yumurtalik"]} yumurtalık, {N13["uterus"]} uterus, {N13["serviks"]} serviks, {N13["vajina"]} vajinadır.',f'tuba {N13["tuba"]} · uterus {N13["uterus"]}'),
  A('Döllenme yeri','Atılan ikincil oosit tubaya girer; sperm hücresiyle tubada karşılaşır ve döllenme orada gerçekleşir.',f'döllenme: tuba ({N13["tuba"]})'),
  A('Tutunma yeri','Blastosist uterusa ulaşır ve endometriyuma tutunur.',f'tutunma: uterus ({N13["uterus"]})'),
  A('Sonuç','Sıra döllenme yeri, tutunma yeri olarak yazılır.',d13)],
 'Yumurtanın atıldıktan sonraki yolunu sırala.',sekil=sk13,dogru=d13,
 yan=[(y13[0],'Döllenmenin yumurtalıkta gerçekleştiğini sanmış; oysa yumurtalıktan atılan oosit tubaya girer ve döllenme tubada olur.','bilgi'),
      (y13[1],'Embriyonun serviksin içine tutunduğunu sanmış; oysa embriyo uterusun iç yüzeyine (endometriyuma) tutunur.','bilgi'),
      (y13[2],'Döllenmenin yumurtalıkta gerçekleştiğini ve embriyonun tubaya tutunduğunu sanmış; oysa döllenme tubada, tutunma uterus duvarında gerçekleşir.','bilgi'),
      (y13[3],'Embriyonun vajinaya tutunduğunu düşünmüş; oysa vajina doğum kanalıdır, embriyo uterusta gelişir.','bilgi')],
 sira=sorted([d13]+y13))
# ================= 14 · yumurtalık hormonları · orta · olumsuz =================
D14='Ovulasyon, korpus luteumdan salgılanan progesteronun ani artışıyla tetiklenir.'
Y14=[('Gelişen folikülün hücreleri östrojen salgılar.','Folikül hücrelerinin östrojen salgıladığını bilmeyip ifadeyi yanlış sanmış; oysa bu ifade doğrudur.','bilgi'),
     ('Ovulasyondan sonra boşalan folikül, korpus luteuma dönüşür.','Boşalan folikülün korpus luteuma dönüştüğünü bilmeyip ifadeyi yanlış sanmış; oysa bu ifade doğrudur.','bilgi'),
     ('Korpus luteum, progesteronun yanı sıra az miktarda östrojen de salgılar.','Korpus luteumun yalnız progesteron salgıladığını düşünüp ifadeyi yanlış sanmış; oysa korpus luteum az miktarda östrojen de salgılar.','bilgi'),
     ('Döllenme gerçekleşirse korpus luteum, embriyodan kaynaklanan hCG sayesinde işlevini sürdürür.','hCG’nin korpus luteumu koruduğunu bilmeyip ifadeyi yanlış sanmış; oysa bu ifade doğrudur.','bilgi')]
Q('ur-disi','orta','Yumurtalık yapıları ve hormonlar','Folikül östrojen, korpus luteum progesteron (az östrojen) salgılar; ovulasyonu ani LH artışı tetikler; hCG korpus luteumu korur.','Ovulasyonu tetikleyen hormonu karıştırmak.','düz',
 'Dişide yumurtalıktaki folikül, hipofiz hormonlarının etkisiyle gelişir. Folikül, ovulasyonla yumurta hücresini bırakır ve geriye kalan hücreler yeni bir yapıya dönüşerek hormon salgılamayı sürdürür. Bu süreçlerin tümü, hipofiz ve yumurtalık hormonlarının birbirini etkilediği bir denetim altındadır.\nBuna göre, dişi üreme sistemindeki bu olaylarla ilgili aşağıdakilerden hangisi yanlıştır?',
 'Yumurtalıkta gerçekleşen olaylarla ilgili yanlış ifade.','Ovulasyonu başlatan hormonun hangisi olduğunu, korpus luteumun neyi salgıladığını ayrı ayrı hatırla.',
 [B('Folikül ve korpus luteum','Folikül, yumurtalıkta yumurta hücresini çevreleyen yapıdır ve östrojen salgılar. Ovulasyondan sonra folikül hücreleri korpus luteuma dönüşür. Örnek: Hipofizin salgıladığı iki gonadotropin hormon vardır')],
 [A('Olay sırası','Önce folikül gelişir, ovulasyon olur, sonra boşalan folikül korpus luteuma dönüşür.','folikül → ovulasyon → korpus luteum'),
  A('Hormon kaynakları','Folikül östrojen, korpus luteum progesteron ve az östrojen salgılar; hCG korpus luteumu korur.','folikül: östrojen · korpus luteum: progesteron'),
  A('Ovulasyonun tetikleyicisi','Ovulasyonu başlatan, ani artış gösteren LH’dir; korpus luteum ise ovulasyondan sonra oluşur, bu yüzden ovulasyonu tetikleyemez.','ovulasyon → LH'),
  A('Sonuç','Ovulasyonu korpus luteumun progesteronuna bağlayan ifade yanlıştır.','yanlış ifade: progesteron')],
 'Ovulasyonu başlatan hormonun hangisi olduğunu ve yapıların oluşum sırasını düşün.',sekil=None,dogru=D14,yan=Y14,sira=yer(D14,[y[0] for y in Y14],'E'))
# ================= 15 · döllenme · zor · öncüllü =================
T15=[True,True,True]
IO=(23,46); K2=(23,23); Z=(46,46)
assert IO[1]==2*IO[0] and K2[1]==K2[0] and Z[0]==2*IO[0]
n15=['ikincil oositte mayoz II başlamıştır, kromozomlar eşlenmiş durumda olup 23 kromozom × 2 kromatit = 46 kromatit bulunur',
     'mayoz II’de kardeş kromatitler ayrılır; ikinci kutup hücresi 23 tane tek kromatitli kromozom taşır',
     'zigot, ootit ve sperm çekirdeklerinin birleşmesiyle oluşur: 23 + 23 = 46 kromozom, ikincil oositteki 23’ün iki katıdır']
d15,y15,s15=onc(T15,n15,'E')
Q('ur-dollenme','zor','Döllenmede kromozom ve kromatit sayıları','İkincil oosit metafaz II’de (eşlenmiş kromozomlarla) bekler; sperm girişiyle mayoz II tamamlanır, ootit ve ikinci kutup hücresi oluşur; çekirdekler birleşince zigot 2n olur.','Kromozom ve kromatit sayısını karıştırmak.','öncüllü',
 'İnsanda (2n = 46) metafaz II evresinde bekleyen ikincil oosit tubada bir sperm hücresi ile karşılaşır ve sperm hücresi oositin içine girer. Bu olaydan sonra oosit mayoz II’yi tamamlar; oluşan ootitin çekirdeği ile spermin çekirdeği birleşerek zigot meydana gelir.\n'
 +etiket_oncul('Sperm hücresi oosite girmeden önce ikincil oositteki toplam kromatit sayısı 46’dır.','Mayoz II tamamlandığında oluşan ikinci kutup hücresinde tek kromatitli 23 kromozom bulunur.','Zigottaki toplam kromozom sayısı, ikincil oositteki toplam kromozom sayısının iki katıdır.')+'Buna göre, yukarıdaki yargılardan hangileri doğrudur?',
 'Döllenme sürecine ilişkin doğru yargılar.','Mayoz II’nin hangi evrede beklediğini, sperm girişiyle neyin ayrıldığını ve çekirdeklerin birleşmesinin kromozom sayısını nasıl etkilediğini adım adım izle.',
 [B('Döllenme ve ploidi','Mayoz, kromozom sayısını yarıya indirir; eşlenmiş her kromozom iki kardeş kromatitten oluşur. Örnek: 2n = 6 olan bir canlının gametinde 3 kromozom bulunur')],
 oadim(T15,n15)+[A('Sonuç','Üç yargı da doğrudur.','I, II ve III')],'Her aşamada kromozom ve kromatit sayısını ayrı ayrı yaz.',sekil=None,dogru=d15,yan=y15,sira=s15)
# ================= 16 · ilk evreler şeması · orta · olumsuz · şekilli =================
AN16=['zig','iki','dort','mor','bla']
N16={'zig':3,'iki':1,'dort':5,'mor':2,'bla':4}
sk16=sek_evre(N16)
D16=f'{N16["zig"]} numaralı evreden {N16["bla"]} numaralı evreye geçerken embriyonun toplam hacmi belirgin biçimde artar.'
Y16=[(f'{N16["zig"]} numaralı evreden {N16["iki"]} numaralı evreye geçişte oluşan her hücrenin kromozom sayısı, zigottaki kromozom sayısına eşittir.','Mitozla oluşan hücrelerin zigotla aynı kromozom sayısına sahip olduğunu bilmeyip ifadeyi yanlış sanmış; oysa bu ifade doğrudur.','bilgi'),
     (f'{", ".join(map(str,sorted([N16["iki"],N16["dort"],N16["mor"]])[:2]))} ve {sorted([N16["iki"],N16["dort"],N16["mor"]])[2]} numaralı evrelerdeki hücrelerin boyutu, her bölünmede küçülür.','Yarılmada (segmentasyon) hücre büyümesi olmadığını bilmeyip ifadeyi yanlış sanmış; oysa hücreler bölündükçe küçülür.','bilgi'),
     (f'{N16["mor"]} numaralı evre hücrelerden oluşan içi dolu bir kümedir; {N16["bla"]} numaralı evrede ise içi sıvı dolu bir boşluk bulunur.','Morula ile blastosistin yapısını karıştırıp ifadeyi yanlış sanmış; oysa bu ifade doğrudur.','bilgi'),
     (f'{N16["bla"]} numaralı evredeki embriyo uterus duvarına tutunur ve dış tabakasındaki hücreler plasentanın embriyoya ait kısmının oluşumuna katılır.','Blastosistin dış tabakasının plasentayı oluşturduğunu bilmeyip ifadeyi yanlış sanmış; oysa bu ifade doğrudur.','bilgi')]
Q('ur-dollenme','orta','Zigottan blastosiste yarılma evreleri','Yarılma (segmentasyon) mitozla gerçekleşir, hücre büyümesi olmaz; toplam hacim değişmez, hücreler küçülür; blastosist uterusa tutunur.','Hücre sayısı arttıkça embriyonun toplam hacminin de arttığını sanmak.','şekilli',
 'Şekilde, döllenmeden sonra tuba boyunca ilerleyen insan embriyosunun ilk evreleri gösterilmiştir. Bu evreler sırasında embriyo, çevresindeki koruyucu katman içinde kalır ve hücreler art arda mitoz bölünmeyle çoğalır.\nBuna göre, şekildeki evrelerle ilgili aşağıdakilerden hangisi yanlıştır?',
 'Şekildeki evrelerle ilgili yanlış ifade.','Yarılma sırasında hücrelerin büyüyüp büyümediğini ve çevredeki katmanın boyutunun değişip değişmediğini şekilden izle.',
 [B('Yarılma (segmentasyon)','Zigot, tuba boyunca ilerlerken ardışık mitoz bölünmelerle hücre sayısını artırır; bu bölünmeler arasında hücre büyümesi çok azdır. Örnek: Bir meyve dilimlendikçe parça sayısı artar, toplam meyve değişmez')],
 [A('Evre sırasını belirle',f'Zigot {N16["zig"]}, iki hücreli {N16["iki"]}, dört hücreli {N16["dort"]}, morula {N16["mor"]}, blastosist {N16["bla"]} numaralı evredir.','zigot → 2 → 4 → morula → blastosist'),
  A('Yarılmayı yorumla','Hücreler mitozla bölünür; kromozom sayısı değişmez, hücre boyutu küçülür; çevredeki koruyucu katmanın boyutu aynı kalır.','mitoz, büyüme yok'),
  A('İfadeleri sına','Dört ifade bu bilgilerle uyumludur; toplam hacmin belirgin arttığını söyleyen ifade, şekildeki sabit boyuta ve yarılma özelliğine aykırıdır.','1 ifade çelişir'),
  A('Sonuç','Toplam hacmin belirgin biçimde arttığını söyleyen ifade yanlıştır.','yanlış ifade: hacim artışı')],
 'Çevredeki katman ve toplam boyut şekilde nasıl değişiyor, bak.',sekil=sk16,dogru=D16,yan=Y16,sira=yer(D16,[y[0] for y in Y16],'A'))
# ================= 17 · embriyonik tabakalar tablosu · orta · olumsuz · tablo =================
TAB17={'X':['Epidermis','Beyin','Göz merceği','Saç ve tırnak'],'Y':['Kalp kası','Kemik','Böbrek','Pankreas'],'Z':['Karaciğer','Akciğer epiteli','Tiroit bezi','Mide epiteli']}
KOKEN={'Epidermis':'ekto','Beyin':'ekto','Göz merceği':'ekto','Saç ve tırnak':'ekto','Kalp kası':'meso','Kemik':'meso','Böbrek':'meso','Pankreas':'endo','Karaciğer':'endo','Akciğer epiteli':'endo','Tiroit bezi':'endo','Mide epiteli':'endo'}
SUT={'X':'ekto','Y':'meso','Z':'endo'}
yanlis=[y for s_,l in TAB17.items() for y in l if KOKEN[y]!=SUT[s_]]; assert yanlis==['Pankreas']
sk17=tab(['X','Y','Z'],[[TAB17['X'][i],TAB17['Y'][i],TAB17['Z'][i]] for i in range(4)],ilk_kalin=False)
Y17=[('Göz merceği','Göz merceğinin ektodermden geliştiğini bilmeyip X sütunundaki yerleşimi yanlış sanmış; oysa bu yerleşim doğrudur.','bilgi'),
     ('Böbrek','Böbreğin boşaltım sistemi organı olarak mezodermden geliştiğini bilmeyip Y sütunundaki yerleşimi yanlış sanmış; oysa bu yerleşim doğrudur.','bilgi'),
     ('Tiroit bezi','Tiroit bezinin endodermden geliştiğini bilmeyip Z sütunundaki yerleşimi yanlış sanmış; oysa bu yerleşim doğrudur.','bilgi'),
     ('Kalp kası','Kalp kasının mezodermden geliştiğini bilmeyip Y sütunundaki yerleşimi yanlış sanmış; oysa bu yerleşim doğrudur.','bilgi')]
Q('ur-tabaka','orta','Embriyonik tabakalardan gelişen yapılar','Ektoderm: epidermis, sinir sistemi, duyu organları; mezoderm: kas, iskelet, dolaşım ve boşaltım sistemi; endoderm: sindirim kanalı epiteli, karaciğer, pankreas, akciğer, tiroit.','Pankreası ve bezleri mezodermden gelişen yapılar sanmak.','tablo',
 'Gastrula evresinde oluşan üç embriyonik tabakadan gelişen yapılara örnekler, tabakaların adları verilmeden X, Y ve Z sütunlarında gösterilmiştir. Tabloda yapılardan yalnız biri, yanlış tabakanın sütununa yazılmıştır.\nBuna göre, yanlış sütuna yazılmış olan yapı aşağıdakilerden hangisidir?',
 'Yanlış sütuna yazılmış yapı.','Önce sütunların hangi embriyonik tabakaya ait olduğunu, çoğunluğu oluşturan yapılardan çıkar; sonra uymayan yapıyı ara.',
 [B('Embriyonik tabakalar','Gastrulada ektoderm, mezoderm ve endoderm oluşur. Dış tabaka ektoderm, orta tabaka mezoderm, iç tabaka endodermdir. Örnek: Dil epitelinin altındaki bağ dokusu mezodermden gelişir')],
 [A('Sütunları adlandır','X’te epidermis, beyin; Y’de kemik, kalp kası, böbrek; Z’de karaciğer, akciğer epiteli, mide epiteli çoğunlukta olduğundan X ektoderm, Y mezoderm, Z endodermdir.','X: ekto · Y: meso · Z: endo'),
  A('Yapıları sına','Her yapı kendi sütunundaki tabakayla karşılaştırılır; yalnız bir yapı uymaz.','12 yapı karşılaştırıldı'),
  A('Uymayan yapı','Pankreas, sindirim bezi olarak endodermden gelişir; ancak mezoderm sütununda yer almaktadır.','pankreas: endoderm'),
  A('Sonuç','Yanlış sütundaki yapı pankreastır.','Pankreas')],
 'Sütunun tabakasını çoğunluktan bul; uymayan yapıyı ara.',sekil=sk17,dogru='Pankreas',yan=Y17,sira=yer('Pankreas',[y[0] for y in Y17],'B'))
# ================= 18 · plasenta ve zarlar · zor · öncüllü =================
T18=[True,False,False]
n18=['amniyon boşluğundaki sıvı, embriyoyu mekanik darbelere karşı korur',
     'plasentada anne ile embriyonun kanları birbirine karışmaz; madde alışverişi, kılcal damar duvarları arasında difüzyonla gerçekleşir',
     'göbek kordonundaki iki atardamar, embriyodan plasentaya oksijence fakir kan taşır; plasentadan embriyoya oksijence zengin kanı kordondaki toplardamar getirir']
d18,y18,s18=onc(T18,n18,'A')
Q('ur-tabaka','orta','Plasenta, göbek kordonu ve embriyo zarları','Amniyon sıvısı korur; plasentada kanlar karışmaz, madde geçişi difüzyonla olur; kordonda 2 atardamar embriyodan plasentaya, 1 toplardamar plasentadan embriyoya kan taşır.','Anne ve embriyo kanının plasentada karıştığını sanmak; kordon damarlarında kanın yönünü ve oksijen durumunu ters yorumlamak.','öncüllü',
 'İnsan embriyosu uterus içinde gelişirken amniyon zarıyla çevrilidir ve göbek kordonuyla plasentaya bağlıdır. Plasenta, embriyonun koryon zarından köken alan kısmı ile annenin endometriyumundan oluşur; embriyonun beslenmesi, solunumu ve boşaltımı plasenta aracılığıyla anneyle gerçekleştirilir.\n'
 +etiket_oncul('Amniyon boşluğundaki sıvı, embriyoyu darbelere karşı korur.','Plasentada anne ve embriyonun kanları birbirine karışarak madde alışverişi sağlanır.','Göbek kordonundaki atardamarlar, plasentadan embriyoya oksijence zengin kan taşır.')+'Buna göre, yukarıdaki yargılardan hangileri doğrudur?',
 'Plasenta ve embriyo zarlarına ilişkin doğru yargılar.','Her yargıda hangi yapıdan söz edildiğini belirle.',
 [B('Plasenta ve kordon','Plasenta, gebelik süresince oluşan geçici bir organdır. Göbek kordonu, embriyoyu plasentaya bağlar ve içinden damarlar geçer. Örnek: Atardamar, kanı kalpten uzaklaştıran damardır')],
 oadim(T18,n18)+[A('Sonuç','Doğru yargı yalnız I’dir.','Yalnız I')],'Her yargıdaki yapıyı ve görevini ayrı ayrı değerlendir.',sekil=None,dogru=d18,yan=y18,sira=s18)
# ================= 19 · ikiz oluşumu şeması · orta · şekilli · öncüllü =================
T19=[True,True,False]
n19=['K çiftinde bebekler tek zigottan geliştiğinden, mutasyon olmadıkça aynı genotipe sahiptir',
     'K çiftinde tek zigot mitozla bölünür ve oluşan hücre toplulukları ayrılarak iki embriyoyu meydana getirir',
     'L çiftinde bebekler farklı zigotlardan oluştuğundan cinsiyetleri farklı olabilir']
sk19=sek_ikiz()
d19,y19,s19=onc(T19,n19,'B')
Q('ur-ikiz','orta','Tek yumurta ve çift yumurta ikizleri','Tek zigottan gelişen ikizler aynı genotipte ve aynı cinsiyette; iki ayrı zigottan gelişen ikizler farklı genotipte ve cinsiyetleri farklı olabilir.','Çift yumurta ikizlerinin cinsiyetlerinin aynı olmak zorunda olduğunu sanmak.','şekilli',
 'Şekilde K ve L ile gösterilen iki ayrı ikiz gebeliğinin oluşumu şematik olarak verilmiştir. Her gebelikte iki bebek gelişmiştir ve şekildeki hücrelerin hepsi insan hücresidir.\n'
 +etiket_oncul('K çiftindeki bebekler, mutasyon olmadıkça aynı genotipe sahiptir.','K çiftindeki bebekleri oluşturan hücreler, tek bir zigotun mitoz bölünmeleriyle oluşmuştur.','L çiftindeki bebeklerin cinsiyetlerinin aynı olması zorunludur.')+'Buna göre, yukarıdaki yargılardan hangileri doğrudur?',
 'Şekle göre doğru yargılar.','Her çiftte kaç yumurta ve kaç sperm hücresinin döllenmeye katıldığını, kaç zigot oluştuğunu şekilden say.',
 [B('İkiz oluşumu','İkizler, tek bir zigotun ayrılmasıyla ya da iki ayrı zigotun aynı anda gelişmesiyle oluşur. Örnek: Zigot, döllenmiş yumurta hücresinin adıdır')],
 oadim(T19,n19)+[A('Sonuç','Doğru yargılar I ve II’dir.','I ve II')],'Zigot sayısı, ikizlerin genotip ve cinsiyet benzerliğini belirler.',sekil=sk19,dogru=d19,yan=y19,sira=s19)
# ================= 20 · soyağacı ve ikiz olasılığı · zor =================
from fractions import Fraction as F
pA=F(1,4); tek=2*pA*(1-pA)
assert tek==F(3,8)
w1=F(1,16); w2=F(3,16); w3=F(1,4); w5=F(9,16)
assert w1==pA*pA and w2==pA*(1-pA) and w5==(1-pA)**2
assert len({w1,w2,w3,tek,w5})==5
sk20=sek_soyagaci()
Q('ur-ikiz','zor','İkizlerde kalıtım olasılığı','Çocuğu albino olan sağlıklı ebeveynler taşıyıcıdır (Aa × Aa); cinsiyetleri farklı ikizler çift yumurta ikizidir ve fenotipleri birbirinden bağımsız belirlenir.','Cinsiyeti farklı ikizleri tek yumurta ikizi sanmak ya da olasılıkları çarpmadan tek çocuk olasılığını vermek.','şekilli',
 'Albinizm, otozomal çekinik bir genle (a) taşınan kalıtsal bir durumdur. Şekilde, fenotipi normal olan bir çiftin albino kızı ve daha sonra doğan X ve Y ikizleri gösterilmiştir. İkizlerin biri erkek, diğeri kızdır; ikizlerin albino olup olmadığı belirtilmemiştir.\nBuna göre, X ve Y ikizlerinden yalnız birinin albino olma olasılığı kaçtır?',
 'İkizlerden yalnız birinin albino olma olasılığı.','İkizlerin kaç zigottan oluştuğunu belirle.',
 [B('Çekinik kalıtım ve ikizler','Çekinik bir özelliği taşıyan hastalıklı çocuk doğuran sağlıklı ebeveynler taşıyıcıdır. Farklı zigotlardan gelişen kardeşlerin genotipleri birbirinden bağımsız oluşur. Örnek: Bir madeni parayı iki kez atınca sonuçlar birbirini etkilemez')],
 [A('Ebeveyn genotipi','Fenotipi normal ebeveynlerin albino çocuğu olduğundan her ikisi de taşıyıcıdır.','Aa × Aa'),
  A('Tek çocuk olasılığı','Aa × Aa çaprazlamasında aa olasılığı 1/4, normal fenotip olasılığı 3/4’tür.','P(aa) = 1/4'),
  A('İkizin türü','Biri erkek, biri kız olduğundan ikizler iki ayrı zigottan oluşmuştur; fenotipler bağımsızdır.','çift yumurta ikizi'),
  A('Yalnız biri albino','X albino Y normal ya da X normal Y albino olabilir.',f'2 × 1/4 × 3/4 = 3/8')],
 'Ebeveyn genotipini ve ikizlerin zigot sayısını çıkar.',sekil=sk20,dogru='3/8',
 yan=[('1/16','İkizlerin her ikisinin de albino olma olasılığını (1/4 × 1/4) bulmuş; oysa soru yalnız birinin albino olmasını sormaktadır.','dikkat'),
      ('3/16','Yalnız X’in albino, Y’nin normal olma olasılığını (1/4 × 3/4) bulmuş; Y’nin albino, X’in normal olduğu durumu da saymamıştır.','dikkat'),
      ('1/4','İkizleri tek bir çocuk gibi ele alıp bir çocuğun albino olma olasılığını vermiş.','bilgi'),
      ('9/16','İkizlerin ikisinin de normal olma olasılığını (3/4 × 3/4) bulmuş; oysa istenen yalnız birinin albino olmasıdır.','dikkat')],
 sira=['1/16','3/16','1/4','3/8','9/16'])
# ================= yaz =================
def bitir_ab():
    for qq in P.ANA: qq['kardes']=None
    P.yaz(os.path.join(GD,'ureme-1.json'),'/tmp/bos-ureme.json')
    tipler={}
    for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu='abio|'+KONU))['kartlar'].append(c['id'])
    json.dump(dict(konu=KONU,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2018–2026 biyoloji soruları (yalnız mantık), MEB 11–12. sınıf biyoloji.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar','abureme.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler),'sorular',len(P.ANA))
bitir_ab()
