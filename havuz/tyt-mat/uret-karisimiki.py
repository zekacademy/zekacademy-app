"""Karışım Problemleri · parti 2 (hafif mod): 19 ana soru, kardeş yok, ipucu 1. Her cevap ve çeldirici kodla doğrulanır."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_mat as H
from _hafif_mat import *
H.KONU='Karışım Problemleri'
UK='prob|Karışım Problemleri'
P=Parti('karisimiki','Karışım Problemleri',UK)
def M(no,**k): mk(P,no,adim=len(k['ad']),**k)
def pc(a,b): return Fr(100*a,b)
ORAN=B('Karışımda oran','oran = maddenin miktarı ÷ karışımın toplam miktarı. Örnek: 200 g karışımda 50 g tuz varsa tuz oranı 50 ÷ 200 = %25')
EKLE=B('Madde veya su ekleme','su eklenince yalnız toplam büyür; madde eklenince hem madde hem toplam artar. Örnek: 100 g’da 20 g tuz varsa 100 g su eklenince oran 20 ÷ 200 = %10')
BUHAR=B('Buharlaşma','buharlaşırken yalnız su azalır, çözünen madde olduğu gibi kalır. Örnek: 200 g’da 20 g tuz varsa 100 g su buharlaşınca oran 20 ÷ 100 = %20')
BIRL=B('Karışımları birleştirme','madde miktarları ve toplam miktarlar ayrı ayrı toplanır. Örnek: 100 g %10’luk ile 100 g %30’luk karışırsa (10 + 30) ÷ 200 = %20')
CEK=B('Karışımdan alıp yerine koyma','alınan kısım karışımla aynı oranda madde taşır; geriye kalan madde = ilk madde − alınan kısımdaki madde. Örnek: 100 g %20’lik tuzlu sudan 50 g alınırsa 10 g tuz gider, 10 g tuz kalır')
FIYAT=B('Fiyat karışımı','karışımın birim fiyatı = toplam maliyet ÷ toplam miktar. Örnek: 2 kg 10 TL’lik ile 3 kg 20 TL’lik karışırsa (20 + 60) ÷ 5 = 16 TL/kg')
KURU=B('Değişmeyen miktar','kuruma sırasında yalnız su kaybolur, kuru madde kütlesi sabit kalır. Örnek: %90’ı su olan 100 kg üzümde kuru madde 10 kg’dır')
KAR=B('Oranlı karışım','a : b oranıyla karışan miktarlar a·k ve b·k olarak yazılır; madde miktarı her bileşende miktar × oran ile bulunur. Örnek: %10’luk ile %40’lık 1 : 1 karışırsa (10 + 40) ÷ 2 = %25')
KY='ÖSYM 2018–2026 TYT Matematik (karışım, yüzde) · yayın soru bankaları (yalnız mantık) · MEB 9. sınıf'
kart('K-KRB-01','Madde veya su ekleme','Eklenen su yalnız toplamı, eklenen madde hem maddeyi hem toplamı büyütür; yeni oran = yeni madde ÷ yeni toplam. İstenen oran için eklenecek miktar da aynı kurulumla bulunur.','Eklenen suyu madde saymak; toplamı güncellememek; oran farkını doğrudan miktar sanmak.','orta','hikâyeli',3,'krb-ekleme','Madde veya su ekleme',KY)
kart('K-KRB-02','Buharlaşma ve kuruma','Buharlaşma ve kurumada çözünen madde (kuru madde) sabittir; yeni toplam = madde ÷ yeni oran.','Buharlaşan miktarı yeni toplam sanmak; madde miktarını da azaltmak.','orta','hikâyeli',3,'krb-buharlasma','Buharlaşma ve kuruma',KY)
kart('K-KRB-03','İki ya da daha çok karışımı birleştirme','Madde ve toplam ayrı toplanır; oranla verilen karışımda oran parçaları miktar yerine geçer; istenen oran için bilinmeyen miktar denklemle bulunur.','Yüzdelerin aritmetik ortalamasını almak; oranları ters kullanmak; suyu hesaba katmamak.','orta','hikâyeli',3,'krb-birlestirme','Karışımları birleştirme ve oranlı karışım',KY)
kart('K-KRB-04','Karışımdan alma ve yerine koyma','Alınan kısım aynı oranda madde taşır; geride kalan madde hesaplanır, yerine konan kısmın maddesi eklenir ve toplam korunur. Tek turlu sorularda istenen oran için alınacak miktar da aranır.','Alınan kısmın maddesini düşmemek; yerine konan kısmı saf madde sanmak; toplamı yanlış almak.','zor','hikâyeli',4,'krb-cekme','Karışımdan alma ve yerine koyma',KY)
kart('K-KRB-05','Fiyat karışımı','Karışımın birim fiyatı toplam maliyetin toplam miktara bölümüdür; istenen fiyat için cinslerin miktar oranı fiyat farklarından bulunur.','Fiyatların aritmetik ortalamasını almak; oranı ters yazmak; kârı maliyete eklerken yüzdeyi yanlış tabana uygulamak.','orta','hikâyeli',3,'krb-fiyat','Fiyat karışımı',KY)
kart('K-KRB-06','Yorum ve yeni nesil karışım','Tanımlanan yeni bir ölçü (Brix, tuz puanı gibi) ya da öncüllü ifadeler, karışımın temel ilişkileri (madde sabit, toplam değişir) üzerinden sınanır.','Tanımı gözetmeden alışılmış oran formülünü kullanmak; ifadeleri sınamadan tahmin etmek.','zor','yeni nesil',4,'krb-yorum','Yorum ve yeni nesil karışım',KY)

# ---- 01 kolay · kolonya + su ----
a=Fr(60*300,100); assert a==180 and pc(a,400)==45
M('0001',tipId='krb-ekleme',tip='Madde veya su ekleme',z='kolay',alt='Su Ekleme',kaz='Karışıma saf su eklendiğinde alkol miktarının değişmediğini kullanarak yeni oranı bulur.',kalip='hikâyeli',
 kart='K-KRB-01 (su ekleme) · alkollü kolonyaya saf su',
 metin='Hacimce %60’ı alkol olan 300 mL kolonyaya 100 mL saf su ekleniyor ve karışım iyice karıştırılıyor.\nBuna göre oluşan karışımın alkol oranı yüzde kaçtır?',
 dogru=pc(a,400),yan=[(pc(100,400),'Eklenen suyun hacmini toplam hacme bölmüş (100 ÷ 400).','dikkat'),(60,'Su eklense de oranın aynı kaldığını sanmış.','bilgi'),(pc(a+100,400),'Eklenen suyu da alkol sayıp (180 + 100) ÷ 400 hesaplamış.','bilgi'),(pc(a,300-100),'Toplam hacmi büyütmek yerine 300 − 100 = 200 almış: 180 ÷ 200.','islem')],
 istenen='Karışımın alkol oranı (%).',
 ip=['Başlangıçta 300 mL’nin içinde kaç mL alkol var? Su eklenince bu miktar için ne olur, toplam hacim kaç olur?'],
 bilgi=[ORAN,EKLE],
 ad=[A('Alkol miktarı','300 mL’nin %60’ı alkoldür.','300 × 0,60 = 180 mL'),A('Yeni toplam','Eklenen su toplam hacmi büyütür.','300 + 100 = 400 mL'),A('Yeni oran','Alkol miktarı ÷ yeni toplam.','180 ÷ 400 = %45')],
 puf='Saf su eklenince madde miktarı sabit kalır, yalnız toplam büyür; yeni oranı hep madde ÷ yeni toplam ile bul.')

# ---- 02 kolay · kahve fiyatı ----
c=Fr(30*120+20*170,50); assert c==140
M('0002',tipId='krb-fiyat',tip='Fiyat karışımı',z='kolay',alt='Fiyat Karışımı',kaz='Birim fiyatları farklı iki kahveyi karıştırınca toplam maliyeti toplam kütleye bölerek karışımın kilogram fiyatını bulur.',kalip='hikâyeli',
 kart='K-KRB-05 (fiyat karışımı) · iki cins çekirdek kahve',
 metin='Bir kahve dükkânı, kilogramı 120 TL olan kahveden 30 kg ile kilogramı 170 TL olan kahveden 20 kg’ı karıştırarak yeni bir harman hazırlıyor.\nBu harmanın kilogramı, toplam maliyetin toplam kütleye bölünmesiyle bulunduğuna göre kaç TL’dir?',
 dogru=c,yan=[(Fr(120+170,2),'İki fiyatın aritmetik ortalamasını almış; miktarlar farklı.','bilgi'),(Fr(20*120+30*170,50),'Miktarları fiyatlarla ters eşleştirmiş: (20 × 120 + 30 × 170) ÷ 50.','dikkat'),(Fr(30*120+20*170,20),'Toplam maliyeti 50 yerine 20 kg’a bölmüş.','islem'),(30*120+20*170,'Toplam maliyeti bulup kütleye bölmeyi unutmuş.','dikkat')],
 istenen='Harmanın kilogram fiyatı (TL).',
 ip=['Önce her kahveden alınan miktarın toplam maliyetini ayrı ayrı bul.'],
 bilgi=[FIYAT],
 ad=[A('Maliyetleri bul','Miktar × birim fiyat.','30 × 120 = 3600 TL · 20 × 170 = 3400 TL'),A('Toplamlar','Maliyet ve kütle toplamı.','3600 + 3400 = 7000 TL · 30 + 20 = 50 kg'),A('Birim fiyat','Toplam maliyet ÷ toplam kütle.','7000 ÷ 50 = 140 TL/kg')],
 puf='Fiyat karışımında birim fiyat, fiyatların aritmetik ortalaması değil; toplam maliyetin toplam miktara bölümüdür.')

# ---- 03 kolay · oranlı şerbet ----
for k in (1,2,5):
    assert Fr(2*k*10+k*40,3*k)==20
M('0003',tipId='krb-birlestirme',tip='Karışımları birleştirme ve oranlı karışım',z='kolay',alt='Oranlı Karışım',kaz='Hacim oranı verilen iki meyve suyunun meyve oranlarını ağırlıklandırarak karışımın oranını bulur.',kalip='hikâyeli',
 kart='K-KRB-03 (oranlı karışım) · 2 : 1 hacim oranlı meyve suları',
 metin='Hacimce %10’u meyve olan meyve suyu ile hacimce %40’ı meyve olan meyve suyu, hacimce sırasıyla 2 : 1 oranında karıştırılıyor.\nBuna göre oluşan meyve suyunun meyve oranı (hacimce) yüzde kaçtır?',
 dogru=20,yan=[(Fr(10+40,2),'İki yüzdenin aritmetik ortalamasını almış (10 + 40) ÷ 2.','bilgi'),(Fr(1*10+2*40,3),'Oranları ters eşleştirmiş: (1 × 10 + 2 × 40) ÷ 3.','dikkat'),(10+40,'Yüzdeleri toplayıp karışım oranı sanmış.','dikkat'),(2*10+40,'Meyve miktarını (20 + 40 = 60) bulup toplam parçaya bölmeyi unutmuş.','islem')],
 istenen='Karışımın meyve oranı (%).',
 ip=['Hacimleri 2k ve k diye adlandır; her meyve suyunda ne kadar meyve olur?'],
 bilgi=[KAR],
 ad=[A('Hacimleri yaz','Birincisi 2k, ikincisi k hacmindedir.','toplam hacim = 3k'),A('Meyve miktarları','Her hacmin kendi oranı kadar meyvesi vardır.','0,10 × 2k = 0,2k · 0,40 × k = 0,4k'),A('Oran','Toplam meyve ÷ toplam hacim.','0,6k ÷ 3k = 0,20 → %20')],
 puf='Oranla verilen karışımda hacimleri a·k ve b·k yaz; k sadeleşir. Yüzdelerin ortalaması yalnız eşit miktarlarda doğrudur.')

# ---- 04 kolay · sirke ----
asit=Fr(30*400,100); son=Fr(asit*100,20); assert asit==120 and son==600 and son-400==200
M('0004',tipId='krb-ekleme',tip='Madde veya su ekleme',z='orta',alt='İstenen Oran İçin Su',kaz='Asit miktarı sabit kalacak biçimde istenen oranı sağlayan toplam hacmi bulup eklenecek suyu hesaplar.',kalip='hikâyeli',
 kart='K-KRB-01 (istenen oran için su) · asit çözeltisi seyreltme',
 metin='Hacimce %30’u asit olan 400 mL asit çözeltisine saf su eklenerek hacimce asit oranı %20’ye düşürülüyor.\nBuna göre çözeltiye kaç mL su eklenmiştir?',
 dogru=son-400,yan=[(son,'Yeni toplam hacmi (600 mL) eklenen su sanmış.','dikkat'),(asit,'Asit miktarını (120 mL) eklenen su sanmış.','dikkat'),(Fr(400*(30-20),100),'Yüzde farkının (10) 400 mL’deki karşılığını almış.','bilgi'),(Fr(400*20,100),'Eklenen suyu 400 mL’nin %20’si sanmış.','bilgi')],
 istenen='Eklenen su miktarı (mL).',
 ip=['Çözeltideki asit miktarı kaç mL? Bu miktar yeni karışımın %20’si olunca toplam kaç mL olur?'],
 bilgi=[ORAN,EKLE],
 ad=[A('Asit miktarı','400 mL’nin %30’u asittir.','400 × 0,30 = 120 mL'),A('Yeni toplam','120 mL, yeni toplamın %20’sidir.','120 ÷ 0,20 = 600 mL'),A('Eklenen su','Yeni toplamdan ilk hacmi çıkar.','600 − 400 = 200 mL')],
 puf='Su eklenirken madde sabit kalır; maddeyi yeni orana bölerek yeni toplamı bul, sonra ilk toplamı çıkar.')

# ---- 05 orta · deniz suyu buharlaşma ----
t=Fr(4*900,100); yt=Fr(t*100,6); assert t==36 and yt==600 and 900-yt==300
M('0005',tipId='krb-buharlasma',tip='Buharlaşma ve kuruma',z='orta',alt='Buharlaşma',kaz='Buharlaşmada tuz miktarının sabit kaldığını kullanarak istenen oranı sağlayan buharlaşan su miktarını bulur.',kalip='hikâyeli',
 kart='K-KRB-02 (buharlaşma) · tuzla (saline) havuzu',
 metin='Kütlece %4’ü tuz olan 900 kg deniz suyundan bir miktar su buharlaştırılarak tuz oranı kütlece %6’ya çıkarılıyor.\nBuna göre kaç kg su buharlaşmıştır?',
 dogru=900-yt,yan=[(yt,'Buharlaşmadan sonra kalan karışımın kütlesini (600 kg) buharlaşan su sanmış.','dikkat'),(t,'Tuz miktarını (36 kg) buharlaşan su sanmış.','dikkat'),(Fr(900*(6-4),100),'Yüzde farkının (2) 900 kg’daki karşılığını almış.','bilgi'),(Fr(900,6),'Yeni oran olan 6’yı kütleye bölüp 900 ÷ 6 hesaplamış.','islem')],
 istenen='Buharlaşan su miktarı (kg).',
 ip=['Başlangıçta 900 kg’ın içinde kaç kg tuz var? Buharlaşma bu miktarı etkiler mi, yeni toplam kaç kg olur?'],
 bilgi=[BUHAR],
 ad=[A('Tuz miktarı','900 kg’ın %4’ü tuzdur.','900 × 0,04 = 36 kg'),A('Yeni toplam','Tuz aynı kalır ve yeni karışımın %6’sıdır.','36 ÷ 0,06 = 600 kg'),A('Buharlaşan su','İlk kütleden yeni kütleyi çıkar.','900 − 600 = 300 kg')],
 puf='Buharlaşmada tuz sabit kalır; tuzu yeni orana bölerek yeni kütleyi bul, ilk kütleden çıkar.')

# ---- 06 orta · şeker ekleme ----
s0=Fr(20*400,100); su=400-s0; top=Fr(su*100,50); ek=top-400
assert s0==80 and su==320 and top==640 and ek==240
M('0006',tipId='krb-ekleme',tip='Madde veya su ekleme',z='orta',alt='Madde Ekleme',kaz='Su miktarı sabit kalırken eklenen şekerle istenen oranı sağlayan şeker miktarını bulur.',kalip='hikâyeli',
 kart='K-KRB-01 (madde ekleme) · şerbete şeker eklenerek oran artırılıyor',
 metin='Kütlece %20’si şeker olan 400 gramlık şerbete bir miktar şeker ekleniyor ve şekerin tamamı çözünüyor.\nŞerbetin şeker oranı kütlece %50 olduğuna göre kaç gram şeker eklenmiştir?',
 dogru=ek,yan=[(top,'Yeni toplam kütleyi (640 g) eklenen şeker sanmış.','dikkat'),(400,'İlk kütleyi (400 g) eklenen şeker sanmış.','dikkat'),(Fr(400*(50-20),100),'Yüzde farkının (30) 400 g’daki karşılığını almış; toplamın da büyüdüğünü unutmuş.','bilgi'),(50-20,'Yüzde farkını doğrudan gram sanmış.','dikkat')],
 istenen='Eklenen şeker miktarı (g).',
 ip=['Şerbetteki suyun kütlesini bul. Şeker eklenirken bu miktar değişir mi; yeni karışımda suyun oranı kaç olur?'],
 bilgi=[ORAN,EKLE],
 ad=[A('İlk şeker ve su','400 g’ın %20’si şeker, kalanı sudur.','şeker 80 g · su 320 g'),A('Yeni toplam','Su sabittir ve yeni karışımın %50’sidir.','320 ÷ 0,50 = 640 g'),A('Eklenen şeker','Yeni toplamdan ilk toplamı çıkar.','640 − 400 = 240 g')],
 puf='Madde eklenirken diğer bileşen (su) sabit kalır; sabit bileşeni onun yeni oranına bölerek yeni toplamı bul.')

# ---- 07 orta · dezenfektan birleştirme ----
x=Fr(900*50-900*30,75-30); assert x==400 and Fr(75*400+30*500,900)==50
M('0007',tipId='krb-birlestirme',tip='Karışımları birleştirme ve oranlı karışım',z='orta',alt='İstenen Oran İçin Karışım',kaz='İki farklı derişimdeki çözeltinin toplamı ve son oranı verildiğinde bileşenlerden birinin miktarını denklemle bulur.',kalip='hikâyeli',
 kart='K-KRB-03 (birleştirme, bilinmeyen miktar) · iki alkol çözeltisi',
 metin='Hacimce %30 alkollü ile hacimce %75 alkollü iki alkol çözeltisi karıştırılarak hacimce %50 alkollü 900 mL çözelti hazırlanıyor.\nBuna göre %30 alkollü çözeltiden kaç mL kullanılmıştır?',
 dogru=900-x,yan=[(x,'%75 alkollü çözeltinin miktarını (400 mL) bulup sorulan %30 alkollü yerine yazmış.','dikkat'),(450,'Eşit miktarda karıştırıldığını sanmış.','bilgi'),(Fr(900*(50-30),100),'Yüzde farkını (20) 900 mL’deki karşılığına çevirip bilinmeyen miktar sanmış.','islem'),(Fr(900*(75-50),100),'Yüzde farkını (25) 900 mL’deki karşılığına çevirip bilinmeyen miktar sanmış.','islem')],
 istenen='%30 alkollü çözeltinin miktarı (mL).',
 ip=['%75 alkollü çözelti x mL ise %30’luk kaç mL olur? Her ikisindeki alkol miktarını yaz.'],
 bilgi=[BIRL],
 ad=[A('Miktarları yaz','%75 alkollü x mL ise %30’luk (900 − x) mL’dir.','x + (900 − x) = 900'),A('Alkol denklemi','Alkol miktarları toplamı son karışımdaki alkole eşittir.','0,75x + 0,30 (900 − x) = 0,50 × 900 = 450'),A('Çöz','Denklemi sadeleştir.','0,45x + 270 = 450 → 0,45x = 180'),A('x’i bul','Bölme yap.','x = 400 mL (%75 alkollü)'),A('İstenen miktar','Toplamdan çıkar.','900 − 400 = 500 mL (%30 alkollü)')],
 puf='Birleştirmede madde toplamı korunur: iki bileşenin madde miktarları toplamı son karışımdaki madde miktarına eşittir.')

# ---- 08 orta · çay fiyatı + kâr ----
mal=Fr(2*150+3*100,5); sat=mal*Fr(120,100); assert mal==120 and sat==144
M('0008',tipId='krb-fiyat',tip='Fiyat karışımı',z='orta',alt='Fiyat ve Kâr',kaz='İki cins çayı verilen oranda karıştırıp maliyeti bulur ve yüzde kârla satış fiyatını hesaplar.',kalip='hikâyeli',
 kart='K-KRB-05 (fiyat karışımı, kâr) · iki cins çay 2 : 3',
 metin='Kilogramı 150 TL olan çay ile kilogramı 100 TL olan çay, kütlece sırasıyla 2 : 3 oranında karıştırılıyor. Elde edilen karışım, maliyetinin %20 fazlasına satılıyor.\nBuna göre karışımın kilogramı kaç TL’ye satılmıştır?',
 dogru=sat,yan=[(mal,'Kâr eklemeyi unutup maliyeti yazmış.','dikkat'),(mal+20,'%20’yi 20 TL olarak maliyete eklemiş.','bilgi'),(Fr(150+100,2),'Kârı unutup fiyatların aritmetik ortalamasını (125 TL) yazmış.','bilgi'),(mal*Fr(80,100),'Kâr yerine %20 indirim uygulamış.','dikkat')],
 istenen='Karışımın kilogram satış fiyatı (TL).',
 ip=['Çayları 2k ve 3k kg diye adlandır; toplam maliyeti ve toplam kütleyi bul.'],
 bilgi=[FIYAT,KAR],
 ad=[A('Maliyetler','2k kg 150 TL’den, 3k kg 100 TL’den.','2k × 150 = 300k · 3k × 100 = 300k'),A('Kilogram maliyeti','Toplam maliyet ÷ toplam kütle.','600k ÷ 5k = 120 TL'),A('Satış fiyatı','Maliyetin %20 fazlası.','120 × 1,20 = 144 TL')],
 puf='Önce karışımın kilogram maliyetini toplam maliyet ÷ toplam kütle ile bul; kârı bu maliyet üzerinden yüzde olarak uygula.')

# ---- 09 orta · boya üç bileşen ----
r=Fr(2*60+3*30+5*0,10); assert r==21
M('0009',tipId='krb-birlestirme',tip='Karışımları birleştirme ve oranlı karışım',z='orta',alt='Üç Bileşenli Karışım',kaz='Hacim oranı verilen üç bileşenin (biri saf su) pigment miktarlarını toplayıp karışımın pigment oranını bulur.',kalip='hikâyeli',
 kart='K-KRB-03 (oranlı karışım, üç bileşen) · iki boya ve su',
 metin='Hacimce %60’ı pigment olan X boyası, hacimce %30’u pigment olan Y boyası ve saf su, hacimce sırasıyla 2 : 3 : 5 oranında karıştırılarak yeni bir boya elde ediliyor.\nBuna göre yeni boyanın pigment oranı yüzde kaçtır?',
 dogru=r,yan=[(Fr(60+30+0,3),'Üç bileşenin yüzdelerinin aritmetik ortalamasını almış.','bilgi'),(Fr(5*60+3*30+2*0,10),'Oranları ters sıralamış (5 : 3 : 2).','dikkat'),(Fr(2*60+3*30,5),'Suyu hesaba katmayıp yalnız iki boyanın toplam hacmine (5 parça) bölmüş.','dikkat'),(Fr(60+30,2),'Yalnız iki boyanın yüzdelerinin ortalamasını almış.','bilgi')],
 istenen='Yeni boyanın pigment oranı (%).',
 ip=['Hacimleri 2k, 3k ve 5k alıp her bileşendeki pigment miktarını yaz; suyun pigment miktarı kaçtır?'],
 bilgi=[KAR],
 ad=[A('Hacimler','Toplam hacim 2k + 3k + 5k.','10k'),A('Pigment miktarları','Her bileşenin pigmenti kendi oranı kadardır.','0,60 × 2k = 1,2k · 0,30 × 3k = 0,9k · su: 0'),A('Oran','Toplam pigment ÷ toplam hacim.','2,1k ÷ 10k = 0,21 → %21')],
 puf='Saf su da hacmi büyüten ama madde katmayan bir bileşendir; toplam hacme mutlaka dahil edilir.')

# ---- 10 orta · tek tur zeytinyağı ----
y0=Fr(40*50,100); kal=y0-Fr(40*10,100); yeni=kal+10; assert y0==20 and kal==16 and yeni==26 and pc(yeni,50)==52
M('0010',tipId='krb-cekme',tip='Karışımdan alma ve yerine koyma',z='orta',alt='Alıp Saf Madde Koyma',kaz='Karışımdan alınan kısmın maddesini düşüp yerine konan saf maddeyi ekleyerek yeni oranı bulur.',kalip='hikâyeli',
 kart='K-KRB-04 (alıp yerine saf madde koyma) · zeytinyağı–ayçiçek yağı',
 metin='Bir depoda hacimce %40’ı zeytinyağı, kalanı ayçiçek yağı olan 50 L yağ karışımı vardır. Depodan 10 L karışım alınıyor ve yerine 10 L saf zeytinyağı konarak karıştırılıyor.\nBuna göre depodaki karışımın zeytinyağı oranı yüzde kaçtır?',
 dogru=pc(yeni,50),yan=[(40+10,'Oranı 10 puan artırıp %50 yazmış.','bilgi'),(pc(kal,50),'Yerine konan saf zeytinyağını eklememiş: 16 ÷ 50.','dikkat'),(pc(y0+Fr(40*10,100),50),'Alınan karışımdaki zeytinyağını düşmek yerine eklemiş: (20 + 4) ÷ 50.','dikkat'),(40,'Alma ve koymadan sonra oranın değişmediğini sanmış.','bilgi')],
 istenen='Son zeytinyağı oranı (%).',
 ip=['Alınan 10 L’de kaç L zeytinyağı var? Depoda başlangıçtaki zeytinyağından bu kadar çıkınca ne kalır?'],
 bilgi=[CEK],
 ad=[A('İlk zeytinyağı','50 L’nin %40’ı.','50 × 0,40 = 20 L'),A('Alınan kısım','10 L karışımın %40’ı zeytinyağıdır.','10 × 0,40 = 4 L → kalan 20 − 4 = 16 L'),A('Yeni zeytinyağı','Eklenen 10 L saf zeytinyağı.','16 + 10 = 26 L (toplam yine 50 L)'),A('Yeni oran','Zeytinyağı ÷ toplam.','26 ÷ 50 = %52')],
 puf='Alınan kısım, karışımla aynı oranda madde götürür; yerine konan saf kısım ise tamamen maddedir. Toplam hacim değişmez.')

# ---- 11 orta · öncüllü şerbet ----
base=Fr(25*400,100)
assert base==100 and pc(base,400+100)==20 and pc(base,400-200)==50 and pc(base+100,400+100)==40 and pc(base+100,400)==50
assert pc(base,400)==25 and pc(base,400+200)!=50 and Fr(100,600)!=Fr(1,2)
M('0011',tipId='krb-yorum',tip='Yorum ve yeni nesil karışım',z='orta',alt='Öncüllü Karışım',kaz='Şerbete su ekleme, buharlaşma ve şeker ekleme işlemlerinin sonucunu ayrı ayrı sınayarak doğru öncülleri belirler.',kalip='öncüllü',
 kart='K-KRB-06 (öncüllü karışım) · şerbet: su ekleme, buharlaşma, şeker ekleme',
 metin='Kütlece %25’i şeker olan 400 gram şerbet vardır. Buna göre,\nI. Şerbete 100 gram su eklenirse şeker oranı %20 olur.\nII. Şerbetten 200 gram su buharlaştırılırsa şeker oranı %50 olur.\nIII. Şerbete 100 gram şeker eklenip tamamen çözülürse şeker oranı %50 olur.\nifadelerinden hangileri doğrudur?',
 dogru='I ve II',sira=['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III'],
 yan=[('Yalnız I','II’de buharlaşan 200 g’ı toplamdan çıkarmak yerine ekleyip 100 ÷ 600 bulmuş ve II’yi yanlış saymış.','dikkat'),('Yalnız II','I’de su eklenince toplamı büyütmeyip 100 ÷ 400 = %25 bulmuş.','dikkat'),('I ve III','II’de buharlaşan suyu toplama ekleyip yanlış saymış; III’te toplamı büyütmeyip 200 ÷ 400 = %50 bulmuş.','dikkat'),('I, II ve III','III’te şeker eklenince toplamı da büyütmeyip 200 ÷ 400 = %50 bulmuş.','dikkat')],
 istenen='Doğru olan ifadeler.',
 ip=['Şerbetteki şekerin gram cinsinden miktarını bul; üç ifadeyi ayrı ayrı yeni şeker ve yeni toplam ile sına.'],
 bilgi=[ORAN,EKLE,BUHAR],
 ad=[A('Şeker miktarı','400 g’ın %25’i.','100 g şeker'),A('I ve II','I: şeker 100, toplam 500. II: şeker 100, toplam 200.','100 ÷ 500 = %20 ✓ · 100 ÷ 200 = %50 ✓'),A('III','Şeker 200, toplam 500.','200 ÷ 500 = %40 ≠ %50 ✗'),A('Sonuç','I ve II doğru, III yanlıştır.','I ve II')],
 puf='Her işlemde yeni şeker ve yeni toplamı ayrı yaz: su eklemek toplamı büyütür, buharlaşma toplamı azaltır, şeker eklemek ikisini de büyütür.')

# ---- 12 orta · Brix yeni nesil ----
bx=60; ks=Fr(bx*100,100); tp=Fr(ks*100,12); sw=tp-100
assert ks==60 and tp==500 and sw==400
M('0012',tipId='krb-yorum',tip='Yorum ve yeni nesil karışım',z='orta',alt='Brix Değeri',kaz='Tanımı verilen Brix değerini 100 g çözeltideki şeker miktarı olarak kullanıp istenen Brix için eklenecek su miktarını bulur.',kalip='yeni nesil',
 kart='K-KRB-06 (yeni nesil) · Brix tanımı, konsantre seyreltme',
 metin='Bir meyve suyunun Brix değeri, 100 gram meyve suyunda bulunan çözünmüş şekerin gram cinsinden miktarıdır. Örneğin Brix değeri 10 olan 100 gram meyve suyunda 10 gram şeker vardır.\nBrix değeri 60 olan 100 gram konsantreye saf su eklenerek Brix değeri 12 olan meyve suyu elde ediliyor.\nBuna göre konsantreye kaç gram su eklenmiştir?',
 dogru=sw,yan=[(Fr(100*(60-12),100),'Brix farkının (48) 100 g’daki karşılığını eklenen su sanmış.','bilgi'),(ks,'Konsantredeki şeker miktarını (60 g) eklenen su sanmış.','dikkat'),(60+12,'İki Brix değerini toplayıp eklenen su sanmış.','dikkat'),(tp,'Yeni toplam kütleyi (500 g) eklenen su sanmış.','dikkat')],
 istenen='Eklenen su miktarı (g).',
 ip=['Tanıma göre 100 g konsantrede kaç g şeker var? Yeni meyve suyunun kaç gramında bu şeker 12 gram olur?'],
 bilgi=[B('Brix tanımı','Brix = 100 g çözeltideki şeker gramı. Örnek: Brix 20 olan 50 g çözeltide 10 g şeker vardır'),EKLE],
 ad=[A('Şeker miktarı','Brix 60: 100 g’da 60 g şeker.','100 g konsantrede 60 g şeker'),A('Yeni toplam','Şeker aynı kalır; 100 g’ında 12 g şeker olacak.','60 ÷ 12 × 100 = 500 g'),A('Eklenen su','Yeni toplamdan konsantre kütlesini çıkar.','500 − 100 = 400 g')],
 puf='Yeni nesil sorularda önce verilen tanımı oku; Brix gibi bir ölçü, oranın başka bir adıdır ve madde sabitliği aynen geçerlidir.')

# ---- 13 orta · süt-krema ayırma ----
yg=Fr(6*600,100); kr=30; kalan=600-100; ky=yg-kr
assert yg==36 and ky==6 and pc(ky,kalan)==Fr(6,5)
AYR=B('Ayrılan kısım','ayrılan kısımdaki madde, o kısmın kendi oranıyla bulunur; kalan madde = ilk madde − ayrılan kısımdaki madde. Örnek: 100 L’de 20 L madde varken 30 L’lik kısımda 3 L madde ayrılırsa kalan 70 L’de 17 L madde vardır')
M('0013',tipId='krb-cekme',tip='Karışımdan alma ve yerine koyma',z='orta',alt='Karışımdan Kısım Ayırma',kaz='Karışımdan ayrılan kısmın içerdiği maddeyi düşerek kalan karışımın oranını bulur.',kalip='hikâyeli',
 kart='K-KRB-04 (karışımdan kısım ayırma) · süt ve krema',
 metin='Hacimce %6’sı yağ olan 600 L süt, bir ayırıcıdan geçirilerek hacimce %30’u yağ olan 100 L krema ve geriye kalan süt olarak ikiye ayrılıyor.\nBuna göre kalan sütün yağ oranı hacimce yüzde kaçtır?',
 dogru=pc(ky,kalan),yan=[(Fr(yg*100,kalan),'Ayrılan kremadaki yağı düşmeden 36 ÷ 500 hesaplamış.','dikkat'),(6,'Bir kısım ayrıldığı için oranın değişmediğini sanmış.','bilgi'),(yg,'İlk yağ miktarını (36 L) oran sanmış.','dikkat'),(30,'Ayrılan kremanın yağ oranını kalan sütünkü sanmış.','dikkat')],
 istenen='Kalan sütün yağ oranı (%).',
 ip=['600 L sütte kaç L yağ var? Ayrılan kremayla bunun ne kadarı gitti, kalan sütün hacmi kaç L?'],
 bilgi=[AYR],
 ad=[A('İlk yağ','600 L’nin %6’sı.','36 L'),A('Ayrılan yağ','100 L kremanın %30’u.','30 L → kalan yağ 36 − 30 = 6 L'),A('Kalan süt','Hacim azalır.','600 − 100 = 500 L'),A('Yeni oran','Kalan yağ ÷ kalan süt.','6 ÷ 500 = %1,2')],
 puf='Ayrılan kısmın yağı kendi oranına göre hesaplanır; kalan yağı kalan hacme böl. Ayrılan kısmın oranı ile kalanın oranı aynı değildir.')

# ---- 14 zor · alıp su koyma, istenen oran ----
al=Fr(60*80,100); hed=Fr(45*80,100); xx=Fr(al-hed,Fr(60,100)); assert al==48 and hed==36 and xx==20
M('0014',tipId='krb-cekme',tip='Karışımdan alma ve yerine koyma',z='orta',alt='İstenen Oran İçin Alınacak Miktar',kaz='Alınıp yerine saf su konan karışımda istenen son orana göre alınması gereken miktarı bilinmeyenli denklemle bulur.',kalip='hikâyeli',
 kart='K-KRB-04 (alıp su koyma, bilinmeyen miktar) · antiseptik çözelti',
 metin='80 litrelik bir kapta hacimce %60’ı alkol olan antiseptik çözelti vardır. Kaptan bir miktar çözelti alınıp yerine aynı hacimde saf su konuyor ve karıştırılıyor. Son durumda çözeltinin alkol oranı %45 olmuştur.\nBuna göre kaptan kaç litre çözelti alınmıştır?',
 dogru=xx,yan=[(Fr(60*80,100)-Fr(45*80,100),'Alınan miktarın tamamını alkol sayıp 48 − 36 = 12 bulmuş.','bilgi'),(60-45,'Yüzde farkını (15) doğrudan litre sanmış.','dikkat'),(hed,'Son alkol miktarını (36 L) alınan çözelti sanmış.','dikkat'),(80-20,'Kapta kalan çözelti miktarını (60 L) bulup alınan yerine yazmış.','dikkat')],
 istenen='Alınan çözelti miktarı (L).',
 ip=['Alınan çözelti x L ise bunun içinde kaç L alkol vardır? Son durumda kapta kaç L alkol olmalı?'],
 bilgi=[CEK],
 ad=[A('İlk ve son alkol','İlk: 80 L’nin %60’ı. Son: 80 L’nin %45’i (toplam değişmez).','48 L → 36 L'),A('Alınan x L’nin alkolü','Alınan kısım %60 alkollüdür.','0,60x L alkol çıkar'),A('Denklem','İlk alkol − çıkan alkol = son alkol (su alkolsüzdür).','48 − 0,60x = 36'),A('x’i bul','Denklemi çöz.','0,60x = 12 → x = 20 L')],
 puf='Alınan kısım karışımla aynı oranda madde götürür; yerine konan su madde getirmez. Toplam sabitse son madde miktarı ilk madde − 0,oran × alınan olur.')

# ---- 15 zor · iki aşamalı ----
a0=Fr(50*60,100); a1=a0-Fr(50*20,100)+Fr(80*20,100); a2=pc(a1,100)
assert a0==30 and a1==36 and a2==36
M('0015',tipId='krb-cekme',tip='Karışımdan alma ve yerine koyma',z='zor',alt='Alıp Başka Karışım Koyma',kaz='Karışımdan alınan kısmın yerine daha yüksek oranlı karışım konup ardından su eklenmesiyle oluşan son oranı bulur.',kalip='hikâyeli',
 kart='K-KRB-04 (alıp başka karışım koyma, ardından su) · alkol çözeltisi',
 metin='Hacimce %50’si alkol olan 60 L çözeltiden 20 L alınıyor ve yerine hacimce %80’i alkol olan 20 L çözelti konuyor. Karıştırıldıktan sonra karışıma 40 L saf su ekleniyor.\nBuna göre son karışımın alkol oranı yüzde kaçtır?',
 dogru=a2,yan=[(pc(a0+Fr(80*20,100),100),'Alınan 20 L’deki alkolü (10 L) düşmemiş: (30 + 16) ÷ 100.','dikkat'),(pc(a1,60),'Su eklemeyi toplam hacme katmamış: 36 ÷ 60.','dikkat'),(pc(a1,60+20),'Toplamı 60 + 20 = 80 L almış: 36 ÷ 80.','islem'),(50,'Alma ve koymadan sonra ilk oranın değişmediğini sanıp suyu da atlamış.','bilgi')],
 istenen='Son karışımın alkol oranı (%).',
 ip=['60 L çözeltide kaç L alkol var? Alınan 20 L ve konan 20 L alkolü ne kadar değiştirir?'],
 bilgi=[CEK,EKLE],
 ad=[A('İlk alkol','60 L’nin %50’si.','30 L'),A('Alınan kısım','20 L’nin %50’si alkoldür.','10 L → kalan 30 − 10 = 20 L'),A('Konan kısım','20 L’nin %80’i alkoldür.','16 L → 20 + 16 = 36 L alkol (toplam 60 L)'),A('Su ekleme','Toplam 40 L artar, alkol sabit.','60 + 40 = 100 L'),A('Son oran','Alkol ÷ toplam.','36 ÷ 100 = %36')],
 puf='Aşamaları sırayla yaz: her aşamada alkol miktarını ve toplam hacmi ayrı güncelle; oranı yalnız en sonda hesapla.')

# ---- 16 zor · kuruyemiş, bilinmeyen eklenen miktar ----
fx=Fr(40*160-40*100,300-100); assert fx==12
xs=[x for x in range(1,200) if Fr(6400+100*x,40+x)==148]; assert xs==[10]
M('0016',tipId='krb-fiyat',tip='Fiyat karışımı',z='zor',alt='Fiyat ve Eklenen Miktar',kaz='Karışımın kilogram maliyetini ve yeni kilogram maliyetini kullanarak eklenen kuru üzüm miktarını bilinmeyenli denklemle bulur.',kalip='hikâyeli',
 kart='K-KRB-05 (fiyat karışımı, bilinmeyen ek miktar) · fındık içi ve kuru üzüm',
 metin='Kilogramı 300 TL olan fındık içi ile kilogramı 100 TL olan kuru üzüm karıştırılarak kilogramı 160 TL’ye mal olan 40 kg’lık bir karışım hazırlanıyor. Bu karışıma kilogramı 100 TL olan kuru üzümden bir miktar daha eklenince karışımın kilogram maliyeti 148 TL oluyor.\nBuna göre karışıma kaç kg kuru üzüm eklenmiştir?',
 dogru=10,yan=[(160-148,'Fiyat farkını (12) eklenen miktar sanmış.','dikkat'),(148-100,'Yeni fiyatla üzüm fiyatı arasındaki farkı (48) eklenen miktar sanmış.','dikkat'),(40,'İlk karışımın kütlesini (40 kg) eklenen miktar sanmış.','dikkat'),(Fr(40*12,200),'Fiyat farkını (12) ilk kütleyle çarpıp fındık–üzüm fiyat farkına (200) bölmüş.','islem')],
 istenen='Eklenen kuru üzüm miktarı (kg).',
 ip=['Eklenen miktara x kg de; yeni karışımın toplam maliyetini ve toplam kütlesini x cinsinden yaz.'],
 bilgi=[FIYAT],
 ad=[A('İlk toplam maliyet','40 kg, kilogramı 160 TL.','40 × 160 = 6400 TL'),A('Yeni toplamlar','x kg üzüm 100 TL’den eklenir.','maliyet 6400 + 100x · kütle 40 + x'),A('Denklem','Yeni kilogram maliyeti 148 TL.','(6400 + 100x) ÷ (40 + x) = 148 → 6400 + 100x = 5920 + 148x'),A('x’i bul','Denklemi çöz.','480 = 48x → x = 10 kg')],
 puf='Karışıma yeni miktar eklenince toplam maliyet ve toplam kütle birlikte güncellenir; yeni birim fiyat bunların bölümüdür.')

# ---- 17 orta · kuru üzüm ----
km=Fr(15*400,100); kuru=Fr(km*100,80); pak=kuru*1000/250
assert km==60 and kuru==75 and pak==300
M('0017',tipId='krb-buharlasma',tip='Buharlaşma ve kuruma',z='orta',alt='Kuruma',kaz='Kuruma sırasında kuru maddenin sabit kaldığını kullanarak kuru ürünün kütlesini ve paket sayısını bulur.',kalip='hikâyeli',
 kart='K-KRB-02 (kuruma) · taze üzüm',
 metin='Kütlece %85’i su olan 400 kg taze üzüm kurutulup kütlece %20’si su olan kuru üzüm haline getiriliyor. Elde edilen kuru üzümün tamamı 250 gramlık paketlere eksiksiz olarak dolduruluyor.\nBuna göre kaç paket doldurulmuştur?',
 dogru=pak,yan=[(Fr(km*1000,250),'Kuru madde miktarını (60 kg) kuru üzümün kütlesi sanmış.','dikkat'),(Fr(Fr(20*400,100)*1000,250),'Kuru üzümü taze üzümün %20’si (80 kg) almış.','bilgi'),(Fr(Fr(80*400,100)*1000,250),'Kuru üzümü taze üzümün %80’i (320 kg) almış.','bilgi'),(Fr((400-km)*1000,250),'Suyun kütlesini (340 kg) kuru üzüm sanmış.','dikkat')],
 istenen='Doldurulan paket sayısı.',
 ip=['Kuruma sırasında kütlesi değişmeyen kısım hangisidir? Taze üzümde bu kısım kaç kg’dır?'],
 bilgi=[KURU],
 ad=[A('Kuru madde','Taze üzümde su %85, kuru madde %15.','400 × 0,15 = 60 kg'),A('Kuru üzümün kütlesi','Kuru üzümde su %20, yani kuru madde %80’dir.','60 ÷ 0,80 = 75 kg'),A('Gram’a çevir','1 kg = 1000 g.','75 × 1000 = 75 000 g'),A('Paket sayısı','Toplam ÷ paket kütlesi.','75 000 ÷ 250 = 300')],
 puf='Kurumada su azalır, kuru madde sabit kalır; kuru maddeyi kuruma sonundaki kuru madde yüzdesine bölerek yeni kütleyi bul.')

# ---- 18 zor · öncüllü iki tuzlu su ----
A0=Fr(5*300,100); B0=Fr(15*200,100); sm=A0+B0
assert (A0,B0,sm)==(15,30,45) and pc(sm,500)==9 and Fr(5+15,2)==10
assert pc(sm,500+100)==Fr(15,2) and pc(sm+50,500+50)!=19 and pc(sm+50,500)==19 and pc(sm+100,500+100)!=Fr(15,2)
M('0018',tipId='krb-yorum',tip='Yorum ve yeni nesil karışım',z='zor',alt='Öncüllü Karışım',kaz='İki tuzlu su çözeltisinin karışımına yapılan işlemlerin sonuçlarını ayrı ayrı sınayarak doğru öncülleri belirler.',kalip='öncüllü',
 kart='K-KRB-06 (öncüllü karışım) · iki tuzlu suyun birleştirilmesi ve eklemeler',
 metin='Kütlece %5’i tuz olan 300 gram tuzlu su ile kütlece %15’i tuz olan 200 gram tuzlu su bir kapta karıştırılıyor. Buna göre,\nI. Karışımın tuz oranı %10’dur.\nII. Karışıma 100 gram su eklenirse tuz oranı %7,5 olur.\nIII. Karışıma 50 gram tuz eklenip tamamen çözülürse tuz oranı %19 olur.\nifadelerinden hangileri doğrudur?',
 dogru='Yalnız II',sira=['Yalnız I','Yalnız II','I ve II','II ve III','I, II ve III'],
 yan=[('Yalnız I','I’de iki yüzdenin ortalamasını (10) alıp doğru saymış; II’de eklenen 100 g’ı tuz sayıp II’yi yanlış bulmuş.','bilgi'),('I ve II','I’de iki yüzdenin ortalamasını (10) alıp I’i doğru saymış.','bilgi'),('II ve III','III’te tuz eklenince toplamı 500 g bırakıp 95 ÷ 500 = %19 bulmuş.','dikkat'),('I, II ve III','I’de yüzdelerin ortalamasını alıp, III’te tuz eklenince toplamı büyütmeden 95 ÷ 500 hesaplamış.','bilgi')],
 istenen='Doğru olan ifadeler.',
 ip=['İki çözeltideki tuzu ayrı ayrı gram olarak bul; üç ifadeyi karışımın tuz ve toplam miktarıyla tek tek sına.'],
 bilgi=[BIRL,EKLE],
 ad=[A('Tuz miktarları','300 g’ın %5’i ve 200 g’ın %15’i.','15 g + 30 g = 45 g tuz · toplam 500 g'),A('I','Tuz ÷ toplam.','45 ÷ 500 = %9 ≠ %10 ✗'),A('II','Su tuzu değiştirmez, toplam 600 g.','45 ÷ 600 = %7,5 ✓'),A('III','Tuz 95 g, toplam 550 g.','95 ÷ 550 ≈ %17,3 ≠ %19 ✗'),A('Sonuç','Yalnız II doğrudur.','Yalnız II')],
 puf='Önce karışımın toplam tuzunu ve toplam kütlesini bul; sonraki her ifadeyi bu iki sayıyı güncelleyerek ayrı ayrı sına.')

# ---- 19 zor · şeker puanı ----
t0=Fr(600,5); s0_=600-t0; s1=s0_-160; ekle=s1-t0
assert t0==120 and s0_==480 and s1==320 and ekle==200
th=Fr(25*600,100); sh=600-th; assert th==150 and sh==450 and (sh-160)-th==140
M('0019',tipId='krb-yorum',tip='Yorum ve yeni nesil karışım',z='zor',alt='Şeker Puanı',kaz='Tanımı verilen şeker puanını şekerin suya oranı olarak kullanıp buharlaşma ve şeker eklemeyi birlikte içeren bir durumda eklenecek şekeri bulur.',kalip='yeni nesil',
 kart='K-KRB-06 (yeni nesil) · şeker puanı tanımı, buharlaşma ve şeker ekleme',
 metin='Bir şerbetin şeker puanı, şerbetteki şeker kütlesinin su kütlesine oranının yüzde cinsinden değeridir. Örneğin 10 gram şeker ile 40 gram sudan oluşan şerbetin şeker puanı 25’tir.\nŞeker puanı 25 olan 600 gramlık şerbetten 160 gram su buharlaştırılıyor, ardından bir miktar şeker eklenerek tamamen çözülüyor ve şeker puanı 100 oluyor.\nBuna göre eklenen şeker kaç gramdır?',
 dogru=ekle,yan=[(sh-160-th,'Şeker puanını şeker oranıyla karıştırıp ilk şekeri 150 g, suyu 450 g almış ve 290 − 150 = 140 bulmuş.','bilgi'),(s0_-t0,'Buharlaşmayı hesaba katmayıp su 480 g iken 480 − 120 = 360 g şeker eklemiş.','dikkat'),(s1,'Son şeker miktarını (320 g) eklenen şeker sanmış.','dikkat'),(s0_,'Su miktarını (480 g) eklenen şeker sanmış.','dikkat')],
 istenen='Eklenen şeker miktarı (g).',
 ip=['Tanıma göre ilk şerbette şeker ve su kütlelerini ayrı ayrı bul; buharlaşmadan sonra hangisi değişir?'],
 bilgi=[B('Şeker puanı tanımı','şeker puanı = (şeker kütlesi ÷ su kütlesi) × 100. Örnek: 20 g şeker ve 80 g suda puan 25’tir'),BUHAR],
 ad=[A('Şeker ve su','Puan 25: şeker : su = 1 : 4, toplam 600 g.','şeker 120 g · su 480 g'),A('Buharlaşma','Yalnız su azalır.','su 480 − 160 = 320 g · şeker 120 g'),A('Yeni şeker','Puan 100: şeker kütlesi su kütlesine eşit.','şeker = 320 g'),A('Eklenen şeker','Yeni şekerden ilk şekeri çıkar.','320 − 120 = 200 g')],
 puf='Yeni nesil sorularda ölçü tanımını aynen uygula: burada payda toplam değil yalnız su kütlesidir; buharlaşma suyu azaltır, şeker eklemek şekeri artırır.')

bitir(P,'karisimiki',UK)
