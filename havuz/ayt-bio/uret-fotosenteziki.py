"""AYT Biyoloji · Fotosentez – Kemosentez · 2. dalga · 10 soru. Kardeş yok, ipucu 1.
Şekiller TikZ/pgfplots; tüm değerler tek yerde tanımlanır, doğru şık ve çeldiriciler assert edilir."""
import sys,os,json,math
from collections import Counter
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-bio'))
import _hafif_bio as H
from _hafif_bio import *
KONU_AD='Fotosentez – Kemosentez'; KEY='abio|Fotosentez – Kemosentez'
P=Parti('fotosenteziki',KONU_AD,KEY,ders='AYT Biyoloji',idon='aytbio'); H.KONU=KONU_AD
KAYNAK='ÖSYM AYT 2018–2026 Biyoloji fotosentez ve kemosentez soruları (yalnız mantık) · MEB 12. sınıf Canlılarda Enerji Dönüşümü'
TIP={'klo':('fs2-kloroplast','Kloroplast ve fotosentez yapan hücreler'),
     'cal':('fs2-calvin','Calvin döngüsü'),
     'fak':('fs2-faktor','Fotosentez hızı, solunum ve sınırlayıcı faktörler'),
     'den':('fs2-deney','Fotosentez deneyleri'),
     'pig':('fs2-pigment','Pigmentler ve ışık rengi'),
     'kem':('fs2-kemosentez','Kemosentez ve fotosentezle karşılaştırma')}
def Q(no,tp,z,kalip,alt,kaz,fikir,tuzak,ozet,ad,**k):
    t,tn=TIP[tp]; H.kart(f'K-ABFOT2-{no}',alt,fikir,tuzak,z,kalip,len(ad),t,tn,KAYNAK)
    assert len(k['ip'])==1
    mk(P,no.zfill(4),ad=ad,adim=len(ad),tipId=t,tip=tn,z=z,alt=alt,kaz=kaz,kalip=kalip,kart=f'K-ABFOT2-{no} ({ozet})',**k)
def yer(harf,dogru,digerler):
    sira=[None]*5; sira['ABCDE'.index(harf)]=dogru; it=iter(digerler)
    for i in range(5):
        if sira[i] is None: sira[i]=next(it)
    assert len(set(sira))==5 and None not in sira; return sira
def tk(body,scale=1.0): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small,scale=%s]\n%s\n\\end{tikzpicture}'%(scale,body))
OK='-{Stealth[length=2.2mm,width=1.8mm]}'
ROM=['I','II','III','IV','V']
MASTER=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
def oncul(pre,harf):
    """pre: [(metin,dogru_mu,aciklama)] ; doğru öncülleri soran kök. (satırlar, sira, dogru, yan, işlem)"""
    anahtar=[i for i,(t,v,a) in enumerate(pre) if v]
    dogru=MASTER[[[0],[1],[2],[0,1],[0,2],[1,2],[0,1,2]].index(anahtar)]
    m=MASTER.index(dogru); p='ABCDE'.index(harf); assert m-p>=0 and m-p+5<=7,(dogru,harf)
    sira=MASTER[m-p:m-p+5]; yan=[]
    for o in sira:
        if o==dogru: continue
        idx=[[0],[1],[2],[0,1],[0,2],[1,2],[0,1,2]][MASTER.index(o)]; c=[]
        for i in range(3):
            if i in idx and i not in anahtar: c.append(f'{ROM[i]}. öncül yanlıştır ({pre[i][2]}); ancak doğru sanılıp seçilmiş.')
            if i not in idx and i in anahtar: c.append(f'{ROM[i]}. öncül doğrudur ({pre[i][2]}); ancak yanlış sanılıp dışarıda bırakılmış.')
        assert c; yan.append((o,' '.join(c),'bilgi'))
    satir='\n'.join(f'{ROM[i]}. {t}' for i,(t,v,a) in enumerate(pre))
    islem=' · '.join(f'{ROM[i]}: {"doğru" if v else "yanlış"}' for i,(t,v,a) in enumerate(pre))
    return satir,sira,dogru,yan,islem
def cyan(vals,aciklar,turler=None):
    return [(v,a,(turler[i] if turler else 'dikkat')) for i,(v,a) in enumerate(zip(vals,aciklar))]

# ============================ SORU 1 · panaşlı yaprak, nişasta ============================
BOL1={'I':dict(folyo=True,klorofil=True),'II':dict(folyo=False,klorofil=True),'III':dict(folyo=False,klorofil=False)}
NIS1=sorted(k for k,v in BOL1.items() if (not v['folyo']) and v['klorofil'])
assert NIS1==['II']
def sk1():
    b=[r'\draw[line width=1.3pt,fill=white] (0,0) ellipse (3.1 and 1.8);',
       r'\draw[line width=.8pt,fill=green!45] (0,0) ellipse (2.5 and 1.3);',
       r'\draw[line width=1pt,fill=gray!55] (-1.5,-.7) rectangle (-.3,.7);',
       r'\draw[line width=.8pt] (-3.1,0)--(-3.7,-.3);']
    b.append(rf'\node[font=\large\bfseries] at (-.9,2.6) {{I}};\draw[{OK},line width=.9pt] (-.9,2.3)--(-.9,.75);')
    b.append(rf'\node[font=\large\bfseries] at (1.3,2.6) {{II}};\draw[{OK},line width=.9pt] (1.3,2.3)--(1.3,.6);')
    b.append(rf'\node[font=\large\bfseries] at (4.4,0) {{III}};\draw[{OK},line width=.9pt] (3.95,0)--(2.85,0);')
    return tk('\n'.join(b),.95)
SK1=sk1()
# ============================ SORU 2 · renkli ışık ============================
IS2={'K':('Mavi ışık','blue!70',3),'L':('Yeşil ışık','green!60!black',1),'M':('Kırmızı ışık','red!75',2)}   # soğurma düzeyi (göreli)
assert IS2['L'][2]<IS2['M'][2] and IS2['L'][2]<IS2['K'][2]
def sk2():
    b=[]
    for i,(k,(ad,c,_)) in enumerate(IS2.items()):
        x=i*4.4
        b.append(rf'\draw[line width=1pt] ({x},3.6)--({x},3.25);')
        b.append(rf'\draw[line width=1pt,fill={c},fill opacity=.35] ({x-.6},3.25)--({x+.6},3.25)--({x+.95},2.6)--({x-.95},2.6)--cycle;')
        for dx in (-.7,0,.7): b.append(rf'\draw[{c},dashed,line width=1pt] ({x+dx},2.5)--({x+dx*.7},1.55);')
        b.append(rf'\draw[line width=1pt,fill=brown!45] ({x-.45},0)--({x+.45},0)--({x+.6},.6)--({x-.6},.6)--cycle;')
        b.append(rf'\draw[line width=1.2pt,green!50!black] ({x},.6)--({x},1.5);')
        b.append(rf'\draw[line width=.8pt,fill=green!55!black!60] ({x-.35},1.15) ellipse (.38 and .17);\draw[line width=.8pt,fill=green!55!black!60] ({x+.35},1.4) ellipse (.38 and .17);')
        b.append(rf'\node[font=\small] at ({x},4.0) {{{ad}}};\node[font=\large\bfseries] at ({x},-.5) {{{k}}};')
    return tk('\n'.join(b),.9)
SK2=sk2()
# ============================ SORU 3 · yaprak kesiti ============================
KLO3={'I':False,'II':True,'III':True,'IV':True}   # numaralı hücrede kloroplast var mı (I: üst epidermis; IV: bekçi hücresi)
assert [k for k,v in KLO3.items() if not v]==['I']
def sk3():
    b=[]
    def nuc(x,y): return rf'\fill[black!55] ({x:.2f},{y:.2f}) circle (.07);'
    for i in range(8):
        x=i*1.125; b.append(rf'\draw[line width=.9pt] ({x:.3f},4.2) rectangle ({x+1.125:.3f},4.9);'); b.append(nuc(x+.56,4.55))
    for i in range(14):
        x=i*.643; b.append(rf'\draw[line width=.9pt,rounded corners=3pt] ({x:.3f},2.5) rectangle ({x+.643:.3f},4.2);'); b.append(nuc(x+.32,3.0))
    for (cx,cy,rx,ry) in [(.5,1.9,.45,.35),(1.4,2.1,.4,.3),(2.3,1.8,.45,.35),(3.3,2.0,.4,.3),(4.3,1.8,.5,.35),(5.3,2.1,.4,.3),(6.3,1.8,.45,.35),(7.2,2.1,.4,.3),(8.2,1.9,.45,.35),
                          (.9,1.1,.4,.3),(1.9,1.2,.45,.3),(2.9,1.0,.4,.3),(3.8,1.1,.4,.3),(5.0,1.0,.5,.3),(5.9,1.2,.4,.3),(6.9,1.0,.45,.3),(7.9,1.2,.4,.3)]:
        b.append(rf'\draw[line width=.9pt] ({cx},{cy}) ellipse ({rx} and {ry});'); b.append(nuc(cx,cy))
    for i in range(4):
        x=i*.95; b.append(rf'\draw[line width=.9pt] ({x:.2f},0) rectangle ({x+.95:.2f},.5);'); b.append(nuc(x+.47,.25))
    for i in range(4):
        x=5.2+i*.95; b.append(rf'\draw[line width=.9pt] ({x:.2f},0) rectangle ({x+.95:.2f},.5);'); b.append(nuc(x+.47,.25))
    # bekçi hücreleri (böbrek biçimli) ve stoma
    b.append(r'\draw[line width=1pt] (3.8,.25) .. controls (3.85,.6) and (4.5,.6) .. (4.5,.25) .. controls (4.5,-.1) and (3.85,-.1) .. (3.8,.25);')
    b.append(r'\draw[line width=1pt] (5.0,.25) .. controls (5.0,.6) and (4.6,.6) .. (4.6,.25) .. controls (4.6,-.1) and (5.0,-.1) .. (5.0,.25);')
    b.append(nuc(4.15,.28)); b.append(nuc(4.85,.28))
    b.append(rf'\node[font=\large\bfseries] at (-.9,4.55) {{I}};\draw[{OK},line width=.9pt] (-.6,4.55)--(.15,4.55);')
    b.append(rf'\node[font=\large\bfseries] at (-.9,3.3) {{II}};\draw[{OK},line width=.9pt] (-.55,3.3)--(.15,3.3);')
    b.append(rf'\node[font=\large\bfseries] at (9.9,1.5) {{III}};\draw[{OK},line width=.9pt] (9.45,1.5)--(8.5,1.4);')
    b.append(rf'\node[font=\large\bfseries] at (4.5,-1.0) {{IV}};\draw[{OK},line width=.9pt] (4.5,-.65)--(4.15,-.08);')
    return tk('\n'.join(b),.62)
SK3=sk3()
# ============================ SORU 4 · KOH düzeneği ============================
def sk4():
    b=[]
    for i,(k,ad) in enumerate((('K','KOH'),('L','Su'))):
        x=i*4.6
        b.append(rf'\draw[line width=1.3pt,rounded corners=10pt] ({x-1.5},0) rectangle ({x+1.5},3.3);\draw[line width=1.3pt] ({x-1.6},3.3)--({x+1.6},3.3);')
        b.append(rf'\draw[line width=1pt,fill=cyan!25] ({x-1.35},.08) rectangle ({x-.35},.85);\node[font=\small] at ({x-.85},.46) {{{ad}}};')
        b.append(rf'\draw[line width=1.2pt,green!50!black] ({x+.55},.1)--({x+.55},1.9);')
        b.append(rf'\draw[line width=.8pt,fill=green!55!black!60,rotate around={{25:({x+.15},2.0)}}] ({x+.15},2.0) ellipse (.45 and .2);\draw[line width=.8pt,fill=green!55!black!60,rotate around={{-25:({x+.95},2.2)}}] ({x+.95},2.2) ellipse (.45 and .2);')
        b.append(rf'\node[font=\large\bfseries] at ({x},-.5) {{{k}}};')
        b.append(rf'\fill[yellow!85!orange] ({x},4.3) circle (.28);')
        for a in range(0,360,45): b.append(rf'\draw[yellow!70!orange,line width=1pt] ({x+.4*math.cos(math.radians(a)):.2f},{4.3+.4*math.sin(math.radians(a)):.2f})--({x+.6*math.cos(math.radians(a)):.2f},{4.3+.6*math.sin(math.radians(a)):.2f});')
        b.append(rf'\node[font=\small] at ({x},5.0) {{Işık}};')
    return tk('\n'.join(b),.95)
SK4=sk4()
# ============================ SORU 5 · tablo, sınırlayıcı faktör ============================
ORT5={1:('Düşük','Yüksek',25,2),2:('Yüksek','Yüksek',25,8),3:('Yüksek','Düşük',25,3),4:('Yüksek','Yüksek',10,4)}
def fark(a,b): return [n for n,(x,y) in zip(('ışık','CO₂','sıcaklık'),zip(ORT5[a][:3],ORT5[b][:3])) if x!=y]
assert fark(1,2)==['ışık'] and fark(2,3)==['CO₂'] and fark(2,4)==['sıcaklık'] and set(fark(1,3))=={'ışık','CO₂'}
assert ORT5[1][3]<ORT5[2][3] and ORT5[3][3]<ORT5[2][3] and ORT5[4][3]<ORT5[2][3]
SK5=tablo_svg(['Ortam','Işık şiddeti','CO₂ derişimi','Sıcaklık (°C)','Fotosentez hızı'],[[str(k),v[0],v[1],str(v[2]),str(v[3])] for k,v in ORT5.items()])
# ============================ SORU 6 · gaz alışverişi durumları ============================
DUR6={'I':(5,5),'II':(8,5),'III':(2,5)}   # (fotosentez hızı, solunum hızı) göreli
FS6=[k for k,(f,s) in DUR6.items() if f>s]; assert FS6==['II']
assert [k for k,(f,s) in DUR6.items() if f-s==0]==['I'] and [k for k,(f,s) in DUR6.items() if f<s]==['III']
def sk6():
    b=[]
    for i,k in enumerate(DUR6):
        x=i*5.6
        b.append(rf'\draw[line width=1.3pt,rounded corners=10pt] ({x},0) rectangle ({x+4.4},3.4);')
        b.append(rf'\draw[line width=1pt,fill=green!45] ({x+.9},1.7) ellipse (.65 and .45);\draw[line width=1pt,fill=orange!50] ({x+3.5},1.7) ellipse (.65 and .45);')
        b.append(rf'\draw[{OK},line width=.9pt] ({x+1.6},1.95)--({x+2.8},1.95);\node[font=\small] at ({x+2.2},2.3) {{O$_2$}};')
        b.append(rf'\draw[{OK},line width=.9pt] ({x+2.8},1.45)--({x+1.6},1.45);\node[font=\small] at ({x+2.2},1.1) {{CO$_2$}};')
        if k=='II':
            b.append(rf'\draw[{OK},line width=.9pt] ({x+.9},2.2)--({x+.9},4.4);\node[font=\small] at ({x+.9},4.75) {{O$_2$}};')
            b.append(rf'\draw[{OK},line width=.9pt] ({x-1.0},1.7)--({x+.2},1.7);\node[font=\small] at ({x-.55},2.05) {{CO$_2$}};')
        if k=='III':
            b.append(rf'\draw[{OK},line width=.9pt] ({x+5.3},1.7)--({x+4.2},1.7);\node[font=\small] at ({x+4.85},2.05) {{O$_2$}};')
            b.append(rf'\draw[{OK},line width=.9pt] ({x+3.5},2.2)--({x+3.5},4.4);\node[font=\small] at ({x+3.5},4.75) {{CO$_2$}};')
        b.append(rf'\node[font=\large\bfseries] at ({x+2.2},-.55) {{{k}}};')
    b.append(r'\draw[line width=1pt,fill=green!45] (1.2,-1.45) ellipse (.4 and .26);\node[font=\small,anchor=west] at (1.7,-1.45) {Kloroplast};\draw[line width=1pt,fill=orange!50] (6.8,-1.45) ellipse (.4 and .26);\node[font=\small,anchor=west] at (7.3,-1.45) {Mitokondri};')
    return tk('\n'.join(b),.62)
SK6=sk6()
# ============================ SORU 8 · gün boyu net CO2 ============================
SAAT_ISIK=12; NET_ISIK=6; SOL=4; SAAT_KAR=24-SAAT_ISIK; CO2_GLIKOZ=6
NET_CO2=NET_ISIK*SAAT_ISIK-SOL*SAAT_KAR
GLI=Fr(NET_CO2,CO2_GLIKOZ); assert GLI==4
BRUT=(NET_ISIK+SOL)*SAAT_ISIK; assert Fr(BRUT-SOL*24,CO2_GLIKOZ)==GLI          # iki yoldan doğrulama
assert len({GLI,Fr(NET_ISIK*SAAT_ISIK,6),Fr(BRUT,6),Fr(SOL*SAAT_KAR,6),NET_CO2})==5
def sk8():
    b=[r'\begin{axis}[width=8.4cm,height=5.4cm,xmin=0,xmax=24,ymin=-6,ymax=8,xtick={0,6,12,18,24},ytick={-4,0,6},axis lines=left,xlabel={Zaman (saat)},ylabel={Net CO$_2$ alışverişi hızı},tick label style={font=\footnotesize},label style={font=\small},every axis plot/.append style={line width=1.6pt}]',
       r'\addplot[black!55,dashed,line width=.8pt] coordinates {(0,0)(24,0)};',
       r'\addplot[vurgu] coordinates {(0,-4)(6,-4)(6,6)(18,6)(18,-4)(24,-4)};',
       r'\addplot[black!45,dashed,line width=.8pt] coordinates {(6,-6)(6,8)};\addplot[black!45,dashed,line width=.8pt] coordinates {(18,-6)(18,8)};',
       r'\node[font=\small,anchor=south] at (axis cs:12,6.2) {Aydınlık};\node[font=\small,anchor=south] at (axis cs:3,0.3) {Karanlık};\node[font=\small,anchor=south] at (axis cs:21,0.3) {Karanlık};',
       r'\end{axis}']
    return tk('\n'.join(b),.95)
SK8=sk8()
# ============================ SORU 9 · CO2 kesilince ara ürünler ============================
def sk9():
    b=[r'\begin{axis}[width=7.8cm,height=5.2cm,xmin=0,xmax=10,ymin=0,ymax=10,xtick={0,3,10},xticklabels={0,CO$_2$ kesildi,10},ytick=\empty,axis lines=left,xlabel={Zaman},ylabel={Madde miktarı},tick label style={font=\footnotesize},label style={font=\small},every axis plot/.append style={line width=1.6pt}]',
       r'\addplot[black!50,dashed,line width=.9pt] coordinates {(3,0)(3,10)};',
       r'\addplot[black,smooth] coordinates {(0,4)(3,4)(4,6)(5,7.4)(6,8.2)(8,8.9)(10,9.2)};',
       r'\addplot[vurgu,smooth] coordinates {(0,8)(3,8)(4,4.6)(5,2.7)(6,1.6)(8,.8)(10,.5)};',
       r'\node[font=\small\bfseries,anchor=north] at (axis cs:9.2,7.4) {K};\node[font=\small\bfseries,vurgu,anchor=south] at (axis cs:9.2,.8) {L};',r'\end{axis}']
    return tk('\n'.join(b),.95)
SK9=sk9()
# ============================ SORU 10 · iki fotosentez denklemi ============================
from collections import Counter as C_
def atom(d):
    t=C_()
    for k,v in d.items(): t[k]+=v
    return t
CO2={'C':1,'O':2}; H2O={'H':2,'O':1}; H2S={'H':2,'S':1}; GLU={'C':6,'H':12,'O':6}; O2={'O':2}; S1={'S':1}
def topla(lst):
    t=C_()
    for n,m in lst:
        for k,v in m.items(): t[k]+=n*v
    return t
X_SOL=[(6,CO2),(12,H2O)]; X_SAG=[(1,GLU),(6,O2),(6,H2O)]
Y_SOL=[(6,CO2),(12,H2S)]; Y_SAG=[(1,GLU),(12,S1),(6,H2O)]
assert topla(X_SOL)==topla(X_SAG) and topla(Y_SOL)==topla(Y_SAG)
# CO2 nin 12 O atomu: 6'sı glikoza, 6'sı H2O ya gider; O2 yalnız sudan (12 O atomu = 6 O2)
assert 6*CO2['O']==GLU['O']+6*H2O['O'] and 6*O2['O']==12*H2O['O']
def sk10():
    b=[r'\node[anchor=west,align=left] at (0,1.2) {\textbf{X} (alg): 6CO$_2$ + 12H$_2$O $\xrightarrow{\text{ışık}}$ C$_6$H$_{12}$O$_6$ + 6O$_2$ + 6H$_2$O};',
       r'\node[anchor=west,align=left] at (0,0) {\textbf{Y} (yeşil kükürt bakterisi): 6CO$_2$ + 12H$_2$S $\xrightarrow{\text{ışık}}$ C$_6$H$_{12}$O$_6$ + 12S + 6H$_2$O};']
    return tk('\n'.join(b),.68)
SK10=sk10()

# ============================ SORULAR ============================
# 01 · kolay · panaşlı yaprak
Q('1','den','kolay','şekilli','Nişasta deneyi','Klorofil ve ışığın fotosentez için gerekliliğini panaşlı yaprak ve folyo deneyinden yorumlar.',
  'Fotosentezin gerçekleşmesi için ışık enerjisinin soğurulması gerekir; ışığı soğuran pigment (klorofil) yoksa ya da ışık ulaşmıyorsa karbonhidrat sentezi olmaz.','Yeşil rengi görülen her bölgenin fotosentez yaptığını sanmak.','panaşlı yaprak ve folyo deneyi',
  metin='Karanlıkta bekletilerek nişastası tüketilmiş, yeşil ve beyaz bölgeleri olan bir yaprağın yeşil bölgesinin bir kısmı şekildeki gibi alüminyum folyo ile kaplanıyor. Yaprak birkaç saat güçlü ışıkta bırakıldıktan sonra folyo çıkarılıp iyot çözeltisiyle boyanıyor ve nişasta bulunan bölgeler mavi-mor renk alıyor. Şekilde I folyoyla kaplı yeşil bölgeyi, II açıkta kalan yeşil bölgeyi, III açıkta kalan beyaz bölgeyi göstermektedir.\nBuna göre, numaralı bölgelerin hangilerinde mavi-mor renk gözlenir?',
  dogru='Yalnız II',sira=MASTER[:5],
  yan=[('Yalnız I','I numaralı bölge yeşil olsa da folyoyla kaplı olduğundan ışık almaz; fotosentez yapamadığı için nişasta oluşmaz.','dikkat'),
       ('Yalnız III','III numaralı bölgede klorofil bulunmadığından ışık soğurulamaz ve nişasta oluşmaz; beyaz bölge yeşil bölgeyle karıştırılmış.','dikkat'),
       ('I ve II','II numaralı bölge doğru seçilmiş ancak I numaralı bölgenin folyo nedeniyle ışık almadığı gözden kaçmıştır.','dikkat'),
       ('I ve III','Her iki bölgede de fotosentez için gerekli bir koşul eksiktir: I de ışık, III te klorofil yoktur; ikisi birlikte seçilmiş.','bilgi')],
  istenen='Nişasta oluşan (mavi-mor renk veren) bölgeler.',
  ip=['Her bölgede fotosentez için gereken iki koşulun, ışık alma ve ışığı soğuran pigment bulundurma, sağlanıp sağlanmadığına bak.'],
  bilgi=[B('Fotosentezin koşulları','fotosentez için ışık, CO₂, su ve ışığı soğuran pigment gerekir · fazla glikoz bitkilerde nişasta olarak depolanır'),
         B('İyot çözeltisi','nişastayı mavi-mor renge boyar; bu yüzden nişasta varlığını göstermek için kullanılır')],
  ad=[A('Bölgeleri koşullara göre tara','I: klorofil var, ışık yok · II: klorofil var, ışık var · III: klorofil yok, ışık var.','I: ışık yok · II: ikisi de var · III: klorofil yok'),
      A('Fotosentez koşulunu uygula','Fotosentezin gerçekleşmesi için hem ışık hem klorofil gerekir; yalnız ikisinin birlikte bulunduğu bölge fotosentez yapar.','Yalnız II'),
      A('Nişasta bulgusuna çevir','Fotosentez yapan bölgede glikoz nişastaya çevrilir ve iyotla mavi-mor renk görülür.','Mavi-mor: II')],
  puf='Yeşil görünmek yetmez; ışık da alınmalıdır. Işık ve klorofilin ikisi de aranır.',sekil=SK1)

# 02 · kolay · renkli ışık
d2='K ve M nin fotosentez hızı, L nin fotosentez hızından yüksektir.'
o2=['Üç bitkinin fotosentez hızı eşittir.','L nin fotosentez hızı, K ve M nin fotosentez hızından yüksektir.','L nin fotosentez hızı, M nin fotosentez hızından yüksektir.','K ve L nin fotosentez hızı, M nin fotosentez hızından yüksektir.']
Q('2','pig','kolay','şekilli','Işığın rengi','Klorofilin yeşil ışığı az, mavi ve kırmızı ışığı çok soğurduğunu bitkilerin fotosentez hızına uygular.',
  'Fotosentez hızı klorofil ve diğer pigmentlerin soğurduğu ışık miktarıyla ilişkilidir; yeşil ışık büyük ölçüde yansıtıldığı için en az etkilidir.','Işığın şiddeti eşit olunca her renkte aynı hızın beklendiğini düşünmek.','mavi, yeşil ve kırmızı ışıkta üç bitki',
  metin='Aynı türden, özdeş saksı ve toprakta yetişen K, L ve M bitkileri, şekilde gösterildiği gibi eşit şiddette ve farklı renkte ışık veren birer lamba ile aynı süre aydınlatılıyor. Bitkilerin diğer tüm yaşam koşulları ortaktır.\nBuna göre, bu bitkilerin fotosentez hızlarıyla ilgili aşağıdakilerden hangisi doğrudur?',
  dogru=d2,sira=yer('C',d2,o2),
  yan=[(o2[0],'Işık şiddeti eşit olsa da pigmentler farklı dalga boylarını farklı düzeyde soğurur; hızlar eşit olmaz.','bilgi'),
       (o2[1],'Yeşil ışık klorofil tarafından en az soğurulduğundan L bitkisinin hızı en düşüktür; en yüksek olması yanlıştır.','dikkat'),
       (o2[2],'Yeşil ışık kırmızı ışıktan daha az soğurulur; bu nedenle L nin hızı M ninkinden düşüktür.','dikkat'),
       (o2[3],'L bitkisi yeşil ışıkta olduğundan hızı M ninkinden düşüktür; bu yüzden K ve L nin birlikte M den yüksek olması yanlıştır.','dikkat')],
  istenen='Fotosentez hızları için doğru ifade.',
  ip=['Klorofilin hangi renkteki ışığı çok, hangi renkteki ışığı az soğurduğunu düşün.'],
  bilgi=[B('Klorofil ve ışık','klorofil mavi-mor ve kırmızı ışığı çok, yeşil ışığı çok az soğurur · yeşil ışık büyük ölçüde yansıtılır'),
         B('Hız ve soğurma','birim zamanda soğurulan ışık enerjisi arttıkça, ışık dışındaki faktörler sınırlayıcı olmadığı sürece fotosentez hızı artar')],
  ad=[A('Işık renklerini soğurmaya çevir','Mavi ve kırmızı ışık iyi soğurulur; yeşil ışık çok az soğurulur.','K, M: çok · L: az'),
      A('Hızlara aktar','Soğurulan ışık fazla olan bitkilerde fotosentez hızı da yüksektir; L en düşüktür.','L < K ve L < M'),
      A('İfadeyi seç','K ve M nin L den yüksek olduğunu söyleyen ifade doğrudur; K ile M arasında sıra belirtilmemiştir.','K, M > L')],
  puf='Yaprak yeşil görünür çünkü yeşil ışığı yansıtır; yansıttığı ışık fotosentezde en az kullanılır.',sekil=SK2)

# 03 · orta · olumsuz · yaprak kesiti
d3='I'; o3=['II','III','IV','II ve III']
Q('3','klo','orta','şekilli','Yaprak hücreleri ve kloroplast','Yaprak kesitinde hangi hücrelerin kloroplast taşıdığını ayırt eder.',
  'Kloroplast, yapraktaki fotosentez yapan hücrelerde bulunur; yaprağın koruyucu örtü dokusundaki sıradan hücrelerde bulunmaz, ancak stomayı çevreleyen bekçi hücreleri bu açıdan farklıdır.','Yaprağın tüm hücrelerinin ya da epidermisin tamamının kloroplast taşıdığını sanmak.','yaprak enine kesiti',
  metin='Şekilde bir bitki yaprağının enine kesiti şematik olarak verilmiş ve bazı hücreleri I, II, III ve IV ile numaralandırılmıştır.\nBuna göre, numaralı hücrelerden hangisinde ışığa bağımlı tepkimeler gerçekleşmez?',
  dogru=d3,sira=yer('A',d3,['II','III','IV','II ve III']),
  yan=[('II','II numaralı palizat hücrelerinde çok sayıda kloroplast bulunur; ışığa bağımlı tepkimeler burada gerçekleşir.','dikkat'),
       ('III','III numaralı sünger parankima hücreleri de kloroplast taşır; ışığa bağımlı tepkimeler burada da gerçekleşir.','dikkat'),
       ('IV','IV numaralı stoma bekçi hücreleri epidermisin diğer hücrelerinden farklı olarak kloroplast taşır; tepkimeler burada gerçekleşir.','bilgi'),
       ('II ve III','Her iki doku da kloroplast taşıdığından ışığa bağımlı tepkimeler ikisinde de gerçekleşir; bu seçenek yanlıştır.','dikkat')],
  istenen='Işığa bağımlı tepkimelerin gerçekleşmediği hücre.',
  ip=['Şekildeki dokuları biçimlerinden tanı ve her birinin fotosentez yapıp yapmadığını düşün.'],
  bilgi=[B('Yaprağın dokuları','üst ve alt epidermis koruyucu örtü dokusudur · palizat ve sünger parankima fotosentez yapan temel dokulardır'),
         B('Işığa bağımlı tepkimeler','kloroplastın tilakoit zarlarında gerçekleşir; kloroplast bulunmayan hücrede bu tepkimeler olmaz')],
  ad=[A('Dokuları tanı','I: üst epidermis · II: palizat parankiması · III: sünger parankima · IV: stoma bekçi hücreleri.','I epidermis · II palizat · III sünger · IV bekçi'),
      A('Kloroplast varlığını tara','Palizat, sünger ve bekçi hücreleri kloroplast taşır; epidermisin sıradan hücreleri taşımaz.','II, III, IV: var · I: yok'),
      A('Olumsuz kökü uygula','Işığa bağımlı tepkimelerin gerçekleşmediği hücre kloroplastsız olan I dir.','Cevap: I')],
  puf='Bekçi hücreleri epidermis içinde olsa da kloroplastlıdır; epidermisin diğer hücreleri kloroplastsızdır.',sekil=SK3)

# 04 · orta · öncüllü · KOH düzeneği
pre4=[('L düzeneğindeki yaprak iyot çözeltisiyle boyandığında mavi-mor renk gözlenir.',True,'L de CO₂ vardır ve ışıkta fotosentez sonucu nişasta birikir'),
      ('K düzeneğindeki yaprakta CO₂ bulunmadığından karbonhidrat sentezi yapılamaz ve nişasta oluşmaz.',True,'KOH çözeltisi CO₂ yi tutar, Calvin döngüsü için karbon kaynağı kalmaz'),
      ('Bu deneyde bağımsız değişken ışık şiddetidir.',False,'iki düzenekte de ışık aynıdır; farklı olan CO₂ varlığıdır')]
s4,sr4,d4,y4,i4=oncul(pre4,'C')
Q('4','den','orta','öncüllü','CO₂ gerekliliği deneyi','CO₂ tutucu madde içeren düzenekle CO₂ nin fotosentez için gerekliliğini yorumlar ve bağımsız değişkeni belirler.',
  'Bir deneyde yalnız incelenen faktör değiştirilir; aynı koşulların sağlandığı düzenek kontrol grubudur. CO₂ yi tutan bir madde ortamda CO₂ bulunmamasını sağlar.','Deneydeki tüm farkların bağımsız değişken olduğunu düşünmek.','KOH ve su içeren iki düzenek',
  metin='Karanlıkta bekletilerek nişastası tüketilmiş, aynı türden iki yaprak, şekildeki K ve L fanuslarına yerleştiriliyor. K de CO₂ yi tutan KOH çözeltisi, L de su bulunuyor. İki düzenek de aynı güçlü ışıkta aynı süre bekletildikten sonra yapraklar iyot çözeltisiyle boyanıyor ve nişasta bulunan yaprak mavi-mor renk alıyor.\n'+s4+'\nBuna göre, yukarıdaki ifadelerden hangileri doğrudur?',
  dogru=d4,sira=sr4,yan=y4,istenen='Doğru olan öncüller.',
  ip=['İki düzenek arasındaki tek farkın ne olduğunu belirle; sonra her düzende fotosentezin sürüp sürmeyeceğine bak.'],
  bilgi=[B('Deney tasarımı','bağımsız değişken deneyde bilinçli olarak değiştirilen, bağımlı değişken ölçülen faktördür · diğer faktörler iki düzenekte aynı tutulur'),
         B('Fotosentez girdileri','karbonhidrat sentezi için ışık, su ve CO₂ gerekir')],
  ad=[A('Düzenekleri karşılaştır','Işık ve yaprak aynıdır; fark ortamda CO₂ bulunup bulunmamasıdır.','Fark: CO₂ (K yok, L var)'),
      A('L yi değerlendir','L de CO₂ vardır, ışık da vardır; fotosentez ve nişasta birikimi olur, iyotla mavi-mor renk görülür.','I: doğru'),
      A('K yi değerlendir','K de KOH CO₂ yi tuttuğundan karbonhidrat sentezi yapılamaz, nişasta oluşmaz.','II: doğru'),
      A('Bağımsız değişkeni belirle','Bağımsız değişken CO₂ varlığıdır; ışık şiddeti iki düzenekte aynıdır.','III: yanlış')],
  puf='Bağımsız değişken, iki düzenek arasında bilerek değiştirilen tek faktördür.',sekil=SK4)

# 05 · orta · olumsuz · tablo
d5='1 ve 3 numaralı ortamların sonuçları karşılaştırılarak CO₂ derişiminin hıza etkisi kesin olarak belirlenebilir.'
o5=['1 ve 2 numaralı ortamlar karşılaştırıldığında, 1 numaralı ortamda ışık şiddetinin fotosentez hızını sınırladığı söylenebilir.',
    '2 ve 3 numaralı ortamlar karşılaştırıldığında, 3 numaralı ortamda CO₂ derişiminin fotosentez hızını sınırladığı söylenebilir.',
    '2 ve 4 numaralı ortamlar karşılaştırıldığında, 4 numaralı ortamda sıcaklığın fotosentez hızını sınırladığı söylenebilir.',
    '4 numaralı ortamda sıcaklık 25 °C’a çıkarılırsa, fotosentez hızının 2 numaralı ortamdaki değere yaklaşması beklenir.']
Q('5','fak','orta','tablo','Sınırlayıcı faktör','Tablodaki ortamlarda yalnız bir faktör farklı olan çiftleri seçerek sınırlayıcı faktörü yorumlar.',
  'Bir faktörün etkisi, yalnız o faktörün farklı olduğu iki ortamın karşılaştırılmasıyla belirlenir; birden çok faktör birlikte değişirse hız farkı tek faktöre bağlanamaz.','Birkaç faktörün birlikte değiştiği karşılaştırmalardan tek faktörlü sonuç çıkarmak.','ışık, CO₂ ve sıcaklık tablosu',
  metin='Aynı türden eş bitkiler, ışık şiddeti, CO₂ derişimi ve sıcaklığı farklı dört ortamda yetiştirilmiş; fotosentez hızları (birim zamanda üretilen O₂ miktarı) tabloda verilmiştir. Diğer koşullar tüm ortamlarda aynıdır.\nBuna göre, aşağıdaki çıkarımlardan hangisi yanlıştır?',
  dogru=d5,sira=yer('E',d5,o5),
  yan=[(o5[0],'1 ve 2 numaralı ortamlarda yalnız ışık şiddeti farklıdır; hız 2 ile 8 olduğundan ifade doğrudur ve yanlış sanılarak seçilmiş.','dikkat'),
       (o5[1],'2 ve 3 numaralı ortamlarda yalnız CO₂ derişimi farklıdır; hız 8 den 3 e düştüğünden ifade doğrudur.','dikkat'),
       (o5[2],'2 ve 4 numaralı ortamlarda yalnız sıcaklık farklıdır; hız 8 den 4 e düştüğünden ifade doğrudur.','dikkat'),
       (o5[3],'Diğer faktörler 2 numaralı ortamla aynı olduğundan sıcaklığı 25 °C a çıkarmak hızı 2 numaralı ortamdaki değere yaklaştırır; ifade doğrudur.','bilgi')],
  istenen='Tabloya göre yanlış olan çıkarım.',
  ip=['Her çıkarımda karşılaştırılan iki ortamın hangi faktörlerde ayrıldığına bak.'],
  bilgi=[B('Sınırlayıcı faktör','fotosentez hızını, ihtiyaç duyulan faktörlerden minimumda olan belirler; o faktör artırılınca hız artar'),
         B('Kontrollü karşılaştırma','bir faktörün etkisi, yalnız o faktörün değiştiği ortamların karşılaştırılmasıyla belirlenir')],
  ad=[A('Ortam çiftlerini tara','1–2: yalnız ışık · 2–3: yalnız CO₂ · 2–4: yalnız sıcaklık · 1–3: hem ışık hem CO₂.','1–3: iki faktör birlikte değişiyor'),
      A('Tek faktörlü çiftleri yorumla','Düşük ışık, düşük CO₂ ve düşük sıcaklık, hızı ilgili ortamda sınırlamıştır; bu üç çıkarım doğrudur.','A, B, C doğru'),
      A('Çift faktörlü çifti değerlendir','1 ve 3 te iki faktör birden farklı olduğundan hız farkı CO₂ ye tek başına bağlanamaz.','1 ve 3: çıkarım geçersiz'),
      A('Yanlışı seç','CO₂ etkisinin 1 ve 3 ten kesin belirlendiğini söyleyen çıkarım yanlıştır.','Yanlış: 1 ve 3 çıkarımı')],
  puf='Birden fazla faktör farklıysa nedeni tek faktöre bağlayamazsın; yalnız bir faktörün farklı olduğu çifti ara.',sekil=SK5)

# 06 · orta · gaz alışverişi durumları
o6=MASTER[:5]
Q('6','fak','orta','şekilli','Fotosentez ve solunum dengesi','Bitki hücresindeki gaz alışverişini ok şemasından okuyup fotosentez ve solunum hızlarını karşılaştırır.',
  'Hücrenin dışa verdiği ya da dışarıdan aldığı gaz, fotosentez ve solunum hızları arasındaki farkı gösterir; iki hız eşitse gaz alışverişi hücre içinde karşılanır.','Dışarıdan O₂ alınan hücrede de fotosentezin solunumdan hızlı olduğunu düşünmek.','kloroplast ve mitokondri gaz akışı',
  metin='Şekilde, ışıklı bir ortamdaki üç yaprak hücresinde (I, II ve III) kloroplast ile mitokondri arasındaki ve hücre ile dış ortam arasındaki O2 ve CO2 akışları oklarla gösterilmiştir. Hücrelerde başka O2 ve CO2 kaynağı ya da tüketimi yoktur.\nBuna göre, hangi hücre(ler)de fotosentez hızı hücresel solunum hızından büyüktür?',
  dogru='Yalnız II',sira=o6,
  yan=[('Yalnız I','I de dış ortamla gaz alışverişi yoktur; kloroplastın ürettiği O₂ tamamen solunumda kullanılır, yani iki hız eşittir.','dikkat'),
       ('Yalnız III','III te hücre dışarıdan O₂ alıp CO₂ verir; bu durumda solunum hızı fotosentez hızından büyüktür.','dikkat'),
       ('I ve II','II doğru seçilmiş; ancak I de gaz alışverişi hücre içinde dengelendiğinden fotosentez ve solunum hızları eşittir.','bilgi'),
       ('I ve III','I de hızlar eşittir, III te solunum hızı büyüktür; hiçbirinde fotosentez hızı solunum hızından büyük değildir.','dikkat')],
  istenen='Fotosentez hızı solunum hızından büyük olan hücre(ler).',
  ip=['Hücrenin dış ortama net olarak hangi gazı verdiğine bak ve bunu iki olayın hızlarıyla ilişkilendir.'],
  bilgi=[B('Fotosentez ve solunum gazları','fotosentez CO₂ tüketip O₂ üretir, hücresel solunum O₂ tüketip CO₂ üretir'),
         B('Net gaz alışverişi','iki hız arasındaki fark, hücrenin dış ortamla yaptığı net gaz alışverişini belirler')],
  ad=[A('Dış ortam oklarını oku','I: dış ok yok · II: dışarıya O₂ verilir, dışarıdan CO₂ alınır · III: dışarıdan O₂ alınır, dışarıya CO₂ verilir.','I: net 0 · II: O₂ çıkışı · III: O₂ girişi'),
      A('Hızları karşılaştır','Dışarıya O₂ verilmesi, üretilen O₂ nin tüketilenden fazla olduğunu, yani fotosentez hızının büyük olduğunu gösterir.','II: fotosentez > solunum'),
      A('Diğer hücreleri yorumla','I de iki hız eşit, III te solunum hızı büyüktür.','I: eşit · III: solunum > fotosentez')],
  puf='Dışarıya net O₂ veren hücrede fotosentez hızı solunum hızından büyüktür.',sekil=SK6)

# 07 · orta · öncüllü · kemosentez
pre7=[('Kükürt bakterileri, H₂S nin yükseltgenmesiyle açığa çıkan enerjiyi organik madde sentezinde kullanır.',True,'kemosentezde enerji inorganik maddelerin yükseltgenmesinden sağlanır'),
      ('Kükürt bakterilerinin organik madde sentezi, ışık enerjisi gerektiğinden ışıksız ortamda gerçekleşemez.',False,'kemosentez ışığa bağımlı değildir, ışıksız ortamda sürebilir'),
      ('Kükürt bakterileri karbon kaynağı olarak CO₂ yi kullanabilir ve kendi besinlerini üretebildiklerinden ototroftur.',True,'kemosentez yapanlar CO₂ den organik madde sentezleyen ototroflardır')]
s7,sr7,d7,y7,i7=oncul(pre7,'D')
Q('7','kem','orta','öncüllü','Kükürt bakterileri','Kemosentez yapan bir bakterinin enerji kaynağını, ışık gereksinimini ve beslenme türünü değerlendirir.',
  'Kemosentezde organik madde sentezinin enerjisi ışıktan değil, inorganik maddelerin yükseltgenmesinden gelir; bu canlılar da CO₂ den besin ürettiği için ototroftur.','Her ototrofun ışık enerjisiyle besin ürettiğini düşünmek.','kükürt bakterisi kemosentezi',
  metin='Derin deniz tabanındaki hidrotermal bacaların çevresinde yaşayan bazı kükürt bakterileri, ortamdaki H2S yi yükseltgeyerek enerji elde eder ve bu enerjiyle CO2 ve H2O den organik madde sentezler. Bu bölgeye güneş ışığı ulaşmamaktadır.\n'+s7+'\nBuna göre, yukarıdaki ifadelerden hangileri doğrudur?',
  dogru=d7,sira=sr7,yan=y7,istenen='Doğru olan öncüller.',
  ip=['Bu bakterinin enerji kaynağını, ışığa gereksinimi olup olmadığını ve karbon kaynağını ayrı ayrı sorgula.'],
  bilgi=[B('Kemosentez','bazı bakterilerin inorganik maddeleri yükseltgeyerek elde ettiği enerjiyle CO₂ den organik madde sentezlemesidir'),
         B('Ototrof beslenme','inorganik maddelerden kendi organik besinini üretebilen canlıların beslenme biçimidir')],
  ad=[A('Enerji kaynağını belirle','Bakteri H₂S yi yükseltgeyerek enerji elde eder; bu enerji organik madde sentezinde kullanılır.','I: doğru'),
      A('Işık gereksinimini sorgula','Ortama ışık ulaşmadığı hâlde sentez sürüyor; süreç ışığa bağımlı değildir.','II: yanlış'),
      A('Beslenme türünü belirle','Bakteri karbonu CO₂ den alıp organik madde üretir; ototroftur.','III: doğru')],
  puf='Kemosentezde enerji ışıktan değil, inorganik maddelerin yükseltgenmesinden gelir.')

# 08 · zor · gün boyu net CO2
Q('8','fak','zor','grafik','Günlük karbonhidrat bütçesi','Net CO₂ grafiğinden aydınlık ve karanlık sürelerde net alımı ve solunumu birleştirip günlük net glikoz birikimini hesaplar.',
  'Net CO₂ alımı, fotosentezle alınan ile solunumla verilen CO₂ arasındaki farktır; günlük birikim için bütün süredeki net değişim, stokiyometri ile glikoza çevrilir.','Yalnız aydınlık süredeki net alımı ya da brüt fotosentezi günlük net birikim sanmak.','24 saatlik net CO₂ grafiği',
  metin='Bir bitkinin 24 saat boyunca birim zamanda yaptığı net CO2 alışverişi şekildeki grafikte verilmiştir. Pozitif değerler ortamdan CO2 alındığını, negatif değerler ortama CO2 verildiğini gösterir. Hücresel solunum hızı 24 saat boyunca sabittir ve fotosentezle üretilen glikoz dışında bir glikoz kaynağı yoktur. 6 birim CO2 ile 1 birim glikoz sentezlendiği kabul edilecektir.\nBuna göre, bitkide bu 24 saatte net kaç birim glikoz birikmiştir?',
  dogru=4,yan=[(12,f'Yalnız aydınlık süredeki net CO₂ alımı glikoza çevrilmiş (6 × 12 = 72; 72 / 6 = 12); karanlıkta solunumla verilen CO₂ hesaba katılmamıştır.','islem'),
       (20,f'Brüt fotosentez bulunmuş ((6 + 4) × 12 = 120; 120 / 6 = 20); 24 saatlik solunumla yıkılan glikoz düşülmemiştir.','islem'),
       (8,f'Karanlık süredeki CO₂ kaybı glikoza çevrilmiş (4 × 12 = 48; 48 / 6 = 8); fotosentezle kazanılan miktar hesaba katılmamıştır.','islem'),
       (24,f'Net CO₂ miktarı bulunmuş (72 − 48 = 24) ancak 6 birim CO₂ nin 1 birim glikoz verdiği dönüşüm yapılmamıştır.','islem')],
  istenen='24 saatte net glikoz birikimi (birim).',
  ip=['Grafikteki iki farklı süreyi ayrı ayrı hesapla; sonra net CO₂ değişimini glikoz birimine çevir.'],
  bilgi=[B('Net gaz alışverişi','aydınlıkta ölçülen net CO₂ alımı, fotosentez ile solunum hızları arasındaki farktır · karanlıkta yalnız solunum vardır'),
         B('Glikoz sentezi','6 CO₂ den 1 glikoz sentezlenir; birimler arası dönüşümde bu oran kullanılır')],
  ad=[A('Aydınlık süre','Aydınlık 6. ile 18. saat arasında 12 saat sürer; net alım 6 × 12 = 72 birim CO₂.','6 × 12 = 72'),
      A('Karanlık süre','Karanlık süre 12 saattir; solunumla 4 × 12 = 48 birim CO₂ verilir.','4 × 12 = 48'),
      A('Net CO₂ i bul','24 saatte net CO₂ alımı 72 − 48 = 24 birimdir.','72 − 48 = 24'),
      A('Glikoza çevir','6 birim CO₂ 1 birim glikoz verdiğinden 24 / 6 = 4 birim glikoz birikir.','24 / 6 = 4')],
  puf='Önce süreyi ve hızı çarp, net CO₂ yi bul; en sonda 6 ya böl.',sekil=SK8)

# 09 · zor · öncüllü · CO2 kesilince
pre9=[('K eğrisi RuBP, L eğrisi PGA miktarındaki değişimi göstermektedir.',True,'CO₂ kesilince RuBP e CO₂ bağlanamaz: RuBP birikir, PGA azalır'),
      ('CO₂ kesildikten sonra PGAL oluşum hızı azalır.',True,'PGA azalınca PGAL e dönüşecek madde kalmaz'),
      ('CO₂ kesildikten sonra stromada NADP⁺ miktarı artar.',False,'PGAL e dönüşüm yavaşlayınca NADPH harcanmaz, NADP⁺ azalır')]
s9,sr9,d9,y9,i9=oncul(pre9,'D')
Q('9','cal','zor','öncüllü','CO₂ kesilmesi ve Calvin döngüsü','CO₂ kaynağı kesilince Calvin döngüsü ara ürünlerindeki ve ışığa bağımlı evre ürünlerindeki değişimi birlikte yorumlar.',
  'Calvin döngüsünde CO₂ RuBP ye bağlanarak PGA oluşturur; CO₂ kesilirse bu basamak durur ve bunun sonuçları döngü ile ATP ve NADPH tüketimine yansır.','CO₂ eksikliğinde ışığa bağımlı evre ürünlerinin tüketiminde de bir değişiklik olmayacağını sanmak.','CO₂ kesilince RuBP ve PGA',
  metin='Işık altındaki yeşil alg hücrelerinin bulunduğu ortamda, şekildeki işaretli anda CO2 girişi durduruluyor; ışık ve diğer koşullar değişmiyor. Bu hücrelerde Calvin döngüsünün iki ara ürünü olan RuBP ve PGA miktarlarındaki değişim K ve L eğrileriyle gösterilmiştir.\n'+s9+'\nBuna göre, yukarıdaki ifadelerden hangileri doğrudur?',
  dogru=d9,sira=sr9,yan=y9,istenen='Doğru olan öncüller.',
  ip=['CO₂ nin döngüde hangi maddeyle birleşerek hangi maddeyi oluşturduğunu düşün; bu basamak durunca diğer basamaklara ne olur?'],
  bilgi=[B('Calvin döngüsünün basamakları','CO₂ RuBP ye bağlanır ve PGA oluşur · PGA, ATP ve NADPH kullanılarak PGAL e çevrilir · PGAL nin bir bölümüyle RuBP yeniden oluşur'),
         B('Işığa bağımlı evre ürünleri','ATP ve NADPH Calvin döngüsünde harcanır; harcama azalırsa ADP ve NADP⁺ yeniden oluşumu da azalır')],
  ad=[A('Ara ürünlerin yönünü belirle','CO₂ olmayınca RuBP PGA ya çevrilemez; RuBP birikir, PGA azalır.','K ↑ RuBP · L ↓ PGA'),
      A('PGAL sentezini yorumla','PGA miktarı azaldıkça PGAL e dönüşen madde de azalır; PGAL oluşumu yavaşlar.','II: doğru'),
      A('NADPH tüketimini yorumla','PGAL oluşumu yavaşlayınca NADPH harcanmaz; NADP⁺ miktarı artmaz, azalır.','III: yanlış'),
      A('Öncülleri birleştir','I ve II doğru, III yanlıştır.','I ve II')],
  puf='CO₂ yoksa PGA oluşmaz; sonrasındaki basamaklar da onu izler.',sekil=SK9)

# 10 · zor · öncüllü · 18O iki denklem
pre10=[('X te açığa çıkan O₂ gazı işaretli oksijen içerir.',False,'O₂ suyun fotolizinden gelir, işaretli olan CO₂ nin oksijeni O₂ ye geçmez'),
       ('X te denklemin ürünlerinden olan H₂O işaretli oksijen içerir.',True,'CO₂ nin 12 oksijen atomundan 6 sı glikoza, 6 sı H₂O ya geçer'),
       ('Y de sentezlenen glikoz işaretli oksijen içerir.',True,'glikozun oksijen atomları CO₂ den gelir')]
s10,sr10,d10,y10,i10=oncul(pre10,'E')
Q('10','kem','zor','öncüllü','Denklemlerde atom izleme','İki farklı fotosentez denkleminde işaretli oksijenin hangi ürünlere geçtiğini atom sayımıyla izler.',
  'Genel fotosentez denklemlerinde ürünlerdeki her atom girenlerden gelir; oksijenin kaynağı, atomların denklemdeki dağılımı izlenerek bulunur.','Ürün olarak yazılan her H₂O nin ve O₂ nin aynı kaynaktan geldiğini düşünmek.','iki farklı fotosentez denklemi',
  metin='Işık enerjisiyle organik madde sentezleyen X (alg) ve Y (yeşil kükürt bakterisi) canlılarında gerçekleşen olayların genel denklemleri şekilde verilmiştir. İki canlıya da oksijen atomları 18O ile işaretlenmiş CO2 veriliyor; su ve H2S işaretsizdir.\n'+s10+'\nBuna göre, yukarıdaki ifadelerden hangileri doğrudur?',
  dogru=d10,sira=sr10,yan=y10,istenen='Doğru olan öncüller.',
  ip=['İşaretli oksijenin hangi girenden başladığını belirle ve ürünlerdeki oksijen atomlarının kaynağını denklemde tek tek izle.'],
  bilgi=[B('Atomların izlenmesi','kimyasal tepkimede girenlerin atomları ürünlere dağılır; yeni atom oluşmaz · işaretli atomlar hangi ürünlerde bulunabileceği denklemden bulunur'),
         B('Oksijenli ve oksijensiz fotosentez','suyun hidrojen kaynağı olduğu fotosentezde O₂ açığa çıkar; H₂S gibi başka kaynak kullanıldığında O₂ yerine başka bir ürün çıkar')],
  ad=[A('X te oksijenin kaynağı','X te O₂ suyun parçalanmasından gelir; işaretli oksijen CO₂ de olduğundan O₂ işaretsizdir.','I: yanlış'),
      A('X te CO₂ nin oksijenleri','6 CO₂ de 12 oksijen vardır; 6 sı glikoza geçer, kalan 6 sı ürün H₂O ya gider.','II: doğru'),
      A('Y de glikozun oksijenleri','Glikozun 6 oksijeni CO₂ den gelir; Y de CO₂ işaretlidir.','III: doğru'),
      A('Öncülleri birleştir','II ve III doğru, I yanlıştır.','II ve III')],
  puf='Ürünlerdeki oksijen atomlarını girenlerle eşleştirerek say; O₂ nin kaynağı sudur.',sekil=SK10)

# ============================ YAZ ============================
assert len(P.ANA)==10
Z=Counter(q['zorluk'] for q in P.ANA); assert Z=={'kolay':2,'orta':5,'zor':3},Z
HR=Counter(q['cevap']['sik'] for q in P.ANA); assert all(HR[h]==2 for h in 'ABCDE'),HR
assert 4<=len({q['tipId'] for q in P.ANA})<=6
SEK=sum(1 for q in P.ANA if q['sekil']); assert SEK>=6,SEK
for q in P.ANA: q['kardes']=None
P.yaz(os.path.join(GD,'fotosenteziki-1.json'),'/tmp/claude-0/sp/bos-fotosenteziki.json')
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=KEY))['kartlar'].append(c['id'])
json.dump(dict(konu=KONU_AD,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2018–2026 Biyoloji (yalnız mantık), MEB 12. sınıf.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','abfotosenteziki.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler),'şekil',SEK)
