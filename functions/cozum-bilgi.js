/* Zek AI çözüm bilgisi ("beceriler"): her çözüm isteğine eklenir (önbellekte durur, ucuzdur).
   16 Kasım 2026 ilk sürüm: 2026 TYT kör testindeki zayıf noktalardan (Türkçe anlam/paragraf, cümle birleştirme,
   yazım-noktalama; iklim grafiği; istatistik; prizma; "kesinlikle/olabilir" yargı soruları) çıkarıldı.
   17 Kasım 2026: soru havuzunun mantık kartlarından (tuzak türleri), çeldirici sebeplerinden ve bilgi kutularından
   Türkçe paragraf, cümle anlamı, anlatım bozukluğu, yazım-noktalama, dil bilgisi, coğrafya ve fen kuralları eklendi.
   19 Kasım 2026: geometri (üçgen eşitsizliği, benzerlik, açıortay, çevre açı), biyoloji (deney karşılaştırma, enzim, kalıtım),
   kaldırma kuvveti, cümle sıralamada gönderme/sonuç cümlesi; geometri/AYT/biyoloji/fen havuz dalgalarının püf ve çeldiricilerinden.
   Yer açmak için eski maddeler anlam kaybı olmadan kısaltıldı.
   23 Kasım 2026: AYT Matematik 2. dalganın (300 soru) püf ve çeldiricilerinden AYT MATEMATİK bölümü (eşitsizlik, limit,
   türev, integral, olasılık, logaritma, karmaşık, fonksiyon) eklendi; gerçek hata kaydı yoktu. Yer için bazı maddeler kısaltıldı.
   İki günde bir çalışan "Zek AI çözüm eğitimi" görevi bu dosyayı soru havuzundan ve gerçek hatalardan günceller.
   KURAL: 2026 TYT sınav seti (kör test seti) bu dosyaya örnek olarak GİRMEZ. Soru metni kopyalanmaz, yalnız kural yazılır. */
export const KAYNAK_COMMIT = "ea3f1a1a8c77c5f85562432e237f1eb07dd015d8";
export const GUNCELLEME = "2026-11-23";

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
- Boşluk doldurma: giriş cümlesi kendi başına anlaşılır, öncüle bağlanan sözcük (bu, ancak, ayrıca, böylece, söz konusu) taşımaz. Ortadaki cümle hem önceki cümlenin yönüyle hem sonraki cümlenin gönderimiyle (bu, böyle, oysa) uyuşmalı. Son cümle öncekilerden çıkan sonuçtur; konuyu yeni sayı, örnek ya da yan bilgiyle sürdüren cümle sona gelmez.
- Cümle sıralama ve paragraf bölme: zamir ya da bağlaçla öncekine bağlı cümle başa gelmez ve yeni paragrafı başlatmaz; birbirine gönderen cümleler ardışıktır ("Çünkü" açıkladığı cümlenin ardından; "bunlar" adını veren cümleye bitişik). "Dolayısıyla, kısacası" ile başlayan sonuç cümlesi kanıt ve örneklerden sonra, çoğu zaman sona gelir. Yeni paragraf konunun ya da bakış açısının değiştiği cümlede başlar.
- Akışı bozan cümle: odağı (neyi, hangi yönden) belirle; aynı anahtar sözcüğü taşısa da odaktan sapan cümle akışı bozar. Sınama: adayı çıkar; sonraki cümle ("Bu nedenle, Böylece") öncekine daha sıkı bağlanıyorsa akışı bozan odur.
- Anlatım biçimleri: açıklama, tartışma (karşı görüşü çürütme), öyküleme (zaman akışı), betimleme; iç içe olabilir.
- Düşünceyi geliştirme yolları: tanık gösterme = başkasının sözüne başvurma (yalnız ad yetmez); sayısal veri = düşünceyi sayıyla destekleme (her sayı değil); benzetme; karşılaştırma; örnekleme; tanımlama; kişileştirme.
- Yeni nesil: tablodaki her değeri kontrol et; iki konuşmacıda görüşün sahibini karıştırma.

TÜRKÇE · CÜMLE VE SÖZCÜK ANLAMI
- Sözcükte ve sözde anlam: anlamı parçanın kendi açıklamasından çıkar (yanındaki karşıtlık, niteleme: neyle karşılaştırılıyor, kim kurmuş, gönüllü mü zorunlu mu). Sözcüğün en yaygın anlamına ya da çağrışımına göre seçme ("yalın" bağlamda "yüzeysel" olabilir, "süssüz" değil).
- Deyim ve atasözü: sözü sadeleştirip özünü çıkar, sonra şıktaki durumun aynı özü taşıyıp taşımadığına bak; ortak sözcüğe değil düşüncenin yönüne göre eşleştir.
- Anlamca özdeş cümle: "Yalnızca A olanlar B'dir" = "B olan herkes A'dır"; tersi ("A olan herkes B'dir") aynı anlama gelmez.
- Neden-sonuç: "-dığı için, yüzünden, -dığından"; amaç-sonuç: "için, diye, amacıyla" (ulaşılmak istenen); koşul: "-sa, -mak şartıyla". Amacı nedenle, koşulu nedenle karıştırma.
- Öznel yargı beğeni, duygu, değer bildirir (bence, güzel, gereksiz), kanıtlanamaz; nesnel yargı doğrulanabilir.
- İki cümlenin birleştirilmesi: iki cümledeki bilgilerin hepsi korunmalı, aralarındaki anlam ilişkisi (neden-sonuç, karşıtlık, zaman sırası, koşul) değişmemeli.

TÜRKÇE · ANLATIM BOZUKLUĞU
- Türler: gereksiz sözcük (geri iade, yaklaşık tahminen); yanlış anlamlı sözcük; özne-yüklem kişi/sayı uyumsuzluğu; ortak öge yanlışlığı (ortak ögenin eki her yüklemle uyumlu olmalı: "kitaba baktı ve okudu" bozuk); ek eksikliği; mantık ve neden-sonuç çelişkisi; sıralama yanlışlığı; karşılaştırılan ögelerin farklı türden olması; "tarafından" ile etken fiil kullanılması (edilgen olmalı).
- Önce yüklemi bul, ortak ögeyi her yüklemle ayrı dene. Vurgu amaçlı tekrar bozukluk değildir.

TÜRKÇE · YAZIM VE NOKTALAMA (TDK)
- Büyük harf: kişi, yer, kurum, millet, dil adlarının her sözcüğü büyük başlar; özel adı tamamlayan "Gölü, Dağı, Bulvarı" da büyük. Belirli tarih bildiren ay ve gün adları büyük (29 Ekim 1923 Pazartesi), belirli tarih yoksa küçük (her pazartesi). Yön adı yer adının parçasıysa büyük (Doğu Anadolu), yön bildiriyorsa küçük (güneye gitti).
- Kesme işareti: özel adlara gelen çekim ekleri kesmeyle ayrılır (Ankara'ya); kurum, kuruluş, kurul adlarına gelen ekler ayrılmaz (Türk Dil Kurumuna, Hukuk Fakültesine); kurum adından sonra kesme varsa yanlıştır. Yapım ekinden sonra ve dil adına gelen ekte kesme yok (Ankaralı, Türkçeyi). Kısaltma ve rakamla yazılan sayıya gelen ek kesmeyle ayrılır ve okunuşa göre seçilir (TDK'ye, 1960'ta, 40'ı).
- Ayrı/bitişik: bağlaç "de/da" ayrı yazılır, hiç "te/ta" olmaz; bulunma eki bitişik, sert ünsüzden sonra "-te/-ta" olur. Bağlaç "ki" ayrı, ilgi "-ki" bitişik (evdeki, dünkü); kalıplaşmış "belki, çünkü, sanki, oysaki" bitişik. Soru eki "mi" ayrı, ona gelen ekler bitişik (geldin mi, mısın). "-ken, -leyin" bitişik. "Ya da, her şey, bir şey" ayrı; "birkaç, hiçbir, herhangi, biraz" bitişik. Ses olayına uğrayan birleşik fiil bitişik (hissetmek), uğramayan ayrı (yardım etmek). Pekiştirme bitişik (masmavi), ikileme ayrı ve araya işaret konmaz (ağır ağır).
- Virgül: sıralı eş görevli sözcük ve sıfatlar arasına (son sıfatla ad arasına değil); "ve"den önce konmaz; özne, nesne, yüklem arasına gereksiz virgül konmaz, ancak uzak düşen özneyi belirtmek ya da karışmayı önlemek için özneden sonra virgül DOĞRUDUR (Ali, Ayşe ve Veli'yi aradı); hitap ve evet/hayır sonrasına; ara sözün iki yanına; yüklemi ortak cümleler arasına.
- Noktalı virgül: ögeleri arasında virgül bulunan sıralı cümleler arasına. İki nokta: tamamlanmış cümleden sonra açıklama, örnek, sıralama ya da alıntı öncesine, cümle ortasında değil. Yay ayraç: açıklama, (?) kesinsizlik, (!) alay; yüklem gibi temel öge ayraç içine alınmaz. Üç nokta: bitmemiş cümle, sürdürülebilecek örnekler. Soru anlamı taşıyan cümle soru işaretiyle, soru sözcüğü olsa da bilgi veren dolaylı soru noktayla biter.

TÜRKÇE · DİL BİLGİSİ
- Cümlenin olumlu/olumsuz, fiil/isim, kurallı/devrik oluşu yükleme göre belirlenir; fiilimsideki olumsuzluk cümleyi olumsuz yapmaz.
- Fiilimsiler yüklem olmaz: isim-fiil (-mak, -ma, -ış), sıfat-fiil (-an, -dık, -acak, -mış, -ar, -maz), zarf-fiil (-arak, -ınca, -ıp, -ken, -madan). Kalıcı adlaşmış sözcükler (yazı, süpürge, dondurma) fiilimsi değildir.
- Ögeler yükleme soru sorularak bulunur: kim/ne (özne), neyi/ne (nesne), kime/nerede/nereden (dolaylı tümleç), ne zaman/nasıl/ne kadar (zarf tümleci). Edat öbeği (için, gibi, göre, ile) zarf tümlecidir; ara söz ve hitap öge değildir. Edilgen yüklemin öznesi sözde öznedir.
- Ses olayları: sözcüğü kök + ek diye ayır: ünlü düşmesi (ağız → ağzı), ünlü daralması (yaşıyor), ünsüz yumuşaması (kitabı), ünsüz benzeşmesi (-de → -te), ünsüz düşmesi (küçücük). "Yoktur" sorusunda her olaya örnek ara.
- "-ları": sahip tekilse çoğul + 3. tekil iyelik (onun ihtiyaçları); sahip çoğulsa 3. çoğul iyelik (onların evi).

SOSYAL
- İklim grafiği: Akdeniz yaz kurak, kış yağışlı; Karadeniz her mevsim yağışlı; karasal kış soğuk, yağış az; muson yaz çok yağışlı, kış kurak; ekvatoral her ay sıcak ve yağışlı; savan yaz yağışlı, kış kurak; çöl yağış çok az.
- En sıcak ay Ocak civarındaysa yer Güney Yarım Küre'dedir.
- Eş eğri haritalarında (izoterm, izobar, izohips) noktanın değeri komşu iki eğri arasında bir aralıktır, eğri üzerindeki nokta eğrinin değerini alır; aynı aralıktaki iki noktayı kesin sıralama.
- Nüfus piramidi: geniş taban → doğum oranı yüksek; daralan taban → doğum düşüyor; geniş üst → yaşlı nüfus fazla.
- Tarih ve felsefede parçadaki bilgiyle yetin; ezber cümle cevap değildir. Kronolojide tarihleri yazıp sırala.

MATEMATİK
- İstatistik: ortanca = SIRALANMIŞ verinin ortası (çift sayıda veride ortadaki ikisinin ortalaması); tepe değer = en sık; açıklık = en büyük − en küçük; birleşik ortalama = toplamların toplamı / toplam kişi (ortalamaların ortalaması değil).
- Grafikte her eksen ölçeğini ayrı oku; "kaç katı", "yüzde kaç arttı", "ne kadar arttı" farklıdır.
- Prizma: hacim abc, yüzey 2(ab + ac + bc). Birimleri eşitle (dk-sa, cm-m); "kaç fazla" farkı sorar.
- Bulunan sayının koşullarını (tam sayı, pozitif, farklı rakam) sına.

AYT MATEMATİK
- Bulduğun kökü tanım koşuluna sok (log: taban > 0, ≠ 1, içi > 0; kareleme yabancı kök üretir; uzunluk pozitif).
- Eşitsizlik: payda kökü çözüme girmez; çift katlı kökte işaret değişmez; negatifle çarpınca yön döner. "Her x için ax² + bx + c > 0" → a > 0, Δ < 0 ("≥ 0" ise Δ ≤ 0).
- Limit sağ-sol limit eşitliğine bağlıdır, f(a)'ya değil; süreklilik = limit = f(a). Payda sıfırken limit sonluysa pay da sıfırdır.
- Türev: kırılma, kopukluk, dikey teğette türev yok. f′ işaret değiştirmiyorsa ekstremum yok. Kapalı aralıkta mutlak uç değer için uç noktaları da hesapla. Normal eğimi = −1/(teğet eğimi). Parçalı fonksiyonda türevlilik: süreklilik + sağ-sol türev eşitliği.
- İntegral: eksen altı integralde negatiftir; alan için kesişimlerde böl, üst − alt al; yol = ∫|v|. Değişken değiştirince sınırları da değiştir; [∫ₐ^g(x) f(t)dt]′ = f(g(x))·g′(x).
- Sayma/olasılık: "en az bir" → 1 − hiç; iadesiz çekimde paydayı güncelle; dairesel dizilişte (n − 1)!; ortak durumu iki kez sayma.
- f⁻¹(b) = a ⇔ f(a) = b. Bileşkede önce içteki değeri bul. iⁿ 4'lü döngü, (1 + i)² = 2i.

GEOMETRİ
- Şekil ölçekli değildir; yalnız yazılı değer ve işaretleri kullan. Yamuk alanı = (alt taban + üst taban)/2 · yükseklik; yükseklik tabanlara dik uzaklıktır, yan kenar değildir. Dış açı = komşu olmayan iki iç açının toplamı.
- Üçgen eşitsizliği |b − c| < a < b + c, uçlar dahil değil. Benzerlikte eşit açıların köşelerini aynı sırayla yaz (ADE ∼ ACB olabilir), oranı eşit açıların karşısındaki kenarlarla kur; alan oranı = (benzerlik oranı)².
- İç açıortay karşı kenarı komşu kenarlar oranında böler. Çevre açı gördüğü yayın yarısıdır.

FEN
- "Kesinlikle doğrudur": her olası durumda doğru olmalı. "Doğru olabilir": en az bir durumda mümkün olması yeter. Hal değişimi sırasında ısı alan maddenin sıcaklığı değişmez; ortalama kinetik enerji yalnızca sıcaklığa bağlıdır.
- Dokunmayla elektriklenmede toplam yük korunur, sığalarla orantılı paylaşılır; etkiyle elektriklenmede yaklaştırılan cismin yükü değişmez.
- Grafikte eğim ve alan: konum-zaman eğimi hız, hız-zaman eğimi ivme, hız-zaman alanı yer değiştirme (eksen altı ters yön).
- Basınç ve kuvvette kütleyi değil ağırlığı (mg) kullan. Kaldırma kuvveti: yüzen cisimde ağırlığa eşit, batanda V(cisim) · d(sıvı) · g.
- Deneyde bir etkenin etkisi yalnız o etkenin farklı olduğu düzenekler karşılaştırılarak yorumlanır. Enzim aktivasyon enerjisini düşürür, harcanmaz.
- Kalıtım: erkek X'ini anneden alır (hasta oğlu olan sağlıklı anne taşıyıcıdır); hasta ebeveynlerden sağlıklı çocuk → özellik baskın. "Kesin" yargı her olası genotipte doğru olmalı.
`;
