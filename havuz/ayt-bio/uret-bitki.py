"""AYT Biyoloji · Bitki Biyolojisi · 20 soru. Kardeş yok, ipucu 1.
Şekil koordinatları, grafik verileri, kromozom hesapları ve öncül doğrulukları Python'da tek yerde tanımlanır; TikZ/pgfplots bu değerlerden üretilir."""
import sys,os,json,math,random,itertools
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-bio')); sys.path.insert(0,os.path.join(HV,'tyt-kim'))
import _hafif_bio as H
from _hafif_bio import *
from _hafif_kim import onc as _onc, tek
KONU_AD='Bitki Biyolojisi'; KEY='abio|Bitki Biyolojisi'
P=Parti('bitki',KONU_AD,KEY,ders='AYT Biyoloji',idon='aytbio'); H.KONU=KONU_AD
KAYNAK='ÖSYM AYT 2018–2026 Biyoloji bitki biyolojisi soruları (yalnız mantık) · MEB 11. sınıf Bitki Biyolojisi'
TIP={'doku':('bt-doku','Bitki dokuları ve özellikleri'),'yapi':('bt-yapi','Kök, gövde ve yaprak yapısı'),'tasima':('bt-tasima','Su ve madde taşınması'),
     'terleme':('bt-terleme','Terleme ve stoma hareketleri'),'hormon':('bt-hormon','Bitki hormonları'),'hareket':('bt-hareket','Tropizma ve nasti hareketleri'),
     'ureme':('bt-ureme','Çiçek, tohum ve çimlenme'),'buyume':('bt-buyume','Bitkilerde büyüme')}
def Q(no,tp,z,kalip,alt,kaz,fikir,tuzak,ozet,ad,**k):
    t,tn=TIP[tp]; assert len(k['ip'])==1
    kart(f'K-ABBIT-{no}',alt,fikir,tuzak,z,kalip,len(ad),t,tn,KAYNAK)
    mk(P,'00'+no,ad=ad,adim=len(ad),tipId=t,tip=tn,z=z,alt=alt,kaz=kaz,kalip=kalip,kart=f'K-ABBIT-{no} ({ozet})',**k)
import re
def kucult(s):
    def f(m):
        v=float(m.group(0)); a=abs(v); t=f'{v:.1f}' if a>=10 else (f'{v:.2f}' if a>=1 else f'{v:.3f}')
        if '.' in t: t=t.rstrip('0').rstrip('.')
        return t or '0'
    return re.sub(r'(?<![\w#.])-?\d+\.\d{3,}',f,s)
def tk(g,scale=1.0): return kucult(tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small,scale=%s]\n%s\n\\end{tikzpicture}'%(scale,g)))
def yerles(dogru,yanlislar,i): return list(yanlislar[:i])+[dogru]+list(yanlislar[i:])
ARR='-{Stealth[length=2.2mm,width=1.8mm]}'
def etiket(t,x,y,x1,y1,x2,y2):
    return f'\\node[font=\\normalsize\\bfseries] at ({x},{y}) {{{t}}};\\draw[{ARR},line width=.8pt] ({x1},{y1})--({x2},{y2});'
# öncüllü seçenek üretici (hedef: doğru kümenin şık sırası)
def _anah(s): return (len(s),tuple(s))
def onc_t(d,hedef):
    sir=['I','II','III']; T=frozenset(k for k,v in d.items() if v[0])
    ad=lambda s:tuple(sorted(s,key=sir.index))
    adaylar=sorted([c for n in range(1,4) for c in itertools.combinations(sir,n)],key=_anah); kt=_anah(ad(T))
    alt=[c for c in adaylar if _anah(c)<kt]; ust=[c for c in adaylar if _anah(c)>kt]
    assert hedef<=len(alt) and 4-hedef<=len(ust),('hedef uygun degil',T,hedef,len(alt),len(ust))
    uz=lambda c:len(frozenset(c)^T)
    sa=sorted(alt,key=lambda c:(uz(c),-adaylar.index(c)))[:hedef]; su=sorted(ust,key=lambda c:(uz(c),adaylar.index(c)))[:4-hedef]
    ops=sorted(sa+[ad(T)]+su,key=_anah); assert ops.index(ad(T))==hedef
    return _onc(d,ops)
def oy(d): return ' · '.join(f'{k}: '+('doğru' if d[k][0] else 'yanlış') for k in d)
def tum(d): return ' '.join(f'{k}. '+('doğru' if d[k][0] else 'yanlış')+f' çünkü {d[k][1]}.' for k in d)

# ================= ŞEKİLLER =================
def f_kok():
    b=[]; R=2.6
    b.append(f'\\draw[line width=1.7pt] (0,0) circle ({R});\\draw[line width=.6pt] (0,0) circle ({R-.24});')
    for k in range(24):
        a=math.radians(k*15); b.append(f'\\draw[line width=.5pt] ({(R-.24)*math.cos(a):.2f},{(R-.24)*math.sin(a):.2f})--({R*math.cos(a):.2f},{R*math.sin(a):.2f});')
    for a in (20,60,100,200,240,280,320,350):
        r=math.radians(a); b.append(f'\\draw[line width=1pt] ({R*math.cos(r):.2f},{R*math.sin(r):.2f})--({(R+.42)*math.cos(r):.2f},{(R+.42)*math.sin(r):.2f});')
    for rr,n in ((1.98,16),(1.5,11)):
        for k in range(n):
            a=math.radians(k*360/n+(8 if rr<1.7 else 0)); b.append(f'\\draw[line width=.5pt,fill=black,fill opacity=.05] ({rr*math.cos(a):.2f},{rr*math.sin(a):.2f}) circle (.25);')
    b.append('\\fill[black,fill opacity=.22,even odd rule] (0,0) circle (1.2) (0,0) circle (1.0);\\draw[line width=.7pt] (0,0) circle (1.2);\\draw[line width=.7pt] (0,0) circle (1.0);')
    for k in range(12):
        a=math.radians(k*30); b.append(f'\\draw[line width=.5pt] ({1.0*math.cos(a):.2f},{1.0*math.sin(a):.2f})--({1.2*math.cos(a):.2f},{1.2*math.sin(a):.2f});')
    b.append('\\draw[line width=.5pt] (0,0) circle (.86);')
    for a in (0,90,180,270):
        b.append(f'\\begin{{scope}}[rotate={a}]\\draw[rounded corners=2pt,fill=black,fill opacity=.5,line width=.6pt] (0,-.15) rectangle (.78,.15);\\draw[fill=white,line width=.5pt] (.62,0) circle (.09);\\end{{scope}}')
    b.append('\\fill[black,fill opacity=.5] (0,0) circle (.2);')
    for a in (45,135,225,315):
        r=math.radians(a)
        for dr in (.47,.65):
            b.append(f'\\draw[line width=.6pt,fill=white] ({dr*math.cos(r):.2f},{dr*math.sin(r):.2f}) circle (.09);')
    b.append(etiket('I',-3.6,1.9,-3.3,1.75,-2.25,1.3))      # epidermis
    b.append(etiket('II',3.7,2.2,3.35,2.05,1.7,1.35))        # korteks
    b.append(etiket('III',3.7,-.6,3.3,-.45,.6,.0))           # ksilem (sağ kol ucu)
    b.append(etiket('IV',-3.6,-2.0,-3.25,-1.85,-.5,-.5))     # floem
    b.append(etiket('V',3.7,-2.2,3.35,-2.05,.95,-.75))       # endodermis
    return tk('\n'.join(b),.82)
def f_yaprak():
    b=[]; random.seed(5)
    b.append('\\draw[line width=2.2pt] (0,4.1)--(6,4.1);\\draw[line width=2.2pt] (0,.38)--(6,.38);')
    for i in range(10): b.append(f'\\draw[line width=.7pt,fill=black,fill opacity=.06] ({i*.6:.2f},3.6) rectangle ({(i+1)*.6:.2f},4.05);')
    for i in range(12): b.append(f'\\draw[line width=.7pt,rounded corners=2pt,fill=black,fill opacity=.04] ({i*.5+.03:.2f},2.45) rectangle ({(i+1)*.5-.03:.2f},3.55);')
    cells=[]; bx,by=3.0,1.55
    dene=0
    while len(cells)<20 and dene<4000:
        dene+=1
        x=random.uniform(.25,5.75); y=random.uniform(1.05,2.25)
        if (x-bx)**2+(y-by)**2<.72**2: continue
        if abs(x-4.6)<.55 and y<1.5: continue
        if all((x-a)**2+(y-c)**2>.58**2 for a,c in cells): cells.append((x,y))
    for x,y in cells: b.append(f'\\draw[line width=.6pt,fill=black,fill opacity=.04] ({x:.2f},{y:.2f}) ellipse ({random.uniform(.2,.27):.2f} and {random.uniform(.15,.21):.2f});')
    b.append(f'\\draw[line width=.9pt,fill=white] ({bx},{by}) circle (.58);\\draw[line width=.6pt] ({bx},{by}) circle (.5);')
    b.append(f'\\fill[black,fill opacity=.5] ({bx-.28},{by+.05}) rectangle ({bx+.28},{by+.4});')
    for dx in (-.2,0,.2): b.append(f'\\draw[line width=.6pt,fill=white] ({bx+dx},{by-.22}) circle (.075);')
    for i in range(10):
        if i==7:
            b.append('\\draw[line width=.7pt,fill=black,fill opacity=.14] (4.4,.72) ellipse (.17 and .26);\\draw[line width=.7pt,fill=black,fill opacity=.14] (4.82,.72) ellipse (.17 and .26);')
            b.append('\\draw[line width=.7pt] (4.2,.42)--(4.2,.98)(5.04,.42)--(5.04,.98);')
        elif i==8: pass
        else: b.append(f'\\draw[line width=.7pt,fill=black,fill opacity=.06] ({i*.6:.2f},.42) rectangle ({(i+1)*.6:.2f},.98);')
    b.append('\\draw[line width=.7pt,fill=black,fill opacity=.06] (5.4,.42) rectangle (6.0,.98);')
    b.append(etiket('I',7.0,3.85,6.7,3.85,5.75,3.85)); b.append(etiket('V',7.0,3.0,6.7,3.0,5.8,3.0))
    b.append(etiket('II',7.0,1.9,6.7,1.9,5.6,1.85)); b.append(etiket('IV',7.0,.7,6.7,.7,5.8,.7))
    b.append(etiket('III',-.9,1.55,-.55,1.55,2.4,1.55))
    return tk('\n'.join(b),.82)
def demet(x,y,ang,kamb=False):
    kb='\\draw[line width=.9pt] (.0,-.19)--(.0,.19);' if kamb else ''
    return (f'\\begin{{scope}}[shift={{({x:.2f},{y:.2f})}},rotate={ang:.0f}]\\draw[line width=.7pt,fill=white] (0,0) ellipse (.36 and .22);'+kb+
            '\\fill[black,fill opacity=.55] (-.15,0) circle (.1);\\draw[line width=.5pt,fill=white] (.16,0) circle (.08);\\end{scope}')
def f_govde():
    b=[]; random.seed(9)
    for cx,ad in ((0,'A'),(5.2,'B')):
        b.append(f'\\draw[line width=1.6pt] ({cx},0) circle (1.95);\\draw[line width=.5pt] ({cx},0) circle (1.75);')
        if ad=='A':
            for k in range(8):
                a=math.radians(k*45+10); b.append(demet(cx+1.3*math.cos(a),1.3*math.sin(a),math.degrees(a),True))
        else:
            pts=[]; dn=0
            while len(pts)<11 and dn<20000:
                dn+=1
                r=1.6*math.sqrt(random.random()); a=random.uniform(0,2*math.pi); x,y=r*math.cos(a),r*math.sin(a)
                if all((x-u)**2+(y-v)**2>.66**2 for u,v in pts): pts.append((x,y))
            for x,y in pts: b.append(demet(cx+x,y,math.degrees(math.atan2(y,x))))
        b.append(f'\\node[font=\\large\\bfseries] at ({cx},-2.45) {{{ad}}};')
    b.append('\\fill[black,fill opacity=.55] (-1.3,-3.35) circle (.1);\\node[anchor=west] at (-1.1,-3.35) {ksilem};\\draw[line width=.5pt,fill=white] (1.2,-3.35) circle (.07);\\node[anchor=west] at (1.4,-3.35) {floem};')
    return tk('\n'.join(b),.78)
def f_stoma():
    b=[]
    for s in (1,-1):
        pts=' '.join(f'({s*x},{y})' for x,y in ((.12,1.2),(.7,1.0),(1.15,.4),(1.2,-.4),(.7,-1.0),(.12,-1.2),(.4,-.5),(.44,.5)))
        b.append(f'\\draw[line width=1pt,smooth cycle,fill=black,fill opacity=.12,tension=.8] plot coordinates {{{pts}}};')
        b.append(f'\\draw[line width=3pt,smooth] plot coordinates {{({s*.12},1.2) ({s*.44},.5) ({s*.4},-.5) ({s*.12},-1.2)}};')
        b.append(f'\\draw[line width=.7pt,fill=black,fill opacity=.3] ({s*.85},0) ellipse (.12 and .2);')
        b.append(f'\\draw[line width=1pt,rounded corners=10pt] ({s*1.45},-1.75) rectangle ({s*3.7},1.75);\\draw[line width=.7pt,fill=black,fill opacity=.3] ({s*2.9},1.0) circle (.2);')
        b.append(f'\\draw[{ARR},vurgu,line width=1.7pt] ({s*2.6},.25)--({s*1.5},.2);\\node[font=\\normalsize] at ({s*2.2},.62) {{K$^+$}};')
        b.append(f'\\draw[{ARR},vurgu!60!black,line width=1.7pt,dashed] ({s*2.6},-.6)--({s*1.5},-.5);\\node[font=\\normalsize] at ({s*2.2},-.98) {{H$_2$O}};')
    return tk('\n'.join(b),.85)
# ---- tüp deneyi (Q7): kayıp su mL, tek yerde
KAYIP={'K':9,'L':2,'M':8,'N':1}; UST,ALT,DIGER=1,7,1
assert KAYIP['K']==UST+ALT+DIGER and KAYIP['L']==UST+DIGER and KAYIP['M']==ALT+DIGER and KAYIP['N']==DIGER
def f_tup():
    b=[]; H0=3.0; ol=.22
    for i,(ad,vz_u,vz_a) in enumerate((('K',0,0),('L',0,1),('M',1,0),('N',1,1))):
        x=i*2.3; sv=H0-KAYIP[ad]*ol
        b.append(f'\\fill[vurgu,fill opacity=.16] ({x-.45},0) rectangle ({x+.45},{sv:.2f});')
        b.append(f'\\draw[line width=1.3pt] ({x-.45},4.1)--({x-.45},0)--({x+.45},0)--({x+.45},4.1);')
        b.append(f'\\draw[line width=.7pt,dashed] ({x-.45},{H0})--({x+.45},{H0});')
        b.append(f'\\fill[black,fill opacity=.65] ({x-.45},{sv:.2f}) rectangle ({x+.45},{sv+.09:.2f});')
        b.append(f'\\draw[line width=1.6pt] ({x},.35)--({x},5.3);')
        for sy,sg in ((5.1,1),(4.4,-1)):
            u='3.2pt' if vz_u else '.8pt'; a='3.2pt' if vz_a else '.8pt'
            b.append(f'\\begin{{scope}}[shift={{({x},{sy})}},xscale={sg},rotate=12]\\draw[line width={u},{"vurgu!50!black" if vz_u else "black"}] (0,0) arc(180:0:.7 and .2);\\draw[line width={a},{"vurgu!50!black" if vz_a else "black"}] (0,0) arc(180:360:.7 and .2);\\end{{scope}}')
        b.append(f'\\node[font=\\large\\bfseries] at ({x},-.5) {{{ad}}};\\node[font=\\small] at ({x},-1.05) {{{KAYIP[ad]} mL}};')
    b.append('\\node[font=\\scriptsize,anchor=east] at (-.55,3.0) {başlangıç};')
    b.append('\\draw[line width=3.2pt,vurgu!50!black] (-.4,-1.8)--(.2,-1.8);\\node[anchor=west,font=\\small] at (.3,-1.8) {vazelin sürülen yüzey};')
    return tk('\n'.join(b),.62)
# ---- su dengesi grafiği (Q8)
ZS=[0,3,6,9,12,15,18,21,24]
TR=[2,2,2,10,22,26,22,10,2]; AL=[2,2,2,4,10,16,18,10,4]
def trap(f,a,b_): return (f(a)+f(b_))*(b_-a)/2
def denge():
    D=[0]
    for i in range(1,len(ZS)): D.append(D[-1]+3*((AL[i-1]+AL[i])/2-(TR[i-1]+TR[i])/2))
    return D
DEN=denge(); assert DEN.index(min(DEN))==ZS.index(21) and ZS[TR.index(max(TR))]==15 and ZS[AL.index(max(AL))]==18
FARK=[a-t for a,t in zip(AL,TR)]; assert ZS[FARK.index(min(FARK))]==12 and AL[ZS.index(21)]==TR[ZS.index(21)]
def f_denge():
    ct=' '.join(f'({z},{v})' for z,v in zip(ZS,TR)); ca=' '.join(f'({z},{v})' for z,v in zip(ZS,AL))
    g=['\\begin{axis}[width=8cm,height=5.4cm,xmin=0,xmax=24,ymin=0,ymax=30,xtick={0,3,6,9,12,15,18,21,24},ytick={0,10,20,30},axis lines=left,xlabel={Günün saati},ylabel={Hız (mL/saat)},tick label style={font=\\footnotesize},label style={font=\\small},every axis plot/.append style={line width=1.5pt},legend style={at={(0.02,0.98)},anchor=north west,font=\\footnotesize,draw=none,fill=none}]',
       f'\\addplot[black] coordinates {{{ct}}};\\addlegendentry{{Terleme hızı}}',f'\\addplot[vurgu,dashed] coordinates {{{ca}}};\\addlegendentry{{Su alım hızı}}','\\end{axis}']
    return tk('\n'.join(g))
def f_floem():
    b=[]
    b.append('\\draw[line width=1.1pt,fill=vurgu,fill opacity=.18] (-1.2,4.1) .. controls (-.3,5.0) and (1.0,4.9) .. (1.3,4.1) .. controls (.4,3.4) and (-.7,3.5) .. (-1.2,4.1);')
    b.append('\\draw[line width=.7pt] (-.9,4.1)--(1.0,4.1);')
    b.append('\\draw[line width=1.2pt] (1.55,3.7)--(1.55,.7)(2.15,3.7)--(2.15,.7);')
    for y in (3.3,2.7,2.1,1.5,.9): b.append(f'\\draw[line width=.8pt] (1.55,{y})--(2.15,{y});')
    b.append('\\draw[line width=1.2pt] (2.7,3.7)--(2.7,.7)(3.5,3.7)--(3.5,.7);\\draw[line width=.6pt,dotted] (3.1,3.6)--(3.1,.8);')
    b.append('\\draw[line width=1.1pt,fill=black,fill opacity=.08] (2.6,.1) ellipse (1.8 and .62);')
    b.append(f'\\draw[{ARR},line width=2pt,vurgu] (1.85,3.5)--(1.85,1.1);\\draw[{ARR},line width=2pt] (3.1,1.3)--(3.1,3.3);')
    b.append(f'\\draw[{ARR},line width=1.2pt] (1.0,3.75)--(1.5,3.55);\\node[font=\\footnotesize] at (.55,3.35) {{şeker}};')
    b.append(etiket('I',-1.6,4.9,-1.35,4.8,-.9,4.45)); b.append(etiket('II',.85,2.2,1.15,2.2,1.5,2.2))
    b.append(etiket('III',4.3,2.4,4.0,2.4,3.55,2.4)); b.append(etiket('IV',5.1,.1,4.8,.1,4.45,.1))
    return tk('\n'.join(b),.82)
def f_koleoptil():
    b=[]
    for i,ad in enumerate('ABCD'):
        x=i*2.1; h=2.7 if ad!='A' else 2.2
        b.append(f'\\draw[line width=1.2pt,rounded corners=4pt,fill=vurgu,fill opacity=.12] ({x-.3},0) rectangle ({x+.3},{h});')
        if ad=='A':
            b.append(f'\\draw[line width=.8pt,dashed,rounded corners=3pt,rotate around={{70:({x+.9},.25)}}] ({x+.7},.1) rectangle ({x+1.0},.62);')
        if ad=='B': b.append(f'\\draw[line width=1pt,fill=black,rounded corners=2pt] ({x-.38},2.05) rectangle ({x+.38},2.78);')
        if ad=='C': b.append(f'\\draw[line width=1pt,dashed,rounded corners=2pt,fill=white,fill opacity=.5] ({x-.38},2.05) rectangle ({x+.38},2.78);')
        if ad=='D': b.append(f'\\draw[line width=1pt,fill=black,rounded corners=2pt] ({x-.38},.25) rectangle ({x+.38},1.45);')
        b.append(f'\\draw[line width=1pt] ({x-.8},0)--({x+.8},0);\\node[font=\\large\\bfseries] at ({x},-.5) {{{ad}}};')
        for yy in (2.2,.9):
            if ad=='A' and yy>2.0: yy=1.8
            b.append(f'\\draw[{ARR},line width=1.4pt,orange!85!black] ({x+1.0},{yy})--({x+.5},{yy});')
    return tk('\n'.join(b),.82)
# ---- oksin grafiği (Q12)
KOK={-11:0,-10:30,-9:10,-8:-30,-7:-60,-6:-90,-5:-100,-4:-100,-3:-100}
GOV={-11:0,-10:0,-9:0,-8:5,-7:20,-6:50,-5:80,-4:50,-3:-20}
ALTD,USTD=-6,-9
gv=(GOV[ALTD],GOV[USTD]); kk=(KOK[ALTD],KOK[USTD])
assert gv[0]>gv[1] and kk[0]<kk[1]    # gövde: alt hızlı → yukarı; kök: üst hızlı → aşağı
def f_oksin():
    ck=' '.join(f'({x},{y})' for x,y in KOK.items()); cg=' '.join(f'({x},{y})' for x,y in GOV.items())
    g=['\\begin{axis}[width=8cm,height=5.6cm,xmin=-11,xmax=-3,ymin=-110,ymax=100,xtick={-9,-6,-3},xticklabels={$10^{-9}$,$10^{-6}$,$10^{-3}$},ytick={-100,0,100},axis lines=left,xlabel={Oksin derişimi (M)},ylabel={Uzama hızı değişimi (\\%)},tick label style={font=\\footnotesize},label style={font=\\small},every axis plot/.append style={line width=1.5pt}]',
       '\\draw[dashed,line width=.6pt] (axis cs:-11,0)--(axis cs:-3,0);',
       f'\\addplot[black,smooth] coordinates {{{ck}}};\\addplot[vurgu,smooth] coordinates {{{cg}}};',
       '\\node[font=\\small\\bfseries] at (axis cs:-4.4,-80) {Kök};\\node[font=\\small\\bfseries,vurgu!60!black] at (axis cs:-7.4,48) {Gövde};','\\end{axis}']
    return tk('\n'.join(g))
def f_apikal():
    b=[]
    for i,ad in enumerate('ABCD'):
        x=i*2.6; uzun=ad in 'BD'
        b.append(f'\\draw[line width=1.8pt] ({x},0)--({x},3.0);\\draw[line width=1pt] ({x-.8},0)--({x+.8},0);')
        for sy in (1.0,1.9,2.6):
            for sg in (1,-1):
                if uzun:
                    b.append(f'\\draw[line width=1.4pt,vurgu!60!black] ({x},{sy})--({x+sg*.5},{sy+.85});\\draw[fill=vurgu,fill opacity=.4,line width=.6pt] ({x+sg*.5},{sy+.85}) ellipse (.14 and .09);')
                else: b.append(f'\\draw[fill=vurgu,fill opacity=.5,line width=.7pt] ({x+sg*.1},{sy+.05}) ellipse (.11 and .07);')
        if ad in 'AD': b.append(f'\\draw[fill=vurgu,fill opacity=.5,line width=.8pt] ({x},3.2) ellipse (.13 and .22);')
        else: b.append(f'\\draw[line width=1.3pt] ({x-.1},3.0)--({x+.1},3.0);')
        if ad=='C': b.append(f'\\draw[line width=.7pt,fill=black,fill opacity=.45] ({x},3.12) ellipse (.2 and .12);\\node[font=\\footnotesize,anchor=south] at ({x},3.35) {{oksin}};')
        if ad=='D':
            for sy in (1.0,1.9,2.6):
                for sg in (1,-1): b.append(f'\\fill[black,fill opacity=.7] ({x+sg*.17},{sy+.12}) circle (.05);')
            b.append(f'\\node[font=\\footnotesize,anchor=north] at ({x},-.2) {{sitokinin}};')
        b.append(f'\\node[font=\\large\\bfseries] at ({x},-.75) {{{ad}}};' if ad!='D' else f'\\node[font=\\large\\bfseries] at ({x},-.95) {{{ad}}};')
    return tk('\n'.join(b),.78)
def f_cicek():
    b=[]
    b.append('\\draw[line width=1pt,smooth cycle,fill=black,fill opacity=.05] plot coordinates {(-0.75,0.1) (-0.85,0.8) (-0.5,1.45) (0,1.6) (0.5,1.45) (0.85,0.8) (0.75,0.1) (0,-0.1)};')
    for sx in (-.3,.3): b.append(f'\\draw[line width=.8pt,fill=white] ({sx},.8) ellipse (.18 and .26);\\draw[line width=.5pt] ({sx},.82) circle (.07);')
    b.append('\\draw[line width=1.1pt] (-.12,1.6)--(-.1,3.4)(.12,1.6)--(.1,3.4);\\draw[line width=1pt,fill=black,fill opacity=.3] (0,3.6) ellipse (.3 and .2);')
    for s in (-1,1):
        b.append(f'\\draw[line width=1.1pt] ({s*.8},.2) .. controls ({s*1.25},.8) and ({s*1.4},1.6) .. ({s*1.1},1.9);\\draw[line width=1pt,fill=black,fill opacity=.2] ({s*1.1},2.3) ellipse (.26 and .4);\\draw[line width=.5pt] ({s*1.1},1.95)--({s*1.1},2.65);')
        pts=' '.join(f'({s*x},{y})' for x,y in ((.5,-.05),(1.6,.3),(2.4,1.2),(2.65,2.4),(2.3,3.3),(1.95,2.4),(1.7,1.4),(1.0,.5)))
        b.append(f'\\draw[line width=.9pt,smooth cycle,fill=black,fill opacity=.04] plot coordinates {{{pts}}};')
    b.append('\\draw[line width=1pt] (-.4,-.1) .. controls (-.2,-.5) and (.2,-.5) .. (.4,-.1);')
    b.append(etiket('I',1.8,4.3,1.5,4.15,.35,3.7)); b.append(etiket('II',1.8,3.1,1.5,3.05,.15,2.9)); b.append(etiket('III',-3.6,.5,-3.3,.5,-.85,.7))
    b.append(etiket('IV',3.7,-.9,3.4,-.8,.4,.65)); b.append(etiket('V',-1.1,3.7,-1.1,3.45,-1.1,2.75)); b.append(etiket('VI',-3.6,1.4,-3.3,1.4,-1.25,1.4))
    b.append(etiket('VII',3.9,2.4,3.55,2.4,2.7,2.4))
    return tk('\n'.join(b),.8)
def f_kese():
    b=[]
    b.append('\\draw[line width=1.5pt] (0,0) ellipse (1.25 and 2.2);')
    b.append('\\draw[line width=.9pt,fill=black,fill opacity=.06] (0,1.2) ellipse (.32 and .38);\\draw[line width=.8pt,fill=black,fill opacity=.5] (0,1.15) circle (.1);')
    for s in (-1,1): b.append(f'\\draw[line width=.9pt,fill=black,fill opacity=.06] ({s*.58},1.55) ellipse (.2 and .3);\\draw[line width=.8pt,fill=black,fill opacity=.5] ({s*.58},1.55) circle (.07);')
    b.append('\\draw[line width=.8pt,fill=black,fill opacity=.65] (-.18,.1) circle (.12);\\draw[line width=.8pt,fill=black,fill opacity=.65] (.18,-.1) circle (.12);')
    for x,y in ((-.55,-1.4),(0,-1.65),(.55,-1.4)): b.append(f'\\draw[line width=.9pt,fill=black,fill opacity=.06] ({x},{y}) ellipse (.22 and .3);\\draw[line width=.8pt,fill=black,fill opacity=.5] ({x},{y}) circle (.07);')
    b.append(etiket('I',2.5,.85,2.2,.85,.35,1.0)); b.append(etiket('II',2.5,-.1,2.2,-.1,.32,-.05))
    b.append(etiket('III',-2.5,1.9,-2.2,1.85,-.8,1.6)); b.append(etiket('IV',2.5,-1.6,2.2,-1.55,.8,-1.45))
    return tk('\n'.join(b),.85)
# ---- ABA grafiği (Q18)
GN=list(range(9))
ABA=[10,12,20,45,75,90,96,98,100]; STO=[100,98,90,65,35,18,10,8,8]; FOT=[100,100,97,85,55,35,25,20,18]
def f_aba():
    g=['\\begin{axis}[width=8cm,height=5.4cm,xmin=0,xmax=8,ymin=0,ymax=105,xtick={0,2,4,6,8},ytick={0,50,100},axis lines=left,xlabel={Kuraklık süresi (gün)},ylabel={Göreli değer (\\%)},tick label style={font=\\footnotesize},label style={font=\\small},every axis plot/.append style={line width=1.5pt},legend style={at={(0.5,-0.32)},anchor=north,legend columns=3,font=\\footnotesize,draw=none,/tikz/every even column/.append style={column sep=.3cm}}]']
    for nm,v,st in (('ABA',ABA,'vurgu'),('Stoma açıklığı',STO,'black'),('Fotosentez',FOT,'black,dashed')):
        g.append(f'\\addplot[{st}] coordinates {{{" ".join(f"({x},{y})" for x,y in zip(GN,v))}}};\\addlegendentry{{{nm}}}')
    g.append('\\end{axis}'); return tk('\n'.join(g))

# ================= SORULAR =================
# ---- 01 · kök kesiti · kolay
SK=f_kok()
Q('01','yapi','kolay','şekilli','Kök yapısı','Kök enine kesitindeki dokuları tanıyıp olgun hâlde cansız olan iletim dokusunu belirler.',
  'Dikotil kök kesitinde dıştan içe epidermis, korteks, endodermis ve merkezde ksilem–floem bulunur; olgunlaşınca cansız olan iletim dokusu ksilemdir.','Floemi de çekirdeksiz olduğu için cansız sanmak; endodermisi iletim dokusu saymak.','kök kesiti, cansız iletim dokusu',
  [A('Kesitteki yapıları tanı','Dışta tek sıra hâlinde epidermis, altında yuvarlak hücreli korteks, ince halka biçimli endodermis; merkezde çapraz biçimli ksilem ve arada küçük hücre öbekleri hâlinde floem yer alır.','I: epidermis · II: korteks · III: ksilem · IV: floem · V: endodermis'),
   A('Özelliği iletim dokularıyla eşleştir','Olgunlaştığında çekirdek ve sitoplazmasını yitiren cansız hücreler suyu ileten dokuyu oluşturur. Organik maddeyi taşıyan doku ise canlı hücrelerden kurulur.','Cansız, su ileten doku → ksilem'),
   A('Numarayı bul','Ksilem, şekilde merkezde çapraz biçimli yapıdır.','Cevap: III')],
  metin='Şekilde, çift çenekli bir bitkinin kökünden alınan enine kesit şematik olarak verilmiştir. Kesitte dıştaki hücre tabakası kök tüyleri taşımaktadır.\nBuna göre, numaralı yapılardan hangisi olgunlaştığında çekirdek ve sitoplazmasını yitirmiş, cansız hücrelerden oluşur ve kökün aldığı suyu gövdeye ileten dokudur?',
  dogru='III',sira=['I','II','III','IV','V'],
  yan=[('I','I numaralı yapı epidermistir; canlı hücrelerden oluşur ve kök tüyleriyle su alımına katılır, su iletimi yapmaz.','bilgi'),
       ('II','II numaralı yapı korteksidir; canlı parankima hücreleri su ve besin depolar, olgun hâlde cansız değildir.','bilgi'),
       ('IV','IV numaralı yapı floemdir; kalburlu boru hücrelerinin çekirdeği olmasa da sitoplazması canlıdır ve organik madde taşır, bu nedenle cansız değildir.','bilgi'),
       ('V','V numaralı yapı endodermistir; korteksle iletim demetleri arasındaki canlı hücre tabakasıdır ve su iletmez.','bilgi')],
  istenen='Olgun hâlde cansız hücrelerden oluşan su iletim dokusunun numarası.',
  ip=['Kökte su ve organik madde taşıyan iki iletim dokusunun hangi özelliklerle birbirinden ayrıldığını düşün; şekildeki yapıların biçimlerine bak.'],
  bilgi=[B('Kök enine kesiti','dışta epidermis, altında korteks, ardından endodermis ve merkezde iletim demetlerinin bulunduğu silindir yer alır; iletim demeti iki tür iletim dokusundan oluşur'),
         B('Bitki dokularında hücre canlılığı','bazı dokular olgunlaştığında protoplastlarını kaybeder ve cansız hücrelerden oluşur; çeperi ligninle kalınlaşan hücrelerde bu durum sık görülür. Örnek: odun lifleri')],
  puf='Olgunlaşınca cansız kalan ve su ileten doku ksilemdir; organik madde taşıyan floem canlıdır.',sekil=SK)

# ---- 02 · meristem · kolay · olumsuz
mer=[('Büyük bir merkezî koful bulundurur ve sitoplazması, bölünmeyen olgun hücrelere göre daha azdır.',False,'meristem hücrelerinde koful küçüktür, sitoplazma ise yoğundur.'),
     ('Hücre çeperleri incedir ve hücreler arasında boşluk yok denecek kadar azdır.',True,'meristem hücreleri sıkı dizilmiş, ince çeperli hücrelerdir.'),
     ('Çekirdekleri büyüktür ve sitoplazmaları yoğundur.',True,'meristem hücreleri etkin metabolizma gösterir; çekirdek büyük, sitoplazma yoğundur.'),
     ('Mitoz bölünme geçirerek yeni hücreler oluşturabilir.',True,'meristem hücreleri mitozla bölünerek bitkinin büyümesini sağlar.'),
     ('Bölünmeyle oluşan hücrelerin bir kısmı farklılaşarak kalıcı dokulara katılır.',True,'meristem hücrelerinden oluşan yeni hücreler farklılaşarak parankima, epidermis, iletim dokusu gibi kalıcı dokuları oluşturur.')]
o=tek(mer,False)
Q('02','doku','kolay','düz','Meristem','Uç meristem hücrelerinin özelliklerini bilir ve olgun hücre özellikleriyle karıştırmaz.',
  'Meristem hücreleri küçük, ince çeperli, yoğun sitoplazmalı ve bölünme yeteneğindedir; kofulları küçüktür.','Meristem hücresini büyük kofullu olgun parankima hücresiyle karıştırmak.','meristem hücrelerinin özellikleri',
  [A('Meristemin özelliğini hatırla','Meristem hücreleri sürekli bölünür; bu yüzden çekirdekleri büyük, sitoplazmaları yoğun, çeperleri ince ve kofulları küçüktür.','Meristem → bölünme yeteneği yüksek, farklılaşmamış'),
   A('Her ifadeyi bu özelliklerle karşılaştır','Sıkı dizilim, ince çeper, mitoz ve farklılaşma meristemle uyumludur. Büyük koful ise genişleyip olgunlaşmış hücrelerin özelliğidir.','Büyük merkezî koful → olgun hücre özelliği'),
   A('Uyuşmayan ifadeyi seç','Meristem için söylenemeyecek tek ifade büyük koful ve az sitoplazma içeren ifadedir.','Cevap: büyük kofullu hücre ifadesi')],
  metin='Bitkilerde büyüme, bölünme yeteneğini koruyan meristem dokuları sayesinde gerçekleşir. Kök ve gövdenin uç kısımlarında bulunan uç (apikal) meristem hücreleri mikroskopta incelendiğinde bazı ortak özellikler gözlenir.\nBuna göre, uç meristem hücreleriyle ilgili aşağıdakilerden hangisi söylenemez?',
  istenen='Meristem hücreleri için doğru olmayan ifade.',ip=['Meristem hücrelerinin sürekli bölünmesi için hangi hücre özelliklerine gerek duyulduğunu düşün.'],
  bilgi=[B('Bitkilerde dokular','bitkilerde dokular bölünebilen (meristem) ve bölünme yeteneğini yitirmiş (kalıcı) dokular olarak ikiye ayrılır; kalıcı dokular meristemden farklılaşarak oluşur'),
         B('Meristemin yeri','bitkilerde kök ve gövde uçlarında uç meristem, kök ve gövdenin yanlarında yanal meristem bulunur')],
  puf='Bölünen hücre küçük, ince çeperli ve yoğun sitoplazmalıdır; büyük kofullu hücre olgunlaşmıştır.',**o)

# ---- 03 · yaprak kesiti · kolay
SK=f_yaprak()
Q('03','yapi','kolay','şekilli','Yaprak yapısı','Yaprak enine kesitinde dokuları tanıyıp fotosentezin en yoğun olduğu dokuyu belirler.',
  'Palizat parankiması üst epidermisin hemen altında, sık dizilmiş silindirik hücrelerden oluşur ve en çok kloroplast içerir.','Sünger parankimasını ya da epidermisi fotosentezin ana yeri saymak.','yaprak kesiti, palizat',
  [A('Katmanları tanı','Üstte ve altta tek sıra epidermis, üst epidermisin altında sık dizili silindirik hücreler, onların altında aralıklı yuvarlak hücreler ve ortada iletim demeti bulunur.','I: üst epidermis · II: sünger · III: iletim demeti · IV: alt epidermis · V: palizat'),
   A('Kloroplast dağılımını hatırla','Işık yapraktaki üst yüzeyden girer; ışığı ilk alan ve sık dizilmiş silindirik parankima hücrelerinde en çok kloroplast bulunur.','En çok kloroplast → palizat parankiması'),
   A('Numarayı seç','Silindirik hücreleri üst epidermisin hemen altında sıralıdır.','Cevap: V')],
  metin='Şekilde, bir yaprağın enine kesiti şematik olarak gösterilmiştir. Kesitte epidermis hücreleri, mezofil dokusunu oluşturan hücre katmanları, iletim demeti ve alt yüzeyde bir stoma görülmektedir.\nBuna göre, numaralı yapılardan hangisinde hücre başına düşen kloroplast sayısı ve fotosentez hızı en yüksektir?',
  dogru='V',sira=['I','II','III','IV','V'],
  yan=[('I','I numaralı yapı üst epidermistir; ışığı geçirir ve yaprağı korur, hücrelerinde genellikle kloroplast bulunmaz.','bilgi'),
       ('II','II numaralı yapı sünger parankimasıdır; kloroplast içerir ancak palizat hücrelerine göre daha az ve aralıklı dizilidir.','bilgi'),
       ('III','III numaralı yapı iletim demetidir; su ve organik madde taşır, fotosentezin ana yeri değildir.','bilgi'),
       ('IV','IV numaralı yapı alt epidermistir; stoma bekçi hücreleri dışında kloroplast taşımaz.','bilgi')],
  istenen='Kloroplast yoğunluğu en fazla olan dokunun numarası.',ip=['Işığın yaprağa hangi yüzeyden girdiğini ve hücre dizilişinin ışık yakalamaya nasıl uyum sağladığını düşün.'],
  bilgi=[B('Yaprağın yapısı','yaprak, epidermis ile örtülü olup içinde mezofil (palizat ve sünger parankiması) ve iletim demetleri bulunur; alt epidermiste genellikle stomalar yer alır'),
         B('Fotosentez ve kloroplast','fotosentez, kloroplast taşıyan canlı hücrelerde gerçekleşir ve ışık enerjisinin kimyasal enerjiye dönüşümünü sağlar')],
  puf='Fotosentez en çok ışığı ilk alan, sık dizilmiş ve kloroplastça zengin palizat parankimasında olur.',sekil=SK)

# ---- 04 · doku tablosu · orta · öncüllü
SK=tablo_svg(['Özellik','X','Y','Z'],[['Olgun hâlde canlı protoplast','+','+','−'],['Çeperde lignin birikimi','−','−','+'],['Kloroplast bulundurabilme','+','+','−'],['Çeperin köşelerde selülozla kalınlaşması','−','+','−']])
d4={'I':(True,'X dokusu parankimadır; parankima hücreleri olgun olsa da canlıdır ve gerektiğinde yeniden bölünebilir'),
    'II':(True,'Y dokusu kollenkimadır; çeperi köşelerde kalınlaşmış canlı hücreleri genç ve uzayan organlarda esnek destek sağlar'),
    'III':(False,'Z dokusu sklerenkimadır; olgun hücreleri ligninli kalın çeper taşır ve cansızdır')}
o=onc_t(d4,1)
Q('04','doku','orta','tablo','Destek ve temel dokular','Tablodaki özelliklerden parankima, kollenkima ve sklerenkimayı ayırt ederek her dokuyla ilgili yargıları değerlendirir.',
  'Canlılık, lignin ve çeper kalınlaşma biçimi parankima, kollenkima ve sklerenkimayı birbirinden ayırır.','Kollenkimayı ligninli sanmak; sklerenkimayı canlı hücreli sanmak.','doku özellik tablosu',
  [A('Sütunları dokularla eşleştir','Yalnız Z olgunlaşınca cansızdır ve ligninli çeper taşır; bu sklerenkimadır. Çeperi köşelerde kalınlaşan Y kollenkimadır. Geriye kalan X parankimadır.','X: parankima · Y: kollenkima · Z: sklerenkima'),
   A('I. yargıyı değerlendir','Parankima hücreleri canlıdır, olgunlaşsa da bölünme yeteneğini koruyabilir.',oy({'I':d4['I']})),
   A('II. yargıyı değerlendir','Kollenkima, genç gövde ve yaprak sapı gibi uzayan kısımlarda esnek destek sağlar.',oy({'II':d4['II']})),
   A('III. yargıyı değerlendir','Sklerenkima olgunlaşınca cansızdır; çeperinde lignin bulunur. Yargı Z için canlı protoplast iddia ettiğinden yanlıştır.',oy({'III':d4['III']}))],
  metin='Tabloda, bir bitkideki parankima, kollenkima ve sklerenkima dokularına ait X, Y ve Z hücrelerinin bazı özellikleri verilmiştir (+: var, −: yok). Dokuların hangi harfle gösterildiği belirtilmemiştir.\nI. X dokusunun hücreleri, olgunlaştıktan sonra yeniden bölünebilir.\nII. Y dokusu, bitkinin genç ve uzayan kısımlarında esnek destek sağlayabilir.\nIII. Z dokusunun olgun hücreleri canlı protoplast taşır.\nBuna göre bu yargılardan hangileri doğrudur?',
  istenen='Doğru olan yargıların belirlenmesi.',ip=['Tablodaki canlılık ve lignin satırlarına bakarak önce hangi sütunun hangi dokuya ait olduğunu belirle.'],
  bilgi=[B('Temel ve destek dokuları','parankima, kollenkima ve sklerenkima bitkilerde temel ve destek dokularıdır; bu dokuların hücreleri çeper yapısı ve canlılık bakımından birbirinden ayrılır'),
         B('Lignin','bitki hücre çeperlerinde birikebilen, çeperi sertleştiren ve geçirgenliğini azaltan bir maddedir')],
  puf='Tablodaki en ayırt edici satır lignindir: ligninli çeperli olgun hücre sklerenkimadır ve cansızdır.',sekil=SK,**o)

# ---- 05 · gövde kesiti · orta · öncüllü
SK=f_govde()
d5={'I':(True,'iletim demetleri halka biçiminde dizilmiş gövde çift çenekli bitkilere aittir'),
    'II':(False,'iletim demetleri dağınık olan gövde tek çenekli bitkiye aittir ve bu bitkinin tohumunda tek çenek yaprağı bulunur'),
    'III':(True,'çift çenekli bitkinin iletim demetinde ksilem ile floem arasında bölünebilen kambiyum bulunur; tek çenekli bitkide kambiyum yoktur')}
o=onc_t(d5,3)
Q('05','yapi','orta','öncüllü','Gövde yapısı','Tek ve çift çenekli bitki gövdelerinin kesitlerini iletim demeti dizilişine göre ayırt eder.',
  'Çift çenekli gövdede iletim demetleri halkada dizilir ve kambiyum bulunur; tek çenekli gövdede demetler dağınıktır, kambiyum yoktur.','Dağınık demetli gövdeyi çift çenekli sanmak; tek çenekli bitkide kalınlaşma beklemek.','gövde kesitleri, çenek sayısı',
  [A('Kesitleri tanı','A kesitinde iletim demetleri halka biçiminde, B kesitinde ise gövdeye dağınık hâlde dizilmiştir.','A: halka dizilim · B: dağınık dizilim'),
   A('Çenek sayısıyla eşleştir','Halka biçimli dizilim çift çenekli, dağınık dizilim tek çenekli bitkilerin özelliğidir. B bitkisinin tohumunda tek çenek yaprağı bulunur.',oy({'I':d5['I'],'II':d5['II']})),
   A('Kambiyumu değerlendir','Çift çenekli gövdede ksilem ile floem arasında bölünebilen kambiyum bulunur, tek çenekli gövdede bulunmaz.',oy({'III':d5['III']}))],
  metin='Şekilde, çiçekli iki bitkiye ait gövdelerin enine kesitleri şematik olarak verilmiştir. Kesitlerde iletim demetlerindeki ksilem koyu, floem açık renkli yapılarla gösterilmiş; demet içindeki ince çizgi, ksilem ile floem arasındaki bölünebilen dokuyu göstermektedir.\nI. A kesiti, çift çenekli bir bitkiye aittir.\nII. B kesitindeki bitkinin tohumunda iki çenek yaprağı bulunur.\nIII. A kesitindeki bitkinin iletim demetlerinde, ksilem ile floem arasında bölünme yeteneğini koruyan kambiyum bulunur; B kesitindeki bitkinin demetlerinde bulunmaz.\nBuna göre bu yargılardan hangileri doğrudur?',
  istenen='Doğru olan yargıların belirlenmesi.',ip=['İletim demetlerinin gövde kesitindeki dizilişini, çenek sayısı ve kambiyum ile ilişkilendir.'],
  bilgi=[B('Çenek sayısı','çiçekli bitkiler tohumlarındaki çenek yaprağı sayısına göre tek çenekli ve çift çenekli olarak ikiye ayrılır; bu ayrım kök, gövde ve yaprak yapısına da yansır'),
         B('Kambiyum','ksilem ile floem arasında yer alan, bölünme yeteneğini koruyan meristematik dokudur ve kalınlaşmayı sağlar')],
  puf='Halka dizilimli demet ve kambiyum çift çenekli, dağınık demet tek çenekli gövdeyi gösterir.',sekil=SK,**o)

# ---- 06 · stoma · orta · öncüllü
SK=f_stoma()
d6={'I':(False,'K⁺ girişi bekçi hücrelerinin ozmotik basıncını artırır, su girişini hızlandırır ve turgoru yükseltir'),
    'II':(False,'bekçi hücrelerinin stoma aralığına bakan çeperi daha kalındır; turgor artınca hücreler dışa doğru bükülür ve stoma açılır'),
    'III':(True,'bekçi hücreleri, komşu epidermis hücrelerinden farklı olarak kloroplast taşır')}
o=onc_t(d6,2)
Q('06','terleme','orta','öncüllü','Stoma hareketi','Bekçi hücrelerine iyon ve su girişiyle stomanın açılmasını yorumlar.',
  'Bekçi hücrelerine K⁺ girişi ozmotik basıncı artırır, su girişi turgoru yükseltir; kalın iç çeper nedeniyle hücreler dışa bükülür ve stoma açılır.','K⁺ girişinin turgoru düşürdüğünü sanmak; iç çeperi ince sanmak.','stoma açılması',
  [A('Şekildeki olayı yorumla','Şekilde komşu epidermis hücrelerinden bekçi hücrelerine K⁺ ve su girişi, stomanın açık olduğu durumla birlikte gösterilmiştir.','K⁺ ve su girişi → stoma açık'),
   A('I. ve II. yargıları değerlendir','K⁺ girişi ozmotik basıncı artırır ve su girişini hızlandırır, turgor yükselir. Stoma aralığına bakan çeper kalındır; bu yüzden hücreler dışa bükülür ve stoma açılır.',oy({'I':d6['I'],'II':d6['II']})),
   A('III. yargıyı değerlendir','Epidermisin diğer hücrelerinde kloroplast yoktur, bekçi hücreleri ise kloroplast taşır ve ışıkta fotosentez yapabilir.',oy({'III':d6['III']}))],
  metin='Şekilde, ışıklı ortamda açık durumdaki bir stoma ile komşu epidermis hücrelerinden bekçi hücrelerine doğru K⁺ ve su hareketi gösterilmiştir.\nI. Bekçi hücrelerine K⁺ girişi, bu hücrelerdeki su miktarını azaltarak turgor basıncını düşürür.\nII. Bekçi hücrelerinin stoma aralığına bakan çeperi, diğer çeperlerine göre daha ince olduğu için stoma açılır.\nIII. Bekçi hücreleri, komşu epidermis hücrelerinden farklı olarak kloroplast taşır.\nBuna göre bu yargılardan hangileri doğrudur?',
  istenen='Doğru olan yargıların belirlenmesi.',ip=['Şekildeki iyon ve su hareketinin bekçi hücrelerinin ozmotik ve turgor durumunu nasıl değiştirdiğini sırayla düşün.'],
  bilgi=[B('Stoma ve bekçi hücreleri','stoma, iki bekçi hücresinin çevrelediği gaz alışverişi açıklığıdır; bekçi hücrelerinin turgor basıncındaki değişim stomanın açılıp kapanmasını sağlar'),
         B('Ozmoz ve turgor','hücreye su girişi hücre içi basıncı (turgor) artırır; çözünen madde derişimi yüksek olan hücre suyu çeker')],
  puf='Bekçi hücresine K⁺ girerse su da girer, turgor artar ve kalın iç çeper nedeniyle stoma açılır.',sekil=SK,**o)

# ---- 07 · tüp deneyi · orta · olumsuz
SK=f_tup()
d7=[('Bu bitkinin yaprağının üst yüzeyinde stoma bulunmaz.',False,'üst yüzeyi kapatılan L ve N tüplerinde de su kaybı olduğundan bu bilgi deneyden çıkarılamaz.'),
    ('Terleyle kaybedilen suyun büyük bölümü yaprağın alt yüzeyinden olur.',True,'alt yüzeyi kapatılan L tüpünde su kaybı 9 mL’den 2 mL’ye düşmüştür.'),
    ('L ve N tüplerinde su kaybı, K tüpündekinden azdır.',True,'L’de 2 mL, N’de 1 mL, K’de ise 9 mL su kaybolmuştur.'),
    ('N tüpünde de su kaybı olmuştur.',True,'N tüpünden 1 mL su kaybolmuştur.'),
    ('Vazelin sürülmeyen K tüpü, diğer tüplerle karşılaştırma yapmaya olanak sağlayan kontrol düzeneğidir.',True,'K tüpünde yüzeylere işlem yapılmamıştır ve diğer tüpler onunla kıyaslanır.')]
assert KAYIP['K']-KAYIP['M']==UST and KAYIP['K']-KAYIP['L']==ALT and ALT>UST*3
o=tek(d7,False)
Q('07','terleme','orta','şekilli','Terleme deneyi','Yaprak yüzeylerinin kapatıldığı deney sonuçlarından terlemenin yaprağın hangi yüzeyinde yoğun olduğunu yorumlar.',
  'Yüzeyi kapatılan tüplerdeki su kaybı farkı, o yüzeyden olan terlemeyi gösterir; deney sonucundan yalnız verilerle desteklenen çıkarımlar yapılabilir.','Su kaybının azalmasından stomanın hiç bulunmadığı sonucunu çıkarmak.','vazelinli yaprak deneyi',
  [A('Deney düzeneğini incele','Dört tüpte eşit hacimde su vardır; suyun yüzeyi yağla örtüldüğünden su kaybı yalnız bitkiden olur. Tüplerde kaybolan su miktarları verilmiştir.','K: 9 · L: 2 · M: 8 · N: 1 (mL)'),
   A('Yüzey katkılarını hesapla','Üst yüzey katkısı K−M kadar, alt yüzey katkısı K−L kadardır.','Üst: 9−8 = 1 · Alt: 9−2 = 7'),
   A('İfadeleri verilere uydur','Alt yüzeyden kayıp çok, üst yüzeyden az; N’de de kayıp vardır. Üst yüzeyde stoma olmadığı ise verilerle kanıtlanamaz.','Üst yüzeyde stoma yok → deneyden söylenemez')],
  metin='Aynı türden bitkilerin eşit yaprak sayılı dallarından alınan dört parça, eşit hacimde su içeren K, L, M ve N tüplerine yerleştirilmiş, suların yüzeyi ince bir yağ tabakasıyla örtülmüştür. K’de yaprakların hiçbir yüzeyine işlem yapılmamış; L’de alt yüzeyler, M’de üst yüzeyler, N’de her iki yüzey vazelinle kaplanmıştır. Aynı koşullarda 24 saat sonra tüplerden kaybolan su miktarları şekilde verilmiştir.\nBuna göre, bu deneyle ilgili aşağıdakilerden hangisi söylenemez?',
  istenen='Deney sonuçlarından çıkarılamayan ifade.',ip=['Hangi tüpler karşılaştırıldığında her yüzeyin su kaybına katkısının bulunabileceğini düşün; yalnızca verilerle desteklenen ifadeleri ele.'],
  bilgi=[B('Terleme','bitkinin su buharını yaprak yüzeyinden atmasıdır; büyük bölümü stomalardan, az bir bölümü kutikula yoluyla gerçekleşir'),
         B('Deney tasarımı','kontrol grubu, işlem uygulanmayan gruptur; diğer gruplar onunla karşılaştırılarak değişkenin etkisi belirlenir')],
  puf='Deneyde ancak karşılaştırmayla bulunabilen çıkarım doğrudur; verinin ötesindeki iddia (stoma yoktur) söylenemez.',sekil=SK,**o)

# ---- 08 · su dengesi grafiği · zor
SK=f_denge()
KAYBOL=-min(DEN); assert KAYBOL==96 and -DEN[4]==36 and -DEN[5]==69 and -DEN[6]==90 and -DEN[8]==93
Q('08','tasima','zor','grafik','Su alımı ve terleme','Su alım ve terleme hızı grafiklerinden alan hesaplayarak dokulardaki su miktarının değişimini bulur.',
  'Dokulardaki su miktarı, alım ve terleme hızları farkının zaman içindeki toplamına (eğriler arası alana) bağlıdır; en düşük değer, farkın işaret değiştirdiği anda olur.','Yalnız bir andaki hız farkını ya da gün sonu değerini en büyük azalma sanmak.','su dengesi grafiği',
  [A('Grafiği oku','Terleme hızı gün içinde artıp azalır; su alım hızı terlemeyi gecikmeli izler. Değerler 3 saatlik aralıklarla okunur.','Terleme ve alım: 3 saatte bir okunan değerler'),
   A('Her aralıkta net değişimi hesapla','Her 3 saatlik aralıkta (alım hızı ortalaması − terleme hızı ortalaması) × 3 saat net su değişimini verir.','9: −9 · 12: −27 · 15: −33 · 18: −21 · 21: −6 (mL)'),
   A('Birikimi izle','Net değişimler eksi oldukça su azalır; eğriler 21. saatte kesişince azalma biter. En düşük miktar bu ana kadar toplanan değerdir.','−9 −27 −33 −21 −6 = −96 mL'),
   A('Sonucu yaz','Gün başına göre en büyük azalma 96 mL’dir.','Cevap: 96')],
  metin='Şekilde, açık havada yetişen bir bitkide 24 saat boyunca (0: gece yarısı) terleme hızı ile köklerin su alım hızı gösterilmiştir; hızlar 3 saatlik aralıklarla okunup her aralıkta doğrusal değiştiği kabul edilecektir. Dokulardaki su miktarındaki değişimin yalnızca bu iki hıza bağlı olduğu kabul edilmektedir.\nBuna göre, gün boyunca bitkinin dokularındaki su miktarı, gün başındaki değerine göre en fazla kaç mL azalır?',
  dogru=KAYBOL,
  yan=[(-DEN[4],'12. saate kadar olan birikim hesaplanmış; oysa su miktarı terleme alımı aştığı sürece 12. saatten sonra da azalmaya devam eder.','dikkat'),
       (-DEN[5],'15. saate (terlemenin en yüksek olduğu ana) kadar olan birikim alınmış; azalma bu saatten sonra da sürer.','bilgi'),
       (-DEN[6],'18. saate (alım hızının en yüksek olduğu ana) kadar olan birikim alınmış; alım hâlâ terlemenin altındadır ve azalma sürer.','bilgi'),
       (-DEN[8],'Gün sonundaki (24. saat) net azalma alınmış; oysa 21. saatten sonra alım terlemeyi aşar ve su miktarı kısmen yeniden artar, en büyük azalma 21. saatte olur.','islem')],
  istenen='Gün başına göre su miktarındaki en büyük azalma (mL).',ip=['Her 3 saatlik aralıkta iki hızın ortalamasını karşılaştır ve net değişimi biriktirerek izle.'],
  bilgi=[B('Bitkide su dengesi','bitkinin su miktarı, köklerle alınan su ile yapraklardan terlemeyle kaybedilen suyun farkıyla belirlenir'),
         B('Terleme ve su alımı','terleme yapraklardan su buharı kaybıdır, su alımı ise köklerin topraktan su almasıdır; ikisinin hızı gün boyunca değişir')],
  puf='Hız grafiklerinde miktar değişimi, eğri altındaki alanların farkıyla bulunur.',sekil=SK)

# ---- 09 · floem şeması · orta · olumsuz
SK=f_floem()
d9=[('I numaralı yapıda üretilen şeker, arkadaş hücreleri yardımıyla II numaralı yapıya aktarıldığında II’deki ozmotik basınç artar.',True,'şeker yüklemesi kalburlu borunun ozmotik basıncını yükseltir.'),
    ('I numaralı yapıda üretilen şekerin II numaralı yapıya taşınması difüzyonla olduğundan bu taşınmada ATP harcanmaz.',False,'şekerin floeme yüklenmesi arkadaş hücreleri aracılığıyla aktif taşımayla yapılır ve ATP harcanır.'),
    ('III numaralı yapıdan II numaralı yapıya su girişi, II’deki basıncı artırarak özsuyun havuza doğru akmasına katkı sağlar.',True,'kalburlu boruya su girişi basıncı yükseltir ve kütlesel akışı sürdürür.'),
    ('IV numaralı yapıda şeker II numaralı yapıdan boşaltıldığında, II’deki su ozmozla III numaralı yapıya geri geçebilir.',True,'şeker havuzda boşaltılınca ozmotik basınç düşer ve su ksileme döner.'),
    ('II numaralı yapıdaki özsuyun akış yönü, kaynak ve havuz olan organların konumuna bağlıdır.',True,'floemde akış kaynaktan havuza doğrudur ve organların görevi değişirse yön de değişir.')]
d9=[d9[0],d9[1]]+d9[2:]
Q('09','tasima','orta','şekilli','Floemde taşınma','Kaynak–havuz arasındaki organik madde taşınmasını basınç akışı açısından değerlendirir.',
  'Kaynakta şeker floeme aktif yüklenir, ozmotik basınç artar, ksilemden su girer; havuzda şeker boşaltılır ve su ksileme döner.','Floeme şeker yüklemesini difüzyon sanmak.','floem basınç akışı',
  [A('Şemayı oku','I yaprakta şeker üretilen kaynaktır, II floemin kalburlu borusudur, III ksilemdir, IV ise şekerin kullanıldığı havuzdur.','I: kaynak · II: floem · III: ksilem · IV: havuz'),
   A('Yükleme ve basınç artışını incele','Şeker arkadaş hücreleriyle floeme aktif taşımayla yüklenir. Ozmotik basınç artınca ksilemden su girer, basınç yükselir ve özsu havuza doğru akar.','Yükleme: aktif taşıma (ATP harcanır)'),
   A('Havuzdaki olayı incele','Havuzda şeker boşaltılınca ozmotik basınç düşer ve su ksileme geri döner. Akış yönü kaynak ile havuzun konumuna göredir.','Su: floem → ksilem'),
   A('Yanlış ifadeyi seç','ATP harcanmadığını söyleyen ifade, yüklemenin difüzyonla olduğunu varsaydığından yanlıştır.','Cevap: difüzyon iddiası')],
  metin='Şekilde, bir bitkideki kaynak organ olan yaprak ile havuz organ arasında floem yoluyla şeker taşınması şematik olarak gösterilmiştir. Yaprakta fotosentezle üretilen şeker, ok yönünde kalburlu boru hücrelerinden geçerek havuza ulaşmaktadır.\nBuna göre, numaralı yapılarla ilgili aşağıdakilerden hangisi yanlıştır?',
  istenen='Yanlış olan ifade.',ip=['Şemadaki her numaralı yapının görevini belirle ve ifadeleri sırayla bu görevlerle karşılaştır.'],
  bilgi=[B('Kaynak ve havuz','şeker üretilen ya da depodan salınan organ kaynak, şekerin kullanıldığı ya da depolandığı organ havuzdur; bir organ koşullara göre biri ya da diğeri olabilir'),
         B('Floem ve ksilem','floem canlı hücrelerle organik madde, ksilem cansız hücrelerle su ve mineral taşır')],
  puf='Floemde yükleme aktif taşımayla olur; sonrasında su girişi basıncı artırır ve akışı sürdürür.',**tek([d9[0],d9[1],d9[2],d9[3],d9[4]],False),sekil=SK)

# ---- 10 · toprak çözeltisi tablosu · orta · öncüllü
SK=tablo_svg(['Saksı','Toprak çözeltisi (mol/L)','Kök tüyü hücre sıvısı (mol/L)'],[['K','0,10','0,30'],['L','0,30','0,30'],['M','0,50','0,30']])
d10={'I':(True,'toprak çözeltisi hücre sıvısından seyrek olduğundan su ozmozla kök tüyü hücresine girer'),
     'II':(False,'mineral iyonları derişim farkına karşın aktif taşımayla ATP harcanarak hücreye alınabilir; ozmotik denge iyon girişini durdurmaz'),
     'III':(True,'toprak çözeltisi hücre sıvısından derişik olduğundan su hücreden çıkar ve turgor basıncı düşer')}
o=onc_t(d10,4)
Q('10','tasima','orta','tablo','Kökte su ve mineral alımı','Toprak çözeltisi ile kök tüyü hücre sıvısının derişimine göre su ve mineral alımını yorumlar.',
  'Su derişimi çok olandan az olana ozmozla geçer; mineral iyonlarının alımı ise derişim farkına karşın aktif taşımayla sürebilir.','Ozmotik dengede mineral alımının da durduğunu sanmak.','kök tüyü ozmoz tablosu',
  [A('Su geçiş yönünü belirle','Su, derişimi düşük (su oranı çok) çözeltiden derişimi yüksek çözeltiye geçer. K’de toprak çözeltisi seyrektir, M’de derişiktir, L’de ikisi eşittir.','K: toprak < hücre · L: eşit · M: toprak > hücre'),
   A('I. ve III. yargıları değerlendir','K’de su kök tüyüne girer. M’de su hücreden toprağa çıkar ve turgor düşer.',oy({'I':d10['I'],'III':d10['III']})),
   A('II. yargıyı değerlendir','Ozmotik denge suyun net geçişini durdurur. Mineral iyonları ise taşıyıcı proteinlerle ATP harcanarak alınmaya devam eder.',oy({'II':d10['II']}))],
  metin='Aynı türden ve eşit büyüklükteki üç fide, K, L ve M saksılarına dikilmiştir. Saksılardaki toprak çözeltileri yalnızca suda çözünmüş mineral tuzlardan oluşmaktadır ve kök tüyü hücrelerinin zarı su için geçirgendir. Tabloda her saksının toprak çözeltisi ile fidelerin kök tüyü hücre sıvısı derişimleri verilmiştir.\nI. K saksısındaki fidenin kök tüyü hücrelerine ozmozla su girer.\nII. L saksısındaki fidenin kök tüyü hücrelerine mineral iyonlarının girişi tamamen durur.\nIII. M saksısındaki fidenin kök tüyü hücreleri su kaybeder ve turgor basınçları azalır.\nBuna göre bu yargılardan hangileri doğrudur?',
  istenen='Doğru olan yargıların belirlenmesi.',ip=['Tablodaki derişimleri karşılaştırarak her saksıda suyun hangi yönde ilerleyeceğini bul; ardından mineral iyonlarının zardan geçiş yolunu düşün.'],
  bilgi=[B('Ozmoz','suyun yarı geçirgen zardan, çözünen derişiminin düşük olduğu ortamdan yüksek olduğu ortama geçmesidir ve enerji gerektirmez'),
         B('Aktif taşıma','taşıyıcı proteinler ve ATP kullanılarak yapılan madde geçişidir; çoğunlukla derişimin az olduğu yerden çok olduğu yere gerçekleşir')],
  puf='Su derişim farkına göre ozmozla, iyonlar ise ATP kullanarak aktif taşımayla alınır; ozmotik denge iyon alımını bitirmez.',sekil=SK,**o)

# ---- 11 · koleoptil · orta
SK=f_koleoptil()
GR={'A':False,'B':False,'C':True,'D':True}      # ışığa doğru eğilir mi
assert [k for k,v in GR.items() if v]==['C','D']
Q('11','hareket','orta','şekilli','Fototropizma','Koleoptil ucunun ışığı algılayıp eğilmeyi başlattığını deney düzeneğinden çıkarır.',
  'Işığı koleoptil ucu algılar; oksin gölge tarafına kayar ve o taraf daha hızlı uzar. Uç yoksa ya da ışık almıyorsa eğilme olmaz; uç ışık alıyorsa altı örtülü olsa da eğilir.','Eğilmenin yalnız büyüyen bölgedeki ışıktan kaynaklandığını sanmak.','koleoptil ve tek yönlü ışık',
  [A('Düzenekleri incele','A’nın ucu kesilmiştir, B’nin ucu ışık geçirmeyen başlıkla, C’nin ucu saydam başlıkla örtülüdür. D’de ise uç açıkta, alt bölge ışık geçirmeyen kılıfla örtülüdür.','A: uç yok · B: uç opak örtülü · C: uç saydam örtülü · D: uç açık, alt örtülü'),
   A('Uç ışığı alıyor mu?','Işığı koleoptilin ucu algılar. Ucu kesilen ya da ucu opak örtülen fidede uyarı alınmaz; saydam örtü ışığı geçirdiğinden uç uyarılır.','C ve D uç ışık alıyor'),
   A('Eğilmeyi sonuçlandır','Uç ışığı alınca oksin gölgeli tarafa kayar; gölge tarafı hızlı uzar ve fide ışığa doğru eğilir. Alt bölgenin örtülü olması bunu değiştirmez.','Eğilen fideler: C ve D')],
  metin='Aynı türden, eşit boyda dört koleoptil fidesi sağdan gelen tek yönlü ışığa maruz bırakılmıştır. A fidesinin ucu kesilmiştir. B fidesinin ucu ışık geçirmeyen, C fidesinin ucu ışığı geçiren (saydam) bir başlıkla örtülmüştür. D fidesinde ise uç açıkta bırakılmış, alt bölge ışık geçirmeyen bir kılıfla örtülmüştür. Düzenek şekilde gösterilmiştir.\nBuna göre bir süre sonra bu fidelerden hangileri ışık kaynağına doğru eğilir?',
  dogru='C ve D',sira=['Yalnız D','B ve C','C ve D','B, C ve D','A, C ve D'],
  yan=[('Yalnız D','Ucu açık olan tek fide D sanılmış; C’de saydam örtünün ışığı geçirdiği ve ucun uyarıldığı gözden kaçırılmıştır.','dikkat'),
       ('B ve C','Ucu örtülü fidelerin eğileceği sanılmış; B’de örtü ışığı geçirmediği için uç uyarılmaz, D’de ise uç ışık aldığından fide eğilir.','bilgi'),
       ('B, C ve D','B’nin ucu opak örtüyle ışıktan korunduğu hâlde eğileceği sanılmıştır; uç uyarılmayınca oksin dağılımı değişmez.','bilgi'),
       ('A, C ve D','Ucu kesilen A fidesinin de eğileceği sanılmış; uç ışığı algılayan ve oksin üreten bölge olduğundan A’da eğilme gözlenmez.','bilgi')],
  istenen='Işık kaynağına doğru eğilen fidelerin belirlenmesi.',ip=['Koleoptilde ışığı hangi bölgenin algıladığını düşün ve her düzenekte o bölgenin ışık alıp almadığına bak.'],
  bilgi=[B('Tropizma','bitkilerin uyarıcının yönüne bağlı olarak büyüyerek yaptığı yönelim hareketidir; bu hareket hormonların dağılımındaki farklılıkla gerçekleşir'),
         B('Oksin','bitkilerde hücre uzamasını uyaran hormondur; eşit olmayan dağılımı organın bir tarafının diğerinden daha hızlı uzamasına neden olur')],
  puf='Işığı koleoptilin ucu algılar: ucu ışık alan fide eğilir, ucu kesilen ya da opak örtülen fide eğilmez.',sekil=SK)

# ---- 12 · oksin grafiği · zor
SK=f_oksin()
assert GOV[ALTD]-GOV[USTD]==50 and KOK[USTD]-KOK[ALTD]==100
Q('12','hormon','zor','grafik','Oksin ve yerçekimi','Kök ve gövdenin oksin derişimine verdiği farklı yanıtları yerçekimi tropizmiyle birleştirir.',
  'Aynı oksin derişimi gövdede uzamayı uyarırken kökte engelleyebilir; hızlı uzayan yüzeyin karşı tarafa doğru organ bükülür.','Oksinin her organda uzamayı artırdığını sanmak.','oksin eğrisi, geotropizma',
  [A('Gövde için değerleri oku','Gövdede 10⁻⁶ M derişimde uzama kontrole göre yaklaşık %50 artar, 10⁻⁹ M derişimde değişmez. Alt yüzey daha hızlı uzar.','Gövde: alt +50 · üst 0'),
   A('Kök için değerleri oku','Kökte 10⁻⁶ M derişim uzamayı yaklaşık %90 azaltır, 10⁻⁹ M derişim hafifçe artırır. Üst yüzey daha hızlı uzar.','Kök: alt −90 · üst +10'),
   A('Bükülme yönünü bul','Organ, daha yavaş uzayan yüzeye doğru bükülür. Gövdede alt yüzey hızlı uzadığından uç yukarı kalkar. Kökte alt yüzey yavaş uzadığından uç aşağı döner.','Gövde: yukarı · Kök: aşağı')],
  metin='Şekildeki grafik, aynı bitkinin gövde ve kökünde farklı oksin derişimlerinin uzama hızını, oksin uygulanmayan kontrole göre nasıl değiştirdiğini göstermektedir (kontrol: 0). Yatay konumda tutulan bir fidede yerçekiminin etkisiyle oksin alt yüzeyde birikmiş; hem gövdede hem kökte alt yüzeydeki oksin derişimi 10⁻⁶ M, üst yüzeydeki derişim 10⁻⁹ M olmuştur.\nBuna göre bu fidenin gövdesi ve kökü zamanla nasıl bükülür?',
  dogru='Gövde yukarı, kök aşağı yönde bükülür.',sira=yerles('Gövde yukarı, kök aşağı yönde bükülür.',['Gövde aşağı, kök yukarı yönde bükülür.','Gövde yukarı, kök yukarı yönde bükülür.','Gövde aşağı, kök aşağı yönde bükülür.','Gövde ve kök bükülmeden düz uzar.'],0),
  yan=[('Gövde aşağı, kök yukarı yönde bükülür.','Bükülme yönü, hızlı uzayan yüzeye doğru sanılmış. Oysa organ daha yavaş uzayan yüzeye doğru bükülür: gövdede alt yüzey hızlı uzadığından gövde yukarı döner.','bilgi'),
       ('Gövde yukarı, kök yukarı yönde bükülür.','Yüksek oksin derişiminin kökte de uzamayı artırdığı sanılmış. Oysa 10⁻⁶ M derişim kökte uzamayı yaklaşık %90 azaltır ve kök aşağı döner.','bilgi'),
       ('Gövde aşağı, kök aşağı yönde bükülür.','Yüksek derişimin her iki organda uzamayı engellediği sanılmış. Oysa gövdede alt yüzeydeki 10⁻⁶ M derişim uzamayı yaklaşık %50 artırır, bu yüzden gövde yukarı döner.','bilgi'),
       ('Gövde ve kök bükülmeden düz uzar.','Alt ve üst yüzeylerin eşit uzadığı sanılmış. Oysa iki yüzeydeki derişim farkı her iki organda da farklı uzama hızları oluşturur.','dikkat')],
  istenen='Yatay konumdaki fidenin gövde ve kökünün bükülme yönü.',ip=['Grafikte her organın iki derişimdeki uzama değişimini ayrı ayrı oku ve hangi yüzeyin daha hızlı uzadığını bul.'],
  bilgi=[B('Oksin','hücre uzamasını uyaran bitki hormonudur; etkisi derişime ve hedef organa bağlıdır'),
         B('Eşit olmayan büyüme','bir organın iki yüzeyi farklı hızlarda uzadığında organ, daha yavaş uzayan yüzeye doğru bükülür')],
  puf='Eğrideki işareti oku: uzamayı artıran yüzey dışa, azaltan yüzey içe doğru bükülmeyi belirler; kök ve gövde aynı derişime ters yanıt verebilir.',sekil=SK)

# ---- 13 · etilen · orta · öncüllü
d13={'I':(False,'sitokinin hücre bölünmesini uyaran ve yaşlanmayı geciktiren bir hormondur; olgunlaşmayı uyaran gaz hâlindeki hormon etilendir'),
     'II':(True,'olgun meyvelerin saldığı gaz hâlindeki etilen hormonu, havada yayılarak diğer meyvelerin olgunlaşmasını uyarır'),
     'III':(True,'kapalı ortamda etilen dışarı yayılamadığından meyvelerin çevresinde birikir ve olgunlaşmayı hızlandırır')}
o=onc_t(d13,4)
Q('13','hormon','orta','hikâyeli','Etilen','Olgunlaşmayı uyaran gaz hormonun özelliklerini günlük bir gözlemle ilişkilendirir.',
  'Etilen, gaz hâlindeki bir hormondur; olgun meyvelerden salınır, havada yayılır ve çevredeki meyvelerin olgunlaşmasını hızlandırır.','Olgunlaşmayı sitokinin ya da oksine bağlamak.','etilen ve meyve olgunlaşması',
  [A('Gözlemi yorumla','Yeşil muzlar olgun elmalarla birlikte kapalı kolide daha çabuk sararmıştır. Bu, elmalardan çıkan bir maddenin muzları etkilediğini gösterir.','Elma → muz: olgunlaşma hızlanmış'),
   A('I. yargıyı değerlendir','Sitokinin yaşlanmayı geciktirir ve hücre bölünmesini uyarır; olgunlaşmayı hızlandırmaz.',oy({'I':d13['I']})),
   A('II. ve III. yargıları değerlendir','Olgun meyvelerden salınan gaz hâlindeki etilen havada yayılır. Kapalı ortamda dışarı çıkamadığından muzların çevresinde birikir.',oy({'II':d13['II'],'III':d13['III']}))],
  metin='Bir manav, olgunlaşmamış yeşil muzları olgun elmalarla birlikte kapalı bir kolide bekletmiştir. Birkaç gün sonra bu muzların, aynı koşullarda yalnız başına bekletilen yeşil muzlara göre daha çabuk sararıp olgunlaştığı gözlenmiştir.\nI. Elmalar tarafından salınan sitokinin hormonu, muzların olgunlaşmasını hızlandırmıştır.\nII. Olgun elmaların saldığı gaz hâlindeki bir hormon, muzlara ulaşarak olgunlaşmayı uyarmıştır.\nIII. Kolinin kapalı olması, bu hormonun muzların çevresinde birikmesine katkıda bulunmuştur.\nBuna göre bu yargılardan hangileri doğrudur?',
  istenen='Doğru olan yargıların belirlenmesi.',ip=['Meyvelerin olgunlaşmasını hangi hormonun uyardığını ve kolinin kapalı olmasının sonuçlarını düşün.'],
  bilgi=[B('Bitki hormonları','bitkilerde büyüme, gelişme ve çevreye yanıt, çok az miktarda üretilen hormonlarla düzenlenir; her hormonun etkisi hedef doku ve derişime göre değişir'),
         B('Hormonların etkileri','oksin ve giberellin uzamayı, sitokinin hücre bölünmesini uyarır; absisik asit (ABA) büyümeyi baskılar')],
  puf='Meyve olgunlaşmasını uyaran gaz hormon etilendir; kapalı ortamda birikerek etkisini artırır.',**o)

# ---- 14 · apikal dominans · zor · öncüllü
SK=f_apikal()
SON={'A':False,'B':True,'C':False,'D':True}   # yan tomurcuklar gelişti mi
d14={'I':(True,'A ile B karşılaştırıldığında uç tomurcuk varken yan tomurcuklar gelişmez, uç kesilince gelişir; baskılayan etki uç tomurcuktan gelir'),
     'II':(True,'B ile C karşılaştırıldığında uç kesilmiş olsa da kesik yüzeye oksin sürülünce yan tomurcuklar gelişmez; oksin baskılayıcı etkenlerden biridir'),
     'III':(False,'D’de uç tomurcuk kesilmediği hâlde sitokinin sürülen yan tomurcuklar gelişmiştir; sitokinin, uç kesilmeden de uyarıcı olabilir')}
assert SON['A']!=SON['B'] and SON['C']==SON['A'] and SON['D'] and not d14['III'][0]
o=onc_t(d14,3)
Q('14','hormon','orta','öncüllü','Apikal dominans','Uç tomurcuk, oksin ve sitokinin uygulamalı deney sonuçlarından hormonların yan tomurcuk gelişimindeki rolünü çıkarır.',
  'Uç tomurcukta üretilen oksin yan tomurcukların gelişimini baskılar; sitokinin bu baskıyı ortadan kaldırarak yan tomurcuk gelişimini uyarır.','Sitokininin etkisinin yalnız uç kesildiğinde ortaya çıktığını sanmak.','apikal dominans deneyi',
  [A('Grup farklarını belirle','A kontroldür, B’de uç kesilmiştir, C’de uç kesilip kesik yüzeye oksin sürülmüştür, D’de uç bırakılıp yan tomurcuklara sitokinin sürülmüştür.','A: baskılı · B: gelişmiş · C: baskılı · D: gelişmiş'),
   A('I. yargıyı değerlendir','A ve B arasındaki tek fark uç tomurcuktur; uç varken yan tomurcuklar gelişmez, kesilince gelişir.',oy({'I':d14['I']})),
   A('II. yargıyı değerlendir','B ile C arasındaki fark kesik yüzeye sürülen oksindir; oksin sürülünce yan tomurcuk gelişimi yeniden baskılanır.',oy({'II':d14['II']})),
   A('III. yargıyı değerlendir','D’de uç tomurcuk yerindeyken sitokinin sürülen yan tomurcuklar gelişmiştir. Bu nedenle sitokininin etkisi uç kesilmesine bağlı değildir.',oy({'III':d14['III']}))],
  metin='Aynı türden dört bitkiye şu uygulamalar yapılmış ve 10 gün sonraki durumları şekilde gösterilmiştir. A: uç tomurcuk bırakılmıştır. B: uç tomurcuk kesilmiştir. C: uç tomurcuk kesilmiş, kesik yüzeye oksin içeren macun sürülmüştür. D: uç tomurcuk bırakılmış, yan tomurcuklara sitokinin sürülmüştür.\nI. Yan tomurcukların gelişimi, uç tomurcuğun varlığıyla baskılanmaktadır.\nII. Oksin, yan tomurcuk gelişimini baskılayan etkenlerden biridir.\nIII. Sitokinin, yan tomurcuk gelişimini yalnızca uç tomurcuk kesildiğinde uyarabilir.\nBuna göre bu yargılardan hangileri doğrudur?',
  istenen='Doğru olan yargıların belirlenmesi.',ip=['Her yargı için şekildeki uygulamaları ve sonuçları karşılaştır.'],
  bilgi=[B('Tomurcuklar','bitkilerde uç ve yan tomurcuklar bulunur; tomurcukların gelişimi hormonlarla düzenlenir'),
         B('Kontrollü deney','bir değişkenin etkisi, yalnız o değişkenin farklı olduğu gruplar karşılaştırılarak belirlenir')],
  puf='İki grubu karşılaştırırken yalnız tek değişkenin farklı olduğu çifti seç; sonuç o değişkene aittir.',sekil=SK,**o)

# ---- 15 · çiçek kesiti · orta
SK=f_cicek()
pairs=['I – II','II – IV','IV – III','III – IV','VII – IV']
Q('15','ureme','orta','şekilli','Çiçek yapısı','Çiçeğin yapısında numaralı kısımları tanıyıp döllenme sonrası meyve ve tohum oluşturan yapıları belirler.',
  'Döllenmeden sonra ovaryum meyveye, ovül tohuma dönüşür; stil, stigma, anter ve taç yaprak meyveyi oluşturmaz.','Ovül ile ovaryumu karıştırmak; stili meyveye dönüşecek yapı saymak.','çiçek boyuna kesiti',
  [A('Yapıları tanı','Üstte stigma, onu ovaryuma bağlayan ince stil, ovaryum içinde ovüller, yanlarda filament ve anterler, en dışta taç yapraklar bulunur.','I: stigma · II: stil · III: ovaryum · IV: ovül · V: anter · VI: filament · VII: taç yaprak'),
   A('Döllenme sonrası dönüşümü hatırla','Döllenmiş ovül tohuma, ovülü saran ovaryum duvarı ise meyveye dönüşür.','Ovaryum → meyve · Ovül → tohum'),
   A('Çiftleri eşleştir','Meyveyi oluşturan yapı III, tohumu oluşturan yapı IV’tür.','III – IV')],
  metin='Şekilde, çiçekli bir bitkinin çiçeğinin boyuna kesiti şematik olarak verilmiştir. Bu çiçekte polen taneleri stigmaya ulaşmış, çifte döllenme gerçekleşmiş ve çiçek meyve vermiştir.\nBuna göre, döllenmeden sonra gelişerek sırasıyla meyveyi ve tohumu oluşturan yapılar numaralı kısımlardan hangileridir?',
  dogru='III – IV',sira=pairs,
  yan=[('I – II','Stigma meyve, stil tohum sanılmış; oysa stigma polenin tutunduğu, stil ise polen tüpünün ilerlediği yapıdır ve her ikisi de döllenmeden sonra solar.','bilgi'),
       ('II – IV','Stil meyveye dönüşen yapı sanılmış; oysa meyveyi ovaryum oluşturur, stil döllenmeden sonra solar.','bilgi'),
       ('IV – III','Ovül ile ovaryumun görevi yer değiştirmiş; oysa ovaryum meyveye, ovül tohuma dönüşür.','bilgi'),
       ('VII – IV','Taç yaprak meyve sanılmış; oysa taç yapraklar döllenmeden sonra dökülür ya da solar, meyveyi ovaryum oluşturur.','bilgi')],
  istenen='Döllenmeden sonra meyveyi ve tohumu oluşturan yapıların numaraları.',ip=['Döllenmenin gerçekleştiği yapıyı ve onu saran dokuyu şekilde bul; döllenme sonrası bunların nasıl değiştiğini düşün.'],
  bilgi=[B('Çiçeğin kısımları','çiçekte dişi organ (stigma, stil, ovaryum) ile erkek organ (anter, filament) ve taç yapraklar bulunur; polen anterde, ovül ovaryumda oluşur'),
         B('Döllenme sonrası gelişim','çiçekli bitkilerde döllenmeden sonra çiçeğin bazı kısımları gelişir, bazıları ise solar ya da dökülür')],
  puf='Döllenme sonrası ovaryum meyve, ovül tohum olur; geri kalan çiçek kısımları solar.',sekil=SK)

# ---- 16 · embriyo kesesi · zor
SK=f_kese()
N=12; CIFT=2*N; assert CIFT==24
ZIGOT=N+N; ENDO=N+N+N; TOP=ZIGOT+ENDO; assert (ZIGOT,ENDO,TOP)==(24,36,60)
assert 8*N==96 and ENDO==36 and ZIGOT+(N+N+N+N)==72 and ZIGOT+(N+N)==48
Q('16','ureme','zor','şekilli','Çifte döllenme','Embriyo kesesindeki çekirdekleri sayıp çifte döllenmeden oluşan yapıların kromozom sayılarını hesaplar.',
  'Embriyo kesesindeki çekirdekler haploiddir; yumurta ile sperm birleşince zigot (2n), iki polar çekirdek ile sperm birleşince endosperm ana hücresi (3n) oluşur.','Endospermi 2n ya da 4n sanmak; tüm çekirdekleri saymak.','embriyo kesesi, kromozom sayısı',
  [A('Çekirdek sayılarını şekilden oku','I numaralı hücrede bir, II numaralı yapıda iki çekirdek vardır. Embriyo kesesindeki her çekirdek haploiddir ve vücut hücresinin yarısı kadar kromozom taşır.','n = 24 ÷ 2 = 12'),
   A('Zigotu hesapla','Yumurta çekirdeği (n) ile bir sperm çekirdeği (n) birleşir.','12 + 12 = 24'),
   A('Endosperm ana hücresini hesapla','İki polar çekirdek (n + n) ile diğer sperm çekirdeği (n) birleşir.','12 + 12 + 12 = 36'),
   A('Toplamı bul','İstenen, iki hücrenin çekirdeklerindeki kromozom sayılarının toplamıdır.','24 + 36 = 60')],
  metin='Şekilde, vücut hücrelerinde 24 kromozom bulunan bir çiçekli bitkinin olgun embriyo kesesi gösterilmiştir. Polen tüpüyle gelen iki sperm çekirdeğinden biri I numaralı hücrenin çekirdeğiyle, diğeri II numaralı çekirdeklerle birleşerek çifte döllenmeyi tamamlamıştır.\nBuna göre, bu olay sonucunda oluşan zigot ile endosperm ana hücresinin çekirdeklerindeki toplam kromozom sayısı kaçtır?',
  dogru=TOP,
  yan=[(ENDO,'Yalnız endosperm ana hücresi (3n = 36) hesaplanmış, zigot (2n = 24) toplama katılmamıştır.','dikkat'),
       (ZIGOT+(N+N),'Endosperm ana hücresi 2n = 24 sanılmış; oysa iki polar çekirdek ve bir sperm çekirdeği bulunduğundan 3n = 36’dır. 24 + 24 = 48 bulunmuştur.','bilgi'),
       (ZIGOT+4*N,'Endosperm ana hücresi 4n = 48 sanılmış; iki sperm çekirdeğinin ikisi de polar çekirdeklerle birleşmiş kabul edilmiştir. 24 + 48 = 72 bulunmuştur.','bilgi'),
       (8*N,'Embriyo kesesindeki sekiz çekirdeğin hepsi toplanmış (8 × 12 = 96); oysa istenen yalnız zigot ve endosperm ana hücresinin kromozomlarıdır.','dikkat')],
  istenen='Zigot ile endosperm ana hücresindeki toplam kromozom sayısı.',ip=['Embriyo kesesindeki çekirdeklerin haploit olduğunu ve her sperm çekirdeğinin hangi çekirdekle birleştiğini sırayla izle.'],
  bilgi=[B('Embriyo kesesi','çiçekli bitkilerde dişi gametofittir; megasporun mitozlarıyla oluşan haploit çekirdekleri bulundurur'),
         B('Çifte döllenme','çiçekli bitkilerde döllenme sırasında iki sperm çekirdeği görev alır; oluşan yapıların kromozom sayısı, birleşen çekirdeklerin kromozom sayılarının toplamıdır')],
  puf='Embriyo kesesindeki çekirdekler haploittir: yumurta + sperm = 2n, iki polar çekirdek + sperm = 3n.',sekil=SK)

# ---- 17 · halkalama · zor
s17=[('Ksilem de zedelendiği için halkanın üstündeki dala su ulaşamaz; salkımlar yalnızca yapraklardaki şekerle büyür ve kökler şeker almayı sürdürür.',False,'ksilem zedelenmediğinden su taşınımı sürer; ayrıca floem kesik olduğundan köklere yapraklardan şeker ulaşmaz.'),
     ('Şeker halkanın altında birikir; salkımlar şeker alamadığı için küçük kalır ve kökler daha fazla şeker kullanır.',False,'şeker floemden aşağıya geçemeyeceği için halkanın üstünde birikir; üstteki salkımlar havuz olduğundan daha fazla şeker alır ve kökler şekersiz kalır.'),
     ('Floemde şeker yalnız yukarı yönde taşındığından salkımlar şeker alamaz; kökler ise ksilemden şeker alarak beslenir.',False,'floemde şeker kaynaktan havuza taşınır ve salkımlar havuz olduğunda şeker alır; ksilem ise şeker değil su ve mineral taşır.'),
     ('Salkımlara giden şeker artar; halkanın altındaki kökler yapraklardan şeker alamadığı için zamanla depo maddelerini kullanır, ksilem sağlam kaldığından su taşınımı sürer.',True,''),
     ('Halkanın altındaki kökler yapraklardan şeker almayı sürdürdüğünden salkımlara giden şeker miktarı değişmez ve su taşınımı durur.',False,'floem kesildiği için köklere şeker ulaşmaz; ksilem zedelenmediğinden su taşınımı da durmaz.')]
o=tek(s17,True)
Q('17','tasima','zor','hikâyeli','Floem ve ksilem','Floemin kesilmesinin şeker ve su taşınmasına etkisini kaynak–havuz ilişkisiyle yorumlar.',
  'Floem şekeri kaynaktan havuza taşır, ksilem suyu kökten yukarı iletir; floem kesilirse şeker kesik yerin üstünde birikir, su taşınımı sürer.','Halkalamanın ksilemi de kestiğini sanmak; floemde yalnız tek yönlü akış olduğunu düşünmek.','halkalama, kaynak ve havuz',
  [A('Uygulamayı yorumla','Kabuk şeridiyle birlikte floem çepeçevre kaldırılmış, odun kısmı yani ksilem sağlam bırakılmıştır.','Floem kesik · ksilem sağlam'),
   A('Şeker taşınmasını incele','Yapraklarda üretilen şeker floemde kaynaktan havuza taşınır. Halkada floem olmadığından şeker aşağıya geçemez ve salkımlara yönelir.','Şeker: halkanın altına inemez'),
   A('Su taşınmasını incele','Su ve mineraller ksilemle yukarı taşınır. Ksilem zedelenmediğinden halkanın üstündeki dala su ulaşmaya devam eder.','Su: ksilemle sürer'),
   A('Sonucu birleştir','Salkımlara şeker yönelir, kökler depo maddeye döner ve su akışı sürer.','Doğru ifade: şeker üstte kalır, su taşınımı sürer')],
  metin='Bağcılıkta salkımlardaki taneleri iri ve şekerli elde etmek için, meyve veren bir dalın tabanından floemi içine alacak biçimde çepeçevre ince bir kabuk şeridi kaldırılır; odun kısmı (ksilem) zedelenmez. Dalın üstünde yapraklar ve salkımlar, altında ise gövde ve kökler bulunmaktadır.\nBuna göre, bu uygulamadan sonra aşağıdakilerden hangisi gerçekleşir?',
  istenen='Halkalama sonrası şeker ve su taşınmasıyla ilgili doğru ifade.',ip=['Halkada hangi iletim dokusunun kesildiğini ve hangisinin sağlam kaldığını belirle; sonra şeker ile suyun ayrı yollarını düşün.'],
  bilgi=[B('Kaynak ve havuz','şeker üretilen organ kaynak, kullanıldığı ya da depolandığı organ havuzdur; floemde şeker kaynaktan havuza doğru taşınır'),
         B('Ksilem ve floem','ksilem kökten yukarı su ve mineral taşır, floem yapraklardan şekeri havuza taşır; iki doku ayrı ayrı çalışır')],
  puf='Floem ile ksilem ayrı çalışır: floemi kesmek şekerin yolunu keser, suyun yolunu kesmez.',**o)

# ---- 18 · ABA grafiği · zor · olumsuz
SK=f_aba()
assert all(ABA[i]<ABA[i+1] for i in range(8)) and all(STO[i]>=STO[i+1] for i in range(8))
assert FOT[4]>40 and STO[4]<50 and FOT[4]<70 and ABA[5]==90 and all(v<30 for v in STO[5:])
s18=[('ABA derişimindeki artış, klorofil moleküllerini doğrudan parçalayarak fotosentez hızını düşürmüştür.',False,''),
     ('Kuraklık süresi uzadıkça ABA derişimi artarken stoma açıklığı azalmıştır.',True,'grafikte ABA eğrisi yükselirken stoma açıklığı eğrisi alçalmaktadır.'),
     ('4. günde fotosentez hızı, 0. gündeki değerinin %40’ından fazladır.',True,'4. günde fotosentez hızı yaklaşık %55’tir.'),
     ('4. günde stoma açıklığı 0. gündeki değerinin %50’sinin altındadır ve fotosentez hızı 0. gündeki değerinin %70’inin altındadır.',True,'4. günde stoma açıklığı yaklaşık %35, fotosentez hızı yaklaşık %55’tir.'),
     ('ABA derişimi en yüksek değerinin %90’ına ulaştığında stoma açıklığı 0. gündeki değerinin %30’unun altına inmiştir.',True,'ABA 5. günde %90’a ulaşmış ve aynı günde stoma açıklığı yaklaşık %18’dir.')]
o=tek(s18,False)
Q('18','terleme','zor','grafik','ABA ve stoma','Kuraklıkta ABA, stoma açıklığı ve fotosentez hızı eğrilerini birlikte yorumlar ve grafikle desteklenmeyen çıkarımı ayırt eder.',
  'ABA, kuraklıkta stomaların kapanmasını sağlar; stoma kapanınca CO₂ girişi azalır ve fotosentez hızı düşer; grafikten yalnız verilerle desteklenen çıkarımlar yapılabilir.','Grafikte ölçülmeyen bir mekanizmayı (klorofil yıkımı) veriden çıkarılabilir sanmak.','kuraklık, ABA ve stoma grafiği',
  [A('Eğrileri oku','ABA derişimi günler içinde artarken stoma açıklığı ve fotosentez hızı azalmaktadır. Fotosentez, stomadan biraz gecikmeyle düşmeye başlar.','ABA ↑ · Stoma ↓ · Fotosentez ↓'),
   A('Yargıları grafikle sına','ABA artarken stomanın azalması, 4. gün fotosentezin %55, stoma açıklığının %35 olması grafikte görülür. ABA’nın 5. günde %90’a ulaşması ve stomanın %18 olması da grafikte vardır.','Grafikle desteklenen: 4 yargı'),
   A('Desteklenmeyeni seç','Klorofilin ABA tarafından doğrudan parçalandığına ilişkin bir veri grafikte yoktur; ABA’nın etkisi stomaların kapanmasıdır.','Cevap: klorofil parçalanması iddiası')],
  metin='Şekildeki grafikte, kuraklık stresine giren bir bitkinin yapraklarında ABA derişimi, stoma açıklığı ve fotosentez hızının 8 gün boyunca değişimi verilmiştir. Her büyüklük, kendi en yüksek değerine göre yüzde olarak gösterilmiştir; stoma açıklığı ve fotosentez hızı 0. günde en yüksek değerindedir.\nBuna göre, bu grafikten aşağıdakilerden hangisi çıkarılamaz?',
  istenen='Grafikten çıkarılamayan ifade.',ip=['Her ifadeyi, grafikteki eğrilerin değerleriyle tek tek karşılaştır.'],
  bilgi=[B('Absisik asit (ABA)','bitkilerde stres koşullarında üretilen ve büyümeyi baskılayan hormondur; kuraklıkta bekçi hücrelerinden iyon çıkışını uyararak stomaların kapanmasını sağlar'),
         B('Grafik yorumlama','bir grafikten çıkarım yapılırken eğrilerin eksenlerdeki değerleri okunur ve eğrilerin zamanla değişimleri karşılaştırılır')],
  puf='Grafikten yalnız çizilen eğrilerle desteklenen çıkarım yapılır; ölçülmeyen mekanizma iddiası çıkarılamaz.',sekil=SK,**o)

# ---- 19 · gutasyon · orta · öncüllü
d19={'I':(False,'gutasyonda su, stomalardan buhar olarak değil, hidatodlardan sıvı hâlinde atılır'),
     'II':(True,'kök basıncı ksilemdeki suyu yukarı iter ve hidatodlardan sıvı su çıkışını sağlar'),
     'III':(False,'gutasyon, stomaların kapalı ve havanın nemli olduğu gece ve sabah saatlerinde görülür; stomalardan terleme ise gündüz yoğundur')}
o=onc_t(d19,1)
Q('19','tasima','orta','hikâyeli','Gutasyon ve kök basıncı','Yaprak kenarında sıvı su damlacıklarının oluşumunu gutasyon ve kök basıncı ile açıklar.',
  'Gutasyon, nemli ve serin havada hidatodlardan sıvı suyun atılmasıdır; kök basıncı bu suyu yukarı iter, terleme ise stomalardan buhar kaybıdır.','Gutasyonu terleme sanmak; sıvı su kaybını stomalara bağlamak.','gutasyon ve terleme',
  [A('Olayı tanımla','Serin ve nemli bir gecenin sabahında yaprak kenar ve uçlarında sıvı su damlacıkları oluşması gutasyondur.','Olay: gutasyon (sıvı su atılımı)'),
   A('I. ve III. yargıları değerlendir','Gutasyonda su stomalardan buhar olarak değil, hidatodlardan sıvı olarak atılır. Olay gece ve sabah, stomalar kapalıyken görülür.',oy({'I':d19['I'],'III':d19['III']})),
   A('II. yargıyı değerlendir','Stomaların kapalı olduğu gece buharlaşma azdır; kök basıncı suyu ksilemde yukarı iterek damlacıkların oluşmasını sağlar.',oy({'II':d19['II']}))],
  metin='Serin ve nemli bir gecenin ardından sabah erken saatte, bir çim bitkisinin yaprak kenar ve uçlarında su damlacıkları gözlenmiştir. Bu saatte havadaki nem oranı yüksektir ve bitkinin stomaları kapalıdır. Güneş yükselip hava ısındıkça damlacıkların kaybolduğu görülmüştür.\nI. Bu olayda su, stomalardan su buharı hâlinde atılmaktadır.\nII. Olayın gerçekleşmesinde kök basıncı etkilidir.\nIII. Olay, stomaların açık olduğu gündüz saatlerinde en yoğun yaşanır.\nBuna göre bu yargılardan hangileri doğrudur?',
  istenen='Doğru olan yargıların belirlenmesi.',ip=['Yaprak kenarındaki damlacıkların hangi hâlde ve hangi yapıdan atıldığını düşün; suyu yukarı iten kuvveti belirle.'],
  bilgi=[B('Terleme','bitkinin yapraklarından su buharı kaybetmesidir; stomaların açıklığı ve havanın nemi bu kaybı etkiler'),
         B('Kök basıncı','köklerde su girişine bağlı olarak ksilem içinde oluşan basınçtır')],
  puf='Sıvı su damlası gutasyondur: hidatoddan, kök basıncıyla, stomalar kapalıyken ortaya çıkar.',**o)

# ---- 20 · çimlenme tablosu · orta · olumsuz
SK=tablo_svg(['Kap','Su','Sıcaklık (°C)','Oksijen','Işık','Çimlenme'],[['1','Var','25','Var','Var','Gerçekleşti'],['2','Yok','25','Var','Var','Gerçekleşmedi'],['3','Var','4','Var','Var','Gerçekleşmedi'],['4','Var','25','Yok','Var','Gerçekleşmedi'],['5','Var','25','Var','Yok','Gerçekleşti']])
s20=[('Su, bu tohumların çimlenmesi için gerekli bir koşuldur.',True,'1. ve 2. kaplar yalnız su yönünden farklıdır ve çimlenme yalnız suyun bulunduğu kapta gerçekleşmiştir.'),
     ('Karbondioksit, bu tohumların çimlenmesi için gerekli bir koşuldur.',False,''),
     ('Oksijen, bu tohumların çimlenmesi için gerekli bir koşuldur.',True,'1. ve 4. kaplar yalnız oksijen yönünden farklıdır ve çimlenme yalnız oksijenin bulunduğu kapta gerçekleşmiştir.'),
     ('Işık, bu tohumların çimlenmesi için zorunlu değildir.',True,'1. ve 5. kaplar yalnız ışık yönünden farklıdır ve karanlık kapta da çimlenme gerçekleşmiştir.'),
     ('Sıcaklık, bu tohumların çimlenmesini etkileyen faktörlerden biridir.',True,'1. ve 3. kaplar yalnız sıcaklık yönünden farklıdır ve 4 °C’taki kapta çimlenme gerçekleşmemiştir.')]
o=tek(s20,False)
Q('20','ureme','orta','tablo','Çimlenme koşulları','Kontrollü deney tablosundan çimlenme için gerekli koşulları belirler; verinin ötesindeki çıkarımı ayırt eder.',
  'Çimlenme için su, uygun sıcaklık ve oksijen gerekir; bir koşulun gerekliliği yalnız o koşulun farklı olduğu kapların karşılaştırılmasıyla anlaşılır.','Denenmemiş bir koşulun (CO₂) gerekli olduğunu çıkarmak.','çimlenme deney tablosu',
  [A('Karşılaştırma çiftlerini belirle','Bir koşulun etkisi, yalnız o koşul bakımından farklı iki kap karşılaştırılarak bulunur. 1. kap kontrol kabıdır.','1–2: su · 1–3: sıcaklık · 1–4: oksijen · 1–5: ışık'),
   A('İfadeleri sına','Su, oksijen ve sıcaklık yokluğunda çimlenme olmamış, ışıksızlıkta ise olmuştur. Bu sonuçlar ilk üç ifadeyle ve ışık ifadesiyle uyumludur.','Su, oksijen, sıcaklık: gerekli · Işık: zorunlu değil'),
   A('Desteklenmeyeni seç','Karbondioksit hiçbir kapta değiştirilmemiştir; bu koşul hakkında bu deneyden sonuç çıkarılamaz.','Cevap: karbondioksit ifadesi')],
  metin='Aynı bitkiden alınan eşit sayıda ve nitelikte tohumlar, çimlenme koşullarının farklılaştırıldığı beş kapta aynı süre bekletilmiştir. Kapların su, sıcaklık, oksijen ve ışık durumları ile çimlenme sonuçları tabloda verilmiştir. Kaplardaki diğer koşullar aynıdır.\nBuna göre, bu deneyin sonuçlarından aşağıdakilerden hangisi çıkarılamaz?',
  istenen='Deney sonuçlarından çıkarılamayan ifade.',ip=['Her ifade için, yalnız o koşul bakımından farklı iki kap olup olmadığına bak.'],
  bilgi=[B('Çimlenme','tohumun dinlenme durumundan çıkıp embriyonun büyümeye başlamasıdır; su alımı ile başlar ve enzim etkinliği artar'),
         B('Kontrollü deney','bir faktörün etkisini görmek için yalnız o faktör değiştirilir, diğerleri sabit tutulur; karşılaştırılacak kap, kontrol grubuyla yalnız tek farkla ayrılır')],
  puf='Bir koşulun gerekliliği yalnız o koşulun farklı olduğu iki kapla gösterilir; denenmeyen koşul hakkında sonuç çıkarılamaz.',sekil=SK,**o)


PUF={'01':'Su ileten ve organik madde taşıyan dokuların hücre canlılığını karşılaştır.','03':'Hücre biçimini ve dizilişini yaprağın görevleriyle eşleştir.','06':'Şekildeki iyon ve su yönünü izle, bekçi hücresinin durumunu buna göre yorumla.',
 '07':'Karşılaştırma yapılırken yalnız verinin desteklediği sonuçlar kabul edilir.','09':'Yükleme ve boşaltmada suyun ve şekerin yönünü ayrı ayrı izle.','10':'Suyun ve iyonların geçiş yollarını ayrı ayrı düşün.',
 '11':'Uyaranı algılayan bölgeyi belirle, sonra her düzenekte o bölgenin durumuna bak.','13':'Olayı açıklayan hormonu ve ortam koşulunu birlikte değerlendir.','14':'Karşılaştırmada yalnız bir değişkeni farklı olan grupları eşleştir.',
 '15':'Döllenme sonrası çiçek kısımlarının akıbetini bir tabloyla çıkar.','16':'Her çekirdeğin ploidisini yazıp birleşmeleri toplayarak ilerle.','17':'İki iletim dokusunun görevini ayrı ayrı değerlendir.','19':'Damlacığın hâlini ve çıkış yerini belirle.','20':'Her yargıyı veriyle sınayarak ilerle.'}
FIK={'01':'Kök kesitinde dokular canlılık ve yapı bakımından ayrışır.','03':'Yaprak kesitindeki hücre biçimi ve dizilişi dokunun görevine uyum gösterir.','07':'Kontrollü deneyde sonuçlar yalnız verinin desteklediği ölçüde yorumlanır.','08':'Miktar değişimi, hız eğrileri arasındaki alanlarla bulunur.',
 '09':'Floemde madde taşınması kaynak ve havuz arasında enerji ve basınç farkıyla gerçekleşir.','11':'Yönelim hareketlerinde uyaranı algılayan bölge belirlenir.','15':'Döllenme sonrası çiçek kısımları farklı akıbetlere uğrar.','17':'Ksilem ve floem farklı maddeleri farklı yollarla taşır.','19':'Bitkiler suyu farklı yollarla ve farklı hâllerde atabilir.','20':'Bir faktörün etkisi yalnız o faktörün değiştiği gruplarla sınanır.','18':'Hormon, stoma ve fotosentez arasındaki ilişki grafikle yorumlanır.'}
TUZ={'07':'Veri yorumunda sonucu verinin ötesine taşımak.','20':'Deneyde sınanmamış bir etkeni sonuca katmak.','18':'Grafikte ölçülmeyen bir ilişkiyi veriden çıkarılabilir sanmak.','15':'Çiçek kısımlarının döllenme sonrası dönüşümlerini karıştırmak.'}
for q in P.ANA:
    n=q['id'][-2:]
    if n in PUF: q['puf']=PUF[n]
for c in H.KARTLAR:
    n=c['id'][-2:]
    if n in FIK: c['fikir']=FIK[n]
    if n in TUZ: c['tuzak']=TUZ[n]

# ================= yaz =================
for x in P.ANA: x['kardes']=None
SCR=os.environ.get('SCRATCH','/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/bit')
os.makedirs(SCR,exist_ok=True)
P.yaz(os.path.join(GD,'bitki-1.json'),os.path.join(SCR,'bos-bitki.json'))
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=KEY))['kartlar'].append(c['id'])
json.dump(dict(konu=KONU_AD,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2018–2026 Biyoloji (bitki biyolojisi), MEB 11. sınıf Bitki Biyolojisi.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','abbitki.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
