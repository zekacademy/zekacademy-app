import sys,re,json,math
from fractions import Fraction as F
sys.path.insert(0,'/home/claude/zekacademy-app/havuz')
from cizim import tikz_svg
GIRDI='/tmp/kor/kart/parti/p05.txt'
CIKTI='/home/claude/zekacademy-app/havuz/tekrar/kart-p05.json'
girdi=[]
for l in open(GIRDI,encoding='utf8'):
    m=re.match(r'^### (\S+) \| (.+?) \| (.+?) \| (\d+) soru',l)
    if m: girdi.append((m.group(1),m.group(2)))
K=dict(girdi)
def T(body,sc=.85): return tikz_svg(r'\begin{tikzpicture}[scale=%s,font=\small]'%sc+body+r'\end{tikzpicture}')
def ra(P,u,v,s=.25):
    ux,uy=u;vx,vy=v;px,py=P
    a=(px+s*ux,py+s*uy);b=(px+s*ux+s*vx,py+s*uy+s*vy);c=(px+s*vx,py+s*vy)
    return r'\draw (%.3f,%.3f)--(%.3f,%.3f)--(%.3f,%.3f);'%(a+b+c)
def unit(a,b):
    d=math.hypot(b[0]-a[0],b[1]-a[1]);return ((b[0]-a[0])/d,(b[1]-a[1])/d)
kartlar={}
def kart(id,baslik,olcer,kural,formul,sekil,soru,adimlar,cevap,hata,akilda):
    kartlar[id]={"id":id,"k":K[id],"baslik":baslik,"olcer":olcer,"kural":kural,"formul":formul,"sekil":sekil,
      "ornek":{"soru":soru,"adimlar":adimlar,"cevap":cevap},"hata":hata,"akilda":akilda}

# 1 açı-kenar
A_,B_,C_=70,45,180-70-45; assert C_==65 and A_>C_>B_
kart("geo-aci-kenar-01","Açı–kenar sıralaması",
 "Üçgende açıların sırasından karşılarındaki kenarların sırasını çıkarabildiğini.",
 "Üçgende **büyük açının karşısında büyük kenar** bulunur; eşit açıların karşısındaki kenarlar da eşittir. Önce her açının karşısındaki kenarı yaz, sonra açı sırasını kenarlara aynen aktar. Eksik açıyı iç açılar toplamından (180°) bul.",
 "m(A) > m(B) ⇒ |BC| > |AC|",
 T(r'''\draw (0,0)coordinate(B)--(5,0)coordinate(C)--(3.4,3.4)coordinate(A)--cycle;
\node[below left]at(B){B};\node[below right]at(C){C};\node[above]at(A){A};
\node at(3.4,2.6){$70^\circ$};\node at(.9,.3){$45^\circ$};\node at(4.15,.3){$65^\circ$};'''),
 "ABC üçgeninde m(A) = 70° ve m(B) = 45° ise |AB|, |BC|, |AC| kenarlarını büyükten küçüğe sırala.",
 ["Üçüncü açı: m(C) = 180° − 70° − 45° = 65°.","Karşılar: A → |BC|, B → |AC|, C → |AB|.","Açı sırası A > C > B olduğundan kenar sırası |BC| > |AB| > |AC|."],
 "|BC| > |AB| > |AC|",
 "Her kenarı komşu açıyla eşleştirmek (A → AB gibi). Kontrol: |BC| kenarının karşısındaki köşe A'dır; kenar adında geçmeyen harf karşı açıdır.",
 "Büyük açının karşısı büyük kenar.")

# 2 açıortay
BIC=134; Ak=2*(BIC-90); assert Ak==88 and 180-(180-Ak)//2==BIC
Bp=(0,0);Cp=(5,0);Ap=(1.8,3.2)
a_=math.dist(Bp,Cp);b_=math.dist(Cp,Ap);c_=math.dist(Ap,Bp);s_=a_+b_+c_
I=((a_*Ap[0]+b_*Bp[0]+c_*Cp[0])/s_,(a_*Ap[1]+b_*Bp[1]+c_*Cp[1])/s_)
kart("geo-aciortay-02","İç açıortaylar ve açı hesabı",
 "Açıortayların kesiştiği noktadaki açıdan üçgenin köşe açısına geçebildiğini.",
 "Üçgenin iç açıortayları **I** noktasında (iç teğet çemberin merkezi) kesişir; I kenarlara eşit uzaktadır. B ve C açıortaylarının oluşturduğu açı **m(BIC) = 90° + m(A)/2** olur. Açıortay açıyı iki eş açıya böler.",
 "m(BIC) = 90° + m(A) / 2",
 T(r'''\coordinate(B)at(0,0);\coordinate(C)at(5,0);\coordinate(A)at(1.8,3.2);\coordinate(I)at(%.3f,%.3f);
\draw(B)--(C)--(A)--cycle;\draw[thick,vurgu](B)--(I)(C)--(I);\draw[dashed,vurgu](A)--(I);
\fill(I)circle(.05);\node[below left]at(B){B};\node[below right]at(C){C};\node[above]at(A){A};\node[right]at(I){I};
\node at(%.3f,%.3f){$134^\circ$};'''%(I+(I[0]-.1,I[1]-.55)),.9),
 "ABC üçgeninde iç açıortaylar I noktasında kesişiyor. m(BIC) = 134° ise m(A) kaçtır?",
 ["90° çıkar: 134° − 90° = 44° (bu, A'nın yarısı).","2 ile çarp: 44° · 2 = 88°.","Kontrol: B/2 + C/2 = 46°, 180° − 46° = 134° ✓."],
 "m(A) = 88°",
 "BIC ile A'yı bütünler sanmak ya da 90° çıkardıktan sonra 2 ile çarpmayı unutmak. Kontrol: A'nın yarısı BIC'den 90° eksiktir.",
 "Önce 90° çıkar, sonra ikiyle çarp.")

# 3 çevre / bant
n,r=4,3; duz=2*(n-1)*2*r; assert duz==36
kart("geo-dairede-cevre-02","Tekerlek turu ve bant uzunluğu",
 "Çember çevresini kullanarak tur sayısını ve çemberleri saran bandın uzunluğunu hesaplayabildiğini.",
 "Çemberin çevresi **2πr**'dir. Tekerlekte tur sayısı = yol ÷ çevre. Yan yana çemberleri saran bantta **düz parçaları ve yayları ayrı ayrı** say: uçlardaki iki yarım çember bir tam çember eder, aralarda alttan ve üstten düz parçalar vardır.",
 "Bant = düz parçalar + 2πr",
 T(r'''\foreach \x in {0,2,4,6}{\draw(\x,0)circle(1);\fill(\x,0)circle(.05);}
\draw[very thick,vurgu](0,1)--(6,1)(0,-1)--(6,-1);\draw[very thick,vurgu](0,-1)arc(-90:-270:1);\draw[very thick,vurgu](6,-1)arc(-90:90:1);
\draw(6,0)--(6.7,.7)node[right]{$r$};''',.55),
 "Yarıçapı 3 cm olan 4 özdeş çember teğet olarak yan yana dizilip bir bantla sarılıyor. Bandın uzunluğu kaç cm'dir?",
 ["Düz parçalar: 3 aralık var, her biri 2r = 6; alt ve üst için 2 · 3 · 6 = 36.","Yaylar: uçlardaki iki yarım çember bir tam çember eder, 2π · 3 = 6π.","Toplam: 36 + 6π."],
 "(36 + 6π) cm",
 "Yalnız yayları ya da yalnız düz parçaları yazmak. Kontrol: bant kapalı bir çizgidir; cevapta hem π'li hem π'siz terim olmalı.",
 "Düz ve yayı ayrı ayrı say.")

# 4 deltoid
AB,CB,BD=13,15,24; h=BD//2; pa=math.isqrt(AB*AB-h*h); pc=math.isqrt(CB*CB-h*h); assert pa*pa+h*h==AB*AB and pc*pc+h*h==CB*CB
AC=pa+pc; top=2*AB+2*CB+BD+AC; assert (pa,pc,AC,top)==(5,9,14,94)
kart("geo-deltoid-02","Deltoidde çıta ve çevre",
 "Deltoidin simetri özelliğinden köşegen uzunluklarını bulup toplam uzunluğu hesaplayabildiğini.",
 "Deltoidde **iki çift komşu kenar eşittir**. Eşit kenarların köşelerini birleştiren köşegen simetri eksenidir; diğer köşegeni **dik keser ve ortalar**. Eksik parçaları dik üçgende Pisagorla bul. Toplam uzunlukta her parçayı bir kez say.",
 "Alan = köşegenler çarpımı ÷ 2",
 T(r'''\coordinate(A)at(-1.25,0);\coordinate(B)at(0,-3);\coordinate(C)at(2.25,0);\coordinate(D)at(0,3);
\draw(A)--(B)--(C)--(D)--cycle;\draw[dashed,vurgu](B)--(D)(A)--(C);
\node[left]at(A){A};\node[below]at(B){B};\node[right]at(C){C};\node[above]at(D){D};
\node[left]at(-.7,-1.5){13};\node[right]at(1.2,-1.5){15};\node[right]at(0,1.7){24};''',.7),
 "Deltoid biçimli bir iskelette |AB| = |AD| = 13, |CB| = |CD| = 15 ve |BD| = 24 cm'dir. Tüm kenar ve köşegen çıtalarının toplamı kaç cm'dir?",
 ["[AC], [BD]'yi ortalar: yarısı 12. A tarafı √(13² − 12²) = 5, C tarafı √(15² − 12²) = 9.","|AC| = 5 + 9 = 14.","Toplam: 2·13 + 2·15 + 24 + 14 = 94."],
 "94 cm",
 "Yalnız kenar çıtalarını toplayıp köşegen çıtalarını unutmak. Kontrol: 4 kenar ve 2 köşegeni tek tek yazıp işaretle.",
 "Parçaları tek tek yaz, birer kez say.")

# 5 pisagor
mer,alt=20,12; hh=math.isqrt(mer*mer-alt*alt); assert hh*hh==mer*mer-alt*alt==256 and hh==16
kart("geo-dik-ucgen-03","Pisagor bağıntısı",
 "Dik üçgende iki kenar bilinirken üçüncü kenarı Pisagorla bulabildiğini.",
 "Dik üçgende **dik kenarların kareleri toplamı hipotenüsün karesine eşittir**. Hipotenüs dik açının karşısındaki en uzun kenardır. 3-4-5, 5-12-13, 8-15-17 üçlülerini ve katlarını bil. Merdiven, duvar ve zemin bir dik üçgen kurar; merdiven hipotenüstür.",
 "a² + b² = c²",
 T(r'''\draw(0,0)--(3,0)--(0,4)--cycle;\draw(0,.3)--(.3,.3)--(.3,0);\draw[very thick,vurgu](3,0)--(0,4);
\node[below]at(1.5,0){12 m};\node[above right]at(1.5,2){20 m};\node[left]at(0,2){h};''',.8),
 "Duvara dayalı 20 m'lik bir merdivenin alt ucu duvardan 12 m uzaktadır. Merdiven duvarda kaç metre yüksekliğe ulaşır?",
 ["Merdiven hipotenüstür: c = 20, bir dik kenar 12.","h² = 20² − 12² = 400 − 144 = 256.","h = √256 = 16."],
 "16 m",
 "Uzunlukları toplamak ya da çarpmak, kare farkını bulup karekökü almayı unutmak. Kontrol: dik kenar hipotenüsten kısadır.",
 "Dik kenarların kareleri toplamı hipotenüs karesi.")

# 6 doğruda açılar
x=(180-10+5)//5; assert 5*x+5==180 and x==35 and 2*x-5==65 and 3*x+10==115
Bx,By=2.5*math.cos(math.radians(65)),2.5*math.sin(math.radians(65))
kart("geo-dogruda-acilar-01","Doğru üzerinde bitişik açılar",
 "Bir doğru üzerindeki açıların toplamının 180° olduğunu kullanıp sorulan açıya ulaşabildiğini.",
 "Bir doğru üzerindeki bitişik açıların toplamı **180°**'dir (bütünler açılar). Tümler açıların toplamı 90°'dir. Açıortay açıyı iki eş parçaya böler. Önce denklemi kur, x'i bul, sonra **sorulan açıya dön**.",
 "Doğru üzerinde: α + β = 180°",
 T(r'''\draw[thick](-3,0)--(3,0);\draw(0,0)--(%.3f,%.3f);\fill(0,0)circle(.06);
\node[below left]at(-3,0){A};\node[below right]at(3,0){C};\node[below]at(0,0){O};\node[above]at(%.3f,%.3f){B};
\node at(1.35,.6){$2x-5$};\node at(-.95,1.1){$3x+10$};'''%(Bx,By,Bx,By),.8),
 "[AC] doğru parçası üzerindeki O noktası ve dışındaki B noktası için m(AOB) = 3x + 10° ve m(BOC) = 2x − 5° ise m(BOC) kaçtır?",
 ["Bitişik açılar: 3x + 10 + 2x − 5 = 180.","5x + 5 = 180 → x = 35.","Sorulan açı: m(BOC) = 2 · 35 − 5 = 65°."],
 "65°",
 "x'i bulunca durmak ya da 2x gibi bir katsayıyı atlamak. Kontrol: son satırda istenen açıyı yaz ve iki açının toplamının 180° olduğunu doğrula.",
 "x'i bulunca sorulan açıya dön.")

# 7 analitik
k=3; m1=F(-(k+1),2); m2=F(-1,-2); assert m1*m2==-1 and m2==F(1,2)
kart("geo-dogrunun-analitigi-02","Paralel ve dik doğrular",
 "Doğru denkleminden eğimi okuyup paralellik ve diklik koşullarını uygulayabildiğini.",
 "ax + by + c = 0 doğrusunun eğimi **−a/b**'dir. **Paralel** doğruların eğimleri eşittir (m₁ = m₂). **Dik** doğruların eğimleri çarpımı −1'dir (m₁ · m₂ = −1). Önce iki doğrunun eğimini yaz, sonra koşulu kur.",
 "Paralel: m₁ = m₂ · Dik: m₁ · m₂ = −1",
 None,
 "(k + 1)x + 2y − 5 = 0 doğrusu x − 2y + 3 = 0 doğrusuna dik ise k kaçtır?",
 ["x − 2y + 3 = 0 doğrusunun eğimi −1/(−2) = 1/2.","Birinci doğrunun eğimi −(k + 1)/2.","Dik olduğu için (1/2) · (−(k + 1)/2) = −1, buradan k + 1 = 4 ve k = 3."],
 "k = 3",
 "Paralel yerine dik koşulunu kullanmak ya da eğimi ters (−b/a) yazmak. Kontrol: eğimi hep −a/b diye yaz; paralelde eşitle, dikte çarpımı −1 yap.",
 "Paralelde eşitle, dikte çarp.")

# 8 dönüşüm
P=(5,3);M=(2,1);u,v=P[0]-M[0],P[1]-M[1]; Q=(M[0]-v,M[1]+u); assert (u,v)==(3,2) and Q==(0,4)
kart("geo-donusum-geometrisi-02","Dönme ve simetri",
 "Bir noktanın verilen yönde döndürülmüş konumunu ve şekillerin simetri eksenlerini bulabildiğini.",
 "Orijin etrafında **saat yönünde 90°**: (x, y) → (y, −x). **Saatin tersi yönünde 90°**: (x, y) → (−y, x). 180°: (−x, −y). Merkez başka bir noktaysa önce merkezden noktaya giden farkı döndür, sonra merkezi ekle. Düzgün n kenarlı çokgenin n simetri ekseni vardır.",
 "Saatin tersi 90°: (x, y) → (−y, x)",
 None,
 "P(5, 3) noktası M(2, 1) etrafında saatin tersi yönünde 90° döndürülüyor. Yeni konumunu bul.",
 ["M'den P'ye fark: (5 − 2, 3 − 1) = (3, 2).","Saatin tersi 90°: (u, v) → (−v, u) = (−2, 3).","Merkezi ekle: (2 − 2, 1 + 3) = (0, 4)."],
 "(0, 4)",
 "Dönme yönünü karıştırmak ya da merkez orijin değilken farkı almadan döndürmek. Kontrol: noktayı kabaca çiz, hangi bölgeye gittiğine bak.",
 "Önce farkı al, sonra döndür.")

# 9 eşkenar dörtgen
ke,d1=10,12; yar=math.isqrt(ke*ke-(d1//2)**2); d2=2*yar; assert yar==8 and d1*d2//2==96
kart("geo-eskenar-dortgen-01","Eşkenar dörtgenin alanı",
 "Kenar ve bir köşegenden diğer köşegeni bulup eşkenar dörtgenin alanını hesaplayabildiğini.",
 "Eşkenar dörtgende dört kenar eşittir; köşegenler birbirini **dik ortalar**. Yarım köşegenler ve kenar bir dik üçgen kurar (Pisagor). Alan = **köşegenler çarpımının yarısı**. Taban × yükseklik de geçerlidir.",
 "Alan = (d₁ · d₂) ÷ 2",
 T(r'''\coordinate(A)at(-3.2,0);\coordinate(B)at(0,-2.4);\coordinate(C)at(3.2,0);\coordinate(D)at(0,2.4);
\draw(A)--(B)--(C)--(D)--cycle;\draw[dashed,vurgu](A)--(C)(B)--(D);'''+ra((0,0),(1,0),(0,1),.3)+r'''
\node[left]at(A){A};\node[below]at(B){B};\node[right]at(C){C};\node[above]at(D){D};
\node[below right]at(1.6,-1.2){10};\draw[<->](-.5,-2.4)--(-.5,2.4);\node[left]at(-.5,1.2){12};\node[above]at(1.6,0){?};''',.8),
 "Kenarı 10 cm, bir köşegeni 12 cm olan eşkenar dörtgenin alanı kaç cm²'dir?",
 ["Yarım köşegen 6, kenar 10 (hipotenüs).","Diğer yarım köşegen √(10² − 6²) = 8, köşegen 16.","Alan = 12 · 16 ÷ 2 = 96."],
 "96 cm²",
 "Çevreyi hesaplamak ya da yarım köşegenleri çarpıp alan saymak. Kontrol: alan için tam köşegenleri çarpıp ikiye böl.",
 "Tam köşegenleri çarp, ikiye böl.")

# 11 kare
d=12; assert (d*d)//2==72 and (6*6*2)==72
kart("geo-kare-01","Karede köşegen ve alan",
 "Karenin kenarı, köşegeni ve alanı arasında geçiş yapabildiğini.",
 "Kenarı a olan karede köşegen **a√2**, alan **a²**'dir; buradan alan = köşegenin karesi ÷ 2 olur. Köşegenler eşittir, birbirini dik ortalar ve köşe açılarını 45°'ye böler. Karo döşemede kenar = karo sayısı × karo kenarıdır.",
 "d = a√2 · Alan = d² ÷ 2",
 T(r'''\draw(0,0)rectangle(3,3);\draw[thick,vurgu](0,0)--(3,3);'''+ra((3,0),(-1,0),(0,1),.3)+r'''
\node[below]at(1.5,0){$a$};\node[above left]at(1.5,1.5){$d$};''',.8),
 "Köşegeni 12 cm olan karenin alanı kaç cm²'dir?",
 ["d = a√2 olduğundan a = 12 ÷ √2 = 6√2.","Alan = a² = (6√2)² = 72.","Kontrol: d² ÷ 2 = 144 ÷ 2 = 72."],
 "72 cm²",
 "Köşegeni kenar sanıp d²'yi (burada 144) alan yazmak. Kontrol: köşegen kenardan uzundur; alan köşegenin karesinin yarısıdır.",
 "Kare alanı, köşegen karesinin yarısı.")

# 12 katı cisimler
a_,dg=4,9; hq=math.isqrt(dg*dg-2*a_*a_); assert hq*hq==49 and hq==7; ya=2*a_*a_+4*a_*hq; assert ya==144
kart("geo-kati-cisimler-02","Prizma: köşegen, alan, eleman sayısı",
 "Cisim köşegeninden yüksekliği bulup yüzey alanını ve prizmanın yüz, köşe, ayrıt sayısını hesaplayabildiğini.",
 "Cisim köşegeni **d² = a² + b² + h²**'dir. Tüm yüzey alanı = **2 × taban alanı + yanal alan**; yanal alan = taban çevresi × yükseklik. Tabanı n kenarlı prizmada yüz sayısı n + 2, köşe 2n, ayrıt 3n'dir.",
 "A = 2 · taban + çevre · h",
 None,
 "Taban kenarı 4 cm olan kare dik prizmanın cisim köşegeni 9 cm'dir. Tüm yüzey alanı kaç cm²'dir?",
 ["81 = 4² + 4² + h² → h² = 49, h = 7.","İki taban: 2 · 16 = 32.","Yanal alan: 4 · 4 · 7 = 112; toplam 32 + 112 = 144."],
 "144 cm²",
 "Yalnız yanal alanı bulup tabanları eklememek ya da yan yüzü iki tane saymak. Kontrol: kare prizmada 2 taban + 4 yan yüz = 6 yüz say.",
 "İki taban, dört yan yüz.")

# 13 kenarortay
AD=21; k_=AD//3; assert (2*k_,k_)==(14,7)
G=((1.2+0+5)/3,3.5/3)
kart("geo-kenarortay-03","Ağırlık merkezi ve kenarortay",
 "Ağırlık merkezinin kenarortayı 2 : 1 oranında böldüğünü kullanıp uzunluk bulabildiğini.",
 "Kenarortaylar **ağırlık merkezi G**'de kesişir. G, her kenarortayı köşeden başlayarak **2 : 1** oranında böler: köşe tarafı 2k, kenar tarafı k, kenarortayın tamamı **3k**'dır. G'den tabana çizilen paralel benzerlikle bulunur.",
 "|AG| = 2 · |GD| · |AD| = 3 · |GD|",
 T(r'''\coordinate(A)at(1.2,3.5);\coordinate(B)at(0,0);\coordinate(C)at(5,0);\coordinate(D)at(2.5,0);\coordinate(G)at(%.3f,%.3f);
\draw(B)--(C)--(A)--cycle;\draw[thick,vurgu](A)--(D);\fill(G)circle(.06);
\node[above]at(A){A};\node[below left]at(B){B};\node[below right]at(C){C};\node[below]at(D){D};\node[right]at(G){G};
\node[left]at(1.7,2.4){14};\node[left]at(2.25,.55){7};'''%G,.85),
 "ABC üçgeninde [AD] kenarortay, G ağırlık merkezidir. |AD| = 21 cm ise |AG| ve |GD| kaçtır?",
 ["Kenarortayın tamamı 3k = 21, buradan k = 7.","Kenar tarafı kısa parçadır: |GD| = k = 7.","Köşe tarafı uzun parçadır: |AG| = 2k = 14."],
 "|AG| = 14 cm, |GD| = 7 cm",
 "Oranı ters kurmak ya da yalnız |AG|'yi bulup tüm kenarortay sorulmuşken |GD|'yi eklememek. Kontrol: köşe tarafı hep uzun parçadır.",
 "Köşe tarafı iki, kenar tarafı bir.")

# 14 küp
a=5; assert 12*a==60 and 6*a*a==150
kart("geo-kup-01","Küpün köşegenleri ve yüzey alanı",
 "Küpün ayrıtı, yüz köşegeni, cisim köşegeni ve yüzey alanı arasında geçiş yapabildiğini.",
 "Ayrıtı a olan küpte **yüz köşegeni a√2**, **cisim köşegeni a√3**'tür. Küpün **12 ayrıtı**, 6 yüzü, 8 köşesi vardır. Yüzey alanı 6a², hacmi a³'tür. Önce cisim köşegeninden a'yı bul.",
 "d = a√3 · A = 6a² · V = a³",
 T(r'''\draw(0,0)rectangle(2,2);\draw(0,2)--(1,2.8)--(3,2.8)--(2,2);\draw(2,0)--(3,.8)--(3,2.8);
\draw[dashed](0,0)--(1,.8)--(3,.8)(1,.8)--(1,2.8);\draw[very thick,vurgu](0,0)--(3,2.8);
\node[below]at(1,0){$a$};\node[below right]at(1.5,1.55){$d$};''',.9),
 "Cisim köşegeni 5√3 cm olan küpün tüm ayrıtlarının uzunlukları toplamı kaç cm'dir?",
 ["a√3 = 5√3 olduğundan ayrıt a = 5.","Küpün 12 ayrıtı var: 12 · 5 = 60.","Kontrol: yüz köşegeni 5√2, cisim köşegeninden kısadır."],
 "60 cm",
 "Ayrıt sayısını 6 ya da 8 almak (8, köşe sayısıdır) veya yalnız bir yüzün çevresini bulmak. Kontrol: küpte 12 ayrıt, 6 yüz, 8 köşe vardır.",
 "On iki ayrıt, altı yüz, sekiz köşe.")

# 15 küre
R_,d_=10,6; r_=math.isqrt(R_*R_-d_*d_); assert r_==8
kart("geo-kure-02","Kürenin kesit dairesi",
 "Küreyi bir düzlemle kesen dairenin yarıçapını Pisagorla bulup alanını hesaplayabildiğini.",
 "Düzlemle kesilen kürenin kesiti **dairedir**. Kürenin yarıçapı R, merkezin düzleme uzaklığı d ise kesit yarıçapı **r² = R² − d²**'dir. Kürenin yüzey alanı 4πR²'dir; yarım kürenin eğri yüzeyi bunun yarısıdır, tabanla birlikte 3πR² olur.",
 "r² = R² − d²",
 None,
 "Yarıçapı 10 cm olan bir küre, merkeze 6 cm uzaklıktaki düzlemle kesiliyor. Kesit dairenin alanı kaç cm²'dir?",
 ["R, d ve r dik üçgen kurar: r² = 10² − 6² = 100 − 36 = 64.","r = 8 cm.","Alan = π · 8² = 64π."],
 "64π cm²",
 "Yarıçapların farkını (R − d) ya da toplamını kesit yarıçapı saymak. Kontrol: R hipotenüstür, d ve r dik kenarlardır.",
 "R hipotenüs, d ve r dik kenar.")

# 16 paralelkenar
Ac=28; Bc=90-Ac; assert Bc==62 and 180-Bc==118
al=math.radians(Ac); L=4*math.cos(al); Cc=(L*math.cos(al),L*math.sin(al)); Dd=(Cc[0]-4,Cc[1])
uCA=unit(Cc,(0,0)); uCB=unit(Cc,(4,0))
kart("geo-paralelkenar-01","Paralelkenarda açılar",
 "Paralelkenarın açı özelliklerini ve üçgenlerdeki açı bağıntılarını birlikte kullanabildiğini.",
 "Paralelkenarda **karşılıklı açılar eşit**, komşu açılar **bütünlerdir** (toplamları 180°). Üçgenin iç açıları toplamı 180°'dir. Önce köşegenle oluşan üçgenden bir köşe açısını bul, sonra karşılıklı eşitliği ya da bütünlüğü kullan.",
 "m(A) = m(C) · m(A) + m(B) = 180°",
 T(r'''\coordinate(A)at(0,0);\coordinate(B)at(4,0);\coordinate(C)at(%.3f,%.3f);\coordinate(D)at(%.3f,%.3f);
\draw(A)--(B)--(C)--(D)--cycle;\draw[dashed,vurgu](A)--(C);%s
\node[below left]at(A){A};\node[below right]at(B){B};\node[above right]at(C){C};\node[above left]at(D){D};
\node at(.95,.2){$28^\circ$};\node at(%.3f,%.3f){$x$};'''%(Cc+Dd+(ra(Cc,uCA,uCB,.25),Dd[0]+.45,Dd[1]-.3)),.9),
 "ABCD paralelkenarında [AC] köşegeni [BC]'ye diktir ve m(CAB) = 28°'dir. m(ADC) kaçtır?",
 ["ABC üçgeninde C = 90°, A = 28° → m(ABC) = 62°.","Karşılıklı açılar eşit: m(ADC) = m(ABC) = 62°.","Kontrol: m(BAD) = 180° − 62° = 118° ve 118° + 62° = 180° ✓."],
 "62°",
 "Dik açıyı ya da verilen açıyı cevap sanmak; karşılıklı yerine komşu açıyı (bütünleyeni) yazmak. Kontrol: istenen açının hangi köşede olduğunu işaretle.",
 "Karşılıklı eşit, komşu bütünler.")

# 17 piramit
a,hy=10,13; assert a*a+4*(a*hy//2)==360
kart("geo-piramit-01","Kare dik piramidin yüzey alanı",
 "Piramidin tüm yüzey alanını taban ve yan yüzlerin alanlarını ayrı ayrı bularak hesaplayabildiğini.",
 "Tüm yüzey alanı = **taban alanı + yan yüzlerin alanları toplamı**. Kare dik piramitte dört yan yüz eş ikizkenar üçgendir; her birinin alanı **taban kenarı × yan yüz yüksekliği ÷ 2**'dir. Açınımda bir kare ve dört üçgen görürsün.",
 "A = a² + 4 · (a · h ÷ 2)",
 None,
 "Taban kenarı 10 cm, yan yüz yüksekliği 13 cm olan kare dik piramidin tüm yüzey alanı kaç cm²'dir?",
 ["Taban: 10² = 100.","Bir yan yüz: 10 · 13 ÷ 2 = 65; dört tane 260.","Toplam: 100 + 260 = 360."],
 "360 cm²",
 "Yalnız tabanı ya da yalnız yan yüzleri hesaplamak, ya da tek bir yan yüz eklemek. Kontrol: toplam 5 yüz var (1 taban, 4 üçgen); çadırda zemin dahil mi diye bak.",
 "Taban artı dört yan yüz.")

# 18 prizmalar
V=40*25*30; assert V==30000 and V//1000==30 and 30//5==6
kart("geo-prizmalar-02","Su aktarma ve doldurma süresi",
 "Dikdörtgen prizma biçimli kapta su hacmini bulup litreye çevirerek doldurma süresini hesaplayabildiğini.",
 "Prizmanın hacmi **taban alanı × yükseklik**'tir (a · b · c). **1 litre = 1000 cm³**. Doldurma süresi = suyun hacmi (litre) ÷ musluğun debisi (litre/dakika). Su yüksekliği sorulursa kabın tamamını değil, **suyun yüksekliğini** kullan.",
 "Süre = hacim (L) ÷ debi (L/dk)",
 None,
 "Tabanı 40 cm × 25 cm olan boş bir akvaryum, dakikada 5 litre su akıtan musluktan 30 cm yüksekliğe kadar dolduruluyor. Kaç dakika sürer?",
 ["Su hacmi: 40 · 25 · 30 = 30 000 cm³.","Litreye çevir: 30 000 ÷ 1000 = 30 L.","Süre: 30 ÷ 5 = 6 dakika."],
 "6 dakika",
 "1 litreyi 100 cm³ sanmak, kabın tüm yüksekliğini almak ya da debiye bölmeyi unutmak. Kontrol: birimleri sırayla yaz: cm³ → L → dakika.",
 "Önce cm³'ü litreye çevir.")

# 19 silindir
assert F(150,25)==6
kart("geo-silindir-02","Silindirin hacmi ve su yüksekliği",
 "Silindirin hacmini ve içine cisim atılınca yükselen su seviyesini hacim eşitliğiyle bulabildiğini.",
 "Silindirin hacmi **V = π r² h**'dir. Aynı taban ve yükseklikli koni silindirin **üçte biri** kadardır; koninin ana doğrusu l ise l² = r² + h²'dir. Kaba batırılan cismin **hacmi, yükselen suyun hacmine eşittir**.",
 "V = π r² h",
 None,
 "Taban yarıçapı 5 cm olan silindirik bir kaba hacmi 150π cm³ olan bir cisim tamamen batırılıyor (su taşmıyor). Su seviyesi kaç cm yükselir?",
 ["Yükselen suyun hacmi cismin hacmine eşit: π · 5² · h = 150π.","25h = 150.","h = 6."],
 "6 cm",
 "Koninin ana doğrusunu yükseklik almak ya da koni hacmindeki 1/3'ü unutmak. Kontrol: yükseklik tabana inen diktir: h = √(l² − r²).",
 "Koni, silindirin üçte biridir.")

# 20 yamuk
x=5; assert 2*x+1==3*x-4==11 and 7+15+2*11==44
kart("geo-yamuk-03","Yamukta açı ve özel yamuklar",
 "İkizkenar ve dik yamuğun özelliklerini kullanıp bilinmeyeni bulduktan sonra çevre ya da açı hesaplayabildiğini.",
 "İkizkenar yamukta **yan kenarlar eşittir**, taban açıları da eşittir. Dik yamukta yardımcı **dikme** çizip dik üçgen elde edersin. Çevre sorularında önce bilinmeyen x'i bul, sonra **dört kenarı** ayrı ayrı yaz. Aynı yan kenardaki açılar bütünlerdir.",
 "Çevre = alt + üst + 2 · yan kenar",
 T(r'''\coordinate(A)at(0,0);\coordinate(B)at(5,0);\coordinate(C)at(3.67,2);\coordinate(D)at(1.33,2);
\draw(A)--(B)--(C)--(D)--cycle;\node[below left]at(A){A};\node[below right]at(B){B};\node[above right]at(C){C};\node[above left]at(D){D};
\node[below]at(2.5,0){15};\node[above]at(2.5,2){7};\node[left]at(.65,1){$2x+1$};\node[right]at(4.35,1){$3x-4$};''',.85),
 "İkizkenar yamuğun tabanları 7 cm ve 15 cm, yan kenarları (2x + 1) cm ve (3x − 4) cm'dir. Çevresi kaç cm'dir?",
 ["Yan kenarlar eşit: 2x + 1 = 3x − 4 → x = 5.","Yan kenar: 2 · 5 + 1 = 11 cm.","Çevre: 7 + 15 + 11 + 11 = 44."],
 "44 cm",
 "Yalnız iki tabanı toplamak, yan kenarlardan yalnız birini eklemek ya da x'i kenar uzunluğu sanmak. Kontrol: dört kenarı yazdın mı?",
 "Önce x'i bul, sonra dört kenarı topla.")

# 21 çemberde açı
assert (360-140)//2==110
kart("geo-cemberde-aci-03","Merkez açı ve çevre açı",
 "Merkez açı, çevre açı ve çapı gören açı arasındaki ilişkiyi yayın hangi tarafta kaldığına göre uygulayabildiğini.",
 "**Çevre açı, gördüğü yayın yarısıdır**; merkez açı yayın kendisine eşittir. Çapı gören çevre açı **90°**'dir. Köşe yayın karşı tarafındaysa o yay yarılanır; köşe yayın üzerindeyse **diğer (büyük) yay** yarılanır. Yarıçaplar ikizkenar üçgen kurar.",
 "Çevre açı = gördüğü yay ÷ 2",
 None,
 "O merkezli çemberde m(AOB) = 140°'dir. C noktası küçük [AB] yayı üzerindeyse m(ACB) kaçtır?",
 ["C küçük yayda olduğundan büyük yayı görür: 360° − 140° = 220°.","Çevre açı yayın yarısıdır: 220° ÷ 2 = 110°."],
 "110°",
 "Çevre açıyı hep merkez açının yarısı (70°) almak. Kontrol: köşe hangi yayın üzerinde? Açı, köşenin bulunmadığı yayı görür.",
 "Çevre açı, gördüğü yayın yarısıdır.")

# 22 teğet
OP,rr=17,8; pa=math.isqrt(OP*OP-rr*rr); assert pa==15 and pa*pa==225
Op=(0,0);Pp=(3.4,0);Ap2=(1.6*8/17,1.6*math.sqrt(1-(8/17)**2))
kart("geo-cemberde-uzun-02","Teğet uzunlukları",
 "Teğetin yarıçapa dik olduğunu kullanıp dış noktadan çembere çizilen teğetin uzunluğunu bulabildiğini.",
 "Teğet, değme noktasındaki **yarıçapa diktir**; dış noktadan çizilen iki teğetin uzunluğu eşittir. Merkezi değme noktasına ve dış noktaya bağla: **merkeze uzaklık hipotenüs**, yarıçap ve teğet dik kenardır. Ortak teğette de merkezlerden dik üçgen kurulur.",
 "|PA|² = |OP|² − r²",
 T(r'''\draw(0,0)circle(1.6);\coordinate(O)at(0,0);\coordinate(P)at(3.4,0);\coordinate(A)at(%.3f,%.3f);
\draw(A)--(P);\draw[thick,vurgu](O)--(A);\draw[dashed](O)--(P);%s\fill(O)circle(.05);
\node[below left]at(O){O};\node[below right]at(P){P};\node[above]at(A){A};
\node[left]at(.37,.75){8};\node[below]at(1.7,0){17};\node[above right]at(2.1,.7){?};'''%(Ap2+(ra(Ap2,unit(Ap2,(0,0)),unit(Ap2,(3.4,0)),.25),)),.8),
 "Merkezi O, yarıçapı 8 cm olan çembere P dış noktasından çizilen teğet çembere A'da değiyor. |OP| = 17 cm ise |PA| kaçtır?",
 ["OAP dik üçgendir: [OA] ⊥ [AP].","|PA|² = 17² − 8² = 289 − 64 = 225.","|PA| = 15."],
 "15 cm",
 "Hipotenüsü (|OP|) ya da yarıçapı cevap yazmak, uzaklıkların farkını almak. Kontrol: teğet uzunluğu dik kenardır, |OP|'den küçüktür.",
 "Teğet yarıçapa dik, merkez hipotenüs.")

# 23 çokgenler
a=6; assert F(6*a*a,4)==54 and F(3*a*a,2)==54
vs=[(2*math.cos(math.radians(60*i)),2*math.sin(math.radians(60*i))) for i in range(6)]
hexs='--'.join('(%.3f,%.3f)'%p for p in vs)+'--cycle'
spk=''.join(r'\draw[dashed,vurgu](0,0)--(%.3f,%.3f);'%p for p in vs)
kart("geo-cokgenler-01","Düzgün altıgenin alanı",
 "Düzgün altıgeni eş eşkenar üçgenlere bölüp alanını ve bölgelerin alanlarını hesaplayabildiğini.",
 "Düzgün altıgen, merkezden köşelere çizilen doğru parçalarıyla **6 eş eşkenar üçgene** ayrılır. Kenarı a olan eşkenar üçgenin alanı **a²√3 ÷ 4**'tür; altıgenin alanı bunun 6 katıdır. Her iç açı 120°'dir. Bölge alanı, alanların farkıyla bulunur.",
 "Alan = 6 · a²√3 ÷ 4 = 3a²√3 ÷ 2",
 T(r'\draw'+hexs+';'+spk+r'\fill(0,0)circle(.05);\node[above right]at(1.5,.87){6};',.85),
 "Kenarı 6 cm olan düzgün altıgenin alanı kaç cm²'dir?",
 ["Bir eşkenar üçgen: 6² · √3 ÷ 4 = 9√3.","Altı üçgen: 6 · 9√3 = 54√3.","Kontrol: 3 · 36 · √3 ÷ 2 = 54√3 ✓."],
 "54√3 cm²",
 "Altıgeni 3 ya da 4 üçgene ayırmak ya da √3 çarpanını unutmak. Kontrol: altıgenin 6 köşesi var, 6 üçgen çıkar; eşkenar üçgen alanında √3 bulunur.",
 "Altıgen, altı eşkenar üçgendir.")

# 24 özel dörtgenler
kart("geo-ozel-dortgenler-01","Özel dörtgenlerin köşegenleri",
 "Köşegen özelliklerinden dörtgenin türünü kesin olarak belirleyebildiğini.",
 "**Paralelkenarda** köşegenler birbirini ortalar; başka özellik kesin değildir. **Dikdörtgende** köşegenler eşittir. **Eşkenar dörtgende** köşegenler dik ortalar ve köşe açılarını ikiye böler. **Kare** hepsine sahiptir. Deltoidde bir köşegen diğerini dik keser.",
 None,None,
 "Köşegenleri eşit uzunlukta ve birbirini dik ortalayan dörtgen hangisidir?",
 ["Köşegenler eşit → dikdörtgen ya da kare adayı.","Köşegenler dik ortalar → eşkenar dörtgen ya da kare adayı.","İki özellik birlikte yalnız karede vardır."],
 "Kare",
 "Dikdörtgenin köşegenlerini dik ya da açıortay sanmak. Kontrol: dik kesişme ve açıortaylık yalnız eşkenar dörtgen ve karede vardır.",
 "Eşit: dikdörtgen. Dik: eşkenar dörtgen.")

# 25 üçgende alan
Fa=F(80)*F(3,4)*F(2,5); assert Fa==24
kart("geo-ucgende-alan-02","Ortak yükseklik ve alan oranı",
 "Yüksekliği ortak üçgenlerde alan oranını taban oranına eşitleyerek bilinmeyen alanı bulabildiğini.",
 "Yükseklikleri ortak olan üçgenlerin **alanları oranı, tabanları oranına eşittir**. Önce ortak yüksekliği olan üçgen çiftini bul ve her adımda **bir taban oranı** uygula. Payı ve paydayı hangi üçgene ait olduğuna göre dikkatle yaz.",
 "A₁ / A₂ = taban₁ / taban₂",
 None,
 "ABC üçgeninin alanı 80 cm²'dir. D ∈ [BC] için |BD| / |BC| = 3/4, E ∈ [AD] için |AE| / |AD| = 2/5 ise ABE üçgeninin alanı kaçtır?",
 ["A'dan inen yükseklik ortak: Alan(ABD) = 80 · 3/4 = 60.","B'den inen yükseklik ortak: Alan(ABE) = Alan(ABD) · 2/5.","60 · 2/5 = 24."],
 "24 cm²",
 "Yalnız tek bir oranı uygulamak ya da paydaya yanlış üçgenin tabanını yazmak. Kontrol: her adımda ortak yüksekliğin hangi köşeden indiğini söyle.",
 "Ortak yükseklik: alan oranı taban oranı.")

# 26 üçgende açılar
B_,C_=84,40; A_=180-B_-C_; assert A_==56 and A_//2-(90-B_)==22==(B_-C_)//2
Bp=(0,0);Cp=(5,0);Ap=(.405,3.855);Hp=(.405,0);Dp=(1.963,0)
kart("geo-ucgende-acilar-02","Yükseklik ve açıortay arası açı",
 "Aynı köşeden çıkan yükseklik ile açıortay arasındaki açıyı üçgenin diğer iki açısından bulabildiğini.",
 "Yükseklik karşı kenarla **90°** yapar; açıortay köşe açısını iki eş açıya böler. Aynı köşeden çıkan ikisinin arasındaki açı, **diğer iki açının farkının yarısıdır**. Önce her birinin bir kenarla yaptığı açıyı ayrı ayrı bul, farkını al.",
 "Açı = |B − C| ÷ 2",
 T(r'''\coordinate(A)at(.405,3.855);\coordinate(B)at(0,0);\coordinate(C)at(5,0);\coordinate(H)at(.405,0);\coordinate(D)at(1.963,0);
\draw(A)--(B)--(C)--cycle;\draw[dashed](A)--(H);\draw[thick,vurgu](A)--(D);%s
\node[above]at(A){A};\node[below left]at(B){B};\node[below right]at(C){C};\node[below]at(H){H};\node[below]at(D){D};
\node at(.62,3.05){$x$};\node at(2.6,-.75){$m(B)=84^\circ,\ m(C)=40^\circ$};'''%ra(Hp,(0,1),(1,0),.25),1.0),
 "ABC üçgeninde m(B) = 84° ve m(C) = 40°'dir. [AH] yükseklik, [AD] açıortay ise m(HAD) = x kaçtır?",
 ["m(A) = 180° − 84° − 40° = 56° olduğundan m(BAD) = 28°.","ABH dik üçgeninde m(BAH) = 90° − 84° = 6°.","x = 28° − 6° = 22°."],
 "22°",
 "Tek bir açıyı (örneğin BAH) bulup bırakmak ya da farkı ikiye bölmeyi unutmak. Kontrol: iki açıyı da aynı kenardan ölç; arada kalan, farkıdır.",
 "İkisini ayrı ölç, farkını al.")

# 27 benzerlik
x=10; assert F(x,x+5)==F(6,9)
kart("geo-ucgende-benzerlik-02","Yamukta benzerlik",
 "Yamuğun yan kenar uzantılarıyla oluşan benzer üçgenlerde oranı kurup uzunluk bulabildiğini.",
 "Tabanlar paralelse yan kenarların uzantıları bir noktada kesişir ve **iki benzer üçgen** oluşur (açılar eşit). Benzer üçgenlerde karşılıklı kenarların oranı sabittir. Bilinmeyene **x** verip bütün kenarı x cinsinden yaz; oran tek denkleme dönüşür.",
 "|ED| / |EA| = |DC| / |AB|",
 T(r'''\coordinate(A)at(0,0);\coordinate(B)at(4.5,0);\coordinate(C)at(3.6,1.5);\coordinate(D)at(.6,1.5);\coordinate(E)at(1.8,4.5);
\draw(A)--(B)--(C)--(D)--cycle;\draw[dashed](D)--(E)--(C);
\node[above]at(E){E};\node[below left]at(A){A};\node[below right]at(B){B};\node[right]at(C){C};\node[left]at(D){D};
\node[below]at(2.25,0){9};\node[below]at(2.1,1.5){6};\node[left]at(.3,.75){5};\node[left]at(1.2,3){$x$};''',.85),
 "[DC] // [AB], |DC| = 6, |AB| = 9 ve |AD| = 5'tir. AD ve BC doğruları E noktasında kesişiyor. |ED| kaçtır?",
 ["EDC ~ EAB olduğundan |ED| / |EA| = 6 / 9 = 2/3.","|ED| = x ise |EA| = x + 5.","x / (x + 5) = 2/3 → 3x = 2x + 10 → x = 10."],
 "|ED| = 10",
 "Oranı yanlış kurmak ya da |EA|'yı bulup |ED|'ye geçmemek. Kontrol: karşılıklı kenarlar aynı açının karşısındadır; 10 / 15 = 2/3 olmalı.",
 "Bilinmeyene x ver, bütünü x'li yaz.")

# 28 ikizkenar
assert 180-60==120 and (180-120)//2==30 and 60+30==90
kart("geo-ikizkenar-ucgen-01","İkizkenar ve eşkenar üçgen birlikte",
 "Ortak kenarlı ikizkenar ve eşkenar üçgenlerde açıları zincirleme hesaplayabildiğini.",
 "İkizkenar üçgende eşit kenarların karşısındaki açılar eşittir; eşkenar üçgenin her açısı **60°**'dir. Ortak kenarı paylaşan üçgenlerde **eşit kenarları işaretle**. Kare ve eşkenar üçgenin ortak kenarı da ikizkenar üçgen kurar. Tamamlayıcı açılarda 180° ya da 360°'yi kullan.",
 "Taban açı = (180° − tepe açı) ÷ 2",
 T(r'''\coordinate(A)at(1.5,2.6);\coordinate(B)at(0,0);\coordinate(C)at(3,0);\coordinate(D)at(6,0);
\draw(A)--(B)--(C)--(A);\draw(A)--(D)--(C);
\node[above]at(A){A};\node[below left]at(B){B};\node[below]at(C){C};\node[below right]at(D){D};
\node[below]at(1.5,0){$a$};\node[left]at(.7,1.4){$a$};\node[right]at(2.35,1.4){$a$};\node[below]at(4.5,0){$a$};\draw([shift=(240:.9)]A)arc(240:330:.9);\node at(1.82,1.4){$x$};''',.8),
 "ABC eşkenar üçgendir; B, C, D noktaları doğrusaldır ve |CD| = |CA|'dır. m(BAD) = x kaçtır?",
 ["C'de doğru üzerinde: m(ACD) = 180° − 60° = 120°.","ACD ikizkenar (|CA| = |CD|): m(CAD) = (180° − 120°) ÷ 2 = 30°.","x = m(BAC) + m(CAD) = 60° + 30° = 90°."],
 "90°",
 "İlk bulduğun açıyı cevap sanıp durmak ya da eşkenarın 60°'sini taban açısına eklemek. Kontrol: sorulan açının hangi parçalardan oluştuğunu şekle yaz.",
 "Eşit kenarları işaretle, açıları zincirle.")

# çıktı
cikti=[]
for id,_ in girdi:
    if id=="geo-eskenar-ucgen-02": cikti.append({"id":id,"birlesti":"geo-ikizkenar-ucgen-01"})
    else: cikti.append(kartlar[id])
# doğrulama
def w(s): return len(s.replace('**','').split())
assert [c['id'] for c in cikti]==[i for i,_ in girdi] and len(set(c['id'] for c in cikti))==len(girdi)
nk=ns=0
for c in cikti:
    if 'birlesti' in c: assert c['birlesti'] in K; continue
    nk+=1
    for f in ('id','k','baslik','olcer','kural','ornek','hata','akilda'): assert c[f],(c['id'],f)
    assert w(c['baslik'])<=6,(c['id'],'baslik',w(c['baslik']))
    assert w(c['olcer'])<=25 and not c['olcer'].startswith('Bu soru'),(c['id'],'olcer',w(c['olcer']))
    assert w(c['kural'])<=60,(c['id'],'kural',w(c['kural']))
    assert w(c['hata'])<=40,(c['id'],'hata',w(c['hata']))
    assert w(c['akilda'])<=8 and '"' not in c['akilda'] and '“' not in c['akilda'],(c['id'],'akilda')
    o=c['ornek']; assert o['soru'] and o['cevap'] and 2<=len(o['adimlar'])<=4
    if c['sekil']: ns+=1; assert len(c['sekil'])<=25000,(c['id'],len(c['sekil']))
print('kart',nk,'sekilli',ns,'birlesen',len(cikti)-nk)
json.dump(cikti,open(CIKTI,'w',encoding='utf8'),ensure_ascii=False,indent=1)
for c in cikti:
    if c.get('sekil'): open('/tmp/kor/kart/p05/%s.svg'%c['id'],'w').write(c['sekil'])
