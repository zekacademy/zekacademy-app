"""Ebob – ekok · şekilli paket (ebobsek): 9 soru, hepsi şekilli. Kardeş yok, ipucu 1. Her cevap ve çeldirici değer kodla hesaplanıp assert edilir.
Şekil ölçüleri Python'da üretilir; TikZ gövdesi aynı değerlerden f-string ile yazılır (bkz. havuz/URETIM-SEKIL.md)."""
import sys,os,math
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
from math import gcd
from functools import reduce
H.KONU='Ebob – ekok'
P=Parti('ebobsek','Ebob – ekok','mat|Ebob – ekok')
KY='ÖSYM 2018–2026 TYT Matematik (şekilli ebob–ekok soruları, yalnız mantık) · MEB 9. sınıf'
TP=lambda g:tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'+g+'\n\\end{tikzpicture}')
G_=lambda *a:reduce(gcd,a)
L_=lambda *a:reduce(lambda x,y:x*y//gcd(x,y),a)
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)

EB=B('EBOB','iki ya da daha fazla sayıyı birlikte tam bölen en büyük sayıdır. Örnek: EBOB(12, 18) = 6')
EK=B('EKOK','iki ya da daha fazla sayının ortak katlarının en küçüğüdür. Örnek: EKOK(4, 6) = 12')
KES=B('Kesim ve parça sayısı','bir çubuk n eş parçaya ayrılırsa n − 1 kesim yapılır. Örnek: 5 eş parçalı çubuk için 4 kesim gerekir')
SAY=B('Aralık ve nokta sayısı','kapalı bir çevrede eşit aralıklı nokta sayısı, aralık sayısına eşittir; doğrusal (açık) yolda nokta sayısı, aralık sayısından 1 fazladır. Örnek: 12 m’lik doğru yolda 3 m ara ile 4 aralık, 5 nokta olur')

kart('K-EBS-01','Eş parçalara kesme','Farklı boydaki çubukların hepsini artık kalmadan en uzun eş parçalara kesmek için boyların EBOB’u alınır; her çubuktan parça sayısı bölme ile, kesim sayısı parça sayısının bir eksiğiyle bulunur.','Parça sayısıyla kesim sayısını karıştırmak; EKOK almak; toplam parçadan 1 çıkarıp tek çubuk sanmak.','orta','şekilli',4,'ebs-kesme','Çubukları eş parçalara kesme',KY)
kart('K-EBS-02','Zemini karoyla kaplama','Dikdörtgen zeminin kenarlarının EBOB’u en büyük kare karonun kenarıdır; karo sayısı iki kenardaki karo sayılarının çarpımıdır.','EBOB yerine EKOK almak; karo sayısı yerine kenarı ya da toplamı yazmak; alanı kenarla bölmek.','kolay','şekilli',3,'ebs-karo','Dikdörtgen zemini eş kare karoyla kaplama',KY)
kart('K-EBS-03','Çevreye eşit aralıklı direk','Eşit aralığın en büyük değeri kenarların EBOB’udur; bir kenarı duvar olan açık yolda direk sayısı aralık sayısından 1 fazladır.','Açık yolu kapalı çevre sanmak; köşe direklerini iki kez saymak; EBOB yerine yarısını almak.','orta','şekilli',4,'ebs-direk','Eşit aralıklı direk dikme',KY)
kart('K-EBS-04','Dişli çarklar','Birbirine geçen çarkların işaretli dişleri yeniden başlangıç konumuna gelene kadar geçen diş sayısı çarkların diş sayılarının EKOK’udur; tur sayısı bu sayının diş sayısına bölümüdür.','Yalnız iki çarkın EKOK’unu almak; diş sayısını tur sanmak; başka çarkın tur sayısını yazmak.','orta','şekilli',3,'ebs-disli','Dişli çarklarda işaretli dişlerin buluşması',KY)
kart('K-EBS-05','Tuğlalardan küp','Dikdörtgenler prizması tuğlalarla oluşturulabilecek en küçük küpün ayrıtı, tuğla boyutlarının EKOK’udur; yüzey alanı 6 × ayrıt²’dir.','EKOK yerine EBOB ya da çarpım almak; yüzey alanı yerine bir yüzün alanını ya da hacmi yazmak.','orta','şekilli',3,'ebs-tugla','Tuğlalardan en küçük küp',KY)
kart('K-EBS-06','Dairesel pistte koşucular','Tur süreleri farklı iki koşucunun başlangıçta yan yana gelme anları EKOK’un katlarıdır; verilen süre ya da tur için bu katlar sayılır.','Çıkış anını saymak ya da saymamak; son anı dışarıda bırakmak; tur sayısıyla yan yana gelme sayısını karıştırmak.','orta','şekilli',3,'ebs-pist','Dairesel pistte yan yana gelme',KY)
kart('K-EBS-07','Asal çarpan ağacı','Ağaçtaki asal yapraklar çarpılarak sayılar bulunur; asal çarpanlarına ayrılan sayılarda EBOB ortak çarpanların küçük, EKOK tüm çarpanların büyük üsleriyle kurulur.','Ağacın yapraklarından birini okumamak; EKOK’ta ortak olmayan çarpanları unutmak; üsleri karıştırmak.','orta','şekilli',4,'ebs-agac','Asal çarpan ağacından EKOK',KY)
kart('K-EBS-08','Yanıp sönme zaman çizelgesi','Zaman çizelgesinden iki lambanın periyodu okunur; belirli sürede her lambanın ve ortak yanma anlarının sayısı bölmeyle bulunur, en az birinin yandığı anlar iki kümenin birleşimiyle hesaplanır.','Ortak anları iki kez saymak ya da hiç çıkarmamak; EBOB ile EKOK’u karıştırmak; süreyi yanlış bölmek.','zor','şekilli',5,'ebs-isik','Zaman çizelgesinde iki lambanın yanma anları',KY)

# ---------- 01 · orta · çubuk kesme ----------
ub=[90,150,210]; e=G_(*ub); pc=[x//e for x in ub]; kes=sum(p-1 for p in pc)
assert e==30 and pc==[3,5,7] and kes==12 and sum(pc)==15 and sum(pc)-1==14
e2=15; assert sum(x//e2-1 for x in ub)==27 and G_(*ub)==30
sc=.033; g=''
for i,x in enumerate(ub):
    y=-i*.8; g+=f'\\draw[thick] (0,{y}) rectangle ({x*sc:.3f},{y-.36});\\node[anchor=west] at ({x*sc+.15:.3f},{y-.18}) {{{x} cm}};'
sek=TP(g)
q('0001',tipId='ebs-kesme',tip='Çubukları eş parçalara kesme',z='orta',alt='EBOB Problemleri',kaz='Boyları farklı çubukları artık kalmadan en uzun eş parçalara keserken gereken kesim sayısını bulur.',kalip='şekilli',sekil=sek,
 kart='K-EBS-01 (eş parçalara kesme) · 90, 150, 210 cm çubuklar, toplam kesim sayısı',
 metin='Şekilde boyları verilen üç çubuğun her biri, hiç artık kalmayacak biçimde, boyları birbirine eşit ve olabildiğince uzun parçalara kesilecektir.\nBuna göre toplam kaç kesim yapılması gerekir?',
 dogru=12,yan=[(14,'Toplam 15 parçayı bulup tek çubuk sanarak 15 − 1 = 14 kesim demiş; her çubukta ayrı ayrı bir eksik kesim yapılır.','islem'),(15,'Parça sayısını (3 + 5 + 7 = 15) kesim sayısı sanmış.','dikkat'),(27,'EBOB’u 15 almış (30 değil); parçalar 6, 10, 14 olup kesimler 5 + 9 + 13 = 27 çıkmış.','bilgi'),(30,'Kesim sayısı yerine EBOB’u (parça uzunluğunu) yazmış.','dikkat')],
 istenen='Toplam kesim sayısı.',
 ip=['Önce her çubuk için aynı uzunluktaki en uzun parçanın boyunu bul.'],
 bilgi=[EB,KES],
 ad=[A('Parça boyu','Üç boyun EBOB’u en uzun ortak parça boyudur.','EBOB(90, 150, 210) = 30 cm'),A('Parça sayıları','Her boyu 30’a böl.','90 ÷ 30 = 3 · 150 ÷ 30 = 5 · 210 ÷ 30 = 7'),A('Kesim sayıları','Her çubukta parça sayısından 1 eksik kesim yapılır.','2 + 4 + 6'),A('Topla','Kesimleri topla.','2 + 4 + 6 = 12')],
 puf='“Kaç kesim” sorulduğunda parça sayısı değil, her çubuk için parça sayısı − 1 toplanır.')

# ---------- 02 · kolay · dikdörtgen zemin, karo ----------
w2,h2=252,180; t2=G_(w2,h2); n2=(w2//t2)*(h2//t2)
assert t2==36 and w2//t2==7 and h2//t2==5 and n2==35 and 7+5==12 and w2*h2//t2==1260 and (w2//18)*(h2//18)==140
sc=.022; g=f'\\draw[thick] (0,0) rectangle ({w2*sc:.3f},{h2*sc:.3f});'
g+=f'\\node at ({w2*sc/2:.3f},{-.3}) {{{w2} cm}};\\node[rotate=90] at ({-.3},{h2*sc/2:.3f}) {{{h2} cm}};'
sek=TP(g)
q('0002',tipId='ebs-karo',tip='Dikdörtgen zemini eş kare karoyla kaplama',z='kolay',alt='EBOB Problemleri',kaz='Dikdörtgen zemini kesmeden kaplayan en büyük kare karonun kenarını ve karo sayısını bulur.',kalip='şekilli',sekil=sek,
 kart='K-EBS-02 (zemini karoyla kaplama) · 252 × 180 cm zemin, karo sayısı',
 metin='Bir salonun dikdörtgen biçimindeki zemini şekilde gösterilmiştir. Bu zemin, aynı boyda kare karolarla, karo kesmeden ve boşluk bırakmadan döşenecektir. Karo kenarı santimetre cinsinden tam sayı olup mümkün olan en büyük değeri alacaktır.\nBuna göre salonun zeminine kaç karo döşenir?',
 dogru=35,yan=[(12,'Kenarlara dizilen karo sayılarını (7 ve 5) toplamış; karo sayısı iki sayının çarpımıdır.','dikkat'),(36,'Karo sayısı yerine karonun kenarını (EBOB = 36) yazmış.','dikkat'),(140,'EBOB’u 18 almış (36 değil, yarısı); karo sayısı 14 × 10 = 140 çıkmış.','bilgi'),(1260,'Zeminin alanını (45360) karonun kenarına (36) bölmüş; karonun alanına (1296) bölmesi gerekirdi.','islem')],
 istenen='Gerekli karo sayısı.',
 ip=['Karo kenarının zeminin iki kenarını da tam bölmesi gerekir.'],
 bilgi=[EB],
 ad=[A('Karo kenarı','En büyük kare karonun kenarı iki kenarın EBOB’udur.','EBOB(252, 180) = 36 cm'),A('Her kenardaki karo sayısı','Kenarları 36’ya böl.','252 ÷ 36 = 7 · 180 ÷ 36 = 5'),A('Çarp','Karo sayısı iki sayının çarpımıdır.','7 × 5 = 35')],
 puf='Karo sayısını bulmak için alan oranını (45360 ÷ 1296) da kullanabilirsin; sonuç kenar sayıları çarpımıyla aynıdır.')

# ---------- 03 · zor · iki dişli çark, dakikada tur ----------
dA,dB,hz,dk=18,30,20,10; ek3=L_(dA,dB); turA=ek3//dA; sn=turA*60//hz; top=dk*60; kez3=top//sn
assert ek3==90 and turA==5 and sn==15 and top==600 and kez3==40 and top//sn+1==41 and top//sn-1==39
m3=.06; rA,rB=dA*m3,dB*m3; pB3=360/dB
def disli2(cx,rr,n,faz,ad,isaret):
    p=360/n; pts=[]
    for k in range(n):
        t0=faz+k*p-.25*p
        for (ang,ra) in [(t0,rr-.07),(t0+.1*p,rr+.07),(t0+.4*p,rr+.07),(t0+.5*p,rr-.07)]:
            pts.append((cx+ra*math.cos(math.radians(ang)),ra*math.sin(math.radians(ang))))
    s_='\\draw[thick] '+' -- '.join(f'({x:.3f},{y:.3f})' for x,y in pts)+' -- cycle;'
    s_+=f'\\node[font=\\scriptsize,align=center] at ({cx:.3f},0) {{{ad}\\\\{n} diş}};'
    s_+=f'\\fill[vurgu] ({cx+(rr+.0)*math.cos(math.radians(isaret)):.3f},{(rr+.0)*math.sin(math.radians(isaret)):.3f}) circle (.07);'
    return s_
sek=TP(disli2(0,rA,dA,0,'A',0)+disli2(rA+rB,rB,dB,180+pB3/2,'B',180+pB3/2))
q('0003',tipId='ebs-disli',tip='Dişli çarklarda işaretli dişlerin buluşması',z='zor',alt='EKOK Problemleri',kaz='Birbirine geçen iki çarkın işaretli dişlerinin ortak konuma gelme süresini EKOK ile bulup belirli sürede kaç kez buluştuklarını hesaplar.',kalip='şekilli',sekil=sek,
 kart='K-EBS-04 (dişli çarklar) · 18 ve 30 dişli çark, A dakikada 20 tur, 10 dakikada buluşma sayısı',
 metin='Şekilde diş sayıları verilen A ve B çarkları birbirine geçmiştir. Başlangıçta her çarkın işaretli dişi (yeşil nokta) temas noktasındadır. A çarkı sabit hızla dakikada 20 tur yapmaktadır.\nÇarklar 10 dakika boyunca döndürülürse, işaretli dişler başlangıç anı hariç, 10. dakikanın sonu dahil olmak üzere kaç kez yeniden temas noktasında bulunur?',
 dogru=40,yan=[(5,'Sorulan sayı yerine işaretli dişlerin ilk buluşmasına kadar A’nın attığı tur sayısını (90 ÷ 18 = 5) yazmış.','dikkat'),(15,'Sorulan sayı yerine ilk buluşmaya kadar geçen süreyi (15 saniye) yazmış.','dikkat'),(39,'10. dakikanın sonundaki buluşmayı (600. saniye) saymamış.','dikkat'),(41,'Başlangıç anını da bir buluşma sayıp 40 + 1 = 41 bulmuş.','dikkat')],
 istenen='İşaretli dişlerin yeniden temas noktasında bulunma sayısı.',
 ip=['İşaretli dişler, kaç diş geçince ikisi birden başlangıç konumuna döner? Bu geçiş A’nın kaç saniyesine denk gelir?'],
 bilgi=[EK,B('Hız ve süre','sabit hızla dakikada n tur yapan çark, bir turu 60 ÷ n saniyede tamamlar. Örnek: dakikada 12 tur yapan çarkın bir turu 5 saniye sürer')],
 ad=[A('Ortak diş sayısı','İki işaret aynı anda başlangıç konumuna geldiğinde geçen diş sayısı 18 ve 30’un ortak katıdır; ilki EKOK’tur.','EKOK(18, 30) = 90 diş'),A('A’nın turu','A çarkı 18 dişli.','90 ÷ 18 = 5 tur'),A('Süre','A’nın bir turu 60 ÷ 20 = 3 saniyedir.','5 × 3 = 15 saniyede bir'),A('Say','10 dakika 600 saniyedir; son an dahil.','600 ÷ 15 = 40')],
 puf='Birbirine geçen çarklarda geçen diş sayısı eşittir; ilk ortak konum EKOK kadar diş sonra olur ve sonraki buluşmalar onun katlarıdır.')

# ---------- 04 · orta · bir kenarı duvar olan bahçe, direk ----------
a4,b4=72,54; g4=G_(a4,b4); yol=a4+b4+a4; dir4=yol//g4+1
assert g4==18 and yol==198 and yol//g4==11 and dir4==12
assert (2*a4+2*b4)//g4==14 and yol//9+1==23 and yol//6+1==34
sc=.07; W,Hh=a4*sc,b4*sc
g=f'\\draw[thick] (0,0) -- ({W:.3f},0) -- ({W:.3f},{Hh:.3f}) -- (0,{Hh:.3f});'
g+=f'\\draw[line width=2.6pt,gray] (0,0) -- (0,{Hh:.3f});\\draw[pattern=north east lines,pattern color=gray] (-.3,0) rectangle (-.1,{Hh:.3f});\\node[rotate=90,font=\\scriptsize] at (-.55,{Hh/2:.3f}) {{duvar}};'
for (x,y) in [(0,0),(W,0),(W,Hh),(0,Hh)]: g+=f'\\fill[vurgu] ({x:.3f},{y:.3f}) circle (.09);'
g+=f'\\node at ({W/2:.3f},-.32) {{{a4} m}};\\node at ({W/2:.3f},{Hh+.32:.3f}) {{{a4} m}};\\node[anchor=west] at ({W+.15:.3f},{Hh/2:.3f}) {{{b4} m}};'
g+=f'\\fill[vurgu] ({W+.35:.3f},{Hh+.5:.3f}) circle (.09);\\node[anchor=west,font=\\scriptsize] at ({W+.5:.3f},{Hh+.5:.3f}) {{köşe direği}};'
sek=TP(g)
q('0004',tipId='ebs-direk',tip='Eşit aralıklı direk dikme',z='orta',alt='EBOB Problemleri',kaz='Bir kenarı duvar olan dikdörtgen bahçenin diğer üç kenarına eşit aralıklı direk dikerken gereken en az direk sayısını bulur.',kalip='şekilli',sekil=sek,
 kart='K-EBS-03 (çevreye eşit aralıklı direk) · 72 × 54 m bahçe, bir kenar duvar',
 metin='Şekilde, bir kenarı duvar olan dikdörtgen biçimindeki bir bahçe gösterilmiştir. Duvarın bulunmadığı üç kenara tel örgü çekilecek, dört köşeye birer direk dikilecek ve ardışık iki direk arasındaki uzaklık her yerde eşit ve metre cinsinden tam sayı olacaktır.\nBuna göre bu iş için en az kaç direk gerekir?',
 dogru=12,yan=[(11,'Aralık sayısını (198 ÷ 18 = 11) direk sayısı sanmış; açık yolda direk sayısı aralıktan 1 fazladır.','dikkat'),(14,'Duvarlı kenarı da sayıp kapalı çevre (252 m) için 252 ÷ 18 = 14 direk bulmuş; üç kenarlık açık yolda iki uç direğini ve duvarlı kenarın direk gerektirmediğini düşünmemiş.','dikkat'),(23,'EBOB’u 9 almış (18 değil); 198 ÷ 9 + 1 = 23.','bilgi'),(34,'EBOB’u 6 almış; 198 ÷ 6 + 1 = 34.','bilgi')],
 istenen='En az direk sayısı.',
 ip=['Aralığın en büyük değeri, tel örgü çekilen kenarların ortak bölenidir; üç kenar da duvara kadar uzanır.'],
 bilgi=[EB,SAY],
 ad=[A('Aralık','En az direk için aralık en büyük olmalı; 72 ve 54’ün EBOB’u alınır.','EBOB(72, 54) = 18 m'),A('Tel örgü uzunluğu','Duvar olmayan üç kenar: iki uzun, bir kısa.','72 + 54 + 72 = 198 m'),A('Aralık sayısı','Toplam uzunluğu aralığa böl.','198 ÷ 18 = 11 aralık'),A('Direk sayısı','Yol kapalı değil, açık olduğundan direk sayısı aralıktan 1 fazladır.','11 + 1 = 12')],
 puf='Kapalı çevrede direk sayısı aralık sayısına eşittir; bir kenarı açık bırakılan (duvarlı) yolda iki uç da direk istediğinden bir fazla olur.')

# ---------- 05 · orta · üç dişli çark ----------
dt=[16,24,40]; E5=L_(*dt); tur=[E5//d for d in dt]
assert E5==240 and tur==[15,10,6] and L_(16,24)//24==2 and L_(24,40)//24==5
m=.052; r=[d*m for d in dt]; cx=[0,r[0]+r[1],r[0]+2*r[1]+r[2]]
def disli(cx,rr,n,faz,ad):
    isa=faz+round((90-faz)/(360/n))*(360/n)
    p=360/n; pts=[]
    for k in range(n):
        t0=faz+k*p-.25*p
        for (ang,ra) in [(t0,rr-.07),(t0+.1*p,rr+.07),(t0+.4*p,rr+.07),(t0+.5*p,rr-.07)]:
            pts.append((cx+ra*math.cos(math.radians(ang)),ra*math.sin(math.radians(ang))))
    s='\\draw[thick] '+' -- '.join(f'({x:.3f},{y:.3f})' for x,y in pts)+' -- cycle;'
    s+=f'\\node[font=\\scriptsize,align=center] at ({cx:.3f},0) {{{ad}\\\\{n} diş}};'
    s+=f'\\fill[vurgu] ({cx+(rr+.07)*math.cos(math.radians(isa)):.3f},{(rr+.07)*math.sin(math.radians(isa)):.3f}) circle (.06);'
    return s
pB=360/24; pC=360/40
g=disli(cx[0],r[0],16,0,'A')+disli(cx[1],r[1],24,180+pB/2,'B')+disli(cx[2],r[2],40,180,'C')
sek=TP(g)
q('0005',tipId='ebs-disli',tip='Dişli çarklarda işaretli dişlerin buluşması',z='orta',alt='EKOK Problemleri',kaz='Birbirine geçen üç çarkın işaretli dişlerinin yeniden ilk konuma gelmesi için bir çarkın attığı tur sayısını EKOK ile bulur.',kalip='şekilli',sekil=sek,
 kart='K-EBS-04 (dişli çarklar) · 16, 24, 40 dişli üç çark, B çarkının tur sayısı',
 metin='Şekilde diş sayıları verilen A, B ve C çarkları, A–B ve B–C çarkları birbirine geçecek biçimde yan yana yerleştirilmiştir. Her çarkın bir dişi (yeşil nokta ile) işaretlenmiştir. Çarklar döndürülmeye başlandığında üç çarkın da işaretli dişleri ilk kez aynı anda başlangıçtaki konumlarına gelmektedir.\nBuna göre bu anda B çarkı kaç tur atmış olur?',
 dogru=10,yan=[(2,'Yalnız A ve B çarklarının EKOK’unu (48 diş) alıp B’nin 48 ÷ 24 = 2 turunu bulmuş; C çarkını hesaba katmamış.','dikkat'),(5,'Yalnız B ve C çarklarının EKOK’unu (120 diş) alıp B’nin 120 ÷ 24 = 5 turunu bulmuş; A çarkını hesaba katmamış.','dikkat'),(6,'B çarkı yerine C çarkının tur sayısını (240 ÷ 40) yazmış.','dikkat'),(15,'B çarkı yerine A çarkının tur sayısını (240 ÷ 16) yazmış.','dikkat')],
 istenen='B çarkının attığı tur sayısı.',
 ip=['Çarklar birbirine geçerken her birinden kaç diş geçer?'],
 bilgi=[EK],
 ad=[A('Diş geçişi','Çarklar birbirine geçtiğinden her çarkta aynı sayıda diş geçer; bir çark kaç tur atarsa atsın, ortak diş sayısı aynı olur.','geçen diş sayısı üç çarkta da eşit'),A('Geçen diş sayısı','Hepsi başlangıç konumuna dönmek için geçen diş sayısı üç diş sayısının ortak katı olmalı; ilk kez olması için en küçüğü alınır.','EKOK(16, 24, 40) = 240 diş'),A('B’nin turu','B çarkı 24 dişlidir.','240 ÷ 24 = 10 tur')],
 puf='Birbirine geçen çarklarda geçen diş sayısı eşit olduğundan tur sayısı = EKOK ÷ çarkın diş sayısıdır.')

# ---------- 06 · kolay · dairesel pist ----------
sa,sb=72,90; ek=L_(sa,sb); T=sa*30; kez=T//ek
assert ek==360 and T==2160 and kez==6 and ek//sb==4 and T//ek-1==5 and T//ek+1==7
sc=1.25; g=f'\\draw[thick] (0,0) circle ({sc});\\draw[thick,vurgu] (0,{-sc-.2}) -- (0,{-sc+.2});\\node[font=\\scriptsize] at (0,{-sc-.45}) {{başlangıç çizgisi}};'
g+=f'\\fill[vurgu] (0,{-sc}) circle (.1);\\draw[thick,fill=white] (0,{-sc+.32}) circle (.1);'
g+=f'\\draw[-{{Stealth[length=2mm]}}] ({.5*math.cos(math.radians(150)):.3f},{.5*math.sin(math.radians(150)):.3f}) arc[start angle=150,delta angle=-240,radius=.5];'
g+=f'\\fill[vurgu] (2.1,.45) circle (.1);\\node[anchor=west] at (2.3,.45) {{A: bir tur {sa} s}};\\draw[thick] (2.1,-.1) circle (.1);\\node[anchor=west] at (2.3,-.1) {{B: bir tur {sb} s}};'
sek=TP(g)
q('0006',tipId='ebs-pist',tip='Dairesel pistte yan yana gelme',z='orta',alt='EKOK Problemleri',kaz='Tur süreleri farklı iki koşucunun başlangıç çizgisinde yan yana gelme sayısını EKOK ile bulur.',kalip='şekilli',sekil=sek,
 kart='K-EBS-06 (dairesel pistte koşucular) · A 72 s, B 90 s, A 30 tur atıncaya kadar yan yana gelme sayısı',
 metin='Şekildeki dairesel pistte A ve B koşucuları, başlangıç çizgisinden aynı anda ve aynı yönde sabit hızlarla koşmaya başlıyor; şekilde her koşucunun bir turu tamamlama süresi verilmiştir.\nA koşucusu 30 tur atıncaya kadar (30. turun bittiği an dahil, başlangıç anı hariç) bu iki koşucu başlangıç çizgisinde kaç kez yan yana gelir?',
 dogru=6,yan=[(4,'İlk yan yana gelme anına kadar B’nin attığı tur sayısını (360 ÷ 90 = 4) yazmış.','dikkat'),(5,'A’nın 30. turunun bittiği anı (2160. saniye) saymamış (2160 ÷ 360 − 1).','dikkat'),(7,'Çıkış anını da bir buluşma olarak sayıp 6 + 1 = 7 bulmuş.','dikkat'),(30,'Sorulan sayı yerine A’nın tur sayısını (30) yazmış.','dikkat')],
 istenen='Başlangıç çizgisinde yan yana gelme sayısı.',
 ip=['İki koşucu aynı anda başlangıçtaysa bu an, iki tur süresinin ortak katıdır.'],
 bilgi=[EK],
 ad=[A('Buluşma aralığı','İki koşucu, tur sürelerinin ortak katlarında başlangıçtadır; ilki EKOK’tadır.','EKOK(72, 90) = 360 s'),A('Toplam süre','A’nın 30 turu.','30 × 72 = 2160 s'),A('Say','Buluşmalar 360 s’nin katlarıdır; 2160 dahil.','2160 ÷ 360 = 6')],
 puf='Buluşma sayısı = toplam süre ÷ EKOK; çıkış anını sorudaki “hariç/dahil” ifadesine göre ayrıca düşün.')

# ---------- 07 · orta · tuğlalardan küp ----------
tb=[4,10,15]; ed=L_(*tb); ya=6*ed*ed
assert ed==60 and ya==21600 and 12*ed==720 and ed*ed==3600 and 6*L_(10,15)**2==5400 and ed**3==216000
sc=.17; wd,hd,dd=15*sc,10*sc,4*sc; ox,oy=dd*.85,dd*.55
g=f'\\draw[thick] (0,0) rectangle ({wd:.3f},{hd:.3f});\\draw[thick] ({wd:.3f},{hd:.3f}) -- ({wd+ox:.3f},{hd+oy:.3f}) -- ({ox:.3f},{hd+oy:.3f}) -- (0,{hd:.3f});\\draw[thick] ({wd:.3f},0) -- ({wd+ox:.3f},{oy:.3f}) -- ({wd+ox:.3f},{hd+oy:.3f});'
g+=f'\\draw[dashed] (0,0) -- ({ox:.3f},{oy:.3f}) -- ({wd+ox:.3f},{oy:.3f});\\draw[dashed] ({ox:.3f},{oy:.3f}) -- ({ox:.3f},{hd+oy:.3f});'
g+=f'\\node at ({wd/2:.3f},-.28) {{15 cm}};\\node[anchor=east] at (-.1,{hd/2:.3f}) {{10 cm}};\\node[anchor=west] at ({wd+ox+.08:.3f},{hd/2+oy/2+.02:.3f}) {{4 cm}};'
sek=TP(g)
q('0007',tipId='ebs-tugla',tip='Tuğlalardan en küçük küp',z='orta',alt='EKOK Problemleri',kaz='Boyutları verilen eş tuğlalarla oluşturulabilecek en küçük küpün ayrıtını EKOK ile bulup yüzey alanını hesaplar.',kalip='şekilli',sekil=sek,
 kart='K-EBS-05 (tuğlalardan küp) · 4 × 10 × 15 cm tuğla, en küçük küpün yüzey alanı',
 metin='Şekilde boyutları verilen dikdörtgenler prizması biçimindeki eş tuğlalar, hepsi aynı yönde olacak biçimde ve aralarında boşluk kalmadan yan yana ve üst üste dizilerek içi dolu bir küp oluşturacaktır. Küp, mümkün olan en küçük küp olacaktır.\nBuna göre bu küpün yüzey alanı kaç cm² olur?',
 dogru=21600,yan=[(720,'Yüzey alanı yerine küpün tüm ayrıtlarının uzunlukları toplamını (12 × 60) yazmış.','dikkat'),(3600,'Yüzey alanı yerine yalnız bir yüzün alanını (60 × 60) yazmış.','dikkat'),(5400,'Küpün ayrıtını yalnız 10 ve 15’in EKOK’u (30) alıp 4’ü hesaba katmamış; 6 × 30² = 5400.','dikkat'),(216000,'Yüzey alanı yerine küpün hacmini (60³) yazmış.','dikkat')],
 istenen='En küçük küpün yüzey alanı.',
 ip=['Küpün her ayrıtı, tuğlanın üç boyutunun da katı olmalıdır.'],
 bilgi=[EK,B('Küpün yüzey alanı','ayrıtı a olan küpün altı yüzü vardır; yüzey alanı 6 × a²’dir. Örnek: ayrıtı 5 cm olan küpün yüzey alanı 6 × 25 = 150 cm²')],
 ad=[A('Ayrıt','Küpün ayrıtı üç boyutun ortak katı olmalı; en küçüğü EKOK’tur.','EKOK(4, 10, 15) = 60 cm'),A('Bir yüz','Bir yüz, kenarı 60 cm olan bir karedir.','60 × 60 = 3600 cm²'),A('Yüzey alanı','Küpün 6 yüzü vardır.','6 × 3600 = 21600 cm²')],
 puf='Ayrıtı en küçük küp, tuğla boyutlarının EKOK’udur; ayrıt bulunduktan sonra sorulan büyüklüğe (hacim, yüzey alanı, tuğla sayısı) dikkat et.')

# ---------- 08 · zor · asal çarpan ağacı ----------
def yer(t,d,konum,out,ox=0):
    if isinstance(t,int):
        x=len(konum)*.72+ox; konum.append(x); out.append(('yaprak',x,-d*.85,t)); return x,-d*.85
    lab,ch=t; pos=[yer(c,d+1,konum,out,ox) for c in ch]; x=sum(p[0] for p in pos)/len(pos); y=-d*.85
    out.append(('kutu',x,y,lab)); out.append(('bag',x,y,pos)); return x,y
TA=('A',[(None,[(None,[2,2]),(9,[3,3])]),5]); TB=('B',[7,(None,[3,(18,[2,(None,[3,3])])])])
def deger(t): return t if isinstance(t,int) else deger(t[1][0])*deger(t[1][1])
def dogrula(t):
    if isinstance(t,int): return
    for c in t[1]: dogrula(c)
    if isinstance(t[0],int): assert t[0]==deger(t)
dogrula(TA); dogrula(TB)
A8,B8=deger(TA),deger(TB); assert (A8,B8)==(180,378)
eb=G_(A8,B8); ekk=L_(A8,B8); assert eb==18 and ekk==3780 and A8*B8==68040 and 2*3**2*5*7==630 and 2*3**3*5*7==1890 and L_(36,B8)==756
def agac(t,ox):
    out=[]; konum=[]; yer(t,0,konum,out,ox); s=''
    for o in out:
        if o[0]=='bag':
            _,x,y,pos=o
            for (px,py) in pos: s+=f'\\draw ({x:.3f},{y-.25:.3f}) -- ({px:.3f},{py+(.25):.3f});'
    for o in out:
        if o[0]=='yaprak': s+=f'\\node[draw,circle,fill=white,inner sep=1.5pt,minimum size=.5cm] at ({o[1]:.3f},{o[2]:.3f}) {{{o[3]}}};'
        elif o[0]=='kutu': s+=f'\\node[draw,fill=white,minimum size=.5cm,inner sep=1pt] at ({o[1]:.3f},{o[2]:.3f}) {{{o[3] if o[3] is not None else ""}}};'
    return s,len(konum)
s1,n1=agac(TA,0); s2,n2=agac(TB,n1*.72+.7)
sek=TP(s1+s2)
q('0008',tipId='ebs-agac',tip='Asal çarpan ağacından EKOK',z='orta',alt='EBOB–EKOK Uygulamaları',kaz='Asal çarpan ağaçlarından iki sayıyı bulup asal çarpanlarına ayırarak EKOK’larını hesaplar.',kalip='şekilli',sekil=sek,
 kart='K-EBS-07 (asal çarpan ağacı) · A = 180 ve B = 378 ağaçları, EKOK(A, B)',
 metin='Şekilde A ve B doğal sayılarının asal çarpan ağaçları gösterilmiştir. Her kutudaki sayı, kendisinden bir alt düzeydeki iki sayının çarpımına eşittir; yuvarlak içindekiler asal sayılardır; boş kutular bilinmeyen sayılardır.\nBuna göre EKOK(A, B) kaçtır?',
 dogru=3780,yan=[(18,'EKOK yerine EBOB’u (2 × 3² = 18) hesaplamış.','dikkat'),(630,'Ortak çarpanları küçük üsleriyle (2¹, 3²), ortak olmayanları da alarak 2 × 3² × 5 × 7 = 630 bulmuş; EKOK’ta ortak çarpanlar büyük üsle alınır.','bilgi'),(756,'A ağacındaki 5 yaprağını okumamış (A = 36 sanmış); EKOK(36, 378) = 756 bulmuş.','dikkat'),(1890,'2 için küçük üssü (2¹), 3 için büyük üssü (3³) alıp 2 × 3³ × 5 × 7 = 1890 bulmuş.','bilgi')],
 istenen='EKOK(A, B).',
 ip=['Her ağaçta yaprakları (asal sayıları) çarparak sayıyı bul; sonra asal çarpanlarını karşılaştır.'],
 bilgi=[B('Asal sayı','1’den büyük olup yalnız 1’e ve kendisine bölünen doğal sayıdır. Örnek: 2, 3, 5, 7 asaldır; 9 = 3 × 3 asal değildir'),EK,EB],
 ad=[A('A’yı oku','A ağacının yaprakları 2, 2, 3, 3, 5.','A = 2² × 3² × 5 = 180'),A('B’yi oku','B ağacının yaprakları 7, 3, 2, 3, 3.','B = 2 × 3³ × 7 = 378'),A('Üsleri seç','EKOK için her asal çarpanın en büyük üssü alınır.','2², 3³, 5, 7'),A('Çarp','Seçilen çarpanları çarp.','4 × 27 × 5 × 7 = 3780')],
 puf='EKOK’ta bütün asal çarpanlar en büyük üsleriyle, EBOB’da yalnız ortak çarpanlar en küçük üsleriyle alınır; A × B = EBOB × EKOK ilişkisiyle sonucu denetle: 18 × 3780 = 68040.')

# ---------- 09 · zor · yanıp sönme zaman çizelgesi ----------
pa,pb,N=8,12,300; ca,cb,cab=N//pa,N//pb,N//L_(pa,pb); un=ca+cb-cab
assert (ca,cb,cab,un)==(37,25,12,50) and ca+cb==62 and ca+cb+cab==74
sc=.145; g=''
for i,(ad,p) in enumerate([('A',pa),('B',pb)]):
    y=-i*.8; g+=f'\\node at (-.4,{y}) {{{ad}}};\\draw[gray] (0,{y}) -- ({48*sc:.3f},{y});'
    for t in range(p,49,p): g+=f'\\fill[vurgu] ({t*sc:.3f},{y}) circle (.09);'
g+=f'\\draw[-{{Stealth[length=1.8mm]}}] (0,-1.5) -- ({48*sc+.3:.3f},-1.5);'
for t in range(0,49,4): g+=f'\\draw (-0,-1.5) ++({t*sc:.3f},.05) -- ++(0,-.1);\\node[font=\\scriptsize] at ({t*sc:.3f},-1.78) {{{t}}};'
g+=f'\\node[font=\\scriptsize,anchor=west] at ({48*sc+.4:.3f},-1.5) {{saniye}};'
sek=TP(g)
q('0009',tipId='ebs-isik',tip='Zaman çizelgesinde iki lambanın yanma anları',z='zor',alt='EKOK Problemleri',kaz='Zaman çizelgesinden iki lambanın periyodunu okuyup belirli sürede en az birinin yandığı anların sayısını ortak anları çıkararak bulur.',kalip='şekilli',sekil=sek,
 kart='K-EBS-08 (yanıp sönme zaman çizelgesi) · A 8 s, B 12 s, 300 s içinde en az birinin yandığı an sayısı',
 metin='Şekilde A ve B lambalarının 0–48. saniyeler arasındaki yanma anları (yeşil noktalar) gösterilmiştir; lambalar aynı aralıkla yanmaya devam etmektedir. 0. saniyede hiçbir lamba yanmamaktadır.\n300. saniyeye kadar (300. saniye dahil) bu iki lambadan en az birinin yandığı kaç an vardır?',
 dogru=50,yan=[(12,'Yalnız iki lambanın birlikte yandığı anları (24’ün katları) saymış.','dikkat'),(37,'Yalnız A lambasının yanma sayısını (300 ÷ 8 = 37) yazmış.','dikkat'),(62,'A ve B’nin yanma sayılarını (37 + 25) toplamış; birlikte yanılan anları iki kez saymış, bir kez çıkarmamış.','dikkat'),(74,'Ortak anları çıkarmak yerine toplama eklemiş (37 + 25 + 12).','islem')],
 istenen='En az bir lambanın yandığı an sayısı.',
 ip=['Her lambanın yanma aralığını şekilden oku; iki lambanın birlikte yandığı anlar neden ayrıca düşünülmeli?'],
 bilgi=[EK,B('İki kümenin birleşimi','s(A ∪ B) = s(A) + s(B) − s(A ∩ B). Örnek: 1’den 12’ye kadar 2’nin 6, 3’ün 4, 6’nın 2 katı vardır; 2 ya da 3’ün katı 6 + 4 − 2 = 8 tanedir')],
 ad=[A('Aralıkları oku','İlk yanışlar 8 ve 12. saniyedir; sonra aynı aralıkla sürer.','A her 8 s, B her 12 s'),A('A’nın sayısı','300’e kadar 8’in katları.','300 ÷ 8 = 37 (kalan 4) → 37'),A('B’nin sayısı','300’e kadar 12’nin katları.','300 ÷ 12 = 25 → 25'),A('Ortak anlar','İkisi birlikte EKOK(8, 12) = 24’ün katlarında yanar.','300 ÷ 24 = 12 (kalan 12) → 12'),A('Birleşim','Ortak anları iki kez saydığın için bir kez çıkar.','37 + 25 − 12 = 50')],
 puf='“En az birinin” sorularında iki sayımı topla, ortak olanları bir kez çıkar; ortak anlar EKOK’un katlarıdır.')

bitir(P,'ebobsek','mat|Ebob – ekok')
