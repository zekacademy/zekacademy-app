"""Yüzde Problemleri · parti 2 (hafif mod): 29 ana soru, kardeş yok, ipucu 1. Her cevap ve çeldirici kodla doğrulanır."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_mat as H
from _hafif_mat import *
H.KONU='Yüzde Problemleri'
UK='prob|Yüzde Problemleri'
P=Parti('yuzdeprobiki','Yüzde Problemleri',UK)
KY='ÖSYM 2018–2026 TYT Matematik (yüzde problemleri) · yayın soru bankaları (yalnız mantık) · MEB 7–9. sınıf'

YUZ=B('Yüzde','%35 = 35/100 = 0,35. Bir sayının %35’i, sayı × 0,35’tir. Örnek: 200’ün %35’i = 200 × 0,35 = 70')
BUT=B('Yüzdesi bilinen parçadan bütün','Bütünün %p’si a ise bütün = a ÷ (p/100) olur. Örnek: bir sayının %25’i 30 ise sayı = 30 ÷ 0,25 = 120')
KAL=B('Kalan yüzde','Bütün %100’dür; bir kısım %p ise kalan %(100 − p) olur. Örnek: %70’i gidilen yolun kalanı %30’dur')
CARP=B('Yüzde artış ve azalış çarpanı','%p artış çarpanı 1 + p/100, %p azalış çarpanı 1 − p/100’dür. Örnek: %20 artış × 1,2; %20 azalış × 0,8. Peş peşe değişimlerde çarpanlar çarpılır')
DEG=B('Yüzde değişim','yüzde değişim = (yeni − eski) ÷ eski × 100. Örnek: 50’den 60’a çıkış (60 − 50) ÷ 50 = 0,2 → %20 artıştır')
FAZ=B('Yüzde kaç fazla / eksik','“A, B’den yüzde kaç fazla” sorusunda taban B’dir: (A − B) ÷ B. “B, A’dan yüzde kaç eksik” sorusunda taban A’dır. Örnek: 50 ile 40’ta 50, 40’tan %25 fazla; 40, 50’den %20 eksiktir')
PUAN=B('Yüzde puan','iki oran arasındaki farka yüzde puan denir. Örnek: %40’tan %46’ya çıkış 6 yüzde puanlık artıştır; bu, 6 ÷ 40 = %15’lik bir göreli artıştır')
ORAN=B('Oranı yüzdeye çevirme','a / b oranı = a ÷ b × 100 yüzdesidir. Örnek: 3 / 4 = 0,75 → %75')
AGIR=B('Birleşik yüzde','iki grubun ortak yüzdesi yüzdelerin düz ortalaması değildir; her grubun sayısı hesaplanıp toplanır, toplam sayıya bölünür. Örnek: 10 kişinin %50’si, 30 kişinin %10’u: (5 + 3) ÷ 40 = %20')
KDV=B('KDV dahil ve hariç fiyat','KDV hariç fiyat × (1 + KDV oranı) = KDV dahil fiyat. Örnek: KDV oranı %20 ise 100 TL’lik hariç fiyatın dahil hali 100 × 1,2 = 120 TL’dir; KDV tutarı 20 TL’dir')
KUR=B('Koşullu kural','verilen kural cümlesini koşuluyla birlikte uygula; değerler eşiğin altında mı üstünde mi diye bakılır. Örnek: “1000 TL ve üzerine %10 indirim” kuralında 1000 TL’lik sepete 100 TL indirim yapılır')

KARTLAR_=[
 ('K-YZB-01','Yüzde hesaplama ve bütünü bulma','Verilen yüzdelerden kalan yüzde ve kısmın sayısı bulunur; yüzdesi bilinen kısımdan bütüne gidilir.','Yüzdeyi bilinen sayıya uygulamak; kalan kısmı bütün sanmak; kalan yüzdeyi unutmak.','kolay','hikâyeli',2,'yzb-hesap','Yüzde hesaplama ve bütünü bulma'),
 ('K-YZB-02','Ardışık artış–azalış ve yüzde değişimi','Peş peşe yüzde değişimleri çarpanlarla birleştirilir; başlangıç değeri, net değişim ya da bilinmeyen yüzde bulunur.','Yüzdeleri toplayıp çıkarmak; ikinci yüzdeyi ilk değere uygulamak; çarpanı yüzde olarak yazmak.','orta','hikâyeli',3,'yzb-degisim','Ardışık yüzde değişimi ve net değişim'),
 ('K-YZB-03','“Yüzde kaç fazlası / eksiği” ve yüzde puan','Karşılaştırmada tabanın hangi nicelik olduğu belirlenir; yüzde puan farkı ile göreli yüzde değişimi ayrılır.','Tabanı karıştırmak (yön tuzağı); yüzde puan ile yüzde farkını aynı sanmak.','orta','hikâyeli',3,'yzb-fark','Yüzde kaç fazlası/eksiği ve yüzde puan'),
 ('K-YZB-04','Oranı yüzdeye çevirme ve anket','Başarı, isabet, doluluk, defo oranları ve anket sonuçları yüzdeye çevrilir ya da yüzdeden sayıya dönülür.','Yüzdeyi sayı sanmak; toplam yerine kısmı payda almak; yüzdeleri toplamayıp ortalamasını almak.','orta','tablo',3,'yzb-oran','Oranı yüzdeye çevirme ve anket sonuçları'),
 ('K-YZB-05','Birleşik (ağırlıklı) yüzde','Gruplardaki yüzdeler sayılara çevrilip toplanır; birleşik ya da bilinmeyen grubun yüzdesi bulunur.','Yüzdelerin düz ortalamasını almak; grup büyüklüklerini eşit varsaymak.','zor','hikâyeli',4,'yzb-agirlikli','Birleşik (ağırlıklı) yüzde'),
 ('K-YZB-06','KDV ve vergi hesapları','KDV hariç–dahil dönüşümleri çarpan 1 + oran ile yapılır; dahil fiyattan KDV tutarı ve indirimli satış birlikte çözülür.','KDV dahil fiyattan doğrudan %20 almak; hariç fiyat yerine dahil fiyatı taban almak.','orta','hikâyeli',3,'yzb-vergi','KDV dahil–hariç ve vergi hesapları'),
 ('K-YZB-07','Kural tanımlı yüzde (kupon, kademeli tarife)','Eşiklere ve kademelere bağlı yüzde kuralları soruda tanımlandığı gibi uygulanır.','Tüm tüketime tek bir birim fiyatı uygulamak; eşiği geçince oranın tüm tutara değil yalnız aşan kısma mı uygulandığını karıştırmak.','orta','yeni nesil',3,'yzb-yeninesil','Kural tanımlı yüzde: kupon ve kademeli tarife'),
 ('K-YZB-08','Öncüllü yüzde yorumu','Yüzde ifadeleri çarpanlar ve sayısal örneklerle sınanır; kesinlikle doğru olanlar seçilir.','Yüzde puan ile yüzde farkını aynı sanmak; değişimlerin yönünü ve tabanını karıştırmak; bir örnekle yetinmek.','orta','öncüllü',3,'yzb-oncullu','Öncüllü yüzde yorumu'),
]
for k in KARTLAR_: kart(k[0],k[1],k[2],k[3],k[4],k[5],k[6],k[7],k[8],KY)

SAY=[0]
def q(**kw):
    SAY[0]+=1; kw['adim']=len(kw['ad']); kw['ad']=kw['ad']
    mk(P,f'{SAY[0]:04d}',**kw)
def ek(*s):  # şıkların hepsi farklı sayı olmalı
    assert len(set(s))==len(s)

# 01 kolay · pil, bütünü bulma
kal,yz=1400,35; cap=Fr(kal*100,yz); assert cap==4000
q(tipId='yzb-hesap',tip='Yüzde hesaplama ve bütünü bulma',z='kolay',alt='Bütünü bulma',kaz='Bir parçanın yüzdesi ve değeri verildiğinde bütünü hesaplar.',kalip='hikâyeli',
 kart='K-YZB-01 (yüzde hesaplama ve bütün) · pil şarj seviyesi',
 metin='Bir akıllı telefonun bataryasının şarj seviyesi %35’e düştüğünde bataryada 1400 mAh enerji kalmıştır.\nBuna göre bu bataryanın tam dolu kapasitesi kaç mAh’tir?',
 dogru=4000,yan=[(Fr(kal*yz,100),'1400’ün %35’ini almış (490); 1400 bütün değil, bütünün %35’idir.','bilgi'),(cap-kal,'Kapasiteyi bulup kalan enerjiyi çıkarmış; harcanan miktarı vermiş.','dikkat'),(cap+kal,'Kapasite ile kalan enerjiyi toplamış.','dikkat'),(kal*yz,'1400 × 35 işlemini yapıp 100’e bölmeyi unutmuş.','islem')],
 istenen='Bataryanın tam dolu kapasitesi (mAh).',
 ip=['1400 mAh, bütünün hangi kesrine karşılık geliyor?'],
 bilgi=[YUZ,BUT],
 ad=[A('Eşitliği kur','Kalan enerji kapasitenin %35’idir.','Kapasite × 35/100 = 1400'),A('Kapasiteyi bul','Her iki tarafı 100/35 ile çarp.','Kapasite = 1400 × 100 ÷ 35 = 4000 mAh'),A('Kontrol et','Bulunan kapasitenin %35’i verilen değeri vermeli.','4000 × 35/100 = 1400 ✓')],
 puf='Bir parçanın yüzdesi ve değeri biliniyorsa bütünü bulmak için parçayı yüzdeye (kesir olarak) böl.')
assert [Fr(kal*yz,100),cap-kal,cap+kal,kal*yz]==[490,2600,5400,49000]

# 02 kolay · sınav boş sayısı
n=40; d=Fr(70*n,100); y=Fr(20*n,100); b=n-d-y; assert (d,y,b)==(28,8,4)
q(tipId='yzb-hesap',tip='Yüzde hesaplama ve bütünü bulma',z='kolay',alt='Yüzde hesaplama',kaz='Soru sayısının yüzdelerinden kalan kısmın sayısını bulur.',kalip='hikâyeli',
 kart='K-YZB-01 (yüzde hesaplama) · deneme sınavında boş sayısı',
 metin='40 soruluk bir deneme sınavında Deniz, soruların %70’ini doğru, %20’sini yanlış cevaplamış; kalan soruları boş bırakmıştır.\nBuna göre Deniz kaç soruyu boş bırakmıştır?',
 dogru=4,yan=[(y,'Yanlış sayısını (40’ın %20’si) boş sayısı sanmış.','dikkat'),(100-70-20,'Boş kalan yüzdeyi (%10) soru sayısı sanmış.','dikkat'),(d,'Doğru sayısını (40’ın %70’i) vermiş.','dikkat'),(d+y,'Doğru ve yanlış sayısının toplamını vermiş.','dikkat')],
 istenen='Boş bırakılan soru sayısı.',
 ip=['Soruların tamamı yüzde kaçtır; doğru ve yanlış bunun ne kadarını kaplıyor?'],
 bilgi=[YUZ,KAL],
 ad=[A('Boş yüzdesini bul','Bütün %100’dür; doğru ve yanlışı çıkar.','100 − 70 − 20 = 10 → boş %10'),A('Sayıya çevir','Yüzdeyi 40 soruya uygula.','40 × 10/100 = 4 soru'),A('Kontrol et','Üç grubun toplamı soru sayısına eşit olmalı.','28 + 8 + 4 = 40 ✓')],
 puf='Önce kalan yüzdeyi bul, sonra bütüne uygula; yüzdeyi doğrudan sayı sanma.')
assert [y,10,d,d+y]==[8,10,28,36]

# 03 kolay · sinema doluluk
kol,sat=250,175; dol=Fr(sat*100,kol); assert dol==70 and 100-dol==30 and kol-sat==75 and Fr(sat,kol)*10==7
q(tipId='yzb-oran',tip='Oranı yüzdeye çevirme ve anket sonuçları',z='kolay',alt='Doluluk oranı',kaz='Bir kısmın bütüne oranını yüzde olarak ifade eder.',kalip='hikâyeli',
 kart='K-YZB-04 (oranı yüzdeye çevirme) · sinema salonu doluluğu',
 metin='250 koltuklu bir sinema salonunda bir seans için 175 bilet satılmıştır.\nBuna göre bu seansın doluluk oranı yüzde kaçtır?',
 dogru=70,yan=[(7,'175/250 = 0,7 buldu ama yüzdeye çevirirken 100 yerine 10 ile çarpmış.','islem'),(30,'Boş koltukların oranını (%30) vermiş.','dikkat'),(75,'Boş koltuk sayısını (250 − 175) yüzde sanmış.','dikkat'),(175,'Satılan bilet sayısını yüzde sanmış.','dikkat')],
 istenen='Seansın doluluk oranı (yüzde).',
 ip=['Satılan bilet sayısının koltuk sayısına oranını yaz.'],
 bilgi=[ORAN],
 ad=[A('Oranı yaz','Dolu koltuk / tüm koltuk.','175/250 = 0,7'),A('Yüzdeye çevir','Oranı 100 ile çarp.','0,7 × 100 = %70'),A('Kontrol et','Boş koltuk oranı ile toplamı %100 olmalı.','70 + 30 = 100 ✓')],
 puf='Doluluk, başarı, isabet gibi oranlar kısmın bütüne bölümüdür; 100 ile çarpınca yüzde olur.')

# 04 kolay · nüfus artışı
e,yn=200000,250000; assert Fr((yn-e)*100,e)==25 and Fr((yn-e)*100,yn)==20 and (yn-e)//1000==50 and Fr(yn*100,e)==125 and Fr(e*100,yn)==80
q(tipId='yzb-degisim',tip='Ardışık yüzde değişimi ve net değişim',z='kolay',alt='Yüzde değişimi',kaz='Başlangıç ve son değerden yüzde artışı hesaplar.',kalip='hikâyeli',
 kart='K-YZB-02 (yüzde değişimi) · belde nüfusu',
 metin='Bir beldenin nüfusu 2005 yılında 200 000, 2025 yılında ise 250 000 olarak kaydedilmiştir.\nBuna göre bu belde nüfusu 20 yılda yüzde kaç artmıştır?',
 dogru=25,yan=[(20,'Artışı yeni nüfusa bölmüş (50 000 ÷ 250 000).','bilgi'),(50,'Artış miktarını (50 bin) yüzde sanmış.','dikkat'),(80,'Eski nüfusun yeni nüfusa oranını (%80) artış sanmış.','dikkat'),(125,'Yeni nüfusun eskiye oranını (%125) artış yüzdesi sanmış.','bilgi')],
 istenen='Nüfustaki yüzde artış.',
 ip=['Artışı hangi değere bölmen gerektiğine karar ver.'],
 bilgi=[DEG],
 ad=[A('Artışı bul','Yeni nüfustan eskiyi çıkar.','250 000 − 200 000 = 50 000'),A('Eskiye oranla','Artışı başlangıçtaki nüfusa böl.','50 000 ÷ 200 000 = 0,25 → %25'),A('Kontrol et','Eski nüfusun %25 fazlası yeni nüfusu vermeli.','200 000 × 1,25 = 250 000 ✓')],
 puf='Yüzde değişimde taban her zaman başlangıçtaki (eski) değerdir.')

# 05 kolay · KDV hariç→dahil
h5=800; dah=Fr(h5*120,100); assert dah==960 and Fr(h5,Fr(8,10))==1000 and h5*20//100==160 and h5-160==640 and h5+20==820
q(tipId='yzb-vergi',tip='KDV dahil–hariç ve vergi hesapları',z='kolay',alt='KDV hesabı',kaz='KDV hariç fiyattan KDV dahil fiyatı hesaplar.',kalip='hikâyeli',
 kart='K-YZB-06 (KDV) · hariç fiyattan dahil fiyata',
 metin='KDV hariç fiyatı 800 TL olan bir ürüne %20 KDV uygulanmaktadır.\nBuna göre ürünün KDV dahil fiyatı kaç TL’dir?',
 dogru=960,yan=[(160,'Yalnız KDV tutarını (%20’sini) bulmuş.','dikkat'),(640,'KDV tutarını fiyattan çıkarmış.','dikkat'),(820,'%20’yi 20 TL sanıp fiyata eklemiş.','bilgi'),(1000,'800’ü 0,8’e bölmüş (kalan %80 mantığı).','bilgi')],
 istenen='KDV dahil fiyat (TL).',
 ip=['KDV, hariç fiyatın belirli bir yüzdesi kadardır ve fiyata eklenir.'],
 bilgi=[KDV],
 ad=[A('KDV tutarını bul','Hariç fiyatın %20’si.','800 × 20/100 = 160 TL'),A('Fiyata ekle','Dahil fiyat = hariç + KDV.','800 + 160 = 960 TL'),A('Kontrol et','Doğrudan çarpanla da aynı sonuç çıkar.','800 × 1,2 = 960 TL ✓')],
 puf='KDV hariç fiyattan dahil fiyata gitmek için fiyatı 1 + KDV oranı ile çarp.')

# 06 kolay · yüzde kaç fazla (yön tuzağı)
a6,b6=30,75; assert Fr((b6-a6)*100,a6)==150 and Fr((b6-a6)*100,b6)==60 and Fr(b6*100,a6)==250 and Fr(a6*100,b6)==40 and b6-a6==45
q(tipId='yzb-fark',tip='Yüzde kaç fazlası/eksiği ve yüzde puan',z='kolay',alt='Yüzde kaç fazla',kaz='İki nicelik arasındaki farkın yüzdesini doğru tabana göre hesaplar.',kalip='hikâyeli',
 kart='K-YZB-03 (yüzde kaç fazlası) · kafe müşteri sayısı',
 metin='Bir kafenin hafta içi günlük müşteri sayısı ortalama 30, hafta sonu günlük müşteri sayısı ise ortalama 75’tir.\nBuna göre hafta sonu müşteri sayısı, hafta içi müşteri sayısından yüzde kaç fazladır?',
 dogru=150,yan=[(40,'30’un 75’e oranını (%40) fark sanmış.','bilgi'),(45,'Farkı (45 müşteri) yüzde sanmış.','dikkat'),(60,'Tabanı 75 almış; hafta içi 30 olduğundan taban 30 olmalı.','bilgi'),(250,'75’in 30’a oranını (%250) fazlalık sanmış; fazlalık oranın 100’den fazlasıdır.','bilgi')],
 istenen='Hafta sonu müşteri sayısının hafta içine göre yüzde fazlası.',
 ip=['“…’dan yüzde kaç fazla” ifadesinde karşılaştırılan değer, “…’dan” yazılan değerdir.'],
 bilgi=[FAZ],
 ad=[A('Farkı bul','Büyük sayıdan küçüğü çıkar.','75 − 30 = 45'),A('Tabana oranla','“Hafta içinden fazla” → taban 30.','45 ÷ 30 = 1,5 → %150'),A('Kontrol et','30’un %150 fazlası 75’i vermeli.','30 × 2,5 = 75 ✓')],
 puf='“A, B’den yüzde kaç fazla” denince farkı B’ye böl; taban “den/dan” ekinden önceki niceliktir.')

# 07 orta · hisse %20 artış %20 azalış
v=Fr(48); bas=v/(Fr(12,10)*Fr(8,10)); assert bas==50 and v/Fr(8,10)==60 and v/Fr(12,10)==40 and v/Fr(8,10)/Fr(8,10)==75
q(tipId='yzb-degisim',tip='Ardışık yüzde değişimi ve net değişim',z='orta',alt='Artış–azalış',kaz='Art arda uygulanan %20 artış ve %20 azalıştan başlangıç değerini bulur.',kalip='hikâyeli',
 kart='K-YZB-02 (ardışık artış–azalış) · hisse senedi değeri',
 metin='Bir hisse senedinin değeri bir gün %20 artmış, ertesi gün ise bir önceki günün değerinin %20’si kadar azalmıştır.\nİkinci günün sonunda hisse senedinin değeri 48 TL olduğuna göre senedin ilk günün başındaki değeri kaç TL’dir?',
 dogru=50,yan=[(40,'Yalnız artışı (×1,2) geri alarak 48 ÷ 1,2 hesaplamış.','dikkat'),(48,'%20 artış ve %20 azalışın birbirini götürdüğünü sanmış.','bilgi'),(60,'Yalnız azalışı (×0,8) geri alarak 48 ÷ 0,8 hesaplamış.','dikkat'),(75,'Azalışı iki kez geri alıp 48 ÷ 0,8 ÷ 0,8 hesaplamış.','islem')],
 istenen='İlk günün başındaki değer (TL).',
 ip=['İkinci yüzde, birinci günün sonundaki değer üzerinden hesaplanır.'],
 bilgi=[CARP],
 ad=[A('Çarpanları yaz','%20 artış → 1,2; %20 azalış → 0,8.','Değer × 1,2 × 0,8'),A('Toplam çarpan','İki çarpanı çarp.','1,2 × 0,8 = 0,96'),A('Başlangıcı bul','Son değer başlangıcın 0,96 katıdır.','Başlangıç × 0,96 = 48 → 48 ÷ 0,96 = 50 TL')],
 puf='Aynı yüzdeyle önce artıp sonra azalmak değeri eski haline getirmez; çarpanları çarp.')

# 08 orta · üretim net değişim
net=Fr(14,10)*Fr(75,100); assert net==Fr(105,100) and 40-25==15 and 40+25==65 and Fr(40*75,100)==30
q(tipId='yzb-degisim',tip='Ardışık yüzde değişimi ve net değişim',z='orta',alt='Üretim değişimi',kaz='İki yıllık yüzde değişimlerinden net değişimi bulur.',kalip='hikâyeli',
 kart='K-YZB-02 (ardışık değişim, net) · fabrika üretimi',
 metin='Bir fabrikanın yıllık üretimi, ilk yıl bir önceki yıla göre %40 artmış; ikinci yıl ise ilk yılın üretimine göre %25 azalmıştır.\nBuna göre iki yıl sonunda üretim, başlangıçtaki üretime göre yüzde kaç artmıştır?',
 dogru=5,yan=[(15,'Yüzdeleri doğrudan çıkarmış (40 − 25).','bilgi'),(30,'Artışa (%40) azalış çarpanı uygulamış: 40 × 0,75.','bilgi'),(65,'Yüzdeleri toplamış.','bilgi'),(105,'Çarpanı (1,05) bulup artış yüzdesi yerine yüzde değer olarak yazmış.','dikkat')],
 istenen='Başlangıca göre yüzde artış.',
 ip=['Başlangıçtaki üretime 100 de ve iki yılın sonundaki değeri bul.'],
 bilgi=[CARP,DEG],
 ad=[A('Başlangıcı 100 al','Üretim 100 birim olsun.','100'),A('Yıl yıl hesapla','%40 artış, sonra %25 azalış.','100 × 1,4 = 140 → 140 × 0,75 = 105'),A('Değişimi yaz','Son değer başlangıcın 105’idir.','105 − 100 = 5 → %5 artış')],
 puf='Net değişim için başlangıcı 100 al; yüzdeleri toplayıp çıkarma, çarpanları çarp.')

# 09 orta · zincir karşılaştırma
A_,B_,C_=Fr(125,100),Fr(1),Fr(100,120)
a=Fr(5,4)*Fr(6,5); assert a==Fr(3,2) and 25+20==45 and 25-20==5
q(tipId='yzb-fark',tip='Yüzde kaç fazlası/eksiği ve yüzde puan',z='orta',alt='Zincir karşılaştırma',kaz='Ardışık yüzde karşılaştırmalarını çarpanlarla birleştirir.',kalip='hikâyeli',
 kart='K-YZB-03 (yüzde kaç fazlası, zincir) · üç mağazanın satışı',
 metin='Aynı caddedeki üç mağazadan A’nın aylık satış tutarı B’ninkinden %25 fazla, B’nin aylık satış tutarı ise C’ninkinden %20 fazladır.\nBuna göre A’nın aylık satış tutarı, C’ninkinden yüzde kaç fazladır?',
 dogru=50,yan=[(5,'Yüzdeleri çıkarmış (25 − 20).','bilgi'),(25,'Yalnız ilk karşılaştırmayı (A ile B) dikkate almış.','dikkat'),(45,'Yüzdeleri toplamış (25 + 20).','bilgi'),(150,'Oranı (1,5) fazlalık yüzdesi sanmış.','dikkat')],
 istenen='A’nın satışının C’ninkine göre yüzde fazlası.',
 ip=['C’nin satışını bir sayı seç; B’yi ve sonra A’yı bu sayıdan türet.'],
 bilgi=[FAZ,CARP],
 ad=[A('C’yi 100 al','Hesabı kolaylaştırmak için C = 100 TL.','C = 100'),A('B ve A’yı bul','B, C’den %20; A, B’den %25 fazla.','B = 100 × 1,2 = 120 · A = 120 × 1,25 = 150'),A('Farkı yorumla','A, C’yi 50 geçer; taban C.','(150 − 100) ÷ 100 = %50')],
 puf='Zincirleme karşılaştırmada yüzdeleri toplama; ortak niceliğe 100 verip sırayla ilerle.')
assert 100*Fr(6,5)*Fr(5,4)==150

# 10 orta · basketbol isabet
i1,a1,i2,a2=30,40,30,60; top=Fr((i1+i2)*100,a1+a2); assert top==60 and Fr(i1*100,a1)==75 and Fr(i2*100,a2)==50 and Fr(75+50,2)==Fr(125,2) and 75+50==125
q(tipId='yzb-oran',tip='Oranı yüzdeye çevirme ve anket sonuçları',z='orta',alt='İsabet yüzdesi',kaz='İki ayrı denemenin isabet sayılarından toplam isabet yüzdesini bulur.',kalip='hikâyeli',
 kart='K-YZB-04 (oranı yüzdeye çevirme) · serbest atış isabeti',
 metin='Bir basketbolcu serbest atış antrenmanında önce 40 atış yapıp 30’unu, ardından 60 atış yapıp 30’unu isabet ettirmiştir.\nBuna göre basketbolcunun bu antrenmandaki toplam isabet yüzdesi kaçtır?',
 dogru=60,yan=[(50,'Yalnız ikinci serinin isabet yüzdesini (%50) vermiş.','dikkat'),(Fr(125,2),'İki serinin yüzdelerinin düz ortalamasını almış (75 ile 50).','bilgi'),(75,'Yalnız ilk serinin isabet yüzdesini (%75) vermiş.','dikkat'),(125,'İki serinin yüzdelerini toplamış (75 + 50).','bilgi')],
 istenen='Toplam isabet yüzdesi.',
 ip=['Her serideki isabet sayısını ayrı ayrı bulup yüzdeleri doğrudan birleştirmenin uygun olup olmadığını düşün.'],
 bilgi=[ORAN,AGIR],
 ad=[A('Toplam isabet','İki serideki isabetleri topla.','30 + 30 = 60'),A('Toplam atış','İki serideki atışları topla.','40 + 60 = 100'),A('Yüzdeye çevir','Toplam isabet ÷ toplam atış.','60 ÷ 100 = %60')],
 puf='Farklı büyüklükteki serilerde yüzdelerin ortalamasını değil, toplam sayıların oranını al.')

# 11 orta · kulüp ağırlıklı
n9,n10,p9,p10=120,80,35,60; ü=Fr(n9*p9,100)+Fr(n10*p10,100); r=ü*100/(n9+n10); assert (Fr(n9*p9,100),Fr(n10*p10,100),ü,r)==(42,48,90,45) and Fr(p9+p10,2)==Fr(95,2)
q(tipId='yzb-agirlikli',tip='Birleşik (ağırlıklı) yüzde',z='orta',alt='Birleşik yüzde',kaz='İki grubun ayrı yüzdelerinden birleşik yüzdeyi hesaplar.',kalip='hikâyeli',
 kart='K-YZB-05 (birleşik yüzde) · satranç kulübü üyeliği',
 metin='Bir okulun 9. sınıflarında 120, 10. sınıflarında 80 öğrenci vardır. 9. sınıf öğrencilerinin %35’i, 10. sınıf öğrencilerinin %60’ı satranç kulübüne üyedir.\nBuna göre bu iki sınıftaki öğrencilerin yüzde kaçı satranç kulübüne üyedir?',
 dogru=45,yan=[(42,'9. sınıftaki üye sayısını (120’nin %35’i) yüzde sanmış.','dikkat'),(Fr(95,2),'%35 ile %60’ın düz ortalamasını almış; sınıf mevcutları farklıdır.','bilgi'),(90,'Toplam üye sayısını bulup öğrenci sayısına bölmeyi unutmuş.','dikkat'),(95,'İki yüzdeyi toplamış.','bilgi')],
 istenen='Kulübe üye öğrencilerin yüzdesi.',
 ip=['Her sınıftaki üye sayısını ayrı ayrı bul.'],
 bilgi=[YUZ,AGIR],
 ad=[A('Üye sayılarını bul','Her sınıfın üyesini ayrı hesapla.','120 × 35/100 = 42 · 80 × 60/100 = 48'),A('Toplamları al','Üyeleri ve öğrencileri ayrı topla.','42 + 48 = 90 üye · 120 + 80 = 200 öğrenci'),A('Yüzdeye çevir','Üye ÷ öğrenci.','90 ÷ 200 = %45')],
 puf='İki grubun birleşik yüzdesi, grup büyüklüklerine göre ağırlıklandırılır; düz ortalama hatalıdır.')

# 12 orta · sayı zinciri
x=Fr(15,1)/(Fr(40,100)*Fr(50,100)); assert x==75 and Fr(60*25,100)==15 and Fr(15,Fr(4,10))==Fr(75,2) and Fr(15,Fr(5,10))==30 and Fr(15)*Fr(2,10)==3 and 60/Fr(2,10)==300
q(tipId='yzb-hesap',tip='Yüzde hesaplama ve bütünü bulma',z='orta',alt='Yüzdenin yüzdesi',kaz='Art arda alınan yüzdelerle kurulan eşitlikten bilinmeyen sayıyı bulur.',kalip='düz',
 kart='K-YZB-01 (yüzde hesaplama) · sayının yüzdesinin yüzdesi',
 metin='x pozitif bir gerçel sayıdır.\nx sayısının %40’ının %50’si, 60’ın %25’ine eşittir.\nBuna göre x kaçtır?',
 dogru=75,yan=[(3,'Eşitliği çözmek yerine 15 × 0,2 hesaplamış.','islem'),(30,'Yalnız %50’yi kullanıp 15 ÷ 0,5 hesaplamış; %40’ı atlamış.','dikkat'),(Fr(75,2),'Yalnız %40’ı kullanıp 15 ÷ 0,4 hesaplamış; %50’yi atlamış.','dikkat'),(15,'Sağ taraftaki değeri (60’ın %25’i = 15) x sanmış.','dikkat')],
 istenen='x sayısının değeri.',
 ip=['İki yüzdeyi ardışık uygularsan x’in hangi kesri çıkar?'],
 bilgi=[YUZ,BUT],
 ad=[A('Sağ tarafı bul','60’ın %25’i.','60 × 0,25 = 15'),A('Sol tarafı yaz','x’in %40’ının %50’si x × 0,4 × 0,5’tir.','x × 0,2 = 15'),A('x’i bul','Her iki yanı 0,2’ye böl.','x = 15 ÷ 0,2 = 75')],
 puf='“%a’sının %b’si” ifadesi çarpma demektir: a/100 × b/100.')

# 13 orta · KDV dahil, KDV tutarı
dh=1440; kdv=Fr(dh,Fr(12,10))*Fr(2,10); ha=Fr(dh,Fr(12,10)); assert (ha,kdv)==(1200,240) and dh*20//100==288 and dh-288==1152 and Fr(dh*12,10)==1728
q(tipId='yzb-vergi',tip='KDV dahil–hariç ve vergi hesapları',z='orta',alt='KDV tutarı',kaz='KDV dahil fiyattan KDV tutarını hesaplar.',kalip='hikâyeli',
 kart='K-YZB-06 (KDV dahil fiyattan tutar) · etiket fiyatındaki KDV',
 metin='Etiket fiyatı KDV dahil 1440 TL olan bir ürüne %20 KDV uygulanmıştır.\nBuna göre bu fiyatın içindeki KDV tutarı kaç TL’dir?',
 dogru=240,yan=[(288,'KDV’yi dahil fiyat üzerinden hesaplamış (1440’ın %20’si).','bilgi'),(1152,'Dahil fiyattan %20’sini çıkarıp hariç fiyat sanmış (1440 − 288).','bilgi'),(1200,'KDV hariç fiyatı bulup KDV tutarını bulmamış.','dikkat'),(1728,'Dahil fiyata bir kez daha %20 eklemiş.','bilgi')],
 istenen='Etiket fiyatındaki KDV tutarı (TL).',
 ip=['Etiket fiyatı hangi değerin üzerine KDV eklenerek bulunmuştur?'],
 bilgi=[KDV],
 ad=[A('Çarpanı kur','Dahil fiyat = hariç × 1,2.','Hariç × 1,2 = 1440'),A('Hariç fiyatı bul','1440’ı 1,2’ye böl.','1440 ÷ 1,2 = 1200 TL'),A('KDV tutarını bul','Dahil fiyattan hariç fiyatı çıkar.','1440 − 1200 = 240 TL')],
 puf='KDV dahil fiyat, hariç fiyatın (1 + oran) katıdır; KDV tutarı için önce hariç fiyatı bul.')

# 14 orta · baskı hatası, onarım
tp,df=2000,80; yeni=Fr(df//2*100,tp); assert yeni==2 and Fr(df*100,tp)==4 and df//2==40 and 100-4==96 and 100-2==98
q(tipId='yzb-oran',tip='Oranı yüzdeye çevirme ve anket sonuçları',z='orta',alt='Hata oranı',kaz='Hatalı ürün sayısı değişince hata oranını yüzde olarak yeniden hesaplar.',kalip='hikâyeli',
 kart='K-YZB-04 (oranı yüzdeye çevirme) · baskı hatası oranı',
 metin='Bir matbaa bir günde 2000 kitap basmış ve bunların 80’inde baskı hatası bulunmuştur. Hatalı kitapların yarısı düzeltilerek sorunsuz hale getirilmiştir.\nBuna göre bu günün üretiminde hatalı kitapların oranı yüzde kaça düşmüştür?',
 dogru=2,yan=[(4,'Hatalı oranı ilk haliyle (%4) bırakmış; onarımı hesaba katmamış.','dikkat'),(40,'Onarılan sayıyı (40 kitap) yüzde sanmış.','dikkat'),(96,'İlk sağlam oranını (%96) vermiş.','dikkat'),(98,'Sağlam oranını (%98) vermiş; soru hatalı oranını soruyor.','dikkat')],
 istenen='Onarımdan sonra hatalı kitapların oranı (yüzde).',
 ip=['Onarımdan sonra hangi sayı değişiyor, hangisi sabit kalıyor?'],
 bilgi=[ORAN],
 ad=[A('Kalan hatalıları bul','80’in yarısı onarıldı.','80 ÷ 2 = 40 hatalı kitap'),A('Oranı yaz','Hatalı kitap ÷ tüm kitap.','40 ÷ 2000 = 0,02'),A('Yüzdeye çevir','100 ile çarp.','0,02 × 100 = %2')],
 puf='Oran sorularında bütün (payda) sabit kalıyorsa yalnız payı güncelle.')

# 15 orta · yakıt deposu
ek_,p1,p2=24,35,75; kap=Fr(ek_*100,p2-p1); assert kap==60 and Fr(ek_*100,p2)==32 and Fr(ek_*100,100-p2)==96 and p2-p1==40
q(tipId='yzb-hesap',tip='Yüzde hesaplama ve bütünü bulma',z='orta',alt='Depo doluluğu',kaz='Doluluk yüzdesindeki değişimden deponun kapasitesini bulur.',kalip='hikâyeli',
 kart='K-YZB-01 (yüzde hesaplama) · yakıt deposu',
 metin='Bir aracın yakıt deposu %35 doluyken depoya 24 litre benzin ekleniyor ve depo %75 dolu hale geliyor.\nBuna göre bu deponun tamamı kaç litre benzin alır?',
 dogru=60,yan=[(24,'Eklenen yakıtı deponun kapasitesi sanmış.','dikkat'),(32,'24 litreyi yeni doluluğun (%75) karşılığı sanmış.','bilgi'),(40,'Doluluk farkını (40 yüzde puan) litre sanmış.','dikkat'),(96,'24 litreyi kalan boşluğun (%25) karşılığı sanmış.','bilgi')],
 istenen='Deponun kapasitesi (litre).',
 ip=['24 litre, deponun hangi yüzdelik kısmını doldurdu?'],
 bilgi=[BUT,PUAN],
 ad=[A('Doluluk farkını bul','Eklenen yakıt, iki doluluk arasındaki farktır.','75 − 35 = 40 → deponun %40’ı'),A('Eşitliği kur','24 litre kapasitenin %40’ıdır.','Kapasite × 40/100 = 24'),A('Kapasiteyi bul','24’ü 0,4’e böl.','24 ÷ 0,4 = 60 litre')],
 puf='Doluluk yüzdesi değişince eklenen miktar, yüzde puan farkının karşılığıdır; bütünü ona göre hesapla.')

# 16 orta · kupon (yeni nesil)
def kupon(s): return s*Fr(85,100) if s>=2000 else s*Fr(9,10) if s>=1000 else Fr(s)
od1,od2=kupon(1800),kupon(2000); assert (od1,od2)==(1620,1700) and od2-od1==80 and 200*Fr(9,10)==180 and 200*Fr(85,100)==170
q(tipId='yzb-yeninesil',tip='Kural tanımlı yüzde: kupon ve kademeli tarife',z='orta',alt='Kupon kuralı',kaz='Eşiğe bağlı indirim kuralını uygulayarak ödenecek tutardaki değişimi bulur.',kalip='yeni nesil',
 kart='K-YZB-07 (kural tanımlı kupon) · eşiğe bağlı indirim',
 metin='Bir çevrim içi mağazada kupon kuralı şöyledir:\n• Sepet tutarı 1000 TL ve üzerindeyse sepet tutarının %10’u kadar,\n• Sepet tutarı 2000 TL ve üzerindeyse sepet tutarının %15’i kadar indirim uygulanır.\nİndirimler birlikte uygulanmaz; sepet tutarına uygun olan tek indirim yapılır.\nSepet tutarı 1800 TL olan Ayşe, sepetine 200 TL’lik bir ürün daha eklerse ödeyeceği tutar kaç TL artar?',
 dogru=80,yan=[(170,'Eklenen 200 TL’ye yeni oranı (%15) uygulayıp indirimli fark sanmış.','bilgi'),(180,'Eklenen ürüne eski oranı (%10) uygulamış; tutar yeni eşiğe geçince tüm sepete yeni oran uygulanır.','dikkat'),(200,'İndirimin değişmediğini sanıp eklenen ürünün fiyatını vermiş.','dikkat'),(1700,'Yeni ödeme tutarını bulup artışı hesaplamamış.','dikkat')],
 istenen='Ödenecek tutardaki artış (TL).',
 ip=['Sepet tutarı eşik değerine ulaşınca indirimin hangi tutara uygulandığına dikkat et.'],
 bilgi=[KUR,YUZ],
 ad=[A('İlk ödeme','1800 TL için %10 indirim.','1800 × 0,9 = 1620 TL'),A('Yeni sepet','1800 + 200 = 2000 TL; %15 indirim bölgesi.','2000 × 0,85 = 1700 TL'),A('Farkı al','Yeni ödemeden ilkini çıkar.','1700 − 1620 = 80 TL')],
 puf='Kural soruda tanımlandığı gibi uygulanır; eşik aşılınca oran tüm tutara geçiyorsa her iki durumu ayrı ayrı hesapla.')

# 17 orta · su tarifesi (kademeli, yeni nesil)
bf=20; zam=Fr(bf*140,100); fat=10*bf+6*zam; assert (zam,fat)==(28,368) and 16*bf==320 and 16*zam==448 and 6*zam==168 and 10*bf+6*(bf+40)==560
q(tipId='yzb-yeninesil',tip='Kural tanımlı yüzde: kupon ve kademeli tarife',z='orta',alt='Kademeli tarife',kaz='Kademeli tarifede her dilime ilgili birim fiyatı uygulayarak fatura tutarını hesaplar.',kalip='yeni nesil',
 kart='K-YZB-07 (kademeli tarife) · su faturası',
 metin='Bir belediyenin aylık su tarifesi şöyledir:\n• İlk 10 m³ için her m³ 20 TL,\n• 10 m³’ü aşan kısım için her m³’ün fiyatı, ilk 10 m³’ün birim fiyatından %40 daha yüksektir.\nFaturada başka kalem bulunmadığına göre bu tarifede bir ayda 16 m³ su kullanan haneye kaç TL fatura gelir?',
 dogru=368,yan=[(168,'Yalnız 10 m³’ü aşan 6 m³’ün bedelini hesaplamış.','dikkat'),(320,'Tüm tüketime ilk dilimin fiyatını (20 TL) uygulamış.','bilgi'),(448,'Tüm tüketime zamlı birim fiyatı (28 TL) uygulamış.','bilgi'),(560,'%40 zammı 40 TL zam sanıp aşan kısmı 60 TL’den hesaplamış.','islem')],
 istenen='Haneye gelen fatura tutarı (TL).',
 ip=['Tüketimi iki dilime ayır ve her dilimin birim fiyatını ayrı bul.'],
 bilgi=[KUR,CARP],
 ad=[A('Birinci dilim','İlk 10 m³ × 20 TL.','10 × 20 = 200 TL'),A('İkinci dilim','Aşan 16 − 10 = 6 m³; birim fiyat 20 TL’nin %40 fazlası.','20 × 1,4 = 28 TL · 6 × 28 = 168 TL'),A('Toplam fatura','İki dilimi topla.','200 + 168 = 368 TL')],
 puf='Kademeli tarifede her dilim kendi birim fiyatıyla hesaplanır; sonra dilimler toplanır.')

# 18 orta · anket tablosu
yb=100-40-25-15; tot=Fr(80*100,yb); bsk=tot*25/100; assert (yb,tot,bsk)==(20,400,100) and Fr(80*25,100)==20
q(tipId='yzb-oran',tip='Oranı yüzdeye çevirme ve anket sonuçları',z='orta',alt='Anket sonuçları',kaz='Tabloda yüzde ve sayı karışık verilen anket sonuçlarından bir seçeneğin sayısını bulur.',kalip='tablo',
 kart='K-YZB-04 (anket sonuçları) · en çok izlenen spor dalı',
 metin='Bir ankette katılımcılara en çok izledikleri spor dalı sorulmuş; her katılımcı yalnızca bir spor dalı işaretlemiştir. Sonuçlar aşağıdaki tabloda verilmiştir.\nBuna göre ankette basketbolu işaretleyen kişi sayısı kaçtır?',
 dogru=100,yan=[(20,'80 kişiyi anketin tamamı sanıp 80’in %25’ini almış.','dikkat'),(25,'Basketbolun yüzdesini (%25) kişi sayısı sanmış.','dikkat'),(80,'Voleybolun kişi sayısını vermiş.','dikkat'),(40,'Futbolun yüzdesini (%40) basketbolun kişi sayısı sanmış.','dikkat')],
 istenen='Basketbolu işaretleyen kişi sayısı.',
 sekil=tablo_svg(['Spor dalı','Sonuç'],[['Futbol','%40'],['Basketbol','%25'],['Voleybol','80 kişi'],['Yüzme','%15']]),
 ip=['Tabloda yüzdesi verilmeyen dal için dört dalın toplamının ne olması gerektiğini düşün.'],
 bilgi=[KAL,BUT],
 ad=[A('Voleybolun yüzdesi','Dört dalın toplamı %100’dür.','100 − 40 − 25 − 15 = %20'),A('Katılımcı sayısı','80 kişi tüm katılımcıların %20’sidir.','80 ÷ 0,2 = 400 kişi'),A('Basketbol','Katılımcıların %25’i.','400 × 25/100 = 100 kişi')],
 puf='Tablodaki yüzde ve sayıyı eşleştirip toplamı bul; sonra istenen satırın yüzdesini toplama uygula.')

# 19 orta · öncüllü: işsizlik (yüzde puan / yüzde)
i0,i1=10,12; assert i1-i0==2 and Fr((i1-i0)*100,i0)==20
isg0,isg1=Fr(1000),Fr(1200)   # işgücü değişebilir: III kesin değil
assert Fr(isg1*i1,100)/Fr(isg0*i0,100)!=Fr(12,10)
isg0,isg1=Fr(1000),Fr(1000)
assert Fr(isg1*i1,100)/Fr(isg0*i0,100)==Fr(12,10)
q(tipId='yzb-oncullu',tip='Öncüllü yüzde yorumu',z='orta',alt='Yüzde puan yorumu',kaz='Oran değişimini yüzde puan ve göreli yüzde olarak yorumlayıp işgücü değişirse sayının kesin değişmediğini ayırt eder.',kalip='öncüllü',
 kart='K-YZB-08 (öncüllü yüzde yorumu) · işsizlik oranı',
 metin='Bir ilde işsizlik oranı (işsiz sayısının işgücüne oranı) geçen yıl %10, bu yıl %12 olmuştur. İşgücü sayısının iki yılda aynı olup olmadığı bilinmemektedir.\nBuna göre,\nI. İşsizlik oranı 2 yüzde puan artmıştır.\nII. İşsizlik oranı %20 oranında artmıştır.\nIII. İşsiz sayısı %20 artmıştır.\nifadelerinden hangileri kesinlikle doğrudur?',
 dogru='I ve II',sira=['Yalnız I','I ve II','I ve III','II ve III','I, II ve III'],
 yan=[('Yalnız I','Oranın göreli artışını (2 ÷ 10 = %20) hesaplamayıp II’yi yanlış saymış.','dikkat'),('I ve III','İşgücünün sabit kaldığını varsayıp III’ü doğru saymış; II’yi de yüzde puanla karıştırmış.','bilgi'),('II ve III','Yüzde puan farkını (2) fark etmeyip I’i yanlış saymış; III’ü işgücü sabitmiş gibi doğru saymış.','dikkat'),('I, II ve III','İşgücünün sabit olduğunu varsayarak III’ü de doğru saymış.','dikkat')],
 istenen='Kesinlikle doğru olan ifadeler.',
 ip=['İşsiz sayısını hangi iki büyüklüğün çarpımı olarak yazabilirsin?'],
 bilgi=[PUAN,DEG],
 ad=[A('I’i sına','İki oran arasındaki fark yüzde puandır.','12 − 10 = 2 yüzde puan → I doğru'),A('II’yi sına','Göreli artış farkın eski orana bölümüdür.','2 ÷ 10 = 0,2 → %20 → II doğru'),A('III’ü sına','İşgücü değişirse işsiz sayısının artışı da değişir. Örnek: işgücü 1000’den 1200’e çıkarsa işsiz sayısı 100’den 144’e çıkar (%44).','Kesin değil → III yanlış'),A('Sonuç','Kesinlikle doğru olanlar I ve II.','I ve II')],
 puf='Oran verilip ana kütle belirsizse sayısal değişim hakkında kesin hüküm verme; yüzde puan ile yüzde farkını ayır.')
assert Fr(1200*12,100)==144 and Fr(1000*10,100)==100

# 20 orta · öncüllü: abonelik ücreti
c=Fr(3,2)*Fr(6,10); assert c==Fr(9,10) and 200*c==180 and Fr(6,10)*Fr(3,2)==c
q(tipId='yzb-oncullu',tip='Öncüllü yüzde yorumu',z='orta',alt='Fiyat değişimi yorumu',kaz='Art arda artış ve azalışın net etkisini çarpanlarla yorumlar.',kalip='öncüllü',
 kart='K-YZB-08 (öncüllü yüzde yorumu) · abonelik ücreti',
 metin='Bir dijital platformun aylık abonelik ücreti önce %50 artırılmış, ardından yeni ücret %40 azaltılmıştır.\nBuna göre,\nI. Son ücret, ilk ücretten %10 düşüktür.\nII. İşlemlerin sırası değişseydi (önce %40 azaltma, sonra %50 artırma) son ücret farklı olurdu.\nIII. İlk ücret 200 TL ise son ücret 180 TL’dir.\nifadelerinden hangileri kesinlikle doğrudur?',
 dogru='I ve III',sira=['Yalnız I','Yalnız III','I ve II','I ve III','I, II ve III'],
 yan=[('Yalnız I','Son ücreti hesaplayıp III’ü sayısal olarak sınamamış.','dikkat'),('Yalnız III','Net değişimin %10 azalış olduğunu görmeyip I’i yanlış saymış.','bilgi'),('I ve II','Çarpmanın değişme özelliğini bilmeyip sıranın sonucu etkilediğini sanmış; III’ü sınamamış.','bilgi'),('I, II ve III','Sıra değişince sonucun değişeceğini sanıp II’yi de doğru saymış.','bilgi')],
 istenen='Kesinlikle doğru olan ifadeler.',
 ip=['Her ifadeyi çarpanlarla ve ilk ücrete verdiğin bir sayıyla sına.'],
 bilgi=[CARP],
 ad=[A('Çarpanı bul','%50 artış 1,5; %40 azalış 0,6.','1,5 × 0,6 = 0,9 → I doğru'),A('Sırayı değiştir','Çarpma değişmelidir.','0,6 × 1,5 = 0,9 → sonuç aynı, II yanlış'),A('III’ü sına','İlk ücret 200 TL.','200 × 1,5 = 300 → 300 × 0,6 = 180 → III doğru')],
 puf='Art arda yüzde değişimlerinde net etki çarpanların çarpımıdır; çarpma değişmeli olduğundan sıra sonucu etkilemez.')

# 21 orta · öncüllü: a, b'den %25 fazla
for b in (4,8,12,40):
    a=Fr(5,4)*b
    assert Fr((b-a)*100,a)!=-25 and Fr((a-b)*100,b)==25 and Fr((a+b)*100,b)==225 and Fr((a-b)*100,a)==20
q(tipId='yzb-oncullu',tip='Öncüllü yüzde yorumu',z='orta',alt='Fazla–eksik yorumu',kaz='“Yüzde kaç fazla” bilgisinden ters yöndeki yüzde ve toplam yüzdelerini yorumlar.',kalip='öncüllü',
 kart='K-YZB-08 (öncüllü yüzde yorumu) · a, b’den %25 fazla',
 metin='a ve b pozitif gerçel sayılardır ve a sayısı, b sayısından %25 fazladır.\nBuna göre,\nI. b sayısı, a sayısından %25 eksiktir.\nII. a − b farkı, b sayısının %25’idir.\nIII. a + b toplamı, b sayısının %200’üdür.\nifadelerinden hangileri kesinlikle doğrudur?',
 dogru='Yalnız II',sira=['Yalnız I','Yalnız II','I ve II','II ve III','I, II ve III'],
 yan=[('Yalnız I','Eksiklik yüzdesini de %25 sanıp tabanın değiştiğini görmemiş.','bilgi'),('I ve II','I’de taban a olduğu için eksiklik %20’dir; bunu fark etmeyip I’i doğru saymış.','bilgi'),('II ve III','a + b = 1,25b + b = 2,25b olduğunu görmeyip toplamı 2b (%200) hesaplamış.','islem'),('I, II ve III','I’de tabanı karıştırmış, III’te de toplamı 2b saymış.','bilgi')],
 istenen='Kesinlikle doğru olan ifadeler.',
 ip=['b’ye 100 değeri ver ve a ile diğer ifadelerin değerlerini bul.'],
 bilgi=[FAZ],
 ad=[A('Sayıları yaz','b = 100 al; a, b’den %25 fazla.','b = 100 · a = 125'),A('I’i sına','b, a’dan 25 eksik; taban a.','25 ÷ 125 = %20 → I yanlış'),A('II ve III’ü sına','Farkı ve toplamı b’ye oranla.','125 − 100 = 25 → %25 → II doğru · 125 + 100 = 225 → %225 → III yanlış')],
 puf='Yüzde fazla ya da eksik karşılaştırmasında taban değişince yüzde de değişir; ifadeyi bir sayıyla sına.')

# 22 zor · otel doluluk
pm,dm,dt=40,75,60; dolu_m=Fr(pm*dm,100); dolu_dig=dt-dolu_m; oranı=dolu_dig*100/(100-pm); assert (dolu_m,dolu_dig,oranı)==(30,30,50) and dt-pm==20
q(tipId='yzb-agirlikli',tip='Birleşik (ağırlıklı) yüzde',z='zor',alt='Birleşik yüzde',kaz='Genel doluluk ve bir grubun doluluğu verilince diğer grubun doluluk yüzdesini bulur.',kalip='hikâyeli',
 kart='K-YZB-05 (birleşik yüzde, bilinmeyen grup) · otel doluluğu',
 metin='Bir otelin odalarının %40’ı deniz manzaralıdır. Deniz manzaralı odaların %75’i, otelin tüm odalarının ise %60’ı doludur.\nBuna göre deniz manzarasız odaların yüzde kaçı doludur?',
 dogru=50,yan=[(20,'Genel doluluk ile manzaralı oda yüzdesini (60 − 40) çıkarmış.','bilgi'),(30,'Manzarasız dolu odaların sayısını (100 odada 30) yüzde sanmış.','dikkat'),(60,'Genel doluluk yüzdesini (%60) vermiş.','dikkat'),(75,'Manzaralı odaların doluluğunu (%75) manzarasız odalar için de geçerli sanmış.','bilgi')],
 istenen='Manzarasız odaların doluluk yüzdesi.',
 ip=['Otelde 100 oda olduğunu düşün ve dolu oda sayılarını parça parça bul.'],
 bilgi=[AGIR,YUZ],
 ad=[A('Odaları böl','100 oda al: manzaralı 40, manzarasız 60.','40 + 60 = 100'),A('Manzaralı dolu odalar','40’ın %75’i.','40 × 75/100 = 30'),A('Manzarasız dolu odalar','Toplam dolu 100’ün %60’ı = 60 oda.','60 − 30 = 30 oda'),A('Yüzdeye çevir','Manzarasız dolu ÷ manzarasız oda.','30 ÷ 60 = %50')],
 puf='Genel yüzde ve bir grubun yüzdesi biliniyorsa toplam sayıdan grubun payını çıkararak diğer grubu bul.')

# 23 zor · fon üç yıl
f=Fr(15,10)*Fr(6,10); p=(Fr(126,100)/f-1)*100; assert f==Fr(9,10) and p==40 and 126-100==26 and 126-90==36
q(tipId='yzb-degisim',tip='Ardışık yüzde değişimi ve net değişim',z='zor',alt='Bilinmeyen yüzde',kaz='Üç yıllık ardışık değişimde bilinmeyen yüzdeyi çarpanlardan bulur.',kalip='hikâyeli',
 kart='K-YZB-02 (ardışık değişim, bilinmeyen yüzde) · yatırım fonu',
 metin='Bir yatırım fonunun birim değeri ilk yıl %50 artmış, ikinci yıl %40 azalmış, üçüncü yıl ise %p artmıştır.\nÜç yıl sonunda birim değer başlangıçtaki değerin %126’sı olduğuna göre p kaçtır?',
 dogru=40,yan=[(26,'Son değerin 100’ün üstündeki kısmını (126 − 100) doğrudan p sanmış.','dikkat'),(36,'İlk iki yılın çarpanından (%90) farkı (126 − 90) yüzde artış sanmış.','bilgi'),(10,'İlk iki yılın net sonucunu (%10 azalış) p sanmış.','dikkat'),(16,'Yüzdeleri toplayıp 50 − 40 + p = 126 − 100 yazmış (p = 16).','bilgi')],
 istenen='Üçüncü yıldaki artış yüzdesi (p).',
 ip=['Her yılın çarpanını yaz ve üç çarpanın çarpımını son orana eşitle.'],
 bilgi=[CARP],
 ad=[A('İlk iki yıl','%50 artış 1,5; %40 azalış 0,6.','1,5 × 0,6 = 0,9'),A('Üçüncü yıl çarpanı','Üçüncü çarpan x olsun.','0,9 × x = 1,26'),A('x’i bul','1,26’yı 0,9’a böl.','x = 1,4'),A('Yüzdeye çevir','Çarpan 1 + p/100’dür.','1,4 = 1 + p/100 → p = 40')],
 puf='Bilinmeyen bir yüzde, çarpan olarak yazılır; bilinen çarpanları ayırınca kalan çarpan bulunur ve 1’den çıkarılır.')

# 24 zor · aynı yüzdeyle artış ve azalış
ok_=[x for x in range(1,100) if Fr(100+x,100)*Fr(100-x,100)==Fr(91,100)]; assert ok_==[30] and 100-91==9 and 30**2==900 and Fr(9,2)==Fr(9,2)
q(tipId='yzb-degisim',tip='Ardışık yüzde değişimi ve net değişim',z='zor',alt='Bilinmeyen yüzde',kaz='Aynı yüzdeyle art arda artış ve azalıştan bilinmeyen yüzdeyi bulur.',kalip='hikâyeli',
 kart='K-YZB-02 (ardışık artış–azalış, bilinmeyen yüzde) · günlük kullanıcı sayısı',
 metin='Bir uygulamanın günlük kullanıcı sayısı önce %x artmış, ardından bu yeni sayı %x azalmıştır. Bu iki değişimden sonra kullanıcı sayısı, ilk sayının %91’i olmuştur.\n0 < x < 100 olduğuna göre x kaçtır?',
 dogru=30,yan=[(Fr(9,2),'Toplam azalışı (%9) iki değişime eşit paylaştırmış.','bilgi'),(9,'Toplam azalışı (%9) doğrudan x sanmış; artış ve azalışın birbirini götürdüğünü düşünmüş.','bilgi'),(Fr(3,10),'(1 + x)(1 − x) = 0,91 yazıp x = 0,3 bulmuş; yüzdeye çevirmemiş.','islem'),(3,'Çarpımı 1 − x²/100 yazıp (payda 100² yerine 100) x² = 9, x = 3 bulmuş.','islem')],
 istenen='x’in değeri.',
 ip=['Her iki değişimin çarpanını x cinsinden yazıp çarpımını verilen orana eşitle.'],
 bilgi=[CARP,B('Eşlenik çarpım','(1 + t)(1 − t) = 1 − t². Örnek: 1,1 × 0,9 = 1 − 0,01 = 0,99')],
 ad=[A('Çarpanları yaz','%x artış 1 + x/100; %x azalış 1 − x/100.','(1 + x/100)(1 − x/100)'),A('Eşitliği kur','Çarpım 0,91 olmalı.','1 − x²/10 000 = 0,91'),A('x²’yi bul','Eşitliği düzenle.','x²/10 000 = 0,09 → x² = 900'),A('x’i bul','Pozitif kökü al.','x = 30')],
 puf='Aynı yüzdeyle artış ve azalış çarpımı 1 − (x/100)² biçimindedir; net değişim her zaman bir azalıştır.')

# 25 zor · harçlık, yön tuzağı
berk=Fr(450)/(Fr(15,10)-Fr(75,100)); assert berk==600 and Fr(450,Fr(25,100))==1800 and Fr(450,Fr(5,10))==900 and Fr(450,Fr(15,10)*Fr(75,100)-Fr(75,100))==1200
q(tipId='yzb-fark',tip='Yüzde kaç fazlası/eksiği ve yüzde puan',z='orta',alt='Farktan sayıyı bulma',kaz='Bir sayıdan yüzde fazla ve eksik olan iki değerin farkından o sayıyı bulur.',kalip='hikâyeli',
 kart='K-YZB-03 (yüzde fazla/eksik, farktan sayı) · harçlıklar',
 metin='Ali’nin parası Berk’in parasından %25 eksik, Can’ın parası ise Berk’in parasından %50 fazladır.\nCan ile Ali’nin paraları arasındaki fark 450 TL olduğuna göre Berk’in parası kaç TL’dir?',
 dogru=600,yan=[(1200,'Can’ın parasını Ali’den %50 fazla sanmış (1,5 × 0,75b = 1,125b; fark 0,375b = 450).','bilgi'),(450,'Verilen farkı Berk’in parası sanmış.','dikkat'),(900,'Yalnız Can’ın fazlalığını (%50) dikkate alıp 450 ÷ 0,5 hesaplamış.','dikkat'),(1800,'Yalnız Ali’nin eksikliğini (%25) dikkate alıp 450 ÷ 0,25 hesaplamış.','dikkat')],
 istenen='Berk’in parası (TL).',
 ip=['Berk’in parasına b de; Ali ve Can’ın parasını b cinsinden yaz.'],
 bilgi=[FAZ],
 ad=[A('Ali ve Can’ı yaz','Her ikisi de Berk’in parası (b) üzerinden.','Ali = 0,75b · Can = 1,5b'),A('Farkı kur','Can − Ali = 450.','1,5b − 0,75b = 0,75b = 450'),A('b’yi bul','450’yi 0,75’e böl.','b = 600 TL')],
 puf='Aynı tabana (Berk) göre yüzdeleri sayı olarak yaz; farklı kişilerin farkı tabanın yüzdesi olarak çıkar.')

# 26 zor · KDV ve indirimli satış
ha=2500; et=Fr(ha*120,100); od=et*Fr(85,100); hh=od/Fr(12,10); kd=od-hh; assert (et,od,hh,kd)==(3000,2550,2125,425) and ha*15//100==375 and ha*20//100==500 and Fr(od*20,100)==510 and Fr(et*20,100)==600
q(tipId='yzb-vergi',tip='KDV dahil–hariç ve vergi hesapları',z='zor',alt='KDV ve indirim',kaz='İndirimli KDV dahil satış fiyatının içindeki KDV tutarını bulur.',kalip='hikâyeli',
 kart='K-YZB-06 (KDV ve indirimli satış) · kampanyalı etiket',
 metin='KDV hariç fiyatı 2500 TL olan bir ürünün etiket fiyatı, hariç fiyata %20 KDV eklenerek belirlenmiştir. Kampanyada etiket fiyatı üzerinden %15 indirim yapılmış ve müşteri indirimli fiyatı ödemiştir.\nBuna göre müşterinin ödediği tutarın içindeki KDV kaç TL’dir?',
 dogru=425,yan=[(375,'Hariç fiyatın %15’ini (indirim oranı) KDV sanmış.','dikkat'),(500,'İndirimi unutup hariç fiyatın %20’sini KDV sanmış.','dikkat'),(510,'Ödenen tutarın %20’sini almış; KDV dahil tutarın içinde hariç fiyat esas alınmalıdır.','bilgi'),(600,'İndirimden önceki etiket fiyatının %20’sini KDV sanmış.','dikkat')],
 istenen='Ödenen tutarın içindeki KDV (TL).',
 ip=['Ödenen tutarın içinde KDV hariç kısım ne kadardır? Önce ödenen tutarı bul.'],
 bilgi=[KDV,CARP],
 ad=[A('Etiket fiyatı','Hariç fiyata %20 KDV ekle.','2500 × 1,2 = 3000 TL'),A('Ödenen tutar','Etiket üzerinden %15 indirim.','3000 × 0,85 = 2550 TL'),A('Hariç kısım','Ödenen tutar hariç kısmın 1,2 katıdır.','2550 ÷ 1,2 = 2125 TL'),A('KDV tutarı','Ödenen tutardan hariç kısmı çıkar.','2550 − 2125 = 425 TL')],
 puf='İndirim KDV dahil fiyata uygulanınca KDV tutarı yeni toplamın içinden (1,2’ye bölünerek) ayrılır.')

# 27 zor · elektrik tarifesi
bf=3; zm=bf*Fr(15,10); lim=200; fat=825; ast=fat-lim*bf; kw=lim+ast/zm; assert (zm,ast,kw)==(Fr(9,2),225,250) and Fr(fat,bf)==275 and ast==225 and kw-lim==50
q(tipId='yzb-yeninesil',tip='Kural tanımlı yüzde: kupon ve kademeli tarife',z='zor',alt='Kademeli tarife',kaz='Kademeli elektrik tarifesinde fatura tutarından tüketilen kWh miktarını geriye doğru hesaplar.',kalip='yeni nesil',
 kart='K-YZB-07 (kademeli tarife, geriye) · elektrik faturası',
 metin='Bir elektrik tarifesinde aylık tüketimin ilk 200 kWh’ı için her kWh 3 TL’dir. 200 kWh’ı aşan her kWh için fiyat, ilk fiyatın %50 fazlasıdır.\nFaturası yalnızca tüketim bedelinden oluşan ve 825 TL gelen bir hane o ay kaç kWh elektrik tüketmiştir?',
 dogru=250,yan=[(50,'Aşan kısmın kWh miktarını (50) toplam tüketim sanmış.','dikkat'),(225,'Aşan kısmın bedelini (225 TL) kWh sanmış.','dikkat'),(75,'Aşan bedeli 3 TL’ye bölüp (225 ÷ 3) bunu toplam tüketim sanmış.','bilgi'),(200,'Yalnız ilk dilimin kWh miktarını vermiş.','dikkat')],
 istenen='Toplam tüketim (kWh).',
 ip=['Önce ilk dilimin bedelini bul; kalan tutar zamlı dilimin bedelidir.'],
 bilgi=[KUR,CARP],
 ad=[A('İlk dilim bedeli','200 kWh × 3 TL.','200 × 3 = 600 TL'),A('Aşan tutar','Fatura − ilk dilim.','825 − 600 = 225 TL'),A('Zamlı birim fiyat','3 TL’nin %50 fazlası.','3 × 1,5 = 4,5 TL'),A('Aşan kWh ve toplam','Aşan bedel ÷ zamlı fiyat; 200’e ekle.','225 ÷ 4,5 = 50 kWh · 200 + 50 = 250 kWh')],
 puf='Kademeli tarifede geriye doğru çözerken önce dolu dilimlerin bedelini çıkar, kalanı son dilimin fiyatına böl.')

# 28 zor · anket, yüzde puan
n1,n2=500,800; a1=Fr(n1*60,100); a2=a1*Fr(12,10); o2=a2*100/n2; assert (a1,a2,o2)==(300,360,45) and 60-o2==15 and Fr(15*100,60)==25
q(tipId='yzb-fark',tip='Yüzde kaç fazlası/eksiği ve yüzde puan',z='zor',alt='Yüzde puan farkı',kaz='İki ankette değişen katılımcı ve oy sayılarından oy oranındaki yüzde puan farkını bulur.',kalip='hikâyeli',
 kart='K-YZB-03 (yüzde puan) · iki anketin karşılaştırılması',
 metin='Bir belediye, parkta yapılacak etkinlik için iki ayrı anket yapmıştır. Birinci ankete 500 kişi katılmış ve katılımcıların %60’ı A seçeneğini işaretlemiştir. İkinci ankete 800 kişi katılmış; A seçeneğini işaretleyenlerin sayısı birinci ankettekine göre %20 artmıştır.\nBuna göre A seçeneğinin oy oranı, birinci ankete göre kaç yüzde puan azalmıştır?',
 dogru=15,yan=[(20,'A’yı işaretleyenlerin sayısındaki artış yüzdesini (%20) vermiş.','dikkat'),(25,'Azalışı göreli yüzde olarak vermiş (15 ÷ 60); soru yüzde puan soruyor.','bilgi'),(45,'İkinci anketteki oy oranını (%45) vermiş.','dikkat'),(60,'Birinci anketteki oy oranını (%60) vermiş.','dikkat')],
 istenen='Oy oranındaki azalış (yüzde puan).',
 ip=['Her ankette A’yı işaretleyenlerin sayısını ve oranını ayrı bul.'],
 bilgi=[PUAN,YUZ],
 ad=[A('Birinci anket','500’ün %60’ı.','500 × 60/100 = 300 kişi'),A('İkinci anketteki A sayısı','300’ün %20 fazlası.','300 × 1,2 = 360 kişi'),A('İkinci anketteki oran','360 kişi, 800 katılımcının yüzde kaçı?','360 ÷ 800 = %45'),A('Yüzde puan farkı','İki oranı çıkar.','60 − 45 = 15 yüzde puan')],
 puf='Yüzde puan, iki oranın doğrudan farkıdır; oranları bulmak için her anketin kendi katılımcı sayısına böl.')

# 29 zor · yol
tp=Fr(252)/(Fr(7,10)*Fr(6,10)); assert tp==600 and 600*Fr(3,10)==180 and 600*Fr(28,100)==168 and 180+168+252==600 and Fr(252,Fr(7,10))==360 and Fr(252,Fr(6,10))==420 and Fr(252,Fr(3,10))==840 and Fr(252,Fr(4,10))==630
q(tipId='yzb-hesap',tip='Yüzde hesaplama ve bütünü bulma',z='zor',alt='Kalanın yüzdesi',kaz='Art arda kalan miktarın yüzdesi alınarak oluşan yolun toplam uzunluğunu bulur.',kalip='hikâyeli',
 kart='K-YZB-01 (kalan üzerinden yüzde, bütünü bulma) · üç günlük tur',
 metin='Bir bisikletli bir turu üç günde tamamlamıştır. İlk gün turun %30’unu, ikinci gün ise ilk günden sonra kalan yolun %40’ını gitmiş; üçüncü gün kalan 252 km’yi gitmiştir.\nBuna göre turun toplam uzunluğu kaç km’dir?',
 dogru=600,yan=[(360,'İlk günden sonra kalan yolu (%70) üçüncü günün yolu sanmış.','dikkat'),(420,'İlk günü hesaba katmayıp yalnız ikinci günden sonra kalan %60 üzerinden 252 ÷ 0,6 hesaplamış.','dikkat'),(630,'252 ÷ 0,4 hesaplamış: ikinci günün yüzdesini kalan yol sanmış.','dikkat'),(840,'Yüzdeleri doğrudan çıkarıp (100 − 30 − 40 = %30) 252 ÷ 0,3 hesaplamış.','bilgi')],
 istenen='Turun toplam uzunluğu (km).',
 ip=['İkinci günün yüzdesi, ilk günden sonra kalan yola göredir; üçüncü gün turun yüzde kaçı kalıyor?'],
 bilgi=[KAL,BUT],
 ad=[A('İlk günden sonra kalan','Turun %30’u gidildi.','100 − 30 = %70 kaldı'),A('İkinci günden sonra kalan','Kalan %70’in %40’ı gidildi; %60’ı kaldı.','70 × 0,6 = %42 kaldı'),A('Eşitliği kur','252 km turun %42’sidir.','Tur × 0,42 = 252'),A('Turu bul','252’yi 0,42’ye böl.','252 ÷ 0,42 = 600 km')],
 puf='Art arda “kalanın yüzdesi” işlemlerinde kalan yüzde çarpılarak ilerler; son kalan bütünün çarpım kadarıdır.')

assert Fr(225,3)==75 and 100-90==10 and 50-40+16==26 and Fr(30,100)==Fr(3,10)
assert SAY[0]==29
bitir(P,'yuzdeprobiki',UK)
