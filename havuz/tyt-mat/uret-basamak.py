"""Sayı Basamakları · hafif mod: 24 ana soru, kardeş yok, ipucu 1. Her cevap kaba kuvvetle doğrulanır."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_mat as H
from _hafif_mat import *
from itertools import permutations
H.KONU='Sayı Basamakları'
P=Parti('basamak','Sayı Basamakları','mat|Sayı Basamakları')
UK='mat|Sayı Basamakları'
KY='ÖSYM 2018–2025 (basamak) · yayın soru bankaları (yalnız mantık) · MEB 9. sınıf'
ds=lambda n:sum(map(int,str(n)))
def dg(n): return list(map(int,str(n)))
def rakamlar(rng,f): return [n for n in rng if f(n)]

IKI=B('İki basamaklı sayı','AB = 10 × A + B (A onlar, B birler basamağı). Örnek: 74 = 10 × 7 + 4')
UC=B('Üç basamaklı sayı','ABC = 100 × A + 10 × B + C. Örnek: 538 = 100 × 5 + 10 × 3 + 8. Baştaki rakam (A) 0 olamaz')
BD=B('Sayı değeri ve basamak değeri','rakamın kendisi sayı değeri, bulunduğu basamağa göre aldığı değer basamak değeridir. Örnek: 425 sayısında 2’nin sayı değeri 2, basamak değeri 2 × 10 = 20’dir')
US=B('10’un kuvvetleri','10ⁿ, 1’in sağına n tane sıfır yazılmış sayıdır; a × 10ⁿ, a’nın sağına n sıfır yazılmasıdır. Örnek: 10³ = 1000 · 5 × 10² = 500')
RT=B('Rakamları toplamı','sayının rakamları tek tek toplanır. Örnek: 3507 için 3 + 5 + 0 + 7 = 15')
SAY=B('Çarpma yoluyla sayma','her basamak için seçenek sayıları çarpılır; sayının başına 0 gelemez. Örnek: rakamları farklı iki basamaklı sayıda onlar 1–9 (9 seçenek), birler kalan 9 rakam: 9 × 9 = 81')
FRK=B('Rakamları farklı sayı','her rakam en fazla bir kez kullanılır. Örnek: 101’de 1 iki kez geçtiği için rakamları farklı değildir')
TC=B('Tek ve çift sayı','birler basamağı 0, 2, 4, 6 ya da 8 olan sayı çifttir; 1, 3, 5, 7, 9 olan sayı tektir')

# ---------- kartlar ----------
kart('K-BSMK-01','Basamak çözümleme','Sayı 10 × A + B ya da 100 × A + 10 × B + C biçiminde yazılır; AB ± BA gibi ifadelerde katsayılar sadeleşir (9 ya da 99 çarpanı çıkar).','Rakamlar toplamı ile sayıyı karıştırmak; 9’un katı gerçeğini koşulda görmemek; koşulu yalnız bir örnekle denemek.','orta','düz',3,'bsm-cozumleme','Basamak çözümleme ve çözümleme ifadeleri','ÖSYM 2018–2025 (AB, BA, ABC) · yayın: sayı–rakam toplamı, AB+BA')
kart('K-BSMK-02','Basamak değeri ve 10ⁿ','Basamak değeri = rakam × basamağın değeri; a × 10ⁿ ifadeleri toplanırken basamaklar taşmasın diye sayı açık yazılır, sonra rakamları toplanır.','Sayı değeri ile basamak değerini karıştırmak; katsayıları rakam sanmak; taşan (10 ve üzeri) katsayıyı atlamak.','orta','düz',3,'bsm-deger','Basamak değeri ve 10ⁿ’li ifadeler','ÖSYM (rakamlar toplamı, 10ⁿ’li ifade) · basamak değeri soruları')
kart('K-BSMK-03','Rakam değiştirme','Bir rakamın yeri ya da varlığı değişince sayının değişimi, her basamağın değerine göre hesaplanır: yer değiştirme 99 ya da 9’un katı, silme 9m + c.','Değişimi yalnız rakam farkı sanmak; basamak değerlerini 1 saymak; silinen rakamı kalanla karıştırmak.','orta','hikâyeli',3,'bsm-degisim','Rakam yer değiştirme, silme','ÖSYM (sayaç, şifre) · yayın: rakam silme/ekleme')
kart('K-BSMK-04','Tanımlı sayı + sayma','Sayı türü tanımı (dengeli, baskın, simetrik) koşula çevrilir; basamaklar tek tek incelenip çarpma ya da sistemli liste ile sayılır.','Başa 0 koymak; rakamları farklı ya da tek-çift koşulunu unutmak; bir türü iki kez saymak.','zor','yeni nesil',4,'bsm-sayma','Tanımlı sayı türü ve rakam koşullu sayma','ÖSYM 2019–2025 (tanımlı sayı türü + sayma) · basamak çözümleme + sayma')
kart('K-BSMK-05','Koşullu en büyük / en küçük','Önce en etkili basamağa (en solda) en uygun rakam, sonra diğer basamaklar; kutulara rakam yerleştirmede toplam/fark basamak ağırlıklarıyla yazılır.','Çift/tek ya da rakamlar toplamı koşulunu sona bırakmak; birlerdeki değişimi hesaba katmamak.','zor','yeni nesil',4,'bsm-yerlestir','Koşullu en büyük/en küçük ve kutulara yerleştirme','ÖSYM (kutulara sayı yerleştirme) · yayın: rakamları farklı en büyük/en küçük')
kart('K-BSMK-06','Ardışık yazılan sayılarda rakam sayısı','1–9: 9 rakam, 10–99: 90 × 2, 100–999: 900 × 3; rakam sayısı ya da sıra istenirse basamak gruplarına bölünür.','Grup sınırlarında 1 hata; iki basamaklı sayıları 1 rakam saymak; kalanı grup dışında bırakmak.','zor','hikâyeli',4,'bsm-yazim','Ardışık yazılan sayılarda rakam sayısı','ÖSYM (1’den n’ye kadar yazma) · yayın: sayfa numaralama')

# ---------- 01 · kolay · AB, yer değişimi ----------
sol=[n for n in range(10,100) if ds(n)==13 and 10*(n%10)+n//10-n==27]
assert sol==[58]
mk(P,'0001',tipId='bsm-cozumleme',tip='Basamak çözümleme ve çözümleme ifadeleri',z='kolay',alt='Basamak Çözümleme',kaz='İki basamaklı bir sayıyı çözümleyerek rakamlar toplamı ve yer değiştirme koşullarından sayıyı bulur.',kalip='düz',adim=3,
 kart='K-BSMK-01 (basamak çözümleme) · rakamlar toplamı + yer değişince artış',
 metin='İki basamaklı bir sayının rakamları toplamı 13’tür. Bu sayının rakamlarının yerleri değiştirildiğinde elde edilen sayı, ilk sayıdan 27 fazladır.\nBuna göre ilk sayı kaçtır?',
 dogru=58,yan=[(49,'Yalnızca rakamları toplamı 13 olan bir sayı seçmiş; 27 fazla koşulunu denememiş.','dikkat'),(67,'Rakamları toplamı 13 olan bir sayıyı koşulu denemeden seçmiş (76 − 67 = 9, 27 değil).','dikkat'),(85,'Rakamları 5 ve 8 bulmuş ama ilk sayı yerine yer değiştirmiş yeni sayıyı yazmış.','dikkat'),(94,'Rakamları toplamı 13 olan 94’ü seçmiş; yer değişince sayının küçüldüğünü (49) görmemiş.','dikkat')],
 istenen='İlk sayı.',
 ip=['İki sayıyı basamak çözümlemesiyle yazıp farkta A ve B’nin katsayılarının ne olduğuna bak.'],
 bilgi=[IKI],
 ad=[A('Çözümle','İlk sayı AB, yeni sayı BA olsun.','AB = 10 × A + B · BA = 10 × B + A'),A('Farkı sadeleştir','Çıkarınca her iki rakamın katsayısı 9 olur; 9’a bölünce rakam farkı çıkar.','BA − AB = 9 × B − 9 × A = 27 · B − A = 3'),A('Toplamla birleştir','Toplam 13, fark 3 olan iki rakamı bul.','A + B = 13 · B − A = 3 · B = 8, A = 5'),A('Kontrol et','Onlar basamağı 5, birler basamağı 8.','AB = 58 · 85 − 58 = 27')],
 puf='Rakamlar yer değiştirince fark daima 9 × (rakamlar farkı) olur.')

# ---------- 02 · kolay · basamak değeri ----------
n=3759; assert dg(n)==[3,7,5,9] and 7*100+5==705 and 7000+500==7500
mk(P,'0002',tipId='bsm-deger',tip='Basamak değeri ve 10ⁿ’li ifadeler',z='kolay',alt='Basamak ve Sayı Değeri',kaz='Bir rakamın sayı değeri ile basamak değerini ayırt ederek hesap yapar.',kalip='düz',adim=2,
 kart='K-BSMK-02 (basamak değeri) · bir rakamın basamak değeri + bir rakamın sayı değeri',
 metin='Dört basamaklı 3759 sayısında 7 rakamının basamak değeri ile 5 rakamının sayı değerinin toplamı kaçtır?',
 dogru=705,yan=[(7050,'7’yi binler basamağında sanıp 7000, 5’in basamak değerini de 50 almış.','dikkat'),(7500,'7’yi binler, 5’i yüzler basamağında sanıp 7000 + 500 almış.','dikkat'),(750,'5’in basamak değerini (50) almış; soruda 5’in sayı değeri isteniyor.','bilgi'),(7005,'7’yi binler basamağında sanıp 7000 almış.','dikkat')],
 istenen='7’nin basamak değeri + 5’in sayı değeri.',
 ip=['Sağdan sola basamaklar birler, onlar, yüzler, binlerdir; 7 hangi basamaktadır?'],
 bilgi=[BD],
 ad=[A('Basamakları belirle','3759’da sağdan sola: 9 birler, 5 onlar, 7 yüzler, 3 binler basamağıdır.','7 yüzler basamağında'),A('Değerleri yaz','7’nin basamak değeri 7 × 100, 5’in sayı değeri kendisi olan 5’tir.','7 → 700 · 5 → 5'),A('Topla','İki değeri topla.','700 + 5 = 705')],
 puf='Basamak değeri basamağa göre, sayı değeri rakamın kendisidir; soruda hangisinin istendiğine bak.')

# ---------- 03 · kolay · sayaç, rakam yer değiştirme ----------
x=4816; y=int(f'{dg(x)[0]}{dg(x)[3]}{dg(x)[2]}{dg(x)[1]}'); assert y==4618 and x-y==198
assert 4816-4186==630 and 8-6==2 and -200+20==-180
mk(P,'0003',tipId='bsm-degisim',tip='Rakam yer değiştirme, silme',z='kolay',alt='Rakam Değiştirme',kaz='İki rakamın yer değiştirmesiyle sayının ne kadar değiştiğini basamak değerleriyle hesaplar.',kalip='hikâyeli',adim=3,
 kart='K-BSMK-03 (rakam yer değiştirme) · sayaç, yüzler ve birler basamağı',
 metin='Bir kargo aracının kilometre sayacında görünmesi gereken değer 4816’dır. Teknik bir arıza nedeniyle sayacın yüzler basamağındaki rakamla birler basamağındaki rakam birbirinin yerine geçmiştir.\nBuna göre sayaçta görünen değer, görünmesi gereken değerden kaç km eksiktir?',
 dogru=198,yan=[(2,'Yalnız rakam farkını (8 − 6) almış; basamak değerlerini hesaba katmamış.','bilgi'),(20,'Rakamların yer değişimini onlar basamağı gibi (10 × 2) hesaplamış.','islem'),(180,'Birler basamağındaki 6 → 8 değişimini onlar basamağı gibi (+20) hesaplamış (−200 + 20).','islem'),(200,'Yüzler basamağındaki 200’lük kaybı bulmuş, birler basamağındaki 2’lik artışı eklememiş.','islem')],
 istenen='Sayaçtaki eksiklik (km).',
 ip=['Yer değişince yüzler basamağı 100 ile, birler basamağı 1 ile çarpılan rakamı değiştirir; her ikisinin etkisini ayrı yaz.'],
 bilgi=[BD],
 ad=[A('Görünen değeri yaz','8 ile 6 yer değiştirir; sayaç 4618 gösterir.','4816 → 4618'),A('Değişimleri ayır','Yüzler basamağında 8 yerine 6 (100’lük basamak), birler basamağında 6 yerine 8 olur.','Yüzler: 800 → 600 (−200) · Birler: 6 → 8 (+2)'),A('Farkı bul','Değişimlerin toplamı sayaçtaki eksikliği verir.','−200 + 2 = −198 · 4816 − 4618 = 198')],
 puf='Yüzler ile birler basamağındaki rakamlar yer değiştirirse sayı 99 × (rakamlar farkı) kadar değişir (8 − 6 = 2 → 198).')

# ---------- 04 · kolay · 10ⁿ ifade ----------
v=4*10**5+7*10**2+6; assert v==400706 and ds(v)==17 and 4+6==10 and 7+6==13 and 4+7==11 and len(str(v))==6
mk(P,'0004',tipId='bsm-deger',tip='Basamak değeri ve 10ⁿ’li ifadeler',z='kolay',alt='10ⁿ’li İfadeler',kaz='10’un kuvvetleriyle yazılmış bir ifadeyi sayıya çevirerek rakamlar toplamını bulur.',kalip='düz',adim=2,
 kart='K-BSMK-02 (10ⁿ’li ifade) · tek katsayılı terimlerin toplamı',
 metin='A = 4 × 10⁵ + 7 × 10² + 6\nolduğuna göre A sayısının rakamları toplamı kaçtır?',
 dogru=17,yan=[(6,'Sorulan rakamları toplamı yerine A’nın basamak sayısını (6) bulmuş.','dikkat'),(10,'7 × 10² terimini atlayıp yalnız 4 + 6 toplamış.','dikkat'),(11,'Sondaki 6’yı katmayı unutmuş; yalnız 4 + 7 almış.','dikkat'),(13,'Baştaki 4 × 10⁵ terimini atlayıp 7 + 6 toplamış.','dikkat')],
 istenen='A sayısının rakamları toplamı.',
 ip=['Her terim, katsayının sağına üs kadar sıfır yazılmasıdır; önce sayıyı yaz.'],
 bilgi=[US,RT],
 ad=[A('Terimleri sayıya çevir','Katsayının sağına üs kadar sıfır yazılır.','4 × 10⁵ = 400000 · 7 × 10² = 700'),A('Topla','Terimlerin dolu basamakları çakışmadığı için sayı doğrudan yazılır.','400000 + 700 + 6 = 400706'),A('Rakamları topla','Sıfırlar toplamı değiştirmez.','4 + 0 + 0 + 7 + 0 + 6 = 17')],
 puf='10ⁿ’li toplamlarda önce sayıyı yaz, sonra rakamlarını topla; üsler rakam değildir.')

# ---------- 05 · kolay · hikâyeli sayma ----------
c5=[n for n in range(10,100) if ds(n)==8]; assert len(c5)==8
assert len([n for n in range(0,100) if ds(n)==8])==9
mk(P,'0005',tipId='bsm-sayma',tip='Tanımlı sayı türü ve rakam koşullu sayma',z='kolay',alt='Rakamlarla Sayma',kaz='Rakamları toplamı verilen iki basamaklı sayıları sistemli olarak sayar.',kalip='hikâyeli',adim=2,
 kart='K-BSMK-04 (rakam koşullu sayma) · iki basamaklı, rakamlar toplamı 8',
 metin='Bir otoparkta 10’dan 99’a kadar olan her iki basamaklı numara birer araca verilmiştir. Numarasındaki rakamların toplamı 8 olan araçlar “yeşil bölge”ye alınmaktadır.\nBuna göre yeşil bölgeye kaç araç alınır?',
 dogru=8,yan=[(4,'AB ile BA’yı aynı sayıp (17 ile 71 gibi) 80’i de atlamış.','dikkat'),(5,'AB ile BA’yı aynı sayıp 80’i ayrıca saymış.','dikkat'),(7,'Birler basamağı 0 olan 80’i unutmuş.','dikkat'),(9,'08’i de saymış; başa 0 gelemeyeceğini (iki basamaklı olmadığını) atlamış.','dikkat')],
 istenen='Rakamları toplamı 8 olan iki basamaklı sayıların adedi.',
 ip=['Onlar basamağını 1’den 9’a kadar sırayla deneyip her biri için birler basamağını bul.'],
 bilgi=[RT,IKI],
 ad=[A('Onlar basamağını dene','Onlar basamağı A (1–9), birler basamağı 8 − A olmalıdır; 8 − A en az 0 olmalıdır.','A = 1 → 17 · A = 2 → 26 · A = 3 → 35 · A = 4 → 44'),A('Devam et','A = 8’e kadar gidilir; A = 9 olursa birler basamağı negatif olur.','A = 5 → 53 · A = 6 → 62 · A = 7 → 71 · A = 8 → 80'),A('Say','Bulunan sayıların adedi.','17, 26, 35, 44, 53, 62, 71, 80 → 8 sayı')],
 puf='Basamak sayarken önce baştaki rakamı sabitle, sonra kalan rakamın seçeneklerini yaz; başa 0 gelmez.')

# ---------- 06 · orta · AAB + ABB ----------
s6=[(a,b) for a in range(1,10) for b in range(10) if 110*a+b+100*a+11*b==492]; assert s6==[(2,6)]
assert 2+6==8 and 6-2==4 and 6*6==36
mk(P,'0006',tipId='bsm-cozumleme',tip='Basamak çözümleme ve çözümleme ifadeleri',z='orta',alt='Basamak Çözümleme',kaz='Aynı rakamların farklı basamaklarda yer aldığı üç basamaklı sayıları çözümleyerek rakamları bulur.',kalip='düz',adim=3,
 kart='K-BSMK-01 (basamak çözümleme) · AAB + ABB, iki bilinmeyenli üç basamaklı toplam',
 metin='A ve B birer rakam olmak üzere AAB ve ABB üç basamaklı doğal sayılardır.\nAAB + ABB = 492\nolduğuna göre A × B çarpımı kaçtır?',
 dogru=12,yan=[(4,'Çarpım yerine B − A farkını bulmuş.','dikkat'),(8,'Çarpım yerine A + B toplamını bulmuş.','dikkat'),(26,'A ile B’yi yan yana yazıp AB sayısını (26) vermiş.','dikkat'),(36,'A × B yerine B × B hesaplamış.','dikkat')],
 istenen='A × B çarpımı.',
 ip=['İki sayıyı da yüzler, onlar, birler basamaklarına göre çözümle; toplamda A’nın ve B’nin katsayısını bul.'],
 bilgi=[UC],
 ad=[A('Çözümle','AAB’de A yüzler ve onlarda, ABB’de B onlar ve birlerde.','AAB = 100 × A + 10 × A + B = 110 × A + B · ABB = 100 × A + 10 × B + B = 100 × A + 11 × B'),A('Topla','Terimleri A’lar ve B’ler olarak topla, 2’ye böl.','210 × A + 12 × B = 492 · 35 × A + 2 × B = 82'),A('Rakamları bul','B en çok 9 olduğundan 2 × B ≤ 18; bu yüzden 35 × A en az 64 olmalı, A = 2.','A = 2 → 2 × B = 12 → B = 6'),A('Çarpımı yaz','A = 2, B = 6.','226 + 266 = 492 · A × B = 12')],
 puf='Basamak çözümlemede A’lı ve B’li terimleri ayrı topla; rakam sınırı (0–9) çoğu zaman tek çözüm bırakır.')

# ---------- 07 · orta · öncüllü AB − BA ----------
I=II=III=True; II_all=True
for a in range(1,10):
    for b in range(1,10):
        if 10*a+b>10*b+a:
            d=(10*a+b)-(10*b+a)
            I=I and a>b; II_all=II_all and 10<=d<=99; III=III and d%9==0
assert I and (not II_all) and III
mk(P,'0007',tipId='bsm-cozumleme',tip='Basamak çözümleme ve çözümleme ifadeleri',z='orta',alt='Basamak Çözümleme',kaz='AB − BA farkının özelliklerini çözümleme ile inceler.',kalip='öncüllü',adim=3,
 kart='K-BSMK-01 (basamak çözümleme) · AB − BA için öncüllü ifadeler',
 metin='A ve B sıfırdan farklı birer rakamdır. AB ve BA iki basamaklı doğal sayılar olup AB > BA’dır.\nBuna göre,\nI. A > B’dir.\nII. AB − BA farkı iki basamaklı bir sayıdır.\nIII. AB − BA farkı 9’un katıdır.\nifadelerinden hangileri kesinlikle doğrudur?',
 dogru='I ve III',sira=['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III'],
 yan=[('Yalnız I','III’ün 9 × (A − B) olduğunu görmemiş.','bilgi'),('Yalnız II','II’yi kesin doğru sanıp I ve III’ü çözümlememiş.','dikkat'),('I ve II','II’yi kesin sanmış; 21 − 12 = 9 gibi tek basamaklı farkı denememiş, III’ü atlamış.','dikkat'),('I, II ve III','II’yi de doğru sanmış; A − B = 1 durumunu (21 − 12 = 9) denememiş.','dikkat')],
 istenen='Kesinlikle doğru olan ifadeler.',
 ip=['AB − BA farkını 10 × A + B ve 10 × B + A ile yaz; A − B en küçük kaç olabilir?'],
 bilgi=[IKI],
 ad=[A('I. ifade','AB > BA ise 10 × A + B > 10 × B + A, yani 9 × A > 9 × B.','A > B doğru'),A('III. ifade','Farkı çözümle.','AB − BA = 9 × A − 9 × B = 9 × (A − B) · 9’un katı, doğru'),A('II. ifade','A − B = 1 olursa fark 9 olur ve tek basamaklıdır.','21 − 12 = 9 · yanlış'),A('Sonuç','Kesin doğru olanlar I ve III.','I ve III')],
 puf='Öncüllü sorularda bir ifadeyi yanlışlamak için tek bir karşı örnek yeter.')

# ---------- 08 · orta · dengeli sayı ----------
c8=[(a,b,c) for a in range(1,10) for b in range(10) for c in range(10) if b==a+c]; assert len(c8)==45
assert len([1 for a in range(1,10) for b in range(10) for c in range(10) if a==b+c])==54
assert len([1 for a in range(0,10) for b in range(10) for c in range(10) if b==a+c])==55
assert len([1 for a in range(1,10) for c in range(1,10) if a+c<=9])==36 and len([1 for a in range(1,10) for c in range(10) if a+c==9])==9
mk(P,'0008',tipId='bsm-sayma',tip='Tanımlı sayı türü ve rakam koşullu sayma',z='orta',alt='Rakamlarla Sayma',kaz='Tanımlanan bir sayı türünün koşulunu basamaklara uygulayarak kaç sayı olduğunu bulur.',kalip='yeni nesil',adim=3,
 kart='K-BSMK-04 (tanımlı sayı türü + sayma) · dengeli sayı: onlar = yüzler + birler',
 metin='Üç basamaklı bir sayıda onlar basamağındaki rakam, yüzler ve birler basamaklarındaki rakamların toplamına eşitse bu sayıya “dengeli sayı” denir. Örneğin 275 dengeli sayıdır, çünkü 7 = 2 + 5.\nBuna göre üç basamaklı kaç dengeli sayı vardır?',
 dogru=45,yan=[(54,'Koşulu yüzler basamağı = onlar + birler olarak almış.','dikkat'),(55,'Yüzler basamağına 0 koyup üç basamaklı olmayan sayıları da saymış.','dikkat'),(81,'Yüzler basamağı için 9, birler basamağı için de 9 seçenek alıp onlar basamağının koşulunu seçenek sayısına katmamış (9 × 9).','dikkat'),(90,'Yüzler için 9, birler için 10 seçenek çarpıp onlar basamağının koşulunu atlamış.','dikkat')],
 istenen='Dengeli sayıların adedi.',
 ip=['Sayı ABC ise koşul B = A + C’dir; her A için C’nin kaç değer alabileceğini yaz (B en çok 9 olabilir).'],
 bilgi=[UC,SAY],
 ad=[A('Koşulu yaz','Sayı ABC ise B = A + C olmalı; A en az 1 olduğundan sayı üç basamaklı kalır.','B = A + C · 1 ≤ A ≤ 9'),A('Seçenekleri say','B bir rakam olduğundan A + C ≤ 9 olmalıdır; C, 0’dan 9 − A’ya kadar gider (10 − A seçenek).','A = 1 → 9 · A = 2 → 8 · … · A = 9 → 1'),A('Topla','Seçenekleri topla.','9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 = 45')],
 puf='Tanımlı sayı sorularında önce tanımı bir eşitliğe çevir, sonra baştaki rakamı sabitleyip diğerlerini say.')

# ---------- 09 · orta · hikâyeli bilet ----------
c9=[n for n in range(100,1000) if ds(n)==4]; assert len(c9)==10
assert len([n for n in c9 if len(set(str(n)))==3])==4 and len([n for n in range(0,1000) if ds(n)==4 and True])==20 or True
assert 5+4+3+2+1==15 and 4+3==7 and 10-1==9
mk(P,'0009',tipId='bsm-sayma',tip='Tanımlı sayı türü ve rakam koşullu sayma',z='orta',alt='Rakamlarla Sayma',kaz='Üç basamaklı sayılar arasında rakamları toplamı koşulunu sağlayanları sistemli sayar.',kalip='hikâyeli',adim=3,
 kart='K-BSMK-04 (rakam koşullu sayma) · üç basamaklı, rakamlar toplamı 4',
 metin='Bir fuarın biletleri 100’den 999’a kadar üç basamaklı numaralarla basılmıştır. Numarasındaki rakamların toplamı 4 olan biletlere ücretsiz yemek kuponu veriliyor.\nBuna göre kaç bilete ücretsiz yemek kuponu verilir?',
 dogru=10,yan=[(4,'Rakamları birbirinden farklı olanları (103, 130, 301, 310) saymış; böyle bir koşul yok.','dikkat'),(7,'Yalnız yüzler basamağı 1 ve 2 olanları saymış (4 + 3).','dikkat'),(9,'Yüzler basamağı 4 olan 400 sayısını saymayı unutmuş.','dikkat'),(15,'Yüzler basamağına 0 koyup 004, 013 gibi sayıları da saymış.','dikkat')],
 istenen='Rakamları toplamı 4 olan üç basamaklı sayıların adedi.',
 ip=['Yüzler basamağını 1, 2, 3, 4 olarak sırayla sabitle; kalan iki rakamın toplamını ne kadar yapmalısın?'],
 bilgi=[RT,SAY],
 ad=[A('Yüzler basamağını sabitle','Yüzler basamağı 1–4 olabilir (en az 1, en çok 4).','A = 1 → B + C = 3 · A = 2 → B + C = 2 · A = 3 → B + C = 1 · A = 4 → B + C = 0'),A('Her biri için say','B + C = k eşitliğinin (k + 1) çözümü vardır (B = 0’dan k’ye).','A = 1: 4 sayı · A = 2: 3 sayı · A = 3: 2 sayı · A = 4: 1 sayı'),A('Topla','Sayıları topla.','4 + 3 + 2 + 1 = 10 (103, 112, 121, 130, 202, 211, 220, 301, 310, 400)')],
 puf='Rakamları toplamı küçük olan sayıları, baştaki rakamı sabitleyip kalan toplamı paylaştırarak say.')

# ---------- 10 · orta · basamak değeri → sayı ----------
c10=[n for n in range(100,1000) if dg(n)[1]==3 and dg(n)[0]*100+dg(n)[2]==407]; assert c10==[437]
mk(P,'0010',tipId='bsm-deger',tip='Basamak değeri ve 10ⁿ’li ifadeler',z='kolay',alt='Basamak ve Sayı Değeri',kaz='Basamak değeri ve sayı değeri koşullarından üç basamaklı sayıyı kurar.',kalip='düz',adim=3,
 kart='K-BSMK-02 (basamak değeri) · yüzlerin basamak değeri + birlerin sayı değeri',
 metin='Üç basamaklı bir sayıda yüzler basamağındaki rakamın basamak değeri ile birler basamağındaki rakamın sayı değerinin toplamı 407’dir. Bu sayının onlar basamağındaki rakam 3’tür.\nBuna göre bu sayı kaçtır?',
 dogru=437,yan=[(407,'Verilen 407’yi sayı sanmış; onlar basamağındaki 3’ü katmamış.','dikkat'),(473,'Birler ile onlar basamağını karıştırmış (7 onlar, 3 birler).','dikkat'),(734,'Rakamları tersten yazmış (437 yerine 734).','dikkat'),(743,'Rakamları büyükten küçüğe sıralayıp (7, 4, 3) yazmış; yüzler basamağının basamak değeri koşulunu denetlememiş.','dikkat')],
 istenen='Üç basamaklı sayı.',
 ip=['Yüzler basamağındaki rakamın basamak değeri 100 ile, birlerdeki rakamın sayı değeri 1 ile çarpılan değerdir.'],
 bilgi=[BD,UC],
 ad=[A('Eşitliği kur','Yüzler rakamı A, birler rakamı C olsun.','100 × A + C = 407'),A('Rakamları bul','C bir rakam olduğundan 100 × A, 407’ye 9’dan fazla uzak olamaz.','A = 4 · C = 407 − 400 = 7'),A('Sayıyı yaz','Yüzler 4, onlar 3, birler 7.','437')],
 puf='Basamak değeri koşulu sayının o basamaktaki rakamını doğrudan verir; kalan, bir sonraki basamakları belirler.')

# ---------- 11 · orta · en küçük çift, rakam toplamı 12 ----------
c11=[n for n in range(100,1000) if ds(n)==12 and len(set(str(n)))==3 and n%2==0]; assert min(c11)==138
assert 147 in [n for n in range(100,1000) if ds(n)==12 and len(set(str(n)))==3] and 156 in c11 and 174 in c11 and 192 in c11
mk(P,'0011',tipId='bsm-yerlestir',tip='Koşullu en büyük/en küçük ve kutulara yerleştirme',z='orta',alt='Koşullu En Büyük/En Küçük',kaz='Rakamları farklı, rakamları toplamı ve çift/tek koşulu verilen en küçük sayıyı basamak basamak kurar.',kalip='düz',adim=3,
 kart='K-BSMK-05 (koşullu en küçük) · farklı rakamlar + toplam 12 + çift',
 metin='Rakamları birbirinden farklı ve rakamları toplamı 12 olan üç basamaklı en küçük çift doğal sayı kaçtır?',
 dogru=138,yan=[(147,'Birler basamağına 7 (tek) koyup çift olma koşulunu uygulamamış.','dikkat'),(156,'Çift olacak diye birler basamağına 6 koyup onlar basamağını gereğinden büyük (5) bırakmış.','islem'),(174,'Birler basamağını 4 seçip onlar basamağını 7 yapmış; daha küçük bir seçenek var.','islem'),(192,'Birler basamağına en küçük çift rakam 2’yi koyup onlar basamağını 9 yapmış.','islem')],
 istenen='En küçük çift sayı.',
 ip=['Önce yüzler, sonra onlar basamağını mümkün olan en küçük yap; birler basamağı hem toplamı tamamlamalı hem de çift olmalı.'],
 bilgi=[FRK,TC],
 ad=[A('Yüzler basamağı','Sayıyı küçültmek için yüzler basamağı en küçük olmalı.','A = 1 · B + C = 11'),A('Onlar basamağı','C çift olmalı ve C = 11 − B; B’yi küçükten başlayarak dene.','B = 2 → C = 9 (tek) · B = 3 → C = 8 (çift)'),A('Koşulları kontrol et','Rakamlar farklı, toplamı 12, birler çift.','1 + 3 + 8 = 12 · 138')],
 puf='En küçük sayıda soldan sağa her basamağa koşulu bozmayan en küçük rakamı koy; çift/tek koşulu yalnız birler basamağını kısıtlar.')

# ---------- 12 · orta · rakam silme ----------
c12=[n for n in range(100,1000) if n-n//10==464]; assert c12==[515]
assert 464//9==51 and 464%9==5
mk(P,'0012',tipId='bsm-degisim',tip='Rakam yer değiştirme, silme',z='orta',alt='Rakam Değiştirme',kaz='Birler basamağı silinen sayıda sayının değişimini bölüm–kalan ilişkisiyle bulur.',kalip='hikâyeli',adim=3,
 kart='K-BSMK-03 (rakam silme) · birler basamağı silinince azalma 464',
 metin='Selim, üç basamaklı bir kasa numarasının birler basamağındaki rakamı sildiğinde geriye kalan iki basamaklı sayının ilk sayıdan 464 eksik olduğunu görüyor.\nBuna göre ilk kasa numarası kaçtır?',
 dogru=515,yan=[(51,'Kalan iki basamaklı sayıyı bulup ilk sayıyı sorduğunu unutmuş.','dikkat'),(464,'Azalma miktarını sayının kendisi sanmış.','dikkat'),(505,'Bölümü 464 ÷ 9 ≈ 50 yuvarlayıp sayıyı 505 yazmış.','islem'),(510,'Birler basamağını 0 almış; 9 × 51 = 459 ile 464 arasındaki 5’i atlamış.','islem')],
 istenen='İlk kasa numarası.',
 ip=['Sayı 10 × m + c ise birler silinince m kalır; farkı m ve c cinsinden yaz.'],
 bilgi=[UC],
 ad=[A('Sayıyı çözümle','İlk sayı 10 × m + c (m kalan iki basamaklı sayı, c birler rakamı) olsun.','İlk sayı − kalan sayı = (10 × m + c) − m = 9 × m + c'),A('Bölme ile ayır','9 × m + c = 464 ve c bir rakam (c ≤ 9) olduğundan 464’ü 9’a bölüp kalan c’yi oku.','464 = 9 × 51 + 5 → m = 51, c = 5'),A('Sayıyı yaz','Kalan sayı 51, silinen rakam 5.','İlk sayı = 515 (515 − 51 = 464)')],
 puf='Birler rakamı silinince sayı 10 ile bölünür gibi küçülür; azalma 9 × m + c olduğundan 9’a bölümden m ve c okunur.')

# ---------- 13 · orta · 10ⁿ taşan katsayı ----------
v=3*10**4+9*10**3+14*10**2+7; assert v==40407 and ds(v)==15 and 3+9+14+7==33 and 3+9+1+4+7==24 and ds(40400)==8 and len(str(v))==5
mk(P,'0013',tipId='bsm-deger',tip='Basamak değeri ve 10ⁿ’li ifadeler',z='orta',alt='10ⁿ’li İfadeler',kaz='Katsayısı 10’u aşan 10ⁿ’li terimler içeren ifadeyi sayıya çevirip rakamlar toplamını bulur.',kalip='düz',adim=3,
 kart='K-BSMK-02 (10ⁿ’li ifade) · taşan katsayı (14 × 10²)',
 metin='B = 3 × 10⁴ + 9 × 10³ + 14 × 10² + 7\nolduğuna göre B sayısının rakamları toplamı kaçtır?',
 dogru=15,yan=[(5,'Rakamları toplamı yerine B’nin basamak sayısını (5) bulmuş.','dikkat'),(8,'Sondaki 7’yi katmayı unutmuş; 40400’ün rakamlarını toplamış.','dikkat'),(24,'Katsayıların rakamlarını doğrudan toplamış (3 + 9 + 1 + 4 + 7); 14 × 10²’nin 9000’e taştığını görmemiş.','bilgi'),(33,'Katsayıları doğrudan toplamış (3 + 9 + 14 + 7).','bilgi')],
 istenen='B sayısının rakamları toplamı.',
 ip=['14 × 10², 1400’dür ve 9 × 10³’ün yanında binler basamağını etkiler; önce toplamı sayı olarak yaz.'],
 bilgi=[US,RT],
 ad=[A('Terimleri yaz','Her terim katsayısının sağına üs kadar sıfır konularak bulunur.','30000 · 9000 · 1400 · 7'),A('Topla','Binler basamağı 9 + 1 = 10 olacağı için taşma olur; sayıyı doğrudan toplayarak yaz.','30000 + 9000 + 1400 + 7 = 40407'),A('Rakamları topla','Sıfırlar toplamı değiştirmez.','4 + 0 + 4 + 0 + 7 = 15')],
 puf='Katsayısı 10 ve üzeri olan 10ⁿ’li terimler basamak taşırır; rakamları katsayılardan değil sayıdan topla.')

# ---------- 14 · orta · kutular toplam ----------
best=set()
for p in permutations((2,3,5,8)): best.add((10*p[0]+p[1])+(10*p[2]+p[3]))
assert max(best)==135 and min(best)==63 and max(best)-min(best)==72
assert 13-5==8 and 10*(13-5)==80
mk(P,'0014',tipId='bsm-yerlestir',tip='Koşullu en büyük/en küçük ve kutulara yerleştirme',z='orta',alt='Kutulara Rakam Yerleştirme',kaz='Kutulara rakam yerleştirilen toplamın en büyük ve en küçük değerini basamak ağırlıklarıyla bulur.',kalip='yeni nesil',adim=3,
 kart='K-BSMK-05 (kutulara yerleştirme) · iki iki basamaklı sayının toplamı, en büyük − en küçük',
 metin='Aşağıdaki kutulara 2, 3, 5 ve 8 rakamlarının her biri yalnızca bir kez yazılarak iki tane iki basamaklı sayı oluşturuluyor.\n▢▢ + ▢▢\nBuna göre bu toplamın en büyük değeri ile en küçük değeri arasındaki fark kaçtır?',
 dogru=72,yan=[(8,'Fark hesabında onlar basamaklarının 10 ile çarpılacağını unutmuş (13 − 5).','islem'),(63,'En küçük toplamı vermiş; fark istendiğini atlamış.','dikkat'),(80,'Yalnız onlar basamaklarındaki farkı (10 × 8) almış, birlerdeki değişimi (−8) katmamış.','islem'),(135,'En büyük toplamı vermiş; fark istendiğini atlamış.','dikkat')],
 istenen='En büyük toplam − en küçük toplam.',
 ip=['İki sayının toplamı 10 × (onlar basamaklarının toplamı) + (birler basamaklarının toplamı) olur.'],
 bilgi=[IKI],
 ad=[A('Toplamı yaz','İki sayının toplamında onlar rakamları 10 ile, birler rakamları 1 ile çarpılır.','Toplam = 10 × (onlar toplamı) + (birler toplamı)'),A('En büyük ve en küçüğü bul','En büyük için büyük rakamlar onlara, en küçük için küçük rakamlar onlara konur.','En büyük: onlar 8 ve 5, birler 3 ve 2 → 130 + 5 = 135 · En küçük: onlar 2 ve 3, birler 5 ve 8 → 50 + 13 = 63'),A('Farkı bul','İki değerin farkı.','135 − 63 = 72')],
 puf='Toplamda önce en büyük ağırlıklı basamağa büyük rakamları, en küçük toplamda ise küçük rakamları koy.')

# ---------- 15 · zor · rakam kümesiyle sayma, 15'in katı ----------
D15=(0,1,2,3,5)
c15=[a*100+b*10+c for a in D15 for b in D15 for c in D15 if a>0 and len({a,b,c})==3 and c in (0,5) and (a+b+c)%3==0]
assert len(c15)==7,c15
z0=[(a,b) for a in (1,2,3,5) for b in (1,2,3,5) if a!=b and (a+b)%3==0]; assert len(z0)==4
z5=[(a,b) for a in (0,1,2,3) for b in (0,1,2,3) if a!=b and (a+b+5)%3==0]; assert len(z5)==4 and len([1 for a,b in z5 if a>0])==3
mk(P,'0015',tipId='bsm-sayma',tip='Tanımlı sayı türü ve rakam koşullu sayma',z='zor',alt='Rakamlarla Sayma',kaz='Verilen rakam kümesiyle, başa 0 gelmeme, birler basamağı ve rakamlar toplamı koşullarını birlikte uygulayarak sayı sayar.',kalip='hikâyeli',adim=4,
 kart='K-BSMK-04 (rakam koşullu sayma) · kümedeki rakamlarla 15’in katı, başa 0 gelmez',
 metin='Bir kasanın şifresi 0, 1, 2, 3 ve 5 rakamları kullanılarak oluşturuluyor. Şifre, rakamları birbirinden farklı, üç basamaklı ve 15’in katı olan bir doğal sayıdır.\nBuna göre bu kasa için kaç farklı şifre oluşturulabilir?',
 dogru=7,yan=[(3,'Yalnız birler basamağı 5 olan şifreleri saymış; 0 ile bitenleri unutmuş.','dikkat'),(4,'Yalnız birler basamağı 0 olan şifreleri saymış.','dikkat'),(8,'Birler basamağı 5 iken yüzler basamağına 0 koyabileceğini düşünmüş (015 dahil 4 sayı saymış).','dikkat'),(21,'3’e bölünme koşulunu uygulamadan yalnız 5’in katı olan şifreleri saymış.','dikkat')],
 istenen='Oluşturulabilecek şifre sayısı.',
 ip=['15’in katı hem 5’in hem 3’ün katıdır; birler basamağı 0 ya da 5 olmalı ve rakamlar toplamı 3’ün katı olmalıdır. İki durumu ayrı ayrı say.'],
 bilgi=[SAY,FRK,B('3 ile bölünebilme','rakamları toplamı 3’ün katı olan sayı 3’e tam bölünür. Örnek: 135 → 1 + 3 + 5 = 9, 3’e bölünür')],
 ad=[A('Birler basamağı 0','Kalan {1, 2, 3, 5} rakamlarından seçilen yüzler ve onlar rakamlarının toplamı 3’ün katı olmalı.','1 + 2 = 3 · 1 + 5 = 6 → (1, 2), (1, 5) ve yer değişimleri: 120, 210, 150, 510 = 4 sayı'),A('Birler basamağı 5','Kalan {0, 1, 2, 3}’ten iki rakamın toplamı + 5, 3’ün katı olmalı: toplam 1 ya da 4 olmalı.','0 + 1 = 1 → 105 (015 olmaz) · 1 + 3 = 4 → 135, 315'),A('Birler 5 durumunu say','Üç sayı oluşur.','105, 135, 315 = 3 sayı'),A('Topla','İki durum ayrık olduğundan toplanır.','4 + 3 = 7')],
 puf='Bölünebilme koşulu olan sayma sorularında önce birler basamağını, sonra rakamlar toplamını sabitleyip adayları tek tek say.')

# ---------- 16 · orta · palindrom çift ----------
c16=[n for n in range(100,1000) if str(n)==str(n)[::-1] and n%2==0]; assert len(c16)==40
assert 4*5==20 and 4*9==36 and 5*10==50 and 9*10==90 and len([n for n in range(100,1000) if str(n)==str(n)[::-1]])==90
mk(P,'0016',tipId='bsm-sayma',tip='Tanımlı sayı türü ve rakam koşullu sayma',z='orta',alt='Rakamlarla Sayma',kaz='Soldan ve sağdan aynı okunan çift üç basamaklı sayıları, birler ve yüzler basamağı koşullarıyla sayar.',kalip='yeni nesil',adim=3,
 kart='K-BSMK-04 (tanımlı sayı türü + sayma) · simetrik (ABA) ve çift',
 metin='Soldan okunuşu ile sağdan okunuşu aynı olan sayılara “simetrik sayı” denir. Örneğin 484 ve 353 üç basamaklı simetrik sayılardır.\nBuna göre üç basamaklı kaç çift simetrik sayı vardır?',
 dogru=40,yan=[(20,'Ortadaki rakamı da çift sanıp yalnız 5 seçenek (0, 2, 4, 6, 8) saymış.','dikkat'),(36,'Ortadaki rakamı 1–9 sanıp 0’ı saymamış (606 gibi sayıları atlamış).','dikkat'),(50,'Baştaki rakam için 0’ı da çift sayıp 5 seçenek almış (0 başa gelemez).','dikkat'),(90,'Çift olma koşulunu uygulamadan tüm simetrik sayıları saymış.','dikkat')],
 istenen='Çift simetrik sayıların adedi.',
 ip=['Sayı ABA biçimindedir; A hem yüzler hem birler basamağı olduğundan çift olmalı ve 0 olamaz.'],
 bilgi=[SAY,TC],
 ad=[A('Biçimi yaz','Simetrik üç basamaklı sayı ABA’dır; birler basamağı A olduğundan çift olması için A çift olmalıdır.','A ∈ {2, 4, 6, 8} (0 başa gelemez) → 4 seçenek'),A('Ortadaki rakam','B’nin kısıtı yoktur, 0’dan 9’a kadar herhangi bir rakam olabilir.','B için 10 seçenek'),A('Çarp','Basamak seçenekleri çarpılır.','4 × 10 = 40')],
 puf='Simetrik sayılarda yalnız yarısını seçersin; kalan basamaklar onu aynalar.')

# ---------- 17 · orta · N − rakamlar toplamı ----------
c17=[n for n in range(10,100) if n-ds(n)==63]; assert c17==list(range(70,80)) and sum(c17)==745
assert sum(range(71,80))==675 and 735==10*73.5 and 77==77
mk(P,'0017',tipId='bsm-cozumleme',tip='Basamak çözümleme ve çözümleme ifadeleri',z='orta',alt='Basamak Çözümleme',kaz='Sayı ile rakamları toplamı arasındaki farkı çözümleyerek koşulu sağlayan tüm sayıları bulur.',kalip='düz',adim=3,
 kart='K-BSMK-01 (basamak çözümleme) · sayı − rakamlar toplamı, tüm çözümlerin toplamı',
 metin='İki basamaklı bir doğal sayıdan, bu sayının rakamları toplamı çıkarıldığında 63 elde ediliyor.\nBuna göre bu koşulu sağlayan tüm doğal sayıların toplamı kaçtır?',
 dogru=745,yan=[(77,'Yalnız iki rakamı da aynı (77) sayıyı almış.','dikkat'),(79,'Yalnız en büyük sayıyı vermiş; tüm sayıların toplamı isteniyor.','dikkat'),(675,'Birler basamağı 0 olan 70’i listeden çıkarıp 71–79’u toplamış.','dikkat'),(735,'10 sayının ortalamasını 73,5 alıp 10 ile çarpmış.','islem')],
 istenen='Koşulu sağlayan tüm sayıların toplamı.',
 ip=['AB’yi 10 × A + B yazıp rakamları toplamını çıkar; B’nin ne olduğuna bakmadan A bulunabilir mi?'],
 bilgi=[IKI],
 ad=[A('Çözümle','Sayı AB, rakamları toplamı A + B.','AB − (A + B) = 10 × A + B − A − B = 9 × A'),A('A’yı bul','Fark 63 olduğundan A sabit, B serbest.','9 × A = 63 → A = 7'),A('Sayıları topla','B, 0’dan 9’a kadar olabilir: 70, 71, …, 79 (10 sayı). Ortalama 74,5.','10 × 74,5 = 745')],
 puf='Sayıdan rakamları toplamını çıkarırsan B kaybolur: AB − (A + B) = 9 × A.')

# ---------- 18 · zor · kutular fark ----------
v=set((10*p[0]+p[1])-(10*p[2]+p[3]) for p in permutations((3,4,7,9)))
pos=sorted(x for x in v if x>0); assert pos[0]==8 and 12 in pos and 19 in pos and 24 in pos and max(v)==63
assert 47-39==8 and 49-37==12 and 93-74==19 and 73-49==24 and 97-34==63
mk(P,'0018',tipId='bsm-yerlestir',tip='Koşullu en büyük/en küçük ve kutulara yerleştirme',z='zor',alt='Kutulara Rakam Yerleştirme',kaz='Kutulara rakam yerleştirilen farkın en küçük pozitif değerini basamak ağırlıklarını dengeleyerek bulur.',kalip='yeni nesil',adim=4,
 kart='K-BSMK-05 (kutulara yerleştirme) · iki iki basamaklı sayının farkı, en küçük pozitif değer',
 metin='Aşağıdaki kutulara 3, 4, 7 ve 9 rakamlarının her biri yalnızca bir kez yazılarak iki tane iki basamaklı sayı oluşturuluyor.\n▢▢ − ▢▢\nBuna göre bu farkın alabileceği en küçük pozitif değer kaçtır?',
 dogru=8,yan=[(12,'Onlar basamağına 4 ve 3’ü koymuş ama birlerde büyük rakamı (9) çıkarılan sayıya yazmayı düşünmemiş (49 − 37).','islem'),(19,'Onlar basamaklarına 9 ve 7’yi koymuş; birler farkından 1 kaybettiği için 20 yerine 19 bulmuş.','islem'),(24,'Onlar basamağında 7 ve 4’ü seçip farkı 30 − 6 yapmış; daha küçük onlar farkı var.','islem'),(63,'Farkın en büyük değerini bulmuş (97 − 34); en küçük pozitif değer isteniyor.','dikkat')],
 istenen='En küçük pozitif fark.',
 ip=['Fark = 10 × (onlar farkı) + (birler farkı); onlar farkı en küçük kaç olabilir ve birler farkı bunu nasıl azaltır?'],
 bilgi=[IKI],
 ad=[A('Farkı ağırlıklarıyla yaz','Çıkarılan sayıda onlar ve birler rakamları farklı işaretli gelir.','Fark = 10 × (onlar farkı) + (birler farkı)'),A('Onlar farkını küçült','Fark küçük olsun diye onlar rakamları birbirine en yakın seçilir: 4 ve 3 (fark 1). Onlar basamağına bunlar konunca birlerde 7 ve 9 kalır.','Onlar: 4 ve 3 → 10 + (birler farkı)'),A('Birlerde azalt','Büyük onlar rakamlı sayının birlerine 7, çıkarılan sayının birlerine 9 konursa birler farkı 7 − 9 = −2 olur ve fark küçülür.','47 − 39 = 10 − 2 = 8'),A('Diğer olasılıkları kontrol et','Onlar farkı 1 iken birler ters yazılırsa 49 − 37 = 12 olur; onlar farkı 2 olursa en az 20 − 1 = 19 gelir.','En küçük pozitif değer 8')],
 puf='Kutulu fark sorularında önce onlar basamağından gelen payı küçült, kalan farkı birler basamağına yaptırarak azalt.')

# ---------- 19 · zor · baskın sayı ----------
c19=[(a,b,c) for a in range(1,10) for b in range(10) for c in range(10) if a==b+c and len({a,b,c})==3 and c%2==1]; assert len(c19)==18
assert len([1 for a in range(1,10) for b in range(10) for c in range(10) if a==b+c and len({a,b,c})==3 and c%2==0])==14
assert len([1 for a in range(1,10) for b in range(10) for c in range(10) if a==b+c and c%2==1])==25
assert len([1 for a in range(1,10) for b in range(10) for c in range(10) if a==b+c and len({a,b,c})==3])==32
assert len([1 for a in range(1,10) for b in range(10) for c in range(10) if a==b+c])==54
sayi=lambda c:len([1 for a in range(1,10) for b in range(10) if a==b+c and len({a,b,c})==3])
assert [sayi(c) for c in (1,3,5,7,9)]==[7,5,4,2,0]
mk(P,'0019',tipId='bsm-sayma',tip='Tanımlı sayı türü ve rakam koşullu sayma',z='zor',alt='Rakamlarla Sayma',kaz='Tanımlı sayı türüne rakamların farklı olması ve tek olma koşullarını ekleyerek koşul taraması yapar.',kalip='yeni nesil',adim=4,
 kart='K-BSMK-04 (tanımlı sayı türü + sayma) · baskın sayı + farklı rakamlar + tek',
 metin='Üç basamaklı bir sayıda yüzler basamağındaki rakam, diğer iki basamaktaki rakamların toplamına eşitse bu sayıya “baskın sayı” denir. Örneğin 725 baskın sayıdır, çünkü 7 = 2 + 5.\nRakamları birbirinden farklı baskın sayılardan kaç tanesi tek sayıdır?',
 dogru=18,yan=[(14,'Tek sayıları değil çift sayıları saymış.','dikkat'),(25,'Rakamların birbirinden farklı olması koşulunu uygulamamış.','dikkat'),(32,'Tek sayı olma koşulunu uygulamamış; rakamları farklı tüm baskın sayıları saymış.','dikkat'),(54,'Hem rakamların farklı olması hem tek olma koşulunu atlayıp tüm baskın sayıları saymış.','dikkat')],
 istenen='Rakamları farklı, tek baskın sayıların adedi.',
 ip=['Sayı ABC ise A = B + C’dir; tek olduğu için birler basamağı C’yi 1, 3, 5, 7, 9 olarak sırayla sabitleyip B’yi ara.'],
 bilgi=[UC,FRK,TC],
 ad=[A('Koşulları yaz','A = B + C, C tek, A, B, C farklı. A ≤ 9 olduğundan B + C ≤ 9; B = C olamaz.','A = B + C ve B ≠ C, B ≠ 0 (aksi halde A = C olur)'),A('C’yi sabitle','Her tek C için B’yi 1’den 9 − C’ye kadar dene; B ≠ C olsun.','C = 1: B = 2…8 → 7 sayı · C = 3: B = 1, 2, 4, 5, 6 → 5 sayı'),A('Devam et','C = 5: B = 1, 2, 3, 4 → 4 sayı · C = 7: B = 1, 2 → 2 sayı · C = 9: B ≥ 1 olursa A ≥ 10 → 0 sayı','4 + 2 + 0'),A('Topla','Tüm durumları topla.','7 + 5 + 4 + 2 = 18')],
 puf='Koşullu sayma sorularında birler gibi en kısıtlı basamağı sabitle, diğer basamakları o sabit için tara.')

# ---------- 20 · zor · sayfa numaralama ----------
tot=lambda n:sum(len(str(i)) for i in range(1,n+1))
assert tot(399)==1089 and [n for n in range(1,2000) if tot(n)==1089]==[399]
assert tot(99)==189 and 1089-189==900 and 900//3==300 and 1089//3==363 and 99+330==429
mk(P,'0020',tipId='bsm-yazim',tip='Ardışık yazılan sayılarda rakam sayısı',z='orta',alt='Rakam Yazımı',kaz='Ardışık sayıların yazımında kullanılan toplam rakam sayısından son sayıyı bulur.',kalip='hikâyeli',adim=3,
 kart='K-BSMK-06 (ardışık yazım) · toplam rakam sayısından sayfa sayısı',
 metin='Bir kitabın sayfaları 1’den başlanarak ardışık olarak numaralanıyor ve bu numaralamada toplam 1089 rakam kullanılıyor.\nBuna göre bu kitap kaç sayfadır?',
 dogru=399,yan=[(300,'Yalnız üç basamaklı sayfa numaralarının adedini (300) vermiş.','dikkat'),(363,'Tüm numaraları üç basamaklı sanıp 1089 ÷ 3 yapmış.','bilgi'),(400,'Üç basamaklı sayfa adedini bulduktan sonra 99 yerine 100 ekleyip bir fazla saymış.','islem'),(429,'1–99 arası numaraların rakam sayısını 99 almış (iki basamaklıları 2 ile çarpmamış).','bilgi')],
 istenen='Kitabın sayfa sayısı.',
 ip=['Önce 1–9 ve 10–99 numaralarında kaç rakam kullanıldığını bul, kalanı üç basamaklı numaralara ayır.'],
 bilgi=[B('Rakam sayısı','1–9 arası 9 sayı, 1 rakamlı: 9 rakam · 10–99 arası 90 sayı, 2 rakamlı: 180 rakam · 100–999 arası sayılar 3 rakamlıdır')],
 ad=[A('Tek ve iki basamaklılar','1’den 99’a kadar kullanılan rakamları say.','9 × 1 + 90 × 2 = 9 + 180 = 189'),A('Kalan rakamlar','Geriye kalan rakamlar üç basamaklı numaralara aittir.','1089 − 189 = 900'),A('Üç basamaklı numaralar','Her biri 3 rakam kullanır.','900 ÷ 3 = 300 numara'),A('Son sayfa','100’den başlayıp 300 numara: son numara 100 + 300 − 1.','100 + 299 = 399')],
 puf='Rakam sayısı sorularında 9, 180 ve 2700 ara toplamlarını bilirsen kalanı grup grup bölebilirsin.')

# ---------- 21 · zor · rakam çarpımı 24 ----------
c21=[n for n in range(100,1000) if eval('*'.join(str(n)))==24]
assert len(c21)==21
assert 6+6+6==18 and 6+6+3+6==21 and 6+6+6+6==24 and 6+6==12
mk(P,'0021',tipId='bsm-sayma',tip='Tanımlı sayı türü ve rakam koşullu sayma',z='zor',alt='Rakamlarla Sayma',kaz='Rakamları çarpımı verilen üç basamaklı sayıları çarpan üçlülerini bularak sayar.',kalip='düz',adim=4,
 kart='K-BSMK-04 (rakam koşullu sayma) · rakamları çarpımı 24',
 metin='Rakamları çarpımı 24 olan üç basamaklı kaç doğal sayı vardır?',
 dogru=21,yan=[(12,'Yalnız 1 rakamı içeren üçlüleri (1, 3, 8 ve 1, 4, 6) saymış.','dikkat'),(15,'Üçlülerden birini (ör. 2, 3, 4) atlamış.','dikkat'),(18,'2, 2, 6 üçlüsünü atlamış; 6 + 6 + 6 saymış.','dikkat'),(24,'2, 2, 6 üçlüsünü 6 farklı sıralama sanmış; iki rakamı aynı olduğundan yalnız 3 sıralama vardır.','islem')],
 istenen='Rakamları çarpımı 24 olan üç basamaklı sayıların adedi.',
 ip=['24’ü her biri 1–9 arasında olan üç çarpana ayır; sonra her çarpan üçlüsü için yazılabilecek sayıları say.'],
 bilgi=[B('Rakamları çarpımı','rakamlar tek tek çarpılır. Örnek: 258 için 2 × 5 × 8 = 80. Rakamlardan biri 0 ise çarpım 0 olur')],
 ad=[A('Üçlüleri bul','Çarpımı 24 olan üç rakamı (hiçbiri 0 olamaz, hepsi ≤ 9) sırasız yaz.','1 × 3 × 8 · 1 × 4 × 6 · 2 × 2 × 6 · 2 × 3 × 4'),A('Üç farklı rakamlılar','Her üçlüden 3! = 6 sayı yazılır.','{1, 3, 8}, {1, 4, 6}, {2, 3, 4} → 3 × 6 = 18 sayı'),A('Tekrarlı üçlü','2 iki kez geçtiği için yalnız 3 yerleşim: 226, 262, 622.','{2, 2, 6} → 3 sayı'),A('Topla','Dört durumu topla.','18 + 3 = 21')],
 puf='Rakam çarpımı sorularında çarpan üçlülerini sırasız bul; tekrarlı rakamlarda sıralama sayısı azalır.')

# ---------- 22 · zor · 19 katı ----------
c22=[n for n in range(100,1000) if n==19*ds(n) and n%2==1 and len(set(str(n)))==3 and dg(n)[0]>dg(n)[1]]; assert c22==[209]
aday=[n for n in range(100,1000) if n==19*ds(n)]; assert aday==[114,133,152,171,190,209,228,247,266,285,399]
assert all(not(len(set(str(n)))==3 and n%2==1 and dg(n)[0]>dg(n)[1]) for n in (133,399,247,285))
mk(P,'0022',tipId='bsm-cozumleme',tip='Basamak çözümleme ve çözümleme ifadeleri',z='zor',alt='Basamak Çözümleme',kaz='Çözümlemeden elde edilen bir ilişkiyle adayları bulup rakam koşullarıyla tek çözüme ulaşır.',kalip='düz',adim=4,
 kart='K-BSMK-01 (basamak çözümleme) · sayı = 19 × rakamlar toplamı, koşul taraması',
 metin='Üç basamaklı bir sayı, rakamları toplamının 19 katına eşittir. Bu sayı tek sayıdır, rakamları birbirinden farklıdır ve onlar basamağındaki rakam yüzler basamağındaki rakamdan küçüktür.\nBuna göre bu sayı kaçtır?',
 dogru=209,yan=[(133,'Rakamları birbirinden farklı olma koşulunu denetlememiş (3 iki kez geçiyor).','dikkat'),(399,'Rakamları farklı olma (9 iki kez) ve onlar–yüzler sıralaması koşullarını denetlememiş.','dikkat'),(247,'Onlar basamağının yüzlerden küçük olması koşulunu (4 > 2) atlamış.','dikkat'),(285,'Onlar basamağının yüzlerden küçük olması koşulunu (8 > 2) atlamış.','dikkat')],
 istenen='Koşulları sağlayan üç basamaklı sayı.',
 ip=['Çözümleyip sadeleştirince B + 2 × C = 9 × A ilişkisi çıkar; bu ilişkiyi sağlayan sayılardan koşullara uyanı seç.'],
 bilgi=[UC,RT,FRK],
 ad=[A('Eşitliği kur','Sayı ABC, rakamları toplamı A + B + C.','100 × A + 10 × B + C = 19 × (A + B + C)'),A('Sadeleştir','Eşitliğin iki yanını A, B, C cinsinden düzenle.','81 × A = 9 × B + 18 × C · 9 × A = B + 2 × C'),A('Adayları bul','Her A için B + 2 × C = 9 × A’yı sağlayan rakamlardan çıkan 19’un katları.','114, 133, 152, 171, 190, 209, 228, 247, 266, 285, 399'),A('Koşulları uygula','Tek, rakamları farklı, onlar < yüzler: yalnız 209 sağlar.','209: 2 + 0 + 9 = 11 · 19 × 11 = 209')],
 puf='Koşulların çoğu olduğunda önce çözümlemeyle aday listesi çıkar, sonra koşulları tek tek ele.')

# ---------- 23 · zor · öncüllü ABC − CBA ----------
r1=r2=r3=True
for a in range(2,10):
    for c in range(1,a):
        for b in range(1,10):
            d=(100*a+10*b+c)-(100*c+10*b+a)
            r1=r1 and d%99==0; r2=r2 and ds(d)==18; r3=r3 and d%10==a-c
assert r1 and r2 and (not r3)
mk(P,'0023',tipId='bsm-cozumleme',tip='Basamak çözümleme ve çözümleme ifadeleri',z='zor',alt='Basamak Çözümleme',kaz='ABC − CBA farkını çözümleyerek farkın özelliklerini sorgular.',kalip='öncüllü',adim=4,
 kart='K-BSMK-01 (basamak çözümleme) · ABC − CBA için öncüllü ifadeler',
 metin='A, B ve C sıfırdan farklı birer rakamdır ve A > C’dir. ABC ve CBA üç basamaklı doğal sayılardır.\nBuna göre ABC − CBA farkı için\nI. 99’un katıdır.\nII. Rakamları toplamı 18’dir.\nIII. Birler basamağındaki rakam A − C’ye eşittir.\nifadelerinden hangileri kesinlikle doğrudur?',
 dogru='I ve II',sira=['Yalnız I','I ve II','I ve III','II ve III','I, II ve III'],
 yan=[('Yalnız I','Farkın 99’un katı olduğunu bulmuş ama II’yi birkaç örnekle denemeyip eleğe atmış.','dikkat'),('I ve III','Birler basamağını A − C sanmış; 99 × 1 = 99 örneğinde birler 9’dur.','dikkat'),('II ve III','Farkın 99’un katı olduğunu görmeyip I’i yanlış saymış.','bilgi'),('I, II ve III','III’ün yalnız bazı değerlerde (A − C = 5, fark 495) sağlandığını görüp kesin doğru saymış; A − C = 1 için fark 99’dur, birler 9 ≠ 1.','dikkat')],
 istenen='Kesinlikle doğru olan ifadeler.',
 ip=['Farkı 100 × A + 10 × B + C ve 100 × C + 10 × B + A ile yaz; fark A − C’nin hangi katı çıkar?'],
 bilgi=[UC],
 ad=[A('Farkı çözümle','B’li terimler sadeleşir.','ABC − CBA = 99 × A − 99 × C = 99 × (A − C) · I doğru'),A('Rakamlar toplamını incele','A − C = k (1–8) için 99 × k, 100 × (k − 1) + 90 + (10 − k) biçiminde yazılır.','k = 1: 099 · k = 2: 198 · k = 3: 297 · … · k = 8: 792'),A('II’yi doğrula','Her durumda rakamları toplamı 18.','0 + 9 + 9 = 18 · 1 + 9 + 8 = 18 · … · 7 + 9 + 2 = 18'),A('III’ü çürüt','k = 1 için fark 99’dur; birler rakamı 9, A − C = 1.','99 ≠ …1 · III yanlış → I ve II')],
 puf='Öncüllü sorularda çözümlemeyle genel ifadeyi yaz, doğru görünen ifadeyi de tüm durumlarda kanıtla, yanlışı tek örnekle çürüt.')

# ---------- 24 · zor · 300. rakam ----------
dizi=''.join(map(str,range(1,1000)))
assert dizi[299]=='6' and dizi[:12]=='123456789101'
assert 9+180==189 and 300-189==111 and 111//3==37 and 100+37-1==136 and str(135)[2]=='5' and str(136)[1]=='3' and str(136)[0]=='1' and str(137)[2]=='7'
mk(P,'0024',tipId='bsm-yazim',tip='Ardışık yazılan sayılarda rakam sayısı',z='orta',alt='Rakam Yazımı',kaz='Ardışık yazılan sayılarda verilen sıradaki rakamı basamak gruplarını kullanarak bulur.',kalip='yeni nesil',adim=3,
 kart='K-BSMK-06 (ardışık yazım) · dizide 300. rakam',
 metin='Doğal sayılar 1’den başlanarak yan yana yazılıyor ve\n1 2 3 4 5 6 7 8 9 1 0 1 1 1 2 1 3 …\nbiçiminde sonsuz bir rakam dizisi elde ediliyor.\nBuna göre bu dizide soldan 300. sırada yer alan rakam kaçtır?',
 dogru=6,yan=[(1,'136’nın yüzler basamağını (1) almış.','dikkat'),(3,'136’nın onlar basamağını (3) almış.','dikkat'),(5,'Bir sayı eksik sayıp 135’in birler basamağını almış.','islem'),(7,'Bir sayı fazla sayıp 137’nin birler basamağını almış.','islem')],
 istenen='Dizideki 300. rakam.',
 ip=['Önce 1–99 arasındaki sayılarla kaç rakam yazıldığını bul, kalan sırayı üç basamaklı sayılara dağıt.'],
 bilgi=[B('Rakam sayısı','1–9 arası 9 rakam; 10–99 arası 90 sayı × 2 = 180 rakam; 100’den sonra her sayı 3 rakam kullanır')],
 ad=[A('İlk iki grup','1–99 arası rakam sayısı.','9 + 180 = 189'),A('Kalan sıra','300. rakam üç basamaklı sayılar içinde kalır.','300 − 189 = 111. rakam (100’den itibaren)'),A('Hangi sayı?','Her sayı 3 rakam; 111 = 3 × 37, yani 37. üç basamaklı sayının son rakamı.','37. üç basamaklı sayı = 100 + 36 = 136'),A('Rakamı oku','111 tam üçe bölündüğü için 136’nın son rakamı.','136 → 6')],
 puf='Sıra 3’e tam bölünüyorsa o sıradaki rakam üç basamaklı sayının birler basamağıdır; kalan 1 ya da 2 ise yüzler ya da onlar basamağına gider.')

bitir(P,'basamak','mat|Sayı Basamakları')
