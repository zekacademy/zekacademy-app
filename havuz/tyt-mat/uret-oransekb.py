"""Oran Orantı · ŞEKİLLİ ek paket (oransekb): 10 soru; şekil/tablo/grafik çözüm verisini taşır; sayılar Python'da hesaplanır, her doğru ve çeldirici değer assert'lidir. Kardeş yok, ipucu 1."""
import sys,os,math
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
H.KONU='Oran Orantı'
P=Parti('oransekb','Oran Orantı','mat|Oran Orantı')
KY='ÖSYM 2018–2026 TYT Matematik (şekilli/tablolu/grafikli oran-orantı soruları; yalnız mantık) · MEB 8–9. sınıf'
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)
def fig(body): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'+body+'\n\\end{tikzpicture}')
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)
def tx(x,y,t,st=''): return f'\\node[{st}] at ({x:.3f},{y:.3f}) {{{t}}};'
def ln(x1,y1,x2,y2,st=''): return f'\\draw[{st}] ({x1:.3f},{y1:.3f}) -- ({x2:.3f},{y2:.3f});'

DO=B('Doğru orantı','iki çokluktan biri belli sayıda katına çıkınca öteki de aynı sayıda katına çıkıyorsa orantı doğrudur; oran sabittir. Örnek: 4 kalem 20 TL ise 6 kalem 30 TL’dir')
TO=B('Ters orantı','biri belli sayıda katına çıkarken öteki aynı sayıda küçülüyorsa orantı terstir; çarpım sabittir. Örnek: 6 işçi 10 günde bitirirse 4 işçi 15 günde bitirir')
BEN=B('Benzer şekiller','karşılıklı kenar uzunlukları aynı oranda büyüyen ya da küçülen şekillere benzer denir; bu oran her kenar için aynıdır. Örnek: 2 cm × 3 cm’lik dikdörtgen 3 katına büyütülürse 6 cm × 9 cm olur')
KAR=B('Karışım oranı','“a : b” oranı, toplamın a + b parçaya bölündüğünü gösterir; bir madde miktarı toplamla parça sayısı oranlanarak bulunur. Örnek: 3 : 2 oranlı 100 mL karışımda 60 mL ve 40 mL vardır')
ORN=B('Oranın değerleri','verilen oran, iki çokluğun (ya da çokluğun toplama) bölümüdür; ortak çarpan k ile “a = 2k, b = 3k” yazılır. Örnek: 2 : 3 oranlı 35 kişide 14 ve 21 kişi vardır')
BENUC=B('Benzer üçgenler','paralel doğrularla oluşan üçgenlerin karşılıklı kenarları orantılıdır. Örnek: 6 cm yüksekliğindeki üçgenin tabanı 8 cm ise benzer 3 cm yüksekliğindeki üçgenin tabanı 4 cm’dir')
HIZ=B('Hız, yol, zaman','yol = hız × zaman; aynı sürede alınan yollar hızlarla doğru orantılıdır. Örnek: aynı sürede 80 km ve 60 km yol alan iki aracın hızları 4 : 3 oranındadır')
DOLUM=B('Birlikte dolum','birlikte çalışan musluklar için dolan hacim toplanır; hacim = debi × açık kalma süresi. Örnek: 10 L/dk ve 20 L/dk debili iki musluk 3 dk birlikte açık kalırsa 90 L dolar')
YAY=B('Yay uzaması','esneklik sınırı içinde yayın uzaması asılan kütleyle doğru orantılıdır; toplam boy, uzamaya yayın ilk boyunu eklemekle bulunur. Örnek: 100 g’da 3 cm uzayan yay 200 g’da 6 cm uzar')
TER=B('Terazide denge','eşit kollu terazi dengedeyse iki kefedeki kütleler eşittir; bir cismin kütlesi başka bir cisminkiyle ilişkilendirilerek ortak birimle yazılır. Örnek: 2A = 3B ise 4A = 6B’dir')
ETI=B('Birim değer','100 g’da bulunan miktardan 1 g’daki miktar bulunur; istenen gram sayısıyla çarpılır. Örnek: 100 g’da 400 kcal varsa 25 g’da 100 kcal vardır')

kartla('K-ORB-01','Hız–yol tablosu','Sabit hızda yol, süreyle doğru orantılıdır; iki okumadan hız, hızdan istenen sürenin yolu bulunur.','Saat ve dakika farkını ondalık saat gibi yazmak; yol farkını yönsüz eklemek.','orta','tablo',4,'orb-hizyol','Hız–yol tablosu')
kartla('K-ORB-02','Fotoğraf büyütme','Benzer dikdörtgenlerde kenarlar aynı oranda büyür; büyütme oranı genişlikten bulunur, yükseklik ve çevre hesaplanır.','Aynı sayıyı hem eklemek hem çarpmak; yalnız bir kenarı büyütmek.','kolay','hikâyeli',4,'orb-foto','Fotoğraf büyütme ve çevre')
kartla('K-ORB-03','Karışık sıvı kapları','Her kaptaki maddenin hacmi oran ve kap hacminden bulunur; toplam madde ve toplam hacimle son oran hesaplanır.','Yüzdelerin ortalamasını almak; eklenen suyu toplam hacme katmamak.','orta','hikâyeli',5,'orb-sivi','Karışık sıvı kapları')
kartla('K-ORB-04','Sütun grafiği ve oran','Grafikten ilgili sütunların değeri okunur; verilen oranlar toplam parçaya bölünerek istenen pay bulunur.','Yanlış sütunu okumak; kız ve erkeği karıştırmak.','orta','grafik',4,'orb-sutun','Sütun grafiği ve orantılı pay')
kartla('K-ORB-05','Rampa ve destek','Aynı eğimli rampada yükseklikler, yatay uzaklıklarla doğru orantılıdır; benzer üçgenlerle platform yüksekliği bulunur.','Toplamsal düşünmek; oranı ters kurmak; yatay uzaklık yerine kalan uzaklığı kullanmak.','kolay','hikâyeli',3,'orb-rampa','Rampa eğimi ve benzer üçgenler')
kartla('K-ORB-06','Yol şeması ve buluşma','Aynı sürede alınan yollar hızlarla doğru orantılıdır; buluşma noktasının iki yanındaki uzaklıklardan hız oranı bulunur.','Oranı ters kurmak; yolu hız sanmak; toplamsal düşünmek.','kolay','hikâyeli',3,'orb-yol','Karşılaşma noktası ve hız oranı')
kartla('K-ORB-07','Dolum grafiği','İki doğrunun eğiminden debiler bulunur; geç açılan musluğun gecikmesi hesaba katılarak toplam hacme ulaşılan süre bulunur.','Gecikmeyi unutmak; debiyi gecikmeden hesaplamak; yalnız bir musluğu almak.','zor','grafik',5,'orb-dolum','İki musluklu dolum grafiği')
kartla('K-ORB-08','Yay uzaması','Yayın uzaması kütleyle doğru orantılıdır; ilk boyu çıkararak uzama bulunur.','Toplam boyu kütleyle orantılı sanmak; ilk boyu unutmak.','orta','hikâyeli',4,'orb-yay','Yay uzaması ve kütle')
kartla('K-ORB-09','Teraziler','İki terazideki eşitlikler ortak bir cisimle yazılır; dizi oranları birleştirilir.','Eşitliği ters yazmak; cisim sayısını toplamak.','orta','yeni nesil',4,'orb-terazi','Terazi dengelerinde oran zinciri')
kartla('K-ORB-10','Besin etiketi','Etiketteki 100 g’lık değerden 1 g’daki miktar bulunur; yenen kısımların gramı hesaplanır.','100 g değerini doğrudan kullanmak; yenen kısmı yanlış çıkarmak.','orta','tablo',4,'orb-etiket','Besin etiketi ve gram hesabı')

# ================= 01 · hız–yol tablosu =================
from fractions import Fraction as Fr
t0,t1,t2=8*60,9*60+10,10*60+40; y1,y2=102,210
hiz=Fr(y2-y1,t2-t1); a=y1-hiz*(t1-t0); assert hiz==Fr(6,5) and a==18 and hiz*60==72
e1=[y1-hiz*60*Fr(11,10),hiz*(t1-t0),y1+hiz*(t1-t0),y1-hiz*60]
assert e1==[Fr('22.8'),84,186,30] and len({a,*e1})==5
SK=tablo_svg(['Saat','Kilometre sayacı (km)'],[['08.00','a'],['09.10','102'],['10.40','210']])
q('0001',tipId='orb-hizyol',tip='Hız–yol tablosu',z='orta',alt='Hız ve Yol İlişkisi',kaz='Bir tablodaki iki sayaç okumasından sabit hızı bulup başka bir andaki sayaç değerini hesaplar.',kalip='tablo',sekil=SK,
 kart='K-ORB-01 (hız–yol tablosu) · 09.10’da 102 km, 10.40’ta 210 km → 08.00’de a',
 metin='Bir nakliyeci, İzmir’den çıkan kamyonuyla hiç durmadan ve sabit hızla giderken yol kenarındaki taşlardan kilometre sayacının üç farklı saatteki okumasını not etmiştir. Notlar yukarıdaki tabloda verilmiştir; tabloda a, kamyonun saat 08.00’deki sayaç okumasını göstermektedir.\nBuna göre a kaçtır?',
 dogru=int(a),yan=[(Fr('22.8'),'70 dakikayı 1,1 saat almış: sayaç 72 × 1,1 = 79,2 km geri gitmiş, 102 − 79,2 = 22,8.','dikkat'),(30,'08.00 ile 09.10 arasını 1 saat saymış: 102 − 72 × 1 = 30.','dikkat'),(84,'Bulunan 84 km’lik yolu sayaç okuması sanıp çıkarma yapmamış.','dikkat'),(186,'Yolu çıkarmak yerine eklemiş: 102 + 84 = 186.','islem')],
 istenen='08.00’deki sayaç okuması (km).',
 ip=['Sayacın iki okuması arasındaki yol farkını ve geçen süreyi bul; sonra 08.00 ile 09.10 arasındaki süreyi aynı birimde yaz.'],
 bilgi=[HIZ],
 ad=[A('Hızı bul','İki okuma arasında 90 dakika geçmiştir.','(210 − 102) ÷ 90 = 1,2 km/dk'),A('08.00–09.10 arası','Bu süre 70 dakikadır.','70 × 1,2 = 84 km'),A('Geriye git','Daha önceki saatte sayaç daha küçüktür.','102 − 84 = 18')],
 puf='Saat dakika farkını dakikaya çevir; sabit hızda yol = hız × süre.')

# ================= 02 · fotoğraf büyütme =================
w0,h0,w1=12,18,30; k=Fr(w1,w0); h1=h0*k; d2=2*(w1+h1); assert k==Fr(5,2) and h1==45 and d2==150
e2=[2*(w1+h0*Fr(w0,w1)),2*(w1+(h0+(w1-w0))),2*(w1+h0),w1+h1]
assert e2==[Fr('74.4'),132,96,75] and len({d2,*e2})==5
u=.13
o=[f'\\draw[line width=1.2pt,fill=black!8] (0,0) rectangle ({w0*u:.3f},{h0*u:.3f});',tx(w0*u/2,-.3,'12 cm'),tx(-.55,h0*u/2,'18 cm'),
   ln(w0*u+.5,h0*u/2,w0*u+1.4,h0*u/2,'-{Stealth[length=2mm]}'),tx(w0*u+.95,h0*u/2+.3,'\\footnotesize büyütme'),
   f'\\draw[line width=1.2pt,fill=black!8] ({w0*u+1.9:.3f},0) rectangle ({w0*u+1.9+w1*.1:.3f},{h0*u*w1*.1/(w0*u):.3f});']
bx=w0*u+1.9; bh=h0*u*w1*.1/(w0*u)
o+= [tx(bx+w1*.05,-.3,'30 cm'),tx(bx+w1*.1+.45,bh/2,'$?$')]
SK=fig('\n'.join(o))
q('0002',tipId='orb-foto',tip='Fotoğraf büyütme ve çevre',z='kolay',alt='Benzerlik ve Büyütme',kaz='Dikdörtgen bir fotoğrafın en-boy oranı bozulmadan büyütülmesinde yeni boyutları bulup çevresini hesaplar.',kalip='hikâyeli',sekil=SK,
 kart='K-ORB-02 (fotoğraf büyütme) · 12 × 18 → genişlik 30, çevre 150',
 metin='Bir fotoğrafçı, boyutları yukarıda gösterilen dikdörtgen biçimindeki bir fotoğrafı, en-boy oranını hiç bozmadan büyüterek bir sergi duvarına asacaktır. Büyütülen fotoğrafın genişliği şekilde gösterilmiştir. Şekil ölçekli değildir.\nBuna göre büyütülmüş fotoğrafın çevresi kaç santimetredir?',
 dogru=int(d2),yan=[(Fr('74.4'),'Büyütme oranını ters kurmuş: yükseklik 18 × 12/30 = 7,2; çevre 2 × (30 + 7,2) = 74,4.','dikkat'),(75,'Çevre yerine yarım çevreyi (30 + 45) yazmış.','dikkat'),(96,'Yalnız genişliği büyütüp yüksekliği 18 cm bırakmış: 2 × (30 + 18) = 96.','dikkat'),(132,'Toplamsal düşünmüş: genişlik 18 cm arttığı için yüksekliğe de 18 cm eklemiş (36): 2 × (30 + 36) = 132.','islem')],
 istenen='Büyütülmüş fotoğrafın çevresi (cm).',
 ip=['Genişliğin kaç katına büyütüldüğünü bul; yüksekliği de aynı oranda büyüt.'],
 bilgi=[BEN],
 ad=[A('Büyütme oranını bul','Genişlik 12 cm’den 30 cm’ye çıkmıştır.','30 ÷ 12 = 5/2'),A('Yeni yüksekliği bul','Yükseklik de aynı oranda büyür.','18 × 5/2 = 45 cm'),A('Çevreyi hesapla','Dikdörtgenin çevresi 2 × (genişlik + yükseklik)’tir.','2 × (30 + 45) = 150')],
 puf='Benzer şekillerde her kenar aynı sayıyla çarpılır; toplamsal artış benzerlik değildir.')

# ================= 03 · karışık sıvı kapları =================
vK,(ak,bk),vL,(cl,dl),wsu=600,(1,3),400,(3,1),250
kc=Fr(vK*ak,ak+bk); kw=vK-kc; lc=Fr(vL*cl,cl+dl); lw=vL-lc
assert (kc,kw,lc,lw)==(150,450,300,100)
tot=vK+vL+wsu; W=kw+lw+wsu; d3=W*100/tot; assert d3==64 and tot==1250 and W==800
e3=[100-d3,(kw+lw)*100/(vK+vL),((Fr(kw,vK)+Fr(lw,vL))/2*(vK+vL)+wsu)*100/tot,(kw+lw+wsu)*100/(vK+vL)]
assert e3==[36,55,60,80] and len({d3,*e3})==5
o=[]
def kap(x,v,hh,ad,ora):
    ls=[f'\\draw[line width=1.2pt] ({x},2.9) -- ({x},0) -- ({x+1.5},0) -- ({x+1.5},2.9);',f'\\fill[vurgu!18] ({x+.03},.03) rectangle ({x+1.47},{hh:.3f});',ln(x,hh,x+1.5,hh,'line width=.8pt'),
        tx(x+.75,-.4,f'\\textbf{{{ad}}} · {v} mL'),tx(x+.75,-.85,'\\footnotesize konsantre : su'),tx(x+.75,-1.25,f'\\footnotesize {ora}')]
    return ls
o+=kap(0,600,2.4,'K','1 : 3'); o+=kap(3.2,400,1.6,'L','3 : 1')
SK=fig('\n'.join(o))
q('0003',tipId='orb-sivi',tip='Karışık sıvı kapları',z='orta',alt='Karışım Problemleri',kaz='İki kaptaki oranlı karışımların hacimlerini bulup birleştirir, eklenen su ile son karışımın su yüzdesini hesaplar.',kalip='hikâyeli',sekil=SK,
 kart='K-ORB-03 (karışık sıvı kapları) · 600 mL (1:3) + 400 mL (3:1) + 250 mL su',
 metin='Bir meyve suyu atölyesinde K ve L kaplarında hacimce farklı oranlarda hazırlanmış konsantre–su karışımları vardır; kapların hacimleri ve oranları yukarıda gösterilmiştir. İki kaptaki karışımın tamamı büyük bir tanka boşaltılıyor ve üzerine 250 mL saf su ekleniyor. Karışırken hacim kaybı olmamaktadır.\nBuna göre tanktaki karışımın hacimce yüzde kaçı sudur?',
 dogru=int(d3),yan=[(36,'Su yerine konsantrenin yüzdesini yazmış: 100 − 64 = 36.','dikkat'),(55,'Eklenen 250 mL suyu hesaba katmamış: 550 ÷ 1000 = %55.','dikkat'),(60,'İki kabın su yüzdelerinin ortalamasını (75 ve 25 → %50) alıp hacimleri hesaba katmamış: (500 + 250) ÷ 1250 = %60.','dikkat'),(80,'Eklenen suyu toplam hacme katmamış: (550 + 250) ÷ 1000 = %80.','dikkat')],
 istenen='Tanktaki karışımın su yüzdesi.',
 ip=['Her kaptaki su ve konsantre miktarını mililitre olarak bul; sonra eklenen suyla toplam su ve toplam hacmi yaz.'],
 bilgi=[KAR],
 ad=[A('K kabındaki su','K’de toplam 4 parça vardır ve 3 parçası sudur.','600 × 3/4 = 450 mL su'),A('L kabındaki su','L’de toplam 4 parça vardır ve 1 parçası sudur.','400 × 1/4 = 100 mL su'),A('Toplam su','İki kaptaki su ve eklenen su toplanır.','450 + 100 + 250 = 800 mL'),A('Toplam hacim','İki kaptaki karışım ve eklenen su toplanır.','600 + 400 + 250 = 1250 mL'),A('Yüzdeyi bul','Su miktarı toplam hacme oranlanır.','800 ÷ 1250 = %64')],
 puf='Oranlı karışımlarda yüzdeleri değil, her kaptaki madde miktarını (hacmi) topla; sonra toplam hacme böl.')

# ================= 04 · sütun grafiği ve oran =================
KL=[('Satranç',18),('Tiyatro',35),('Robotik',42),('Resim',24)]
tiy=KL[1][1]; rob=KL[2][1]
kiz_t=Fr(tiy*2,5); kiz_r=Fr(rob*4,7); er_t=Fr(tiy*3,5); er_r=Fr(rob*3,7)
d4=kiz_t+kiz_r; assert (kiz_t,kiz_r,d4)==(14,24,38)
e4=[er_t+er_r,tiy+rob,kiz_r,kiz_t]; assert e4==[39,77,24,14] and len({d4,*e4})==5
sx=1.3; sy=.075
o=[]
for t in range(0,50,5): o.append(ln(0,t*sy,4*sx+.1,t*sy,'black!15,line width=.4pt')); o.append(tx(-.3,t*sy,f'\\footnotesize {t}'))
o+=[ln(0,0,0,47*sy,'line width=1pt'),ln(0,0,4*sx+.1,0,'line width=1.2pt'),tx(-.1,47*sy+.3,'\\footnotesize Öğrenci sayısı')]
for i,(n_,v) in enumerate(KL):
    x=.2+i*sx; o.append(f'\\fill[vurgu!45] ({x:.3f},0) rectangle ({x+.7:.3f},{v*sy:.3f});'); o.append(tx(x+.35,-.3,f'\\footnotesize {n_}'))
SK=fig('\n'.join(o))
q('0004',tipId='orb-sutun',tip='Sütun grafiği ve orantılı pay',z='orta',alt='Oran ve Orantılı Bölme',kaz='Sütun grafiğinden okunan sayıları verilen oranlara göre paylara ayırıp istenen grubun toplamını bulur.',kalip='grafik',sekil=SK,
 kart='K-ORB-04 (sütun grafiği) · Tiyatro 35 (2:3), Robotik 42 (4:3) kız toplamı',
 metin='Bir lisede dört kulübe kayıtlı öğrencilerin sayıları yukarıdaki sütun grafiğinde verilmiştir. Her öğrenci yalnız bir kulübe üyedir. Tiyatro kulübünde kız öğrencilerin sayısının erkek öğrencilerin sayısına oranı 2/3, Robotik kulübünde ise 4/3’tür.\nBuna göre bu iki kulüpteki kız öğrencilerin sayıları toplamı kaçtır?',
 dogru=int(d4),yan=[(14,'Yalnız Tiyatro kulübünün kız öğrencilerini hesaplamış.','dikkat'),(24,'Yalnız Robotik kulübünün kız öğrencilerini hesaplamış.','dikkat'),(39,'Kız yerine erkek öğrencilerin sayısını toplamış: 21 + 18 = 39.','dikkat'),(77,'İki kulübün toplam öğrenci sayısını yazmış: 35 + 42 = 77.','dikkat')],
 istenen='Tiyatro ve Robotik kulüplerindeki kız öğrenci sayıları toplamı.',
 ip=['Grafikten iki kulübün öğrenci sayısını oku; her kulüp için oranın parça toplamına göre kız öğrenci sayısını bul.'],
 bilgi=[ORN],
 ad=[A('Sayıları oku','Grafikte Tiyatro 35, Robotik 42 öğrencidir.','35 ve 42'),A('Tiyatroda kız','Oran 2/3 olduğundan toplam 5 parçadır ve 2 parçası kızdır.','35 × 2/5 = 14'),A('Robotikte kız','Oran 4/3 olduğundan toplam 7 parçadır ve 4 parçası kızdır.','42 × 4/7 = 24'),A('Topla','İki kulüpteki kız sayıları toplanır.','14 + 24 = 38')],
 puf='“Kız sayısının erkek sayısına oranı 2/3” ise toplam 5 parçadır; kız sayısı toplamın 2/5’idir.')

# ================= 05 · rampa ve destek =================
AE,DE,AC=6,80,15; d5=Fr(DE*AC,AE); assert d5==200
e5=[Fr(DE*AE,AC),Fr(DE*(AC-AE),AE),DE+(AC-AE)*100,DE*AC]
assert e5==[32,120,980,1200] and len({d5,*e5})==5
o=[ln(0,0,6.4,0,'line width=1.2pt'),ln(0,0,6.4,1.7,'line width=1.8pt,vurgu'),ln(6.4,0,6.4,1.7,'line width=1.2pt'),ln(2.0,0,2.0,.54,'line width=1.2pt'),
   '\\draw (1.8,0) -- (1.8,.2) -- (2.0,.2); \\draw (6.2,0) -- (6.2,.2) -- (6.4,.2);',
   '\\fill (2.0,.54) circle (.05);',
   tx(-.25,-.1,'A'),tx(2.0,-.3,'E'),tx(6.65,-.1,'C'),tx(6.65,1.8,'B'),tx(1.8,.75,'D'),
   ln(2.3,0,2.3,.62,'<->'),tx(2.95,.25,'\\footnotesize 80 cm'),
   ln(0,-.7,2.0,-.7,'<->'),tx(1.0,-1.0,'\\footnotesize 6 m'),ln(0,-1.45,6.4,-1.45,'<->'),tx(3.2,-1.75,'\\footnotesize 15 m')]
SK=fig('\n'.join(o))
q('0005',tipId='orb-rampa',tip='Rampa eğimi ve benzer üçgenler',z='kolay',alt='Benzer Üçgenlerle Orantı',kaz='Düz bir rampada destek yüksekliği ve yatay uzaklıklardan benzer üçgenlerle platform yüksekliğini bulur.',kalip='hikâyeli',sekil=SK,
 kart='K-ORB-05 (rampa ve destek) · AE = 6 m, DE = 80 cm, AC = 15 m → BC = 200 cm',
 metin='Bir spor salonunun girişine, A noktası yerde, B noktası platformda olacak biçimde düz bir rampa yapılmıştır. Rampanın D noktasının altına, yere dik bir destek konmuştur. ABC ve ADE üçgenlerindeki ölçüler şekilde verilmiştir. Şekil ölçekli değildir.\nBuna göre platformun yerden yüksekliği olan |BC| kaç santimetredir?',
 dogru=int(d5),yan=[(32,'Oranı ters kurmuş: 80 × 6 ÷ 15 = 32.','dikkat'),(120,'Yatay uzaklık olarak 15 m yerine EC = 9 m’yi alıp 80 × 9 ÷ 6 işlemini yapmış.','dikkat'),(980,'Toplamsal düşünmüş: kalan yatay uzaklığı (9 m = 900 cm) destek yüksekliğine eklemiş: 80 + 900.','dikkat'),(1200,'Oran kurmadan destek yüksekliğini 15 ile çarpmış: 80 × 15.','islem')],
 istenen='|BC| uzunluğu (cm).',
 ip=['ADE ve ABC üçgenlerinin benzerliğinden yatay uzaklıkların oranını yüksekliklerin oranıyla eşleştir.'],
 bilgi=[BENUC],
 ad=[A('Benzerliği yaz','DE ve BC paraleldir; yükseklikler yatay uzaklıklarla orantılıdır.','|DE| / |BC| = |AE| / |AC|'),A('Değerleri yerleştir','AE = 6 m, AC = 15 m, DE = 80 cm.','80 / |BC| = 6 / 15'),A('Çöz','İçler dışlar çarpımı yapılır.','|BC| = 80 × 15 ÷ 6 = 200 cm')],
 puf='Paralel doğrular benzer üçgen oluşturur; karşılıklı kenarların oranı yukarıda ya da aşağıda aynıdır.')

# ================= 06 · yol şeması ve buluşma =================
AK,KB,vA=100,60,120
vB=Fr(vA*KB,AK); assert vB==72
e6=[vA-(AK-KB),Fr(vA*AK,KB),KB,AK+KB-vA]
assert e6==[80,200,60,40] and len({vB,*e6})==5
o=[ln(0,0,7.6,0,'line width=1.2pt'),'\\fill (0,0) circle (.07); \\fill (4.4,0) circle (.07); \\fill (7.6,0) circle (.07);',
   tx(0,-.35,'A'),tx(4.4,-.35,'K'),tx(7.6,-.35,'B'),
   ln(.2,.55,4.2,.55,'<->'),tx(2.2,.9,'100 km'),ln(4.6,.55,7.4,.55,'<->'),tx(6.0,.9,'60 km'),
   ln(.2,-.9,1.5,-.9,'-{Stealth[length=2mm]}'),tx(.8,-1.2,'\\footnotesize 1. araç'),ln(7.4,-.9,6.1,-.9,'-{Stealth[length=2mm]}'),tx(6.8,-1.2,'\\footnotesize 2. araç')]
SK=fig('\n'.join(o))
q('0006',tipId='orb-yol',tip='Karşılaşma noktası ve hız oranı',z='kolay',alt='Hız ve Yol İlişkisi',kaz='İki aracın karşılaşma noktasının iki yanındaki uzaklıklardan hızlar arasındaki orantıyı kurup bilinmeyen hızı bulur.',kalip='hikâyeli',sekil=SK,
 kart='K-ORB-06 (yol şeması) · AK = 100 km, KB = 60 km, hızı 120 olan araç',
 metin='A ve B kentlerinden aynı anda birbirlerine doğru yola çıkan iki otomobil, yolun K noktasında karşılaşmıştır. Otomobiller yolculuk boyunca sabit hızla gitmiştir ve A kentinden çıkan otomobilin hızı saatte 120 kilometredir. Yolun ölçüleri yukarıdaki şemada verilmiştir.\nBuna göre B kentinden çıkan otomobilin hızı saatte kaç kilometredir?',
 dogru=int(vB),yan=[(40,'Toplam yoldan (160) A’dan çıkan aracın hızını çıkarmış: 160 − 120 = 40.','dikkat'),(60,'KB yolunun uzunluğunu (60 km) hız sanmış.','dikkat'),(80,'Toplamsal düşünmüş: yollar arasındaki farkı (40 km) hızdan çıkarmış: 120 − 40 = 80.','dikkat'),(200,'Oranı ters kurmuş: 120 × 100 ÷ 60 = 200.','dikkat')],
 istenen='B’den çıkan otomobilin hızı (km/sa).',
 ip=['Karşılaşma anına kadar iki otomobilin geçen süresi nasıl karşılaştırılır?'],
 bilgi=[B('Hız, yol, zaman','yol = hız × zaman’dır. Örnek: 60 km/sa hızla 3 saat giden araç 180 km yol alır')],
 ad=[A('Aynı süreyi yaz','Karşılaşmaya kadar iki araç da aynı süre gitmiştir; yollar hızlarla doğru orantılıdır.','100 / 60 = 120 / v'),A('Orantıyı kur','1. aracın yolu 100 km, 2. aracın yolu 60 km’dir.','v = 120 × 60 ÷ 100'),A('Hızı bul','İşlem yapılır.','v = 72 km/sa')],
 puf='Aynı sürede alınan yollar hızlarla doğru orantılıdır; yolu fazla olanın hızı da fazladır.')

# ================= 07 · dolum grafiği =================
r1=Fr(90,6); r2=Fr(150,10-4); assert (r1,r2)==(15,25)
V=540; d7=4+Fr(V-r1*4,r1+r2); assert d7==16 and r1*16+r2*(16-4)==V
e7=[Fr(V,r1+r2),Fr(V,r1+r2)+4,Fr(V,15+30)*0+Fr(V,Fr(90,6)+Fr(150,10)),Fr(V,r1)]
assert e7==[Fr('13.5'),Fr('17.5'),18,36] and len({d7,*e7})==5
sx=.3; sy=.012
o=[]
for t in range(0,21,2): o.append(ln(t*sx,0,t*sx,300*sy,'black!12,line width=.4pt')); o.append(tx(t*sx,-.3,f'\\footnotesize {t}'))
for v in range(0,301,50): o.append(ln(0,v*sy,20*sx,v*sy,'black!12,line width=.4pt')); o.append(tx(-.35,v*sy,f'\\footnotesize {v}'))
o+=[ln(0,0,20*sx,0,'line width=1.2pt'),ln(0,0,0,300*sy,'line width=1.2pt'),tx(20*sx+.5,0,'\\footnotesize dk'),tx(0,300*sy+.3,'\\footnotesize Hacim (L)'),
 ln(0,0,18*sx,270*sy,'line width=1.8pt'),ln(4*sx,0,14*sx,250*sy,'line width=1.8pt,vurgu'),
 f'\\fill (6*{sx},90*{sy}) circle (.07); \\fill (10*{sx},150*{sy}) circle (.07);',
 tx(18*sx+.2,270*sy+.25,'\\footnotesize 1. musluk'),tx(14*sx+.15,250*sy+.25,'\\footnotesize 2. musluk')]
SK=fig('\n'.join(o))
q('0007',tipId='orb-dolum',tip='İki musluklu dolum grafiği',z='zor',alt='Bileşik Orantı ve Debi',kaz='Grafikteki iki doğrudan debileri bulup geç açılan musluğun gecikmesini hesaba katarak havuzun dolma süresini bulur.',kalip='grafik',sekil=SK,
 kart='K-ORB-07 (dolum grafiği) · debiler 15 ve 25 L/dk, 2. musluk 4 dk geç, 540 L',
 metin='Boş bir su deposunu dolduran iki musluğun, açıldıkları andan itibaren depoya akıttığı su miktarlarının zamanla değişimi yukarıdaki grafikte gösterilmiştir. Musluklar sabit debiyle çalışmaktadır; iki musluk da dolana kadar açık kalmıştır ve depodan su çıkışı yoktur. Deponun hacmi 540 litredir.\nBuna göre depo, 1. musluğun açılmasından kaç dakika sonra dolar?',
 dogru=int(d7),yan=[(Fr('13.5'),'2. musluğun geç açıldığını görmemiş; iki musluğu baştan birlikte sayıp 540 ÷ 40 = 13,5 bulmuş.','dikkat'),(Fr('17.5'),'Gecikmeyi sonuca eklemiş: 13,5 + 4 = 17,5 (musluk 4 dk çalışmadığı için su eksiğini hesaba katmamış).','dikkat'),(18,'2. musluğun debisini 150 L ÷ 10 dk = 15 L/dk sanmış (açılış anını hesaba katmamış): 540 ÷ 30 = 18.','dikkat'),(36,'Yalnız 1. musluğu hesaba katmış: 540 ÷ 15 = 36.','dikkat')],
 istenen='Deponun dolma süresi (dk).',
 ip=['Grafikteki noktalardan iki musluğun debisini bul; 2. musluğun hangi dakikada akmaya başladığına dikkat et.'],
 bilgi=[DOLUM],
 ad=[A('1. musluğun debisi','Doğru orijinden geçer; 6. dakikada 90 L akmıştır.','90 ÷ 6 = 15 L/dk'),A('2. musluğun debisi','Doğru 4. dakikada başlar; 10. dakikada 150 L akmıştır; 6 dakikada.','150 ÷ 6 = 25 L/dk'),A('Denklemi kur','t dk sonunda 1. musluk 15t, 2. musluk 25(t − 4) litre akıtır.','15t + 25(t − 4) = 540'),A('Çöz','Parantez açılır ve düzenlenir.','40t − 100 = 540 → t = 16'),A('Denetle','16 dk’da 1. musluk 240 L, 2. musluk 12 dk’da 300 L akıtır.','240 + 300 = 540')],
 puf='Geç açılan musluk için süre, açılış anından itibaren (t − gecikme) olarak alınır; debi bu süre aralığında hesaplanır.')

# ================= 08 · yay uzaması =================
L0,m1,l1,m2,l2,Lh=20,100,25,300,35,50
ek=Fr(l1-L0,m1); assert ek==Fr(l2-L0,m2)==Fr(1,20)
d8=(Lh-L0)/ek; assert d8==600
e8=[Lh*Fr(m1,l1),(Lh-l2)/ek,(Lh-l1)/ek,Lh/ek]
assert e8==[200,300,500,1000] and len({d8,*e8})==5
sc=.1; o=[ln(-.4,3.6,8.4,3.6,'line width=1.4pt')]
def yay(x,L,m):
    top=3.6; bot=top-L*sc; ls=[]; n=10; pts=[(x,top),(x,top-.15*sc*10)]
    ys=[top-.15-(i+.5)*(L*sc-.3)/n for i in range(n)]
    p=f'({x},{top}) -- ({x},{top-.15})'
    for i,y in enumerate(ys): p+=f' -- ({x+(.22 if i%2==0 else -.22):.3f},{y:.3f})'
    p+=f' -- ({x},{bot+.15}) -- ({x},{bot})'
    ls.append(f'\\draw[line width=1.1pt] {p};')
    if m: ls.append(f'\\draw[fill=black!10,line width=1pt] ({x-.4},{bot-.5}) rectangle ({x+.4},{bot}); '+tx(x,bot-.25,f'\\footnotesize {m} g'))
    ls.append(ln(x+.9,top,x+.9,bot,'<->'))
    ls.append(tx(x+1.5,(top+bot)/2,f'\\footnotesize {L} cm')); return ls
o+=yay(.5,L0,0)+yay(3.5,l1,m1)+yay(6.5,l2,m2)
SK=fig('\n'.join(o))
q('0008',tipId='orb-yay',tip='Yay uzaması ve kütle',z='orta',alt='Doğru Orantı',kaz='Farklı kütlelerde ölçülen yay boylarından uzamanın kütleyle orantısını bulup verilen boy için kütleyi hesaplar.',kalip='hikâyeli',sekil=SK,
 kart='K-ORB-08 (yay uzaması) · 20 cm, 100 g → 25 cm, 300 g → 35 cm, boy 50 cm → 600 g',
 metin='Fen laboratuvarında bir öğrenci, aynı yayı yüksüz, 100 gram ve 300 gram kütleyle yüklediğinde ölçtüğü yay boylarını yukarıdaki şekilde göstermiştir. Yay, bu denemelerde esneklik sınırı içinde kalmıştır ve uzaması asılan kütleyle doğru orantılıdır. Öğrenci aynı yaya şimdi daha büyük bir kütle asacaktır.\nBuna göre yayın boyu 50 cm olduğu anda yayda asılı olan kütle kaç gramdır?',
 dogru=int(d8),yan=[(200,'Toplam boyun kütleyle orantılı olduğunu sanmış: 100 g’da 25 cm ise 50 cm için 200 g.','dikkat'),(300,'300 g’lık okumadan başlayıp uzama farkını kütle sanmış: (50 − 35) × 20 = 300 (ilk kütleyi eklememiş).','dikkat'),(500,'100 g’lık okumadan başlayıp yeni uzama kadar kütleyi bulmuş fakat 100 g’ı eklememiş: (50 − 25) × 20 = 500.','dikkat'),(1000,'İlk boyu hesaba katmamış: 50 cm tamamen uzama sanılmış, 50 × 20 = 1000.','dikkat')],
 istenen='Yayda asılı olan kütle (g).',
 ip=['Yüksüz boy ile yüklü boylar arasındaki farktan, bir gramın yayı ne kadar uzattığını bul.'],
 bilgi=[YAY],
 ad=[A('Uzamayı bul','Uzama, yüklü boydan yüksüz boy çıkarılarak bulunur.','100 g: 25 − 20 = 5 cm · 300 g: 35 − 20 = 15 cm'),A('Birim uzamayı bul','5 cm’lik uzama 100 g’a aittir; 15 cm 300 g’a aittir.','1 cm uzama = 20 g'),A('50 cm’de uzama','Yayın boyu 50 cm olunca uzama 30 cm’dir.','50 − 20 = 30 cm'),A('Kütleyi bul','Uzama birim uzamayla çarpılır.','30 × 20 = 600 g')],
 puf='Yayda orantı uzama ile kütle arasındadır; toplam boy ile değil. Önce yüksüz boyu çıkar.')

# ================= 09 · teraziler =================
a_,b_,c_,d_,x_,y_=2,3,5,2,6,1
dogru9=Fr(x_*b_*d_,a_*c_)+Fr(y_*d_,c_)  # 2K=3L → K=3/2 L ; 5L=2M → L=2/5 M
assert dogru9==4
def v(a,b,c,d): return x_*Fr(b,a)*Fr(d,c)+y_*Fr(d,c)
e9=[v(b_,a_,c_,d_),v(a_,b_,d_,c_),v(b_,a_,d_,c_),x_+y_]
assert e9==[2,25,Fr('12.5'),7] and len({dogru9,*e9})==5
def blok(x,y,h,r=.38):
    f={'K':'black!15','L':'vurgu!30','M':'white'}[h]
    return f'\\draw[fill={f},line width=.8pt] ({x:.3f},{y:.3f}) rectangle ({x+r:.3f},{y+r:.3f}); '+tx(x+r/2,y+r/2,f'\\footnotesize {h}')
def terazi(cx,sol,sag):
    ls=[f'\\draw[line width=1.2pt] ({cx},1.4) -- ({cx-.5},-.9) -- ({cx+.5},-.9) -- cycle;',ln(cx-2.2,1.4,cx+2.2,1.4,'line width=1.6pt')]
    for sg,ic,xo in [(-1,sol,cx-1.7),(1,sag,cx+1.7)]:
        ls+= [ln(xo-.75,1.4,xo-.75,-.1),ln(xo+.75,1.4,xo+.75,-.1),ln(xo-.8,-.1,xo+.8,-.1,'line width=1.6pt')]
        n=len(ic); 
        for i,h in enumerate(ic):
            r_,c_=divmod(i,3); ls.append(blok(xo-.57+c_*.38,-.1+r_*.38,h))
    return ls
SK=fig('\n'.join(terazi(0,'KK','LLL')+terazi(5.6,'LLLLL','MM')))
q('0009',tipId='orb-terazi',tip='Terazi dengelerinde oran zinciri',z='orta',alt='Ortak Terimle Oranlar',kaz='İki terazideki eşitliklerden üç cismin kütleleri arasındaki ilişkiyi bulup bir kefedeki cisimlere denk gelen sayıyı hesaplar.',kalip='yeni nesil',sekil=SK,
 kart='K-ORB-09 (teraziler) · 2K = 3L ve 5L = 2M → 6K + L = 4M',
 metin='Bir bilim atölyesinde eşit kollu iki terazi, yukarıda gösterildiği gibi dengede durmaktadır. Aynı harfle gösterilen cisimler özdeştir ve tartılan cisimlerin dışında kefelerde başka bir şey yoktur.\nBuna göre bir kefesine 6 tane K ve 1 tane L konulan eşit kollu bir terazinin dengede kalması için öteki kefesine kaç tane M konulmalıdır?',
 dogru=int(dogru9),yan=[(2,'İlk dengeyi ters okumuş (3K = 2L): 6K = 4L, 4L + L = 5L = 2M.','dikkat'),(7,'Cisimlerin sayılarını toplamış: 6 + 1 = 7.','dikkat'),(Fr('12.5'),'Her iki dengeyi de ters okumuş: 3K = 2L ve 2L = 5M; 5L, 12,5 M eder.','dikkat'),(25,'İkinci dengeyi ters okumuş (2L = 5M): 10L = 25M.','dikkat')],
 istenen='Dengeyi sağlayan M sayısı.',
 ip=['K’yi L cinsinden, sonra L’yi M cinsinden yaz; kefedeki bütün cisimleri tek cisimle ifade et.'],
 bilgi=[TER],
 ad=[A('K’yi L ile yaz','İlk dengede 2K = 3L’dir.','6K = 9L'),A('Kefeyi tek cinse çevir','L’leri topla.','6K + L = 9L + L = 10L'),A('L’yi M ile yaz','İkinci dengede 5L = 2M’dir.','10L = 4M'),A('Sonucu yaz','Öteki kefeye M konulur.','4 tane M')],
 puf='Terazi eşitliklerini ortak bir cisimle yaz; kefedeki hepsini aynı cins cinsinden toplayıp sonra dönüştür.')

# ================= 10 · besin etiketi =================
en100,net,yen,por=520,250,40,2
kalan=net-por*yen; kardes=Fr(kalan,2); d10=kardes*en100/100; assert (kalan,kardes,d10)==(170,85,442)
e10=[kalan*en100/100,Fr(net,2)*en100/100,en100,por*yen*en100/100]
assert e10==[884,650,520,416] and len({d10,*e10})==5
SK=tablo_svg(['Besin öğesi','100 g’da'],[['Enerji','520 kcal'],['Protein','8 g'],['Karbonhidrat','64 g'],['Yağ','26 g'],['Net miktar','250 g (paketin tamamı)']])
q('0010',tipId='orb-etiket',tip='Besin etiketi ve gram hesabı',z='orta',alt='Doğru Orantı',kaz='Etiketteki 100 g başına enerji değerinden yenen miktarın enerjisini hesaplar.',kalip='tablo',sekil=SK,
 kart='K-ORB-10 (besin etiketi) · 250 g paket, 2 × 40 g, kalanın yarısı → enerji',
 metin='Bir bisküvi paketinin üzerindeki besin değerleri etiketi yukarıdaki tabloda verilmiştir. Ali, paketten 40 gramlık iki porsiyon yemiş; kalan bisküvilerin yarısını da kardeşine vermiştir. Kardeşi, kendisine verilen bisküvilerin tamamını yemiştir ve paketin içinde başka bir şey yoktur.\nBuna göre kardeşinin yediği bisküvilerden aldığı enerji kaç kilokaloridir?',
 dogru=int(d10),yan=[(416,'Kardeşi yerine Ali’nin yediği miktarı hesaplamış: 80 g için 80 × 5,2 = 416.','dikkat'),(520,'100 g’lık etiket değerini doğrudan kardeşin enerjisi sanmış.','dikkat'),(650,'Paketin yarısını (125 g) kardeşin payı sanmış, Ali’nin yediklerini düşmemiş: 125 × 5,2 = 650.','dikkat'),(884,'Kalan 170 g’ın tamamını kardeşin yediği sanmış (yarısını almamış): 170 × 5,2 = 884.','dikkat')],
 istenen='Kardeşinin aldığı enerji (kcal).',
 ip=['Önce kardeşine verilen bisküvinin kaç gram olduğunu bul; sonra 1 gramın enerjisini hesapla.'],
 bilgi=[ETI],
 ad=[A('Ali’nin yediği','İki porsiyon 40 gramlıktır.','2 × 40 = 80 g'),A('Kalanı bul','Paketin tamamından Ali’nin yedikleri çıkarılır.','250 − 80 = 170 g'),A('Kardeşin payı','Kalanın yarısı verilmiştir.','170 ÷ 2 = 85 g'),A('Enerjiyi bul','100 g’da 520 kcal olduğundan 1 g’da 5,2 kcal vardır.','85 × 5,2 = 442 kcal')],
 puf='Etiket değerleri 100 g içindir; önce yenen gramı bul, sonra gram başına değerle çarp.')

bitir(P,'oransekb','mat|Oran Orantı')
