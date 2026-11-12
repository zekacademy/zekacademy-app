"""Sayı Problemleri · parti 2 (hafif mod): 34 ana soru, kardeş yok, ipucu 1. Her cevap ve çeldirici kodla doğrulanır."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_mat as H
from _hafif_mat import *
H.KONU='Sayı Problemleri'
UK='prob|Sayı Problemleri'
P=Parti('sayiprobiki','Sayı Problemleri',UK)
DEN=B('Sözel ifadeyi denkleme çevirme','“x’in 3 katının 5 fazlası” 3x + 5, “x’in 3 katından 5 eksiği” 3x − 5, “x’in 5 fazlasının 3 katı” 3(x + 5) demektir. Örnek: “bir sayının 2 katının 4 eksiği 10” ise 2x − 4 = 10, x = 7')
ARD=B('Ardışık sayılar','Ardışık tam sayılar x, x + 1, x + 2; ardışık çift ya da tek sayılar x, x + 2, x + 4 biçimindedir. Örnek: ardışık üç sayının toplamı, ortancanın 3 katıdır: 4 + 5 + 6 = 3 × 5')
IKI=B('İki bilinmeyenli kurulum','Nesne türlerinin adedi ve toplam değeri iki denklem verir; biri öbürüne yerleştirilir. Örnek: 10 baş ve 28 ayak için x + y = 10, 2x + 4y = 28 ise y = 4')
EF=B('Eksik–fazla paylaştırma','Mal sayısı iki ayrı dağıtımla ifade edilip eşitlenir: artan miktar eklenir, eksik kalan miktar çıkarılır. Örnek: kişi başı 2 verilirse 5 artıyor, 3 verilirse 1 eksik kalıyorsa 2x + 5 = 3x − 1, x = 6')
SIRA=B('Sıra ve kuyruk','Baştan a., sondan b. sıradaki kişi varsa kuyrukta a + b − 1 kişi vardır; sıra numaraları farkından 1 çıkarılırsa aradaki kişi sayısı bulunur. Örnek: 5. ile 9. arasında 9 − 5 − 1 = 3 kişi vardır')
KAT=B('Kat ve numara','Her katta k daire varsa zemin kattan başlayarak 1’den numaralanan n numaralı dairenin üzerindeki kat sayısı (n − 1) ÷ k’nın tam kısmıdır. Örnek: katta 4 daire varsa 10 numaralı daire (10 − 1) ÷ 4 = 2 kat yukarıdadır')
ALIS=B('Alışveriş ve para üstü','Verilen para = alınan malların bedeli + para üstü. Örnek: tanesi 20 TL olan 3 ürün için 100 TL verilirse para üstü 100 − 60 = 40 TL’dir')
PER=B('Periyot ve kalan','n gün sonrasının haftanın günü, n’nin 7’ye bölümünden kalanla bulunur; ortak katlar ve kalanlı koşullarda “kalan + 1 = ortak bölen” gibi eşitlikler aranır. Örnek: Salı’dan 10 gün sonrası için 10 = 7 + 3, Cuma gelir')
TIR=B('Gündüz çıkıp geceleyin kayma','Her gün net kazanç, çıkış ile kaymanın farkıdır; ama son gün hedefe ulaşılınca kayma olmaz. Örnek: 2 m çıkıp 1 m kayan ve 6 m’ye varması gereken birinin n. gün sonu en yüksek noktası (n − 1) × 1 + 2’dir')
PUAN=B('Puanlama ve net','puan = doğru × a − yanlış × b; boş soru puan getirmez, yanlış götürmez. Örnek: +4 ve −1 puanla 10 soruda 7 doğru 3 yanlış varsa puan 28 − 3 = 25’tir')
TER=B('Terazi dengesi','Denge durumunda iki kefenin ağırlığı eşittir; iki kefede de bulunan nesneler aynı sayıda çıkarılabilir. Örnek: 3 elma + 40 g = 5 elma ise 40 g = 2 elmadır, bir elma 20 g’dır')
ENC=B('En az – en çok','Bir değeri en çok (en az) yapmak için diğer değerler ters yönde uç değerlerde alınır. Örnek: toplamı 10 olan iki pozitif tam sayıdan büyük olan en çok 9, küçük olan en az 1’dir')
GER=B('Geriye giderek çözme','Sonuçtan başlanır, her işlemin tersi ters sırayla uygulanır. Örnek: bir sayı 2 ile çarpılıp 3 eklenince 11 oluyorsa sayı (11 − 3) ÷ 2 = 4’tür')
BAS=B('İki basamaklı sayı','ab sayısı 10a + b’dir; rakamlar yer değiştirince sayı 10b + a olur ve aradaki fark 9(a − b) çıkar. Örnek: 52 − 25 = 27 = 9 · 3')
OZ=B('Ardışık sayıların ortancası','Ardışık tek sayıda sayının toplamı, sayı adedi × ortanca terimdir. Örnek: ardışık 5 sayının toplamı 40 ise ortanca 8, sayılar 6, 7, 8, 9, 10’dur')
KY='ÖSYM 2018–2026 TYT Matematik (Problemler) · yayın soru bankaları (yalnız mantık) · MEB 9. sınıf'
CT={}
def K_(c,alt,fikir,tuzak,z,kalip,adim,tid,tip):
    CT[c]=(tid,tip); kart(f'K-SPB-{c}',alt,fikir,tuzak,z,kalip,adim,tid,tip,KY)
K_('01','Sözel ifade → denklem','“fazlası, katı, eksiği” ifadeleri sırasıyla toplama, çarpma ve çıkarmaya çevrilir; iki yanı eşitlenir.','“x’in 5 fazlasının 3 katı” ile “3 katının 5 fazlası”nı karıştırmak; “eksiği” işaretini ters kurmak.','kolay','düz',2,'spb-sozel','Sözel ifadeyi denkleme çevirme')
K_('02','Ardışık sayılar','Ardışık (çift/tek) sayılar x, x+d, x+2d biçiminde yazılır; toplam ve koşullar ortanca veya ilk terim üzerinden çözülür.','Ardışık tek/çift sayıda adım farkını 1 almak; sayı adedinde bir fazla ya da eksik saymak.','orta','düz',3,'spb-ardisik','Ardışık sayı problemleri')
K_('03','İki bilinmeyenli kurulum','Adet ve toplam değer (ayak, para, basamak, tekerlek) iki ya da üç denklemle kurulur ve yerine koyma ile çözülür.','İstenen yerine ara değeri vermek; ayak sayısını baş sayısıyla karıştırmak.','orta','hikâyeli',3,'spb-ikibilinmeyen','Adet–değer ve basamak kurulumları')
K_('04','Paylaştırma eksik / fazla','Aynı mal iki dağıtımla ifade edilir (artan eklenir, eksik çıkarılır) ve eşitlenir; kişi, sıra ya da mal sayısı bulunur.','Artanı ve eksiği toplam yerine çıkarmak; son kişiye düşen azı kişi başı payla karıştırmak.','zor','hikâyeli',4,'spb-eksikfazla','Eksik ve fazla ile paylaştırma')
K_('05','Sıra, kuyruk, kat','Baştan–sondan sırada a + b − 1; aradaki kişi sayısı fark − 1; kat numaralarında zemin kat dikkate alınır.','Aradaki kişi için fazladan 1 çıkarmamak; kat farkını yukarı yuvarlamak.','orta','hikâyeli',3,'spb-sira','Sıra, kuyruk ve kat problemleri')
K_('06','Alışveriş, para üstü, fiyat listesi','Hesap fişleri ve para üstünden iki türün fiyatı bulunur; verilen para = bedel + para üstü.','Para üstünü bedele eklememek; iki fişin farkını ürün fiyatı sanmak.','orta','tablo',3,'spb-alisveris','Alışveriş, para üstü ve fiyat listesi')
K_('07','Merdiven, adım, takvim, periyot','Kalanlı koşullar, günlük ilerleme-kayma ve takvim hesapları 7 ve ortak bölenlerle çözülür.','Son gün kaymayı saymak; aylarda gün sayısını eşit almak; kalan koşulunu atlamak.','orta','hikâyeli',3,'spb-periyot','Merdiven, takvim ve periyot')
K_('08','Puanlama ve net','Doğru, yanlış, boş sayıları ve puan kuralıyla (net) iki denklem kurulup çözülür; kurallı oyunlarda galibiyet–beraberlik–mağlubiyet de bu mantıktadır.','Yanlışın puanını işaret hatasıyla eklemek; boşları saymamak.','zor','hikâyeli',4,'spb-puan','Doğru–yanlış puanlama ve puan sistemleri')
K_('09','Terazi ve en az – en çok','Terazi dengesi eşitlik olarak yazılır; en çok/en az sorularında diğer değerler en küçük (ya da en büyük) alınır.','Farklı olma koşulunu atlamak; 0’ı pozitif saymak.','orta','hikâyeli',3,'spb-sinir','Terazi ve en az–en çok')
K_('10','Geriye giderek çözme ve makine','Zincir işlemlerde sonuçtan başlayıp tersleri ters sırayla uygulamak; makine zincirleri.','İşlemleri ters sırada uygulamamak; işaretleri değiştirmemek.','zor','yeni nesil',4,'spb-geriye','Geriye giderek çözme ve işlem zinciri')

def S(no,c,z,alt,kaz,kalip,adim,kk,metin,dogru,yan,ist,ip,bil,ad,puf,sira=None,kisa=None):
    tid,tip=CT[c]
    mk(P,no,tipId=tid,tip=tip,z=z,alt=alt,kaz=kaz,kalip=kalip,adim=adim,kart=f'K-SPB-{c} ({kk})',metin=metin,dogru=dogru,yan=yan,istenen=ist,ip=[ip],bilgi=bil,ad=ad,puf=puf,sira=sira,kisa=kisa)


# ---------- 0001 kolay · sözel
x=12; assert 3*x-7==2*x+5==29 and 2*x==24 and 3*x==36 and x+7==19
S('0001','01','kolay','Sözel İfade','Sözel olarak verilen iki ifadeyi eşitleyerek bilinmeyen sayıyı bulur.','düz',2,'sözel ifade → denklem · katı, eksiği, fazlası',
 'Bir sayının 3 katının 7 eksiği, bu sayının 2 katının 5 fazlasına eşittir.\nBuna göre bu sayı kaçtır?',
 12,[(19,'Sayının 7 fazlasını (12 + 7) yazmış.','dikkat'),(24,'Sayıyı değil, sayının 2 katını vermiş.','dikkat'),(29,'Eşit oldukları değeri (3x − 7) vermiş; sayıyı sormuyor.','dikkat'),(36,'Sayıyı değil, sayının 3 katını vermiş.','dikkat')],
 'Sayının kendisi.','Sayıya x de ve iki ifadeyi ayrı ayrı yaz; “eksiği” ve “fazlası” ifadelerinin işaretine dikkat et.',[DEN],
 [A('İfadeleri yaz','Sayıya x denirse.','3x − 7 = 2x + 5'),A('x’i yalnız bırak','Bilinmeyenleri bir tarafa topla.','3x − 2x = 5 + 7 → x = 12'),A('Kontrol','İki yanı hesapla.','3·12 − 7 = 29 = 2·12 + 5 ✓')],
 '“Fazlası” toplama, “eksiği” çıkarma, “katı” çarpma demektir; iki ifadeyi eşitle.')

# ---------- 0002 orta · sözel
x=7; assert Fr(5*x-8,3)==x+2==9
assert Fr(10,4)==Fr(5,2)
assert 5*(23-8)==75==3*(23+2)
assert 5*1-8==3*(1-2)
S('0002','01','orta','Sözel İfade','Sözel ifadedeki işlem sırasını koruyarak denklem kurar ve çözer.','düz',3,'sözel ifade → denklem · çıkarıp bölme',
 'Bir sayının 5 katından 8 çıkarılıp sonuç 3’e bölündüğünde, bu sayının 2 fazlası elde ediliyor.\nBuna göre bu sayı kaçtır?',
 7,[(Fr(5,2),'3’e bölmeyi unutup 5x − 8 = x + 2 yazmış: 4x = 10.','islem'),(23,'Bölmeyi 8’i çıkarmadan önce yapmış: 5(x − 8) = 3(x + 2).','dikkat'),(1,'“2 fazlası” yerine “2 eksiği”ni almış: 5x − 8 = 3(x − 2).','dikkat'),(9,'Sayıyı değil, elde edilen sonucu (x + 2) vermiş.','dikkat')],
 'Sayının kendisi.','İşlem sırasını sözdeki sıraya göre yaz; bölme işleminden sonra elde edilen değerin neye eşit olduğuna dikkat et.',[DEN],
 [A('Denklemi kur','Sayıya x denirse.','(5x − 8) ÷ 3 = x + 2'),A('Paydadan kurtul','İki yanı 3 ile çarp.','5x − 8 = 3x + 6'),A('x’i bul','Bilinmeyenleri topla.','2x = 14 → x = 7')],
 'Sözde verilen işlem sırasını bozmadan yaz; bölme varsa iki tarafı bölenle çarp.')

# ---------- 0003 orta · iki sayı
a,b=36,16; assert a+b==52 and 2*a==3*b+24 and a-b==20 and 52-24==28
assert 2*16==32
assert [n for n in range(1,52) if 2*(52-n)==3*n+24]==[16]
S('0003','01','orta','Sözel İfade','Toplamı ve bir katlar ilişkisi verilen iki sayıyı bulur.','düz',3,'sözel ifade → denklem · iki sayı',
 'Toplamları 52 olan iki pozitif tam sayıdan büyüğünün 2 katı, küçüğünün 3 katından 24 fazladır.\nBuna göre bu sayıların büyüğü kaçtır?',
 36,[(16,'Büyük sayı yerine küçük sayıyı bulmuş.','dikkat'),(20,'Sayıların farkını (36 − 16) vermiş.','dikkat'),(32,'Küçük sayının 2 katını (2 · 16) vermiş.','dikkat'),(28,'Toplamdan 24 çıkarıp (52 − 24) cevap sanmış.','bilgi')],
 'Büyük sayı.','Küçüğe b, büyüğe 52 − b de ve “2 katı, 3 katından 24 fazla” ifadesini bu iki terimle yaz.',[DEN],
 [A('Denklemi kur','Küçük sayı b, büyük sayı 52 − b.','2(52 − b) = 3b + 24'),A('b’yi bul','Parantezi aç.','104 − 2b = 3b + 24 → 5b = 80 → b = 16'),A('Büyüğü bul','Toplamdan küçüğü çıkar.','52 − 16 = 36')],
 'İki sayının toplamı verilmişse birine x, diğerine toplam − x de; tek bilinmeyenli denklem elde edilir.')

# ---------- 0004 kolay · ardışık tek
assert 31+33+35==99 and 3*32+3==99 and 33+4==37
S('0004','02','kolay','Ardışık Sayılar','Toplamı verilen ardışık tek sayıların en büyüğünü bulur.','düz',2,'ardışık sayılar · toplamdan ortanca',
 'Ardışık üç pozitif tek sayının toplamı 99’dur.\nBuna göre bu sayıların en büyüğü kaçtır?',
 35,[(31,'En büyük yerine en küçük sayıyı vermiş.','dikkat'),(33,'En büyük yerine ortanca sayıyı (99 ÷ 3) vermiş.','dikkat'),(34,'Sayıları ardışık tam sayı sanıp (32, 33, 34) en büyüğünü yazmış.','bilgi'),(37,'Ortancaya 4 ekleyerek en büyüğü bulduğunu sanmış.','islem')],
 'Üç sayının en büyüğü.','Ardışık tek sayılarda birbirine komşu iki sayı arasındaki fark ne kadardır? Toplamı ortanca terim cinsinden yaz.',[ARD,OZ],
 [A('Sayıları yaz','Ortanca sayıya m denirse.','m − 2, m, m + 2'),A('Toplamı kur','Toplamda ±2 birbirini götürür.','3m = 99 → m = 33'),A('En büyüğü bul','En büyük sayı m + 2.','33 + 2 = 35')],
 'Ardışık sayı sayısı tekse ortancayı değişken al; toplam, adet × ortancadır.')

# ---------- 0005 orta · 12 ardışık
assert sum(range(20,32))==306 and len(range(20,32))==12 and 12*19+sum(range(1,13))==306 and 19+11==30 and 20+12==32 and Fr(306,12)==Fr(51,2)
S('0005','02','orta','Ardışık Sayılar','Çift sayıda ardışık sayının toplamından en büyük sayıyı bulur.','düz',3,'ardışık sayılar · çift adet',
 'Ardışık 12 pozitif tam sayının toplamı 306’dır.\nBuna göre bu sayıların en büyüğü kaçtır?',
 31,[(20,'En büyük yerine en küçük sayıyı vermiş.','dikkat'),(25,'Ortalama 25,5’i aşağı yuvarlayıp en büyük sanmış.','dikkat'),(30,'12a + 78 = 306 yazmış (1 + … + 12 = 78); doğrusu 0 + … + 11 = 66.','bilgi'),(32,'En büyük sayıyı a + 12 almış; 12 sayıda en büyük a + 11’dir.','dikkat')],
 'Sayıların en büyüğü.','İlk sayıya a de; 12 sayının toplamında a’nın ve eklenen sabitlerin toplamını ayrı yaz.',[ARD],
 [A('Toplamı kur','İlk sayı a ise sayılar a, a + 1, …, a + 11.','12a + (0 + 1 + … + 11) = 12a + 66'),A('a’yı bul','Toplam 306’dır.','12a = 240 → a = 20'),A('En büyüğü bul','En büyük sayı a + 11.','20 + 11 = 31')],
 'n tane ardışık sayının toplamı, n × ilk sayı + (0 + 1 + … + (n − 1)) olarak yazılır.')

# ---------- 0006 orta · öncüllü
ts=[23,25,27]; assert sum(ts)==75 and all(t%2 for t in ts)
I=ts[1]==25; II=ts[2]+ts[0]==52; III=ts[2]-ts[0]==4; assert (I,II,III)==(True,False,True) and ts[2]+ts[0]==50
S('0006','02','orta','Ardışık Sayılar','Toplamı verilen ardışık tek sayılarla ilgili öncüllerin doğruluğunu sınar.','öncüllü',3,'ardışık sayılar · öncüllü',
 'Ardışık üç pozitif tek sayının toplamı 75’tir.\nBuna göre,\nI. Ortanca sayı 25’tir.\nII. En büyük sayı ile en küçük sayının toplamı 52’dir.\nIII. En büyük sayı, en küçük sayıdan 4 fazladır.\nifadelerinden hangileri doğrudur?',
 'I ve III',[('Yalnız I','III’ü kontrol etmemiş: 27 − 23 = 4 olduğundan III de doğrudur.','dikkat'),('Yalnız II','Ortancayı 26 bulup I’i yanlış saymış; ardışık tek sayılar arası fark 2 diye III’ü eleyip 26 + 26 = 52 ile II’yi doğru bulmuş.','bilgi'),('I ve II','III’ü “fark 2” sanarak eleyip II’yi ortanca + en büyük (25 + 27 = 52) hesabıyla doğru bulmuş.','islem'),('I, II ve III','II’yi sınamadan hepsini doğru kabul etmiş.','dikkat')],
 'Doğru olan öncüller.','Önce sayıları bul, sonra her öncülü bulduğun sayılarla tek tek sına.',[ARD,OZ],
 [A('Sayıları bul','Ortanca m ise 3m = 75.','m = 25 → 23, 25, 27'),A('Öncülleri sına','I: ortanca 25 ✓ · II: 23 + 27 = 50 ≠ 52 ✗ · III: 27 − 23 = 4 ✓','I ve III doğru'),A('Sonuç','Doğru olanlar I ve III’tür.','I ve III')],
 'Öncüllü sorularda önce verileni çöz, sonra her öncülü sayılarla ayrı ayrı sına.',
 sira=['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III'])

# ---------- 0007 zor · ardışık beş tek
def toplam5(f):
    return [x for x in range(1,200) if f(x)]
x=15; assert (x+x+2+x+4)==(x+6+x+8)+7 and sum(x+2*i for i in range(5))==95
assert toplam5(lambda x:3*x+6==2*x+14+7)==[15]
assert 5*11+10==65 and 3*11+3==2*11+7+7           # ardışık tam sayı
assert toplam5(lambda x:3*x+6==2*x+14-7)==[1] and sum(1+2*i for i in range(5))==25
assert 5*(15+2)==85 and 15+4==19
S('0007','02','orta','Ardışık Sayılar','İki ayrı toplam arasındaki ilişkiyi kurarak ardışık tek sayıların toplamını bulur.','düz',4,'ardışık sayılar · iki toplamın karşılaştırılması',
 'Ardışık beş pozitif tek sayıdan ilk üçünün toplamı, son ikisinin toplamından 7 fazladır.\nBuna göre bu beş sayının toplamı kaçtır?',
 95,[(19,'Beş sayının toplamı yerine ortancayı (15 + 4) vermiş.','dikkat'),(25,'“7 fazladır” yerine “7 eksiktir” kurmuş (sayılar 1, 3, 5, 7, 9).','dikkat'),(65,'Sayıları ardışık tam sayı (x, x + 1, …) alıp 11 bulmuş.','bilgi'),(85,'Beş sayının toplamını 5 × (ikinci sayı) diye hesaplamış.','islem')],
 'Beş sayının toplamı.','En küçük sayıya x de; beş sayıyı x, x + 2, … biçiminde yaz ve “ilk üçün toplamı” ile “son ikinin toplamı”nı ayrı ayrı x cinsinden bul.',[ARD],
 [A('Sayıları yaz','En küçük sayı x.','x, x + 2, x + 4, x + 6, x + 8'),A('Koşulu kur','İlk üç = son iki + 7.','(3x + 6) = (2x + 14) + 7'),A('x’i bul','Denklemi çöz.','x = 15 → 15, 17, 19, 21, 23'),A('Toplamı bul','Beş sayıyı topla.','15 + 17 + 19 + 21 + 23 = 95')],
 'Ardışık tek sayılarda sayılar x, x + 2, x + 4, … olur; iki ayrı toplamı x cinsinden yazıp eşitle.')

# ---------- 0008 kolay · ayak
t,k=10,8; assert t+k==18 and 2*t+4*k==52 and 52//4==13 and 52//2==26
assert [(a_,18-a_) for a_ in range(19) if 2*a_+4*(18-a_)==52]==[(10,8)]
S('0008','03','kolay','İki Bilinmeyen','Baş ve ayak sayısından iki tür hayvanın sayısını bulur.','hikâyeli',2,'iki bilinmeyen · baş ve ayak',
 'Bir çiftlikte yalnızca tavuk ve koyun bulunmaktadır. Hayvanların sayısı 18, ayaklarının toplam sayısı 52’dir.\nBuna göre bu çiftlikte kaç tavuk vardır?',
 10,[(13,'Ayak sayısını yalnız 4’e bölmüş (52 ÷ 4).','dikkat'),(18,'Hayvan sayısını (18) tavuk sayısı sanmış.','dikkat'),(26,'Ayak sayısını yalnız 2’ye bölmüş (52 ÷ 2).','dikkat'),(52,'Ayak sayısını cevap olarak yazmış.','dikkat')],
 'Tavuk sayısı.','Tavuk sayısına t, koyun sayısına 18 − t de ve ayakların toplamını yaz.',[IKI],
 [A('Denklemi kur','Tavuk t, koyun 18 − t.','2t + 4(18 − t) = 52'),A('t’yi bul','Parantezi aç.','72 − 2t = 52 → t = 10'),A('Kontrol','Koyun 8; ayaklar 20 + 32 = 52 ✓','10 tavuk')],
 'Baş sayısı toplamı, ayak sayısı ağırlıklı toplamı verir; biri öbürüne yerleştirilir.')

# ---------- 0009 orta · madeni para
x=19; assert x+(37-x)==37 and 1*x+5*(37-x)==109 and (109-37)//2==36 and 109-37==72 and 109//5==21
assert [a_ for a_ in range(38) if a_+5*(37-a_)==109]==[19]
S('0009','03','orta','İki Bilinmeyen','Madeni para adedi ve toplam tutardan 1 TL’lik para sayısını bulur.','hikâyeli',3,'iki bilinmeyen · madeni para',
 'Bir kumbarada yalnızca 1 TL’lik ve 5 TL’lik madeni paralar vardır. Kumbarada toplam 37 madeni para ve 109 TL bulunduğuna göre 1 TL’lik madeni paraların sayısı kaçtır?',
 19,[(36,'5 TL ile 1 TL farkını 4 yerine 2 sanıp (109 − 37) ÷ 2 işlemini yapmış.','islem'),(18,'1 TL’lik yerine 5 TL’lik paraların sayısını vermiş.','dikkat'),(21,'109 ÷ 5 işleminin tam kısmını alıp cevap sanmış.','bilgi'),(72,'Toplam tutardan para adedini çıkarıp (109 − 37) cevap saymış.','islem')],
 '1 TL’lik madeni paraların sayısı.','1 TL’liklerin sayısına x de; 5 TL’liklerin sayısını x cinsinden yaz ve tutarı kur.',[IKI],
 [A('Denklemi kur','1 TL’lik x, 5 TL’lik 37 − x tane.','x + 5(37 − x) = 109'),A('x’i bul','Parantezi aç.','185 − 4x = 109 → x = 19'),A('Kontrol','5 TL’lik 18 tane; 19 + 90 = 109 ✓','19')],
 'Adet toplamı ve tutar toplamı iki denklem verir; birini x cinsinden yazıp öbürüne yerleştir.')

# ---------- 0010 orta · koli (iki ağırlık türü)
b_,a_=10,14; assert a_+b_==24 and 5*a_+10*b_==170 and 170//10==17 and 24-17==7 and (170-24*5)//10==5
assert [(x_,24-x_) for x_ in range(25) if 5*x_+10*(24-x_)==170]==[(14,10)]
S('0010','03','orta','İki Bilinmeyen','Koli sayısı ve toplam ağırlıktan 10 kg’lık kolilerin sayısını bulur.','hikâyeli',3,'iki bilinmeyen · iki ağırlık türü',
 'Bir manav, yalnızca 5 kg’lık ve 10 kg’lık portakal kolileri satın almıştır. Toplam 24 koli almış ve bu kolilerin toplam ağırlığı 170 kg olmuştur.\nBuna göre manav kaç tane 10 kg’lık koli almıştır?',
 10,[(5,'Hepsi 5 kg sayıp farkı (50 kg) 10’a bölmüş; birim fark 5 kg’dır.','islem'),(7,'170 ÷ 10 = 17 koliyi 10 kg’lık sanıp toplamdan çıkarmış (24 − 17).','bilgi'),(14,'10 kg’lık yerine 5 kg’lık kolilerin sayısını vermiş.','dikkat'),(17,'Bütün kolileri 10 kg’lık sayıp 170 ÷ 10 yapmış.','bilgi')],
 '10 kg’lık kolilerin sayısı.','Ağır kolilerin sayısına x de; hafif kolilerin sayısını x cinsinden yaz ve toplam ağırlığı kur.',[IKI],
 [A('Denklemi kur','10 kg’lık x, 5 kg’lık 24 − x tane.','10x + 5(24 − x) = 170'),A('x’i bul','Parantezi aç.','5x + 120 = 170 → x = 10'),A('Kontrol','5 kg’lık 14 tane: 10·10 + 14·5.','100 + 70 = 170 ✓')],
 'Adet toplamı ve ağırlık toplamı iki denklem verir; birini x cinsinden yazıp öbürüne yerleştir.')

# ---------- 0011 zor · üç tür tekerlek
b_,t_,k_=9,4,5; assert b_==2*t_+1 and b_+t_+k_==18 and 2*b_+3*t_+4*k_==50 and 18-4==14
sol=[(b,t,18-b-t) for b in range(19) for t in range(19) if b==2*t+1 and 18-b-t>=0 and 2*b+3*t+4*(18-b-t)==50]; assert sol==[(9,4,5)]
S('0011','03','zor','İki Bilinmeyen','Araç ve tekerlek sayılarını üç türlü araç için kurup dört tekerlekli araç sayısını bulur.','hikâyeli',4,'iki bilinmeyen · üç tür araç',
 'Bir lunaparkta yalnızca bisiklet (2 tekerlekli), üç tekerlekli bisiklet ve dört tekerlekli elektrikli araç bulunmaktadır. Toplam 18 araç ve 50 tekerlek vardır. Bisikletlerin sayısı, üç tekerlekli bisikletlerin sayısının 2 katından 1 fazladır.\nBuna göre dört tekerlekli elektrikli araçların sayısı kaçtır?',
 5,[(4,'Üç tekerlekli bisiklet sayısını vermiş.','dikkat'),(9,'Bisiklet sayısını vermiş.','dikkat'),(14,'Toplam araçtan yalnız üç tekerlekli sayısını çıkarmış (18 − 4).','islem'),(18,'Toplam araç sayısını cevap yazmış.','dikkat')],
 'Dört tekerlekli araç sayısı.','Üç tekerlekli sayısına t de; bisiklet ve dört tekerlekli sayısını t cinsinden yazıp tekerlek toplamını kur.',[IKI],
 [A('Sayıları t cinsinden yaz','Üç tekerlekli t, bisiklet 2t + 1, dört tekerlekli 18 − (3t + 1) = 17 − 3t.','b = 2t + 1 · k = 17 − 3t'),A('Tekerlekleri topla','2(2t + 1) + 3t + 4(17 − 3t) = 50.','70 − 5t = 50'),A('t’yi bul','Denklemi çöz.','t = 4 → bisiklet 9'),A('İstenen','k = 17 − 3·4.','5')],
 'Üç tür varsa verilen ek ilişkiyle ikisini üçüncü cinsinden yaz; tek bilinmeyenli denklem kalır.')

# ---------- 0012 orta · fındık (eksik-fazla)
n=10; assert 5*n+12==7*n-8==62 and (12+8)// (7-5)==10 and (12-8)//2==2 and 5*2+12==22 and 5*n==50
assert [m for m in range(1,100) if 5*m+12==7*m-8]==[10]
S('0012','04','orta','Eksik – Fazla','Kişi başı iki ayrı dağıtımdaki artan ve eksik miktardan mal sayısını bulur.','hikâyeli',3,'eksik–fazla · kişi başı iki dağıtım',
 'Bir miktar fındık, bir grup çocuğa kişi başı 5 tane verilirse 12 tane artıyor, kişi başı 7 tane verilirse 8 tane eksik kalıyor.\nBuna göre fındık sayısı kaçtır?',
 62,[(10,'Çocuk sayısını bulup fındık sayısı sanmış.','dikkat'),(12,'Artan fındık sayısını vermiş.','dikkat'),(22,'Çocuk sayısını (12 − 8) ÷ 2 = 2 bulmuş: 5·2 + 12.','islem'),(50,'Yalnız 5 × 10 işlemini yapıp artanı eklememiş.','dikkat')],
 'Fındık sayısı.','Çocuk sayısına x de; fındık sayısını iki dağıtımdan ayrı ayrı yaz ve eşitle.',[EF],
 [A('Eşitliği kur','Artan eklenir, eksik çıkarılır.','5x + 12 = 7x − 8'),A('x’i bul','Bilinmeyenleri topla.','20 = 2x → x = 10'),A('Fındığı bul','5·10 + 12.','62 · kontrol: 7·10 − 8 = 62 ✓')],
 'Artan miktar eklenir, eksik miktar çıkarılır; iki dağıtımdaki mal sayısını eşitle.')

# ---------- 0013 orta · sıralar
n=12; assert 3*n+4==40==4*(n-2) and 3*6+4==22==4*6-2 and 3*n==36 and 4*n==48
assert [m for m in range(1,100) if 3*m+4==4*(m-2)]==[12]
S('0013','04','orta','Eksik – Fazla','Sıralara oturma düzenlerinden öğrenci sayısını bulur.','hikâyeli',3,'eksik–fazla · sıra ve boş sıra',
 'Bir sınıfta öğrenciler sıralara üçer kişi oturduğunda 4 öğrenci ayakta kalıyor. Dörder kişi oturduklarında ise 2 sıra boş kalıyor, boş sıralar dışındaki sıraların hepsi tam dolu oluyor.\nBuna göre sınıfta kaç öğrenci vardır?',
 40,[(12,'Sıra sayısını bulup öğrenci sayısı sanmış.','dikkat'),(22,'“2 sıra boş” koşulunu “2 öğrenci eksik” diye okumuş: 3n + 4 = 4n − 2.','bilgi'),(36,'Yalnız 3 × 12 işlemini yapıp ayakta kalan 4 öğrenciyi eklememiş.','dikkat'),(48,'4 × 12 işlemini yapıp boş kalan 2 sırayı çıkarmamış.','dikkat')],
 'Öğrenci sayısı.','Sıra sayısına n de; öğrenci sayısını üçerli ve dörderli oturma durumlarından ayrı yaz.',[EF],
 [A('Eşitliği kur','Üçer: 3n + 4. Dörder: dolu sıra n − 2.','3n + 4 = 4(n − 2)'),A('n’i bul','Parantezi aç.','3n + 4 = 4n − 8 → n = 12'),A('Öğrenci sayısı','3·12 + 4.','40 · kontrol: 4·10 = 40 ✓')],
 'Boş kalan sıralar dağıtımı yapılan sıra sayısını azaltır; toplam sayıyı iki yoldan yaz ve eşitle.')

# ---------- 0014 zor · kitap, son öğrenciye 3
n=7; assert 6*n+9==8*(n-1)+3==51 and 6*3+9==27 and 6*n==42 and 8*(n-1)==48
assert [m for m in range(1,100) if 6*m+9==8*(m-1)+3]==[7]
assert [m for m in range(1,100) if 6*m+9==8*m+3]==[3]
S('0014','04','zor','Eksik – Fazla','Son kişiye kalan az miktarın bulunduğu paylaştırmada mal sayısını bulur.','hikâyeli',4,'eksik–fazla · son kişiye düşen pay',
 'Bir miktar kitap bir grup öğrenciye 6’şar tane dağıtılırsa 9 kitap artıyor. Aynı kitaplar 8’er tane dağıtılırsa son öğrenciye 3 kitap düşüyor ve hiç kitap kalmıyor.\nBuna göre kitap sayısı kaçtır?',
 51,[(7,'Öğrenci sayısını bulup kitap sayısı sanmış.','dikkat'),(27,'Son öğrenciyi de 8 almış sayıp 6n + 9 = 8n + 3 yazmış (n = 3).','bilgi'),(42,'Yalnız 6 × 7 işlemini yapıp artan 9 kitabı eklememiş.','dikkat'),(48,'Yalnız 8 × 6 işlemini yapıp son öğrencinin 3 kitabını eklememiş.','dikkat')],
 'Kitap sayısı.','Öğrenci sayısına n de; 8’erli dağıtımda son öğrenci dışındaki (n − 1) öğrenci 8’er kitap alır.',[EF],
 [A('İlk dağıtım','n öğrenci 6’şar alırsa 9 artar.','kitap = 6n + 9'),A('İkinci dağıtım','n − 1 öğrenci 8’er, son öğrenci 3.','kitap = 8(n − 1) + 3'),A('n’i bul','İki ifadeyi eşitle.','6n + 9 = 8n − 5 → n = 7'),A('Kitap sayısı','6·7 + 9.','51 · kontrol: 8·6 + 3 = 51 ✓')],
 'Son kişiye tam pay düşmüyorsa önceki kişilerin payı ayrı, son kişinin payı ayrı yazılır.')

# ---------- 0015 zor · öğrenci sayısı azalırsa
n=21; assert 5*n+14==119==7*(n-4) and 5*n==105 and 7*n==147
assert [m for m in range(1,100) if 5*m+14==7*(m-4)]==[21] and 5*9+14==59 and [m for m in range(1,100) if 5*m+14==7*m-4]==[9]
S('0015','04','orta','Eksik – Fazla','Öğrenci sayısı değişince oluşan dağıtım farkından mal sayısını bulur.','hikâyeli',3,'eksik–fazla · kişi sayısı değişiyor',
 'Bir miktar defter bir grup öğrenciye 5’er tane dağıtılırsa 14 defter artıyor. Öğrenci sayısı 4 az olsaydı aynı defterler 7’şer tane dağıtıldığında hiç defter artmayacaktı.\nBuna göre defter sayısı kaçtır?',
 119,[(21,'Öğrenci sayısını bulup defter sayısı sanmış.','dikkat'),(59,'“Öğrenci sayısı 4 az” koşulunu 7n − 4 diye yazmış (n = 9).','bilgi'),(105,'Yalnız 5 × 21 işlemini yapıp artan 14 defteri eklememiş.','dikkat'),(147,'7 × 21 işlemini yapıp 4 öğrencilik farkı hesaba katmamış.','dikkat')],
 'Defter sayısı.','Öğrenci sayısına n de; ikinci dağıtımda öğrenci sayısının n − 4 olduğunu unutma.',[EF],
 [A('Eşitliği kur','İlk: 5n + 14. İkinci: n − 4 öğrenci 7’şer.','5n + 14 = 7(n − 4)'),A('n’i bul','Parantezi aç.','5n + 14 = 7n − 28 → n = 21'),A('Defter sayısı','5·21 + 14.','119 · kontrol: 7·17 = 119 ✓')],
 'Kişi sayısı değişiyorsa ikinci dağıtımda yeni kişi sayısını kullan; sonra toplamı eşitle.')

# ---------- 0016 kolay · kuyruk
assert 8+12-1==19 and abs(8-12)==4 and 8+12-2==18 and 8+12==20 and 8*12==96
S('0016','05','kolay','Sıra – Kuyruk','Baştan ve sondan sıradan toplam kişi sayısını bulur.','hikâyeli',2,'sıra ve kuyruk · baştan–sondan',
 'Bir kuyrukta Ali baştan 8., sondan 12. sıradadır.\nBuna göre bu kuyrukta kaç kişi vardır?',
 19,[(4,'Sıra numaralarının farkını (12 − 8) vermiş.','dikkat'),(18,'8 + 12’den 2 çıkarmış; Ali’yi bir kez saymak gerekir.','dikkat'),(20,'8 + 12 toplamını Ali’yi iki kez sayarak vermiş.','dikkat'),(96,'Sıra numaralarını çarpmış.','dikkat')],
 'Kuyruktaki kişi sayısı.','Ali’nin önündeki ve arkasındaki kişileri ayrı ayrı say.',[SIRA],
 [A('Ali’nin önü','Baştan 8. ise önünde 7 kişi var.','7'),A('Ali’nin arkası','Sondan 12. ise arkasında 11 kişi var.','11'),A('Toplam','Önündekiler + Ali + arkasındakiler.','7 + 1 + 11 = 19')],
 'Baştan a., sondan b. sırada olan kişi için kuyruk a + b − 1 kişidir.')

# ---------- 0017 orta · kat
kat=lambda n,k=6:(n-1)//k
assert kat(22)==3 and kat(41)==6 and kat(41)-kat(22)==3 and -(-(41-22)//6)==4 and 41-22==19 and kat(41)==6
S('0017','05','orta','Sıra – Kuyruk','Daire numaralarından iki dairenin bulunduğu katlar arasındaki farkı bulur.','hikâyeli',3,'kat ve numara · zemin kattan başlayan numaralama',
 'Her katında 6 daire bulunan bir apartmanda daireler, zemin kattan başlayarak 1’den itibaren ardışık olarak numaralanmıştır (zemin katta 1–6, birinci katta 7–12, … numaralı daireler bulunur).\nAli 22 numaralı dairede, Ayşe 41 numaralı dairede oturduğuna göre Ayşe, Ali’nin kaç kat üstünde oturmaktadır?',
 3,[(4,'Daire numaraları farkını (19) 6’ya bölüp yukarı yuvarlamış.','bilgi'),(6,'Ayşe’nin bulunduğu katı (6. kat) cevap sanmış.','dikkat'),(7,'Ayşe’nin dairesini 7. grupta bulup kat farkı yerine bu sayıyı vermiş.','dikkat'),(19,'Daire numaralarının farkını vermiş.','dikkat')],
 'Ayşe’nin Ali’nin kaç kat üstünde oturduğu.','Her dairenin katını ayrı ayrı bul; zemin katın 0. kat olduğunu unutma.',[KAT],
 [A('Ali’nin katı','(22 − 1) ÷ 6’nın tam kısmı.','21 ÷ 6 = 3 kalan 3 → 3. kat'),A('Ayşe’nin katı','(41 − 1) ÷ 6’nın tam kısmı.','40 ÷ 6 = 6 kalan 4 → 6. kat'),A('Fark','Kat numaralarını çıkar.','6 − 3 = 3')],
 'Numara farkını doğrudan bölmek yerine her dairenin katını ayrı bul, sonra çıkar.')

# ---------- 0018 zor · kuyruk, Eda
cem=6; den=cem+9+1; top=den+5-1; eda=cem+5; assert (den,top,eda)==(16,20,11) and top-eda+1==10 and top-eda==9
S('0018','05','zor','Sıra – Kuyruk','Aradaki kişi sayısı ve orta kişi bilgisiyle sondan sırayı bulur.','hikâyeli',4,'sıra ve kuyruk · arada kalan kişiler',
 'Bir kuyrukta Cem baştan 6. sıradadır. Deniz, Cem’in arkasındadır ve Cem ile Deniz arasında 9 kişi vardır. Deniz sondan 5. sıradadır. Eda, Cem ile Deniz arasındaki bu 9 kişinin tam ortasındadır.\nBuna göre Eda sondan kaçıncı sıradadır?',
 10,[(9,'Sondan sırayı 20 − 11 = 9 bulmuş; Eda’yı da saymak gerekir (+1).','dikkat'),(11,'Eda’nın baştan sırasını vermiş.','dikkat'),(16,'Deniz’in baştan sırasını vermiş.','dikkat'),(20,'Kuyruktaki toplam kişi sayısını vermiş.','dikkat')],
 'Eda’nın sondan sırası.','Önce Deniz’in baştan sırasını, sonra kuyruğun toplam uzunluğunu bul.',[SIRA],
 [A('Deniz’in sırası','Cem 6., arada 9 kişi var.','6 + 9 + 1 = 16. sıra'),A('Kuyruk uzunluğu','Deniz sondan 5.','16 + 5 − 1 = 20 kişi'),A('Eda’nın sırası','9 kişinin ortası 5. kişidir.','6 + 5 = 11. sıra (baştan)'),A('Sondan sıra','Toplam − baştan sıra + 1.','20 − 11 + 1 = 10')],
 'Arada n kişi varsa sıra farkı n + 1’dir; baştan sıradan sondan sıraya geçerken toplam − sıra + 1 kullan.')

# ---------- 0019 kolay · para üstü
assert 200-12-4*38==36 and 200-4*38==48 and 200-4*38+12==60 and 4*38==152 and 200-12==188
S('0019','06','kolay','Alışveriş','Para üstünden yararlanarak bir ürünün fiyatını bulur.','hikâyeli',2,'alışveriş · para üstü',
 'Bir öğrenci, tanesi 38 TL olan 4 kalem ile 1 defter almak için kasiyere 200 TL veriyor ve 12 TL para üstü alıyor.\nBuna göre defterin fiyatı kaç TL’dir?',
 36,[(48,'Para üstünü hesaba katmamış: 200 − 152.','dikkat'),(60,'Para üstünü çıkarmak yerine eklemiş: 200 − 152 + 12.','dikkat'),(152,'Kalemlerin toplam fiyatını vermiş.','dikkat'),(188,'Ödenen tutarı (200 − 12) vermiş.','dikkat')],
 'Defterin fiyatı (TL).','Önce kasiyere gerçekte ne kadar ödendiğini bul, sonra kalemlerin bedelini çıkar.',[ALIS],
 [A('Ödenen tutar','Verilen para − para üstü.','200 − 12 = 188 TL'),A('Kalemlerin bedeli','4 kalem.','4 · 38 = 152 TL'),A('Defter','Ödenen − kalemler.','188 − 152 = 36 TL')],
 'Verilen para = alınanların bedeli + para üstü; önce gerçek ödemeyi bul.')

# ---------- 0020 orta · fiyat listesi (tablo)
c,t=15,55; assert 2*c+3*t==195 and 3*c+t==100 and t-c==40 and 195-100==95 and c+t==70
assert [(c_,t_) for c_ in range(1,100) for t_ in range(1,100) if 2*c_+3*t_==195 and 3*c_+t_==100]==[(15,55)]
S('0020','06','orta','Alışveriş','İki hesap fişinden iki ürünün fiyat farkını bulur.','tablo',3,'alışveriş · fiyat listesi, iki fiş',
 'Bir kafede çay ve tostun fiyatları sabittir. Aynı gün kesilen iki hesap fişinin içeriği şöyledir:\nFiş 1: 2 çay + 3 tost = 195 TL\nFiş 2: 3 çay + 1 tost = 100 TL\nBuna göre bir tost, bir çaydan kaç TL pahalıdır?',
 40,[(15,'Çayın fiyatını vermiş.','dikkat'),(55,'Tostun fiyatını vermiş.','dikkat'),(70,'Bir çay ile bir tostun toplam fiyatını vermiş.','dikkat'),(95,'İki fişin toplam farkını (195 − 100) ürün farkı sanmış.','bilgi')],
 'Tost fiyatı ile çay fiyatı arasındaki fark (TL).','İki fişten birini seçip bir ürünü diğeri cinsinden ifade etmeyi dene.',[IKI],
 [A('Denklemleri yaz','Çay c, tost t.','2c + 3t = 195 · 3c + t = 100'),A('Yerleştir','t = 100 − 3c.','2c + 300 − 9c = 195 → c = 15'),A('Tostu bul','t = 100 − 45.','t = 55'),A('Fark','Tost − çay.','55 − 15 = 40')],
 'İki fişten iki bilinmeyenli denklem kurulur; birinden bir ürünü çıkarıp öbürüne yerleştir.')

# ---------- 0021 zor · para, iki alışveriş
g,p=300,415; M=1820; assert 3*g+2*p+90==M and 2*g+3*p==M+25 and g+p==715 and 3*g+2*p==1730 and 2*g+3*p==1845 and p-g==115
assert [(g_,p_) for g_ in range(1,2000) for p_ in range(1,2000) if g_+p_==715 and 2*g_+3*p_-(3*g_+2*p_)==115]==[(300,415)]
assert 5*(g+p)==2*M-65 and (5*715+65)//2==1820
S('0021','06','zor','Alışveriş','İki ayrı alışveriş durumundan (artan ve eksik para) kişinin parasını bulur.','hikâyeli',4,'alışveriş · artan ve eksik para',
 'Can, parasıyla 3 gömlek ve 2 pantolon alırsa 90 TL artmakta, 2 gömlek ve 3 pantolon almak isterse 25 TL eksik kalmaktadır. Bir gömlek ile bir pantolonun birlikte fiyatı 715 TL’dir.\nBuna göre Can’ın parası kaç TL’dir?',
 1820,[(415,'Pantolonun fiyatını vermiş.','dikkat'),(715,'Verilen gömlek + pantolon fiyatını cevap sanmış.','dikkat'),(1730,'Artan 90 TL’yi paraya eklememiş (3 gömlek + 2 pantolon).','dikkat'),(1845,'İkinci alışverişin tutarını (parası + 25) vermiş.','dikkat')],
 'Can’ın parası (TL).','Parası M olsun; iki alışverişin tutarını M cinsinden yaz ve farklarını al.',[ALIS,IKI],
 [A('Tutarları M ile yaz','Artan çıkarılır, eksik eklenir.','3g + 2p = M − 90 · 2g + 3p = M + 25'),A('Farkı al','İkinciden birinciyi çıkar.','p − g = 115'),A('Fiyatları bul','g + p = 715.','p = 415, g = 300'),A('Parayı bul','3·300 + 2·415 + 90.','900 + 830 + 90 = 1820 · kontrol: 600 + 1245 = 1845 = 1820 + 25 ✓')],
 'Artan ve eksik para iki alışverişin tutar farkını verir; M kendiliğinden yok olur.',
 kisa='İki alışverişi taraf tarafa topla: 5(g + p) = 2M − 65. g + p = 715 olduğundan 3575 = 2M − 65, M = 1820.')

# ---------- 0022 kolay · merdiven
assert 54//3==18 and 18*5==90 and 18*4==72 and 18*6==108 and 54*5==270
KB=B('Kat ve basamak','n. kata çıkmak için n kat çıkılır; kat sayısı × bir katın basamak sayısı = toplam basamak. Örnek: bir katta 12 basamak varsa 4. kata 48 basamak çıkılır')
S('0022','07','kolay','Merdiven','Katlar arasında eşit basamak sayısından istenen kata çıkılan basamak sayısını bulur.','hikâyeli',3,'merdiven · eşit basamak',
 'Bir binada her iki kat arasındaki merdiven basamaklarının sayısı eşittir. Zemin kattan 3. kata çıkarken 54 basamak çıkılmaktadır.\nBuna göre zemin kattan 5. kata çıkarken kaç basamak çıkılır?',
 90,[(18,'Bir katın basamak sayısını vermiş.','dikkat'),(72,'4. kata çıkılan basamağı hesaplamış (4 kat).','dikkat'),(108,'6 kat saymış.','dikkat'),(270,'54 ile 5’i çarpmış.','islem')],
 'Zemin kattan 5. kata çıkılan basamak sayısı.','Zemin kattan 3. kata kaç kat çıkıldığını sayarak bir katın basamak sayısını bul.',[KB],
 [A('Bir kat','Zemin kattan 3. kata 3 kat çıkılır.','54 ÷ 3 = 18 basamak'),A('5 kat','Zemin kattan 5. kata 5 kat çıkılır.','5 · 18 = 90'),A('Kontrol','3 kat için tekrar hesapla.','3 · 18 = 54 ✓')],
 'Zemin kattan n. kata n kat çıkılır; önce bir katın değerini bul.')

# ---------- 0023 orta · kurbağa
top=lambda n:3*(n-1)+5
assert top(5)==17>=17 and top(4)==14<17
assert min(n for n in range(1,50) if top(n)>=17)==5
assert -(-17//5)==4 and -(-17//3)==6 and min(n for n in range(1,50) if 3*n-2>=17)==7 and -(-17//2)==9
S('0023','07','orta','Gündüz – Gece','Gündüz çıkıp geceleyin kayan hareketle hedefe ulaşma gününü bulur.','hikâyeli',3,'gündüz çıkma, gece kayma',
 'Bir kurbağa, 17 metre derinliğindeki bir kuyudan çıkmaya çalışmaktadır. Her gün gündüz 5 metre yukarı tırmanmakta, her gece 2 metre aşağı kaymaktadır. Kurbağa ilk gün sabahı kuyunun dibinden başlamıştır.\nBuna göre kurbağa kuyunun ağzına kaçıncı gün ulaşır?',
 5,[(4,'Kaymayı hiç hesaba katmamış: 17 ÷ 5’i yukarı yuvarlamış.','dikkat'),(6,'Her gün net 3 metre sanıp 17 ÷ 3’ü yukarı yuvarlamış.','dikkat'),(7,'Gün sonunda yüksekliği 3n − 2 almış (3n − 2 ≥ 17).','bilgi'),(9,'Yalnız gecelik kaymayı sayıp 17 ÷ 2’yi yukarı yuvarlamış.','dikkat')],
 'Kurbağanın kuyunun ağzına ulaştığı gün.','İlk n − 1 günün sonundaki yüksekliği bul; son gün gündüz çıkışın bitirip bitirmediğine bak.',[TIR],
 [A('Net kazanç','Bir günde gündüz 5, gece −2.','5 − 2 = 3 m/gün'),A('Son günden önce','n − 1 gün sonunda yükseklik 3(n − 1); son gün 5 m çıkış yeter.','3(n − 1) + 5 ≥ 17'),A('n’i bul','En küçük tam sayı.','3(n − 1) ≥ 12 → n ≥ 5'),A('Kontrol','4. gün en yüksek nokta 14 < 17; 5. gün 17 ✓','5. gün')],
 'Hedefe son gün kayma olmadan ulaşılır; son günün çıkışını ayrı tut, önceki günleri net kazançla say.')

# ---------- 0024 orta · bilye, kalan koşulları
sol=[n for n in range(101,130) if n%3==2 and n%4==3 and n%5==4]; assert sol==[119]
assert [n for n in range(101,130) if n%60==0]==[120] and [n for n in range(101,130) if n%60==1]==[121] and [n for n in range(101,130) if n%60==4]==[124] and 120-2==118
EK=B('Ortak katlar','3, 4 ve 5’e tam bölünen sayılar, bu sayıların en küçük ortak katı olan 60’ın katlarıdır. Örnek: 2 ve 3’e tam bölünen sayılar 6’nın katlarıdır: 6, 12, 18, …')
S('0024','07','orta','Kalan Koşulları','Farklı gruplamalarda artan bilye sayılarından bilye sayısını bulur.','hikâyeli',4,'kalan koşulları · gruplama',
 'Bir kutudaki bilyelerin sayısı 100’den büyük ve 130’dan küçüktür. Bilyeler 3’erli gruplanınca 2, 4’erli gruplanınca 3, 5’erli gruplanınca 4 bilye artmaktadır.\nBuna göre kutuda kaç bilye vardır?',
 119,[(118,'Bilye sayısını 60’ın katından 2 eksik almış (N = 60k − 2).','bilgi'),(120,'Artanları yok sayıp 3, 4 ve 5’in ortak katını (60’ın katı) almış.','bilgi'),(121,'Bütün artanları 1 sanıp N = 60k + 1 almış.','bilgi'),(124,'Bütün gruplamalarda artanı 4 almış (N = 60k + 4).','bilgi')],
 'Kutudaki bilye sayısı.','Her gruplamada artanı grup büyüklüğüyle karşılaştır; ortak bir durum var mı?',[EK],
 [A('Artanlara bak','Artan her seferinde grup büyüklüğünden 1 eksik.','3 − 2 = 4 − 3 = 5 − 4 = 1'),A('Bir ekle','N + 1 sayısı 3, 4 ve 5’e tam bölünür.','N + 1, 60’ın katı'),A('Aralığı uygula','100 < N < 130.','N + 1 = 120 → N = 119'),A('Kontrol','119 = 3·39 + 2 = 4·29 + 3 = 5·23 + 4 ✓','119')],
 'Artanlar grup büyüklüğünden hep aynı miktar eksikse sayıya bu miktarı ekle; ortak kat bulunur.')

# ---------- 0025 orta · takvim
gun=['Pazartesi','Salı','Çarşamba','Perşembe','Cuma','Cumartesi','Pazar']
ay=[31,28,31,30,31,30,31,31]; d=sum(ay); assert d==243 and d%7==5 and gun[(3+d)%7]=='Salı'   # 1 Ocak Perşembe (indeks 3)
assert gun[(3+d+1)%7]=='Çarşamba' and gun[(3+d-1)%7]=='Pazartesi' and gun[(3+8*30)%7]=='Cumartesi' and gun[(3+8*31)%7]=='Pazar'
S('0025','07','orta','Takvim','Ayların gün sayılarından yola çıkarak iki tarih arasındaki gün farkıyla haftanın gününü bulur.','hikâyeli',3,'takvim · yıl içinde haftanın günü',
 'Artık yıl olmayan bir yılın 1 Ocak günü Perşembe’dir.\nBuna göre aynı yılın 1 Eylül günü haftanın hangi günüdür?',
 'Salı',[('Çarşamba','Şubat’ı 29 gün saymış (artık yıl varsaymış).','dikkat'),('Pazartesi','Ağustos’u 30 gün alıp 242 gün saymış.','dikkat'),('Cumartesi','Her ayı 30 gün sayıp 8 × 30 = 240 gün hesaplamış.','bilgi'),('Pazar','Her ayı 31 gün sayıp 8 × 31 = 248 gün hesaplamış.','bilgi')],
 'Haftanın günü.','1 Ocak ile 1 Eylül arasında kaç gün geçtiğini ay ay topla ve 7’ye böl.',[PER],
 [A('Gün sayısı','Ocak’tan Ağustos’a kadar 8 ay.','31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 = 243 gün'),A('7’ye böl','Tam haftaları at.','243 = 7·34 + 5 → kalan 5'),A('Günü bul','Perşembe’den 5 gün sonrası.','Cuma, Cumartesi, Pazar, Pazartesi, Salı → Salı')],
 'Tarihler arası gün sayısını bulup 7’ye böl; yalnız kalan günü ileri sayılır.',
 sira=['Pazartesi','Salı','Çarşamba','Cumartesi','Pazar'])

# ---------- 0026 orta · puanlama
d=24; assert 5*d-2*(30-d)==108 and 30-d==6 and [m for m in range(31) if 5*m+2*(30-m)==108]==[16]
assert 108//5==21 and -(-108//5)==22 and [m for m in range(31) if 5*m-2*(30-m)==108]==[24]
S('0026','08','orta','Puanlama','Doğru ve yanlış cevap puanlarından doğru sayısını bulur.','hikâyeli',3,'puanlama · doğru ve yanlış',
 'Bir testte 30 soru vardır. Her doğru cevap için 5 puan verilmekte, her yanlış cevap için 2 puan düşülmekte, boş bırakılan sorulara puan verilmemekte ve puan düşülmemektedir. Tüm soruları cevaplayan Deniz’in puanı 108’dir.\nBuna göre Deniz kaç soruyu doğru cevaplamıştır?',
 24,[(6,'Doğru yerine yanlış sayısını vermiş.','dikkat'),(16,'Yanlışın puanını eklemiş: 5d + 2(30 − d) = 108.','bilgi'),(21,'108 ÷ 5 işleminin tam kısmını vermiş.','dikkat'),(22,'108 ÷ 5 işlemini yukarı yuvarlamış.','dikkat')],
 'Doğru cevap sayısı.','Doğru sayısına d de; yanlış sayısını 30 − d yaz ve puanı doğru − yanlış olarak kur.',[PUAN],
 [A('Puan denklemini kur','Doğru d, yanlış 30 − d.','5d − 2(30 − d) = 108'),A('d’yi bul','Parantezi aç.','7d − 60 = 108 → d = 24'),A('Kontrol','Yanlış 6; 120 − 12 = 108 ✓','24')],
 'Tüm sorular cevaplanmışsa yanlış sayısı toplamdan doğruyu çıkararak yazılır; puan farkı kurulur.')

# ---------- 0027 orta · net
D,Y=26,8; assert D+Y+6==40 and D-Y/4==24 and 24+8==32 and D+Y==34
assert [(a_,b_) for a_ in range(41) for b_ in range(41-a_) if a_+b_==34 and a_-b_/4==24]==[(26,8)]
S('0027','08','orta','Puanlama','Boş sayısı ve net bilgisinden doğru sayısını bulur.','hikâyeli',3,'puanlama · net hesabı',
 'Bir testte 40 soru vardır. Her 4 yanlış cevap 1 doğru cevabı götürmektedir. Ece 6 soruyu boş bırakmış ve neti 24 olmuştur.\nBuna göre Ece kaç soruyu doğru cevaplamıştır?',
 26,[(8,'Doğru yerine yanlış sayısını vermiş.','dikkat'),(24,'Neti doğru sayısı sanmış.','dikkat'),(32,'Neti yanlış sayısıyla (8) düzeltmiş; doğrusu yanlışın dörtte biri.','islem'),(34,'Cevaplanan soru sayısını (doğru + yanlış) vermiş.','dikkat')],
 'Doğru cevap sayısı.','Cevaplanan soru sayısını bul; doğruya d, yanlışa 34 − d de ve net formülüne yaz.',[PUAN],
 [A('Cevaplanan soru','40 − 6.','d + y = 34'),A('Net denklemi','Net = doğru − yanlış ÷ 4.','d − (34 − d)/4 = 24'),A('d’yi bul','4 ile çarp.','4d − 34 + d = 96 → d = 26'),A('Kontrol','Yanlış 8; 26 − 2 = 24 ✓','26')],
 'Net = doğru − yanlış ÷ 4; boşlar cevaplanan soru sayısından düşülür.')

# ---------- 0028 zor · iki sınav
assert 4*11-(25-11)==30==5*10-2*(20-10) and 11+10==21
cands=[(a_,b_) for a_ in range(26) for b_ in range(21) if a_+b_==21 and 4*a_-(25-a_)==5*b_-2*(20-b_)]; assert cands==[(11,10)]
assert 30+30==60
S('0028','08','zor','Puanlama','İki ayrı puanlama kuralında eşit puan ve toplam doğru koşulundan puanı bulur.','hikâyeli',4,'puanlama · iki sınav',
 'Ece, her birinde tüm soruları cevapladığı iki sınava girmiştir. Birinci sınav 25 sorudan oluşmakta, her doğru cevap 4 puan, her yanlış cevap −1 puan getirmektedir. İkinci sınav 20 sorudan oluşmakta, her doğru cevap 5 puan, her yanlış cevap −2 puan getirmektedir. Ece iki sınavdan eşit puan almış ve toplam 21 soruyu doğru cevaplamıştır.\nBuna göre Ece’nin bir sınavdan aldığı puan kaçtır?',
 30,[(10,'İkinci sınavdaki doğru sayısını vermiş.','dikkat'),(11,'Birinci sınavdaki doğru sayısını vermiş.','dikkat'),(21,'Toplam doğru sayısını puan sanmış.','dikkat'),(60,'İki sınavın puanını toplamış (30 + 30).','islem')],
 'Ece’nin bir sınavdan aldığı puan.','Birinci sınavdaki doğru sayısına d de; ikinci sınavdaki doğru sayısını toplam doğrudan yaz.',[PUAN],
 [A('Puanları yaz','Birinci: 4d − (25 − d) = 5d − 25. İkinci doğru 21 − d: 5(21 − d) − 2(d − 1) = 107 − 7d.','5d − 25 ve 107 − 7d'),A('Eşitle','İki puan eşit.','5d − 25 = 107 − 7d → d = 11'),A('Puanı bul','Birinci sınavda 11 doğru, 14 yanlış.','44 − 14 = 30'),A('Kontrol','İkinci: 10 doğru, 10 yanlış.','50 − 20 = 30 ✓')],
 'İki kuralda puanı doğru sayısı cinsinden yaz; toplam doğru koşuluyla tek bilinmeyene indir.')

# ---------- 0029 orta · turnuva puanı
assert [(a_,b_,13-a_-b_) for a_ in range(14) for b_ in range(14-a_) if a_==3*(13-a_-b_) and 3*a_+b_==23 and 13-a_-b_>=0]==[(6,5,2)]
assert 3*6==18 and 6+2==8
TBL=B('Puan sistemi','Her sonucun puanı, o sonucun sayısıyla çarpılıp toplanır; toplam maç = galibiyet + beraberlik + mağlubiyet. Örnek: 2 galibiyet, 1 beraberlik 3 − 1 − 0 puanlı sistemde 2·3 + 1·1 = 7 puandır')
S('0029','08','orta','Puan Sistemi','Galibiyet, beraberlik ve mağlubiyet puanlarıyla beraberlik sayısını bulur.','hikâyeli',3,'puan sistemi · galibiyet–beraberlik–mağlubiyet',
 'Bir turnuvada her maç sonunda galibiyet 3 puan, beraberlik 1 puan, mağlubiyet 0 puan getirmektedir. Bir takım bu turnuvada 13 maç oynamış ve 23 puan toplamıştır. Takımın galibiyet sayısı, mağlubiyet sayısının 3 katıdır.\nBuna göre bu takımın beraberlik sayısı kaçtır?',
 5,[(2,'Mağlubiyet sayısını vermiş.','dikkat'),(6,'Galibiyet sayısını vermiş.','dikkat'),(8,'Galibiyet ve mağlubiyet toplamını vermiş.','dikkat'),(18,'Galibiyetlerden gelen puanı (3 · 6) vermiş.','dikkat')],
 'Beraberlik sayısı.','Mağlubiyet sayısına m de; galibiyet ve beraberlik sayısını m cinsinden yaz ve puan toplamını kur.',[TBL],
 [A('Sayıları m ile yaz','Mağlubiyet m, galibiyet 3m, beraberlik 13 − 4m.','3·3m + (13 − 4m) = 23'),A('m’yi bul','Denklemi çöz.','5m + 13 = 23 → m = 2'),A('Beraberlik','13 − 4·2.','5 · kontrol: 18 + 5 = 23 ✓')],
 'Puan sisteminde her sonucun puanını kendi sayısıyla çarp; toplam maç ve toplam puan iki denklem verir.')

# ---------- 0030 kolay · terazi
k=60; assert 4*k+180==7*k and 180//(7-4)==60 and 180//2==90 and 180*(7-4)==540 and 180*4==720
TR2=B('Terazi dengesi','Denge durumunda iki kefenin ağırlığı eşittir. Örnek: bir kefede 1 kg’lık ağırlık, diğerinde 500 g’lık ağırlık ve bir kutu varsa kutu 500 g’dır')
S('0030','09','kolay','Terazi','Kefelerdeki özdeş nesnelerin dengesinden bir nesnenin ağırlığını bulur.','hikâyeli',2,'terazi · özdeş nesneler',
 'Özdeş yumurtalarla yapılan bir tartıda, terazinin bir kefesinde 4 yumurta ve 180 gramlık bir ağırlık, diğer kefesinde 7 yumurta bulunmaktadır. Terazi dengededir.\nBuna göre bir yumurta kaç gramdır?',
 60,[(90,'Yumurta farkını 3 yerine 2 alıp 180 ÷ 2 yapmış.','dikkat'),(180,'Verilen ağırlığı cevap sanmış.','dikkat'),(540,'180 ile yumurta farkı olan 3’ü çarpmış.','islem'),(720,'180 ile 4’ü çarpmış.','islem')],
 'Bir yumurtanın ağırlığı (gram).','İki kefedeki ortak kısmı sadeleştirmeyi dene.',[TR2],
 [A('Eşitliği yaz','Yumurta k gram.','4k + 180 = 7k'),A('Ortak yumurtaları at','Her iki yandan 4k çıkar.','180 = 3k'),A('k’yı bul','Böl.','k = 60 g')],
 'Dengede iki kefenin ağırlığı eşittir; ortak nesneleri iki yandan çıkar.')

# ---------- 0031 orta · en çok ürün
assert 4*27+3*42==234 and 300-234==66 and 66//27==2 and 4+3+2==9 and 66//42==1 and 4+3+1==8 and 300//27==11 and -(-66//27)==3 and 4+3+3==10 and 4+3==7
mx=max(a_+b_ for a_ in range(4,12) for b_ in range(3,8) if 27*a_+42*b_<=300); assert mx==9
S('0031','09','orta','En Az – En Çok','Bütçe ve en az alım koşuluyla alınabilecek en çok ürün sayısını bulur.','hikâyeli',3,'en çok – en az · bütçeyle alım',
 'Bir okul kantininde simit 27 TL, poğaça 42 TL’dir. Elinde 300 TL bulunan Selin, bu kantinden en az 4 simit ve en az 3 poğaça almak koşuluyla en çok kaç ürün alabilir?',
 9,[(7,'Yalnız zorunlu ürünleri (4 + 3) almış; artan parayla ürün almamış.','dikkat'),(8,'Artan parayla (66 TL) yalnız poğaça almış.','bilgi'),(10,'Artan 66 TL’yi 27’ye bölüp yukarı yuvarlamış (3 simit).','islem'),(11,'Bütün parayı simide verip (300 ÷ 27) zorunlu poğaçaları unutmuş.','dikkat')],
 'Alınabilecek en çok ürün sayısı.','Zorunlu alımı yaptıktan sonra elde kalan parayı nasıl harcarsan ürün sayısı artar?',[ENC],
 [A('Zorunlu alım','4 simit + 3 poğaça.','4·27 + 3·42 = 234 TL'),A('Artan para','300 − 234.','66 TL'),A('En ucuz ürün','Simitten 66 ÷ 27’nin tam kısmı.','2 simit (54 TL)'),A('Toplam','4 + 3 + 2.','9 ürün')],
 'Ürün sayısını en çok yapmak için zorunlu alımdan sonra artan parayı en ucuz ürüne ver.')

# ---------- 0032 orta · en büyük sayı en çok
assert 40-(1+2+3+4)==30 and 40-(2+3+4+5)==26 and 40-(0+1+2+3)==34 and 40-4==36 and 40-(1+2+3+5)==29
S('0032','09','orta','En Az – En Çok','Toplamı verilen farklı sayılardan en büyüğünün alabileceği en büyük değeri bulur.','düz',3,'en çok – en az · farklı pozitif tam sayılar',
 'Birbirinden farklı beş pozitif tam sayının toplamı 40’tır.\nBuna göre bu sayıların en büyüğü en çok kaçtır?',
 30,[(26,'Diğer dört sayıyı 2’den başlatmış (2 + 3 + 4 + 5).','dikkat'),(29,'Diğer sayıları 1, 2, 3, 5 almış; 4’ü atlamış.','dikkat'),(34,'Diğer dört sayıyı 0, 1, 2, 3 almış; 0 pozitif değildir.','dikkat'),(36,'“Farklı” koşulunu unutup diğer dört sayıyı 1 almış.','dikkat')],
 'En büyük sayının alabileceği en büyük değer.','En büyük sayı büyük olsun diye diğerlerinden ne beklersin? “Farklı” koşuluna dikkat et.',[ENC],
 [A('Diğer dört sayı','En küçük farklı pozitif tam sayılar.','1, 2, 3, 4 → toplam 10'),A('En büyük','Toplamdan çıkar.','40 − 10 = 30'),A('Kontrol','1 + 2 + 3 + 4 + 30 = 40 ve sayılar farklı pozitif tam sayı.','30')],
 'En büyüğü en çok yapmak için diğerleri en küçük farklı pozitif tam sayılar olur.')

# ---------- 0033 orta · geriye
x=12; s_=((4*x-6)//2)+7; assert s_==28 and 4*x-6==42 and 42//2==21
assert (28-7)*2+6==48 and 48/4==12 and ((21*2-6)/4)==9 and ((28+7)*2+6)/4==19
S('0033','10','orta','Geriye Çözme','Zincir işlemlerin sonucundan geriye giderek ilk sayıyı bulur.','düz',3,'geriye giderek çözme · dört işlem',
 'Bir sayı önce 4 ile çarpılıyor, çıkan sonuçtan 6 çıkarılıyor, elde edilen sayı 2’ye bölünüyor ve son olarak bölümün 7 fazlası alınıyor. Sonuç 28 bulunuyor.\nBuna göre ilk sayı kaçtır?',
 12,[(9,'Geri giderken 6’yı çıkarmış (eklemesi gerekirken): (21·2 − 6) ÷ 4.','dikkat'),(19,'Sonda eklenen 7’yi yeniden eklemiş: (35·2 + 6) ÷ 4.','dikkat'),(21,'Yalnız son işlemi geri almış (28 − 7).','dikkat'),(28,'Verilen sonucu ilk sayı sanmış.','dikkat')],
 'İlk sayı.','Sondan başa doğru her işlemin tersini ters sırada uygula.',[GER],
 [A('Son işlemi geri al','Bölümün 7 fazlası 28 ise bölüm.','28 − 7 = 21'),A('Bölmeyi geri al','2’ye bölünmüştü.','21 · 2 = 42'),A('Çıkarmayı geri al','6 çıkarılmıştı.','42 + 6 = 48'),A('Çarpmayı geri al','4 ile çarpılmıştı.','48 ÷ 4 = 12')],
 'Zincir işlemlerde sonuçtan başla; her işlemin tersini ters sırayla uygula.')

# ---------- 0034 zor · makine, yeni nesil
Af=lambda v:2*v-3; Bf=lambda v:3*v-4
xx=5; assert Af(Bf(Af(xx)))==31 and Bf(Af(Bf(xx)))==53 and Bf(xx)==11 and Af(Bf(xx))==19 and Af(xx)==7 and Bf(Af(xx))==17 and Bf(Af(Bf(7)))==89
assert [v for v in range(-50,100) if Af(Bf(Af(v)))==31]==[5]
S('0034','10','zor','Makine','İki makinenin zincirinde çıktıdan girdiyi bulup zinciri ters sırayla yeniden uygular.','yeni nesil',4,'geriye giderek çözme · makine zinciri',
 'Birinci makine girdiği sayıyı 2 ile çarpıp 3 çıkararak, ikinci makine ise girdiği sayıyı 3 ile çarpıp 4 çıkararak çıktı verir. Bir sayı sırasıyla birinci, ikinci ve tekrar birinci makineye girdiğinde çıktı 31 olmuştur.\nAynı sayı sırasıyla ikinci, birinci ve tekrar ikinci makineye girerse çıktı kaç olur?',
 53,[(5,'Yalnız girdiyi bulup durmuş.','dikkat'),(89,'Geri gitmeyi bir adım erken bırakıp girdiyi 7 sanmış: 3·7 − 4 = 17 → 2·17 − 3 = 31 → 3·31 − 4 = 89.','islem'),(19,'İkinci zincirde yalnız ilk iki makineyi uygulamış.','dikkat'),(31,'Verilen çıktıyı (ilk zincir) cevap sanmış.','dikkat')],
 'İkinci zincirin çıktısı.','Önce birinci zincirin sonundan geri giderek girdiyi bul; sonra yeni sırayla ileri doğru uygula.',[GER],
 [A('Geri git','Son makine 2v − 3 = 31.','v = 17'),A('Bir geri daha','İkinci makine 3u − 4 = 17.','u = 7'),A('Girdiyi bul','Birinci makine 2x − 3 = 7.','x = 5'),A('Yeni zincir','İkinci → birinci → ikinci.','3·5 − 4 = 11 → 2·11 − 3 = 19 → 3·19 − 4 = 53')],
 'Çıktıdan geriye giderek girdiyi bul; sonra yeni sıralamayı baştan ileri doğru uygula.')

bitir(P,'sayiprobiki',UK)
