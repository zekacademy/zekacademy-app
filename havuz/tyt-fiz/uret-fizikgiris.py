import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif as H
from _hafif import *
H.KONU='Fizik Bilimine Giriş'
P=Parti('fizikgiris','Fizik Bilimine Giriş','fiz|Fizik Bilimine Giriş',ders='TYT Fizik',idon='tytfiz')
KY='ÖSYM 2018–2025 (fiziksel nicelikler, bilimsel yöntem) · MEB 9. sınıf'
kart('K-FZGR-01','Niceliklerin sınıflandırılması','Temel nicelikler (uzunluk, kütle, zaman, sıcaklık…) başka niceliklerden türetilmez; yönü olan nicelikler vektörel, olmayanlar skalerdir.','Enerjiyi ya da sıcaklığı vektörel sanmak; hızı temel nicelik sanmak.','kolay','düz',2,'fz-gr-siniflama','Temel, türetilmiş, skaler ve vektörel nicelikler',KY)
kart('K-FZGR-02','Birim türetme','Türetilmiş niceliğin birimi, tanım bağıntısından temel birimlerle çıkarılır.','Bağıntıdaki zaman üssünü yanlış almak.','orta','düz',3,'fz-gr-birim','Birim türetme',KY)
kart('K-FZGR-03','Birim dönüşümü','SI birimine çevirirken her büyüklüğün çevirme katsayısı ayrı alınır: 1 dm³ = 1000 cm³ = 10⁻³ m³.','Hacim birimlerinde 10’un üssünü yanlış almak.','orta','hikâyeli',3,'fz-gr-donusum','Özkütlede birim dönüşümü',KY)
kart('K-FZGR-04','Kontrollü deney','Bir etkeni incelemek için yalnız o etken değiştirilir, diğerleri sabit tutulur.','Birden çok etkenin değiştiği deneyleri karşılaştırmak.','zor','tablo',4,'fz-gr-deney','Kontrollü deney tasarımı',KY)
# ---- 0001
mk(P,'0001',tipId='fz-gr-siniflama',tip='Temel, türetilmiş, skaler ve vektörel nicelikler',z='kolay',alt='Fiziksel Niceliklerin Sınıflandırılması',kaz='Fiziksel nicelikleri temel–türetilmiş ve skaler–vektörel olarak sınıflandırır.',kalip='düz',adim=2,
 kart='K-FZGR-01 (niceliklerin sınıflandırılması) · hem türetilmiş hem vektörel',
 metin='Aşağıdaki fiziksel niceliklerden hangisi hem türetilmiş hem de vektörel bir niceliktir?',
 dogru='Hız',sira=['Sıcaklık','Hız','Enerji','Kütle','Uzunluk'],yan=[('Sıcaklık','Sıcaklığı hem türetilmiş hem vektörel sanmış; sıcaklık temel ve skaler bir niceliktir.','bilgi'),('Enerji','Enerjinin türetilmiş olduğunu bilmiş ama yönü olmadığını (skaler) görmemiş.','bilgi'),('Kütle','Kütle temel ve skalerdir; hiçbir koşulu sağlamaz.','bilgi'),('Uzunluk','Uzunluk temel bir niceliktir ve yönü yoktur.','bilgi')],
 istenen='Hem türetilmiş hem vektörel olan nicelik.',
 ip=['Önce hangi seçeneklerin temel nicelik olduğunu ele; kalanlardan yönü olanı bul.'],
 bilgi=[B('Temel ve türetilmiş nicelikler','temel nicelikler (uzunluk, kütle, zaman, sıcaklık, akım şiddeti…) başka niceliklerden türetilemez; türetilmiş nicelikler temel niceliklerden oluşur. Örnek: hız = yer değiştirme ÷ zaman'),B('Skaler ve vektörel','vektörel nicelikler büyüklük ve yön, skaler nicelikler yalnız büyüklük taşır. Örnek: 5 m/s kuzeye hız vektörel, 5 kg kütle skalerdir')],
 ad=[A('Temel olanları ele','Sıcaklık, kütle ve uzunluk temel niceliklerdir.','Sıcaklık, kütle, uzunluk elendi'),A('Kalanları incele','Hız ve enerji türetilmiştir. Enerjinin yönü yoktur; hızın yönü vardır.','Enerji: skaler · Hız: vektörel'),A('Sonuç','Hem türetilmiş hem vektörel olan hızdır.','Hız')],
 puf='Önce temel nicelikleri ele, kalan türetilmiş niceliklerden yönü olanı seç.')
# ---- 0002
# P = W/t = F x / t ; F = kg m/s2  -> kg m2/s3
mk(P,'0002',tipId='fz-gr-birim',tip='Birim türetme',z='orta',alt='Fiziksel Niceliklerin Sınıflandırılması',kaz='Tanım bağıntısından türetilmiş bir niceliğin temel birimlerle ifadesini bulur.',kalip='düz',adim=3,
 kart='K-FZGR-02 (birim türetme) · güç',
 metin='Kuvvetin birimi kg·m/s²’dir. İş, kuvvet ile yolun çarpımı; güç ise işin zamana bölümüdür.\nBuna göre SI birim sisteminde birimi kg·m²/s³ olan nicelik aşağıdakilerden hangisidir?',
 dogru='Güç',sira=['Kuvvet','Enerji','Basınç','Özkütle','Güç'],yan=[('Kuvvet','Birimi kg·m/s² olan kuvveti seçmiş; metre üssünü ve zamanı hesaba katmamış.','dikkat'),('Enerji','İşin birimini (kg·m²/s²) bulmuş ama zamana bölmeyi unutmuş.','islem'),('Basınç','Birimi kg/(m·s²) olan basıncı seçmiş; kuvveti alana bölmüş.','bilgi'),('Özkütle','Özkütlenin birimi kg/m³’tür; temel birimlerle karıştırmış.','bilgi')],
 istenen='Birimi kg·m²/s³ olan nicelik.',
 ip=['Önce işin, sonra gücün birimini temel birimlerle yaz; zaman birimi paydaya girer.'],
 bilgi=[B('Birim türetme','türetilmiş niceliğin birimi bağıntıdan çıkar; çarpmada birimler çarpılır, bölmede bölünür. Örnek: hız = yol ÷ zaman ise birim m/s’dir')],
 ad=[A('İşin birimi','İş = kuvvet × yol.','kg·m/s² × m = kg·m²/s²'),A('Gücün birimi','Güç = iş ÷ zaman.','kg·m²/s² ÷ s = kg·m²/s³'),A('Sonuç','Bu birim güce aittir (watt).','Güç')],
 puf='Birim sorularında tanım bağıntısını sırayla uygula; her bölmede paydaya bir saniye üssü eklenir.')
# ---- 0003
m_g=540; V_dm3=Fr(2,10); d=Fr(m_g,1000)/(V_dm3/1000)
assert d==2700 and Fr(m_g)/(V_dm3*1000)==Fr(27,10) and Fr(m_g)/(V_dm3*10000)*1000/1000*1==Fr(27,100)
assert Fr(m_g,1000)/(V_dm3*10000/10**6)==270 and Fr(m_g,1000)/(V_dm3*100/10**6)==27000 and Fr(m_g)/(V_dm3/1000)==2700000
mk(P,'0003',tipId='fz-gr-donusum',tip='Özkütlede birim dönüşümü',z='orta',alt='Fiziksel Niceliklerin Sınıflandırılması',kaz='Kütle ve hacim birimlerini SI birimine çevirerek özkütleyi hesaplar.',kalip='hikâyeli',adim=3,
 kart='K-FZGR-03 (birim dönüşümü) · g ve dm³ verilmiş, kg/m³ istenmiş',
 metin='Bir kuyumcu, homojen bir alüminyum parçanın kütlesini 540 g, hacmini 0,2 dm³ ölçüyor.\nBuna göre alüminyum parçanın özkütlesi kaç kg/m³’tür?',
 dogru=2700,yan=[(Fr(27,10),'Hacmi doğru çevirip (0,2 dm³ = 200 cm³) 540 ÷ 200 = 2,7 g/cm³ bulmuş; sonucu kg/m³’e çevirmeyi (× 1000) unutmuş.','dikkat'),(270,'1 dm³’ü 10 000 cm³ almış; hacmi 2000 cm³ bulmuş.','islem'),(27000,'1 dm³’ü 100 cm³ almış; hacmi 20 cm³ bulmuş.','islem'),(2700000,'Kütleyi kg’ye çevirmemiş; g/m³ cinsinden sonucu kg/m³ sanmış.','islem')],
 istenen='Alüminyum parçanın özkütlesi (kg/m³).',
 ip=['Kütleyi kilograma, hacmi metreküpe çevir: 1 dm³ = 10⁻³ m³ ve 1000 g = 1 kg.'],
 bilgi=[B('Birim çevirme','1 kg = 1000 g; 1 dm³ = 1 L = 1000 cm³ = 10⁻³ m³. Örnek: 2 dm³ = 2 × 10⁻³ m³'),B('Özkütle','d = m ÷ V. Örnek: 6 kg kütleli, 2 m³ hacimli cismin özkütlesi 3 kg/m³’tür')],
 ad=[A('Kütle','Gramı kilograma çevir.','m = 540 g = 0,54 kg'),A('Hacim','Desimetreküpü metreküpe çevir.','V = 0,2 dm³ = 0,2 × 10⁻³ m³ = 2 × 10⁻⁴ m³'),A('Özkütle','Kütle hacme bölünür.','d = 0,54 ÷ (2 × 10⁻⁴) = 2700 kg/m³')],
 puf='Özkütlede g/cm³ değeri 1000 ile çarpılınca kg/m³ olur: 2,7 g/cm³ = 2700 kg/m³.')
# ---- 0004
D={'K':(50,100,10),'L':(50,200,10),'M':(80,100,10),'N':(80,200,20)}
from itertools import combinations
gecerli=[(a,b) for a,b in combinations('KLMN',2) if sum(x!=y for x,y in zip(D[a],D[b]))==1 and D[a][0]!=D[b][0]]
assert gecerli==[('K','M')], gecerli
mk(P,'0004',tipId='fz-gr-deney',tip='Kontrollü deney tasarımı',z='kolay',alt='Fiziksel Niceliklerin Sınıflandırılması',kaz='Bir etkenin etkisini incelemek için kontrol edilmesi gereken değişkenleri belirler.',kalip='tablo',adim=4,
 kart='K-FZGR-04 (kontrollü deney) · basit sarkaç, dört deney, tek geçerli çift',
 metin='Bir öğrenci, basit sarkacın periyodunun (bir tam salınım süresinin) ip uzunluğuna bağlı olup olmadığını araştırmak için dört deney yapıyor. Deneylerde kullanılan değerler aşağıdadır.\nDeney K: ip uzunluğu 50 cm, kütle 100 g, ilk açı 10°\nDeney L: ip uzunluğu 50 cm, kütle 200 g, ilk açı 10°\nDeney M: ip uzunluğu 80 cm, kütle 100 g, ilk açı 10°\nDeney N: ip uzunluğu 80 cm, kütle 200 g, ilk açı 20°\nBuna göre öğrenci, ip uzunluğunun etkisini belirlemek için hangi iki deneyin sonuçlarını karşılaştırmalıdır?',
 dogru='K ve M',sira=['K ve M','K ve L','L ve N','M ve N','L ve M'],yan=[('K ve L','Yalnız kütlesi farklı iki deneyi seçmiş; bu çift kütlenin etkisini gösterir.','dikkat'),('L ve N','İp uzunluğu ile ilk açının birlikte değiştiği çifti seçmiş; etkiler ayrılamaz.','bilgi'),('M ve N','İp uzunluğu sabit olan, kütle ve ilk açısı farklı çifti seçmiş.','dikkat'),('L ve M','İp uzunluğu ile kütlenin birlikte değiştiği çifti seçmiş; etkiler ayrılamaz.','bilgi')],
 istenen='İp uzunluğunun etkisini ölçecek deney çifti.',
 ip=['İncelenen etken dışında her şeyi sabit tutan deney çiftini ara: ip uzunluğu farklı, kütle ve ilk açı aynı olmalıdır.'],
 bilgi=[B('Kontrollü deney','bir etkenin etkisi incelenirken yalnız o etken (bağımsız değişken) değiştirilir, diğerleri sabit tutulur. Örnek: bitkinin büyümesine ışığın etkisini incelerken su ve toprak miktarı iki bitkide de aynı olmalıdır')],
 ad=[A('Değiştirilecek etken','İncelenen etken ip uzunluğudur; kütle ve ilk açı sabit olmalıdır.','değişen: ip · sabit: kütle, ilk açı'),A('Çiftleri tara','K–M çiftinde yalnız uzunluk (50 ve 80 cm) farklıdır; kütle 100 g, açı 10° aynıdır.','K–M: yalnız ip farklı'),A('Diğer çiftler','K–L yalnız kütle, L–M ip ve kütle, L–N ip ve açı, M–N kütle ve açı bakımından farklıdır.','K ve M dışında hepsi uygun değil'),A('Sonuç','Tek geçerli çift K ve M’dir.','K ve M')],
 puf='Kontrollü deneyde karşılaştırılan iki deney arasında yalnız incelenen etken farklı olmalıdır.')
bitir(P,'fizikgiris','fiz|Fizik Bilimine Giriş')
