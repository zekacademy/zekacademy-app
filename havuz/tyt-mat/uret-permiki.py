"""Permütasyon ve Kombinasyon · parti 2 (hafif mod): 14 ana soru, kardeş yok, ipucu 1. Her cevap ve çeldirici kodla doğrulanır."""
import sys,os,math
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_mat as H
from _hafif_mat import *
from itertools import product,permutations,combinations
from math import comb,factorial as fa
H.KONU='Permütasyon ve Kombinasyon'
UK='matd|Permütasyon ve Kombinasyon'
P=Parti('permiki','Permütasyon ve Kombinasyon',UK)
def M(no,**k):
    k['adim']=len(k['ad']); mk(P,no,**k)

TOP=B('Toplama ve çarpma ilkesi','Birbirini izleyen aşamalar çarpılır, birbirinin yerine seçilen durumlar toplanır. Örnek: 2 gömlek ve 3 pantolondan birer tane giymek 2 × 3 = 6 biçimde, bir gömlek ya da bir pantolon seçmek 2 + 3 = 5 biçimde olur')
SAYI=B('Basamak koşulları','Çok basamaklı bir sayının ilk basamağı 0 olamaz; çift sayılar 0, 2, 4, 6, 8 ile, tek sayılar 1, 3, 5, 7, 9 ile biter. Önce en kısıtlı basamağı doldur. Örnek: rakamları farklı üç basamaklı tek sayılar için birler 5, yüzler 8, onlar 8 seçenek: 5 × 8 × 8 = 320')
PERM=B('Sıralama','n farklı nesne yan yana n! (n faktöriyel = n × (n − 1) × … × 1) biçimde sıralanır. Yan yana durması istenenler tek nesne sayılır ve kendi içinde ayrıca sıralanır. Örnek: 3 kişi 3 × 2 × 1 = 6 biçimde sıralanır')
TEKR=B('Tekrarlı permütasyon','n nesnenin a tanesi birbirinin aynı, b tanesi birbirinin aynı ise sıralama sayısı n!/(a! × b!) olur. Örnek: AABC harfleriyle 4!/2! = 12 kelime yazılır')
KOMB=B('Kombinasyon','n nesneden sırası önemsiz r tanesi C(n, r) = n!/(r! × (n − r)!) biçimde seçilir; C(n, r) = C(n, n − r). Örnek: C(5, 2) = 5 × 4/2 = 10')
BIRL=B('Birlikte olmasın koşulu','Birlikte olmaması istenen nesnelerin yan yana olduğu dizilişler tüm dizilişlerden çıkarılır; yan yana olanlar tek blok sayılır, blok kendi içinde de sıralanır. Örnek: 3 kişiden A ile B yan yana olmasın: 3! − 2! × 2! = 2')
TUM=B('“En az bir” koşulu','“En az bir” koşullu seçimlerde tüm durumlardan “hiç yok” durumu çıkarılır. Örnek: 5 kişiden 2 kişilik seçimde en az bir kız olması isteniyorsa tüm seçimlerden kızsız seçimler çıkarılır')
NOK=B('Doğrusal noktalar','Üçgenin köşeleri doğrusal olmayan üç noktadır; aynı doğru üzerindeki üç nokta üçgen oluşturmaz. Örnek: 5 noktadan 3’lü seçim C(5, 3) = 10’dur; bu noktaların 3’ü bir doğru üzerindeyse bu seçimlerden 1’i üçgen vermez')
YOL=B('En kısa yol sayma','Yalnızca doğuya (D) ve kuzeye (K) giden yolda adımların sırası yolu belirler: 2 D ve 1 K adımı C(3, 1) = 3 yol verir. Örnek: 2 D ve 2 K adım için C(4, 2) = 6 yol vardır')
ESL=B('İkili eşleşmeler','n kişi arasında her iki kişi birer kez eşleşirse C(n, 2) eşleşme olur; yön ayrımı varsa (A→B ile B→A farklı) n × (n − 1) olur. Örnek: 5 kişi arasında C(5, 2) = 10 maç, 5 × 4 = 20 mesaj')

KY='ÖSYM 2018–2026 TYT Matematik (sayma, permütasyon, kombinasyon) · yayın soru bankaları (yalnız mantık) · MEB 10. sınıf Sayma'
kart('K-PKB-01','Toplama–çarpma ile sayma','Ardışık aşamalar çarpılır, alternatif durumlar toplanır; birleşik durumlarda parantezleme doğru yapılır.','Alternatifleri çarpmak ya da aşamaları toplamak; bir aşamayı tüm durumlara uygulamayı unutmak.','kolay','hikâyeli',3,'pkb-sayma','Toplama ve çarpma ilkesi',KY)
kart('K-PKB-02','Koşullu sayı yazma','Rakam koşulları (farklı, çift, aralık) en kısıtlı basamaktan başlanarak ve gerekirse durumlara ayrılarak sayılır.','Sıfırın başa gelmesine izin vermek; tekrar yasağını ya da aralık koşulunu atlamak; durumları ayırmadan tek çarpım yazmak.','orta','düz',3,'pkb-sayi','Koşullu sayı yazma',KY)
kart('K-PKB-03','Sıralama ve tekrarlı permütasyon','Yan yana gelme (blok), gelmeme (tümleyen), uçlarda durma ve aynı harfli kelimeler sayılır.','Bloğun iç sıralamasını unutmak; aynı nesneleri farklı saymak; koşulu yanlış okumak.','zor','hikâyeli',4,'pkb-sira','Koşullu sıralama ve tekrarlı permütasyon',KY)
kart('K-PKB-04','Kombinasyonla seçme ve eşleşme','Sırasız seçim kombinasyonla, “en az bir” koşulu tümleyenle, ikili eşleşmeler C(n, 2) ile sayılır.','Sırasız seçimi sıralı saymak; “en az bir”i “tam bir” sanmak; seçimde fazla saymak.','orta','hikâyeli',3,'pkb-secme','Kombinasyonla seçme ve ikili eşleşme',KY)
kart('K-PKB-05','Nokta, üçgen ve yol sayma','Doğrusal noktalardan üçgen sayısı C ile, ızgarada en kısa yol adım sıralamasıyla bulunur.','Doğrusal noktaları da üçgen saymak; adımları farklı nesne gibi sıralamak; koşullu uç adımları atlamak.','orta','hikâyeli',3,'pkb-nokta','Üçgen ve en kısa yol sayma',KY)
kart('K-PKB-06','Yeni nesil ve öncüllü sayma','Kural ya da ifade verilen sayma kurgularında her koşul ayrı sayılır, öncüllerin değeri tek tek hesaplanır.','Kuralları yanlış birleştirmek; sıra önemli mi sorusunu atlamak; öncülleri hesaplamadan karar vermek.','zor','yeni nesil',4,'pkb-yeninesil','Yeni nesil ve öncüllü sayma',KY)

# ---------- 01 kolay · yol ----------
yollar=[('AB',i) for i in range(3)]; bc=[('BC',j) for j in range(4)]; ac=[('AC',k) for k in range(2)]
tum=[(a,b) for a in yollar for b in bc]+[(c,) for c in ac]
assert len(tum)==14==3*4+2 and 3+4+2==9 and 3*4==12 and 3*(4+2)==18 and 3*4*2==24
M('0001',tipId='pkb-sayma',tip='Toplama ve çarpma ilkesi',z='kolay',alt='Saymanın Temel İlkesi',kaz='Ardışık yolları çarpıp doğrudan yolları ekleyerek toplam yol sayısını bulur.',kalip='hikâyeli',
 kart='K-PKB-01 (toplama–çarpma) · B’ye uğrayarak ya da doğrudan yol',
 metin='A, B ve C kasabaları arasında yalnızca şu yollar vardır: A ile B arasında 3, B ile C arasında 4 ve A ile C arasında doğrudan 2 farklı yol. Yolların hepsi çift yönlüdür.\nBir sürücü A’dan C’ye gidecek; yolculuğunda B’ye uğrayabilir ya da uğramayabilir ve hiçbir kasabaya ikinci kez uğramayacaktır.\nBuna göre sürücü A’dan C’ye kaç farklı biçimde gidebilir?',
 dogru=14,yan=[(9,'Tüm yol sayılarını toplamış: 3 + 4 + 2.','bilgi'),(12,'Yalnızca B üzerinden gidilen yolları (3 × 4) saymış, doğrudan yolları unutmuş.','dikkat'),(18,'Doğrudan 2 yolu B’den sonraki 4 yola ekleyip 3 × (4 + 2) hesaplamış.','bilgi'),(24,'Tüm yol sayılarını çarpmış: 3 × 4 × 2.','bilgi')],
 istenen='A’dan C’ye gidiş sayısı.',
 ip=['Yolculuğu hangi iki farklı biçimde yapabilirsin? Her biçimde seçenekleri ayrı say.'],
 bilgi=[TOP],
 ad=[A('B’ye uğrayarak','A–B ve B–C yolları art arda kullanılır; aşamalar çarpılır.','3 × 4 = 12'),A('Doğrudan','A–C yollarından biri tek başına seçilir.','2'),A('Toplam','İki biçim birbirinin yerine seçilir; sayılar toplanır.','12 + 2 = 14')],
 puf='Art arda yapılan aşamalar çarpılır, biri ya da diğeri seçilen durumlar toplanır.')

# ---------- 02 kolay · kombin ----------
kom=[('e',i) for i in range(3)]+[('t',i,'p',j) for i in range(5) for j in range(4)]
assert len(kom)==23 and len(kom)*3==69
assert 3*3+5*4==29 and 5*4*3==60 and 3+5+4+3==15
M('0002',tipId='pkb-sayma',tip='Toplama ve çarpma ilkesi',z='kolay',alt='Saymanın Temel İlkesi',kaz='Alternatif ve ardışık seçimleri içeren kombin sayısını toplama ve çarpma ilkeleriyle bulur.',kalip='hikâyeli',
 kart='K-PKB-01 (toplama–çarpma) · elbise ya da tişört–pantolon, sonra ayakkabı',
 metin='Bir mağazada 3 farklı elbise, 5 farklı tişört, 4 farklı pantolon ve 3 farklı ayakkabı satılmaktadır.\nSelin ya tek bir elbise ya da bir tişört ile bir pantolon seçecek; ardından bir ayakkabı seçecektir.\nBuna göre Selin kaç farklı kombin oluşturabilir?',
 dogru=69,yan=[(23,'Ayakkabı seçimini hiç saymamış: 3 + 5 × 4.','dikkat'),(29,'Ayakkabıyı yalnızca elbiseyle çarpmış: 3 × 3 + 5 × 4.','dikkat'),(15,'Tüm sayıları toplamış: 3 + 5 + 4 + 3.','bilgi'),(60,'Elbiseyi saymayıp yalnızca tişört–pantolon seçeneklerini ayakkabıyla çarpmış: 5 × 4 × 3.','dikkat')],
 istenen='Farklı kombin sayısı.',
 ip=['Giyim kısmını kaç farklı biçimde oluşturabilirsin? Ayakkabı seçimi bu seçimin hangi kısmını etkiler?'],
 bilgi=[TOP],
 ad=[A('Giyim seçenekleri','Elbise ya da (tişört ve pantolon).','3 + 5 × 4 = 3 + 20 = 23'),A('Ayakkabı','Her giyim seçeneği için 3 ayakkabı seçilebilir.','× 3'),A('Toplam','Giyim sayısını ayakkabıyla çarp.','23 × 3 = 69')],
 puf='Alternatifleri önce kendi içinde topla, sonra sonraki aşamayla çarp.')

# ---------- 03 kolay · satranç maçı ----------
mac=list(combinations(range(9),2)); assert len(mac)==36==comb(9,2) and 9*8==72 and 9*9==81 and sum(range(1,10))==45 and 9*2==18
M('0003',tipId='pkb-secme',tip='Kombinasyonla seçme ve ikili eşleşme',z='kolay',alt='Kombinasyon',kaz='Herkesin birbiriyle birer kez oynadığı turnuvadaki maç sayısını C(n, 2) ile bulur.',kalip='hikâyeli',
 kart='K-PKB-04 (ikili eşleşme) · satranç turnuvası',
 metin='Bir satranç turnuvasına 9 sporcu katılmıştır. Her sporcu, diğer sporcuların her biriyle tam birer maç yapacaktır.\nBuna göre bu turnuvada toplam kaç maç oynanır?',
 dogru=36,yan=[(18,'Maçı iki sporcunun yaptığını görüp 9 × 2 yazmış, sporcu çiftlerini saymamış.','dikkat'),(45,'Toplamı 1 + 2 + … + 9 olarak almış; ilk sporcunun 9 değil 8 maç yaptığını gözden kaçırmış.','islem'),(72,'9 × 8 hesaplamış; her maçı iki kez (A–B ve B–A) saymış.','bilgi'),(81,'Her sporcu kendisi dahil 9 sporcuyla oynuyor sanıp 9 × 9 hesaplamış.','dikkat')],
 istenen='Toplam maç sayısı.',
 ip=['Bir maçı iki sporcu birlikte yapar; sporcu çiftlerini düşün.'],
 bilgi=[ESL],
 ad=[A('Maçı çift olarak gör','Her maç, 9 sporcudan seçilen 2 sporcudur; sıra önemli değildir.','C(9, 2)'),A('Hesapla','Kombinasyonu aç.','9 × 8/2 = 36'),A('Kontrol','1. sporcu 8, 2. sporcu yeni 7, … son sporcu 0 maç ekler.','8 + 7 + … + 1 = 36')],
 puf='Herkesin herkesle birer kez oynadığı durumlarda eşleşme sayısı C(n, 2)’dir; sıra önemsizdir.')

# ---------- 04 orta · 400'den büyük ----------
S=range(6)
b4=[a*100+b*10+c for a,b,c in permutations(S,3) if a>0 and a*100+b*10+c>400]
assert len(b4)==40==2*5*4 and 2*6*6==72 and len([1 for a,b,c in permutations(S,3) if a>0])==100==5*5*4 and 2*5*5==50 and 1*5*4==20
M('0004',tipId='pkb-sayi',tip='Koşullu sayı yazma',z='orta',alt='Sayı Yazma',kaz='Rakamları farklı ve 400’den büyük olan üç basamaklı sayıların sayısını basamak koşullarına göre bulur.',kalip='düz',
 kart='K-PKB-02 (koşullu sayı yazma) · rakamları farklı, 400’den büyük',
 metin='0, 1, 2, 3, 4 ve 5 rakamları kullanılarak yazılan, rakamları birbirinden farklı üç basamaklı doğal sayılardan kaç tanesi 400’den büyüktür?',
 dogru=40,yan=[(50,'Rakamların farklı olması koşulunu birler basamağında unutmuş: 2 × 5 × 5.','dikkat'),(72,'Rakamların tekrar edebileceğini düşünmüş: 2 × 6 × 6.','bilgi'),(100,'400’den büyük olma koşulunu unutup tüm farklı rakamlı sayıları saymış: 5 × 5 × 4.','dikkat'),(20,'“400’den büyük”ü “yüzler basamağı 4’ten büyük” okuyup yalnızca 5’i almış: 1 × 5 × 4.','dikkat')],
 istenen='Koşulu sağlayan sayıların adedi.',
 ip=['Önce yüzler basamağında hangi rakamlar bulunabilir? Diğer basamaklarda kalan rakamları say.'],
 bilgi=[SAYI],
 ad=[A('Yüzler basamağı','Sayı 400’den büyük ve en az 4xx olmalı; yüzler basamağı 4 ya da 5 olur.','2 seçenek'),A('Onlar basamağı','Yüzler basamağında kullanılan rakam dışındaki 5 rakamdan biri gelir.','5 seçenek'),A('Birler basamağı','Kalan 4 rakamdan biri gelir; 4 seçenek vardır. Sonra çarp.','2 × 5 × 4 = 40')],
 puf='Basamak koşullarında en kısıtlı basamaktan başla; rakamlar farklıysa sonraki basamaklarda seçenek bir azalır.')

# ---------- 05 zor · binler basamağı 5'ten büyük, çift ----------
d=[(a,b,c,e) for a,b,c,e in permutations(range(10),4) if a>5 and e%2==0]
assert len(d)==1008==4*8*7+2*4*8*7+2*3*8*7
c2=sum(1 for a,b,c,e in permutations(range(10),4) if a>=5 and e%2==0)
assert 4*5*8*7==1120 and 4*10*10*5==2000 and 1008-4*8*7==784
M('0005',tipId='pkb-sayi',tip='Koşullu sayı yazma',z='zor',alt='Sayı Yazma',kaz='Rakamları farklı, çift ve binler basamağı koşullu dört basamaklı sayıları birler basamağına göre durumlara ayırarak sayar.',kalip='düz',
 kart='K-PKB-02 (koşullu sayı yazma) · çift, binler basamağı 5’ten büyük',
 metin='Rakamları birbirinden farklı olan ve binler basamağındaki rakam 5’ten büyük olan dört basamaklı çift doğal sayılar kaç tanedir?',
 dogru=1008,yan=[(784,'Sıfırla biten sayıları saymamış; yalnızca 2, 4, 6, 8 ile biten sayıları hesaplamış (1008 − 224).','dikkat'),(c2,'Binler basamağını “5 ve daha büyük” alıp 5’i de katmış.','dikkat'),(1120,'Birler basamağı için 5 çift rakam, binler için 4 seçenek alıp ikisinin çakışmasını (6 ve 8) hesaba katmamış: 4 × 5 × 8 × 7.','islem'),(2000,'Rakamların farklı olması koşulunu atlamış: 4 × 10 × 10 × 5.','bilgi')],
 istenen='Koşulu sağlayan sayıların adedi.',
 ip=['Birler basamağı sıfır olduğunda ve olmadığında binler basamağındaki seçeneklerin sayısı aynı mı?'],
 bilgi=[SAYI],
 ad=[A('Birler basamağı 0','Binler basamağı 6, 7, 8, 9’dan biri; onlar ve yüzler kalan rakamlardan.','4 × 8 × 7 = 224'),A('Birler basamağı 2 veya 4','Binler basamağı yine 4 seçenek (6, 7, 8, 9); onlar 8, yüzler 7 seçenek.','2 × 4 × 8 × 7 = 448'),A('Birler basamağı 6 veya 8','Binler basamağında birler basamağındaki rakam kullanıldığından 3 seçenek kalır.','2 × 3 × 8 × 7 = 336'),A('Durumları topla','Üç durum birbirinden ayrıdır.','224 + 448 + 336 = 1008')],
 puf='Bir rakam iki farklı koşulda geçiyorsa (burada 6 ve 8) durumlara ayır; seçenek sayısı duruma göre değişir.')

# ---------- 06 orta · kitaplar ----------
def kitap():
    n=0
    for p in permutations('MMMFF'): pass
    c=0
    for p in permutations(range(5)):  # 0,1,2 matematik
        pos=sorted(p.index(i) for i in range(3))
        if pos[2]-pos[0]!=2: c+=1
    return c
assert fa(3)-fa(2)*fa(2)==2 and kitap()==84==fa(5)-fa(3)*fa(3) and fa(3)*fa(3)==36 and fa(5)-fa(3)==114 and fa(2)*fa(3)==12
M('0006',tipId='pkb-sira',tip='Koşullu sıralama ve tekrarlı permütasyon',z='orta',alt='Sıralama',kaz='Üç nesnenin birden ardışık olmadığı sıralamaları, ardışık olanları tümünden çıkararak sayar.',kalip='hikâyeli',
 kart='K-PKB-03 (yan yana gelmeme) · kitap rafı',
 metin='Birbirinden farklı 3 matematik ve 2 fizik kitabı bir rafa yan yana dizilecektir.\nMatematik kitaplarının üçü birden art arda (yan yana) gelmeyecek biçimde bu 5 kitap kaç farklı sırayla dizilebilir?',
 dogru=84,yan=[(12,'“Üçü birden yan yana olmasın” koşulunu “hiçbir ikisi yan yana olmasın” diye okumuş: fizikleri dizip aralarına matematikleri yerleştirmiş, 2 × 6.','dikkat'),(36,'Matematik kitaplarının üçünün birden yan yana olduğu durumları saymış, çıkarmamış.','dikkat'),(114,'Üç kitaplık bloğun kendi içindeki sıralamasını (3!) unutup yan yana olan dizilişleri yalnızca 3! = 6 saymış: 120 − 6.','islem'),(120,'Koşulu hiç uygulamamış: 5 kitabı serbestçe sıralamış.','bilgi')],
 istenen='Koşula uygun diziliş sayısı.',
 ip=['Üç matematik kitabının raftaki konumlarını düşün; koşula uymayan dizilişlerin ortak özelliği ne?'],
 bilgi=[PERM,BIRL],
 ad=[A('Tüm dizilişler','5 farklı kitap serbestçe sıralanır.','5! = 120'),A('Üçü birden yan yana','3 matematik kitabını tek blok say: blok ve 2 fizik kitabı 3 nesnedir; blok kendi içinde de sıralanır.','3! × 3! = 36'),A('Çıkar','Tümünden istenmeyen dizilişleri çıkar.','120 − 36 = 84')],
 puf='“Birlikte olmasın” koşulunda tüm sıralamalardan birlikte olanları çıkar.')

# ---------- 07 orta · uçlarda ----------
c7=sum(1 for p in permutations(range(7)) if {p[0],p[6]}=={0,1})
assert c7==240==2*fa(5) and fa(5)==120 and fa(6)==720 and 2*fa(6)==1440 and fa(7)==5040
M('0007',tipId='pkb-sira',tip='Koşullu sıralama ve tekrarlı permütasyon',z='orta',alt='Sıralama',kaz='İki kişinin sıranın iki ucuna oturma koşuluyla yapılan sıralamaları sayar.',kalip='hikâyeli',
 kart='K-PKB-03 (uçta durma) · panel konuşmacıları',
 metin='Bir panelde 7 farklı konuşmacı, sahnedeki yan yana dizilmiş 7 sandalyeye oturacaktır. Sandalyeler tek sıra hâlindedir.\nKonuşmacılardan Taner ile Selma, sıranın iki ucundaki sandalyelere (biri bir ucuna, diğeri öbür ucuna) oturacaktır.\nBuna göre konuşmacılar kaç farklı biçimde oturabilir?',
 dogru=240,yan=[(120,'İki ucu tek biçim saymış: Taner ile Selma’nın uçlarda yer değiştirebileceğini atlamış, 5!.','dikkat'),(720,'Yalnız Taner’i sol uca koyup kalan 6 kişiyi sıralamış; Selma’nın koşulunu uygulamamış (6!).','dikkat'),(1440,'Yalnız Taner’in iki uçtan birine oturduğunu düşünüp 2 × 6! hesaplamış.','bilgi'),(5040,'Koşulu hiç uygulamamış: 7!.','bilgi')],
 istenen='Farklı oturma düzeni sayısı.',
 ip=['Önce uçlardaki iki sandalyeyi doldur; kalan sandalyelere kimlerin oturabileceğine bak.'],
 bilgi=[PERM],
 ad=[A('Uçlar','Taner sol uçta Selma sağ uçta ya da tersi.','2 biçim'),A('Ortadaki sandalyeler','Kalan 5 kişi ortadaki 5 sandalyeye oturur.','5! = 120'),A('Çarp','Uç düzeni ile ortadaki düzen ardışık aşamalardır.','2 × 120 = 240')],
 puf='Koşullu kişileri önce yerleştir, kalanları serbest sırala; yer değiştirme sayısını da çarp.')

# ---------- 08 zor · SAKARYA ----------
w=set(permutations('SAKARYA')); assert len(w)==840
c8=sum(1 for p in w if p[0]=='S' and 'AAA' not in ''.join(p))
assert c8==96==120-24 and fa(4)==24 and 720==840-120 and fa(6)-fa(4)*fa(3)==576 and 5040//6==840
M('0008',tipId='pkb-sira',tip='Koşullu sıralama ve tekrarlı permütasyon',z='orta',alt='Tekrarlı Permütasyon',kaz='Aynı harfli kelimelerde başlangıç harfi ve harflerin yan yana gelmemesi koşullarını birlikte uygulayarak sayar.',kalip='düz',
 kart='K-PKB-03 (tekrarlı permütasyon) · SAKARYA, ilk harf S, üç A birden art arda değil',
 metin='SAKARYA kelimesindeki 7 harfin hepsi kullanılarak, anlamlı ya da anlamsız 7 harfli kelimeler yazılıyor.\nİlk harfi S olan ve üç A harfinin üçü birden art arda (yan yana) gelmeyen kaç farklı kelime yazılabilir?',
 dogru=96,yan=[(120,'Üç A’nın yan yana gelmeme koşulunu uygulamamış; yalnızca ilk harfi S yapıp 6!/3! hesaplamış.','dikkat'),(576,'Üç A’yı birbirinden farklı sanmış: 6! − 4! × 3!.','bilgi'),(720,'İlk harfin S olması koşulunu atlamış: 7!/3! − 5! = 840 − 120.','dikkat'),(840,'Hiçbir koşulu uygulamamış: 7!/3!.','bilgi')],
 istenen='Koşula uygun kelime sayısı.',
 ip=['S sabitlendikten sonra kalan 6 harfle ilgili koşulsuz ve koşulu bozan durumları ayrı say.'],
 bilgi=[TEKR,BIRL],
 ad=[A('S başa sabit','Kalan harfler K, R, Y, A, A, A; üç A aynıdır.','6!/3! = 120'),A('Üç A birden yan yana','AAA tek blok; blok ve K, R, Y toplam 4 nesne olur.','4! = 24'),A('Çıkar','Koşulu bozanları tümünden çıkar.','120 − 24 = 96')],
 puf='Aynı harfler varsa önce tekrarlı permütasyonla say; “birlikte olmasın” koşulunda birlikte olanları blok yapıp çıkar.')

# ---------- 09 orta · yönetim ----------
c9=sum(1 for g in combinations(range(11),4) if any(x<6 for x in g))
assert c9==325==comb(11,4)-comb(5,4) and comb(5,4)==5 and 6*comb(5,3)==60 and comb(11,4)==330 and comb(10,3)==120
M('0009',tipId='pkb-secme',tip='Kombinasyonla seçme ve ikili eşleşme',z='orta',alt='Kombinasyon',kaz='“En az bir” koşullu seçimi tümleyen yoluyla kombinasyonla sayar.',kalip='hikâyeli',
 kart='K-PKB-04 (en az bir) · apartman yönetim kurulu',
 metin='Bir apartmanda 6 kadın ve 5 erkek oturmaktadır. Bu 11 kişi arasından 4 kişilik bir yönetim kurulu seçilecektir; kurulda görev ayrımı yoktur ve sıra önemli değildir.\nKurulda en az bir kadın bulunması istendiğine göre kurul kaç farklı biçimde seçilebilir?',
 dogru=325,yan=[(5,'Yalnızca hiç kadının bulunmadığı seçimleri sayıp C(5, 4) = 5’te kalmış.','dikkat'),(60,'“En az bir”i “tam bir” sanmış: 6 × C(5, 3).','bilgi'),(330,'Kadın koşulunu uygulamamış: C(11, 4).','dikkat'),(120,'Belirli bir kadını kurula sabit alıp kalan 3 üyeyi diğer 10 kişiden seçmiş: C(10, 3).','islem')],
 istenen='Farklı yönetim kurulu sayısı.',
 ip=['Önce koşulsuz kaç kurul seçilebileceğini bul; koşul hangi kurulları dışarıda bırakıyor?'],
 bilgi=[KOMB,TUM],
 ad=[A('Tüm kurullar','11 kişiden 4 kişi, sıra önemsiz.','C(11, 4) = 330'),A('Hiç kadın yok','Kurulun tamamı 5 erkekten seçilir.','C(5, 4) = 5'),A('Çıkar','En az bir kadın = tüm kurullar − kadınsız kurullar.','330 − 5 = 325')],
 puf='“En az bir” görünce tümleyeni düşün: tüm durumlar eksi “hiç yok” durumu.')

# ---------- 10 orta · üçgen ----------
Pt=[(i,0) for i in range(6)]+[(0,2),(2,5),(4,1),(5,3)]
def kolin(a,b,c): return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])==0
kt=[t for t in combinations(Pt,3) if kolin(*t)]
assert len(kt)==comb(6,3)==20  # yalnız doğru üzerindeki üçlüler
u=comb(10,3)-20; assert u==100==comb(6,2)*4+6*comb(4,2)+comb(4,3) and comb(10,3)==120 and u-comb(4,3)==96 and 10*9*8-6*5*4==600
M('0010',tipId='pkb-nokta',tip='Üçgen ve en kısa yol sayma',z='orta',alt='Doğru ve Üçgen Sayma',kaz='Doğrusal noktaları dışlayarak köşeleri verilen noktalardan seçilen üçgenlerin sayısını bulur.',kalip='düz',
 kart='K-PKB-05 (doğrusal noktalardan üçgen) · 6 doğrusal nokta ve 4 nokta',
 metin='Bir düzlemde, bir d doğrusu üzerinde 6 nokta ve d doğrusu üzerinde olmayan 4 nokta daha işaretlenmiştir. Bu 10 noktanın doğrusal olan üçlüleri yalnızca d doğrusu üzerindeki noktalardan oluşan üçlülerdir; başka hiçbir üç nokta doğrusal değildir.\nKöşeleri bu 10 noktadan seçilen kaç farklı üçgen çizilebilir?',
 dogru=100,yan=[(20,'Yalnızca doğru üzerindeki 3’lü seçimleri saymış: C(6, 3).','dikkat'),(96,'d üzerindeki 3’lüleri çıkarmış ama d dışındaki 4 noktadan oluşan üçgenleri de çıkarmış (4 üçgen eksik).','dikkat'),(120,'Doğrusal noktaları fark etmeyip tüm 3’lü seçimleri üçgen saymış: C(10, 3).','dikkat'),(600,'Köşelerin sırasını önemli sanmış: P(10, 3) − P(6, 3).','bilgi')],
 istenen='Çizilebilecek üçgen sayısı.',
 ip=['Üç noktanın üçgen oluşturması için ne gerekir? Tüm üçlüleri bu açıdan ayır.'],
 bilgi=[KOMB,NOK],
 ad=[A('Tüm 3’lü seçimler','10 noktadan 3 nokta, sıra önemsiz.','C(10, 3) = 120'),A('Üçgen vermeyenler','Doğrusal üçlüler yalnızca d üzerindeki 6 noktadan seçilir.','C(6, 3) = 20'),A('Çıkar','Üçgen = tüm seçimler − doğrusal seçimler.','120 − 20 = 100')],
 puf='Doğrusal üç nokta üçgen oluşturmaz; tüm üçlülerden doğrusal olanları çıkar.')

# ---------- 11 orta · ızgara ----------
yl=[p for p in set(permutations('DDDDKKKK')) if p[0]=='D' and p[-1]=='K']
assert len(yl)==20==comb(6,3) and comb(8,3)==56 and comb(7,3)==35 and comb(8,4)==70 and fa(6)==720
M('0011',tipId='pkb-nokta',tip='Üçgen ve en kısa yol sayma',z='orta',alt='Yol Sayma',kaz='Başlangıç ve bitiş adımı belirli en kısa yolları kalan adımların sıralamasıyla sayar.',kalip='hikâyeli',
 kart='K-PKB-05 (ızgarada en kısa yol) · ilk adım doğu, son adım kuzey',
 metin='Sokakları birbirine dik, eş uzunlukta bloklardan oluşan bir mahallede bir kurye, evinden bir müşterinin kapısına yalnızca doğuya ya da kuzeye doğru birer blok ilerleyerek gidecektir. Müşteri, kuryenin evinden 4 blok doğuda ve 4 blok kuzeydedir.\nKurye ilk bloğu doğuya, son bloğu kuzeye doğru yürüyeceğine göre kaç farklı en kısa yoldan gidebilir?',
 dogru=20,yan=[(56,'Doğu adımı sayısını 3, kuzey adımı sayısını 5 sanıp C(8, 3) hesaplamış.','dikkat'),(35,'Yalnızca ilk adımın doğu olması koşulunu uygulamış: C(7, 3).','dikkat'),(70,'Hiçbir uç koşulu uygulamamış: C(8, 4).','dikkat'),(720,'6 adımı birbirinden farklı sanıp 6! hesaplamış.','bilgi')],
 istenen='Kuryenin gidebileceği en kısa yol sayısı.',
 ip=['İlk ve son adım belli iken yolun hangi kısmı serbestçe düzenlenebilir?'],
 bilgi=[YOL,KOMB],
 ad=[A('Toplam adım','4 doğu ve 4 kuzey adımı gerekir.','8 adım'),A('Serbest adımlar','İlk adım D, son adım K sabit; kalan 6 adımda 3 D ve 3 K bulunur.','6 adım'),A('Adımları sırala','6 adımdan 3’ünün yeri D için seçilir.','C(6, 3) = 20')],
 puf='Yalnızca iki yöne giden yolda hangi adımların doğu olacağını seçmek yeterlidir; sabit adımları baştan ayır.')

# ---------- 12 orta · öncüllü ----------
assert 8*7==56 and comb(8,2)==28 and comb(8,5)==56 and 8*5==40
SI=['Yalnız I','Yalnız III','I ve II','I ve III','I, II ve III']
M('0012',tipId='pkb-yeninesil',tip='Yeni nesil ve öncüllü sayma',z='orta',alt='Öncüllü Sayma',kaz='Sıra önemli ve önemsiz seçimlerin sayısını hesaplayıp öncülleri değerlendirir.',kalip='öncüllü',
 kart='K-PKB-06 (öncüllü) · başkan–yardımcı, 2 kişilik grup, 5 kişilik komite',
 metin='8 öğrenci arasından aşağıdaki seçimler ayrı ayrı yapılacaktır.\nI. Bir başkan ile bir başkan yardımcısı seçmek (aynı öğrenci iki görevde bulunamaz).\nII. 2 kişilik bir temsilci grubu seçmek (görev ayrımı yoktur, sıra önemsizdir).\nIII. 5 kişilik bir komite seçmek (görev ayrımı yoktur, sıra önemsizdir).\nBu seçimlerden hangilerinin yapılış sayısı 56’dır?',
 dogru='I ve III',sira=SI,yan=[('Yalnız I','III’ü sıralı sayıp 8 × 7 × 6 × 5 × 4 = 6720 bulmuş; III’ün 56 olduğunu görememiş.','islem'),('Yalnız III','I’de sıranın önemli olduğunu unutup C(8, 2) = 28 bulmuş; III’ü doğru hesaplamış.','bilgi'),('I ve II','II’yi sıralı saymış (8 × 7 = 56); III’te C(8, 5) yerine 8 × 5 = 40 yazmış.','islem'),('I, II ve III','II’de sıranın önemsiz olduğunu atlayıp 8 × 7 = 56 bulmuş; II’yi de 56 saymış.','bilgi')],
 istenen='Yapılış sayısı 56 olan seçimler.',
 ip=['Her seçimde sıranın önemli olup olmadığına bak ve her öncülün sayısını ayrı hesapla.'],
 bilgi=[KOMB,PERM],
 ad=[A('I','Görevler farklı olduğundan sıra önemlidir: önce başkan, sonra yardımcı.','8 × 7 = 56'),A('II','Görev ayrımı yok; 8 öğrenciden 2’si seçilir.','C(8, 2) = 28 (56 değil)'),A('III','8 öğrenciden 5’i seçilir; C(8, 5) = C(8, 3).','C(8, 5) = 56'),A('Sonuç','I ve III’ün değeri 56’dır.','I ve III')],
 puf='Görevler farklıysa sıra önemlidir (çarpma); görev ayrımı yoksa kombinasyon kullan.')

# ---------- 13 zor · mektup ----------
n13=[n for n in range(2,60) if n*(n-1)==342]; assert n13==[19]
assert comb(19,3)==969 and comb(19,3)-17==952 and 17==19-2 and 18*19==342 and comb(18,3)-16==800 and 969-2*17==935
assert sum(1 for t in combinations(range(19),3) if not (0 in t and 1 in t))==952
M('0013',tipId='pkb-secme',tip='Kombinasyonla seçme ve ikili eşleşme',z='zor',alt='Kombinasyon',kaz='Sıralı ikili ilişkiden öğrenci sayısını bulup koşullu bir kombinasyon seçimini hesaplar.',kalip='hikâyeli',
 kart='K-PKB-04 (n(n − 1) ve kombinasyon) · mektuplaşma ve nöbet ekibi',
 metin='Bir sınıftaki her öğrenci, sınıftaki diğer her öğrenciye tam birer mektup yazmıştır; kimse kendine mektup yazmamıştır. Toplam 342 mektup yazılmıştır.\nBu sınıftan 3 kişilik bir nöbet ekibi seçilecektir (görev ayrımı yoktur, sıra önemli değildir). Sınıfın öğrencilerinden Ayşe ile Burak ekipte birlikte bulunmayacaktır (ikisinden biri bulunabilir ya da hiçbiri bulunmayabilir).\nBuna göre nöbet ekibi kaç farklı biçimde seçilebilir?',
 dogru=952,yan=[(17,'Yalnızca Ayşe ile Burak’ın birlikte bulunduğu ekipleri saymış: 17.','dikkat'),(800,'Öğrenci sayısını n × (n + 1) = 342 alıp 18 bulmuş: C(18, 3) − 16.','islem'),(935,'Ayşe ile Burak’ın birlikte olduğu ekipleri 2 × 17 sayıp çıkarmış (ikisinin sırasını farklı saymış).','bilgi'),(969,'Birlikte bulunmama koşulunu uygulamamış: C(19, 3).','dikkat')],
 istenen='Koşula uygun nöbet ekibi sayısı.',
 ip=['Önce her öğrencinin kaç mektup yazdığını sınıf mevcudu cinsinden düşün; sonra ekip seçimine geç.'],
 bilgi=[ESL,KOMB,TUM],
 ad=[A('Öğrenci sayısı','Her öğrenci (n − 1) mektup yazar; toplam n × (n − 1).','n × (n − 1) = 342 → 19 × 18 → n = 19'),A('Tüm ekipler','19 öğrenciden 3 kişi, sıra önemsiz.','C(19, 3) = 969'),A('Birlikte bulunanlar','Ayşe ve Burak ekipte; üçüncü kişi kalan 17 öğrenciden biri.','17'),A('Çıkar','Koşula uygun ekipler = tümü − birlikte bulunanlar.','969 − 17 = 952')],
 puf='n × (n − 1) sıralı ikililerin sayısıdır; “birlikte olmasın” koşulunda birlikte olan seçimleri tümünden çıkar.')

# ---------- 14 zor · şifre kuralı ----------
H_=['A','E','İ','K','M','T']; V={'A','E','İ'}
hr=[h for h in permutations(H_,3) if V&set(h)]; rk=[r for r in permutations(range(10),2) if (r[0]+r[1])%2==0]
assert len(hr)==114 and len(rk)==40 and 114*40==4560
bir=[h for h in permutations(H_,3) if len(V&set(h))==1]; assert len(bir)==54 and 54*40==2160 and 6*5*4*40==4800 and 19*40==760 and comb(6,3)-1==19 and 114*20==2280
M('0014',tipId='pkb-yeninesil',tip='Yeni nesil ve öncüllü sayma',z='zor',alt='Yeni Nesil',kaz='Harf ve rakam kısımları için verilen kuralları ayrı ayrı sayıp çarparak şifre sayısını bulur.',kalip='yeni nesil',
 kart='K-PKB-06 (yeni nesil, şifre kuralı) · en az bir sesli harf ve toplamı çift rakamlar',
 metin='Bir uygulamada şifre, önce 3 harf, ardından 2 rakamdan oluşmaktadır ve şu kurallara uymak zorundadır:\n• Harfler A, E, İ, K, M, T harflerinden seçilir ve birbirinden farklıdır; sesli harfler A, E, İ’dir. Harf kısmında en az bir sesli harf bulunmalıdır.\n• Rakamlar 0, 1, …, 9 rakamlarından seçilir ve birbirinden farklıdır. İki rakamın toplamı çift olmalıdır.\nHarflerin ve rakamların yeri sıralıdır (sıra önemlidir).\nBuna göre bu kurallara uyan kaç farklı şifre oluşturulabilir?',
 dogru=4560,yan=[(4800,'En az bir sesli harf koşulunu atlayıp 6 × 5 × 4 × 40 hesaplamış.','dikkat'),(760,'Harfleri sırasız seçmiş: (C(6, 3) − C(3, 3)) × 40 = 19 × 40.','bilgi'),(2160,'Harf kısmında “en az bir” yerine “tam bir” sesli harf almış: 54 × 40.','bilgi'),(2280,'Rakam çiftlerini sırasız sayıp C(5, 2) + C(5, 2) = 20 bulmuş: 114 × 20.','dikkat')],
 istenen='Kurallara uyan şifre sayısı.',
 ip=['Harf kısmı ile rakam kısmını birbirinden bağımsız iki sayma problemi olarak ele al.'],
 bilgi=[TOP,TUM,B('Toplamı çift iki rakam','İki rakamın toplamı çift ise rakamların ikisi de çift ya da ikisi de tektir. Örnek: 2 + 6 = 8 ve 3 + 7 = 10 çifttir, 2 + 3 = 5 çift değildir')],
 ad=[A('Harf kısmı','Tüm farklı üçlü diziler eksi hiç sesli harf içermeyenler (yalnız K, M, T).','6 × 5 × 4 − 3 × 2 × 1 = 114'),A('Rakam kısmı','Toplam çift için iki rakam da çift ya da ikisi de tek; sıralı ve farklı.','5 × 4 + 5 × 4 = 40'),A('Birleştir','Harf ve rakam kısımları art arda yazılır; çarp.','114 × 40 = 4560')],
 puf='Bağımsız kısımlar ayrı sayılıp çarpılır; “en az bir” koşulu tümleyenle, “toplamı çift” koşulu aynı çift/tek durumlarıyla çözülür.')

bitir(P,'permiki',UK)
