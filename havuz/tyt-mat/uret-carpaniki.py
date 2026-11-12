"""Çarpanlara Ayırma · parti 2 (hafif mod): 9 ana soru, kardeş yok, ipucu 1. Her cevap ve çeldirici kodla doğrulanır."""
import sys,os,math
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_mat as H
from _hafif_mat import *
H.KONU='Çarpanlara Ayırma'
P=Parti('carpaniki','Çarpanlara Ayırma','mat|Çarpanlara Ayırma')
UK='mat|Çarpanlara Ayırma'
IKF=B('İki kare farkı','a² − b² = (a − b) × (a + b). Örnek: 7² − 3² = 4 × 10 = 40')
TKO=B('Tam kare açılımları','(a + b)² = a² + 2ab + b² · (a − b)² = a² − 2ab + b². Örnek: (3 + 2)² = 9 + 12 + 4 = 25')
TERS=B('x ile 1/x’in çarpımı','x × 1/x = 1 olduğundan (x + 1/x)² = x² + 2 + 1/x² ve (x − 1/x)² = x² − 2 + 1/x²')
ORT=B('Ortak çarpan','her terimde bulunan çarpan parantez dışına alınır. Örnek: x²y + xy² = xy × (x + y)')
SAD=B('Sadeleştirme','pay ve paydayı çarpanlarına ayır, aynı çarpanları (sıfırdan farklı olduklarından) sadeleştir. Örnek: (x + 1)(x − 2)/((x + 1)(x + 3)) = (x − 2)/(x + 3)')
UCT=B('x² + bx + c ayrımı','çarpımı c, toplamı b olan iki sayı p ve q bulunursa x² + bx + c = (x + p)(x + q) olur. Örnek: x² + 5x + 6 = (x + 2)(x + 3), çünkü 2 × 3 = 6 ve 2 + 3 = 5')
CEV=B('Karenin çevresi ve alanı','kenarı a olan karenin çevresi 4a, alanı a² dir. Örnek: kenarı 5 olan karenin çevresi 20, alanı 25’tir')

KY='ÖSYM 2018–2026 TYT Matematik (özdeşlikler, çarpanlara ayırma) · yayın soru bankaları (yalnız mantık) · MEB 8–9. sınıf'
kart('K-CRPB-01','İki kare farkı','a² − b² = (a − b)(a + b) özdeşliği büyük sayılarda hızlı hesapta kullanılır.','Farkı (a − b)² sanmak; iki çarpanı toplamak; kareleri alırken işlem hatası yapmak.','kolay','düz',2,'cpb-ikikare','İki kare farkı: sayısal hesap',KY)
kart('K-CRPB-02','Tam kare ve x + 1/x','x + 1/x ya da x − 1/x verilir, kare alınarak x² + 1/x² bulunur; denklemden x + 1/x elde edilip kuvvet zinciri kurulur.','Kareyi alıp 2’yi çıkarmamak ya da eklemek; 2 yerine 4 çıkarmak; denklemi x’e bölmeyi akıl edememek.','orta','düz',3,'cpb-tamkare','Tam kare açılımı ve x + 1/x değerleri',KY)
kart('K-CRPB-03','Toplam–çarpım ilişkisi','(a + b)², (a − b)², a² + b² ve a × b arasındaki ilişkiden istenen büyüklük bulunur; öncüllü ifadeler çözümleyerek yorumlanır.','4ab yerine 2ab kullanmak; a² + b² ile (a + b)²’yi karıştırmak; a = b varsayımıyla öncülleri doğrulamak.','orta','düz',3,'cpb-toplamcarpim','(a + b)², (a − b)² ve a × b ilişkisi',KY)
kart('K-CRPB-04','Ortak çarpan','Toplam ve çarpım bilgisi ortak çarpan parantezine yerleştirilerek ifadenin değeri bulunur.','Ortak çarpanı alıp diğer çarpanı unutmak; parantezde fazladan terim bırakmak.','kolay','düz',3,'cpb-ortak','Ortak çarpan parantezine alma ve değer bulma',KY)
kart('K-CRPB-05','x² + bx + c ve sadeleştirme','İkinci dereceden üç terimliler ve iki kare farkı çarpanlarına ayrılır; rasyonel ifadelerin bölümü sadeleştirilerek yalınlaştırılır.','Bölmede ikinci kesri ters çevirmemek; çarpan işaretlerini yanlış yazmak; yalnız bir kesri sadeleştirmek.','zor','düz',5,'cpb-sadelestirme','Rasyonel ifade sadeleştirme (x² + bx + c ve iki kare farkı)',KY)
kart('K-CRPB-06','Geometrik yorum (sözle)','Kare alan farkı a² − b² ve çevre farkından kenarların farkı ve toplamı bulunur; şekil verilmeden sözlü kurgu çözülür.','Çevre farkını kenar farkı sanmak (4’e bölmemek); toplam yerine tek kenarı vermek.','orta','hikâyeli',3,'cpb-alan','Kare alan ve çevre farkı ile iki kare farkı',KY)
kart('K-CRPB-08','Gruplama ve tam sayı çarpan çiftleri','Dört terimli ifade gruplanarak (a + p)(b + q) = N biçimine getirilir; pozitif tam sayı çarpan çiftleri taranır.','Gruplarken işaret hatası; sağ tarafı sabit terimle düzeltmeyi unutmak; çarpan çiftlerinden pozitiflik koşuluna uymayanı saymak.','zor','düz',4,'cpb-gruplama','Gruplama ve tam sayı çarpan çiftleri',KY)
kart('K-CRPB-09','Tam kare üç terimli koşulu','x² + bx + c ifadesinin tam kare olması için orta terimin ±2√c olması gerekir; parametre değerleri iki işaretle bulunur.','Yalnız pozitif işareti almak; orta terimi 2 yerine 1 ile kurmak; parametreyi katsayıyla karıştırmak.','orta','düz',3,'cpb-uctam','Tam kare üç terimli koşulu',KY)
kart('K-CRPB-07','Öncüllü yorum','Toplam ve iki kare farkı verilen iki gerçel sayı için öncüllerin kesin doğruluğu çözümlenerek sınanır.','a = b gibi tek bir özel durumu denemekle yetinmek; a² + b² ile (a + b)²/2’yi karıştırmak.','orta','öncüllü',3,'cpb-oncullu','Öncüllü toplam–çarpım ilişkisi',KY)

# 01 kolay
assert 101**2-99**2==400==2*200 and (101-99)**2==4 and 101+99==200 and 2+200==202 and 99*99==9801 and 10201-9601==600
mk(P,'0001',tipId='cpb-ikikare',tip='İki kare farkı: sayısal hesap',z='kolay',alt='İki Kare Farkı',kaz='İki kare farkı özdeşliğiyle yakın iki sayının kareleri farkını hızlı hesaplar.',kalip='düz',adim=2,
 kart='K-CRPB-01 (iki kare farkı, sayısal hesap) · yeni sayılar: ardışık tek sayılar',
 metin='101² − 99²\nişleminin sonucu kaçtır?',
 dogru=400,yan=[(4,'(101 − 99)² = 4 işlemini yapmış; iki kare farkı (a − b)² değil, (a − b)(a + b)’dir.','bilgi'),(200,'Yalnız a + b = 200’ü yazmış; a − b = 2 çarpanını unutmuş.','dikkat'),(202,'İki çarpanı çarpmak yerine toplamış: 2 + 200.','islem'),(600,'Kareleri tek tek alırken 99² değerini 9601 bulmuş: 10 201 − 9601 = 600.','islem')],
 istenen='101² − 99² işleminin değeri.',
 ip=['Kareleri hesaplamadan a² − b² = (a − b)(a + b) özdeşliğini kullan.'],
 bilgi=[IKF],
 ad=[A('Özdeşliği uygula','a = 101, b = 99 olan iki kare farkıdır.','101² − 99² = (101 − 99) × (101 + 99)'),A('Çarp','Fark 2, toplam 200.','2 × 200 = 400'),A('Kontrol','Kareleri doğrudan hesaplayınca da aynı değer çıkar.','10 201 − 9801 = 400 ✓')],
 puf='Birbirine yakın iki sayının kareleri farkı istendiğinde kareleri alma; (fark) × (toplam) yaz.')

# 02 kolay
for x in [3+8**.5, 3-8**.5]:
    assert abs(x+1/x-6)<1e-9 and abs(x*x+1/x/x-34)<1e-9
assert 6**2==36 and 36-2==34 and 36+2==38 and 36-4==32 and 36-12==24
mk(P,'0002',tipId='cpb-tamkare',tip='Tam kare açılımı ve x + 1/x değerleri',z='kolay',alt='Tam Kare',kaz='x + 1/x değeri verildiğinde tam kare açılımıyla x² + 1/x² değerini bulur.',kalip='düz',adim=2,
 kart='K-CRPB-02 (tam kare, x + 1/x) · x + 1/x verilip x² + 1/x² isteniyor',
 metin='x sıfırdan farklı bir gerçel sayı olmak üzere\nx + 1/x = 6\nolduğuna göre x² + 1/x² kaçtır?',
 dogru=34,yan=[(32,'Kareyi alırken ortadaki terimi 2 yerine 4 almış: 36 − 4.','bilgi'),(36,'Eşitliğin karesini alıp ortadaki 2’yi çıkarmayı unutmuş.','dikkat'),(38,'Ortadaki 2’yi çıkarmak yerine eklemiş: 36 + 2.','islem'),(24,'Ortadaki 2 · x · 1/x terimini 2 · 6 = 12 sanıp 36 − 12 hesaplamış.','bilgi')],
 istenen='x² + 1/x² ifadesinin değeri.',
 ip=['Verilen eşitliğin her iki tarafının karesini al; x × 1/x = 1 olduğuna dikkat et.'],
 bilgi=[TKO,TERS],
 ad=[A('Karesini al','İki tarafın karesini alınca tam kare açılımı gelir.','(x + 1/x)² = 6² = 36'),A('Açılımı yaz','Ortadaki terim 2 × x × 1/x = 2’dir.','x² + 2 + 1/x² = 36'),A('Sonucu bul','2’yi karşı tarafa at.','x² + 1/x² = 36 − 2 = 34')],
 puf='x + 1/x verildiğinde karesini al; ortadaki terim her zaman 2’dir, sonuçtan 2 çıkar.')

# 03 orta
for a,b in [(7,2)]: pass
s3=[(a,b) for a in range(-30,31) for b in range(-30,31) if (a+b)**2==81 and (a-b)**2==25]
assert all(a*b==14 for a,b in s3) and len(s3)==4 and (81-25)//4==14 and 81-25==56 and (81-25)//2==28 and (81+25)//2==53 and 81+25==106
mk(P,'0003',tipId='cpb-toplamcarpim',tip='(a + b)², (a − b)² ve a × b ilişkisi',z='orta',alt='Özdeşlikler',kaz='(a + b)² ve (a − b)² değerlerinden iki sayının çarpımını bulur.',kalip='düz',adim=3,
 kart='K-CRPB-03 (toplam–çarpım ilişkisi) · iki karenin farkından 4ab',
 metin='İki gerçel sayının toplamının karesi 81, farkının karesi 25’tir.\nBuna göre bu iki sayının çarpımı kaçtır?',
 dogru=14,yan=[(56,'İki açılımı çıkarıp 4ab = 56 bulmuş ama 4’e bölmemiş.','dikkat'),(28,'İki açılımı çıkarınca 2ab = 56 sanıp 2’ye bölmüş; fark 4ab’dir.','bilgi'),(53,'İki açılımı toplayıp 2’ye bölmüş: (81 + 25)/2 = a² + b² değerini bulmuş.','bilgi'),(106,'İki açılımı toplayıp sonucu çarpım sanmış: 81 + 25.','islem')],
 istenen='a · b çarpımı.',
 ip=['İki açılımı alt alta yazıp çıkar; geriye hangi terim kalır?'],
 bilgi=[TKO],
 ad=[A('Açılımları yaz','İki karenin açılımı ortadaki işaretle ayrılır.','(a + b)² = a² + 2ab + b² · (a − b)² = a² − 2ab + b²'),A('Çıkar','a² ve b² terimleri birbirini götürür, 4ab kalır.','(a + b)² − (a − b)² = 4ab = 81 − 25 = 56'),A('Çarpımı bul','4’e böl.','ab = 56 ÷ 4 = 14')],
 puf='(a + b)² − (a − b)² = 4ab ve (a + b)² + (a − b)² = 2(a² + b²) özdeşliklerini ezberle; çarpım ya da kareler toplamı hemen çıkar.',
 kisa='(a + b)² − (a − b)² = 4ab olduğundan çarpım (81 − 25)/4 diye tek satırda bulunur.')

# 04 orta
s4=[(x,y) for x in range(-20,21) for y in range(-20,21) if x+y==6 and x*y==8]
assert s4==[(2,4),(4,2)] and all(x*x*y+x*y*y==48 for x,y in s4) and 8*6==48 and 8+6==14 and 6**2==36 and 48+8==56
mk(P,'0004',tipId='cpb-ortak',tip='Ortak çarpan parantezine alma ve değer bulma',z='kolay',alt='Ortak Çarpan',kaz='Ortak çarpan parantezine alarak toplam ve çarpım verilen ifadenin değerini bulur.',kalip='düz',adim=2,
 kart='K-CRPB-04 (ortak çarpan) · x + y ve xy’den x²y + xy²',
 metin='x ve y gerçel sayılar olmak üzere\nx + y = 6\nx · y = 8\nolduğuna göre x²y + xy² ifadesinin değeri kaçtır?',
 dogru=48,yan=[(8,'xy’yi parantez dışına alıp (x + y) çarpanını yazmayı unutmuş.','dikkat'),(14,'x²y + xy² yerine xy + (x + y) hesaplamış: 8 + 6.','islem'),(36,'İfadeyi (x + y)² sanmış: 6².','bilgi'),(56,'xy ortak çarpanını alırken parantezde bir xy fazladan bırakıp xy(x + y) + xy = 48 + 8 hesaplamış.','islem')],
 istenen='x²y + xy² ifadesinin değeri.',
 ip=['İki terimde ortak olan çarpanı parantez dışına al.'],
 bilgi=[ORT],
 ad=[A('Ortak çarpanı al','İki terimde de x ve y vardır.','x²y + xy² = xy × (x + y)'),A('Değerleri yerine koy','Verilen çarpım ve toplam yazılır.','8 × 6 = 48'),A('Kontrol','x = 2, y = 4 için: 4 × 4 + 2 × 16.','16 + 32 = 48 ✓')],
 puf='Terimleri tek tek bulmaya çalışma; ortak çarpanı parantez dışına alınca verilen toplam ve çarpım doğrudan yerine geçer.')

# 05 zor
f=lambda x:Fr(x*x-2*x-15,x*x-25)/Fr(x*x+6*x+9,x*x-9)
g=lambda x:Fr(x-3,x+5)
bad={'(x + 3)/(x + 5)':lambda x:Fr(x+3,x+5),'(x − 3)/(x − 5)':lambda x:Fr(x-3,x-5),'(x + 5)/(x − 3)':lambda x:Fr(x+5,x-3),'(x + 3)²/((x + 5)(x − 3))':lambda x:Fr((x+3)**2,(x+5)*(x-3))}
xs=[x for x in range(-40,41) if x not in(-5,-3,3,5)]
assert all(f(x)==g(x) for x in xs)
for k,h in bad.items(): assert any(h(x)!=f(x) for x in xs),k
assert all(Fr(x*x-2*x-15,x*x-25)==Fr(x+3,x+5) and Fr(x*x+6*x+9,x*x-9)==Fr(x+3,x-3) for x in xs)
assert all(Fr(x*x-2*x-15,x*x-25)*Fr(x*x+6*x+9,x*x-9)==bad['(x + 3)²/((x + 5)(x − 3))'](x) for x in xs)
dg='(x − 3)/(x + 5)'
mk(P,'0005',tipId='cpb-sadelestirme',tip='Rasyonel ifade sadeleştirme (x² + bx + c ve iki kare farkı)',z='zor',alt='Rasyonel İfadeler',kaz='İki rasyonel ifadenin bölümünü çarpanlara ayırarak en sade biçime getirir.',kalip='düz',adim=5,
 kart='K-CRPB-05 (x² + bx + c ve sadeleştirme) · iki rasyonel ifadenin bölümü',
 metin='x’in ifadeyi tanımlı yapan her değeri için\n(x² − 2x − 15)/(x² − 25) ÷ (x² + 6x + 9)/(x² − 9)\nişleminin sonucu aşağıdakilerden hangisidir?',
 dogru=dg,sira=['(x + 3)/(x + 5)','(x − 3)/(x − 5)','(x + 5)/(x − 3)','(x + 3)²/((x + 5)(x − 3))',dg],
 yan=[('(x + 3)/(x + 5)','Yalnız birinci kesri sadeleştirip ikinci kesrin bölme etkisini unutmuş.','dikkat'),('(x − 3)/(x − 5)','x² − 25’ten (x − 5) yerine (x + 5) çarpanını sadeleştirmiş; kalan çarpanı (x − 5) yazmış.','islem'),('(x + 5)/(x − 3)','Bölmede ikinci kesri ters çevirdikten sonra sonucu da bir kez daha ters çevirmiş.','islem'),('(x + 3)²/((x + 5)(x − 3))','Bölmeyi çarpma gibi yapmış; ikinci kesri ters çevirmemiş.','bilgi')],
 istenen='İşlemin en sade biçimi.',
 ip=['Dört ifadenin hepsini çarpanlarına ayır; bölmeyi ikinci kesri ters çevirerek çarpmaya çevir.'],
 bilgi=[UCT,IKF,SAD],
 ad=[A('Birinci kesri ayır','x² − 2x − 15 = (x − 5)(x + 3) ve x² − 25 = (x − 5)(x + 5).','(x − 5)(x + 3) / ((x − 5)(x + 5)) = (x + 3)/(x + 5)'),A('İkinci kesri ayır','x² + 6x + 9 = (x + 3)² ve x² − 9 = (x − 3)(x + 3).','(x + 3)² / ((x − 3)(x + 3)) = (x + 3)/(x − 3)'),A('Bölmeyi çarpmaya çevir','İkinci kesri ters çevirip çarp.','(x + 3)/(x + 5) × (x − 3)/(x + 3)'),A('Sadeleştir','(x + 3) çarpanı sadeleşir.','(x − 3)/(x + 5)')],
 puf='Rasyonel bölmelerde önce her pay ve paydayı çarpanlarına ayır, sonra ikinci kesri ters çevirip sadeleştir.')

# 06 orta
s6=[(a,b) for a in range(1,100) for b in range(1,a) if 4*a-4*b==24 and a*a-b*b==168]
assert s6==[(17,11)] and 17+11==28 and 28//2==14 and 24//4==6
mk(P,'0006',tipId='cpb-alan',tip='Kare alan ve çevre farkı ile iki kare farkı',z='orta',alt='Kare Alan Farkı',kaz='Kare biçimli iki bahçenin çevre ve alan farkından kenarları bularak iki kare farkı özdeşliğini kullanır.',kalip='hikâyeli',adim=3,
 kart='K-CRPB-06 (geometrik yorum, sözle) · iki kare bahçenin çevre ve alan farkı',
 metin='Kare biçimli iki bahçeden büyüğünün çevresi küçüğünün çevresinden 24 m, alanı ise küçüğünün alanından 168 m² fazladır.\nBuna göre küçük bahçenin bir kenarı kaç metredir?',
 dogru=11,yan=[(6,'Çevre farkı olan 24’ü 4’e bölüp yalnızca kenar farkını (6) bulmuş.','dikkat'),(14,'Kenar toplamının yarısını (28/2) küçük kenar sanmış; kenarlar farklı olduğundan yarısı olmaz.','islem'),(17,'Büyük bahçenin kenarını bulup küçük bahçeyi sorulduğunu unutmuş.','dikkat'),(28,'Kenarlar toplamını (a + b) bulup durmuş.','dikkat')],
 istenen='Küçük bahçenin bir kenarı (m).',
 ip=['Kenarlar a ve b ise çevre farkından a − b, alan farkından a² − b² bilgisini yaz.'],
 bilgi=[CEV,IKF],
 ad=[A('Kenar farkını bul','Çevre farkı 4 × (a − b) kadardır.','4 × (a − b) = 24 → a − b = 6'),A('İki kare farkı','Alan farkı a² − b² = (a − b)(a + b) dir.','6 × (a + b) = 168 → a + b = 28'),A('Kenarları çöz','Toplam ve farktan küçük kenarı bul.','2b = 28 − 6 = 22 → b = 11'),A('Kontrol','Büyük kenar 17, alanlar farkı 168.','17² − 11² = 289 − 121 = 168 ✓')],
 puf='Kare biçimli iki şeklin alan farkı ile çevre farkı verilirse kenar farkını çevreden, kenar toplamını iki kare farkından bul.')

# 07 orta öncüllü
s7=[(a,b) for a in range(-30,31) for b in range(-30,31) if a+b==6 and a*a-b*b==12]
assert s7==[(4,2)] and 4-2==2 and 4*2==8 and 16+4==20 and 6**2//2==18
mk(P,'0007',tipId='cpb-oncullu',tip='Öncüllü toplam–çarpım ilişkisi',z='orta',alt='Özdeşlikler',kaz='Toplam ve iki kare farkı verilen iki sayının fark, çarpım ve kareler toplamını çözümleyip öncülleri değerlendirir.',kalip='öncüllü',adim=3,
 kart='K-CRPB-07 (öncüllü yorum) · a + b = 6 ve a² − b² = 12',
 metin='a ve b gerçel sayılar olmak üzere\na + b = 6\na² − b² = 12\nolduğuna göre,\nI. a − b = 2\nII. a · b = 8\nIII. a² + b² = 18\nifadelerinden hangileri kesinlikle doğrudur?',
 dogru='I ve II',sira=['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III'],
 yan=[('Yalnız I','a = 4 ve b = 2’yi bulmuş ama a · b yerine a + b = 6 hesaplayıp II’yi, a² + b² = 20 bulup III’ü doğru saymamış.','islem'),('Yalnız II','a = 4 ve b = 2’yi bulmuş; I’i sınarken a − b yerine b − a = −2 hesaplayıp I’i yanlış saymış.','islem'),('I ve III','a² + b² değerini (a + b)²/2 = 18, a · b değerini (a + b)²/4 = 9 sanıp III’ü doğru, II’yi yanlış saymış.','bilgi'),('I, II ve III','a = 4, b = 2 bulduktan sonra a² + b² yerine (a + b)²/2 = 18 hesaplayıp III’ü de doğru kabul etmiş.','bilgi')],
 istenen='Kesinlikle doğru olan ifadeler.',
 ip=['a² − b² = (a − b)(a + b) yazıp a − b’yi bul; sonra a ve b’yi çöz.'],
 bilgi=[IKF],
 ad=[A('Farkı bul','İki kare farkından a − b bulunur.','(a − b) × 6 = 12 → a − b = 2'),A('Sayıları çöz','Toplam 6, fark 2.','a = 4 · b = 2'),A('Öncülleri sına','I: 4 − 2 = 2 doğru. II: 4 × 2 = 8 doğru. III: 16 + 4 = 20, 18 değil.','I doğru · II doğru · III yanlış'),A('Sonuç','Kesinlikle doğru olanlar I ve II.','I ve II')],
 puf='Toplam ve iki kare farkı verilince fark hemen çıkar; sayıları bulduktan sonra her öncülü tek tek sına.')

# 08 zor · gruplama
s8=[(a,b) for a in range(1,200) for b in range(1,200) if a*b-3*a+2*b==18]
assert s8==[(1,7),(2,6),(4,5),(10,4)] and all((a+2)*(b-3)==12 for a,b in s8) and max(a*b for a,b in s8)==40
assert sorted(a*b for a,b in s8)==[7,12,20,40] and 12*4==48 and 6*5==30 and 4*5==20
mk(P,'0008',tipId='cpb-gruplama',tip='Gruplama ve tam sayı çarpan çiftleri',z='zor',alt='Gruplama',kaz='Dört terimli ifadeyi gruplayıp çarpan çiftlerini tarayarak pozitif tam sayı çözümlerinin çarpımını bulur.',kalip='düz',adim=4,
 kart='K-CRPB-08 (gruplama, tam sayı çarpan çiftleri) · ab − 3a + 2b = 18',
 metin='a ve b pozitif tam sayılar olmak üzere\nab − 3a + 2b = 18\neşitliğini sağlayan (a, b) ikilileri için a · b çarpımının en büyük değeri kaçtır?',
 dogru=40,yan=[(12,'(a + 2)(b − 3) = 12 yazıp sağ taraftaki 12’yi çarpımın cevabı sanmış.','dikkat'),(20,'(4, 5) çiftinde durup a + 2 = 12 durumunu (a = 10, b = 4) atlamış.','dikkat'),(30,'a + 2 = 6 ve b − 3 = 2 çiftinde a’yı 6 alıp 6 × 5 hesaplamış; a + 2 = 6 ise a = 4’tür.','islem'),(48,'a + 2 = 12 ve b − 3 = 1 çiftinde a’yı 12 alıp 12 × 4 hesaplamış; a = 10’dur.','islem')],
 istenen='a · b çarpımının en büyük değeri.',
 ip=['Sabit terimi tamamlayarak eşitliği (a + 2)(b − 3) = sayı biçimine getir.'],
 bilgi=[B('Gruplama','dört terimli ifadede ikişer terimi grupla, ortak çarpanı al. Örnek: ab + 2a + 3b + 6 = a(b + 2) + 3(b + 2) = (a + 3)(b + 2)')],
 ad=[A('Gruplamaya hazırla','ab − 3a + 2b ifadesine −6 eklenirse (a + 2)(b − 3) çarpımı elde edilir.','(a + 2)(b − 3) = ab − 3a + 2b − 6'),A('Sabiti taşı','Eşitliğin iki yanından 6 çıkar.','ab − 3a + 2b − 6 = 18 − 6 → (a + 2)(b − 3) = 12'),A('Çarpan çiftleri','a + 2 ≥ 3 ve b − 3 pozitif olmalı.','3 × 4 · 4 × 3 · 6 × 2 · 12 × 1'),A('Çarpımları bul','a + 2 = 3, 4, 6, 12 için (a, b) = (1, 7), (2, 6), (4, 5), (10, 4).','7, 12, 20, 40 → en büyüğü 40')],
 puf='Dört terimli ifadede eksik sabiti iki yana ekleyerek (x + p)(y + q) = N biçimine getir; sonra N’nin çarpan çiftlerini pozitiflik koşuluna göre tara.')

# 09 orta · tam kare koşulu
ms=[m for m in range(-60,61) if (m-2)**2-36==0]
assert ms==[-4,8] and ms[0]*ms[1]==-32 and 6*-6==-36 and sum(ms)==4
mk(P,'0009',tipId='cpb-uctam',tip='Tam kare üç terimli koşulu',z='orta',alt='Tam Kare',kaz='Üç terimlinin tam kare olma koşulundan parametrenin değerlerini bulup çarpımını hesaplar.',kalip='düz',adim=3,
 kart='K-CRPB-09 (tam kare üç terimli koşulu) · x² + (m − 2)x + 9',
 metin='m bir gerçel sayı olmak üzere\nx² + (m − 2)x + 9\nifadesi bir tam karedir.\nBuna göre m’nin alabileceği değerlerin çarpımı kaçtır?',
 dogru=-32,yan=[(-36,'m − 2 değerlerinin (6 ve −6) çarpımını almış; sorulan m değerleridir.','dikkat'),(4,'m değerlerinin çarpımı yerine toplamını (8 + (−4)) almış.','dikkat'),(8,'Yalnız m − 2 = 6 durumunu alıp tek değer bulmuş.','dikkat'),(32,'m = 8 ve m = −4 değerlerini çarparken işareti kaçırmış.','islem')],
 istenen='m değerlerinin çarpımı.',
 ip=['x² + (m − 2)x + 9 = (x ± 3)² biçiminde olmalı; orta terim 2 × x × 3’ün iki işaretli hâlidir.'],
 bilgi=[TKO],
 ad=[A('Tam kareyi yaz','Son terim 9 = 3² olduğundan ifade (x + 3)² ya da (x − 3)² olmalı.','(x ± 3)² = x² ± 6x + 9'),A('Orta terimi eşitle','m − 2 = 6 ya da m − 2 = −6.','m = 8 ya da m = −4'),A('Çarp','İki değerin çarpımı.','8 × (−4) = −32')],
 puf='Tam kare üç terimlide orta terim, ilk ve son terimin köklerinin çarpımının ±2 katıdır; iki işareti de dene.')

bitir(P,'carpaniki',UK)
