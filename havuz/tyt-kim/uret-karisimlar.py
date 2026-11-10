import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_kim as H
from _hafif_kim import *
H.KONU='Karışımlar'
P=Parti('karisimlar','Karışımlar','kim|Karışımlar',ders='TYT Kimya',idon='tytkim')
KY='ÖSYM 2018–2025 (homojen–heterojen karışımlar, ayırma teknikleri) · MEB 9. sınıf'
kart('K-KRSM-01','Homojen–heterojen ayrımı','Tek fazlı, her yerinde aynı özellikte olan karışım homojendir; bileşenleri ayırt edilebiliyorsa heterojendir.','Çözeltiyi, alaşımı ya da bulanık görüneni yanlış sınıflandırmak.','kolay','öncüllü',2,'kim-krs-sinif','Karışımı sınıflandırma',KY)
kart('K-KRSM-02','Ayırma sırası','Katı karışımda önce mıknatıs, sonra suda çözme–süzme, son olarak buharlaştırma uygulanır.','Süzme ile buharlaştırmanın sırasını karıştırmak; suya atmadan süzmek.','orta','düz',3,'kim-krs-sira','Ayırma işlem sırası',KY)
kart('K-KRSM-03','Buharlaştırma ile derişim','Çözücü azalınca çözünen kütlesi sabit kalır; yüzde = çözünen ÷ çözelti × 100.','Çözelti kütlesi yerine çözücü kütlesini kullanmak; buharlaşan su yerine su eklenmiş saymak.','orta','hikâyeli',3,'kim-krs-buhar','Buharlaştırma ve kütlece yüzde',KY)
kart('K-KRSM-04','Çözelti karıştırma','Aynı maddenin iki çözeltisi karıştırılınca çözünen kütleleri ve çözelti kütleleri ayrı ayrı toplanır.','Derişimlerin aritmetik ortalamasını almak.','orta','hikâyeli',3,'kim-krs-karis','İki çözeltiyi karıştırma',KY)
kart('K-KRSM-05','Çözünürlük ve çökme','Doygun çözeltide çözücü kütlesi ile çözünürlük orantılıdır; soğutmada çözünürlük farkı kadar katı çöker.','100 g su için verilen farkı gerçek su kütlesine ölçeklememek.','zor','tablo',4,'kim-krs-cozunurluk','Soğutmada çöken madde miktarı',KY)
kart('K-KRSM-06','Doygun çözelti özellikleri','Doygun çözeltide aynı sıcaklıkta ek katı çözünmez, su eklenince çözelti doymamış olur, su buharlaşınca derişim sabit kalır.','Su buharlaşınca derişimin arttığını sanmak.','zor','öncüllü',3,'kim-krs-doygun','Doygun çözelti',KY)
# ---- 0001
d={'I':(True,'şekerli su tek fazlıdır, her yerinde aynı özelliktedir; homojendir'),
   'II':(False,'çamurlu suda katı parçacıklar ayırt edilir, heterojendir'),
   'III':(True,'bronz bakır–kalay alaşımıdır, katı çözeltidir ve homojendir')}
r=onc(d,[('I','III'),('I',),('II',),('III',),('II','III')])
mk(P,'0001',tipId='kim-krs-sinif',tip='Karışımı sınıflandırma',z='kolay',alt='Homojen ve Heterojen Karışımlar',kaz='Verilen karışımları homojen ve heterojen olarak sınıflandırır.',kalip='öncüllü',adim=2,
 kart='K-KRSM-01 (homojen–heterojen) · şekerli su, çamurlu su, bronz',
 metin='Aşağıda üç karışım verilmiştir.\nI. Şekerli su\nII. Çamurlu su\nIII. Bronz (bakır–kalay alaşımı)\nBunlardan hangileri homojen karışımdır?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Homojen olan karışımlar.',
 ip=['Karışımın her yerinde aynı görünüm ve aynı özellik varsa homojendir; parçacıkları ayırt edebiliyorsan heterojendir.'],
 bilgi=[B('Homojen ve heterojen karışım','Homojen karışımda bileşenler her yerde aynı oranda dağılmıştır ve tek faz görülür (örnek: tuzlu su). Heterojen karışımda bileşenler ayırt edilebilir (örnek: kum–su)')],
 ad=[A('Karışımı incele','Her karışımın her yerinde aynı özellik olup olmadığına bak.','I · II · III'),A('Şekerli su','Şeker suda tamamen çözünür, tek faz oluşur.','I: homojen'),A('Çamurlu su','Toprak parçacıkları ayırt edilir ve zamanla dibe çöker.','II: heterojen'),A('Bronz','Alaşımlar katı çözeltidir, her yerinde aynı bileşimdedir.','III: homojen · Sonuç: I ve III')],
 puf='Gözle ayırt edilebilen bileşen yoksa ve her yer aynıysa karışım homojendir; alaşımlar da homojendir.')
# ---- 0002
S=[('Suya atma → süzme → buharlaştırma',False,'demir tozu ve kum süzgeçte birlikte kalır, üç madde ayrı ayrı elde edilemez'),
   ('Buharlaştırma → süzme → mıknatıs',False,'katı karışımda buharlaştırılacak bir sıvı yoktur ve süzme için önce suda çözmek gerekir'),
   ('Mıknatıs → süzme → suya atma → buharlaştırma',False,'karışım suya atılmadan süzülemez; süzme çözme işleminden sonra yapılır'),
   ('Mıknatıs → suya atma → buharlaştırma → süzme',False,'su buharlaşınca tuz kumla birlikte kalır ve süzme ikisini ayıramaz'),
   ('Mıknatıs → suya atma → süzme → buharlaştırma',True,'')]
r=tek(S,True)
mk(P,'0002',tipId='kim-krs-sira',tip='Ayırma işlem sırası',z='orta',alt='Ayırma ve Saflaştırma Teknikleri',kaz='Katı karışımdaki maddeleri uygun ayırma yöntemlerini doğru sırayla uygulayarak ayırır.',kalip='düz',adim=3,
 kart='K-KRSM-02 (ayırma sırası) · demir tozu–kum–tuz',
 metin='Demir tozu, kum ve tuzdan oluşan katı karışımdaki üç madde de ayrı ayrı elde edilecektir.\nMıknatıs, su, süzgeç kâğıdı ve ısıtıcı kullanılabildiğine göre aşağıdaki işlem sıralarından hangisi bu amaca uygundur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Üç maddeyi ayıran doğru işlem sırası.',
 ip=['Her yöntemin hangi özellik farkına dayandığını düşün: mıknatıslanma, suda çözünme, buharlaşma.'],
 bilgi=[B('Fiziksel ayırma yöntemleri','Mıknatıs demir gibi mıknatıslanan maddeyi ayırır. Suda çözünen madde (tuz) ile çözünmeyen madde (kum) çözme ve süzme ile ayrılır. Buharlaştırma, çözünen katıyı çözeltiden geri kazanır')],
 ad=[A('Mıknatıs','Demir tozu mıknatısla çekilerek ayrılır.','kalan: kum + tuz'),A('Suda çözme ve süzme','Tuz suda çözünür, kum çözünmez; süzgeçte kum kalır.','süzgeçte: kum · süzüntü: tuzlu su'),A('Buharlaştırma','Tuzlu su ısıtılınca su uçar, tuz geride kalır.','geri kalan: tuz'),A('Şıkları ele','Sıra bu üç adıma uyan tek şıktır.','E: doğru · diğerleri: yanlış')],
 puf='Katı karışımlarda önce mıknatıs gibi doğrudan ayıranı, sonra çözme–süzme–buharlaştırma zincirini uygula.')
# ---- 0003
m,y,bu=300,20,100; tuz=Fr(m*y,100); yeni=tuz/(m-bu)*100
assert tuz==60 and yeni==30 and tuz/(m+bu)*100==15 and tuz/(m-tuz)*100==25
mk(P,'0003',tipId='kim-krs-buhar',tip='Buharlaştırma ve kütlece yüzde',z='orta',alt='Homojen ve Heterojen Karışımlar',kaz='Çözeltiden su buharlaştırıldığında kütlece yüzde derişimin değişimini hesaplar.',kalip='hikâyeli',adim=3,
 kart='K-KRSM-03 (buharlaştırma ile derişim) · %20’lik tuzlu su, 100 g su buharlaşıyor',
 metin='Kütlece %20’lik 300 g tuzlu su çözeltisi açık bir kapta ısıtılıyor ve çözeltideki sudan 100 g buharlaşıyor. Tuz buharlaşmamaktadır.\nBuna göre kalan çözeltinin kütlece yüzde derişimi kaçtır?',
 dogru=30,yan=[(15,'Buharlaşan suyu çözeltiye eklenmiş gibi hesaplayıp 60 ÷ 400 yapmış.','dikkat'),(20,'Derişimin değişmediğini sanmış; su azalınca yüzdenin arttığını fark etmemiş.','bilgi'),(25,'Tuz kütlesini çözeltiye değil, ilk çözelti kütlesinden tuz çıkarılmış suya (240 g) bölmüş.','islem'),(60,'Tuzun gram cinsinden kütlesini (60) yüzde değeri olarak yazmış.','dikkat')],
 istenen='Kalan çözeltinin kütlece yüzde derişimi (%).',
 ip=['Buharlaşan yalnızca sudur; tuzun kütlesi değişmez, çözeltinin kütlesi değişir.'],
 bilgi=[B('Kütlece yüzde','Kütlece yüzde derişim = çözünen kütlesi ÷ çözelti kütlesi × 100. Örnek: 20 g şekeri 80 g suda çözersen çözelti 100 g olur ve derişim %20 olur')],
 ad=[A('Tuz kütlesi','%20’lik 300 g çözeltide tuz miktarı bulunur.','tuz = 300 × 20 ÷ 100 = 60 g'),A('Yeni çözelti kütlesi','Yalnız su gittiği için tuz 60 g kalır.','çözelti = 300 − 100 = 200 g'),A('Yeni derişim','Tuz kütlesi yeni çözelti kütlesine bölünür.','60 ÷ 200 × 100 = %30')],
 puf='Su buharlaşınca çözünen kütlesi sabit kalır; yalnız çözelti kütlesi azalır, derişim artar.')
# ---- 0004
a1,y1,a2,y2=200,10,100,40; sk=Fr(a1*y1+a2*y2,100); yy=sk/(a1+a2)*100
assert sk==60 and yy==20 and Fr(y1+y2,2)==Fr(50,2) and sk/a1*100==30 and y1+y2==50
mk(P,'0004',tipId='kim-krs-karis',tip='İki çözeltiyi karıştırma',z='orta',alt='Homojen ve Heterojen Karışımlar',kaz='Aynı maddenin farklı derişimli iki çözeltisini karıştırdığında oluşan derişimi hesaplar.',kalip='hikâyeli',adim=3,
 kart='K-KRSM-04 (çözelti karıştırma) · %10’luk 200 g + %40’lık 100 g şekerli su',
 metin='Bir öğrenci, kütlece %10’luk 200 g şekerli su çözeltisi ile kütlece %40’lık 100 g şekerli su çözeltisini aynı kapta karıştırıyor.\nBuna göre oluşan çözeltinin kütlece yüzde derişimi kaçtır?',
 dogru=20,yan=[(10,'Karışımın derişimini küçük olan çözeltinin derişimine eşit sanmış.','bilgi'),(25,'İki derişimin aritmetik ortalamasını almış; çözelti kütlelerini hesaba katmamış.','bilgi'),(30,'Toplam şekeri (60 g) yalnız ilk çözeltinin kütlesine (200 g) bölmüş.','islem'),(50,'İki derişimi toplamış.','islem')],
 istenen='Oluşan çözeltinin kütlece yüzde derişimi (%).',
 ip=['Önce her çözeltideki şeker kütlesini bul; sonra şekerleri ve çözelti kütlelerini ayrı ayrı topla.'],
 bilgi=[B('Kütlece yüzde','Kütlece yüzde = çözünen kütlesi ÷ çözelti kütlesi × 100. Örnek: %10’luk 100 g çözeltide 10 g çözünen vardır')],
 ad=[A('Şeker kütleleri','Her çözeltideki şeker bulunur.','1. çözelti: 200 × 10 ÷ 100 = 20 g · 2. çözelti: 100 × 40 ÷ 100 = 40 g'),A('Toplamlar','Şekerler ve çözelti kütleleri toplanır.','şeker = 20 + 40 = 60 g · çözelti = 200 + 100 = 300 g'),A('Yeni derişim','Toplam şeker toplam çözeltiye bölünür.','60 ÷ 300 × 100 = %20')],
 puf='Çözeltileri karıştırırken derişimleri değil, çözünen ve çözelti kütlelerini topla.')
# ---- 0005
c20,c50,su=30,50,300; x50=Fr(c50*su,100); x20=Fr(c20*su,100); cok=x50-x20
assert x50==150 and x20==90 and cok==60 and (c50-c20)==20 and c20==30
mk(P,'0005',tipId='kim-krs-cozunurluk',tip='Soğutmada çöken madde miktarı',z='zor',alt='Homojen ve Heterojen Karışımlar',kaz='Çözünürlük verisinden soğutma sırasında çöken madde miktarını hesaplar.',kalip='tablo',adim=4,
 kart='K-KRSM-05 (çözünürlük) · 50 °C’de doygun çözelti 20 °C’ye soğutuluyor',
 metin='X katısının sudaki çözünürlüğü tabloda verilmiştir.\nSıcaklık (°C) | Çözünürlük (g X / 100 g su)\n20 | 30\n50 | 50\n50 °C’de 300 g su kullanılarak hazırlanan doygun X çözeltisi, hiçbir bileşen kaybedilmeden 20 °C’ye soğutuluyor.\nBuna göre kaç gram X katısı çöker?',
 dogru=60,yan=[(20,'100 g su için olan farkı (50 − 30) 300 g suya ölçeklememiş.','dikkat'),(30,'20 °C’deki çözünürlük değerini çöken miktar sanmış.','bilgi'),(90,'Soğutmadan sonra çözeltide kalan X miktarını çöken miktar sanmış.','dikkat'),(150,'50 °C’de çözünmüş toplam X miktarını çöken miktar sanmış.','dikkat')],
 istenen='20 °C’ye soğutulunca çöken X katısı kütlesi (g).',
 ip=['Çözünürlük 100 g su için verilmiştir; 300 g su için üç katını al. Çöken miktar iki sıcaklıktaki çözünen kütlelerinin farkıdır.'],
 bilgi=[B('Çözünürlük ve doygunluk','Çözünürlük, belirli sıcaklıkta 100 g suda çözünebilen en çok madde kütlesidir. Örnek: çözünürlük 30 g ise 200 g suda en çok 60 g çözünür'),B('Soğutma','Çözünürlük sıcaklıkla azalıyorsa doygun çözelti soğutulunca fazla madde katı olarak çöker')],
 ad=[A('50 °C’de çözünen','300 g su 100 g suyun 3 katıdır.','X = 50 × 3 = 150 g'),A('20 °C’de çözünebilen','Aynı 300 g su için 20 °C’deki sınır bulunur.','X = 30 × 3 = 90 g'),A('Çöken miktar','Fazla olan kısım katı olarak dibe çöker.','150 − 90 = 60 g')],
 puf='Çözünürlük 100 g su içindir; su kütlesi farklıysa önce oranla, sonra çıkar.')
# ---- 0006
d={'I':(True,'doygun çözelti o sıcaklıkta daha fazla katı çözemez, eklenen X dibe çöker'),
   'II':(True,'su eklenince çözücü artar ve çözelti aynı sıcaklıkta daha çok X çözebilir hâle gelir, yani doymamış olur'),
   'III':(False,'su buharlaşınca fazla kalan X dibe çöker ve sıcaklık sabit olduğundan doygun çözeltinin derişimi değişmez')}
r=onc(d,[('I',),('II',),('III',),('I','III'),('I','II')])
mk(P,'0006',tipId='kim-krs-doygun',tip='Doygun çözelti',z='zor',alt='Homojen ve Heterojen Karışımlar',kaz='Doygun bir çözeltide yapılan değişikliklerin sonucunu yorumlar.',kalip='öncüllü',adim=3,
 kart='K-KRSM-06 (doygun çözelti) · katı ekleme, su ekleme, su buharlaştırma',
 metin='Dibinde çözünmemiş katı bulunmayan, 20 °C’deki doygun bir X çözeltisi için aşağıdakiler söyleniyor.\nI. Sıcaklık değişmeden çözeltiye bir miktar X katısı eklenirse eklenen katı çözünmez.\nII. Sıcaklık değişmeden çözeltiye bir miktar su eklenirse çözelti doymamış hâle gelir.\nIII. Sıcaklık değişmeden çözeltiden bir miktar su buharlaştırılırsa çözeltinin kütlece yüzde derişimi artar.\nBuna göre hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan öncüller.',
 ip=['Doygun çözeltide aynı sıcaklıkta çözücü başına çözülebilen en çok madde miktarı sabittir.'],
 bilgi=[B('Doygun çözelti','Belirli sıcaklıkta daha fazla madde çözemeyen çözeltidir. Örnek: 100 g suyun çözebildiği en çok X 30 g ise 30 g X içeren çözelti doygundur, sıcaklık aynıysa derişimi hep aynıdır')],
 ad=[A('Katı eklemek','Çözelti zaten doygundur, ek katı çözünemez.','I: doğru'),A('Su eklemek','Çözücü arttığı için daha çok X çözülebilir; çözelti doymamış olur.','II: doğru'),A('Su buharlaştırmak','Çözülemeyen fazla X katı olarak çöker, doygun çözeltinin derişimi sabit kalır.','III: yanlış'),A('Sonuç','Doğru olanlar bir araya getirilir.',etk(d)+' · Sonuç: I ve II')],
 puf='Sıcaklık sabitse doygun çözeltinin derişimi sabittir; fazlası katı olarak çöker.')
bitir(P,'karisimlar','kim|Karışımlar')
