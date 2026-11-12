"""Oran Orantı · parti 2 (hafif mod): 19 ana soru, kardeş yok, ipucu 1. Her cevap ve çeldirici kodla doğrulanır."""
import sys,os,math
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_mat as H
from _hafif_mat import *
H.KONU='Oran Orantı'
UK='mat|Oran Orantı'
P=Parti('oraniki','Oran Orantı',UK)
ORAN=B('Oranı k ile yazmak','a/3 = b/4 ise ortak değere k denir: a = 3k, b = 4k. Örnek: a/3 = b/4 ve a + b = 14 ise 7k = 14, k = 2 → a = 6, b = 8')
OZ=B('Oran özelliği','a/b = c/d = k ise (m·a + n·c)/(m·b + n·d) = k olur. Örnek: 1/2 = 3/6 ise (1 + 3)/(2 + 6) = 4/8 = 1/2')
DOGRU=B('Doğru orantı','biri kaç katına çıkarsa diğeri de o kadar katına çıkar; oranları sabittir. Örnek: 2 kg 60 TL ise 6 kg 180 TL')
TERS=B('Ters orantı','biri kaç katına çıkarsa diğeri o kadar kata bölünür; çarpımları sabittir. Örnek: 4 kişi 6 günde bitiriyorsa 8 kişi 3 günde bitirir (4 × 6 = 8 × 3)')
BIL=B('Bileşik orantı','işçi sayısı, gün ve günlük saat çarpımı (toplam işçi–saat) iş miktarına eşittir. Örnek: 3 işçi günde 4 saat 5 gün çalışırsa 3 × 4 × 5 = 60 işçi–saat iş yapar')
PAYD=B('Doğru orantılı paylaştırma','2, 3 ve 5 ile doğru orantılı paylar 2k, 3k ve 5k’dir. Örnek: toplam 100 ise 10k = 100, k = 10 → 20, 30, 50')
PAYT=B('Ters orantılı paylaştırma','2, 3 ve 6 ile ters orantılı paylar 1/2, 1/3 ve 1/6 ile doğru orantılıdır; paydalar eşitlenince 3 : 2 : 1 olur. Örnek: toplam 60 ise 6k = 60, k = 10 → 30, 20, 10')
ORTB=B('Aritmetik ortalama','sayıların toplamı ÷ adedi aritmetik ortalamadır; toplam = ortalama × adet. Örnek: 4, 6 ve 11’in ortalaması 21 ÷ 3 = 7, toplamları 7 × 3 = 21')
OLC=B('Ölçek','1/250 000 ölçeğinde haritadaki 1 cm gerçekte 250 000 cm’dir. 1 km = 1000 m = 100 000 cm. Örnek: 2 cm → 500 000 cm = 5 km')
KAR=B('Karışım oranı','su : limon = 7 : 2 ise karışımın 9 parçasının 7’si su, 2’si limondur. Örnek: 18 L karışımda bir parça 2 L, limon 4 L’dir')
HIZ=B('Yol, hız, süre','yol = hız × süre. Yol sabitse hız ile süre ters orantılıdır. Örnek: 60 km/sa ile 4 saatte alınan 240 km’lik yol 80 km/sa ile 3 saatte alınır')
DIS=B('Dişlilerde dönme','kenetli iki dişlide (diş sayısı × tur sayısı) eşittir; yani diş sayısı ile tur sayısı ters orantılıdır. Aynı mildeki dişliler birlikte döner. Örnek: 20 dişli 6 tur atarsa kenetli 30 dişli 4 tur atar')
KUR=B('Kur ile çevirme','1 dolar = 32 TL ise 640 dolar = 640 × 32 TL’dir. Bir parayı başka parayla ifade etmek için önce TL’ye, sonra TL’yi hedef paranın kuruna bölünür. Örnek: 1 euro = 40 TL ise 80 TL = 80 ÷ 40 = 2 euro')
TAR=B('Tarif ölçekleme','tarifteki her malzeme kişi sayısıyla doğru orantılıdır; kişi başına düşen miktar bulunur. Örnek: 6 kişilik 450 g un → kişi başı 75 g')

KY='ÖSYM 2018–2026 TYT Matematik (oran, orantı, ortalama) · yayın soru bankaları (yalnız mantık) · MEB 7–9. sınıf'
kart('K-ORNB-01','Oran–orantı özellikleri','a/b = c/d = k özelliklerinden katsayılı toplam–oranlar ve üçlü eşit oranlar çözülür.','Oranı payla paydayı karıştırmak; ortak değeri (k) bulmayıp doğrudan toplamı bölmek; katsayıları atlamak.','kolay','düz',2,'orb-oran','Oran ve orantı özellikleri (a/b = c/d = k)',KY)
kart('K-ORNB-02','Doğru ve ters orantı (tablo)','Tabloda verilen iki çokluğun doğru ya da ters orantılı olduğu belirlenip eksik değerler bulunur.','Ters orantıyı doğru orantı gibi kurmak; tabloda eksik değerlerden yalnızca birini bulup durmak.','kolay','tablo',3,'orb-dogruters','Doğru ve ters orantı: tablo',KY)
kart('K-ORNB-03','Bileşik orantı','İşçi, gün ve günlük saat çarpımıyla iş miktarı sabit tutulur; ortada işçi ekleme gibi değişimler iş miktarı bölümlenerek çözülür.','Her çokluğu yalnız tek başına orantılamak; doğru–ters ayrımını karıştırmak; çalışılan işi ayırmamak.','orta','hikâyeli',3,'orb-bilesik','Bileşik orantı (işçi–gün–saat)',KY)
kart('K-ORNB-04','Orantılı paylaştırma','Doğru, ters ve karışık orantılı paylaştırmada payların ortak oranı bulunup bir veri üzerinden toplam hesaplanır.','Ters orantılıyı doğru orantılı paylaştırmak; fark bilgisini bir parça sanmak.','kolay','hikâyeli',3,'orb-paylastirma','Doğru ve ters orantılı paylaştırma',KY)
kart('K-ORNB-05','Aritmetik ortalama','Toplam = ortalama × adet ilişkisiyle eleman ekleme ve çıkarma sorularında ortalamanın değişimi çözülür; toplam ve çarpımdan sayılar bulunur.','Toplam yerine ortalamayla işlem yapmak; çıkan sayının ortalamasını ortalama farkı sanmak; fark için karekökü unutmak.','kolay','düz',3,'orb-ortalama','Aritmetik ortalama değişimi',KY)
kart('K-ORNB-06','Ölçek','Haritadaki uzunluk ve ölçekten gerçek uzaklık bulunur; birim dönüşümü (cm–km) yapılır.','Santimetreden kilometreye geçişte sıfır sayısını yanlış almak.','kolay','hikâyeli',2,'orb-olcek','Ölçek ve harita',KY)
kart('K-ORNB-07','Karışım oranı','Parça sayısı toplamı üzerinden karışımın bileşenleri hesaplanır.','Oranı kesir olarak karıştırıp parça yerine toplamı kullanmak; yanlış bileşeni vermek.','kolay','hikâyeli',2,'orb-karisim','Karışım ve tarif oranı',KY)
kart('K-ORNB-08','Hız–zaman ters orantısı','Yol sabitken hız ile süre ters orantılıdır; gidiş–dönüş yolculuklarında ortalama hız toplam yol ÷ toplam süre ile bulunur.','Hızı ve süreyi doğru orantılı almak; ortalama hızı hızların aritmetik ortalaması sanmak; farkla yeni değeri karıştırmak.','kolay','hikâyeli',2,'orb-hiz','Hız–zaman ters orantısı',KY)
kart('K-ORNB-09','Yeni nesil: dişli, kur, tarif','Dişli çevrimi, kur çevirme ve tarif ölçekleme gibi günlük bağlamlı orantı kurguları adım adım çözülür.','Dişlilerde diş sayısı ile tur sayısını doğru orantılı almak; kuru ters kullanmak; en kısıtlayıcı malzemeyi gözden kaçırmak.','zor','yeni nesil',4,'orb-yeninesil','Yeni nesil orantı: dişli, kur çevirme, tarif',KY)
kart('K-ORNB-10','Öncüllü oran','Ortak terimle birleştirilen oranlardan çıkan değerler üzerinden öncüller kesinlikle doğru mu diye sınanır.','k = 1 gibi tek bir değerle yetinmek; tam sayı koşulunun gerektirdiği çarpanı kaçırmak.','orta','öncüllü',3,'orb-oncullu','Öncüllü oran yorumu',KY)

# ---------- 01 kolay · oran ----------
for k in range(1,50):
    a,b,c=3*k,4*k,7*k
    if a+b+c==56: assert (a,b,c,k)==(12,16,28,4) and 56//4==14
mk(P,'0001',tipId='orb-oran',tip='Oran ve orantı özellikleri (a/b = c/d = k)',z='kolay',alt='Oran Özellikleri',kaz='Eşit oranlar verildiğinde ortak değeri bulup istenen terimi hesaplar.',kalip='düz',adim=2,
 kart='K-ORNB-01 (oran özellikleri) · üçlü eşit oran ve toplam',
 metin='a, b ve c pozitif gerçel sayılardır.\na/3 = b/4 = c/7\na + b + c = 56\nolduğuna göre b kaçtır?',
 dogru=16,yan=[(4,'Ortak değeri (k) bulup b = 4k adımını yapmamış.','dikkat'),(12,'b yerine a’yı (3k) hesaplamış.','dikkat'),(14,'Toplamı yalnızca b’nin katsayısına bölmüş: 56 ÷ 4.','bilgi'),(28,'b yerine c’yi (7k) hesaplamış.','dikkat')],
 istenen='b’nin değeri.',
 ip=['Üç oranın ortak değerine k de; a, b ve c’yi k cinsinden yaz.'],
 bilgi=[ORAN],
 ad=[A('k ile yaz','Ortak değer k olsun.','a = 3k · b = 4k · c = 7k'),A('Toplamı kur','Üç sayının toplamı 56’dır.','3k + 4k + 7k = 14k = 56 → k = 4'),A('b’yi bul','b = 4k.','b = 4 × 4 = 16')],
 puf='a/m = b/n = c/p gibi eşit oranlarda ortak değere k de; her terim m·k, n·k, p·k olur.')

# ---------- 02 kolay · hız ----------
v1,v2,t1=40,60,9; yol=v1*t1; t2=Fr(yol,v2); assert t2==6 and t1-t2==3 and Fr(t1*v2,v1)==Fr(27,2) and Fr(t1*v2,v1)-t1==Fr(9,2) and Fr(v2,v1)==Fr(3,2)
mk(P,'0002',tipId='orb-hiz',tip='Hız–zaman ters orantısı',z='kolay',alt='Hız ve Süre',kaz='Yol sabitken hız ile süre arasındaki ters orantıyı kullanarak süredeki değişimi bulur.',kalip='hikâyeli',adim=2,
 kart='K-ORNB-08 (hız–zaman ters orantısı) · süre kısalması',
 metin='Bir kargo treni, iki istasyon arasındaki yolu sabit 40 km/sa hızla 9 saatte alıyor.\nTren aynı yolu sabit 60 km/sa hızla gitseydi yolculuk süresi kaç saat kısalırdı?',
 dogru=3,yan=[(Fr(3,2),'Hızlar oranı olan 60/40 = 1,5’i süredeki kısalma saati sanmış.','bilgi'),(Fr(9,2),'Doğru orantı kurup yeni süreyi 13,5 saat bulmuş, farkı 13,5 − 9 = 4,5 yazmış.','bilgi'),(6,'Yeni süreyi (6 saat) bulup kısalmayı değil süreyi vermiş.','dikkat'),(9,'Hız değişse de süre kısalmaz sanmış; ilk süreyi yazmış.','dikkat')],
 istenen='Yolculuk süresindeki kısalma (saat).',
 ip=['Yol sabit; yolu hız × süre ile bul, yeni hızla süreyi hesapla.'],
 bilgi=[HIZ],
 ad=[A('Yolu bul','yol = hız × süre.','40 × 9 = 360 km'),A('Yeni süreyi bul','Aynı yolu 60 km/sa ile gitmek.','360 ÷ 60 = 6 saat'),A('Farkı al','Önceki süreden yeni süreyi çıkar.','9 − 6 = 3 saat')],
 puf='Yol sabitken hız artarsa süre aynı oranda azalır; önce yolu bul, sonra yeni süreyi hesapla.')

# ---------- 03 kolay · ölçek ----------
cm=8*250000; assert cm==2_000_000 and Fr(cm,100000)==20
yan3=[(cm,'Santimetre cinsinden bulduğu 2 000 000’i kilometreye çevirmeyi unutmuş.','dikkat'),(Fr(cm,100),'Santimetreyi metreye çevirip (20 000) kilometreye geçmeyi unutmuş.','dikkat'),(Fr(cm,10**3),'1 km’yi 1000 cm sanmış.','bilgi'),(Fr(cm,10**4),'1 km’yi 10 000 cm sanmış.','bilgi')]
assert [v for v,_,_ in yan3]==[2000000,20000,2000,200]
mk(P,'0003',tipId='orb-olcek',tip='Ölçek ve harita',z='kolay',alt='Ölçek',kaz='Harita ölçeği ve haritadaki uzunluktan gerçek uzaklığı kilometre cinsinden bulur.',kalip='hikâyeli',adim=2,
 kart='K-ORNB-06 (ölçek) · 1/250 000 ölçekli harita',
 metin='Ölçeği 1/250 000 olan bir haritada iki şehir arasındaki uzaklık 8 cm olarak ölçülüyor.\nBuna göre bu iki şehir arasındaki gerçek uzaklık kaç kilometredir?',
 dogru=20,yan=yan3,
 istenen='Gerçek uzaklık (km).',
 ip=['Haritadaki 1 cm gerçekte kaç cm eder? Sonra cm’yi km’ye çevir (1 km = 100 000 cm).'],
 bilgi=[OLC],
 ad=[A('Gerçek uzunluğu cm yap','Ölçek 1/250 000: 1 cm = 250 000 cm.','8 × 250 000 = 2 000 000 cm'),A('km’ye çevir','1 km = 100 000 cm.','2 000 000 ÷ 100 000 = 20 km'),A('Kontrol','Haritadaki 1 cm gerçekte 2,5 km eder, 8 cm bunun 8 katıdır.','8 × 2,5 = 20 km ✓')],
 puf='Ölçek sorularında önce santimetre cinsinden gerçek uzunluğu bul, sonra 100 000’e bölerek kilometreye çevir.')

# ---------- 04 kolay · karışım ----------
parca=Fr(450,9); assert parca==50 and parca*2==100 and parca*7==350 and 450*2==900 and 450*7==3150 and 450//2==225
mk(P,'0004',tipId='orb-karisim',tip='Karışım ve tarif oranı',z='kolay',alt='Karışım',kaz='Hacim oranı verilen bir karışımın toplamından bileşenin miktarını bulur.',kalip='hikâyeli',adim=2,
 kart='K-ORNB-07 (karışım oranı) · su ve limon suyu',
 metin='Bir limonata, hacimce su ve limon suyu 7 : 2 oranında karıştırılarak hazırlanıyor.\nHazırlanan limonata 450 mL olduğuna göre bu limonatadaki limon suyu kaç mL’dir?',
 dogru=100,yan=[(225,'Oranı 1/2 sanıp 450’nin yarısını almış.','bilgi'),(350,'Limon suyu yerine suyun miktarını (7 parça) bulmuş.','dikkat'),(900,'Limon suyu payı olan 2 ile 450’yi çarpmış; parça değerini bulmamış.','islem'),(3150,'7 ile 450’yi çarpmış; toplamı parçalara bölmemiş.','islem')],
 istenen='Limon suyu miktarı (mL).',
 ip=['Toplam kaç eşit parçadır? Bir parçanın hacmini bul.'],
 bilgi=[KAR],
 ad=[A('Parçaları say','7 + 2 = 9 eşit parça.','9 parça = 450 mL'),A('Bir parçayı bul','450’yi 9’a böl.','450 ÷ 9 = 50 mL'),A('Limon suyu','Limon suyu 2 parçadır.','2 × 50 = 100 mL')],
 puf='Karışımda toplam parça sayısını bul, bir parçanın değerini hesapla, sonra istenen bileşenin parça sayısıyla çarp.')

# ---------- 05 orta · tablo, ters ----------
x1,y2_=4,8
# x ile y ters orantılı: x·y sabit; tablo: (4,b), (6,8), (a,3)
c5=6*8; b=Fr(c5,4); a=Fr(c5,3); assert (a,b)==(16,12) and a*b==192 and 4+10==6+8==11+3 and 10*11==110
mk(P,'0005',tipId='orb-dogruters',tip='Doğru ve ters orantı: tablo',z='kolay',alt='Ters Orantı',kaz='Ters orantılı iki çokluğun tablosundaki eksik değerleri bulur.',kalip='tablo',adim=3,
 kart='K-ORNB-02 (doğru–ters orantı, tablo) · eksik iki değer ve çarpım',
 metin='Aşağıdaki tabloda x ile y ters orantılıdır.\nx : 4 | 6 | a\ny : b | 8 | 3\nBuna göre a · b çarpımı kaçtır?',
 dogru=192,yan=[(48,'Sabit çarpımı (6 × 8 = 48) bulup a · b çarpımı sanmış.','dikkat'),(12,'Yalnız b’yi bulup durmuş.','dikkat'),(16,'Yalnız a’yı bulup durmuş.','dikkat'),(110,'Ters orantı yerine toplamları sabit sanmış: 4 + b = 6 + 8 = a + 3 yazıp b = 10, a = 11 bulmuş.','bilgi')],
 istenen='a · b çarpımı.',
 ip=['Ters orantıda x · y çarpımı sabittir; bilinen sütundan sabiti bul.'],
 bilgi=[TERS],
 ad=[A('Sabiti bul','Tam bilinen sütun 6 ve 8’dir.','x × y = 6 × 8 = 48'),A('b ve a’yı bul','Diğer sütunlarda da çarpım 48’dir.','4 × b = 48 → b = 12 · a × 3 = 48 → a = 16'),A('Çarp','İstenen çarpımı hesapla.','a × b = 16 × 12 = 192')],
 puf='Ters orantılı tablolarda her sütunun çarpımı aynıdır; tam bilinen sütundan sabiti bul.')

# ---------- 06 orta · bileşik ----------
isc,sa,g=5,8,12; is_=isc*sa*g; assert is_==480 and Fr(is_,6*10)==8
assert Fr(g*isc,6)==10 and Fr(g*sa,10)==Fr(48,5) and Fr(g*6,isc)==Fr(72,5) and Fr(g*6*10,isc*sa)==18
mk(P,'0006',tipId='orb-bilesik',tip='Bileşik orantı (işçi–gün–saat)',z='orta',alt='Bileşik Orantı',kaz='İşçi sayısı, gün ve günlük çalışma saati arasındaki bileşik orantıyı kurarak gün sayısını bulur.',kalip='hikâyeli',adim=3,
 kart='K-ORNB-03 (bileşik orantı) · işçi ve günlük saat birlikte değişiyor',
 metin='Eşit verimle çalışan 5 işçi, günde 8 saat çalışarak bir işi 12 günde bitirmektedir.\nBu işi, aynı verimle çalışan 6 işçi günde 10 saat çalışarak kaç günde bitirir?',
 dogru=8,yan=[(Fr(48,5),'Yalnız günlük saati (8 → 10) dikkate alıp 12 × 8/10 hesaplamış; işçi artışını unutmuş.','dikkat'),(10,'Yalnız işçi sayısını (5 → 6) dikkate alıp 12 × 5/6 hesaplamış.','dikkat'),(Fr(72,5),'İşçi sayısını doğru orantılı alıp 12 × 6/5 yazmış.','bilgi'),(18,'Üç çokluğu da doğru orantılı alıp 12 × (6/5) × (10/8) hesaplamış.','bilgi')],
 istenen='İşin bitme süresi (gün).',
 ip=['İş miktarını işçi × saat × gün çarpımı olarak yaz; yeni durumda da aynı çarpımı kur.'],
 bilgi=[BIL],
 ad=[A('İş miktarını bul','İşçi × günlük saat × gün.','5 × 8 × 12 = 480 işçi–saat'),A('Yeni durumu kur','6 işçi, günde 10 saat, x gün.','6 × 10 × x = 480'),A('x’i bul','Denklemi çöz.','60x = 480 → x = 8 gün')],
 puf='İş sabitken işçi, günlük saat ve gün sayısı birbirleriyle ters orantılıdır; çarpımları değişmez.')

# ---------- 07 orta · doğru paylaştırma ----------
k7=Fr(450,3); assert k7==150 and 10*k7==1500 and 5*k7==750 and 7*k7==1050 and 450*5==2250
mk(P,'0007',tipId='orb-paylastirma',tip='Doğru ve ters orantılı paylaştırma',z='kolay',alt='Orantılı Paylaştırma',kaz='Doğru orantılı paylaştırmada pay farkından toplam tutarı bulur.',kalip='hikâyeli',adim=3,
 kart='K-ORNB-04 (orantılı paylaştırma) · pay farkından toplam',
 metin='Üç ortak, bir işletmenin kârını 2, 3 ve 5 ile doğru orantılı olacak biçimde paylaşmıştır.\nEn çok pay alan ortak, en az pay alan ortaktan 450 TL fazla aldığına göre kârın tamamı kaç TL’dir?',
 dogru=1500,yan=[(450,'Verilen farkı kârın tamamı sanmış.','dikkat'),(750,'En çok pay alanın payını (5k) bulup toplam sanmış.','dikkat'),(1050,'En az ve en çok payların toplamını (7k) bulup tüm payı eklememiş.','dikkat'),(2250,'Fark olan 450’yi 5 ile çarpmış; parça değerini hesaplamamış.','islem')],
 istenen='Kârın tamamı (TL).',
 ip=['Paylar 2k, 3k, 5k; en çok ile en az payın farkı kaç k eder?'],
 bilgi=[PAYD],
 ad=[A('Payları yaz','2, 3 ve 5 ile doğru orantılı.','2k · 3k · 5k'),A('k’yi bul','En çok − en az = 5k − 2k.','3k = 450 → k = 150'),A('Toplamı bul','Toplam 10k.','10 × 150 = 1500 TL')],
 puf='Paylaştırmada verilen farkı ya da payı k cinsinden yaz; k’yi bulunca toplam parça sayısıyla çarp.')

# ---------- 08 orta · ters paylaştırma ----------
h=[2,3,6]; T=1320; w=[Fr(1,x) for x in h]; kk=Fr(T)/sum(w); pay=[kk*x for x in w]; assert pay==[660,440,220] and max(pay)-min(pay)==440
d_=[Fr(T,sum(h))*x for x in h]; assert max(d_)-min(d_)==480 and 6*120==720 and 660==max(pay) and 220==min(pay) and 880==660+220
mk(P,'0008',tipId='orb-paylastirma',tip='Doğru ve ters orantılı paylaştırma',z='orta',alt='Orantılı Paylaştırma',kaz='Ters orantılı paylaştırmada payları bulup en çok ve en az pay arasındaki farkı hesaplar.',kalip='hikâyeli',adim=3,
 kart='K-ORNB-04 (orantılı paylaştırma) · yaşlarla ters orantılı harçlık',
 metin='Bir dede, 1320 TL’lik harçlığı yaşları 2, 3 ve 6 olan üç torununa, yaşlarıyla ters orantılı olacak biçimde dağıtmıştır.\nBuna göre en çok harçlık alan torun ile en az alan torun arasındaki fark kaç TL’dir?',
 dogru=440,yan=[(720,'Doğru orantılı dağıtıp en çok payı (6 × 120 = 720) fark sanmış.','bilgi'),(480,'Doğru orantılı dağıtıp (2 : 3 : 6) farkı 6 − 2 = 4 parça olarak almış.','bilgi'),(660,'Ters orantılı payı doğru bulmuş ama en çok payı (3 parça) fark sanmış.','dikkat'),(880,'En çok ve en az payları çıkarmak yerine toplamış: 660 + 220.','islem')],
 istenen='En çok ve en az ikramiye arasındaki fark (TL).',
 ip=['Ters orantı için 1/2, 1/3, 1/6 ile doğru orantılı paylaştır; paydaları eşitle.'],
 bilgi=[PAYT],
 ad=[A('Oranı bul','1/2 : 1/3 : 1/6 = 3/6 : 2/6 : 1/6.','3 : 2 : 1 (toplam 6 parça)'),A('Parçayı bul','1320’yi 6 parçaya böl.','1320 ÷ 6 = 220 TL'),A('Payları yaz','En çok 3 parça, en az 1 parça.','660, 440, 220 TL'),A('Farkı al','En çok − en az.','660 − 220 = 440 TL')],
 puf='Ters orantılı paylaştırmada sayıların çarpmaya göre tersleriyle (1/2, 1/3, 1/6) doğru orantılı paylaştır; küçük sayı büyük pay alır.')

# ---------- 09 orta · ortalama çıkarma ----------
assert 5*12==60 and 4*10==40 and 60-40==20 and 12-10==2 and 12+10==22
mk(P,'0009',tipId='orb-ortalama',tip='Aritmetik ortalama değişimi',z='kolay',alt='Aritmetik Ortalama',kaz='Sayıların toplamı ile ortalama arasındaki ilişkiden çıkarılan sayıyı bulur.',kalip='düz',adim=3,
 kart='K-ORNB-05 (ortalama değişimi) · bir sayı çıkarılınca ortalama azalıyor',
 metin='Beş sayının aritmetik ortalaması 12’dir. Bu sayılardan biri çıkarılınca kalan dört sayının aritmetik ortalaması 10 oluyor.\nBuna göre çıkarılan sayı kaçtır?',
 dogru=20,yan=[(2,'İki ortalamanın farkını (12 − 10) çıkarılan sayı sanmış.','dikkat'),(12,'İlk ortalamayı çıkarılan sayı sanmış.','dikkat'),(40,'Kalan dört sayının toplamını bulup çıkarılan sayı sanmış.','dikkat'),(60,'Beş sayının toplamını çıkarılan sayı sanmış.','dikkat')],
 istenen='Çıkarılan sayı.',
 ip=['Toplam = ortalama × adet; çıkarmadan önceki ve sonraki toplamların farkına bak.'],
 bilgi=[ORTB],
 ad=[A('İlk toplam','5 sayının toplamı.','5 × 12 = 60'),A('Kalan toplam','4 sayının toplamı.','4 × 10 = 40'),A('Farkı al','Çıkarılan sayı iki toplamın farkıdır.','60 − 40 = 20')],
 puf='Ortalama sorularında ortalamaları toplama çevir (toplam = ortalama × adet); eklenen ya da çıkan sayı toplamların farkıdır.')

# ---------- 10 orta · ortalama ve çarpım ----------
s10=[(a,b) for a in range(1,40) for b in range(1,40) if a+b==20 and a*b==36]
assert s10==[(2,18),(18,2)] and 18-2==16 and 20**2-4*36==256 and 20-6==14
mk(P,'0010',tipId='orb-ortalama',tip='Aritmetik ortalama değişimi',z='orta',alt='Aritmetik Ortalama',kaz='İki sayının aritmetik ortalaması ve çarpımından sayıları bulup farkını hesaplar.',kalip='düz',adim=3,
 kart='K-ORNB-05 (aritmetik ortalama) · ortalama ve çarpımdan fark',
 metin='İki pozitif gerçel sayının aritmetik ortalaması 10, çarpımı 36’dır.\nBuna göre bu iki sayının farkı kaçtır?',
 dogru=16,yan=[(2,'Sayıları bulup küçük olanı fark sanmış.','dikkat'),(14,'Toplamdan (20) çarpımın karekökünü (6) çıkarmış.','bilgi'),(18,'Sayıları bulup büyük olanı fark sanmış.','dikkat'),(256,'(a − b)² = 256 bulup karekök almayı unutmuş.','islem')],
 istenen='İki sayının farkı.',
 ip=['Ortalamadan toplamı bul; (a − b)² = (a + b)² − 4ab açılımını kullan.'],
 bilgi=[ORTB,B('Tam kare farkı','(a − b)² = (a + b)² − 4ab. Örnek: a + b = 7, ab = 12 ise (a − b)² = 49 − 48 = 1')],
 ad=[A('Toplamı bul','Toplam = ortalama × adet.','a + b = 2 × 10 = 20 · ab = 36'),A('Farkın karesi','Tam kare açılımından.','(a − b)² = 20² − 4 × 36 = 400 − 144 = 256'),A('Karekök al','Fark pozitif alınır.','a − b = 16 (sayılar 18 ve 2)')],
 puf='Ortalama toplamı verir; toplam ve çarpım bilinince (a − b)² = (a + b)² − 4ab ile fark bulunur.')

# ---------- 11 orta · oran özelliği ----------
for s in range(1,6):
    for t in range(1,6):
        a,b,c,d=2*s,5*s,2*t,5*t
        assert Fr(3*a+2*c,3*b+2*d)==Fr(2,5)
assert 28*5//2==70 and Fr(28*2,5)==Fr(56,5) and 28*5==140 and 3*5+2*5==25
mk(P,'0011',tipId='orb-oran',tip='Oran ve orantı özellikleri (a/b = c/d = k)',z='orta',alt='Oran Özellikleri',kaz='a/b = c/d = k özelliğini katsayılı toplamlara uygulayarak bilinmeyen toplamı bulur.',kalip='düz',adim=3,
 kart='K-ORNB-01 (oran özellikleri) · katsayılı toplamın oran özelliği',
 metin='a, b, c ve d pozitif gerçel sayılardır.\na/b = c/d = 2/5\n3a + 2c = 28\nolduğuna göre 3b + 2d kaçtır?',
 dogru=70,yan=[(Fr(56,5),'Oran özelliğini ters kurup 28 × 2/5 hesaplamış.','bilgi'),(28,'Oran özelliğinde toplamın değişmeyeceğini sanmış: 3b + 2d = 3a + 2c.','bilgi'),(140,'28’i 5 ile çarpıp 2’ye bölmeyi unutmuş.','islem'),(25,'b = 5 ve d = 5 yazıp 3 × 5 + 2 × 5 hesaplamış.','bilgi')],
 istenen='3b + 2d değeri.',
 ip=['a = 2s, b = 5s, c = 2t, d = 5t yaz; 3a + 2c ile 3b + 2d arasındaki oranı bul.'],
 bilgi=[OZ,ORAN],
 ad=[A('Oranı yaz','a/b = c/d = 2/5 olduğundan katsayılı toplamlar da aynı orandadır.','(3a + 2c)/(3b + 2d) = 2/5'),A('Değeri yerine koy','3a + 2c = 28.','28/(3b + 2d) = 2/5'),A('İçler dışlar','Çapraz çarp.','2 × (3b + 2d) = 140 → 3b + 2d = 70')],
 puf='a/b = c/d = k ise pay ile paydalarda aynı katsayılarla yapılan toplamlar da k oranını korur.')

# ---------- 12 orta · kur ----------
usd,eurTL,usdTL=640,40,32
eur=Fr(usd*usdTL,eurTL); assert eur==512 and Fr(usd,eurTL)==16 and Fr(usd*eurTL,usdTL)==800 and usd*usdTL==20480
mk(P,'0012',tipId='orb-yeninesil',tip='Yeni nesil orantı: dişli, kur çevirme, tarif',z='orta',alt='Kur Çevirme',kaz='İki farklı döviz kurunu kullanarak bir para birimini diğerine çevirir.',kalip='hikâyeli',adim=3,
 kart='K-ORNB-09 (kur çevirme) · dolardan euroya',
 metin='Bir döviz bürosunda 1 dolar 32 TL, 1 euro 40 TL’dir. Büro komisyon almamakta; alış ve satış kuru aynıdır.\nBu bürodan 640 dolarını euroya çeviren bir kişi kaç euro alır?',
 dogru=512,yan=[(16,'640’ı yalnız euro kuruna bölmüş (640 ÷ 40); dolar kurunu kullanmamış.','dikkat'),(640,'Dolar ile euroyu birbirine eşit varsaymış.','bilgi'),(800,'Kurları ters kullanıp 640 × 40 ÷ 32 hesaplamış.','bilgi'),(20480,'640 doları TL’ye çevirip durmuş; euro kuruna bölmemiş.','dikkat')],
 istenen='Alınan euro miktarı.',
 ip=['Önce dolarları TL’ye çevir, sonra TL’yi euro kuruna böl.'],
 bilgi=[KUR],
 ad=[A('TL’ye çevir','1 dolar 32 TL.','640 × 32 = 20 480 TL'),A('Euroya çevir','1 euro 40 TL.','20 480 ÷ 40 = 512 euro'),A('Kontrol','Geri çevirince aynı TL değeri çıkmalı.','512 × 40 = 20 480 TL ✓')],
 puf='İki döviz arasında çevirmede önce ortak birime (TL) geç, sonra hedef paranın kuruna böl.')

# ---------- 13 orta · öncüllü ----------
for k in range(1,30):
    a,b,c=3*k,4*k,10*k
    assert Fr(a,b)==Fr(3,4) and Fr(b,c)==Fr(2,5)
    assert (a+b+c)%17==0 and b%4==0
assert 10%4!=0 and 20%4==0
mk(P,'0013',tipId='orb-oncullu',tip='Öncüllü oran yorumu',z='orta',alt='Oran Özellikleri',kaz='Ortak terimle birleştirilen oranlardan çıkan değerler için öncüllerin kesin doğruluğunu sınar.',kalip='öncüllü',adim=3,
 kart='K-ORNB-10 (öncüllü oran) · a/b = 3/4 ve b/c = 2/5',
 metin='a, b ve c pozitif tam sayılardır.\na/b = 3/4\nb/c = 2/5\nolduğuna göre,\nI. a + b + c toplamı 17’nin katıdır.\nII. c, 4’ün katıdır.\nIII. b, 4’ün katıdır.\nifadelerinden hangileri kesinlikle doğrudur?',
 dogru='I ve III',sira=['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III'],
 yan=[('Yalnız I','b = 4k olduğunu fark etmeyip III’ü yanlış saymış.','dikkat'),('Yalnız II','Toplamı 17k yazamayıp I’i, b = 4k’yı görmeyip III’ü yanlış saymış; II’yi yalnız k = 2 ile doğrulamış.','dikkat'),('I ve II','II’yi yalnız k = 2 için (c = 20) doğrulamış; III’ü sınamamış.','dikkat'),('I, II ve III','II’yi yalnız k = 2 için (c = 20) doğrulayıp kesin saymış.','dikkat')],
 istenen='Kesinlikle doğru olan ifadeler.',
 ip=['Ortak terim b’yi 4’e eşitle: b/c = 2/5 oranını 4/10 yaz; sonra a, b, c’yi k cinsinden yaz.'],
 bilgi=[B('Ortak terimi eşitleme','a/b = 3/4 ve b/c = 2/5 ise b iki oranda eşitlenir: 2/5 = 4/10 ⇒ a : b : c = 3 : 4 : 10. Örnek: pozitif tam sayılar için a = 3k, b = 4k, c = 10k (k pozitif tam sayı)'),B('Katlar','4’ün katı 4 × m biçimindedir. Örnek: 4k her k için 4’ün katıdır; 10k yalnız k çift iken 4’ün katıdır (k = 2 → 20)')],
 ad=[A('b’yi eşitle','b/c = 2/5 = 4/10; böylece b = 4 olur.','a : b : c = 3 : 4 : 10'),A('k ile yaz','Pozitif tam sayılar için a = 3k, b = 4k, c = 10k.','a + b + c = 17k'),A('Öncülleri sına','I: 17k, 17’nin katıdır. II: k = 1 için c = 10, 4’ün katı değildir. III: b = 4k her zaman 4’ün katıdır.','I doğru · II yanlış · III doğru'),A('Sonuç','Kesinlikle doğru olanlar I ve III.','I ve III')],
 puf='Ortak terimle oranları birleştirip her terimi k ile yaz; k’ye bağlı olarak değişen ifadeleri bir örnekle çürüt, her k için geçerli olanları kanıtla.')

# ---------- 14 zor · dişli ----------
A_,B_,C_,D_=36,12,24,9; turA=6
tB=Fr(A_*turA,B_); tC=tB; tD=Fr(C_*tC,D_)
assert tB==18 and tD==48 and Fr(tC*D_,C_)==Fr(27,4) and Fr(turA*A_,D_)==24 and Fr(A_,B_)*Fr(C_,D_)==8
mk(P,'0014',tipId='orb-yeninesil',tip='Yeni nesil orantı: dişli, kur çevirme, tarif',z='zor',alt='Dişli Çarkları',kaz='Kenetli ve aynı mildeki dişlilerden oluşan bir düzenekte ters orantıyı iki kez kullanarak dönme sayısını bulur.',kalip='yeni nesil',adim=4,
 kart='K-ORNB-09 (dişli düzeneği) · iki kademeli dişli, A dönüyor D sorulur',
 metin='Bir düzenekte 36 dişli A dişlisi ile 12 dişli B dişlisi birbirine kenetlidir. 24 dişli C dişlisi, B ile aynı mil üzerindedir ve B ile birlikte döner. 9 dişli D dişlisi ise C ile kenetlidir.\nA dişlisi 6 tam tur döndüğünde D dişlisi kaç tur döner?',
 dogru=48,yan=[(Fr(27,4),'İkinci kademeyi doğru orantılı alıp 18 × 9/24 hesaplamış.','bilgi'),(8,'Dişli oranlarını (3 ve 8/3) çarpıp 8 bulmuş; A’nın tur sayısıyla çarpmamış.','dikkat'),(18,'B’nin (ve C’nin) tur sayısını bulup D’yi hesaplamamış.','dikkat'),(24,'A ile D’yi doğrudan kenetli sanıp 6 × 36/9 hesaplamış.','bilgi')],
 istenen='D dişlisinin tur sayısı.',
 ip=['Kenetli dişlilerde diş sayısı × tur sayısı eşittir; aynı mildeki dişliler aynı tur sayısına sahiptir.'],
 bilgi=[DIS],
 ad=[A('A ile B','Kenetli: diş sayısı × tur eşit.','36 × 6 = 12 × tB → tB = 18 tur'),A('B ile C','Aynı mildedir, tur sayıları eşittir.','tC = 18 tur'),A('C ile D','Kenetli: 24 × 18 = 9 × tD.','432 = 9 × tD'),A('D’nin turu','Denklemi çöz.','tD = 48 tur')],
 puf='Dişli düzeneklerinde kenetli çiftte diş × tur sabittir; aynı mildeki dişliler aynı turu atar. Kademeleri sırayla uygula.')

# ---------- 15 zor · işçi ayrılıyor, saat artıyor ----------
top=6*8*20; yap=6*8*5; kal=top-yap; gun=Fr(kal,4*10); assert top==960 and kal==720 and gun==18 and 5+gun==23
assert Fr(kal,4*8)+5==Fr(55,2) and Fr(top,4*10)==24
mk(P,'0015',tipId='orb-bilesik',tip='Bileşik orantı (işçi–gün–saat)',z='zor',alt='İşçi Problemleri',kaz='İşçi sayısı ve günlük çalışma saati birlikte değişen bir işte yapılan ve kalan işi işçi–saat cinsinden ayırarak toplam süreyi bulur.',kalip='hikâyeli',adim=5,
 kart='K-ORNB-03 (bileşik orantı) · işçi ayrılıyor, günlük saat artıyor',
 metin='Eşit verimle çalışan 6 işçi, günde 8 saat çalışarak bir işi 20 günde bitirebilmektedir. İşçiler günde 8 saat çalışarak 5 gün çalıştıktan sonra 2 işçi işten ayrılıyor; kalan işçiler günlük çalışma süresini 10 saate çıkarıyor.\nBuna göre bu iş toplam kaç günde biter?',
 dogru=23,yan=[(18,'Değişimden sonra geçen süreyi (18 gün) toplam süre sanmış.','dikkat'),(20,'İşçi ayrılması ve saat artışını dikkate almayıp ilk süreyi yazmış.','dikkat'),(Fr(55,2),'Günlük saat artışını unutup kalan işi 4 işçi × 8 saat ile hesaplamış: 5 + 22,5.','dikkat'),(24,'4 işçi, günde 10 saatle işin tamamını baştan yapıyormuş gibi 960 ÷ 40 hesaplamış.','dikkat')],
 istenen='İşin toplam bitme süresi (gün).',
 ip=['İşi işçi–saat cinsinden bul; ilk 5 günde yapılanı çıkar, kalanı yeni işçi ve saat sayısına böl.'],
 bilgi=[BIL],
 ad=[A('Toplam iş','İşçi × günlük saat × gün.','6 × 8 × 20 = 960 işçi–saat'),A('İlk 5 gün','6 işçi, günde 8 saat.','6 × 8 × 5 = 240 işçi–saat'),A('Kalan iş','Toplamdan çıkar.','960 − 240 = 720 işçi–saat'),A('Yeni düzen','4 işçi, günde 10 saat: günde 40 işçi–saat.','720 ÷ 40 = 18 gün'),A('Toplam süre','İlk 5 gün ile 18 günü topla.','5 + 18 = 23 gün')],
 puf='Çalışma sırasında işçi sayısı ya da günlük saat değişirse işi işçi–saat birimiyle yaz; yapılan kısmı çıkar, kalanı yeni işçi × saat değerine böl.')

# ---------- 16 zor · ortalama hız ----------
for d in (60,120,240):
    assert Fr(2*d,Fr(d,12)+Fr(d,20))==15
assert Fr(12*20,12+20)==Fr(15,2) and Fr(12+20,2)==16 and 12*20==240 and 12+20==32
mk(P,'0016',tipId='orb-hiz',tip='Hız–zaman ters orantısı',z='zor',alt='Ortalama Hız',kaz='Gidiş ve dönüş hızları farklı olan bir yolculukta toplam yolu toplam süreye bölerek ortalama hızı bulur.',kalip='hikâyeli',adim=4,
 kart='K-ORNB-08 (hız–zaman ters orantısı) · gidiş–dönüş ortalama hızı',
 metin='Bir bisikletli, A noktasından B noktasına sabit 12 km/sa hızla gidiyor ve aynı yoldan sabit 20 km/sa hızla geri dönüyor.\nOrtalama hız, toplam yolun toplam süreye bölümü olduğuna göre bisikletlinin tüm yolculuktaki ortalama hızı kaç km/sa’tir?',
 dogru=15,yan=[(Fr(15,2),'Formülde 2’yi unutup 12 × 20 ÷ (12 + 20) hesaplamış.','islem'),(16,'Ortalama hızı iki hızın aritmetik ortalaması (12 + 20)/2 sanmış; süreler eşit değildir.','bilgi'),(32,'İki hızı toplamış.','dikkat'),(240,'İki hızı çarpmış.','dikkat')],
 istenen='Ortalama hız (km/sa).',
 ip=['Yolun uzunluğuna 60 km de; gidiş ve dönüş sürelerini ayrı hesapla.'],
 bilgi=[HIZ],
 ad=[A('Yolu seç','Sonuç yoldan bağımsızdır; AB = 60 km alınabilir.','toplam yol = 120 km'),A('Gidiş süresi','60 ÷ 12.','5 saat'),A('Dönüş süresi','60 ÷ 20.','3 saat'),A('Ortalama hız','Toplam yol ÷ toplam süre.','120 ÷ 8 = 15 km/sa')],
 puf='Gidiş–dönüş yolculuğunda ortalama hız, hızların aritmetik ortalaması değildir; toplam yolu toplam süreye böl.')

# ---------- 17 orta · ortalama, eklenen ----------
t6=6*70; t8=8*74; ek=t8-t6; assert ek==172 and (ek-8)//2==82 and 82+8==90 and ek//2==86 and ek-8==164
mk(P,'0017',tipId='orb-ortalama',tip='Aritmetik ortalama değişimi',z='orta',alt='Aritmetik Ortalama',kaz='İki yeni değer eklenince değişen ortalamadan eklenenlerin toplamını bulup aralarındaki farktan değerleri hesaplar.',kalip='hikâyeli',adim=4,
 kart='K-ORNB-05 (ortalama değişimi) · sınıfa iki öğrenci katılıyor',
 metin='Bir sınıftaki 6 öğrencinin matematik sınavı puan ortalaması 70’tir. Sınıfa katılan iki yeni öğrenci de aynı sınava girince 8 öğrencinin puan ortalaması 74 olmuştur.\nYeni öğrencilerden biri diğerinden 8 puan fazla aldığına göre yüksek puan alan yeni öğrencinin puanı kaçtır?',
 dogru=90,yan=[(8,'Verilen farkı (8) puan sanmış.','dikkat'),(82,'Düşük puanı bulup yüksek puanı sormuş.','dikkat'),(86,'İki yeni öğrenciyi eşit puanlı sayıp toplamı ikiye bölmüş: 172 ÷ 2.','islem'),(164,'172 − 8 = 164’ü ikiye bölmeden yüksek puan sanmış.','islem')],
 istenen='Yüksek puan alan yeni öğrencinin puanı.',
 ip=['Önce 6 ve 8 öğrencinin puan toplamlarını bul; farkları yeni iki öğrencinin toplamıdır.'],
 bilgi=[ORTB],
 ad=[A('Toplamları bul','Ortalama × adet.','6 × 70 = 420 · 8 × 74 = 592'),A('Yeni öğrencilerin toplamı','Fark, yeni iki puanın toplamıdır.','592 − 420 = 172'),A('Düşük puanı bul','Düşük x, yüksek x + 8.','x + (x + 8) = 172 → x = 82'),A('Yüksek puanı yaz','Yüksek puan x + 8.','82 + 8 = 90')],
 puf='Değer eklenince toplamlar farkı eklenenlerin toplamını verir; farkları da verilirse iki bilinmeyenli küçük bir denklem kurulur.')

# ---------- 18 zor · karışık paylaştırma ----------
gun=[18,20,16]; hata=[3,4,4]; q=[Fr(g_,h_) for g_,h_ in zip(gun,hata)]; assert q==[6,5,4] and (q[0]-q[2])*Fr(600,2)==600 and sum(q)*300==4500
assert q[0]*300==1800 and sum([Fr(1,x) for x in hata])==Fr(5,6)
# yalnız hata ters: 1/3:1/4:1/4 = 4:3:3, fark 1 parça
assert [Fr(1,3)*12,Fr(1,4)*12,Fr(1,4)*12]==[4,3,3] and 10*600==6000
# yalnız gün: 9:10:8, fark 1 parça
assert [Fr(18,2),Fr(20,2),Fr(16,2)]==[9,10,8] and 27*600==16200 and 15*600==9000
mk(P,'0018',tipId='orb-paylastirma',tip='Doğru ve ters orantılı paylaştırma',z='zor',alt='Orantılı Paylaştırma',kaz='Çalışma gününe doğru, hata sayısına ters orantılı paylaştırmada payları bulup toplam tutarı hesaplar.',kalip='hikâyeli',adim=4,
 kart='K-ORNB-04 (orantılı paylaştırma) · gün ile doğru, hata ile ters orantılı ikramiye',
 metin='Bir şirket, ikramiyeyi üç çalışana paylaştırıyor. Her çalışanın payı, çalışma gün sayısıyla doğru, hata sayısıyla ters orantılıdır.\nÇalışanlar sırasıyla 18, 20 ve 16 gün çalışmış; sırasıyla 3, 4 ve 4 hata yapmıştır.\nBirinci çalışan, üçüncü çalışandan 600 TL fazla aldığına göre ikramiyenin tamamı kaç TL’dir?',
 dogru=4500,yan=[(1800,'Birinci çalışanın payını bulup toplam sanmış.','dikkat'),(6000,'Yalnız hata sayılarına göre ters orantılı paylaştırmış (4 : 3 : 3).','bilgi'),(9000,'600 TL’lik farkı bir parça sanıp toplam 15 parçayı 600 ile çarpmış; fark 2 parçadır.','islem'),(16200,'Yalnız çalışılan günlere göre paylaştırmış (9 : 10 : 8).','bilgi')],
 istenen='İkramiyenin tamamı (TL).',
 ip=['Her çalışanın payı gün ÷ hata ile doğru orantılıdır; bu üç oranı sadeleştir.'],
 bilgi=[PAYD,PAYT],
 ad=[A('Pay oranlarını yaz','Pay, gün ÷ hata ile orantılı.','18/3 : 20/4 : 16/4 = 6 : 5 : 4'),A('Farkı parçalarla yaz','Birinci ile üçüncü arasındaki fark 6k − 4k.','2k = 600 → k = 300'),A('Toplam parça','6 + 5 + 4 = 15 parça.','15k'),A('Toplamı bul','Parçayı çarp.','15 × 300 = 4500 TL')],
 puf='Bir pay hem doğru hem ters orantılı etkileniyorsa pay ∝ doğru ÷ ters oranı olarak yazılır; sadeleştirince tam sayı parçalar çıkar.')

# ---------- 19 zor · tarif ----------
kb=[Fr(450,6),Fr(180,6),Fr(120,6)]; assert kb==[75,30,20]
st=[1200,560,300]; mx=[int(s_//k_) for s_,k_ in zip(st,kb)]; assert mx==[16,18,15] and min(mx)==15 and Fr(560,30)>18 and Fr(560,30)<19 and 15//6==2 and 2*6==12
assert max(n for n in range(0,100) if all(n*k_<=s_ for s_,k_ in zip(st,kb)))==15
mk(P,'0019',tipId='orb-yeninesil',tip='Yeni nesil orantı: dişli, kur çevirme, tarif',z='orta',alt='Tarif Ölçekleme',kaz='Her malzemenin kişi sayısıyla doğru orantılı kullanıldığı bir tarifte eldeki stoğa göre yapılabilecek en çok kişi sayısını bulur.',kalip='yeni nesil',adim=3,
 kart='K-ORNB-09 (tarif ölçekleme) · en kısıtlayıcı malzeme',
 metin='Bir kek tarifinde 6 kişilik için 450 g un, 180 g şeker ve 120 g tereyağı gerekiyor. Her malzeme, kişi sayısıyla doğru orantılı olarak kullanılıyor ve kişi sayısı tam sayı olmak zorunda.\nElde 1200 g un, 560 g şeker ve 300 g tereyağı bulunan bir pastane, en çok kaç kişilik kek yapabilir?',
 dogru=15,yan=[(12,'Tarifi yalnızca 6 kişilik bütün olarak katlayabileceğini sanıp 2 tarif (12 kişi) bulmuş.','bilgi'),(16,'Yalnız unu (1200 ÷ 75) dikkate almış; tereyağı yetmez.','dikkat'),(18,'Yalnız şekeri dikkate alıp 560 ÷ 30 = 18,67’yi aşağı yuvarlamış; tereyağı yetmez.','dikkat'),(19,'Şekerden çıkan 18,67’yi yukarı yuvarlamış; hem tam sayı olmaz hem de tereyağı yetmez.','islem')],
 istenen='Yapılabilecek en çok kişi sayısı.',
 ip=['Her malzeme için kişi başına düşen miktarı bul; stoğu bu miktara bölüp en küçük sonucu seç.'],
 bilgi=[TAR],
 ad=[A('Kişi başı miktar','Tarifi 6’ya böl.','un 75 g · şeker 30 g · tereyağı 20 g'),A('Her malzemeyle kaç kişi','Stok ÷ kişi başı miktar.','un: 1200 ÷ 75 = 16 · şeker: 560 ÷ 30 = 18,67 → 18 · tereyağı: 300 ÷ 20 = 15'),A('Kısıtlayıcıyı seç','Hepsi birden yeterli olmalı, en küçük değer sınırdır.','en küçük = 15'),A('Kontrol','15 kişi için gerekenler stoğu aşmaz.','un 1125 ≤ 1200 · şeker 450 ≤ 560 · tereyağı 300 ≤ 300')],
 puf='Birden çok malzemeli ölçeklemede her malzemenin yetebileceği kişi sayısını ayrı bul; en küçüğü sınırdır.')

bitir(P,'oraniki',UK)
