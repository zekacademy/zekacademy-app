/* Zek AI çözüm bilgisi ("beceriler"): her çözüm isteğine eklenir (önbellekte durur, ucuzdur).
   16 Kasım 2026 ilk sürüm: 2026 TYT kör testindeki zayıf noktalardan (Türkçe anlam/paragraf, cümle birleştirme,
   yazım-noktalama; iklim grafiği; istatistik; prizma; "kesinlikle/olabilir" yargı soruları) çıkarıldı.
   İki günde bir çalışan "Zek AI çözüm eğitimi" görevi bu dosyayı soru havuzundan ve gerçek hatalardan günceller.
   KURAL: 2026 TYT sınav seti (kör test seti) bu dosyaya örnek olarak GİRMEZ. Soru metni kopyalanmaz, yalnız kural yazılır. */
export const KAYNAK_COMMIT = "";
export const GUNCELLEME = "2026-11-16";

export const COZUM_BILGI = `ÇÖZÜM BECERİLERİ (her soruda uygula):

GENEL
- Önce soru kökünü oku ve olumsuz/özel ifadeyi işaretle: "değildir, yoktur, söylenemez, ulaşılamaz, değinilmemiştir, yanlıştır, en az, en çok, kesinlikle, olabilir". Olumsuz kökte YANLIŞ olanı ararsın.
- Öncüllü sorularda (I, II, III) her öncülü ayrı ayrı doğru/yanlış diye değerlendir; "hangileri" sorusunda doğru olanların hepsi seçilir.
- Bulduğun cevabı soruda verilen her koşula geri koyarak sına. Bir şıkkı seçmeden önce en güçlü rakip şıkkın neden elendiğini bil.
- Hesap sonucu hiçbir şıkka uymuyorsa soruyu ve okuduğun değerleri baştan oku; şıkka zorla uydurma.

TÜRKÇE
- Paragrafta "çıkarılabilir / ulaşılabilir / söylenebilir": parçada açıkça yazan ya da ondan zorunlu olarak çıkan bilgi. Kendi yorumunu, genel doğruları ya da parçadan fazlasını söyleyen şık yanlıştır. "Değinilmemiştir": parçada hiç söz edilmeyen.
- Ana düşünce / asıl anlatılmak istenen: parçanın tamamını kapsayan yargıdır (çoğu zaman giriş ya da sonuç cümlesinde). Parçanın yalnızca bir bölümünü anlatan şık yardımcı düşüncedir.
- Paragrafta boşluk doldurma: boşluktan önceki ve sonraki cümleyle hem konu hem bağlaç (ama, çünkü, bu yüzden) bakımından uyan cümle doğrudur.
- Akışı bozan cümle: konuyu ya da bakış açısını değiştiren cümledir; konuya değinip farklı bir yöne giden cümle de akışı bozar.
- İki cümlenin birleştirilmesi: iki cümledeki bilgilerin hepsi korunmalı, aralarındaki anlam ilişkisi (neden-sonuç, karşıtlık, zaman sırası, koşul) değişmemeli. Bilgi ekleyen, eksilten ya da ilişkiyi tersine çeviren şık yanlıştır.
- Sözcükte anlam: sözcüğün o cümledeki anlamına bak (gerçek, mecaz, yan anlam); sözlükteki ilk anlam değil.
- Anlatım bozukluğu: özne-yüklem uyumsuzluğu, ortak öge yanlışlığı (ekleri farklı ögelerin ortak kullanılması), gereksiz sözcük (anlamca tekrar), yanlış sözcük seçimi, ek eksikliği.
- Büyük harf: kişi, yer, kurum, kuruluş, millet, dil adları ve bunların her sözcüğü büyük başlar; belirli bir tarih bildiren ay ve gün adları büyük yazılır (29 Ekim 1923 Pazartesi), belirli tarih yoksa küçük (her pazartesi). Unvanlar özel addan sonra gelince büyük (Ayşe Hanım). Yön adı yer adının parçasıysa büyük (Doğu Anadolu), değilse küçük (ülkenin doğusu).
- Kesme işareti: özel adlara gelen çekim ekleri kesmeyle ayrılır (Ankara'ya); kurum, kuruluş, gazete ve dergi adlarına gelen ekler ayrılmaz (Türk Dil Kurumuna). Yapım ekinden sonra kesme konmaz (Türklük).
- Ayrı/bitişik: bağlaç olan "de/da", "ki" ve soru eki "mi" ayrı yazılır; ek olan "-de/-da" ve "-ki" bitişik yazılır. "Ki" bağlacı ayrı yazılır ama kalıplaşmış olanlar bitişik: belki, çünkü, sanki, oysaki, mademki, halbuki.
- Noktalama: sıralı eş görevli sözcükler arasına virgül; ögeleri arasında virgül bulunan sıralı cümleler arasına noktalı virgül; açıklama ve örnek öncesine iki nokta; alıntı sözler tırnak içinde; soru anlamı taşıyan cümle sonuna soru işareti.

SOSYAL
- İklim grafiği: yağış rejimine ve sıcaklık farkına bak. Akdeniz: yaz sıcak ve kurak, kış ılık ve yağışlı. Karadeniz: her mevsim yağışlı, sıcaklık farkı az. Karasal: kış soğuk, yaz sıcak, yağış az, en çok ilkbaharda. Muson: yaz çok yağışlı, kış kurak. Ekvatoral: her ay sıcak (yaklaşık 25-27 °C) ve yağışlı. Savan: sıcak, yaz yağışlı kış kurak. Çöl: yağış çok az, günlük sıcaklık farkı büyük.
- Grafikte en sıcak ay Ocak civarındaysa yer Güney Yarım Küre'dedir; mevsimleri buna göre ters düşün.
- Tarih ve felsefe sorularında parçada verilen bilgiyle yetin; parçadaki yargıyı çağın ya da düşünürün genel bilgisiyle karıştırma.

MATEMATİK
- İstatistik: aritmetik ortalama = toplam / sayı; ortanca (medyan) = veriler sıralanınca ortadaki değer, veri sayısı çiftse ortadaki iki değerin ortalaması; tepe değer (mod) = en çok tekrar eden; açıklık = en büyük − en küçük. Sorulan büyüklüğü bulmak için bu tanımlardan denklem kur, şıkları koşullara koyarak kontrol et.
- Dikdörtgenler prizması (a, b, c): hacim = a·b·c, yüzey alanı = 2(ab + ac + bc), yüzlerin alanları ab, ac, bc. Bir yüzün alanı verilirse kalan kenarı hacimden bul, sonra yüzey alanı koşulunu sağlat.
- Problemlerde birimleri eşitle (dakika-saat, cm-m, kuruş-lira); "kaç tane daha / kaç fazla" farkı sorar.
- Sayı problemlerinde bulunan değerin tam sayı, pozitif, rakam olma gibi koşulları sağladığını kontrol et.

FEN
- "Kesinlikle doğrudur": her olası durumda doğru olmalı. "Doğru olabilir": en az bir durumda mümkün olması yeter. Hal değişimi sırasında ısı alan maddenin sıcaklığı değişmez; ortalama kinetik enerji yalnızca sıcaklığa bağlıdır.
- Yük ve elektriklenme: dokunma ile elektriklenmede toplam yük korunur, yükler sığalarla orantılı paylaşılır; etki ile elektriklenmede yaklaştırılan cismin yükü değişmez.
- Grafik sorularında eğim ve alan anlamını kullan (konum-zaman eğimi hız, hız-zaman alanı yer değiştirme).
`;
