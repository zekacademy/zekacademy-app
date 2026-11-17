# Matematik çözüm kılavuzu (TYT, ikinci bölüm)

## Kümeler ve Kartezyen Çarpım

### Alt küme sayma — tanıma: "alt kümelerinden kaç tanesi … içerir / içermez / en az bir …"
- Yol: n elemanlı kümenin 2ⁿ alt kümesi vardır (∅ ve kendisi dahil). Durumu belli elemanlara "var/yok" de; kalan k serbest eleman 2ᵏ verir. "En az bir" → tümleyen: 2ⁿ − 2^(hiç içermeyen). Birbirine bağlı koşulda ("a varsa b de") durumları ayrı say, topla. "En az bir tek ve en az bir çift": (2ᵗ − 1)(2ᶜ − 1). 2ⁿ⁺³ − 2ⁿ = 2ⁿ(8 − 1).
- Tuzak: ∅'yi gereksiz çıkarmak; koşulu sağlamayanı vermek.

### Kartezyen çarpım — tanıma: A × B, sıralı ikili, ızgarada noktalar
- Yol: s(A × B) = s(A)·s(B); (A × B) ∩ (B × A) = (A ∩ B) × (A ∩ B) ⇒ s(A ∩ B)². s(A ∪ B) = s(A) + s(B) − s(A ∩ B); s(A \ B) = s(A) − s(A ∩ B). Çarpım ve birleşim/kesişim verilince s(A) + s(B) ile s(A)·s(B) bulunur. "En çok/en az": iki yerleşimi de dene. Izgarada önce istenen noktaları yaz, koşulları (x > y, toplam > 0) tek tek uygula.

### Küme işlemleri, tümleyen, kapsama, tanımlı işlem
- Yol: A ⊂ B ⇒ B′ ⊂ A′ (yön döner); A ∩ B′ = A \ B. s(A′) = s(E) − s(A); s((A ∪ B)′) = s(E) − s(A ∪ B). Birleşim/kesişim/fark verilince bölgeleri doldur. Tanımlı işlem ("yalnız birinde olanlar") bölgelere çevrilir; s(A ∪ B) = o + s(A ∩ B). Öncüllerde küçük örnek küme kur. Sayı doğrusunda dolu nokta dahil, boş hariç; eşitsizlikli kümede uçları (≤ dahil, < hariç) kontrol edip say.

### Venn problemleri — tanıma: "en az birine katılan / yalnız bir …", tablo, şema
- Yol: yalnız bölge = küme − kesişim; hiçbirinde olmayan = toplam − birleşim. Kesişim kesir/kat ile verilmişse kesişime x de, birleşim denklemini kur. Üç küme: x₁ + x₂ + x₃ = kişi, x₁ + 2x₂ + 3x₃ = kümelerin toplamı. Bir küme = onu içeren 4 bölge; 8 bölge toplamı evrensel küme. Tabloda yalnız bir gruba ait = üye toplamı − 2·ortak.
- Tuzak: kesişimi iki kez saymak; "hiçbiri"ni gruba katmak.

## Mantık

### Doğruluk değeri, tablo, p-q-r bulma, açık önerme
- Yol: ∧ yalnız (1,1) iken 1; ∨ yalnız (0,0) iken 0; ⇒ yalnız (1,0) iken 0; ⇔ eşitse 1. Değilli sütunu ayrı yaz, içten dışa hesapla. Bulma: doğru "ve" → hepsi 1; yanlış "veya" → hepsi 0; yanlış ⇒ → p = 1, q = 0; değilli ifadede önce olumsuzu aç. Açık önermede p ⇒ q'nun doğruluk kümesi = (p doğru, q yanlış) olanların tümleyeni.

### Denklik, De Morgan, totoloji, devre
- Yol: (p ∧ q)′ ≡ p′ ∨ q′; (p ∨ q)′ ≡ p′ ∧ q′; p ⇒ q ≡ q′ ⇒ p′ ≡ p′ ∨ q; (p ⇒ q)′ ≡ p ∧ q′; p ⇔ q ≡ (p ⇒ q) ∧ (q ⇒ p). Karşıt (q ⇒ p) ve ters (p′ ⇒ q′) denk değildir. Totoloji: tüm satırlar 1; çürütmek için tek 0 yeter. Devre: seri ∧, paralel ∨; ortak anahtarı dışarı al.
- Tuzak: koşullunun olumsuzunu koşullu yazmak; terimi değilleyip bağlacı değiştirmemek.

### Niceleyiciler
- Yol: (∀x P)′ ≡ ∃x P′; (∃x P)′ ≡ ∀x P′; ≥ → <, ≤ → >. "Her … dir"in olumsuzu "… olmayan en az bir … vardır". Bileşikte önce bağlacı De Morgan'la değiştir, sonra parçaları değille. "Olumsuzu doğru" = kendisi yanlış. ∀ için tek karşı örnek, ∃ için tek örnek yeter;
- Tuzak: niceleyiciyi ya da özelliği değillemeyi unutmak.

### Hikâyeli çıkarım — tanıma: "kesinlikle doğru olan"
- Yol: koşulluları p ⇒ q yaz. p ve p ⇒ q → q; q′ ve p ⇒ q → p′. q'dan p, p′'den q çıkmaz. "A veya B olursa C" ve C yok → ikisi de yok. Kesin bilgiden başla, zinciri yürüt, her öncülü ayrı sına.

## Mutlak Değer

### Açma ve denklemler
- Yol: |A| = A (A ≥ 0), −A (A < 0); içinin işaretini önce belirle. |A| = k (k > 0) ⇒ A = ±k; |A| = |B| ⇒ A = B ya da A = −B (eksi tüm parantezde). İki terimli toplamda içi sıfırlayan noktalarla bölgelere ayır, her kökü bölgede doğrula. |x − a| + |x − b| = |a − b| ise çözüm a ile b arası (uçlar dahil, tam sayı fark + 1). Üç terimli toplam ortancada en küçüktür.
- Tuzak: tek durum çözmek; toplam/çarpım karışması.

### Eşitsizlik, uzaklık, tolerans
- Yol: |x − a| < r ⇒ a − r < x < a + r; |x − a| > r ⇒ x < a − r ya da x > a + r. a < |ifade| ≤ b iki ayrı aralık verir. |x − a| < |x − b| ⇒ x orta noktanın a tarafında (orta nokta hariç). "m ± d" ⇒ |x − m| ≤ d; aralığı yazma: merkez (m + M)/2, yarıçap (M − m)/2. "A'ya uzaklığı r olan" iki nokta. "En az r uzaklık" iki yönlüdür, başka koşul bir yönü eler.

### Grafik, kat/yol
- Yol: y = |x − a| + b tepe (a, b), kolları 1 eğimli V; tepeden h yukarıda taban 2h. Yolculuklarda her farkın mutlak değerini ayrı al, topla.

## Olasılık

### Temel, kombinasyonlu, art arda, bağımsız
- Yol: P = uygun / tüm (eşit şanslı). İki zar: 36 sıralı ikili. n para: 2ⁿ; tam k tura C(n,k)/2ⁿ. "A ya da B": a + b − ortak. Aynı anda/geri konmadan: pay ve payda sırasız C. Art arda geri konmadan: her adım payda 1 azalır, çarp; renk sıraları ayrı yol, topla. Geri konarak/bağımsızda olasılıklar sabit çarpılır. Ağaçta dal boyunca çarp, aynı sonucu verenleri topla. "En az bir" = 1 − hiç; "en az iki" = tam iki + üçü.
- Kontrol: sonuç 0–1 arasında, tüm durumların toplamı 1.

### Geometrik olasılık, sayı bulma
- Yol: ölçü oranı: çarkta merkez açı/360; halka/dairede alan (yarıçapın karesi). C(r,2)/C(n,2) verilmişse r(r−1) = … çöz, sonra istenen renge geç.
- Tuzak: yarıçap oranını olasılık sanmak.

## Oran Orantı

### Doğru–ters orantı, bileşik orantı, hız, dişli, ölçek
- Yol: doğru orantıda oran/birim değer sabit; ters orantıda çarpım sabit. İşçi × gün × saat = iş (işçi–saat); iş sırasında değişim varsa yapılanı çıkar. Yol = hız × süre; gidiş-dönüş ortalama hız = toplam yol / toplam süre. Dişli/kasnak: diş (çap) × tur sabit; aynı milde aynı tur. Ölçek: harita × payda = gerçek (cm); 1 km = 100 000 cm. Kur: önce TL'ye, sonra hedefe böl. Tarif: her malzemenin yeteceği kişiyi bul, en küçüğü al.

### Paylaştırma, oran kurma, ortalama
- Yol: a, b, c ile doğru orantılı pay ak, bk, ck; ters orantılı 1/a, 1/b, 1/c ile doğru (paydaları eşitle). Hem doğru hem ters etkide pay ∝ doğru/ters. a/m = b/n = c/p = k ⇒ a = mk…; a/b = c/d = k ise (ma + nc)/(mb + nd) = k. Ortak terimi eşitleyip oranları birleştir. Ekleme/çıkarmada iki durumu k ile yaz. Ortalama: toplam = ortalama × adet; eklenen/çıkan = toplamlar farkı; (a − b)² = (a + b)² − 4ab.
- Tuzak: verilen farkı toplam sanmak; k'yi bulup durmak.

## Permütasyon ve Kombinasyon

### Çarpma/toplama ilkesi, sayı yazma
- Yol: ardışık aşamalar çarpılır, birbirinin yerine seçilenler toplanır; alternatifleri önce kendi içinde topla. İsteğe bağlı seçimde "almamak" +1. Sayı yazmada en kısıtlı basamaktan başla; baş 0 olmaz; çiftte birler 0 ayrı durum.
- Tuzak: 0'ı başa koymak; birler 0 durumunu atlamak.

### Sıralama, masa, boyama
- Yol: n!; yan yana olacaklar blok (içi ayrı çarpılır); "yan yana olmasın" = tüm − yan yana; iki yasakta tümü − ihlal₁ − ihlal₂ + ikisi. Tekrarlı: n!/(a!·b!). Uçlara oturanların yer değiştirmesi (2!) çarpılır. Boyama: çok komşulu bölgeden başla; halkada ilk-son komşudur (k renk, n halka: (k−1)ⁿ + (−1)ⁿ(k−1)).
- Tuzak: blok içi sırayı unutmak; özdeş harfleri farklı saymak.

### Seçme, eşleştirme, yol sayma
- Yol: sırasız C(n,r); görev farkı varsa sıralı. "En az bir" tümleyenle. Herkes herkesle birer kez C(n,2); yönlü (mektup) n(n−1); toplamdan n'yi çöz. Doğrusal 3 nokta üçgen vermez: C(n,3) − C(d,3). Eşleştirme (2n kişi): (2n−1)(2n−3)…1. Izgara en kısa yol C(a+b, a); ara noktadan geçen = parçaları çarp; geçmeyen = tüm − geçen; kavşak kavşak toplamla kontrol et.
- Tuzak: kapalı yolu saymamak; iki parçayı toplamak.

## Rasyonel Sayılar

### Karşılaştırma, doğru, işlem, koşul
- Yol: ortak payda ya da ondalık. "Arasında kaç tam sayı": uçları ondalıkla yaz, negatif ve 0 dahil. Eşit aralık = fark ÷ parça (n nokta n−1 parça); parçalı doğruda aralıkların parçası ayrı, başlangıcı ekle. Toplama: payda eşitle, yalnız pay işle; bölme = ters çarpma; iç içe kesirde en içten çık; denklemde dıştakini tersle. Tam sayı koşulu: (an+b)/(n+c) = a + k/(n+c), payda k'nın böleni, negatifler de; doğal sayıda 0 dahil.

### Devirli ondalık
- Yol: 0,(a) = a/9; 0,(ab) = ab/99; 0,a(b) = (ab − a)/90; sadeleştir. ab ± ba = 11(a + b) / 9(a − b).
- Tuzak: devretmeyen rakamı çıkarmamak; sonlu ondalık gibi toplamak.

### Ölçü, gösterge, model
- Yol: bölme değeri = etiket farkı ÷ aralık sayısı (çizgi değil aralık). Gösterge: kesir × kapasite; miktar korunur (başlangıç + eklenen = harcanan + kalan). "Kaç katı" çarpma; kaç saksı/kişi bölme. Parçanın parçası çarpılır. Bindirmede örtüşme bir kez sayılır. İki doluluk farkı = eklenen miktarın bütüne oranı.

## Rutin Olmayan Problemler

### Tarife, tablo, takvim, periyot
- Yol: tarifeyi dilimlere ayır; "saatin bir kısmı" yukarı yuvarlar. Seçenekleri tek tek hesapla (sabit ücreti en düşük en ucuz olmayabilir). Tablo yargısında "katı" için önce çarp. Takvimde aynı gün 7 gün arayla. Periyotta kalanla çalış, yinelenmeyen başı ayır. Ortak an EKOK; "yalnız biri" = her sayımdan ortağı çıkar. Bölen sayısı tek ⇔ tam kare (lamba/anahtar).

### Sayma, yol, kesim, örüntü
- Yol: sabit artışta n. terim = ilk + (n−1)·artış; ortak kenarı düş. Kesim: 1 + d + (kâğıt içindeki kesişimler). Kapalı yollu ızgarada tümü − kapalıdan geçen ya da kavşak toplamı. Çemberde eleme: çıkandan sonra sayım yeniden başlar, kalanları listele. Komşuya aktarmada komşu çiftlerden geçen top sayılarını topla.

### Oyun, optimizasyon, şifre, mantık, tanımlı işlem
- Yol: oyunda küçük sayılardan kaybettiren/kazandıran konumları sırayla işaretle; rakibe kaybettiren bırakırsan kazanırsın. En az hamle/süre: tüm stratejileri dene (büyük birimle başlamak her zaman en azı vermez; köprüde yavaşları birlikte geçir). Şifre ipucunda rakamın varlığını/yerini sırayla ele, sonda tüm satırları doğrula; alfabe 29 harf. Puan 5d − 2y = P: tüm tam sayı çözümleri yaz, sınırla ele. Üç bilinmeyen–iki denklem: parametre seç. "Kesinlikle" için bütün dizilişlerde doğrula; doğrucu–yalancıda varsay, çelişirse tersine dön. Tanımlı işlem: parantez önce; özelliği tek örnekle çürüt, cebirle kanıtla.

## Sayı Problemleri

### Denklem kurma (sözel, adet–değer, fiş, terazi, zincir)
- Yol: "fazlası" +, "eksiği" −, "katı" ×; işlem sırasını bozma. İki tür nesne: adet toplamı + değer toplamı; "hepsi ucuz olsaydı": fark ÷ birim fark = diğer türün adedi. İki fiş/terazi: biri öbüründen çıkar ya da yerine koy; terazide ortak nesneleri at. Verilen para = ödenen + para üstü. Zincirde sondan başla, işlemleri tersle.
- Tuzak: ara değeri cevap sanmak.
- Kontrol: sonucu tüm koşullara geri koy.

### Ardışık sayı, sıra, dizilim
- Yol: ardışık tek sayıda terimde ortancayı al (toplam = adet × ortanca); n ardışık sayı: n·a + (0 + 1 + … + (n−1)). Baştan a., sondan b.: a + b − 1 kişi; arada n kişi ⇒ sıra farkı n + 1; sondan sıra = toplam − baştan + 1. Kat: zemin 0. kat, n. daire için tam kısım((n−1)/k). Düz yolda uçlar dahil öğe = aralık + 1; kapalı yolda öğe = aralık.
- Tuzak: ucu iki kez saymak.

### Eksik–fazla, planlı paylaşım, periyot, puan
- Yol: mal = a·n + artan = b·n − eksik; boş sıra/son kişi ayrı yazılır. Eksilen kişinin payı kalanlara bölünür. "Artanlar hep k eksik" ⇒ sayı + k ortak kat. Net: doğru·a − yanlış·b, boş etkisiz; "4 yanlış 1 doğruyu götürür" ⇒ net = doğru − yanlış/4.
- Tuzak: yanlışı puana eklemek.

### Alışveriş, kampanya, en az–en çok
- Yol: kampanyada tam grupları ucuz yerde al, artanı öbür yerde tamamla, karma seçenekleri dene ("3 al 1 hediye" = 4'te 3 ödenir). En çok ürün: zorunlu alımdan sonra artanı en ucuza ver. En büyüğü en çok: diğerleri en küçük farklı pozitif tam sayılar. Fiş: adet × birim, bilinenleri çıkar, kalanı adede böl.

## Temel Kavramlar

### Tek–çift, asal, ardışık, işaret
- Yol: tek + tek = çift; tek + çift = tek; çarpımda biri çiftse çift. Asal denklemde toplam tekse biri 2'dir, iki durumu da dene. Ardışıkta en küçüğe x de, tek/çift şartını kontrol et. İşaret: çarpım/bölüm pozitifse aynı işaret; çift kuvvet pozitif, tek kuvvet işareti korur; sıralama bilgisi hangisinin pozitif olduğunu söyler. "Kesinlikle"de tüm durumları dene.
- Tuzak: ara değeri (x) cevap sanmak; iki durumdan birini unutmak.

### Faktöriyel, basamak, rakam
- Yol: n! = n·(n−1)!; (n+1)! − n! = n·n!; küçük faktöriyeli ortak çarpan al. a! = k·b! ⇒ k = (b+1)…a (a = k, b = k − 1 de çözüm). AB = 10A + B; AB ± BA = 11(A + B) / 9(A − B); ABC − CBA = 99(A − C). Onlar +1 ⇒ sayı +10. En büyük/en küçükte baştan büyük/küçük rakam, baş 0 olamaz, çiftte birler çift.

### Doğru, gösterge, örüntü, döngü, işaret yerleştirme
- Yol: eşit aralık = fark ÷ aralık sayısı (aralık = çizgi − 1). Cetvel/gösterge: bölme değerini bul, uçları aynı birimde yaz. İleri-geri sıçrayış: s + t = toplam, 6s − 2t = yer değiştirme. Uçlar dahil n nesne n−1 aralık. Döngüde tam turu at, kalanla çalış; yinelenmeyen başlangıcı ayır; blok toplamı × tam blok + artan terimler. Makinede sondan tersle. Akış şemasında "en fazla" eşitliği içerir. İşaret yerleştirmede işlem önceliğiyle hedefi dene, ilk satırı doğrula. Sihirli karede dolu satırdan ortak toplamı bul.
- Tuzak: çizgi sayısıyla bölmek.

## Veri ve İstatistik

### Ortalama, ağırlıklı ortalama
- Yol: toplam = ortalama × adet; eklenen/çıkan = toplamlar farkı; eksik terim = ortalama × adet − bilinenler. Gruplu: (n₁m₁ + n₂m₂)/(n₁ + n₂); ortalamaların ortalaması alınmaz. Hedef ortalamada toplamı (ortalama × ağırlık toplamı) kur, bilinenleri çıkar, kalanı kendi ağırlığına böl.
- Tuzak: ağırlıkları ters eşleştirmek; farkı cevap sanmak.

### Ortanca, tepe değer, açıklık, çeyrek
- Yol: önce sırala; tek terimde ortadaki, çiftte ortadaki ikinin ortalaması. Tepe değer = en çok tekrar eden. Açıklık = en büyük − en küçük; bilinmeyen yeni en küçük ya da yeni en büyük olabilir (iki durum). Çeyrekler açıklığı Q₃ − Q₁: alt/üst yarının ortancaları (yöntemi soru belirtir; tek terimde ortanca yarılara katılmaz). Sıklık tablosunda birikimli sıklıkla ortanca sırasını bul, tek/çift terim sayısını ayrı denetle.
- Tuzak: sıralamamak; sütun sırasını ortanca sanmak.

### Standart sapma, dönüşüm
- Yol: formül soruda verilir (payda n ya da n−1): √(Σ(xᵢ − ort)² / payda). Her terime +b: ortalama, ortanca +b; açıklık, sapma değişmez. ×a: ortalama, ortanca ×a; açıklık, sapma ×|a|; varyans ×a². Aynı ortalamada sapma, uzaklıkların kareleri toplamıyla büyür; hepsi eşitse 0.
- Tuzak: kök almamak; sapmaya +b uygulamak.

## Yaş Problemleri

### Yaş farkı, kaydırma, toplam, oran
- Yol: yaş farkı sabit, herkes yılda 1 büyür. n kişinin toplamı t yılda n·t değişir; o yıl doğmamış kişiyi toplamdan ayır, bugün ayrıca ekle. Oran/kat: bugünkü yaşlara k de, iki yaşa aynı sayıyı ekleyip yeni koşulu yaz. Toplam–fark: büyük = (toplam + fark)/2. "Ben senin yaşındayken" = yaş farkı kadar geri, "sen benim yaşıma geldiğinde" = o kadar ileri; farkı d al, iki toplamı yaz. Eşitlenmede bir yanda 1, öbürde n kişi ise fark yılda n − 1 değişir. Takvim yılında yaş = yıl − doğum yılı; yaş farkı doğum yılları farkı; yılı y al. Farklı yıllara ait yaşları önce ortak yıla çek.
- Kontrol: yaşları tüm koşullara geri koy.

## Yüzde Problemleri

### Hesap, bütünü bulma, oran, tablo, grafik
- Yol: %p = p/100; parça a ise bütün = a ÷ (p/100); oran → yüzde: a/b × 100. "Kalanın %q'si" çarpılarak ilerler. Yüzdenin tabanını yaz (tümü mü, grup mu): 100'lük tablo kur. Yüzde puan farkı eklenen miktarın bütüne oranı. Daire grafiğinde açı toplamı 360°, derece başına değer sabit. Geçerli oy: toplam = geçerli ÷ oran. Pazar payı × pazar: çarpanlar çarpılır. Grup birleşiminde sayılar toplanır.
- Tuzak: parçayı bütün sanmak; tabanı karıştırmak.

### Ardışık değişim, net değişim, çarpım
- Yol: %p artış çarpanı 1 + p/100, azalış 1 − p/100; ardışıkta çarp (toplamaz, sıra önemsiz). Aynı % artıp azalırsa (1+t)(1−t) = 1 − t²: net azalış. Bilinmeyen yüzdeyi çarpanla yaz, 1'den çıkar. Başlangıcı bulmak için bütün çarpanlarla böl.

### Fazla/eksik, yüzde puan, öncüllü
- Yol: "A, B'den yüzde kaç fazla" = (A − B)/B; taban "-den" ekinden önceki. Taban değişince yüzde değişir (%25 fazlanın tersi %20 eksik). Yüzde puan = oranların farkı; göreli = fark ÷ eski oran. Ana kütle belirsizse sayısal değişimde kesin hüküm verme.
- Tuzak: yüzde puanı göreli yüzde yazmak; tabanı karıştırmak.

### KDV, indirim, kademe, kupon
- Yol: dahil = hariç × (1 + oran); hariç = dahil ÷ (1 + oran); KDV = dahil − hariç; indirim sonrası KDV'yi yeni dahil tutardan ayır. İndirimli fiyat = etiket × (1 − oran); ardışık indirim çarpılır. Kademede her dilim kendi fiyatıyla; geriye çözerken dolu dilimleri çıkar. Kupon/eşikte hangi oran hangi tutara uygulanıyor, her seçeneği ayrı hesapla.

## Üslü Sayılar

### Kurallar ve negatif taban
- Yol: aᵐ·aⁿ = aᵐ⁺ⁿ; aᵐ/aⁿ = aᵐ⁻ⁿ; (aᵐ)ⁿ = aᵐⁿ; a⁻ⁿ = 1/aⁿ; a⁰ = 1 (a ≠ 0); (a/b)⁻ⁿ = (b/a)ⁿ. Tabanlar farklıysa ortak tabana çevir (4 = 2², 8 = 2³, 1/4 = 2⁻²); üsler yalnız aynı tabanda toplanır, farklı üslü terimlerin toplamında üsler toplanmaz. (−a)ⁿ: n çift + , tek −; −3² = −9, (−3)² = 9. 2n çift, 2n+1 tektir: kesinlik sorularında n'nin tek ve çift durumuna bak.
- Tuzak: parantezi gözetmemek; negatif üsle sayıyı negatif yapmak; kesir tabanı çevirmemek.

### Ortak çarpan, sadeleştirme, denklem
- Yol: aˣ⁺ᵏ = aˣ·aᵏ, aˣ⁻ᵏ = aˣ/aᵏ; en küçük kuvveti ortak çarpan al. Değişken değiştir (3ˣ = t ⇒ 9ˣ = t²); a > 0 için aˣ negatif olamaz, negatif kökü ele. Aynı tabanda üsleri eşitle; üste çarpılan parantezin her terimini çarp. En sonda sorulan ifadeye (örn. 5ˣ⁺¹) dön. "Çeyreği" ÷4, "4 katı" ×4.
- Tuzak: x'i ya da ara kuvveti cevap sanmak.

### Karşılaştırma, bilimsel gösterim, basamak
- Yol: sıralamada üsleri ya da tabanları eşitle (a⁴⁰ = (a⁴)¹⁰); taban > 1'de büyük üs büyük, negatif üs küçültür. Bilimsel gösterim a × 10ⁿ (1 ≤ a < 10): katsayıları, 10 kuvvetlerini ayrı işle, sonda düzelt (0,5 × 10⁶ = 5 × 10⁵). 1 m = 10² cm = 10³ mm. 2ᵃ·5ᵇ: küçük üssü kadar 10 çıkar, kalan k × 10ⁿ ⇒ basamak = k'nın basamağı + n.

### Büyüme, azalma, eşik, sayma
- Yol: başlangıç N, her adımda k katı: N·kⁿ. "n. gün" ile "n. gün sonu toplam"ı ayır; toplamda her günü yaz. Eşikte 2ⁿ ile sınırı karşılaştır, "ilk kez" için bir önceki adımı da sına; başlangıç da üslü olabilir (2⁻⁴). İlk günün üssüne dikkat (ilk gün 2², n. gün 2ⁿ⁺¹). 2ᵃ·3ᵇ ≤ sınır sayımında bir üssü sabitle, a = 0 ve b = 0'ı atlama.
- Tuzak: "yarısı"/"tümü" gününü karıştırmak.
