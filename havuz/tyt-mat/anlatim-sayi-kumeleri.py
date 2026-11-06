"""Sayı Kümeleri 0001–0026: sıfırdan anlatım (koç standardı, 6 Kasım 2026).
Kullanım: python3 anlatim-sayi-kumeleri.py <parti.json> ...  → bilgi ve adimlar alanlarını yeniden yazar."""
import json,sys
B=lambda ad,ifade:dict(ad=ad,ifade=ifade)
TEK=B('Tek-çift kuralları','tek + tek = çift · çift + çift = çift · tek + çift = tek')
CARP=B('Çarpımda tek-çift','çarpanlardan biri çiftse çarpım çifttir; hepsi tekse çarpım tektir')
IKI=B('İki basamaklı sayı','AB = 10 × A + B (A onlar, B birler basamağı). Örnek: 74 = 10 × 7 + 4')
UC=B('Üç basamaklı sayı','ABC = 100 × A + 10 × B + C. Örnek: 352 = 300 + 50 + 2')
ASAL=B('Asal sayı','1’den büyük, yalnızca 1’e ve kendisine bölünen sayı: 2, 3, 5, 7, 11, 13, … 2, çift olan tek asal sayıdır')
FAK=B('Faktöriyel','n! = 1 × 2 × … × n. Örnek: 4! = 24. Ayrıca 6! = 6 × 5 × 4! gibi yazılabilir')
A=lambda b,a,i:dict(baslik=b,aciklama=a,islem=i)
Y={
'0001':([B('Rakam','0’dan 9’a kadar olan sembollerdir; sayılar rakamlarla yazılır')],[
 A('Tanımı anla','Denk sayıda rakamları toplayınca ve çarpınca **aynı sonuç** çıkar. Örnekteki 22 için ikisi de 4’tür.','2 + 2 = 4 · 2 × 2 = 4'),
 A('Büyük rakamları dene','Üç rakamın hepsi en az 2 olsun. En küçük durum 2, 2, 2: çarpım toplamdan şimdiden büyük. Rakamlar büyüdükçe çarpım daha da hızlı büyür, bu yüzden eşitlik olmaz.','2 + 2 + 2 = 6 · 2 × 2 × 2 = 8'),
 A('İki tane 1 olamaz','Rakamlar 1, 1, c olsun. Toplam c + 2, çarpım c olur; toplam hep 2 fazla kalır.','1 + 1 + c ≠ 1 × 1 × c'),
 A('Bir tane 1 olsun','Rakamlar 1, b, c olsun. b = 2 için 1 + 2 + c = 2 × c olmalı; buradan **c = 3** bulunur. b = 3 seçilirse c = 2 çıkar (yine 1, 2, 3); b = 4 ve üstünde c tam sayı çıkmaz.','1 + 2 + 3 = 6 · 1 × 2 × 3 = 6'),
 A('Sayıları yaz','1, 2 ve 3 rakamlarını üç basamağa farklı sıralarla yerleştir.','123, 132, 213, 231, 312, 321 ⇒ 6 sayı')]),
'0002':([TEK,CARP],[
 A('Verilenleri yaz','a × b + c **tek**, b × c + a **çift**. a’nın tek mi çift mi olduğunu deneyerek bulacağız.','a × b + c = tek · b × c + a = çift'),
 A('a tek olsaydı?','b × c + a çift ve a tek ise b × c de tek olmalı; yani b ve c ikisi de tek. O zaman a × b + c = tek + tek = **çift** olur, ama tek olması gerekiyordu.','çelişki ⇒ a tek olamaz'),
 A('a çifttir','a çift olduğuna göre a × b de çifttir.','a çift ⇒ a × b çift'),
 A('c’yi bul','a × b + c tek ve a × b çift ise c **tek** olmalı.','çift + c = tek ⇒ c tek'),
 A('b’yi bul','b × c + a çift ve a çift ise b × c çift olmalı. c tek olduğuna göre **b çift**.','b × tek = çift ⇒ b çift'),
 A('İfadeleri dene','a çift, b çift, c tek. b + c = çift + tek = tek; a + b = çift; a × c = çift.','yalnız I tek')]),
'0003':([B('Uçlar dahil dizilim','n tane nesne arasında n − 1 aralık vardır. Örnek: 3 direk ⇒ 2 aralık')],[
 A('Direk aralık sayısı','Bir uçtan öbür uca 7 direk varsa aralarında **6** boşluk vardır.','7 − 1 = 6 aralık'),
 A('Bir direk aralığı','3,6 metreyi 6 eşit parçaya böl.','3,6 ÷ 6 = 0,6 m'),
 A('4. direğin yeri','1. direk başlangıçtadır; 4. direğe gelmek için **3** aralık geçilir.','3 × 0,6 = 1,8 m'),
 A('Bir lamba aralığı','10 lamba arasında 9 aralık vardır.','3,6 ÷ 9 = 0,4 m'),
 A('6. lambanın yeri','6. lambaya gelmek için **5** aralık geçilir.','5 × 0,4 = 2,0 m'),
 A('Farkı al','İki konumun farkı istenen uzaklıktır.','2,0 − 1,8 = 0,2 m')]),
'0004':([B('Eşit bölmeli gösterge','her küçük aralık aynı değeri gösterir')],[
 A('Etiketleri bul','Göstergede yazılı iki değer var: 40 ve 60.','40 ve 60'),
 A('Aralıkları say','40 ile 60 arasındaki **boşlukları** say (çizgileri değil): 5 aralık var.','5 aralık'),
 A('Bir aralığın değeri','20 birimlik fark 5 eşit aralığa bölünmüş.','(60 − 40) ÷ 5 = 4'),
 A('Okun değeri','Ok, 40’tan başlayarak **8** aralık sağda.','40 + 8 × 4 = 72')]),
'0005':([],[
 A('Kaç sayı dışarıda?','7 sayıdan 6’sı kutulara yazılır; **1** sayı dışarıda kalır.','7 − 6 = 1'),
 A('Çarpmayı dene','Çarpımın sonucu da listede olmalı. 2 × 3 = 6 listede var; 2 × 4 = 8, 2 × 5 = 10, 3 × 4 = 12 gibi diğerleri yok.','2 × 3 = 6'),
 A('Kalanları yaz','2, 3 ve 6 kullanıldı.','kalanlar: 4, 5, 7, 9'),
 A('Toplamayı dene','Kalanlardan ikisinin toplamı üçüncüsü olmalı: 4 + 5 = 9 uyuyor (4 + 7 = 11, 5 + 7 = 12 listede yok).','4 + 5 = 9'),
 A('Dışarıda kalan','Kullanılmayan tek sayı kaldı.','7')]),
'0006':([IKI],[
 A('Şifreleri aç','AB ve BA sayılarını basamaklarına ayırarak yaz.','AB = 10A + B · BA = 10B + A'),
 A('Toplamı kullan','İki şifreyi topla: 11A + 11B = 121. İki tarafı 11’e böl.','A + B = 11'),
 A('Farkı kullan','Ece’ninkinden Can’ınkini çıkar: 9A − 9B = 27. İki tarafı 9’a böl.','A − B = 3'),
 A('A ve B’yi bul','İki denklemi topla: 2A = 14, yani **A = 7**; o zaman **B = 4**. Kontrol: 74 + 47 = 121, 74 − 47 = 27.','A = 7 · B = 4'),
 A('Çarp','İstenen A × B.','7 × 4 = 28')]),
'0007':([IKI,B('Gösterimler','⟨n⟩: rakamları topla, ⟨35⟩ = 8 · [n]: rakamları çarp, [35] = 15')],[
 A('İçten dışa çalış','⟨[AB]⟩ yazısında önce içteki [AB] yapılır, sonra dıştaki ⟨ ⟩.','önce iç, sonra dış'),
 A('İkinci koşuldan başla','⟨AB⟩ = A + B, en fazla 18’dir. [A + B] = 8 olması için A + B ya **8** olmalı ya da rakamları çarpımı 8 olan iki basamaklı **18**.','[8] = 8 · [18] = 1 × 8 = 8'),
 A('A + B = 18 dene','Bu yalnızca A = 9, B = 9 ile olur. Birinci koşulu kontrol et.','[99] = 81 ⇒ ⟨81⟩ = 9 ✓'),
 A('A + B = 8 dene','Sayılar: 17, 26, 35, 44, 53, 62, 71, 80. Rakam çarpımları 7, 12, 15, 16, 0; bunların rakam toplamı hiçbir zaman 9 olmuyor.','⟨7⟩, ⟨12⟩, ⟨15⟩, ⟨16⟩, ⟨0⟩ ≠ 9'),
 A('Sonuç','İki koşulu birlikte sağlayan tek sayı 99.','AB = 99')]),
'0008':([B('Ardışık çift sayılar','2’şer artar: 10, 12, 14, 16, …')],[
 A('En küçüğe x de','Beş sayı 2’şer artarak yazılır.','x, x + 2, x + 4, x + 6, x + 8'),
 A('Topla','x’ler ve sayılar ayrı ayrı toplanır.','5x + (2 + 4 + 6 + 8) = 5x + 20'),
 A('Denklemi kur','Toplam, en küçüğün (x) 6 katına eşit. İki taraftan 5x çıkar.','5x + 20 = 6x ⇒ x = 20'),
 A('En büyüğü bul','Soru en büyük sayıyı soruyor: x + 8.','20 + 8 = 28')]),
'0009':([B('Kesir karşılaştırma','paydalar eşitse payı büyük olan kesir büyüktür. Örnek: 5/12 = 50/120')],[
 A('Paydaları eşitle','2/5 ve 5/12’yi paydası 120 olacak şekilde genişlet (2/5’i 24 ile, 5/12’yi 10 ile).','2/5 = 48/120 · 5/12 = 50/120'),
 A('3/7’yi yerleştir','3/7 payda 120 ile tam yazılamaz; ondalık olarak yaklaşık 0,428’dir. Bu 51/120 (0,425) ile 52/120 arasına düşer.','3/7 ≈ 51,4/120'),
 A('Sınırları diz','Üç sınır sayı doğrusunda şöyle sıralanır.','48/120 < 50/120 < 51,4/120'),
 A('Şıkları dene','43, 45, 47 için hem Ali hem Cem yanılır (**iki yanlış**). 51 için kimse yanılmaz. 49 için yalnızca Cem yanılır (**tek yanlış**).','49/120 ✓')]),
'0010':([B('Parçanın parçası','kesirleri çarparız: bir dilimin 1/3’ü = 1/6 × 1/3')],[
 A('Bir dilim','Tepsi 6 eş dilim; bir dilim tepsinin altıda biri.','1/6'),
 A('Bir küçük parça','Bir dilim 3 eş parçaya bölünmüş.','1/6 × 1/3 = 1/18'),
 A('Dört parça','4 küçük parça ikram edilmiş. Sonucu sadeleştir (pay ve paydayı 2’ye böl).','4 × 1/18 = 4/18 = 2/9')]),
'0011':([B('Tutar','birim fiyat × miktar')],[
 A('Domates tutarı','12,40 × 2,5’i ikiye ayır: 2 kg ve 0,5 kg.','12,40 × 2 = 24,80 · 12,40 × 0,5 = 6,20 ⇒ 31'),
 A('Biber tutarı','18,60 × 1,5 = 18,60’ın kendisi + yarısı.','18,60 + 9,30 = 27,90'),
 A('Toplam tutar','İki tutarı topla.','31 + 27,90 = 58,90'),
 A('Para üstü','100 TL’den toplam tutarı çıkar.','100 − 58,9 = 41,1')]),
'0012':([B('Tekrar eden düzen','tam turlar sonucu değiştirmez; yalnızca artan (kalan) süreye bakılır')],[
 A('Bir tur','Yeşil, sarı ve kırmızı sürelerini topla.','40 + 5 + 30 = 75 sn'),
 A('Geçen süre','09.00.00’dan 09.17.20’ye 17 dakika 20 saniye geçer.','17 × 60 + 20 = 1040 sn'),
 A('Tam turları at','1040’ın içinde 13 tam tur var; artan süreyi bul.','13 × 75 = 975 ⇒ 1040 − 975 = 65 sn'),
 A('Turun içinde yer','Bir turda 0–40 yeşil, 40–45 sarı, 45–75 kırmızı. 65. saniye kırmızıdadır.','45 < 65 < 75 ⇒ kırmızı'),
 A('Kaç saniyedir yanıyor?','Kırmızı 45. saniyede yandı.','65 − 45 = 20 sn')]),
'0013':([IKI,UC],[
 A('Sayıları aç','Her sayıyı basamaklarına ayır.','AB = 10A + B · BC = 10B + C · CA = 10C + A'),
 A('Topla','Her harf bir kez 10 ile, bir kez 1 ile geçer.','AB + BC + CA = 11A + 11B + 11C'),
 A('Eşitsizliği sadeleştir','11A + 11B + 11C > 100A + 10B + C. İki taraftan 11A, 10B ve C çıkar.','B + 10C > 89A'),
 A('A’yı bul','Sol taraf en fazla 8 + 90 = 98 olabilir. A = 2 olsaydı 178’i geçmesi gerekirdi; imkânsız. O hâlde **A = 1**.','B + 10C > 89'),
 A('C’yi bul','C = 8 olsaydı sol taraf en fazla 9 + 80 = 89 olurdu, 89’dan büyük olamazdı. O hâlde **C = 9**.','C = 9'),
 A('En küçük ABC','B; 0, 1 ve 9 olamaz (rakamlar farklı ve sıfırdan farklı). En küçük seçenek **2**.','ABC = 129')]),
'0014':([B('1’den 9’a toplam','1 + 2 + … + 9 = 45')],[
 A('Kutu toplamı','Üç kutunun toplamı eşit; 45’i üçe böl.','45 ÷ 3 = 15'),
 A('9’un kutusu','9 ile birlikte iki kart daha var ve toplam 15; diğer ikisinin toplamı 6 olmalı: (1, 5) ya da (2, 4).','{1, 5, 9} veya {2, 4, 9}'),
 A('{1, 5, 9}’u dene','Kalan 2, 3, 4, 6, 7, 8 ile toplamı 15 olan üçlüler {2, 6, 7} ve {3, 4, 8}. İkisinde de ardışık kart var (6–7 ve 3–4).','olmaz ✗'),
 A('{2, 4, 9}’u dene','Kalan 1, 3, 5, 6, 7, 8 ile üçlüler {1, 6, 8} ve {3, 5, 7}. Hiçbir kutuda ardışık kart yok.','olur ✓'),
 A('Çarpımı bul','9’un kutusundaki kartlar 2, 4, 9.','2 × 4 × 9 = 72')]),
'0015':([B('3 katına çıkma','her sıra öncekinin 3 katı: 1, 3, 9, 27, 81, …')],[
 A('Sıraları yaz','1. sıradan başlayarak her sırayı 3 ile çarp.','1, 3, 9, 27, 81, 243, …'),
 A('Renkleri belirle','Tek numaralı sıralar (1., 3., 5.) mavi; çift numaralılar (2., 4.) beyaz.','mavi: 1, 9, 81 · beyaz: 3, 27'),
 A('Farkı biriktir','Mavileri ekle, beyazları çıkar; her yeni sırada farkı güncelle.','1 → −2 → 7 → −20 → 61'),
 A('Sıra sayısı','Fark 61 olduğunda **5** sıra vardır.','5 sıra'),
 A('Toplam kare','Beş sıradaki kareleri topla.','1 + 3 + 9 + 27 + 81 = 121')]),
'0016':([UC],[
 A('Sayıları aç','İki sayıyı basamaklarına ayır.','CBA = 100C + 10B + A · ABC = 100A + 10B + C'),
 A('Farkı al','CBA − ABC yapınca 10B’ler birbirini götürür.','99C − 99A = 99(C − A)'),
 A('C − A’yı bul','Fark 594 olduğuna göre 99’a böl.','594 ÷ 99 = 6 ⇒ C − A = 6'),
 A('A ve C ikilileri','A ve C sıfırdan farklı rakam; C, A’dan 6 fazla.','(1, 7), (2, 8), (3, 9)'),
 A('B’yi say','B; 1–9 arasında, A’dan ve C’den farklı olmalı: **7** seçenek.','9 − 2 = 7'),
 A('Toplam sayı','Her ikili için 7 farklı B var.','3 × 7 = 21')]),
'0017':([B('Ardışık tek / çift sayılar','2’şer artar: 15, 17 (tek) · 30, 32 (çift)')],[
 A('Duru’ya d de','Cem’in sayısı Duru’nunkinden 2 fazla.','Duru = d · Cem = d + 2'),
 A('Ayla ve Burak','Ayla, Duru’nun 2 katı; Burak, Ayla’dan 2 fazla.','Ayla = 2d · Burak = 2d + 2'),
 A('Toplamı yaz','Dört sayıyı topla ve 110’dan küçük olmalı.','d + (d + 2) + 2d + (2d + 2) = 6d + 4 < 110'),
 A('d’nin sınırı','6d < 106, yani d < 17,67. d iki basamaklı **tek** sayı: en büyük **17**.','d = 17'),
 A('Burak’ı bul','Burak = 2d + 2. Kontrol: 17, 19, 34, 36 toplamı 106 < 110.','2 × 17 + 2 = 36')]),
'0018':([TEK,B('3 ile çarpım','3 × tek = tek · 3 × çift = çift')],[
 A('Mesafe','5. basamaktan 46. basamağa çıkılıyor.','46 − 5 = 41 basamak'),
 A('Denklemi kur','x ikişerli, y üçerli adım olsun.','2x + 3y = 41'),
 A('y tek mi?','2x her zaman çift. Çift + 3y = 41 (tek) olması için 3y tek olmalı; bu da **y tek** demek. I doğru.','çift + tek = tek'),
 A('Tüm olasılıklar','y = 1, 3, 5, …, 13 için x = 19, 16, 13, 10, 7, 4, 1. Toplam adım x + y: 20, 19, 18, 17, 16, 15, 14.','x + y ∈ {14, …, 20}'),
 A('II ve III’ü dene','Toplam 19 gibi tek de olabilir: II kesin değil. Toplam hiçbir durumda 14’ten az değil: III doğru.','Doğrular: I ve III')]),
'0019':([ASAL,TEK],[
 A('Tek-çift dengesi','23 tek; x · y + z toplamında biri tek, biri çift olmalı.','tek = tek + çift'),
 A('Çift olan kim?','Çift asal sayı yalnızca 2. Ya z = 2 ya da x · y çift (x < y olduğundan x = 2).','z = 2 veya x = 2'),
 A('z = 2 durumu','x · y = 21 olmalı; 21 = 3 × 7.','3 + 7 + 2 = 12'),
 A('x = 2 durumu','2y + z = 23. y = 3 ⇒ z = 17; y = 5 ⇒ z = 13; y = 7 ⇒ z = 9 (asal değil); y = 11 ⇒ z = 1 (asal değil).','toplamlar 22 ve 20'),
 A('En küçüğü seç','Bulunan toplamlar 12, 20, 22.','en az 12')]),
'0020':([FAK],[
 A('(n + 1)!’i aç','(n + 1)!, n!’in (n + 1) katıdır.','(n + 1)! = (n + 1) × n!'),
 A('Ortak paranteze al','Sol tarafta iki terimde de n! var; dışarı al.','(n + 1) × n! − n! = n! × (n + 1 − 1) = n × n!'),
 A('n!’i aç','n! = n × (n − 1)! yazınca iki tarafta da (n − 1)! olur ve sadeleşir.','n × n × (n − 1)! = 25 × (n − 1)! ⇒ n² = 25'),
 A('n’yi bul','n pozitif olduğundan n = 5.','n = 5'),
 A('İstenen değer','Soru (n + 1)! = 6!’i soruyor.','6! = 1 × 2 × 3 × 4 × 5 × 6 = 720')]),
'0021':([B('Çarpımın işareti','çarpım pozitifse iki sayı aynı işaretli, negatifse zıt işaretlidir')],[
 A('b ve c','b · c > 0 olduğundan **b ve c aynı işaretli**.','b, c aynı işaret'),
 A('a','a · b < 0 olduğundan a, b’nin (ve c’nin) **zıt işaretli**.','a zıt işaret'),
 A('Hangi durum?','İki ihtimal var: a pozitif, b ve c negatif; ya da a negatif, b ve c pozitif. İkincisinde a > c olamaz (negatif sayı pozitiften büyük olamaz).','a > 0 · b < 0 · c < 0'),
 A('Şıkları dene','a · b · c = (+) × (−) × (−) = pozitif. a · c ve b + c negatif; a + b ile c − b’nin işareti sayılara bağlı.','a · b · c > 0')]),
'0022':([B('Basamak kuralı','bir sayı 0 ile başlayamaz; 02 iki basamaklı bir sayı değildir')],[
 A('Strateji','A − B’nin büyük olması için A mümkün olduğunca büyük, B mümkün olduğunca küçük olmalı.','A büyük · B küçük'),
 A('A’nın ilk iki basamağı','En büyük rakamlar 9 ve 7, A’nın yüzler ve onlar basamağına.','A = 97_'),
 A('En küçük B','Kalan 0, 2, 5. B’nin onlar basamağı 0 olamaz; en küçük B = 20.','B = 20'),
 A('A’yı tamamla','A’nın birler basamağına kalan rakam 5 gelir.','A = 975'),
 A('Farkı hesapla','Bulunan sayıları çıkar.','975 − 20 = 955')]),
'0023':([B('Bir sayının 4/9’u','önce 9’a böl, sonra 4 ile çarp')],[
 A('Dolu yerler','36’nın 4/9’u.','36 ÷ 9 × 4 = 16'),
 A('Görünen yerler','Kamera otoparkın tamamını görüyor; 12 yer kapalı.','36 − 12 = 24 görünen yer, 7’si dolu'),
 A('Kapalı alandaki dolular','Dolu yerlerin görünmeyenleri kamyonun arkasında.','16 − 7 = 9'),
 A('Kapalı alandaki boşlar','Kapalı 12 yerin 9’u dolu.','12 − 9 = 3')]),
'0024':([FAK],[
 A('6!/4!','6! = 6 × 5 × 4! olduğundan 4! sadeleşir.','6!/4! = 6 × 5 = 30'),
 A('3!','3 faktöriyel.','3! = 1 × 2 × 3 = 6'),
 A('Topla','İki sonucu topla.','30 + 6 = 36')]),
'0025':([ASAL,TEK],[
 A('Tek-çift dengesi','15 tek; iki sayının toplamı tekse biri tek, biri çifttir.','tek + çift = tek'),
 A('Çift asal','Çift olan tek asal sayı 2; diğer sayı 15 − 2 = 13 ve 13 asaldır.','a = 2 · b = 13'),
 A('Çarp','İki sayıyı çarp.','2 × 13 = 26')]),
'0026':([TEK,CARP],[
 A('k · e','e çift olduğundan çarpım çifttir.','tek × çift = çift'),
 A('k + e','Tek ile çiftin toplamı her zaman tektir.','tek + çift = tek ✓'),
 A('2k + e','2 ile çarpılan her sayı çifttir; çift + çift = çift.','2k + e = çift'),
 A('Diğer ikisi','k · e + e = çift + çift = çift; e² = e × e = çift.','k · e + e ve e² çift')]),
}
for f in sys.argv[1:]:
    Q=json.load(open(f))
    for q in Q:
        b,a=Y[q['id'][-4:]]; q['bilgi']=b; q['adimlar']=a
    json.dump(Q,open(f,'w'),ensure_ascii=False,indent=1)
print('ok')
