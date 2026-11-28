"""AYT Biyoloji · Bitki Biyolojisi · 2. dalga · 10 soru. Kardeş yok, ipucu 1.
Şekiller TikZ/pgfplots; tüm değerler tek yerde tanımlanır, doğru şık ve çeldiriciler assert edilir."""
import sys,os,json,math
from collections import Counter
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-bio'))
import _hafif_bio as H
from _hafif_bio import *
KONU_AD='Bitki Biyolojisi'; KEY='abio|Bitki Biyolojisi'
P=Parti('bitkiiki',KONU_AD,KEY,ders='AYT Biyoloji',idon='aytbio'); H.KONU=KONU_AD
KAYNAK='ÖSYM AYT 2018–2026 Biyoloji bitki biyolojisi soruları (yalnız mantık) · MEB 11. sınıf Bitki Biyolojisi'
TIP={'buy':('bt2-buyume','Primer büyüme ve kök ucu'),
     'dok':('bt2-doku','Dokular ve sekonder büyüme'),
     'ure':('bt2-ureme','Tohum, döllenme ve meyve'),
     'hor':('bt2-hormon','Bitki hormonları ve tepkiler'),
     'tas':('bt2-tasima','Su ve mineral alımı')}
def Q(no,tp,z,kalip,alt,kaz,fikir,tuzak,ozet,ad,**k):
    t,tn=TIP[tp]; H.kart(f'K-ABBIT2-{no}',alt,fikir,tuzak,z,kalip,len(ad),t,tn,KAYNAK)
    assert len(k['ip'])==1
    mk(P,no.zfill(4),ad=ad,adim=len(ad),tipId=t,tip=tn,z=z,alt=alt,kaz=kaz,kalip=kalip,kart=f'K-ABBIT2-{no} ({ozet})',**k)
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
    return satir,sira,dogru,yan
def lab(t,x,y,x1,y1,x2,y2):
    return rf'\node[font=\large\bfseries] at ({x},{y}) {{{t}}};\draw[{OK},line width=.9pt] ({x1},{y1})--({x2},{y2});'

# ============ ŞEKİL 1 · kök ucu boyuna kesit ============
def sk1():
    b=[r'\begin{scope}\clip (-1.1,7.0)--(-1.1,1.1) arc(180:360:1.1)--(1.1,7.0)--cycle;',
       r'\fill[brown!35] (-1.2,-.1) rectangle (1.2,.95);\fill[yellow!40] (-1.2,.95) rectangle (1.2,2.3);\fill[green!25] (-1.2,2.3) rectangle (1.2,4.5);\fill[orange!20] (-1.2,4.5) rectangle (1.2,7.1);']
    y=1.0
    while y<2.3:
        b.append(rf'\draw[line width=.5pt] (-1.2,{y:.2f})--(1.2,{y:.2f});'); y+=.28
    x=-.84
    while x<1.0:
        b.append(rf'\draw[line width=.5pt] ({x:.2f},.95)--({x:.2f},2.3);'); x+=.28
    y=2.3
    while y<4.5:
        b.append(rf'\draw[line width=.5pt] (-1.2,{y:.2f})--(1.2,{y:.2f});'); y+=.55
    for x in (-.37,.37): b.append(rf'\draw[line width=.5pt] ({x},2.3)--({x},4.5);')
    y=4.5
    while y<7.1:
        b.append(rf'\draw[line width=.5pt] (-1.2,{y:.2f})--(1.2,{y:.2f});'); y+=1.2
    for x in (-.4,.4): b.append(rf'\draw[line width=.5pt] ({x},4.5)--({x},7.1);')
    b.append(r'\end{scope}')
    b.append(r'\draw[line width=1.4pt] (-1.1,7.0)--(-1.1,1.1) arc(180:360:1.1)--(1.1,7.0);')
    for y in (.95,2.3,4.5): b.append(rf'\draw[dashed,line width=.8pt] (-1.1,{y})--(1.1,{y});')
    for y in (4.9,5.7,6.5): b.append(rf'\draw[line width=1pt] (-1.1,{y})--(-1.8,{y+.15});')
    for y in (5.3,6.1,6.9): b.append(rf'\draw[line width=1pt] (1.1,{y})--(1.8,{y+.15});')
    b.append(lab('I',3.0,.5,2.6,.5,.5,.5)); b.append(lab('II',3.0,1.65,2.6,1.65,.5,1.65))
    b.append(lab('III',3.0,3.4,2.6,3.4,.5,3.4)); b.append(lab('IV',-3.0,5.3,-2.6,5.3,-.5,5.3))
    return tk('\n'.join(b),.78)
SK1=sk1()
# ============ ŞEKİL 2 · çift çenekli tohum ============
def sk2():
    b=[r'\draw[line width=1.6pt,fill=brown!35] (0,0) ellipse (3.2 and 2.0);',
       r'\draw[line width=.8pt,fill=white] (0,0) ellipse (2.95 and 1.75);',
       r'\draw[line width=1pt,fill=yellow!35] (0,-.15) ellipse (2.65 and 1.35);\draw[line width=.7pt] (-2.1,-.15)--(2.1,-.15);',
       r'\draw[line width=4pt,green!50!black] (-2.1,.7)--(-1.0,1.15);\fill[brown!70] (-2.1,.7)--(-2.55,.3)--(-2.35,.95)--cycle;',
       r'\draw[line width=.7pt,fill=green!60,rotate around={55:(-.85,1.3)}] (-.85,1.3) ellipse (.36 and .12);\draw[line width=.7pt,fill=green!60,rotate around={15:(-.7,1.2)}] (-.7,1.2) ellipse (.36 and .12);',
       lab('I',4.2,1.5,3.8,1.4,3.05,.5), lab('II',4.2,-1.4,3.8,-1.3,1.9,-.6),
       lab('III',-4.2,-.6,-3.8,-.5,-2.5,.35), lab('IV',-1.2,3.0,-1.0,2.7,-.8,1.5)]
    return tk('\n'.join(b),.85)
SK2=sk2()
# ============ ŞEKİL 3 · tablo giberellin ============
D3=[('K','Embriyolu yarım tohum','Su','Var'),('L','Embriyosuz yarım tohum','Su','Yok'),
    ('M','Embriyosuz yarım tohum','Giberellin','Var'),('N','Embriyolu yarım tohum','Absisik asit','Yok')]
SK3=tablo_svg(['Kap','Tohum parçası','Ortama eklenen','Nişasta yıkımı'],[list(r) for r in D3])
# ============ ŞEKİL 4 · grafik ABA / giberellin ============
ABA=[(0,9),(4,8),(8,5),(12,3),(16,2),(20,1.5)]; GA=[(0,1),(4,1),(8,2.5),(12,6),(16,8),(20,8.5)]
TC=12
da=dict(ABA); dg=dict(GA)
assert da[TC]<dg[TC] and da[0]>dg[0] and da[4]>dg[4] and dg[16]==4*da[16] and da[8]>da[12]>da[16] and dg[8]<dg[12]<dg[16]
def pts(l): return ''.join(f'({x},{y})' for x,y in l)
def sk4():
    b=[r'\begin{axis}[width=8.4cm,height=5.4cm,xmin=0,xmax=20,ymin=0,ymax=10,xtick={0,4,8,12,16,20},ytick={0,2,4,6,8,10},axis lines=left,xlabel={Zaman (gün)},ylabel={Hormon derişimi (göreli)},tick label style={font=\footnotesize},label style={font=\small},every axis plot/.append style={line width=1.6pt}]',
       rf'\addplot[black,smooth] coordinates {{{pts(GA)}}};',rf'\addplot[vurgu,smooth] coordinates {{{pts(ABA)}}};',
       rf'\addplot[black!50,dashed,line width=.9pt] coordinates {{({TC},0)({TC},10)}};',
       r'\node[font=\small\bfseries,anchor=south west] at (axis cs:17,8.6) {K};\node[font=\small\bfseries,vurgu,anchor=south] at (axis cs:18.2,2.0) {L};',
       rf'\node[font=\small,anchor=south east] at (axis cs:{TC-.3},9.0) {{Çimlenme başladı}};',r'\end{axis}']
    return tk('\n'.join(b),.95)
SK4=sk4()
# ============ ŞEKİL 5 · odunsu gövde enine kesit ============
W5=[.55,.5,.22,.5,.6,.45]; assert min(W5)==W5[2]
def sk5():
    b=[]; R=.4+sum(W5)+.1+.3+.25
    b.append(rf'\draw[line width=1.4pt,fill=brown!40] (0,0) circle ({R:.2f});')
    R2=R-.25; b.append(rf'\draw[line width=.8pt,fill=gray!30] (0,0) circle ({R2:.2f});')
    R3=R2-.3; b.append(rf'\draw[line width=1.2pt,fill=white] (0,0) circle ({R3:.2f});')
    R4=R3-.1; b.append(rf'\draw[line width=.8pt,fill=yellow!30] (0,0) circle ({R4:.2f});')
    r=R4
    for i in range(len(W5)-1,-1,-1):
        r-=W5[i] if i==len(W5)-1 else 0
    # halkalar dıştan içe
    rr=R4
    for i in range(len(W5)-1,-1,-1):
        fill='yellow!45' if i%2==0 else 'orange!25'
        b.append(rf'\draw[line width=.7pt,fill={fill}] (0,0) circle ({rr:.2f});'); rr-=W5[i]
    b.append(rf'\draw[line width=.7pt,fill=green!25] (0,0) circle ({rr:.2f});'); assert abs(rr-.4)<1e-9
    r1=.4+W5[0]/2; r3=.4+W5[0]+W5[1]+W5[2]/2; rk=R4+.05
    b.append(lab('I',-4.6,0,-4.2,0,-r1,0)); b.append(lab('II',4.6,0,4.2,0,r3,0))
    b.append(lab('III',4.6,3.3,4.2,3.0,rk*math.cos(math.radians(45)),rk*math.sin(math.radians(45))))
    return tk('\n'.join(b),.6)
SK5=sk5()
# ============ ŞEKİL 6 · tablo hücre ψ ============
HUC6={'K':(-1.0,.4),'L':(-1.2,.2),'M':(-.9,.6)}
PSI={k:round(a+b,1) for k,(a,b) in HUC6.items()}
assert PSI=={'K':-.6,'L':-1.0,'M':-.3}
assert PSI['M']>PSI['K']>PSI['L'] and HUC6['L'][0]<HUC6['K'][0]
SK6=tablo_svg(['Hücre','Osmotik potansiyel (MPa)','Turgor basıncı (MPa)'],[[k,f'{a:.1f}'.replace('.',',').replace('-','−'),f'{b:.1f}'.replace('.',',')] for k,(a,b) in HUC6.items()])
# ============ ŞEKİL 7 · klinostat ============
def sk7():
    b=[]
    b.append(r'\draw[line width=1.2pt] (-3,-1.6) rectangle (3,-1.1);\node[font=\small] at (0,-1.35) {Nemli ortam};')
    b.append(r'\fill[black!70] (0,0) circle (.14);')
    b.append(r'\draw[line width=2.4pt,brown!70!black] (0,0) .. controls (1,0) and (1.8,-.2) .. (2.3,-1.0);')
    b.append(r'\draw[line width=2.4pt,green!50!black] (0,0) .. controls (-1,0) and (-1.8,.3) .. (-2.3,1.2);')
    b.append(r'\node[font=\large\bfseries] at (0,-2.2) {K};\node[font=\small] at (0,-2.7) {Sabit};')
    b.append(r'\begin{scope}[xshift=7.5cm]')
    b.append(r'\draw[line width=2.4pt,brown!70!black] (0,0)--(2.3,0);\draw[line width=2.4pt,green!50!black] (0,0)--(-2.3,0);\fill[black!70] (0,0) circle (.14);')
    b.append(rf'\draw[{OK},line width=1pt,vurgu] (0,1.0) arc(90:-210:1.0);')
    b.append(r'\node[font=\large\bfseries] at (0,-2.2) {L};\node[font=\small] at (0,-2.7) {Yavaş dönüyor};\end{scope}')
    return tk('\n'.join(b),.62)
SK7=sk7()
# ============ ŞEKİL 8 · O2 – K+ alımı ============
KA=[(0,1),(5,5),(10,8),(15,9.5),(20,10),(30,10),(40,10)]; LA=[(0,1),(40,1)]
assert KA[0][1]==LA[0][1] and KA[4][1]==KA[5][1]==KA[6][1]
def sk8():
    b=[r'\begin{axis}[width=8.4cm,height=5.4cm,xmin=0,xmax=40,ymin=0,ymax=12,xtick={0,10,20,30,40},ytick={0,2,4,6,8,10},axis lines=left,xlabel={Ortamdaki O$_2$ derişimi (\%)},ylabel={K$^+$ alım hızı},tick label style={font=\footnotesize},label style={font=\small},every axis plot/.append style={line width=1.6pt}]',
       rf'\addplot[black,smooth] coordinates {{{pts(KA)}}};',rf'\addplot[vurgu] coordinates {{{pts(LA)}}};',
       r'\node[font=\small\bfseries,anchor=south] at (axis cs:35,10.2) {K};\node[font=\small\bfseries,vurgu,anchor=south] at (axis cs:35,1.2) {L};',r'\end{axis}']
    return tk('\n'.join(b),.95)
SK8=sk8()
# ============ ŞEKİL 9 · tablo meyve ============
SK9=tablo_svg(['Çiçek','Tozlaşma','Oksin uygulaması','Sonuç'],[['A','Var','Yok','Tohumlu meyve'],['B','Yok','Var','Tohumsuz meyve'],['C','Yok','Yok','Çiçek döküldü']])
# ============ SORU 10 hesap ============
MMC,MEGA=12,3; POLEN=MMC*4; SPERM=POLEN*2; KESE_HUC=MEGA*7; KESE_CEK=MEGA*8
D10=SPERM-KESE_HUC; assert D10==75
Y10=[SPERM-KESE_CEK,POLEN-KESE_HUC if False else (POLEN)*1-KESE_HUC,MMC*2-KESE_HUC,SPERM-MEGA*4*7]
assert Y10==[72,27,3,12] and len({D10,*Y10})==5 and D10>max(Y10)

# ============================ SORULAR ============================
# 01 · kolay · olumsuz · kök ucu
d1='III numaralı bölgedeki hücreler yoğun biçimde mitoz geçirerek sayıca artar.'
o1=['I numaralı bölge, bölünen hücreleri toprak parçacıklarının sürtünmesinden korur.',
    'II numaralı bölgedeki hücreler bölünme yeteneğini korur ve meristematiktir.',
    'III numaralı bölgede hücrelerin koful hacmi artar ve hücreler boyuna uzar.',
    'IV numaralı bölgede epidermis hücreleri kök tüyü oluşturarak emilim yüzeyini artırır.']
Q('1','buy','kolay','şekilli','Kök ucu bölgeleri','Kök ucunun boyuna kesitinde kök kılıfı, bölünme, uzama ve olgunlaşma bölgelerini ayırt edip işlevlerini ilişkilendirir.',
  'Kök ucunda hücre sayısı bölünme bölgesinde artar, uzama bölgesinde hücreler büyür; olgunlaşmış bölgede ise hücreler görevlerine göre farklılaşır.','Kökün uzamasının tüm bölgelerde mitozla sayıca artan hücrelerden kaynaklandığını sanmak.','kök ucu boyuna kesiti',
  metin='Şekilde, çift çenekli bir bitkinin kök ucunun boyuna kesiti şematik olarak verilmiş; kökün uç kısmından yukarıya doğru ardışık dört bölge I, II, III ve IV ile gösterilmiştir.\nBuna göre, numaralı bölgelerle ilgili aşağıdakilerden hangisi yanlıştır?',
  dogru=d1,sira=yer('A',d1,o1),
  yan=[(o1[0],'I numaralı bölge kök kılıfıdır ve ucu korur; ifade doğru olduğundan yanlış ifade aranırken seçilmemelidir.','dikkat'),
       (o1[1],'II numaralı bölge bölünme bölgesidir ve meristematik hücreler içerir; ifade doğrudur.','dikkat'),
       (o1[2],'III numaralı uzama bölgesinde hücreler kofullarının büyümesiyle uzar; ifade doğrudur.','bilgi'),
       (o1[3],'IV numaralı bölgede kök tüyleri epidermis hücrelerinden gelişir ve emilimi artırır; ifade doğrudur.','dikkat')],
  istenen='Kök ucu bölgeleri için yanlış olan ifade.',
  ip=['Bölgeleri kökün ucundan yukarıya doğru sırayla adlandır ve hücre sayısının hangi bölgede arttığını düşün.'],
  bilgi=[B('Kök ucu bölgeleri','uçtan yukarıya kök kılıfı, bölünme, uzama ve olgunlaşma bölgeleri sıralanır'),
         B('Büyüme ve bölünme','hücre sayısı mitozla artar; hücre boyutu ise hücrenin kendi büyümesiyle değişir')],
  ad=[A('Bölgeleri adlandır','I: kök kılıfı · II: bölünme bölgesi · III: uzama bölgesi · IV: olgunlaşma (kök tüylü) bölge.','I kılıf · II bölünme · III uzama · IV olgunlaşma'),
      A('İşlevleri yaz','Mitoz yalnız II de yoğundur; III te hücreler kofulları büyüyerek uzar; IV te hücreler farklılaşır.','Mitoz: II'),
      A('Yanlışı belirle','III te mitozla sayıca artış olduğunu söyleyen ifade yanlıştır.','Yanlış: III te yoğun mitoz')],
  puf='Sayıca artış bölünme bölgesinde, boyca artış uzama bölgesindedir.',sekil=SK1)

# 02 · kolay · tohum
d2='III numaralı yapı, çimlenmede bitkinin kökünü oluşturur.'
o2=['I numaralı yapı, döllenmiş yumurta hücresinin gelişmesiyle oluşmuştur.',
    'II numaralı yapı, çimlenmede sürgünün gövdesini ve yapraklarını oluşturur.',
    'IV numaralı yapı, çimlenmede bitkinin kökünü oluşturur.',
    'IV numaralı yapıdaki hücreler, mayoz bölünmeyle çoğalarak gövdeyi oluşturur.']
Q('2','ure','kolay','şekilli','Tohumun yapısı','Çift çenekli bir tohumda tohum kabuğu, çenek, kökçük ve tomurcuğun çimlenmedeki görevlerini ayırt eder.',
  'Tohumda kabuk embriyoyu korur, çenek besin depolar; embriyonun kökçüğü köke, tomurcuğu ise gövde ve yapraklara dönüşür.','Çeneğin sürgüne dönüştüğünü ya da kabuğun embriyoya ait olduğunu düşünmek.','çift çenekli tohum şeması',
  metin='Şekilde, çift çenekli bir bitkinin tohumunun boyuna kesiti şematik olarak gösterilmiştir. Tohum kabuğu I, çenek II, kökçük III ve tomurcuk IV ile numaralandırılmıştır.\nBuna göre, numaralı yapılarla ilgili aşağıdakilerden hangisi doğrudur?',
  dogru=d2,sira=yer('B',d2,o2),
  yan=[(o2[0],'Tohum kabuğu döllenmiş yumurtadan değil, tohum taslağının örtülerinden oluşur; bu nedenle ifade yanlıştır.','bilgi'),
       (o2[1],'Çenek çimlenmede besin depolar ve embriyoya besin sağlar; gövde ve yaprakları tomurcuk oluşturur.','dikkat'),
       (o2[2],'Kökü oluşturan yapı kökçüktür, yani III numaralıdır; IV numaralı yapı tomurcuktur.','dikkat'),
       (o2[3],'Tomurcuğun hücreleri mayozla değil mitozla bölünerek çoğalır; bu nedenle ifade yanlıştır.','bilgi')],
  istenen='Tohumun yapılarıyla ilgili doğru ifade.',
  ip=['Şekildeki yapıların adını yaz ve her birinin çimlenmede hangi organa dönüştüğünü ya da hangi görevi yaptığını düşün.'],
  bilgi=[B('Tohumun bölümleri','tohum kabuğu, besin depolayan çenek ve embriyo ekseninden oluşur'),
         B('Embriyo ekseni','kökçük ve tomurcuktan oluşur; çimlenmede bunlar mitozla büyür')],
  ad=[A('Yapıları adlandır','I: tohum kabuğu · II: çenek · III: kökçük · IV: tomurcuk.','I kabuk · II çenek · III kökçük · IV tomurcuk'),
      A('Görevleri eşle','Kökçük köke, tomurcuk gövde ve yapraklara dönüşür; çenek besin depolar.','III: kök'),
      A('İfadeleri ele','Kökün III ten oluştuğunu söyleyen ifade doğrudur; diğer ifadeler yapı ve bölünme türünü yanlış verir.','Doğru: III kök')],
  puf='Kökçük köke, tomurcuk sürgüne dönüşür; çenek ise besin deposudur.',sekil=SK2)

# 03 · zor · öncüllü · giberellin tablosu
pre3=[('K ile L nin sonuçları, nişasta yıkımını uyaran maddenin embriyodan geldiğini gösterir.',True,'iki kap arasındaki tek fark embriyonun varlığıdır'),
      ('L ile M nin sonuçları, giberellinin nişasta yıkımını uyarmada embriyonun yerini tutabildiğini gösterir.',True,'embriyosuz tohumda giberellin yıkımı başlatmıştır'),
      ('K ile N nin sonuçları, absisik asidin embriyonun nişasta yıkımını uyaran etkisini artırdığını gösterir.',False,'N de yıkım görülmemiştir; absisik asit uyarıcı etkiyi artırmamış, engellemiştir')]
s3,sr3,d3,y3=oncul(pre3,'C')
Q('3','hor','zor','tablo','Giberellin ve nişasta yıkımı','Tablodaki deney düzeneklerini karşılaştırarak embriyo, giberellin ve absisik asidin nişasta yıkımına etkisini yorumlar.',
  'Bir sonuç yalnız bir faktörün farklı olduğu iki düzeneğin karşılaştırılmasıyla yorumlanır; çimlenmede giberellin depo nişastasının yıkımını başlatır, absisik asit ise çimlenmeyi baskılar.','Birden fazla faktörün değiştiği kapları kıyaslayıp tek faktöre bağlı sonuç çıkarmak.','dört kaplı hormon deneyi',
  metin='Nişasta içeren, aynı büyüklükte ve aynı sıcaklıktaki yarım arpa tohumları, tabloda belirtilen koşullarda dört ayrı kapta aynı süre bekletiliyor. Sonunda her kapta nişasta yıkımının olup olmadığına bakılıyor.\n'+s3+'\nBuna göre, yukarıdaki ifadelerden hangileri doğrudur?',
  dogru=d3,sira=sr3,yan=y3,istenen='Doğru olan öncüller.',
  ip=['Her öncülde karşılaştırılan iki kabın hangi faktörlerde ayrıldığına bak.'],
  bilgi=[B('Çimlenmede hormonlar','giberellin tohumdaki depo besinlerin yıkımını başlatır; absisik asit tohumun dinlenmede kalmasını sağlar'),
         B('Kontrollü karşılaştırma','bir faktörün etkisi, yalnız o faktör farklı olan düzeneklerin sonuçlarıyla yorumlanır')],
  ad=[A('K ile L yi karşılaştır','Fark yalnız embriyodur; embriyolu kapta yıkım var, embriyosuzda yok.','I: doğru'),
      A('L ile M yi karşılaştır','Fark yalnız giberellindir; embriyosuz tohum giberellinle yıkım yapmıştır.','II: doğru'),
      A('K ile N yi karşılaştır','Fark absisik asittir; N de yıkım olmaması uyarının engellendiğini gösterir.','III: yanlış'),
      A('Öncülleri birleştir','I ve II doğru, III yanlıştır.','I ve II')],
  puf='Her sonuçta yalnız bir faktörün farklı olduğu iki kabı karşılaştır.',sekil=SK3)

# 04 · orta · olumsuz · hormon grafiği
d4='Çimlenme başladığında absisik asit derişimi, giberellin derişiminden yüksektir.'
o4=['İlk 4 gün boyunca absisik asit derişimi, giberellin derişiminden yüksektir.',
    '8. ve 12. günler arasında absisik asit derişimi azalırken giberellin derişimi artmıştır.',
    'Çimlenmenin başladığı güne kadar giberellin derişimi artmıştır.',
    '16. günde giberellin derişimi, absisik asit derişiminin 4 katıdır.']
Q('4','hor','orta','grafik','Çimlenmede hormon dengesi','Grafikteki eğrilerden hangisinin absisik asit, hangisinin giberellin olduğunu çıkarıp çimlenmeyle ilişkilendirerek ifadeleri değerlendirir.',
  'Tohum dinlenmedeyken absisik asit baskındır; çimlenme sırasında absisik asit azalır, giberellin artar ve depo besinlerin kullanımı başlar.','Çimlenme anında dinlenme hormonunun hâlâ baskın olduğunu düşünmek.','iki hormonun zamana karşı derişimi',
  metin='Şekildeki grafikte, bir tohumda çimlenme öncesi ve sırasında K ve L eğrileriyle gösterilen iki hormonun derişimlerinin zamanla değişimi verilmiştir. Eğrilerden biri absisik asidi, diğeri giberellini göstermektedir. Kesikli çizgi çimlenmenin başladığı günü belirtmektedir.\nBuna göre, aşağıdakilerden hangisi söylenemez?',
  dogru=d4,sira=yer('A',d4,o4),
  yan=[(o4[0],'0. ve 4. günlerde absisik asit derişimi 9 ve 8, giberellin derişimi ise 1 dir; ifade doğrudur.','dikkat'),
       (o4[1],'8. günden 12. güne absisik asit 5 ten 3 e düşmüş, giberellin 2,5 ten 6 ya çıkmıştır; ifade doğrudur.','dikkat'),
       (o4[2],'Giberellin derişimi başlangıçtaki 1 den çimlenme gününde 6 ya yükselmiştir; ifade doğrudur.','dikkat'),
       (o4[3],'16. günde giberellin 8, absisik asit 2 olduğundan oran 8 / 2 = 4 tür; ifade doğrudur.','islem')],
  istenen='Grafiğe göre söylenemeyecek ifade.',
  ip=['Önce hangi eğrinin dinlenmeyi sağlayan hormona ait olduğunu belirle; sonra çimlenme çizgisindeki değerleri oku.'],
  bilgi=[B('Absisik asit','tohumun dinlenmede kalmasını ve stomaların kapanmasını sağlayan hormondur'),
         B('Giberellin','tohumda depo besinlerin yıkımını başlatarak çimlenmeyi uyarır ve gövdenin uzamasını sağlar')],
  ad=[A('Eğrileri tanı','Çimlenmeyle azalan L eğrisi absisik asit, artan K eğrisi giberellindir.','L: absisik asit · K: giberellin'),
      A('Çimlenme gününü oku','12. günde absisik asit 3, giberellin 6 dır; giberellin daha yüksektir.','12. gün: 3 < 6'),
      A('İfadeleri sına','Diğer dört ifade grafikteki değerlerle uyuşur; çimlenme anında absisik asidin yüksek olduğu ifadesi uyuşmaz.','Söylenemez: ABA > giberellin')],
  puf='Çimlenme çizgisinde iki eğrinin hangisinin üstte olduğuna bak.',sekil=SK4)

# 05 · orta · yıllık halka
d5='II numaralı halkanın dar olması, o yıl kambiyumun az miktarda ksilem oluşturduğunu gösterir.'
o5=['I numaralı halka, ağacın yaşamının son yılında oluşmuştur.',
    'III numaralı yapı, bölünerek her yıl dışa doğru ksilem, içe doğru floem oluşturur.',
    'Yıllık halkalar, odun gövdede floem dokusunun her yıl yenilenmesiyle oluşur.',
    'Şekildeki halkalar, gövdenin boyca uzaması olan primer büyüme sonucunda oluşmuştur.']
Q('5','dok','orta','şekilli','Yıllık halkalar','Odunsu bir gövdenin enine kesitinde kambiyumun görevini ve yıllık halkaların nasıl oluştuğunu yorumlar.',
  'Çok yıllık odunsu bitkilerde kambiyum her yıl içe ksilem, dışa floem oluşturur; yıllık halkalar ksilemden oluşur, dar halka o yıl az ksilem yapıldığını gösterir.','Halkaların floemden oluştuğunu ya da en içteki halkanın en yeni olduğunu düşünmek.','odunsu gövde enine kesiti',
  metin='Şekilde, çok yıllık odunsu bir bitkinin gövdesinin enine kesiti şematik olarak verilmiştir. Gövdenin merkezinde öz, çevresinde yıllık halkalar, en dışta ise kambiyum, floem ve mantar doku bulunmaktadır. En içteki halka I, üçüncü halka II, kambiyum III ile gösterilmiştir.\nBuna göre, aşağıdakilerden hangisi doğrudur?',
  dogru=d5,sira=yer('E',d5,o5),
  yan=[(o5[0],'Kambiyum ksilemi içe doğru ekler; bu nedenle en içteki I numaralı halka en eski halkadır, son yıla ait değildir.','dikkat'),
       (o5[1],'Kambiyum içe doğru ksilem, dışa doğru floem oluşturur; ifadedeki yönler ters verilmiştir.','bilgi'),
       (o5[2],'Yıllık halkaları ksilem oluşturur; floem hücreleri bu halkaları oluşturmaz.','bilgi'),
       (o5[3],'Halkalar kambiyumun bölünmesiyle gövdenin kalınlaşması olan sekonder büyümenin ürünüdür.','bilgi')],
  istenen='Kesitle ilgili doğru ifade.',
  ip=['Kambiyumun hangi yönlere hangi dokuyu eklediğini ve halkaların hangi dokudan oluştuğunu düşün.'],
  bilgi=[B('Sekonder büyüme','kambiyumun bölünmesiyle gövdenin ve kökün kalınlaşmasıdır; ksilem içe, floem dışa eklenir'),
         B('Yıllık halka','her yıl oluşan ksilem halkasıdır; halka genişliği o yıl oluşan ksilem miktarını yansıtır')],
  ad=[A('Yapıları tanı','I: en eski halka · II: dar üçüncü halka · III: kambiyum.','I eski · II dar · III kambiyum'),
      A('Kambiyumun görevini uygula','Kambiyum içe ksilem, dışa floem ekler; halkalar ksilemdir ve içten dışa gittikçe yenidir.','Halka = ksilem'),
      A('Halka genişliğini yorumla','Dar halka, o yıl az ksilem oluştuğunu gösterir; doğru ifade budur.','Dar halka = az ksilem')],
  puf='Halkalar ksilemden oluşur ve içten dışa doğru yeniden eskiye değil, eskiden yeniye sıralanır.',sekil=SK5)

# 06 · zor · öncüllü · su potansiyeli
pre6=[('Su, M hücresinden K hücresine doğru hareket eder.',True,'M nin su potansiyeli −0,3 MPa, K ninki −0,6 MPa dır ve su yüksek potansiyelden düşüğe hareket eder'),
      ('L hücresine su girişi sürdükçe L nin turgor basıncı artar ve L ile K arasındaki su potansiyeli farkı azalır.',True,'L ye su girince hacmi ve duvar basıncı artar, su potansiyeli yükselir'),
      ('L hücresinin osmotik potansiyeli K ninkinden daha düşük olduğundan su L den K ya doğru hareket eder.',False,'su hareketi toplam su potansiyeline göre olur ve L nin toplam potansiyeli K ninkinden düşüktür, yani su K den L ye gider')]
s6,sr6,d6,y6=oncul(pre6,'D')
Q('6','tas','zor','tablo','Hücreler arası su hareketi','Osmotik potansiyel ve turgor basıncından hücrelerin su potansiyelini hesaplayıp su hareketinin yönünü yorumlar.',
  'Hücrenin su potansiyeli, osmotik potansiyel ile turgor basıncının toplamıdır; su, potansiyeli yüksek olandan düşük olana doğru hareket eder.','Su hareketini yalnız osmotik potansiyele ya da yalnız turgor basıncına göre belirlemek.','üç hücrenin ψs ve turgor basıncı tablosu',
  metin='Kök korteksinde yan yana, M – K – L sırasıyla dizilmiş üç hücrenin osmotik potansiyelleri ve turgor basınçları tabloda verilmiştir. Hücrelerin su potansiyeli, osmotik potansiyel ile turgor basıncının toplamına eşittir.\n'+s6+'\nBuna göre, yukarıdaki ifadelerden hangileri doğrudur?',
  dogru=d6,sira=sr6,yan=y6,istenen='Doğru olan öncüller.',
  ip=['Önce her hücrenin toplam su potansiyelini bul, sonra komşu hücreleri yöne göre karşılaştır.'],
  bilgi=[B('Su potansiyeli','osmotik potansiyel ile turgor basıncının toplamıdır · su yüksek potansiyelden düşük potansiyele doğru hareket eder'),
         B('Turgor basıncı','hücreye su girdikçe hücre duvarına yapılan basınç artar')],
  ad=[A('Toplam potansiyelleri hesapla','K: −1,0 + 0,4 = −0,6 · L: −1,2 + 0,2 = −1,0 · M: −0,9 + 0,6 = −0,3 MPa.','K −0,6 · L −1,0 · M −0,3'),
      A('Hareket yönünü bul','M > K > L olduğundan su M den K ya, K den L ye hareket eder.','M → K → L'),
      A('Öncülleri değerlendir','I doğru; L ye su girişi turgoru artırır ve fark azalır, II doğru; III de yön ters verilmiştir.','I, II doğru · III yanlış'),
      A('Öncülleri birleştir','I ve II doğru, III yanlıştır.','I ve II')],
  puf='Su hareketini toplam potansiyel belirler; iki bileşeni toplamadan yön söyleme.',sekil=SK6)

# 07 · orta · klinostat
d7='L deki bitkinin gövdesinde oksin, her yüzde yaklaşık eşit dağılır.'
o7=['K deki kökün alt yüzünde oksin derişimi azaldığı için kök aşağı doğru kıvrılır.',
    'K deki gövdenin alt yüzünde oksin derişimi artar ve bu yüzde uzama yavaşlar.',
    'L deki kök, yerçekimi yönüne doğru bükülür.',
    'L deki sonuç, yerçekiminin bitkilerde oksin dağılımını hiçbir zaman değiştirmediğini gösterir.']
Q('7','hor','orta','şekilli','Yerçekimi tepkisi','Klinostat düzeneğinde dönmenin yerçekiminin tek yönlü etkisini ortadan kaldırdığını oksin dağılımıyla ilişkilendirir.',
  'Yerçekimi tropizmasında oksin yerçekimi yönündeki yüzde birikir; kökte yüksek derişim uzamayı baskılar, gövdede ise artırır. Dönen düzenekte oksin her yüzde eşit dağılır.','Oksinin kök ve gövdede aynı derişimde aynı etkiyi yaptığını sanmak.','sabit ve dönen saksı',
  metin='Aynı türden tohumlar karanlıkta çimlendirilirken K tohumu sabit tutulmuş; L tohumu ise yatay eksen etrafında yavaşça döndürülmüştür. Birkaç gün sonra bitkilerin şekildeki gibi yönlendiği gözlenmiştir. İki düzenekte de başka bir yönlendirici etki yoktur.\nBuna göre, aşağıdakilerden hangisi doğrudur?',
  dogru=d7,sira=yer('B',d7,o7),
  yan=[(o7[0],'Kökün alt yüzünde oksin artar ve uzamayı baskılar; ifadedeki azalma yanlıştır.','bilgi'),
       (o7[1],'Gövdenin alt yüzünde biriken oksin uzamayı artırır, yavaşlatmaz; ifade yanlıştır.','bilgi'),
       (o7[2],'Dönen düzenekte yerçekimi tek yönlü etki yapmadığından kök bükülmez, düz büyür.','dikkat'),
       (o7[3],'K da oksin dağılımı yerçekimiyle değişmiş, L de değişmemiştir; bu nedenle genelleme yanlıştır.','dikkat')],
  istenen='Deney için doğru ifade.',
  ip=['Dönmenin yerçekiminin etkisini hangi yönde değiştirdiğini ve oksinin kök ile gövdedeki etkisini ayrı ayrı düşün.'],
  bilgi=[B('Tropizma','bitkinin uyarıcıya göre yön alarak büyümesidir; asimetrik büyümeyle gerçekleşir'),
         B('Oksin','hücre uzamasını uyarır; kökte gövdeye göre daha düşük derişimlerde etkilidir')],
  ad=[A('K yı yorumla','Sabit bitkide oksin alt yüzde toplanır; kök aşağı, gövde yukarı yönelir.','K: yönelim var'),
      A('L yi yorumla','Dönen bitkide yerçekimi her yüze eşit etki ettiğinden oksin eşit dağılır; yönelim olmaz.','L: eşit dağılım'),
      A('İfadeyi seç','Oksinin L de her yüzde yaklaşık eşit dağıldığını söyleyen ifade doğrudur.','Doğru: L de eşit')],
  puf='Dönme, yerçekiminin tek yönlü etkisini ortadan kaldırır.',sekil=SK7)

# 08 · orta · öncüllü · K+ alımı
pre8=[('K⁺ nin kök hücrelerine alınmasında enerji gerektiren bir taşıma da rol oynar.',True,'solunumu engelleyen maddenin bulunduğu ortamda alım hızı düşük kalır ve O₂ arttıkça hız yükselir'),
      ('Ortamdaki O₂ derişimi %0 iken K⁺ alımı tamamen durur.',False,'K eğrisi %0 O₂ de de sıfır değildir, çok düşük de olsa alım sürer'),
      ('O₂ derişimi %20 nin üzerine çıkarıldığında K⁺ alım hızı artmaz; bu aralıkta O₂ sınırlayıcı değildir.',True,'K eğrisi %20 den sonra yataydır')]
s8,sr8,d8,y8=oncul(pre8,'C')
Q('8','tas','orta','grafik','Kökte mineral alımı','Grafikten kökte mineral iyonu alımının O₂ derişimine ve ATP sentezine bağlılığını yorumlar.',
  'Kök hücrelerine mineral alımı büyük ölçüde enerji gerektirir; O₂ derişimi arttıkça ATP üretimi ve alım hızı yükselir, bir noktadan sonra başka faktörler sınırlayıcı olur.','Mineral alımının yalnız difüzyonla gerçekleştiğini düşünmek.','O₂ derişimi ve K⁺ alım hızı',
  metin='Aynı türden eşit kök parçaları, K+ içeren ve farklı O2 derişimlerine sahip ortamlara konuyor. K eğrisi normal ortamdaki, L eğrisi ise hücresel solunumda ATP sentezini engelleyen bir madde eklenmiş ortamdaki K+ alım hızını göstermektedir.\n'+s8+'\nBuna göre, yukarıdaki ifadelerden hangileri doğrudur?',
  dogru=d8,sira=sr8,yan=y8,istenen='Doğru olan öncüller.',
  ip=['K ve L eğrilerini karşılaştır; sonra K eğrisinin O₂ nin sıfır ve yüksek değerlerindeki hâline bak.'],
  bilgi=[B('Mineral alımı','kök hücrelerine iyon alımı difüzyonla ve ATP harcanarak aktif taşıma ile gerçekleşir'),
         B('Sınırlayıcı faktör','bir faktör artırıldığında hız artmıyorsa o faktör sınırlayıcı değildir')],
  ad=[A('K ile L yi kıyasla','ATP sentezi engellenince alım hızı düşük kalır; O₂ arttıkça normal ortamda hız artar.','I: doğru'),
      A('O₂ sıfırdaki değeri oku','K eğrisinin başlangıcı 1 dir, sıfır değildir; alım tamamen durmaz.','II: yanlış'),
      A('Yüksek O₂ bölgesini oku','%20 den sonra hız 10 da sabit kalır; O₂ sınırlayıcı değildir.','III: doğru'),
      A('Öncülleri birleştir','I ve III doğru, II yanlıştır.','I ve III')],
  puf='Eğrinin başlangıç noktasını ve yataylaştığı bölgeyi ayrı ayrı oku.',sekil=SK8)

# 09 · orta · olumsuz · partenokarpi
d9='B deki meyvede, döllenmiş yumurta hücresinden gelişen embriyo bulunur.'
o9=['A daki meyve, çiçeğin yumurtalığının gelişmesiyle oluşmuştur.',
    'B deki meyvenin oluşumunda uygulanan oksin, döllenmenin yaptığı uyarıyı yerine getirmiştir.',
    'C de çiçeğin dökülmesi, ne tozlaşmanın ne de oksin uygulamasının olmamasıyla ilişkilidir.',
    'A ve B deki meyveler yumurtalık duvarından gelişir.']
Q('9','ure','orta','tablo','Tohumsuz meyve','Döllenme olmadan oksinle meyve oluşumunu yorumlayıp meyve ve tohumun hangi yapılardan geliştiğini ayırt eder.',
  'Meyve yumurtalıktan, tohum ise tohum taslağından gelişir; meyve gelişimi döllenmeden doğan hormon uyarısına bağlıdır ve bu uyarı oksin uygulamasıyla verilebilir.','Her meyvenin tohum ve embriyo içerdiğini düşünmek.','tozlaşma ve oksin uygulaması',
  metin='Aynı bitkinin üç çiçeği tabloda belirtilen koşullara tabi tutuluyor. B ve C çiçekleri tomurcuk evresinde kapatılarak tozlaşmaları engelleniyor. Birkaç hafta sonra çiçeklerin durumu tabloda gösterilmiştir.\nBuna göre, aşağıdakilerden hangisi söylenemez?',
  dogru=d9,sira=yer('D',d9,o9),
  yan=[(o9[0],'Meyve yumurtalıktan gelişir; ifade doğrudur ve söylenebilir.','dikkat'),
       (o9[1],'Döllenme olmadığı hâlde B de meyve oluşmuştur; bu uyarıyı oksin sağlamıştır, ifade doğrudur.','dikkat'),
       (o9[2],'C de hem tozlaşma hem oksin uygulaması yoktur ve meyve gelişmemiştir; ifade doğrudur.','dikkat'),
       (o9[3],'Her iki meyve de yumurtalık duvarından gelişir; ifade doğrudur.','bilgi')],
  istenen='Tabloya göre söylenemeyecek ifade.',
  ip=['Hangi çiçekte döllenmenin gerçekleşebileceğini belirle ve embriyonun hangi olayla oluştuğunu düşün.'],
  bilgi=[B('Meyve ve tohum','meyve yumurtalıktan, tohum tohum taslağından gelişir'),
         B('Hormonların etkisi','meyve gelişimini uyaran oksin gibi hormonlar, döllenme sonrası oluşur ya da dışarıdan uygulanabilir')],
  ad=[A('Koşulları oku','A: tozlaşma var · B ve C: tozlaşma engellenmiş · yalnız B ye oksin uygulanmış.','A tozlaşmış · B oksin · C hiçbiri'),
      A('Döllenmeyi belirle','Tozlaşma olmadığından B ve C de döllenme gerçekleşmez; embriyo oluşmaz.','B de zigot yok'),
      A('Söylenemeyeni seç','B deki meyvede embriyo bulunduğunu söyleyen ifade söylenemez.','Söylenemez: B de embriyo')],
  puf='Tozlaşma yoksa döllenme de yoktur; döllenme yoksa embriyo da oluşmaz.',sekil=SK9)

# 10 · zor · hesap · sperm / embriyo kesesi
Q('10','ure','zor','düz','Gamet sayımı','Mikrospor ve megaspor ana hücrelerinden oluşan yapıları sayıp gametofit hücre sayılarını karşılaştırır.',
  'Bir mikrospor ana hücresi mayozla 4 mikrospor, her mikrospor ise polen tanesi verir; bir megaspor ana hücresinden yalnız bir işlevsel megaspor ve bir embriyo kesesi oluşur.','Her mayoz ürününün işlevsel olduğunu ya da embriyo kesesinde hücre ile çekirdek sayısının aynı olduğunu düşünmek.','12 mikrospor ana hücresi ve 3 megaspor ana hücresi',
  metin='Bir çiçekli bitkinin çiçeğinde 12 mikrospor ana hücresi ve 3 megaspor ana hücresi bulunmaktadır. Tüm ana hücreler mayoz geçirir; oluşan tüm mikrosporlar polen tanesine dönüşür ve her polen tanesi 2 sperm hücresi oluşturur. Her megaspor ana hücresinden yalnız bir işlevsel megaspor kalır ve bu megaspor 7 hücreli (8 çekirdekli) bir embriyo kesesi oluşturur.\nBuna göre, bu çiçekte oluşan toplam sperm hücresi sayısı, embriyo keselerindeki toplam hücre sayısından kaç fazladır?',
  dogru=D10,yan=[(Y10[0],'Embriyo keselerinin çekirdek sayısı (3 × 8 = 24) hücre sayısı yerine kullanılmış; 96 − 24 = 72 bulunmuştur.','islem'),
                 (Y10[1],'Her polen tanesi 1 sperm veriyor sanılmış; 48 − 21 = 27 bulunmuştur.','islem'),
                 (Y10[2],'Her ana hücreden yalnız bir polen tanesi oluştuğu varsayılmış; 24 − 21 = 3 bulunmuştur.','islem'),
                 (Y10[3],'Her megaspor ana hücresinden 4 işlevsel megaspor ve 12 embriyo kesesi sayılmış; 96 − 84 = 12 bulunmuştur.','islem')],
  istenen='Sperm hücresi sayısı ile embriyo kesesi hücre sayısı arasındaki fark.',
  ip=['Erkek ve dişi tarafta, ana hücreden başlayarak her basamakta kaç ürün oluştuğunu ayrı ayrı say.'],
  bilgi=[B('Erkek gametofit','mikrospor ana hücresi mayozla 4 mikrospor oluşturur; her mikrospor polen tanesine dönüşür'),
         B('Embriyo kesesi','tek bir işlevsel megasporun mitozlarıyla oluşan 7 hücreli, 8 çekirdekli yapıdır')],
  ad=[A('Polen tanelerini say','12 × 4 = 48 polen tanesi oluşur.','12 × 4 = 48'),
      A('Sperm sayısını bul','Her polen tanesi 2 sperm verir; 48 × 2 = 96 sperm oluşur.','48 × 2 = 96'),
      A('Embriyo kesesi hücrelerini say','3 embriyo kesesi vardır; her biri 7 hücrelidir; 3 × 7 = 21 hücre.','3 × 7 = 21'),
      A('Farkı hesapla','Sperm sayısı hücre sayısından 96 − 21 = 75 fazladır.','96 − 21 = 75')],
  puf='Önce her iki tarafta ürün sayılarını ayrı say; çekirdek ile hücre sayısını karıştırma.')

# ============================ YAZ ============================
assert len(P.ANA)==10
Z=Counter(q['zorluk'] for q in P.ANA); assert Z=={'kolay':2,'orta':5,'zor':3},Z
HR=Counter(q['cevap']['sik'] for q in P.ANA); assert all(HR[h]==2 for h in 'ABCDE'),HR
assert 4<=len({q['tipId'] for q in P.ANA})<=6
SEK=sum(1 for q in P.ANA if q['sekil']); assert SEK>=6,SEK
for q in P.ANA: q['kardes']=None
P.yaz(os.path.join(GD,'bitkiiki-1.json'),'/tmp/claude-0/sp/bos-bitkiiki.json')
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=KEY))['kartlar'].append(c['id'])
json.dump(dict(konu=KONU_AD,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2018–2026 Biyoloji (yalnız mantık), MEB 11. sınıf.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','abbitkiiki.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler),'şekil',SEK)
