"""Olasılık · parti 1: 8 ana + 8 kardeş. Her olasılık tüm durumlar (itertools) taranarak Fraction ile doğrulanır."""
import sys,os
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,os.path.join(H,'..'))
from ortak import *
from math import comb

P=Parti('olasilik','Olasılık','matd|Olasılık')
TT=lambda **k:k
K_=lambda v:f'{v.numerator}/{v.denominator}' if isinstance(v,Fr) and v.denominator!=1 else str(v)
def tek_dogru(siklar,sik,deger):
    S=dict(zip('ABCDE',siklar)); d=K_(deger)
    assert S[sik]==d and list(S.values()).count(d)==1,(siklar,sik,d)
    deg=[Fr(x) for x in siklar]; assert len(set(deg))==5 and deg==sorted(deg),siklar   # sade ve farklı değerler, sıralı
    assert all(K_(Fr(x))==x for x in siklar),'kesir sade değil'
def olas(uzay,kosul):
    uzay=list(uzay); return Fr(sum(1 for u in uzay if kosul(u)),len(uzay))

OLS=B('Olasılık','olasılık = istenen durum sayısı / tüm durum sayısı (her durum eşit şanslıysa). Örnek: zarda çift gelme 3/6 = 1/2')
ARD=B('Art arda olaylar','iki olayın sırayla birlikte olma olasılığı çarpılır. Geri atılmazsa ikinci çekilişte torbadaki bilye sayısı 1 azalır')
KOMB=B('Kombinasyon','n nesneden sırası önemsiz r tanesi C(n, r) biçimde seçilir. Örnek: C(5, 2) = 10')
TUML=B('Tümleyen olay','bir olayın olma olasılığı = 1 − olmama olasılığı. “En az bir” için “hiç” durumunu 1’den çıkar')

# ===== 0001 basit olay KOLAY (K-OL-01)
v=olas(range(1,41),lambda n:n%4==0 or n%6==0); assert v==Fr(13,40)
assert olas(range(1,41),lambda n:n%12==0)==Fr(3,40) and olas(range(1,41),lambda n:n%4==0)==Fr(1,4) and Fr(16,40)==Fr(2,5) and 1-v==Fr(27,40)
s=['3/40','1/4','13/40','2/5','27/40']; tek_dogru(s,'C',v)
P.R('0001','ol-temel','Basit olayın olasılığı','kolay','Basit Olay','İki bölünebilme koşulundan en az birini sağlayan durumları içerme–dışarma ile sayıp olasılığı bulur.','hikâyeli',2,
 'K-OL-01 (numaralı kart, bölünebilme) · “4 ile ya da 6 ile” koşulu',
 'Bir torbada üzerlerinde 1’den 40’a kadar numaralar yazılı 40 kart vardır. Torbadan rastgele bir kart çekiliyor.\nÇekilen kartın numarasının 4 ile ya da 6 ile (en az biriyle) tam bölünebilme olasılığı kaçtır?',
 s,'C','Kart numarasının 4 ya da 6 ile bölünme olasılığı.',
 ['1–40 arasında 4’ün kaç katı var? 6’nın kaç katı var?','Hem 4’ün hem 6’nın katı olan sayılar iki listede de geçer.','İstenen durum sayısını 40’a böl.'],[OLS,B('Ortak katlar','hem 4’ün hem 6’nın katı olan sayılar EKOK(4, 6) = 12’nin katlarıdır')],
 [A('4’ün katları','40 ÷ 4 = 10.','4, 8, …, 40 ⇒ 10 sayı'),
  A('6’nın katları','36’ya kadar.','6, 12, …, 36 ⇒ 6 sayı'),
  A('Ortakları çıkar','12’nin katları iki listede de sayıldı; bir kez çıkar.','12, 24, 36 ⇒ 10 + 6 − 3 = 13'),
  A('Olasılık','İstenen durumları tüm durumlara böl.','13/40')],
 '“Ya da” koşulunda iki listeyi topla, ortak olanları bir kez çıkar.',
 dict(A='3/40, hem 4 hem 6 ile bölünenlerin (12’nin katları) olasılığı.',B='1/4, yalnızca 4 ile bölünenlerin olasılığı.',D='2/5, ortak katları iki kez saymak (16/40).',E='27/40, ikisiyle de bölünmeyenlerin olasılığı; bu tümleyen.'),
 TT(A='dikkat',B='dikkat',D='islem',E='dikkat'))
v=olas(range(1,51),lambda n:n%3 and n%5); assert v==Fr(27,50)
assert olas(range(1,51),lambda n:n%15==0)==Fr(3,50) and olas(range(1,51),lambda n:n%3==0 and n%5)==Fr(13,50) and 1-v==Fr(23,50) and Fr(50-16-10,50)==Fr(12,25)
s=['3/50','13/50','23/50','12/25','27/50']; tek_dogru(s,'E',v)
P.K('0001','Bir torbada 1’den 50’ye kadar numaralanmış 50 top vardır. Torbadan rastgele bir top çekiliyor.\nÇekilen topun numarasının ne 3 ile ne de 5 ile tam bölünebilme olasılığı kaçtır?',
 s,'E','Numaranın ne 3 ne 5 ile bölünme olasılığı.',
 ['Önce 3 ile ya da 5 ile bölünen numaraları say.','15’in katları iki listede de geçer.','Bölünenleri 50’den çıkar.'],[OLS,B('Ortak katlar','hem 3’ün hem 5’in katı olan sayılar 15’in katlarıdır')],
 [A('3’ün katları','48’e kadar.','50 ÷ 3 ⇒ 16 sayı'),
  A('5’in katları','50’ye kadar.','10 sayı'),
  A('En az biriyle bölünenler','15, 30, 45 iki listede de var.','16 + 10 − 3 = 23'),
  A('Olasılık','İkisiyle de bölünmeyenler kalan numaralardır.','50 − 23 = 27 ⇒ 27/50')],
 '“Ne … ne …” istenince önce “en az biri”ni say, sonra tümden çıkar.',
 dict(A='3/50, hem 3 hem 5 ile bölünenlerin (15’in katları) olasılığı.',B='13/50, 3 ile bölünüp 5 ile bölünmeyenlerin olasılığı.',C='23/50, en az biriyle bölünenlerin olasılığı; bu tümleyen.',D='12/25, ortak katları geri eklemeyip 50 − 16 − 10 = 24 bulmak.'),
 TT(A='dikkat',B='dikkat',C='dikkat',D='islem'))

# ===== 0002 art arda çekiliş KOLAY (K-OL-02)
torba=['K']*3+['M']*5
v=olas(permutations(range(8),2),lambda p:torba[p[0]]=='K' and torba[p[1]]=='M'); assert v==Fr(15,56)==Fr(3,8)*Fr(5,7)
assert Fr(3,8)*Fr(4,7)==Fr(3,14) and 2*v==Fr(15,28)
s=['3/14','15/56','3/8','15/28','5/8']; tek_dogru(s,'B',v)
P.R('0002','ol-ardisik','Art arda olaylar','kolay','Art Arda Olaylar','Geri atılmadan yapılan art arda çekilişte sıralı olayın olasılığını çarpma ile bulur.','hikâyeli',2,
 'K-OL-02 (geri atılmadan art arda çekiliş) · istenen sıra: kırmızı sonra mavi',
 'Bir torbada 3 kırmızı ve 5 mavi bilye vardır. Torbadan geri atılmamak koşuluyla art arda iki bilye çekiliyor.\nBirinci bilyenin kırmızı, ikinci bilyenin mavi olma olasılığı kaçtır?',
 s,'B','Önce kırmızı sonra mavi çekme olasılığı.',
 ['Birinci çekilişte kırmızı gelme olasılığı kaç?','Bir kırmızı çekildikten sonra torbada kaç bilye ve kaç mavi kalır?','İki olasılığı birleştir: çarp.'],[OLS,ARD],
 [A('Birinci çekiliş','8 bilyeden 3’ü kırmızı.','3/8'),
  A('İkinci çekiliş','Bir kırmızı çıktı; torbada 7 bilye, 5 mavi kaldı.','5/7'),
  A('Çarp','İki olay sırayla birlikte oluyor.','3/8 × 5/7 = 15/56')],
 'Geri atılmayan çekilişte her adımda torbayı güncelle: hem toplam hem çekilen renk 1 azalır.',
 dict(A='3/14, ikinci çekilişte mavi sayısını da 1 azaltmak (3/8 × 4/7); çekilen bilye kırmızıydı.',C='3/8, yalnızca birinci bilyenin kırmızı olma olasılığı.',D='15/28, sırayı önemsemeyip kırmızı–mavi ve mavi–kırmızı düzenlerini toplamak.',E='5/8, ikinci çekilişi tek başına düşünmek; iki olayın birlikte olma olasılığı çarpımdır.'),
 TT(A='islem',C='dikkat',D='dikkat',E='bilgi'))
kutu=['S']*4+['B']*2
v=olas(permutations(range(6),2),lambda p:kutu[p[0]]==kutu[p[1]]=='S'); assert v==Fr(2,5)
assert olas(permutations(range(6),2),lambda p:kutu[p[0]]==kutu[p[1]]=='B')==Fr(1,15) and Fr(2,3)**2==Fr(4,9) and olas(permutations(range(6),2),lambda p:kutu[p[0]]!=kutu[p[1]])==Fr(8,15)
s=['1/15','2/5','4/9','8/15','2/3']; tek_dogru(s,'B',v)
P.K('0002','Bir kutuda 4 sağlam ve 2 bozuk ampul vardır. Kutudan geri konulmamak üzere art arda iki ampul alınıyor.\nAlınan iki ampulün de sağlam olma olasılığı kaçtır?',
 s,'B','İki ampulün de sağlam olma olasılığı.',
 ['Birinci ampulün sağlam olma olasılığı kaç?','Bir sağlam ampul alınınca kutuda kaç ampul, kaç sağlam kalır?','İki olasılığı çarp ve sadeleştir.'],[OLS,ARD],
 [A('Birinci ampul','6 ampulden 4’ü sağlam.','4/6 = 2/3'),
  A('İkinci ampul','Bir sağlam alındı; 5 ampul, 3 sağlam kaldı.','3/5'),
  A('Çarp','İki olay birlikte oluyor.','2/3 × 3/5 = 2/5')],
 'Geri konulmayan seçimde ikinci adımın paydası 1 azalır; ilk adımda alınan türün sayısı da 1 azalır.',
 dict(A='1/15, iki ampulün de bozuk olma olasılığı.',C='4/9, ampulü geri koyuyormuş gibi 2/3 × 2/3 hesaplamak.',D='8/15, birinin sağlam birinin bozuk olma olasılığı.',E='2/3, yalnızca birinci ampulün sağlam olma olasılığı.'),
 TT(A='dikkat',C='bilgi',D='dikkat',E='dikkat'))

# ===== 0003 kombinasyonla olasılık ORTA (K-OL-04)
sinif=['k']*6+['e']*4
v=olas(combinations(range(10),3),lambda c:sum(sinif[i]=='k' for i in c)==2); assert v==Fr(1,2)
assert Fr(comb(6,2)*4,720)==Fr(1,12) and Fr(6,10)*Fr(5,9)*Fr(4,8)==Fr(1,6)
assert olas(combinations(range(10),3),lambda c:sum(sinif[i]=='k' for i in c)==1)==Fr(3,10) and olas(combinations(range(10),3),lambda c:sum(sinif[i]=='k' for i in c)>=2)==Fr(2,3)
s=['1/12','1/6','3/10','1/2','2/3']; tek_dogru(s,'D',v)
P.R('0003','ol-secme','Kombinasyonla olasılık','orta','Kombinasyonla Olasılık','Birlikte seçimde istenen bileşimin olasılığını kombinasyonla hesaplar.','hikâyeli',3,
 'K-OL-04 (birlikte seçimde bileşim) · 2 kız 1 erkek',
 'Bir sınıfta 6 kız ve 4 erkek öğrenci vardır. Bu sınıftan rastgele 3 öğrenci seçiliyor.\nSeçilen öğrencilerden 2’sinin kız, 1’inin erkek olma olasılığı kaçtır?',
 s,'D','2 kız 1 erkek seçilme olasılığı.',
 ['10 öğrenciden 3 öğrenci kaç farklı biçimde seçilir?','2 kızı 6 kızdan, 1 erkeği 4 erkekten seç; bu seçimler çarpılır.','İstenen seçim sayısını tüm seçimlere böl.'],[OLS,KOMB],
 [A('Tüm seçimler','10 öğrenciden 3’ü, sıra önemsiz.','C(10, 3) = 120'),
  A('İstenen seçimler','6 kızdan 2, 4 erkekten 1.','C(6, 2) × C(4, 1) = 15 × 4 = 60'),
  A('Olasılık','İstenenleri tüm seçimlere böl.','60/120 = 1/2')],
 'Pay ile paydayı aynı yöntemle say: ikisi de sırasız (kombinasyon) ya da ikisi de sıralı.',
 dict(A='1/12, paydayı sıralı seçimle (10 × 9 × 8 = 720) alıp payı sırasız saymak.',B='1/6, yalnızca kız–kız–erkek sırasını hesaplamak (6/10 × 5/9 × 4/8); erkek 3 farklı sırada gelebilir.',C='3/10, 1 kız 2 erkek seçilme olasılığı.',E='2/3, en az 2 kız seçilme olasılığı; 3 kızın seçildiği durum da eklenmiş.'),
 TT(A='bilgi',B='bilgi',C='dikkat',E='dikkat'))
tb=['K']*5+['B']*3+['S']*2
v=olas(combinations(range(10),2),lambda c:tb[c[0]]!=tb[c[1]]); assert v==Fr(31,45)
assert 1-v==Fr(14,45) and Fr(5*3,45)==Fr(1,3) and Fr(31,90)==v/2 and olas(product(range(10),repeat=2),lambda c:tb[c[0]]!=tb[c[1]])==Fr(31,50)
s=['14/45','1/3','31/90','31/50','31/45']; tek_dogru(s,'E',v)
P.K('0003','Bir torbada 5 kırmızı, 3 beyaz ve 2 siyah bilye vardır. Torbadan rastgele 2 bilye birlikte çekiliyor.\nÇekilen bilyelerin farklı renkte olma olasılığı kaçtır?',
 s,'E','İki bilyenin farklı renkte olma olasılığı.',
 ['10 bilyeden 2 bilye kaç farklı biçimde seçilir?','Farklı renk durumlarını tek tek saymak yerine aynı renk durumlarını say.','Tümleyeni kullan.'],[OLS,KOMB,TUML],
 [A('Tüm seçimler','10 bilyeden 2’si.','C(10, 2) = 45'),
  A('Aynı renk','İki kırmızı, iki beyaz ya da iki siyah.','C(5, 2) + C(3, 2) + C(2, 2) = 10 + 3 + 1 = 14'),
  A('Farklı renk','Tümleyeni al.','45 − 14 = 31 ⇒ 31/45')],
 'Çok sayıda karma durum varsa az olan “aynı renk” durumlarını sayıp tümden çıkar.',
 dict(A='14/45, iki bilyenin aynı renkte olma olasılığı.',B='1/3, yalnızca kırmızı–beyaz ikililerini saymak (15/45).',C='31/90, sırasız durum sayısını sıralı paydaya (10 × 9) bölmek.',D='31/50, bilyeleri geri atılarak çekiliyormuş gibi hesaplamak.'),
 TT(A='dikkat',B='dikkat',C='bilgi',D='bilgi'))

# ===== 0004 tümleyen ORTA (K-OL-05)
U4=list(product(range(1,6),repeat=3))
v=olas(U4,lambda t:len(set(t))<3); assert v==Fr(13,25)
assert olas(U4,lambda t:len(set(t))==1)==Fr(1,25) and olas(U4,lambda t:len(set(t))==3)==Fr(12,25) and 3*Fr(1,5)==Fr(3,5)
s=['1/25','1/5','12/25','13/25','3/5']; tek_dogru(s,'D',v)
P.R('0004','ol-tumleyen','Tümleyen olay','orta','Tümleyen Olay','“En az ikisi aynı” olasılığını “hepsi farklı” tümleyeninden bulur.','hikâyeli',3,
 'K-OL-05 (en az … olasılığı tümleyenden) · yeni kurgu (üç kişinin sayı seçmesi)',
 'Ayşe, Bora ve Cenk birbirlerinden habersiz olarak 1, 2, 3, 4 ve 5 sayılarından birini rastgele seçiyor.\nEn az iki kişinin aynı sayıyı seçmiş olma olasılığı kaçtır?',
 s,'D','En az iki kişinin aynı sayıyı seçme olasılığı.',
 ['Üç kişinin seçimleri kaç farklı biçimde olabilir?','“En az iki kişi aynı” olmayan durum nedir?','Üçünün de farklı seçtiği durumları say ve 1’den çıkar.'],[OLS,TUML,B('Çarpma ilkesi','her kişi 5 sayıdan birini seçerse üç kişinin seçimleri 5 × 5 × 5 biçimde olur')],
 [A('Tüm durumlar','Her kişi 5 sayıdan birini seçer.','5 × 5 × 5 = 125'),
  A('Hepsi farklı','Ayşe 5, Bora kalan 4, Cenk kalan 3 sayıdan seçer.','5 × 4 × 3 = 60'),
  A('Tümleyen','“En az ikisi aynı”, “hepsi farklı”nın tümleyenidir.','1 − 60/125 = 65/125 = 13/25')],
 '“En az iki aynı” sorularında “hepsi farklı” durumunu say ve 1’den çıkar.',
 dict(A='1/25, üçünün de aynı sayıyı seçme olasılığı.',B='1/5, yalnızca Bora’nın Ayşe ile aynı sayıyı seçme olasılığı.',C='12/25, herkesin farklı sayı seçme olasılığı; bu tümleyen.',E='3/5, üç ikilinin eşleşme olasılıklarını (1/5) toplamak; bu olaylar aynı anda olabildiği için toplanamaz.'),
 TT(A='dikkat',B='dikkat',C='dikkat',E='bilgi'))
p=Fr(2,3); v=sum((p if a else 1-p)*(p if b else 1-p)*(p if c else 1-p) for a,b,c in product((1,0),repeat=3) if a or b or c); assert v==Fr(26,27)
assert (1-p)**3==Fr(1,27) and p**3==Fr(8,27) and 1-p**3==Fr(19,27)
s=['1/27','8/27','2/3','19/27','26/27']; tek_dogru(s,'E',v)
P.K('0004','Bir okçu, attığı her okla hedefi 2/3 olasılıkla vurmaktadır; atışların sonuçları birbirini etkilememektedir.\nOkçu 3 ok attığında hedefi en az bir kez vurmuş olma olasılığı kaçtır?',
 s,'E','Üç atışta en az bir isabet olasılığı.',
 ['Bir atışta ıskalama olasılığı kaç?','“En az bir kez vurma” olmayan durum nedir?','Üç atışın da ıskalanma olasılığını 1’den çıkar.'],[TUML,B('Bağımsız olaylar','sonuçları birbirini etkilemeyen olayların birlikte olma olasılığı çarpılır. Örnek: iki yazı-tura atışında iki yazı 1/2 × 1/2 = 1/4')],
 [A('Iskalama','Bir atışta ıskalama olasılığı.','1 − 2/3 = 1/3'),
  A('Hiç vuramama','Üç atışın üçü de ıskalanmalı.','1/3 × 1/3 × 1/3 = 1/27'),
  A('Tümleyen','“En az bir” = 1 − “hiç”.','1 − 1/27 = 26/27')],
 '“En az bir kez” olasılığı her zaman 1 − (hiç olmama olasılığı) ile hızlıca bulunur.',
 dict(A='1/27, hiç vuramama olasılığı; bu tümleyen.',B='8/27, üç atışta da vurma olasılığı.',C='2/3, bir atıştaki vurma olasılığını cevap sanmak.',D='19/27, “hepsini vurma”nın tümleyenini almak (1 − 8/27); istenen “en az bir kez vurma”.'),
 TT(A='dikkat',B='dikkat',C='bilgi',D='islem'))

# ===== 0005 iki aşamalı ORTA (K-OL-03)
gec={'Y':Fr(2,5),'K':Fr(1,5)}  # bugün Y(ağmurlu) / K(uru) iken yarın yağmur olasılığı
def yol(bas,dizi):
    o=Fr(1); d=bas
    for x in dizi:
        py=gec[d]; o*=py if x=='Y' else 1-py; d=x
    return o
v=sum(yol('Y',(sali,'Y')) for sali in 'YK'); assert v==Fr(7,25) and yol('Y','YY')==Fr(4,25) and yol('Y','KY')==Fr(3,25) and 1-v==Fr(18,25)
s=['3/25','4/25','7/25','2/5','18/25']; tek_dogru(s,'C',v)
P.R('0005','ol-ardisik','Art arda olaylar','orta','Art Arda Olaylar','İki aşamalı olayda olası yolların olasılıklarını çarpıp toplar.','hikâyeli',3,
 'K-OL-03 (iki aşamalı olay, yolları toplama) · yeni kurgu (günlük hava durumu)',
 'Bir şehirde yağmurlu bir günün ertesi gününün de yağmurlu olma olasılığı 2/5, yağmursuz bir günün ertesi gününün yağmurlu olma olasılığı ise 1/5’tir.\nBu şehirde pazartesi günü yağmur yağdığına göre çarşamba günü yağmur yağma olasılığı kaçtır?',
 s,'C','Çarşamba gününün yağmurlu olma olasılığı.',
 ['Pazartesiden çarşambaya giderken salı günü kaç farklı durumda olabilir?','Her durum için salının ve çarşambanın olasılıklarını çarp.','Bulduğun iki yolu topla.'],[ARD,B('Ayrık yolları toplama','bir sonuca birbirinden ayrı yollarla ulaşılıyorsa her yolun olasılığı ayrı hesaplanır ve toplanır')],
 [A('Salı yağmurlu','Pazartesi yağmurlu ⇒ salı yağmurlu 2/5; ardından çarşamba yağmurlu 2/5.','2/5 × 2/5 = 4/25'),
  A('Salı yağmursuz','Salının yağmursuz olma olasılığı 1 − 2/5 = 3/5; ardından çarşamba yağmurlu 1/5.','3/5 × 1/5 = 3/25'),
  A('Topla','İki yol birbirinden ayrık.','4/25 + 3/25 = 7/25')],
 'Ara aşaması belirsiz olaylarda her olası ara durumu ayrı bir yol olarak hesapla, sonra topla.',
 dict(A='3/25, yalnızca salının yağmursuz olduğu yolu hesaplamak.',B='4/25, yalnızca salının yağmurlu olduğu yolu hesaplamak.',D='2/5, salıyı atlayıp pazartesiden çarşambaya doğrudan 2/5 almak.',E='18/25, çarşamba günü yağmur yağmama olasılığı.'),
 TT(A='dikkat',B='dikkat',D='bilgi',E='dikkat'))
v=Fr(10,100)*Fr(80,100)+Fr(90,100)*Fr(10,100); assert v==Fr(17,100)
# 1000 ürünlük örnek tablo ile kontrol
kus=100; sag=900; assert Fr(kus*80//100+sag*10//100,1000)==v
s=['8','9','17','45','90']; tek_dogru(s,'C',v*100)
P.K('0005','Bir fabrikada üretilen ürünlerin %10’u kusurludur. Bir kalite kontrol cihazı kusurlu bir ürünü %80 olasılıkla, sağlam bir ürünü ise %10 olasılıkla “kusurlu” olarak işaretlemektedir.\nRastgele seçilen bir ürünün bu cihaz tarafından “kusurlu” olarak işaretlenme olasılığı yüzde kaçtır?',
 s,'C','Bir ürünün “kusurlu” işaretlenme olasılığı (yüzde).',
 ['Bir ürün “kusurlu” işaretine iki farklı yoldan ulaşabilir; hangileri?','Kusurlu olup işaretlenme ve sağlam olup işaretlenme olasılıklarını ayrı ayrı çarp.','İki yolu topla ve yüzdeye çevir.'],[ARD,B('Yüzde','%10 = 10/100 = 0,1. Örnek: 200’ün %10’u 20’dir')],
 [A('Kusurlu ve işaretli','Ürünlerin %10’u kusurlu, bunların %80’i işaretlenir.','0,10 × 0,80 = 0,08'),
  A('Sağlam ama işaretli','Ürünlerin %90’ı sağlam, bunların %10’u yanlışlıkla işaretlenir.','0,90 × 0,10 = 0,09'),
  A('Topla','İki yol ayrık.','0,08 + 0,09 = 0,17 ⇒ %17')],
 'Oranları doğrudan toplama ya da ortalamasını alma; her oranı ait olduğu grubun payıyla çarp.',
 dict(A='8, yalnızca kusurlu ürünlerin işaretlenmesini hesaplamak.',B='9, yalnızca sağlam ürünlerin yanlışlıkla işaretlenmesini hesaplamak.',D='45, %80 ile %10’un ortalamasını almak; oranlar grupların payıyla çarpılmalı.',E='90, %80 ile %10’u toplamak.'),
 TT(A='dikkat',B='dikkat',D='bilgi',E='bilgi'))

# ===== 0006 şekil üzerinde ORTA (K-OL-06)
def komsu_ciftleri(sat,sut):
    kare=[(r,c) for r in range(sat) for c in range(sut)]
    ck=list(combinations(kare,2))
    kenar=[p for p in ck if abs(p[0][0]-p[1][0])+abs(p[0][1]-p[1][1])==1]
    kose=[p for p in ck if abs(p[0][0]-p[1][0])==1 and abs(p[0][1]-p[1][1])==1]
    return kare,ck,kenar,kose
kare,ck,kenar,kose=komsu_ciftleri(3,3); assert len(ck)==36 and len(kenar)==12 and len(kose)==8
v=Fr(len(kenar),len(ck)); assert v==Fr(1,3) and Fr(8,36)==Fr(2,9) and Fr(24,81)==Fr(8,27) and Fr(20,36)==Fr(5,9) and Fr(24,36)==Fr(2,3)
komsu={k:sum(1 for p in kenar if k in p) for k in kare}; assert sum(komsu.values())==24
s=['2/9','8/27','1/3','5/9','2/3']; tek_dogru(s,'C',v)
def tahta(sat,sut,etiket=None):
    u=min(52,240/sut,150/sat); W=330; ox=(W-sut*u)/2; oy=10; b=[]
    for r in range(sat):
        for c in range(sut):
            x,y=ox+c*u,oy+r*u
            b.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{u:.1f}" height="{u:.1f}" stroke-width="2" style="fill:var(--bg,#fff)" fill-opacity="0"/>')
            if etiket: b.append(G._t(x+u/2,y+u/2+5,str(etiket[(r,c)]),size=15,bold=True,renk=G.ACC))
    return G._svg(W,round(oy*2+sat*u),''.join(b))
P.R('0006','ol-sekil','Şekil üzerinde olasılık','orta','Şekilli Olasılık','Kareli tahtada ortak kenarlı kare çiftlerini sayarak olasılığı bulur.','şekilli',3,
 'K-OL-06 (kareli tahtada komşu kareler) · 3 × 3 tahta, ortak kenar',
 'Aşağıda 3 satır ve 3 sütun biçiminde dizilmiş 9 eş kareden oluşan bir tahta gösterilmiştir. Bu karelerden rastgele 2 tanesi seçiliyor.\nSeçilen iki karenin ortak bir kenarının olma olasılığı kaçtır?',
 s,'C','Seçilen iki karenin ortak kenarlı olma olasılığı.',
 ['9 kareden 2 kare kaç farklı biçimde seçilir?','Her satırda yan yana kaç komşu çift var? Her sütunda alt alta kaç çift var?','Köşeleri değen kareler ortak kenarlı değildir.'],[OLS,KOMB],
 [A('Tüm seçimler','9 kareden 2’si, sıra önemsiz.','C(9, 2) = 36'),
  A('Komşu çiftler','Her satırda 2 yan yana çift, her sütunda 2 alt alta çift. Şekilde her karenin komşu sayısı yazılı; toplamları 24, her çift iki kez sayıldığı için ikiye bölünür.','3 × 2 + 3 × 2 = 12',tahta(3,3,komsu)),
  A('Olasılık','İstenen çiftleri tüm seçimlere böl.','12/36 = 1/3')],
 'Komşu çiftleri satır satır ve sütun sütun say; her kareden sayarsan sonucu ikiye bölmeyi unutma.',
 dict(A='2/9, yalnızca köşe köşeye değen kareleri saymak (8/36).',B='8/27, kareleri sıralı ve tekrarlı seçiyormuş gibi saymak (24/81).',D='5/9, köşesi değen kareleri de saymak (20/36).',E='2/3, her karenin komşu sayılarını toplayıp (24) ikiye bölmemek.'),
 TT(A='dikkat',B='bilgi',D='dikkat',E='islem'),sekil=tahta(3,3))
kare,ck,kenar,kose=komsu_ciftleri(2,4); assert len(ck)==28 and len(kenar)==10
v=Fr(len(kenar),len(ck)); assert v==Fr(5,14)
yan=[p for p in kenar if p[0][0]==p[1][0]]; alt=[p for p in kenar if p[0][1]==p[1][1]]; assert len(yan)==6 and len(alt)==4
ayni=[p for p in ck if p[0][0]==p[1][0] or p[0][1]==p[1][1]]; assert Fr(len(ayni),28)==Fr(4,7) and Fr(10,56)==Fr(5,28)
komsu={k:sum(1 for p in kenar if k in p) for k in kare}; assert sum(komsu.values())==20
s=['1/7','5/28','3/14','5/14','4/7']; tek_dogru(s,'D',v)
P.K('0006','Aşağıdaki şekilde 2 satır ve 4 sütundan oluşan, 8 eş kareli bir tahta gösterilmiştir. Bu karelerden rastgele 2 tanesi seçiliyor.\nSeçilen karelerin ortak bir kenarı olma olasılığı kaçtır?',
 s,'D','Seçilen iki karenin ortak kenarlı olma olasılığı.',
 ['8 kareden 2 kare kaç farklı biçimde seçilir?','Satırlarda yan yana duran çiftleri say.','Sütunlarda alt alta duran çiftleri de ekle.'],[OLS,KOMB],
 [A('Tüm seçimler','8 kareden 2’si.','C(8, 2) = 28'),
  A('Komşu çiftler','Her satırda 3 yan yana çift, her sütunda 1 alt alta çift. Şekildeki komşu sayılarının toplamı 20; her çift iki kez sayıldığı için 10 eder.','2 × 3 + 4 × 1 = 10',tahta(2,4,komsu)),
  A('Olasılık','İstenenleri tümüne böl ve sadeleştir.','10/28 = 5/14')],
 'Ortak kenarlı kareler ya aynı satırda yan yana ya aynı sütunda alt altadır; ikisini ayrı say.',
 dict(A='1/7, yalnızca alt alta duran kareleri saymak (4/28).',B='5/28, kareler birlikte seçildiği hâlde paydayı sıralı (8 × 7 = 56) almak.',C='3/14, yalnızca yan yana duran kareleri saymak (6/28).',E='4/7, aynı satırdaki ya da aynı sütundaki tüm kare çiftlerini saymak (16/28); kareler bitişik olmalı.'),
 TT(A='dikkat',B='bilgi',C='dikkat',E='dikkat'),sekil=tahta(2,4))

# ===== 0007 olasılıktan sayı bulma ZOR (K-OL-07)
r_=[r for r in range(0,11) if Fr(comb(r,2),comb(10,2))==Fr(1,3)]; assert r_==[6]
tb=['K']*6+['B']*4
v=olas(combinations(range(10),2),lambda c:tb[c[0]]==tb[c[1]]=='B'); assert v==Fr(2,15)
assert Fr(4,10)**2==Fr(4,25) and olas(combinations(range(10),2),lambda c:tb[c[0]]!=tb[c[1]])==Fr(8,15)
s=['2/15','4/25','1/3','2/5','8/15']; tek_dogru(s,'A',v)
P.R('0007','ol-sayi-bulma','Olasılıktan sayı bulma','zor','Olasılıktan Sayı Bulma','Verilen olasılıktan torbadaki renk sayısını bulup başka bir olayın olasılığını hesaplar.','hikâyeli',4,
 'K-OL-07 (olasılıktan sayı bulma) · yeni kurgu (kırmızı–beyaz bilye), istenen diğer renk',
 'Bir torbada yalnızca kırmızı ve beyaz bilyeler vardır ve toplam bilye sayısı 10’dur. Torbadan rastgele 2 bilye birlikte çekildiğinde ikisinin de kırmızı olma olasılığı 1/3’tür.\nBuna göre torbadan rastgele çekilen 2 bilyenin ikisinin de beyaz olma olasılığı kaçtır?',
 s,'A','İki bilyenin de beyaz olma olasılığı.',
 ['10 bilyeden 2 bilye kaç farklı biçimde seçilir?','İki kırmızı seçiminin sayısı, tüm seçimlerin 1/3’ü olmalı. Kaç kırmızı bilye bunu sağlar?','Beyaz sayısını bulup iki beyaz seçiminin olasılığını hesapla.'],[OLS,KOMB],
 [A('Tüm seçimler','10 bilyeden 2’si.','C(10, 2) = 45'),
  A('Kırmızı sayısı','İki kırmızı seçimi 45 × 1/3 = 15 olmalı.','C(r, 2) = 15 ⇒ r × (r − 1) = 30 ⇒ r = 6'),
  A('Beyaz sayısı','Kalanlar beyaz.','10 − 6 = 4'),
  A('İki beyaz','4 beyazdan 2’si.','C(4, 2) / 45 = 6/45 = 2/15')],
 'Olasılık verilmişse önce istenen durum sayısını bul (tüm durum × olasılık), sonra bilinmeyen sayıyı çöz.',
 dict(B='4/25, bilyeleri geri atılarak çekiliyormuş gibi (4/10)² hesaplamak.',C='1/3, ikisinin de kırmızı olma olasılığı; soru beyazı soruyor.',D='2/5, tek bir bilyenin beyaz olma olasılığı (4/10).',E='8/15, bilyelerin farklı renkte olma olasılığı (24/45).'),
 TT(B='bilgi',C='dikkat',D='bilgi',E='dikkat'))
m_=[m for m in range(0,13) if 1-Fr(comb(12-m,2),comb(12,2))==Fr(5,11)]; assert m_==[3]
kt=['M']*3+['S']*9
v=olas(combinations(range(12),2),lambda c:kt[c[0]]==kt[c[1]]=='M'); assert v==Fr(1,22)
assert Fr(3,12)**2==Fr(1,16) and olas(combinations(range(12),2),lambda c:kt[c[0]]!=kt[c[1]])==Fr(9,22) and 1-Fr(5,11)==Fr(6,11)
s=['1/22','1/16','9/22','5/11','6/11']; tek_dogru(s,'A',v)
P.K('0007','Bir kutudaki 12 kalemin bir kısmı mavi, diğerleri siyahtır. Kutudan rastgele 2 kalem birlikte alındığında en az birinin mavi olma olasılığı 5/11’dir.\nBuna göre alınan 2 kalemin ikisinin de mavi olma olasılığı kaçtır?',
 s,'A','İki kalemin de mavi olma olasılığı.',
 ['“En az biri mavi” olasılığından “hiçbiri mavi değil” olasılığını bul.','Hiç mavi olmaması, iki siyah kalem seçilmesi demektir; kaç siyah kalem bunu sağlar?','Mavi sayısını bulup iki mavi seçiminin olasılığını hesapla.'],[OLS,KOMB,TUML],
 [A('Tümleyen','Hiç mavi olmama olasılığı.','1 − 5/11 = 6/11'),
  A('Siyah sayısı','C(12, 2) = 66; iki siyah seçimi 66 × 6/11 = 36 olmalı.','C(s, 2) = 36 ⇒ s × (s − 1) = 72 ⇒ s = 9'),
  A('Mavi sayısı','Kalanlar mavi.','12 − 9 = 3'),
  A('İki mavi','3 maviden 2’si.','C(3, 2) / 66 = 3/66 = 1/22')],
 '“En az bir” olasılığı verildiyse önce tümleyeni bul; “hiç” durumu tek bir türden seçimdir.',
 dict(B='1/16, kalemleri geri koyarak alınıyormuş gibi (3/12)² hesaplamak.',C='9/22, tam bir kalemin mavi olma olasılığı (27/66).',D='5/11, verilen “en az biri mavi” olasılığı.',E='6/11, hiçbirinin mavi olmama olasılığı.'),
 TT(B='bilgi',C='dikkat',D='dikkat',E='dikkat'))

# ===== 0008 sayma ile olasılık ZOR (K-OL-08)
sec=list(combinations(range(1,10),3)); assert len(sec)==84
v=olas(sec,lambda c:int(''.join(map(str,sorted(c))))%2==0); assert v==Fr(17,42)
assert [comb(m-1,2) for m in (2,4,6,8)]==[0,3,10,21] and Fr(10+21,84)==Fr(31,84) and Fr(comb(4,2)+comb(6,2)+comb(8,2),84)==Fr(7,12)
s=['31/84','17/42','4/9','1/2','7/12']; tek_dogru(s,'B',v)
TC=B('Tek ve çift sayı','birler basamağı 0, 2, 4, 6 ya da 8 olan sayı çift; 1, 3, 5, 7 ya da 9 olan sayı tektir')
P.R('0008','ol-sayma','Sayma ile olasılık','zor','Olasılık ve Sayma','Sıralanarak yazılan sayının çift olmasını en büyük rakama bağlayıp kombinasyonla sayar.','hikâyeli',4,
 'K-OL-08 (rakam seçip sıralı sayı yazma) · küçükten büyüğe dizilim, çift olma',
 'Ece, 1’den 9’a kadar olan rakamlardan birbirinden farklı üç tanesini rastgele seçip bu rakamları soldan sağa küçükten büyüğe sıralayarak üç basamaklı bir sayı yazıyor.\nEce’nin yazdığı sayının çift sayı olma olasılığı kaçtır?',
 s,'B','Yazılan sayının çift olma olasılığı.',
 ['Rakamlar küçükten büyüğe dizilince birler basamağına hangi rakam gelir?','Sayının çift olması, en büyük rakamın çift olması demektir.','En büyük rakam m ise diğer iki rakam m’den küçük rakamlardan seçilir.'],[TC,KOMB,OLS],
 [A('Birler basamağı','Rakamlar küçükten büyüğe dizildiği için birler basamağı en büyük rakamdır.','sayı çift ⇔ en büyük rakam çift'),
  A('Tüm seçimler','9 rakamdan 3’ü, sıra önemsiz (dizilişi kural belirliyor).','C(9, 3) = 84'),
  A('En büyük rakam çift','En büyük rakam m ise diğer ikisi m’den küçük m − 1 rakamdan seçilir. m = 2 olamaz; 2’den küçük yalnızca 1 rakam var.','m = 4: C(3, 2) = 3 · m = 6: C(5, 2) = 10 · m = 8: C(7, 2) = 21'),
  A('Olasılık','Durumları topla, tüm seçimlere böl.','(3 + 10 + 21) / 84 = 34/84 = 17/42')],
 'Rakamlar bir kurala göre diziliyorsa birler basamağını o kural belirler; olasılığı o rakamın seçimine bağla.',
 dict(A='31/84, en büyük rakamın 4 olduğu durumu (3 seçim) unutmak.',C='4/9, sıralama kuralını unutup birler basamağını 9 rakamdan rastgele biri sanmak.',D='1/2, tek ve çift rakamların sayısını eşit sanmak; 1–9 arasında 4 çift, 5 tek rakam var.',E='7/12, en büyük rakam m iken diğer ikisini C(m, 2) ile saymak; m’den küçük m − 1 rakam vardır.'),
 TT(A='dikkat',C='dikkat',D='bilgi',E='islem'))
sec=list(combinations(range(1,9),3)); assert len(sec)==56
v=olas(sec,lambda c:int(''.join(map(str,sorted(c,reverse=True))))%2==1); assert v==Fr(17,28)
assert [comb(8-m,2) for m in (1,3,5,7)]==[21,10,3,0] and Fr(21,56)==Fr(3,8) and Fr(21+10,56)==Fr(31,56) and Fr(sum(comb(9-m,2) for m in (1,3,5,7)),56)==Fr(25,28)
s=['3/8','1/2','31/56','17/28','25/28']; tek_dogru(s,'D',v)
P.K('0008','Kaan, 1’den 8’e kadar olan rakamlardan birbirinden farklı üç tanesini rastgele seçip bunları soldan sağa büyükten küçüğe dizerek üç basamaklı bir sayı oluşturuyor.\nOluşan sayının tek sayı olma olasılığı kaçtır?',
 s,'D','Oluşan sayının tek olma olasılığı.',
 ['Büyükten küçüğe dizilince birler basamağında hangi rakam olur?','Sayının tek olması için en küçük rakam ne olmalı?','En küçük rakam m ise diğer ikisi m’den büyük rakamlardan seçilir.'],[TC,KOMB,OLS],
 [A('Birler basamağı','Büyükten küçüğe dizildiği için birler basamağı en küçük rakamdır.','sayı tek ⇔ en küçük rakam tek'),
  A('Tüm seçimler','8 rakamdan 3’ü.','C(8, 3) = 56'),
  A('En küçük rakam tek','En küçük rakam m ise diğer ikisi m’den büyük 8 − m rakamdan seçilir. m = 7 olamaz; 7’den büyük yalnızca 8 var.','m = 1: C(7, 2) = 21 · m = 3: C(5, 2) = 10 · m = 5: C(3, 2) = 3'),
  A('Olasılık','Durumları topla, tümüne böl.','(21 + 10 + 3) / 56 = 34/56 = 17/28')],
 'Sıralı yazılan sayılarda birler basamağı en büyük ya da en küçük rakamdır; koşulu o rakama taşı.',
 dict(A='3/8, yalnızca en küçük rakamın 1 olduğu durumu saymak (21/56).',B='1/2, birler basamağını rastgele sanıp tek ve çift rakam sayısı eşit diye 1/2 almak.',C='31/56, en küçük rakamın 5 olduğu durumu unutmak.',E='25/28, en küçük rakam m iken diğer ikisini m dahil C(9 − m, 2) ile saymak.'),
 TT(A='dikkat',B='bilgi',C='dikkat',E='islem'))

P.yaz(os.path.join(H,'olasilik-1.json'),os.path.join(H,'olasilik-1-kardes.json'))
