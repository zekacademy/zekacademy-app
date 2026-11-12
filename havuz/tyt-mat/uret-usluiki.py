"""Üslü Sayılar · parti 2 (hafif mod): 14 yeni ana soru, kardeş yok, ipucu 1. Her cevap ve her çeldirici değeri, tarif edilen hatadan Fraction ile yeniden üretilip assert edilir."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_mat as H
from _hafif_mat import *
H.KONU='Üslü Sayılar'
P=Parti('usluiki','Üslü Sayılar','mat|Üslü Sayılar')
UK='mat|Üslü Sayılar'
def pw(a,n): return Fr(a)**n
def srt(ps):
    """[(etiket,değer)] -> değere göre sıralı etiket listesi (değerler farklı olmalı)."""
    v=[Fr(x[1]) for x in ps]; assert len(set(v))==len(v)
    return [x[0] for x in sorted(ps,key=lambda x:Fr(x[1]))]

NEG=B('Negatif üs','a⁻ⁿ = 1/aⁿ (a ≠ 0); işaret değişmez, sayı ters çevrilir. Örnek: 2⁻³ = 1/8 · 5⁻¹ = 1/5')
CRP=B('Aynı tabanda çarpma ve bölme','aᵐ × aⁿ = aᵐ⁺ⁿ · aᵐ ÷ aⁿ = aᵐ⁻ⁿ. Tabanlar farklıysa üsler toplanıp çıkarılamaz, önce tabanlar eşitlenir. Örnek: 3⁵ ÷ 3² = 3³')
KK=B('Kuvvetin kuvveti','(aᵐ)ⁿ = aᵐⁿ, yani üsler çarpılır. Örnek: 4³ = (2²)³ = 2⁶ · 8² = (2³)² = 2⁶')
ON=B('10’un kuvvetleri','10ⁿ, 1’in yanına n tane sıfır yazmaktır; 10⁻ⁿ = 1/10ⁿ. Örnek: 10³ = 1000 · 10⁻² = 0,01')
ORT=B('Ortak çarpan','aⁿ⁺ᵏ = aⁿ × aᵏ ve aⁿ⁻ᵏ = aⁿ ÷ aᵏ; en küçük kuvveti parantez dışına al. Örnek: 2ⁿ⁺³ − 2ⁿ = 2ⁿ × (8 − 1) = 7 × 2ⁿ')
NT=B('Negatif tabanın kuvveti','(−a)ⁿ: n çift ise sonuç pozitif, n tek ise negatiftir. Parantez önemlidir: (−3)² = 9 ama −3² = −9. Örnek: (−2)³ = −8 · (−2)⁴ = 16')
TK=B('Tek ve çift sayı','2 ile bölünen sayı çifttir, bölünmeyen tektir. 2n her zaman çifttir, 2n + 1 her zaman tektir. Örnek: n = 3 için 2n = 6 çift, 2n + 1 = 7 tek')
BIL=B('Bilimsel gösterim','Sayı, a × 10ⁿ biçiminde yazılır (1 ≤ a < 10). 10’un kuvvetleri kendi arasında, katsayılar kendi arasında işlenir. Örnek: (3 × 10⁴) × (2 × 10⁻¹) = 6 × 10³')
BASAMAK=B('Basamak sayısı','k × 10ⁿ sayısında k kaç basamaklıysa sayı onun n fazlası kadar basamaklıdır. Örnek: 8 × 10⁵ = 800000 → 1 + 5 = 6 basamak')
BIRIM=B('Uzunluk birimleri','1 m = 10² cm = 10³ mm, yani 1 cm = 10⁻² m ve 1 mm = 10⁻³ m. Örnek: 2 × 10⁻⁵ m = 2 × 10⁻³ cm')
YARI=B('Yarısı, çeyreği, katı','Bir sayının yarısı 2’ye, çeyreği 4’e bölmek; 4 katı ise 4 ile çarpmaktır. 2’nin kuvvetlerinde: 2ⁿ ÷ 4 = 2ⁿ⁻², 4 × 2ⁿ = 2ⁿ⁺². Örnek: 2⁵’in çeyreği 2³ = 8')
KAT=B('Katlanarak artış','Her adımda sayı r katına çıkıyorsa k adım sonra başlangıç değeri rᵏ ile çarpılmış olur. Örnek: kalınlık 3 mm, her adımda 2 katı → 4 adım sonra 3 × 2⁴ = 48 mm')

# ---------- kartlar ----------
KY='ÖSYM 2018–2026 (üslü ifadeler, bilimsel gösterim) · yayın soru bankaları (yalnız mantık) · MEB 9. sınıf'
kart('K-USLB-01','Farklı tabanları eşitleyerek sadeleştirme','Çarpım ve bölümdeki tabanlar aynı asal tabana çevrilir (4 = 2², 8 = 2³), kuvvetin kuvveti ile üsler çarpılıp aynı tabanda üsler toplanıp çıkarılır.','Farklı tabanlıyken üsleri toplayıp çıkarmak; 8² gibi kuvvetin kuvvetini 8 × 2 yapmak; tabanı çevirip üssü çevirmeyi unutmak.','kolay','düz',2,'usb-kural','Üslü ifadelerde sadeleştirme ve negatif üs işlemleri',KY)
kart('K-USLB-02','Negatif tabanın tek ve çift kuvveti','Parantezli negatif tabanın çift kuvveti pozitif, tek kuvveti negatiftir; terimler ayrı ayrı değerlendirilip toplanır.','(−3)² ile −3²’yi karıştırmak; tek üssün işaretini kaçırmak; üssü çarpma gibi okumak.','kolay','düz',2,'usb-negatif','Negatif tabanın kuvveti ve işaret çözümlemesi',KY)
kart('K-USLB-03','Bilimsel gösterimle ölçü ve bölme','Büyüklükler a × 10ⁿ biçiminde yazılıp katsayılar ve 10’un kuvvetleri ayrı ayrı çarpılır ya da bölünür; sonuç istenen birime çevrilir.','Birim çevirmede üssü yanlış kaydırmak; bölmede katsayıları ters bölmek; katsayıyı 10’dan büyük bırakıp üssü düzeltmemek.','kolay','hikâyeli',2,'usb-bilimsel','Bilimsel gösterim ve 10’un kuvvetleri',KY)
kart('K-USLB-04','Ortak çarpan parantezi (kesirli ifade)','Pay ve paydadaki farklı üslü terimlerde en küçük kuvvet ortak çarpan yapılır; kalan çarpanlar sayısal parantez olarak hesaplanıp 2ⁿ gibi ifadeler sadeleşir.','Parantez içindeki işareti yanlış kurmak; 2ⁿ⁺¹ = 2ⁿ × 2 yerine 2ⁿ⁻¹ × 2 sanmak; pay ve paydayı ayrı hesaplayıp çıkarmak.','orta','düz',3,'usb-ortak','Ortak çarpan parantezi ve sadeleştirme',KY)
kart('K-USLB-05','Ortak tabana çevirerek üslü denklem','Kesirli ve tam sayı tabanlar aynı asal tabana çevrilir (1/4 = 2⁻²), üsler çarpılıp toplanır ve eşitlenerek denklem çözülür.','Negatif üssün işaretini yanlış taşımak; 16 = 2⁴ yerine 2² yazmak; kuvvetin kuvvetinde parantezin tamamıyla çarpmamak.','orta','düz',3,'usb-denklem','Aynı tabana çevirerek ve değişken değiştirerek üslü denklem',KY)
kart('K-USLB-06','2ˣ = 3 verilince üslü ifadenin değeri','4ˣ = (2ˣ)², 2ˣ⁺³ = 8 × 2ˣ ve 2ˣ⁺¹ = 2 × 2ˣ yazılır; verilen değer yerine konup üç terim hesaplanır.','Üsleri toplayarak 2ˣ + 3 gibi yazmak; 4ˣ⁺¹’i (4 × 2ˣ)² yapmak; çıkarılan terimi toplamak.','zor','düz',4,'usb-ortak','Ortak çarpan parantezi ve sadeleştirme',KY)
kart('K-USLB-07','Negatif üslü sayıların sıralanması','Tüm sayılar aynı tabana çevrilir (kesir tabanlar ve negatif üsler dahil), üsler karşılaştırılarak küçükten büyüğe sıralanır.','Negatif üssü yok saymak; kesir tabanda üssün yönünü karıştırmak; negatif üssü sayının eksi işareti sanmak.','orta','düz',3,'usb-siralama','Üslü sayıları sıralama (negatif üs ve kesir taban)',KY)
kart('K-USLB-08','Yarısı, çeyreği, 4 katı ile üslü ifade','“Çeyreği”, “yarısı”, “4 katı” 2’nin kuvvetlerinde üs değişimi olarak yazılır ve terimler 2’nin ortak kuvvetiyle toplanır.','Çeyreği ile 4 katını karıştırmak; 4 = 2³ sanmak; toplanan kuvvetlerin üslerini toplamak.','orta','düz',3,'usb-oran','“Yarısı, çeyreği, 4 katı” ile üslü ifade',KY)
kart('K-USLB-09','2ᵃ × 5ᵇ biçiminde basamak sayısı','2’nin ve 5’in kuvvetleri eşlenerek 10’un kuvveti elde edilir, kalan çarpan ile birlikte basamak sayısı bulunur.','Basamak sayısını üsle karıştırmak; 1 fazlasını yanlış saymak; üsleri toplamak.','orta','düz',3,'usb-basamak','2ᵃ × 5ᵇ biçimli sayının basamak sayısı',KY)
kart('K-USLB-10','Üslü ifade öncülleri','Her öncül n’nin tek ve çift olduğu durumlar ayrı incelenerek kanıtlanır ya da bir karşıt örnekle çürütülür.','Tek bir n değeriyle “kesinlikle” sonucuna varmak; 2n + 1’i çift sanmak; (−1)ⁿ’in işaretini karıştırmak.','orta','öncüllü',3,'usb-negatif','Negatif tabanın kuvveti ve işaret çözümlemesi',KY)
kart('K-USLB-11','Negatif üslü terimlerle bölme','Negatif üslü terimler kesre çevrilip toplanır; ters kesirle bölme yapılır, ya da ortak çarpan kuralıyla üsler birleştirilir.','Üsleri toplayıp aynı tabana sığdırmak; bölmeyi çarpma gibi yapmak; terimlerden birini unutmak.','orta','düz',3,'usb-kural','Üslü ifadelerde sadeleştirme ve negatif üs işlemleri',KY)
kart('K-USLB-12','Katlanarak artış (kâğıt katlama)','Başlangıç değeri 2⁻⁴ gibi bir kuvvettir; her katlamada 2 ile çarpılır, birim eşitlenip 2ⁿ⁻⁴ ile verilen eşik karşılaştırılır.','Başlangıcı yok saymak; birimi (m–mm) karıştırmak; eşiği aşan ilk üssün bir eksik ya da fazlasını almak.','orta','hikâyeli',4,'usb-buyume','Katlanarak artan nicelikte eşik problemi',KY)
kart('K-USLB-13','Mikroskop ve bilimsel gösterimle bölme','Görüntü boyutundan gerçek boyut bulunur, birim çevrilir ve toplam uzunluğun bir hücreye oranından hücre sayısı hesaplanır.','Birimi yanlış çevirmek (cm, mm); büyütmeyi çarpma gibi kullanmak; oranı ters kurmak.','zor','hikâyeli',4,'usb-bilimsel','Bilimsel gösterim ve 10’un kuvvetleri',KY)
kart('K-USLB-14','2ᵃ × 3ᵇ biçimli sayıları sayma','Tanımlı sayı kümesi b değerlerine göre gruplanır; her grupta 2ᵃ çarpanıyla sınırın altında kalan sayılar sayılır ve toplanır.','b = 0 ve a = 0 durumlarını atlamak; b’nin büyük değerlerini unutmak; sınırın kendisini (100’ü) saymak.','zor','yeni nesil',4,'usb-tanimli','Tanımlı üslü sayı kümesinde sayma','ÖSYM 2022–2026 (yeni nesil tanımlı kavram) · yayın: 2ᵃ·3ᵇ biçimli sayıları sayma')

# ---------- 01 · kolay · tabanları eşitleme ----------
d1=pw(2,5)*pw(4,3)/pw(8,2); assert d1==32 and 2**(5+6-6)==32
e1=pw(2,5+3-2); assert e1==64                               # üsleri toplayıp çıkarmış
e2=pw(2,5)*pw(4,3)/(8*2); assert e2==128                    # 8² = 8×2
e3=pw(2,5)*pw(2,2+3)/pw(2,6); assert e3==16                 # 4³ = 2^(2+3)
e4=pw(2,5)*pw(2,3)/pw(2,6); assert e4==4                    # 4³ = 2³
mk(P,'0001',tipId='usb-kural',tip='Üslü ifadelerde sadeleştirme ve negatif üs işlemleri',z='kolay',alt='Üslü İfadelerde İşlemler',kaz='Farklı tabanlı çarpım ve bölümü aynı tabana çevirip üs kurallarıyla sadeleştirir.',kalip='düz',adim=2,
 kart='K-USLB-01 (tabanları eşitleyerek sadeleştirme) · 2, 4 ve 8 tabanlı çarpım–bölüm',
 metin='(2⁵ × 4³) ÷ 8²\nişleminin sonucu kaçtır?',
 dogru=32,yan=[(e1,'Tabanlar farklı olduğu halde üsleri toplayıp çıkarmış: 2⁵⁺³⁻² = 2⁶. Tabanlar önce eşitlenmelidir.','bilgi'),(e2,'8² yerine 8 × 2 = 16 yazmış; kuvvet, tabanın üs kadar kendisiyle çarpımıdır, 8² = 64.','bilgi'),(e3,'4³ için 2^(2+3) = 2⁵ yazmış; kuvvetin kuvvetinde üsler çarpılır: 4³ = (2²)³ = 2⁶.','bilgi'),(e4,'4’ü 2² yapıp dış üssü 3’ü 2’yle çarpmayı unutmuş: 4³ = 2³ almış.','islem')],
 istenen='İfadenin sayısal değeri.',
 ip=['4 ve 8’i 2’nin kuvveti olarak yaz, sonra aynı tabanda üsleri toplayıp çıkar.'],
 bilgi=[KK,CRP],
 ad=[A('Tabanları eşitle','4 = 2² ve 8 = 2³ olduğundan hepsi 2 tabanına çevrilir; kuvvetin kuvvetinde üsler çarpılır.','4³ = 2⁶ · 8² = 2⁶'),A('İfadeyi yeniden yaz','Artık tüm tabanlar 2.','(2⁵ × 2⁶) ÷ 2⁶'),A('Üsleri işle','Çarpmada üsler toplanır, bölmede çıkarılır.','2⁵⁺⁶⁻⁶ = 2⁵ = 32')],
 puf='Tabanlar farklıysa önce ortak asal tabana çevir; üs kuralları ancak aynı tabanda çalışır.')

# ---------- 02 · kolay · negatif taban ----------
d2=pw(-3,2)-(-pw(3,2))+pw(-2,3); assert d2==10
e1=pw(-3,2)-pw(-3,2)+pw(-2,3); assert e1==-8              # b = −3² yerine (−3)²
e2=pw(-3,2)+pw(3,2)-pw(-2,3); assert e2==26               # c = +8
e3=3*2+pw(3,2)+pw(-2,3); assert e3==7                     # a = 3 × 2
e4=pw(-3,2)+pw(3,2)+(-2*3); assert e4==12                 # (−2)³ = −2 × 3
mk(P,'0002',tipId='usb-negatif',tip='Negatif tabanın kuvveti ve işaret çözümlemesi',z='kolay',alt='Negatif Taban',kaz='Parantezli ve parantezsiz negatif tabanlı üslü ifadelerin işaretini belirleyerek verilen ifadenin değerini bulur.',kalip='düz',adim=2,
 kart='K-USLB-02 (negatif tabanın tek ve çift kuvveti) · a = (−3)², b = −3², c = (−2)³ değişkenli kurgu',
 metin='a = (−3)²\nb = −3²\nc = (−2)³\nolduğuna göre a − b + c ifadesinin değeri kaçtır?',
 dogru=10,yan=[(e1,'b = −3²’yi (−3)² gibi okuyup +9 almış; parantez yoksa üs yalnız 3’e aittir, −3² = −9.','bilgi'),(e2,'c = (−2)³’ü +8 almış; negatif tabanın tek kuvveti negatiftir, c = −8.','bilgi'),(e3,'a = (−3)² yerine 3 × 2 = 6 yazmış; üs çarpma değil tekrarlı çarpmadır, a = 9.','bilgi'),(e4,'(−2)³’ü −2 × 3 = −6 hesaplamış; (−2)³ = (−2) × (−2) × (−2) = −8.','bilgi')],
 istenen='a − b + c ifadesinin değeri.',
 ip=['a, b ve c’yi ayrı ayrı hesapla; parantezli ve parantezsiz negatif tabanı karıştırma.'],
 bilgi=[NT],
 ad=[A('Değerleri bul','Parantezli negatif tabanın çift kuvveti pozitif, tek kuvveti negatiftir; parantezsiz −3² = −(3²).','a = (−3)² = 9 · b = −3² = −9 · c = (−2)³ = −8'),A('Yerine yaz','Çıkarılan b negatif olduğundan işaret değişir.','a − b + c = 9 − (−9) + (−8)'),A('Hesapla','Sırayla topla ve çıkar.','9 + 9 − 8 = 10')],
 puf='Parantezli negatif tabanda üs çiftse sonuç pozitiftir; parantezsiz −3² ise −(3²) = −9’dur. Çıkarmada işareti bir kez daha değiştirmeyi unutma.')

# ---------- 03 · kolay · bilimsel gösterim, depolama ----------
dg=Fr(3*10**10,6*10**4); assert dg==5*10**5
V=lambda k,n:Fr(k)*Fr(10)**n
c3=[('5 × 10⁵',V(5,5)),('2 × 10⁶',V(2,6)),('5 × 10⁶',V(5,6)),('5 × 10¹³',V(5,13)),('2 × 10⁻⁶',V(2,-6))]
assert V(3,10)/V(6,4)==V(5,5)
assert V(2,6)==Fr(6,3)*Fr(10)**(10-4)                       # katsayıları ters bölmemiş (6/3) ve üsler 10−4
assert Fr(5,10)*Fr(10)**6==V(5,5) and V(5,6)!=V(5,5)           # 0,5 × 10⁶ → 5 × 10⁶ (virgül kaydırılmamış)
assert Fr(3,6)*Fr(10)**(10+4)==V(5,13)                      # üsleri toplamış
assert Fr(6,3)*Fr(10)**(4-10)==V(2,-6)                      # ters oran
mk(P,'0003',tipId='usb-bilimsel',tip='Bilimsel gösterim ve 10’un kuvvetleri',z='kolay',alt='Bilimsel Gösterim',kaz='Bilimsel gösterimle verilen iki büyüklüğün oranını bulur ve sonucu bilimsel gösterimle yazar.',kalip='hikâyeli',adim=2,
 kart='K-USLB-03 (bilimsel gösterimle ölçü ve bölme) · depolama alanı ve fotoğraf boyutu',
 metin='Kapasitesi 3 × 10¹⁰ bayt olan bir depolama alanına, her biri 6 × 10⁴ bayt boyutunda özdeş fotoğraflar yükleniyor.\nDepolama alanı tam dolana kadar fotoğraf yüklendiğine göre kaç fotoğraf yüklenmiştir?',
 dogru='5 × 10⁵',sira=srt(c3),
 yan=[('2 × 10⁶','Katsayıları ters bölmüş: 6 ÷ 3 = 2 almış (doğrusu 3 ÷ 6 = 0,5); üsleri 10 − 4 = 6 doğru çıkarmış.','islem'),('5 × 10⁶','3 ÷ 6 = 0,5 bulup 0,5 × 10⁶ ifadesini 5 × 10⁶ yazmış; virgülü bir basamak kaydırınca üs bir azalmalıdır.','islem'),('5 × 10¹³','Bölme yerine üsleri toplamış: 10¹⁰ × 10⁴ = 10¹⁴ ve 0,5 × 10¹⁴ = 5 × 10¹³.','bilgi'),('2 × 10⁻⁶','Oranı ters kurmuş: fotoğraf boyutunu alana bölmüş (6 × 10⁴ ÷ 3 × 10¹⁰).','dikkat')],
 istenen='Yüklenen fotoğraf sayısı.',
 ip=['Fotoğraf sayısı = alan ÷ fotoğraf boyutu; katsayıları ve 10’un kuvvetlerini ayrı ayrı böl.'],
 bilgi=[BIL,CRP],
 ad=[A('İşlemi kur','Alan, fotoğraf boyutuna bölünür.','(3 × 10¹⁰) ÷ (6 × 10⁴)'),A('Katsayıları ve kuvvetleri ayrı böl','3 ÷ 6 = 0,5 ve 10¹⁰ ÷ 10⁴ = 10⁶.','0,5 × 10⁶'),A('Bilimsel gösterime çevir','Katsayı 1 ile 10 arasında olmalı; virgül bir basamak sağa kayınca üs bir azalır.','0,5 × 10⁶ = 5 × 10⁵ = 500000')],
 puf='Bilimsel gösterimde böl: katsayılar kendi arasında, 10’un kuvvetleri kendi arasında; sonunda katsayıyı 1 ile 10 arasına getir.')

# ---------- 04 · orta · ortak çarpan, kesir ----------
def g4(n): return (pw(2,n+4)-pw(2,n))/(pw(2,n+1)-pw(2,n-1))
assert all(g4(n)==10 for n in range(-6,12))
assert (16-1)*2/ (4-1)==10
e1=Fr(3)*pw(2,5)/(3*pw(2,4)); assert e1==2                 # 2ⁿ⁺⁴ = 2ⁿ × 4 sanmış: pay 3 × 2ⁿ, payda 3 × 2ⁿ⁻¹ (n = 5)
e2=Fr(15)*pw(2,5)/(pw(2,5)*(2-1)); assert e2==15                    # paydada 2ⁿ⁻¹ yerine 2ⁿ (2ⁿ × (2 − 1))
e3=Fr(15,3); assert e3==5                                    # 2ⁿ ile 2ⁿ⁻¹ sadeleştiğini sanmış
e4=Fr(15)*pw(2,5)/(pw(2,4)*(2-1)); assert e4==30            # 2ⁿ⁺¹ = 2ⁿ⁻¹ × 2
mk(P,'0004',tipId='usb-ortak',tip='Ortak çarpan parantezi ve sadeleştirme',z='orta',alt='Ortak Çarpan',kaz='Pay ve paydadaki üslü terimleri ortak çarpan parantezine alarak ifadenin değerini bulur.',kalip='düz',adim=3,
 kart='K-USLB-04 (ortak çarpan parantezi) · pay ve paydada 2ⁿ’li fark, sabit değerli kesir',
 metin='n bir tam sayı olmak üzere\n(2ⁿ⁺⁴ − 2ⁿ) ÷ (2ⁿ⁺¹ − 2ⁿ⁻¹)\nifadesinin değeri kaçtır?',
 dogru=10,yan=[(e1,'2ⁿ⁺⁴’ü 2ⁿ × 4 sanıp payı 3 × 2ⁿ bulmuş; 2ⁿ⁺⁴ = 2ⁿ × 2⁴ = 2ⁿ × 16’dır.','bilgi'),(e2,'Paydada 2ⁿ⁺¹ − 2ⁿ⁻¹ farkından 2ⁿ’yi ortak çarpan alıp (2 − 1) yazmış; 2ⁿ⁻¹, 2ⁿ’nin yarısıdır.','islem'),(e3,'2ⁿ ile 2ⁿ⁻¹’in aynı olduğunu sanıp 15 ÷ 3 = 5 bulmuş; 2ⁿ⁻¹ = 2ⁿ ÷ 2’dir.','bilgi'),(e4,'2ⁿ⁺¹’i 2ⁿ⁻¹ × 2 yazıp paydayı 2ⁿ⁻¹ × (2 − 1) bulmuş; 2ⁿ⁺¹ = 2ⁿ⁻¹ × 2² = 2ⁿ⁻¹ × 4’tür.','islem')],
 istenen='İfadenin sayısal değeri.',
 ip=['Payda en küçük kuvvet 2ⁿ⁻¹; her iki terimi de 2ⁿ⁻¹ cinsinden yaz. Payı ise 2ⁿ ortak çarpanıyla yaz.'],
 bilgi=[ORT,CRP],
 ad=[A('Payı çarpanlara ayır','2ⁿ ortak çarpan; 2ⁿ⁺⁴ = 2ⁿ × 16.','2ⁿ⁺⁴ − 2ⁿ = 2ⁿ × (16 − 1) = 15 × 2ⁿ'),A('Paydayı çarpanlara ayır','En küçük kuvvet 2ⁿ⁻¹; 2ⁿ⁺¹ = 2ⁿ⁻¹ × 2² = 2ⁿ⁻¹ × 4.','2ⁿ⁺¹ − 2ⁿ⁻¹ = 2ⁿ⁻¹ × (4 − 1) = 3 × 2ⁿ⁻¹'),A('Sadeleştir','2ⁿ = 2ⁿ⁻¹ × 2 olduğundan oran 2’ye bölünür.','(15 × 2ⁿ) ÷ (3 × 2ⁿ⁻¹) = 5 × 2 = 10')],
 puf='Kesirde pay ve paydadaki üslü farkları ayrı ayrı ortak çarpan parantezine al; ortak üslü çarpanı sadeleştirirken 2ⁿ ile 2ⁿ⁻¹ arasındaki 2 katı unutma.')

# ---------- 05 · orta · üslü denklem, kesir taban ----------
def f5(x): return Fr(1,4)**(x+1)*Fr(8)**x
S5=[x for x in range(-40,41) if f5(x)==16]; assert S5==[6]
assert [x for x in range(-40,41) if -2*x+1+3*x==4]==[3]     # 1/4 = 2⁻², üs −2x + 1 (+1'i çarpmamış)
assert [x for x in range(-40,41) if -2*x-2+3*x==2]==[4]     # 16 = 2²
assert [x for x in range(-40,41) if -2*x-2+3*x==3]==[5]     # 16 = 2³
assert 4-2==2                                               # x − 2 = 4 → x = 4 − 2
mk(P,'0005',tipId='usb-denklem',tip='Aynı tabana çevirerek ve değişken değiştirerek üslü denklem',z='orta',alt='Üslü Denklem',kaz='Kesirli ve tam sayı tabanları 2 tabanında birleştirip üsleri eşitleyerek denklemi çözer.',kalip='düz',adim=3,
 kart='K-USLB-05 (ortak tabana çevirerek denklem) · 1/4, 8 ve 16 tabanları',
 metin='(1/4)ˣ⁺¹ × 8ˣ = 16\nolduğuna göre x kaçtır?',
 dogru=6,yan=[(2,'Üs eşitliğini x − 2 = 4 yazıp 4’ü karşıya geçirirken x = 4 − 2 = 2 bulmuş; doğrusu x = 4 + 2.','islem'),(3,'(2⁻²)ˣ⁺¹’i 2⁻²ˣ⁺¹ yazmış; −2 üssü x + 1’in her iki terimiyle çarpılmalıdır (−2x − 2).','islem'),(4,'16’yı 2² almış (16 = 2⁴); 2⁴ yerine 2² yazınca x − 2 = 2 çıkmış.','bilgi'),(5,'16’yı 2³ almış (aynı soruda geçen 8 = 2³ ile karıştırmış): x − 2 = 3 ⇒ x = 5; oysa 16 = 2⁴’tür.','dikkat')],
 istenen='x’in değeri.',
 ip=['Her tabanı 2’nin kuvveti olarak yaz: 1/4 = 2⁻², 8 = 2³, 16 = 2⁴.'],
 bilgi=[NEG,KK],
 ad=[A('Aynı tabana çevir','1/4 = 2⁻², 8 = 2³, 16 = 2⁴.','(2⁻²)ˣ⁺¹ × (2³)ˣ = 2⁴'),A('Kuvvetin kuvveti, sonra çarpma','Üsler çarpılır; parantez içindeki x + 1’in her iki terimi çarpılmalı. Aynı tabanda çarpmada üsler toplanır.','2⁻²ˣ⁻² × 2³ˣ = 2ˣ⁻²'),A('Üsleri eşitle','Tabanlar aynı olduğundan üsler eşit.','x − 2 = 4 ⇒ x = 6'),A('Kontrol','x = 6: (1/4)⁷ × 8⁶ = 2⁻¹⁴ × 2¹⁸.','2⁻¹⁴ × 2¹⁸ = 2⁴ = 16 ✓')],
 puf='Kesirli tabanı negatif üsle yaz (1/4 = 2⁻²); parantezli üstleri çarparken parantezin her terimini çarp.')

# ---------- 06 · orta · negatif üslü sıralama ----------
def ex(a,n): return Fr(a)**n
va=ex(8,-3); vb=ex(Fr(1,4),-5); vc=ex(Fr(1,2),7)
assert va==Fr(1,2**9) and vb==2**10 and vc==Fr(1,2**7) and va<vc<vb
# hata modelleri
eA=(ex(8,3),ex(Fr(1,4),5),vc)                        # negatif üssü yok saymış (8⁻³ → 8³, (1/4)⁻⁵ → (1/4)⁵)
assert eA[1]<eA[2]<eA[0] and True
sirala=lambda t:' < '.join(n for n,_ in sorted(zip('abc',t),key=lambda p:p[1]))
dg6=sirala((va,vb,vc)); assert dg6=='a < c < b'
oA=sirala(eA); assert oA=='b < c < a'
eB=(va,ex(4,-5),ex(2,7)); oB=sirala(eB); assert oB=='b < a < c'                 # kesir tabanı yok saymış (1/4 → 4, 1/2 → 2)
eD=(va,ex(2,-2-5),ex(2,7)); oD=sirala(eD); assert oD=='a < b < c'              # (1/4)⁻⁵ = 2^(−2−5) ve (1/2)⁷ = 2⁷
eE=(ex(8,3),vb,vc); oE=sirala(eE); assert oE=='c < a < b'                       # yalnız 8⁻³’ü 8³ okumuş
assert len({dg6,oA,oB,oD,oE})==5
mk(P,'0006',tipId='usb-siralama',tip='Üslü sayıları sıralama (negatif üs ve kesir taban)',z='orta',alt='Üslü Sayıları Sıralama',kaz='Negatif üslü ve kesir tabanlı sayıları aynı tabana çevirerek küçükten büyüğe sıralar.',kalip='düz',adim=3,
 kart='K-USLB-07 (negatif üslü sayıların sıralanması) · 8⁻³, (1/4)⁻⁵, (1/2)⁷',
 metin='a = 8⁻³\nb = (1/4)⁻⁵\nc = (1/2)⁷\nolduğuna göre a, b ve c sayılarının küçükten büyüğe doğru sıralanışı aşağıdakilerden hangisidir?',
 dogru=dg6,sira=['a < b < c','a < c < b','b < a < c','b < c < a','c < a < b'],
 yan=[(oA,'8⁻³ ve (1/4)⁻⁵’teki negatif üssü yok sayıp 8³ ve (1/4)⁵ gibi hesaplamış; negatif üs sayıyı ters çevirir.','bilgi'),(oB,'Kesir tabanları yok sayıp 4⁻⁵ ve 2⁷ yazmış; (1/4)⁻⁵ = 4⁵ = 2¹⁰ ve (1/2)⁷ = 2⁻⁷ olmalıydı.','bilgi'),(oD,'(1/4)⁻⁵’te üsleri çarpmak yerine toplamış (2⁻²⁻⁵ = 2⁻⁷) ve (1/2)⁷’yi 2⁷ okumuş: a = 2⁻⁹ < b = 2⁻⁷ < c = 2⁷.','bilgi'),(oE,'Yalnız 8⁻³’ü 8³ okumuş (2⁹); b ve c doğru çevrilince c < a < b çıkmış.','dikkat')],
 istenen='Üç sayının küçükten büyüğe sıralanışı.',
 ip=['Üçünü de 2’nin kuvveti olarak yaz; negatif üs ve kesir tabana dikkat et.'],
 bilgi=[NEG,KK],
 ad=[A('2 tabanına çevir','8 = 2³, 1/4 = 2⁻², 1/2 = 2⁻¹.','a = (2³)⁻³ · b = (2⁻²)⁻⁵ · c = (2⁻¹)⁷'),A('Üsleri çarp','Kuvvetin kuvvetinde üsler çarpılır.','a = 2⁻⁹ · b = 2¹⁰ · c = 2⁻⁷'),A('Üsleri karşılaştır','Taban 2 > 1 olduğundan büyük üs büyük sayıyı verir.','−9 < −7 < 10 ⇒ a < c < b')],
 puf='Tabanı 1’den büyük bir sayıda üs büyüdükçe sayı büyür; negatif üsler küçük (negatif) üstür, sayı 0’a yaklaşır.')

# ---------- 07 · orta · çeyreği / 4 katı ----------
x7=pw(2,12); y7=pw(2,9)
d7=x7/4+4*y7; assert d7==3*2**10
c7=[('3 × 2¹⁰',3*2**10),('2¹²',2**12),('5 × 2¹⁰',5*2**10),('9 × 2¹¹',9*2**11),('2²¹',2**21)]
assert x7/2+4*y7==2**12                       # çeyreği yerine yarısı
assert x7/4+8*y7==5*2**10                       # 4 katı için 2⁹ × 2³ (4 = 2³)
assert 4*x7+4*y7==9*2**11                     # çeyreği yerine 4 katı
assert pw(2,10)+pw(2,11)!=2**21 and 2**(10+11)==2**21
mk(P,'0007',tipId='usb-oran',tip='“Yarısı, çeyreği, 4 katı” ile üslü ifade',z='orta',alt='Yarısı, Çeyreği, Katı',kaz='Bir üslü sayının çeyreği ve 4 katını 2’nin kuvvetleriyle yazıp toplamını bulur.',kalip='düz',adim=3,
 kart='K-USLB-08 (yarısı, çeyreği, 4 katı) · x = 2¹², y = 2⁹',
 metin='x = 2¹²\ny = 2⁹\nolduğuna göre x sayısının çeyreği ile y sayısının 4 katının toplamı aşağıdakilerden hangisine eşittir?',
 dogru='3 × 2¹⁰',sira=srt(c7),
 yan=[('2¹²','Çeyreği yerine yarısını alıp x ÷ 2 = 2¹¹ bulmuş; 2¹¹ + 2¹¹ = 2¹² çıkmış. Çeyrek, 4’e bölmektir (2¹⁰).','dikkat'),('5 × 2¹⁰','y’nin 4 katını 2⁹ × 2³ = 2¹² yazmış (4 = 2³ sanmış) ve 2¹⁰ + 2¹² = 5 × 2¹⁰ bulmuş; 4 = 2² olduğundan 4 katı 2¹¹’dir.','bilgi'),('9 × 2¹¹','Çeyreği yerine 4 katını almış: x × 4 = 2¹⁴ ve 2¹⁴ + 2¹¹ = 9 × 2¹¹.','dikkat'),('2²¹','Terimleri 2¹⁰ + 2¹¹ diye doğru bulup toplarken üsleri toplamış (10 + 11 = 21); toplamada üsler toplanmaz.','bilgi')],
 istenen='x’in çeyreği ile y’nin 4 katının toplamı.',
 ip=['Çeyrek 4’e bölmek, 4 katı 4 ile çarpmaktır; 4 = 2² yaz.'],
 bilgi=[YARI,CRP],
 ad=[A('Terimleri ayrı ayrı yaz','Çeyreği için 4’e böl, 4 katı için 4 ile çarp; 4 = 2².','x ÷ 4 = 2¹² ÷ 2² = 2¹⁰ · 4 × y = 2² × 2⁹ = 2¹¹'),A('Toplamı kur','Terimlerin üsleri farklı; küçük olan 2¹⁰ ortak çarpan olur.','2¹⁰ + 2¹¹ = 2¹⁰ × (1 + 2)'),A('Hesapla','Parantezi bul.','2¹⁰ × 3 = 3 × 2¹⁰')],
 puf='Aynı tabanlı kuvvetler toplanırken üsler toplanmaz; küçük kuvveti ortak çarpan yapıp parantez içini hesapla.')

# ---------- 08 · orta · basamak sayısı ----------
v8=2**15*5**12; assert v8==8*10**12 and len(str(v8))==13
mk(P,'0008',tipId='usb-basamak',tip='2ᵃ × 5ᵇ biçimli sayının basamak sayısı',z='orta',alt='Basamak Sayısı',kaz='2 ve 5 tabanlı üslü çarpımı 10’un kuvvetiyle yazarak sayının basamak sayısını bulur.',kalip='düz',adim=3,
 kart='K-USLB-09 (2ᵃ × 5ᵇ ile basamak sayısı) · 2¹⁵ × 5¹²',
 metin='2¹⁵ × 5¹²\nsayısı kaç basamaklıdır?',
 dogru=13,yan=[(12,'10¹² sayısındaki sıfır sayısını (12) basamak sayısı sanmış ve 8 çarpanını saymamış.','dikkat'),(14,'8 × 10¹²’yi 8’in bir basamağı ve 10¹²’nin 13 basamağı diye sayıp 14 bulmuş; 10¹² zaten 13 basamaklıdır.','islem'),(15,'2³’ün üssünü (3) kalan üsse eklemiş: 3 + 12 = 15 basamak sanmış.','bilgi'),(27,'Üsleri toplayıp 15 + 12 = 27 yazmış; sayı 10’un kuvvetine çevrilmeden basamak sayısı üslerin toplamından bulunamaz.','bilgi')],
 istenen='Sayının basamak sayısı.',
 ip=['2 ile 5’i eşleştirip 10’un kuvvetini oluştur; arta kalan çarpanı yaz.'],
 bilgi=[BASAMAK,CRP],
 ad=[A('2 ve 5’i eşleştir','5¹² ile 2¹²’den 10¹² oluşur; 2¹⁵ = 2³ × 2¹².','2¹⁵ × 5¹² = 2³ × (2¹² × 5¹²)'),A('10’un kuvvetini yaz','Aynı üslü çarpımlar birleştirilir.','2³ × 10¹² = 8 × 10¹²'),A('Basamak sayısını bul','8 bir basamaklı; 12 sıfır eklenince sayı 8000000000000 olur.','1 + 12 = 13 basamak')],
 puf='2ᵃ × 5ᵇ sayısında küçük üssü kadar 2 ile 5’i eşleştirip 10’un kuvveti yap; arta kalan çarpanla birlikte basamak sayısını say.')

# ---------- 09 · zor · 2ˣ = 3 verilince ----------
import math
xx=math.log2(3)
assert abs(4**(xx+1)-2**(xx+3)+2**(xx+1)-18)<1e-9
t=Fr(3)
d9=4*t*t-8*t+2*t; assert d9==18
e36=4*t*t-(3+3)+(3+3); assert e36==36                    # 2ˣ⁺³ = 3 + 3 ve 2ˣ⁺¹ = 3 + 3
e34=4*t*t-(3+3)+(3+1); assert e34==34                    # 2ˣ⁺³ = 3 + 3 ve 2ˣ⁺¹ = 3 + 1
e66=4*t*t+8*t+2*t; assert e66==66                        # çıkarılanı toplamış
e126=(4*t)**2-8*t+2*t; assert e126==126                  # 4ˣ⁺¹ = (4 × 2ˣ)²
assert len({d9,e36,e34,e66,e126})==5
mk(P,'0009',tipId='usb-ortak',tip='Ortak çarpan parantezi ve sadeleştirme',z='zor',alt='Verilen Değerle Üslü İfade',kaz='2ˣ değeri verildiğinde 4ˣ⁺¹, 2ˣ⁺³ ve 2ˣ⁺¹ terimlerini 2ˣ cinsinden yazıp ifadenin değerini bulur.',kalip='düz',adim=4,
 kart='K-USLB-06 (2ˣ = 3 verilince üslü ifade) · 4ˣ⁺¹ − 2ˣ⁺³ + 2ˣ⁺¹',
 metin='2ˣ = 3\nolduğuna göre 4ˣ⁺¹ − 2ˣ⁺³ + 2ˣ⁺¹ ifadesinin değeri kaçtır?',
 dogru=18,yan=[(e34,'2ˣ⁺³’ü 3 + 3 = 6 ve 2ˣ⁺¹’i 3 + 1 = 4 yazmış (üsleri tabanla toplamış); 2ˣ⁺³ = 2ˣ × 2³ = 24, 2ˣ⁺¹ = 6’dır.','bilgi'),(e36,'2ˣ⁺³ ve 2ˣ⁺¹ için 2ˣ’e 3 ekleyip (3 + 3 = 6) işlem yapmış; üsteki sayı çarpan olur: 2³ ve 2¹.','bilgi'),(e66,'Çıkarılan terimi de toplamış: 36 + 24 + 6.','dikkat'),(e126,'4ˣ⁺¹’i (4 × 2ˣ)² = 144 yazmış; 4ˣ⁺¹ = 4 × (2ˣ)² = 4 × 9 = 36’dır.','islem')],
 istenen='İfadenin sayısal değeri.',
 ip=['Her terimi 2ˣ cinsinden yaz: 4ˣ = (2ˣ)², 2ˣ⁺³ = 2ˣ × 2³.'],
 bilgi=[KK,ORT,CRP],
 ad=[A('4ˣ⁺¹’i çevir','4 = 2² olduğundan 4ˣ = (2ˣ)²; 4ˣ⁺¹ = 4 × 4ˣ.','4ˣ⁺¹ = 4 × (2ˣ)² = 4 × 3² = 36'),A('2ˣ⁺³’ü çevir','Üsteki toplam, çarpan olur.','2ˣ⁺³ = 2ˣ × 2³ = 3 × 8 = 24'),A('2ˣ⁺¹’i çevir','Aynı kurala göre.','2ˣ⁺¹ = 2ˣ × 2 = 3 × 2 = 6'),A('Hesapla','Çıkarma ve toplamayı sırayla yap.','36 − 24 + 6 = 18')],
 puf='2ˣ değeri verildiğinde her terimi 2ˣ’in kuvveti ve sabit çarpan olarak yaz: aˣ⁺ᵏ = aˣ × aᵏ ve a²ˣ = (aˣ)².')

# ---------- 10 · orta · öncüllü ----------
N10=range(1,60)
I_=all(pw(-1,n)+pw(-1,n+1)==0 for n in N10); II_=all(pw(-2,n)+pw(2,n)==0 for n in N10); III_=all(pw(-5,2*n+1)<0 for n in N10)
assert I_ and (not II_) and III_ and pw(-2,1)+pw(2,1)==0 and pw(-2,2)+pw(2,2)==8
S10=['Yalnız I','Yalnız III','I ve II','I ve III','I, II ve III']
mk(P,'0010',tipId='usb-negatif',tip='Negatif tabanın kuvveti ve işaret çözümlemesi',z='orta',alt='Negatif Taban',kaz='Negatif tabanlı üslü ifadelerin işaretini n’nin tek ve çift olmasına göre inceleyerek kesinlikle doğru olanları belirler.',kalip='öncüllü',adim=3,
 kart='K-USLB-10 (üslü ifade öncülleri) · (−1)ⁿ, (−2)ⁿ ve (−5)²ⁿ⁺¹',
 metin='n pozitif bir tam sayı olmak üzere,\nI. (−1)ⁿ + (−1)ⁿ⁺¹ = 0\nII. (−2)ⁿ + 2ⁿ = 0\nIII. (−5)²ⁿ⁺¹ < 0\nifadelerinden hangileri kesinlikle doğrudur?',
 dogru='I ve III',sira=S10,
 yan=[('Yalnız I','III’te üssün 2n’li göründüğü için çift sayı olduğunu sanıp (−5)²ⁿ⁺¹’i pozitif saymış; 2n + 1 her zaman tektir.','dikkat'),('Yalnız III','I’de n’ye göre iki terimin işareti değişir diye toplamın 0 olmayabileceğini sanmış; terimlerin işareti hep zıttır, toplam 0’dır.','bilgi'),('I ve II','II’yi yalnız n = 1 ile deneyip doğru sanmış; III’te 2n + 1’i çift sanıp (−5)²ⁿ⁺¹’i pozitif bulmuş (iki hata birlikte).','dikkat'),('I, II ve III','II’yi yalnız n = 1 ile denemiş; kesinlikle doğru için n’nin çift değerleri de denenmelidir.','dikkat')],
 istenen='Kesinlikle doğru olan ifadeler.',
 ip=['n çift ve n tek durumlarını ayrı ayrı dene; (−1)ⁿ ile (−1)ⁿ⁺¹ ardışık kuvvetlerdir.'],
 bilgi=[NT,TK],
 ad=[A('I’i incele','n ile n + 1’den biri çift, diğeri tektir; (−1)’in çift kuvveti 1, tek kuvveti −1 olur.','(−1)ⁿ + (−1)ⁿ⁺¹ = 1 + (−1) = 0 · her n için doğru'),A('II’yi çürüt','n = 1’de sağlanır, fakat n çiftse iki terim de pozitiftir.','n = 2: (−2)² + 2² = 4 + 4 = 8 ≠ 0 · yanlış'),A('III’ü incele','2n çifttir, 2n + 1 her zaman tektir; negatif tabanın tek kuvveti negatiftir.','(−5)²ⁿ⁺¹ < 0 · her n için doğru'),A('Sonuç','I ve III kesinlikle doğru.','I ve III')],
 puf='“Kesinlikle doğru” için n’nin tek ve çift durumlarını ayrı ayrı incele; bir tek örnek doğru çıkarsa ifade kesin olmaz, bir karşıt örnek ifadeyi çürütür.')

# ---------- 11 · orta · negatif üslü bölme ----------
d11=(pw(5,-1)+pw(5,-2))/pw(5,-3); assert d11==30
e1=pw(5,-3)/pw(5,-3); assert e1==1                         # 5⁻¹ + 5⁻² = 5⁻³
e2=(pw(5,-1)+pw(5,-2))/pw(5,-2); assert e2==6               # 5⁻³ yerine 5⁻² (1/25)
e3=pw(5,-1)/pw(5,-3); assert e3==25                         # ikinci terimi atlamış
e4=(pw(5,-1)+pw(5,-2))/(-pw(5,-3)); assert e4==-30          # 5⁻³ = −1/125
mk(P,'0011',tipId='usb-kural',tip='Üslü ifadelerde sadeleştirme ve negatif üs işlemleri',z='orta',alt='Negatif Üs',kaz='Negatif üslü terimleri kesre çevirerek toplayıp negatif üslü bir terime bölme işlemini yapar.',kalip='düz',adim=3,
 kart='K-USLB-11 (negatif üslü terimlerle bölme) · (5⁻¹ + 5⁻²) ÷ 5⁻³',
 metin='(5⁻¹ + 5⁻²) ÷ 5⁻³\nişleminin sonucu kaçtır?',
 dogru=30,yan=[(e1,'5⁻¹ + 5⁻² = 5⁻³ yazıp (üsleri toplamış) 5⁻³ ÷ 5⁻³ = 1 bulmuş; farklı üslü terimler toplanırken üsler toplanmaz.','bilgi'),(e2,'Böleni 5⁻³ yerine 5⁻² (= 1/25) almış; 5⁻³ = 1/125’tir.','islem'),(e3,'İkinci terimi (5⁻²) unutup yalnız 5⁻¹ ÷ 5⁻³ = 25 hesaplamış.','dikkat'),(e4,'5⁻³’ü −1/125 almış; negatif üs sayıyı negatif yapmaz, ters çevirir.','bilgi')],
 istenen='İfadenin sayısal değeri.',
 ip=['Her terimi kesre çevir: 5⁻¹ = 1/5, 5⁻² = 1/25, 5⁻³ = 1/125.'],
 bilgi=[NEG,CRP],
 ad=[A('Negatif üsleri kesre çevir','Üs negatifse sayı ters çevrilir.','5⁻¹ = 1/5 · 5⁻² = 1/25 · 5⁻³ = 1/125'),A('Paydaları eşitleyip topla','Paydalar 25’te eşitlenir.','1/5 + 1/25 = 5/25 + 1/25 = 6/25'),A('Ters kesirle çarp','Bir kesre bölmek, tersiyle çarpmaktır.','(6/25) ÷ (1/125) = 6/25 × 125 = 30')],
 puf='Negatif üslü terimleri toplamadan önce kesre çevir; üslü terimler toplanırken üsler asla toplanmaz.')

# ---------- 12 · zor · kâğıt katlama ----------
def kal(n): return Fr(2)**(n-4)
n12=min(n for n in range(0,60) if kal(n)>1000); assert n12==14 and kal(13)==512 and kal(14)==1024 and 2**10==1024
assert min(n for n in range(0,60) if Fr(2)**n>1000)==10                       # başlangıç kalınlığını yok saymış
assert min(n for n in range(0,60) if Fr(2)**(n+4)>1000)==6                    # 2ⁿ × 2⁴ (üssün işaretini ters almış)
assert min(n for n in range(0,60) if kal(n)>100)==11                          # 1 m = 100 mm sanmış
assert 13==n12-1                                                               # 2⁹ = 512 < 1000 → bir eksik
mk(P,'0012',tipId='usb-buyume',tip='Katlanarak artan nicelikte eşik problemi',z='orta',alt='Katlanarak Artış',kaz='Başlangıç değeri üslü verilen ve her adımda iki katına çıkan bir niceliğin eşiği aşması için gereken adım sayısını bulur.',kalip='hikâyeli',adim=4,
 kart='K-USLB-12 (katlanarak artış, kâğıt katlama) · kalınlık 2⁻⁴ mm, eşik 1 m',
 metin='Kalınlığı 2⁻⁴ milimetre olan çok ince bir kâğıt art arda ikiye katlanıyor ve her katlamada oluşan yığının kalınlığı bir önceki katlamadaki kalınlığın 2 katı oluyor. (2¹⁰ = 1024 olduğu bilinmektedir.)\nYığının kalınlığının ilk kez 1 metreyi aşması için kâğıt en az kaç kez katlanmalıdır?',
 dogru=14,yan=[(6,'Kalınlığı 2ⁿ × 2⁴ yazmış (2⁻⁴’ü 2⁴ almış); 2ⁿ⁺⁴ > 1000 için n + 4 = 10, n = 6 bulmuş.','bilgi'),(10,'Başlangıç kalınlığını (2⁻⁴ mm) hesaba katmamış; 2ⁿ > 1000 için n = 10 almış.','dikkat'),(11,'1 m’yi 100 mm sanıp 2ⁿ⁻⁴ > 100 koşulundan (2⁷ = 128) n = 11 bulmuş.','bilgi'),(13,'2ⁿ⁻⁴ > 1000 koşulunda üssü 9 almış (2⁹ = 512); 512 henüz 1000’i aşmaz, üs 10 olmalıdır.','islem')],
 istenen='Kâğıdın en az katlanma sayısı.',
 ip=['n katlama sonunda kalınlık 2⁻⁴ × 2ⁿ = 2ⁿ⁻⁴ milimetre; 1 m = 1000 mm ile karşılaştır.'],
 bilgi=[KAT,BIRIM,CRP],
 ad=[A('Kalınlığı yaz','Her katlamada 2 ile çarpılır, n katlamada 2ⁿ ile.','kalınlık = 2⁻⁴ × 2ⁿ = 2ⁿ⁻⁴ mm'),A('Birimi eşitle','1 m = 1000 mm; kalınlık milimetre cinsinden 1000’i aşmalı.','2ⁿ⁻⁴ > 1000'),A('Üssü bul','2⁹ = 512 < 1000 ve 2¹⁰ = 1024 > 1000 olduğundan üs en az 10 olmalı.','n − 4 ≥ 10'),A('n’yi hesapla','Eşitsizliği çöz.','n ≥ 14 ⇒ en az 14 katlama')],
 puf='Katlanarak artan niceliklerde başlangıç değeri de üslüdür; kalınlığı 2ⁿ⁻⁴ gibi tek üslü ifadeyle yazıp 2’nin kuvvetlerinden eşiği bul.')

# ---------- 13 · zor · mikroskop ----------
hucre=Fr(6,100)/(3*10**3); assert hucre==Fr(2,10**5)
assert Fr(1,100)/hucre==500
assert hucre/Fr(1,100)==Fr(2,10**3) and Fr(1,10**4)/hucre==5 and Fr(1,10**3)/hucre==50
assert Fr(1,100)/Fr(2,10**6)==5000                          # −2 − 3 = −6 sanmış
mk(P,'0013',tipId='usb-bilimsel',tip='Bilimsel gösterim ve 10’un kuvvetleri',z='zor',alt='Bilimsel Gösterim',kaz='Görüntü boyutu ve büyütme oranından gerçek boyutu bulup birim çevirerek hücre sayısını hesaplar.',kalip='hikâyeli',adim=4,
 kart='K-USLB-13 (mikroskop ve bilimsel gösterimle bölme) · büyütme 3 × 10³, görüntü 6 × 10⁻² m, 1 cm',
 metin='Bir mikroskop cisimleri 3 × 10³ kat büyütmektedir. Bu mikroskopla özdeş hücrelerden biri incelendiğinde hücrenin görüntüsünün çapı 6 × 10⁻² metre ölçülmüştür.\nBu hücrelerden kaç tanesi aralarında boşluk kalmadan yan yana dizilirse dizinin uzunluğu 1 santimetre olur?',
 dogru=500,yan=[(Fr(2,10**3),'Oranı ters kurmuş: hücre çapını 1 cm’ye bölmüş (2 × 10⁻⁵ ÷ 10⁻² = 2 × 10⁻³).','dikkat'),(5,'1 cm’yi 10⁻⁴ m almış; 1 cm = 10⁻² m’dir.','bilgi'),(50,'1 cm’yi 1 mm (10⁻³ m) ile karıştırmış: 10⁻³ ÷ 2 × 10⁻⁵ = 50.','bilgi'),(5000,'Hücre çapını bulurken 10⁻² ÷ 10³ için −2 − 3 = −6 yazmış (2 × 10⁻⁶ m); doğru üs −5’tir.','islem')],
 istenen='Dizinin 1 cm olması için gereken hücre sayısı.',
 ip=['Gerçek çap = görüntü çapı ÷ büyütme; sonra 1 cm = 10⁻² m’yi gerçek çapa böl.'],
 bilgi=[BIL,BIRIM,CRP],
 ad=[A('Gerçek çapı bul','Görüntü, gerçek boyutun büyütme katıdır; bu yüzden bölünür.','(6 × 10⁻²) ÷ (3 × 10³) = 2 × 10⁻⁵ m'),A('Birimi eşitle','1 cm = 10⁻² m.','uzunluk = 10⁻² m'),A('Oranı kur','Hücre sayısı, toplam uzunluğun bir hücrenin çapına oranıdır.','10⁻² ÷ (2 × 10⁻⁵) = 0,5 × 10³'),A('Sonucu yaz','0,5 × 10³ = 5 × 10².','5 × 10² = 500 hücre')],
 puf='Mikroskop sorularında önce görüntüyü büyütmeye böl, sonra birimleri aynı birime getirip bilimsel gösterimde böl.')

# ---------- 14 · zor · 2ᵃ × 3ᵇ sayıları ----------
L14=sorted(2**a*3**b for a in range(0,8) for b in range(0,6) if 2**a*3**b<100); assert len(L14)==len(set(L14))==20
c_b=lambda bmax,amin=0,bmin=0:sum(1 for a in range(0,8) for b in range(bmin,bmax+1) if 2**a*3**b<100 and a>=amin)
assert c_b(4)==20 and c_b(4)-1==19 and c_b(2)==17 and c_b(1)==13 and c_b(4,1,1)==9
assert [sum(1 for a in range(0,8) if 2**a*3**b<100) for b in range(5)]==[7,6,4,2,1]
mk(P,'0014',tipId='usb-tanimli',tip='Tanımlı üslü sayı kümesinde sayma',z='zor',alt='Tanımlı Sayı Kümesi',kaz='Tanımlanan 2ᵃ × 3ᵇ biçimindeki sayıları üs çiftlerine göre gruplayıp sınırın altında kalanları sayar.',kalip='yeni nesil',adim=4,
 kart='K-USLB-14 (2ᵃ × 3ᵇ biçimli sayıları sayma) · “ikiüçlü sayı”, 100’den küçük kaç tane',
 metin='a ve b negatif olmayan tam sayılar olmak üzere, 2ᵃ × 3ᵇ biçiminde yazılabilen doğal sayılara “ikiüçlü sayı” denir. Örneğin 1 = 2⁰ × 3⁰ ve 12 = 2² × 3¹ sayıları ikiüçlü sayıdır.\n100’den küçük kaç tane ikiüçlü sayı vardır?',
 dogru=20,yan=[(9,'a ve b’yi en az 1 almış (a ≥ 1, b ≥ 1); 2ᵃ yalnız ya da 3ᵇ yalnız olan sayılar (1, 2, 4, 3, 9, …) da ikiüçlüdür.','bilgi'),(13,'Yalnız b = 0 ve b = 1 gruplarını saymış (7 + 6); b = 2, 3, 4 gruplarını unutmuş.','dikkat'),(17,'b = 0, 1, 2 gruplarını sayıp (7 + 6 + 4) 27 ve 54’ü, 81’i unutmuş.','dikkat'),(19,'1 = 2⁰ × 3⁰ sayısını ikiüçlü saymamış; a = b = 0 da tanıma uyar.','dikkat')],
 istenen='100’den küçük ikiüçlü sayıların adedi.',
 ip=['b = 0, 1, 2, … için 2ᵃ × 3ᵇ < 100 koşulunu sağlayan a değerlerini say.'],
 bilgi=[CRP,B('Sıfırıncı kuvvet','Sıfırdan farklı her sayının 0. kuvveti 1’dir. Örnek: 2⁰ = 1 · 3⁰ = 1 · 2⁰ × 3² = 9')],
 ad=[A('b’ye göre grupla','Her b için 3ᵇ sabit; 2ᵃ × 3ᵇ < 100 olan a değerleri aranır.','3⁰ = 1 · 3¹ = 3 · 3² = 9 · 3³ = 27 · 3⁴ = 81 (3⁵ = 243 > 100)'),A('b = 0, 1 grupları','Çarpan 1: 1, 2, 4, 8, 16, 32, 64. Çarpan 3: 3, 6, 12, 24, 48, 96.','7 + 6 = 13 sayı'),A('b = 2, 3, 4 grupları','Çarpan 9: 9, 18, 36, 72. Çarpan 27: 27, 54. Çarpan 81: 81.','4 + 2 + 1 = 7 sayı'),A('Topla','Hiçbir sayı iki grupta yer almaz (asal çarpanlara ayrılış tektir).','13 + 7 = 20')],
 puf='Tanımlı biçimdeki sayıları saymak için bir üssü sabitleyip diğerinin alabileceği değerleri say; hiçbir durumu (a = 0, b = 0) atlama.')

bitir(P,'usluiki','mat|Üslü Sayılar')
from collections import Counter
print(Counter(q['cevap']['sik'] for q in P.ANA),Counter(q['zorluk'] for q in P.ANA))
