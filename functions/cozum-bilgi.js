/* Zek AI çözüm bilgisi ("beceriler"): her çözüm isteğine eklenir (önbellekte durur, ucuzdur).
   16 Kasım 2026 ilk sürüm: 2026 TYT kör testindeki zayıf noktalardan (Türkçe anlam/paragraf, cümle birleştirme,
   yazım-noktalama; iklim grafiği; istatistik; prizma; "kesinlikle/olabilir" yargı soruları) çıkarıldı.
   17 Kasım 2026: soru havuzunun mantık kartlarından (tuzak türleri), çeldirici sebeplerinden ve bilgi kutularından
   Türkçe paragraf, cümle anlamı, anlatım bozukluğu, yazım-noktalama, dil bilgisi, coğrafya ve fen kuralları eklendi.
   İki günde bir çalışan "Zek AI çözüm eğitimi" görevi bu dosyayı soru havuzundan ve gerçek hatalardan günceller.
   KURAL: 2026 TYT sınav seti (kör test seti) bu dosyaya örnek olarak GİRMEZ. Soru metni kopyalanmaz, yalnız kural yazılır. */
export const KAYNAK_COMMIT = "11efaa821ca9b7104bb141f4124e1707d9de4cb3";
export const GUNCELLEME = "2026-11-17";

export const COZUM_BILGI = `ÇÖZÜM BECERİLERİ (her soruda uygula):

GENEL
- Önce soru kökünü oku ve olumsuz/özel ifadeyi işaretle: "değildir, yoktur, söylenemez, ulaşılamaz, değinilmemiştir, yanlıştır, en az, en çok, kesinlikle, olabilir". Olumsuz kökte YANLIŞ olanı ararsın.
- Öncüllü sorularda (I, II, III) her öncülü ayrı ayrı doğru/yanlış diye değerlendir; "hangileri" sorusunda doğru olanların hepsi seçilir.
- Bulduğun cevabı soruda verilen her koşula geri koyarak sına. Bir şıkkı seçmeden önce en güçlü rakip şıkkın neden elendiğini bil.
- Hesap sonucu hiçbir şıkka uymuyorsa soruyu ve okuduğun değerleri baştan oku; şıkka zorla uydurma.
- Emin görünüp yanılma: seçtiğin şıkkı parçadaki bir cümleye, bir kurala ya da bir hesaba dayandıramıyorsan veya iki şık arasında gerçekten kaldıysan emin=false yap. Doğru şık en uzun ya da en "güzel" görünen şık olmak zorunda değildir.

TÜRKÇE · PARAGRAF
- Her şıkkı parçadaki bir dayanak cümlesiyle eşleştir. "Çıkarılabilir / ulaşılabilir / söylenebilir": parçada açıkça yazan ya da ondan zorunlu olarak çıkan bilgi. Kendi yorumunu, gerçek hayatta doğru olan genel bilgiyi ya da parçadan fazlasını söyleyen şık yanlıştır.
- "Ulaşılamaz / değinilmemiştir / söylenemez": dört şıkkın her birinin parçadaki karşılığını bul; karşılığı olmayan ya da parçayla çelişen tek şık cevaptır. Sözcük birebir geçmese de aynı anlam (eş anlamlı ifade, yan cümlede değinme) varsa o şık parçada vardır. Konuya yakın, doğru bir bilgi parçada geçmiyorsa "değinilmemiştir".
- Aşırı genelleme tuzağı: "her, hiç, yalnızca, tek, her zaman, tümüyle, kesinlikle" parçada olmayan bir kesinlik katıyorsa şık parçayı aşar. "Çoğu" → "hepsi", "bazen" → "her zaman" yapan, neden-sonuç yönünü ters çeviren ya da bir kişinin görüşünü başkasına yükleyen şık yanlıştır.
- Ana düşünce / asıl anlatılmak istenen: parçanın tamamını kapsayan yargı (çoğu zaman giriş ya da sonuç cümlesinde). Karşıtlık bağlacından (ama, oysa, ne var ki, aslında) sonra gelen yargı genelde yazarın asıl görüşüdür; yazarın eleştirdiği görüş, bir örnek ya da parçanın yalnız bir bölümünü anlatan şık ana düşünce değildir (yardımcı düşüncedir).
- Konu ve başlık: konu bir adlandırmadır (yargı değil), başlık konuyu ve vurguyu kısaca özetler; ikisi de parçanın tamamını karşılamalı, tek bir örneğe dayanan (dar) ya da parçayı aşan (geniş) şık yanlıştır. Yazarın amacı: göstermek, savunmak ya da eleştirmek istediği şey.
- Boşluk doldurma: giriş cümlesi kendi başına anlaşılır, "bu, şu, ancak, ayrıca, böylece, bu yüzden, söz konusu, aynı" gibi öncüle dayanan sözcük taşımaz. Ortadaki boşluk hem önceki cümleyle konu ve yön bakımından hem de sonraki cümlenin gönderimiyle (bu, böyle, oysa, bu yüzden) uyuşmalı. Son cümle öncekilerden çıkan sonucu verir; yeni bilgi ya da aşırı genelleme getirmez.
- Cümle sıralama ve paragraf bölme: zamir ya da bağlaçla öncekine bağlı cümle başa gelmez ve yeni paragrafı başlatmaz; birbirine gönderen cümle çiftleri ardışık olmalı ("Çünkü" cümlesi açıkladığı cümlenin hemen ardından gelir). "Dolayısıyla, sonuç olarak, kısacası" ile başlayan sonuç cümlesi, kanıt ve örnek cümlelerinden sonra, çoğu zaman sona gelir. Yeni paragraf konunun ya da bakış açısının değiştiği cümlede başlar.
- Akışı bozan cümle: parçanın odağını (neyi, hangi yönden anlattığını) belirle; parçayla aynı anahtar sözcüğü taşısa da bu odaktan başka yöne geçen cümle akışı bozar.
- Anlatım biçimleri: açıklama (bilgi verme), tartışma (görüş savunma, karşı görüşü çürütme), öyküleme (olayı zaman akışıyla anlatma), betimleme (görünüşü sözcüklerle resmetme). Bir parçada birden çok biçim iç içe olabilir.
- Düşünceyi geliştirme yolları: tanık gösterme = görüşü desteklemek için başkasının sözüne/görüşüne başvurma (yalnız kişi adı geçmesi yetmez); sayısal veri = düşünceyi sayı, oran, yüzdeyle destekleme (geçen her sayı değil); benzetme = iki varlık arasında "gibi, kadar" ile benzerlik kurma; karşılaştırma = iki durumu benzerlik ve farklarıyla yan yana koyma; örnekleme = somut bir durumla destekleme; tanımlama = "X, ... dır" diye kavramı açıklama; kişileştirme = insan dışı varlığa insan özelliği verme. "Yoktur" kökünde parçada hiç kullanılmayanı ara.
- Yeni nesil sorular: tablo ya da grafikteki her değeri tek tek kontrol et (artış miktarı ile artış oranını, toplam ile oranı karıştırma); iki konuşmacılı metinde her görüşün sahibini ayrı tut; kural-durum sorularında kuralın her koşulunu duruma uygula.

TÜRKÇE · CÜMLE VE SÖZCÜK ANLAMI
- Sözcükte anlam: sözcüğün o cümledeki anlamına bak (gerçek, mecaz, yan anlam); sözlükteki ilk anlam değil. "Soğuk bakış, sert söz" gibi alışılmış birleşimler mecazdır.
- Deyim ve atasözü: sözü sadeleştirip özünü çıkar, sonra şıktaki durumun aynı özü taşıyıp taşımadığına bak; ortak sözcüğe değil düşüncenin yönüne göre eşleştir.
- Anlamca özdeş cümle: "Yalnızca A olanlar B'dir" = "B olan herkes A'dır"; tersi ("A olan herkes B'dir") aynı anlama gelmez. Sınırlayıcı sözcükleri (yalnızca, ancak, bile, de) gözden kaçırma.
- Neden-sonuç: "-dığı için, yüzünden, -dığından"; amaç-sonuç: "için, diye, amacıyla" (ulaşılmak istenen); koşul: "-sa, -mak şartıyla". Amacı nedenle, koşulu nedenle karıştırma.
- Öznel yargı: beğeni, duygu, değer bildirir (bence, güzel, en iyi, gereksiz, ne yazık ki); kanıtlanamaz. Nesnel yargı: ölçülebilir, doğrulanabilir, kişiye göre değişmez. Bilgi gibi görünen ama değer yargısı içeren ifade özneldir.
- İki cümlenin birleştirilmesi: iki cümledeki bilgilerin hepsi korunmalı, aralarındaki anlam ilişkisi (neden-sonuç, karşıtlık, zaman sırası, koşul) değişmemeli. Bilgi ekleyen, eksilten ya da ilişkiyi tersine çeviren şık yanlıştır.

TÜRKÇE · ANLATIM BOZUKLUĞU
- Türler: gereksiz sözcük (anlamca tekrar: geri iade, yaklaşık tahminen); yanlış anlamlı sözcük; özne-yüklem kişi/sayı uyumsuzluğu; ortak öge yanlışlığı (ortak ögenin eki her yüklemle uyumlu olmalı: "kitaba baktı ve okudu" bozuk); ek eksikliği; mantık ve neden-sonuç çelişkisi; sıralama yanlışlığı; karşılaştırılan ögelerin farklı türden olması; "tarafından" ile etken fiil kullanılması (edilgen olmalı).
- Her cümleyi sınamak için önce yüklemi bul, ortak ögeyi her yüklemle ayrı ayrı dene. Vurgu amaçlı doğal tekrar ya da anlamı farklı iki sözcük bozukluk değildir; dil bilgisi doğru görünen cümle anlamca bozuk olabilir.

TÜRKÇE · YAZIM VE NOKTALAMA (TDK)
- Büyük harf: kişi, yer, kurum, kuruluş, millet, dil adları ve bunların her sözcüğü büyük başlar; özel adı tamamlayan "Gölü, Dağı, Bulvarı" da büyük. Belirli tarih bildiren ay ve gün adları büyük (29 Ekim 1923 Pazartesi), belirli tarih yoksa küçük (her pazartesi). Unvanlar özel addan sonra gelince büyük (Ayşe Hanım). Yön adı yer adının parçasıysa büyük (Doğu Anadolu), yön bildiriyorsa küçük (güneye gitti).
- Kesme işareti: özel adlara gelen çekim ekleri kesmeyle ayrılır (Ankara'ya); kurum, kuruluş, kurul adlarına gelen ekler ayrılmaz (Türk Dil Kurumuna). Yapım ekinden sonra ve dil adına gelen ekte kesme yok (Ankaralı, Türkçeyi). Kısaltma ve rakamla yazılan sayıya gelen ek kesmeyle ayrılır ve okunuşa göre seçilir (TDK'ye, 1960'ta, 40'ı).
- Ayrı/bitişik: bağlaç "de/da" ayrı yazılır, hiç "te/ta" olmaz; bulunma eki bitişik, sert ünsüzden sonra "-te/-ta" olur. Bağlaç "ki" ayrı, ilgi "-ki" bitişik (evdeki, dünkü); kalıplaşmış "belki, çünkü, sanki, oysaki, mademki, halbuki" bitişik. Soru eki "mi" ayrı, ona gelen ekler bitişik (geldin mi, mısın). "-ken, -leyin" bitişik. "Ya da, hem de, her şey, her gün, hiçbir şey, bir an, bir şey" ayrı; "birkaç, hiçbir, herhangi, birbiri, biraz, birlikte" bitişik. Ses olayına uğrayan birleşik fiil bitişik (hissetmek, kaybolmak), uğramayan ayrı (yardım etmek, kabul etmek). Pekiştirme bitişik (masmavi), ikileme ayrı ve araya işaret konmaz (ağır ağır).
- Virgül: sıralı eş görevli sözcük ve sıfatlar arasına (son sıfatla ad arasına değil); "ve"den önce konmaz; özne, nesne, yüklem arasına gereksiz virgül konmaz; hitap ve evet/hayır sonrasına; ara sözün iki yanına; yüklemi ortak cümleler arasına.
- Noktalı virgül: ögeleri arasında virgül bulunan sıralı cümleler arasına. İki nokta: tamamlanmış cümleden sonra açıklama, örnek, sıralama ya da alıntı öncesine, cümle ortasında değil. Tırnak: alıntı, vurgulanan söz, eser adı. Yay ayraç: açıklama, (?) kesinsizlik, (!) alay; yüklem gibi temel öge ayraç içine alınmaz. Üç nokta: bitmemiş cümle, sayılabilecek başka örnekler. Soru anlamı taşıyan cümle soru işaretiyle, soru sözcüğü olsa da bilgi veren dolaylı soru noktayla biter. Büyük harfli kurum kısaltmalarına nokta konmaz (TBMM).

TÜRKÇE · DİL BİLGİSİ
- Cümlenin olumlu/olumsuz, fiil/isim, kurallı/devrik oluşu yükleme göre belirlenir; fiilimsideki olumsuzluk cümleyi olumsuz yapmaz. Birleşik cümle fiilimsi, şart ya da "ki" ile yan yargı içerir; sıralı cümle bağımsız yargılardan oluşur.
- Fiilimsiler yüklem olmaz: isim-fiil (-mak, -ma, -ış), sıfat-fiil (-an, -dık, -acak, -mış, -ar, -maz), zarf-fiil (-arak, -ınca, -ıp, -ken, -madan). Kalıcı adlaşmış sözcükler (yazı, süpürge, dondurma) fiilimsi değildir.
- Ögeler yükleme soru sorularak bulunur: kim/ne (özne), neyi/ne (nesne), kime/nerede/nereden (dolaylı tümleç), ne zaman/nasıl/ne kadar (zarf tümleci). Edat öbeği (için, gibi, göre, ile) zarf tümlecidir; ara söz ve hitap öge değildir. Edilgen yüklemin öznesi sözde öznedir.

SOSYAL
- İklim grafiği: yağış rejimine ve sıcaklık farkına bak. Akdeniz: yaz sıcak ve kurak, kış ılık ve yağışlı. Karadeniz: her mevsim yağışlı, sıcaklık farkı az. Karasal: kış soğuk, yaz sıcak, yağış az, en çok ilkbaharda. Muson: yaz çok yağışlı, kış kurak. Ekvatoral: her ay sıcak (yaklaşık 25-27 °C) ve yağışlı. Savan: sıcak, yaz yağışlı kış kurak. Çöl: yağış çok az, günlük sıcaklık farkı büyük.
- Grafikte en sıcak ay Ocak civarındaysa yer Güney Yarım Küre'dedir; mevsimleri buna göre ters düşün.
- Eş eğri haritaları (izoterm, izobar, izohips): bir noktanın değeri yalnız komşu iki eğri arasında bir aralıktır; eğri üzerindeki nokta eğrinin değerini alır. Aynı aralıktaki iki noktanın kesin sıralamasını, değer yazmıyorsa varsayma.
- Nüfus piramidi: tabanı geniş → doğum oranı yüksek, genç nüfus fazla; tabanı daralan → doğum oranı düşüyor; üst basamaklar geniş → yaşlı nüfus fazla, ortalama yaşam süresi uzun.
- Tarih ve felsefe sorularında parçada verilen bilgiyle yetin; parçadaki yargıyı çağın ya da düşünürün genel bilgisiyle karıştırma. Kronoloji sorularında olayların tarihlerini yazıp sırala.

MATEMATİK
- İstatistik: aritmetik ortalama = toplam / sayı; ortanca (medyan) = veriler sıralanınca ortadaki değer, veri sayısı çiftse ortadaki iki değerin ortalaması; tepe değer (mod) = en çok tekrar eden; açıklık = en büyük − en küçük. Sorulan büyüklüğü bulmak için bu tanımlardan denklem kur, şıkları koşullara koyarak kontrol et.
- Grafik ve tablo: her grafiğin eksen ölçeğini ayrı oku (iki grafiğin ölçeği farklı olabilir); "kaç katı", "yüzde kaç arttı" ve "ne kadar arttı" farklı sorulardır.
- Dikdörtgenler prizması (a, b, c): hacim = a·b·c, yüzey alanı = 2(ab + ac + bc), yüzlerin alanları ab, ac, bc. Bir yüzün alanı verilirse kalan kenarı hacimden bul, sonra yüzey alanı koşulunu sağlat.
- Problemlerde birimleri eşitle (dakika-saat, cm-m, kuruş-lira); "kaç tane daha / kaç fazla" farkı sorar.
- Sayı problemlerinde bulunan değerin tam sayı, pozitif, rakam olma, rakamları farklı olma gibi koşulları sağladığını kontrol et; basamak değeri ile sayı değerini karıştırma.

GEOMETRİ
- Şekil ölçekli değildir; yalnız yazılı değer ve işaretleri kullan. Yamuk alanı = (alt taban + üst taban)/2 · yükseklik; yükseklik tabanlara dik uzaklıktır, yan kenar değildir. Dış açı = komşu olmayan iki iç açının toplamı.

FEN
- "Kesinlikle doğrudur": her olası durumda doğru olmalı. "Doğru olabilir": en az bir durumda mümkün olması yeter. Hal değişimi sırasında ısı alan maddenin sıcaklığı değişmez; ortalama kinetik enerji yalnızca sıcaklığa bağlıdır.
- Yük ve elektriklenme: dokunma ile elektriklenmede toplam yük korunur, yükler sığalarla orantılı paylaşılır; etki ile elektriklenmede yaklaştırılan cismin yükü değişmez.
- Grafik sorularında eğim ve alan anlamını kullan (konum-zaman eğimi hız, hız-zaman eğimi ivme, hız-zaman alanı yer değiştirme; eksenin altındaki alan ters yönde yer değiştirmedir).
- Ağırlık = kütle × g; basınç ve kuvvet hesaplarında kütleyi değil ağırlığı kullan. Mol sayısı = kütle / mol kütlesi; mol ile gramı karıştırma.
`;
