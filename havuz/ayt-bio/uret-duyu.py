"""AYT Biyoloji · Duyu Organları · 20 soru. Kardeş yok, ipucu 1.
Şekiller TikZ/pgfplots (cizim.tikz_svg): göz, kulak, deri şemaları, ışın yolu, mercek durumları, retina grafiği, koku grafiği, impuls kaydı;
öncüllerin doğru/yanlış değeri tek yerde (onc), grafik/tablo/ışın verileri Python'da hesaplanıp assert edilir."""
import sys,os,json,math
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-bio'))
import _hafif_bio as H
from _hafif_bio import *
from cizim import tikz_svg
KONU_AD='Duyu Organları'; KEY='abio|Duyu Organları'
P=Parti('duyu',KONU_AD,KEY,ders='AYT Biyoloji',idon='aytbio'); H.KONU=KONU_AD
KAYNAK='ÖSYM AYT 2018–2026 Biyoloji duyu organları soruları (yalnız mantık) · MEB 11. sınıf Denetleyici ve Düzenleyici Sistemler'
TIP={'yapi':('gz-yapi','Göz yapıları ve ışığın izlediği yol'),'retina':('gz-retina','Retina, çubuk–koni ve kör nokta'),
 'uyum':('gz-uyum','Akomodasyon ve göz bebeği tepkisi'),'kusur':('gz-kusur','Görme kusurları ve muayene sonuçları'),
 'kulak':('ku-yapi','Kulak yapısı, basınç ve denge'),'isitme':('ku-kusur','İşitme kayıpları'),
 'kemo':('bk-kemo','Koku ve tat reseptörleri'),'deri':('dr-reseptor','Deri ve reseptör sınıflandırması'),'impuls':('re-impuls','Reseptör uyarısı ve impuls oluşumu')}
HEDEF={}  # no -> beklenen cevap harfi
def Q(no,tp,z,kalip,alt,kaz,fikir,tuzak,ozet,ad,harf,**k):
    t,tn=TIP[tp]; kid=f'K-ABDUYU-{no[-2:]}'
    kart(kid,alt,fikir,tuzak,z,kalip,len(ad),t,tn,KAYNAK)
    HEDEF[no]=harf
    assert len(k['ip'])==1
    mk(P,no,ad=ad,adim=len(ad),tipId=t,tip=tn,z=z,alt=alt,kaz=kaz,kalip=kalip,kart=f'{kid} ({ozet})',**k)
ROM=['I','II','III','IV','V']
ETK={frozenset([0]):'Yalnız I',frozenset([1]):'Yalnız II',frozenset([2]):'Yalnız III',frozenset([0,1]):'I ve II',frozenset([0,2]):'I ve III',frozenset([1,2]):'II ve III',frozenset([0,1,2]):'I, II ve III'}
def onc(giris,yarg,kok,sira):
    """yarg: [(metin, doğru_mu, neden)]; döndürür: metin, dogru etiketi, yan listesi, adım listesi (öncül adımları)."""
    for t,d,n in yarg: assert n.endswith('.') and not n.endswith('..') and len(n)>30
    T=frozenset(i for i,(t,d,n) in enumerate(yarg) if d); assert T in ETK
    dogru=ETK[T]; assert dogru in sira and len(set(sira))==5 and all(s in ETK.values() for s in sira)
    inv={v:k for k,v in ETK.items()}
    metin=giris+'\n'+'\n'.join(f'{ROM[i]}. {t}' for i,(t,d,n) in enumerate(yarg))+'\n'+kok
    yan=[]
    for s in sira:
        if s==dogru: continue
        S=inv[s]; parca=[]
        for i in sorted(S-T): parca.append(f'{ROM[i]} öncülü yanlış olduğu hâlde doğru sanılmıştır: {yarg[i][2]}')
        for i in sorted(T-S): parca.append(f'{ROM[i]} öncülü doğru olduğu hâlde yanlış sanılmıştır: {yarg[i][2]}')
        yan.append((s,' '.join(parca),'bilgi'))
    adim=[A(f'{ROM[i]}. öncülü değerlendir',n,f'{ROM[i]}: '+('doğru' if d else 'yanlış')) for i,(t,d,n) in enumerate(yarg)]
    return dict(metin=metin,dogru=dogru,yan=yan,sira=sira,adim=adim,T=T)
def yer(harf,dogru,yanlar):
    sira=[None]*5; sira['ABCDE'.index(harf)]=dogru; it=iter(yanlar)
    for i in range(5):
        if sira[i] is None: sira[i]=next(it)
    assert sorted(sira)==sorted([dogru]+list(yanlar)); return sira
from cizim import tikz_svg
OK='-{Stealth[length=2.2mm,width=1.8mm]}'
def tk(body,scale=1.0,font='\\small'):
    return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=%s,scale=%s]\n%s\n\\end{tikzpicture}'%(font,scale,body))
def bez(p0,p1,p2,p3,t):
    return tuple((1-t)**3*p0[i]+3*(1-t)**2*t*p1[i]+3*(1-t)*t**2*p2[i]+t**3*p3[i] for i in (0,1))
CB=((-1.81,.845),(-2.55,.65),(-2.55,-.65),(-1.81,-.845))
# ---------------- GÖZ ----------------
EYE_T={ # parça: (hedef noktası, etiket konumu)
 'kornea':(bez(*CB,.25),(-3.3,1.55)),
 'sulu':((-1.7,.3),(-3.3,.6)),
 'pupil':((-1.22,.0),(-3.3,-.45)),
 'iris':((-1.16,-.8),(-3.0,-1.2)),
 'mercek':((-.7,-.3),(-.2,-2.85)),
 'camsi':((.5,.5),(.9,2.85)),
 'retina':((1.78*math.cos(math.radians(50)),1.78*math.sin(math.radians(50))),(2.9,2.0)),
 'sariben':((1.86,0.0),(3.5,.55)),
 'sinir':((2.45,-.75),(3.5,-1.4)),
 'sert':((2*math.cos(math.radians(-55)),2*math.sin(math.radians(-55))),(2.7,-2.5)),
}
def eye(lab,ligaments=True):
    b=[]
    b.append(r'\draw[line width=1.5pt] (205:2) arc[start angle=205,end angle=515,radius=2];')
    b.append(r'\draw[line width=1.5pt] (155:2) .. controls (-2.55,.65) and (-2.55,-.65) .. (205:2);')
    # retina (iki parça; görme siniri çıkışında kesik)
    b.append(r'\draw[line width=2.6pt] (214:1.86) arc[start angle=214,end angle=342,radius=1.86];')
    b.append(r'\draw[line width=2.6pt] (352:1.86) arc[start angle=352,end angle=506,radius=1.86];')
    # sarı benek: retinada yoğun kısa bölge
    b.append(r'\draw[line width=5pt] (-4:1.86) arc[start angle=-4,end angle=4,radius=1.86];')
    # görme siniri
    b.append(r'\draw[line width=1.2pt,fill=black,fill opacity=.12] (1.92,-.57)--(2.95,-.57)--(2.95,-.93)--(1.77,-.93);')
    # iris
    b.append(r'\draw[line width=3.4pt] (-1.16,.36)--(-1.16,1.5);\draw[line width=3.4pt] (-1.16,-.36)--(-1.16,-1.5);')
    # mercek
    b.append(r'\draw[line width=1.3pt,fill=black,fill opacity=.14] (-.78,.74) .. controls (-.5,.5) and (-.5,-.5) .. (-.78,-.74) .. controls (-1.06,-.5) and (-1.06,.5) .. (-.78,.74);')
    # silier gövde + askı bağları
    for s in (1,-1):
        b.append(f'\\draw[line width=1pt,fill=black,fill opacity=.3] (-.95,{s*1.33}) rectangle (-.55,{s*1.62});')
        b.append(f'\\draw[line width=.7pt] (-.85,{s*1.33})--(-.8,{s*.74});\\draw[line width=.7pt] (-.65,{s*1.33})--(-.76,{s*.74});')
    for k,n in lab.items():
        (tx,ty),(lx,ly)=EYE_T[k]
        b.append(f'\\node[font=\\normalsize\\bfseries] at ({lx},{ly}) {{{n}}};')
        # ok başı etiketten hedefe, etiket kenarından biraz içeride başlar
        dx,dy=tx-lx,ty-ly; d=math.hypot(dx,dy); sx,sy=lx+dx/d*.28,ly+dy/d*.28
        b.append(f'\\draw[{OK},line width=.8pt] ({sx:.2f},{sy:.2f})--({tx:.2f},{ty:.2f});')
    return '\n'.join(b)

# ---------------- KULAK ----------------
# hedef noktaları (x sağa), etiket konumları
EAR_T={
 'kepce':((0.1,0.5),(-.6,1.9)),
 'yol':((2.0,.18),(2.0,1.9)),
 'zar':((3.05,-0.15),(2.0,-1.7)),
 'cekic':((3.55,.12),(3.5,1.9)),
 'ors':((4.25,.38),(4.3,1.9)),
 'uzengi':((4.9,.28),(5.2,1.9)),
 'ostaki':((4.8,-2.0),(3.4,-2.8)),
 'koklea':((7.1,-.5),(8.9,-1.6)),
 'yarim':((6.9,1.55),(8.4,2.2)),
 'sinir':((8.0,-.1),(9.1,.4)),
}
def ear(lab):
    b=[]
    # kulak kepçesi
    b.append(r'\draw[line width=1.5pt] (1.1,1.3) .. controls (-.4,1.9) and (-.7,-1.9) .. (1.1,-1.3);')
    b.append(r'\draw[line width=1pt] (.8,.9) .. controls (.1,1.0) and (.0,-1.0) .. (.8,-.9);')
    # kulak yolu
    b.append(r'\draw[line width=1.4pt] (1.0,.4)--(3.0,.4);\draw[line width=1.4pt] (1.0,-.4)--(3.0,-.4);')
    # kulak zarı
    b.append(r'\draw[line width=2.4pt] (3.0,.42) .. controls (3.15,.15) and (3.15,-.15) .. (3.0,-.42);')
    # orta kulak boşluğu
    b.append(r'\draw[line width=1.4pt] (3.0,.4)--(3.0,1.05)--(5.7,1.05);\draw[line width=1.4pt] (3.0,-.4)--(3.0,-1.05)--(4.3,-1.05);\draw[line width=1.4pt] (5.0,-1.05)--(5.7,-1.05);')
    b.append(r'\draw[line width=1.4pt] (5.7,1.05)--(5.7,.55);\draw[line width=1.4pt] (5.7,.05)--(5.7,-.25);\draw[line width=1.4pt] (5.7,-.65)--(5.7,-1.05);')
    # östaki borusu
    b.append(r'\draw[line width=1.4pt] (4.3,-1.05) .. controls (4.4,-1.8) and (4.5,-2.0) .. (4.9,-2.6);\draw[line width=1.4pt] (5.0,-1.05) .. controls (5.1,-1.6) and (5.1,-1.8) .. (5.4,-2.4);')
    # kemikçikler: çekiç (sopa), örs (üçgen), üzengi (halka)
    b.append(r'\draw[line width=1.2pt,fill=black,fill opacity=.2] (3.1,.05)--(3.95,.2) -- (3.95,.04) -- (3.1,-.05)--cycle;\draw[line width=1.2pt,fill=black,fill opacity=.2] (3.95,.12) circle (.17);')
    b.append(r'\draw[line width=1.2pt,fill=black,fill opacity=.2] (4.1,.2)--(4.55,.8)--(4.7,.55)--(4.5,.4)--(4.3,.1)--cycle;')
    b.append(r'\draw[line width=1.2pt] (4.6,.5)--(5.1,.28);\draw[line width=1.2pt,fill=black,fill opacity=.2] (5.1,.28) circle (.17);\draw[line width=1.2pt] (5.1,.28) circle (.08);\draw[line width=2pt] (5.7,.35)--(5.7,.22);')
    # iç kulak: koklea (sarmal), yarım daire kanalları
    b.append(r'\draw[line width=2.6pt] plot[domain=0:760,samples=80,variable=\t] ({7.1+(.16+.0007*\t)*cos(\t)},{-.55+(.16+.0007*\t)*sin(\t)});')
    b.append(r'\draw[line width=1.2pt] (5.7,.35)--(6.4,.35) (5.7,-.4)--(6.4,-.4);')
    b.append(r'\draw[line width=1.8pt] (6.3,.35) .. controls (6.2,1.0) and (6.3,1.4) .. (6.7,1.55) .. controls (7.2,1.75) and (7.9,1.4) .. (7.6,.9) .. controls (7.4,.6) and (6.9,.5) .. (6.7,.45);')
    b.append(r'\draw[line width=1.8pt] (6.2,.9) .. controls (6.0,1.4) and (6.4,2.1) .. (6.9,2.0) .. controls (7.6,1.9) and (7.5,1.4) .. (7.2,1.3);')
    b.append(r'\draw[line width=1.8pt] (6.9,.5) circle (.2);')
    # işitme siniri
    b.append(r'\draw[line width=1.6pt] (7.7,-.1)--(8.6,.15);')
    for k,n in lab.items():
        (tx,ty),(lx,ly)=EAR_T[k]
        b.append(f'\\node[font=\\normalsize\\bfseries] at ({lx},{ly}) {{{n}}};')
        dx,dy=tx-lx,ty-ly; d=math.hypot(dx,dy); sx,sy=lx+dx/d*.28,ly+dy/d*.28
        b.append(f'\\draw[{OK},line width=.8pt] ({sx:.2f},{sy:.2f})--({tx:.2f},{ty:.2f});')
    return '\n'.join(b)

# ---------------- DERİ ----------------
SKIN_T={
 'epi':((5.3,3.75),(7.0,4.3)),
 'dermis':((5.6,2.7),(7.0,3.1)),
 'hipo':((5.4,.7),(7.0,.7)),
 'ter':((3.6,1.85),(7.0,1.9)),
 'kil':((1.5,4.5),(.3,5.0)),
 'kilkok':((1.5,2.15),(-.9,2.15)),
 'reseptor':((4.9,1.35),(7.0,1.2)),
}
def skin(lab):
    b=[]
    # katmanlar
    b.append(r'\draw[line width=1.4pt] (0,3.4) -- (6,3.4);\draw[line width=1.4pt] (0,1.7)--(6,1.7);')
    b.append(r'\draw[line width=1.5pt,fill=black,fill opacity=.10] (0,3.4) rectangle (6,3.95);')
    b.append(r'\draw[line width=1.5pt] (0,3.95) .. controls (1,4.05) and (2,3.85) .. (3,3.95) .. controls (4,4.05) and (5,3.85) .. (6,3.95);')
    b.append(r'\draw[line width=1.5pt] (0,3.4)--(0,0)--(6,0)--(6,3.4);')
    # epidermis hücre çizgileri
    for x in [i*.4+.2 for i in range(15)]: b.append(f'\\draw[line width=.4pt] ({x:.1f},3.4)--({x:.1f},3.9);')
    # hipodermis yağ hücreleri
    for (x,y) in [(.5,.8),(1.4,.55),(2.2,1.0),(3.0,.5),(3.7,1.1),(1.2,1.3),(2.6,1.45),(4.4,.5),(5.3,1.0),(.4,1.45)]:
        b.append(f'\\draw[line width=.8pt,fill=black,fill opacity=.06] ({x},{y}) circle (.28);')
    # kıl
    b.append(r'\draw[line width=2pt] (1.5,2.3)--(1.5,4.9);')
    b.append(r'\draw[line width=1.1pt] (1.3,2.0) .. controls (1.25,3.0) and (1.3,3.4) .. (1.32,3.95);\draw[line width=1.1pt] (1.7,2.0) .. controls (1.75,3.0) and (1.7,3.4) .. (1.68,3.95);')
    b.append(r'\draw[line width=1.1pt,fill=black,fill opacity=.25] (1.5,1.95) circle (.3);')
    # yağ (sebase) bezi
    b.append(r'\draw[line width=1pt,fill=black,fill opacity=.15] (2.15,2.75) ellipse (.3 and .2);\draw[line width=.8pt] (1.85,2.8)--(1.7,3.0);')
    # ter bezi: kangal + kanal
    b.append(r'\draw[line width=1.1pt] plot[domain=0:900,samples=90,variable=\t] ({3.6+(.1+.0003*\t)*cos(\t)},{1.95+(.1+.0003*\t)*sin(\t)});')
    b.append(r'\draw[line width=1.1pt] (3.6,2.1) .. controls (3.4,2.6) and (3.8,3.0) .. (3.6,3.4) .. controls (3.45,3.7) and (3.75,3.9) .. (3.6,4.05);')
    # damar
    b.append(r'\draw[line width=1pt] (4.2,3.4) .. controls (4.5,2.9) and (4.3,2.4) .. (4.6,1.9) .. controls (4.8,1.5) and (4.5,1.0) .. (4.6,.0);')
    # sinir ve reseptörler
    b.append(r'\draw[line width=1pt] (5.0,0)--(5.0,1.2);\draw[line width=1pt] (5.0,1.9)--(5.0,2.7) .. controls (5.0,3.0) and (5.3,3.2) .. (5.3,3.6);\draw[line width=1pt] (5.0,2.7) .. controls (5.0,3.0) and (4.7,3.3) .. (4.7,3.6);')
    b.append(r'\draw[line width=.9pt,fill=black,fill opacity=.1] (5.0,1.55) ellipse (.2 and .35);\draw[line width=.9pt] (5.0,1.55) ellipse (.12 and .25);\draw[line width=.9pt] (5.0,1.2)--(5.0,1.3) (5.0,1.8)--(5.0,1.9);')
    b.append(r'\draw[line width=.9pt] (5.0,1.55) ellipse (.05 and .12);')
    for k,n in lab.items():
        (tx,ty),(lx,ly)=SKIN_T[k]
        b.append(f'\\node[font=\\normalsize\\bfseries] at ({lx},{ly}) {{{n}}};')
        dx,dy=tx-lx,ty-ly; d=math.hypot(dx,dy); sx,sy=lx+dx/d*.28,ly+dy/d*.28
        b.append(f'\\draw[{OK},line width=.8pt] ({sx:.2f},{sy:.2f})--({tx:.2f},{ty:.2f});')
    return '\n'.join(b)

import math
R=1.5; LX=-1.05
def ray_eye(x0,fx,ad):
    """x0: gözün yatay kayması; fx: paralel ışınların odak noktası x (göz merkezinden)."""
    b=[]
    def P(x,y): return f'({x0+x:.3f},{y:.3f})'
    b.append(f'\\draw[line width=1.5pt] {P(0,0)} circle ({R});')
    b.append(f'\\draw[line width=3pt] {P(R*math.cos(math.radians(-55)),R*math.sin(math.radians(-55)))} arc[start angle=-55,end angle=55,radius={R}];')
    b.append(f'\\draw[line width=1.3pt,fill=black,fill opacity=.14] {P(LX,.75)} .. controls {P(LX+.3,.5)} and {P(LX+.3,-.5)} .. {P(LX,-.75)} .. controls {P(LX-.3,-.5)} and {P(LX-.3,.5)} .. {P(LX,.75)};')
    hs=[.62,.31,0,-.31,-.62]
    for h in hs:
        b.append(f'\\draw[line width=.9pt,{OK}] ({x0-3.2:.2f},{h}) -- {P(LX-.15,h)};' if False else f'\\draw[line width=.9pt] ({x0-3.2:.2f},{h}) -- {P(LX,h)};')
        # lens sonrası
        sl=-h/(fx-LX)  # eğim
        xs=LX; ys=h
        # retina ile kesişim
        xe=None
        x=LX
        while x<=R+.01:
            y=h+sl*(x-LX)
            if math.hypot(x,y)>=R and x>0: xe=x;ye=y;break
            x+=.002
        assert xe is not None
        b.append(f'\\draw[line width=.9pt] {P(LX,h)} -- {P(xe,ye)};')
        if fx>xe+.05 and h!=0:  # odak retinanın gerisinde: kesikli devam
            b.append(f'\\draw[line width=.6pt,dash pattern=on 2pt off 2pt] {P(xe,ye)} -- {P(fx,0)};')
    # ok başları (giriş)
    for h in hs: b.append(f'\\draw[line width=.9pt,{OK}] ({x0-3.2:.2f},{h}) -- ({x0-2.7:.2f},{h});')
    b.append(f'\\node[font=\\normalsize\\bfseries] at ({x0},-2.1) {{{ad}}};')
    return '\n'.join(b)
# ---------------- MERCEK DURUMLARI ----------------
def mercek(x0,yakin,ad):
    b=[]
    P=lambda x,y:f'({x0+x:.2f},{y:.2f})'
    if yakin: rx,ry,kd,kh=.55,.85,1.25,.5   # kalın mercek, kas kasılı (kalın, merceğe yakın)
    else: rx,ry,kd,kh=.24,.95,1.55,.26
    b.append(f'\\draw[line width=1.4pt,fill=black,fill opacity=.14] {P(0,0)} ellipse ({rx} and {ry});')
    for s in (1,-1):
        y0=s*kd; y1=s*(kd+kh)
        b.append(f'\\draw[line width=1.1pt,fill=black,fill opacity=.30] {P(-.55,y0)} rectangle {P(.55,y1)};')
        ys=s*ry*.96
        if yakin:
            for dx in (-.25,.25):
                b.append(f'\\draw[line width=.8pt,decorate,decoration={{snake,amplitude=.6pt,segment length=2.2mm}}] {P(dx,y0)} -- {P(dx*.5,ys*.99)};')
        else:
            for dx in (-.25,.25):
                b.append(f'\\draw[line width=.8pt] {P(dx,y0)} -- {P(dx*.5,ys*.99)};')
    b.append(f'\\node[font=\\normalsize\\bfseries] at ({x0},-2.5) {{{ad}}};')
    return '\n'.join(b)
def mercek_etiket(x0):
    b=[]
    b.append(f'\\node[font=\\small,anchor=east] at ({x0-1.2},0) {{Mercek}};\\draw[{OK},line width=.8pt] ({x0-1.15},0)--({x0-.55},0);')
    b.append(f'\\node[font=\\small,anchor=east] at ({x0-1.2},1.7) {{Silier kas}};\\draw[{OK},line width=.8pt] ({x0-1.15},1.7)--({x0-.5},1.6);')
    b.append(f'\\node[font=\\small,anchor=west] at ({x0+1.0},1.05) {{Askı bağı}};\\draw[{OK},line width=.8pt] ({x0+.98},1.05)--({x0+.3},1.0);')
    return '\n'.join(b)

import math
# ---------- retina reseptör yoğunluğu ----------
def kor(x): return 1-math.exp(-((x-15)/1.6)**2)
def koni(x): return (150*math.exp(-(x/2.4)**2)+7*math.exp(-(x/30)**2))*kor(x)
def cubuk(x): return 138*math.exp(-((abs(x)-19)/17)**2)*(1-math.exp(-(x/4.5)**2))*kor(x)
def retina_grafik():
    xs=sorted(set([float(i) for i in range(0,61,2)]+[11+i/2 for i in range(0,13)]))
    cx=' '.join(f'({x:.1f},{koni(x):.1f})' for x in xs); cy=' '.join(f'({x:.1f},{cubuk(x):.1f})' for x in xs)
    b=['\\begin{axis}[width=8.4cm,height=5.4cm,xmin=0,xmax=60,ymin=0,ymax=185,xtick={0,10,20,30,40,50,60},ytick={0,50,100,150},axis lines=left,'
       'tick label style={font=\\small},every axis plot/.append style={line width=1.4pt}]',
              f'\\addplot[black,smooth] coordinates {{{cx}}};',f'\\addplot[vurgu,smooth] coordinates {{{cy}}};',
       '\\node[font=\\small\\bfseries] at (axis cs:4.5,150) {X};\\node[font=\\small\\bfseries,vurgu] at (axis cs:32,125) {Y};',
       '\\draw[-{Stealth[length=2mm]},line width=.8pt] (axis cs:15,172)--(axis cs:15,12);\\node[font=\\small\\bfseries] at (axis cs:15,180) {L};','\\end{axis}',
       '\\node[font=\\small,anchor=north] at ([yshift=-.75cm]current axis.south) {{\\fontencoding{OT1}\\selectfont Sarı beneğe uzaklık (\\ensuremath{^\\circ})}};\\node[font=\\small,rotate=90,anchor=south] at ([xshift=-1.0cm]current axis.west) {{\\fontencoding{OT1}\\selectfont Hücre yoğunluğu (bin/mm\\ensuremath{^2})}};']
    return tk('\n'.join(b))
# ---------- koku adaptasyonu ----------
def koku(t):
    if t<0.3 or t>=5: return 0
    return 18+72*math.exp(-(t-.3)/1.1)
def koku_grafik():
    pts=[(0,0),(.3,0),(.3,90)]+[(.3+i*.1,koku(.3+i*.1)) for i in range(1,47)]+[(4.99,koku(4.99)),(5,0),(10,0)]
    c=' '.join(f'({x:.2f},{y:.1f})' for x,y in pts)
    b=['\\begin{axis}[width=8.4cm,height=5.0cm,xmin=0,xmax=10,ymin=0,ymax=110,xtick={0,1,2,3,4,5,6,7,8,9,10},ytick={0,25,50,75,100},axis lines=left,'
       'tick label style={font=\\small},every axis plot/.append style={line width=1.5pt}]',
              f'\\addplot[black] coordinates {{{c}}};','\\end{axis}',
       '\\node[font=\\small,anchor=north] at ([yshift=-.75cm]current axis.south) {{\\fontencoding{OT1}\\selectfont Zaman (dk)}};\\node[font=\\small,rotate=90,anchor=south] at ([xshift=-1.0cm]current axis.west) {{\\fontencoding{OT1}\\selectfont İmpuls sayısı (impuls/s)}};']
    return tk('\n'.join(b))
# ---------- impuls kaydı ----------
def impuls(sp,ad,y0,sub=False):
    b=[]
    b.append(f'\\draw[line width=.8pt] (0,{y0+2.1})--(0,{y0-.2});')
    b.append(f'\\draw[line width=1.2pt] (0,{y0}) '+(f'.. controls (1.4,{y0+.02}) and (2,{y0+.38}) .. (3.2,{y0+.4}) .. controls (4.6,{y0+.42}) and (5.4,{y0+.05}) .. (6.4,{y0}) .. controls (7.4,{y0-.02}) and (8,{y0+.28}) .. (9.2,{y0+.3}) .. controls (10.2,{y0+.3}) and (10.8,{y0}) .. (11,{y0});' if sub else
            ''.join((f'-- ({t-.12:.2f},{y0}) -- ({t:.2f},{y0+2.0}) -- ({t+.14:.2f},{y0-.12}) -- ({t+.3:.2f},{y0}) ') for t in sp)+f'-- (11,{y0});'))
    b.append(f'\\node[font=\\normalsize\\bfseries,anchor=east] at (-.15,{y0+.7}) {{{ad}}};')
    return '\n'.join(b)
def impuls_grafik(spL,spM):
    b=[impuls([],'K',0,sub=True),impuls(spL,'L',-3),impuls(spM,'M',-6)]
    b.append('\\draw[dashed,line width=.7pt] (0,1.25)--(11,1.25);\\draw[dashed,line width=.7pt] (0,-1.75)--(11,-1.75);\\draw[dashed,line width=.7pt] (0,-4.75)--(11,-4.75);')
    b.append('\\node[font=\\small,anchor=west] at (11.1,1.25) {eşik};')
    b.append('\\draw[line width=.9pt] (0,-6.4)--(11,-6.4);')
    for t in range(0,11,2): b.append(f'\\draw[line width=.8pt] ({t*1.1:.1f},-6.4)--({t*1.1:.1f},-6.55);\\node[font=\\small] at ({t*1.1:.1f},-6.85) {{{t*10}}};')
    b.append('\\node[font=\\small] at (5.5,-7.7) {Zaman (ms)};')
    return tk('\n'.join(b),.62)

# ===================== 01 · Göz yapıları · kolay · şekilli =====================
SK1=tk(eye({'camsi':'I','kornea':'II','mercek':'III','retina':'IV','iris':'V'}),.9)
Q('0001','yapi','kolay','şekilli','Göz yapıları','Şematik gözde numaralı yapıları tanıyıp kalınlığı değişerek odaklamayı sağlayan yapıyı belirler.',
  'Göz şemasında yapılar konum ve biçimden tanınır; kalınlığı ayarlanabilen tek saydam yapı merceğidir.','Kornea ya da irisi ışığı ayarlayan yapı diye merceğin yerine seçmek.','mercek tanıma',
  [A('Soruyu çözümle','Yakın ve uzak cisimlere bakarken görüntünün retinada net düşmesi için kalınlığı değişen bir yapı aranıyor.','Aranan: kalınlığı değişebilen yapı'),
   A('Yapıları tanı','Gözün önündeki saydam kubbe kornea, renkli halka iris, iki yüzü dışbükey yapı mercek, mercek gerisindeki geniş boşluk camsı cisim, iç tabaka retinadır.','I: camsı cisim · II: kornea · III: mercek · IV: retina · V: iris'),
   A('Kalınlığı değişeni seç','Mercek, silier kasların kasılıp gevşemesiyle kalınlaşıp incelir ve ışığın kırılma miktarını ayarlar.','Kalınlığı değişen yapı: mercek (III)'),
   A('Diğerlerini ele','Kornea sabit eğriliklidir, iris göz bebeğinin çapını ayarlar, camsı cisim gözün şeklini korur, retina ışığı algılar.','Diğer yapıların kalınlığı odaklamak için değişmez')],'C',
  metin='Şekilde insan gözünün bazı yapıları I, II, III, IV ve V ile numaralandırılmıştır.\nBir kişi önce yakındaki bir kitaba, ardından uzaktaki bir dağa baktığında, gözün her iki durumda da net görüntü oluşturabilmesi için kalınlığı değişen yapı numaralandırılmış yapılardan hangisidir?',
  dogru='III',sira=['I','II','III','IV','V'],
  yan=[('I','I numaralı camsı cisim, jelimsi saydam bir sıvıdır ve gözün şeklini korur; kalınlığı bakılan cismin uzaklığına göre değişmez.','bilgi'),
       ('II','II numaralı kornea ışığı kırmaya katkı sağlar ancak eğriliği sabittir; kalınlığı odaklama için değişmez.','bilgi'),
       ('IV','IV numaralı retina ışığa duyarlı reseptörleri taşır; odaklamayı değil ışığın algılanmasını sağlar.','bilgi'),
       ('V','V numaralı iris göz bebeğinin çapını değiştirerek ışık miktarını ayarlar; görüntünün retinaya odaklanmasını sağlayan yapı değildir.','bilgi')],
  istenen='Kalınlığı değişerek odaklamayı sağlayan yapı.',
  ip=['Görüntünün retina üzerinde net oluşması için ışığın kırılma miktarını ayarlayabilen saydam yapıyı bul.'],
  bilgi=[B('Gözün katmanları','göz küresi dışta sert tabaka (ön kısmı saydam kornea), ortada damar tabaka (ön kısmı iris ve göz bebeği), içte retina ile örtülüdür; retinada ışığa duyarlı reseptörler bulunur'),
         B('Saydam ortamlar','kornea, sulu sıvı, mercek ve camsı cisim saydamdır; ışığı kırarak retinaya ulaştırırlar')],
  puf='Kalınlığı ya da eğriliği değişebilen saydam yapı odaklamayı ayarlar; ışık miktarını ayarlayan yapı ise ayrı bir görev üstlenir.',sekil=SK1)

# ===================== 02 · Kulak · kolay · şekilli =====================
SK2=tk(ear({'koklea':'I','zar':'II','ostaki':'III','yarim':'IV','ors':'V'}),.8)
Q('0002','kulak','kolay','şekilli','Kulağın bölümleri','Şematik kulakta numaralı bölümleri tanıyıp işitme reseptörlerinin yerini belirler.',
  'İşitme reseptörleri iç kulakta, sarmal biçimli kokleadaki Korti organındadır.','Yarım daire kanallarını da işitmeyle ilişkilendirmek ya da kemikçiklerde reseptör aramak.','Korti organının yeri',
  [A('Soruyu çözümle','Titreşimi sinir impulsuna çeviren işitme reseptörlerinin yer aldığı bölüm aranıyor.','Aranan: Korti organını içeren bölüm'),
   A('Bölümleri tanı','Kulak yolunun ucundaki zar kulak zarı, orta kulaktaki küçük kemik örs, orta kulağı yutağa bağlayan boru östaki borusu, sarmal yapı koklea, halkalı yapılar yarım daire kanallarıdır.','I: koklea · II: kulak zarı · III: östaki borusu · IV: yarım daire kanalları · V: örs'),
   A('Reseptörün yerini bul','Ses titreşimleri kokleadaki sıvıda dalga oluşturur ve Korti organındaki tüylü hücreler uyarılır.','Korti organı: koklea (I)'),
   A('Diğerlerini ele','Kulak zarı ve örs titreşimi iletir, östaki borusu basıncı dengeler, yarım daire kanalları dengeyle ilgilidir.','Diğer bölümlerde işitme reseptörü yoktur')],'A',
  metin='Şekilde insan kulağının bazı bölümleri I, II, III, IV ve V ile numaralandırılmıştır.\nSes dalgalarının oluşturduğu titreşimleri sinir impulslarına dönüştüren işitme reseptörlerini içeren Korti organı, numaralandırılmış bölümlerden hangisinin içinde yer alır?',
  dogru='I',sira=['I','II','III','IV','V'],
  yan=[('II','II numaralı kulak zarı ses dalgalarıyla titreşir ve bu titreşimi kemikçiklere iletir; reseptör hücre taşımaz.','bilgi'),
       ('III','III numaralı östaki borusu orta kulak ile yutak arasında bağlantı kurarak basıncı dengeler; işitme reseptörü içermez.','bilgi'),
       ('IV','IV numaralı yarım daire kanalları da iç kulaktadır ancak denge reseptörlerini taşır; işitme reseptörleri kokleadadır.','bilgi'),
       ('V','V numaralı örs orta kulaktaki kemikçiklerden biridir; titreşimi iletir ve impuls üretmez.','bilgi')],
  istenen='Korti organının bulunduğu bölüm.',
  ip=['İç kulakta işitmeye ve dengeye ayrılmış iki ayrı yapı vardır; işitmeden sorumlu olanı seç.'],
  bilgi=[B('Kulağın bölümleri','dış kulak kulak kepçesi ve kulak yolundan, orta kulak kulak zarının arkasındaki hava dolu boşluk, üç kemikçik ve östaki borusundan, iç kulak ise sıvı dolu koklea ile yarım daire kanallarından oluşur'),
         B('Reseptör ve impuls','reseptörler aldıkları uyarıyı sinir impulsuna çevirir; impulsu duyu siniri beyindeki ilgili merkeze taşır')],
  puf='İşitme reseptörleri kokleadadır; yarım daire kanallarındaki reseptörler ise dengeyle ilgilidir.',sekil=SK2)

# ===================== 03 · Reseptör–uyarı eşleştirme · kolay · olumsuz =====================
Q('0003','deri','kolay','düz','Reseptör türleri','Duyu reseptörlerini algıladıkları uyarı türüyle eşleştirir ve yanlış eşleştirmeyi bulur.',
  'Her reseptör türü belirli bir uyarıya duyarlıdır: ışık, kimyasal madde, sıcaklık ya da mekanik uyarı.','Yarım daire kanallarının da ses algıladığını sanmak.','reseptör–uyarı',
  [A('Soruyu çözümle','Eşleştirmelerden biri yanlış; yanlış olanı bulmak için her reseptörün uyarı türü ayrı ayrı sınanıyor.','Aranan: yanlış eşleştirme'),
   A('Kimyasal ve ışık reseptörlerini ele','Tat tomurcukları çözünmüş kimyasal maddelere, retinadaki çubuk hücreleri ışığa duyarlıdır.','Tat tomurcuğu: kimyasal · çubuk: ışık'),
   A('Isı ve ses reseptörlerini ele','Deri soğuk reseptörleri sıcaklık değişimini, Korti organındaki tüylü hücreler ses titreşimlerini algılar.','Soğuk reseptörü: sıcaklık · Korti organı: ses'),
   A('Denge reseptörlerini değerlendir','Yarım daire kanalları baş hareketini ve yönünü algılar; ses titreşimlerini algılayan yapı kokleadır.','Yarım daire kanalları: denge, ses değil')],'E',
  metin='Duyu reseptörleri, dış ortamdan ya da vücut içinden gelen uyarıları sinir impulsuna dönüştüren yapılardır ve her reseptör türü belirli bir uyarı çeşidine duyarlıdır.\nBuna göre, aşağıdaki reseptör – algıladığı uyarı eşleştirmelerinden hangisi yanlıştır?',
  dogru='Yarım daire kanallarındaki reseptörler – Ses titreşimleri',
  sira=['Dildeki tat tomurcukları – Suda çözünmüş kimyasal maddeler','Derideki soğuk reseptörleri – Sıcaklık değişimi','Retinadaki çubuk hücreleri – Işık','Korti organındaki tüylü hücreler – Ses titreşimleri','Yarım daire kanallarındaki reseptörler – Ses titreşimleri'],
  yan=[('Dildeki tat tomurcukları – Suda çözünmüş kimyasal maddeler','Bu şıkkı yanlış sanan öğrenci tat reseptörlerinin kimyasal uyarıyı algıladığını bilmemiştir; tat tomurcukları çözünmüş maddelerle uyarılan kemoreseptörlerdir.','bilgi'),
       ('Derideki soğuk reseptörleri – Sıcaklık değişimi','Bu şıkkı yanlış sanan öğrenci deride termoreseptörlerin bulunduğunu hatırlamamıştır; soğuk reseptörleri sıcaklık değişimini algılar.','bilgi'),
       ('Retinadaki çubuk hücreleri – Işık','Bu şıkkı yanlış sanan öğrenci çubukların fotoreseptör olduğunu karıştırmıştır; çubuk hücreleri loş ışığı algılar.','bilgi'),
       ('Korti organındaki tüylü hücreler – Ses titreşimleri','Bu şıkkı yanlış sanan öğrenci Korti organını denge yapısıyla karıştırmıştır; Korti organındaki tüylü hücreler ses titreşimlerini algılar.','bilgi')],
  istenen='Yanlış olan eşleştirme.',
  ip=['Her reseptörün hangi duyu organında bulunduğunu ve o organın işlevini düşünerek eşleştirmeleri sına.'],
  bilgi=[B('Reseptör çeşitleri','fotoreseptörler ışığı, kemoreseptörler kimyasal maddeleri, termoreseptörler sıcaklığı, mekanoreseptörler basınç ve titreşim gibi mekanik uyarıları algılar'),
         B('İç kulakta iki işlev','koklea işitmeden, yarım daire kanalları ve vestibül dengeden sorumludur')],
  puf='Reseptörü bulunduğu yapının işleviyle eşleştir: koklea işitme, yarım daire kanalları denge.')

# ===================== 04 · Işığın yolu · orta · şekilli =====================
SK4=tk(eye({'mercek':'I','camsi':'II','kornea':'III','sulu':'IV','pupil':'V'}),.9)
SIRA4=['III – IV – V – I – II','III – V – IV – I – II','IV – III – V – I – II','III – IV – I – V – II','III – IV – V – II – I']
Q('0004','yapi','orta','şekilli','Işığın izlediği yol','Işığın gözde retinaya ulaşıncaya kadar saydam yapılardan geçiş sırasını şekilden çıkarır.',
  'Işık kornea, sulu sıvı, göz bebeği, mercek ve camsı cisimden geçerek retinaya ulaşır; yapılar şekilde ön–arka konumlarından sıralanır.','Göz bebeğini sulu sıvıdan önce ya da mercekten sonra koymak; camsı cisim ile mercek sırasını karıştırmak.','ışığın yolu',
  [A('Yapıları tanı','Şekilde III gözün ön yüzeyindeki kornea, IV onun arkasındaki sulu sıvı, V irisin ortasındaki açıklık, I iki yüzü dışbükey mercek, II ise mercek gerisindeki camsı cisimdir.','III: kornea · IV: sulu sıvı · V: göz bebeği · I: mercek · II: camsı cisim'),
   A('Konumlarına göre sırala','Işık gözün önünden arkasına ilerlediği için yapıları ön–arka sırasıyla geçer.','Ön yüzeyden retinaya doğru sıra belirlenir'),
   A('Sırayı yaz','Önce kornea, ardından sulu sıvı, iris açıklığı olan göz bebeği, mercek ve en sonda camsı cisim yer alır.','III – IV – V – I – II'),
   A('Şıkları sına','Diğer sıralarda göz bebeği, mercek ya da camsı cisim şekildeki konumlarına aykırı yerlere konmuştur.','Yalnız bir sıra konumlarla uyumludur')],'B',
  metin='Şekilde insan gözünün bazı yapıları I, II, III, IV ve V ile numaralandırılmıştır.\nGözün ön yüzeyine gelen bir ışık ışınının retinaya ulaşıncaya kadar numaralandırılmış yapılardan hangi sırayla geçtiği aşağıdakilerin hangisinde doğru verilmiştir?',
  dogru=SIRA4[0],sira=yer('B',SIRA4[0],SIRA4[1:]),
  yan=[(SIRA4[1],'Bu sırada göz bebeği sulu sıvıdan önce konmuştur; oysa sulu sıvı kornea ile iris arasındadır ve ışık göz bebeğine ulaşmadan önce ondan geçer.','bilgi'),
       (SIRA4[2],'Bu sırada sulu sıvı korneadan önce konmuştur; oysa ışık gözün en dışındaki yapı olan korneadan girer ve sulu sıvıya ondan sonra ulaşır.','dikkat'),
       (SIRA4[3],'Bu sırada göz bebeği mercekten sonra konmuştur; oysa göz bebeği irisin ortasındaki açıklıktır ve mercekten önce yer alır.','bilgi'),
       (SIRA4[4],'Bu sırada camsı cisim mercekten önce konmuştur; oysa camsı cisim merceğin arkasında, retinanın hemen önünde bulunur.','bilgi')],
  istenen='Işığın yapılardan geçiş sırası.',
  ip=['Şekildeki yapıların konumlarına bakarak ışığın gözün önünden arkasına doğru hangi yapıdan hangisine geçtiğini sırala.'],
  bilgi=[B('Işığın kırılması','ışık farklı yoğunluktaki saydam ortamlara geçerken yön değiştirir; gözde kırılma en çok kornea ile mercekte olur ve ışınlar retina üzerinde toplanır'),
         B('Göz bebeği','irisin ortasındaki açıklıktır; ışık bu açıklıktan geçerek gözün iç bölümüne ulaşır')],
  puf='Işığın yolunu gözün ön–arka eksenine göre sırala: ön yüzeyden arkaya doğru yapıların konumu sıralamayı verir.',sekil=SK4)

# ===================== 05 · Retina grafiği · zor · öncüllü =====================
assert koni(0)>140 and cubuk(0)<1 and koni(15)<1 and cubuk(15)<1 and max(cubuk(x/2) for x in range(-120,121))>130 and koni(19)<10 and cubuk(19)>130
SK5=retina_grafik()
O5=onc('Şekilde, insan gözünün retinasında sarı beneğin merkezinden başlayarak yatay doğrultuda ölçülen X ve Y reseptör hücrelerinin yoğunlukları gösterilmiştir. L noktasında görme siniri gözden çıkmaktadır.',
  [('X hücrelerinin bir bölümü farklı dalga boylarındaki ışıklara duyarlıdır.',True,'X hücreleri sarı benekte yoğunlaşan koni hücreleridir; koniler kırmızı, yeşil ve mavi ışığa duyarlı farklı türler içerir.'),
   ('Ortam ışığının çok az olduğu bir odada sarı beneğe düşen görüntü, retinanın diğer bölgelerine düşenden daha net algılanır.',False,'Loş ışıkta çubuk hücreleri görev yapar ve çubuk hücreleri (Y) sarı benekte bulunmaz; bu nedenle loş ışıkta sarı benekteki görüntü daha net algılanmaz.'),
   ('Görüntüsü L noktasına düşen cisim, bu gözle algılanamaz.',True,'L noktasında her iki hücre türünün yoğunluğu sıfırdır; ışığı algılayacak reseptör bulunmayan bu kör noktada görüntü algılanamaz.')],
  'Buna göre, yukarıdaki yargılardan hangileri doğrudur?',['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III'])
assert O5['dogru']=='I ve III'
Q('0005','retina','zor','grafik','Çubuk, koni ve kör nokta','Retina grafiğinden reseptör türlerini belirleyip renk görme, loş ışıkta görme ve kör nokta yargılarını birlikte değerlendirir.',
  'Grafikte sarı benekte yoğunlaşan hücre koni, sarı benek dışında yoğunlaşan çubuktur; reseptör bulunmayan L noktası kör noktadır.','X ile Y’yi ters okumak ya da loş ışıkta en net görmenin sarı benekte olduğunu sanmak.','çubuk–koni grafiği',
  [A('Grafikten hücre türlerini belirle','X sarı beneğin merkezinde çok yoğundur, Y ise merkezde yoktur ve ondan uzakta zirve yapar.','X: koni · Y: çubuk')]+O5['adim']+[A('Sonucu yaz','Doğru olan öncüller I ve III’tür.','Cevap: I ve III')],'D',
  metin=O5['metin'],dogru=O5['dogru'],yan=O5['yan'],sira=O5['sira'],
  istenen='Doğru olan yargılar.',
  ip=['Eğrilerin sarı benekte ve L noktasında aldığı değerlere bakarak X ile Y’nin hangi reseptör türü olduğunu belirle.'],
  bilgi=[B('Çubuk ve koni','retinada çubuk ve koni adı verilen iki tür ışık reseptörü bulunur; çubuklar loş ışıkta, koniler parlak ışıkta görev yapar'),
         B('Kör nokta','görme sinirinin gözden çıktığı bölgede reseptör hücre bulunmaz')],
  puf='Merkezde yoğunlaşan hücre koni, çevrede yoğunlaşan çubuktur; reseptörsüz bölgeye düşen görüntü algılanmaz.',sekil=SK5)

# ===================== 06 · Göz bebeği tablosu · orta · öncüllü =====================
CAP=[('K','Çok az (karanlık oda)',7),('L','Orta (aydınlık oda)',4),('M','Çok fazla (güneşli açık alan)',2)]
assert CAP[0][2]>CAP[1][2]>CAP[2][2] and CAP[0][2]>3*CAP[2][2]
SK6=tablo_svg(['Ortam','Işık düzeyi','Göz bebeği çapı (mm)'],[[a,b,str(c)] for a,b,c in CAP])
O6=onc('Aşağıdaki tabloda, sağlıklı bir bireyin göz bebeği çapı, ışık düzeyleri farklı üç ortamda yaklaşık olarak verilmiştir.',
  [('K ortamındaki göz bebeği çapı, M ortamındakinin üç katından fazladır.',True,'K’da çap 7 mm, M’de 2 mm’dir; M’nin üç katı 6 mm olduğundan 7 mm bundan büyüktür.'),
   ('Işık düzeyi azaldıkça retinaya ulaşan ışık miktarını artırıcı yönde bir ayarlama yapılır.',True,'Tabloda ışık azaldıkça göz bebeği çapı büyümektedir; büyük bir göz bebeği retinaya daha fazla ışık girmesini sağlar.'),
   ('Göz bebeği çapının ışık düzeyine göre değişmesi, retinadaki reseptörlerden başlayıp irisin kaslarına uzanan sinirsel bir yolla gerçekleşir.',True,'Göz bebeğinin ışığa tepkisi bir refleks olup reseptör, duyu nöronu, merkezi sinir sistemi ve irisin kaslarını uyaran nöronları içerir.')],
  'Buna göre, yukarıdaki yargılardan hangileri doğrudur?',['Yalnız I','Yalnız II','I ve II','II ve III','I, II ve III'])
assert O6['dogru']=='I, II ve III'
Q('0006','uyum','orta','tablo','Göz bebeği tepkisi','Tablodaki ışık düzeyi–göz bebeği çapı ilişkisini iris, retinaya ulaşan ışık ve refleks kavramlarıyla yorumlar.',
  'Işık azaldıkça göz bebeği genişler, arttıkça daralır; bu ayar irisle yapılan ve sinirsel yolla gerçekleşen bir reflekstir.','Göz bebeği çapını merceğin ayarladığını sanmak ya da tepkiyi sinir sisteminden bağımsız saymak.','göz bebeği çapı tablosu',
  [A('Tabloyu oku','Işık düzeyi çok az olan K ortamında çap en büyük, ışığı en fazla olan M ortamında en küçüktür.','Çap: K 7 mm · L 4 mm · M 2 mm')]+O6['adim']+[A('Sonucu yaz','Üç öncül de doğrudur.','Cevap: I, II ve III')],'E',
  metin=O6['metin'],dogru=O6['dogru'],yan=O6['yan'],sira=O6['sira'],
  istenen='Doğru olan yargılar.',
  ip=['Tablodaki çap değişiminin yönünü, gözün iç bölümüne giren ışık miktarıyla ve bu ayarı yapan yapıyla ilişkilendir.'],
  bilgi=[B('Göz bebeği','irisin ortasındaki açıklıktır; çapı irisin kasları tarafından değiştirilir'),
         B('Refleks','uyarana verilen ve bilinçli karar gerektirmeyen hızlı tepkidir; reseptör, duyu nöronu, merkezi sinir sistemi ve motor nöronla gerçekleşir')],
  puf='Parlak ışıkta göz bebeği daralır, loş ışıkta genişler; bu ayar iris kaslarıyla yapılan bir reflekstir.',sekil=SK6)

# ===================== 07 · Akomodasyon · orta · olumsuz · şekilli =====================
SK7=tk(mercek(0,True,'I')+mercek(5.2,False,'II')+mercek_etiket(0),.8)
S7=['I numaralı durum, kişi uzaktaki cisme bakarken oluşur.','II numaralı durumda askı bağları gergindir ve mercek daha incedir.','I numaralı durumda silier kaslar kasılmış hâldedir.','II numaralı durumda merceğin ışığı kırma gücü, I numaralı duruma göre daha azdır.','Her iki durumda da cismin görüntüsü retina üzerinde odaklanır.']
Q('0007','uyum','orta','şekilli','Akomodasyon','Yakın ve uzak görmede mercek, silier kas ve askı bağı durumlarını şekilden yorumlar.',
  'Yakına bakarken silier kaslar kasılır, askı bağları gevşer, mercek kalınlaşır; uzağa bakarken tersi olur.','Silier kasların uzağa bakarken kasıldığını sanmak.','akomodasyon durumları',
  [A('Şekli yorumla','I’de mercek kalın, silier kas kasılmış, askı bağları gevşektir; II’de mercek ince ve askı bağları gergindir.','I: kalın mercek · II: ince mercek'),
   A('Durumları cisimle eşle','Kalın mercek ışığı daha çok kırar ve yakın cisimleri odaklar; ince mercek uzak cisimler içindir.','I: yakın cisim · II: uzak cisim'),
   A('İfadeleri sına','İnce mercek, gergin askı bağı, kasılmış silier kas ve kırma gücü karşılaştırması şekille uyumludur; normal bir gözde iki durumda da görüntü retinada netleşir.','Dört ifade doğru'),
   A('Yanlış olanı belirle','I’deki durumun uzak cisme bakarken oluştuğunu söyleyen ifade şekle ve akomodasyon kuralına aykırıdır.','Söylenemeyen: I’in uzağa bakarken oluştuğu')],'A',
  metin='Şekilde, sağlıklı bir kişinin gözündeki merceğin ve çevresindeki yapıların, kişi iki farklı uzaklıktaki cisme bakarken aldığı durumlar I ve II ile gösterilmiştir. Kişi bu cisimlerden birini kendisine çok yakın, diğerini çok uzak tutmuştur.\nBuna göre, bu kişiyle ilgili aşağıdakilerden hangisi söylenemez?',
  dogru=S7[0],sira=S7,
  yan=[(S7[1],'Bu şıkkı yanlış sanan öğrenci ince merceğin askı bağlarının gerilmesiyle oluştuğunu bilmemiştir; şekilde II’de bağlar gergin, mercek incedir ve ifade doğrudur.','bilgi'),
       (S7[2],'Bu şıkkı yanlış sanan öğrenci kalın merceğin silier kasların kasılmasıyla oluştuğunu karıştırmıştır; I’de kaslar kasılmış ve bağlar gevşemiştir, ifade doğrudur.','bilgi'),
       (S7[3],'Bu şıkkı yanlış sanan öğrenci ince merceğin kırma gücünün daha az olduğunu bilmemiştir; mercek inceldikçe ışığı daha az kırar ve ifade doğrudur.','bilgi'),
       (S7[4],'Bu şıkkı yanlış sanan öğrenci sağlıklı gözün iki durumda da odaklama yapabildiğini gözden kaçırmıştır; akomodasyon sayesinde görüntü retina üzerinde netleşir ve ifade doğrudur.','dikkat')],
  istenen='Söylenemeyen ifade.',
  ip=['Şekilde mercek kalınlığını ve askı bağlarının gerginliğini karşılaştırarak her durumu bakılan cismin uzaklığıyla ilişkilendir.'],
  bilgi=[B('Akomodasyon (uyum)','gözün farklı uzaklıktaki cisimleri retinada net odaklayabilmesi için mercek kalınlığının ayarlanmasıdır; silier kaslar ve askı bağları bu ayarı yapar'),
         B('Kırma gücü','merceğin kalınlığı arttıkça ışığı kırma gücü artar ve ışınlar daha kısa mesafede toplanır')],
  puf='Kalın mercek yakına, ince mercek uzağa bakmak içindir; kalınlaşmayı silier kasların kasılması sağlar.',sekil=SK7)

# ===================== 08 · Görme kusurları ışın şeması · orta · öncüllü =====================
FXA,FXB=.65,3.1
assert FXA<R and FXB>R   # X: odak retinanın önünde (miyop), Y: odak retinanın gerisinde (hipermetrop)
SK8=tk(ray_eye(0,FXA,'X')+ray_eye(6.3,FXB,'Y'),.75)
O8=onc('Şekilde X ve Y gözlerine, çok uzaktaki bir cisimden gelen paralel ışık ışınlarının izlediği yol gösterilmiştir. Her iki gözde de merceğin kalınlığı o anda en az düzeydedir.',
  [('X gözünün sahibi uzaktaki cisimleri gözlüksüz net göremez.',True,'X gözünde uzaktan gelen paralel ışınlar retinanın önünde toplanır; mercek daha fazla incelemeyeceği için uzak cisim bulanık görülür.'),
   ('Y gözündeki kusur, ışınları toplayan mercekli gözlükle düzeltilebilir.',True,'Y gözünde ışınlar retinanın gerisinde toplanır; ışınları önceden bir miktar toplayan yakınsak mercek odağı retinaya getirir.'),
   ('X gözündeki kusurun nedeni göz küresinin normalden kısa olmasıdır.',False,'Işınların retinanın önünde toplanması miyopta görülür ve nedeni göz küresinin uzun olması ya da merceğin fazla kalınlaşmasıdır; kısa göz küresi ışınların retinanın gerisinde toplanmasına yol açar.')],
  'Buna göre, yukarıdaki yargılardan hangileri doğrudur?',['Yalnız I','Yalnız II','I ve II','I ve III','II ve III'])
assert O8['dogru']=='I ve II'
Q('0008','kusur','orta','şekilli','Miyop ve hipermetrop','Işın şemasından görme kusurunu belirleyip görme durumunu, gözlük türünü ve nedenini değerlendirir.',
  'Odak retinanın önündeyse miyop (ıraksak mercekle), gerisindeyse hipermetrop (yakınsak mercekle) düzeltilir.','Odak noktasının konumundan kusuru ters çıkarmak ya da gözlük merceğinin türünü karıştırmak.','ışın şeması kusur',
  [A('Odak konumlarını oku','X’te ışınlar retinaya ulaşmadan kesişir, Y’de retinaya ulaştıkları hâlde henüz toplanmamıştır.','X: odak retinanın önünde · Y: odak retinanın gerisinde')]+O8['adim']+[A('Sonucu yaz','Doğru olan öncüller I ve II’dir.','Cevap: I ve II')],'C',
  metin=O8['metin'],dogru=O8['dogru'],yan=O8['yan'],sira=O8['sira'],
  istenen='Doğru olan yargılar.',
  ip=['Odak noktasının retinaya göre konumunu belirle; ardından bu konumu mercek türüyle ve göz küresinin boyuyla ilişkilendir.'],
  bilgi=[B('Görme kusurları','göz küresinin boyu ile merceğin kırma gücü uyumsuz olduğunda ışınlar retina üzerinde değil, önünde ya da gerisinde toplanır ve görüntü bulanık olur'),
         B('Mercek türleri','yakınsak (tümsek) mercek ışınları toplar, ıraksak (çukur) mercek ışınları dağıtır')],
  puf='Odak retinanın önündeyse ışınları dağıtan, gerisindeyse ışınları toplayan mercek gerekir.',sekil=SK8)

# ===================== 09 · Östaki borusu · orta · olumsuz · şekilli =====================
SK9=tk(ear({'zar':'I','uzengi':'II','koklea':'III','ostaki':'IV','yarim':'V'}),.8)
S9=['Orta kulaktaki hava basıncının dış ortam basıncına eşitlenememesi','Korti organındaki reseptör hücrelerinin yapısal olarak bozulması','Kulak zarının iki yüzü arasında basınç farkı oluşması','Kulak zarının titreşme yeteneğinin geçici olarak azalması','İşitme duyusunda geçici bir azalma yaşanması']
Q('0009','kulak','orta','şekilli','Östaki borusu ve basınç','Orta kulak ile yutağı birleştiren yapının tıkanmasının sonuçlarını kulak şeması üzerinden değerlendirir.',
  'Östaki borusu kulak zarının iki yüzündeki basıncı eşitler; tıkanınca orta kulakta basınç dengesi bozulur, iç kulaktaki reseptörler yapısal olarak etkilenmez.','Östaki borusunun tıkanmasını iç kulak reseptörlerinin hasarıyla ilişkilendirmek.','östaki borusu tıkanması',
  [A('Yapıyı tanı','Şekilde IV, orta kulaktan yutağa uzanan östaki borusudur.','IV: östaki borusu'),
   A('İşlevini hatırla','Östaki borusu orta kulaktaki hava basıncını dış ortam basıncına eşitler.','Görev: basınç dengesi'),
   A('Tıkanmanın sonuçlarını yaz','Boru tıkanınca orta kulak basıncı eşitlenemez, kulak zarının iki yüzü arasında basınç farkı oluşur, zar iyi titreşemez ve işitme geçici olarak azalır.','Beklenen: basınç farkı, titreşimde azalma, işitmede azalma'),
   A('Beklenmeyeni bul','Korti organı iç kulaktadır ve borunun tıkanması orta kulaktaki basıncı etkiler; reseptör hücrelerin yapısı bozulmaz.','Beklenmeyen: Korti organındaki yapısal bozulma')],'B',
  metin='Şekilde insan kulağının bazı bölümleri I, II, III, IV ve V ile numaralandırılmıştır. Bir kişide IV numaralı yapı, soğuk algınlığı nedeniyle iltihaplanıp tıkanmıştır ve kişi hava yolculuğu sırasında kulağında dolgunluk hissetmektedir.\nBuna göre, bu kişide aşağıdakilerden hangisinin gerçekleşmesi beklenmez?',
  dogru=S9[1],sira=[S9[0],S9[1],S9[2],S9[3],S9[4]],
  yan=[(S9[0],'Bu şıkkı seçen öğrenci “beklenmez” sözcüğünü gözden kaçırmıştır; borunun tıkanması orta kulak basıncının dış ortamla eşitlenmesini engeller ve bu durum beklenir.','dikkat'),
       (S9[2],'Bu şıkkı seçen öğrenci basınç farkının oluşmayacağını sanmıştır; boru tıkalı olduğundan zarın iki yüzündeki basınç eşitlenemez ve fark oluşur.','bilgi'),
       (S9[3],'Bu şıkkı seçen öğrenci zarın titreşiminin etkilenmeyeceğini sanmıştır; iki yüz arasındaki basınç farkı zarı gererek titreşimini azaltır.','bilgi'),
       (S9[4],'Bu şıkkı seçen öğrenci işitmenin etkilenmeyeceğini sanmıştır; zarın titreşmesi azalınca iç kulağa iletilen titreşim azalır ve işitme geçici olarak düşer.','bilgi')],
  istenen='Beklenmeyen sonuç.',
  ip=['IV numaralı yapının birbirine bağladığı bölgeleri bul ve tıkanmanın hangi bölgedeki basıncı etkilediğini düşün.'],
  bilgi=[B('Orta kulak ve basınç','orta kulak, östaki borusuyla yutağa bağlanan hava dolu bir boşluktur; bu bağlantı kulak zarının iki yüzündeki hava basıncının eşitlenmesini sağlar'),
         B('Kulak zarı','iki yüzündeki basınç eşit olduğunda en iyi titreşir; basınç farkı titreşimini sınırlar')],
  puf='Bir yapının tıkanması ya da bozulması önce o yapının görevini, sonra o göreve bağlı yapıları etkiler; sonuçları bu zincirle sırala.',sekil=SK9)
# yarım daire ve koklea şıkları aynı yönde yorumlanmasın: B şıkkı doğru (beklenmeyen) – harf B

# ===================== 10 · İşitme kayıpları · orta · öncüllü =====================
O10=onc('İşitme kaybının nedeni hasarlı yapıya göre değişir. K kişisinde kulak zarı delinmiş, L kişisinde orta kulaktaki üç kemikçik birbirine kaynamış, M kişisinde ise kokleadaki reseptör hücreler hasar görmüştür.',
  [('K’da ses dalgalarının orta kulağa aktarılması aksar.',True,'Delinmiş kulak zarı ses dalgalarıyla etkin biçimde titreşemez; bu nedenle titreşimlerin kemikçiklere aktarılması aksar.'),
   ('L’de kemikçikler titreşimleri iç kulağa etkin biçimde iletemez.',True,'Kaynaşmış kemikçikler serbestçe hareket edemez; kulak zarındaki titreşimi oval pencereye aktarma işlevi bozulur.'),
   ('M’deki işitme kaybı, titreşimlerin iç kulağa iletilmesindeki aksamadan kaynaklanır.',False,'M’de titreşimler iç kulağa ulaşır; sorun titreşimi impulsa çeviren reseptör hücrelerin hasarlı olmasıdır, yani kayıp iletimle değil reseptörle ilgilidir.')],
  'Buna göre, yukarıdaki yargılardan hangileri doğrudur?',['Yalnız I','Yalnız II','Yalnız III','I ve II','I, II ve III'])
assert O10['dogru']=='I ve II'
Q('0010','isitme','orta','öncüllü','İletim ve reseptör kaynaklı kayıplar','Kulak zarı, kemikçik ve koklea hasarlarının işitmeyi nasıl etkilediğini iletim ve impuls oluşumu açısından değerlendirir.',
  'Kulak zarı ve kemikçikler titreşimi iletir; koklea reseptörleri titreşimi impulsa çevirir; hasar yeri kaybın türünü belirler.','Koklea reseptörlerindeki hasarı da iletim sorunu sanmak.','işitme kaybı türleri',
  [A('Yapıların görevini hatırla','Kulak zarı ve kemikçikler mekanik titreşimi iletir; koklea reseptörleri titreşimi impulsa çevirir.','İletim: zar, kemikçik · impuls: koklea')]+O10['adim']+[A('Sonucu yaz','Doğru olan öncüller I ve II’dir.','Cevap: I ve II')],'D',
  metin=O10['metin'],dogru=O10['dogru'],yan=O10['yan'],sira=O10['sira'],
  istenen='Doğru olan yargılar.',
  ip=['Her kişide hasarlı yapının titreşimi iletmekle mi yoksa impulsa çevirmekle mi görevli olduğunu ayır.'],
  bilgi=[B('Ses yolu','ses dalgaları kulak zarını titreştirir, titreşim orta kulaktaki üç kemikçikle iç kulağa aktarılır, kokleadaki reseptör hücreler uyarılır ve impuls işitme siniriyle beyne iletilir')],
  puf='Zar ve kemikçik hasarı titreşim iletimini, koklea reseptör hasarı impuls oluşumunu bozar.')

# ===================== 11 · Deri · orta · şekilli =====================
SK11=tk(skin({'hipo':'I','epi':'II','kilkok':'III','ter':'IV','dermis':'V'}),.85)
Q('0011','deri','orta','şekilli','Derinin tabakaları','Deri kesitinde tabakaları ve yapıları tanıyıp reseptör uçlarının, kıl köklerinin ve ter bezlerinin bulunduğu tabakayı belirler.',
  'Dermis; sinir uçları, kan damarları, kıl kökleri ve ter bezlerini içeren canlı hücreli tabakadır.','Yüzeydeki epidermisi ya da yağ dokusunu içeren hipodermisi reseptörlerin asıl tabakası sanmak.','dermis',
  [A('Soruyu çözümle','Reseptör sinir uçları, kıl kökleri, ter bezleri ve kan damarlarının birlikte bulunduğu tabaka aranıyor.','Aranan: bir tabaka'),
   A('Şekli tanı','I yağ hücreleriyle dolu hipodermis, II en üstteki ince epidermis, III kıl kökü, IV kangal biçimli ter bezi, V ikisinin arasında kalan geniş dermistir.','I: hipodermis · II: epidermis · III: kıl kökü · IV: ter bezi · V: dermis'),
   A('Tabakayı seç','Kıl kökü ve ter bezi tabaka değil, tabaka içindeki yapılardır; bunları ve sinir uçlarıyla damarları barındıran tabaka dermistir.','Tabaka: dermis (V)'),
   A('Diğerlerini ele','Epidermis dış tabakadır ve kan damarı içermez; hipodermis yağ dokusu bakımından zengindir.','Diğer tabakalar bu tanıma uymaz')],'E',
  metin='Şekilde insan derisinin kesiti gösterilmiş ve bazı bölümleri numaralandırılmıştır.\nDokunma, basınç ve sıcaklık gibi uyarıları algılayan reseptörlerin sinir uçlarının, kıl köklerinin, ter bezlerinin ve kan damarlarının birlikte bulunduğu canlı hücrelerden oluşan tabaka, numaralandırılmış bölümlerden hangisidir?',
  dogru='V',sira=['I','II','III','IV','V'],
  yan=[('I','I numaralı hipodermis yağ hücrelerinden zengin, ısı yalıtımı ve enerji depolamayla ilişkili alt tabakadır; sorudaki yapıların birlikte bulunduğu tabaka değildir.','bilgi'),
       ('II','II numaralı epidermis deri yüzeyindeki tabakadır ve kan damarı içermez; kıl kökleri ile ter bezleri bu tabakanın altında yer alır.','bilgi'),
       ('III','III numaralı kıl kökü tek bir yapıdır ve soru bir tabakayı sormaktadır; kıl kökü ise aranan tabakanın içinde bulunur.','dikkat'),
       ('IV','IV numaralı ter bezi tek bir yapıdır ve soru bir tabakayı sormaktadır; ter bezi ise aranan tabakanın içinde bulunur.','dikkat')],
  istenen='Sorudaki yapıların birlikte bulunduğu tabaka.',
  ip=['Soru bir tabakayı soruyor; deri tabakalarını dıştan içe sırala ve yalnızca tabaka olan numaraları değerlendir.'],
  bilgi=[B('Derinin tabakaları','deri dıştan içe epidermis, dermis ve hipodermis tabakalarından oluşur; epidermisin dış kısmı ölü hücrelerle örtülüdür'),
         B('Deride duyu','deride dokunma, basınç, sıcaklık ve ağrı reseptörleri bulunur ve bu reseptörler sinir uçlarıyla bağlantılıdır')],
  puf='Soruda bir tabaka isteniyorsa tek yapıları (kıl, bez) değil, onları barındıran tabakaları değerlendir.',sekil=SK11)

# ===================== 12 · İki nokta ayrımı · orta · öncüllü · tablo =====================
IKI=[('Parmak ucu',3),('Avuç içi',12),('Ön kol',38),('Sırt',45)]
assert IKI[0][1]<IKI[3][1] and IKI[2][1]>IKI[1][1] and len(set(v for k,v in IKI))==4
SK12=tablo_svg(['Vücut bölgesi','İki noktayı ayrı hissetme eşiği (mm)'],[[a,str(b)] for a,b in IKI])
O12=onc('Bir araştırmada gönüllülerin gözleri kapatılmış ve derilerine aynı anda iki ince uç değdirilmiştir. Uçlar arasındaki uzaklık değiştirilerek kişinin iki noktayı ayrı hissedebildiği en küçük uzaklık farklı vücut bölgelerinde ölçülmüş ve tabloda verilmiştir.',
  [('Parmak ucunda birim alandaki dokunma reseptörü sayısı, sırttakinden fazladır.',True,'Parmak ucunda iki noktayı ayırmak için gereken uzaklık sırttakinden çok daha küçüktür; bu da birim alanda daha fazla reseptör bulunduğunu gösterir.'),
   ('Ön koldaki dokunma duyusu, avuç içindekinden daha keskindir.',False,'Ön kolda iki noktayı ayırt etmek için gereken uzaklık avuç içindekinden büyüktür; bu nedenle ön koldaki dokunma duyusu avuç içindekinden daha az keskindir.'),
   ('Dokunma reseptörlerinin deri üzerindeki dağılımı, ölçülen tüm bölgelerde eşittir.',False,'Eşik değerleri bölgelere göre farklıdır; reseptörler deri üzerinde eşit dağılmaz ve bazı bölgelerde yoğunlaşır.')],
  'Buna göre, yukarıdaki yargılardan hangileri doğrudur?',['Yalnız I','Yalnız II','I ve II','I ve III','II ve III'])
assert O12['dogru']=='Yalnız I'
Q('0012','deri','orta','tablo','Dokunma reseptörlerinin dağılımı','Tablodaki eşik değerlerinden reseptör yoğunluğu ve duyu keskinliği çıkarımı yapar.',
  'İki noktayı ayırma eşiği küçüldükçe birim alandaki reseptör sayısı ve duyu keskinliği artar.','Eşiği büyük bölgenin duyusunu daha keskin sanmak ya da reseptörlerin eşit dağıldığını düşünmek.','iki nokta ayrımı',
  [A('Tabloyu oku','Eşik parmak ucunda en küçük, sırtta en büyüktür; ön kolda avuç içinden büyüktür.','Eşik: parmak ucu < avuç içi < ön kol < sırt')]+O12['adim']+[A('Sonucu yaz','Yalnızca ilk öncül doğrudur.','Cevap: Yalnız I')],'A',
  metin=O12['metin'],dogru=O12['dogru'],yan=O12['yan'],sira=O12['sira'],
  istenen='Doğru olan yargılar.',
  ip=['Eşik değeri küçük olan bölgede iki ucu ayırt edebilmek için reseptörlerin birbirine daha yakın mı yoksa uzak mı olması gerektiğini düşün.'],
  bilgi=[B('Dokunma reseptörleri','derideki mekanoreseptörler dokunma ve basıncı algılar; sayıları ve yoğunlukları deri bölgelerine göre farklılık gösterir')],
  puf='İki noktayı ayırma eşiği ne kadar küçükse o bölgede reseptörler o kadar sıktır.',sekil=SK12)

# ===================== 13 · Koku adaptasyonu · orta · öncüllü · grafik =====================
assert koku(.4)>koku(2)>koku(4.9)>0 and koku(5)==0 and koku(7)==0 and koku(.1)==0
SK13=koku_grafik()
O13=onc('Bir koku reseptöründen, ortama belirli bir koku maddesi verildiğinde ve bir süre sonra bu madde ortamdan uzaklaştırıldığında kaydedilen impuls sayısı grafikte gösterilmiştir. Koku maddesinin derişimi, ortamda bulunduğu sürece sabit tutulmuştur.',
  [('1–5. dakikalar arasında impuls sayısındaki azalma, reseptörün sürekli uyarılması sonucu duyarlılığının düşmesiyle açıklanabilir.',True,'Uyaran sabitken impuls sayısının azalması reseptörün aynı uyarana alışması, yani duyarlılığının düşmesidir.'),
   ('Koku maddesi ortamdan uzaklaştırıldıktan sonra reseptörde impuls oluşmaz.',True,'Grafikte koku maddesi kalktıktan sonra impuls sayısı sıfırdır; reseptör uyarılmadığı için impuls üretmez.'),
   ('Koku maddesi ortamda bulunduğu sürece beyin kokuyu aynı şiddette algılar.',False,'Reseptörden beyne giden impuls sayısı azaldığı için koku algısı zamanla zayıflar; beyin kokuyu aynı şiddette algılamaz.')],
  'Buna göre, yukarıdaki yargılardan hangileri doğrudur?',['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III'])
assert O13['dogru']=='I ve II'
Q('0013','kemo','orta','grafik','Koku reseptörleri ve adaptasyon','Sabit uyarana karşı impuls sayısının azalmasını adaptasyon kavramıyla yorumlar.',
  'Sabit bir uyaran sürerken reseptörün tepkisi azalır (adaptasyon); uyaran kalkınca impuls oluşmaz.','Azalan impulsu uyaranın ortamdan kalktığı biçiminde yorumlamak.','koku adaptasyonu',
  [A('Grafiği oku','Koku verilince impuls sayısı hızla en yüksek değere çıkar, uyaran sürerken azalır ve koku kalkınca sıfıra düşer.','Zirve, ardından azalma, sonra sıfır')]+O13['adim']+[A('Sonucu yaz','Doğru olan öncüller I ve II’dir.','Cevap: I ve II')],'C',
  metin=O13['metin'],dogru=O13['dogru'],yan=O13['yan'],sira=O13['sira'],
  istenen='Doğru olan yargılar.',
  ip=['Koku maddesi ortamdayken impuls sayısının zamanla değişimini, uyaran sabit olduğu için hangi olayla açıklayabileceğini düşün.'],
  bilgi=[B('Adaptasyon','reseptörlerin aynı uyarana uzun süre maruz kalmasıyla ortaya çıkan tepki değişimidir. Örnek: koldaki saatin bir süre sonra hissedilmemesi'),
         B('Koku reseptörleri','burun boşluğunun üst kısmındaki kemoreseptörlerdir; havadaki kimyasal maddelerle uyarılırlar')],
  puf='Uyaran sabitken tepkinin azalması adaptasyonu, uyaran kalkınca tepkinin kesilmesi reseptörün uyarılmadığını gösterir.',sekil=SK13)

# ===================== 14 · Nezle ve tat · orta · olumsuz =====================
S14=['Yiyeceklerdeki kimyasal maddeler, burun boşluğundaki koku reseptörlerine daha az ulaşmaktadır.','Burun tıkalı olduğu için dildeki tat reseptörleri uyarılamaz hâle gelmiştir.','Yemeğin tadı olarak algılanan duyu, tat ve koku reseptörlerinden gelen impulsların beyinde birlikte değerlendirilmesiyle oluşur.','Dildeki tat tomurcukları, suda çözünmüş maddelerle uyarılır.','Koku reseptörlerinden gelen impulslardaki azalma, lezzet algısının zayıflamasına katkıda bulunur.']
Q('0014','kemo','orta','hikâyeli','Tat ve koku birlikteliği','Tat ve koku duyularının birlikte çalışmasını nezle örneğiyle yorumlar.',
  'Lezzet algısı tat ve koku reseptörlerinden gelen impulsların birlikte yorumlanmasıyla oluşur; burun tıkanınca yalnız koku katkısı azalır, tat reseptörleri çalışmaya devam eder.','Burun tıkanıklığının tat reseptörlerini de işlevsiz bıraktığını sanmak.','nezle ve lezzet algısı',
  [A('Olayı yorumla','Nezlede burun tıkandığı için koku reseptörlerine ulaşan madde azalır ve yemeğin tadı zayıf algılanır.','Azalan: koku girdisi'),
   A('Doğru ifadeleri ayıkla','Kimyasal maddelerin koku reseptörlerine az ulaşması, lezzetin tat ve kokunun birleşimiyle oluşması, tat tomurcuklarının çözünmüş maddelerle uyarılması ve koku impulslarındaki azalmanın lezzeti zayıflatması doğrudur.','Dört ifade doğru'),
   A('Tat reseptörlerini değerlendir','Dildeki tat reseptörleri burunla ilişkisiz çalışır; burun tıkanması onları işlevsiz yapmaz, yalnız koku katkısını azaltır.','Tat reseptörleri çalışmaya devam eder'),
   A('Söylenemeyeni belirle','Tat reseptörlerinin uyarılamaz hâle geldiğini söyleyen ifade yanlıştır.','Söylenemeyen: tat reseptörlerinin işlevsizleşmesi')],'B',
  metin='Nezle olan Deniz, burnu tıkalı olduğu günlerde yemeklerin tadını normalden daha az aldığını fark etmiştir.\nBuna göre, Deniz’le ilgili aşağıdakilerden hangisi söylenemez?',
  dogru=S14[1],sira=S14,
  yan=[(S14[0],'Bu şıkkı yanlış sanan öğrenci burun tıkanıklığının koku reseptörlerine ulaşan maddeyi azalttığını gözden kaçırmıştır; ifade doğrudur.','dikkat'),
       (S14[2],'Bu şıkkı yanlış sanan öğrenci lezzetin tek bir duyudan geldiğini sanmıştır; lezzet tat ve koku impulslarının birlikte yorumlanmasıyla oluşur ve ifade doğrudur.','bilgi'),
       (S14[3],'Bu şıkkı yanlış sanan öğrenci tat reseptörlerinin kimyasal uyarana duyarlı olduğunu bilmemiştir; tat tomurcukları çözünmüş maddelerle uyarılır ve ifade doğrudur.','bilgi'),
       (S14[4],'Bu şıkkı yanlış sanan öğrenci koku girdisinin lezzet algısına katkısını küçümsemiştir; koku impulsları azalınca lezzet algısı zayıflar ve ifade doğrudur.','bilgi')],
  istenen='Söylenemeyen ifade.',
  ip=['Burun tıkanıklığının hangi duyu reseptörlerine ulaşan maddeyi azalttığını ve hangi reseptörlerin bundan bağımsız çalıştığını ayır.'],
  bilgi=[B('Tat ve koku reseptörleri','ikisi de kemoreseptördür: tat tomurcukları dilde, koku reseptörleri burun boşluğunda yer alır ve çözünmüş ya da gaz hâlindeki kimyasal maddelerle uyarılır'),
         B('Lezzet algısı','tat ve koku reseptörlerinden gelen impulslar beyinde birlikte değerlendirilir')],
  puf='Burun tıkanınca yalnız koku girdisi azalır; tat reseptörleri çalışmaya devam eder.')

# ===================== 15 · Ses yolu sırası · orta · şekilli =====================
SK15=tk(ear({'zar':'K','ostaki':'L','ors':'M','uzengi':'N','koklea':'P'}),.8)
S15=['K – M – N – P','K – N – M – P','M – K – N – P','K – M – P – N','P – K – M – N']
Q('0015','kulak','orta','şekilli','Sesin izlediği yol','Kulak şemasında harfle verilen yapıların ses titreşimini iletme sırasını belirler.',
  'Titreşim kulak zarından başlayıp kemikçik zinciriyle iç kulağa aktarılır ve kokleadaki reseptörlerde impulsa dönüşür.','Kemikçiklerin sırasını ya da kokleanın konumunu karıştırmak.','ses yolu sırası',
  [A('Yapıları tanı','Şekilde K kulak yolunun ucundaki zar, M ve N orta kulaktaki iki kemikçik (örs ve üzengi), P sarmal koklea, L ise orta kulağı yutağa bağlayan borudur.','K: kulak zarı · M: örs · N: üzengi · P: koklea · L: östaki borusu'),
   A('Titreşimin yolunu çiz','Ses dalgaları önce zarı titreştirir; titreşim kemikçik zincirinde örsten üzengiye, oradan iç kulaktaki kokleaya geçer.','Zar, örs, üzengi, koklea'),
   A('Borunun rolünü ele','Östaki borusu titreşim iletmez, basıncı dengeler; bu nedenle sıralamada yer almaz.','L sıralamada yok'),
   A('Sırayı yaz','Zarla başlayan, örs ve üzengiyle sürüp kokleayla biten sıra doğrudur.','K – M – N – P')],'D',
  metin='Şekilde insan kulağının bazı bölümleri K, L, M, N ve P harfleriyle gösterilmiştir.\nDış ortamdan gelen ses dalgalarının oluşturduğu titreşim, impulsa dönüşünceye kadar şekildeki yapılardan (titreşimi iletmeyen yapı sıralamaya alınmamıştır) hangi sırayla ilerler?',
  dogru=S15[0],sira=yer('D',S15[0],S15[1:]),
  yan=[(S15[1],'Bu sırada üzengi örsten önce konmuştur; oysa kemikçik zincirinde titreşim önce örse, sonra üzengiye geçer.','bilgi'),
       (S15[2],'Bu sırada örs kulak zarından önce konmuştur; oysa titreşim ilk olarak kulak zarında oluşur.','bilgi'),
       (S15[3],'Bu sırada koklea üzengiden önce konmuştur; oysa kemikçik zinciri titreşimi iç kulaktaki kokleaya aktarır.','bilgi'),
       (S15[4],'Bu sırada koklea en başa konmuştur; oysa kokleadaki reseptörler titreşimin ulaştığı son basamaktır.','bilgi')],
  istenen='Titreşimin yapılardan geçiş sırası.',
  ip=['Titreşimin dış kulaktan iç kulağa doğru hangi yapıdan hangisine aktarıldığını şekildeki konumlara bakarak sırala.'],
  bilgi=[B('Ses yolu','ses dalgaları dış ortamdan kulak yoluna girer; titreşimin iç kulağa ulaşması için orta kulaktaki yapılar da görev yapar')],
  puf='Sıralamada titreşimi taşıyan yapıları dıştan içe doğru konumlarına göre diz.',sekil=SK15)

# ===================== 16 · Reseptör uyarısı ve impuls · zor · öncüllü · grafik =====================
SPL=[1.2,5.0,8.8]; SPM=[0.8,2.2,3.6,5.0,6.4,7.8,9.2,10.4]
assert len(SPL)==3 and len(SPM)==8 and len(SPM)>len(SPL)
SK16=impuls_grafik(SPL,SPM)
O16=onc('Bir reseptör hücresine bağlı duyu nöronundan, üç farklı şiddette uyarı uygulandığında kaydedilen impulslar şekilde gösterilmiştir. Uyarı şiddeti K’da 1, L’de 4, M’de 8 birimdir ve her kayıt 100 milisaniye sürmüştür.',
  [('K’daki uyarı, nöronda impuls oluşturacak eşik değerin altındadır.',True,'K kaydında impuls yoktur ve gerilim eşik çizgisine ulaşmaz; uyarı eşik değerin altında kaldığı için impuls oluşmamıştır.'),
   ('M’de impuls sayısının L’den fazla olması, impuls genliğinin artmasıyla sağlanmıştır.',False,'L ve M’deki impulsların yükseklikleri aynıdır; uyarı şiddeti arttıkça impulsun genliği değişmez, yalnız impuls sayısı artar.'),
   ('Eşik değerin üzerindeki uyarılarda, uyarı şiddeti arttıkça aynı sürede oluşan impuls sayısı artar.',True,'Kayıtta 100 milisaniyede L’de 3, M’de 8 impuls vardır; uyarı şiddeti arttıkça aynı sürede oluşan impuls sayısı artmıştır.')],
  'Buna göre, yukarıdaki yargılardan hangileri doğrudur?',['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III'])
assert O16['dogru']=='I ve III'
Q('0016','impuls','zor','grafik','Eşik değer ve impuls sıklığı','İmpuls kaydından eşik değeri, impuls genliğinin sabitliğini ve uyarı şiddetinin impuls sıklığıyla kodlanmasını birlikte yorumlar.',
  'Eşik altı uyarı impuls oluşturmaz; eşiği aşan uyarılarda impuls genliği sabittir, şiddet arttıkça impuls sıklığı artar.','Uyarı şiddetiyle impulsun genliğinin de arttığını sanmak.','impuls sıklığı ve genlik',
  [A('Kayıtları oku','K’da impuls yoktur, L’de üç, M’de sekiz impuls vardır ve L ile M’deki impulsların yükseklikleri aynıdır.','K: 0 · L: 3 · M: 8 impuls')]+O16['adim']+[A('Sonucu yaz','Doğru olan öncüller I ve III’tür.','Cevap: I ve III')],'E',
  metin=O16['metin'],dogru=O16['dogru'],yan=O16['yan'],sira=O16['sira'],
  istenen='Doğru olan yargılar.',
  ip=['Kayıtlarda impulsların yüksekliğini ve aynı sürede kaç tane oluştuğunu uyarı şiddetiyle karşılaştır.'],
  bilgi=[B('Eşik değer','bir uyarının impuls oluşturabilmesi için ulaşması gereken en küçük şiddettir; eşik altı uyarılar impuls oluşturmaz'),
         B('İmpuls oluşumu','nöronda impuls oluşabilmesi için uyarının eşik değere ulaşması gerekir; impuls oluşumunda “ya hep ya hiç” kuralı geçerlidir')],
  puf='Uyarı şiddeti impulsun büyüklüğüne değil, sıklığına yansır; eşik altındaki uyarı hiç impuls oluşturmaz.',sekil=SK16)

# ===================== 17 · Odak konumu ve akomodasyon · zor · olumsuz =====================
S17=['L’nin görme kusurunu düzeltmek için ışınları toplayan (yakınsak) mercekli gözlük kullanılması gerekir.','K’nın 30 cm uzaklıktaki kitabı net görebilmesi için silier kaslarının kasılması gerekir.','M, 6 m uzaklıktaki cismi net görebilmek için merceğini kalınlaştırabilir.','M için 30 cm uzaklıktaki kitabı netleştirmek, 6 m uzaklıktaki cismi netleştirmekten daha fazla mercek kalınlaşması gerektirir.','L’nin merceği zaten en ince durumdayken ışınlar retinanın önünde toplandığı için 6 m uzaklıktaki cisim gözlüksüz bulanık görülür.']
Q('0017','kusur','zor','yeni nesil','Kusur ve akomodasyon','Odak konumuna göre görme kusurunu belirleyip akomodasyon ve gözlük merceği türü yargılarını birlikte değerlendirir.',
  'Odak retinanın önündeyse miyop, gerisindeyse hipermetroptur; yakına bakmak merceğin kalınlaşmasını gerektirir ve hipermetrop göz uzağa bakarken bile akomodasyon yapabilir.','Miyop gözün düzeltilmesinde yakınsak mercek seçmek ya da hipermetrop gözün uzağa bakarken uyum yapamadığını sanmak.','kusur + akomodasyon',
  [A('Kusurları belirle','Silier kaslar gevşekken odak K’da retinada, L’de önünde, M’de gerisindedir.','K: normal · L: miyop · M: hipermetrop'),
   A('Gözlük merceklerini değerlendir','Miyopta ışınların retinanın önünde toplanması, ışınları dağıtan ıraksak mercekle düzeltilir; toplayan mercek odağı daha da öne çeker.','L: ıraksak mercek gerekir'),
   A('Akomodasyonu değerlendir','Yakın cisme bakmak ve hipermetrop gözün odağı retinaya getirmesi merceğin kalınlaşmasını gerektirir; L’de mercek zaten en incedir.','K, M ve L için akomodasyon ifadeleri doğru'),
   A('Söylenemeyeni belirle','L için toplayıcı mercek önerisi yanlıştır.','Söylenemeyen: L için yakınsak mercek')],'A',
  metin='K, L ve M kişilerinin gözlerinde, silier kasları gevşekken 6 m uzaklıktaki bir cisimden gelen ışınların odaklandığı yer şöyledir: K’da retina üzerinde, L’de retinanın önünde, M’de retinanın gerisinde. Üç kişi de gözlüksüz hâlde 30 cm uzaklıktaki bir kitaba bakmaya çalışmaktadır.\nBuna göre, aşağıdakilerden hangisi söylenemez?',
  dogru=S17[0],sira=S17,
  yan=[(S17[1],'Bu şıkkı yanlış sanan öğrenci yakına bakarken silier kasların gevşediğini sanmıştır; yakın cisim için mercek kalınlaşır, bunu silier kasların kasılması sağlar ve ifade doğrudur.','bilgi'),
       (S17[2],'Bu şıkkı yanlış sanan öğrenci hipermetrop gözün uzağa bakarken uyum yapamayacağını sanmıştır; mercek kalınlaşınca odak retinaya yaklaşır ve ifade doğrudur.','bilgi'),
       (S17[3],'Bu şıkkı yanlış sanan öğrenci yakın cismin ek uyum gerektirdiğini gözden kaçırmıştır; M, uzak cisim için bile uyum yaparken yakın cisim için daha fazla kalınlaştırması gerekir ve ifade doğrudur.','bilgi'),
       (S17[4],'Bu şıkkı yanlış sanan öğrenci miyop gözde merceğin daha fazla incelemeyeceğini gözden kaçırmıştır; L’de odak retinanın önünde kaldığı için uzak cisim bulanık görülür ve ifade doğrudur.','bilgi')],
  istenen='Söylenemeyen ifade.',
  ip=['Her kişi için odağın retinaya göre konumundan kusuru belirle; ardından uzak ve yakın cisimler için mercek kalınlığının nasıl değişmesi gerektiğini düşün.'],
  bilgi=[B('Odak konumu ve kusur','ışınlar silier kaslar gevşekken retinanın önünde toplanıyorsa miyop, gerisinde toplanıyorsa hipermetrop söz konusudur'),
         B('Akomodasyon','yakın cisme bakarken silier kaslar kasılır ve mercek kalınlaşır; kalınlaşan mercek ışınları daha çok kırar')],
  puf='Kusuru odak konumundan belirle: önünde miyop (ıraksak mercek), gerisinde hipermetrop (yakınsak mercek); yakına bakmak her zaman kalınlaşma ister.')

# ===================== 18 · Denge · orta · hikâyeli =====================
S18=['Orta kulaktaki kemikçiklerin titreşiminin durmasının zaman alması','Östaki borusu ile dış ortam arasında basınç farkı oluşması','Yarım daire kanallarındaki sıvının hareketini bir süre sürdürerek denge reseptörlerini uyarması','Korti organındaki tüylü hücrelerin dönme yönünü algılaması','Retinadaki reseptörlerin ışık olmadığı hâlde impuls üretmeye devam etmesi']
Q('0018','kulak','orta','hikâyeli','Denge ve yarım daire kanalları','Dönme sonrası baş dönmesini iç kulaktaki denge yapısının işleviyle açıklar.',
  'Yarım daire kanalları baş hareketini ve dönmeyi algılar; kanaldaki sıvı hareket durduktan sonra bir süre akmaya devam eder.','Dönme hissini işitme yapılarına ya da göze bağlamak.','dönme sonrası baş dönmesi',
  [A('Olayı yorumla','Kişi gözleri kapalı olduğu hâlde, sandalye durunca dönme hissini sürdürmektedir; bu his görmeden gelmez.','Aranan: denge algısını sürdüren yapı'),
   A('Dönmeyi algılayan yapıyı bul','Baş hareketini ve dönmeyi iç kulaktaki yarım daire kanalları algılar; kanallardaki sıvı hareket edince reseptörler uyarılır.','Dönme algısı: yarım daire kanalları'),
   A('Neden durmadığını açıkla','Sandalye durunca kanallardaki sıvı bir süre hareketine devam eder ve reseptörleri uyarmayı sürdürür.','Sonuç: dönme hissi sürer'),
   A('Diğer şıkları ele','Kemikçikler ve östaki borusu işitmeyle ilgili iletim yapılarıdır, Korti organı sesi algılar, retina ışığı algılar.','Bu yapılar dönme algısıyla ilgili değildir')],'C',
  metin='Dönen bir sandalyede gözleri kapalı oturan bir kişi, sandalye aniden durdurulduktan sonra bir süre daha dönüyormuş gibi hissetmektedir.\nBu durumun nedeni aşağıdakilerden hangisidir?',
  dogru=S18[2],sira=S18,
  yan=[(S18[0],'Bu şıkkı seçen öğrenci kemikçikleri denge işleviyle ilişkilendirmiştir; kemikçikler yalnız ses titreşimini iletir ve dönme algısında rol almaz.','bilgi'),
       (S18[1],'Bu şıkkı seçen öğrenci basınç dengesini dönme algısıyla karıştırmıştır; östaki borusu orta kulakla yutak arasında basıncı dengeler ve dönme hissine yol açmaz.','bilgi'),
       (S18[3],'Bu şıkkı seçen öğrenci Korti organını denge reseptörü sanmıştır; Korti organındaki tüylü hücreler ses titreşimlerini algılar, dönme yönünü değil.','bilgi'),
       (S18[4],'Bu şıkkı seçen öğrenci dönme hissini görmeyle ilişkilendirmiştir; gözler kapalıyken ışık reseptörleri dönme algısı oluşturmaz.','dikkat')],
  istenen='Dönme hissinin sürmesinin nedeni.',
  ip=['Gözler kapalıyken dönme ve baş hareketi bilgisini hangi iç kulak yapısının algıladığını düşün.'],
  bilgi=[B('İç kulakta denge','iç kulaktaki yarım daire kanalları ve vestibül baş hareketini ve vücut dengesini algılayan reseptörleri taşır; bu yapılar işitmede rol almaz')],
  puf='Dönme ve baş hareketi yarım daire kanallarındaki sıvı ve reseptörlerle algılanır; ses ise kokleada algılanır.')

# ===================== 19 · Tat–koku deneyi · zor · yeni nesil =====================
S19=['Tat reseptörleri yalnızca burun açıkken işlev görebilir.','Koku reseptörleri yalnızca gaz hâlindeki maddelerle, tat reseptörleri yalnızca katı maddelerle uyarılır.','Tat tomurcukları, iki ayrı gıda maddesinin ayırt edilmesinde hiçbir şekilde kullanılamaz.','Bu üç gıdanın birbirinden ayırt edilmesinde koku duyusunun katkısı, tat duyusunun katkısından daha fazladır.','Gözler bağlı olduğu hâlde görme duyusu üç durumda da ayırt etmeye katkı sağlamıştır.']
Q('0019','kemo','zor','yeni nesil','Tat–koku deneyi','Deney sonuçlarından tat ve koku duyularının katkısını karşılaştırarak yalnızca verilerle desteklenen sonucu seçer.',
  'Deneyde yalnız tat (burun tıkalı) ve yalnız koku (parça burun altında) durumları karşılaştırılarak her duyunun katkısı ölçülür; verilerin desteklemediği genellemeler elenir.','Sonuçların ötesine geçen genellemeleri doğru sanmak.','tat–koku deneyi',
  [A('Grupları çöz','Birinci grupta yalnız tat, ikinci grupta tat ve koku birlikte, üçüncü grupta yalnız koku çalışır; gözler üç grupta da bağlıdır.','1: tat · 2: tat + koku · 3: koku'),
   A('Oranları karşılaştır','Yalnız tat çalışırken doğru tanıma şansa yakın, yalnız koku çalışırken ise çok yüksektir.','Tat: %35 · koku: %90 · ikisi: %95'),
   A('Sonucu yorumla','Koku tek başına ayırt etmeyi büyük ölçüde sağladığı için koku duyusunun katkısı daha fazladır.','Koku katkısı > tat katkısı'),
   A('Diğer ifadeleri ele','Verilerle desteklenmeyen genellemeler (yalnızca, hiçbir şekilde) ve görmeye ilişkin ifade deneyle uyuşmaz.','Diğer ifadeler sonuçlardan çıkarılamaz')],'D',
  metin='Bir araştırmacı, gözleri bağlı gönüllülere elma, soğan ve patates parçalarından birini vererek ne olduğunu sormuştur. Üç seçenek arasından rastgele tahmin, yaklaşık %33 doğru tanıma sağlar. Aynı gönüllüler üç farklı düzenekte denenmiş ve doğru tanıma oranları şöyle bulunmuştur:\nBurnu tıkalıyken parçayı dilinde tutan: %35\nBurnu açıkken parçayı dilinde tutan: %95\nBurnu açıkken parçayı ağzına almadan burnunun altında tutan: %90\nBuna göre, bu deneyin sonuçlarından hangisine ulaşılabilir?',
  dogru=S19[3],sira=S19,
  yan=[(S19[0],'Bu şıkkı seçen öğrenci burnun açık olmasını tat reseptörlerinin çalışma koşulu sanmıştır; veriler tat reseptörlerinin burun tıkalıyken de çalıştığını dışlamaz ve bu sonuca ulaşılamaz.','dikkat'),
       (S19[1],'Bu şıkkı seçen öğrenci “yalnızca” genellemesine kanmıştır; deney koku ve tat reseptörlerini uyaran maddelerin hâlini karşılaştırmaz ve bu sonuca ulaşılamaz.','dikkat'),
       (S19[2],'Bu şıkkı seçen öğrenci %35’in şansa yakın olmasından tat reseptörlerinin hiç işe yaramadığı sonucunu çıkarmıştır; veriler yalnızca bu üç gıdada tek başına tadın yetersiz kaldığını gösterir ve bu genellemeye ulaşılamaz.','dikkat'),
       (S19[4],'Bu şıkkı seçen öğrenci gözlerin bağlı olduğunu gözden kaçırmıştır; gözler bağlı olduğundan üç durumda da görme duyusu katkı sağlayamaz.','dikkat')],
  istenen='Deney sonuçlarından çıkarılabilecek sonuç.',
  ip=['Burun tıkalıyken yalnız hangi duyunun, parça burnun altındayken yalnız hangi duyunun çalıştığını belirleyip oranları karşılaştır.'],
  bilgi=[B('Tat ve koku birlikteliği','yiyeceklerin ayırt edilmesinde tat ve koku reseptörlerinden gelen impulslar beyinde birlikte değerlendirilir'),
         B('Deney yorumlama','bir duyunun katkısı, yalnız o duyunun çalıştığı düzenekteki başarıyla; ikisinin birlikte çalıştığı düzenekteki başarı karşılaştırılarak değerlendirilir')],
  puf='Sonucu yalnız verilerin desteklediği ölçüde yaz; “yalnızca” ve “hiçbir şekilde” gibi genellemeler çoğunlukla verilerin ötesindedir.')

# ===================== 20 · Muayene tablosu · zor · tablo =====================
MUA=[('K','Net','Bulanık','Yeterli','Yeterli'),('L','Bulanık','Net','Yeterli','Yeterli'),('M','Net','Net','Yetersiz','Yeterli'),('N','Net','Net','Yeterli','Yetersiz')]
SK20=tablo_svg(['Kişi','Uzak (6 m)','Yakın (30 cm)','Loş ışık','Renk'],[list(r) for r in MUA])
S20=['K’nın gözlüğü ışınları dağıtan, L’nin gözlüğü ışınları toplayan mercek olmalıdır.','M ve N’nin sorunları retinadaki reseptör hücreleriyle ilgili olabilirken, K ve L’nin sorunları ışığın retina üzerinde odaklanamamasıyla ilgilidir.','M’nin sorunu, retinadaki koni hücrelerinin işlevinin azalmasından kaynaklanır.','N’de sorunun nedeni, ışığın retinanın önünde ya da gerisinde odaklanmasıdır.','K ile L’nin her ikisinde de retinadaki ışığa duyarlı hücrelerin sayısı azalmıştır.']
Q('0020','kusur','zor','tablo','Muayene sonuçlarının yorumu','Muayene tablosundan odaklama sorunlarını ve reseptör kaynaklı sorunları ayırıp gözlük merceği ve neden yargılarını birlikte değerlendirir.',
  'Uzak ya da yakın bulanıklığı odaklama sorunudur; loş ışıkta ya da renk görmedeki yetersizlik reseptör (çubuk, koni) kaynaklı olabilir.','Her görme sorununu odaklama kusuru sanmak ya da gözlük mercek türlerini ters yazmak.','muayene tablosu',
  [A('Tabloyu oku','K’da yakın, L’de uzak görme bulanıktır; M’de loş ışıkta, N’de renk ayırt etmede yetersizlik vardır.','K: yakın · L: uzak · M: loş ışık · N: renk'),
   A('Sorunun türünü ayır','Uzak ya da yakın bulanıklığı ışığın retinada odaklanmamasıdır; loş ışık ve renk sorunları ise ışığı algılayan hücrelerle ilgili olabilir.','K, L: odaklama · M, N: reseptör'),
   A('Gözlük mercek türlerini belirle','Yakını bulanık gören K’nın gözünde odak retinanın gerisindedir ve toplayıcı mercek gerekir; uzağı bulanık gören L için dağıtıcı mercek gerekir.','K: toplayıcı · L: dağıtıcı'),
   A('Şıkları sına','Şıklardan yalnız biri odaklama sorunu ile reseptör kaynaklı sorunu doğru ayırır; diğerleri mercek türünü, nedeni ya da hücre sayısını yanlış eşleştirir.','Tek doğru ifade bulunur')],'B',
  metin='Aşağıdaki tabloda, gözlük kullanmayan dört kişinin görme muayenesi sonuçları verilmiştir. Muayenede kişilerden 6 m uzaklıktaki harf tablosunu ve 30 cm uzaklıktaki yazıyı okumaları, loş ışıkta nesneleri tanımaları ve renk kartlarını ayırt etmeleri istenmiştir; tabloda her isteğe verilen yanıtın yeterliliği gösterilmiştir. Her kişide yalnız tek bir sorun bulunmaktadır.\nBuna göre, aşağıdakilerden hangisi doğrudur?',
  dogru=S20[1],sira=[S20[0],S20[1],S20[2],S20[3],S20[4]],
  yan=[(S20[0],'Bu şıkkı seçen öğrenci mercek türlerini ters yazmıştır; yakını bulanık gören K toplayıcı, uzağı bulanık gören L dağıtıcı mercekle düzeltilir.','bilgi'),
       (S20[2],'Bu şıkkı seçen öğrenci loş ışıkta görme sorununu konilere bağlamıştır; M’nin sorunu loş ışıkta görmeyi sağlayan çubuk hücreleriyle ilgili olabilir, renk ve parlak ışıkta keskin görmeyi sağlayan konilerle ilgili değildir.','bilgi'),
       (S20[3],'Bu şıkkı seçen öğrenci renk görme sorununu odaklama kusuru sanmıştır; N’nin sorunu renk algılayan koni hücreleriyle ilgili olabilir, odak konumuyla ilgili değildir.','bilgi'),
       (S20[4],'Bu şıkkı seçen öğrenci odaklama kusurlarını reseptör kaybıyla açıklamıştır; K ve L’de sorun ışığın retinada odaklanmasındadır ve reseptör sayısı azalmamıştır.','bilgi')],
  istenen='Doğru olan ifade.',
  ip=['Tablodaki her sorunu, ışığın odaklanmasıyla mı yoksa ışığı algılayan hücrelerle mi ilişkili olduğuna göre iki gruba ayır.'],
  bilgi=[B('Odaklama sorunları','uzak ya da yakın cisimlerde bulanıklık, ışığın retina üzerinde toplanamamasından kaynaklanır ve uygun mercekli gözlükle düzeltilir'),
         B('Retinadaki reseptörler','çubuklar loş ışıkta, koniler renkli ve keskin görmede görev yapar; bu hücrelerin işlevi azalırsa ilgili görme yetisi bozulur')],
  puf='Önce sorunu iki gruba ayır: ışığın odaklanması (gözlükle düzelir) ve reseptör hücreler (loş ışık, renk).',sekil=SK20)

# ===================== yaz =====================
from collections import Counter
for x in P.ANA: x['kardes']=None
assert len(P.ANA)==20
for q_ in P.ANA:
    no=q_['id'][-4:]; assert q_['cevap']['sik']==HEDEF[no],(no,q_['cevap']['sik'],HEDEF[no])
SCR=os.environ.get('SCRATCH','/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/duyu')
P.yaz(os.path.join(GD,'duyu-1.json'),os.path.join(SCR,'bos-duyu.json'))
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=KEY))['kartlar'].append(c['id'])
json.dump(dict(konu=KONU_AD,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2018–2026 Biyoloji (yalnız mantık), MEB 11. sınıf Denetleyici ve Düzenleyici Sistemler.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','abduyu.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler),'· şekilli',sum(1 for x in P.ANA if x['sekil']),'· öncüllü',sum(1 for x in P.ANA if x['metin'].count('\nI. ')))
