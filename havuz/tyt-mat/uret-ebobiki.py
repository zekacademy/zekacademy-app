"""EBOB – EKOK (2. parti) · hafif mod: 14 ana soru, kardeş yok, ipucu 1. Her cevap Python'da hesaplanıp assert edilir."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_mat as H
from _hafif_mat import *
from math import gcd,lcm
from collections import Counter
H.KONU='EBOB – EKOK'
P=Parti('ebobiki','EBOB – EKOK','mat|Ebob – ekok')
UK='mat|Ebob – ekok'
KY='ÖSYM 2018–2025 (EBOB–EKOK, bölen sayısı) · yayın soru bankaları: Bölünebilme Kuralları, Sayı Kümeleri (yalnız mantık) · MEB 9. sınıf'

def bolenler(n): return [d for d in range(1,n+1) if n%d==0]
def nb(n): return len(bolenler(n))
def tek_say(f,lo,hi): return sum(1 for x in range(lo,hi+1) if f(x))

ASAL=B('Asal sayı ve asal çarpan','1’den büyük ve yalnız 1 ile kendisine bölünen sayıya asal sayı denir (2, 3, 5, 7, 11 …). Bir sayıyı asal sayıların çarpımı olarak yazmaya asal çarpanlara ayırma denir. Örnek: 72 = 2 × 2 × 2 × 3 × 3 = 2³ × 3²')
BS=B('Pozitif bölen sayısı','asal çarpanlara ayrılmış N = aᵐ × bⁿ × cᵖ için pozitif bölen sayısı (m + 1)(n + 1)(p + 1)’dir. Örnek: 12 = 2² × 3 → (2 + 1)(1 + 1) = 6 bölen: 1, 2, 3, 4, 6, 12')
EB=B('EBOB','iki sayıyı birlikte bölen en büyük sayıdır. Asal çarpanlarda ortak asalların küçük üssü alınır. Örnek: EBOB(12, 18) = 6')
EK=B('EKOK','iki sayının ortak katlarının en küçüğüdür. Asal çarpanlarda tüm asalların büyük üssü alınır. Örnek: EKOK(12, 18) = 36')
IL=B('EBOB ile EKOK ilişkisi','a × b = EBOB(a, b) × EKOK(a, b). Örnek: 12 × 18 = 216 = 6 × 36')
AA=B('Aralarında asal','EBOB’u 1 olan iki sayıya aralarında asal denir; bunların EKOK’u çarpımlarına eşittir. Örnek: EBOB(8, 15) = 1, EKOK(8, 15) = 120')
OB=B('EBOB ve ortak bölenler','EBOB, iki sayıyı birlikte bölen en büyük sayıdır ve ortak bölenler EBOB’un bölenleridir. Örnek: EBOB(12, 18) = 6; ortak bölenler 6’nın bölenleri olan 1, 2, 3, 6’dır')
TC=B('Tek ve çift sayı','birler basamağı 0, 2, 4, 6 ya da 8 olan sayı çifttir, 1, 3, 5, 7, 9 olan sayı tektir. Çift bölen, 2’yi asal çarpan olarak içerir')
OK=B('Ortak katlar','iki sayının ortak katları EKOK’un katlarıdır. Örnek: 4 ve 6’nın ortak katları 12, 24, 36 … (12’nin katları)')
KL=B('Kalan koşulu','N, 9’a bölündüğünde 4 kalıyorsa N = 9k + 4’tür; bölenden kalan kadar eksik de yazılabilir: N + 5 = 9(k + 1). Örnek: 31 = 9 × 3 + 4 ve 31 + 5 = 36 = 9 × 4')

# ---------- kartlar ----------
kart('K-EBKB-01','Asal çarpanlar ve bölen sayısı','Sayı asal çarpanlarına ayrılır; üslerin bir fazlası çarpılarak bölen sayısı bulunur. Çift/tek bölen ve en küçük sayı koşullarında hangi asalın hangi üslerde bulunması gerektiği yazılır.','Üs toplamını ya da üs çarpımını bölen sayısı sanmak; 2⁰ ya da 3⁰ gibi 1’i veren üssü unutmak; koşulu (çift, 18’in katı) atlamak.','orta','düz',3,'ekb-bolen','Asal çarpanlara ayırma ve pozitif bölen sayısı','ÖSYM 2019–2024 (bölen sayısı, asal çarpan) · yayın: bölen sayısı, kuvvetleri toplamı')
kart('K-EBKB-02','Aralarında asal ve EBOB × EKOK = a × b','İki sayı a = d·x, b = d·y yazılır (x, y aralarında asal); EBOB × EKOK = a × b ve asal çarpan üslerinden EBOB/EKOK kurulur. Aralarında asal sayıların özellikleri öncüllü sorulur.','EKOK yerine EBOB (ya da çarpım) vermek; aralarında asal sayısını sayarken ortak katları iki kez elemek; asalları üssüz almak.','orta','öncüllü',3,'ekb-iliski','Aralarında asal sayılar ve EBOB × EKOK = a × b','ÖSYM 2018–2025 (EBOB–EKOK ilişkisi) · yayın: aralarında asal, EBOB + EKOK = k')
kart('K-EBKB-03','EBOB ile en az parça (çevre)','Aralık ya da parça uzunluğu hepsinin EBOB’udur; çevresel dizilimde köşe sayısı ile parça sayısı eşittir (çevre / aralık).','Çevresel dizilimde sona 1 eklemek; köşelerdeki parçayı iki kez saymak; EBOB’u sayı sanmak.','kolay','hikâyeli',2,'ekb-parca','Eş aralıklarla çevre dizilimi (EBOB)','ÖSYM (en büyük eş parça) · yayın: çevreye ağaç dikme')
kart('K-EBKB-04','Birlikte karşılaşma ve tur sayısı (EKOK)','Hareketler ya da çarklar ilk kez birlikte başlangıç konumunda buluşurken geçen süre/diş EKOK’tur; tur sayısı = EKOK / periyot. İkili ve üçlü çakışmalarda kapsama–dışlama yapılır.','EKOK’u tur sayısı sanmak; bir koşucuyu toplamda unutmak; üçlü anı üç çiftin her birinde saymak.','zor','yeni nesil',4,'ekb-periyot','Koşu, dişli çark ve çakışma sayısı','ÖSYM 2020–2025 (periyot, EKOK) · yayın: koşu pisti, çark, zil')
kart('K-EBKB-05','Ortak kat sayma ve kalan koşulu','Kalan koşullu sayılar N = EKOK × k ± c biçimindedir; verilen aralıkta kaç tane olduğu k’nın sınırlarından bulunur (uç değerler dahil mi diye bak).','Aralıktaki ortak kat sayısını EBOB ile saymak; uç değerleri unutmak ya da fazla saymak; kalanı eklemek yerine çıkarmak.','orta','düz',3,'ekb-kalan','Ortak katları sayma ve kalan koşulu','ÖSYM (kalan, ortak kat) · yayın: aralıkta kaç sayı')

# ---------- 01 · kolay · bölen sayısı ----------
n=720; assert 720==2**4*3**2*5 and nb(n)==30
assert 4+2+1==7 and 4*2*1==8 and 5+3+2==10 and len({2,3,5})==3
mk(P,'0001',tipId='ekb-bolen',tip='Asal çarpanlara ayırma ve pozitif bölen sayısı',z='kolay',alt='Pozitif Bölen Sayısı',kaz='Bir sayıyı asal çarpanlarına ayırıp pozitif bölenlerinin sayısını bulur.',kalip='düz',adim=2,
 kart='K-EBKB-01 (asal çarpan, bölen sayısı) · tek asal çarpanlı üslü yazım, doğrudan bölen sayısı',
 metin='720 sayısının pozitif tam bölenlerinin sayısı kaçtır?',
 dogru=30,yan=[(3,'Farklı asal çarpanların sayısını (2, 3, 5) bölen sayısı sanmış.','bilgi'),(7,'Üsleri toplamış (4 + 2 + 1); “üs + 1” çarpımını kullanmamış.','bilgi'),(8,'Üsleri çarpmış (4 × 2 × 1); her üsse 1 eklemeyi unutmuş.','bilgi'),(10,'Her üssün bir fazlasını almış ama çarpmak yerine toplamış (5 + 3 + 2).','islem')],
 istenen='720’nin pozitif bölenlerinin adedi.',
 ip=['720’yi asal çarpanlarına ayır; her asalın üssüne 1 ekleyip sonuçları çarp.'],
 bilgi=[ASAL,BS],
 ad=[A('Asal çarpanlara ayır','720 sırayla 2, 3, 5 asallarına bölünerek 1’e indirilir.','720 = 2 × 360 = 2⁴ × 45 = 2⁴ × 3² × 5'),A('Üslere 1 ekle','Her asalın bölende alabileceği üs sayısı, üssünün bir fazlasıdır (0’dan üsse kadar).','2⁴ → 5 seçenek · 3² → 3 seçenek · 5¹ → 2 seçenek'),A('Çarp','Seçimler birbirinden bağımsız olduğundan çarpılır.','5 × 3 × 2 = 30')],
 puf='N = aᵐ × bⁿ × … ise bölen sayısı (m + 1)(n + 1)… ; üsleri toplamak ya da çarpmak yanlıştır.')

# ---------- 02 · kolay · EBOB × EKOK ----------
a2,b2=12,30; assert gcd(a2,b2)==6 and a2*b2==360 and lcm(a2,b2)==60
assert 360//6==60 and 360//2==180 and 360*6==2160
mk(P,'0002',tipId='ekb-iliski',tip='Aralarında asal sayılar ve EBOB × EKOK = a × b',z='kolay',alt='EBOB – EKOK İlişkisi',kaz='İki sayının çarpımı ile EBOB’u bilindiğinde EKOK’unu ilişkiden bulur.',kalip='düz',adim=2,
 kart='K-EBKB-02 (EBOB × EKOK = a × b) · çarpım ve EBOB verilmiş, EKOK isteniyor',
 metin='İki pozitif tam sayının çarpımı 360, en büyük ortak böleni 6’dır.\nBuna göre bu iki sayının en küçük ortak katı kaçtır?',
 dogru=60,yan=[(6,'EKOK yerine verilen EBOB’u cevap yazmış.','dikkat'),(180,'Çarpımı yalnız 2’ye bölmüş; EBOB’a (6) bölmesi gerektiğini atlamış.','islem'),(360,'EBOB × EKOK ilişkisini kullanmamış; verilen çarpımı EKOK sanmış.','bilgi'),(2160,'EKOK = çarpım × EBOB demiş (360 × 6); bölmesi gerekirken çarpmış.','islem')],
 istenen='İki sayının EKOK’u.',
 ip=['Çarpım, EBOB ve EKOK arasında bir ilişki kurar; 12 ile 30 gibi bir örnekte dene.'],
 bilgi=[EB,EK,IL],
 ad=[A('İlişkiyi yaz','İki sayının çarpımı EBOB × EKOK’a eşittir.','a × b = EBOB × EKOK · 360 = 6 × EKOK'),A('EKOK’u çek','Çarpımı EBOB’a böl.','EKOK = 360 ÷ 6 = 60'),A('Örnekle doğrula','12 ile 30 için EBOB 6, çarpım 360’tır; EKOK 60 çıkar.','12 × 30 = 360 = 6 × 60')],
 puf='EKOK = (a × b) ÷ EBOB; çarpımı EBOB’a bölmek, iki sayıyı tek tek bulmadan sonuca götürür.')

# ---------- 03 · kolay · çevre dizilimi ----------
k3,u3=60,36
d3=gcd(k3,u3); cevre=2*(k3+u3); assert d3==12 and cevre==192 and cevre//d3==16
assert min(cevre//d for d in range(1,min(k3,u3)+1) if k3%d==0 and u3%d==0)==16
assert (k3+u3)//d3==8 and cevre//d3+1==17 and 2*(k3//d3+1)+2*(u3//d3+1)==20
mk(P,'0003',tipId='ekb-parca',tip='Eş aralıklarla çevre dizilimi (EBOB)',z='kolay',alt='Çevreye Ağaç Dikme',kaz='Bir dikdörtgenin çevresine köşelerde de bulunacak biçimde eşit aralıklı dizilen en az nesne sayısını EBOB ile bulur.',kalip='hikâyeli',adim=3,
 kart='K-EBKB-03 (çevre dizilimi) · dikdörtgen çevresine köşelerde ağaç, en az ağaç',
 metin='Kenar uzunlukları 60 m ve 36 m olan dikdörtgen biçimindeki bir parkın çevresine ağaç dikilecektir. Dört köşenin her birine bir ağaç dikilecek, ardışık iki ağaç arasındaki uzaklık her yerde eşit ve metre cinsinden tam sayı olacaktır.\nBuna göre bu iş için en az kaç ağaç gerekir?',
 dogru=16,yan=[(8,'Çevre yerine yarı çevreyi (96 m) kullanıp 96 ÷ 12 = 8 bulmuş.','dikkat'),(12,'Sorulan ağaç sayısı yerine ağaçlar arası uzaklığı (EBOB = 12) vermiş.','dikkat'),(17,'Çevre kapalı bir hat olduğu halde 192 ÷ 12 = 16’ya bir ağaç daha eklemiş.','bilgi'),(20,'Uzun kenara 6, kısa kenara 4 ağaç sayıp 2 × (6 + 4) = 20 yazmış; köşelerdeki ağaçları iki kez saymış.','islem')],
 istenen='En az ağaç sayısı.',
 ip=['Aralık en çok kaç metre olabilir? Köşeler ağaçla dolu olduğu için aralık her iki kenarı da bölmelidir.'],
 bilgi=[EB],
 ad=[A('Aralığı belirle','Köşelere ağaç gelecek, bu yüzden aralık hem 60’ı hem 36’yı bölmelidir. Ağaç sayısı en az olsun diye aralık en büyük olmalıdır.','Aralık = EBOB(60, 36) = 12 m'),A('Çevreyi bul','Parkın çevresi iki uzun ve iki kısa kenardan oluşur.','Çevre = 2 × (60 + 36) = 192 m'),A('Ağaç sayısını bul','Kapalı bir çevrede ağaç sayısı, aralık sayısına eşittir.','192 ÷ 12 = 16 ağaç')],
 puf='Kapalı bir hatta (çevre) ağaç sayısı aralık sayısına eşittir; “+1” yalnız iki ucu açık yolda eklenir.')

# ---------- 04 · orta · çift bölen sayısı ----------
n=540; assert 540==2**2*3**3*5 and nb(n)==24
ce=[d for d in bolenler(n) if d%2==0]; te=[d for d in bolenler(n) if d%2==1]
assert len(ce)==16 and len(te)==8 and 24//2==12 and 2+3+1==6
mk(P,'0004',tipId='ekb-bolen',tip='Asal çarpanlara ayırma ve pozitif bölen sayısı',z='orta',alt='Çift Bölenlerin Sayısı',kaz='Bölen sayısı formülünü çift bölen koşuluna uyarlar.',kalip='düz',adim=3,
 kart='K-EBKB-01 (bölen sayısı) · yalnız çift olan bölenlerin sayısı',
 metin='540 sayısının pozitif tam bölenlerinden kaç tanesi çift sayıdır?',
 dogru=16,yan=[(6,'Asal çarpanların üslerini toplamış (2 + 3 + 1); bölen sayısı formülünü kullanmamış.','bilgi'),(8,'Tek bölenlerin sayısını (2’siz bölenler) bulmuş; çift bölenleri sormuş olduğunu atlamış.','dikkat'),(12,'Tüm bölenlerin sayısını yarıya bölmüş (24 ÷ 2); çift bölenlerin yarıdan fazla olduğunu görmemiş.','bilgi'),(24,'Bütün pozitif bölenleri saymış; çift olma koşulunu uygulamamış.','dikkat')],
 istenen='540’ın çift olan pozitif bölenlerinin adedi.',
 ip=['Bölen çift olacağı için 2’nin üssü en az 1 olmalıdır; 2’nin üssü için kaç seçenek kalır?'],
 bilgi=[ASAL,BS,TC],
 ad=[A('Asal çarpanlara ayır','540’ı 2, 3, 5 asallarına ayır.','540 = 2² × 3³ × 5'),A('Çift olma koşulunu yaz','Bölen çift olmalı; 2’nin üssü 0 olamaz, 1 ya da 2 olabilir. 3’ün üssü 0, 1, 2, 3; 5’in üssü 0, 1 olabilir.','2 için 2 · 3 için 4 · 5 için 2 seçenek'),A('Çarp','Her asal için seçenek sayıları çarpılır.','2 × 4 × 2 = 16'),A('Kontrol et','Tüm bölenler 3 × 4 × 2 = 24; tek bölenler 2’siz olan 3³ × 5’in bölenleri, yani 4 × 2 = 8.','24 − 8 = 16')],
 puf='Çift bölen sayısı = toplam bölen sayısı − tek bölen sayısı; tek bölenler 2’yi içermeyen çarpanlardan gelir.')

# ---------- 05 · orta · aralarında asal olmayanları sayma ----------
n=30; aa=[x for x in range(1,n+1) if gcd(x,n)==1]; assert len(aa)==8
na=[x for x in range(1,n+1) if gcd(x,n)>1]; assert len(na)==22
assert len([x for x in range(1,31) if x%2==0])==15 and len([x for x in range(1,31) if x%3==0])==10
assert 15+10-5==20 and 15+10+6==31
mk(P,'0005',tipId='ekb-iliski',tip='Aralarında asal sayılar ve EBOB × EKOK = a × b',z='orta',alt='Aralarında Asal Olmayanları Sayma',kaz='Bir sayıyla aralarında asal olmayan sayıların adedini asal çarpanları üzerinden sayar.',kalip='düz',adim=4,
 kart='K-EBKB-02 (aralarında asal) · 1’den 30’a 30 ile aralarında asal olmayanların sayısı',
 metin='1’den 30’a kadar (1 ve 30 dahil) olan pozitif tam sayılardan kaç tanesi 30 ile aralarında asal değildir?',
 dogru=22,yan=[(8,'30 ile aralarında asal olanları (8 tane) saymış; sorudaki “değildir” koşulunu atlamış.','dikkat'),(10,'Yalnız 3’ün katlarını (10 tane) saymış; 2’nin ve 5’in katlarını atlamış.','bilgi'),(15,'Yalnız çift sayıları (15 tane) saymış; 3’ün ve 5’in katlarını atlamış.','bilgi'),(20,'5’in katlarını unutup 2’nin ve 3’ün katlarını (15 + 10 − 5) saymış.','bilgi')],
 istenen='30 ile EBOB’u 1’den büyük olan sayıların adedi.',
 ip=['30 = 2 × 3 × 5; 30 ile ortak böleni olan sayı 2’ye, 3’e ya da 5’e bölünür. Kolay yol: aralarında asal olanları say.'],
 bilgi=[ASAL,AA],
 ad=[A('Asal çarpanları bul','30’un asal çarpanları 2, 3 ve 5’tir; bir sayı bunlardan birine bölünüyorsa 30 ile ortak böleni vardır.','30 = 2 × 3 × 5'),A('Aralarında asalları listele','Hiçbirine bölünmeyen sayılar 30 ile aralarında asaldır.','1, 7, 11, 13, 17, 19, 23, 29 → 8 sayı'),A('Eksik tamamla','Geri kalanlar aralarında asal değildir.','30 − 8 = 22'),A('Doğrula','2’nin katı 15, 3’ün katı 10, 5’in katı 6 tanedir; ortak sayılanlar çıkarılınca 22 kalır.','15 + 10 + 6 − 5 − 3 − 2 + 1 = 22')],
 puf='“Aralarında asal olmayan” sorulunca aralarında asal olanları sayıp toplamdan çıkarmak çoğu zaman daha hızlıdır.')

# ---------- 06 · orta · öncüllü aralarında asal ----------
I=II=III=True
cI=cII=cIII=None
okI=okII=okIII=True
for a in range(2,80):
    for b in range(1,a):
        if gcd(a,b)==1:
            okI=okI and gcd(a,a+b)==1
            okII=okII and lcm(a,b)==a*b
            okIII=okIII and gcd(a+b,a-b)==1
assert okI and okII and not okIII and gcd(3+1,3-1)==2
mk(P,'0006',tipId='ekb-iliski',tip='Aralarında asal sayılar ve EBOB × EKOK = a × b',z='orta',alt='Aralarında Asal Sayıların Özellikleri',kaz='Aralarında asal iki sayıyla ilgili ifadelerin her zaman doğru olup olmadığını örnek ve ilişkiyle inceler.',kalip='öncüllü',adim=3,
 kart='K-EBKB-02 (aralarında asal) · EBOB(a, a + b), EBOB(a + b, a − b), EKOK = a × b ifadeleri',
 metin='a ve b pozitif tam sayılar olmak üzere a > b ve EBOB(a, b) = 1’dir.\nBuna göre,\nI. EBOB(a, a + b) = 1\nII. EBOB(a + b, a − b) = 1\nIII. EKOK(a, b) = a × b\nifadelerinden hangileri kesinlikle doğrudur?',
 dogru='I ve III',sira=['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III'],
 yan=[('Yalnız I','III’ü çözmemiş; aralarında asal sayıların EKOK’unun çarpımlarına eşit olduğunu bilmiyor.','bilgi'),('Yalnız II','I’i denemeden geçmiş, II’yi tek örnekle (a = 4, b = 1) doğru sanmış.','dikkat'),('I ve II','II’yi doğru sanmış; a = 3, b = 1 için EBOB(4, 2) = 2 olduğunu denememiş.','dikkat'),('I, II ve III','II’yi yalnız a = 4, b = 1 gibi bir örnekle denemiş (EBOB(5, 3) = 1); a = 3, b = 1 karşı örneğini bulmamış.','dikkat')],
 istenen='Kesinlikle doğru olan ifadeler.',
 ip=['II için a = 3, b = 1 gibi küçük bir değer dene; I için a ile a + b’nin ortak bölenlerini düşün.'],
 bilgi=[AA],
 ad=[A('I’i incele','a ile a + b’yi bölen bir sayı, farkları olan b’yi de böler; yani a ve b’nin ortak böleni olur. Ortak bölen yalnız 1 olduğundan I doğrudur.','Ortak bölen ⇒ a ve b’nin ortak böleni ⇒ 1'),A('II’yi dene','Karşı örnek aramak yeterlidir: a = 3, b = 1 aralarında asal ve 3 > 1, fakat EBOB(4, 2) = 2.','EBOB(3 + 1, 3 − 1) = EBOB(4, 2) = 2 ≠ 1'),A('III’ü incele','Aralarında asal sayılarda EBOB = 1 olduğundan EKOK çarpıma eşittir.','a × b = 1 × EKOK ⇒ EKOK = a × b'),A('Sonucu yaz','I ve III kesinlikle doğru, II her zaman doğru değil.','Cevap: I ve III')],
 puf='“Kesinlikle doğru” sorularında bir karşı örnek ifadeyi eler; doğru saydığın ifadeyi ise ilişkiyle (ortak bölen ⇒ ortak bölen) kanıtla.')

# ---------- 07 · orta · aralıkta ortak kat sayma ----------
lo,hi=100,400
oku=[x for x in range(lo+1,hi) if x%12==0 and x%18==0]; assert len(oku)==9 and oku[0]==108 and oku[-1]==396 and lcm(12,18)==36
assert hi//36==11 and hi//36-1==10 and len([x for x in range(lo+1,hi) if x%12==0])==25
assert len([x for x in range(lo+1,hi) if x%6==0])==50
mk(P,'0007',tipId='ekb-kalan',tip='Ortak katları sayma ve kalan koşulu',z='orta',alt='Aralıkta Ortak Kat Sayma',kaz='İki sayıya birlikte bölünen sayıların bir aralıktaki adedini EKOK ile bulur.',kalip='düz',adim=3,
 kart='K-EBKB-05 (ortak kat sayma) · 12 ve 18’e bölünebilen, 100 ile 400 arasında',
 metin='100’den büyük, 400’den küçük kaç tane doğal sayı hem 12’ye hem 18’e tam olarak bölünür?',
 dogru=9,yan=[(25,'Yalnız 12’nin katlarını (108’den 396’ya) saymış; 18’e de bölünme koşulunu atlamış.','dikkat'),(10,'400 ÷ 36’nın tam kısmı olan 11’den yalnız 1 çıkarmış; 100’ün altındaki 36’nın katlarının (36, 72) sayısını (2) düşmemiş.','islem'),(11,'400 ÷ 36’nın tam kısmını (11) cevap almış; 100’ün altındaki ortak katları (36, 72) çıkarmamış.','dikkat'),(50,'EKOK yerine EBOB’u (6) kullanıp 6’nın katlarını saymış.','bilgi')],
 istenen='Aralıktaki ortak katların adedi.',
 ip=['Hem 12’ye hem 18’e bölünen sayılar, 12 ile 18’in EKOK’unun katlarıdır.'],
 bilgi=[EK,OK],
 ad=[A('EKOK’u bul','12 = 2² × 3 ve 18 = 2 × 3²; büyük üsler alınır.','EKOK = 2² × 3² = 36'),A('Aralığı sınırla','Ortak katlar 36’nın katlarıdır. 100’den büyük ilk kat 108 (36 × 3), 400’den küçük son kat 396 (36 × 11).','108 = 36 × 3 · 396 = 36 × 11'),A('Say','3’ten 11’e kadar olan çarpanların sayısı.','11 − 3 + 1 = 9')],
 puf='a’dan büyük, b’den küçük m’nin katları ⌊(b − 1)/m⌋ − ⌊a/m⌋ kadardır (b, m’nin katıysa b sayılmaz).')

# ---------- 08 · orta · koşucu turları ----------
t8=[24,36,40]; E8=lcm(*t8); tur=[E8//t for t in t8]
assert E8==360 and tur==[15,10,9] and sum(tur)==34 and 720//24+720//36+720//40==68 and 15+10==25
mk(P,'0008',tipId='ekb-periyot',tip='Koşu, dişli çark ve çakışma sayısı',z='orta',alt='Koşucuların Tur Sayıları',kaz='Sabit hızla koşan üç kişinin ilk kez başlangıç noktasında buluştuğu süreyi EKOK ile bulup tur sayılarını hesaplar.',kalip='hikâyeli',adim=3,
 kart='K-EBKB-04 (koşu pisti, EKOK) · tur süreleri 24, 36, 40 sn; tamamlanan turların toplamı',
 metin='Çembersel bir pistte üç koşucu, başlangıç noktasından aynı anda ve aynı yöne doğru sabit hızlarla koşmaya başlıyor. Koşucuların birer tur atma süreleri sırasıyla 24 saniye, 36 saniye ve 40 saniyedir.\nÜç koşucu başlangıç noktasında ilk kez yeniden bir araya geldiğinde, üçünün tamamladığı tur sayılarının toplamı kaçtır?',
 dogru=34,yan=[(15,'Yalnız en hızlı koşucunun (24 saniyelik) tur sayısını bulmuş.','dikkat'),(68,'Buluşma süresini 720 saniye bulup tur sayılarını 30 + 20 + 18 toplamış.','islem'),(25,'40 saniyede bir tur atan koşucunun turunu toplama katmamış (15 + 10).','dikkat'),(360,'Buluşma süresini (EKOK = 360 saniye) tur sayıları toplamı yerine vermiş.','dikkat')],
 istenen='İlk buluşmaya kadar tamamlanan turların toplamı.',
 ip=['Üçü ancak her birinin tur süresinin ortak katı kadar zaman geçince başlangıçta buluşur; ilk kez olduğu için en küçüğü gerekir.'],
 bilgi=[EK],
 ad=[A('Buluşma süresi','Başlangıçta buluşma için geçen süre, üç tur süresinin de katı olmalıdır; ilk kez olduğu için en küçük ortak kat alınır.','EKOK(24, 36, 40) = 360 saniye'),A('Tur sayıları','Her koşucunun turu = süre ÷ tur süresi.','360 ÷ 24 = 15 · 360 ÷ 36 = 10 · 360 ÷ 40 = 9'),A('Topla','Üçünün tur sayıları toplanır.','15 + 10 + 9 = 34')],
 puf='İlk buluşmada her koşucunun tur sayısı EKOK ÷ tur süresidir; soru “tur sayısı” diyorsa EKOK’un kendisi cevap değildir.')

# ---------- 09 · orta · dişli çark ----------
d1,d2=24,56; E9=lcm(d1,d2)
assert E9==168 and E9//d1==7 and E9//d2==3 and 7+3==10 and gcd(d1,d2)==8
mk(P,'0009',tipId='ekb-periyot',tip='Koşu, dişli çark ve çakışma sayısı',z='orta',alt='Dişli Çarklar',kaz='Birbirine geçmiş dişli çarkların işaretli dişlerinin yeniden karşılaşması için gereken dönüş sayısını EKOK ile bulur.',kalip='hikâyeli',adim=3,
 kart='K-EBKB-04 (dişli çark, EKOK) · 24 ve 56 dişli çarklarda küçük çarkın tur sayısı',
 metin='Diş sayıları 24 ve 56 olan iki dişli çark birbirine geçmiştir. Başlangıçta küçük çarkın işaretli dişi ile büyük çarkın işaretli dişi birbirine değmektedir.\nÇarklar döndürülmeye başlandığında bu iki işaretli diş ilk kez yeniden birbirine değdiği anda küçük çark kaç tur atmış olur?',
 dogru=7,yan=[(3,'Büyük çarkın tur sayısını (168 ÷ 56) bulmuş; soru küçük çarkı soruyor.','dikkat'),(10,'İki çarkın tur sayılarını toplamış (7 + 3).','dikkat'),(8,'EBOB(24, 56) = 8’i tur sayısı sanmış.','bilgi'),(168,'İşaretli dişlerin yeniden değdiği anda geçen diş sayısını (EKOK) tur sayısı sanmış.','dikkat')],
 istenen='Küçük çarkın attığı tur sayısı.',
 ip=['Çarklar birbirine geçtiği için her birinde aynı sayıda diş yer değiştirir; bu diş sayısı ikisinin de diş sayısının katı olunca işaretliler yeniden karşılaşır.'],
 bilgi=[EK],
 ad=[A('Geçen diş sayısı','İki çarkta eşit sayıda diş yer değiştirir. İşaretli dişler yeniden değdiğinde bu sayı iki diş sayısının da katıdır; ilk kez için en küçük ortak kat alınır.','EKOK(24, 56) = 168 diş'),A('Küçük çarkın turu','Küçük çarkın tur sayısı = geçen diş ÷ 24.','168 ÷ 24 = 7'),A('Kontrol et','Büyük çark 168 ÷ 56 = 3 tur atmıştır; ikisi de tam sayı.','7 ve 3 tam tur')],
 puf='Dişli çarklarda geçen diş sayısı ortaktır; tur sayısı = EKOK ÷ diş sayısı (küçük çark daha çok döner).')

# ---------- 10 · orta · ortak bölen sayısı ----------
a10,b10=144,180; g10=gcd(a10,b10)
ob=[d for d in range(1,a10+1) if a10%d==0 and b10%d==0]
assert g10==36 and len(ob)==9 and nb(g10)==9 and nb(a10)==15 and nb(b10)==18 and 15+18==33
asalort=[p for p in (2,3,5) if a10%p==0 and b10%p==0]; assert len(asalort)==2
mk(P,'0010',tipId='ekb-bolen',tip='Asal çarpanlara ayırma ve pozitif bölen sayısı',z='orta',alt='Ortak Bölenlerin Sayısı',kaz='İki sayının ortak pozitif bölenlerinin sayısını EBOB’un bölen sayısı olarak bulur.',kalip='düz',adim=3,
 kart='K-EBKB-01 (bölen sayısı) · iki sayının ortak pozitif bölenlerinin sayısı',
 metin='144 ile 180 sayılarının her ikisini de tam bölen kaç tane pozitif tam sayı vardır?',
 dogru=9,yan=[(15,'Yalnız 144’ün pozitif bölen sayısını bulmuş.','dikkat'),(18,'Yalnız 180’in pozitif bölen sayısını bulmuş.','dikkat'),(33,'İki sayının bölen sayılarını toplamış (15 + 18); ortak bölenleri saymamış.','bilgi'),(36,'Ortak bölenlerin en büyüğünü (EBOB = 36) bulup adedini sormayı atlamış.','dikkat')],
 istenen='144 ve 180’in ortak pozitif bölenlerinin adedi.',
 ip=['İki sayının ortak bölenleri, EBOB’un bölenleridir.'],
 bilgi=[ASAL,OB,BS],
 ad=[A('Asal çarpanlara ayır','Her iki sayıyı asal çarpanlarına ayır.','144 = 2⁴ × 3² · 180 = 2² × 3² × 5'),A('EBOB’u bul','Ortak asallar 2 ve 3; küçük üsler alınır.','EBOB = 2² × 3² = 36'),A('Bölen sayısı','Ortak bölenler EBOB’un bölenleridir; sayısı (üs + 1) çarpımıdır.','(2 + 1)(2 + 1) = 9')],
 puf='Ortak bölen sayısı = EBOB’un bölen sayısı; ortak bölenleri tek tek listelemek yerine EBOB’u asal çarpanlarına ayır.')

# ---------- 11 · orta · asal çarpanlarla EBOB/EKOK oranı ----------
A_=2**3*3**2*5; B_=2**2*3**4*7
e=gcd(A_,B_); k=lcm(A_,B_)
assert e==2**2*3**2==36 and k==2**3*3**4*5*7==22680 and k//e==630
assert 2*3*5*7==210 and 3**2*5*7==315 and k%e==0
mk(P,'0011',tipId='ekb-iliski',tip='Aralarında asal sayılar ve EBOB × EKOK = a × b',z='orta',alt='Asal Çarpanlarla EBOB ve EKOK',kaz='Asal çarpanlarına ayrılmış iki sayının EBOB ve EKOK’unu üslerden kurarak oranlar.',kalip='düz',adim=3,
 kart='K-EBKB-02 (EBOB × EKOK) · asal çarpanlı iki sayı, EKOK / EBOB oranı',
 metin='A = 2³ × 3² × 5\nB = 2² × 3⁴ × 7\nolduğuna göre EKOK(A, B) ÷ EBOB(A, B) işleminin sonucu kaçtır?',
 dogru=630,yan=[(36,'EKOK yerine EBOB’u (2² × 3²) bulmuş.','dikkat'),(210,'Her asalı yalnız bir kez alıp çarpmış (2 × 3 × 5 × 7); üsleri hesaba katmamış.','bilgi'),(315,'2’nin üs farkından gelen çarpanı (2³⁻² = 2) yazmayı unutmuş; yalnız 3² × 5 × 7 almış.','islem'),(22680,'Oranı değil yalnız EKOK’u hesaplamış.','dikkat')],
 istenen='EKOK ÷ EBOB.',
 ip=['EBOB’ta ortak asalların küçük, EKOK’ta tüm asalların büyük üssü alınır; bölünce her asalın üs farkı kalır.'],
 bilgi=[ASAL,EB,EK],
 ad=[A('EBOB’u kur','Ortak asallar 2 ve 3, küçük üsler.','EBOB = 2² × 3²'),A('EKOK’u kur','Tüm asallar (2, 3, 5, 7), büyük üsler.','EKOK = 2³ × 3⁴ × 5 × 7'),A('Böl','Aynı tabanlı üsler bölünürken üsler çıkarılır.','2³⁻² × 3⁴⁻² × 5 × 7 = 2 × 9 × 5 × 7 = 630')],
 puf='EKOK ÷ EBOB = her asalın üs farkından gelen çarpımdır; sayıları açmadan, yalnız üslerle çalış.')

# ---------- 12 · zor · kalan koşulu + aralık ----------
lo,hi=175,900
c12=[x for x in range(lo,hi+1) if x%9==4 and x%12==7]
assert lcm(9,12)==36 and len(c12)==21 and c12[0]==175 and c12[-1]==895
assert all((x+5)%36==0 for x in c12)
assert (hi+5)//36==25 and len([x for x in c12 if x>lo])==20
assert len([x for x in range(lo,hi+1) if x%108==103])==7
assert len([x for x in range(lo,hi+1) if (x+5)%3==0])==242
mk(P,'0012',tipId='ekb-kalan',tip='Ortak katları sayma ve kalan koşulu',z='zor',alt='Kalan Koşullu Sayıların Adedi',kaz='Farklı kalan veren ama aynı eksiği olan koşulları EKOK ile birleştirip aralıktaki adedi bulur.',kalip='düz',adim=4,
 kart='K-EBKB-05 (kalan koşulu + aralık) · 9’a bölümden kalan 4, 12’ye bölümden kalan 7',
 metin='Bir N doğal sayısı 9’a bölündüğünde 4, 12’ye bölündüğünde 7 kalanını vermektedir.\n175 ≤ N ≤ 900 olduğuna göre bu koşulları sağlayan kaç farklı N sayısı vardır?',
 dogru=21,yan=[(7,'EKOK yerine 9 × 12 = 108’i almış; sayıları 108 aralıklarla sıralamış.','bilgi'),(20,'175 = 36 × 5 − 5 sayısının koşulu sağladığını görüp saymamış; alt sınırı dışarıda bırakmış.','dikkat'),(25,'Yalnız üst sınıra bakıp (905 ÷ 36 = 25) alt sınırdan önceki sayıları (31, 67, 103, 139) çıkarmamış.','dikkat'),(242,'EBOB’u (3) kullanıp N + 5’in 3’ün katı olmasına bakmış; 36’nın katı olması gerektiğini atlamış.','bilgi')],
 istenen='Koşulları sağlayan N sayısının adedi.',
 ip=['9’a bölümde kalan 4 ise 5 eksik, 12’ye bölümde kalan 7 ise yine 5 eksiktir; N + 5 ne olmalıdır?'],
 bilgi=[EK,KL],
 ad=[A('Eksiği yaz','9’a bölünce 4 kalıyorsa 9’a tamamlamak için 5 eksik; 12’de de 12 − 7 = 5 eksik.','N + 5 hem 9’un hem 12’nin katı'),A('EKOK’u uygula','N + 5 ortak kat olduğundan 36’nın katıdır.','EKOK(9, 12) = 36 · N = 36k − 5'),A('k’yı sınırla','175 ≤ 36k − 5 ≤ 900 ise 180 ≤ 36k ≤ 905; en küçük k = 5, en büyük k = 25 (36 × 25 = 900).','5 ≤ k ≤ 25'),A('Say','k tam sayı olarak 5’ten 25’e kadar değişir.','25 − 5 + 1 = 21')],
 puf='Kalanlar farklı ama eksikler eşitse N + eksik ortak kat olur; sonra sınırlardan k’yı bul ve uç değerleri ayrı kontrol et.')

# ---------- 13 · zor · en küçük sayı ve bölen sayısı ----------
c13=[x for x in range(1,2000) if x%18==0 and nb(x)==12]; assert c13[0]==72
assert nb(60)==12 and 60%18!=0 and nb(90)==12 and 90%18==0 and nb(96)==12 and 96%18!=0 and nb(108)==12 and 108%18==0 and 72 in c13
assert 72==2**3*3**2 and 90==2*3**2*5 and 108==2**2*3**3
assert min(x for x in range(1,2000) if nb(x)==12)==60
mk(P,'0013',tipId='ekb-bolen',tip='Asal çarpanlara ayırma ve pozitif bölen sayısı',z='zor',alt='Koşullu En Küçük Sayı',kaz='Bölen sayısı ve katı olma koşulunu birlikte sağlayan en küçük sayıyı asal çarpan üslerini kurarak bulur.',kalip='düz',adim=4,
 kart='K-EBKB-01 (bölen sayısı + koşul) · 18’in katı olan ve tam 12 pozitif böleni bulunan en küçük sayı',
 metin='Tam 12 tane pozitif böleni olan ve 18’in katı olan en küçük pozitif tam sayı kaçtır?',
 dogru=72,yan=[(60,'18’in katı olma koşulunu atlayıp yalnızca 12 bölenli en küçük sayıyı (60) vermiş.','dikkat'),(90,'2 × 3² × 5 yapısını denemiş; 2³ × 3² yapısının (72) daha küçük olduğunu görmemiş.','islem'),(96,'2⁵ × 3 yapısını seçmiş; 18’in katı olması için 3’ün üssünün en az 2 olması gerektiğini atlamış.','bilgi'),(108,'2² × 3³ yapısını seçmiş; 2³ × 3²’nin de 12 böleni olduğunu denememiş.','islem')],
 istenen='Koşulları sağlayan en küçük sayı.',
 ip=['18 = 2 × 3² olduğundan sayıda 2’nin üssü en az 1, 3’ün üssü en az 2 olmalıdır; bölen sayısı 12 olacak üs çiftlerini dene.'],
 bilgi=[ASAL,BS],
 ad=[A('Koşulu yaz','Sayı 18’in katı olduğu için asal çarpanlarında en az 2¹ ve 3² bulunur.','N = 2ᵃ × 3ᵇ × … · a ≥ 1, b ≥ 2'),A('Bölen sayısını kur','(a + 1)(b + 1)(…) = 12. Yalnız 2 ve 3 kullanılırsa (a + 1)(b + 1) = 12 olmalıdır.','(a, b) = (1, 5), (2, 3), (3, 2) çiftleri; b ≥ 2 şartı sağlanıyor'),A('Üçüncü asalı da dene','Üçüncü bir asal (5) eklenirse (a + 1)(b + 1) × 2 = 12 ise (a + 1)(b + 1) = 6.','(a, b) = (1, 2) → N = 2 × 3² × 5 = 90'),A('En küçüğü seç','Adaylar: 2 × 3⁵ = 486, 2² × 3³ = 108, 2³ × 3² = 72, 90.','En küçüğü 72')],
 puf='Koşullu bölen sayısı sorularında önce zorunlu asal çarpanları yaz, kalan üsleri bölen sayısı çarpımına uyacak biçimde dağıt; küçük asala büyük üs vermek sayıyı küçültür.')

# ---------- 14 · zor · üç tabela ----------
p14=[12,18,20]; T=360
def kac(t): return sum(1 for p in p14 if t%p==0)
yal=[t for t in range(1,T+1) if t%12==0 and t%18==0 and t%20!=0]
c1218=T//lcm(12,18); c3=T//lcm(12,18,20)
assert c1218==10 and c3==2 and len(yal)==8 and 10+2==12 and T//lcm(12,20)==6
mk(P,'0014',tipId='ekb-periyot',tip='Koşu, dişli çark ve çakışma sayısı',z='zor',alt='Ortak Yanma Sayısı',kaz='İki periyodik olayın birlikte gerçekleştiği anlardan üçüncüsünün de gerçekleştiği anları çıkararak sayar.',kalip='hikâyeli',adim=4,
 kart='K-EBKB-04 (çakışma sayısı) · 12, 18, 20 dakikalık üç tabela, ilk ikisi birlikte yanarken üçüncüsü yanmayan anlar',
 metin='Bir alışveriş merkezinin girişindeki üç ışıklı tabela sırasıyla 12 dakikada bir, 18 dakikada bir ve 20 dakikada bir yanıp sönmektedir. Üçü saat 08.00’de aynı anda yanıp sönmüştür.\nBuna göre saat 08.00’den sonra 14.00’e kadar (14.00 dahil, 08.00 hariç) birinci ve ikinci tabelanın aynı anda yanıp söndüğü, üçüncü tabelanın ise yanıp sönmediği kaç an vardır?',
 dogru=8,yan=[(2,'Yalnız üç tabelanın birlikte yandığı anları (180 dakikada bir) saymış.','dikkat'),(6,'Birinci ve üçüncü tabelanın birlikte yandığı anları (60 dakikada bir) saymış.','dikkat'),(10,'Yalnız birinci ve ikinci tabelanın birlikte yandığı anları saymış; üçüncünün yanmaması koşulunu atlamış.','dikkat'),(12,'Üçüncünün yandığı anları çıkarmak yerine eklemiş (10 + 2).','islem')],
 istenen='Birinci ve ikinci tabela yanarken üçüncünün yanmadığı anların adedi.',
 ip=['Önce ilk ikisinin birlikte yandığı anları say; bunların hangilerinde üçüncü de yanıyor?'],
 bilgi=[EK,OK],
 ad=[A('Süreyi dakikaya çevir','08.00 ile 14.00 arası 6 saattir.','6 × 60 = 360 dakika'),A('İlk ikisinin anları','İlk ikisi EKOK(12, 18) = 36 dakikada bir birlikte yanar.','360 ÷ 36 = 10 an'),A('Üçlü anları bul','Üçü birlikte EKOK(12, 18, 20) = 180 dakikada bir yanar; bu anlar yukarıdaki 10 anın içindedir.','360 ÷ 180 = 2 an'),A('Çıkar','İlk ikisi yanarken üçüncünün yanmadığı anlar kalır.','10 − 2 = 8')],
 puf='“A ve B olup C olmayan” sayılırken A ile B’nin ortak anlarından üçünün de ortak anlarını çıkar.')

bitir(P,'ebobiki',UK)
