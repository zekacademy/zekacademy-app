import sys, re, json, math
sys.path.insert(0, '/home/claude/zekacademy-app/havuz')
from cizim import tikz_svg

def T(body, sc=1.0):
    return tikz_svg(r'\begin{tikzpicture}[font=\footnotesize,line cap=round,line join=round,scale=%s]' % sc + body + r'\end{tikzpicture}')

S = {}
S['aciortay'] = T(r'''
\coordinate (B) at (0,0);\coordinate (C) at (4.6,0);\coordinate (A) at (1.3,2.6);\coordinate (D) at (1.88,0);
\draw[thick] (A)--(B)--(C)--cycle;\draw[vurgu,very thick] (A)--(D);
\pic[draw=vurgu,angle radius=.6cm]{angle=B--A--D};\pic[draw=vurgu,angle radius=.75cm]{angle=D--A--C};
\node[above] at (A){A};\node[below left] at (B){B};\node[below right] at (C){C};\node[below] at (D){D};
\node[left] at (.6,1.4){$c$};\node[right] at (3.1,1.5){$b$};
\node[below] at (.9,-.25){$m$};\node[below] at (3.3,-.25){$n$};
''', 1.1)
S['dairede'] = T(r'''
\fill[vurgu!25,even odd rule](0,0)circle(1.8)(0,0)circle(1.0);
\draw[thick](0,0)circle(1.8);\draw[thick](0,0)circle(1.0);\fill(0,0)circle(1.2pt);
\draw[thick](0,0)--(200:1.0) node[pos=.5,above]{4};
\draw[thick](0,0)--(35:1.8) node[pos=.8,above left]{7};
\node[below right] at (0,0){O};
''', 1.4)
S['dik'] = T(r'''
\coordinate (C) at (0,0);\coordinate (B) at (2.6,0);\coordinate (A) at (0,1.5);
\draw[thick](A)--(B)--(C)--cycle;\draw (0,0)++(.2,0)--++(0,.2)--++(-.2,0);
\node[left] at (0,.75){$1$};\node[below] at (1.3,0){$\sqrt{3}$};\node[above right] at (1.3,.75){$2$};
\node at (.4,1.05){$60^\circ$};\node at (1.95,.2){$30^\circ$};
''', 1.5)
S['dikdortgen'] = T(r'''
\begin{scope}[scale=.45]
\coordinate (B) at (0,0);\coordinate (A) at (10,0);\coordinate (D) at (10,8);\coordinate (C) at (0,8);\coordinate (E) at (4,0);\coordinate (F) at (0,3);
\draw[thick](B)--(A)--(D)--(C)--cycle;\draw[dashed](F)--(D);\draw[dashed](C)--(E);
\draw[vurgu,very thick](F)--(E);
\node[below left] at (B){B};\node[below right] at (A){A};\node[above right] at (D){D};\node[above left] at (C){C};
\node[below] at (E){E};\node[left] at (F){F};
\node[below] at (2,-.3){4};\node[left] at (-.2,1.5){$x$};\node[left] at (-.2,5.5){$8-x$};
\end{scope}
''', 1.0)
S['dogruda'] = T(r'''
\draw[thick](0,0)--(4.6,0);\draw[thick](0,1.6)--(4.6,1.6);\draw[thick](1.0,-.5)--(3.2,2.1);
\coordinate (P) at (1.423,0);\coordinate (Q) at (2.777,1.6);\coordinate (R) at (3,0);\coordinate (L) at (1.5,1.6);
\pic[draw=vurgu,angle radius=.5cm]{angle=R--P--Q};\pic[draw=vurgu,angle radius=.5cm]{angle=L--Q--P};
\node at (2.55,.32){$3x-5$};\node at (1.5,1.25){$x+45$};
\node[right] at (4.6,0){$d_2$};\node[right] at (4.6,1.6){$d_1$};
''', 1.2)
S['eskenar'] = T(r'''
\draw[thick](2,0)--(0,1.2)--(-2,0)--(0,-1.2)--cycle;\draw[dashed](-2,0)--(2,0);\draw[dashed](0,-1.2)--(0,1.2);
\draw (.2,0)--(.2,.2)--(0,.2);
\node[below] at (1,0){$\frac{d_1}{2}$};\node[right] at (0,.55){$\frac{d_2}{2}$};\node[above right] at (1,.6){$a$};
''', 1.5)
S['kare'] = T(r'''
\coordinate (A) at (0,0);\coordinate (B) at (3,0);\coordinate (C) at (3,3);\coordinate (D) at (0,3);\coordinate (E) at (1.5,-2.598);
\draw[thick](A)--(B)--(C)--(D)--cycle;\draw[thick](A)--(E)--(B);\draw[vurgu,very thick](C)--(E);
\pic[draw=vurgu,angle radius=.5cm]{angle=C--B--E};
\node[above left] at (A){A};\node[right] at (B){B};\node[above right] at (C){C};\node[above left] at (D){D};\node[below] at (E){E};
\node[vurgu,right] at (3.35,1.2){$x$};\draw[->,vurgu](3.3,1.2)--(2.95,1.6);
\node at (3.55,-.3){$150^\circ$};
''', 1.1)
S['kenarortay'] = T(r'''
\coordinate (A) at (1.0,3.0);\coordinate (B) at (0,0);\coordinate (C) at (4.2,0);
\coordinate (D) at ($(B)!.5!(C)$);\coordinate (E) at ($(A)!.5!(C)$);\coordinate (G) at ($(A)!.6667!(D)$);
\fill[vurgu!30](C)--(D)--(G)--(E)--cycle;
\draw[thick](A)--(B)--(C)--cycle;\draw(A)--(D);\draw(B)--(E);\fill(G)circle(1.2pt);
\node[above] at (A){A};\node[below left] at (B){B};\node[below right] at (C){C};\node[below] at (D){D};\node[above right] at (E){E};
\node[above left] at (G){G};
''', 1.2)
S['koni'] = T(r'''
\draw[thick](-1.5,0)--(0,2.6)--(1.5,0);\draw[thick](1.5,0)arc(0:-180:1.5 and .45);\draw[dashed](1.5,0)arc(0:180:1.5 and .45);
\draw[dashed](0,0)--(0,2.6);\draw[vurgu,very thick](0,0)--(1.5,0);\fill(0,0)circle(1pt);
\node[left] at (0,1.3){$h$};\node[above] at (.75,0){$r$};\node[right] at (.85,1.5){$\ell$};
''', 1.5)
S['kup'] = T(r'''
\draw[thick](0,0)rectangle(2,2);\draw[thick](2,0)--(2.8,.7)--(2.8,2.7)--(.8,2.7)--(0,2);\draw[thick](2,2)--(2.8,2.7);
\draw[dashed](0,0)--(.8,.7)--(2.8,.7);\draw[dashed](.8,.7)--(.8,2.7);
\fill[red](0,0)circle(2.5pt);\fill[blue](1,0)circle(2.5pt);\fill[vurgu](1,1)circle(2.5pt);
\node[anchor=north west,align=left] at (-.2,-.3){\textcolor{red}{$\bullet$} köşe: 3 yüz boyalı\\ \textcolor{blue}{$\bullet$} ayrıt: 2 yüz boyalı\\ \textcolor{vurgu}{$\bullet$} yüz içi: 1 yüz boyalı};
''', 1.0)
S['paralelkenar'] = T(r'''
\coordinate (A) at (0,0);\coordinate (B) at (3.6,0);\coordinate (C) at (4.6,1.5);\coordinate (D) at (1.0,1.5);\coordinate (H) at (1.0,0);
\draw[thick](A)--(B)--(C)--(D)--cycle;\draw[dashed,vurgu,thick](D)--(H);\draw(1.0,0)++(.2,0)--++(0,.2)--++(-.2,0);
\node[below] at (1.8,0){taban};\node[right] at (1.0,.75){$h$};\node[left] at (.4,.8){yan kenar};
''', 1.0)
S['piramit'] = T(r'''
\coordinate(A)at(0,0);\coordinate(B)at(3,0);\coordinate(C)at(3.9,.9);\coordinate(D)at(.9,.9);\coordinate(T)at(1.95,2.8);\coordinate(O)at(1.95,.45);
\draw[thick](A)--(B)--(C);\draw[dashed](A)--(D)--(C);\draw[thick](T)--(A);\draw[thick](T)--(B);\draw[thick](T)--(C);\draw[dashed](T)--(D);
\draw[vurgu,thick,dashed](T)--(O);
\coordinate(M1)at($(T)!.5!(A)$);\coordinate(M2)at($(T)!.5!(B)$);\coordinate(M3)at($(T)!.5!(C)$);\coordinate(M4)at($(T)!.5!(D)$);
\draw[vurgu,thick](M1)--(M2)--(M3);\draw[vurgu,dashed](M3)--(M4)--(M1);
\node[right] at (1.95,1.7){$h$};\node[below] at (1.5,0){taban};\node[left,vurgu] at (M1){kesit};
''', 1.2)
S['prizma'] = T(r'''
\coordinate(A)at(0,0);\coordinate(B)at(2.4,0);\coordinate(C)at(0,1);\coordinate(A2)at(1,.7);\coordinate(B2)at(3.4,.7);\coordinate(C2)at(1,1.7);
\draw[thick](A)--(B)--(C)--cycle;\draw[thick](B)--(B2)--(C2)--(C);
\draw[dashed](A)--(A2)--(B2);\draw[dashed](A2)--(C2);
\node[below] at (1.2,0){12};\node[left] at (0,.5){5};\node[right] at (2.9,.35){10};
''', 1.4)
S['yamuk'] = T(r'''
\coordinate(A)at(0,0);\coordinate(B)at(4.05,0);\coordinate(C)at(3.4,1.9);\coordinate(D)at(.97,1.9);\coordinate(H)at(.97,0);
\draw[thick](A)--(B)--(C)--(D)--cycle;\draw[dashed,vurgu,thick](D)--(H);\draw(.97,0)++(.2,0)--++(0,.2)--++(-.2,0);
\node[below] at (2,0){15};\node[above] at (2.2,1.9){9};\node[right] at (.97,.9){7};
''', 1.1)
S['kirisler'] = T(r'''
\draw[thick](0,0)circle(1.6);
\coordinate(A)at(100:1.6);\coordinate(B)at(200:1.6);\coordinate(C)at(300:1.6);\coordinate(D)at(30:1.6);\coordinate(E)at($(B)!1.45!(C)$);
\draw[thick](A)--(B)--(C)--(D)--cycle;\draw[thick](C)--(E);\pic[draw=vurgu,angle radius=.45cm]{angle=E--C--D};
\node[above] at (A){A};\node[left] at (B){B};\node[below] at (C){C};\node[right] at (D){D};\node[right] at (E){E};
''', 1.2)
S['alan'] = T(r'''
\coordinate(C)at(0,0);\coordinate(B)at(4,0);\coordinate(A)at(1.8,2.4);\coordinate(H)at(1.8,0);\coordinate(K)at(1.44,1.92);
\draw[thick](A)--(B)--(C)--cycle;\draw[dashed,vurgu,thick](A)--(H);\draw[dashed,vurgu,thick](B)--(K);
\node[above] at (A){A};\node[below left] at (C){C};\node[below right] at (B){B};
\node[below] at (3.3,0){10};\node[right] at (1.8,.5){6};\node[above left] at (.9,1.2){7,5};\node[below left] at (2.8,.9){$h$};
''', 1.2)
S['benzerlik'] = T(r'''
\coordinate(A)at(1.2,3);\coordinate(B)at(0,0);\coordinate(C)at(4,0);\coordinate(D)at(.72,1.8);\coordinate(E)at(2.32,1.8);
\draw[thick](A)--(B)--(C)--cycle;\draw[vurgu,very thick](D)--(E);
\node[above] at (A){A};\node[below left] at (B){B};\node[below right] at (C){C};\node[left] at (D){D};\node[right] at (E){E};
\node[left] at (.96,2.4){$x$};\node[left] at (.36,.9){$x+3$};\node[right] at (1.76,2.4){4};\node[right] at (3.16,.9){6};
''', 1.2)
S['ikizkenar'] = T(r'''
\coordinate(A)at(0,0);\coordinate(B)at(248:3.6);\coordinate(C)at(292:3.6);\coordinate(D)at(292:1.58);
\draw[thick](A)--(B)--(C)--cycle;\draw[vurgu,very thick](B)--(D);
\pic[draw=vurgu,angle radius=.7cm,"$44^\circ$",angle eccentricity=1.9]{angle=B--A--C};
\node[above] at (A){A};\node[below left] at (B){B};\node[below right] at (C){C};\node[right] at (D){D};
''', 1.3)

K = []
def kart(id, baslik, olcer, kural, formul, sekil, soru, adimlar, cevap, hata, akilda):
    K.append(dict(id=id, k='geo', baslik=baslik, olcer=olcer, kural=kural, formul=formul, sekil=sekil,
                  ornek=dict(soru=soru, adimlar=adimlar, cevap=cevap), hata=hata, akilda=akilda))

# 1
a, b = 5, 12
assert (b - a, b + a) == (7, 17) and a + b + 16 == 33
kart('geo-aci-kenar-02', 'Üçgende kenar sınırları',
 'İki kenarı bilinen üçgende üçüncü kenarın hangi aralıkta olabileceğini ve bunun çevreyi nasıl sınırladığını bulabilmeni.',
 'Bir üçgenin herhangi bir kenarı, diğer iki kenarın **farkından büyük**, **toplamından küçüktür**. Uç değerler dahil değildir. Tam sayı isteniyorsa aralığın içindeki değerleri say; en büyük çevre için en büyük tam sayıyı al.',
 '|b − c| < a < b + c', None,
 'Kenarları 5 cm ve 12 cm olan bir üçgenin üçüncü kenarı tam sayı ise çevresi en çok kaç cm olabilir?',
 ['Aralığı yaz: 12 − 5 < x < 12 + 5, yani 7 < x < 17', 'x tam sayı olduğundan en büyük değer 16', 'Çevre: 5 + 12 + 16 = 33'],
 '33 cm',
 'Farkı üst sınır sanmak ya da uç değeri (17) kullanmak. Kontrol: yazdığın üç kenardan **en kısa ikisinin toplamı en uzundan büyük** olmalı.',
 'Fark < kenar < toplam.')
# 2
ab, ac, bc = 12, 20, 24
u = bc / ((ab + ac) // 4)  # 3:5 -> 8 parça
assert ab / ac == 3 / 5 and bc / 8 == 3 and 3 * 3 == 9 and 5 * 3 == 15
kart('geo-aciortay-03', 'Açıortay teoremi',
 'Açıortayın karşı kenarı hangi oranda böldüğünü bilip bu oranla uzunluk ya da kenar bulabilmeni.',
 'İç açıortay karşı kenarı **komşu kenarların oranında** böler. Dış açıortay da karşı kenarın uzantısını aynı oranda dıştan böler. Açıortay üzerindeki her nokta, açının kollarına **eşit uzaklıktadır**.',
 '|BD| / |DC| = |AB| / |AC|', S['aciortay'],
 '|AB| = 12, |AC| = 20, |BC| = 24 olan ABC üçgeninde [AD] açıortay ise |BD| kaçtır?',
 ['Oranı kur: |BD| / |DC| = 12 / 20 = 3 / 5', 'BC\'yi 3 + 5 = 8 parçaya böl: her parça 24 ÷ 8 = 3', '|BD| = 3 · 3 = 9, |DC| = 5 · 3 = 15'],
 '|BD| = 9',
 'Oranı ters kurmak ya da açıortayı kenarortay sanıp BC\'yi ikiye bölmek. Kontrol: **uzun kenarın yanındaki parça da uzundur.**',
 'Parça oranı, komşu kenar oranıdır.')
# 3
assert 7**2 - 4**2 == 33
kart('geo-dairede-cevre-03', 'Taralı alan, halka, bileşik şekil',
 'Daire ve çember formüllerini kullanıp bir şeklin taralı alanını ya da çevresini parçalara ayırarak bulabilmeni.',
 'Daire alanı **π r²**, çember uzunluğu **2π r**\'dir. Taralı alan = bütün alan − çıkarılan alan. Teğet çemberlerde uzunlukları yarıçapların katı olarak yaz. Halkanın alanı, dış daire ile iç dairenin alanları farkıdır.',
 'A = π r² · Ç = 2π r · halka = π(R² − r²)', S['dairede'],
 'Dış yarıçapı 7 cm, iç yarıçapı 4 cm olan halkanın alanı kaç cm²\'dir?',
 ['Dış daire: π · 7² = 49π', 'İç daire: π · 4² = 16π', 'Halka: 49π − 16π = 33π'],
 '33π cm²',
 'Alan yerine çevre formülünü (2πr) kullanmak ya da çember sayısını yanlış saymak. Kontrol: alan **kare birimdir**, formülde r² görmelisin.',
 'Taralı alan: bütün eksi boşluk.')
# 4
h = 16; kisa = h // 2; assert kisa**2 * 3 + kisa**2 == h**2
kart('geo-dik-ucgen-01', 'Özel dik üçgenler',
 '30-60-90 ve 45-45-90 üçgenlerde kenar oranlarını, hangi kenarın hangi açının karşısında olduğunu bilerek kullanabilmeni.',
 '**30°-60°-90°** üçgende kenarlar 1 : √3 : 2\'dir; en kısa kenar 30°\'nin karşısındadır. **45°-45°-90°** üçgende kenarlar 1 : 1 : √2\'dir. 3-4-5 üçgeni ve katları da sık çıkar. Hipotenüse ait kenarortay hipotenüsün yarısıdır.',
 '30-60-90 → 1 : √3 : 2 · 45-45-90 → 1 : 1 : √2', S['dik'],
 '30°-60°-90° üçgende hipotenüs 16 cm\'dir. 60°\'nin karşısındaki kenar kaç cm\'dir?',
 ['Kısa kenar hipotenüsün yarısıdır: 16 ÷ 2 = 8', '60°\'nin karşısındaki kenar, kısa kenarın √3 katıdır', 'Uzunluk: 8√3'],
 '8√3 cm',
 'Hangi kenarın hangi açının karşısında olduğuna bakmadan oranları dizmek. Kontrol: **en uzun kenar hipotenüstür**, en kısa kenar 30°\'nin karşısıdır.',
 'Kısa kenar 30°\'nin karşısındadır.')
# 5
x = (64 - 16) / 16; assert x == 3 and 8 - x == 5 and x**2 + 4**2 == (8 - x)**2
kart('geo-dikdortgen-01', 'Katlama soruları',
 'Katlayınca üst üste gelen uzunlukların eşit kaldığını görüp dik üçgende Pisagor kurabilmeni.',
 'Katlayınca üst üste gelen parçalar **eşittir**; kat izi, karşılıklı noktaların **orta dikmesidir**. Önce eşit kalan uzunlukları yaz, bilinmeyene x de. Sonra oluşan dik üçgende **Pisagor** kur ve x\'i çöz.',
 'kat izi → eşit uzunluklar → dik üçgende Pisagor', S['dikdortgen'],
 '|AB| = 10, |BC| = 8 olan dikdörtgen kâğıtta C köşesi, [AB] üzerinde |BE| = 4 olan E noktasına gelecek biçimde katlanıyor. Kat izi [BC]\'yi F\'de kesiyorsa |FC| kaçtır?',
 ['C, E\'ye geldi: |FE| = |FC|. |BF| = x ise |FC| = |FE| = 8 − x', 'BFE dik üçgeninde: x² + 4² = (8 − x)²', 'x² + 16 = 64 − 16x + x² → 16x = 48 → x = 3', '|FC| = 8 − 3 = 5'],
 '5',
 'x = |BF| = 3\'te kalmak ya da |FC| = |BC| − |DE| gibi ilişkisiz bir çıkarma yapmak. Kontrol: **x\'in hangi uzunluk olduğunu** şekle yaz.',
 'Katla, eşitle, Pisagor kur.')
# 6
x = 25; assert 3 * x - 5 == x + 45 == 70 and 180 - 70 == 110
kart('geo-dogruda-acilar-02', 'Paralel doğrular ve kesen',
 'Paralel iki doğruyu kesen doğruda hangi açıların eşit, hangilerinin bütünler olduğunu ayırt edebilmeni.',
 'Paralel doğruları bir doğru kesince **iç ters, dış ters ve yöndeş** açılar eşittir. Kesenin aynı yanındaki iç (ya da dış) açılar **bütünlerdir**, toplamları 180°\'dir. Zigzag\'da bir yöne bakan açıların toplamı ters yöndekilere eşittir.',
 'ters açılar eşit · yan yana açılar toplamı 180°', S['dogruda'],
 'd₁ // d₂ doğrularını kesen doğruda iç ters açılar (3x − 5)° ve (x + 45)°\'dir. (3x − 5)° açının bütünleri kaç derecedir?',
 ['İç ters açılar eşit: 3x − 5 = x + 45', '2x = 50 → x = 25', 'Açı: 3 · 25 − 5 = 70°', 'Bütünleri: 180° − 70° = 110°'],
 '110°',
 'Denklemi çözüp x\'i cevap sanmak ya da ters açı yerine toplamı 180° almak. Kontrol: şekilde açılar **eşit mi, bütünler mi** diye konumlarına bak.',
 'Ters açı eşit, yan yana bütünler.')
# 7
m = (-3 - 5) / (3 - (-1)); assert m == -2 and 5 + (-2) * (0 + 1) == 3 and -3 == -2 * 3 + 3
kart('geo-dogrunun-analitigi-03', 'Eğim ve doğru denklemi',
 'İki noktadan eğimi bulup işaretini yorumlayabilmeni ve bu eğimle doğru denklemini yazabilmeni.',
 'Eğim, **dikey farkın yatay farka** oranıdır; x ekseniyle yapılan açı α ise m = tan α. Sağa yükselen doğrunun eğimi **pozitif**, alçalanın **negatiftir**. Eğimi m olan ve (x₁, y₁)\'den geçen doğru: y − y₁ = m(x − x₁).',
 'm = (y₂ − y₁) / (x₂ − x₁)', None,
 'A(−1, 5) ve B(3, −3) noktalarından geçen doğrunun denklemi nedir?',
 ['Eğim: m = (−3 − 5) / (3 − (−1)) = −8 / 4 = −2', 'Sağa giderken doğru iniyor, eğim negatif olmalı: uygun', 'A\'dan geçen doğru: y − 5 = −2(x + 1)', 'Düzenle: y = −2x + 3'],
 'y = −2x + 3',
 'Oranı ters kurmak (yatay ÷ dikey) ya da işareti düşünmeden yazmak. Kontrol: **sağa giderken doğru aşağı iniyorsa** eğim negatiftir.',
 'Eğim: dikey bölü yatay.')
# 8
tp = 1 + 2 + 4 + 5; assert 360 / tp == 30 and 5 * 30 == 150
kart('geo-dortgenler-01', 'Dörtgende açılar toplamı',
 'Dörtgenin iç açıları toplamının 360° olduğunu ve oranı verilen açıları bu toplamdan paylaştırabilmeni.',
 'Konveks dörtgenin iç açıları toplamı **360°**\'dir. Oranı verilen açılarda bir parça = 360° ÷ toplam parça sayısıdır. Açıortay sorularında yarım açıları, üçgenin **180°** toplamıyla birleştir.',
 'A + B + C + D = 360°', None,
 'Açıları 1 : 2 : 4 : 5 oranında olan dörtgenin en büyük açısı kaç derecedir?',
 ['Toplam parça: 1 + 2 + 4 + 5 = 12', 'Bir parça: 360° ÷ 12 = 30°', 'En büyük açı: 5 · 30° = 150°'],
 '150°',
 'Toplamı 180° almak ya da kalan toplamı açı sayısına bölüp oranı yok saymak. Kontrol: bulduğun dört açının toplamı **360° ediyor mu?**',
 'Dörtgen: dört açı, toplam 360°.')
# 9
assert math.hypot(7, 24) == 25 and 4 * 25 == 100
kart('geo-eskenar-dortgen-02', 'Eşkenar dörtgen: kenar ve köşegen',
 'Köşegenlerin birbirini dik ortaladığını kullanıp kenarı, çevreyi ve açıları bulabilmeni.',
 'Eşkenar dörtgenin köşegenleri birbirini **dik ortalar** ve köşe açılarını ikiye böler. Kenar, yarım köşegenlerin oluşturduğu dik üçgenin **hipotenüsüdür**. Eşit genişlikli iki şeridin ortak parçası da eşkenar dörtgendir; kenar = genişlik ÷ sin(açı).',
 'a² = (d₁ / 2)² + (d₂ / 2)²', S['eskenar'],
 'Köşegenleri 14 cm ve 48 cm olan eşkenar dörtgenin çevresi kaç cm\'dir?',
 ['Yarım köşegenler: 14 ÷ 2 = 7 ve 48 ÷ 2 = 24', 'Kenar: √(7² + 24²) = √625 = 25', 'Çevre: 4 · 25 = 100'],
 '100 cm',
 'Köşegenleri toplamak ya da yarım köşegenleri (7 + 24) kenar sanmak. Kontrol: **kenar, iki yarım köşegenin her birinden uzundur.**',
 'Yarım köşegenler dik üçgen kurar.')
# 10
x = 7; assert 3 * x - 4 == x + 10 and 3 * x - 4 == 17
kart('geo-eslik-ve-01', 'Eş üçgenlerde karşılıklı kenarlar',
 'Eşlik yazımındaki harf sırasından karşılıklı kenarları bulup eşitleyerek bilinmeyeni çözebilmeni.',
 'Üçgenler **KAK, AKA ya da KKK** ile eştir. ABC ≅ DEF yazımında köşeler sırayla eşleşir: A↔D, B↔E, C↔F. Eş üçgenlerde karşılıklı kenarlar ve açılar **eşittir**. Kenarı köşe sırasından bul, sonra eşitle.',
 'ABC ≅ DEF → |AB| = |DE|, |BC| = |EF|, |AC| = |DF|', None,
 'ABC ≅ DEF, |AB| = 3x − 4 ve |DE| = x + 10 ise |AB| kaçtır?',
 ['A↔D ve B↔E olduğundan |AB| = |DE|', '3x − 4 = x + 10 → 2x = 14 → x = 7', '|AB| = 3 · 7 − 4 = 17'],
 '17',
 'x\'i bulup cevap olarak yazmak ya da yanlış kenarları eşlemek. Kontrol: soru **x\'i mi yoksa uzunluğu mu** istiyor, bir kez daha oku.',
 'Harf sırası eşleşmeyi söyler.')
# 11
assert 90 + 60 == 150 and (180 - 150) / 2 == 15
kart('geo-kare-02', 'Karede açı ve eşkenar üçgen',
 'Kare ve eşkenar üçgenin ortak kenarından ikizkenar üçgenleri görüp açıyı hesaplayabilmeni.',
 'Karede dört kenar eşit, açılar **90°**\'dir; köşegen köşe açısını 45°\'ye böler. Eşkenar üçgenin açıları **60°**\'dir. Kare ile eşkenar üçgenin kenarı çakışırsa iki kenar eşit olur ve **ikizkenar üçgen** oluşur; taban açıları eşittir.',
 'kare 90° + eşkenar 60° → ikizkenar üçgen', S['kare'],
 'ABCD karesinin dışına, [AB] kenarı üzerine ABE eşkenar üçgeni çiziliyor. m(BCE) kaç derecedir?',
 ['|BE| = |AB| = |BC| olduğundan BCE ikizkenardır', 'm(CBE) = 90° + 60° = 150°', 'Taban açısı: (180° − 150°) ÷ 2 = 15°'],
 '15°',
 'İkizkenarlığı fark etmeden 90° − 60° = 30° gibi tek adımlık işlem yapmak. Kontrol: **hangi iki kenar eşit?** önce onu bul, sonra tepe açısını hesapla.',
 'Ortak kenar, ikizkenar demektir.')
# 12
assert 84 / 6 == 14 and 2 * 14 == 28
kart('geo-kenarortay-01', 'Kenarortay ve alan',
 'Kenarortayların üçgeni eşit alanlı parçalara böldüğünü kullanıp istenen bölgenin alanını bulabilmeni.',
 'Bir kenarortay üçgeni **eşit alanlı iki** parçaya böler. Üç kenarortay üçgeni **eşit alanlı 6** küçük üçgene ayırır; her biri toplamın 1/6\'sıdır. Bölgenin kaç parça içerdiğini say; toplam alanı 6\'ya bölüp parça sayısıyla çarp.',
 'küçük üçgen = A(ABC) ÷ 6', S['kenarortay'],
 'Alanı 84 cm² olan ABC üçgeninde [AD] ve [BE] kenarortaydır, kesişim noktası G\'dir. CDGE dörtgeninin alanı kaç cm²\'dir?',
 ['Bir küçük üçgen: 84 ÷ 6 = 14', 'CDGE, iki küçük üçgenden (DGC ve CGE) oluşur', 'Alan: 2 · 14 = 28'],
 '28 cm²',
 'Bölgeyi tek parça sanmak ya da parça sayısını yanlış saymak. Kontrol: bölgenin içindeki **küçük üçgenleri tek tek say.**',
 'Üç kenarortay, altı eş alan.')
# 13
assert math.hypot(8, 15) == 17 and 8 * 17 == 136
kart('geo-koni-01', 'Koni: ana doğru ve yanal alan',
 'Yarıçap, yükseklik ve ana doğrunun dik üçgen kurduğunu görüp ana doğruyu ve yanal alanı bulabilmeni.',
 'Koninin yarıçapı, yüksekliği ve ana doğrusu bir **dik üçgen** oluşturur; ana doğru **hipotenüstür**. Yanal alan π r ℓ, taban alanı π r²\'dir. Tüm alan, taban ile yanal alanın toplamıdır.',
 'ℓ² = r² + h² · yanal alan = π r ℓ', S['koni'],
 'Yarıçapı 8 cm, yüksekliği 15 cm olan koninin yanal alanı kaç cm²\'dir?',
 ['Ana doğru: ℓ = √(8² + 15²) = √289 = 17', 'Yanal alan: π · 8 · 17 = 136π'],
 '136π cm²',
 'Pisagor yerine çıkarma yapmak ya da yarıçapı ana doğru sanmak. Kontrol: **ana doğru, r ve h\'nin ikisinden de büyük** çıkmalıdır.',
 'Ana doğru, dik üçgenin hipotenüsü.')
# 14
n = 6; assert 12 * (n - 2) == 48 and 8 + 12 * (n - 2) + 6 * (n - 2)**2 + (n - 2)**3 == n**3
kart('geo-kup-02', 'Boyanıp bölünen küp',
 'Küçük küpleri köşe, ayrıt, yüz içi ve iç diye sınıflayıp istenen türü sayabilmeni.',
 'Her ayrıtı n parçaya bölünen küpte köşe küpler **3 yüzü**, ayrıt küpleri **2 yüzü**, yüz içindekiler **1 yüzü** boyalıdır; içteki **(n − 2)³** küpün boyası yoktur. Önce küçük küpleri sınıfla, sonra istenen sınıfı say.',
 '2 yüzü boyalı = 12 (n − 2) · 1 yüzü boyalı = 6 (n − 2)²', S['kup'],
 'Dış yüzeyi boyanıp her ayrıtı 6 eş parçaya bölünen küpte tam iki yüzü boyalı kaç küçük küp vardır?',
 ['Tam iki yüzü boyalı küpler ayrıtlardadır, köşeler hariç', 'Bir ayrıtta 6 − 2 = 4 küp var', 'Küpün 12 ayrıtı var: 12 · 4 = 48'],
 '48',
 'Köşe küpleri de ayrıta katmak (12 · 6) ya da boyalı yüzü olan bütün küpleri saymak. Kontrol: köşeler **3 yüzlü** gruptadır, ayrıta sayma.',
 'Köşe üç, ayrıt iki, yüz bir.')
# 15
assert math.hypot(8, 15) == 17
kart('geo-noktanin-analitigi-01', 'Uzaklık, orta nokta, bölen nokta',
 'Koordinat farklarından iki nokta arasındaki uzaklığı bulup orta ve bölen noktayı hesaplayabilmeni.',
 'Uzaklık, koordinat **farklarıyla** Pisagor\'dur: farkları ayrı ayrı karele, topla, karekökü al. Orta nokta koordinatların **ortalamasıdır**. Oranla bölen noktada her koordinatı ayrı hesapla: |AP| : |PB| = m : n ise P = (n·A + m·B) / (m + n).',
 '|AB| = √[(x₂ − x₁)² + (y₂ − y₁)²]', None,
 'A(−4, −1) ve B(4, 14) noktaları arasındaki uzaklık kaçtır?',
 ['Farklar: 4 − (−4) = 8 ve 14 − (−1) = 15', 'Pisagor: √(8² + 15²) = √(64 + 225) = √289', 'Uzaklık: 17'],
 '17',
 'Farkları toplamak (8 + 15) ya da karekökü almayı unutmak. Kontrol: uzaklık **her farktan büyük**, farkların toplamından küçüktür.',
 'Fark, kare, topla, kök.')
# 16
assert 12 * 5 == 60 and 60 / 8 == 7.5
kart('geo-paralelkenar-02', 'Paralelkenarın alanı',
 'Alanı taban ile o tabana ait dik yüksekliğin çarpımı olarak hesaplayıp yan kenarı yükseklikle karıştırmamayı.',
 'Paralelkenarın alanı **taban × o tabana ait yükseklik**\'tir. Yükseklik tabana **dik** uzaklıktır, yan kenar değildir. Üçgen gibi ikiye bölünmez. Köşegen ve orta noktalar paralelkenarı **eşit alanlı** parçalara ayırır.',
 'Alan = taban × yükseklik', S['paralelkenar'],
 'Tabanı 12 cm, yan kenarı 8 cm, tabana ait yüksekliği 5 cm olan paralelkenarın alanı kaç cm²\'dir? 8 cm\'lik kenara ait yükseklik kaç cm\'dir?',
 ['Alan = 12 · 5 = 60', 'Aynı alan 8 cm\'lik tabanla: 8 · h = 60', 'h = 60 ÷ 8 = 7,5'],
 'Alan 60 cm², yükseklik 7,5 cm',
 'Yan kenarı yükseklik sanmak ya da alanı ikiye bölmek. Kontrol: yükseklik tabana **dik** çizilen kesik çizgidir; yan kenar ondan uzundur.',
 'Taban çarpı dik yükseklik.')
# 17
assert 9 * 9 * 8 / 3 == 216 and 81 / 4 == 20.25
kart('geo-piramit-02', 'Piramidin hacmi ve kesit',
 'Hacmi taban alanı ve dik yükseklikle bulup tabana paralel kesitte benzerlik oranını kullanabilmeni.',
 'Piramidin hacmi **taban alanı × yükseklik ÷ 3**\'tür; yükseklik tepeden tabana inen dik uzunluktur. Tabana paralel kesit tabana benzerdir. Benzerlik oranı tepeden uzaklıkların oranıdır, **alanlar oranı bunun karesidir**.',
 'V = (taban alanı · h) ÷ 3 · alan oranı = k²', S['piramit'],
 'Taban kenarı 9 cm, yüksekliği 8 cm olan kare dik piramidin hacmi kaç cm³\'tür? Yüksekliğin orta noktasından tabana paralel kesilirse kesit alanı kaç cm²\'dir?',
 ['Taban alanı 9 · 9 = 81; V = 81 · 8 ÷ 3 = 216', 'Kesit, tepeden yarı uzaklıkta: k = 1/2', 'Kesit alanı: 81 · (1/2)² = 81/4 = 20,25'],
 '216 cm³ ve 20,25 cm²',
 'Taban alanı yerine kenarı ya da çevreyi çarpmak, 3 yerine 2\'ye bölmek. Kontrol: önce **taban alanını** yaz, yüksekliği çarp, en son 3\'e böl.',
 'Taban çarpı yükseklik, bölü üç.')
# 18
assert math.hypot(5, 12) == 13 and 2 * 30 + 30 * 10 == 360
kart('geo-prizmalar-03', 'Prizmanın hacmi ve yüzey alanı',
 'Prizmanın hacmini ve yüzey alanını taban alanı, taban çevresi ve yükseklikten kurabilmeni.',
 'Hacim **taban alanı × yükseklik**\'tir. Tüm yüzey alanı **2 × taban alanı + taban çevresi × yükseklik**\'tir. Dikdörtgenler prizmasında üç farklı yüzün alanını topla, ikiyle çarp. Alt ve üst tabanı unutma.',
 'V = Tₐ · h · Yüzey = 2Tₐ + Ç · h', S['prizma'],
 'Tabanı dik kenarları 5 cm ve 12 cm olan dik üçgen, yüksekliği 10 cm olan dik prizmanın tüm yüzey alanı kaç cm²\'dir?',
 ['Hipotenüs √(25 + 144) = 13; taban alanı 5 · 12 ÷ 2 = 30', 'Taban çevresi: 5 + 12 + 13 = 30', 'Yüzey: 2 · 30 + 30 · 10 = 60 + 300 = 360'],
 '360 cm²',
 'Alt ve üst tabanı unutup yalnız yan yüzleri saymak. Kontrol: **tabanlar iki tane**, yan yüzler taban çevresi × yükseklikle gelir.',
 'İki taban artı yan yüzler.')
# 19
assert (9 + 15) / 2 * 7 == 84
kart('geo-yamuk-01', 'Yamuğun alanı',
 'Yamuğun alanını iki tabanı ve dik yüksekliği kullanarak hesaplayabilmeni.',
 'Yamuğun alanı **tabanlar toplamının yarısı × yükseklik**\'tir. Yükseklik iki tabana **dik** uzaklıktır, yan kenar değildir. İkizkenar yamukta aynı tabana ait açılar ve köşegenler eşittir.',
 'Alan = (a + c) ÷ 2 · h', S['yamuk'],
 'Tabanları 9 cm ve 15 cm, yüksekliği 7 cm olan yamuğun alanı kaç cm²\'dir?',
 ['Tabanlar toplamı: 9 + 15 = 24', 'Yarısı: 24 ÷ 2 = 12', 'Alan: 12 · 7 = 84'],
 '84 cm²',
 'Tabanlardan yalnız birini kullanmak ya da toplamı 2\'ye bölmeyi unutmak. Kontrol: iki tabanı da **parantez içinde** topladığından emin ol.',
 'Taban toplamının yarısı çarpı yükseklik.')
# 20
x = 25; assert 4 * x + 5 + 2 * x + 25 == 180 and 4 * x + 5 == 105 and 2 * x + 25 == 75 and 180 - 75 == 105
kart('geo-cemberde-aci-01', 'Kirişler dörtgeni',
 'Kirişler dörtgeninde karşılıklı açıların bütünlerini kullanıp iç ve dış açıyı bulabilmeni.',
 'Köşeleri çemberde olan dörtgende **karşılıklı açıların toplamı 180°**\'dir. Bir kenar uzatılınca oluşan **dış açı, karşısındaki iç açıya eşittir**. Doğrusal açılar da 180°\'ye tamamlanır. x\'i bulduktan sonra sorulan açıya dön.',
 'A + C = 180° · dış açı = karşıt iç açı', S['kirisler'],
 'ABCD kirişler dörtgeninde m(A) = (4x + 5)° ve m(C) = (2x + 25)°\'dir. [BC] uzatılırsa C köşesindeki dış açı (DCE) kaç derecedir?',
 ['Karşılıklı açılar bütünler: 4x + 5 + 2x + 25 = 180', '6x = 150 → x = 25; m(A) = 105°, m(C) = 75°', 'Dış açı: 180° − 75° = 105° (A açısına eşit)'],
 '105°',
 'Karşılıklı açıları eşit sanmak ya da x\'i bulup iç açıda kalmak. Kontrol: soru **dış açıyı** soruyorsa son adım 180°\'den çıkarmaktır.',
 'Karşılıklı açılar 180° yapar.')
# 21
assert 360 / 10 == 36 and 3 * 36 / 2 == 54
kart('geo-cemberde-aci-04', 'Eşit yay ve çevre açı',
 'Eşit kirişlerin eşit yay ayırdığını ve çevre açının gördüğü yayın yarısı olduğunu kullanabilmeni.',
 'Çemberde eşit kirişler **eşit yayları** ayırır; paralel iki kirişin arasında kalan yaylar eşittir. Çevre açı, gördüğü yayın **yarısıdır**. Eşit aralıklı n noktada her yay 360° ÷ n\'dir. Önce yayları, sonra yayları gören açıları yaz.',
 'çevre açı = yay ÷ 2 · eşit aralıkta yay = 360° ÷ n', None,
 'Bir çember üzerinde eşit aralıklı 10 nokta var. 3 aralık uzunluğundaki yayı gören çevre açı kaç derecedir?',
 ['Her yay: 360° ÷ 10 = 36°', '3 aralık: 3 · 36° = 108°', 'Çevre açı: 108° ÷ 2 = 54°'],
 '54°',
 'Verilen başka bir açıyı x\'e eşit sanmak ya da yayı yarılamayı unutmak. Kontrol: **x hangi yayı görüyor?** Yayı bul, sonra yarıla.',
 'Çevre açı, yayın yarısıdır.')
# 22
assert (5 - 0) ** 2 + (2 - 2) ** 2 == 25 and (2 - (-3)) ** 2 == 25
kart('geo-cemberin-analitigi-01', 'Çember denklemi',
 'Merkez ve yarıçaptan çember denklemini yazıp denklemden merkez ve yarıçapı okuyabilmeni.',
 'Merkezi M(a, b), yarıçapı r olan çemberin denklemi **(x − a)² + (y − b)² = r²**\'dir. Parantezdeki işaret merkezin **ters işaretlisidir**. Sağ taraf yarıçapın **karesidir**: 25 görürsen r = 5\'tir.',
 '(x − a)² + (y − b)² = r²', None,
 'Merkezi M(−3, 2) ve yarıçapı 5 olan çemberin denklemi nedir?',
 ['a = −3, b = 2, r = 5', '(x − (−3))² + (y − 2)² = 5²', '(x + 3)² + (y − 2)² = 25'],
 '(x + 3)² + (y − 2)² = 25',
 'Merkezin işaretini ters yazmak ya da sağ tarafa r\'yi (5) ya da çapı yazmak. Kontrol: **(x + 3) görürsen merkezin apsisi −3\'tür.**',
 'Parantez ters işaret, sağ taraf r².')
# 23
n = 360 // 30; assert n == 12 and n * (n - 3) // 2 == 54
kart('geo-cokgenler-02', 'Çokgende köşegen sayısı',
 'Kenar sayısını bulup toplam köşegen sayısını ve düzgün çokgende açıları hesaplayabilmeni.',
 'n kenarlı çokgende bir köşeden **n − 3** köşegen çizilir; toplam köşegen **n(n − 3) ÷ 2**\'dir. Bir köşeden çizilen köşegenler çokgeni **n − 2** üçgene ayırır. Düzgün çokgende bir dış açı **360° ÷ n**\'dir.',
 'köşegen sayısı = n (n − 3) ÷ 2', None,
 'Bir dış açısı 30° olan düzgün çokgenin kaç köşegeni vardır?',
 ['Kenar sayısı: n = 360° ÷ 30° = 12', 'Bir köşeden 12 − 3 = 9 köşegen çizilir', 'Toplam: 12 · 9 ÷ 2 = 54'],
 '54',
 'Yalnız bir köşeden çıkanları saymak ya da üçgen sayısını kenar sayısı sanmak. Kontrol: **2\'ye bölmeyi** unutma, her köşegen iki köşeden sayılır.',
 'Köşegen: n çarpı n eksi 3, bölü 2.')
# 25
assert 10 * 6 / 2 == 30 and 2 * 30 / 7.5 == 8
kart('geo-ucgende-alan-03', 'Üçgenin alanı',
 'Alanı taban ve ona ait yükseklikle ya da iki kenar ve aradaki açıyla bulup başka tabana ait yüksekliği hesaplayabilmeni.',
 'Üçgenin alanı **taban × yükseklik ÷ 2**\'dir. Her kenar taban olabilir; yükseklik, o kenara karşı köşeden inen dikmedir. Aynı alan farklı tabanlarla yazılır. İki kenar ve aradaki açı verilirse alan **½ · a · b · sin C**\'dir.',
 'A = (taban · h) ÷ 2 = ½ · a · b · sin C', S['alan'],
 'ABC üçgeninde |BC| = 10 cm, bu kenara ait yükseklik 6 cm ve |AC| = 7,5 cm\'dir. |AC|\'ye ait yükseklik kaç cm\'dir?',
 ['Alan: 10 · 6 ÷ 2 = 30', 'Aynı alan AC tabanıyla: 7,5 · h ÷ 2 = 30', 'h = 60 ÷ 7,5 = 8'],
 '8 cm',
 'Alanı ikiye bölüp yüksekliği bulurken yine ikiye bölmek ya da başka tabana ait yüksekliği kullanmak. Kontrol: **her yükseklik kendi tabanıyla** eşleşir.',
 'Her taban kendi yüksekliğiyle.')
# 26
assert 180 - 40 - 65 == 75
kart('geo-ucgende-acilar-03', 'Üçgende açılar ve kenarlar',
 'İç ve dış açı bağıntılarıyla açıları bulup açı–kenar sıralamasını kurabilmeni.',
 'İç açılar toplamı **180°**\'dir. Dış açı, komşu olmayan **iki iç açının toplamına** eşittir; dış açılar toplamı 360°\'dir. **Büyük açının karşısı büyük kenardır**; eşit açıların karşısı eşit kenardır. Önce üçüncü açıyı bul.',
 'A + B + C = 180° · dış açı = iki uzak iç açının toplamı', None,
 'ABC üçgeninde m(A) = 40° ve m(B) = 65°\'dir. Kenarları küçükten büyüğe sıralayın.',
 ['m(C) = 180° − 40° − 65° = 75°', 'Karşılıklar: A → |BC|, B → |AC|, C → |AB|', 'Sıralama: |BC| < |AC| < |AB|'],
 '|BC| < |AC| < |AB|',
 'Her açıya karşısındaki yerine komşu kenarı eşlemek ya da üçüncü açıyı hesaplamadan sıralamak. Kontrol: açının **karşısındaki** kenar, o köşe harfini içermez.',
 'Büyük açının karşısı büyük kenar.')
# 27
x = 6; assert x / (x + 3) == 4 / 6 and x + x + 3 == 15
kart('geo-ucgende-benzerlik-03', 'Thales ve temel orantı',
 'Paralel doğruların kenarları orantılı böldüğünü kullanıp denklem kurarak uzunluk bulabilmeni.',
 'Üçgende bir kenara **paralel** doğru, diğer iki kenarı **orantılı** böler: DE // BC ise AD / DB = AE / EC. Paralel doğrular kesenlerini de orantılı parçalara ayırır (Thales). Cebirsel ifadeleri doğrudan orana yaz, bulduğun x\'i parçalarda yerine koy.',
 'AD / DB = AE / EC', S['benzerlik'],
 'DE // BC, |AD| = x, |DB| = x + 3, |AE| = 4 ve |EC| = 6 ise |AB| kaçtır?',
 ['Orantı: x / (x + 3) = 4 / 6', '6x = 4x + 12 → x = 6', '|AB| = x + (x + 3) = 6 + 9 = 15'],
 '15',
 'x\'i bulup orada kalmak ya da yalnız bir parçayı (x + 3 = 9) cevap yazmak. Kontrol: soru **tüm kenarı** mı yoksa parçayı mı soruyor?',
 'Paralel doğru, orantılı parçalar.')
# 28
tab = (180 - 44) / 2; assert tab == 68 and 180 - 2 * 68 == 44 and 68 - 44 == 24
# geometrik doğrulama: BD = BC, D, AC üzerinde
Bp = (3.6 * math.cos(math.radians(248)), 3.6 * math.sin(math.radians(248)))
Cp = (3.6 * math.cos(math.radians(292)), 3.6 * math.sin(math.radians(292)))
Dp = (1.58 * math.cos(math.radians(292)), 1.58 * math.sin(math.radians(292)))
assert abs(math.dist(Bp, Dp) - math.dist(Bp, Cp)) < 0.01
kart('geo-ikizkenar-ucgen-02', 'İkizkenar üçgende açı zinciri',
 'Taban açılarının eşitliğiyle art arda ikizkenar üçgenlerde açıları adım adım bulabilmeni.',
 'İkizkenar üçgende eşit kenarların karşısındaki **taban açıları eşittir**; iç açılar toplamı 180°\'dir. Art arda ikizkenar üçgen varsa bulduğun açıyı sonraki üçgene **taşı**. Her adımda eşit iki kenarı ve karşılarındaki açıları yaz.',
 'taban açısı = (180° − tepe açısı) ÷ 2', S['ikizkenar'],
 'ABC ikizkenar üçgeninde |AB| = |AC| ve m(A) = 44°\'dir. D, [AC] üzerinde ve |BD| = |BC| ise m(ABD) kaç derecedir?',
 ['Taban açıları: (180° − 44°) ÷ 2 = 68°, yani m(B) = m(C) = 68°', 'BCD ikizkenar (|BD| = |BC|): m(BDC) = m(C) = 68°', 'm(DBC) = 180° − 2 · 68° = 44°', 'm(ABD) = 68° − 44° = 24°'],
 '24°',
 'Taban açısını yarıya bölmek ya da tepe açısını bulup bırakmak. Kontrol: son açıyı diğerleriyle topla, **180°\'ye ulaşıyor mu** bak.',
 'Eşit kenar, eşit taban açısı.')

# birleşen / kapsam dışı
sonuc = {k['id']: k for k in K}
sonuc['geo-ozel-dortgenler-02'] = {'id': 'geo-ozel-dortgenler-02', 'birlesti': 'geo-eskenar-dortgen-02'}

girdi = open('/tmp/kor/kart/parti/p06.txt', encoding='utf-8').read()
idler = re.findall(r'^### (\S+) \|', girdi, re.M)
assert set(idler) == set(sonuc) and len(idler) == len(sonuc), (set(idler) ^ set(sonuc))
cikti = [sonuc[i] for i in idler]

def kel(s): return len(s.replace('**', '').split())
zorunlu = ['id', 'k', 'baslik', 'olcer', 'kural', 'formul', 'sekil', 'ornek', 'hata', 'akilda']
for c in cikti:
    if 'birlesti' in c or 'kapsamDisi' in c:
        continue
    for z in zorunlu:
        assert z in c, (c['id'], z)
    for z in ['id', 'k', 'baslik', 'olcer', 'kural', 'hata', 'akilda']:
        assert c[z], (c['id'], z)
    assert kel(c['baslik']) <= 6, (c['id'], 'baslik', kel(c['baslik']))
    assert kel(c['olcer']) <= 25 and not c['olcer'].startswith('Bu soru'), (c['id'], 'olcer', kel(c['olcer']))
    assert kel(c['kural']) <= 60 and '**' in c['kural'], (c['id'], 'kural', kel(c['kural']))
    assert kel(c['hata']) <= 40, (c['id'], 'hata', kel(c['hata']))
    assert kel(c['akilda']) <= 8 and '"' not in c['akilda'] and '“' not in c['akilda'], (c['id'], 'akilda', kel(c['akilda']))
    o = c['ornek']
    assert o['soru'] and o['cevap'] and 2 <= len(o['adimlar']) <= 4, (c['id'], 'ornek')
    if c['sekil']:
        assert len(c['sekil'].encode()) <= 25000, (c['id'], len(c['sekil']))

import os
os.makedirs('/tmp/kor/kart/png', exist_ok=True)
for c in cikti:
    if c.get('sekil'):
        p = f"/tmp/kor/kart/p06/{c['id']}.svg"
        open(p, 'w').write(c['sekil'])
        os.system(f"rsvg-convert -w 360 {p} -o /tmp/kor/kart/png/{c['id']}.png")
sekilli = sum(1 for c in cikti if c.get('sekil'))
json.dump(cikti, open('/home/claude/zekacademy-app/havuz/tekrar/kart-p06.json', 'w'), ensure_ascii=False, indent=1)
print(len(cikti), 'kayit;', sum(1 for c in cikti if 'baslik' in c), 'kart;', sekilli, 'sekilli')
