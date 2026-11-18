import json, re, math, itertools
from fractions import Fraction
from math import gcd

GR, BL, OR, MU = "#0f8a6a", "#2f5bea", "#c2410c", "#7a8599"

def svg(w, h, body, label):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="{label.replace("<", "küçüktür").replace(">", "büyüktür")}">{body}</svg>')

def t(x, y, s, size=12, anchor="middle", weight="400", fill=None):
    s = str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    f = f' fill="{fill}"' if fill else ''
    return f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}" font-weight="{weight}"{f}>{s}</text>'

def ln(x1, y1, x2, y2, c=MU, w=1.5, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="{w}"{d}/>'

def rect(x, y, w, h, c=MU, fill="none", op=".2", sw=1.5):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" stroke="{c}" stroke-width="{sw}" fill="{fill}" fill-opacity="{op}"/>'

def circ(x, y, r, c, filled):
    return f'<circle cx="{x}" cy="{y}" r="{r}" stroke="{c}" stroke-width="2" fill="{c if filled else "none"}"/>'

def axis(x0, x1, y, lo, hi, step=1, labels=None):
    sc = (x1 - x0) / (hi - lo)
    X = lambda v: x0 + (v - lo) * sc
    b = ln(x0 - 8, y, x1 + 8, y)
    for v in range(lo, hi + 1, step):
        b += ln(X(v), y - 4, X(v), y + 4)
        b += t(X(v), y + 20, str(v).replace("-", "−"))
    return b, X

cards = []
def add(**k): cards.append(k)

# 1 esitsizlik-02
ax, X = axis(20, 260, 120, -6, 6)
b = ax + ln(X(1), 78, X(5), 78, BL, 4) + circ(X(1), 78, 5, BL, False) + circ(X(5), 78, 5, BL, False) + t(X(3), 66, "b", 13, weight="600", fill=BL)
b += ln(X(-5), 38, X(-1), 38, OR, 4) + circ(X(-5), 38, 5, OR, False) + circ(X(-1), 38, 5, OR, False) + t(X(-3), 26, "−b", 13, weight="600", fill=OR)
sk1 = svg(280, 145, b, "1 < b < 5 aralığı ve −b için −5 < −b < −1 aralığı sayı doğrusunda")
a_, b_ = (2, 7), (1, 4)
lo = a_[0] - 2 * b_[1]; hi = a_[1] - 2 * b_[0]
assert (lo, hi) == (-6, 5) and len(range(lo + 1, hi)) == 10
add(id="mat-basit-esitsizlikler-02", baslik="Eşitsizlikte aralık ve işaret",
    olcer="Verilen aralıklardan yeni bir ifadenin aralığını bulup alabileceği tam sayıları sayabilmeni.",
    kural="Aynı yönlü eşitsizlikler taraf tarafa **toplanır**, çıkarılmaz. a − b için önce −b'nin aralığını bul: negatifle çarpınca **yön değişir**, uçlar yer değiştirir. Sonra iki aralığı topla; kesin eşitsizlikte uçlar sayılmaz.",
    formul="1 < b < 5 ⇒ −5 < −b < −1", sekil=sk1,
    ornek={"soru": "2 < a < 7 ve 1 < b < 4 ise a − 2b ifadesi kaç farklı tam sayı değeri alır?",
           "adimlar": ["b'yi 2 ile çarp: 2 < 2b < 8. Eksiyle çarp: −8 < −2b < −2.",
                       "Taraf tarafa topla: 2 − 8 < a − 2b < 7 − 2, yani −6 < a − 2b < 5.",
                       "Uçlar dahil değil: −5, −4, …, 4 tam sayıları kalır."],
           "cevap": "10 tam sayı"},
    hata="a ile b'nin en büyük değerlerini koyup sonucu en büyük sanmak. b büyüdükçe a − 2b küçülür; en büyük sonucu çıkarılan terimin en küçük değeri verir.",
    akilda="Çıkarılan küçükse sonuç büyük.")

# 2 bolme-01
sol = [A for A in range(10) if int(f"6{A}4") % 12 == 0]
assert sol == [2, 8]
add(id="mat-bolme-ve-01", baslik="Bölünebilme kuralları",
    olcer="Bölünebilme kuralını doğru basamaklara uygulayıp bilinmeyen rakamı bulabilmeni.",
    kural="**4** ile bölünmede yalnız son iki basamağa, **8** ile bölünmede son üç basamağa bak. **3** ve **9** için rakamlar toplamı, **11** için sağdan +, −, + işaretli toplam kullanılır. Bileşik sayıda aralarında asal çarpanlara ayır: 12 için hem 4 hem 3.",
    formul="12 | N ⇔ 4 | N ve 3 | N", sekil=None,
    ornek={"soru": "6A4 üç basamaklı sayısı 12 ile bölünebiliyorsa A kaç olabilir?",
           "adimlar": ["12 = 4 × 3 olduğundan sayı hem 4'e hem 3'e bölünmeli.",
                       "4 için A4 sayısına bak: 10A + 4 yalnız A çiftken 4'ün katıdır: 0, 2, 4, 6, 8.",
                       "3 için 6 + A + 4 = 10 + A, 3'ün katı olmalı: A = 2, 5, 8. Ortak olanlar: 2 ve 8."],
           "cevap": "A = 2 ya da 8"},
    hata="Kuralı yanlış basamak sayısına uygulamak: 4 için üç basamağa, 8 için iki basamağa bakmak. Bulduğun rakamı sayıya koyup bölerek kontrol et.",
    akilda="Dört iki basamak, sekiz üç basamak.")

# 3 bolme-03
gun = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]
assert (8 * 5) % 7 == 5 and gun[(1 + 8 * 5) % 7] == "Pazar"
add(id="mat-bolme-ve-03", baslik="Kalan aritmetiği ve periyot",
    olcer="Kalanı kullanarak tekrarlanan bir olayda haftanın gününü ya da konumu bulabilmeni.",
    kural="Toplamın ya da çarpımın kalanı, **kalanların** toplamının ya da çarpımının kalanıdır. İlk işten n. işe **(n − 1) aralık** vardır. Toplam günü 7'ye böl; ilerlemen gereken gün sayısı **kalandır**.",
    formul="bölünen = bölen × bölüm + kalan  (0 ≤ kalan < bölen)", sekil=None,
    ornek={"soru": "Ali ilacı her 5 günde bir içiyor. 1. ilacı Salı günü içtiyse 9. ilacı hangi gün içer?",
           "adimlar": ["1. ilaçtan 9. ilaca 9 − 1 = 8 aralık var: 8 × 5 = 40 gün.",
                       "40'ı 7'ye böl: 40 = 5 × 7 + 5, kalan 5.",
                       "Salı gününden 5 gün ilerle: Çarşamba, Perşembe, Cuma, Cumartesi, Pazar."],
           "cevap": "Pazar"},
    hata="Aralık yerine ilaç sayısıyla çarpmak (9 × 5) ya da başlangıç gününü de sayıp bir gün fazla ilerlemek. Kalan 0 ise aynı güne dönersin.",
    akilda="Aralık say, yediye böl, kalan kadar ilerle.")

# 4 denklem-02
a = 5
assert (a - 2) * (-3) + 4 == a - 10
add(id="mat-denklem-cozme-02", baslik="Kök ve parametreli denklem",
    olcer="Kökü verilen denklemde x yerine koyarak parametreyi, ya da çözüm kümesinin boş olduğu değeri bulabilmeni.",
    kural="Denklemin kökü, denklemi sağlayan x değeridir: x yerine **kökü koy**. Parantezi dağıtırken işaretlere dikkat et: eksi × eksi = artı. ax = b denkleminde a = 0 ve b ≠ 0 ise çözüm **boştur**, a = 0 ve b = 0 ise **sonsuz** çözüm vardır.",
    formul="ax = b:  a = 0, b ≠ 0 ⇒ çözüm kümesi boş", sekil=None,
    ornek={"soru": "(a − 2)x + 4 = a − 10 denkleminin bir kökü x = −3 ise a kaçtır?",
           "adimlar": ["x yerine −3 koy: (a − 2)(−3) + 4 = a − 10.",
                       "Dağıt: −3a + 6 + 4 = a − 10, yani −3a + 10 = a − 10.",
                       "a'ları topla: 20 = 4a, a = 5."],
           "cevap": "a = 5"},
    hata="(−3) × (−2) çarpımını −6 almak ya da (a − 2)x ifadesini ax − 2 yazmak. Parametreyi bulunca denklemde yerine koyup eşitliği kontrol et.",
    akilda="Kök verildi: x yerine koy.")

# 5 denklem-04
x = Fraction(9)
assert (x + 1) / 2 - x / 3 == 2
add(id="mat-denklem-cozme-04", baslik="Birinci dereceden denklem çözme",
    olcer="Parantezli ve kesirli birinci dereceden denklemi doğru dağılma ve işaretle çözebilmeni.",
    kural="Parantezin önündeki sayı **her terimle** çarpılır. Kesirli denklemde her terimi paydaların **EKOK'uyla** çarp. x'li terimleri bir yana, sayıları öbür yana topla. Sonuç −x = k çıkarsa iki tarafı −1 ile çarp.",
    formul="−x = k ⇒ x = −k", sekil=None,
    ornek={"soru": "(x + 1)/2 − x/3 = 2 denklemini çöz.",
           "adimlar": ["Paydaların EKOK'u 6: her terimi 6 ile çarp: 3(x + 1) − 2x = 12.",
                       "Dağıt: 3x + 3 − 2x = 12, yani x + 3 = 12.",
                       "x = 9. Kontrol: 10/2 − 9/3 = 5 − 3 = 2."],
           "cevap": "x = 9"},
    hata="Önünde eksi olan parantezde ikinci terimin işaretini değiştirmemek: −2(x − 5) ifadesini −2x − 10 yazmak. Doğrusu −2x + 10. Sonucu denklemde dene.",
    akilda="Dağıt, işarete bak, sonucu dene.")

# 6 ebob-ekok-01
pairs = [(5 * m, 5 * (9 - m)) for m in range(1, 9) if gcd(m, 9 - m) == 1]
best = max(pairs, key=lambda p: p[0] * p[1] // gcd(*p))
assert best[0] * best[1] // gcd(*best) == 100 and sorted(best) == [20, 25]
add(id="mat-ebob-ekok-01", baslik="EBOB–EKOK ilişkisi",
    olcer="Verilen EBOB bilgisinden sayıları EBOB·m ve EBOB·n biçiminde yazıp EKOK'u ya da olası ikilileri bulabilmeni.",
    kural="EBOB(a, b) = d ise a = d·m ve b = d·n yazılır; m ile n **aralarında asal**dır. EKOK = **d·m·n** olur. Ayrıca iki sayının çarpımı **EBOB × EKOK**'a eşittir. Önce m ile n'nin olası ikililerini tara.",
    formul="EBOB × EKOK = a × b", sekil=None,
    ornek={"soru": "EBOB'u 5 ve toplamı 45 olan iki doğal sayının EKOK'u en çok kaç olabilir?",
           "adimlar": ["Sayılar 5m ve 5n; toplam 5(m + n) = 45 ⇒ m + n = 9.",
                       "Aralarında asal ikililer: (1, 8), (2, 7), (4, 5). (3, 6) olmaz, çünkü ortak böleni 3.",
                       "EKOK = 5·m·n: 40, 70, 100. En büyüğü (4, 5) ikilisinden gelir: sayılar 20 ve 25."],
           "cevap": "100"},
    hata="Soru EKOK'u sorarken EBOB'u ya da m·n'yi yazmak; ya da (3, 6) gibi aralarında asal olmayan ikiliyi taramaya katmak. Sorunun istediği değere bir kez daha bak.",
    akilda="Sayı = EBOB × aralarında asal çarpan.")

# 7 ebob-ekok-03
assert gcd(24, 40) == 8 and (24 // 8) * (40 // 8) == 15
bd = rect(50, 24, 180, 108, MU, BL, ".10")
for i in range(1, 5): bd += ln(50 + 36 * i, 24, 50 + 36 * i, 132, BL, 1.2)
for j in range(1, 3): bd += ln(50, 24 + 36 * j, 230, 24 + 36 * j, BL, 1.2)
bd += t(140, 16, "40 m", 13, weight="600") + t(24, 82, "24 m", 13, weight="600") + t(68, 47, "8", 12, fill=BL) + t(140, 152, "kare kenarı = EBOB = 8", 12)
sk7 = svg(280, 160, bd, "40 m ile 24 m boyutlu dikdörtgen zemin 8 m kenarlı 15 kareye bölünmüş")
add(id="mat-ebob-ekok-03", baslik="EBOB ile eş parçalara bölme",
    olcer="Artmadan, eş ve olabildiğince büyük parçalara bölme isteyen problemi EBOB'a çevirebilmeni.",
    kural="“Artmadan, eş ve en **büyük** parça” görürsen **EBOB** kullan. Parça sayısı için her uzunluğu EBOB'a böl, sonuçları topla. Dikdörtgeni eş karelere bölerken kare kenarı EBOB'dur. Yan yana n parça varsa uçlar dahil n + 1 nokta vardır.",
    formul="parça sayısı = Σ (uzunluk ÷ EBOB)", sekil=sk7,
    ornek={"soru": "24 m × 40 m'lik dikdörtgen zemin, hiç artmadan en büyük eş karelerle kaplanacak. Kaç kare gerekir?",
           "adimlar": ["Kare kenarı EBOB(24, 40) = 8 m.",
                       "Uzun kenara 40 ÷ 8 = 5, kısa kenara 24 ÷ 8 = 3 kare sığar.",
                       "Toplam kare: 5 × 3 = 15."],
           "cevap": "15 kare"},
    hata="Parça sayısı sorulurken EBOB'u (parça uzunluğunu) yazmak ya da ortak bölenlerden en büyüğünü seçmeyip 4 gibi küçük bir değer almak.",
    akilda="En büyük eş parça: EBOB.")

# 8 koklu-02
assert 23 < 24 < 27 and 2 * 2 * 6 == 24 and 3 * 3 * 3 == 27
ax = ln(20, 80, 260, 80)
pos = lambda v: 20 + (v - 4.5) / 1.0 * 240
b = ax
for v, lab in [(4.5, "4,5"), (5.0, "5"), (5.5, "5,5")]:
    b += ln(pos(v), 76, pos(v), 84) + t(pos(v), 100, lab)
for v, lab, up in [(math.sqrt(23), "√23", True), (math.sqrt(24), "2√6", False), (math.sqrt(27), "3√3", True)]:
    b += circ(round(pos(v), 1), 80, 4.5, BL, True) + t(round(pos(v), 1), 58 if up else 122, lab, 13, weight="600", fill=BL)
sk8 = svg(280, 135, b, "√23, 2√6 ve 3√3 sayıları sayı doğrusunda soldan sağa bu sırayla dizili")
add(id="mat-koklu-sayilar-02", baslik="Köklü sayıları tahmin ve sıralama",
    olcer="Köklü sayıların yerini tam karelerle sınırlayıp büyüklük sırasına koyabilmeni.",
    kural="a² < n < b² ise **a < √n < b** olur. Köklü sayıları sıralarken katsayıyı köke sok: **a√b = √(a²·b)**. Pozitif köklerde kök içi büyük olan büyüktür. İki kök toplanıyorsa her kökü ayrı sınırla, sınırları topla.",
    formul="a√b = √(a² · b)", sekil=sk8,
    ornek={"soru": "√23, 2√6 ve 3√3 sayılarını küçükten büyüğe sırala.",
           "adimlar": ["Katsayıları köke sok: 2√6 = √(4 · 6) = √24.",
                       "3√3 = √(9 · 3) = √27.",
                       "Kök içleri 23 < 24 < 27, o hâlde √23 < √24 < √27."],
           "cevap": "√23 < 2√6 < 3√3"},
    hata="Katsayının kendisini köke sokmak: 2√6 ifadesini √12 yazmak. Doğrusu karesi girer. Kontrol: 2√6 yaklaşık 2 × 2,4 = 4,9 olmalı.",
    akilda="Katsayının karesi köke girer.")

# 9 koklu-04
assert math.isclose(math.sqrt(75) - math.sqrt(12) + 2 * math.sqrt(27), 9 * math.sqrt(3))
assert 75 == 25 * 3 and 12 == 4 * 3 and 27 == 9 * 3 and 5 - 2 + 6 == 9
add(id="mat-koklu-sayilar-04", baslik="Kök dışına çıkarma ve işlemler",
    olcer="Köklü ifadeleri kök dışına çıkarıp benzer köklerle toplama, çıkarma ve çarpma yapabilmeni.",
    kural="Kök içini **tam kare × kalan** yaz, tam karenin kökünü dışarı al. Yalnız **benzer köklerin** katsayıları toplanır ya da çıkarılır. Çarpmada katsayılar katsayılarla, kök içleri kök içleriyle çarpılır. Ondalık sayıyı 100'lü ya da 10 000'li paya çevirerek kökünü al.",
    formul="a√n ± b√n = (a ± b)√n", sekil=None,
    ornek={"soru": "√75 − √12 + 2√27 işleminin sonucu kaçtır?",
           "adimlar": ["Her kökü sadeleştir: √75 = 5√3, √12 = 2√3, √27 = 3√3.",
                       "Yerine yaz: 5√3 − 2√3 + 2 · 3√3 = 5√3 − 2√3 + 6√3.",
                       "Katsayıları işle: 5 − 2 + 6 = 9."],
           "cevap": "9√3"},
    hata="Kök içleri farklı terimleri doğrudan toplamak (√8 + √18 = √26) ya da çıkarılan terimin işaretini unutmak. Önce hepsini aynı köke getir.",
    akilda="Önce kökü sadeleştir, sonra topla.")

# 10 mutlak-02
sol = [v for v in range(-20, 20) if abs(2 * v - 3) < 7]
assert sol == [-1, 0, 1, 2, 3, 4] and sum(sol) == 9
ax, X = axis(30, 258, 90, -3, 6)
b = ax + ln(X(-2), 50, X(5), 50, GR, 4) + circ(X(-2), 50, 5, GR, False) + circ(X(5), 50, 5, GR, False)
for v in sol: b += circ(X(v), 90, 3.5, BL, True)
b += t(X(1.5), 38, "−2 < x < 5", 13, weight="600", fill=GR)
sk10 = svg(280, 125, b, "−2 ile 5 arasındaki açık aralık ve içindeki tam sayılar sayı doğrusunda")
add(id="mat-mutlak-deger-02", baslik="Mutlak değerli eşitsizlikler",
    olcer="Mutlak değerli eşitsizliği çift taraflı eşitsizliğe çevirip tam sayı çözümlerini sayabilmeni.",
    kural="|ifade| < k ise **−k < ifade < k**. |ifade| > k ise **ifade > k ya da ifade < −k**. Sonra x'i yalnız bırak. Kesin eşitsizlikte (<, >) uçlar **sayılmaz**, ≤ ya da ≥ ise uçlar sayılır.",
    formul="|x − a| ≤ k ⇒ a − k ≤ x ≤ a + k", sekil=sk10,
    ornek={"soru": "|2x − 3| < 7 eşitsizliğini sağlayan tam sayıların toplamı kaçtır?",
           "adimlar": ["Çift taraflı yaz: −7 < 2x − 3 < 7.",
                       "Her yana 3 ekle: −4 < 2x < 10. Sonra 2'ye böl: −2 < x < 5.",
                       "Uçlar dahil değil: −1, 0, 1, 2, 3, 4. Toplam: 9."],
           "cevap": "9"},
    hata="Kesin eşitsizlikte uçlardan birini saymak ya da yalnız bir tarafı çözüp öbürünü unutmak. Uçları ana eşitsizliğe koyarak kontrol et.",
    akilda="Kesinse uç yok, eşitse uç var.")

# 11 mutlak-04
assert (14 + 26) / 2 == 20 and (26 - 14) / 2 == 6
b = ln(30, 120, 250, 120) + ln(140, 20, 140, 135)
b += ln(60, 30, 140, 120, GR, 3) + ln(140, 120, 220, 30, BL, 3)
b += t(60, 130, "−3") + t(220, 136, "3") + t(150, 17, "y", 12, "start") + t(256, 124, "x", 12, "start")
b += t(76, 82, "x < 0: −x", 12, "end", fill=GR) + t(204, 82, "x ≥ 0: x", 12, "start", fill=BL)
b += t(140, 152, "y = |x| grafiği", 12)
sk11 = svg(280, 160, b, "y = |x| grafiği: x negatifken −x doğrusu, x pozitifken x doğrusu")
add(id="mat-mutlak-deger-04", baslik="Mutlak değerin tanımı ve açma",
    olcer="Mutlak değeri işarete göre açabilmeni ve bir aralığı |x − merkez| ≤ yarıçap biçiminde yazabilmeni.",
    kural="a ≥ 0 ise |a| = a; a < 0 ise **|a| = −a**. Önce içerinin işaretine bak. Önünde eksi olan mutlak değeri açınca sonucu **paranteze al**. Aralık için merkez = (m + M) ÷ 2, yarıçap = (M − m) ÷ 2.",
    formul="m ≤ x ≤ M ⇒ |x − merkez| ≤ yarıçap", sekil=sk11,
    ornek={"soru": "Bir deponun sıcaklığı 14 °C ile 26 °C arasında (uçlar dahil) tutuluyor. Bunu |x − a| ≤ r biçiminde yaz.",
           "adimlar": ["Merkez: (14 + 26) ÷ 2 = 20.",
                       "Yarıçap: (26 − 14) ÷ 2 = 6.",
                       "Yaz: |x − 20| ≤ 6. Kontrol: x = 14 ve x = 26 uçları eşitliği sağlar."],
           "cevap": "|x − 20| ≤ 6"},
    hata="x negatifken |x| ifadesini x olarak bırakmak ya da |2x| için 2x yazmak. Mutlak değerin sonucu negatif çıkamaz; çıktıysa işareti yanlış açmışsındır.",
    akilda="Mutlak değer negatif olamaz.")

# 12 oran-02
a_, b_, c_ = 3, 4, 10
assert 4 * 2 == 8 and Fraction(4, 5) == Fraction(2, 5) * 2  # sanity dummy
assert Fraction(2, 5) == Fraction(4, 10)
k = 85 // (3 + 4 + 10); assert 85 == 17 * 5 and 10 * k == 50
add(id="mat-oran-oranti-02", baslik="Ortak terimle oran birleştirme",
    olcer="Oranları ortak terimle birleştirip oranı k ile yazarak istenen parçayı bulabilmeni.",
    kural="a/b = 2/3 ise **a = 2k, b = 3k** yazılır. İki oranda ortak harf varsa onu **eşitle**: a/b ve b/c oranlarındaki b aynı sayı olmalı. Toplam biliniyorsa parça sayıları toplamından k bulunur. Sonra **istenen parçayı** hesapla.",
    formul="a/b = 3/4 ve b/c = 2/5 ⇒ a : b : c = 3 : 4 : 10", sekil=None,
    ornek={"soru": "a/b = 3/4, b/c = 2/5 ve a + b + c = 85 ise c kaçtır?",
           "adimlar": ["b'yi eşitle: 2/5 = 4/10, böylece a : b : c = 3 : 4 : 10.",
                       "Toplam parça 3 + 4 + 10 = 17; 17k = 85, k = 5.",
                       "c = 10k = 50."],
           "cevap": "50"},
    hata="k değerini (5) cevap sanmak ya da başka bir parçayı yazmak. Bulduğun sayı sorulan harfe mi ait, son adımda bir kez daha bak.",
    akilda="Ortak terimi eşitle, k ile yaz.")

# 13 oran-04
assert 6 * 8 * 15 == 10 * 9 * 8
add(id="mat-oran-oranti-04", baslik="Doğru, ters ve bileşik orantı",
    olcer="Soruda doğru mu ters mi orantı olduğunu ayırt edip bilinmeyeni bulabilmeni.",
    kural="Doğru orantıda biri artınca diğeri de artar; **bölümleri sabit**tir. Ters orantıda biri artınca diğeri azalır; **çarpımları sabit**tir. İşçi–gün–saat gibi bileşik sorularda her değişkenin güne etkisini ayrı ayrı belirle.",
    formul="doğru: a/b = sabit   ·   ters: a × b = sabit", sekil=None,
    ornek={"soru": "6 işçi günde 8 saat çalışarak bir işi 15 günde bitiriyor. 10 işçi günde 9 saat çalışırsa iş kaç günde biter?",
           "adimlar": ["İşçi ve saat arttıkça gün azalır: ikisi de gün ile ters orantılı.",
                       "Çarpım sabit: 6 · 8 · 15 = 10 · 9 · x.",
                       "720 = 90x ⇒ x = 8."],
           "cevap": "8 gün"},
    hata="Orantı türünü yanlış seçip ters orantıda bölmek. Kontrol: işçi sayısı artınca iş daha çabuk bitmeli, yani cevap 15'ten küçük çıkmalı.",
    akilda="Biri artınca diğeri azalıyorsa çarp.")

# 14 rasyonel-02
assert Fraction(3, 4) + Fraction(5, 6) - Fraction(1, 3) == Fraction(5, 4)
add(id="mat-rasyonel-sayilar-02", baslik="Kesirli ölçüm problemleri",
    olcer="Kesirli uzunluk, tarif ve terazi problemlerinde toplama, çıkarma ve denge kurabilmeni.",
    kural="Kesirlerde **paydaları eşitle**, yalnız paylar işlem görür. Üst üste binen bölüm toplamda **iki kez** sayılır; bir kez çıkarmalısın. Terazide denge varsa iki kefedeki kütleler **eşittir**; özdeş cisimler aynı kütlededir.",
    formul="birleşik uzunluk = şeritlerin toplamı − bindirmeler", sekil=None,
    ornek={"soru": "3/4 m ve 5/6 m uzunluğundaki iki şerit, 1/3 m bindirilerek uç uca ekleniyor. Toplam uzunluk kaç metredir?",
           "adimlar": ["Şeritleri topla: 3/4 + 5/6 = 9/12 + 10/12 = 19/12.",
                       "Bindirilen kısım iki kez sayıldı, bir kez çıkar: 1/3 = 4/12.",
                       "19/12 − 4/12 = 15/12 = 5/4."],
           "cevap": "5/4 m"},
    hata="Bindirme bölümünü hiç çıkarmamak ya da toplama eklemek. Kontrol: birleşik şerit, şeritlerin toplamından kısa olmalı.",
    akilda="Üst üste binen bir kez sayılır.")

# 15 rasyonel-04
fr = [Fraction(3, 5), Fraction(5, 8), Fraction(7, 12)]
assert sorted(fr) == [Fraction(7, 12), Fraction(3, 5), Fraction(5, 8)] and (72, 75, 70) == (3 * 24, 5 * 15, 7 * 10)
add(id="mat-rasyonel-sayilar-04", baslik="Kesirleri sıralama ve dört işlem",
    olcer="Kesirleri ortak paydada karşılaştırıp sıralayabilmeni ve dört işlemi doğru sırayla yapabilmeni.",
    kural="Paydalar eşitse **payı büyük** olan kesir büyüktür; paydalar farklıysa **EKOK'ta eşitle**. Bir sayının a/b'si için önce b'ye böl, sonra a ile çarp. Parçanın parçası **çarpılarak** bulunur. İşlem sırası: parantez, çarpma–bölme, toplama–çıkarma.",
    formul="a/b < c/d ⇔ a·d < c·b  (paydalar pozitif)", sekil=None,
    ornek={"soru": "3/5, 5/8 ve 7/12 kesirlerini küçükten büyüğe sırala.",
           "adimlar": ["Paydaların EKOK'u 120: 3/5 = 72/120, 5/8 = 75/120, 7/12 = 70/120.",
                       "Payları karşılaştır: 70 < 72 < 75."],
           "cevap": "7/12 < 3/5 < 5/8"},
    hata="Payı büyük olan kesri her zaman büyük sanmak: 7/12 kesrini 3/5'ten büyük görmek. Pay ve paydayı birlikte değerlendirmek için paydaları eşitle.",
    akilda="Karşılaştırmadan önce paydaları eşitle.")

# 16 sayi-basamaklari-02
cands = [n for n in range(100, 1000) if len(set(str(n))) == 3 and sum(map(int, str(n))) == 10]
assert min(cands) == 109
add(id="mat-sayi-basamaklari-02", baslik="Rakamlarla en büyük–en küçük sayı",
    olcer="Basamak çözümlemesiyle koşulu kurup rakamlarla yazılabilen en büyük ya da en küçük sayıyı bulabilmeni.",
    kural="Sayıyı çözümle: **ABC = 100A + 10B + C**. Koşulu tek harfe indir. En büyük sayı için yüksek basamaktan başla, en büyük rakamı dene ve koşulu **kontrol et**. En küçük sayıda baştaki rakam **0 olamaz**.",
    formul="ABC = 100A + 10B + C", sekil=None,
    ornek={"soru": "Rakamları birbirinden farklı ve rakamları toplamı 10 olan üç basamaklı en küçük sayı kaçtır?",
           "adimlar": ["Yüzler basamağı 0 olamaz, en küçüğü 1 al.",
                       "Onlar basamağına en küçük rakam 0'ı koy.",
                       "Birler 10 − 1 − 0 = 9; rakamlar 1, 0, 9 farklı, koşul sağlanıyor."],
           "cevap": "109"},
    hata="Koşulu kontrol etmeden ilk bulduğun sayıyı seçmek ya da yüzler basamağına 0 koymak (019 gibi). Seçtiğin sayıyı koşula koyup sına.",
    akilda="Yüksek basamaktan başla, koşulu kontrol et.")

# 17 sayi-basamaklari-04
assert 925 - 529 == 396 == 99 * (9 - 5)
add(id="mat-sayi-basamaklari-04", baslik="Rakam yer değiştirme ve silme",
    olcer="Rakamlar yer değiştirince ya da silinince sayının ne kadar değiştiğini basamak değerleriyle hesaplayabilmeni.",
    kural="Rakamın sayıya katkısı **rakam × basamak değeri**dir. Değişim, rakam farkı ile basamak değerinin çarpımıdır. Yüzler ile birler basamağı yer değiştirirse sayı **99 × rakam farkı** kadar değişir. Baştaki rakam 0 olamaz.",
    formul="ABC → CBA: fark = 99 × (A − C)", sekil=None,
    ornek={"soru": "925 sayısında yüzler ile birler basamağındaki rakamlar yer değiştirirse sayı ne kadar azalır?",
           "adimlar": ["Yeni sayı 529.",
                       "Fark: 925 − 529 = 396.",
                       "Kontrol: 99 × (9 − 5) = 99 × 4 = 396."],
           "cevap": "396"},
    hata="Yalnız rakam farkını (9 − 5) almak ya da yer değişimini onlar basamağı gibi (10 × 4) hesaplamak. Rakamların hangi basamakta olduğuna bak.",
    akilda="Fark = basamak değeri × rakam farkı.")

# 18 temel-02
for aa in (1, 3, 5, 7):
    for bb in (0, 2, 4, 6):
        assert (3 * aa + bb + 1) % 2 == 0
add(id="mat-temel-kavramlar-02", baslik="Tek–çift ve ardışık sayılar",
    olcer="Tek–çift kurallarıyla bir ifadenin her zaman tek ya da çift olup olmadığına karar verebilmeni.",
    kural="Tek + tek = çift, çift + çift = çift, tek + çift = tek. Çarpımda çarpanlardan biri çiftse çarpım **çift**, hepsi tekse **tek**dir. “Her zaman” sorularında harflere farklı tek–çift değerler ver; bir durumda bozulursa ifade **her zaman** değildir. Ardışık tek sayılar 2'şer artar.",
    formul="çift × herhangi sayı = çift", sekil=None,
    ornek={"soru": "a tek, b çift sayıdır. 3a + b + 1 ifadesi tek mi çifttir?",
           "adimlar": ["3a: tek × tek = tek.",
                       "3a + b: tek + çift = tek.",
                       "Üstüne 1 ekle: tek + tek = çift."],
           "cevap": "Her zaman çift"},
    hata="Tek bir sayı deneyip karar vermek. Bir ifade bir durumda tek çıkıyor diye her zaman tek değildir; harflerin tek ve çift hâllerini ayrı ayrı düşün.",
    akilda="Çarpanlardan biri çiftse çarpım çift.")

# 19 temel-04
vals = dict(R1=4, R2=7, R3=9, R4=2, T=5, B=6)
tot = sum(vals.values()); assert tot == 33 and tot - 7 - 2 == 24
S = 44; x0 = 30; yr = 54
cells = [("T", x0 + S, yr - S, OR), ("R1", x0, yr, BL), ("R2", x0 + S, yr, GR), ("R3", x0 + 2 * S, yr, BL), ("R4", x0 + 3 * S, yr, GR), ("B", x0 + S, yr + S, OR)]
b = ""
for nm, cx, cy, col in cells:
    b += rect(cx, cy, S, S, col, col, ".22") + t(cx + S / 2, cy + S / 2 + 6, vals[nm], 16, weight="600")
b += t(140, 124, "Aynı renk:", 12, "start") + t(140, 142, "karşılıklı yüz", 12, "start")
sk19 = svg(280, 155, b, "Zar açınımı: yan yana dört kare, ikinci karenin üstünde ve altında birer kare; aynı renkli kareler karşılıklı yüzdür")
add(id="mat-temel-kavramlar-04", baslik="Örüntü, döngü ve zar açınımı",
    olcer="Zar açınımında karşılıklı yüzleri belirleyip örüntü ve döngü sorularında toplam ya da kalanı bulabilmeni.",
    kural="Açınımda aynı sırada, **aralarında bir kare** bulunan iki kare karşılıklı yüzdür; yan yana kareler komşudur. Yan yüzlerin toplamı = **tümü − karşılıklı bir çift**. Döngülerde (saat, gün) toplam adımı periyoda böl, yalnız **kalan** önemlidir.",
    formul="yan yüzler = tüm yüzler − ön − arka", sekil=sk19,
    ornek={"soru": "Şekildeki açınım zar olacak biçimde katlanıyor. 7 yazan yüz ön yüzse, ön ve arka yüz dışındaki yüzlerin toplamı kaçtır?",
           "adimlar": ["7'nin karşısı, aralarında bir kare olan 2'dir (arka yüz).",
                       "Tüm yüzlerin toplamı: 4 + 7 + 9 + 2 + 5 + 6 = 33.",
                       "33 − 7 − 2 = 24."],
           "cevap": "24"},
    hata="Yan yana duran kareyi karşılıklı yüz sanmak. Karşılıklı yüzler arasında her zaman bir kare vardır; üst ve alt kareler birbirinin karşısıdır.",
    akilda="Karşılıklı yüz, arada bir kare.")

# 20 temel-06
w = Fraction(3, 4) * Fraction(2, 3); assert w == Fraction(1, 2) and 90 / w == 180
add(id="mat-temel-kavramlar-06", baslik="Günlük ölçü ve model problemleri",
    olcer="Kalanın kesri ve cetvel okuma gibi günlük problemleri adımlara bölüp bütünü bulabilmeni.",
    kural="Bütünün a/b'si ayrılınca kalan **1 − a/b**'dir. Kalanın c/d'si, bütünün **(1 − a/b) · c/d**'sidir. Bütünü bulmak için verilen parçayı **bütüne düşen kesre böl**. Cetvelde önce bir bölmenin değerini bul: 1 cm = 10 mm.",
    formul="bütün = parça ÷ parçanın bütüne oranı", sekil=None,
    ornek={"soru": "Bir bahçenin 1/4'üne marul, kalanın 2/3'üne havuç ekilmiştir. Havuç bölümü 90 m² ise bahçe kaç m²'dir?",
           "adimlar": ["Marul sonrası kalan 1 − 1/4 = 3/4.",
                       "Havuç bütünün 3/4 · 2/3 = 1/2'sidir.",
                       "Bütün = 90 ÷ 1/2 = 180."],
           "cevap": "180 m²"},
    hata="Kalanın kesrini bütünün kesri sanmak: havuç 2/3 diyerek 90 ÷ 2/3 = 135 bulmak. Kalan, bütünün tamamı değildir; önce kalanla çarp.",
    akilda="Kalanın kesrini bütüne çevir, sonra böl.")

# 21 carpanlara-02
xx, yy = 7, 5
assert xx * yy - 3 * xx + 4 * yy - 12 == (xx + 4) * (yy - 3) == 22
add(id="mat-carpanlara-ayirma-02", baslik="Ortak çarpan ve gruplama",
    olcer="Ortak çarpan parantezine alıp gruplayarak ifadeyi çarpanlarına ayırabilmeni.",
    kural="Önce bütün terimlerdeki **ortak çarpanı** dışarı al. Dört terimde ikişer terimi **grupla**, her gruptan ortak çarpanı al; kalan parantezler **aynı** olmalı. Eksi işaretli terimde ortak çarpanı eksiyle birlikte al.",
    formul="ac + ad + bc + bd = (a + b)(c + d)", sekil=None,
    ornek={"soru": "xy − 3x + 4y − 12 ifadesini çarpanlarına ayır; x = 7, y = 5 için değerini bul.",
           "adimlar": ["İkişer grupla: x(y − 3) + 4(y − 3).",
                       "Ortak parantezi al: (x + 4)(y − 3).",
                       "Değer: (7 + 4)(5 − 3) = 11 · 2 = 22."],
           "cevap": "22"},
    hata="Eksi terimden çarpan alırken işareti atlamak; −12'yi dışarı alınca (y + 3) elde etmek. İki parantez eşleşmiyorsa işaretlerini yeniden kontrol et.",
    akilda="İki parantez aynı çıkmalı.")

# 22 carpanlara-04
a_, b_ = 9, 4
assert a_ ** 2 - b_ ** 2 == 65 and a_ + b_ == 13 and 65 // 13 == 5 and (13 + 5) // 2 == 9 and (13 - 5) // 2 == 4
b = '<polygon points="60,20 132,20 132,78 190,78 190,150 60,150" fill="#0f8a6a" fill-opacity=".2" stroke="#0f8a6a" stroke-width="2"/>'
b += '<rect x="132" y="20" width="58" height="58" fill="none" stroke="#7a8599" stroke-width="1.5" stroke-dasharray="4 3"/>'
b += t(44, 90, "a", 14, weight="600") + t(125, 166, "a", 14, weight="600") + t(161, 14, "b", 14, weight="600") + t(204, 52, "b", 14, weight="600")
b += t(110, 100, "kalan alan", 12) + t(110, 118, "a² − b²", 13, weight="600")
sk22 = svg(280, 175, b, "Kenarı a olan kareden kenarı b olan küçük kare köşeden kesilmiş")
add(id="mat-carpanlara-ayirma-04", baslik="Alan modelleri ve çarpanlara ayırma",
    olcer="Alan problemlerini iki kare farkı ya da ortak çarpanla çarpanlara ayırıp kenarları bulabilmeni.",
    kural="Kareden kare kesilince kalan alan **a² − b²** olur ve **(a − b)(a + b)** biçiminde çarpanlanır. Kenar toplamı ya da farkı verilince diğerini bölerek bul. Şerit kesilirse kalan alan **x(x − y)** biçiminde ortak çarpanla yazılır.",
    formul="a² − b² = (a − b)(a + b)", sekil=sk22,
    ornek={"soru": "Kenarı a olan kareden kenarı b olan kare kesilince kalan alan 65 cm² oluyor. a + b = 13 ise b kaçtır?",
           "adimlar": ["65 = (a − b)(a + b) = (a − b) · 13, yani a − b = 5.",
                       "a + b = 13 ve a − b = 5 taraf tarafa toplanır: 2a = 18, a = 9.",
                       "b = 13 − 9 = 4."],
           "cevap": "b = 4 cm"},
    hata="Bulduğun ilk değeri (a − b = 5 ya da a = 9) cevap yazmak. Soru hangi kenarı istiyor, son adımda bir kez daha oku.",
    akilda="Alan farkı: (a − b)(a + b).")

# 23 uslu-02
xs = 1
assert Fraction(1, 4) ** (xs + 2) == Fraction(8) ** (xs - 3) == Fraction(1, 64)
add(id="mat-uslu-sayilar-02", baslik="Üslü denklemler",
    olcer="Üslü denklemde tabanları ortak tabana çevirip üsleri eşitleyebilmeni.",
    kural="Bütün tabanları **aynı tabana** çevir; taban eşitse **üsler eşittir**. Kesirli tabanı negatif üsle yaz: 1/4 = 2⁻². Kuvvetin kuvvetinde üsler çarpılır; parantezli üssü çarparken **her terimi** çarp.",
    formul="aˣ = aʸ ⇒ x = y  (a ≠ 0, 1)", sekil=None,
    ornek={"soru": "(1/4)^(x+2) = 8^(x−3) denkleminde x kaçtır?",
           "adimlar": ["Tabanı 2 yap: (2⁻²)^(x+2) = (2³)^(x−3), yani 2^(−2x−4) = 2^(3x−9).",
                       "Üsleri eşitle: −2x − 4 = 3x − 9.",
                       "5 = 5x, x = 1."],
           "cevap": "x = 1"},
    hata="Kesirli tabandaki negatif işareti atmak: (1/4)^(x+2) ifadesini 2^(2x+4) yazmak. Doğrusu 2^(−2x−4). Sonucu iki tarafa koyup kontrol et.",
    akilda="Önce tabanı eşitle, sonra üsleri.")

# 24 uslu-04
A, B, C = Fraction(1, 9) ** 2, Fraction(27) ** -1, Fraction(1, 3) ** -2
assert A == Fraction(3) ** -4 and B == Fraction(3) ** -3 and C == Fraction(3) ** 2 and A < B < C
add(id="mat-uslu-sayilar-04", baslik="Üslü sayıları sıralama",
    olcer="Üslü sayıları ortak tabana çevirerek büyüklük sırasına koyabilmeni.",
    kural="Negatif üs sayıyı **ters çevirir**: a⁻ⁿ = 1/aⁿ. Tabanları aynı tabana getir; taban 1'den büyükse **üssü büyük olan** büyüktür. Tabanlar ortaklaşmıyorsa üsleri ortak bölenle eşitle. Tabanı 1'den büyük ve üssü negatif sayı 0'a yakındır, küçüktür.",
    formul="(1/a)ⁿ = a⁻ⁿ", sekil=None,
    ornek={"soru": "A = (1/9)², B = 27⁻¹, C = (1/3)⁻² sayılarını küçükten büyüğe sırala.",
           "adimlar": ["Tabanı 3 yap: A = (3⁻²)² = 3⁻⁴, B = (3³)⁻¹ = 3⁻³, C = (3⁻¹)⁻² = 3².",
                       "Taban 3 > 1, üs büyük olan büyük: −4 < −3 < 2."],
           "cevap": "A < B < C"},
    hata="Negatif üssü yok sayıp 27⁻¹ değerini 27 gibi büyük almak. Negatif üs sayıyı ters çevirir; sonuç 0'a yakın küçük bir kesirdir.",
    akilda="Negatif üs sayıyı ters çevirir.")

# --- kapanış ---
girdi = re.findall(r"^### (\S+) \|", open("/tmp/kor/kart/parti/p12.txt", encoding="utf-8").read(), re.M)
wc = lambda s: len(s.split())
for c in cards:
    c["k"] = "mat"; c.setdefault("sekil", None)
    for f in ("id", "baslik", "olcer", "kural", "ornek", "hata", "akilda"):
        assert c.get(f), (c["id"], f)
    assert "formul" in c
    assert wc(c["baslik"]) <= 6 and wc(c["olcer"]) <= 25 and wc(c["kural"]) <= 60, (c["id"], wc(c["baslik"]), wc(c["olcer"]), wc(c["kural"]))
    assert wc(c["hata"]) <= 40 and wc(c["akilda"]) <= 8, c["id"]
    assert not c["olcer"].startswith("Bu soru")
    o = c["ornek"]; assert o["soru"] and 2 <= len(o["adimlar"]) <= 4 and o["cevap"], c["id"]
    if c["sekil"]:
        assert len(c["sekil"]) <= 25000
        open(f"/tmp/kor/kart/p12/{c['id']}.svg", "w", encoding="utf-8").write(c["sekil"])
    # key order
    order = ["id", "k", "baslik", "olcer", "kural", "formul", "sekil", "ornek", "hata", "akilda"]
    for key in list(c): 
        pass
cards = [{k: c[k] for k in ["id", "k", "baslik", "olcer", "kural", "formul", "sekil", "ornek", "hata", "akilda"]} for c in cards]
assert [c["id"] for c in cards] == girdi and len(set(girdi)) == len(girdi) == 24
json.dump(cards, open("/home/claude/zekacademy-app/havuz/tekrar/kart-p12.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(cards), "kart,", sum(1 for c in cards if c["sekil"]), "şekilli")
