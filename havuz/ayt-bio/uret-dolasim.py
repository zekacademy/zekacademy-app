"""AYT Biyoloji · Dolaşım ve Bağışıklık Sistemi · 20 soru. Kardeş yok, ipucu 1.
Şekil verileri (basınç eğrileri, damar eğrileri, soy ağacı, kan grubu tabloları) Python'da tanımlanır; kapakçık durumları, olasılıklar ve öncül doğrulukları
buradan hesaplanıp assert edilir; anahtar, adım ve çeldirici açıklamaları oradan üretilir."""
import sys,os,math,json
from fractions import Fraction as Fr
BD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(BD,'..')
sys.path.insert(0,os.path.join(HV,'tyt-bio')); sys.path.insert(0,HV)
import _hafif_bio as H
from _hafif_bio import *
KONU_='Dolaşım ve Bağışıklık Sistemi'; UK='abio|Dolaşım ve Bağışıklık Sistemi'; H.KONU=KONU_
P=Parti('dolasim',KONU_,UK,ders='AYT Biyoloji',idon='aytbio')
KY='ÖSYM AYT 2018–2026 Biyoloji dolaşım ve bağışıklık soruları (yalnız mantık) · MEB 11. sınıf Dolaşım ve Bağışıklık'
TIP={'kalp':('abdo-kalp','Kalbin yapısı ve kan akışı'),'dongu':('abdo-kalp-dongusu','Kalp döngüsü, kalp atışı ve debi'),'damar':('abdo-damar','Damarlar ve kan basıncı'),
     'kan':('abdo-kan','Kan hücreleri ve kan grupları'),'lenf':('abdo-lenf','Lenf sistemi'),'bag':('abdo-bagisiklik','Bağışıklık türleri, aşı ve serum')}
USED=[]
def Q(no,tp,z,kalip,alt,kaz,ne,fikir,tuzak,ad,**k):
    assert len(k['ip'])==1 and no not in USED; USED.append(no)
    t,tn=TIP[tp]; kart(f'K-ABDO-{no[-2:]}',alt,fikir,tuzak,z,kalip,len(ad),t,tn,KY)
    mk(P,no,ad=ad,adim=len(ad),tipId=t,tip=tn,z=z,kalip=kalip,alt=alt,kaz=kaz,kart=f'K-ABDO-{no[-2:]} ({tn.lower()}) · {ne}',**k)
ORD=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
SETS=[('I',),('II',),('III',),('I','II'),('I','III'),('II','III'),('I','II','III')]
def onc(d,harf):
    T=tuple(k for k in d if d[k][1]); i=SETS.index(T); p='ABCDE'.index(harf)
    assert i-2<=p<=i,('harf uygun degil',T,harf)
    ops=SETS[:i][:p]+[T]+SETS[i+1:][:4-p]; assert len(ops)==5
    sira=[ORD[SETS.index(o)] for o in ops]; yan=[]
    for o in ops:
        if o==T: continue
        pr=[]
        for x in sorted(set(o)-set(T),key=lambda z:'I II III'.split().index(z)): pr.append(f'{x} öncülünü doğru sanmış; oysa yanlıştır: {d[x][2]}')
        for x in sorted(set(T)-set(o),key=lambda z:'I II III'.split().index(z)): pr.append(f'{x} öncülünü yanlış sanmış; oysa doğrudur: {d[x][2]}')
        yan.append((ORD[SETS.index(o)],'. '.join(pr)+'.','bilgi'))
    return dict(dogru=ORD[i],yan=yan,sira=sira)
def omet(giris,d,kok): return giris+'\n'+'\n'.join(f'{x}. {d[x][0]}' for x in d)+'\n'+kok
def oad(d,bas=None):
    a=list(bas or [])
    for x in d: a.append(A(f'{x}. öncülü incele',d[x][2][0].upper()+d[x][2][1:]+'.',('doğru' if d[x][1] else 'yanlış')))
    T=[x for x in d if d[x][1]]
    a.append(A('Sonucu yaz','Doğru olan öncüller bir arada yazılır.',' ve '.join(T) if len(T)<3 else 'I, II ve III'))
    return a
def tek(items,hedef,harf,sanc):
    """items: [(metin,bayrak,not)]; hedef: cevap olan bayrak değeri; sanc(metin,not)->çeldirici açıklaması."""
    h=[s for s in items if s[1]==hedef]; assert len(h)==1,[s[0] for s in h]
    dg=h[0]; dig=[s for s in items if s[1]!=hedef]; assert len(dig)==4
    sira=dig[:]; sira.insert('ABCDE'.index(harf),dg)
    yan=[(m,sanc(m,n),'bilgi') for m,b,n in dig]
    return dict(dogru=dg[0],yan=yan,sira=[s[0] for s in sira]),dg[2]
def sanc_dogru(m,n): return f'Bu ifadeyi doğru sanmış; oysa yanlıştır: {n}.'
def sanc_yanlis(m,n): return f'Bu ifadeyi yanlış sanmış; oysa doğrudur: {n}.'

# ======================= ŞEKİL YARDIMCILARI =======================
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
ARR='-{Stealth[length=2.3mm,width=1.9mm]}'
def tk(g,sc=1.0): return tikz_svg(HEAD.replace('font=\\small]',f'font=\\small,scale={sc}]')+g+TAIL)
def pl(pts,ex='',sm=True): return '\\draw[%s] plot%s coordinates {%s};'%(ex,'[smooth]' if sm else '',' '.join(f'({x:.2f},{y:.2f})' for x,y in pts))
def tube(c,w,fill=True,kapat=True,col='cyan!25'):
    """c: orta çizgi noktaları; iki yan çizgi + serbest uç kapağı."""
    n=len(c); L=[];R=[]
    for i,(x,y) in enumerate(c):
        a=c[max(i-1,0)]; b=c[min(i+1,n-1)]; dx,dy=b[0]-a[0],b[1]-a[1]; m=math.hypot(dx,dy); nx,ny=-dy/m,dx/m
        L.append((x+nx*w/2,y+ny*w/2)); R.append((x-nx*w/2,y-ny*w/2))
    s=''
    if fill: s+='\\fill[%s] plot[smooth]'%col+' coordinates {%s} -- plot[smooth] coordinates {%s} -- cycle;'%(' '.join(f'({x:.2f},{y:.2f})' for x,y in L),' '.join(f'({x:.2f},{y:.2f})' for x,y in R[::-1]))
    s+=pl(L,'line width=1pt')+pl(R,'line width=1pt')
    if kapat: s+='\\draw[line width=1pt] (%.2f,%.2f)--(%.2f,%.2f);'%(L[-1][0],L[-1][1],R[-1][0],R[-1][1])
    return s
def kalp(et):
    """et: {anahtar:rakam}. anahtarlar: svc (üst ana toplardamar), pa (akciğer atardamarı), pv (akciğer toplardamarı), ao (aort), ra, la, rv, lv (odacıklar)."""
    b=[]
    # tüpler
    b.append(tube([(-2.0,2.0),(-2.0,3.7)],.7))                                   # üst ana toplardamar
    b.append(tube([(-.35,.3),(-.35,2.0),(-.5,2.6),(-1.25,2.85)],.6))              # akciğer atardamarı
    b.append(tube([(.5,.3),(.5,1.8),(.9,2.6),(1.8,3.0),(2.7,2.7),(3.1,2.0)],.6))   # aort
    b.append(tube([(3.7,1.45),(2.5,1.4)],.5,kapat=True)); b.append(tube([(3.7,.85),(2.5,.9)],.5,kapat=True))  # akciğer toplardamarları
    # kulakçıklar
    b.append('\\draw[line width=1.2pt,fill=orange!30] (-1.6,1.25) ellipse (.85 and .95);\\draw[line width=1.4pt] (-1.6,1.25) ellipse (.85 and .95);')
    b.append('\\draw[line width=1.2pt,fill=orange!30] (1.8,1.25) ellipse (.8 and .95);\\draw[line width=1.4pt] (1.8,1.25) ellipse (.8 and .95);')
    # karıncıklar (dış hat) ve sol karıncık iç boşluğu (kalın duvar)
    dis=[(-2.3,.3),(-2.35,-.9),(-1.5,-2.2),(0,-2.95),(.9,-3.1),(1.9,-2.5),(2.6,-1.2),(2.6,.3)]
    b.append('\\fill[orange!30] plot[smooth] coordinates {%s} -- cycle;'%' '.join(f'({x:.2f},{y:.2f})' for x,y in dis))
    b.append(pl(dis,'line width=1.4pt'))
    b.append('\\draw[line width=1.2pt] (.1,.3)--(.95,-2.9);')                                           # septum
    b.append(pl([(.45,.3),(.5,-1.2),(.95,-2.5),(1.65,-1.9),(2.15,-.9),(2.15,.3)],'line width=1pt'))     # sol karıncık boşluğu
    # AV hattı (kapakçık boşlukları) ve kapakçık yaprakları
    for x1,x2 in [(-2.3,-1.9),(-.9,-.65),(-.05,.2),(.8,1.2),(2.1,2.6)]: b.append(f'\\draw[line width=1.4pt] ({x1},.3)--({x2},.3);')
    b.append('\\draw[line width=1.1pt] (-1.9,.3)--(-1.6,-.35);\\draw[line width=1.1pt] (-.9,.3)--(-1.2,-.35);')
    b.append('\\draw[line width=1.1pt] (1.2,.3)--(1.45,-.3);\\draw[line width=1.1pt] (2.1,.3)--(1.85,-.3);')
    b.append('\\draw[line width=1pt] (-.65,.62)--(-.35,.38)--(-.05,.62);\\draw[line width=1pt] (.2,.62)--(.5,.38)--(.8,.62);')   # yarım ay kapakçıklar
    # etiketler
    orta={'ra':(-1.6,1.25),'la':(1.8,1.25),'rv':(-1.0,-1.1),'lv':(1.3,-1.2)}
    uz={'svc':((-3.3,3.6),(-2.4,3.3)),'pa':((-.35,3.75),(-.35,2.62)),'ao':((1.8,4.2),(1.8,3.25)),'pv':((4.7,1.15),(3.3,1.15))}
    for k,r in et.items():
        if k in orta: b.append(f'\\node[font=\\large\\bfseries] at ({orta[k][0]},{orta[k][1]}) {{{r}}};')
        else:
            (tx,ty),(ax,ay)=uz[k]; b.append(f'\\node[font=\\large\\bfseries] at ({tx},{ty}) {{{r}}};\\draw[{ARR},line width=.8pt] ({tx+(.0 if abs(tx-ax)<.01 else (.3 if ax>tx else -.3))},{ty-(.28 if abs(tx-ax)<.01 else 0)})--({ax},{ay});')
    return tk(''.join(b),.8)
def eksen(W,Hh,xlab,ylab,xt=(),yt=(),xs=1,ys=1,xtl=None,ytl=None,ylab_gap=.9,xly=-.75):
    s=f'\\draw[-{{Stealth}},line width=1pt] (0,0)--({W+.35},0);\\draw[-{{Stealth}},line width=1pt] (0,0)--(0,{Hh+.35});'
    for x in xt: s+=f'\\draw (%.2f,.07)--(%.2f,-.07);\\node[below=1pt] at (%.2f,-.05) {{%s}};'%(x*xs,x*xs,x*xs,(xtl or {}).get(x,str(x)))
    for y in yt: s+=f'\\draw (.07,%.2f)--(-.07,%.2f);\\node[left=1pt] at (-.05,%.2f) {{%s}};'%(y*ys,y*ys,y*ys,(ytl or {}).get(y,str(y)))
    s+=f'\\node[anchor=north] at ({W/2:.2f},{xly}) {{{xlab}}};\\node[rotate=90,anchor=south] at (-{ylab_gap},{Hh/2:.2f}) {{{ylab}}};'
    return s

# ======================= 01 · kolay · şekil · olumsuz · kalp yapısı =======================
S1=kalp({'svc':1,'pa':2,'la':3,'lv':4,'ao':5})
it=[('5 numaralı damardaki kan basıncı, 2 numaralı damardaki kan basıncından daha düşüktür.',False,'aort, sol karıncığın yüksek basınçla pompaladığı kanı taşır; akciğer atardamarındaki basınç ise sistem dolaşımındakinden çok daha düşüktür'),
    ('1 numaralı damar, vücuttan gelen oksijence fakir kanı sağ kulakçığa taşır.',True,'üst ana toplardamar, baş ve kollardan dönen oksijence fakir kanı sağ kulakçığa getirir'),
    ('2 numaralı damarda oksijence fakir kan bulunur.',True,'akciğer atardamarı, sağ karıncıktan çıkan oksijence fakir kanı akciğerlere götürür'),
    ('3 numaralı bölüme akciğerlerden gelen oksijence zengin kan dolar.',True,'sol kulakçık, akciğer toplardamarlarıyla gelen oksijence zengin kanı alır'),
    ('4 numaralı bölümün duvarı, sağ karıncığın duvarından daha kalındır.',True,'sol karıncık kanı bütün vücuda pompaladığı için duvarı sağ karıncıktan daha kalındır')]
r,g=tek(it,False,'A',sanc_yanlis)
Q('0001','kalp','kolay','şekilli','Kalbin bölümleri ve damarlar','Kalp odacıkları ve ona bağlı damarlar için kan akışı, oksijen durumu ve basınç ilişkilerini değerlendirir.','numaralı kalp şeması, olumsuz kök',
 'Her numaranın hangi odacık ya da damar olduğunu belirleyip taşıdığı kanın oksijen durumu ve basıncı ile ilişkilendirmek gerekir.','Damarların taşıdığı kanın özelliklerini karıştırmak.',
 [A('Numaraları adlandır','Şekilde 1 üst ana toplardamar, 2 akciğer atardamarı, 3 sol kulakçık, 4 sol karıncık, 5 aorttur.','1 üst ana toplardamar · 2 akciğer atardamarı · 3 sol kulakçık · 4 sol karıncık · 5 aort'),
  A('Kanın niteliğini belirle','Akciğer atardamarı ve üst ana toplardamar oksijence fakir kan taşır; sol kulakçık akciğerden oksijence zengin kan alır.','2 ve 1: oksijence fakir · 3: oksijence zengin'),
  A('Basınç ve duvar kalınlığı','Sol karıncık kanı tüm vücuda pompaladığından duvarı kalın, çıkan kanın basıncı yüksektir; sağ karıncık yalnız akciğerlere pompalar.','sol karıncık duvarı > sağ karıncık duvarı · aort basıncı > akciğer atardamarı basıncı'),
  A('Yanlış ifadeyi seç','Dört ifade yukarıdaki bilgilerle uyumludur; aort ile akciğer atardamarı basıncını karşılaştıran ifade ise tersine kurulmuştur.','basınç ifadesi yanlış')],
 metin='Şekilde, sağlıklı bir insana ait kalp ve kalbe bağlı bazı damarlar 1, 2, 3, 4 ve 5 ile numaralandırılmıştır. Kalbin sağ ve sol yarısı birbirinden bir kas duvarla ayrılmıştır; kapakçıklar kanın yalnız tek yönde akmasını sağlar.\nBuna göre, numaralı yapılarla ilgili aşağıdakilerden hangisi yanlıştır?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Yanlış olan ifade.',ip=['Hangi yapının kanı vücuda, hangisinin akciğerlere gönderdiğini düşün.'],
 bilgi=[B('Kalp odacıkları','Sağ yarı oksijence fakir kanı akciğerlere, sol yarı oksijence zengin kanı vücuda pompalar · Kulakçıklar kanı alır, karıncıklar pompalar')],
 puf='Her numaranın hangi odacık ya da damar olduğunu belirleyip görevini ve taşıdığı kanın özelliğini sorgula.',sekil=S1)

# ======================= 02 · kolay · öncüllü · kan hücreleri =======================
d={'I':('Olgun insan alyuvarlarında çekirdek bulunmaz.',True,'olgun alyuvarlar çekirdeğini yitirir; böylece hemoglobine daha fazla yer kalır'),
   'II':('Kan pulcukları (trombositler), kanın pıhtılaşmasında görev alır.',True,'trombositler kanamada damar yaralanmasını kapatmaya ve pıhtı oluşumuna katılır'),
   'III':('Akyuvarların tamamı, vücuda giren mikroorganizmaları fagositozla yok eder.',False,'yalnız bazı akyuvarlar (nötrofil, makrofaj gibi) fagositoz yapar; lenfositler ise antikor üretir ya da enfekte hücreleri yok eder')}
r=onc(d,'D')
Q('0002','kan','kolay','öncüllü','Kanın hücresel bileşenleri','Alyuvar, akyuvar ve kan pulcuklarının yapı ve görevlerini ayırt eder.','kan hücreleri öncülleri',
 'Her kan hücresinin çekirdek durumu ve görevi ayrı ayrı bilinmelidir.','Bütün akyuvarların fagositoz yaptığını sanmak.',
 oad(d),metin=omet('Kanın hücresel bileşenleri olan alyuvarlar, akyuvarlar ve kan pulcukları kemik iliğindeki kök hücrelerden oluşur ve kanda farklı görevler üstlenir. Bu hücrelerle ilgili aşağıdaki yargılar verilmiştir.',d,'Buna göre, bu yargılardan hangileri doğrudur?'),
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',ip=['Akyuvarların çeşitli türleri olduğunu ve her türün aynı görevi yapmadığını hatırla.'],
 bilgi=[B('Kan hücreleri','Alyuvar: oksijen taşır, olgunlaşınca çekirdeğini yitirir · Akyuvar: savunma · Kan pulcuğu: pıhtılaşma')],
 puf='“Tamamı” ve “hiçbiri” gibi genellemelerde istisna olup olmadığını sorgula.')

# ======================= 03 · kolay · tablo · kan grubu =======================
KISI=[('Ali',1,0,1),('Burak',0,1,0),('Derya',1,1,0),('Ece',1,0,0),('Cem',0,0,1)]
def abo(a,b): return {(1,0):'A',(0,1):'B',(1,1):'AB',(0,0):'O'}[(a,b)]
def antikor(a,b): return {'A':{'anti-B'},'B':{'anti-A'},'AB':set(),'O':{'anti-A','anti-B'}}[abo(a,b)]
iki=[k for k,a,b,rh in KISI if antikor(a,b)=={'anti-A','anti-B'}]; assert iki==['Cem']
S3=tablo_svg(['Kişi','A antijeni','B antijeni','Rh antijeni'],[[k,'var' if a else 'yok','var' if b else 'yok','var' if rh else 'yok'] for k,a,b,rh in KISI])
Q('0003','kan','kolay','tablo','ABO kan grubu antijen ve antikorları','Alyuvardaki antijenlerden kan grubunu belirleyip plazmadaki doğal antikorları bulur.','antijen tablosu',
 'Plazma, alyuvarda bulunmayan ABO antijenine karşı doğal antikor taşır.','Alyuvarda bulunan antijenin aynı adlı antikoru plazmada bulundurduğunu sanmak.',
 [A('Kan gruplarını belirle','A antijeni olan A, B antijeni olan B, ikisi de olan AB, hiçbiri olmayan O grubudur.','Ali: A · Burak: B · Derya: AB · Ece: A · Cem: O'),
  A('Plazma antikorlarını yaz','Plazma, alyuvarında bulunmayan antijene karşı antikor taşır; A grubunda anti-B, B grubunda anti-A, AB grubunda hiçbiri, O grubunda ikisi de bulunur.','A grubu: anti-B; B grubu: anti-A; AB grubu: yok; O grubu: anti-A ve anti-B'),
  A('Kişiyi seç','Hem anti-A hem anti-B yalnız hiçbir ABO antijeni taşımayan kişide bulunur.','Cem')],
 metin='Aşağıdaki tabloda, daha önce hiç kan nakli geçirmemiş beş kişinin alyuvarlarında bulunan antijenler gösterilmiştir.\nBuna göre, bu kişilerden hangisinin kan plazmasında hem anti-A hem de anti-B antikorları bulunur?',
 dogru='Cem',sira=['Ali','Burak','Derya','Ece','Cem'],
 yan=[('Ali','Ali’nin alyuvarında A antijeni vardır; plazmasında yalnız anti-B bulunur, anti-A bulunmaz.','bilgi'),('Burak','Burak’ın alyuvarında B antijeni vardır; plazmasında yalnız anti-A bulunur, anti-B bulunmaz.','bilgi'),
      ('Derya','Derya’nın alyuvarında A ve B antijenlerinin ikisi de vardır; plazmasında bu antikorların hiçbiri bulunmaz.','bilgi'),('Ece','Ece’nin alyuvarında A antijeni vardır; Rh antijeninin olmaması plazmadaki anti-A ve anti-B durumunu değiştirmez, plazmasında yalnız anti-B bulunur.','dikkat')],
 istenen='Plazmasında anti-A ve anti-B bulunan kişi.',ip=['Antikorlar, kişinin alyuvarında bulunmayan antijenlere karşı oluşur.'],
 bilgi=[B('ABO grupları ve antikorlar','A grubu: A antijeni, plazmada anti-B · B grubu: B antijeni, plazmada anti-A · AB grubu: iki antijen, antikor yok · O grubu: antijen yok, plazmada anti-A ve anti-B')],
 puf='Antikor, alyuvarda olmayan antijene karşıdır; O grubunda ikisi birden bulunur.',sekil=S3)

# ======================= 04 · orta · grafik · öncüllü · damarlar =======================
CAT=['Aort','Atardamar','Kılcal\\\\damar','Toplardamar','Ana\\\\toplardamar']
BAS=[100,80,35,10,3]; HIZ=[80,60,5,25,50]; ALAN=[3,8,100,35,6]
assert all(BAS[i]>BAS[i+1] for i in range(4)) and HIZ.index(min(HIZ))==2 and ALAN.index(max(ALAN))==2 and HIZ[3]<HIZ[1] and HIZ[4]<HIZ[0]
def egri4(v,ex): return pl([(i*1.9,x/100*3.4) for i,x in enumerate(v)],ex)
g4=eksen(7.6,3.4,'Damar türleri','Göreli değer',xt=range(5),xs=1.9,xtl={i:'\\shortstack{%s}'%c for i,c in enumerate(CAT)},xly=-1.5)
g4=g4.replace('node[below=1pt]','node[below=1pt,font=\\normalsize]')
g4+=egri4(ALAN,'line width=1.7pt,blue!70!black')+egri4(BAS,'line width=1.7pt,red!75!black,dash pattern=on 6pt off 3pt')+egri4(HIZ,'line width=1.9pt,green!50!black,dash pattern=on 1.5pt off 3pt')
g4+='\\node[font=\\large\\bfseries,text=blue!70!black] at (4.3,3.7) {X};\\node[font=\\large\\bfseries,text=red!75!black] at (1.2,3.5) {Y};\\node[font=\\large\\bfseries,text=green!50!black] at (8.0,1.75) {Z};'
S4=tk(g4,.85)
d={'I':('X eğrisi, kan akış hızını göstermektedir.',False,'X eğrisi kılcal damarlarda en yüksek değere ulaştığından toplam kesit alanını gösterir; kan akış hızı bu bölgede en düşüktür'),
   'II':('Y eğrisi, kan basıncını göstermektedir.',True,'kan basıncı kalpten uzaklaştıkça sürekli azalır ve toplardamarlarda çok düşüktür; yalnız Y eğrisi böyle seyreder'),
   'III':('Kan akış hızı, toplardamarlarda atardamarlardakinden daha yüksektir.',False,'hız eğrisi (Z) toplardamarlarda atardamarlardakinden düşüktür; kan toplardamarlarda kılcal damarlardakinden hızlı, atardamarlardakinden yavaş akar')}
r=onc(d,'B')
Q('0004','damar','orta','grafik','Damarlarda basınç, hız ve kesit alanı','Damar türlerine göre kan basıncı, akış hızı ve toplam kesit alanı eğrilerini birbirine bağlayarak yorumlar.','X, Y, Z eğrileri',
 'Toplam kesit alanı arttıkça kan akış hızı azalır; basınç kalpten uzaklaştıkça düşer.','Hız ile toplam kesit alanı eğrilerini karıştırmak.',
 oad(d,[A('Eğrileri tanı','Kılcal damarlarda en yüksek olan eğri toplam kesit alanıdır; hız bu bölgede en düşüktür. Aortta en yüksek olup sürekli azalan eğri basınçtır.','alan, basınç, hız eğrilerinin ayrılması')]),
 metin=omet('Şekilde, kanın dolaşım sırasında geçtiği damar türlerindeki kan basıncı, kan akış hızı ve toplam kesit alanının değişimi X, Y ve Z eğrileriyle gösterilmiştir. Hangi eğrinin hangi büyüklüğe ait olduğu belirtilmemiştir.',d,'Buna göre, bu yargılardan hangileri doğrudur?'),
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',ip=['Toplam kesit alanı ile akış hızının nasıl ilişkili olduğunu düşün.'],
 bilgi=[B('Damarlarda akış','Toplam kesit alanı en geniş yer kılcal damarlardır; akış orada en yavaştır · Kan basıncı kalpten uzaklaştıkça düşer')],
 puf='Akış hızı ile toplam kesit alanı ters ilişkilidir.',sekil=S4)

# ======================= 05 · zor · grafik · kalp döngüsü =======================
TT=[0,.05,.1,.15,.2,.25,.3,.35,.4,.42,.45,.5,.6,.8]
LV=[10,12,16,48,84,100,98,86,50,30,14,4,8,10]
AO=[70,68,66,66,74,92,94,90,84,82,80,76,72,70]
LA=[16,26,16,12,13,14,16,20,24,24,22,18,18,16]
def dur(t):
    i=TT.index(t); return dict(av=LA[i]>LV[i],sl=LV[i]>AO[i],kasilma=LV[i]>=LV[i-1] and 0<i<=7)
K5={'K':.05,'L':.15,'M':.25,'N':.4,'O':.6}
D5={k:dur(t) for k,t in K5.items()}
assert D5['K']==dict(av=True,sl=False,kasilma=False) or (D5['K']['av'] and not D5['K']['sl'])
assert (D5['L']['av'],D5['L']['sl'])==(False,False) and (D5['M']['av'],D5['M']['sl'])==(False,True) and (D5['N']['av'],D5['N']['sl'])==(False,False) and (D5['O']['av'],D5['O']['sl'])==(True,False) and (D5['K']['av'],D5['K']['sl'])==(True,False)
def e5(v,ex): return pl([(t/.8*7.2,x/110*4.2) for t,x in zip(TT,v)],ex)
g5=eksen(7.2,4.2,'Zaman (s)','Basınç',xt=[0,.2,.4,.6,.8],xs=7.2/.8,xtl={0:'0',.2:'0,2',.4:'0,4',.6:'0,6',.8:'0,8'})
g5+=e5(AO,'line width=1.7pt,blue!70!black')+e5(LV,'line width=1.7pt,red!75!black,dash pattern=on 6pt off 3pt')+e5(LA,'line width=1.9pt,green!50!black,dash pattern=on 1.5pt off 3pt')
for k,t in K5.items(): g5+=f'\\draw[dash pattern=on 1pt off 2pt,line width=.6pt] ({t/.8*7.2:.2f},0)--({t/.8*7.2:.2f},4.55);\\node[font=\\large\\bfseries] at ({t/.8*7.2:.2f},4.85) {{{k}}};'
g5+='\\node[anchor=west] at (7.35,2.9) {\\normalsize Aort};\\node[anchor=west] at (7.35,.55) {\\normalsize Kulakçık};\\node[anchor=west] at (7.35,.05) {\\normalsize Karıncık};'
# eğri türü açıklaması: düz çizgi aort, kesikli sol karıncık, noktalı sol kulakçık
g5+='\\draw[line width=1.7pt,blue!70!black] (7.0,3.35)--(7.35,3.35);\\node[anchor=west] at (7.45,3.35) {\\normalsize Aort};\\draw[line width=1.7pt,red!75!black,dash pattern=on 6pt off 3pt] (7.0,2.85)--(7.35,2.85);\\node[anchor=west] at (7.45,2.85) {\\normalsize Karıncık};\\draw[line width=1.9pt,green!50!black,dash pattern=on 1.5pt off 3pt] (7.0,2.35)--(7.35,2.35);\\node[anchor=west] at (7.45,2.35) {\\normalsize Kulakçık};'
g5=g5.replace('\\node[anchor=west] at (7.35,2.9) {\\normalsize Aort};\\node[anchor=west] at (7.35,.55) {\\normalsize Kulakçık};\\node[anchor=west] at (7.35,.05) {\\normalsize Karıncık};','')
S5=tk(g5,.7)
it=[('K anında iki loblu kapakçık kapalı, aort kapakçığı açıktır.',False,'K anında sol kulakçık basıncı sol karıncık basıncından yüksektir; iki loblu kapakçık açıktır ve karıncık basıncı aort basıncından düşük olduğundan aort kapakçığı kapalıdır'),
    ('L anında sol karıncıktaki kan aorta pompalanmaktadır.',False,'L anında karıncık kasılmaya başlamıştır ama karıncık basıncı henüz aort basıncına ulaşmamıştır; iki kapakçık da kapalıdır ve kan aorta geçmez'),
    ('M anında iki loblu kapakçık açıktır.',False,'M anında karıncık basıncı kulakçık basıncından çok yüksektir; iki loblu kapakçık kapalıdır, aort kapakçığı açıktır'),
    ('L ve N anlarının her ikisinde de iki loblu kapakçık ile aort kapakçığı kapalıdır.',True,'L anında karıncık basıncı hem kulakçık hem aort basıncından, N anında ise aort basıncından düşük ve kulakçık basıncından yüksektir'),
    ('K ve O anlarının her ikisinde de sol karıncık kasılmaktadır.',False,'K ve O anlarında karıncık basıncı düşük kalmıştır; karıncık gevşemiş hâldedir ve kulakçıktan kan almaktadır')]
for k in 'LN': assert not D5[k]['av'] and not D5[k]['sl']
r,g=tek(it,True,'D',sanc_dogru)
Q('0005','dongu','zor','grafik','Kalp döngüsünde kapakçıklar','Kulakçık, karıncık ve aort basınç eğrilerini karşılaştırarak kapakçıkların açık ya da kapalı olduğu anları belirler.','basınç–zaman eğrileri',
 'Kapakçık, kanı yüksek basınçlı bölmeden düşük basınçlı bölmeye geçirir; iki bölme arasındaki basınç farkı durumu belirler.','Karıncık basıncının aort basıncından düşük olduğu anda kapakçıkların ikisini birden kapalı görmemek.',
 [A('Kuralı belirle','İki loblu kapakçık, sol kulakçık basıncı sol karıncıktan yüksekken; aort kapakçığı, sol karıncık basıncı aorttan yüksekken açılır.','kulakçık > karıncık: iki loblu açık · karıncık > aort: aort kapakçığı açık'),
  A('Beş anı oku','K’da kulakçık basıncı karıncıktan yüksektir; L’de karıncık kulakçığı geçmiş ama aorta ulaşmamıştır; M’de karıncık aortu geçmiştir; N’de karıncık basıncı düşmüş ama hâlâ kulakçıktan yüksektir; O’da kulakçık yine karıncıktan yüksektir.','K: yalnız iki loblu açık · L: ikisi kapalı · M: yalnız aort kapakçığı açık · N: ikisi kapalı · O: yalnız iki loblu açık'),
  A('İfadeleri sına','L ve N anlarının her ikisinde de iki kapakçık kapalıdır; diğer ifadeler okunan durumlarla çelişir.','L ve N: ikisi de kapalı')],
 metin='Şekilde, bir kalp döngüsü sırasında insanın sol kulakçık, sol karıncık ve aort basınçları verilmiştir. Kapakçıklar, kanı basıncı yüksek olan bölmeden basıncı düşük olan bölmeye geçirir; ters yönde akışı engelleyecek biçimde kapanır. K, L, M, N ve O harfleri döngü içinde seçilmiş beş anı göstermektedir.\nBuna göre, bu anlarla ilgili aşağıdakilerden hangisi doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan ifade.',ip=['Her anda önce kulakçık ile karıncığı, sonra karıncık ile aortu karşılaştır.'],
 bilgi=[B('Kapakçıkların çalışması','Kapakçıklar basınç farkıyla açılıp kapanır · İki loblu kapakçık kulakçık ile karıncık, aort kapakçığı karıncık ile aort arasındadır')],
 puf='Her an için iki karşılaştırma yap: kulakçık-karıncık ve karıncık-aort; sonuçlar iki kapakçığın durumunu verir.',sekil=S5)

# ======================= 06 · orta · olumsuz · kalp atış hızı =======================
it=[('Derin uykuya geçen kişide parasempatik etkinin baskın olması',False,''),
    ('Ani bir korku yaşayan kişide kana adrenalin salgılanması',True,'adrenalin kalp atış hızını artırır; korku durumunda salgısı artan hormon kalbi hızlandırır'),
    ('Kan karbon dioksit derişimi yükselen kişinin dinlenme hâlinde olması',True,'kandaki CO2 artışı kalp ve solunum merkezlerini uyararak atış hızını artırır'),
    ('Tiroksin hormonu fazla salgılanan kişinin dinlenme hâlinde olması',True,'tiroksin metabolizma hızını artırır ve kalp atış hızını yükseltir'),
    ('Sempatik sinir uçlarından kalbe noradrenalin salgılanması',True,'sempatik sinirler kalp atışını hızlandırır')]
def sanc6(m,n): return f'Bu durumda kalp atış hızının artmayacağını sanmış; oysa artış beklenir: {n}.'
r,g=tek(it,False,'A',sanc6)
Q('0006','dongu','orta','düz','Kalp atışının düzenlenmesi','Kalp atış hızını artıran ve azaltan sinirsel, hormonal ve kimyasal etkenleri ayırt eder.','durumlar, olumsuz kök',
 'Sempatik sinirler ve adrenalin hızlandırır; parasempatik sinirler (asetilkolin) yavaşlatır.','Her uyarıcı durumun kalp atışını artırdığını varsaymak.',
 [A('Düzenleme sistemini hatırla','Sinüs düğümünün kendiliğinden başlattığı ritmi sempatik sinirler, adrenalin, tiroksin ve CO2 artışı hızlandırır; parasempatik sinirler yavaşlatır.','hızlandıranlar: sempatik, adrenalin, tiroksin, CO2 · yavaşlatan: parasempatik'),
  A('Durumları tek tek değerlendir','Korku, CO2 artışı, fazla tiroksin ve noradrenalin salgısı kalbi hızlandırır; derin uykuda parasempatik etki baskındır ve atış hızı azalır.','dört durumda artış · uyku durumunda azalma'),
  A('Artış beklenmeyen durumu seç','Soru artış beklenmeyen durumu sorduğundan parasempatik etkinin baskın olduğu durum seçilir.','uyku ve parasempatik etki')],
 metin='Kalp kasının kasılma ritmini sağ kulakçıktaki sinüs düğümü başlatır; bu ritim, otonom sinir sistemi ile bazı hormon ve kimyasal maddeler tarafından değiştirilebilir. Aşağıda, sağlıklı insanlarda görülebilecek beş durum verilmiştir.\nBuna göre, bu durumlardan hangisinde kalp atış hızında artış beklenmez?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Kalp atış hızında artış beklenmeyen durum.',ip=['Hızlandırıcı ve yavaşlatıcı sinirleri ayrı ayrı hatırla.'],
 bilgi=[B('Kalp atışının düzenlenmesi','Sempatik sinirler (noradrenalin) ve adrenalin kalbi hızlandırır · Parasempatik sinirler (asetilkolin) kalbi yavaşlatır · Kandaki CO2 artışı atış hızını artırır')],
 puf='Her etkenin kalbi hızlandırıcı mı yavaşlatıcı mı olduğunu ayrı ayrı sorgula.')

# ======================= 07 · orta · sayısal · kalp debisi =======================
DAK1,HAC1,DAK2,HAC2=60,80,150,120
deb1=DAK1*HAC1; deb2=DAK2*HAC2; assert (deb1,deb2)==(4800,18000)
dogru7=Fr(deb2-deb1,1000); assert dogru7==Fr('13.2')
y7=[Fr(deb2,1000),Fr((DAK2-DAK1)*HAC1,1000),Fr((HAC2-HAC1)*DAK2,1000),Fr(deb2+deb1,1000)]; assert y7==[18,Fr('7.2'),6,Fr('22.8')]
Q('0007','dongu','orta','hikâyeli','Kalp debisi','Atım hacmi ve dakikadaki atım sayısından kalp debisini hesaplar ve değişimi bulur.','debi hesabı',
 'Kalp debisi = dakikadaki atım sayısı × atım hacmi; mL değeri litreye çevrilir.','Debiyi hesaplamak yerine yalnız atım sayısındaki ya da yalnız hacimdeki artışı kullanmak.',
 [A('Debi tanımını yaz','Kalp debisi, dakikadaki atım sayısı ile bir atımda pompalanan kan hacminin çarpımıdır.','debi = atım sayısı × atım hacmi'),
  A('Dinlenme debisini bul','Dakikada 60 atım ve her atımda 80 mL kan pompalanır.','60 × 80 = 4800 mL/dk'),
  A('Egzersiz debisini bul','Dakikada 150 atım ve her atımda 120 mL kan pompalanır.','150 × 120 = 18000 mL/dk'),
  A('Farkı litreye çevir','Egzersiz debisinden dinlenme debisi çıkarılır; 1000 mL = 1 L olduğundan sonuç litreye çevrilir.','18000 − 4800 = 13200 mL = 13,2 L')],
 metin='Bir sporcunun kalbi dinlenme hâlinde dakikada 60 kez atmakta ve her atımda sol karıncıktan aorta 80 mL kan pompalamaktadır. Aynı kişinin yoğun egzersiz sırasında dakikadaki atım sayısı 150’ye, her atımda pompalanan kan hacmi ise 120 mL’ye çıkmaktadır. Kalp debisi, kalbin bir dakikada pompaladığı kan hacmidir.\nBuna göre, egzersiz sırasında kalp debisi dinlenme hâline göre dakikada kaç litre artmıştır?',
 dogru=dogru7,yan=[(y7[0],'Egzersiz debisini (18 L) bulup dinlenme debisini çıkarmayı unutmuş; artışı değil egzersizdeki toplam debiyi vermiş.','dikkat'),
   (y7[1],'Yalnız atım sayısındaki artışı (150 − 60 = 90) dinlenmedeki atım hacmiyle (80 mL) çarpmış: 90 × 80 = 7200 mL = 7,2 L. Atım hacmindeki artışı hesaba katmamıştır.','islem'),
   (y7[2],'Yalnız atım hacmindeki artışı (120 − 80 = 40 mL) egzersizdeki atım sayısıyla çarpmış: 40 × 150 = 6000 mL = 6 L. Atım sayısındaki artışın etkisini ihmal etmiştir.','islem'),
   (y7[3],'İki debiyi toplamış (18 + 4,8 = 22,8 L); artış için çıkarma yapılması gerekir.','dikkat')],
 istenen='Kalp debisindeki artış (L/dk).',ip=['Kalp debisinin hangi iki büyüklükten oluştuğunu düşün.'],
 bilgi=[B('Kalp debisi','Debi, kalbin bir dakikada pompaladığı kan miktarıdır: atım sayısı × atım hacmi · Örnek: 70 atım/dk ve 60 mL ise 4200 mL/dk')],
 puf='Debide iki değişken birlikte değişir: iki durumun debisini ayrı ayrı bulmadan fark alma.')

# ======================= 08 · zor · grafik · öncüllü · kılcal damarda sıvı alışverişi =======================
def hid(x): return 38-22*x
OSM=25
net_ust=Fr(0)
xs=[i/1000 for i in range(1001)]
filt=sum(max(hid(x)-OSM,0) for x in xs)/1000; reab=sum(max(OSM-hid(x),0) for x in xs)/1000
assert hid(0)>OSM and hid(1)<OSM and filt>reab*1.5
g8=eksen(6.4,4.0,'Kılcal damar boyunca konum','Basınç (mmHg)',xt=[0,1],xs=6.4,xtl={0:'Atardamar ucu',1:'Toplardamar ucu'},yt=[0,20,40],ys=4.0/40,ylab_gap=1.0)
g8=g8.replace('node[below=1pt]','node[below=1pt,font=\\normalsize]').replace('at (0.00,-.05) {Atardamar ucu}','at (.45,-.05) {Atardamar ucu}').replace('at (6.40,-.05) {Toplardamar ucu}','at (5.9,-.05) {Toplardamar ucu}')
g8+=f'\\draw[line width=1.7pt,red!75!black] (0,{hid(0)/10:.2f})--(6.4,{hid(1)/10:.2f});\\draw[line width=1.7pt,blue!70!black,dashed] (0,{OSM/10:.2f})--(6.4,{OSM/10:.2f});'
g8+='\\node[anchor=west,font=\\normalsize] at (6.55,1.6) {Osmotik basınç};\\node[anchor=west,font=\\normalsize] at (6.55,2.2) {Hidrostatik basınç};'
g8=g8.replace('\\node[anchor=west,font=\\normalsize] at (6.55,1.6) {Osmotik basınç};\\node[anchor=west,font=\\normalsize] at (6.55,2.2) {Hidrostatik basınç};','')
g8+='\\draw[line width=1.7pt,red!75!black] (3.9,4.75)--(4.35,4.75);\\node[anchor=west,font=\\normalsize] at (4.45,4.75) {Hidrostatik};\\draw[line width=1.7pt,blue!70!black,dashed] (3.9,4.3)--(4.35,4.3);\\node[anchor=west,font=\\normalsize] at (4.45,4.3) {Osmotik};'
S8=tk(g8,.8)
d={'I':('Atardamar ucunda sıvı, osmotik basıncın hidrostatik basınçtan büyük olması nedeniyle damar dışına çıkar.',False,'atardamar ucunda hidrostatik basınç osmotik basınçtan büyüktür; bu fark sıvıyı doku sıvısına doğru iter, osmotik basınç sıvıyı damar içinde tutmaya çalışır'),
   'II':('Toplardamar ucunda osmotik basınç hidrostatik basınçtan büyük olduğundan doku sıvısındaki sıvının bir bölümü kana geri döner.',True,'toplardamar ucunda hidrostatik basınç osmotik basıncın altına düşer ve net basınç damar içine doğru olur'),
   'III':('Kılcal damardan doku sıvısına geçen sıvı miktarı, doku sıvısından kana geri dönen sıvı miktarından fazladır.',True,'atardamar ucunda damar dışına itme farkı toplardamar ucunda içeri çekme farkından hem büyük hem daha geniş bir bölgede sürer; grafikteki iki fark alanı karşılaştırıldığında dışarı çıkan sıvı fazladır')}
r=onc(d,'E')
Q('0008','damar','zor','grafik','Kılcal damarlarda sıvı alışverişi','Hidrostatik ve osmotik basınç eğrilerini karşılaştırarak kılcal damarda sıvı geçişinin yönünü ve lenf sisteminin işlevini yorumlar.','hidrostatik–osmotik basınç eğrileri',
 'Net basınç farkı sıvının yönünü belirler; damar dışına çıkan sıvı geri dönen sıvıdan fazla olduğundan fazlalığı lenf toplar.','Osmotik basıncın sıvıyı damar dışına çıkardığını sanmak.',
 oad(d,[A('Eğrileri oku','Hidrostatik basınç atardamar ucundan toplardamar ucuna doğru azalır; osmotik basınç sabit kalır. Eğriler bir noktada kesişir.','hidrostatik: azalır · osmotik: sabit')]),
 metin=omet('Şekilde, sağlıklı bir insanda bir kılcal damar boyunca kanın hidrostatik basıncı (kan basıncı) ile plazma proteinlerinin oluşturduğu osmotik basıncın değişimi gösterilmiştir. Sıvı, net basıncın yönüne doğru hareket eder; hidrostatik basınç sıvıyı damardan dışarı iter, osmotik basınç ise sıvıyı damar içinde tutmaya çalışır.',d,'Buna göre, bu yargılardan hangileri doğrudur?'),
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',ip=['Eğriler arasındaki farkın hangi uçta hangi yöne doğru olduğuna ve iki bölgedeki farkın büyüklüğüne bak.'],
 bilgi=[B('Kılcal damar alışverişi','Hidrostatik basınç sıvıyı damardan dışarı, plazma proteinlerinin osmotik basıncı damar içine çeker · Geri dönemeyen sıvı lenf kılcallarına geçer')],
 puf='Net basınç farkının yönü sıvının yönünü, fark alanlarının büyüklüğü sıvı miktarını belirler.',sekil=S8)

# ======================= 09 · orta · öncüllü · lenf =======================
d={'I':('Lenf sıvısı alyuvar içerir ve oksijen taşınmasında görev alır.',False,'lenf sıvısında alyuvar bulunmaz; oksijen taşımaz'),
   'II':('Lenf damarlarında kapakçıklar bulunur ve lenfin ilerlemesinde iskelet kaslarının kasılması etkilidir.',True,'lenf damarlarında kalp gibi bir pompa yoktur; kapakçıklar geri akışı önler, kas kasılmaları lenfi ilerletir'),
   'III':('Lenf düğümlerinde lenfositler çoğalır ve mikroplar fagositozla yok edilir.',True,'lenf düğümleri savunma işlevi görür; lenfositler burada çoğalır ve fagositler mikropları temizler')}
r=onc(d,'D')
Q('0009','lenf','orta','öncüllü','Lenf sistemi','Lenfin bileşimini, hareketini ve lenf düğümlerinin savunmadaki görevini kavrar.','lenf öncülleri',
 'Lenf sistemi kapalı bir dolaşım yapmaz; doku sıvısını toplayıp kana taşır ve savunmada rol oynar.','Lenfi kan gibi alyuvar taşıyan bir sıvı sanmak.',
 oad(d),metin=omet('İnsanda lenf sistemi; lenf kılcalları, lenf damarları ve lenf düğümlerinden oluşur. Bu sistemle ve lenf sıvısıyla ilgili aşağıdaki yargılar verilmiştir.',d,'Buna göre, bu yargılardan hangileri doğrudur?'),
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',ip=['Lenf sıvısının kanın hangi bileşenlerini içerdiğini ve lenfi hareket ettiren etkenleri düşün.'],
 bilgi=[B('Lenf sistemi','Doku sıvısının fazlasını toplayıp kana taşır · Lenf düğümlerinde lenfositler bulunur · Lenf damarlarında kapakçık vardır')],
 puf='Lenfin bileşimini ve hareket mekanizmasını kan dolaşımıyla karşılaştırarak sorgula.')

# ======================= 10 · orta · tablo · kan grubu ve kan nakli =======================
KG=[('Ayşe',1,0,1),('Berk',0,1,0),('Can',1,1,0),('Deniz',0,0,1),('Elif',0,0,0)]
def verebilir(v,a):
    _,av,bv,rv=[x for x in KG if x[0]==v][0]; _,aa,ba,ra=[x for x in KG if x[0]==a][0]
    return av<=aa and bv<=ba and rv<=ra
assert [verebilir('Elif',x[0]) for x in KG]==[True]*5 and not verebilir('Berk','Ayşe') and not verebilir('Can','Berk') and not verebilir('Deniz','Elif') and not verebilir('Ayşe','Deniz')
S10=tablo_svg(['Kişi','Anti-A serum','Anti-B serum','Anti-Rh serum'],[[k,'+' if a else '−','+' if b else '−','+' if rh else '−'] for k,a,b,rh in KG])
it=[('Berk, Ayşe’ye kan verebilir.',False,'Berk B grubu olduğundan alyuvarında B antijeni vardır; Ayşe A grubudur ve plazmasındaki anti-B antikorları Berk’in alyuvarlarını kümeleştirir'),
    ('Elif, tablodaki her kişiye kan verebilir.',True,'Elif O grubu ve Rh negatiftir; alyuvarında ABO ve Rh antijeni yoktur, bu yüzden alıcıların antikorlarıyla tepkime vermez'),
    ('Can, Berk’e kan verebilir.',False,'Can AB grubu olduğundan alyuvarında A antijeni de vardır; Berk’in plazmasındaki anti-A antikorları Can’ın alyuvarlarını kümeleştirir'),
    ('Deniz, Elif’e kan verebilir.',False,'Deniz Rh pozitiftir; Rh negatif olan Elif Rh antijenine karşı antikor oluşturabileceğinden Rh pozitif kan alması sakıncalıdır'),
    ('Ayşe, Deniz’e kan verebilir.',False,'Ayşe A grubudur; Deniz O grubu olduğundan plazmasında anti-A antikoru vardır ve Ayşe’nin alyuvarlarını kümeleştirir')]
r,g=tek(it,True,'B',sanc_dogru)
Q('0010','kan','orta','tablo','Kan grubu belirleme ve kan nakli','Serumlarla yapılan kümeleşme sonuçlarından kan grubunu bulup kan nakli uygunluğunu değerlendirir.','kümeleşme tablosu',
 'Kümeleşme olan serumun karşıtı antijen alyuvarda vardır; verici alyuvarındaki antijen alıcıda karşılık bulmamalıdır.','Antijenle antikoru karıştırmak; Rh uyumunu hesaba katmamak.',
 [A('Tabloyu oku','Anti-A ile kümeleşme A antijenini, anti-B ile kümeleşme B antijenini, anti-Rh ile kümeleşme Rh antijenini gösterir.','Ayşe A Rh+ · Berk B Rh− · Can AB Rh− · Deniz O Rh+ · Elif O Rh−'),
  A('Uygunluk kuralını uygula','Vericideki antijenler alıcının alyuvarında da bulunmalı; ayrıca Rh pozitif alyuvar Rh negatif alıcıya verilmemelidir.','verici antijenleri ⊆ alıcı antijenleri'),
  A('İfadeleri sına','Yalnız hiçbir antijeni taşımayan kişi, diğer herkese ABO ve Rh bakımından uygundur; diğer ifadelerde alıcının plazma antikorları ya da Rh uyumsuzluğu engel olur.','O Rh− olan kişi herkese verebilir')],
 metin='Aşağıdaki tabloda, beş kişinin kan örneklerine anti-A, anti-B ve anti-Rh serumları damlatıldığında alyuvarlarda kümeleşmenin görülüp görülmediği verilmiştir. (+) işareti kümeleşme olduğunu, (−) işareti kümeleşme olmadığını göstermektedir.\nBuna göre, bu kişilerin kan nakli yönünden aşağıdakilerden hangisi doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan ifade.',ip=['Önce her kişinin ABO ve Rh grubunu yaz, sonra vericideki antijenin alıcıda engel çıkarıp çıkarmadığına bak.'],
 bilgi=[B('Kan nakli uyumu','Alıcının plazmasındaki antikorlar vericinin alyuvarındaki antijeni tanırsa alyuvarlar kümeleşir · Rh negatif kişinin Rh pozitif kan alması sakıncalıdır')],
 puf='Kan nakli sorularında verici alyuvarının antijenlerini, alıcı plazmasının antikorlarıyla karşılaştır.',sekil=S10)

# ======================= 11 · zor · soy ağacı · kan grubu + Rh =======================
# Bireyler: (kuşak, no, cinsiyet, ABO fenotipi, Rh fenotipi)
def ciz_birey(x,y,cins,no,etk):
    sek=f'\\draw[line width=1.2pt] ({x-.4},{y-.4}) rectangle ({x+.4},{y+.4});' if cins=='E' else f'\\draw[line width=1.2pt] ({x},{y}) circle (.45);'
    return sek+f'\\node[font=\\normalsize\\bfseries] at ({x},{y}) {{{no}}};\\node[font=\\normalsize] at ({x},{y-.95}) {{{etk.replace("−","$-$")}}};'
# I: 1 (E, A, Rh+) × 2 (K, B, Rh+) → II: 1 (K, O, Rh−), 2 (E, AB, Rh+); II-2 × II-4 (K, O, Rh−) → III: ?
b11=ciz_birey(-1.2,4.2,'E',1,'A, Rh+')+ciz_birey(1.2,4.2,'K',2,'B, Rh+')+'\\draw[line width=1.2pt] (-.8,4.2)--(.75,4.2);'
b11+='\\draw[line width=1.2pt] (0,4.2)--(0,2.5);\\draw[line width=1.2pt] (-2.2,2.5)--(1.4,2.5);\\draw[line width=1.2pt] (-2.2,2.5)--(-2.2,2.05);\\draw[line width=1.2pt] (1.4,2.5)--(1.4,2.05);'
b11+=ciz_birey(-2.2,1.6,'K',1,'O, Rh−')+ciz_birey(1.4,1.6,'E',2,'AB, Rh+')+ciz_birey(3.8,1.6,'K',4,'O, Rh−')+'\\draw[line width=1.2pt] (1.8,1.6)--(3.35,1.6);'
b11+='\\draw[line width=1.2pt] (2.6,1.6)--(2.6,-.55);\\draw[line width=1.2pt] (2.6,-.55) -- (2.95,-.9) -- (2.6,-1.25) -- (2.25,-.9) -- cycle;\\node[font=\\normalsize\\bfseries] at (2.6,-.9) {?};'
b11+='\\node[font=\\large\\bfseries] at (-3.6,4.2) {I};\\node[font=\\large\\bfseries] at (-3.6,1.6) {II};\\node[font=\\large\\bfseries] at (-3.6,-.9) {III};'
b11+='\\draw[line width=1pt] (-3.7,-2.3) rectangle (-3.3,-1.9);\\node[anchor=west,font=\\normalsize] at (-3.2,-2.1) {erkek};\\draw[line width=1pt] (-1.5,-2.1) circle (.2);\\node[anchor=west,font=\\normalsize] at (-1.2,-2.1) {kadın};'
S11=tk(b11,.8)
# olasılık: ABO (IA IB × ii) ve Rh (anne-baba I-1, I-2 Dd × Dd; II-1 dd kanıtı → I-1, I-2 Dd; II-2 Rh+ → DD 1/3, Dd 2/3; II-4 dd)
rhd=[('DD',Fr(1,4)),('Dd',Fr(1,2)),('dd',Fr(1,4))]
pDd=Fr(1,2)/(Fr(1,4)+Fr(1,2)); pDD=1-pDd; assert (pDD,pDd)==(Fr(1,3),Fr(2,3))
pRhNeg=pDd*Fr(1,2); pB=Fr(1,2)
dog11=pB*pRhNeg; assert dog11==Fr(1,6)
HAR={Fr(1,12):'II-2’nin Rh genotipinin Dd olma olasılığını 2/3 almış, fakat bu bireyle Rh negatif eşinden dd çocuk olasılığını Dd × Dd çaprazındaki 1/4 değeriyle hesaplamıştır: 1/2 × 2/3 × 1/4 = 1/12.',
     Fr(1,8):'Rh negatif çocuk olasılığını Dd × Dd çaprazından 1/4 almış, B grubu olasılığını 1/2 almıştır: 1/2 × 1/4 = 1/8.',
     Fr(1,4):'II-2’yi kesin Dd kabul etmiş, Rh negatif çocuk olasılığını 1/2 almıştır: 1/2 × 1/2 = 1/4.',
     Fr(1,3):'Yalnızca Rh negatif olma olasılığını (1/3) hesaplamış, B grubu olma olasılığını (1/2) hesaba katmamıştır.'}
assert Fr(1,2)*Fr(2,3)*Fr(1,4)==Fr(1,12) and Fr(1,2)*Fr(1,4)==Fr(1,8) and Fr(1,2)*Fr(1,2)==Fr(1,4)
s11=['1/12','1/8','1/6','1/4','1/3']
Q('0011','kan','zor','şekilli','Kan grubu ve Rh kalıtımı','Soy ağacından ebeveyn genotiplerini çıkarıp ABO ve Rh özelliklerini birlikte hesaplayarak çocuğun fenotip olasılığını bulur.','soy ağacı, iki özellik',
 'Rh negatif çocuğu olan Rh pozitif ebeveynler Dd’dir; Rh pozitif bireyin genotip olasılığı koşullu hesaplanır, ABO ve Rh bağımsız çarpılır.','Rh pozitif bireyin kesin Dd olduğunu varsaymak ya da Rh olasılığını Dd × Dd çaprazından almak.',
 [A('Ebeveyn genotiplerini bul','I-1 ile I-2 Rh pozitif olduğu hâlde Rh negatif bir kızları vardır; bu yüzden ikisi de Dd’dir. AB grubundaki II-2 IAIB, O grubundaki II-4 ii’dir.','I-1 ve I-2: Dd · II-2: IAIB · II-4: ii, dd'),
  A('II-2’nin Rh genotipini hesapla','Dd × Dd çaprazında Rh pozitif bireyler DD (1/4) ve Dd (2/4) olur; Rh pozitif olduğu bilindiğinden olasılıklar yeniden oranlanır.','DD: 1/3 · Dd: 2/3'),
  A('Rh negatif çocuk olasılığı','Çocuk ancak II-2 Dd ise ve ondan d aleli alırsa Rh negatif olur; II-4 yalnız d verir.','2/3 × 1/2 = 1/3'),
  A('B grubu olasılığı ve sonuç','IAIB × ii çaprazında çocuklar 1/2 IAi (A) ve 1/2 IBi (B) olur; iki özellik bağımsızdır.','1/2 × 1/3 = 1/6')],
 metin='Soy ağacında, bir ailenin bazı bireylerinin ABO kan grupları ve Rh özellikleri gösterilmiştir. ABO kan grupları IA, IB ve i alelleriyle belirlenir (IA ve IB eş baskın, ikisi de i’ye baskındır). Rh pozitiflik (D) Rh negatifliğe (d) baskındır; iki özelliğin genleri farklı kromozomlardadır.\nII. kuşaktaki 2 numaralı birey ile 4 numaralı bireyin evliliğinden doğacak ilk çocuğun kan grubunun B ve Rh negatif olma olasılığı kaçtır?',
 dogru='1/6',sira=s11,yan=[(v,HAR[Fr(*map(int,v.split('/')))],'islem' if v in('1/12','1/8','1/4') else 'dikkat') for v in s11 if v!='1/6'],
 istenen='Çocuğun B grubu ve Rh negatif olma olasılığı.',ip=['Önce II. kuşaktaki Rh negatif bireyden yararlanarak I. kuşağın Rh genotiplerini belirle.'],
 bilgi=[B('Koşullu genotip olasılığı','Baskın fenotipli bireyin genotipi, ebeveyn çaprazından bulunan baskın genotipler yeniden oranlanarak bulunur · Örnek: Aa × Aa çaprazında baskın görünümlü bireyin 1/3’ü AA, 2/3’ü Aa’dır'),B('ABO kan grubu kalıtımı','IA ve IB alelleri birbirine eş baskındır, ikisi de i alelline baskındır; fenotip bu alellerin ilişkisiyle belirlenir')],
 puf='Baskın fenotipli bireyin genotipini sorarken önce ebeveyn çaprazından olasılıkları bul, sonra yalnız baskın fenotipli bireyler arasında yeniden oranla.',sekil=S11)

# ======================= 12 · orta · olumsuz · Rh uyuşmazlığı =======================
it=[('Anne ilk doğumda Rh pozitif bebeğin alyuvarlarıyla karşılaşırsa annede anti-Rh antikorları oluşabilir.',True,'doğum sırasında bebeğin Rh antijenli alyuvarları anne kanına geçebilir ve annenin bağışıklık sistemi antikor üretmeye başlar'),
    ('Annede oluşan anti-Rh antikorları, sonraki hamilelikte Rh pozitif bebeğin alyuvarlarını yıkabilir.',True,'anti-Rh antikorları plasentadan geçerek Rh pozitif bebeğin alyuvarlarını parçalar'),
    ('Çiftin sonraki çocuğu Rh negatif ise annedeki antikorlar bu bebeğin alyuvarlarını yıkmaz.',True,'Rh negatif bebeğin alyuvarında Rh antijeni bulunmadığından anti-Rh antikorları ona karşı etkisizdir'),
    ('Rh uyuşmazlığı yalnızca bebeğin Rh pozitif, annenin Rh negatif olduğu gebeliklerde sorun oluşturabilir.',True,'sorun, Rh negatif annede Rh pozitif bebeğe karşı antikor oluşmasından kaynaklanır'),
    ('Annede anti-Rh antikorları, ilk bebeğin alyuvarlarını doğumdan önce yıkarak ilk gebelikte de ciddi alyuvar yıkımı oluşturur.',False,'')]
def sanc12(m,n): return f'Bu ifadenin söylenemeyeceğini sanmış; oysa söylenebilir: {n}.'
r,g=tek(it,False,'D',sanc12)
Q('0012','kan','orta','düz','Rh uyuşmazlığı','Rh negatif annenin Rh pozitif bebeğe karşı antikor oluşturma sürecini ve bunun gebeliklerdeki sonuçlarını açıklar.','Rh gebelik senaryosu, olumsuz kök',
 'Antikorlar ilk doğum sırasında oluşmaya başlar; sorun sonraki Rh pozitif gebeliklerde görülür.','İlk bebekte de alyuvar yıkımı olduğunu sanmak.',
 [A('Süreci sırala','Rh negatif anne ilk Rh pozitif bebeğini doğurduğunda bebeğin alyuvarları anne kanına geçer ve anti-Rh antikoru üretimi başlar.','antikor oluşumu doğum sırasında başlar'),
  A('Sonraki gebelikleri değerlendir','Sonraki bebek Rh pozitifse antikorlar plasentadan geçip bebeğin alyuvarlarını parçalar; Rh negatif bebekte tepkime olmaz.','sorun: sonraki Rh pozitif bebek'),
  A('İlk bebeği değerlendir','İlk gebelikte antikor henüz oluşmadığından ilk bebekte alyuvar yıkımı beklenmez.','ilk bebek: sorun yok'),
  A('Söylenemeyeni seç','İlk bebekte doğumdan önce ciddi alyuvar yıkımı olduğunu söyleyen ifade süreçle çelişir.','çelişen ifade seçilir')],
 metin='Rh negatif bir kadın ile Rh pozitif bir erkeğin ilk çocukları Rh pozitif olarak doğmuştur. Anne, bu doğum sonrasında Rh uyuşmazlığına yönelik herhangi bir önlem almamıştır. Çift ikinci kez çocuk sahibi olmak istemektedir.\nBuna göre, bu çiftteki Rh uyuşmazlığıyla ilgili aşağıdakilerden hangisi söylenemez?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Söylenemeyecek olan ifade.',ip=['Annede antikor oluşumunun ne zaman başladığını ve antikorların hangi bebeği etkileyebileceğini düşün.'],
 bilgi=[B('Rh uyuşmazlığı','Rh antijeni taşımayan anne, Rh pozitif bebeğin alyuvarlarına karşı antikor üretebilir · Antikorlar sonraki Rh pozitif bebeklerin alyuvarlarına zarar verir')],
 puf='Antikorun ne zaman oluştuğunu ve kimi etkileyebildiğini ayrı ayrı sorgula.')

# ======================= 13 · orta · tablo · deney · bağışıklık türleri =======================
S13=tablo_svg(['Grup','0. gün','14. gün','28. gün'],[['1','Tuzlu su','Canlı X','Hastalandı'],['2','Öldürülmüş X','Canlı X','Sağlıklı'],['3','—','Canlı X + X’e karşı serum','Sağlıklı']])
it=[('1. gruptaki fareler X’e karşı korunmuştur.',False,'tabloya göre 1. gruptaki fareler 28. günde hastalanmıştır; korunmamışlardır'),
    ('2. gruptaki fareler, ilk uygulamayla dışarıdan hazır antikor almıştır.',False,'öldürülmüş X bir antijen kaynağıdır (aşı gibidir); fareler antikorları kendi bağışıklık sistemleriyle üretir'),
    ('3. gruptaki fareler, canlı X’e karşı korumayı kendi ürettikleri antikorlarla sağlamıştır.',False,'serum, hazır antikor içerir; 3. gruptaki fareler korumayı dışarıdan aldıkları antikorlarla sağlamıştır'),
    ('3. gruptaki fareler, canlı X ile ikinci kez karşılaştıklarında hızlı bir ikinci yanıt vermiştir.',False,'3. gruptaki fareler X’e karşı bellek hücresi oluşturmadığından hızlı ikinci yanıt oluşmaz'),
    ('2. gruptaki farelerin korunması bağışıklık belleğine, 3. gruptaki farelerin korunması ise dışarıdan alınan hazır antikorlara dayanır.',True,'öldürülmüş X ile bellek hücreleri oluşur (aşıya benzer, aktif bağışıklık); serumla alınan antikorlar geçici koruma sağlar (pasif bağışıklık)')]
r,g=tek(it,True,'E',sanc_dogru)
Q('0013','bag','orta','tablo','Aktif ve pasif bağışıklık','Aşı ve serum uygulamasının doğurduğu bağışıklık türlerini deney sonuçlarından ayırt eder.','fare deneyi tablosu',
 'Antijen verilmesi aktif (bellekli), hazır antikor verilmesi pasif (belleksiz, geçici) bağışıklık sağlar.','Serumu aşı gibi düşünüp bellek oluştuğunu varsaymak.',
 [A('Grupları tanı','1. grup kontroldür; 2. gruba öldürülmüş X (antijen), 3. gruba X ile birlikte hazır antikor içeren serum uygulanmıştır.','1: kontrol · 2: antijen uygulaması · 3: serum uygulaması'),
  A('Bağışıklık türünü belirle','Antijen uygulaması bağışıklık sisteminin antikor ve bellek hücresi üretmesini sağlar; serum ise hazır antikor sağlar ve bellek oluşturmaz.','2: aktif bağışıklık, bellek var · 3: pasif bağışıklık, bellek yok'),
  A('İfadeleri sına','Doğru ifade, 2. grubun korunmasını bağışıklık belleğine, 3. grubun korunmasını dışarıdan alınan antikorlara bağlar.','2: bellek · 3: hazır antikor')],
 metin='Bir araştırmacı, X mikrobuna karşı bağışıklık türlerini incelemek için üç grup fare ile deney yapmıştır. Gruplara uygulananlar ve 28. gün sonunda farelerin durumu tabloda gösterilmiştir. Serum, X’e karşı hazır antikor içermektedir; her gruptaki fare sayısı ve koşullar eşittir.\nBuna göre, bu deneyle ilgili aşağıdakilerden hangisi doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan ifade.',ip=['Her uygulamada vücudun antikoru kendisinin mi ürettiğini, yoksa hazır mı aldığını ayırt et.'],
 bilgi=[B('Aktif ve pasif bağışıklık','Aktif bağışıklık: vücut antijene karşı kendi antikorunu ve bellek hücrelerini üretir (hastalığı geçirme, aşı) · Pasif bağışıklık: hazır antikor alınır, koruma geçicidir (serum, anne sütü)')],
 puf='Antikoru kim üretiyor? Vücut kendisi üretiyorsa aktif ve bellekli, hazır alıyorsa pasif ve geçici.',sekil=S13)

# ======================= 14 · orta · grafik · öncüllü · birincil/ikincil yanıt =======================
AX=[(0,0),(4,0),(8,10),(13,20),(20,14),(28,9),(30,45),(33,90),(37,100),(45,85),(56,70)]
AY=[(0,0),(28,0),(32,0),(37,10),(42,20),(49,14),(56,9)]
def zirve(v,a,b): return max(y for x,y in v if a<=x<=b)
def esik(v,a,e):  # a'dan sonra e değerine ulaşılan ilk gün (doğrusal)
    for (x1,y1),(x2,y2) in zip(v,v[1:]):
        if x2>=a and y2>=e and y1<e: return x1+(e-y1)*(x2-x1)/(y2-y1)
assert zirve(AX,28,56)>4*zirve(AX,0,27) and zirve(AY,28,56)==zirve(AX,0,27) and esik(AX,28,10)-28<esik(AX,0,10) and esik(AY,28,10)-28>esik(AX,28,10)-28
def e14(v,ex): return pl([(x/56*6.8,y/110*3.6) for x,y in v],ex)
g14=eksen(6.8,3.6,'Zaman (gün)','Antikor derişimi',xt=[0,14,28,42,56],xs=6.8/56,yt=[0,50,100],ys=3.6/110,ylab_gap=1.0)
g14+=e14(AX,'line width=1.7pt,blue!70!black')+e14(AY,'line width=1.8pt,red!75!black,dash pattern=on 6pt off 3pt')
g14+=f'\\draw[{ARR},line width=.9pt] (0,4.55)--(0,4.0);\\node[font=\\normalsize] at (0,4.85) {{X}};\\draw[{ARR},line width=.9pt] ({28/56*6.8:.2f},4.55)--({28/56*6.8:.2f},4.0);\\node[font=\\normalsize] at ({28/56*6.8:.2f},4.85) {{X ve Y}};'
g14+='\\draw[line width=1.7pt,blue!70!black] (.9,3.25)--(1.3,3.25);\\node[anchor=west,font=\\normalsize] at (1.4,3.25) {X’e karşı};\\draw[line width=1.8pt,red!75!black,dash pattern=on 6pt off 3pt] (.9,2.75)--(1.3,2.75);\\node[anchor=west,font=\\normalsize] at (1.4,2.75) {Y’ye karşı};'
S14=tk(g14,.8)
d={'I':('28. günden sonra Y’ye karşı oluşan antikorlar, X için oluşan bellek hücrelerinden üretilmiştir.',False,'Y’ye karşı yanıt X’e karşı oluşan belleğe bağlı değildir; Y ile ilk kez karşılaşıldığından birincil yanıt gibi geç ve düşüktür'),
   'II':('0–28. günler arasında X’e karşı antikor derişiminin azalması, X’e özgü bellek hücrelerinin de yok olduğunu gösterir.',False,'antikor derişimi azalsa da bellek hücreleri kalır; ikinci temasta X’e karşı yanıtın hızlı ve güçlü olması bunu gösterir'),
   'III':('X’e karşı ikinci yanıtın birincil yanıttan daha hızlı ve güçlü olması, ilk temasta oluşan bellek hücrelerinden kaynaklanır.',True,'ilk temasta oluşan bellek hücreleri ikinci temasta hızla çoğalıp antikor üreten hücrelere dönüşür')}
r=onc(d,'C')
Q('0014','bag','orta','grafik','Birincil ve ikincil bağışıklık yanıtı','Antikor derişimi–zaman grafiğinden birincil ve ikincil yanıtı karşılaştırıp bellek hücrelerinin rolünü yorumlar.','antikor–zaman grafiği',
 'İkinci temasta bellek hücreleri sayesinde yanıt daha hızlı, daha güçlü ve daha uzun sürelidir; ilk kez karşılaşılan antijene karşı yanıt birincil yanıttır.','Antikor derişiminin azalmasını belleğin kaybolması sanmak.',
 oad(d,[A('Grafiği oku','X’e ilk kez 0. günde, ikinci kez 28. günde maruz kalınmıştır; Y ile ilk karşılaşma 28. gündedir. X’e karşı ikinci yanıt daha hızlı ve çok daha yüksektir; Y’ye karşı yanıt ilk X yanıtına benzer.','X: ikinci yanıt hızlı ve yüksek · Y: birincil yanıt')]),
 metin=omet('Bir kişiye 0. günde X antijeni, 28. günde ise X ve Y antijenleri birlikte verilmiştir. Kişide X ve Y antijenlerine karşı oluşan antikorların derişimi 56 gün boyunca ölçülmüş ve şekilde gösterilmiştir.',d,'Buna göre, bu yargılardan hangileri doğrudur?'),
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',ip=['28. günden sonra hangi antijenle ilk kez, hangisiyle ikinci kez karşılaşıldığına göre iki yanıtı karşılaştır.'],
 bilgi=[B('Bağışıklık belleği','Antijenle ilk karşılaşmada B ve T lenfositlerinden bellek hücreleri oluşur · Aynı antijenle ikinci karşılaşmada yanıt daha hızlı ve güçlüdür')],
 puf='İkinci yanıtı güçlü ve hızlı yapan bellek hücreleridir; antikor derişiminin düşmesi belleğin yok olduğu anlamına gelmez.',sekil=S14)

# ======================= 15 · zor · grafik · aşı ve serum =======================
K1=[(0,0),(1,80),(10,45),(20,22),(30,10),(40,4),(50,2),(56,3),(60,6),(66,12),(72,16),(80,14)]      # hazır antikor (serum)
K2=[(0,0),(6,2),(12,10),(20,28),(26,30),(35,22),(45,18),(50,17),(51,40),(53,90),(57,100),(65,80),(80,55)]  # aşı
def deg(v,t):
    for (x1,y1),(x2,y2) in zip(v,v[1:]):
        if x1<=t<=x2: return y1+(y2-y1)*(t-x1)/(x2-x1)
assert deg(K1,1)>deg(K2,1)*10 and all(deg(K1,t)>deg(K1,t+10) for t in (1,10,20,30)) and max(y for x,y in K2 if x>=50)>5*max(y for x,y in K1 if x>=50)
assert deg(K2,53)>deg(K1,53)*20 and deg(K2,26)==30 and deg(K2,50)>deg(K1,50)*5
def e15(v,ex): return pl([(x/80*6.8,y/110*3.6) for x,y in v],ex)
g15=eksen(6.8,3.6,'Zaman (gün)','Antikor derişimi',xt=[0,20,40,60,80],xs=6.8/80,yt=[0,50,100],ys=3.6/110,ylab_gap=1.0)
g15+=e15(K1,'line width=1.8pt,red!75!black,dash pattern=on 6pt off 3pt')+e15(K2,'line width=1.7pt,blue!70!black')
g15+=f'\\draw[{ARR},line width=.9pt] (0,4.55)--(0,4.0);\\node[font=\\normalsize,anchor=south] at (0,4.55) {{uygulama}};\\draw[{ARR},line width=.9pt] ({50/80*6.8:.2f},4.55)--({50/80*6.8:.2f},4.0);\\node[font=\\normalsize,anchor=south] at ({50/80*6.8:.2f},4.55) {{mikrop}};'
g15+='\\draw[line width=1.8pt,red!75!black,dash pattern=on 6pt off 3pt] (2.3,3.25)--(2.7,3.25);\\node[anchor=west,font=\\normalsize] at (2.8,3.25) {Kişi 1};\\draw[line width=1.7pt,blue!70!black] (2.3,2.75)--(2.7,2.75);\\node[anchor=west,font=\\normalsize] at (2.8,2.75) {Kişi 2};'
S15=tk(g15,.8)
def sanc15(m,n): return f'Bu ifadeyi doğru sanmış; oysa yanlıştır: {n}.'
it=[('Kişi 1’e aşı, Kişi 2’ye serum uygulanmıştır.',False,'Kişi 1’de antikor derişimi uygulamadan hemen sonra yüksektir ve zamanla azalır; bu hazır antikor (serum) uygulamasının, Kişi 2’deki yavaş artış ise aşının sonucudur'),
    ('Kişi 2’de 50. günden sonra ulaşılan en yüksek derişim, aşıdan sonraki ilk zirveden daha yüksektir ve bu bellek hücrelerinden kaynaklanır; Kişi 1’deki antikorları ise kişinin kendi bağışıklık sistemi üretmemiştir.',True,'aşı bellek hücreleri oluşturur ve ikinci karşılaşmada hızlı yanıt sağlar; serumdaki antikorlar hazır verilmiştir ve bellek oluşturmaz'),
    ('Kişi 1’de 1–40. günlerde görülen antikor azalması, antikorların bellek hücrelerine dönüşmesinin sonucudur.',False,'antikorlar bellek hücresine dönüşmez; hazır verilen antikorlar zamanla yıkılır ve derişimleri azalır'),
    ('Kişi 2’ye uygulanan işlem, uygulamadan hemen sonra Kişi 1’dekinden daha hızlı koruma sağlar.',False,'uygulamadan hemen sonra antikor derişimi Kişi 1’de çok yüksek, Kişi 2’de çok düşüktür; hazır antikor anında koruma sağlar, aşının etkisi ise gecikmelidir'),
    ('Kişi 1’in 50. günden sonraki yanıtının yavaş olması, bu kişide bağışıklık belleğinin oluşmuş olmasından kaynaklanır.',False,'bellek oluşmuş olsaydı yanıt hızlı olurdu; Kişi 1’de bellek hücresi oluşmadığı için yanıt birincil yanıt gibi yavaş ve düşüktür')]
r,g=tek(it,True,'B',sanc15)
Q('0015','bag','zor','grafik','Aşı ve serum','Antikor derişimi–zaman grafiğinden hangi kişiye aşı, hangisine serum uygulandığını çıkarıp bellek hücreleri ve ikinci yanıtla ilişkilendirir.','aşı–serum antikor grafiği',
 'Serum hazır antikor verir: etki hızlı, kısa ve belleksizdir; aşı antijen verir: etki geç, kalıcı ve bellekli, ikinci karşılaşmada hızlı ve güçlü yanıtla sonuçlanır.','Serum ve aşıyı birbiriyle karıştırmak; serumun da bellek oluşturduğunu sanmak.',
 [A('Uygulamaları tanı','Kişi 1’de antikor derişimi uygulamadan hemen sonra yüksektir ve azalır: hazır antikor (serum). Kişi 2’de derişim yavaş artar ve uzun süre kalır: aşı.','Kişi 1: serum · Kişi 2: aşı'),
  A('İlk 40 günü yorumla','Serumdaki antikorlar kişinin kendi hücrelerince üretilmediğinden yıkılır ve derişim düşer; aşıda ise kişinin bağışıklık sistemi antikor ve bellek hücresi üretir.','serum: geçici · aşı: kalıcı'),
  A('50. günden sonrasını yorumla','Aşıyla bellek hücreleri oluştuğundan Kişi 2 mikropla karşılaşınca hızlı ve güçlü yanıt verir; serum alan Kişi 1’de bellek oluşmadığı için yanıt yavaş ve zayıftır.','Kişi 2: hızlı ve yüksek · Kişi 1: yavaş ve düşük'),
  A('İfadeleri sına','Bellek hücresi ve hazır antikor ayrımını doğru yapan ifade seçilir.','bellek: aşı · hazır antikor: serum')],
 metin='Aynı mikroba karşı, biri hazır antikor içeren bir serum, diğeri ise aşı olmak üzere iki farklı uygulama, Kişi 1 ve Kişi 2’ye 0. günde yapılmıştır. İki kişinin kanındaki antikor derişimleri izlenmiş; 50. günde her iki kişi de bu mikropla karşılaşmıştır. Sonuçlar şekilde gösterilmiştir.\nBuna göre, aşağıdakilerden hangisi doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan ifade.',ip=['Uygulamadan hemen sonraki ilk günlerde ve 50. günden sonra antikor derişimlerinin nasıl değiştiğine bak.'],
 bilgi=[B('Aşı ve serum','Aşı: zayıflatılmış ya da öldürülmüş mikrop (antijen) verilir, vücut antikor ve bellek hücresi üretir · Serum: hazır antikor verilir, etki hızlıdır ama geçicidir')],
 puf='Antikorların kaynağını ve etkinin zamanını eğriden okuyarak uygulamanın türünü sorgula.',sekil=S15)

# ======================= 16 · zor · şekil · öncüllü · kapakçık yetmezliği =======================
S16=kalp({'ra':1,'la':2,'lv':3,'ao':4,'pv':5})
d={'I':('5 numaralı damarlarda kan birikir ve akciğer kılcal damarlarında hidrostatik basınç yükselir.',True,'sol kulakçıktaki basınç artınca akciğer toplardamarlarından kulakçığa kan akışı güçleşir; kan akciğer kılcallarında birikir ve oradaki hidrostatik basınç yükselir'),
   'II':('Karıncık kasılırken 4 numaralı damara pompalanan kan miktarı sağlıklı kişiye göre artar.',False,'kanın bir kısmı kulakçığa geri kaçtığından aorta pompalanan kan miktarı artmaz, azalır'),
   'III':('1 numaralı bölümdeki kanın oksijen oranı sağlıklı kişiye göre artar.',False,'sağ kulakçığa vücuttan oksijence fakir kan döner; sol taraftaki kapakçık yetmezliği bu kanın oksijen oranını değiştirmez')}
r=onc(d,'A')
Q('0016','kalp','zor','şekilli','Kapakçık yetmezliğinin sonuçları','Kalpte kapakçık yetmezliğinin basınç ve kan akışına etkisini akciğer kılcallarındaki sıvı alışverişiyle birlikte yorumlar.','kapakçık yetmezliği senaryosu',
 'Geri kaçan kan sol kulakçık basıncını artırır; bu basınç akciğer toplardamarları ve kılcallarına yansır.','Kapakçık yetmezliğinde aorta giden kanın arttığını ya da sağ taraftaki kanın oksijen oranının değiştiğini sanmak.',
 oad(d,[A('Durumu çözümle','Sol kulakçıkla sol karıncık arasındaki iki loblu kapakçık tam kapanmadığı için karıncık kasılırken kanın bir bölümü sol kulakçığa geri kaçar.','2 numaralı bölüme geri akış')]),
 metin=omet('Şekilde, sol kulakçık ile sol karıncık arasındaki kapakçığı tam kapanmayan bir hastanın kalbi ve bazı damarları numaralandırılmıştır. Bu hastada karıncık kasılırken kanın bir kısmı sol kulakçığa geri kaçmaktadır. Kalbin diğer kapakçıkları sağlıklı çalışmaktadır.',d,'Buna göre, bu hastada sağlıklı bir kişiye göre aşağıdakilerden hangilerinin gerçekleşmesi beklenir?'),
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Beklenen sonuçlar.',ip=['Geri kaçan kanın hangi bölmede basıncı değiştireceğini ve bu basıncın hangi damarlara yansıyacağını düşün.'],
 bilgi=[B('Kapakçıkların işlevi','Kapakçıklar kanın geri akışını önler · Kapakçık yetmezliğinde kan ters yönde kaçar ve bölmelerdeki basınç ile pompalanan kan miktarı değişir')],
 puf='Geri akış basıncı bir önceki bölmeye ve ona bağlı damarlara taşır; ileri akış ise azalır.',sekil=S16)

# ======================= 17 · orta · şekil · olumsuz · damar yapıları =======================
def damar_sekli():
    b=[]
    # 1: atardamar (kalın, çok katlı duvar; dar boşluk)
    x=0
    for a,c in ((-.9,-.3),(.3,.9)): b.append(f'\\draw[line width=1.2pt,fill=orange!35] ({x+a},0) rectangle ({x+c},3.4);')
    for a in (-.9,-.6,-.3,.3,.6,.9): b.append(f'\\draw[line width=1pt] ({x+a},0)--({x+a},3.4);')
    # 2: toplardamar (ince duvar, geniş boşluk, kapakçık)
    x=3.6
    for a,c in ((-.9,-.65),(.65,.9)): b.append(f'\\draw[line width=1.2pt,fill=orange!35] ({x+a},0) rectangle ({x+c},3.4);')
    b.append(f'\\draw[line width=1.2pt] ({x-.9},0)--({x-.9},3.4);\\draw[line width=1.2pt] ({x+.9},0)--({x+.9},3.4);')
    b.append(f'\\draw[line width=1.3pt] ({x-.65},1.2) .. controls ({x-.5},1.7) and ({x-.2},1.9) .. ({x-.05},2.0);\\draw[line width=1.3pt] ({x+.65},1.2) .. controls ({x+.5},1.7) and ({x+.2},1.9) .. ({x+.05},2.0);')
    # 3: kılcal damar (tek katlı duvar, alyuvarlar tek sıra)
    x=7.2
    b.append(f'\\draw[line width=1.2pt] ({x-.35},0)--({x-.35},3.4);\\draw[line width=1.2pt] ({x+.35},0)--({x+.35},3.4);')
    for y in (.5,1.7,2.9): b.append(f'\\draw[line width=1pt,fill=red!40] ({x},{y}) ellipse (.24 and .38);')
    for x0,n in ((0,1),(3.6,2),(7.2,3)): b.append(f'\\node[font=\\large\\bfseries] at ({x0},-.6) {{{n}}};')
    return tk(''.join(b),.8)
S17=damar_sekli()
it=[('2 numaralı damarda kanın geri akışını kapakçıklar engeller; kanın ilerlemesi damar duvarındaki düz kasların kasılmasıyla sağlanır.',False,'toplardamarlarda kan, çevredeki iskelet kaslarının kasılmasıyla ve solunum hareketleriyle ilerler; kapakçıklar geri akışı önler'),
    ('1 numaralı damar, kalpten uzaklaşan kanı taşır ve kan basıncının en yüksek olduğu damar türüdür.',True,'atardamarın kalın ve esnek duvarı yüksek basınca dayanır; kalpten uzaklaştıkça basınç düşer'),
    ('3 numaralı damarın duvarı tek katlı epitelden oluştuğu için madde alışverişi bu damarda gerçekleşir.',True,'kılcal damar duvarı tek hücre kalınlığındadır; gazlar ve besinler doku sıvısıyla buradan alışveriş eder'),
    ('2 numaralı damardaki kanın akış hızı, 3 numaralı damardakinden yüksektir.',True,'kılcal damarlarda toplam kesit alanı en geniş olduğundan akış en yavaştır; toplardamarlarda hız artar'),
    ('1 numaralı damarda kalp atışıyla uyumlu nabız hissedilir, 2 numaralı damarda hissedilmez.',True,'atardamarlar kalp atışıyla genişleyip daralır ve nabız oluşturur; toplardamarda basınç düşük olduğundan nabız hissedilmez')]
r,g=tek(it,False,'B',sanc_yanlis)
Q('0017','damar','orta','şekilli','Damar yapıları','Atardamar, toplardamar ve kılcal damarın yapısı ile kan akışı özelliklerini ilişkilendirir.','damar kesitleri, olumsuz kök',
 'Damar duvarının kalınlığı, boşluğu ve kapakçık varlığı damarın türünü ve kan basıncını gösterir.','Toplardamarlarda kanın yalnız düz kas kasılmasıyla ilerlediğini sanmak.',
 [A('Damarları tanı','Kalın duvarlı, dar boşluklu damar atardamar; ince duvarlı, geniş boşluklu ve kapakçıklı damar toplardamar; tek hücre kalınlığındaki ince damar kılcal damardır.','1: atardamar · 2: toplardamar · 3: kılcal damar'),
  A('Özellikleri eşleştir','Atardamarda basınç ve nabız vardır; kılcal damarda duvar tek katlı olduğundan alışveriş gerçekleşir ve akış en yavaştır; toplardamarda akış kılcal damardan hızlıdır.','dört ifade bu özelliklerle uyumludur'),
  A('Yanlış olanı belirle','Toplardamardaki ilerleme yalnız düz kasla açıklanmaz; iskelet kaslarının ve solunum hareketlerinin katkısı vardır.','düz kas ifadesi eksiktir')],
 metin='Şekilde, insan dolaşım sisteminde bulunan üç farklı damar türünün uzunlamasına kesiti gösterilmiştir. Damarların duvar yapısı, iç boşluk genişliği ve iç yapıları birbirinden farklıdır.\nBuna göre, numaralı damarlarla ilgili aşağıdakilerden hangisi yanlıştır?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Yanlış olan ifade.',ip=['Duvar kalınlığı ve kapakçık gibi şekil ipuçlarından önce damar türlerini belirle.'],
 bilgi=[B('Damar türleri','Atardamar: kalın, esnek duvar, yüksek basınç · Toplardamar: ince duvar, kapakçık · Kılcal damar: tek katlı duvar, madde alışverişi')],
 puf='Damar türünü duvar yapısından ve kapakçıktan belirleyip her ifadeyi ayrı ayrı sına.',sekil=S17)

# ======================= 18 · zor · düz · lenf yolu ve dolaşım =======================
YAP={1:'Lakteal (bağırsak tümseğindeki lenf kılcalı)',2:'Göğüs kanalı',3:'Sol köprücükaltı toplardamarı',4:'Sağ kulakçık',5:'Akciğer atardamarı',6:'Sol kulakçık',7:'Aort'}
DOGRU18=(1,2,3,4,5,6,7)
def yol(t): return ' – '.join(map(str,t))
W18=[((1,3,2,4,5,6,7),'Lenfin önce toplardamara, sonra göğüs kanalına geçtiğini sanmıştır; oysa lenf göğüs kanalında toplanır ve ancak oradan sol köprücükaltı toplardamarına boşalır.','bilgi'),
     ((2,1,3,4,5,6,7),'Göğüs kanalını lakteal öncesine yerleştirmiştir; lenf önce bağırsak tümseğindeki lakteale girer, göğüs kanalına sonra ulaşır.','bilgi'),
     ((1,2,3,4,6,5,7),'Kanın sağ kulakçıktan sonra sol kulakçığa, ardından akciğer atardamarına geçtiğini sanmıştır; kan sağ karıncıktan akciğer atardamarıyla akciğere gider ve sol kulakçığa akciğer toplardamarlarıyla döner.','bilgi'),
     ((1,2,3,5,4,6,7),'Akciğer atardamarını sağ kulakçıktan önce yerleştirmiştir; kan sağ kulakçıktan sağ karıncığa geçer ve akciğer atardamarına ondan sonra girer.','bilgi')]
assert DOGRU18 not in [w[0] for w in W18] and len(set(w[0] for w in W18))==4
s18=[yol(W18[0][0]),yol(W18[1][0]),yol(DOGRU18),yol(W18[2][0]),yol(W18[3][0])]
Q('0018','lenf','orta','düz','Yağ sindirim ürünlerinin taşınma yolu','Yağ asidinin lenf yoluyla kana karışmasını ve ardından kalp ile akciğer dolaşımındaki yolunu sıraya koyar.','taşınma yolu sıralama',
 'Yağ asidi ve gliserol lakteale geçer; lenf göğüs kanalı ve sol köprücükaltı toplardamarıyla kana boşalır, kan önce sağ kalbe ve akciğere gider.','Bütün besinlerin karaciğer kapı toplardamarıyla taşındığını sanmak; akciğer dolaşımının sırasını karıştırmak.',
 [A('Emilimi belirle','Yağın sindirim ürünleri (yağ asidi, gliserol) bağırsak tümseğindeki lenf kılcalına (lakteal) geçer; glikoz gibi karaciğer kapı toplardamarına geçmez.','başlangıç: 1'),
  A('Lenfin kana karışması','Lenf göğüs kanalında toplanır ve sol köprücükaltı toplardamarına boşalır; kan oradan üst ana toplardamara ve sağ kulakçığa ilerler.','1 → 2 → 3 → 4'),
  A('Kalp ve akciğer yolunu izle','Sağ kulakçıktan sağ karıncığa geçen kan akciğer atardamarıyla akciğere gider; akciğer toplardamarlarıyla sol kulakçığa döner ve sol karıncık yoluyla aorta pompalanır.','4 → 5 → 6 → 7'),
  A('Sıralamayı yaz','Tüm yapılar bu sırayla birleştirilir.',yol(DOGRU18))],
 metin='Bir kişi yağlı bir yemek yemiştir. İnce bağırsakta sindirilen yağın son ürünleri olan yağ asidi ve gliserol, bağırsak epitelinden emilmiştir. Aşağıda bazı yapılar numaralandırılmıştır:\n'+'\n'.join(f'{k}. {v}' for k,v in YAP.items())+'\nBu yağ asidi molekülü emildikten sonra aorta ulaşıncaya kadar yukarıdaki yapılardan hangi sırayla geçer?',
 dogru=yol(DOGRU18),sira=s18,yan=[(yol(t),a,tu) for t,a,tu in W18],
 istenen='Yağ asidinin yapılardan geçiş sırası.',ip=['Yağın sindirim ürünlerinin kana hangi damar sistemiyle, hangi toplardamara boşalarak karıştığını hatırla.'],
 bilgi=[B('Lenfin kana karışması','Lenf damarları birleşerek göğüs kanalını oluşturur; lenf köprücükaltı toplardamarlarında kana karışır'),B('Akciğer dolaşımı','Sağ karıncık → akciğer atardamarı → akciğer → akciğer toplardamarı → sol kulakçık')],
 puf='Besin ürününün emildiği yapıyı belirleyip hangi damar sistemine geçtiğini sorgula.')

# ======================= 19 · orta · öncüllü · bağışıklık hücreleri =======================
d={'I':('Makrofajlar, vücuda giren mikroorganizmaları fagositozla yok eder ve bu işlem mikrop türüne özgü (özgül) savunmanın bir parçasıdır.',False,'makrofajların fagositozu mikrop türünü ayırt etmez; özgül olmayan savunmanın parçasıdır'),
   'II':('B lenfositlerden farklılaşan plazma hücreleri, antijene özgü antikor üretir.',True,'B lenfositler antijenle karşılaşınca plazma hücrelerine dönüşür ve antikor salgılar'),
   'III':('Sitotoksik T lenfositler, enfekte olmuş vücut hücrelerini yok ederek hücresel bağışıklıkta görev alır.',True,'sitotoksik T lenfositler virüslü ya da bozulmuş hücreleri öldürür; bu hücresel bağışıklıktır')}
r=onc(d,'E')
Q('0019','bag','orta','öncüllü','Bağışıklık hücreleri','Doğal ve kazanılmış bağışıklıkta görev alan hücreleri ve işlevlerini ayırt eder.','bağışıklık hücreleri öncülleri',
 'Fagositler özgül olmayan, lenfositler özgül bağışıklıkta görev alır; B lenfositler antikor (humoral), T lenfositler hücresel bağışıklık sağlar.','Plazma hücrelerini T lenfositlerden sanmak; makrofajları özgül savunmaya dâhil etmek.',
 oad(d),metin=omet('İnsan vücudu mikroorganizmalara karşı doğal ve kazanılmış bağışıklık mekanizmalarıyla korunur. Bu mekanizmalarda görev alan bazı hücreler ve işlevleriyle ilgili aşağıdaki yargılar verilmiştir.',d,'Buna göre, bu yargılardan hangileri doğrudur?'),
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',ip=['Her hücre türünün özgül mü özgül olmayan mı savunmada görev yaptığını ve ne ürettiğini düşün.'],
 bilgi=[B('Bağışıklık hücreleri','Makrofaj: fagositoz · B lenfosit → plazma hücresi → antikor · T lenfosit: hücresel bağışıklık')],
 puf='Her hücrenin hangi savunma basamağında ve hangi işlevle görev aldığını ayrı ayrı sorgula.')

# ======================= 20 · orta · olumsuz · bağışıklık türleri ve savunma =======================
it=[('Suçiçeği geçiren bir kişinin aynı virüse karşı uzun süre korunması, kazanılmış aktif bağışıklığa örnektir.',True,'hastalığı geçirmek antikor ve bellek hücresi oluşturur; bu aktif bağışıklıktır'),
    ('Anne sütüyle bebeğe geçen antikorlar, bebekte kazanılmış pasif bağışıklık sağlar.',True,'antikorlar hazır alındığından bağışıklık pasiftir ve geçicidir'),
    ('Plasentadan anneden bebeğe geçen antikorlar, bebekte bellek hücrelerinin oluşmasını sağlayarak kalıcı koruma oluşturur.',False,''),
    ('Deri ve mukus, mikroorganizmaların vücuda girişini engelleyen özgül olmayan savunma engelleridir.',True,'deri ve mukus mikrop türü ayırt etmeden fiziksel ve kimyasal engel oluşturur'),
    ('İnterferonlar, virüs enfekte hücreler tarafından salgılanır ve komşu hücrelerin virüse karşı korunmasına yardımcı olur.',True,'interferonlar komşu hücrelerde virüs çoğalmasını engelleyen özgül olmayan savunma maddeleridir')]
def sanc20(m,n): return f'Bu ifadeyi yanlış sanmış; oysa doğrudur: {n}.'
r,g=tek(it,False,'A',sanc20)
Q('0020','bag','orta','düz','Doğal ve kazanılmış bağışıklık','Özgül olmayan savunma, aktif ve pasif bağışıklık kavramlarını doğru ve yanlış ifadeler içinde ayırt eder.','bağışıklık ifadeleri, olumsuz kök',
 'Hazır antikor geçişi (anne sütü, plasenta, serum) pasif bağışıklıktır: geçicidir ve bellek hücresi oluşturmaz.','Anneden geçen antikorların kalıcı bellek oluşturduğunu sanmak.',
 [A('Savunma türlerini hatırla','Deri, mukus ve interferon özgül olmayan; antikor ve bellek hücreleri özgül savunmadandır. Vücudun kendi ürettiği antikor aktif, hazır alınan antikor pasif bağışıklıktır.','özgül olmayan: deri, mukus, interferon · aktif: kendi üretimi · pasif: hazır antikor'),
  A('İfadeleri değerlendir','Suçiçeği geçirmek aktif, anne sütü ile geçen antikor pasif bağışıklıktır; deri-mukus ve interferon ifadeleri doğrudur.','dört ifade doğru'),
  A('Yanlış olanı seç','Plasentadan geçen antikorlar hazır olduğundan bebekte bellek hücresi oluşturmaz ve koruma geçicidir.','plasenta ifadesi yanlış')],
 metin='Vücudun savunması, mikroorganizmaların vücuda girişini engelleyen engellerden başlayarak antikor ve bellek hücrelerinin görev aldığı özgül yanıta kadar uzanan basamaklardan oluşur. Bağışıklık kazanma yolları aktif ya da pasif olabilir.\nBuna göre, bu savunma basamakları ve bağışıklık türleriyle ilgili aşağıdakilerden hangisi yanlıştır?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Yanlış olan ifade.',ip=['Antikorların kişinin kendi hücrelerince mi üretildiğini, yoksa hazır mı geçtiğini ayırt et.'],
 bilgi=[B('Bağışıklık türleri','Aktif: vücut antikor ve bellek hücresi üretir · Pasif: hazır antikor alınır, bellek oluşmaz, koruma geçicidir · Doğal ve yapay olabilir')],
 puf='Antikorun kaynağını (kendi ürettiği mi, hazır mı) sorgula.')

# ======================= yaz =======================
assert len(P.ANA)==20,len(P.ANA)
for qq in P.ANA: qq['kardes']=None
P.yaz(os.path.join(BD,'dolasim-1.json'),'/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/bos-dolasim.json')
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=UK))['kartlar'].append(c['id'])
json.dump(dict(konu=KONU_,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2018–2026 Biyoloji dolaşım ve bağışıklık soruları (yalnız mantık), MEB 11. sınıf biyoloji müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','abdolasim.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
