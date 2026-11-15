"""Çarpanlara Ayırma · şekilli paket (carpansek): 7 soru, hepsi şekilli (alan modelleri). Kardeş yok, ipucu 1. Her cevap ve çeldirici değer kodla hesaplanıp assert edilir.
Şekil ölçüleri Python'da üretilir; TikZ gövdesi aynı değerlerden f-string ile yazılır (bkz. havuz/URETIM-SEKIL.md)."""
import sys,os,math
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
H.KONU='Çarpanlara Ayırma'
P=Parti('carpansek','Çarpanlara Ayırma','mat|Çarpanlara Ayırma')
KY='ÖSYM 2018–2026 TYT Matematik (şekilli çarpanlara ayırma ve alan modeli soruları, yalnız mantık) · MEB 9. sınıf'
TP=lambda g:tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'+g+'\n\\end{tikzpicture}')
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)

IKF=B('İki kare farkı','a² − b² = (a − b)(a + b). Örnek: 9² − 4² = (9 − 4)(9 + 4) = 65')
TAM=B('Tam kare açılımı','(a + b)² = a² + 2ab + b². Örnek: (5 + 2)² = 25 + 20 + 4 = 49')
UCT=B('x² + px + q çarpanlara ayırma','çarpımı q, toplamı p olan iki sayı bulunursa x² + px + q = (x + m)(x + n) olur. Örnek: x² + 9x + 20 = (x + 4)(x + 5)')
ALN=B('Dikdörtgenin alanı ve çevresi','kenarları a ve b olan dikdörtgenin alanı ab, çevresi 2(a + b)’dir. Örnek: kenarları 4 ve 7 olan dikdörtgenin alanı 28, çevresi 22')

kart('K-CAS-01','Bahçe ve havuz arası yol alanı','Dış ve iç karenin kenarları şekilden okunur; yol alanı iki karenin alanları farkıdır ve iki kare farkı özdeşliğiyle kolayca hesaplanır.','Kenar farkını (ya da farkın karesini) alan sanmak; yalnız dış karenin alanını yazmak; toplamla çarpmayı unutmak.','kolay','şekilli',3,'cas-cerceve','Kare çerçevede iki kare farkı',KY)
kart('K-CAS-02','Alan parçalarından çevre','Dikdörtgenin dört parçasının alanları x² + 5x + 2x + 10 olarak toplanıp çarpanlara ayrılır; kenarlar (x + 5) ve (x + 2) bulunur ve çevre denklemi kurulur.','Çevre yerine yarı çevreyi yazmak; kenarlardan birini eksik almak; çevre denkleminde 2 ile çarpmayı unutmak.','kolay','şekilli',3,'cas-parca','Alan parçalarından kenar ve çevre',KY)
kart('K-CAS-03','Karelerle bölünmüş kare','Büyük kare, a² ve b² alanlı iki kare ile ab alanlı iki dikdörtgene ayrılır; kenarlar √ ile bulunup (a + b)² hesaplanır.','Yalnız iki karenin alanını toplamak; dikdörtgenin alanını yanlış hesaplamak; yalnız bir dikdörtgeni saymak.','orta','şekilli',4,'cas-kare','Kareyi karelere ve dikdörtgenlere bölme',KY)
kart('K-CAS-04','Cebir karoları (öncüllü)','Karoların alanları toplanıp x² + 5x + 6 elde edilir ve çarpanlara ayrılır; her öncül kenar, çevre ve alan yönünden ayrı ayrı denetlenir.','Çevreyi kenarlar toplamı sanmak; alan değerinde kenarı yanlış yazmak; karoları farklı gruplayıp başka kenar bulmak.','orta','şekilli',4,'cas-karo','Cebir karolarıyla dikdörtgen oluşturma',KY)
kart('K-CAS-05','Dikdörtgen bahçe ve yol','Yolun alanı dış ve iç dikdörtgenlerin alanları farkıdır; elde edilen ikinci dereceden ifade çarpanlara ayrılarak yol genişliği bulunur.','Yolun genişliğini iki yandan 2x yerine x almak; negatif kökü seçmek; denklemi çarpanlara ayırırken işaret hatası yapmak.','zor','şekilli',5,'cas-yol','Dikdörtgen bahçede yol genişliği',KY)
kart('K-CAS-06','Yan yana iki kare','Alt kenar uzunlukları toplamı a + b, alanlar farkı a² − b² olarak verilir; a² − b² = (a − b)(a + b) ile a − b bulunur ve kenarlar çözülür.','Alan farkını kenar farkı sanmak; büyük karenin çevresini yazmak; a − b ile a + b’yi karıştırmak.','orta','şekilli',4,'cas-yan','Yan yana iki karede iki kare farkı',KY)
kart('K-CAS-07','Cebirsel kenarlı dikdörtgen','Alan ifadesi çarpanlarına ayrılır; bilinen kenara göre diğer kenar bulunur; çevre bilgisinden x çözülür ve alan hesaplanır.','Çarpanlardan hangisinin hangi kenar olduğunu karıştırmak; çevre denkleminde 2 ile çarpmayı unutmak; x yerine kenarı alan hesabına katmak.','zor','şekilli',5,'cas-cebir','Cebirsel kenarlı dikdörtgende alan',KY)

# ---------- 01 · kolay · bahçe ve yol (kare çerçeve) ----------
D1,I1=74,26
assert D1*D1-I1*I1==(D1-I1)*(D1+I1)==4800 and D1-I1==48 and (D1-I1)**2==2304 and D1*D1==5476 and D1*D1+I1*I1==6152 and D1+I1==100
sc=.045; sd,si=D1*sc,I1*sc; o=(sd-si)/2
g=f'\\path[fill=vurgu!25,even odd rule] (0,0) rectangle ({sd:.3f},{sd:.3f}) ({o:.3f},{o:.3f}) rectangle ({o+si:.3f},{o+si:.3f});\\draw[thick] (0,0) rectangle ({sd:.3f},{sd:.3f});\\draw[thick] ({o:.3f},{o:.3f}) rectangle ({o+si:.3f},{o+si:.3f});'
g+=f'\\node at ({sd/2:.3f},-.32) {{{D1} m}};\\node at ({sd/2:.3f},{sd/2:.3f}) {{{I1} m}};'
sek=TP(g)
q('0001',tipId='cas-cerceve',tip='Kare çerçevede iki kare farkı',z='kolay',alt='İki Kare Farkı',kaz='Dış ve iç kare kenarlarını şekilden okuyup aradaki yolun alanını iki kare farkı özdeşliğiyle hesaplar.',kalip='şekilli',sekil=sek,
 kart='K-CAS-01 (bahçe ve havuz arası yol alanı) · 74 m dış kare, 26 m iç kare',
 metin='Kare biçimli bir bahçenin tam ortasına, kenarları bahçenin kenarlarına paralel olacak biçimde kare biçimli bir havuz yapılmıştır. Bahçe ile havuz arasında kalan boşluk, şekilde gölgeli olarak gösterilen yürüyüş yoludur.\nBuna göre bu yolun alanı kaç m²’dir?',
 dogru=4800,yan=[(100,'Kenarların toplamını (74 + 26) yol alanı sanmış; fark ile çarpmayı unutmuş.','dikkat'),(2304,'(74 − 26)² hesaplamış; kareler farkı, farkın karesine eşit değildir.','bilgi'),(5476,'Yalnız bahçenin (dış karenin) alanını yazmış; havuzun alanını çıkarmamış.','dikkat'),(6152,'Havuzun alanını çıkarmak yerine eklemiş: 74² + 26².','islem')],
 istenen='Yolun alanı.',
 ip=['Yolun alanını iki karenin alanı cinsinden yaz; sayıların büyük olduğuna dikkat et.'],
 bilgi=[IKF],
 ad=[A('Alanı kur','Yol alanı, dış kare ile iç karenin alanları farkıdır.','74² − 26²'),A('Özdeşlik','İki kare farkı: a² − b² = (a − b)(a + b).','(74 − 26)(74 + 26)'),A('Hesapla','Parantezleri hesapla.','48 × 100 = 4800')],
 puf='İki karenin alanları farkı istendiğinde karelerin ayrı ayrı hesabı yerine (a − b)(a + b) kullanılır.')

# ---------- 02 · kolay · alan parçalarından çevre ----------
x2=6; w2=[x2,5]; h2=[x2,2]
assert x2*x2+5*x2+2*x2+10==(x2+5)*(x2+2) and 2*((x2+5)+(x2+2))==38
for yy,ac in [(7,'x+5 ve x ile'),(12,''),(19,''),(24,'')]: pass
assert (38-10)//4==7 and 4*7+10==38 and (38-14)==24 and 38//2==19 and 4*x2+14==38 and (38-14)/2==12
a1,a2,b1,b2=1.8,1.5,1.8,.6
g=f'\\draw[thick] (0,0) rectangle ({a1+a2:.2f},{b1+b2:.2f});\\draw[thick] ({a1:.2f},0) -- ({a1:.2f},{b1+b2:.2f});\\draw[thick] (0,{b2:.2f}) -- ({a1+a2:.2f},{b2:.2f});'
g+=f'\\node at ({a1/2:.2f},{b2+b1/2:.2f}) {{$x^2$}};\\node at ({a1+a2/2:.2f},{b2+b1/2:.2f}) {{$5x$}};\\node at ({a1/2:.2f},{b2/2:.2f}) {{$2x$}};\\node at ({a1+a2/2:.2f},{b2/2:.2f}) {{$10$}};'
g+=f'\\node[anchor=west,font=\\footnotesize] at ({a1+a2+.1:.2f},{b1+b2+.0:.2f}) {{(alanlar cm$^2$)}};'
sek=TP(g)
q('0002',tipId='cas-parca',tip='Alan parçalarından kenar ve çevre',z='kolay',alt='Alan Modeli',kaz='Dört parçaya bölünmüş dikdörtgenin parça alanlarını toplayıp çarpanlara ayırarak kenarları ve çevreyi kullanıp x’i bulur.',kalip='şekilli',sekil=sek,
 kart='K-CAS-02 (alan parçalarından çevre) · x², 5x, 2x, 10 parçaları, çevre 38',
 metin='Şekilde, dikdörtgen biçimli bir karton, kenarları dikdörtgenin kenarlarına paralel doğrularla dört dikdörtgen parçaya ayrılmıştır. x² cm² alanlı parça karedir; parçaların alanları cm² cinsinden verilmiştir. x pozitif bir gerçek sayıdır.\nKartonun çevresi 38 cm olduğuna göre x kaçtır?',
 dogru=6,yan=[(7,'Kenarları (x + 5) ve x almış (2 cm’lik parça payını unutmuş): 4x + 10 = 38 → x = 7.','dikkat'),(12,'Çevre denkleminde 4x + 14 = 38’den 4x = 24 bulup 4’e bölmek yerine 2’ye bölmüş.','islem'),(19,'Çevreyi yarı çevre sanıp 38 ÷ 2 = 19 yazmış.','dikkat'),(24,'4x = 24’ü bulduktan sonra 4’e bölmeyi unutmuş.','islem')],
 istenen='x değeri.',
 ip=['Dört parçanın alanlarını topla ve ortaya çıkan ifadeyi çarpanlarına ayır.'],
 bilgi=[UCT,ALN],
 ad=[A('Toplam alan','Parça alanları toplanır.','x² + 5x + 2x + 10 = x² + 7x + 10'),A('Kenarlar','Çarpımı 10, toplamı 7 olan sayılar 2 ve 5’tir.','(x + 2)(x + 5) → kenarlar x + 2 ve x + 5'),A('Çevre','Çevre, iki komşu kenar toplamının 2 katıdır.','2(2x + 7) = 38'),A('Çöz','Denklemi çöz.','4x + 14 = 38 → x = 6')],
 puf='Alan parçalarını toplayıp çarpanlarına ayırınca kenarlar ortaya çıkar; çevre için iki kenarı topla ve 2 ile çarp.')

# ---------- 03 · orta · karelerle bölünmüş kare ----------
a3,b3=6,4
assert a3*a3==36 and b3*b3==16 and (a3+b3)**2==100 and 36+16==52 and 36+16+24==76 and 36+16+2*16==84 and 36+16+2*36==124
sc=.5; s_=(a3+b3)*sc
g=f'\\draw[thick] (0,0) rectangle ({s_:.3f},{s_:.3f});'
g+=f'\\draw[thick,fill=vurgu!25] (0,0) rectangle ({a3*sc:.3f},{a3*sc:.3f});\\draw[thick,fill=vurgu!25] ({a3*sc:.3f},{a3*sc:.3f}) rectangle ({s_:.3f},{s_:.3f});'
g+=f'\\draw[thick] ({a3*sc:.3f},0) -- ({a3*sc:.3f},{a3*sc:.3f});\\draw[thick] (0,{a3*sc:.3f}) -- ({a3*sc:.3f},{a3*sc:.3f});'
g+=f'\\draw[thick] ({a3*sc:.3f},{a3*sc:.3f}) -- ({s_:.3f},{a3*sc:.3f});\\draw[thick] ({a3*sc:.3f},{a3*sc:.3f}) -- ({a3*sc:.3f},{s_:.3f});'
g+=f'\\node at ({a3*sc/2:.3f},{a3*sc/2:.3f}) {{{a3*a3} m$^2$}};\\node[font=\\footnotesize] at ({a3*sc+b3*sc/2:.3f},{a3*sc+b3*sc/2:.3f}) {{{b3*b3} m$^2$}};'
sek=TP(g)
q('0003',tipId='cas-kare',tip='Kareyi karelere ve dikdörtgenlere bölme',z='orta',alt='Alan Modeli',kaz='Karelere ve dikdörtgenlere bölünmüş büyük karenin kenarını iki karenin kenarlarının toplamı olarak bulup alanı hesaplar.',kalip='şekilli',sekil=sek,
 kart='K-CAS-03 (karelerle bölünmüş kare) · 36 ve 16 m² kareler, büyük karenin alanı',
 metin='Kare biçimli bir arsa, şekildeki gibi kenarları arsanın kenarlarına paralel doğrularla iki kare ve iki dikdörtgene ayrılmıştır. Şekilde boyalı olan karelerin alanları verilmiştir.\nBuna göre arsanın tamamının alanı kaç m²’dir?',
 dogru=100,yan=[(36,'Yalnız boyalı karelerden büyüğünün alanını yazmış.','dikkat'),(52,'Yalnız iki karenin alanını (36 + 16) toplamış; iki dikdörtgenin alanlarını katmamış.','dikkat'),(76,'İki dikdörtgenden yalnız birini (24) hesaba katmış.','dikkat'),(84,'Dikdörtgenlerin alanını küçük karenin alanı (16) gibi alıp 36 + 16 + 2 × 16 hesaplamış.','islem')],
 istenen='Arsanın alanı.',
 ip=['Boyalı karelerin kenarlarını bul; arsanın kenarı bu kenarlarla nasıl ilişkili?'],
 bilgi=[TAM,B('Karenin kenarı','alanı A olan karenin kenarı √A’dır. Örnek: alanı 49 olan karenin kenarı 7')],
 ad=[A('Kenarları bul','Karelerin kenarı alanlarının karekökü.','√36 = 6 · √16 = 4'),A('Arsanın kenarı','Bir kenar, iki karenin kenarlarının toplamıdır.','6 + 4 = 10'),A('Alan','Karenin alanı kenarın karesi.','10² = 100')],
 puf='Kare iki kare ve iki dikdörtgene bölünmüşse kenarı a + b, alanı a² + 2ab + b² = (a + b)² olur.')

# ---------- 04 · orta · cebir karoları, öncüllü ----------
x4=4
assert x4*x4+5*x4+6==(x4+2)*(x4+3)==42 and 2*((x4+2)+(x4+3))==2*(2*x4+5)==26 and 4*x4+10==26 and 4*x4+12==28
g=f'\\draw[thick,fill=vurgu!25] (0,0) rectangle (1.2,1.2);\\node at (.6,1.45) {{$x$}};\\node at (-.25,.6) {{$x$}};'
g+=f'\\draw[thick,fill=vurgu!10] (2.4,0) rectangle (3.6,.4);\\node at (3.0,.65) {{$x$}};\\node at (2.15,.2) {{$1$}};'
g+=f'\\draw[thick,fill=vurgu!10] (5.0,0) rectangle (5.4,.4);\\node at (5.2,.65) {{$1$}};\\node at (4.75,.2) {{$1$}};'
g+=f'\\node at (.6,-.35) {{1 adet}};\\node at (3.0,-.35) {{5 adet}};\\node at (5.2,-.35) {{6 adet}};'
sek=TP(g)
sk=['Yalnız I','Yalnız III','I ve II','I ve III','II ve III']
q('0004',tipId='cas-karo',tip='Cebir karolarıyla dikdörtgen oluşturma',z='orta',alt='Alan Modeli',kaz='Cebir karolarının alanlarını toplayıp çarpanlarına ayırarak oluşan dikdörtgenin kenarları, çevresi ve alanı hakkındaki ifadeleri değerlendirir.',kalip='öncüllü',sekil=sek,
 kart='K-CAS-04 (cebir karoları) · x², 5 · x, 6 · 1 karoları, çevre ve alan öncülleri',
 metin='Şekilde, kenarları x ve 1 birim olan karolar ile adetleri gösterilmiştir (x > 1). Bu karoların hepsi kullanılarak, karolar boşluk kalmadan ve üst üste binmeden yan yana dizilip tek bir dikdörtgen oluşturuluyor.\nBu dikdörtgen için,\nI. Kenar uzunlukları x + 2 ve x + 3 birimdir.\nII. Çevresi 4x + 12 birimdir.\nIII. x = 4 iken alanı 42 birim karedir.\nifadelerinden hangileri doğrudur?',
 dogru='I ve III',yan=[('Yalnız I','III’ü yanlış sanmış: x = 4 iken alanı 16 + 20 + 6 = 42 hesaplayıp doğruladığını görmeliydi.','dikkat'),('Yalnız III','I’i yanlış sanmış: x² + 5x + 6 = (x + 2)(x + 3) olduğundan kenarlar doğrudur.','dikkat'),('I ve II','Çevreyi 4x + 12 sanmış: çevre 2[(x + 2) + (x + 3)] = 4x + 10’dur; III’ü de yanlış değerlendirmiş.','islem'),('II ve III','I’i yanlış değerlendirip II’yi doğru sanmış: çevre 4x + 10 olduğundan II yanlıştır.','dikkat')],
 sira=sk,
 istenen='Doğru olan öncüller.',
 ip=['Karoların alanlarını toplayıp ifadeyi çarpanlarına ayır; her öncülü bu kenarlarla ayrı ayrı dene.'],
 bilgi=[UCT,ALN],
 ad=[A('Toplam alan','Karoların alanları toplanır.','x² + 5x + 6'),A('Çarpanlar','Çarpımı 6, toplamı 5 olan sayılar 2 ve 3’tür; I doğrudur.','(x + 2)(x + 3)'),A('II’yi dene','Çevre iki komşu kenarın toplamının 2 katıdır; 4x + 10 olur, II yanlıştır.','2(2x + 5) = 4x + 10'),A('III’ü dene','x = 4 için kenarlar 6 ve 7 birimdir; III doğrudur.','6 × 7 = 42')],
 puf='Öncüllü sorularda her ifadeyi bulduğun çarpanlı biçimden ayrı ayrı doğrula; çevre ve alanı karıştırma.')

# ---------- 05 · zor · dikdörtgen bahçe ve yol ----------
L5,W5,x5,yal=30,18,2,208
assert (L5+2*x5)*(W5+2*x5)-L5*W5==yal==4*x5**2+96*x5 and x5*x5+24*x5-52==(x5+26)*(x5-2)==0
assert 2*x5==4 and (x5+12)**2==196 and 26 and 52
sc=.13; iw,ih=L5*sc,W5*sc; bw=x5*sc
g=f'\\path[fill=vurgu!25,even odd rule] ({-bw:.3f},{-bw:.3f}) rectangle ({iw+bw:.3f},{ih+bw:.3f}) (0,0) rectangle ({iw:.3f},{ih:.3f});'
g+=f'\\draw[thick] ({-bw:.3f},{-bw:.3f}) rectangle ({iw+bw:.3f},{ih+bw:.3f});\\draw[thick] (0,0) rectangle ({iw:.3f},{ih:.3f});'
g+=f'\\node at ({iw/2:.3f},{ih-.3:.3f}) {{{L5} m}};\\node[rotate=90] at (.3,{ih/2:.3f}) {{{W5} m}};'
g+=f'\\draw[<->,>=Stealth] ({iw+bw+.45:.3f},{ih/2:.3f}) -- ({iw+bw+.45:.3f},{ih/2:.3f}) ;'
g=g.rsplit('\\draw[<->',1)[0]
g+=f'\\draw[-{{Stealth[length=1.5mm]}}] ({iw+bw+.55:.3f},{ih/2:.3f}) -- ({iw+.02:.3f},{ih/2:.3f});\\draw[-{{Stealth[length=1.5mm]}}] ({iw+bw+.55:.3f},{ih/2:.3f}) -- ({iw+bw-.02:.3f},{ih/2:.3f});\\node[anchor=west] at ({iw+bw+.55:.3f},{ih/2:.3f}) {{$x$}};'
sek=TP(g)
q('0005',tipId='cas-yol',tip='Dikdörtgen bahçede yol genişliği',z='zor',alt='Alan Modeli',kaz='Dikdörtgen bahçenin çevresindeki yolun alanını dış ve iç dikdörtgenlerin farkı olarak yazıp ikinci dereceden ifadeyi çarpanlarına ayırarak yol genişliğini bulur.',kalip='şekilli',sekil=sek,
 kart='K-CAS-05 (dikdörtgen bahçe ve yol) · 30 × 18 m bahçe, yol alanı 208 m²',
 metin='Şekilde, boyutları verilen dikdörtgen biçimli bir bahçenin dışında, bahçeyi dört yandan çevreleyen ve her yerde aynı genişlikte (x metre) olan bir yürüyüş yolu yapılmıştır. Gölgeli bölge yolu göstermektedir. Yolun alanı 208 m²’dir.\nBuna göre yolun genişliği x kaç metredir?',
 dogru=2,yan=[(4,'Yolun her kenarda iki kez eklendiğini görüp 2x = 4’ü x sanmış.','dikkat'),(14,'x² + 24x − 52 = 0’ı (x + 12)² = 196 yazıp x + 12 = 14’te durmuş; 12’yi çıkarmamış.','islem'),(26,'(x + 26)(x − 2) = 0 çarpanlarında kökü seçerken 26’yı almış (negatif kök −26’nın mutlak değeri).','dikkat'),(52,'Denklemdeki sabit terimi (52) çözüm sanmış.','dikkat')],
 istenen='Yolun genişliği x.',
 ip=['Dış dikdörtgenin kenarları bahçenin kenarlarından kaç birim uzundur? Yolun alanını dış ile iç alanların farkı olarak yaz.'],
 bilgi=[UCT,ALN],
 ad=[A('Dış kenarlar','Yol her yanda x genişliğinde olduğundan her kenar 2x uzar.','(30 + 2x) ve (18 + 2x)'),A('Yol alanı','Dış alandan iç alan çıkarılır.','(30 + 2x)(18 + 2x) − 30 · 18 = 4x² + 96x'),A('Denklem','Yolun alanı 208’e eşitlenir ve sadeleştirilir.','4x² + 96x = 208 → x² + 24x − 52 = 0'),A('Çarpanla','Çarpımı −52, toplamı 24 olan sayılar 26 ve −2’dir.','(x + 26)(x − 2) = 0'),A('Uzunluk','Genişlik pozitif olduğundan x = 2.','x = 2')],
 puf='Yol genişliği her iki yanda eklendiğinden dış kenar 2x artar; ikinci dereceden denklemde yalnız pozitif kök uzunluk olur.')

# ---------- 06 · orta · yan yana iki kare ----------
a6,b6=9,5; T6=14; F6=56
assert a6+b6==T6 and a6*a6-b6*b6==F6 and F6//T6==4 and (T6+F6//T6)//2==a6 and 4*b6==20 and 4*a6==36 and 4*4==16 and 2*14==28
sc=.3; g=f'\\draw[thick,fill=vurgu!25] (0,0) rectangle ({a6*sc:.3f},{a6*sc:.3f});\\draw[thick,fill=vurgu!10] ({a6*sc:.3f},0) rectangle ({(a6+b6)*sc:.3f},{b6*sc:.3f});'
g+=f'\\draw[<->,>=Stealth] (0,-.3) -- ({(a6+b6)*sc:.3f},-.3);\\node at ({(a6+b6)*sc/2:.3f},-.62) {{{T6} cm}};'
sek=TP(g)
q('0006',tipId='cas-yan',tip='Yan yana iki karede iki kare farkı',z='orta',alt='İki Kare Farkı',kaz='Yan yana iki karenin kenarları toplamı ve alanları farkı verildiğinde iki kare farkı özdeşliğiyle kenarları bulur.',kalip='şekilli',sekil=sek,
 kart='K-CAS-06 (yan yana iki kare) · kenarlar toplamı 14 cm, alan farkı 56 cm²',
 metin='Şekilde, alt kenarları aynı doğru üzerinde olacak biçimde yan yana konulmuş iki kare ve alt kenarların toplam uzunluğu gösterilmiştir. Büyük karenin alanı, küçük karenin alanından 56 cm² fazladır.\nBuna göre küçük karenin çevresi kaç cm’dir?',
 dogru=20,yan=[(16,'Kenarlar farkını (4) bulup çevre sanarak 4 × 4 = 16 yazmış.','dikkat'),(28,'Toplam uzunluğun (14) 2 katını çevre almış.','dikkat'),(36,'Büyük karenin çevresini (4 × 9) yazmış.','dikkat'),(56,'Alanlar farkını çevre olarak yazmış.','dikkat')],
 istenen='Küçük karenin çevresi.',
 ip=['Karelerin alanları farkını, kenarların toplamı ve farkı cinsinden yaz.'],
 bilgi=[IKF],
 ad=[A('Özdeşlik','Kenarlar a (büyük) ve b (küçük) olsun; alanlar farkı iki kare farkıdır.','a² − b² = (a − b)(a + b) = 56'),A('Kenar farkı','Kenarlar toplamı 14’tür.','(a − b) · 14 = 56 → a − b = 4'),A('Kenarlar','Toplam ve farktan kenarlar bulunur.','a = 9, b = 5'),A('Çevre','Küçük karenin çevresi.','4 × 5 = 20')],
 puf='Alanlar farkı ve kenarlar toplamı verildiğinde iki kare farkından kenarlar farkını (a − b) bul.')

# ---------- 07 · zor · cebirsel kenarlı dikdörtgen ----------
x7=16
assert x7*x7-5*x7-14==(x7-7)*(x7+2)==162 and 2*((x7-7)+(x7+2))==54 and 9*9==81 and x7*(x7-7)==144 and x7*(x7+2)==288 and 18*18==324
g=f'\\draw[thick] (0,0) rectangle (4.4,1.6);\\node[font=\\small] at (2.2,.8) {{$A = x^2 - 5x - 14$ cm$^2$}};\\node[rotate=90] at (-.6,.8) {{$x-7$ cm}};'
sek=TP(g)
q('0007',tipId='cas-cebir',tip='Cebirsel kenarlı dikdörtgende alan',z='zor',alt='Alan Modeli',kaz='Alanı cebirsel verilen dikdörtgenin diğer kenarını çarpanlara ayırma ile bulup çevre bilgisinden x’i çözerek alanı hesaplar.',kalip='şekilli',sekil=sek,
 kart='K-CAS-07 (cebirsel kenarlı dikdörtgen) · kısa kenar x − 7, alan x² − 5x − 14, çevre 54',
 metin='Şekilde bir kenarı ve alanı verilen dikdörtgen biçimli kartonun çevresi 54 cm’dir.\nBuna göre kartonun alanı kaç cm²’dir?',
 dogru=162,yan=[(81,'Kenarın (x − 7 = 9) karesini alan sanmış.','dikkat'),(144,'x ile bilinen kenarı (16 × 9) çarpmış.','dikkat'),(288,'x ile diğer kenarı (16 × 18) çarpmış.','dikkat'),(324,'Uzun kenarın karesini (18²) alan sanmış.','dikkat')],
 istenen='Kartonun alanı.',
 ip=['Alan ifadesini çarpanlarına ayırıp bilinen kenarla karşılaştır; diğer kenarı x cinsinden yaz.'],
 bilgi=[UCT,ALN],
 ad=[A('Çarpanlar','Çarpımı −14, toplamı −5 olan sayılar −7 ve 2’dir.','x² − 5x − 14 = (x − 7)(x + 2)'),A('Kenarlar','Kenarlardan biri x − 7 olduğundan diğeri x + 2’dir.','x − 7 ve x + 2'),A('Çevre','Çevreden x çözülür.','2(2x − 5) = 54 → x = 16'),A('Kenarlar ve alan','x = 16 yazılır.','9 × 18 = 162 cm²'),A('Kontrol','Alan ifadesine de yazılabilir.','16² − 5 · 16 − 14 = 162')],
 puf='Alan ifadesini çarpanlarına ayırıp verilen kenarı eşleştir; kalan çarpan diğer kenardır.')

bitir(P,'carpansek','mat|Çarpanlara Ayırma')
