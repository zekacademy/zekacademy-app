import sys, json, re, itertools
from fractions import Fraction as F
from math import comb
sys.path.insert(0,'/home/claude/zekacademy-app/havuz')
from cizim import tikz_svg

IDS=[l.split('|')[0].replace('###','').strip() for l in open('/tmp/kor/kart/parti/p10.txt') if l.startswith('###')]
KART=[]
def K(id,k,baslik,olcer,kural,formul,sekil,soru,adimlar,cevap,hata,akilda):
    KART.append(dict(id=id,k=k,baslik=baslik,olcer=olcer,kural=kural,formul=formul,sekil=sekil,
        ornek=dict(soru=soru,adimlar=adimlar,cevap=cevap),hata=hata,akilda=akilda))
S=lambda g: tikz_svg(g)

# ---------- FONKSİYONLAR ----------
# 01
f=lambda x:3*x-5
assert (3*7-5)==16 and (16+5)//3==7
K('matd-fonksiyonlar-01','matd|Fonksiyonlar','Bileşke ve ters fonksiyon',
 'Art arda uygulanan fonksiyonları doğru sırayla çalıştırıp çıkıştan girişe geri dönebilmeni.',
 '**Bileşkede** (f ∘ g)(x) = f(g(x)) yazılır: önce g, sonra f çalışır. Makine şemasında soldaki makine önce çalışır. **Ters** bulurken çıkıştan girişe gidilir: makineler sondan başa, her biri kendi tersiyle çalıştırılır.',
 '(f ∘ g)(x) = f(g(x)) · ters: sondan başa, işlemin tersiyle',None,
 'x → ×3 → −5 makinesinin çıkışı 16 ise giriş x kaçtır?',
 ['Makineleri sondan başa doğru ele al: son makine −5 idi, tersi +5. 16 + 5 = 21.','Önceki makine ×3 idi, tersi ÷3. 21 ÷ 3 = 7.','Kontrol: 7 × 3 − 5 = 16 olur.'],
 'x = 7',
 'Makineleri şemadaki sırayla (baştan sona) tersleyip sırayı karıştırmak, ya da yalnız tek makineyi uygulamak. Önce kendine hangi makinenin ilk çalıştığını sor.',
 'Ok yönü sırayı verir, ters sondan başlar')
# 02
a=F(10-4,3-1); b=4-a*1; assert a==3 and b==1 and a*5+b==16
K('matd-fonksiyonlar-02','matd|Fonksiyonlar','Doğrusal ve parçalı fonksiyon',
 'Grafikteki ya da tablodaki bilgiden fonksiyonun kuralını kurup görünmeyen değerleri hesaplayabilmeni.',
 'Doğrusal fonksiyonda f(x) = ax + b yazılır. İşaretli iki noktadan **eğim** a = (y₂ − y₁)/(x₂ − x₁) bulunur, sonra b bir noktadan hesaplanır. f(x) = k denkleminde **y = k doğrusu** grafiği kaç yerde keserse o kadar çözüm vardır; içi boş nokta sayılmaz.',
 'a = (y₂ − y₁)/(x₂ − x₁) · b = y₁ − a·x₁',None,
 'Doğrusal bir f fonksiyonunun grafiği (1, 4) ve (3, 10) noktalarından geçiyor. f(5) kaçtır?',
 ['Eğim: a = (10 − 4)/(3 − 1) = 3.','(1, 4) noktasından 4 = 3·1 + b, yani b = 1. Kural f(x) = 3x + 1.','f(5) = 3·5 + 1 = 16.'],
 'f(5) = 16',
 'Sabit terimi 0 almak (kuralı ax sanmak) ya da bir noktanın y değerini doğrudan b yapmak. Kuralı yazınca iki noktayı da yerine koyup sına.',
 'Önce kuralı yaz, sonra değer hesapla')
# 03 şekil
sk=S(r'''\begin{tikzpicture}
\draw (0,0) ellipse (0.8 and 1.4); \draw (3.6,0) ellipse (0.8 and 1.4);
\node at (0,1.8) {A}; \node at (3.6,1.8) {B};
\node (a1) at (0,0.8) {1}; \node (a2) at (0,0) {2}; \node (a3) at (0,-0.8) {3};
\node (b1) at (3.6,0.8) {p}; \node (b2) at (3.6,0) {q}; \node (b3) at (3.6,-0.8) {r};
\draw[->] (0.3,0.8)--(3.3,0); \draw[->] (0.3,0)--(3.3,-0.8);
\draw[->,dashed,vurgu,thick] (0.3,-0.8)--(3.3,0.8);
\end{tikzpicture}''')
K('matd-fonksiyonlar-03','matd|Fonksiyonlar','Fonksiyon, birebir ve örten',
 'Ok şemasından fonksiyon olup olmadığını ayırt edip birebir ve örten eşlemede eksik oku bulabilmeni.',
 'Şemada tanım kümesinin **her elemanından tam bir ok** çıkarsa fonksiyondur. Birebir ve örten fonksiyonda değer kümesinin **her elemanına da tam bir ok** gelir. Gösterilmeyen eleman, kalan elemanla eşlenir.',
 'Her elemandan 1 ok çıkar · birebir-örtenle her elemana 1 ok gelir',sk,
 'A = {1, 2, 3}, B = {p, q, r} ve f: A → B birebir ve örten. f(1) = q ve f(2) = r ise f(3) kaçtır?',
 ['q ve r değer kümesinde başka okla eşlendi.','Birebir ve örten olduğundan p tam bir ok alır.','Kalan eleman 3, kalan elemanla eşlenir.'],
 'f(3) = p',
 'Kalan elemanı değer kümesinin ilk ya da son elemanı sanıp zaten eşlenmiş elemanı tekrar kullanmak. Hangi elemanların kullanıldığını işaretle.',
 'Her eleman bir kez kullanılır')
# 04
assert 4*5-3==17 and 4*6-3==21
K('matd-fonksiyonlar-04','matd|Fonksiyonlar','Fonksiyonda değer bulma',
 'Kuralda, tabloda ve grafikte f(a) değerini okuyup bileşke denklemlerinde bilinmeyeni bulabilmeni.',
 'f(a) için kuralda x gördüğün her yere a yazılır; grafikte x = a noktasının **y koordinatı** okunur. f(a) = c ise ters yönde a = f⁻¹(c) olur. Bileşkede **içteki fonksiyon önce** çalışır.',
 'f(a) = c ⇒ a = f⁻¹(c)',None,
 'f(x) = 4x − 3 için f(a) = 17 ise f(a + 1) kaçtır?',
 ['f(a) = 4a − 3 = 17 ise 4a = 20, a = 5.','a + 1 = 6 olur.','f(6) = 4·6 − 3 = 21.'],
 'f(a + 1) = 21',
 'a bulunca durup f(a) değerini cevap sanmak, ya da f(a + 1) yerine f(a) + 1 hesaplamak. Soruda hangi girdinin istendiğini yeniden oku.',
 'Önce bilinmeyeni bul, sonra istenen girdiyi yaz')

# ---------- KÜMELER ----------
sa,sb_u,si=5,9,3; sb=sb_u-sa+si; assert sb==7 and sa*sb==35
K('matd-kumelerkartezyen-carpim-01','matd|Kümeler-Kartezyen Çarpım','Kartezyen çarpım',
 'Eleman sayılarını birleşim ve kesişimden bulup Kartezyen çarpımın eleman sayısına ulaşabilmeni.',
 'A × B, ilk bileşeni A’dan, ikinci bileşeni B’den alınan **sıralı ikililerin** kümesidir. Eleman sayısı s(A × B) = s(A) · s(B) olur. Birleşimde kesişim iki kez sayıldığından **bir kez çıkarılır**. A × B ile B × A aynı küme değildir.',
 's(A × B) = s(A) · s(B) · s(A ∪ B) = s(A) + s(B) − s(A ∩ B)',None,
 's(A) = 5, s(A ∪ B) = 9, s(A ∩ B) = 3 ise s(A × B) kaçtır?',
 ['s(A ∪ B) = s(A) + s(B) − s(A ∩ B) ⇒ 9 = 5 + s(B) − 3.','Buradan s(B) = 7.','s(A × B) = 5 · 7 = 35.'],
 '35',
 'Önce B’nin eleman sayısını bulmadan birleşimin sayısıyla çarpmak, ya da çarpımda toplama yapmak. Çarpım istenmişse son adım her zaman çarpmadır.',
 'Önce s(B) bul, sonra çarp')
assert 2**(7-3)==16
K('matd-kumelerkartezyen-carpim-02','matd|Kümeler-Kartezyen Çarpım','Alt küme sayısı',
 'Koşullu alt küme sayısını kesin olan elemanları ayırıp kalan elemanlarla 2 üzeri k ile bulabilmeni.',
 'n elemanlı kümenin **2ⁿ alt kümesi** vardır; boş küme ve kümenin kendisi dahildir. Alt kümede mutlaka olan ve asla olmayan elemanları çıkar. Geriye kalan **serbest elemanların** her biri için var/yok olmak üzere 2 seçenek vardır.',
 'Serbest eleman sayısı k ise alt küme sayısı 2ᵏ',None,
 'A = {a, b, c, d, e, f, g} kümesinin a ve b’yi içeren, c’yi içermeyen kaç alt kümesi vardır?',
 ['a ve b kesin var, c kesin yok: 3 eleman belirli.','Serbest eleman sayısı 7 − 3 = 4 (d, e, f, g).','Alt küme sayısı 2⁴ = 16.'],
 '16',
 'Serbest eleman sayısını yanlış saymak ya da koşulu sağlayan kümelerden boş kümeyi çıkarmak. Kesin bulunan eleman zaten kümededir, boş küme olamaz.',
 'Belirliyi çıkar, kalanla 2 üzeri k')
# 03 Venn
sk=S(r'''\begin{tikzpicture}
\draw (-1.9,-1.9) rectangle (3.7,1.9);
\draw (0,0) circle (1.4); \draw (1.8,0) circle (1.4);
\node at (-0.6,0) {16}; \node at (0.9,0) {9}; \node at (2.4,0) {9}; \node at (3.2,-1.5) {6};
\node at (-0.6,1.65) {Futbol}; \node at (2.4,1.65) {Basket};
\end{tikzpicture}''')
assert 25+18-9==34 and 40-6==34 and 25-9==16 and 18-9==9 and 16+9+9+6==40
K('matd-kumelerkartezyen-carpim-03','matd|Kümeler-Kartezyen Çarpım','Venn şeması ve sayma',
 'İki kümeli problemlerde bölgeleri tek tek yazıp toplamdan bilinmeyen sayıyı bulabilmeni.',
 'Her bölge hangi kümelerde olup hangilerinde olmadığıyla okunur. **Kesişimi** bulmadan yalnız-bir-küme sayısını yazma. Toplam = yalnız A + yalnız B + **kesişim** + hiçbiri. Kesir verildiyse bütünü x cinsinden yaz.',
 's(A ∪ B) = s(A) + s(B) − s(A ∩ B)',sk,
 '40 kişilik sınıfta 25 kişi futbol, 18 kişi basketbol oynuyor, 6 kişi hiçbirini oynamıyor. Yalnız futbol oynayan kaç kişi var?',
 ['En az birini oynayan: 40 − 6 = 34.','34 = 25 + 18 − x ⇒ kesişim x = 9.','Yalnız futbol: 25 − 9 = 16.'],
 '16 kişi',
 'Kesişimi iki kez saymak ya da yalnız bir kümeyi sorarken kümenin tamamını yazmak. Şemada her bölgeye ayrı sayı yaz, toplamı kontrol et.',
 'Önce kesişim, sonra yalnız bölgeler')
# 04
A={1,2,3,5,8}; B={2,5,6,9}; assert sum(A-B)==12 and sorted(A-B)==[1,3,8]
sk=S(r'''\begin{tikzpicture}
\draw (0,0) circle (1.4); \draw (1.8,0) circle (1.4);
\node at (-0.6,0) {1, 3, 8}; \node at (0.9,0) {2, 5}; \node at (2.4,0) {6, 9};
\node at (-0.6,1.7) {A}; \node at (2.4,1.7) {B};
\end{tikzpicture}''')
K('matd-kumelerkartezyen-carpim-04','matd|Kümeler-Kartezyen Çarpım','Küme işlemleri ve fark',
 'Birleşim, kesişim ve fark işlemlerini şemada bölgelere ayırıp doğru elemanları seçebilmeni.',
 'A ∪ B en az birinde olanlar, A ∩ B ikisinde birden olanlardır. **A \\ B**, A’da olup B’de olmayan elemanlardır; kesişimdeki elemanlar **içermez**. İç içe kümelerde A ⊂ B ise s(B \\ A) = s(B) − s(A) olur.',
 'A \\ B = A’nın yalnız kendine ait bölgesi',sk,
 'A = {1, 2, 3, 5, 8} ve B = {2, 5, 6, 9} ise A \\ B kümesinin elemanları toplamı kaçtır?',
 ['Ortak elemanlar 2 ve 5, bunlar A \\ B’de yer almaz.','A \\ B = {1, 3, 8}.','Toplam 1 + 3 + 8 = 12.'],
 '12',
 'B \\ A’yı hesaplamak ya da kesişimdeki elemanları da fark kümesine katmak. Fark yönüne dikkat et: soldaki küme kalır.',
 'Fark kümesi kesişimi içermez')

# ---------- MANTIK ----------
assert not all(x%2==0 for x in {2,4,6,9}) 
Bk={3,5,8,11}; asal=lambda n:n>1 and all(n%d for d in range(2,n))
assert not all(asal(x) for x in Bk) and any(not asal(x) for x in Bk)
K('matd-mantik-01','matd|Mantık','Niceleyiciler ve olumsuzu',
 'Kümenin elemanlarını tarayıp “her” ve “en az bir” önermelerinin doğruluğunu ve olumsuzunu belirleyebilmeni.',
 '“Her” (∀) önermesi bütün elemanlar için doğruysa doğrudur; **tek karşı örnek** onu yanlış yapar. “En az bir” (∃) önermesi için **tek örnek** yeter. Olumsuzunda ∀ ile ∃ yer değiştirir ve koşul olumsuz olur.',
 '(∀x) p(x) değili (∃x) p(x)′ · (∃x) p(x) değili (∀x) p(x)′',None,
 'B = {3, 5, 8, 11} için “Her x ∈ B için x asaldır” önermesi doğru mudur? Olumsuzu doğru mudur?',
 ['Elemanları tara: 3, 5, 11 asal; 8 asal değil.','8 bir karşı örnek, önerme yanlıştır.','Olumsuzu “en az bir x ∈ B için x asal değildir”: 8 buna uyar, doğrudur.'],
 'Önerme yanlış, olumsuzu doğru',
 'Bir örnek bulup “her” önermesini doğru saymak ya da olumsuzunda yalnız ∀’yı ∃ yapıp koşulu olumsuz yapmamak. Tüm elemanları tek tek dene.',
 'Her için bir karşı örnek yeter')
K('matd-mantik-02','matd|Mantık','Koşullu önerme ve denkleri',
 'p ⇒ q ile her durumda aynı değeri veren ifadeyi karşıt, ters ve karşıt tersten ayırabilmeni.',
 'p ⇒ q yalnız p = 1, q = 0 iken yanlıştır. Denk ifadeleri **karşıt tersi** q′ ⇒ p′ ve **p′ ∨ q**’dur. Karşıtı (q ⇒ p) ve tersi (p′ ⇒ q′) p ⇒ q ile **denk değildir**.',
 'p ⇒ q ≡ q′ ⇒ p′ ≡ p′ ∨ q',None,
 '“Bir sayı 10’a bölünürse 5’e bölünür” önermesinin karşıt tersi nedir? Karşıtı neden denk değildir?',
 ['p: sayı 10’a bölünür, q: sayı 5’e bölünür.','Karşıt ters q′ ⇒ p′: “5’e bölünmeyen sayı 10’a bölünmez.”','Karşıt q ⇒ p: “5’e bölünen sayı 10’a bölünür” yanlıştır, çünkü 15 bölünmez.'],
 'Karşıt tersi denktir, karşıtı değildir',
 'Karşıtı ya da tersi denk sanmak; “ya da” ile kurulu p′ ∨ q biçimini ise denk olarak görmemek. Karşıt örnek bulmaya çalış.',
 'Yalnız karşıt ters ve p′ ∨ q denk')
# 03 devre
cnt=sum(1 for p,q,r in itertools.product([0,1],repeat=3) if p and (q or r)); assert cnt==3
sk=S(r'''\begin{tikzpicture}
\draw (0,0) circle (0.06); \draw (0.06,0)--(0.6,0);
\node[draw,minimum width=0.8cm,minimum height=0.6cm] at (1,0) {$p$};
\draw (1.4,0)--(2.1,0); \draw (2.1,0.7)--(2.1,-0.7);
\draw (2.1,0.7)--(2.6,0.7); \node[draw,minimum width=0.8cm,minimum height=0.6cm] at (3,0.7) {$q$}; \draw (3.4,0.7)--(3.9,0.7);
\draw (2.1,-0.7)--(2.6,-0.7); \node[draw,minimum width=0.8cm,minimum height=0.6cm] at (3,-0.7) {$r$}; \draw (3.4,-0.7)--(3.9,-0.7);
\draw (3.9,0.7)--(3.9,-0.7); \draw (3.9,0)--(4.5,0); \draw (4.56,0) circle (0.06);
\end{tikzpicture}''')
K('matd-mantik-03','matd|Mantık','Anahtarlı devre ve sadeleştirme',
 'Anahtarlı devrenin ifadesini yazıp akımın geçtiği durumları saymayı ve ifadeyi sadeleştirmeyi bilmeni.',
 '**Seri** bağlı anahtarlar “ve” (∧), **paralel** bağlı anahtarlar “veya” (∨) ile gösterilir. Anahtar kapalıysa önerme 1, açıksa 0’dır. Akım, devre ifadesi 1 olunca geçer. İfadeler çarpanlara ayrılarak ya da tabloyla sadeleştirilir.',
 'seri = ∧ · paralel = ∨ · (a ∧ b) ∨ (a ∧ c) ≡ a ∧ (b ∨ c)',sk,
 'p anahtarı, paralel bağlı q ve r anahtarlarıyla seri bağlıdır. Üç anahtarın kaç durumunda akım geçer?',
 ['Devrenin ifadesi p ∧ (q ∨ r).','p kapalı (1) olmalı; q ∨ r ise 4 durumdan 3’ünde 1’dir.','1 · 3 = 3 durum.'],
 '3 durum',
 'Hepsini seri sanıp yalnız tüm anahtarların kapalı olduğu durumu saymak ya da geçmeyen durumları yazmak. Önce ifadeyi yaz, sonra say.',
 'Önce ifadeyi yaz, sonra durumları say')
tk=[x for x in range(1,9) if (not asal(x)) or x%2==1]; assert tk==[1,3,4,5,6,7,8] and len(tk)==7
K('matd-mantik-04','matd|Mantık','Açık önerme ve doğruluk kümesi',
 'Koşullu açık önermenin doğruluk kümesini yanlış yapan değerleri ayırarak bulabilmeni.',
 'x’e değer verilince doğru ya da yanlış olan ifade **açık önerme**dir; onu doğru yapan değerlerin kümesi **doğruluk kümesi**dir. p ⇒ q yalnız p doğru, q yanlış iken yanlıştır. Doğruluk kümesi, bu durumu yaratan değerlerin tümleyenidir.',
 'p ⇒ q yalnız p = 1 ve q = 0 iken 0',None,
 'x ∈ {1, 2, …, 8} için “x asal ⇒ x tek” açık önermesinin doğruluk kümesinin kaç elemanı vardır?',
 ['Yanlış yapan değer: x asal ama çift olmalı. Bu yalnız x = 2’dir.','Geri kalan 8 − 1 = 7 değer önermeyi doğru yapar.','Doğruluk kümesi {1, 3, 4, 5, 6, 7, 8}.'],
 '7 eleman',
 '⇒ yerine ∧ ya da ∨ kullanmak, ya da yalnız p’nin doğru olduğu değerleri saymak. Önce önermeyi yanlış yapan tek durumu bul.',
 'Yanlış yapanı bul, tümleyenini al')
sol=[q for q in (0,1) if (not 1 or not q)==1]; assert sol==[0]
K('matd-mantik-05','matd|Mantık','Önerme ve doğruluk değeri',
 'Bileşik önermenin sonucundan p, q, r değerlerini satır satır ve parçaları ayırarak bulabilmeni.',
 'Doğruluk değeri verilebilen cümle önermedir; soru, emir ve x’e bağlı ifade önerme değildir. Bileşik önermede **içteki parçadan** başla. p ∧ q yalnız ikisi 1 iken 1, p ∨ q yalnız ikisi 0 iken 0’dır. **Gizli değere** 1 ve 0 yazıp sınayabilirsin.',
 'p ⇒ q yalnız (1, 0) iken 0 · p ⇔ q aynı değerde iken 1',None,
 'p = 1 ve (p ⇒ q′) = 1 ise q’nun doğruluk değeri nedir?',
 ['p = 1 iken p ⇒ q′ yalnız q′ = 1 ise 1 olur.','q′ = 1 demek q = 0 demektir.','Kontrol: 1 ⇒ 1 = 1, koşul sağlanır.'],
 'q = 0',
 'q′ yerine q almak (olumsuzu atlamak) ya da ⇒ yönünü ters okumak. Her satırı ayrı çöz ve olumsuzu ayrı bir adım yaz.',
 'Her satırı ayrı çöz')

# ---------- OLASILIK ----------
assert 120+90+150==360 and F(90+150,360)==F(2,3)
sk=S(r'''\begin{tikzpicture}
\fill[vurgu!25] (0,0)--(120:1.6) arc(120:210:1.6)--cycle;
\fill[vurgu!25] (0,0)--(210:1.6) arc(210:360:1.6)--cycle;
\draw (0,0) circle (1.6);
\draw (0,0)--(0:1.6); \draw (0,0)--(120:1.6); \draw (0,0)--(210:1.6);
\node at (60:0.9) {120°}; \node at (165:0.95) {90°}; \node at (285:0.95) {150°};
\end{tikzpicture}''')
K('matd-olasilik-01','matd|Olasılık','Geometrik olasılık',
 'Şekildeki ya da çarktaki bölgenin ölçüsünü toplam ölçüye oranlayarak olasılığı bulabilmeni.',
 'Rastgele bir noktanın bir bölgede olma olasılığı, bölgenin **ölçüsünün** (alan ya da merkez açı) tüm bölgenin ölçüsüne oranıdır. Dilimler eşit olmayabilir: önemli olan dilim sayısı değil **ölçüsüdür**. Birlikte olamayan bölgeler için ölçüler toplanır.',
 'P = istenen bölgenin ölçüsü / toplam ölçü',sk,
 'Çarkın dilimleri 120°, 90° ve 150°’dir. İğnenin 90° ya da 150°’lik dilimde durma olasılığı kaçtır?',
 ['Toplam açı 360°.','İstenen dilimler: 90° + 150° = 240°.','P = 240/360 = 2/3.'],
 '2/3',
 'Dilimleri eşit olasılıklı sanıp dilim sayısına oranlamak ya da istenmeyen dilimin olasılığını bulmak. Her dilimin ölçüsünü yaz.',
 'Dilim sayısına değil ölçüsüne bak')
p=F(3,4);q=F(2,5); assert 1-(1-p)*(1-q)==F(17,20) and F(3,10)+F(9,20)+F(1,10)+F(3,20)==1
sk=S(r'''\begin{tikzpicture}
\node (r) at (0,0) {};
\node (a1) at (2.4,1.2) {Ali İ}; \node (a2) at (2.4,-1.2) {Ali K};
\draw (r)--(a1) node[midway,above,sloped]{3/4}; \draw (r)--(a2) node[midway,below,sloped]{1/4};
\node (l1) at (5.4,1.8) {3/10}; \node (l2) at (5.4,0.6) {9/20};
\node (l3) at (5.4,-0.6) {1/10}; \node[vurgu] (l4) at (5.4,-1.8) {3/20};
\draw (a1)--(l1) node[midway,above,sloped]{2/5}; \draw (a1)--(l2) node[midway,below,sloped]{3/5};
\draw (a2)--(l3) node[midway,above,sloped]{2/5}; \draw (a2)--(l4) node[midway,below,sloped]{3/5};
\end{tikzpicture}''')
K('matd-olasilik-02','matd|Olasılık','Bağımsız ve art arda olaylar',
 'Birbirini etkileyen ve etkilemeyen olayları ayırıp ağaçta olasılıkları çarpıp toplayabilmeni.',
 'Bağımsız olayların ikisinin birden olma olasılığı **çarpımdır**. Ağaçta bir yol boyunca olasılıklar çarpılır, farklı yollar toplanır. “**En az biri**” için tümleyen kolaydır: 1 − hiçbiri. Geri konmadan çekimde her aşamada payda azalır.',
 'P(en az biri) = 1 − P(hiçbiri)',sk,
 'Ali’nin isabet olasılığı 3/4, Bora’nınki 2/5’tir. İkisi birer atış yaparsa en az birinin isabet etme olasılığı kaçtır?',
 ['Hiçbirinin isabet etmemesi: 1/4 · 3/5 = 3/20 (ağaçta son yol).','En az biri: 1 − 3/20.','= 17/20.'],
 '17/20',
 'Olasılıkları toplayıp bire yaklaştırmak ya da “en az biri” yerine “tam biri” hesaplamak. Önce olayın tümleyenini yaz.',
 'En az biri için tümleyene bak')
assert F(comb(4,2)*comb(6,1),comb(10,3))==F(3,10)
K('matd-olasilik-03','matd|Olasılık','Kombinasyonla olasılık',
 'Aynı anda yapılan seçimlerde istenen ve tüm durumları kombinasyonla sayıp oranlayabilmeni.',
 'Sırasız ya da aynı anda yapılan seçimde durum sayısı **C(n, r)** ile bulunur. Olasılık = istenen durum sayısı / tüm durum sayısıdır; **ikisi de** kombinasyonla sayılır. Farklı gruplardan seçim yapılıyorsa gruplardaki seçimler çarpılır, “ya da” durumları toplanır.',
 'P = C(istenen) / C(tümü)',None,
 '4 kız ve 6 erkek arasından rastgele 3 kişi seçiliyor. Tam 2 kızın seçilme olasılığı kaçtır?',
 ['Tüm durumlar C(10, 3) = 120.','İstenen: 2 kız ve 1 erkek, C(4, 2) · C(6, 1) = 6 · 6 = 36.','P = 36/120 = 3/10.'],
 '3/10',
 'Yalnız bir durumu (örneğin üç kız) saymak ya da payı kombinasyon, paydayı permütasyonla hesaplamak. Pay ve paydada aynı yöntemi kullan.',
 'Pay ve payda aynı yöntemle sayılır')
ss=[(i,j) for i in range(1,7) for j in range(1,7) if i+j in (5,6)]; assert len(ss)==9 and F(len(ss),36)==F(1,4)
K('matd-olasilik-04','matd|Olasılık','Örnek uzay ve tümleyen olay',
 'Örnek uzayı doğru sayıp istenen sonuçları ayırarak ya da tümleyenle olasılığı bulabilmeni.',
 'Her sonucun eşit şansla gerçekleştiği deneyde olasılık = **istenen sonuç sayısı / tüm sonuç sayısı**dır. İki zar atılışında sonuçlar **sıralı ikililerdir**, 36 sonuç vardır. Zor sayılıyorsa tümleyen olayı kullan: P(A′) = 1 − P(A).',
 'P(A) = s(A)/s(E) · P(A′) = 1 − P(A)',None,
 'İki zar atılıyor. Zarların toplamının 5 ya da 6 olma olasılığı kaçtır?',
 ['Tüm sonuçlar 6 · 6 = 36 sıralı ikili.','Toplam 5: (1,4), (2,3), (3,2), (4,1); toplam 6: (1,5), (2,4), (3,3), (4,2), (5,1). Toplam 4 + 5 = 9.','P = 9/36 = 1/4.'],
 '1/4',
 'Zarları ayırt edilmez sayıp (2,3) ile (3,2)’yi tek saymak ya da toplam değerlerini eşit olasılıklı sanmak. Sonuçları sıralı ikili olarak yaz.',
 'Zar sonuçları sıralı ikilidir')
n=sum(1 for t in itertools.permutations([1,2,3,4,5],3) if t[2]%2==0); assert n==24 and F(2,n)==F(1,12)
K('matd-olasilik-05','matd|Olasılık','Öncüllü ve yeni nesil olasılık',
 'Koşulları önce sayma ilkesiyle uygulayıp çok aşamalı olayın olasılığını hesaplayabilmeni.',
 'Önce koşulu sağlayan **tüm durumları** say: koşullu basamağı ya da aşamayı ilk doldur, kalanlar çarpılır. Sonra olasılık = istenen / tüm durum olur. Birden fazla farklı deneme hakkı varsa deneme sayısı **paya** yazılır.',
 'P = deneme sayısı / koşullu durum sayısı',None,
 '1, 2, 3, 4, 5 rakamlarıyla rakamları farklı, son rakamı çift 3 basamaklı şifre yapılıyor. Farklı iki denemede şifreyi bulma olasılığı kaçtır?',
 ['Son rakam 2 ya da 4: 2 seçenek.','İlk rakam 4, ortadaki 3 seçenek: şifre sayısı 2 · 4 · 3 = 24.','İki farklı deneme: P = 2/24 = 1/12.'],
 '1/12',
 'Koşulları uygulamadan tüm şifreleri saymak ya da tek denemeyi hesaplamak. Önce koşullu basamağı doldur, deneme sayısını paya yaz.',
 'Önce koşullu basamağı doldur')

# ---------- PERMÜTASYON ----------
assert 4*2+3*5+1==24
sk=S(r'''\begin{tikzpicture}
\node[draw,circle] (A) at (0,0) {A}; \node[draw,circle] (B) at (2.6,1.4) {B};
\node[draw,circle] (C) at (2.6,-1.4) {C}; \node[draw,circle] (D) at (5.2,0) {D};
\draw (A)--(B) node[midway,above,sloped]{4 yol}; \draw (B)--(D) node[midway,above,sloped]{2 yol};
\draw (A)--(C) node[midway,below,sloped]{3 yol}; \draw (C)--(D) node[midway,below,sloped]{5 yol};
\draw (A)--(D) node[midway,above,sloped]{1 yol};
\end{tikzpicture}''')
K('matd-permutasyon-ve-01','matd|Permütasyon ve Kombinasyon','Toplama ve çarpma ilkesi',
 'Yol ağında art arda adımları çarpıp birbirinin yerine geçen rotaları toplayabilmeni.',
 'Birbirini izleyen aşamalarda seçenek sayıları **çarpılır** (“ve”). Birbirinin yerine geçen ayrı durumlarda sayılar **toplanır** (“ya da”). Yol ağında her rotayı ayrı yaz: ara şehirden geçen rotalar çarpılır, rotalar toplanır.',
 'art arda: ×  ·  ya da: +',sk,
 'A’dan D’ye şekildeki yollarla kaç farklı biçimde gidilir?',
 ['B üzerinden: 4 · 2 = 8 yol.','C üzerinden: 3 · 5 = 15 yol, doğrudan: 1 yol.','Toplam 8 + 15 + 1 = 24.'],
 '24 yol',
 'Bütün yolları toplamak ya da yalnız bir ara şehirden geçen rotayı saymak. Önce rotaları ayır, sonra çarp, en son topla.',
 'Ve ise çarp, ya da ise topla')
assert 7*6*5//6==35 and 7*5*6==210 and comb(7,2)*5==105
K('matd-permutasyon-ve-02','matd|Permütasyon ve Kombinasyon','Kombinasyonla seçme',
 'Sırasız seçimlerde C(n, k) ile gruplardan istenen sayıda kişi seçmeyi bilmeni.',
 'Görev farkı ve sıra yoksa seçim **sırasızdır**: n kişiden k kişi **C(n, k)** biçimde seçilir. Farklı gruplardan seçimler çarpılır. Herkesin birbiriyle bir kez eşleştiği durumda eşleşme sayısı C(n, 2) olur; yön ayrımı varsa n(n − 1).',
 'C(n, k) = n! / (k! (n − k)!)',None,
 '7 matematik ve 5 fen öğretmeninden 2 matematik, 1 fen öğretmeni seçilerek komisyon kuruluyor. Kaç farklı komisyon kurulur?',
 ['Matematikten 2 kişi: C(7, 2) = 21.','Fenden 1 kişi: C(5, 1) = 5.','Seçimler çarpılır: 21 · 5 = 105.'],
 '105',
 'Her gruptan seçimi sıralı (permütasyon) saymak ya da 2 kişilik seçimi 2 ile çarpmak. Görev farkı yoksa C kullan.',
 'Görev farkı yoksa C kullan')
assert comb(7,3)==35 and 3*comb(4,2)==18 and 35-18==17
sk=S(r'''\begin{tikzpicture}
\foreach \x in {0,...,4} \draw (\x,0)--(\x,3);
\foreach \y in {0,...,3} \draw (0,\y)--(4,\y);
\fill (0,0) circle (0.07) (4,3) circle (0.07);
\fill[vurgu] (2,1) circle (0.12);
\node[below left] at (0,0) {A}; \node[above right] at (4,3) {B};
\end{tikzpicture}''')
K('matd-permutasyon-ve-03','matd|Permütasyon ve Kombinasyon','Izgarada ve şekilde sayma',
 'Izgarada kısıtlı en kısa yolları, tüm yollardan yasak noktadan geçenleri çıkararak sayabilmeni.',
 'Sağa a, yukarı b adım gerekiyorsa en kısa yol sayısı **C(a + b, a)**’dır. Bir noktadan geçilmeyecekse **tüm yollardan** o noktadan geçenleri çıkar. Noktadan geçen yollar, iki parçanın yol sayılarının çarpımıdır.',
 'geçmeyen = tüm yollar − noktadan geçen',sk,
 'A’dan B’ye (4 sağa, 3 yukarı) yalnız sağa ve yukarı giderek, işaretli noktadan (2, 1) geçmeyen kaç en kısa yol vardır?',
 ['Tüm yollar C(7, 3) = 35.','İşaretli noktadan geçen: A→nokta C(3, 1) = 3, nokta→B C(4, 2) = 6; çarpım 18.','Geçmeyen: 35 − 18 = 17.'],
 '17 yol',
 'Noktadan geçen yolları tüm yollardan çıkarmayı unutmak ya da iki parçayı çarpmak yerine toplamak. Parçaları ayrı ayrı say.',
 'Tümünden yasak yolları çıkar')
assert 2*120==240
K('matd-permutasyon-ve-04','matd|Permütasyon ve Kombinasyon','Sıralama ve yan yana koşulu',
 'Koşullu sıralamada yan yana kalması istenenleri blok yapıp blok içi sıralamayı da saymayı bilmeni.',
 'Yan yana olması istenenler **tek blok** sayılır; blok diğer elemanlarla sıralanır, sonra **blok içi sıralama** ayrıca çarpılır. Tekrarlı permütasyonda aynı elemanların sıralamasına bölünür. Masada komşuluk, koltukların gerçek yerine bağlıdır.',
 'blok sayısı! · blok içi sıralamalar',None,
 '6 kişi sıraya giriyor. Kaan ile Lale yan yana olmak koşuluyla kaç farklı sıralama vardır?',
 ['Kaan ve Lale tek blok: 5 öğe, 5! = 120 sıralama.','Blok içinde Kaan-Lale ya da Lale-Kaan: 2 biçim.','120 · 2 = 240.'],
 '240',
 'Koşulu hiç dikkate almamak (6!) ya da blok içi iki sıralamayı çarpmayı unutmak. Blok kurarken “içi de kendi arasında dizilir” de.',
 'Blok kur, blok içini de çarp')

# ---------- VERİ ----------
d=[1,3,4,6,7,9,10]; assert d[3]==6 and d[1]==3 and d[5]==9 and d[-1]-d[0]==9
K('matd-veri-ve-01','matd|Veri ve İstatistik','Açıklık ve çeyrekler açıklığı',
 'Açıklığı, çeyrekler açıklığını ve standart sapmanın ortalamaya uzaklıkla ilişkisini yorumlayabilmeni.',
 '**Açıklık** = en büyük − en küçük değerdir. Sıralı veri ortancayla ikiye ayrılır; alt yarının ortancası Q₁, üst yarının ortancası Q₃’tür ve **çeyrekler açıklığı** Q₃ − Q₁ olur. Standart sapma, değerlerin **ortalamadan uzaklığıyla** büyür.',
 'Açıklık = en büyük − en küçük · ÇA = Q₃ − Q₁',None,
 '1, 3, 4, 6, 7, 9, 10 verisinin açıklığı ve çeyrekler açıklığı kaçtır?',
 ['Açıklık: 10 − 1 = 9.','Ortanca 6; alt yarı 1, 3, 4 ise Q₁ = 3, üst yarı 7, 9, 10 ise Q₃ = 9.','Çeyrekler açıklığı 9 − 3 = 6.'],
 'Açıklık 9, çeyrekler açıklığı 6',
 'Ortancayı yarılara katmak ya da standart sapmayı yalnız uç değerlere bakarak karşılaştırmak. Sapma tüm değerlerin ortalamaya uzaklığına bağlıdır.',
 'Sapma, ortalamaya uzaklıkla büyür')
d=sorted([8,3,9,3,12,7]); assert (d[2]+d[3])/2==7.5 and max(set(d),key=d.count)==3
K('matd-veri-ve-02','matd|Veri ve İstatistik','Ortanca ve tepe değer',
 'Veriyi sıralayıp ortancayı ve en çok tekrar eden tepe değeri doğru bulabilmeni.',
 'Ortanca için veri önce **küçükten büyüğe sıralanır**. Terim sayısı tekse ortadaki, çiftse ortadaki iki sayının **ortalaması** ortancadır. **Tepe değer**, en çok tekrar eden değerdir; sıklık tablosunda en büyük sıklığa bakılır.',
 'çift terim: ortanca = (ortadaki iki sayı toplamı) / 2',None,
 '8, 3, 9, 3, 12, 7 verisinin ortancasını ve tepe değerini bulunuz.',
 ['Sırala: 3, 3, 7, 8, 9, 12.','6 terim var, ortadakiler 7 ve 8: ortanca (7 + 8)/2 = 7,5.','3 iki kez geçer: tepe değer 3.'],
 'Ortanca 7,5; tepe değer 3',
 'Veriyi sıralamadan ortadaki sayıyı almak ya da çift terimde yalnız bir ortadaki sayıyı seçmek. Önce sırala, sonra say.',
 'Önce sırala, sonra ortayı bul')
assert 4*15-3*13==21
K('matd-veri-ve-03','matd|Veri ve İstatistik','Aritmetik ve ağırlıklı ortalama',
 'Ortalama ve terim sayısından toplamı bulup eksik ya da eklenen terimi hesaplayabilmeni.',
 'Ortalama = toplam / terim sayısı olduğundan **toplam = ortalama × terim sayısı**dır. Terim eklenince ya da çıkarılınca **iki toplamın farkına** bak. Ağırlıklı ortalamada her değer kendi ağırlığıyla çarpılır, toplam ağırlığa bölünür.',
 'toplam = ortalama × terim sayısı',None,
 '4 sayının ortalaması 15’tir. Bir sayı çıkarılınca kalan 3 sayının ortalaması 13 oluyor. Çıkarılan sayı kaçtır?',
 ['İlk toplam 4 · 15 = 60.','Kalan toplam 3 · 13 = 39.','Çıkarılan sayı 60 − 39 = 21.'],
 '21',
 'Ortalamalar arasındaki farkı (15 − 13) terim sanmak ya da yeni ortalamayı çıkarılan sayı saymak. Önce iki toplamı bul.',
 'Önce toplamları bul, farkı al')
assert 4*9+1==37 and 4*7==28
K('matd-veri-ve-04','matd|Veri ve İstatistik','Ölçülere dönüşümün etkisi',
 'Verinin her terimine işlem uygulanınca ortalama, ortanca ve açıklığın nasıl değiştiğini bilmeni.',
 'Her terim **a ile çarpılıp b eklenirse** ortalama ve ortanca da a · ort + b olur. Açıklık ve standart sapma yalnız |a| ile çarpılır; **b etkisizdir**. Tablo ve grafikten ölçü hesaplarken önce toplam terim sayısını bul.',
 'ort′ = a · ort + b · açıklık′ = |a| · açıklık',None,
 'Bir verinin ortalaması 9, açıklığı 7’dir. Her terim 4 ile çarpılıp 1 eklenirse yeni ortalama ve açıklık kaç olur?',
 ['Ortalama aynı işlemden geçer: 4 · 9 + 1 = 37.','Açıklıkta toplama etkisizdir: 4 · 7 = 28.','Sonuç: ortalama 37, açıklık 28.'],
 'Ortalama 37, açıklık 28',
 'Yalnız çarpmayı ya da yalnız toplamayı uygulamak; açıklığa da +1 eklemek. Toplama konumu kaydırır, dağılımı değiştirmez.',
 'Ortalama işlemi aynen alır')

# ---------- DOĞRULAMA ----------
w=lambda s:len(s.replace('**','').split())
ids=[x['id'] for x in KART]
assert sorted(ids)==sorted(IDS) and len(ids)==len(set(ids)),(set(IDS)^set(ids))
for x in KART:
    for a in ('id','k','baslik','olcer','kural','hata','akilda'): assert x[a],(x['id'],a)
    assert x['formul'] is None or x['formul']
    o=x['ornek']; assert o['soru'] and o['cevap'] and 2<=len(o['adimlar'])<=4
    assert w(x['baslik'])<=6,(x['id'],'baslik',w(x['baslik']))
    assert w(x['olcer'])<=25 and not x['olcer'].startswith('Bu soru'),(x['id'],'olcer',w(x['olcer']))
    assert w(x['kural'])<=60,(x['id'],'kural',w(x['kural']))
    assert w(x['hata'])<=40,(x['id'],'hata',w(x['hata']))
    assert w(x['akilda'])<=8 and '"' not in x['akilda'] and '“' not in x['akilda'],(x['id'],'akilda',w(x['akilda']))
    if x['sekil']: assert len(x['sekil'])<=25000,(x['id'],len(x['sekil']))
json.dump(KART,open('/home/claude/zekacademy-app/havuz/tekrar/kart-p10.json','w'),ensure_ascii=False)
for x in KART:
    if x['sekil']: open(f"/tmp/kor/kart/p10/{x['id']}.svg",'w').write(x['sekil'])
print(len(KART),'kart;',sum(1 for x in KART if x['sekil']),'şekilli')
