"""TYT Türkçe · Paragrafta Birden Çok Soru (ortak parça): 10 parça x 2 soru = 20 ana soru (hafif mod). Metinler özgündür."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from hafif_dilbilgisi import *
KY='ÖSYM 2018–2026 (paragrafta anlam; birden çok soru) · Paraf İQ · Sıfır Risk'
def kart(alt,fikir,tuzak,z,tip,adim): return dict(alt=alt,fikir=fikir,tuzak=tuzak,zorluk=z,kalip='düz',adim=adim,tipId=tip,kaynak=KY)
KARTLAR={
 'K-PIK-01':kart('Ortak Parça · Ana Düşünce','Parçanın tümünü kapsayan asıl yargıyı, ayrıntı ve örneklerden ayırarak bulmak.','Parçadaki bir ayrıntıyı ya da fazla geniş bir genellemeyi ana düşünce sanmak.','orta','pik-ana',3),
 'K-PIK-02':kart('Ortak Parça · Ulaşılamayan Yargı','Dört şıkkın parçada karşılığını bulup parçadan çıkmayan yargıyı seçmek.','Olumsuz kökü gözden kaçırıp parçadan çıkan yargıyı seçmek.','orta','pik-ulasilamaz',3),
 'K-PIK-03':kart('Ortak Parça · Değinilmeyen','Parçada geçen dört konuyu eşleyip hiç geçmeyeni bulmak.','Konuyla ilgili görünen ama parçada geçmeyen yargıyı var saymak.','orta','pik-degin',3),
 'K-PIK-04':kart('Ortak Parça · Altı Çizili Söz','Sözün bağlam içindeki yan ya da mecaz anlamını bulmak.','Sözcüğün sözlük anlamına bağlı kalıp bağlamı atlamak.','orta','pik-altcizili',3),
 'K-PIK-05':kart('Ortak Parça · Çıkarım','Parçadan kesin olarak çıkarılabilecek yargıyı, parçada söylenmeyen akla yatkın genellemelerden ayırmak.','Parçada geçmeyen “her, hiç, yalnızca” içeren genellemeyi doğru saymak.','zor','pik-cikarim',4),
 'K-PIK-06':kart('Ortak Parça · Anlatım Tekniği','Parçada kullanılan düşünceyi geliştirme yolunu cümleyle eşleyip kullanılmayan yollardan ayırmak.','Benzer iki yolu karıştırmak.','orta','pik-yapi',3),
}
TIPLER={'pik-ana':'Ortak parça: ana düşünce','pik-ulasilamaz':'Ortak parça: ulaşılamayan yargı','pik-degin':'Ortak parça: değinilmeyen','pik-altcizili':'Ortak parça: altı çizili sözün anlamı','pik-cikarim':'Ortak parça: çıkarılabilecek yargı','pik-yapi':'Ortak parça: anlatım tekniği'}
Q=kur('pikili','Paragrafta Birden Çok Soru','tr|Paragraf',KARTLAR,TIPLER); Q.n=20
B_ANA=B('Ana düşünce','parçanın tümüne yayılan asıl mesajdır; ayrıntı ve örnekler onu destekler, yerine geçmez. Örnek: “Spor sağlığı korur” ana, “yüzmek omurgaya iyi gelir” ayrıntıdır')
B_ULA=B('Ulaşılamaz / değinilmemiş kökü','doğru şık parçadan çıkmayan ya da parçada geçmeyen şıktır; öbür dört şıkkın her biri parçada karşılık bulur')
B_ALT=B('Altı çizili söz','sözün anlamı cümlenin bağlamından çıkarılır; sözlük anlamı ile bağlamdaki anlam farklı olabilir. Örnek: “kapıyı çaldı” = zili/kapıyı vurdu, “sınavı çaldı” = bilgiyi ele geçirdi diye yorumlanmaz')
B_CIK=B('Çıkarım','parçada açık yazılanlardan zorunlu olarak doğan yargıdır; “her, hiç, yalnızca” gibi fazla kesin sözlerle genellenmiş şıklar çoğunlukla çıkarılamaz')
B_YOL=B('Düşünceyi geliştirme yolları','tanımlama · örnekleme · karşılaştırma · tanık gösterme · benzetme · sayısal veri. Hangisi varsa parçada ona ait bir cümle gösterilebilir')
CFG={ # tip -> (tur, kök, istenen, puf, bilgi, adım başlıkları)
 'ana':('bilgi','Bu parçada asıl anlatılmak istenen aşağıdakilerden hangisidir?','Parçanın tümünü kapsayan asıl mesaj.','Ana düşünce parçanın tümünü kapsar; yalnız bir cümleyi özetleyen şık ayrıntıdır.',[B_ANA]),
 'ula':('dikkat',None,'Parçadan çıkarılamayan yargı.','“Ulaşılamaz” sorusunda doğru şık parçada karşılığı olmayan şıktır.',[B_ULA]),
 'deg':('dikkat',None,'Parçada geçmeyen konu.','“Değinilmemiştir” sorusunda parçada geçen dört konuyu elersen cevap kalır.',[B_ULA]),
 'alt':('bilgi',None,'Altı çizili sözün bağlamdaki anlamı.','Altı çizili sözün anlamını cümlenin öncesi ve sonrasındaki yargıdan çıkar.',[B_ALT]),
 'cik':('bilgi','Bu parçadan aşağıdakilerden hangisi çıkarılabilir?','Parçadan kesin olarak çıkarılabilecek yargı.','Çıkarım, parçada söylenenden zorunlu olarak doğan yargıdır; fazla kesin söz içeren şık çoğunlukla çıkmaz.',[B_CIK]),
 'yol':('bilgi','Bu parçada düşünceyi geliştirme yollarından hangisine başvurulmuştur?','Parçada kullanılan düşünceyi geliştirme yolu.','Bir yolu seçmeden önce parçada ona ait bir cümle göster.',[B_YOL]),
}
TIPKART={'ana':'K-PIK-01','ula':'K-PIK-02','deg':'K-PIK-03','alt':'K-PIK-04','cik':'K-PIK-05','yol':'K-PIK-06'}
KAZ={'ana':'Paragrafın ana düşüncesini belirler.','ula':'Parçadan ulaşılamayan yargıyı belirler.','deg':'Parçada değinilmeyen yargıyı belirler.','alt':'Altı çizili sözle anlatılmak istenen anlamı belirler.','cik':'Parçadan çıkarılabilecek yargıyı belirler.','yol':'Parçadaki düşünceyi geliştirme yolunu belirler.'}
LETTERS=list('ACBDCEDAEBADCEBDEABC')
SPEC=[]
def PQ(no,tip,zor,parca,dogru,yan,ozet,dayanak,ip,kok=None):
    """dogru=(şık, etiket); yan=4 x (şık, etiket, neden)"""
    SPEC.append(dict(no=no,tip=tip,zor=zor,parca=parca,dogru=dogru,yan=yan,ozet=ozet,dayanak=dayanak,ip=ip,kok=kok))
KU='Bu parçadan aşağıdakilerin hangisine ulaşılamaz?'
KD='Bu parçada aşağıdakilerden hangisine değinilmemiştir?'
def KA(s): return f'Bu parçada “{s}” sözüyle anlatılmak istenen aşağıdakilerden hangisidir?'
# ---------------- 1 yürüyüş ----------------
P1=('Yürümek, insanın en eski ve en ucuz ulaşım biçimi olmakla birlikte günümüzde giderek ihmal edilen bir alışkanlıktır. Kısa mesafeleri bile araçla kat etmeye alışan kentli, günde birkaç yüz adım atarak yaşamını sürdürebilmektedir. Oysa düzenli yürüyüş yapan kişilerde kalp ve damar hastalıklarının daha seyrek görüldüğü, uyku düzeninin daha sağlıklı olduğu bilinir. Yürüyüşün yararı yalnızca bedenle sınırlı değildir; açık havada geçen yarım saat zihni de dinlendirir, insanın kafasındaki düğümleri çözmesine yardım eder. Bir sokağı ya da parkı arşınlamak, şehri yeniden tanımaya da fırsat verir. Pahalı bir ekipman, özel bir salon ya da uzun bir hazırlık gerektirmemesi de onu herkesin ulaşabileceği bir sağlık aracı hâline getirir. Bu nedenle sağlıklı yaşamak isteyen biri, işe başlarken karmaşık yöntemler aramak yerine önce ayakkabılarını bağlayıp kapıdan çıkmayı denemelidir.')
PQ('0001','ana','orta',P1,('Yürüyüş, herkesin yapabileceği ve beden ile zihne yarar sağlayan bir alışkanlıktır.','son cümle ve gerekçeler'),
 [('Kalp ve damar hastalıklarından korunmanın tek yolu düzenli yürüyüş yapmaktır.','fazla geniş','Parça yürüyenlerde bu hastalıkların seyrek görüldüğünü söyler; “tek yol” demez.'),
  ('Yürüyüş yapmak için pahalı bir ekipmana ya da özel bir salona gerek yoktur.','ayrıntı','Bu yargı parçada geçer ama yürüyüşün kolay ulaşılabilirliğini destekleyen bir ayrıntıdır; parçanın tamamını kapsamaz.'),
  ('Günümüzde insanlar kısa mesafeleri bile yürüyerek gitmeyi tercih etmektedir.','ters','Parça yürümenin günümüzde ihmal edildiğini söyler; şık parçaya terstir.'),
  ('Zihinsel yorgunluk yalnızca açık havada geçirilen zamanla giderilebilir.','fazla geniş','Parça açık havanın zihni dinlendirdiğini söyler; “yalnızca” ile fazla genelleme yapılmıştır.')],
 'Yürümek ucuz ve kolaydır; hem bedeni hem zihni olumlu etkiler.','“Bu nedenle” ile başlayan son cümle: herkes için kolay bir sağlık aracı olarak yürüyüşü önerir.','Parçanın tamamında yürüyüşün yararı ve kolaylığı anlatılıyor; bunu bir cümleyle özetle.')
PQ('0002','ula','kolay',P1,('Yürüyüş, her türlü spor dalından daha etkili bir sağlık yöntemidir.','parçada hiç geçmez'),
 [('Yürüyüşün bedene yararının yanında zihinsel bir yararı da vardır.','var','“açık havada geçen yarım saat zihni de dinlendirir” cümlesi bu yargıyı verir.'),
  ('Düzenli yürüyüş yapan kişilerin uyku düzeni daha sağlıklı olabilir.','var','“uyku düzeninin daha sağlıklı olduğu bilinir” cümlesi bu yargıyı verir.'),
  ('Yürüyüş yapmak için pahalı ya da özel bir donanım gerekmez.','var','“Pahalı bir ekipman … gerektirmemesi” cümlesi bu yargıyı verir.'),
  ('Yürüme alışkanlığı günümüzde eskisi kadar ilgi görmemektedir.','var','“giderek ihmal edilen bir alışkanlıktır” cümlesi bu yargıyı verir.')],
 'Ulaşılamaz: parçada karşılığı olmayan yargı.','Yürüyüşün başka sporlarla karşılaştırıldığı hiçbir cümle yoktur.','Dört şıkkın her biri için parçadan bir cümle göster.',KU)
# ---------------- 2 arılar ----------------
P2=('Arılar, bal üretmekten çok daha büyük bir görev üstlenir: tozlaşma. Bir çiçekten öbürüne konarken ayaklarına yapışan polen taneleri, bitkilerin döllenmesini sağlar. Yeryüzündeki yiyecek bitkilerinin önemli bir bölümü bu işleme muhtaçtır; elma, badem ve kabak gibi ürünler arı olmadan ya hiç meyve vermez ya da çok az verir. Bir kovandaki arılar yaz boyunca binlerce çiçeği ziyaret eder; bu ziyaretlerin her biri küçük görünse de toplamda bir ekosistemin dengesini kurar. Son yıllarda böcek ilaçlarının yaygınlaşması ve doğal yaşam alanlarının daralması arı topluluklarını zayıflatmıştır. Bu durum yalnızca arıcıları değil, sofrasında çeşit görmek isteyen herkesi ilgilendirir. Çünkü bir bölgedeki ürün verimi, çoğu zaman çevredeki arı topluluklarının sağlığına bağlıdır; zayıflayan bir topluluk, görünmeyen bir verim kaybı demektir. Bu yüzden arıların korunması, çevre meselesi olduğu kadar gıda güvenliği meselesidir.')
PQ('0003','deg','kolay',P2,('Arıların kovan içindeki iş bölümüne','parçada hiç geçmez'),
 [('Tozlaşmanın arıların ayaklarına yapışan polenle gerçekleştiğine','var','“ayaklarına yapışan polen taneleri” ifadesi bunu anlatır.'),
  ('Bazı meyve ve sebzelerin arıya muhtaç olduğuna','var','“elma, badem ve kabak …” cümlesi bunu söyler.'),
  ('Böcek ilaçları ile yaşam alanlarının daralmasının arıları zayıflattığına','var','“böcek ilaçlarının yaygınlaşması ve doğal yaşam alanlarının daralması” ifadesi bunu söyler.'),
  ('Arıların korunmasının gıda güvenliğiyle ilişkisine','var','son cümle bunu açıkça söyler.')],
 'Değinilmeyen: parçada hiç geçmeyen konu.','Parçada kovanın içinden değil, çiçek ziyaretlerinden söz edilir.','Her şıkkı parçada bir ifadeyle eşle; eşleşmeyen cevaptır.',KD)
PQ('0004','ana','orta',P2,('Arılar, tozlaşmayla gıda güvenliğine katkı sağladığı için korunmalıdır.','son cümle'),
 [('Arılar, bal üretiminden çok tozlaşmayla ilgilenen canlılardır.','yan düşünce','Parçanın ilk cümlesindeki bir karşılaştırmadır; asıl mesaj korumanın gerekliliğidir.'),
  ('Böcek ilaçları, arı topluluklarını zayıflatan tek etken olarak görülmelidir.','fazla geniş','Parça ilaçların yanında yaşam alanlarının daralmasını da sayar; “tek etken” yargısı yoktur.'),
  ('Elma, badem ve kabak gibi ürünler yalnızca arılar sayesinde yetişir.','fazla geniş','Parça bu ürünlerin arı olmadan “ya hiç ya da çok az” meyve verdiğini söyler; “yalnızca” aşırı bir genellemedir.'),
  ('Arıcılığın yaygınlaştırılması, çevre sorunlarıyla mücadelenin en önemli yoludur.','parçada yok','Parçada arıcılığın çevre mücadelesindeki yeri değerlendirilmez.')],
 'Arılar tozlaşmayla yiyecek bitkilerini yaşatır; zayıflamaları gıda sorunudur.','“Bu yüzden …” ile başlayan son cümle sonucu verir.','Son cümledeki “bu yüzden” hangi görüşü sonuç olarak veriyor?')
# ---------------- 3 tablo ----------------
P3=('Bir tabloya bakmak, ona bir kez bakıp geçmek demek değildir. Gözün tablo üzerinde gezinmesi, renklerin birbirine nasıl yaslandığını, ışığın hangi köşeden geldiğini fark etmesi zaman ister. Müzelerde saniyeler içinde bir salonu geçen ziyaretçi, sanatçının aylarca emek verdiği eseri adeta bir tabela gibi okur ve geçer. Oysa tablo, acele edenin değil bekleyenin önünde açılır. Bir resmin önünde on dakika durmayı alışkanlık hâline getiren kişi, kısa sürede ayrıntıları görmenin tadını keşfeder ve sanata bakışı değişir. Hızın ödüllendirildiği bir çağda bir resmin önünde durmak, kendi başına küçük bir direniştir; çünkü sanat, izleyiciden önce zamanını ister. Böyle bir ziyaretçi için müze, tek bir günde bitirilecek bir liste değil, her gelişte biraz daha açılan bir kapıdır. Sanatçının fırça darbelerindeki tereddüdü ya da kararlılığı yakalamak da ancak bu sabırla mümkündür.')
PQ('0005','alt','kolay',P3,('Eseri derinlemesine incelemeden yüzeysel görüp geçer.','bağlam: saniyeler içinde geçme'),
 [('Eserin altındaki tabelada yazılanları tek tek dikkatle okur.','sözlük anlamı','“Tabela” sözcüğünün gerçek anlamına bağlı kalınmış; oysa cümle hızla geçmeyi anlatır.'),
  ('Sanatçının adını öğrenmek için tabeladaki yazıya bakar.','sözlük anlamı','Parçada sanatçının adının öğrenilmesinden söz edilmez; söz mecazdır.'),
  ('Eseri beğenmediği için ona hiç bakmadan hızla uzaklaşır.','parçada yok','Parça hızla geçişin nedenini beğenmemek olarak göstermez, acele ve yüzeysellik olarak gösterir.'),
  ('Tabloyu bir yazı gibi satır satır çözümlemeye çalışır.','ters','Parçada ziyaretçi çözümleme yapmaz; tam tersine acele eder.')],
 'Hızlı geçen ziyaretçi eseri bir tabelaya bakar gibi göz ucuyla okur ve geçer.','Sonraki cümledeki “Oysa tablo, acele edenin değil bekleyenin önünde açılır” cümlesi sözün anlamını belirler.','Sözün hemen ardından gelen “oysa” cümlesine bak.',KA('tabela gibi okur ve geçer'))
PQ('0006','ula','orta',P3,('Müzeler, ziyaretçi için salonlarını yeniden düzenlemelidir.','parçada hiç geçmez'),
 [('Bir tabloyu anlamak için ona yeterince zaman ayırmak gerekir.','var','“Gözün … fark etmesi zaman ister” cümlesi bu yargıyı verir.'),
  ('Salonları hızla gezen ziyaretçi, eseri yüzeysel görür.','var','“tabela gibi okur ve geçer” sözü bunu anlatır.'),
  ('Sanatçılar, eserlerini oluştururken uzun süre emek verir.','var','“aylarca emek verdiği eser” ifadesi bunu söyler.'),
  ('Resmin önünde sabırla bekleyen kişi, ayrıntıları fark eder.','var','“ayrıntıları görmenin tadını keşfeder” cümlesi bunu söyler.')],
 'Ulaşılamaz: parçada karşılığı olmayan yargı.','Müze düzeni ya da ziyaretçi sayısı hiç geçmez.','Dört şıkkı parçada ara; karşılığı olmayanı seç.',KU)
# ---------------- 4 telefon ----------------
P4=('Telefonumuzda her şeyin kaydı var: randevular, telefon numaraları, doğum günleri. Bu kolaylık, beynimizin bilgiyi saklama çabasını azaltıyor. Nitekim pek çok kişi en yakın arkadaşının numarasını ezbere bilmiyor. Kaslar gibi, zihinsel yetiler de kullanılmadıkça zayıflar. Adresleri, şifreleri, hatta bir dostumuzun doğum gününü hatırlama işini de aynı şekilde cihaza bıraktık. Bu alışkanlık ilk bakışta zararsız görünür; ancak yıllar içinde zihnin kendi başına bulma becerisi körelir. Bu körelme çoğu zaman ihtiyaç duyulduğu anda fark edilir. Bu, teknolojiyi bırakmamız gerektiği anlamına gelmez; ancak her bilgiyi cihaza devretmek yerine bazılarını bilinçli olarak aklımızda tutmaya çalışmak, belleğimizi canlı tutmanın yoludur. Örneğin yolu navigasyona sormadan önce rotayı kafamızda canlandırmaya çalışmak küçük ama etkili bir egzersizdir. Teknoloji, ona ihtiyaç duyduğumuzda yardım eden bir araç olmalı, düşünmeyi üstlenen bir vekil olmamalıdır.')
PQ('0007','ana','kolay',P4,('Teknoloji kullanırken zihin yetilerimizi çalıştırmalıyız.','son cümle ve ortadaki öneri'),
 [('Telefonlar insanın hafızasını tümüyle yok etmektedir.','fazla geniş','Parça belleğin zayıflayabileceğini söyler; “yok etmektedir” abartıdır.'),
  ('Telefon numaralarını ezberlemek günümüzde gereksizdir.','ters','Parça bazı bilgilerin bilinçli olarak aklda tutulmasını önerir.'),
  ('Kullanılmayan zihinsel yetiler zamanla körelir ve zayıflar.','gerekçe','Bu yargı parçada geçer ama ana düşünceyi destekleyen bir gerekçedir.'),
  ('Cihazların kayıt özelliği kullanıcıya büyük kolaylık sağlar.','yan düşünce','Parçanın ilk cümlelerindeki bir tespittir; parçanın vardığı sonuç değildir.')],
 'Telefon her şeyi saklıyor, zihin yetileri kullanılmayınca zayıflıyor; öyleyse bazı bilgileri kafada tutmalıyız.','Son cümle teknolojiyi araç, düşünmeyi insanın işi olarak kurar.','“Teknoloji bir araç olmalı” cümlesi hangi mesajı veriyor?')
PQ('0008','deg','orta',P4,('Çocukların telefonla geçirdiği sürenin sınırlanması gerektiğine','parçada hiç geçmez'),
 [('Telefonda randevu ve doğum günü gibi kayıtların tutulduğuna','var','ilk cümle bunu söyler.'),
  ('Pek çok kişinin arkadaşının numarasını ezbere bilmediğine','var','“Nitekim pek çok kişi …” cümlesi bunu söyler.'),
  ('Kullanılmayan zihinsel yetilerin zayıfladığına','var','“zihinsel yetiler de kullanılmadıkça zayıflar” cümlesi bunu söyler.'),
  ('Rotayı kafada canlandırmanın bir egzersiz olabileceğine','var','“Örneğin yolu navigasyona sormadan önce …” cümlesi bunu söyler.')],
 'Değinilmeyen: parçada hiç geçmeyen konu.','Çocuklardan ya da süre sınırından hiç söz edilmez.','Her şık için parçadan bir cümle göster; gösteremediğin cevaptır.',KD)
# ---------------- 5 hata ----------------
P5=('Okulda hata yapmak çoğu zaman utanılacak bir durum olarak öğretilir. Yanlış cevap veren öğrenci, sınıfın önünde küçük düşmemek için bir sonraki sefere sessiz kalmayı seçer. Oysa öğrenmenin en verimli anları, yanlışın fark edildiği anlardır. Bir problemi yanlış çözen öğrenci, neden yanlış olduğunu araştırırsa konuyu daha derinlemesine kavrayabilir. Hatayı cezalandıran bir sınıf ortamı, öğrencileri riskten kaçınan, yalnızca kesin bildiğini söyleyen çocuklar hâline getirir; hatayı bir bilgi kaynağı sayan ortam ise cesur düşünmeyi besler. Buna karşılık bazı sınıflarda öğretmen, yanlış cevabı bir hata olarak değil, birlikte çözülecek bir bulmaca olarak karşılar; böyle sınıflarda parmak kaldıran öğrenci sayısı artar. Bu sınıflarda yanlış, saklanacak bir şey olmaktan çıkar. Bu nedenle öğretmenin sınıfta yanlışa verdiği ilk tepki, çoğu zaman o dersin geri kalanının havasını belirler.')
PQ('0009','cik','orta',P5,('Hataya gösterilen tepki, öğrencilerin derse katılma isteğini etkiler.','“sessiz kalmayı seçer” ve son cümle'),
 [('Doğru çözen öğrenciler, yanlış çözenlerden daha çok soru sorar.','parçada yok','Parça doğru çözenlerin soru sorma sıklığından söz etmez.'),
  ('Öğrencilerin çoğu, hata yapmaktan korktuğu için sınavlarda başarısız olur.','fazla geniş','Parça bazı öğrencilerin sessiz kaldığını söyler; sınav başarısına ilişkin bir yargı parçadan çıkmaz.'),
  ('Öğretmenler, yanlış cevap veren öğrencilerin sorularına yanıt vermemelidir.','ters','Parçanın savunduğu cesur düşünmeyle çelişir.'),
  ('Yanlış cevaplar, sınav notlandırmasında hiç dikkate alınmamalıdır.','parçada yok','Parça notlandırmadan söz etmez.')],
 'Hatayı cezalandıran ortam öğrenciyi susturur, hatayı bilgi sayan ortam cesur düşünceyi besler.','“Sessiz kalmayı seçer” ile “cesur düşünmeyi besler” ifadeleri tutumun katılımı belirlediğini gösterir.','Hataya verilen tepki ile öğrencinin davranışı arasında nasıl bir ilişki kurulmuş?')
PQ('0010','alt','kolay',P5,('Yanlışlardan ders çıkarılmasını özendiren öğrenme ortamı','bağlam: “cesur düşünmeyi besler”'),
 [('Öğrencilerin kaynaklara serbestçe ulaştığı kütüphane ortamı','sözlük anlamı','“Bilgi kaynağı” sözüne gerçek anlamıyla bağlanılmış; parçada kütüphaneden söz edilmez.'),
  ('Yanlış yapanın hiç uyarılmadığı gevşek bir sınıf düzeni','parçada yok','Parça uyarılmamaktan değil, yanlışa gösterilen tutumdan söz eder.'),
  ('Kesin bilgilerin ezberletildiği, soru sorulmayan ders ortamı','ters','Parçada kesin bildiğini söyletenler hatayı cezalandıran ortamdır.'),
  ('Hata yapan öğrencinin sınıftan çıkarıldığı ortam','ters','Bu, hatayı cezalandıran ortamı anlatır; sözün anlamıyla çelişir.')],
 'Hatayı bir bilgi kaynağı sayan ortam, yanlıştan öğrenmeyi özendiren ortamdır.','Cümlenin devamı “cesur düşünmeyi besler” diyerek anlamı belirler.','Sözün karşısındaki “hatayı cezalandıran ortam”a bak.',KA('hatayı bir bilgi kaynağı sayan ortam'))
# ---------------- 6 akarsu ----------------
P6=('Akarsular, yalnızca suyun aktığı yataklar olmanın ötesinde uygarlıkların doğduğu yerlerdir. Çünkü verimli toprak, içme suyu ve ulaşım olanağı bir arada çoğunlukla nehir kıyılarında bulunur. Bu yüzden insanlık tarihinin ilk büyük yerleşimleri ırmak boylarında kurulmuştur. Nil, Fırat ve Dicle gibi nehirlerin vadilerindeki medeniyetler bu duruma örnek gösterilebilir. Tarım, kentleşme ve ticaret bu vadilerde birbirini besleyerek büyümüştür. Ancak bugün akarsuların kıyıları betonla kaplanmakta, yatakları daraltılmakta, kirlenen sular canlı yaşamını tehdit etmektedir. Akarsulara sahip çıkan toplumlar geçmişte yükselmiş, onları ihmal edenler ise zamanla gerilemiştir. Bunun nedeni basittir: su, bir toplumun tarımını, ticaretini ve sağlığını aynı anda belirler. Yeni kuşakların akarsuyu bir tehdit olarak değil, ortak bir miras olarak görmesi için çocuklara akarsu bilinci erken yaşta kazandırılmalıdır. Bu nedenle akarsuyu korumak, geleceği korumak demektir.')
PQ('0011','ana','orta',P6,('Akarsular, uygarlıkların temelini oluşturduğu için korunmalıdır.','son cümle'),
 [('Nil, Fırat ve Dicle vadilerinde tarım, kentleşme ve ticaret birbirini beslemiştir.','ayrıntı','Bu yargı parçada geçer ama yalnızca bir örnektir; parçanın ana mesajını (korunması gerektiğini) vermez.'),
  ('Akarsu kıyılarının betonla kaplanması, kentleşmenin gereğidir.','ters','Parça betonlaşmayı akarsuyu tehdit eden bir durum olarak sunar.'),
  ('Bugün akarsuların kıyıları betonla kaplanmakta, yatakları daraltılmaktadır.','ayrıntı','Bu yargı parçada geçer ama yalnızca bir ayrıntıdır; parçanın tamamını kapsamaz.'),
  ('Akarsuya sahip olan her toplum güçlü bir uygarlık kurmuştur.','fazla geniş','Parça “sahip çıkan” toplumların yükseldiğini söyler; “sahip olan her toplum” genellemesi yapılmaz.')],
 'Akarsu uygarlıkları doğurmuş; ihmal edilince toplumlar gerilemiş; bu yüzden korunmalı.','“Bu nedenle” ile başlayan son cümle sonucu verir.','Son cümle parçanın vardığı yargıyı söylüyor.')
PQ('0012','yol','orta',P6,('Örneklendirme','“Nil, Fırat ve Dicle gibi nehirlerin vadilerindeki medeniyetler bu duruma örnek gösterilebilir.”'),
 [('Tanık gösterme','yok','Parçada bir uzmanın sözüne başvurulmaz.'),
  ('Sayısal verilerden yararlanma','yok','Parçada sayı, yüzde ya da oran verilmez.'),
  ('Benzetme','yok','Bir varlık, ortak bir yönü nedeniyle başka bir varlığa benzetilmez.'),
  ('Kişileştirme','yok','Cansız varlıklara insana özgü nitelikler verilmez.')],
 'Nil, Fırat ve Dicle örnek verilerek düşünce somutlaştırılmış.','“Örneğin”, “… gibi”, “örnek gösterilebilir” ifadeleri örneklendirmenin işaretidir.','Hangi yolun parçada gösterilebilecek bir cümlesi var?')
# ---------------- 7 dil ----------------
P7=('Bir dilde yabancı sözcük kullanılması tek başına bir tehlike değildir; diller tarih boyunca birbirinden sözcük almış, aldıklarını kendi ses düzenlerine uydurarak benimsemiştir. Asıl sorun, karşılığı varken bile yabancısının tercih edilmesi ve bu tercihin bir ayrıcalık göstergesi sayılmasıdır. Böyle bir tutum, dilin kendi üretkenliğine olan güveni zedeler; yeni bir kavramla karşılaşan kişi, karşılık üretmek yerine hazır sözcüğü almaya alışır. Nitekim bir sözcüğün karşılığını bulmak için harcanan emek, çoğu zaman dilin kendi kaynaklarını yeniden keşfetmesine de vesile olur. Kullanılmayan kaynaklar ise zamanla unutulur. Oysa bir dil, ancak yeni sözcükler türetebildiği sürece gelişmeye devam eder. Türetme, toplumun yeni bir kavramı kendi malzemesiyle kavradığının göstergesidir; yalnızca bir sözcük bulmak değil, kavramı sindirmek demektir. Bu nedenle dil politikası, alıntı sözcükleri yasaklamaya değil, türetmeyi özendirmeye dayanmalıdır.')
PQ('0013','ula','orta',P7,('Alıntı sözcüklerin dilden tümüyle çıkarılması, dilin gelişmesi için zorunludur.','parçayla çelişir'),
 [('Yabancı sözcük almak, tek başına bir dil sorunu sayılmaz.','var','“tek başına bir tehlike değildir” cümlesi bunu söyler.'),
  ('Alınan sözcükler çoğu zaman alıcı dilin ses düzenine uydurulur.','var','“kendi ses düzenlerine uydurarak benimsemiştir” ifadesi bunu söyler.'),
  ('Karşılığı bulunan yabancı sözcüğün tercih edilmesi bir ayrıcalık gibi görülebilir.','var','“bir ayrıcalık göstergesi sayılmasıdır” ifadesi bunu söyler.'),
  ('Sözcük türetmek, kavramı sindirmenin bir göstergesidir.','var','“kavramı sindirmek demektir” ifadesi bunu söyler.')],
 'Ulaşılamaz: parçayla çelişen ya da parçada olmayan yargı.','Parça alıntıyı yasaklamayı değil türetmeyi özendirmeyi savunur.','Parça yasaklama konusunda ne diyor? Bu şık onunla uyuşuyor mu?',KU)
PQ('0014','ana','zor',P7,('Dilin gelişmesi, yasaklarla değil, türetmeyi özendirmekle sağlanır.','son cümle ve “Oysa bir dil, ancak …”'),
 [('Diller arasındaki sözcük alışverişi, dilin üretkenliğini azaltan bir olgudur.','ters','Parça sözcük alışverişini “tek başına tehlike” saymaz; sorun tercih biçimindedir.'),
  ('Karşılığı bulunan yabancı sözcüklerin kullanımı, dil bilinci eksikliğinin göstergesidir.','yan düşünce','Parça bu tutumu eleştirir ama asıl mesajı türetmeyi özendirmektir; şık parçanın yalnız bir yönünü söyler.'),
  ('Dil politikası, toplumun yeni kavramlara uyumunu hızlandırmayı hedeflemelidir.','parçada yok','Parça uyum hızından değil türetmeden söz eder.'),
  ('Yeni kavramlarla karşılaşan kişiler, hazır sözcüğü almaya yönelir.','gözlem','Bu bir tespittir ve parçada geçer; ana düşünce değildir.')],
 'Yabancı sözcük tek başına sorun değil; asıl çözüm türetmeyi özendirmektir.','Son cümle: “yasaklamaya değil, türetmeyi özendirmeye dayanmalıdır”.','Parçanın vardığı sonucu “Oysa” ile başlayan cümleye ve “Bu nedenle” ile başlayan son cümleye bakarak bul.')
# ---------------- 8 futbol ----------------
P8=('İyi bir futbol takımını izlerken fark edilen ilk şey, topun sahipsiz kalmamasıdır. Oyuncular, topu yalnızca bir araç olarak değil, birbirlerine duydukları güvenin taşıyıcısı olarak görürler. Her pas, “sana güveniyorum” demenin sessiz yoludur. Yıldız oyuncularla dolu ama birbirine pas vermeyen takımlar, çoğu zaman sahada dağınık ve verimsiz kalır. Seyirci ise sonuçtan önce bu uyumu hisseder; çünkü bir takımın gücü, attığı gol sayısından çok o gollere giden yolda kaç kişinin ortak emek verdiğinde yatar. Takım olmak, yetenekleri toplamak değil, yetenekleri birbirine bağlamaktır. Bu bağ kurulduğunda küçük bir kadro bile, tek tek daha yetenekli ama birbirinden kopuk bir kadroyu geride bırakabilir. Antrenmanda en çok çalışılması gereken şey de bu bağı güçlendirmektir. Bu yüzden hazırlık dönemlerinin büyük bölümü, bireysel hareketlerden çok ortak hareketlere ayrılmalıdır.')
PQ('0015','alt','orta',P8,('Pas vermek, oyuncunun takım arkadaşına güven göstermesidir.','önceki cümle: “güvenin taşıyıcısı”'),
 [('Oyuncular, pas verirken takım arkadaşlarıyla hiç konuşmamalıdır.','sözlük anlamı','“Sessiz yol” sözüne gerçek anlamıyla bağlanılmış; cümle güvenin göstergesinden söz eder.'),
  ('Pas, takımın sorumluluğunu tek bir oyuncuya devretmektir.','yan anlam','Parça uyumdan ve ortak emekten söz eder; sorumluluğun tek kişiye devrinden söz etmez.'),
  ('Pas vermek, topu kaybetme riskini en aza indirmenin yoludur.','parçada yok','Parça pasın riskinden değil, güveni göstermesinden söz eder.'),
  ('Pas, oyuncuların birbirini oyun içinde uyarma biçimidir.','parçada yok','Cümlede uyarıdan değil, güven göstermesinden söz edilir.')],
 'Her pas, “sana güveniyorum” mesajını sessizce vermektir.','Cümleden önceki “güvenin taşıyıcısı” ifadesi anlamı belirler.','Söz, öncesindeki cümleyle birlikte okunursa “güven” anahtar sözcüktür.',KA('Her pas, ‘sana güveniyorum’ demenin sessiz yoludur'))
PQ('0016','deg','orta',P8,('Antrenörün oyun planını belirlemedeki rolüne','parçada hiç geçmez'),
 [('Topun sahipsiz kalmamasının iyi takımın bir özelliği olduğuna','var','ilk cümle bunu söyler.'),
  ('Yıldız oyuncularla dolu bir takımın dağınık kalabileceğine','var','“Yıldız oyuncularla dolu ama birbirine pas vermeyen takımlar …” cümlesi bunu söyler.'),
  ('Seyircinin takım uyumunu sonuçtan önce hissettiğine','var','“Seyirci ise sonuçtan önce bu uyumu hisseder” cümlesi bunu söyler.'),
  ('Küçük bir kadronun birbirine bağlıysa daha yetenekli ama kopuk kadroyu geçebileceğine','var','sondan üçüncü cümle bunu söyler.')],
 'Değinilmeyen: parçada hiç geçmeyen konu.','Parçada antrenörden yalnızca “antrenman” bağlamında söz edilir; oyun planı yoktur.','Dört şık parçada var; hangisi yok?',KD)
# ---------------- 9 erteleme ----------------
P9=('Ertelemeyi çoğu zaman tembelliğin bir belirtisi sayarız; oysa işi sürekli geciktiren kişiler ekseriyetle tembel değil, kaygılıdır. Başarısız olma ihtimali, işe başlamayı bile ağırlaştırır; çünkü başlamadığımız sürece sonucun kötü olup olmayacağını sınamak zorunda kalmayız. Böylece erteleme, kısa vadede kaygıyı azaltan bir sığınağa dönüşür. Bu sığınak, her seferinde biraz daha cazip görünür; çünkü kaygının hemen dindiğini hisseden zihin, bu yolu bir sonraki görevde de seçmeye yatkınlaşır. Üstelik ertelenen iş, zihinde sürekli arka planda çalışan bir yük olarak kalır. Ne var ki bu rahatlama kalıcı değildir: yaklaşan son tarih kaygıyı yeniden büyütür ve kişi aynı döngüye girer. Bu döngüyü kırmanın yolu, daha çok irade göstermek değil, işi tamamlanması korkutmayacak kadar küçük parçalara bölüp ilk parçaya hemen başlamaktır. İlk adım atıldığında, sonucun belirsizliği yerini yapılabilir bir eyleme bırakır ve kaygı çoğu zaman beklenenden çabuk dağılır.')
PQ('0017','ana','zor',P9,('Erteleme, kaygıdan doğan bir kaçınmadır; küçük adımlarla aşılabilir.','ilk ve son bölümler'),
 [('Erteleyen kişiler, tembel oldukları için işe başlamaktan kaçınır.','ters','Parça, geciktirenlerin tembel değil kaygılı olduğunu söyler; şık parçayla çelişir.'),
  ('Başarısızlıktan korkan kişiler, hiçbir işe başlayamaz hâle gelir.','fazla geniş','Parça başlamanın ağırlaştığını söyler; “hiçbir işe başlayamaz” demez.'),
  ('Son tarihin yaklaşması, kaygıyı gidermede en etkili yoldur.','ters','Parçada yaklaşan son tarih kaygıyı yeniden büyütür.'),
  ('İrade gücü yüksek kişiler ertelemeyi kolayca bırakabilir.','ters','Parça yolun “daha çok irade” olmadığını söyler.')],
 'Erteleme kaygıdan doğar; kısa vadede rahatlatır ama döngü yaratır; küçük adımlarla kırılır.','Parçada hem nedenin (kaygı) hem çözümün (küçük adım) anlatıldığına dikkat et.','İki şıktan biri yalnız nedeni, öbürü hem nedeni hem çözümü söylüyor olabilir mi?')
PQ('0018','cik','orta',P9,('İşe başlamak, ertelemeyi besleyen kaygıyı zayıflatabilir.','son cümle'),
 [('Kaygısız insanlar hiçbir işi ertelemez.','fazla geniş','Parça ertelemenin kaygıyla ilişkisini söyler ama kaygısızların hiç ertelemeyeceğini söylemez.'),
  ('Son tarih yaklaşınca ertelemeyi bırakmak kolaylaşır.','ters','Parça yaklaşan son tarihin kaygıyı büyüttüğünü söyler.'),
  ('Küçük parçalara bölünen işler, daha kısa sürede tamamlanır.','parçada yok','Parça süre kısalığından söz etmez.'),
  ('Erteleme alışkanlığı yalnızca öğrencilerde görülür.','parçada yok','Parça öğrencilerden söz etmez; genelleme parçada yoktur.')],
 'İlk adım atılınca kaygı çoğu zaman dağılır.','“İlk adım atıldığında … kaygı çoğu zaman beklenenden çabuk dağılır” cümlesi bunu söyler.','Parçada işe başlamanın kaygıyla ilişkisini anlatan cümleleri bul.')
# ---------------- 10 ışık kirliliği ----------------
P10=('Büyük şehirlerde gece gökyüzüne baktığımızda yalnızca birkaç yıldız seçebiliriz. Bunun nedeni yıldızların azalması değil, şehir ışıklarının gökyüzünü aydınlatarak soluk yıldızları görünmez kılmasıdır. Işık kirliliği denen bu durum, yalnızca amatör gökbilimcileri değil, göçmen kuşları ve gece avlanan canlıları da etkiler; yönünü yıldızlara bakarak bulan kuşlar şehir ışıklarına kapılıp bina duvarlarına çarpabilir. Yaprakları ışıkta uzun süre kalan ağaçların mevsim döngüsünü şaşırması da aynı sorunun bir sonucudur. Böylece sorun yalnızca gökyüzünü değil, doğanın saatini de bozar. Çözüm, ışığı tümüyle söndürmek değildir; aydınlatmaları aşağı yönlü tasarlayıp gereksiz parlaklığı azaltmak, hem enerji tasarrufu sağlar hem de gökyüzünü yeniden görünür kılar. Karanlığı korumak, ışığa karşı çıkmak değil, ışığı yerinde kullanmaktır. Böylece şehirde yaşayan bir çocuk da bir gün başını kaldırıp gökyüzünün tam hâlini görme şansı bulur.')
PQ('0019','deg','orta',P10,('Işık kirliliğinin insanın uyku düzeni üzerindeki etkisine','parçada hiç geçmez'),
 [('Soluk yıldızların şehir ışıklarıyla görünmez kılındığına','var','ikinci cümle bunu söyler.'),
  ('Göçmen kuşların bu durumdan etkilendiğine','var','“göçmen kuşları … da etkiler” ifadesi bunu söyler.'),
  ('Aydınlatmaların aşağı yönlü tasarlanabileceğine','var','“aydınlatmaları aşağı yönlü tasarlayıp” ifadesi bunu söyler.'),
  ('Gereksiz parlaklığın azaltılmasının enerji tasarrufu sağladığına','var','“hem enerji tasarrufu sağlar” ifadesi bunu söyler.')],
 'Değinilmeyen: parçada hiç geçmeyen konu.','Parçada insanın uykusundan söz edilmez.','Her şıkkı bir cümleyle eşle; eşleşmeyen cevaptır.',KD)
PQ('0020','alt','orta',P10,('Aydınlatmayı gerektiği kadar ve gerektiği yönde kullanmak','bağlam: “aşağı yönlü tasarlayıp gereksiz parlaklığı azaltmak”'),
 [('Işığı bulunduğu yerden başka yere taşımamak','sözlük anlamı','“Yerinde” sözüne gerçek anlamıyla bağlanılmış; cümle ışığın bilinçli kullanımından söz eder.'),
  ('Gece aydınlatmasını yalnızca ana caddelerde sürdürmek','parçada yok','Parça ana caddelerden ya da bölgesel ayrımdan söz etmez.'),
  ('Gece boyunca bütün lambaları söndürmek','ters','Parça çözümün “ışığı tümüyle söndürmek değil” olduğunu söyler.'),
  ('Aydınlatma giderlerini yerel yönetimlerin bütçesinden karşılamak','parçada yok','Parçada bütçe ya da yönetim konusu yoktur.')],
 'Işığı yerinde kullanmak, ışığı gereksiz yere dağıtmadan gerektiği kadar kullanmaktır.','Aynı cümlenin başındaki “ışığa karşı çıkmak değil” ve önceki cümle anlamı belirler.','Sözün anlamını önceki cümledeki çözüm önerisinden çıkar.',KA('ışığı yerinde kullanmaktır'))

def kur_hepsi():
    L='ABCDE'
    for i,s in enumerate(SPEC):
        harf=LETTERS[i]; tip=s['tip']; tur,kokd,istenen,puf,bilgi=CFG[tip]
        kok=s['kok'] or kokd; assert kok
        dogru=s['dogru']; yan=list(s['yan']); assert len(yan)==4
        opts=[(m,'yan',f'{e.capitalize()}: {n}' if len(n)<30 else n,tur) for m,e,n in yan]
        opts.insert(L.index(harf),(dogru[0],'dogru','',''))
        etk={}
        for k,o in enumerate(opts):
            etk[L[k]]='doğru' if o[1]=='dogru' else (yan[[y[0] for y in yan].index(o[0])][1])
        islem=' · '.join(f'{x}: {etk[x]}' for x in L)
        if tip in ('ula','deg'):
            adim=[A('Kökü doğru oku','Parçada karşılığı olmayan şıkkı arıyoruz; dört şık parçada bulunur.','aranan: olmayan'),
                  A('Şıkları parçada ara','Her şık için parçadan bir ifade göster.',' · '.join(f'{x}: '+('yok' if etk[x]=='doğru' else 'var') for x in L)),
                  A('Sonucu belirle',f'{harf} şıkkı '+(dogru[1] if dogru[1].startswith('parça') else 'parçada '+dogru[1])+'.',f'{harf}: cevap')]
        elif tip=='alt':
            adim=[A('Sözü bağlamda oku','Sözün geçtiği cümleyi ve çevresindeki cümleleri birlikte oku.','söz → bağlam'),
                  A('Anlamı çıkar',s['ozet'],'anlam: bağlamdan'),
                  A('Şıkları sına',f'Doğru şık bağlamla uyumludur ({dogru[1]}); öbürleri sözlük anlamına bağlı kalır ya da parçada yoktur.',islem)]
        elif tip=='yol':
            adim=[A('Yolları tanı','Karşılaştırma, tanık gösterme, sayısal veri, benzetme gibi yolların ayırt edici işaretlerini hatırla.','işaret → yol'),
                  A('Parçada ara',s['ozet'],' · '.join(f'{x}: '+('var' if etk[x]=='doğru' else 'yok') for x in L)),
                  A('Sonucu belirle',f'Dayanak cümle: {dogru[1]}.',f'{harf}: cevap')]
        else:
            adim=[A('Parçayı özetle',s['ozet'],'konu → sonuç'),
                  A('Dayanağı bul',f'Doğru şıkkın dayanağı: {dogru[1]}.','dayanak cümle'),
                  A('Şıkları ele','Ayrıntı, ters ya da fazla geniş şıklar elenir.',islem)]
        metin=s['parca']+'\n'+kok
        Q.kartlar[TIPKART[tip]]  # varlık
        soru(Q,s['no'],TIPKART[tip],s['zor'],KAZ[tip],3,metin,opts,harf,lambda t:t=='dogru',istenen,s['ip'],bilgi,adim,puf)
kur_hepsi()
# her kayıt ana soru tipine göre: kalıp düz, metin parça+kök (soru() bunu yapar)
# aynı parçayı paylaşan iki soru: 'parca' alanı (denetle.py bu çiftleri havuz içi benzerlikten muaf tutar)
_bit=bitir
def bitir(Q):
    _bit(Q)
    import json
    f='havuz/tyt-tr/pikili-1.json'; D=json.load(open(f))
    for q in D: n=int(q['id'][-4:]); q['parca']=f'pikili-P{(n+1)//2:02d}'
    json.dump(D,open(f,'w'),ensure_ascii=False,indent=1)
bitir(Q)
