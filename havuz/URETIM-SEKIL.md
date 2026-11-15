# Şekilli soru üretim talimatı (hafif mod dahil bütün üreticiler için · koç kararı 15 Kasım 2026)

Koç kararı: **hafif mod üreticileri şekil çizmeyi bilir ve kullanır; şekil az kullanılmışsa artırılır.** Bu dosya `URETIM.md`, `URETIM-DERSLER.md` ve `arac/MAT-ORTAK.md` ile birlikte geçerlidir; şekil konusunda çelişki olursa BU dosya geçerlidir ("ŞEKİL KULLANMA" diyen eski talimatlar kalktı).

## Hedef oranlar (ÖSYM 2018–2026 profiline göre; `osym-harita.json` → `kalip_sikligi`)
Bir pakette şekilli + grafik + tablo sorularının payı en az:
| Alan | Hedef |
|---|---|
| Matematik: sayılar (temel kavramlar, basamak, bölünebilme, EBOB-EKOK, rasyonel) | %30 |
| Matematik: denklem, eşitsizlik, mutlak değer, oran-orantı, üslü-köklü, çarpanlara ayırma | %25 |
| Matematik: problemler (sayı, kesir, yaş, yüzde, kâr-zarar, karışım, işçi, hareket, rutin olmayan) | %30 |
| Kümeler, olasılık, mantık | %20 |
| Permütasyon-kombinasyon, fonksiyonlar | %40 |
| Veri ve istatistik, grafik problemleri | %70–100 |
| Geometri | %90–100 |
| Fizik | %50 |
| Kimya | %25 |
| Biyoloji | %25 |
| Coğrafya | %25 (harita gerektirenler internet açılınca) |
Şekil süs değildir: **çözüm için gereken veriyi taşır** (ÖSYM'de olduğu gibi). Metinle anlatılabilecek soruya zorla şekil ekleme; şeklin doğal olduğu kurguyu seç.

## Matematikte şeklin doğal olduğu kurgular (ÖSYM mantık aileleri)
- Sayı doğrusu ve eşit aralıklar; cetvel/gösterge/ölçek okuma; terazi ve tartı; saat ve takvim yaprağı.
- Kutulara / ızgaraya / piramide sayı yerleştirme; işlem makinesi ve akış şeması (ok ve kutular); sihirli kare; sayı çarkı.
- Kesir modelleri (bölünmüş dikdörtgen/daire, boyalı parçalar); kap ve sıvı seviyesi (karışım, depo); para/bozukluk dizilimi.
- Yol şeması (hareket: şehirler arası mesafe çizgisi, pist), zaman çizelgesi (yaş, işçi), fiyat etiketi/fiş/tarife tablosu (yüzde, kâr-zarar).
- Venn şeması (kümeler), ağaç şeması ve ızgara yolu (sayma, olasılık), çark/hedef tahtası/zar açınımı (olasılık), ok diyagramı ve koordinat düzleminde grafik (fonksiyon), doğruluk tablosu (mantık).
- Tablo: `tablo_svg`; sütun/çizgi/daire grafiği: `tyt-mat/uret-grafikiki.py` yardımcıları.

## Araçlar
- **`havuz/cizim.py` → `tikz_svg(govde)`**: TikZ gövdesi → tema uyumlu SVG (doğrudan `sekil` alanına). Paketler: `tikz`, `tkz-euclide` (geometri), `circuitikz` (devre; **`tikzpicture` içinde**: `\draw … to[R,l=$R_1$] …`), `tikz-3dplot`, `pgfplots`, `mhchem`. `chemfig` YOK. Renk: `vurgu` (yeşil); taralı alan `fill=vurgu!20`; sıvı `fill=vurgu!15`; zemin `pattern=north east lines`. Yazı serifsiz. Şekil genişliği ~5–9 cm (420 pt üstü reddedilir).
- `havuz/tyt-mat/_hafif_mat.py`: `tablo_svg(basliklar, satirlar)`; `mk(..., sekil=...)`.
- Betik başına: `sys.path`'e `havuz/` ekle → `from cizim import tikz_svg`.
- Örnek betikler (aynen bu düzeni izle): `tyt-geo/uret-geopilot.py` (geometri, 3B), `tyt-fiz/uret-fizpilot.py` (düzenek, devre, optik, grafik), `tyt-bio/uret-biopilot.py` (hücre, soyağacı, besin ağı, bölünme evreleri, pgfplots), `tyt-mat/uret-grafikiki.py`, `tyt-mat/uret-veri.py`.

## Çizim kuralları (denemelerden çıkan dersler)
1. **Tek veri kaynağı:** koordinatları ve sayıları Python'da hesapla; TikZ gövdesini f-string ile aynı değerlerden üret; cevap aynı hesaptan assert edilir. Elle koordinat uydurma.
2. **Ölçekli çiz:** uzunluk, açı, hacim, kesit verileri şekilde gerçek oranında. Düzeneklerde tek ölçek (1 cm = sabit birim).
3. **Metin–şekil tutarlılığı:** metindeki her veri şekilde de görünür (ya da metin "şekilde … verilmiştir" der); şekilde metinde olmayan veri bulunmaz; dik açı/eşitlik/paralellik işareti yalnız verilen bilgi için.
4. **Etiketler:** köşe harfleri dışarıda; uzunluk kenarın ortasında ve dış tarafında; açı değeri yayın içinde; birim etikette; hiçbir yazı çizgiyle ya da başka yazıyla kesişmez. Bilinmeyen "x" ya da "?"; "?" bir ızgara değerine/şıkka hizalı görünmesin.
5. **Şekil cevabı ele vermez:** sorulan yapı tek başına farklı renkte olmaz (ör. yalnız kloroplast yeşil); yapı adı şekilde yazmaz (numara I–V); sonuç değeri etiketlenmez.
6. **Üç boyut:** ön yüz gerçek oranında, derinlik ~yarı kısaltılmış eğik görünüm; görünmeyen kenarlar ve içten geçen doğrular kesikli; bir doğru başka köşenin üstüne düşüyorsa bakış açısını değiştir. Gizli kenarı hesapla (kendi izdüşümün), tahmin etme.
7. **Bilimsel doğruluk:** kuvvet yönleri, ölçü aleti bağlantısı (ampermetre seri, voltmetre paralel), ışın yolu (hesapla), ok yönü (besin ağında yenenden yiyene), kromozom/kromatit sayıları, organel yapıları (mitokondri: çift zar + krista; kloroplast: çift zar + grana).
8. **Metin içinde boru (|) işaretli tablo yasak**; tablo `tablo_svg` ile.
9. `kalip`: 'şekilli' (çizim), 'grafik', 'tablo'. Aynı pakette aynı şekil türünü ikiden fazla kullanma.

## Zorunlu görsel kontrol (üretici)
`python3 havuz/kalite.py <klasör>/<onek> <onek>` → `/tmp/kor/<id>.png`. Üretici **her** PNG'yi Read ile açar ve eleştirir (çakışma, taşma, ölçek, okunaklılık, bilimsel doğruluk, metinle çelişki); en az iki tur düzeltir; raporda baktığı PNG'leri yazar.

## Koordinatör akışı (şekilli paket)
üretim → koordinatör kontak sayfasına bakar → **kör çözücü** (PNG'yi açarak çözer) ‖ **içerik doğrulayıcı** ‖ **şekil eleştirmeni** (her PNG: etiket, ölçek, bilimsel doğruluk, ele verme) → düzeltme → değişen şekillere yeniden bakılır → bayrak → yerel commit.

## Henüz yapılamayanlar
İnternet kapalı olduğu için hazır görsel gerektirenler bekliyor: gerçek haritalar (Natural Earth verisi), organ/doku çizimleri (Servier Medical Art, Bioicons), tarihî görseller (Wikimedia Commons). Bunlar açılana kadar şematik çizimle yapılabilenler yapılır; yapılamayan soru tipi rapora yazılır.
