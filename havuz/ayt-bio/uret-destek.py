"""AYT Biyoloji · Destek ve Hareket Sistemi · 20 soru (kardeş yok, ipucu 1). Şekiller TikZ/pgfplots; sarkomer ölçüleri ve öncül değerleri Python'da hesaplanıp assert edilir."""
import sys,os,json,random,itertools
from fractions import Fraction as Fr
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-bio'))
import _hafif_bio as H
from _hafif_bio import *
from _hafif_bio3 import onc
KONU_AD='Destek ve Hareket Sistemi'; KEY='abio|Destek ve Hareket Sistemi'
P=Parti('destek',KONU_AD,KEY,ders='AYT Biyoloji',idon='aytbio'); H.KONU=KONU_AD
KAYNAK='ÖSYM AYT 2018–2026 Biyoloji destek-hareket soruları (yalnız mantık) · MEB 11. sınıf Destek ve Hareket Sistemi'
TIP={'kemik':('ds-kemik-kikirdak','Kemik ve kıkırdak doku yapısı'),'eklem':('ds-eklem','Eklemler ve hareket yeteneği'),
     'kas':('ds-kas-turleri','Kas türlerinin yapı ve işlevi'),'sark':('ds-sarkomer','Sarkomer yapısı ve boy değişimi'),
     'kasilma':('ds-kasilma','Kas kasılma mekanizması'),'enerji':('ds-kas-enerji','Kasta enerji kaynakları'),'hareket':('ds-kas-hareket','Kas–kemik ilişkisi ve karşıt çalışan kaslar')}
def Q(no,tp,z,kalip,alt,kaz,fikir,tuzak,ozet,ad,**k):
    assert len(k['ip'])==1
    t,tn=TIP[tp]; kart(f'K-ABDES-{no}',alt,fikir,tuzak,z,kalip,len(ad),t,tn,KAYNAK)
    mk(P,no,ad=ad,adim=len(ad),tipId=t,tip=tn,z=z,alt=alt,kaz=kaz,kalip=kalip,kart=f'K-ABDES-{no} ({ozet})',**k)
def tablo_r(b,r): return tablo_svg(b,r).replace('style="fill:currentColor;stroke:none" fill-opacity=".08"','style="fill:#16A34A;stroke:none" fill-opacity=".28"')
def tk(g,sc=1.0): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small,scale=%s]\n%s\n\\end{tikzpicture}'%(sc,g))
AR='-{Stealth[length=2.2mm,width=1.8mm]}'
def dd(v,fact): return (v,f'{fact} Bu nedenle ifade {"doğrudur" if v else "yanlıştır"}.')
def tek_(secs,hedef,harf):
    """secs: [(metin,bool,neden)] 5 adet (sırası serbest); doğru şık 'harf' konumuna yerleştirilir."""
    assert len(secs)==5
    h=[s for s in secs if s[1]==hedef]; assert len(h)==1,[s[0] for s in h]
    dig=[s for s in secs if s[1]!=hedef]; i='ABCDE'.index(harf); sira=dig[:i]+h+dig[i:]
    yan=[]
    for m,b,n in dig:
        yan.append((m,(f'Bu ifadeyi doğru sanmış; oysa {n}' if hedef else f'Bu ifadeyi yanlış sanmış; oysa doğrudur: {n}'),'bilgi'))
    return dict(dogru=h[0][0],yan=yan,sira=[s[0] for s in sira])

# ======================= ŞEKİLLER =======================
# --- uzun kemik kesiti ---
def kemik_sekil(lab):
    """lab: {'kikirdak','plak','sunger','sikisik','ilik','periost'} -> Romen rakamı (yalnız verilenler etiketlenir)"""
    rnd=random.Random(5)
    out_=[(-0.55,-1.5),(-0.55,1.5),(-1.0,1.8),(-1.0,3.05),(1.0,3.05),(1.0,1.8),(0.55,1.5),(0.55,-1.5),(1.0,-1.8),(1.0,-3.05),(-1.0,-3.05),(-1.0,-1.8)]
    pth='\\draw[rounded corners=5pt]'+' -- '.join(f'({x},{y})' for x,y in out_)+' -- cycle'
    import math
    b=['\\fill[brown!35,rounded corners=5pt] '+' -- '.join(f'({x},{y})' for x,y in out_)+' -- cycle;']
    for sg in (1,-1):                      # süngerimsi doku (epifiz) + iç ağ
        y0,y1=(2.12,2.93) if sg>0 else (-2.93,-2.12)
        b.append(f'\\fill[brown!12] (-1.0,{y0}) rectangle (1.0,{y1});')
        seg=[]
        for i in range(8):
            for j in range(3):
                x=-0.75+i*0.21+rnd.uniform(-.04,.04); y=y0+.15+j*0.27+rnd.uniform(-.04,.04); a=rnd.choice((20,60,120,160)); l=.26
                seg.append(f'({x:.2f},{y:.2f}) -- ({x+l*math.cos(math.radians(a)):.2f},{y+l*math.sin(math.radians(a)):.2f})')
        b.append('\\draw[brown!75!black,line width=.7pt] '+' '.join(seg)+';')
        pl=(1.9,2.12) if sg>0 else (-2.12,-1.9)
        b.append(f'\\fill[cyan!35] (-1.0,{pl[0]}) rectangle (1.0,{pl[1]});')
        cp=(2.93,3.05) if sg>0 else (-3.05,-2.93)
        b.append(f'\\fill[cyan!35] (-1.0,{cp[0]}) rectangle (1.0,{cp[1]});')
    b.append('\\fill[yellow!35] (-0.3,-1.9) rectangle (0.3,1.9);')   # ilik boşluğu
    b.append('\\draw[brown!60!black,line width=.5pt] (-0.3,-1.9) -- (-0.3,1.9) (0.3,-1.9) -- (0.3,1.9);')
    for sg in (1,-1):
        for yy in ((1.9,2.12,2.93) if sg>0 else (-2.12,-1.9,-2.93)): b.append(f'\\draw[line width=.5pt] (-1.0,{yy}) -- (1.0,{yy});')
    b.append(pth.replace('\\draw[rounded','\\draw[line width=1.6pt,rounded')+';')
    b.append('\\draw[line width=1.8pt,violet!60] (-0.6,-1.5) -- (-0.6,1.5) (0.6,-1.5) -- (0.6,1.5);')
    tg={'kikirdak':((0.55,3.0),3.0),'sunger':((0.45,2.5),2.45),'plak':((0.7,2.0),1.9),'periost':((0.6,1.0),1.3),'sikisik':((0.44,0.1),0.6),'ilik':((0.1,-0.6),-0.1)}
    ly={'kikirdak':3.0,'sunger':2.45,'plak':1.9,'periost':1.25,'sikisik':0.6,'ilik':-0.05}
    for k,r in lab.items():
        (tx,ty),_=tg[k]
        b.append(f'\\node[anchor=west,font=\\large\\bfseries] at (2.3,{ly[k]}) {{{r}}};\\draw[{AR},line width=.8pt] (2.25,{ly[k]}) -- ({tx},{ty});')
    return tk('\n'.join(b),1.0)

# --- oynar eklem kesiti ---
def eklem_sekil(lab):
    """lab: {'kikirdak','sivi','kapsul','bag','kemik'} -> Romen rakamı"""
    b=[]
    b.append('\\draw[rounded corners=6pt,line width=1.4pt,fill=brown!25] (-0.55,3.2) -- (-0.55,1.7) -- (-1.0,1.5) -- (-1.0,0.35) -- (1.0,0.35) -- (1.0,1.5) -- (0.55,1.7) -- (0.55,3.2);')
    b.append('\\draw[rounded corners=6pt,line width=1.4pt,fill=brown!25] (-0.55,-3.2) -- (-0.55,-1.7) -- (-1.0,-1.5) -- (-1.0,-0.35) -- (1.0,-0.35) -- (1.0,-1.5) -- (0.55,-1.7) -- (0.55,-3.2);')
    b.append('\\fill[cyan!35] (-1.0,0.17) rectangle (1.0,0.35);\\fill[cyan!35] (-1.0,-0.35) rectangle (1.0,-0.17);')
    b.append('\\draw[line width=.6pt] (-1.0,0.17) -- (1.0,0.17) (-1.0,-0.17) -- (1.0,-0.17);')
    b.append('\\fill[blue!12] (-1.0,-0.17) rectangle (1.0,0.17);')
    b.append('\\draw[line width=3pt,orange!80!black] (-1.0,1.3) .. controls (-1.3,0.5) and (-1.3,-0.5) .. (-1.0,-1.3);')
    b.append('\\draw[line width=3pt,orange!80!black] (1.0,1.3) .. controls (1.3,0.5) and (1.3,-0.5) .. (1.0,-1.3);')
    b.append('\\draw[line width=4pt,violet!70] (-0.55,2.4) .. controls (-1.9,1.0) and (-1.9,-1.0) .. (-0.55,-2.4);')
    tg={'kikirdak':((0.8,0.27),(2.6,1.0)),'sivi':((0.4,0.0),(2.6,0.0)),'kapsul':((1.25,-0.5),(2.6,-1.0)),'bag':((-1.55,0.0),(-3.0,0.0)),'kemik':((0.3,2.4),(2.6,2.2))}
    for k,r in lab.items():
        t,l=tg[k]
        b.append(f'\\node[font=\\large\\bfseries] at ({l[0]+(.2 if l[0]>0 else -.2)},{l[1]}) {{{r}}};\\draw[{AR},line width=.8pt] ({l[0]-(.05 if l[0]>0 else -.05)},{l[1]}) -- ({t[0]},{t[1]});')
    return tk('\n'.join(b),0.75)

# --- kas hücreleri K (düz) L (iskelet) M (kalp) ---
def kashucre_sekil(ad):
    """ad: {'duz':harf,'iskelet':harf,'kalp':harf}"""
    b=[]
    # düz kas: iğ biçimli, tek merkezî çekirdek, çizgisiz
    y=0
    b.append(f'\\draw[line width=1.2pt,fill=pink!35] (0.4,{y+.4}) .. controls (1.5,{y+1.0}) and (4.5,{y+1.0}) .. (5.6,{y+.4}) .. controls (4.5,{y-.2}) and (1.5,{y-.2}) .. (0.4,{y+.4});')
    b.append(f'\\draw[line width=1pt,fill=violet!55] (3.0,{y+.4}) ellipse (.55 and .2);')
    b.append(f'\\node[font=\\large\\bfseries] at (-.3,{y+.4}) {{{ad["duz"]}}};')
    # iskelet kası: uzun silindir, çok çekirdek çevrede, enine çizgili
    y=-1.9
    b.append(f'\\draw[line width=1.2pt,rounded corners=4pt,fill=red!12] (0.4,{y}) rectangle (5.6,{y+.8});')
    for i in range(1,21): b.append(f'\\draw[red!55!black,line width=.5pt] ({.4+i*.25:.2f},{y}) -- ({.4+i*.25:.2f},{y+.8});')
    for x in (1.0,2.1,3.3,4.5): b.append(f'\\draw[line width=1pt,fill=violet!55] ({x},{y+.68}) ellipse (.25 and .09);')
    b.append(f'\\node[font=\\large\\bfseries] at (-.3,{y+.4}) {{{ad["iskelet"]}}};')
    # kalp kası: dallanmış, çizgili, tek çekirdek, ara diskler
    y=-4.0
    sh=[(0.4,0.0),(0.4,.8),(2.5,.8),(2.5,1.4),(3.5,1.4),(3.5,.8),(5.6,.8),(5.6,0.0),(3.5,0.0),(3.5,-.6),(2.5,-.6),(2.5,0.0)]
    b.append('\\draw[line width=1.2pt,rounded corners=3pt,fill=red!18] '+' -- '.join(f'({x},{y+yy})' for x,yy in sh)+' -- cycle;')
    for i in range(1,21):
        x=.4+i*.25
        lo,hi=(0.0,.8)
        if 2.5<x<3.5: lo,hi=-.6,1.4
        b.append(f'\\draw[red!55!black,line width=.5pt] ({x:.2f},{y+lo}) -- ({x:.2f},{y+hi});')
    for x in (1.3,4.7): b.append(f'\\draw[line width=2.6pt] ({x},{y}) -- ({x},{y+.8});')
    for x in (0.85,3.0,5.15): b.append(f'\\draw[line width=1pt,fill=violet!55] ({x},{y+.4}) ellipse (.25 and .13);')
    b.append(f'\\node[font=\\large\\bfseries] at (-.3,{y+.4}) {{{ad["kalp"]}}};')
    return tk('\n'.join(b),0.8)

# --- sarkomer ---
THIN=Fr(1); THICK=Fr(8,5)
def sark_g(L,x0=0.0,y0=0.0,U=1.45,etiket=None,H=1.0):
    """L: Z–Z (µm). Z çizgileri x0 ve x0+L·U; ince iplikçikler Z'ye bağlı (1,0 µm), kalın iplikçik ortada (1,6 µm)."""
    L=Fr(L); assert L>=2*THIN
    s=[]; w=float(L)*U
    rows_thin=(-.62,-.21,.21,.62); rows_thick=(-.42,0.0,.42)
    for r in rows_thin:
        s.append(f'\\draw[blue!70!black,line width=1.3pt] ({x0:.3f},{y0+r:.3f}) -- ({x0+float(THIN)*U:.3f},{y0+r:.3f});')
        s.append(f'\\draw[blue!70!black,line width=1.3pt] ({x0+w:.3f},{y0+r:.3f}) -- ({x0+w-float(THIN)*U:.3f},{y0+r:.3f});')
    c=x0+w/2
    for r in rows_thick:
        s.append(f'\\draw[red!75!black,line width=3.2pt] ({c-float(THICK)/2*U:.3f},{y0+r:.3f}) -- ({c+float(THICK)/2*U:.3f},{y0+r:.3f});')
    for x in (x0,x0+w): s.append(f'\\draw[line width=2.4pt] ({x:.3f},{y0-.85}) -- ({x:.3f},{y0+.85});')
    return '\n'.join(s)
def brace_alt(x1,x2,y,rom,yt=None):   # alt ölçü çizgisi
    yt=y-.45 if yt is None else yt
    return (f'\\draw[<->,line width=.8pt] ({x1:.3f},{y}) -- ({x2:.3f},{y});\\node[font=\\large\\bfseries] at ({(x1+x2)/2:.3f},{yt}) {{{rom}}};')
def brace_ust(x1,x2,y,rom,yt=None):
    yt=y+.45 if yt is None else yt
    return (f'\\draw[<->,line width=.8pt] ({x1:.3f},{y}) -- ({x2:.3f},{y});\\node[font=\\large\\bfseries] at ({(x1+x2)/2:.3f},{yt}) {{{rom}}};')
def sark_sekil13():
    U=1.45; L=Fr(3); w=float(L)*U
    b=[sark_g(L,0,0,U)]
    # I: Z–Z, II: kalın iplikçik boyu, III: yalnız kalın iplikçiklerin bulunduğu orta bölge
    c=w/2; t=float(THICK)/2*U; h=float(L-2*THIN)/2*U
    b.append(brace_alt(0,w,-1.15,'I',yt=-1.62))
    b.append(brace_ust(c-t,c+t,1.1,'II'))
    b.append(f'\\draw[dotted,line width=.8pt] ({c-h:.3f},-.85) -- ({c-h:.3f},-2.5) ({c+h:.3f},-.85) -- ({c+h:.3f},-2.5);')
    b.append(brace_alt(c-h,c+h,-2.5,'III',yt=-2.97))
    return tk('\n'.join(b),1.0)
def sark_sekil14():
    U=1.45; b=[]
    for Lz,y,ad,lab in ((Fr(14,5),0,'X','2,8 µm'),(Fr(11,5),-3.2,'Y','2,2 µm')):
        w=float(Lz)*U
        b.append(sark_g(Lz,0,y,U)); b.append(f'\\node[font=\\large\\bfseries] at (-.7,{y}) {{{ad}}};')
        b.append(f'\\draw[<->,line width=.8pt] (0,{y-1.15}) -- ({w:.3f},{y-1.15});\\node[font=\\normalsize\\bfseries] at ({w/2:.3f},{y-1.6}) {{{lab}}};')
    return tk('\n'.join(b),0.95)

def sark_sekil15():
    U=1.65; L=Fr(13,5); w=float(L)*U
    b=[sark_g(L,0,0,U)]
    th=float(THIN)*U; c=w/2; t=float(THICK)/2*U
    b.append(f'\\draw[<->,line width=.8pt] (0,1.0) -- ({th:.3f},1.0);\\node[font=\\normalsize\\bfseries] at ({th/2:.3f},1.45) {{1,0 µm}};')
    b.append(f'\\draw[<->,line width=.8pt] ({c-t:.3f},-1.0) -- ({c+t:.3f},-1.0);\\node[font=\\normalsize\\bfseries] at ({c:.3f},-1.45) {{1,6 µm}};')
    b.append(f'\\draw[<->,line width=.8pt] (0,-1.85) -- ({w:.3f},-1.85);\\node[font=\\normalsize\\bfseries] at ({w/2:.3f},-2.3) {{2,6 µm}};')
    return tk('\n'.join(b),0.95)

# --- motor nöron – kas lifi şeması (nöromüsküler kavşak) ---
def kavsak_sekil(lab):
    """lab: {'noron','sr','mito','miyofibril','zar'}"""
    b=[]
    b.append('\\draw[line width=1.4pt,rounded corners=6pt,fill=red!8] (2.0,0) rectangle (9.0,3.2);')
    for yy in (0.55,1.95):
        b.append(f'\\draw[line width=1.2pt,rounded corners=5pt,orange!80!black,fill=orange!25] (2.35,{yy-.2}) rectangle (8.65,{yy+.75});')
        b.append(f'\\draw[line width=.9pt,rounded corners=3pt,fill=red!30] (2.5,{yy}) rectangle (8.5,{yy+.55});')
        for i in range(1,24): b.append(f'\\draw[red!60!black,line width=.5pt] ({2.5+i*.25:.2f},{yy}) -- ({2.5+i*.25:.2f},{yy+.55});')
    for x in (4.2,6.0,7.8):
        b.append(f'\\draw[line width=.9pt,fill=orange!25] ({x},1.6) ellipse (.4 and .2);\\draw[line width=.5pt] ({x-.3},1.6) -- ({x-.2},1.7) -- ({x-.1},1.5) -- ({x},1.7) -- ({x+.1},1.5) -- ({x+.2},1.7) -- ({x+.3},1.6);')
    b.append('\\draw[line width=1.4pt] (-0.8,1.6) -- (1.2,1.6);')
    b.append('\\draw[line width=1.4pt,fill=green!20] (1.45,1.6) ellipse (.5 and .75);')
    for (x,y) in ((1.3,1.9),(1.5,1.55),(1.25,1.3),(1.6,1.95)): b.append(f'\\fill[green!50!black] ({x},{y}) circle (.07);')
    tg={'noron':((1.45,2.3),(1.2,3.6)),'zar':((9.0,1.7),(10.0,2.4)),'sr':((4.4,2.68),(4.4,3.9)),'mito':((6.0,1.4),(6.0,-.9)),'miyofibril':((7.6,2.22),(8.0,3.9))}
    for k,r in lab.items():
        t,l=tg[k]
        b.append(f'\\node[font=\\large\\bfseries] at ({l[0]},{l[1]}) {{{r}}};\\draw[{AR},line width=.8pt] ({l[0]},{l[1]+(-.3 if l[1]>2 else .3)}) -- ({t[0]},{t[1]});')
    return tk('\n'.join(b),0.62)

# --- kol (dirsek bükülmesi) ---
def kol_sekil(lab):
    """lab: {'arka':romen,'on':romen}. Ön (iç) taraftaki kas kasılmış (kısa, kalın); arka kas gevşemiş (uzun, ince)."""
    b=[]
    b.append('\\draw[line width=10pt,gray!55,line cap=round] (0,4) -- (0,0);\\draw[line width=10pt,gray!55,line cap=round] (0,0) -- (2.6,1.5);')
    b.append('\\draw[line width=1pt,fill=white] (0,0) circle (.14);')
    # ön kas (kasılı, kalın, kısa)
    b.append('\\draw[line width=1.1pt,fill=red!35] (0.2,3.7) .. controls (1.3,3.2) and (1.35,1.6) .. (0.85,0.6) .. controls (0.6,0.45) and (0.4,0.7) .. (0.35,1.2) .. controls (0.3,2.2) and (0.2,3.0) .. (0.2,3.7);')
    b.append('\\draw[line width=.6pt,red!60!black] (0.3,3.4) .. controls (0.9,2.6) and (0.95,1.6) .. (0.7,0.75);')
    # arka kas (gevşek, ince, uzun)
    b.append('\\draw[line width=1.1pt,fill=red!12] (-0.2,3.8) .. controls (-0.6,2.6) and (-0.6,0.9) .. (-0.28,-0.1) .. controls (-0.2,-0.12) and (-0.12,-0.1) .. (-0.1,0.0) .. controls (-0.12,1.2) and (-0.12,2.6) .. (-0.2,3.8);')
    b.append('\\draw[line width=.6pt,red!60!black] (-0.3,3.4) .. controls (-0.4,2.4) and (-0.4,1.0) .. (-0.24,0.0);')
    b.append(f'\\draw[{AR},line width=1.2pt] (2.86,1.65) arc[start angle=30,end angle=58,radius=3.3];')
    on,ar=lab['on'],lab['arka']
    b.append(f'\\node[font=\\large\\bfseries] at (2.3,3.2) {{{on}}};\\draw[{AR},line width=.8pt] (2.05,3.1) -- (1.15,2.5);')
    b.append(f'\\node[font=\\large\\bfseries] at (-1.6,2.0) {{{ar}}};\\draw[{AR},line width=.8pt] (-1.35,2.0) -- (-0.5,2.0);')
    return tk('\n'.join(b),0.85)

# --- grafik: ATP, kreatin fosfat, laktik asit ---
import math as _m
ATP=lambda t:5.0-0.4*(t/60.0)
KP=lambda t:2.0+23.0*_m.exp(-t/18.0)
LA=lambda t:1.0+14.0*(1-_m.exp(-t/35.0))
def enerji_sekil():
    pts=lambda f:' '.join(f'({t},{f(t):.2f})' for t in range(0,61,3))
    b=['\\begin{axis}[width=7.8cm,height=5.4cm,xmin=0,xmax=60,ymin=0,ymax=28,xtick={0,10,20,30,40,50,60},ytick={0,5,10,15,20,25},axis lines=left,xlabel={Süre (s)},ylabel={Derişim (mmol/L)},tick label style={font=\\small},label style={font=\\small},every axis plot/.append style={line width=1.5pt}]',
       f'\\addplot[blue!70!black,smooth] coordinates {{{pts(ATP)}}};',f'\\addplot[red!75!black,smooth,dashed] coordinates {{{pts(KP)}}};',f'\\addplot[green!45!black,smooth,dash dot] coordinates {{{pts(LA)}}};',
       '\\node[font=\\large\\bfseries,blue!70!black] at (axis cs:55,7.2) {X};\\node[font=\\large\\bfseries,red!75!black] at (axis cs:4,24.6) {Y};\\node[font=\\large\\bfseries,green!45!black] at (axis cs:55,17.2) {Z};','\\end{axis}']
    return tk('\n'.join(b))

# --- deney: zarı geçirgen kas lifleri ---
def deney_sekil(satir):
    """satir: {'Ca':[4],'ATP':[4],'Miyozin':[4],'Kasılma':[4]} (True/False)"""
    b=[]; xs=[2.6,4.4,6.2,8.0]; hd=['K','L','M','N']
    for x,h in zip(xs,hd):
        b.append(f'\\draw[line width=1.2pt,fill=blue!8] ({x-.6},0) -- ({x-.6},1.1) -- ({x+.6},1.1) -- ({x+.6},0) -- cycle;')
        b.append(f'\\draw[line width=1.2pt] ({x-.6},1.1) -- ({x-.6},1.7) ({x+.6},1.1) -- ({x+.6},1.7);')
        b.append(f'\\draw[line width=2pt,red!70!black] ({x-.35},.5) .. controls ({x-.1},.7) and ({x+.1},.3) .. ({x+.35},.5);')
        b.append(f'\\node[font=\\large\\bfseries] at ({x},2.1) {{{h}}};')
    names=[('Ca','Ca$^{2+}$'),('ATP','ATP'),('Miyozin','Miyozin iplikçikleri'),('Kasılma','Kasılma')]
    for i,(k,ad) in enumerate(names):
        y=-.7-i*.62
        b.append(f'\\node[anchor=east,font=\\small] at (1.75,{y}) {{{ad}}};')
        for x,v in zip(xs,satir[k]): b.append(f'\\node[font=\\small\\bfseries] at ({x},{y}) {{{"var" if v else "yok"}}};')
        b.append(f'\\draw[line width=.5pt,gray] (-1.2,{y-.31}) -- (8.8,{y-.31});')
    b.append(f'\\draw[line width=.5pt,gray] (-1.2,-.39) -- (8.8,-.39);')
    return tk('\n'.join(b),0.75)

# ======================= SORULAR =======================
def adim_onc(d,s): return A(f'{s}. yargıyı değerlendir',d[s][1],f'{s}: '+('doğru' if d[s][0] else 'yanlış'))
def QO(no,tp,z,kalip,alt,kaz,fikir,tuzak,ozet,ad,o,**k):
    Q(no,tp,z,kalip,alt,kaz,fikir,tuzak,ozet,ad,dogru=o['dogru'],yan=o['yan'],sira=o['sira'],**k)

# ---------- 01 · uzun kemik kesiti · kolay · A ----------
M1={'periost':'I','kikirdak':'II','sunger':'III','sikisik':'IV','ilik':'V'}
SK1=kemik_sekil(M1)
QO('0001','kemik','kolay','şekilli','Uzun kemik yapısı','Uzun kemiğin kesitinde kemik zarını tanır ve enine büyüme ile onarımdaki rolünü bilir.',
  'Uzun kemiğin kesitinde dışta kemik zarı, uçlarda eklem kıkırdağı ve süngerimsi doku, ortada sıkı doku ile ilik boşluğu bulunur.',
  'Osteoblast içeren yapıyı kemik dokusunun iç kısımlarında (süngerimsi doku, ilik) aramak.','kemik zarı',
  [A('Bölümleri adlandır','Kesitte dışta ince bir zar, uçlarda kıkırdak başlık ve süngerimsi doku, ortada duvar oluşturan sıkı doku ve içte ilik boşluğu görülür.','I: kemik zarı · II: eklem kıkırdağı · III: süngerimsi kemik · IV: sıkı kemik · V: ilik boşluğu'),
   A('Görevi hatırla','Kırık onarımı ve kemiğin enine büyümesi, osteoblast içeren kemik zarının (periost) görevidir.','Onarım ve enine büyüme → kemik zarı'),
   A('Numarayı bul','Kemik zarı şekilde kemiği çevreleyen dış tabakadır ve I ile gösterilmiştir.','Cevap: I')],
  o=dict(dogru='I',sira=['I','II','III','IV','V'],yan=[
   ('II','II numaralı yapı eklem kıkırdağıdır; damar içermez ve kırık onarımında ya da enine büyümede görev almaz.','bilgi'),
   ('III','III numaralı bölge süngerimsi kemiktir; ilik içerir ama kemiği dıştan kalınlaştıran tabaka değildir.','bilgi'),
   ('IV','IV numaralı bölge sıkı kemik dokudur; kemik zarı bu dokunun dış yüzünü saran ayrı bir tabakadır.','bilgi'),
   ('V','V numaralı bölge ilik boşluğudur; yağ depolar, enine büyümeyi sağlayan hücreleri taşımaz.','bilgi')]),
  metin='Şekilde bir uzun kemiğin boyuna kesiti verilmiş ve bazı bölümleri I, II, III, IV ve V ile numaralandırılmıştır.\nBir kemik kırıldığında onarım ve kemiğin enine büyümesi, osteoblast hücreleri bakımından zengin bir bağ doku tabakası sayesinde gerçekleşir.\nBuna göre, bu tabaka şekilde numaralandırılmış bölümlerden hangisidir?',
  istenen='Osteoblastlı, onarım ve enine büyümeyi sağlayan tabakanın numarası.',
  ip=['Kesitin her bölümünü adlandır; kemiği kalınlaştıran hücrelerin kemik dokusunun neresinde bulunabileceğini düşün.'],
  bilgi=[B('Kemik dokusunun hücreleri','osteoblast kemik matriksini oluşturan, osteosit olgun ve matriksi koruyan, osteoklast matriksi yıkan hücredir · Kemik doku canlıdır; kan damarı ve sinir içerir')],
  puf='Görevi verilen yapıyı bulmak için önce kesitin bütün bölümlerini adlandır.',sekil=SK1)

# ---------- 02 · kemik–kıkırdak öncülleri · orta · B ----------
d2={'I':dd(False,'Osteoblastlar kemik matriksini oluşturan hücrelerdir; matriksi yıkan hücreler osteoklastlardır.'),
    'II':dd(False,'Kulak kepçesinin iskeleti elastik kıkırdaktır; lifli kıkırdak omurlar arası disklerde bulunur.'),
    'III':dd(True,'Kıkırdakta damar yoktur; besin ve gaz alışverişi hücreler arası maddeden yayılmayla olur.')}
o2=onc(d2,False,'B'); assert o2['dogru']=='I ve II'
QO('0002','kemik','orta','öncüllü','Kemik ve kıkırdak dokular','Kemik ve kıkırdak dokuların hücre ve yapı özelliklerini karşılaştırır.',
  'Osteoblast yapar, osteoklast yıkar; kulak kepçesi elastik, omurlar arası disk lifli kıkırdaktır; kıkırdak damarsızdır.',
  'Osteoblast ile osteoklastın görevlerini karıştırmak; elastik ve lifli kıkırdağın yerlerini ters sanmak.','kemik–kıkırdak öncülleri',
  [adim_onc(d2,'I'),adim_onc(d2,'II'),adim_onc(d2,'III'),A('Yanlışları birleştir','Yanlış olan yargılar I ve II’dir.','Cevap: I ve II')],
  o=o2,
  metin='İnsan iskeletini oluşturan kemik ve kıkırdak, destek dokusu olarak görev yapar. Bu dokularla ilgili üç ifade aşağıda verilmiştir.\nI. Osteoblastlar, kemik matriksini yıkarak kemiğin yeniden şekillenmesini sağlar.\nII. Kulak kepçesinin iskeletini oluşturan kıkırdak, lifli kıkırdak çeşididir.\nIII. Kıkırdak dokuda kan damarı bulunmaz; hücreler besinleri hücreler arası maddeden alır.\nBuna göre, bu ifadelerden hangileri yanlıştır?',
  istenen='Yanlış olan ifadeler.',
  ip=['Her ifadedeki hücre ya da kıkırdak türünü ayrı ayrı hatırla; görev ve yer eşleştirmelerini tek tek sına.'],
  bilgi=[B('Destek dokular','kemik ve kıkırdak, hücrelerinin arasında bol hücreler arası madde bulunan bağ doku çeşitleridir · Kıkırdak hiyalin, elastik ve lifli olmak üzere üç çeşittir; çeşitler hücreler arası maddedeki liflerin türüne ve miktarına göre ayrılır'),
         B('Kemik dokunun hücre türleri','osteoblast, osteosit ve osteoklast olmak üzere üç tür hücre bulunur; görevleri birbirinden farklıdır')],
  puf='Osteoblast “yapar”, osteoklast “yıkar”; kıkırdakta damar yoktur, çeşidi bulunduğu yer belirler.')

# ---------- 03 · uzun kemik, büyüme çağı · orta · C ----------
M3={'kikirdak':'I','plak':'II','sunger':'III','sikisik':'IV','ilik':'V'}
SK3=kemik_sekil(M3)
S3=[('I numaralı yapı kan damarlarıyla zengindir ve besinlerini doğrudan kandan alır.',False,'I numaralı yapı eklem kıkırdağıdır; damar içermez, besinleri çevresinden yayılmayla alır.'),
    ('II numaralı bölgedeki hücrelerin bölünmesi ve ürettiği dokunun kemikleşmesi, kemiğin boyuna uzamasını sağlar.',True,''),
    ('III numaralı bölgede kemik hücresi bulunmaz; yalnız kıkırdak hücreleri vardır.',False,'III numaralı süngerimsi kemik, kemik dokudur ve osteosit içerir.'),
    ('IV numaralı bölge süngerimsi doku olduğu için kırmızı kemik iliğinin tamamını barındırır.',False,'IV numaralı bölge sıkı kemik dokudur; ilik, kemiğin iç boşluklarında ve süngerimsi dokuda bulunur.'),
    ('V numaralı boşlukta bulunan ilik, ergenlik döneminde kemiğin boyuna uzamasını sağlar.',False,'V numaralı boşluktaki ilik yağ depolar ya da kan hücresi üretir; boyca uzama büyüme plağındaki kıkırdağın işidir.')]
o3=tek_([S3[0],S3[2],S3[1],S3[3],S3[4]],True,'C'); assert o3['sira'][2].startswith('II numaralı')
QO('0003','kemik','orta','şekilli','Uzun kemik yapısı','Büyüme çağındaki uzun kemiğin kesitinde yapıların bileşimini ve işlevini ilişkilendirir.',
  'Uzun kemiğin kesitindeki yapıların doku türleri ve görevleri.',
  'Yapıların doku türlerini karıştırmak.','büyüme çağında uzun kemik',
  [A('Bölümleri adlandır','Uçta eklem kıkırdağı, süngerimsi kemik, ucun altındaki kıkırdak plak, ortada sıkı kemik duvarı ve ilik boşluğu görülür.','I: eklem kıkırdağı · II: büyüme plağı · III: süngerimsi kemik · IV: sıkı kemik · V: ilik boşluğu'),
   A('Büyüme çağı bilgisini kullan','Ergenlikte kemik, uçlardaki kıkırdak plakta hücre bölünmesi ve kemikleşmeyle boyca uzar.','Boyca uzama → büyüme plağı'),
   A('Seçenekleri eleştir','Eklem kıkırdağı damarsızdır, süngerimsi doku kemik hücresi taşır, sıkı doku ilik barındırmaz, ilikteki sarı ya da kırmızı ilik uzamadan sorumlu değildir.','Uzamayı yalnız büyüme plağı açıklar')],
  o=o3,
  metin='Şekilde, ergenlik çağındaki bir bireyin uzun kemiğinin boyuna kesiti verilmiştir. Kesitte bazı bölümler I, II, III, IV ve V ile numaralandırılmıştır.\nBuna göre, numaralandırılmış bölümlerle ilgili aşağıdakilerden hangisi doğrudur?',
  istenen='Numaralı bölümlerle ilgili doğru ifade.',
  ip=['Kemiğin boyuna uzaması için hücre bölünmesi gereken bir doku düşün; kesitte kıkırdak izlenimi veren bölgelerin her birini ayrı ayrı değerlendir.'],
  bilgi=[B('Kemiğin uzaması','kemikler büyüme döneminde uçlarında kıkırdak içeren bir bölgenin etkinliğiyle boyca uzar; büyüme tamamlanınca bu bölge kemikleşir · Kemiğin kalınlaşması ise ayrı bir yapının işidir')],
  puf='Her yapının doku türünü (kemik, kıkırdak, ilik) ayır; hücre bölünmesi gerektiren olayı hangi dokunun yapabileceğini düşün.',sekil=SK3)

# ---------- 04 · kıkırdaktan kemiğe · orta · D ----------
S4=[('Kıkırdağın kemikleşmesinde hücreler arası maddede kalsiyum fosfat gibi mineral tuzlar birikir.',True,'kemikleşmede kıkırdak matriksine mineral tuzlar yerleşir ve doku sertleşir.'),
    ('Kemikleşen bölgelerde kan damarı içermeyen kıkırdağın yerini damarlı kemik doku alır.',True,'kemik doku damar ve sinir içerir, kıkırdak ise damarsızdır.'),
    ('Erişkinde de eklem yüzeylerinde ve kulak kepçesinde kıkırdak doku bulunmaya devam eder.',True,'kıkırdağın bir bölümü kemikleşmez; eklem yüzeyi ve kulak kepçesi gibi yerlerde kalır.'),
    ('Kemikleşme sırasında yeni kemik matriksini osteoblast hücreleri oluşturur.',True,'kemik matriksini yapan hücreler osteoblastlardır.'),
    ('Erişkin dönemde iskeletteki bütün kıkırdaklar kemikleşir ve vücutta kıkırdak doku kalmaz.',False,'')]
o4=tek_(S4,False,'D')
QO('0004','kemik','orta','düz','Kıkırdaktan kemiğe geçiş','Kıkırdak dokunun kemikleşmesi ve erişkinde kıkırdağın kalan yerleri hakkındaki ifadeleri değerlendirir.',
  'Kemikleşmede kıkırdağın yerini kemik doku alır; genelleme içeren ifadeler karşı örnekle sınanır.',
  'Genellemeleri sorgulamamak.','kıkırdağın kemikleşmesi',
  [A('Kemikleşmeyi tanımla','Bebekte çok olan kıkırdağın bir bölümü büyümeyle kemik dokuyla yer değiştirir.','Kıkırdak → kemik doku'),
   A('Doğru olan ifadeleri ayıkla','Mineral birikimi, damarlı kemik doku oluşumu ve osteoblastların matriks yapması doğrudur; eklem yüzeyindeki kıkırdak da kalır.','Dört ifade doğru'),
   A('Söylenemeyeni seç','Erişkinde bütün kıkırdakların kemikleştiği ifadesi, eklem yüzeyi ve kulak kepçesi örnekleriyle çelişir.','Cevap: “vücutta kıkırdak kalmaz” ifadesi')],
  o=o4,
  metin='Bir bebeğin iskeletinde kıkırdak doku miktarı, erişkininkine göre fazladır. Büyüme sürecinde kıkırdağın büyük bölümü kemik dokuyla yer değiştirir ve bu olaya kemikleşme denir.\nBuna göre, insanda kıkırdak ve kemik dokuyla ilgili aşağıdakilerden hangisi söylenemez?',
  istenen='Kemikleşme ve kıkırdak dokuyla ilgili söylenemeyecek ifade.',
  ip=['Tümünü kapsayan ifadelerde karşı örnek ara; her ifadeyi bu açıdan sına.'],
  bilgi=[B('Kemikleşme','kıkırdağın yerini zamanla kemik dokunun alması olayıdır; kemik doku hücreler arası maddesinde mineral tuzlar içerir')],
  puf='“Hepsi/hiçbiri” içeren ifadelerde karşı örnek bulmak yeter.')

# ---------- 05 · kemik yapısı deneyi · zor · E ----------
d5={'I':dd(False,'Asitte çözünen mineraller (kalsiyum fosfat tuzları) kemiğe sertlik kazandırır; esneklik organik maddeden gelir.'),
    'II':dd(True,'Isıtılınca organik maddeler yanıp uzaklaşır; geriye kalan mineral yapı sert ama kırılgan olur, esneklik organik maddeye aittir.'),
    'III':dd(True,'Yaşla organik madde oranı azalır; kemik M parçasındaki gibi esnekliğini yitirip daha kolay kırılır.')}
o5=onc(d5,True,'E'); assert o5['dogru']=='II ve III'
QO('0005','kemik','orta','öncüllü','Kemiğin bileşimi','Kemiğin organik ve inorganik bileşenlerinin özelliklerini deney sonuçlarıyla ilişkilendirir ve yaşa bağlı değişimi yorumlar.',
  'Kemikte organik ve inorganik bileşenler bulunur; yaşla bileşim oranları değişir.',
  'Asitte çözünen maddeyi esneklikten sorumlu sanmak; yaşlanmada organik madde oranının arttığını düşünmek.','kemik bileşimi deneyi',
  [A('Deney sonuçlarını yorumla','Asitle işlem gören L esnek, ısıyla işlem gören M kırılgan olmuştur; her işlem kemikten bir bileşeni uzaklaştırmıştır.','L: mineral çıkmış → esnek · M: organik çıkmış → kırılgan'),
   adim_onc(d5,'I'),adim_onc(d5,'II'),adim_onc(d5,'III'),
   A('Sonucu birleştir','II ve III yargıları sonuçlarla ve verilen bilgiyle uyumludur.','Cevap: II ve III')],
  o=o5,
  metin='Aynı kemikten alınan eş boyutlu üç parçadan K’ye işlem yapılmamış, L seyreltik asit çözeltisinde bekletilmiş, M ise yüksek sıcaklıkta kızdırılmıştır. K sert ve hafif esnek, L kolayca bükülebilen, M ise sert ama hafif bir darbeyle ufalanan yapıdadır. Yaşlanmayla kemikteki organik madde oranının azaldığı bilinmektedir.\nBuna göre,\nI. L parçasında asitte çözünen madde, kemiğin esnekliğini sağlar.\nII. M parçasında ısıyla uzaklaşan madde, kemiğin kırılmadan bükülebilmesini sağlar.\nIII. Yaşlı bireylerde kemiğin kırılmaya yatkın olması, M parçasının durumuyla uyumludur.\nyargılarından hangilerine ulaşılabilir?',
  istenen='Deney sonuçlarından ve verilen bilgiden çıkarılabilecek yargılar.',
  ip=['Her işlemin kemikten hangi tür maddeyi uzaklaştırdığını düşün; sonra uzaklaştırılan maddenin kaybı hangi özelliği değiştirmiş, buna bak.'],
  bilgi=[B('Kemik matriksinin bileşenleri','kemik doku hücreler arası maddesinde organik maddeler (ör. kolajen lifleri) ve inorganik mineraller (ör. kalsiyum tuzları) bulunur · Organik maddeler yüksek sıcaklıkta yanarak uzaklaşır, mineral tuzlar yanmaz fakat asitte çözünür')],
  puf='Deneyde her işlemle neyin değiştiğine bak, sonra değişen özelliği yorumla.')

# ---------- 06 · oynar eklem · orta · A ----------
M6={'kikirdak':'I','sivi':'II','kapsul':'III','bag':'IV','kemik':'V'}
SK6=eklem_sekil(M6)
S6=[('IV numaralı yapı, kasları kemiklere bağlayan tendondur.',False,''),
    ('I numaralı yapı, eklem yüzeylerindeki sürtünmeyi azaltır ve darbeleri sönümler.',True,'eklem kıkırdağı yüzeyi pürüzsüz tutar, sürtünmeyi azaltır ve darbeleri emer.'),
    ('II numaralı sıvı, eklem yüzeylerinin kayganlaşmasını sağlayarak aşınmayı azaltır.',True,'eklem sıvısı yağlayıcıdır ve yüzeyleri kayganlaştırır.'),
    ('III numaralı yapı, eklemi çevreleyerek eklem boşluğunu kapalı tutar.',True,'eklem kapsülü eklemi çevreler ve eklem sıvısını içeride tutar.'),
    ('V numaralı yapı kemik dokudan oluşur ve eklem yapan ucu kıkırdakla örtülüdür.',True,'kemiğin eklem yapan ucu kemik dokudur ve eklem kıkırdağıyla kaplıdır.')]
o6=tek_(S6,False,'A')
QO('0006','eklem','orta','şekilli','Oynar eklem yapısı','Oynar eklemin yapı elemanlarını tanır ve görevlerini ayırt eder.',
  'Oynar eklemin elemanları ve görevleri.',
  'Yapıların görevlerini karıştırmak.','oynar eklemin yapısı',
  [A('Yapıları adlandır','Kemik uçlarını kaplayan kıkırdak, aradaki sıvılı boşluk, eklemi saran kapsül ve kemikleri bağlayan şerit görülür.','I: eklem kıkırdağı · II: eklem sıvısı · III: eklem kapsülü · IV: bağ · V: kemik'),
   A('İfadeleri sına','Kıkırdak, sıvı, kapsül ve kemik ucuyla ilgili ifadeler görevlerine uygundur.','Dört ifade doğru'),
   A('Yanlışı belirle','Kemiği kemiğe bağlayan yapı bağdır; kasları kemiğe bağlayan yapı ise tendondur.','Bağ ≠ tendon')],
  o=o6,
  metin='Şekilde bir oynar eklemin boyuna kesiti verilmiştir; eklemi oluşturan bazı yapılar I, II, III, IV ve V ile numaralandırılmıştır. Bu eklem bükülme ve açılma hareketi yaparken yapılar birlikte çalışarak eklemin zarar görmesini önler.\nBuna göre, numaralandırılmış yapılarla ilgili aşağıdakilerden hangisi yanlıştır?',
  istenen='Numaralı yapılarla ilgili yanlış ifade.',
  ip=['Şekildeki her yapıyı adlandır; ardından hangi yapının kemiği kemiğe, hangisinin kası kemiğe bağladığını ayırt et.'],
  bilgi=[B('Oynar eklemin elemanları','eklem kapsülü, eklem sıvısı, eklem kıkırdağı ve bağlar oynar eklemde bulunur · Bağlar kemikleri birbirine, tendonlar kasları kemiklere bağlar')],
  puf='Her yapının adını ve görevini ayrı ayrı eşleştir.',sekil=SK6)

# ---------- 07 · eklem türleri tablosu · orta · B ----------
SK7=tablo_r(['Eklem','Kemikler arasında','Eklem boşluğu','Hareket'],[['K','Sıkı lifli bağ doku','Yok','Yok'],['L','Kıkırdak disk','Yok','Çok sınırlı'],['M','Kapsül ve eklem kıkırdağı','Var','Tek düzlemde'],['N','Kapsül ve eklem kıkırdağı','Var','Her yönde']])
d7={'I':dd(True,'Kafatası kemikleri sıkı lifli bağ dokuyla kenetlenir; boşluk ve hareket yoktur, bu K’nin özelliğidir.'),
    'II':dd(True,'Omurlar arasında kıkırdak diskler bulunur; boşluk yoktur ve hareket sınırlıdır, bu L’nin özelliğidir.'),
    'III':dd(False,'Omuz eklemi her yönde hareket eder; bu özellik N’de görülür, M ise tek düzlemde hareket eden eklemlere uyar.')}
o7=onc(d7,True,'B'); assert o7['dogru']=='I ve II'
QO('0007','eklem','orta','tablo','Eklem türleri','Eklem türlerini yapı ve hareket özelliklerine göre sınıflandırır ve örneklerle eşleştirir.',
  'Eklemler kemik birleşimine, eklem boşluğuna ve hareket yeteneğine göre sınıflandırılır.',
  'Örnek eklemlerin hareket yeteneğini karıştırmak.','eklem türlerini örneklerle eşleştirme',
  [A('Tablodan türleri çıkar','K: boşluksuz ve hareketsiz, L: boşluksuz ve sınırlı hareketli, M: boşluklu ve tek düzlemli, N: boşluklu ve çok yönlü eklemdir.','K: oynamaz · L: yarı oynar · M, N: oynar'),
   adim_onc(d7,'I'),adim_onc(d7,'II'),adim_onc(d7,'III'),
   A('Sonucu birleştir','I ve II doğru, III yanlıştır.','Cevap: I ve II')],
  o=o7,
  metin='Aşağıdaki tabloda insan iskeletindeki dört farklı eklem türünün bazı özellikleri K, L, M ve N harfleriyle verilmiştir.\nI. K, kafatası kemikleri arasındaki eklemlere örnektir.\nII. L, omurlar arasındaki eklemlere örnektir.\nIII. M, omuz eklemine örnektir.\nBuna göre, bu ifadelerden hangileri doğrudur?',
  istenen='Tablodaki eklem türleri için doğru örnek eşleştirmeleri.',
  ip=['Tablodan her harfin boşluk ve hareket özelliğini oku; her örneğin hareket yeteneğini hatırlayıp eşleştir.'],
  bilgi=[B('Eklem türleri','eklemler hareket yeteneğine göre oynamaz, yarı oynar ve oynar eklem olarak sınıflandırılır; sınıflama kemiklerin birleştiği dokuya ve eklem boşluğunun varlığına dayanır')],
  puf='Boşluk yoksa oynamaz ya da yarı oynar; boşluk varsa oynar eklemdir, hareket yönü eklem türüne göre değişir.',sekil=SK7)

# ---------- 08 · oynamaz eklem · kolay · C ----------
S8=[('Omuz eklemi',False,'omuz eklemi oynar eklemdir; eklem boşluğu ve eklem sıvısı bulunur, her yönde hareket eder.'),
    ('Omurlar arasındaki eklem',False,'omurlar arasındaki eklem kıkırdak diskle birleşir ve yarı oynardır; sınırlı da olsa hareket eder.'),
    ('Kafatası kemikleri arasındaki dikiş',True,''),
    ('Dirsek eklemi',False,'dirsek eklemi oynar eklemdir; tek düzlemde bükülüp açılır.'),
    ('Kalça eklemi',False,'kalça eklemi oynar eklemdir; her yönde geniş hareket sağlar.')]
o8=tek_(S8,True,'C')
QO('0008','eklem','kolay','düz','Eklemlerin sınıflandırılması','Eklemleri hareket yeteneğine göre sınıflandırarak oynamaz eklemi belirler.',
  'Eklemler hareket yeteneğine göre oynamaz, yarı oynar ve oynar olarak sınıflandırılır.',
  'Omurlar arasındaki ekleme hareket yeteneği olduğu için oynar demek.','oynamaz eklem örneği',
  [A('Sınıfları hatırla','Eklemler hareket yeteneğine göre oynamaz, yarı oynar ve oynar olarak üçe ayrılır.','Oynamaz: boşluk yok, hareket yok'),
   A('Örnekleri sınıflandır','Omuz, dirsek ve kalça oynar eklemdir; omurlar arası eklem yarı oynar eklemdir.','Omuz, dirsek, kalça: oynar · Omurlar arası: yarı oynar'),
   A('Oynamaz olanı seç','Kafatası kemikleri dikişle kenetlenir ve hiç hareket etmez.','Cevap: kafatası kemikleri arasındaki dikiş')],
  o=o8,
  metin='İnsan iskeletinde kemikler arasındaki eklemler, hareket yeteneğine göre oynar, yarı oynar ve oynamaz eklem olarak sınıflandırılır. Oynar eklemlerde eklem boşluğu ve eklem sıvısı bulunurken oynamaz eklemlerde kemikler sıkı bağ dokuyla birbirine kenetlenir.\nBuna göre, aşağıdakilerden hangisi oynamaz eklemdir?',
  istenen='Oynamaz eklem örneği.',
  ip=['Eklem sınıflarının hareket yeteneğini hatırla ve örnekleri bu sınıflara yerleştir.'],
  bilgi=[B('Eklem sınıfları','oynar eklemde eklem boşluğu ve sıvısı vardır; yarı oynar eklemde kıkırdak diskle birleşme ve sınırlı hareket görülür; oynamaz eklemde kemikler hareketsiz birleşir')],
  puf='Önce sınıfları, sonra örneklerin hangi sınıfa girdiğini düşün.')

# ---------- 09 · kas hücreleri · kolay · D ----------
SK9=kashucre_sekil({'duz':'K','iskelet':'L','kalp':'M'})
S9=[('K hücrelerinden oluşan kas, sindirim kanalı ve kan damarlarının duvarında bulunur ve istemsiz çalışır.',True,''),
    ('L hücrelerinden oluşan kas dokusu yalnızca kalpte bulunur.',False,'L çok çekirdekli ve çizgili hücrelerden oluşan iskelet kasıdır; kalp kası M’dir.'),
    ('M hücrelerinden oluşan kas, kemiklere tendonlarla bağlanarak istemli hareketi sağlar.',False,'M kalp kasıdır; istemsiz çalışır ve kemiklere bağlanmaz.'),
    ('K ve L hücrelerinde enine çizgilenme görülür.',False,'K düz kas hücresidir ve çizgilenme göstermez; yalnız L ve M çizgilidir.'),
    ('L ve M hücrelerinin çekirdekleri hücrenin merkezinde yer alır.',False,'L’de çekirdekler hücre çevresindedir; merkezde olması düz ve kalp kası hücreleri için geçerlidir.')]
o9=tek_(S9,True,'E')
QO('0009','kas','kolay','şekilli','Kas hücrelerinin tanınması','Düz, çizgili ve kalp kası hücrelerini şekilden ayırt eder ve işlevlerini ilişkilendirir.',
  'Düz kas iğ biçimli, çizgisiz, tek merkezî çekirdeklidir; iskelet kası çok çekirdekli ve çizgilidir; kalp kası dallanmış, çizgili ve ara disklidir.',
  'Çizgili görünen her kası istemli sanmak.','kas hücrelerini şekilden tanıma',
  [A('Hücreleri tanı','K iğ biçimli ve çizgisiz, L uzun ve çok çekirdekli çizgili, M dallanmış ve ara diskli çizgili hücredir.','K: düz kas · L: iskelet kası · M: kalp kası'),
   A('İfadeleri sına','Düz kas sindirim kanalı ve damar duvarında bulunur ve istemsiz çalışır; iskelet kası çizgilidir ve çok çekirdeklidir; kalp kası istemsizdir.','Düz kas: istemsiz, çizgisiz'),
   A('Doğru ifadeyi bul','Sindirim kanalı ve damarlarla ilgili ifade düz kasa uygundur.','Cevap: düz kasla ilgili ifade')],
  o=o9,
  metin='Şekilde insan vücudunda bulunan üç farklı kas hücresi K, L ve M ile gösterilmiştir. Hücrelerin biçimleri, çekirdek sayıları, çekirdeklerin konumu ve çizgilenme durumları şekildeki gibidir.\nBuna göre, bu hücrelerle ilgili aşağıdakilerden hangisi doğrudur?',
  istenen='Şekildeki hücrelerle ilgili doğru ifade.',
  ip=['Önce her hücrenin çizgilenmesine, çekirdek sayısına ve biçimine bakarak kas türünü belirle; sonra her türün çalışma biçimini hatırla.'],
  bilgi=[B('Kas türleri','insanda üç tür kas dokusu vardır: iskelet (çizgili), düz ve kalp kası · Türler hücre biçimi, çekirdek sayısı ve konumu, çizgilenme ve çalışma biçimi bakımından birbirinden ayrılır')],
  puf='Çizgilenme yok → düz kas; çok çekirdek çevrede → iskelet kası; dallanma ve ara disk → kalp kası.',sekil=SK9)

# ---------- 10 · kas özellikleri tablosu · orta · E ----------
SK10=tablo_r(['Kas','Kasılma hızı','Yorulma','Çalışma biçimi'],[['K','Hızlı','Çabuk yorulur','İstemli'],['L','Yavaş','Geç yorulur','İstemsiz'],['M','Orta hızlı','Yorulmaz','İstemsiz, kendi ritmiyle']])
d10={'I':dd(True,'K hızlı ve istemli çalışan iskelet kasıdır; iskelet kası liflerinde düzenli sarkomerler bulunur.'),
     'II':dd(False,'Bütün kas türlerinde kasılma ATP gerektirir; düz kas da ATP harcayarak kasılır.'),
     'III':dd(True,'M, kalp kasıdır; kendi ritmik uyartılarını oluşturabildiği için sinir uyarısı gelmese de kasılır.')}
o10=onc(d10,True,'E'); assert o10['dogru']=='I ve III'
QO('0010','kas','orta','tablo','Kas türlerinin özellikleri','Kas türlerini çalışma özelliklerinden tanıyıp yapı ve enerji bilgisiyle yargıları değerlendirir.',
  'Hızlı–istemli kas iskelet kasıdır; geç yorulan istemsiz kas düzdür; kendi ritmiyle çalışan, yorulmayan kas kalp kasıdır; tüm kasılmalar ATP ister.',
  'Düz kasın ATP kullanmadan kasıldığını sanmak.','kas türü tablosu',
  [A('Tablodan türleri çıkar','İstemli ve hızlı çalışan K iskelet kasıdır; yavaş ve istemsiz çalışan L düz kastır; kendi ritmiyle çalışan M kalp kasıdır.','K: iskelet · L: düz · M: kalp'),
   adim_onc(d10,'I'),adim_onc(d10,'II'),adim_onc(d10,'III'),
   A('Sonucu birleştir','I ve III doğrudur.','Cevap: I ve III')],
  o=o10,
  metin='Aşağıdaki tabloda insan vücudundaki üç farklı kas dokusunun bazı özellikleri K, L ve M ile gösterilmiştir.\nI. K kasının hücrelerinde, kasılma birimi olan sarkomerler bulunur.\nII. L kasının kasılması ATP kullanılmadan gerçekleşir.\nIII. M kası, sinirsel uyarı gelmese de kendi ritmik uyartılarıyla kasılabilir.\nBuna göre, bu ifadelerden hangileri doğrudur?',
  istenen='Tablodaki kaslarla ilgili doğru ifadeler.',
  ip=['Tablodaki özelliklerden her kasın hangi tür olduğunu çıkar; sonra türlerin ortak ve ayırt edici özelliklerini sırala.'],
  bilgi=[B('Kas türlerinin çalışması','istemli kaslar sinir sisteminin isteğe bağlı bölümünce, istemsiz kaslar otonom sinir sistemince denetlenir · Kalp kası uyartıyı hücre içinden de başlatabilir')],
  puf='Hızlı + istemli = iskelet; yavaş + istemsiz = düz; kendi ritmi + yorulmaz = kalp; hepsi ATP ile kasılır.',sekil=SK10)

# ---------- 11 · koşan sporcu · orta · A ----------
d11={'I':dd(True,'Bacak kasları iskelet kasıdır ve kas lifleri çok çekirdeklidir.'),
     'II':dd(False,'Sindirim kanalındaki düz kas istemsiz çalışır; sporcunun isteğiyle durdurulamaz.'),
     'III':dd(False,'Kalp kası çizgilidir; aktin ve miyozin iplikçikleri düzenli dizildiğinden enine çizgilenme görülür.')}
o11=onc(d11,True,'A'); assert o11['dogru']=='Yalnız I'
QO('0011','kas','orta','öncüllü','Kas türlerinin karşılaştırılması','Aynı anda çalışan farklı kas türlerinin hücre yapısı ve denetimi hakkında yargıları değerlendirir.',
  'İskelet kası çok çekirdeklidir; düz kas istemsizdir; kalp kası çizgilidir.',
  'Çizgilenmeyi yalnız iskelet kasına özgü sanmak; düz kası istemli denetlenebilir saymak.','koşan sporcuda üç kas türü',
  [adim_onc(d11,'I'),adim_onc(d11,'II'),adim_onc(d11,'III'),A('Sonucu birleştir','Yalnız I yargısı doğrudur.','Cevap: Yalnız I')],
  o=o11,
  metin='Bir sporcu koşarken bacak kasları, sindirim kanalının duvarındaki kaslar ve kalp kası aynı anda çalışmaktadır. Bu kas dokularıyla ilgili,\nI. Bacak kası hücreleri çok çekirdeklidir.\nII. Sindirim kanalındaki kasların çalışması, sporcunun isteğiyle durdurulabilir.\nIII. Kalp kası hücrelerinde enine çizgilenme görülmez.\nyargılarından hangileri doğrudur?',
  istenen='Doğru olan yargılar.',
  ip=['Üç kas türünün çekirdek sayısını, çizgilenmesini ve denetim biçimini ayrı ayrı hatırla; yargıları bu bilgilerle karşılaştır.'],
  bilgi=[B('Kasların denetimi','istemli kaslar isteğe bağlı olarak çalıştırılıp durdurulabilir; istemsiz kaslar isteğimizden bağımsız çalışır')],
  puf='Çizgilenme yalnız iskelet kasında değil, kalp kasında da vardır; düz kas çizgisiz ve istemsizdir.')

# ---------- 12 · kasta enerji ve yorgunluk · orta · B ----------
S12=[('Kas hücresindeki çok sayıdaki mitokondri, kasılma sürerken oksijenli solunumla ATP yapımının sürdürülmesini sağlar.',True,'kas hücrelerinde çok sayıda mitokondri bulunur ve oksijen yeterliyse oksijenli solunumla ATP üretilir.'),
     ('Kas yorgunluğunda kasların ATP’ye gereksinimi kalmadığı için kasılma gücü azalır.',False,''),
     ('Şiddetli egzersizde oksijen yetersiz kaldığında kaslarda oksijensiz yıkımla ATP üretilir ve laktik asit birikebilir.',True,'oksijensiz glikoz yıkımı ATP sağlar ve yan ürün olarak laktik asit oluşur.'),
     ('Miyoglobin, kas hücrelerinde oksijen depolayarak oksijenli solunumu destekler.',True,'miyoglobin kasta oksijen depolayan bir proteindir.'),
     ('Kaslarda depolanan glikojenin yıkımı, ATP üretiminde kullanılan glikozu sağlar.',True,'glikojen kasta depolanan karbonhidratdır ve yıkılarak glikoz verir.')]
o12=tek_(S12,False,'B')
QO('0012','enerji','orta','düz','Kas yorgunluğu ve enerji','Kasta ATP sağlama yollarını ve kas yorgunluğunun nedenlerini ilişkilendirir.',
  'Kasta ATP sağlama yolları ve oksijen durumu ile kas yorgunluğu arasındaki ilişki.',
  'Yorgun kasta ATP gereksiniminin bittiğini sanmak.','kasta enerji sağlama yolları',
  [A('Enerji yollarını hatırla','Kasta ATP, oksijenli solunum, oksijensiz yıkım ve depo maddelerle sağlanır.','Mitokondri, miyoglobin, glikojen, laktik asit'),
   A('İfadeleri sına','Mitokondri, oksijensiz yıkım, miyoglobin ve glikojen ifadeleri kasın enerji kaynaklarıyla uyumludur.','Dört ifade doğru'),
   A('Söylenemeyeni seç','Yorgun kas da kasılmak için ATP’ye gereksinim duyar; gücün azalması ATP gereksiniminin bitmesinden değil, yeterince sağlanamamasından kaynaklanır.','Cevap: “ATP gereksinimi kalmadı” ifadesi')],
  o=o12,
  metin='Kısa sürede çok şiddetli egzersiz yapan bir sporcunun iskelet kaslarında enerji sağlama yolları incelenmektedir. Kaslar oksijen gereksinimlerinin tamamını karşılayamadığında ATP sağlamak için birden fazla yol devreye girmektedir.\nBuna göre, kasta enerji sağlanmasıyla ilgili aşağıdakilerden hangisi söylenemez?',
  istenen='Söylenemeyecek ifade.',
  ip=['Kasılmanın her aşamasında ATP’nin rolünü düşün; her ifadeyi bu bilgiyle ve oksijen durumuyla sına.'],
  bilgi=[B('Kasta ATP kaynakları','kas hücresi ATP’yi oksijenli solunumla, oksijensiz yıkımla ve depo maddelerle sağlar')],
  puf='Kasılma ve gevşeme için her zaman ATP gerekir; ifadelerde “gereksinim kalmadı” gibi mutlak çıkarımları sorgula.')

# ---------- 13 · sarkomer ölçüleri · orta · C ----------
SK13=sark_sekil13()
L0=Fr(3); H0=L0-2*THIN; assert H0==1
d13={'I':dd(True,'Kasılmada ince iplikçikler kalın iplikçikler üzerinde kayarak Z çizgilerini birbirine yaklaştırır; Z çizgileri arası uzaklık kısalır.'),
     'II':dd(False,'Kalın iplikçiğin boyu (A bandı) kasılmada değişmez; iplikçikler kısalmaz, yalnız birbiri üzerinde kayar.'),
     'III':dd(True,'İnce iplikçiklerin uçları birbirine yaklaştıkça yalnız kalın iplikçik içeren orta bölge (H bölgesi) daralır.')}
o13=onc(d13,True,'C'); assert o13['dogru']=='I ve III'
QO('0013','sark','orta','öncüllü','Sarkomerin yapısı','Kasılma sırasında sarkomerin hangi bölümlerinin boyunun değiştiğini belirler.',
  'Kasılmada sarkomer bölümlerinin boy değişimi iplikçiklerin kaymasıyla açıklanır.',
  'Kalın iplikçik boyunun (A bandı) kısaldığını sanmak.','sarkomer bölümlerinin boyu',
  [A('Bölümleri adlandır','I numaralı uzunluk iki Z çizgisi arasıdır, II kalın iplikçiğin boyudur, III yalnız kalın iplikçik içeren orta bölgedir.','I: Z–Z (sarkomer) · II: A bandı · III: H bölgesi'),
   adim_onc(d13,'I'),adim_onc(d13,'II'),adim_onc(d13,'III'),
   A('Sonucu birleştir','I ve III yargıları doğrudur.','Cevap: I ve III')],
  o=o13,
  metin='Şekilde gevşemiş bir iskelet kası sarkomeri ve sarkomerin bazı bölümlerinin uzunluğunu gösteren I, II ve III numaralı çizgiler verilmiştir. Bu kas lifi uyarıldığında sarkomer kasılmaktadır.\nKasılma sırasında,\nI. I numaralı uzunluk kısalır.\nII. II numaralı uzunluk kısalır.\nIII. III numaralı uzunluk kısalır.\nyargılarından hangileri doğrudur?',
  istenen='Kasılmada kısalan uzunluklar.',
  ip=['Kasılmada hangi yapıların boyunun sabit kaldığını, hangilerinin birbiri üzerinde kaydığını düşünüp her çizginin hangi iki yapı arasını ölçtüğüne bak.'],
  bilgi=[B('Sarkomerin bölümleri','sarkomer iki Z çizgisi arasıdır · İnce iplikçikler Z çizgilerine, kalın iplikçikler sarkomerin ortasına bağlıdır · Yalnız ince iplikçik içeren bölge I bandı, kalın iplikçik içeren bölge A bandı, yalnız kalın iplikçik içeren orta bölge H bölgesidir')],
  puf='İplikçiklerin kısalıp kısalmadığını ya da kaydığını kendine sor; her çizginin hangi yapılar arasını ölçtüğüne bak.',sekil=SK13)

# ---------- 14 · iki sarkomer ölçüsü · orta · D ----------
SK14=sark_sekil14()
X14,Y14=Fr(14,5),Fr(11,5)
Ib=lambda Z:Z-THICK; Hb=lambda Z:Z-2*THIN
assert Ib(X14)==Fr(6,5) and Hb(X14)==Fr(4,5) and Ib(Y14)==Fr(3,5) and Hb(Y14)==Fr(1,5)
dI=Ib(X14)-Ib(Y14); dH=Hb(X14)-Hb(Y14); tot=dI+dH; assert tot==Fr(6,5) and dI==dH==Fr(3,5)
Q('0014','sark','orta','şekilli','Sarkomerin yapısı','Gevşek ve kasılı sarkomer ölçülerinden bant uzunluklarındaki toplam değişimi hesaplar.',
  'Sarkomer bölümlerinin uzunlukları iplikçik boylarından ve Z–Z uzaklığından hesaplanır.',
  'Yalnız tek bölgenin değişimini hesaplamak ya da A bandını değişen saymak.','sarkomer bölüm uzunlukları',
  [A('Bölümleri hesapla','I bandı, Z–Z’den kalın iplikçik boyunun; H bölgesi, Z–Z’den iki ince iplikçik boyunun çıkarılmasıyla bulunur.','X: I = 2,8 − 1,6 = 1,2 · H = 2,8 − 2,0 = 0,8'),
   A('Y için hesapla','Aynı bağıntılar Z–Z = 2,2 µm için uygulanır.','Y: I = 2,2 − 1,6 = 0,6 · H = 2,2 − 2,0 = 0,2'),
   A('Azalmaları topla','I bandı 0,6 µm, H bölgesi 0,6 µm azalmıştır; toplam azalma istenir.','0,6 + 0,6 = 1,2 µm')],
  dogru=Fr(6,5),yan=[(Fr(1,5),'Y’deki H bölgesi (0,2 µm) toplam azalma sanılmış; oysa azalma X ile Y arasındaki farktır.','dikkat'),
                (Fr(3,5),'Yalnız tek bölgenin azalması (0,6 µm) alınmış; I bandı ve H bölgesinin ikisi de azalmıştır.','dikkat'),
                (Fr(4,5),'X’teki H bölgesi (0,8 µm) azalma sanılmış; oysa H bölgesi tamamen yok olmamış, 0,2 µm kalmıştır.','bilgi'),
                (Fr(8,5),'Kalın iplikçik boyu (1,6 µm) değişim sanılmış; oysa A bandı kasılmada değişmez.','bilgi')],
  metin='Şekilde bir iskelet kası lifindeki aynı sarkomerin iki farklı andaki hâli X ve Y ile, Z çizgileri arasındaki uzaklıklarla birlikte gösterilmiştir. İnce iplikçiklerin her biri 1,0 µm, kalın iplikçikler 1,6 µm uzunluğundadır ve bu uzunluklar değişmemektedir. I bandı yalnız ince iplikçik bulunan bölgelerin toplam uzunluğu, H bölgesi yalnız kalın iplikçik bulunan orta bölgenin uzunluğudur.\nBuna göre, sarkomer X’ten Y’ye geçerken I bandı ile H bölgesinin uzunlukları toplamı kaç µm azalmıştır?',
  istenen='I bandı ve H bölgesindeki toplam azalma (µm).',
  ip=['Her sarkomer için önce iplikçik boylarından I bandı ve H bölgesinin uzunluklarını yaz; sonra iki durumu karşılaştır.'],
  bilgi=[B('Sarkomer bölümleri','sarkomerin boyu iki Z çizgisi arasındaki uzaklıktır; ince iplikçikler Z çizgilerine, kalın iplikçikler ortaya bağlıdır')],
  puf='Önce iplikçik boylarından bölge uzunluklarını yaz, sonra iki durumu karşılaştır.',sekil=SK14)

# ---------- 15 · miyofibril boyu · zor · D ----------
SK15=sark_sekil15()
t_,thick_,Z0=THIN,THICK,Fr(13,5); Hc=Fr(1,5); N=10000
Zc=2*t_+Hc; assert Zc==Fr(11,5) and Z0-Zc==Fr(2,5)
mm=lambda um: um*N/1000
assert mm(Zc)==22 and mm(Z0-Zc)==4 and mm(t_+Hc)==12 and mm(2*t_)==20 and mm(Z0)==26
Q('0015','sark','zor','şekilli','Sarkomer ve kas boyu','Sarkomer ölçülerinden kasılmış miyofibrilin boyunu hesaplar.',
  'Kasılmada iplikçik boyu sabittir; Z–Z uzaklığı iki ince iplikçik ile H bölgesinin toplamıdır; miyofibril boyu sarkomer sayısı ile çarpılarak bulunur.',
  'Kasılmış sarkomeri bulurken H bölgesini ya da ince iplikçiklerden birini unutmak; kısalma miktarı ile son boyu karıştırmak.','miyofibril boyu hesabı',
  [A('İplikçik boylarını oku','Şekilden ince iplikçik 1,0 µm ve kalın iplikçik 1,6 µm; iplikçik boyları kasılmada değişmez.','İnce: 1,0 µm · Z–Z (gevşek): 2,6 µm'),
   A('Kasılmış sarkomeri bul','Kasılmış sarkomerde Z–Z uzaklığı iki ince iplikçik ile H bölgesinin toplamıdır.','Z–Z = 2 × 1,0 + 0,2 = 2,2 µm'),
   A('Seri bağlı sarkomerleri topla','Miyofibril boyu, sarkomer sayısı ile bir sarkomerin boyunun çarpımıdır.','10 000 × 2,2 = 22 000 µm'),
   A('Birimi çevir','1000 µm = 1 mm olduğundan 22 000 µm = 22 mm eder.','Cevap: 22 mm')],
  dogru=22,yan=[(4,'Bu değer miyofibrilin kısalma miktarıdır: (2,6 − 2,2) × 10 000 µm = 4 mm. Soru kasılmış miyofibrilin son boyunu sorar.','dikkat'),
                (12,'Kasılmış sarkomerde yalnız bir ince iplikçik sayılmış: (1,0 + 0,2) × 10 000 µm = 12 mm. Oysa Z çizgisinin iki yanında da ince iplikçik vardır.','bilgi'),
                (20,'H bölgesi unutulmuş: 2 × 1,0 × 10 000 µm = 20 mm. Ancak ince iplikçik uçları arasında 0,2 µm’lik H bölgesi kalmıştır.','bilgi'),
                (26,'Gevşek sarkomer boyu kullanılmış: 2,6 × 10 000 µm = 26 mm. Kasılma sonrası Z–Z uzaklığı azalmıştır.','dikkat')],
  metin='Şekilde, bir iskelet kası miyofibrilinde gevşek hâldeki bir sarkomerin ölçüleri verilmiştir. Miyofibrilde bu sarkomerlerden 10 000 tanesi uç uca bağlıdır. Kasılma sırasında iplikçiklerin boyları değişmemiş ve yalnız kalın iplikçik bulunan orta bölge (H bölgesi) 0,2 µm olmuştur. 1 mm = 1000 µm’dir.\nBuna göre, kasılmış miyofibrilin boyu kaç mm’dir?',
  istenen='Kasılmış miyofibrilin boyu (mm).',
  ip=['Kasılmış sarkomerin iki Z çizgisi arasında kaç ince iplikçik ve hangi boşluk bulunduğunu yazarak başla.'],
  bilgi=[B('Sarkomerin sıralanması','bir miyofibril, uç uca eklenmiş çok sayıda sarkomerden oluşur; miyofibrilin boyu sarkomerlerin boylarının toplamıdır')],
  puf='Kasılan sarkomerde Z–Z = iki ince iplikçik + H bölgesi; miyofibril boyu için sarkomer sayısıyla çarp, birimi en sonda çevir.',sekil=SK15)

# ---------- 16 · tutarsız ölçüm satırı · zor · A ----------
Tt=Fr(1); A0=Fr(8,5)
sat=[('K',Fr(13,5),Fr(7,5),Fr(6,5),Fr(3,5)),('L',Fr(16,5),Fr(8,5),Fr(8,5),Fr(6,5)),('M',Fr(14,5),Fr(8,5),Fr(6,5),Fr(4,5)),('N',Fr(12,5),Fr(8,5),Fr(4,5),Fr(2,5)),('O',Fr(2),Fr(8,5),Fr(2,5),Fr(0))]
def tutarli(r): n,Z,Aa,I,Hh=r; return Z==Aa+I and Hh==Z-2*Tt and Aa==A0
res={r[0]:tutarli(r) for r in sat}; assert res=={'K':False,'L':True,'M':True,'N':True,'O':True}
fmt=lambda x: f'{float(x):.1f}'.replace('.',',')
SK16=tablo_r(['Satır','Z–Z (µm)','A bandı (µm)','I bandı (µm)','H bölgesi (µm)'],[[r[0]]+[fmt(v) for v in r[1:]] for r in sat])
def ced16(r):
    n,Z,Aa,I,Hh=r
    return (n,f'{n} satırı tutarsız sanılmış; oysa {fmt(Z)} = {fmt(Aa)} + {fmt(I)} ve {fmt(Z)} − 2,0 = {fmt(Hh)} olup A bandı sabit 1,6 µm olduğundan satır tutarlıdır.','dikkat')
for r in sat[1:]: assert r[1]==r[2]+r[3] and r[4]==r[1]-2 and r[2]==Fr(8,5)
Q('0016','sark','zor','tablo','Sarkomer bölümlerinin ilişkisi','Sarkomer bölümleri arasındaki bağıntıları (A bandı sabit, Z–Z = A + I, H = Z–Z − 2 ince iplikçik) kullanarak tutarsız ölçümü bulur.',
  'A bandı kalın iplikçik boyuna eşit ve sabittir; Z–Z uzaklığı A ve I bandının toplamıdır; H bölgesi Z–Z’den iki ince iplikçik çıkarılarak bulunur.',
  'A bandının kasılmayla değiştiğini sanıp tutarsız satırı H ya da I sütununda aramak.','sarkomer ölçüm tablosu',
  [A('Bağıntıları yaz','Z–Z, A bandı ile I bandının toplamıdır; H bölgesi Z–Z’den iki ince iplikçik (2,0 µm) çıkarılarak bulunur.','Z–Z = A + I (toplam) · H = Z–Z − 2,0'),
   A('Sabit değeri bul','A bandı kalın iplikçik boyuna eşittir ve kasılmada değişmez.','A bandı = 1,6 µm'),
   A('Satırları sına','K satırı kendi içinde tutarlı olsa da A bandı 1,4 µm çıkmaktadır; diğer satırlar tüm bağıntıları sağlar.','K: A ≠ 1,6 · L, M, N, O: tutarlı'),
   A('Satırı seç','Tutarsız ölçüm K satırındadır.','Cevap: K')],
  dogru='K',sira=['K','L','M','N','O'],yan=[ced16(r) for r in sat[1:]],
  metin='Bir iskelet kası lifinde farklı anlarda ölçülen sarkomer bölümlerinin uzunlukları tabloda verilmiştir. İnce iplikçiklerin her biri 1,0 µm, kalın iplikçiklerin her biri 1,6 µm uzunluğundadır. I bandı, yalnız ince iplikçik bulunan bölgelerin toplam uzunluğu; H bölgesi ise yalnız kalın iplikçik bulunan orta bölgenin uzunluğudur. Aynı kas lifinin sarkomerlerinde iplikçik boyları sabittir.\nBuna göre, hangi satırdaki ölçümler aynı kas lifinin sarkomerlerine ait olamaz?',
  istenen='Aynı kas lifine ait olamayacak satır.',
  ip=['Sarkomer bölümleri arasındaki toplam ve fark bağıntılarını yaz; kasılmada hangi bölümün sabit kaldığını bil ve satırları buna göre karşılaştır.'],
  bilgi=[B('Sarkomer bölümleri','Z çizgileri arası uzaklık sarkomerin boyudur; kalın iplikçik boyu A bandına eşittir · Sarkomerin A bandı dışında kalan kısmı I bandıdır')],
  puf='Önce satırlar arasındaki bağıntıları yaz, sonra her satırı tek tek sına.',sekil=SK16)

# ---------- 17 · motor nöron – kas lifi · orta · E ----------
M17={'noron':'I','sr':'II','mito':'III','miyofibril':'IV','zar':'V'}
SK17=kavsak_sekil(M17)
d17={'I':dd(True,'Motor nöronun akson ucundan salgılanan asetilkolin, kas lifi zarında (V) uyarı oluşumunu başlatır.'),
     'II':dd(False,'Sarkoplazmik retikulum Ca²⁺ iyonlarını kas lifinin sitoplazmasına bırakır; hücre dışına salmaz.'),
     'III':dd(True,'Mitokondriler, kasılma için gereken ATP’nin önemli bölümünü sentezler.')}
o17=onc(d17,True,'E'); assert o17['dogru']=='I ve III'
QO('0017','kasilma','orta','öncüllü','Sinirsel uyarı ve kasılma','Motor nörondan kas lifine uyarı iletimini ve kas lifindeki yapıların görevlerini ilişkilendirir.',
  'Motor nöron asetilkolin salgılar, kas lifi zarında uyarı oluşur, sarkoplazmik retikulum Ca²⁺ iyonlarını sitoplazmaya bırakır; mitokondri ATP sentezler.',
  'Ca²⁺ iyonlarının hücre dışına salındığını sanmak.','motor nöron ve kas lifi şeması',
  [A('Yapıları tanı','I motor nöron ucu, II sarkoplazmik retikulum, III mitokondri, IV miyofibril ve V kas lifi zarıdır.','I: motor nöron ucu · II: sarkoplazmik retikulum · III: mitokondri · IV: miyofibril · V: kas lifi zarı'),
   adim_onc(d17,'I'),adim_onc(d17,'II'),adim_onc(d17,'III'),
   A('Sonucu birleştir','I ve III doğrudur.','Cevap: I ve III')],
  o=o17,
  metin='Şekilde bir iskelet kası lifi ve ona uyarı ileten bir motor nöronun ucu gösterilmiş; bazı yapılar I, II, III, IV ve V ile numaralandırılmıştır. Motor nöron uyarıldığında kas lifi kasılmaktadır.\nBuna göre,\nI. I numaralı yapıdan salgılanan kimyasal madde, V numaralı yapıda uyarı oluşturur.\nII. II numaralı yapı, uyarı sonrasında Ca²⁺ iyonlarını kas lifinin dışına bırakır.\nIII. III numaralı yapıda, kasılmada kullanılan ATP’nin bir bölümü sentezlenir.\nifadelerinden hangileri doğrudur?',
  istenen='Şekildeki yapılarla ilgili doğru ifadeler.',
  ip=['Uyarının motor nörondan kas lifi içindeki iplikçiklere kadar izlediği yolu sırayla düşün; her yapıyı bu zincirdeki görevine göre eşleştir.'],
  bilgi=[B('Kas lifinin yapısı','kas lifi çok sayıda miyofibril, mitokondri ve Ca²⁺ depolayan bir iç zar ağı içerir · Kas lifinin dışını saran zar uyartıyı iletir')],
  puf='Uyarının motor nörondan kas lifi içindeki iplikçiklere kadar izlediği yolu sırayla düşün.',sekil=SK17)

# ---------- 18 · deney: Ca²⁺, ATP, miyozin · zor · E ----------
SK18=deney_sekil({'Ca':[1,0,1,0],'ATP':[1,1,0,1],'Miyozin':[1,1,1,0],'Kasılma':[1,0,0,0]})
d18={'I':dd(True,'K ile L arasındaki tek fark Ca²⁺ iyonlarıdır; Ca²⁺ yokluğunda kasılma olmaması, kasılma için gerekli olduklarını gösterir.'),
     'II':dd(True,'K ile M arasındaki tek fark ATP’dir; ATP yokluğunda kasılma olmaması, kasılma için gerekli olduğunu gösterir.'),
     'III':dd(False,'K ile N iki bakımdan (Ca²⁺ ve miyozin) farklıdır; kasılmamanın nedeni tek bir etkene bağlanamaz.')}
o18=onc(d18,True,'D'); assert o18['dogru']=='I ve II'
QO('0018','kasilma','zor','şekilli','Kasılmanın gereksinimleri','Kontrollü deney sonuçlarından Ca²⁺, ATP ve miyozinin kasılmadaki gerekliliğini çıkarır.',
  'Kasılma için Ca²⁺, ATP ve aktin–miyozin iplikçikleri birlikte gerekir; tek fark taşıyan düzenekler karşılaştırılarak sonuç çıkarılır.',
  'Ca²⁺ ve ATP varlığının tek başına yeterli olduğunu sanmak.','kasılma koşulları deneyi',
  [A('Düzenekleri karşılaştır','L ve M, K’den tek bakımdan; N ise iki bakımdan farklıdır; sonuç ancak tek fark varsa bir etkene bağlanabilir.','L: Ca²⁺ yok · M: ATP yok · N: Ca²⁺ ve miyozin yok'),
   adim_onc(d18,'I'),adim_onc(d18,'II'),adim_onc(d18,'III'),
   A('Sonucu birleştir','I ve II çıkarılabilir; III çıkarılamaz.','Cevap: I ve II')],
  o=o18,
  metin='Zarı geçirgen duruma getirilmiş, aynı uzunlukta iskelet kası lifleri, bileşimleri farklı dört çözeltiye konmuş ve kasılma olup olmadığı gözlenmiştir. Düzenekler ve sonuçlar şekilde verilmiştir. Diğer koşulların tüm düzeneklerde eşit olduğu bilinmektedir.\nBuna göre, bu deney sonuçlarından,\nI. Kasılma için Ca²⁺ iyonları gereklidir.\nII. Kasılma için ATP gereklidir.\nIII. Kasılma için miyozin iplikçikleri gereklidir.\nsonuçlarının hangilerine ulaşılabilir?',
  istenen='Deney sonuçlarından çıkarılabilecek sonuçlar.',
  ip=['Her düzeneği kasılan düzenekle karşılaştır; yalnız bir koşulu farklı olan düzeneklerde sonucun neden değiştiğine bak.'],
  bilgi=[B('Kontrollü deney','bir etkenin sonuca etkisini görmek için yalnız o etkenin farklı, diğer koşulların aynı olduğu düzenekler karşılaştırılır')],
  puf='Tek farklı koşul taşıyan iki düzeneği karşılaştır: sonuç değişiyorsa o koşul gereklidir.',sekil=SK18)

# ---------- 19 · enerji grafiği · zor · B ----------
SK19=enerji_sekil()
assert abs(ATP(0)-ATP(60))<0.5 and KP(0)>KP(60)+15 and LA(60)>LA(0)+10
S19=[('X eğrisi ATP’ye aittir ve derişiminin sabit kalması, kasılma sırasında ATP’nin harcanmadığını gösterir.',False,'ATP kasılmada sürekli harcanır; derişiminin sabit kalması, harcanan ATP’nin kreatin fosfat ve glikoz yıkımıyla yeniden üretildiğini gösterir.'),
     ('Kreatin fosfatı gösteren eğri Y’dir ve azalması, ATP’nin yeniden oluşturulmasında kullanıldığını gösterir.',True,''),
     ('Z eğrisi, oksijenli solunumun son ürününe aittir ve artışı mitokondrideki ATP yapımının hızlandığını gösterir.',False,'Z laktik asittir; oksijensiz ortamda glikozun fermantasyonla yıkımında oluşur ve oksijenli solunumun ürünü değildir.'),
     ('Laktik asidi gösteren eğri X’tir ve kasta birikmesi kas yorgunluğuna yol açar.',False,'X sabit kalan ATP’dir; süre boyunca artan Z eğrisi laktik asittir.'),
     ('Kreatin fosfat tükendiğinde kasta ATP üretimi durur ve kasılma sürdürülemez.',False,'kreatin fosfat azalınca kas, glikozun yıkımıyla ATP üretmeyi sürdürür; Z’nin artışı bunun göstergesidir.')]
o19=tek_(S19,True,'B')
QO('0019','enerji','zor','grafik','Kasta ATP kaynakları','Şiddetli kasılmada ATP, kreatin fosfat ve laktik asit derişim değişimlerini yorumlar.',
  'Kasılmada ATP derişimi kreatin fosfat ve glikoz yıkımıyla sabit tutulur; kreatin fosfat hızla azalır, oksijen yetersizliğinde laktik asit birikir.',
  'ATP derişiminin sabit olmasını ATP’nin harcanmadığı biçiminde yorumlamak.','ATP, kreatin fosfat ve laktik asit grafiği',
  [A('Eğrileri maddelerle eşleştir','Sabit kalan eğri ATP, hızla azalan eğri kreatin fosfat, artan eğri laktik asittir.','X: ATP · Y: kreatin fosfat · Z: laktik asit'),
   A('Kreatin fosfatın rolünü yorumla','Kreatin fosfat, ADP’ye fosfat aktararak ATP’yi yeniden oluşturur; bu yüzden kreatin fosfat azalırken ATP derişimi korunur.','Y azalır → ATP yenilenir'),
   A('Seçenekleri sına','Laktik asit oksijensiz yıkımın ürünüdür ve ATP kasılma boyunca harcanır; kreatin fosfat bitince glikoz yıkımı ATP sağlamayı sürdürür.','Y’nin işlevi doğru, diğerleri yanlış')],
  o=o19,
  metin='Şiddetli ve kısa süreli kasılma yapan bir iskelet kasında ATP, kreatin fosfat ve laktik asit derişimlerinin süre içindeki değişimi X, Y ve Z eğrileriyle gösterilmiştir. Kasa yeterli oksijen ulaşmamaktadır ve hangi eğrinin hangi maddeye ait olduğu belirtilmemiştir.\nBuna göre, aşağıdakilerden hangisi doğrudur?',
  istenen='Grafikle uyumlu doğru ifade.',
  ip=['Önce hangi eğrinin hangi maddeyi gösterdiğini davranışlarına bakarak belirle; sonra her maddenin kasta üstlendiği rolü sırala.'],
  bilgi=[B('Kasta enerji','kasılma enerjisini ATP sağlar; ATP yedeği azdır ve kreatin fosfat, glikoz yıkımı gibi kaynaklarla sürekli yenilenir · Oksijensiz yıkımın ürünü laktik asittir')],
  puf='Hangi maddenin sabit kaldığını ve bunun nasıl mümkün olduğunu sorgula.',sekil=SK19)

# ---------- 20 · kol bükülmesi · zor · C ----------
SK20=kol_sekil({'on':'II','arka':'I'})
S20=[('I numaralı kasta ince ve kalın iplikçiklerin boyu uzar, II numaralı kasta kısalır.',False,'iplikçiklerin boyu ne kasılmada ne gevşemede değişir; iplikçikler yalnız birbiri üzerinde kayar.'),
     ('Her iki kasta da Z çizgileri arasındaki uzaklık azalır.',False,'gevşeyen kasta sarkomer uzar; Z çizgileri arası uzaklık artar, yalnız kasılan kasta azalır.'),
     ('I numaralı kasta H bölgesi genişlerken II numaralı kasta daralır.',True,''),
     ('II numaralı kasta A bandı kısalırken I numaralı kasta uzar.',False,'A bandı kalın iplikçik boyuna eşittir ve iki kasta da değişmez.'),
     ('Kolu bükmek için gereken çekme kuvvetini I numaralı kas oluşturur.',False,'kaslar yalnız kasılarak çeker; kolu bükme kuvvetini kasılan kas (II) oluşturur, gevşeyen kas (I) kuvvet üretmez.')]
o20=tek_(S20,True,'C')
QO('0020','hareket','zor','şekilli','Karşıt çalışan kaslar ve sarkomer','Karşıt çalışan kasların durumunu sarkomer düzeyinde yorumlar.',
  'Karşıt çalışan kaslarda sarkomer durumları.',
  'Gevşeyen kastaki iplikçiklerin uzadığını ya da gevşeyen kasın da kuvvet ürettiğini sanmak.','dirsek bükülmesinde sarkomer değişimi',
  [A('Kasların durumunu belirle','Şekilde kol bükülürken kalın ve kısa görünen II kasılan, ince ve uzun görünen I gevşeyen kastır; kaslar karşıt çalışır.','II: kasılı · I: gevşek'),
   A('Sarkomer değişimini yaz','Kasılan kasta Z–Z, I bandı ve H bölgesi kısalır; gevşeyen kasta sarkomerler uzar, H bölgesi genişler.','II: H daralır · I: H genişler'),
   A('İfadeleri sına','İplikçik boyu ve A bandı iki kasta da sabittir; kuvvet kasılan kastan gelir.','İplikçik, A bandı: sabit')],
  o=o20,
  metin='Şekilde, bir kişinin kolunu dirsekten bükerken kasların durumu gösterilmiştir. Kolun ön ve arka yüzündeki kaslar birbirine zıt etki yapar ve hareket sırasında biri kasılırken diğeri gevşer.\nBuna göre, I ve II numaralı kasların sarkomerleriyle ilgili aşağıdakilerden hangisi doğrudur?',
  istenen='I ve II numaralı kasların sarkomerleri için doğru ifade.',
  ip=['Hangi kasın kasıldığını şekildeki kalınlık ve kolun hareket yönünden çıkar; kasılan ve gevşeyen kasta sarkomerin nasıl değiştiğini ayrı ayrı yaz.'],
  bilgi=[B('Karşıt çalışan kaslar','bir eklemi hareket ettiren kaslar çiftler hâlinde çalışır: biri kasılıp eklemi bir yöne çekerken öteki gevşer · Kaslar yalnız kasılarak çeker, itme yapmaz')],
  puf='Önce hangi kasın kasıldığını belirle, sonra her kasın sarkomer ve iplikçik durumunu ayrı ayrı yaz.',sekil=SK20)

# ======================= BİTİŞ =======================
from collections import Counter
def bitir_ayt(P,onek,k):
    for q in P.ANA: q['kardes']=None
    P.yaz(os.path.join(GD,f'{onek}-1.json'),f'/tmp/bos-{onek}.json')
    tipler={}
    for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=k))['kartlar'].append(c['id'])
    json.dump(dict(konu=P.konu_adi,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2018–2026 Biyoloji çıkmış soruları (yalnız mantık), MEB 11. sınıf Destek ve Hareket Sistemi.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar',f'ab{onek}.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler))
bitir_ayt(P,'destek',KEY)
assert len(P.ANA)==20 and Counter(q['cevap']['sik'] for q in P.ANA)=={'A':4,'B':4,'C':4,'D':4,'E':4},Counter(q['cevap']['sik'] for q in P.ANA)
