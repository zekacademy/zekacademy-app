"""Fonksiyonlar · parti 2 (hafif mod): 14 ana soru, kardeş yok, ipucu 1. Her cevap ve çeldirici kodla doğrulanır."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_mat as H
from _hafif_mat import *
from itertools import product
H.KONU='Fonksiyonlar'
UK='matd|Fonksiyonlar'
P=Parti('fonkiki','Fonksiyonlar',UK)
KY='ÖSYM 2018–2026 TYT Matematik (fonksiyonlar) · yayın soru bankaları (yalnız mantık) · MEB 10. sınıf'
DEG=B('Fonksiyonda değer','f(x + k) biçiminde verilen kuralda f(a) için x + k = a olacak biçimde x bulunur ve kurala yazılır. Örnek: f(x + 1) = 2x ise f(5) için x = 4 alınır, f(5) = 8')
DOG=B('Doğrusal fonksiyon','f(x) = ax + b ve a = (f(x₂) − f(x₁)) / (x₂ − x₁) eğimidir; sonra b bir noktadan bulunur. Örnek: f(1) = 3, f(3) = 7 ise a = 2, b = 1 ve f(x) = 2x + 1')
BIL=B('Bileşke fonksiyon','(f ∘ g)(x) = f(g(x)) olup önce g, sonra f uygulanır. Örnek: f(x) = x + 1, g(x) = 2x ise (f ∘ g)(3) = f(6) = 7 ve (g ∘ f)(3) = g(4) = 8')
TERS=B('Ters fonksiyon','y = f(x) eşitliğinde x yalnız bırakılırsa f⁻¹ bulunur; f⁻¹(b) = a ile f(a) = b aynı şeydir. Örnek: f(x) = 2x + 4 için x = (y − 4)/2 olduğundan f⁻¹(6) = 1')
BIR=B('Birebir ve örten','Birebir fonksiyonda farklı elemanların görüntüleri farklıdır; örten fonksiyonda değer kümesinin her elemanı en az bir elemanın görüntüsüdür. Örnek: A = {1, 2}, B = {a, b} için f(1) = a, f(2) = b birebir ve örtendir')
SAY=B('Fonksiyon sayısı','s(A) = m ve s(B) = n ise A’dan B’ye nᵐ tane fonksiyon vardır; her eleman için görüntü n seçenekten seçilir. Örnek: A = {1, 2}, B = {a, b, c} için 3² = 9 fonksiyon')
PAR=B('Tablodan okuma','Tabloda f(a) değeri, x = a sütunundaki sayıdır; f⁻¹(b) ise f(x) = b olan sütunun x değeridir. Örnek: x = 1, 2 için f(x) = 5, 7 ise f(2) = 7 ve f⁻¹(5) = 1')
PARC=B('Parçalı fonksiyon','Fonksiyonun kuralı x’in bulunduğu aralığa göre seçilir; iç içe değerlerde önce içteki hesaplanır, sonucun aralığına bakılır. Örnek: f(x) = x + 1 (x < 2), 3x (x ≥ 2) ise f(f(1)) = f(2) = 6')

kart('K-FNB-01','Fonksiyonda değer bulma','f(x + k) biçiminde verilen kuraldan istenen noktadaki değer bulunur.','x yerine istenen sayıyı doğrudan yazmak; k’yı ters yönde çıkarmak.','kolay','düz',2,'fnb-deger','Fonksiyonda değer: f(x + k)',KY)
kart('K-FNB-02','Doğrusal fonksiyon ve doğrusal model','İki noktadan eğim ve kural; hikâyeli doğrusal modelde sabit ücret ve birim ücret.','Eğimi bulup sabit terimi unutmak; sabit terimi verilen değer sanmak.','orta','düz',3,'fnb-dogrusal','Doğrusal fonksiyon ve model',KY)
kart('K-FNB-03','Bileşke ve ters fonksiyon','Bileşke fonksiyonun kuralı ve değeri; doğrusal fonksiyonun tersi.','Bileşke sırasını ters almak; ters alırken işlem işaretini yanlış çevirmek.','orta','düz',3,'fnb-bileske','Bileşke ve ters fonksiyon',KY)
kart('K-FNB-04','Birebir, örten ve fonksiyon sayısı','Sonlu kümelerde eşleme, birebir–örten ayrımı ve koşullu fonksiyon sayısı.','Eleman sayılarını ters çarpmak; koşulları birbirine karıştırmak.','orta','düz',3,'fnb-eslesme','Eşleme, birebir ve örten, fonksiyon sayısı',KY)
kart('K-FNB-05','Parçalı ve tablo ile verilen fonksiyon','Parçalı kuralda doğru aralık seçimi; tablodan değer ve ters değer okuma.','Aralığa bakmadan tek kural uygulamak; f⁻¹ yerine f okumak.','orta','tablo',3,'fnb-tablo','Parçalı fonksiyon ve tablo',KY)
kart('K-FNB-06','Doğrusal fonksiyonun kendisiyle bileşkesi','f(f(x)) = px + q verilen doğrusal f’nin kuralı katsayı karşılaştırmasıyla bulunur.','Artan/azalan koşulunu yok sayıp işaret seçmek; sabit terimi atlamak.','zor','düz',4,'fnb-ffx','Doğrusal fonksiyonun kendisiyle bileşkesi',KY)

# 01
f1=lambda x:3*(x-2)-1  # f(x+2)=3x-1 -> f(t)=3(t-2)-1
assert f1(5)==8 and 3*5-1==14 and 3*7-1==20 and 3*5-1+2==16 and 3*4-1==11
mk(P,'0001',tipId='fnb-deger',tip='Fonksiyonda değer: f(x + k)',z='kolay',alt='Fonksiyonda Değer',kaz='f(x + k) kuralı verilen fonksiyonda istenen noktadaki değeri bulur.',kalip='düz',adim=2,
 kart='K-FNB-01 · f(x + 2) = 3x − 1',
 metin='Gerçel sayılarda tanımlı f fonksiyonu için\nf(x + 2) = 3x − 1\neşitliği veriliyor.\nBuna göre f(5) kaçtır?',
 dogru=8,yan=[(11,'x + 2 = 5 için x yerine 4 yazmış (2 yerine 1 çıkarmış).','dikkat'),(14,'Kuraldaki x yerine doğrudan 5 yazmış: 3 · 5 − 1.','bilgi'),(16,'Doğrudan 3 · 5 − 1 = 14 bulup 2’yi eklemiş.','bilgi'),(20,'x + 2 = 5 için x’i 5 + 2 = 7 almış.','dikkat')],
 istenen='f(5).',
 ip=['Parantezin içi 5 olacak biçimde x’in değerini bul.'],
 bilgi=[DEG],
 ad=[A('x’i bul','x + 2 = 5 olmalı.','x = 3'),A('Kurala yaz','x = 3 için.','f(5) = 3 · 3 − 1'),A('Hesapla','İşlemi yap.','9 − 1 = 8')],
 puf='f(x + k) = … verildiğinde istenen noktayı x + k’ya eşitleyip x’i bul, sonra kurala yaz.')

# 02
a=Fr(14-5,4-1); b=5-a*1; f2=lambda x:a*x+b; assert (a,b)==(3,2) and f2(10)==32 and 3*10==30 and 3*10+5==35 and 5*10==50 and 14+3*10==44
mk(P,'0002',tipId='fnb-dogrusal',tip='Doğrusal fonksiyon ve model',z='kolay',alt='Doğrusal Fonksiyon',kaz='İki noktası verilen doğrusal fonksiyonun kuralını bulup değer hesaplar.',kalip='düz',adim=3,
 kart='K-FNB-02 · iki noktadan doğrusal fonksiyon',
 metin='Gerçel sayılarda tanımlı f doğrusal bir fonksiyondur.\nf(1) = 5\nf(4) = 14\nolduğuna göre f(10) kaçtır?',
 dogru=32,yan=[(30,'Eğimi bulup sabit terimi hesaplamamış: 3 · 10.','dikkat'),(35,'Sabit terimi f(1) = 5 sanmış: 3 · 10 + 5.','bilgi'),(44,'Eğimi bulup f(4) = 14 değerine 3 · 10 eklemiş.','bilgi'),(50,'f(1) = 5’i eğim sanıp 5 · 10 hesaplamış.','bilgi')],
 istenen='f(10).',
 ip=['Doğrusal fonksiyonu f(x) = ax + b yazıp iki noktayı kullan.'],
 bilgi=[DOG],
 ad=[A('Eğimi bul','Değer farkı ÷ x farkı.','a = (14 − 5)/(4 − 1) = 3'),A('Sabiti bul','f(1) = 5 noktası.','3 + b = 5 → b = 2'),A('Değeri hesapla','f(x) = 3x + 2.','f(10) = 32')],
 puf='Doğrusal fonksiyonda önce eğimi, sonra bir noktadan sabit terimi bul.')

# 03
cnt=sum(1 for _ in product(range(3),repeat=4)); assert cnt==81 and 4**3==64 and 3*4==12 and 4*3*2==24 and 3+4==7
mk(P,'0003',tipId='fnb-eslesme',tip='Eşleme, birebir ve örten, fonksiyon sayısı',z='kolay',alt='Fonksiyon Sayısı',kaz='Sonlu kümeler arasında tanımlanabilecek fonksiyon sayısını bulur.',kalip='düz',adim=2,
 kart='K-FNB-04 · A → B fonksiyon sayısı',
 metin='A = {1, 2, 3, 4} ve B = {a, b, c} kümeleri veriliyor.\nA’dan B’ye tanımlanabilen kaç farklı fonksiyon vardır?',
 dogru=81,yan=[(7,'Eleman sayılarını toplamış: 4 + 3.','bilgi'),(12,'Kartezyen çarpımın eleman sayısını (4 · 3) vermiş.','bilgi'),(24,'Her elemana farklı görüntü seçilir sanıp azalan seçenekleri sayarak 4 · 3 · 2 hesaplamış.','dikkat'),(64,'Üs ile taban yer değiştirmiş: 4³.','bilgi')],
 istenen='Fonksiyon sayısı.',
 ip=['A’nın her elemanı için görüntüsünün kaç seçeneği olduğunu düşün.'],
 bilgi=[SAY],
 ad=[A('Her eleman için seçenek','1, 2, 3 ve 4’ün her biri B’nin 3 elemanından birine gider.','3 seçenek × 4 eleman'),A('Çarp','Seçimler birbirinden bağımsız.','3 · 3 · 3 · 3'),A('Hesapla','Çarpımı bul.','3⁴ = 81')],
 puf='Fonksiyon sayısı, değer kümesinin eleman sayısının tanım kümesinin eleman sayısı kadar kuvvetidir.')

# 04
a4=Fr(12,3); assert a4==4; b4=5-a4*2; f4=lambda x:a4*x+b4
assert f4(10)==37 and 4*10+5==45 and 5+12*8==101 and 5+12==17 and 5+8==13
mk(P,'0004',tipId='fnb-dogrusal',tip='Doğrusal fonksiyon ve model',z='orta',alt='Doğrusal Fonksiyon',kaz='Eşit aralıklardaki değer farkından eğimi bulup doğrusal fonksiyonun değerini hesaplar.',kalip='düz',adim=3,
 kart='K-FNB-02 · f(x + 3) − f(x) farkı',
 metin='Gerçel sayılarda tanımlı f doğrusal bir fonksiyondur.\nf(x + 3) − f(x) = 12\nf(2) = 5\nolduğuna göre f(10) kaçtır?',
 dogru=37,yan=[(13,'Eğimi hesaba katmayıp x farkı kadar (10 − 2 = 8) f(2)’ye eklemiş: 5 + 8.','dikkat'),(17,'12 farkını bir kez f(2)’ye eklemiş.','dikkat'),(45,'f(2) = 5’i sabit terim sanıp 4 · 10 + 5 hesaplamış.','bilgi'),(101,'12’yi eğim sanıp 5 + 12 · 8 hesaplamış.','bilgi')],
 istenen='f(10).',
 ip=['f(x) = ax + b için f(x + 3) − f(x) ifadesini a cinsinden yaz.'],
 bilgi=[DOG],
 ad=[A('Eğimi bul','f(x + 3) − f(x) = a(x + 3) + b − ax − b = 3a.','3a = 12 → a = 4'),A('Sabiti bul','f(2) = 5.','8 + b = 5 → b = −3'),A('Değeri hesapla','f(x) = 4x − 3.','f(10) = 37')],
 puf='Doğrusal fonksiyonda x, h kadar artınca değer a · h kadar artar; farktan eğime ulaşılır.')

# 05
g5=lambda x:2*x+3; f5=lambda x:2*x-1
assert all(f5(g5(x))==4*x+5 for x in range(-5,6)) and g5(5)==13 and (4*5+5-1)//2==12 and Fr(4*5+5,2)==Fr(25,2) and f5(5)==9 and g5(f5(5))==21
mk(P,'0005',tipId='fnb-bileske',tip='Bileşke ve ters fonksiyon',z='orta',alt='Bileşke Fonksiyon',kaz='Bileşke fonksiyonun kuralı ve bir fonksiyon verildiğinde diğerinin kuralını bulur.',kalip='düz',adim=3,
 kart='K-FNB-03 · (f ∘ g)(x) verilmiş, g aranıyor',
 metin='Gerçel sayılarda tanımlı f ve g fonksiyonları için\nf(x) = 2x − 1\n(f ∘ g)(x) = 4x + 5\nolduğuna göre g(5) kaçtır?',
 dogru=13,yan=[(9,'g(5) yerine f(5) değerini hesaplamış.','dikkat'),(12,'2g(x) − 1 = 4x + 5 denkleminde −1’i taşırken işareti ters çevirmiş: g(x) = (4x + 5 − 1)/2.','islem'),(Fr(25,2),'−1 terimini hiç hesaba katmayıp g(x) = (4x + 5)/2 bulmuş.','islem'),(21,'g(5) yerine (g ∘ f)(5) = g(f(5)) hesaplamış.','bilgi')],
 istenen='g(5).',
 ip=['(f ∘ g)(x) = f(g(x)) olduğundan f kuralında x yerine g(x) yaz.'],
 bilgi=[BIL],
 ad=[A('Bileşkeyi aç','f(g(x)) = 2g(x) − 1.','2g(x) − 1 = 4x + 5'),A('g(x)’i bul','−1’i diğer tarafa at, 2’ye böl.','g(x) = 2x + 3'),A('Değeri hesapla','x = 5.','g(5) = 13')],
 puf='(f ∘ g)(x) = f(g(x)) olduğundan f’nin kuralında x yerine g(x) yazıp g(x)’i yalnız bırak.')

# 06
fi=lambda y:(3*y+1)/2
f6=lambda x:Fr(2*x-1,3); assert f6(fi(Fr(7)))==7 and fi(7)==11
assert (3*7-1)//2==10 and 2*7-1==13 and 3*7==21 and 3*7+1==22
mk(P,'0006',tipId='fnb-bileske',tip='Bileşke ve ters fonksiyon',z='orta',alt='Ters Fonksiyon',kaz='Doğrusal fonksiyonun tersinin kuralını bulup değer hesaplar.',kalip='düz',adim=3,
 kart='K-FNB-03 · kesirli doğrusal fonksiyonun tersi',
 metin='f: ℝ → ℝ, birebir ve örten bir fonksiyon olup\nf(x) = (2x − 1)/3\nkuralıyla tanımlanıyor.\nBuna göre f⁻¹(7) kaçtır?',
 dogru=11,yan=[(10,'Ters kuralı bulurken +1’i −1 yapmış: (3 · 7 − 1)/2.','islem'),(13,'f’nin payını (2 · 7 − 1) hesaplamış; ters almamış.','bilgi'),(21,'Yalnızca 3 ile çarpıp +1 ve 2’ye bölme adımlarını yapmamış.','islem'),(22,'3 · 7 + 1 bulup 2’ye bölmeyi unutmuş.','islem')],
 istenen='f⁻¹(7).',
 ip=['f⁻¹(7) = a ise f(a) = 7 olur; bu denklemi kur.'],
 bilgi=[TERS],
 ad=[A('Denklemi kur','f⁻¹(7) = a ise f(a) = 7.','(2a − 1)/3 = 7'),A('Çöz','Önce 3 ile çarp, sonra 1 ekle, 2’ye böl.','2a − 1 = 21 → 2a = 22 → a = 11'),A('Kontrol','f(11) = (22 − 1)/3.','f(11) = 7 ✓')],
 puf='f⁻¹(b) = a eşitliği f(a) = b ile aynıdır; ters kuralı bulmak yerine f(a) = b denklemini çözebilirsin.')

# 07
sols=[(a_,b_) for a_ in (0,2) for b_ in (1,2) if sorted([a_+1,5,2*b_-1,7])==[1,3,5,7] and a_>b_]; assert sols==[(2,1)]
assert 3*2+1==7 and 3*0+2==2 and 2+1==3 and 3*3+1==10 and 3*2+0==6
tb7=tablo_svg(['x','1','2','3','4'],[['f(x)','a + 1','5','2b − 1','7']])
mk(P,'0007',tipId='fnb-eslesme',tip='Eşleme, birebir ve örten, fonksiyon sayısı',z='orta',alt='Birebir ve Örten',kaz='Birebir ve örten fonksiyonun tablosundan bilinmeyen değerleri eşleyerek ifade değerini bulur.',kalip='tablo',adim=4,sekil=tb7,
 kart='K-FNB-04 · tabloda birebir ve örten eşleme',
 metin='A = {1, 2, 3, 4} ve B = {1, 3, 5, 7} kümeleri için f: A → B fonksiyonu aşağıdaki tabloda verilmiştir.\nf birebir ve örten bir fonksiyondur ve a > b dir.\nBuna göre 3a + b kaçtır?',
 dogru=7,yan=[(2,'Eşlemeyi ters seçip a + 1 = 1 ve 2b − 1 = 3 almış (a < b); a > b koşulunu sınamamış.','dikkat'),(3,'Sorulan ifadeyi yanlış okuyup a + b değerini vermiş.','dikkat'),(6,'2b − 1 = 1 denkleminde −1’i karşıya −1 olarak atıp 2b = 1 − 1 = 0, b = 0 bulmuş; a = 2 ile 3a + b = 6.','islem'),(10,'a + 1 = 3 yerine a = 3 almış: 3 · 3 + 1.','islem')],
 istenen='3a + b.',
 ip=['Değer kümesinin tüm elemanları tabloda tam bir kez bulunmalı; hangi değerler a + 1 ve 2b − 1’e kalıyor?'],
 bilgi=[BIR],
 ad=[A('Kalan değerler','Tabloda 5 ve 7 var; B’den 1 ve 3 kalıyor.','a + 1 ve 2b − 1 sayıları 1 ile 3’tür'),A('İki durum','Durum 1: a + 1 = 3, 2b − 1 = 1 → a = 2, b = 1. Durum 2: a + 1 = 1, 2b − 1 = 3 → a = 0, b = 2.','a > b yalnız Durum 1’de sağlanır'),A('İfade','a = 2, b = 1.','3a + b = 7')],
 puf='Birebir ve örten fonksiyonda değer kümesinin her elemanı tam bir kez kullanılır; kalan değerlerle ek koşulu sınayarak eşlemeyi belirle.')

# 08
def fn_all():
    return list(product(range(3),repeat=4))
F=fn_all(); inj=[f for f in F if len(set(f))==4]; sur=[f for f in F if len(set(f))==3]
assert len(inj)==0 and len(sur)>0 and len(sur)<len(F)
mk(P,'0008',tipId='fnb-eslesme',tip='Eşleme, birebir ve örten, fonksiyon sayısı',z='orta',alt='Birebir ve Örten',kaz='Eleman sayıları farklı iki küme arasındaki fonksiyonlarda birebirlik ve örtenlik olasılıklarını yorumlar.',kalip='öncüllü',adim=3,
 kart='K-FNB-04 · 4 elemanlı kümeden 3 elemanlı kümeye',
 metin='A = {1, 2, 3, 4} ve B = {a, b, c} kümeleri için f: A → B bir fonksiyondur.\nBuna göre,\nI. f birebir olabilir.\nII. f örten olabilir.\nIII. f örten olmak zorundadır.\nifadelerinden hangileri doğrudur?',
 dogru='Yalnız II',sira=['Yalnız II','Yalnız III','I ve II','II ve III','I, II ve III'],
 yan=[('Yalnız III','II’de 4 elemanın 3 elemana örten gidemeyeceğini sanıp yanlış bulmuş; III’ü “örten olmayan fonksiyon olmaz” diye doğru saymış.','dikkat'),('I ve II','I’de A’nın 4 elemanının B’nin 3 elemanına birebir gidebileceğini sanmış; III’ü yanlış bulmuş.','bilgi'),('II ve III','III’ü doğru saymış (her fonksiyonun örten olduğunu sanmış); I’i yanlış bulmuş.','dikkat'),('I, II ve III','Üç ifadeyi de “olabilir” diye okuyup hepsini doğru saymış.','dikkat')],
 istenen='Doğru olan ifadeler.',
 ip=['A’nın eleman sayısı B’ninkinden fazla; her ifadede “olabilir” mi “zorunlu” mu diye ayırıp küçük örnek fonksiyonlar dene.'],
 bilgi=[BIR],
 ad=[A('I. ifade','4 eleman, 3 farklı görüntüye sığmaz; iki eleman aynı görüntüye gider.','I yanlış'),A('II. ifade','f(1) = a, f(2) = b, f(3) = c, f(4) = a örten bir fonksiyondur.','II doğru'),A('III. ifade','f(1) = f(2) = f(3) = f(4) = a sabit fonksiyonu örten değildir.','III yanlış'),A('Sonuç','Yalnız II doğrudur.','Yalnız II')],
 puf='Tanım kümesi daha kalabalıksa birebir fonksiyon olmaz; “olabilir” ve “zorunlu” ifadelerini bir örnek fonksiyonla ayrı ayrı sına.')

# 09
def f9(x):
    if x<0: return 4-x*x
    if x<3: return 3*x+1
    return 12-x
assert f9(-1)==3 and f9(2)==7 and f9(7)==5 and f9(-1)+f9(f9(2))==8
assert 3+(3*7+1)==25 and (3*(-1)+1)+5==3 and 3+7==10 and 3+f9(4-4)==4 and f9(4-4)==1
mk(P,'0009',tipId='fnb-tablo',tip='Parçalı fonksiyon ve tablo',z='orta',alt='Parçalı Fonksiyon',kaz='Üç parçalı fonksiyonda iç içe değeri aralıklara bakarak hesaplar.',kalip='düz',adim=4,
 kart='K-FNB-05 · üç parçalı fonksiyon, f(−1) + f(f(2))',
 metin='Gerçel sayılarda tanımlı f fonksiyonu\nf(x) = 4 − x², x < 0 ise\nf(x) = 3x + 1, 0 ≤ x < 3 ise\nf(x) = 12 − x, x ≥ 3 ise\nbiçiminde veriliyor.\nBuna göre f(−1) + f(f(2)) toplamı kaçtır?',
 dogru=8,yan=[(3,'f(−1) için aralığa bakmayıp 3x + 1 kuralını uygulamış (−2); f(7) = 5’i doğru bulmuş.','dikkat'),(4,'f(2) için aralığa bakmayıp 4 − x² uygulamış (f(2) = 0), f(0) = 1 bulmuş.','dikkat'),(10,'f(f(2)) yerine f(2) = 7 değerini toplamış.','dikkat'),(25,'f(7) için 3x + 1 kuralını uygulamış (22).','dikkat')],
 istenen='f(−1) + f(f(2)).',
 ip=['Her değerde önce x’in hangi aralıkta olduğuna bak; iç içe olanda içteki sonucun aralığına da bak.'],
 bilgi=[PARC],
 ad=[A('f(−1)','−1 < 0 olduğundan ilk kural.','4 − 1 = 3'),A('f(2)','0 ≤ 2 < 3 olduğundan ikinci kural.','3 · 2 + 1 = 7'),A('f(7)','7 ≥ 3 olduğundan üçüncü kural.','12 − 7 = 5'),A('Topla','f(−1) + f(f(2)).','3 + 5 = 8')],
 puf='Parçalı fonksiyonda her adımda x’in aralığını kontrol et; iç içe değerde önce içteki sonucun aralığına bak.')

# 10
tf={1:3,2:4,3:5,4:1,5:2}; inv={v:k for k,v in tf.items()}
assert len(inv)==5 and tf[tf[2]]==1 and inv[2]==5 and tf[tf[2]]+inv[2]==6 and 1+2==3 and 1+tf[2]==5 and tf[2]+inv[2]==9 and tf[2]+tf[2]==8
tb10=tablo_svg(['x','1','2','3','4','5'],[['f(x)','3','4','5','1','2']])
mk(P,'0010',tipId='fnb-tablo',tip='Parçalı fonksiyon ve tablo',z='kolay',alt='Tablo ile Fonksiyon',kaz='Tabloyla verilen birebir ve örten fonksiyonda bileşke ve ters değerleri okur.',kalip='tablo',adim=3,sekil=tb10,
 kart='K-FNB-05 · tabloda f(f(2)) ve f⁻¹(2)',
 metin='A = {1, 2, 3, 4, 5} kümesinde tanımlı f fonksiyonu aşağıdaki tabloda verilmiştir.\nf birebir ve örten olduğuna göre f(f(2)) + f⁻¹(2) toplamı kaçtır?',
 dogru=6,yan=[(3,'f⁻¹(2) yerine 2 yazıp f(f(2)) = 1 ile toplamış.','dikkat'),(5,'f⁻¹(2) yerine f(2) = 4 okumuş: 1 + 4.','bilgi'),(8,'f(f(2)) yerine f(2) = 4 alıp f⁻¹(2) yerine de f(2) = 4 okumuş.','bilgi'),(9,'f(f(2)) yerine tek adım f(2) = 4 alıp f⁻¹(2) = 5 ile toplamış.','dikkat')],
 istenen='f(f(2)) + f⁻¹(2).',
 ip=['f⁻¹(2) için tabloda f(x) satırında 2’nin bulunduğu sütunun x değerine bak.'],
 bilgi=[PAR],
 ad=[A('f(f(2))','f(2) = 4, sonra f(4).','f(f(2)) = f(4) = 1'),A('f⁻¹(2)','f(x) = 2 olan x.','f(5) = 2 olduğundan f⁻¹(2) = 5'),A('Topla','İki değeri topla.','1 + 5 = 6')],
 puf='Tabloda f(a) için a sütununa, f⁻¹(b) için f(x) satırında b’nin olduğu sütuna bak.')

# 11
fr=lambda t:3*t+4; gr=lambda x:2*x-5
assert all(fr(2*x+1)==6*x+7 for x in range(-5,6))
a11=[a_ for a_ in range(-200,200) if gr(Fr(a_-4,3))==7]; assert a11==[22]
assert 43==6*6+7
assert fr(7)==25 and gr(15)==25 and 3*6+7==25 and fr(6)==22
mk(P,'0011',tipId='fnb-bileske',tip='Bileşke ve ters fonksiyon',z='zor',alt='Bileşke ve Ters',kaz='f(2x + 1) biçiminde verilen kuraldan f(x)’i bulup bileşke ve ters fonksiyon koşulundan bilinmeyeni hesaplar.',kalip='düz',adim=4,
 kart='K-FNB-03 · f(2x + 1) kuralı, g ∘ f⁻¹',
 metin='Gerçel sayılarda tanımlı f ve g fonksiyonları için\nf(2x + 1) = 6x + 7\ng(x) = 2x − 5\nveriliyor. f birebir ve örtendir.\n(g ∘ f⁻¹)(a) = 7 olduğuna göre a kaçtır?',
 dogru=22,yan=[(6,'f⁻¹(a) = 6 bulup a yerine bu değeri vermiş.','dikkat'),(15,'(g ∘ f⁻¹)(a) yerine (f⁻¹ ∘ g)(a) = 7 okumuş: g(a) = f(7) = 25, a = 15.','bilgi'),(25,'f(x) kuralını f(x) = 3x + 7 bulup f(6) hesaplamış.','islem'),(43,'6x + 7’yi doğrudan f(x) sanıp f(6) hesaplamış.','bilgi')],
 istenen='a.',
 ip=['Önce 2x + 1 = t diyerek f(t) kuralını bul; sonra g ile ters fonksiyonu sırayla çöz.'],
 bilgi=[DEG,BIL,TERS],
 ad=[A('f(x)’i bul','2x + 1 = t → x = (t − 1)/2.','f(t) = 6 · (t − 1)/2 + 7 = 3t + 4'),A('g’yi çöz','g(f⁻¹(a)) = 7.','2 · f⁻¹(a) − 5 = 7 → f⁻¹(a) = 6'),A('a’yı bul','f⁻¹(a) = 6 ise a = f(6).','a = 3 · 6 + 4 = 22'),A('Kontrol','f⁻¹(22) = 6, g(6) = 7.','7 ✓')],
 puf='f(2x + 1) biçiminde verilen kuralda 2x + 1 = t dönüşümü yap; bileşkeyi içten dışa doğru aç.')

# 12
sol=[(a_,b_) for a_ in range(-6,7) for b_ in range(-20,21) if a_>0 and a_*a_==4 and a_*b_+b_==9]; assert sol==[(2,3)]
f12=lambda x:2*x+3; assert all(f12(f12(x))==4*x+9 for x in range(-5,6)) and f12(11)==25
assert -2*11-9==-31 and (11-3)//2==4 and 2*11-3==19 and 2*11==22 and (-2)*(-9)+(-9)==9
mk(P,'0012',tipId='fnb-ffx',tip='Doğrusal fonksiyonun kendisiyle bileşkesi',z='zor',alt='Bileşke Fonksiyon',kaz='Doğrusal fonksiyonun kendisiyle bileşkesinden kuralı bulup değer hesaplar.',kalip='düz',adim=4,
 kart='K-FNB-06 · (f ∘ f)(x) = 4x + 9, f artan doğrusal',
 metin='Gerçel sayılarda tanımlı f, artan ve doğrusal bir fonksiyondur.\n(f ∘ f)(x) = 4x + 9\nolduğuna göre f(11) kaçtır?',
 dogru=25,yan=[(-31,'“Artan” koşulunu yok sayıp a = −2 almış: f(x) = −2x − 9.','dikkat'),(4,'f(11) yerine f⁻¹(11) değerini hesaplamış.','dikkat'),(19,'f(x) = 2x + 3 bulduktan sonra sabit terimin işaretini ters alıp 2 · 11 − 3 hesaplamış.','islem'),(22,'Sabit terimi bulmayıp yalnızca a = 2 ile 2 · 11 hesaplamış.','dikkat')],
 istenen='f(11).',
 ip=['f(x) = ax + b yazıp f(f(x)) ifadesini a ve b cinsinden aç; x’li ve sabit terimleri ayrı ayrı eşitle.'],
 bilgi=[DOG,BIL],
 ad=[A('Bileşkeyi aç','f(f(x)) = a(ax + b) + b.','a²x + ab + b = 4x + 9'),A('a’yı bul','x’in katsayıları eşit; f artan olduğundan a > 0.','a² = 4 → a = 2'),A('b’yi bul','Sabit terimler eşit.','2b + b = 9 → b = 3'),A('Değeri hesapla','f(x) = 2x + 3.','f(11) = 25')],
 puf='Doğrusal fonksiyonun kendisiyle bileşkesinde x’in katsayısından eğimi, sabit terimden b’yi bul; “artan” koşulu işareti belirler.')

# 13
cnt=sum(1 for f in product(range(5),repeat=4) if f[0]==f[1] and f[2]!=f[3]); assert cnt==100
assert 5*5*1==25 and 5*5*5==125 and 5*5*5*4==500 and 5**4==625 and 5*4==20
mk(P,'0013',tipId='fnb-eslesme',tip='Eşleme, birebir ve örten, fonksiyon sayısı',z='orta',alt='Fonksiyon Sayısı',kaz='İki koşulu birlikte sağlayan fonksiyonların sayısını seçimleri çarparak bulur.',kalip='düz',adim=4,
 kart='K-FNB-04 · f(1) = f(2) ve f(3) ≠ f(4)',
 metin='A = {1, 2, 3, 4} ve B = {a, b, c, d, e} kümeleri veriliyor.\nA’dan B’ye tanımlanan f fonksiyonlarından f(1) = f(2) ve f(3) ≠ f(4) koşullarını sağlayan kaç tanesi vardır?',
 dogru=100,yan=[(25,'f(3) ≠ f(4) koşulunu f(3) = f(4) okuyup 5 · 5 · 1 = 25 bulmuş.','dikkat'),(125,'f(3) ≠ f(4) koşulunu uygulamayıp f(3) ve f(4) için 5 · 5 seçenek saymış.','dikkat'),(500,'f(1) = f(2) koşulunu uygulamayıp f(1) ve f(2) için 5 · 5 seçenek saymış.','dikkat'),(625,'Koşulları uygulamadan tüm fonksiyonları (5⁴) saymış.','dikkat')],
 istenen='Koşulları sağlayan fonksiyon sayısı.',
 ip=['f(1) = f(2) olduğunda bu iki eleman için kaç seçim yapılır? f(3) seçildikten sonra f(4) kaç şekilde seçilir?'],
 bilgi=[SAY],
 ad=[A('f(1) = f(2)','İkisi aynı görüntüye gider.','5 seçenek'),A('f(3)','Serbest.','5 seçenek'),A('f(4)','f(3)’ten farklı olmalı.','4 seçenek'),A('Çarp','Seçimler bağımsız.','5 · 5 · 4 = 100')],
 puf='Koşullu fonksiyon sayısında her elemanın seçenek sayısını koşula göre belirleyip çarp.')

# 14
A_=lambda x:60+38*x; B_=lambda x:114+28*x
k=min(x for x in range(0,100) if B_(x)<A_(x)); assert k==6 and A_(6)-B_(6)==6
assert B_(5)-A_(5)==4 and A_(7)-B_(7)==16 and 38-28==10 and 114-60==54
mk(P,'0014',tipId='fnb-dogrusal',tip='Doğrusal fonksiyon ve model',z='zor',alt='Doğrusal Model',kaz='İki doğrusal ücret modelini karşılaştırıp tam sayı koşuluyla ücret farkını hesaplar.',kalip='hikâyeli',adim=4,
 kart='K-FNB-02 · iki taksinin ücret karşılaştırması',
 metin='Bir taksi durağında iki araç vardır. A aracı açılışta 60 TL, ardından her kilometre için 38 TL almaktadır. B aracı açılışta 114 TL, ardından her kilometre için 28 TL almaktadır. Ücretler yalnızca tam kilometre üzerinden hesaplanmaktadır.\nBir yolcu, B aracının A aracından daha ucuz olduğu en küçük tam sayı kilometrelik yolculuğu yapıyor.\nBuna göre iki aracın bu yolculuk için aldığı ücretler arasındaki fark kaç TL’dir?',
 dogru=6,yan=[(4,'Dönüm noktasını 5,4 km bulup 5 km almış; bu yolculukta B daha pahalı olur, farkı 4 TL bulmuş.','dikkat'),(10,'Kilometre başına ücret farkını (38 − 28) cevap sanmış.','dikkat'),(16,'Dönüm noktasından sonra bir kilometre fazla alıp 7 km için farkı bulmuş.','dikkat'),(54,'Açılış ücretleri arasındaki farkı (114 − 60) cevap sanmış.','dikkat')],
 istenen='Ücret farkı (TL).',
 ip=['Her aracın ücretini kilometre sayısı x cinsinden yaz; x için eşitsizlik kur ve tam sayı koşulunu unutma.'],
 bilgi=[B('Doğrusal ücret modeli','Sabit ücret + birim ücret × miktar biçimindeki ücret f(x) = ax + b ile yazılır. Örnek: açılış 20 TL, km başına 10 TL ise 3 km için f(3) = 20 + 30 = 50 TL')],
 ad=[A('Ücretleri yaz','x kilometre için.','A(x) = 60 + 38x · B(x) = 114 + 28x'),A('Eşitsizliği çöz','B(x) < A(x).','114 + 28x < 60 + 38x → 54 < 10x → x > 5,4 → en küçük tam sayı x = 6'),A('Ücretleri bul','x = 6.','A(6) = 288 · B(6) = 282'),A('Farkı al','A(6) − B(6).','288 − 282 = 6 TL')],
 puf='İki doğrusal modeli karşılaştırırken eşitsizliği çöz ve sonucu tam sayıya yuvarlarken yönüne dikkat et.')

bitir(P,'fonkiki',UK)
