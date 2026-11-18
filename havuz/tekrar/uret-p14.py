# -*- coding: utf-8 -*-
import sys, re, json, math, itertools
from fractions import Fraction as F
sys.path.insert(0, '/home/claude/zekacademy-app/havuz')

GIRDI = '/tmp/kor/kart/parti/p14.txt'
CIKTI = '/home/claude/zekacademy-app/havuz/tekrar/kart-p14.json'
BLUE, GREEN, ORG = '#2f5bea', '#0f8a6a', '#c2410c'

def svg(govde, h=170):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 %d" role="img" aria-label="%s" '
            'font-family="sans-serif" font-size="12" fill="currentColor" stroke="none">%s</svg>')

def sv(aria, govde, h=170):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 %d" role="img" aria-label="%s" '
            'font-family="sans-serif" font-size="12">%s</svg>' % (h, aria, govde))

def T(x, y, s, size=12, col='currentColor', w='normal', anchor='start'):
    return '<text x="%s" y="%s" font-size="%s" fill="%s" font-weight="%s" text-anchor="%s">%s</text>' % (x, y, size, col, w, anchor, s)

def arrow(x1, y1, x2, y2, col):
    a = math.atan2(y2 - y1, x2 - x1); L = 8
    p1 = (x2 - L * math.cos(a - .45), y2 - L * math.sin(a - .45))
    p2 = (x2 - L * math.cos(a + .45), y2 - L * math.sin(a + .45))
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="2.5"/>'
            '<polygon points="%s,%s %.1f,%.1f %.1f,%.1f" fill="%s"/>') % (x1, y1, x2, y2, col, x2, y2, p1[0], p1[1], p2[0], p2[1], col)

# ---------- şekiller ----------
def pie():
    cx, cy, r = 140, 85, 72
    sl = [(90, BLUE, 'A 90°'), (120, GREEN, 'B 120°'), (150, ORG, 'C 150°')]
    assert sum(s[0] for s in sl) == 360
    a0 = -90.0; out = ''
    for ang, col, lab in sl:
        a1 = a0 + ang
        p = lambda a: (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
        x0, y0 = p(a0); x1, y1 = p(a1)
        big = 1 if ang > 180 else 0
        out += '<path d="M%s,%s L%.1f,%.1f A%s,%s 0 %d 1 %.1f,%.1f Z" fill="%s" stroke="#ffffff" stroke-width="2"/>' % (cx, cy, x0, y0, r, r, big, x1, y1, col)
        m = math.radians(a0 + ang / 2)
        out += T('%.1f' % (cx + r * .6 * math.cos(m)), '%.1f' % (cy + r * .6 * math.sin(m) + 4), lab, 12, '#ffffff', '600', 'middle')
        a0 = a1
    return sv('Daire grafiği: A dilimi 90 derece, B dilimi 120 derece, C dilimi 150 derece', out)

def cizgi():
    vals = [150, 200, 180, 170, 190]; gun = ['Pzt', 'Sal', 'Çar', 'Per', 'Cum']
    o = '<line x1="40" y1="140" x2="262" y2="140" stroke="currentColor" stroke-width="1.5"/><line x1="40" y1="140" x2="40" y2="20" stroke="currentColor" stroke-width="1.5"/>'
    for v in (0, 100, 200):
        y = 140 - v * .5
        o += '<line x1="40" y1="%s" x2="262" y2="%s" stroke="currentColor" stroke-opacity=".25" stroke-dasharray="3 3"/>' % (y, y)
        o += T(8, y + 4, v, 11)
    pts = [(60 + i * 48, 140 - v * .5) for i, v in enumerate(vals)]
    o += '<polyline points="%s" fill="none" stroke="%s" stroke-width="2.5"/>' % (' '.join('%s,%s' % p for p in pts), BLUE)
    for (x, y), g in zip(pts, gun):
        o += '<circle cx="%s" cy="%s" r="4" fill="%s"/>' % (x, y, BLUE) + T(x, 156, g, 11, anchor='middle')
    return sv('Çizgi grafiği: beş günlük değerler noktalarla gösterilmiş', o, 165)

def nehir():
    o = '<rect x="20" y="40" width="240" height="90" rx="8" fill="%s" fill-opacity=".15" stroke="%s"/>' % (BLUE, BLUE)
    o += arrow(30, 55, 110, 55, BLUE) + T(120, 59, 'akıntı (a)', 12, BLUE)
    o += arrow(60, 85, 220, 85, GREEN) + T(140, 78, 'v + a', 13, GREEN, '600', 'middle')
    o += arrow(220, 112, 60, 112, ORG) + T(140, 126, 'v − a', 13, ORG, '600', 'middle')
    return sv('Nehirde akıntı yönünde giden tekne hızlı, akıntıya karşı giden tekne yavaş gider', o, 150)

def pist():
    o = '<circle cx="140" cy="85" r="55" fill="none" stroke="currentColor" stroke-width="2"/>'
    o += arrow(110, 30, 170, 30, GREEN) + T(140, 20, 'A', 13, GREEN, '600', 'middle')
    o += arrow(170, 140, 110, 140, ORG) + T(140, 158, 'B', 13, ORG, '600', 'middle')
    o += T(140, 90, 'bir tur = çevre', 12, anchor='middle')
    return sv('Dairesel pist; A ve B koşucuları zıt yönde ilerliyor', o, 170)

def yol():
    o = '<line x1="30" y1="95" x2="250" y2="95" stroke="currentColor" stroke-width="2"/>'
    o += '<circle cx="30" cy="95" r="5" fill="currentColor"/><circle cx="250" cy="95" r="5" fill="currentColor"/>'
    o += T(30, 120, 'A', 13, anchor='middle', w='600') + T(250, 120, 'B', 13, anchor='middle', w='600')
    o += arrow(36, 70, 130, 70, GREEN) + T(40, 58, 'hız 1', 12, GREEN)
    o += arrow(244, 70, 150, 70, ORG) + T(212, 58, 'hız 2', 12, ORG)
    o += '<line x1="140" y1="62" x2="140" y2="102" stroke="currentColor" stroke-dasharray="3 3"/>' + T(140, 140, 'karşılaşma noktası', 12, anchor='middle')
    return sv('A ve B noktalarından birbirine doğru çıkan iki hareketli yolda karşılaşıyor', o, 160)

def serit():
    o = ''
    for i in range(8):
        fill = 'fill="%s" fill-opacity=".45"' % GREEN if i < 3 else 'fill="none"'
        o += '<rect x="%s" y="40" width="28" height="36" %s stroke="currentColor" stroke-width="1.5"/>' % (30 + i * 28, fill)
    o += '<line x1="30" y1="92" x2="114" y2="92" stroke="%s" stroke-width="2.5"/>' % GREEN + T(30, 110, '3 parça = X', 12, GREEN, '600')
    o += '<line x1="30" y1="128" x2="254" y2="128" stroke="currentColor" stroke-width="2"/>' + T(142, 146, 'bütün = 8 parça', 12, anchor='middle', w='600')
    return sv('Bütün sekiz eş parçaya bölünmüş; üç parça gösterilmiş', o, 160)

def kuyruk():
    o = ''
    for i in range(8):
        col = ORG if i == 2 else 'none'
        o += '<circle cx="%s" cy="75" r="11" fill="%s" stroke="currentColor" stroke-width="1.5"/>' % (30 + i * 30, col)
    o += '<line x1="30" y1="100" x2="90" y2="100" stroke="%s" stroke-width="2.5"/>' % GREEN + T(60, 118, 'baştan 3', 12, GREEN, '600', 'middle')
    o += '<line x1="90" y1="48" x2="240" y2="48" stroke="%s" stroke-width="2.5"/>' % BLUE + T(165, 38, 'sondan 6', 12, BLUE, '600', 'middle')
    o += T(140, 150, '3 + 6 − 1 = 8 kişi', 13, anchor='middle', w='600')
    return sv('Sekiz kişilik kuyrukta üçüncü kişi baştan 3., sondan 6. sıradadır', o, 165)

def yuzde():
    o = ''; x = 30
    for p, col, lab in [(35, BLUE, '%35'), (25, GREEN, '%25'), (40, ORG, '?')]:
        w = 220 * p / 100
        o += '<rect x="%s" y="55" width="%s" height="40" fill="%s"/>' % (x, w, col) + T(x + w / 2, 80, lab, 14, '#ffffff', '600', 'middle')
        x += w
    o += '<line x1="30" y1="112" x2="250" y2="112" stroke="currentColor" stroke-width="2"/>' + T(140, 132, 'toplam = %100', 12, anchor='middle', w='600')
    return sv('Yüzde şeridi: iki dilimin yüzdesi verilmiş, üçüncü dilim bilinmiyor', o, 150)

# ---------- kartlar ----------
K = []
def kart(id, baslik, olcer, kural, formul, sekil, soru, adimlar, cevap, hata, akilda):
    K.append(dict(id=id, baslik=baslik, olcer=olcer, kural=kural, formul=formul, sekil=sekil,
                  ornek=dict(soru=soru, adimlar=adimlar, cevap=cevap), hata=hata, akilda=akilda))

# 1 daire grafiği
t, a1, a2 = 240, 75, 105
assert t * a1 // 360 == 50 and t * a2 // 360 == 70 and t * (a2 - a1) // 360 == 20
kart('prob-grafik-problemleri-02', 'Daire grafiğinde dilimden sayıya',
 'Dilim açılarını toplam sayıya göre kişi sayısına çevirip dilimleri karşılaştırabildiğini.',
 'Tüm daire **360°**\'dir. Bir dilimin sayısı, toplamın o dilimin açısına oranı kadardır. Birden çok dilim isteniyorsa önce açıları topla ya da farkı al, sonra **tek seferde** sayıya çevir.',
 'dilimin sayısı = toplam × açı ÷ 360', pie(),
 '240 öğrencinin kulüp tercihleri daire grafiğinde gösteriliyor. Müzik dilimi 105°, spor dilimi 75° ise müzik tercih edenler spor tercih edenlerden kaç kişi fazladır?',
 ['Açı farkı: 105° − 75° = 30°', 'Sayıya çevir: 240 × 30 ÷ 360', '240 ÷ 360 × 30 = 20 kişi'], '20 kişi',
 'Dilimin açısını kişi sayısı sanmak ya da tek dilimi bulup soruyu bitmiş saymak. Soru hangi dilim ya da farkı istiyor, bir kez daha oku.',
 'Önce açıyı topla, sonra sayıya çevir.')

# 2 çizgi grafiği
assert (200 - 180) * 100 // 200 == 10
kart('prob-grafik-problemleri-04', 'Çizgi grafiğinde değişim ve yüzde',
 'Noktalardan değerleri okuyup ardışık farkı ve yüzde değişimi doğru hesaplayabildiğini.',
 'Noktadan yatay çizgiyi izleyip dikey eksendeki değeri oku. İki nokta arasındaki **fark** değişimdir. Yüzde değişimde bölen her zaman **eski (önceki) değerdir**, yeni değer değil. Artış mı azalış mı olduğuna işarete bakarak karar ver.',
 'yüzde değişim = fark ÷ eski değer × 100', cizgi(),
 'Bir kafenin günlük satışı pazartesi 150, salı 200, çarşamba 180 TL\'dir. Salıdan çarşambaya satış yüzde kaç değişmiştir?',
 ['Fark: 180 − 200 = −20 (düşüş)', 'Eski değer salıdır: 200', 'Oran: 20 ÷ 200 = 0,10'], '%10 azalış',
 'Farkı yeni değere bölmek ya da düşüşü artış saymak. Bölen önceki gündür; en büyük artış sorusunda da yüzdeyi değil, farkı karşılaştır.',
 'Yüzdede bölen eski değerdir.')

# 3 akıntı
v, a, yol_ = 20, 4, 48
s1, s2 = F(yol_, v + a), F(yol_, v - a)
assert s1 == 2 and s2 == 3 and s1 + s2 == 5
kart('prob-hareket-hiz-01', 'Akıntı yönünde ve karşı hız',
 'Akıntı yönündeki ve akıntıya karşı bölümleri ayrı hızlarla hesaplayıp süreleri toplayabildiğini.',
 'Akıntı yönünde hız **tekne + akıntı**, akıntıya karşı hız **tekne − akıntı**\'dır. Akıntıyla sürüklenen cisim, akıntı hızıyla gider. Her bölümün yolunu kendi hızına böl, süreleri topla.',
 'gidiş: v + a · dönüş: v − a · süre = yol ÷ hız', nehir(),
 'Durgun suda 20 km/sa hızla giden bir tekne, akıntı hızı 4 km/sa olan nehirde A\'dan B\'ye gidip aynı yoldan dönüyor. |AB| = 48 km ise yolculuk kaç saat sürer?',
 ['Gidiş (akıntı yönünde): 20 + 4 = 24 km/sa, süre 48 ÷ 24 = 2 sa', 'Dönüş (akıntıya karşı): 20 − 4 = 16 km/sa, süre 48 ÷ 16 = 3 sa', 'Toplam: 2 + 3 = 5 sa'], '5 saat',
 'Akıntıyı hiç hesaba katmamak ya da dönüşte de akıntı yönünde gittiğini sanmak. Dönüşte hız her zaman daha küçüktür; sonucu bununla kontrol et.',
 'Gidiş ve dönüş hızı ayrıdır.')

# 4 dairesel pist
c, va, vb = 600, 40, 60
assert c % (va + vb) == 0 and 3 * c // (va + vb) == 18
kart('prob-hareket-hiz-03', 'Dairesel pistte karşılaşma ve yetişme',
 'Dairesel pistte aynı ve zıt yönlü hareketlerde doğru hızı (fark ya da toplam) seçebildiğini.',
 'Aynı yönde koşanlar, hızlı olan bir tur fazla attığında yan yana gelir: **hız farkı** kullanılır. Zıt yönde koşanlar toplam yol bir tur olunca karşılaşır: **hız toplamı** kullanılır. Karşılaşmalar eşit aralıklarla olur.',
 'aralık = çevre ÷ hızlar toplamı (zıt yön) · çevre ÷ hız farkı (aynı yön)', pist(),
 'Çevresi 600 m olan pistte iki koşucu aynı noktadan zıt yönde, 40 m/dk ve 60 m/dk hızla başlıyor. Üçüncü kez kaçıncı dakikada karşılaşırlar?',
 ['Zıt yön: hızlar toplanır, 40 + 60 = 100 m/dk', 'İki karşılaşma arası: 600 ÷ 100 = 6 dk', 'Üçüncü karşılaşma: 3 × 6 = 18. dk'], '18. dakika',
 'Zıt yönde giderken hız farkını kullanmak ya da bir koşucunun tur sayısını karşılaşma sayısı sanmak. Soruda yön yazıyorsa önce ona bak.',
 'Zıt yön toplar, aynı yön çıkarır.')

# 5 karşılaşma yetişme
assert 40 * F(3, 2) == 60 and F(60, 60 - 40) == 3
kart('prob-hareket-hiz-05', 'Karşılaşma ve yetişme süresi',
 'Aradaki yolu hızlar toplamı ya da farkıyla kullanıp karşılaşma ve yetişme süresini bulabildiğini.',
 'Birbirine doğru gidenlerde aradaki yol her saat **hızlar toplamı** kadar kısalır. Aynı yönde yetişmede **hız farkı** kullanılır. Biri önce çıktıysa önce onun aldığı yolu hesapla, sonra kalan yolla devam et.',
 'karşılaşma: t = yol ÷ (v₁ + v₂) · yetişme: t = açık ÷ (v₁ − v₂)', yol(),
 'Bir araç 40 km/sa hızla yola çıkıyor. 1,5 saat sonra aynı yerden aynı yöne 60 km/sa hızla ikinci araç çıkıyor. İkinci araç, kendi çıkışından kaç saat sonra birincisine yetişir?',
 ['Birincinin önde aldığı yol: 40 × 1,5 = 60 km', 'Aynı yön: hız farkı 60 − 40 = 20 km/sa', 'Süre: 60 ÷ 20 = 3 sa'], '3 saat',
 'Aynı yönde giderken hızları toplamak ya da birine doğru giderken farkı almak. Önce çıkanın yolunu eklemeyi unutma; yetişme süresi ikinci çıkıştan sayılır.',
 'Karşılaşmada yollar toplanır.')

# 6 fireli alım
mal, br, fire, kar_, ilk, ilkf = 100, 8, 10, 25, 40, 10
mal_ = mal * br; hedef = mal_ * (100 + kar_) // 100; kalan = mal - fire - ilk
assert hedef == 1000 and (hedef - ilk * ilkf) == 600 and 600 / kalan == 12 and kalan == 50
kart('prob-kar-zarar-01', 'Fireli alımda hedef kâr',
 'Satılamayan malın maliyetini de katarak hedef kâr için kalan malın satış fiyatını bulabildiğini.',
 'Kâr, aksi söylenmedikçe **alış fiyatına** göre hesaplanır. Önce tüm maliyeti bul; satılamayan malın parası da maliyete dahildir. Sonra hedef tahsilatı yaz, bildiğin satışları çıkar, kalanı **kalan mala** böl.',
 'hedef tahsilat = toplam maliyet × (100 + kâr%) ÷ 100', None,
 'Kilosu 8 TL\'den 100 kg elma alınıyor. 10 kg çürüyüp satılamıyor. Toplamda %25 kâr hedefleniyor. İlk 40 kg\'ı kilosu 10 TL\'ye satılırsa kalanın kilosu kaç TL olmalıdır?',
 ['Maliyet: 100 × 8 = 800 TL; hedef tahsilat: 800 × 1,25 = 1000 TL', 'İlk satış: 40 × 10 = 400 TL; kalan tahsilat: 1000 − 400 = 600 TL', 'Kalan mal: 100 − 10 − 40 = 50 kg; fiyat 600 ÷ 50 = 12 TL'], '12 TL',
 'Hedefi yalnız satılan malın maliyetine göre kurmak ya da ortalama fiyatı kalanın fiyatı sanmak. Çürüyen malın parası da ödendi, hedefe dahildir.',
 'Önce toplam tahsilatı bul.')

# 7 etiket indirim
et, ind, alis = 400, 25, 250
sat = et * (100 - ind) // 100
assert sat == 300 and (sat - alis) * 100 // alis == 20
kart('prob-kar-zarar-03', 'Etiket, indirim ve kâr',
 'Etiket fiyatından satış fiyatını bulup alış fiyatıyla karşılaştırarak kâr tutarını ve yüzdesini hesaplayabildiğini.',
 '**İndirimli fiyat** = etiket × (100 − indirim%) ÷ 100. Gerçek satış fiyatı indirimli fiyattır. Kâr = **satış − alış**. Kâr yüzdesi alış fiyatına göre bulunur. Faturadaki KDV satıcıya kalmaz.',
 'kâr% = (satış − alış) ÷ alış × 100', None,
 'Alış fiyatı 250 TL olan bir ürünün etiketi 400 TL\'dir. Üründe %25 indirim yapılıp satılıyor. Satıcının kâr yüzdesi kaçtır?',
 ['Satış: 400 × 75 ÷ 100 = 300 TL', 'Kâr: 300 − 250 = 50 TL', 'Yüzde: 50 ÷ 250 × 100 = %20'], '%20',
 'Kâr tutarıyla kâr yüzdesini karıştırmak ya da indirim oranını kâr oranı sanmak. Kârı etiket fiyatından değil, indirimli satıştan hesapla.',
 'Kâr = indirimli satış − alış.')

# 8 alıp yerine koyma
top, o_, al = 200, 20, 50
tuz = top * o_ // 100; tuz2 = tuz - al * o_ // 100; top2 = top - al
assert tuz == 40 and tuz2 == 30 and top2 == 150 and F(tuz2 * 100, 25) == 120 and top2 - 120 == 30
kart('prob-karisim-problemleri-02', 'Alıp yerine koyma ve buharlaştırma',
 'Karışımdan alınan kısımdaki maddeyi ve su eklenince ya da buharlaşınca değişmeyen maddeyi doğru izleyebildiğini.',
 'Karışımdan alınan kısım, o anki oranda madde içerir; bu maddeyi hem maddeden hem toplamdan düş. Su eklenince ya da buharlaşınca **madde miktarı değişmez**, yalnız toplam değişir. Hedef toplamı maddeden bul.',
 'hedef toplam = madde ÷ hedef oran', None,
 '200 g %20\'lik tuzlu sudan 50 g alınıyor. Kalan karışımı %25\'lik yapmak için kaç g su buharlaştırılmalıdır?',
 ['Başta tuz: 200 × 0,20 = 40 g; alınan 50 g\'da tuz 10 g', 'Kalan: 150 g karışım, 40 − 10 = 30 g tuz', 'Hedef toplam: 30 ÷ 0,25 = 120 g; buharlaşan 150 − 120 = 30 g'], '30 g',
 'Alınan kısımdaki maddeyi geri gelecek sanmak ya da yalnız oran farkını toplamla çarpmak. Gidenler geri gelmez, buharlaşmada tuz sabittir.',
 'Buharlaşmada madde sabit kalır.')

# 9 karışımları birleştirme
m1, o1, m2, o2 = 300, 10, 200, 35
x1, x2 = m1 * o1 // 100, m2 * o2 // 100
assert x1 == 30 and x2 == 70 and (x1 + x2) * 100 // (m1 + m2) == 20
kart('prob-karisim-problemleri-04', 'Karışımları birleştirip oran bulma',
 'Karışımların madde ve toplam miktarlarını ayrı ayrı toplayıp yeni oranı bulabildiğini.',
 'Madde ve toplamı **ayrı sütunlarda** izle. Karışımları birleştirince maddeleri topla, toplamları da topla. Eklenen madde hem maddeye hem toplama yazılır. En sonda böl. Oranların ortalamasını **alma**.',
 'yeni oran = toplam madde ÷ toplam karışım', None,
 '300 g %10\'luk ve 200 g %35\'lik iki tuzlu su karıştırılıyor. Yeni karışımın tuz oranı yüzde kaçtır?',
 ['Tuz: 300 × 0,10 = 30 g ve 200 × 0,35 = 70 g', 'Toplam madde: 100 g; toplam karışım: 500 g', 'Oran: 100 ÷ 500 = %20'], '%20',
 'İki oranın düz ortalamasını almak (%22,5 gibi) ya da yeni maddeyi eski toplama bölmek. Miktarlar eşit değilse ortalama yanlış çıkar.',
 'Madde ve toplamı ayrı yaz.')

# 10 kalanın kesri
p = 120
harc1 = p * F(1, 4); kal1 = p - harc1; harc2 = kal1 * F(2, 3); kal2 = kal1 - harc2
assert kal2 == 30 and F(3, 4) * F(1, 3) == F(1, 4)
kart('prob-kesir-problemleri-02', 'Ardışık kalan kesirleri',
 'Kalanın kesrini bütünün kesrinden ayırıp sondan başa doğru geri izleyebildiğini.',
 '“**Kalanın** 2/3\'ü” ifadesi, o ana kadar geriye kalan miktarın kesridir; bütünün değil. Her adımdan sonra bütünün kaçta kaçı kaldığını yaz. Sonra verilen sayıyı bu kesre bölüp **bütüne** geç.',
 'kalan = (1 − 1. kesir) × (1 − 2. kesir)', None,
 'Bir paranın 1/4\'ü harcanıyor, kalanın 2/3\'ü daha harcanıyor ve geriye 30 TL kalıyor. Para kaç TL\'ydi?',
 ['1/4 harcandı, 3/4 kaldı', 'Kalanın 2/3\'ü harcandı, kalanın 1/3\'ü kaldı: 3/4 × 1/3 = 1/4', 'Bütünün 1/4\'ü 30 ise bütün 30 × 4 = 120 TL'], '120 TL',
 'İkinci kesri paranın tamamına uygulamak. “Kalanın” demek bütünün değil, o anki kalanın demektir; sonuçta geri doğrulayarak kontrol et.',
 'Kalan, bütünün parçası değildir.')

# 11 parçadan bütüne
assert F(24, 3) * 8 == 64
kart('prob-kesir-problemleri-04', 'Parçadan bütüne geçiş',
 'Bir kesrin karşılığı verilen sayıdan bütünü bulabildiğini.',
 'Bütünün a/b\'si X ise önce **a\'ya böl**: bütünün 1/b\'si çıkar. Sonra **b ile çarp**: bütün çıkar. İki kesir aynı miktarı ifade ediyorsa eşitleyip ortak bir k değeriyle oranı kur.',
 'bütün = X ÷ a × b', serit(),
 'Bir kitabın 3/8\'i olan 24 sayfa okunmuştur. Kitap kaç sayfadır?',
 ['3 parça 24 sayfa ise 1 parça 24 ÷ 3 = 8 sayfa', 'Bütün 8 parça: 8 × 8 = 64'], '64 sayfa',
 'Sayıyı yalnız paya bölüp bırakmak ya da payla çarpmak. Önce paya böl (bir parça), sonra paydayla çarp (bütün).',
 'Önce paya böl, sonra paydayla çarp.')

# 12 tarife
import math as _m
sure = 3 + 10 / 60; dilim = _m.ceil(sure)
assert dilim == 4 and 20 + (dilim - 1) * 8 == 44
kart('prob-rutin-olmayan-02', 'Tarife ve kural yorumlama',
 'Soruda verilen tarife ya da kuralı eksiksiz uygulayıp tutarı veya tarihi bulabildiğini.',
 'Soruda verilen kuralı **harfiyen** uygula. “Her saat ya da bir kısmı” denince başlanan her birim **tam** ücretlenir. Dilimli tarifede ilk dilimi ayrı, ek dilimleri ayrı hesapla. Takvimde günler **7\'lik** döngüyle tekrar eder.',
 'ücret = ilk dilim + ek dilim sayısı × ek ücret', None,
 'Bir otoparkta ilk saat 20 TL, sonraki her saat ya da bir kısmı 8 TL\'dir. 3 saat 10 dakika park eden araç kaç TL öder?',
 ['3 saat 10 dk, 4. saate girmiş: 4 saat sayılır', 'İlk saat 20 TL, ek saat 4 − 1 = 3', 'Ücret: 20 + 3 × 8 = 44 TL'], '44 TL',
 'Bir kısmını saymamak ya da ilk dilimi unutmak. Tutardan süreye giderken sınır değerleri (tam saat) ayrıca dene.',
 'Başlanan birim tam sayılır.')

# 13 mantık
ks = [p_ for p_ in itertools.permutations('ABCD')
      if p_[0] != 'B' and p_.index('C') == p_.index('A') + 1 and p_[3] == 'D']
assert ks == [('A', 'C', 'B', 'D')]
kart('prob-rutin-olmayan-04', 'Koşullu yerleştirme ve çıkarım',
 'Koşulları tabloya işleyip seçenekleri eleyerek zorunlu yerleşimi bulabildiğini.',
 'Kesin bilgileri önce tabloya yaz. “Sağında” herhangi bir yer, **“hemen sağında”** yan yana demektir. Uç koşulu varsa **iki ucu ayrı ayrı dene**: çelişen durum elenir, kalan kesinleşir. Yan yana kalanları tek blok say.',
 None, None,
 'Dört kişi A, B, C, D soldan sağa sıralanıyor. B en solda değil, C, A\'nın hemen sağında ve D en sağdadır. Soldan 2. sırada kim vardır?',
 ['D en sağda: 4. sıra. Kalan yerler 1, 2, 3', 'A–C yan yana blok; B en solda olamaz, blok 1–2\'ye girer', 'Sıra A, C, B, D'], 'C',
 'Koşulu eksik okuyup “hemen” sözcüğünü yok saymak. Bulduğun sırayı bütün koşullarla tek tek geri kontrol et.',
 'Önce kesin olanı yerleştir.')

# 14 eksik-fazla
x = (7 + 9) // (5 - 3)
assert 3 * x + 7 == 5 * x - 9 == 31 and x == 8
kart('prob-sayi-problemleri-01', 'Eksik–fazla paylaştırma',
 'İki ayrı dağıtımdaki artan ve eksik miktardan kişi ve mal sayısını bulabildiğini.',
 'Mal sayısını iki dağıtımla ayrı ayrı yaz. **Artan** miktar eklenir, **eksik** miktar çıkarılır. İki ifadeyi eşitleyip kişi sayısını bul, sonra mal sayısına geç. Soru kişiyi mi malı mı soruyor, sona bırakma.',
 'kişi × a + artan = kişi × b − eksik', None,
 'Öğrencilere kişi başı 3 kalem verilirse 7 kalem artıyor, 5 kalem verilirse 9 kalem eksik kalıyor. Kaç kalem vardır?',
 ['Kişi sayısı x: 3x + 7 = 5x − 9', '2x = 16, x = 8 öğrenci', 'Kalem: 3 · 8 + 7 = 31'], '31 kalem',
 'Kişi sayısını bulup mal sayısı sanmak ya da artanı cevap vermek. Bulduğun değeri iki dağıtımda da deneyip kontrol et.',
 'Artan eklenir, eksik çıkarılır.')

# 15 sözel → denklem
xs = [x for x in range(-50, 50) if 5 * x - 3 == 2 * (x + 6)]
assert xs == [5]
kart('prob-sayi-problemleri-03', 'Sözel ifadeyi denkleme çevirme',
 'Sözel ifadedeki işlem sırasını koruyarak denklem kurup bilinmeyen sayıyı bulabildiğini.',
 '“**Fazlası**” toplama, “**eksiği**” çıkarma, “**katı**” çarpma demektir. İşlem sırasını sözdeki sırayla koru: “x\'in 5 fazlasının 3 katı” 3(x + 5) olur. İki ifade eşitse denklem kur. Ardışık sayılar x, x + 1, x + 2\'dir.',
 '“x\'in 4 katının 3 eksiği” = 4x − 3', None,
 'Bir sayının 5 katının 3 eksiği, aynı sayının 6 fazlasının 2 katına eşittir. Sayı kaçtır?',
 ['Sol taraf: 5x − 3; sağ taraf: 2(x + 6)', '5x − 3 = 2x + 12', '3x = 15, x = 5'], '5',
 'İşlem sırasını karıştırıp parantezi unutmak ya da eşitliğin değerini sayı sanmak. Sorunun neyi sorduğuna bak ve sonucu denklemde dene.',
 'Fazla toplar, eksik çıkarır.')

# 16 sıra
assert 9 + 6 - 1 == 14 and 12 - 5 - 1 == 6
kart('prob-sayi-problemleri-05', 'Sıra, kuyruk ve periyot',
 'Baştan ve sondan sıradan toplam kişiyi, iki sıra arasındaki kişi sayısını bulabildiğini.',
 'Baştan a., sondan b. sıradaki kişi varsa kuyrukta **a + b − 1** kişi vardır; o kişi iki kez sayıldığı için bir çıkar. Aradaki kişi sayısı **fark − 1**\'dir. Tekrarlayan düzenlerde (gün, kat) **kalanı** kullan.',
 'toplam = baştan + sondan − 1', kuyruk(),
 'Bir kuyrukta Selin baştan 9., sondan 6. sıradadır. Kuyrukta kaç kişi vardır? Baştan 5. ile 12. kişinin arasında kaç kişi vardır?',
 ['Toplam: 9 + 6 − 1 = 14 kişi', 'Aradaki kişi: 12 − 5 − 1 = 6'], '14 kişi; aralarında 6 kişi',
 'Sıra numaralarının farkını aradaki kişi sanmak ya da toplamda Selin\'i iki kez saymak. Önce kişiyi kaç kez saydığına bak.',
 'Ortak kişi iki kez sayılır.')

# 17 yaş grafik/tablo
assert 38 - 10 == 28 and 2 * 28 == 28 + 28
kart('prob-yas-problemleri-02', 'Grafik ve tabloyla yaş problemleri',
 'Grafik ya da tablodaki yaşları okuyup yaş farkı ve toplam ilişkisiyle istenen yaşı bulabildiğini.',
 'Önce grafik ya da tablodan **yaşları oku**, sonra ilişkiyi kur. İki kişinin yaş farkı **hiç değişmez**. n kişinin yaşları toplamı her yıl **n** artar. Zamanı kaydırırken herkese aynı yılı ekle.',
 't yıl sonra toplam = şimdiki toplam + n × t', None,
 'Anne 38, kızı 10 yaşındadır. Anne kızının yaşının 2 katı olduğunda kızı kaç yaşında olur?',
 ['Yaş farkı sabittir: 38 − 10 = 28', 'Anne kızın 2 katıysa fark kızın yaşına eşittir', 'Kız 28 yaşında (anne 56)'], '28 yaş',
 'Yaş farkını zamanla değişiyor sanmak ya da yanlış kişiyi esas almak. Tablodaki hangi yılın yaşı olduğunu ve sorunun kimi sorduğunu işaretle.',
 'Yaş farkı hiç değişmez.')

# 18 yaş farkı kat
xx = [x for x in range(1, 100) if 4 * x + x + 10 == 55]
assert xx == [9] and 4 * 9 == 36
kart('prob-yas-problemleri-04', 'Yaş farkı ve kat ilişkisi',
 'Bugünkü ve gelecekteki kat ya da toplam ilişkilerini kurup istenen kişinin yaşını bulabildiğini.',
 'İki kişinin yaş farkı **hiç değişmez**. Yıl kaydırırken ikisine de aynı sayıyı ekle ya da çıkar. “Katı” ilişkisini hangi zamana ait olduğuna göre kur. İki kişide t yılda toplam **2t** değişir.',
 'fark sabit · toplam değişimi = kişi sayısı × yıl', None,
 'Anne yaşı oğlunun yaşının 4 katıdır. 5 yıl sonra ikisinin yaşları toplamı 55 olacaktır. Annenin bugünkü yaşı kaçtır?',
 ['Bugünkü toplam: 55 − 2 · 5 = 45', 'Oğul x, anne 4x: 5x = 45, x = 9', 'Anne: 4 · 9 = 36'], '36',
 'Gelecekteki yaşı bugünkü sanmak ya da sorulan kişiyi karıştırmak (oğul 9, anne 36). Sonunda sorunun kimi sorduğuna bir kez daha bak.',
 'Her iki yaşa aynı yıl eklenir.')

# 19 ardışık yüzde
net = F(3, 2) * F(3, 5)
assert net == F(9, 10)
kart('prob-yuzde-problemleri-02', 'Ardışık yüzde değişimi',
 'Art arda yüzde değişimlerini çarpanlarla birleştirip net değişimi bulabildiğini.',
 'Her yüzde değişimini **çarpana** çevir: %20 artış × 1,2, %25 azalış × 0,75. Çarpanları art arda çarp; ikinci yüzde **yeni değere** uygulanır. Yüzdeleri toplamak ya da çıkarmak yanlıştır.',
 'net çarpan = çarpan₁ × çarpan₂', None,
 'Bir ürünün fiyatı önce %50 artıyor, sonra %40 azalıyor. Net değişim nedir?',
 ['Çarpanlar: %50 artış × 1,5; %40 azalış × 0,6', 'Net çarpan: 1,5 × 0,6 = 0,9', 'Fiyat 0,9 katına indi: %10 azalış'], '%10 azalış',
 'Yüzdeleri toplamak (+50 − 40 = +10) ya da ikinci yüzdeyi ilk değere uygulamak. Yüzde puan farkı ile yüzde değişimi de karıştırma.',
 'Yüzdeler toplanmaz, çarpılır.')

# 20 birleşik yüzde
y1, y2 = 20 * 60 // 100, 30 * 80 // 100
assert (y1, y2) == (12, 24) and (y1 + y2) * 100 // 50 == 72
kart('prob-yuzde-problemleri-04', 'Gruplarda birleşik yüzde',
 'Farklı büyüklükteki grupların yüzdelerini sayıya çevirip birleşik yüzdeyi kurabildiğini.',
 'Yüzdeleri doğrudan ortalama alma. Her grubu **sayıya çevir**; mevcutlar farklıysa ağırlıklar farklıdır. Sayıları topla, toplam mevcuda böl, 100 ile çarp. Bütünü 100 almak işi kolaylaştırır.',
 'birleşik % = toplam sayı ÷ toplam mevcut × 100', None,
 'A sınıfındaki 20 öğrencinin %60\'ı, B sınıfındaki 30 öğrencinin %80\'i sınavı geçiyor. İki sınıfın birlikte geçme yüzdesi kaçtır?',
 ['A: 20 × 0,60 = 12; B: 30 × 0,80 = 24', 'Geçen: 12 + 24 = 36; mevcut: 20 + 30 = 50', 'Yüzde: 36 ÷ 50 = %72'], '%72',
 'Yüzdelerin düz ortalamasını almak (%70). Sınıf mevcutları farklıysa her yüzde kendi grubuna göredir; önce sayıya çevir.',
 'Yüzdeyi sayıya çevir, sonra topla.')

# 21 grafik yüzde
bil = 100 - 35 - 25
assert bil == 40 and 600 * (35 + bil) // 100 == 450
kart('prob-yuzde-problemleri-06', 'Grafik ve modelle yüzde yorumu',
 'Grafik ya da şeritteki yüzdeleri okuyup bilinmeyen dilimi ve istenen toplam sayıyı bulabildiğini.',
 'Dilim yüzdelerinin toplamı **%100**\'dür; bilinmeyen dilimi 100\'den çıkararak bul. İstenen dilimlerin yüzdelerini **önce topla**, sonra kişi sayısına çevir. Yüzde artışta bölen eski değerdir.',
 'sayı = toplam × yüzde ÷ 100', yuzde(),
 '600 kişinin okuduğu kitap türleri: roman %35, öykü %25, geri kalanı şiir. Roman ya da şiir okuyan kaç kişidir?',
 ['Şiir: 100 − 35 − 25 = %40', 'İstenen: %35 + %40 = %75', 'Kişi: 600 × 75 ÷ 100 = 450'], '450 kişi',
 'Yüzdeleri toplamayı unutup yalnız bir dilimi almak ya da yüzdeyi kişi sayısı sanmak. Sorulan dilimleri alt alta yazıp işaretle.',
 'Önce yüzdeleri topla.')

# 22 havuz
net = F(1, 3) + F(1, 6) - F(1, 4)
assert net == F(1, 4) and 1 / net == 4
kart('prob-isci-emek-02', 'Havuz ve musluk problemleri',
 'Dolduran ve boşaltan muslukların saatlik etkilerini işaretleriyle toplayıp dolma süresini bulabildiğini.',
 'Bir havuzu t saatte dolduran musluk saatte **1/t** doldurur. Dolduran **+**, boşaltan **−** yazılır. Net hız = dolduranlar − boşaltanlar. Havuzun tamamı 1 sayılır; süre 1 ÷ net hızdır.',
 'süre = 1 ÷ (1/a + 1/b − 1/c)', None,
 'Bir havuzu A musluğu 3 saatte, B musluğu 6 saatte doldurur; C musluğu dolu havuzu 4 saatte boşaltır. Üçü birlikte açılırsa boş havuz kaç saatte dolar?',
 ['Saatlik iş: 1/3 + 1/6 − 1/4 (C eksi)', 'Ortak payda 12: 4/12 + 2/12 − 3/12 = 3/12 = 1/4', 'Süre: 1 ÷ 1/4 = 4 saat'], '4 saat',
 'Boşaltan musluğu da dolduran saymak ya da süreleri çıkarıp ortalamak. Saatlik işlerle çalış; süreler toplanmaz.',
 'Boşaltanın işareti eksidir.')

# 23 grafik iş
yap = 2 * (F(1, 10) + F(1, 15)); kalan = 1 - yap
assert yap == F(1, 3) and kalan / F(1, 15) == 10
kart('prob-isci-emek-04', 'Grafik ve çizelgeyle iş problemleri',
 'Grafik ya da çizelgeden yapılan işi okuyup kalan işi yeni ekibin hızına göre süreye çevirebildiğini.',
 'Grafikten **iş payını ya da yapılan işi** oku; işin tamamını 1 al. Kalan iş = 1 − yapılan iş. Yeni ekibin hızını bul, kalan işi bu hıza böl. Aynı sürede yapılan işler **hızlarıyla orantılıdır**.',
 'kalan süre = kalan iş ÷ yeni ekibin hızı', None,
 'Ali bir işi tek başına 10 günde, Burak 15 günde bitiriyor. İkisi 2 gün birlikte çalıştıktan sonra Ali ayrılıyor. Kalan işi Burak kaç günde bitirir?',
 ['Birlikte günde 1/10 + 1/15 = 1/6; 2 günde 1/3', 'Kalan iş: 1 − 1/3 = 2/3', 'Burak\'ın hızı 1/15: (2/3) ÷ (1/15) = 10 gün'], '10 gün',
 'Kalan işi yalnız bir kişinin hızıyla hesaplamak ya da yapılan yarıyı kalan iş sanmak. Önce kim çalışıyor, sonra hangi hızla, diye sor.',
 'Kalan işi yeni hıza böl.')

# ---------- doğrulama ----------
girdi = open(GIRDI, encoding='utf-8').read()
bloklar = [l.split(' | ') for l in girdi.splitlines() if l.startswith('### ')]
ids = [b[0][4:] for b in bloklar]
anahtar = {b[0][4:]: b[1] for b in bloklar}
for c in K:
    c['k'] = anahtar[c['id']]
def sirala(c):
    return dict(id=c['id'], k=c['k'], baslik=c['baslik'], olcer=c['olcer'], kural=c['kural'], formul=c['formul'],
                sekil=c['sekil'], ornek=c['ornek'], hata=c['hata'], akilda=c['akilda'])
K = [sirala(c) for c in K]
def kel(s): return len(s.replace('**', '').split())
for c in K:
    for f in ('id', 'k', 'baslik', 'olcer', 'kural', 'hata', 'akilda'):
        assert c[f], (c['id'], f)
    o = c['ornek']
    assert o['soru'] and o['cevap'] and 2 <= len(o['adimlar']) <= 4, c['id']
    assert kel(c['baslik']) <= 6, (c['id'], 'baslik')
    assert kel(c['olcer']) <= 25 and not c['olcer'].startswith('Bu soru'), (c['id'], 'olcer', kel(c['olcer']))
    assert kel(c['kural']) <= 60 and '**' in c['kural'], (c['id'], 'kural', kel(c['kural']))
    assert kel(c['hata']) <= 40, (c['id'], 'hata', kel(c['hata']))
    assert kel(c['akilda']) <= 8 and '"' not in c['akilda'] and '“' not in c['akilda'], (c['id'], 'akilda')
    if c['sekil']:
        assert len(c['sekil'].encode()) <= 25000
        assert all(int(s) >= 11 for s in re.findall(r'font-size="(\d+)"', c['sekil']))
assert [c['id'] for c in K] == ids or sorted(c['id'] for c in K) == sorted(ids), 'id uyumsuz'
assert len(set(c['id'] for c in K)) == len(ids)
json.dump(K, open(CIKTI, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
import os
os.makedirs('/tmp/kor/kart/png', exist_ok=True)
for c in K:
    if c['sekil']:
        open('/tmp/kor/kart/p14/%s.svg' % c['id'], 'w', encoding='utf-8').write(c['sekil'])
print(len(K), 'kart,', sum(1 for c in K if c['sekil']), 'şekilli')
