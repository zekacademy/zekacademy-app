import sys, re, json, math
from fractions import Fraction as Fr
sys.path.insert(0, '/home/claude/zekacademy-app/havuz')
from cizim import tikz_svg

K = []
def kart(id, k, baslik, olcer, kural, formul, sekil, soru, adimlar, cevap, hata, akilda):
    K.append({"id": id, "k": k, "baslik": baslik, "olcer": olcer, "kural": kural, "formul": formul,
              "sekil": sekil, "ornek": {"soru": soru, "adimlar": adimlar, "cevap": cevap},
              "hata": hata, "akilda": akilda})

def fmt(x):
    return str(x).replace('.', ',')

# ---------------- ŞEKİLLER ----------------
def sk_basinc():
    return tikz_svg(r'''\begin{tikzpicture}[scale=0.8,font=\footnotesize]
\fill[gray!45] (0,1.6) rectangle (1,3.4);
\draw[line width=1.2pt] (0,5) -- (0,0) -- (1,0) -- (1,5);
\node[right] at (1.1,0.8) {gaz};
\node[right] at (1.1,2.5) {cıva};
\draw[<->] (-0.35,1.6) -- (-0.35,3.4); \node[left] at (-0.4,2.5) {$h$};
\draw[->,vurgu,thick] (0.5,5.9) -- (0.5,3.6); \node[vurgu,right] at (0.6,5.3) {$P_0$};
\end{tikzpicture}''')

def sk_direnc():
    return tikz_svg(r'''\begin{tikzpicture}[scale=0.8,font=\footnotesize]
\draw[->] (0,0) -- (4.3,0) node[below left] {$I$ (A)};
\draw[->] (0,0) -- (0,4.3) node[above] {$V$ (V)};
\draw[vurgu,thick] (0,0) -- (3.9,3.9);
\draw[dashed] (3,0) -- (3,3) -- (0,3);
\fill (3,3) circle (1.8pt);
\node[below] at (3,0) {3}; \node[left] at (0,3) {18};
\end{tikzpicture}''')

def sk_konum():
    return tikz_svg(r'''\begin{tikzpicture}[font=\footnotesize]
\draw[->] (0,0) -- (4.4,0) node[right] {$t$ (s)};
\draw[->] (0,0) -- (0,3.3) node[above] {$x$ (m)};
\draw[vurgu,thick] (0,0.3) -- (2,2.7) -- (4,1.5);
\draw[dashed] (0,0.3) -- (0,0.3) (0,2.7) -- (2,2.7) -- (2,0) (0,1.5) -- (4,1.5) -- (4,0);
\node[left] at (0,0.3) {2}; \node[left] at (0,2.7) {18}; \node[left] at (0,1.5) {10};
\node[below] at (2,0) {4}; \node[below] at (4,0) {8};
\end{tikzpicture}''')

def sk_ayna():
    return tikz_svg(r'''\begin{tikzpicture}[font=\footnotesize]
\draw[line width=1.6pt] (0,-1.2) -- (0,1.8);
\foreach \y in {-1,-0.6,...,1.6} \draw (0,\y) -- (0.15,\y-0.15);
\draw[->,thick] (-2,0) -- (-2,1); \node[below] at (-2,0) {cisim};
\draw[->,thick,dashed,vurgu] (2,0) -- (2,1); \node[below] at (2,0) {görüntü};
\draw[<->] (-2,-0.9) -- (0,-0.9); \node[above] at (-1,-0.9) {$x$};
\draw[<->] (0,-0.9) -- (2,-0.9); \node[above] at (1,-0.9) {$x$};
\draw[<->,vurgu] (-2,-1.6) -- (2,-1.6); \node[below] at (0,-1.6) {$2x$};
\end{tikzpicture}''')

def sk_mercek():
    return tikz_svg(r'''\begin{tikzpicture}[scale=0.55,font=\footnotesize]
\draw (-5,0) -- (7.2,0);
\draw[<->,thick] (0,-2.6) -- (0,2.6);
\foreach \x/\t in {-4/2F,-2/F,2/F',4/2F'} {\draw (\x,-0.1) -- (\x,0.1); \node[below] at (\x,-0.15) {\t};}
\draw[->,thick] (-3,0) -- (-3,1); \node[above] at (-3,1) {cisim};
\draw[->,thick,vurgu] (6,0) -- (6,-2); \node[below] at (6,-2) {görüntü};
\draw[gray] (-3,1) -- (0,1) -- (6,-2);
\draw[gray] (-3,1) -- (6,-2);
\end{tikzpicture}''')

def sk_is():
    return tikz_svg(r'''\begin{tikzpicture}[font=\footnotesize]
\fill[vurgu!25] (0,0) -- (1,1.6) -- (3,1.6) -- (4,0) -- cycle;
\draw[->] (0,0) -- (4.6,0) node[right] {$x$ (m)};
\draw[->] (0,0) -- (0,2.3) node[above] {$F$ (N)};
\draw[vurgu,thick] (0,0) -- (1,1.6) -- (3,1.6) -- (4,0);
\draw[dashed] (0,1.6) -- (1,1.6) (1,1.6) -- (1,0) (3,1.6) -- (3,0);
\node[left] at (0,1.6) {4};
\node[below] at (1,0) {2}; \node[below] at (3,0) {6}; \node[below] at (4,0) {8};
\end{tikzpicture}''')

def sk_yuzen():
    return tikz_svg(r'''\begin{tikzpicture}[font=\footnotesize]
\draw[line width=1.2pt] (0,3) -- (0,0) -- (3,0) -- (3,3);
\fill[blue!15] (0.03,0.03) rectangle (2.97,1.8);
\draw[blue!60] (0.03,1.8) -- (2.97,1.8);
\fill[orange!25] (0.8,0.8) rectangle (2.2,2.6);
\draw[thick] (0.8,0.8) rectangle (2.2,2.6);
\draw[dashed] (0.8,1.8) -- (2.2,1.8);
\node[right] at (3.1,2.2) {dışarıda: 3/8};
\node[right] at (3.1,1.3) {batan: 5/8};
\end{tikzpicture}''')

# ---------------- KARTLAR ----------------

# 1. basınç-02
gaz1 = 75 + 20; gaz2 = 75 - 20
assert (gaz1, gaz2) == (95, 55)
kart("fiz-basinc-02", "fiz|Basınç", "Gaz basıncı ve Bernoulli",
 "Hapsolmuş gazın basıncını açık hava basıncı ve cıva sütunuyla dengeleyerek bulabilmeni.",
 "Cıva tıkacın her yüzüne etki eden **basınçları listele** ve dengeyi yaz. Kapalı uç altta, tüp ağzı yukarıdaysa gaz basıncı P₀ + h olur; ağız aşağıdaysa P₀ − h olur. Bernoulli: dar kesitte akışkan hızlanır ve **hız arttıkça basınç azalır**.",
 "Ağız yukarı: P_gaz = P₀ + h · Ağız aşağı: P_gaz = P₀ − h",
 sk_basinc(),
 "Açık hava basıncı 75 cmHg. Kapalı ucu altta olan dikey tüpte 20 cm'lik cıva tıkaç gazı hapsetmiştir. Gazın basıncı kaç cmHg'dir? Tüp ters çevrilirse kaç olur?",
 ["Tıkaç dengede: gazın yukarı itişi, aşağıdaki P₀ ile cıvanın basıncının toplamına eşittir.",
  f"Ağız yukarı: P_gaz = 75 + 20 = {gaz1} cmHg.",
  f"Ters çevirince cıva gazın altında kalır: P_gaz + 20 = 75, P_gaz = {gaz2} cmHg."],
 f"{gaz1} cmHg; ters çevrilince {gaz2} cmHg",
 "Gaz basıncını yalnız cıva yüksekliğine eşitlemek ya da cıvayı hep çıkarmak. Çıkarma yalnız ağız aşağıdayken yapılır. Kontrol: cıva gazın üstündeyse gaz sıkışır, **basınç P₀'dan büyüktür**.",
 "Tıkacın iki yüzünü yaz, eşitle.")

# 2. basınç-04
m, g = 12, 10
a_cm2 = 10 * 20; A = Fr(a_cm2, 10**4); G = m * g; P = G / A
assert A == Fr(2, 100) and G == 120 and P == 6000
kart("fiz-basinc-04", "fiz|Basınç", "Katı basıncı",
 "Cismin zemine yaptığı basıncı ağırlık ve temas alanından hesaplayıp yüzeyleri karşılaştırabilmeni.",
 "Katı basıncı, ağırlığın **zemine değen yüzün alanına** bölümüdür. Alanı cm²'den m²'ye çevir (1 cm² = 10⁻⁴ m²). Ağırlık G = m·g'dir; kütleyi doğrudan kullanma. Cismi çevirince ağırlık aynı kalır, alan değişir: **küçük alan, büyük basınç**.",
 "P = F / A = m·g / A",
 None,
 "Kütlesi 12 kg, ayrıtları 10 cm, 20 cm ve 30 cm olan prizma en küçük yüzü üzerinde duruyor (g = 10 N/kg). Zemine yaptığı basınç kaç Pa'dır?",
 ["Zemine değen en küçük yüz: 10 × 20 = 200 cm² = 0,02 m².",
  "Ağırlık: G = 12 × 10 = 120 N.",
  "P = 120 ÷ 0,02 = 6000 Pa."],
 "6000 Pa",
 "Zemine değen yüzü karıştırmak (yanlış iki ayrıtı çarpmak) ya da kütleyi ağırlık yerine kullanmak. Kontrol: alanı **hep zemine değen yüzden** al, kuvveti newton cinsinden yaz.",
 "Önce temas yüzü, sonra metrekare.")

# 3. dalgalar-02
v, t = 340, Fr(3, 2); x = v * t / 2
assert x == 255
kart("fiz-dalgalar-02", "fiz|Dalgalar", "Ses: yükseklik, şiddet, yankı",
 "Sesin inceliğinin frekansa, şiddetinin genliğe bağlı olduğunu ve yankıda yolun gidiş dönüş olduğunu bilmeni.",
 "Sesin **inceliği frekansa**, şiddeti genliğe bağlıdır: frekans büyükse ses incedir, genlik büyükse ses güçlüdür. Yankıda ses engele gidip döner; yol = hız × süre ve **engele uzaklık yolun yarısıdır**. Ses katıda en hızlı, gazda en yavaştır; ortam değişince frekans sabit kalır.",
 "Yankıda uzaklık: x = v · t / 2",
 None,
 "Ses hızı 340 m/s olan havada bir çığlığın yankısı 1,5 s sonra duyuluyor. Yansıtan engel kaç m uzaktadır?",
 ["Ses gidip geri döndü: toplam yol = 340 × 1,5 = 510 m.",
  "Engele uzaklık bu yolun yarısıdır: 510 ÷ 2 = 255 m."],
 "255 m",
 "Frekans ile genliği karıştırmak: sıklığı büyük dalgayı kalın sanmak. Yankıda **gidiş dönüş yolunu** uzaklık almak da sık hatadır. Osiloskopta sıklık frekansı, yükseklik genliği gösterir.",
 "Sıklık inceliği, genlik şiddeti belirler.")

# 4. dalgalar-04
f = Fr(12, 3); lam2 = Fr(8) / f
assert f == 4 and lam2 == 2
kart("fiz-dalgalar-04", "fiz|Dalgalar", "Su dalgasında ortam değişimi",
 "Su dalgası derinden sığa geçerken frekansın sabit kaldığını, hız ve dalga boyunun birlikte değiştiğini kullanabilmeni.",
 "Dalga ortam değiştirirken **frekans değişmez**; hız ve dalga boyu aynı oranda değişir. Derin yerde hız büyüktür, dalga boyu da büyüktür; sığa geçince ikisi küçülür. Her iki ortamda **v ÷ λ = f** aynıdır. Düz engelden yansımada hız, dalga boyu ve frekans değişmez.",
 "v₁/λ₁ = v₂/λ₂ = f",
 None,
 "Derin bölgede hızı 12 m/s, dalga boyu 3 m olan su dalgası sığ bölgeye geçince hızı 8 m/s oluyor. Sığ bölgede dalga boyu kaç m'dir?",
 ["Frekansı bul: f = 12 ÷ 3 = 4 Hz.",
  "Sığ bölgede de frekans 4 Hz'dir.",
  "λ = v ÷ f = 8 ÷ 4 = 2 m."],
 "2 m",
 "Dalga boyunun ortam değişince sabit kaldığını sanmak ya da yeni hızı eski dalga boyuna bölmek. Kontrol: bölme işlemini **aynı ortamın** hızı ve dalga boyuyla yap.",
 "Frekans sabit; hız ve boy beraber değişir.")

# 5. dinamik-01
N = 60 * (10 - 2)
assert N == 480
kart("fiz-dinamik-01", "fiz|Dinamik", "Serbest düşme ve asansör",
 "Hava direncinde limit hızı, asansördeki görünür ağırlığı ve ağırlıkla kütle farkını ayırt edebilmeni.",
 "Serbest düşmede yalnız ağırlık etkir; ivme herkes için g'dir. Hava direncinde hız arttıkça **direnç artar**, ağırlığa eşit olunca net kuvvet sıfırlanır ve cisim sabit hızla düşer (limit hız). Asansörde tartı ivme yukarıysa artar, **aşağıysa azalır**.",
 "Yukarı ivme: N = m(g + a) · Aşağı ivme: N = m(g − a)",
 None,
 "60 kg'lık bir kişi asansördeki tartının üstünde duruyor. Asansör 2 m/s² ivmeyle aşağı doğru hızlanıyor (g = 10 m/s²). Tartı kaç N gösterir?",
 ["Gerçek ağırlık: 60 × 10 = 600 N.",
  "İvme aşağı yönlü: tartı gerçek ağırlıktan az gösterir.",
  "N = 60 × (10 − 2) = 480 N."],
 "480 N",
 "Limit hıza yaklaşırken direncin azaldığını sanmak. Doğrusu: direnç **ağırlığa eşitlenene kadar artar**, ivme sıfıra gider. Ağırlık (N) ile kütleyi (kg) karıştırmak da sık hatadır.",
 "Direnç ağırlığa eşitse hız sabit.")

# 6. dinamik-03
Nn = 3 * 10; fs = Fr(2, 10) * Nn; Fn = 15 - fs; a = Fn / 3
assert (fs, Fn, a) == (6, 9, 3)
kart("fiz-dinamik-03", "fiz|Dinamik", "Sürtünme ve net kuvvet",
 "Bölgelere göre net kuvveti ayrı hesaplayıp hızın artıp azalmadığını yorumlayabilmeni.",
 "Sürtünme harekete **zıt yönde** etkir: F_net = F − f. Net kuvvet hareket yönündeyse hız artar, sıfırsa hız **sabit kalır**, zıt yöndeyse azalır. Kıpırdamadan önce sürtünme uygulanan kuvvete eşittir; hareket başlayınca kinetik sürtünme sabittir: f = μ·N.",
 "F_net = F − f · f = μ·N · a = F_net / m",
 None,
 "Yatay zeminde duran 3 kg'lık cisme 15 N'luk yatay kuvvet uygulanıyor. Kinetik sürtünme katsayısı 0,2, g = 10 m/s². Cismin ivmesi kaç m/s²'dir?",
 ["Normal kuvvet: N = 3 × 10 = 30 N.",
  "Sürtünme: f = 0,2 × 30 = 6 N.",
  "Net kuvvet: 15 − 6 = 9 N; a = 9 ÷ 3 = 3 m/s²."],
 "3 m/s²",
 "Net kuvveti sıfır olan bölgede cismin durduğunu sanmak. Net kuvvet sıfırsa cisim **o anki hızıyla sabit gider**. Her bölgede F ile f'yi ayrı ayrı karşılaştır.",
 "Net sıfırsa durmaz, sabit hızla gider.")

# 7. elektrik-01
E_gun = 5 * Fr(40, 1000) * 8; E_ay = E_gun * 30; fatura = E_ay * 2
assert (E_gun, E_ay, fatura) == (Fr(8, 5), 48, 96)
kart("fiz-elektrik-01", "fiz|Elektrik", "Elektrik enerjisi ve fatura",
 "Güç, adet ve süre verilerinden kWh'yi bulup faturaya çevirebilmeni.",
 "Enerji = güç × süre. Gücü **kW**, süreyi saat alırsan enerji kWh çıkar (100 W = 0,1 kW). Fatura için sırayla: günlük kWh, gün sayısıyla çarp, sonra **birim fiyatla çarp**. Etiketli lambada direnç R = V² ÷ P'dir; seri bağlı lambalarda direnci büyük olan daha çok güç harcar.",
 "E = P · t · adet → Fatura = E · gün · birim fiyat",
 None,
 "40 W'lık 5 lamba günde 8 saat yanıyor. 1 kWh 2 TL ise 30 günlük fatura kaç TL'dir?",
 ["Günlük enerji: 5 × 0,04 kW × 8 h = 1,6 kWh.",
  "30 günde: 1,6 × 30 = 48 kWh.",
  "Ücret: 48 × 2 = 96 TL."],
 "96 TL",
 "Gün sayısını ya da birim fiyatı çarpmayı unutmak, lamba adedini katmamak. Kontrol: son sonuç **TL mi, kWh mi?** Sorulan birime ulaşmadan bırakma.",
 "Günlük kWh, gün sayısı, birim fiyat.")

# 8. elektrik-03
R1 = Fr(18, 3); Req = R1 + 4; I = Fr(40) / Req
assert (R1, Req, I) == (6, 10, 4)
kart("fiz-elektrik-03", "fiz|Elektrik", "Direnç ve eşdeğer direnç",
 "Telin direncinin boy ve kesite bağlılığını, grafikten direnci ve eşdeğer direnci doğru bulabilmeni.",
 "Tel direnci **boyla doğru, kesitle ters** orantılıdır: R = ρ·ℓ/A. V–I grafiğinde herhangi bir noktadaki V ÷ I direnci verir. Seri bağlı dirençler toplanır ve **akım her birinde aynıdır**. Akımı bulmak için önce eşdeğer direnci, sonra I = V/R'yi kullan.",
 "R = ρ·ℓ/A · R_seri = R₁ + R₂ + … · I = V/R",
 sk_direnc(),
 "Grafiği verilen R₁ direnci (3 A, 18 V) noktasından geçiyor. R₁, 4 Ω'luk bir dirençle seri bağlanıp 40 V'luk kaynağa takılıyor. Devre akımı kaç A'dır?",
 ["Grafikten: R₁ = 18 ÷ 3 = 6 Ω.",
  "Seri eşdeğer direnç: 6 + 4 = 10 Ω.",
  "I = 40 ÷ 10 = 4 A."],
 "4 A",
 "Seri devrede yalnız tek direnci ya da ortalamayı eşdeğer almak. Kontrol: seri eşdeğer direnç **her dirençten büyüktür** ve akım buna göre küçülür.",
 "Seride toplanır, grafikte V bölü I.")

# 9. elektrik-05
a1 = Fr(8 - 2, 2); c_son = Fr(a1, 2)
assert a1 == 3 and c_son == Fr(3, 2)
kart("fiz-elektrik-05", "fiz|Elektrik", "Elektroskop ve yük paylaşımı",
 "Dokunmadan yaklaştırmada yük ayrışmasını, temasta yükün eşit paylaşımını ve Coulomb kuvvetini yorumlayabilmeni.",
 "Dokunmadan yaklaştırınca iletkenin **toplam yükü değişmez**; elektronlar yalnız yer değiştirir ve çubuk uzaklaşınca eski hâle döner. Özdeş iletken küreler dokununca toplam yük korunur ve eşit paylaşılır. Coulomb kuvveti yüklerin çarpımıyla doğru, **uzaklığın karesiyle ters** orantılıdır.",
 "q_son = (q₁ + q₂) / 2 · F = k·q₁·q₂ / d²",
 None,
 "Özdeş iletken A (+8q) ve B (−2q) küreleri dokundurulup ayrılıyor. Sonra B küresi yüksüz C küresine dokundurulup ayrılıyor. C'nin son yükü kaç q'dur?",
 ["A ile B: toplam +6q, eşit paylaşılır, her biri +3q olur.",
  "B (+3q) ile C (0) dokunur: toplam +3q.",
  "Eşit paylaşım: C'nin yükü +1,5q olur."],
 "+1,5q",
 "Yaklaştırılan çubuğun elektroskopa yük verdiğini sanmak. Dokunma yoksa toplam yük aynı kalır, yalnız yükler ayrışır; çubuk **uzaklaşınca yapraklar kapanır**.",
 "Dokunmadan yük ayrışır, dokununca paylaşılır.")

# 10. fizik bilimine giriş
kart("fiz-fizik-bilimine-02", "fiz|Fizik Bilimine Giriş", "Temel, türetilmiş, skaler, vektörel",
 "Niceliklerin temel mi türetilmiş mi, skaler mi vektörel mi olduğunu ayırt edebilmeni.",
 "**Temel nicelikler** başka niceliklerden türetilemez: uzunluk, kütle, zaman, sıcaklık, akım şiddeti. Türetilmiş niceliğin birimi temel birimlerin çarpımı ya da bölümüdür (hız, kuvvet, hacim). Skaler nicelik yalnız büyüklük, **vektörel nicelik büyüklük ve yön** taşır: yol ve sürat skaler; yer değiştirme, hız, kuvvet vektöreldir.",
 "Yol, sürat: skaler · Yer değiştirme, hız, kuvvet: vektörel",
 None,
 "Uzunluk, alan, akım şiddeti ve ivme niceliklerinden hangileri temeldir? Hangisi vektöreldir?",
 ["Alanın birimi m², ivmenin birimi m/s²'dir; ikisi de temel birimlerden türetilmiştir.",
  "Uzunluk (m) ve akım şiddeti (A) başka niceliklerden türetilemez: temeldir.",
  "Bunlardan yalnız ivmenin yönü vardır: vektöreldir."],
 "Uzunluk ve akım şiddeti temel; ivme vektörel",
 "Birimi tek sembolle yazılan kuvveti (N) temel saymak ya da sıcaklığı temel saymamak. Kontrol: birimi **başka birimlerle** yazabiliyorsan nicelik türetilmiştir.",
 "Birimi çarpım ya da bölümse türetilmiştir.")

# 11. hareket-01
R = math.hypot(17 - 12, 12)
assert R == 13
kart("fiz-hareket-ve-01", "fiz|Hareket ve Kuvvet", "Kuvvet türleri ve bileşke",
 "Temaslı ve temassız kuvvetleri, ağırlık ile kütleyi ayırt edip bileşke kuvveti bulabilmeni.",
 "Sürtünme, normal kuvvet ve ip gerilmesi **temaslı**; ağırlık, manyetik ve elektriksel kuvvet **temassızdır**. Ağırlık W = m·g newton ile, kütle kg ile ölçülür. Bileşkede aynı doğrultudaki zıt kuvvetler çıkarılır; birbirine dik bileşkelerde R = √(R₁² + R₂²) alınır.",
 "W = m·g · R = √(R₁² + R₂²)",
 None,
 "Bir cisme doğuya 17 N, batıya 12 N ve kuzeye 12 N'luk kuvvet etkiyor. Bileşke kuvvet kaç N'dur?",
 ["Doğu–batı doğrultusu: 17 − 12 = 5 N doğuya.",
  "Kuzey yönü: 12 N. Bu ikisi birbirine diktir.",
  "R = √(5² + 12²) = √169 = 13 N."],
 "13 N",
 "Ağırlığı temaslı sanmak ya da kütleyle aynı birimde ölçmek. Ağırlık Dünya'nın **uzaktan** çekimidir ve N ile ölçülür. Sürtünme ise yalnız temas eden yüzeyler arasında oluşur.",
 "Ağırlık uzaktan etkir, newtonla ölçülür.")

# 12. hareket-03
x0, xmax, xs = 2, 18, 10; dx = xs - x0; yol = (xmax - x0) + (xmax - xs)
assert (dx, yol) == (8, 24) and Fr(dx, 8) == 1 and Fr(yol, 8) == 3
kart("fiz-hareket-ve-03", "fiz|Hareket ve Kuvvet", "Yol, yer değiştirme, ortalama hız",
 "Konum–zaman verisinden yer değiştirmeyi ve yolu ayırıp ortalama hızı ve sürati bulabilmeni.",
 "**Yer değiştirme** = son konum − ilk konum (yönlüdür). Yol, gidilen bütün uzunlukların toplamıdır. Ortalama hız = yer değiştirme ÷ süre; ortalama sürat = yol ÷ süre. Aradaki hareketler hızı etkilemez: yalnız **ilk ve son konuma** bak.",
 "v_ort = Δx / Δt · sürat = yol / Δt",
 sk_konum(),
 "Grafikteki cisim 0–4 s'de 2 m'den 18 m'ye gidiyor, 4–8 s'de 10 m'ye dönüyor. 0–8 s için ortalama hızı ve ortalama sürati bulun.",
 ["Yer değiştirme: 10 − 2 = 8 m; ortalama hız = 8 ÷ 8 = 1 m/s.",
  "Yol: gidiş 18 − 2 = 16 m, dönüş 18 − 10 = 8 m, toplam 24 m.",
  "Ortalama sürat = 24 ÷ 8 = 3 m/s."],
 "Ortalama hız 1 m/s, ortalama sürat 3 m/s",
 "Yolu yer değiştirme yerine kullanmak ya da yer değiştirmeyi süreye bölmeyi unutmak. Geri dönüşlü harekette **yol, yer değiştirmeden büyüktür**; ortalama hız için son konuma bak.",
 "Ortalama hız: ilk ve son konum.")

# 13. ısı-sıcaklık-02
oran = Fr(3 * 1 * 20, 1 * 2 * 10)
assert oran == 3
kart("fiz-isi-sicaklik-02", "fiz|Isı, Sıcaklık ve Genleşme", "Genleşme ve bimetal",
 "Boyca uzamanın ilk boy, madde cinsi ve sıcaklık değişimiyle orantısını birlikte kullanabilmeni.",
 "Boyca uzama **ΔL = α·L₀·ΔT**'dir; üç büyüklükle doğru orantılıdır ve oranlar **çarpılır**. Yüzeyce genleşme katsayısı 2α, hacimce 3α'dır. Bimetal ısınınca **çok genleşen metal dışta** kalacak biçimde bükülür; soğutulunca ters yöne bükülür.",
 "ΔL = α · L₀ · ΔT",
 None,
 "K çubuğunun ilk boyu 2L, katsayısı α, sıcaklık artışı 10 °C'dir. M çubuğunun ilk boyu L, katsayısı 3α, sıcaklık artışı 20 °C'dir. M'nin uzaması K'ninkinin kaç katıdır?",
 ["Oranları yaz: katsayı 3, ilk boy 1/2, sıcaklık artışı 2.",
  "Oranlar çarpılır: 3 × 1/2 × 2 = 3.",
  "Doğrulama: M için 3·1·20 = 60, K için 1·2·10 = 20; 60 ÷ 20 = 3."],
 "3 kat",
 "Oranları toplamak ya da bir oranı (sıcaklık artışı gibi) atlamak. Üç oranı yan yana yaz ve **çarp**: katsayı oranı × ilk boy oranı × sıcaklık artışı oranı.",
 "Genleşme oranları toplanmaz, çarpılır.")

# 14. ısı-sıcaklık-04
q_su = 250 * 1 * 16; q_buz = 100 * 80; eriyen = Fr(q_su, 80); kalan = 100 - eriyen
assert (q_su, q_buz, eriyen, kalan) == (4000, 8000, 50, 50) and q_su < q_buz
kart("fiz-isi-sicaklik-04", "fiz|Isı, Sıcaklık ve Genleşme", "Hâl değişimi ve ısıl denge",
 "Karışımda buzun tamamen erip ermediğini ısıları karşılaştırarak yorumlayabilmeni.",
 "Saf maddede hâl değişimi sırasında **sıcaklık sabit kalır**; alınan ısı bağları gevşetir. Erime için Q = m·L, ısınma için Q = m·c·ΔT gerekir. Buz–su karışımında önce **buz tamamen erir mi** diye bak: suyun verebileceği ısıyı, buzu eritmek için gereken ısıyla karşılaştır.",
 "Q = m·c·ΔT · Q = m·L",
 None,
 "0 °C'de 100 g buz, 16 °C'de 250 g suya atılıyor (c = 1 cal/g·°C, L = 80 cal/g). Isıl dengede kaç g buz kalır ve sıcaklık kaç °C olur?",
 ["Su 0 °C'ye inerken verir: 250 × 1 × 16 = 4000 cal.",
  "Buzun tamamı erimek için 100 × 80 = 8000 cal ister; ısı yetmez.",
  "Eriyen buz: 4000 ÷ 80 = 50 g; kalan buz 50 g, sıcaklık 0 °C."],
 "50 g buz kalır; sıcaklık 0 °C",
 "Buzun tamamen eridiğini varsayıp son sıcaklığı hesaplamak ya da erime ısısını katmamak. Önce **ısıları karşılaştır**: su 0 °C'ye inerken verdiği ısı buzu eritmeye yetiyor mu?",
 "Önce buz erir mi, ona bak.")

# 15. madde-01
kart("fiz-madde-ve-01", "fiz|Madde ve Özellikleri", "Adezyon, kohezyon, kılcallık",
 "Sıvı yüzeyinin biçiminden adezyon ve kohezyon üstünlüğünü yorumlayabilmeni.",
 "**Adezyon** farklı cins, **kohezyon** aynı cins moleküller arasındaki çekimdir. Adezyon baskınsa sıvı kabı ıslatır, yüzey **çukur** olur ve sıvı dar borularda yükselir (kılcallık). Kohezyon baskınsa yüzey **tümsek** olur. Yüzey gerilimi, yüzey moleküllerinin içe çekilmesinden doğar; deterjan onu azaltır.",
 "Çukur yüzey: adezyon > kohezyon · Tümsek yüzey: kohezyon > adezyon",
 None,
 "Cam boruda alkolün yüzeyi çukur, cıvanın yüzeyi tümsek görünüyor. Hangisi camı ıslatır, hangisi kılcal boruda yükselir?",
 ["Alkol: yüzey çukur, yani adezyon baskın. Cam ıslanır.",
  "Cıva: yüzey tümsek, yani kohezyon baskın. Cam ıslanmaz.",
  "Kılcallıkta yalnız adezyonun baskın olduğu sıvı yükselir."],
 "Alkol ıslatır ve yükselir; cıva ıslatmaz ve yükselmez",
 "Çukur yüzeyi kohezyonun büyüklüğüne bağlamak. Çukur yüzey **adezyonun baskın** olduğunu, tümsek yüzey ise sıvının kendi molekülleri arasındaki çekimin baskın olduğunu gösterir.",
 "Çukursa adezyon, tümsekse kohezyon baskın.")

# 16. madde-03
o1, o2 = Fr(1, 2), Fr(1, 6)
assert o1 / o2 == 3
kart("fiz-madde-ve-03", "fiz|Madde ve Özellikleri", "Ortak özellik ve dayanıklılık",
 "Hangi özelliklerin maddeyi tanıttığını ve dayanıklılığın kesit alanı ile hacme bağlılığını kullanabilmeni.",
 "Kütle, hacim ve eylemsizlik **ortak** özelliktir; maddeyi tanıtmaz. **Özkütle**, erime ve kaynama sıcaklığı ayırt edicidir. Aynı maddeyi bulmak için kütle ÷ hacme bak; değerler tam eşit olmalı. Dayanıklılık kesit alanıyla doğru, hacimle ters orantılıdır; küpte oran **1 ÷ a**'dır.",
 "d = m / V · Dayanıklılık ∝ A / V",
 None,
 "Aynı maddeden yapılmış iki küpün ayrıtları 2 cm ve 6 cm'dir. Hangisi daha dayanıklıdır ve kaç katıdır?",
 ["Küpte kesit a², hacim a³; dayanıklılık oranı 1 ÷ a'dır.",
  "Küçük küp: 1/2; büyük küp: 1/6.",
  "(1/2) ÷ (1/6) = 3."],
 "2 cm'lik küp, 3 kat daha dayanıklı",
 "Kütlesi ya da hacmi eşit cisimleri aynı maddeden sanmak; ikisi de ortak özelliktir. Özkütleler **yaklaşık değil, tam eşit** olmalıdır.",
 "Aynı madde, aynı özkütle demektir.")

# 17. manyetizma-02
kart("fiz-manyetizma-02", "fiz|Manyetizma", "Mıknatıs ve manyetik alan",
 "Mıknatısın kutuplarını, alan çizgilerinin sıklığını ve mıknatıs bölününce olanları yorumlayabilmeni.",
 "Aynı cins kutuplar **iter**, farklı cins kutuplar çeker. Alan çizgileri mıknatısın dışında N'den S'ye gider; çizgiler **sıksa alan güçlüdür**. Pusulanın N ucu o noktadaki alan yönünü gösterir. Mıknatıs bölününce her parça yine **N ve S kutbu** olan bir mıknatıs olur; tek kutup yoktur.",
 "Dışarıda alan: N → S · Sık çizgi = güçlü alan",
 None,
 "Soldan sağa N–S dizili bir çubuk mıknatıs ortadan kesiliyor. İki parça kesim yüzeylerinden yan yana getirilirse birbirini çeker mi, iter mi?",
 ["Her parça yine mıknatıstır ve soldan sağa N–S dizilidir.",
  "Sol parçanın kesim ucu S, sağ parçanın kesim ucu N olur.",
  "Karşı karşıya gelen kutuplar farklı cinstir: birbirini çeker."],
 "Çeker",
 "Mıknatısı bölünce tek kutuplu parçalar oluştuğunu sanmak. Her parçada **N ve S birlikte** vardır. Alan şiddeti için çizgi sayısına değil, çizgilerin sıklığına bak.",
 "Mıknatısın tek kutbu olmaz.")

# 18. optik-02
sari = {"K", "Y"}; cyan = {"Y", "M"}; ort = sari & cyan
assert ort == {"Y"}
kart("fiz-optik-02", "fiz|Optik", "Işık, cisim rengi ve karışım",
 "Renkli ışık altında cismin görünen rengini ışığın ve cismin bileşenlerinden bulabilmeni.",
 "Ana ışık renkleri kırmızı, yeşil ve mavidir; sarı = kırmızı + yeşil, macenta = kırmızı + mavi, camgöbeği = yeşil + mavi. Cisim yalnız **kendi bileşenlerini yansıtır**, kalanını soğurur. Cisim, ışıkla ortak bileşeni yansıtıyorsa o renkte, yoksa **siyah** görünür. Prizmada mor en çok, kırmızı en az kırılır.",
 "Görünen renk = ışığın bileşenleri ∩ cismin yansıttıkları",
 None,
 "Sarı bir cisim camgöbeği ışıkla aydınlatılıyor. Cisim hangi renkte görünür?",
 ["Bileşenlere ayır: sarı = kırmızı + yeşil; camgöbeği = yeşil + mavi.",
  "Ortak bileşen yalnız yeşildir; cisim yeşili yansıtır.",
  "Kırmızı cisimde var ama ışıkta yok; mavi ışıkta var ama cisimde yok."],
 "Yeşil",
 "Ortak bileşeni atlamak: camgöbeği ışıktaki mavinin ya da sarı ışıktaki kırmızının yansıdığını unutmak. Işığı ve cismi **bileşenlerine ayır**, ortakları bul; yoksa siyah.",
 "Bileşenlere ayır, ortak olanı yansıt.")

# 19. optik-04
d0, kay = 3, 2; yeni = d0 + kay; arasi = 2 * yeni
assert (yeni, arasi) == (5, 10)
kart("fiz-optik-04", "fiz|Optik", "Düzlem aynada görüntü",
 "Görüntü uzaklığını ve yansıyan ışının yolunu yansıma yasasıyla bulabilmeni.",
 "Görüntü aynanın arkasında, aynadan cisim kadar uzaktadır. **Cisim–görüntü arası = 2 × aynaya uzaklık**. Yansımada gelme ve yansıma açıları **normalden** ölçülür ve eşittir. Ayna α kadar dönerse yansıyan ışın 2α döner. Boyunu tamamen görmek için ayna boyunun yarısı yeter.",
 "Cisim–görüntü arası = 2x · Ayna α döner → ışın 2α döner",
 sk_ayna(),
 "Cisim düzlem aynadan 3 m uzakta. Ayna cisimden 2 m uzaklaştırılırsa cisim ile görüntüsü arası kaç m olur?",
 ["Yeni uzaklık: 3 + 2 = 5 m.",
  "Görüntü de aynanın arkasında 5 m uzaktadır.",
  "Cisim–görüntü arası: 2 × 5 = 10 m."],
 "10 m",
 "Cismin yeni aynaya uzaklığını cevap sanmak ya da aynanın kaymasını hesaba katmamak. Önce **yeni uzaklığı** bul, sonra ikiyle çarp; açıyı da yüzeyden değil normalden ölç.",
 "Cisim–görüntü arası uzaklığın iki katıdır.")

# 20. optik-06
f_, d_ = 10, 15
assert f_ < d_ < 2 * f_ and 25 > 2 * f_
kart("fiz-optik-06", "fiz|Optik", "Mercekte görüntü ve göz kusuru",
 "Cismin konumuna göre görüntünün yerini, türünü ve boyunu ve göz kusuru gözlüğünü belirleyebilmeni.",
 "İnce kenarlı mercekte cisim **2F'nin ötesindeyse** görüntü gerçek, ters, küçüktür; F–2F arasındaysa gerçek, ters, büyüktür; **F'nin içindeyse** sanal, düz, büyüktür. Kalın kenarlı mercekte görüntü hep sanal, düz, küçüktür. Miyop kalın, hipermetrop ince kenarlı mercek kullanır.",
 "Cisim yaklaşırsa gerçek görüntü büyür ve uzaklaşır",
 sk_mercek(),
 "Odak uzaklığı 10 cm olan ince kenarlı merceğin 15 cm önüne cisim konuyor. Görüntünün özelliği nedir? Cisim 25 cm'e konursa ne değişir?",
 ["F = 10 cm, 2F = 20 cm. Cisim 15 cm'de: F ile 2F arasında.",
  "Görüntü 2F'nin ötesinde; gerçek, ters ve büyüktür.",
  "Cisim 25 cm'de olsaydı 2F'nin ötesinde olurdu: görüntü gerçek, ters ve küçük."],
 "Gerçek, ters, büyük; 25 cm'de küçük olur",
 "F'nin içindeki cismin görüntüsünü küçük sanmak ya da sanal görüntünün düz olduğunu atlamak. **Sanal görüntü hep düzdür**; gerçek görüntü hep terstir.",
 "Gerçek ters, sanal düz.")

# 21. kaldırma-02
bk = Fr(9, 10) / Fr(12, 10); bs = Fr(9, 10) / 1
assert (bk, bs) == (Fr(3, 4), Fr(9, 10)) and bs > bk
kart("fiz-sivilarin-kaldirma-02", "fiz|Sıvıların Kaldırma Kuvveti", "Yüzme, askıda kalma, batma",
 "Özkütleleri karşılaştırarak yüzme, askıda kalma ve batmayı; gemi, denizaltı ve balonda kuvvet dengesini yorumlayabilmeni.",
 "d_cisim < d_sıvı ise cisim **yüzer**; eşitse **askıda kalır**; büyükse **batar**. Yüzen ve askıdaki cisimde kaldırma kuvveti ağırlığa eşittir; batan cisimde ağırlıktan küçüktür. Yüzen cismin batan kesri d_cisim ÷ d_sıvı'dır. Sıvı özkütlesi artarsa batan kesir küçülür.",
 "Yüzer: F_k = G · V_batan / V = d_cisim / d_sıvı",
 None,
 "Özkütlesi 0,9 g/cm³ olan bir cisim 1,2 g/cm³'lük tuzlu suda yüzüyor. Hacminin kaçı batar? Aynı cisim saf suya (1 g/cm³) konursa batan kesir nasıl değişir?",
 ["Tuzlu suda: 0,9 ÷ 1,2 = 3/4 batar.",
  "Saf suda: 0,9 ÷ 1 = 9/10 batar.",
  "Sıvı özkütlesi azaldı, batan kesir arttı."],
 "3/4; saf suda 9/10'a çıkar",
 "Yüzmeyle askıda kalmayı aynı sanmak ve kaldırma kuvvetinin her durumda ağırlığa eşit olduğunu düşünmek. Batan cismin kaldırma kuvveti **ağırlığından küçüktür**; askıdaki cisim tamamen batmıştır.",
 "Yüzen cismin özkütlesi sıvıdan küçüktür.")

# 22. kaldırma-04
dc = 1000 * Fr(5, 8)
assert dc == 625
kart("fiz-sivilarin-kaldirma-04", "fiz|Sıvıların Kaldırma Kuvveti", "Yüzen cismin batan hacmi",
 "Yüzen, askıdaki ve batan cisimlerde batan hacmi, özkütleyi ve kaldırma kuvvetini hesaplayabilmeni.",
 "Yüzen cisimde **ağırlık = kaldırma kuvveti**: d_cisim·V = d_sıvı·V_batan. Düzgün cisimde batan hacim oranı batan yükseklik oranına eşittir. Dinamometre okuması = ağırlık − kaldırma kuvveti; tamamen batınca kaldırma kuvveti derinlikle **değişmez**. Üstüne yük konursa batan hacim artar.",
 "V_batan / V = d_cisim / d_sıvı",
 sk_yuzen(),
 "Düzgün bir silindir suda (1000 kg/m³) yüzüyor ve yüksekliğinin 3/8'i su dışında kalıyor. Silindirin özkütlesi kaç kg/m³'tür?",
 ["Batan kesir: 1 − 3/8 = 5/8.",
  "Yüzen cisimde batan kesir = d_cisim ÷ d_sıvı.",
  "d_cisim = 1000 × 5/8 = 625 kg/m³."],
 "625 kg/m³",
 "Dışarıda kalan oranı batan oran sanmak, özkütleleri toplamak ya da oranı ters yazmak. Sonucu bulunca kontrol et: **yüzen cismin özkütlesi sıvıdan küçük** olmalı.",
 "Yüzende batan oran, özkütle oranıdır.")

# 23. iş-güç-02
w = Fr(1, 2) * 2 * 4 + 4 * 4 + Fr(1, 2) * 2 * 4
assert w == 24
kart("fiz-is-guc-02", "fiz|İş, Güç ve Enerji", "İş ve kuvvet–yol grafiği",
 "Kuvvet–yol grafiğinin altındaki alandan işi bulabilmeni ve kuvvetin iş yapmadığı durumları ayırt edebilmeni.",
 "İş W = F·x'tir; kuvvet **yer değiştirme doğrultusundayken** hesaplanır. Kuvvet–yol grafiğinde **eğrinin altındaki alan** işi verir. Yer değiştirme sıfırsa ya da kuvvet yola diktirse kuvvet iş yapmaz. Bölgeli yolda her bölgenin işini ayrı hesaplayıp topla.",
 "W = F · x = grafiğin altındaki alan",
 sk_is(),
 "Grafikte kuvvet 0–2 m'de 0'dan 4 N'a düzgün artıyor, 2–6 m'de 4 N sabit kalıyor, 6–8 m'de 0'a düzgün azalıyor. Kuvvetin 8 m'de yaptığı iş kaç J'dür?",
 ["0–2 m üçgen: ½ × 2 × 4 = 4 J.",
  "2–6 m dikdörtgen: 4 × 4 = 16 J.",
  "6–8 m üçgen: ½ × 2 × 4 = 4 J; toplam 4 + 16 + 4 = 24 J."],
 "24 J",
 "Kuvvet uygulamayı iş yapmakla karıştırmak. Duvarı itmek ya da yatay yolda yük taşırken **yukarı kuvvet** iş yapmaz. Grafikte iş, değerin kendisi değil alanıdır.",
 "İş, grafiğin altındaki alandır.")

# 24. iş-güç-04
oran_ek = Fr(2 * 1, 1 * 9)
assert oran_ek == Fr(2, 9)
kart("fiz-is-guc-04", "fiz|İş, Güç ve Enerji", "Kinetik ve potansiyel enerji",
 "Kütle ve hız oranlarından kinetik enerji oranını, yükseklikten potansiyel enerjiyi karşılaştırabilmeni.",
 "E_k = ½·m·v² ve E_p = m·g·h'dir. Hız **2 katına çıkarsa** kinetik enerji 4 katına çıkar. İki cismin oranı: kütle oranı × **(hız oranı)²**. Potansiyel enerji referans seviyesine göre bulunur. Kinetik enerji–yol grafiğinde eğim bileşke kuvveti verir: F_net·x = ΔE_k.",
 "E_k = ½mv² · E_p = mgh · F_net = ΔE_k / x",
 None,
 "K cisminin kütlesi 2m, hızı v; L cisminin kütlesi m, hızı 3v'dir. E_K ÷ E_L oranı kaçtır?",
 ["Kütle oranı: 2m ÷ m = 2.",
  "Hız oranı: v ÷ 3v = 1/3; karesi 1/9.",
  "Oran: 2 × 1/9 = 2/9."],
 "2/9",
 "Yalnız kütle oranını ya da yalnız hız oranını almak. Hız **karesiyle** girer: hız 3 katına çıkarsa kinetik enerji 9 katına çıkar.",
 "Kinetik enerji hızın karesiyle büyür.")

# ---------------- DOĞRULAMA ----------------
ids_girdi = re.findall(r'^### (\S+) \|', open('/tmp/kor/kart/parti/p04.txt', encoding='utf-8').read(), re.M)
ids_cikti = [c["id"] for c in K]
assert sorted(ids_girdi) == sorted(ids_cikti) and len(set(ids_cikti)) == len(ids_cikti), (set(ids_girdi) ^ set(ids_cikti))

def kel(s):
    return len(s.replace('**', '').split())
ZOR = ["id", "k", "baslik", "olcer", "kural", "ornek", "hata", "akilda"]
for c in K:
    if c.get("kapsamDisi") or c.get("birlesti"):
        continue
    for z in ZOR:
        assert c.get(z), (c["id"], z)
    o = c["ornek"]
    assert o["soru"] and o["cevap"] and 2 <= len(o["adimlar"]) <= 4, c["id"]
    assert kel(c["baslik"]) <= 6, (c["id"], "baslik", kel(c["baslik"]))
    assert kel(c["olcer"]) <= 25 and not c["olcer"].startswith("Bu soru"), (c["id"], "olcer")
    assert kel(c["kural"]) <= 60, (c["id"], "kural", kel(c["kural"]))
    assert kel(c["hata"]) <= 40, (c["id"], "hata", kel(c["hata"]))
    assert kel(c["akilda"]) <= 8 and '"' not in c["akilda"] and '“' not in c["akilda"], (c["id"], "akilda")
    assert "**" in c["kural"], c["id"]
    assert c["formul"] is None or len(c["formul"]) > 0
    if c["sekil"]:
        assert len(c["sekil"].encode()) <= 25000, (c["id"], len(c["sekil"]))

json.dump(K, open('/home/claude/zekacademy-app/havuz/tekrar/kart-p04.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
import os
os.makedirs('/tmp/kor/kart/png', exist_ok=True)
for c in K:
    if c.get("sekil"):
        open(f'/tmp/kor/kart/p04-{c["id"]}.svg', 'w').write(c["sekil"])
print(len(K), "kart;", sum(1 for c in K if c.get("sekil")), "şekilli")
