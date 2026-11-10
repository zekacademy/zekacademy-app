"""TYT Türkçe · Paragrafta Anlatım Teknikleri: 28 ana soru (hafif mod). Metinler özgündür; kişiler kurgudur."""
import sys,os,random
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from hafif_dilbilgisi import *
KY='ÖSYM 2018–2026 (anlatım biçimleri, düşünceyi geliştirme yolları) · Paraf İQ · Sıfır Risk'
def kart(alt,fikir,tuzak,z,tip): return dict(alt=alt,fikir=fikir,tuzak=tuzak,zorluk=z,kalip='düz',adim=3,tipId=tip,kaynak=KY)
KARTLAR={
 'K-PT-01':kart('Anlatım Biçimleri','Parçada açıklama, tartışma, öyküleme ve betimlemeden hangisinin kullanıldığını ya da kullanılmadığını belirlemek.','Aynı parçada birden çok biçimin iç içe geçtiğini görmeyip tek biçime bakmak; “yoktur” kökünü “vardır” diye okumak.','orta','pt-bicim'),
 'K-PT-02':kart('Düşünceyi Geliştirme Yolları','Tanımlama, örnekleme, karşılaştırma, tanık gösterme, benzetme ve sayısal veri kullanımını parçadaki cümlelerle eşleştirmek.','Örnekle tanığı, karşılaştırmayla benzetmeyi karıştırmak; parçada geçmeyen yolu var saymak.','orta','pt-yol'),
 'K-PT-03':kart('Öncüllü Düşünceyi Geliştirme','Üç öncülün her birini parçada sınayıp doğru kombinasyonu bulmak.','Bir öncülü sınamadan şık seçmek; benzer iki yolu aynı sanmak.','orta','pt-oncul'),
 'K-PT-04':kart('Kişileştirme ve Betimleme Ayrımı','Cümlelerdeki kişileştirme, betimleme, benzetme ve öyküleme ögelerini ayırmak.','Her güzel anlatımı kişileştirme saymak; benzetmeyi kişileştirmeyle karıştırmak.','orta','pt-kisi'),
 'K-PT-05':kart('Tanık Gösterme ve Sayısal Veri','Cümlede kime ya da neye başvurulduğuna bakıp tanık gösterme, sayısal veri ve öteki yolları ayırmak.','Cümlede bir kişi adı geçince tanık gösterme sanmak; sayı geçince sayısal veri saymak.','zor','pt-tanik'),
}
TIPLER={'pt-bicim':'Anlatım biçimlerini tanıma','pt-yol':'Düşünceyi geliştirme yollarını tanıma','pt-oncul':'Öncüllü düşünceyi geliştirme yolları','pt-kisi':'Kişileştirme ve betimleme ayrımı','pt-tanik':'Tanık gösterme ve sayısal veri ayrımı'}
Q=kur('pteknik','Paragrafta Anlatım Teknikleri','tr|Paragraf',KARTLAR,TIPLER); Q.n=28
B_TAN=B('Tanımlama','bir kavramın ne olduğunu “X, … olan şeydir” diyerek belirtmek · “Empati, kendini başkasının yerine koyabilmektir.”')
B_ORN=B('Örnekleme','düşünceyi somut bir olayla destekleme; “örneğin, mesela” ile gelir · “Örneğin erken yatan öğrenci derste daha dinçtir.”')
B_KAR=B('Karşılaştırma','iki varlığı ya da durumu benzerlik ve ayrılıklarıyla yan yana koymak · “Kentte zaman hızlı, köyde yavaş akar.”')
B_TAK=B('Tanık gösterme','görüşü desteklemek için bir uzmanın ya da atasözünün sözüne başvurmak · “Dr. Ece Sarıtaş’a göre okumak düşünmeyi besler.”')
B_BEN=B('Benzetme','zayıf olanı güçlü olana “gibi, sanki, kadar” ile benzetmek · “Kitap bir bahçe gibidir.”')
B_SAY=B('Sayısal verilerden yararlanma','düşünceyi sayı, yüzde, oran gibi verilerle desteklemek · “Öğrencilerin yüzde 70’i erken kalkıyor.”')
B_BIC=B('Anlatım biçimleri','açıklama: bilgi verme · tartışma: görüş savunma · öyküleme: olayı zamana bağlı anlatma · betimleme: görünüşü sözcüklerle resmetme')
B_KIS=B('Kişileştirme ve betimleme','kişileştirme: insan dışı varlığa insan özelliği vermek (“Rüzgâr fısıldadı”) · betimleme: görünüşü ayrıntılı anlatmak (“Saçları kırlaşmış, yüzü kırışmıştı”)')
SPEC=[]
def TEK(no,kart,zor,mod,parca,kok,opts,bilgi,puf,ip):
    SPEC.append(dict(t='tek',no=no,kart=kart,zor=zor,mod=mod,parca=parca,kok=kok,opts=opts,bilgi=bilgi,puf=puf,ip=ip))
def ONC(no,kart,zor,parca,onc,setler,bilgi,puf,ip):
    SPEC.append(dict(t='onc',no=no,kart=kart,zor=zor,parca=parca,onc=onc,setler=setler,bilgi=bilgi,puf=puf,ip=ip))
KY_='Bu parçanın anlatımında aşağıdakilerden hangisi yoktur?'
KV_='Bu parçanın anlatımında aşağıdakilerden hangisine başvurulmuştur?'
KDY='Bu parçada düşünceyi geliştirme yollarından hangisi kullanılmamıştır?'
KDV='Bu parçada düşünceyi geliştirme yollarından hangisine başvurulmuştur?'
# ---------------- ANLATIM BİÇİMLERİ ----------------
TEK('0001','K-PT-01','kolay','v',
 'Sabah erkenden kalkıp iskeleye indi. Balıkçı teknesinin halatını çözdü, motoru çalıştırdı ve kıyıdan yavaşça uzaklaştı. Birkaç saat sonra ağları denize bıraktı. Öğleye doğru ağları çekmeye başladı, çıkan balıkları tek tek kasalara dizdi. Akşam olmadan limana döndü; teknesini bağladı, kasaları iskeleye taşıdı. Sonra elini yüzünü yıkayıp eve doğru yürüdü.',KV_,
 [('Öyküleme','v','“iskeleye indi, halatı çözdü, motoru çalıştırdı” gibi fiiller olayı zaman sırasıyla anlatır'),
  ('Tartışma','y','bir görüş savunulmaz, karşıt düşünce çürütülmez'),
  ('Betimleme','y','kişi ya da yer ayrıntılı biçimde resmedilmez, fiiller olayı ilerletir'),
  ('Tanık gösterme','y','bir uzmanın ya da başkasının sözüne yer verilmez'),
  ('Sayısal verilerden yararlanma','y','sayı, yüzde ya da oran gibi bir veri kullanılmaz')],
 [B_BIC],'Fiiller zaman sırasıyla dizilip olay ilerliyorsa anlatım öyküleyicidir.','Cümlelerin çoğu bir eylemi anlatıyor; bu eylemler hangi sırayla geliyor?')
TEK('0002','K-PT-01','kolay','y',
 'Güneş sistemi, merkezindeki yıldız ile onun çekim alanında dolanan gezegenlerden oluşur. Gezegenler, Güneş’e yakınlıklarına göre sıralanır; en yakın olan Merkür, en uzak olan ise Neptün’dür. Bu gökcisimleri kendi eksenleri etrafında dönerken Güneş’in çevresinde de dolanırlar. Dünya, bu dolanımı yaklaşık 365 gün 6 saatte tamamlar. Örneğin Jüpiter, tek başına öbür gezegenlerin toplam kütlesinden daha ağırdır.',KY_,
 [('Tanımlama','v','“Güneş sistemi, … gezegenlerden oluşur” cümlesi sistemin ne olduğunu belirtir'),
  ('Örnekleme','v','“Örneğin Jüpiter …” cümlesi bir örnek verir'),
  ('Sayısal verilerden yararlanma','v','“365 gün 6 saat” sayısal bir veridir'),
  ('Açıklama','v','gezegenlerin sıralanışını anlatan cümleler okura bilgi verir'),
  ('Öyküleme','y','olaylar zaman akışı içinde anlatılmaz, yalnız bilgi verilir')],
 [B_BIC,B_TAN],'“Yoktur” sorularında önce parçada olan dört yolu bul, geriye kalan cevaptır.','Dört şık parçada bulunuyor. Hangisi için bir cümle gösteremezsin?')
TEK('0003','K-PT-01','kolay','v',
 'Eski evin bahçesinde kocaman bir dut ağacı vardı. Kalın gövdesi yer yer çatlamış, kabuğu gri ve pürüzlüydü. Dalları geniş bir şemsiye gibi avluyu gölgelerken yapraklar rüzgârda hafifçe titriyordu. Yerde dökülmüş morumsu meyveler bir halı gibi serilmiş, taş duvarın dibinde yosunlar yeşil bir şerit oluşturmuştu. Ağacın altındaki tahta bank, yılların yağmurundan soluk bir renk almıştı; üzerindeki boya kabarcıklar hâlinde dökülüyordu.',KV_,
 [('Betimleme','v','“Kalın gövdesi yer yer çatlamış, kabuğu gri ve pürüzlüydü” gibi cümleler ağacın görünüşünü ayrıntılı resmeder'),
  ('Öyküleme','y','birbirini izleyen olaylar yoktur, yalnız bir görünüm anlatılır'),
  ('Tartışma','y','bir görüş savunulmaz'),
  ('Tanık gösterme','y','başkasının sözüne başvurulmaz'),
  ('Sayısal verilerden yararlanma','y','sayısal bir veri verilmez')],
 [B_BIC],'Renk, biçim ve görünüş ayrıntıları sıralanıyorsa anlatım betimleyicidir.','Parçada olaylar mı ilerliyor, yoksa bir şeyin görünüşü mü anlatılıyor?')
TEK('0004','K-PT-01','kolay','y',
 'Bence bilgisayar oyunlarını tümüyle zararlı saymak haksızlıktır. Örneğin strateji oyunları, oyuncuyu plan yapmaya ve sonuçları önceden düşünmeye zorlar. Eğitimci Dr. Ayten Korkmaz’ın dediği gibi “Oyun bir araçtır; iyi ya da kötü oluşu kullananın elindedir.” Ancak günde üç saati aşan ekran süresi göz ve sırt sağlığını bozar. Bu nedenle oyun süresine sınır konmalıdır. Kısacası asıl sorun oyunun kendisi değil, onu nasıl kullandığımızdır.',KY_,
 [('Tartışma','v','“Bence … haksızlıktır” ile bir görüş savunulur'),
  ('Örnekleme','v','“Örneğin strateji oyunları …” bir örnektir'),
  ('Tanık gösterme','v','“Eğitimci Dr. Ayten Korkmaz’ın dediği gibi …” bir uzmanın sözüne başvurur'),
  ('Sayısal verilerden yararlanma','v','“günde üç saati aşan ekran süresi” sayısal bir veridir'),
  ('Öyküleme','y','olaylar zamana bağlı sıralanmaz')],
 [B_BIC,B_TAK],'Cümlede “bence, kanımca” varsa ve gerekçe sıralanıyorsa anlatım tartışmacıdır.','Dört şıkkın her biri için parçada bir ifade göster; gösteremediğin cevaptır.')
TEK('0005','K-PT-01','orta','v',
 'Metafor, bir kavramı başka bir kavramın yerine koyarak anlatma sanatıdır. Dilin en eski anlatım araçlarından biri olan bu yol, soyut düşünceleri somut imgelerle kavramamızı sağlar. Günlük konuşmamıza o kadar işlemiştir ki çoğu zaman metafor kullandığımızın farkına bile varmayız. Bu bakımdan şiirden bilime kadar her alanda karşımıza çıkar.',KDV,
 [('Tanımlama','v','“Metafor, … anlatma sanatıdır” cümlesi metaforun ne olduğunu belirtir'),
  ('Tanık gösterme','y','hiçbir uzmanın sözüne başvurulmaz'),
  ('Sayısal verilerden yararlanma','y','sayı ya da oran verilmez'),
  ('Karşılaştırma','y','iki durum yan yana konup karşılaştırılmaz'),
  ('Örnekleme','y','“örneğin” ile verilmiş somut bir örnek yoktur')],
 [B_TAN],'“X, … olan şeydir / sanatıdır” kalıbı tanımlama işaretidir.','Parçanın ilk cümlesi bir kavramı mı açıklıyor?')
TEK('0006','K-PT-02','orta','y',
 'Bisiklet, insan gücüyle pedal çevrilerek ilerleyen iki tekerlekli bir taşıttır. Kısa mesafelerde otomobilden hem daha hızlı hem daha ucuzdur. Otomobil, şehir merkezinde ortalama saatte on beş kilometre hızla ilerlerken bisikletli aynı yolda yaklaşık yirmi kilometre hızla gider. Üstelik otomobilin yakıt, park ve bakım giderleri varken bisikletin masrafı çok azdır. Örneğin evi iş yerine altı kilometre uzak olan biri, bu yolu bisikletle yaklaşık yirmi dakikada alabilir.',KDY,
 [('Tanımlama','v','“Bisiklet, … iki tekerlekli bir taşıttır” cümlesi tanımdır'),
  ('Karşılaştırma','v','bisiklet ile otomobil hız ve masraf bakımından yan yana konur'),
  ('Sayısal verilerden yararlanma','v','“saatte on beş kilometre”, “yirmi kilometre” sayısal verilerdir'),
  ('Örnekleme','v','“Örneğin evi iş yerine altı kilometre uzak olan biri …” bir örnektir'),
  ('Tanık gösterme','y','hiçbir uzman ya da kaynağın sözüne başvurulmaz')],
 [B_TAN,B_KAR,B_SAY],'Parçada sayı varsa sayısal veri, “örneğin” varsa örnekleme, iki varlık yan yana ise karşılaştırma vardır.','Parçadaki dört yol için birer cümle bulabilirsin; beşincisi için bulamazsın.')
TEK('0007','K-PT-01','zor','y',
 'Köyün girişindeki eski değirmen, yıllardır susmuş bir yaşlı gibi duruyordu. Çocukluğumda babamla oraya gitmiştik; babam kapıyı omzuyla itip içeri girmiş, ben de peşinden sürünerek yürümüştüm. Duvarlar nemli ve yosun kokuluydu, tavandan örümcek ağları sarkıyor, köşede yırtık çuvallar yığılı duruyordu. Çatıdaki kiremitlerden biri düşmüş, açılan boşluktan sızan ışık tozlu havada ince bir çizgi çiziyordu. Değirmen, tahılı öğütmeye yarayan su gücüyle çalışan bir düzenektir; ama benim için o, geçmişe açılan bir kapıdır. Dün yeniden gittim, kapıyı aynı omuz hareketiyle itip içeri girdim.',KY_,
 [('Betimleme','v','“Duvarlar nemli ve yosun kokuluydu, tavandan örümcek ağları sarkıyor …” görünümü ayrıntılı anlatır'),
  ('Öyküleme','v','“babam kapıyı itip içeri girmiş … Dün yeniden gittim” olayları zamana bağlı aktarır'),
  ('Benzetme','v','“susmuş bir yaşlı gibi duruyordu” bir benzetmedir'),
  ('Tanımlama','v','“Değirmen, tahılı öğütmeye yarayan … bir düzenektir” cümlesi tanımdır'),
  ('Sayısal verilerden yararlanma','y','sayı, yüzde ya da oran verilmez')],
 [B_BIC,B_BEN],'Öyküleyici bir parçada betimleme, benzetme ve tanım iç içe geçebilir; her şıkka cümleyle bak.','Bu parçada tek bir biçim değil, birkaç teknik iç içe. Hangisinin hiç izi yok?')
TEK('0008','K-PT-02','zor','y',
 'Dilbilimci Prof. Dr. Selin Karaağaç’a göre dil, düşüncenin yalnızca kabı değil, aynı zamanda kalıbıdır. Dil, bir topluluğun kendi aralarında anlaşmak için kullandığı ortak işaretler dizgesidir. Denizcilikle uğraşan topluluklar rüzgârın yönleri için ayrı ayrı adlar bulurken ormanda yaşayanlar ağaç türlerini tek tek adlandırır. Oysa kentli, bu ayrımları yapmaya hiç ihtiyaç duymaz; çünkü onun gündeminde başka kavramlar vardır. Bu yüzden bir dili anlamak, o dili konuşanların dünyaya hangi pencereden baktığını anlamaktır. Çeviri çalışmalarının güçlüğü de çoğu zaman buradan doğar; çünkü her sözcük, kendi toplumunun deneyimini taşır.',KDY,
 [('Tanık gösterme','v','“Dilbilimci Prof. Dr. Selin Karaağaç’a göre …” bir uzmanın sözüne başvurur'),
  ('Tanımlama','v','“Dil, … ortak işaretler dizgesidir” cümlesi tanımdır'),
  ('Örnekleme','v','denizcilikle uğraşanlar ve ormanda yaşayanlar düşünceyi örnekler'),
  ('Karşılaştırma','v','“Oysa kentli …” cümlesiyle iki yaşam biçimi karşı karşıya konur'),
  ('Sayısal verilerden yararlanma','y','sayı, yüzde ya da oran verilmez')],
 [B_TAK,B_ORN],'Dört yolun da iç içe geçtiği parçada olmayanı bulmak için önce sayı, alıntı, örnek, tanım izini ara.','Parçada bir uzman, bir tanım, örnekler ve bir karşıtlık var. Peki bir rakam var mı?')
# ---------------- DÜŞÜNCEYİ GELİŞTİRME YOLLARI ----------------
TEK('0009','K-PT-02','kolay','v',
 'Kitap, bir bahçe gibidir; özenle bakılırsa her mevsim yeni bir çiçek açar. Okur da bu bahçede dolaşan, her köşede başka bir güzellikle karşılaşan bir gezgin gibidir. Her sayfa bir patikadır; hangisinden yürürsek yürüyelim bizi başka bir yere çıkarır. Kimi sayfada gölge bulur, kimi sayfada ışığa çıkarız. İşte bu yüzden iyi okur, sabırlı bir bahçıvan gibi acele etmez.',KDV,
 [('Benzetme','v','“Kitap, bir bahçe gibidir” ve “gezgin gibidir” benzetme ilgisi kurar'),
  ('Sayısal verilerden yararlanma','y','sayısal bir veri yoktur'),
  ('Tanık gösterme','y','hiçbir uzmanın sözü aktarılmaz'),
  ('Tanımlama','y','bir kavramın ne olduğu “X, … olan şeydir” diye tanımlanmaz'),
  ('Örnekleme','y','“örneğin” ile verilmiş somut bir olay yoktur')],
 [B_BEN],'“Gibi, sanki, kadar” ile kurulan ilişki benzetmedir.','Parçada “gibi” sözcüğü kaç kez geçiyor ve ne için kullanılıyor?')
TEK('0010','K-PT-02','kolay','v',
 'Önyargı, bir kişi ya da grup hakkında yeterli bilgi edinmeden önceden verilen hükümdür. Bu hüküm çoğu kez alışkanlıklara, duyulanlara ve ilk izlenimlere dayanır. Önyargı, kişinin karşısındakini gerçekte olduğu gibi görmesini engeller. Bu yüzden insanlarla ilişkide acele hüküm vermemek gerekir. Tanıdıkça değişen yargılar, çoğu zaman en baştaki yargıların ne kadar temelsiz olduğunu da gösterir.',KDV,
 [('Tanımlama','v','“Önyargı, … önceden verilen hükümdür” cümlesi kavramı tanımlar'),
  ('Sayısal verilerden yararlanma','y','sayı ya da oran verilmez'),
  ('Tanık gösterme','y','hiçbir uzmanın sözüne başvurulmaz'),
  ('Benzetme','y','“gibi, sanki” ile kurulmuş bir benzetme yoktur'),
  ('Karşılaştırma','y','iki varlık ya da durum yan yana konmaz')],
 [B_TAN],'Parçanın başında kavramın ne olduğu söyleniyorsa tanımlama vardır.','İlk cümlede “önyargı”nın ne olduğu açıklanıyor mu?')
TEK('0011','K-PT-02','orta','y',
 'Uyku, bedenin ve zihnin kendini onardığı dinlenme hâlidir. Uyku bilimci Dr. Ferit Aksungur, yetişkinlerin gecede en az yedi saat uyuması gerektiğini söylüyor. Oysa bugün pek çok insan altı saatin altında uyuyor; öğrenciler ise sınav dönemlerinde bu süreyi dört saate kadar indiriyor. Örneğin gece geç saate kadar çalışan bir öğrenci, ertesi gün derste dikkatini toplayamaz. Uykusuzluk yalnızca yorgunluk değil, hafıza ve dikkat kaybı da demektir.',KDY,
 [('Tanımlama','v','“Uyku, … dinlenme hâlidir” cümlesi tanımdır'),
  ('Tanık gösterme','v','“Uyku bilimci Dr. Ferit Aksungur … söylüyor” bir uzmanın görüşüne başvurur'),
  ('Sayısal verilerden yararlanma','v','“yedi saat”, “altı saat”, “dört saat” sayısal verilerdir'),
  ('Örnekleme','v','“Örneğin gece geç saate kadar çalışan bir öğrenci …” bir örnektir'),
  ('Benzetme','y','“gibi, sanki” ile kurulmuş bir benzetme yoktur')],
 [B_TAK,B_SAY],'Dört yolu birer cümleyle eşleştir; eşleşmeyen cevaptır.','Uzman, rakam, örnek, tanım: bunların hepsi parçada var. Hangisi yok?')
TEK('0012','K-PT-02','orta','v',
 'Kırsalda yaşam daha yavaş akar; sabah horozla başlayan gün, akşam güneşle biter. Kentte ise zaman, trafiğin ve toplantıların ritmine göre tüketilir. Kırın sessizliği insana kendi sesini duyma fırsatı verirken kentin gürültüsü düşünmeye zaman bırakmaz. Her ikisinin de güzel yanları vardır; ama biri dinlendirir, öbürü yorar. Hangisini seçeceğimiz, hayattan ne beklediğimize bağlıdır.',KDV,
 [('Karşılaştırma','v','“Kırsalda … Kentte ise …” ile kır ve kent yaşamı yan yana konur'),
  ('Sayısal verilerden yararlanma','y','sayı ya da oran verilmez'),
  ('Tanık gösterme','y','hiçbir kişinin sözüne başvurulmaz'),
  ('Tanımlama','y','bir kavram “X, … olan şeydir” diye tanımlanmaz'),
  ('Örnekleme','y','“örneğin” ile verilmiş somut bir olay yoktur')],
 [B_KAR],'“Ise, oysa, ama, buna karşılık” ile iki durumu karşı karşıya koyan parçada karşılaştırma vardır.','Parçada iki ayrı yaşam biçimi birlikte ele alınıyor mu?')
TEK('0013','K-PT-02','orta','y',
 'Bellek, yaşanmışlıkları depolayan ve gerektiğinde geri çağıran zihinsel yetidir. Bilgisayarın belleği gibi her şeyi olduğu gibi saklamaz; insan belleği, anıları her hatırlayışta yeniden kurar. Örneğin çocukluğumuzdaki bir doğum günü, her anlatışımızda biraz değişir. Bu yüzden iki kişi aynı olayı farklı hatırlayabilir. Bu bakımdan bellek, sabit bir kayıt defterinden çok sürekli yeniden yazılan bir taslağa benzer.',KDY,
 [('Tanımlama','v','“Bellek, … zihinsel yetidir” cümlesi tanımdır'),
  ('Karşılaştırma','v','insan belleği ile bilgisayar belleği yan yana konur'),
  ('Örnekleme','v','“Örneğin çocukluğumuzdaki bir doğum günü …” bir örnektir'),
  ('Benzetme','v','“yeniden yazılan bir taslağa benzer” bir benzetmedir'),
  ('Tanık gösterme','y','hiçbir uzmanın sözüne başvurulmaz')],
 [B_TAN,B_KAR,B_BEN],'Dört yolun hepsi için cümle bulunup biri bulunamıyorsa cevap odur.','Hangi tekniğin parçada hiçbir ipucu yok?')
TEK('0014','K-PT-02','orta','y',
 'LED, elektrik akımı geçtiğinde ışık veren yarı iletken bir devre elemanıdır. Enerji mühendisi Doç. Dr. Hakan Yüceyurt’un deyişiyle “En ucuz enerji, harcanmayan enerjidir.” Eski tip akkor ampuller harcadıkları enerjinin büyük bölümünü ışığa değil ısıya dönüştürür; LED’ler ise aynı aydınlığı çok daha az enerjiyle verir. Bir evde aydınlatma LED’e çevrildiğinde elektrik tüketimi yaklaşık yüzde yetmiş beş azalabilir.',KDY,
 [('Tanımlama','v','“LED, … bir devre elemanıdır” cümlesi tanımdır'),
  ('Tanık gösterme','v','“Doç. Dr. Hakan Yüceyurt’un deyişiyle …” bir uzmanın sözüne başvurur'),
  ('Karşılaştırma','v','akkor ampul ile LED yan yana konur'),
  ('Sayısal verilerden yararlanma','v','“yaklaşık yüzde yetmiş beş” sayısal bir veridir'),
  ('Benzetme','y','“gibi, sanki” ile kurulmuş bir benzetme yoktur')],
 [B_TAK,B_SAY],'Alıntı tırnak içinde ve bir kişiye bağlıysa tanık gösterme, rakam varsa sayısal veridir.','Parçada bir tanım, bir uzman sözü, bir karşılaştırma ve bir yüzde var.')
TEK('0015','K-PT-02','zor','v',
 'Eleştirmen Prof. Dr. Nermin Tanrıkulu, iyi bir romanın okuru “değiştirmeden bırakmayan” roman olduğunu söyler. Bu ölçüt, yazarın okurdan ne beklediğini de açıklar: okur metnin içinde dolaşırken kendi yargılarını yeniden düşünmelidir. Başka bir ifadeyle roman, okura hazır cevaplar sunmak yerine sorular bırakır. Bu ölçüt aynı zamanda eleştirmenin görevini de belirler: iyi bir eleştirmen, kitabın okurda bıraktığı izi sorgular. Sorguladığı şey beğeni değil, değişimdir. Böyle bakıldığında bir kitabın satış listesinde ne kadar kalacağı, değerini belirleyen bir ölçüt olmaktan çıkar.',KDV,
 [('Tanık gösterme','v','“Eleştirmen Prof. Dr. Nermin Tanrıkulu … söyler” bir uzmanın sözüne başvurur'),
  ('Sayısal verilerden yararlanma','y','sayı, yüzde ya da oran verilmez'),
  ('Örnekleme','y','“örneğin” ile verilmiş somut bir olay ya da kitap adı yoktur'),
  ('Benzetme','y','“gibi, sanki” ile kurulmuş bir benzetme yoktur'),
  ('Öyküleme','y','olaylar zamana bağlı anlatılmaz')],
 [B_TAK],'Bir uzmanın adı ve görüşü verilip düşünce onunla destekleniyorsa tanık gösterme vardır.','Parçada bir isim geçiyor; bu isim görüşü desteklemek için mi kullanılmış?')
TEK('0016','K-PT-02','zor','y',
 'Şehir, ağaçsız kaldıkça nefessiz kalan bir canlı gibidir. Bir ağaç yazın çevresindeki havayı birkaç derece serinletir. Asfalt yüzey ise gölgedeki toprağa göre yirmi dereceye yakın daha sıcak olabilir; bu yüzden betonla çevrili semtler, parkı olan semtlerden belirgin biçimde daha sıcaktır. Örneğin yeşil alanı bol bir mahallede termometre öğle saatinde bile ötekilerden daha düşük değer gösterir. Bu yüzden kent planlamacıları, yeni mahalleler kurulurken yeşil alanı sonradan eklenen bir süs değil, baştan düşünülmesi gereken bir altyapı olarak ele almalıdır.',KDY,
 [('Benzetme','v','“nefessiz kalan bir canlı gibidir” bir benzetmedir'),
  ('Sayısal verilerden yararlanma','v','“birkaç derece”, “yirmi dereceye yakın” sayısal verilerdir'),
  ('Karşılaştırma','v','betonla çevrili semtler ile parkı olan semtler yan yana konur'),
  ('Örnekleme','v','“Örneğin yeşil alanı bol bir mahallede …” bir örnektir'),
  ('Tanık gösterme','y','hiçbir uzman ya da kaynağın sözüne başvurulmaz')],
 [B_BEN,B_SAY,B_KAR],'Uzun parçada her yol için bir cümle ara; bulamadığın cevaptır.','Benzetme, rakam, karşıtlık ve örnek var. Başka birinin sözü var mı?')
# ---------------- ÖNCÜLLÜ ----------------
S1=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
ONC('0017','K-PT-03','orta',
 'Empati, kendini karşısındakinin yerine koyarak onun duygularını anlayabilmektir. Örneğin arkadaşı sınavdan düşük not aldığında “Üzülmemelisin” demek yerine “Şu an çok bozulduğunu anlıyorum” diyen biri empati kurmuş olur. Empati, ilişkilerin sağlıklı yürümesinin temel koşuludur; çünkü insan, anlaşıldığını hissettiği yerde kendini güvende sayar.',
 [('tanımlama',True,'“Empati, … anlayabilmektir” cümlesi kavramı tanımlar'),('sayısal verilerden yararlanma',False,'parçada sayı, yüzde ya da oran yoktur'),('örnekleme',True,'“Örneğin arkadaşı sınavdan düşük not aldığında …” bir örnektir')],
 ['Yalnız I','Yalnız III','I ve II','I ve III','II ve III'],[B_TAN,B_ORN],'Üç öncülü ayrı ayrı sına; yalnız cümleyle gösterebildiklerini işaretle.','Önce üç yolun her biri için parçada bir cümle ara.')
ONC('0018','K-PT-03','orta',
 'Elektrikli otobüsler, dizel otobüslere göre daha sessiz çalışır; üstelik kilometre başına enerji maliyeti yaklaşık üçte bir oranında daha düşüktür. Dizel araçta motor sürekli titreşirken elektrikli araçta bu titreşim neredeyse hissedilmez. Ancak elektrikli otobüsün ilk satın alma bedeli, dizel otobüsünkinden fazladır; bu fark, birkaç yıl içinde yakıt tasarrufuyla kapanır.',
 [('tanımlama',False,'hiçbir kavram “X, … olan şeydir” biçiminde tanımlanmaz'),('karşılaştırma',True,'elektrikli ve dizel otobüsler sessizlik, titreşim ve maliyet bakımından yan yana konur'),('sayısal verilerden yararlanma',True,'“üçte bir oranında” sayısal bir veridir')],
 ['Yalnız II','I ve II','I ve III','II ve III','I, II ve III'],[B_KAR,B_SAY],'Şıktaki her öncül parçada karşılık buluyorsa o şıkta yer alır.','İki aracın yan yana ele alınması hangi yola işaret eder?')
ONC('0019','K-PT-03','orta',
 'Fikirler tohum gibidir; uygun toprak bulunca filizlenir, bulamayınca kuru bir kabuk olarak kalır. İyi bir öğretmen bu toprağı hazırlayan bahçıvandır. Öğrenci ise sabırla sulanmayı bekleyen taze bir fidandır. Bahçıvan acele ederse fidan boynunu büker; fazla özen gösterirse kök salamaz. Eğitimde de ölçü, ne bırakmak ne de boğmaktır.',
 [('benzetme',True,'“Fikirler tohum gibidir” bir benzetmedir'),('tanık gösterme',False,'hiçbir uzmanın sözüne başvurulmaz'),('sayısal verilerden yararlanma',False,'parçada sayısal veri yoktur')],
 ['Yalnız I','Yalnız II','I ve II','I ve III','II ve III'],[B_BEN],'Öncüllü sorularda her öncülü ayrı ayrı sınamadan şıka bakma.','“Gibi” ile kurulan ilişkiyi hangi yol karşılar?')
ONC('0020','K-PT-03','orta',
 'Müzik eğitiminin çocukların dil gelişimine katkı sağladığı sık dile getirilen bir görüştür. Çocuk gelişimi uzmanı Dr. Aslı Pekgüzel, ritim çalışan çocukların heceleri ayırmada daha başarılı olduğunu belirtiyor. Örneğin ilkokulda her hafta şarkı söyleyen öğrencilerin yeni sözcükleri daha çabuk öğrendiği gözlenmiştir. Bu nedenle okullarda müziğe ayrılan saatin kısılması, yalnızca bir sanat dersinden vazgeçmek anlamına gelmez.',
 [('tanık gösterme',True,'“Çocuk gelişimi uzmanı Dr. Aslı Pekgüzel … belirtiyor” bir uzmanın sözüne başvurur'),('sayısal verilerden yararlanma',False,'parçada sayı, yüzde ya da oran yoktur'),('örnekleme',True,'“Örneğin ilkokulda her hafta şarkı söyleyen öğrenciler …” bir örnektir')],
 ['Yalnız I','I ve II','I ve III','II ve III','I, II ve III'],[B_TAK,B_ORN],'Uzman adı + görüş = tanık gösterme; “örneğin” = örnekleme.','Parçadaki uzman kişi ve “örneğin” sözcüğü hangi öncülleri destekliyor?')
ONC('0021','K-PT-03','zor',
 'Nezaket, başkalarının duygularını incitmeden davranma biçimidir. İnsan ilişkilerinde bir yağ gibidir; dişliler onunla sürtünmeden döner. Kabalık ise karşıdakini her söyleyişte biraz daha uzaklaştıran bir çıkıntıdır. Nazik biri aynı eleştiriyi yumuşak bir dille yaptığında karşısındaki onu dinler; kaba biri yaptığında ise karşısındaki savunmaya geçer. Nitekim çoğu anlaşmazlık, söylenenin içeriğinden çok söyleniş biçiminden çıkar. Biçimi düzeltmek, içeriği değiştirmeden sonucu değiştirir. Bu nedenle nezaket, bir süs değil, doğrudan sonuç alma aracıdır.',
 [('tanımlama',True,'“Nezaket, … davranma biçimidir” cümlesi kavramı tanımlar'),('benzetme',True,'“bir yağ gibidir” bir benzetmedir'),('karşılaştırma',True,'nazik kişi ile kaba kişi aynı eleştiri karşısında yan yana konur')],
 ['Yalnız II','I ve II','I ve III','II ve III','I, II ve III'],[B_TAN,B_BEN,B_KAR],'Üç öncülün üçü de parçada varsa “I, II ve III” seçilir; yine de her birini cümleyle doğrula.','Parçanın ilk cümlesi, “gibi” sözcüğü ve “nazik / kaba” karşıtlığı birer yol gösteriyor.')
ONC('0022','K-PT-03','zor',
 'Çocuklara okuma alışkanlığı kazandırmak, sandığımızdan daha çok evdeki havaya bağlıdır. Eğitimci Dr. Tülin Kocabaşoğlu, çocukların yaşadıklarını görerek öğrendiğini, bu yüzden en etkili öğüdün davranışla verilen öğüt olduğunu söylüyor. Örneğin akşam yemeğinden sonra bir saat kitap okuyan bir ailede büyüyen çocuk, bu saati kendiliğinden ayrılmış sayar. Aynı çocuk ileride kendi evinde de benzer bir saati kendisi oluşturacaktır. Bu durum, çocuğa öğüt vermeden önce kendi davranışımızı gözden geçirmemiz gerektiğini düşündürür. Okuma saati evin doğal bir parçası olduğunda kalıcı bir alışkanlığa dönüşür.',
 [('tanık gösterme',True,'“Eğitimci Dr. Tülin Kocabaşoğlu … söylüyor” bir uzmanın görüşüne başvurur'),('örnekleme',True,'“Örneğin akşam yemeğinden sonra bir saat kitap okuyan bir ailede …” bir örnektir'),('karşılaştırma',False,'iki varlık ya da durum yan yana konup karşılaştırılmaz; yalnız tek bir aile örneği anlatılır')],
 ['Yalnız I','I ve II','I ve III','II ve III','I, II ve III'],[B_TAK,B_ORN,B_KAR],'Bir öncül için karşılığı olmayan tek bir cümle bile yoksa o öncülü işaretleme.','Üçüncü öncülde iki durum gerçekten karşı karşıya mı konuyor?')
# ---------------- KİŞİLEŞTİRME / BETİMLEME ----------------
TEK('0023','K-PT-04','kolay','v',None,'Aşağıdaki cümlelerin hangisinde kişileştirme yapılmıştır?',
 [('Yağmur, camlara usulca vurup içeri girmek istiyordu.','v','yağmura “içeri girmek istemek” gibi insana özgü bir davranış verilmiştir'),
  ('Gökyüzü, kurşun gibi gri bir örtüyle kaplanmıştı.','y','insan özelliği verilmemiş, “gibi” ile benzetme yapılmıştır'),
  ('Yağmur sabaha kadar durmadan yağdı.','y','yalnızca bir olay aktarılır, insan özelliği yoktur'),
  ('Pencerenin önündeki kiraz ağacının dalları incecik ve çıplaktı.','y','ağacın görünüşü anlatılır; bu betimlemedir, kişileştirme değil'),
  ('Yağmurun sesi, çatıda davul gibi çalıyordu.','y','ses davula benzetilmiştir; insan özelliği verilmemiştir')],
 [B_KIS],'İnsan dışı varlık düşünüyor, konuşuyor, istiyorsa kişileştirme vardır.','Hangi cümlede yağmur, insan gibi bir şey “yapıyor”?')
TEK('0024','K-PT-04','orta','v',None,'Aşağıdaki cümlelerin hangisinde betimleme vardır?',
 [('Kapıdan giren adamın saçları kırlaşmış, yüzü kırışmış, gözleri çökmüştü.','v','adamın görünüşü ayrıntılarla resmedilmiştir'),
  ('Adam, kapıdan girer girmez doğruca masaya yürüdü.','y','art arda eylemler anlatılır; bu öykülemedir'),
  ('Rüzgâr, ağaçların arasında fısıldaşıp duruyordu.','y','rüzgâra insan özelliği verilmiştir; bu kişileştirmedir'),
  ('Her sabah beşte kalkıp koşuya çıkar.','y','bir alışkanlık bildirilir, görünüş resmedilmez'),
  ('Sağlıklı beslenmek için sebze ve meyve tüketmek gerekir.','y','bilgi ve öğüt verilir; görünüş anlatılmaz')],
 [B_KIS],'Renk, biçim, görünüş ayrıntıları sıralanıyorsa betimleme vardır.','Hangi cümle bir şeyin nasıl göründüğünü anlatıyor?')
TEK('0025','K-PT-04','orta','v',None,'Aşağıdaki cümlelerin hangisinde hem benzetme hem kişileştirme birlikte kullanılmıştır?',
 [('Deniz, geceleri bir dev gibi uyuyup sabaha doğru yavaşça uyanır.','v','“bir dev gibi” benzetme, “uyuyup uyanır” kişileştirmedir'),
  ('Dağlar, güneşe doğru kollarını açıp uzanıyordu.','y','yalnız kişileştirme vardır, “gibi” ile kurulmuş bir benzetme yoktur'),
  ('Ay, gümüş bir tepsi gibi gökyüzünde asılıydı.','y','yalnız benzetme vardır, ay insan gibi davranmaz'),
  ('Gökyüzü masmavi, bulutsuzdu.','y','yalnızca görünüş anlatılır; betimlemedir'),
  ('Kuşlar sabahleyin yuvalarından çıktı.','y','yalnızca bir olay aktarılır')],
 [B_KIS,B_BEN],'İki teknik soruluyorsa her teknik için cümlede ayrı bir işaret ara.','Hangi şıkta hem “gibi” hem insana özgü bir eylem var?')
# ---------------- TANIK GÖSTERME / SAYISAL VERİ ----------------
TEK('0026','K-PT-05','orta','v',None,'Aşağıdakilerden hangisi, düşüncesini bir uzmanın sözüyle destekleyen cümledir?',
 [('Ekonomist Prof. Dr. Cemile Arıtürk’ün dediği gibi “Tasarruf, geleceğe yapılan bir yatırımdır.”','v','bir uzmanın sözüne başvurularak görüş desteklenir'),
  ('Tasarruf, gelirin bir bölümünü ileride kullanmak üzere ayırmaktır.','y','bir kavramın ne olduğu söylenir; bu tanımlamadır'),
  ('Örneğin aylık gelirinin onda birini ayıran biri, bir yılda yaklaşık bir aylık maaşını biriktirir.','y','somut bir olayla düşünce desteklenir; bu örneklemedir'),
  ('Tasarruf eden insan, kışa hazırlanan karıncalar gibidir.','y','“gibi” ile kurulmuş bir benzetmedir'),
  ('Tasarrufa yönelen ailelerin sayısı son beş yılda yüzde kırk artmıştır.','y','yüzde ile verilmiş sayısal veridir')],
 [B_TAK],'Bir kişinin adı + sözü ile görüş destekleniyorsa tanık gösterme vardır.','Hangi cümlede bir uzmanın sözü aktarılıyor?')
TEK('0027','K-PT-05','orta','v',None,'Aşağıdaki cümlelerin hangisinde sayısal verilerden yararlanılmıştır?',
 [('Bu şehirde bisiklet kullanımı, bisiklet yolları yapıldıktan sonra üç yıl içinde dört katına çıkmıştır.','v','“üç yıl”, “dört katı” görüşü destekleyen sayısal verilerdir'),
  ('Bisikletli ulaşım, hem sağlığı hem çevreyi koruyan bir yoldur.','y','sayı içermeyen bir yargıdır'),
  ('Bisiklet, iki tekerlekli ve pedalla yürüyen bir taşıttır.','y','“iki” bir veri değildir; cümle bisikleti tanımlar'),
  ('Çocukluğumda bisikletim vardı; bir yaz günü ilk kez düşmüştüm.','y','yaşanmış bir olay anlatılır; bu öyküleyicidir'),
  ('Bisiklet, otomobile göre daha ucuz ve daha sağlıklıdır.','y','iki aracı yan yana koyar; bu karşılaştırmadır, sayısal veri yoktur')],
 [B_SAY],'Her sayı sayısal veri değildir; sayı bir iddiayı desteklemek için kullanılıyorsa veridir.','“İki tekerlekli” ile “dört katına çıkmak” aynı işi mi görüyor?')
TEK('0028','K-PT-05','zor','y',None,'Aşağıdaki cümlelerin hangisinde, adı geçen kişinin sözünden yararlanılmadığı için tanık gösterme yoktur?',
 [('Dr. Neşe Ongunsoy’un deyişiyle “Sabır, acının tadını tatlıya çeviren zamandır.”','v','bir kişinin sözü, görüşü desteklemek için aktarılmıştır'),
  ('Uzmanlara göre düzenli uyku, öğrenmenin en güçlü destekçisidir.','v','“Uzmanlara göre” ile uzman görüşü aktarılır'),
  ('Bir atasözünün dediği gibi “Damlaya damlaya göl olur.”','v','atasözüne başvurularak düşünce desteklenir'),
  ('Dün öğretmenimiz Selma Hanım bizi müzeye götürdü ve sergiyi gezdirdi.','y','bir kişi adı geçer ama onun sözüne başvurulmaz; olay aktarılır'),
  ('Eğitim bilimci Doç. Dr. Mert Orhonoğlu, merak duygusunun öğrenmenin yakıtı olduğunu söylüyor.','v','bir uzmanın görüşü aktarılır')],
 [B_TAK],'Cümlede kişi adı geçmesi tek başına tanık göstermek değildir; o kişinin sözü görüşü desteklemeli.','Hangi cümlede adı geçen kişinin söylediği bir şey yok, yalnız yaptığı bir şey var?')

EK={
'0001':' Gün boyunca neredeyse hiç konuşmadı; yalnızca motorun sesi ona eşlik etti. Ertesi sabah aynı iskeleye yine erkenden indi.',
'0002':' Merkür ise Güneş çevresindeki bir turu yaklaşık seksen sekiz günde bitirir.',
'0003':' Kapının yanındaki eski kuyunun taş kenarı da sarmaşıkla örtülmüş, kovası paslanmış zincirinde sallanıyordu.',
'0005':' Hatta çoğu zaman en etkili anlatım, kullanıldığı fark edilmeyen anlatımdır; bu yüzden metafor dilin en sessiz ama en güçlü ustalarından sayılır.',
'0007':' Ağır ağır yürüdüğümüz o yoldan her adımda tanıdık bir koku yükselirdi. Annemin bu yerden hiç hoşlanmadığını, her gidişimizde beni geri çağırdığını da hatırlarım.',
'0008':' Bu nedenle dil öğretimi, yalnızca kural aktarmak değil, bir bakış biçimini tanıtmaktır. Bir sözcüğün yerini bulmak, çoğu zaman o toplumun neyi önemsediğini bulmaktır.',
'0009':' Bahçede aceleyle yürüyenin gözünden en güzel çiçekler kaçar.',
'0010':' Çünkü gerçek bir tanışma, hükmün değil dinlemenin ardından başlar.',
'0012':' Bu yüzden aynı kişi bile hayatının farklı dönemlerinde farklı tercih yapabilir.',
'0013':' Bu nedenle aynı anıyı paylaşan arkadaşlar bile ayrıntıda anlaşamaz.',
'0014':' Bu yüzden aydınlatma ihtiyacı karşılanırken verimli çözümler tercih edilmelidir.',
'0015':' Bu bakımdan bir romanın değeri, okurda uyandırdığı soruların kalıcılığıyla ölçülür. Çabuk unutulan bir kitap ne kadar çok okunursa okunsun bu ölçütü karşılamaz.',
'0016':' Gölge, rüzgâr ve nem de bu serinliği artıran etkenlerdir. Bu etkenlerin her biri tek başına küçük görünse de toplamda kentin yaşanabilirliğini belirler. Kent yaşamını planlayanların bu toplamı görmesi gerekir.',
'0017':' Bu nedenle empati, öğrenilebilen ve geliştirilebilen bir beceri olarak da görülür.',
'0018':' Bu nedenle belediyeler filo yenilerken yalnız fiyata değil, işletme maliyetine de bakmalıdır.',
'0019':' Fidanın büyümesi için gereken, hazırlanan toprak ve zamandır.',
'0021':' Çalışma hayatında da durum farklı değildir; aynı hatayı “Bunu yanlış yapmışsın” diye değil “Şuraya bir daha bakalım” diye söyleyen yönetici, ekibinin güvenini kazanır.',
'0022':' Çocuğun okuduğu kitabı bir sohbet konusu yapmak da bu alışkanlığı besler.',
}
for _s in SPEC:
    if _s['no'] in EK: _s['parca']+=EK[_s['no']]
# ---------------- kurma ----------------
def etiketle(s,harf):
    L='ABCDE'
    if s['t']=='tek':
        mod=s['mod']; ok=[o for o in s['opts'] if o[1]==mod]; assert len(ok)==1,(s['no'],'tek doğru değil')
        yan=[o for o in s['opts'] if o[1]!=mod]; assert len(yan)==4
        opts=[]
        for o in yan: opts.append(o)
        opts.insert(L.index(harf),ok[0])
        son=[]
        for o in opts:
            ad,d,ac=o
            if o is ok[0]: son.append((ad,'dogru','',''))
            elif mod=='y': son.append((ad,'yan',f'Bu yol parçada vardır: {ac}. Soru olmayanı sorduğu için bu şık elenir.','dikkat'))
            else: son.append((ad,'yan',f'Parçada bu yola başvurulmamıştır: {ac}.','bilgi'))
        metin=(s['parca']+'\n' if s['parca'] else '')+s['kok']
        d=ok[0]
        if s['parca']:
            adim=[A('Kökü doğru oku','Parçada olmayanı arıyoruz; dört şık parçada karşılık bulur.' if mod=='y' else 'Parçada kullanılan tek yolu arıyoruz; öbür şıklar parçada yoktur.','aranan: '+('olmayan' if mod=='y' else 'olan')),
                  A('Her yolu parçada ara','Her şık için parçada bir cümle bulmaya çalış; cümle gösterebildiklerin “var”dır.',' · '.join(f"{L[i]}: {'var' if (o[1]=='yan')==(mod=='y') else 'yok'}" for i,o in enumerate(son))),
                  A('Sonucu belirle',f'{d[0]}: {d[2]}.' ,f'{L[L.index(harf)]}: cevap')]
        else:
            adim=[A('Kökü doğru oku','Sorulan tekniği tanımla; her cümleyi o tanıma göre sına.','aranan: '+('olmayan' if mod=='y' else 'olan')),
                  A('Cümleleri tek tek çözümle','Her cümlenin hangi anlatım tekniğini kullandığını belirle.',' · '.join(f"{L[i]}: {'doğru' if o[1]=='dogru' else 'elendi'}" for i,o in enumerate(son))),
                  A('Sonucu belirle',f'{L[L.index(harf)]} şıkkı: {d[2]}.',f'{L[L.index(harf)]}: cevap')]
        return metin,son,adim,'Parçada bulunmayan yolu bulmak.' if (mod=='y' and s['parca']) else ('Parçada kullanılan yolu bulmak.' if s['parca'] else 'Sorulan tekniği taşıyan cümleyi bulmak.')
    else:
        onc=s['onc']; ROMN=['I','II','III']
        dogru=[i for i,o in enumerate(onc) if o[1]]
        def lab(ix): return ('Yalnız '+ROMN[ix[0]]) if len(ix)==1 else (' ve '.join(ROMN[i] for i in ix) if len(ix)==2 else 'I, II ve III')
        gerek=lab(dogru); ok=[k for k,x in enumerate(s['setler']) if x==gerek]; assert len(ok)==1,(s['no'],gerek)
        assert 'ABCDE'[ok[0]]==harf
        son=[]
        for k,x in enumerate(s['setler']):
            if x==gerek: son.append((x,'dogru','','')); continue
            ix=[ROMN.index(t) for t in (['I','II','III'] if x=='I, II ve III' else x.replace('Yalnız ','').replace(' ve ',',').split(','))] if x!='I, II ve III' else [0,1,2]
            fark=[i for i in range(3) if (i in ix)!=(i in dogru)]
            i=fark[0]
            if i in ix: c=f'{ROMN[i]}. öncül ({onc[i][0]}) parçada yoktur: {onc[i][2]}; ama şıkta yer alıyor.'
            else: c=f'{ROMN[i]}. öncül ({onc[i][0]}) parçada vardır: {onc[i][2]}; ama şıkta yer almıyor.'
            son.append((x,'yan',c,'bilgi'))
        kok='Bu parçada,\n'+'\n'.join(f'{ROMN[i]}. {o[0]}' for i,o in enumerate(onc))+'\nyollarından hangilerine başvurulmuştur?'
        metin=s['parca']+'\n'+kok
        adim=[A('Öncülleri tanı','Her öncülün hangi yolu anlattığını hatırla; sonra parçada ara.','I, II, III: üç yol'),
              A('Her öncülü sına','Parçada cümleyle gösterebildiğin öncül vardır, gösteremediğin yoktur.',' · '.join(f"{ROMN[i]}: {'var' if o[1] else 'yok'}" for i,o in enumerate(onc))),
              A('Şıkkı seç',f'Doğru kombinasyon {gerek}; öbür şıklar bir öncülü yanlış yerleştirir.',f'{harf}: {gerek}')]
        return metin,son,adim,'Parçada başvurulan yolların hangileri olduğu.'

def kur_hepsi():
    # öncüllü harfleri sabit
    fix={}
    for s in SPEC:
        if s['t']=='onc':
            dogru=[i for i,o in enumerate(s['onc']) if o[1]]
            R=['I','II','III']
            g=('Yalnız '+R[dogru[0]]) if len(dogru)==1 else (' ve '.join(R[i] for i in dogru) if len(dogru)==2 else 'I, II ve III')
            fix[s['no']]='ABCDE'[s['setler'].index(g)]
    n=len(SPEC); hedef={'A':6,'B':6,'C':6,'D':5,'E':5}
    for h in fix.values(): hedef[h]-=1
    havuz=[h for h,c in hedef.items() for _ in range(max(c,0))]
    random.seed(7); random.shuffle(havuz)
    k=n-len(fix); assert len(havuz)>=k,(havuz,k)
    havuz=havuz[:k]
    it=iter(havuz)
    for s in SPEC:
        harf=fix.get(s['no']) or next(it)
        metin,opts,adim,istenen=etiketle(s,harf)
        kz=s['kart']; zor=s['zor']
        kaz={'pt-bicim':'Parçadaki anlatım biçimini belirler.','pt-yol':'Parçadaki düşünceyi geliştirme yollarını belirler.','pt-oncul':'Öncüllerde verilen düşünceyi geliştirme yollarını parçada sınar.','pt-kisi':'Kişileştirme, betimleme ve benzetmeyi ayırt eder.','pt-tanik':'Tanık gösterme ve sayısal veri kullanımını ayırt eder.'}[KARTLAR[kz]['tipId']]
        soru(Q,s['no'],kz,zor,kaz,3,metin,opts,harf,lambda t:t=='dogru',istenen,s['ip'],s['bilgi'],adim,s['puf'])
kur_hepsi()
bitir(Q)
