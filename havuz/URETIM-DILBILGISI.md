# Dil bilgisi genişletme talimatı (TYT Türkçe · koç onayı 10 Kasım 2026)

Önce `havuz/URETIM.md`, `havuz/URETIM-DERSLER.md` ve `havuz/URETIM-PARAGRAF.md` dosyalarını oku; burada yazmayan her kural oradan gelir. Bu dosya **dil bilgisi genişletmesinin** farklarını anlatır. Hedef: dil bilgisinde toplam ~300 soru (42 iskelet + ~258 yeni).

## Dağılım (yeni soru sayısı · önek · uygulama anahtarı · kart öneki · tipId öneki)
| Konu | Hedef | Var | Yeni | Önek | Anahtar | Kart | tipId |
|---|---|---|---|---|---|---|---|
| Yazım | 55 | 6 | 49 | `dyazim` | `tr\|Yazım Kuralları` | `K-DBYZ-..` | `dyz-` |
| Noktalama | 55 | 6 | 49 | `dnokta` | `tr\|Noktalama İşaretleri` | `K-DBNK-..` | `dnk-` |
| Sözcük türleri | 45 | 4 | 41 | `dsozcuk` | `tr\|Sözcük Türleri` | `K-DBST-..` | `dst-` |
| Ögeler | 40 | 6 | 34 | `doge` | `tr\|Cümlenin Ögeleri` | `K-DBOG-..` | `dog-` |
| Yapı / ekler | 30 | 4 | 26 | `dyapi` | `tr\|Sözcükte Yapı/Ekler` | `K-DBYP-..` | `dyp-` |
| Fiil · ek fiil · fiilimsi · çatı | 30 | 4 | 26 | `dfiil` | `tr\|Fiiller-Fiilimsiler-Ek Fiiller-Çatı` | `K-DBFL-..` | `dfl-` |
| Ses bilgisi | 20 | 4 | 16 | `dses` | `tr\|Ses Bilgisi` | `K-DBSS-..` | `dss-` |
| Anlatım bozukluğu | 13 | 4 | 9 | `danlat` | `tr\|Anlatım Bozukluğu` | `K-DBAB-..` | `dab-` |
| Cümle türleri | 12 | 4 | 8 | `dcumle` | `tr\|Cümle Türleri` | `K-DBCT-..` | `dct-` |

İskelet dosyalarındaki (ör. `yazim-1.json`) soruları oku ve **tekrarlama**: aynı örnek cümleyi, aynı sözcük çiftini, aynı kurguyu kullanma.

## Hafif mod (geçerli)
- Kardeş yok (`kardes` None), `ipuclari` tam 1 ipucu (cevabı söylemez).
- Yardımcı: `havuz/tyt-tr/hafif_db.py` (`kur`, `soru`, `bitir`; `soru(..., kalip='öncüllü')`). Her şıkka etiket verilir; tek şık koşulu sağlar (assert). Ayrıca doğru şık belirgin en uzunsa, uç sözcük örüntüsü varsa, kök `?` ile bitmiyorsa, harf dengesi ±2'yi aşıyorsa betik durur.
- Betik: `havuz/tyt-tr/uret-<onek>.py`; `Q=kur('<onek>','<Konu adı>','<anahtar>',KARTLAR,TIPLER); Q.n=<sayı>` … `bitir(Q)`. Kartlar `havuz/kartlar/<onek>.json`'a yazılır.
- Mevcut dosyaları değiştirme; yalnız kendi öneklerine yaz.

## Kaynak ve zorluk
- Tip ve zorluk ölçüsü: ÖSYM TYT Türkçe 2018–2026 dil bilgisi soruları ve koçun satın aldığı **Bilgi Sarmal Dil Bilgisi Soru Bankası** (görüntü PDF; ÖSYM Tipi bölümleri). Kitaptan ya da ÖSYM'den **metin, cümle, örnek kopyalanmaz**; yalnız mantık kartı (soru kalıbı, tuzak türü, zorluğun kaynağı) çıkarılır. Kart `kaynak` alanı: `"ÖSYM TYT Türkçe 2018–2026 · Bilgi Sarmal Dil Bilgisi SB (ÖSYM Tipi) · TDK Yazım Kılavuzu"`.
- 11 Kasım üretiminde kitap sayfalarına erişilemedi (Mac bağlantısı yok); kartlar ÖSYM kalıp bilgisine göre yazıldı. Kitap erişilince kartlar gözden geçirilebilir.
- **Zorluk ÖSYM düzeyinde.** Dağılım her önekte ~%20 kolay, %50 orta, %30 zor. İskelet soruları çoğunlukla "kolay–orta"; genişletmede ağırlık orta–zor.

## ÖSYM'nin dil bilgisi soru biçimleri (çeşitlendir)
1. **Beş cümle** (klasik): "Aşağıdaki cümlelerin hangisinde … yanlışı vardır / … yoktur / … kullanılmıştır?" Şıklar benzer uzunlukta, aynı konu alanından değil; her şık farklı bir kuralı sınar.
2. **Numaralı parça** (ÖSYM'nin son yıllardaki ağırlıklı biçimi, sayının ~%40'ı): 50–90 kelimelik özgün parça; sınanan sözcük/öge/yer `(I)`, `(II)` … `(V)` ile işaretlenir. Altı çizgi yok, onun yerine sözcükten hemen sonra numara: "yarın (I) da gelecek". Kök: "Bu parçadaki numaralanmış sözcüklerden hangisinin yazımı yanlıştır?", "Bu parçada numaralanmış yerlerden hangisine virgül (,) getirilmelidir?", "Bu parçadaki numaralanmış sözcüklerden hangisi türce ötekilerden farklıdır?" Şıklar `I`, `II`, `III`, `IV`, `V` (kalıp `öncüllü`).
3. **Boşluk sırası** (noktalama): "Bu cümlede boş bırakılan yerlere sırasıyla hangi noktalama işaretleri getirilmelidir?" Boşluk `( )`; şıklar `(,) (;) (.)` gibi sıralı diziler. Yalnız tek dizi tümüyle doğru olmalı; çeldiriciler tek yerde farklılaşsın.
4. **Öncül eşleme / karşılaştırma**: "Bu cümlenin ögeleri sırasıyla hangi seçenekte verilmiştir?", "Aşağıdaki sözcüklerin hangisinin karşısında yazılan ses olayı yanlıştır?", "I ve II'deki altı çizili sözcükler … bakımından aynıdır" türü.
5. **Ortak özellik**: "Bu cümlelerin hangisi yapıca ötekilerden farklıdır?", "Aşağıdaki cümlelerin hangisinde hem … hem … vardır?" (zor soru kaynağı).

## Konu başına alt tipler (kart önerisi; her önekte en az 5 kart, her karttan en az 3 soru)
- **Yazım**: de/da · ki · mi; büyük harf (kurum, unvan, yer, tarih, yön, eser adı); bitişik/ayrı yazılan birleşik sözcükler (yardımcı fiilli birleşikler: hissetmek ama yardım etmek; "-a, -e" ile kurulanlar); pekiştirme/ikileme; sayılar, kısaltmalar ve eklerinin yazımı (TDK'ye, km'yi); düzeltme işareti; yazılışı karıştırılan sözcükler; "-ken, -leyin, ile" eklerinin yazımı; numaralı parçada yazım.
- **Noktalama**: virgül (sıralı ögeler, cümle başı sözler, ara söz, uzun özneden sonra, sıralı cümleler); noktalı virgül; iki nokta; üç nokta; kesme (özel ad, kurum adı ekleri — kurum adına gelen ek kesmeyle ayrılmaz!, kısaltma, sayı); tırnak; yay ayraç; kısa çizgi / uzun çizgi; soru ve ünlem (alay/kesinsizlik için ayraç içi); numaralı yere hangi işaret; boşluk sırası.
- **Sözcük türleri**: ad (yapı, anlam: soyut/somut, topluluk), sıfat (niteleme/belirtme, sıfat tamlaması), zamir (kişi, dönüşlülük, işaret, belgisiz, soru, ilgi -ki), zarf (durum, zaman, miktar, yer–yön, soru), edat (gibi, kadar, için, göre, ile), bağlaç (ve, ama, ki, de, ile ayrımı); aynı sözcüğün farklı görevleri (türce farklı olan); "en çok ad soylu sözcük" türü ince sorular.
- **Ögeler**: yüklem (isim/fiil soylu), özne (gizli, sözde), nesne (belirtili/belirtisiz), dolaylı tümleç, zarf tümleci (edat tümleci dahil), ögelerin sıralanışı, ara söz/ cümle dışı unsur, aynı ögeyi bulma, yüklemi en sonda olmayan (devrik) cümle.
- **Yapı / ekler**: basit/türemiş/birleşik sözcük; yapım–çekim eki ayrımı; isimden isim/fiil, fiilden isim/fiil yapım ekleri; çekim ekleri (hâl, iyelik, çoğul, ilgi, eşitlik); kök–gövde; aynı ek mi farklı mı; numaralı parçada yapıca farklı sözcük.
- **Fiil – ek fiil – fiilimsi – çatı**: kip ve kişi; birleşik zamanlı fiiller (hikâye, rivayet, şart); ek fiilin görevleri (ad soylu sözcüğü yüklem yapma / birleşik zaman); isim-fiil, sıfat-fiil, zarf-fiil; kalıcı adlaşmış fiilimsi tuzağı (dolma, çakmak, dondurma); çatı (etken/edilgen; geçişli/geçişsiz; dönüşlü/işteş); fiilde anlam (yeterlik, tezlik, sürerlik, yaklaşma).
- **Ses bilgisi**: ünlü uyumları; ünlü düşmesi; ünlü daralması; ünsüz yumuşaması/benzeşmesi (sertleşmesi); ünsüz düşmesi; kaynaştırma; ulama; ses olayı eşleştirme ve "ses olayı olmayan" sözcük; numaralı parçada ses olayı.
- **Anlatım bozukluğu**: gereksiz sözcük; yanlış sözcük/anlam; mantık hatası; tamlama/ek eksikliği; özne–yüklem uyumsuzluğu (sayı ve kişi); öge eksikliği (ortak öge yanlışlığı); çatı uyuşmazlığı; sıralama yanlışlığı; bağlaç yanlışı. Her soruda bozukluğun TÜRÜ adımlarda adıyla söylenir.
- **Cümle türleri**: yüklemin türü ve yeri (kurallı/devrik/eksiltili); anlamına göre (olumlu/olumsuz/soru/ünlem; biçimce olumlu anlamca olumsuz); yapısına göre (basit/birleşik — fiilimsi ve -ki ile, iç içe, şartlı; sıralı/bağımlı sıralı — ortak öge; bağlaçlı).

## Tek doğru şık ve çeldirici kuralları (en önemli)
- Her şık betikte etiketlenir; `pred` tam bir şıkta doğru olur. **Kendini kör çözücü yerine koy**: başka bir şık da savunulabiliyorsa cümleyi değiştir.
- **İki savunulabilir şık yasak.** TDK Yazım Kılavuzu'nda iki biçimi kabul edilen (ör. "birçok/bir çok" ayrımı anlama göre, "yalnız" zarf/bağlaç, "-ki" ile kurulan "halbuki"), uzmanlar arasında tartışmalı olan (ör. "kadar" edat mı ad mı, isim tamlaması mı sıfat tamlaması mı belirsiz yapılar, "sıralı mı bağımlı sıralı mı" bulanık cümleler, "vurgu/ses olayı" yoruma açık durumlar) örnekleri **kullanma**. Kuralın tartışmasız örneğini seç.
- **Ele veren şık yok**: doğru şık en uzun, en "düzgün" ya da biçimce farklı olmasın; beş cümle aynı uzunluk bandında (±%25). Numaralı parçada doğru numara her zaman aynı konumda olmasın.
- **Uç sözcük kuralı**: yanlış şıklara "yalnızca, hiç, tamamen, kesinlikle" gibi sözcük yığma; yapı soruları uç sözcükle çözülmemeli.
- Çeldiriciler gerçek öğrenci hatalarından: bağlaç "de"yi ek sanmak; kurum adına kesme koymak; "gibi"yi bağlaç sanmak; sıfat-fiili sıfat saymamak; kalıcı adlaşmayı fiilimsi saymak; sözde özneyi gerçek özne sanmak; edat tümlecini dolaylı tümleç sanmak; "-ki" ilgi zamirini sıfat sanmak.
- Olumsuz kökte ("… yoktur / değildir / yanlıştır") dört şıkta ilgili özellik açıkça ve tartışmasız bulunmalı.
- Cümleler doğal, güncel Türkçe; konu çeşitli (doğa, sanat, okul, şehir, bilim, spor, aile). Gerçek kişi alıntısı yok; kişi adları sıradan (Elif, Kerem…), unvanlı uydurma kişi yok ("Prof. Dr. X" yerine "bir öğretim üyesi"). Kurum/yer adı gerekiyorsa gerçek ve tartışmasız olanlar (Türk Dil Kurumu, Ankara, Karadeniz).
- Her sorunun bir yazım/noktalama hatası **yalnız sınanan yerde** olmalı: sorunun kendi metninde başka yazım ya da noktalama yanlışı bulunmasın (en sık doğrulayıcı bulgusu).

## Anlatım alanları
- `bilgi` 1–2 madde (kural + bir örnek). `adimlar` 3–5 adım: kuralı hatırla → şıkları/numaraları tek tek sına (`islem` kısa: "I: ayrı ✓ · II: bitişik ✗") → sonuç. `puf` tek cümle, genellenebilir. Çeldirici açıklamaları (`cel`) şıkkın neden doğru/yanlış olmadığını kuralı adıyla söyler (≥12 karakter).

## Denetim
`python3 havuz/denetle.py havuz/tyt-tr/<onek>-1.json --benzerlik /home/claude/kutup/dersler/osym_turkce.txt` → **0 hata**. (Kaynak dosyası yoksa benzerliksiz çalıştır; koordinatör sonra benzerliği ekler.) Havuz içi tekrar uyarısında cümleyi değiştir.

## Dosyalar ve kural
- Yalnız kendi öneklerine yaz: `havuz/kartlar/<onek>.json`, `havuz/tyt-tr/uret-<onek>.py`, `havuz/tyt-tr/<onek>-1.json`.
- Numara 0001'den başlar. Cevap harfleri öneğin içinde dengeli (her harf ±2).
- git commit/push yok, GitHub yok, artifact yok.
- Sonunda kısa rapor: sayı, zorluk, harf dağılımı, kart/tip dağılımı, "emin olmadıklarım" (id + neden).
