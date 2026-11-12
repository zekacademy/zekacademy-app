"""İşçi Emek Problemleri · parti 2 (hafif mod): 19 ana soru, kardeş yok, ipucu 1. Her cevap ve çeldirici kodla doğrulanır."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_mat as H
from _hafif_mat import *
H.KONU='İşçi Emek Problemleri'
UK='prob|İşçi Emek Problemleri'
P=Parti('isciiki','İşçi Emek Problemleri',UK)
def M(no,**k): mk(P,no,adim=len(k['ad']),**k)
def r(a): return Fr(1,a)
BIRL=B('Birlikte çalışma','bir işi tek başına a günde bitiren kişi günde işin 1/a’sını yapar; birlikte günlük iş bu kesirlerin toplamıdır. Örnek: 6 ve 3 günde bitirenler günde 1/6 + 1/3 = 1/2 iş yapar ve işi birlikte 2 günde bitirir')
KISMI=B('İşin kesri','t günde yapılan iş = t × günlük hız; kalan iş = 1 − yapılan iş. Örnek: işi 10 günde bitiren kişi 4 günde işin 4/10 = 2/5’ini yapar, geriye 3/5 kalır')
VERIM=B('Verim ve süre','verim k katına çıkarsa süre k kat azalır; verim ile süre ters orantılıdır. Örnek: hızı 3/2 katına çıkan kişi 12 günlük işi 12 ÷ (3/2) = 8 günde bitirir')
HAVUZ=B('Havuz ve musluk','dolduran musluk +1/a, boşaltan −1/b iş yapar; net hız bunların toplamıdır. Örnek: 4 saatte dolduran ve 12 saatte boşaltan iki musluk birlikte 1/4 − 1/12 = 1/6 hızla çalışır')
MAK=B('Makine ve üretim','üretim = saatlik üretim × süre. Örnek: saatte 30 ürün yapan makine 4 saatte 30 × 4 = 120 ürün yapar')
UCRET=B('Ücret paylaşımı','ücret yapılan işle orantılı bölünür; yapılan iş = hız × çalışılan süre. Örnek: 1/10 hızla 6 gün çalışan ile 1/15 hızla 6 gün çalışan işin 3/5 ve 2/5’ini yapar; 100 TL ücret 60 ve 40 TL olur')
VARD=B('Dönüşümlü çalışma','bir turda yapılan iş toplanır, tam turlar sayılır; kalan iş sıradaki kişinin hızına bölünür. Örnek: 1/4 ve 1/6 hızla 1’er saat çalışan iki kişi bir turda 5/12 iş yapar')
ISGUN=B('İşçi–gün','eşit verimli işçilerde iş = işçi sayısı × gün. Örnek: 6 işçi 10 günde 60 işçi–gün iş yapar; aynı işi 12 işçi 5 günde bitirir')
TANIM=B('Tanımlı işlem','yeni bir işlemin tanımındaki sayılar yerine yazılır ve verilen sırayla uygulanır. Örnek: a ∗ b = a + 2b ise 3 ∗ 4 = 3 + 8 = 11')
KY='ÖSYM 2018–2026 TYT Matematik (işçi, havuz problemleri) · yayın soru bankaları (yalnız mantık) · MEB 9. sınıf'
kart('K-ISB-01','Birlikte ve dönüşümlü çalışma','Kişilerin günlük işleri toplanır; ikişerli süreler verilen üç kişide toplam hız, ikili hızların toplamının yarısıdır. Dönüşümlü çalışmada bir turluk iş toplanıp tam turlar sayılır, kalan iş sıradaki kişiyle bitirilir.','Süreleri toplamak ya da ortalamasını almak; ikişerli toplamlarda yarıya bölmeyi unutmak; son turun yarım kalabileceğini gözden kaçırmak.','orta','hikâyeli',3,'isb-birlikte','Birlikte ve dönüşümlü çalışma',KY)
kart('K-ISB-02','Ayrılma, katılma ve işin kesri','Yapılan iş ve kalan iş kesirle yazılır; sonradan katılan ya da ayrılan kişiye göre kalan işin süresi bulunur.','Kalan işi yeni hızla bölmeyi unutmak; geçen süreyi toplam süreye eklememek.','orta','hikâyeli',3,'isb-kismi','Ayrılma, katılma ve işin kesri',KY)
kart('K-ISB-03','Verim ve kapasite değişimi','Hız değişimi süreyle ters orantılıdır; farklı verimli işçiler ortak bir birime çevrilerek karşılaştırılır.','Hız artışını süre azalışı sanmak; yüzde artışı süreye aynı yüzdeyle uygulamak.','orta','hikâyeli',3,'isb-verim','Verim ve kapasite değişimi',KY)
kart('K-ISB-04','Havuz–musluk ve makine–ürün','Dolduran ve boşaltan hızlar işaretli toplanır; makinelerde üretim hız × süre ile bulunur; aşamalı sorularda her aşamanın işi ayrı yazılır.','Boşaltanı doldurucu saymak; aşamaların sürelerini birlikte almak; birim dönüşümünü atlamak.','orta','hikâyeli',3,'isb-hiz','Havuz–musluk ve makine–ürün',KY)
kart('K-ISB-05','Ücret paylaşımı','Ücret yapılan iş oranında bölünür; her kişinin yaptığı iş hızı ile çalıştığı sürenin çarpımıdır.','Ücreti çalışılan günle orantılamak; sonradan katılanın çalışma süresini yanlış bulmak.','zor','hikâyeli',5,'isb-ucret','Ücret paylaşımı',KY)
kart('K-ISB-06','Yeni nesil ve öncüllü','Tanımlı işlem ve öncüllü ifadeler, birlikte çalışma ve kısmi iş kesirleriyle ayrı ayrı sınanır.','Tanımı değiştirmek; öncülleri sınamadan tahminle işaretlemek.','zor','yeni nesil',4,'isb-yorum','Yeni nesil ve öncüllü işçi sorusu',KY)

# 01 kolay · dizgi birlikte
assert r(9)+r(18)==r(6)
M('0001',tipId='isb-birlikte',tip='Birlikte ve dönüşümlü çalışma',z='kolay',alt='Birlikte Çalışma',kaz='İki kişinin tek başına sürelerinden günlük işleri toplayarak birlikte bitirme süresini bulur.',kalip='hikâyeli',
 kart='K-ISB-01 (birlikte çalışma) · sayfa düzeni işi',
 metin='Bir ders kitabının sayfa düzenini Selin tek başına 9 saatte, Mert ise tek başına 18 saatte tamamlayabiliyor. İkisi de sabit hızla çalışmaktadır.\nSelin ile Mert birlikte çalışırsa sayfa düzenini kaç saatte tamamlar?',
 dogru=6,yan=[(9,'Hızlı çalışan Selin’in süresini birlikte süre sanmış.','dikkat'),(Fr(9+18,2),'İki sürenin aritmetik ortalamasını almış.','bilgi'),(18,'Yavaş çalışan Mert’in süresini yazmış.','dikkat'),(9+18,'Süreleri toplamış.','dikkat')],
 istenen='Birlikte tamamlama süresi (saat).',
 ip=['Her biri bir saatte işin kaçta kaçını yapar? Birlikte bir saatlik iş ne olur?'],
 bilgi=[BIRL],
 ad=[A('Saatlik iş','1 saatte yapılan iş 1/süre.','Selin 1/9 · Mert 1/18'),A('Birlikte saatlik iş','Kesirleri topla.','1/9 + 1/18 = 3/18 = 1/6'),A('Süre','İşin tamamı ÷ saatlik iş.','1 ÷ (1/6) = 6 saat')],
 puf='Birlikte çalışmada süreler değil, birim zamandaki işler (1/süre) toplanır.')

# 02 kolay · şişe
v=Fr(90,12); assert v*120==900
M('0002',tipId='isb-hiz',tip='Havuz–musluk ve makine–ürün',z='kolay',alt='Makine ve Üretim',kaz='Verilen süredeki üretimden makinenin hızını bulup farklı bir sürede üretimi hesaplar.',kalip='hikâyeli',
 kart='K-ISB-04 (makine–ürün) · şişeleme hattı',
 metin='Bir su şişeleme hattındaki dolum makinesi, sabit hızla her 12 dakikada 90 şişe dolduruyor.\nBu makine aynı hızla kesintisiz çalışırsa 2 saatte kaç şişe doldurur?',
 dogru=900,yan=[(v*2,'2 saati dakikaya çevirmeden dakikalık üretimi 2 ile çarpmış (7,5 × 2).','dikkat'),(90*2,'Verilen 90 şişeyi 2 ile çarpmış.','dikkat'),(90*12,'90 şişeyi 12 ile çarpmış.','islem'),(90*120,'90 şişeyi dakika cinsinden süreyle (120) çarpmış.','islem')],
 istenen='2 saatte doldurulan şişe sayısı.',
 ip=['Makine bir dakikada kaç şişe doldurur? 2 saat kaç dakikadır?'],
 bilgi=[MAK],
 ad=[A('Dakikalık üretim','90 şişe ÷ 12 dakika.','7,5 şişe/dk'),A('Süreyi dakikaya çevir','1 saat = 60 dakika.','2 saat = 120 dakika'),A('Toplam üretim','Dakikalık üretim × süre.','7,5 × 120 = 900 şişe')],
 puf='Önce birim zamandaki üretimi bul; süreyi aynı birime çevirmeden çarpma yapma.')

# 03 kolay · %25 hız
yeni=Fr(20)/Fr(125,100); assert yeni==16 and 20-yeni==4 and Fr(20*25,100)==5
M('0003',tipId='isb-verim',tip='Verim ve kapasite değişimi',z='kolay',alt='Hız Artışı',kaz='Hız %25 arttığında sürenin ters orantıyla azalmasını kullanarak işin kaç gün erken biteceğini bulur.',kalip='hikâyeli',
 kart='K-ISB-03 (%25 hız artışı) · çevirmen',
 metin='Bir kitabı sabit hızla çevirip 20 günde bitirebilen bir çevirmen, çalışma hızını %25 artırıyor.\nBuna göre bu çevirmen kitabı kaç gün erken bitirir?',
 dogru=4,yan=[(Fr(20*25,100),'Süreyi de %25 azaltıp kısalmayı 20 × 0,25 = 5 gün bulmuş.','bilgi'),(20-5,'Süreyi %25 azaltıp yeni süreyi 20 − 5 = 15 gün bulmuş ve bunu kısalma saymış.','bilgi'),(yeni,'Yeni süreyi (16 gün) kısalma sanmış.','dikkat'),(Fr(20*125,100),'Süreyi %25 artırıp 25 gün bulmuş.','dikkat')],
 istenen='Kitabın kaç gün erken bittiği.',
 ip=['Hız %25 artınca hız kaç katına çıkar? Hız ile süre arasında nasıl bir ilişki vardır?'],
 bilgi=[VERIM],
 ad=[A('Yeni hız','Hız 1,25 katına çıkar.','hız = 5/4 kat'),A('Yeni süre','Süre hız katının tersiyle çarpılır.','20 ÷ 5/4 = 16 gün'),A('Kısalma','İlk süre − yeni süre.','20 − 16 = 4 gün')],
 puf='Hız yüzde artarken süre aynı yüzdeyle azalmaz; süre, hız katının tersiyle çarpılır.')

# 04 kolay · kesir
assert Fr(6*5,2)==15
M('0004',tipId='isb-kismi',tip='Ayrılma, katılma ve işin kesri',z='kolay',alt='İşin Kesri',kaz='Belirli sürede yapılan işin kesrinden işin tamamının süresini bulur.',kalip='hikâyeli',
 kart='K-ISB-02 (işin kesri) · duvar örme',
 metin='Sabit hızla çalışan bir usta, bir duvarın 2/5’ini 6 günde örüyor.\nBu usta aynı hızla çalışmaya devam ederse duvarın tamamını kaç günde örer?',
 dogru=15,yan=[(Fr(6*2,5),'Süreyi kesirle çarpıp 6 × 2/5 hesaplamış.','islem'),(Fr(6,2),'Süreyi payına bölüp 6 ÷ 2 = 3 bulmuş.','islem'),(Fr(6*3,2),'Kalan 3/5’lik işin süresini (9 gün) toplam süre sanmış.','dikkat'),(6*2,'Süreyi payla çarpmış.','islem')],
 istenen='Duvarın tamamının örülme süresi (gün).',
 ip=['Usta bir günde duvarın kaçta kaçını örer?'],
 bilgi=[KISMI],
 ad=[A('Günlük iş','2/5 işi 6 günde yapıyor.','günde (2/5) ÷ 6 = 1/15'),A('Tamamının süresi','1 ÷ günlük iş.','15 gün'),A('Kontrol','15 günde 15 × 1/15 = 1 iş; 6 günde 6/15.','6/15 = 2/5 ✓')],
 puf='Kesirli iş ve süre verilirse önce birim zamandaki işi bul, sonra 1’i buna böl.')

# 05 orta · pompa musluk
x=1/(Fr(1,4)-Fr(1,12)); assert x==6 and Fr(1,4)+Fr(1,12)==Fr(1,3) and 4*12==48
M('0005',tipId='isb-hiz',tip='Havuz–musluk ve makine–ürün',z='orta',alt='Tank Boşaltma',kaz='Boşaltıcı ile dolduruncunun birlikte çalıştığı durumda net hızdan dolduruncunun süresini bulur.',kalip='hikâyeli',
 kart='K-ISB-04 (havuz–musluk) · pompa ile musluk, bilinmeyen musluk süresi',
 metin='Dolu bir su tankını P pompası tek başına 4 saatte boşaltmaktadır. Pompa ve M musluğu sabit debiyle çalışmaktadır. Pompa çalışırken aynı anda tankı bir M musluğu da doldurduğunda tank tamamen 12 saatte boşalmaktadır.\nBuna göre M musluğu boş tankı tek başına kaç saatte doldurur?',
 dogru=6,yan=[(12,'Birlikte boşalma süresini (12 saat) musluğun süresi sanmış.','dikkat'),(12-4,'Süreleri çıkarmış: 12 − 4.','islem'),(12+4,'Süreleri toplamış: 12 + 4.','islem'),(4*12,'Süreleri çarpmış.','islem')],
 istenen='M musluğunun tek başına doldurma süresi (saat).',
 ip=['Pompa saatte tankın kaçta kaçını boşaltır; ikisi birlikteyken tank saatte ne kadar boşalır?'],
 bilgi=[HAVUZ],
 ad=[A('Pompa hızı','4 saatte boşaltır.','−1/4 tank/saat'),A('Net hız','12 saatte boşalıyor.','−1/12 tank/saat'),A('Musluk hızı','Net hız = musluk − pompa.','M − 1/4 = −1/12 → M = 1/4 − 1/12 = 1/6'),A('Süre','1 ÷ (1/6).','6 saat')],
 puf='Net hız = doldurucu hızı − boşaltıcı hızı; tek başına süre için bilinmeyen hızı yalnız bırak.')

# 06 orta · ücret
th=Fr(1,1)/(r(10)+r(15)); assert th==6 and Fr(th,10)==Fr(3,5) and Fr(9000*3,5)==5400
M('0006',tipId='isb-ucret',tip='Ücret paylaşımı',z='orta',alt='Ücret Paylaşımı',kaz='Birlikte biten bir işte yapılan işe orantılı ücret paylaşımıyla bir kişinin payını bulur.',kalip='hikâyeli',
 kart='K-ISB-05 (ücret paylaşımı) · web sitesi tasarımı',
 metin='Elif ile Furkan bir web sitesi tasarımını tek başlarına sırasıyla 10 ve 15 günde bitirebiliyor. İkisi işe birlikte başlıyor ve işi birlikte bitiriyor. Toplam 9000 TL ücret alıyorlar ve bu ücreti yaptıkları işle orantılı olarak paylaşıyorlar.\nBuna göre Elif kaç TL almıştır?',
 dogru=5400,yan=[(Fr(9000*10,25),'Ücreti süreler (10 : 15) ile doğru orantılı bölüp Elif’e 2 parça vermiş.','bilgi'),(9000//2,'Ücreti eşit paylaştırmış.','bilgi'),(Fr(9000*10,15),'Elif’in süresini Furkan’ın süresine bölüp 9000 ile çarpmış.','islem'),(9000,'Toplam ücreti Elif’in payı sanmış.','dikkat')],
 istenen='Elif’in aldığı ücret (TL).',
 ip=['Birlikte ve dönüşümlü çalışmani bul; bu sürede her biri işin kaçta kaçını yapar?'],
 bilgi=[BIRL,UCRET],
 ad=[A('Birlikte süre','1/10 + 1/15 = 1/6.','6 gün'),A('Elif’in yaptığı iş','6 gün × 1/10.','6/10 = 3/5'),A('Elif’in ücreti','Ücret iş oranındadır.','9000 × 3/5 = 5400 TL')],
 puf='Ücret çalışılan günle değil yapılan işle orantılıdır; hızlı çalışan aynı sürede daha çok iş yapar.')

# 07 orta · üç kişi
S=(r(10)+r(12)+r(15))/2; assert S==Fr(1,8)
assert 1/((r(10)+r(12)+r(15))) == 4 and 1/(S/2)==16
M('0007',tipId='isb-birlikte',tip='Birlikte ve dönüşümlü çalışma',z='orta',alt='Üç Kişi, İkişerli Süreler',kaz='İkişerli birlikte çalışma süreleri verilen üç kişinin hepsinin birlikte çalışma süresini bulur.',kalip='hikâyeli',
 kart='K-ISB-01 (üç kişi, ikişerli süreler) · hasat',
 metin='Deniz, Emre ve Fatma bir tarlanın hasadını yapıyor. Üçünün de çalışma hızı sabittir. Deniz ile Emre hasadı birlikte 10 günde, Emre ile Fatma 12 günde, Deniz ile Fatma ise 15 günde bitirebiliyor.\nBuna göre üçü birlikte çalışırsa hasat kaç günde biter?',
 dogru=1/S,yan=[(4,'İkişerli günlük işleri toplayıp yarıya bölmeyi unutmuş (1/4).','dikkat'),(12,'Sürelerin ortanca değerini (12 gün) yazmış.','bilgi'),(16,'Toplamı iki kez yarıya bölmüş (1/16).','islem'),(10+12+15,'Üç süreyi toplamış.','dikkat')],
 istenen='Üç kişinin birlikte çalışma süresi (gün).',
 ip=['Üç ikili için günlük işleri yaz; bu kesirleri topladığında her kişi kaç kez sayılmış olur?'],
 bilgi=[BIRL],
 ad=[A('İkili günlük işler','Her ikili için 1/süre.','D+E = 1/10 · E+F = 1/12 · D+F = 1/15'),A('Topla','Her kişi iki kez sayılır.','2 (D + E + F) = 1/10 + 1/12 + 1/15 = 15/60 = 1/4'),A('Üçünün günlük işi','İkiye böl.','D + E + F = 1/8'),A('Süre','1 ÷ (1/8).','8 gün')],
 puf='İkişerli toplamlarda her kişi iki kez sayılır; üç kişinin hızı, ikili hızların toplamının yarısıdır.')

# 08 orta · robot 2 kat
rr=r(18); assert rr+2*rr==r(6)
M('0008',tipId='isb-verim',tip='Verim ve kapasite değişimi',z='orta',alt='Kapasite',kaz='Biri diğerinin iki katı hızlı iki makinenin birlikte süresinden yavaş olanın tek başına süresini bulur.',kalip='hikâyeli',
 kart='K-ISB-03 (kapasite, 2 katı hız) · boyama robotları',
 metin='Bir fabrikada yeni boyama robotu, eski boyama robotunun tam 2 katı hızla çalışıyor ve iki robotun da hızı sabittir. İki robot birlikte bir partiyi 6 saatte boyuyor.\nBuna göre eski robot aynı partiyi tek başına kaç saatte boyar?',
 dogru=18,yan=[(Fr(6,3),'Toplam hızı 3 parça sayıp süreyi 3’e bölmüş.','dikkat'),(Fr(6,2),'Süreyi hız katı olan 2’ye bölmüş.','dikkat'),(9,'Yeni robotun tek başına süresini (9 saat) yazmış.','dikkat'),(6*2,'Süreyi hız katıyla çarpmış.','islem')],
 istenen='Eski robotun tek başına süresi (saat).',
 ip=['Eski robotun saatlik işine r dersen yeni robotun saatlik işi ne olur?'],
 bilgi=[BIRL,VERIM],
 ad=[A('Hızları yaz','Eski r, yeni 2r.','birlikte r + 2r = 3r'),A('Birlikte süre','6 saatte biter.','3r = 1/6'),A('r’yi bul','Denklemi çöz.','r = 1/18'),A('Süre','Eski robotun tek başına süresi.','1 ÷ (1/18) = 18 saat')],
 puf='Hızlar arasında “k katı” ilişkisi varsa birini r al, diğerini k·r yaz; birlikte hız (k + 1) r olur.')

# 09 orta · öncüllü işçi–gün
iş=6*20; assert iş==120 and Fr(iş,8)==15 and Fr(iş,5)==24 and Fr(iş-6*5,10)+5==14
# I (doğru): 8 işçi 15 gün; II (yanlış): 5 işçi 25 gün (gerçek 24); III (doğru): 6 işçi 5 gün + 4 işçi katılır → 14 gün
assert 20+5==25 and 20-(8-6)==18 and Fr(iş,10)==12
M('0009',tipId='isb-yorum',tip='Yeni nesil ve öncüllü işçi sorusu',z='orta',alt='Öncüllü İşçi',kaz='Eşit verimli işçilerde işçi–gün ilişkisini kullanarak işçi sayısı değişimi ve sonradan katılma durumlarını ayrı ayrı sınayıp doğru öncülleri belirler.',kalip='öncüllü',
 kart='K-ISB-06 (öncüllü) · işçi–gün, işçi sayısı değişimi, sonradan katılma',
 metin='Eşit verimle çalışan 6 işçi bir işi 20 günde bitirebiliyor. Buna göre,\nI. Aynı verimle çalışan 8 işçi bu işi 15 günde bitirir.\nII. Aynı verimle çalışan 5 işçi bu işi 25 günde bitirir.\nIII. 6 işçi 5 gün çalıştıktan sonra aynı verimle çalışan 4 işçi daha katılırsa iş, başlangıçtan 14 gün sonra biter.\nifadelerinden hangileri doğrudur?',
 dogru='I ve III',sira=['Yalnız I','I ve II','I ve III','II ve III','I, II ve III'],
 yan=[('Yalnız I','III’te 4 işçinin baştan çalıştığını sanıp 120 ÷ 10 = 12 gün bulmuş ve III’ü yanlış saymış.','dikkat'),('I ve II','II’de işçi azalınca süreye 5 gün eklemeyi (20 + 5 = 25) doğru sanmış; III’te 4 işçiyi baştan çalışıyor sanıp 12 gün bulmuş.','bilgi'),('II ve III','I’de işçi 2 artınca süre 2 gün azalır sanıp 18 gün bulmuş; II’de süreye 5 gün eklemiş.','bilgi'),('I, II ve III','II’de işçi 1 azalınca süreyi 5 gün artırıp 25 bulmuş.','bilgi')],
 istenen='Doğru olan ifadeler.',
 ip=['İşin tamamını işçi–gün cinsinden kaç birim olarak yazarsın? Üç ifadeyi bu birimle tek tek sına.'],
 bilgi=[ISGUN],
 ad=[A('İş miktarı','6 işçi × 20 gün.','120 işçi–gün'),A('I','8 işçi.','120 ÷ 8 = 15 gün ✓'),A('II','5 işçi.','120 ÷ 5 = 24 gün ≠ 25 ✗'),A('III','İlk 5 gün 30 işçi–gün; kalan 90’ı 10 işçi yapar.','90 ÷ 10 = 9 gün → 5 + 9 = 14 gün ✓'),A('Sonuç','I ve III doğrudur.','I ve III')],
 puf='Eşit verimli işçilerde işi işçi–gün birimiyle yaz; işçi sayısı değişince bu birimi yeni sayıya böl, sonradan katılmalarda yapılan kısmı çıkar.')

# 10 orta · yeni nesil işlem
def op(a,b): return Fr(a*b,a+b)
x10=[x for x in range(1,200) if op(6,x)==4]; assert x10==[12] and op(6,12)==4
# hatalı çözümler: 6x = 24 + 4x
assert Fr(24,10)*10==24                      # 6x + 4x = 24 (işaret hatası) → 2,4
assert Fr(24,5)*5==24                        # 6x = 24 + x → 4,8
assert Fr(24,6)==4                           # 4x unutulmuş: 6x = 24 → 4
assert 6*24-4*24==2*24 and Fr(2*24,2)==24    # 2x = 24 sonucu x = 24 yazılmış
M('0010',tipId='isb-yorum',tip='Yeni nesil ve öncüllü işçi sorusu',z='orta',alt='Tanımlı İşlem',kaz='Birlikte çalışma süresi ifadesi tanımlı işlem olarak verildiğinde denklem kurup bilinmeyen işçi süresini bulur.',kalip='yeni nesil',
 kart='K-ISB-06 (yeni nesil) · birlikte çalışma süresi için tanımlı işlem',
 metin='Bir işi tek başına a günde ve b günde bitiren iki işçi sabit hızla birlikte çalışırsa işi (a · b) ÷ (a + b) günde bitirir. Bu süre, a ∗ b biçiminde gösterilmektedir.\nBir işi tek başına 6 günde bitiren işçi ile aynı işi tek başına x günde bitiren işçi birlikte çalıştığında 6 ∗ x = 4 olduğuna göre x kaçtır?',
 dogru=12,yan=[(Fr(24,10),'6x = 24 + 4x eşitliğinde 4x’i karşıya geçirirken işaret hatası yapıp 10x = 24 bulmuş.','islem'),(4,'6x = 24 + 4x eşitliğinde 4x’i unutup 6x = 24 yazmış.','islem'),(Fr(24,5),'4’ü yalnız 6’ya dağıtıp 6x = 24 + x, 5x = 24 bulmuş.','islem'),(24,'2x = 24 eşitliğinde x’i bulurken 2’ye bölmeyi unutup x = 24 yazmış.','islem')],
 istenen='İkinci işçinin işi tek başına bitirme süresi x (gün).',
 ip=['Tanımdaki a yerine 6, b yerine x yaz ve ifadeyi 4’e eşitle.'],
 bilgi=[TANIM,BIRL],
 ad=[A('Tanımı uygula','a = 6, b = x.','6x ÷ (6 + x) = 4'),A('Paydadan kurtul','İki tarafı (6 + x) ile çarp.','6x = 24 + 4x'),A('Çöz','x’li terimleri topla.','2x = 24'),A('x','Bölme.','x = 12 gün')],
 puf='Tanımlı işlemde yerine yazmayı sırasıyla yap, sonra ortaya çıkan basit denklemi çöz.')

# 11 orta · Hakan Selim
hk=Fr(4,14); kalan=1-hk; sel=kalan*21
assert hk==Fr(2,7) and sel==15
M('0011',tipId='isb-kismi',tip='Ayrılma, katılma ve işin kesri',z='orta',alt='İşi Bırakan Kişi',kaz='İlk kişinin yaptığı işi çıkarıp kalan işi ikinci kişinin hızıyla bölerek ikinci kişinin çalışma süresini bulur.',kalip='hikâyeli',
 kart='K-ISB-02 (biri başlayıp ayrılır) · ev boyası',
 metin='Bir ev boyasını Hakan tek başına 14 günde, Selim tek başına 21 günde bitirebiliyor. İkisinin de hızı sabittir. Hakan işe tek başına başlıyor, 4 gün çalıştıktan sonra işi bırakıyor ve kalan işi Selim tek başına bitiriyor.\nBuna göre Selim kaç gün çalışmıştır?',
 dogru=sel,yan=[(Fr(5,7)*14,'Kalan 5/7’lik işi Hakan’ın hızıyla bölmüş (14 × 5/7).','dikkat'),(Fr(21-4),'Hakan’ın 4 gününü Selim’in süresinden çıkarmış.','bilgi'),(4+sel,'Hesapladığı 15 güne Hakan’ın 4 gününü eklemiş.','dikkat'),(21+4,'Selim’in tek başına süresi olan 21 güne 4 gün eklemiş.','dikkat')],
 istenen='Selim’in çalıştığı süre (gün).',
 ip=['Hakan 4 günde işin kaçta kaçını yapar; geriye ne kadar iş kalır?'],
 bilgi=[KISMI],
 ad=[A('Hakan’ın işi','4 gün × 1/14.','4/14 = 2/7'),A('Kalan iş','1 − 2/7.','5/7'),A('Selim’in süresi','Kalan iş ÷ Selim’in günlük işi.','(5/7) ÷ (1/21) = 15 gün')],
 puf='Önce yapılan işi, sonra kalan işi kesirle yaz; kalan işi, işi bitirecek kişinin günlük işine böl.')

# 12 orta · makine A B
yan_=[]; kalan=1520-3*40; ts=Fr(kalan,100)+3; assert kalan==1400 and ts==17 and Fr(1400,40)==35 and Fr(1520,40)==38 and Fr(1520,100)==Fr(76,5)
M('0012',tipId='isb-hiz',tip='Havuz–musluk ve makine–ürün',z='orta',alt='İki Makine, Aşamalı',kaz='Önce tek makinenin çalıştığı, sonra ikincinin katıldığı üretimde toplam süreyi bulur.',kalip='hikâyeli',
 kart='K-ISB-04 (makine–ürün, aşamalı) · enjeksiyon makineleri',
 metin='Bir atölyede A makinesi saatte 40, B makinesi saatte 60 parça üretiyor; ikisi de sabit hızla çalışıyor. 1520 parçalık bir siparişe A makinesi tek başına başlıyor, 3 saat sonra B makinesi de devreye girip ikisi birlikte siparişi tamamlıyor.\nBuna göre sipariş, işe başlandıktan kaç saat sonra tamamlanır?',
 dogru=ts,yan=[(Fr(1400,100),'İlk 3 saati süreye eklememiş.','dikkat'),(Fr(1520,100),'A’nın ilk 3 saatteki üretimini çıkarmadan 1520 ÷ 100 hesaplamış.','dikkat'),(Fr(1400,40),'Kalan parçaları yalnız A makinesinin hızına bölmüş.','dikkat'),(Fr(1520,40),'Tüm siparişi yalnız A’nın hızıyla hesaplamış.','dikkat')],
 istenen='Siparişin tamamlanma süresi (saat).',
 ip=['A makinesi ilk 3 saatte kaç parça üretir; geriye kaç parça kalır, iki makine birlikte saatte kaç parça üretir?'],
 bilgi=[MAK,BIRL],
 ad=[A('İlk 3 saat','A saatte 40 parça.','3 × 40 = 120 parça'),A('Kalan sipariş','Toplamdan çıkar.','1520 − 120 = 1400 parça'),A('Birlikte süre','Birlikte saatte 40 + 60 = 100 parça.','1400 ÷ 100 = 14 saat'),A('Toplam süre','İlk 3 saati ekle.','3 + 14 = 17 saat')],
 puf='Aşamalı işlerde önce yalnız çalışan aşamayı hesapla; kalan işi birlikte hıza böl ve ilk aşamanın süresini toplam süreye ekle.')

# 13 orta · işçi katılım
t13=8*15; yap=8*3; kal=t13-yap; sg=Fr(kal,12); assert t13==120 and kal==96 and sg==8 and 3+sg==11 and Fr(t13,12)==10
M('0013',tipId='isb-kismi',tip='Ayrılma, katılma ve işin kesri',z='orta',alt='Sonradan Katılan İşçiler',kaz='İşçi sayısı sonradan artan bir işte iş miktarını işçi–gün olarak yazıp toplam süreyi bulur.',kalip='hikâyeli',
 kart='K-ISB-02 (işçi katılıyor) · tarla ekimi',
 metin='Eşit verimle çalışan 8 işçi bir tarlayı 15 günde ekebiliyor. Bu işçiler işe başladıktan 3 gün sonra, aynı verimle çalışan 4 işçi daha ekibe katılıyor.\nBuna göre tarlanın ekimi, işe başlandıktan kaç gün sonra biter?',
 dogru=3+sg,yan=[(sg,'Katılımdan sonra geçen süreyi (8 gün) toplam süre sanmış.','dikkat'),(Fr(t13,12),'12 işçinin işi baştan yaptığını sanıp 120 ÷ 12 hesaplamış.','dikkat'),(15-3,'Planlanan süreden 3 günü çıkarmış.','dikkat'),(3+Fr(t13,12),'12 işçi ile baştan hesaplanan 10 güne 3 gün eklemiş.','dikkat')],
 istenen='Ekimin biteceği gün sayısı.',
 ip=['İşi işçi–gün birimiyle yaz; ilk 3 günde ne kadar işçi–gün iş yapılmış?'],
 bilgi=[ISGUN],
 ad=[A('Toplam iş','8 işçi × 15 gün.','120 işçi–gün'),A('İlk 3 gün','8 işçi × 3 gün.','24 işçi–gün → kalan 96'),A('Yeni ekip','12 işçi kalanı yapar.','96 ÷ 12 = 8 gün'),A('Toplam','İlk 3 gün + 8 gün.','11 gün')],
 puf='Eşit verimli işçilerde işi işçi–gün birimiyle ifade et; yapılan kısmı çıkar, kalanı yeni işçi sayısına böl.')

# 14 zor · vardiya
a_,b_=r(8),r(12); tur=a_+b_; assert tur==Fr(5,24)
def vardiya():
    t=Fr(0); w=Fr(0)
    while True:
        for h in (a_,b_):
            if w+h>=1: return t+(1-w)/h
            w+=h; t+=1
sv=vardiya(); assert sv==Fr(19,2) and 4*tur==Fr(5,6) and 4*tur+a_==Fr(23,24) and Fr(24,5)==Fr(24,5)
assert Fr(1)/tur==Fr(24,5)
M('0014',tipId='isb-birlikte',tip='Birlikte ve dönüşümlü çalışma',z='zor',alt='Dönüşümlü Çalışma',kaz='Dönüşümlü çalışan iki makinenin bir turluk işini ve tam turları sayıp son turdaki kesirli süreyi bulur.',kalip='hikâyeli',
 kart='K-ISB-01 (dönüşümlü çalışma) · yükleme vinçleri',
 metin='Bir limanda bir geminin yüklenmesini A vinci tek başına 8 saatte, B vinci tek başına 12 saatte bitirebiliyor. İki vinç de sabit hızla çalışmaktadır. Vinçler dönüşümlü olarak çalışıyor: önce A vinci 1 saat, sonra B vinci 1 saat, sonra yine A vinci 1 saat çalışıyor ve bu düzen iş bitene kadar sürüyor. Aynı anda yalnız bir vinç çalışmaktadır.\nBuna göre gemi, işe başlandıktan kaç saat sonra yüklenmiş olur?',
 dogru=sv,yan=[(Fr(24,5),'Vinçlerin birlikte çalıştığını varsayıp 1 ÷ (1/8 + 1/12) hesaplamış.','bilgi'),(8,'4 tam turdan sonra işin bittiğini sanmış (8 saat).','dikkat'),(9,'9. saatin sonunda işin bittiğini sanmış (kalan 1/24’ü yok saymış).','dikkat'),(10,'Beşinci turun sonuna yuvarlamış.','dikkat')],
 istenen='Yüklemenin bitme süresi (saat).',
 ip=['A ve B’nin birer saatlik çalışmasıyla bir turda işin ne kadarı yapılır? Kaç tam tur sonrası iş bitmez?'],
 bilgi=[VARD],
 ad=[A('Bir tur','A 1 saat + B 1 saat.','1/8 + 1/12 = 5/24'),A('4 tur sonrası','8 saat.','4 × 5/24 = 5/6'),A('9. saat (A)','A bir saat daha çalışır.','5/6 + 1/8 = 23/24 → kalan 1/24'),A('B’nin yarım saati','Kalan işi B’nin hızına böl.','(1/24) ÷ (1/12) = 1/2 saat'),A('Toplam','9 saat + yarım saat.','9,5 saat')],
 puf='Dönüşümlü çalışmada bir turun işini bul, tam turları say; kalan işi sıradaki kişinin hızına bölerek son kesirli süreyi ekle.')

# 15 zor · ücret, üç kişi
rK,rL,rM=r(10),r(15),r(30); half=Fr(1,2); assert 3*(rK+rL)==half
d=half/(rK+rL+rM); assert d==Fr(5,2)
iK=3*rK+d*rK; iL=3*rL+d*rL; iM=d*rM; assert iK+iL+iM==1 and iM==Fr(1,12) and 9000*iM==750
M('0015',tipId='isb-ucret',tip='Ücret paylaşımı',z='zor',alt='Aşamalı Ücret Paylaşımı',kaz='Sonradan katılan kişinin çalışma süresini bulup yaptığı işe orantılı ücretini hesaplar.',kalip='hikâyeli',
 kart='K-ISB-05 (ücret paylaşımı, sonradan katılan) · parke döşeme',
 metin='Kemal, Lale ve Murat bir parke döşeme işini tek başlarına sırasıyla 10, 15 ve 30 günde bitirebiliyor. Üçünün de çalışma hızı sabittir. Kemal ile Lale işe birlikte başlıyor; 3 gün sonra Murat da onlara katılıyor ve üçü işi birlikte bitiriyor. İş bitince alınan 9000 TL ücret, herkesin yaptığı işle orantılı olarak paylaşılıyor.\nBuna göre Murat kaç TL almıştır?',
 dogru=750,yan=[(9000*Fr(3,30),'Murat’ın da 3 gün çalıştığını sanıp 3 ÷ 30 = 1/10 iş hesaplamış.','dikkat'),(9000*Fr(5,30),'Murat’ın da baştan katıldığını sanıp üçünün 5 günde bitirdiğini varsayarak 5 ÷ 30 = 1/6 iş hesaplamış.','bilgi'),(Fr(9000,3),'Ücreti üç kişi arasında eşit bölmüş.','bilgi'),(Fr(9000,2),'Kalan yarım işin ücretinin tamamını Murat’a vermiş.','dikkat')],
 istenen='Murat’ın aldığı ücret (TL).',
 ip=['İlk 3 günde Kemal ile Lale işin ne kadarını yapar? Kalan işi üçü birlikte kaç günde bitirir?'],
 bilgi=[BIRL,UCRET],
 ad=[A('İlk 3 gün','Kemal + Lale: 1/10 + 1/15 = 1/6.','3 × 1/6 = 1/2 iş, kalan 1/2'),A('Üçünün hızı','1/10 + 1/15 + 1/30.','6/30 = 1/5'),A('Murat’ın süresi','Kalan iş ÷ üçlü hız.','(1/2) ÷ (1/5) = 2,5 gün'),A('Murat’ın işi','2,5 × 1/30.','1/12'),A('Ücret','9000 × 1/12.','750 TL')],
 puf='Sonradan katılan kişinin çalışma süresini kalan işten bul; ücreti, yaptığı işin kesriyle toplam ücretten hesapla.')

# 16 zor · usta çırak, sonradan katılma
bir=2*2+4; tot=bir*9; assert bir==8 and tot==72
g1=4*2+2*1; yap=3*g1; g2=4*2+6*1; sg=Fr(tot-yap,g2); assert (g1,yap,g2,sg)==(10,30,14,3) and 3+sg==6
# hatalar
eş=Fr((2+4)*9); assert eş==54 and 54-3*6==36 and Fr(36,10)+3==Fr(33,5)   # usta = çırak: 6 kişi→ 4 kişi? (aşağıda doğrulanır)
# eşit sayma: başlangıç 6 kişi (4 usta + 2 çırak), 3 gün sonra 4 çırak daha → 10 kişi
eş_top=(2+4)*9; eş_kalan=eş_top-3*(4+2); eş_son=3+Fr(eş_kalan,4+2+4); assert eş_son==Fr(33,5)
# usta = çırağın yarısı
y_top=(2*Fr(1,2)+4)*9; y_g1=4*Fr(1,2)+2; y_g2=4*Fr(1,2)+6; y_son=3+(y_top-3*y_g1)/y_g2; assert y_top==45 and y_son==Fr(57,8)
M('0016',tipId='isb-verim',tip='Verim ve kapasite değişimi',z='zor',alt='Usta ve Çırak Verimi',kaz='Farklı verimli çalışanları ortak bir birime çevirip iş miktarını bularak sonradan çırak katılan ekibin toplam süresini hesaplar.',kalip='hikâyeli',
 kart='K-ISB-03 (verim farkı, ortak birim, sonradan katılma) · kaynak atölyesi',
 metin='Bir kaynak atölyesinde bir usta, bir çırağın tam 2 katı verimle çalışıyor; tüm usta ve çıraklar sabit hızla çalışmaktadır. 2 usta ve 4 çırak bir işi 9 günde bitiriyor.\n4 usta ve 2 çırak aynı işe başlıyor; 3 gün sonra 4 çırak daha ekibe katılıyor ve iş bu ekiple tamamlanıyor.\nBuna göre iş, başlangıçtan kaç gün sonra biter?',
 dogru=6,yan=[(3,'Katılımdan sonra geçen süreyi (3 gün) toplam süre sanmış.','dikkat'),(Fr(33,5),'Usta ile çırağı eşit verimli sayıp iş miktarını 54 kişi–gün alarak hesaplamış.','bilgi'),(y_son,'Ustayı çırağın yarısı kadar verimli sayıp iş miktarını 45 birim almış.','bilgi'),(9,'Ekip değişse de sürenin 9 gün kaldığını sanmış.','bilgi')],
 istenen='İşin bitme süresi (gün).',
 ip=['Bir çırağın günlük işine bir birim de; usta kaç birim eder? İşin tamamı kaç birimdir?'],
 bilgi=[ISGUN,VERIM],
 ad=[A('Birim belirle','1 çırak = 1 birim, 1 usta = 2 birim.','2 usta + 4 çırak = 4 + 4 = 8 birim/gün'),A('İş miktarı','Günlük birim × gün.','8 × 9 = 72 birim'),A('İlk 3 gün','4 usta + 2 çırak = 8 + 2 = 10 birim/gün.','3 × 10 = 30 birim → kalan 42'),A('Yeni ekip','4 usta + 6 çırak.','8 + 6 = 14 birim/gün'),A('Kalan süre','Kalan iş ÷ günlük birim.','42 ÷ 14 = 3 gün'),A('Toplam','İlk 3 gün + 3 gün.','6 gün')],
 puf='Farklı verimli çalışanları tek bir ortak birime çevir; iş miktarını bu birimle yazıp aşamaları ayrı ayrı hesapla.')

# 17 zor · pompa pompa musluk
n1=r(24)-r(12)-r(24); assert n1==-Fr(1,12)  # P1 -1/12, P2 -1/24, M +1/24 → net -1/12
fa=6*Fr(1,12); k2=1-fa; sf=k2/(r(12)+r(24)); assert fa==Fr(1,2) and sf==4 and 6+sf==10
assert 1/(Fr(1,12)) == 12 and 1/(r(12)+r(24))==8 and 6*(r(12)+r(24)+r(24))==1
M('0017',tipId='isb-hiz',tip='Havuz–musluk ve makine–ürün',z='zor',alt='Tank Boşaltma, Aşamalı',kaz='Pompalar ve bir musluğun birlikte çalıştığı, ardından musluğun kapandığı durumda iki aşamalı net hızlarla toplam süreyi bulur.',kalip='hikâyeli',
 kart='K-ISB-04 (havuz–musluk, aşamalı) · iki pompa ve bir musluk',
 metin='Dolu bir su tankını P1 pompası tek başına 12 saatte, P2 pompası tek başına 24 saatte boşaltabiliyor. Boş bir tankı M musluğu tek başına 24 saatte dolduruyor. Pompalar ve musluk sabit debiyle çalışmaktadır. Tank doluyken P1, P2 ve M aynı anda açılıyor; 6 saat sonra M musluğu kapatılıyor ve iki pompa çalışmaya devam ediyor.\nBuna göre tank, işe başlandıktan kaç saat sonra tamamen boşalır?',
 dogru=10,yan=[(4,'Yalnız son aşamanın süresini yazmış.','dikkat'),(6,'M musluğunu da boşaltıcı sanıp 1/12 + 1/24 + 1/24 = 1/6 hızla 6 saatte boşaldığını bulmuş.','bilgi'),(8,'M musluğunu hiç hesaba katmayıp iki pompayla 1 ÷ (1/12 + 1/24) hesaplamış.','bilgi'),(12,'Üçü sürekli açık kalmış gibi 1 ÷ (1/12) hesaplamış.','bilgi')],
 istenen='Tankın tamamen boşalma süresi (saat).',
 ip=['Üçü açıkken tank saatte ne kadar boşalır? 6 saatte tankın ne kadarı boşalmış olur?'],
 bilgi=[HAVUZ],
 ad=[A('İlk aşama hızı','Pompalar −, musluk +.','−1/12 − 1/24 + 1/24 = −1/12'),A('6 saatte boşalan','6 × 1/12.','1/2 tank'),A('İkinci aşama hızı','M kapalı, yalnız pompalar.','1/12 + 1/24 = 1/8 tank/saat'),A('Kalan süre','Kalan yarım tank.','(1/2) ÷ (1/8) = 4 saat'),A('Toplam','6 + 4.','10 saat')],
 puf='Aşamalı havuz sorularında her aşamanın net hızını ayrı yaz; aşama süresi × net hız ile işi güncelle.')

# 18 zor · sonradan katılma
zz,oo=r(20),r(12); x18=10-Fr(1,2)/oo*0-0
ork=Fr(1,2)/oo; kat=10-ork; assert ork==6 and kat==4 and 10*zz==Fr(1,2)
assert Fr(20*12,32)==Fr(15,2) and 10-Fr(15,2)==Fr(5,2) and 10-Fr(1,2)/(zz+oo)==Fr(25,4)
M('0018',tipId='isb-kismi',tip='Ayrılma, katılma ve işin kesri',z='orta',alt='Katılma Zamanı',kaz='Toplam süre verilen bir işte iki kişinin yaptığı işlerin toplamını 1’e eşitleyerek ikinci kişinin katılma zamanını bulur.',kalip='hikâyeli',
 kart='K-ISB-02 (toplam süre verilmiş, katılma zamanı) · kitap çevirisi',
 metin='Bir kitap çevirisini Zeynep tek başına 20 günde, Orhan tek başına 12 günde bitirebiliyor. İkisi de sabit hızla çalışıyor. Zeynep işe tek başına başlıyor; bir süre sonra Orhan da katılıyor ve çeviri, Zeynep başladıktan toplam 10 gün sonra bitiyor.\nBuna göre Orhan, Zeynep işe başladıktan kaç gün sonra çalışmaya katılmıştır?',
 dogru=kat,yan=[(10-Fr(20*12,32),'Birlikte bitirme süresi olan 7,5 günü toplam süreden çıkarıp 10 − 7,5 = 2,5 bulmuş.','bilgi'),(ork,'Orhan’ın çalıştığı 6 günü katılma zamanı sanmış.','dikkat'),(10-Fr(1,2)/(zz+oo),'Kalan yarım işin birlikte bitme süresini (3,75 gün) Orhan’ın çalışma süresi sanıp 10 − 3,75 = 6,25 bulmuş.','dikkat'),(10,'Toplam süreyi katılma zamanı sanmış.','dikkat')],
 istenen='Orhan’ın katılma zamanı (gün).',
 ip=['Zeynep 10 günün tamamında çalıştığına göre işin ne kadarını yapmıştır? Orhan’a kalan iş ne kadardır?'],
 bilgi=[KISMI,BIRL],
 ad=[A('Zeynep’in işi','10 gün × 1/20.','1/2'),A('Orhan’ın işi','Kalan yarım iş.','1 − 1/2 = 1/2'),A('Orhan’ın süresi','İş ÷ günlük iş.','(1/2) ÷ (1/12) = 6 gün'),A('Katılma zamanı','Toplam süreden Orhan’ın süresini çıkar.','10 − 6 = 4 gün')],
 puf='Toplam süre verilmişse her kişinin yaptığı işi (hız × çalıştığı süre) yaz ve toplamını 1’e eşitle.')

# 19 zor · öncüllü Ali Berk 12 24
rA,rB=r(12),r(24); b=rA+rB
assert 1/b==8 and 3*b==Fr(3,8) and 4*b==Fr(1,2) and Fr(1,2)/rB==12
assert Fr(12+24,2)!=8 and 3*Fr(1,18)!=Fr(3,8) and 3*rA==Fr(1,4) and Fr(1,2)/rB!=20
M('0019',tipId='isb-yorum',tip='Yeni nesil ve öncüllü işçi sorusu',z='zor',alt='Öncüllü İşçi',kaz='Birlikte çalışma, kısmi iş ve ayrılma durumlarını ayrı ayrı sınayarak doğru öncülleri belirler.',kalip='öncüllü',
 kart='K-ISB-06 (öncüllü) · birlikte süre, 3 günlük iş, ayrılma',
 metin='Bir işi Aslı tek başına 12 günde, Barış tek başına 24 günde bitirebiliyor. İkisinin de çalışma hızı sabittir. Buna göre,\nI. İkisi birlikte çalışırsa işi 8 günde bitirir.\nII. İkisi birlikte 3 gün çalışırsa işin 3/8’i biter.\nIII. İkisi 4 gün birlikte çalıştıktan sonra Aslı ayrılırsa kalan işi Barış tek başına 12 günde bitirir.\nifadelerinden hangileri doğrudur?',
 dogru='I, II ve III',sira=['Yalnız I','Yalnız III','I ve II','I ve III','I, II ve III'],
 yan=[('Yalnız I','II’de yalnız Aslı’nın hızıyla 3 × 1/12 = 1/4 bulmuş; III’te kalan işi Barış’ın süresinden 24 − 4 = 20 gün bulmuş.','dikkat'),('Yalnız III','I’de (12 + 24) ÷ 2 = 18 gün bulup I’i, II’de yalnız Aslı’nın hızıyla 3 × 1/12 = 1/4 bulup II’yi yanlış saymış; III’ü doğru bulmuş.','dikkat'),('I ve II','III’te kalan 1/2 işi Barış’ın hızıyla bölmek yerine 24 − 4 = 20 gün bulmuş.','dikkat'),('I ve III','II’de yalnız Aslı’nın hızıyla 3 × 1/12 = 1/4 hesaplamış.','dikkat')],
 istenen='Doğru olan ifadeler.',
 ip=['Aslı ve Barış’ın günlük işini kesir olarak yaz; birlikte günlük işi bulup üç ifadeyi tek tek sına.'],
 bilgi=[BIRL,KISMI],
 ad=[A('Birlikte günlük iş','1/12 + 1/24.','3/24 = 1/8'),A('I','1 ÷ (1/8).','8 gün ✓'),A('II','3 × 1/8.','3/8 ✓'),A('III','4 gün: 4 × 1/8 = 1/2; kalan 1/2’yi Barış 1/24 hızla yapar.','(1/2) ÷ (1/24) = 12 gün ✓'),A('Sonuç','Üçü de doğrudur.','I, II ve III')],
 puf='Önce birlikte günlük işi bul; her öncülü bu kesirle ayrı ayrı sına, ayrılma durumunda kalan işi kalan kişinin hızına böl.')

bitir(P,'isciiki',UK)
