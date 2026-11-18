import sys, re, json, math
sys.path.insert(0, '/home/claude/zekacademy-app/havuz')

# ---------- hesaplar (assert) ----------
# 1) Zn + 2HCl -> ZnCl2 + H2
n_zn = 13 / 65; m_h2 = n_zn * 2
assert abs(n_zn - 0.2) < 1e-9 and abs(m_h2 - 0.4) < 1e-9
# 3) X: A=31, n=16, 3-
p3 = 31 - 16; e3 = p3 + 3
assert (p3, e3) == (15, 18)
# 6) C3H8 + 5O2 -> 3CO2 + 4H2O
a, b, c, d = 1, 5, 3, 4
assert 3*a == c and 8*a == 2*d and 2*b == 2*c + d and a + b + c + d == 13
# 9) 2CO + O2 -> 2CO2, 12 L CO, 9 L O2
co, o2 = 12, 9; gerek = co / 2; artan = o2 - gerek; co2 = co
assert (gerek, artan, co2, co2 + artan) == (6, 3, 12, 15)
# 10) Ca:O = 5/2, 20 g Ca, 10 g O
g_o = 20 * 2 / 5; assert g_o == 8 and 10 - g_o == 2 and 20 + g_o == 28
# 11) 2Na + Cl2 -> 2NaCl
n_na = 4.6 / 23; n_cl = 0.3
assert abs(n_na - 0.2) < 1e-9 and (n_na / 2) < (n_cl / 1)
harc = n_na / 2; kal = n_cl - harc
assert abs(kal - 0.2) < 1e-9 and abs(kal * 71 - 14.2) < 1e-9
# 12) CaCO3
M = 40 + 12 + 3 * 16; assert M == 100 and 3 * 16 / M * 100 == 48
# 15) atom no 12 ve 9
def diz(z):
    out = []
    for k in (2, 8, 8):
        t = min(k, z); out.append(t); z -= t
        if z == 0: break
    return out
assert diz(12) == [2, 8, 2] and diz(9) == [2, 7]
ver, al = 2, 1  # XY2
assert ver == al * 2
# 20) 2,8,6
assert diz(16) == [2, 8, 6] and len(diz(16)) == 3 and diz(16)[-1] == 6

# ---------- şekiller ----------
S = 'stroke-width="2" fill="none"'
def svg(label, body, h=170):
    return (f'<svg viewBox="0 0 280 {h}" role="img" aria-label="{label}">{body}</svg>')

# sabun + yağ damlası
cx, cy = 140, 82
b = [f'<circle cx="{cx}" cy="{cy}" r="26" fill="var(--warn-soft)" stroke="var(--warn)" stroke-width="2"/>',
     f'<text x="{cx-8}" y="{cy+4}" font-size="12">yağ</text>']
for i in range(10):
    t = 2 * math.pi * i / 10
    x1, y1 = cx + 26 * math.cos(t), cy + 26 * math.sin(t)
    x2, y2 = cx + 50 * math.cos(t), cy + 50 * math.sin(t)
    b.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="var(--warn)" stroke-width="2"/>')
    x3, y3 = cx + 56 * math.cos(t), cy + 56 * math.sin(t)
    b.append(f'<circle cx="{x3:.1f}" cy="{y3:.1f}" r="6" fill="var(--brand)"/>')
b.append('<circle cx="14" cy="148" r="6" fill="var(--brand)"/><text x="26" y="152" font-size="12">polar baş: suya dönük</text>')
b.append('<line x1="8" y1="164" x2="20" y2="164" stroke="var(--warn)" stroke-width="2"/><text x="26" y="168" font-size="12">apolar zincir: yağa dönük</text>')
SEKIL_SABUN = svg("Yağ damlasının çevresinde sabun molekülleri: apolar zincirler damlaya, polar başlar suya dönük", "".join(b), 176).replace('0 0 280 170', '0 0 280 176')

# ısıtma grafiği
isit = ('<line x1="40" y1="145" x2="268" y2="145" stroke="var(--muted)" stroke-width="1.5"/>'
        '<line x1="40" y1="145" x2="40" y2="20" stroke="var(--muted)" stroke-width="1.5"/>'
        '<polyline points="46,140 80,115 120,115 150,80 205,80 250,58" fill="none" stroke="var(--rule)" stroke-width="2.5"/>'
        '<text x="4" y="14" font-size="12">Sıcaklık</text><text x="222" y="162" font-size="12">Isı</text>'
        '<text x="42" y="106" font-size="11">katı</text>'
        '<text x="76" y="106" font-size="11" fill="var(--warn)">katı + sıvı</text>'
        '<text x="124" y="134" font-size="11">sıvı</text>'
        '<text x="154" y="72" font-size="11" fill="var(--warn)">sıvı + gaz</text>'
        '<text x="218" y="98" font-size="11">gaz</text>')
SEKIL_ISIT = svg("Isıtma grafiği: eğimli aralıklarda tek hâl, yatay aralıklarda iki hâl birlikte", isit)

# tanecik modeli
tb = []
for i, (x0, ad) in enumerate([(10, 'Katı'), (100, 'Sıvı'), (190, 'Gaz')]):
    tb.append(f'<rect x="{x0}" y="14" width="80" height="96" rx="6" fill="none" stroke="var(--muted)" stroke-width="1.5"/>')
    tb.append(f'<text x="{x0+28}" y="132" font-size="13" font-weight="600">{ad}</text>')
for r in range(4):
    for c_ in range(4):
        tb.append(f'<circle cx="{26+c_*16}" cy="{30+r*20}" r="6" fill="var(--brand)"/>')
liq = [(112,100),(126,96),(140,102),(154,98),(116,80),(132,76),(148,82),(160,78),(112,60),(128,56),(144,62),(158,58),(118,38),(134,34),(150,40),(120,98-60+20)]
for x, y in liq[:15]:
    tb.append(f'<circle cx="{x}" cy="{y}" r="6" fill="var(--brand)"/>')
for x, y in [(204,28),(246,40),(222,64),(258,92),(206,96),(240,102)]:
    tb.append(f'<circle cx="{x}" cy="{y}" r="6" fill="var(--brand)"/>')
tb.append('<text x="10" y="156" font-size="11">Plazma: iyon + serbest elektron (iletir)</text>')
SEKIL_TANECIK = svg("Katıda düzenli sıkı, sıvıda düzensiz yakın, gazda uzak dağınık tanecikler", "".join(tb), 164)

# periyodik eğilimler
per = ('<defs><marker id="ok" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="var(--brand)"/></marker></defs>'
       '<line x1="30" y1="14" x2="264" y2="14" stroke="var(--brand)" stroke-width="2.5" marker-end="url(#ok)"/>'
       '<line x1="14" y1="26" x2="14" y2="160" stroke="var(--brand)" stroke-width="2.5" marker-end="url(#ok)"/>'
       '<rect x="30" y="28" width="236" height="132" rx="8" fill="var(--rule-soft)" stroke="var(--muted)"/>'
       '<text x="40" y="48" font-size="12" font-weight="600" fill="var(--rule)">Periyotta soldan sağa</text>'
       '<text x="40" y="66" font-size="12">yarıçap azalır</text>'
       '<text x="40" y="82" font-size="12">elektronegatiflik artar</text>'
       '<text x="40" y="98" font-size="12">metalik karakter azalır</text>'
       '<text x="40" y="122" font-size="12" font-weight="600" fill="var(--warn)">Grupta yukarıdan aşağı</text>'
       '<text x="40" y="140" font-size="12">yarıçap artar</text>'
       '<text x="40" y="156" font-size="12">elektronegatiflik azalır</text>')
SEKIL_PER = svg("Periyotta soldan sağa ve grupta yukarıdan aşağı periyodik özelliklerin değişimi", per)

# gaz hacim kutuları
gz = []
def kare(x): gz.append(f'<rect x="{x}" y="46" width="30" height="30" rx="3" fill="var(--brand-soft)" stroke="var(--brand)" stroke-width="2"/>')
for x in (20, 54): kare(x)
kare(122)
for x in (196, 230): kare(x)
gz += ['<text x="94" y="68" font-size="18">+</text>', '<text x="158" y="68" font-size="18">→</text>',
       '<text x="30" y="100" font-size="13" font-weight="600">CO</text>', '<text x="124" y="100" font-size="13" font-weight="600">O₂</text>',
       '<text x="206" y="100" font-size="13" font-weight="600">CO₂</text>',
       '<text x="22" y="120" font-size="12">2 hacim</text>', '<text x="116" y="120" font-size="12">1 hacim</text>', '<text x="198" y="120" font-size="12">2 hacim</text>']
SEKIL_GAZ = svg("2CO + O₂ → 2CO₂ tepkimesinde hacim oranı 2 : 1 : 2", "".join(gz), 134)

# ---------- kartlar ----------
K = []
def kart(id, k, baslik, olcer, kural, formul, sekil, soru, adimlar, cevap, hata, akilda):
    K.append({"id": id, "k": k, "baslik": baslik, "olcer": olcer, "kural": kural, "formul": formul, "sekil": sekil,
              "ornek": {"soru": soru, "adimlar": adimlar, "cevap": cevap}, "hata": hata, "akilda": akilda})

kart("kim-asitler-bazlar-02", "kim|Asitler, Bazlar ve Tuzlar", "Nötrleşme ve tuz formülü",
 "Asit–baz ve asit–metal tepkimelerinde oluşan tuzun formülünü ve gazın miktarını bulabilmeni.",
 "Asit + baz → **tuz + su**. Tuz, bazdaki metal iyonu ile asittaki negatif iyondan oluşur. Formülde **yükleri çaprazla**: katyonun yükü anyonun indisi olur. Asit + metal tepkimesinde tuz ile H₂ gazı çıkar; miktarı mol hesabıyla bulunur.",
 "Ca²⁺ + PO₄³⁻ → Ca₃(PO₄)₂", None,
 "Zn + 2HCl → ZnCl₂ + H₂ tepkimesinde 13 g Zn harcanırsa kaç g H₂ çıkar? (Zn: 65, H: 1 g/mol)",
 ["Zn mol sayısı: 13 ÷ 65 = 0,2 mol", "Denklemde 1 Zn → 1 H₂ olduğundan 0,2 mol H₂ oluşur", "H₂ kütlesi: 0,2 × 2 = 0,4 g"],
 "0,4 g H₂",
 "Yükleri çaprazlamayı unutmak ya da ters çaprazlamak. Kontrol: toplam artı yük, toplam eksi yüke eşit olmalı; Al₂(SO₄)₃'te 2 × 3 = 3 × 2.",
 "Yükleri çaprazla, sonra sıfırı kontrol et.")

kart("kim-atom-ve-01", "kim|Atom ve Yapısı", "Atom modelleri ve katkıları",
 "Atom modellerini bilim insanlarıyla ve her modelin getirdiği yenilikle eşleştirebilmeni.",
 "Dalton: bölünemeyen küre. Thomson: elektronun keşfi; artı yüklü kütle içinde elektronlar. Rutherford: alfa saçılmasıyla **çekirdeğin varlığı**. Bohr: **belirli enerjili katmanlar**. Her model, öncekinin açıklayamadığı bir gözlemle ortaya çıkmıştır.",
 "Dalton → Thomson → Rutherford → Bohr", None,
 "Altın levhaya gönderilen alfa parçacıklarının çoğu levhadan geçiyor, çok azı geri dönüyor. Atom için ne söylenebilir?",
 ["Çoğu geçiyor: atomun büyük kısmı boşluktur", "Çok azı geri dönüyor: aynı yüklü, küçük ve yoğun bir bölge onları itiyor", "Bu artı yüklü bölge çekirdektir"],
 "Atomda küçük, yoğun, artı yüklü bir çekirdek vardır.",
 "Thomson ile Rutherford'u karıştırmak. Kontrol: dağınık elektronlu \"üzümlü kek\" modelinde çekirdek yoktur; çekirdek Rutherford'la, katmanlar Bohr'la gelir.",
 "Çekirdek Rutherford, katmanlar Bohr.")

kart("kim-atom-ve-03", "kim|Atom ve Yapısı", "İyon ve izoelektronik tanecikler",
 "İyonun proton, nötron ve elektron sayısını yükünden ve kütle numarasından bulabilmeni.",
 "Kütle numarası = proton + nötron; elektron katılmaz. Nötr atomda elektron = proton. **Artı yüklü iyonda elektron = proton − yük**; **eksi yüklü iyonda elektron = proton + yük**. Elektron sayıları eşit taneciklere izoelektronik denir.",
 "elektron = proton − yük (yük işaretiyle)", None,
 "Kütle numarası 31, nötron sayısı 16 olan X taneciği 3− yüklüdür. Kaç elektronu vardır?",
 ["Proton: 31 − 16 = 15", "Yük 3−: elektron protondan 3 fazladır", "Elektron: 15 + 3 = 18"],
 "18 elektron",
 "Eksi yükü elektrondan çıkarmak. Kontrol: eksi yük elektron fazlalığıdır, yani elektron protondan çoktur. Artı yükte elektron protondan azdır; iyonda ikisi eşit olmaz.",
 "Eksi yük, fazla elektron demektir.")

K.append({"id": "kim-karisimlar-01", "kapsamDisi": True,
          "neden": "Koligatif özellikler TYT (MEB 9–10) kapsamı dışında; yalnız 2 soru."})

kart("kim-karisimlar-03", "kim|Karışımlar", "Çözünme ve çözelti iletkenliği",
 "Çözünme türüne göre çözeltide iyon mu molekül mü bulunduğunu ve iletkenliği yorumlayabilmeni.",
 "**İyonik** bileşikler çözününce iyonlarına ayrışır; serbest iyonlar akımı iletir. **Moleküler** maddeler çözününce yüksüz molekülleri dağılır; çözelti iletmez. Benzer benzeri çözer. Doygun çözeltide fazla madde çözünmez; sıcaklık düşünce çözünürlük azalır ve fazlası çöker.",
 "İyonik → iyon → iletir · Moleküler → molekül → iletmez", None,
 "Potasyum bromür (KBr) ve gliserin ayrı ayrı suda çözünüyor. Hangi çözelti elektrik akımını iletir?",
 ["KBr iyoniktir; çözününce K⁺ ve Br⁻ serbest iyonları oluşur", "Gliserin moleküler maddedir; yüksüz molekülleri bozulmadan dağılır", "Yük taşıyıcı yalnız KBr çözeltisinde vardır"],
 "Yalnız KBr çözeltisi iletir.",
 "Her çözeltinin iletken olduğunu sanmak. Kendine sor: çözününce ne oluştu? Serbest iyon varsa çözelti iletir, yalnız yüksüz molekül varsa iletmez.",
 "İyon varsa iletir, molekül varsa iletmez.")

kart("kim-kimya-bilimi-01", "kim|Kimya Bilimi", "Atom sayma ve denkleştirme",
 "Katsayı ve indislerle formülde atom sayısını bulup denklemi denkleştirebilmeni.",
 "**Katsayı** bütün formül birimini çoğaltır. **Parantez dışındaki indis**, paranteze giren her atomu çoğaltır. Denkleştirirken yalnız katsayı değişir, indis değişmez. Her atom, tepkimenin iki yanında eşit sayıda olmalıdır.",
 "4Mg(NO₃)₂ → Mg: 4 · N: 4×2 = 8 · O: 4×2×3 = 24", None,
 "C₃H₈ + O₂ → CO₂ + H₂O denklemini denkleştirirsen katsayılar toplamı kaç olur?",
 ["C: 3 olduğundan 3CO₂; H: 8 olduğundan 4H₂O", "Sağdaki O: 3 × 2 + 4 = 10, yani 5O₂", "C₃H₈ + 5O₂ → 3CO₂ + 4H₂O; toplam 1 + 5 + 3 + 4 = 13"],
 "13",
 "Katsayıyı ya da parantez dışı indisi hesaba katmamak. Kontrol: önce parantezi aç, sonra katsayıyla çarp; 3Ca(OH)₂'de O sayısı 3 × 2 = 6'dır.",
 "Önce parantezi aç, sonra katsayıyla çarp.")

kart("kim-kimya-bilimi-03", "kim|Kimya Bilimi", "Laboratuvar güvenliği ve malzemeleri",
 "Güvenli ve güvensiz laboratuvar davranışlarını ayırt edip malzemeleri kullanım amacına göre eşleştirebilmeni.",
 "Asit suya **azar azar** eklenir. Koku, elle yelpazelenerek anlaşılır. Artan kimyasal şişeye geri konmaz. Zehirli gazlarda **çeker ocak** kullanılır. Dereceli silindir hacim ölçer; beherglas hazırlama ve ısıtmada, erlenmayer çalkalamada kullanılır. Alev yanıcı, kuru kafa zehirli demektir.",
 None, None,
 "Bir öğrenci derişik sülfürik asidi seyreltmek için asidin üzerine su döküyor. Bu davranış doğru mu?",
 ["Asit ile su karışırken çok ısı açığa çıkar", "Suyu asidin üstüne dökersen karışım kaynayıp sıçrayabilir", "Doğrusu: asit suya azar azar ve karıştırılarak eklenir"],
 "Yanlış; asit suya eklenmeli.",
 "Kimyasalla doğrudan temas ya da kirletme içeren davranışı doğru sanmak (koklamak, artanı şişeye geri koymak). Kontrol: davranış seni zehirliyor ya da kimyasalı kirletiyor mu?",
 "Asit suya azar azar eklenir.")

kart("kim-kimya-her-02", "kim|Kimya Her Yerde", "Sabun ve deterjan",
 "Sabun molekülünün polar ve apolar kısımlarının suyla ve yağla nasıl etkileştiğini yorumlayabilmeni.",
 "Sabun molekülünün bir ucu **iyonik (polar)**, öbür ucu **apolar hidrokarbon zinciridir**. Polar uç suya, apolar zincir yağa çekilir; sabun yağı suda dağıtıp temizler. Temizlik maddeleri kendi ambalajında, çocukların ulaşamayacağı yerde saklanır.",
 "Polar uç ↔ su · Apolar zincir ↔ yağ", SEKIL_SABUN,
 "Sabun yağlı bir bardağı yıkarken sabun moleküllerinin hangi ucu yağ damlasına dönük olur?",
 ["Yağ apolardır; benzer benzeri çözer", "Apolar uç hidrokarbon zinciridir, yağa yönelir", "İyonik uç suya dönük kalır; damla suda dağılır"],
 "Hidrokarbon zinciri (apolar uç) yağa dönük olur.",
 "Zincirin de suyu sevdiğini sanmak. Kontrol: hidrokarbon zinciri apolardır, suda iyi çözünmez; suya dönük olan yalnız iyonik uçtur.",
 "İyonik uç suyu, zincir yağı sever.")

kart("kim-kimyanin-temel-01", "kim|Kimyanın Temel Kanunları", "Gaz hacim oranları ve Avogadro",
 "Tepkimede gazların hacimlerini katsayı oranından bulup artan gazı hesaba katabilmeni.",
 "Aynı sıcaklık ve basınçta gazlar **katsayı oranında hacimle** birleşir. Eşit hacimli gazlar (Avogadro) **eşit sayıda tanecik** içerir. Önce sınırlayıcı gazı bul; ürünü ve artan gazı ayrı hesapla. Toplam hacim genelde korunmaz.",
 "2CO + O₂ → 2CO₂ : hacim oranı 2 : 1 : 2", SEKIL_GAZ,
 "Aynı koşullarda 2CO + O₂ → 2CO₂ tepkimesine 12 L CO ile 9 L O₂ giriyor. Tepkime sonunda kaptaki toplam gaz hacmi kaç L'dir?",
 ["12 L CO için 12 ÷ 2 = 6 L O₂ gerekir; CO sınırlayıcıdır", "Artan O₂: 9 − 6 = 3 L", "CO₂ hacmi CO ile aynı katsayıda: 12 L", "Toplam: 12 + 3 = 15 L"],
 "15 L",
 "Yalnız ürünün hacmini yazıp artan gazı unutmak. Kontrol: soru \"kaptaki toplam gaz\" diyorsa ürünü ve artan gazı birlikte topla.",
 "Katsayı oranı, hacim oranıdır.")

kart("kim-kimyanin-temel-03", "kim|Kimyanın Temel Kanunları", "Sabit oranlar kanunu",
 "Elementlerin sabit kütle oranından artan maddeyi ve oluşan bileşiğin kütlesini bulabilmeni.",
 "Bir bileşikte elementlerin **kütlece oranı sabittir**. Oranı koruyacak kadar madde birleşir, **fazla gelen madde artar**. Oluşan bileşiğin kütlesi yalnız birleşenlerin toplamıdır; artan madde ürüne katılmaz.",
 "Ürün kütlesi = birleşen A + birleşen B", None,
 "Ca ve O kütlece 5/2 oranında birleşir. 20 g Ca ile 10 g O tepkimeye girerse kaç g bileşik oluşur?",
 ["20 g Ca ile birleşen O: 20 × 2 ÷ 5 = 8 g", "O 10 g olduğundan 2 g artar; Ca sınırlayıcıdır", "Ürün: 20 + 8 = 28 g"],
 "28 g",
 "Girenlerin tamamını ürün sanmak. Kontrol: artan madde tepkimeye girmemiştir; ürün kütlesi yalnız gerçekten birleşenlerin toplamıdır.",
 "Önce oranı kur, artanı ayır.")

kart("kim-kimyasal-hesaplamalar-01", "kim|Kimyasal Hesaplamalar", "Sınırlayıcı bileşen ve artan madde",
 "Hangi maddenin önce bittiğini bulup ürün ve artan madde miktarını hesaplayabilmeni.",
 "Mol = kütle ÷ mol kütlesi. Her maddenin mol sayısını **katsayısına böl**; **en küçük değer sınırlayıcıdır**, önce biter ve ürünü o belirler. Artan miktar, eldeki moldan harcananın çıkarılmasıyla bulunur. Verim varsa gerçek ürün = teorik ürün × verim.",
 "mol ÷ katsayı: en küçük → sınırlayıcı", None,
 "2Na + Cl₂ → 2NaCl tepkimesinde 4,6 g Na ile 0,3 mol Cl₂ tepkimeye giriyor. Kaç g Cl₂ artar? (Na: 23, Cl: 35,5 g/mol)",
 ["Na: 4,6 ÷ 23 = 0,2 mol. Katsayıya böl: Na 0,2 ÷ 2 = 0,1; Cl₂ 0,3 ÷ 1 = 0,3", "En küçük Na'dadır, sınırlayıcı Na'dır", "0,2 mol Na, 0,1 mol Cl₂ harcar; artan 0,3 − 0,1 = 0,2 mol", "Kütle: 0,2 × 71 = 14,2 g"],
 "14,2 g Cl₂",
 "Maddeleri 1 : 1 oranında tepkimeye sokmak ya da eklenen maddenin tamamını artan saymak. Kontrol: mol sayılarını daima denklemdeki katsayıyla karşılaştır.",
 "Mol ÷ katsayı, en küçük sınırlar.")

kart("kim-kimyasal-hesaplamalar-03", "kim|Kimyasal Hesaplamalar", "Kütlece yüzde ve basit formül",
 "Bileşiğin formülünden kütlece yüzdeyi, kütle verilerinden basit formülü bulabilmeni.",
 "**Kütlece yüzde** = (formüldeki elementin toplam kütlesi ÷ bileşiğin mol kütlesi) × 100. İndis, kütleyi o sayıda artırır. **Basit formül** için kütleler atom kütlesine bölünür, oran en küçük tam sayılara getirilir. Molekül formülü basit formülün katıdır.",
 "% X = (indis × atom kütlesi ÷ mol kütlesi) × 100", None,
 "CaCO₃ bileşiğinde oksijen kütlece yüzde kaçtır? (Ca: 40, C: 12, O: 16)",
 ["Mol kütlesi: 40 + 12 + 3 × 16 = 100", "Oksijenin toplam kütlesi: 3 × 16 = 48", "Yüzde: 48 ÷ 100 × 100 = 48"],
 "%48",
 "Atom sayısına bakıp yüzdeyi bulmak (4 atomdan 1'i → %25). Kontrol: yüzde kütleyle hesaplanır; atom kütlesini indisle çarpmayı unutma.",
 "Yüzde atom sayısıyla değil kütleyle bulunur.")

kart("kim-kimyasal-turler-01", "kim|Kimyasal Türler Arası Etkileşimler", "Zayıf etkileşimler ve kaynama noktası",
 "Moleküllerin yapısından baskın zayıf etkileşimi belirleyip kaynama noktalarını karşılaştırabilmeni.",
 "Apolar moleküller arasında London, polar moleküller arasında dipol–dipol vardır. H atomu F, O ya da N'ye bağlıysa **hidrojen bağı** oluşur. Etkileşim güçlendikçe **kaynama noktası yükselir**. Apolar maddelerde mol kütlesi büyüdükçe London kuvvetleri artar.",
 "London < dipol–dipol < hidrojen bağı", None,
 "CH₃OH ile C₂H₆ moleküllerinin baskın etkileşimlerini yaz. Hangisi daha yüksek sıcaklıkta kaynar?",
 ["CH₃OH: H, O atomuna bağlı, yani hidrojen bağı vardır", "C₂H₆ apolardır, baskın etkileşim London kuvvetleridir", "Hidrojen bağı London kuvvetinden güçlüdür, CH₃OH daha yüksek kaynar"],
 "CH₃OH daha yüksek sıcaklıkta kaynar.",
 "H içeren her molekülde hidrojen bağı sanmak. Kontrol: H, doğrudan F, O ya da N atomuna bağlı olmalıdır; HBr ve CH₄'te hidrojen bağı yoktur.",
 "H, F, O, N'ye bağlıysa hidrojen bağı.")

kart("kim-kimyasal-turler-03", "kim|Kimyasal Türler Arası Etkileşimler", "Çözünme ve fiziksel–kimyasal değişim",
 "Maddelerin polarlığına göre çözünmeyi yorumlayıp hangi etkileşimlerin koptuğunu ayırt edebilmeni.",
 "**Benzer benzeri çözer**: polar ve iyonik maddeler polar çözücüde (su), apolar maddeler apolar çözücüde (CCl₄) çözünür. Fiziksel değişimde madde kimliği değişmez, yalnız moleküller arası etkileşim kopar. **Kimyasal değişimde** atomlar arası bağlar kopar, yeni madde oluşur.",
 "Fiziksel: moleküller arası kopar · Kimyasal: bağlar kopar", None,
 "Şekerin suda çözünmesi ile kâğıdın yanmasından hangisinde atomlar arası bağlar kopar?",
 ["Şekerin çözünmesi fiziksel olaydır; madde kimliği aynı kalır", "Kâğıdın yanması kimyasal olaydır; yeni maddeler oluşur", "Yanmada atomlar arası bağlar kopar; çözünmede ve hâl değişiminde yalnız moleküller arası etkileşim kopar"],
 "Kâğıdın yanmasında.",
 "Hâl değişiminde atomlar arası bağların koptuğunu sanmak. Kontrol: kaynayan suda H–O bağları sağlam kalır, yalnız moleküller arası etkileşim kopar; yeni madde oluşmadıysa değişim fizikseldir.",
 "Önce etiketle: polar, apolar, iyonik.")

kart("kim-kimyasal-turler-05", "kim|Kimyasal Türler Arası Etkileşimler", "Bağ türü ve bileşik formülü",
 "Elementlerin türünden bağ türünü, atom numarasından bileşik formülünü bulabilmeni.",
 "**Metal + ametal**: elektron aktarımıyla iyonik bağ. **Ametal + ametal**: ortak elektron kullanımıyla kovalent bağ. Elektronlar katmanlara 2, 8, 8 sırasıyla dizilir. Metal son katmanındaki elektronları verir, ametal oktetini tamamlayacak kadar alır; verilen ve alınan sayılar eşitlenir.",
 "Metal + ametal → iyonik · Ametal + ametal → kovalent", None,
 "Atom numarası 12 olan X ile atom numarası 9 olan Y arasında oluşan bileşiğin formülü ve bağ türü nedir?",
 ["X: 2, 8, 2 (2 elektron verir, metal). Y: 2, 7 (1 elektron alır, ametal)", "Verilen ve alınan eşit olsun: 1 X için 2 Y gerekir, formül XY₂", "Metal + ametal olduğundan bağ iyoniktir"],
 "XY₂, iyonik bağ",
 "Elementlerin metal mi ametal mi olduğuna bakmadan bağ türüne karar vermek. Kontrol: yalnız ametaller (C, H, O gibi) varsa bağ kovalenttir.",
 "Metal varsa iyonik, yoksa kovalent.")

kart("kim-maddenin-halleri-02", "kim|Maddenin Halleri", "Hâl değişimleri ve ısıtma grafiği",
 "Isıtma grafiğinin her aralığında maddenin hangi hâlde bulunduğunu belirleyebilmeni.",
 "Saf maddede sıcaklığın arttığı eğimli aralıkta madde **tek hâldedir**. Sıcaklığın sabit kaldığı yatay aralıkta hâl değişimi olur ve **iki hâl birlikte** bulunur. Karışımda hâl değişimi sırasında sıcaklık sabit kalmaz, bir sıcaklık aralığında gerçekleşir.",
 "Eğimli → tek hâl · Yatay → iki hâl birlikte", SEKIL_ISIT,
 "Katı hâldeki saf X maddesi ısıtılıyor; sıcaklık 20 °C'den 60 °C'ye çıkıyor, 60 °C'de 5 dakika sabit kalıyor, sonra yeniden artıyor. Sabit kalan aralıkta madde hangi hâllerdedir?",
 ["Sıcaklığın sabit kalması hâl değişimini gösterir", "60 °C altında madde katıdır, üstünde sıvı olur: bu aralık erimedir", "Erimede katı ve sıvı birlikte bulunur"],
 "Katı + sıvı",
 "Yatay aralıkta maddenin yalnız sıvı (ya da yalnız gaz) olduğunu sanmak. Kontrol: sıcaklık sabitse hâl değişimi sürüyordur, iki hâl birlikte bulunur.",
 "Eğim tek hâl, yatay iki hâl.")

kart("kim-maddenin-halleri-04", "kim|Maddenin Halleri", "Katı türleri ve özellikleri",
 "İletkenlik ve erime noktası verilerinden katının iyonik, metalik, kovalent ağ ya da moleküler olduğunu bulabilmeni.",
 "Katı hâlde **iletiyorsa metaliktir**. Katıda iletmeyip sıvıda ya da çözeltide **iletiyorsa iyoniktir**. Hiç iletmeyen ve erime noktası çok yüksek olan kovalent ağ, düşük olan moleküler katıdır. Kristal katı belirli sıcaklıkta erir; amorf katı (cam) giderek yumuşar.",
 "katıda iletir → metalik · sıvıda iletir → iyonik", None,
 "X katısı katı hâlde iletmiyor, sıvı hâlde iletiyor. Y katısı hiçbir hâlde iletmiyor ve erime noktası çok yüksek. X ve Y hangi katı türüdür?",
 ["X: katıda iletmez, sıvıda iletir; bu iyonik katıdır", "Y: hiç iletmez ve erime noktası çok yüksek; bu kovalent ağ katısıdır", "Y'nin erime noktası düşük olsaydı moleküler katı olurdu"],
 "X iyonik, Y kovalent ağ katısı.",
 "Sıvıda iletmeyi metalik katı belirtisi sanmak. Kontrol: metaller katıyken de iletir; katıda iletmeyip yalnız sıvıda ileten madde iyoniktir.",
 "Katıda iletir metalik, sıvıda iletir iyonik.")

kart("kim-maddenin-halleri-06", "kim|Maddenin Halleri", "Hâllerin tanecik modeli ve plazma",
 "Kaplardaki tanecik dizilişine bakıp katı, sıvı, gaz ve plazma hâllerini ayırt edebilmeni.",
 "Katıda tanecikler **düzenli ve sıkı** dizilir, yerinde titreşir. Sıvıda düzensiz ama yakındır, birbiri üzerinde kayar. Gazda birbirinden çok uzaktır, kabın tamamına yayılır. Plazma **iyonlaşmış gazdır**; serbest iyon ve elektron içerdiği için iletir. Tanecikleri uzaklaştıran hâl değişimi ısı alır.",
 "Düzenli-sıkı: katı · yakın-düzensiz: sıvı · uzak: gaz", SEKIL_TANECIK,
 "Bir kapta tanecikler düzensiz ama birbirine yakın ve birbiri üzerinde kayıyor. Bu maddenin tanecikleri birbirinden çok uzaklaşırsa hangi hâl değişimi olur, ısı alınır mı verilir mi?",
 ["Düzensiz ama yakın dizilim: madde sıvıdır", "Tanecikler çok uzaklaşınca gaz olur; sıvıdan gaza geçiş buharlaşmadır", "Tanecikleri uzaklaştıran değişim ısı alır"],
 "Buharlaşma; ısı alınır.",
 "Düzensiz ama yakın dizilimi gaza, çok uzak dağınık dizilimi katıya yormak. Kontrol: önce taneciklerin aralığına ve düzenine bak.",
 "Düzenli katı, yakın sıvı, uzak gaz.")

kart("kim-periyodik-sistem-02", "kim|Periyodik Sistem", "Periyodik özelliklerin değişimi",
 "Atom yarıçapı, elektronegatiflik ve metalik karakterin periyotta ve grupta nasıl değiştiğini kullanabilmeni.",
 "Periyotta soldan sağa çekirdek yükü artar: **yarıçap azalır, elektronegatiflik artar**, metalik karakter azalır. Grupta yukarıdan aşağı katman sayısı artar: yarıçap artar, iyonlaşma enerjisi ve elektronegatiflik azalır. Grafikteki değer karşılaştırmalarını grafikten yap.",
 "Periyotta → : r ↓ EN ↑ · Grupta ↓ : r ↑ EN ↓", SEKIL_PER,
 "Aynı periyotta X (1A), Y (5A) ve Z (7A) elementleri bulunuyor. Atom yarıçapı ve elektronegatiflik sıralamasını yaz.",
 ["Aynı periyotta soldan sağa sıra X, Y, Z'dir", "Yarıçap azalır: X > Y > Z", "Elektronegatiflik artar: Z > Y > X"],
 "Yarıçap X > Y > Z; elektronegatiflik Z > Y > X",
 "Elektronegatifliği elektron verme eğilimi sanmak. Kontrol: elektronegatiflik bağ elektronunu çekme eğilimidir; ametalde yüksek, metalde düşüktür; arttıkça metalik karakter azalır.",
 "Sağa ve yukarı çıktıkça elektronegatiflik artar.")

kart("kim-periyodik-sistem-04", "kim|Periyodik Sistem", "Element sınıfları ve grup adları",
 "Periyodik sistemdeki konumdan elementin metal, yarı metal ya da ametal olduğunu ve özelliklerini bulabilmeni.",
 "**A grubu numarası değerlik elektron sayısını verir.** 1A ve 2A (H hariç) metaldir; 6A ve 7A ametaldir; 8A soy gazdır. Metaller parlak, işlenebilir ve iyi iletkendir. Ametaller genellikle kırılgan ve kötü iletkendir. Yarı metaller bu ikisinin arasındadır.",
 "Grup numarası = değerlik elektron sayısı", None,
 "Elektron dizilimi 2, 8, 6 olan elementin periyodu, grubu ve sınıfı nedir?",
 ["Üç katman dolu: 3. periyot", "Son katmanda 6 elektron: 6A grubu", "6A grubu ametaldir"],
 "3. periyot, 6A, ametal",
 "Elementin sınıfını görünüşüne bakarak seçmek. Kontrol: önce tablodaki konumuna bak; parlaklık, işlenebilirlik ve iletkenlik yalnız metal bölgesindeki elementlerde beklenir.",
 "Önce konuma bak, sonra sınıfı söyle.")

# ---------- doğrulama ----------
girdi = re.findall(r'^### (\S+) \|', open('/tmp/kor/kart/parti/p09.txt', encoding='utf-8').read(), re.M)
assert [x["id"] for x in K] == girdi, "id uyuşmuyor"

def kel(s): return len(s.replace('**', '').split())
ZOR = ["id", "k", "baslik", "olcer", "kural", "ornek", "hata", "akilda"]
n_sekil = 0
for x in K:
    if x.get("kapsamDisi") or x.get("birlesti"): continue
    for z in ZOR: assert x[z], (x["id"], z)
    assert "formul" in x and "sekil" in x
    assert kel(x["baslik"]) <= 6, x["id"]
    assert kel(x["olcer"]) <= 25 and not x["olcer"].startswith("Bu soru"), x["id"]
    assert kel(x["kural"]) <= 60 and 1 <= x["kural"].count("**") // 2 <= 2, (x["id"], kel(x["kural"]))
    assert kel(x["hata"]) <= 40, (x["id"], kel(x["hata"]))
    assert kel(x["akilda"]) <= 8 and '"' not in x["akilda"] and '“' not in x["akilda"], x["id"]
    o = x["ornek"]
    assert o["soru"] and o["cevap"] and 2 <= len(o["adimlar"]) <= 4, x["id"]
    if x["sekil"]:
        n_sekil += 1
        assert len(x["sekil"].encode()) <= 25000
        for fs in re.findall(r'font-size="(\d+)"', x["sekil"]): assert int(fs) >= 11
print("kart:", sum(1 for x in K if "baslik" in x), "sekilli:", n_sekil)
json.dump(K, open('/home/claude/zekacademy-app/havuz/tekrar/kart-p09.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for x in K:
    if x.get("sekil"):
        open(f'/tmp/kor/kart/p09/{x["id"]}.svg', 'w', encoding='utf-8').write(
            re.sub(r'var\(--([a-z-]+)\)', lambda m: {'ink': '#18212f', 'muted': '#5b6678', 'brand': '#2f5bea', 'brand-soft': '#e7edff', 'rule': '#0f8a6a', 'rule-soft': '#e3f5ef', 'warn': '#c2410c', 'warn-soft': '#fff1e8'}[m.group(1)],
                   x["sekil"].replace('<svg ', '<svg xmlns="http://www.w3.org/2000/svg" ').replace('<text ', '<text fill="#18212f" ')))
