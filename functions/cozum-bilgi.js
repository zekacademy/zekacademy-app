/* Zek AI çözüm bilgisi ("beceriler"): her çözüm isteğine eklenir (önbellekte durur, ucuzdur).
   16 Kasım 2026 ilk sürüm: 2026 TYT kör testindeki zayıf noktalardan (Türkçe anlam/paragraf, cümle birleştirme,
   yazım-noktalama; iklim grafiği; istatistik; prizma; "kesinlikle/olabilir" yargı soruları) çıkarıldı.
   17 Kasım 2026: soru havuzunun mantık kartlarından (tuzak türleri), çeldirici sebeplerinden ve bilgi kutularından
   Türkçe paragraf, cümle anlamı, anlatım bozukluğu, yazım-noktalama, dil bilgisi, coğrafya ve fen kuralları eklendi.
   19 Kasım 2026: geometri (üçgen eşitsizliği, benzerlik, açıortay, çevre açı), biyoloji (deney karşılaştırma, enzim, kalıtım),
   kaldırma kuvveti, cümle sıralamada gönderme/sonuç cümlesi; geometri/AYT/biyoloji/fen havuz dalgalarının püf ve çeldiricilerinden.
   Yer açmak için eski maddeler anlam kaybı olmadan kısaltıldı.
   İki günde bir çalışan "Zek AI çözüm eğitimi" görevi bu dosyayı soru havuzundan ve gerçek hatalardan günceller.
   KURAL: 2026 TYT sınav seti (kör test seti) bu dosyaya örnek olarak GİRMEZ. Soru metni kopyalanmaz, yalnız kural yazılır. */
export const KAYNAK_COMMIT = "0a26a4038738fa7e222aed0025625602c560b214";
export const GUNCELLEME = "2026-11-19";

export const COZUM_BILGI = `ÇÖZÜM BECERİLERİ (her soruda uygula):

GENEL
- Önce soru kökünü oku ve olumsuz/özel ifadeyi işaretle: "değildir, yoktur, söylenemez, ulaşılamaz, değinilmemiştir, yanlıştır, en az, en çok, kesinlikle, olabilir". Olumsuz kökte YANLIŞ olanı ararsın.
- Öncüllü sorularda (I, II, III) her öncülü ayrı ayrı doğru/yanlış diye değerlendir; "hangileri" sorusunda doğru olanların hepsi seçilir.
- Cevabı her koşula geri koyarak sına; en güçlü rakip şıkkın neden elendiğini bil. Hesap hiçbir şıkka uymuyorsa soruyu ve okuduğun değerleri baştan oku, şıkka zorla uydurma. Sonda istenene dön (parça mı bütün mü).
- Seçtiğin şıkkı parçadaki bir cümleye, kurala ya da hesaba dayandıramıyorsan veya iki şık arasında kaldıysan emin=false yap.

TÜRKÇE · PARAGRAF
- Her şıkkı parçadaki bir dayanak cümlesiyle eşleştir. "Çıkarılabilir / ulaşılabilir / söylenebilir": parçada açıkça yazan ya da ondan zorunlu olarak çıkan bilgi. Yorum, genel doğru bilgi ya da parçadan fazlası yanlıştır. Doğru şık çoğu zaman parçadaki bir cümlenin başka sözcüklerle söylenmiş hâlidir.
- "Ulaşılamaz / değinilmemiştir / söylenemez": dört şıkkın her birinin parçadaki karşılığını bul; karşılığı olmayan ya da parçayla çelişen tek şık cevaptır. Sözcük birebir geçmese de aynı anlam (eş anlamlı ifade, yan cümlede değinme) varsa o şık parçada vardır.
- Aşırı genelleme: "her, hiç, yalnızca, tümüyle" parçada olmayan bir kesinlik katıyorsa şık parçayı aşar; "çoğu" → "hepsi" yapan, neden-sonucu ters çeviren ya da bir kişinin görüşünü başkasına yükleyen şık da yanlıştır. Ama sözcüğe bakıp otomatik eleme: parça gerçekten o genişliği anlatıyorsa "her" diyen şık doğrudur.
- Ana düşünce / asıl anlatılmak istenen: parçanın tamamını kapsayan yargı. Karşıtlık bağlacından (ama, oysa, ne var ki, aslında) sonra gelen yargı genelde yazarın asıl görüşüdür; eleştirilen görüş, örnek ya da parçanın bir bölümü ana düşünce değildir.
- "Destekler / savunulan": önce yazarın görüşünü bul (karşı çıktığı yaygın görüşten sonra "oysa, ama, söyleyeceğim, tersini savunmak" ile gelir). Doğru şık bu görüşü başka sözlerle söyler ya da ona kanıt olur; yazarın çürüttüğü görüşü destekleyen şık yanlıştır. Parça zincir kuruyorsa ("A ancak B kadar; B de ancak C kadar") doğru şık çoğu zaman zincirin ilk ve son halkasını bağlar.
- Konu ve başlık: parçanın tamamını karşılamalı; tek örneğe dayanan (dar) ya da parçayı aşan (geniş) şık yanlıştır.
- Boşluk doldurma: giriş cümlesi kendi başına anlaşılır, öncüle bağlanan sözcük (bu, şu, ancak, ayrıca, böylece, bu yüzden, söz konusu) taşımaz. Ortadaki cümle hem önceki cümlenin yönüyle hem sonraki cümlenin gönderimiyle (bu, böyle, oysa) uyuşmalı. Son cümle öncekilerden çıkan sonuçtur; konuyu yeni sayı, örnek ya da yan bilgiyle sürdüren cümle sona gelmez.
- Cümle sıralama ve paragraf bölme: zamir ya da bağlaçla öncekine bağlı cümle başa gelmez ve yeni paragrafı başlatmaz; birbirine gönderen cümle çiftleri ardışık olmalı ("Çünkü" cümlesi açıkladığı cümlenin hemen ardından gelir; "bu kalıplar, bunlar" adını veren cümleye bitişir). "Dolayısıyla, sonuç olarak, kısacası" ile başlayan sonuç cümlesi bütün kanıt ve örnek cümlelerinden sonra, çoğu zaman sona gelir. Yeni paragraf konunun ya da bakış açısının değiştiği cümlede başlar.
- Akışı bozan cümle: parçanın odağını (neyi, hangi yönden anlattığını) belirle; parçayla aynı anahtar sözcüğü taşısa da bu odaktan başka yöne geçen cümle akışı bozar. Sınama: adayı çıkar; sonraki cümle ("Bu nedenle, Bu yüzden, Böylece" ile başlıyorsa özellikle) bir öncekine daha sıkı bağlanıyorsa çıkardığın cümle akışı bozandır.
- Anlatım biçimleri: açıklama, tartışma (görüş savunma, karşı görüşü çürütme), öyküleme (zaman akışı), betimleme (görünüşü resmetme); iç içe olabilir.
- Düşünceyi geliştirme yolları: tanık gösterme = başkasının sözüne başvurma (yalnız kişi adı yetmez); sayısal veri = düşünceyi sayıyla destekleme (her sayı değil); benzetme ("gibi"); karşılaştırma (iki durumu yan yana koyma); örnekleme; tanımlama; kişileştirme. "Yoktur" kökünde parçada hiç kullanılmayanı ara.
- Yeni nesil: tablodaki her değeri tek tek kontrol et; iki konuşmacılı metinde görüşlerin sahibini karıştırma.

TÜRKÇE · CÜMLE VE SÖZCÜK ANLAMI
- Sözcükte ve sözde anlam: anlamı parçanın kendi açıklamasından çıkar (yanındaki karşıtlık, niteleme: neyle karşılaştırılıyor, kim kurmuş, gönüllü mü zorunlu mu). Sözcüğün en yaygın anlamına ya da çağrışımına göre seçme ("yalın" bağlamda "yüzeysel" olabilir, "süssüz" değil).
- Deyim ve atasözü: sözü sadeleştirip özünü çıkar, sonra şıktaki durumun aynı özü taşıyıp taşımadığına bak; ortak sözcüğe değil düşüncenin yönüne göre eşleştir.
- Anlamca özdeş cümle: "Yalnızca A olanlar B'dir" = "B olan herkes A'dır"; tersi ("A olan herkes B'dir") aynı anlama gelmez.
- Neden-sonuç: "-dığı için, yüzünden, -dığından"; amaç-sonuç: "için, diye, amacıyla" (ulaşılmak istenen); koşul: "-sa, -mak şartıyla". Amacı nedenle, koşulu nedenle karıştırma.
- Öznel yargı beğeni, duygu, değer bildirir (bence, güzel, gereksiz), kanıtlanamaz; nesnel yargı doğrulanabilir.
- İki cümlenin birleştirilmesi: iki cümledeki bilgilerin hepsi korunmalı, aralarındaki anlam ilişkisi (neden-sonuç, karşıtlık, zaman sırası, koşul) değişmemeli.

TÜRKÇE · ANLATIM BOZUKLUĞU
- Türler: gereksiz sözcük (anlamca tekrar: geri iade, yaklaşık tahminen); yanlış anlamlı sözcük; özne-yüklem kişi/sayı uyumsuzluğu; ortak öge yanlışlığı (ortak ögenin eki her yüklemle uyumlu olmalı: "kitaba baktı ve okudu" bozuk); ek eksikliği; mantık ve neden-sonuç çelişkisi; sıralama yanlışlığı; karşılaştırılan ögelerin farklı türden olması; "tarafından" ile etken fiil kullanılması (edilgen olmalı).
- Her cümleyi sınamak için önce yüklemi bul, ortak ögeyi her yüklemle ayrı ayrı dene. Vurgu amaçlı tekrar bozukluk değildir.

TÜRKÇE · YAZIM VE NOKTALAMA (TDK)
- Büyük harf: kişi, yer, kurum, kuruluş, millet, dil adları ve bunların her sözcüğü büyük başlar; özel adı tamamlayan "Gölü, Dağı, Bulvarı" da büyük. Belirli tarih bildiren ay ve gün adları büyük (29 Ekim 1923 Pazartesi), belirli tarih yoksa küçük (her pazartesi). Yön adı yer adının parçasıysa büyük (Doğu Anadolu), yön bildiriyorsa küçük (güneye gitti).
- Kesme işareti: özel adlara gelen çekim ekleri kesmeyle ayrılır (Ankara'ya); kurum, kuruluş, kurul adlarına gelen ekler ayrılmaz (Türk Dil Kurumuna, Hukuk Fakültesine); kurum adından sonra kesme varsa yanlıştır. Yapım ekinden sonra ve dil adına gelen ekte kesme yok (Ankaralı, Türkçeyi). Kısaltma ve rakamla yazılan sayıya gelen ek kesmeyle ayrılır ve okunuşa göre seçilir (TDK'ye, 1960'ta, 40'ı).
- Ayrı/bitişik: bağlaç "de/da" ayrı yazılır, hiç "te/ta" olmaz; bulunma eki bitişik, sert ünsüzden sonra "-te/-ta" olur. Bağlaç "ki" ayrı, ilgi "-ki" bitişik (evdeki, dünkü); kalıplaşmış "belki, çünkü, sanki, oysaki, mademki, halbuki" bitişik. Soru eki "mi" ayrı, ona gelen ekler bitişik (geldin mi, mısın). "-ken, -leyin" bitişik. "Ya da, hem de, her şey, her gün, hiçbir şey, bir an, bir şey" ayrı; "birkaç, hiçbir, herhangi, birbiri, biraz, birlikte" bitişik. Ses olayına uğrayan birleşik fiil bitişik (hissetmek, kaybolmak), uğramayan ayrı (yardım etmek, kabul etmek). Pekiştirme bitişik (masmavi), ikileme ayrı ve araya işaret konmaz (ağır ağır).
- Virgül: sıralı eş görevli sözcük ve sıfatlar arasına (son sıfatla ad arasına değil); "ve"den önce konmaz; özne, nesne, yüklem arasına gereksiz virgül konmaz, ancak yüklemden uzak düşen özneyi belirtmek ya da özneden sonra gelen sözcükle karışmasını önlemek için özneden sonra virgül konması DOĞRUDUR (Ali, Ayşe ve Veli'yi aradı); hitap ve evet/hayır sonrasına; ara sözün iki yanına; yüklemi ortak cümleler arasına.
- Noktalı virgül: ögeleri arasında virgül bulunan sıralı cümleler arasına. İki nokta: tamamlanmış cümleden sonra açıklama, örnek, sıralama ya da alıntı öncesine, cümle ortasında değil. Yay ayraç: açıklama, (?) kesinsizlik, (!) alay; yüklem gibi temel öge ayraç içine alınmaz. Üç nokta: bitmemiş cümle, sayılabilecek başka örnekler. Soru anlamı taşıyan cümle soru işaretiyle, soru sözcüğü olsa da bilgi veren dolaylı soru noktayla biter.

TÜRKÇE · DİL BİLGİSİ
- Cümlenin olumlu/olumsuz, fiil/isim, kurallı/devrik oluşu yükleme göre belirlenir; fiilimsideki olumsuzluk cümleyi olumsuz yapmaz.
- Fiilimsiler yüklem olmaz: isim-fiil (-mak, -ma, -ış), sıfat-fiil (-an, -dık, -acak, -mış, -ar, -maz), zarf-fiil (-arak, -ınca, -ıp, -ken, -madan). Kalıcı adlaşmış sözcükler (yazı, süpürge, dondurma) fiilimsi değildir.
- Ögeler yükleme soru sorularak bulunur: kim/ne (özne), neyi/ne (nesne), kime/nerede/nereden (dolaylı tümleç), ne zaman/nasıl/ne kadar (zarf tümleci). Edat öbeği (için, gibi, göre, ile) zarf tümlecidir; ara söz ve hitap öge değildir. Edilgen yüklemin öznesi sözde öznedir.
- Ses olayları: her sözcüğü kök + ek diye ayırıp olayları tek tek ara: ünlü düşmesi (ağız → ağzı), ünlü daralması (-yor önünde a/e → ı/i: yaşıyor, bekliyor), ünsüz yumuşaması (-dık + ı → -dığı, kitabı), ünsüz benzeşmesi (-ce → -çe, -de → -te), ünsüz düşmesi (küçük → küçücük). "Hangisi yoktur" sorusunda her olay için metinden bir örnek bulmadan eleme yapma.
- "-ları" çözümlemesi: sahip tekilse çoğul eki + 3. tekil iyelik (onun ihtiyaçları); 3. çoğul iyelik ancak sahip çoğulsa (onların evi = evleri).

SOSYAL
- İklim grafiği: Akdeniz yaz kurak, kış yağışlı; Karadeniz her mevsim yağışlı; karasal kış soğuk, yağış az; muson yaz çok yağışlı, kış kurak; ekvatoral her ay sıcak ve yağışlı; savan yaz yağışlı, kış kurak; çöl yağış çok az.
- Grafikte en sıcak ay Ocak civarındaysa yer Güney Yarım Küre'dedir; mevsimleri buna göre ters düşün.
- Eş eğri haritalarında (izoterm, izobar, izohips) noktanın değeri komşu iki eğri arasında bir aralıktır, eğri üzerindeki nokta eğrinin değerini alır; aynı aralıktaki iki noktayı kesin sıralama.
- Nüfus piramidi: geniş taban → doğum oranı yüksek, genç nüfus fazla; daralan taban → doğum düşüyor; geniş üst basamaklar → yaşlı nüfus fazla.
- Tarih ve felsefe sorularında parçadaki bilgiyle yetin; parçada söylenmeyen ezber cümle cevap değildir. Kronolojide tarihleri yazıp sırala.
- Teşkilât-ı Esasiye (1921): millî egemenlik, güçler birliği, Meclis hükûmeti; laiklik, kabine sistemi ve güçler ayrılığı yoktur.

MATEMATİK
- İstatistik: ortanca = sıralı verinin ortası (veri sayısı çiftse ortadaki iki değerin ortalaması); tepe değer = en sık; açıklık = en büyük − en küçük; birleşik ortalama = toplamların toplamı / toplam kişi.
- Grafik ve tablo: her grafiğin eksen ölçeğini ayrı oku; "kaç katı", "yüzde kaç arttı" ve "ne kadar arttı" farklı sorulardır.
- Dikdörtgenler prizması: hacim abc, yüzey alanı 2(ab + ac + bc).
- Problemlerde birimleri eşitle (dk-sa, cm-m, kuruş-lira); "kaç tane daha / kaç fazla" farkı sorar.
- Sayı problemlerinde bulunan değerin koşullarını (tam sayı, pozitif, rakam, farklı rakam) sına; basamak değeri ile sayı değerini karıştırma.

GEOMETRİ
- Şekil ölçekli değildir; yalnız yazılı değer ve işaretleri kullan. Yamuk alanı = (alt taban + üst taban)/2 · yükseklik; yükseklik tabanlara dik uzaklıktır, yan kenar değildir. Dış açı = komşu olmayan iki iç açının toplamı.
- Üçgen eşitsizliği |b − c| < a < b + c, uçlar dahil değil. Benzerlikte eşit açıların köşelerini aynı sırayla yaz (ADE ∼ ACB olabilir), oranı eşit açıların karşısındaki kenarlarla kur; alan oranı = (benzerlik oranı)².
- İç açıortay karşı kenarı komşu kenarlar oranında böler. Çevre açı gördüğü yayın yarısıdır.

FEN
- "Kesinlikle doğrudur": her olası durumda doğru olmalı. "Doğru olabilir": en az bir durumda mümkün olması yeter. Hal değişimi sırasında ısı alan maddenin sıcaklığı değişmez; ortalama kinetik enerji yalnızca sıcaklığa bağlıdır.
- Yük ve elektriklenme: dokunma ile elektriklenmede toplam yük korunur, yükler sığalarla orantılı paylaşılır; etki ile elektriklenmede yaklaştırılan cismin yükü değişmez.
- Grafik sorularında eğim ve alan anlamını kullan (konum-zaman eğimi hız, hız-zaman eğimi ivme, hız-zaman alanı yer değiştirme; eksenin altındaki alan ters yönde yer değiştirmedir).
- Ağırlık = kütle × g; basınç ve kuvvet hesaplarında kütleyi değil ağırlığı kullan.
- Kaldırma kuvveti: yüzen cisimde ağırlığa eşit, batanda V(cisim) · d(sıvı) · g.
- Deneyde bir etkenin etkisi yalnız o etkenin farklı olduğu düzenekler karşılaştırılarak yorumlanır. Enzim aktivasyon enerjisini düşürür, harcanmaz.
- Kalıtım: erkek X'ini anneden alır (hasta oğlu olan sağlıklı anne taşıyıcıdır); hasta ebeveynlerden sağlıklı çocuk → özellik baskın. "Kesin" yargı her olası genotipte doğru olmalı.
`;
