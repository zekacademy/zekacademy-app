"""AYT Biyoloji · Dolaşım ve Bağışıklık Sistemi · 2. dalga · 10 soru (kardeş yok, ipucu 1). Şekiller TikZ/pgfplots ve tablo_svg; sayılar Python'da hesaplanır ve assert edilir."""
import sys,os,json,math
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,os.path.join(HV,'tyt-bio')); sys.path.insert(0,HV)
import _hafif_bio as H
from _hafif_bio import *
KONUAD='Dolaşım ve Bağışıklık Sistemi'; KK='abio|Dolaşım ve Bağışıklık Sistemi'
H.KONU=KONUAD
P=Parti('dolasimiki',KONUAD,KK,ders='AYT Biyoloji',idon='aytbio')
KY='ÖSYM AYT 2018–2026 Biyoloji (yalnız mantık) · MEB 11–12. sınıf Dolaşım ve Bağışıklık'
def q(n,tipId,tip,z,alt,kaz,kalip,ozet,ne,fikir,tuzak,ad,**k):
    assert len(k['ip'])==1 and 3<=len(ad)<=7
    kid=f'K-ABDO2-{n:02d}'
    kart(kid,alt,fikir,tuzak,z,kalip,len(ad),tipId,tip,KY)
    mk(P,f'{n:04d}',ad=ad,adim=len(ad),tipId=tipId,tip=tip,z=z,alt=alt,kaz=kaz,kalip=kalip,kart=f'{kid} ({ozet}) · {ne}',**k)
def qo(n,r,tipId,tip,z,alt,kaz,ozet,ne,fikir,tuzak,**k):
    q(n,tipId,tip,z,alt,kaz,'öncüllü',ozet,ne,fikir,tuzak,r['adim'],dogru=r['dogru'],yan=r['yan'],sira=r['sira'],**k)
def yer(harf,dogru,yanlar):
    sira=[None]*5; sira['ABCDE'.index(harf)]=dogru; it=iter(yanlar)
    for i in range(5):
        if sira[i] is None: sira[i]=next(it)
    assert sorted(sira)==sorted([dogru]+list(yanlar)); return sira
ORD=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
SETS=[{'I'},{'II'},{'III'},{'I','II'},{'I','III'},{'II','III'},{'I','II','III'}]
def onc(d,harf,mod='dogru'):
    T={k for k,v in d.items() if v[0]==(mod=='dogru')}; assert T in SETS,T
    p=SETS.index(T); h='ABCDE'.index(harf)
    assert max(0,p-2)<=h<=min(4,p),('harf uygun değil',T,p,h)
    ad='doğru' if mod=='dogru' else 'yanlış'
    mes=lambda i:len(SETS[i]^T)
    once=sorted([i for i in range(7) if i<p],key=lambda i:(mes(i),-i))[:h]
    sonra=sorted([i for i in range(7) if i>p],key=lambda i:(mes(i),i))[:4-h]
    ops=sorted(once+[p]+sonra); assert ops.index(p)==h and len(ops)==5
    yan=[]
    for i in ops:
        if i==p: continue
        S=SETS[i]; parca=[]
        for k in sorted(S-T,key=['I','II','III'].index): parca.append(f'{k}. öncülünü {ad} saymış. Doğrusu: {d[k][1]}')
        for k in sorted(T-S,key=['I','II','III'].index): parca.append(f'{k}. öncülünü {ad} saymamış. Doğrusu: {d[k][1]}')
        yan.append((ORD[i],' '.join(parca),'bilgi'))
    steps=[A(f'{k}. öncülü değerlendir',d[k][1],f'{k}: '+('doğru' if d[k][0] else 'yanlış')) for k in d]
    steps.append(A('Sonucu yaz','İstenen koşulu sağlayan öncüller bir arada yazılır.','Sonuç: '+ORD[p]))
    return dict(dogru=ORD[p],yan=yan,sira=[ORD[i] for i in ops],adim=steps)
def tk(body,scale=1.0): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small,scale=%s]\n%s\n\\end{tikzpicture}'%(scale,body))
OKU='-{Stealth[length=2.3mm,width=1.9mm]}'
def lab(t,x,y,x1,y1,x2,y2):
    return f'\\node[font=\\normalsize\\bfseries] at ({x},{y}) {{{t}}};\\draw[{OKU},line width=.8pt] ({x1},{y1})--({x2},{y2});'
AX='/pgf/number format/1000 sep={},tick label style={font=\\small},label style={font=\\small},axis lines=left,every axis plot/.append style={line width=1.4pt}'
LEG='legend style={font=\\small,at={(0.5,1.03)},anchor=south,legend columns=-1,draw=none,fill=none}'
# ============ ŞEKİLLER ============
def sekil_cift():
    b=[]
    box=lambda x,y,t,f:f'\\node[draw,rounded corners=4pt,line width=1.4pt,minimum width=3.1cm,minimum height=1.1cm,font=\\normalsize\\bfseries,fill={f}] at ({x},{y}) {{{t}}};'
    b.append(box(-2.1,0,'Kalbin sağ yarısı','red!12')); b.append(box(2.1,0,'Kalbin sol yarısı','red!12'))
    b.append(box(0,3.6,'Akciğerler','cyan!15')); b.append(box(0,-3.6,'Vücut dokuları','orange!18'))
    for x1,y1,x2,y2,t,tx,ty in [(-2.1,.6,-.9,3.0,'I',-2.0,2.0),(.9,3.0,2.1,.6,'II',2.1,2.0),(2.1,-.6,.9,-3.0,'III',2.2,-2.0),(-.9,-3.0,-2.1,-.6,'IV',-2.2,-2.0)]:
        b.append(f'\\draw[{OKU},line width=1.6pt] ({x1},{y1})--({x2},{y2});\\node[font=\\large\\bfseries,fill=white,inner sep=1.5pt] at ({tx},{ty}) {{{t}}};')
    return tk('\n'.join(b),.8)
def sekil_yangi():
    b=[]
    b.append('\\draw[line width=1.4pt,fill=brown!25] (-4,4.4) rectangle (1.6,5.1);\\draw[line width=1.4pt,fill=brown!25] (2.6,4.4) rectangle (4.6,5.1);')
    b.append('\\fill[orange!12] (-4,4.4) rectangle (4.6,1.9);\\draw[line width=1.2pt] (-4,1.9)--(4.6,1.9);\\draw[line width=1.4pt] (-4,4.4)--(1.6,4.4);\\draw[line width=1.4pt] (2.6,4.4)--(4.6,4.4);\\draw[line width=1.4pt] (1.6,4.4)--(1.6,5.1);\\draw[line width=1.4pt] (2.6,4.4)--(2.6,5.1);')
    b.append('\\draw[line width=1.6pt,fill=red!10] (-4,-.2) rectangle (4.6,.9);\\fill[red!10] (-4,-.2) rectangle (4.6,.9);\\draw[line width=1.6pt] (-4,-.2)--(4.6,-.2);\\draw[line width=1.6pt] (-4,.9)--(4.6,.9);')
    for x,y in [(.4,3.8),(1.6,3.5),(2.7,3.8),(3.6,3.4)]: b.append(f'\\draw[green!50!black,fill=green!50!black] ({x},{y}) ellipse (.22 and .1);')
    # mast hücresi I
    b.append('\\draw[line width=1.5pt,fill=violet!18] plot[smooth cycle] coordinates {(-3.2,3.4) (-2.4,3.8) (-1.5,3.5) (-1.4,2.8) (-2.2,2.4) (-3.0,2.7)};')
    for x,y in [(-2.7,3.2),(-2.2,3.4),(-1.9,3.0),(-2.6,2.8),(-2.1,2.7)]: b.append(f'\\fill[violet!60!black] ({x},{y}) circle (.07);')
    # fagosit III
    b.append('\\draw[line width=1.5pt,fill=cyan!20] plot[smooth cycle] coordinates {(.5,2.7) (1.3,3.1) (2.1,2.8) (2.1,2.2) (1.3,1.9) (.6,2.2)};')
    for x,y in [(1.0,2.6),(1.4,2.7),(1.7,2.4),(1.2,2.2)]: b.append(f'\\fill[blue!55!black] ({x},{y}) circle (.17);')
    # IV: ok noktalı
    b.append(f'\\draw[{OKU},line width=1.2pt,dash pattern=on 2pt off 2.5pt] (-2.3,2.35)--(-2.3,.95);')
    b.append(f'\\draw[{OKU},line width=1.6pt] (1.4,.95)--(1.4,1.85);')
    b.append(lab('I',-4.2,3.4,-3.85,3.4,-3.3,3.2)); b.append(lab('II',-4.3,.35,-3.9,.35,-3.3,.35))
    b.append(lab('III',3.6,2.6,3.2,2.6,2.2,2.5)); b.append(lab('IV',-3.6,1.7,-3.2,1.7,-2.4,1.6)); b.append(lab('V',3.4,5.6,3.4,5.35,2.9,3.7).replace('(3.4,5.35)--(2.9,3.7)','(3.2,5.35)--(2.9,3.8)'))
    return tk('\n'.join(b),.78)
def sekil_toplardamar():
    b=[]
    b.append('\\draw[line width=1.5pt,fill=red!35] (-2.4,-2.2) .. controls (-2.8,0) .. (-2.4,2.2) -- (-1.0,2.2) -- (-1.0,-2.2) -- cycle;')
    b.append('\\draw[line width=1.5pt,fill=red!35] (2.4,-2.2) .. controls (2.8,0) .. (2.4,2.2) -- (1.0,2.2) -- (1.0,-2.2) -- cycle;')
    b.append('\\draw[line width=1.8pt] (-.55,-3.3)--(-.55,3.3);\\draw[line width=1.8pt] (.55,-3.3)--(.55,3.3);\\fill[blue!10] (-.55,-3.3) rectangle (.55,3.3);\\draw[line width=1.8pt] (-.55,-3.3)--(-.55,3.3);\\draw[line width=1.8pt] (.55,-3.3)--(.55,3.3);')
    # alt kapakçık II (kapalı): yapraklar ortada birleşir
    b.append('\\draw[line width=2.4pt] (-.55,-1.8)--(-.04,-1.15);\\draw[line width=2.4pt] (.55,-1.8)--(.04,-1.15);')
    # üst kapakçık III (açık): yapraklar duvara yakın
    b.append('\\draw[line width=2.4pt] (-.55,1.1)--(-.42,2.1);\\draw[line width=2.4pt] (.55,1.1)--(.42,2.1);')
    b.append(f'\\draw[{OKU},line width=2.6pt,red!70] (0,-.6)--(0,.9);\\draw[{OKU},line width=2.6pt,red!70] (0,2.4)--(0,3.6);')
    b.append('\\node[font=\\normalsize\\bfseries] at (0,4.0) {Kalbe};')
    b.append(lab('I',-3.9,0,-3.5,0,-2.9,0)); b.append(lab('II',2.6,-2.7,2.2,-2.6,.75,-1.6).replace('(2.2,-2.6)--(.75,-1.6)','(2.2,-2.5)--(.7,-1.6)'))
    b.append(lab('III',2.6,2.7,2.2,2.6,.7,1.7)); b.append(lab('IV',-1.9,-.6,-1.5,-.6,-.7,-.3))
    return tk('\n'.join(b),.78)
# Q7: kılcal damar boyunca madde miktarı
def sekil_kilcal():
    f={'K':'domain=0:1,samples=30,smooth,red!75,{ 1.0*exp(-1.2*x)+0.08 }','L':'','M':''}
    b=[]
    base='width=3.0cm,height=3.6cm,xmin=-.05,xmax=1.05,ymin=0,ymax=1.1,xtick={0,1},xticklabels={{Atar-\\\\damar\\\\ucu},{Toplar-\\\\damar\\\\ucu}},xticklabel style={font=\\small,align=center},ytick=\\empty,ylabel={Miktar},'+AX
    for nm,dx,expr in [('K',0,'1.0*exp(-1.4*x)+0.05'),('L',4.2,'1.0-0.9*exp(-1.4*x)'),('M',8.4,'0.55')]:
        b.append(f'\\begin{{axis}}[{base},at={{({dx}cm,0)}},title={{\\normalsize\\bfseries {nm}}}]\\addplot[domain=0:1,samples=30,smooth,red!75!black]{{{expr}}};\\end{{axis}}')
    return tk('\n'.join(b),.95)
# Q9: organ kan akışı
ORG=['Beyin','Sindirim','Böbrek','Kas']
DIN={'Beyin':700,'Sindirim':1200,'Böbrek':1100,'Kas':1000,'Diğer':1000}
EGZ={'Beyin':700,'Sindirim':500,'Böbrek':500,'Kas':12000,'Diğer':6300}
TD,TE=sum(DIN.values()),sum(EGZ.values())
assert TD==5000 and TE==20000 and TE==4*TD and EGZ['Kas']==12*DIN['Kas']
assert DIN['Kas']*100//TD==20 and EGZ['Kas']*100//TE==60
assert EGZ['Böbrek']-DIN['Böbrek']==-600 and EGZ['Kas']-DIN['Kas']==11000
assert DIN['Beyin']*1000/TD==140 and EGZ['Beyin']*1000/TE==35
assert DIN['Sindirim']*1000/TD==240 and EGZ['Sindirim']*1000/TE==25
assert sum(DIN[o] for o in ORG[:3])==3000 and sum(EGZ[o] for o in ORG[:3])==1700
def sekil_bar():
    b=['\\begin{axis}[ybar,bar width=9pt,width=8.2cm,height=6cm,xmin=.4,xmax=4.6,xtick={1,2,3,4},xticklabels={Beyin,Sindirim,Böbrek,Kas},scaled y ticks=false,ymin=0,ymax=16500,ytick={0,3000,6000,9000,12000},nodes near coords,nodes near coords style={font=\\footnotesize,rotate=90,anchor=west},xlabel={Organ},ylabel={Kan akışı (mL/dk)},'+LEG+','+AX+',every axis plot/.append style={line width=.8pt}]']
    b.append('\\addplot[fill=blue!35,draw=blue!70!black] coordinates {'+' '.join(f'({i+1},{DIN[o]})' for i,o in enumerate(ORG))+'};\\addlegendentry{Dinlenme}')
    b.append('\\addplot[fill=red!45,draw=red!70!black] coordinates {'+' '.join(f'({i+1},{EGZ[o]})' for i,o in enumerate(ORG))+'};\\addlegendentry{Egzersiz}')
    b.append('\\end{axis}')
    return tk('\n'.join(b),.95)
# Q10: HIV
XS=[0,.3,1,2,4,6,8,9,10]
KV=[0,92,16,10,12,15,20,62,96]; LT=[100,72,88,82,66,52,34,16,6]
def sekil_hiv():
    b=['\\begin{axis}[width=8cm,height=5.8cm,xmin=-.3,xmax=10.5,ymin=0,ymax=108,xtick={0,2,4,6,8,10},ytick={0,25,50,75,100},xlabel={Enfeksiyondan sonra geçen süre (yıl)},ylabel={Göreli miktar (\\%)},'+LEG+','+AX+']']
    b.append('\\addplot[red!75!black,mark=*,mark size=1.8pt,smooth] coordinates {'+' '.join(f'({x},{y})' for x,y in zip(XS,KV))+'};\\addlegendentry{K}')
    b.append('\\addplot[blue!70,mark=square*,mark size=1.8pt,smooth] coordinates {'+' '.join(f'({x},{y})' for x,y in zip(XS,LT))+'};\\addlegendentry{L}')
    b.append('\\end{axis}')
    return tk('\n'.join(b),.95)
# ============ SORULAR ============
T_DONGU=('do2-dongu','Çift dolaşım ve kalp'); T_KAN=('do2-kan','Kan ve pıhtılaşma'); T_DAMAR=('do2-damar','Damarlar ve madde alışverişi')
T_DOGAL=('do2-dogal','Doğal bağışıklık'); T_OZGUL=('do2-ozgul','Özgül bağışıklık ve bağışıklık bozuklukları')
ROMS=['I','II','III','IV']
# ---------- 01 · çift dolaşım şeması · kolay · A ----------
S1={'d':'I ve IV','a':'II ve III','b':'I ve II','c':'III ve IV','e':'I, II ve IV'}
q(1,*T_DONGU,'kolay','Çift dolaşım','Çift dolaşım şemasında kalbe giden ve kalpten çıkan damarlarda taşınan kanın oksijen durumunu belirler.','şekilli','çift dolaşım şeması','çift dolaşım şeması',
 'kalbin sağ yarısı oksijence fakir kanı akciğerlere gönderir; akciğerlerde gaz alışverişiyle zenginleşen kan kalbin sol yarısına döner ve oradan vücuda pompalanır; vücut dokularından dönen kan yeniden oksijence fakirdir','Akciğere giden damarın oksijence zengin kan taşıdığını sanmak; toplardamarların her zaman oksijence fakir kan taşıdığını düşünmek.',
 [A('Kanın akış yönünü izle','Kan kalbin sağ yarısından akciğerlere, akciğerlerden sol yarıya, sol yarıdan vücuda, vücuttan yeniden sağ yarıya akar.','Sağ yarı → akciğer → sol yarı → vücut → sağ yarı'),
  A('Gaz alışverişinin yerini bul','Oksijen akciğerlerde kana geçer, vücut dokularında kandan hücrelere geçer.','Akciğerden önce fakir · akciğerden sonra zengin · dokudan sonra fakir'),
  A('Damarları sınıfla','I numaralı damar akciğere giden, IV numaralı damar dokulardan dönen kanı taşır.','Fakir: I ve IV')],
 metin='Şekilde, insanda çift dolaşımın şematik gösterimi verilmiştir. Oklar kanın akış yönünü, I, II, III ve IV ise kalbe bağlı damarları göstermektedir.\nBuna göre, oksijence fakir kan taşıyan damarların tamamı aşağıdakilerden hangisinde doğru olarak verilmiştir?',
 dogru=S1['d'],sira=yer('A',S1['d'],[S1['a'],S1['b'],S1['c'],S1['e']]),yan=[(S1['a'],'II numaralı damar akciğerlerden kalbe, III numaralı damar kalpten vücuda oksijence zengin kan taşır; bu ikisi fakir kan taşıyan damarlar değildir.','bilgi'),
  (S1['b'],'II numaralı damar akciğerde oksijen almış kanı kalbin sol yarısına getirir; fakir kan taşıyanlar arasında sayılamaz.','bilgi'),
  (S1['c'],'III numaralı damar kalbin sol yarısından vücuda oksijence zengin kan taşır; fakir kan taşıyanlar arasında sayılamaz.','bilgi'),
  (S1['e'],'II numaralı damar da fakir sayılmış; oysa akciğerden dönen kan oksijence zengindir.','bilgi')],
 istenen='Oksijence fakir kan taşıyan damarların tamamı.',ip=['Kanın hangi organda oksijen aldığını, hangi organda oksijen verdiğini düşün.'],
 bilgi=[B('Çift dolaşım','insanda kan bir turda kalpten iki kez geçer; kalbin sağ yarısı kanı akciğerlere, sol yarısı kanı vücuda gönderir')],
 puf='Önce gaz alışverişinin gerçekleştiği iki yeri işaretle, sonra damarları bu yerlere göre sınıfla.',sekil=sekil_cift())
# ---------- 02 · omurgalı kalbi tablosu · kolay · B ----------
S2={'d':'Balık – Kurbağa – Kuş','a':'Kurbağa – Balık – Kuş','b':'Balık – Kuş – Kurbağa','c':'Kurbağa – Kuş – Balık','e':'Kuş – Kurbağa – Balık'}
SK2=tablo_svg(['Canlı','Kulakçık sayısı','Karıncık sayısı','Karıncıkta kan karışması'],[['K','1','1','Yok'],['L','2','1','Var'],['M','2','2','Yok']])
q(2,*T_DONGU,'kolay','Omurgalı kalbi','Omurgalı gruplarının kalp yapılarını kulakçık ve karıncık sayısına göre ayırt eder.','tablo','omurgalı kalbi karşılaştırma tablosu','omurgalı kalbi tablosu',
 'balıkta kalp tek kulakçık ve tek karıncıktan oluşur; kurbağada iki kulakçık ve tek karıncık bulunur, karıncıkta kan karışır; kuş ve memelide iki kulakçık ve iki karıncık vardır, kan karışmaz','Kuşların kalbinde balık gibi tek karıncık bulunduğunu sanmak; kurbağada kanın karışmadığını düşünmek.',
 [A('K’yi tanı','Kalbi tek kulakçık ve tek karıncıktan oluşan omurgalı balıktır.','K: balık'),
  A('L’yi tanı','İki kulakçık, tek karıncık ve karıncıkta kan karışması kurbağaya özgüdür.','L: kurbağa'),
  A('M’yi tanı','İki kulakçık, iki karıncık ve kanın karışmaması kuşta görülür.','M: kuş')],
 metin='Tabloda, balık, kurbağa ve kuş gruplarından birer canlıya ait kalp özellikleri verilmiştir. Canlılar K, L ve M ile gösterilmiştir.\nBuna göre, K, L ve M canlıları sırasıyla aşağıdakilerden hangisinde doğru olarak verilmiştir?',
 dogru=S2['d'],sira=yer('B',S2['d'],[S2['a'],S2['b'],S2['c'],S2['e']]),yan=[(S2['a'],'K balık olmalıdır çünkü tek kulakçık ve tek karıncık balığa aittir; K kurbağa, L balık yazılırsa tablodaki 1–1 ve 2–1 sayıları eşleşmez.','bilgi'),
  (S2['b'],'L için verilen iki kulakçık, tek karıncık ve kan karışması kurbağaya aittir; L kuş yazılırsa karıncık sayısı 2 olmak zorunda kalırdı.','bilgi'),
  (S2['c'],'K balıktır ve M kuştur; bu sıralamada K kurbağa, M balık yazıldığı için tablodaki kulakçık ve karıncık sayıları uyuşmaz.','bilgi'),
  (S2['e'],'M kuş olduğu hâlde bu sıralamada kuş K’ye yazılmıştır; oysa K’nin kalbi tek kulakçık ve tek karıncıktan oluşur.','bilgi')],
 istenen='K, L ve M canlılarının sırasıyla adları.',ip=['Kulakçık ve karıncık sayısının omurgalı gruplarında nasıl arttığını sırala.'],
 bilgi=[B('Omurgalı kalpleri','omurgalılarda kalbin odacık sayısı balıktan kuşa doğru artar; bazı gruplarda karıncıkta kan karışır')],
 puf='Önce tabloda en az odacığı olan canlıyı, sonra kan karışan canlıyı belirle.',sekil=SK2)
# ---------- 03 · pıhtılaşma deneyi · orta · öncüllü · C ----------
d3={'I':(True,'Sitrat Ca²⁺ iyonlarını bağladığında pıhtı oluşmaz, ortama Ca²⁺ verilince oluşur; bu sonuç pıhtılaşmada Ca²⁺ iyonlarının gerekli olduğunu gösterir.'),
    'II':(True,'M tüpüne eklenen CaCl₂ ortama Ca²⁺ sağlar; sitratın etkisi ortadan kalkar ve pıhtı oluşur.'),
    'III':(False,'Üç tüpte de aynı kan kullanılmıştır; L tüpünde pıhtı oluşmaması fibrinojen miktarının azaldığını göstermez, Ca²⁺ eksikliğinden kaynaklanır.')}
r=onc(d3,'C')
SK3=tablo_svg(['Tüp','Eklenen madde','Sonuç'],[['K','Yok','Pıhtı oluştu'],['L','Sodyum sitrat','Pıhtı oluşmadı'],['M','Sodyum sitrat ve CaCl₂','Pıhtı oluştu']])
qo(3,r,*T_KAN,'orta','Kanın pıhtılaşması','Pıhtılaşma deneyinin sonuçlarından Ca²⁺ iyonlarının işlevini çıkarır.','pıhtılaşma deney tablosu','pıhtılaşma deneyi',
 'yaralanmada trombositler ve pıhtılaşma faktörleri etkinleşir; pıhtılaşma faktörleri ve bazı inorganik iyonlar gerekir; protrombin trombine, trombin de fibrinojeni fibrine dönüştürür','Pıhtılaşmayı yalnız trombositlerin yaptığını sanmak; bir maddenin pıhtıyı engellemesini fibrinojenin azalmasına bağlamak.',
 metin='Bir araştırmacı, aynı sağlıklı bireyden alınan eşit hacimli taze kan örneklerini K, L ve M tüplerine koymuş; tüplere tabloda belirtilen maddeleri eklemiştir. Sodyum sitrat kandaki Ca²⁺ iyonlarını bağlayan, CaCl₂ ise ortama Ca²⁺ veren bir maddedir.\nBuna göre,\nI. Pıhtılaşmada Ca²⁺ iyonları gereklidir.\nII. M tüpünde sitratın etkisi, eklenen Ca²⁺ ile ortadan kalkmıştır.\nIII. L tüpünde pıhtı oluşmaması, fibrinojen miktarının azalmasından kaynaklanmıştır.\nifadelerinden hangileri doğrudur?',
 istenen='Doğru olan öncüllerin hangileri olduğu.',ip=['Tüpleri birbiriyle karşılaştırırken hangi maddenin eklenmesinin sonucu değiştirdiğine bak.'],
 bilgi=[B('Pıhtılaşma','kanın pıhtılaşması trombositlerin ve pıhtılaşma faktörlerinin etkinleşmesiyle gerçekleşir; bu olay için pıhtılaşma faktörleri ve bazı inorganik iyonlar gerekir')],
 puf='Sonucu değiştiren tek farkı bulmak için tüpleri ikişerli karşılaştır.',sekil=SK3)
# ---------- 04 · yangısal tepki · orta · şekilli · olumsuz · D ----------
S4={'y':'I numaralı hücre antikor üretir ve bu antikorlar III numaralı hücrelerin fagositoz yapmasını sağlar.','a':'I numaralı hücre bağ dokuda bulunur ve IV ile gösterilen maddeyi salgılar.','b':'IV ile gösterilen madde II numaralı damarın geçirgenliğini artırır.','c':'III numaralı hücreler II numaralı damarın duvarından doku sıvısına geçebilir.','d':'V numaralı canlılar, III numaralı hücreler tarafından hücre içine alınarak parçalanabilir.'}
q(4,*T_DOGAL,'orta','Yangısal tepki','Yangısal tepkideki hücre ve maddeleri şekil üzerinde işlevleriyle ilişkilendirir.','şekilli','yangısal tepki şeması','yangısal tepki şeması',
 'hasarlı dokuda mast hücreleri histamin salgılar; histamin kılcal damar geçirgenliğini artırır; akyuvarlar damardan çıkıp mikropları fagositozla yok eder','Mast hücrelerini antikor üreten hücre sanmak; yangısal tepkiyi özgül bağışıklığın parçası saymak.',
 [A('Yapıları tanı','Bağ dokudaki granüllü hücre mast hücresi, damardan çıkan lobu çekirdekli hücre fagosittir; V mikroorganizmadır.','I: mast hücresi · II: kılcal damar · III: fagosit · IV: histamin · V: bakteri'),
  A('Doğru ifadeleri ayır','Histamin salgısı, geçirgenlik artışı, akyuvar göçü ve fagositoz yangısal tepkinin basamaklarıdır.','Dört ifade bu basamaklarla uyumludur'),
  A('Mast hücresinin işlevini sına','Mast hücresi histamin salgılar; antikor üretimi B lenfositlerine aittir.','Antikor üretimi I’in işlevi değil'),
  A('Yanlışı seç','Mast hücresine antikor üretimini yükleyen ifade yanlıştır.','Cevap: I antikor üretir ifadesi')],
 metin='Şekilde, deride oluşan bir yaranın ardından gelişen yangısal tepkinin bir evresi gösterilmiştir. IV ile gösterilen madde, I numaralı hücre tarafından salgılanan histamindir ve yapılar I, II, III, IV ve V ile numaralandırılmıştır.\nBuna göre, numaralı yapılarla ilgili aşağıdakilerden hangisi yanlıştır?',
 dogru=S4['y'],sira=yer('D',S4['y'],[S4['a'],S4['b'],S4['c'],S4['d']]),yan=[(S4['a'],'Mast hücreleri bağ dokuda bulunur ve histamin salgılar; ifade doğrudur.','bilgi'),
  (S4['b'],'Histamin kılcal damarların geçirgenliğini artırır ve akyuvarların dokuya geçmesini kolaylaştırır; ifade doğrudur.','bilgi'),
  (S4['c'],'Fagositler damar duvarından doku sıvısına geçerek yara bölgesine ulaşır; ifade doğrudur.','bilgi'),
  (S4['d'],'Fagositler mikroorganizmaları hücre içine alıp parçalar; ifade doğrudur.','bilgi')],
 istenen='Yanlış olan ifade.',ip=['Yangısal tepkideki her hücrenin hangi maddeyi salgıladığını ya da hangi işi yaptığını ayrı ayrı sına.'],
 bilgi=[B('Yangısal tepki','doku hasarında mast hücrelerinden histamin salgılanır; damar geçirgenliği artar ve akyuvarlar bölgeye göç ederek fagositoz yapar')],
 puf='Her hücrenin yangıdaki görevini ayrı ayrı sına.',sekil=sekil_yangi())
# ---------- 05 · toplardamar kapakçık · orta · olumsuz · E ----------
S5={'y':'II numaralı kapakçık açık, III numaralı kapakçık kapalıdır.','a':'Kasların kasılması IV numaralı toplardamar bölümüne baskı yaparak kanın kalbe doğru ilerlemesine yardım eder.','b':'II numaralı kapakçık kapalıdır ve kanın IV numaralı bölümden geriye akmasını engeller.','c':'Kas gevşediğinde kan geriye doğru akmak ister ancak III numaralı kapakçık kapanarak bunu engeller.','d':'Toplardamarlarda kan basıncı düşük olduğundan kanın kalbe dönüşünde kapakçıklar ve kas kasılması önem taşır.'}
q(5,*T_DAMAR,'orta','Toplardamar kapakçıkları','Çevre kaslarının kasılmasıyla toplardamarda kanın tek yönlü ilerlemesini kapakçık durumlarıyla açıklar.','şekilli','toplardamar ve iskelet kası şeması','toplardamar kapakçık şeması',
 'toplardamarlarda kan basıncı düşüktür; iskelet kaslarının kasılması damara baskı yapar, kapakçıklar kanın yalnız kalbe doğru akmasını sağlar','Toplardamarda kanın kalbin kasılmasıyla ilerlediğini sanmak; kapakçıkların kanı ters yöne ittiğini düşünmek.',
 [A('Şekli oku','Kas kasılmış; kan kalbe doğru ilerliyor. Alttaki kapakçığın yaprakları birleşmiş, üsttekiler birbirinden ayrılmıştır.','II: kapalı · III: açık'),
  A('Kan akışını yorumla','Kapalı kapakçık kanın geriye akmasını engeller; açık kapakçık kanın kalbe doğru geçmesine izin verir.','Alt kapakçık geri akışı önler · üst kapakçık geçişe izin verir'),
  A('Diğer ifadeleri sına','Kas baskısı ve kapakçıklar toplardamarda kan dönüşünü sağlar; kas gevşediğinde üst kapakçık kapanır.','Dört ifade uyumlu'),
  A('Yanlışı seç','Kapakçık durumlarını ters veren ifade yanlıştır.','Cevap: II açık, III kapalı ifadesi')],
 metin='Şekilde, bir bacak toplardamarının iskelet kaslarının kasıldığı andaki durumu gösterilmiştir. Kanın akış yönü şekilde belirtilmiş, yapılar I, II, III ve IV ile numaralandırılmıştır. I numaralı yapılar iskelet kaslarıdır.\nBuna göre, aşağıdaki ifadelerden hangisi yanlıştır?',
 dogru=S5['y'],sira=yer('E',S5['y'],[S5['a'],S5['b'],S5['c'],S5['d']]),yan=[(S5['a'],'Kasılan kaslar toplardamara baskı yapar ve kanı kalbe doğru iter; ifade doğrudur.','bilgi'),
  (S5['b'],'Şekilde II numaralı kapakçığın yaprakları birleşmiştir; kapalı kapakçık kanın geri akışını engeller ve ifade doğrudur.','bilgi'),
  (S5['c'],'Kas gevşediğinde üstteki kapakçık kapanır ve geri akışı engeller; ifade doğrudur.','bilgi'),
  (S5['d'],'Toplardamarlardaki düşük basınç nedeniyle kanın dönüşünde kas baskısı ve kapakçıklar önemlidir; ifade doğrudur.','bilgi')],
 istenen='Yanlış olan ifade.',ip=['Kapakçıkların yapraklarının birleşip ayrılmasının kanın hangi yöne geçişini etkilediğini düşün.'],
 bilgi=[B('Toplardamar yapısı','toplardamarlarda kan basıncı düşüktür; iç yüzeydeki kapakçıklar kanın yalnız kalbe doğru akmasını sağlar')],
 puf='Şekildeki kapakçık yapraklarının birleşik mi ayrık mı olduğuna bak; ifadeleri buna göre sına.',sekil=sekil_toplardamar())
# ---------- 06 · bağışıklık bozuklukları · orta · öncüllü · olumsuz · A ----------
d6={'I':(True,'Alerjide bağışıklık sistemi, zararsız bir maddeye (alerjene) karşı aşırı yanıt verir; ifade doğrudur.'),
    'II':(True,'Otoimmün hastalıklarda bağışıklık sistemi kişinin kendi hücrelerine karşı yanıt oluşturur; ifade doğrudur.'),
    'III':(False,'Doku ve organ naklinde verici ile alıcının doku uyumu arttıkça ret riski azalır; ifade yanlıştır.')}
r=onc(d6,'A','yanlis')
qo(6,r,*T_OZGUL,'orta','Bağışıklık bozuklukları','Alerji, otoimmün hastalık ve doku reddi kavramlarını bağışıklık sistemi açısından değerlendirir.','alerji, otoimmün hastalık, doku reddi','bağışıklık bozuklukları yargıları',
 'alerjide zararsız maddeye aşırı yanıt, otoimmün hastalıkta kendi hücrelerine yanıt, nakilde ise yabancı dokuya yanıt söz konusudur; doku uyumu arttıkça ret azalır','Otoimmün hastalığı mikroorganizmaya karşı yanıt sanmak; doku uyumu arttıkça retin arttığını düşünmek.',
 metin='İnsanda bağışıklık sisteminin işleyişindeki bazı bozukluklar ve durumlar şunlardır: alerji, otoimmün hastalıklar ve nakledilen doku ya da organın reddedilmesi.\nBuna göre,\nI. Alerjide bağışıklık sistemi zararsız bir maddeye karşı aşırı yanıt verir.\nII. Otoimmün hastalıklarda bağışıklık sistemi kişinin kendi hücrelerine karşı yanıt oluşturur.\nIII. Doku ve organ naklinde verici ile alıcı arasındaki doku uyumu arttıkça ret riski de artar.\nifadelerinden hangileri yanlıştır?',
 istenen='Yanlış olan öncüllerin hangileri olduğu.',ip=['Her durumda bağışıklık sisteminin hangi maddeye ya da hücreye yanıt verdiğini ayrı ayrı düşün.'],
 bilgi=[B('Bağışıklık bozuklukları','alerji, otoimmün hastalık ve doku reddi bağışıklık sisteminin istenmeyen yanıtlarıdır')],
 puf='Her öncülde yanıtın hedefini belirle; sonra doku uyumu ile ret ilişkisini yönüyle sına.')
# ---------- 07 · kılcal damar grafikleri · orta · B ----------
S7={'d':'K: Oksijen · L: Karbondioksit · M: Hemoglobin','a':'K: Karbondioksit · L: Oksijen · M: Hemoglobin','b':'K: Oksijen · L: Karbondioksit · M: Laktik asit','c':'K: Oksijen · L: Hemoglobin · M: Karbondioksit','e':'K: Hemoglobin · L: Oksijen · M: Karbondioksit'}
q(7,*T_DAMAR,'orta','Kılcal damar','Çalışan bir dokunun kılcal damarı boyunca madde miktarı değişimlerini grafiklerden tanır.','grafik','kılcal damar boyunca madde miktarı grafikleri','kılcal damar madde değişimi grafikleri',
 'kılcal damarda atardamar ucundan toplardamar ucuna madde miktarı, maddenin hücrelerce kullanılmasına ya da üretilmesine ve kılcal damar duvarından geçip geçmemesine göre değişir','Hücrelerin kandan aldığı maddenin kılcal damar boyunca arttığını sanmak; kandan ayrılmayan maddenin de azaldığını düşünmek.',
 [A('K grafiğini yorumla','Atardamar ucundan toplardamar ucuna azalan madde doku hücrelerince kullanılan maddedir.','K: azalıyor → oksijen'),
  A('L grafiğini yorumla','Hücrelerce üretilip kana geçen madde toplardamar ucuna doğru artar.','L: artıyor → karbondioksit'),
  A('M grafiğini yorumla','Alyuvarın içinde bulunan ve kılcal damardan ayrılmayan madde miktarı değişmez.','M: sabit → hemoglobin')],
 metin='Şekilde, çalışmakta olan bir iskelet kasındaki kılcal damarın atardamar ucundan toplardamar ucuna doğru akan kanda bazı maddelerin miktarındaki değişim K, L ve M grafikleriyle gösterilmiştir. Bu değişimlerin üç farklı maddeye ait olduğu bilinmektedir.\nBuna göre, K, L ve M grafikleri aşağıdaki maddelerden hangileriyle doğru eşleştirilmiştir?',
 dogru=S7['d'],sira=yer('B',S7['d'],[S7['a'],S7['b'],S7['c'],S7['e']]),yan=[(S7['a'],'K ve L ters yazılmıştır; kasta oksijen kullanıldığı için azalan eğri oksijene, artan eğri karbondioksite aittir.','bilgi'),
  (S7['b'],'M grafiği sabit kalmaktadır; çalışan kasta laktik asit üretilip kana geçtiğinden laktik asit miktarı toplardamar ucuna doğru artar ve M ile eşleşmez.','bilgi'),
  (S7['c'],'L grafiği artmaktadır; hemoglobin alyuvardan ayrılmadığı için artmaz, artan madde karbondioksittir.','bilgi'),
  (S7['e'],'K grafiği azalmaktadır; hemoglobin miktarı değişmediği için azalan eğri hemoglobine değil oksijene aittir.','bilgi')],
 istenen='K, L ve M grafikleriyle doğru eşleştirilen maddeler.',ip=['Çalışan bir doku hücresinin kandan hangi maddeyi aldığını, kana hangi maddeyi verdiğini düşün.'],
 bilgi=[B('Kılcal damarda madde alışverişi','dokulardaki kılcal damarlarda kanla hücreler arasında madde alışverişi gerçekleşir; kanla hücreler arasındaki geçiş kılcal damar duvarından olur')],
 puf='Eğrinin yönünü (azalan, artan, sabit) önce yaz; sonra her yönü bir maddeyle ilişkilendir.',sekil=sekil_kilcal())
# ---------- 08 · deri nakli deneyi · zor · öncüllü · C ----------
d8={'I':(True,'Ret süresinin 12 günden 4 güne inmesi, ilk nakilde oluşan hafıza T hücrelerinin ikinci karşılaşmada hızlı yanıt vermesiyle açıklanır.'),
    'II':(False,'Timusu alınmış farede T lenfositleri yoktur ama B lenfositleri ve antikorlar vardır; ret görülmemesi, reddin antikorlarla değil T lenfositlerle gerçekleştiğini gösterir.'),
    'III':(True,'Timussuz farede ret görülmezken T lenfositleri aktarılınca hızlı ret görülür; bu, doku reddinde T lenfositlerin görevli olduğunu destekler.')}
r=onc(d8,'C')
SK8=tablo_svg(['Deney','Y soyundan farenin durumu','Ret süresi'],[['1','Daha önce nakil yok','12 gün'],['2','Ret sonrası 30. günde X nakli','4 gün'],['3','Timusu alınmış','Ret yok'],['4','Timussuz + T lenfosit','4 gün']])
qo(8,r,*T_OZGUL,'zor','Doku reddi deneyi','Deri nakli deneyinin sonuçlarından hafıza hücreleri ve T lenfositlerin doku reddindeki rolünü çıkarır.','deri nakli deney tablosu','deri nakli ve ret süresi',
 'nakledilen dokunun reddi hücresel bağışıklıkla gerçekleşir; ilk karşılaşmada hafıza T hücreleri oluşur, ikinci karşılaşmada ret daha hızlıdır; timus T lenfositlerin olgunlaştığı yerdir','Doku reddini antikorlara bağlamak; hafıza hücrelerini yalnız B lenfositlere özgü sanmak.',
 metin='Saf ırk X soyundan farelerin derisi, saf ırk Y soyundan farelere nakledilmiş ve nakil yerindeki deri parçasının reddedilmesi için geçen süre izlenmiştir. Her deneyde Y soyundan fareler tabloda belirtilen durumdadır; 2. deneyde, 1. deneydeki ret tamamlandıktan 30 gün sonra aynı fareye yine X soyundan deri nakledilmiştir. Nakil yapılan fare, deneyde kendi yaşamı boyunca başka bir antijenle karşılaşmamıştır.\nBuna göre,\nI. 2. deneyde ret süresinin kısalması, 1. deneyde oluşan hafıza hücreleriyle açıklanır.\nII. 3. deneyde ret görülmemesi, doku reddinden antikorların sorumlu olduğunu gösterir.\nIII. 3. ve 4. deneyler birlikte, doku reddinde T lenfositlerin görevli olduğunu destekler.\nifadelerinden hangileri doğrudur?',
 istenen='Doğru olan öncüllerin hangileri olduğu.',ip=['Hangi fare grubunda hangi lenfosit türünün bulunmadığını ya da sonradan eklendiğini belirleyip sonuçla ilişkilendir.'],
 bilgi=[B('Hücresel bağışıklık','T lenfositler timusta olgunlaşır; yabancı doku hücrelerine karşı hücresel bağışıklıkta görev alır ve hafıza hücreleri oluşturur')],
 puf='Önce ilk satırı referans al; sonra her satırın referanstan hangi tek farkla ayrıldığına bak.',sekil=SK8)
# ---------- 09 · egzersizde kan akışı · zor · D ----------
q(9,*T_DAMAR,'zor','Kanın organlara dağılımı','Egzersizde toplam debi ve organlara giden kan miktarındaki değişimi mutlak ve oransal olarak karşılaştırır.','grafik','dinlenme–egzersiz organ kan akışı sütun grafiği','organ kan akışı sütun grafiği',
 'egzersizde kalpten pompalanan toplam kan artar ve kan kaslara yönelir; bazı organlara giden miktar azalabilir; bir organın payı ile mutlak miktarı birbirinden ayrı değerlendirilir','Kan miktarı sabit kalan organın payının da sabit kaldığını sanmak; kas dışı organlara giden kan miktarının arttığını düşünmek.',
 [A('Toplam debiyi karşılaştır','Dinlenmede toplam kan akışı 5000 mL/dk, egzersizde 20000 mL/dk’dır.','20000 / 5000 = 4 kat'),
  A('Kasın değerlerini hesapla','Kas için dinlenme 1000, egzersiz 12000 mL/dk’dır; payı toplam debiye oranlanır.','12000 / 1000 = 12 kat · 1000 / 5000 = %20 · 12000 / 20000 = %60'),
  A('Diğer ifadeleri sına','Böbrek azalması 600, kas artışı 11000 mL/dk’dır; beynin mutlak değeri aynı olsa da payı küçülür; sindirimin payı yaklaşık onda bire iner; kas dışı üç organın toplamı 3000’den 1700’e düşer.','Dört ifade yanlış'),
  A('Doğruyu seç','Hesaplanan oranlarla uyuşan ifade seçilir.','Cevap: 4 kat · 12 kat · %20 → %60')],
 metin='Grafikte, sağlıklı bir bireyin dinlenme ve şiddetli egzersiz sırasında bazı organlara giden kan akışı verilmiştir. Bu bireyde toplam kalp debisi dinlenmede 5000 mL/dk, egzersizde 20000 mL/dk’dır. Grafikte gösterilmeyen diğer organlar da kan almaktadır.\nBuna göre, aşağıdakilerden hangisi söylenebilir?',
 dogru='Toplam debi 4 kat artarken kasa giden kan akışı 12 kat artmış, kasın toplam debideki payı %20’den %60’a çıkmıştır.',
 sira=yer('D','Toplam debi 4 kat artarken kasa giden kan akışı 12 kat artmış, kasın toplam debideki payı %20’den %60’a çıkmıştır.',['Böbreğe giden kan akışındaki azalma, kasa giden kan akışındaki artıştan daha fazladır.','Beyne giden kan akışı değişmediğinden beynin toplam debideki payı da değişmemiştir.','Sindirim sistemine giden kanın toplam debideki payı, dinlenmedekinin yarısına inmiştir.','Kas dışında kalan üç organa giden toplam kan akışı, egzersizde dinlenmedekinden fazladır.']),
 yan=[('Böbreğe giden kan akışındaki azalma, kasa giden kan akışındaki artıştan daha fazladır.','Böbrekte azalma 1100 − 500 = 600 mL/dk, kasta artış 12000 − 1000 = 11000 mL/dk’dır; artış çok daha büyüktür.','islem'),
  ('Beyne giden kan akışı değişmediğinden beynin toplam debideki payı da değişmemiştir.','Beyin akışı 700 mL/dk kalır ama toplam 5000’den 20000’e çıktığı için payı %14’ten %3,5’e düşer.','islem'),
  ('Sindirim sistemine giden kanın toplam debideki payı, dinlenmedekinin yarısına inmiştir.','Sindirimin payı 1200/5000 = %24’ten 500/20000 = %2,5’e iner; bu yaklaşık onda birdir, yarısı değildir.','islem'),
  ('Kas dışında kalan üç organa giden toplam kan akışı, egzersizde dinlenmedekinden fazladır.','Üç organın toplamı dinlenmede 700 + 1200 + 1100 = 3000, egzersizde 700 + 500 + 500 = 1700 mL/dk’dır; azalmıştır.','islem')],
 istenen='Grafik ve verilen debilerden söylenebilen ifade.',ip=['Mutlak kan miktarı ile toplam debideki payı ayrı ayrı hesapla.'],
 bilgi=[B('Kalp debisi ve dağılımı','kalbin dakikada pompaladığı kan miktarı kalp debisidir; organlara dağılımı organın etkinliğine göre değişir')],
 puf='Her ifade için önce mutlak değerleri, sonra toplam debiye oranlarını hesapla.',sekil=sekil_bar())
# ---------- 10 · HIV grafiği · zor · öncüllü · yanlış · E ----------
d10={'I':(True,'Virüs yardımcı T lenfositlerinde çoğalır; enfeksiyonun başında K eğrisinin yükselmesi bununla uyumludur ve ifade doğrudur.'),
     'II':(False,'K eğrisi 2. ve 8. yıl arasında düşük kalırken L eğrisi 82’den 34’e azalmaktadır; L sabit kalmaz, ifade yanlıştır.'),
     'III':(False,'HIV alyuvarları değil, yardımcı T lenfositlerini yok eder; fırsatçı enfeksiyonlar bağışıklık sisteminin zayıflamasından kaynaklanır ve ifade yanlıştır.')}
assert KV[3]==10 and KV[6]==20 and LT[3]==82 and LT[6]==34 and LT[3]>LT[6] and KV[1]>KV[2]
r=onc(d10,'E','yanlis')
qo(10,r,*T_OZGUL,'orta','HIV ve bağışıklık yetmezliği','Enfeksiyon sürecinde virüs miktarı ve T lenfosit sayısı grafiğini bağışıklık yetmezliği mekanizmasıyla birleştirir.','HIV enfeksiyonu virüs–T lenfosit grafiği','HIV grafiği',
 'HIV bağışıklık sistemi hücrelerini hedef alan bir virüstür; hastalığın seyri virüs miktarı ile ilgili hücre sayısının birlikte izlenmesiyle yorumlanır','Virüsün alyuvarlara saldırdığını sanmak; virüs miktarı düşükken T lenfosit sayısının sabit kaldığını düşünmek.',
 metin='Grafikte, HIV ile enfekte olmuş ve tedavi görmeyen bir bireyde kandaki virüs miktarı ile yardımcı T lenfosit sayısının zamanla değişimi, başlangıç değerlerine göre göreli olarak verilmiştir. Eğrilerden biri virüs miktarını, diğeri yardımcı T lenfosit sayısını göstermektedir.\nBuna göre,\nI. K eğrisinin ilk haftalarda hızla yükselmesi, virüsün yardımcı T lenfositlerinde çoğalmasıyla ilişkilidir.\nII. K eğrisinin 2. ve 8. yıl arasında düşük kalması, bu dönemde L eğrisinin sabit kaldığını gösterir.\nIII. Hastalığın son döneminde görülen fırsatçı enfeksiyonlar, virüsün alyuvarları yok etmesinden kaynaklanır.\nifadelerinden hangileri yanlıştır?',
 istenen='Yanlış olan öncüllerin hangileri olduğu.',ip=['Hangi eğrinin virüse, hangisinin yardımcı T lenfositlere ait olduğunu, virüsün hedef hücresine bakarak belirle.'],
 bilgi=[B('Bağışıklık yetmezliği','HIV, bağışıklık sisteminin hücrelerini hedef alan bir virüstür; hastalığın seyri virüs miktarı ve ilgili hücre sayısıyla izlenir')],
 puf='Önce eğrileri virüs ve T lenfosit olarak adlandır; sonra her öncülü grafikten ve mekanizmadan ayrı ayrı sına.',sekil=sekil_hiv())
# ---------- bitiş ----------
for q_ in P.ANA: q_['kardes']=None
P.yaz(os.path.join(GD,'dolasimiki-1.json'),os.path.join(SCR:='/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad','kardes-dolasimiki.json'))
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=KK))['kartlar'].append(c['id'])
json.dump(dict(konu=KONUAD,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2018–2026 Biyoloji dolaşım ve bağışıklık soruları (yalnız mantık), MEB 11–12. sınıf biyoloji müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','abdolasimiki.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
