#!/usr/bin/env python3
# p08 Konu Tekrarı kartları (kimya) -> kart-p08.json
import json, math, re, os

OUT = '/home/claude/zekacademy-app/havuz/tekrar/kart-p08.json'
GIRDI = '/tmp/kor/kart/parti/p08.txt'
TMP = '/tmp/kor/kart/p08'
os.makedirs(TMP, exist_ok=True)

INK = 'currentColor'
BR, RU, WA, ME = '#2f5bea', '#0f8a6a', '#c2410c', '#7c3aed'


def svg(w, h, aria, body):
    return (f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="{aria}" xmlns="http://www.w3.org/2000/svg">'
            f'<g font-family="Lexend,system-ui,sans-serif" font-size="12" fill="{INK}">{body}</g></svg>')


# ---------- ŞEKİLLER ----------
def sekil_ph():
    b = ''
    for i in range(14):
        t = i / 13
        if t < .5:
            c = f'rgb({int(220-120*t*2)},{int(70+120*t*2)},70)'
        else:
            u = (t - .5) * 2
            c = f'rgb({int(100-60*u)},{int(190-70*u)},{int(70+170*u)})'
        b += f'<rect x="{20+i*17.5}" y="50" width="17.5" height="34" fill="{c}" stroke="{INK}" stroke-width=".5"/>'
    for i in (0, 7, 14):
        b += f'<text x="{20+i*17.5-(4 if i<14 else 8)}" y="102" font-size="12">{i}</text>'
    b += f'<text x="30" y="40" font-size="13" font-weight="600">asit</text>'
    b += f'<text x="124" y="40" font-size="13" font-weight="600">nötr</text>'
    b += f'<text x="215" y="40" font-size="13" font-weight="600">baz</text>'
    b += f'<text x="60" y="128" font-size="12">baz eklenince pH artar →</text>'
    b += f'<text x="60" y="146" font-size="12">← asit eklenince pH azalır</text>'
    return svg(280, 160, 'pH ölçeği: 0 ile 7 arası asit, 7 nötr, 7 ile 14 arası baz', b)


def sekil_katman():
    cx, cy = 100, 85
    b = f'<circle cx="{cx}" cy="{cy}" r="9" fill="{WA}"/>'
    for r, n in ((24, 2), (44, 8), (64, 5)):
        b += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{INK}" stroke-width="1.5"/>'
        for k in range(n):
            a = 2 * math.pi * k / n - math.pi / 2
            b += f'<circle cx="{cx+r*math.cos(a):.1f}" cy="{cy+r*math.sin(a):.1f}" r="4.5" fill="{BR}"/>'
    b += f'<text x="190" y="52" font-size="12">K katmanı: 2</text>'
    b += f'<text x="190" y="85" font-size="12">L katmanı: 8</text>'
    b += f'<text x="190" y="118" font-size="12">M katmanı: 5</text>'
    b += f'<text x="190" y="146" font-size="12" font-weight="600">toplam: 15 e⁻</text>'
    return svg(280, 170, 'Üç katmanlı katman diyagramı: 2, 8 ve 5 elektron', b)


def sekil_buhar():
    b = f'<line x1="40" y1="140" x2="262" y2="140" stroke="{INK}" stroke-width="1.5"/>'
    b += f'<line x1="40" y1="140" x2="40" y2="14" stroke="{INK}" stroke-width="1.5"/>'
    b += f'<line x1="40" y1="50" x2="262" y2="50" stroke="{ME}" stroke-width="1.5" stroke-dasharray="5 3"/>'
    def egri(k, c, m=1.0):
        pts = []
        for i in range(0, 41):
            x = 40 + i * 5.2
            y = 140 - m * 125 * (math.exp(k * i / 40) - 1) / (math.exp(k) - 1)
            pts.append(f'{x:.1f},{y:.1f}')
        return f'<polyline points="{" ".join(pts)}" fill="none" stroke="{c}" stroke-width="2.5"/>'
    b += egri(3.2, RU) + egri(4.4, WA, .85)
    b += f'<text x="46" y="44" font-size="12" fill="{ME}">dış basınç</text>'
    b += f'<text x="150" y="30" font-size="13" font-weight="600" fill="{RU}">B</text>'
    b += f'<text x="214" y="30" font-size="13" font-weight="600" fill="{WA}">A</text>'
    b += f'<text x="190" y="156" font-size="12">Sıcaklık</text>'
    b += f'<text x="4" y="12" font-size="12">Buhar basıncı</text>'
    return svg(280, 164, 'Buhar basıncı sıcaklık grafiği: B eğrisi dış basınca daha düşük sıcaklıkta ulaşır', b)


def sekil_gaz():
    b = ''
    for x0, w, pozisyon in ((20, 100, 'önce'), (170, 55, 'sonra')):
        b += f'<rect x="{x0}" y="40" width="{w}" height="100" fill="none" stroke="{INK}" stroke-width="2"/>'
        b += f'<text x="{x0+w/2-14}" y="32" font-size="12">{pozisyon}</text>'
    pts1 = [(35, 60), (70, 55), (100, 70), (50, 90), (85, 100), (35, 120), (70, 130), (105, 120)]
    pts2 = [(182, 60), (205, 58), (190, 80), (213, 85), (182, 100), (205, 108), (190, 125), (212, 128)]
    for x, y in pts1 + pts2:
        b += f'<circle cx="{x}" cy="{y}" r="5" fill="{BR}"/>'
    b += f'<path d="M130,90 L158,90" stroke="{INK}" stroke-width="2" fill="none"/><path d="M152,84 L160,90 L152,96" stroke="{INK}" stroke-width="2" fill="none"/>'
    b += f'<text x="20" y="158" font-size="12">boşluk çok</text><text x="165" y="158" font-size="12">boşluk az</text>'
    return svg(280, 168, 'Sıkıştırılan gazda taneciklerin boyu aynı kalır, aralarındaki uzaklık azalır', b)


def sekil_kati():
    b = ''
    xs = [30 + i * 32 for i in range(3)]
    ys = [50 + j * 32 for j in range(3)]
    for x in xs:
        b += f'<line x1="{x}" y1="{ys[0]}" x2="{x}" y2="{ys[-1]}" stroke="{INK}" stroke-width="2"/>'
    for y in ys:
        b += f'<line x1="{xs[0]}" y1="{y}" x2="{xs[-1]}" y2="{y}" stroke="{INK}" stroke-width="2"/>'
    for x in xs:
        for y in ys:
            b += f'<circle cx="{x}" cy="{y}" r="6" fill="{BR}"/>'
    b += f'<text x="22" y="28" font-size="12" font-weight="600">kovalent ağ</text>'
    b += f'<text x="14" y="134" font-size="12">tüm bağlar kopar</text>'
    for mx, my in ((170, 55), (225, 55), (170, 100), (225, 100)):
        b += f'<line x1="{mx}" y1="{my}" x2="{mx+18}" y2="{my}" stroke="{INK}" stroke-width="2"/>'
        b += f'<circle cx="{mx}" cy="{my}" r="6" fill="{RU}"/><circle cx="{mx+18}" cy="{my}" r="6" fill="{RU}"/>'
    b += f'<line x1="196" y1="55" x2="219" y2="55" stroke="{WA}" stroke-width="1.5" stroke-dasharray="3 3"/>'
    b += f'<line x1="196" y1="100" x2="219" y2="100" stroke="{WA}" stroke-width="1.5" stroke-dasharray="3 3"/>'
    b += f'<text x="170" y="28" font-size="12" font-weight="600">moleküler</text>'
    b += f'<text x="150" y="134" font-size="12">zayıf çekim gevşer</text>'
    return svg(280, 160, 'Kovalent ağ katıda atomlar ağ biçiminde bağlı; moleküler katıda moleküller zayıf kuvvetle bir arada', b)


def sekil_iyonlasma():
    degerler = [738, 1450, 7730, 10540]
    b = f'<line x1="40" y1="140" x2="262" y2="140" stroke="{INK}" stroke-width="1.5"/>'
    b += f'<line x1="40" y1="140" x2="40" y2="14" stroke="{INK}" stroke-width="1.5"/>'
    for i, v in enumerate(degerler):
        h = 118 * v / 10540
        x = 62 + i * 50
        c = WA if i == 2 else BR
        b += f'<rect x="{x}" y="{140-h:.1f}" width="32" height="{h:.1f}" fill="{c}"/>'
        b += f'<text x="{x+6}" y="156" font-size="12">IE{i+1}</text>'
    b += f'<text x="4" y="12" font-size="12">Enerji (kJ/mol)</text>'
    b += f'<text x="60" y="40" font-size="12" fill="{WA}">büyük sıçrama (IE3)</text>'
    return svg(280, 164, 'Ardışık iyonlaşma enerjileri: üçüncü enerjide büyük sıçrama var', b)


# ---------- KARTLAR ----------
K = []


def kart(id, baslik, olcer, kural, formul, sekil, soru, adimlar, cevap, hata, akilda):
    K.append({'id': id, 'k': 'kim|' + id_to_k[id], 'baslik': baslik, 'olcer': olcer, 'kural': kural,
              'formul': formul, 'sekil': sekil,
              'ornek': {'soru': soru, 'adimlar': adimlar, 'cevap': cevap},
              'hata': hata, 'akilda': akilda})


# anahtar: girdideki ikinci alan
ham = open(GIRDI, encoding='utf-8').read()
basliklar = [l[4:].split(' | ') for l in ham.splitlines() if l.startswith('### ')]
girdi_idler = [b[0].strip() for b in basliklar]
id_to_k = {b[0].strip(): b[1].strip() for b in basliklar}
# k alanı girdideki anahtarın aynısı olmalı (örn. "kim|Asitler, Bazlar ve Tuzlar")
def kart(id, baslik, olcer, kural, formul, sekil, soru, adimlar, cevap, hata, akilda):  # noqa: F811
    K.append({'id': id, 'k': id_to_k[id], 'baslik': baslik, 'olcer': olcer, 'kural': kural,
              'formul': formul, 'sekil': sekil,
              'ornek': {'soru': soru, 'adimlar': adimlar, 'cevap': cevap},
              'hata': hata, 'akilda': akilda})


# 1 ----------------------------------------------------------------
kart('kim-asitler-bazlar-01', 'Günlük hayatta asit, baz ve tuz',
     'Günlük hayattaki asit, baz ve tuzların özelliklerini ve asit yağmurunu doğru ifadelerle eşleştirebilmeni.',
     'pH değeri 7\'den küçükse madde asidik, büyükse bazik, eşitse nötrdür. **Sabun, kireç suyu ve çamaşır suyu bazik**; limon, sirke ve mide özsuyu asidiktir. SO₂ ve NO₂ gazları yağmur suyunda çözünüp **asit yağmuru** oluşturur. Tuzların da gübre, alçı gibi kullanım alanları vardır.',
     'pH < 7 asit · pH = 7 nötr · pH > 7 baz', None,
     'Limonlu su, sabunlu su ve saf suyu pH\'a göre nasıl sınıflarsın?',
     ['Limonlu su ekşidir ve pH\'ı 7\'den küçüktür: asit.',
      'Sabunlu su bazik özelliktedir, pH\'ı 7\'den büyüktür: baz.',
      'Saf suyun pH\'ı tam 7\'dir: nötr.'],
     'Limonlu su asit, sabunlu su baz, saf su nötr.',
     'Doğru ifadeyi yanlış sanmak: asit ve bazlar suda iyon verdiği için sulu çözeltileri elektriği iletir. Olumsuz kökte ifadeleri tek tek sına, bilimsel gerçekle çelişen tek ifade cevaptır.',
     'Sabun bazik, limon asidik.')

# 2 ----------------------------------------------------------------
kart('kim-asitler-bazlar-03', 'İndikatör, pH ve asit özellikleri',
     'Turnusol ve fenolftalein renklerinden ve pH değerinden çözeltinin asit, baz ya da nötr olduğunu belirleyebilmeni.',
     'Asit mavi turnusolu kırmızıya, **baz kırmızı turnusolu maviye** çevirir ve fenolftaleini pembe yapar. Nötr çözelti renk değiştirmez. Asit sulu çözeltisinde iyon verir, elektriği iletir; aktif metalle tepkimesinde **hidrojen gazı** çıkar. pH küçüldükçe asitlik artar.',
     'pH < 7 asit · pH = 7 nötr · pH > 7 baz', sekil_ph(),
     'pH\'ı 3 olan X ile pH\'ı 6 olan Y çözeltisi var. Hangisi daha asidiktir? X\'e baz eklenirse pH nasıl değişir?',
     ['pH ne kadar küçükse çözelti o kadar asidiktir: 3 < 6.',
      'Demek ki X daha asidiktir.',
      'Asite baz eklenince asitlik azalır, pH artar ve 7\'ye doğru yükselir.'],
     'X daha asidik; baz eklenince pH artar.',
     'Aktif metal ile asit tepkimesinde oksijen çıktığını sanmak. Çıkan gaz hep hidrojendir. Ayrıca pH 2\'yi pH 5\'ten daha az asidik sanmak da sık görülür.',
     'Asit + aktif metal: hidrojen.')

# 3 ----------------------------------------------------------------
# hesap
e = 2 + 8 + 5; nötron = 16
assert e == 15 and e + nötron == 31
kart('kim-atom-ve-02', 'Katman diyagramından atom numarası',
     'Katman diyagramındaki elektronları sayıp atom numarasını, kütle numarasını ve tanecik türünü bulabilmeni.',
     'Her çember bir katmandır, noktalar elektrondur. **Nötr atomda elektron sayısı proton sayısına, yani atom numarasına eşittir.** Kütle numarası proton ile nötron toplamıdır. Proton elektrondan fazlaysa katyon, azsa anyondur. K katmanı en çok 2, L en çok 8 elektron alır.',
     'Kütle no = proton + nötron', sekil_katman(),
     'Katmanlarında 2, 8 ve 5 elektron bulunan nötr atomun 16 nötronu varsa kütle numarası kaçtır?',
     ['Toplam elektron: 2 + 8 + 5 = 15.',
      'Nötr atomda proton = elektron, atom numarası 15.',
      'Kütle numarası = 15 + 16 = 31.'],
     'Atom numarası 15, kütle numarası 31.',
     'Atom numarasını kütle numarası sanmak ya da son katmandaki elektronları nötron diye toplamaya eklemek. Elektronlar çekirdekte değil katmanlardadır, kütle numarasına girmez.',
     'Toplam elektron, nötr atomun atom numarasıdır.')

# 4 ----------------------------------------------------------------
X = (17, 35); Y = (17, 37); Z = (18, 37)
nX, nY, nZ = X[1]-X[0], Y[1]-Y[0], Z[1]-Z[0]
assert (nX, nY, nZ) == (18, 20, 19)
assert X[0] == Y[0] and Y[1] == Z[1] and len({nX, nY, nZ}) == 3
kart('kim-atom-ve-04', 'İzotop, izobar, izoton ve ortalama kütle',
     'Atomların proton, nötron ve kütle numarasını karşılaştırıp izotop, izobar ve izoton ilişkisini ayırt edebilmeni.',
     'Önce her atomun proton ve nötron sayısını yaz. **İzotop: proton aynı. İzobar: kütle numarası aynı. İzoton: nötron aynı.** Proton ve nötronun kütlesi yaklaşık eşit, elektron çok hafiftir. Ortalama atom kütlesi, izotop kütlelerinin bolluk oranıyla ağırlıklı ortalamasıdır.',
     'Nötron = kütle no − proton no', None,
     '₁₇X³⁵, ₁₇Y³⁷ ve ₁₈Z³⁷ atomlarından hangi çiftler izotop, hangileri izobardır?',
     ['Nötronlar: X için 35 − 17 = 18, Y için 37 − 17 = 20, Z için 37 − 18 = 19.',
      'Proton sayısı aynı olan X ile Y izotoptur.',
      'Kütle numarası aynı olan Y ile Z izobardır; nötron sayıları 18, 20, 19 olduğundan izoton çifti yoktur.'],
     'X–Y izotop, Y–Z izobar.',
     'İzo- sözcüklerini ezberden karıştırmak ve nötron sayısını hesaplamadan izoton demek. Sayıları yazmadan karar verme, her atom için proton ve nötronu yan yana yaz.',
     'Proton aynıysa izotop, kütle aynıysa izobar.')

# 5 ----------------------------------------------------------------
kart('kim-karisimlar-02', 'Karışım türleri ve ayırma',
     'Tanecik modeli ve gözlemden saf madde, homojen ya da heterojen karışımı ve çözelti, kolloit, süspansiyonu ayırt edebilmeni.',
     'Saf madde tek tür tanecikten oluşur. İki tür tanecik **her yerde düzgün karışmışsa homojen**, ayrı bölgelerde toplanmışsa **heterojen** karışımdır. Çözelti ışığı saçmaz, çökmez. Kolloit ışığı saçar, çökmez. Süspansiyon ışığı saçar, bekletilince çöker, süzgeçte kalır.',
     'Çözelti · Kolloit · Süspansiyon: ışık, süzgeç, çökme', None,
     'Bir karışım ışığı saçıyor, süzgeçten geçiyor ve bekletilince çökmüyor. Karışım hangi türdür?',
     ['Işığı saçtığı için çözelti olamaz; çözelti ışığı saçmaz.',
      'Bekletilince çökmediği için süspansiyon da olamaz.',
      'Işığı saçıp süzgeçten geçen ve çökmeyen karışım kolloittir.'],
     'Kolloit.',
     'Tek fazlı görünen her karışımı çözelti saymak ya da iki tür tanecik ayrı bölgelerdeyken karışımı homojen demek. Önce taneciklerin dağılışına bak, sonra ışık, süzgeç ve çökme gözlemlerine.',
     'Her yerde aynıysa homojen, ayrıysa heterojen.')

# 6 ----------------------------------------------------------------
m_cz = 150; yuzde = 20
tuz = m_cz * yuzde / 100
assert tuz == 30
yeni = tuz / (m_cz - 50) * 100
assert yeni == 30
kart('kim-karisimlar-04', 'Derişim: yüzde, ppm, seyreltme',
     'Kütlece ya da hacimce yüzdeden çözünen ve çözücü miktarını bulup buharlaştırma ve karıştırma sorularını çözebilmeni.',
     '**Yüzde derişim = çözünen ÷ çözelti × 100.** Çözücü miktarı, çözeltiden çözüneni çıkararak bulunur. Seyreltmede ve karıştırmada **çözünen miktarı toplanır**. Buharlaştırmada yalnız çözücü azalır, çözünen sabit kalır. Sulu çözeltide 1 ppm = 1 mg çözünen / 1 kg çözelti.',
     'Yüzde = çözünen / çözelti × 100', None,
     'Kütlece %20\'lik 150 g tuzlu sudan 50 g su buharlaştırılırsa yeni derişim yüzde kaç olur?',
     ['Çözünen tuz: 150 × 20 / 100 = 30 g. Buharlaşmada değişmez.',
      'Yeni çözelti kütlesi: 150 − 50 = 100 g.',
      'Derişim: 30 / 100 × 100 = %30.'],
     '%30',
     'Soruda suyun yüzdesi ya da hacmi sorulurken çözünenin değerini yazmak. Yüzde değerini mL ya da g sanmak da sık görülür. Cevaptan önce sorunun neyi istediğini bir daha oku.',
     'Çözünen sabit, çözelti değişir.')

# 7 ----------------------------------------------------------------
kart('kim-kimya-bilimi-02', 'Kimya disiplinleri ve simya',
     'Bir çalışmanın hangi kimya dalına girdiğini amacına bakarak seçebilmeni ve simyanın kimyaya katkısını bilmeni.',
     'Dalı çalışmanın **amacı** belirler. Madde türünü ve miktarını belirleyen dal **analitik kimyadır**. Canlılardaki olayları inceleyen dal biyokimya, maddenin yapısını ve tepkimelerini inceleyen dal organik ve anorganik kimyadır. Simyacılar altın yapmaya çalışırken damıtma ve süzme gibi yöntemleri geliştirdi.',
     None, None,
     'Bir fabrika, atık sudaki kurşun miktarını ölçüyor. Bu çalışma hangi kimya dalına girer?',
     ['Çalışmada maddenin kendisi değil, ne kadar bulunduğu soruluyor.',
      'Madde türünü ve miktarını belirleme analitik kimyanın işidir.',
      'Su numunesi canlıyla ilgili olmadığından biyokimya değildir.'],
     'Analitik kimya.',
     'Disiplini numunenin türüne bakarak seçmek, örneğin sudan dolayı biyokimya demek. Numune ne olursa olsun disiplini çalışmanın amacı belirler: tür mü, miktar mı, üretim mi?',
     'Dalı, maddeye değil amaca bakarak seç.')

# 8 ----------------------------------------------------------------
birim_atom = 2 + 3 + 1
assert birim_atom * 200 == 1200
kart('kim-kimya-her-01', 'Polimerler ve geri dönüşüm',
     'Polimerin monomerini, tekrar eden birimini ve zincirdeki toplam atom sayısını bulabilmeni.',
     'Monomer, polimeri oluşturan küçük moleküldür. Polimerde **tekrar eden birim** zincir boyunca sıralanır. Monomerin çift bağı açılarak polimer oluşur. **Zincirdeki atom sayısı = birimdeki atom sayısı × birim sayısı.** Geri dönüşüm hammadde ve enerji tasarrufu sağlar.',
     'Toplam atom = birimdeki atom × birim sayısı', None,
     'Tekrar eden birimi C₂H₃Cl olan polimerde 200 birim varsa zincirde toplam kaç atom bulunur?',
     ['Birimdeki atomlar: 2 C + 3 H + 1 Cl = 6 atom.',
      'Birim sayısıyla çarp: 6 × 200 = 1200.'],
     '1200 atom',
     'Yalnız karbon ya da yalnız bir cins atomu saymak. Birimdeki her atomu, indisleriyle birlikte topla. Formülde indis yazmayan atomun sayısı 1\'dir.',
     'Önce birimdeki tüm atomları say.')

# 9 ----------------------------------------------------------------
kart('kim-kimya-her-03', 'Gıda katkıları ve saklama',
     'Gıda saklama yöntemlerinin ilkesini ve katkı kodları ile güvenlik işaretlerinin anlamını değerlendirebilmeni.',
     'Gıda saklamanın amacı **mikroorganizmaların çoğalmasını engellemektir**. Isıtma onları öldürür; kurutma, tuzlama ve şekerleme onların ihtiyaç duyduğu suyu azaltır. Soğuk onları öldürmez, yalnız yavaşlatır. E kodlu katkılar kullanım izni olan maddelerdir, sayı grubu gösterir.',
     None, None,
     'Reçelde yüksek şeker oranı gıdanın bozulmasını neden geciktirir?',
     ['Mikroorganizmaların çoğalması için suya ihtiyaç vardır.',
      'Çok şeker, ortamdaki suyu tutar ve mikroorganizmaların kullanabileceği su azalır.',
      'Böylece mikroorganizmalar çoğalamaz, bozulma gecikir.'],
     'Şeker suyu tutar, mikroorganizma çoğalamaz.',
     'Soğutmanın mikroorganizmaları öldürdüğünü sanmak. Soğuk ancak çoğalmayı yavaşlatır. Ayrıca olumsuz kökte doğru ifadeleri yanlış sanıp elemek sık yapılan bir hatadır.',
     'Saklama, mikroorganizmaları durdurmaktır.')

# 10 ---------------------------------------------------------------
y1, y2 = 16, 32
oran = y2 // y1
assert y2 % y1 == 0 and oran == 2 and 2 * oran == 4
kart('kim-kimyanin-temel-02', 'Katlı oranlar kanunu',
     'Aynı iki elementten oluşan iki bileşikte kütle oranından ikinci bileşiğin formülünü bulabilmeni.',
     'Aynı iki elementten oluşan bileşiklerde **birinin sabit kütlesiyle birleşen diğerinin kütleleri arasında küçük tam sayılı oran vardır.** Önce sabit elementin kütlesini eşitle, sonra öteki elementin kütle oranını bul. Bu oranı ilgili indise çarparak yeni formüle ulaş.',
     'Oran = Y₂ / Y₁ → yeni indis = eski indis × oran', None,
     'I. bileşik XY₂\'dir; 6 g X ile 16 g Y birleşiyor. II. bileşikte 6 g X ile 32 g Y birleşiyorsa II. bileşiğin formülü nedir?',
     ['X kütlesi iki bileşikte de 6 g, yani sabit.',
      'Y kütleleri oranı: 32 / 16 = 2.',
      'I. bileşikteki Y indisi 2 olduğundan II. bileşikte 2 × 2 = 4 olur.'],
     'XY₄',
     'Kütle oranını doğrudan indis sanmak ya da indise eklemek. Oran, eski indisle çarpılır. Sabit elementin kütlesi eşit değilse önce eşitle.',
     'Oranı indisle çarp, ekleme.')

# 11 ---------------------------------------------------------------
assert 8 + 32 - 22 == 18
kart('kim-kimyanin-temel-04', 'Kütlenin korunumu',
     'Kapalı ve açık kapta tepkimeden önce ve sonraki kütleleri kütlenin korunumuyla karşılaştırabilmeni.',
     '**Kapalı kapta girenlerin toplam kütlesi ürünlerin toplam kütlesine eşittir.** Bilinmeyen bir kütle varsa iki tarafın toplamını eşitle. Açık kapta gaz kaçabileceğinden kap kütlesi değişebilir. Denklemi denkleştirmek atom sayısını eşitler, kütle zaten korunur.',
     'Σ m(giren) = Σ m(ürün)', None,
     'Kapalı kapta 8 g CH₄ ile 32 g O₂ tam verimle tepkimeye girip 22 g CO₂ oluşturuyor. Oluşan H₂O kaç gramdır?',
     ['Girenlerin toplamı: 8 + 32 = 40 g.',
      'Ürünlerin toplamı da 40 g olmalıdır.',
      'H₂O = 40 − 22 = 18 g.'],
     '18 g',
     'Girenlerden yalnız birinin kütlesini ürün sanmak ya da mol kütlesini harcanan madde kütlesi saymak. Soruda verilen gram değerleriyle iki tarafı toplayıp eşitle.',
     'Giren toplam kütle, ürün toplam kütleye eşit.')

# 12 ---------------------------------------------------------------
n_nh3 = 1.5
n_h2 = n_nh3 * 3 / 2
v = round(n_h2 * 22.4, 1)
assert n_h2 == 2.25 and v == 50.4
kart('kim-kimyasal-hesaplamalar-02', 'Tepkimede mol, kütle ve hacim',
     'Denkleştirilmiş tepkimedeki katsayılardan mol oranı kurup kütle ve normal koşullardaki gaz hacmini hesaplayabilmeni.',
     '**Katsayı oranı mol oranıdır.** Önce verilen maddeyi mole çevir: n = kütle ÷ mol kütlesi. Sonra katsayılarla istenen maddenin molünü bul. Son adımda grama ya da hacme dön: **NK\'da 1 mol gaz 22,4 L** kaplar.',
     'n = m / M · V(NK) = n × 22,4 L', None,
     'N₂ + 3H₂ → 2NH₃ tepkimesinde 1,5 mol NH₃ oluşması için NK\'da kaç litre H₂ harcanır?',
     ['Katsayılar: 3 mol H₂ ile 2 mol NH₃ oluşur.',
      'H₂ molü: 1,5 × 3 / 2 = 2,25 mol.',
      'Hacim: 2,25 × 22,4 = 50,4 L.'],
     '50,4 L',
     'Katsayıyı kullanmadan molleri eşit almak ya da yanlış maddenin katsayısını kullanmak. İstenen ve verilen maddenin katsayısını ayrı ayrı yaz, oranı bunlarla kur.',
     'Katsayı oranı, mol oranıdır.')

# 13 ---------------------------------------------------------------
n = 34 / 17
atom_mol = n * 4
assert n == 2 and atom_mol == 8 and 8 * 6 == 48
kart('kim-kimyasal-hesaplamalar-04', 'Mol, tanecik ve atom sayısı',
     'Kütleden mol, molekül ve toplam atom sayısına ilerleyip farklı gazları karşılaştırabilmeni.',
     '**Mol sayısı n = kütle ÷ mol kütlesi.** 1 mol = 6 × 10²³ tanecik. Molekül sayısı n × NA\'dır. **Atom sayısı = mol × molekül başına atom × NA.** Molekülün her cins atomunu sayarak topla, örneğin NH₃\'te 1 N ve 3 H, yani 4 atom vardır.',
     'Atom sayısı = n × (molekülündeki atom) × NA', None,
     '34 g NH₃ (mol kütlesi 17 g/mol) kaç atom içerir? (NA = 6 × 10²³)',
     ['Mol sayısı: 34 / 17 = 2 mol NH₃.',
      'Bir NH₃ molekülünde 1 + 3 = 4 atom var: 2 × 4 = 8 mol atom.',
      'Atom sayısı: 8 × 6 × 10²³ = 4,8 × 10²⁴.'],
     '4,8 × 10²⁴ atom',
     'Molekül sayısında durup atom sayısına geçmemek ya da yalnız tek cins atomu saymak. Soru "atom" diyorsa molekül başına tüm atomlar çarpılır.',
     'Mol, molekül başına atom, sonra NA.')

# 14 ---------------------------------------------------------------
bag = {'H': 1, 'C': 4, 'N': 3}
assert bag['H'] + bag['C'] + bag['N'] == 8  # H-C≡N: C 1 + 3 = 4, N 3
assert 4 - 1 == 3 == bag['N']
kart('kim-kimyasal-turler-02', 'Lewis yapısı ve bağ polarlığı',
     'Atomların yapması gereken bağ sayısından çoklu bağı bulabilmeni ve elektronegatiflik farkından bağ polarlığını karşılaştırabilmeni.',
     'Ametal atom oktetini tamamlamak için **8 − değerlik elektronu** kadar bağ yapar: H 1, O 2, N 3, C 4. Tek bağla doymayan atomlar **çift ya da üçlü bağ** kurar. Elektronegatiflik farkı büyüdükçe bağ daha polardır; aynı atomlar arasındaki bağ apolardır.',
     'H 1 · O 2 · N 3 · C 4 bağ', None,
     'HCN molekülünde (H, C, N atomları bu sırayla bağlı) C ile N arasında kaç bağ vardır?',
     ['H bir bağ yapar: H–C. C dört bağ yapacağından 3 bağı daha var.',
      'N üç bağ yapmalıdır ve N\'nin başka komşusu yok.',
      'C ile N arasında 3 ortak çift gerekir: H–C≡N.'],
     'Üçlü bağ.',
     'H₂O ya da NH₃ gibi moleküllerde çoklu bağ aramak ya da CO₂ ve C₂H₄\'teki çift bağı atlamak. Önce her atomun bağ sayısını yaz, eksik kalan bağlar çoklu bağdır.',
     'Bağ sayısı eksikse çoklu bağ kur.')

# 15 ---------------------------------------------------------------
kart('kim-kimyasal-turler-04', 'Katı türleri ve erime noktası',
     'Erime noktası ve yapı bilgisinden kovalent ağ ile moleküler katıyı ayırt edip erimede hangi etkileşimin koptuğunu bilmeni.',
     '**Kovalent ağ katılarda** (elmas, kuvars) atomlar ağ biçiminde bağlıdır; erimek için kovalent bağlar kopar, erime noktası çok yüksektir. **Moleküler katılarda** erirken yalnız moleküller arası zayıf kuvvetler gevşer, molekül içi bağlar kopmaz, erime noktası düşüktür.',
     'Çok yüksek erime noktası → ağ · düşük → moleküler', sekil_kati(),
     'Naftalin 80 °C\'de, kuvars 1700 °C\'de eriyor. Hangisi erirken kovalent bağlar kopar?',
     ['Naftalinin erime noktası düşüktür: moleküler katıdır.',
      'Moleküler katı erirken yalnız zayıf çekim kuvvetleri gevşer.',
      'Kuvars çok yüksek sıcaklıkta erir: ağ yapılıdır, erimede kovalent bağlar kopar.'],
     'Kuvars.',
     'Erimede molekül içi bağların koptuğunu sanmak. N≡N gibi bir bağ erirken kopmaz. Düşük erime noktası, moleküller arası çekimlerin zayıflığından kaynaklanır.',
     'Moleküler katı erirken molekül bozulmaz.')

# 16 ---------------------------------------------------------------
kart('kim-maddenin-halleri-01', 'Buharlaşma ve buhar basıncı',
     'Buharlaşma hızını etkileyen etmenleri ve buhar basıncıyla kaynama noktası ilişkisini yorumlayabilmeni.',
     'Sıcaklık ve yüzey alanı arttıkça **buharlaşma hızlanır**. Buharlaşma her sıcaklıkta yüzeyde, kaynama belirli sıcaklıkta her yerde olur. Buhar basıncı sıcaklıkla artar, sıvı miktarına bağlı değildir. **Buhar basıncı dış basınca eşitlenince sıvı kaynar**; buhar basıncı büyük olan daha düşük sıcaklıkta kaynar.',
     'Buhar basıncı = dış basınç → kaynama', sekil_buhar(),
     'Aynı sıcaklıkta A sıvısının buhar basıncı 40, B sıvısınınki 90 mmHg ise hangisinin kaynama noktası daha düşüktür?',
     ['Buhar basıncı büyük olan sıvı daha kolay buharlaşır, yani daha uçucudur.',
      'B daha kolay buharlaştığı için dış basınca daha düşük sıcaklıkta ulaşır.'],
     'B sıvısı.',
     'Yüzey alanı ya da sıcaklığın etkisini ters yorumlamak. İkisi de arttıkça buharlaşma hızlanır. Süre ile hız ters yönde sıralanır: hızlı olan kısa sürede biter.',
     'Sıcak ve geniş yüzey, çabuk buharlaşır.')

# 17 ---------------------------------------------------------------
kart('kim-maddenin-halleri-03', 'Viskozite ve yüzey gerilimi',
     'Bilyenin düşme süresinden viskoziteyi ve sıcaklık ile tanecikler arası etkileşimin sıvı özelliklerine etkisini yorumlayabilmeni.',
     '**Viskozite akmaya karşı dirençtir.** Tanecikler arası etkileşim arttıkça artar, sıcaklık arttıkça azalır. Akışkanlık viskozitenin tersidir. Bilye sıvıda geç iniyorsa viskozite büyüktür. Yüzey gerilimi, yüzeydeki moleküllerin içeri çekilmesiyle yüzeyin gergin zar gibi davranmasıdır.',
     'Viskozite ↑ → akışkanlık ↓', None,
     'Aynı sıcaklıkta bilye X sıvısında 6 s, Y sıvısında 2 s\'de iniyor. Hangisinin viskozitesi büyük, hangisi daha akışkandır?',
     ['Bilye X\'te daha geç indiği için X akmaya daha çok direnir.',
      'Demek ki X\'in viskozitesi büyüktür, X\'te tanecikler arası etkileşim daha güçlüdür.',
      'Akışkanlık viskozitenin tersidir: Y daha akışkandır.'],
     'X\'in viskozitesi büyük, Y daha akışkan.',
     'Viskoziteyi sıcaklıkla aynı yönde değiştiğini sanmak. Isınınca viskozite azalır, akışkanlık artar. Küçük viskoziteyi yanlış yorumlayıp akıcılığın düştüğünü düşünmek de sık görülür.',
     'Bilye geç iniyorsa viskozite büyük.')

# 18 ---------------------------------------------------------------
kart('kim-maddenin-halleri-05', 'Gazların özellikleri ve basıncı',
     'Gazların sıkıştırılabilirliğini, difüzyonu ve basıncı tanecik hareketi ile uzaklığına dayanarak açıklayabilmeni.',
     'Gazlarda tanecikler arası boşluk çok büyüktür, bu yüzden **gaz kolay sıkıştırılır**. Sıkıştırınca taneciklerin boyu değil, **aralarındaki uzaklık azalır**. Sıvı ve katıda boşluk az olduğundan zor sıkışır. Difüzyon sıcaklıkla hızlanır. Basınç taneciklerin duvara çarpmasından doğar.',
     None, sekil_gaz(),
     'Hava dolu şırınganın pistonu itilip hacim yarıya indiriliyor. Tanecik sayısı, tanecik boyu ve tanecikler arası uzaklık nasıl değişir?',
     ['Şırınga kapalı, tanecik sayısı değişmez.',
      'Taneciklerin kendisi küçülmez, boyları aynı kalır.',
      'Yalnız aralarındaki uzaklık azalır.'],
     'Sayı ve boy aynı kalır, uzaklık azalır.',
     'Gaz sıkıştırılınca taneciklerin küçüldüğünü sanmak. Küçülen taneciklerin kendisi değil, aralarındaki boşluktur. Sıvıların neredeyse sıkışmamasını da boşluğun azlığıyla açıkla.',
     'Sıkışan boşluktur, tanecik değil.')

# 19 ---------------------------------------------------------------
ie = [738, 1450, 7730, 10540]
sicrama = [ie[i+1] / ie[i] for i in range(3)]
assert sicrama.index(max(sicrama)) == 1  # 2. ile 3. arasında sıçrama -> 2 değerlik elektronu
kart('kim-periyodik-sistem-01', 'İyonlaşma enerjisi ve iyon yarıçapı',
     'Ardışık iyonlaşma enerjilerinden grubu bulabilmeni ve elektron sayısı eşit iyonları proton sayısına göre karşılaştırabilmeni.',
     'Her elektron koparken gereken enerji artar. **Değerlik elektronları bitince enerji aniden büyük sıçrar**; sıçramadan önceki sayı değerlik elektronudur. Bir periyotta iyonlaşma enerjisi genelde artar. **Elektron sayısı eşit iyonlarda proton arttıkça yarıçap küçülür.**',
     'Sıçramadan önceki enerji sayısı = değerlik elektronu', sekil_iyonlasma(),
     'Bir atomun ardışık iyonlaşma enerjileri 738, 1450, 7730, 10540 kJ/mol\'dür. Atom kaç değerlik elektronludur?',
     ['Enerjiler arası oranlar: 1450/738 ≈ 2, 7730/1450 ≈ 5,3, 10540/7730 ≈ 1,4.',
      'Büyük sıçrama 2. ile 3. enerji arasındadır.',
      'İki elektron kolay koptu: 2 değerlik elektronu (2A grubu).'],
     '2 değerlik elektronu, 2A grubu.',
     'Elektron sayısı eşit iyonlarda yarıçapı katman sayısıyla yorumlamak. Hepsinin katmanı aynıdır, fark proton sayısındadır. Proton fazla olan iyon daha küçüktür.',
     'Elektron eşitse proton belirler.')

# 20 ---------------------------------------------------------------
z = 35
dizilim = [2, 8, 18]
son = z - sum(dizilim)
assert son == 7
kart('kim-periyodik-sistem-03', 'Periyot, grup ve atom numarası',
     'Atom numarası, iyon ya da tablodaki konumdan elementin periyodunu, grubunu ve B grubu olup olmadığını belirleyebilmeni.',
     'Katman sayısı periyodu, **son katmandaki elektron sayısı A grubunu** gösterir. İyonda atomun elektronunu bulmak için katyonda yükü ekle, anyonda yükü çıkar. Tabloda etiketsiz orta sütunlar **B grubudur** (4. periyottan itibaren). Her periyodun son sütunu soy gazdır.',
     'Periyot = katman sayısı · Grup = son katman e⁻', None,
     'Atom numarası 35 olan elementin periyodunu ve grubunu bul.',
     ['Elektron dizilimi: 2, 8, 18, 7 (toplam 35).',
      'Dört katman var: 4. periyot.',
      'Son katmanda 7 elektron var: 7A grubu (halojen).'],
     '4. periyot, 7A grubu.',
     'Etiketsiz orta sütunları A grubu sanmak ya da aynı sütundaki elementleri aynı grup saymayı unutmak. Önce konumu elektron dizilimiyle doğrula, sonra periyodik özelliği yorumla.',
     'Katman periyot, son katman elektronu gruptur.')


# ---------- DOĞRULAMA ----------
ZORUNLU = ['id', 'k', 'baslik', 'olcer', 'kural', 'formul', 'sekil', 'ornek', 'hata', 'akilda']


def kelime(s):
    return len(s.replace('**', '').split())


ids = [c['id'] for c in K]
assert sorted(ids) == sorted(girdi_idler), (set(girdi_idler) ^ set(ids))
assert len(ids) == len(set(ids))
for c in K:
    for a in ZORUNLU:
        assert a in c, (c['id'], a)
    for a in ('id', 'k', 'baslik', 'olcer', 'kural', 'hata', 'akilda'):
        assert isinstance(c[a], str) and c[a].strip(), (c['id'], a)
    assert c['formul'] is None or c['formul'].strip()
    o = c['ornek']
    assert o['soru'] and o['cevap'] and 2 <= len(o['adimlar']) <= 4, c['id']
    assert kelime(c['baslik']) <= 6, (c['id'], 'baslik', kelime(c['baslik']))
    assert kelime(c['olcer']) <= 25 and not c['olcer'].startswith('Bu soru'), (c['id'], 'olcer', kelime(c['olcer']))
    assert kelime(c['kural']) <= 60, (c['id'], 'kural', kelime(c['kural']))
    assert 1 <= c['kural'].count('**') // 2 <= 2 and c['kural'].count('**') % 2 == 0, (c['id'], 'kalin')
    assert kelime(c['hata']) <= 40, (c['id'], 'hata', kelime(c['hata']))
    assert kelime(c['akilda']) <= 8 and '"' not in c['akilda'] and '“' not in c['akilda'], (c['id'], 'akilda', kelime(c['akilda']))
    if c['sekil']:
        assert len(c['sekil'].encode()) <= 25000
        open(f"{TMP}/{c['id']}.svg", 'w', encoding='utf-8').write(c['sekil'])

with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(K, f, ensure_ascii=False, indent=1)
print(len(K), 'kart,', sum(1 for c in K if c['sekil']), 'şekilli')
