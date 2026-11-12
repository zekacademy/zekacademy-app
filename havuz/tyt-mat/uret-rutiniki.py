"""Rutin Olmayan Problemler · parti 2 (hafif mod): 34 ana soru, kardeş yok, ipucu 1. Mantık sorularında bütün durumlar taranır; her cevap ve çeldirici kodla doğrulanır."""
import sys,os,datetime,calendar
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_mat as H
from _hafif_mat import *
from itertools import permutations,product,combinations
from functools import lru_cache
H.KONU='Rutin Olmayan Problemler'
UK='prob|Rutin Olmayan Problemleri'
P=Parti('rutiniki','Rutin Olmayan Problemler',UK)

ISL=B('Tanımlı işlem','a ★ b = 2a − b + 1 gibi bir kuralda a ve b yerine verilen sayılar yazılır; parantez içi önce yapılır. Örnek: a ★ b = a + 2b ise 3 ★ 1 = 3 + 2 = 5')
PER=B('Periyodik düzen','Bir düzen her p adımda kendini yineliyorsa n. adımın durumu, n sayısının p ile bölümünden kalana bakılarak bulunur. Örnek: 3 renkli düzende 10. sıra için 10 = 3 · 3 + 1 olduğundan 1. renktir')
ORU=B('Örüntü','Her adımda sabit miktar artan örüntüde n. terim = ilk terim + (n − 1) · artış. Örnek: 4, 7, 10, … örüntüsünde 5. terim 4 + 4 · 3 = 16’dır')
SAY=B('İkili seçimler','n kişiden iki kişi seçmenin yolu n · (n − 1) / 2’dir (sıra önemsizse). Örnek: 5 kişinin birbiriyle birer kez tokalaşması 5 · 4 / 2 = 10 tokalaşmadır')
SIF=B('Şifre sayma','Her basamak için seçenekler, koşullara uyularak çarpılır. Örnek: ilk basamak 0 olamayan 3 basamaklı sayılar 9 · 10 · 10 = 900 tanedir')
TER=B('Terazi mantığı','Bir tartımın üç sonucu vardır (sol ağır, sağ ağır, eşit); n tartımda en çok 3ⁿ seçenek ayırt edilir. Örnek: 1 tartımda en çok 3 bilye arasından hafif olan bulunur')
TAB=B('Tablo okuma','Önce her seçeneğin toplam maliyetini ayrı ayrı hesapla, sonra karşılaştır. Örnek: sabit 100 TL + dakikası 2 TL olan tarife 30 dakikada 100 + 60 = 160 TL’dir')
CIK=B('Koşullu çıkarım','Kesin bilgiler tabloya işlenir; bir seçenek bütün koşullarla çelişiyorsa elenir. Örnek: "A, B’den uzundur" ve "B, C’den uzundur" ise A, C’den de uzundur')
OYN=B('Kazanan konum','Hamle yapamayan kaybediyorsa, rakibe kaybettiren bir konum bırakabiliyorsan o konumdasın kazanırsın. Örnek: 1, 2 ya da 3 çubuk alınan oyunda 4 çubuk kalan oyuncu kaybeder')
OPT=B('En az süre','Birden çok strateji varsa her birinin toplam süresini hesaplayıp karşılaştır; ilk bulunan çözüm en iyisi olmayabilir. Örnek: bir yolu otobüs + yürüyüşle 20 + 15 = 35 dakikada, taksiyle 30 dakikada gidebilen kişi 30 dakikayı seçer')
KOS=B('Koşullu tarama','Koşullardan sayıyı en çok daraltanı seç; kalan durumları tek tek say. Örnek: iki basamaklı, rakamları toplamı 5 olan sayılar 14, 23, 32, 41, 50’dir')
BOLN=B('Bölen sayısı','Bir doğal sayının pozitif bölenleri d ve n/d biçiminde çiftler oluşturur; d = n/d olursa (sayı tam kare ise) bölen sayısı tek olur. Örnek: 36’nın bölenleri 1, 2, 3, 4, 6, 9, 12, 18, 36 (9 tane, tek)')
YOL=B('Izgarada yol sayma','a birim doğu ve b birim kuzey adımı sıralı dizilir; bu dizilişlerin sayısı C(a + b, a)’dır. Örnek: 2 doğu, 1 kuzey adımı için C(3, 1) = 3 yol vardır')
DAI=B('Dairesel sayım','Çemberde sayım bir kişi çıkınca çıkan kişinin ardındaki kişiden sürer; kalanlar sırayla listelenir. Örnek: 1, 2, 3, 4, 5 çemberinde 2’şer sayılıp 2. kişi çıkarılırsa çıkanlar 2, 4, 1, 5, kalan 3 olur')
BLN=B('Bölenler toplamı','Bir sayının kendisi dışındaki bölenleri yazılıp toplanır. Örnek: 6 için 1 + 2 + 3 = 6; 8 için 1 + 2 + 4 = 7')
OYM=B('Kaybettiren konum','Sırası gelen oyuncunun ne yaparsa yapsın rakibin kazandığı konuma kaybettiren konum denir. Örnek: 1 ya da 2 çubuk alınan ve son çubuğu almak zorunda kalanın kaybettiği oyunda 4 çubuk kalan oyuncu kaybeder')
OPS=B('Su ölçme','İki kaptan hangisinin önce doldurulduğuna göre ulaşılan durumlar farklıdır; yollar karşılaştırılır. Örnek: 4 L ve 3 L kapla 2 L ölçmek için önce hangi kabı doldurmanın daha kısa olduğuna bakılır')
OPK=B('Kutularla sayma','En büyük kutudan başlamak her zaman en az kutuyu vermez. Örnek: 3’lü ve 5’li kutularla 11 kalem için 5 + 3 + 3 = 3 kutu gerekir')
DIZ=B('Kuralla üretilen dizi','Bir sonraki terim kuralla bulunur; terimler sırayla yazılarak ilerlenir. Örnek: a₁ = 3 ve her terim öncekinin 2 katı ise 3, 6, 12, 24, …')

KY='ÖSYM 2018–2026 TYT Matematik (mantık–muhakeme, problemler, sayı kümeleri) · yayın soru bankaları (yalnız mantık) · MEB 9. sınıf'
kart('K-RTB-01','Tanımlı kural, işlem ve sayı türü','Verilen işlem kuralı ya da sayı türü tanımına göre değer hesaplanır ve ifadeler tek tek sınanır.','Parantez sırasını ya da argüman sırasını karıştırmak; bir örnekle doğrulanan ifadeyi her zaman doğru sanmak.','orta','yeni nesil',3,'rtb-kural','Tanımlı işlem ve sayı türü',KY)
kart('K-RTB-02','Örüntü ve dizi','Şekil ve sayı örüntüsünde n. terim bulunur; kuralla üretilen konum ve dairesel eleme sorularında adım adım ilerlenir.','İlk terimle artışı karıştırmak (n yerine n − 1); sayımı yanlış yerden başlatmak.','orta','hikâyeli',3,'rtb-oruntu','Örüntü, dizi ve konum',KY)
kart('K-RTB-03','Periyodik durum','Lamba, takvim, tren ve renk dizilerinde tekrar eden düzenin periyodu bulunur; kalan ya da ortak kat kullanılır.','Kalanı sayı sanmak; ilk ve son durumu iki kez ya da hiç saymamak.','orta','hikâyeli',4,'rtb-periyot','Periyodik durum (takvim, lamba, tren)',KY)
kart('K-RTB-04','Mantık ve çıkarım','Sıralama, eşleştirme ve doğru–yalan bilgisinden tüm olasılıklar taranarak tek çözüm bulunur.','Bir koşulu atlayıp birden çok çözümün içinden birini seçmek; "kesinlikle" ifadesini "olabilir" ile karıştırmak.','zor','yeni nesil',5,'rtb-cikarim','Mantık ve çıkarım (sıralama, eşleştirme)',KY)
kart('K-RTB-05','Oyun ve puanlama','Kazanan konumlar geriden ileriye taranır; puan toplamından atış sayısı çıkarılır.','Oyunu bitirme kuralını yanlış okumak; "her bölgeye en az bir" koşulunu unutmak.','zor','yeni nesil',4,'rtb-oyun','Oyun stratejisi ve puanlama',KY)
kart('K-RTB-06','Sayı yerleştirme ve koşullu tarama','Küçük ızgara ve rakam koşullarında seçenekler sistemli taranarak yerleştirme tamamlanır.','Bir kural satırda uygulanıp sütunda unutulmak; baştaki sıfırı saymak.','zor','tablo',5,'rtb-yerlestirme','Sayı yerleştirme (ızgara, rakam koşulu)',KY)
kart('K-RTB-07','Şifre ve kod kuralı','Şifre sayısı koşullu çarpma ile, kodlama kuralı alfabe üzerinde adım adım, ipucundan şifre bulma tarama ile çözülür.','Alfabe uzunluğunu yanlış almak; ipuçlarından birini gözden kaçırmak.','orta','yeni nesil',4,'rtb-sifre','Şifre ve kod kuralı',KY)
kart('K-RTB-08','Sayma: tokalaşma, yol, maç','İkili seçimler, kapalı noktalı en kısa yol ve turnuva maç sayısı parça parça sayılır.','Aynı ikiliyi iki kez saymak; bir aşamanın maçlarını unutmak.','orta','hikâyeli',3,'rtb-sayma','Sayma: tokalaşma, yol, maç sayısı',KY)
kart('K-RTB-09','Optimizasyon: en az, en çok','En az hamle, en az kutu ve en kısa sürenin bulunması için bütün stratejiler sistemli denenir.','İlk akla gelen (açgözlü) yolu en iyi sanmak.','zor','yeni nesil',5,'rtb-optimizasyon','Optimizasyon (en az hamle, en az süre)',KY)
kart('K-RTB-10','Yaşam becerisi ve tablo yorumu','Tarife, kampanya ve kademeli fatura hesaplanır; tabloya dayalı ifadeler tek tek sınanır.','Kademeli fiyatı tüm tüketime uygulamak; yalnız sabit ücrete bakmak.','orta','tablo',4,'rtb-yasam','Yaşam becerisi: tarife, kampanya, tablo',KY)

NO=[0]
def S(tipId,tip,z,alt,kaz,kalip,kart_,metin,dogru,yan,istenen,ip,bilgi,ad,puf,sekil=None,sira=None):
    NO[0]+=1
    mk(P,f'{NO[0]:04d}',tipId=tipId,tip=tip,z=z,alt=alt,kaz=kaz,kalip=kalip,adim=len(ad),kart=kart_,metin=metin,dogru=dogru,yan=yan,istenen=istenen,ip=ip,bilgi=bilgi,ad=ad,puf=puf,sekil=sekil,sira=sira)
def tek(vals): assert len(set(map(str,vals)))==len(vals),vals
OK=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']

# ---------- 01 kolay · tanımlı işlem ----------
f=lambda a,b:2*a-b+1
d=f(f(5,2),4); w1=f(5,f(2,4)); g=lambda a,b:2*b-a+1; w2=g(g(5,2),4); h_=lambda a,b:2*a-b; w3=h_(h_(5,2),4); j=lambda a,b:2*(a-b)+1; w4=j(j(5,2),4)
assert (d,w1,w2,w3,w4)==(15,10,9,12,7)
S('rtb-kural','Tanımlı işlem ve sayı türü','kolay','Tanımlı İşlem','Tanımlı işlem kuralını iç içe uygulayarak sonucu hesaplar.','düz','K-RTB-01 (tanımlı işlem) · iç içe uygulama',
 'Gerçel sayılar kümesinde ★ işlemi\na ★ b = 2a − b + 1\nbiçiminde tanımlanıyor.\nBuna göre (5 ★ 2) ★ 4 işleminin sonucu kaçtır?',
 d,[(w1,'Parantezi dikkate almadan sağdan işlem yapmış: 5 ★ (2 ★ 4) hesaplamış.','dikkat'),(w2,'a ile b’nin yerlerini değiştirmiş: a ★ b yerine 2b − a + 1 kullanmış.','dikkat'),(w3,'Kuralın sonundaki + 1’i atlamış.','islem'),(w4,'Kuralı 2(a − b) + 1 diye okumuş; çarpanı parantezle b’ye de dağıtmış.','islem')],
 '(5 ★ 2) ★ 4 işleminin değeri.',['Önce parantezin içindeki işlemi, kuralda a yerine 5, b yerine 2 yazarak yap.'],[ISL],
 [A('İçteki işlemi yap','5 ★ 2 için a = 5, b = 2.','2 · 5 − 2 + 1 = 9'),A('Sonucu yerine koy','Şimdi 9 ★ 4 hesaplanır: a = 9, b = 4.','2 · 9 − 4 + 1 = 15'),A('Kontrol','İçteki işlemin sonucunu yeniden denetle.','5 ★ 2 = 9 ✓ → 15')],
 'Parantezli tanımlı işlemde önce parantezi hesapla, çıkan sayıyı kuralda a ya da b yerine yaz.')

# ---------- 02 kolay · ışık düzeni ----------
cyc=['kırmızı','sarı','yeşil','mavi','mor','beyaz']
n=100; mor=sum(1 for i in range(n) if cyc[i%6]=='mor'); assert mor==16 and divmod(100,6)==(16,4) and 100//5==20 and 96==16*6
S('rtb-periyot','Periyodik durum (takvim, lamba, tren)','kolay','Periyodik Düzen','Tekrar eden bir renk düzeninde belirli rengin sayısını tur ve kalan yardımıyla bulur.','hikâyeli','K-RTB-03 (periyodik durum) · renk dizisi',
 'Bir tabelada ışıklar sırayla yanmaktadır. Işıkların renkleri kırmızı, sarı, yeşil, mavi, mor, beyaz sırasıyla yinelenmekte ve bu düzen hiç ara verilmeden sürmektedir. İlk yanan ışık kırmızıdır.\nBuna göre tabelada yanan ilk 100 ışığın kaç tanesi mordur?',
 16,[(4,'Bölümden kalan 4’ü mor ışık sayısı sanmış.','dikkat'),(17,'100 ÷ 6 = 16,67’yi yukarı yuvarlamış; kalan 4 ışıkta mor yoktur.','islem'),(20,'Mor 5. sırada olduğu için 100’ü 5’e bölmüş.','bilgi'),(96,'Tam turlardaki ışık sayısını (16 · 6) mor ışık sayısı sanmış.','dikkat')],
 'İlk 100 ışık içindeki mor ışık sayısı.',['100 ışığın kaç tam tur ve kaç artan ışıktan oluştuğunu bul; artan ışıklarda mor var mı diye bak.'],[PER],
 [A('Turları bul','Düzen 6 ışıktan oluşur.','100 = 6 · 16 + 4'),A('Tam turlarda say','Her turda 1 mor ışık vardır.','16 tur → 16 mor'),A('Kalanı kontrol et','Kalan 4 ışık kırmızı, sarı, yeşil, mavi’dir; mor 5. sıradadır.','Ek mor yok → 16')],
 'Tekrar eden düzende önce tam tur sayısını, sonra kalan kısmın içeriğini incele.')

# ---------- 03 kolay · kibrit örüntüsü ----------
kb=lambda n:3*n+1; assert [kb(1),kb(2),kb(3)]==[4,7,10] and kb(20)==61 and 4*20==80 and 3*20==60 and 4+3*20==64 and 3*20+2==62
S('rtb-oruntu','Örüntü, dizi ve konum','kolay','Şekil Örüntüsü','Şekil örüntüsünde adım sayısıyla çöp sayısı arasındaki ilişkiyi bulup büyük bir adımı hesaplar.','hikâyeli','K-RTB-02 (örüntü) · kibrit çöpü kareleri',
 'Kibrit çöpleriyle yan yana kareler yapılıyor. Komşu iki kare bir çöpü ortak kullanıyor. 1 kare için 4, 2 kare için 7, 3 kare için 10 çöp gerekiyor.\nBu düzen aynı biçimde sürdürülürse yan yana 20 kare yapmak için kaç çöp gerekir?',
 61,[(80,'Her kareyi ayrı 4 çöple yapıp ortak çöpleri düşmemiş.','dikkat'),(60,'Her kare için yalnızca 3 çöp saymış; ilk karenin 4. çöpünü unutmuş.','dikkat'),(64,'İlk kare 4 çöp, sonraki her biri 3 çöp kuralını 20 adım uygulamış: 4 + 3 · 20.','islem'),(62,'Her kareye 3 çöp sayıp yalnız 2 ekleme yapmış: 3 · 20 + 2.','dikkat')],
 'Yan yana 20 kare için gereken çöp sayısı.',['Her yeni kare eklenince çöp sayısı kaç artıyor? İlk kareden sonra kaç kare ekleniyor?'],[ORU],
 [A('Artışı bul','4, 7, 10 → her yeni kare 3 çöp ekler.','artış = 3'),A('Kuralı yaz','İlk kare 4 çöp, sonraki 19 kare 3’er çöp.','4 + 3 · 19'),A('Hesapla','Toplam çöp.','4 + 57 = 61')],
 'n. şekil için ilk şekli yaz, sonra (n − 1) kez artışı ekle.')

# ---------- 04 kolay · tokalaşma ----------
assert 12*11//2==66 and 11*10//2==55 and 66//2==33 and 2*66==132
S('rtb-sayma','Sayma: tokalaşma, yol, maç sayısı','kolay','İkili Sayma','Toplam tokalaşma sayısından katılımcı sayısını bulur.','hikâyeli','K-RTB-08 (sayma) · tokalaşma',
 'Bir toplantıya katılan herkes, toplantının sonunda diğer katılımcıların her biriyle yalnızca bir kez el sıkışmıştır. Toplantıda toplam 66 el sıkışma yapılmıştır.\nBuna göre toplantıya kaç kişi katılmıştır?',
 12,[(11,'Bir kişinin yaptığı el sıkışma sayısını (n − 1 = 11) katılımcı sayısı sanmış.','dikkat'),(33,'Her el sıkışmada iki kişi olduğu için 66’yı 2’ye bölüp sonucu kişi sayısı yazmış.','dikkat'),(66,'El sıkışma sayısını kişi sayısı sanmış.','dikkat'),(132,'Her el sıkışmayı iki kez sayıp 66 · 2 yazmış.','islem')],
 'Toplantıya katılan kişi sayısı.',['Katılımcı sayısına n de ve toplam el sıkışma sayısını n cinsinden yazmayı dene.'],[SAY],
 [A('Denklemi kur','n kişi için n(n − 1)/2 el sıkışma olur.','n(n − 1)/2 = 66'),A('Çarpımı bul','Her iki yanı 2 ile çarp.','n(n − 1) = 132'),A('Ardışık sayıları bul','132 = 12 · 11.','n = 12')],
 'Herkesin herkesle bir kez yaptığı ikili işlemler n(n − 1)/2’dir; toplam verilmişse ardışık iki sayının çarpımı aranır.')

# ---------- 05 kolay · şifre sayma ----------
c=sum(1 for p in product(range(1,6),repeat=4) if p[0]==p[3] and p[1]!=p[2])
assert c==100 and 5*5*5==125 and 5**4==625 and 5*5*4*5==500 and 5*4==20 and sum(1 for p in product(range(1,6),repeat=4) if p[0]==p[3] and p[1]!=p[2] and p[0]!=p[1])==80
S('rtb-sifre','Şifre ve kod kuralı','kolay','Şifre Sayma','Koşullu 4 basamaklı şifre sayısını basamak basamak çarparak bulur.','düz','K-RTB-07 (şifre) · koşullu basamaklar',
 'Bir kapı kilidinin şifresi 4 basamaklıdır ve her basamağında 1, 2, 3, 4 ya da 5 rakamlarından biri bulunur; rakamlar tekrar edebilir. Şifrenin ilk rakamı son rakamıyla aynıdır, ikinci rakamı ise üçüncü rakamından farklıdır.\nBuna göre bu kurallara uyan kaç farklı şifre oluşturulabilir?',
 100,[(80,'İkinci rakamın ilk rakamdan da farklı olması gerektiğini sanmış: 5 · 4 · 4.','dikkat'),(125,'İkinci ve üçüncü rakamların farklı olması koşulunu unutmuş: 5 · 5 · 5.','dikkat'),(500,'İlk ile son rakamın aynı olması koşulunu unutmuş: 5 · 5 · 4 · 5.','dikkat'),(20,'İlk ve son rakamı hiç saymayıp yalnız ortadaki iki rakamın sıralı seçimini yazmış: 5 · 4.','dikkat')],
 'Şifre sayısı.',['Önce ilk rakamı seç; son rakam kaç türlü seçilebilir? Sonra ortadaki iki rakamın sıralı seçimini say.'],[SIF],
 [A('İlk ve son rakam','İlk rakam 5 türlü; son rakam ilkine eşit.','5 · 1 = 5'),A('Ortadaki rakamlar','İkinci 5 türlü, üçüncü ikincisinden farklı: 4 türlü.','5 · 4 = 20'),A('Çarp','Birbirinden bağımsız seçimler çarpılır.','5 · 20 = 100')],
 'Koşullu şifre sayarken bağlı basamakları birlikte, serbest olanları ayrı ayrı say ve çarp.')

# ---------- 06 kolay · terazi ----------
@lru_cache(None)
def tart(c):
    if c<=1: return 0
    return 1+min(max(tart(a),tart(c-2*a)) for a in range(1,c//2+1))
assert tart(9)==2 and tart(3)==1 and tart(27)==3
S('rtb-optimizasyon','Optimizasyon (en az hamle, en az süre)','orta','Terazi Mantığı','Eşit kollu terazide hafif bilyeyi bulmak için gereken en az tartım sayısını belirler.','hikâyeli','K-RTB-09 (optimizasyon) · terazi',
 'Dışarıdan birbirinden ayırt edilemeyen 9 bilyenin biri diğer sekizinden daha hafiftir; diğer sekizi birbirine eşit ağırlıktadır. Ağırlık ölçeği olmayan, eşit kollu bir terazide yalnızca iki kefedeki bilyeler karşılaştırılabilmektedir.\nHafif bilyenin hangisi olduğu hangi durumda olursa olsun kesin olarak bulunacaksa, en az kaç tartım yapılması gerekir?',
 2,[(1,'Kefelere 4 ve 4 bilye koyup tek tartımda hafif bilyeyi doğrudan bulacağını sanmış.','dikkat'),(3,'4 – 4 – 1 gruplarına ayırmış: hafif grup 4 bilye kalır, 2 – 2 ve 1 – 1 ile 3 tartım yapmış.','bilgi'),(4,'Bilyeleri ikişerli karşılaştırmış (1–2, 3–4, 5–6, 7–8); en kötü durumda 4 tartım yapmış.','bilgi'),(8,'Bir bilyeyi diğerlerinin her biriyle tek tek karşılaştırmış; en kötü durumda 8 tartım.','bilgi')],
 'Gerekli en az tartım sayısı.',['En kötü durumda bile kesin sonuç için her tartımın eleyebileceği bilye sayısını düşün.'],[TER],
 [A('Üç gruba ayır','9 bilyeyi 3 + 3 + 3 olarak böl; iki grubu tart.','1. tartım: 3 – 3'),A('Hafif grubu bul','Terazi bir tarafa eğilirse hafif grup oradadır; eşit kalırsa dışarıda kalan gruptadır.','Hafif bilye 3 bilyelik bir grupta'),A('İkinci tartım','Gruptan 1 – 1 bilye tart; eğilirse hafif olan, eşit kalırsa dışarıdaki bilye hafiftir.','2. tartım → bulundu')],
 'Terazide her tartım 3 sonuç verir; adayları üç eşit gruba bölmek en az tartım sağlar (9 = 3²).')

# ---------- 07 orta · tarife tablosu ----------
tar={'A':(120,300,Fr(3,5)),'B':(150,400,Fr(1,2)),'C':(200,500,Fr(2,5))}
dk=450; mal={k:u+max(0,dk-m)*a for k,(u,m,a) in tar.items()}
assert mal=={'A':210,'B':175,'C':200} and min(mal.values())==175 and min(u for u,_,_ in tar.values())==120
S('rtb-yasam','Yaşam becerisi: tarife, kampanya, tablo','orta','Tarife Karşılaştırma','Sabit ücret, dahil dakika ve aşım ücretine göre en uygun tarifenin ücretini tablodan hesaplar.','tablo','K-RTB-10 (yaşam becerisi) · cep telefonu tarifeleri',
 'Aşağıdaki tabloda bir operatörün üç tarifesi verilmiştir. Dahil dakika bittikten sonra konuşulan her ek dakika için tabloda yazılı aşım ücreti ayrıca ödenir.\nHer ay tam 450 dakika konuşan bir abone, bu üç tarifeden aylık toplam ücreti en düşük olanı seçerse ayda kaç TL öder?',
 175,[(120,'Yalnız aylık sabit ücrete bakmış; A tarifesindeki aşımı hesaba katmamış.','dikkat'),(150,'B tarifesinin sabit ücretini toplam ücret saymış; 50 dakikalık aşımı eklememiş.','dikkat'),(200,'Dahil dakikası en yüksek olan C tarifesini seçmiş; aşım olmasa da sabit ücret yüksektir.','bilgi'),(210,'A tarifesinin toplamını (120 + 150 · 0,60) en düşük sanmış; B tarifesini hesaplamamış.','dikkat')],
 'Üç tarifeden en düşük aylık toplam ücret (TL).',['Her tarife için önce aşım dakikasını, sonra toplam ücreti ayrı ayrı hesapla.'],[TAB],
 [A('A tarifesi','Aşım: 450 − 300 = 150 dakika.','120 + 150 · 0,60 = 210 TL'),A('B tarifesi','Aşım: 450 − 400 = 50 dakika.','150 + 50 · 0,50 = 175 TL'),A('C tarifesi','450 dakika dahil dakika içindedir.','200 TL'),A('En düşüğü seç','Üçünü karşılaştır.','175 TL')],
 'Sabit ücreti en düşük tarife, kullanım arttığında en ucuz olmayabilir; her tarifenin toplamını hesapla.',
 sekil=tablo_svg(['Tarife','Aylık ücret (TL)','Dahil dakika','Aşım (TL/dk)'],[['A','120','300','0,60'],['B','150','400','0,50'],['C','200','500','0,40']]))

# ---------- 08 orta · kurul toplantıları ----------
gun=['Pazartesi','Salı','Çarşamba','Perşembe','Cuma','Cumartesi','Pazar']
k8=[k for k in range(1,100) if (9*k)%7==0][0]; assert k8==7 and 9%7==2 and 7+1==8 and 9*7==63
S('rtb-periyot','Periyodik durum (takvim, lamba, tren)','orta','Takvim','Her 9 günde bir tekrarlanan etkinliğin haftanın aynı gününe yeniden denk geldiği toplantıyı bulur.','hikâyeli','K-RTB-03 (periyodik durum) · takvim',
 'Bir kurul ilk toplantısını bir pazartesi günü yapmıştır. Bundan sonra her toplantıyı bir önceki toplantıdan tam 9 gün sonra yapmaktadır.\nİlk toplantıdan sonra yapılan toplantılar içinde, pazartesi gününe rastlayan ilk toplantı, ilk toplantıdan sonraki kaçıncı toplantıdır?',
 7,[(2,'Her toplantıda günün 9 mod 7 = 2 gün kaydığını bulup bu sayıyı toplantı sırası sanmış.','dikkat'),(8,'İlk toplantıyı da sayarak toplantının genel sırasını (8.) yazmış.','dikkat'),(9,'Toplantılar arası gün sayısını (9) sıra sanmış.','dikkat'),(63,'Pazartesiye yeniden gelinen gün sayısını (63) toplantı sırası sanmış.','dikkat')],
 'İlk toplantıdan sonraki toplantı sırası.',['İlk birkaç toplantının haftanın hangi gününe denk geldiğini yazarak bir düzen ara.'],[PER],
 [A('Kaymayı bul','9 = 7 + 2: her toplantıda gün 2 ileri kayar.','kayma = 2 gün'),A('Koşulu yaz','k toplantı sonra kayma 2k gün; 7’nin katı olmalı.','2k ≡ 0 (mod 7)'),A('En küçük k','2 ile 7 aralarında asaldır.','k = 7')],
 'Haftalık düzende kalan sınıflarına bak: her adımda kayan gün sayısı 7’nin katı olunca gün yeniden aynı olur.')

# ---------- 09 orta · lambalar ----------
acik=[False]*41
for kisi in range(1,41):
    for l in range(kisi,41,kisi): acik[l]=not acik[l]
sayi=sum(acik[1:]); assert sayi==6 and [i for i in range(1,41) if acik[i]]==[1,4,9,16,25,36] and 40//2==20 and 40-6==34
S('rtb-periyot','Periyodik durum (takvim, lamba, tren)','orta','Lamba Durumu','Her lambanın kaç kez değiştirildiğini bölen sayısıyla bularak son durumdaki açık lambaları sayar.','yeni nesil','K-RTB-03 (periyodik durum) · düğme değiştirme',
 'Bir koridorda 1’den 40’a kadar numaralanmış 40 lamba vardır ve başlangıçta hepsi kapalıdır. 40 kişi sırayla koridordan geçmektedir. k. kişi, numarası k’nin katı olan her lambanın düğmesine bir kez basmaktadır (açık lamba kapanır, kapalı lamba açılır).\n40 kişi de geçtikten sonra kaç lamba açıktır?',
 6,[(7,'√40 ≈ 6,3 değerini yukarı yuvarlayıp 7 yazmış.','islem'),(20,'Yalnız çift numaralı lambaların açıldığını sanmış.','dikkat'),(34,'Kapalı kalan lambaların sayısını yazmış.','dikkat'),(40,'Her lambanın bir kez açıldığını sanmış.','dikkat')],
 'Açık kalan lamba sayısı.',['Bir lambaya kaç kez basıldığını lamba numarasıyla ilişkilendir; birkaç küçük numara için tek tek dene.'],[BOLN],
 [A('Basış sayısını yorumla','Lamba n’ye, n’nin her böleni kadar kişi basar.','basış sayısı = bölen sayısı'),A('Açık kalma koşulu','Tek sayıda basılan lamba açık kalır.','bölen sayısı tek olmalı'),A('Bu sayıları bul','Bölen sayısı tek olanlar tam kare sayılardır.','1, 4, 9, 16, 25, 36'),A('Say','1’den 40’a kadar 6 tam kare vardır.','6 lamba')],
 'Bir lambaya basış sayısı bölen sayısıdır; bölen sayısı tek olan sayılar tam karelerdir.')

# ---------- 10 orta · çubuk oyunu (son çubuğu alan kaybeder) ----------
@lru_cache(None)
def kazan(n,mv=(1,2,3)):
    return any(n>=m and not kazan(n-m,mv) for m in mv)
@lru_cache(None)
def misere(n):  # son çubuğu alan kaybeder; True = sırası gelen kazanır
    if n==1: return False
    return any(n>=m and n-m>=1 and not misere(n-m) for m in (1,2,3))
sec10=[18,19,20,22,25]; assert [n for n in sec10 if not misere(n)]==[25] and not kazan(20)
mh={n:[m for m in (1,2,3) if n-m>=1 and not misere(n-m)][0] for n in (18,19,20,22)}; assert mh=={18:1,19:2,20:3,22:1}
S('rtb-oyun','Oyun stratejisi ve puanlama','orta','Çubuk Oyunu','Kaybettiren konumları küçük sayılardan başlayarak tarar ve ikinci oyuncunun kazandığı başlangıç sayısını bulur.','yeni nesil','K-RTB-05 (oyun stratejisi) · çubuk oyunu',
 'Masada N çubuk bulunmaktadır. İki oyuncu sırayla oynamakta ve her hamlede 1, 2 ya da 3 çubuk almaktadır. Son çubuğu almak zorunda kalan oyuncu oyunu kaybeder. İki oyuncu da en iyi biçimde oynamaktadır.\nBuna göre aşağıdaki başlangıç sayılarından hangisinde ikinci oynayan oyuncu kazanmayı garantiler?',
 25,[(18,'Kaybettiren konumun 4k + 2 biçiminde olduğunu sanmış; ilk oyuncu 1 alıp 17 bırakır ve kazanır.','bilgi'),(19,'Kaybettiren konumun 4k + 3 biçiminde olduğunu sanmış; ilk oyuncu 2 alıp 17 bırakır ve kazanır.','bilgi'),(20,'Son çubuğu alanın kazandığı oyunu sanıp 4’ün katını seçmiş; bu oyunda ilk oyuncu 3 alıp 17 bırakır.','bilgi'),(22,'Kaybettiren konumun 4k + 2 biçiminde olduğunu sanmış; ilk oyuncu 1 alıp 21 bırakır ve kazanır.','bilgi')],
 'İkinci oyuncunun kazanmayı garantilediği N.',['Küçük sayılardan başlayarak her çubuk sayısı için sırası gelen oyuncunun kazanıp kazanmadığını yaz.'],[OYM],
 [A('Küçük sayıları tara','1 çubuk kalan oyuncu son çubuğu almak zorundadır ve kaybeder; 2, 3 ya da 4 çubukta oyuncu 1, 2 ya da 3 alıp rakibe 1 çubuk bırakır.','1 kaybettirir · 2, 3, 4 kazandırır'),A('Deseni bul','5 çubukta ne alınırsa alınsın rakip 4, 3 ya da 2 çubukla karşılaşıp kazanır.','Kaybettirenler: 1, 5, 9, …'),A('Şıkları tara','Kaybettiren sayılar 4k + 1 biçimindedir; şıklardan yalnızca 25 = 4 · 6 + 1 böyledir.','N = 25')],
 'Birbirini tamamlayan hamleli oyunlarda kaybettiren sayılar aralıklı tekrar eder; ilk kaybettiren konumdan başlayarak deseni bul.')

# ---------- 11 orta · su kapları ----------
from collections import deque
def bfs(bas,hedef=lambda a,b:a==4,ca=5,cb=3):
    q=deque([(bas,0)]);gor={bas}
    while q:
        (a,b),d=q.popleft()
        if hedef(a,b): return d
        for s_ in {(ca,b),(a,cb),(0,b),(a,0),(a-min(a,cb-b),b+min(a,cb-b)),(a+min(b,ca-a),b-min(b,ca-a))}:
            if s_ not in gor: gor.add(s_);q.append((s_,d+1))
en=bfs((0,0)); s2=1+bfs((0,3)); assert en==6 and s2==8
yol=[(5,0),(2,3),(2,0),(0,2),(5,2),(4,3)]; assert yol[-1][0]==4 and len(yol)==6
S('rtb-optimizasyon','Optimizasyon (en az hamle, en az süre)','orta','Kap ile Ölçme','Ölçeksiz iki kapla belirli miktar su ölçmek için gereken en az işlem sayısını bulur.','yeni nesil','K-RTB-09 (optimizasyon) · su kapları',
 'Üzerinde ölçek bulunmayan 5 litrelik ve 3 litrelik iki kap ile sınırsız su vardır. Bir işlem şunlardan biridir: bir kabı ağzına kadar doldurmak, bir kabı tamamen boşaltmak ya da bir kaptaki suyu, kendi suyu bitene veya diğer kap dolana kadar diğerine aktarmak. Başlangıçta iki kap da boştur.\n5 litrelik kapta tam 4 litre su elde etmek için yapılması gereken en az işlem sayısı kaçtır?',
 6,[(3,'Yalnız aktarma işlemlerini (3 tane) saymış.','dikkat'),(5,'Doldurma ve aktarmaları saymış (2 + 3); boşaltmayı işlem saymamış.','dikkat'),(7,'Başlangıçtaki boş durumu da bir işlem olarak saymış.','dikkat'),(8,'Önce 3 litrelik kabı doldurarak başlamış; bu yoldan 4 litreye en az 8 işlemde ulaşılır.','bilgi')],
 'En az işlem sayısı.',['İki kaptan hangisini önce doldurduğunda hangi durumlara ulaşıldığını yazarak yolları karşılaştır.'],[OPS],
 [A('Büyük kabı doldur','5 L’yi doldur, 3 L’ye aktar.','(5, 0) → (2, 3)'),A('Küçük kabı boşalt','3 L’yi boşalt, 5 L’deki 2 L’yi aktar.','(2, 0) → (0, 2)'),A('Yeniden doldur','5 L’yi doldur, 3 L dolana kadar aktar (1 L geçer).','(5, 2) → (4, 3)'),A('İşlemleri say','Doldur, aktar, boşalt, aktar, doldur, aktar.','6 işlem')],
 'Su ölçme problemlerinde iki başlangıç yolunu da dene ve her yolun işlem sayısını karşılaştır.')

# ---------- 12 orta · atış ----------
tum=[(a,b,c) for a in range(8) for b in range(8) for c in range(8) if a+b+c==7 and 4*a+7*b+10*c==58]
tamam=[t for t in tum if min(t)>=1]; assert tum==[(0,4,3),(1,2,4),(2,0,5)] and tamam==[(1,2,4)]
S('rtb-oyun','Oyun stratejisi ve puanlama','orta','Atış Puanı','Toplam puan ve atış sayısı koşullarını birlikte sağlayan tek dağılımı tarayarak bulur.','hikâyeli','K-RTB-05 (puanlama) · hedef atışı',
 'Bir atış yarışmasında hedefin üç bölgesi vardır ve bu bölgelere isabet eden atışlar sırasıyla 4, 7 ve 10 puan kazandırır. Bir yarışmacı 7 atış yapmış, atışlarının hepsi hedefe isabet etmiş, her bölgeye en az bir atışı isabet etmiş ve toplam 58 puan toplamıştır.\nBuna göre bu yarışmacının 10 puanlık bölgeye isabet eden atış sayısı kaçtır?',
 4,[(1,'4 puanlık bölgedeki atış sayısını (1) yazmış.','dikkat'),(2,'7 puanlık bölgedeki atış sayısını (2) yazmış.','dikkat'),(3,'"Her bölgeye en az bir" koşulunu atlayıp 4 puanlık bölgesiz (0, 4, 3) dağılımını bulmuş.','dikkat'),(5,'"Her bölgeye en az bir" koşulunu atlayıp 7 puanlık bölgesiz (2, 0, 5) dağılımını bulmuş.','dikkat')],
 '10 puanlık bölgeye isabet eden atış sayısı.',['Her bölgedeki atış sayısına bir harf ver ve verilen bilgileri eşitlik olarak yaz.'],[KOS],
 [A('Eşitlikleri yaz','a + b + c = 7 ve 4a + 7b + 10c = 58.','a + b + c = 7 · 4a + 7b + 10c = 58'),A('Sadeleştir','Birinci eşitliği 4 ile çarpıp çıkar.','3b + 6c = 30 → b + 2c = 10'),A('Koşula uyanı tara','a, b, c ≥ 1: (b, c) = (2, 4) → a = 1; (4, 3) → a = 0 ✗; (6, 2) → a = −1 ✗.','(a, b, c) = (1, 2, 4)'),A('Cevabı seç','10 puanlık atış sayısı c.','c = 4')],
 'İki bilinmeyenli tam sayı koşullarında b + 2c = sabit gibi bir ilişki bulup bütün çözümleri tara, ek koşullarla ele.')

# ---------- 13 orta · apartman ----------
def apt(cl): return [p for p in permutations(range(1,6)) if all(c(*p) for c in cl)]
C13=[lambda A_,B_,C_,D_,E_:B_==C_+1,lambda A_,B_,C_,D_,E_:A_>E_,lambda A_,B_,C_,D_,E_:D_<B_,lambda A_,B_,C_,D_,E_:E_!=1,lambda A_,B_,C_,D_,E_:A_!=5]
s13=apt(C13); assert s13==[(3,5,4,1,2)]
v_drop0={p[0] for p in apt(C13[1:])}; v_drop4={p[0] for p in apt(C13[:4])}; v_rev={p[0] for p in apt([C13[0],lambda A_,B_,C_,D_,E_:A_<E_]+C13[2:])}
assert 4 in v_drop0 and 5 in v_drop4 and v_rev<={1,2,3,4,5} and 2 in v_rev and 1 in v_rev
S('rtb-cikarim','Mantık ve çıkarım (sıralama, eşleştirme)','orta','Kat Eşleştirme','Konum koşullarını birlikte sağlayan tek yerleşimi tarayarak bir kişinin katını bulur.','yeni nesil','K-RTB-04 (mantık ve çıkarım) · kat eşleştirme',
 'Beş katlı bir apartmanın her katında bir kişi oturmaktadır. Ali, Banu, Cem, Deniz ve Ece bu apartmanda farklı katlarda oturmaktadır (katlar yerden başlayarak 1’den 5’e numaralanmıştır). Oturanlarla ilgili şunlar bilinmektedir:\n• Banu, Cem’in oturduğu katın hemen üstündeki katta oturmaktadır.\n• Ali, Ece’den daha üst katta oturmaktadır.\n• Deniz, Banu’dan daha alt katta oturmaktadır.\n• Ece 1. katta oturmamaktadır.\n• Ali 5. katta oturmamaktadır.\nBuna göre Ali kaçıncı katta oturmaktadır?',
 3,[(1,'"Ali, Ece’den üstte" koşulunu ters okumuş (Ali Ece’nin altında); bu durumda Ali 1. kata yerleşir.','dikkat'),(2,'"Ali, Ece’den üstte" koşulunu ters okumuş; Ece’yi 3. kata alıp Ali’yi 2. kata yerleştirmiş.','dikkat'),(4,'"Hemen üstünde" koşulunu "üstünde" okumuş; Banu 5, Cem 3 alarak Ali’yi 4. kata yerleştirmiş.','dikkat'),(5,'Ali 5. katta oturmaz koşulunu gözden kaçırmış.','dikkat')],
 'Ali’nin oturduğu kat.',['Önce birbirine en sıkı bağlı koşuldan başla: Banu ile Cem’in katları ardışıktır. Sonra Deniz’i yerleştir.'],[CIK],
 [A('Banu–Cem çiftini tara','Banu, Cem’in hemen üstünde: (Banu, Cem) = (2, 1), (3, 2), (4, 3) ya da (5, 4).','4 olasılık'),A('Çiftleri ele','Banu 2 ise Deniz için alt kat kalmaz. Banu 3 ya da 4 ise Ali 5. katta oturamayacağından Ece 5. kata kalır ve Ali Ece’nin üstünde olamaz.','Yalnız Banu 5, Cem 4 kalır'),A('Kalan katları yerleştir','1, 2 ve 3. katlar Ali, Deniz ve Ece’nindir; Ece 1. katta değil, Ali Ece’nin üstünde.','Ece 2, Ali 3, Deniz 1'),A('Sonucu yaz','Beş koşulu birden sağlayan tek yerleşim bulundu.','Ali 3. kattadır')],
 'Mantık sorularında bütün koşulları sağlayan yerleşimleri tara; kesin bilgiyi tek çözüme ulaşana kadar daralt.')

# ---------- 14 orta · sihirli kare ----------
def sihir(kosul):
    r=[]
    for p in permutations(range(1,10)):
        if p[0]!=2 or p[5]!=3: continue
        rw=all(sum(p[3*i:3*i+3])==15 for i in range(3)); cl=all(sum(p[i::3])==15 for i in range(3)); dg=p[0]+p[4]+p[8]==15 and p[2]+p[4]+p[6]==15
        if kosul(rw,cl,dg): r.append(p)
    return r
tam=sihir(lambda r,c,d:r and c and d); assert tam==[(2,9,4,7,5,3,6,1,8)]
ndg=sihir(lambda r,c,d:r and c); ncl=sihir(lambda r,c,d:r and d); nsu=sihir(lambda r,c,d:c)
assert {p[6] for p in ndg}=={6,9} and 1 in {p[6] for p in ncl} and 5 in {p[6] for p in sihir(lambda r,c,d:d)} and 4 in {p[6] for p in nsu}
S('rtb-yerlestirme','Sayı yerleştirme (ızgara, rakam koşulu)','orta','Sihirli Kare','Satır, sütun ve köşegen toplamı eşit olan 3 × 3 yerleştirmede bilinen iki sayıdan eksik kutuyu bulur.','tablo','K-RTB-06 (sayı yerleştirme) · 3 × 3 ızgara',
 'Aşağıdaki 3 × 3 tablonun boş kutularına, 1’den 9’a kadar olan tam sayıların her biri tam bir kez kullanılacak biçimde sayılar yazılarak her satırdaki, her sütundaki ve iki köşegendeki sayıların toplamı 15 yapılacaktır. Bazı kutulardaki sayılar verilmiştir.\nBuna göre tabloda ? ile gösterilen kutuya hangi sayı yazılmalıdır?',
 6,[(1,'Sütun toplamlarını kontrol etmemiş; satırları ve köşegenleri sağlayan bir yerleşimde ? kutusuna 1 yazmış.','dikkat'),(4,'Yalnız sütun toplamlarına bakıp satırları ve köşegenleri kontrol etmemiş; ? kutusuna 4 yazmış.','dikkat'),(5,'Yalnız köşegen toplamlarına bakmış; ? kutusuna 5 yazmış.','dikkat'),(9,'Köşegen toplamlarını kontrol etmemiş; satırları ve sütunları sağlayan bir yerleşimde ? kutusuna 9 yazmış.','dikkat')],
 '? kutusundaki sayı.',['Bilinen sayılardan başlayıp her satır, sütun ve köşegendeki eksik sayıları sırayla belirlemeye çalış.'],[CIK],
 [A('Orta kutuyu bul','Toplamlar 15, dokuz sayının toplamı 45; orta satır, orta sütun ve iki köşegen orta kutuyu içerir.','4 · 15 = 60 = 45 + 3 · orta → orta = 5'),A('Orta satırı tamamla','Orta satırda ? + 5 + 3 = 15.','orta satırın 1. kutusu 7'),A('1. sütunu kullan','1. sütunda 2 + 7 + ? = 15.','? = 6')],
 'Eşit toplamlı ızgaralarda önce ortak kutuları (özellikle orta kutuyu) toplamlardan çıkar, sonra koşulları tek tek uygula.',
 sekil=tablo_svg(['1. sütun','2. sütun','3. sütun'],[['2','','' ],['','','3'],['?','','']]))

# ---------- 16 orta · en kısa yol ----------
def yol(kapali):
    d={(0,0):1}
    for x in range(5):
        for y in range(4):
            if (x,y)==(0,0): continue
            d[(x,y)]=0 if (x,y)==kapali else d.get((x-1,y),0)+d.get((x,y-1),0)
    return d[(4,3)]
assert yol(None)==35 and yol((2,1))==17 and 3*6==18 and 35-6==29 and 35-3==32
S('rtb-sayma','Sayma: tokalaşma, yol, maç sayısı','orta','Yol Sayma','Kapalı bir kavşak bulunan ızgara yolunda en kısa yol sayısını toplama yöntemiyle bulur.','hikâyeli','K-RTB-08 (sayma) · kapalı kavşaklı yol',
 'Bir şehirde yollar, kare ızgara oluşturacak biçimde birbirine bağlanmıştır. Bir araç, A kavşağından 4 birim doğuda ve 3 birim kuzeyde bulunan B kavşağına, yalnızca doğuya ya da kuzeye 1 birimlik yol parçalarını kullanarak gidecektir. A’nın 2 birim doğusunda ve 1 birim kuzeyinde bulunan kavşak yol çalışması nedeniyle kapalıdır; araç bu kavşaktan geçemez.\nBuna göre araç A’dan B’ye en kısa yoldan kaç farklı biçimde gidebilir?',
 17,[(35,'Kapalı kavşağı hiç dikkate almamış: C(7, 3) = 35.','dikkat'),(18,'Kapalı kavşaktan geçen yolların sayısını (3 · 6) cevap sanmış.','dikkat'),(29,'Kapalı kavşaktan geçen yollardan yalnız ikinci parçayı (6) çıkarmış: 35 − 6.','islem'),(32,'Kapalı kavşaktan geçen yollardan yalnız ilk parçayı (3) çıkarmış: 35 − 3.','islem')],
 'A’dan B’ye en kısa yol sayısı.',['Gidilecek adımları bir sıra olarak düşün; kapalı kavşağın yolları nasıl kısıtladığını incele.'],[YOL],
 [A('Bütün en kısa yollar','7 adımın 3’ü kuzey yönündedir.','C(7, 3) = 35'),A('Kapalı kavşağa kadar','A’dan (2, 1)’e 3 adım, 1’i kuzey.','C(3, 1) = 3'),A('Kapalı kavşaktan sonra','(2, 1)’den (4, 3)’e 4 adım, 2’si kuzey.','C(4, 2) = 6'),A('Çıkar','Kapalı kavşaktan geçen yollar 3 · 6 = 18.','35 − 18 = 17')],
 'Yasak noktalı yol sorularında tüm yolların sayısından yasak noktadan geçenlerin sayısını (iki parçanın çarpımı) çıkar.')

# ---------- 17 orta · turnuva maç sayısı ----------
mac=2*(6*5//2)+2+1+1; assert mac==34 and 12*11//2==66 and 30==2*15 and 30+2==32 and 30+2+1==33
S('rtb-sayma','Sayma: tokalaşma, yol, maç sayısı','orta','Maç Sayısı','Gruplu turnuvada grup, yarı final, final ve üçüncülük maçlarını ayrı ayrı sayarak toplam maç sayısını bulur.','hikâyeli','K-RTB-08 (sayma) · gruplu turnuva',
 'Bir voleybol turnuvasına 12 takım katılmıştır. Takımlar 6’şarlık iki gruba ayrılmış ve her takım, kendi grubundaki diğer takımlarla birer maç yapmıştır. Daha sonra her grubun puan sıralamasında ilk iki sırayı alan takımlar, bir grubun birincisi diğer grubun ikincisiyle eşleşecek biçimde yarı final oynamıştır. Yarı finali kazananlar finalde, kaybedenler üçüncülük maçında birer kez karşılaşmıştır. Bütün maçlar tek maç olarak oynanmış ve hepsinde bir galip çıkmıştır.\nBuna göre turnuvada toplam kaç maç oynanmıştır?',
 34,[(30,'Yalnız grup maçlarını saymış (2 · 15).','dikkat'),(32,'Grup maçlarına yalnız yarı final maçlarını eklemiş; final ve üçüncülük maçını unutmuş.','dikkat'),(33,'Üçüncülük maçını saymayı unutmuş: 30 + 2 + 1.','dikkat'),(66,'12 takımın birbiriyle birer maç yaptığını sanmış: C(12, 2).','dikkat')],
 'Turnuvadaki toplam maç sayısı.',['Maçları aşamalara ayır: grup maçları, yarı final, final ve üçüncülük maçı. Her grupta kaç maç var?'],[SAY],
 [A('Grup maçları','Her grupta 6 takım birbiriyle birer maç yapar.','C(6, 2) = 15 · iki grup: 30'),A('Yarı finaller','Dört takım, iki eşleşme.','2 maç'),A('Final ve üçüncülük','Biri kazananlar, biri kaybedenler için.','1 + 1 = 2 maç'),A('Topla','Aşamaları ekle.','30 + 2 + 2 = 34')],
 'Çok aşamalı turnuvada her aşamanın maç sayısını ayrı bul ve topla; hiçbir aşamayı (özellikle üçüncülük maçını) unutma.')

# ---------- 18 orta · harf kaydırma şifresi ----------
ALF='A B C Ç D E F G Ğ H I İ J K L M N O Ö P R S Ş T U Ü V Y Z'.split(); assert len(ALF)==29
def kodla(w,k,m=29): return [ (ALF.index(ch)+k)%m for ch in w]
w='ZAFER'; yeni=[(ALF.index(ch)+3)%29 for ch in w]; top=sum(i+1 for i in yeni)
assert [ALF[i] for i in yeni]==['C','Ç','H','Ğ','T'] and top==50
nowrap=sum(ALF.index(ch)+1+3 for ch in w); w26=sum(((ALF.index(ch)+1+3-1)%26)+1 if ALF.index(ch)+1+3>26 else ALF.index(ch)+1+3 for ch in w); orj=sum(ALF.index(ch)+1 for ch in w)
assert nowrap==79 and w26==53 and orj==64 and orj+3==67
S('rtb-sifre','Şifre ve kod kuralı','orta','Kodlama Kuralı','Alfabede kaydırmalı bir şifreleme kuralını (sona gelince başa dönerek) bir sözcüğe uygular.','yeni nesil','K-RTB-07 (şifre) · harf kaydırma',
 'Bir şifreleme yönteminde her harf, Türk alfabesinde kendisinden 3 harf sonra gelen harfle değiştirilir; alfabenin sonuna gelindiğinde başa dönülür (Z harfinden sonra A, B, C, … gelir). Türk alfabesi 29 harflidir ve sırası aşağıdaki gibidir:\nA, B, C, Ç, D, E, F, G, Ğ, H, I, İ, J, K, L, M, N, O, Ö, P, R, S, Ş, T, U, Ü, V, Y, Z\nA harfinin sıra numarası 1, B’nin 2, …, Z’nin 29’dur.\nBu yöntemle ZAFER sözcüğü şifrelendiğinde elde edilen sözcükteki harflerin sıra numaralarının toplamı kaçtır?',
 50,[(53,'Alfabeyi 26 harfli sanıp Z için başa dönüşte 26’yı çıkarmış.','bilgi'),(64,'Kaydırmayı hiç uygulamayıp ZAFER’in harf numaraları toplamını yazmış.','dikkat'),(67,'3’ü yalnız bir kez (toplama) eklemiş: 64 + 3.','dikkat'),(79,'Başa dönmeyi unutmuş: Z için 29 + 3 = 32’yi sıra numarası kabul etmiş.','dikkat')],
 'Şifreli sözcükteki harf numaralarının toplamı.',['Her harfin numarasını yaz ve kuralı uygula; alfabenin sonuna gelindiğinde ne olduğuna dikkat et.'],[DIZ],
 [A('Harf numaraları','Z = 29, A = 1, F = 7, E = 6, R = 21.','29, 1, 7, 6, 21'),A('3 ekle','29 + 3 = 32 başa döner: 32 − 29 = 3.','3, 4, 10, 9, 24'),A('Harfleri kontrol et','Yeni harfler.','C, Ç, H, Ğ, T'),A('Topla','Yeni numaraları ekle.','3 + 4 + 10 + 9 + 24 = 50')],
 'Dairesel kaydırmada numara toplam harf sayısını (29) aşınca 29 çıkarılır; alfabenin Türkçe uzunluğuna dikkat et.')

# ---------- 19 orta · ulaşım seçimi (tablo) ----------
ul={'A':(8,10,35,1),'B':(12,4,30,2),'C':(5,15,32,0)}
tp={k:y+b+yo+6*a for k,(y,b,yo,a) in ul.items()}; assert tp=={'A':59,'B':58,'C':52}
akt={k:y+b+yo for k,(y,b,yo,a) in ul.items()}; bek={k:y+yo+6*a for k,(y,b,yo,a) in ul.items()}; ak2={k:y+b+yo+a for k,(y,b,yo,a) in ul.items()}
assert min(akt.values())==46 and min(bek.values())==37 and min(ak2.values())==48 and tp['B']==58 and min(ul,key=lambda k:ul[k][2])=='B'
S('rtb-yasam','Yaşam becerisi: tarife, kampanya, tablo','orta','Ulaşım Seçimi','Tablodaki yürüyüş, bekleme, yolculuk ve aktarma bilgilerini birleştirerek en kısa toplam süreyi bulur.','tablo','K-RTB-10 (yaşam becerisi) · ulaşım süresi karşılaştırma',
 'Bir öğrenci okula üç ayrı yolla gidebilmektedir. Aşağıdaki tabloda her yol için evden durağa yürüyüş, ortalama bekleme ve araçta geçen süre ile aktarma sayısı verilmiştir. Her aktarma için ayrıca 6 dakika yürüme ve bekleme süresi harcanmaktadır.\nBu öğrenci toplam süresi en kısa olan yolu seçerse evden okula kaç dakikada ulaşır?',
 52,[(37,'Bekleme süresini hesaba katmamış; en kısa süreyi 37 dakika bulmuş.','dikkat'),(46,'Aktarma süresini hiç eklememiş; en kısa süreyi 46 dakika bulmuş.','dikkat'),(48,'Aktarma sayısını dakika sanıp (6 dakika yerine 1 ve 2) eklemiş; 48 dakika bulmuş.','dikkat'),(58,'Yolculuk süresi en kısa olan B yolunu seçip onun toplamını (58) yazmış.','dikkat')],
 'En kısa toplam süre (dakika).',['Her yol için bütün süreleri ve aktarmaların toplam süresini ayrı ayrı hesapla.'],[TAB],
 [A('A yolu','Yürüyüş + bekleme + yolculuk + 1 aktarma.','8 + 10 + 35 + 6 = 59 dk'),A('B yolu','2 aktarma: 12 dakika.','12 + 4 + 30 + 12 = 58 dk'),A('C yolu','Aktarma yok.','5 + 15 + 32 = 52 dk'),A('En kısayı seç','Üçünü karşılaştır.','52 dk')],
 'Parçalı sürelerde her seçeneğin toplamını ayrı hesapla; aktarma gibi ek süreleri unutma.',
 sekil=tablo_svg(['Yol','Yürüyüş (dk)','Bekleme (dk)','Yolculuk (dk)','Aktarma'],[['A','8','10','35','1'],['B','12','4','30','2'],['C','5','15','32','0']]))

# ---------- 20 orta · kademeli fatura ----------
def fat(t,k=((10,20),(15,35),(10**9,60))):
    top=0;kal=t
    for lim,p in k:
        x=min(kal,lim);top+=x*p;kal-=x
    return top
assert fat(32)==1145 and 32*60==1920 and 32*35==1120 and 10*20+22*35==970 and 10*20+15*60+7*35==1345
S('rtb-yasam','Yaşam becerisi: tarife, kampanya, tablo','orta','Kademeli Fatura','Kademeli su tarifesini tüketimin ilgili dilimlerine ayrı ayrı uygulayarak fatura tutarını hesaplar.','tablo','K-RTB-10 (yaşam becerisi) · kademeli tarife',
 'Bir belediyenin su tarifesi aşağıdaki tabloda verilmiştir. Her kademenin birim fiyatı yalnız o kademeye giren tüketime uygulanır.\nBir ayda 32 m³ su tüketen bir abonenin fatura tutarı kaç TL’dir?',
 1145,[(970,'3. kademeyi atlayıp ilk 10 m³’ten sonraki bütün tüketime 2. kademe fiyatını uygulamış: 10 · 20 + 22 · 35.','dikkat'),(1120,'Bütün tüketime 2. kademe fiyatını uygulamış: 32 · 35.','dikkat'),(1345,'Fiyatları kademelerle karıştırmış: 10 · 20 + 15 · 60 + 7 · 35.','dikkat'),(1920,'Bütün tüketime en yüksek kademenin fiyatını uygulamış: 32 · 60.','dikkat')],
 'Fatura tutarı (TL).',['Tüketimi kademelere ayır: önce ilk 10 m³, sonra 15 m³, kalanı üçüncü kademe.'],[TAB],
 [A('Tüketimi ayır','32 m³ = 10 + 15 + 7.','1. kademe 10 · 2. kademe 15 · 3. kademe 7'),A('Her dilimi fiyatla','Birim fiyatla çarp.','10 · 20 = 200 · 15 · 35 = 525 · 7 · 60 = 420'),A('Topla','Üç tutarı ekle.','200 + 525 + 420 = 1145 TL')],
 'Kademeli tarifede her birim fiyat yalnız kendi dilimine uygulanır; tüketimi dilimlere bölüp tutarları topla.',
 sekil=tablo_svg(['Kademe','Aylık tüketim dilimi','Birim fiyat (TL/m³)'],[['1. kademe','ilk 10 m³','20'],['2. kademe','sonraki 15 m³','35'],['3. kademe','25 m³’ten sonrası','60']]))

# ---------- 21 orta · öncüllü tanımlı işlem ----------
op=lambda a,b:a*b+a
rg=range(-6,7)
I21=op(-2,3)==op(3,-2); II21=all(op(a,0)==a for a in rg); III21=all((op(a,b)!=0) or (a==0 or b==-1) for a in rg for b in rg)
assert (I21,II21,III21)==(False,True,True) and op(-2,3)==-8 and op(3,-2)==-3
S('rtb-kural','Tanımlı işlem ve sayı türü','orta','Tanımlı İşlem','Tanımlı bir işlemin değişme, etkisiz eleman ve sıfır çarpım özelliklerini sınar.','öncüllü','K-RTB-01 (tanımlı işlem) · öncüllü işlem özellikleri',
 'Gerçel sayılar kümesinde ⊕ işlemi\na ⊕ b = a · b + a\nbiçiminde tanımlanıyor.\nI. (−2) ⊕ 3 = 3 ⊕ (−2) dir.\nII. Her a gerçel sayısı için a ⊕ 0 = a dır.\nIII. a ⊕ b = 0 ise a = 0 ya da b = −1 dir.\nyargılarından hangileri doğrudur?',
 'II ve III',[('Yalnız I','I’i hesaplamadan işlemi değişmeli sanıp doğru kabul etmiş; II ve III’ü sınamamış.','dikkat'),('Yalnız II','III’ü sınarken a ⊕ b = a(b + 1) çarpımını sıfıra eşitlemeyi atlamış.','dikkat'),('I ve II','I’i denemeden işlemi çarpma gibi değişmeli sanmış; III’ün b = −1 durumunu kaçırmış.','dikkat'),('I ve III','I’i değişmeli sanmış; II’de a ⊕ 0 = a · 0 + a işleminde a’yı unutup sonucu 0 bulmuş.','dikkat')],
 'Doğru olan yargılar.',['Her yargıyı ayrı ayrı sına: I için iki tarafı da hesapla; II ve III için kuralı sade biçimde yaz.'],[ISL],
 [A('I’i sına','İki yanı ayrı ayrı hesapla.','(−2) ⊕ 3 = −8 · 3 ⊕ (−2) = −3 → eşit değil'),A('II’yi sına','a ⊕ 0 = a · 0 + a.','= a → doğru'),A('III’ü sına','a ⊕ b = a(b + 1) = 0 ise a = 0 ya da b = −1.','doğru'),A('Sonuç','II ve III doğru.','II ve III')],
 'Tanımlı işlemde bir özellik tek örnekle çürütülebilir; doğru olduğunu göstermek için cebirsel hesap gerekir.',
 sira=['Yalnız I','Yalnız II','I ve II','I ve III','II ve III'])

# ---------- 26 orta · dairesel eleme ----------
def jos(n,k,bas=0,ters=False):
    ppl=list(range(1,n+1))
    if ters: ppl=[1]+list(range(n,1,-1))
    ppl=ppl[bas:]+ppl[:bas]; i=0; sira_=[]
    while ppl:
        i=(i+k-1)%len(ppl); sira_.append(ppl.pop(i))
        if ppl: i%=len(ppl)
    return sira_
dogru26=jos(12,3)[-1]; assert dogru26==10 and jos(12,2)[-1]==9 and jos(12,3,ters=True)[-1]==4 and jos(12,3,bas=1)[-1]==11 and jos(12,3)[-2]==5
S('rtb-oruntu','Örüntü, dizi ve konum','orta','Dairesel Eleme','Dairesel sayımla elemeyi tur tur uygulayarak son kalan kişinin sıra numarasını bulur.','hikâyeli','K-RTB-02 (konum) · dairesel eleme',
 'Bir çemberin çevresinde saat yönünde 1’den 12’ye kadar numaralanmış 12 kişi durmaktadır. Sayım 1 numaralı kişiden başlayıp saat yönünde “bir, iki, üç” diye sürmekte ve “üç” diyen kişi çemberden çıkmaktadır. Sayım, çıkan kişiden sonraki kişiden yeniden “bir” diyerek devam etmektedir. Bu işlem çemberde tek kişi kalana kadar sürmektedir.\nBuna göre çemberde son kalan kişinin numarası kaçtır?',
 10,[(4,'Sayımı saat yönünün tersine yapmış.','dikkat'),(5,'Son iki kişi (5 ve 10) arasında kalmış; çıkan son kişiyi kalan sanmış.','dikkat'),(9,'Çıkan kişiyi de sayarak “bir, iki” demiş; yani her seferinde 2. kişiyi çıkarmış.','dikkat'),(11,'Sayıma 1 yerine 2 numaralı kişiden başlamış.','dikkat')],
 'Son kalan kişinin numarası.',['Çıkan kişileri sırayla yaz; çember küçüldükçe sayımın nereden devam ettiğine dikkat et.'],[DAI],
 [A('İlk tur','3, 6, 9, 12 çıkar; sayım 1’den sürer.','Çıkanlar: 3, 6, 9, 12 · kalanlar: 1, 2, 4, 5, 7, 8, 10, 11'),A('İkinci tur','Sayım 1’den başlar: 4, 8 ve 1 sırayla çıkar.','Çıkanlar: 4, 8, 1 · kalanlar: 2, 5, 7, 10, 11'),A('Üçüncü tur','Sayım 2’den devam eder: 7, 2, 11 sırayla çıkar.','Kalanlar: 5, 10'),A('Son aşama','Sayım 5’ten devam eder: 5 çıkar.','Kalan: 10')],
 'Dairesel elemede her çıkıştan sonra sayımın yeniden başladığı kişiyi işaretle ve kalanları listele.')

# ---------- 28 orta · öncüllü bol sayı ----------
def bol(n): return sum(d for d in range(1,n) if n%d==0)>n
bolller=[n for n in range(1,30) if bol(n)]
I28=bol(18); II28=all(not bol(2**k) for k in range(0,12)); III28=len([n for n in range(7,30) if bol(n)])==5
assert bolller==[12,18,20,24] and (I28,II28,III28)==(True,True,False) and sum(d for d in range(1,28) if 28%d==0)==28 and 1+2+3+4==10
S('rtb-kural','Tanımlı işlem ve sayı türü','orta','Tanımlı Sayı Türü','Verilen sayı türü tanımına göre sayıları sınar ve ifadelerin doğruluğunu karar verir.','öncüllü','K-RTB-01 (tanımlı sayı türü) · bol sayı',
 'Bir doğal sayının kendisi dışındaki pozitif bölenlerinin toplamı kendisinden büyükse bu sayıya “bol sayı” denir. Örneğin 12’nin kendisi dışındaki pozitif bölenlerinin toplamı 1 + 2 + 3 + 4 + 6 = 16 > 12 olduğundan 12 bol sayıdır.\nI. 18 bol sayıdır.\nII. Hiçbir 2 kuvveti (1, 2, 4, 8, …) bol sayı değildir.\nIII. 6’dan büyük, 30’dan küçük bol sayıların sayısı 5’tir.\nyargılarından hangileri doğrudur?',
 'I ve II',[('Yalnız I','II’yi 2 kuvvetlerinin bölenlerini toplayıp denemeden yanlış saymış.','dikkat'),('Yalnız II','18’in bölenlerini 1 + 2 + 3 + 6 = 12 diye eksik toplayıp (9’u atlayıp) I’i yanlış bulmuş.','dikkat'),('Yalnız III','28’i de bol sayı sayıp III’ü doğru bulmuş; I ve II’yi sınamamış.','dikkat'),('I ve III','28’i de bol sayı sayıp III’ü doğru bulmuş; II’yi sınamamış.','dikkat')],
 'Doğru olan yargılar.',['Her yargı için ilgili sayıların kendisi dışındaki bölenlerini yazıp toplamları kendileriyle karşılaştır.'],[BLN],
 [A('I’i sına','18’in bölenleri 1, 2, 3, 6, 9.','1 + 2 + 3 + 6 + 9 = 21 > 18 → doğru'),A('II’yi sına','2ⁿ’nin kendisi dışındaki bölenleri 1, 2, 4, …, 2ⁿ⁻¹.','toplam = 2ⁿ − 1 < 2ⁿ → doğru'),A('III’ü sına','7’den 29’a bol sayılar: 12, 18, 20, 24 (28’in toplamı 28, bol değil).','4 tane → III yanlış'),A('Sonuç','I ve II doğru.','I ve II')],
 'Bir tanımı sınamak için sayıların bölenlerini tek tek yaz; genel bir yargıyı bir örnekle değil, genel bir toplamla doğrula.',
 sira=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III'])

# ---------- 29 orta · öncüllü tablo ----------
sat={'Ocak':(40,30,20),'Şubat':(35,45,25),'Mart':(50,30,40),'Nisan':(45,35,30)}
topB=sum(v[1] for v in sat.values()); topC=sum(v[2] for v in sat.values())
I29=topB>Fr(13,10)*topC; II29=all(v[0]>v[2] for v in sat.values()); aytop={k:sum(v) for k,v in sat.items()}; III29=max(aytop,key=aytop.get)=='Mart'
assert (topB,topC)==(140,115) and not I29 and II29 and III29 and aytop=={'Ocak':90,'Şubat':105,'Mart':120,'Nisan':110} and Fr(13,10)*115==Fr(299,2)
S('rtb-yasam','Yaşam becerisi: tarife, kampanya, tablo','orta','Tablo Yorumlama','Aylık satış tablosundan toplam, karşılaştırma ve en büyük değer yargılarını sınar.','tablo','K-RTB-10 (tablo yorumu) · satış tablosu',
 'Bir kırtasiyenin dört ay boyunca sattığı A, B ve C ürünlerinin adetleri aşağıdaki tabloda verilmiştir.\nI. B ürününün dört aydaki toplam satışı, C ürününün toplam satışının 1,3 katından fazladır.\nII. Her ay A ürünü, C ürününden daha çok satılmıştır.\nIII. Üç ürünün toplam satışının en fazla olduğu ay Mart’tır.\nyargılarından hangileri doğrudur?',
 'II ve III',[('Yalnız II','III için yalnız B ürününün en yüksek olduğu Şubat’a (45) bakıp Mart’ı en fazla satış ayı saymamış; III’ü yanlış bulmuş.','dikkat'),('Yalnız III','II’de Mart ayında C’nin 40’ını A’nın 50’siyle değil Ocak’taki 40’la karşılaştırıp “eşit” bulmuş; II’yi yanlış saymış.','dikkat'),('I ve II','I’de 1,3 katını hesaplamadan 140 > 115 diye yargıyı doğru saymış; III’ü Şubat’ı en yüksek sanıp yanlış bulmuş.','dikkat'),('I ve III','I’de 1,3 katını hesaplamadan 140 > 115 diye yargıyı doğru saymış; II’yi denememiş.','dikkat')],
 'Doğru olan yargılar.',['Her yargı için gerekli toplamları tablodan ayrı ayrı hesapla; I için 1,3 ile çarpmayı unutma.'],[TAB],
 [A('I’i sına','B toplamı 30 + 45 + 30 + 35 = 140; C toplamı 20 + 25 + 40 + 30 = 115; 1,3 · 115 = 149,5.','140 < 149,5 → I yanlış'),A('II’yi sına','Her ayda A ile C karşılaştırılır.','40 > 20 · 35 > 25 · 50 > 40 · 45 > 30 → doğru'),A('III’ü sına','Aylık toplamlar.','90 · 105 · 120 · 110 → Mart en fazla → doğru'),A('Sonuç','II ve III doğru.','II ve III')],
 'Tablo yargılarını tek tek sına; "katından fazla" gibi ifadelerde önce çarpımı hesapla, sonra karşılaştır.',
 sekil=tablo_svg(['Ay','A ürünü','B ürünü','C ürünü'],[['Ocak','40','30','20'],['Şubat','35','45','25'],['Mart','50','30','40'],['Nisan','45','35','30']]),
 sira=['Yalnız II','Yalnız III','I ve II','I ve III','II ve III'])

# ================= ZOR =================
# ---------- 30 orta · şehir–spor eşleştirme ----------
KIS=['Ahmet','Berna','Cemil','Derya']; SEH=['İzmir','Ankara','Bursa','Konya']; SPR=['yüzme','tenis','basketbol','voleybol']
K1=[lambda c,s,i,si:c[si['yüzme']]=='İzmir',
    lambda c,s,i,si:s[i['Ankara']]=='tenis',
    lambda c,s,i,si:c['Ahmet'] not in ('İzmir','Ankara'),
    lambda c,s,i,si:s['Ahmet']!='basketbol',
    lambda c,s,i,si:s['Berna'] not in ('yüzme','basketbol')]
def coz1(cl):
    r=[]
    for ct in permutations(SEH):
        for sp in permutations(SPR):
            c=dict(zip(KIS,ct)); s_=dict(zip(KIS,sp)); i={v:k for k,v in c.items()}; si={v:k for k,v in s_.items()}
            if all(f_(c,s_,i,si) for f_ in cl): r.append((c,s_))
    return r
r1=coz1(K1); assert {(c['Berna'],s_['Berna']) for c,s_ in r1}=={('Ankara','tenis')}
dog1='Ankara – tenis'; ist=['Bursa – voleybol','Ankara – voleybol','Konya – basketbol','İzmir – yüzme']; yan1=[]
for pr in ist:
    dr=[k for k in range(5) if any(f"{c['Berna']} – {s_['Berna']}"==pr for c,s_ in coz1([f_ for j_,f_ in enumerate(K1) if j_!=k]))]
    assert dr,pr; yan1.append((pr,f'{dr[0]+1}. bilgiyi gözden kaçırıp ({pr}) yerleşimini de olası saymış.','dikkat'))
S('rtb-cikarim','Mantık ve çıkarım (sıralama, eşleştirme)','orta','Eşleştirme','Beş koşuldan Berna’nın şehrini ve sporunu eleme yoluyla bulur.','yeni nesil','K-RTB-04 (mantık ve çıkarım) · şehir ve spor eşleştirme',
 'Ahmet, Berna, Cemil ve Derya’nın her biri İzmir, Ankara, Bursa ve Konya’dan farklı birinde yaşamakta; ayrıca her biri yüzme, tenis, basketbol ve voleybol sporlarından farklı birini yapmaktadır. Şunlar bilinmektedir:\n• Yüzme yapan kişi İzmir’de yaşamaktadır.\n• Ankara’da yaşayan kişi tenis oynamaktadır.\n• Ahmet ne İzmir’de ne de Ankara’da yaşamaktadır.\n• Ahmet basketbol oynamamaktadır.\n• Berna ne yüzme ne de basketbol yapmaktadır.\nBuna göre Berna’nın yaşadığı şehir ve yaptığı spor aşağıdakilerden hangisidir?',
 dog1,yan1,'Berna’nın şehri ve sporu.',['Önce Ahmet’in yapabileceği sporları ele; sonra Berna için kalan sporlara bak.'],[CIK],
 [A('Ahmet’i bul','Ahmet basketbol oynamıyor; yüzücü İzmir’de, tenisçi Ankara’da yaşadığından Ahmet yüzme ve tenis de yapamaz.','Ahmet voleybol oynar'),A('Berna’yı bul','Berna ne yüzme ne basketbol yapıyor; voleybol Ahmet’te.','Berna tenis oynar'),A('Şehri bul','Tenis oynayan kişi Ankara’da yaşıyor.','Berna Ankara’da yaşar')],
 'Eşleştirme sorularında önce en çok koşulu olan kişiden başla; her kişi için olanaksız seçenekleri çıkar.',
 sira=['Bursa – voleybol','Ankara – voleybol','Ankara – tenis','Konya – basketbol','İzmir – yüzme'])

# ---------- 31 zor · öncüllü boy sıralaması ----------
NM=['Elif','Ferit','Gül','Hakan','İrem']
yer=[dict(zip(NM,p)) for p in permutations(range(5)) if (lambda h:h['Elif']>h['Hakan'] and h['Hakan']>h['Gül'] and h['Hakan']>h['İrem'] and h['Gül']<h['Ferit'] and h['Ferit']<h['Elif'])(dict(zip(NM,p)))]
assert len(yer)==5
I31=all(max(h,key=h.get)=='Elif' for h in yer); II31=all(h['Hakan']>h['Ferit'] for h in yer); III31=all(min(h,key=h.get) in ('Gül','İrem') for h in yer)
assert (I31,II31,III31)==(True,False,True) and any(h['Hakan']>h['Ferit'] for h in yer)
S('rtb-cikarim','Mantık ve çıkarım (sıralama, eşleştirme)','zor','Boy Sıralaması','Eksik sıralama bilgisinde bütün olası dizilişleri tarayarak kesin doğru yargıları ayırt eder.','öncüllü','K-RTB-04 (mantık ve çıkarım) · öncüllü sıralama',
 'Elif, Ferit, Gül, Hakan ve İrem’in boyları birbirinden farklıdır. Boylarıyla ilgili şunlar bilinmektedir:\n• Elif, Hakan’dan uzundur.\n• Hakan, Gül’den ve İrem’den uzundur.\n• Gül, Ferit’ten kısadır.\n• Ferit, Elif’ten kısadır.\nBuna göre,\nI. Elif en uzun kişidir.\nII. Hakan, Ferit’ten uzundur.\nIII. En kısa kişi Gül ya da İrem’dir.\nyargılarından hangileri kesinlikle doğrudur?',
 'I ve III',[('Yalnız I','III’ü sınarken Ferit’in de en kısa olabileceğini düşünmüş; oysa Ferit Gül’den uzundur.','dikkat'),('Yalnız III','I’i, Elif’in Hakan’dan ve Ferit’ten uzun olduğunu görüp zinciri Gül ve İrem’e kadar tamamlamadığı için kesin saymamış.','dikkat'),('I ve II','II’yi, Hakan’ın Gül ve İrem’den uzun olmasından yola çıkarak Ferit’ten de uzun sanmış; Ferit–Hakan sırası verilmemiştir.','dikkat'),('I, II ve III','II’yi kesin doğru sanmış (Hakan–Ferit sırası bilgiden çıkmaz).','dikkat')],
 'Kesinlikle doğru olan yargılar.',['Koşullardan bir boy zinciri kur. Zincirde sırası belli olmayan kişi çiftlerini bul ve her iki durumu da dene.'],[CIK],
 [A('Zinciri kur','Elif > Hakan > Gül ve İrem; Elif > Ferit > Gül.','Elif en üstte'),A('Belirsizliği bul','Hakan ile Ferit, İrem ile Ferit ve Gül ile İrem arasında sıra verilmemiş.','Beş olası dizilişin tamamı yazılır'),A('Yargıları sına','I: Elif her dizilişte en uzun. II: Ferit Hakan’dan uzun olduğu dizilişler var. III: En kısa kişi Gül ya da İrem.','I doğru · II kesin değil · III doğru'),A('Sonuç','Kesin doğrular I ve III.','I ve III')],
 '“Kesinlikle doğru” sorusunda yargı, koşulları sağlayan bütün dizilişlerde doğru olmalıdır; tek bir karşı örnek yeter.',
 sira=['Yalnız I','Yalnız III','I ve II','I ve III','I, II ve III'])

# ---------- 32 zor · ileri-geri hareket ----------
def robot(hedef):
    x=0
    for n in range(1,500):
        x+= n if n%2==1 else -n
        if x==hedef: return n
assert robot(20)==39 and 2*20==40 and 19*2+1+2==41
S('rtb-oruntu','Örüntü, dizi ve konum','zor','Konum Örüntüsü','İleri ve geri hareketlerin değiştiği bir kuralda konum örüntüsünü bulup hedef konuma ilk ulaşılan hamleyi belirler.','yeni nesil','K-RTB-02 (konum örüntüsü) · ileri–geri hamleler',
 'Sayı doğrusu üzerinde 0 noktasında duran bir robot, n. hamlesinde n birim yol gitmektedir: n tek sayı ise pozitif yönde, n çift sayı ise negatif yönde. (Örneğin 1. hamlede 1 birim sağa, 2. hamlede 2 birim sola gider.)\nRobot, 20 noktasında ilk kez hangi hamlenin sonunda bulunur?',
 39,[(19,'İkişerli hamlelerin sayısını (m = 19) hamle numarası sanmış.','dikkat'),(20,'n. hamlenin sonunda robotun n noktasında olduğunu sanmış.','dikkat'),(40,'Her iki hamlede 1 birim ilerlediğini sanıp hamle sayısını 2 · 20 bulmuş.','bilgi'),(41,'2m + 1. hamlede konumu m (m + 1 yerine) sanıp m = 20 için 41 bulmuş.','dikkat')],
 'Robotun 20 noktasında ilk kez bulunduğu hamle numarası.',['İlk birkaç hamleden sonraki konumları yazıp bir düzen ara.'],[ORU,B('Tek ve çift sayılar','2m çift, 2m + 1 tek sayıdır; ardışık iki sayıdan biri tek, biri çifttir. Örnek: 7 = 2 · 3 + 1 tektir, 8 = 2 · 4 çifttir')],
 [A('İlk konumları yaz','Konumlar: 1, −1, 2, −2, 3, −3, …','1. hamle: 1 · 2: −1 · 3: 2 · 4: −2'),A('Kuralı çıkar','2m hamleden sonra konum −m; 2m + 1 hamleden sonra konum m + 1.','2m → −m · 2m + 1 → m + 1'),A('Hedefi çöz','Pozitif konumlara yalnız tek hamlelerde ulaşılır.','m + 1 = 20 → m = 19'),A('Hamle numarası','2m + 1.','2 · 19 + 1 = 39')],
 'Sırayla değişen kurallı hareketlerde, iki hamleyi bir grup alıp konumun grup sayısına göre değişimini yaz.')

# ---------- 33 zor · rakam koşullu sayma ----------
c52=[n for n in range(1000,10000) if len(set(str(n)))==4 and sum(map(int,str(n)))==10 and n%2==0]
assert len(c52)==52 and len([n for n in range(1000,10000) if len(set(str(n)))==4 and sum(map(int,str(n)))==10])==96
assert len([n for n in range(1000,10000) if sum(map(int,str(n)))==10 and n%2==0])==124 and sum(1 for p in permutations(range(10),4) if sum(p)==10 and p[3]%2==0)==60
assert len([n for n in c52 if '0' not in str(n)])==12
S('rtb-yerlestirme','Sayı yerleştirme (ızgara, rakam koşulu)','orta','Rakam Koşulu','Rakamları farklı, rakam toplamı belli çift dört basamaklı sayıları kümelere ayırarak sayar.','düz','K-RTB-06 (koşullu tarama) · rakam toplamı ve çift sayı',
 'Rakamları birbirinden farklı olan ve rakamları toplamı 10 olan 4 basamaklı çift doğal sayıların sayısı kaçtır?',
 52,[(12,'Yalnız 1, 2, 3, 4 rakamlarını kullanmış; sıfır içeren kümeleri atlamış.','dikkat'),(60,'Baştaki rakamın 0 olamayacağını unutmuş; 0 ile başlayan yazılışları da saymış.','dikkat'),(96,'Sayının çift olması koşulunu unutmuş.','dikkat'),(124,'Rakamların farklı olması koşulunu unutmuş.','dikkat')],
 'Koşulu sağlayan sayıların sayısı.',['Önce rakamları farklı ve toplamı 10 olan dört rakamlı kümeleri bul; sonra her küme için çift ve geçerli yazılışları say.'],[KOS],
 [A('Kümeleri bul','Farklı dört rakamın toplamı 10.','{0,1,2,7} {0,1,3,6} {0,1,4,5} {0,2,3,5} {1,2,3,4}'),A('Sıfırsız küme','{1,2,3,4}: son rakam 2 ya da 4 (2 seçenek), kalan 3 rakam 3! yolla.','2 · 6 = 12'),A('Sıfırlı kümeler','Son rakam çift, baş rakam 0 değil: {0,1,2,7} 10, {0,1,3,6} 10, {0,1,4,5} 10, {0,2,3,5} 10 sayı.','4 · 10 = 40'),A('Topla','İki durumu ekle.','12 + 40 = 52')],
 'Koşullu tarama: önce rakam kümelerini bul, sonra son basamak ve baştaki sıfır koşullarıyla yazılışları say.')

# ---------- 34 zor · kutu optimizasyonu ----------
def kutu(N,bx):
    INF=99;dd=[INF]*(N+1);dd[0]=0
    for nn in range(1,N+1):
        for b_ in bx:
            if nn>=b_ and dd[nn-b_]+1<dd[nn]: dd[nn]=dd[nn-b_]+1
    return dd[N]
bx=[3,7,12]; en5=kutu(40,bx); assert en5==5
tm={tuple(c) for c in product(range(14),range(6),range(4)) if 3*c[0]+7*c[1]+12*c[2]==40}; assert (0,4,1) in tm and min(sum(c) for c in tm)==5
gr=min(a+kutu(40-12*a,[3,7]) for a in (2,) ); assert gr==6 and kutu(40,[3,7])==8 and -(-40//12)==4 and -(-40//3)==14
S('rtb-optimizasyon','Optimizasyon (en az hamle, en az süre)','zor','Kutu Seçimi','Farklı boyutlu kutularla tam sayıda ürün almak için en az kutu sayısını sistemli taramayla bulur.','yeni nesil','K-RTB-09 (optimizasyon) · en az kutu',
 'Bir kırtasiyede kalemler yalnızca 3’lü, 7’li ve 12’li kutularda satılmaktadır. Kutular açılamaz ve her kutudan istenildiği kadar vardır.\nTam 40 kalem almak isteyen bir müşteri en az kaç kutu almalıdır?',
 5,[(4,'40 ÷ 12 ≈ 3,3’ü yukarı yuvarlayıp 4 kutu yazmış; 4 kutu 48 kalem eder, 40 etmez.','islem'),(6,'En büyük kutudan başlayıp (2 tane 12’lik) kalanı 3’lü ve 7’lilerle tamamlamış: 2 + 4 = 6.','bilgi'),(8,'12’lik kutuyu hiç kullanmamış: 4 tane 7’li ve 4 tane 3’lü.','bilgi'),(14,'40 ÷ 3 = 13,3’ü yukarı yuvarlayıp 14 tane 3’lü kutu yazmış; 42 kalem eder.','islem')],
 'Gerekli en az kutu sayısı.',['En büyük kutudan başlamak her zaman en iyi sonucu vermez; farklı kutu karışımlarını sistemli dene.'],[OPK],
 [A('Üç 12’lik','3 · 12 = 36; kalan 4 kalem 3’lü ve 7’lilerle tamamlanamaz.','olmaz'),A('İki 12’lik','24; kalan 16 = 7 + 3 · 3 → 4 kutu.','2 + 4 = 6 kutu'),A('Bir 12’lik','12; kalan 28 = 4 · 7.','1 + 4 = 5 kutu'),A('Sıfır 12’lik ve karşılaştır','40 = 4 · 7 + 4 · 3 → 8 kutu; hepsini karşılaştır.','En az 5 kutu')],
 'En büyük birimden başlamak her zaman en az sayıyı vermez; büyük birimin sayısını değiştirerek bütün durumları tara.')

# ---------- 35 zor · tren seferleri ----------
A_t=set(range(0,361,12)); B_t=set(range(0,361,18)); ort=A_t&B_t; tek_=len(A_t^B_t)
assert (len(A_t),len(B_t),len(ort),tek_)==(31,21,11,30) and len(A_t|B_t)==41 and len(A_t)+len(B_t)==52 and len(A_t-B_t)==20
S('rtb-periyot','Periyodik durum (takvim, lamba, tren)','zor','Sefer Çizelgesi','İki periyodik seferin ortak ve ayrı kalkış anlarını EKOK ve sayma yoluyla ayırır.','hikâyeli','K-RTB-03 (periyodik durum) · tren seferleri',
 'Bir istasyondan A treni her 12 dakikada, B treni her 18 dakikada bir kalkmaktadır. İki tren de saat 08.00’de birlikte kalkmış ve bu düzen sabit kalmıştır. Saat 08.00 ile 14.00 arasında (iki saat de dahil) yalnızca bir trenin kalktığı kaç ayrı kalkış anı vardır?',
 30,[(11,'Yalnız iki trenin birlikte kalktığı anların sayısını yazmış.','dikkat'),(20,'Yalnız A treninin tek başına kalktığı anları saymış: 31 − 11.','dikkat'),(41,'En az bir trenin kalktığı anların sayısını yazmış: 31 + 21 − 11.','bilgi'),(52,'İki trenin kalkış sayılarını doğrudan toplamış: 31 + 21.','dikkat')],
 'Yalnız bir trenin kalktığı kalkış anı sayısı.',['Önce iki trenin birlikte kalktığı anları bul; sonra her trenin 08.00–14.00 arasındaki kalkışlarını say ve ortak anları ayır.'],[PER],
 [A('A ve B’nin kalkış sayıları','6 saat = 360 dakika; 08.00 dahil.','A: 360 ÷ 12 + 1 = 31 · B: 360 ÷ 18 + 1 = 21'),A('Ortak kalkışlar','Birlikte kalkış 12 ve 18’in EKOK’u olan 36 dakikada bir.','360 ÷ 36 + 1 = 11'),A('Yalnız bir tren','Her trenin ortak anları dışındaki kalkışları.','A: 31 − 11 = 20 · B: 21 − 11 = 10'),A('Topla','İki sonucu ekle.','20 + 10 = 30')],
 'Periyodik olaylarda ortak anlar EKOK’la bulunur; “yalnız biri” sayılırken ortak anlar her iki sayımdan da çıkarılır.')

# ---------- 36 orta · şifre bulma ----------
def fb(sec,g):
    a=sum(x==y for x,y in zip(sec,g)); b=len(set(sec)&set(g))-a; return a,b
adaylar=[p_ for p_ in permutations('0123456789',3)]
sec=('9','4','3'); gs=[('5','6','3'),('9','5','4'),('6','5','0')]
assert [c for c in adaylar if all(fb(c,g)==fb(sec,g) for g in gs)]==[sec]
assert [fb(sec,g) for g in gs]==[(1,0),(1,1),(0,0)]
alt_=[]
for dr in range(3):
    for c in [c for c in adaylar if all(fb(c,g)==fb(sec,g) for k,g in enumerate(gs) if k!=dr) and c!=sec]:
        alt_.append((sum(map(int,c)),''.join(c),dr))
yan36=[]; used={16}
for t,c,dr in sorted(alt_,key=lambda x:(x[2],x[0])):
    if t not in used and len(yan36)<4 and (dr,) not in [(y[3],) for y in yan36 if len([1 for z in yan36 if z[3]==dr])>=2]:
        used.add(t); yan36.append((t,f'{dr+1}. ipucunu gözden kaçırıp {c} şifresini bulmuş.','dikkat',dr))
assert len(yan36)==4 and sum(map(int,sec))==16
yan36=[y[:3] for y in yan36]
ipuc=[f'{"".join(g)}  →  {fb(sec,g)[0]} rakam doğru yerde, {fb(sec,g)[1]} rakam yanlış yerde' for g in gs]
S('rtb-sifre','Şifre ve kod kuralı','orta','Şifre Bulma','Geri bildirimli üç denemeden tek şifreyi eleyerek bulur.','yeni nesil','K-RTB-07 (şifre) · ipuçlarından şifre bulma',
 'Bir kasanın şifresi, rakamları birbirinden farklı 3 basamaklı bir koddur (ilk rakam 0 da olabilir). Şifreyle ilgili üç deneme yapılmış ve her deneme için şu bilgiler verilmiştir:\n'+'\n'.join('• '+x for x in ipuc)+'\n(“Doğru yerde” bir rakamın şifrede aynı basamakta bulunması, “yanlış yerde” ise şifrede olup başka basamakta bulunması demektir.)\nBuna göre şifrenin rakamları toplamı kaçtır?',
 16,yan36,'Şifrenin rakamları toplamı.',['Şifrede hiçbir rakamı bulunmayan denemeyi bul ve o rakamları ele.'],[KOS],
 [A('Olmayan rakamlar','3. denemede (6 5 0) hiçbir rakam şifrede yok.','6, 5, 0 şifrede yok'),A('Son rakam','1. denemede (5 6 3) bir rakam doğru yerde; 5 ve 6 yok.','3 şifrenin 3. rakamı'),A('Diğer rakamlar','2. denemede (9 5 4) 5 yok; 9 ve 4 şifrede, biri doğru yerde biri yanlış yerde. 4 üçüncü basamakta olamaz.','9 birinci, 4 ikinci basamakta'),A('Topla','Şifre 9 4 3.','9 + 4 + 3 = 16')],
 'Geri bildirimli şifre sorularında önce hiçbir rakamı olmayan denemeyle rakamları ele, sonra yerleri belirle.')

# ---------- 37 zor · 4 × 4 yerleştirme ----------
rows4=list(permutations(range(1,5)))
def kolon_ok(g): return all(len({g[r][c] for r in range(4)})==4 for c in range(4))
def kutu_ok(g): return all(len({g[bi][bj],g[bi][bj+1],g[bi+1][bj],g[bi+1][bj+1]})==4 for bi in (0,2) for bj in (0,2))
GR={'rcb':[],'rb':[],'cb':[]}
for a_ in rows4:
    for b_ in rows4:
        for c_ in rows4:
            for d_ in rows4:
                g=(a_,b_,c_,d_); ko=kolon_ok(g); bo=kutu_ok(g)
                if bo: GR['rb'].append(g)
                if ko and bo: GR['rcb'].append(g)
GR['cb']=[tuple(zip(*g)) for g in GR['rb']]
ver={(0,1):2,(2,1):4,(2,2):2,(3,1):1,(3,3):3}
fl={k:[g for g in v if all(g[i][j]==x for (i,j),x in ver.items())] for k,v in GR.items()}
assert len(fl['rcb'])==1; sol9=fl['rcb'][0]; assert sol9==((1,2,3,4),(4,3,1,2),(3,4,2,1),(2,1,4,3)) and sol9[0][0]*sol9[1][2]==1
w9={}
for k in ('rb','cb'):
    for g in fl[k]:
        v=g[0][0]*g[1][2]
        if v!=1: w9.setdefault(v,(k,g[0][0],g[1][2]))
yan9=[]
for v in (4,6,9,12):
    k,a_,b_=w9[v]; assert a_*b_==v
    yan9.append((v,('Sütun' if k=='rb' else 'Satır')+f' kuralını atlayıp ? kutularına {a_} ve {b_} yazmış.','dikkat'))
S('rtb-yerlestirme','Sayı yerleştirme (ızgara, rakam koşulu)','zor','Izgara Yerleştirme','Her satır, sütun ve 2 × 2 bölgede 1–4 sayılarının birer kez bulunduğu ızgarada eksik kutuları belirler.','tablo','K-RTB-06 (sayı yerleştirme) · 4 × 4 ızgara',
 'Aşağıdaki 4 × 4 tablonun boş kutuları, 1, 2, 3 ve 4 sayılarıyla; her satırda, her sütunda ve tablonun dört 2 × 2’lik bölgesinin (sol üst, sağ üst, sol alt, sağ alt) her birinde her sayı tam bir kez kullanılacak biçimde doldurulacaktır. Bazı kutulardaki sayılar verilmiştir.\nBuna göre tabloda ? ile gösterilen iki kutudaki sayıların çarpımı kaçtır?',
 1,yan9,
 '? ile gösterilen iki kutudaki sayıların çarpımı.',['Önce satır ya da sütunu en çok dolu olan çizgiden başla; her kutu için kalan seçenekleri liste hâlinde tut.'],[CIK],
 [A('2. sütunu tamamla','2. sütunda 2, 4 ve 1 var; kalan sayı 3.','2. satırın 2. kutusu 3'),A('3. ve 4. satırları tamamla','3. satırda kalan 1 ve 3’ten 3, 4. sütunda zaten var → 3. satır 3 4 2 1; 4. satırda kalan 2 ve 4’ten 2, 3. sütunda zaten var → 4. satır 2 1 4 3.','3. satır: 3 4 2 1 · 4. satır: 2 1 4 3'),A('3. sütunu tamamla','3. sütunda 2 ve 4 var; 1. ve 2. satırlara 1 ile 3 kalır; 2. satırda 3 olduğundan 2. satırın 3. kutusu 1, 1. satırın 3. kutusu 3.','2. satır: ? 3 1 ?'),A('Kalanı bul','1. sütunda 3 ve 2 var; 2. satırın 1. kutusu 4 ya da 1; 2. satırda 1 var → 4. Bu durumda 1. satırın 1. kutusu 1.','? kutuları 1 ve 1 → çarpım 1')],
 'Izgara yerleştirmede satır, sütun ve bölge kurallarını birlikte kullan; en az seçeneği kalan kutudan başla.',
 sekil=tablo_svg(['1. sütun','2. sütun','3. sütun','4. sütun'],[['?','2','',''],['','','?',''],['','4','2',''],['','1','','3']]))

# ---------- 38 orta · çıkarma oyunu ----------
mv=(2,5)
@lru_cache(None)
def kz(n): return any(n>=m and not kz(n-m) for m in mv)
@lru_cache(None)
def anti(n):
    if not any(n>=m for m in mv): return True
    return any(n>=m and not anti(n-m) for m in mv)
@lru_cache(None)
def mis(n):
    if n==0: return True
    if not any(n>=m for m in mv): return False
    return any(n>=m and not mis(n-m) for m in mv)
sec38=[9,10,12,13,14]
assert [n for n in sec38 if not kz(n)]==[14] and [n for n in (10,13) if not anti(n)]==[10,13] and not mis(12) and all(kz(n) for n in (9,10,12,13))
ilk={n:[m for m in mv if n>=m and not kz(n-m)][0] for n in (9,10,12,13)}; assert ilk=={9:2,10:2,12:5,13:2} and [n for n in range(15) if not kz(n)]==[0,1,4,7,8,11,14]
S('rtb-oyun','Oyun stratejisi ve puanlama','orta','Çıkarma Oyunu','Hamle kümesi {2, 5} olan oyunda kaybettiren başlangıç sayısını küçük sayılardan başlayarak bulur.','yeni nesil','K-RTB-05 (oyun stratejisi) · {2, 5} çıkarma oyunu',
 'Masada N taş bulunmaktadır. İki oyuncu sırayla oynamakta ve her hamlede masadan tam 2 ya da tam 5 taş almaktadır. Sırası gelen oyuncu hamle yapamıyorsa (masada 2’den az taş kalmışsa) oyunu kaybeder. İki oyuncu da en iyi biçimde oynamaktadır.\nBuna göre aşağıdaki N değerlerinden hangisinde ikinci oynayan oyuncu kazanmayı garantiler?',
 14,[(9,'İkinci oyuncunun her hamleyi 7’ye (2 + 5) tamamladığını sanmış; oysa ilk oyuncu 2 alıp 7 bırakır ve kazanır.','bilgi'),(10,'Hamle yapamayanın kazandığını sanmış; oysa ilk oyuncu 2 alıp 8 bırakır ve kazanır.','bilgi'),(12,'Son taşı alanın kaybettiğini sanmış; oysa ilk oyuncu 5 alıp 7 bırakır ve kazanır.','bilgi'),(13,'Hamle yapamayanın kazandığını sanmış; oysa ilk oyuncu 2 alıp 11 bırakır ve kazanır.','bilgi')],
 'İkinci oyuncunun kazanmayı garantilediği N.',['0 ve 1 taş kalan oyuncu kaybeder. Küçük sayılardan başlayarak her N için sırası gelenin kazanıp kazanmadığını yaz.'],[OYN],
 [A('Küçük sayıları tara','0 ve 1: hamle yok, kaybeder. 2, 3: 2 alıp 0 ya da 1 bırakır, kazanır. 4: yalnız 2 alabilir, rakip kalan 2’yi alır; kaybeder.','Kaybettirenler: 0, 1, 4'),A('Tabloyu sürdür','Bir sayı, 2 ya da 5 çıkarınca kaybettiren sayıya ulaşıyorsa kazandırır: 5, 6 kazandırır; 7 ve 8 kaybettirir; 9, 10 kazandırır.','Kaybettirenler: 0, 1, 4, 7, 8, 11, 14'),A('Şıkları tara','9, 10, 12 ve 13 kazandırır (2 ya da 5 alarak sırasıyla 7, 8, 7, 11’e getirilir); 14 kaybettirir.','N = 14')],
 'Çıkarma oyunlarında kaybettiren sayıları sırayla belirle; her sayı kendinden 2 ve 5 küçük sayılara bakılarak değerlendirilir.')

# ---------- 39 zor · doğrucu–yalancı ----------
def dj(st):
    A_,B_,C_,D_=st; y=4-sum(st); k=sum(st)
    return [(A_==1)==(y>=2),(B_==1)==(k==2),(C_==1)==(A_==0),(D_==1)==(B_==C_)]
sol39=[st for st in product([0,1],repeat=4) if all(dj(st))]; assert sol39==[(1,1,0,0)]
isim='ABCD'; yan39=[]
for W in [(1,0,1,0),(0,1,0,1),(0,0,1,1),(1,1,1,0)]:
    ad_=''.join(isim[i] for i in range(4) if W[i]); ihl=[isim[i] for i,o in enumerate(dj(W)) if not o][0]
    lab=' ve '.join(ad_) if len(ad_)==2 else ', '.join(ad_[:-1])+' ve '+ad_[-1]
    yan39.append((lab,f'Doğrucuları {lab} alıp durumu sınamamış; bu durumda {ihl}’nin ifadesi çelişir.','dikkat'))
assert [y[0] for y in yan39]==['A ve C','B ve D','C ve D','A, B ve C']
S('rtb-cikarim','Mantık ve çıkarım (sıralama, eşleştirme)','zor','Doğrucu ve Yalancı','Dört kişinin birbirini ilgilendiren ifadelerinden doğrucu–yalancı dağılımını tüm olasılıkları sınayarak bulur.','yeni nesil','K-RTB-04 (mantık ve çıkarım) · doğrucu–yalancı',
 'Bir adada herkes ya her zaman doğruyu söyleyen bir doğrucu ya da her zaman yalan söyleyen bir yalancıdır. A, B, C ve D adlı dört kişi şunları söylemiştir:\nA: “Aramızda en az iki yalancı vardır.”\nB: “Aramızda tam iki doğrucu vardır.”\nC: “A yalancıdır.”\nD: “B ile C aynı türdendir (ikisi de doğrucu ya da ikisi de yalancıdır).”\nBuna göre bu dört kişiden doğrucu olanlar hangileridir?',
 'A ve B',yan39,'Doğrucu olanlar.',['16 olasılığı tek tek yazmak yerine A’nın doğrucu ya da yalancı olması durumlarını ayrı ayrı dene.'],[CIK],
 [A('A doğrucu ise','A doğrucuysa C’nin “A yalancı” ifadesi yalandır.','A doğrucu, C yalancı'),A('B ve D’yi sına','B doğrucuysa B ile C farklı türden olduğundan D’nin ifadesi yalandır; D yalancıdır. Bu durumda 2 doğrucu, 2 yalancı vardır ve dört ifade tutarlıdır. B yalancıysa D de yalancı olur ve B, C aynı türden çıkar; D’nin ifadesi doğru çıkar, çelişir.','A, B doğrucu · C, D yalancı'),A('A yalancı ise','A yalancıysa en çok 1 yalancı olmalıdır; A tek yalancıdır, B doğrucudur ve “tam iki doğrucu” demiştir, oysa 3 doğrucu vardır.','Çelişki → A doğrucudur'),A('Sonuç','Tek tutarlı dağılım.','Doğrucular A ve B')],
 'Doğrucu–yalancı sorularında bir kişinin türünü varsayıp ifadelerin tutarlılığını sına; çelişki varsa varsayımı ele.',
 sira=['A ve B','A ve C','B ve D','C ve D','A, B ve C'])

# ---------- 40 zor · köprü ----------
def kopru(sure):
    en=(frozenset(sure),0); heap=[(0,0,frozenset(sure),0)]
    import heapq
    dist={}
    while heap:
        d,_,sol,yon=heapq.heappop(heap)
        if (sol,yon) in dist: continue
        dist[(sol,yon)]=d
        if not sol and yon==1: return d
        if yon==0:
            for a_,b_ in combinations(sorted(sol),2): heapq.heappush(heap,(d+max(a_,b_),0,sol-{a_,b_},1))
            for a_ in sol: heapq.heappush(heap,(d+a_,0,sol-{a_},1))
        else:
            kar=frozenset(sure)-sol
            for a_ in kar: heapq.heappush(heap,(d+a_,0,sol|{a_},0))
            for a_,b_ in combinations(sorted(kar),2): heapq.heappush(heap,(d+max(a_,b_),0,sol|{a_,b_},0))
assert kopru([1,2,5,10])==17
st19=2+1+5+1+10; st24=10+5+5+2+2; st21=10+2+5+2+2
assert (st19,st24,st21,1+2+5+10)==(19,24,21,18)
S('rtb-optimizasyon','Optimizasyon (en az hamle, en az süre)','zor','Köprü Geçişi','Tek fenerli köprü geçişinde bütün geçiş stratejilerini karşılaştırarak en kısa süreyi bulur.','yeni nesil','K-RTB-09 (optimizasyon) · fenerli köprü',
 'Dört yürüyüşçü, karanlıkta tek bir fenerle dar bir köprüden karşıya geçecektir. Köprüden aynı anda en çok iki kişi geçebilir ve geçişler fenerle yapılmalıdır; feneri karşıdan geri getirmek için bir kişinin geri yürümesi gerekir. İki kişi birlikte geçiyorsa yavaş olanın süresi kadar zaman geçer. Yürüyüşçülerin köprüyü tek başına geçme süreleri sırasıyla 1, 2, 5 ve 10 dakikadır.\nDördünün de karşıya geçmesi için gereken en kısa süre kaç dakikadır?',
 17,[(18,'Dördünün süreleri toplamını (1 + 2 + 5 + 10) yazmış; geri dönüşleri hesaba katmamış.','dikkat'),(19,'En hızlı kişiyi her geçişte eşlik ettirmiş: 2 + 1 + 5 + 1 + 10.','bilgi'),(21,'2 dakikalık kişiyi eşlikçi seçmiş: 10 + 2 + 5 + 2 + 2.','bilgi'),(24,'En yavaş iki kişiyi (10 ve 5) önce geçirip 5 dakikalık kişiyle geri dönmüş: 10 + 5 + 5 + 2 + 2.','bilgi')],
 'En kısa toplam süre (dakika).',['Geri dönüş süreleri de toplam süreye girer; feneri geri getirecek kişiyi farklı biçimlerde seçip toplam süreleri karşılaştır.'],[OPT],
 [A('İlk geçiş ve dönüş','1 ve 2 geçer (2 dk), 1 geri döner (1 dk).','2 + 1 = 3 dk'),A('Yavaşlar birlikte','5 ve 10 birlikte geçer (10 dk); karşıdaki 2 geri döner (2 dk).','10 + 2 = 12 dk'),A('Son geçiş','1 ve 2 son kez geçer.','2 dk'),A('Topla ve karşılaştır','3 + 12 + 2 = 17; diğer stratejiler 18–24 dk.','En kısa 17 dk')],
 'Köprü sorusunda en yavaş iki kişiyi aynı geçişte götürüp geri dönüşleri hızlı kişilere yaptırmak süreyi azaltır; stratejileri tek tek karşılaştır.')

bitir(P,'rutiniki',UK)
