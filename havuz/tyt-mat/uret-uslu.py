"""Üslü Sayılar · parti 1: 8 ana + 8 kardeş. Her cevap ve ara sonuç kodla doğrulanır."""
import sys,os
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,os.path.join(H,'..'))
from ortak import *
P=Parti('uslu','Üslü Sayılar','mat|Üslü Sayılar')
TT=lambda **k:k
NEG=B('Negatif üs','a⁻ⁿ = 1/aⁿ (a ≠ 0); işaret değişmez, sayı ters çevrilir. Örnek: 2⁻³ = 1/8 · 5⁻¹ = 1/5')
SIF=B('Sıfırıncı kuvvet','sıfırdan farklı her sayının 0. kuvveti 1’dir. Örnek: 7⁰ = 1 · (−4)⁰ = 1')
CRP=B('Aynı tabanda çarpma ve bölme','aᵐ × aⁿ = aᵐ⁺ⁿ · aᵐ ÷ aⁿ = aᵐ⁻ⁿ. Örnek: 10⁻⁶ × 10³ = 10⁻³ · 3⁵ ÷ 3² = 3³')
KK=B('Kuvvetin kuvveti','(aᵐ)ⁿ = aᵐⁿ, yani üsler çarpılır. Örnek: 9ˣ = (3²)ˣ = 3²ˣ · 27⁴ = (3³)⁴ = 3¹²')
ON=B('10’un kuvvetleri','10ⁿ, 1’in yanına n tane sıfır yazmaktır; 10⁻ⁿ = 1/10ⁿ. Örnek: 10³ = 1000 · 10⁻² = 0,01')
ORT=B('Ortak çarpan','aˣ⁺² = aˣ × a² ve aˣ⁻¹ = aˣ ÷ a. Örnek: 2ˣ⁺³ + 2ˣ = 2ˣ × (8 + 1) = 9 × 2ˣ')
POZ=B('Üslü ifade pozitiftir','a > 0 ise aˣ her x için pozitiftir. Örnek: 3⁻² = 1/9 > 0; 3ˣ hiçbir zaman −6 olamaz')

# ===== 0001 KOLAY us-kural (K-US-01)
assert Fr(1,2)+Fr(1,4)+1==Fr(7,4)
assert Fr(1,2)+Fr(1,4)+0==Fr(3,4) and Fr(1,2)+Fr(1,2)+1==2 and Fr(1,2)+Fr(1,4)+3==Fr(15,4) and 2+4+1==7
P.R('0001','us-kural','Üslü ifadelerde işlem kuralları','kolay','Negatif ve Sıfırıncı Kuvvet','Negatif ve sıfırıncı kuvvetleri kesre çevirerek toplama yapar.','düz',2,
 'K-US-01 (negatif ve sıfırıncı kuvvet) · üç terimli toplam, yeni tabanlar',
 '2⁻¹ + 4⁻¹ + 3⁰\nişleminin sonucu kaçtır?',
 ['3/4','7/4','2','15/4','7'],'B','Üç terimin toplamı.',
 ['Negatif üs sayının işaretini mi değiştirir, yoksa sayıyı ters mi çevirir?','Sıfırdan farklı bir sayının 0. kuvveti kaçtır?','Kesirleri toplarken paydaları eşitle.'],[NEG,SIF],
 [A('Negatif üsleri çevir','Negatif üs, sayının çarpmaya göre tersini verir; işaret değişmez.','2⁻¹ = 1/2 · 4⁻¹ = 1/4'),
  A('Sıfırıncı kuvvet','3 sıfırdan farklı olduğu için 0. kuvveti 1’dir.','3⁰ = 1'),
  A('Topla','Paydaları 4’te eşitle.','1/2 + 1/4 + 1 = 2/4 + 1/4 + 4/4 = 7/4')],
 'Negatif üs sayıyı negatif yapmaz, ters çevirir: a⁻¹ = 1/a.',
 dict(A='3/4, 3⁰’ı 0 almak; sıfırdan farklı her sayının 0. kuvveti 1’dir.',C='2, 4⁻¹’i 1/2 almak; 4⁻¹ = 1/4, üs −1 karekök demek değildir.',D='15/4, 3⁰’ı 3 almak; 0. kuvvet 1’dir.',E='7, negatif üsleri yok sayıp 2 + 4 + 1 toplamak.'),
 TT(A='bilgi',C='bilgi',D='bilgi',E='bilgi'))
assert Fr(1,3)+Fr(1,6)+1==Fr(3,2) and -3-6+1==-8 and Fr(1,3)+Fr(1,6)==Fr(1,2) and Fr(1,9)+1==Fr(10,9) and Fr(1,2)+5==Fr(11,2)
P.K('0001','3⁻¹ + 6⁻¹ + 5⁰\ntoplamı kaçtır?',
 ['−8','1/2','10/9','3/2','11/2'],'D','Üç terimin toplamı.',
 ['3⁻¹ ve 6⁻¹’i kesir olarak yaz.','5⁰ kaça eşittir?','1/3 ile 1/6’yı toplarken paydaları 6’da eşitle.'],[NEG,SIF],
 [A('Negatif üsleri çevir','Üs −1 olduğunda sayı ters çevrilir.','3⁻¹ = 1/3 · 6⁻¹ = 1/6'),
  A('Sıfırıncı kuvvet','5 sıfırdan farklı; 0. kuvveti 1.','5⁰ = 1'),
  A('Topla','Paydaları 6’da eşitle ve sadeleştir.','2/6 + 1/6 + 1 = 3/6 + 1 = 1/2 + 1 = 3/2')],
 'Üslü terimleri toplamadan önce her birini ayrı ayrı sayıya çevir.',
 dict(A='−8, negatif üssü sayının negatifi sanmak: −3 − 6 + 1.',B='1/2, 5⁰’ı 0 almak; 5⁰ = 1.',C='10/9, 3⁻¹ + 6⁻¹’i 9⁻¹ yapmak; üslü sayılar tabanları toplanarak toplanmaz.',E='11/2, 5⁰’ı 5 almak; 0. kuvvet 1’dir.'),
 TT(A='bilgi',B='bilgi',C='bilgi',E='bilgi'))

# ===== 0002 KOLAY us-bilimsel (K-US-02)
L=4*Fr(1,10**6)*5000; assert L==Fr(2,100) and L*1000==20                  # metre ve mm
assert 4*5*Fr(1,10**4)*1000==2 and 4*5*Fr(1,10**2)*1000==200 and L*10==Fr(2,10)
P.R('0002','us-bilimsel','Bilimsel gösterim ve 10’un kuvvetleri','kolay','Bilimsel Gösterim','10’un kuvvetleriyle verilen ölçülerle çarpma yapar ve sonucu istenen birime çevirir.','hikâyeli',2,
 'K-US-02 (bilimsel gösterimle ölçü) · yeni kurgu (yan yana hücreler), birim milimetre',
 'Çapı 4 × 10⁻⁶ metre olan özdeş hücreler, bir doğru boyunca aralarında boşluk kalmayacak biçimde yan yana dizilmiştir. Dizide 5000 hücre vardır.\nBuna göre bu dizinin uzunluğu kaç milimetredir?',
 ['0,02','0,2','2','20','200'],'D','Dizinin milimetre cinsinden uzunluğu.',
 ['5000’i 10’un kuvvetiyle yaz.','Katsayıları ayrı, 10’un kuvvetlerini ayrı çarp.','Sonucu milimetreye çevirmeyi unutma: 1 m kaç mm?'],[ON,CRP,B('Metre ve milimetre','1 m = 1000 mm, yani 10⁻³ m = 1 mm. Örnek: 0,5 m = 500 mm')],
 [A('Sayıyı 10’un kuvvetiyle yaz','5000, 5’in yanına üç sıfırdır.','5000 = 5 × 10³'),
  A('Uzunluğu hesapla','Toplam uzunluk = bir hücrenin çapı × hücre sayısı. Katsayıları ve kuvvetleri ayrı çarp.','4 × 10⁻⁶ × 5 × 10³ = 20 × 10⁻³ m'),
  A('Milimetreye çevir','10⁻³ m = 1 mm olduğundan sonuç doğrudan milimetre olur.','20 × 10⁻³ m = 0,02 m = 20 mm')],
 'Bilimsel gösterimde katsayıları ve 10’un kuvvetlerini ayrı çarp; en sonda birimi kontrol et.',
 dict(A='0,02, uzunluğu metre olarak bırakmak; soru milimetre soruyor.',B='0,2, 1 m = 10 mm sanmak; 1 m = 1000 mm.',C='2, 5000’i 5 × 10² yazmak; 5000 = 5 × 10³.',E='200, 5000’i 5 × 10⁴ yazmak; bir sıfır fazla sayılmış.'),
 TT(A='dikkat',B='bilgi',C='islem',E='islem'))
L=8*Fr(1,10**5)*2500; assert L==Fr(2,10) and L*100==20
assert 8*Fr(25,10)*Fr(1,10**3)*100==2 and L*1000==200 and L*10000==2000
P.K('0002','Bir yaprağının kalınlığı 8 × 10⁻⁵ metre olan özdeş kâğıtlardan 2500 tanesi, aralarında boşluk kalmadan üst üste konarak bir deste yapılmıştır.\nBuna göre bu destenin yüksekliği kaç santimetredir?',
 ['0,2','2','20','200','2000'],'C','Destenin santimetre cinsinden yüksekliği.',
 ['2500’ü 25 × 10ⁿ biçiminde yaz.','8 × 25 kaç eder? 10’un kuvvetlerini topla.','Bulduğun metreyi santimetreye çevir.'],[ON,CRP,B('Metre ve santimetre','1 m = 100 cm = 10² cm. Örnek: 0,3 m = 30 cm')],
 [A('Sayıyı 10’un kuvvetiyle yaz','2500 = 25 × 100.','2500 = 25 × 10²'),
  A('Yüksekliği hesapla','Deste yüksekliği = bir yaprağın kalınlığı × yaprak sayısı.','8 × 10⁻⁵ × 25 × 10² = 200 × 10⁻³ = 0,2 m'),
  A('Santimetreye çevir','1 m = 100 cm.','0,2 × 100 = 20 cm')],
 'Önce sayıyı 10’un kuvvetiyle yaz, sonra çarp; birim dönüşümünü en sona bırak.',
 dict(A='0,2, sonucu metre olarak bırakmak; soru santimetre soruyor.',B='2, 2500’ü 25 × 10 gibi bir sıfır eksik yazmak; sonuç 10 kat küçük çıkar.',D='200, sonucu milimetreye çevirmek; soru santimetre soruyor.',E='2000, 1 m = 10 000 cm sanmak; 1 m = 100 cm.'),
 TT(A='dikkat',B='islem',D='dikkat',E='bilgi'))

# ===== 0003 ORTA us-ortak-carpan (K-US-03)
v=[x for x in range(-10,20) if Fr(5)**(x+1)-Fr(5)**(x-1)==600]; assert v==[3] and 5**4==625 and 5**2*24==600
P.R('0003','us-ortak-carpan','Ortak çarpan parantezine alma','orta','Ortak Çarpan','Farklı kuvvetlerden oluşan üslü toplamda en küçük kuvveti ortak çarpan yapar ve istenen kuvveti bulur.','düz',3,
 'K-US-03 (en küçük kuvvet parantezine alma) · fark biçimi, yeni istenen (5ˣ⁺¹)',
 '5ˣ⁺¹ − 5ˣ⁻¹ = 600\nolduğuna göre 5ˣ⁺¹ kaçtır?',
 ['3','25','125','600','625'],'E','5ˣ⁺¹ ifadesinin değeri.',
 ['Hangi kuvvet daha küçük? Onu ortak çarpan parantezine al.','5ˣ⁺¹, 5ˣ⁻¹’in kaç katıdır?','Bulduğun değer sorulan ifade mi? Sorulana dönüştür.'],[ORT,CRP],
 [A('Ortak çarpan seç','Küçük kuvvet 5ˣ⁻¹. 5ˣ⁺¹ = 5ˣ⁻¹ × 5².','5ˣ⁺¹ − 5ˣ⁻¹ = 5ˣ⁻¹ × (25 − 1)'),
  A('Parantezi hesapla','25 − 1 = 24.','24 × 5ˣ⁻¹ = 600 ⇒ 5ˣ⁻¹ = 25'),
  A('Sorulana çevir','5ˣ⁺¹, 5ˣ⁻¹’in 5² = 25 katıdır.','5ˣ⁺¹ = 25 × 25 = 625 (x = 3)')],
 'Üslü toplamda en küçük kuvveti ortak çarpan yap; sonunda bulduğun kuvveti sorulana çevir.',
 dict(A='3, x’in değeri; soru 5ˣ⁺¹’i soruyor.',B='25, 5ˣ⁻¹’in değeri; soru 5ˣ⁺¹’i soruyor.',C='125, 5ˣ’in değeri; soru 5ˣ⁺¹’i soruyor.',D='600, 5ˣ⁻¹ terimini yok sayıp 5ˣ⁺¹’i 600 almak.'),
 TT(A='dikkat',B='dikkat',C='dikkat',D='islem'))
v=[x for x in range(-10,20) if Fr(3)**(x+1)+Fr(3)**x+Fr(3)**(x-1)==117]; assert v==[3] and 9+3+1==13 and 13*9==117
P.K('0003','3ˣ⁺¹ + 3ˣ + 3ˣ⁻¹ = 117\nolduğuna göre 3ˣ kaçtır?',
 ['3','9','13','27','81'],'D','3ˣ ifadesinin değeri.',
 ['Üç terimin en küçük kuvveti hangisi?','3ˣ⁺¹ ve 3ˣ, 3ˣ⁻¹’in kaç katıdır?','Önce 3ˣ⁻¹’i bul, sonra 3ˣ’e geç.'],[ORT,CRP],
 [A('Ortak çarpan seç','En küçük kuvvet 3ˣ⁻¹. 3ˣ⁺¹ = 3ˣ⁻¹ × 9 ve 3ˣ = 3ˣ⁻¹ × 3.','3ˣ⁻¹ × (9 + 3 + 1) = 117'),
  A('Parantezi hesapla','9 + 3 + 1 = 13.','13 × 3ˣ⁻¹ = 117 ⇒ 3ˣ⁻¹ = 9'),
  A('Sorulana çevir','3ˣ, 3ˣ⁻¹’in 3 katıdır.','3ˣ = 9 × 3 = 27 (x = 3)')],
 'Parantez içine giren sayılar, her terimin en küçük kuvvete göre kaç katı olduğunu gösterir.',
 dict(A='3, x’in değeri; soru 3ˣ’i soruyor.',B='9, 3ˣ⁻¹’in değeri; bir adım eksik kalmış.',C='13, parantezin içi; 117’nin 13’e bölünmesi unutulmuş.',E='81, 3ˣ⁺¹’in değeri; soru 3ˣ’i soruyor.'),
 TT(A='dikkat',B='dikkat',C='islem',E='dikkat'))

# ===== 0004 ORTA us-denklem (K-US-04)
v=[x for x in range(-30,30) if Fr(1,9)**x==Fr(27)**(x-5)]; assert v==[3]
assert [x for x in range(-30,30) if 2*x==3*x-15]==[15] and [x for x in range(-30,30) if -2*x==3*x-5]==[1] and 5*(-3)==-15 and 3*5==15
P.R('0004','us-denklem','Üslü denklemler','orta','Üslü Denklem','Kesirli ve tam sayı tabanları ortak tabana çevirerek üsleri eşitler.','düz',3,
 'K-US-04 (ortak tabana çevirme) · kesirli taban (1/9) ve 27, yeni sayılar',
 '(1/9)ˣ = 27ˣ⁻⁵\nolduğuna göre x kaçtır?',
 ['−3','1','3','5','15'],'C','x’in değeri.',
 ['1/9 ve 27’yi 3’ün kuvveti olarak yaz.','1/9 = 3’ün hangi kuvveti? İşarete dikkat.','Tabanlar eşitlenince üsleri eşitle.'],[NEG,KK],
 [A('Ortak tabana çevir','1/9 = 1/3² = 3⁻² ve 27 = 3³.','(3⁻²)ˣ = (3³)ˣ⁻⁵'),
  A('Kuvvetin kuvveti','Üsler çarpılır; parantezdeki her terim çarpılmalı.','3⁻²ˣ = 3³ˣ⁻¹⁵'),
  A('Üsleri eşitle','Tabanlar aynı olunca üsler eşit olur.','−2x = 3x − 15 ⇒ −5x = −15 ⇒ x = 3'),
  A('Kontrol','x = 3 için iki taraf da 3⁻⁶.','(1/9)³ = 1/729 · 27⁻² = 1/729 ✓')],
 'Kesirli tabanı negatif üsle yaz: 1/aⁿ = a⁻ⁿ; sonra tek tabanda üsleri eşitle.',
 dict(A='−3, son adımda −5x = −15’i x = −3 bulmak; eksi bölü eksi artıdır.',B='1, 27ˣ⁻⁵’i 3³ˣ⁻⁵ yazmak; 3, x − 5’in iki terimiyle de çarpılmalı.',D='5, −2x’i görmeyip 3x = 15 çözmek.',E='15, 1/9’u 3² sanmak; 1/9 = 3⁻².'),
 TT(A='islem',B='islem',D='islem',E='bilgi'))
v=[x for x in range(-30,30) if Fr(1,27)**x==Fr(9)**(x+5)]; assert v==[-2]
assert [x for x in range(-30,30) if 3*x==2*x+10]==[10] and [x for x in range(-30,30) if -3*x==2*x+5]==[-1] and [x for x in range(-30,30) if 5*x==10]==[2] and [x for x in range(-30,30) if -x==10]==[-10]
P.K('0004','(1/27)ˣ = 9ˣ⁺⁵\neşitliğini sağlayan x değeri kaçtır?',
 ['−10','−2','−1','2','10'],'B','x’in değeri.',
 ['1/27 ve 9’u 3’ün kuvveti olarak yaz.','Kuvvetin kuvvetinde üsler çarpılır; parantezin tamamına dikkat.','Üsleri eşitleyip denklemi çöz; işaretleri kontrol et.'],[NEG,KK],
 [A('Ortak tabana çevir','1/27 = 3⁻³ ve 9 = 3².','(3⁻³)ˣ = (3²)ˣ⁺⁵'),
  A('Kuvvetin kuvveti','Üsleri çarp.','3⁻³ˣ = 3²ˣ⁺¹⁰'),
  A('Üsleri eşitle','Tabanlar aynı.','−3x = 2x + 10 ⇒ −5x = 10 ⇒ x = −2'),
  A('Kontrol','x = −2 için iki taraf da 3⁶.','(1/27)⁻² = 27² = 729 · 9³ = 729 ✓')],
 'Bir tarafı kesirli tabanlı üslü denklemde çözüm çoğu zaman negatif çıkar; işaretleri adım adım takip et.',
 dict(A='−10, −3x − 2x’i −x hesaplamak; −3x − 2x = −5x.',C='−1, 9ˣ⁺⁵’i 3²ˣ⁺⁵ yazmak; 2, x + 5’in iki terimiyle de çarpılmalı.',D='2, −5x = 10’u x = 2 bulmak; eksi işareti kaybolmuş.',E='10, 1/27’yi 3³ sanmak; 1/27 = 3⁻³.'),
 TT(A='islem',C='islem',D='islem',E='bilgi'))

# ===== 0005 ORTA us-buyume (K-US-05)
gun=[3**k for k in range(1,6)]; assert sum(gun[:4])==120 and gun[3]==81 and sum(gun)==363 and 3*4==12
P.R('0005','us-buyume','Katlanarak artma ve azalma','orta','Katlanarak Artma','Her adımda sabit katına çıkan bir niceliği üslü ifadeyle yazar ve belirli bir adıma kadar toplamını bulur.','hikâyeli',3,
 'K-US-05 (her adımda sabit katına çıkma) · yeni kurgu (okulda duyuru), yeni istenen (toplam)',
 'Bir okulda bir duyuru şöyle yayılmıştır: 1. gün müdür duyuruyu 3 öğrenciye söylemiştir. Sonraki her gün, bir önceki gün duyuruyu öğrenen her öğrenci, duyuruyu henüz bilmeyen 3 yeni öğrenciye söylemiştir. Hiçbir öğrenciye duyuru iki kez söylenmemiştir.\nBuna göre 4. günün sonunda duyuruyu öğrenmiş toplam öğrenci sayısı kaçtır?',
 ['12','81','120','121','363'],'C','İlk 4 günde duyuruyu öğrenen öğrencilerin toplamı.',
 ['1. gün kaç öğrenci öğrendi? 2. gün bu sayının kaç katı öğrendi?','Her gün yeni öğrenen sayısını 3’ün kuvveti olarak yaz.','Soru yalnız 4. günü değil, 4 günün toplamını soruyor.'],[B('Katlanarak artma','her adımda sayı 3 katına çıkıyorsa n. adımdaki sayı 3ⁿ olur. Örnek: 3, 9, 27, 81 → 4. adım 3⁴ = 81')],
 [A('Her günü yaz','1. gün 3 öğrenci; sonraki her gün bir önceki günün 3 katı kadar yeni öğrenci.','3¹ = 3 · 3² = 9 · 3³ = 27 · 3⁴ = 81'),
  A('Topla','4. günün sonuna kadar öğrenenlerin hepsi sayılır.','3 + 9 + 27 + 81 = 120'),
  A('Müdürü ayır','Soru öğrenci sayısını soruyor; müdür sayılmaz.','120 öğrenci')],
 '“n. günün sonunda toplam” soruluyorsa her günü ayrı yazıp topla; yalnız son günü alma.',
 dict(A='12, her gün 3 yeni öğrenci eklendiğini sanmak (3 × 4); sayı her gün 3 katına çıkıyor.',B='81, yalnız 4. gün öğrenenler; soru toplamı soruyor.',D='121, müdürü de saymak; soru öğrenci sayısını soruyor.',E='363, 5 günü toplamak; soru 4. günün sonunu soruyor.'),
 TT(A='bilgi',B='dikkat',D='dikkat',E='dikkat'))
tur=[4**k for k in range(1,5)]; assert sum(tur[:3])==84 and tur[2]==64 and sum(tur)==340 and 4**4==256
P.K('0005','Bir bilgi yarışmasına katılım şöyle olmuştur: 1. turda yarışmayı düzenleyen kişi 4 kişiyi davet etmiştir. Sonraki her turda, bir önceki turda davet edilen her kişi, daha önce davet edilmemiş 4 yeni kişiyi davet etmiştir.\nBuna göre ilk 3 turda davet edilen kişilerin toplam sayısı kaçtır?',
 ['64','84','85','256','340'],'B','İlk 3 turda davet edilenlerin toplamı.',
 ['1. turda kaç kişi davet edildi? Her tur kaç katına çıkıyor?','Her turu 4’ün kuvveti olarak yaz.','Düzenleyen kişi davet edilmedi; onu sayma.'],[B('Katlanarak artma','her adımda sayı 4 katına çıkıyorsa n. adımdaki sayı 4ⁿ olur. Örnek: 4, 16, 64 → 3. adım 4³ = 64')],
 [A('Her turu yaz','1. tur 4 kişi; sonraki her tur bir öncekinin 4 katı.','4¹ = 4 · 4² = 16 · 4³ = 64'),
  A('Topla','İlk 3 turda davet edilenlerin hepsi.','4 + 16 + 64 = 84'),
  A('Kontrol','Düzenleyen kişi davet edilmediği için eklenmez.','84 kişi')],
 'Katlanarak artan toplamda her adımı ayrı yaz; kimin sayıldığını sorudan kontrol et.',
 dict(A='64, yalnız 3. turda davet edilenler; soru toplamı soruyor.',C='85, düzenleyen kişiyi de saymak; o davet edilmedi.',D='256, 3. turdaki sayıyı 4⁴ almak; n. turda 4ⁿ kişi davet edilir.',E='340, 4 turu toplamak; soru ilk 3 turu soruyor.'),
 TT(A='dikkat',C='dikkat',D='islem',E='dikkat'))

# ===== 0006 ORTA us-siralama (K-US-06)
a,b,c=2**40,3**30,5**20; assert a<c<b and 2**40==16**10 and 3**30==27**10 and 5**20==25**10
assert 9**10<16**10<25**10 and 10**10<16**10<27**10      # çeldirici C (3³ = 9) ve D (5² = 10)
P.R('0006','us-siralama','Üslü sayıları karşılaştırma','orta','Sıralama','Üsleri ortak bölenle eşitleyerek üslü sayıları tabanlarına göre sıralar.','düz',3,
 'K-US-06 (ortak kuvvete getirerek karşılaştırma) · üç sayı, yeni taban ve üsler',
 'a = 2⁴⁰\nb = 3³⁰\nc = 5²⁰\nolduğuna göre a, b ve c sayılarının doğru sıralanışı aşağıdakilerden hangisidir?',
 ['a < c < b','a < b < c','b < a < c','c < a < b','c < b < a'],'A','Üç sayının küçükten büyüğe sıralanışı.',
 ['40, 30 ve 20’nin ortak böleni hangisi?','Her sayıyı (…)¹⁰ biçiminde yaz.','Üsler eşitse büyük tabanlı sayı büyüktür.'],[KK,B('Aynı üs, farklı taban','üsler eşit ve pozitifse tabanı büyük olan sayı büyüktür. Örnek: 3¹⁰ < 4¹⁰')],
 [A('Ortak üs seç','40, 30 ve 20’nin ortak böleni 10.','2⁴⁰ = (2⁴)¹⁰ · 3³⁰ = (3³)¹⁰ · 5²⁰ = (5²)¹⁰'),
  A('Tabanları hesapla','2⁴ = 16, 3³ = 27, 5² = 25.','a = 16¹⁰ · b = 27¹⁰ · c = 25¹⁰'),
  A('Sırala','Üsler eşit; tabanlara bak: 16 < 25 < 27.','a < c < b')],
 'Üslü sayıları karşılaştırmak için önce üsleri (ya da tabanları) eşitle; ikisi birden farklıyken karar verme.',
 dict(B='a < b < c, yalnızca tabanlara (2, 3, 5) bakmak; üsler farklıyken taban tek başına karar vermez.',C='b < a < c, 3³’ü 9 hesaplamak; 3³ = 27.',D='c < a < b, 5²’yi 10 hesaplamak; 5² = 25.',E='c < b < a, yalnızca üslere (40, 30, 20) bakmak.'),
 TT(B='bilgi',C='islem',D='islem',E='bilgi'))
x,y,z=2**60,3**40,7**20; assert z<x<y and x==8**20 and y==9**20
assert 6**20<7**20<9**20 and 6**20<7**20<8**20
P.K('0006','x = 2⁶⁰\ny = 3⁴⁰\nz = 7²⁰\nolduğuna göre x, y ve z arasındaki sıralama aşağıdakilerden hangisidir?',
 ['z < x < y','x < y < z','x < z < y','y < z < x','z < y < x'],'A','Üç sayının küçükten büyüğe sıralanışı.',
 ['60, 40 ve 20’nin ortak böleni hangisi?','Her sayıyı (…)²⁰ biçiminde yaz.','Üsler eşitlenince tabanları karşılaştır.'],[KK,B('Aynı üs, farklı taban','üsler eşit ve pozitifse tabanı büyük olan sayı büyüktür. Örnek: 5²⁰ < 6²⁰')],
 [A('Ortak üs seç','60, 40 ve 20’nin ortak böleni 20.','2⁶⁰ = (2³)²⁰ · 3⁴⁰ = (3²)²⁰ · 7²⁰'),
  A('Tabanları hesapla','2³ = 8 ve 3² = 9.','x = 8²⁰ · y = 9²⁰ · z = 7²⁰'),
  A('Sırala','Tabanlar: 7 < 8 < 9.','z < x < y')],
 'Üsler arasında ortak bölen varsa sayıları aynı üsse getir; karşılaştırma tabanlara kalır.',
 dict(B='x < y < z, yalnızca tabanlara (2, 3, 7) bakmak.',C='x < z < y, 2³’ü 6 hesaplamak; 2³ = 8.',D='y < z < x, 3²’yi 6 hesaplamak; 3² = 9.',E='z < y < x, yalnızca üslere (60, 40, 20) bakmak.'),
 TT(B='bilgi',C='islem',D='islem',E='bilgi'))

# ===== 0007 ZOR us-denklem (K-US-07)
kok=[a for a in range(-60,61) if 9*a*a-27*a==486]; assert sorted(kok)==[-6,9]
assert 9**3-3**5==486 and [x for x in range(-5,10) if 9**(x+1)-3**(x+3)==486]==[2]
assert sorted(a for a in range(-60,61) if (a+9)*(a-6)==0)==[-9,6]       # yanlış çarpanlara ayırma
P.R('0007','us-denklem','Üslü denklemler','zor','Değişken Değiştirme','Üslü denklemi değişken değiştirerek ikinci dereceden denkleme çevirir; üslü ifadenin pozitifliğiyle kökü seçer.','düz',4,
 'K-US-07 (9ˣ = (3ˣ)² ile değişken değiştirme) · fark biçimi, negatif kökü eleme',
 '9ˣ⁺¹ − 3ˣ⁺³ = 486\nolduğuna göre 3ˣ kaçtır?',
 ['−9','−6','2','6','9'],'E','3ˣ ifadesinin değeri.',
 ['3ˣ’e bir harf ver: 3ˣ = a. 9ˣ⁺¹ ve 3ˣ⁺³’ü a ile yaz.','Elde ettiğin ikinci dereceden denklemi sadeleştir ve çarpanlarına ayır.','3ˣ negatif olabilir mi?'],[KK,POZ,B('Değişken değiştirme','tekrar eden ifadeye harf ver: 3ˣ = a ise 9ˣ = (3²)ˣ = (3ˣ)² = a²')],
 [A('Harf ver','3ˣ = a olsun. 9ˣ⁺¹ = 9 × 9ˣ ve 9ˣ = (3ˣ)².','9ˣ⁺¹ = 9a² · 3ˣ⁺³ = 27a'),
  A('Denklemi kur','Denklemi 9’a böl.','9a² − 27a = 486 ⇒ a² − 3a − 54 = 0'),
  A('Çarpanlara ayır','Çarpımı −54, toplamı −3 olan iki sayı: −9 ve 6.','(a − 9) × (a + 6) = 0 ⇒ a = 9 ya da a = −6'),
  A('Pozitif kökü seç','3ˣ her zaman pozitif; −6 olamaz.','3ˣ = 9 (x = 2) · kontrol: 9³ − 3⁵ = 729 − 243 = 486 ✓')],
 'aˣ’e harf verdiğinde çıkan negatif kökü ele: a > 0 ise aˣ asla negatif olamaz.',
 dict(A='−9, a² − 3a − 54’ü (a + 9) × (a − 6) diye yanlış ayırıp negatif kökü almak.',B='−6, denklemin öbür kökü; 3ˣ negatif olamaz.',C='2, x’in değeri; soru 3ˣ’i soruyor.',D='6, a² − 3a − 54’ü (a + 9) × (a − 6) diye yanlış ayırmak; çarpanların toplamı +3 olur, −3 değil.'),
 TT(A='islem',B='bilgi',C='dikkat',D='islem'))
kok=[a for a in range(-60,61) if 4*a*a-8*a==192]; assert sorted(kok)==[-6,8]
assert 4**4-2**6==192 and [x for x in range(-5,10) if 4**(x+1)-2**(x+3)==192]==[3]
assert sorted(a for a in range(-60,61) if 2*a*a-8*a==192)==[-8,12] and sorted(a for a in range(-60,61) if (a+8)*(a-6)==0)==[-8,6]
P.K('0007','4ˣ⁺¹ − 2ˣ⁺³ = 192\neşitliğine göre 2ˣ kaçtır?',
 ['−6','3','6','8','12'],'D','2ˣ ifadesinin değeri.',
 ['2ˣ = a de; 4ˣ⁺¹’i a cinsinden yaz.','Denklemi 4’e bölüp çarpanlarına ayır.','2ˣ negatif bir sayı olabilir mi?'],[KK,POZ,B('Değişken değiştirme','tekrar eden ifadeye harf ver: 2ˣ = a ise 4ˣ = (2²)ˣ = (2ˣ)² = a²')],
 [A('Harf ver','2ˣ = a olsun. 4ˣ⁺¹ = 4 × (2ˣ)², 2ˣ⁺³ = 8 × 2ˣ.','4ˣ⁺¹ = 4a² · 2ˣ⁺³ = 8a'),
  A('Denklemi kur','Denklemi 4’e böl.','4a² − 8a = 192 ⇒ a² − 2a − 48 = 0'),
  A('Çarpanlara ayır','Çarpımı −48, toplamı −2: −8 ve 6.','(a − 8) × (a + 6) = 0 ⇒ a = 8 ya da a = −6'),
  A('Pozitif kökü seç','2ˣ > 0 olduğundan a = 8.','2ˣ = 8 (x = 3) · kontrol: 4⁴ − 2⁶ = 256 − 64 = 192 ✓')],
 'Üslü denklemi harf vererek ikinci dereceye çevirdiğinde her kökü “aˣ bu değeri alabilir mi?” diye sına.',
 dict(A='−6, denklemin öbür kökü; 2ˣ negatif olamaz.',B='3, x’in değeri; soru 2ˣ’i soruyor.',C='6, a² − 2a − 48’i (a + 8) × (a − 6) diye yanlış ayırmak.',E='12, 4ˣ⁺¹’i 2²ˣ⁺¹ yazmak; (2²)ˣ⁺¹ = 2²ˣ⁺², yani 4a².'),
 TT(A='bilgi',B='dikkat',C='islem',E='islem'))

# ===== 0008 ZOR us-buyume (K-US-08)
t_=[t for t in range(0,40) if 2**4*4**t==8*2**10*2**t]; assert t_==[9]
assert [t for t in range(0,40) if 2**4*4**t==2**10*2**t]==[6] and [t for t in range(0,40) if 2**10*2**t==8*2**4*4**t]==[3] and [t for t in range(0,40) if 4+2*t==10+t+8]==[14]
P.R('0008','us-buyume','Katlanarak artma ve azalma','zor','Büyümelerin Karşılaştırılması','Farklı hızlarda katlanan iki niceliği aynı tabanda yazar, “k katı” koşulunu üs eşitliğine çevirir.','hikâyeli',4,
 'K-US-08 (iki farklı katlanma, “k katı” koşulu) · yeni kurgu (iki kapta bakteri), yeni istenen (süre)',
 'Bir laboratuvarda A kabında başlangıçta 2¹⁰ bakteri vardır ve bu kaptaki bakteri sayısı her saat 2 katına çıkmaktadır. B kabında başlangıçta 2⁴ bakteri vardır ve bu kaptaki bakteri sayısı her saat 4 katına çıkmaktadır.\nBuna göre kaç saat sonra B kabındaki bakteri sayısı A kabındakinin 8 katı olur?',
 ['3','6','9','13','14'],'C','B’nin A’nın 8 katı olduğu andaki süre (saat).',
 ['t saat sonra iki kaptaki sayıyı 2’nin kuvveti olarak yaz.','4ᵗ = (2²)ᵗ; “8 katı” = 2³ ile çarpmak.','Üsleri eşitle: hangi kap hangisinin 8 katı?'],[CRP,KK,B('Katlanarak artma','başlangıç sayısı N, her saat k katına çıkıyorsa t saat sonra N × kᵗ olur. Örnek: 2⁴ × 4ᵗ')],
 [A('A kabı','2¹⁰ ile başlar, her saat 2 katı.','A = 2¹⁰ × 2ᵗ = 2¹⁰⁺ᵗ'),
  A('B kabı','2⁴ ile başlar, her saat 4 = 2² katı.','B = 2⁴ × (2²)ᵗ = 2⁴⁺²ᵗ'),
  A('Koşulu yaz','B, A’nın 8 katı: 8 = 2³ olduğundan A’nın üssüne 3 eklenir.','2⁴⁺²ᵗ = 2³ × 2¹⁰⁺ᵗ = 2¹³⁺ᵗ'),
  A('Üsleri eşitle','Aynı tabanda üsler eşit olmalı.','4 + 2t = 13 + t ⇒ t = 9'),
  A('Kontrol','9 saat sonra A = 2¹⁹, B = 2²².','2²² ÷ 2¹⁹ = 2³ = 8 ✓')],
 '“k katı” koşulunda k’yı tabanın kuvveti olarak yaz (8 = 2³) ve üsse o kuvveti ekle; k’nın kendisini değil.',
 dict(A='3, koşulu ters kurmak (A, B’nin 8 katı); soru B’nin A’nın 8 katı olmasını soruyor.',B='6, iki kabın eşit olduğu an; soru 8 katı olmasını soruyor.',D='13, 3 + 10’u, yani A’nın üssündeki sabiti süre sanmak.',E='14, “8 katı” için üsse 8 eklemek; 8 = 2³ olduğundan üsse 3 eklenir.'),
 TT(A='dikkat',B='dikkat',D='dikkat',E='bilgi'))
t_=[t for t in range(0,40) if 3**2*9**t==3*3**8*3**t]; assert t_==[7]
assert [t for t in range(0,40) if 3**2*9**t==3**8*3**t]==[6] and [t for t in range(0,40) if 3**8*3**t==3*3**2*9**t]==[5] and [t for t in range(0,40) if 2+2*t==8+t+3]==[9]
P.K('0008','Bir araştırmada P kabında başlangıçta 3⁸ hücre vardır ve bu kaptaki hücre sayısı her gün 3 katına çıkmaktadır. R kabında başlangıçta 3² hücre vardır ve bu kaptaki hücre sayısı her gün 9 katına çıkmaktadır.\nBuna göre kaç gün sonra R kabındaki hücre sayısı P kabındakinin 3 katı olur?',
 ['5','6','7','8','9'],'C','R’nin P’nin 3 katı olduğu andaki süre (gün).',
 ['t gün sonra iki kaptaki sayıyı 3’ün kuvveti olarak yaz.','9ᵗ = (3²)ᵗ; “3 katı” üsse kaç ekler?','Üsleri eşitle; koşulun yönüne dikkat et.'],[CRP,KK,B('Katlanarak artma','başlangıç sayısı N, her gün k katına çıkıyorsa t gün sonra N × kᵗ olur. Örnek: 3² × 9ᵗ')],
 [A('P kabı','3⁸ ile başlar, her gün 3 katı.','P = 3⁸ × 3ᵗ = 3⁸⁺ᵗ'),
  A('R kabı','3² ile başlar, her gün 9 = 3² katı.','R = 3² × (3²)ᵗ = 3²⁺²ᵗ'),
  A('Koşulu yaz','R, P’nin 3 katı: üsse 1 eklenir.','3²⁺²ᵗ = 3 × 3⁸⁺ᵗ = 3⁹⁺ᵗ'),
  A('Üsleri eşitle','Aynı tabanda üsler eşit.','2 + 2t = 9 + t ⇒ t = 7'),
  A('Kontrol','7 gün sonra P = 3¹⁵, R = 3¹⁶.','3¹⁶ ÷ 3¹⁵ = 3 ✓')],
 'Katlanan iki niceliği aynı tabanda yazınca “kaç katı” sorusu üsler arasındaki fark sorusuna döner.',
 dict(A='5, koşulu ters kurmak (P, R’nin 3 katı).',B='6, iki kabın eşit olduğu an; soru 3 katı olmasını soruyor.',D='8, başlangıç gününü de sayıp bir fazla bulmak.',E='9, “3 katı” için üsse 3 eklemek; 3 = 3¹ olduğundan üsse 1 eklenir.'),
 TT(A='dikkat',B='dikkat',D='dikkat',E='bilgi'))

P.yaz(os.path.join(H,'uslu-1.json'),os.path.join(H,'uslu-1-kardes.json'))
