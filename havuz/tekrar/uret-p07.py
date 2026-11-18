import sys, re, json, math, os
from fractions import Fraction as F
sys.path.insert(0,'/home/claude/zekacademy-app/havuz')
from cizim import tikz_svg

GIRDI='/tmp/kor/kart/parti/p07.txt'
CIKTI=os.path.join(os.path.dirname(os.path.abspath(__file__)),'kart-p07.json')
ids=[m.group(1) for m in re.finditer(r'^### (\S+) \|',open(GIRDI,encoding='utf-8').read(),re.M)]

def tz(g): return tikz_svg('\\begin{tikzpicture}[line width=.8pt,>=stealth]\n'+g+'\n\\end{tikzpicture}')
RA=lambda p,a,b,s=.25: ''  # yer tutucu

kartlar=[]
def K(id,k,baslik,olcer,kural,formul,sekil,soru,adimlar,cevap,hata,akilda):
    kartlar.append({"id":id,"k":k,"baslik":baslik,"olcer":olcer,"kural":kural,"formul":formul,"sekil":sekil,
      "ornek":{"soru":soru,"adimlar":adimlar,"cevap":cevap},"hata":hata,"akilda":akilda})

# 1 açıortay
assert F(10,15)==F(2,3) and F(100,5)*2==40
K('geo-aciortay-01','geo|Açıortay','Açıortay ve alan oranı',
 'Açıortay teoremiyle bulduğun taban oranını, ortak yükseklikli üçgenlerde alan oranına çevirebilmeni.',
 'İç açıortay karşı kenarı **komşu kenarların oranında** böler. Açıortayla ayrılan iki üçgenin yüksekliği ortaktır; bu yüzden alanları **tabanlarıyla orantılıdır**. Yani kenar oranı alan oranı olur. Önce oranı kur, sonra toplam alanı bu orana göre paylaştır.',
 '|BD| / |DC| = |AB| / |AC| = A(ABD) / A(ADC)',
 tz(r'''\coordinate (A) at (1.2,3);\coordinate (B) at (0,0);\coordinate (C) at (5,0);\coordinate (D) at (2,0);
\draw (A)--(B)--(C)--cycle;\draw[vurgu,very thick] (A)--(D);
\node[above] at (A){A};\node[below left] at (B){B};\node[below right] at (C){C};\node[below] at (D){D};
\node[left] at (.45,1.7){$c$};\node[right] at (3.3,1.7){$b$};'''),
 '|AB| = 10, |AC| = 15 olan ABC üçgeninde [AD] açıortaydır ve A(ABC) = 100 cm²\'dir. A(ABD) kaç cm²\'dir?',
 ['Oranı kur: |BD| / |DC| = 10 / 15 = 2 / 3.','ABD ve ADC üçgenlerinin yüksekliği ortaktır; alanları da 2 : 3 oranındadır.','Toplam 2 + 3 = 5 parça: her parça 100 ÷ 5 = 20 cm².','A(ABD) = 2 · 20 = 40.'],
 '40 cm²',
 'Oranı ters yazmak ya da D\'yi orta nokta sanıp alanı yarıya bölmek. Kontrol yolu: kısa kenarın yanındaki parçanın alanı da küçüktür.',
 'Kenar oranı, alan oranıdır.')

# 2 daire dilimi
assert F(150,360)==F(5,12) and 144*F(5,12)==60
K('geo-dairede-cevre-01','geo|Dairede Çevre ve Alan','Daire diliminde yay ve alan',
 'Merkez açıya göre dilimin yay uzunluğunu, alanını ve çevresini doğru formülle bulabilmeni.',
 'Merkez açısı α olan dilim, dairenin **α/360** kadarıdır. Yay uzunluğu ve alan bu kesirle çarpılır. Dilimin çevresi sorulursa yaya **iki yarıçap** da eklenir. Çap ile yarıçapı karıştırma: formüllerde **r yarıçaptır**.',
 'Yay = 2πr · α/360   ·   Alan = πr² · α/360',
 tz(r'''\draw[fill=vurgu!15] (0,0)--(2,0) arc(0:150:2)--cycle;
\draw[dashed] (2,0) arc(0:-210:2);
\node at (.75,.32){$\alpha$};\node[below] at (1,0){$r$};\node[above left] at (-.7,.85){$r$};
\fill (0,0) circle(1.5pt);'''),
 'Yarıçapı 12 cm, merkez açısı 150° olan daire diliminin alanı kaç π cm²\'dir?',
 ['Tam daire alanı: π · 12² = 144π.','Dilimin kesri: 150 / 360 = 5 / 12.','Alan = 144π · 5 / 12 = 60π.'],
 '60π cm²',
 'Çevre sorusunda yalnız yayı yazmak ya da yarıçap yerine çapı kullanmak. Sınırdaki her çizgiyi say: yay ile iki yarıçap.',
 'Çevrede sınırdaki her çizgiyi say.')

# 3 deltoid
assert math.isqrt(13**2-12**2)==5 and math.isqrt(15**2-12**2)==9 and 14*24//2==168
K('geo-deltoid-01','geo|Deltoid','Deltoidin alanı',
 'Köşegen uzunluklarını (gerekirse Pisagorla) bulup deltoidin tüm alanını hesaplayabilmeni.',
 'Deltoidde eşit kenarlı köşeleri birleştiren köşegen **simetri eksenidir**: diğer köşegeni **dik keser ve ortalar**. Köşegenler dik olduğu için alan, **köşegenler çarpımının yarısıdır**. Bir köşegen eksikse oluşan dik üçgenlerde Pisagor uygula.',
 'Alan = |AC| · |BD| ÷ 2',
 tz(r'''\coordinate (A) at (-1.8,0);\coordinate (C) at (3,0);\coordinate (B) at (0,1.7);\coordinate (D) at (0,-1.7);\coordinate (O) at (0,0);
\draw (A)--(B)--(C)--(D)--cycle;\draw[dashed] (A)--(C);\draw[dashed] (B)--(D);
\draw (0,.22)--(.22,.22)--(.22,0);
\node[left] at (A){A};\node[above] at (B){B};\node[right] at (C){C};\node[below] at (D){D};\node[below left] at (-.05,0){O};'''),
 '|AB| = |AD| = 13, |CB| = |CD| = 15 ve |BD| = 24 olan ABCD deltoidinin alanı kaçtır?',
 ['AC, BD\'yi O\'da dik keser ve ortalar: |BO| = 12.','|AO| = √(13² − 12²) = 5 ve |CO| = √(15² − 12²) = 9, yani |AC| = 14.','Alan = 14 · 24 ÷ 2 = 168.'],
 '168',
 'Bir köşegenin yalnız yarısını çarpmak ya da tek üçgenin alanını verip bırakmak. Alan formülüne iki köşegenin tam boyu girer.',
 'Dik köşegenler: çarp, ikiye böl.')

# 4 dik üçgen Öklid
assert 4*16==64 and 4*20==80 and 80==16*5 and 4*4+64==80
K('geo-dik-ucgen-02','geo|Dik Üçgen','Öklid bağıntıları',
 'Hipotenüse inen yüksekliğin ayırdığı parçalardan yüksekliği ya da dik kenarı bulabilmeni.',
 'Dik üçgende hipotenüse indirilen yükseklik hipotenüsü p ve k parçalarına ayırır. **h² = p · k** ve **dik kenar² = komşu parça · hipotenüs** olur. Hipotenüse ait kenarortay da hipotenüsün **yarısına** eşittir.',
 'h² = p · k   ·   a² = p · c',
 tz(r'''\coordinate (B) at (0,0);\coordinate (C) at (5,0);\coordinate (A) at (1.8,2.4);\coordinate (D) at (1.8,0);
\draw (A)--(B)--(C)--cycle;\draw[vurgu,very thick] (A)--(D);
\draw (1.8,.2)--(2,.2)--(2,0);
\node[above] at (A){A};\node[below left] at (B){B};\node[below right] at (C){C};\node[below] at (D){D};
\node[below] at (.9,-.3){$p$};\node[below] at (3.4,-.3){$k$};\node[left] at (1.75,1.2){$h$};'''),
 'Dik üçgende hipotenüse inen yüksekliğin ayırdığı parçalar 4 ve 16\'dır. Yükseklik ile uzunluğu 4 olan parçaya komşu dik kenar kaçtır?',
 ['h² = 4 · 16 = 64, yani h = 8.','Hipotenüs c = 4 + 16 = 20.','a² = 4 · 20 = 80, yani a = 4√5.'],
 'h = 8, a = 4√5',
 'Dik kenarın karesini yükseklik · hipotenüs yazmak. Kontrol: dik kenar, komşu olduğu parçayla eşleşir; hipotenüs bütün kenardır.',
 'Yükseklik karesi, parçaların çarpımıdır.')

# 5 dikdörtgen
assert math.isqrt(81+144)==15 and 9+12-15==6
K('geo-dikdortgen-02','geo|Dikdörtgen','Dikdörtgende köşegen ve çevre',
 'Köşegeni Pisagorla bulup yolları karşılaştırabilmeni ve çevreden eksik kenarı çıkarabilmeni.',
 'Dikdörtgende köşegen, iki kenarla bir **dik üçgen** kurar: köşegen² = a² + b². Köşegenler eşit uzunlukta olup birbirini ortalar. Çevre 2(a + b) olduğundan **yarım çevre** iki kenarın toplamıdır; eksik kenarı yarım çevreden çıkararak bul.',
 'd² = a² + b²   ·   Çevre = 2(a + b)',
 tz(r'''\draw (0,0) rectangle (4,2.4);\draw[vurgu,very thick] (0,0)--(4,2.4);
\node[below] at (2,0){$a$};\node[right] at (4,1.2){$b$};\node[above left] at (2,1.35){$d$};
\draw (3.75,0)--(3.75,.25)--(4,.25);'''),
 'Kenarları 9 m ve 12 m olan dikdörtgen bir bahçede, bir köşeden karşı köşeye kenarlardan yürümek yerine köşegenden geçmek kaç m kısaltır?',
 ['Köşegen: √(9² + 12²) = √225 = 15 m.','Kenar yolu: 9 + 12 = 21 m.','Fark: 21 − 15 = 6 m.'],
 '6 m',
 'Köşegeni bulup yalnız uzun kenarla kıyaslamak. Kenar yolu iki kenarın toplamıdır; farkı onunla köşegen arasında al.',
 'Kestirme: iki kenar toplamı eksi köşegen.')

# 6 doğrunun analitiği
assert 6*4//2==12 and 2*6+3*0-12==0 and 2*0+3*4-12==0
K('geo-dogrunun-analitigi-01','geo|Doğrunun Analitiği','Doğru, eksenler ve üçgen alanı',
 'Doğrunun eksenleri kestiği noktaları bulup oluşan üçgenin alanını ve kesişim noktasını hesaplayabilmeni.',
 'x eksenini kesen nokta için **y = 0**, y eksenini kesen nokta için **x = 0** yazılır. Doğru ile eksenlerin sınırladığı dik üçgenin dik kenarları, bu kesim noktalarının **mutlak değeridir**. İki doğrunun kesişimi, denklemlerin **ortak çözümüdür**.',
 'Alan = |a| · |b| ÷ 2',
 tz(r'''\draw[->] (-.5,0)--(4,0) node[right]{$x$};\draw[->] (0,-.5)--(0,3) node[above]{$y$};
\fill[vurgu!15] (0,0)--(3,0)--(0,2)--cycle;\draw[vurgu,very thick] (-.4,2.27)--(3.4,-.27);
\node[below] at (3,-.05){$(a,0)$};\node[left] at (-.05,2){$(0,b)$};\node at (.8,.6){alan};
\fill (3,0) circle(1.5pt);\fill (0,2) circle(1.5pt);'''),
 '2x + 3y − 12 = 0 doğrusu ile eksenlerin sınırladığı üçgenin alanı kaçtır?',
 ['y = 0 için 2x = 12, x = 6. Doğru x eksenini (6, 0) noktasında keser.','x = 0 için 3y = 12, y = 4. Doğru y eksenini (0, 4) noktasında keser.','Alan = 6 · 4 ÷ 2 = 12.'],
 '12',
 'Katsayıları (2 ve 3) dik kenar sanmak ya da alan yerine hipotenüsü hesaplamak. Önce kesim noktalarını bul, sonra alan formülünü yaz.',
 'Eksen kesimi için diğer koordinatı sıfır yap.')

# 7 dönüşüm
assert math.isqrt(10**2+24**2)==26
K('geo-donusum-geometrisi-01','geo|Dönüşüm Geometrisi','Öteleme ve yansıma',
 'Noktanın öteleme ve yansımalarla yeni koordinatını bulup uzaklığı hesaplayabilmeni.',
 '(a, b) kadar ötelemede (x, y) noktası **(x + a, y + b)** olur: a sağa (+), b yukarı (+). x eksenine yansımada **y**, y eksenine yansımada **x** işaret değiştirir. y = x doğrusuna göre yansımada koordinatlar **yer değiştirir**. Öteleme ve yansıma uzunluğu korur.',
 'x eksenine: (x, y) → (x, −y)   ·   y eksenine: (x, y) → (−x, y)',
 None,
 'A(5, 12) noktası önce x eksenine, sonra y eksenine göre yansıtılarak A\'\' noktası elde ediliyor. |AA\'\'| kaçtır?',
 ['x eksenine yansıma: (5, 12) → (5, −12).','y eksenine yansıma: (5, −12) → (−5, −12).','Yatay fark 10, dikey fark 24: |AA\'\'| = √(100 + 576) = 26.'],
 '26',
 'Öteleme bileşenlerini işaretine bakmadan toplamak ya da çıkarmak. Sağ ve yukarı pozitif, sol ve aşağı negatiftir; işareti yazarak ilerle.',
 'x eksenine yansıyınca y\'nin işareti değişir.')

# 8 dörtgenler
assert 2*(12//2+20//2)==32
K('geo-dortgenler-02','geo|Dörtgenler','Dörtgende köşegen ve orta noktalar',
 'Köşegenleri dik dörtgenin alanını ve orta noktalardan oluşan paralelkenarın çevresini köşegenlerden bulabilmeni.',
 'Köşegenleri **dik** kesişen dörtgenin alanı, köşegenlerin çarpımının yarısıdır. Kenar orta noktalarını birleştirince **paralelkenar** oluşur. Orta tabandan dolayı kenarları köşegenlerin **yarısına** eşittir; çevresi köşegenlerin toplamı kadardır.',
 'Alan = |AC| · |BD| ÷ 2   ·   Çevre(KLMN) = |AC| + |BD|',
 tz(r'''\coordinate (A) at (0,0);\coordinate (B) at (4,.5);\coordinate (C) at (3.6,3);\coordinate (D) at (.4,2.4);
\draw (A)--(B)--(C)--(D)--cycle;\draw[dashed] (A)--(C);\draw[dashed] (B)--(D);
\coordinate (K) at ($(A)!.5!(B)$);\coordinate (L) at ($(B)!.5!(C)$);\coordinate (M) at ($(C)!.5!(D)$);\coordinate (N) at ($(D)!.5!(A)$);
\draw[vurgu,very thick] (K)--(L)--(M)--(N)--cycle;
\node[below left] at (A){A};\node[below right] at (B){B};\node[above right] at (C){C};\node[above left] at (D){D};
\node[below] at (K){K};\node[right] at (L){L};\node[above] at (M){M};\node[left] at (N){N};'''),
 'Köşegenleri 12 cm ve 20 cm olan bir dörtgenin kenar orta noktaları sırayla birleştiriliyor. Oluşan paralelkenarın çevresi kaç cm\'dir?',
 ['Orta tabana göre paralelkenarın kenarları köşegenlerin yarısıdır: 6 cm ve 10 cm.','Çevre = 2 · (6 + 10) = 32.'],
 '32 cm',
 'Orta tabanı yarım almayı unutmak ya da bir üçgenin alanını bulup bırakmak. Önce alan mı çevre mi istendiğine bak.',
 'Orta noktalar köşegenin yarısını verir.')

# 9 eşkenar
assert F(10**2,4)==25
K('geo-eskenar-ucgen-01','geo|Eşkenar Üçgen','Eşkenar üçgende yükseklik ve alan',
 'Eşkenar üçgenin yüksekliğini ve alanını kenar uzunluğundan köklü olarak yazabilmeni.',
 'Eşkenar üçgende yükseklik tabanı **ortalar** ve 30°-60°-90° üçgen oluşur. Kenar a ise **h = a√3 ÷ 2**, alan **a²√3 ÷ 4** olur. Yükseklik kenara eşit değildir. Burada √2 değil **√3** kuralı geçerlidir.',
 'h = a√3 / 2   ·   Alan = a²√3 / 4',
 tz(r'''\coordinate (A) at (0,0);\coordinate (B) at (4,0);\coordinate (C) at (2,3.46);\coordinate (H) at (2,0);
\draw (A)--(B)--(C)--cycle;\draw[vurgu,very thick] (C)--(H);\draw (2,.2)--(2.2,.2)--(2.2,0);
\node[below] at (1,0){$a/2$};\node[below] at (3,0){$a/2$};\node[left] at (.9,1.8){$a$};\node[right] at (2.05,1.5){$h$};'''),
 'Kenarı 10 cm olan eşkenar üçgenin yüksekliği ve alanı kaçtır?',
 ['h = 10√3 ÷ 2 = 5√3.','Alan = 10² · √3 ÷ 4 = 100√3 ÷ 4 = 25√3.'],
 'h = 5√3 cm, alan = 25√3 cm²',
 'Yarım kenara 45° kuralını (√2) uygulamak ya da yüksekliği kenara eşit sanmak. Eşkenar üçgenin açıları 60° olduğundan √3 gelir.',
 'Eşkenar üçgende yükseklik a√3/2.')

# 10 eşlik ve benzerlik
assert 2*4*3*4==96 and 6*16==96
K('geo-eslik-ve-02','geo|Eşlik ve Benzerlik','Ölçek ve gölge problemleri',
 'Uzunluk oranını alan oranına doğru çevirebilmeni ve gölge problemlerinde benzerlik kurabilmeni.',
 'Haritada ölçek her yerde aynıdır. Uzunluk **k kat** büyürse alan **k² kat** büyür; alanı ölçekle doğrudan çarpma. Aynı anda oluşan gölgelerde ışınlar paraleldir ve boy / gölge oranı eşittir. Eş üçgenlerde köşeler yazım sırasıyla eşleşir.',
 'Alan oranı = (uzunluk oranı)²',
 None,
 'Bir haritada 1 cm, gerçekte 4 km\'yi gösteriyor. Haritada 2 cm × 3 cm görünen dikdörtgen arazinin gerçek alanı kaç km²\'dir?',
 ['Gerçek kenarlar: 2 · 4 = 8 km ve 3 · 4 = 12 km.','Gerçek alan: 8 · 12 = 96 km².','Kontrol: haritada alan 6 cm², ölçeğin karesi 16: 6 · 16 = 96.'],
 '96 km²',
 'Haritadaki alanı ölçekle doğrudan çarpmak (6 · 4). Önce uzunlukları gerçeğe çevir ya da alan için ölçeğin karesini kullan.',
 'Uzunluk k kat, alan k² kat.')

# 11 katı cisimler
ust=[[2,3,1],[1,4,2]]
onden=sum(max(ust[r][c] for r in range(2)) for c in range(3)); assert onden==8 and sum(map(sum,ust))==13
K('geo-kati-cisimler-01','geo|Katı Cisimler','Birim küp yapıları ve görünümler',
 'Üstten görünümdeki sayılardan önden ve yandan görünümdeki birim kare sayısını bulabilmeni.',
 'Üstten görünümdeki sayı, o sütundaki **küp sayısıdır**. Önden görünümde her sütunun **en büyük** sayısı, yandan görünümde her sıranın **en büyük** sayısı görünür. Üst üste küpler tek görünümde tekrar sayılmaz. Yüzey alanında birleşen yüzler dışarıdan sayılmaz.',
 'Önden: sütun en büyükleri   ·   Yandan: sıra en büyükleri',
 None,
 'Üstten görünümü ön sırada 2 3 1, arka sırada 1 4 2 olan birim küp yapının önden görünümünde kaç birim kare vardır?',
 ['Önden bakınca her sütunun en büyüğü görünür: 2, 4 ve 2.','Birim kare sayısı: 2 + 4 + 2 = 8.'],
 '8 birim kare',
 'Toplam küp sayısını (13) ya da üstten görünümdeki kare sayısını vermek. Önden görünümde her sütunun yalnız en yüksek yığını sayılır.',
 'Görünümde her sütunun en yükseği sayılır.')

# 12 kenarortay
x=10; assert x+4==(3*x-2)/2 and 3*x-2==28
K('geo-kenarortay-02','geo|Kenarortay','Dik üçgende hipotenüs kenarortayı',
 'Hipotenüse ait kenarortay özelliğiyle denklem kurup doğru uzunluğu (kenarortayı mı, hipotenüsü mü) bulabilmeni.',
 'Dik üçgende hipotenüse ait kenarortay, hipotenüsün **yarısına** eşittir; orta nokta üç köşeye eşit uzaklıktadır. Ağırlık merkezi kenarortayı köşeden başlayarak **2 : 1** oranında böler. Denklemden x\'i bulunca soruda **hangi uzunluğun** istendiğine yeniden bak.',
 'Kenarortay = Hipotenüs ÷ 2',
 tz(r'''\coordinate (A) at (0,0);\coordinate (B) at (4,0);\coordinate (C) at (0,3);\coordinate (D) at (2,1.5);
\draw (A)--(B)--(C)--cycle;\draw[vurgu,very thick] (A)--(D);\draw (0,.25)--(.25,.25)--(.25,0);
\node[below left] at (A){A};\node[below right] at (B){B};\node[above left] at (C){C};\node[above right] at (D){D};
\fill (D) circle(1.5pt);'''),
 'A\'da dik olan ABC üçgeninde D, [BC]\'nin orta noktasıdır. |AD| = x + 4 ve |BC| = 3x − 2 ise |BC| kaçtır?',
 ['Hipotenüse ait kenarortay hipotenüsün yarısıdır: x + 4 = (3x − 2) ÷ 2.','2x + 8 = 3x − 2, yani x = 10.','|BC| = 3 · 10 − 2 = 28.'],
 '28',
 'Bulduğun x\'i ya da kenarortay uzunluğunu (14) hipotenüs sanmak. Son adımda sorulan uzunluğu yaz: hipotenüs kenarortayın iki katıdır.',
 'Hipotenüs, kenarortayın iki katıdır.')

# 13 koni
assert F(36*8,3)==96 and 96/16==6
K('geo-koni-02','geo|Koni','Koninin hacmi ve su aktarımı',
 'Koninin hacmini yükseklikle bulup suyu silindire aktarınca yeni yüksekliği hesaplayabilmeni.',
 'Koninin hacmi, aynı taban ve yükseklikli silindirin **üçte biridir**. Yükseklik tabana **dik** olan uzunluktur; ana doğru değildir. Yarıçapı kullan, çapı değil. Su aktarımında hacim **değişmez**: koninin hacmini silindirin πr²h ifadesine eşitle.',
 'V(koni) = πr²h ÷ 3   ·   V(silindir) = πr²h',
 None,
 'Yarıçapı 6 cm, yüksekliği 8 cm olan koni biçimli huni tamamen su dolu. Su, taban yarıçapı 4 cm olan silindire boşaltılırsa silindirde su kaç cm yükselir?',
 ['Huni hacmi: π · 6² · 8 ÷ 3 = 96π cm³.','Silindirde: π · 4² · h = 16π · h.','16π · h = 96π olduğundan h = 6.'],
 '6 cm',
 'Yükseklik yerine ana doğruyu (10) kullanmak ya da 1/3 çarpanını unutmak. Hacimde tabana dik yüksekliği al.',
 'Koni: taban alanı, yükseklik, üçte bir.')

# 14 küre
assert F(4*125,3)==F(500,3) and 4*25==100
K('geo-kure-01','geo|Küre','Kürenin hacmi',
 'Yarıçapı (gerekirse yüzey alanından) bulup kürenin hacmini hesaplayabilmeni.',
 'Kürenin hacmi **4πr³ ÷ 3**, yüzey alanı **4πr²**\'dir. r **yarıçaptır**, çap değil. Yüzey alanı verilmişse önce yarıçapı bul, sonra hacme geç. Hacim formülündeki ÷ 3\'ü unutma.',
 'V = 4πr³ ÷ 3   ·   A = 4πr²',
 None,
 'Yüzey alanı 100π cm² olan kürenin hacmi kaç cm³\'tür?',
 ['4πr² = 100π olduğundan r² = 25, yani r = 5.','V = 4π · 5³ ÷ 3 = 4π · 125 ÷ 3.','V = 500π / 3.'],
 '500π / 3 cm³',
 'Hacim yerine yüzey alanı formülünü kullanmak, ÷ 3\'ü unutmak ya da yarıçap yerine çap yazmak. Formülde r\'nin yarıçap olduğunu kontrol et.',
 'Hacim r³ ile, yüzey r² ile.')

# 15 noktanın analitiği
assert (1+7+4)//3==4 and (2+5+11)//3==6
K('geo-noktanin-analitigi-02','geo|Noktanın Analitiği','Ağırlık merkezi ve alan',
 'Köşe koordinatlarından üçgenin ağırlık merkezini ve çokgenin alanını bulabilmeni.',
 'Köşeleri (x₁, y₁), (x₂, y₂), (x₃, y₃) olan üçgenin ağırlık merkezi, apsislerin ve ordinatların **ayrı ayrı aritmetik ortalamasıdır**: üçe bölünür. Kareli zeminde alan için çokgeni saran dikdörtgenden **dışarıda kalan üçgenleri çıkar**.',
 'G = ((x₁ + x₂ + x₃) / 3 , (y₁ + y₂ + y₃) / 3)',
 None,
 'A(1, 2), B(7, 5), C(4, 11) köşeli üçgenin ağırlık merkezinin koordinatları nedir?',
 ['Apsis: (1 + 7 + 4) ÷ 3 = 4.','Ordinat: (2 + 5 + 11) ÷ 3 = 6.','G(4, 6).'],
 'G(4, 6)',
 'Toplamı ikiye bölmek ya da yalnız apsisi bulup ordinatı hesaplamamak. İki koordinat için de ayrı ayrı üçe böl.',
 'İki değil üç: köşe sayısına böl.')

# 16 paralelkenar
assert math.isqrt(13**2-12**2)==5 and 2*(5+9+13)==54
K('geo-paralelkenar-03','geo|Paralelkenar','Paralelkenarda yükseklik ve Pisagor',
 'Yükseklikle oluşan dik üçgenlerde Pisagor uygulayıp kenarı ve çevreyi bulabilmeni.',
 'Paralelkenarda karşılıklı kenarlar eşit, köşegenler birbirini ortalar. Çevre, iki komşu kenarın toplamının **iki katıdır**. Yükseklik çizilince oluşan her dik üçgene **ayrı ayrı Pisagor** uygula; parçaları toplayarak tabanı bul.',
 'Çevre = 2(a + b)   ·   Alan = taban · yükseklik',
 tz(r'''\coordinate (A) at (0,0);\coordinate (B) at (4.2,0);\coordinate (C) at (5.7,3.6);\coordinate (D) at (1.5,3.6);\coordinate (E) at (1.5,0);
\draw (A)--(B)--(C)--(D)--cycle;\draw[vurgu,very thick] (D)--(E);\draw (1.5,.22)--(1.72,.22)--(1.72,0);
\node[below left] at (A){A};\node[below right] at (B){B};\node[above right] at (C){C};\node[above left] at (D){D};\node[below] at (E){E};'''),
 'ABCD paralelkenarında D\'den [AB]\'ye inen dikmenin ayağı E\'dir. |AD| = 13, |DE| = 12 ve |EB| = 9 ise çevre kaçtır?',
 ['AED dik üçgeninde |AE| = √(13² − 12²) = 5.','|AB| = |AE| + |EB| = 5 + 9 = 14.','Çevre = 2 · (14 + 13) = 54.'],
 '54',
 'Yalnız dik üçgenin kenarlarını toplamak ya da |AD| + |DE| + |EB| yazmak. Çevre, paralelkenarın dört kenarının toplamıdır.',
 'Yükseklik çiz, dik üçgene Pisagor uygula.')

# 17 prizmalar
adaylar=[(2+3)**2+12**2,(2+12)**2+3**2,(3+12)**2+2**2]; assert min(adaylar)==169 and 13**2==169
K('geo-prizmalar-01','geo|Prizmalar','Prizmada en kısa yol',
 'Prizmayı açıp zıt köşeler arasındaki olası yolları karşılaştırarak en kısasını seçebilmeni.',
 'Yüzey üzerindeki yol, prizma açılınca **düz bir doğru parçası** olur. Dik üçgenin bir dik kenarı bir ayrıttır, diğeri ise **diğer iki ayrıtın toplamıdır**. Üç farklı açılım vardır; üçünü de hesaplayıp **en küçüğünü** seç.',
 'Yol² = (a + b)² + c²',
 tz(r'''\draw (0,0) rectangle (3,3.6);\draw (1.5,0)--(1.5,3.6);
\draw[vurgu,very thick] (0,0)--(3,3.6);
\node[below] at (.75,0){$a$};\node[below] at (2.25,0){$b$};\node[right] at (3,1.8){$c$};
\node[left] at (0,0){K};\node[right] at (3,3.6){L};'''),
 'Ayrıtları 2, 3 ve 12 cm olan dikdörtgenler prizmasının yüzeyinde, zıt köşeler arasındaki en kısa yol kaç cm\'dir?',
 ['Üç açılım: (2 + 3)² + 12² = 169; (2 + 12)² + 3² = 205; (3 + 12)² + 2² = 229.','En küçük değer 169, yani yol √169 = 13.'],
 '13 cm',
 'İki ayrıtın toplamını yol sanmak ya da yalnız tek açılımı hesaplamak. Her açılımda kalan ayrıt dik kenardır; üçünü de karşılaştır.',
 'Üç açılımı hesapla, en küçüğünü seç.')

# 18 silindir
assert 2*5*8==80 and 2*25==50 and 80+50==130
K('geo-silindir-01','geo|Silindir','Silindirin yanal ve tüm alanı',
 'Yanal alanı açınımdaki dikdörtgenden bulup kapakları ne zaman ekleyeceğini ayırt edebilmeni.',
 'Silindirin açınımında yan yüzey, kenarları **2πr** ve **h** olan bir dikdörtgendir. **Yanal alan = 2πrh**. Tüm yüzey alanı için iki kapağın alanı (2πr²) eklenir. Etiket ya da boya gibi sorularda kapaklar dahil değildir.',
 'Yanal = 2πrh   ·   Tüm = 2πrh + 2πr²',
 tz(r'''\draw (0,0) rectangle (4,1.8);\draw (1,2.4) circle(.6);\draw (1,-.6) circle(.6);
\node[above] at (3,1.8){$2\pi r$};\node[left] at (0,.9){$h$};\draw[vurgu,very thick] (1,2.4)--(1.6,2.4);\node[above] at (1.35,2.35){\footnotesize $r$};'''),
 'Yarıçapı 5 cm, yüksekliği 8 cm olan silindirin yanal alanı ve tüm yüzey alanı kaçtır?',
 ['Yanal alan: 2π · 5 · 8 = 80π.','İki kapak: 2 · π · 5² = 50π.','Tüm yüzey alanı: 80π + 50π = 130π.'],
 'Yanal 80π cm², tüm 130π cm²',
 'Yanal alandaki 2 çarpanını unutmak, hacmi (πr²h) hesaplamak ya da etiket sorusuna kapakları eklemek. İstenen alanın hangisi olduğuna bak.',
 'Yanal alan: çevre çarpı yükseklik.')

# 19 yamuk
a_,c_=6,18; assert (a_+c_)//2==12 and a_//2+(c_-a_)//2+a_//2==12 and (c_-a_)//2==6
K('geo-yamuk-02','geo|Yamuk','Yamukta orta taban ve benzerlik',
 'Orta tabanı ve köşegenlerin ayırdığı parçaları tabanlardan bulabilmeni.',
 'Orta taban tabanlara paraleldir; uzunluğu **tabanların ortalamasıdır**. Köşegenler onu üç parçaya ayırır: uç parçalar **küçük tabanın yarısı**, ortadaki parça **tabanlar farkının yarısıdır**. Paralel doğrularla oluşan küçük üçgenler benzerdir.',
 'Orta taban = (a + c) ÷ 2   ·   Ortadaki parça = (c − a) ÷ 2',
 tz(r'''\coordinate (D) at (0,0);\coordinate (C) at (6,0);\coordinate (A) at (1.5,2.4);\coordinate (B) at (3.5,2.4);
\draw (A)--(B)--(C)--(D)--cycle;\draw[dashed] (A)--(C);\draw[dashed] (B)--(D);
\coordinate (E) at (.75,1.2);\coordinate (F) at (4.75,1.2);\draw[vurgu,very thick] (E)--(F);
\node[above left] at (A){A};\node[above right] at (B){B};\node[below left] at (D){D};\node[below right] at (C){C};
\node[left] at (E){E};\node[right] at (F){F};\node[below] at (1.75,1.2){\small P};\node[below] at (3.75,1.2){\small Q};'''),
 '|AB| = 6 ve |DC| = 18 olan ABCD yamuğunun orta tabanı [EF], köşegenleri P ve Q noktalarında kesiyor. |PQ| kaçtır?',
 ['Orta taban: |EF| = (6 + 18) ÷ 2 = 12.','Uç parçalar küçük tabanın yarısıdır: 6 ÷ 2 = 3 ve 3.','|PQ| = 12 − 3 − 3 = 6 (ya da (18 − 6) ÷ 2 = 6).'],
 '6',
 'Yalnız uç parçayı bulup bırakmak ya da tabanlar farkını yarılamadan yazmak. Üç parçanın toplamı orta tabana eşit olmalı: kontrol et.',
 'Uç parça küçük tabanın yarısıdır.')

# 20 çemberde açı
assert (40+110)//2==75
K('geo-cemberde-aci-02','geo|Çemberde Açı','Teğet–kiriş, iç ve dış açı',
 'Açıyı gördüğü yaylara bağlayıp teğet–kiriş, iç ve dış açı ilişkilerinden doğrusunu seçebilmeni.',
 '**Teğet–kiriş açısı** gördüğü yayın yarısıdır; aynı yayı gören çevre açıya eşittir. **İç açı** (çember içinde kesişen kirişler) iki yayın toplamının yarısıdır. **Dış açı** büyük yayla küçük yayın farkının yarısıdır. Teğet doğrusunda açılar 180°\'ye tamamlanır.',
 'İç: (a + b) / 2   ·   Dış: (a − b) / 2   ·   Teğet–kiriş: yay / 2',
 tz(r'''\def\r{2}\draw (0,0) circle(\r);
\coordinate (P1) at (200:\r);\coordinate (P2) at (50:\r);\coordinate (P3) at (110:\r);\coordinate (P4) at (320:\r);
\path[name path=c1] (P1)--(P2);\path[name path=c2] (P3)--(P4);\path[name intersections={of=c1 and c2,by=X}];
\draw (P1)--(P2);\draw (P3)--(P4);
\draw[vurgu,very thick] (50:\r) arc(50:110:\r);\draw[vurgu,very thick] (200:\r) arc(200:320:\r);
\node at (80:2.45){$a$};\node at (260:2.5){$b$};\node[below] at ($(X)+(.05,.45)$){$x$};'''),
 'Bir çemberin içinde kesişen iki kirişin gördüğü yaylar 40° ve 110°\'dir. Kirişlerin yaptığı açı kaç derecedir?',
 ['İç açı, gördüğü iki yayın toplamının yarısıdır.','(40° + 110°) ÷ 2 = 75°.'],
 '75°',
 'Teğet ile kiriş arasındaki açıyı yayın kendisine eşit sanmak ya da iç açıda yayları çıkarmak. Açı yayın yarısıdır: yayı bulup ikiye böl.',
 'Açı, gördüğü yayın yarısıdır.')

# 21 çemberde uzun
assert math.isqrt(17**2-15**2)==8
K('geo-cemberde-uzun-01','geo|Çemberde Uzun','Merkezden kirişe dikme',
 'Merkezden kirişe dikmenin kirişi ortaladığını kullanıp Pisagorla dikme uzunluğunu bulabilmeni.',
 'Merkezden kirişe inen dikme kirişi **ortalar**. Yarıçap, yarım kiriş ve dikme bir **dik üçgen** kurar; yarıçap hipotenüstür. Önce kirişi ikiye böl, sonra Pisagor uygula. Kareyi bulunca karekök almayı unutma.',
 'r² = (kiriş ÷ 2)² + dikme²',
 tz(r'''\def\r{2.2}\draw (0,0) circle(\r);\coordinate (O) at (0,0);\coordinate (A) at (-1.775,-1.3);\coordinate (B) at (1.775,-1.3);\coordinate (H) at (0,-1.3);
\draw (A)--(B);\draw[vurgu,very thick] (O)--(H);\draw (O)--(B);\draw (0,-1.05)--(.25,-1.05)--(.25,-1.3);
\fill (O) circle(1.5pt);\node[above] at (O){O};\node[left] at (A){A};\node[right] at (B){B};\node[below] at (H){H};
\node[left] at (0,-.65){\small dikme};'''),
 'Yarıçapı 17 cm olan çemberde 30 cm uzunluğundaki bir kirişin merkeze uzaklığı kaç cm\'dir?',
 ['Dikme kirişi ortalar: yarım kiriş 30 ÷ 2 = 15.','Pisagor: dikme² = 17² − 15² = 289 − 225 = 64.','Dikme = 8.'],
 '8 cm',
 'Yarım kirişi ya da yarıçapı cevap sanmak, ya da kareyi bulup karekökü almayı unutmak. Dikme, dik üçgenin dik kenarıdır.',
 'Dikme kirişi ortalar, Pisagor çözer.')

# 22 çemberin analitiği
assert (0+5)**2+(2-2)**2==25
K('geo-cemberin-analitigi-02','geo|Çemberin Analitiği','Teğet çember ve nokta konumu',
 'Eksene teğet çemberin denklemini yazıp noktanın çembere göre konumunu belirleyebilmeni.',
 'Merkezi (a, b), yarıçapı r olan çemberin denklemi **(x − a)² + (y − b)² = r²**\'dir. y eksenine teğetse **r = |a|**, x eksenine teğetse **r = |b|** olur. Sağ tarafa r² yazılır. Nokta denklemde yerine konur: sonuç r²\'den küçükse içte, eşitse üzerinde, büyükse dışta.',
 '(x − a)² + (y − b)² = r²',
 tz(r'''\draw[->] (-4.4,0)--(1,0) node[right]{$x$};\draw[->] (0,-.5)--(0,3.4) node[above]{$y$};
\draw[fill=vurgu!10] (-2,1.5) circle(2);\fill (-2,1.5) circle(1.5pt);\node[above left] at (-2,1.5){M};
\draw[vurgu,very thick] (-2,1.5)--(0,1.5);\node[above] at (-1,1.5){$r$};\fill (0,1.5) circle(1.5pt);'''),
 'Merkezi (−5, 2) olan çember y eksenine teğettir. Çemberin denklemi nedir?',
 ['y eksenine teğet olduğundan yarıçap, merkezin apsisinin mutlak değeridir: r = |−5| = 5.','Denklem: (x + 5)² + (y − 2)² = 25.'],
 '(x + 5)² + (y − 2)² = 25',
 'Yarıçap yerine çapı yazmak, sağ tarafa r² yerine r koymak ya da hangi eksene teğet olunduğunu karıştırmak. Merkezin işaretini de ters yaz.',
 'y eksenine teğetse yarıçap apsistir.')

# 23 çokgenler
assert (6-2)*180-(130+140+110+120)==220 and 220//2==110
K('geo-cokgenler-03','geo|Çokgenler','Çokgende iç ve dış açılar',
 'İç açılar toplamını kenar sayısından bulup bilinmeyen eşit açıları ve düzgün çokgen açılarını hesaplayabilmeni.',
 'n kenarlı konveks çokgenin iç açılar toplamı **(n − 2) · 180°**, dış açılar toplamı **360°**\'dir. İç açı ile komşu dış açı 180°\'ye tamamlanır. Düzgün çokgende bir dış açı **360° ÷ n**\'dir. Eşit açıları, kalan toplamı bölerek bul.',
 'İç açılar toplamı = (n − 2) · 180°   ·   Dış açı = 360° ÷ n',
 None,
 'Bir altıgenin dört iç açısı 130°, 140°, 110° ve 120°\'dir. Kalan iki açı birbirine eşit ise her biri kaç derecedir?',
 ['Altıgenin iç açılar toplamı: (6 − 2) · 180° = 720°.','Verilen dört açı: 130° + 140° + 110° + 120° = 500°.','Kalan 720° − 500° = 220°; iki eşit açı: 220° ÷ 2 = 110°.'],
 '110°',
 'Kenar sayısını yanlış sayıp (n − 2) çarpanını bozmak ya da iç açı yerine komşu dış açıyı hesaplamak. Önce çokgenin kenarlarını say.',
 'İç toplam: (n − 2) kere 180°.')

# 24 üçgende alan
assert F(4,18)==F(2,9) and 72*F(2,9)==16
K('geo-ucgende-alan-01','geo|Üçgende Alan','Üçgende alan bölüşümü',
 'Tabanları orantılı ve yükseklikleri ortak üçgenlerde alanı paylaştırıp bilinmeyen uzunluğu bulabilmeni.',
 'Yüksekliği ortak üçgenlerin alanları **tabanlarıyla orantılıdır**. Kenarortay üçgeni **eşit alanlı** iki parçaya, üç kenarortay **altı eş alanlı** parçaya böler. Verilen alanları parçalara ayır; her parçanın tabanını ve yüksekliğini ayrı yaz.',
 'A₁ / A₂ = taban₁ / taban₂',
 tz(r'''\coordinate (A) at (1,3);\coordinate (B) at (0,0);\coordinate (C) at (6,0);\coordinate (D) at (2.4,0);
\draw (A)--(B)--(C)--cycle;\draw[vurgu,very thick] (A)--(D);\draw[dashed] (A)--(1,0);\node[left] at (1,1.5){$h$};
\node[above] at (A){A};\node[below left] at (B){B};\node[below right] at (C){C};\node[below] at (D){D};'''),
 'ABC üçgeninde D, [BC] üzerindedir. |BC| = 18, |BD| = 4 ve A(ABC) = 72 cm² ise A(ABD) kaç cm²\'dir?',
 ['ABD ve ABC üçgenlerinin A\'dan inen yüksekliği ortaktır; alan oranı taban oranıdır.','Oran: 4 / 18 = 2 / 9.','A(ABD) = 72 · 2 / 9 = 16.'],
 '16 cm²',
 'D\'yi orta nokta sanıp alanı yarıya bölmek ya da bulduğun yüksekliği uzunluk sanmak. Önce tabanların oranını yaz.',
 'Ortak yükseklikte alan oranı taban oranıdır.')

# 25 üçgende açılar
assert 180-(48+71)==61
K('geo-ucgende-acilar-01','geo|Üçgende Açılar','Paralel doğrular ve üçgende açılar',
 'Paralel doğruların ters açılarını üçgenin köşelerine taşıyıp bilinmeyen açıyı bulabilmeni.',
 'Paralel iki doğruyu bir doğru keserse **ters açılar** eşittir. Bu eşit açıları üçgenin köşelerine taşı. Sonra üçgenin iç açıları toplamının **180°** olduğunu kullan. Kırık çizgilerde **yardımcı paralel** çizip açıları iki parçada say.',
 'Üçgende A + B + C = 180°',
 tz(r'''\draw (-.6,2)--(5.6,2) node[right]{$d_1$};\draw (-.6,0)--(5.6,0) node[right]{$d_2$};
\coordinate (P) at (2.5,2);\coordinate (B) at (.3,0);\coordinate (C) at (4.8,0);
\draw[vurgu,very thick] (B)--(P)--(C);
\node[above left] at (P){P};\node at (1.6,2.25){\small $48^\circ$};\node at (3.55,2.25){\small $71^\circ$};\node at (2.5,1.5){$x$};'''),
 'd₁ // d₂ doğruları arasındaki üçgenin tepesi d₁ üzerindeki P noktasındadır, tabanı d₂ üzerindedir. d₁ doğrusunda P\'nin iki yanında 48° ve 71° görülüyor. Üçgenin P\'deki açısı x kaç derecedir?',
 ['Ters açılar eşit: taban açıları 48° ve 71°.','İç açılar toplamı: x = 180° − (48° + 71°).','x = 61°.'],
 '61°',
 'Yalnız bir köşedeki ters açıyı yazıp bırakmak ya da verilen iki açıyı toplayıp x sanmak. Üçüncü açıyı 180°\'den çıkararak bul.',
 'Ters açıyı taşı, 180°\'ye tamamla.')

# 26 benzerlik-01
assert F(6,6+9)==F(2,5) and 45*F(2,5)==18
K('geo-ucgende-benzerlik-01','geo|Üçgende Benzerlik','Benzerlik oranı, çevre ve alan',
 'Benzer üçgenlerde kenar oranından çevre ve alan oranını doğru kurabilmeni.',
 'Karşılıklı kenarlar aynı oranda büyür: **k = kenar oranı**. Benzer üçgenlerin çevreleri **k oranında**, alanları **k² oranındadır**. Oranı yazmadan önce her uzunluğun hangi üçgene ait olduğunu belirle ve karşılıklı kenarları eşleştir.',
 'Çevre oranı = k   ·   Alan oranı = k²',
 tz(r'''\coordinate (A) at (2,3.2);\coordinate (B) at (0,0);\coordinate (C) at (6,0);
\coordinate (D) at ($(A)!.4!(B)$);\coordinate (E) at ($(A)!.4!(C)$);
\draw (A)--(B)--(C)--cycle;\draw[vurgu,very thick] (D)--(E);
\node[above] at (A){A};\node[below left] at (B){B};\node[below right] at (C){C};\node[left] at (D){D};\node[right] at (E){E};'''),
 'ABC üçgeninde D ∈ [AB], E ∈ [AC] ve DE // BC\'dir. |AD| = 6, |DB| = 9 ve Çevre(ABC) = 45 cm ise Çevre(ADE) kaç cm\'dir?',
 ['|AB| = 6 + 9 = 15. ADE ile ABC benzerdir: k = |AD| / |AB| = 6 / 15 = 2 / 5.','Çevreler k oranındadır: 45 · 2 / 5 = 18.'],
 '18 cm',
 'Oranı |DB| / |AB| almak ya da büyük çevreden bir kenar çıkarmak. Küçük üçgenin kenarını büyük üçgenin karşılık gelen kenarına böl.',
 'Çevre k, alan k² kat.')

# 27 benzerlik-04
assert F(3,2)*12/2==9
K('geo-ucgende-benzerlik-04','geo|Üçgende Benzerlik','Gölge, kelebek ve iç içe benzerlik',
 'Hangi üçgenlerin benzer olduğunu görüp orantıyı doğru kurarak bilinmeyen uzunluğu bulabilmeni.',
 'Paralel doğrular ve ortak ya da ters açılar **benzerlik** kurar: iç içe üçgen, kelebek ve aynı anda gölge. Karşılıklı kenarları eşleştirip **orantı** yaz. Boy / gölge oranı sabittir. Farkla değil **oranla** çöz, sonucu gerçek hayata göre kontrol et.',
 'boy₁ / gölge₁ = boy₂ / gölge₂',
 tz(r'''\coordinate (A) at (0,2);\coordinate (B) at (2,2);\coordinate (O) at (1,1);\coordinate (D) at (3,-1);\coordinate (C) at (-1,-1);
\draw (A)--(B);\draw (C)--(D);\draw (A)--(D);\draw (B)--(C);
\draw[vurgu,very thick] (A)--(B);\draw[vurgu,very thick] (C)--(D);
\node[above left] at (A){A};\node[above right] at (B){B};\node[below left] at (C){C};\node[below right] at (D){D};\node[above] at (1,.95){O};'''),
 'Boyu 1,5 m olan bir kişinin gölgesi 2 m iken aynı anda bir ağacın gölgesi 12 m\'dir. Ağacın boyu kaç m\'dir?',
 ['Aynı anda boy / gölge oranı eşittir: 1,5 / 2 = x / 12.','x = 1,5 · 12 ÷ 2 = 9.'],
 '9 m',
 'Oranı ters kurmak ya da farkla orantı yapmak (12 − 2). Sonuç mantıklı mı bak: gölge uzunsa boy da uzundur.',
 'Önce eşleştir, sonra orantı kur.')

# 28 ikizkenar
assert 3*5+1==2*5+6==16 and 16+16+10==42
K('geo-ikizkenar-ucgen-03','geo|İkizkenar Üçgen','İkizkenar üçgende kenar ve çevre',
 'Eş kenarlardan x\'i bulup çevreyi hesaplayabilmeni ve yükseklikle dik üçgen kurabilmeni.',
 'İkizkenar üçgende iki kenar eşittir; **eş kenarların karşısındaki açılar da eşittir**. Tepeden tabana inen yükseklik tabanı **ortalar** ve dik üçgen oluşturur: Pisagor uygulanır. Denklemden x\'i bulduktan sonra istenenin kenar mı çevre mi olduğuna bak.',
 'Çevre = 2 · eş kenar + taban',
 tz(r'''\coordinate (B) at (0,0);\coordinate (C) at (4,0);\coordinate (A) at (2,3);\coordinate (H) at (2,0);
\draw (A)--(B)--(C)--cycle;\draw[vurgu,very thick] (A)--(H);\draw (2,.2)--(2.2,.2)--(2.2,0);
\draw[decoration={markings,mark=at position .5 with {\draw (0,-.12)--(0,.12);}},postaction={decorate}] (B)--(A);
\draw[decoration={markings,mark=at position .5 with {\draw (0,-.12)--(0,.12);}},postaction={decorate}] (A)--(C);
\node[above] at (A){A};\node[below left] at (B){B};\node[below right] at (C){C};\node[below] at (H){H};'''),
 'Bir ikizkenar üçgenin eş kenarları 3x + 1 ve 2x + 6, tabanı 10 cm\'dir. Çevresi kaç cm\'dir?',
 ['Eş kenarlar eşit: 3x + 1 = 2x + 6, yani x = 5.','Eş kenar: 3 · 5 + 1 = 16 cm.','Çevre = 16 + 16 + 10 = 42.'],
 '42 cm',
 'x\'i bulup bırakmak ya da bir eş kenarı (16) çevre sanmak. Son adımda üç kenarı da topladığından emin ol.',
 'x\'i bulunca soruyu yeniden oku.')

# ---- doğrulama ----
def kw(s): return len(s.split())
assert [k['id'] for k in kartlar]==ids, (set(ids)^set(k['id'] for k in kartlar))
for k in kartlar:
    for f in ['id','k','baslik','olcer','kural','hata','akilda']: assert k[f] and isinstance(k[f],str),(k['id'],f)
    assert kw(k['baslik'])<=6,(k['id'],'baslik'); assert kw(k['olcer'])<=25,(k['id'],'olcer',kw(k['olcer']))
    assert not k['olcer'].startswith('Bu soru'); assert kw(k['kural'])<=60,(k['id'],'kural',kw(k['kural']))
    assert kw(k['hata'])<=40,(k['id'],'hata',kw(k['hata'])); assert kw(k['akilda'])<=8,(k['id'],'akilda',kw(k['akilda']))
    assert '"' not in k['akilda'] and '“' not in k['akilda']
    o=k['ornek']; assert o['soru'] and o['cevap'] and 2<=len(o['adimlar'])<=4,(k['id'],'ornek')
    assert k['formul'] is None or k['formul'].strip()
    if k['sekil']: assert len(k['sekil'].encode())<=25000,(k['id'],len(k['sekil'].encode()))
json.dump(kartlar,open(CIKTI,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
sek=[k for k in kartlar if k['sekil']]
print(len(kartlar),'kart,',len(sek),'şekilli')
for k in sek: open(f'/tmp/kor/kart/p07/{k["id"]}.svg','w').write(k['sekil'])
