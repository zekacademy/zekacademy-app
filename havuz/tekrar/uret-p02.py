import json, re, itertools
from fractions import Fraction

IN = '/tmp/kor/kart/parti/p02.txt'
OUT = '/home/claude/zekacademy-app/havuz/tekrar/kart-p02.json'
S = 'stroke="#334155" fill="none" stroke-width="2"'
T = 'font-family="sans-serif" font-size="12" fill="#334155"'

def svg(w, h, body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">{body}</svg>'

def txt(x, y, s, anchor='middle', extra=''):
    base = T.replace(' fill="#334155"', '') if 'fill=' in extra else T
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" {base} {extra}>{s}</text>'

# --- şekiller ---
sek_metab = svg(320, 180,
    f'<path d="M40 20 V140 H300" {S}/>'
    f'<path d="M40 130 C100 125 130 50 170 40 C200 36 215 60 235 135" stroke="#2563eb" fill="none" stroke-width="3"/>'
    f'<path d="M170 40 V140" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4 3" fill="none"/>'
    + txt(170, 158, 'optimum') + txt(170, 175, 'sıcaklık') + txt(52, 16, 'hız', 'start')
    + txt(95, 85, 'artar', 'middle') + txt(262, 70, 'enzim', 'middle') + txt(262, 86, 'bozulur', 'middle'))

def box(x, y, w, h, s):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" {S}/>' + txt(x+w/2, y+h/2+4, s)
sek_dikotom = svg(340, 190,
    box(100, 8, 140, 34, '1. Hücre duvarı var mı?')
    + f'<path d="M140 42 L70 78 M200 42 L270 78" {S}/>'
    + txt(88, 62, 'yok', 'end') + txt(252, 62, 'var', 'start')
    + box(15, 78, 110, 34, 'Hayvanlar')
    + box(215, 78, 110, 34, '2. Duvar neden?')
    + f'<path d="M245 112 L205 148 M295 112 L300 148" {S}/>'
    + box(150, 148, 70, 34, 'Mantar') + box(262, 148, 70, 34, 'Bitki')
    + txt(215, 134, 'kitin', 'end') + txt(300, 134, 'selüloz', 'start'))

def sym(x, y, kind, hasta):
    f = '#334155' if hasta else '#ffffff'
    if kind == 'k':
        return f'<rect x="{x-14}" y="{y-14}" width="28" height="28" stroke="#334155" stroke-width="2" fill="{f}"/>'
    return f'<circle cx="{x}" cy="{y}" r="14" stroke="#334155" stroke-width="2" fill="{f}"/>'
sek_soy = svg(300, 190,
    sym(100, 30, 'k', False) + sym(200, 30, 'd', False)
    + f'<path d="M114 30 H186 M150 30 V90 M70 90 H230 M70 90 V100 M150 90 V100 M230 90 V100" {S}/>'
    + sym(70, 115, 'k', False) + sym(150, 115, 'd', False) + sym(230, 115, 'k', True)
    + txt(150, 165, 'Dolu simge: özelliği gösterir.') + txt(150, 183, 'Ebeveynde yok, çocukta var.'))

sek_oz = svg(340, 190,
    f'<path d="M45 20 V150 H320" {S}/>'
    f'<path d="M45 140 C70 60 90 50 320 48" stroke="#dc2626" fill="none" stroke-width="3"/>'
    f'<path d="M45 140 C100 138 130 130 160 70 C180 35 200 40 220 80 C240 125 270 142 320 144" stroke="#16a34a" fill="none" stroke-width="3"/>'
    f'<path d="M45 60 C150 58 200 58 235 75 C270 95 290 125 320 132" stroke="#2563eb" fill="none" stroke-width="3"/>'
    + txt(180, 172, 'zaman (yıl)') + txt(55, 14, 'miktar', 'start')
    + txt(180, 40, 'fosfat', 'middle', 'fill="#dc2626"')
    + txt(122, 128, 'alg', 'middle', 'fill="#16a34a"')
    + txt(100, 54, 'oksijen', 'middle', 'fill="#2563eb"'))

sek_zar = svg(320, 180,
    f'<rect x="20" y="30" width="280" height="130" rx="10" {S}/>'
    f'<ellipse cx="160" cy="104" rx="70" ry="34" stroke="#2563eb" fill="none" stroke-width="3"/>'
    + txt(160, 108, 'kese %25') + txt(160, 22, 'beher %10') + txt(160, 155, 'su içeri girer', 'middle', 'fill="#2563eb"')
    + f'<path d="M60 70 L105 88 M260 70 L215 88" stroke="#2563eb" stroke-width="3" fill="none"/>')

sek_punnett = svg(320, 190,
    txt(125, 24, 'A') + txt(205, 24, 'a')
    + txt(48, 70, 'A') + txt(48, 130, 'a')
    + f'<rect x="85" y="36" width="80" height="60" {S}/><rect x="165" y="36" width="80" height="60" {S}/>'
    + f'<rect x="85" y="96" width="80" height="60" {S}/><rect x="165" y="96" width="80" height="60" {S}/>'
    + txt(125, 72, 'AA') + txt(205, 72, 'Aa') + txt(125, 132, 'Aa') + txt(205, 132, 'aa')
    + txt(160, 180, 'Üstte bir, solda öteki ebeveynin gametleri'))

# --- hesaplar ---
# metabolizma
assert 12 / 4 == 3
# peptit
aa, z = 150, 3
bag = aa - z; assert bag == 147
kalan = bag - 10; assert kalan == 137
# bakteri
assert 60 // 20 == 3 and 2**3 == 8
# popülasyon
son = 300 + 60 - 40 + 20 - 10; assert son == 330
yog = Fraction(son, 5); assert yog == 66
# mayoz
n2 = 10
# bölünme
tam = 28 // 6; assert tam == 4 and 2**tam == 16
# ABO + Rh
def alel_gamet(g): return list(g)
def olasilik():
    anne = ['A', 'O']; baba = ['B', 'O']
    pO = Fraction(sum(1 for a, b in itertools.product(anne, baba) if a == 'O' and b == 'O'), 4)
    anneR = ['R', 'r']; babaR = ['r', 'r']
    pr = Fraction(sum(1 for a, b in itertools.product(anneR, babaR) if a == 'r' and b == 'r'), 4)
    return pO, pr, pO * pr
pO, pr, pt = olasilik(); assert (pO, pr, pt) == (Fraction(1, 4), Fraction(1, 2), Fraction(1, 8))
# AB x OO
assert {tuple(sorted(x)) for x in itertools.product('AB', 'OO')} == {('A', 'O'), ('B', 'O')}
# gamet çeşidi
assert 2 ** 3 == 8
# soy ağacı
assert Fraction(1, 2) * Fraction(1, 2) == Fraction(1, 4)
# dihibrit
def p_yuv_yesil():
    c = 0
    for a, b in itertools.product(itertools.product('Rr', 'Ss'), itertools.product('Rr', 'Ss')):
        pass
    r = [x + y for x, y in itertools.product('Rr', 'Rr')]
    s = [x + y for x, y in itertools.product('Ss', 'Ss')]
    pr_ = Fraction(sum(1 for g in r if 'R' in g), 4)
    ps_ = Fraction(sum(1 for g in s if g == 'ss'), 4)
    return pr_, ps_, pr_ * ps_
assert p_yuv_yesil() == (Fraction(3, 4), Fraction(1, 4), Fraction(3, 16))

def K(id, k, baslik, olcer, kural, formul, sekil, soru, adimlar, cevap, hata, akilda):
    return {"id": id, "k": k, "baslik": baslik, "olcer": olcer, "kural": kural, "formul": formul,
            "sekil": sekil, "ornek": {"soru": soru, "adimlar": adimlar, "cevap": cevap},
            "hata": hata, "akilda": akilda}

C = []
C.append(K('bio-canlilarin-ortak-02', 'bio', 'Metabolizma ve sıcaklık grafiği',
 'Metabolizma hızının sıcaklıkla nasıl değiştiğini grafikten okuyup anabolik ile katabolik tepkimeyi ayırabilmeni.',
 '**Anabolizma** küçük moleküllerden büyük molekül yapar ve enerji harcar. **Katabolizma** büyük molekülü yıkar ve enerji açığa çıkarır. Metabolizma enzimlerle yürür: hız optimum sıcaklığa kadar artar, daha yüksek sıcaklıkta enzimler bozulduğu için düşer.',
 'Anabolizma: yapım, enerji harcar · Katabolizma: yıkım, enerji verir', sek_metab,
 'Bir hücrede metabolizma hızı 15 °C\'ta 4, 35 °C\'ta 12, 65 °C\'ta 1 birim ölçülüyor. Hız 15 °C\'tan 35 °C\'a kaç kat artmıştır ve 65 °C\'taki düşüşün nedeni nedir?',
 ['Artışı oranla: 12 ÷ 4 = 3 kat.', '35 °C optimuma yakındır, hız yükselmiştir.', '65 °C çok yüksektir; enzimlerin yapısı bozulmuştur, hız düşer.'],
 '3 kat artmıştır; düşüşün nedeni yüksek sıcaklıkta enzimlerin bozulmasıdır.',
 'Sıcaklık arttıkça hızın sürekli arttığını sanmak. Grafikte tepe noktasından sonra eğri düşer; her aralığı ayrı ayrı oku.',
 'Önce yükselir, optimumdan sonra düşer'))
C.append(K('bio-canlilarin-ortak-04', 'bio', 'Canlı–cansız ayrımı ve çoğalma',
 'Tablodaki özelliklerden canlı ile cansızı ayırıp bakteri çoğalmasını hesaplayabilmeni.',
 'Canlılar hücresel yapıdadır; beslenir, solunum yapar, boşaltım yapar, uyarılara tepki verir, büyür ve ürer. **Cansızlar bu özelliklerin hiçbirini** göstermez. Virüsler hücresel yapıda değildir. Bakteriler ikiye bölünerek çoğalır: n bölünmede **2 üzeri n** bakteri olur.',
 'n bölünme sonunda bakteri sayısı = 2ⁿ', None,
 'Her 20 dakikada bir ikiye bölünen tek bakteri 1 saat sonra kaç bakteri olur?',
 ['1 saat = 60 dakika.', 'Bölünme sayısı: 60 ÷ 20 = 3.', 'Bakteri sayısı: 2 üzeri 3 = 8.'],
 '8 bakteri.',
 'Bölünme sayısını bakteri sayısı sanmak (3 demek). Önce bölünme sayısını bul, sonra 2\'nin o kuvvetini al; sütunu özellik özellik oku.',
 'Hepsi varsa canlı, hiçbiri yoksa cansız'))
C.append(K('bio-canlilarin-siniflandirilmasi-02', 'bio', 'Dikotom anahtar ve dallanma',
 'Dikotom anahtarı basamak basamak izleyip canlının hangi gruba gittiğini bulabilmeni.',
 'Dikotom anahtarda her basamakta **iki seçenek** vardır. Canlının özelliğine uyan seçeneği seçer, gösterilen basamağa gidersin. Bir grup adına ulaşınca durursun. Dallanma şemasında dalların ayrıldığı nokta **ortak atayı** gösterir; ortak atası yakın olanlar daha akrabadır.',
 None, sek_dikotom,
 'Yukarıdaki anahtarda hücre duvarı selülozdan oluşan, ototrof bir canlı hangi gruba girer?',
 ['1. basamak: hücre duvarı var, bu yüzden 2. basamağa geç.', '2. basamak: duvar selülozdan, yani sağ seçenek.', 'Sağ seçenek Bitki grubunu gösterir.'],
 'Bitkiler.',
 'Bir özelliği görmeyip yanlış yöne gitmek (ör. çok hücreli ya da duvar bilgisini atlamak). Her basamakta yalnız o basamağın sorusuna bak.',
 'Her basamakta uyan seçeneği izle'))
C.append(K('bio-canlilarin-siniflandirilmasi-04', 'bio', 'Bitki ve hayvan grupları',
 'Bitki ve omurgasız hayvan gruplarını ortak ve farklı özelliklerine göre ayırabilmeni.',
 'Bitkiler **damarsız** ve **damarlı** diye ayrılır. Damarlılar tohumsuz ve tohumlu olur; tohumlular açık ya da kapalı tohumludur. Tohumsuz bitkiler **sporla** ürer. Omurgasız gruplarda her özellik her grupta bulunmaz; ifadeyi tablodaki sütunla karşılaştır.',
 'Bitkiler → damarlı → tohumlu → kapalı tohumlu', None,
 'Kozalaklı ağaç, eğrelti otu ve kara yosunundan hangisi damarlı ama tohumsuzdur?',
 ['Kara yosunu damarsızdır, elenir.', 'Kozalaklı ağaç damarlı ve tohumludur (açık tohumlu), elenir.', 'Eğrelti otu damarlıdır ve sporla ürer, tohumsuzdur.'],
 'Eğrelti otu.',
 '"Hepsi" ya da "tek" gibi kapsamlı sözleri tüm satırlarda sınamamak. Bir satır uymuyorsa ifade yanlıştır; her gruba tek tek bak.',
 'Tohumsuz bitki sporla ürer'))
C.append(K('bio-canlilarin-temel-01', 'bio', 'Enzimlerin özellikleri ve grafikleri',
 'Enzimin ne yaptığını, ürün–zaman grafiğinde enzim miktarının ve sıcaklığın etkisini yorumlayabilmeni.',
 'Enzim tepkimeyi hızlandıran **biyolojik katalizördür**; genellikle proteindir. Aktivasyon enerjisini düşürür, tepkime sonunda **harcanmaz**, her enzim belirli bir substrata etki eder (özgüldür). Aşırı sıcakta yapısı bozulur. Kontrollü deneyde yalnız bir etken değiştirilir.',
 'Enzim: hızlandırır · harcanmaz · özgüldür', None,
 'Aynı miktar substratla iki tüp kuruluyor: 1. tüpte 1 birim, 2. tüpte 2 birim enzim var. Ürün–zaman grafiğinde fark ne olur?',
 ['Enzim fazlaysa tepkime daha hızlı ilerler: 2. tüpün eğrisi daha dik yükselir.', 'Substrat miktarı aynıdır; en sonda oluşan toplam ürün de aynı olur.', 'Enzim harcanmadığı için ikisinde de plato aynı yükseklikte biter.'],
 '2. tüp daha hızlı yükselir, ikisi de aynı en yüksek ürün miktarına ulaşır.',
 'Enzimin tepkimede harcandığını sanmak. Enzim yalnız süreyi kısaltır, ürün miktarını artırmaz; grafikte plato yüksekliğine bak.',
 'Enzim hızlandırır, harcanmaz, özgüdür'))
C.append(K('bio-canlilarin-temel-03', 'bio', 'Peptit bağı ve su sayısı',
 'Amino asit ve zincir sayısından peptit bağı ile su sayısını bulabilmeni.',
 'Amino asitler **peptit bağıyla** bağlanır. Her bağ kurulurken 1 su molekülü çıkar (dehidrasyon). Hidrolizde ise bağ kopması için su **kullanılır**. Tek zincirli proteinde bağ sayısı amino asit sayısından 1 eksiktir; zincir sayısı artarsa o kadar eksik olur.',
 'Bağ = su = amino asit sayısı − zincir sayısı', None,
 '3 zincirli, 150 amino asitli bir proteinde kaç peptit bağı vardır? Bağların 10 tanesi hidrolizle koparılırsa kaç bağ kalır?',
 ['Bağ sayısı: 150 − 3 = 147.', 'Sentezde 147 su açığa çıkmıştır.', 'Hidrolizle 10 bağ koparsa kalan: 147 − 10 = 137.'],
 '147 bağ; 10 tanesi kopunca 137 bağ kalır.',
 'Zincir sayısını 1 sanıp amino asit sayısından yalnız 1 çıkarmak ya da amino asit sayısını bölmek. Zincir sayısını soru metninde ara.',
 'Su = bağ = amino asit − zincir'))
C.append(K('bio-canlilarin-temel-05', 'bio', 'Yapıtaşları, su ve mineraller',
 'Organik bileşiklerin yapıtaşlarını eşleştirip su, mineral ve vitaminlerin görevlerini ayırt edebilmeni.',
 '**Amino asit** proteinin, **nükleotit** nükleik asidin, **monosakkarit** polisakkaritin yapıtaşıdır; yağ gliserol ve yağ asitlerinden oluşur. Su çözücüdür, madde taşır, hidrolize girer, ısı kapasitesi yüksektir ama enerji vermez. Mineraller de enerji vermez.',
 'Protein ← amino asit · Nükleik asit ← nükleotit', None,
 'Glikoz, amino asit, nükleotit ve gliserol ile yağ asidi hangi bileşiklerin yapıtaşıdır?',
 ['Glikoz bir monosakkarittir: nişasta gibi polisakkaritleri kurar.', 'Amino asitler protein, nükleotitler DNA ve RNA oluşturur.', 'Gliserol ile yağ asitleri birleşip yağı oluşturur.'],
 'Glikoz: polisakkarit, amino asit: protein, nükleotit: nükleik asit, gliserol ve yağ asidi: yağ.',
 'Karbonhidrat yapıtaşını protein ya da nükleotitle karıştırmak. Bileşiğin adından ters çalış: protein dendiyse amino asit.',
 'Protein amino asit, DNA nükleotit'))
C.append(K('bio-ekosistem-02', 'bio', 'Çevre sorunları ve doğal kaynaklar',
 'Besin tuzu artışının alg ve oksijen düzeyine etkisini zaman sırasıyla yorumlayabilmeni.',
 'Azot ve fosfor gibi **besin tuzları** artınca algler çoğalır. Algler ölünce ayrıştırıcılar onları parçalarken suyun **oksijenini** kullanır, oksijen düşer. Yenilenebilir kaynaklar kullanılma hızından hızlı ya da sürekli yenilenir; yenilenemeyenler tükenir.',
 'Besin tuzu ↑ → alg ↑ → alg ölümü → oksijen ↓', sek_oz,
 'Bir göle 2. yılda fazla fosfat karışıyor. Alg 4. yılda en yüksek değere çıkıyor, çözünmüş oksijen 7. yıldan sonra düşüyor. Olayları sırala.',
 ['Önce fosfat artar (2. yıl).', 'Sonra alg miktarı yükselir (4. yıl zirve).', 'Algler ölür, ayrıştırıcılar çoğalıp oksijeni kullanır; oksijen 7. yıldan sonra düşer.'],
 'Fosfat artışı, alg artışı, alg ölümü ve oksijenin düşmesi.',
 'Alg azalırken fosfatın azaldığını sanmak. Eğrilerin değişime başladığı zamanları yan yana yaz; olay sırası zaman sırasıdır.',
 'Eğriler hangi sırayla döndü, olay o sıra'))
C.append(K('bio-ekosistem-04', 'bio', 'Popülasyon ve ekolojik ilişkiler',
 'Doğum, ölüm ve göçten popülasyon büyüklüğünü ve yoğunluğunu bulup ilişki türlerini ayırabilmeni.',
 '**Mutualizm**: iki taraf da yararlanır (liken). **Parazitizm**: biri yararlanır, konak zarar görür (kene). **Kommensalizm**: biri yararlanır, diğeri etkilenmez. Popülasyon büyüklüğü doğum ve göçle girenle artar, ölüm ve göçle çıkanla azalır.',
 'Yoğunluk = birey sayısı ÷ alan', None,
 'Yıl başında 300 birey, 5 km² alanda yaşıyor. Yıl içinde 60 doğum, 40 ölüm, 20 göçle giriş, 10 göçle çıkış oluyor. Yıl sonu yoğunluğu kaçtır?',
 ['Büyüklük: 300 + 60 − 40 + 20 − 10 = 330.', 'Alan 5 km² olduğundan yoğunluk = 330 ÷ 5.', 'Sonuç 66.'],
 '66 birey/km².',
 'Yıl başı sayıya değişimi eklemeyi unutmak ya da göçü yanlış yöne yazmak. Girenleri topla, çıkanları çıkar; ilişkide önce kim yararlanıyor diye sor.',
 'Kim yararlanıyor, kim zarar görüyor?'))
C.append(K('bio-hucre-ve-01', 'bio', 'Hücre teorisi ve bilim insanları',
 'Hücreyi adlandıran bilim insanı ile hücre teorisine katkı yapanları ayırabilmeni.',
 '**Hooke** mantar kesitinde odacıkları görüp onlara hücre adını verdi. Leeuwenhoek mikroskopla tek hücreli canlıları gözledi. Schleiden bitkilerin, Schwann hayvanların hücrelerden oluştuğunu söyledi. Virchow hücrenin hücreden oluştuğunu belirtti. Teori bu **katkıların birleşmesiyle** doğdu.',
 None, None,
 'Bir öğrenci "bitkilerin hücrelerden oluştuğunu söyleyen bilim insanı hücreyi de adlandırmıştır" diyor. Doğru mu?',
 ['Hücre adını mantar kesitinde odacıkları gören Hooke verdi.', 'Bitkilerin hücreli yapısını söyleyen Schleiden\'dir.', 'İkisi ayrı olaylardır; öğrenci birbirine karıştırmıştır.'],
 'Yanlış; adı Hooke verdi.',
 'Bitki ya da hayvan dokusunun hücreli olduğunu söyleyeni, hücreyi adlandıran sanmak. "Gördü ve adını koydu" ile "dokunun hücreli olduğunu söyledi" farklı işlerdir.',
 'Hücre adı Hooke, bitki Schleiden'))
C.append(K('bio-hucre-ve-03', 'bio', 'Organeller ve görevleri',
 'Organellerin görevlerini eşleştirip salgı proteininin hücre içindeki yolunu sıralayabilmeni.',
 'Hücre dışına salgılanan protein **ribozomlu** yapıda üretilir, ER ve **Golgi** içinden geçip keseciklerle zara taşınır. Plastitler çift zarlıdır: kloroplast klorofil, kromoplast renkli pigment taşır; lökoplast renksizdir ve besin depolar.',
 'Ribozom → granüllü ER → Golgi → kesecik → zar', None,
 'Bir hücrede salgılanan sindirim enzimi için Golgi cisimciğinden hemen önce hangi yapıdan geçer, hemen sonra hangisine geçer?',
 ['Protein ribozomda yapılır, granüllü ER\'ye girer.', 'Granüllü ER\'den Golgi\'ye geçer: Golgi\'den önceki yapı granüllü ER\'dir.', 'Golgi\'den kesecikler kopar; sonraki yapı kesecik, sonra zardır.'],
 'Önce granüllü ER, sonra kesecik.',
 'Sırayı tersine ya da Golgi ile keseciği yer değiştirerek yazmak. Radyoaktivite zirvesi erken olan yapı yolun başındadır; kesecik Golgi\'den koptuğu için ondan sonra gelir.',
 'Tepe erkense yol başındadır'))
C.append(K('bio-hucre-ve-05', 'bio', 'Zardan madde geçişi ve ozmoz',
 'Ozmoz yönünü, deney değişkenlerini ve yüzey/hacim oranını yorumlayabilmeni.',
 'Su, yarı geçirgen zardan çözünen derişiminin **düşük** olduğu yerden **yüksek** olduğu yere geçer. Çözünen madde geçemiyorsa yalnız su hareket eder. Küpte yüzey alanı kenarın karesiyle, hacim küpüyle orantılıdır; hücre büyüdükçe **yüzey/hacim oranı küçülür**.',
 'Su: seyrek ortamdan → derişik ortama', sek_zar,
 'İçinde %25 şeker çözeltisi olan selofan kese %10 şekerli çözeltiye batırılıyor; şeker selofandan geçemiyor. Kese kütlesi nasıl değişir? Kenarı 2 cm ve 4 cm olan küplerin yüzey/hacim oranını da bul.',
 ['Kese daha derişik: su beherden içeri girer, kütle artar.', 'Küpte oran: 6a² ÷ a³ = 6 ÷ a.', 'a = 2 cm için 3; a = 4 cm için 1,5.'],
 'Kese kütlesi artar; oran 3 ve 1,5 olur, büyük küpte oran küçüktür.',
 'Suyun çözünen yönüne gitmesini ters sanmak ya da kesede derişimi bağımsız değişken saymamak. Önce "neyi değiştirdim, neyi ölçtüm?" sorusunu sor.',
 'Su derişik tarafa akar'))
C.append(K('bio-hucrede-bolunme-02', 'bio', 'Mayoz ve kalıtsal çeşitlilik',
 'Mayozun evrelerindeki kromozom ve kromatit sayısını ve çeşitlilik kaynaklarını belirleyebilmeni.',
 '**Mayoz I**\'de homolog kromozomlar ayrılır; kromozom sayısı yarıya iner (n), kromozomlar çift kromatitli kalır. **Mayoz II**\'de kardeş kromatitler ayrılır. Krossing-over, homologların kardeş olmayan kromatitleri arasında parça değişimidir ve çeşitlilik sağlar.',
 'Mayoz I: homolog ayrılır · Mayoz II: kromatit ayrılır', None,
 'Kromozom sayısı 2n = 10 olan bir hücre mayoza girer. Mayoz I sonunda bir hücrede kaç kromozom ve kaç kromatit vardır? Mayoz II sonunda?',
 ['Mayoz I\'de sayı yarıya iner: 10 ÷ 2 = 5 kromozom.', 'Kromozomlar hâlâ çift kromatitlidir: 5 × 2 = 10 kromatit.', 'Mayoz II\'de kromatitler ayrılır: 5 kromozom ve 5 kromatit.'],
 'Mayoz I sonu: 5 kromozom, 10 kromatit; mayoz II sonu: 5 kromozom, 5 kromatit.',
 'Kardeş kromatitlerin mayoz I\'de ayrıldığını sanmak. Mayoz I\'de ayrılan homologlardır; kromatit sayısını hücredeki toplamla da karıştırma.',
 'Mayoz I homolog, II kromatit ayırır'))
C.append(K('bio-hucrede-bolunme-04', 'bio', 'Bölünmede kromozom ve hücre hesabı',
 'Döngü süresinden hücre sayısını, evrelerden kromozom ve kromatit sayısını hesaplayabilmeni.',
 'Her mitozda hücre sayısı **iki katına** çıkar; n bölünmede 2 üzeri n hücre olur. Önce toplam süreyi döngü süresine bölüp **tam** döngü sayısını bul. DNA eşlenince her kromozom iki kardeş kromatitli olur; mitozda yavru hücre ana hücreyle aynı kromozom sayısındadır.',
 'Hücre sayısı = 2 üzeri tam bölünme sayısı', None,
 'Döngüsü 6 saat süren bir hücre 28 saatte en çok kaç hücre olur?',
 ['Tam bölünme sayısı: 28 ÷ 6 = 4,66; tam sayı 4.', 'Tamamlanmamış beşinci bölünme sayılmaz.', 'Hücre sayısı: 2 üzeri 4 = 16.'],
 '16 hücre.',
 'Bölünme sayısını hücre sayısı sanmak ya da 4,66\'yı 5\'e yuvarlamak. Yalnız biten döngüler sayılır; sonra 2\'nin kuvvetini al.',
 'Tam döngüyü say, 2 üzeri al'))
C.append(K('bio-kalitim-01', 'bio', 'ABO ve Rh kan grupları',
 'Kan gruplarından genotipleri bulup ABO ve Rh olasılıklarını birlikte hesaplayabilmeni.',
 'A ve B alelleri O\'ya baskındır, birbirine **eş baskındır**. A grubu AA ya da AO, B grubu BB ya da BO, AB grubu AB, O grubu OO\'dur. O grubu çocuk her ebeveynden **bir O aleli** almıştır. Ayrı özelliklerin olasılıkları çarpılır.',
 'Bağımsız özellikler: olasılıklar çarpılır', None,
 'Anne AO ve Rh pozitif (Rr), baba BO ve Rh negatif (rr). Çocuğun O grubu ve Rh negatif olma olasılığı nedir?',
 ['O grubu için: AO × BO, 4 birleşmeden 1\'i OO, yani 1/4.', 'Rh negatif için: Rr × rr, 1/2 rr.', 'Birlikte: 1/4 × 1/2 = 1/8.'],
 '1/8.',
 'İlk çocuğun O olmasından sonra AB olamayacağını sanmak; her doğum bağımsızdır. Gametleri çarpıp bir de bölmek de yanlıştır.',
 'O çocuk, her ebeveynden bir O'))
C.append(K('bio-kalitim-03', 'bio', 'Soy ağacı analizi',
 'Soy ağacından kalıtım biçimini ve ebeveyn genotiplerini çıkarabilmeni.',
 'Ebeveynde görülmeyen özellik çocukta ortaya çıkıyorsa özellik **çekiniktir** ve ebeveynler **taşıyıcıdır** (Aa). Hasta kızın babası sağlıklıysa özellik eşeye bağlı çekinik olamaz. Dolu simge özelliği gösteren bireyi belirtir.',
 'Aa × Aa → 1 AA : 2 Aa : 1 aa', sek_soy,
 'Sağlıklı ebeveynlerin ilk çocuğu hasta. İkinci çocuğun da hasta olma olasılığı nedir?',
 ['Sağlıklı ebeveynde hasta çocuk: hastalık çekiniktir.', 'Ebeveynler taşıyıcıdır: Aa × Aa.', 'aa olasılığı 1/4.'],
 '1/4.',
 'Ebeveynlerin heterozigot olduğunu fark etmemek ya da Aa × Aa\'da çekinik olasılığını 1/2 sanmak. Sağlıklı iki ebeveyn, hasta çocuk: hep 1/4.',
 'Ebeveynde yok, çocukta var: çekinik'))
C.append(K('bio-kalitim-05', 'bio', 'Gamet çeşidi sayısı',
 'Bir genotipten kaç çeşit gamet oluşabileceğini bulabilmeni.',
 'Heterozigot gen çifti (Aa) **2 çeşit** gamet verir; homozigot çift (AA, aa) **1 çeşit**. Çeşit sayısı, **2 üzeri heterozigot çift sayısıdır**; örneğin AaBb için 4.',
 'Çeşit = 2 üzeri heterozigot çift sayısı', None,
 'AaBBCcDd genotipli bir bireyden kaç çeşit gamet oluşur?',
 ['Heterozigot çiftleri say: Aa, Cc, Dd = 3 tane.', 'BB homozigottur, çeşit katmaz.', '2 üzeri 3 = 8.'],
 '8 çeşit.',
 'Gen çifti sayısını 2 ile çarpmak ya da homozigot BB çiftini de 2 çeşit saymak. Yalnız heterozigot çiftleri say.',
 'Gamet çeşidi: 2 üzeri heterozigot'))
C.append(K('bio-kalitim-07', 'bio', 'Monohibrit ve dihibrit çaprazlama',
 'Tek ve iki karakterli çaprazlamada genotip ile fenotip olasılıklarını hesaplayabilmeni.',
 'Önce her ebeveynin **gametlerini** yaz, sonra kareyi doldur. Aa × Aa → 1 AA : 2 Aa : 1 aa; baskın görünüş **3 : 1**. Bağımsız iki özellikte olasılıklar **çarpılır**; baskın özellik heterozigotta da görünür.',
 'Aa × Aa → AA : Aa : aa = 1 : 2 : 1', sek_punnett,
 'Yuvarlak (R) tohum buruşuğa, sarı (S) renk yeşile baskın. RrSs × RrSs çaprazlamasında yavrunun yuvarlak ve yeşil olma olasılığı nedir?',
 ['Yuvarlak için Rr × Rr: R_ olasılığı 3/4.', 'Yeşil için Ss × Ss: ss olasılığı 1/4.', 'Çarp: 3/4 × 1/4 = 3/16.'],
 '3/16.',
 'Heterozigot ebeveynden çekinik yavru çıkmayacağını sanmak ya da dört birleşmeyi 16 sanıp olasılığı küçültmek. Her özelliği ayrı kareyle bul, sonra çarp.',
 'Önce gamet, sonra kare'))

# --- doğrulama ---
ids = re.findall(r'^### (\S+) \|', open(IN, encoding='utf-8').read(), flags=re.M)
assert [c['id'] for c in C] == ids and len(set(ids)) == len(ids), (len(C), len(ids))
def w(s): return len(s.replace('**', '').split())
for c in C:
    assert c['baslik'] and w(c['baslik']) <= 6, c['id']
    assert w(c['olcer']) <= 25 and not c['olcer'].startswith('Bu soru'), c['id']
    assert w(c['kural']) <= 60 and '**' in c['kural'], (c['id'], w(c['kural']))
    assert w(c['hata']) <= 40, (c['id'], w(c['hata']))
    assert w(c['akilda']) <= 8 and '"' not in c['akilda'], c['id']
    o = c['ornek']
    assert o['soru'] and 2 <= len(o['adimlar']) <= 4 and o['cevap'], c['id']
    if c['sekil']:
        assert len(c['sekil']) <= 25000
    assert c['formul'] is None or isinstance(c['formul'], str)
json.dump(C, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(C), 'kart,', sum(1 for c in C if c['sekil']), 'şekilli')
