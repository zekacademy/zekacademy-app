"""pyapi · 1. parça (0001–0028). Metinler özgündür."""
from _hafif_pyapi import *
def F(b,a,k): return dict(baglac=b,akis=a,konu=k)

# ================= TAMAMLAMA (9) =================
# 0001 giriş · kolay · A
tam('0001','kolay','giris',
 '........ Güneşin ısıttığı deniz ve göl yüzeylerinden yükselen su buharı, yüksek katmanlarda soğuyarak küçük damlacıklara dönüşür. Bu damlacıklar bulutları oluşturur ve yeterince ağırlaştığında yağmur ya da kar olarak yeryüzüne geri düşer. Toprağa karışan su, ırmaklar aracılığıyla yeniden denizlere ulaşır. Bu döngü hiç durmadığı için aynı su, binlerce yıl boyunca yeniden yeniden kullanılır.',
 'Yeryüzündeki su hiçbir zaman tükenmez, yalnızca biçim değiştirir.',
 [('Yağmur, tarım için en değerli doğa olaylarından biridir.',F(True,True,False),'Sonraki cümleler yağmurun tarımdaki değerini değil, suyun dolaşımını anlatır; şık konudan sapar.','dikkat'),
  ('Bu yüzden suyun korunması her yurttaşın görevidir.',F(False,True,True),'“Bu yüzden” kendinden önce bir neden ister; paragrafın ilk cümlesinde gönderme yapacağı bir şey yoktur.','bilgi'),
  ('Denizlerin tuzlu olması, suda çözünmüş minerallerden kaynaklanır.',F(True,True,False),'Tuzluluk, parçanın anlattığı buharlaşma ve yağış dolaşımıyla ilgili değildir; sonraki cümlelere zemin hazırlamaz.','dikkat'),
  ('Yeryüzünde su hızla yok olmakta ve kaynaklar tükenmektedir.',F(True,False,True),'Parça suyun döngüyle yeniden kullanıldığını söyler; şık suyun yok olduğunu söyleyerek parçayla çelişir.','bilgi')],
 'A',('Sonraki cümleler buharlaşma, bulut ve yağış aşamalarını sırayla anlatıyor; son cümle “bu döngü” diyerek toparlıyor.','boşluk → suyun dolaşımına giriş'),
 'Boşluktaki cümle suyun yok olmayıp dolaştığını ilk söyler; sonraki aşamalar bu fikrin ayrıntısı olur.',
 'Parçanın tamamı suyun yolculuğunu anlatıyor; boşluk bu konuyu açan, öncül istemeyen bir cümle olmalı.',
 'Başa gelecek cümle “bu yüzden, ancak” gibi öncül isteyen sözcükler taşımaz ve parçanın konusunu açar.')

# 0002 giriş · orta · C
tam('0002','orta','giris',
 '........ Kulak, art arda gelen sesler arasındaki süre kalıbını fark ettiğinde beyin bir sonraki vuruşu önceden kestirmeye başlar. Bu tahmin doğru çıktığında hoşnutluk, beklenmedik bir vuruş geldiğinde ise şaşkınlık duyarız. Bestecinin ustalığı, dinleyeni bu iki duygu arasında gezdirmesinde yatar. Dolayısıyla ritim, müzikte yalnızca zamanı bölmekle kalmaz, dinleyicinin beklentisini de yönetir.',
 'Ritim, farkında olmasak da zihnimizi sürekli çalıştıran bir unsurdur.',
 [('Dolayısıyla müziğin en önemli öğesi ezgidir ve ritim ikinci planda kalır.',F(False,False,True),'“Dolayısıyla” bir sonuç bildirir ama ilk cümlede dayanacağı bir şey yoktur; üstelik ritmi ikinci plana atarak parçayla çelişir.','bilgi'),
  ('Davul, tarihte ilk kullanılan çalgılardan biridir.',F(True,True,False),'Çalgının tarihçesi parçanın konusu değildir; sonraki “vuruşu kestirmek” cümlesine zemin hazırlamaz.','dikkat'),
  ('Ritim duygusu bazı insanlarda hiç gelişmez ve onlar müzikten zevk alamaz.',F(True,False,False),'Parça dinleyicinin beklentisini ve duygularını genel olarak anlatır; şık dinleyiciyi dışlayıp konudan sapar.','dikkat'),
  ('Ancak bestecilerin çoğu ritmi göz ardı ederek yalnızca ezgi üzerinde çalışır.',F(False,False,True),'“Ancak” öncesinde bir yargı ister; ayrıca son cümledeki “ritim … beklentiyi yönetir” düşüncesiyle çelişir.','bilgi')],
 'C',('Sonraki cümleler kulağın kalıbı fark etmesini ve beynin vuruşu önceden kestirmesini anlatıyor; son cümle ritmin beklentiyi yönettiğini söylüyor.','boşluk → ritmin zihinsel etkisi'),
 'Boşluktaki cümle ritmi zihinsel bir etkinlik olarak tanıtır; “kestirmeye başlar” ve “beklentisini yönetir” ifadeleriyle tutarlıdır.',
 'Boşluktan sonraki cümleler ritmin zihinde neye yol açtığını anlatıyor; ilk cümle bu konuyu açmalı.',
 'Giriş cümlesi, parçanın geri kalanında ayrıntısı verilen kavramı öncül istemeden tanıtır.')

# 0003 giriş · zor · E
tam('0003','zor','giris',
 '........ Zihin, kendisine ulaşan binlerce uyarandan çoğunu daha ilk anda eler; geriye kalanların bir bölümünü kısa süre tutar, çok azını ise kalıcı belleğe yerleştirir. Bu eleme, bir kusur olmaktan çok bir hayatta kalma düzeneğidir. Her ayrıntıyı saklayan bir zihin, önemli olanı önemsizden ayırmakta zorlanır ve karar vermekte gecikir. Üstelik unutulan şey, çoğu zaman gerçekten kaybolmaz; uygun bir ipucuyla yeniden çağrılabilir. Demek ki unutmak, hatırlamanın karşıtı değil, onun işleyişinin bir parçasıdır.',
 'Unutmak, çoğu zaman sanıldığı gibi belleğin başarısızlığı değildir.',
 [('Okul başarısı, büyük ölçüde ezberleme gücüne bağlıdır.',F(True,True,False),'Ezber ve okul başarısı parçada geçmez; sonraki cümleler elemeyi anlatır, şık bu odağa zemin hazırlamaz.','dikkat'),
  ('Unutmak, belleğin en ciddi hastalıklarından biridir.',F(True,False,True),'Parça unutmayı bir düzenek ve işleyişin parçası sayar; şık unutmayı hastalık sayarak parçayla çelişir.','bilgi'),
  ('Kalıcı bellek, kısa süreli bellekten çok daha geniş bir kapasiteye sahiptir.',F(True,False,True),'Parça, kalıcı belleğe “çok azının” yerleştiğini söyler; şık geniş kapasite diyerek bu yargıyla çelişir.','bilgi'),
  ('Yaşlandıkça unutkanlık artar ve insan yalnızca eski anılarıyla yaşar.',F(True,True,False),'Yaşlılık ve unutkanlığın artışı parçanın odağı değildir; sonraki cümlelerdeki eleme düşüncesine bağlanmaz.','dikkat')],
 'E',('Sonraki cümleler elemeyi bir kusur değil düzenek olarak anlatıyor; son cümle “unutmak … işleyişinin parçasıdır” diyor.','boşluk → unutmanın yeniden değerlendirilmesi'),
 'Boşluktaki cümle unutmayı “başarısızlık sanılan” bir durum olarak açar; sonraki cümleler bunun neden öyle olmadığını gösterir ve son cümle aynı görüşü sonuçlandırır.',
 'Parçanın son cümlesi unutmaya nasıl baktığını söylüyor; ilk cümle bu bakışın karşısındaki yaygın görüşü açabilir.',
 'Girişte yaygın bir yanlış kanıyı anıp parçanın devamında düzelten cümle çoğu kez doğru akışı kurar.')

# 0004 orta(ortada) · kolay · B
tam('0004','kolay','orta',
 'Arılar, nektar toplamak için çiçekten çiçeğe konarken vücutlarına yapışan poleni farkında olmadan taşır. ........ Polen, çiçeğin dişi organına ulaşınca tohumun ve meyvenin oluşması başlar. Tarlalarda ve bahçelerde arı sayısı azaldığında bu süreç aksar. Bu yüzden meyve ve sebze verimi de düşer. Arıları korumak, sofralarımızdaki çeşitliliği korumak anlamına gelir.',
 'Bu taşıma, birçok bitkinin döllenmesi için vazgeçilmez bir işlemdir.',
 [('Oysa arılar yalnızca bal yapmak için çalışır ve bitkilere hiçbir yararı yoktur.',F(False,False,True),'“Oysa” bir karşıtlık bildirir; ayrıca şık, arıların bitkilere yararı olmadığını söyleyerek sonraki cümlelerle çelişir.','bilgi'),
  ('Arıların ürettiği bal, besin değeri yüksek bir gıdadır.',F(True,True,False),'Bal parçanın konusu değildir; sonraki “Polen” cümlesiyle bağ kurmaz.','dikkat'),
  ('Polenin taşınması, bitkiler için bir zarar doğurur.',F(True,False,True),'Sonraki cümlelere göre polen tohum ve meyve oluşumunu sağlar; şık bu düşünceye ters düşer.','bilgi'),
  ('Bu yüzden arılar kışın kovanlarından hiç çıkmaz.',F(False,True,True),'“Bu yüzden” bir neden–sonuç bağı kurar ama polen taşımasının sonucu arıların kışın kovanda kalması değildir; bağlaç boşa düşer.','dikkat')],
 'B',('Önce arıların poleni “farkında olmadan taşıdığı” söyleniyor; sonra “Polen … ulaşınca” diyerek bu poleni ele alan cümle geliyor.','boşluk → taşımanın bitki için önemi'),
 '“Bu taşıma” ifadesi önceki cümledeki polen taşımasını gösterir; cümle sonraki “Polen … tohumun ve meyvenin oluşması” cümlesine de yol açar.',
 'Boşluğun önünde “taşır”, arkasında “Polen” var; boşluk bu taşımanın ne işe yaradığını söylemeli.',
 'Ortadaki boşlukta cümle hem önceki cümleye gönderme yapmalı hem sonrakine zemin hazırlamalıdır.')

# 0005 orta(ortada) · orta · D
tam('0005','orta','orta',
 'Öğrenciye verilen ödevin amacı, derste anlatılanı pekiştirmektir. ........ Ödev yığıldıkça öğrenci onu bir yük olarak görmeye başlar ve işi savsaklar. Neden yaptığını bilmediği işe kimse gönülden bağlanmaz. Oysa az ama düşünülerek hazırlanmış bir ödev, öğrencinin konuyu kendi başına çözmesini sağlar. Bu nedenle ödevde ölçü, yazılan sayfa sayısı değil, kazanılan beceridir.',
 'Ne var ki bu amaç, ödevin sayısı arttıkça kendiliğinden gerçekleşmez.',
 [('Bu yüzden öğretmenler ödev vermekten tümüyle vazgeçmelidir.',F(False,False,True),'“Bu yüzden” ilk cümlenin sonucu olamaz; üstelik parça ödevi bırakmayı değil, ölçülü tutmayı savunur.','bilgi'),
  ('Çünkü ödev, öğrenciyi sınav kaygısından ve ders stresinden tamamen kurtarır.',F(True,False,False),'Parçada sınav kaygısından söz edilmez ve sonraki cümledeki “yük” düşüncesiyle çelişir.','dikkat'),
  ('Öğrencilerin çoğu en çok matematik ödevinden şikâyet eder.',F(True,True,False),'Hangi dersten şikâyet edildiği parçanın odağı değildir; sonraki “yığıldıkça” cümlesine bağlanmaz.','dikkat'),
  ('Bu nedenle ödev, öğrenci için asla bir yük sayılmamalıdır.',F(True,False,True),'Sonraki cümle ödev yığıldığında yük olduğunu söyler; şık bununla çelişir.','bilgi')],
 'D',('Önce ödevin amacı olumlu anlatılıyor; sonra “yığıldıkça … yük” diyen olumsuz bir durum geliyor.','boşluk → olumludan olumsuza geçiş'),
 '“Ne var ki” amaçtan sapmaya geçişi sağlar; sonraki “yığıldıkça yük olur” cümlesi bu karşıtlığın açıklamasıdır.',
 'Boşluğun öncesi olumlu, sonrası olumsuz bir durum anlatıyor; aradaki geçişi sağlayan cümleyi ara.',
 'Önceki cümle olumlu, sonraki olumsuzsa boşluğa karşıtlık bildiren bir cümle gelir.')

# 0006 orta(ortada) · orta · A
tam('0006','orta','orta',
 'Kent merkezlerinde araç trafiği arttıkça yayalar kaldırımlardan ve meydanlardan uzaklaşıyor. ........ Oysa yaya dostu sokaklara sahip kentlerde esnaf daha çok kazanıyor, insanlar birbirini daha sık görüyor ve mahalle bilinci güçleniyor. Bu yüzden kent planlamasında ilk soru, araçlar nereden geçecek diye değil, insanlar nerede yürüyecek diye sorulmalıdır.',
 'Bu durum, kentleri yaşanan yerler olmaktan çıkarıp geçilen yerlere dönüştürüyor.',
 [('Yaya dostu sokaklar, kentlerin hava kalitesini ve gürültü düzeyini de olumlu etkiler.',F(False,False,True),'Sonraki “Oysa” bir karşıtlık ister; önceki cümle olumsuz olduğu için olumlu bir yargı karşıtlığı bozar.','bilgi'),
  ('Çünkü yayalar trafik kurallarına uymakta gönüllü davranmıyor.',F(False,False,False),'Parça yayaları suçlamaz; kaldırımlardan uzaklaşmanın nedeni araç trafiğidir. Şık parçayla çelişir.','bilgi'),
  ('Kentlerde yaşayanların sayısı her yıl artmaktadır.',F(False,True,False),'Nüfus artışı parçanın odağı değildir ve sonraki “Oysa” karşıtlığına zemin hazırlamaz.','dikkat'),
  ('Bu nedenle araç sahibi olmak artık kimse için bir gereklilik sayılmaz.',F(True,False,False),'Parça araç sahipliğinden değil, yayaların kentten uzaklaşmasından söz eder; sonuç çıkarımı parçada yoktur.','dikkat')],
 'A',('Önce yayaların uzaklaştığı söyleniyor; sonra “Oysa” ile yaya dostu kentlerin yararları sıralanıyor.','boşluk → olumsuz durumun sonucu'),
 '“Bu durum” önceki cümledeki yayaların uzaklaşmasına gönderme yapar; olumsuz bir sonuç bildirdiği için “Oysa” ile başlayan olumlu cümleye karşıtlık hazırlar.',
 '“Oysa” ile başlayan cümle yararları anlatıyor; demek ki boşluk bir zarar ya da olumsuz durum bildirmeli.',
 'Boşluktan sonra “oysa” geliyorsa boşluktaki cümle genellikle olumsuz ya da yanlış bir durumu dile getirir.')

# 0007 sonuç · orta · C
tam('0007','orta','sonuc',
 'Şiirde bir sözcüğün anlamı, sözlükteki karşılığından ibaret kalmaz. Aynı sözcük, yanına geldiği öteki sözcüklere ve cümlenin ritmine göre başka bir ağırlık kazanır. Dizenin sonunda bekleyen bir ad ya da başında duran bir sıfat, okurda bambaşka çağrışımlar uyandırabilir. Bu yüzden şair, sözcüğü seçerken yalnızca anlamına değil, sesine ve çağrışımlarına da bakar. ........',
 'Kısacası şiirde sözcük, içinde bulunduğu bütünle birlikte anlam kazanır.',
 [('Bu nedenle şiir okurken sözlüğe başvurmak hiçbir zaman yararlı olmaz.',F(True,False,True),'Parça sözlük anlamının “yetmediğini” söyler, “yararsız” olduğunu değil; şık aşırı bir genellemedir.','bilgi'),
  ('Her okur, bir şiirdeki sözcüğün anlamını tamamen aynı biçimde kavrar.',F(True,False,False),'Parça anlamın bağlama göre değiştiğini söyler; herkesin aynı kavradığı yargısı parçada yoktur ve çelişir.','bilgi'),
  ('Şiirde kullanılan sözcük sayısı arttıkça şiirin değeri de aynı oranda artar.',F(True,True,False),'Sözcük sayısı ile şiirin değeri arasındaki ilişki parçada hiç geçmez; yargı konu dışıdır.','dikkat'),
  ('Şairler, sözcüğün sesine bakmaktan çoğu zaman vazgeçmelidir.',F(True,False,True),'Parça şairin sese de baktığını söyler; şık bu görüşe ters düşer.','bilgi')],
 'C',('Parça sözcüğün anlamının bağlamla, ritimle, sesle ve çağrışımla değiştiğini söylüyor.','sonuç: anlam bağlama bağlı'),
 'Sonuç cümlesi, parçadaki üç yargının ortak sonucunu verir: anlam, sözcüğün içinde bulunduğu bütünle belirlenir.',
 'Parçadaki bütün cümleler sözcüğün tek başına değil, başka bir şeyle birlikte anlam kazandığını söylüyor.',
 'Sonuç cümlesi parçadaki yargıların ortak paydasını verir; parçada olmayan aşırı iddialar getirmez.')

# 0008 sonuç · orta · E
tam('0008','orta','sonuc',
 'Koşuya yeni başlayanların en sık yaptığı hata, ilk günden hızlı gitmeye çalışmaktır. Oysa vücut, yük altında ancak yavaş yavaş uyum sağlar. Kaslar güçlenmeden hız artırılırsa sakatlık kaçınılmaz olur. Düzenli ama ölçülü bir tempoyla ilerleyen koşucu ise haftalar sonra hem daha uzun hem daha rahat koşabildiğini fark eder. ........',
 'Dolayısıyla koşuda kalıcı başarının anahtarı, hız değil sabırdır.',
 [('Bu yüzden her koşucu, haftanın her günü en az üç saat antrenman yapmalıdır.',F(True,False,False),'Parçada süre ya da yoğunluk önerisi yoktur; tersine ölçülü tempo öğütlenir.','bilgi'),
  ('Sakatlanan koşucular bir daha asla koşuya dönemez.',F(True,False,True),'Parça sakatlığın nedenini söyler, sonucunun kalıcılığını değil; “asla” ifadesi aşırı bir genellemedir.','bilgi'),
  ('Hızlı koşan kişi her zaman daha sağlıklı bir vücuda sahiptir.',F(True,False,True),'Parça hıza erken yüklenmeyi sakıncalı bulur; şık parçanın görüşüne ters düşer.','bilgi'),
  ('Koşu ayakkabısının fiyatı, başarıyı doğrudan belirler.',F(True,True,False),'Ayakkabı fiyatı parçada geçmez; sonuç cümlesi parçadan çıkmalıdır.','dikkat')],
 'E',('Parça acele edenin sakatlandığını, ölçülü ilerleyenin ise başarılı olduğunu söylüyor.','sonuç: hız değil sabır'),
 '“Dolayısıyla” öncekilerden çıkan sonucu bildirir: acele sakatlık getirir, ölçülü tempo başarı getirir; yani anahtar sabırdır.',
 'Parça hızı eleştirip ölçülü ilerleyeni över; sonuç cümlesi bu karşılaştırmanın hükmünü vermeli.',
 'Son boşlukta “dolayısıyla, kısacası” gibi bir bağlaçla parçanın hükmünü toparlayan cümle aranır.')

# 0009 sonuç · zor · B
tam('0009','zor','sonuc',
 'Çeviri, bir metni sözcük sözcük başka bir dile aktarmak sanıldığında büyük bir yanılgıya düşülür. Her dil dünyayı kendi kategorileriyle bölümler; bir dilde tek sözcükle dile gelen bir duygu, ötekinde ancak uzun bir tümceyle karşılanabilir. Çevirmen bu yüzden sözlük karşılığıyla yetinemez; metnin tonunu, ritmini ve kültürel çağrışımlarını da taşımak zorundadır. Ne var ki bu taşıma hiçbir zaman tam olmaz; kazanılan her yakınlık, başka bir yerde küçük bir yitime yol açar. İyi çeviri, aslına eksiksiz denk düşen çeviri değil, yitirdiğini en az yitiren çeviridir. ........',
 'Demek ki çevirmen kusursuzluğu değil, katlanılabilir yitimi aramalıdır.',
 [('Dolayısıyla çevirmen, kaynak metnin tonunu korumayı bırakıp okurun kolay anlamasına öncelik vermelidir.',F(True,False,True),'Parça tonu ve çağrışımı taşımayı çevirmenin zorunluluğu sayar; şık bu görüşü terk etmeyi önerir.','bilgi'),
  ('Böylece iki dil arasındaki anlam farkları, yeterli çabayla tümüyle giderilebilir.',F(True,False,True),'Parça taşımanın “hiçbir zaman tam olmadığını” söyler; şık bununla doğrudan çelişir.','bilgi'),
  ('Kısacası her çeviri, aslına yaklaştıkça okur için daha anlaşılır olur.',F(True,False,True),'Parçaya göre aslına yakınlık başka yerde yitime yol açar; yakınlığın anlaşılırlığı artırdığı parçada yoktur.','dikkat'),
  ('Demek ki çevirmenin asıl işi, kültürel çağrışımları yalnızca dipnotla açıklamaktır.',F(True,True,False),'Parçada dipnottan söz edilmez; çağrışımların metinle birlikte taşınması istenir.','dikkat')],
 'B',('Parça önce çevirinin sözcük aktarımı olmadığını, sonra taşımanın hiçbir zaman tam olmadığını, son olarak iyi çevirinin yitimi en azaltan çeviri olduğunu söylüyor.','sonuç: kusursuzluk yok, en az yitim'),
 'Sonuç cümlesi “yitirdiğini en az yitiren” ölçütüne dayanır: kusursuzluk yerine katlanılabilir yitim aranır; hiçbir yargı parçanın söylediğinden fazlasını içermez.',
 'Parçanın son yargısı kusursuz çevirinin olmadığını söylüyor; sonuç cümlesi bu görüşü çevirmenin tutumuna dönüştürmeli.',
 'Sonuç cümlesi, parçanın son yargısını bozmadan onun doğal çıkarımını verir; yeni iddia getirmez.')

# ================= AKIŞ BOZAN (6) =================
# 0010 · kolay · II → B
akis('0010','kolay',
 ['Kütüphaneler, yalnızca kitap saklanan yerler değil, aynı zamanda insanların bir arada sessizce çalıştığı ortak alanlardır.',
  'Kitap fiyatları son yıllarda belirgin biçimde artmış ve baskı sayıları düşmüştür.',
  'Bu ortamda öğrenci, evdeki dikkat dağıtıcı şeylerden uzaklaşıp derse yoğunlaşabilir.',
  'Kütüphane çalışanları da okuyucuya aradığı kaynağı bulmada yol gösterir.',
  'Bu nedenle kütüphane, bir toplumun öğrenme alışkanlığını besleyen en kalıcı kurumlardan biridir.'],
 [('konuyu tanıtır',''),('sapma',''),('“Bu ortamda” ile I. cümledeki ortak çalışma alanına bağlanır','Bu ortamda'),('kütüphanenin bir başka işlevini anlatır',''),('“Bu nedenle” ile sonuç verir','Bu nedenle')],
 1,'Parça, kütüphanenin insanlara ve topluma sağladığı yararı anlatıyor.',
 'II. cümle kitap fiyatlarından ve baskı sayılarından söz eder; kütüphanenin işleviyle ilgisi yoktur.',
 'II. cümle çıkarılınca I’deki “ortak alan” ile III’teki “Bu ortamda” doğrudan bağlanır; akış kesintisiz sürer.',
 'Önce parçanın odağını tek cümleyle söyle: kütüphane ne işe yarıyor?',
 'Odağa hizmet eden cümleler zamir ve bağlaçlarla birbirine bağlanır; zincirin dışında kalan cümle akışı bozandır.')

# 0011 · kolay · IV → D
akis('0011','kolay',
 ['Uyku, bedenin dinlendiği bir boşluk değil, birçok onarım işinin yapıldığı etkin bir süreçtir.',
  'Gece boyunca kaslar kendini yeniler ve gün içinde yıpranan dokular onarılır.',
  'Beyin de bu sürede öğrendiklerini düzenler ve önemli olanları kalıcı belleğe aktarır.',
  'Bazı insanlar sabahın erken saatlerinde, bazıları ise akşam geç saatlerde daha üretken çalışır.',
  'Bu yüzden yeterince uyumayan biri hem bedensel hem zihinsel olarak daha çabuk yorulur.'],
 [('konuyu tanıtır',''),('uykuda bedenin onarımını anlatır',''),('“Beyin de” ile uykunun zihinsel işlevini ekler','Beyin de'),('sapma',''),('“Bu yüzden” ile önceki işlevlerin sonucunu verir','Bu yüzden')],
 3,'Parça, uykunun beden ve zihin için işlevlerini anlatıyor.',
 'IV. cümle insanların hangi saatte daha üretken çalıştığını söyler; uykunun işleviyle ilgili değildir.',
 'IV. cümle çıkarılınca III’teki işlev ile V’teki “Bu yüzden” sonucu doğrudan bağlanır.',
 'Parçanın odağı uykunun ne işe yaradığıdır; her cümle bu soruya yanıt veriyor mu?',
 'Bir cümle konuyla ilgili görünse de yanıtladığı soru farklıysa akışı bozar.')

# 0012 · orta · III → C
akis('0012','orta',
 ['Yabancı dil öğrenmenin en etkili yollarından biri, öğrenilen dilde sık sık okumaktır.',
  'Okurken karşılaşılan sözcükler, cümlenin içinde anlam kazandığı için sözlük listelerinden çok daha kolay akılda kalır.',
  'Sözlükler, günümüzde artık çoğunlukla elektronik ortamda kullanılan başvuru kaynaklarıdır.',
  'Üstelik okuma, dilin yazım ve cümle kuruluşuyla öğrencinin fark etmeden tanışmasını sağlar.',
  'Bu nedenle öğrenciye ilk günlerden itibaren düzeyine uygun kısa metinler okutmak yararlıdır.'],
 [('konuyu tanıtır',''),('okumanın yararı: sözcüğü bağlamda öğretir',''),('sapma',''),('“Üstelik” ile okumanın bir başka yararını ekler','Üstelik'),('“Bu nedenle” ile okumanın yararlarından sonuç çıkarır','Bu nedenle')],
 2,'Parça, yabancı dil öğrenmede okumanın yararlarını anlatıyor.',
 'III. cümle “sözlük” sözcüğünü paylaşsa da sözlüklerin hangi ortamda kullanıldığını söyler; okumanın yararlarıyla ilgisi yoktur.',
 'III. cümle çıkarılınca II’deki okumanın yararına IV’teki “Üstelik” ile yenisi eklenir; akış bozulmaz.',
 'Parçanın odağı “okumanın yararı”; yalnızca ortak sözcük taşıyan cümleye aldanma.',
 'Aynı anahtar sözcüğü taşımak, cümlenin parçanın odağına hizmet ettiğini göstermez.')

# 0013 · orta · V → E
akis('0013','orta',
 ['Mercan kayalıkları, okyanus tabanının çok küçük bir bölümünü kaplamalarına karşın sayısız deniz canlısına yuva olur.',
  'Kayalıkların girintili çıkıntılı yapısı, küçük balıklara büyük avcılardan saklanacak yerler sağlar.',
  'Bu yüzden kayalıklar bozulduğunda onlara bağlı balık türlerinin sayısı da hızla azalır.',
  'Kayalıkta yaşayan canlılar birbirinin atığından beslenerek zengin bir besin ağı kurar.',
  'Kayalıkların renkli görüntüsü, her yıl çok sayıda turistin fotoğraf çekmek için bölgeye akın etmesine yol açar.'],
 [('konuyu tanıtır',''),('kayalığın canlılara sağladığı barınağı anlatır',''),('“Bu yüzden” ile II’deki barınma işlevinin sonucunu verir','Bu yüzden'),('kayalıktaki canlıların besin ağını anlatır',''),('sapma','')],
 4,'Parça, mercan kayalıklarının deniz canlıları için ekolojik önemini anlatıyor.',
 'V. cümle kayalıkların turistik çekiciliğinden söz eder; canlılar için taşıdığı önemle ilgisi yoktur.',
 'V. cümle çıkarılınca parça kayalığın yuva ve besin ağı işleviyle bütünlüğünü korur.',
 'Parçanın odağı kayalığın canlılar için ne anlama geldiği; turizm, fotoğraf gibi konulara dikkat et.',
 'Bir parça belli bir yönden (ekolojik, ekonomik, sanatsal) ele alınmışsa o yönün dışına çıkan cümle akışı bozar.')

# 0014 · zor · IV → D
akis('0014','zor',
 ['Yaratıcılığın sınırsız özgürlükte doğduğu sanılır; oysa sınırlar, çoğu zaman yaratıcı düşünceyi tetikleyen asıl etkendir.',
  'Kafiye ve ölçü gibi katı kalıplara bağlı bir şair, anlatmak istediğini ister istemez alışılmadık sözcüklerle ve yeni imgelerle kurmak zorunda kalır.',
  'Benzer biçimde yalnızca üç rengi olan bir ressam, elindeki sınırlı malzemeden en çarpıcı etkiyi çıkarmanın yollarını arar.',
  'Yaratıcı kişilerin ürünleri çoğu zaman kendi dönemlerinde değil, sonraki kuşaklar tarafından değerlendirilir.',
  'Demek ki kısıt, düşünceyi daraltan bir duvar değil, onu zorlayıp yeni yollara iten bir basamak olabilir.'],
 [('ana iddiayı (sınır yaratıcılığı tetikler) açar','oysa'),('iddiaya şiirden örnek verir',''),('“Benzer biçimde” ile II’deki örneğe ressamdan ikinci örnek ekler','Benzer biçimde'),('sapma',''),('“Demek ki” ile I–III’ten sonuç çıkarır','Demek ki')],
 3,'Parça, kısıtların yaratıcılığı engellemek yerine tetiklediğini örneklerle savunuyor.',
 'IV. cümle “yaratıcı kişiler” sözleriyle konuya yakın görünür; ama ürünlerin ne zaman değerlendirildiğini anlatır, kısıtın yaratıcılığa etkisini değil.',
 'IV. cümle çıkarılınca iki örnek (şair, ressam) hemen ardından “Demek ki” sonucuna bağlanır; düşünce kesintisiz ilerler.',
 'Parçanın savunduğu iddia ne? Örnekler ve sonuç bu iddiaya bağlanıyor mu?',
 'Konuya aynı sözcüklerle yaklaşan ama iddiayı ne destekleyen ne de sonuçlandıran cümle akışı bozar.')

# 0015 · zor · II → B
akis('0015','zor',
 ['Günlük hayatın gürültüsü, kulağı yoran bir rahatsızlık olmanın ötesinde bedeni de sürekli diken üstünde tutar.',
  'Sessizlik, birçok kültürde erdem sayılmış ve bilgelerin ortak özelliği olarak anılmıştır.',
  'Sürekli yüksek sesle karşılaşan insanın kalp atışı hızlanır ve stres hormonları artar.',
  'Bu etki, uyku sırasında bile sürer; kişi uyanmasa da vücut gürültüye tepki vermeyi bırakmaz.',
  'Dolayısıyla gürültüyü azaltmak, yalnızca konfor için değil, sağlığı korumak için de gerekli bir önlemdir.'],
 [('gürültünün bedene etkisini tanıtır',''),('sapma',''),('I’deki “bedeni diken üstünde tutar” iddiasına bedensel kanıt getirir',''),('“Bu etki” ile III’teki bedensel tepkiyi sürdürür','Bu etki'),('“Dolayısıyla” ile sağlık sonucunu çıkarır','Dolayısıyla')],
 1,'Parça, gürültünün insan bedenine etkisini ve bundan çıkan sonucu anlatıyor.',
 'II. cümle sessizliğin kültürlerdeki saygın yerinden söz eder; gürültünün bedene etkisini değil, sessizliğe verilen değeri anlatır.',
 'II. cümle çıkarılınca I’deki “beden” iddiası III’te kanıtlanır, IV’teki “Bu etki” III’e bağlanır; akış bozulmaz.',
 'Parçanın odağı gürültünün bedene etkisi; sessizlik/gürültü karşıtlığına dair her cümle bu odağa hizmet ediyor mu?',
 'Konunun “karşıtını” öven ya da tarihçesini anlatan cümle, parçanın asıl etki odağından sapmış olabilir.')

# ================= PARAGRAFI İKİYE BÖLME (5) =================
# 0016 · kolay · cut V → D
bolme('0016','kolay',
 ['Demir, nemli havayla temas ettiğinde yüzeyinde kırmızımsı bir tabaka oluşur.',
  'Bu tabakaya pas denir ve pas, demirin yavaş yavaş çürümesine yol açar.',
  'Pasın ilerlemesi, havadaki oksijenle ve suyla doğrudan ilgilidir.',
  'Bu nedenle nemli ortamlarda bırakılan demir parçalar çok daha çabuk bozulur.',
  'Peki demiri pastan korumak için ne yapılabilir?',
  'Yüzeyi boyayarak ya da çinko gibi bir metalle kaplayarak havayla ilişkisini kesmek en yaygın yöntemdir.'],
 [('bas','',''),('devam','Bu tabakaya','“Bu tabakaya” ile I’deki tabakaya bağlanır'),('devam','Pasın','“Pasın” ile II’deki pası sürdürür'),('devam','Bu nedenle','“Bu nedenle” ile III’ün sonucunu verir'),('yeni','Peki','“Peki” sorusuyla pasın oluşumundan korunma yollarına geçilir'),('devam','Yüzeyi','V’teki sorunun yanıtını verir')],
 'İlk dört cümle pasın nasıl oluştuğunu ve neden ilerlediğini anlatıyor.',
 'V ve VI pastan korunma yollarını anlatıyor; konu “neden oluşur” sorusundan “nasıl önlenir” sorusuna geçmiştir.',
 'Pasın oluşumu anlatılırken konu nerede “önlem” e dönüyor? Soru soran ya da yönü değiştiren cümleyi ara.',
 'Yeni paragraf, düşüncenin yönü değiştiğinde başlar; bu çoğunlukla “peki, öte yandan, gelelim” gibi sözcüklerle belli olur.')

# 0017 · orta · cut III → B
bolme('0017','orta',
 ['Kuşların ötüşü, ilk bakışta eş çağırmaya hizmet eden bir davranış gibi görünür.',
  'Gerçekten de erkek kuşlar, üreme mevsiminde en gür seslerini dişileri etkilemek için çıkarır.',
  'Öte yandan aynı ötüşün bölge sınırı belirleme işlevi de vardır.',
  'Bir dalda ötmeye başlayan kuş, komşu erkeklere burasının kendi alanı olduğunu bildirir.',
  'Bu iletiyi anlayan rakip, genellikle sınırı geçmeden geri çekilir.',
  'Böylece kavga edilmeden alan paylaşımı yapılmış olur.'],
 [('bas','',''),('devam','Gerçekten de','“Gerçekten de” ile I’deki eş çağırma işlevini doğrular'),('yeni','Öte yandan','“Öte yandan” ile ötüşün ikinci işlevine (bölge belirleme) geçilir'),('devam','Bir dalda','bölge belirleme işlevinin ayrıntısını verir'),('devam','Bu iletiyi','“Bu iletiyi” ile IV’teki iletiye bağlanır'),('devam','Böylece','“Böylece” ile V’in sonucunu verir')],
 'I ve II ötüşün eş çağırma işlevini anlatıyor.',
 'III–VI ötüşün bölge belirleme işlevini ve sonucunu anlatıyor; iki işlev iki ayrı paragraf oluşturur.',
 'Kuşların ötüşünün kaç ayrı işlevi anlatılıyor? İkincisine geçiş nerede?',
 '“Öte yandan, bir de, ikinci olarak” gibi sözcükler, yeni bir yönün başladığını gösterir.')

# 0018 · orta · cut IV → C
bolme('0018','orta',
 ['Fotoğraf makinesi icat edildiğinde birçok kişi resim sanatının sonunun geldiğini düşündü.',
  'Gerçeği olduğu gibi kaydetme görevi makineye geçince ressamlar bu işten kurtuldu.',
  'Böylece tuvale yalnızca kendilerinin verebileceği renk, biçim ve duyguya daha çok yöneldiler.',
  'Gelelim fotoğrafın kendi gelişimine: ilk dönemlerde fotoğrafçılar da resim gibi sahne kurar, poz verdirirdi.',
  'Zamanla anı yakalama olanağı, fotoğrafı bağımsız bir sanat dalı yaptı.',
  'Bu bağımsızlık, fotoğrafçıların ressamları taklit etmeyi bırakıp kendi diline yönelmesiyle pekişti.'],
 [('bas','',''),('devam','bu işten','I’deki endişeyi yanıtlayarak ressamların durumunu sürdürür'),('devam','Böylece','“Böylece” ile II’nin sonucunu verir'),('yeni','Gelelim','“Gelelim” ile ressamlardan fotoğrafın kendi gelişimine geçilir'),('devam','Zamanla','“Zamanla” ile IV’teki ilk dönemin devamını anlatır'),('devam','Bu bağımsızlık','“Bu bağımsızlık” ile V’teki bağımsız sanat dalına bağlanır')],
 'I–III fotoğrafın ressamlar üzerindeki etkisini anlatıyor.',
 'IV–VI fotoğrafın kendi gelişimini anlatıyor; konu ressamlardan fotoğrafçılara geçmiştir.',
 'İlk üç cümlede kimin durumu anlatılıyor, sonrasında kimin? Konu değişimini işaretleyen sözcüğü bul.',
 '“Gelelim, söz edelim, sıra … da” gibi ifadeler konunun değiştiğini açıkça bildirir.')

# 0019 · orta · cut II → A
bolme('0019','orta',
 ['Koku, duyularımız arasında anıyla en doğrudan bağ kuran duyudur.',
  'Peki bu bağ neden bu kadar güçlüdür?',
  'Koku bilgisini işleyen beyin bölgesi, duyguları ve anıları düzenleyen bölgeyle yan yanadır.',
  'Bu yakınlık, bir kokunun bizi birdenbire çocukluğumuza götürmesini açıklar.',
  'Bu nedenle bir kokuyu yeniden duyduğumuzda anı, çoğu zaman ayrıntılarıyla birlikte canlanır.',
  'Aynı yoğunlukta bir canlanma, görüntü ya da ses yoluyla çok daha seyrek yaşanır.'],
 [('bas','',''),('yeni','Peki','“Peki” sorusuyla iddiadan gerekçeye (neden sorusuna) geçilir'),('devam','yan yanadır','II’deki sorunun yanıtını başlatır'),('devam','Bu yakınlık','“Bu yakınlık” ile III’teki komşuluğa bağlanır'),('devam','Bu nedenle','“Bu nedenle” ile IV’ün sonucunu verir'),('devam','Aynı yoğunlukta','“Aynı yoğunlukta” ile V’teki canlanmayı karşılaştırır')],
 'I, kokunun anıyla bağını bir iddia olarak ortaya koyuyor.',
 'II–VI bu bağın nedenini sorgulayıp açıklıyor; iddia ile gerekçe ayrı paragraflara düşer.',
 'İlk cümle bir iddia; gerekçeye geçişi başlatan soru kalıbını ara.',
 'Bir iddiayı gerekçelendirmeye başlayan “peki” sorusu çoğu kez yeni paragrafın ilk cümlesidir.')

# 0020 · zor · cut IV → C
bolme('0020','zor',
 ['Mizah, çoğu kez alışılmış beklentinin ters yüz edilmesinden doğar.',
  'Dinleyici cümlenin nereye gideceğini kestirirken anlatıcı beklenmedik bir yöne sapar ve aradaki boşluk gülmeye dönüşür.',
  'Bu açıdan bakıldığında iyi bir fıkra, kurallara uyar gibi görünüp en uygun anda onları çiğneyen bir oyundur.',
  'Mizahın toplumsal işlevi ise çoğu zaman bu bilişsel oyunun gölgesinde kalır.',
  'Oysa ortak bir şakaya gülen insanlar, o anda aynı şeyi gülünç bulduklarını fark ederek birbirine yaklaşır.',
  'Bu yakınlık, bir topluluğun üyeleri arasında sözle kurulamayan bir bağın oluşmasına yardım eder.'],
 [('bas','',''),('devam','beklenmedik','I’deki beklenti bozulmasını açıklar'),('devam','Bu açıdan bakıldığında','“Bu açıdan bakıldığında” ile I–II’deki mekanizmayı özetler'),('yeni','toplumsal işlevi ise','“Mizahın toplumsal işlevi ise” ile konu bilişsel mekanizmadan toplumsal işleve geçer'),('devam','Oysa','“Oysa” ile IV’teki toplumsal işlevin gölgede kaldığı yargısına karşı çıkar'),('devam','Bu yakınlık','“Bu yakınlık” ile V’teki yakınlaşmaya bağlanır')],
 'I–III mizahın nasıl oluştuğunu, yani bilişsel mekanizmasını anlatıyor.',
 'IV–VI mizahın toplumsal işlevini anlatıyor; “Oysa” bu yeni konunun içinde bir karşıtlık kurar, konu değiştirmez.',
 'Parçada iki ayrı konu var: mizah nasıl doğar, mizah ne işe yarar? İkinci konuyu ilk kez açan cümleyi bul.',
 '“Oysa, ne var ki” gibi karşıtlık bağlaçları çoğu zaman aynı konunun içindedir; konu değişimini yeni bir kavramın ya da yönün girişi belirler.')

# ================= CÜMLE SIRALAMA (5) =================
S1=['Kahve, kahve ağacının kiraz görünümlü meyvesinin içindeki çekirdekten elde edilir.',
    'Bu meyveler olgunlaşınca elle ya da makineyle toplanır.',
    'Toplanan meyvelerin kabuğu soyulur ve çekirdekler kurutulur.',
    'Kurutulan çekirdekler daha sonra kavrularak bilinen koyu rengini ve kokusunu alır.',
    'Son olarak kavrulmuş çekirdekler öğütülür ve fincana girmeye hazır hâle gelir.']
sira('0021','kolay',S1,
 [('ilk',0,None,'','Konuyu tanıtan, zamir ve bağlaç taşımayan cümle girişe uygundur.'),
  ('hemen',0,1,'Bu meyveler','“Bu meyveler” ifadesi giriş cümlesindeki meyveye gönderme yapar; hemen ardından gelir.'),
  ('once',1,2,'Toplanan','“Toplanan meyveler” önce toplanmış olmalıdır; toplamayı anlatan cümleden sonra gelir.'),
  ('once',2,3,'Kurutulan','“Kurutulan çekirdekler” kurutmayı anlatan cümleden sonra gelir.'),
  ('son',4,None,'Son olarak','“Son olarak” süreci kapatır, en sonda yer alır.')],
 ['giriş: kahvenin nereden elde edildiğini tanıtır','“Bu meyveler” ile giriş cümlesine bağlanır','“Toplanan” ile toplamadan sonra gelir','“Kurutulan” ile kurutmadan sonra gelir','“Son olarak” ile süreci kapatır'],
 1,'C','“Bu meyveler”, “Toplanan”, “Kurutulan”, “Son olarak” ifadeleri cümlelerin yerini belirler.',
 'Hiçbir zamir ya da bağlaç taşımayan, konuyu tanıtan cümleyi ara.','Paragraf, bir şeyin ilk tanıtıldığı cümleyle başlar; zamirli cümleler gönderme yaptıkları cümleden sonra gelir.',101)

S2=['Bir yazıyı düzeltmenin en zor yanı, onu başkası gibi okuyabilmektir.',
    'Çünkü yazar kendi cümlelerini okurken aslında ne yazmak istediğini hatırlar ve eksikleri farkında olmadan tamamlar.',
    'Bu yüzden yazıyı bir süre çekmeceye koyup unutmak, en eski ve etkili yöntemlerden biridir.',
    'Aradan geçen zaman, yazarı kendi metnine yabancı bir okurun gözüyle bakabilecek duruma getirir.',
    'O zaman görülmeyen tekrarlar ve boşluklar bir anda göze çarpar.']
sira('0022','orta',S2,
 [('hemen',0,1,'Çünkü','“Çünkü” 0’daki zorluğun nedenini açıklar; hemen ardından gelir.'),
  ('hemen',1,2,'Bu yüzden','“Bu yüzden” 1’deki nedenin sonucunu (çözüm yolunu) bildirir.'),
  ('hemen',2,3,'Aradan geçen zaman','“Aradan geçen zaman”, çekmeceye koyup unutma süresine gönderme yapar.'),
  ('hemen',3,4,'O zaman','“O zaman”, 3’teki yabancı okur gibi bakabildiği ana gönderme yapar.')],
 ['genel yargı: düzeltmenin zorluğu','“Çünkü” ile zorluğun nedenini açıklar','“Bu yüzden” ile çözüm yolunu bildirir','“Aradan geçen zaman” ile unutma süresini sürdürür','“O zaman” ile sonucu verir'],
 3,'D','“Çünkü” nedeni, “Bu yüzden” sonucu bildirir; “Aradan geçen zaman” ve “O zaman” zamana gönderme yapar.',
 'Zinciri baştan kur: hangi cümle bir zorluğu söylüyor, hangisi ona neden gösteriyor?','Zamir ve bağlaçlı cümleler, gönderme yaptıkları cümlenin hemen arkasına dizilir; çıkış noktası zincirin başıdır.',102)

S3=['Karlı dağların yüksek kesimlerinde kış boyunca yağan kar, yaz mevsiminde tümüyle erimez.',
    'Yıllar içinde üst üste biriken bu kar, kendi ağırlığı altında sıkışarak yoğun bir buza dönüşür.',
    'Kütlesi yeterince büyüyen buz, yer çekiminin etkisiyle yamaçtan aşağı çok yavaş akmaya başlar.',
    'Ancak bu akış, alçak kesimlere ulaşıldığında sıcaklık arttığı için eriyerek son bulur.',
    'Eriyen buzdan oluşan sular ise ırmakları besler.']
sira('0023','orta',S3,
 [('ilk',0,None,'','Kardan söz eden, öncül istemeyen cümle girişe uygundur.'),
  ('hemen',0,1,'bu kar','“bu kar” 0’daki yaz mevsiminde erimeyen kara gönderme yapar.'),
  ('hemen',1,2,'Kütlesi yeterince büyüyen buz','“büyüyen buz”, 1’de oluşan buza gönderme yapar.'),
  ('hemen',2,3,'bu akış','“bu akış” 2’deki akmaya başlamayı gösterir.'),
  ('hemen',3,4,'Eriyen buz','“Eriyen buz” 3’teki erimeye gönderme yapar.')],
 ['giriş: karın erimeden kalmasını anlatır','“bu kar” ile girişe bağlanır','“büyüyen buz” ile buza dönüşmeden sonra gelir','“bu akış” ile akmaya başlamadan sonra gelir','“Eriyen buz” ile erimeden sonra gelir'],
 -2,'A','“bu kar, büyüyen buz, bu akış, Eriyen buz” ifadeleri bir olay zincirini sırayla bağlar.',
 'Olay zincirini kur: kar önce ne oluyor, sonra nasıl bir hâle geliyor?','Aşamalı süreçlerde her cümle, bir öncekinin anlattığı nesneye (“bu kar, bu buz, bu akış”) gönderme yapar.',103)

S4=['Eskiden bir mektubun yazılması, postalanması ve cevabının gelmesi haftalar alırdı.',
    'Bu bekleyiş, yazanın her sözcüğü uzun uzun tartmasına yol açardı.',
    'Günümüzde ise iletiler saniyeler içinde karşı tarafa ulaşıyor.',
    'Hız arttıkça yazılanlara gösterilen özen çoğu zaman azaldı.',
    'Belki de bu yüzden eski mektuplar, bugün birer hatıra olarak saklanıyor.']
sira('0024','orta',S4,
 [('ilk',0,None,'','“Eskiden” ile dönemi başlatan, öncül istemeyen cümle girişe uygundur.'),
  ('hemen',0,1,'Bu bekleyiş','“Bu bekleyiş” 0’daki haftalar süren bekleyişe gönderme yapar.'),
  ('once',1,2,'Günümüzde ise','“Günümüzde ise” eski dönemle karşıtlık kurar; eski dönemi anlatan cümlelerden sonra gelir.'),
  ('hemen',2,3,'Hız arttıkça','“Hız”, 2’deki saniyeler içinde ulaşan iletiye gönderme yapar.'),
  ('once',3,4,'Belki de bu yüzden','“bu yüzden” 3’teki özen azalmasının sonucunu bildirir.')],
 ['giriş: eskiden mektubun gecikmesini anlatır','“Bu bekleyiş” ile girişe bağlanır','“Günümüzde ise” ile eski dönemle karşıtlık kurar','“Hız” ile iletilerin saniyeler içinde ulaşmasına bağlanır','“Belki de bu yüzden” ile sonuç çıkarır'],
 -1,'E','“Eskiden” ile “Günümüzde ise” zaman karşıtlığı kurar; “Hız arttıkça” ve “bu yüzden” ise neden–sonuç bağıdır.',
 'Zaman sözcüklerine (eskiden, günümüzde) ve “bu yüzden” gibi sonuç bildiren bağlaca bak.','Zaman karşıtlığı kuran paragrafta eski dönem önce, yeni dönem sonra anlatılır; sonuç bağlacı taşıyan cümle sondadır.',104)

S5=['Bir toplum yeni bir araç ya da kavramla karşılaştığında, onu adlandırmak için önce var olan sözcüklerden birine başvurur.',
    'Örneğin bilgisayarda imleci yönlendiren küçük aygıt, bir kemirgen adıyla çağrılır.',
    'Böyle bir adlandırma, iki şey arasındaki görünüş ya da işlev benzerliğine dayanır.',
    'Zamanla ilk anlam geri plana çekilir ve sözcük yeni kavramın adı olarak yerleşir.',
    'Dolayısıyla bir dilin söz varlığı, çoğu zaman yeni sözcük türetilerek değil, eski sözcüklere yeni anlamlar yüklenerek genişler.']
sira('0025','zor',S5,
 [('ilk',0,None,'','Genel durumu söyleyen, öncül istemeyen cümle girişe uygundur.'),
  ('once',0,1,'Örneğin','“Örneğin” genel yargıdan sonra gelir; örnek, genel cümleyi izler.'),
  ('hemen',1,2,'Böyle bir adlandırma','“Böyle bir adlandırma”, 1’deki örnek adlandırmaya gönderme yapar.'),
  ('once',2,3,'ilk anlam','“ilk anlam”, 2’deki benzerliğe dayanan ad verme sürecinden sonra geri plana çekilir.'),
  ('son',4,None,'Dolayısıyla','“Dolayısıyla” tüm anlatılandan sonuç çıkarır; en sonda yer alır.')],
 ['giriş: adlandırmada var olan sözcüğe başvurulduğunu söyler','“Örneğin” ile genel yargıya örnek verir','“Böyle bir adlandırma” ile örneği genelleştirir','“ilk anlam” ile benzerliğe dayanan adlandırmanın sonrasını anlatır','“Dolayısıyla” ile sonuç çıkarır'],
 2,'B','“Örneğin”, “Böyle bir adlandırma”, “Zamanla” ve “Dolayısıyla” genel → örnek → genelleme → gelişme → sonuç sırasını kurar.',
 'Genel yargıyı, ona verilen örneği ve örneği genelleyen cümleyi sırayla bul.','Genelden özele giden paragrafta “örneğin” cümlesi genel yargıdan sonra, “dolayısıyla” cümlesi en sonda gelir.',105)

# ================= GİRİŞ CÜMLESİ OLABİLEN / OLAMAYAN (3) =================
# 0026 · kolay · olabilir · D
giris('0026','kolay','olabilir',
 ('Şehir yaşamında insanın doğayla ilişkisi giderek zayıflamaktadır.',''),
 [('Ancak bu durum çocukların oyun alışkanlıklarını da değiştirmiştir.','Ancak','“Ancak” ve “bu durum” öncede anlatılmış bir şeye dayanır; paragrafı başlatamaz.','bilgi'),
  ('Ayrıca ormanların azalması hava kalitesini de düşürmüştür.','Ayrıca','“Ayrıca” daha önce söylenmiş bir şeye ekleme yapar; giriş cümlesi olamaz.','bilgi'),
  ('Bu yüzden insanlar tatillerini doğada geçirmeyi tercih ediyor.','Bu yüzden','“Bu yüzden” bir neden ister; öncede söylenmiş neden olmadan paragraf başlamaz.','dikkat'),
  ('Oysa birçok kişi bunun farkında bile değildir.','Oysa','“Oysa” ve “bunun” önceki bir yargıya karşıtlık kurar ve ona gönderme yapar; giriş olamaz.','bilgi')],
 'D','Her şıkta cümlenin başına bak: önceki bir cümleye dayanan bağlaç ya da zamir var mı?',
 'Giriş cümlesi, öncül gerektiren “ancak, ayrıca, oysa, bu yüzden” gibi sözcükler taşımaz.',
 kok='İnsanın doğayla ilişkisini anlatan bir paragrafın ilk cümlesi olabilecek cümle aşağıdakilerden hangisidir?')

# 0027 · orta · olamaz · A
giris('0027','orta','olamaz',
 ('Çocuklar da bu işe küçük yaşta katılır.','bu işe'),
 [('Anadolu’nun birçok yöresinde halı dokumacılığı kuşaktan kuşağa aktarılan bir zanaattır.','Kendi başına anlaşılır; konuyu tanıtır, gönderme ya da bağlaç taşımaz.','dikkat'),
  ('Dokuma tezgâhının başında geçen uzun saatler, ustaya sabrı öğretir.','Zamirsiz ve bağlaçsız; bağımsız bir yargı olduğundan paragrafı başlatabilir.','dikkat'),
  ('Her halı motifi, dokuyanın yaşadığı çevreden izler taşır.','Önceki bir cümleye dayanmaz; kendi başına anlaşılır.','dikkat'),
  ('Boyar maddelerin bitkilerden elde edildiği dönemlerde renkler daha yumuşaktı.','İçinde gönderme sözcüğü yoktur; tümce kendi başına anlam taşır, giriş olabilir.','dikkat')],
 'A','Hangi cümlede “bu, şu, o” gibi önceden söylenmiş bir şeyi gösteren sözcük var?',
 'Cümlenin içinde bile olsa “bu, şu, aynı” gibi gönderme sözcüğü taşıyan cümle paragrafı başlatamaz.',
 kok='Halı dokumacılığını konu alan bir yazıda, aşağıdaki cümlelerden hangisi paragrafı başlatan cümle olamaz?')

# 0028 · zor · olamaz · C
giris('0028','zor','olamaz',
 ('Söz konusu yaklaşım, doğa bilimlerinde yeni bir araştırma geleneğinin doğmasına yol açmıştır.','Söz konusu'),
 [('Bilim insanları, bir kuramın doğruluğunu onu çürütmeye çalışarak sınar.','İç bağlaç ya da gönderme taşımaz; konuyu doğrudan açar, giriş olabilir.','dikkat'),
  ('Gözlemin kuramdan önce geldiği düşüncesi, yüzyıllardır tartışılan konulardan biridir.','Cümle kendi başına anlaşılır; “tartışılan” bir sıfat-fiildir, öncel bir cümleye gönderme yapmaz.','dikkat'),
  ('Kuramlar, çürütülemedikleri sürece geçici olarak doğru sayılır ama hiçbir zaman kesinlik kazanmaz.','“ama” cümle içindeki iki yargıyı bağlar; öncel bir cümleye dayanmaz, giriş olabilir.','bilgi'),
  ('Her deney, yeni bir sorunun kapısını aralamaktan başka bir şey yapmaz.','Cümle kendi içinde tamdır; gönderme ya da öncüle bağlı bağlaç yoktur.','dikkat')],
 'C','Cümlenin içindeki bağlaçları ayır: cümle içi mi, öncel cümleye mi bağlıyor? Örtük göndermeleri de ara.',
 'Cümle içindeki “ama” bağımsızdır; “söz konusu, aynı, bahsedilen” gibi örtük göndermeler ise cümleyi öncüle bağlar.',
 kok='Bilimsel yöntem üzerine yazılacak bir paragraf için aşağıdakilerden hangisi giriş cümlesi olamaz?')
