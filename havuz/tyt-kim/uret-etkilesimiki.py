"""TYT Kimya · Kimyasal Türler Arası Etkileşimler · ek paket (etkilesimiki): 24 soru, kardeş yok, ipucu 1.
Şekil verileri Python'da hesaplanır; TikZ bu değerlerden üretilir. Her cevap/çeldirici değer ve her öncül betikte TEK yerde tanımlanır."""
import sys,os,math
GD=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,GD)
import _hafif_kim2 as H
from _hafif_kim2 import *
from _hafif_kim import onc,tek,etk,kab,yer
KONU_='Kimyasal Türler Arası Etkileşimler'; UK='kim|Kimyasal Türler Arası Etkileşimler'
H.KONU=KONU_
P=Parti('etkilesimiki',KONU_,UK,ders='TYT Kimya',idon='tytkim')
KY='ÖSYM 2018–2026 TYT Kimya (yalnız mantık) · MEB 9. sınıf Kimyasal Türler Arası Etkileşimler'
TIPMAP={'tur':('tur','Atom, iyon, molekül ve tanecik modeli'),'kaplar':('tur',None),'formul':('formul','İyonik/kovalent bileşik formülü, adı ve bileşimi'),'kovadlandirma':('formul',None),'iyonproton':('formul',None),'karisikbag':('formul',None),
 'lewis':('lewis','Lewis yapısı ve molekül polarlığı'),'noktalewis':('lewis',None),'lewis3':('lewis',None),'polar':('lewis',None),
 'metalik':('ozellik','Bağ türü ve madde özellikleri'),'iletken':('ozellik',None),'metalikgucu':('ozellik',None),'kirilgan':('ozellik',None),'bagturu':('ozellik',None),
 'hidrur':('zayif','Zayıf etkileşimler ve kaynama noktası'),'hbagi':('zayif',None),'soygaz':('zayif',None),'dipollondon':('zayif',None),'siralama':('zayif',None),
 'degisim':('degisim','Fiziksel ve kimyasal değişim, enerji'),'enerji':('degisim',None),'sinif':('degisim',None),'isitma':('degisim',None)}
TIPAD={}
def S(no,alt,tipId,tip,z,kalip,fikir,tuzak,kaz,oz,deg,ad,**k):
    nt,na=TIPMAP[tipId]
    if na: TIPAD[nt]=na
    tipId=nt; tip=TIPAD[nt]
    kart(f'K-KMET2-{no[-2:]}',alt,fikir,tuzak,z,kalip,len(ad),f'km-et2-{tipId}',tip,KY)
    mk(P,no,ad=ad,adim=len(ad),tipId=f'km-et2-{tipId}',tip=tip,z=z,alt=alt,kaz=kaz,kalip=kalip,kart=f'K-KMET2-{no[-2:]} ({oz}) · {deg}',**k)
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
ARR='-{Stealth[length=2mm,width=1.8mm]}'
def tk(g,head=HEAD): return tikz_svg(head+g+TAIL)
def pt(x,y): return f'({x:.3f},{y:.3f})'
STD=['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III']
ORD=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
def oc(d,sira):
    tup=[tuple(x for x in t.replace('Yalnız ','').replace(',',' ').replace(' ve ',' ').split()) for t in sira]
    return onc(d,tup)
def siralist(*k):
    assert [x for x in ORD if x in k]==list(k),k
    return list(k)

# ---------------- ortak çizim: Lewis ----------------
def pair(x,y,dx,dy,sep=.075):
    return f'\\fill {pt(x-dx*sep,y-dy*sep)} circle (.04); \\fill {pt(x+dx*sep,y+dy*sep)} circle (.04);'
def lewis(atoms,bonds,lones,ox=0,oy=0,gizle=()):
    """atoms {ad:(x,y,sembol)}; bonds [(a,b,n)]; lones [(a,açı,)] her biri bir ortaklanmamış çift."""
    o=[]
    for a,(x,y,s) in atoms.items(): o.append(f'\\node at {pt(ox+x,oy+y)} {{\\large {s}}};')
    for a,b,n in bonds:
        (x1,y1,_),(x2,y2,_)=atoms[a],atoms[b]; L=math.hypot(x2-x1,y2-y1); ux,uy=(x2-x1)/L,(y2-y1)/L; px,py=-uy,ux
        for i in range(n):
            off=(i-(n-1)/2)*.2; o.append(pair(ox+(x1+x2)/2+off*ux,oy+(y1+y2)/2+off*uy,px,py))
    for a,ang in lones:
        x,y,_=atoms[a]; v=(math.cos(math.radians(ang)),math.sin(math.radians(ang)))
        o.append(pair(ox+x+.4*v[0],oy+y+.4*v[1],-v[1],v[0]))
    return '\n'.join(o)
def valence(atoms,bonds,lones):
    """her atomun değerlik elektron sayısı = bağ sayısı + 2·ortaklanmamış çift; oktet/dublet kontrolü"""
    r={}
    for a in atoms:
        b=sum(n for x,y,n in bonds if a in (x,y)); l=sum(1 for x,_ in lones if x==a)
        tot=2*b+2*l; assert tot==(2 if atoms[a][2]=='H' else 8),(a,tot); r[a]=b+2*l
    return r

# ====================================================================================
# 01 · kimyasal tür (atom, iyon, molekül) · kolay · öncüllü
tur_={'X':(11,10),'Y':(17,18),'Z':(10,10),'T':(8,8)}
yuk={a:p-e for a,(p,e) in tur_.items()}; assert yuk=={'X':1,'Y':-1,'Z':0,'T':0}
d={'I':(True,'proton sayısı elektron sayısından fazla olan X, +1 yüklü katyondur'),
   'II':(True,'elektron sayısı proton sayısından fazla olan Y, −1 yüklü anyondur'),
   'III':(False,'tek çekirdekli nötr bir tanecik atomdur; molekül en az iki atomun bağlanmasıyla oluşur')}
r=oc(d,STD); assert r['dogru']=='I ve II'
S('0001','Kimyasal Türler','tur','Atom, iyon ve molekül ayrımı','kolay','öncüllü','Proton–elektron sayısı karşılaştırılarak tanecik atom, katyon ya da anyon olarak sınıflanır; molekül en az iki atomdan oluşur.','Tek atomlu nötr taneciğe “molekül” demek; elektron fazlasını katyon sanmak.',
 'Taneciklerin proton ve elektron sayılarından yüklerini bularak kimyasal tür sınıflaması yapar.','tanecik sınıflaması','proton ve elektron sayıları',
 [A('Yükleri hesapla','Yük = proton sayısı − elektron sayısı.','X: 11 − 10 = +1 · Y: 17 − 18 = −1 · Z: 10 − 10 = 0 · T: 8 − 8 = 0'),
  A('I ve II’yi değerlendir','Pozitif yüklü tanecik katyon, negatif yüklü anyondur.','X katyon → I: doğru · Y anyon → II: doğru'),
  A('III’ü değerlendir','Z ve T tek atomlu nötr taneciklerdir; atom adını alır.','III: yanlış'),
  A('Sonuç','Doğru öncüller toplanır.',etk(d)+' · Sonuç: I ve II')],
 metin='Bir öğrenci, hepsi tek çekirdekli olan X, Y, Z ve T taneciklerinin proton ve elektron sayılarını deftere şöyle yazmıştır: X: 11 proton, 10 elektron; Y: 17 proton, 18 elektron; Z: 10 proton, 10 elektron; T: 8 proton, 8 elektron.\nI. X katyondur.\nII. Y anyondur.\nIII. Z ve T nötr oldukları için molekül olarak adlandırılır.\nBuna göre hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',
 ip=['Her taneciğin yükünü proton ve elektron sayısını karşılaştırarak bul; sonra “molekül” sözcüğünün tanımına bak.'],
 bilgi=[B('Kimyasal tür','Atom, iyon ve molekül kimyasal türlerdir. Proton sayısı elektron sayısından fazlaysa katyon, azsa anyondur. Örnek: 12 proton ve 10 elektronlu tanecik +2 yüklü katyondur'),B('Molekül','Aynı ya da farklı cins en az iki atomun kovalent bağla bağlanmasıyla oluşan nötr tanecik moleküldür. Örnek: H₂O')],
 puf='Önce yükü bul: proton − elektron; nötr tek atom “atom”, yüklü tanecik “iyon”dur.')

# 02 · tanecik modeli: kaplar · kolay · düz şekil
RAD={'H':.17,'O':.24,'Ne':.26,'Na':.23,'Cl':.29}
LAB={'H':'H','O':'O','Ne':'Ne','Na':'Na$^+$','Cl':'Cl$^-$'}
TM={'Ne':[('Ne',0,0)],'O2':[('O',-.17,0),('O',.17,0)],'H2':[('H',-.1,0),('H',.1,0)],'H2O':[('O',0,0),('H',-.24,-.27),('H',.24,-.27)],'Na':[('Na',0,0)],'Cl':[('Cl',0,0)]}
FIL={'H':'white','O':'gray!35','Ne':'vurgu!20','Na':'vurgu!20','Cl':'gray!20'}
def kap(x0,items,etiket,w=1.9,h=1.8):
    o=[f'\\draw[thick] ({x0},{h}) -- ({x0},0) -- ({x0+w},0) -- ({x0+w},{h});']
    for t,cx,cy,rot in items:
        c,s=math.cos(math.radians(rot)),math.sin(math.radians(rot))
        for a,dx,dy in TM[t]:
            X=x0+cx+dx*c-dy*s; Y=cy+dx*s+dy*c
            o.append(f'\\draw[fill={FIL[a]}] {pt(X,Y)} circle ({RAD[a]}); \\node[font=\\tiny] at {pt(X,Y)} {{{LAB[a]}}};')
    o.append(f'\\node[font=\\small\\bfseries] at {pt(x0+w/2,-.35)} {{{etiket}}};')
    return '\n'.join(o)
g=[]
g.append(kap(0,[('Ne',.5,.5,0),('Ne',1.4,.55,0),('Ne',.9,1.15,0),('Ne',.45,1.45,0),('Ne',1.45,1.4,0)],'I'))
g.append(kap(2.2,[('O2',.7,.45,20),('O2',1.35,1.0,-50),('O2',.65,1.4,80)],'II'))
lat=[]
for i in range(3):
    for j in range(2):
        lat.append(('Na' if (i+j)%2==0 else 'Cl',.5+i*.62,.55+j*.62,0))
g.append(kap(6.6,lat,'IV'))
g.append(kap(4.4,[('H2O',.55,.5,0),('H2O',1.3,.6,160),('H2O',.9,1.38,200)],'III'))
g.append(kap(8.8,[('H2',.5,.4,30),('H2',1.35,.5,-30),('H2',.5,1.3,90),('H2',1.35,1.35,0)],'V'))
SK2=tk('\n'.join(g))
d2=dict(I='yalnızca tek atomlu soygaz',II='iki oksijen atomundan oluşan element molekülü',III='iyonik bileşik',IV='farklı cins atomlardan oluşan bileşik molekülü',V='iki hidrojen atomundan oluşan element molekülü')
S('0002','Kimyasal Türler','kaplar','Tanecik modelinden madde türü','kolay','şekilli','Kapta çizilen taneciklerin atom, iyon ya da molekül; molekülün aynı ya da farklı cins atomdan oluştuğu okunur.','Bileşik olan iyonik maddeyi molekül sanmak; element molekülünü bileşik saymak.',
 'Tanecik modelinden maddenin atom, iyon, element molekülü ya da bileşik molekülü olduğunu belirler.','tanecik modeli','5 kapta farklı kimyasal türler',
 [A('Taneciklere bak','Kaplardaki taneciklerin cinsi ve birbirine bağlı olup olmadığı okunur.','I: Ne atomları · II: O₂ · III: H₂O · IV: Na⁺ ve Cl⁻ · V: H₂'),
  A('Molekülleri ayır','Molekül, bağlı en az iki atomdan oluşur; iyonik madde ve soygaz molekül içermez.','molekül içeren: II, III, V'),
  A('Farklı cins atomu ara','Bileşik molekülünde farklı cins atomlar bulunur.','II: O–O, V: H–H, III: O–H'),
  A('Sonuç','Yalnız H₂O kabında farklı cins atomlar bağlıdır.','Cevap: H₂O’nun bulunduğu kap')],
 metin='Beş ayrı kapalı kapta, oda koşullarında bulunan birer saf maddenin tanecik modeli şekilde gösterilmiştir. Taneciklerin içindeki simgeler atom ya da iyon cinsini belirtmektedir; birbirine değen atomlar birbirine bağlıdır.\nBuna göre hangi kapta bulunan maddenin yapı birimi, farklı cins atomlardan oluşan moleküldür?',
 dogru='III',yan=[('I','Ne atomlarını molekül sanmış; soygazlar tek atomlu bulunur.','bilgi'),('II','O₂’nin molekül olduğunu görmüş ama iki atomun da aynı cins olduğunu atlamış.','dikkat'),('IV','Bileşik olan iyonik maddeyi moleküllerden oluşmuş sanmış; yapı birimi iyondur.','bilgi'),('V','H₂’yi bileşik molekülü sanmış; iki atom da hidrojendir.','dikkat')],
 sira=['I','II','III','IV','V'],istenen='Yapı birimi bileşik molekülü olan maddenin bulunduğu kap.',
 ip=['Önce hangi kapların moleküllerden oluştuğunu belirle, sonra bu moleküllerin atomlarının aynı cins olup olmadığına bak.'],
 bilgi=[B('Madde ve yapı birimi','Element atomlardan ya da aynı cins atomlu moleküllerden, bileşik farklı cins atomlu moleküllerden ya da iyonlardan oluşur. Örnek: O₂ element, CO₂ bileşiktir')],
 puf='Yapı birimi “molekül” ise bileşik demek için moleküldeki atomların farklı cins olması gerekir.',sekil=SK2)

# 03 · iyonik bileşik formülü (çok atomlu iyonlar) · orta · tablo · olumsuz kök
KAT={'Na⁺':('Na',1),'Mg²⁺':('Mg',2),'Ca²⁺':('Ca',2),'Al³⁺':('Al',3),'NH₄⁺':('NH₄',1)}
AN={'Cl⁻':('Cl',1,False),'OH⁻':('OH',1,True),'NO₃⁻':('NO₃',1,True),'SO₄²⁻':('SO₄',2,True),'PO₄³⁻':('PO₄',3,True)}
SUB=dict(zip('0123456789','₀₁₂₃₄₅₆₇₈₉'))
def formul(kat,an):
    ks,kq=KAT[kat]; as_,aq,poly=AN[an]; g_=math.gcd(kq,aq); nk,na=aq//g_,kq//g_
    ps=lambda s,n,p: s if n==1 else ((f'({s})' if p else s)+''.join(SUB[c] for c in str(n)))
    return ps(ks,nk,ks=='NH₄')+ps(as_,na,poly)
assert formul('Mg²⁺','PO₄³⁻')=='Mg₃(PO₄)₂' and formul('NH₄⁺','Cl⁻')=='NH₄Cl' and formul('Ca²⁺','OH⁻')=='Ca(OH)₂' and formul('Na⁺','SO₄²⁻')=='Na₂SO₄' and formul('Al³⁺','NO₃⁻')=='Al(NO₃)₃'
satir=[('Amonyum klorür','NH₄⁺','Cl⁻',None),('Kalsiyum hidroksit','Ca²⁺','OH⁻',None),('Magnezyum fosfat','Mg²⁺','PO₄³⁻','Mg₂(PO₄)₃'),('Sodyum sülfat','Na⁺','SO₄²⁻',None),('Alüminyum nitrat','Al³⁺','NO₃⁻',None)]
ROM=['I','II','III','IV','V']
rows=[[ROM[i],s[0],s[3] or formul(s[1],s[2])] for i,s in enumerate(satir)]
assert rows[2][2]!=formul('Mg²⁺','PO₄³⁻')
SK3=tablo_svg(['Satır','Bileşiğin adı','Yazılan formül'],rows)
sec=[(f'{ROM[i]}',i!=2,f'{satir[i][0]} için {satir[i][1]} ve {satir[i][2]} iyonlarının yükleri dengelenince formül {formul(satir[i][1],satir[i][2])} olur') for i in range(5)]
r=tek(sec,False)
S('0003','Güçlü Etkileşimler','formul','Çok atomlu iyonlu bileşiğin formülü','orta','tablo','Katyon ve anyon yükleri çaprazlanarak indisler bulunur; çok atomlu iyondan birden fazla varsa parantez içine alınır.','Çaprazlamada yükü iyon sayısı yerine atom sayısı yapmak; parantez ve indisi karıştırmak.',
 'Çok atomlu iyon içeren iyonik bileşiklerin formülünü yük dengesine göre yazar.','iyonik bileşik formülü','amonyum, hidroksit, sülfat, fosfat, nitrat',
 [A('Yükleri yaz','Verilen iyonların yükleri hatırlanır.','NH₄⁺, Cl⁻, Ca²⁺, OH⁻, Mg²⁺, PO₄³⁻, Na⁺, SO₄²⁻, Al³⁺, NO₃⁻'),
  A('Yükleri çaprazla','Katyonun yükü anyonun, anyonun yükü katyonun indisi olur; çok atomlu iyon parantez içine alınır.','Ca(OH)₂ · Na₂SO₄ · Al(NO₃)₃ · NH₄Cl'),
  A('III. satırı kontrol et','Mg²⁺ ile PO₄³⁻ için çaprazlama yapılır.','Mg: 3 tane (3 × 2 = 6) · PO₄: 2 tane (2 × 3 = 6) → Mg₃(PO₄)₂'),
  A('Sonuç','Yazılan Mg₂(PO₄)₃ formülünde indisler ters yazılmıştır.','Cevap: III')],
 metin='Bir öğrenci, gübre ve temizlik ürünlerinde bulunan bazı iyonik bileşiklerin adlarını ve formüllerini tablodaki gibi yazmıştır. İyon yükleri NH₄⁺: +1, OH⁻: −1, NO₃⁻: −1, SO₄²⁻: −2, PO₄³⁻: −3, Na⁺: +1, Ca²⁺: +2, Mg²⁺: +2, Al³⁺: +3 ve Cl⁻: −1’dir.\nBuna göre hangi satırdaki formül yanlıştır?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Formülü yanlış yazılmış satır.',
 ip=['Her satırda toplam pozitif yükün toplam negatif yüke eşit olup olmadığını kontrol et.'],
 bilgi=[B('İyonik bileşik formülü','Toplam pozitif yük toplam negatif yüke eşit olacak biçimde iyon sayıları seçilir; çok atomlu iyondan birden fazla varsa parantez kullanılır. Örnek: Na⁺ ve CO₃²⁻ → Na₂CO₃')],
 puf='Formülün doğruluğunu hızlıca denetlemek için indis × yük çarpımlarını katyon ve anyonda karşılaştır.',sekil=SK3)

# 04 · fiziksel / kimyasal değişim ve bağ · kolay · öncüllü
d={'I':(False,'su buharlaşırken moleküller arası etkileşimler kopar; molekül içindeki O–H bağları korunur'),
   'II':(True,'mum yanarken yeni maddeler oluşur; eski bağlar kırılıp yenileri kurulur'),
   'III':(True,'süblimleşme fiziksel değişimdir; yalnız moleküller arası etkileşimler zayıflar')}
r=oc(d,siralist('Yalnız II','Yalnız III','I ve II','I ve III','II ve III')); assert r['dogru']=='II ve III'
S('0004','Fiziksel ve Kimyasal Değişimler','degisim','Değişimde bağ kırılması ve oluşması','kolay','öncüllü','Fiziksel değişimde molekül yapısı korunur, yalnız moleküller arası etkileşimler değişir; kimyasal değişimde atomlar arası bağlar kırılıp yenileri oluşur.','Buharlaşmada moleküllerin atomlarına ayrıldığını sanmak.',
 'Fiziksel ve kimyasal değişimleri bağ kırılması ve oluşması açısından ayırt eder.','fiziksel–kimyasal değişim','buharlaşma, yanma, süblimleşme',
 [A('I. öncül','Buharlaşmada moleküller birbirinden ayrılır, molekülün kendisi bozulmaz.','O–H bağları korunur → I: yanlış'),
  A('II. öncül','Yanma kimyasal değişimdir; yeni maddeler oluşur.','bağlar kırılır ve yeniden oluşur → II: doğru'),
  A('III. öncül','Süblimleşme hâl değişimidir; fiziksel değişimdir.','yalnız moleküller arası etkileşim → III: doğru'),
  A('Sonuç','Doğru olanlar toplanır.',etk(d)+' · Sonuç: II ve III')],
 metin='Bir kimya öğretmeni, mutfakta gözlenen olaylarla ilgili tahtaya şu yargıları yazıyor.\nI. Çaydanlıktaki suyun buharlaşması sırasında H₂O moleküllerinin içindeki O–H bağları kırılır.\nII. Mumun yanarken kimyasal değişime uğraması, atomlar arası bağların kırılıp yeni bağların oluşmasıyla gerçekleşir.\nIII. İyot kristallerinin ısıtılınca mor buhara dönüşmesi sırasında molekül yapısı değişmez.\nBuna göre hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',
 ip=['Her olayda yeni bir madde oluşup oluşmadığına, yani molekülün kendisinin değişip değişmediğine bak.'],
 bilgi=[B('Fiziksel ve kimyasal değişim','Fiziksel değişimde maddenin kimliği değişmez; hâl değişimlerinde yalnız moleküller arası etkileşimler değişir. Kimyasal değişimde atomlar arası bağlar kırılır ve yeni maddeler oluşur. Örnek: şekerin erimesi fiziksel, yanması kimyasal değişimdir')],
 puf='Yeni madde oluşuyorsa atomlar arası bağlar değişmiştir; hâl değişiminde bağlar değil, moleküller arası etkileşimler değişir.')

# 05 · kovalent bileşik adlandırma · kolay · düz
ONEK={1:'mono',2:'di',3:'tri',4:'tetra',5:'penta'}
EL={'C':('karbon','karbon'),'N':('azot','nitrür'),'S':('kükürt','sülfür'),'P':('fosfor','fosfür'),'O':('oksijen','oksit'),'Cl':('klor','klorür')}
def adx(e1,n1,e2,n2):
    a={'N':'azot'}.get(e1,EL[e1][0]); b={'O':'oksit','Cl':'klorür','S':'sülfür'}[e2]
    return ('' if n1==1 else ONEK[n1])+a+' '+(ONEK[n2]+b).replace('mono'+'oksit','monoksit')
assert adx('S',1,'O',3)=='kükürt trioksit' and adx('N',2,'O',4)=='diazot tetraoksit' and adx('P',2,'O',5)=='difosfor pentaoksit' and adx('C',1,'O',1)=='karbon monoksit' and adx('Cl',2,'O',1)=='diklor monoksit'
secs=[('N₂O₄ – azot tetraoksit',False,'ilk elementin atom sayısı 2 olduğu için “di” öneki gerekir: diazot tetraoksit'),
      ('SO₃ – kükürt trioksit',True,''),
      ('P₂O₅ – fosfor pentaoksit',False,'ilk element de “di” alır: difosfor pentaoksit'),
      ('CO – monokarbon monoksit',False,'ilk elementte atom sayısı 1 ise “mono” yazılmaz: karbon monoksit'),
      ('Cl₂O – klor monoksit',False,'ilk elementin 2 atomu için “di” gerekir: diklor monoksit')]
r=tek(secs,True)
S('0005','Güçlü Etkileşimler','kovadlandirma','Kovalent bileşik adlandırma (mono, di, tri)','kolay','düz','İki ametalden oluşan kovalent bileşiklerde atom sayıları mono-, di-, tri- önekleriyle belirtilir; ilk elementte 1 atom varsa mono yazılmaz; ikinci elementin adı -ür/-it ile biter.','İlk elementin önekini unutmak ya da karbon monoksit yerine monokarbon monoksit yazmak.',
 'İki ametalden oluşan kovalent bileşiklerin formülünü ve adını mono-, di-, tri- öneklerine göre eşleştirir.','kovalent bileşik adlandırması','N₂O₄, SO₃, P₂O₅, CO, Cl₂O',
 [A('Kuralı hatırla','Atom sayısı öneklerle yazılır; ilk elementte yalnız bir atom varsa mono kullanılmaz.','1: mono · 2: di · 3: tri · 4: tetra · 5: penta'),
  A('Şıkları ele','Her şıktaki ilk ve ikinci elementin atom sayısı öneke çevrilir.','N₂O₄ → diazot tetraoksit · P₂O₅ → difosfor pentaoksit · CO → karbon monoksit · Cl₂O → diklor monoksit'),
  A('Doğru adı bul','Yalnız SO₃’te ilk elementte tek atom vardır ve ad kurala uygundur.','SO₃ → kükürt trioksit'),
  A('Sonuç','Doğru eşleşme bulunur.','Cevap: SO₃ – kükürt trioksit')],
 metin='Bir laboratuvar şişelerinin üzerindeki etiketlerde, iki ametalden oluşan bazı kovalent bileşiklerin formülleri ile adları birlikte yazılıdır. Etiketleri okuyan öğrenciden, kovalent bileşik adlandırma kurallarına göre formülü ve adı doğru eşleşen şişeyi bulması isteniyor.\nBuna göre hangi etiket doğru yazılmıştır?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Formülü ve adı doğru eşleşen kovalent bileşik.',
 ip=['Her adın ilk sözcüğünde ilk elementin atom sayısının nasıl belirtildiğine bak.'],
 bilgi=[B('Kovalent bileşik adı','Ametal–ametal bileşiklerinde atom sayıları mono (1), di (2), tri (3), tetra (4), penta (5) öneklerle söylenir; ilk elementte tek atom varsa mono yazılmaz. Örnek: CO₂ karbon dioksit, N₂O₃ diazot trioksit')],
 puf='Önce ilk elementin atom sayısına bak: 1 ise önek yok, 2 ve üzeri ise di, tri…')

# 06 · metalik bağ · kolay · öncüllü
d={'I':(True,'metalik bağda değerlik elektronları belirli bir atoma ait değildir, pozitif yüklü atom kalıpları arasında serbestçe dolaşır'),
   'II':(False,'katı metaller de elektriği iletir; serbest elektronlar yük taşır'),
   'III':(True,'tabakalar kaydığında elektron denizi katyonları sarmaya devam ettiği için metal dövülebilir ve tel çekilebilir')}
r=oc(d,siralist('Yalnız I','Yalnız II','I ve II','I ve III','II ve III')); assert r['dogru']=='I ve III'
S('0006','Güçlü Etkileşimler','metalik','Metalik bağ ve özellikleri','kolay','öncüllü','Metalik bağda değerlik elektronları katyonlar arasında serbest dolaşır; elektrik iletkenliği, dövülebilirlik ve tel çekilebilme bununla açıklanır.','Metallerin yalnız sıvı hâlde iletken olduğunu sanmak; elektron denizini iyonik bağla karıştırmak.',
 'Metalik bağın nitel modelini ve metallerin özelliklerini ilişkilendirir.','metalik bağ','bakır tel, dövülebilirlik, iletkenlik',
 [A('I. öncül','Metalik bağın temel fikri serbest elektron denizidir.','I: doğru'),
  A('II. öncül','Metalde serbest elektronlar katı hâlde de hareket eder.','katı metal iletkendir → II: yanlış'),
  A('III. öncül','Kayma sırasında elektron denizi katyonları bir arada tutar.','III: doğru'),
  A('Sonuç','Doğru olanlar toplanır.',etk(d)+' · Sonuç: I ve III')],
 metin='Bir elektrik teli üretiminde bakır külçe önce ısıtılıp sonra dövülüyor, ardından çekilerek tel hâline getiriliyor. Teknisyen, bakırın bu işlemler sırasında kırılmadığını ve soğuduktan sonra da elektriği iyi ilettiğini gözlemliyor ve metalik bağla ilgili şu yargıları yazıyor.\nI. Değerlik elektronları katyonlar arasında serbestçe dolaşır.\nII. Katı metaller elektriği iletmez.\nIII. Katyon tabakaları kayınca bağ kopmaz, bu yüzden metal şekillendirilebilir.\nBuna göre hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',
 ip=['Metalik bağda elektronların atomlara bağlı olup olmadığını ve katyon tabakaları kayarken ne olduğunu düşün.'],
 bilgi=[B('Metalik bağ','Metal atomları değerlik elektronlarını ortak bir “elektron denizine” verir; pozitif atom kalıpları bu denizle sarılıdır. Örnek: sodyum metalinde Na⁺ katyonları elektron denizi içinde dizilidir')],
 puf='Metalik bağ yönlenmez: elektron denizi sayesinde metaller hem iletken hem dövülebilirdir.')

# 07 · Lewis yapısı verilen molekülde grup bulma · orta · şekil
at7={'H':(0,0,'H'),'X':(1.5,0,'X'),'Y':(3.0,0,'Y')}; bg7=[('H','X',1),('X','Y',3)]; ln7=[('Y',0)]
val7=valence(at7,bg7,ln7); assert val7=={'H':1,'X':4,'Y':5}
SK7=tk(lewis(at7,bg7,ln7),HEAD.replace('font=\\small]','font=\\small,scale=1.5,every node/.style={scale=1.5}]'))
secs=[('X: 4A, Y: 5A',True,''),('X: 4A, Y: 6A',False,'Y’nin ortaklanmamış çifti de değerlik elektronudur: 3 + 2 = 5, 6 değil'),('X: 3A, Y: 5A',False,'X’in 4 bağı vardır ve hiç ortaklanmamış çifti yoktur; değerlik elektronu 3 değil 4’tür'),('X: 5A, Y: 5A',False,'X yalnız 4 elektronunu ortaklaşa kullanır; 5 elektron sayımı hatalıdır'),('X: 5A, Y: 6A',False,'X’in 4 bağına H için 1 daha ekleyip 5 bulmuş; Y’nin değerlik elektronunu da bir fazla saymış')]
r=tek(secs,True)
S('0007','Güçlü Etkileşimler','lewis','Lewis yapısından değerlik elektronu ve grup','orta','şekilli','Lewis yapısında atomun değerlik elektronu = ortaklanan elektron sayısı + ortaklanmamış elektron sayısıdır; buradan A grubu bulunur.','Ortaklanmamış çifti saymayı unutmak ya da bağ çiftini iki atomun da elektronu olarak ikişer kez saymak.',
 'Elektron nokta (Lewis) yapısından atomların değerlik elektron sayısını ve grubunu bulur.','Lewis yapısı','H, X, Y atomlu molekül',
 [A('Dubleti ve oktedi kontrol et','H’de 2, X ve Y’de 8 elektron çevresi vardır.','H: 1 ortak çift · X: 1 + 3 = 4 ortak çift · Y: 3 ortak çift + 1 ortaklanmamış çift'),
  A('X’in değerlik elektronları','X’in bağ çiftleri 1 elektronunu H ile, 3 elektronunu Y ile ortaklaşa verir.','1 + 3 = 4 → 4A'),
  A('Y’nin değerlik elektronları','Y 3 elektronunu ortaklaşa kullanır, 2 elektron da ortaklanmamış çifttedir.','3 + 2 = 5 → 5A'),
  A('Sonuç','X 4A, Y 5A grubundadır.','Cevap: X: 4A, Y: 5A')],
 metin='Şekilde, H, X ve Y atomlarından oluşan bir molekülün elektron nokta (Lewis) yapısı verilmiştir. Molekülde bütün atomlar kararlı yapıya ulaşmıştır (H dublet, X ve Y oktet). Her nokta çifti bir ortak ya da ortaklanmamış elektron çiftini göstermektedir; X ve Y gerçek element sembolü değildir.\nBuna göre X ve Y atomları periyodik cetvelde hangi gruplardadır?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='X ve Y atomlarının A grubu numaraları.',
 ip=['Her atomun çevresindeki noktaları ayrı say: kaçı ortak çifte, kaçı ortaklanmamış çifte aittir, ve atomun kendi payına kaç elektron düşer?'],
 bilgi=[B('Lewis yapısı','Ortaklanan her çift, iki atomdan birer elektrondan oluşur. Atomun değerlik elektronu = bağ sayısı + 2 × ortaklanmamış çift sayısıdır. Örnek: H₂O’da O: 2 + 2 × 2 = 6 değerlik elektronu, 6A')],
 puf='Değerlik elektronu = bağ sayısı + 2 × ortaklanmamış çift; A grubu numarası buna eşittir.',sekil=SK7)

# 08 · polar / apolar molekül (dipol okları) · orta · öncüllü şekil
def dip(p,q,k=.3,yon=1,kisalt=.45):
    (x1,y1),(x2,y2)=p,q; L=math.hypot(x2-x1,y2-y1); ux,uy=(x2-x1)/L,(y2-y1)/L; px,py=-uy*yon,ux*yon
    a=(x1+ux*kisalt+px*k,y1+uy*kisalt+py*k); b=(x2-ux*kisalt+px*k,y2-uy*kisalt+py*k)
    return f'\\draw[vurgu,thick,{{Bar[width=2mm]}}-{{Stealth[length=2mm,width=1.8mm]}}] {pt(*a)} -- {pt(*b)};'
def atom_(x,y,s): return f'\\node[fill=white,inner sep=1.5pt] at {pt(x,y)} {{\\large {s}}};'
o=[]
# I: O=C=O
Oa,C_,Ob=(-1.5,0),(0,0),(1.5,0)
for sgn in (-.05,.05):
    o.append(f'\\draw {pt(Oa[0],sgn)} -- {pt(C_[0],sgn)} -- {pt(Ob[0],sgn)};')
o+= [atom_(*Oa,'O'),atom_(*C_,'C'),atom_(*Ob,'O'),dip(C_,Oa,yon=-1),dip(C_,Ob,yon=1)]
# II: bent H2O
ox=4.3
Ow,H1,H2=(ox,0),(ox-1.0,-.8),(ox+1.0,-.8)
o+= [f'\\draw {pt(*H1)} -- {pt(*Ow)} -- {pt(*H2)};',atom_(*Ow,'O'),atom_(*H1,'H'),atom_(*H2,'H'),dip(H1,Ow,k=.32,yon=-1,kisalt=.4),dip(H2,Ow,k=.32,yon=1,kisalt=.4)]
# III: HCl
hx=8.3
Ha,Cl_=(hx-.9,0),(hx+.9,0)
o+= [f'\\draw {pt(*Ha)} -- {pt(*Cl_)};',atom_(*Ha,'H'),atom_(*Cl_,'Cl'),dip(Ha,Cl_,k=.35,yon=-1)]
for i,x in enumerate((0,ox,hx)): o.append(f'\\node[font=\\bfseries] at {pt(x,-1.55)} {{{ROM[i]}}};')
o.append(f'\\node[font=\\footnotesize] at {pt(4.2,-2.2)} {{{{$\\mapsto$ : bağ elektronlarının çekildiği yön}}}};')
SK8=tk('\n'.join(o))
d={'I':(True,'iki C=O dipolü zıt yönlü ve eşit olduğundan birbirini götürür; molekül polar bağ içermesine karşın apolardır'),
   'II':(True,'bükülmüş yapıda iki O–H dipolü birbirini götürmez; molekül polardır'),
   'III':(False,'HCl iki atomludur ama farklı cins atomlar arasındaki bağ polardır; molekül de polardır')}
r=oc(d,siralist('Yalnız I','I ve II','I ve III','II ve III','I, II ve III')); assert r['dogru']=='I ve II'
S('0008','Güçlü Etkileşimler','polar','Bağ polarlığı ve molekül polarlığı','orta','öncüllü','Molekül polarlığı bağ dipollerinin simetriyle birbirini götürüp götürmediğine bağlıdır: CO₂ apolar, H₂O ve HCl polardır.','Polar bağ içeren her molekülü polar sanmak; iki atomlu molekülün hep apolar olduğunu düşünmek.',
 'Bağ dipollerinin yönüne bakarak molekülün polar ya da apolar olduğuna karar verir.','polar ve apolar molekül','CO₂, H₂O, HCl',
 [A('Şekli oku','Oklar elektronların çekildiği atomu gösterir; oklar zıt ve eşitse etkisi sıfırdır.','I: iki zıt ok · II: iki ok bükülmüş · III: tek ok'),
  A('I numaralı molekül','Simetrik doğrusal yapıda dipoller birbirini götürür.','polar bağ var, molekül apolar → I: doğru'),
  A('II ve III','Bükülmüş yapıda dipoller götürülmez; HCl’de tek dipol vardır.','II: polar → II: doğru · III: polar → III: yanlış'),
  A('Sonuç','Doğru olanlar toplanır.',etk(d)+' · Sonuç: I ve II')],
 metin='Şekilde, üç molekülün atomları ve her bağda elektronların hangi atoma doğru çekildiği oklarla gösterilmiştir. Öğretmen, molekül polarlığıyla ilgili aşağıdaki yargıları öğrencilere sunuyor.\nI. I numaralı molekül polar bağ içermesine karşın apolardır.\nII. II numaralı molekülde bağ dipolleri birbirini götürmediği için molekül polardır.\nIII. III numaralı molekül iki atomlu olduğundan apolardır.\nBuna göre hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',
 ip=['Her molekülde okları vektör gibi düşün: zıt yönlü ve eşit büyüklükteki oklar birbirini götürür mü?'],
 bilgi=[B('Polar ve apolar molekül','Farklı cins atomlar arası bağ polardır. Bağ dipolleri simetri nedeniyle birbirini götürüyorsa molekül apolar, götürmüyorsa polardır. Örnek: CH₄ apolar, NH₃ polardır')],
 puf='Molekül polarlığı için yalnız bağa değil, moleküldeki bağ dipollerinin toplamına bak.',sekil=SK8)

# 09 · iletkenlik deneyi · orta · öncüllü şekil
def duz(cx,tur,yanik):
    g=[f'\\draw[thick] {pt(cx-1,1.5)} -- {pt(cx-1,0)} -- {pt(cx+1,0)} -- {pt(cx+1,1.5)};']
    if tur=='kati':
        for i,(a,b) in enumerate([(-.8,0),(-.45,0),(.0,0),(.35,0),(-.6,.3),(-.05,.33),(.4,.3)]):
            g.append(f'\\draw[fill=gray!25] {pt(cx+a,b)} rectangle {pt(cx+a+.3,b+.3)};')
    else:
        g.append(f'\\fill[vurgu!15] {pt(cx-1,0)} rectangle {pt(cx+1,1.0)};')
        if tur=='iyon':
            for (a,b,s) in [(-.75,.2,'+'),(-.35,.55,'$-$'),(.05,.2,'+'),(.4,.6,'$-$'),(.75,.25,'+'),(-.6,.8,'$-$'),(.1,.85,'+')]: g.append(f'\\node[font=\\scriptsize] at {pt(cx+a,b)} {{{s}}};')
        else:
            for (a,b) in [(-.7,.2),(-.3,.6),(.1,.25),(.45,.65),(.75,.3),(-.55,.85),(.15,.88)]: g.append(f'\\draw[fill=white] {pt(cx+a,b)} circle (.1);')
    g.append(f'\\draw[line width=2pt] {pt(cx-.5,2.0)} -- {pt(cx-.5,.2)}; \\draw[line width=2pt] {pt(cx+.5,2.0)} -- {pt(cx+.5,.2)};')
    g.append(f'\\draw {pt(cx-.5,2.0)} -- {pt(cx-.5,2.42)}; \\draw {pt(cx-.7,2.42)} -- {pt(cx-.3,2.42)}; \\draw[line width=2pt] {pt(cx-.6,2.56)} -- {pt(cx-.4,2.56)}; \\draw {pt(cx-.5,2.56)} -- {pt(cx-.5,3.2)} -- {pt(cx-.28,3.2)};')
    g.append(f'\\draw[fill={"vurgu!35" if yanik else "white"}] {pt(cx,3.2)} circle (.28); \\draw {pt(cx-.2,3.0)} -- {pt(cx+.2,3.4)}; \\draw {pt(cx-.2,3.4)} -- {pt(cx+.2,3.0)};')
    g.append(f'\\draw {pt(cx+.28,3.2)} -- {pt(cx+.5,3.2)} -- {pt(cx+.5,2.0)};')
    if yanik:
        for a in range(0,360,45): g.append(f'\\draw[vurgu] {pt(cx+.38*math.cos(math.radians(a)),3.2+.38*math.sin(math.radians(a)))} -- {pt(cx+.56*math.cos(math.radians(a)),3.2+.56*math.sin(math.radians(a)))};')
    return '\n'.join(g)
SK9=tk('\n'.join([duz(0,'kati',False),duz(2.8,'iyon',True),duz(5.6,'seker',False)]+[f'\\node[font=\\bfseries] at {pt(x,-.35)} {{{n}}}; \\node[font=\\footnotesize] at {pt(x,-.8)} {{{t}}};' for x,n,t in [(0,'1','katı NaCl'),(2.8,'2','NaCl çözeltisi'),(5.6,'3','şeker çözeltisi')]]))
d={'I':(True,'katı NaCl’de iyonlar kafes noktalarında sabittir ve yük taşıyamaz'),
   'II':(False,'ampulü yakan serbest elektronlar değil, çözeltide serbest hareket eden Na⁺ ve Cl⁻ iyonlarıdır'),
   'III':(False,'şeker kovalent bir bileşiktir; suda moleküller hâlinde çözünür ve iyon oluşmadığı için ampul yanmaz')}
r=oc(d,siralist('Yalnız I','Yalnız II','I ve II','I ve III','II ve III')); assert r['dogru']=='Yalnız I'
S('0009','Güçlü Etkileşimler','iletken','İyonik ve kovalent bileşiklerin iletkenliği','orta','öncüllü','İyonik katıda iyonlar sabit olduğundan iletkenlik yoktur; çözeltide ya da sıvıda serbest iyonlar yük taşır; kovalent molekül çözeltisi iletken değildir.','Çözeltideki iletkenliği serbest elektronlara bağlamak; şekerin çözeltisinde iyon oluştuğunu sanmak.',
 'Katı, sulu çözelti ve molekül çözeltisinin iletkenliğini tanecik düzeyinde yorumlar.','iletkenlik deneyi','katı NaCl, NaCl çözeltisi, şeker çözeltisi',
 [A('Düzeneği oku','1. kapta ampul sönük, 2. kapta yanık, 3. kapta sönük.','1: katı NaCl · 2: NaCl çözeltisi · 3: şeker çözeltisi'),
  A('I. öncül','İyonlar katıda sabit konumdadır.','I: doğru'),
  A('II. öncül','Çözeltide yük taşıyan taneciklerin serbest iyonlar olduğu bilinmelidir.','elektron değil iyon taşır → II: yanlış'),
  A('III. öncül','Şeker kovalent bileşiktir ve çözeltisinde iyon yoktur.','III: yanlış'),
  A('Sonuç','Yalnız I doğrudur.',etk(d)+' · Sonuç: Yalnız I')],
 metin='Bir öğrenci, aynı pil ve ampulle kurduğu üç düzenekte katı NaCl, NaCl çözeltisi ve şeker çözeltisi ile deney yapıyor; ampullerin durumu şekilde gösterilmiştir. Öğrenci sonuçlarla ilgili şu yargıları yazıyor.\nI. 1 numaralı kapta iyonlar kafes noktalarında sabit olduğu için ampul yanmaz.\nII. 2 numaralı kapta ampulü, çözeltideki serbest elektronlar yakar.\nIII. 3 numaralı kapta şekerin iyonlarına ayrışmış olması ampulün yanmamasına neden olur.\nBuna göre hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',
 ip=['Ampulün yanması için çözeltide yük taşıyan, serbest hareket edebilen tanecikler gerektiğini düşün; bunların elektron mu iyon mu olduğuna dikkat et.'],
 bilgi=[B('Elektrik iletkenliği','İyonik bileşikler katı hâlde iletken değildir; sıvı hâlde ve sulu çözeltide serbest iyonlar yük taşır. Kovalent bileşiklerin çoğu çözeltide de iyon vermez. Örnek: erimiş KBr iletkendir')],
 puf='Çözeltide akımı taşıyan serbest iyonlardır; iyon yoksa iletkenlik de yoktur.',sekil=SK9)

# 10 · Lewis sembolleri ile iyonik bileşik · orta · şekil
def dots(n,x,y):
    sides={1:[(0,1,1)],2:[(0,1,2)],6:[(0,1,2),(1,0,2),(0,-1,2)],7:[(0,1,2),(1,0,2),(0,-1,2),(-1,0,1)]}[n]
    o=[]
    for dx,dy,c in sides:
        cx,cy=x+.42*dx,y+.42*dy
        if c==2: o.append(pair(cx,cy,-dy if dx==0 else 0,dx if dy==0 else 0))
        else: o.append(f'\\fill {pt(cx,cy)} circle (.04);')
    return '\n'.join(o)
LD=[('X',2),('Y',7),('Z',6)]
SK10=tk(head=HEAD.replace('font=\\small]','font=\\small,scale=1.5,every node/.style={scale=1.5}]'),g='\n'.join(f'\\node at {pt(i*2.2,0)} {{\\large {s}}};'+dots(n,i*2.2,0) for i,(s,n) in enumerate(LD)))
# X metal (2 değerlik e⁻), Y 7, Z 6 değerlik e⁻
vx,vy,vz=2,7,6; assert (vx,8-vy,8-vz)==(2,1,2)
fXY='XY₂'; fXZ='XZ'; assert ((8-vy)//math.gcd(vx,8-vy),vx//math.gcd(vx,8-vy))==(1,2) and ((8-vz)//math.gcd(vx,8-vz),vx//math.gcd(vx,8-vz))==(1,1)
secs=[('X ile Y arasında XY₂ formüllü iyonik bileşik oluşur.',True,''),
      ('X ile Z arasında X₂Z formüllü iyonik bileşik oluşur.',False,'X 2 elektron verir, Z 2 elektron alır; bileşik XZ’dir'),
      ('Y ile Z arasında iyonik bağlı bir bileşik oluşur.',False,'Y ve Z ikisi de ametal olduğu için aralarında kovalent bağ oluşur'),
      ('X ile Y arasında X₂Y formüllü bir bileşik oluşur.',False,'X 2 elektron verir, Y 1 alır; formül XY₂’dir'),
      ('Z ile Y arasında Z₂Y formüllü kovalent bir bileşik oluşur.',False,'Z 2, Y 1 elektron ortaklaşa kullanır; formül ZY₂’dir')]
r=tek(secs,True)
S('0010','Güçlü Etkileşimler','noktalewis','İyonik bağın oluşumu ve Lewis sembolleri','orta','şekilli','Lewis sembolündeki nokta sayısı değerlik elektronunu verir; metal elektron verip ametal alarak iyonik bileşik oluşturur, ametaller arasında ortaklaşa kullanım olur.','Elektron alışverişini ters yorumlamak; ametal–ametal bileşiği iyonik sanmak; indisleri ters yazmak.',
 'Lewis sembollerinden değerlik elektronlarını okuyup oluşacak bileşiğin türünü ve formülünü belirler.','Lewis sembolü ve bileşik türü','X, Y, Z elementleri',
 [A('Değerlik elektronlarını oku','Her nokta bir değerlik elektronudur.','X: 2 · Y: 7 · Z: 6'),
  A('Ne yapacaklarını bul','Metal elektron verir; ametal oktet için eksik kadar alır.','X: 2 e⁻ verir · Y: 1 e⁻ alır · Z: 2 e⁻ alır'),
  A('X–Y bileşiği','Verilen ve alınan elektron eşitlenir.','1 X × 2 = 2 · 2 Y × 1 = 2 → XY₂ (iyonik)'),
  A('Diğer şıklar','XZ olmalı; Y–Z ve Z–Y ametal–ametal kovalenttir.','XZ · Y–Z: kovalent · ZY₂: kovalent'),
  A('Sonuç','Yalnız XY₂ ifadesi doğrudur.','Cevap: X ile Y arasında XY₂ formüllü iyonik bileşik')],
 metin='Şekilde X, Y ve Z elementlerinin elektron nokta (Lewis) sembolleri verilmiştir. X bir metal, Y ve Z ise ametaldir; X, Y ve Z gerçek element sembolü değildir. Bu elementlerin atomları birbirleriyle kararlı bileşikler oluşturmak üzere bir araya getiriliyor.\nBuna göre aşağıdakilerden hangisi doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan ifade.',
 ip=['Her noktanın bir değerlik elektronu olduğunu hatırla; kimin vereceğini, kimin alacağını ve alınan–verilen elektron sayılarının eşitlenmesini düşün.'],
 bilgi=[B('Lewis sembolü','Elementin sembolü çevresine değerlik elektronları nokta olarak çizilir. Metaller elektron vererek, ametaller elektron alarak ya da ortaklaşa kullanarak oktet tamamlar. Örnek: 1 nokta (Li gibi) 1 elektron verir')],
 puf='İyonik bileşikte verilen elektron sayısı alınan elektron sayısına eşitlenir; formül buradan çıkar.',sekil=SK10)

# 11 · hidrürlerin kaynama noktası grafiği · zor · öncüllü grafik
A4=[(2,-162,'CH₄'),(3,-112,'SiH₄'),(4,-88,'GeH₄'),(5,-52,'SnH₄')]; A7=[(2,20,'HF'),(3,-85,'HCl'),(4,-67,'HBr'),(5,-35,'HI')]
g=['\\begin{axis}[width=7.4cm,height=5.4cm,xlabel={Merkez atomun periyodu},ylabel={Kaynama noktası ($^\\circ$C)},xmin=1.6,xmax=5.6,ymin=-190,ymax=50,xtick={2,3,4,5},ytick={-150,-100,-50,0,50},grid=major,grid style={gray!25},legend pos=south east,legend style={font=\\scriptsize,fill=none,draw=none}]']
g.append('\\addplot[thick,mark=*,mark size=2pt] coordinates {'+' '.join(f'({a},{b})' for a,b,_ in A4)+'};\\addlegendentry{4A hidrürleri}')
g.append('\\addplot[thick,vurgu,mark=square*,mark size=2.2pt] coordinates {'+' '.join(f'({a},{b})' for a,b,_ in A7)+'};\\addlegendentry{7A hidrürleri}')
for a,b,s in A4: g.append(f'\\node[font=\\scriptsize,below right=-1pt] at (axis cs:{a},{b}) {{\\ce{{{s.translate(str.maketrans('₀₁₂₃₄₅₆₇₈₉','0123456789'))}}}}};')
for a,b,s in A7: g.append(f'\\node[font=\\scriptsize,above=1pt] at (axis cs:{a},{b}) {{\\ce{{{s.translate(str.maketrans('₀₁₂₃₄₅₆₇₈₉','0123456789'))}}}}};')
g.append('\\end{axis}')
SK11=tikz_svg('\\begin{tikzpicture}[font=\\small]\n'+'\n'.join(g)+TAIL)
assert A4[3][1]>A4[0][1] and all(A4[i][1]<A4[i+1][1] for i in range(3)) and A7[0][1]>A7[1][1] and A7[1][1]<A7[2][1]<A7[3][1] and A7[1][1]>A4[1][1]
d={'I':(True,'4A hidrürleri apolardır; mol kütlesi arttıkça London kuvvetleri güçlenir ve kaynama noktası yükselir'),
   'II':(True,'HF’de H, F atomuna bağlıdır; hidrojen bağı HF’nin kaynama noktasını HCl’den çok yüksek yapar'),
   'III':(False,'HCl’nin SiH₄’ten yüksek olması hidrojen bağından değil, polar olmasından yani dipol–dipol etkileşiminden kaynaklanır')}
r=oc(d,STD); assert r['dogru']=='I ve II'
S('0011','Zayıf Etkileşimler','hidrur','Hidrürlerin kaynama noktası grafiği','zor','öncüllü','4A hidrürlerinde (apolar) kaynama noktası London kuvvetleriyle mol kütlesiyle artar; 7A’da HF hidrojen bağı nedeniyle bu eğilimin dışındadır; HCl’de dipol–dipol vardır.','HCl’de hidrojen bağı aramak; HF’nin yüksek kaynama noktasını mol kütlesine bağlamak.',
 'Grafikten kaynama noktası eğilimini okuyup zayıf etkileşim türleriyle ilişkilendirir.','hidrürlerin kaynama noktaları','4A ve 7A hidrürleri',
 [A('Grafiği oku','Her iki grupta kaynama noktası periyotla değişir; HF eğilimin dışında.','CH₄ → SnH₄: −162 → −52 · HF: 20, HCl: −85, HBr: −67, HI: −35'),
  A('I. öncül','4A hidrürleri apolardır; mol kütlesi arttıkça kaynama noktası artar.','London kuvvetleri → I: doğru'),
  A('II. öncül','HF molekülleri arasında hidrojen bağı vardır.','20 °C ≫ −85 °C → II: doğru'),
  A('III. öncül','HCl polar moleküldür; SiH₄ apolardır.','dipol–dipol, hidrojen bağı değil → III: yanlış'),
  A('Sonuç','Doğru olanlar toplanır.',etk(d)+' · Sonuç: I ve II')],
 metin='Şekildeki grafikte, 4A ve 7A gruplarındaki bazı elementlerin hidrürlerinin kaynama noktaları, merkez atomun periyoduna göre verilmiştir. Öğretmen, grafikten çıkarılan sonuçlarla ilgili aşağıdaki yargıları sunuyor.\nI. 4A hidrürlerinde kaynama noktasının artışı London kuvvetlerinin güçlenmesiyle açıklanır.\nII. HF’nin kaynama noktasının HCl’den yüksek olması, HF moleküllerinin hidrojen bağı yapmasındandır.\nIII. HCl’nin SiH₄’ten yüksek kaynama noktasına sahip olması hidrojen bağı nedeniyledir.\nBuna göre hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',
 ip=['Hangi hidrürlerin polar, hangilerinin apolar olduğunu ve hidrojenin F, O ya da N’ye bağlı olup olmadığını düşün.'],
 bilgi=[B('Zayıf etkileşimler','Apolar moleküller arasında London kuvvetleri, polar moleküller arasında dipol–dipol etkileşimi vardır. H atomu F, O ya da N’ye bağlıysa hidrojen bağı oluşur ve kaynama noktası olağan eğilimin üstüne çıkar. Örnek: H₂O')],
 puf='Mol kütleleri yakınsa önce hidrojen bağına, sonra polarlığa bak; apolarlarda mol kütlesi belirler.',sekil=SK11)

# 12 · hidrojen bağı yapabilen moleküller (açık formül) · orta · şekil
def mol_(at,bg,ox):
    o=[]
    for a,b in bg:
        (x1,y1,_),(x2,y2,_)=at[a],at[b]; L=math.hypot(x2-x1,y2-y1); ux,uy=(x2-x1)/L,(y2-y1)/L; s=.24
        o.append(f'\\draw {pt(ox+x1+ux*s,y1+uy*s)} -- {pt(ox+x2-ux*s,y2-uy*s)};')
    for a,(x,y,s) in at.items(): o.append(f'\\node at {pt(ox+x,y)} {{{s}}};')
    return '\n'.join(o)
N3={'N':(0,0,'N'),'a':(-.9,-.25,'H'),'b':(.9,-.25,'H'),'c':(0,-.9,'H')}
ET={'C1':(-.8,0,'C'),'O':(.8,0,'O'),'h1':(-.8,.85,'H'),'h2':(-.8,-.85,'H'),'h3':(-1.65,0,'H'),'h4':(.8,-.85,'H')}
ME={'C1':(-.8,0,'C'),'O':(.8,0,'O'),'C2':(2.4,0,'C'),'h1':(-.8,.85,'H'),'h2':(-.8,-.85,'H'),'h3':(-1.65,0,'H'),'g1':(2.4,.85,'H'),'g2':(2.4,-.85,'H'),'g3':(3.25,0,'H')}
# not: ET = CH3-OH, ME = CH3-O-CH3 (aynı çizim biçimi)
mols={'I':(N3,[('N','a'),('N','b'),('N','c')],'NH₃',True),
      'II':(ME,[('C1','O'),('O','C2'),('C1','h1'),('C1','h2'),('C1','h3'),('C2','g1'),('C2','g2'),('C2','g3')],'CH₃OCH₃',False),
      'III':(ET,[('C1','O'),('C1','h1'),('C1','h2'),('C1','h3'),('O','h4')],'CH₃OH',True)}
def hbag(at,bg):
    """H atomu F/O/N'ye doğrudan bağlı mı"""
    for a,b in bg:
        s=(at[a][2],at[b][2])
        if 'H' in s and (set(s)-{'H'})&{'N','O','F'}: return True
    return False
for k,(at,bg,f_,y_) in mols.items(): assert hbag(at,bg)==y_,k
oxs={'I':1.0,'II':5.2,'III':11.0}
SK12=tk('\\path (-.3,-2.2) rectangle (13.3,1.4);\n'+'\n'.join(mol_(at,bg,oxs[k])+f'\\node[font=\\bfseries] at {pt(oxs[k]+(1.2 if k=="II" else .0),-1.7)} {{{k}}};' for k,(at,bg,_,_) in mols.items()))
S('0012','Zayıf Etkileşimler','hbagi','Hidrojen bağı yapabilen moleküller','orta','şekilli','Hidrojen bağı için H atomunun doğrudan F, O ya da N atomuna bağlı olması gerekir; H’nin yalnız C’ye bağlı olması yetmez.','CH₃OCH₃’ta oksijen olduğu için hidrojen bağı sanmak.',
 'Açık formülden hidrojen atomunun F, O, N’ye doğrudan bağlı olup olmadığına bakarak hidrojen bağını belirler.','hidrojen bağı koşulu','NH₃, CH₃OCH₃, CH₃OH',
 [A('Şekli oku','Her molekülde H’lerin hangi atomlara bağlı olduğuna bak.','I: N–H · II: C–H · III: C–H ve O–H'),
  A('Koşulu uygula','H, F–O–N atomlarından birine doğrudan bağlı olmalı.','I: N–H var · II: yalnız C–H · III: O–H var'),
  A('Sonuç','I ve III’te hidrojen bağı vardır; II’de yoktur.','Cevap: I ve III')],
 metin='Şekilde üç molekülün açık formülleri verilmiştir. Bu üç maddenin de saf sıvı hâlde bulunduğu bir deneyde, moleküller arasındaki etkileşimler inceleniyor. Öğrenci, hangi sıvıların molekülleri arasında hidrojen bağı bulunduğunu belirlemeye çalışıyor.\nBuna göre hangi maddelerin saf sıvısında moleküller arası hidrojen bağı bulunur?',
 dogru='I ve III',yan=[('Yalnız I','III’teki O–H bağını görmemiş; hidroksit hidrojeni de hidrojen bağı yapar.','dikkat'),('Yalnız II','II’de oksijen olduğu için hidrojen bağı sanmış; oksijene bağlı hidrojen yoktur.','bilgi'),('Yalnız III','NH₃’teki N–H bağını atlamış.','dikkat'),('I, II ve III','II’yi de saymış; H atomları yalnız karbona bağlıdır.','bilgi')],
 sira=['Yalnız I','Yalnız II','Yalnız III','I ve III','I, II ve III'],istenen='Moleküller arası hidrojen bağı bulunan maddeler.',
 ip=['Her molekülde H atomunun kime bağlı olduğuna bak: F, O ya da N’ye doğrudan bağlı mı?'],
 bilgi=[B('Hidrojen bağı','H atomu F, O ya da N atomuna bağlıysa, bu H ile başka bir molekülün F, O ya da N atomu arasında hidrojen bağı kurulur. Örnek: H₂O ve HF’de vardır, CH₄’te yoktur')],
 puf='Hidrojen bağı için H’nin doğrudan F, O ya da N’ye bağlı olduğuna bak; yalnız oksijenin molekülde bulunması yetmez.',sekil=SK12)

# 13 · soygazların kaynama noktaları · orta · düz
sg=[('He',2,-269),('Ne',10,-246),('Ar',18,-186),('Kr',36,-153)]
assert all(sg[i][2]<sg[i+1][2] and sg[i][1]<sg[i+1][1] for i in range(3))
secs=[('Atom numarası arttıkça dipol–dipol etkileşimi güçlendiği için kaynama noktası yükselir.',False,'soygaz atomları apolar ve tek atomludur, dipol–dipol etkileşimi oluşturmazlar'),
      ('Atom numarası ve elektron sayısı arttıkça London kuvvetleri güçlenir, kaynama noktası yükselir.',True,''),
      ('Ne’nin kaynama noktasının He’dan yüksek olması, Ne atomları arasındaki hidrojen bağından kaynaklanır.',False,'Ne atomlarında hidrojen yoktur; neden London kuvvetleridir'),
      ('Kr’nin kaynama noktasının yüksek olması, atomları arasında iyonik bağ bulunmasındandır.',False,'soygaz atomları bağ yapmaz; aralarında yalnız London kuvvetleri vardır'),
      ('Soygaz atomları arasında hiçbir etkileşim olmadığından kaynama noktaları tesadüfidir.',False,'apolar atomlar arasında da London kuvvetleri vardır ve kaynama noktasını belirler')]
r=tek(secs,True)
S('0013','Zayıf Etkileşimler','soygaz','Soygazlarda London kuvvetleri','kolay','düz','Apolar ve tek atomlu soygazlarda yalnız London kuvvetleri vardır; elektron sayısı arttıkça güçlenir ve kaynama noktası artar.','Soygazlar arasında hiç etkileşim olmadığını düşünmek; London kuvvetini dipol–dipolle karıştırmak.',
 'Soygazların kaynama noktası verilerini London kuvvetleriyle açıklar.','London kuvvetleri','He, Ne, Ar, Kr kaynama noktaları',
 [A('Verileri sırala','Atom numarası arttıkça kaynama noktası da yükseliyor.','He (2): −269 · Ne (10): −246 · Ar (18): −186 · Kr (36): −153'),
  A('Etkileşimi belirle','Soygazlar apolar ve tek atomludur; yalnız London kuvvetleri etkindir.','London kuvvetleri'),
  A('Şıkları ele','Dipol–dipol, hidrojen bağı ve iyonik bağ soygaz atomlarında yoktur.','dipol–dipol, hidrojen bağı, iyonik bağ ve “etkileşim yok” ifadeleri: yanlış'),
  A('Sonuç','Elektron sayısı arttıkça London kuvvetleri güçlenir.','Cevap: London kuvvetleri güçlenir, kaynama noktası yükselir')],
 metin='Bir öğrenci, 1 atm basınçta soygazların kaynama noktalarını kaynaklardan derleyip şu şekilde yazıyor: He (atom numarası 2) −269 °C, Ne (10) −246 °C, Ar (18) −186 °C, Kr (36) −153 °C. Öğrenci, bu verilerden yola çıkarak soygazlar arasındaki etkileşimin türünü ve kaynama noktasındaki eğilimin nedenini yorumlamak istiyor.\nBuna göre hangi yorum doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Veriler için doğru yorum.',
 ip=['Soygaz atomlarının polar mı apolar mı olduğunu ve bu durumda hangi etkileşimin kaldığını düşün.'],
 bilgi=[B('London kuvvetleri','Her tür taneciğin arasında bulunan anlık dipollerden doğan zayıf etkileşimdir. Elektron sayısı (mol kütlesi) arttıkça güçlenir. Örnek: Cl₂’nin kaynama noktası F₂’den yüksektir')],
 puf='Apolar maddelerde kaynama noktası mol kütlesiyle birlikte artar; sebep London kuvvetleridir.')

# 14 · dipol–dipol / London · zor · öncüllü tablo
tb=[('HBr',81,-67),('Kr',84,-153),('HI',128,-35),('Xe',131,-108)]
assert tb[0][1]<tb[1][1] and tb[0][2]>tb[1][2] and tb[2][2]>tb[3][2] and tb[3][2]>tb[1][2]
SK14=tablo_svg(['Madde','Mol kütlesi (g/mol)','Kaynama noktası (°C)'],[[a,str(b),str(c).replace('-','−')] for a,b,c in tb])
d={'I':(True,'HBr ile Kr’nin mol kütleleri yaklaşık eşittir; HBr polar olduğundan dipol–dipol etkileşimi de vardır ve kaynama noktası daha yüksektir'),
   'II':(False,'HI’de H, I atomuna bağlıdır; hidrojen bağı yoktur, baskın etkileşim dipol–dipol ve London kuvvetleridir'),
   'III':(True,'Xe ile Kr apolar tek atomlu maddelerdir; mol kütlesi büyük olan Xe’de London kuvvetleri daha güçlüdür')}
r=oc(d,siralist('Yalnız I','Yalnız II','I ve II','I ve III','II ve III')); assert r['dogru']=='I ve III'
S('0014','Zayıf Etkileşimler','dipollondon','Mol kütlesi eşitken polarlık etkisi','zor','tablo','Mol kütlesi yaklaşık eşit olan polar ve apolar maddelerde polar olanın kaynama noktası yüksektir; apolar maddelerde mol kütlesi belirleyicidir.','HI’de hidrojen bağı aramak; mol kütlesinin her durumda tek belirleyici olduğunu sanmak.',
 'Tablodaki mol kütlesi ve kaynama noktası verilerini dipol–dipol ve London kuvvetleriyle yorumlar.','polar–apolar kaynama noktası karşılaştırması','HBr, Kr, HI, Xe',
 [A('Tabloyu oku','Mol kütleleri ikişer ikişer birbirine yakın.','HBr 81 ≈ Kr 84 · HI 128 ≈ Xe 131'),
  A('I. öncül','HBr polardır; Kr apolar tek atomludur.','−67 °C > −153 °C → dipol–dipol katkısı → I: doğru'),
  A('II. öncül','H, I atomuna bağlıdır.','hidrojen bağı yok → II: yanlış'),
  A('III. öncül','Xe ve Kr apolar; Xe’nin mol kütlesi büyük.','−108 °C > −153 °C → London kuvveti → III: doğru'),
  A('Sonuç','Doğru olanlar toplanır.',etk(d)+' · Sonuç: I ve III')],
 metin='Tabloda, 1 atm basınçta bazı maddelerin mol kütlesi ve kaynama noktası verilmiştir. Öğretmen, mol kütlesi birbirine yakın olan maddeleri karşılaştırarak etkileşimleri yorumlamalarını istiyor.\nI. HBr’nin kaynama noktasının Kr’den yüksek olması, HBr’deki dipol–dipol etkileşiminden kaynaklanır.\nII. HI’nin kaynama noktası, moleküller arasındaki hidrojen bağı nedeniyle yüksektir.\nIII. Xe’nin kaynama noktasının Kr’den yüksek olması, London kuvvetlerinin daha güçlü olmasıyla açıklanabilir.\nBuna göre hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',
 ip=['Her madde çiftinde önce mol kütlelerini, sonra maddelerin polar ya da apolar olup olmadığını karşılaştır.'],
 bilgi=[B('Polar ve apolar maddeler','Mol kütlesi yaklaşık eşit olan maddelerde polar olanın kaynama noktası daha yüksektir; polar moleküllerde dipol–dipol de London kuvvetlerine eklenir. Apolar maddelerde mol kütlesi büyüdükçe kaynama noktası yükselir. Örnek: Ar ve HCl')],
 puf='Mol kütleleri yakınsa polarlığa bak; polarlık aynıysa mol kütlesine bak.',sekil=SK14)

# 15 · bağ kırılması / oluşması enerji diyagramı (nitel) · kolay · grafik
Er,Ea,Eu=250,600,100
assert Eu<Er<Ea
sc=.0085
y=lambda e: e*sc
g=[f'\\draw[{ARR}] (0,0) -- (0,5.3); \\draw[{ARR}] (0,0) -- (7.3,0);',
   '\\node[rotate=90] at (-.5,2.65) {Enerji}; \\node at (3.7,-.5) {Tepkime ilerlemesi};']
for e in (Eu,Er,Ea): g.append(f'\\draw[gray,dashed] (0,{y(e)}) -- (.8,{y(e)});')
g.append(f'\\draw[very thick] (.8,{y(Er)}) -- (2.0,{y(Er)}); \\draw[very thick] (3.0,{y(Ea)}) -- (4.2,{y(Ea)}); \\draw[very thick] (5.2,{y(Eu)}) -- (6.4,{y(Eu)});')
g.append(f'\\node[above] at (1.4,{y(Er)+.05}) {{X$_2$ + Y$_2$}}; \\node[above] at (3.6,{y(Ea)+.05}) {{2X + 2Y}}; \\node[above] at (5.8,{y(Eu)+.05}) {{2XY}};')
g.append(f'\\draw[vurgu,thick,{ARR}] (2.05,{y(Er)}) -- (2.95,{y(Ea)}) node[midway,left,font=\\footnotesize] {{1. basamak}}; \\draw[vurgu,thick,{ARR}] (4.25,{y(Ea)}) -- (5.15,{y(Eu)}) node[midway,right,font=\\footnotesize] {{2. basamak}};')
SK15=tk('\n'.join(g))
secs=[('Bağların kırılması enerji açığa çıkarır, bağların oluşması enerji ister.',False,'bağ kırmak için enerji harcanır; bağ oluşurken enerji verilir'),
      ('Bağlar kırılırken enerji alınır, bağlar oluşurken enerji açığa çıkar; ürünlerin enerjisi düşük olduğundan tepkimede net olarak enerji açığa çıkar.',True,''),
      ('Bağ oluşurken açığa çıkan enerji, bağ kırılırken alınan enerjiden küçük olduğu için tepkime enerji verir.',False,'ürünlerin enerjisi düşük olduğuna göre oluşumda açığa çıkan enerji, kırılmada alınandan büyüktür'),
      ('Atomların enerjisi reaktiflerden düşüktür; bu yüzden bağlar kırılırken enerji açığa çıkar.',False,'atomların enerjisi reaktiflerden yüksektir; bağ kırılırken enerji alınır'),
      ('Tepkime boyunca enerji ne alınır ne verilir; reaktif ve ürün enerjisi aynı kalır.',False,'reaktif ve ürün enerjileri farklıdır; kırılma ve oluşumda enerji alışverişi olur')]
r=tek(secs,True)
S('0015','Fiziksel ve Kimyasal Değişimler','enerji','Bağ kırılması ve oluşması sırasındaki enerji','kolay','grafik','Bağ kırılması enerji gerektirir, bağ oluşması enerji açığa çıkarır; ürün enerjisi reaktiften düşükse net olarak enerji açığa çıkar.','Bağ oluşumunun da enerji gerektirdiğini sanmak.',
 'Enerji diyagramından bağ kırılması ve oluşmasındaki enerji alışverişini nitel olarak yorumlar.','enerji diyagramı','reaktif, atom, ürün düzeyleri',
 [A('Diyagramı oku','Atomlar düzeyi en yüksek, ürünler en düşüktür.','reaktifler < atomlar; ürünler < reaktifler'),
  A('1. basamak','Reaktiften atomlara çıkarken bağlar kırılır; enerji yükselir.','enerji alınır'),
  A('2. basamak','Atomlardan ürüne inerken bağlar oluşur; enerji düşer.','enerji açığa çıkar'),
  A('Sonuç','Ürün enerjisi reaktiften düşüktür; toplam olarak enerji açığa çıkar.','Cevap: kırılmada enerji alınır, oluşumda verilir; net enerji açığa çıkar')],
 metin='Gaz hâldeki X₂ ve Y₂ moleküllerinden 2XY molekülünün oluştuğu tepkimenin enerji diyagramı şekilde gösterilmiştir. Tepkime iki basamakta ilerlemektedir: önce reaktiflerdeki bütün bağlar kırılarak atomlar oluşur, sonra atomlardan yeni bağlar kurularak ürünler oluşur.\nBuna göre bu tepkimeyle ilgili aşağıdakilerden hangisi doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Enerji alışverişiyle ilgili doğru ifade.',
 ip=['Diyagramda enerjinin her basamakta yükseldiğini mi alçaldığını mı izleyip bunu bağın kırılması ya da oluşmasıyla eşleştir.'],
 bilgi=[B('Bağ kırılması ve oluşması','Bağ kırılırken enerji alınır, bağ oluşurken enerji açığa çıkar. Örnek: su elektrolizinde O–H bağlarını kırmak için enerji verilmesi gerekir')],
 puf='Kırılma = enerji alma, oluşum = enerji verme; diyagramda yükselen basamak kırılmadır.',sekil=SK15)

# 16 · fiziksel değişim ayırt etme · kolay · düz · olumsuz
secs=[('Kuru buzun (katı CO₂) oda koşullarında gaza dönüşmesi',True,'süblimleşme hâl değişimidir, fiziksel değişimdir'),
      ('Alkolün açık kapta buharlaşması',True,'buharlaşma hâl değişimidir, fiziksel değişimdir'),
      ('Sofra tuzunun suda çözünerek iyonlarına ayrılması',True,'çözünme fiziksel değişimdir; yeni madde oluşmaz'),
      ('Bakır telin çekiçle düzleştirilmesi',True,'şekil değişimidir, fiziksel değişimdir'),
      ('Sütün bozularak ekşimesi',False,'yeni maddeler (laktik asit gibi) oluşur, kimyasal değişimdir')]
r=tek(secs,False)
S('0016','Fiziksel ve Kimyasal Değişimler','sinif','Fiziksel ve kimyasal değişim sınıflaması','kolay','düz','Yeni madde oluşmuyorsa değişim fizikseldir; çözünme, hâl değişimi, şekil değişimi fiziksel değişimlerdir.','Çözünmeyi ve süblimleşmeyi kimyasal değişim sanmak.',
 'Günlük olayları fiziksel ve kimyasal değişim olarak sınıflar.','değişim sınıflaması','süblimleşme, çözünme, ekşime',
 [A('Ölçütü hatırla','Fiziksel değişimde yeni madde oluşmaz; kimyasal değişimde oluşur.','yeni madde → kimyasal'),
  A('Şıkları incele','Süblimleşme, buharlaşma, çözünme ve şekil değişimi maddenin kimliğini değiştirmez.','süblimleşme, buharlaşma, çözünme, çekiçleme: fiziksel'),
  A('Ekşimeyi incele','Sütteki şekerin bakterilerce asite dönüşmesiyle yeni madde oluşur.','süt ekşimesi: kimyasal'),
  A('Sonuç','Fiziksel olmayan olay bulunur.','Cevap: sütün ekşimesi')],
 metin='Bir aile, tatile çıkmadan önce evde gözlemledikleri bazı olayları fiziksel ve kimyasal değişim olarak sınıflandırmaya çalışıyor. Çocukları, her olayda maddenin kimliğinin değişip değişmediğini tartışarak olayları gruplandırıyor ve fiziksel değişim olmayan olayı bulmaya çalışıyor.\nBuna göre aşağıdakilerden hangisi fiziksel değişim değildir?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Fiziksel değişim olmayan olay.',
 ip=['Her olayda sonunda başka bir maddenin oluşup oluşmadığına bak.'],
 bilgi=[B('Fiziksel ve kimyasal değişim','Fiziksel değişimde madde türü değişmez (hâl değişimi, çözünme, şekil değişimi); kimyasal değişimde yeni maddeler oluşur (yanma, paslanma, bozulma). Örnek: buzun erimesi fiziksel, ağacın yanması kimyasal değişimdir')],
 puf='Yeni madde oluşup oluşmadığına bak; çözünme ve hâl değişimleri fizikseldir.')

# 17 · madde özelliklerinden bağ türü · orta · hikâyeli
secs=[('iyonik – metalik – kovalent',False,'iletken ve dövülebilen alüminyum folyo metalik bağlıdır; sofra tuzu iyonik bağlıdır'),
      ('metalik – kovalent – iyonik',False,'katıyken yalıtkan olup çözeltisi iletken olan tuz iyonik, şeker ise kovalent bağlıdır'),
      ('kovalent – iyonik – metalik',False,'iletken ve dövülebilir folyo kovalent değil metalik bağlıdır; şeker metal değildir'),
      ('metalik – iyonik – iyonik',False,'çözeltisi de iletmeyen şeker iyonik değil kovalent bağlı bir moleküldür'),
      ('metalik – iyonik – kovalent',True,'')]
r=tek(secs,True)
S('0017','Güçlü Etkileşimler','bagturu','Madde özelliklerinden bağ türü','orta','hikâyeli','Katı hâlde iletken ve dövülebilir madde metalik bağlı, katıda yalıtkan çözeltide iletken madde iyonik, her iki hâlde yalıtkan molekül kovalent bağlıdır.','Her ametalli bileşiği iyonik sanmak; çözeltideki iletkenliği metalik bağa bağlamak.',
 'Katı hâl ve çözelti iletkenliği ile dövülebilirlik gözlemlerinden baskın bağ türünü belirler.','bağ türü ve özellikler','alüminyum folyo, sofra tuzu, şeker',
 [A('Folyoyu değerlendir','Katı hâlde iletken ve dövülebilir.','metalik bağ'),
  A('Tuzu değerlendir','Katıda iyonlar sabittir; çözeltide serbest iyonlar yük taşır.','iyonik bağ'),
  A('Şekeri değerlendir','Çözeltide de iletmediği için iyon oluşmaz; moleküller kovalent bağlıdır.','kovalent bağ'),
  A('Sonuç','Üç madde sırasıyla eşleştirilir.','Cevap: metalik – iyonik – kovalent')],
 metin='Bir lise laboratuvarında alüminyum folyo, sofra tuzu (NaCl) ve toz şeker ile deney yapılıyor. Alüminyum folyo katı hâlde elektriği iletiyor ve çekiçle dövülebiliyor. Sofra tuzu katıyken iletmiyor ama suda çözününce çözeltisi iletiyor. Şeker ise hem katıyken hem suda çözününce elektriği iletmiyor.\nBuna göre bu üç maddedeki baskın bağ türleri sırasıyla (folyo, tuz, şeker) aşağıdakilerden hangisidir?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Üç maddenin baskın bağ türleri.',
 ip=['Her gözlemin (iletkenlik, dövülebilirlik, çözünce iletme) hangi bağ türünün özelliği olduğunu ayrı ayrı düşün.'],
 bilgi=[B('Bağ türü ve özellik','Metalik bağlı katılar iletken ve dövülebilirdir; iyonik katılar katıda yalıtkan, çözeltide ve sıvıda iletkendir; kovalent moleküllü maddeler çoğunlukla yalıtkandır. Örnek: bakır tel iletkendir')],
 puf='Katıda iletken = metalik; yalnız çözeltide/sıvıda iletken = iyonik; hiçbirinde iletmeyen molekül = kovalent.')

# 18 · iyon elektron sayısı ve bileşikte toplam proton · orta
ZX,ZY=12,7  # Ne ile aynı elektron sayısı
assert ZX-2==10 and ZY+3==10
fx,fy=3,2; assert fx*2==fy*3
prot=fx*ZX+fy*ZY; assert prot==50
e=[ZX+ZY, 2*ZX+2*ZY, 2*ZX+3*ZY, 3*ZX+3*ZY]; assert e==[19,38,45,57]
S('0018','Güçlü Etkileşimler','iyonproton','Eş elektronlu iyonlardan bileşik','orta','düz','İyonun elektron sayısından atom numarası bulunur; yükler eşitlenerek formül yazılır ve formül birimindeki proton sayısı toplanır.','Katyon yerine anyonun elektron sayısını yanlış yorumlamak; çaprazlamayı ters yapmak.',
 'Eş elektronlu iyonlardan atom numaralarını bulup oluşan bileşikte toplam proton sayısını hesaplar.','iyonik bileşik ve proton sayısı','X²⁺ ve Y³⁻, 10 elektron',
 [A('Atom numaralarını bul','Katyon elektron vermiş, anyon elektron almıştır.','X: 10 + 2 = 12 · Y: 10 − 3 = 7'),
  A('Formülü bul','Yükler çaprazlanır.','X²⁺ ve Y³⁻ → X₃Y₂ (3 × 2 = 2 × 3)'),
  A('Protonları topla','Bir formül biriminde 3 X ve 2 Y atomu vardır.','3 × 12 + 2 × 7 = 36 + 14'),
  A('Sonuç','Toplam proton sayısı bulunur.','= 50')],
 metin='Bir laboratuvarda X²⁺ ve Y³⁻ iyonlarının elektron sayılarının birbirine eşit olduğu ve her birinin 10 elektron içerdiği belirleniyor. X ve Y atomlarının bir araya gelmesiyle kararlı, iyonik yapılı bir bileşik oluşuyor.\nBuna göre bu bileşiğin bir formül biriminde toplam kaç proton bulunur?',
 dogru=prot,yan=[(e[0],'Bileşiğin formülünü XY alıp 12 + 7 hesaplamış.','bilgi'),(e[1],'2+ ve 3− yüklerini sadeleştirip X₂Y₂ yazmış: 2 × 12 + 2 × 7 = 38.','islem'),(e[2],'Çaprazlamayı ters yapıp X₂Y₃ bulmuş: 2 × 12 + 3 × 7.','islem'),(e[3],'Yükleri iyon sayısı gibi alıp X₃Y₃ yazmış: 3 × 12 + 3 × 7.','islem')],
 istenen='Bir formül birimindeki toplam proton sayısı.',
 ip=['Her iyonun atom numarasını elektron ve yük sayısından bul; sonra yükleri eşitleyen iyon sayılarını belirle.'],
 bilgi=[B('İyon elektron sayısı','Katyonun elektron sayısı proton sayısından yük kadar az, anyonunki yük kadar fazladır. Örnek: 11 protonlu +1 yüklü iyonun 10 elektronu vardır'),B('Formül','Toplam pozitif yük toplam negatif yüke eşit olacak şekilde iyon sayıları bulunur. Örnek: Al³⁺ ve O²⁻ → Al₂O₃')],
 puf='Katyonun protonu elektron + yük, anyonun protonu elektron − yük kadardır; formül birimindeki her atomun protonunu topla.')

# 19 · metalik bağ ve erime noktası · orta · öncüllü tablo
mt=[('Na',1,98),('Mg',2,650),('Al',3,660)]
assert all(mt[i][1]<mt[i+1][1] and mt[i][2]<mt[i+1][2] for i in range(2))
d={'I':(False,'değerlik elektronu arttıkça serbest elektron denizi yoğunlaşır ve metalik bağ zayıflamaz, güçlenir'),
   'II':(True,'Na’nın değerlik elektronu en az olduğundan metalik bağı en zayıftır ve erime noktası en düşüktür'),
   'III':(True,'Al’nin değerlik elektronu en çoktur; metalik bağı en güçlü olduğu için erime noktası en yüksektir')}
r=oc(d,siralist('Yalnız I','Yalnız II','Yalnız III','I ve II','II ve III')); assert r['dogru']=='II ve III'
S('0019','Güçlü Etkileşimler','metalikgucu','Metalik bağ gücü ve erime noktası','orta','öncüllü','Metalde değerlik elektronu sayısı arttıkça elektron denizi yoğunlaşır, metalik bağ güçlenir ve erime noktası genellikle yükselir.','Al’nin bileşiğindeki bağı iyonik sanmak; değerlik elektronu artınca bağın zayıfladığını düşünmek.',
 'Verilerden metalik bağ gücünü ve erime noktası ilişkisini yorumlar.','metalik bağ gücü','Na, Mg, Al',
 [A('Verileri oku','Değerlik elektronu 1, 2, 3 arttıkça erime noktası da artıyor.','98 °C < 650 °C < 660 °C'),
  A('I. öncül','Değerlik elektronu arttıkça bağ güçleniyor.','I: yanlış'),
  A('II. öncül','Na, en az elektron veren metaldir.','II: doğru'),
  A('III. öncül','Al’nin erime noktası en yüksektir ve değerlik elektronu en fazladır.','III: doğru'),
  A('Sonuç','Doğru olanlar toplanır.',etk(d)+' · Sonuç: II ve III')],
 metin='Aynı periyotta bulunan üç metalin değerlik elektron sayıları ve erime noktaları şöyledir: Na 1 elektron, 98 °C; Mg 2 elektron, 650 °C; Al 3 elektron, 660 °C. Öğretmen, bu verileri metalik bağ modeliyle yorumlamalarını istiyor.\nI. Değerlik elektron sayısı arttıkça metalik bağ zayıflar.\nII. Na, bu üç metal içinde en zayıf metalik bağa sahiptir.\nIII. Al’nin erime noktasının en yüksek olması, daha fazla serbest elektrondan kaynaklanan güçlü metalik bağla açıklanabilir.\nBuna göre hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',
 ip=['Elektron denizindeki elektron sayısı arttıkça katyonlarla elektron denizi arasındaki çekimin nasıl değiştiğini düşün.'],
 bilgi=[B('Metalik bağ gücü','Metal atomunun ortak elektron denizine verdiği değerlik elektronu sayısı arttıkça katyonları tutan çekim güçlenir ve erime noktası yükselir. Örnek: 2 değerlik elektronlu metal, 1 değerlik elektronlu aynı periyot metalinden daha yüksek erime noktasına sahiptir')],
 puf='Metalde serbest elektron çoğaldıkça metalik bağ güçlenir; erime noktası yükselir.')

# 20 · Lewis yapıları (zor) · öncüllü şekil
at_a={'X1':(0,0,'X'),'X2':(1.5,0,'X')}; bg_a=[('X1','X2',3)]; ln_a=[('X1',180),('X2',0)]
at_b={'Y':(0,0,'Y'),'H1':(-.95,-.62,'H'),'H2':(.95,-.62,'H')}; bg_b=[('Y','H1',1),('Y','H2',1)]; ln_b=[('Y',55),('Y',125)]
at_c={'Y1':(-1.6,0,'Y'),'Z':(0,0,'Z'),'Y2':(1.6,0,'Y')}; bg_c=[('Y1','Z',2),('Z','Y2',2)]; ln_c=[('Y1',130),('Y1',230),('Y2',50),('Y2',310)]
va=valence(at_a,bg_a,ln_a); vb=valence(at_b,bg_b,ln_b); vc=valence(at_c,bg_c,ln_c)
assert va['X1']==5 and vb['Y']==6 and vc['Z']==4 and vc['Y1']==6
lonY=sum(1 for a,_ in ln_b if a=='Y'); assert lonY==2
sa=lewis(at_a,bg_a,ln_a,1.0,0)+lewis(at_b,bg_b,ln_b,4.7,0)+lewis(at_c,bg_c,ln_c,8.7,0)
sa+='\n'.join(f'\\node[font=\\bfseries] at {pt(x,-1.6)} {{{n}}};' for x,n in [(1.75,'I'),(4.7,'II'),(8.7,'III')])
SK20=tk(sa,HEAD.replace('font=\\small]','font=\\small,scale=1.25,every node/.style={scale=1.25}]'))
d={'I':(True,'X₂’de her X atomu 3 ortak elektronla birlikte 1 ortaklanmamış çift taşır: 3 + 2 = 5 değerlik elektronu'),
   'II':(False,'H₂Y’de Y atomunun iki ortaklanmamış elektron çifti vardır, bir değil'),
   'III':(True,'ZY₂’de Z’nin dört ortak elektronu vardır, ortaklanmamış çifti yoktur; bu da 4A grubunu gösterir')}
r=oc(d,siralist('Yalnız I','Yalnız II','I ve II','I ve III','II ve III')); assert r['dogru']=='I ve III'
S('0020','Güçlü Etkileşimler','lewis3','Lewis yapılarından atom özellikleri','orta','öncüllü','Lewis yapısında bağ ve ortaklanmamış çift sayılarından değerlik elektronları ve gruplar belirlenir.','Ortaklanmamış çifti saymamak; çift bağı tek ortak çift gibi okumak.',
 'Üç molekülün Lewis yapısını inceleyerek atomların değerlik elektronları ve ortaklanmamış çift sayıları hakkında yargıya varır.','Lewis yapısı yorumu','X₂, H₂Y, ZY₂',
 [A('X₂’yi incele','İki X arasında üç ortak çift, her X’te bir ortaklanmamış çift vardır.','X: 3 + 2 = 5 → I: doğru'),
  A('H₂Y’yi incele','Y’de iki ortaklanmamış çift çizilmiştir.','Y: 2 bağ + 2 × 2 = 6 e⁻ · II: yanlış'),
  A('ZY₂’yi incele','Z iki çift bağ yapar, ortaklanmamış çifti yoktur.','Z: 4 bağ = 4 e⁻ → III: doğru'),
  A('Sonuç','Doğru olanlar toplanır.',etk(d)+' · Sonuç: I ve III')],
 metin='Şekilde, X₂, H₂Y ve ZY₂ moleküllerinin Lewis (elektron nokta) yapıları gösterilmiştir. Bu moleküllerdeki bütün atomlar kararlı yapıya ulaşmıştır; X, Y ve Z gerçek element sembolü değildir.\nI. X atomunun değerlik elektron sayısı 5’tir.\nII. H₂Y molekülünde Y atomunun ortaklanmamış 1 elektron çifti vardır.\nIII. Z atomunun değerlik elektron sayısı 4’tür.\nBuna göre hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',
 ip=['Atomun değerlik elektron sayısını çizimden bulmak için ortak elektronlarını ve ortaklanmamış çiftlerini ayrı ayrı say.'],
 bilgi=[B('Lewis yapısı yorumu','Atomun değerlik elektronu = bağ sayısı + 2 × ortaklanmamış çift sayısı. Çift bağda 2 çift, üçlü bağda 3 çift ortak kullanılır. Örnek: NH₃’te N’nin 3 bağı ve 1 ortaklanmamış çifti vardır')],
 puf='Önce atomun bağ sayısını, sonra ortaklanmamış çiftlerini say; ikisinin toplamı değerlik elektronunu verir.',sekil=SK20)

# 21 · kaynama noktası sıralaması · zor · düz tablo
sr=[('H₂',2,-253),('CH₄',16,-162),('HF',20,20),('HCl',36.5,-85)]
SK21=tablo_svg(['Madde','Mol kütlesi (g/mol)'],[[a,str(b).replace('.',',')] for a,b,_ in sr])
bp=dict((a,c) for a,_,c in sr); dogru_sira=sorted(bp,key=bp.get); assert dogru_sira==['H₂','CH₄','HCl','HF']
secs=[('H₂ < CH₄ < HCl < HF',True,''),('H₂ < CH₄ < HF < HCl',False,'yalnız mol kütlesine bakmış; HF’deki hidrojen bağı HCl’nin dipol–dipolünden daha güçlüdür'),
      ('CH₄ < H₂ < HCl < HF',False,'apolar H₂ ile CH₄ arasında mol kütlesinin etkisini ters değerlendirmiş'),
      ('H₂ < HCl < CH₄ < HF',False,'polar maddeyi apolardan düşük yazmış; polar maddede dipol–dipol de vardır'),
      ('HF < HCl < CH₄ < H₂',False,'sıralamayı tamamen ters kurmuş; hidrojen bağı en yüksek kaynama noktasını verir')]
r=tek(secs,True)
S('0021','Zayıf Etkileşimler','siralama','Kaynama noktası sıralaması','orta','tablo','Kaynama noktası sıralamasında önce hidrojen bağı, sonra dipol–dipol ve London kuvvetleri, en son mol kütlesi değerlendirilir.','Yalnız mol kütlesine göre sıralamak; apolar–polar farkını görmemek.',
 'Mol kütlesi, polarlık ve hidrojen bağına göre kaynama noktası sıralaması yapar.','kaynama noktası sıralaması','H₂, CH₄, HF, HCl',
 [A('Etkileşimleri belirle','Her maddede baskın etkileşim bulunur.','H₂, CH₄: London · HCl: dipol–dipol (+ London) · HF: hidrojen bağı'),
  A('Apolarları sırala','Apolar maddelerde mol kütlesi büyük olanın kaynama noktası yüksektir.','H₂ (2) < CH₄ (16)'),
  A('Polarları ekle','Polar HCl apolarlardan yüksek, hidrojen bağlı HF en yüksektir.','CH₄ < HCl < HF'),
  A('Sonuç','Tüm sıralama birleştirilir.','H₂ < CH₄ < HCl < HF')],
 metin='Aynı koşullarda gaz hâldeki H₂, CH₄, HF ve HCl’nin mol kütleleri tabloda verilmiştir. H₂ ve CH₄ apolar, HF ve HCl ise polar moleküllerdir. Bir öğrenci, bu dört maddenin kaynama noktalarını karşılaştırmak için moleküller arası etkileşimleri değerlendirecektir.\nBuna göre bu maddelerin kaynama noktaları arasındaki ilişki aşağıdakilerden hangisidir?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Kaynama noktalarının doğru sıralanışı.',
 ip=['Önce hangi maddede hidrojen bağı bulunduğunu, sonra polar ve apolar olanları ayır; apolarlarda mol kütlesine bak.'],
 bilgi=[B('Kaynama noktası','Aynı hâldeki maddeler arasında kaynama noktası, moleküller arası etkileşimler güçlendikçe yükselir. Güç sırası genellikle London < dipol–dipol < hidrojen bağıdır. Örnek: H₂O’nun kaynama noktası H₂S’ten yüksektir')],
 puf='Mol kütleleri yakınsa hidrojen bağı > polarlık; apolar maddelerde mol kütlesi belirleyicidir.',sekil=SK21)

# 22 · ısıtma grafiği ve bağlar · zor · öncüllü grafik
Y=lambda T:(T+50)*.036
seg=[(0,-40),(.6,0),(2.2,0),(5.2,100),(9.2,100),(9.65,130)]
g=[f'\\draw[{ARR}] (0,0) -- (0,7.0); \\draw[{ARR}] (0,0) -- (10.2,0);',
   '\\node at (5.2,-.55) {Zaman}; \\node[rotate=90] at (-1.2,3.4) {Sıcaklık ($^\\circ$C)};']
for T in (0,100): g.append(f'\\draw (.08,{Y(T):.3f}) -- (-.08,{Y(T):.3f}); \\node[left] at (-.1,{Y(T):.3f}) {{{T}}}; \\draw[gray,dashed] (0,{Y(T):.3f}) -- (10,{Y(T):.3f});')
g.append('\\draw[very thick,vurgu] '+' -- '.join(pt(x,Y(T)) for x,T in seg)+';')
for k,(x,yv) in enumerate([(1.0,Y(-15)),(1.4,Y(0)+.4),(3.9,Y(50)+.45),(7.2,Y(100)+.4),(9.9,Y(118))],1): g.append(f'\\node[draw,circle,inner sep=1.5pt,font=\\footnotesize] at {pt(x,yv)} {{{k}}};')
SK22=tk('\n'.join(g))
d={'I':(False,'2. bölgede (erime) buz–su hâl değişimi olur; molekül içindeki O–H bağları kırılmaz'),
   'II':(True,'4. bölgede sıcaklık sabit; verilen enerji moleküller arasındaki hidrojen bağlarını koparmaya harcanır'),
   'III':(False,'1. ve 5. bölgelerde verilen ısı yalnız tanecik hızını (kinetik enerjiyi) artırır; H₂O atomlarına ayrılmaz')}
yanl=frozenset(k for k,v in d.items() if not v[0]); assert yanl==frozenset(['I','III'])
sira22=siralist('Yalnız I','I ve II','I ve III','II ve III','I, II ve III')
d_y={k:(not v[0],v[1]) for k,v in d.items()}
r=oc(d_y,sira22); assert r['dogru']=='I ve III'
_T=frozenset(k for k,v in d.items() if not v[0]); _y=[]
for _o in sira22:
    _W=frozenset(x for x in _o.replace('Yalnız ','').replace(',',' ').replace(' ve ',' ').split())
    if _W==_T: continue
    _p=[f'{x} öncülünü yanlış sanmış; oysa {d[x][1]}' for x in sorted(_W-_T)]+[f'{x} öncülünü doğru sanmış; oysa {d[x][1]}' for x in sorted(_T-_W)]
    _y.append((_o,'. '.join(_p)+'.','bilgi'))
r['yan']=_y
S('0022','Fiziksel ve Kimyasal Değişimler','isitma','Isıtma grafiğinde bağlar ve etkileşimler','zor','grafik','Hâl değişimi sırasında sıcaklık sabittir ve verilen enerji moleküller arası etkileşimleri zayıflatır; molekül içindeki kovalent bağlar korunur.','Hâl değişiminde O–H bağlarının koptuğunu sanmak; sabit sıcaklıkta enerji verilmediğini düşünmek.',
 'Isıtma grafiğinde bölgelere göre hangi etkileşimlerin değiştiğini yorumlar.','ısıtma grafiği ve bağlar','buz–su–buhar',
 [A('Bölgeleri tanı','1: buz ısınır · 2: erir · 3: su ısınır · 4: kaynar · 5: buhar ısınır.','2 ve 4: sıcaklık sabit'),
  A('I. öncül','Erirken molekül içi O–H bağları değil, moleküller arası etkileşimler değişir.','I: yanlış'),
  A('II. öncül','Kaynarken hidrojen bağları koparılır; sıcaklık değişmez.','II: doğru'),
  A('III. öncül','1 ve 5. bölgelerde tanecik hızı artar; H₂O ayrışmaz.','III: yanlış'),
  A('Sonuç','Yanlış olanlar sorulduğu için I ve III bulunur.','Yanlış: I ve III')],
 metin='Sabit güçte bir ısıtıcıyla 1 atm basınçta ısıtılan −40 °C’deki buzun sıcaklığının zamanla değişimi grafikte verilmiştir. Grafikteki bölgeler 1’den 5’e kadar numaralandırılmıştır. Öğretmen, bu süreçle ilgili aşağıdaki yargıları sunuyor.\nI. 2. bölgede H₂O moleküllerinin içindeki O–H bağları kırılır.\nII. 4. bölgede moleküller arasındaki hidrojen bağları kopar.\nIII. 1. ve 5. bölgelerde verilen ısı H₂O moleküllerini atomlarına ayırır.\nBuna göre bu yargılardan hangileri yanlıştır?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Yanlış olan yargılar.',
 ip=['Sıcaklığın sabit kaldığı bölgelerde ve arttığı bölgelerde verilen enerjinin ne için kullanıldığını ayrı ayrı düşün.'],
 bilgi=[B('Hâl değişiminde etkileşimler','Erime ve kaynama sırasında sıcaklık sabittir; verilen enerji moleküller arası etkileşimleri (suda hidrojen bağları) zayıflatır ya da koparır. Molekül içindeki kovalent bağlar korunur. Örnek: su buharlaşınca H₂O molekülleri olarak kalır')],
 puf='Hâl değişiminde molekül içindeki bağlar değil, moleküller arası etkileşimler değişir.',sekil=SK22)

# 23 · iyonik kristalin kırılganlığı · orta · şekil
def lat(ox,kay,dx=.6):
    o=[]
    for i in range(3):
        sh=kay*dx if i==0 else 0
        for j in range(4):
            x=ox+j*dx+sh; y=-i*dx; pos=(i+j)%2==0
            o.append(f'\\draw[fill={"vurgu!25" if pos else "white"}] {pt(x,y)} circle ({.2 if pos else .27}); \\node[font=\\scriptsize] at {pt(x,y)} {{{"+" if pos else "$-$"}}};')
    return o
o=lat(0,0)+lat(5.2,1)
o.append(f'\\draw[vurgu,very thick,{ARR}] (5.2,.75) -- (6.4,.75) node[midway,above,font=\\footnotesize] {{kuvvet}};')
o.append('\\node[font=\\footnotesize] at (1.0,-2.0) {Kuvvet uygulanmadan önce}; \\node[font=\\footnotesize] at (6.7,-2.0) {Üst katman bir iyon kaydırıldı};')
SK23=tk('\n'.join(o))
secs=[('Kayma sonucu aynı yüklü iyonlar yan yana gelir; itme kuvvetleri kristali kırar.',True,''),
      ('Kayma sonucu katyon–anyon çekimi artar ve kristal daha sağlam hâle gelir.',False,'kaymada karşılıklı zıt yükler uzaklaşır, aynı yükler yaklaşır; çekim azalır'),
      ('İyonik kristal, serbest elektron denizi sayesinde şekil değiştirir ve kırılmaz.',False,'serbest elektron denizi metalik bağa özgüdür; iyonik katı kırılgandır'),
      ('Kayma sırasında iyonlar elektron alışverişi yaparak yeni bir bileşik oluşturur.',False,'kayma fiziksel bir olaydır; yeni madde oluşmaz'),
      ('Kristalde iyonlar hareketsiz olduğundan katı iyonik bileşik hiçbir kuvvet altında kırılmaz.',False,'iyonlar kafeste titreşir; darbe uygulanınca kristal kırılır')]
r=tek(secs,True)
S('0023','Güçlü Etkileşimler','kirilgan','İyonik kristalin kırılganlığı','kolay','şekilli','İyonik katıda katyon ve anyonlar dönüşümlü dizilir; darbede katmanlar kayınca aynı yükler karşı karşıya gelir ve itme kristali kırar.','İyonik katıyı metal gibi dövülebilir sanmak.',
 'İyonik kristalin neden kırılgan olduğunu iyon düzeniyle açıklar.','iyonik kristalin kırılganlığı','kayan iyon katmanı',
 [A('Şekli yorumla','İlk kristalde zıt yükler yan yana; ikinci kristalde üst katman kaymıştır.','solda +/−, sağda aynı yükler üst üste'),
  A('Kuvvetleri değerlendir','Aynı yüklü iyonlar birbirini iter.','itme artar, çekim azalır'),
  A('Sonuç','Bu itme kristalin parçalanmasına yol açar.','Cevap: aynı yüklü iyonlar yan yana gelir, itme kristali kırar')],
 metin='Bir öğrenci, sofra tuzu kristalini çekiçle vurunca, metal bir kaşığın aksine tuzun parçalara ayrıldığını gözlemliyor. Öğretmeni, bunu açıklamak için iyonik kristalin iki durumunu şekildeki gibi çiziyor: kuvvet uygulanmadan önce ve üst katmanın bir iyon kaydırıldığı an.\nBuna göre iyonik katının kırılgan olması aşağıdakilerden hangisiyle açıklanır?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='İyonik katının kırılganlığının açıklaması.',
 ip=['Kayma sonrası komşu iyonlar arasındaki çekim ve itme kuvvetlerini karşılaştır.'],
 bilgi=[B('İyonik kristal','Kristalde katyon ve anyonlar dönüşümlü dizilir ve elektrostatik çekimle bir arada tutulur. Örnek: sofra tuzu kristalinde Na⁺ ve Cl⁻ iyonları dönüşümlü sıralanmıştır')],
 puf='İyonik katı darbede kırılır; metal ise elektron denizi sayesinde şekil değiştirir.',sekil=SK23)

# 24 · çok atomlu iyonlu bileşiklerde bağ türleri · zor · hikâyeli
BG={'NH₄Cl':(True,True),'KNO₃':(True,True),'MgCl₂':(True,False),'CO₂':(False,True),'Na₃PO₄':(True,True),'HCl':(False,True),'NaCl':(True,False)}
n=sum(1 for a,b in BG.values() if a and b); assert n==3
iyonik=sum(1 for a,b in BG.values() if a); assert iyonik==5
assert sum(1 for k in ['NH₄Cl'])==1 and sum(1 for k in ['KNO₃','Na₃PO₄'])==2 and n+1==4
S('0024','Güçlü Etkileşimler','karisikbag','Hem iyonik hem kovalent bağ içeren bileşikler','zor','hikâyeli','Çok atomlu iyon (NH₄⁺, NO₃⁻, PO₄³⁻ gibi) içeren iyonik bileşiklerde iyonlar arasında iyonik, iyon içinde kovalent bağ bulunur.','NH₄⁺, NO₃⁻ gibi çok atomlu iyonların içindeki kovalent bağı unutmak.',
 'Bileşiklerde iyonik ve kovalent bağların birlikte bulunmasını çok atomlu iyonlar üzerinden değerlendirir.','iyonik ve kovalent bağlı bileşikler','NH₄Cl, KNO₃, Na₃PO₄',
 [A('İyonları ayır','Her bileşiği oluşturan iyonlara ayır.','NH₄⁺Cl⁻ · K⁺NO₃⁻ · Mg²⁺ ve 2 Cl⁻ · 3 Na⁺ ve PO₄³⁻ · Na⁺Cl⁻'),
  A('Çok atomlu iyonları bul','Çok atomlu iyonun içinde kovalent bağ vardır.','NH₄⁺, NO₃⁻, PO₄³⁻'),
  A('Bileşikleri say','İyonik + kovalent: NH₄Cl, KNO₃, Na₃PO₄; MgCl₂ ve NaCl yalnız iyonik; CO₂ ve HCl yalnız kovalent.','3 bileşik'),
  A('Sonuç','Üç bileşikte iki bağ türü birlikte bulunur.','Cevap: 3')],
 metin='Bir tarım kooperatifinin laboratuvarında yedi madde (NH₄Cl, KNO₃, MgCl₂, CO₂, Na₃PO₄, HCl ve NaCl) etiketlenmiştir. Depo sorumlusu, bu maddeleri kimyasal yapılarına göre sınıflandırıyor ve hem iyonik hem de kovalent bağ içeren maddeleri ayrı bir rafa koyuyor.\nBuna göre rafa kaç madde konulur?',
 dogru=n,yan=[(1,'Yalnız amonyum klorürü çok atomlu iyonlu sanmış; KNO₃ ve Na₃PO₄’ın içindeki iyonlar da çok atomludur.','bilgi'),(2,'Yalnız nitrat ve fosfat içerenleri saymış; NH₄⁺ iyonunun içindeki N–H bağlarını atlamış.','dikkat'),(4,'MgCl₂’yi de saymış; Cl₂ indisini kovalent bağ sanmış.','bilgi'),(5,'Bütün iyonik bileşikleri (MgCl₂ ve NaCl dahil) saymış; tek atomlu iyonların içinde kovalent bağ yoktur.','bilgi')],
 istenen='İyonik ve kovalent bağı birlikte içeren madde sayısı.',
 ip=['Her bileşiğin hangi iyonlardan oluştuğunu yaz; bu iyonlardan hangileri tek atomlu, hangileri çok atomlu?'],
 bilgi=[B('Çok atomlu iyon','NH₄⁺, OH⁻, NO₃⁻, SO₄²⁻, CO₃²⁻, PO₄³⁻ çok atomlu iyonlardır; atomları kovalent bağla bağlıdır, iyonlar arasında ise iyonik bağ bulunur. Örnek: Na₂SO₄’te iyonik ve kovalent bağ birlikte vardır')],
 puf='Bileşikte NH₄⁺, OH⁻, NO₃⁻, SO₄²⁻, CO₃²⁻ ya da PO₄³⁻ varsa hem iyonik hem kovalent bağ vardır.')

bitir(P,'etkilesimiki',UK)
