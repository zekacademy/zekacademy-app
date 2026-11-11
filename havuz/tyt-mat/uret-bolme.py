"""Bölme ve Bölünebilme · parti 2 (hafif mod): 19 ana soru, kardeş yok, ipucu 1. Her cevap ve şık kodla (kaba kuvvet tarama) doğrulanır."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_mat as H
from _hafif_mat import *
H.KONU='Bölme ve Bölünebilme'
P=Parti('bolme','Bölme ve Bölünebilme','mat|Bölme ve Bölünebilme')
UK='mat|Bölme ve Bölünebilme'
ds=lambda n:sum(map(int,str(n)))

KAL=B('Kalanlı bölme','bölünen = bölen × bölüm + kalan ve 0 ≤ kalan < bölen. Örnek: 17 = 5 × 3 + 2 (kalan 2, bölen 5’ten küçük)')
S4=B('4 ile bölünebilme','son iki basamağın oluşturduğu sayı 4’ün katıysa sayı 4’e tam bölünür. Örnek: 316 → 16 = 4 × 4, bu yüzden 316 sayısı 4’e bölünür')
S8=B('8 ile bölünebilme','son üç basamağın oluşturduğu sayı 8’in katıysa sayı 8’e tam bölünür. Örnek: 2136 → 136 = 8 × 17')
R9=B('3 ve 9 ile bölünebilme','rakamlar toplamı 3’ün (9’un) katıysa sayı 3’e (9’a) tam bölünür. Örnek: 252 → 2 + 5 + 2 = 9, hem 3’e hem 9’a bölünür')
R11=B('11 ile bölünebilme','sağdan başlayarak rakamlara sırayla +, −, +, … işareti verilip toplanır; sonuç 0 ya da 11’in katıysa sayı 11’e bölünür. Örnek: 2541 → 1 − 4 + 5 − 2 = 0, 11’e bölünür')
ASAL=B('Aralarında asal çarpanlar','sayı, aralarında asal çarpanlarına ayrılır ve her çarpana ayrı ayrı bölünme aranır. Örnek: 18 = 2 × 9, 36 = 4 × 9, 72 = 8 × 9, 99 = 9 × 11')
KALAR=B('Kalanlarla işlem','toplamın ya da çarpımın kalanı, kalanların toplamının ya da çarpımının kalanıdır. Örnek: 17 ve 20’nin 6 ile kalanları 5 ve 2; 17 + 20 = 37 → kalan 1, 5 + 2 = 7 → kalan 1')
GUN=B('Günlerde kalan','7 gün sonra aynı gün gelir; bu yüzden gün sayısının 7 ile bölümünden kalan kadar ilerlenir. Örnek: Pazartesi + 9 gün → 9 = 7 + 2, kalan 2 → Çarşamba')
TK=B('Tek ve çift sayı','2 ile bölünen sayı çifttir, bölünmeyen tektir. Çift sayıya tek sayı eklenince sonuç tek, çift sayı eklenince çift olur. Örnek: 6k çifttir, 6k + 5 tektir')
EKSI=B('Kalanı bölenden 1 az olan sayı','n, 4’e bölündüğünde 3 kalıyorsa n + 1, 4’ün katıdır. Örnek: 11’in 4 ile kalanı 3, 11 + 1 = 12 = 4 × 3')
KAT=B('Katlar','12’nin katı 12 × k biçimindedir (k doğal sayı). Aynı sayının katlarının toplamı o sayının katıdır. Örnek: 12 + 18 = 30 sayısı 6’nın katıdır')

# ---------- kartlar ----------
KY='ÖSYM 2019–2026 (bölünebilme, kalan) · yayın soru bankaları (yalnız mantık) · MEB 6–9. sınıf'
kart('K-BLNB-01','Bölme işlemi','Bölünen = bölen × bölüm + kalan eşitliği ve kalan < bölen koşuluyla en büyük/en küçük bölünen, bölüm–kalan ilişkisi ve iki farklı bölenle yazılan eşitlik kurulur.','Kalanı bölene eşit ya da büyük almak; bölen ile bölümü karıştırmak; parantezi dağıtırken katsayıyı unutmak.','orta','düz',3,'blb-bolme','Bölme işlemi ve bölünen–bölen–bölüm–kalan ilişkisi',KY)
kart('K-BLNB-02','2, 4, 5, 8, 10 ile bölünebilme','Son basamak, son iki ya da son üç basamak kuralı yalnızca o basamakları sınırlar; geri kalan rakamlar serbesttir.','Rakamlar toplamı kuralını karıştırmak; 4 yerine 2, 8 yerine 4 kuralını uygulamak; son iki basamağı eksik yazmak.','kolay','düz',2,'blb-son','Son basamaklarla bölünebilme','ÖSYM (4, 8 ile bölünebilme) · yayın: 857a, 19321x tipi')
kart('K-BLNB-03','3, 9, 11 ile bölünebilme','Rakamlar toplamı (3, 9) ve artı–eksi (alternatif) toplam (11) kuralları aynı sayıya birlikte uygulanıp bilinmeyen rakamlar bulunur.','11 kuralında işaretleri yanlış sıralamak; 99’u 9 ve 11’e ayırmamak; birden çok çözümü elememek.','zor','düz',4,'blb-rakam','Rakam toplamı ve 11 kuralıyla rakam bulma','ÖSYM (3, 9, 11) · yayın: 23a58b tipi')
kart('K-BLNB-04','Aralarında asal çarpanlarla bölünebilme','6, 12, 15, 18, 36, 72 gibi sayılara bölünme, aralarında asal çarpanlarının koşullarıyla birlikte aranır ve adaylar taranır.','Çarpanları aralarında asal olmayan seçmek (36 = 6 × 6 gibi); koşullardan birini atlamak; rakamların farklı olması koşulunu unutmak.','orta','düz',3,'blb-asal','Aralarında asal çarpanlarla bölünebilme','ÖSYM (6, 12, 15, 18, 36 ile bölünebilme) · yayın: 6a7b, 8x46y, 325ab tipleri')
kart('K-BLNB-05','Kalan aritmetiği ve eş kalan','Toplam ve çarpımın kalanı kalanlardan bulunur; birden çok bölende kalan koşulları ortak kat ve eşit kalan (n + k) fikriyle tek bir ifadeye indirilir; günlerde kalan 7’ye göre alınır.','Kalanları bölenden sonra yeniden indirgememek; kalan yerine bölümü almak; sayma başlangıcını yanlış seçmek.','orta','hikâyeli',3,'blb-kalan','Kalan aritmetiği ve ortak kalan koşulları','ÖSYM (gün/saat kalanı, artan eşya) · yayın: paketleme, nöbet ve gün soruları')
kart('K-BLNB-06','Tanımlı sayılar ve makineler','Soruda tanımlanan kalan koşulu ya da makine kuralı eşitliğe çevrilir, periyot (ortak kat) bulunur ve aralıktaki değerler sayılır.','Periyodu yanlış kurmak; ilk ve son değeri aralığa göre denetlememek; sınır değeri (0, 60) hesaba katmak ya da katmamak.','zor','yeni nesil',4,'blb-tanimli','Kalan koşuluyla tanımlı sayılar ve makine soruları','ÖSYM 2022–2026 (yeni nesil tanımlı kavram) · yayın: kalan koşullu sayma')

# ---------- 01 · kolay · en büyük bölünen ----------
mx=max(n for n in range(0,500) if n//13==9); assert mx==129 and 13*9+12==129
assert 13*9==117 and 9*13+8==125 and 117+9==126 and 13*9+11==128 and 13*10==130
mk(P,'0001',tipId='blb-bolme',tip='Bölme işlemi ve bölünen–bölen–bölüm–kalan ilişkisi',z='kolay',alt='Bölme İşlemi',kaz='Bölme işleminde bölen ve bölüm verildiğinde kalanın alabileceği en büyük değerle en büyük bölüneni bulur.',kalip='düz',adim=2,
 kart='K-BLNB-01 (bölme işlemi) · bölen ve bölüm verilip en büyük bölünen istenir',
 metin='Doğal sayılarla yapılan bir bölme işleminde bölen 13, bölüm 9’dur.\nBuna göre bölünen en çok kaçtır?',
 dogru=129,yan=[(117,'Kalanı 0 almış; “en çok” denince kalanın da en büyük olması gerektiğini atlamış.','dikkat'),(126,'Kalanı bölüme eşit (9) almış; kalan bölenden küçük en büyük değeri (12) almalıydı.','dikkat'),(128,'Kalanı bölenden iki küçük (11) almış; bölenden bir küçük olan 12 mümkündür.','islem'),(130,'Kalanı bölene eşit (13) almış; kalan bölenden küçük olmalıdır, 13 olsaydı bölüm 10 olurdu.','bilgi')],
 istenen='Bölünenin en büyük değeri.',
 ip=['Bölünen = 13 × 9 + kalan; kalan en çok kaç olabilir?'],
 bilgi=[KAL],
 ad=[A('Eşitliği yaz','Bölünen, bölen ile bölümün çarpımına kalanın eklenmesiyle bulunur.','bölünen = 13 × 9 + kalan'),A('Kalanı en büyük al','Kalan bölenden küçük olmalı; en büyük değeri bölenin bir eksiğidir.','0 ≤ kalan ≤ 12 → kalan = 12'),A('Hesapla','Çarpımı bulup kalanı ekle.','13 × 9 + 12 = 117 + 12 = 129')],
 puf='Bölünen en büyük olsun isteniyorsa kalan bölenin bir eksiğidir, en küçük olsun isteniyorsa 0 (kalan sıfırdan farklıysa 1) alınır.')

# ---------- 02 · kolay · 5A2, 4 ile ----------
s2=[a for a in range(10) if int(f'5{a}2')%4==0]; assert s2==[1,3,5,7,9] and sum(s2)==25
assert sum(a for a in range(10) if a%2==0)==20 and sum(a for a in range(10) if (7+a)%3==0)==15 and sum(range(10))==45
assert sum(a for a in range(10) if int(f'5{a}2')%8==0)==15 and [a for a in range(10) if (50+a)%4==0]==[2,6]
mk(P,'0002',tipId='blb-son',tip='Son basamaklarla bölünebilme',z='kolay',alt='Bölünebilme Kuralları',kaz='4 ile bölünebilme kuralını son iki basamağa uygulayarak bilinmeyen rakamın değerlerini bulur.',kalip='düz',adim=2,
 kart='K-BLNB-02 (son basamak kuralları) · 4 ile bölünebilme, A’nın değerleri toplamı',
 metin='Bir mağazada raflar, A bir rakam olmak üzere 5A2 biçiminde üç basamaklı numaralarla numaralandırılmıştır. Numarası 4’ün katı olan raflar kampanyaya alınmıştır.\nBuna göre kampanyaya alınan rafların numaralarında A yerine yazılan rakamların toplamı kaçtır?',
 dogru=25,yan=[(8,'Yüzler ve onlar basamağındaki 5A’ya bakıp 4’ün katı olan 52 ve 56’dan A = 2 ve 6 bulmuş; 4 ile bölünme son iki basamağa bağlıdır.','bilgi'),(15,'8 ile bölünebilme kuralını (son üç basamak) uygulayıp A = 1, 5, 9 bulmuş.','bilgi'),(20,'Sayının çift olması için A’yı çift sanmış; A çift olunca 4’e bölünme sağlanmaz (502 gibi).','bilgi'),(45,'Sayı hep çift olduğu için 4’e bölüneceğini sanıp A’nın tüm değerlerini (0–9) toplamış.','bilgi')],
 istenen='A’nın alabileceği değerlerin toplamı.',
 ip=['4 ile bölünme yalnız son iki basamağa bağlıdır: A2 sayısı 4’ün katı olmalı.'],
 bilgi=[S4],
 ad=[A('Son iki basamağa bak','5 yüzler basamağında olduğundan 4’e bölünmeyi etkilemez; A2 sayısı 4’ün katı olmalıdır.','A2 = 10 × A + 2'),A('Değerleri dene','A2’nin 4’ün katı olduğu rakamları bul: 02, 12, 22, …, 92 içinden.','12 = 4 × 3 · 32 = 4 × 8 · 52 = 4 × 13 · 72 = 4 × 18 · 92 = 4 × 23 → A = 1, 3, 5, 7, 9'),A('Topla','Bulunan rakamları topla.','1 + 3 + 5 + 7 + 9 = 25')],
 puf='4 ile bölünebilmede yalnız son iki basamağa bak; yüzler ve sonrası fark etmez.')

# ---------- 03 · kolay · gün kalanı ----------
gun=['Pazartesi','Salı','Çarşamba','Perşembe','Cuma','Cumartesi','Pazar']
assert gun[(0+11*10)%7]=='Cumartesi' and 110%7==5 and gun[(12*10)%7]=='Salı' and gun[(10*10)%7]=='Çarşamba' and gun[5+1]=='Pazar' and gun[4]=='Cuma'
assert [gun[(0+(k-1)*10)%7] for k in (1,2,3,4,5,6,7,8)]==['Pazartesi','Perşembe','Pazar','Çarşamba','Cumartesi','Salı','Cuma','Pazartesi']
mk(P,'0003',tipId='blb-kalan',tip='Kalan aritmetiği ve ortak kalan koşulları',z='kolay',alt='Günlerde Kalan',kaz='Belirli aralıklarla tekrarlanan bir işte gün sayısının 7 ile bölümünden kalanını kullanarak haftanın gününü bulur.',kalip='hikâyeli',adim=3,
 kart='K-BLNB-05 (kalan aritmetiği) · 10 günde bir sulama, 12. sulamanın günü',
 metin='Bir bahçıvan, çiçeklere 10 günde bir su vermektedir. İlk sulamayı pazartesi günü yapmıştır.\nBuna göre 12. sulamayı hangi gün yapar?',
 dogru='Cumartesi',sira=['Salı','Çarşamba','Perşembe','Cuma','Cumartesi'],
 yan=[('Salı','12 sulama için 12 × 10 = 120 gün saymış; ilk sulamadan 12. sulamaya 11 aralık vardır.','dikkat'),('Çarşamba','10 aralık sayıp 100 gün ilerlemiş; 12. sulamaya kadar 11 aralık vardır.','dikkat'),('Cuma','Kalan 5’i bulmuş ama pazartesi gününü de sayarak (pazartesi 1, … cuma 5) Cuma demiş.','dikkat'),('Perşembe','Yalnız ilk aralığı (10 gün = 7 + 3) düşünüp 3 gün ilerlemiş.','dikkat')],
 istenen='12. sulamanın yapıldığı gün.',
 ip=['İlk sulamadan 12. sulamaya kaç gün geçtiğini bul; 7 gün sonra aynı gün gelir.'],
 bilgi=[GUN],
 ad=[A('Geçen günü bul','1. sulama ile 12. sulama arasında 11 aralık vardır, her aralık 10 gün.','11 × 10 = 110 gün'),A('7 ile böl','Haftalar aynı günü verir, yalnız kalan önemlidir.','110 = 7 × 15 + 5 → kalan 5'),A('Günü yaz','Pazartesiden 5 gün sonrası: salı, çarşamba, perşembe, cuma, cumartesi.','Pazartesi + 5 = Cumartesi')],
 puf='Tekrarlanan işlerde ilk iş ile n. iş arasındaki aralık sayısı (n − 1) kadar adım vardır; günü bulmak için toplam gün 7’ye bölünür.')

# ---------- 04 · kolay · iki tepsi, kalanların toplamı ----------
for a in range(6,200):
    for b in range(6,200):
        if a%6==4 and b%6==5: assert (a+b)%6==3
assert (4*5)%6==2 and (4+5)//6==1 and (4+5)%6==3
mk(P,'0004',tipId='blb-kalan',tip='Kalan aritmetiği ve ortak kalan koşulları',z='kolay',alt='Kalanlarla İşlem',kaz='İki sayının kalanlarından toplamlarının kalanını bulur.',kalip='hikâyeli',adim=2,
 kart='K-BLNB-05 (kalan aritmetiği) · iki tepsideki poğaçalar birleştirilince kalan',
 metin='Bir fırında iki ayrı tepsideki poğaçalar sayılıyor. Birinci tepsideki poğaçalar 6’şarlı paketlendiğinde 4, ikinci tepsideki poğaçalar 6’şarlı paketlendiğinde 5 poğaça paketlere girmeden kalıyor.\nİki tepsideki tüm poğaçalar birleştirilip 6’şarlı paketlenirse kaç poğaça paketlere girmeden kalır?',
 dogru=3,yan=[(1,'Kalanların toplamının (9) 6’ya bölümünden bölümü (1) almış; sorulan kalandır.','dikkat'),(2,'Toplam yerine kalanları çarpmış: 4 × 5 = 20, 20’nin 6 ile kalanı 2.','bilgi'),(4,'Yalnız birinci tepsinin kalanını (4) yazmış; ikinci tepsiyi hesaba katmamış.','dikkat'),(9,'4 + 5 = 9 bulup 9’u kalan sanmış; 9, 6’dan büyük olduğundan kalan olamaz (bir paket daha yapılır).','islem')],
 istenen='Birleştirilince artan poğaça sayısı.',
 ip=['Her tepsiyi 6 × (paket sayısı) + kalan olarak yaz ve toplayıp 6’nın katlarını ayır.'],
 bilgi=[KALAR],
 ad=[A('Tepsileri yaz','Birinci tepsi 6x + 4, ikinci tepsi 6y + 5 poğaçadır.','6x + 4 · 6y + 5'),A('Topla','6’nın katlarını ayır; kalan toplam 9 olur ve 9, bir paket daha yapar.','6x + 6y + 9 = 6 × (x + y + 1) + 3'),A('Kalanı oku','6’nın katı olmayan kısım artan poğaça sayısıdır.','kalan = 3')],
 puf='Kalanlar toplanınca toplam bölenden büyük çıkabilir; sonucu bir kez daha bölenle böl.')

# ---------- 05 · orta · 3A7B, 11, A×B en büyük ----------
s5=[(a,b) for a in range(10) for b in range(10) if int(f'3{a}7{b}')%11==0]; assert all(a+b==10 for a,b in s5) and len(s5)==9
assert max(a*b for a,b in s5)==25 and max(a*b for a,b in s5 if a!=b)==24
assert max(a*b for a in range(10) for b in range(10) if a+b==12)==36 and max(a*b for a in range(10) for b in range(10) if a-b==4)==45
mk(P,'0005',tipId='blb-rakam',tip='Rakam toplamı ve 11 kuralıyla rakam bulma',z='orta',alt='Bölünebilme Kuralları',kaz='11 ile bölünebilme kuralıyla iki bilinmeyen rakam arasındaki bağıntıyı bulup çarpımın en büyük değerini hesaplar.',kalip='düz',adim=3,
 kart='K-BLNB-03 (3, 9, 11) · 3A7B sayısı 11 ile bölünür, A × B en büyük',
 metin='3A7B dört basamaklı bir doğal sayıdır; A ve B birer rakamdır. Bu sayı 11’in katı olduğuna göre A × B çarpımı en fazla kaç olabilir?',
 dogru=25,yan=[(10,'A + B toplamını (10) bulup çarpımı istenen değerle karıştırmış.','dikkat'),(24,'A + B = 10 bulup eşit olmayan ilk çifti (4, 6) almış; toplamı sabit çarpımın en büyüğü için rakamlar eşit alınmalıdır.','islem'),(36,'Rakamlar toplamı kuralını 11’e uygulayıp 10 + A + B = 22 yazmış; A + B = 12, çarpım 36.','bilgi'),(45,'İşaretleri yanlış dizip A − B = 4 bulmuş; en büyük çarpım 9 × 5 = 45.','islem')],
 istenen='A × B çarpımının en büyük değeri.',
 ip=['Sağdan başlayarak +, −, +, − işaretleriyle topla: B − 7 + A − 3 sonucu 11’in katı olmalı.'],
 bilgi=[R11],
 ad=[A('Kuralı uygula','Sağdan işaretler: B (+), 7 (−), A (+), 3 (−). Sonuç 0 ya da 11’in katı olmalı.','B − 7 + A − 3 = A + B − 10'),A('Rakamlara sığdır','A + B en çok 18 olabilir; A + B − 10 yalnız 0 olabilir (−11 ya da 11 mümkün değildir).','A + B = 10'),A('Çarpımı en büyük yap','Toplamı sabit iki rakamın çarpımı, rakamlar birbirine en yakınken en büyüktür.','A = B = 5 → 3575 = 11 × 325 · A × B = 5 × 5 = 25')],
 puf='Toplamı sabit olan iki sayının çarpımı, sayılar eşitken (ya da en yakınken) en büyüktür.')

# ---------- 06 · orta · 7A2B, 18 ile, kaç sayı ----------
s6=[(a,b) for a in range(10) for b in range(10) if int(f'7{a}2{b}')%18==0]; assert s6==[(0,0),(1,8),(3,6),(5,4),(7,2),(9,0)] and len(s6)==6
assert len([1 for a in range(10) for b in range(10) if (a+b)%9==0])==12 and len([1 for a in range(10) for b in range(10) if a+b==9])==10
assert len([1 for a in range(10) for b in range(0,10,2) if a+b==9])==5 and len(s6)+1==7
mk(P,'0006',tipId='blb-asal',tip='Aralarında asal çarpanlarla bölünebilme',z='orta',alt='Bölünebilme Kuralları',kaz='18 ile bölünebilmeyi 2 ve 9 koşullarına ayırarak koşulu sağlayan sayıların adedini bulur.',kalip='düz',adim=3,
 kart='K-BLNB-04 (aralarında asal çarpanlar) · 7A2B sayısı 18 ile bölünür, kaç farklı sayı',
 metin='A ve B birer rakam olmak üzere, dört basamaklı 7A2B sayısı 18 ile tam bölünebilmektedir.\nBuna göre bu koşulu sağlayan kaç farklı 7A2B sayısı yazılabilir?',
 dogru=6,yan=[(5,'A + B = 9 durumlarını sayıp A = B = 0 (7020) çözümünü unutmuş.','dikkat'),(7,'A = B = 9 (7929) sayısını da saymış; birler basamağı 9 çift olmadığı için 2’ye bölünmez.','dikkat'),(10,'A + B = 9 koşulunu bulmuş, B’nin çift olması koşulunu uygulamamış ve 0 ile 18 toplamlarını da atlamış.','dikkat'),(12,'Yalnız 9 ile bölünebilmeyi uygulayıp (A + B = 0, 9, 18) 2 ile bölünebilmeyi unutmuş.','bilgi')],
 istenen='Koşulu sağlayan farklı sayıların adedi.',
 ip=['18 = 2 × 9; B çift olmalı ve rakamlar toplamı 9’un katı olmalı: A + B hangi değerleri alabilir?'],
 bilgi=[ASAL,R9],
 ad=[A('Koşulları ayır','18 = 2 × 9 ve 2 ile 9 aralarında asal. Birler basamağı B çift, rakamlar toplamı 9’un katı olmalı.','B ∈ {0, 2, 4, 6, 8} · 7 + A + 2 + B = 9 + A + B'),A('A + B’yi sınırla','A + B, 0 ile 18 arasındadır ve 9’un katı olmalıdır.','A + B = 0, 9 ya da 18'),A('Çiftleri yaz','B çift olmak zorunda; A + B = 18 için B = 9 gerekir, çift değil, elenir.','A + B = 0: (0, 0) · A + B = 9: (9, 0), (7, 2), (5, 4), (3, 6), (1, 8)'),A('Say','Bulunan sayılar 7020, 7920, 7722, 7524, 7326, 7128.','1 + 5 = 6 sayı')],
 puf='Bileşik sayıyla bölünmede (18 = 2 × 9) çarpanların koşullarını ayrı ayrı yaz, ortak çözümleri say; hiçbirini unutma.')

# ---------- 07 · orta · bölünen, bölen, bölüm, kalan toplamı ----------
s7=[n for n in range(1,600) if (lambda q,r:q==r+5 and n+11+q+r==127)(n//11,n%11)]; assert s7==[103]
assert 11*9==99 and 99+9==108 and 103%11==4 and 103//11==9 and 14*4+71==127
mk(P,'0007',tipId='blb-bolme',tip='Bölme işlemi ve bölünen–bölen–bölüm–kalan ilişkisi',z='orta',alt='Bölme İşlemi',kaz='Bölünen, bölen, bölüm ve kalan toplamı ile bölüm–kalan ilişkisinden bölünen sayıyı bulur.',kalip='düz',adim=3,
 kart='K-BLNB-01 (bölme işlemi) · dört terimin toplamı + bölüm kalandan 5 fazla',
 metin='Doğal sayılarla yapılan bir bölme işleminde bölen 11’dir. Bölüm, kalandan 5 fazladır. Bölünen, bölen, bölüm ve kalanın toplamı 127’dir.\nBuna göre bölünen kaçtır?',
 dogru=103,yan=[(4,'Eşitliği çözüp kalanı (4) bulmuş ama bölünenin sorulduğunu unutmuş.','dikkat'),(9,'Bölümü (9) bulup durmuş.','dikkat'),(99,'Bölünen = bölen × bölüm yazıp kalanı eklememiş.','bilgi'),(108,'Bölünen = bölen × bölüm + bölüm yazmış (kalan yerine bölümü eklemiş).','bilgi')],
 istenen='Bölünen sayı.',
 ip=['Kalana r de; bölüm r + 5 olur. Bölünen = 11 × (r + 5) + r.'],
 bilgi=[KAL],
 ad=[A('Her şeyi r ile yaz','Kalan r, bölüm r + 5, bölünen 11 × (r + 5) + r.','bölünen = 11 × (r + 5) + r = 12 × r + 55'),A('Toplamı kur','Dört terimi topla ve 127’ye eşitle.','(12 × r + 55) + 11 + (r + 5) + r = 14 × r + 71 = 127'),A('r’yi bul','Denklemi çöz.','14 × r = 56 → r = 4 · bölüm = 9'),A('Bölüneni hesapla','Kontrol: kalan 4 < 11.','11 × 9 + 4 = 103')],
 puf='Bölme sorularında kalanı bilinmeyen alıp bölüneni bölen × bölüm + kalan ile yaz; kalan < bölen koşulunu kontrol et.')

# ---------- 08 · orta · öncüllü n = 6k+5 ----------
I=II=III=True
for n in range(5,1000,6):
    I=I and n%2==1; II=II and n%3==2; III=III and n%4==1
assert I and II and (not III) and 5%4==1 and 11%4==3
mk(P,'0008',tipId='blb-kalan',tip='Kalan aritmetiği ve ortak kalan koşulları',z='orta',alt='Kalanlarla İşlem',kaz='6 ile bölümünden kalanı verilen bir sayının 2, 3 ve 4 ile bölümünden kalanlarını çözümleyerek yorumlar.',kalip='öncüllü',adim=3,
 kart='K-BLNB-05 (kalan aritmetiği) · 6 ile bölümünden kalan 5 olan sayı için öncüllü ifadeler',
 metin='n bir doğal sayıdır ve n sayısının 6 ile bölümünden kalan 5’tir.\nBuna göre,\nI. n tek sayıdır.\nII. n sayısının 3 ile bölümünden kalan 2’dir.\nIII. n sayısının 4 ile bölümünden kalan 1’dir.\nifadelerinden hangileri kesinlikle doğrudur?',
 dogru='I ve II',sira=['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III'],
 yan=[('Yalnız I','II’de n = 6k + 5 = 3 × (2k + 1) + 2 yazıp 3 ile kalanı bulmamış.','bilgi'),('Yalnız II','6k çift, 5 tek olduğundan n’nin tek olduğunu görmemiş.','dikkat'),('I ve III','II’de 6k + 5’in 3 ile bölümünden kalanı bulamayıp II’yi yanlış saymış; III’ü yalnız n = 5 ile doğrulamış.','dikkat'),('I, II ve III','III’ü yalnız n = 5 ile denemiş; n = 11 için 4 ile kalan 3’tür.','dikkat')],
 istenen='Kesinlikle doğru olan ifadeler.',
 ip=['n = 6k + 5 yaz ve n = 5, 11, 17 gibi birkaç değerle de dene.'],
 bilgi=[KAL,TK],
 ad=[A('Sayıyı yaz','6 ile bölümünden kalan 5 ise n, 6k + 5 biçimindedir.','n = 6k + 5'),A('I ve II’yi incele','6k çifttir, 5 ekleyince tek olur. 6k + 5 = 3 × (2k + 1) + 2 olduğundan 3 ile kalan 2’dir.','I doğru · II doğru'),A('III’ü dene','n = 5 için 4 ile kalan 1, n = 11 için 4 ile kalan 3 olduğundan III her zaman doğru değildir.','5 = 4 × 1 + 1 · 11 = 4 × 2 + 3'),A('Sonuç','Kesinlikle doğru olanlar I ve II.','I ve II')],
 puf='Kalan verilen sayıyı n = bölen × k + kalan yaz; öncüllerde kesin doğruyu çözümlemeyle kanıtla, yanlışı bir örnekle çürüt.')

# ---------- 09 · orta · 2a + 3b ----------
for a in range(7,300,9):
    for b in range(5,300,9): assert (2*a+3*b)%9==2
assert 29%9==2 and (7+5)%9==3 and 35%9==8 and 5+6==11 and 14%9==5 and 15%9==6
mk(P,'0009',tipId='blb-kalan',tip='Kalan aritmetiği ve ortak kalan koşulları',z='orta',alt='Kalanlarla İşlem',kaz='İki sayının kalanlarından katsayılı bir toplamın kalanını bulur.',kalip='düz',adim=3,
 kart='K-BLNB-05 (kalan aritmetiği) · iki sayının 9 ile kalanından 2a + 3b’nin kalanı',
 metin='a ve b doğal sayılarının 9 ile bölümünden kalanlar sırasıyla 7 ve 5’tir.\nBuna göre 2a + 3b sayısının 9 ile bölümünden kalan kaçtır?',
 dogru=2,yan=[(3,'Katsayıları (2 ve 3) hesaba katmamış; 7 + 5 = 12’nin 9 ile kalanını (3) bulmuş.','bilgi'),(8,'Toplam yerine kalanları çarpmış; 7 × 5 = 35’in 9 ile kalanı 8.','bilgi'),(11,'2 × 7 = 14’ün kalanı 5, 3 × 5 = 15’in kalanı 6 bulup 5 + 6 = 11 yazmış; toplamı yeniden 9 ile bölmemiş.','islem'),(29,'2 × 7 + 3 × 5 = 29 bulup 9 ile bölümünden kalanı almamış.','islem')],
 istenen='2a + 3b’nin 9 ile bölümünden kalan.',
 ip=['Her sayıyı 9’un katı artı kalan biçiminde yaz ve ifadede 9’un katlarını ayır.'],
 bilgi=[KALAR],
 ad=[A('Sayıları yaz','Kalanlarla çarpanlar bölenin katı olarak ayrılır.','a = 9p + 7 · b = 9q + 5'),A('İfadeyi kur','Her sayıyı katsayısıyla çarp ve topla.','2a + 3b = 18p + 14 + 27q + 15 = 18p + 27q + 29'),A('Kalanı oku','29 = 27 + 2 olduğundan 9’un katı olmayan kısım 2’dir.','2a + 3b = 9 × (2p + 3q + 3) + 2 → kalan 2')],
 puf='Kalanlar aynı bölenle işlem görünce sonuç kalanlarla hesaplanıp tekrar bölenle bölünür: (2 × 7 + 3 × 5) ÷ 9 → kalan 2.')

# ---------- 10 · orta · 4A6B, farklı rakamlar ----------
s10=[(a,b) for a in range(10) for b in range(10) if len(set(f'4{a}6{b}'))==4 and int(f'4{a}6{b}')%5==1 and int(f'4{a}6{b}')%3==0]; assert s10==[(7,1)]
assert 7-1==6 and 1-1==0 and 4-1==3 and 5-6==-1 and 8-6==2
for a,b in ((1,1),(4,1),(5,6),(8,6)):
    n=int(f'4{a}6{b}'); assert n%5==1 and n%3==0 and len(set(str(n)))<4
mk(P,'0010',tipId='blb-asal',tip='Aralarında asal çarpanlarla bölünebilme',z='orta',alt='Bölünebilme Kuralları',kaz='5 ile bölümünden kalan ve 3 ile bölünebilme koşullarını rakamların farklı olması koşuluyla birlikte uygulayarak rakamları bulur.',kalip='düz',adim=3,
 kart='K-BLNB-04 (aralarında asal çarpanlar) · 5 ile kalan 1, 3 ile bölünür, rakamlar farklı',
 metin='A ve B birer rakam olmak üzere, rakamları birbirinden farklı dört basamaklı 4A6B sayısının 5 ile bölümünden kalan 1’dir. Bu sayı 3 ile tam bölünebilmektedir.\nBuna göre A − B farkı kaçtır?',
 dogru=6,yan=[(-1,'B = 6 ile A = 5 almış (4566); 6 rakamı iki kez geçtiği için rakamları farklı değildir.','dikkat'),(0,'A = B = 1 (4161) seçmiş; rakamlar farklı olmalı.','dikkat'),(2,'B = 6 ile A = 8 almış (4866); 6 rakamı tekrarlanıyor.','dikkat'),(3,'A = 4, B = 1 (4461) seçmiş; 4 rakamı tekrarlanıyor.','dikkat')],
 istenen='A − B farkı.',
 ip=['Kalan 1 ise birler basamağı iki farklı rakam olabilir; hangisi sayıda zaten var?'],
 bilgi=[B('5 ile bölümden kalan','sayının 5 ile bölümünden kalan, birler basamağının 5 ile bölümünden kalanıdır. Örnek: 4726 → birler 6, 6 = 5 × 1 + 1, kalan 1'),R9],
 ad=[A('Birler basamağı','Kalan 1 ise B = 1 ya da B = 6; 6 zaten sayıda var ve rakamlar farklı olmalı.','B = 1'),A('3 ile bölünme','Rakamlar toplamı 3’ün katı olmalı.','4 + A + 6 + 1 = 11 + A → A = 1, 4 ya da 7'),A('Farklı rakamlar','1 ve 4 sayıda zaten var; geriye A = 7 kalır.','A = 7 → 4761 = 3 × 1587 · A − B = 7 − 1 = 6')],
 puf='Koşullar çoğaldığında önce birler basamağını sınırla, sonra rakamlar toplamı ve “farklı rakam” koşuluyla adayları ele.')

# ---------- 11 · orta · kütüphane, 4'te 3 / 6'da 5 artan ----------
s11=[n for n in range(101,200) if n%4==3 and n%6==5]; assert s11==[107,119,131,143,155,167,179,191] and len(s11)==8
assert len([n for n in range(101,200) if n%6==5])==17 and len([n for n in range(101,200) if n%4==3])==25
assert (191-107)//12==7 and -(-(200-100)//12)==9
mk(P,'0011',tipId='blb-kalan',tip='Kalan aritmetiği ve ortak kalan koşulları',z='orta',alt='Ortak Kalan',kaz='Farklı bölenlerle verilen ve bölenden 1 eksik olan kalan koşullarını ortak katla birleştirip aralıktaki değerleri sayar.',kalip='hikâyeli',adim=3,
 kart='K-BLNB-05 (eş kalan, n + 1) · 4’te 3, 6’da 5 kalan, aralıkta kaç değer',
 metin='Bir kütüphanedeki kitapların sayısı 100’den çok, 200’den azdır. Bu kitaplar 4’erli gruplara ayrıldığında 3, 6’şarlı gruplara ayrıldığında 5 kitap gruplara girmeden kalmaktadır.\nBuna göre kitap sayısı kaç farklı değer alabilir?',
 dogru=8,yan=[(7,'107’den 191’e kadar olan değerlerin farkını 12’ye bölüp (84 ÷ 12 = 7) uç değeri saymayı unutmuş.','islem'),(9,'(200 − 100) ÷ 12 = 8,33 değerini yukarı yuvarlayıp 9 bulmuş.','islem'),(17,'Yalnız 6 ile kalan 5 koşulunu (101, 107, …, 197) sayıp 4 ile koşulu atlamış.','dikkat'),(25,'Yalnız 4 ile kalan 3 koşulunu (103, 107, …, 199) sayıp 6 ile koşulu atlamış.','dikkat')],
 istenen='Kitap sayısının alabileceği farklı değerlerin adedi.',
 ip=['4’e bölümünden kalan 3 ve 6’ya bölümünden kalan 5 ise kitap sayısının 1 fazlası hem 4’ün hem 6’nın katıdır.'],
 bilgi=[KAL,EKSI],
 ad=[A('Ortak koşulu yaz','Kalanlar bölenlerden birer eksiktir: n + 1, hem 4’ün hem 6’nın katı, yani 12’nin katıdır.','n + 1 = 12 × k'),A('Aralığı uygula','n, 101 ile 199 arasında olmalı: n + 1, 102 ile 200 arasında.','12 × 9 = 108 · … · 12 × 16 = 192 (12 × 17 = 204 çok büyük)'),A('Say','k = 9’dan 16’ya kadar değerler alır.','16 − 9 + 1 = 8 değer (n = 107, 119, …, 191)')],
 puf='Kalanlar bölenlerden aynı farkla eksikse sayıya o fark kadar ekle; sonuç ortak kat (OKEK) olur.')

# ---------- 12 · orta · makine: 5n + 9, 7 ile kalan 0 ----------
s12=[n for n in range(100,1000) if (5*n+9)%7==0]; assert s12[0]==106 and all(n%7==1 for n in s12)
assert 99%7==1 and (5*99+9)%7==0 and 105%7==0 and 104%7==6 and 113%7==1 and 113>106 and min(n for n in range(100,1000) if n%7==0)==105 and min(n for n in range(100,1000) if n%7==6)==104
mk(P,'0012',tipId='blb-tanimli',tip='Kalan koşuluyla tanımlı sayılar ve makine soruları',z='orta',alt='Makine ve Şifre',kaz='Bir makinenin işlem kuralını bölünebilme koşuluna çevirip en küçük üç basamaklı değeri bulur.',kalip='yeni nesil',adim=3,
 kart='K-BLNB-06 (tanımlı kural, makine) · 5n + 9’un 7 ile kalanı 0, en küçük üç basamaklı n',
 metin='Bir makine, kendisine verilen doğal sayıyı önce 5 ile çarpıyor, sonra 9 ekliyor ve elde ettiği sonucun 7 ile bölümünden kalanı ekrana yazıyor.\nBuna göre ekranda 0 görülen en küçük üç basamaklı doğal sayı kaçtır?',
 dogru=106,yan=[(99,'n = 7k + 1 bulmuş ama 99’un üç basamaklı olmadığını (iki basamaklı) gözden kaçırmış.','dikkat'),(104,'5n + 9 yerine 5n − 9’un 7’nin katı olmasını isteyip n = 7k + 6 bulmuş.','islem'),(105,'+ 9’u unutup 5n’nin 7’nin katı olmasını istemiş; n, 7’nin katı olur.','dikkat'),(113,'n = 7k + 1 biçimini bulmuş ama 106 yerine bir sonraki değeri (113) yazmış.','dikkat')],
 istenen='Ekranda 0 yazdıran en küçük üç basamaklı sayı.',
 ip=['5n + 9 = 5 × (n − 1) + 14 yazılabilir; 14 zaten 7’nin katıdır.'],
 bilgi=[KALAR],
 ad=[A('Koşulu kur','Kalan 0 ise 5n + 9 sayısı 7’nin katıdır.','5n + 9 = 5 × (n − 1) + 14'),A('Sadeleştir','14, 7’nin katı olduğundan 5 × (n − 1) de 7’nin katı olmalı; 5 ile 7 aralarında asaldır.','n − 1 = 7k → n = 7k + 1'),A('En küçüğü bul','n ≥ 100 için k en az 15 olur (7 × 14 + 1 = 99 iki basamaklı).','k = 15 → n = 106 (5 × 106 + 9 = 539 = 7 × 77)')],
 puf='Kalan koşuluyla verilen ifadeyi, bölenin katını ayırarak (14 gibi) sadeleştir; aralarında asal çarpanı atabilirsin.')

# ---------- 13 · orta · öncüllü, 12 ve 18'in katları ----------
I=II=III=True; Iex=False
for k in range(1,60):
    for m in range(1,60):
        a=12*k; b=18*m
        I=I and (a+b)%12==0; II=II and (a*b)%36==0; III=III and (a+b)%6==0
assert (not I) and II and III and (12+36)%12==0 and 12*18==216 and 216==36*6
mk(P,'0013',tipId='blb-asal',tip='Aralarında asal çarpanlarla bölünebilme',z='orta',alt='Katlar',kaz='Verilen sayıların katları için toplam ve çarpımın bölünebilme özelliklerini çözümleyerek yorumlar.',kalip='öncüllü',adim=3,
 kart='K-BLNB-04 (çarpanlar ve katlar) · 12 ve 18’in katlarının toplamı ve çarpımı için öncüllü ifadeler',
 metin='a ve b pozitif tam sayılardır. a sayısı 12 ile, b sayısı 18 ile tam bölünmektedir.\nBuna göre,\nI. a + b toplamı 12 ile tam bölünür.\nII. a × b çarpımı 36 ile tam bölünür.\nIII. a + b toplamı 6 ile tam bölünür.\nifadelerinden hangileri kesinlikle doğrudur?',
 dogru='II ve III',sira=['Yalnız I','Yalnız III','I ve II','I ve III','II ve III'],
 yan=[('Yalnız I','I’i a = 12, b = 36 örneğiyle doğrulayıp (48 = 12 × 4) II ve III’ü incelememiş.','dikkat'),('Yalnız III','a × b çarpımının 36’nın katı olduğunu görmemiş; 12 × 18 = 216 = 36 × 6.','bilgi'),('I ve II','I’i a = 12, b = 36 gibi tek örnekle doğrulamış; III’ün 6 × (2k + 3m) olduğunu görmemiş.','dikkat'),('I ve III','I’i a = 12, b = 36 örneğiyle doğrulamış; II’yi incelememiş.','dikkat')],
 istenen='Kesinlikle doğru olan ifadeler.',
 ip=['a = 12k ve b = 18m yazıp toplam ve çarpımı çarpanlarına ayır; I için k = m = 1 deneyebilirsin.'],
 bilgi=[KAT],
 ad=[A('Sayıları yaz','a, 12’nin; b, 18’in katıdır.','a = 12k · b = 18m'),A('III’ü ve I’i incele','Toplam 6’nın katıdır. k = m = 1 için 30, 12’nin katı değildir.','a + b = 6 × (2k + 3m) · III doğru · 12 + 18 = 30 → I yanlış'),A('II’yi incele','Çarpım 216 × k × m olur; 216 = 36 × 6.','a × b = 216 × k × m = 36 × (6km) · II doğru'),A('Sonuç','Kesin doğru olanlar II ve III.','II ve III')],
 puf='Bir sayının katını k ile yaz; toplamda ortak çarpanı, çarpımda çarpanları ayırarak bölünebilmeyi kanıtla.')

# ---------- 14 · zor · 3A58B, 36 ile ----------
s14=[(a,b,int(f'3{a}58{b}')) for a in range(10) for b in range(10) if int(f'3{a}58{b}')%36==0]
assert [x[2] for x in s14]==[32580,33588,37584] and max(x[2] for x in s14)==37584
assert max(int(f'3{a}58{b}') for a in range(10) for b in range(10) if int(f'3{a}58{b}')%4==0)==39588
assert max(int(f'3{a}58{b}') for a in range(10) for b in range(10) if int(f'3{a}58{b}')%12==0)==39588 and 39588%36!=0
assert max(int(f'3{a}58{b}') for a in range(10) for b in range(10) if int(f'3{a}58{b}')%9==0)==39582 and 39582%4!=0
mk(P,'0014',tipId='blb-asal',tip='Aralarında asal çarpanlarla bölünebilme',z='orta',alt='Bölünebilme Kuralları',kaz='36 ile bölünebilmeyi 4 ve 9 koşullarına ayırıp adayları tarayarak en büyük sayıyı bulur.',kalip='düz',adim=3,
 kart='K-BLNB-04 (aralarında asal çarpanlar) · 3A58B sayısı 36 ile bölünür, en büyük sayı',
 metin='A ve B birer rakam olmak üzere, beş basamaklı 3A58B sayısı 36 ile tam bölünebilmektedir.\nBuna göre bu koşulu sağlayan en büyük sayı kaçtır?',
 dogru=37584,yan=[(32580,'B = 0 için A = 2 bulup ilk bulduğu sayıyı yazmış; diğer durumları denememiş.','dikkat'),(33588,'B’yi en büyük (8) seçip yalnız onunla yetinmiş; B = 4 için A = 7 daha büyük sayıyı verir.','dikkat'),(39582,'Yalnız 9 ile bölünebilmeyi (A + B = 11) kullanıp 4 ile bölünmeyi atlamış; 82, 4’ün katı değildir.','bilgi'),(39588,'36 yerine 12’ye (3 ve 4) bölünme koşulunu uygulamış; 9’un katı olma koşulunu (A + B = 2 ya da 11) sağlamıyor.','bilgi')],
 istenen='Koşulu sağlayan en büyük sayı.',
 ip=['36 = 4 × 9; önce son iki basamak 8B’yi, sonra rakamlar toplamını kullan.'],
 bilgi=[S4,ASAL,R9],
 ad=[A('4 koşulu','Son iki basamak 8B, 4’ün katı olmalı.','80, 84, 88 → B = 0, 4, 8'),A('9 koşulu','Rakamlar toplamı 9’un katı olmalı: 3 + A + 5 + 8 + B = 16 + A + B.','A + B = 2 ya da 11 (A + B = 20 mümkün değil)'),A('Çiftleri bul','Her B için A’yı hesapla.','B = 0 → A = 2 · B = 4 → A = 7 · B = 8 → A = 3'),A('En büyüğü seç','Üç sayıyı karşılaştır.','32580 · 37584 · 33588 → en büyüğü 37584')],
 puf='36 gibi bileşik sayılarda 4 ve 9 koşullarını ayrı uygulayıp ortak çözümleri listeye al; en büyük/en küçük için tüm adayları karşılaştır.')

# ---------- 15 · zor · 2A42B, 99 ----------
s15=[(a,b) for a in range(10) for b in range(10) if int(f'2{a}42{b}')%99==0]; assert s15==[(7,3)] and 27423==99*277
assert 7*3==21 and 7-3==4 and 7+3==10 and 6*2==12 and 5*5==25 and 9*5==45 and int('29425')%9!=0 and int('26422')%9!=0
mk(P,'0015',tipId='blb-rakam',tip='Rakam toplamı ve 11 kuralıyla rakam bulma',z='zor',alt='Bölünebilme Kuralları',kaz='99 ile bölünebilmeyi 9 ve 11 kurallarına ayırıp iki bilinmeyen rakamı ortak çözümle bulur.',kalip='düz',adim=4,
 kart='K-BLNB-03 (3, 9, 11) · 2A42B sayısı 99 ile bölünür, A × B',
 metin='A ve B birer rakam olmak üzere, beş basamaklı 2A42B sayısı 99 ile tam bölünebilmektedir.\nBuna göre A × B çarpımı kaçtır?',
 dogru=21,yan=[(10,'A + B toplamını (10) bulup çarpımı hesaplamamış.','dikkat'),(12,'11 koşulundan A − B = 4 bulup (6, 2) çiftini seçmiş; rakamlar toplamı koşulunu (A + B = 10) denetlememiş.','dikkat'),(25,'Yalnız 9 koşulunu kullanıp A + B = 10 bulmuş ve (5, 5) çiftini seçmiş; 11 koşulunu uygulamamış.','bilgi'),(45,'11 koşulunda yüzlerle onlar gibi basamakları yanlış işaretleyip A − B = 4 koşulundan (9, 5) çiftini almış; 9 ile bölünmeyi denetlememiş.','islem')],
 istenen='A × B çarpımı.',
 ip=['99 = 9 × 11; 9 için rakamlar toplamını, 11 için artı–eksi toplamını yaz ve iki koşulu birleştir.'],
 bilgi=[R9,R11,ASAL],
 ad=[A('9 koşulu','Rakamlar toplamı 9’un katı olmalı: 2 + A + 4 + 2 + B = 8 + A + B.','A + B = 1 ya da 10'),A('11 koşulu','Sağdan işaretler: B (+), 2 (−), 4 (+), A (−), 2 (+).','B − 2 + 4 − A + 2 = B − A + 4 → A − B = 4 ya da −7'),A('Koşulları birleştir','A + B = 10 ve A − B = 4 → A = 7, B = 3. Diğer birleşimlerde A, B tam sayı olmaz.','A + B = 1 ile A − B = 4 ya da −7 → tam sayı çıkmaz · A + B = 10 ile A − B = −7 → A = 1,5'),A('Çarpımı bul','27423 = 99 × 277 ile doğrula.','A × B = 7 × 3 = 21')],
 puf='99’a bölünme 9 ve 11 koşullarının birleşimidir; iki koşuldan A + B ve A − B’yi bulup birlikte çöz.')

# ---------- 16 · zor · üç koşullu kalan, fark ----------
s16=[n for n in range(100,1000) if n%4==1 and n%6==3 and n%5==2]; assert s16[0]==117 and s16[-1]==957 and s16==list(range(117,958,60))
assert max(s16)-min(s16)==840 and 957-57==900 and 993-105==888 and 60*14==840
assert max(n for n in range(100,1000) if n%4==1 and n%6==3)-min(n for n in range(100,1000) if n%4==1 and n%6==3)==888 and 57%4==1 and 57%6==3 and 57%5==2
mk(P,'0016',tipId='blb-kalan',tip='Kalan aritmetiği ve ortak kalan koşulları',z='zor',alt='Ortak Kalan',kaz='Üç farklı bölenle verilen kalan koşullarını adım adım birleştirerek üç basamaklı en büyük ve en küçük sayıyı bulur.',kalip='düz',adim=4,
 kart='K-BLNB-05 (eş kalan, çoklu koşul) · 4’te 1, 6’da 3, 5’te 2 kalan, en büyük − en küçük',
 metin='Üç basamaklı bir n doğal sayısı 4 ile bölündüğünde 1, 6 ile bölündüğünde 3, 5 ile bölündüğünde 2 kalanını vermektedir.\nBuna göre n sayısının en büyük değeri ile en küçük değeri arasındaki fark kaçtır?',
 dogru=840,yan=[(60,'Sayılar arasındaki adımı (4, 6 ve 5’in OKEK’i 60) fark sanmış.','dikkat'),(888,'5 ile bölünme koşulunu atlayıp yalnız 4 ve 6 koşulundan (12k + 9) en büyük ile en küçüğün farkını almış.','dikkat'),(900,'En küçük değer olarak iki basamaklı 57’yi alıp 957 − 57 hesaplamış.','dikkat'),(957,'En büyük değeri bulup fark istendiğini atlamış.','dikkat')],
 istenen='En büyük ile en küçük n arasındaki fark.',
 ip=['Önce 4 ve 6 koşullarını tek bir ifadeye (12k + …) indir, sonra 5 koşulunu bu ifadede ara.'],
 bilgi=[KAL,TK],
 ad=[A('4 ve 6 koşulları','6 ile kalan 3 ise sayı tek ve 3’ün katıdır: 9, 21, 33, 45, 57, … 4 ile kalan 1 olanlar 12 aralıkla gelir.','n = 12k + 9 → 9, 21, 33, 45, 57, …'),A('5 koşulu','Bu listede 5 ile bölümünden kalan 2 olan ilk sayıyı bul: 9 (4), 21 (1), 33 (3), 45 (0), 57 (2).','n = 57 ilk sayı'),A('Ortak adım','Üç koşul birden 4, 6 ve 5’in ortak katı (OKEK = 60) aralıklarla tekrarlanır.','n = 60m + 57'),A('Üç basamaklı sınırlar','En küçüğü 117 (m = 1), en büyüğü 957 (m = 15); fark 14 adım.','957 − 117 = 14 × 60 = 840')],
 puf='Birkaç kalan koşulu aynı anda varsa ilk ortak sayıyı bul, sonra OKEK kadar adımla ilerle: n = OKEK × m + ilk sayı.')

# ---------- 17 · zor · ikiz kalanlı sayı ----------
s17=[n for n in range(1,61) if n%4==n%6]; assert len(s17)==20 and s17[:6]==[1,2,3,12,13,14]
assert len([n for n in range(0,61) if n%4==n%6])==21 and len([n for n in range(1,61) if n%12==0])==5 and len([n for n in range(1,61) if n%12 in (0,1)])==10
assert len([n for n in range(1,61) if n%12 in range(0,5)])==25 and len([n for n in range(1,61) if n%12 in range(0,6)])==30 and len([n for n in range(0,72) if n%4==n%6])==24
assert 14%4==2 and 14%6==2
mk(P,'0017',tipId='blb-tanimli',tip='Kalan koşuluyla tanımlı sayılar ve makine soruları',z='zor',alt='Tanımlı Sayılar',kaz='İki farklı bölenle kalanları eşit olan sayıların periyodunu bulup bir aralıkta sayar.',kalip='yeni nesil',adim=4,
 kart='K-BLNB-06 (tanımlı sayılar) · 4 ve 6 ile kalanları eşit, periyot 12',
 metin='Bir doğal sayının 4 ile bölümünden kalan, 6 ile bölümünden kalana eşitse bu sayıya “ikiz kalanlı sayı” denir. Örneğin 14 ikiz kalanlı bir sayıdır, çünkü 14 sayısının 4 ile de 6 ile de bölümünden kalan 2’dir.\nBuna göre 1’den 60’a kadar (1 ve 60 dahil) kaç ikiz kalanlı sayı vardır?',
 dogru=20,yan=[(21,'0’ı da saymış; sayılar 1’den başlıyor.','dikkat'),(24,'60’ı 12’ye bölüp 5 yerine 6 periyot alarak 6 × 4 hesaplamış.','islem'),(25,'Her periyotta kalan 0, 1, 2, 3, 4 olan beş sayı sanmış; kalan 4 için 4 ile kalan 0, 6 ile kalan 4’tür, eşit değildir.','dikkat'),(30,'Her periyotta kalan 0–5 olan altı sayı almış; kalan 4 ve 5 için kalanlar eşit değildir.','dikkat')],
 istenen='1’den 60’a kadar ikiz kalanlı sayıların adedi.',
 ip=['4 ve 6’nın ortak katı 12’dir; 12’lik bir dilimde kalanların hangi sayılar için eşit olduğuna bak.'],
 bilgi=[KAL],
 ad=[A('Periyodu bul','4 ve 6 ile kalanlar, sayı 12 arttığında aynı kalır; incelemek için 12 sayı yeter.','periyot = OKEK(4, 6) = 12'),A('12’lik dilimi tara','Kalanları yan yana yaz: n’nin 12 ile kalanı r olsun.','r = 0: 0 ve 0 ✓ · r = 1: 1 ve 1 ✓ · r = 2: 2 ve 2 ✓ · r = 3: 3 ve 3 ✓ · r = 4: 0 ve 4 ✗ · r = 5: 1 ve 5 ✗ · r = 6: 2 ve 0 ✗ · r = 7: 3 ve 1 ✗ · r = 8: 0 ve 2 ✗ · r = 9: 1 ve 3 ✗ · r = 10: 2 ve 4 ✗ · r = 11: 3 ve 5 ✗'),A('Dilim sayısı','1’den 60’a kadar 5 tam dilim vardır ve her dilimde 4 sayı uygundur.','60 ÷ 12 = 5 dilim'),A('Say','Dilim sayısını dilimdeki sayıyla çarp.','5 × 4 = 20')],
 puf='Periyodik koşullarda önce OKEK kadar uzunlukta bir dilimi tara, sonra aralıktaki dilim sayısıyla çarp; sınır (0, son sayı) değerlerini ayrı kontrol et.')

# ---------- 18 · zor · 72 ile bölünen, rakamları farklı en büyük ----------
mx72=max(n for n in range(1000,10000) if n%72==0 and len(set(str(n)))==4); assert mx72==9864 and 9864==72*137
assert max(n for n in range(1000,10000) if n%72==0)==9936 and len(set('9936'))==3
assert max(n for n in range(1000,10000) if n%8==0 and len(set(str(n)))==4)==9872 and 9872%9!=0
assert max(n for n in range(1000,10000) if n%9==0 and len(set(str(n)))==4)==9873 and 9873%8!=0
assert max(n for n in range(1000,10000) if n%12==0 and len(set(str(n)))==4)==9876 and 9876%72!=0 and 873%8!=0 and 864%8==0
mk(P,'0018',tipId='blb-asal',tip='Aralarında asal çarpanlarla bölünebilme',z='zor',alt='Bölünebilme Kuralları',kaz='72 ile bölünebilmeyi 8 ve 9 koşullarına ayırıp rakamları farklı en büyük dört basamaklı sayıyı bulur.',kalip='düz',adim=4,
 kart='K-BLNB-04 (aralarında asal çarpanlar) · rakamları farklı, 72 ile bölünen en büyük dört basamaklı sayı',
 metin='Rakamları birbirinden farklı dört basamaklı doğal sayılar arasında 72 ile tam bölünebilen en büyük sayı kaçtır?',
 dogru=9864,yan=[(9872,'Yalnız 8 ile bölünebilme ve farklı rakam koşullarını uygulamış; 9’un katı olma koşulunu (rakamlar toplamı 26) denetlememiş.','bilgi'),(9873,'Yalnız 9 ile bölünebilme ve farklı rakam koşullarını uygulamış; 873, 8’in katı değildir.','bilgi'),(9876,'72 yerine 12’ye (3 ve 4) bölünme koşulunu uygulamış; 9876, 72’nin katı değildir.','bilgi'),(9936,'72’nin en büyük dört basamaklı katını bulmuş; rakamlarının farklı olması koşulunu (9 iki kez geçiyor) denetlememiş.','dikkat')],
 istenen='Koşulları sağlayan en büyük sayı.',
 ip=['72 = 8 × 9; rakamlar farklı olduğundan sayı 98 ile başlamayı dene ve kalan iki rakamı koşullarla belirle.'],
 bilgi=[S8,ASAL,R9],
 ad=[A('Koşulları ayır','72 = 8 × 9; son üç basamak 8’in katı, rakamlar toplamı 9’un katı olmalı.','8 ile · 9 ile'),A('Başlangıcı seç','Sayıyı büyük yapmak için baştan 9, 8 al; kalan iki rakam c ve d olsun.','98cd · 9 + 8 + c + d = 17 + c + d'),A('Toplamı ayarla','17 + c + d, 18 ya da 27 olmalı: c + d = 1 ya da 10.','c + d = 10 için büyükten dene: 73, 64, 46, …'),A('8 koşulunu dene','Büyükten başlayıp 8’in katı olanı seç.','9873 → 873 = 8 × 109 + 1 ✗ · 9864 → 864 = 8 × 108 ✓ · 9864 = 72 × 137')],
 puf='Bileşik sayıda (72 = 8 × 9) önce rakamlar toplamı gibi geniş koşulla adayları daralt, sonra büyükten başlayarak son basamak koşulunu dene.')

# ---------- 19 · zor · 7 ve 9 ile bölümde bölüm farkı ----------
s19=[n for n in range(1,2000) if n%7==4 and n//9==n//7-6 and n%9==8]; assert s19==[179] and 179//7==25 and 179//9==19 and 7*25+4==179
assert 7*1+4==11 and 7*27+4==193 and 193//9==21 and 193%9==4 and 179//9==25-6
mk(P,'0019',tipId='blb-bolme',tip='Bölme işlemi ve bölünen–bölen–bölüm–kalan ilişkisi',z='orta',alt='Bölme İşlemi',kaz='Aynı sayının iki farklı bölenle bölünmesinden elde edilen iki eşitliği eşitleyerek bölünen sayıyı bulur.',kalip='düz',adim=3,
 kart='K-BLNB-01 (bölme işlemi) · aynı sayı 7 ve 9 ile bölünüyor, bölümler arasında a − 6 ilişkisi',
 metin='n bir doğal sayıdır. n sayısı 7 ile bölündüğünde bölüm a ve kalan 4 olmaktadır. Aynı n sayısı 9 ile bölündüğünde bölüm a − 6 ve kalan 8 olmaktadır.\nBuna göre n kaçtır?',
 dogru=179,yan=[(11,'9 × (a − 6) açılımında 9 × 6 = 54 yerine 6 yazmış (parantezi dağıtmamış), a = 1 bulmuş.','islem'),(19,'Bölünen yerine 9 ile bölümündeki bölümü (a − 6 = 19) yazmış.','dikkat'),(25,'Bölünen yerine a değerini (7 ile bölümündeki bölüm) yazmış.','dikkat'),(193,'9 ile bölümünden kalanı 4 sanıp 7a + 4 = 9 × (a − 6) + 4 yazmış; a = 27, n = 193.','dikkat')],
 istenen='n sayısı.',
 ip=['n sayısını iki ayrı bölme eşitliğiyle (7a + 4 ve 9 × (a − 6) + 8) yazıp eşitle.'],
 bilgi=[KAL],
 ad=[A('İki eşitlik yaz','Aynı sayı iki bölenle bölünmüştür.','n = 7a + 4 · n = 9 × (a − 6) + 8'),A('Eşitle','Parantezi dağıt: 9 × (a − 6) = 9a − 54.','7a + 4 = 9a − 54 + 8 = 9a − 46'),A('a’yı bul','Terimleri düzenle.','2a = 50 → a = 25'),A('n’yi hesapla','Kontrol: 7 ile kalan 4 ve 9 ile kalan 8 < 9.','n = 7 × 25 + 4 = 179 · 179 = 9 × 19 + 8')],
 puf='Aynı sayı iki bölenle yazılınca iki eşitliği eşitle; parantezdeki bölümü bölenle çarparak dağıtmayı unutma.')

bitir(P,'bolme','mat|Bölme ve Bölünebilme')
