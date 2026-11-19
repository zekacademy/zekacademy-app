/* Zek AI Türkçe becerisi: yalnız Türkçe sorularında çözüm isteğine eklenir (önbellekte durur).
   17 Kasım 2026 ilk sürüm. Kaynak: Türkçe kör testlerindeki hataların analizi (hata türleri aşağıda) ve
   docs/zek-ai-kilavuz/turkce-*.md. Soru metni kopyalanmaz; 2026 TYT sınav seti (kör test seti) bu dosyaya girmez.
   Hata analizi (model neden yanıldı):
   1) Sözü bağlamdan değil sözlük anlamından/çağrışımından okudu.
   2) "Destekler / örtüşür" sorularında yazarın görüşünü karşı görüşten ya da örnekten ayıramadı; örtük ilkeyi çıkaramadı.
   3) Paragraf yapısında (akış, son cümle, sıralama) gönderim ve bağlaçları sınamadı.
   4) Parçadaki cümlenin başka sözcüklerle söylenmiş hâlini tanımadı; genel doğru bilgiye kaydı.
   5) Dil bilgisi/yazım/noktalama sorularında her birimi tek tek taramadan karar verdi.
   6) Bu hataların çoğunda "eminim" dedi. Bu beceri her şıkkı yazılı olarak etiketletip dayanak ister. */

export const TURKCE_BECERI = `TÜRKÇE BECERİSİ (bu soru Türkçe; aşağıdaki yöntemi adım adım uygula)

ADIM 1 · KÖK: Soru ne istiyor? Tipini belirle: ana düşünce / konu-başlık / ulaşılabilir / ulaşılamaz-değinilmemiş / destekler-örtüşür / boşluk / sıralama / akış bozan / paragraf bölme / anlatım biçimi-düşünceyi geliştirme / söz-sözcük anlamı / dil bilgisi / yazım / noktalama / anlatım bozukluğu. Olumsuz kökü (değildir, yoktur, söylenemez, ulaşılamaz, değinilmemiştir, yanlıştır) büyük harfle not et.

ADIM 2 · PARÇAYI ÇÖZ (paragraf ve anlam sorularında): 'kontrol' alanına kısaca yaz: KONU (ne anlatılıyor), YAZAR GÖRÜŞÜ (yazar neyi savunuyor), KARŞI GÖRÜŞ (yazarın eleştirdiği yaygın düşünce, varsa), BAĞLAÇLAR (ama, oysa, çünkü, bu yüzden, ne var ki, bu nedenle) ve neyi neye bağladıkları. Örnek ya da diyalog varsa: örnek neyi reddediyor, neyi öneriyor? Doğru şık çoğu zaman bu karşıtlığın genel ilkesidir.

ADIM 3 · HER ŞIKKI ETİKETLE ('kontrol' alanına yaz, örnek: "A:YOK B:TERS C:✓(3. cümle) D:ABARTI E:DAR"):
- ✓ = parçada dayanağı var (hangi cümle olduğunu yaz). Dayanak birebir aynı sözcük olmak zorunda değil; aynı anlamın başka sözlerle söylenişi de dayanaktır.
- TERS = parçayla çelişir. YOK = parçada geçmez (gerçek hayatta doğru olsa bile). ABARTI = parçanın söylemediği kesinlik ya da genişlik ekler (çoğu → hepsi, bazen → her zaman). DAR = parçanın yalnız bir bölümünü, bir örneği anlatır. KAYMA = konuya yakın ama başka bir yönü anlatır. KARIŞTIRMA = bir kişinin/metnin görüşünü ötekine yükler.
- Olumlu kökte tek ✓ seçilir; olumsuz kökte dört ✓ bulunur, kalan TERS ya da YOK olan şık cevaptır. İki şık ✓ çıkıyorsa parçayı yeniden oku ve daha kapsayıcı/daha doğrudan dayanağı olanı seç; hâlâ ayıramıyorsan emin=false.
- Etiketi sözcüğe bakarak değil anlama bakarak ver: "her, tüm" içeren şık, parça gerçekten o genişliği anlatıyorsa ✓ olabilir.

ADIM 4 · TİPE ÖZEL KURALLAR
- Ana düşünce: parçanın tamamını kapsayan yazar görüşü; karşıtlık bağlacından sonra gelen yargı genelde odur. Konu/başlık: ne dar (tek örnek) ne geniş.
- Destekler / örtüşür / savunulanlar: önce YAZAR GÖRÜŞÜ'nü tek cümleyle yaz; doğru şık onu başka sözlerle söyler ya da ona kanıt olur. Yazarın çürüttüğü görüşü, konuya yakın genel güzel sözleri ve parçanın hiç işlemediği gerekçeleri ele. Parça zincir kuruyorsa (A ancak B kadar, B ancak C kadar) doğru şık zincirin ilk ve son halkasını bağlar.
- Söz/sözcük anlamı (altı çizili söz, "... sözüyle anlatılmak istenen"): anlamı parçanın kendi açıklamasından çıkar: söz neyle karşılaştırılıyor, yanında hangi niteleme var (kim kurmuş, gönüllü mü zorunlu mu, derin mi yüzeysel mi)? Sözcüğün en bilinen anlamına ya da çağrışımına göre seçme. Sözün yerine şıkkı koyup cümleyi yeniden oku; anlam bozulmuyorsa doğrudur.
- Boşluk doldurma: boşluğun önü ve arkası okunur. Giriş cümlesi öncüle bağlanan sözcük (bu, ancak, ayrıca, böylece) taşımaz. Ortadaki cümle sonraki cümlenin gönderimine (bu, böyle, oysa) uymalı. Son cümle öncekilerden çıkan sonuçtur, çoğu zaman "bu, budur, bu yüzden" ile önceki açıklamaya gönderir; yeni sayı, örnek ya da yan bilgiyle konuyu sürdüren cümle sona gelmez.
- Cümle sıralama: önce başa gelebilecek tek cümleyi bul (kendi başına anlaşılan, gönderim taşımayan); "Çünkü" cümlesi açıkladığı cümlenin hemen ardından, "bu kalıplar, bunlar" gibi gönderme adını veren cümleye bitişir; "Dolayısıyla, kısacası" ile başlayan sonuç cümlesi bütün kanıt ve örneklerden sonra gelir, kanıt zincirini bölmez. Bulduğun sırayı baştan sona okuyarak her göndermeyi sına.
- Akışı bozan cümle: odağı yaz (neyi, hangi yönden). Her adayı çıkarıp sınama yap: çıkarınca sonraki cümle ("Bu nedenle, Bu yüzden" ile başlıyorsa özellikle) öncekine daha sıkı bağlanıyorsa o cümle akışı bozar. Aynı anahtar sözcüğü taşımak cümleyi uygun yapmaz.
- Paragraf bölme: yeni paragraf konu ya da bakış açısı değiştiğinde başlar; öncekine gönderen (bu, bunun, böylece) cümle yeni paragrafı başlatmaz.
- Anlatım biçimi ve düşünceyi geliştirme: tanık gösterme = başkasının sözüne başvurma (yalnız ad geçmesi yetmez); sayısal veri = düşünceyi sayıyla destekleme; örnekleme, karşılaştırma (iki durumu yan yana koyma), benzetme ("gibi"), tanımlama, kişileştirme. "Yoktur" kökünde her yolu parçada tek tek ara.
- Cümle anlamı: neden (-dığı için) / amaç (için, diye) / koşul (-sa) ayrımı; "Yalnızca A olanlar B'dir" = "B olan herkes A'dır". Öznel yargı değer ve beğeni bildirir.

ADIM 5 · DİL BİLGİSİ, YAZIM, NOKTALAMA: KARAR VERMEDEN ÖNCE TARA
- Numaralı cümle/söz sorularında her birimi sırayla ele al ve 'kontrol' alanına her biri için kısa not yaz (I: doğru, II: doğru...). İlk yanlış gibi görüneni bulunca durma; hepsini tara.
- Noktalama: her numaralı cümledeki HER işareti listele ve kuralını sor. Kesme: kişi/yer adına gelen çekim eki kesmeyle ayrılır; kurum, kuruluş, fakülte, bakanlık adlarına gelen ek kesmesiz yazılır (Hukuk Fakültesine); yapım ekinden ve dil adına gelen ekten önce kesme yok. Virgül: eş görevli sözcükler arasına; "ve"den önce yok; yüklemden uzak düşen ya da sonraki sözcükle karışabilecek özneden sonra virgül DOĞRUDUR. Noktalı virgül: ögeleri arasında virgül bulunan sıralı cümleleri ya da virgülle ayrılmış takımları birbirinden ayırır.
- Yazım: "de/da, ki, mi" bağlaç ve ekleri; "-ken, -leyin" bitişik; ses olayına uğrayan birleşik fiil bitişik (hissetmek), uğramayan ayrı (yardım etmek); "her şey, hiçbir şey" ayrı, "birkaç, hiçbir, herhangi" bitişik.
- Ses olayları: her sözcüğü kök + ek diye ayır; ünlü düşmesi (ağzı), ünlü daralması (-yor önünde a/e → ı/i: yaşıyor), ünsüz yumuşaması (-dığı, kitabı), ünsüz benzeşmesi (-çe, -te), ünsüz düşmesi (küçücük). "Yoktur" sorusunda her olay için bir örnek bulmaya çalış; bulunamayan cevaptır.
- Ek ve sözcük türü: "-ları" sahip tekilse çoğul + 3. tekil iyelik (onun ihtiyaçları), sahip çoğulsa 3. çoğul iyelik. Fiilimsiler yüklem olmaz; olumsuzluk ve cümle türü yükleme göre belirlenir. Ögeleri yükleme soru sorarak bul.
- Anlatım bozukluğu: önce yüklemi bul; ortak ögeyi her yüklemle ayrı dene; özne-yüklem uyumu, gereksiz sözcük, yanlış sözcük, mantık hatası, "tarafından" + etken fiil.

ADIM 6 · KARAR VE EMİN: Seçtiğin şıkkın dayanağını ve en yakın rakibin etiketini 'kontrol' alanında yaz. Dayanak cümlesi gösteremiyorsan, iki şık arasında kaldıysan ya da tarama yarım kaldıysa emin=false yap.
`;
