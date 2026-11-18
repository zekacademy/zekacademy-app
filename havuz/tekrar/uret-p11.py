import json, re, math
from fractions import Fraction
from itertools import product

GIRDI = '/tmp/kor/kart/parti/p11.txt'
CIKTI = '/home/claude/zekacademy-app/havuz/tekrar/kart-p11.json'
K = 'mat'

def svg(w, h, label, body):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" role="img" aria-label="%s">%s</svg>'
            % (w, h, label, body))

def line(x1, y1, x2, y2, c='var(--muted)', w=1.5, extra=''):
    return '<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" %s/>' % (x1, y1, x2, y2, c, w, extra)

def text(x, y, s, size=12, anchor='start', weight=400):
    return '<text x="%s" y="%s" font-size="%s" text-anchor="%s" font-weight="%s">%s</text>' % (x, y, size, anchor, weight, s)

def circ(x, y, r, fill, stroke='var(--ink)', w=2):
    return '<circle cx="%s" cy="%s" r="%s" fill="%s" stroke="%s" stroke-width="%s"/>' % (x, y, r, fill, stroke, w)

cards = []
def kart(id, baslik, olcer, kural, formul, sekil, soru, adimlar, cevap, hata, akilda):
    cards.append({"id": id, "k": K, "baslik": baslik, "olcer": olcer, "kural": kural, "formul": formul,
                  "sekil": sekil, "ornek": {"soru": soru, "adimlar": adimlar, "cevap": cevap},
                  "hata": hata, "akilda": akilda})

# 1 ---------------------------------------------------------------
assert 15 + 7 * 12 <= 100 < 15 + 7 * 13
kart("mat-basit-esitsizlikler-01", "Eşitsizlikle problem kurma",
 "Bir harcamayı eşitsizliğe çevirip tam sayı koşuluyla en büyük değeri bulabilmeni.",
 "Sabit harcamayı **önce bütçeden düş**, kalanı birim fiyata böl. Tam sayı istendiği için sonucu **aşağı yuvarla**. “n tane alabiliyor, n + 1 tane alamıyor” bilgisi n × fiyat ≤ para < (n + 1) × fiyat demektir.",
 "sabit + birim × x ≤ bütçe", None,
 "Bir kafede 15 TL sabit servis ücreti var, her çay 7 TL. 100 TL ile en çok kaç çay içilir?",
 ["Eşitsizliği kur: 15 + 7x ≤ 100", "Sabiti düş: 7x ≤ 85, yani x ≤ 12,14…", "Tam sayı istendiği için aşağı yuvarla: x = 12", "Kontrol: 15 + 7·12 = 99 ≤ 100, 15 + 7·13 = 106 > 100"],
 "12 çay",
 "Sonucu yukarı yuvarlamak ya da sabit ücreti düşmeden bölmek. Kontrol: bulduğun sayıyı ve bir fazlasını ücret ifadesine koy; biri bütçeyi aşmalı.",
 "Önce sabiti düş, sonra böl.")

# 2 ---------------------------------------------------------------
sol = [x for x in range(-20, 21) if -10 <= -3 * x + 2 < 8]
assert sol == [-1, 0, 1, 2, 3, 4] and sum(sol) == 9
X = lambda v: 30 + (v + 3) * 27
b = line(20, 50, 262, 50, 'var(--ink)', 2)
for v in range(-3, 6):
    b += line(X(v), 44, X(v), 56, 'var(--ink)', 1.5) + text(X(v), 72, str(v).replace('-', '−'), 12, 'middle')
b += line(X(-2), 50, X(4), 50, 'var(--rule)', 5)
b += circ(X(-2), 50, 6, 'var(--card)', 'var(--rule)', 2.5) + circ(X(4), 50, 6, 'var(--rule)', 'var(--rule)', 2.5)
b += text(140, 24, '−2 &lt; x ≤ 4', 14, 'middle', 600) + text(140, 94, 'boş uç alınmaz, dolu uç alınır', 12, 'middle')
sek = svg(280, 104, 'Sayı doğrusunda −2 boş, 4 dolu uçlu aralık', b)
kart("mat-basit-esitsizlikler-03", "Eşitsizlik çözümü ve tam sayılar",
 "Çift taraflı eşitsizliği çözüp uç değerlere dikkat ederek tam sayı çözümlerini bulabilmeni.",
 "x'i yalnız bırak; **negatif sayıyla çarpar ya da bölersen yön değişir**. Sonra uçlara bak: < ve > uç değeri almaz, ≤ ve ≥ alır. Tam sayıları, negatifler ve 0 dahil, tek tek yaz.",
 "−a · x &lt; b  ⇒  x &gt; −b / a".replace('&lt;', '<').replace('&gt;', '>'), sek,
 "−10 ≤ −3x + 2 < 8 eşitsizliğini sağlayan tam sayıların toplamı kaçtır?",
 ["2'yi çıkar: −12 ≤ −3x < 6", "−3'e böl, yönleri çevir: 4 ≥ x > −2, yani −2 < x ≤ 4", "Tam sayılar: −1, 0, 1, 2, 3, 4", "Toplam: 9"],
 "9",
 "Kesin uç olan −2'yi çözüm saymak ya da negatif tam sayıları ve 0'ı atlamak. Kontrol: aralığı sayı doğrusuna çiz, boş ucu dışarıda bırak.",
 "Negatifle bölersen yön döner.")

# 3 ---------------------------------------------------------------
assert 8 * 6 + 7 == 55
kart("mat-bolme-ve-02", "Kalanlı bölme ilişkisi",
 "Bölünen, bölen, bölüm ve kalan arasındaki ilişkiyi kalanın sınırını da gözeterek kullanabilmeni.",
 "Bölünen = bölen × bölüm + kalan ve her zaman **0 ≤ kalan < bölen**. Bölünen en büyük isteniyorsa kalan **bölenin bir eksiğidir**. En küçük isteniyorsa kalan 0 alınır (0 olamıyorsa 1).",
 "bölünen = bölen × bölüm + kalan", None,
 "Bir sayı 8'e bölündüğünde bölüm 6 çıkıyor. Bu sayı en çok kaç olabilir?",
 ["Kalan 8'den küçük olmalı; en büyüğü 7", "Bölünen = 8 × 6 + 7", "= 48 + 7 = 55"],
 "55",
 "Kalanı 0 bırakmak, bölüme ya da bölene eşit almak. “En çok” denince kalan da en büyük olmalı. Kontrol: kalan bölenden küçük mü?",
 "Kalan her zaman bölenden küçük.")

# 4 ---------------------------------------------------------------
x = 6
assert (2 * x + 1) - (x - 3) == 10
kart("mat-denklem-cozme-01", "Akış şemasından denklem kurma",
 "Makine ya da akış şemasındaki işlemleri sırayla okuyup denkleme çevirebilmeni.",
 "Şemadaki her kutuyu sırayla bir ifadeye çevir. **Çıkarılan ifadeyi parantez içine al** ve işaretleri dağıt. Kollar birleşiyorsa birleşme kutusunun toplama mı çıkarma mı olduğunu doğru oku. Çıkan denklemi çöz.",
 "(üst kol) − (alt kol) = çıkış", None,
 "Girişi x olan şemada üst kol 2x + 1, alt kol x − 3 üretir. Birleşme kutusu üst koldan alt kolu çıkarır ve çıkış 10 olur. x kaçtır?",
 ["Denklemi kur: (2x + 1) − (x − 3) = 10", "Parantezi aç, işaretleri dağıt: 2x + 1 − x + 3 = 10", "Sadeleştir: x + 4 = 10", "x = 6"],
 "x = 6",
 "Çıkarmada parantezi açmayıp 2x + 1 − x − 3 yazmak. Kontrol: bulduğun x'i şemaya geri yerleştir, çıkışın 10 çıktığını gör.",
 "Çıkarılanı parantezle, işareti dağıt.")

# 5 ---------------------------------------------------------------
xx, yy = 4, 3
assert 2 * xx + yy == 11 and xx - yy == 1 and xx + 2 * yy == 10
kart("mat-denklem-cozme-03", "Denklem sistemini çözme",
 "İki denklemden bilinmeyenleri bulup soruda istenen ifadeyi hesaplayabilmeni.",
 "Denklemleri uygun sayıyla çarpıp **taraf tarafa topla ya da çıkar**; bir bilinmeyen yok olur. Çıkarırken ikinci denklemin **her teriminin işaretini değiştir**. Bulduğun değeri öbür denklemde yerine koy. Son olarak **sorulan ifadeyi** hesapla.",
 "yok et → bir bilinmeyeni bul → yerine koy", None,
 "2x + y = 11 ve x − y = 1 ise x + 2y kaçtır?",
 ["Taraf tarafa topla: 3x = 12, yani x = 4", "İkinci denklemde yerine koy: 4 − y = 1, yani y = 3", "İstenen: x + 2y = 4 + 6 = 10"],
 "10",
 "x ya da y'yi bulup durmak; soru x + 2y ya da x · y isteyebilir. Kontrol: iki değeri iki denklemde de dene.",
 "Bul, yerine koy, sorulanı hesapla.")

# 6 ---------------------------------------------------------------
d = 20; k = 3 * d
assert 2 * k + d == 140 and k == 3 * d
kart("mat-denklem-cozme-05", "Terazi ve sözel denklem kurma",
 "Terazi ya da sözel durumdan denklem kurup istenen nesnenin değerini bulabilmeni.",
 "Dengedeki terazide iki kefenin kütlesi eşittir. **İki kefeden aynı nesneyi atınca denge bozulmaz.** Önce nesneler arasındaki oranı bul, sonra her şeyi **tek nesne cinsinden** yaz. Sonda **sorulan nesneyi** ara.",
 "sol kefe = sağ kefe", None,
 "Dengedeki iki terazide: 1 kare = 3 daire ve 2 kare + 1 daire = 140 g. Bir daire kaç gramdır?",
 ["Oran: kare = 3 daire", "Her şeyi daire cinsinden yaz: 2 · 3 daire + 1 daire = 7 daire = 140 g", "Bir daire: 140 ÷ 7 = 20 g"],
 "20 g",
 "Karenin kütlesini (60 g) cevap sanmak ya da oranı ters kurmak. Kontrol: bulduğun değerleri iki terazide de yerine koy.",
 "Önce oran, sonra tek nesne.")

# 7 ---------------------------------------------------------------
e = math.lcm(9, 12)
assert e == 36 and 36 % 7 == 1
kart("mat-ebob-ekok-02", "EKOK ile birlikte tekrar etme",
 "Farklı aralıklarla tekrar eden olayların yeniden birlikte olacağı zamanı EKOK ile bulabilmeni.",
 "İki olay birlikte tekrar ediyorsa buluşma zamanı aralıkların **EKOK'udur**. Dişli, nöbet, lamba ve “en küçük kare” soruları aynı mantık. Gün adı için toplam günü **7'ye böl, kalan kadar ileri say**.",
 "birlikte olma zamanı = EKOK(a, b)", None,
 "Ali her 9 günde, Buse her 12 günde nöbet tutuyor. Pazartesi birlikte tuttularsa bir sonraki ortak nöbet hangi gün?",
 ["EKOK(9, 12) = 36 gün sonra", "36 = 5 · 7 + 1, kalan 1", "Pazartesiden 1 gün ileri: salı"],
 "Salı",
 "Aralıkları toplamak, yalnız büyük aralığı almak ya da EBOB bulmak. Kontrol: sonuç iki aralığa da tam bölünmeli.",
 "Birlikte tekrar eden olaylarda EKOK.")

# 8 ---------------------------------------------------------------
assert Fraction(8) / (math.sqrt(7) - math.sqrt(3)) - 2 * (math.sqrt(7) + math.sqrt(3)) < 1e-9
kart("mat-koklu-sayilar-01", "Eşlenikle paydayı rasyonel yapma",
 "Paydası iki terimli köklü olan kesri eşlenikle genişletip sadeleştirebilmeni.",
 "Paydada √a − √b varsa **hem payı hem paydayı eşleniği √a + √b ile çarp**. Payda a − b olur, kök kalmaz. Payı dağıtmayı ve paydadaki sayıya bölmeyi unutma.",
 "(√a − √b)(√a + √b) = a − b", None,
 "8 / (√7 − √3) kesrinin paydasını rasyonel yap.",
 ["Eşlenik √7 + √3 ile genişlet: 8(√7 + √3) / (√7 − √3)(√7 + √3)", "Payda: 7 − 3 = 4", "8(√7 + √3) / 4 = 2(√7 + √3)"],
 "2(√7 + √3)",
 "Payı eşlenikle çarpmadan bırakmak, paydadaki sayıya bölmeyi unutmak ya da √7 + √3'ü √10 yazmak. Farklı kök içleri tek kökte birleşmez.",
 "Pay da payda da eşlenikle.")

# 9 ---------------------------------------------------------------
assert 128 == 64 * 2 and 4 * 8 == 32 and 32 // 4 == 8
b = '<rect x="80" y="20" width="120" height="120" fill="var(--rule-soft)" stroke="var(--rule)" stroke-width="2.5"/>'
for (px, py) in [(80, 20), (140, 20), (200, 20), (200, 80), (200, 140), (140, 140), (80, 140), (80, 80)]:
    b += circ(px, py, 6, 'var(--warn)', 'var(--card)', 2)
b += text(140, 85, 'kare', 13, 'middle') + text(140, 164, '8 direk = 8 aralık (kapalı çevre)', 12, 'middle')
sek = svg(280, 172, 'Kare çevresinde köşelere ve kenar ortalarına dikilmiş 8 direk', b)
kart("mat-koklu-sayilar-03", "Köklü uzunluk, çevre ve alan",
 "Kenarı ya da alanı köklü verilen şekillerde kök dışına çıkarıp çevre ve alanı hesaplayabilmeni.",
 "Alanı A olan karenin kenarı **√A**, çevresi **4√A**'dır. Kök içini “tam kare × kalan” yazıp dışarı çıkar; benzer köklerin katsayılarını topla. Kapalı çevrede eşit aralıklı nokta sayısı **aralık sayısına eşittir**.",
 "alan A  ⇒  kenar √A, çevre 4√A", sek,
 "Alanı 128 m² olan kare bahçenin çevresine 4√2 m arayla direk dikilecek. Kaç direk gerekir?",
 ["Kenar: √128 = √(64 · 2) = 8√2", "Çevre: 4 · 8√2 = 32√2", "Aralık sayısı: 32√2 ÷ 4√2 = 8"],
 "8 direk",
 "Çevre yerine bir kenarı ya da 2 × kenarı almak, kapalı çevrede aralık sayısına bir direk daha eklemek. Kare çevresi 4 kenardır.",
 "Kapalı çevrede direk sayısı aralık sayısıdır.")

# 10 --------------------------------------------------------------
r = sorted([x for x in range(-30, 30) if abs(3 * x + 3) == 12])
assert r == [-5, 3] and sum(r) == -2
kart("mat-mutlak-deger-01", "Mutlak değerli denklemler",
 "|ifade| = k denklemini iki duruma ayırıp bütün kökleri bulabilmeni.",
 "k > 0 iken |ifade| = k ise ifade **k ya da −k** olur. İki denklemi ayrı çöz; sabiti karşıya geçirirken işarete dikkat et. Sonda soru **toplamı mı çarpımı mı** istiyor, bir kez daha bak. k < 0 ise çözüm yoktur.",
 "|A| = k  ⇒  A = k  ya da  A = −k", None,
 "|3x + 3| = 12 denkleminin köklerinin toplamı kaçtır?",
 ["Pozitif durum: 3x + 3 = 12, 3x = 9, x = 3", "Negatif durum: 3x + 3 = −12, 3x = −15, x = −5", "Toplam: 3 + (−5) = −2"],
 "−2",
 "Yalnız pozitif durumu çözmek ya da negatif durumda sabiti yanlış taşımak. Kontrol: iki kökü de denklemde dene, ikisi de 12 vermeli.",
 "İçerisi hem k hem −k olabilir.")

# 11 --------------------------------------------------------------
cz = sorted([x for x in range(-50, 51) if abs(x - 5) == 2 * abs(x + 1)])
assert cz == [-7, 1] and sum(cz) == -6
b = line(20, 70, 260, 70, 'var(--ink)', 2)
for xx_, lb in [(60, 'a − d'), (140, 'a'), (220, 'a + d')]:
    b += line(xx_, 62, xx_, 78, 'var(--ink)', 1.5) + text(xx_, 96, lb, 13, 'middle', 600)
b += circ(60, 70, 5, 'var(--warn)', 'var(--warn)') + circ(220, 70, 5, 'var(--warn)', 'var(--warn)') + circ(140, 70, 5, 'var(--rule)', 'var(--rule)')
b += line(60, 44, 140, 44, 'var(--brand)', 2) + line(140, 44, 220, 44, 'var(--brand)', 2)
b += text(100, 38, 'd', 13, 'middle', 600) + text(180, 38, 'd', 13, 'middle', 600)
b += text(140, 16, '|x − a| = d', 13, 'middle', 600)
sek = svg(280, 108, 'Sayı doğrusunda a noktasına d uzaklıkta iki nokta: a − d ve a + d', b)
kart("mat-mutlak-deger-03", "Mutlak değer ve uzaklık",
 "Uzaklık ve sapma bilgisini mutlak değerli denkleme çevirip her iki durumu da çözebilmeni.",
 "|x − a|, sayı doğrusunda x ile a arasındaki **uzaklıktır**. |x − a| = d ise x, a'nın **hem sağında hem solunda** d uzaklıktadır. İki durumu da çöz, değerleri kontrol et; soru toplamı mı farkı mı soruyor, ona bak.",
 "|x − a| = d  ⇒  x = a − d  ya da  x = a + d", sek,
 "Bir noktanın 5'e uzaklığı, −1'e uzaklığının 2 katıdır. Bu noktaların toplamı kaçtır?",
 ["Denklem: |x − 5| = 2|x + 1|", "Durum 1: x − 5 = 2x + 2, x = −7. Durum 2: x − 5 = −2x − 2, x = 1", "Kontrol: |−12| = 2·|−6| ve |−4| = 2·|2|", "Toplam: −7 + 1 = −6"],
 "−6",
 "Yalnız tek çözümü (sağdakini ya da soldakini) bulmak, toplam yerine fark almak. Kontrol: her çözümün uzaklığını sayı doğrusunda say.",
 "Uzaklık iki yöne de gidebilir.")

# 12 --------------------------------------------------------------
pay = [Fraction(1, 3), Fraction(1, 4), Fraction(1, 6)]
t = sum(pay)
paylar = [2700 * p / t for p in pay]
assert paylar == [1200, 900, 600] and sum(paylar) == 2700
kart("mat-oran-oranti-01", "Orantılı paylaştırma",
 "Doğru ya da ters orantılı paylaştırmada payları parça sayısı üzerinden bulabilmeni.",
 "**Doğru orantıda** paylar sayıların kendisiyle (2k, 3k), **ters orantıda** tersiyle (k/2, k/3) yazılır; paydaları eşitleyip oranı sadeleştir. Verilen bilgiyi **kaç parçaya** denk geldiğine böl, sonra istenen payı bul.",
 "doğru: a·k, b·k   ters: k/a, k/b", None,
 "3, 4 ve 6 gün çalışan üç kişiye, çalışma süreleriyle ters orantılı olarak 2700 TL paylaştırılıyor. En çok pay alan kaç TL alır?",
 ["Ters orantı: 1/3 : 1/4 : 1/6, paydaları 12'de eşitle: 4 : 3 : 2", "Toplam 9 parça: 2700 ÷ 9 = 300 TL", "En çok pay (4 parça): 4 · 300 = 1200"],
 "1200 TL",
 "Ters orantıda süreyle doğru orantılı bölmek (çok çalışana çok vermek) ya da başka bir kişinin payını yazmak. Kontrol: ters orantıda süresi az olan çok alır.",
 "Ters orantıda önce tersini al.")

# 13 --------------------------------------------------------------
oran = Fraction(32, 20)
yeni_h = 15 * oran
assert yeni_h == 24 and 2 * (32 + yeni_h) == 112
kart("mat-oran-oranti-03", "Benzerlik ve günlük orantı",
 "Ölçek, büyütme, karışım ve tarif gibi günlük durumlarda orantıyı doğru kurabilmeni.",
 "Benzer büyütmede **her kenar aynı sayıyla çarpılır**; toplamsal artış benzerlik değildir. Karışımda “a : b” toplamı a + b parçaya böler. Orantıyı kurarken **aynı cinsi aynı cinse** karşılık getir; çevre için önce yeni kenarları bul.",
 "yeni kenar = eski kenar × büyütme oranı", None,
 "20 cm × 15 cm'lik bir fotoğraf, en-boy oranı bozulmadan genişliği 32 cm olacak biçimde büyütülüyor. Yeni çevre kaç cm olur?",
 ["Büyütme oranı: 32 ÷ 20 = 1,6", "Yeni yükseklik: 15 · 1,6 = 24 cm", "Çevre: 2 · (32 + 24) = 112 cm"],
 "112 cm",
 "Oranı ters kurmak, yalnız bir kenarı büyütmek ya da çevre yerine yarım çevreyi yazmak. Kontrol: büyütmede iki kenar da artmalı.",
 "Her kenar aynı sayıyla çarpılır.")

# 14 --------------------------------------------------------------
from decimal import Decimal as D
arl = D('2.4') / (7 - 1)
assert arl == D('0.4') and arl * 4 == D('1.6')
b = line(30, 50, 250, 50, 'var(--ink)', 3)
for i in range(7):
    xi = 30 + i * 220 / 6
    b += line(xi, 40, xi, 60, 'var(--ink)', 2) + text(round(xi, 1), 80, str(i + 1), 12, 'middle', 600)
b += line(30, 24, 250, 24, 'var(--brand)', 2) + text(140, 16, '2,4 m = 6 aralık', 12, 'middle', 600)
b += text(140, 104, '7 nesne, 6 aralık', 12, 'middle')
sek = svg(280, 114, 'Rafta eşit aralıklı 7 kitap; iki uç arasında 6 aralık var', b)
kart("mat-rasyonel-sayilar-01", "Ondalık sayılar ve aralık sayma",
 "Ondalık uzunlukları eşit aralıklara bölüp nesnelerin konumunu doğru bulabilmeni.",
 "Uçlar dahil dizilimde n nesne arasında **n − 1 aralık** vardır; **k. nesne k − 1 aralık ötededir**. Toplam uzunluğu aralık sayısına böl, konum için aralığı **k − 1 ile çarp**. Ondalık sayı doğrusunda her çizgi 0,1 artar.",
 "aralık = uzunluk ÷ (n − 1)", sek,
 "2,4 m'lik rafa, iki ucu dahil 7 kitap eşit aralıkla diziliyor. 5. kitap sol uçtan kaç m ötededir?",
 ["Aralık sayısı: 7 − 1 = 6", "Bir aralık: 2,4 ÷ 6 = 0,4 m", "5. kitap 4 aralık ötede: 4 · 0,4 = 1,6 m"],
 "1,6 m",
 "Aralık sayısını nesne sayısı kadar almak ya da k. nesneyi k aralık ötede sanmak. Kontrol: ilk nesne 0. konumdadır, aralık bir eksiktir.",
 "Nesne sayısından bir eksik aralık.")

# 15 --------------------------------------------------------------
A, B = Fraction(1, 4), Fraction(7, 4)
par = (B - A) / 4
assert par == Fraction(3, 8) and A + 2 * par == 1
b = line(30, 50, 250, 50, 'var(--ink)', 2.5)
for i in range(5):
    xi = 30 + i * 55
    b += circ(xi, 50, 5, 'var(--rule)' if i in (0, 4) else 'var(--card)', 'var(--ink)', 2)
    b += text(xi, 30, 'A' if i == 0 else ('B' if i == 4 else str(i + 1)), 13, 'middle', 600)
b += text(30, 76, '1/4', 12, 'middle') + text(250, 76, '7/4', 12, 'middle')
b += text(140, 100, '5 nokta = 4 parça', 12, 'middle', 600)
sek = svg(280, 110, 'Sayı doğrusunda A ile B arasında eşit aralıklı 5 nokta, 4 parça', b)
kart("mat-rasyonel-sayilar-03", "Sayı doğrusunda eşit parçalar",
 "İki kesir arasındaki eşit aralıklı noktanın değerini parça sayısını doğru sayarak bulabilmeni.",
 "Bir parça = (büyük − küçük) ÷ parça sayısı. **Parça sayısı nokta sayısından bir eksiktir**: uçlar dahil 6 nokta 5 parça demektir. Paydaları eşitleyerek çalış; istenen noktaya başlangıçtan **kaç parça gittiğini** say.",
 "parça = (B − A) ÷ parça sayısı", sek,
 "Sayı doğrusunda A = 1/4 ile B = 7/4 arasında, uçlar dahil 5 nokta eşit aralıklıdır. Soldan sayılınca (A birinci nokta) 3. nokta kaçtır?",
 ["Parça sayısı: 5 − 1 = 4", "Bir parça: (7/4 − 1/4) ÷ 4 = 3/2 ÷ 4 = 3/8", "3. nokta A'dan 2 parça ötede: 1/4 + 2 · 3/8 = 1/4 + 3/4 = 1"],
 "1",
 "Nokta sayısını parça sayısı almak (5'e bölmek) ya da başlangıcı 0 sanmak. Kontrol: son noktaya vardığında B'yi bulmalısın.",
 "Nokta sayısından bir eksik parça.")

# 16 --------------------------------------------------------------
sayi = [10 * a + c for a in range(1, 10) for c in range(10) if (10 * a + c) - (10 * c + a) == 27 and a + c == 9]
assert sayi == [63]
kart("mat-sayi-basamaklari-01", "Basamak çözümleme",
 "Sayıları basamak değerleriyle yazıp rakam koşullarından denklem kurabilmeni.",
 "İki basamaklı AB = **10A + B**, üç basamaklı ABC = **100A + 10B + C**. Rakamlar yer değiştirince fark ve toplam çözümlemeden çıkar: **AB − BA = 9(A − B)**, AB + BA = 11(A + B). Önce çözümle, sonra rakamları bul.",
 "AB − BA = 9 · (A − B)", None,
 "İki basamaklı bir sayının rakamları yer değiştirince sayı 27 azalıyor. Rakamları toplamı 9 ise sayı kaçtır?",
 ["Çözümle: 10A + B − (10B + A) = 9(A − B) = 27, yani A − B = 3", "A + B = 9 ve A − B = 3 ⇒ A = 6, B = 3", "Sayı 63"],
 "63",
 "Rakam farkıyla sayı farkını karıştırmak (27 farkını rakam farkı sanmak). Kontrol: bulduğun sayıyı ters çevirip farkı hesapla.",
 "Fark 9'un, toplam 11'in katıdır.")

# 17 --------------------------------------------------------------
say = [n for n in range(10, 100) if n // 10 + n % 10 == 11]
assert len(say) == 8
kart("mat-sayi-basamaklari-03", "Rakam koşullu sayma",
 "Koşula uyan sayıları sistemli listeleyip hiçbirini atlamadan ya da iki kez saymadan sayabilmeni.",
 "Önce **baştaki rakamı sabitle**, sonra kalan rakamın seçeneklerini yaz; **başa 0 gelmez**. AB ile BA ayrı sayılardır. 60, 70 gibi birler basamağı 0 olan sayıları da unutma. Listeni baş rakama göre sırala.",
 "önce baş rakam, sonra diğerleri", None,
 "Rakamları toplamı 11 olan iki basamaklı kaç sayı vardır?",
 ["Onlar basamağı 2 ile başla (1 olursa birler 10 gerekir): 29", "Sistemli yaz: 29, 38, 47, 56, 65, 74, 83, 92", "Sayı: 8"],
 "8 sayı",
 "Bir sayıyı atlamak ya da AB ile BA'yı aynı sayıp yalnız birini saymak. Kontrol: baş rakamı 2'den 9'a kadar tek tek yazdın mı?",
 "Baş rakamı sabitle, sonra say.")

# 18 --------------------------------------------------------------
def asal(n): return n > 1 and all(n % i for i in range(2, int(n ** .5) + 1))
cift = [(p, 19 - p) for p in range(2, 18) if asal(p) and asal(19 - p)]
assert cift == [(2, 17), (17, 2)]
kart("mat-temel-kavramlar-01", "Asal sayılar ve faktöriyel",
 "Asal sayıları doğru ayırıp tek-çift özelliğini kullanabilmeni.",
 "Asal sayı **1'den büyük** olup yalnız 1'e ve kendisine bölünür. **1 asal değildir**, 2 tek çift asal sayıdır. 51, 57, 91 asal değildir. İki asalın toplamı tekse biri 2'dir. Izgarada yolları üstten ve soldan **toplayarak** say.",
 "2 tek çift asal sayıdır", None,
 "İki asal sayının toplamı 19 ise çarpımı kaçtır?",
 ["Toplam tek, o hâlde sayılardan biri çift: yani 2", "Öteki: 19 − 2 = 17, asaldır", "Çarpım: 2 · 17 = 34"],
 "34",
 "1'i asal saymak ya da 51, 57 gibi 3'e bölünen sayıları asal sanmak. Kontrol: 2, 3, 5, 7'ye bölünüp bölünmediğine bak.",
 "1 asal değil, 2 tek çifttir.")

# 19 --------------------------------------------------------------
Bf = lambda n: n * (n + 1) // 2
assert Bf(10) - Bf(7) == 27 == 8 + 9 + 10
b = ''
for rr in range(1, 5):
    for cc in range(rr):
        b += '<rect x="%d" y="%d" width="30" height="22" fill="var(--brand-soft)" stroke="var(--brand)" stroke-width="1.5"/>' % (40 + cc * 30, 14 + (rr - 1) * 24)
    b += text(40 + rr * 30 + 8, 30 + (rr - 1) * 24, '%d blok' % rr, 12)
b += text(140, 128, 'B(4) = 1 + 2 + 3 + 4 = 10', 13, 'middle', 600)
sek = svg(280, 138, '4 basamaklı yapıda satırlarda 1, 2, 3, 4 blok var', b)
kart("mat-temel-kavramlar-03", "Tanımlı işlem ve basamaklı yapılar",
 "Verilen kuralı ya da örüntüyü çözüp tanımlı gösterimle istenen değeri hesaplayabilmeni.",
 "Tanımlı işlemde **kuralı küçük bir örnekle dene**, sonra istenen sayıları yerine koy. Basamaklı yapıda blok sayısı **1 + 2 + … + n = n(n + 1)/2**'dir. İki şeklin farkı, aradaki basamakların toplamına eşittir.",
 "B(n) = n(n + 1) / 2", sek,
 "B(n), n basamaklı yapıdaki blok sayısıdır. B(10) − B(7) kaçtır?",
 ["B(10) = 10 · 11 / 2 = 55", "B(7) = 7 · 8 / 2 = 28", "Fark: 55 − 28 = 27 (8 + 9 + 10 ile aynı)"],
 "27",
 "Yarım çarpımı unutup n(n + 1) almak ya da farkta başlangıç şeklini de saymak. Kontrol: B(3) = 6 ile formülü dene.",
 "Fark, aradaki basamakların toplamıdır.")

# 20 --------------------------------------------------------------
poz = sum(v for v in [-4, 3, -7, 5] if v > 0); neg = sum(v for v in [-4, 3, -7, 5] if v < 0)
assert (poz, neg) == (8, -11) and poz - neg == 19
XX = lambda v: 20 + (v + 12) * 240 / 21
b = line(20, 60, 262, 60, 'var(--ink)', 2)
for v in range(-12, 10, 4):
    b += line(XX(v), 54, XX(v), 66, 'var(--ink)', 1.5) + text(round(XX(v), 1), 84, str(v).replace('-', '−'), 11, 'middle')
b += circ(round(XX(-11), 1), 60, 5, 'var(--warn)', 'var(--warn)') + circ(round(XX(8), 1), 60, 5, 'var(--brand)', 'var(--brand)')
b += line(round(XX(-11), 1), 36, round(XX(8), 1), 36, 'var(--rule)', 2.5)
b += text(140, 28, '8 − (−11) = 19', 13, 'middle', 600) + text(round(XX(-11), 1), 106, '−11', 12, 'middle', 600) + text(round(XX(8), 1), 106, '8', 12, 'middle', 600)
sek = svg(280, 116, 'Sayı doğrusunda −11 ile 8 arasındaki uzaklık 19', b)
kart("mat-temel-kavramlar-05", "Sayı doğrusu ve işaret",
 "Negatif ve pozitif değerleri okuyup işaret kurallarıyla toplam ve farkı doğru hesaplayabilmeni.",
 "0'ın altı negatiftir. İki değerin farkı **büyükten küçük çıkarılarak** bulunur; **negatif sayıyı çıkarırsan işaret + olur**. Koordinat bölgelerinde işaretler: I (+,+), II (−,+), III (−,−), IV (+,−). Çarpımda işaretler çarpılır.",
 "a − (−b) = a + b", sek,
 "Dört günün sıcaklıkları −4, 3, −7 ve 5 °C'dir. Negatif sıcaklıkların toplamı, pozitiflerin toplamından kaç derece azdır?",
 ["Pozitifler: 3 + 5 = 8", "Negatifler: −4 + (−7) = −11", "Fark: 8 − (−11) = 8 + 11 = 19"],
 "19 derece",
 "Negatif toplamın işaretini yok sayıp 8 − 11 yazmak ya da −11 − 8 almak. Kontrol: iki nokta arasındaki mesafeyi sayı doğrusunda say.",
 "Büyükten küçüğü çıkar.")

# 21 --------------------------------------------------------------
xv = 5
assert Fraction(xv ** 2 - 9, xv ** 2 + 6 * xv + 9) == Fraction(xv - 3, xv + 3)
kart("mat-carpanlara-ayirma-01", "Rasyonel ifadeyi sadeleştirme",
 "Pay ve paydayı çarpanlarına ayırıp ortak çarpanları sadeleştirebilmeni.",
 "Pay ve paydayı **ayrı ayrı çarpanlarına ayır**: ortak çarpan, iki kare farkı a² − b² = (a − b)(a + b), tam kare a² + 2ab + b² = (a + b)². Sonra yalnız **çarpan olan** ifadeleri sadeleştir; toplam hâlindeki terimler sadeleşmez.",
 "a² − b² = (a − b)(a + b)", None,
 "(x² − 9) / (x² + 6x + 9) ifadesini sadeleştir.",
 ["Pay iki kare farkı: x² − 9 = (x − 3)(x + 3)", "Payda tam kare: x² + 6x + 9 = (x + 3)²", "Bir (x + 3) sadeleşir: (x − 3) / (x + 3)"],
 "(x − 3) / (x + 3)",
 "x² gibi terimleri sadeleştirmek ya da tam kareyi tek çarpan saymak. Kontrol: yalnız çarpım hâlindeki ortak parantezler sadeleşir.",
 "Önce çarpanlara ayır, sonra sadeleştir.")

# 22 --------------------------------------------------------------
assert 63 ** 2 - 37 ** 2 == 26 * 100 == 2600
kart("mat-carpanlara-ayirma-03", "İki kare farkı ve tam kare",
 "Özdeşlikleri kullanarak büyük sayıların hesabını ve toplam–çarpım ilişkilerini çözebilmeni.",
 "**a² − b² = (a − b)(a + b)**; (a ± b)² = a² ± 2ab + b². Toplamı yuvarlak olan iki sayının kareleri farkı, tek çarpmaya iner. a + b ile a² + b² verilirse **2ab = (a + b)² − (a² + b²)** ile çarpımı bul.",
 "(a + b)² = a² + b² + 2ab", None,
 "63² − 37² işleminin sonucu kaçtır?",
 ["İki kare farkı: (63 − 37)(63 + 37)", "= 26 · 100", "= 2600"],
 "2600",
 "Yalnız a − b'yi bulup a + b ile çarpmayı unutmak ya da a² − b² yerine (a − b)² yazmak. Kontrol: sonuç iki çarpanın çarpımı olmalı.",
 "Fark çarpı toplam.")

# 23 --------------------------------------------------------------
assert abs(1.2e5 / 4e2 - 300) < 1e-9
kart("mat-uslu-sayilar-01", "Bilimsel gösterimde oran",
 "Bilimsel gösterimli iki büyüklüğün oranını katsayıları ve 10'un kuvvetlerini ayrı ayrı işleyerek bulabilmeni.",
 "a × 10ⁿ biçiminde (1 ≤ a < 10) sayılarda **katsayılar kendi arasında, 10'un kuvvetleri kendi arasında** işlenir. Bölmede **üsler çıkarılır**, çarpmada toplanır. Tabloda doğru satırı okuduğundan emin ol.",
 "10ᵐ ÷ 10ⁿ = 10ᵐ⁻ⁿ", None,
 "(1,2 × 10⁵) ÷ (4 × 10²) işleminin sonucunu bilimsel gösterimle yaz.",
 ["Katsayılar: 1,2 ÷ 4 = 0,3", "10'un kuvvetleri: 10⁵ ÷ 10² = 10³, yani 0,3 × 10³", "Düzenle (1 ≤ a < 10): 3 × 10²"],
 "3 × 10²",
 "Yalnız katsayıları bölmek, 10'un kuvvetlerini unutmak ya da üsleri çıkarmak yerine toplamak. Kontrol: sonucu 1 ≤ a < 10 olacak biçimde yaz.",
 "Katsayı katsayıyla, kuvvet kuvvetle.")

# 24 --------------------------------------------------------------
assert Fraction(160) * Fraction(1, 2) ** 4 == 10
b = ''
nodes = {0: [140], 1: [90, 190], 2: [65, 115, 165, 215]}
ys = {0: 22, 1: 66, 2: 110}
for lv, xs in nodes.items():
    if lv > 0:
        for i, xv_ in enumerate(xs):
            par_x = nodes[lv - 1][i // 2]
            b += line(par_x, ys[lv - 1] + 9, xv_, ys[lv] - 9, 'var(--muted)', 1.5)
for lv, xs in nodes.items():
    for xv_ in xs:
        b += circ(xv_, ys[lv], 9, 'var(--brand-soft)', 'var(--brand)', 2)
    b += text(6, ys[lv] + 4, '%d. adım' % lv, 11)
b += text(158, 26, '1 hücre', 11) + text(206, 70, '2 hücre', 11) + text(228, 114, '4', 11)
b += text(140, 142, 'değer = 1 · 2ⁿ', 13, 'middle', 600)
sek = svg(280, 152, 'Her adımda ikiye bölünen hücre ağacı: 1, 2, 4 hücre', b)
kart("mat-uslu-sayilar-03", "Katlanarak artma ve azalma",
 "Her adımda sabit katına çıkan ya da küçülen niceliğin n adım sonraki değerini üslü ifadeyle bulabilmeni.",
 "Her adımda değer **r katına** çıkıyorsa n adım sonra değer **başlangıç × rⁿ** olur. Başlangıç değeri ayrı bir çarpan olarak kalır. Adımları dikkatle say: ilk adım da bir adımdır. Azalmada r bir kesirdir, örneğin 1/2.",
 "değer = başlangıç × rⁿ", sek,
 "160 mg'lık bir madde her saat yarıya iniyor. 4 saat sonra kaç mg kalır?",
 ["Çarpan r = 1/2, adım sayısı n = 4", "160 × (1/2)⁴ = 160 × 1/16", "= 10"],
 "10 mg",
 "Üs almak yerine çarpmak (4 × 1/2), başlangıç değerini unutmak ya da adım sayısını bir eksik saymak. Kontrol: 1 adım sonrasını elle hesapla.",
 "Başlangıç çarpı çarpanın kuvveti.")

# 25 --------------------------------------------------------------
assert 2 ** 5 * 4 ** 3 // 8 ** 2 == 32 and 4 ** 3 == 2 ** 6 and 8 ** 2 == 2 ** 6
kart("mat-uslu-sayilar-05", "Üslü ifadelerde işlem kuralları",
 "Aynı tabanlı üslü ifadelerde çarpma, bölme ve sadeleştirme kurallarını doğru uygulayabilmeni.",
 "Aynı tabanda **çarpmada üsler toplanır**, **bölmede çıkarılır**, kuvvetin kuvvetinde çarpılır. Taban farklıysa önce **tabanları eşitle** (16 = 2⁴). Toplamlarda ortak çarpanı parantezle dışarı al. Negatif üs tersini alır: a⁻ⁿ = 1/aⁿ.",
 "aᵐ × aⁿ = aᵐ⁺ⁿ · aᵐ ÷ aⁿ = aᵐ⁻ⁿ · (aᵐ)ⁿ = aᵐⁿ", None,
 "(2⁵ × 4³) ÷ 8² işleminin sonucu kaçtır?",
 ["Tabanı 2 yap: 4³ = (2²)³ = 2⁶ ve 8² = (2³)² = 2⁶", "Çarpma: 2⁵ × 2⁶ = 2¹¹; bölme: 2¹¹ ÷ 2⁶ = 2⁵", "2⁵ = 32"],
 "32",
 "Üssü (5) cevap sanmak ya da farklı tabanlı sayıların üslerini doğrudan toplamak. Kontrol: sonunda istenen sayıyı (2⁵ gibi) hesapladın mı?",
 "Taban aynıysa üsler işlem yapar.")

# ---- doğrulama ----
girdi_ids = re.findall(r'^### (\S+) \|', open(GIRDI, encoding='utf-8').read(), re.M)
wc = lambda s: len(s.replace('**', '').split())
ZORUNLU = ["id", "k", "baslik", "olcer", "kural", "formul", "sekil", "ornek", "hata", "akilda"]
for c in cards:
    for f in ZORUNLU: assert f in c, (c['id'], f)
    for f in ["id", "k", "baslik", "olcer", "kural", "hata", "akilda"]: assert c[f], (c['id'], f)
    assert wc(c['baslik']) <= 6, (c['id'], 'baslik')
    assert wc(c['olcer']) <= 25 and not c['olcer'].startswith('Bu soru'), (c['id'], 'olcer', wc(c['olcer']))
    assert wc(c['kural']) <= 60, (c['id'], 'kural', wc(c['kural']))
    assert wc(c['hata']) <= 40, (c['id'], 'hata', wc(c['hata']))
    assert wc(c['akilda']) <= 8 and not re.search(r'["“”]', c['akilda']), (c['id'], 'akilda')
    o = c['ornek']; assert o['soru'] and o['cevap'] and 2 <= len(o['adimlar']) <= 4, c['id']
    if c['sekil']: assert len(c['sekil'].encode()) <= 25000
ids = [c['id'] for c in cards]
assert sorted(ids) == sorted(girdi_ids) and len(set(ids)) == len(ids), set(girdi_ids) ^ set(ids)
json.dump(cards, open(CIKTI, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(cards), 'kart,', sum(1 for c in cards if c['sekil']), 'şekilli')
for c in cards:
    if c['sekil']:
        s = c['sekil'].replace('var(--ink)', '#18212f').replace('var(--muted)', '#5b6678').replace('var(--card)', '#ffffff') \
            .replace('var(--brand-soft)', '#e7edff').replace('var(--brand)', '#2f5bea').replace('var(--rule-soft)', '#e3f5ef') \
            .replace('var(--rule)', '#0f8a6a').replace('var(--warn)', '#c2410c')
        s = s.replace('<svg ', '<svg style="background:#fff" ', 1)
        open('/tmp/kor/kart/p11/%s.svg' % c['id'], 'w', encoding='utf-8').write(s)
