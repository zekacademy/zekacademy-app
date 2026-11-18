# -*- coding: utf-8 -*-
import json, math, itertools, re

GIRDI = '/tmp/kor/kart/parti/p13.txt'
CIKTI = '/home/claude/zekacademy-app/havuz/tekrar/kart-p13.json'

INK, MUTED, LINE = 'var(--ink,#18212f)', 'var(--muted,#5b6678)', 'var(--line,#dde3ec)'
BRAND, BRAND_S = 'var(--brand,#2f5bea)', 'var(--brand-soft,#e7edff)'
RULE, RULE_S = 'var(--rule,#0f8a6a)', 'var(--rule-soft,#e3f5ef)'
WARN, WARN_S = 'var(--warn,#c2410c)', 'var(--warn-soft,#fff1e8)'

def T(x, y, s, size=12, anchor='start', bold=False, fill=INK):
    w = ' font-weight="600"' if bold else ''
    return f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}"{w} fill="{fill}">{s}</text>'

def svg(w, h, aria, body):
    return (f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="{aria}" xmlns="http://www.w3.org/2000/svg">'
            f'{body}</svg>')

def L(x1, y1, x2, y2, c=MUTED, sw=1.5, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="{sw}"{d}/>'

def R(x, y, w, h, fill='none', stroke=MUTED, sw=1.5):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'

# ---------- şekiller ----------
def sekil_yol_zaman():
    b = L(40, 140, 262, 140) + L(40, 140, 40, 18)
    b += L(40, 140, 160, 32, RULE, 2.5)
    b += L(160, 32, 160, 140, MUTED, 1, '4 3') + L(40, 32, 160, 32, MUTED, 1, '4 3')
    b += f'<circle cx="160" cy="32" r="4" fill="{RULE}"/>'
    b += T(160, 156, '3 sa', 12, 'middle') + T(2, 36, '270 km', 12)
    b += T(262, 156, 'Zaman', 12, 'end') + T(46, 14, 'Yol', 12)
    return svg(280, 166, 'Başlangıçtan geçen doğrusal yol-zaman grafiği; 3 saatte 270 km', b)

def sekil_daire():
    cx, cy, r = 110, 85, 62
    def pt(a):
        return cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a))
    a0, a1 = -90, -90 + 150
    x0, y0 = pt(a0); x1, y1 = pt(a1)
    b = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{BRAND_S}" stroke="{MUTED}" stroke-width="1.5"/>'
    b += (f'<path d="M{cx},{cy} L{x0:.1f},{y0:.1f} A{r},{r} 0 0 1 {x1:.1f},{y1:.1f} Z" '
          f'fill="{RULE_S}" stroke="{RULE}" stroke-width="2"/>')
    mx, my = cx + 0.55 * r * math.cos(math.radians(-15)), cy + 0.55 * r * math.sin(math.radians(-15))
    b += T(f'{mx:.0f}', f'{my:.0f}', '150°', 13, 'middle', True)
    b += T(190, 50, 'Futbol', 13, 'start', True, RULE) + T(190, 70, 'dilimi', 12)
    b += T(110, 165, 'Tüm daire 360°', 12, 'middle', False, MUTED)
    return svg(280, 172, 'Daire grafiğinde 150 derecelik bir dilim', b)

def sekil_sutun():
    base = 140; u = 15
    b = ''
    for i in range(0, 9):
        b += L(40, base - i * u, 250, base - i * u, LINE, 1)
    b += L(40, base, 250, base) + L(40, base, 40, 15)
    for x, n, nm, f, s in [(60, 5, 'A', RULE_S, RULE), (120, 8, 'B', BRAND_S, BRAND), (180, 3, 'C', WARN_S, WARN)]:
        b += R(x, base - n * u, 44, n * u, f, s, 2)
        b += T(x + 22, base + 16, nm, 13, 'middle', True)
    b += T(82, base - 5 * u - 6, '30', 13, 'middle', True, RULE)
    b += T(262, 30, '1 bölme = ?', 12, 'end', False, MUTED)
    return svg(280, 166, 'Değerleri yazılmamış sütun grafiği; A sütunu 5 bölme ve 30', b)

def sekil_tren():
    b = T(4, 12, 'Tamamen geçme', 12, 'start', True)
    b += R(90, 20, 150, 28, BRAND_S, BRAND, 2) + R(30, 26, 60, 16, WARN_S, WARN, 2)
    b += T(165, 38, 'tünel', 12, 'middle')
    b += L(30, 60, 240, 60, RULE, 2) + L(30, 55, 30, 65, RULE, 2) + L(240, 55, 240, 65, RULE, 2)
    b += T(135, 77, 'yol = tren + tünel', 12, 'middle', True, RULE)
    b += T(4, 100, 'Tamamen içinde kalma', 12, 'start', True)
    b += R(90, 108, 150, 28, BRAND_S, BRAND, 2) + R(90, 114, 60, 16, WARN_S, WARN, 2)
    b += T(200, 126, 'tünel', 12, 'middle')
    b += L(150, 146, 240, 146, RULE, 2) + L(150, 141, 150, 151, RULE, 2) + L(240, 141, 240, 151, RULE, 2)
    b += T(195, 163, 'yol = tünel − tren', 12, 'middle', True, RULE)
    return svg(280, 170, 'Tren tünelden geçerken ve tünelin içindeyken alınan yol', b)

def sekil_serit():
    x0, w = 28, 28
    b = T(140, 26, '8 eş bölme', 12, 'middle', True)
    b += L(28, 34, 252, 34, MUTED, 1.2)
    cols = [(0, 3, WARN_S, WARN, 'kira'), (3, 5, BRAND_S, BRAND, 'market'), (5, 8, RULE_S, RULE, 'birikim')]
    for s, e, f, st, nm in cols:
        for i in range(s, e):
            b += R(x0 + i * w, 44, w, 40, f, st, 1.5)
        b += T(x0 + (s + e) * w / 2, 106, nm, 12, 'middle', True, st)
    b += T(x0 + 6.5 * w, 124, '450 TL', 12, 'middle', True, RULE)
    return svg(280, 136, 'Sekiz eş bölmeli şerit: 3 bölme kira, 2 bölme market, 3 bölme birikim', b)

def sekil_zaman():
    def X(y): return 40 + (y - 1950) / 58 * 200
    b = L(30, 56, 250, 56, MUTED, 2)
    for y, nm in [(1950, 'Dede'), (1976, 'Baba'), (2008, 'Çocuk')]:
        x = round(X(y))
        b += f'<circle cx="{x}" cy="56" r="5" fill="{RULE}"/>'
        b += T(x, 38, str(y), 12, 'middle', True) + T(x, 78, nm, 12, 'middle')
    b += T(round((X(1950) + X(1976)) / 2), 100, '26 yıl', 12, 'middle', True, BRAND)
    b += T(round((X(1976) + X(2008)) / 2), 100, '32 yıl', 12, 'middle', True, BRAND)
    return svg(280, 112, 'Doğum yılı çizelgesi: 1950, 1976 ve 2008; iki aralık', b)

# ---------- hesap doğrulamaları ----------
def hesap():
    # g01
    assert 270 / 3 == 90 and 90 * 5 == 450
    # g03
    assert 240 * 150 / 360 == 100
    # g05
    assert 30 / 5 == 6 and (5 + 8 + 3) * 6 == 96
    # h02
    assert 72 / 3.6 == 20 and (480 - 120) / 20 == 18
    # h04
    assert 40 * 2 == 80 and 80 / (60 - 40) == 4 and 8 + 2 + 4 == 14 and 40 * 6 == 240
    # h06
    assert 120 / 40 + 120 / 60 == 5 and 240 / 5 == 48 and 48 < (40 + 60) / 2
    # kz
    assert (300 - 250) + (340 - 400) == -10
    # km01
    assert (80 * 3 + 120 * 2) / 5 == 96
    # km03
    assert 300 * 0.20 == 60 and 60 / 0.30 == 200 and 300 - 200 == 100
    # ke01
    assert 8 - 3 - 2 == 3 and 450 / 3 == 150 and 150 * 8 == 1200
    # ke03
    from fractions import Fraction as F
    d = F(2, 3) - F(2, 9)
    assert d == F(4, 9) and 20 / (4) == 5 and 5 * 9 == 45
    # r01
    n = sum(1 for p in itertools.permutations(range(1, 7), 3) if p[0] % 2 == 0)
    assert n == 60 == 3 * 5 * 4
    # r03
    ren = ['k', 'y', 'm', 's']
    assert sum(1 for i in range(50) if ren[i % 4] == 'k') == 13 and divmod(50, 4) == (12, 2)
    # r05
    assert 8 * 7 == 56 and 56 // 2 == 28 == sum(1 for _ in itertools.combinations(range(8), 2))
    # s02
    k = 300 - 100
    assert k == 200 and k + 300 == 2 * k + 100 == 500
    # s04
    assert 100 - 7 == 93 and 15 * 4 == 60 and 93 - 60 == 33
    # y01
    assert 18 * 5 == 90 and 90 - 22 == 68 and 68 / 4 == 17
    # y03
    assert (1976 - 1950, 2008 - 1976) == (26, 32) and (26 + 32) / 2 == 29
    # yz01
    assert 800 * 60 / 100 == 480 and 480 * 2 == 960
    # yz03
    assert (80 - 40) / 2 == 20 and 20 / 80 * 100 == 25
    # yz05
    assert 28 / 0.70 == 40
    # i01
    from fractions import Fraction as F
    g = F(1, 12) + F(1, 6)
    assert g == F(1, 4) and g * 2 == F(1, 2) and (1 - g * 2) / F(1, 12) == 6
    # i03
    assert F(1, 20) + F(1, 5) == F(1, 4)
hesap()

# ---------- kartlar ----------
def K(id, baslik, olcer, kural, formul, sekil, soru, adimlar, cevap, hata, akilda):
    return dict(id=id, baslik=baslik, olcer=olcer, kural=kural, formul=formul, sekil=sekil,
                ornek=dict(soru=soru, adimlar=adimlar, cevap=cevap), hata=hata, akilda=akilda)

C = {}
def ekle(*a): C[a[0]] = K(*a)

ekle('prob-grafik-problemleri-01', 'Doğrusal grafikte eğim ve hız',
 'Doğrusal grafiğin eğimini hız ya da akış hızı olarak okuyup verilen süre için yolu veya miktarı bulabilmeni.',
 'Doğrusal grafikte **eğim** sabit hızı verir: eğim = değişen miktar ÷ geçen süre. Önce grafikten bir noktanın değerini oku, hızı bul, sonra **soruda istenen süreyle çarp**. Parçalı grafikte her doğru parçasının eğimini ayrı hesapla.',
 'hız = yol farkı ÷ süre farkı · yol = hız × süre', sekil_yol_zaman(),
 'Başlangıçtan geçen yol–zaman grafiğinde bir araç 3 saatte 270 km gidiyor. Aynı hızla 5 saatte kaç km gider?',
 ['Grafikten bir nokta oku: 3 saatte 270 km.', 'Hız = 270 ÷ 3 = 90 km/sa.', 'İstenen süre 5 saat: yol = 90 × 5 = 450 km.'],
 '450 km',
 'Hızı bulup soruda istenen süreyle çarpmayı unutmak ya da grafikteki son değeri cevap sanmak. Cevaptan önce sorulan sürenin kaç saat olduğunu bir kez daha oku.',
 'Eğim hızdır, hız çarpı süre yoldur.')

ekle('prob-grafik-problemleri-03', 'İki kaynağı birlikte yorumlama',
 'İki grafiği ya da tabloyu birlikte okuyup ortak büyüklükten eksik değeri ve sorulan grubu bulabilmeni.',
 'İki kaynağı birlikte okurken her birinden **ortak büyüklüğü** al. Daire grafiğinde dilim = toplam × açı ÷ 360; tabloda gelir = fiyat × adet. Eksik hücreyi bulmak için bilinen satırların hepsini **toplamdan düş**, sonra sorulan grubu seç.',
 'dilim = toplam × açı ÷ 360 · gelir = fiyat × adet', sekil_daire(),
 '240 kişilik bir grubun tercihleri daire grafiğiyle gösteriliyor. Futbol dilimi 150° ise futbolu seçen kaç kişidir?',
 ['Tüm daire 360°, grubun toplamı 240 kişi.', 'Dilim = toplam × açı ÷ 360.', '240 × 150 ÷ 360 = 100 kişi.'],
 '100 kişi',
 'Soru tüm grubu isterken tek satırı ya da tek dilimi cevap yapmak, toplama bir grubu katmamak. Cevaptan önce sorunun hangi grupları kapsadığını işaretle.',
 'Toplamdan bilinenleri düş, kalan senin.')

ekle('prob-grafik-problemleri-05', 'Sütun grafiği ve ölçek',
 'Eksendeki değerler yazılmamış olsa da sütunları bölme sayısıyla okuyup toplam ve yüzde hesaplayabilmeni.',
 'Sütunun değerini üst ucundan **yatay çizgiyi izleyerek** oku. Eksende sayı yoksa bilinen bir sütundan **bir bölmenin değerini** bul, diğer sütunları bölme sayısıyla çarp. Yüzde için parça ÷ bütün × 100 al. Bir aralık birden çok dilimi kapsıyorsa hepsini topla.',
 '1 bölme = bilinen değer ÷ bölme sayısı', sekil_sutun(),
 'Değerleri yazılmamış grafikte A sütunu 5 bölmelik ve 30 öğrenciyi gösteriyor. B sütunu 8, C sütunu 3 bölmelik. Üç sütunun toplamı kaç öğrencidir?',
 ['Bir bölme = 30 ÷ 5 = 6 öğrenci.', 'Toplam bölme: 5 + 8 + 3 = 16.', 'Toplam öğrenci: 16 × 6 = 96.'],
 '96 öğrenci',
 'Bir zaman aralığını tek dilimle sınırlamak ya da bütünü yanlış almak. Aralığın kapsadığı dilimleri tek tek işaretle, sonra toplamı bütüne böl.',
 'Önce bir bölmeyi bul.')

ekle('prob-hareket-hiz-02', 'Tren, tünel ve köprü',
 'Boyu olan trenin tüneli geçme ve tünelde tamamen kalma sürelerini doğru yolla hesaplayabilmeni.',
 'Tren boyu olan bir cisimdir. Tüneli **tamamen geçerken** yol = tren boyu + tünel boyu. Tünelde **tamamen içinde kalırken** yol = tünel boyu − tren boyu. Hız km/sa ise **3,6\'ya bölerek** m/sn yap.',
 'geçme: (tren + tünel) ÷ hız · içinde: (tünel − tren) ÷ hız', sekil_tren(),
 '120 m boyundaki tren 72 km/sa hızla 480 m uzunluğundaki bir tünelden geçiyor. Trenin tünelde tamamen içinde kaldığı süre kaç saniyedir?',
 ['Hızı çevir: 72 ÷ 3,6 = 20 m/sn.', 'Tamamen içindeyken arka uç girişte, ön uç çıkışta olana kadar yol = 480 − 120 = 360 m.', 'Süre = 360 ÷ 20 = 18 sn.'],
 '18 sn',
 'İçinde kalma süresine tren ve tünel boyunu toplamak ya da yalnız tünel veya yalnız tren boyunu kullanmak. Sorunun geçme mi, içinde kalma mı olduğunu işaretle.',
 'Geçerken topla, içindeyken çıkar.')

ekle('prob-hareket-hiz-04', 'Yetişme ve karşılaşma öncülleri',
 'Yetişme ve karşılaşma sorularında temel süreyi bulup her öncülü ayrı ayrı sınayabilmeni.',
 'Aynı yönde giden iki aracın arası her saat **hızlar farkı** kadar kapanır; zıt yönde **hızlar toplamı** kadar. Önce temel büyüklüğü (süre, yol) bul. Sonra her öncülü bu değerle **tek tek sına**. Geç çıkan araç, ilk araçtan daha kısa süre yolda kalır.',
 'yetişme: süre = ön fark ÷ hızlar farkı', None,
 'A aracı 08.00\'de 40 km/sa ile yola çıkıyor. B aracı 10.00\'da aynı yönde 60 km/sa ile çıkıyor. B, A\'ya kaçta yetişir ve A o ana kadar kaç km gitmiş olur?',
 ['A, 2 saatte 40 × 2 = 80 km önde.', 'B her saat 60 − 40 = 20 km yaklaşır: 80 ÷ 20 = 4 saat.', 'B, 10.00 + 4 saat = 14.00\'te yetişir.', 'A, 08.00–14.00 arası 6 saat gitti: 40 × 6 = 240 km.'],
 '14.00, 240 km',
 'Geç çıkan aracın yolda kalma süresiyle ilk aracınkini karıştırmak. Yetişme anında ilk araç daha uzun süredir yoldadır. Her öncülde hangi aracın süresinin sorulduğunu işaretle.',
 'Önce süreyi bul, sonra öncülleri sına.')

ekle('prob-hareket-hiz-06', 'Ortalama hız',
 'Parçalı yolculukta toplam yolu toplam süreye bölerek ortalama hızı bulabilmeni.',
 'Ortalama hız = **toplam yol ÷ toplam süre**; hızların ortalaması değildir. Her parçanın süresini ayrı bul: süre = yol ÷ hız, yol = hız × süre. Birimleri eşitle: dakikayı 60\'a bölerek saate, km/sa\'i 3,6\'ya bölerek m/sn\'ye çevir.',
 'ortalama hız = toplam yol ÷ toplam süre', None,
 '120 km\'lik bir yol gidişte 40 km/sa, dönüşte 60 km/sa hızla alınıyor. Gidiş–dönüş ortalama hızı kaç km/sa\'tir?',
 ['Gidiş süresi 120 ÷ 40 = 3 saat, dönüş süresi 120 ÷ 60 = 2 saat.', 'Toplam yol 240 km, toplam süre 5 saat.', 'Ortalama hız = 240 ÷ 5 = 48 km/sa.'],
 '48 km/sa',
 'İki hızın aritmetik ortalamasını almak ya da toplam yolu tek parçanın süresine bölmek. Yavaş bölüm daha uzun sürdüğü için sonuç iki hızın ortalamasından küçük çıkar.',
 'Toplam yol bölü toplam süre.')

ekle('prob-kar-zarar-02', 'Kâr, zarar ve yüzde',
 'Alış, satış ve zararı doğru işaretle toplayıp kâr ya da zarar yüzdesini alışa göre bulabilmeni.',
 'Kâr = satış − alış; zarar = alış − satış. Kâr ya da zarar **yüzdesi alış fiyatına göre** hesaplanır. Birden çok ürün varsa **zararı eksi işaretle** kâra kat. İndirimli fiyat = etiket × (100 − indirim) ÷ 100.',
 'kâr % = (satış − alış) ÷ alış × 100', None,
 'Bir mağaza 250 TL\'ye aldığı ürünü 300 TL\'ye, 400 TL\'ye aldığı ürünü 340 TL\'ye satıyor. Toplamda kâr mı zarar mı eder, kaç TL?',
 ['1. ürün: 300 − 250 = +50 TL kâr.', '2. ürün: 340 − 400 = −60 TL, yani zarar.', 'Toplam: +50 − 60 = −10 TL.'],
 '10 TL zarar',
 'Zarar eden ürünü de kâr gibi toplamak ya da kâr yerine alış tutarını yazmak. Her ürünün işaretini ayrı yaz, topla ve sorunun neyi istediğine bak.',
 'Zarar eksidir, yüzde alışa göredir.')

ekle('prob-karisim-problemleri-01', 'Fiyat karışımı ve alaşım',
 'Karışımda toplam maliyetten ortalama fiyatı, bölmeli alaşım çubuğundan metal kütlelerini bulabilmeni.',
 'Karışımda **toplam miktar** üzerinden düşün: ortalama fiyat = toplam maliyet ÷ toplam miktar. Bölmeli alaşım çubuğunda bilinen metalden **bir bölmenin kütlesini** bul, diğer metalleri bölme sayısıyla çarp. Ayar, alaşımın kaç bölmesinin saf altın olduğunu gösterir.',
 'ortalama fiyat = toplam maliyet ÷ toplam miktar', None,
 'Kilosu 80 TL olan çaydan 3 kg ile kilosu 120 TL olan çaydan 2 kg karıştırılıyor. Karışımın kilosu kaç TL\'dir?',
 ['Maliyet: 80 × 3 + 120 × 2 = 240 + 240 = 480 TL.', 'Toplam miktar: 3 + 2 = 5 kg.', 'Kilo fiyatı: 480 ÷ 5 = 96 TL.'],
 '96 TL',
 'Sorulan metal yerine bildiğin metalin ya da başka bir metalin kütlesini yazmak. Bir bölmenin kütlesini bulduktan sonra hangi metalin istendiğini altını çizerek kontrol et.',
 'Bilinen parçadan bir bölmeye geç.')

ekle('prob-karisim-problemleri-03', 'Su ekleme ve buharlaşma',
 'Su eklenince ya da buharlaşınca değişmeyen maddeyi bulup yeni toplamı ve oranı hesaplayabilmeni.',
 'Su eklenirken ya da buharlaşırken **madde (tuz, şeker) miktarı değişmez**; yalnız karışımın toplamı değişir. Önce madde miktarını bul: madde = oran × toplam. Sonra yeni toplam = madde ÷ yeni oran. İki toplamın farkı eklenen ya da buharlaşan suyu verir.',
 'yeni toplam = madde ÷ yeni oran', None,
 '300 g %20\'lik şekerli sudan kaç g su buharlaştırılırsa karışım %30\'luk olur?',
 ['Şeker: 300 × 0,20 = 60 g, buharlaşınca değişmez.', 'Yeni toplam: 60 ÷ 0,30 = 200 g.', 'Buharlaşan su: 300 − 200 = 100 g.'],
 '100 g',
 'Oran farkını toplamla çarpmak ya da madde miktarını eklenen su sanmak. Sorunun eklenen suyu mu, yeni toplamı mı, başlangıç suyunu mu istediğini kontrol et.',
 'Madde sabit, toplam değişir.')

ekle('prob-kesir-problemleri-01', 'Şekil ve modelle kesir',
 'Şekil ve modelde eş bölmeleri sayıp bilinen kısımdan bütünü ve kalan kısmı bulabilmeni.',
 'Şekil ya da modelde önce **eş bölme sayısını** say. Bilinen bölmelerin değerinden **bir bölmeyi** bul: bir bölme = değer ÷ bölme sayısı. Bütün = bir bölme × toplam bölme sayısı. Kalan kısım için verilen payları toplam bölmeden çıkar.',
 '1 bölme = bilinen değer ÷ bölme sayısı', sekil_serit(),
 'Bir gelir 8 eş bölmeli şeritle gösterilmiş: 3 bölme kira, 2 bölme market, kalan bölmeler birikim. Birikim 450 TL ise gelirin tamamı kaç TL\'dir?',
 ['Birikim bölmesi: 8 − 3 − 2 = 3.', 'Bir bölme: 450 ÷ 3 = 150 TL.', 'Bütün: 150 × 8 = 1200 TL.'],
 '1200 TL',
 'Sorulan kısım yerine verilen kısmı bulmak ya da kalanı bulmak için verilenleri çıkarmayı unutmak. Sonucun sorudaki "kalan" ya da "tamamı" ifadesine uyup uymadığına bak.',
 'Önce bir bölme, sonra bütün.')

ekle('prob-kesir-problemleri-03', 'Doluluk farkı ve kesir',
 'Doluluk kesirlerinin farkından eklenen miktarı kapasiteyle ilişkilendirip kapasiteyi bulabilmeni.',
 'Kabın doluluğu değişince **kesirlerin farkı**, eklenen ya da alınan miktarın kapasitedeki kesridir. Paydaları eşitleyip farkı bul. Farka karşılık gelen miktardan **bir parçayı**, sonra bütünü bul. Pil ya da yakıtta kullanım süresi de aynı orantıyla bulunur.',
 'kapasite = eklenen miktar ÷ doluluk farkı', None,
 'Bir depo 2/9 doluyken 20 L su eklenince 2/3 doluyor. Deponun kapasitesi kaç litredir?',
 ['Doluluk farkı: 2/3 − 2/9 = 6/9 − 2/9 = 4/9.', '4/9 kapasite 20 L ise 1/9 kapasite 20 ÷ 4 = 5 L.', 'Kapasite: 5 × 9 = 45 L.'],
 '45 L',
 'Paydaları eşitlemeden payları çıkarmak ya da bir parçayı bulup yanlış sayıyla çarpmak. Parça sayısı ortak paydadır; bulduğun kapasiteyi geri yerine koyup kontrol et.',
 'Kesir farkı, eklenen miktarı gösterir.')

ekle('prob-rutin-olmayan-01', 'Şifre sayma ve oyun',
 'Koşullu şifre ve oyun sorularında seçenekleri basamak basamak sayıp çarpabilmeni.',
 'Her basamağın seçenek sayısını koşullara uyarak bul ve **çarp**. En sıkı koşullu basamaktan başla. Bağlı basamaklar birlikte, serbest basamaklar ayrı ayrı sayılır. Oyunlarda **kaybettiren konumları** küçük sayılardan başlayarak bul.',
 'toplam = seçenek₁ × seçenek₂ × seçenek₃', None,
 '1, 2, 3, 4, 5, 6 rakamlarıyla yazılan, rakamları farklı 3 basamaklı sayılardan kaç tanesinin ilk rakamı çifttir?',
 ['İlk rakam çift: 2, 4 ya da 6, yani 3 seçenek.', 'İkinci rakam kalan 5 rakamdan biri: 5 seçenek.', 'Üçüncü rakam kalan 4 rakamdan biri: 4 seçenek.', 'Toplam: 3 · 5 · 4 = 60.'],
 '60',
 'Rakamların farklı olma koşulunu unutmak ya da olmayan bir koşulu eklemek. Her basamak için önce yasak rakamları yaz, sonra seçenekleri say.',
 'Sıkı koşuldan başla, basamakları çarp.')

ekle('prob-rutin-olmayan-03', 'Periyodik düzen ve kalan',
 'Tekrar eden düzende tam tur sayısı ile kalanı kullanarak istenen sıradaki durumu bulabilmeni.',
 'Düzen her **p adımda** tekrar ediyorsa n\'yi p\'ye böl. **Bölüm** tam tur sayısını, **kalan** son turda kaçıncı sırada olduğunu verir. Kalan 0 ise son tur tamamlanmıştır. Sabit artan örüntüde n. terim = ilk terim + (n − 1) · artış.',
 'n = p · tur + kalan', None,
 'Kırmızı, yeşil, mavi, sarı sırasıyla yanan bir lambanın düzeni sürekli tekrar ediyor. İlk 50 ışıkta kaç tane kırmızı vardır?',
 ['Düzen 4 ışıkta tekrar eder: 50 = 4 · 12 + 2.', '12 tam turda 12 kırmızı vardır.', 'Kalan 2 ışık kırmızı ve yeşildir: 1 kırmızı daha.', 'Toplam: 12 + 1 = 13.'],
 '13',
 'Kalanı sayılacak nesnenin sayısı sanmak ya da bölümü yukarı yuvarlamak. Kalan kısımda aranan nesne var mı, tek tek yazarak bak.',
 'Önce tam tur, sonra kalan.')

ekle('prob-rutin-olmayan-05', 'Sayma ve durum tarama',
 'Sayma ve en az-en çok sorularında bütün uygun durumları düzenli listeleyebilmeni.',
 'Sayma sorularında **sıra önemli mi** diye bak. Sıra önemsizse n kişiden ikili seçim sayısı n·(n − 1) ÷ 2\'dir. Durum taramada koşulları yaz, uygun **bütün durumları listele**, sonra en çok ya da en az sorusuna göre seç. Boş cevap puanı değiştirmez.',
 'n kişiden ikili seçim: n · (n − 1) ÷ 2', None,
 '8 takımlı bir turnuvada her takım diğer takımların her biriyle bir kez oynuyor. Toplam kaç maç oynanır?',
 ['Her takım 7 takımla oynar: 8 · 7 = 56.', 'Her maç iki kez sayıldı, çünkü sıra önemsiz.', '56 ÷ 2 = 28.'],
 '28 maç',
 '"En çok" sorusunda en küçük uygun değeri yazmak ya da yanlış cevabı puan kazandıran saymak. Bütün uygun durumları listele, sonra istenen uç değeri seç.',
 'Bütün durumları yaz, sonra seç.')

ekle('prob-sayi-problemleri-02', 'Terazi ve geriye çözme',
 'Terazi dengesinden ağırlık bulup işlem zincirini sondan başa ters işlemlerle çözebilmeni.',
 'Terazi dengedeyse iki kefenin ağırlığı **eşittir**; iki yandan ortak nesneleri çıkarıp denklemi sadeleştir. İşlem zincirinde sonuçtan başla ve işlemleri **ters sırayla, tersiyle** yap (+ ↔ −, × ↔ ÷). En az–en çok sorularında diğer değerleri ters uca al.',
 'sol kefe = sağ kefe', None,
 'Dengedeki terazinin sol kefesinde 1 kutu ve 300 g, sağ kefesinde 2 kutu ve 100 g var. Bir kutu kaç gramdır?',
 ['Sağdan ve soldan 1 kutu çıkar: 300 = 1 kutu + 100.', 'Bir kutu = 300 − 100 = 200 g.', 'Kontrol: sol 200 + 300 = 500, sağ 400 + 100 = 500.'],
 '200 g',
 'Verilen ağırlığı cevap sanmak ya da farkla çarpma yerine bölme yapmak. Ortak nesneleri çıkardıktan sonra kalan eşitliği yaz, bulduğun değeri iki kefeye koyup doğrula.',
 'Ortak nesneyi çıkar, tersten geri git.')

ekle('prob-sayi-problemleri-04', 'Alışveriş ve para üstü',
 'Verilen paradan para üstünü düşerek gerçek bedeli bulup fiyat denklemini kurabilmeni.',
 'Alışverişte **verilen para = bedel + para üstü**. Önce gerçekte ödenen bedeli bul: bedel = verilen − para üstü. İki tür nesnede adet ve tutardan iki denklem kur, birini öbürüne yerleştir. Puanlamada her doğru ve yanlışın puanını ayrı yaz.',
 'bedel = verilen para − para üstü', None,
 'Tanesi 15 TL olan 4 defter ve 1 kalem için 100 TL verilip 7 TL para üstü alınıyor. Kalem kaç TL\'dir?',
 ['Ödenen bedel: 100 − 7 = 93 TL.', 'Defterler: 15 × 4 = 60 TL.', 'Kalem: 93 − 60 = 33 TL.'],
 '33 TL',
 'Para üstünü hesaba katmamak ya da çıkarmak yerine eklemek. Bedeli bulmadan fiyat hesabına geçme; bulduğun fiyatları ödenen bedelle toplayarak kontrol et.',
 'Önce gerçek ödemeyi bul.')

ekle('prob-yas-problemleri-01', 'Yaş ortalaması',
 'Ortalamadan toplam yaşa geçip gruba katılan ya da ayrılan kişinin etkisini hesaplayabilmeni.',
 'Ortalama = yaşlar toplamı ÷ kişi sayısı; bu yüzden **toplam = ortalama × kişi sayısı**. Gruba biri katılınca ya da ayrılınca önce toplamı bul, yaşı ekle ya da çıkar, **yeni kişi sayısına böl**. İki kişinin **yaş farkı hiç değişmez**.',
 'toplam yaş = ortalama × kişi sayısı', None,
 '5 kişilik bir grubun yaş ortalaması 18\'dir. 22 yaşındaki biri gruptan ayrılırsa kalan 4 kişinin yaş ortalaması kaç olur?',
 ['İlk toplam: 18 × 5 = 90.', 'Ayrılınca toplam: 90 − 22 = 68.', 'Yeni ortalama: 68 ÷ 4 = 17.'],
 '17',
 'Ortalamadan doğrudan yaş çıkarmak ya da yaş farkını yıllarla değiştirmek. Her zaman önce toplam yaşa geç; farkları aynı kişiden iki yolla bulup eşitle.',
 'Ortalamayı kişiyle çarp, toplama geç.')

ekle('prob-yas-problemleri-03', 'Doğum yılı ve yaş',
 'Doğum yılı ve takvim yılından yaşları, yaş farklarını ve kuşak aralıklarını bulabilmeni.',
 'Yaş = **takvim yılı − doğum yılı**. İki kişinin yaş farkı doğum yıllarının farkıdır ve değişmez. n kişi arasında **n − 1 aralık** vardır. Ortalama aralık için aralıkların toplamını n − 1\'e böl.',
 'yaş = takvim yılı − doğum yılı', sekil_zaman(),
 'Dede 1950, baba 1976, çocuk 2008 doğumludur. Üç kişi arasındaki kuşak aralıklarının ortalaması kaç yıldır?',
 ['Üç kişi arasında 2 aralık vardır.', 'Aralıklar: 1976 − 1950 = 26 ve 2008 − 1976 = 32.', 'Ortalama: (26 + 32) ÷ 2 = 29.'],
 '29 yıl',
 'Yalnız bir aralığı ortalama sanmak ya da aralıkların toplamını ortalama yazmak. Kaç kişi varsa aralık sayısı bir eksiktir; bölmeden önce aralıkları say.',
 'Üç kişi arasında iki aralık var.')

ekle('prob-yuzde-problemleri-01', 'İndirim ve KDV',
 'İndirim ve KDV\'yi liste fiyatının yüzdesi olarak hesaplayıp ödenecek tutarı bulabilmeni.',
 'İndirimli fiyat = etiket × (100 − indirim) ÷ 100: ödenen, **liste fiyatının kalan yüzdesidir**. KDV dahil fiyat = KDV hariç × (100 + KDV) ÷ 100. Önce bir ürünün fiyatını bul, sonra **adetle çarp**. Kupon ve kademe sorularında kuralı sırayla uygula.',
 'ödenen = etiket × (100 − indirim) ÷ 100', None,
 'Etiketi 800 TL olan montta %40 indirim yapılıyor. Böyle 2 mont için kaç TL ödenir?',
 ['%40 indirimde ödenen, liste fiyatının %60\'ıdır.', 'Bir mont: 800 × 0,60 = 480 TL.', 'İki mont: 2 × 480 = 960 TL.'],
 '960 TL',
 'İndirim tutarını ödenen tutar sanmak, adetle çarpmayı unutmak ya da %40\'ı 40 TL gibi düşmek. Sonda sorunun ödenen mi, indirim mi sorduğuna bak.',
 'İndirimde ödenen, kalan yüzdedir.')

ekle('prob-yuzde-problemleri-03', 'Yüzde kaç fazlası ve aktarım',
 'Yüzdenin hangi niceliğe göre alınacağını ayırt edip aktarım ve karşılaştırma sorularını çözebilmeni.',
 'Eşitlemede **farkın yarısı** aktarılır. "A, B\'nin yüzde kaç fazlası" sorusunda **fark ÷ B** alınır: yüzde, "-nin" dediğin niceliğe göre hesaplanır. Yüzde puan, iki yüzdenin farkıdır; yüzde değişim değildir. Aktarım yüzdesini çıkış yaptığı yere göre bul.',
 'yüzde = fark ÷ karşılaştırılan sayı × 100', None,
 'A kabında 80 L, B kabında 40 L su var. İki kap eşitlenene kadar A\'dan B\'ye su aktarılıyor. Aktarılan su, A\'daki başlangıç suyunun yüzde kaçıdır?',
 ['Fark: 80 − 40 = 40 L.', 'Eşitlemek için farkın yarısı aktarılır: 20 L.', 'A\'ya göre yüzde: 20 ÷ 80 × 100 = %25.'],
 '%25',
 'Aktarılan miktarı yanlış kaba bölmek ya da eşitlendikten sonraki mevcudu cevap sanmak. Yüzdenin neye göre sorulduğunu bul ve paydaya o sayıyı yaz.',
 'Paydaya sorulan niceliği yaz.')

ekle('prob-yuzde-problemleri-05', 'Parçadan bütüne yüzde',
 'Yüzdesi bilinen parçadan bütünü ve kalan kısmı bulup payı doğru bütüne oranlayabilmeni.',
 'Yüzdesi bilinen parçadan bütünü bulmak için **parça ÷ yüzde oranı** al. Yüzdeler toplamı %100\'dür: kalan kısım 100 − verilen yüzdedir. Payı bulurken **hangi bütüne göre** (toplam mı, geçerli mi) hesapladığına dikkat et. Oranı yüzdeye çevirmek için parça ÷ bütün × 100 yap.',
 'bütün = parça ÷ (yüzde ÷ 100)', None,
 'Bir sınıfın %30\'u gözlüklüdür. Gözlüksüz 28 öğrenci varsa sınıf mevcudu kaçtır?',
 ['Gözlüksüz öğrenciler %100 − %30 = %70\'tir.', 'Sınıfın %70\'i 28 ise bütün = 28 ÷ 0,70.', 'Mevcut 40 öğrencidir.'],
 '40 öğrenci',
 'Kalan kısmın yüzdesini istenen payla karıştırmak ya da payı yanlış bütüne oranlamak. Bütünün toplam mı, geçerli mi olduğunu yaz; paydaya o sayıyı koy.',
 'Önce bütünü, sonra payı bul.')

ekle('prob-isci-emek-01', 'Ayrılma ve sonradan katılma',
 'İşi evrelere ayırıp ayrılan ya da sonradan katılan kişilerle kalan işi hesaplayabilmeni.',
 'Bir işi a günde bitiren, günde işin **1/a\'sını** yapar. İşi evrelere ayır: her evrede çalışanların günlük işini topla, süreyle çarp. Kalan iş = 1 − yapılan iş. Bir kişinin toplam süresi sorulduysa **o kişinin bütün evrelerini** topla.',
 'kalan iş = 1 − (günlük iş × gün)', None,
 'Ali bir işi 12 günde, Veli 6 günde bitiriyor. İkisi 2 gün birlikte çalışıp Veli ayrılıyor. Ali kalan işi kaç günde bitirir?',
 ['Birlikte günlük iş: 1/12 + 1/6 = 1/4.', '2 günde yapılan iş: 2 · 1/4 = 1/2, kalan iş 1/2.', 'Ali günde 1/12 yapar: (1/2) ÷ (1/12) = 6 gün.'],
 '6 gün',
 'İlk evrede çalışan diğer kişinin işini saymamak ya da yalnız son evrenin süresini cevap yapmak. Her evre için kimin, kaç gün çalıştığını ayrı satıra yaz.',
 'Evreleri ayır, her evrenin işini yaz.')

ekle('prob-isci-emek-03', 'Birlikte çalışma ve ücret',
 'Birlikte çalışanların birim zamandaki işlerini toplayıp süre, verim ve ücret paylaşımını bulabilmeni.',
 'Birlikte çalışmada **süreler değil, birim zamandaki işler toplanır**. Günlük işlerin toplamı 1/t ise iş t günde biter. Eşit verimli işçilerde toplam iş = işçi × gün. Ücret, **yapılan işle orantılı** paylaştırılır.',
 '1/t = 1/a + 1/b', None,
 'Bir makine bir işi 20 günde, bir başkası 5 günde bitiriyor. İkisi birlikte çalışırsa iş kaç günde biter?',
 ['Günlük işler: 1/20 ve 1/5 = 4/20.', 'Birlikte: 1/20 + 4/20 = 5/20 = 1/4.', 'Günde işin 1/4\'ü bitiyorsa iş 4 günde biter.'],
 '4 gün',
 'Sürelerin ortalamasını ya da farkını almak. Birlikte çalışınca süre her ikisinden de kısadır; bulduğun sürenin en hızlı kişinin süresinden küçük olduğunu kontrol et.',
 'Süreleri değil, günlük işleri topla.')

# ---------- kapsam dışı / birleşen yok: tüm kazanımlar için kart yazıldı ----------

# ---------- girdi ile eşleştir, doğrula ----------
girdi = []
for ln in open(GIRDI, encoding='utf-8'):
    if ln.startswith('### '):
        p = [x.strip() for x in ln[4:].split(' | ')]
        girdi.append((p[0], p[1]))
ids = [g[0] for g in girdi]
assert len(ids) == 23 and set(ids) == set(C), (set(ids) ^ set(C))

def nw(s): return len(re.sub(r'\*\*', '', s).split())

cikti = []
for id_, k in girdi:
    c = C[id_]; c['k'] = k
    c = {kk: c[kk] for kk in ['id', 'k', 'baslik', 'olcer', 'kural', 'formul', 'sekil', 'ornek', 'hata', 'akilda']}
    cikti.append(c)
    for f in ['id', 'k', 'baslik', 'olcer', 'kural', 'hata', 'akilda']:
        assert c[f] and isinstance(c[f], str), (id_, f)
    assert nw(c['baslik']) <= 6, (id_, 'baslik', nw(c['baslik']))
    assert nw(c['olcer']) <= 25 and not c['olcer'].startswith('Bu soru'), (id_, 'olcer', nw(c['olcer']))
    assert nw(c['kural']) <= 60, (id_, 'kural', nw(c['kural']))
    assert nw(c['hata']) <= 40, (id_, 'hata', nw(c['hata']))
    assert nw(c['akilda']) <= 8 and '"' not in c['akilda'] and "'" not in c['akilda'], (id_, 'akilda', nw(c['akilda']))
    assert c['kural'].count('**') >= 2 and c['kural'].count('**') % 2 == 0, (id_, 'kalın')
    o = c['ornek']
    assert o['soru'] and o['cevap'] and 2 <= len(o['adimlar']) <= 4, (id_, 'ornek')
    if c['formul'] is not None:
        assert '\n' not in c['formul']
    if c['sekil'] is not None:
        assert len(c['sekil'].encode('utf-8')) <= 25000
        for m in re.finditer(r'font-size="(\d+)"', c['sekil']):
            assert int(m.group(1)) >= 11
assert len(cikti) == len(ids)
json.dump(cikti, open(CIKTI, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(cikti), 'kart;', sum(1 for c in cikti if c['sekil']), 'şekilli')
for c in cikti:
    if c['sekil']:
        open(f"/tmp/kor/kart/p13/{c['id']}.svg", 'w', encoding='utf-8').write(c['sekil'])
