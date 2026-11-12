"""Hareket Hız Problemleri · parti 2 (hafif mod): 29 ana soru, kardeş yok, ipucu 1. Her cevap ve çeldirici kodla doğrulanır."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_mat as H
from _hafif_mat import *
H.KONU='Hareket Hız Problemleri'
UK='prob|Hareket Hız Problemleri'
P=Parti('hareketiki','Hareket Hız Problemleri',UK)
KY='ÖSYM 2018–2026 TYT Matematik (hareket problemleri) · yayın soru bankaları (yalnız mantık) · MEB 7–9. sınıf'
YHZ=B('Yol, hız, zaman','yol = hız × zaman. Örnek: saatte 60 km hızla 3 saatte 60 × 3 = 180 km gidilir')
BIRIM=B('Birim çevirme','1 km = 1000 m ve 1 saat = 3600 sn; 1 saat = 60 dakika. Örnek: 30 dakika = 30/60 = 0,5 saattir; 1 m/sn = 3600/1000 = 3,6 km/sa')
KARS=B('Karşılaşma','birbirine doğru giden iki hareketlide aradaki yol her saat hızlar toplamı kadar azalır. Örnek: 50 ve 70 km/sa ile 240 km arayla çıkanlar 240 ÷ 120 = 2 saat sonra karşılaşır')
YETIS=B('Yetişme','aynı yönde giden iki hareketlide arkadaki, her saat hızlar farkı kadar yaklaşır. Örnek: 10 km önde olan 15 km/sa’lik hareketliye 25 km/sa’lik hareketli 10 ÷ 10 = 1 saatte yetişir')
SBT=B('Sabit yolda hız ve süre','yol sabitse süre = yol ÷ hız olur; hız azalınca süre uzar. Örnek: 120 km yol 60 km/sa ile 2, 40 km/sa ile 3 saatte alınır')
ORTH=B('Ortalama hız','ortalama hız = toplam yol ÷ toplam süre; hızların ortalaması değildir. Örnek: 60 km’yi 30 km/sa ile (2 sa), 60 km’yi 60 km/sa ile (1 sa) giden araçta ortalama 120 ÷ 3 = 40 km/sa')
CEM=B('Çembersel pist','dairesel parkurda aynı noktadan zıt yöne çıkanlar, aralarındaki yol çevre kadar kapandığında karşılaşır (hızlar toplamı). Aynı yöne çıkanlar, hızlı olan yavaşı bir çevre kadar kazandığında yetişir (hızlar farkı). Örnek: çevre 100 m, hızlar 3 ve 2 m/sn ise zıt yönde 100 ÷ 5 = 20 sn, aynı yönde 100 ÷ 1 = 100 sn')
TUN=B('Uzunluklu cisim','tren gibi boyu olan bir cismin tünel ya da köprüyü tamamen geçmesi için aldığı yol, tren boyu + tünel boyu kadardır. Örnek: 100 m’lik tren 200 m’lik tüneli 20 m/sn ile (100 + 200) ÷ 20 = 15 sn’de geçer')
AKI=B('Akıntı','akıntı yönünde hız = tekne hızı + akıntı hızı; akıntıya karşı hız = tekne hızı − akıntı hızı. Örnek: tekne 10 km/sa, akıntı 2 km/sa ise yön boyunca 12, karşı yönde 8 km/sa')

kart('K-HRB-01','Yol–hız–zaman ve birim çevirme','yol = hız × zaman; dakika–saat ve m/sn–km/sa dönüşümleri yapılır, çok etaplı ya da kesirli bölümlü yolculukta her bölümün yolu ayrı hesaplanır.','Dakikayı saat sanmak; 3,6 yerine yanlış çarpan; etap hızlarını toplamak; yolun bölümlerini hıza göre ağırlıklandırmak.','kolay-orta','hikâyeli',3,'hrb-temel','Yol–hız–zaman ve birim çevirme',KY)
kart('K-HRB-02','Hız değişince süre ve yol (erken/geç varma)','Aynı yolu farklı hızla alınca süre farkından yol ya da planlanan süre bulunur; belirli bir toplam süre için ikinci yarının hızı bulunur.','Hız ortalamasını aritmetik almak; geç/erken sürelerini ters işaretlemek; yarı yol hızını ortalamayla karıştırmak.','orta-zor','hikâyeli',4,'hrb-erkengec','Farklı hızla aynı yol (erken/geç varma, planlanan süre)',KY)
kart('K-HRB-03','Karşılaşma ve yetişme','Zıt yönde hızlar toplamı, aynı yönde hızlar farkı kullanılır; varış noktasında dönen hareketlide aradaki yol yeniden kurulur.','Toplam ile farkı karıştırmak; başlangıç farkını unutmak; dönüş anını atlamak.','kolay-zor','hikâyeli',3,'hrb-karsilasma','Karşılaşma ve yetişme',KY)
kart('K-HRB-04','Ortalama hız ve mola','Ortalama hız toplam yolun toplam süreye bölümüdür; mola süresi toplam süreye girer ama hareket süresine girmez.','Hızların aritmetik ortalamasını almak; molayı iki kez çıkarmak ya da hiç çıkarmamak.','orta','hikâyeli',3,'hrb-ortalama','Ortalama hız ve mola',KY)
kart('K-HRB-05','Çembersel pist','Dairesel parkurda zıt yönde hızlar toplamı, aynı yönde hızlar farkı bir çevreyi kapatır; geç başlayan için önce ilk fark bulunur.','Çevreyi yanlış kullanmak; başlangıç farkını yola eklememek; karşılaşma sayısını karıştırmak.','orta','hikâyeli',3,'hrb-cember','Çembersel pistte karşılaşma ve yetişme',KY)
kart('K-HRB-06','Tren–tünel–köprü','Boyu olan cismin geçişinde alınan yol, cismin boyu ile engelin boyunun toplamıdır; iki trenin geçişinde boylar toplanır.','Tren boyunu unutmak; iki kez saymak; km/sa–m/sn dönüşümünü atlamak.','orta-zor','hikâyeli',4,'hrb-tunel','Tren, tünel ve köprü',KY)
kart('K-HRB-07','Akıntı ve yürüyen merdiven','Akıntı yönünde hızlar toplanır, karşı yönde çıkarılır; yürüyen merdivende kişi ve merdiven hızı birlikte düşünülür.','Toplam ile farkı karıştırmak; süreleri toplamak; hız yerine süreyi orantılamak.','orta-zor','hikâyeli',4,'hrb-akinti','Akıntı ve yürüyen merdiven',KY)
kart('K-HRB-08','Yeni nesil hareket','Verilen kurala göre tahmini varış ve rüzgâr–yer hızı ilişkisi çözülür.','Kuralı sorudaki duruma uygulamamak; birimleri karıştırmak.','orta-zor','yeni nesil',4,'hrb-yeninesil','Yeni nesil hareket: navigasyon ve dron',KY)
kart('K-HRB-09','Öncüllü hareket','Üç ifade hareket verileriyle tek tek sınanır.','Tek bir ifadeyi sınayıp bırakmak; ortalama hızı aritmetik almak.','orta','öncüllü',3,'hrb-oncullu','Öncüllü hareket yorumu',KY)
TIPAD={}
def M(no,tipId,tip,z,alt,kaz,kalip,kart,metin,dogru,yan,istenen,ip,bilgi,ad,puf,sira=None,sekil=None):
    mk(P,no,sekil=sekil,tipId=tipId,tip=tip,z=z,alt=alt,kaz=kaz,kalip=kalip,adim=len(ad),kart=kart,metin=metin,dogru=dogru,yan=yan,istenen=istenen,ip=[ip],bilgi=bilgi,ad=ad,puf=puf,sira=sira)
def yv(l): return [(v,c,t) for v,c,t in l]
TM='hrb-temel'; EG='hrb-erkengec'; KR='hrb-karsilasma'; OR='hrb-ortalama'; CM='hrb-cember'; TN='hrb-tunel'; AK='hrb-akinti'; YN='hrb-yeninesil'; ON='hrb-oncullu'
N={TM:'Yol–hız–zaman ve birim çevirme',EG:'Farklı hızla aynı yol (erken/geç varma, planlanan süre)',KR:'Karşılaşma ve yetişme',OR:'Ortalama hız ve mola',CM:'Çembersel pistte karşılaşma ve yetişme',TN:'Tren, tünel ve köprü',AK:'Akıntı ve yürüyen merdiven',YN:'Yeni nesil hareket: navigasyon ve dron',ON:'Öncüllü hareket yorumu'}
def Q(no,tipId,z,alt,kaz,kalip,kart,metin,dogru,yan,istenen,ip,bilgi,ad,puf,sira=None,sekil=None):
    M(no,tipId,N[tipId],z,alt,kaz,kalip,kart,metin,dogru,yan,istenen,ip,bilgi,ad,puf,sira,sekil)

# 01 kolay: m/sn -> km/sa
v=5; assert Fr(v*3600,1000)==18 and v*3600==18000 and Fr(v*3600,100)==180 and Fr(v*3600,10000)==Fr(9,5) and Fr(v*60,1000)==Fr(3,10)
Q('0001',TM,'kolay','Birim Çevirme','Saniyede metre cinsinden verilen hızı saatte kilometreye çevirir.','hikâyeli','K-HRB-01 (yol–hız–zaman, birim çevirme) · m/sn → km/sa',
 'Bir bisikletli, düz bir yolda sabit 5 m/sn hızla ilerlemektedir.\nBuna göre bisikletlinin hızı saatte kaç kilometredir?',
 18,[(18000,'Bir saatteki metreyi (18 000 m) bulup kilometreye çevirmeyi unutmuş.','dikkat'),(180,'1 km’yi 100 m sanmış.','bilgi'),(Fr(9,5),'1 km’yi 10 000 m sanmış.','bilgi'),(Fr(3,10),'Dakikadaki metreyi (300 m) bulup saate çıkmamış, yalnızca kilometreye çevirmiş.','dikkat')],
 'Bisikletlinin hızı (km/sa).','Hızın metre ve saniye cinsinden değerini kilometre ve saat cinsinden yazmak için hangi iki dönüşüm gerekir?',[YHZ,BIRIM],
 [A('Bir saatteki yol','1 saatte 3600 sn vardır.','5 × 3600 = 18 000 m'),A('Kilometreye çevir','1 km = 1000 m.','18 000 ÷ 1000 = 18 km'),A('Sonuç','Bir saatte alınan yol hızdır.','18 km/sa')],
 'm/sn değerini km/sa’ya çevirmek için 3,6 ile çarp; km/sa değerini m/sn’ye çevirmek için 3,6’ya böl.')

# 02 kolay: 45 dk
assert 80*Fr(45,60)==60 and 80*Fr(45,100)==36 and 80*Fr(3,2)==120 and 80*Fr(9,2)==360 and 80*45==3600
Q('0002',TM,'kolay','Yol–Hız–Zaman','Dakika cinsinden verilen süreyi saate çevirerek alınan yolu hesaplar.','hikâyeli','K-HRB-01 (yol–hız–zaman) · dakikadan yol',
 'Bir motosikletli, sabit 80 km/sa hızla 45 dakika yol alıyor.\nBuna göre motosikletli bu sürede kaç kilometre yol almıştır?',
 60,[(36,'45 dakikayı 0,45 saat sanmış.','bilgi'),(120,'45 dakikayı 1,5 saat sanmış.','bilgi'),(360,'45 dakikayı 4,5 saat sanmış.','bilgi'),(3600,'Hızı dakika ile çarpmış, süreyi saate çevirmemiş.','dikkat')],
 'Alınan yol (km).','Hız saat başına verildiği için süreyi hangi birimde yazman gerekir?',[YHZ,BIRIM],
 [A('Süreyi saate çevir','1 saat = 60 dakika.','45 dakika = 45/60 = 3/4 saat'),A('Yolu hesapla','yol = hız × zaman.','80 × 3/4'),A('Sonuç','Çarpımı bul.','60 km')],
 'Hız saatle verilmişse süreyi önce saate çevir: dakika ÷ 60.')

# 03 kolay: tren karşılaşma
assert Fr(360,90+150)*60==90 and Fr(360,150-90)*60==360 and Fr(360,150)*60==144 and Fr(360,90)*60==240 and Fr(360,240)==Fr(3,2)
Q('0003',KR,'kolay','Karşılaşma','Birbirine doğru giden iki trenin karşılaşma süresini hızlar toplamıyla bulur.','hikâyeli','K-HRB-03 (karşılaşma) · iki tren, süre dakika olarak',
 'Aralarında 360 km bulunan iki istasyondan iki tren aynı anda birbirine doğru hareket ediyor. Trenler sabit 90 km/sa ve 150 km/sa hızla gidiyor.\nBuna göre trenler kaç dakika sonra karşılaşır?',
 90,[(360,'Hızların farkını (60 km/sa) kullanıp 6 saati dakikaya çevirmiş.','bilgi'),(144,'Yolu yalnızca hızlı trenin hızına bölmüş.','bilgi'),(240,'Yolu yalnızca yavaş trenin hızına bölmüş.','bilgi'),(Fr(3,2),'Saat cinsinden bulduğu 1,5’i dakikaya çevirmeyi unutmuş.','dikkat')],
 'Karşılaşma süresi (dakika).','Aradaki yol her saat toplam kaç km kısalıyor?',[KARS,BIRIM],
 [A('Yaklaşma hızı','Zıt yönde hızlar toplanır.','90 + 150 = 240 km/sa'),A('Süreyi bul','süre = yol ÷ hız.','360 ÷ 240 = 1,5 saat'),A('Dakikaya çevir','1 saat = 60 dakika.','1,5 × 60 = 90 dakika')],
 'Birbirine doğru giden iki hareketlinin karşılaşma süresi, aradaki yolun hızlar toplamına bölümüdür.')

# 04 kolay: yürüyen bant
assert Fr(30,Fr(1,2))==60 and 30*Fr(1,2)==15 and Fr(30,5)==6 and 30-Fr(1,2)==Fr(59,2) and Fr(30,Fr(1,20))==600
Q('0004',AK,'kolay','Yürüyen Bant','Yürüyen bantta hareketsiz duran kişinin bant hızıyla gittiği süreyi bulur.','hikâyeli','K-HRB-07 (yürüyen bant) · hareketsiz yolcu',
 'Bir havalimanındaki yürüyen bant, sabit 0,5 m/sn hızla ilerlemektedir. Bandın uzunluğu 30 m’dir.\nBandın üzerinde hareketsiz duran bir yolcu, bandın bir ucundan diğer ucuna kaç saniyede ulaşır?',
 60,[(15,'Uzunluğu hızla çarpmış: 30 × 0,5.','bilgi'),(6,'0,5 yerine 5 alarak 30 ÷ 5 hesaplamış.','islem'),(Fr(59,2),'Uzunluktan hızı çıkarmış: 30 − 0,5.','bilgi'),(600,'0,5’i 0,05 sanıp 30 ÷ 0,05 hesaplamış.','islem')],
 'Yolcunun bandın sonuna ulaşma süresi (sn).','Yolcu kendisi yürümediğine göre yalnızca bandın hızıyla ilerler; hız, yol ve süre arasındaki bağıntıyı yaz.',[YHZ],
 [A('Yolcunun hızı','Yolcu yürümüyor, hızı bandın hızıdır.','v = 0,5 m/sn'),A('Süre formülü','süre = yol ÷ hız.','t = 30 ÷ 0,5'),A('Sonuç','Bölmeyi yap.','60 sn')],
 'Süre = yol ÷ hız; ondalık hıza bölerken hem yolu hem hızı 10 ile genişletmek işi kolaylaştırır.')

# 05 kolay: yolun 2/3'ü
assert 36*2//12==6 and Fr(2,3)*36==24 and Fr(24,12)==2 and Fr(36,12)==3 and Fr(1,3)*36/12==1 and Fr(3,2)*36/12==Fr(9,2)
Q('0005',TM,'kolay','Yolun Kesri','Yolun bir kesri için geçen süreyi yol ÷ hız ile bulur.','hikâyeli','K-HRB-01 (yol–hız–zaman) · yolun kesri',
 'Bir bisikletli 36 km uzunluğundaki bir yolun 2/3’ünü sabit 12 km/sa hızla gidiyor.\nBuna göre bu bölümü kaç saatte alır?',
 2,[(6,'Kesri 2/3 yerine 2 ile çarpmış: 36 × 2 ÷ 12.','bilgi'),(3,'Yolun tamamını (36 ÷ 12) hesaplamış.','dikkat'),(Fr(9,2),'Kesri ters kullanıp yolun 3/2’sini almış.','bilgi'),(24,'Yolun 2/3’ünü (24 km) bulup hıza bölmeyi unutmuş.','dikkat')],
 'Yolun 2/3’ünü alma süresi (saat).','Önce gidilen bölümün kaç km olduğunu bul.',[YHZ],
 [A('Bölümün uzunluğu','Yolun 2/3’ü.','36 × 2/3 = 24 km'),A('Süre formülü','süre = yol ÷ hız.','24 ÷ 12'),A('Sonuç','Bölmeyi yap.','2 saat')],
 'Yolun bir kesri sorulduğunda önce o kesrin kaç km olduğunu bul, sonra hıza böl.')

# 06 kolay: tablo
y1,y2,y3=2*30,1*60,3*45; top=y1+y2+y3; assert top==255 and 30+60+45==135 and 6*45==270 and 6*60==360 and y1+y2==120
Q('0006',TM,'kolay','Etaplı Yolculuk','Etaplara ait süre ve hız bilgisinden toplam yolu hesaplar.','tablo','K-HRB-01 (yol–hız–zaman) · tabloda üç etap',
 'Bir kurye aracının bir sabahki yolculuğu, her etapta sabit hızla olmak üzere aşağıdaki tabloda verilmiştir.\nBuna göre araç bu yolculukta toplam kaç kilometre yol almıştır?',
 255,[(120,'Üçüncü etabı hesaba katmamış.','dikkat'),(135,'Üç hızı toplamış.','bilgi'),(270,'Hızların aritmetik ortalaması olan 45’i toplam süreyle (6 saat) çarpmış.','bilgi'),(360,'Toplam süreyi (6 saat) en yüksek hızla çarpmış.','bilgi')],
 'Toplam yol (km).','Her etapta yolu ayrı ayrı bulmak için tablonun hangi iki sütununu kullanmalısın?',[YHZ],
 [A('1. etap','yol = hız × zaman.','30 × 2 = 60 km'),A('2. etap','Aynı bağıntıyı uygula.','60 × 1 = 60 km'),A('3. etap','Aynı bağıntıyı uygula.','45 × 3 = 135 km'),A('Topla','Etap yollarını topla.','60 + 60 + 135 = 255 km')],
 'Etaplı yolculukta her etabın yolunu hız × süre ile ayrı bul, sonra topla.',
 sekil=tablo_svg(['Etap','Süre','Hız'],[['1','2 saat','30 km/sa'],['2','1 saat','60 km/sa'],['3','3 saat','45 km/sa']]))

# 07 orta: tren gecikme
v1,v2=90,60; gec=Fr(4,3); d=Fr(v1*v2,v1-v2)*gec; assert d==240 and Fr(d,v2)-Fr(d,v1)==gec
assert 30*gec==40 and 60*gec==80 and 90*gec==120 and Fr(v1*v2,v1-v2)*Fr(6,5)==216
Q('0007',EG,'orta','Geç Varış','Planlanan hız ve gerçek hızdaki süre farkından yolu bulur.','hikâyeli','K-HRB-02 (hız değişince süre) · arızalı tren, tek geç kalma',
 'Bir yolcu treni, A ile B arasındaki yolu tarifeye göre sabit 90 km/sa hızla alacaktır. Arıza nedeniyle tren yolun tamamında sabit 60 km/sa hızla gidiyor ve B’ye tarifeden 1 saat 20 dakika geç varıyor.\nBuna göre A ile B arasındaki yol kaç kilometredir?',
 240,[(40,'Hızlar farkını (30 km/sa) gecikmeyle çarpmış.','bilgi'),(80,'Gecikmeyi yalnızca yavaş hızla çarpmış: 60 × 4/3.','bilgi'),(120,'Gecikmeyi yalnızca tarifedeki hızla çarpmış: 90 × 4/3.','bilgi'),(216,'1 saat 20 dakikayı 1,2 saat sanmış.','bilgi')],
 'A ile B arasındaki yol (km).','Yol aynı olduğuna göre iki durumdaki süreleri yola bağlı yaz.',[YHZ,SBT,BIRIM],
 [A('Süreleri yazma','Yol d olsun. t = d ÷ hız.','tarife: d/90 · gerçek: d/60'),A('Gecikmeyi kur','1 saat 20 dk = 4/3 saat.','d/60 − d/90 = 4/3'),A('Denklemi çöz','Paydaları 180’de eşitle.','(3d − 2d)/180 = 4/3 → d/180 = 4/3'),A('Yolu bul','Her iki yanı 180 ile çarp.','d = 240 km')],
 'Yol sabitse süre farkı, yolun hıza bölümlerinin farkıdır: d/v₂ − d/v₁ = fark.')

# 08 orta: yetişme
va,vb,fark=15,20,10; t=Fr(fark,vb-va); assert t==2 and vb*t==40 and va*t==30 and fark+vb*t==50 and va*t+vb*t==70
Q('0008',KR,'orta','Yetişme','Aynı yönde giden iki hareketlinin yetişme süresini hız farkıyla bulur ve alınan yolu hesaplar.','hikâyeli','K-HRB-03 (yetişme) · iki bisikletli, aynı anda, aralarında fark',
 'Bir bisiklet yolunda Hakan, Gizem’in 10 km önündedir. Hakan ve Gizem aynı anda, aynı yönde yola çıkıyor; Hakan sabit 15 km/sa, Gizem sabit 20 km/sa hızla gidiyor.\nBuna göre Gizem, Hakan’a yetiştiği anda yola çıktığı yerden itibaren kaç km yol almış olur?',
 40,[(10,'Başlangıçtaki uzaklığı (10 km) yol sanmış.','dikkat'),(30,'Hakan’ın aldığı yolu bulmuş.','dikkat'),(50,'Gizem’in yoluna başlangıç farkını da eklemiş.','bilgi'),(70,'İki hareketlinin aldığı yolların toplamını yazmış.','bilgi')],
 'Gizem’in yetişme anına kadar aldığı yol (km).','Gizem her saat Hakan’a kaç km yaklaşıyor?',[YETIS,YHZ],
 [A('Yaklaşma hızı','Aynı yönde hızlar çıkarılır.','20 − 15 = 5 km/sa'),A('Yetişme süresi','Başlangıç farkını kapatma süresi.','10 ÷ 5 = 2 saat'),A('Gizem’in yolu','yol = hız × zaman.','20 × 2 = 40 km')],
 'Aynı yönde giden iki hareketlide başlangıç farkı, hızlar farkına bölünerek yetişme süresi bulunur.')

# 09 orta: çember zıt
C,va,vb=3,18,12; t=Fr(C,va+vb)*60; assert t==6 and Fr(C,va-vb)*60==30 and Fr(C,va)*60==10 and Fr(C,vb)*60==15 and Fr(C,va+vb)==Fr(1,10)
Q('0009',CM,'kolay','Çembersel Pist','Çembersel parkurda zıt yöne çıkan iki hareketlinin ilk karşılaşma süresini hızlar toplamıyla bulur.','hikâyeli','K-HRB-05 (çembersel pist) · zıt yön, km ve dakika',
 'Çevresi 3 km olan dairesel bir göl çevresi parkurunda iki bisikletli, aynı noktadan aynı anda zıt yönlere doğru yola çıkıyor. Bisikletliler sabit 18 km/sa ve 12 km/sa hızla gidiyor.\nBuna göre bisikletliler, başlangıç anı sayılmazsa, ilk kez kaç dakika sonra karşılaşır?',
 6,[(Fr(1,10),'Saat cinsinden bulduğu 0,1’i dakikaya çevirmeyi unutmuş.','dikkat'),(10,'Çevreyi yalnızca hızlı bisikletlinin hızına bölmüş.','bilgi'),(15,'Çevreyi yalnızca yavaş bisikletlinin hızına bölmüş.','bilgi'),(30,'Hızların farkını almış: 3 ÷ 6 = 0,5 saat = 30 dakika.','bilgi')],
 'İlk karşılaşma süresi (dakika).','Zıt yönde giden iki bisikletli arasındaki yol, ilk karşılaşmada toplam ne kadar kapanmış olur?',[CEM,BIRIM],
 [A('Kapanan yol','İlk karşılaşmada ikisi toplam bir çevre kadar yol alır.','3 km'),A('Hızlar toplamı','Zıt yönde hızlar toplanır.','18 + 12 = 30 km/sa'),A('Süreyi bul','3 ÷ 30 = 0,1 saat.','0,1 × 60 = 6 dakika')],
 'Çembersel pistte zıt yönlerde ilk karşılaşma süresi, çevrenin hızlar toplamına bölümüdür.')

# 10 zor: pist 3. karşılaşma noktası
C,va,vb=500,4,6; t1=Fr(C,va+vb); t3=3*t1; ece=va*t3; assert t1==50 and t3==150 and ece==600 and ece%C==100 and min(ece%C,C-ece%C)==100
assert C-100==400 and va*t1==200 and vb*t3==900
for n in (1,2,3): assert min((va*n*t1)%C,C-(va*n*t1)%C)==(200 if n==1 else 100)
Q('0010',CM,'zor','Karşılaşma Noktası','Çembersel pistte zıt yönlü üçüncü karşılaşmanın konumunu başlangıç noktasına göre bulur.','hikâyeli','K-HRB-05 (çembersel pist) · üçüncü karşılaşmanın konumu',
 'Çevresi 500 m olan dairesel bir koşu pistinde Ece ile Tolga, pistin O noktasından aynı anda zıt yönlerde koşmaya başlıyor. Ece sabit 4 m/sn, Tolga sabit 6 m/sn hızla koşuyor.\nBaşlangıç anı sayılmadığına göre, ikisinin üçüncü kez karşılaştığı nokta O noktasına pist üzerinde en kısa yoldan kaç metre uzaklıktadır?',
 100,[(200,'İlk karşılaşmanın (Ece 50 sn × 4 m/sn) uzaklığını yazmış.','dikkat'),(400,'Uzaklığı 500 − 100 hesaplayıp uzun yoldan ölçmüş.','dikkat'),(600,'Ece’nin 150 saniyede koştuğu yolu O’ya uzaklık sanmış; tam turu çıkarmamış.','dikkat'),(900,'Tolga’nın koştuğu yolu O’ya uzaklık sanmış.','dikkat')],
 'Üçüncü karşılaşma noktasının O’ya pist üzerindeki en kısa uzaklığı (m).','Üçüncü karşılaşmaya kadar geçen süreyi bulup bir koşucunun aldığı yolu çevreyle karşılaştır.',[CEM,YHZ],
 [A('Karşılaşma aralığı','Zıt yönde hızlar toplanır; her karşılaşmada bir çevre kapanır.','500 ÷ (4 + 6) = 50 sn'),A('Üçüncü karşılaşma','3 × 50 sn.','150 sn'),A('Ece’nin yolu','yol = hız × zaman.','4 × 150 = 600 m'),A('Tam turu çıkar','Bir tur 500 m.','600 − 500 = 100 m'),A('En kısa uzaklık','100 m ile 500 − 100 = 400 m’den küçüğü.','100 m')],
 'Çembersel pistte konum için aldığı yoldan tam turları çıkar; kalan yol ile çevreden kalanın küçüğü en kısa uzaklıktır.')

# 11 orta: tünel
L,T,v=150,450,Fr(72*1000,3600); assert v==20 and Fr(L+T,v)==30 and Fr(L,v)==Fr(15,2) and Fr(T-L,v)==15 and Fr(T,v)==Fr(45,2) and Fr(T+2*L,v)==Fr(75,2)
Q('0011',TN,'orta','Tünelden Geçiş','Boyu olan trenin tüneli tamamen geçme süresini tren boyu ile tünel boyunu toplayarak bulur.','hikâyeli','K-HRB-06 (tren–tünel) · km/sa dönüşümlü',
 'Boyu 150 m olan bir tren, uzunluğu 450 m olan bir tünele sabit 72 km/sa hızla giriyor.\nTrenin ön ucu tünele girdiği andan arka ucu tünelden tamamen çıktığı ana kadar kaç saniye geçer?',
 30,[(Fr(15,2),'Yalnızca tren boyunu (150 m) hıza bölmüş.','dikkat'),(15,'Trenin tünelde tamamen içeride kaldığı süreyi bulmuş: (450 − 150) ÷ 20.','dikkat'),(Fr(45,2),'Yalnızca tünel boyunu (450 m) hıza bölmüş.','dikkat'),(Fr(75,2),'Tren boyunu iki kez eklemiş: (450 + 150 + 150) ÷ 20.','islem')],
 'Geçiş süresi (sn).','Trenin son vagonu tünelden çıktığında, ön ucu giriş noktasına göre ne kadar yol almış olur?',[TUN,BIRIM],
 [A('Hızı m/sn yap','72 km/sa ÷ 3,6.','72 ÷ 3,6 = 20 m/sn'),A('Alınan yol','Ön uç, tünelin uzunluğu ile tren boyu kadar ilerler.','450 + 150 = 600 m'),A('Süreyi bul','süre = yol ÷ hız.','600 ÷ 20 = 30 sn')],
 'Tren tüneli (köprüyü) tamamen geçerken alınan yol = tren boyu + tünel boyu.')

# 12 zor: köprü + direk
Bk=480; t1,t2=40,16
Ltr=Fr(Bk*t2,t1-t2); vv=Fr(Ltr,t2); assert Ltr==320 and vv==20 and (Ltr+Bk)/vv==40 and vv*Fr(36,10)==72
assert Fr(Bk,t1)*Fr(36,10)==Fr(216,5) and Fr(320,40)*Fr(36,10)==Fr(144,5) and Fr(144,5)==Fr('28.8') and Fr(Bk,t2)==30
Q('0012',TN,'zor','Köprü ve Direk','Köprüyü geçiş ve direği geçiş sürelerinden tren boyunu ve hızını bulur.','hikâyeli','K-HRB-06 (tren–köprü–direk) · iki süreden hız',
 'Sabit hızla giden bir tren, 480 m uzunluğundaki bir köprüye girdiği andan tamamen çıktığı ana kadar 40 saniye geçiriyor. Aynı tren köprü üzerindeki bir ışık direğinin yanından 16 saniyede geçiyor.\nBuna göre trenin hızı saatte kaç kilometredir?',
 72,[(20,'Hızı m/sn olarak bulup km/sa’ya çevirmemiş.','dikkat'),(30,'Köprü boyunu direği geçiş süresine bölüp m/sn değerini km/sa sanmış.','bilgi'),(Fr(216,5),'Köprü boyunu tüm geçiş süresine bölüp (12 m/sn) tren boyunu hesaba katmamış.','bilgi'),(Fr(144,5),'Tren boyunu (320 m) köprü geçiş süresine bölüp 8 m/sn bulmuş: 8 × 3,6 = 28,8 km/sa.','bilgi')],
 'Trenin hızı (km/sa).','Direğin yanından geçerken ve köprüden geçerken tren hangi uzunluklar kadar yol alır; ikisini karşılaştır?',[TUN,BIRIM],
 [A('Boyu hıza bağla','Direği geçerken yol tren boyu L’dir; hız v = L ÷ 16.','L = 16v'),A('Köprü geçişi','Yol = L + 480, süre 40 sn.','L + 480 = 40v'),A('Boyu çıkar','L yerine 16v yaz.','16v + 480 = 40v → 24v = 480'),A('Hızı bul','Önce m/sn.','v = 20 m/sn (tren boyu 320 m)'),A('km/sa’ya çevir','m/sn değerini 3,6 ile çarp.','20 × 3,6 = 72 km/sa')],
 'İki farklı engelin geçiş süreleri verildiğinde tren boyunu L, hızını v alıp iki denklemi karşılaştır.')
# not: 30 seçeneği 108 ile aynı hatadan; ayrı hata: 30 m/sn

# 13 orta: iki tren zıt yön
La,Lb,va,vb=100,260,15,25; assert Fr(La+Lb,va+vb)==9 and Fr(Lb,va+vb)==Fr(13,2) and Fr(La+Lb,vb)==Fr(72,5) and Fr(La+Lb,va)==24 and Fr(La+Lb,vb-va)==36 and 54*Fr(10,36)==va and 90*Fr(10,36)==vb
Q('0013',TN,'orta','İki Trenin Geçişi','Zıt yönde giden iki trenin birbirini geçme süresini boyları toplayıp hızlar toplamına bölerek bulur.','hikâyeli','K-HRB-06 (iki tren) · zıt yönde birbirini geçme',
 'Boyları 100 m ve 260 m olan iki tren, paralel raylarda birbirine doğru sırasıyla sabit 54 km/sa ve 90 km/sa hızla gidiyor.\nTrenlerin ön uçları yan yana geldiği andan arka uçları yan yana geldiği ana kadar kaç saniye geçer?',
 9,[(Fr(13,2),'Yalnızca uzun trenin boyunu hesaba katmış.','dikkat'),(Fr(72,5),'Toplam boyu yalnızca hızlı trenin hızına bölmüş.','bilgi'),(24,'Toplam boyu yalnızca yavaş trenin hızına bölmüş.','bilgi'),(36,'Zıt yönde olmalarına rağmen hızları çıkarmış (aynı yönde gibi).','bilgi')],
 'Geçiş süresi (sn).','İki trenin birbirini tamamen geçmesi için birlikte ne kadar yol almaları gerekir?',[TUN,KARS,BIRIM],
 [A('Hızları m/sn yap','km/sa değerlerini 3,6’ya böl.','54 ÷ 3,6 = 15 m/sn · 90 ÷ 3,6 = 25 m/sn'),A('Yaklaşma hızı','Zıt yönde hızlar toplanır.','15 + 25 = 40 m/sn'),A('Toplam yol','İki trenin boyları toplanır.','100 + 260 = 360 m'),A('Süreyi bul','360 ÷ 40.','9 sn')],
 'İki tren birbirini geçerken alınan yol boyların toplamıdır; zıt yönde hızlar toplanır, aynı yönde çıkarılır.')

# 14 zor: akıntı, tahta parçası
d,tf,tb=60,3,5; vf=Fr(d,tf); vbk=Fr(d,tb); u=(vf-vbk)/2; tekne=(vf+vbk)/2; assert (vf,vbk,u,tekne)==(20,12,4,16) and Fr(d,u)==15
assert Fr(d,vf-vbk)==Fr(15,2) and Fr(d,tekne)==Fr(15,4) and tf+tb==8 and Fr(d,vbk)==5
Q('0014',AK,'zor','Akıntı','İki yöndeki sürelerden akıntı hızını bulup akıntıyla sürüklenen cismin süresini hesaplar.','hikâyeli','K-HRB-07 (akıntı) · iki süreden akıntıyla sürüklenen cisim',
 'Bir nehirde iki iskele arasındaki yol 60 km’dir. Durgun suda sabit hızla giden bir tekne bu yolu akıntı yönünde 3 saatte, akıntıya karşı 5 saatte alıyor. Akıntının hızı da sabittir.\nAkıntı yönünde bırakılan bir tahta parçası, yalnızca akıntıyla sürüklenerek aynı iki iskele arasındaki yolu kaç saatte alır?',
 15,[(Fr(15,4),'Teknenin durgun sudaki hızını (16 km/sa) tahtanın hızı sanmış.','dikkat'),(5,'Teknenin akıntıya karşı yolculuk süresini yazmış.','dikkat'),(Fr(15,2),'İki yöndeki hızların farkını (8 km/sa) akıntı hızı sanmış.','bilgi'),(8,'İki yolculuğun sürelerini toplamış: 3 + 5.','dikkat')],
 'Tahta parçasının iki iskele arasını alma süresi (saat).','Tahta parçasının hızı, tekne hızından bağımsız olarak hangi büyüklüğe eşittir?',[AKI,YHZ],
 [A('Bileşke hızlar','hız = yol ÷ süre.','akıntı yönünde 60 ÷ 3 = 20 · karşı yönde 60 ÷ 5 = 12'),A('Denklemleri yaz','Tekne hızı v, akıntı hızı u.','v + u = 20 · v − u = 12'),A('Akıntı hızı','Taraf tarafa çıkar.','2u = 8 → u = 4 km/sa'),A('Tahtanın hızı','Tahta yalnızca akıntıyla gider.','4 km/sa'),A('Süreyi bul','süre = yol ÷ hız.','60 ÷ 4 = 15 saat')],
 'Akıntıyla sürüklenen cismin hızı akıntı hızına eşittir; akıntı hızı iki bileşke hızın farkının yarısıdır.')

# 15 zor: tekne gidiş-dönüş saati
d,v,u,mola=48,12,4,Fr(1,2); t_ak=Fr(d,v+u); t_kr=Fr(d,v-u); ts=t_ak+mola+t_kr; assert (t_ak,t_kr,ts)==(3,6,Fr(19,2)) and 8+ts==Fr(35,2)
assert 8+t_ak+t_kr==17 and 8+2*Fr(d,v)+mola==Fr(33,2) and 8+2*t_ak+mola==Fr(29,2) and 8+2*t_kr+mola==Fr(41,2)
Q('0015',AK,'orta','Gidiş–Dönüş Akıntı','Akıntı yönü ve karşısındaki hızlarla gidiş–dönüş süresini ve beklemeyi birleştirerek dönüş saatini bulur.','hikâyeli','K-HRB-07 (akıntı) · gidiş–dönüş ve bekleme, saat sorusu',
 'Durgun suda sabit 12 km/sa hızla giden bir tekne, akıntının sabit 4 km/sa hızla aktığı bir nehirde A iskelesinden saat 08.00’de hareket edip akıntı yönünde 48 km uzaktaki B iskelesine gidiyor. Tekne B’de 30 dakika bekledikten sonra aynı yoldan A’ya dönüyor. İskelelere yanaşma ve kalkış için ayrıca süre harcanmıyor.\nBuna göre tekne A’ya saat kaçta döner?',
 '17.30',[('14.30','Dönüşü de akıntı yönünde hesaplamış: 3 + 3 + 0,5.','bilgi'),('16.30','Akıntıyı yok sayıp tekne hızını (12 km/sa) kullanmış: 4 + 4 + 0,5.','bilgi'),('17.00','30 dakikalık beklemeyi eklememiş.','dikkat'),('20.30','Gidişi de akıntıya karşı hesaplamış: 6 + 6 + 0,5.','bilgi')],
 'Teknenin A’ya dönüş saati.','Gidiş ve dönüşte tekneyi etkileyen hızı ayrı ayrı yaz.',[AKI,YHZ],
 [A('Gidiş hızı ve süresi','Akıntı yönünde hızlar toplanır.','12 + 4 = 16 km/sa · 48 ÷ 16 = 3 saat'),A('Dönüş hızı ve süresi','Akıntıya karşı hızlar çıkarılır.','12 − 4 = 8 km/sa · 48 ÷ 8 = 6 saat'),A('Toplam süre','Bekleme süresi de eklenir.','3 + 0,5 + 6 = 9,5 saat'),A('Saati bul','08.00 + 9 saat 30 dakika.','17.30')],
 'Akıntılı gidiş–dönüşte iki yönün hızları ayrı alınır; bekleme süresi toplam süreye eklenir.',
 sira=['14.30','16.30','17.00','17.30','20.30'])

# 16 zor: yürüyen merdiven
t_dur,t_yur=40,24; vk=Fr(1,t_yur)-Fr(1,t_dur); assert Fr(1,vk)==60 and t_dur+t_yur==64 and t_dur-t_yur==16 and Fr(t_dur+t_yur,2)==32 and Fr(1,Fr(1,t_yur)+Fr(1,t_dur))==15
Q('0016',AK,'orta','Yürüyen Merdiven','Yürüyen merdivende kişi ve merdivenin hızlarını ayırarak durmuş merdivendeki süreyi bulur.','hikâyeli','K-HRB-07 (yürüyen merdiven) · iki süreden kişinin kendi hızı',
 'Bir alışveriş merkezindeki yürüyen merdivenin tam çıkış yolunu, merdivende hareketsiz duran bir kişi 40 saniyede çıkıyor. Aynı kişi, çalışan merdivende sabit hızla yürüyerek aynı yolu 24 saniyede çıkıyor.\nBuna göre bu kişi, çalışmayan (durmuş) merdiveni aynı hızla yürüyerek kaç saniyede çıkar?',
 60,[(15,'İki hızın toplamına karşılık gelen süreyi bulmuş: 1 ÷ (1/24 + 1/40).','bilgi'),(16,'İki süreyi çıkarmış: 40 − 24.','bilgi'),(32,'İki sürenin aritmetik ortalamasını almış.','bilgi'),(24,'Kişinin çalışan merdivende yürüyerek çıkma süresini (24 sn) yazmış.','dikkat')],
 'Kişinin durmuş merdiveni yürüyerek çıkma süresi (sn).','Yolu 1 birim alıp her durumdaki hızı birim/saniye olarak yaz.',[YHZ,B('Hızların toplanması','merdiven ve kişi aynı yönde ilerliyorsa yer hızları toplanır. Örnek: merdiven 1 m/sn, kişi 2 m/sn ise toplam 3 m/sn')],
 [A('Yolu 1 birim al','Her durum için hız = 1 ÷ süre.','merdiven: 1/40 · merdiven + kişi: 1/24'),A('Kişinin hızı','Toplam hızdan merdivenin hızını çıkar.','1/24 − 1/40 = (5 − 3)/120'),A('Sadeleştir','Payı ve paydayı ikiye böl.','1/60 birim/sn'),A('Süreyi bul','süre = yol ÷ hız.','1 ÷ (1/60) = 60 sn')],
 'Yürüyen merdivende yolu 1 birim alıp hızları 1/süre olarak yaz; kişinin kendi hızı toplam hızdan merdiven hızı çıkarılarak bulunur.')

# 17 orta: öncüllü yetişme
h1,h2,bas=40,60,1; t=Fr(h1*bas,h2-h1); assert t==2 and 9+t==11 and h2*t==120 and 8+3==11 and h1*(bas+t)==120
Q('0017',ON,'orta','Öncüllü Yetişme','Geç çıkan aracın yetişme saatini, yetişme noktasını ve ilk aracın yolda kalma süresini öncüllerle sınar.','öncüllü','K-HRB-09 (öncüllü hareket) · yetişme, doğru I ve III',
 'Bir servis aracı saat 08.00’de A noktasından sabit 40 km/sa hızla yola çıkıyor. İkinci bir araç, saat 09.00’da aynı noktadan aynı yolu izleyerek sabit 60 km/sa hızla yola çıkıyor. İki araç da yol boyunca hiç durmuyor.\nBuna göre,\nI. İkinci araç, birinciye saat 11.00’de yetişir.\nII. Yetişme noktası A’dan 100 km uzaklıktadır.\nIII. Yetişme anında birinci araç 3 saattir yoldadır.\nifadelerinden hangileri doğrudur?',
 'I ve III',[('Yalnız I','II’yi doğru eleyip birinci aracın yetişme anında 2 saattir yolda olduğunu sanarak III’ü yanlış bulmuş.','dikkat'),('Yalnız II','Yetişme noktasını yanlış bulup I ve III’ü doğrulamamış.','islem'),('I ve II','II’yi sınamadan doğru saymış ve birinci aracın yetişme anında 2 saat yolda olduğunu sanıp III’ü yanlış bulmuş.','dikkat'),('I, II ve III','II’yi sınamadan doğru saymış; yetişme noktasının 120 km olduğunu görmemiş.','dikkat')],
 'Doğru olan ifadeler.','Önce ikinci aracın yola çıktığı anda birinci aracın ne kadar önde olduğunu bul.',[YETIS,YHZ],
 [A('Başlangıç farkı','İkinci araç yola çıkarken birinci araç 1 saat yol almıştır.','40 × 1 = 40 km'),A('Yetişme süresi','Aynı yönde hızlar çıkarılır.','40 ÷ (60 − 40) = 2 saat'),A('Öncülleri sına','I: 09.00 + 2 saat = 11.00 doğru. II: 60 × 2 = 120 km, 100 değil. III: 08.00’den 11.00’e 3 saat, doğru.','I doğru · II yanlış · III doğru'),A('Sonuç','Doğru olanlar I ve III.','I ve III')],
 'Öncüllü hareket sorularında önce temel büyüklüğü (süre, yol) bul, her ifadeyi bu değerle tek tek sına.',
 sira=['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III'])

# 18 orta: öncüllü karşılaşma
D,va,vb=280,30,40; t=Fr(D,va+vb); assert t==4 and Fr(D,vb)==7 and vb*t==160 and va*t==120 and D-(va+vb)*2==140 and t!=3
Q('0018',ON,'orta','Öncüllü Karşılaşma','Karşılaşma süresi, alınan yollar ve belli bir andaki uzaklığı öncüllerle sınar.','öncüllü','K-HRB-09 (öncüllü hareket) · karşılaşma, doğru II ve III',
 'Aralarında 280 km bulunan iki limandan iki feribot aynı anda birbirine doğru hareket ediyor. Feribotlar sabit 30 km/sa ve 40 km/sa hızla gidiyor.\nBuna göre,\nI. Feribotlar 7 saat sonra karşılaşır.\nII. Hızlı feribot, karşılaşana kadar 160 km yol alır.\nIII. Hareketten 2 saat sonra feribotlar arasındaki uzaklık 140 km’dir.\nifadelerinden hangileri doğrudur?',
 'II ve III',[('Yalnız I','I’i doğru sanmış: yolu yalnızca hızlı feribotun hızına bölüp 7 saat bulmuş; II ve III’ü sınamamış.','bilgi'),('Yalnız II','III’ü sınamamış ya da 2 saatte kapanan yolu 70 km sanmış.','dikkat'),('I ve III','Karşılaşma süresini 7 saat bulup I’i doğru saymış, II’yi sınamamış.','bilgi'),('I, II ve III','I’i sınamadan doğru saymış; karşılaşma 4 saat sonradır.','dikkat')],
 'Doğru olan ifadeler.','Aradaki yol her saat toplam kaç km kısalıyor?',[KARS,YHZ],
 [A('Yaklaşma hızı','Zıt yönde hızlar toplanır.','30 + 40 = 70 km/sa'),A('Karşılaşma süresi','280 ÷ 70.','4 saat'),A('Öncülleri sına','I: 4 saat, 7 değil. II: 40 × 4 = 160 km doğru. III: 280 − 70 × 2 = 140 km doğru.','I yanlış · II doğru · III doğru'),A('Sonuç','Doğru olanlar II ve III.','II ve III')],
 'Karşılaşma sorularında hızlar toplamını bir kez bulup her öncülü bu değerle sına.',
 sira=['Yalnız I','Yalnız II','I ve III','II ve III','I, II ve III'])

# 19 orta: öncüllü ortalama
d,g,dn=180,60,90; tg,td=Fr(d,g),Fr(d,dn); assert (tg,td)==(3,2) and Fr(2*d,tg+td)==72 and tg-td==1 and 2*d==360
Q('0019',ON,'orta','Öncüllü Ortalama Hız','Gidiş–dönüş yolculuğunda ortalama hız, süre farkı ve toplam yol ifadelerini sınar.','öncüllü','K-HRB-09 (öncüllü hareket) · gidiş–dönüş, doğru I ve II',
 'Bir otomobil, A ile B arasındaki 180 km’lik yolu giderken sabit 60 km/sa, aynı yoldan dönerken sabit 90 km/sa hızla gidiyor. Otomobil yolda hiç durmuyor.\nBuna göre,\nI. Otomobilin gidiş–dönüş yolculuğundaki ortalama hızı 72 km/sa’tir.\nII. Dönüş yolculuğu, gidiş yolculuğundan 1 saat kısa sürmüştür.\nIII. Otomobilin gidiş–dönüşte aldığı toplam yol 180 km’dir.\nifadelerinden hangileri doğrudur?',
 'I ve II',[('Yalnız I','Süre farkını sınamamış ya da gidiş–dönüş sürelerini eşit sanmış.','dikkat'),('Yalnız II','Ortalama hızı aritmetik ortalama (75) sanıp I’i yanlış saymış.','bilgi'),('I ve III','I’i doğru bulmuş ama gidiş–dönüşte toplam yolu 180 km sanıp III’ü doğru saymış; II’yi sınamamış.','dikkat'),('I, II ve III','III’ü sınamadan doğru saymış; toplam yol 360 km’dir.','dikkat')],
 'Doğru olan ifadeler.','Önce gidiş ve dönüş sürelerini ayrı ayrı hesapla.',[ORTH,YHZ],
 [A('Süreleri bul','süre = yol ÷ hız.','gidiş 180 ÷ 60 = 3 sa · dönüş 180 ÷ 90 = 2 sa'),A('Ortalama hız','Toplam yol ÷ toplam süre.','360 ÷ 5 = 72 km/sa'),A('Öncülleri sına','I: 72 km/sa doğru. II: 3 − 2 = 1 saat doğru. III: toplam yol 360 km, 180 değil.','I doğru · II doğru · III yanlış'),A('Sonuç','Doğru olanlar I ve II.','I ve II')],
 'Gidiş–dönüşte toplam yol iki katıdır; ortalama hız hızların aritmetik ortalaması değil, toplam yolun toplam süreye bölümüdür.',
 sira=['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III'])

# 20 orta: yarı yarıya ortalama hız
d=180; assert Fr(d,Fr(d,2)/30+Fr(d,2)/90)==45 and Fr(30+90,2)==60 and Fr(30*90,30+90)==Fr(45,2) and 30+90==120 and 30*90==2700
Q('0020',OR,'orta','Ortalama Hız','Yolun iki yarısı farklı hızla gidilen yolculukta ortalama hızı toplam yol ÷ toplam süre ile bulur.','hikâyeli','K-HRB-04 (ortalama hız) · yolun yarıları farklı hızda',
 'Bir kamyon, A ile B arasındaki yolun ilk yarısını sabit 30 km/sa, ikinci yarısını sabit 90 km/sa hızla gidiyor.\nBuna göre kamyonun tüm yol boyunca ortalama hızı saatte kaç kilometredir?',
 45,[(90,'İkinci yarıdaki hızı (90 km/sa) yazmış.','dikkat'),(60,'Hızların aritmetik ortalamasını (30 + 90) ÷ 2 almış.','bilgi'),(120,'İki hızı toplamış.','dikkat'),(2700,'İki hızı çarpmış.','dikkat')],
 'Kamyonun ortalama hızı (km/sa).','Yolun uzunluğu cevabı etkiliyor mu? Her yarının süresini yolun uzunluğu cinsinden yazmayı dene.',[ORTH,YHZ],
 [A('Kolay bir yol seç','Her yarı 90 km olsun; yol 180 km.','yarı = 90 km'),A('Süreleri bul','süre = yol ÷ hız.','90 ÷ 30 = 3 sa · 90 ÷ 90 = 1 sa'),A('Toplam süre','İki süreyi topla.','3 + 1 = 4 sa'),A('Ortalama hız','Toplam yol ÷ toplam süre.','180 ÷ 4 = 45 km/sa')],
 'Yolun yarıları farklı hızla gidilirse ortalama hız 2·v₁·v₂ ÷ (v₁ + v₂) olur; hızların aritmetik ortalaması değildir.')

# 21 orta: mola
d,T,m=360,Fr(15,2),Fr(3,2); M_=T-m; assert M_==6 and Fr(d,M_)==60 and Fr(d,T)==48 and Fr(d,T+m)==40 and Fr(d,T-2*m)==80 and Fr(d,m)==240
Q('0021',OR,'kolay','Mola','Toplam süreden mola süresini ayırarak hareket hızını bulur.','hikâyeli','K-HRB-04 (mola) · hareket hızı',
 'Bir şehirlerarası yolcu otobüsü, 360 km’lik yolu yolda verdiği tek mola dahil toplam 7 saat 30 dakikada alıyor. Mola 1 saat 30 dakika sürüyor ve otobüs hareket hâlindeyken hep aynı hızla gidiyor.\nBuna göre otobüsün hareket hâlindeki hızı saatte kaç kilometredir?',
 60,[(40,'Mola süresini toplam süreye bir kez daha eklemiş: 360 ÷ 9.','dikkat'),(48,'Mola süresini çıkarmamış: 360 ÷ 7,5.','dikkat'),(80,'Mola süresini iki kez çıkarmış: 360 ÷ 4,5.','islem'),(240,'Yolu yalnızca mola süresine bölmüş: 360 ÷ 1,5.','dikkat')],
 'Otobüsün hareket hâlindeki hızı (km/sa).','Otobüs mola sırasında yol almadığına göre hız hangi süreyle hesaplanmalı?',[YHZ,BIRIM],
 [A('Hareket süresi','Mola sırasında yol alınmaz.','7,5 − 1,5 = 6 saat'),A('Hız formülü','hız = yol ÷ hareket süresi.','360 ÷ 6'),A('Sonuç','Bölmeyi yap.','60 km/sa')],
 'Mola süresi toplam süreye dahilse hareket hızı hesaplanırken molayı toplam süreden çıkar.')

# 22 orta: planlanan süre
v1,v2,g1,g2=30,40,Fr(40,60),Fr(10,60); d=(g1-g2)/(Fr(1,v1)-Fr(1,v2)); plan=Fr(d,v1)-g1; assert d==60 and Fr(d,v2)-g2==plan and plan*60==80 and Fr(d,v1)*60==120 and Fr(d,v2)*60==90 and Fr(d,v1)*60+40==160
Q('0022',EG,'orta','Planlanan Süre','İki farklı hızdaki gecikmelerden yolu ve planlanan süreyi bulur.','hikâyeli','K-HRB-02 (hız değişince süre) · iki geç kalma, planlanan süre',
 'Bir esnaf, malları motosikletiyle depodan dükkâna taşıyor. Saatte 30 km sabit hızla giderse dükkâna planlanan saatten 40 dakika geç, saatte 40 km sabit hızla giderse 10 dakika geç varıyor. Her iki durumda da depodan aynı anda çıkıyor.\nBuna göre planlanan yolculuk süresi kaç dakikadır?',
 80,[(60,'Yolun uzunluğunu (60 km) süre olarak yazmış.','dikkat'),(90,'Yalnızca 40 km/sa ile gidiş süresini bulmuş.','dikkat'),(120,'Yalnızca 30 km/sa ile gidiş süresini bulmuş.','dikkat'),(160,'Gecikmeyi planlanan süreden çıkarmak yerine eklemiş: 120 + 40.','bilgi')],
 'Planlanan yolculuk süresi (dakika).','Her iki durumda da planlanan varış saati aynı; gecikme miktarları arasındaki fark neyi ifade eder?',[SBT,BIRIM],
 [A('Süre farkı','Gecikmeler 40 dk ve 10 dk.','40 − 10 = 30 dk = 1/2 saat'),A('Yolu bul','d ÷ 30 − d ÷ 40 = 1/2.','d/120 = 1/2 → d = 60 km'),A('Gerçek süreler','30 km/sa ile 2 saat = 120 dk. 40 km/sa ile 1,5 saat = 90 dk.','120 dk · 90 dk'),A('Planlanan süre','Geç kalmayı çıkar.','120 − 40 = 80 dk (90 − 10 = 80 ✓)')],
 'Geç ya da erken varma farkı, iki hızdaki sürelerin farkına eşittir; yolu bulunca planlanan süre geç kalmayı çıkararak bulunur.')

# 23 orta: navigasyon
kalan=150; v=100; tahmin=Fr(kalan,v); ilk=Fr(1,2); yol1=60*ilk; rest=kalan-yol1; ger=ilk+Fr(rest,v); assert tahmin==Fr(3,2) and ger==Fr(17,10) and (ger-tahmin)*60==12
assert (v*ilk-yol1)==20 and Fr(rest,v)*60==72 and 30+72==102
Q('0023',YN,'orta','Navigasyon','Kurala göre tahmin edilen ve gerçekleşen varış süresi arasındaki farkı bulur.','yeni nesil','K-HRB-08 (navigasyon) · tahmini varış ile gerçek varış farkı',
 'Bir navigasyon uygulaması, tahmini varış süresini “kalan yol ÷ aracın o andaki hızı” işlemiyle hesaplamaktadır.\nSaat 10.00’da varış noktasına 150 km kalmıştır ve araç o anda 100 km/sa hızla gitmektedir. Sürücü, 10.00’dan sonraki ilk 30 dakikayı trafik nedeniyle sabit 60 km/sa hızla, kalan yolu ise sabit 100 km/sa hızla gidiyor.\nBuna göre aracın gerçek varış saati, 10.00’daki tahmini varış saatinden kaç dakika sonradır?',
 12,[(20,'Yavaş sürüşte geri kalınan yolu (20 km) süre olarak yazmış.','dikkat'),(30,'Yavaş gidilen süreyi gecikme sanmış.','dikkat'),(72,'Yalnızca kalan 120 km’lik bölümün süresini bulmuş.','dikkat'),(102,'Yavaş gidilen 30 dakika ile son bölümün süresini (72 dk) toplamış.','dikkat')],
 'Gerçek ve tahmini varış saatleri arasındaki fark (dakika).','Önce uygulamanın 10.00’daki tahmini süresini bul, sonra gerçek toplam süreyi hesapla.',[YHZ,BIRIM],
 [A('Tahmini süre','kalan yol ÷ hız.','150 ÷ 100 = 1,5 saat = 90 dk'),A('Yavaş bölüm','30 dk = 0,5 saat.','60 × 0,5 = 30 km'),A('Kalan bölüm','150 − 30 = 120 km, hız 100 km/sa.','120 ÷ 100 = 1,2 saat = 72 dk'),A('Gerçek süre ve fark','30 dk + 72 dk = 102 dk.','102 − 90 = 12 dk')],
 'Kural verilen sorularda önce kuralı verilen duruma uygula, sonra gerçek durumu ayrı hesaplayıp karşılaştır.')

# 24 orta: çember geç başlayan
C,va,vb,gec=800,4,6,40; on=va*gec; kal=C-on; t=Fr(kal,va+vb); assert on==160 and kal==640 and t==64 and Fr(C,va+vb)==80 and Fr(on,va+vb)==16 and t+gec==104 and Fr(kal,vb-va)==320 and Fr(C,vb-va)==400
Q('0024',CM,'orta','Geç Başlayan Koşucu','Çembersel pistte geç başlayan zıt yönlü koşucunun karşılaşma süresini başlangıç farkını kullanarak bulur.','hikâyeli','K-HRB-05 (çembersel pist) · geç başlayan, zıt yön',
 'Çevresi 800 m olan dairesel bir koşu pistinde Kaan, bir noktadan sabit 4 m/sn hızla koşmaya başlıyor. Kaan’dan 40 saniye sonra Mira, aynı noktadan Kaan’a zıt yönde sabit 6 m/sn hızla koşmaya başlıyor.\nBuna göre Kaan ile Mira, Mira koşuya başladıktan kaç saniye sonra ilk kez karşılaşır?',
 64,[(400,'Zıt yön yerine aynı yönde, başlangıç farkını da yok sayarak 800 ÷ 2 hesaplamış.','bilgi'),(80,'Kaan’ın 40 saniyede koştuğunu unutup çevreyi hızlar toplamına bölmüş.','dikkat'),(104,'Bulduğu 64 saniyeye Kaan’ın başlangıç süresini (40 sn) eklemiş.','dikkat'),(320,'Zıt yön yerine aynı yönmüş gibi hızları çıkarmış: 640 ÷ 2.','bilgi')],
 'Mira’nın koşuya başlamasından ilk karşılaşmaya kadar geçen süre (sn).','Mira başladığında Kaan başlangıç noktasından ne kadar uzaklaşmış, aralarında (zıt yönden) kalan yol ne kadardır?',[CEM,YHZ],
 [A('Kaan’ın ilk yolu','Mira başlarken Kaan 40 sn koşmuştur.','4 × 40 = 160 m'),A('Aradaki yol','Mira zıt yönde olduğundan aralarındaki yol çevreden bu kadar eksiktir.','800 − 160 = 640 m'),A('Yaklaşma hızı','Zıt yönde hızlar toplanır.','4 + 6 = 10 m/sn'),A('Süreyi bul','640 ÷ 10.','64 sn')],
 'Geç başlayan olduğunda erken başlayanın aldığı yolu bul, aralarındaki yolu çevreden (zıt yönde) ya da doğrudan farktan hesapla.')

# 25 zor: dron
g1,g2=1440,1440; ta,tb=60,90; vw=Fr(g1,ta); vk=Fr(g1,tb); v=(vw+vk)/2; u=(vw-vk)/2; assert (vw,vk,v,u)==(24,16,20,4) and Fr(2400,v)==120 and Fr(2400,vw-vk)==300 and Fr(2400,vk)==150 and Fr(100+150,2)==Fr(250,2) and Fr(2400,u)==600
Q('0025',YN,'orta','Kargo Dronu','Yer hızı kuralını iki yönlü uçuşa uygulayarak dronun rüzgârsız hızını ve süreyi bulur.','yeni nesil','K-HRB-08 (kargo dronu) · rüzgâr yönü ve karşı yön',
 'Bir dronun yere göre hızı, rüzgârla aynı yönde uçarken dronun kendi hızı ile rüzgâr hızının toplamına, rüzgâra karşı uçarken bu iki hızın farkına eşittir.\nSabit hızla uçan bir kargo dronu, 1440 m uzaklıktaki iki nokta arasında rüzgârla aynı yönde 60 saniyede, rüzgâra karşı 90 saniyede uçuyor. Rüzgârın hızı da sabittir.\nBuna göre aynı dron, rüzgârsız havada 2400 m’yi kaç saniyede uçar?',
 120,[(300,'İki yer hızının farkını (8 m/sn) dronun hızı sanmış.','bilgi'),(125,'2400 m için iki yer hızıyla süreleri bulup (100 sn ve 150 sn) ortalamasını (125) almış.','islem'),(150,'Yalnızca rüzgâra karşı yer hızını (16 m/sn) kullanmış.','dikkat'),(600,'Rüzgâr hızını (4 m/sn) dronun kendi hızı sanmış.','bilgi')],
 'Rüzgârsız havada 2400 m için geçen süre (sn).','İki yöndeki yer hızlarını bulup dronun kendi hızıyla rüzgâr hızını ayır.',[YHZ,AKI],
 [A('Yer hızları','hız = yol ÷ süre.','rüzgârla 1440 ÷ 60 = 24 · rüzgâra karşı 1440 ÷ 90 = 16 m/sn'),A('Denklemleri yaz','Dron hızı v, rüzgâr hızı w.','v + w = 24 · v − w = 16'),A('Dronun hızı','Taraf tarafa topla.','2v = 40 → v = 20 m/sn'),A('Süreyi bul','Rüzgârsız havada hız 20 m/sn.','2400 ÷ 20 = 120 sn')],
 'Yer hızı iki yönde verilirse iki hızın ortalaması (toplamının yarısı) kaynağın kendi hızıdır.')

# 26 zor: yolun üç bölümü
v1,v2,v3,T=40,60,120,6; d=Fr(T,Fr(1,2)/v1+Fr(1,4)/v2+Fr(1,4)/v3); assert d==320 and d/2/v1==4 and d/4/v2==Fr(4,3) and d/4/v3==Fr(2,3)
assert Fr(1,2)*v1+Fr(1,4)*v2+Fr(1,4)*v3==65 and 65*T==390 and v1*T==240 and v2*T==360 and v3*T==720
Q('0026',TM,'zor','Yolun Bölümleri','Yolun üç bölümü farklı hızlarla gidildiğinde toplam süreden yolu bulur.','hikâyeli','K-HRB-01 (yol–hız–zaman) · yolun 1/2, 1/4, 1/4 bölümleri',
 'Bir otomobil, bir yolun ilk yarısını sabit 40 km/sa, sonraki 1/4’ünü sabit 60 km/sa, son 1/4’ünü sabit 120 km/sa hızla gidiyor ve tüm yolu toplam 6 saatte alıyor.\nBuna göre yolun uzunluğu kaç kilometredir?',
 320,[(240,'Tüm yolu ilk hızla gidilmiş sanmış: 40 × 6.','dikkat'),(360,'Tüm yolu ikinci hızla gidilmiş sanmış: 60 × 6.','dikkat'),(390,'Hızların yol kesirlerine göre ağırlıklı ortalamasını (65 km/sa) süreyle çarpmış.','bilgi'),(720,'Tüm yolu en yüksek hızla gidilmiş sanmış: 120 × 6.','dikkat')],
 'Yolun uzunluğu (km).','Yolun uzunluğuna x diyerek üç bölümün sürelerini x cinsinden yaz.',[YHZ,SBT],
 [A('Bölümleri yaz','Yol x km olsun.','x/2 · x/4 · x/4'),A('Süreleri yaz','süre = yol ÷ hız.','(x/2) ÷ 40 = x/80 · (x/4) ÷ 60 = x/240 · (x/4) ÷ 120 = x/480'),A('Denklemi kur','Toplam süre 6 saat; paydayı 480’de eşitle.','(6x + 2x + x)/480 = 6'),A('Yolu bul','9x/480 = 6.','x = 320 km')],
 'Yolun bölümleri farklı hızla gidiliyorsa her bölümün süresini yolun uzunluğu x cinsinden yazıp toplam süreye eşitle.')

# 27 orta: ikinci yarı hızı
D,vp,vh,Tp=180,60,45,3; assert D==vp*Tp; th=Fr(D,2)/vh; kalan_t=Tp-th; vi=Fr(D,2)/kalan_t; assert (th,kalan_t,vi)==(2,1,90) and 2*vp-vh==75 and vp+vh==105
Q('0027',EG,'orta','İkinci Yarı Hızı','Planlanan süreyi koruyabilmek için kalan yarının hızını süre bütçesinden bulur.','hikâyeli','K-HRB-02 (planlanan süre) · ikinci yarıda gerekli hız',
 'Bir otobüs, 180 km uzunluğundaki yolu sabit 60 km/sa hızla 3 saatte almayı planlıyor. Otobüs yolun ilk yarısını sabit 45 km/sa hızla gidiyor.\nBuna göre otobüs toplam süreyi 3 saatte tutabilmek için yolun kalan yarısını kaç km/sa sabit hızla gitmelidir?',
 90,[(45,'İlk yarıdaki hızı (45 km/sa) tekrar yazmış.','dikkat'),(60,'Planlanan hıza (60 km/sa) dönmenin yeterli olduğunu sanmış.','bilgi'),(75,'Ortalama 60 olsun diye (45 + x) ÷ 2 = 60 yazarak 75 bulmuş.','bilgi'),(105,'İki hızı toplamış: 60 + 45.','dikkat')],
 'Yolun ikinci yarısındaki hız (km/sa).','Toplam süre sabit kaldığına göre ilk yarıya harcanan süre, ikinci yarıya ne kadar süre bırakır?',[YHZ,ORTH],
 [A('Yarı yol','180 km’nin yarısı.','90 km'),A('İlk yarının süresi','süre = yol ÷ hız.','90 ÷ 45 = 2 saat'),A('Kalan süre','Toplam süre 3 saat.','3 − 2 = 1 saat'),A('Gerekli hız','İkinci yarı 90 km, süre 1 saat.','90 ÷ 1 = 90 km/sa')],
 'Ortalama hız hızların aritmetik ortalaması değildir; belirli bir toplam süre isteniyorsa süre bütçesi üzerinden hesap yap.')

# 28 zor: tren geçişi aynı yön
La,Lb,vb_ms,gec=150,250,10,20; vrel=Fr(La+Lb,gec); v=vb_ms+vrel; assert vrel==20 and v==30 and v*Fr(36,10)==108 and 36==vb_ms*Fr(36,10)
assert (Fr(La+Lb,gec)-vb_ms)*Fr(36,10)==36 and (Fr(La,gec)+vb_ms)*Fr(36,10)==63 and vrel*Fr(36,10)==72
Q('0028',TN,'zor','Aynı Yönde Geçiş','Aynı yönde giden iki trenin geçiş süresinden hızı bulur.','hikâyeli','K-HRB-06 (iki tren) · aynı yönde geçiş',
 'Boyu 150 m olan bir yolcu treni, paralel raylarda aynı yönde sabit 36 km/sa hızla giden boyu 250 m olan bir yük trenini geçiyor. Yolcu treninin ön ucu yük treninin arka ucuyla yan yana geldiği andan, yolcu treninin arka ucu yük treninin ön ucuyla yan yana geldiği ana kadar 20 saniye geçiyor.\nBuna göre yolcu treninin hızı saatte kaç kilometredir?',
 108,[(30,'Hızı m/sn olarak bulup km/sa’ya çevirmemiş.','dikkat'),(36,'Hızları toplanıyormuş gibi (v + 10 = 20) kurup 10 m/sn = 36 km/sa bulmuş; bu yük treninin hızına eşit çıkar ve geçiş olamaz.','bilgi'),(63,'Toplam boy yerine yalnızca yolcu treninin boyunu (150 m) almış.','dikkat'),(72,'Hız farkını (20 m/sn) yolcu treninin hızı sanıp km/sa’ya çevirmiş.','bilgi')],
 'Yolcu treninin hızı (km/sa).','Geçiş boyunca yolcu treni yük trenine göre ne kadar yol almıştır?',[TUN,YETIS,BIRIM],
 [A('Göreli yol','Geçiş için iki trenin boyları toplanır.','150 + 250 = 400 m'),A('Göreli hız','400 m, 20 sn’de alınır.','400 ÷ 20 = 20 m/sn (hızlar farkı)'),A('Yük treninin hızı','36 km/sa ÷ 3,6.','10 m/sn'),A('Yolcu treninin hızı','Fark + yük treni hızı.','20 + 10 = 30 m/sn = 108 km/sa')],
 'Aynı yönde geçişte alınan yol boyların toplamı, süreye bölününce hızlar farkını verir.')

# 29 zor: dönüş yapan kamyon
D,va,vb=120,40,60; tb=Fr(D,vb); ya=va*tb; gap=D-ya; t2=Fr(gap,va+vb); assert (tb,ya,gap,t2)==(2,80,40,Fr(2,5)) and vb*t2==24 and va*t2==16 and va*(tb+t2)==96
Q('0029',KR,'zor','Dönüşte Karşılaşma','Varış noktasında dönen hareketlinin yeniden karşılaşma noktasını iki aşamada bulur.','hikâyeli','K-HRB-03 (karşılaşma) · hızlı araç dönüyor',
 'A kentinden B kentine uzanan 120 km’lik yolda iki kamyon aynı anda A’dan, B’ye doğru yola çıkıyor. Birinci kamyon sabit 40 km/sa, ikinci kamyon sabit 60 km/sa hızla gidiyor. İkinci kamyon B’ye varır varmaz bekleme yapmadan aynı yoldan sabit 60 km/sa hızla A’ya doğru dönüyor.\nBuna göre kamyonlar karşılaştıklarında karşılaşma noktası B’ye kaç km uzaklıktadır?',
 24,[(16,'Birinci kamyonun, ikinci kamyon döndükten sonra aldığı yolu bulmuş.','dikkat'),(40,'İkinci kamyon B’ye vardığı anda aralarındaki uzaklığı bulup durmuş.','dikkat'),(80,'İkinci kamyon B’ye vardığı anda birinci kamyonun aldığı yolu yazmış.','dikkat'),(96,'Karşılaşma noktasının A’dan uzaklığını bulmuş.','dikkat')],
 'Karşılaşma noktasının B’ye uzaklığı (km).','İkinci kamyon B’ye vardığında birinci kamyon A’dan ne kadar yol almıştır?',[KARS,YHZ],
 [A('B’ye varış süresi','120 ÷ 60.','2 saat'),A('Birinci kamyonun yeri','2 saatte alınan yol.','40 × 2 = 80 km (B’ye 40 km kalır)'),A('Karşılaşma süresi','Şimdi iki kamyon birbirine doğru gidiyor, aradaki yol 40 km.','40 ÷ (40 + 60) = 2/5 saat'),A('B’ye uzaklık','İkinci kamyon dönüşte 2/5 saat gider.','60 × 2/5 = 24 km')],
 'Dönüş yapan hareketlide dönüş anını yeni başlangıç say; o anki uzaklığı zıt yönlü karşılaşma gibi çöz.')

bitir(P,'hareketiki',UK)
from collections import Counter
print(Counter(q['cevap']['sik'] for q in P.ANA),Counter(q['zorluk'] for q in P.ANA),len(P.ANA))
print(' '.join(q['id'][-4:]+':'+q['cevap']['sik'] for q in P.ANA))
