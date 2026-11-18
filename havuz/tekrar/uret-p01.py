import json, re, itertools

K = []
def kart(id, baslik, olcer, kural, formul, sekil, soru, adimlar, cevap, hata, akilda):
    K.append({"id": id, "k": "bio", "baslik": baslik, "olcer": olcer, "kural": kural,
              "formul": formul, "sekil": sekil,
              "ornek": {"soru": soru, "adimlar": adimlar, "cevap": cevap},
              "hata": hata, "akilda": akilda})

def box(x, y, w, h, fill, stroke="var(--muted)"):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>'
def txt(x, y, s, size=12, weight=400, anchor="middle"):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}">{s}</text>'
def svg(inner, label):
    return f'<svg viewBox="0 0 280 170" role="img" aria-label="{label}">{inner}</svg>'
def sym(parts):
    out = ""; prev = False
    for b, s in parts:
        out += (f'<tspan dy="5">{b}</tspan>' if prev else b)
        out += f'<tspan dy="-5" font-size="11">{s}</tspan>' if s else ""
        prev = bool(s)
    return out

# ---- 1
kart("bio-canlilarin-ortak-01", "Bilimsel yöntem ve deney değişkenleri",
 "Bir ifadeyi bilimsel yöntem basamağıyla eşleştirip deneyde değişkenleri ve kontrol grubunu ayırabildiğini.",
 "Sıra: **gözlem → problem → hipotez → kontrollü deney → veri yorumu → sonuç**. Hipotez, deneyle sınanabilen geçici tahmindir. Araştırmacının değiştirdiği etken **bağımsız**, ölçtüğü sonuç **bağımlı** değişkendir; diğer koşullar sabit tutulur. Denenen etkenin uygulanmadığı grup **kontrol grubudur**.",
 "Gözlem → Problem → Hipotez → Deney → Veri → Sonuç", None,
 "Bir öğrenci aynı cins fasulyeleri farklı miktarda ışık alan üç saksıya koyup iki hafta sonra boylarını ölçüyor. Bağımsız ve bağımlı değişken nedir?",
 ["Öğrencinin kendi değiştirdiği etken ışık miktarıdır: bağımsız değişken.",
  "Ölçtüğü sonuç fasulyenin boyudur: bağımlı değişken.",
  "Fasulye cinsi, su ve toprak her saksıda aynı tutulur: sabit değişkenler."],
 "Bağımsız: ışık miktarı. Bağımlı: bitki boyu.",
 "Nedeni tahmin eden cümleyi gözlem sanmak. Gözlem yalnız görüleni yazar; **neden** söylüyorsa hipotezdir. Deney yapılmadıysa sonuç da yazılamaz.",
 "Gözlem görür, hipotez tahmin eder")

# ---- 2
kart("bio-canlilarin-ortak-03", "Homeostazi, tepki ve adaptasyon",
 "İç dengenin korunmasını, uyarana tepkiyi ve adaptasyonu ayırt edip değişim grafiğini yorumlayabildiğini.",
 "**Homeostazi**, iç ortamın uygun sınırlar içinde tutulmasıdır; değer değişse de yeniden uygun düzeye döner. **Tepki**, bir uyarana verilen anlık karşılıktır. **Adaptasyon**, popülasyonun uzun sürede kazandığı kalıtsal uyumdur. Grafikte değeri düzelten ve sınıra geri döndüren olay homeostazidir.",
 "Homeostazi: değer değişir → düzeltilir → denge korunur", None,
 "Yemekten sonra kan şekeri 90'dan 140'a çıkıyor, birkaç saat içinde yeniden 95'e iniyor. Bu olay hangi kavramı örnekler?",
 ["Değer önce yükseldi: iç ortam dengeden uzaklaştı.",
  "Sonra uygun düzeye geri döndü: düzeltme var.",
  "Olay kısa sürede bireyde oldu, kalıtsal değişim yok: adaptasyon değil."],
 "Homeostazi (kan şekeri dengesi).",
 "Grafikte tek noktaya bakıp 'sürekli arttı' gibi yorumlamak. Yorumdan önce **bütün değerleri sırayla oku**. Kalıtsal olmayan kısa süreli değişimi adaptasyon sanma.",
 "Değişir, düzelir; denge budur")

# ---- 3
n = 100 // 20; assert n == 5 and 50 * 2 ** n == 1600
kart("bio-canlilarin-siniflandirilmasi-01", "Bakteri büyümesi ve antibiyotik deneyi",
 "Grafik ve deney sonuçlarından bakteri sayısını, antibiyotik etkisini ve birlikte yaşamın sonucunu yorumlayabildiğini.",
 "Bakteriler **ikiye bölünerek** çoğalır; her bölünme süresinde sayı **2 katına** çıkar. Önce bölünme süresini bul, toplam süreyi ona böl: n bölünme olursa sayı **2ⁿ** kat artar. Antibiyotik bakterinin üremesini durdurur; dirençli bakteri etkilenmez. Birlikte yaşamda iki canlı da fayda görebilir.",
 "Son sayı = ilk sayı × 2ⁿ,  n = süre ÷ bölünme süresi", None,
 "Bölünme süresi 20 dakika olan 50 bakteri, 100 dakika sonra kaç olur?",
 ["Bölünme sayısı: 100 ÷ 20 = 5.", "Sayı 2⁵ = 32 katına çıkar.", "50 × 32 = 1600."],
 "1600 bakteri.",
 "Bölünme sayılarını birbirine bölmek ya da çıkarıp sayı oranı sanmak. Sayı oranı **2'nin kuvvetidir**: bölünme sayısı farkı kuvvet olarak yazılır.",
 "Bölünme sayısı kuvvet olur")

# ---- 4
sv = ""
names = ["Tür", "Cins", "Familya", "Takım", "Sınıf", "Şube", "Âlem"]
for i, nm in enumerate(names):
    w = 70 + 30 * i; x = 140 - w / 2; y = 4 + 23 * i
    sv += box(x, y, w, 21, "var(--rule-soft)" if i < 2 else "var(--brand-soft)") + txt(140, y + 15, nm, 12, 600)
kart("bio-canlilarin-siniflandirilmasi-03", "İkili adlandırma ve sınıflandırma basamakları",
 "Basamakları küçükten büyüğe sıralayıp bilimsel addan cins ve tür ilişkisini okuyabildiğini.",
 "Küçükten büyüğe: **tür → cins → familya → takım → sınıf → şube → âlem**. Tür en küçük, âlem en büyük basamaktır; küçük basamakta benzerlik fazladır. Bilimsel ad **cins + tür** adıdır: cins büyük, tür küçük harfle başlar. Cins adı aynıysa canlılar aynı cinstendir.",
 "Tür → Cins → Familya → Takım → Sınıf → Şube → Âlem",
 svg(sv, "Sınıflandırma basamakları: üstte en küçük tür, altta en büyük âlem"),
 "Panthera leo (aslan) ile Panthera tigris (kaplan) aynı cinste mi, aynı türde mi?",
 ["İlk sözcük cins adıdır: ikisinde de Panthera.", "İkinci sözcük tür adıdır: leo ile tigris farklı.", "Cins aynı, tür farklı."],
 "Aynı cinse, farklı türe aittirler.",
 "Basamak sırasını karıştırmak: cinsi familyadan büyük, şubeyi sınıftan küçük sanmak. **Tür en küçük, âlem en büyük** diye başlayıp aradakileri sırayla say.",
 "Tür en küçük, âlem en büyük")

# ---- 5
kart("bio-canlilarin-siniflandirilmasi-05", "Âlemler ve virüsler",
 "Hücre tipi, beslenme ve hücre duvarı özelliğinden canlının âlemini belirleyebildiğini.",
 "**Bakteri**: prokaryot. **Protista**: ökaryot, çoğu tek hücreli. **Mantar**: ökaryot, heterotrof, duvarı **kitin**. **Bitki**: ökaryot, ototrof, duvarı **selüloz**. **Hayvan**: ökaryot, heterotrof, hücre duvarı yok. **Virüsler** hücresel değildir; protein kılıf ve nükleik asitten oluşur.",
 "Hücre tipi → beslenme → hücre duvarı → âlem", None,
 "Ökaryot, heterotrof, hücre duvarı kitinli, tek hücreli bir canlı hangi âlemdedir?",
 ["Ökaryot olduğu için bakteri değildir.", "Heterotrof olduğu için bitki değildir.", "Kitinli duvar mantarlara özgüdür."],
 "Mantarlar âlemi.",
 "Kitinli duvarı bakterilere vermek ya da duvarsız canlıyı protista sanmak. Duvarsız ve heterotrofsa önce **hayvanı** düşün. Virüsün hücresi olmadığını unutma.",
 "Önce hücre tipi, sonra beslenme, sonra duvar")

# ---- 6
A = 60; tot = 200; GC = (tot - 2 * A) // 2
bag = A * 2 + GC * 3
assert GC == 40 and bag == 240
kart("bio-canlilarin-temel-02", "DNA'da baz ve hidrojen bağı",
 "Baz yüzdesi ya da sayısından eşleşen baz çiftlerini bulup toplam hidrojen bağını hesaplayabildiğini.",
 "Çift zincirli DNA'da **A = T** ve **G = C** olur. A–T çifti **2**, G–C çifti **3** hidrojen bağı yapar. Nükleotit; fosfat, pentoz şeker ve organik bazdan oluşur. DNA'da şeker deoksiriboz, RNA'da riboz; DNA'da T, RNA'da U bulunur.",
 "Bağ sayısı = (A–T çifti × 2) + (G–C çifti × 3)", None,
 "Çift zincirli bir DNA'da toplam 200 nükleotit var ve 60'ı adenindir. Kaç hidrojen bağı vardır?",
 ["A = T = 60 olduğundan 60 tane A–T çifti vardır.",
  "Kalan 200 − 120 = 80 nükleotit G ve C'dir: G = C = 40, yani 40 G–C çifti.",
  "Bağ: 60 × 2 + 40 × 3 = 240."],
 "240 hidrojen bağı.",
 "Bütün çiftleri 2 ya da 3 bağlı saymak. A ve T'yi ayrı ayrı çift sayıp ikiyle çarpmak da yanlıştır: **bir çift = bir A + bir T**. Önce çifti say.",
 "Önce çift say, sonra bağ say")

# ---- 7
e = 30 * 4 + 10 * 4 + 5 * 9
assert e == 205
kart("bio-canlilarin-temel-04", "Karbonhidrat, lipit ve besin enerjisi",
 "Karbonhidrat çeşitlerini ve görevlerini bilip besindeki organik maddelerden toplam enerjiyi hesaplayabildiğini.",
 "Glikoz, fruktoz **monosakkarit**; sükroz, maltoz **disakkarit**. **Nişasta** bitkide, **glikojen** hayvanda depo polisakkarittir; selüloz bitki hücre duvarını yapar. Karbonhidrat ve protein 1 g'da 4, yağ 9 kcal verir; su ve mineral enerji vermez. Lugol nişastayı, biüret proteini, Sudan III yağı gösterir.",
 "Enerji = 4 × karbonhidrat + 4 × protein + 9 × yağ", None,
 "Bir besinde 30 g karbonhidrat, 10 g protein, 5 g yağ ve 55 g su var. Toplam enerji kaç kcal?",
 ["Karbonhidrat: 30 × 4 = 120. Protein: 10 × 4 = 40.", "Yağ: 5 × 9 = 45.", "Su enerji vermez. Toplam: 120 + 40 + 45 = 205."],
 "205 kcal.",
 "Nişastayı hayvanda, glikojeni bitkide depo sanmak. Suyu enerji kaynağı saymak da sık hatadır: **su ve mineral enerji vermez**. Gramı kaç kcal verdiğini karıştırma.",
 "Nişasta bitkide, glikojen hayvanda")

# ---- 8
kart("bio-ekosistem-01", "Madde döngüleri ve enerji akışı",
 "Azot döngüsü basamaklarını bakterilerle eşleştirip enerjinin tek yönlü, maddenin döngüsel olduğunu bilebildiğini.",
 "**Azot bağlayıcı** bakteri N₂'yi amonyağa çevirir. **Nitrifikasyon** bakterisi amonyağı nitrata çevirir. **Denitrifikasyon** bakterisi nitratı yeniden N₂'ye çevirir. Enerji besin zincirinde **tek yönlü** akar; madde canlılar ile cansız çevre arasında **döngüsel** dolaşır.",
 "N₂ → amonyak → nitrat → N₂", None,
 "Baklagil köklerindeki bakteriler havadaki N₂'yi amonyağa çeviriyor. Bu bakteriler hangi gruptandır, bundan sonraki basamak nedir?",
 ["N₂'nin amonyağa çevrilmesi azot bağlamadır: azot bağlayıcı bakteriler.", "Sonraki basamak amonyağın nitrata çevrilmesidir.", "Bunu nitrifikasyon bakterileri yapar."],
 "Azot bağlayıcı bakteriler; sonra nitrifikasyon.",
 "Nitrifikasyon ile denitrifikasyonu karıştırmak ya da basamakları ters yazmak. **De-** öneki geri almadır: nitrat yeniden N₂ olur. Basamağı fotosentez sanma.",
 "Bağla, nitrata çevir, gaza döndür")

# ---- 9
en = 8000; zin = [en]
for _ in range(3): zin.append(zin[-1] / 10)
assert zin[-1] == 8
lv = [("Üst etçil", "1 kJ"), ("Etçil", "10 kJ"), ("Otçul", "100 kJ"), ("Üretici", "1000 kJ")]
sv = ""
for i, (nm, v) in enumerate(lv):
    w = 100 + 50 * i; x = 140 - w / 2; y = 6 + 34 * i
    sv += box(x, y, w, 30, "var(--rule-soft)" if i == 3 else "var(--brand-soft)") + txt(140, y + 20, f"{nm} {v}", 12, 600)
sv += txt(140, 164, "Her basamakta enerjinin %10'u geçer", 11)
kart("bio-ekosistem-03", "Besin ağı ve %10 kuralı",
 "Besin ağındaki zincirleri sayıp basamaklar arasındaki enerji miktarını %10 kuralıyla hesaplayabildiğini.",
 "Zincir **üreticiyle** başlar, hiçbir canlı tarafından yenmeyen canlıyla biter. Besin ağı zincirlerin birleşimidir; zincir sayısını üreticiden başlayıp **tüm yolları** sayarak bul. Her basamakta enerjinin yaklaşık **%10'u** üst basamağa geçer, kalanı ısı olarak kaybolur.",
 "Üst basamağın enerjisi = alt basamağın enerjisi ÷ 10",
 svg(sv, "Enerji piramidi: üretici 1000, otçul 100, etçil 10, üst etçil 1 kilojul"),
 "Üretici 8000 kJ ise üretici → otçul → birincil etçil → ikincil etçil zincirinde ikincil etçile kaç kJ ulaşır?",
 ["Otçul: 8000 ÷ 10 = 800.", "Birincil etçil: 800 ÷ 10 = 80.", "İkincil etçil: 80 ÷ 10 = 8."],
 "8 kJ.",
 "Aktarım sayısını yanlış saymak: dört basamaklı zincirde **üç** aktarım vardır. Birini atlayınca ya da fazla yapınca sonuç kayar. Önce basamakları numaralandır.",
 "Enerji her basamakta ona bölünür")

# ---- 10
kart("bio-ekosistem-05", "Biyotik ve abiyotik faktörler",
 "Bir ekosistemdeki etmenlerin canlı mı cansız mı olduğunu ve canlı bileşenlerin görevini ayırt edebildiğini.",
 "**Abiyotik** etmenler cansızdır: ışık, sıcaklık, su, rüzgâr, toprak yapısı, pH. **Biyotik** etmenler canlıdır: üretici, tüketici, ayrıştırıcı, parazit, rakip. Üreticiler organik madde üretir, tüketiciler besini hazır alır, ayrıştırıcılar ölüleri inorganik maddeye dönüştürür.",
 "Cansız etmen = abiyotik · Canlı etmen = biyotik", None,
 "Bir gölde su sıcaklığı, alg, pH, balık ve rüzgâr var. Hangileri abiyotiktir?",
 ["Canlı olanları ayır: alg ve balık biyotiktir.", "Kalanlar cansızdır: sıcaklık, pH, rüzgâr."],
 "Sıcaklık, pH ve rüzgâr.",
 "Işık şiddetini ya da rüzgârı canlı etmen sanmak. Canlıyı etkilese de etmenin kendisi cansızsa abiyotiktir. Her etmene sor: **kendisi canlı mı?**",
 "Cansız etmen abiyotiktir")

# ---- 11
kart("bio-hucre-ve-02", "Prokaryot-ökaryot ve organeller",
 "Prokaryot ile ökaryot hücreyi ayırıp organel bolluğundan hücrenin işlevini çıkarabildiğini.",
 "**Prokaryotta** (bakteri) çekirdek zarı ve zarlı organel yoktur; DNA sitoplazmadadır, tek organel **ribozomdur**. Ökaryotta çekirdek ve zarlı organeller vardır. Bol organel işi gösterir: **mitokondri** enerji, **Golgi** salgı, **lizozom** sindirim, **kloroplast** fotosentez.",
 "Prokaryot: zarlı organel yok, ribozom var", None,
 "Bir hücrede çekirdek zarı yok, DNA sitoplazmada ve yalnız ribozom görülüyor. Bu hücrede mitokondri bulunur mu?",
 ["Çekirdek zarı yok: prokaryot hücre.", "Prokaryotta tek organel ribozomdur.", "Mitokondri zarlı organeldir, bulunmaz."],
 "Hayır, bulunmaz.",
 "Bakteriyi ökaryot gibi düşünüp zarlı organel aramak. Organel zarlıysa prokaryotta yoktur. Çok enerji harcayan hücrede **mitokondrinin** bol olacağını da unutma.",
 "Prokaryotta yalnız ribozom vardır")

# ---- 12
assert 10 < 20
sv = (box(40, 30, 200, 120, "none") + box(41, 70, 99, 79, "var(--brand-soft)", "none") + box(140, 70, 99, 79, "var(--rule-soft)", "none")
      + '<line x1="140" y1="30" x2="140" y2="150" stroke="var(--brand)" stroke-width="2" stroke-dasharray="5 4"/>'
      + txt(140, 22, "yarı geçirgen zar", 11)
      + txt(90, 118, "%10", 14, 600) + txt(90, 136, "şeker", 12)
      + txt(190, 118, "%20", 14, 600) + txt(190, 136, "şeker", 12)
      + '<line x1="100" y1="56" x2="176" y2="56" stroke="var(--brand)" stroke-width="2.5"/>'
      + '<polygon points="176,50 188,56 176,62" fill="var(--brand)"/>' + txt(118, 48, "su", 12, 600))
kart("bio-hucre-ve-04", "Ozmoz ve hücrenin su dengesi",
 "Suyun yarı geçirgen zardan hangi yöne geçtiğini bulup ozmozu difüzyondan ayırabildiğini.",
 "**Ozmoz**, suyun yarı geçirgen zardan geçişidir; su, çözünen derişimi **düşük** taraftan **yüksek** tarafa gider. Hipotonik ortamda hayvan hücresi su alıp şişer, hipertonik ortamda su verip büzüşür. **Difüzyon**, taneciklerin derişimi çok yerden az yere yayılmasıdır; zar gerekmez.",
 "Su: seyreltik taraf → derişik taraf",
 svg(sv, "Yarı geçirgen zarla ayrılmış U borusu: solda yüzde 10, sağda yüzde 20 şeker, su sağa geçiyor"),
 "Yarı geçirgen zarla ayrılmış U borusunun sol kolunda %10, sağ kolunda %20 şeker çözeltisi var. Su hangi yöne geçer?",
 ["Çözünen derişimi sağ kolda daha yüksek.", "Su, derişimi düşük taraftan yüksek tarafa geçer."],
 "Sol koldan sağ kola.",
 "Suyun değil çözünenin hareket ettiğini sanmak ya da tuzlu ortamda hücreye su girdiğini düşünmek. Ortam hücreye göre **derişikse** su hücreden çıkar; hücre büzülür.",
 "Su derişik tarafa doğru gider")

# ---- 13 (3 soru; aynı kural bolunme-05'te)
BIRLESTI = {"id": "bio-hucrede-bolunme-01", "birlesti": "bio-hucrede-bolunme-05"}

# ---- 14
G1, S, G2, M = 6, 8, 4, 2
assert G1 + S + G2 == 18 and G1 + S + G2 + M == 20
sv = ""
seg = [("G1", 20, 80, "var(--brand-soft)"), ("S", 80, 145, "var(--rule-soft)"), ("G2", 145, 205, "var(--brand-soft)"), ("M", 205, 260, "var(--warn-soft)")]
for nm, a, b, f in seg:
    sv += box(a, 70, b - a, 34, f) + txt((a + b) / 2, 92, nm, 13, 600)
sv += ('<line x1="20" y1="60" x2="205" y2="60" stroke="var(--muted)" stroke-width="1.5"/>' + txt(112, 52, "İnterfaz", 12, 600)
       + '<line x1="205" y1="60" x2="260" y2="60" stroke="var(--warn)" stroke-width="1.5"/>' + txt(232, 52, "Bölünme", 12, 600)
       + txt(50, 124, "büyür") + txt(112, 124, "DNA", 12, 600) + txt(112, 139, "eşlenir", 12, 600)
       + txt(175, 124, "hazırlık") + txt(232, 124, "bölünür"))
kart("bio-hucrede-bolunme-03", "Hücre döngüsü ve mitoz evreleri",
 "Döngünün evrelerini ve her evrede olanları ilişkilendirip mitozun evrelerini kromozom görünümüne göre sıralayabildiğini.",
 "Döngü **interfaz** (G1 → S → G2) ve **mitoz** (M) evrelerinden oluşur. G1'de hücre büyür, **S'de DNA eşlenir**, G2'de mitoza hazırlanır. Mitoz: profaz, metafaz, anafaz, telofaz. Kardeş kromatitler **anafazda** ayrılır; sitokinezle sitoplazma ikiye bölünür.",
 "G1 → S → G2 → Mitoz (P–M–A–T) → Sitokinez",
 svg(sv, "Hücre döngüsü: G1, S ve G2 interfazı, M evresi bölünmeyi oluşturur"),
 "Bir hücre döngüsünde G1 = 6, S = 8, G2 = 4, M = 2 saat sürüyor. İnterfaz kaç saattir, DNA hangi evrede eşlenir?",
 ["İnterfaz G1 + S + G2'dir: 6 + 8 + 4 = 18 saat.", "DNA eşlenmesi her zaman S evresindedir.", "M evresi bölünmedir, interfaza katılmaz."],
 "18 saat; DNA S evresinde eşlenir.",
 "G1, S ve G2'yi bölünmenin parçası saymak. Bölünme yalnız **M evresidir**; interfaz bölünme değildir. DNA eşlenmesini mitozun içinde aramak da yanlıştır.",
 "DNA hep S evresinde eşlenir")

# ---- 15
kart("bio-hucrede-bolunme-05", "Eşeysiz üreme türleri",
 "Canlıları eşeysiz üreme biçimleriyle eşleştirip yavruların ana canlıyla özdeş olduğunu yorumlayabildiğini.",
 "Eşeysiz üremede gametler birleşmez; yavrular **mitozla** oluşur ve ana canlıyla genetik olarak **özdeştir**. Türler: ikiye bölünme (amip), tomurcuklanma (hidra, maya), sporla üreme (eğrelti otu), rejenerasyon (planarya), **vejetatif üreme** (bitkide kök, gövde, yaprak parçası). Aşılama ve klonlama da eşeysizdir.",
 "Gamet birleşmez → mitoz → özdeş yavru", None,
 "Çilek bitkisinin yere uzanan gövdesinden yeni bir bitki oluşuyor. Bu hangi üreme türüdür, yavru ana bitkiye genetik olarak benzer mi?",
 ["Yeni birey gövde parçasından oluştu: vejetatif üreme.", "Gametler birleşmedi, hücreler mitozla çoğaldı.", "Mitoz kopya üretir: yavru genetik olarak özdeştir."],
 "Vejetatif üreme; genetik olarak özdeş.",
 "Bir eşleştirmeyi bilmeyip yanlış seçmek ve eşeysiz üremede **çeşitlilik** beklemek. Mitozla oluşan yavrular ana canlıyla aynıdır; aşıda kalemin genotipi anaçtan etkilenmez.",
 "Gamet yoksa eşeysiz, yavru özdeş")

# ---- 16
def cocuk(anne, baba):
    return [a + b for a in anne for b in baba]
kareler = [(a, b) for b in ["XR", "Y"] for a in ["XR", "Xr"]]
assert sum(1 for a, b in kareler if a == "Xr" and b == "Y") == 1 and len(kareler) == 4
P = lambda s: [("X", s[1:])] if s[0] == "X" else [("Y", "")]
def hucre(a, b):
    if b[0] == "X":
        return sym([("X", x) for x in sorted([a[1:], b[1:]], key=lambda t: t != "R")])
    return sym([("X", a[1:]), ("Y", "")])
sv = ""
for i, g in enumerate(["XR", "Xr"]):
    sv += f'<text x="{130 + 70 * i}" y="26" font-size="14" font-weight="600" text-anchor="middle" fill="var(--brand)">{sym(P(g))}</text>'
for j, g in enumerate(["XR", "Y"]):
    sv += f'<text x="76" y="{70 + 60 * j}" font-size="14" font-weight="600" text-anchor="middle" fill="var(--memo)">{sym(P(g))}</text>'
for (a, b) in kareler:
    i = ["XR", "Xr"].index(a); j = ["XR", "Y"].index(b)
    hasta = (a == "Xr" and b == "Y")
    sv += box(95 + 70 * i, 35 + 60 * j, 70, 60, "var(--warn-soft)" if hasta else "var(--rule-soft)")
    sv += f'<text x="{130 + 70 * i}" y="{70 + 60 * j}" font-size="15" font-weight="600" text-anchor="middle">{hucre(a, b)}</text>'
sv += txt(40, 40, "Anne", 11, 400, "middle").replace('x="40"', 'x="60"').replace('y="40"', 'y="22"') + txt(48, 112, "Baba", 11)
kart("bio-kalitim-02", "Eşeye bağlı kalıtım",
 "Eşeye bağlı çekinik özellikte cinsiyeti ve fenotipi birlikte düşünüp çocuğun olasılığını hesaplayabildiğini.",
 "Renk körlüğü ve hemofili **X kromozomundaki çekinik** alellerle taşınır. Kadın XX, erkek XY'dir. Erkekte tek X olduğundan çekinik alel **tek başına** etkili olur; kadında iki çekinik alel gerekir. Cinsiyet de olasılığa girer: soruda koşul yoksa kutuların **hepsi** sayılır.",
 "Taşıyıcı anne × sağlıklı baba → 4 kutudan 1'i renk körü erkek",
 svg(sv, "Taşıyıcı anne ile sağlıklı babanın Punnett karesi: XRXR, XRXr, XRY, XrY"),
 "Renk körlüğü alelini (r) taşıyan anne (XRXr) ile sağlıklı baba (XRY) çocuk sahibi oluyor. İlk çocuğun renk körü olma olasılığı kaçtır?",
 ["Anne gametleri XR, Xr; baba gametleri XR, Y.", "Kare: XRXR, XRXr, XRY, XrY.", "Renk körü yalnız XrY: dört kutudan biri."],
 "1/4.",
 "Olasılıkları toplamak ya da erkek olmayı soruda yokken koşul saymak. Koşul yoksa **kutuların hepsini** paydaya yaz; yalnız 'erkek çocuklar arasında' denirse payda küçülür.",
 "Cinsiyeti de kareye kat")

# ---- 17
kart("bio-kalitim-04", "Mutasyon, modifikasyon ve varyasyon",
 "Kalıtsal değişimi çevre etkisiyle oluşandan ayırıp mutasyonun ne zaman yavruya geçtiğini bilebildiğini.",
 "**Mutasyon**, genetik bilgide kalıcı değişikliktir. **Gamet** hücresinde olursa yavruya geçebilir; **vücut hücresindeki** mutasyon yavruya geçmez. **Modifikasyon**, çevrenin fenotipte yaptığı değişimdir; genotip aynıdır, kalıtsal değildir. Genetik çeşitlilik, bireyler arasında alel farkı demektir.",
 "Mutasyon: gen değişir · Modifikasyon: yalnız fenotip değişir", None,
 "Aynı genotipli iki bitkiden biri güneşte, diğeri gölgede büyüyor ve boyları farklı oluyor. Bu fark yavrulara geçer mi?",
 ["Genotip aynı, fark yalnız ortamdan: modifikasyon.", "Modifikasyon genleri değiştirmez.", "Gametlerin genotipi aynı kalır, fark yavruya geçmez."],
 "Geçmez; bu bir modifikasyondur.",
 "Vücut hücresindeki mutasyonun yavruya geçtiğini sanmak ya da çevreyle oluşan her değişimi mutasyon saymak. Önce hücrenin **gamet mi vücut hücresi mi** olduğuna, sonra genin değişip değişmediğine bak.",
 "Yavruya geçmesi için gamette olmalı")

# ---- 18
yavru = sorted(set(a + b for a in "Bb" for b in "bb"))
assert yavru == ["Bb", "bb"] and sum(1 for a in "Bb" for b in "bb" if a + b == "bb") == 2
kart("bio-kalitim-06", "Baskınlık ve test çaprazlaması",
 "Yavru oranlarına bakarak baskın fenotipli bireyin genotipini ve gamet çeşidini belirleyebildiğini.",
 "**Baskın** alel heterozigotta da görünür; çekinik alel yalnız **homozigotta** görünür. Baskın fenotipli bireyin genotipini bulmak için onu **çekinikle (aa)** çaprazla: yavruların hepsi baskınsa birey AA, **yarısı çekinikse Aa**'dır. Her heterozigot gen çifti 2 çeşit gamet verir.",
 "Aa × aa → 1 Aa : 1 aa · gamet çeşidi = 2ⁿ (n: heterozigot çift)", None,
 "Kahverengi tüy (B), siyaha (b) baskındır. Kahverengi bir tavşan siyahla çaprazlanıyor, 8 yavrunun 4'ü siyah çıkıyor. Tavşanın genotipi nedir?",
 ["Siyah yavru (bb) var: her ebeveyn yavruya b vermiştir.", "Kahverengi tavşan b taşıyorsa genotipi Bb'dir.", "Bb × bb → 1 Bb : 1 bb; 4 kahverengi, 4 siyah sonucuyla uyuşur."],
 "Bb (heterozigot).",
 "Yavrular arasında çıkan çekinik fenotipin anlamını görmemek. Çekinik yavru varsa baskın ebeveyn **heterozigottur**. Heterozigotun gamet çeşidini 1 saymak da sık hatadır: Aa 2 çeşit verir.",
 "Çekinik yavru çıkarsa ebeveyn Aa")

# ---- çıktı + doğrulama
out = []
ids = {}
for k in K:
    ids[k["id"]] = k
out = [ids.get(i) or (BIRLESTI if i == BIRLESTI["id"] else None) for i in
       [l.split("|")[0][4:].strip() for l in open("/tmp/kor/kart/parti/p01.txt", encoding="utf-8") if l.startswith("### ")]]
girdi = [l[4:].split("|")[0].strip() for l in open("/tmp/kor/kart/parti/p01.txt", encoding="utf-8") if l.startswith("### ")]
assert [o["id"] for o in out] == girdi and len(set(girdi)) == len(girdi)
W = lambda s: len(s.replace("**", "").split())
for o in out:
    if "birlesti" in o: continue
    for f in ["id", "k", "baslik", "olcer", "kural", "formul", "ornek", "hata", "akilda"]:
        assert o[f], (o["id"], f)
    assert W(o["baslik"]) <= 6, (o["id"], "baslik", W(o["baslik"]))
    assert W(o["olcer"]) <= 25 and not o["olcer"].startswith("Bu soru"), (o["id"], "olcer", W(o["olcer"]))
    assert W(o["kural"]) <= 60 and "**" in o["kural"], (o["id"], "kural", W(o["kural"]))
    assert W(o["hata"]) <= 40, (o["id"], "hata", W(o["hata"]))
    assert W(o["akilda"]) <= 8 and '"' not in o["akilda"], (o["id"], "akilda", W(o["akilda"]))
    assert 2 <= len(o["ornek"]["adimlar"]) <= 4 and o["ornek"]["soru"] and o["ornek"]["cevap"]
    assert "\n" not in o["formul"]
    if o["sekil"]: assert len(o["sekil"]) <= 25000
json.dump(out, open("/home/claude/zekacademy-app/havuz/tekrar/kart-p01.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
for o in out:
    if o.get("sekil"):
        open(f"/tmp/kor/kart/p01/{o['id']}.svg", "w", encoding="utf-8").write(o["sekil"])
print(len(out), "kayit;", sum(1 for o in out if o.get("sekil")), "sekilli")
