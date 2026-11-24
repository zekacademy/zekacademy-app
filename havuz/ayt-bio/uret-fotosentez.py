"""AYT Biyoloji · Fotosentez – Kemosentez · 20 soru. Kardeş yok, ipucu 1.
Şekiller TikZ/pgfplots; tüm sayılar tek yerde tanımlanır, doğru şık ve çeldiriciler assert edilir."""
import sys,os,json,math
from fractions import Fraction as Fr
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-bio'))
import _hafif_bio as H
from _hafif_bio import *
KONU_AD='Fotosentez – Kemosentez'; KEY='abio|Fotosentez – Kemosentez'
P=Parti('fotosentez',KONU_AD,KEY,ders='AYT Biyoloji',idon='aytbio'); H.KONU=KONU_AD
KAYNAK='ÖSYM AYT 2018–2026 Biyoloji fotosentez ve kemosentez soruları (yalnız mantık) · MEB 12. sınıf Canlılarda Enerji Dönüşümü'
TIPK={}
TIP={'klo':('fs-kloroplast','Kloroplast yapısı ve fotosentez yapan canlılar'),
     'isik':('fs-isiga-bagli','Işığa bağımlı tepkimeler'),
     'cal':('fs-calvin','Calvin döngüsü'),
     'fak':('fs-faktor','Fotosentez hızını etkileyen faktörler'),
     'den':('fs-deney','Fotosentez deneyleri'),
     'pig':('fs-pigment','Pigmentler ve ışık spektrumu'),
     'kem':('fs-kemosentez','Kemosentez ve karşılaştırma')}
def Q(no,tp,z,kalip,alt,kaz,fikir,tuzak,ozet,ad,**k):
    t,tn=TIP[tp]; H.kart(f'K-ABFOT-{no}',alt,fikir,tuzak,z,kalip,len(ad),t,tn,KAYNAK)
    assert len(k['ip'])==1
    mk(P,no.zfill(4),ad=ad,adim=len(ad),tipId=t,tip=tn,z=z,alt=alt,kaz=kaz,kalip=kalip,kart=f'K-ABFOT-{no} ({ozet})',**k)
def yer(harf,dogru,digerler):
    sira=[None]*5; sira['ABCDE'.index(harf)]=dogru; it=iter(digerler)
    for i in range(5):
        if sira[i] is None: sira[i]=next(it)
    assert len(set(sira))==5 and None not in sira; return sira
def tk(body,scale=1.0): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small,scale=%s]\n%s\n\\end{tikzpicture}'%(scale,body))
OK='-{Stealth[length=2.2mm,width=1.8mm]}'
ROM=['I','II','III','IV','V']
MASTER=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
def oncul(pre,yanlis_mi,harf):
    """pre: [(metin,dogru_mu,aciklama)]. Döner: (satirlar, sira, dogru, yan, adim_islem)."""
    anahtar=[i for i,(t,v,a) in enumerate(pre) if (not v if yanlis_mi else v)]
    def ad(idx): return MASTER[[ [0],[1],[2],[0,1],[0,2],[1,2],[0,1,2] ].index(sorted(idx))]
    dogru=ad(anahtar); m=MASTER.index(dogru); p='ABCDE'.index(harf); assert m-p>=0 and m-p+5<=7,(dogru,harf)
    sira=MASTER[m-p:m-p+5]; yan=[]
    for o in sira:
        if o==dogru: continue
        idx=[[0],[1],[2],[0,1],[0,2],[1,2],[0,1,2]][MASTER.index(o)]; c=[]
        for i in range(3):
            if i in idx and i not in anahtar:
                durum='doğru' if yanlis_mi else 'yanlış'; gercek='doğru' if yanlis_mi else 'yanlış'
                c.append(f'{ROM[i]}. öncül aslında {gercek} değildir ya da öyle sanılmamalıdır' if False else f'{ROM[i]}. öncül {("doğrudur" if yanlis_mi else "yanlıştır")} ({pre[i][2]}); ancak {("yanlış" if yanlis_mi else "doğru")} sanılıp seçilmiş.')
            if i not in idx and i in anahtar:
                c.append(f'{ROM[i]}. öncül {("yanlıştır" if yanlis_mi else "doğrudur")} ({pre[i][2]}); ancak {("doğru" if yanlis_mi else "yanlış")} sanılıp dışarıda bırakılmış.')
        yan.append((o,' '.join(c),'bilgi'))
    satir='\n'.join(f'{ROM[i]}. {t}' for i,(t,v,a) in enumerate(pre))
    islem=' · '.join(f'{ROM[i]}: {"doğru" if v else "yanlış"}' for i,(t,v,a) in enumerate(pre))
    return satir,sira,dogru,yan,islem

# ============================ ŞEKİLLER ============================
# --- 01 kloroplast
def kloroplast_sek():
    b=[r'\draw[line width=1.6pt] (0,0) ellipse (3.2 and 1.7);',r'\draw[line width=.7pt] (0,0) ellipse (2.95 and 1.45);']
    stacks=[(-1.7,.55),(.2,.75),(1.9,.45),(-.8,-.75),(1.0,-.7)]
    for sx,sy in stacks:
        for dy in (.3,.1,-.1,-.3):
            b.append(rf'\draw[line width=.8pt,fill=black,fill opacity=.15] ({sx},{sy+dy}) ellipse (.42 and .085);')
    for a,c in ((0,1),(1,2),(3,4)):
        b.append(rf'\draw[line width=.6pt] ({stacks[a][0]+.42},{stacks[a][1]+.1})--({stacks[c][0]-.42},{stacks[c][1]+.1});')
    def lab(t,x,y,x2,y2): return rf'\node[font=\normalsize\bfseries] at ({x},{y}) {{{t}}};\draw[{OK},line width=.8pt] ({x+(.3 if x<0 else -.3 if x>0 else 0)},{y+(-.25 if y>0 else .25)})--({x2},{y2});'
    th=math.radians(150); b.append(lab('I',-4.0,1.5,3.2*math.cos(th),1.7*math.sin(th)))
    b.append(rf'\node[font=\normalsize\bfseries] at (-4.0,-.9) {{II}};\draw[{OK},line width=.8pt] (-3.7,-.8)--(-2.95,-.05);')
    b.append(rf'\node[font=\normalsize\bfseries] at (.1,-2.65) {{III}};\draw[{OK},line width=.8pt] (.1,-2.35)--(.1,-.12);')
    b.append(rf'\node[font=\normalsize\bfseries] at (4.3,1.9) {{IV}};\draw[{OK},line width=.8pt] (3.95,1.75)--(2.33,.62);')
    b.append(rf'\node[font=\normalsize\bfseries] at (4.3,-1.7) {{V}};\draw[{OK},line width=.8pt] (3.95,-1.6)--(1.1,-.8);')
    return tk('\n'.join(b),.95)
SK1=kloroplast_sek()

# --- 03 Calvin
CO2N,RUBP,PGAN=6,6,12
assert CO2N*1+RUBP*5==PGAN*3==12*3 and PGAN*3==10*3+2*3 and 10*3==6*5 and 2*3==6
ATP_PGA=PGAN; ATP_RUBP=RUBP; NADPH=PGAN; ATP=ATP_PGA+ATP_RUBP
assert (ATP,NADPH,ATP+NADPH)==(18,12,30)
def calvin_sek():
    b=[]
    def box(x,y,t,w=2.5): return rf'\node[draw,rounded corners=3pt,line width=1pt,minimum width={w}cm,minimum height=.95cm,align=center] (n{abs(hash(t))%99999}) at ({x},{y}) {{{t}}};'
    b.append(box(0,0,r'6 RuBP\\(5C)')); b.append(box(4.6,0,r'12 PGA\\(3C)')); b.append(box(4.6,-2.4,r'12 PGAL\\(3C)'))
    b.append(box(8.6,-2.4,r'1 glikoz\\(6C)',2.2)); b.append(box(2.3,2.0,r'6 CO$_2$\\(1C)',2.0))
    b.append(rf'\draw[{OK},line width=1pt] (1.3,0)--(3.3,0);')
    b.append(rf'\draw[{OK},line width=1pt] (2.3,1.5)--(2.3,.05);')
    b.append(rf'\draw[{OK},line width=1pt] (4.6,-.5)--(4.6,-1.9);')
    b.append(rf'\draw[{OK},line width=1pt] (5.9,-2.4)--(7.5,-2.4);\node[font=\small] at (6.7,-2.05) {{2 PGAL}};')
    b.append(rf'\draw[{OK},line width=1pt] (3.35,-2.4)--(0,-2.4)--(0,-.52);\node[font=\small] at (1.7,-2.05) {{10 PGAL}};')
    return tk('\n'.join(b),.9)
SK3=calvin_sek()

# --- 04 ışık şiddeti – hız, iki CO2
def cizgi1(I): return min(2*I,4)
def cizgi2(I): return min(2*I,8)
K_,L_,M_=1,4,6
assert cizgi1(K_)==cizgi2(K_)==2 and cizgi2(L_)>cizgi1(L_)==4 and cizgi2(M_)==8==cizgi2(M_+1) and cizgi2(M_-1)==8==cizgi2(M_)
def sk4():
    b=[r'\begin{axis}[width=7.4cm,height=5.2cm,xmin=0,xmax=8,ymin=0,ymax=10,xtick={0,2,4,6,8},ytick={0,2,4,6,8,10},axis lines=left,xlabel={Işık şiddeti (birim)},ylabel={Fotosentez hızı},tick label style={font=\footnotesize},label style={font=\small},every axis plot/.append style={line width=1.5pt}]',
       r'\addplot[black] coordinates {(0,0)(2,4)(8,4)};',r'\addplot[vurgu] coordinates {(0,0)(4,8)(8,8)};',
       rf'\addplot[only marks,mark=*,mark size=2.2pt,black] coordinates {{({K_},{cizgi1(K_)})({L_},{cizgi1(L_)})({M_},{cizgi2(M_)})}};',
       rf'\node[font=\small\bfseries,anchor=north west] at (axis cs:{K_+.12},{cizgi1(K_)-.1}) {{K}};\node[font=\small\bfseries,anchor=north] at (axis cs:{L_},{cizgi1(L_)-.25}) {{L}};\node[font=\small\bfseries,anchor=south] at (axis cs:{M_},{cizgi2(M_)+.25}) {{M}};',
       r'\node[font=\small,anchor=west] at (axis cs:4.3,5.1) {Ortam 1};\node[font=\small,anchor=west,vurgu] at (axis cs:0.4,9.1) {Ortam 2};',r'\end{axis}']
    return tk('\n'.join(b))
SK4=sk4()

# --- 05 sıcaklık – hız, iki ışık şiddeti
Hy=[(5,1),(10,2.5),(15,4),(20,6),(25,8),(30,9),(35,8),(40,5),(45,2),(50,.5)]
Dy=[(5,1),(10,1.8),(15,2),(20,2),(25,2),(30,2),(35,2),(40,1.5),(45,1),(50,.3)]
Hd=dict(Hy); Dd=dict(Dy)
assert Hd[10]<Hd[30] and Hd[50]<Hd[25] and Dd[50]<Dd[25] and all(Dd[t]==2 for t in (15,20,25,30,35))
assert (Dd[30]-Dd[20])==0 and (Hd[20]-Dd[20])>0
def sk5():
    c=lambda L:' '.join(f'({x},{y})' for x,y in L)
    b=[r'\begin{axis}[width=7.6cm,height=5.2cm,xmin=0,xmax=50,ymin=0,ymax=11,xtick={0,10,20,30,40,50},ytick={0,2,4,6,8,10},axis lines=left,xlabel={Sıcaklık ($^\circ$C)},ylabel={Fotosentez hızı},tick label style={font=\footnotesize},label style={font=\small},every axis plot/.append style={line width=1.5pt}]',
       rf'\addplot[vurgu,smooth] coordinates {{(0,.3) {c(Hy)}}};',rf'\addplot[black,smooth] coordinates {{(0,.3) {c(Dy)}}};',
       r'\node[font=\small,anchor=south,vurgu] at (axis cs:30,9.3) {Yüksek ışık};\node[font=\small,anchor=south] at (axis cs:28,2.3) {Düşük ışık};',r'\end{axis}']
    return tk('\n'.join(b))
SK5=sk5()

# --- 06 Elodea düzeneği
D0,D1,BAZ,CAP=40,10,3,36
assert min(CAP,BAZ*(D0//D1)**2)==36 and BAZ*(D0//D1)**2==48
def sk6():
    s=.2; x0=0; xl=-D0*s; xk=-D1*s
    b=[]
    b.append(r'\draw[line width=1.5pt] (-.9,-.3) -- (-.9,-1.7)--(.9,-1.7)--(.9,-.3);\draw[line width=.6pt] (-.9,-.45)--(.9,-.45);')   # kap, su
    b.append(r'\draw[line width=1pt] (0,-1.7)--(0,-.7);')
    for yy in (-1.4,-1.1,-.85):
        b.append(rf'\draw[line width=.8pt] (0,{yy})--(.38,{yy+.2});\draw[line width=.8pt] (0,{yy-.05})--(-.38,{yy+.15});')
    b.append(r'\draw[line width=1pt] (-.28,-.7)--(-.55,-.2) (.28,-.7)--(.55,-.2);\draw[line width=1pt] (-.55,-.2)--(.55,-.2);')
    b.append(r'\draw[line width=1pt] (-.12,-.2)--(-.12,.85)--(.12,.85)--(.12,-.2);\draw (0,1.0) circle (.04);\draw (.04,1.3) circle (.04);\draw (-.03,1.6) circle (.04);\draw (.0,.6) circle (.04);')
    def lamba(x,tur):
        st='dashed' if tur else ''
        return rf'\draw[line width=1.2pt,{st}] ({x},-.85) circle (.38);\draw[line width=1pt,{st}] ({x-.2},-1.22)--({x+.2},-1.22);\draw[line width=.7pt,{st}] ({x+.5},-.85)--({x+.85},-.85) ({x+.45},-.55)--({x+.78},-.35) ({x+.45},-1.15)--({x+.78},-1.35);'
    b.append(lamba(xl,False)); b.append(lamba(xk,True))
    b.append(rf'\draw[line width=.8pt] ({xl},-2.45)--(0,-2.45);')
    for d in range(0,D0+1,10):
        b.append(rf'\draw[line width=.8pt] ({-d*s},-2.35)--({-d*s},-2.55);\node[font=\small,anchor=north] at ({-d*s},-2.6) {{{d}}};')
    b.append(rf'\node[font=\small,anchor=north] at ({xl/2},-3.2) {{Lamba – bitki uzaklığı (cm)}};')
    b.append(rf'\node[font=\small,align=center] at ({xl},.25) {{ilk konum:\\{BAZ} baloncuk/dk}};\node[font=\small,anchor=south] at ({xk-.1},-.25) {{yeni konum}};')
    return tk('\n'.join(b),.95)
SK6=sk6()

# --- 07 işaretli atom düzeneği
def jar(x,etiket,ust,tek):
    b=[rf'\draw[line width=1.5pt] ({x-1.35},-1.6) -- ({x-1.35},.9) arc (180:0:1.35) -- ({x+1.35},-1.6) -- cycle;']
    b.append(rf'\draw[line width=1pt] ({x},-1.6)--({x},-.4);')
    for yy,sg in ((-1.3,1),(-1.0,-1),(-.7,1)):
        b.append(rf'\draw[line width=.8pt] ({x},{yy})--({x+.45*sg},{yy+.25});\draw[line width=.8pt] ({x},{yy-.05})--({x-.45*sg},{yy+.2});')
    b.append(rf'\node[font=\small,align=center] at ({x},.4) {{{ust}}};')
    b.append(rf'\node[font=\normalsize\bfseries] at ({x},-2.0) {{{etiket}}};')
    return '\n'.join(b)
def sk7():
    b=[jar(0,'X',r'H$_2{}^{18}$O + CO$_2$',0),jar(3.6,'Y',r'H$_2$O + C${}^{18}$O$_2$',0)]
    for x in (0,3.6): b.append(rf'\draw[{OK},line width=.9pt,vurgu] ({x-.5},2.65)--({x-.5},2.0);\draw[{OK},line width=.9pt,vurgu] ({x+.5},2.65)--({x+.5},2.0);')
    b.append(r'\node[font=\small,vurgu] at (1.8,2.95) {ışık};')
    return tk('\n'.join(b),.95)
SK7=sk7()

# --- 08 soğurma spektrumu
SPEK=[(400,.3),(415,.7),(430,1),(445,.9),(460,.55),(480,.25),(500,.12),(530,.06),(550,.05),(580,.07),(610,.2),(635,.45),(662,.75),(675,.6),(690,.2),(700,.05)]
SD=dict(SPEK); KW,LW,MW=430,550,662
assert SD[KW]>SD[MW]>SD[LW]
def sk8():
    c=' '.join(f'({x},{y})' for x,y in SPEK)
    b=[r'\begin{axis}[width=8cm,height=5.2cm,xmin=400,xmax=700,ymin=0,ymax=1.45,xtick={400,450,500,550,600,650,700},ytick=\empty,axis lines=left,xlabel={Dalga boyu (nm)},ylabel={Işık soğurma},tick label style={font=\footnotesize},label style={font=\small},every axis plot/.append style={line width=1.6pt}]',
       rf'\addplot[vurgu,smooth] coordinates {{{c}}};']
    for t,w in (('K',KW),('L',LW),('M',MW)):
        b.append(rf'\draw[dashed,line width=.7pt] (axis cs:{w},0)--(axis cs:{w},1.22);\node[font=\small\bfseries,anchor=south] at (axis cs:{w},1.2) {{{t}}};')
    b.append(r'\end{axis}'); return tk('\n'.join(b))
SK8=sk8()

# --- 09 / 10 / 15 tablolar
ENG=[('Mor-mavi',62),('Yeşil',8),('Sarı-turuncu',14),('Kırmızı',51)]
SK9=tablo_svg(['Işık bölgesi','Toplanan bakteri sayısı'],[[a,str(n)] for a,n in ENG])
SK10=tablo_svg(['Bakteri','Enerji kaynağı','Karbon kaynağı','Hidrojen','O₂ çıkışı'],
   [['X','Işık','CO₂','H₂O','Var'],['Y','NH₃ yükseltgenmesi','CO₂','H₂O','Yok'],['Z','Işık','CO₂','H₂S','Yok']])
TUP=[('1','+','−','+','−','−'),('2','+','+','+','+','−'),('3','+','+','−','+','−'),('4','−','+','−','+','+')]
SK15=tablo_svg(['Tüp','Tilakoit','Stroma','Işık','CO₂','Hazır ATP, NADPH'],[list(r) for r in TUP])

# --- 14 tilakoit zar
def sk14():
    b=[r'\draw[line width=1.3pt] (-.3,.13)--(10.4,.13);\draw[line width=1.3pt] (-.3,-.13)--(10.4,-.13);']
    def kutu(x1,x2,t): return rf'\draw[line width=1pt,rounded corners=3pt,fill=black,fill opacity=.12] ({x1},-.55) rectangle ({x2},.55);\draw[line width=1pt,rounded corners=3pt] ({x1},-.55) rectangle ({x2},.55);\node[font=\small] at ({(x1+x2)/2},.35) {{{t}}};'
    b+= [kutu(.7,1.9,'FS II'),kutu(2.6,3.8,'ETS'),kutu(4.6,5.8,'FS I')]
    b.append(r'\draw[line width=1pt,fill=black,fill opacity=.12] (8.0,-.5) rectangle (8.5,.5);\draw[line width=1pt] (8.0,-.5) rectangle (8.5,.5);\draw[line width=1pt,fill=black,fill opacity=.12] (8.25,.88) circle (.4);\draw[line width=1pt] (8.25,.88) circle (.4);')
    b.append(r'\node[font=\small,anchor=north] at (8.25,-1.05) {ATP sentaz};')
    b.append(rf'\draw[{OK},dashed,line width=.9pt] (1.9,.3)--(2.6,.3);\draw[{OK},dashed,line width=.9pt] (3.8,.3)--(4.6,.3);\node[font=\small] at (2.25,.68) {{e$^-$}};\node[font=\small] at (4.2,.68) {{e$^-$}};')
    b.append(rf'\draw[{OK},line width=.9pt] (3.2,1.25)--(3.2,.6);\draw[{OK},line width=.9pt] (3.2,-.6)--(3.2,-1.25);')
    b.append(rf'\draw[{OK},line width=.9pt] (8.25,-1.0)--(8.25,-.55);\draw[{OK},line width=.9pt] (8.25,1.35)--(8.25,1.8);\node[font=\small,anchor=south] at (8.25,1.8) {{ADP + P$_i$ $\rightarrow$ ATP}};')
    b.append(rf'\draw[{OK},line width=.9pt] (1.3,-1.4)--(1.3,-.6);\node[font=\small,anchor=north] at (1.3,-1.4) {{H$_2$O}};')
    b.append(rf'\draw[{OK},line width=.9pt,vurgu] (1.3,2.0)--(1.3,.65);\draw[{OK},line width=.9pt,vurgu] (5.2,2.0)--(5.2,.65);\node[font=\small,vurgu,anchor=south] at (1.3,2.0) {{ışık}};\node[font=\small,vurgu,anchor=south] at (5.2,2.0) {{ışık}};')
    b.append(rf'\draw[{OK},line width=.9pt] (5.8,.35)--(6.6,1.2);\node[font=\small,anchor=west] at (6.55,1.4) {{NADPH}};')
    for (x,y) in [(.5,-1.1),(2.0,-1.55),(2.7,-.95),(3.9,-1.5),(4.4,-.95),(5.3,-1.55),(5.9,-1.1),(6.5,-1.5),(7.1,-.95),(9.3,-1.2),(9.9,-.8),(4.9,-1.9),(3.0,-1.95)]:
        b.append(rf'\node[font=\scriptsize] at ({x},{y}) {{H$^+$}};')
    for (x,y) in [(4.0,1.4),(9.6,1.1)]: b.append(rf'\node[font=\scriptsize] at ({x},{y}) {{H$^+$}};')
    b.append(r'\node[font=\large\bfseries] at (-.7,1.5) {I};\node[font=\large\bfseries] at (-.7,-1.5) {II};')
    return tk('\n'.join(b),1.0)
SK14=sk14()
HLUM,HSTR=13,2   # şekildeki H+ sayıları (lümen çok, stroma az)
assert HLUM>HSTR

# --- 16 net O2 – ışık
RX,SX_,CX_=4,2,12; RY,SY_,CY_=1,1,4
def gx(I): return min(SX_*I,CX_)
def gy(I): return min(SY_*I,CY_)
def nx(I): return gx(I)-RX
def ny(I): return gy(I)-RY
IQ=4
assert (nx(0),ny(0))==(-4,-1) and (nx(IQ),ny(IQ))==(4,3) and (nx(6),nx(8))==(8,8) and (ny(4),ny(8))==(3,3)
FARK=gx(IQ)-gy(IQ); assert FARK==4
def sk16():
    b=[r'\begin{axis}[width=7.6cm,height=5.6cm,xmin=0,xmax=8,ymin=-6,ymax=10,xtick={0,2,4,6,8},ytick={-6,-4,-2,0,2,4,6,8,10},axis lines=left,axis x line=middle,xlabel={Işık şiddeti (birim)},ylabel={Net O$_2$ alışverişi (birim/saat)},xlabel style={at={(axis description cs:1,.38)},anchor=west},tick label style={font=\footnotesize},label style={font=\small},every axis plot/.append style={line width=1.5pt}]',
       rf'\addplot[black] coordinates {{(0,{nx(0)})(6,{nx(6)})(8,{nx(8)})}};',rf'\addplot[vurgu] coordinates {{(0,{ny(0)})(4,{ny(4)})(8,{ny(8)})}};',
       rf'\draw[dashed,line width=.7pt] (axis cs:{IQ},-6)--(axis cs:{IQ},{nx(IQ)});',
       rf'\addplot[only marks,mark=*,mark size=2.2pt,black] coordinates {{({IQ},{nx(IQ)})}};\addplot[only marks,mark=*,mark size=2.2pt,vurgu] coordinates {{({IQ},{ny(IQ)})}};',
       r'\node[font=\small\bfseries,anchor=south] at (axis cs:6.8,8.3) {X};\node[font=\small\bfseries,vurgu,anchor=south] at (axis cs:6.8,3.3) {Y};',r'\end{axis}']
    return tk('\n'.join(b))
SK16=sk16()

# --- 17 kapalı kapta CO2 – zaman
PM=40.0; R0=PM*0.5
def Pf(t): return PM*math.sin(math.pi*(t-6)/12) if 6<=t<=18 else 0.0
CO={0:0.0}; dt=.01; t=0.0; c=0.0; seri=[]
while t<24-1e-9:
    c+=(R0-Pf(t+dt/2))*dt; t+=dt
    if abs(t-round(t))<1e-6: seri.append((round(t),c))
cur=dict(seri); cur[0]=0.0
mx=max((k for k in cur if k<=12),key=lambda k:cur[k]); mn=min((k for k in cur if 6<=k<=20),key=lambda k:cur[k])
assert mx in (8,) and mn==16,(mx,mn)
assert Pf(8)==R0 or abs(Pf(8)-R0)<1e-9 and abs(Pf(16)-R0)<1e-9 and Pf(12)>R0 and Pf(22)==0 and cur[22]>cur[16]
KT,LT,MT,NT=8,12,16,22
def sk17():
    pts=' '.join(f'({k},{cur[k]:.2f})' for k in range(0,25))
    ymin=min(cur.values())-12; ymax=max(cur.values())+25
    b=[rf'\begin{{axis}}[width=7.8cm,height=5.4cm,xmin=0,xmax=24,ymin={ymin:.0f},ymax={ymax:.0f},xtick={{0,6,12,18,24}},ytick=\empty,axis lines=left,xlabel={{Zaman (saat)}},ylabel={{Kaptaki CO$_2$ derişimi}},tick label style={{font=\footnotesize}},label style={{font=\small}},every axis plot/.append style={{line width=1.6pt}}]',
       rf'\fill[vurgu,fill opacity=.14] (axis cs:6,{ymin:.0f}) rectangle (axis cs:18,{ymin+.13*(ymax-ymin):.0f});\node[font=\footnotesize,vurgu] at (axis cs:12,{ymin+.065*(ymax-ymin):.0f}) {{ışık verilen süre}};',
       rf'\addplot[black,smooth] coordinates {{{pts}}};']
    for tt,nm in ((KT,'K'),(LT,'L'),(MT,'M')):
        b.append(rf'\addplot[only marks,mark=*,mark size=2.2pt,black] coordinates {{({tt},{cur[tt]:.2f})}};\node[font=\small\bfseries,anchor=south] at (axis cs:{tt},{cur[tt]+7:.2f}) {{{nm}}};')
    b.append(r'\end{axis}'); return tk('\n'.join(b))
SK17=sk17()

# --- 18 Calvin: ışık kesilince RuBP / PGA
PGA=[(0,6),(4,6),(5,8.5),(6,10),(8,11.5),(10,12)]; RUB=[(0,3),(4,3),(5,2),(6,1.4),(8,.7),(10,.5)]
assert PGA[-1][1]>PGA[1][1] and RUB[-1][1]<RUB[1][1]
def sk18():
    c=lambda L:' '.join(f'({x},{y})' for x,y in L)
    b=[r'\begin{axis}[width=7.6cm,height=5.2cm,xmin=0,xmax=10,ymin=0,ymax=16,xtick={0,2,4,6,8,10},ytick=\empty,axis lines=left,xlabel={Zaman (dakika)},ylabel={Madde miktarı},tick label style={font=\footnotesize},label style={font=\small},every axis plot/.append style={line width=1.6pt}]',
       rf'\addplot[black,smooth] coordinates {{{c(RUB)}}};',rf'\addplot[vurgu,smooth] coordinates {{{c(PGA)}}};',
       r'\draw[dashed,line width=.8pt] (axis cs:4,0)--(axis cs:4,14);\node[font=\footnotesize,anchor=south] at (axis cs:4,14) {ışık kapatıldı};',
       r'\node[font=\small\bfseries,anchor=south] at (axis cs:9,.9) {K};\node[font=\small\bfseries,vurgu,anchor=north] at (axis cs:9,11.3) {L};',r'\end{axis}']
    return tk('\n'.join(b))
SK18=sk18()

# ============================ SORULAR ============================
# 01 · kolay · kloroplast şeması
KLO=B('Kloroplastın bölümleri','dış ve iç zar organeli çevreler · iç zarın içindeki sıvı kısım stroma, içindeki disk biçimli zar keseleri tilakoit, bunların üst üste dizilmiş yığınları granumdur · tilakoitin içi lümen adını alır')
FOT=B('Fotosentezin evreleri','ışığa bağımlı tepkimeler tilakoit zarında, ışıktan bağımsız tepkimeler (Calvin döngüsü) stromada gerçekleşir · ışığa bağımlı evrede ATP ve NADPH üretilir')
Q('1','klo','kolay','şekilli','Kloroplast yapısı','Şematik kloroplastta stromayı tanıyıp Calvin döngüsünün yerini belirler.',
  'Calvin döngüsü enzimleri kloroplastın iç zarla çevrili sıvı kısmında, yani stromada bulunur; tilakoit zarlar ışığa bağımlı evrenin yeridir.','Fotosentezin tamamını tilakoit ya da zarlarla ilişkilendirmek.','kloroplast şeması, karbonhidrat sentezi yeri',
  metin='Şekilde bir yaprak hücresinde bulunan kloroplastın yapısı şematik olarak verilmiş ve bazı kısımları I, II, III, IV ve V ile numaralandırılmıştır.\nBir öğrenci, bu organelde karbondioksitten karbonhidrat sentezlenmesini sağlayan tepkimelerin hangi kısımda gerçekleştiğini araştırıyor.\nBuna göre bu tepkimeler numaralı kısımlardan hangisinde gerçekleşir?',
  dogru='III',sira=ROM,
  yan=[('I','I numaralı yapı dış zardır; maddelerin organele giriş çıkışını denetler, fotosentez tepkimelerine ev sahipliği yapmaz. “En dışta olan her şeyi kapsar” diye seçilmiş.','bilgi'),
       ('II','II numaralı yapı iç zardır; stromayı çevreler ve madde geçişini düzenler, Calvin döngüsünün yürüdüğü ortam değildir.','bilgi'),
       ('IV','IV numaralı yapı granumdur; tilakoit yığınında ışığa bağımlı tepkimeler görülür. Karbonhidrat sentezi ise bu yığınların dışındaki sıvıda yürür; evreler karıştırılmış.','bilgi'),
       ('V','V numaralı kısım tilakoitin iç boşluğudur (lümen); burada suyun fotolizi ve H⁺ birikimi görülür, CO₂ tutulması olmaz.','bilgi')],
  istenen='Karbonhidrat sentezinin yapıldığı kısmın numarası.',
  ip=['Karbonhidrat sentezi ışığa bağımlı mı yoksa ışıktan bağımsız evrede mi gerçekleşir? Sonra o evrenin organeldeki ortamını düşün.'],
  bilgi=[KLO,FOT],
  ad=[A('Yapıları numaralara eşle','Dıştaki iki zar I ve II, zarlar arasında kalan sıvı kısım III, disk yığınları IV, disk içi boşluk V ile gösterilmiştir.','I: dış zar · II: iç zar · III: stroma · IV: granum · V: lümen'),
      A('Olayı evreye bağla','CO₂ nin organik maddeye dönüştürüldüğü tepkimeler ışıktan bağımsız evreye, yani Calvin döngüsüne aittir.','CO₂ → karbonhidrat: Calvin döngüsü'),
      A('Evrenin yerini bul','Calvin döngüsünün enzimleri tilakoit zarların dışındaki sıvıda, stromada bulunur.','Calvin döngüsü → stroma = III')],
  puf='Işığa bağımlı evre tilakoitte, karbonhidrat sentezi (Calvin) stromada gerçekleşir.',sekil=SK1)

# 02 · orta · öncüllü olumsuz · ışığa bağımlı
pre2=[('Işığa bağımlı tepkimelerde ATP sentezi, besinlerin yıkımından elde edilen kimyasal enerjiyle gerçekleşir.',False,'ATP sentezinde kullanılan enerji, soğurulan ışıktan elektronlara aktarılan enerjidir; besin yıkımı hücresel solunumdur'),
      ('Suyun fotolizinde açığa çıkan elektronlar, ışık soğurup elektron kaybeden klorofil molekülünün yerini alır.',True,'fotolizden gelen elektronlar fotosistemdeki elektron eksikliğini giderir'),
      ('NADP⁺ elektron alarak indirgenir ve oluşan NADPH, Calvin döngüsünde kullanılır.',True,'NADPH ışığa bağımlı evrenin ürünüdür ve stromada CO₂ nin indirgenmesinde harcanır')]
s2,sr2,d2,y2,i2=oncul(pre2,True,'A')
Q('2','isik','orta','öncüllü','Işığa bağımlı tepkimeler','Işığa bağımlı tepkimelerdeki enerji kaynağı, elektron akışı ve ürünleri değerlendirir.',
  'ATP ve NADPH ışık enerjisiyle üretilir; fotolizden gelen elektronlar klorofilin kaybettiği elektronları yerine koyar; NADPH Calvin döngüsüne aktarılır.','Işığa bağımlı evrede de besin yıkımıyla ATP üretildiğini sanmak.','ışığa bağımlı evre ifadeleri, yanlış olanlar',
  metin='Bir bitkinin yaprak hücrelerindeki kloroplastlarda tilakoit zarlar üzerinde gerçekleşen ışığa bağımlı tepkimelerle ilgili bir öğrenci aşağıdaki ifadeleri yazıyor.\n'+s2+'\nBuna göre, öğrencinin yazdığı ifadelerden hangileri yanlıştır?',
  dogru=d2,sira=sr2,yan=y2,istenen='Yanlış olan öncüllerin hangileri olduğu.',
  ip=['Işığa bağımlı evrenin enerji kaynağını ve elektronların nereden gelip nereye gittiğini sırayla düşün.'],
  bilgi=[B('Işığa bağımlı tepkimeler','tilakoit zarda ışık enerjisi klorofil gibi pigmentlerce soğurulur; elektron taşıma sistemi ve ATP sentaz ile ATP, NADP⁺ nın indirgenmesiyle NADPH oluşur; su parçalanıp O₂ açığa çıkar'),
         B('Fotoliz','ışık enerjisiyle suyun parçalanması: su → H⁺ + elektron + O₂ · elektronlar fotosistemin kaybettiği elektronların yerini alır')],
  ad=[A('Enerji kaynağını sorgula','ATP üretimi için gereken enerji ışıktan gelir; besin yıkımı hücresel solunumun işidir.','1. öncül: yanlış'),
      A('Elektron akışını izle','Fotolizden gelen elektronlar ışığı soğurup elektron kaybeden klorofile aktarılır.','2. öncül: doğru'),
      A('NADPH’ın görevini hatırla','NADP⁺ elektron alıp NADPH olur ve Calvin döngüsüne gider.','3. öncül: doğru'),
      A('Yanlış olanı belirle',f'Soru yanlış ifadeleri istediğinden yalnız ilk öncül seçilir.','Yanlış olan: yalnız ilk öncül')],
  puf='Işığa bağımlı evrenin tüm enerjisi güneşten gelir; besin yıkımı yoktur.')

# 03 · zor · Calvin sayısal
Q('3','cal','zor','şekilli','Calvin döngüsü','Calvin döngüsünün bir glikoz sentezi için ATP ve NADPH gereksinimini sayısal olarak hesaplar.',
  'PGA → PGAL basamağında her PGA için 1 ATP + 1 NADPH, RuBP’nin yeniden oluşumunda her RuBP için 1 ATP harcanır.','RuBP’nin yenilenmesinde harcanan ATP’leri unutmak ya da NADPH sayısını ATP ile eşit almak.','Calvin döngüsü, glikoz için ATP ve NADPH sayısı',
  metin='Şekilde, ışıktan bağımsız tepkimelerde 6 molekül CO2 nin bağlanarak 1 molekül glikoz sentezlendiği bir döngü, molekül sayıları ve karbon atomu sayılarıyla verilmiştir. Bu süreçte PGA nın PGAL a dönüşmesi için PGA başına 1 ATP ve 1 NADPH, RuBP nin yeniden oluşması için RuBP başına 1 ATP harcanır.\nBuna göre, şekildeki süreçte harcanan toplam ATP ve NADPH sayıları toplamı kaçtır?',
  dogru=ATP+NADPH,yan=[(NADPH,'Yalnızca NADPH sayısı (12) hesaba katılmış; ATP harcamaları toplama eklenmemiş.','dikkat'),
       (ATP,'Yalnızca ATP sayısı (18) alınmış; NADPH harcaması (12) toplama eklenmemiş.','dikkat'),
       (ATP_PGA+NADPH,'RuBP’nin yeniden oluşumundaki 6 ATP unutulmuş: 12 ATP + 12 NADPH = 24.','islem'),
       (2*ATP,'NADPH sayısı da ATP kadar (18) alınmış: 18 + 18 = 36. Oysa NADPH yalnızca PGA → PGAL basamağında harcanır.','islem')],
  istenen='Toplam ATP + NADPH sayısı.',
  ip=['ATP ve NADPH harcanan iki ayrı basamağı bul; her basamakta kaç molekülün dönüştüğünü şekilden say.'],
  bilgi=[B('Calvin döngüsünün basamakları','CO₂ + RuBP → 2 PGA · PGA, ATP ve NADPH ile PGAL a indirgenir · PGAL ın bir kısmı glikoza dönüşür, kalanı ATP harcanarak RuBP’ye çevrilir'),
         B('Molekül ve karbon sayımı','bir molekülün karbon atomu sayısı: RuBP 5, PGA ve PGAL 3, CO₂ 1, glikoz 6 · döngüde karbon atomu toplamı korunur')],
  ad=[A('Karbon sayımıyla kontrol et','12 PGA ve 12 PGAL toplam 36 karbon taşır; 6 CO₂ + 6 RuBP de 36 karbon taşır, şema tutarlıdır.','6 + 30 = 36 · 12 × 3 = 36'),
      A('PGA → PGAL basamağı','12 PGA nın her biri 1 ATP ve 1 NADPH harcar.','12 ATP · 12 NADPH'),
      A('RuBP yenilenmesi','10 PGAL ile 6 RuBP oluşur ve RuBP başına 1 ATP harcanır.','6 ATP'),
      A('Toplamı bul','ATP: 12 + 6 = 18; NADPH: 12. Toplamları sorulduğundan ikisi toplanır.','18 + 12 = 30')],
  puf='Bir glikoz için Calvin döngüsü 18 ATP ve 12 NADPH harcar; ATP daha çoktur çünkü RuBP de ATP ile yenilenir.',sekil=SK3)

# 04 · orta · öncüllü grafik
pre4=[('K noktasında fotosentez hızını sınırlayan faktör ışık şiddetidir.',True,'iki ortamda da hız aynıdır ve ışıkla artmaktadır'),
      ('L noktasında ortamın CO₂ derişimi artırılırsa fotosentez hızı artar.',False,'')][:0]
pre4=[('K noktasında fotosentez hızını sınırlayan faktör ışık şiddetidir.',True,'iki ortamdaki hız da ışık şiddetiyle birlikte artar'),
      ('L noktasında ortamın CO₂ derişimi artırılırsa fotosentez hızı artar.',True,'CO₂ derişimi yüksek olan ortamın hızı aynı ışık şiddetinde daha yüksektir'),
      ('M noktasında ışık şiddeti artırılırsa fotosentez hızı artar.',False,'bu noktada eğri yataydır; ışık sınırlayıcı değildir')]
s4,sr4,d4,y4,i4=oncul(pre4,False,'B')
Q('4','fak','orta','öncüllü','Işık şiddeti ve CO₂','Fotosentez hızı–ışık şiddeti grafiğinde sınırlayıcı faktörü belirler.',
  'Eğrinin yükselen bölgesinde sınırlayıcı faktör ışık şiddetidir; eğri yatay olunca başka bir faktör (CO₂, sıcaklık) sınırlayıcıdır.','Eğrinin yatay bölgesinde de ışık şiddetini artırmanın hızı artıracağını düşünmek.','ışık şiddeti–hız grafiği, sınırlayıcı faktör',
  metin='Şekilde, sıcaklığı ve diğer koşulları aynı olan iki ortamda yetiştirilen eş bitkilerin fotosentez hızlarının ışık şiddetine bağlı değişimi gösterilmiştir. Ortamların yalnızca CO2 derişimleri farklıdır.\n'+s4+'\nBuna göre, yukarıdaki ifadelerden hangileri doğrudur?',
  dogru=d4,sira=sr4,yan=y4,istenen='Doğru olan öncüller.',
  ip=['Her noktada eğrinin yükselen mi yoksa yatay mı olduğuna ve iki eğrinin o noktadaki farkına bak.'],
  bilgi=[B('Sınırlayıcı faktör','fotosentez hızını belirleyen, en az bulunan faktördür · hız, o faktör artırılınca yükselir; diğer faktörler artırılınca değişmez'),
         B('Fotosentez hızını etkileyen faktörler','ışık şiddeti, CO₂ derişimi, sıcaklık, su ve klorofil miktarı')],
  ad=[A('Eğrileri oku','Her iki eğri de başlangıçta aynı eğimle yükselir, sonra iki farklı düzeyde yataylaşır.','Başlangıç: ortak · son: farklı düzeyler'),
      A('Yükselen bölgeyi yorumla','K noktasında hız ışık şiddetiyle artıyor; ışık sınırlayıcıdır ve CO₂ derişimi iki ortamda farklı olsa da hızı değiştirmiyor.','1. öncül: doğru'),
      A('Düşük CO₂ yatay bölgesini yorumla','L noktasında eğri yatay, ama CO₂ derişimi yüksek ortamın hızı daha yüksek; sınırlayıcı CO₂ dir.','2. öncül: doğru'),
      A('Yüksek CO₂ yatay bölgesini yorumla','M noktasında eğri yatay; ışık şiddetini artırmak hızı değiştirmez.','3. öncül: yanlış')],
  puf='Eğri yükseliyorsa sınırlayıcı faktör x eksenindeki faktördür; yataylaştığında başka bir faktör sınırlar.',sekil=SK4)

# 05 · orta · olumsuz · sıcaklık grafiği
d5='Düşük ışık şiddetinde sıcaklığı 20 °C’tan 30 °C’a çıkarmak, aynı sıcaklıkta ışık şiddetini artırmaktan daha fazla fotosentez hızı artışı sağlar.'
o5=['Yüksek ışık şiddetinde 10 °C ile 30 °C arasında sıcaklık artışı fotosentez hızını artırır.',
    'Yüksek ışık şiddetinde 30 °C’tan sonra görülen hız azalması, Calvin döngüsündeki enzimlerin etkinliğini yitirmesiyle açıklanabilir.',
    'Düşük ışık şiddetinde 15 °C ile 35 °C arasında sınırlayıcı faktör sıcaklık değildir.',
    'Her iki ışık şiddetinde de 50 °C’taki hız, 25 °C’taki hızdan düşüktür.']
assert Hd[30]-Dd[30]>0
Q('5','fak','orta','grafik','Sıcaklık ve ışık','Fotosentez hızı–sıcaklık grafiğini iki ışık şiddeti için yorumlar.',
  'Işık yetersizse sıcaklık artışı hızı değiştirmez; ışık yeterliyken sıcaklık enzim etkinliğini belirler ve optimumdan sonra hız düşer.','Düşük ışıkta da sıcaklığın sınırlayıcı olacağını düşünmek.','sıcaklık–hız grafiği, iki ışık şiddeti',
  metin='Şekilde, yeterli CO2 bulunan bir ortamda yetiştirilen aynı tür bitkiler için fotosentez hızının sıcaklıkla değişimi iki farklı ışık şiddetinde gösterilmiştir. Işık şiddeti her denemede sabit tutulmuştur.\nBuna göre, aşağıdakilerden hangisi yanlıştır?',
  dogru=d5,sira=yer('E',d5,o5),
  yan=[(o5[0],'Grafikte yüksek ışık eğrisi 10 °C’tan 30 °C’a kadar yükselir; bu ifade doğrudur ve yanlış sanılarak seçilmiş.','dikkat'),
       (o5[1],'Yüksek sıcaklıkta enzimlerin yapısı bozulur ve hız düşer; ifade doğrudur, seçen öğrenci enzim etkisini yanlış sanmış.','bilgi'),
       (o5[2],'Düşük ışık eğrisi 15–35 °C arasında yataydır; sıcaklık sınırlayıcı değildir. İfade doğrudur.','dikkat'),
       (o5[3],'İki eğri de 50 °C’ta 25 °C’takinden düşüktür; ifade doğrudur.','dikkat')],
  istenen='Grafiğe göre yanlış olan ifade.',
  ip=['Düşük ışık eğrisinde sıcaklık değişince hızın değişip değişmediğine, ışık şiddeti değişince ne olduğuna sırayla bak.'],
  bilgi=[B('Sıcaklık ve fotosentez','Calvin döngüsü enzimlerle yürüdüğünden sıcaklığa duyarlıdır; optimum sıcaklıkta hız en yüksektir, daha yüksek sıcaklıkta enzimler bozulur'),
         B('Işık sınırlayıcıysa','ışık yetersizken sıcaklığı değiştirmek hızı belirgin biçimde değiştirmez')],
  ad=[A('Eğrileri oku','Yüksek ışık eğrisi 30 °C civarında zirve yapar; düşük ışık eğrisi geniş bir aralıkta yataydır.','Zirve: yüksek ışık ≈ 30 °C · düşük ışık: yatay'),
      A('Düşük ışık bölgesini yorumla','20 °C ile 30 °C arasında düşük ışık eğrisi yataydır; sıcaklık artışının etkisi yoktur.','Düşük ışık: 20 → 30 °C artış yok'),
      A('Işığı artırmanın etkisini bul','Aynı sıcaklıkta ışığı yüksek değere getirmek hızı belirgin biçimde yükseltir.','Işık artışı > sıcaklık artışı'),
      A('Yanlış olanı seç','Sıcaklığın daha etkili olduğunu söyleyen ifade grafiğe aykırıdır; diğerleri grafikle uyumlu.','Yanlış: düşük ışıkta sıcaklığın daha etkili olduğu ifadesi')],
  puf='Işık yetersizse sıcaklığı artırmak hızı artırmaz; önce sınırlayıcı faktör giderilmelidir.',sekil=SK5)

# 06 · zor · Elodea
Q('6','fak','zor','şekilli','Işık şiddeti ve uzaklık','Işık şiddetinin uzaklıkla değişimi ile CO₂ sınırını birlikte yorumlayıp baloncuk sayısını hesaplar.',
  'Işık şiddeti uzaklığın karesiyle ters orantılıdır; fotosentez hızı ışık sınırlayıcıyken ışık şiddetiyle orantılı artar, ama başka bir faktörün belirlediği üst sınırı aşamaz.','Işık şiddetini uzaklıkla doğrusal ters orantılı almak ya da üst sınırı unutmak.','Elodea, lamba uzaklığı ve baloncuk sayısı',
  metin='Bir öğrenci, su dolu bir kapta bulunan Elodea bitkisinin fotosentez hızını, bitkiden çıkan O2 baloncuğu sayısıyla ölçüyor. Işığın bitkiye ulaşan şiddeti, lamba ile bitki arasındaki uzaklığın karesiyle ters orantılıdır. Öğrenci ilk ölçümü şekildeki ilk konumda yapıyor. Ortamdaki CO2 miktarı nedeniyle bitki, ışık şiddeti ne olursa olsun dakikada en fazla 36 baloncuk verebilmektedir.\nLamba, şekilde kesikli çizgiyle gösterilen konuma getirilirse bitki dakikada en çok kaç baloncuk verir?',
  dogru=36,yan=[(BAZ*2,'Işık şiddetinin uzaklıkla doğrusal değil karesiyle ters orantılı olduğu unutulmuş; ayrıca kare yerine karekök alınmış: 3 × 2 = 6.','bilgi'),
       (BAZ*(D0//D1),'Uzaklık 4 kat azaldığı için ışık şiddeti 4 kat artmış sanılmış: 3 × 4 = 12. Oysa şiddet uzaklığın karesiyle ters orantılıdır.','bilgi'),
       ((D0//D1)**2,'Işık şiddetindeki artış katı (16) doğrudan baloncuk sayısı sanılmış; ilk baloncuk sayısıyla çarpılmamış.','islem'),
       (BAZ*(D0//D1)**2,'Hesap doğru yapılmış (3 × 16 = 48) ama CO₂ nin belirlediği üst sınır (36) göz ardı edilmiş.','dikkat')],
  istenen='Yeni konumda dakikadaki en çok baloncuk sayısı.',
  ip=['Önce ışık şiddetinin kaç kat değiştiğini uzaklık ilişkisinden bul, sonra bulduğun sonucun ortamın izin verdiği üst sınırla uyumuna bak.'],
  bilgi=[B('Işık şiddeti ve uzaklık','bir ışık kaynağından uzaklaştıkça ışık şiddeti uzaklığın karesiyle ters orantılı azalır · uzaklık 2 katına çıkarsa şiddet 4 kat azalır'),
         B('Fotosentez hızı ölçümü','suda yaşayan bitkilerde birim zamanda çıkan O₂ baloncuğu sayısı fotosentez hızının göstergesi olarak kullanılır')],
  ad=[A('Uzaklık değişimini oku','İlk konum 40 cm, yeni konum 10 cm; uzaklık 4 kat azalıyor.','40 / 10 = 4'),
      A('Işık şiddeti artışını bul','Şiddet uzaklığın karesiyle ters orantılı olduğundan 4² = 16 kat artar.','4² = 16'),
      A('Hızı hesapla','Işık sınırlayıcıysa hız ışık şiddetiyle orantılıdır: 3 × 16 = 48 baloncuk/dk.','3 × 16 = 48'),
      A('Üst sınırla karşılaştır','CO₂ nedeniyle hız 36 baloncuğu aşamaz; 48 değeri ulaşılamaz.','min (48; 36) = 36')],
  puf='Hız artışını hesapladıktan sonra mutlaka başka bir faktörün koyduğu üst sınırı kontrol et.',sekil=SK6)

# 07 · orta · öncüllü · işaretli atom
pre7=[('Y düzeneğinde açığa çıkan O₂ gazı işaretli oksijen içerir.',False,'O₂ suyun fotolizinden gelir ve Y de su işaretsizdir'),
      ('X düzeneğinde sentezlenen glikozun oksijen atomları suyun işaretli oksijeninden gelir.',False,'glikozun oksijeni CO₂ den gelir; X de CO₂ işaretsizdir'),
      ('Y düzeneğinde sentezlenen glikoz işaretli oksijen içerir.',True,'glikozun oksijen atomları CO₂ den gelir ve Y de CO₂ işaretlidir')]
s7,sr7,d7,y7,i7=oncul(pre7,False,'C')
Q('7','den','orta','öncüllü','İşaretli atom deneyi','Fotosentezde O₂ nin sudan, glikozdaki oksijenin CO₂ den geldiğini işaretli atom deneyinden yorumlar.',
  'Fotosentezde açığa çıkan O₂ suyun fotolizinden, glikozdaki karbon ve oksijen CO₂ den gelir.','O₂ nin CO₂ den geldiğini sanmak.','işaretli oksijen deneyi, X ve Y düzenekleri',
  metin='Şekildeki X ve Y düzeneklerinde eş bitkiler, ışıkta ve eşit koşullarda, kapalı ortamlarda tutulmuş; X te yalnız su, Y de yalnız CO2 işaretli oksijen (18O) içermektedir. Bir süre sonra her iki düzenekte de açığa çıkan O2 ve sentezlenen glikoz incelenmiştir.\n'+s7+'\nBuna göre, yukarıdaki ifadelerden hangileri doğrudur?',
  dogru=d7,sira=sr7,yan=y7,istenen='Doğru olan öncüller.',
  ip=['Fotosentezde O₂ nin ve glikozdaki oksijenin hangi başlangıç maddesinden geldiğini ayrı ayrı belirle.'],
  bilgi=[B('Fotosentez denklemi','6CO₂ + 12H₂O → C₆H₁₂O₆ + 6O₂ + 6H₂O (ışık ve klorofil ile) · ürün olan O₂ suyun ayrışmasından, glikozdaki atomlar CO₂ den gelir'),
         B('İşaretli atom (izotop) yöntemi','bir atomun ağır izotopu ile işaretlenmiş madde verilip bu atomun ürünlerde aranmasıyla maddelerin izlendiği yöntemdir')],
  ad=[A('O₂ nin kaynağını belirle','Fotosentezde O₂ suyun fotolizinden açığa çıkar; işaretli su X teki O₂ yi işaretler, Y de işaretli CO₂ O₂ yi işaretlemez.','X: O₂ işaretli · Y: O₂ işaretsiz'),
      A('Glikozun oksijeninin kaynağı','Glikozun oksijen atomları CO₂ den gelir; X te CO₂ işaretsizdir, Y de işaretlidir.','X: glikoz işaretsiz · Y: glikoz işaretli'),
      A('Öncülleri değerlendir',f'Üç öncülün doğru–yanlış durumu bu çıkarımlarla belirlenir.',i7)],
  puf='İşaretli suyun oksijeni O₂ ye, işaretli CO₂ nin oksijeni glikoza gider.',sekil=SK7)

# 08 · kolay · spektrum
SR=['K > M > L','K = M > L','M > K > L','K > L > M','L > K > M']
Q('8','pig','kolay','grafik','Soğurma spektrumu','Klorofilin soğurma spektrumundan fotosentez hızı sıralamasını çıkarır.',
  'Fotosentez hızı pigmentin soğurduğu ışık miktarıyla artar; klorofil mavi-mor ve kırmızı bölgeyi iyi, yeşil bölgeyi az soğurur.','Yeşil ışığın en etkili olduğunu ya da mavi ve kırmızıda soğurmanın eşit olduğunu sanmak.','soğurma spektrumu, O₂ üretimi sıralaması',
  metin='Şekilde bir klorofil pigmentinin farklı dalga boylarındaki ışığı soğurma düzeyi verilmiştir. Eşit sayıda yaprak hücresi taşıyan üç özdeş Elodea dalı, K, L ve M ile gösterilen dalga boylarındaki, eşit şiddetli ışıkla aynı süre aydınlatılmıştır. Fotosentez hızı soğurulan ışık miktarıyla doğru orantılıdır.\nBuna göre, bu üç dalda aynı sürede oluşan O2 miktarlarının sıralaması aşağıdakilerden hangisidir?',
  dogru=SR[0],sira=yer('A',SR[0],SR[1:]),
  yan=[(SR[1],'Mavi ve kırmızı bölgeler eşit soğurulur sanılmış; grafikte K deki soğurma M dekinden daha yüksektir.','dikkat'),
       (SR[2],'Kırmızı ışığın mavi-mor ışıktan daha çok soğurulduğu sanılmış; grafikte K nin değeri M ninkinden yüksektir.','dikkat'),
       (SR[3],'Yeşil bölgenin kırmızıdan daha çok soğurulduğu sanılmış; L deki soğurma en düşüktür.','bilgi'),
       (SR[4],'Yeşil ışığın en etkili olduğu sanılmış: bitkinin yeşil görünmesi onu en çok soğurduğunu değil, en az soğurduğunu gösterir.','bilgi')],
  istenen='O₂ miktarlarının sıralaması.',
  ip=['Hız soğurulan ışık miktarına bağlıdır; grafikte işaretli üç noktanın yüksekliğini karşılaştır.'],
  bilgi=[B('Fotosentetik pigmentler','klorofil a ve b mavi-mor ile kırmızı ışığı, karotenoitler mavi ve yeşilimsi bölgeyi soğurur · yeşil ışık büyük ölçüde yansıtılır'),
         B('Soğurma spektrumu','bir pigmentin dalga boyuna göre ışık soğurma düzeyini gösteren grafiktir')],
  ad=[A('Üç noktayı oku','K mavi-mor bölgede en yüksek, M kırmızı bölgede yüksek ama K den düşük, L yeşil bölgede çok düşüktür.','Soğurma: K > M > L'),
      A('Hız ilişkisini kullan','Fotosentez hızı soğurulan ışık miktarıyla doğru orantılıdır.','Hız ∼ soğurma'),
      A('Sıralamayı O₂ ye çevir','Aynı sürede oluşan O₂ miktarı soğurma sırasıyla değişir.','O₂: K > M > L')],
  puf='Yaprağın yeşil görünmesi yeşil ışığın az soğurulduğunu gösterir; hız mavi-mor ve kırmızıda yüksektir.',sekil=SK8)

# 09 · orta · öncüllü · Engelmann
pre9=[('Mor-mavi ve kırmızı bölgelerdeki bakteri sayılarının farklı olması, bu bölgelerde algin fotosentez hızının eşit olduğunu gösterir.',False,'62 ve 51 bakteri farklı O₂ üretimini yansıtır, hızlar eşit değildir'),
      ('Kırmızı bölgede yeşil bölgeden daha çok bakterinin toplanması, klorofillerin kırmızı ışığı yeşilden daha çok soğurduğunu gösterir.',True,'bakteri sayısı O₂ üretimini, O₂ üretimi soğurulan ışığı yansıtır'),
      ('Yeşil bölgede bakterilerin toplanmış olması, bu bölgede fotosentez yapılmadığını gösterir.',False,'bakteri toplanması bir miktar O₂ üretildiğini gösterir')]
s9,sr9,d9,y9,i9=oncul(pre9,False,'B')
Q('9','pig','orta','tablo','Engelmann deneyi','Etki spektrumu deneyinde bakteri sayısından fotosentez hızı çıkarımı yapar.',
  'Oksijene yönelen bakterilerin sayısı o bölgedeki O₂ üretimini, dolayısıyla fotosentez hızını yansıtır; yeşil bölgede de az da olsa fotosentez görülür.','Bakteri toplanmayan ya da az toplanan bölgede fotosentezin hiç olmadığını düşünmek.','Engelmann deneyi, bakteri tablosu',
  metin='Bir araştırmacı, iplik şeklinde kloroplastlı bir alg ipliğini oksijene yönelen bakterilerin bulunduğu damlaya koyuyor. İplik prizmayla ayrılmış ışığın değişik renk bölgelerine yerleştirilip bekletilince bakteriler iplik boyunca tablodaki gibi dağılıyor.\n'+s9+'\nBuna göre, yukarıdaki ifadelerden hangileri doğrudur?',
  dogru=d9,sira=sr9,yan=y9,istenen='Doğru olan öncüller.',
  ip=['Bakterilerin neden toplandığını düşün ve bakteri sayısını fotosentezle ilişkilendir.'],
  bilgi=[B('Etki spektrumu','fotosentez hızının ışığın dalga boyuna göre değişimidir; soğurma spektrumuyla büyük ölçüde örtüşür'),
         B('Oksijene yönelen bakteriler','oksijenli ortama yönelirler; çok bakteri toplanması o bölgede O₂ üretiminin yüksek olduğunu gösterir')],
  ad=[A('Deneyin mantığını kur','Bakteriler O₂ ye yöneldiğinden bakteri sayısı O₂ üretimini, yani fotosentez hızını yansıtır.','Bakteri sayısı ↑ → O₂ ↑ → fotosentez hızı ↑'),
      A('Mor-mavi ve kırmızıyı karşılaştır','62 ve 51 aynı değildir; hızlar eşit değildir.','1. öncül: yanlış'),
      A('Kırmızı ve yeşili karşılaştır','Kırmızıda 51, yeşilde 8 bakteri var; kırmızı ışık daha çok soğurulur.','2. öncül: doğru'),
      A('Yeşil bölgeyi değerlendir','Yeşilde de 8 bakteri toplanmıştır; az da olsa O₂ üretilmiştir.','3. öncül: yanlış')],
  puf='Bakteri sayısı O₂ üretiminin, O₂ üretimi de soğurulan ışığın ölçüsüdür; az demek hiç demek değildir.',sekil=SK9)

# 10 · orta · öncüllü · tablo kemosentez
pre10=[('X ve Y bakterilerinin organik madde sentezinde kullandığı enerji ışıktan sağlanır.',False,'Y nin enerjisi NH₃ nin yükseltgenmesinden gelir'),
       ('X ve Z bakterilerinin organik madde sentezi fotosentez, Y bakterisininki kemosentezdir.',True,'ışık kullananlar fotosentez, inorganik madde yükseltgeyenler kemosentez yapar'),
       ('Z bakterisinin organik madde sentezi sırasında O₂ açığa çıkmaması, hidrojen kaynağının sudan farklı olmasıyla ilişkilidir.',True,'O₂ suyun fotolizinden gelir; Z su yerine H₂S kullanır')]
s10,sr10,d10,y10,i10=oncul(pre10,False,'E')
Q('10','kem','orta','öncüllü','Fotosentez ve kemosentez','Tablodaki bakterilerin enerji ve hidrojen kaynağına göre fotosentez ve kemosentezi ayırt eder.',
  'Enerjisini ışıktan alan fotosentez, inorganik maddelerin yükseltgenmesinden alan kemosentez yapar; O₂ yalnız hidrojen kaynağı su olan fotosentezde açığa çıkar.','Işık kullanan her bakterinin O₂ çıkardığını ve kemosentezi hep fotosentezle karıştırmak.','bakteri tablosu, enerji kaynağı',
  metin='Üç farklı bakteri türünün organik madde sentezine ilişkin bazı özellikleri tabloda verilmiştir.\n'+s10+'\nBuna göre, yukarıdaki ifadelerden hangileri doğrudur?',
  dogru=d10,sira=sr10,yan=y10,istenen='Doğru olan öncüller.',
  ip=['Her bakterinin enerji kaynağına bak: ışık mı, inorganik bir maddenin yükseltgenmesi mi? O₂ nin kaynağını da hatırla.'],
  bilgi=[B('Kemosentez','bazı bakterilerin inorganik maddeleri yükseltgeyerek elde ettiği enerjiyle CO₂ den organik madde sentezlemesidir · ışık ve klorofil gerekmez · örnek: demir bakterileri'),
         B('Bakteride fotosentez','bazı bakteriler ışığı soğurur ve hidrojen kaynağı olarak H₂S gibi maddeler kullanır; bu durumda O₂ açığa çıkmaz')],
  ad=[A('Enerji kaynaklarını sınıfla','X ve Z ışık, Y inorganik madde yükseltgenmesi kullanıyor.','X, Z: ışık · Y: kimyasal'),
      A('Sentez türlerini belirle','Işıkla sentez yapanlar fotosentetik, kimyasal enerjiyle yapanlar kemosentetiktir.','X, Z: fotosentez · Y: kemosentez'),
      A('O₂ çıkışını yorumla','X te O₂ çıkıyor, Z de çıkmıyor; fark hidrojen kaynağından (H₂O ya da H₂S) gelir.','Z: hidrojen kaynağı H₂S → O₂ yok'),
      A('Öncülleri değerlendir','Bu üç çıkarım öncüllerin değerini belirler.',i10)],
  puf='Enerji ışıksa fotosentez, inorganik madde yükseltgenmesiyse kemosentezdir; O₂ yalnız suyun fotolizinden gelir.',sekil=SK10)

# 11 · orta · olumsuz kemosentez
d11='Kemosentez yapan bakterilerde inorganik maddelerin yükseltgenmesi sırasında O₂ gazı açığa çıkar.'
o11=['Nitrit ve nitrat bakterileri kemosentez yapan canlılara örnektir.',
     'Kemosentezde inorganik maddelerin yükseltgenmesiyle açığa çıkan enerji ATP sentezinde kullanılır.',
     'Kemosentez yapan bakteriler ışığın ulaşmadığı ortamlarda da organik madde üretebilir.',
     'Kemosentezde de organik maddelerin karbon kaynağı CO₂ dir.']
Q('11','kem','orta','düz','Kemosentez','Kemosentezin enerji kaynağını, ürünlerini ve örneklerini değerlendirir.',
  'Kemosentez inorganik madde yükseltgenmesinin enerjisiyle yürür; ışık, klorofil ve fotoliz gerekmediğinden O₂ açığa çıkmaz.','Kemosentezi fotosentezle karıştırıp O₂ çıkışını da beklemek.','kemosentez, yanlış ifade',
  metin='Bir öğrenci, derin deniz hidrotermal bacalarının çevresindeki ışıksız ortamda yaşayan ve H2S, NH3 gibi inorganik maddeleri yükseltgeyerek organik madde sentezleyen bakterileri araştırıyor. Bu bakterilerin besin üretimini fotosentezle karşılaştırarak kemosentezle ilgili notlar alıyor.\nBuna göre, öğrencinin notlarındaki ifadelerden hangisi yanlıştır?',
  dogru=d11,sira=yer('D',d11,o11),
  yan=[(o11[0],'Nitrit ve nitrat bakterileri kemosentez yapar; ifade doğrudur, “kemosentez yalnız ağır madde bakterisinde olur” diye yanlış sanılmış.','bilgi'),
       (o11[1],'Yükseltgenmeden çıkan enerji ATP sentezinde kullanılır; ifade doğrudur, enerjinin doğrudan glikoza aktarıldığı sanılmış.','bilgi'),
       (o11[2],'Kemosentez ışık gerektirmediğinden ışıksız ortamda da sürer; ifade doğrudur.','dikkat'),
       (o11[3],'Kemosentez yapan bakteriler de CO₂ yi karbon kaynağı olarak kullanır; ifade doğrudur.','bilgi')],
  istenen='Kemosentezle ilgili yanlış olan ifade.',
  ip=['Kemosentezde O₂ nin fotosentezdeki gibi suyun ayrışmasından gelip gelmediğini düşün.'],
  bilgi=[B('Kemosentez','inorganik maddelerin yükseltgenmesinden sağlanan enerjiyle CO₂ den organik madde yapılmasıdır · örnekler: nitrit, nitrat, demir ve kükürt bakterileri'),
         B('Fotosentezle fark','fotosentezde enerji ışıktır ve su fotolizinden O₂ çıkar · kemosentezde ışık ve klorofil gerekmez, su fotolizi olmaz')],
  ad=[A('İfadeleri kemosentez bilgisiyle karşılaştır','Kemosentezde enerji, inorganik bir maddenin yükseltgenmesinden gelir ve ATP sentezinde kullanılır.','Enerji kaynağı: kimyasal'),
      A('Işık ve karbon kaynağını sorgula','Işık gerekmez, karbon kaynağı CO₂ dir.','Işıksız ortamda sentez mümkün · karbon kaynağı CO₂'),
      A('O₂ çıkışını sorgula','Suyun fotolizi olmadığından O₂ açığa çıkmaz; bu özelliği taşıyan ifade yanlıştır.','O₂ çıkışı yok')],
  puf='O₂ çıkışı suyun fotolizine bağlıdır; kemosentezde fotoliz olmaz.')

# 12 · zor · öncüllü · nitrifikasyon + kemosentez
pre12=[('Bu bakterilerin organik madde sentezi, ışığın bulunmadığı toprak katmanlarında da sürebilir.',True,'enerji ışıktan değil inorganik madde yükseltgenmesinden gelir'),
       ('X bakterisinin ürettiği nitrit, Y bakterisi için enerji sağlayan bir yükseltgenme basamağının girdisidir.',True,'Y, nitriti nitrata yükseltgeyerek enerji elde eder'),
       ('Y bakterisinin faaliyetleri sonucu toprakta bitkilerin kullanabileceği azot miktarı azalır.',False,'oluşan nitrat bitkilerce kullanılabilen bir azot kaynağıdır ve miktarı artar')]
s12,sr12,d12,y12,i12=oncul(pre12,False,'B')
Q('12','kem','zor','öncüllü','Kemosentez ve azot dönüşümü','Nitrit ve nitrat bakterilerinin kemosentezini azot döngüsü ve bitki beslenmesiyle birlikte yorumlar.',
  'Kemosentetik bakteriler enerji için inorganik maddeyi yükseltger; bu yükseltgenme zinciri toprakta bitkilerin kullanabileceği nitrat oluşturur.','Kemosentetik bakterilerin ışığa gereksinim duyduğunu ya da bitki azotunu azalttığını düşünmek.','nitrit ve nitrat bakterileri',
  metin='Toprakta yaşayan X bakterisi amonyağı nitrite, Y bakterisi ise nitriti nitrata yükseltger. Her iki bakteri de bu tepkimelerden elde ettiği enerjiyle CO2 ve H2O den organik madde sentezler. Bir tarım alanında bu bakterilerin etkinliği incelenmektedir.\n'+s12+'\nBuna göre, yukarıdaki ifadelerden hangileri doğrudur?',
  dogru=d12,sira=sr12,yan=y12,istenen='Doğru olan öncüller.',
  ip=['Bakterilerin enerjiyi nereden aldığını ve tepkime zincirinin sonunda toprakta hangi maddenin biriktiğini düşün.'],
  bilgi=[B('Nitrifikasyon','amonyağın önce nitrite, sonra nitrata yükseltgenmesidir · bu basamakları nitrit ve nitrat bakterileri yürütür'),
         B('Bitkilerin azot kullanımı','bitkiler azotu çoğunlukla nitrat biçiminde alır ve protein, nükleik asit gibi moleküllerin yapımında kullanır')],
  ad=[A('Enerji kaynağını belirle','Bakteriler enerjiyi yükseltgenme tepkimelerinden alır; ışığa gereksinim duymazlar.','1. öncül: doğru'),
      A('Tepkime zincirini izle','X nin ürünü olan nitrit, Y nin yükseltgeyeceği maddedir; yani Y nin enerji sağlayan tepkimesinin girdisidir.','2. öncül: doğru'),
      A('Toprağa etkisini değerlendir','Y nitrat üretir; nitrat bitkilerin alabildiği azot biçimidir, yani kullanılabilir azot artar.','3. öncül: yanlış'),
      A('Öncülleri birleştir','Doğru öncüller seçilir.',i12)],
  puf='Kemosentetik nitrifikasyon bakterileri enerjisini kimyasal tepkimeden alır ve toprağa bitkinin kullanabileceği nitrat kazandırır.')

# 13 · kolay · siyanobakteri
d13='Sitoplazmadaki zar yapılarında (tilakoit benzeri zarlarda)'
o13=['Kloroplastın tilakoit zarlarında','Mitokondrinin iç zarında','Çekirdek zarının üzerinde','Ribozomların yüzeyinde']
Q('13','klo','kolay','düz','Prokaryotta fotosentez','Siyanobakterilerde ışığa bağımlı tepkimelerin zarlı organel olmadan sitoplazmadaki zarlarda yürüdüğünü belirler.',
  'Prokaryotlarda zarlı organel yoktur; fotosentez pigmentleri sitoplazmadaki zar katlanmalarında bulunur.','Fotosentezin yalnız kloroplastta gerçekleşeceğini sanmak.','siyanobakteri hücresi',
  metin='Siyanobakteriler fotosentez yaparak O2 üretir. Bir siyanobakteri hücresi elektron mikroskobuyla incelendiğinde hücrede kloroplast, mitokondri ve çekirdek gibi zarla çevrili organellerin bulunmadığı görülüyor.\nBuna göre, bu hücrede ışığa bağımlı tepkimeler aşağıdakilerden hangisinde gerçekleşir?',
  dogru=d13,sira=yer('B',d13,o13),
  yan=[(o13[0],'Kloroplast ökaryotik hücrelere özgüdür; soruda hücrede kloroplast olmadığı verilmiş. “Fotosentez = kloroplast” diye düşünülmüş.','dikkat'),
       (o13[1],'Mitokondri iç zarında hücresel solunumun elektron taşıma sistemi bulunur; ayrıca hücrede mitokondri yoktur.','bilgi'),
       (o13[2],'Çekirdek zarı kalıtım maddesini çevreler; prokaryotta zaten yoktur ve fotosentezle ilgisi yoktur.','bilgi'),
       (o13[3],'Ribozomlar protein sentezi yeridir; fotosentez pigmentleri ve elektron taşıyıcıları zarlarda bulunur.','bilgi')],
  istenen='Işığa bağımlı tepkimelerin gerçekleştiği yer.',
  ip=['Hücrede olmayan yapıları ele, sonra ışığı soğuran pigmentlerin hangi zarlarda bulunduğunu düşün.'],
  bilgi=[B('Prokaryot hücre','çekirdek ve zarlı organeller (kloroplast, mitokondri) bulunmaz · hücre zarı ve sitoplazma vardır'),
         B('Siyanobakterilerde fotosentez','klorofil a ve diğer pigmentler sitoplazmadaki zar katlanmalarında bulunur ve ışığa bağımlı tepkimeler burada yürür')],
  ad=[A('Hücredeki yapıları ele','Kloroplast, mitokondri ve çekirdek yoktur; bunları içeren şıklar elenir.','Elenenler: kloroplast, mitokondri, çekirdek zarı'),
      A('Kalan seçenekleri düşün','Ribozom protein sentezi yapar; pigmentler zar sistemlerinde bulunur.','Ribozom: protein sentezi'),
      A('Doğru yeri belirle','Pigmentler sitoplazmadaki zar yapılarında yer alır ve ışığa bağımlı tepkimeler orada gerçekleşir.','Cevap: sitoplazmadaki zar yapıları')],
  puf='Fotosentez yalnız kloroplastlara bağlı değildir; prokaryotlarda sitoplazmadaki zarlarda yürür.')

# 14 · orta · olumsuz · tilakoit zar
d14='Elektronlar taşıma sistemi boyunca ilerlerken protonları I numaralı bölgeden II numaralı bölgeye pompalamak için ATP harcanır.'
o14=['ATP sentaz, protonların II numaralı bölgeden I numaralı bölgeye geçişinden yararlanarak ATP sentezler.',
     'II numaralı bölgenin pH değeri, I numaralı bölgenin pH değerinden daha düşüktür.',
     'Suyun fotolizinde açığa çıkan protonlar II numaralı bölgede toplanır.',
     'Üretilen ATP, Calvin döngüsünün gerçekleştiği I numaralı bölgede kullanılır.']
Q('14','klo','orta','şekilli','Tilakoit zar ve kemiozmoz','Tilakoit zarında proton gradyanı ve ATP sentezi mekanizmasını yorumlar.',
  'Elektron akışı enerjisiyle H⁺ lar stromadan lümene pompalanır; lümendeki yüksek H⁺ derişimi ATP sentaz boyunca stromaya geçerken ATP üretilir.','Proton pompalanmasında ATP harcandığını ya da ATP sentazın protonları stromaya taşıdığı için bölge pH’larının tersini düşünmek.','tilakoit zarı, proton gradyanı',
  metin='Şekilde bir kloroplastın tilakoit zarı ve zarın iki yanındaki bölgeler I ve II ile gösterilmiştir; zarda ışığa bağımlı tepkimelerde görevli yapılar yer almaktadır.\nBuna göre, şekle ve ışığa bağımlı tepkimelere göre aşağıdakilerden hangisi yanlıştır?',
  dogru=d14,sira=yer('E',d14,o14),
  yan=[(o14[0],'Protonlar derişimi yüksek lümenden stromaya ATP sentaz boyunca geçerken ATP üretilir; ifade doğrudur.','bilgi'),
       (o14[1],'Lümende H⁺ çok olduğundan pH düşüktür; ifade doğrudur ve “H⁺ çok = pH yüksek” diye yanlış sanılmış.','bilgi'),
       (o14[2],'Fotolizde açığa çıkan H⁺ lar lümende birikir; ifade doğrudur.','bilgi'),
       (o14[3],'ATP stromaya verilir ve Calvin döngüsünde kullanılır; ifade doğrudur.','bilgi')],
  istenen='Yanlış olan ifade.',
  ip=['Protonları zarın bir yanından diğerine taşıyan enerjinin kaynağını ve ATP sentazdaki proton akış yönünü düşün.'],
  bilgi=[B('Kemiozmotik ATP sentezi','elektron taşıma sistemindeki enerjiyle protonlar zarın bir yanında biriktirilir; protonlar ATP sentaz boyunca derişimi az tarafa geçerken ATP sentezlenir'),
         B('Fotosentezde proton gradyanı','tilakoit boşluğu (lümen) H⁺ bakımından zengin, stroma ise fakirdir')],
  ad=[A('Bölgeleri tanı','Şekilde H⁺ lar II numaralı bölgede çok, I numaralı bölgede azdır; ATP sentazın knob kısmı I tarafındadır.','II: lümen · I: stroma'),
      A('Proton akışını izle','Elektron akışının enerjisi protonları I → II pompalar; ATP sentazdan II → I akarken ATP üretilir.','Pompalama: elektron enerjisi · ATP: akış sırasında'),
      A('İfadeleri ele','Pompalama için ATP harcandığını söyleyen ifade yanlıştır; diğerleri doğrudur.','Yanlış: pompalamada ATP harcanır ifadesi')],
  puf='Fotosentezde protonlar ATP harcanarak değil, elektron akışının enerjisiyle pompalanır; ATP proton akışıyla yapılır.',sekil=SK14)

# 15 · orta · tablo deney
o15=['Yalnız 2','1 ve 2','2 ve 4','3 ve 4','1, 2 ve 4']
Q('15','den','orta','tablo','Kloroplast parçalarıyla deney','Işığa bağımlı ve bağımsız evreleri ayrı ayrı çalıştıran deneyde glikoz oluşumunu yorumlar.',
  'Glikoz sentezi için stromada CO₂ ile birlikte ATP ve NADPH gerekir; bunlar ışıkta tilakoitle ya da hazır olarak sağlanırsa karanlıkta da sentez sürer.','Glikoz sentezi için ışığın her zaman gerektiğini düşünmek.','kloroplast parçalarıyla deney',
  metin='Kloroplastlardan ayrılmış tilakoit zar süspansiyonu ile stroma sıvısı (Calvin döngüsü enzimlerini ve RuBP’yi içerir) farklı bileşimlerde dört tüpe konuyor. Tüplerin tümünde ADP, Pi ve NADP⁺ bulunuyor; içerikleri tabloda verilmiştir ve tüpler tabloda belirtilen koşullarda bir süre bekletilmiştir.\nBuna göre, hangi tüplerde glikoz sentezi gerçekleşir?',
  dogru=o15[2],sira=o15,
  yan=[(o15[0],'Yalnız 2. tüp seçilerek 4. tüpteki hazır ATP ve NADPH nin glikoz sentezini karanlıkta da mümkün kıldığı gözden kaçmış.','dikkat'),
       (o15[1],'1. tüpte stroma ve CO₂ olmadığından glikoz oluşmaz; tüpte yalnız ışığa bağımlı tepkimeler sonucu ATP ve NADPH üretilir.','bilgi'),
       (o15[3],'3. tüp karanlıktadır ve hazır ATP ile NADPH içermez; tilakoit ışıksız ATP ve NADPH üretemez, glikoz oluşmaz.','dikkat'),
       (o15[4],'1. tüpte stroma ve CO₂ yoktur, bu yüzden glikoz oluşmaz; ışıkta tilakoitin çalışması glikoz yapımı için yeterli değildir.','bilgi')],
  istenen='Glikoz sentezi gerçekleşen tüpler.',
  ip=['Glikoz sentezi için gerekli üç girdiyi (enzim ortamı, CO₂, enerji taşıyıcıları) her tüpte ayrı ayrı ara.'],
  bilgi=[B('Calvin döngüsünün girdileri','stromada enzimler ve RuBP, ortamda CO₂, ATP ve NADPH bulunmalıdır · bu döngü doğrudan ışığa gereksinim duymaz'),
         B('Tilakoitin görevi','ışığa bağımlı tepkimelerde ATP ve NADPH üretir')],
  ad=[A('Gereken girdileri belirle','Glikoz için stroma, CO₂, ATP ve NADPH gerekir.','Stroma + CO₂ + ATP + NADPH'),
      A('ATP ve NADPH kaynağını bul','Işıkta tilakoit üretir; ışık yoksa ancak hazır verilirse bulunur.','Kaynak: ışık + tilakoit ya da hazır ATP/NADPH'),
      A('Tüpleri tek tek ele','1. tüpte stroma ve CO₂ yok; 2. tüpte hepsi var; 3. tüpte karanlıkta enerji taşıyıcı üretilmez; 4. tüpte hazır enerji taşıyıcıları var.','1: yok · 2: var · 3: yok · 4: var'),
      A('Sonucu yaz','Glikoz yalnız 2. ve 4. tüplerde oluşur.','Tüp 2 ve tüp 4')],
  puf='Glikoz yapımı için gereken şey ışık değil, ATP ve NADPH dir; bunlar hazır verilirse karanlıkta da sentez sürer.',sekil=SK15)

# 16 · zor · net O2 grafiği
Q('16','fak','zor','grafik','Net O₂ alışverişi','Net gaz alışverişi grafiğinden solunumu da ekleyerek toplam fotosentezi hesaplar.',
  'Net O₂ alışverişi, fotosentezle üretilen O₂ ile solunumla tüketilen O₂ nin farkıdır; ışıksız ortamdaki değer solunum hızını verir.','Net değeri toplam fotosentez sanmak ya da solunumu eklemeyi unutmak.','net O₂ alışverişi–ışık grafiği, toplam fotosentez',
  metin='Şekilde, X ve Y bitkilerinin birim zamanda yaptığı net O2 alışverişinin ışık şiddetiyle değişimi gösterilmiştir. Pozitif değerler ortama O2 verildiğini, negatif değerler ortamdan O2 alındığını gösterir. Solunum hızı her iki bitkide ışık şiddetinden bağımsızdır.\nBuna göre, işaretli ışık şiddetinde X in fotosentezle ürettiği toplam O2 miktarı, Y ninkinden kaç birim fazladır?',
  dogru=FARK,yan=[(nx(IQ)-ny(IQ),'Yalnızca net değerler çıkarılmış (4 − 3 = 1); solunumda tüketilen O₂ toplam fotosentezi bulmak için eklenmemiş.','dikkat'),
       (RX-RY,'Işıksız ortamdaki değerler (solunum hızları) çıkarılmış (4 − 1 = 3); fotosentez ve net değerler hesaba katılmamış.','dikkat'),
       (nx(IQ)+ny(IQ),'Net değerler toplanmış (4 + 3 = 7); fark yerine toplam alınmış ve solunum eklenmemiş.','islem'),
       (gx(IQ),'Yalnızca X in toplam fotosentezi (4 + 4 = 8) bulunmuş; Y ninki çıkarılmamış.','islem')],
  istenen='Toplam fotosentez farkı (birim).',
  ip=['Işık şiddeti sıfırken okunan değerlerin neyi gösterdiğini düşün; net değeri toplam fotosentez için nasıl düzeltirsin?'],
  bilgi=[B('Net ve toplam fotosentez','toplam fotosentez O₂ üretimi = net O₂ salınımı + solunumla tüketilen O₂'),
         B('Kompanzasyon noktası','fotosentez hızının solunum hızına eşit olduğu ışık şiddetidir; bu noktada net gaz alışverişi sıfırdır')],
  ad=[A('Solunum hızlarını oku','Işık şiddeti sıfırken fotosentez yoktur; eğrilerin y eksenini kestiği değerler solunumda tüketilen O₂ yi verir.','X: 4 birim · Y: 1 birim'),
      A('İşaretli noktadaki net değerleri oku','Işık şiddeti 4 iken X in net değeri 4, Y ninki 3 birimdir.','X: 4 · Y: 3'),
      A('Toplam fotosentezi hesapla','Toplam = net + solunum.','X: 4 + 4 = 8 · Y: 3 + 1 = 4'),
      A('Farkı bul','Toplam fotosentezler arasındaki fark istenmektedir.','8 − 4 = 4')],
  puf='Eksendeki net değerler fotosentezin tamamı değildir; y eksenindeki negatif başlangıç değeri solunumu verir ve eklenmelidir.',sekil=SK16)

# 17 · zor · öncüllü · kapalı kapta CO2
pre17=[('K anında bitkide fotosentez hızı, hücresel solunum hızından büyüktür.',False,'K de CO₂ derişimi en yüksektir ve eğri yataydır; iki hız eşittir'),
       ('L anında bitkinin birim zamanda fotosentezle tükettiği CO₂ miktarı, solunumla ürettiği CO₂ miktarından fazladır.',True,'L de CO₂ derişimi azalmaktadır'),
       ('M anından sonraki CO₂ artışı, bu andan sonra bitkide fotosentezin durduğunu gösterir.',False,'ışık hâlâ verilmektedir ve fotosentez sürer; yalnızca solunum hızı fotosentezi geçmiştir')]
s17,sr17,d17,y17,i17=oncul(pre17,False,'A')
Q('17','fak','zor','öncüllü','Kapalı kapta gaz değişimi','Kapalı kapta CO₂ değişim grafiğinden fotosentez ve solunum hızlarını karşılaştırır.',
  'Kaptaki CO₂ derişiminin değişimi, solunumla üretilen ve fotosentezle tüketilen CO₂ nin farkını verir; eğri yatayken iki hız eşittir.','CO₂ derişiminin arttığı her anda fotosentezin durduğunu düşünmek.','kapalı kapta CO₂–zaman grafiği',
  metin='Şekilde, saydam ve kapalı bir kapta bulunan bir bitkinin etrafındaki CO2 derişiminin 24 saat boyunca değişimi gösterilmiştir. Kap yalnızca işaretli süre boyunca aydınlatılmış, bitki dışında CO2 kaynağı yoktur ve hücresel solunum hızı sabit kabul edilmiştir.\n'+s17+'\nBuna göre, yukarıdaki ifadelerden hangileri doğrudur?',
  dogru=d17,sira=sr17,yan=y17,istenen='Doğru olan öncüller.',
  ip=['Eğrinin eğimi CO₂ nin arttığını mı azaldığını mı gösterdiğine, yatay olduğu noktada iki hızın nasıl olması gerektiğine bak.'],
  bilgi=[B('Kapalı kapta gaz değişimi','solunum CO₂ üretir, fotosentez CO₂ tüketir · derişim, bu iki hızın farkına göre artar, azalır ya da sabit kalır'),
         B('Hız eşitliği','CO₂ derişimi değişmiyorsa üretim ve tüketim hızları birbirine eşittir')],
  ad=[A('Eğriyi bölgelere ayır','Karanlıkta yalnız solunum vardır; ışıkta ise fotosentez ve solunum birlikte sürer.','Karanlık: CO₂ artar · ışık: farklı eğimler'),
      A('K ve M noktalarını yorumla','K ve M de eğri yataydır; K de CO₂ artıştan azalışa, M de azalıştan artışa döner.','K, M: üretim = tüketim'),
      A('Öncülleri değerlendir','K de hızlar eşittir (1. öncül yanlış); L de CO₂ azalmaktadır (2. öncül doğru); M den sonra ışık sürdüğü için fotosentez durmaz (3. öncül yanlış).',i17)],
  puf='Kaptaki CO₂ derişimi yatay olduğunda fotosentez ve solunum hızları eşittir; artış fotosentezin durduğunu göstermez.',sekil=SK17)

# 18 · zor · öncüllü · ışık kesilince Calvin ara ürünleri
pre18=[('K eğrisi PGA, L eğrisi RuBP miktarındaki değişimi göstermektedir.',False,'ışık kesilince PGA birikir; yani artan L, PGA yı gösterir'),
       ('Işık kapatıldıktan sonra ATP ve NADPH üretiminin azalması, PGA nın PGAL a dönüşümünü yavaşlatır.',True,'PGA nın indirgenmesi için ATP ve NADPH gerekir; azalınca PGA birikir'),
       ('Işık kapatıldıktan sonra RuBP miktarının azalması, CO₂ nin bağlanma hızını düşürür.',True,'CO₂ yi RuBP bağlar; RuBP azalınca bağlanma yavaşlar')]
s18,sr18,d18,y18,i18=oncul(pre18,False,'E')
Q('18','cal','zor','öncüllü','Calvin döngüsü ara ürünleri','Işık kesilince RuBP ve PGA miktarlarındaki değişimi ışığa bağımlı evreyle ilişkilendirir.',
  'Calvin döngüsü ışığı doğrudan kullanmasa da ışığa bağımlı evrenin ATP ve NADPH sine bağımlıdır; ışık kesilince PGA birikir, RuBP azalır.','Calvin döngüsünün ışık olmadan da uzun süre sürebileceğini düşünmek.','ışık kapatılınca RuBP–PGA değişimi',
  metin='CO2 bakımından zengin ortamda yetiştirilen yeşil alg hücreleri, ışıkta fotosentez yaparken bir süre sonra ışık kapatılıyor ve Calvin döngüsünün iki ara ürünü olan RuBP ile PGA nın miktarları ölçülüyor. Sonuçlar K ve L eğrileriyle şekilde verilmiştir.\n'+s18+'\nBuna göre, yukarıdaki ifadelerden hangileri doğrudur?',
  dogru=d18,sira=sr18,yan=y18,istenen='Doğru olan öncüller.',
  ip=['Işık kapatılınca ışığa bağımlı evrenin hangi ürünlerinin azaldığını ve bu ürünlerin Calvin döngüsünde hangi basamakta kullanıldığını düşün.'],
  bilgi=[B('Calvin döngüsü','CO₂ yi RuBP bağlar ve PGA oluşur · PGA, ATP ve NADPH ile PGAL a dönüştürülür · PGAL ın bir kısmı ATP ile RuBP ye çevrilir'),
         B('Işık ve Calvin döngüsü','döngü ışığı doğrudan kullanmaz, ama ışığa bağımlı evrenin ürünleri olan ATP ve NADPH ye bağımlıdır')],
  ad=[A('Eğrileri tanımla','Işıktan sonra L artıyor, K azalıyor; PGA, ATP ve NADPH yetersizliğinden birikir, RuBP ise yenilenemediğinden azalır.','L: PGA · K: RuBP'),
      A('İlk öncülü değerlendir','Eğrilerin kimliği öncülde tersine verilmiş.','1. öncül: yanlış'),
      A('ATP ve NADPH etkisini bul','Işık kapanınca bu ürünler azalır ve PGA → PGAL basamağı yavaşlar.','2. öncül: doğru'),
      A('RuBP ve CO₂ ilişkisini bul','RuBP azalınca CO₂ bağlayacak molekül azalır.','3. öncül: doğru'),
      A('Öncülleri birleştir','Doğru olan öncüller seçilir.',i18)],
  puf='Calvin döngüsü “ışıksız” değil “ışığa dolaylı bağımlıdır”: ışık kesilince ATP ve NADPH biter, döngü birkaç dakika içinde durur.',sekil=SK18)

# 19 · orta · olumsuz · ETS karşılaştırma
d19='Elektronların son alıcısının oksijen olması'
o19=['Elektronların zarda yer alan taşıyıcılar aracılığıyla aktarılması','Protonların zarın bir yanında derişim farkı oluşturacak biçimde birikmesi','ATP sentaz enzimi aracılığıyla ADP nin fosforillenmesi','Zarla çevrili bir organelin zar sisteminde gerçekleşmesi']
Q('19','isik','orta','düz','Fotosentez ve solunum karşılaştırması','Işığa bağımlı elektron taşınımı ile oksijenli solunum ETS sini karşılaştırır.',
  'Her iki zincirde de elektron taşıyıcılar, proton gradyanı ve ATP sentaz vardır; fark son elektron alıcısıdır (NADP⁺ ya da O₂).','Fotosentez ve solunumun elektron zincirlerinin son alıcılarını karıştırmak.','ışığa bağımlı tepkimeler ve solunum ETS si',
  metin='Bir bitki hücresinde, kloroplastların tilakoit zarlarındaki elektron taşınımı ile mitokondrinin iç zarındaki elektron taşıma sistemi karşılaştırılıyor. Bu iki sürecin benzer ve farklı yönleri tabloya yazılıyor.\nBuna göre, aşağıdakilerden hangisi bu iki sürecin ortak özelliği değildir?',
  dogru=d19,sira=yer('A',d19,o19),
  yan=[(o19[0],'İki süreçte de elektronlar zardaki taşıyıcılar arasında aktarılır; ifade ortak bir özelliktir.','bilgi'),
       (o19[1],'İki süreçte de proton gradyanı oluşur; ortak özellik olduğu için bu şık yanlıştır.','bilgi'),
       (o19[2],'Her ikisinde de ATP sentaz ADP yi fosforiller; ortak özelliktir.','bilgi'),
       (o19[3],'Kloroplast ve mitokondri zarla çevrili organellerdir ve süreçler zarlarında gerçekleşir; ortak özelliktir.','bilgi')],
  istenen='İki sürecin ortak özelliği olmayan ifade.',
  ip=['Işığa bağımlı tepkimelerde elektronların son olarak hangi moleküle aktarıldığını, solunumda ise hangisine aktarıldığını karşılaştır.'],
  bilgi=[B('Solunumda ETS','NADH ve FADH₂ den gelen elektronlar iç zardaki taşıyıcılardan geçer ve son olarak O₂ ye aktarılır; ATP kemiozmozla sentezlenir'),
         B('Işığa bağımlı evrede ETS','elektronlar tilakoit zardaki taşıyıcılardan geçer, son olarak NADP⁺ ya aktarılır ve NADPH oluşur')],
  ad=[A('Benzerlikleri sırala','İki süreçte de taşıyıcılar, proton gradyanı ve ATP sentaz vardır; ikisi de zarlı organelde yürür.','Taşıyıcı, gradyan, ATP sentaz, organel zarı: ortak'),
      A('Farkı bul','Solunumda son elektron alıcısı O₂, ışığa bağımlı tepkimelerde NADP⁺ dır.','Son alıcı: O₂ ≠ NADP⁺'),
      A('Ortak olmayan ifadeyi seç','Son alıcının oksijen olması yalnız solunuma özgüdür.','Cevap: son alıcının oksijen olması')],
  puf='İki zincir de aynı düzenekle çalışır; ayıran şey son elektron alıcısıdır: fotosentezde NADP⁺, solunumda O₂.')

# 20 · orta · olumsuz · stoma kapanması
d20='Fotosentez durduğu için bitki hücrelerinde hücresel solunumun da durması'
o20=['Calvin döngüsünde CO₂ nin RuBP ye bağlanma hızının azalması','Stromada ATP ve NADPH nin birikmeye başlaması','Işığa bağımlı tepkimelerin hızının azalması','Yaprak yüzeyinden O₂ çıkışının azalması']
Q('20','fak','orta','düz','CO₂ sınırlaması','Stomaların kapanmasıyla CO₂ nin sınırlayıcı olduğu durumda evrelerin birbirine etkisini yorumlar.',
  'CO₂ girişi azalınca Calvin döngüsü yavaşlar, ATP ve NADPH tüketilmez ve birikir, ışığa bağımlı evre geri besleme ile yavaşlar; solunum ise sürer.','Fotosentez yavaşlayınca solunumun da durduğunu düşünmek.','stoma kapanması ve CO₂ sınırlaması',
  metin='Kurak bir günde sıcaklık yükselince yaprakların stomalarının büyük bölümü kapanıyor ve yaprak içine CO2 girişi azalıyor. Işık şiddeti ve su dışındaki koşullar aynı kalıyor. Bir bitki fizyolojisti, kısa süre sonra kloroplastlarda ve hücrelerde olanları gözlemliyor.\nBuna göre, bu bitkide aşağıdakilerden hangisinin gerçekleştiği söylenemez?',
  dogru=d20,sira=yer('D',d20,o20),
  yan=[(o20[0],'CO₂ girişi azalınca RuBP ye bağlanan CO₂ azalır; olay gerçekleşir, bu yüzden “söylenemez” sorusunun cevabı değildir.','bilgi'),
       (o20[1],'Calvin döngüsü yavaşlayınca ATP ve NADPH tüketimi azalır ve stromada birikir; olay gerçekleşir.','bilgi'),
       (o20[2],'ATP ve NADPH birikip NADP⁺ azalınca ışığa bağımlı tepkimeler yavaşlar; olay gerçekleşir.','bilgi'),
       (o20[3],'Fotosentez hızı düşünce suyun fotolizi azalır ve O₂ çıkışı da azalır; olay gerçekleşir.','dikkat')],
  istenen='Gerçekleştiği söylenemeyecek olay.',
  ip=['Kuraklığın hangi evreyi doğrudan etkilediğini belirle ve bu evredeki yavaşlamanın diğer evre ve solunum üzerindeki etkisini sırayla düşün.'],
  bilgi=[B('Stomalar','yaprağın gaz alışverişini sağlar · kapanınca CO₂ girişi ve O₂ çıkışı azalır'),
         B('Evrelerin bağlantısı','Calvin döngüsü yavaşlayınca ATP ve NADPH harcanmaz, ışığa bağımlı evrenin girdisi olan NADP⁺ azalır · hücresel solunum fotosentezden bağımsız yürür')],
  ad=[A('İlk etkiyi belirle','Stoma kapanınca CO₂ girişi azalır ve Calvin döngüsü yavaşlar.','CO₂ ↓ → Calvin yavaş'),
      A('Evre bağlantısını yürüt','ATP ve NADPH tüketilmediği için birikir; NADP⁺ azalınca ışığa bağımlı evre yavaşlar ve O₂ çıkışı düşer.','Calvin ↓ → ATP, NADPH ↑ → ışığa bağımlı evre ↓ → O₂ ↓'),
      A('Solunumu değerlendir','Hücresel solunum canlı hücrede sürer; fotosentezin yavaşlaması onu durdurmaz.','Solunum: devam eder'),
      A('Yanlış sonucu seç','Solunumun durduğunu söyleyen olay gerçekleşmez.','Cevap: solunumun durması')],
  puf='Fotosentez yavaşlasa da solunum sürer; evreler arasındaki ilişki ATP, NADPH ve NADP⁺ üzerinden kurulur.')

# ============================ YAZ ============================
for qq in P.ANA: qq['kardes']=None
# sağlama
import collections,statistics
assert len(P.ANA)==20
P.yaz(os.path.join(GD,'fotosentez-1.json'),'/tmp/bos-fotosentez.json')
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=KEY))['kartlar'].append(c['id'])
json.dump(dict(konu=KONU_AD,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2018–2026 Biyoloji (yalnız mantık), MEB 12. sınıf.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','abfotosentez.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
