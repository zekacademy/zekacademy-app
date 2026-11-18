# p03 Konu Tekrarı kartları -> kart-p03.json
import json, re, math
from fractions import Fraction

GIRDI = '/tmp/kor/kart/parti/p03.txt'
CIKTI = '/home/claude/zekacademy-app/havuz/tekrar/kart-p03.json'

def svg(h, etiket, govde, w=280):
    return (f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="{etiket}">{govde}</svg>')

INK = 'var(--ink)'; MUT = 'var(--muted)'; BR = 'var(--brand)'; BRS = 'var(--brand-soft)'
RU = 'var(--rule)'; WA = 'var(--warn)'; WAS = 'var(--warn-soft)'; ME = 'var(--memo)'

def T(x, y, s, fs=12, extra=''):
    return f'<text x="{x}" y="{y}" font-size="{fs}" {extra}>{s}</text>'

def ok(x1, y1, x2, y2, renk=INK, w=2):
    # çizgi + ok başı
    dx, dy = x2 - x1, y2 - y1
    L = math.hypot(dx, dy); ux, uy = dx / L, dy / L
    px, py = -uy, ux
    a = (x2 - 8 * ux + 4 * px, y2 - 8 * uy + 4 * py)
    b = (x2 - 8 * ux - 4 * px, y2 - 8 * uy - 4 * py)
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{renk}" stroke-width="{w}"/>'
            f'<polygon points="{x2},{y2} {a[0]:.1f},{a[1]:.1f} {b[0]:.1f},{b[1]:.1f}" fill="{renk}"/>')

# ---------- ŞEKİLLER ----------
S_hidrolik = svg(160, 'Hidrolik sistem: küçük ve büyük piston sıvıyla bağlı',
    f'<rect x="40" y="50" width="40" height="90" fill="none" stroke="{MUT}" stroke-width="2"/>'
    f'<rect x="140" y="50" width="100" height="90" fill="none" stroke="{MUT}" stroke-width="2"/>'
    f'<rect x="80" y="110" width="60" height="30" fill="none" stroke="{MUT}" stroke-width="2"/>'
    f'<rect x="42" y="76" width="36" height="62" fill="{BRS}"/><rect x="82" y="112" width="56" height="26" fill="{BRS}"/>'
    f'<rect x="142" y="76" width="96" height="62" fill="{BRS}"/>'
    f'<rect x="42" y="64" width="36" height="12" fill="{WAS}" stroke="{WA}" stroke-width="2"/>'
    f'<rect x="142" y="64" width="96" height="12" fill="{WAS}" stroke="{WA}" stroke-width="2"/>'
    + ok(60, 18, 60, 60, RU, 2.5) + T(68, 30, 'F₁', 14, 'font-weight="600"')
    + ok(190, 60, 190, 20, RU, 2.5) + T(198, 34, 'F₂', 14, 'font-weight="600"')
    + T(46, 102, 'A₁') + T(176, 102, 'A₂') + T(90, 130, 'sıvı', 12))

S_katman = svg(160, 'Üst üste iki karışmayan sıvı: X üstte, Y altta',
    f'<rect x="40" y="20" width="110" height="130" fill="none" stroke="{MUT}" stroke-width="2"/>'
    f'<rect x="42" y="40" width="106" height="50" fill="{WAS}"/><rect x="42" y="90" width="106" height="58" fill="{BRS}"/>'
    f'<line x1="42" y1="90" x2="148" y2="90" stroke="{MUT}" stroke-dasharray="4 3"/>'
    + T(70, 70, 'X: d₁', 13, 'font-weight="600"') + T(70, 125, 'Y: d₂', 13, 'font-weight="600"')
    + ok(170, 64, 170, 40, RU, 2) + ok(170, 66, 170, 88, RU, 2) + T(180, 70, 'h₁')
    + ok(220, 120, 220, 92, RU, 2) + ok(220, 122, 220, 148, RU, 2) + T(230, 126, 'h₂')
    + T(156, 154, 'taban', 12, f'fill="{MUT}"').replace('x="156"', 'x="158"'))

S_dalga = svg(130, 'Sinüs biçimli dalga; iki tepe arası dalga boyu, eksenden tepeye genlik',
    f'<line x1="15" y1="80" x2="270" y2="80" stroke="{MUT}" stroke-width="1.5"/>'
    f'<path d="M20,80 Q50,20 80,80 T140,80 T200,80 T260,80" fill="none" stroke="{RU}" stroke-width="2.5"/>'
    f'<line x1="50" y1="50" x2="50" y2="26" stroke="{MUT}" stroke-dasharray="3 3"/>'
    f'<line x1="170" y1="50" x2="170" y2="26" stroke="{MUT}" stroke-dasharray="3 3"/>'
    + ok(52, 30, 168, 30, BR, 2) + ok(168, 30, 52, 30, BR, 2) + T(104, 22, 'λ', 15, f'font-weight="600" fill="{BR}"')
    + f'<line x1="230" y1="80" x2="230" y2="110" stroke="{WA}" stroke-width="2.5"/>'
    + T(190, 124, 'genlik (A)', 12, f'fill="{WA}"'))

S_vt = svg(150, 'v–t grafiği: dik doğrunun ivmesi büyüktür',
    f'<line x1="40" y1="130" x2="260" y2="130" stroke="{MUT}" stroke-width="1.5"/>'
    f'<line x1="40" y1="130" x2="40" y2="14" stroke="{MUT}" stroke-width="1.5"/>'
    f'<line x1="40" y1="100" x2="150" y2="22" stroke="{RU}" stroke-width="2.5"/>'
    f'<line x1="40" y1="130" x2="240" y2="50" stroke="{BR}" stroke-width="2.5"/>'
    + T(156, 26, 'K', 14, f'font-weight="600" fill="{RU}"') + T(244, 54, 'L', 14, f'font-weight="600" fill="{BR}"')
    + T(8, 12, 'v') + T(250, 146, 't') + T(120, 146, 'eğim = ivme', 12, f'fill="{MUT}"'))

S_termo = svg(160, 'İki termometre ölçeği: X ölçeği ve Celsius, aynı oran',
    f'<line x1="90" y1="20" x2="90" y2="140" stroke="{INK}" stroke-width="2"/>'
    f'<line x1="190" y1="20" x2="190" y2="140" stroke="{INK}" stroke-width="2"/>'
    + ''.join(f'<line x1="{x-6}" y1="{y}" x2="{x+6}" y2="{y}" stroke="{INK}" stroke-width="2"/>' for x in (90, 190) for y in (20, 90, 140))
    + f'<line x1="90" y1="90" x2="190" y2="90" stroke="{RU}" stroke-dasharray="4 3" stroke-width="2"/>'
    + T(50, 24, 'X₁', 13) + T(58, 94, 'X', 13) + T(50, 144, 'X₀', 13)
    + T(200, 24, '100 °C', 13) + T(200, 94, 'C', 13) + T(200, 144, '0 °C', 13)
    + T(104, 62, 'oran aynı', 12, f'fill="{RU}"'))

S_mv = svg(150, 'Kütle–hacim grafiği: dik doğrunun özkütlesi büyüktür',
    f'<line x1="40" y1="130" x2="260" y2="130" stroke="{MUT}" stroke-width="1.5"/>'
    f'<line x1="40" y1="130" x2="40" y2="14" stroke="{MUT}" stroke-width="1.5"/>'
    f'<line x1="40" y1="130" x2="150" y2="22" stroke="{WA}" stroke-width="2.5"/>'
    f'<line x1="40" y1="130" x2="240" y2="70" stroke="{BR}" stroke-width="2.5"/>'
    + T(156, 28, 'X', 14, f'font-weight="600" fill="{WA}"') + T(244, 74, 'Y', 14, f'font-weight="600" fill="{BR}"')
    + T(8, 12, 'm') + T(250, 146, 'V') + T(120, 146, 'eğim = özkütle', 12, f'fill="{MUT}"'))

def _okb(pts):
    return f'<polygon points="{pts}" fill="{RU}"/>'
S_tel = svg(160, 'Sayfaya giren akımlı telin çevresinde saat yönünde manyetik alan halkası',
    f'<circle cx="140" cy="80" r="46" fill="none" stroke="{RU}" stroke-width="2.5"/>'
    + _okb('148,34 136,28 136,40') + _okb('186,88 180,76 192,76') + _okb('132,126 144,120 144,132') + _okb('94,72 88,84 100,84')
    + f'<circle cx="140" cy="80" r="12" fill="{card if False else "none"}" stroke="{INK}" stroke-width="2"/>'.replace('{card if False else "none"}', 'none')
    + f'<line x1="132" y1="72" x2="148" y2="88" stroke="{INK}" stroke-width="2"/><line x1="148" y1="72" x2="132" y2="88" stroke="{INK}" stroke-width="2"/>'
    + T(14, 24, 'Akım sayfaya girer (⊗)', 12) + T(14, 150, 'Alan: saat yönünde', 12, f'fill="{RU}"'))

S_kirilma = svg(160, 'Havadan ortama geçen ışın normale yaklaşır',
    f'<rect x="20" y="80" width="240" height="70" fill="{BRS}"/>'
    f'<line x1="20" y1="80" x2="260" y2="80" stroke="{MUT}" stroke-width="2"/>'
    f'<line x1="140" y1="14" x2="140" y2="150" stroke="{MUT}" stroke-dasharray="4 3"/>'
    + ok(60, 20, 138, 79, RU, 2.5) + ok(140, 80, 175, 140, RU, 2.5)
    + T(112, 54, 'θ₁', 13) + T(148, 118, 'θ₂', 13) + T(176, 36, 'hava (n = 1)', 12) + T(190, 124, 'ortam (n)', 12)
    + T(146, 24, 'normal', 11, f'fill="{MUT}"'))

S_ayna = svg(160, 'Çukur ayna: cisim F ile M arasında, görüntü M nin ötesinde gerçek ve ters',
    f'<line x1="10" y1="80" x2="270" y2="80" stroke="{MUT}" stroke-width="1.5"/>'
    f'<path d="M230,20 Q262,80 230,140" fill="none" stroke="{INK}" stroke-width="3"/>'
    f'<line x1="206" y1="74" x2="206" y2="86" stroke="{INK}" stroke-width="2"/><line x1="166" y1="74" x2="166" y2="86" stroke="{INK}" stroke-width="2"/>'
    + T(202, 100, 'F', 13) + T(161, 100, 'M', 13)
    + ok(186, 80, 186, 58, WA, 2.5) + T(176, 52, 'cisim', 12, f'fill="{WA}"')
    + ok(126, 80, 126, 122, RU, 2.5) + T(96, 138, 'görüntü', 12, f'fill="{RU}"')
    + f'<line x1="186" y1="60" x2="244" y2="60" stroke="{BR}" stroke-width="1.5"/>'
    + f'<line x1="244" y1="60" x2="126" y2="120" stroke="{BR}" stroke-width="1.5"/>')

# ---------- HESAP KONTROLLERİ ----------
assert (6 // 2) ** 2 == 9 and 15 * 9 == 135                       # hidrolik
assert 800 * 10 * 0.1 + 1200 * 10 * 0.2 == 3200                   # taban basıncı
assert Fraction(160, 4) - Fraction(160, 8) == 20                  # P–S
assert (24 / 2) / 4 == 3                                          # atma
assert 0.5 * 6 == 3                                               # dalga hızı
a_ = 2 * 10 / (3 + 2); assert a_ == 4 and 3 * a_ == 12 and 20 - 3 * a_ == 2 * a_   # ip gerilmesi
assert 12 / 12 == 1 and 12 / 8 == 1.5                             # kısa devre
V6 = 1 * 6; I3 = V6 / 3; Ia = 1 + I3; assert (V6, I3, Ia, V6 + Ia * 2) == (6, 2, 3, 12)
assert 75 - 30 == 45 and 180 / 45 == 4                            # özkütle SI
assert Fraction(15 - 5, 2) / Fraction(12, 4) == Fraction(5, 3)    # ivme
assert Fraction(20 + 10, 120) * 100 == 25                         # termometre
assert (100 * 80 + 300 * 20) / 400 == 35                          # ısıl denge
assert (3 * 20 + 2 * 30) / (20 + 30) == 2.4                       # karışım özkütlesi
assert abs(1 * 0.8 / 0.5 - 1.6) < 1e-9 and abs(3e8 / 1.6 - 1.875e8) < 1                # kırılma
assert 36 / 3 ** 2 == 4                                           # aydınlanma
di = 1 / (1 / 10 - 1 / 15); assert abs(di - 30) < 1e-9 and di > 20                 # çukur ayna
assert (160 + 90) / 50 == 5 and 1000 * 10 * (0.20 + 0.05) == 2500 # seviye
Fk = 6 - 4; Vv = Fk / (1000 * 10); assert abs(Vv - 2e-4) < 1e-12 and abs(0.6 / Vv - 3000) < 1e-6   # dinamometre
assert 1500 / 10 == 150 and 1500 / 2000 == 0.75                   # güç ve verim
assert 1.5 * 10 * (4 - 1) == 45                                   # enerji

def K(id, k, baslik, olcer, kural, formul, sekil, soru, adimlar, cevap, hata, akilda):
    return {"id": id, "k": k, "baslik": baslik, "olcer": olcer, "kural": kural, "formul": formul, "sekil": sekil,
            "ornek": {"soru": soru, "adimlar": adimlar, "cevap": cevap}, "hata": hata, "akilda": akilda}

F = 'fiz|'
kartlar = []
A = kartlar.append

A(K("fiz-basinc-01", "fiz|Basınç", "Pascal ilkesi ve hidrolik sistem",
 "Kapalı sıvıda basıncın aynen iletildiğini ve küçük kuvvetin alan oranıyla büyüdüğünü kullanabilmeni.",
 "Kapalı kaptaki sıvıya uygulanan basınç **her yöne aynen iletilir**. Bu yüzden iki pistonda da kuvvet bölü alan aynıdır. Dairesel pistonda alan yarıçapın karesiyle büyür: yarıçap 2 katına çıkarsa alan 4 katına, dengeleyen kuvvet de 4 katına çıkar.",
 "F₁ / A₁ = F₂ / A₂ ,  A = π · r²", S_hidrolik,
 "Küçük pistonun yarıçapı 2 cm, büyük pistonun yarıçapı 6 cm. Küçük pistona 15 N kuvvet uygulanırsa büyük piston kaç N’luk yükü dengeler?",
 ["Alan oranı, yarıçap oranının karesidir: (6 ÷ 2)² = 9", "Kuvvet de alan oranı kadar büyür: F₂ = 15 × 9 = 135 N"],
 "135 N",
 "Alan oranı yerine yarıçap oranını kullanmak (burada 3 almak). Kuvvet oranını yazmadan önce yarıçap oranının karesini al; alan hep yarıçapın karesiyle orantılıdır.",
 "Kuvvet oranı, alan oranıdır."))

A(K("fiz-basinc-03", "fiz|Basınç", "Sıvı basıncı ve katmanlar",
 "Karışmayan sıvılı kapta taban basıncını katman katman hesaplayıp toplayabildiğini.",
 "Sıvı basıncı **P = d · g · h** ile bulunur; h yüzeyden olan derinliktir. Kap şekli ve sıvı miktarı sonucu değiştirmez. Karışmayan sıvılarda her katmanın basıncı kendi özkütlesi ve kalınlığıyla ayrı hesaplanır, sonra **toplanır**.",
 "P = d₁·g·h₁ + d₂·g·h₂", S_katman,
 "Kapta üstte 10 cm yüksekliğinde özkütlesi 800 kg/m³ olan X, altta 20 cm yüksekliğinde özkütlesi 1200 kg/m³ olan Y sıvısı var (g = 10 m/s²). Taban basıncı kaç Pa’dır?",
 ["X katmanı: 800 · 10 · 0,1 = 800 Pa", "Y katmanı: 1200 · 10 · 0,2 = 2400 Pa", "Toplam: 800 + 2400 = 3200 Pa"],
 "3200 Pa",
 "Bütün sıvıyı tek özkütleyle hesaplamak ya da yalnız bir katmanı saymak. Taban, üstündeki bütün katmanların ağırlığını taşır; katman sayısı kadar terim yaz.",
 "Her katman için d·g·h, sonra topla."))

A(K("fiz-dalgalar-01", "fiz|Dalgalar", "Deprem dalgaları ve uzaklık",
 "Deprem dalgalarının varış sırasını ve P–S farkından merkeze uzaklığı yorumlayabildiğini.",
 "**P dalgası** boyunadır, en hızlıdır ve istasyona ilk gelir. **S dalgası** enine dalgadır ve ikinci gelir. Yüzey dalgaları en yavaştır, en son gelir ve en büyük genliği yapar. Süre = yol ÷ hız olduğundan P ile S arasındaki fark büyüdükçe merkez uzaklaşır.",
 "t = x / v  →  Δt = x / v_S − x / v_P", None,
 "P dalgasının hızı 8 km/s, S dalgasının hızı 4 km/s’dir. Bir istasyona S dalgası P’den 20 s sonra ulaşıyor. Deprem merkezi kaç km uzaktadır?",
 ["Uzaklığa x diyelim: P dalgası x ÷ 8, S dalgası x ÷ 4 sürede gelir", "Fark: x ÷ 4 − x ÷ 8 = x ÷ 8 = 20 s", "x = 20 × 8 = 160 km"],
 "160 km",
 "P’yi enine, S’yi boyuna sanmak ya da ilk gelen dalganın yavaş olduğunu düşünmek. Aynı yolu önce alan dalga daha hızlıdır; sıra P, S, yüzey dalgalarıdır.",
 "Önce P, sonra S, en son yüzey."))

A(K("fiz-dalgalar-03", "fiz|Dalgalar", "Yayda atmalar ve yansıma",
 "Atmaların karşılaşma anını, üst üste binmesini ve uçlardan yansımasını yorumlayabildiğini.",
 "Karşılaşan atmaların yer değiştirmeleri **toplanır**; eşit genlikli tepe ve çukur anlık düz görünür, sonra atmalar yollarına devam eder. Sabit uçtan yansıyan atma **ters döner**, serbest uçtan aynı yönlü döner. Aynı yaydaki atmaların hızı eşittir; zıt gelenler orta noktada buluşur.",
 "t = (L ÷ 2) ÷ v", None,
 "24 m uzunluğundaki yayın iki ucundan, hızları 4 m/s olan eşit boyutlu bir tepe ve bir çukur atma birbirine doğru gönderiliyor. Yay kaç s sonra düz görünür?",
 ["Atmalar zıt yönden eşit hızla geldiği için orta noktada buluşur: 24 ÷ 2 = 12 m", "Her biri 12 m yol alır: t = 12 ÷ 4 = 3 s"],
 "3 s",
 "Toplam uzunluğu tek atmanın hızına bölmek (24 ÷ 4). Atmalar birbirine doğru geldiği için her biri yolun yalnız yarısını alır.",
 "Zıt gelen atmalar ortada buluşur."))

A(K("fiz-dalgalar-05", "fiz|Dalgalar", "Dalga türleri ve dalga hızı",
 "Dalgaları türlerine göre ayırıp dalga boyu ve frekanstan hızı bulabildiğini.",
 "Titreşim yayılmaya dikse dalga **enine** (su, ışık, yay), paralelse **boyuna** (ses) olur. Ortam isteyen dalga mekaniktir (ses, su, yay); **ışık ve radyo dalgaları** ortamsız yayılır. Ardışık iki tepe arası bir dalga boyudur ve hız v = λ · f ile bulunur.",
 "v = λ · f ,  T = 1 / f", S_dalga,
 "Bir ipte ardışık iki tepe arası 0,5 m’dir ve dalga kaynağı saniyede 6 titreşim yapar. Dalganın hızı kaç m/s’dir?",
 ["Ardışık iki tepe arası bir dalga boyudur: λ = 0,5 m", "Saniyedeki titreşim frekanstır: f = 6 Hz", "v = λ · f = 0,5 × 6 = 3 m/s"],
 "3 m/s",
 "Işığı ya da suyu boyuna sanmak; tepe ile komşu çukur arasını dalga boyu almak (o λ ÷ 2’dir). Dalga boyu, aynı fazdaki iki nokta arasındaki uzaklıktır.",
 "Ses boyuna, ışık enine ve ortamsız."))

A(K("fiz-dinamik-02", "fiz|Dinamik", "İp gerilmesi ve ortak ivme",
 "İpe bağlı cisimlerde önce ortak ivmeyi, sonra ip gerilmesini bulabildiğini.",
 "İpe bağlı cisimler **aynı büyüklükte ivmeyle** hareket eder. Önce bütün sisteme ΣF = m_toplam · a yaz ve ortak ivmeyi bul. Sonra **tek bir cisme** ΣF = m · a uygula ve gerilmeyi çıkar. İvmeli harekette gerilme, asılı cismin ağırlığına eşit değildir.",
 "a = ΣF ÷ m_toplam  →  T (tek cisimden)", None,
 "Sürtünmesiz yatay masadaki 3 kg’lık cisim, makaradan geçen iple 2 kg’lık asılı cisme bağlı (g = 10 m/s²). İp gerilmesi kaç N’dur?",
 ["Sistemi hareket ettiren kuvvet asılı cismin ağırlığıdır: 2 · 10 = 20 N", "Ortak ivme: a = 20 ÷ (3 + 2) = 4 m/s²", "Masadaki cisme: T = 3 · 4 = 12 N (kontrol: 20 − 12 = 2 · 4)"],
 "12 N",
 "İp gerilmesini asılı cismin ağırlığına (20 N) eşit almak. Cisim ivmeyle indiği için T < m·g çıkmalı; sonucu asılı cisme uygulayıp kontrol et.",
 "Önce ortak ivme, sonra gerilme."))

A(K("fiz-dinamik-04", "fiz|Dinamik", "Newton yasaları ve eylemsizlik",
 "Araçtaki asılı cismin sapmasından ivme yönünü ve hızın artıp azaldığını yorumlayabildiğini.",
 "Net kuvvet sıfırsa cisim durgun kalır ya da **sabit hızla** gider; hareket değişimine direnmeye **eylemsizlik** denir. Araç hızlanırken asılı cisim geride kalır, yavaşlarken öne savrulur: cisim ivmenin **ters yönüne** sapar. Hız ve ivme aynı yönlüyse hız artar, zıt yönlüyse azalır.",
 "ΣF = m · a", None,
 "Doğuya doğru giden otobüste tavana asılı ip doğu yönüne (öne) sapmıştır. Otobüsün hızı artıyor mu, azalıyor mu?",
 ["İp ivmenin ters yönüne sapar; ip doğuya sapmışsa ivme batıya doğrudur", "Hız doğuya, ivme batıya: yönler zıt", "Zıt yönlü ivme hızı azaltır"],
 "Hızı azalıyor",
 "Sabit hızda da ipin eğik kalacağını sanmak. Sabit hızda ivme sıfırdır ve ip düşey durur; eğik ip her zaman ivme demektir.",
 "İp ivmenin ters yönüne sapar."))

A(K("fiz-elektrik-02", "fiz|Elektrik", "Anahtar, parlaklık ve kısa devre",
 "Anahtar kapanınca devre direncinin, akımın ve lamba parlaklığının nasıl değiştiğini yorumlayabildiğini.",
 "Parlaklık lambanın gücüne (P = I² · R) bağlıdır; **akımı değişmeyen lamba aynı parlaklıkta** kalır. Aynı potansiyeldeki iki nokta arasındaki iletkenden akım geçmez. Bir lambaya **paralel** kapalı anahtar o lambayı **kısa devre** yapar: lamba söner, eşdeğer direnç azalır, ana akım artar.",
 "Kısa devre → R_eş azalır → I artar", None,
 "12 V’luk ideal üretece 4 Ω’luk K, L, M lambaları seri bağlı. L’ye paralel anahtar kapatılırsa K’den geçen akım kaç A’dan kaç A’ya çıkar?",
 ["Önce: R = 12 Ω, I = 12 ÷ 12 = 1 A", "Anahtar kapanınca L kısa devre olur: R = 8 Ω", "Sonra: I = 12 ÷ 8 = 1,5 A (K ve M daha parlak, L söner)"],
 "1 A’dan 1,5 A’ya",
 "Anahtar kapanınca direncin hep azalacağını varsaymak. Önce anahtarın uçları arasında gerilim var mı bak; yoksa devre hiç değişmez.",
 "Uçları eş potansiyelse devre değişmez."))

A(K("fiz-elektrik-04", "fiz|Elektrik", "Akım, gerilim ve ölçü aletleri",
 "Ampermetre ve voltmetre okumalarından kol akımlarını, ana akımı ve üreteç gerilimini bulabildiğini.",
 "**Ampermetre** hangi koldaysa o kolun akımını verir ve seri bağlanır. **Voltmetre** elemana paralel bağlanır. Paralel kolların uçlarındaki gerilim aynıdır, ana akım **kol akımlarının toplamıdır**. Üreteç gerilimi, seri bölümlerdeki gerilimlerin toplamına eşittir.",
 "V = I · R ,  I_ana = I₁ + I₂", None,
 "Ana kolda R₁ = 2 Ω, ardından paralel R₂ = 6 Ω ve R₃ = 3 Ω kolları var. R₂ koluna bağlı ampermetre 1 A gösteriyor. Üreteç gerilimi kaç V’tur?",
 ["Paralel gerilim: V = 1 · 6 = 6 V", "R₃ akımı 6 ÷ 3 = 2 A; ana akım 1 + 2 = 3 A", "R₁ gerilimi 3 · 2 = 6 V; üreteç: 6 + 6 = 12 V"],
 "12 V",
 "Ampermetredeki akımı ana akım sanmak ya da R₁ üzerindeki gerilimi eklememek. Önce okumanın hangi koldan olduğuna bak, akımları topla, sonra bütün gerilimleri ekle.",
 "Okuma hangi koldaysa akım onundur."))

A(K("fiz-fizik-bilimine-01", "fiz|Fizik Bilimine Giriş", "Bilimsel yöntem ve değişkenler",
 "Bilimsel yöntem basamaklarını ve deneydeki değişkenleri ayırt edebildiğini.",
 "Sıra: **gözlem, hipotez, deney, sonuç**. Hipotez sınanabilir bir tahmindir. Araştırılan etken **bağımsız**, ölçülen sonuç **bağımlı**, sabit tutulanlar **kontrol değişkenidir**; deneyde yalnız bir etken değiştirilir. Alt dalı, olayda öne çıkan nicelik belirler: kuvvet mekanik, ısı termodinamik, ışık optik.",
 "Gözlem → Hipotez → Deney → Sonuç", None,
 "Bir öğrenci gübre miktarının fasulye boyuna etkisini inceliyor. Aynı toprak, su ve ışıkta farklı gübre miktarları deniyor. Hangisi bağımsız, bağımlı, kontrol değişkenidir?",
 ["Değiştirdiği etken gübre miktarıdır: bağımsız değişken", "Ölçtüğü sonuç fasulye boyudur: bağımlı değişken", "Sabit tuttukları toprak, su ve ışıktır: kontrol değişkenleri"],
 "Bağımsız: gübre; bağımlı: boy; kontrol: toprak, su, ışık",
 "Ölçülen sonucu bağımsız değişken sanmak. Kendine sor: ben neyi değiştiriyorum, neyi ölçüyorum? Alt dalı da olayın bildik adına göre değil, öne çıkan niceliğe göre seç.",
 "Değiştirdiğin bağımsız, ölçtüğün bağımlı."))

A(K("fiz-fizik-bilimine-03", "fiz|Fizik Bilimine Giriş", "SI birimleri ve dönüşüm",
 "Ölçülen değerleri SI birimine çevirip özkütle gibi bir niceliği doğru hesaplayabildiğini.",
 "Düzgün olmayan cismin hacmi, dereceli silindirde **son seviye − ilk seviye** ile bulunur. Sonra SI birimine çevir: **1 kg = 1000 g**, 1 mL = 1 cm³ = 10⁻⁶ m³, 1 saat = 3600 s. Özkütlenin SI birimi kg/m³’tür; 1 g/cm³ = 1000 kg/m³.",
 "d = m / V ,  1 g/cm³ = 1000 kg/m³", None,
 "Dereceli silindirde su seviyesi 30 mL’dir. 180 g’lık bir taş bırakılınca seviye 75 mL oluyor. Taşın özkütlesi kaç kg/m³’tür?",
 ["Hacim: 75 − 30 = 45 cm³", "d = 180 ÷ 45 = 4 g/cm³", "SI birimine çevir: 4 × 1000 = 4000 kg/m³"],
 "4000 kg/m³",
 "Son seviyeyi cismin hacmi sanmak ya da g ve cm³ değerlerini çevirmeden SI birimi gibi yazmak. Hacim hep seviye farkıdır; sonuçta birimi bir kez daha kontrol et.",
 "Hacim seviye farkıdır, birimi çevir."))

A(K("fiz-hareket-ve-02", "fiz|Hareket ve Kuvvet", "İvme ve hız–zaman grafiği",
 "İvmeyi hız değişiminden bulup v–t grafiğinin eğimiyle karşılaştırabildiğini.",
 "İvme, **birim zamandaki hız değişimidir**; son hıza değil, hız farkına bakılır. v–t grafiğinde doğrunun **eğimi** ivmeyi verir: doğru ne kadar dikse ivme o kadar büyüktür. Hız sabitse ivme sıfırdır. Hız ve ivme zıt yönlüyse cisim yavaşlar.",
 "a = Δv / Δt", S_vt,
 "K aracı 2 s’de hızını 5 m/s’den 15 m/s’ye, L aracı 4 s’de 0’dan 12 m/s’ye çıkarıyor. a_K ÷ a_L oranı kaçtır?",
 ["a_K = (15 − 5) ÷ 2 = 5 m/s²", "a_L = (12 − 0) ÷ 4 = 3 m/s²", "Oran: 5 ÷ 3"],
 "5/3 (K’nin ivmesi daha büyük)",
 "Son hızları ya da ortalama hızları karşılaştırmak. İvme hız değişimi ve süreden bulunur; oranı da sorulan sıraya göre kur (a_K ÷ a_L).",
 "İvme hız değişiminden bulunur."))

A(K("fiz-isi-sicaklik-01", "fiz|Isı, Sıcaklık ve Genleşme", "Sıcaklık ölçekleri ve termometre",
 "Sabit noktaları verilen termometre okumasını Celsius ölçeğine oranla çevirebildiğini.",
 "Eşit bölmeli termometrelerde, ilk sabit noktadan okunan uzaklığın toplam aralığa oranı **her ölçekte aynıdır**. Celsius’ta aralık 100 bölmedir. Kelvin için **K = °C + 273**, Fahrenheit için °F = 1,8 · °C + 32 yazılır. Sıcaklık farkı Celsius ve Kelvin’de aynıdır.",
 "(X − X₀) / (X₁ − X₀) = C / 100", S_termo,
 "X termometresi buzun erime noktasında −10, suyun kaynama noktasında 110 gösteriyor. X termometresi 20 gösterirken sıcaklık kaç °C’tur?",
 ["X aralığı: 110 − (−10) = 120 bölme", "X’in ilk noktadan uzaklığı: 20 − (−10) = 30 bölme", "30 ÷ 120 = C ÷ 100 → C = 25 °C"],
 "25 °C",
 "Yalnız başlangıcı çıkarıp bölme sayılarındaki farkı (120’ye karşı 100) hesaba katmamak ya da oranı ters kurmak. Sonuç mantıklı mı diye bak: 0 ile 100 arasında olmalı.",
 "Önce uzaklığı bul, sonra oranla."))

A(K("fiz-isi-sicaklik-03", "fiz|Isı, Sıcaklık ve Genleşme", "Enerji iletim yolları",
 "İletim, konveksiyon ve ışımanın hangisinde maddesel ortam gerektiğini ayırt edebildiğini.",
 "**İletim**: enerji taneciklerden taneciğe aktarılır (katılarda baskın). **Konveksiyon**: ısınan sıvı ya da gaz yer değiştirir. İkisi de **maddesel ortam ister**. **Işıma** ortam gerektirmez, boşlukta da yayılır; Güneş enerjisi Dünya’ya ışımayla gelir. Meltemde kara çabuk ısınır, çabuk soğur.",
 "İletim ve konveksiyon: madde şart · Işıma: madde gerekmez", None,
 "I. Metal kaşığın sıcak çorbada ısınması. II. Kalorifer ile odadaki havanın dolaşarak ısınması. III. Ateşin önünde otururken yüzün ısınması. Hangileri maddesel ortam gerektirir?",
 ["I: enerji kaşık boyunca taneciklerden aktarılır → iletim, madde gerekir", "II: ısınan hava yer değiştirir → konveksiyon, madde gerekir", "III: ışıma, ortam gerekmez"],
 "I ve II",
 "Sıvı ya da gaz akışıyla olan ısınmanın (konveksiyon) de ortam gerektirdiğini görememek. Önce her olayın yolunu adlandır, sonra ışıma dışındakilere madde şartını uygula.",
 "Işıma dışındaki yollar madde ister."))

A(K("fiz-isi-sicaklik-05", "fiz|Isı, Sıcaklık ve Genleşme", "Isıl denge ve öz ısı",
 "Isı alışverişinde verilen ve alınan ısıyı eşitleyip denge sıcaklığını bulabildiğini.",
 "Isıl dengede sıcak madde verdiği kadar ısıyı soğuk madde alır: **Q_verilen = Q_alınan**, Q = m · c · ΔT. Aynı maddede c sadeleşir. Denge sıcaklığı iki sıcaklığın arasındadır ve **kütlesi büyük olan maddenin sıcaklığına daha yakındır**. Aritmetik ortalama yalnız kütleler eşitse doğrudur.",
 "T = (m₁T₁ + m₂T₂) / (m₁ + m₂)", None,
 "100 g, 80 °C’lik su ile 300 g, 20 °C’lik su karıştırılıyor (ısı kaybı yok). Denge sıcaklığı kaç °C olur?",
 ["Sıcak su verir: 100 · (80 − T); soğuk su alır: 300 · (T − 20)", "Eşitle: 8000 − 100T = 300T − 6000", "400T = 14000 → T = 35 °C"],
 "35 °C",
 "İki sıcaklığın ortalamasını almak (50 °C). Kütleler farklıysa sonuç çok kütleli olana yakın çıkar; cevabın o yöne kaydığını kontrol et.",
 "Verilen ısı, alınan ısıya eşittir."))

A(K("fiz-madde-ve-02", "fiz|Madde ve Özellikleri", "Özkütle ve karışımlar",
 "Hacmi ölçüp özkütleyi bulabildiğini ve karışımın özkütlesini toplam kütle ile toplam hacimden hesaplayabildiğini.",
 "Özkütle **d = m ÷ V**’dir. Düzgün olmayan cismin hacmi dereceli silindirde **seviye farkıdır**. Kütle–hacim grafiğinde orijinden geçen doğrunun **eğimi özkütleyi** verir; dik doğru daha özkütlelidir. Karışımın özkütlesi **toplam kütle ÷ toplam hacim** ile bulunur, özkütlelerin ortalaması alınmaz.",
 "d_karışım = (m₁ + m₂) / (V₁ + V₂)", S_mv,
 "X sıvısından 20 cm³ (d = 3 g/cm³) ile Y sıvısından 30 cm³ (d = 2 g/cm³) karıştırılıyor. Hacim korunduğuna göre karışımın özkütlesi kaç g/cm³’tür?",
 ["m_X = 3 · 20 = 60 g, m_Y = 2 · 30 = 60 g", "Toplam kütle 120 g, toplam hacim 50 cm³", "d = 120 ÷ 50 = 2,4 g/cm³"],
 "2,4 g/cm³",
 "Özkütlelerin ortalamasını almak (2,5) ya da seviyeyi doğrudan hacim saymak. Karışımda her zaman önce kütleleri, sonra hacimleri topla.",
 "Karışımda kütleyi topla, hacmi topla."))

A(K("fiz-manyetizma-01", "fiz|Manyetizma", "Akımın manyetik alanı",
 "Akım taşıyan telin ve elektromıknatısın manyetik etkisini yön ve şiddet açısından yorumlayabildiğini.",
 "Akım taşıyan telin çevresinde **halka biçiminde** manyetik alan oluşur. **Sağ el kuralı**: başparmak akım yönünü gösterirse kıvrılan parmaklar alanın yönünü gösterir. Akım yönü değişince alan yönü de değişir. Elektromıknatıs **akım, sarım sayısı ve demir çekirdekle** güçlenir. Pusula iğnesi halkanın teğetini gösterir.",
 "Başparmak: akım · Dört parmak: manyetik alan", S_tel,
 "Akım sayfaya girerken (⊗) telin altındaki bir noktaya pusula konuyor. Pusulanın N ucu hangi yönü gösterir?",
 ["Sayfaya giren akımda alan, sayfaya bakınca saat yönünde döner", "Saat yönünde dönen halkanın alt noktasında alan sola doğrudur", "N ucu alanın yönünü gösterir"],
 "Sola",
 "Sağ el kuralını ters uygulamak. Kontrol: sayfadan çıkan akımda alan saat yönünün tersine, sayfaya giren akımda saat yönünde döner.",
 "Başparmak akım, parmaklar alan."))

A(K("fiz-optik-01", "fiz|Optik", "Işığın kırılması",
 "Kırılma yönünden ortamların kırılma indisini ve ışık hızını sıralayıp hesaplayabildiğini.",
 "Işık, kırılma indisi küçük ortamdan büyüğe geçerken **normale yaklaşır** ve yavaşlar; büyükten küçüğe geçerken normalden uzaklaşır ve hızlanır. Snell yasası: n₁ · sin θ₁ = n₂ · sin θ₂; açılar **normalden** ölçülür. Ortamdaki hız v = c ÷ n’dir, frekans değişmez.",
 "n₁ · sin θ₁ = n₂ · sin θ₂ ,  v = c / n", S_kirilma,
 "Havadan bir ortama gelen ışın normalle 53°, kırılan ışın 30° yapıyor (sin 53° = 0,8; sin 30° = 0,5). Ortamın kırılma indisi ve ışığın ortamdaki hızı nedir? (c = 3 · 10⁸ m/s)",
 ["Snell: 1 · 0,8 = n · 0,5 → n = 1,6", "v = c ÷ n = 3 · 10⁸ ÷ 1,6", "v = 1,875 · 10⁸ m/s"],
 "n = 1,6 ve v = 1,875 · 10⁸ m/s",
 "Sinüs değerini hız oranı sanmak ya da v = c · n yazmak. Hız, indisle ters orantılıdır: indis büyükse ışık daha yavaştır.",
 "Normale yaklaşan ışın yavaşlar."))

A(K("fiz-optik-03", "fiz|Optik", "Aydınlanma şiddeti",
 "Noktasal kaynağın aydınlanmasının uzaklıkla nasıl değiştiğini oran kurarak bulabildiğini.",
 "Noktasal kaynağın aydınlanma şiddeti **uzaklığın karesiyle ters orantılıdır**: E = I ÷ d². Uzaklık 2 katına çıkarsa aydınlanma **4’te 1’ine**, 3 katına çıkarsa 9’da 1’ine düşer. Yüzeye dik düşen akıda E = Φ ÷ A’dır. İki kaynağın aydınlanması eşitse uzaklıklar, ışık şiddetlerinin kareköküyle orantılıdır.",
 "E₂ / E₁ = (d₁ / d₂)²", None,
 "Bir lambanın 2 m uzağındaki ekranda aydınlanma 36 lx’tir. Ekran 6 m uzağa alınırsa aydınlanma kaç lx olur?",
 ["Uzaklık 6 ÷ 2 = 3 kat arttı", "Aydınlanma 3² = 9 kat azalır", "36 ÷ 9 = 4 lx"],
 "4 lx",
 "Oranı ters kurmak ya da kare almayı unutup 3’e bölmek (36 ÷ 3 = 12). Uzaklık arttıkça aydınlanma azalır ve bu azalma kareyle olur.",
 "Uzaklık kaç katsa, kareye böl."))

A(K("fiz-optik-05", "fiz|Optik", "Çukur ayna ve görüntü",
 "Cismin ayna önündeki konumundan görüntünün yerini ve özelliklerini belirleyebildiğini.",
 "Çukur aynada **M = 2F**’dir. Cisim **M’nin ötesindeyse** görüntü F–M arasında, gerçek, ters, küçüktür. Cisim **F ile M arasındaysa** görüntü M’nin ötesinde, gerçek, ters, büyüktür. Cisim **F’nin içindeyse** görüntü sanal, düz, büyüktür. Eksene paralel ışın yansıyınca F’den geçer.",
 "M = 2F · F dışı: gerçek, ters · F içi: sanal, düz", S_ayna,
 "Odak uzaklığı 10 cm olan çukur aynanın önünde, aynadan 15 cm uzağa bir cisim konuyor. Görüntünün yerini ve özelliklerini yaz.",
 ["M = 2F = 20 cm. Cisim 15 cm’de: F ile M arasında", "Bu konumda görüntü M’nin ötesinde oluşur", "Özellikleri: gerçek, ters, büyük"],
 "M’nin ötesinde; gerçek, ters, büyük",
 "M’nin ötesindeki cismin görüntüsünü büyük sanmak ya da görüntünün gerçek olduğunu atlamak. Önce cismi F ve M’ye göre yerleştir, sonra konuma göre sonucu oku.",
 "F dışındaki cismin görüntüsü gerçek, ters."))

A(K("fiz-sivilarin-kaldirma-01", "fiz|Sıvıların Kaldırma Kuvveti", "Sıvı seviyesi ve taban basıncı",
 "Yüzen ve batan cisimlerin yer değiştirdiği sıvı hacminden seviye artışını ve taban basıncını bulabildiğini.",
 "**Yüzen cisim kendi ağırlığı kadar** sıvıyı yer değiştirir (V = m ÷ d_sıvı). **Batan cisim kendi hacmi kadar** yer değiştirir. Toplam yer değiştiren hacim seviyeyi yükseltir: Δh = V ÷ kesit alanı. Taban basıncı, yeni yükseklikle P = h · d · g’den bulunur.",
 "Δh = V_yer değiştiren / A ,  P = h · d · g", None,
 "50 cm² kesitli kapta su 20 cm yüksekliğinde. Kaba 160 g’lık yüzen bir blok ve 90 cm³ hacimli batan bir taş bırakılıyor (d_su = 1000 kg/m³, g = 10 m/s²). Taban basıncı kaç Pa olur?",
 ["Yüzen blok 160 g su, yani 160 cm³ yer değiştirir; taş 90 cm³. Toplam 250 cm³", "Seviye artışı: 250 ÷ 50 = 5 cm → yeni yükseklik 25 cm", "P = 1000 · 10 · 0,25 = 2500 Pa"],
 "2500 Pa",
 "Yalnız batan cismin hacmini saymak ya da ilk seviyedeki basıncı yazmak. Yüzen cismin batan kısmını da say ve basıncı yeni seviyeden hesapla.",
 "Seviye artışı toplam hacimden bulunur."))

A(K("fiz-sivilarin-kaldirma-03", "fiz|Sıvıların Kaldırma Kuvveti", "Kaldırma kuvveti ve dinamometre",
 "Dinamometre ve taşan sıvı verilerinden kaldırma kuvvetini, hacmi ve özkütleyi bulabildiğini.",
 "Kaldırma kuvveti **cismin yerini tuttuğu sıvının ağırlığıdır**: F_k = d_sıvı · V_batan · g. Dinamometre havada ağırlığı, sıvıda **ağırlık − F_k** değerini gösterir. Seviye farkı batan hacmi verir. Kütleyi ağırlığa çevirirken **g ile çarpmayı** unutma.",
 "F_k = G_hava − G_sıvıda = d_sıvı · V · g", None,
 "Bir cisim dinamometrede havada 6 N, suda 4 N gösteriyor (d_su = 1000 kg/m³, g = 10 m/s²). Cismin hacmi ve özkütlesi nedir?",
 ["F_k = 6 − 4 = 2 N", "V = 2 ÷ (1000 · 10) = 2 · 10⁻⁴ m³ = 200 cm³", "m = 6 ÷ 10 = 0,6 kg; d = 0,6 ÷ (2 · 10⁻⁴) = 3000 kg/m³"],
 "V = 200 cm³, d = 3000 kg/m³",
 "Kütleyi g ile çarpmadan ağırlık yerine kullanmak ya da ilk su ağırlığını kaldırma kuvveti sanmak. Kuvvet hesabında kg değil, N kullan.",
 "Kayıp ağırlık, kaldırma kuvvetidir."))

A(K("fiz-is-guc-01", "fiz|İş, Güç ve Enerji", "Güç ve verim",
 "İş ve süreden gücü, harcanan ve yararlı enerjiden verimi hesaplayabildiğini.",
 "Güç, **birim zamandaki iştir**: P = W ÷ t (birim watt). İş–zaman grafiğinde doğrunun **eğimi** gücü verir. Çok iş yapmak yüksek güç demek değildir; süreye de bak. Verim, **yararlı enerjinin harcanan enerjiye oranıdır** ve %100’den küçüktür.",
 "P = W / t ,  Verim = Yararlı / Harcanan", None,
 "Bir motor 10 s boyunca 2000 J enerji harcayıp 1500 J yararlı iş yapıyor. Motorun yararlı gücü ve verimi nedir?",
 ["Yararlı güç: 1500 ÷ 10 = 150 W", "Verim: 1500 ÷ 2000 = 0,75", "Yüzde olarak %75"],
 "150 W ve %75",
 "Gücü yalnız yapılan işe göre karşılaştırmak. İşi büyük diye gücü büyük sanma; her makine için iş ÷ süre oranını ayrı hesapla.",
 "Güç, iş bölü süredir."))

A(K("fiz-is-guc-03", "fiz|İş, Güç ve Enerji", "Mekanik enerjinin korunumu",
 "Sürtünmesiz ortamda yükseklik farkından kinetik enerji kazancını hesaplayabildiğini.",
 "Sürtünmesiz ortamda **E_K + E_P = sabit** kalır. Alçalan cisim kaybettiği potansiyel enerji kadar kinetik enerji kazanır: **ΔE_K = m · g · Δh**. Bu bağıntıda ½ çarpanı yoktur. Sürtünme varsa kaybolan enerji ısıya dönüşür. Yay bırakılınca esneklik enerjisi kinetik enerjiye döner.",
 "ΔE_K = m · g · Δh", None,
 "Sürtünmesiz rayda 1,5 kg’lık cisim durgun hâlde 4 m yükseklikten bırakılıyor. 1 m yükseklikteki noktadan geçerken kinetik enerjisi kaç J’dir? (g = 10 m/s²)",
 ["Yükseklik kaybı: 4 − 1 = 3 m", "Kaybedilen potansiyel enerji: 1,5 · 10 · 3 = 45 J", "Başlangıçta kinetik enerji 0 olduğundan E_K = 45 J"],
 "45 J",
 "Yükseklik farkından gelen enerjiye ½ çarpanını eklemek ya da tek bir noktadaki potansiyel enerjiyi kinetik sanmak. Kazanç, yükseklik farkından bulunur.",
 "Kinetik kazanç, kaybedilen potansiyeldir."))

# ---------- DOĞRULAMA ----------
def kel(s): return len(s.replace('**', '').split())
ids = re.findall(r'^### (\S+) \|', open(GIRDI, encoding='utf-8').read(), re.M)
assert [c['id'] for c in kartlar] == ids and len(set(ids)) == len(ids), set(ids) ^ {c['id'] for c in kartlar}
for c in kartlar:
    i = c['id']
    for a in ('id', 'k', 'baslik', 'olcer', 'kural', 'hata', 'akilda'):
        assert c[a] and isinstance(c[a], str), (i, a)
    o = c['ornek']; assert o['soru'] and o['cevap'] and 2 <= len(o['adimlar']) <= 4, i
    assert c['formul'] is None or c['formul'].strip(), i
    assert kel(c['baslik']) <= 6 and kel(c['olcer']) <= 25 and kel(c['kural']) <= 60 and kel(c['hata']) <= 40 and kel(c['akilda']) <= 8, (i, kel(c['baslik']), kel(c['olcer']), kel(c['kural']), kel(c['hata']), kel(c['akilda']))
    assert not c['olcer'].startswith('Bu soru') and '"' not in c['akilda'] and '“' not in c['akilda']
    assert 'formul' in c and 'sekil' in c and c['k'].startswith('fiz|')
    if c['sekil']:
        assert len(c['sekil'].encode()) <= 25000
        for fs in re.findall(r'font-size="(\d+)"', c['sekil']): assert int(fs) >= 11, i
json.dump(kartlar, open(CIKTI, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
import os
os.makedirs('/tmp/kor/kart/p03', exist_ok=True)
for c in kartlar:
    if c['sekil']:
        s = c['sekil'].replace('<svg ', '<svg xmlns="http://www.w3.org/2000/svg" ', 1)
        for v, h in {'--ink': '#18212f', '--muted': '#5b6678', '--brand-soft': '#e7edff', '--brand': '#2f5bea', '--rule': '#0f8a6a', '--warn-soft': '#fff1e8', '--warn': '#c2410c', '--memo': '#7c3aed'}.items():
            s = s.replace(f'var({v})', h)
        s = s.replace('<text ', '<text fill="#18212f" ').replace('fill="#18212f" x', 'x') if False else s
        open(f'/tmp/kor/kart/p03/{c["id"]}.svg', 'w', encoding='utf-8').write(s.replace('<svg ', '<svg style="background:#fff" ', 1))
print(len(kartlar), 'kart', sum(1 for c in kartlar if c['sekil']), 'şekilli')
