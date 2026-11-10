"""pyapi · 2. parça (0029–0056). Metinler özgündür."""
from _hafif_pyapi import *
def F(b,a,k): return dict(baglac=b,akis=a,konu=k)

# ================= TAMAMLAMA (9) =================
# 0029 giriş · kolay · E
tam('0029','kolay','giris',
 '........ Ağaç gövdesi kesildiğinde ortaya çıkan halkalardan her biri, ağacın bir yıllık büyümesini gösterir. Yağışlı ve ılıman geçen yıllarda halka kalın, kurak ve soğuk geçen yıllarda ise ince olur. Halkaların rengi ve sıklığı, ağacın hangi yıllarda zorlandığını da belli eder. Bu yüzden bilim insanları, yüzlerce yıllık bir ağacın halkalarına bakarak o bölgenin geçmişteki iklimini yorumlayabilir.',
 'Ağaçlar, yaşadıkları yılların kaydını gövdelerinde saklar.',
 [('Bu yüzden ağaçların kesilmesi tümüyle yasaklanmalıdır.',F(False,False,False),'“Bu yüzden” ilk cümlede dayanacağı bir neden bulamaz; parça kesmeyi yasaklamaktan değil, halkalardan söz eder.','bilgi'),
  ('Meyve ağaçları, kışın yapraklarını dökerek enerji biriktirir.',F(True,True,False),'Yaprak dökümü parçanın konusu değildir; sonraki cümleler gövdedeki halkaları anlatır.','dikkat'),
  ('Ancak ağaçlar yüz yaşından sonra büyümeyi tamamen bırakır.',F(False,False,True),'“Ancak” öncül ister; üstelik parça yüzlerce yıllık ağaçların halkalarından söz ederek bu yargıyla çelişir.','bilgi'),
  ('Orman yangınları, kuru geçen yaz aylarında daha kolay yayılır.',F(True,True,False),'Yangınlar parçanın odağı değildir; “halkalardan her biri” cümlesine zemin hazırlamaz.','dikkat')],
 'E',('Sonraki cümleler halkaların yıllık büyümeyi ve iklimi gösterdiğini anlatıyor; son cümle bilim insanlarının halkalardan geçmişi yorumladığını söylüyor.','boşluk → gövdenin yıl kaydı tutması'),
 'Boşluktaki cümle ağacın yılları gövdesinde sakladığını söyler; halkaları ve iklim yorumunu anlatan sonraki cümleler bu fikrin ayrıntısıdır.',
 'Parçanın tamamı halkalardan söz ediyor; boşluk bu konuyu genel bir yargıyla açmalı.',
 'Giriş cümlesi, sonradan ayrıntısı verilecek genel yargıyı bağlaçsız ve göndermesiz söyler.')

# 0030 giriş · orta · A
tam('0030','orta','giris',
 '........ İki farklı çekim art arda dizildiğinde izleyici, aralarında bir bağ kurmadan edemez. Bir yüzün ardından bir kapının gösterilmesi, o kişinin kapıya baktığı izlenimini verir. Çekimlerin sırası değiştirildiğinde ise aynı görüntüler tümüyle başka bir anlam kazanır. Bu nedenle yönetmen için asıl iş, çekim yapmak kadar çekimleri dizmektir.',
 'Sinemada anlam, tek bir görüntüden çok görüntüler arasındaki ilişkiden doğar.',
 [('Bu nedenle sinema salonlarında sessizlik, izleyicinin en büyük görevidir.',F(False,True,False),'“Bu nedenle” ilk cümlede dayanacağı bir neden bulamaz; sessizlik de parçanın konusu değildir.','bilgi'),
  ('Ancak bazı yönetmenler filmlerini yalnızca tek bir çekimle çeker.',F(False,False,True),'“Ancak” kendinden önce bir yargı ister; üstelik parça çekimlerin dizilmesinin önemini vurgular.','bilgi'),
  ('Film müzikleri, görüntüyü duygusal olarak destekleyen ögelerdir.',F(True,True,False),'Müzik parçanın odağı değildir; sonraki “iki çekim art arda” cümlesine bağlanmaz.','dikkat'),
  ('Oyuncuların yüz ifadeleri, izleyicinin bir filmden zevk almasının tek nedenidir.',F(True,False,True),'Parça anlamın çekimlerin ilişkisinden doğduğunu söyler; “tek neden” yargısı aşırıdır ve parçayla çelişir.','bilgi')],
 'A',('Sonraki cümleler çekimlerin art arda dizilişinin anlam doğurduğunu, sıra değişince anlamın değiştiğini anlatıyor.','boşluk → anlamın ilişkiden doğması'),
 'Boşluktaki cümle genel ilkeyi söyler; sonraki üç cümle bu ilkeyi örneklerle ve sıra değişimiyle gösterir.',
 'Sonraki cümleler çekimlerin birbirine nasıl bağlandığını anlatıyor; boşluk bu ilişkiyi genel olarak söylemeli.',
 'Giriş cümlesi, parçanın geri kalanında örnekle desteklenen genel ilkeyi ortaya koyar.')

# 0031 giriş · zor · C
tam('0031','zor','giris',
 '........ İnsan, ilk kez karşılaştığı bir görüntüye şaşkınlıkla bakar; aynı görüntüyü her gün gördükçe gözü onu seçmez olur. Pencereden dağa bakmaya alışmış biri, dağın nerede durduğunu bile fark etmeyebilir. Her sabah aynı yoldan işe giden biri, yolun kenarındaki yüzlerce ayrıntıdan hiçbirini sonradan anlatamaz. Bu yüzden bir kente yeni gelen yolcu, yerlilerin görmezden geldiği ayrıntıları fotoğraflar. Sanatçıların sıradan nesneleri bile ilk kez görülüyormuş gibi resmetmesi, tam da bu tazelik arayışından doğar. Yani görmemizi sağlayan şey, çoğu zaman görülenin kendisinden çok bakışımızın tazeliğidir. Güzelliği yeniden fark etmek için yer değiştirmek şart değildir; bakışı yenilemek yeter.',
 'Alışkanlık, gözümüzün önündeki en güzel şeyleri bile görünmez kılabilir.',
 [('Güzellik, her insanda aynı etkiyi bırakan değişmez bir özelliktir.',F(True,False,True),'Parça güzelliği fark etmenin bakışın tazeliğine bağlı olduğunu söyler; şık değişmez bir etkiden söz ederek çelişir.','bilgi'),
  ('Dağlar, kentlerin iklimini ve yerleşim düzenini belirleyen en önemli coğrafi ögelerdir.',F(True,True,False),'Dağ, parçada yalnızca bir örnektir; iklim ve yerleşim konusu hiç geçmez, şık konudan sapar.','dikkat'),
  ('Fotoğraf makinesi, insan gözünün göremediği ayrıntıları yakalar.',F(True,True,False),'Parçada fotoğraf, yerlilerin görmediğini gören yolcunun yaptığı bir iştir; makinenin göz karşısındaki üstünlüğü konu edilmez.','dikkat'),
  ('Yolculuklar, insanın kendi kentine duyduğu özlemi artırır.',F(True,True,False),'Yolculuk ve özlem parçada geçmez; sonraki cümleler alışkanlığın gözü köreltmesini anlatır, şık konudan sapar.','dikkat')],
 'C',('Sonraki cümleler alışılan görüntünün artık seçilmediğini, yolcunun ise taze bir bakışla ayrıntıyı gördüğünü anlatıyor.','boşluk → alışkanlığın algıyı köreltmesi'),
 'Boşluktaki cümle, sonraki cümlelerde örneklenen “gözün alıştığını seçmemesi” düşüncesini genel olarak söyler; son cümledeki “bakışı yenilemek” çözümü de bu soruna yanıt olur.',
 'Parçanın son cümlesi bir çözüm öneriyor: bakışı yenilemek. Önce hangi sorun söylenmiş olmalı?',
 'Parçanın sonundaki çözüm ya da sonuç, girişte söylenen sorunla örtüşmelidir.')

# 0032 ortada · kolay · D
tam('0032','kolay','orta',
 'Satranç, kuralları birkaç dakikada öğrenilen ama ustalaşması yıllar alan bir oyundur. ........ Başlangıçta yalnızca taşların nasıl yürüdüğünü bilen oyuncu, zamanla rakibinin bir sonraki hamlesini kestirmeyi öğrenir. Bu yüzden satranç, sabır ve dikkat gerektiren bir zihin egzersizi sayılır. Küçük yaştaki çocuklar bile bu oyunla düşünmeyi eğlenerek ve yavaş yavaş öğrenir.',
 'Çünkü güçlük, kuralları bilmekte değil, onları doğru anda kullanmaktadır.',
 [('Oysa satranç, yalnızca yaşlı insanların boş vakitlerinde oynadığı bir oyundur.',F(False,False,True),'“Oysa” ilk cümleyle karşıtlık kurmaz; üstelik parça satrancı çocukların da öğrenebildiği bir oyun olarak anlatır.','bilgi'),
  ('Bu yüzden satranç tahtasında oynanan her oyun beraberlikle sonuçlanır.',F(False,False,True),'“Bu yüzden” bir nedene dayanmalı; ilk cümlede böyle bir neden yok, ayrıca parçayla ilgisi yok.','bilgi'),
  ('Ayrıca satranç taşları, çoğunlukla ahşap ya da plastikten yapılır.',F(True,True,False),'Taşların malzemesi parçanın konusu değildir; sonraki “Başlangıçta … oyuncu” cümlesine zemin hazırlamaz.','dikkat'),
  ('Kuralların kolay olması, oyuncuya ilk günden ustalık kazandırır.',F(True,False,True),'İlk cümle ustalaşmanın yıllar aldığını söyler; şık bununla çelişir.','bilgi')],
 'D',('Önce kuralın kolay, ustalığın zor olduğu söyleniyor; sonra yalnızca taşların yürüyüşünü bilenin zamanla gelişmesi anlatılıyor.','boşluk → zorluğun nedeni'),
 '“Çünkü” ilk cümledeki zorluğun nedenini açıklar; sonraki cümle “yalnızca yürüyüşü bilen” oyuncunun gelişimini anlatarak bu açıklamayı sürdürür.',
 'Boşluğun öncesinde bir zorluk belirtiliyor; boşluk bu zorluğun nedenini açıklayabilir mi?',
 'Önceki cümlede bir iddia varsa “çünkü” ile başlayan cümle onun nedenini getirir.')

# 0033 ortada · orta · A
tam('0033','orta','orta',
 'Tiyatroda oyuncu ile seyirci aynı mekânı, aynı anda ve aynı nefes alışverişiyle paylaşır. ........ Bir oyuncunun yanlış söylediği tek bir sözcük, salonda bir an içinde fark edilir ve oyuncu da bu tepkiyi hisseder. Bu karşılıklı etkileşim, tiyatroyu film gibi kaydedilmiş sanatlardan ayıran en belirgin ve en değerli özelliktir.',
 'Bu ortaklık, oyunun her akşam seyircinin tepkisiyle değişmesine yol açar.',
 [('Oysa sinemada oyuncular kameranın karşısında seyirciyi hiç düşünmez.',F(False,True,True),'“Oysa” bir karşıtlık ister ama önceki cümlede karşıt bir yargı yok; sonraki “bu tepkiyi” göndermesi de boşta kalır.','bilgi'),
  ('Tiyatro binalarının çoğu şehir merkezlerinde yer alır.',F(False,True,False),'Binaların yeri parçanın odağı değildir; sonraki cümledeki “bu tepkiyi” ifadesi bu cümlede karşılık bulmaz.','dikkat'),
  ('Bu yüzden seyirci, oyun boyunca hiçbir tepki vermemeli ve tümüyle sessiz kalmalıdır.',F(True,False,True),'Parça seyircinin tepkisini tiyatronun ayırt edici özelliği sayar; şık tepkiyi yasaklayarak parçayla çelişir.','bilgi'),
  ('Oyuncular, rollerini ezberlemek için aylarca prova yapar.',F(False,True,False),'Prova parçanın konusu değildir; “bu tepkiyi” ifadesinin gönderme yapacağı bir tepki söz konusu edilmemiştir.','dikkat')],
 'A',('Önce oyuncu ile seyircinin aynı mekânı paylaştığı söyleniyor; sonra “bu tepkiyi” ifadesi seyircinin tepkisine gönderme yapıyor.','boşluk → seyircinin tepkisi'),
 'Sonraki cümlede “bu tepkiyi” denildiğine göre boşlukta seyircinin tepkisi anılmalıdır; “Bu ortaklık” da ilk cümledeki paylaşıma bağlanır.',
 'Boşluktan sonraki cümledeki “bu tepkiyi” ifadesi neye gönderme yapıyor?',
 'Boşluktan sonraki “bu, böyle, o” gibi gönderme sözcükleri, boşlukta anılması gereken şeyi gösterir.')

# 0034 ortada · orta · B
tam('0034','orta','orta',
 'Uzun süre aynı işe odaklanan biri, bir noktadan sonra yaptığı küçük hataları bile görmez olur ve aynı yanlışı tekrarlar. ........ Kısa bir yürüyüş ya da birkaç dakikalık bir dinlenme, zihnin yeniden toparlanmasına yetebilir. Mola vermeyi tembellik sayanlar, aslında verimliliklerini kendi elleriyle düşürmüş olurlar ve işlerini daha geç bitirirler.',
 'Çünkü beyin, yoğun dikkati sınırsız bir süre sürdüremez.',
 [('Bu nedenle çalışırken kesinlikle hiç ara verilmemelidir.',F(True,False,True),'Sonraki cümle kısa dinlenmeyi yararlı bulur; şık araya hiç yer vermeyerek parçayla çelişir.','bilgi'),
  ('Oysa bazı insanlar günde on saat çalışsa da hiç yorulmaz.',F(False,False,True),'“Oysa” önceki cümleye karşıtlık kurar gibi görünür ama parça dinlenmenin gerekliliğini savunur; şık parçayla çelişir.','bilgi'),
  ('Hata yapan kişi, işini bırakıp başka bir mesleğe yönelmelidir.',F(True,True,False),'Meslek değiştirme parçada yoktur; sonraki “Kısa bir yürüyüş” cümlesine zemin hazırlamaz.','dikkat'),
  ('Ayrıca çalışma masasının düzenli olması, dikkati artırır.',F(True,False,False),'Masa düzeni parçanın konusu değildir; sonraki mola önerisi bu cümleden doğmaz.','dikkat')],
 'B',('Önce uzun odaklanmanın hatalara yol açtığı söyleniyor; sonra kısa bir dinlenmenin zihni toparladığı anlatılıyor.','boşluk → hatanın nedeni'),
 '“Çünkü” önceki cümledeki hata birikiminin nedenini açıklar; sonraki cümlede önerilen mola da bu nedenin çözümüdür.',
 'Önceki cümle bir sorunu, sonraki cümle bir çözümü anlatıyor; boşluk sorunun nedenini söylemeli.',
 'Sorun ile çözüm arasındaki boşluğa çoğu kez sorunun nedenini açıklayan cümle gelir.')

# 0035 sonuç · orta · D
tam('0035','orta','sonuc',
 'Kentlerin çatılarında ve boş arsalarında kurulan sebze bahçeleri, son yıllarda birçok şehirde yaygınlaştı. Bu bahçelerde yetişen sebzeler marketlere uzun yollardan taşınmadığı için hem taze hem de daha ucuz olabilir. Komşular toprağı birlikte işlediğinde birbirini tanır, apartman yaşamının getirdiği yalnızlık azalır. Çocuklar ise yedikleri sebzenin nasıl yetiştiğini kendi gözleriyle görür. ........',
 'Kent bahçeleri, hem sofraya hem insan ilişkilerine katkı sağlar.',
 [('Bu nedenle kentlerdeki tarım arazileri apartman bahçelerine dönüştürülmelidir.',F(True,False,True),'Parça böyle bir öneri getirmez; bahçelerin yararını anlatır. Şık parçanın söylediğinden fazlasını iddia eder.','bilgi'),
  ('Kentteki bahçeler, kırsal tarımın yerini alacaktır.',F(True,False,True),'Parçada kırsal tarımdan ve onun yerini almaktan söz edilmez; şık parçanın söylediğinden fazlasını iddia eder.','bilgi'),
  ('Çocuklar yalnızca sebze yemeyi sevdikleri için bu bahçelere ilgi duyar.',F(True,False,True),'Parça çocukların ilgisinin nedenini bu biçimde açıklamaz; yalnızca sebzenin yetişmesini gördüklerini söyler.','dikkat'),
  ('Sebze fiyatlarının ucuzlaması, apartmanda yaşamanın tek avantajıdır.',F(True,False,False),'“Tek avantaj” iddiası parçada yoktur; parça ucuzluğu yalnızca bir yarar olarak sayar.','bilgi')],
 'D',('Parça önce tazelik ve ucuzluğu, sonra komşuluk ilişkilerini, en son çocukların öğrenmesini anlatıyor.','sonuç: sofraya ve ilişkilere katkı'),
 'Sonuç cümlesi, parçadaki yararların (taze ve ucuz sebze, komşuluk, çocukların öğrenmesi) ortak sonucunu verir ve aşırı genelleme getirmez.',
 'Parçanın verdiği yararlar iki grupta toplanıyor: sofraya ve insanlara. Sonuç bu ikisini kapsamalı.',
 'Sonuç cümlesi parçadaki yararların hepsini kapsar, onlardan fazlasını iddia etmez.')

# 0036 sonuç · orta · C
tam('0036','orta','sonuc',
 'Hava durumu tahminleri, atmosferdeki sıcaklık, basınç ve nem ölçümlerinin güçlü bilgisayarlarda işlenmesiyle yapılır. Ölçüm ne kadar sık ve ne kadar geniş bir alandan alınırsa tahmin o kadar sağlam olur. Ancak atmosfer kaotik bir sistemdir; başlangıçtaki küçücük bir ölçüm hatası, günler içinde büyüyerek sonucu büsbütün değiştirebilir. Bu yüzden yarın için yapılan tahminler, on gün sonrası için yapılanlardan çok daha güvenilirdir. ........',
 'Demek ki tahminin güvenilirliği, ileriye gidildikçe azalır.',
 [('Dolayısıyla on günlük tahminler, ölçüm yapılmadan da kolayca yapılabilir.',F(True,False,True),'Parça ölçümün tahmin için gerekli olduğunu söyler; şık ölçümü gereksiz sayarak çelişir.','bilgi'),
  ('Bu nedenle günlük tahminlerin hiçbir değeri yoktur.',F(True,False,True),'Parça yarın için yapılan tahminleri güvenilir bulur; “hiçbir değeri yoktur” aşırı ve çelişkilidir.','bilgi'),
  ('Ölçüm yapılan alan genişledikçe atmosferin kaotikliği ortadan kalkar.',F(True,False,True),'Parça ölçüm alanının genişlemesinin tahmini sağlamlaştırdığını söyler; kaotikliğin kalkacağını söylemez.','bilgi'),
  ('Yarının tahmini, sıcaklık ölçümlerine hiç gerek duymaz.',F(True,False,True),'Parça tahminin sıcaklık, basınç ve nem ölçümlerine dayandığını söyler; şık bununla çelişir.','bilgi')],
 'C',('Parça tahminin ölçümlere dayandığını, küçük hataların zamanla büyüdüğünü ve yakın tarihli tahminin daha güvenilir olduğunu söylüyor.','sonuç: süre uzadıkça güvenilirlik azalır'),
 'Sonuç cümlesi, “küçük hata zamanla büyür” ve “yarın daha güvenilir” yargılarının ortak sonucunu verir.',
 'Parçanın son cümlesi yakın ve uzak tahmini karşılaştırıyor; sonuç bu karşılaştırmanın hükmünü vermeli.',
 'Karşılaştırmayla biten bir parçanın sonuç cümlesi, karşılaştırmanın genel hükmünü söyler.')

# 0037 sonuç · zor · E
tam('0037','orta','sonuc',
 'Bir eserin klasik sayılması, yazıldığı çağda çok satmış olmasına bağlı değildir. Pek çok klasik, ilk yayımlandığında birkaç yüz kişiye ulaşmış, hatta yazarının yaşamında hak ettiği ilgiyi görmemiştir. Onları kalıcı yapan, her çağın okurunun kendi sorusunu o eserde bulabilmesidir. Çünkü büyük bir yapıt, belli bir dönemin sorunlarına yanıt vermekle yetinmez; o sorunların altındaki daha derin ve daha kalıcı insanlık durumlarına da dokunur. Bu sayede aradan yüzyıllar geçse de yeni okur, eserde kendi yaşadığı çağın yankısını duyar. ........',
 'Demek ki klasiği klasik yapan, çağının beğenisi değil, çağları aşan sorulardır.',
 [('Dolayısıyla bir eser, yazıldığı çağın sorunlarına hiç değinmemelidir ki klasik olabilsin.',F(True,False,True),'Parça eserin dönemin sorunlarına yanıt vermekle “yetinmediğini” söyler, hiç değinmemesi gerektiğini değil; şık aşırıdır.','bilgi'),
  ('Böylece çok satan her eser, zamanla klasikler arasına girer.',F(True,False,True),'Parçanın ilk cümlesi satış başarısının klasikliği belirlemediğini söyler; şık bununla çelişir.','bilgi'),
  ('Kısacası klasikler, yazarlarının yaşamında hak ettiği ilgiyi mutlaka görmüştür.',F(True,False,True),'Parça pek çok klasiğin yazarının yaşamında hak ettiği ilgiyi görmediğini söyler; “mutlaka” yargısı bununla çelişir.','bilgi'),
  ('Bu yüzden yeni okur, eski eserleri ancak yazıldığı çağın koşullarını öğrenerek anlayabilir.',F(True,False,False),'Parça yeni okurun eserde kendi çağının yankısını duyduğunu söyler; şık okurun eseri ancak eski koşullarla anlayacağını söyleyerek ters düşer.','dikkat')],
 'E',('Parça klasikliğin satış başarısına değil, çağlar üstü sorulara bağlı olduğunu adım adım gösteriyor.','sonuç: klasiği klasik yapan çağları aşan sorular'),
 'Sonuç cümlesi, parçanın “satış değil kalıcı sorular” yargısını bozmadan özetler; diğer şıklar parçadaki bir yargıyla çelişir ya da aşırı genelleme yapar.',
 'Parçanın ilk cümlesi bir şeyin ölçüt olmadığını, üçüncü cümlesi ise ölçütün ne olduğunu söylüyor.',
 'Çelişki ya da aşırı genelleme içeren şıkları parçadaki açık yargılarla sınamak, sonuç cümlesi sorularında en güvenli yoldur.')

# ================= AKIŞ BOZAN (6) =================
# 0038 · kolay · V → E
akis('0038','kolay',
 ['Kar taneleri, altı kollu küçük kristallerdir ve her biri bulut içinde farklı bir yol izleyerek biçimlenir.',
  'Yükseklerde sıcaklık ve nem değiştikçe kristalin kolları da değişik biçimlerde uzar.',
  'Bu yüzden iki kar tanesinin birbirinin tıpkısı olması son derece düşük bir ihtimaldir.',
  'Kristallerin kolları ne kadar zengin biçimler alırsa tanenin görünümü de o kadar karmaşıklaşır.',
  'Kış turizmi yapılan yörelerde konaklama fiyatları, yılbaşı haftasında en yüksek düzeye çıkar.'],
 [('konuyu tanıtır',''),('kristalin biçimlenmesini sürdürür',''),('“Bu yüzden” ile II’deki farklı biçimlenmenin sonucunu verir','Bu yüzden'),('kristal kollarının görünüme etkisini anlatır',''),('sapma','')],
 4,'Parça, kar tanelerinin nasıl biçimlendiğini ve neden birbirinden farklı olduğunu anlatıyor.',
 'V. cümle kış turizminde konaklama fiyatlarından söz eder; kar tanesinin biçimlenmesiyle ilgisi yoktur.',
 'V. cümle çıkarılınca parça baştan sona kar tanesinin kristal yapısını anlatır; bütünlük korunur.',
 'Parçanın odağı kar tanesinin kendisi; “kar” sözcüğünü paylaşsa da başka bir konuya geçen cümleyi ara.',
 'Parçanın anlattığı şeyden (kar tanesi) çıkıp onun çevresindeki ekonomik ya da turistik bir konuya geçen cümle akışı bozar.')

# 0039 · kolay · II → B
akis('0039','kolay',
 ['Yüzme, bütün kasları aynı anda çalıştırdığı için en kapsamlı ve en dengeli sporlardan biri sayılır.',
  'Havuzların çoğunda su sıcaklığı yirmi sekiz derece civarında tutulur.',
  'Suyun kaldırma gücü eklemler üzerindeki yükü azalttığından yaralanma riski de düşüktür.',
  'Bu yüzden doktorlar, hareket kısıtlılığı olanlara sık sık yüzmeyi önerir.',
  'Düzenli yüzenlerde solunum kapasitesinin ve dayanıklılığın da arttığı görülür.'],
 [('konuyu tanıtır',''),('sapma',''),('yüzmenin eklemler üzerindeki yararını anlatır',''),('“Bu yüzden” ile III’teki yararın sonucunu verir','Bu yüzden'),('“de” ile yüzmenin bir başka yararını ekler','de')],
 1,'Parça, yüzmenin sağlığa sağladığı yararları anlatıyor.',
 'II. cümle havuz suyunun sıcaklığından söz eder; yüzmenin sağlığa yararıyla ilgisi yoktur.',
 'II. cümle çıkarılınca kasların çalışması, eklem yükünün azalması, doktor önerisi ve solunum yararı kesintisiz sıralanır.',
 'Parçanın odağı yüzmenin yararları; havuzla ilgili teknik bir ayrıntıyı ara.',
 'Yararları sıralayan bir parçada yararla ilgisi olmayan teknik ya da çevresel bir ayrıntı akışı bozar.')

# 0040 · orta · V → E
akis('0040','orta',
 ['Bir konser salonunun akustiği, müziğin dinleyiciye ne kadar doğru ulaşacağını belirler.',
  'Sesin duvarlardan fazla yansıdığı salonlarda notalar birbirine karışır ve ezgi bulanıklaşır.',
  'Bunun önüne geçmek için duvar ve tavanlara sesi emen ya da dağıtan özel yüzeyler yerleştirilir.',
  'Böylece her koltuğa gelen ses, dengeli ve berrak bir yapıya kavuşur.',
  'Orkestradaki çalgıların sayısı, bestenin yazıldığı döneme göre büyük farklılıklar gösterir.'],
 [('konuyu tanıtır',''),('kötü akustiğin doğurduğu sorunu anlatır',''),('“Bunun önüne geçmek için” ile II’deki sorunun çözümünü anlatır','Bunun önüne geçmek için'),('“Böylece” ile çözümün sonucunu verir','Böylece'),('sapma','')],
 4,'Parça, salon akustiğinin müziğin dinleyiciye ulaşmasındaki rolünü anlatıyor.',
 'V. cümle orkestradaki çalgı sayısının döneme göre değişmesinden söz eder; salonun akustiğiyle ilgisi yoktur.',
 'V. cümle çıkarılınca sorun (II), çözüm (III) ve sonuç (IV) zinciri parçayı tamamlar.',
 'Parçanın odağı salon akustiği; “müzik” alanında kalıp başka bir yöne geçen cümleyi ara.',
 'Bağlaç zinciri (sorun → çözüm → sonuç) tamamlandıktan sonra gelen ilgisiz bilgi akışı bozar.')

# 0041 · orta · III → C
akis('0041','orta',
 ['Müzede gezerken her eserin başında uzun süre durmaya çalışmak çoğu zaman yorucu ve verimsizdir.',
  'Gözün ve zihnin dikkati sınırlıdır; belli bir süreden sonra eserler birbirine karışmaya başlar.',
  'Müzelerde bilet fiyatları ülkeden ülkeye ve yıldan yıla değişir.',
  'Bu yüzden birkaç eseri seçip onlara yoğunlaşmak, hepsine göz gezdirmekten daha çok şey öğretir.',
  'Gerisini sonraki ziyaretlere bırakmak da ayrıca iyi bir alışkanlıktır.'],
 [('konuyu tanıtır',''),('dikkatin sınırlı olduğunu açıklar',''),('sapma',''),('“Bu yüzden” ile II’deki sınırlı dikkatten sonuç çıkarır','Bu yüzden'),('“ayrıca” ile yöntemi tamamlar','ayrıca')],
 2,'Parça, müzede nasıl gezilirse verim alınacağını anlatıyor.',
 'III. cümle bilet fiyatlarından söz eder; gezme yönteminin verimiyle ilgisi yoktur.',
 'III. cümle çıkarılınca II’deki sınırlı dikkat ile IV’teki “Bu yüzden” önerisi doğrudan bağlanır.',
 'Parçanın odağı müzede verimli gezmenin yolu; bu yola hizmet etmeyen cümleyi ara.',
 'Önerilerle biten bir parçada “bu yüzden” cümlesi gerekçesini bulduğu cümleye bağlanır; gerekçeye hizmet etmeyen cümle bozandır.')

# 0042 · zor · V → E
akis('0042','zor',
 ['Diller, konuşanları var oldukça değişmeyi sürdürür; hiç değişmeyen bir dil, aslında artık kimsenin konuşmadığı bir dildir.',
  'Telefon, bilgisayar ve internet gibi yeni araçlar, kendi sözcüklerini de beraberinde getirerek dile yeni ögeler ekler ve birkaç yıl içinde herkesin günlük konuşmasına yerleşir.',
  'Eski sözcükler ise kullanım alanı daraldıkça önce yaşlı konuşurların dilinde yaşar, sonra yavaş yavaş unutulur; en sonunda yalnızca eski metinlerde ve sözlüklerde kalır.',
  'Bu iki yönlü hareket, dilin sürekli bir yenilenme içinde olduğunu ve hiçbir dönemde durağan kalmadığını gösterir.',
  'Yazım kılavuzlarını hazırlamak, dil bilgisi çalışmalarının en çok emek ve dikkat isteyen alanlarından biridir ve çoğu zaman yıllarca süren titiz bir ekip çalışması gerektirir.'],
 [('ana iddiayı (dil değişir) açar',''),('dile giren yeni sözcükleri anlatır',''),('“ise” ile II’ye karşıt yönü (sözcük kaybını) anlatır','ise'),('“Bu iki yönlü hareket” ile II ve III’ü birlikte yorumlar','Bu iki yönlü hareket'),('sapma','')],
 4,'Parça, dilin sürekli değiştiğini, sözcük kazanımı ve kaybıyla gösteriyor.',
 'V. cümle de dille ilgilidir ama dilin nasıl değiştiğini değil, kılavuz hazırlamanın zahmetini anlatır; parçanın odağı dışındadır.',
 'V. cümle çıkarılınca IV’teki yorum, parçanın sonuç cümlesi olarak bütünü kapatır.',
 'Parçanın iddiası dilin değişmesi; her cümle bu değişimi mi anlatıyor, yoksa dille ilgili başka bir şeyi mi?',
 'Parçayla aynı alana (dil) ait olsa da iddiayı sürdürmeyen cümle akışı bozar; alanın aynı olması ölçüt değildir.')

# 0043 · zor · IV → D
akis('0043','orta',
 ['Asma köprüler, ağırlığı taşıyan çelik halatların iki kule arasında gerilmesiyle ayakta durur.',
  'Yük, halatlar aracılığıyla önce kulelere, oradan da zemine aktarılır.',
  'Bu nedenle kulelerin sağlam bir zemine oturması, köprünün ömrü için belirleyici olur.',
  'Büyük asma köprülerin uzaktan görünüşü, kentlerin simgelerinden biri hâline gelir ve turistik fotoğrafların vazgeçilmez ögesi olur.',
  'Rüzgâr gibi yanal kuvvetlere karşı ise güverteye ek sertlik kazandıran kafes yapılar kullanılır.'],
 [('konuyu (taşıma düzeneğini) tanıtır',''),('yükün nasıl aktarıldığını anlatır',''),('“Bu nedenle” ile II’deki yük aktarımının sonucunu verir','Bu nedenle'),('sapma',''),('“ise” ile köprünün yanal kuvvetlere karşı yapısını anlatır','ise')],
 3,'Parça, asma köprünün yükü nasıl taşıdığını ve dayanıklılığını nasıl sağladığını anlatıyor.',
 'IV. cümle köprünün görünüşünden ve simge olmasından söz eder; taşıma mekaniğiyle ilgisi yoktur.',
 'IV. cümle çıkarılınca III’teki zemin ve kule konusundan V’teki yanal kuvvetlere mühendislik anlatımı kesintisiz sürer.',
 'Parçanın odağı köprünün nasıl ayakta kaldığı; yapının dışarıdan görünüşünü anlatan bir cümle var mı?',
 'Teknik bir işleyişi anlatan parçada görünüş, simge ya da turizm gibi başka bir bakış açısına geçen cümle akışı bozar.')

# ================= PARAGRAFI İKİYE BÖLME (5) =================
# 0044 · kolay · cut III → B
bolme('0044','kolay',
 ['Bulutlar, havadaki su buharının küçük damlacıklara ya da buz kristallerine dönüşmesiyle oluşur.',
  'Bu damlacıklar o kadar hafiftir ki yerçekimine rağmen havada asılı kalabilir.',
  'Bulutlar, oluşumlarının yanı sıra türlerine göre de sınıflandırılır.',
  'Yüksekte oluşan ince ve tüylü bulutlara sirüs denir.',
  'Alçakta toplanıp gökyüzünü gri bir örtüyle kaplayan bulutlar ise yağış getirebilir.',
  'Yığın biçiminde, pamuğa benzeyen bulutlar da çoğunlukla iyi havanın habercisidir.'],
 [('bas','',''),('devam','Bu damlacıklar','“Bu damlacıklar” ile I’deki oluşumu sürdürür'),('yeni','yanı sıra','“oluşumlarının yanı sıra” ile bulutların oluşumundan sınıflandırılmasına geçilir'),('devam','sirüs','sınıflandırmadan bir tür örneği verir'),('devam','ise','sınıflandırmadan bir başka tür örneği verir'),('devam','da','sınıflandırmadan bir başka tür örneği ekler')],
 'I ve II bulutların nasıl oluştuğunu anlatıyor.',
 'III–VI bulutların türlerini anlatıyor; konu oluşumdan sınıflandırmaya geçmiştir.',
 'İlk iki cümle bulutun nasıl oluştuğunu anlatıyor; konunun “türler”e döndüğü yeri bul.',
 'Konu “nasıl oluşur”dan “hangi türleri vardır”a geçtiğinde yeni paragraf başlar.')

# 0045 · orta · cut IV → C
bolme('0045','orta',
 ['Matbaanın yaygınlaşması, bilginin toplumda dolaşım biçimini kökten değiştirdi.',
  'Nitekim matbaadan önce bir kitabı elle çoğaltmak aylar alırdı; matbaayla aynı iş günler içinde bitmeye başladı.',
  'Bu hız, kitapları ucuzlattı ve daha geniş kesimlerin eline ulaştırdı.',
  'Peki bu değişimin asıl sonucu neydi?',
  'Bu sorunun yanıtı, okuma yazma bilenlerin sayısının zamanla artmasında ve okumanın ayrıcalıklı birkaç kişinin işi olmaktan çıkmasında yatar.',
  'Böylece bilgi, birkaç kişinin tekelinden çıkıp sıradan insanların da erişebildiği bir şey oldu.'],
 [('bas','',''),('devam','Nitekim','“Nitekim” ile I’deki değişimi hızla (çoğaltma süresiyle) örnekler'),('devam','Bu hız','“Bu hız” ile II’deki hıza bağlanır'),('yeni','Peki','“Peki” sorusuyla değişimin yöntem ve maliyetinden asıl sonucuna geçilir'),('devam','Bu sorunun yanıtı','“Bu sorunun yanıtı” ile IV’teki soruya bağlanır'),('devam','Böylece','“Böylece” ile V’in sonucunu verir')],
 'I–III matbaanın kitapların çoğalma hızı ve fiyatı üzerindeki etkisini anlatıyor.',
 'IV–VI değişimin toplumsal sonucunu (okur sayısının artışını) anlatıyor; bir soruyla yeni bir yöne geçilmiştir.',
 'İlk üç cümle “nasıl oldu” sorusunu, sonrası “ne sonuç verdi” sorusunu yanıtlıyor. Geçiş nerede?',
 'Bir sonuca ya da yeni bir yöne geçişi açan “peki” sorusu yeni paragrafın başlangıcı olabilir.')

# 0046 · orta · cut V → D
bolme('0046','orta',
 ['Bulmaca çözmek, ilk bakışta yalnızca boş zamanı değerlendirmenin bir yolu gibi görünse de zihni epeyce çalıştıran bir uğraştır.',
  'Bulmaca çözen kişi, eldeki ipuçlarını karşılaştırır ve olasılıkları tek tek eler.',
  'Bu uğraş, farkında olmadan akıl yürütme becerisini çalıştırır.',
  'Düzenli bulmaca çözenlerin sözcük dağarcığının genişlediği de gözlenmiştir.',
  'Gelelim bulmaca çözmenin ruh sağlığına etkisine: çözülen her bulmaca küçük bir başarı duygusu verir.',
  'Bu duygu, kişinin gün içinde karşılaştığı gerilimi hafifletebilir.'],
 [('bas','',''),('devam','Bulmaca çözen kişi','I’deki “zihni çalıştırma” iddiasını açıklar'),('devam','Bu uğraş','“Bu uğraş” ile II’deki çözme işine bağlanır'),('devam','de gözlenmiştir','zihinsel yararlara bir yarar (sözcük dağarcığı) ekler'),('yeni','Gelelim','“Gelelim” ile zihinsel yararlardan ruh sağlığına etkisine geçilir'),('devam','Bu duygu','“Bu duygu” ile V’teki başarı duygusuna bağlanır')],
 'I–IV bulmacanın zihinsel yararlarını (akıl yürütme, sözcük dağarcığı) anlatıyor.',
 'V–VI bulmacanın ruh sağlığı üzerindeki etkisini anlatıyor; yarar türü zihinselden duygusala geçmiştir.',
 'İlk dört cümlede hangi tür yarar anlatılıyor? Farklı bir yarara geçiş nerede başlıyor?',
 'Parçada ele alınan yönün (zihinsel / duygusal) değiştiği yerde yeni paragraf başlar.')

# 0047 · orta · cut VI → E
bolme('0047','orta',
 ['Renk adlarını ayrıntılı biçimde ayırt eden dillerde konuşanlar, benzer tonları daha çabuk fark eder.',
  'Bu durum, sözcüklerin algıyı biçimlendirdiğini düşündürür.',
  'Gerçekten de adı olmayan bir şeyi fark etmek, adı olan bir şeyi fark etmekten daha zordur.',
  'Çocukların yeni bir sözcük öğrendikleri anda o sözcüğün gösterdiği nesneyi çevrelerinde daha sık görmeleri de aynı etkiyle açıklanabilir.',
  'Böylece dilin yalnızca düşünceyi anlatan değil, düşünceyi yönlendiren bir araç olduğu savı güç kazanır.',
  'Ne var ki bu savı eleştirenler, algının dilden bağımsız olarak da işlediğini gösteren deneylere dikkat çeker.'],
 [('bas','',''),('devam','Bu durum','“Bu durum” ile I’deki gözlemi yorumlar'),('devam','Gerçekten de','“Gerçekten de” ile II’deki görüşü destekler'),('devam','de aynı etkiyle','“de aynı etkiyle” ile aynı görüşü bir örnekle destekler'),('devam','Böylece','“Böylece” ile desteklenen görüşün sonucunu verir'),('yeni','Ne var ki','“Ne var ki” ile savı destekleyen anlatımdan savı eleştiren karşıt görüşe geçilir')],
 'I–V dilin algıyı biçimlendirdiği savını destekleyen gözlem ve örnekleri sıralıyor.',
 'VI bu savı eleştiren karşıt görüşü getiriyor; bakış açısı destekten eleştiriye dönmüştür.',
 'İlk beş cümlede yazar hangi görüşü destekliyor? Bu görüşün tersine dönüldüğü yeri bul.',
 'Aynı görüşü sürdüren cümleler bir paragrafta kalır; karşıt görüşe geçildiği cümlede paragraf başlayabilir.')

# 0048 · zor · cut II → A
bolme('0048','zor',
 ['Eskiden bir kitabı çoğaltmak, yazıcıların aylarca süren elle kopyalama emeğine bağlıydı; bu yüzden kitaplar çok pahalıydı, yalnızca zenginlerin ve kurumların elinde bulunurdu, okuma yazma ise dar bir çevreyle sınırlı kalırdı.',
  'Hareketli harflerle çalışan matbaa makineleri ise bir sayfayı yüzlerce kez, hiç değişmeyen bir biçimde basabiliyor.',
  'Bu özellik, bir kitabın maliyetini kopyalama çağına göre büyük ölçüde düşürdü.',
  'Maliyet düştükçe kitap, saray ve manastır duvarlarının dışına çıkıp tüccarın, zanaatkârın ve öğrencinin de elinde yer buldu.',
  'Bu genişleyen okur kitlesi, yeni yazarlar ve yeni konular için bir pazar doğurdu.',
  'Dolayısıyla matbaa, yalnızca kitabı ucuzlatan bir araç değil, bilginin dolaşımını hızlandıran bir düzen kurdu.'],
 [('bas','',''),('yeni','matbaa makineleri ise','“matbaa makineleri ise” ile elle kopyalamanın sorunlarından matbaa çözümüne geçilir; cümle öncekine gönderme yapmayan yeni bir konu açar'),('devam','Bu özellik','“Bu özellik” ile II’deki aynı biçimde çok sayıda basabilme özelliğine bağlanır'),('devam','Maliyet düştükçe','“Maliyet düştükçe” ile III’teki maliyet düşüşüne bağlanır'),('devam','Bu genişleyen okur kitlesi','“Bu genişleyen okur kitlesi” ile IV’teki yeni okurlara bağlanır'),('devam','Dolayısıyla','“Dolayısıyla” ile II–V’in sonucunu verir')],
 'I, kitap çoğaltmanın eski, zahmetli yöntemini ve doğurduğu sorunları anlatıyor; kendi içinde tamamlanıyor.',
 'II–VI matbaanın getirdiği çözümü ve sonuçlarını anlatıyor; III–VI “Bu özellik, Maliyet düştükçe, Bu genişleyen okur kitlesi, Dolayısıyla” ile bir öncekine bağlıdır.',
 'İlk cümle eski yöntemin sorunlarını anlatıyor. Sorundan çözüme geçilen, öncekine gönderme yapmayan cümleyi bul.',
 'Sorunu anlatan bölümden çözüme geçen ve öncekine gönderme yapmayan cümle yeni paragrafı açar; “bu özellik, dolayısıyla” gibi göndermeli cümleler açamaz.')

# ================= CÜMLE SIRALAMA (5) =================
T1=['Ekmek yapmak için önce un, su, tuz ve maya bir kapta karıştırılır.',
    'Elde edilen hamur, uzun süre yoğrularak esnek bir yapıya kavuşturulur.',
    'Yoğrulan hamur, ılık bir ortamda bir süre dinlendirilir ve mayanın etkisiyle kabarır.',
    'Kabaran hamur, şekil verilerek fırına sürülür.',
    'Fırının sıcaklığı sayesinde hamur pişer, kabuk bağlar ve ekmek yemeye hazır hâle gelir.']
sira('0049','kolay',T1,
 [('ilk',0,None,'','Malzemelerin karıştırılmasıyla başlayan, öncül istemeyen cümle girişe uygundur.'),
  ('once',0,1,'Elde edilen hamur','“Elde edilen hamur”, karıştırmanın ürünüdür; karıştırmayı anlatan cümleden sonra gelir.'),
  ('once',1,2,'Yoğrulan hamur','“Yoğrulan hamur” yoğurmayı anlatan cümleden sonra gelir.'),
  ('once',2,3,'Kabaran hamur','“Kabaran hamur” kabarmayı anlatan cümleden sonra gelir.'),
  ('once',3,4,'Fırının sıcaklığı','“Fırının sıcaklığı”, hamurun fırına sürülmesinden sonra gelir.')],
 ['giriş: malzemelerin karıştırılmasını anlatır','“Elde edilen hamur” ile karıştırmadan sonra gelir','“Yoğrulan hamur” ile yoğurmadan sonra gelir','“Kabaran hamur” ile kabarmadan sonra gelir','“Fırının sıcaklığı” ile fırına sürmeden sonra gelir'],
 -1,'E','“Elde edilen, Yoğrulan, Kabaran hamur” ifadeleri bir önceki aşamanın ürününe gönderme yapar.',
 'Hamurun adının her cümlede nasıl değiştiğine bak: elde edilen → yoğrulan → kabaran.','Aşamalı bir işlemde sıfat-fiil ile değişen ad (elde edilen, yoğrulan, kabaran) sırayı belirler.',201)

T2=['Dağlık bölgelerde bağırdığımızda sesimizin bir süre sonra bize geri döndüğünü duyarız.',
    'Bu olaya yankı denir ve sesin bir engele çarpıp geri dönmesinden kaynaklanır.',
    'Ses, havada saniyede yaklaşık üç yüz kırk metre hızla ilerlediği için dönüş hemen duyulmaz.',
    'Engel ne kadar uzaksa sesin gidip gelmesi o kadar uzun sürer.',
    'Yankının bu özelliğinden yararlanılarak denizin derinliği ya da bir cismin uzaklığı ölçülebilir.']
sira('0050','orta',T2,
 [('ilk',0,None,'','Günlük bir gözlemle başlayan, öncül istemeyen cümle girişe uygundur.'),
  ('hemen',0,1,'Bu olaya','“Bu olaya” 0’da anlatılan sesin geri dönmesine gönderme yapar.'),
  ('once',1,2,'dönüş','“dönüş”, 1’de anlatılan geri dönmeden sonra söz edilebilir.'),
  ('once',2,3,'gidip gelmesi','“sesin gidip gelmesi” hız ve dönüşü anlatan cümleden sonra gelir.'),
  ('hemen',3,4,'bu özelliğinden','“bu özelliğinden”, 3’te anlatılan uzaklıkla süre ilişkisine gönderme yapar.')],
 ['giriş: bağırınca sesin geri döndüğünü anlatır','“Bu olaya” ile girişe bağlanır','“dönüş” ile yankıdan sonra gelir','“gidip gelmesi” ile dönüş süresinden sonra gelir','“bu özelliğinden” ile uzaklık–süre ilişkisine bağlanır'],
 2,'A','“Bu olaya” ve “bu özelliğinden” gönderme yapar; “dönüş” ve “gidip gelmesi” süreci aşama aşama ilerletir.',
 'Önce gözlemi, sonra ona ad verilen cümleyi, ardından açıklamaları sırala.','“Bu olaya” gibi bir adlandırma cümlesi, olayın anlatıldığı cümlenin hemen arkasına gelir.',202)

T3=['Bir ressamın boş tuvalin karşısına doğrudan boyayla geçmesi pek görülen bir durum değildir.',
    'Bunun yerine ressam önce kâğıt üzerinde kurşun kalemle küçük eskizler yapar.',
    'Bu eskizlerde kompozisyonun nasıl kurulacağı, ışığın hangi yönden düşeceği denenir.',
    'Beğenilen taslak ise tuvale aktarılır ve asıl çalışma o zaman başlar.',
    'Böylece tuvalde yapılabilecek bir hata, daha tuvale geçmeden kâğıtta ve çok daha ucuza yakalanmış olur.']
sira('0051','orta',T3,
 [('ilk',0,None,'','Durumu genel olarak koyan, zamir ve bağlaç taşımayan cümle girişe uygundur; “Bunun yerine” ile başlayan adım bu girişten sonra gelir.'),
  ('hemen',0,1,'Bunun yerine','“Bunun yerine”, 0’daki doğrudan boyayla başlamaya karşıt bir yöntem getirir; hemen ardından gelir.'),
  ('hemen',1,2,'Bu eskizlerde','“Bu eskizlerde”, 1’de yapılan eskizlere gönderme yapar.'),
  ('once',2,3,'Beğenilen taslak','“Beğenilen taslak”, eskizlerde denemelerden sonra seçilir.'),
  ('son',4,None,'Böylece','“Böylece” tüm sürecin sonucunu verir; en sonda yer alır.')],
 ['giriş: ressamın doğrudan boyayla başlamadığını söyler','“Bunun yerine” ile doğrudan boyayla başlamanın karşıtını verir','“Bu eskizlerde” ile eskiz adımına bağlanır','“Beğenilen taslak” ile denemelerden sonra gelir','“Böylece” ile sonucu verir'],
 3,'A','“Bu eskizlerde”, “Beğenilen taslak” ve “Böylece” ifadeleri adımların sırasını belirler.',
 'Genel yargıyı bul; ardından “Bunun yerine” ile başlayan adımı ve ona gönderme yapan cümleyi sırala.','Genel bir durumdan sonra “bunun yerine” ile karşıt yöntemi getiren adım gelir; “bu” ile başlayan cümle hemen ardından yer alır.',203)

T4=['Gökyüzünün gündüz mavi görünmesinin nedeni, güneş ışığının atmosferdeki gazlarla karşılaşmasıdır.',
    'Bu ışık aslında bütün renkleri içerir ve renklerin her biri farklı bir dalga boyuna sahiptir.',
    'Mavi ışığın dalga boyu kısa olduğu için atmosferdeki gaz parçacıklarınca diğer renklerden çok daha fazla saçılır.',
    'Saçılan bu ışık, gökyüzünün her yönünden gözümüze ulaşır.',
    'Gün batımında ise ışık atmosferde daha uzun bir yol kat ettiğinden mavi neredeyse tümüyle elenir ve kırmızı tonlar öne çıkar.']
sira('0052','orta',T4,
 [('ilk',0,None,'','Olguyu ve nedenini ortaya koyan, öncül istemeyen cümle girişe uygundur.'),
  ('hemen',0,1,'Bu ışık','“Bu ışık”, 0’daki güneş ışığına gönderme yapar.'),
  ('hemen',1,2,'Mavi ışığın','“Mavi ışığın”, 1’de anılan renklerden mavi olana geçer; dalga boyu kavramı 1’de tanıtılmıştır.'),
  ('hemen',2,3,'Saçılan bu ışık','“Saçılan bu ışık”, 2’de saçıldığı söylenen mavi ışığa gönderme yapar.'),
  ('son',4,None,'Gün batımında ise','“Gün batımında ise” gündüzle karşıtlık kurar; gündüz olgusunun anlatımından sonra, sonda gelir.')],
 ['giriş: gökyüzünün mavi görünme nedenini söyler','“Bu ışık” ile güneş ışığına bağlanır','“Mavi ışığın” ile renklerin içinden maviyi seçer','“Saçılan bu ışık” ile saçılan maviye bağlanır','“Gün batımında ise” ile gündüzle karşıtlık kurar'],
 4,'D','“Bu ışık”, “Mavi ışığın” ve “Saçılan bu ışık” gönderme zinciri kurar; “ise” karşıtlık bildirir.',
 'Gönderme zincirini izle: ışık → renkler → mavi → saçılan ışık.','Bir olgunun açıklandığı paragrafta karşıt durum (gün batımı) olgunun anlatımından sonra gelir.',204)

T5=['Merak, çoğu zaman bilgiyi izleyen değil, ona öncülük eden bir duygudur; insan, bilmediği bir şeyin peşine düşerek öğrenir.',
    'Çocuk, dünyaya dair hiçbir şey bilmediği hâlde daha ilk yıllarından itibaren sorular sormaya başlar ve aldığı her yanıtla yenisini arar.',
    'Soruların sayısı arttıkça bilgi birikir, ama bilgi arttıkça daha önce akla gelmeyen yeni sorular da doğar ve cevap aramak yeniden başlar.',
    'Bu döngü, merakın bilgiyle sönmediğini, tersine bilgiyle beslendiğini ve böylece öğrenmenin hiçbir zaman bitmeyen bir yolculuğa dönüştüğünü gösterir; bilgi, merakın düşmanı değil yakıtıdır.',
    'Dolayısıyla öğrenmeyi sürdürmek isteyen biri, bilgisini artırırken merakını da canlı tutmaya çalışmalıdır; çünkü bilgiyi çoğaltan şey, çoğu zaman bitmeyen bir soru arayışıdır.']
sira('0053','zor',T5,
 [('ilk',0,None,'','Merakı genel bir yargıyla tanımlayan, öncül istemeyen cümle girişe uygundur.'),
  ('once',0,1,'bilmediği hâlde','“hiçbir şey bilmediği hâlde sorar” cümlesi, merakın bilgiden önce geldiği genel yargısının örneğidir; yargıdan sonra gelir.'),
  ('hemen',1,2,'Soruların','“Soruların”, 1’de anılan sorulara gönderme yapar.'),
  ('hemen',2,3,'Bu döngü','“Bu döngü”, 2’de anlatılan soru–bilgi–soru döngüsüne gönderme yapar.'),
  ('son',4,None,'Dolayısıyla','“Dolayısıyla” anlatılanlardan sonuç çıkarır; en sonda yer alır.')],
 ['giriş: merakı genel bir yargıyla tanımlar','örnek: çocuğun bilmeden sormasıyla genel yargıyı destekler','“Soruların” ile çocuğun sorularına bağlanır','“Bu döngü” ile soru–bilgi döngüsüne bağlanır','“Dolayısıyla” ile sonuç çıkarır'],
 -2,'B','“Soruların”, “Bu döngü” ve “Dolayısıyla” zinciri kurar; genel yargı ile örnek arasındaki ilişki anlamdan gelir.',
 'Genel yargıyı, onu somutlaştıran örneği ve sonucu bildiren cümleyi bul.','Genel yargı örnekten, sonuç da her ikisinden sonra gelir; gönderme yapan “bu” cümleleri ilgili cümlenin arkasındadır.',205)

# ================= GİRİŞ CÜMLESİ OLABİLEN / OLAMAYAN (3) =================
# 0054 · kolay · olamaz · A
giris('0054','kolay','olamaz',
 ('Bu eserler, ziyaretçilerin tarihle yüz yüze gelmesini sağlar.','Bu eserler'),
 [('Müzeler, bir toplumun belleğini koruyan kurumlardır.','Kendi başına anlaşılır; konuyu tanıtır ve gönderme ya da bağlaç taşımaz.','dikkat'),
  ('Bir müzede sergilenen eser, yalnızca bir nesne değil, bir dönemin tanığıdır.','Cümle kendi içinde tamdır; önceden söylenmiş bir şeye dayanmaz.','dikkat'),
  ('Müze gezmek, çocuklar için tarihi ders kitabından daha canlı öğrenmenin yoludur.','Zamir ya da bağlaç yoktur; bağımsız bir yargı olduğundan giriş olabilir.','dikkat'),
  ('Her müzenin kendine özgü bir koleksiyonu ve sergileme anlayışı vardır.','Genel bir bilgi veren bu cümle öncül istemez; paragrafı başlatabilir.','dikkat')],
 'A','Hangi cümlede önceden anılmış bir şeyi gösteren sözcük (bu, şu, o) var?',
 '“Bu eserler” gibi bir göndermeyle başlayan cümle, eserlerin daha önce anıldığını varsayar; giriş olamaz.',
 kok='Müzeler üzerine yazılan bir paragrafın giriş cümlesi olamayacak cümle aşağıdakilerden hangisidir?')

# 0055 · orta · olabilir · B
giris('0055','kolay','olabilir',
 ('Rüzgâr türbinleri, havanın hareket enerjisini elektriğe dönüştüren makinelerdir.',''),
 [('Bununla birlikte türbinlerin kuruluş maliyeti oldukça yüksektir.','Bununla birlikte','“Bununla birlikte” önce söylenmiş bir olumlu yargıya karşılık gelir; paragrafın başında kullanılamaz.','bilgi'),
  ('Öte yandan kuş göçlerinin geçtiği bölgelerde bu tesisler özenle planlanmalıdır.','Öte yandan','“Öte yandan” daha önce anlatılan bir yöne karşıt yön ekler; “bu tesisler” de önceki bir cümleyi gerektirir.','bilgi'),
  ('Ayrıca türbin kanatlarının uzunluğu üretilen enerjiyi doğrudan etkiler.','Ayrıca','“Ayrıca” daha önce söylenmiş bir bilgiye ekleme yapar; giriş olamaz.','bilgi'),
  ('Söz konusu makineler, yüksek ve esintili bölgelere kurulduğunda verimli çalışır.','Söz konusu','“Söz konusu makineler”, daha önce anılmış makinelere gönderme yapar; giriş olamaz.','bilgi')],
 'B','Her şıkta öncül isteyen bağlaç ya da gönderme sözcüğü ara; hiç taşımayan cümle girişe uygundur.',
 'Giriş cümlesi konuyu ilk kez tanıtır; öncül gerektiren sözcük taşımaz.',
 kok='Rüzgâr enerjisi üzerine yazılmış bir paragrafın ilk cümlesi aşağıdakilerden hangisi olabilir?')

# 0056 · zor · olabilir · E
giris('0056','zor','olabilir',
 ('Çocukların konuşma hataları, dil kurallarını keşfettiklerinin işaretidir.',''),
 [('Çocuk, dil öğrenirken söz konusu kuralları kimse öğretmeden kendi başına keşfeder.','söz konusu','“söz konusu kurallar”, daha önce anılmış kurallara gönderme yapar; cümlenin ortasında olsa bile öncül ister.','bilgi'),
  ('Bebeklerin ilk sözcükleri, anne babanın bu davranışa gösterdiği tepkiyle pekişir.','bu davranışa','“bu davranış” daha önce anılmış bir davranışa gönderme yapar; cümlede karşılığı yoktur, öncüle dayandığı için giriş olamaz.','bilgi'),
  ('Diğer yandan çocuklar, kuralları ezberleyerek değil, örnekleri karşılaştırarak çıkarır.','Diğer yandan','“Diğer yandan” önceki bir yöne karşıt yön ekler; paragrafı başlatamaz.','bilgi'),
  ('Nitekim dil edinimi, ilk beş yıl içinde büyük ölçüde tamamlanır.','Nitekim','“Nitekim” daha önce söylenmiş bir yargıyı doğrulayan bir cümle başlatır; giriş olamaz.','bilgi')],
 'E','Cümlenin başında da içinde de öncüle dayanan bir sözcük ara: nitekim, söz konusu, bu davranış, diğer yandan.',
 'Cümle ortasındaki “söz konusu, bu davranış” gibi göndermeler de cümleyi öncüle bağlar; ama cümle içi bağlaçlar ve karşılığı cümlenin içinde bulunan zamirler bağlamaz.',
 kok='Çocuklarda dil edinimini anlatan bir yazının girişinde aşağıdaki cümlelerden hangisi giriş cümlesi olabilir?')
