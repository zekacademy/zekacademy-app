"""Rasyonel Sayılar · hafif mod: 27 ana soru, kardeş yok, ipucu 1. Her cevap Fraction ile hesaplanıp assert edilir."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_mat as H
from _hafif_mat import *
from itertools import permutations,combinations
H.KONU='Rasyonel Sayılar'
P=Parti('rasyonel','Rasyonel Sayılar','mat|Rasyonel Sayılar')
UK='mat|Rasyonel Sayılar'
KY='ÖSYM 2018–2026 (rasyonel/ondalık sayılar) · yayın soru bankaları (yalnız mantık) · MEB 6–8. sınıf'
def fs(x):
    x=Fr(x); s='−' if x<0 else ''; x=abs(x)
    return s+(str(x.numerator) if x.denominator==1 else f'{x.numerator}/{x.denominator}')
def mkf(P,no,dogru,yan,**k):
    vals=[dogru]+[y[0] for y in yan]
    try:
        for v in vals: fm(v)
        mk(P,no,dogru=dogru,yan=yan,**k)
    except AssertionError as e:
        if 'ondalik' not in str(e): raise
        sira=[fs(v) for v in sorted(set(Fr(v) for v in vals))]
        mk(P,no,dogru=fs(dogru),yan=[(fs(y[0]),y[1],y[2]) for y in yan],sira=sira,**k)
def hs(x): return fs(x)  # metin içinde kesir
KES=B('Kesirleri karşılaştırma','paydalar eşitlenir ya da ondalığa çevrilir. Örnek: 3/5 = 0,6 ve 5/8 = 0,625 → 3/5 < 5/8')
ONC=B('İşlem önceliği','önce parantez, sonra çarpma/bölme (soldan sağa), en son toplama/çıkarma yapılır. Örnek: 2 + 3 × 4 = 14')
TER=B('Ters kesir','a/b kesrinin tersi b/a’dır; bir sayıyı kesre bölmek, kesrin tersiyle çarpmaktır. Örnek: 6 ÷ (2/3) = 6 × 3/2 = 9')
GEN=B('Kesirle toplama','paydalar eşitlenerek pay pay ile toplanır. Örnek: 1/2 + 1/3 = 3/6 + 2/6 = 5/6')
ODK=B('Ondalık sayılarla işlem','virgül yokmuş gibi işlem yapılır, virgül sonra yerleştirilir. Örnek: 0,3 × 0,04 = 3 × 4 = 12 → 0,012 · 0,6 ÷ 0,02 = 60 ÷ 2 = 30')
DEV=B('Devirli ondalık sayı','0,(a) = a/9 · 0,(ab) = ab/99 · 0,a(b) = (ab − a)/90. Parantez içi tekrar eden kısımdır. Örnek: 0,(3) = 3/9 = 1/3 · 0,1(6) = (16 − 1)/90 = 1/6')
SD=B('Sayı doğrusunda eşit parça','iki sayı arası n eş parçaya bölünürse bir parçanın uzunluğu (fark) ÷ n olur. Örnek: 0 ile 1 arası 4 eş parça → her parça 1/4')
GOS=B('Bir bölmenin değeri','iki işaret arasındaki değer farkı ÷ aradaki bölme sayısı. Örnek: 48 L’lik depo 8 bölmeye ayrılırsa bir bölme 48 ÷ 8 = 6 L')
TAN=B('Tanımsız ifade','paydası 0 olan kesir tanımsızdır. Örnek: 5/(x − 3) ifadesi x = 3 için tanımsızdır')
BAS=B('Basit ve bileşik kesir','payı paydasından küçük olan kesir basit kesirdir (3/7); payı paydasından büyük ya da eşit olan kesir bileşik kesirdir (7/3). Sadeleşmeyen: pay ve payda aralarında asal (3/7)')
BOL=B('Tam sayı değeri','a/b bir tam sayıysa b, a’nın bölenidir. Örnek: 12/b tam sayı → b ∈ {±1, ±2, ±3, ±4, ±6, ±12}')

kart('K-RSYN-01','Dört işlem ve işlem önceliği','Kesirler ve ondalıklarla yapılan işlemlerde paydalar eşitlenir, bölme ters çarpmaya çevrilir; merdiven kesirler içten dışa açılır.','İşlem önceliğini atlamak; ters çevirmeyi unutmak; merdiven kesirde bir basamakta durmak.','orta','düz',3,'rsy-islem','Dört işlem ve işlem önceliği','ÖSYM 2018–2025 (rasyonel işlem) · yayın: bileşik kesir, merdiven kesir')
kart('K-RSYN-02','Kesir sıralama ve karşılaştırma','Payda eşitleme, ondalığa çevirme ve pay–payda farkı (aynı farklı kesirlerde payda büyüdükçe 1’e yaklaşma) ile sıralama ve aralık sorusu çözülür.','Pay büyük olan kesri büyük saymak; payda büyük olan kesri büyük saymak; aralığın uçlarını dahil saymak.','orta','öncüllü',3,'rsy-siralama','Kesir sıralama ve karşılaştırma','ÖSYM (rasyonel karşılaştırma + doğru/yanlış) · yayın: kesir sıralama')
kart('K-RSYN-03','Sayı doğrusu ve eşit aralıklar','İki nokta arası eşit parçaya bölününce parça uzunluğu fark ÷ parça sayısıdır; işaretlenen noktalar bu adımla bulunur.','Parça sayısı ile nokta sayısını karıştırmak; başlangıcı 0 almak; farklı aralıkların parça sayısını eşit sanmak.','orta','düz',3,'rsy-dogru','Sayı doğrusu ve eşit aralıklara bölme','ÖSYM (sayı doğrusunda eşit aralıklar, ölçek okuma) · yayın: sayı doğrusu kesir')
kart('K-RSYN-04','Ondalık ve devirli ondalık sayılar','Ondalık işlemlerde virgül kaydırma; devirli sayılar 0,(a) = a/9, 0,(ab) = ab/99, 0,a(b) = (ab − a)/90 ile kesre çevrilir.','Devirli sayıyı sonlu ondalık gibi toplamak; 99 yerine 90 ya da 100 kullanmak; virgülü yanlış kaydırmak.','orta','düz',3,'rsy-ondalik','Ondalık ve devirli ondalık sayılar','ÖSYM (ondalık/devirli) · yayın: devirli ondalık sayı soruları')
kart('K-RSYN-05','Tanımsızlık, tam sayı değeri, basit/bileşik kesir','Paydanın 0 olması, kesrin tam sayı olması (bölenler) ve basit/bileşik/sadeleşmeyen kesir koşulları eşitsizlik ve bölen listeleriyle taranır.','Negatif bölenleri atlamak; 0’ı unutmak; “sadeleşmeyen” koşulunu atlamak; eşitliği (pay = payda) yanlış sınıflamak.','zor','öncüllü',4,'rsy-kosul','Tanımsız, tam sayı değeri ve basit/bileşik kesir koşulları','ÖSYM (kesrin değeri tam sayı/tanımsız) · yayın: basit–bileşik kesir')
kart('K-RSYN-06','Günlük ölçüm (tarif, depo, tartı)','Kesir–bütün ilişkisi (parça ÷ kesir = bütün), bölme ve ölçek okuma ile hikâyeli ölçüm sorusu denkleme çevrilir.','Kesri bütünle karıştırmak; kalan ile kullanılanı karıştırmak; ondalığı yanlış kaydırmak.','orta','hikâyeli',3,'rsy-olcum','Günlük ölçüm: tarif, depo göstergesi, tartı','ÖSYM (kesirle ölçüm/tartı, depo göstergesi) · yayın: kesirli problemler')
kart('K-RSYN-07','Tanımlı işlem','Soruda tanımlanan işlem verilen sayılara adım adım, parantezin içinden başlayarak uygulanır; çıkan sonuç bir sonraki adımda işlenen olur.','İşlem sırasını (parantez) atlamak; tanımı yanlış uygulamak; ters almayı unutmak.','zor','düz',4,'rsy-tanimli','Tanımlı işlem','ÖSYM (tanımlı işlem soruları) · yayın: yeni tanımlı işlem')
kart('K-RSYN-08','Kutulara yerleştirme ve rasyonel gruplama','Rakamların kesirde yerleşimi ve kesir kartlarından grup seçimi tüm olasılıklar sistemli taranarak ya da tümleyen grup düşünülerek çözülür.','Tüm yerleşimleri denemeden karar vermek; “en az” ile “en çok”u karıştırmak; bir grubu iki kez ya da hiç saymamak.','zor','düz',4,'rsy-yerlestirme','Kutulara yerleştirme ve rasyonel gruplama','ÖSYM (kutulara sayı yerleştirme, rasyonel gruplama) · yayın: kesir kartları')

# ---------- 01 kolay · dört işlem ----------
v=Fr(3,4)+Fr(5,6)-Fr(1,3); assert v==Fr(5,4)
e1=Fr(3+5-1,4+6-3); e2=Fr(3,4)+Fr(5,6); e3=Fr(9+10+4,12); e4=Fr(9+10-1,12)
assert e1==1 and e2==Fr(19,12) and e3==Fr(23,12) and e4==Fr(3,2) and len({v,e1,e2,e3,e4})==5
mkf(P,'0001',v,[(e1,'Payları ve paydaları ayrı ayrı toplayıp çıkarmış: (3 + 5 − 1)/(4 + 6 − 3).','bilgi'),(e2,'Sondaki − 1/3 terimini unutmuş.','dikkat'),(e3,'Payda eşitlemeyi doğru yapıp 1/3’ü çıkarmak yerine eklemiş.','dikkat'),(e4,'1/3’ü 12’lik paydaya genişletmeyi unutup 9/12 + 10/12 − 1/12 = 18/12 = 3/2 bulmuş.','islem')],
 tipId='rsy-islem',tip='Dört işlem ve işlem önceliği',z='kolay',alt='Dört İşlem',kaz='Paydaları farklı kesirlerle toplama ve çıkarma işlemini yapar.',kalip='düz',adim=2,
 kart='K-RSYN-01 (dört işlem) · üç kesirli toplama–çıkarma',
 metin='3/4 + 5/6 − 1/3\nişleminin sonucu kaçtır?',
 istenen='İşlemin sonucu.',ip=['Paydaları 12’de eşitle: 4, 6 ve 3’ün en küçük ortak katı.'],bilgi=[GEN],
 ad=[A('Paydaları eşitle','4, 6 ve 3’ün ortak katı 12’dir; her kesri 12’lik paydaya genişlet.','3/4 = 9/12 · 5/6 = 10/12 · 1/3 = 4/12'),A('İşlemi yap','Paydalar eşit olunca paylar işlem görür, payda aynen kalır.','9/12 + 10/12 − 4/12 = 15/12'),A('Sadeleştir','Pay ve paydayı 3’e böl.','15/12 = 5/4 (1,25)')],
 puf='Payda eşitledikten sonra yalnız paylarla işlem yap; paydalar ayrıca toplanmaz.')

# ---------- 02 kolay · tarif ----------
v=Fr(2,3)*Fr(9,2); assert v==3
e=[Fr(2,3)/Fr(9,2),Fr(2,3)+Fr(9,2),Fr(2,3)*4,Fr(2,3)*45]; e[1]=Fr(2,3)*5; assert e==[Fr(4,27),Fr(10,3),Fr(8,3),30] and len({v,*e})==5
mkf(P,'0002',v,[(e[0],'Çarpmak yerine bölmüş: 2/3 ÷ 4,5.','bilgi'),(e[1],'4,5’i 5’e yuvarlayıp 2/3 × 5 hesaplamış.','islem'),(e[2],'4,5 katının ondalık kısmını atıp yalnız 4 katını (2/3 × 4) almış.','islem'),(e[3],'4,5’i 45 gibi alarak virgülü atlamış.','islem')],
 tipId='rsy-olcum',tip='Günlük ölçüm: tarif, depo göstergesi, tartı',z='kolay',alt='Günlük Ölçüm',kaz='Kesir ve ondalık sayıyı çarparak tarif ölçüsünü büyütür.',kalip='hikâyeli',adim=2,
 kart='K-RSYN-06 (günlük ölçüm) · tarifin ondalık katı',
 metin='Bir kurabiye tarifinde 2/3 su bardağı un kullanılmaktadır.\nAşçı bu tarifin 4,5 katı kadar kurabiye yapacağına göre kaç su bardağı un kullanmalıdır?',
 istenen='Gerekli un miktarı (su bardağı).',ip=['4,5’i kesre çevir (9/2) ve çarp.'],bilgi=[ODK,B('Kesirle çarpma','paylar ve paydalar kendi aralarında çarpılır. Örnek: 2/3 × 9/2 = 18/6 = 3')],
 ad=[A('Ondalığı kesre çevir','4,5 = 9/2.','4,5 = 9/2'),A('Çarp','Katı demek çarpmaktır; paylar ve paydalar çarpılır.','2/3 × 9/2 = 18/6'),A('Sadeleştir','Pay ve payda 6’ya bölünür.','18/6 = 3 su bardağı')],
 puf='“Kaç katı” çarpma demektir; ondalığı kesre çevirince sadeleşme kolaylaşır.')

# ---------- 03 kolay · aralık ----------
a_,b_=Fr(3,5),Fr(2,3); v=Fr(5,8); assert a_<v<b_
op=[Fr(4,7),Fr(7,10),Fr(5,9),Fr(9,13)]; assert Fr(4,7)<a_ and Fr(7,10)>b_ and Fr(5,9)<a_ and Fr(9,13)>b_ and Fr(9,13)<Fr(7,10)
mkf(P,'0003',v,[(op[0],'4/7’yi 0,6’dan büyük sanmış (4/7 ≈ 0,571).','islem'),(op[1],'7/10 = 0,7’yi 2/3 = 0,667’den küçük sanmış.','islem'),(op[2],'5/9 ≈ 0,556’yı 0,6’dan büyük sanmış.','bilgi'),(op[3],'9/13 ≈ 0,692’yi 2/3’ten küçük sanmış.','islem')],
 tipId='rsy-siralama',tip='Kesir sıralama ve karşılaştırma',z='kolay',alt='Kesir Sıralama',kaz='İki kesir arasında kalan kesri ondalığa çevirerek belirler.',kalip='düz',adim=2,
 kart='K-RSYN-02 (kesir sıralama) · iki kesir arasındaki kesir',
 metin='Aşağıdaki kesirlerden hangisi 3/5 ile 2/3 arasındadır?',
 istenen='3/5 ile 2/3 arasındaki kesir.',ip=['Beş kesri de ondalığa çevirip 0,6 ve 0,667 ile karşılaştır.'],bilgi=[KES],
 ad=[A('Uçları ondalığa çevir','Pay ÷ payda.','3/5 = 0,6 · 2/3 ≈ 0,667'),A('Şıkları çevir','Her şıkkı ondalığa çevirip aralığa bak.','4/7 ≈ 0,571 · 5/8 = 0,625 · 5/9 ≈ 0,556 · 7/10 = 0,7 · 9/13 ≈ 0,692'),A('Seç','Yalnız 0,625 değeri 0,6 ile 0,667 arasındadır.','3/5 < 5/8 < 2/3')],
 puf='Kesirleri karşılaştırırken en güvenli yol hepsini ondalığa ya da ortak paydaya çevirmektir.')

# ---------- 04 kolay · ondalık ----------
v=Fr('3.6')/Fr('0.12')-Fr('0.4')*5; assert v==28
e=[Fr(3)-2,Fr('3.6')/Fr('0.12')-Fr('0.4')*5+0,(Fr('3.6')/Fr('0.12')-Fr('0.4'))*5,Fr(300)-2,Fr(30)-4]
e=[Fr(30),Fr(32),(Fr(30)-Fr('0.4'))*5,Fr(298)]; assert len({v,*e})==5
mkf(P,'0004',v,[(e[0],'Bölmeyi doğru yapıp 0,4 × 5 çarpımını çıkarmayı unutmuş (30).','dikkat'),(e[1],'Çıkarmak yerine 0,4 × 5 = 2’yi eklemiş (30 + 2).','dikkat'),(e[2],'Çarpmayı yapmadan soldan sağa gidip (30 − 0,4) × 5 hesaplamış.','bilgi'),(e[3],'3,6 ÷ 0,12’yi 300 bulmuş (virgül kaydırmayı bir basamak fazla yapmış).','islem')],
 tipId='rsy-ondalik',tip='Ondalık ve devirli ondalık sayılar',z='kolay',alt='Ondalık Sayılar',kaz='Ondalık sayılarla bölme, çarpma ve çıkarmayı işlem önceliğiyle yapar.',kalip='düz',adim=3,
 kart='K-RSYN-04 (ondalık işlem) · bölme ve çarpma sonra çıkarma',
 metin='3,6 ÷ 0,12 − 0,4 × 5\nişleminin sonucu kaçtır?',
 istenen='İşlemin sonucu.',ip=['Bölmeyi ve çarpmayı ayrı ayrı yap, çıkarmayı en sona bırak.'],bilgi=[ODK,ONC],
 ad=[A('Bölmeyi yap','Virgülleri iki basamak kaydır: 360 ÷ 12.','3,6 ÷ 0,12 = 30'),A('Çarpmayı yap','4 × 5 = 20 ve virgül bir basamak geri gelir.','0,4 × 5 = 2'),A('Çıkar','Çıkarma en sonda yapılır.','30 − 2 = 28')],
 puf='Bölenin virgülünü sağa kaydırırken bölünenin virgülünü de aynı kadar kaydır.')

# ---------- 05 kolay · sayı doğrusu ----------
st=Fr(3-1,5)
K=1+st; L=1+2*st; M=1+3*st; N=1+4*st; assert N<3 and 1+5*st==3
v=K+M; assert v==Fr(18,5)
e=[Fr(2,5)+Fr(6,5),(Fr(3,2)+Fr(5,2)),M,L+N]; assert e==[Fr(8,5),4,Fr(11,5),Fr(22,5)] and len({v,*e})==5
mkf(P,'0005',v,[(e[0],'1 ile 3 arasındaki parçaları 0’dan başlatıp K = 2/5, M = 6/5 almış.','dikkat'),(e[1],'Aralığı 4 eş parçaya bölünmüş sanıp K = 3/2, M = 5/2 almış.','bilgi'),(e[2],'Yalnız M noktasını bulup K’yi toplamamış.','dikkat'),(e[3],'K ile M yerine L ile N noktalarını toplamış.','dikkat')],
 tipId='rsy-dogru',tip='Sayı doğrusu ve eşit aralıklara bölme',z='kolay',alt='Sayı Doğrusu',kaz='Sayı doğrusunda eş parçaya bölünmüş bir aralıktaki noktaların değerlerini bulur.',kalip='düz',adim=3,
 kart='K-RSYN-03 (sayı doğrusu) · 1 ile 3 arası 5 eş parça, K ve M noktaları',
 metin='Sayı doğrusunda 1 ile 3 arası 5 eşit parçaya bölünmüştür. Bölme noktaları 1’den başlayarak sırasıyla K, L, M ve N’dir.\nBuna göre K ile M noktalarının gösterdiği sayıların toplamı kaçtır?',
 istenen='K ve M noktalarının toplamı.',ip=['Bir parçanın uzunluğunu bul ve 1’e kaç parça eklendiğine bak.'],bilgi=[SD],
 ad=[A('Parça uzunluğu','Aralık 3 − 1 = 2 birimdir ve 5 eş parçaya ayrılmıştır.','2 ÷ 5 = 2/5'),A('Noktaları bul','K birinci, M üçüncü bölme noktasıdır; 1’e eklenir.','K = 1 + 2/5 = 7/5 · M = 1 + 6/5 = 11/5'),A('Topla','İki değeri topla.','7/5 + 11/5 = 18/5 = 3,6')],
 puf='Eş parçalarda ilerleme parçanın uzunluğu kadardır; başlangıç noktasını 0 sanma.')

# ---------- 06 kolay · tam sayı koşulu ----------
S=[x for x in range(0,200) if 12%(x+1)==0]; assert S==[0,1,2,3,5,11]
c=[len([x for x in range(1,200) if 12%(x+1)==0]),len([x for x in range(-60,200) if x!=-1 and 12%abs(x+1)==0]),len([d for d in (1,2,3,4) if True]),len([2,3])]
assert c==[5,12,4,2]
mkf(P,'0006',6,[(5,'x doğal sayı olduğundan 0’ı da denemesi gerekirken x = 0 için 12/1 = 12’yi atlamış.','dikkat'),(12,'Negatif tam sayıları da sayarak x tam sayı sanmış (soruda x doğal sayı).','dikkat'),(4,'Yalnız 1, 2, 3, 4 bölenlerini yazıp 6 ve 12’yi unutmuş.','islem'),(2,'12’nin yalnız asal bölenlerini (2, 3) saymış.','bilgi')],
 tipId='rsy-kosul',tip='Tanımsız, tam sayı değeri ve basit/bileşik kesir koşulları',z='kolay',alt='Kesrin Değeri',kaz='Bir kesrin tam sayı olması koşulunu bölenler yoluyla inceler.',kalip='düz',adim=3,
 kart='K-RSYN-05 (tam sayı değeri) · 12/(x+1) ve doğal sayı koşulu',
 metin='x, 0 da dahil olmak üzere bir doğal sayı olmak üzere 12/(x + 1) ifadesi bir tam sayıdır.\nBuna göre x’in alabileceği kaç farklı değer vardır?',
 istenen='x’in alabileceği değerlerin sayısı.',ip=['x + 1, 12’nin pozitif bir böleni olmalıdır; bu bölenleri yaz.'],bilgi=[BOL,B('Doğal sayılar','0, 1, 2, 3, … sayılarıdır; 0 da bir doğal sayıdır')],
 ad=[A('Bölenleri yaz','x doğal sayı olduğundan x + 1 ≥ 1 olur; x + 1, 12’nin pozitif böleni olmalı.','x + 1 ∈ {1, 2, 3, 4, 6, 12}'),A('x değerlerini bul','Her bölenden 1 çıkar.','x ∈ {0, 1, 2, 3, 5, 11}'),A('Say','Altı değer vardır; x = 0 da doğal sayıdır.','6')],
 puf='“Kesir tam sayı” koşulunda paydanın bölenlerini yaz; doğal sayı, tam sayı ayrımına dikkat et.')

# ---------- 07 orta · merdiven ----------
def mer(a,b,c): return a+1/(b+1/c)
v=1+1/(1+1/(1+Fr(1,2))); assert v==Fr(8,5)
e=[Fr(8,3),Fr(5,3),Fr(3,2),1+1/(1+1/(1+2))]; assert e[3]==Fr(7,4) and len({v,*e})==5
mkf(P,'0007',v,[(e[0],'En içte tersini almayı unutup 1 + 5/3 yapmış.','islem'),(e[1],'Hesabı bir basamak erken bırakmış (1 + 2/3).','dikkat'),(e[2],'Yalnız en içteki 1 + 1/2’yi bulup bırakmış.','dikkat'),(e[3],'En içteki 1/2’yi 2 yazarak (1 + 2 = 3) hesaplamış.','islem')],
 tipId='rsy-islem',tip='Dört işlem ve işlem önceliği',z='orta',alt='Bileşik Kesir',kaz='Merdiven biçimindeki kesri içten dışa açarak değerini bulur.',kalip='düz',adim=3,
 kart='K-RSYN-01 (merdiven kesir) · üç katlı, toplamlı',
 metin='1 + 1/(1 + 1/(1 + 1/2))\nifadesinin değeri kaçtır?',
 istenen='İfadenin değeri.',ip=['En içten başla: önce 1 + 1/2’yi hesapla, sonra tersini al.'],bilgi=[TER,ONC],
 ad=[A('En içi hesapla','En içteki toplamı yap.','1 + 1/2 = 3/2'),A('Ters al ve topla','1/(3/2) = 2/3; sonra 1 ile topla.','1 + 2/3 = 5/3'),A('Son basamak','1/(5/3) = 3/5; dıştaki 1 ile topla.','1 + 3/5 = 8/5')],
 puf='İç içe kesirlerde her seferinde yalnız en içteki kesri sadeleştirip dışa doğru ilerle.')

# ---------- 08 orta · sıralama (pay-payda farkı) ----------
x,y,z=Fr(2013,2014),Fr(2014,2015),Fr(2012,2013); assert z<x<y
sira=['z < x < y','x < y < z','x < z < y','y < x < z','z < y < x']
mk(P,'0008',tipId='rsy-siralama',tip='Kesir sıralama ve karşılaştırma',z='orta',alt='Kesir Sıralama',kaz='Pay ile payda farkı eşit olan kesirleri 1’e yakınlığına göre sıralar.',kalip='düz',adim=3,
 kart='K-RSYN-02 (pay–payda farkı) · farkı 1 olan üç kesir',
 metin='x = 2013/2014, y = 2014/2015 ve z = 2012/2013\nolduğuna göre x, y ve z’nin sıralanışı aşağıdakilerden hangisidir?',
 dogru='z < x < y',sira=sira,yan=[('x < y < z','Yalnız z’yi (payı en küçük) en büyük sanıp x < y ilişkisini doğru bırakmış.','bilgi'),('x < z < y','z’yi x’ten büyük sanmış; 2012/2013 = 1 − 1/2013 olup x’ten uzaktır, 1’e yakın değildir.','dikkat'),('y < x < z','Payda büyüdükçe kesir küçülür diye ters düşünmüş.','bilgi'),('z < y < x','x ile y’nin yerini karıştırmış.','dikkat')],
 istenen='Kesirlerin küçükten büyüğe sıralanışı.',ip=['Her kesri 1 − 1/payda biçiminde yaz; çıkan 1/payda büyüdükçe kesir küçülür.'],bilgi=[KES,B('1’e yakınlık','pay, paydadan 1 eksikse n/(n+1) = 1 − 1/(n+1); payda büyüdükçe kesir 1’e yaklaşır. Örnek: 2/3 < 3/4 < 4/5')],
 ad=[A('Biçime getir','Her kesir, 1’den payda bölü 1 çıkarılmış gibidir.','x = 1 − 1/2014 · y = 1 − 1/2015 · z = 1 − 1/2013'),A('Çıkarılanı karşılaştır','Payda büyüdükçe 1/payda küçülür.','1/2013 > 1/2014 > 1/2015'),A('Sırala','Çıkarılan büyükse kesir küçüktür.','z < x < y')],
 puf='Payı paydadan 1 eksik olan kesirlerde payda büyüdükçe kesir büyür (1’e yaklaşır).')

# ---------- 09 orta · öncüllü sıralama ----------
a,b,c=Fr(7,9),Fr(9,11),Fr(11,14); I=a<b; II=b<c; III=a<c; assert (I,II,III)==(True,False,True)
sira=['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III']
mk(P,'0009',tipId='rsy-siralama',tip='Kesir sıralama ve karşılaştırma',z='orta',alt='Kesir Karşılaştırma',kaz='Üç kesrin ondalık karşılığını bularak öncüllü karşılaştırma ifadelerini değerlendirir.',kalip='öncüllü',adim=3,
 kart='K-RSYN-02 (rasyonel karşılaştırma + doğru/yanlış) · öncüllü üç kesir',
 metin='a = 7/9, b = 9/11 ve c = 11/14\nolduğuna göre,\nI. a < b\nII. b < c\nIII. a < c\nifadelerinden hangileri doğrudur?',
 dogru='I ve III',sira=sira,yan=[('Yalnız I','III’ü denetlememiş; a ≈ 0,778 < c ≈ 0,786.','dikkat'),('Yalnız II','1’e tamamlayan kısımları (2/9, 2/11, 3/14) karşılaştırıp küçük olanı küçük kesir sanmış (ters yorum); sonuçta yalnız II doğru çıkmış.','bilgi'),('I ve II','a < b < c sırası bekleyip I ve II’yi doğru saymış; III’ü ayrıca denetlememiş.','dikkat'),('I, II ve III','Payları da paydaları da arttığı için kesirlerin arttığını sanıp hepsini doğru saymış.','dikkat')],
 istenen='Doğru olan ifadeler.',ip=['Üç kesri de iki basamağa kadar ondalığa çevirip sırala.'],bilgi=[KES],
 ad=[A('Ondalığa çevir','Pay ÷ payda.','a ≈ 0,778 · b ≈ 0,818 · c ≈ 0,786'),A('Sırala','Küçükten büyüğe diz.','a < c < b'),A('İfadeleri denetle','I: a < b doğru · II: b < c yanlış · III: a < c doğru','I ve III')],
 puf='Öncüllü sorularda önce tüm değerleri aynı biçime getir, sonra ifadeleri tek tek denetle.')

# ---------- 10 orta · aralıktaki tam sayılar ----------
import math
cnt=[n for n in range(-10,10) if Fr(-7,3)<n<Fr(19,4)]; assert cnt==[-2,-1,0,1,2,3,4] and len(cnt)==7
assert len([n for n in range(0,10) if n<Fr(19,4)])==5 and len([n for n in cnt if n<4])==6 and len([n for n in range(-3,5)])==8 and len(range(-3,6))==9
mk(P,'0010',tipId='rsy-siralama',tip='Kesir sıralama ve karşılaştırma',z='orta',alt='Aralıktaki Sayılar',kaz='İki rasyonel sayı arasında kalan tam sayıları belirler.',kalip='düz',adim=3,
 kart='K-RSYN-02 (aralık sayma) · negatif ve pozitif uç, tam sayı sayısı',
 metin='−7/3 ile 19/4 rasyonel sayıları arasında kaç tane tam sayı vardır?',
 dogru=7,yan=[(5,'Negatif tarafı atlayıp yalnız 0, 1, 2, 3, 4’ü saymış.','dikkat'),(6,'19/4 = 4,75 olduğu hâlde 4’ü dışarıda bırakmış (−2’den 3’e).','islem'),(8,'−7/3’ü −3 gibi yuvarlayıp −3’ten başlamış.','islem'),(9,'Uçları −3 ve 5 olarak yuvarlayıp bunları da saymış.','islem')],
 istenen='İki sayı arasındaki tam sayıların adedi.',ip=['−7/3 ≈ −2,33 ve 19/4 = 4,75; bu iki sayı arasındaki tam sayıları sırayla yaz.'],bilgi=[B('Tam sayılar','…, −2, −1, 0, 1, 2, … sayılarıdır; −2,33 ile 4,75 arasındaki tam sayılar −2’den 4’e kadar gider')],
 ad=[A('Ondalığa çevir','Uçların ondalık değeri.','−7/3 ≈ −2,33 · 19/4 = 4,75'),A('Tam sayıları yaz','−2,33’ten büyük en küçük tam sayı −2, 4,75’ten küçük en büyük tam sayı 4’tür.','−2, −1, 0, 1, 2, 3, 4'),A('Say','Yedi tam sayı vardır.','7')],
 puf='Uçları ondalığa çevirip aralığın içindeki tam sayıları sıralı yaz; 0’ı ve negatifleri unutma.')

# ---------- 11 orta · iki farklı aralık ----------
A_=Fr(3,5); B_=1+Fr(3,4); v=B_-A_; assert v==Fr(23,20)
e=[Fr(3,4)-A_,(1+A_)-A_,A_-B_,B_]; assert e==[Fr(3,20),1,Fr(-23,20),Fr(7,4)] and len({v,*e})==5
mkf(P,'0011',v,[(e[0],'B’yi bulurken 1’i eklemeyi unutup 3/4 almış.','dikkat'),(e[1],'1 ile 2 arasını da 5 eş parça sanıp B = 1 + 3/5 almış.','bilgi'),(e[2],'Farkı ters yönde (A − B) hesaplamış.','dikkat'),(e[3],'B’yi bulup A’yı çıkarmamış.','dikkat')],
 tipId='rsy-dogru',tip='Sayı doğrusu ve eşit aralıklara bölme',z='orta',alt='Sayı Doğrusu',kaz='Farklı sayıda eş parçaya bölünmüş iki aralıktaki noktaların farkını bulur.',kalip='düz',adim=3,
 kart='K-RSYN-03 (sayı doğrusu) · iki aralık farklı parça sayısıyla, iki nokta arasındaki fark',
 metin='Sayı doğrusunda 0 ile 1 arası 5 eşit parçaya, 1 ile 2 arası ise 4 eşit parçaya bölünmüştür. A noktası 0’ın sağında ve 0’a 3 parça uzaklıkta, B noktası da 1’in sağında ve 1’e 3 parça uzaklıktadır.\nBuna göre B ile A noktaları arasındaki uzaklık (B − A) kaçtır?',
 istenen='B − A farkı.',ip=['Her aralığın bir parçası farklı uzunluktadır; A ve B’yi ayrı ayrı bul, B için 1’i unutma.'],bilgi=[SD],
 ad=[A('A noktası','0 ile 1 arası 5 eş parça, parça 1/5; 3 parça ileri.','A = 3 × 1/5 = 3/5'),A('B noktası','1 ile 2 arası 4 eş parça, parça 1/4; 3 parça ilerisi 1’e eklenir.','B = 1 + 3 × 1/4 = 7/4'),A('Farkı al','Paydayı 20’de eşitle.','7/4 − 3/5 = 35/20 − 12/20 = 23/20 = 1,15')],
 puf='Her aralığın parça uzunluğu kendi parça sayısına bağlıdır; ikinci aralıktaki noktaya başlangıç değerini eklemeyi unutma.')
# ---------- 12 orta · eşit aralıklı noktalar ----------
st=(Fr(9,4)+Fr(3,4))/3; Bp=Fr(-3,4)+st; Cp=Bp+st; v=Bp*Cp; assert st==1 and v==Fr(5,16)
e=[Bp+Cp,Fr(-3,4)*Fr(9,4),(Fr(-3,4)+Fr(3,2))*(Fr(-3,4)+3),0]
st2=Fr(3,4); assert (Fr(-3,4)+st2)*(Fr(-3,4)+2*st2)==0
st3=Fr(3,2); e=[Bp+Cp,Fr(-3,4)*Fr(9,4),Fr(5,4)*Fr(7,4),0]; assert e[2]==Fr(35,16) and e[0]==Fr(3,2) and e[1]==Fr(-27,16) and Fr(3,4)+Fr(1,2)==Fr(5,4)
mkf(P,'0012',v,[(e[3],'A ile D arasını 4 eş parçaya bölünmüş sanıp B = 0 almış (çarpım 0).','bilgi'),(e[0],'Çarpım yerine B ile C’nin toplamını bulmuş.','dikkat'),(e[2],'A’yı +3/4 okuyup aralığı (9/4 − 3/4) ÷ 3 = 1/2 bulmuş; B = 5/4, C = 7/4.','bilgi'),(e[1],'B ile C yerine A ile D’nin çarpımını almış.','dikkat')],
 tipId='rsy-dogru',tip='Sayı doğrusu ve eşit aralıklara bölme',z='orta',alt='Eşit Aralıklar',kaz='Eşit aralıklı noktaların uçları verildiğinde ara noktaları bulup işlem yapar.',kalip='düz',adim=4,
 kart='K-RSYN-03 (eşit aralıklı noktalar) · negatif başlangıç, ara iki nokta çarpımı',
 metin='Sayı doğrusunda A, B, C ve D noktaları bu sırayla ve eşit aralıklarla yerleşmiştir. A noktası −3/4’ü, D noktası 9/4’ü göstermektedir.\nBuna göre B ile C noktalarının gösterdiği sayıların çarpımı kaçtır?',
 istenen='B ve C’nin çarpımı.',ip=['A’dan D’ye üç eşit aralık vardır; bir aralığın uzunluğunu bul.'],bilgi=[SD],
 ad=[A('Toplam uzaklık','A’dan D’ye uzaklık.','9/4 − (−3/4) = 12/4 = 3'),A('Aralık uzunluğu','4 nokta arasında 3 eşit aralık vardır.','3 ÷ 3 = 1'),A('Noktaları yaz','A’ya aralık ekleyerek ilerle.','B = −3/4 + 1 = 1/4 · C = 1/4 + 1 = 5/4'),A('Çarp','Paylar ve paydalar çarpılır.','1/4 × 5/4 = 5/16 = 0,3125')],
 puf='Toplam uzaklığı aralık sayısına (n nokta arasında n − 1 aralık) bölerek bir aralığı bul, sonra noktaları sırayla yaz.')

# ---------- 13 orta · ondalık işlem ----------
v=(Fr('1.2')+Fr('0.8')*Fr('0.5'))/Fr('0.04'); assert v==40
e=[(Fr('1.2')+Fr('0.8'))*Fr('0.5')/Fr('0.04'),(Fr('1.2')+Fr('0.4'))/Fr('0.4'),Fr('1.2')+Fr('0.4')/Fr('0.04'),Fr(400)]; assert e==[25,4,Fr('11.2'),400] and len({v,*e})==5
mkf(P,'0013',v,[(e[0],'Çarpmayı toplamadan önce yapmayıp soldan sağa gitmiş: (1,2 + 0,8) × 0,5.','bilgi'),(e[1],'0,04 ile bölmeyi 0,4 ile bölme gibi yapmış (virgülü bir basamak eksik kaydırmış).','islem'),(e[2],'Toplamın tamamını bölmeyip yalnız 0,4’ü 0,04’e bölmüş.','bilgi'),(e[3],'Virgülü iki basamak yerine üç basamak kaydırarak 400 bulmuş.','islem')],
 tipId='rsy-ondalik',tip='Ondalık ve devirli ondalık sayılar',z='orta',alt='Ondalık Sayılar',kaz='Parantezli ondalık ifadede çarpma, toplama ve bölmeyi doğru sırayla yapar.',kalip='düz',adim=3,
 kart='K-RSYN-04 (ondalık işlem) · parantez içinde çarpma ve toplama',
 metin='(1,2 + 0,8 × 0,5) ÷ 0,04\nişleminin sonucu kaçtır?',
 istenen='İşlemin sonucu.',ip=['Önce parantezin içinde çarpmayı, sonra toplamayı yap; en son 0,04’e böl.'],bilgi=[ODK,ONC],
 ad=[A('Parantezde çarp','Çarpma toplamadan önce yapılır.','0,8 × 0,5 = 0,4'),A('Parantezde topla','Toplamı yap.','1,2 + 0,4 = 1,6'),A('Böl','Virgülü iki basamak sağa kaydır: 160 ÷ 4.','1,6 ÷ 0,04 = 40')],
 puf='Ondalık bölmede bölen tam sayı olana kadar iki sayıda da virgülü aynı kadar sağa kaydır.')

# ---------- 14 orta · devirli toplam ----------
xx=Fr(6,9); yy=Fr(16-1,90); v=xx+yy; assert v==Fr(5,6) and yy==Fr(1,6)
e=[Fr(76,100),Fr(6,9)+Fr(16,90),Fr(6,9)+Fr(16,99)]; assert e==[Fr(19,25),Fr(38,45),Fr(82,99)]
mkf(P,'0014',v,[(e[0],'Devirli sayıları sonlu ondalık gibi 0,6 + 0,16 = 0,76 toplamış.','bilgi'),(e[1],'0,1(6) sayısını 16/90 almış; ondalık kısımdaki 1’i çıkarmayı unutmuş.','islem'),(e[2],'0,1(6) sayısını 16/99 almış.','islem'),(Fr(2,3),'Yalnız x’i bulup y’yi toplamamış.','dikkat')],
 tipId='rsy-ondalik',tip='Ondalık ve devirli ondalık sayılar',z='orta',alt='Devirli Ondalık',kaz='Devirli ondalık sayıları kesre çevirip toplar.',kalip='düz',adim=3,
 kart='K-RSYN-04 (devirli ondalık) · 0,(a) ve 0,a(b) toplamı',
 metin='x = 0,(6) ve y = 0,1(6)\n(Parantez içindeki rakamlar sonsuza kadar tekrar eder.)\nolduğuna göre x + y toplamı kaçtır?',
 istenen='x + y toplamı.',ip=['0,(a) = a/9 ve 0,a(b) = (ab − a)/90 kuralıyla iki sayıyı kesre çevir.'],bilgi=[DEV],
 ad=[A('x’i kesre çevir','Devreden tek rakam: payda 9.','0,(6) = 6/9 = 2/3'),A('y’yi kesre çevir','Devretmeyen kısım 1, devreden 6: pay 16 − 1, payda 90.','0,1(6) = 15/90 = 1/6'),A('Topla','Paydayı 6’da eşitle.','2/3 + 1/6 = 4/6 + 1/6 = 5/6')],
 puf='Devirli sayıyı kesre çevirmeden toplama; 0,(ab) için 99, devretmeyen rakam varsa 90’lı payda kullan.')

# ---------- 15 orta · devirli sadeleşmiş kesir ----------
fr_=Fr(81,99); assert fr_==Fr(9,11) and fr_.numerator+fr_.denominator==20
e=[Fr(9,10).numerator+10,81+99,Fr(81,100).numerator+100,9]; assert e==[19,180,181,9]
mkf(P,'0015',20,[(19,'0,(81)’i 81/90 = 9/10 alıp 9 + 10 bulmuş.','islem'),(180,'Kesri sadeleştirmeden 81 + 99 toplamış.','dikkat'),(181,'Devirli sayıyı sonlu ondalık sanıp 81/100 almış, 81 + 100 bulmuş.','bilgi'),(9,'Yalnız payı (9) vermiş; pay ile paydanın toplamı isteniyor.','dikkat')],
 tipId='rsy-ondalik',tip='Ondalık ve devirli ondalık sayılar',z='kolay',alt='Devirli Ondalık',kaz='Devirli ondalık sayıyı sadeleşmiş kesre çevirip pay ve paydasını toplar.',kalip='düz',adim=3,
 kart='K-RSYN-04 (devirli ondalık) · 0,(ab) sadeleşmiş kesir',
 metin='0,(81) devirli ondalık sayısında parantez içindeki rakamlar sonsuza kadar tekrar eder. Bu sayı, m ile n aralarında asal pozitif tam sayılar olmak üzere m/n biçiminde yazılıyor.\nBuna göre m + n toplamı kaçtır?',
 istenen='m + n toplamı.',ip=['0,(ab) = ab/99 kuralıyla kesre çevir ve tam sadeleştir.'],bilgi=[DEV,B('Aralarında asal','1’den başka ortak böleni olmayan sayılar. Örnek: 9 ve 11 aralarında asaldır, 81 ve 99 değildir (ortak bölenleri 9)')],
 ad=[A('Kesre çevir','İki rakam devrediyor: payda 99.','0,(81) = 81/99'),A('Sadeleştir','Pay ve paydayı ortak bölen 9’a böl.','81/99 = 9/11'),A('Topla','m = 9, n = 11.','9 + 11 = 20')],
 puf='Devirli sayıdan çıkan kesri her zaman sadeleştir; pay ve payda aralarında asal olmalıdır.')

# ---------- 16 orta · tanımsız ----------
xs=[x for x in range(-20,20) if x*x-4*x+3==0]; assert xs==[1,3] and sum(xs)==4
mkf(P,'0016',4,[(-4,'Çarpanlara ayırırken işaretleri ters alıp (x + 1)(x + 3) yazmış; köklerin toplamı −4 olmuş.','islem'),(3,'Yalnız x = 3 kökünü bulmuş.','dikkat'),(1,'Yalnız x = 1 kökünü bulmuş.','dikkat'),(2,'Köklerin ortalamasını almış (toplam yerine).','dikkat')],
 tipId='rsy-kosul',tip='Tanımsız, tam sayı değeri ve basit/bileşik kesir koşulları',z='orta',alt='Tanımsızlık',kaz='Paydayı sıfır yapan değerleri bulup toplar.',kalip='düz',adim=3,
 kart='K-RSYN-05 (tanımsızlık) · ikinci dereceden payda',
 metin='x gerçek sayı olmak üzere\n5/(x² − 4x + 3)\nifadesini tanımsız yapan x değerlerinin toplamı kaçtır?',
 istenen='Tanımsızlık değerlerinin toplamı.',ip=['Paydayı çarpanlarına ayır ve her çarpanı 0’a eşitle.'],bilgi=[TAN,B('Çarpanlara ayırma','x² − 4x + 3, toplamı −4 çarpımı 3 olan iki sayıyla (−1) ve (−3) yazılır: (x − 1)(x − 3)')],
 ad=[A('Paydayı 0 yap','Tanımsız olması için payda 0 olmalı.','x² − 4x + 3 = 0'),A('Çarpanlara ayır','Çarpımı 3, toplamı −4 olan sayılar −1 ve −3.','(x − 1)(x − 3) = 0'),A('Kökleri topla','Her çarpan sırayla 0’a eşitlenir.','x = 1 veya x = 3 · 1 + 3 = 4')],
 puf='Tanımsızlık = payda 0; paydayı çarpanlarına ayırıp her çarpanı sıfıra eşitle.')

# ---------- 17 orta · tam sayı değeri, tüm n ----------
ns=[n for n in range(-60,60) if n!=-2 and (3*n+14)%(n+2)==0]; assert sorted(ns)==[-10,-6,-4,-3,-1,0,2,6] and sum(ns)==-16
assert sum(n for n in ns if n>0)==8 and sum(n for n in ns if n+2>0)==7
assert sum(n for n in ns if n<0)==-24
mkf(P,'0017',-16,[(8,'Yalnız pozitif n değerlerini (2 ve 6) toplamış.','dikkat'),(7,'n + 2 pozitif olan değerleri (−1, 0, 2, 6) toplamış; negatif bölenleri atlamış.','dikkat'),(-24,'Yalnız negatif n değerlerini toplamış.','dikkat'),(16,'Doğru toplamı −16 yerine 16 yazmış (işareti atlamış).','dikkat')],
 tipId='rsy-kosul',tip='Tanımsız, tam sayı değeri ve basit/bileşik kesir koşulları',z='orta',alt='Kesrin Değeri',kaz='Bir kesrin tam sayı olması için payı bölen biçimine getirip tüm n değerlerini toplar.',kalip='düz',adim=4,
 kart='K-RSYN-05 (tam sayı değeri) · (3n + 14)/(n + 2), negatif bölenler dahil',
 metin='n bir tam sayı olmak üzere (3n + 14)/(n + 2) ifadesi bir tam sayıdır.\nBuna göre n’in alabileceği değerlerin toplamı kaçtır?',
 istenen='n değerlerinin toplamı.',ip=['3n + 14 = 3 × (n + 2) + 8 yazıp kesri 3 + 8/(n + 2) biçimine getir.'],bilgi=[BOL],
 ad=[A('Kesri ayır','Payı payda cinsinden yaz.','(3n + 14)/(n + 2) = 3 + 8/(n + 2)'),A('Bölenleri yaz','8/(n + 2) tam sayı ise n + 2, 8’in böleni olmalı (negatifler dahil).','n + 2 ∈ {±1, ±2, ±4, ±8}'),A('n değerleri','Her bölenden 2 çıkar.','n ∈ {−1, 0, 2, 6, −3, −4, −6, −10}'),A('Topla','Pozitif ve negatifleri topla.','(−1 + 0 + 2 + 6) + (−3 − 4 − 6 − 10) = 7 − 23 = −16')],
 puf='Kesri “tam kısım + kalan/payda” biçimine getir; payda kalanın böleni olmalıdır, negatif bölenleri de dene.')

# ---------- 18 orta · öncüllü a/b ----------
import itertools
tr=lambda f:all(f(a,b) for a in range(1,40) for b in range(a+1,41))
I=tr(lambda a,b:Fr(a+1,b+1)>Fr(a,b)); II=tr(lambda a,b:Fr(a,b+1)>Fr(a,b)); III=tr(lambda a,b:Fr(a,b)>Fr(b,a))
assert (I,II,III)==(True,False,False) and all(Fr(a,b)<Fr(b,a) for a in range(1,40) for b in range(a+1,41))
mk(P,'0018',tipId='rsy-siralama',tip='Kesir sıralama ve karşılaştırma',z='orta',alt='Kesir Karşılaştırma',kaz='Pozitif tam sayılarla yazılan kesirlerde pay ve paydaya sayı eklemenin etkisini değerlendirir.',kalip='öncüllü',adim=3,
 kart='K-RSYN-02 (rasyonel karşılaştırma + doğru/yanlış) · a < b iken pay–payda değişimi',
 metin='a ve b, a < b olan pozitif tam sayılardır.\nBuna göre,\nI. (a + 1)/(b + 1) > a/b\nII. a/(b + 1) > a/b\nIII. a/b > b/a\nifadelerinden hangileri her zaman doğrudur?',
 dogru='Yalnız I',sira=['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III'],yan=[('Yalnız II','Payda büyüyünce kesrin büyüdüğünü sanıp II’yi doğru, ekleme sonrası kesrin küçüldüğünü sanıp I’i yanlış saymış.','bilgi'),('I ve II','II’yi doğru saymış; paydaya 1 eklemenin kesri büyüttüğünü sanmış.','bilgi'),('I ve III','III’ü doğru saymış; a < b iken a/b < 1 < b/a olduğunu görmemiş.','bilgi'),('I, II ve III','Paydaya sayı eklemenin kesri küçülttüğünü ve a/b < 1 < b/a olduğunu görmemiş.','bilgi')],
 istenen='Her zaman doğru olan ifadeler.',ip=['a = 2, b = 3 gibi küçük bir örnekle üç ifadeyi dene.'],bilgi=[KES],
 ad=[A('Örnek dene','a = 2, b = 3 için a/b = 2/3.','I: 3/4 > 2/3 doğru · II: 2/4 > 2/3 yanlış · III: 2/3 > 3/2 yanlış'),A('I’i doğrula','a < b iken payına ve paydasına 1 eklenen kesir 1’e yaklaşır, yani büyür.','(a + 1)/(b + 1) > a/b her zaman'),A('II ve III’ü çürüt','Payda büyüyünce kesir küçülür; a < b ise a/b < 1 < b/a.','II ve III yanlış → Yalnız I')],
 puf='“Her zaman doğru” için tek karşı örnek ifadeyi çürütür; doğru görünenleri genel olarak gerekçelendir.')

# ---------- 19 orta · depoya ekleme ----------
cap=Fr(36)/(Fr(7,10)-Fr(2,5)); assert cap==120
e=[Fr(36)/Fr(2,5),Fr(36)*Fr(3,10),cap+36,cap-36]; assert e==[90,Fr('10.8'),156,84] and len({cap,*e})==5
mkf(P,'0019',cap,[(e[0],'36 litreyi yalnız başlangıçtaki 2/5’e karşılık sanıp 36 ÷ (2/5) yapmış.','dikkat'),(e[1],'36 litreyi kesirle çarpıp 3/10’un kendisini bulmuş (bölmesi gerekirken).','bilgi'),(e[2],'Kapasiteyi 120 bulduktan sonra eklenen 36 litreyi bir de üstüne katmış.','dikkat'),(e[3],'Kapasiteyi bulduktan sonra 36 litreyi çıkarmış.','dikkat')],
 tipId='rsy-olcum',tip='Günlük ölçüm: tarif, depo göstergesi, tartı',z='orta',alt='Günlük Ölçüm',kaz='Kesir farkına karşılık gelen miktardan bütünü bulur.',kalip='hikâyeli',adim=3,
 kart='K-RSYN-06 (günlük ölçüm) · depoya eklenen su, kesir farkından bütün',
 metin='Bir su deposunun 2/5’i doludur. Depoya 36 litre su eklendiğinde deponun 7/10’u doluyor.\nBuna göre bu deponun tamamı kaç litre su alır?',
 istenen='Deponun kapasitesi (litre).',ip=['Eklenen 36 litre, deponun kaçta kaçına denk geliyor? Kesirleri çıkar.'],bilgi=[TER,B('Parça ve bütün','bir bütünün a/b’si P ise bütün = P ÷ (a/b). Örnek: bütünün 1/4’ü 10 ise bütün 10 × 4 = 40')],
 ad=[A('Farkı bul','Eklenen su, iki doluluk oranının farkıdır.','7/10 − 2/5 = 7/10 − 4/10 = 3/10'),A('Eşitlik kur','Deponun 3/10’u 36 litredir.','(3/10) × T = 36'),A('Bütünü bul','36’yı kesrin tersiyle çarp.','T = 36 × 10/3 = 120')],
 puf='İki doluluk oranının farkı, eklenen miktarın bütüne oranıdır; bütünü bulmak için miktarı o kesre böl.')

# ---------- 20 orta · tartı ----------
e_=Fr(1,2); assert 4*e_+Fr(1,4)==2*e_+Fr(5,4); v=5*e_; assert v==Fr(5,2)
e=[Fr(5,4),Fr(15,4),Fr(5),Fr(25,8)]
assert 5*Fr(1,4)==e[0] and 5*Fr(3,4)==e[1] and 5*1==e[2] and 5*Fr(5,8)==e[3]
assert Fr(1,4)+Fr(5,4)==Fr(3,2) and Fr(3,2)/6==Fr(1,4) and Fr(5,4)/2==Fr(5,8)
mkf(P,'0020',v,[(e[0],'2 elmayı çıkarmak yerine ekleyip 6e = 1,5 yazmış, e = 0,25 bulmuş.','islem'),(e[1],'1/4’ü yanlış tarafa geçirip 2e = 1,25 + 0,25 = 1,5 yazmış, e = 0,75 bulmuş.','islem'),(e[2],'2e = 1 bulup 2’ye bölmeyi atlayarak e = 1 kg almış.','islem'),(e[3],'1/4 kg’lık ağırlığı hesaba katmayıp 2e = 1,25 almış (e = 0,625).','dikkat')],
 tipId='rsy-olcum',tip='Günlük ölçüm: tarif, depo göstergesi, tartı',z='orta',alt='Günlük Ölçüm',kaz='Dengedeki terazi eşitliğinden eşit ağırlıklı nesnenin ağırlığını bulur.',kalip='hikâyeli',adim=3,
 kart='K-RSYN-06 (günlük ölçüm) · terazi dengesi, bilinmeyenli kesirli ağırlık',
 metin='Dengede duran bir terazinin sol kefesinde 4 elma ile 1/4 kg’lık bir ağırlık, sağ kefesinde ise 2 elma ile 1,25 kg’lık bir ağırlık vardır. Elmaların hepsi birbiriyle aynı ağırlıktadır.\nBuna göre 5 elma kaç kg çeker?',
 istenen='5 elmanın ağırlığı (kg).',ip=['Bir elmanın ağırlığına e de; iki kefenin eşitliğini yazıp e’yi bul.'],bilgi=[B('Denge eşitliği','dengedeki terazide iki kefenin ağırlığı eşittir. Her iki taraftan aynı değer çıkarılınca denge bozulmaz')],
 ad=[A('Eşitliği yaz','Bir elma e kg olsun.','4e + 1/4 = 2e + 5/4'),A('Sadeleştir','İki taraftan 2e ve 1/4 çıkar.','2e = 5/4 − 1/4 = 1'),A('e ve sonucu bul','Bir elma 1/2 kg; 5 elma bunun 5 katıdır.','e = 1/2 · 5e = 5/2 = 2,5')],
 puf='Terazi sorularında iki kefeyi eşitle, ortak terimleri iki taraftan da çıkararak bilinmeyeni yalnız bırak.')
# ---------- 21 zor · basit/bileşik ----------
xs=[x for x in range(-50,60) if x>2 and 5>x-2>0 and Fr(x,9)<1 and math.gcd(x,9)==1]; assert xs==[4,5] and sum(xs)==9
assert sum(x for x in range(3,8) if math.gcd(x,9)==1)==16 and sum(x for x in range(3,7))==18 and sum(x for x in range(3,9) if math.gcd(x,9)==1)==24 and sum(range(3,8))==25
mkf(P,'0021',9,[(16,'Pay > payda yerine pay ≥ payda alıp x = 7’yi de eklemiş (4 + 5 + 7).','dikkat'),(18,'Pay > payda koşulunu doğru kullanmış ama x/9’un sadeleşmeyen olma koşulunu atlayıp 3, 4, 5, 6’yı toplamış.','dikkat'),(24,'x/9 koşulunu uygulayıp 5/(x − 2)’nin payının paydadan büyük olması koşulunu hiç kullanmamış (4 + 5 + 7 + 8).','dikkat'),(25,'Pay ≥ payda alıp sadeleşmeme koşulunu da atlayarak 3, 4, 5, 6, 7’yi toplamış.','dikkat')],
 tipId='rsy-kosul',tip='Tanımsız, tam sayı değeri ve basit/bileşik kesir koşulları',z='zor',alt='Basit ve Bileşik Kesir',kaz='Payı paydasından büyük bir kesir ile sadeleşmeyen basit kesir koşullarını birlikte sağlayan tam sayıları belirler.',kalip='düz',adim=4,
 kart='K-RSYN-05 (basit/bileşik kesir) · payı paydasından büyük kesir + sadeleşmeyen basit kesir',
 metin='x bir tam sayı olmak üzere 5/(x − 2) kesrinin payı da paydası da pozitiftir ve payı paydasından büyüktür. x/9 kesri ise sadeleşmeyen bir basit kesirdir.\nBuna göre x’in alabileceği değerlerin toplamı kaçtır?',
 istenen='x değerlerinin toplamı.',ip=['İlk koşul x için bir aralık verir; bu aralıktaki değerlerden paydadaki sayıyla sadeleşenleri ele.'],bilgi=[BAS],
 ad=[A('Birinci koşul','Payda pozitif ve pay paydadan büyük olmalı.','0 < x − 2 < 5 → 3 ≤ x ≤ 6'),A('Basit kesir koşulu','x/9 basit ise x < 9; bu aralıkta zaten sağlanır.','x < 9'),A('Sadeleşmeme koşulu','x ile 9 aralarında asal olmalı; 3 ve 6, 9 ile sadeleşir.','3 ve 6 elenir → x ∈ {4, 5}'),A('Topla','Kalan değerleri topla.','4 + 5 = 9')],
 puf='Kesir koşullarını tek tek aralığa çevir, sonra “sadeleşmeyen” gibi ek koşulla taranan değerleri ele.')
# ---------- 22 zor · devirli ab/ba ----------
sol=[(a,b) for a in range(1,10) for b in range(0,10) if Fr(10*a+b+10*b+a,99)==Fr(11,9) and Fr(10*a+b-10*b-a,99)==Fr(27,99)]; assert sol==[(7,4)] and 7*4==28
mkf(P,'0022',28,[(11,'a + b = 11’i bulup durmuş; çarpım isteniyor.','dikkat'),(3,'a − b farkını (3) çarpım sanmış.','dikkat'),(7,'a’yı bulup bırakmış.','dikkat'),(4,'b’yi bulup bırakmış.','dikkat')],
 tipId='rsy-ondalik',tip='Ondalık ve devirli ondalık sayılar',z='orta',alt='Devirli Ondalık',kaz='İki devirli ondalık eşitliğini kesre çevirip rakamların toplam ve farkını bularak çarpımı hesaplar.',kalip='düz',adim=4,
 kart='K-RSYN-04 (devirli ondalık) · 0,(ab) ve 0,(ba) toplam–farkı',
 metin='a ve b birer rakam olmak üzere\n0,(ab) + 0,(ba) = 1,(2)\n0,(ab) − 0,(ba) = 0,(27)\n(Parantez içindeki rakamlar sonsuza kadar tekrar eder.)\nolduğuna göre a × b çarpımı kaçtır?',
 istenen='a × b çarpımı.',ip=['0,(ab) = (10 × a + b)/99 olarak yaz; toplamda 11 × (a + b), farkta 9 × (a − b) çıkar.'],bilgi=[DEV,IKI if False else B('İki basamaklı sayı','ab = 10 × a + b. Örnek: 74 = 10 × 7 + 4')],
 ad=[A('Eşitlikleri kesre çevir','1,(2) = 1 + 2/9 = 11/9; 0,(27) = 27/99.','(ab + ba)/99 = 11/9 · (ab − ba)/99 = 27/99'),A('Toplamdan','ab + ba = 11 × (a + b) olduğundan 11 × (a + b) = 121.','a + b = 11'),A('Farktan','ab − ba = 9 × (a − b) = 27.','a − b = 3'),A('Rakamları bul','İki denklemi çöz, çarp.','a = 7, b = 4 · a × b = 28')],
 puf='ab ile ba’nın toplamı 11 × (a + b), farkı 9 × (a − b)’dir; devirli sayılarda bu çözümleme işi kısaltır.')

# ---------- 23 zor · tanımlı işlem ----------
d=lambda p,q:1/Fr(p)+1/Fr(q)
v=d(d(3,6),d(4,12)); assert d(3,6)==Fr(1,2) and d(4,12)==Fr(1,3) and v==5
dd=lambda p,q:1/(Fr(p)+Fr(q))
e=[Fr(1,2)+Fr(1,3),dd(Fr(1,2),Fr(1,3)),d(d(3,6),4),Fr(2)*3]; assert e==[Fr(5,6),Fr(6,5),Fr(9,4),6] and len({v,*e})==5
mkf(P,'0023',v,[(e[0],'Son adımda ⊙ yerine toplama yapıp 1/2 + 1/3 almış.','dikkat'),(e[1],'Son adımda tanımı 1/(m + n) gibi uygulayıp 1/(1/2 + 1/3) = 6/5 bulmuş.','bilgi'),(e[2],'4 ⊙ 12 işlemini yapmayıp ikinci işlenen olarak yalnız 4’ü alıp (3 ⊙ 6) ⊙ 4 hesaplamış.','dikkat'),(e[3],'Son adımda tersleri toplamak yerine çarpıp 2 × 3 = 6 bulmuş.','bilgi')],
 tipId='rsy-tanimli',tip='Tanımlı işlem',z='zor',alt='Tanımlı İşlem',kaz='Tersler toplamı biçiminde tanımlanan işlemi iki parantezli ifadede uygular.',kalip='düz',adim=4,
 kart='K-RSYN-07 (tanımlı işlem) · m ⊙ n = 1/m + 1/n, iki parantezin birleşimi',
 metin='Sıfırdan farklı iki rasyonel sayı için\nm ⊙ n = 1/m + 1/n\nişlemi tanımlanıyor. Örneğin 2 ⊙ 4 = 1/2 + 1/4 = 3/4’tür.\nBuna göre (3 ⊙ 6) ⊙ (4 ⊙ 12) işleminin sonucu kaçtır?',
 istenen='(3 ⊙ 6) ⊙ (4 ⊙ 12)’nin değeri.',ip=['Önce iki parantezin içini ayrı ayrı hesapla; çıkan sonuçlar son işlemin işlenenleri olur.'],bilgi=[TER,B('Tanımlı işlem','soruda verilen kural, işlenen sayılar yerine konarak uygulanır. Örnek: m ⊙ n = 1/m + 1/n ise 5 ⊙ 10 = 1/5 + 1/10 = 3/10')],
 ad=[A('Birinci parantez','Kuralı m = 3, n = 6 için uygula.','3 ⊙ 6 = 1/3 + 1/6 = 1/2'),A('İkinci parantez','Kuralı m = 4, n = 12 için uygula.','4 ⊙ 12 = 1/4 + 1/12 = 1/3'),A('Son işlem','İşlenenler artık 1/2 ve 1/3’tür; her birinin tersi alınır.','(1/2) ⊙ (1/3) = 1/(1/2) + 1/(1/3) = 2 + 3'),A('Sonuç','Toplamı yaz.','5')],
 puf='Tanımlı işlemde parantezleri ayrı ayrı hesapla, sonuçları son adımın işlenenleri olarak aynen yerleştir.')
# ---------- 24 zor · kutulara yerleştirme ----------
vals=[Fr(a,b)+Fr(c,d_) for a,b,c,d_ in permutations((2,3,5,7))]; mn=min(vals); assert mn==Fr(29,35)
c1=Fr(2,7)+Fr(3,5); c2=Fr(2,3)+Fr(5,7); c3=Fr(3,2)+Fr(5,7); c4=Fr(7,2)+Fr(5,3); assert (c1,c2,c3,c4)==(Fr(31,35),Fr(29,21),Fr(31,14),Fr(31,6)) and c4==max(Fr(a,b)+Fr(c,d_) for a,b,c,d_ in permutations((2,3,5,7))) and mn not in (c1,c2,c3,c4) and mn in [Fr(2,5)+Fr(3,7),Fr(3,7)+Fr(2,5)]
mkf(P,'0024',mn,[(c1,'Küçük sayıları pay yapmış ama eşleştirmeyi ters kurup 2/7 + 3/5 almış (31/35).','islem'),(c2,'Küçük sayıları (2 ve 5) pay, 3 ve 7’yi payda yapıp 2/3 + 5/7 almış.','bilgi'),(c3,'3/2 + 5/7 yazarak payı büyük kesirleri karıştırmış; paydaya küçük rakam koymuş.','bilgi'),(c4,'“En az” yerine “en çok” okuyup 7/2 + 5/3 yazmış.','dikkat')],
 tipId='rsy-yerlestirme',tip='Kutulara yerleştirme ve rasyonel gruplama',z='zor',alt='Kutulara Yerleştirme',kaz='Dört rakamı iki kesirde yerleştirerek toplamı en küçük yapan düzeni bulur.',kalip='düz',adim=4,
 kart='K-RSYN-08 (kutulara yerleştirme) · en küçük toplam için rakam yerleştirme',
 metin='Aşağıdaki işlemde her kutuya 2, 3, 5 ve 7 rakamlarından biri, her rakam birer kez kullanılmak üzere yazılıyor:\n□/□ + □/□\nBuna göre bu işlemin sonucu en az kaç olur?',
 istenen='İşlemin alabileceği en küçük değer.',ip=['Toplamın küçük olması için pay mı, payda mı büyük olmalı?'],bilgi=[GEN,KES],
 ad=[A('Pay ve paydaları seç','Kesirler küçük olsun diye küçük rakamlar (2, 3) paya, büyük rakamlar (5, 7) paydaya gider.','paylar: 2, 3 · paydalar: 5, 7'),A('Eşleştirmeleri dene','Hangi pay hangi paydanın üstünde olacak? İki durum var.','2/5 + 3/7 · 2/7 + 3/5'),A('Hesapla','Ortak payda 35.','2/5 + 3/7 = 14/35 + 15/35 = 29/35 · 2/7 + 3/5 = 10/35 + 21/35 = 31/35'),A('Karşılaştır','Küçük olanı seç.','29/35 en küçüktür')],
 puf='Toplamı küçültmek için payları küçük, paydaları büyük seç; aynı rakam kümesinde eşleştirmeleri hesapla.')

# ---------- 25 zor · depo göstergesi ----------
bol=Fr(48,8); kul=(5-2)*bol+12; km=kul/Fr('7.5')*100; assert bol==6 and kul==30 and km==400
e=[(kul-24)/Fr('7.5')*100,(kul-12)/Fr('7.5')*100,kul*Fr('7.5'),Fr(12+12)/Fr('7.5')*100]; assert e==[80,240,225,320] and len({km,*e})==5
mkf(P,'0025',km,[(e[0],'Eklenen 12 litreyi ve gösterge farkını yanlış birleştirip 6 L bulmuş (18 − 12).','islem'),(e[1],'Eklenen 12 litreyi hesaba katmamış; yalnız gösterge farkından 18 L bulmuş.','dikkat'),(e[2],'30 litreyi 7,5 ile çarpmış (7,5’e bölmesi gerekirdi).','islem'),(e[3],'Yolun sonunda kalan 2 bölmeyi (12 L) kullanılan yakıt sanıp eklenen 12 L ile toplamış.','dikkat')],
 tipId='rsy-olcum',tip='Günlük ölçüm: tarif, depo göstergesi, tartı',z='zor',alt='Gösterge Okuma',kaz='Bölmeli yakıt göstergesi ve ikmal bilgisinden harcanan yakıtı bulup yol uzunluğuna çevirir.',kalip='hikâyeli',adim=5,
 kart='K-RSYN-06 (günlük ölçüm) · bölmeli yakıt göstergesi, yolda ikmal, tüketim oranı',
 metin='Bir aracın 48 litrelik yakıt deposunun göstergesi, boş ile dolu arasında 8 eş bölmeye ayrılmıştır. Yola çıkılırken gösterge 5 bölmeyi göstermektedir. Yolculuk sırasında depoya bir kez 12 litre yakıt eklenmiş, başka ikmal yapılmamıştır; yolculuk sonunda gösterge 2 bölmeyi göstermektedir. Araç her 100 km’de 7,5 litre yakıt harcamaktadır.\nBuna göre araç bu yolculukta kaç km yol almıştır?',
 istenen='Alınan yol (km).',ip=['Başlangıç ile bitiş arasındaki yakıt azalmasını bul; eklenen yakıt da harcanmış yakıta katılır.'],bilgi=[GOS,B('Oran kurma','100 km’de 7,5 L harcanıyorsa t litre harcamak için yol = t ÷ 7,5 × 100 km. Örnek: 15 L → 15 ÷ 7,5 × 100 = 200 km')],
 ad=[A('Bir bölmenin değeri','48 litre 8 eş bölmeye ayrılmıştır.','48 ÷ 8 = 6 litre'),A('Göstergedeki azalma','Gösterge 5 bölmeden 2 bölmeye düşmüştür.','5 − 2 = 3 bölme = 3 × 6 = 18 litre'),A('Eklenen yakıt','Depoya yolda 12 litre eklendiği için harcanan yakıt, azalmadan 12 litre fazladır.','18 + 12 = 30 litre'),A('Yola çevir','100 km’de 7,5 litre harcandığına göre 30 litre kaç km yoldur?','30 ÷ 7,5 = 4'),A('Sonuç','4 tane 100 km’lik yol.','4 × 100 = 400 km')],
 puf='Gösterge sorularında harcanan yakıt = göstergedeki azalma + yolda eklenen yakıttır.')
# ---------- 26 zor · merdiven denklem ----------
xv=Fr(1); f=lambda x:2+1/(1+1/(x-Fr(1,2))); assert f(xv)==Fr(7,3)
e=[Fr(-1),Fr(1,2),Fr(5,6),Fr(0)]; assert all(f(t)!=Fr(7,3) for t in e if t!=Fr(1,2))
assert Fr(1,2)+Fr(1,3)==Fr(5,6)
mkf(P,'0026',xv,[(Fr(-1),'1/(1 + u) = 1/3 eşitliğinden 1 + u = 1/3 alıp u = −2/3, x = −1 bulmuş (ters almayı hatalı yapmış).','islem'),(Fr(1,2),'x − 1/2 = 1/2 bulup 1/2’yi eklemeyi unutarak x = 1/2 yazmış.','dikkat'),(Fr(5,6),'1 + u = 3’ten u = 3 alıp x − 1/2 = 1/3 yazmış (1’i çıkarmamış), x = 5/6.','islem'),(Fr(0),'x − 1/2 = 1/2’yi doğru bulmuş ama x’i 1/2 − 1/2 = 0 hesaplamış.','islem')],
 tipId='rsy-islem',tip='Dört işlem ve işlem önceliği',z='zor',alt='Bileşik Kesir',kaz='Merdiven biçimindeki kesir denkleminde bilinmeyeni dıştan içe çözer.',kalip='düz',adim=4,
 kart='K-RSYN-01 (merdiven kesir) · bilinmeyen en içte, dıştan içe çözüm',
 metin='2 + 1/(1 + 1/(x − 1/2)) = 7/3\neşitliğini sağlayan x değeri kaçtır?',
 istenen='x değeri.',ip=['Dıştan içe git: önce 2’yi çıkar, sonra tersleri al.'],bilgi=[TER],
 ad=[A('Dıştaki 2’yi çıkar','Eşitliğin iki yanından 2 çıkar.','1/(1 + 1/(x − 1/2)) = 7/3 − 2 = 1/3'),A('Ters al','Bir kesir 1/3 ise paydası 3’tür.','1 + 1/(x − 1/2) = 3'),A('1’i çıkar ve ters al','1’i çıkarınca 1/(x − 1/2) = 2 olur; tersini alınca x − 1/2 = 1/2 bulunur.','1 + 1/(x − 1/2) = 3 · 1/(x − 1/2) = 2 · x − 1/2 = 1/2'),A('x’i bul','1/2 ekle.','x = 1')],
 puf='İç içe kesir denkleminde dıştaki işlemleri tersleriyle sırayla kaldır; her adımda eşitliğin iki yanına aynı işlemi uygula.')

# ---------- 27 zor · seçim sayısı ----------
S=[Fr(1,2),Fr(1,3),Fr(1,4),Fr(1,6),Fr(1,12)]
sel=[c for r in range(1,6) for c in combinations(S,r) if sum(c)==1]; assert len(sel)==2 and sorted(len(c) for c in sel)==[3,4] and sum(len(c) for c in sel)==7 and sum(S)==Fr(4,3)
mk(P,'0027',tipId='rsy-yerlestirme',tip='Kutulara yerleştirme ve rasyonel gruplama',z='zor',alt='Rasyonel Gruplama',kaz='Kesirlerden toplamı 1 olan grupları sistemli bulur.',kalip='düz',adim=4,
 kart='K-RSYN-08 (rasyonel gruplama) · birim kesirlerden toplamı 1 olan gruplar',
 metin='Bir torbada 1/2, 1/3, 1/4, 1/6 ve 1/12 yazılı beş kart vardır. Üzerindeki sayıların toplamı 1 olan her farklı kart grubu için gruptaki kart sayısı bir listeye yazılıyor.\nBuna göre listedeki sayıların toplamı kaçtır?',
 dogru=7,yan=[(2,'Toplamı 1 olan grupların sayısını (2) vermiş; listedeki sayıların toplamı isteniyor.','dikkat'),(3,'Yalnız üç kartlı grubu (1/2 + 1/3 + 1/6) bulmuş.','dikkat'),(4,'Yalnız dört kartlı grubu bulmuş.','dikkat'),(5,'İki grupta geçen kartların birleşimini (tüm 5 kart) sayıp 5 yazmış.','dikkat')],
 istenen='Listedeki sayıların toplamı.',ip=['Beş kartın tüm toplamını bul; 1’e ulaşmak için dışarıda kalması gereken kartların toplamı ne olmalı?'],bilgi=[GEN],
 ad=[A('Tüm toplam','Paydayı 12’de eşitle.','6/12 + 4/12 + 3/12 + 2/12 + 1/12 = 16/12 = 4/3'),A('Dışarıda kalan','Toplamı 1 yapmak için dışarıda kalan kartların toplamı 4/3 − 1 = 1/3 olmalı.','dışarıda kalan toplam = 4/12'),A('Dışarıdakileri bul','Toplamı 4/12 olan gruplar.','{1/3} ya da {1/4, 1/12}'),A('Grupları yaz','Kalan kartlar bir grup oluşturur.','{1/2, 1/4, 1/6, 1/12}: 4 kart · {1/2, 1/3, 1/6}: 3 kart → 3 + 4 = 7')],
 puf='Toplamı verilen gruplarda, tüm toplamdan farkı kadar olan “dışarıda kalan” grubu bulmak aramayı kısaltır.')
bitir(P,'rasyonel','mat|Rasyonel Sayılar')
