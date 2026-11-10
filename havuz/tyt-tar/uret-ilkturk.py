"""TYT Tarih · İlk ve Orta Çağlarda Türk Dünyası (hafif mod): 6 ana soru. Metinler özgündür."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _hafif_tar_a import *
K=Konu('ilkturk','İlk ve Orta Çağlarda Türk Dünyası','tar|İlk ve Orta Çağlarda Türk Dünyası',6)
K.zd={'kolay': 3, 'orta': 3}
K.kart('K-IT-01','Orhun Yazıtları','Yazıtların hükümdar adlarından hangi devlete ait olduğunu bulmak.','Orhun alanındaki Göktürk ve Uygur yazıtlarını karıştırmak.','kolay','düz',2,'it-yazit','Orhun Yazıtları ve devlet')
K.kart('K-IT-02','Türk Devlet Geleneği','Kut anlayışı ve ortak egemenliği tahta geçiş kuralından ayırmak.','Tahta yalnız en büyük oğlun çıktığını sanmak.','orta','öncüllü',3,'it-gelenek','Türk devlet geleneği öncülleri')
K.kart('K-IT-03','Kavimler Göçü','Hunların batıya ilerleyişinin Avrupa’daki sonucunu metinden çıkarmak.','Metinde olmayan bir olayı (Roma’yı tek başına Hunların yıkması gibi) kesin saymak.','orta','yeni nesil',3,'it-gocu','Kavimler Göçü’nün nedeni')
K.kart('K-IT-04','Uygurlar','Uygurların yerleşik hayata geçişini metinden çıkarmak.','Metinde olmayan bir bilgiyi (zamanı kaçırarak) doğru saymak.','orta','yeni nesil',3,'it-uygur','Uygurlarda yerleşik hayat')
K.kart('K-IT-05','Göktürklerde Yönetim','Devletin kuruluşu ve bölünmesinden hanedan ortak egemenliğini çıkarmak.','Metinde olmayan çöküş nedenini (Çin saldırısı gibi) çıkarılabilir sanmak.','kolay','yeni nesil',4,'it-gokturk','Göktürk yönetim yapısı')
K.kart('K-IT-06','Bozkır Coğrafyası ve Yaşam','Coğrafyanın yaşam biçimine ve ordu yapısına etkisini metinden çıkarmak.','Metinde olmayan geçim biçimlerini (tarım, ticaret gibi) çıkarılabilir sanmak.','kolay','yeni nesil',4,'it-yasam','Coğrafya ve yaşam biçimi')

K.Q('0001','K-IT-01','kolay','Orhun Yazıtları’nın ait olduğu devleti belirler.',
 'Bilge Kağan, Kül Tigin ve Tonyukuk adına dikilen Orhun Yazıtları, Türkçenin bilinen en eski yazılı belgeleri arasındadır.\nBu yazıtlar aşağıdaki Türk devletlerinden hangisine aittir?',
 [O('Asya Hun Devleti','Bilge Kağan, Kül Tigin ve Tonyukuk Asya Hun Devleti’ne değil, çok sonraki bir döneme, Göktürklere aittir.'),
  O('Avar Hanlığı','Avarlar Orta Avrupa’da devlet kurmuştur; Orhun Yazıtları onların değildir.'),
  O('Uygur Devleti','Uygurlar da Orhun bölgesinde yazıt bırakmıştır, fakat Bilge Kağan ve Kül Tigin Göktürk hükümdarlarıdır.'),
  O('Hazar Hakanlığı','Hazarlar Karadeniz’in kuzeyinde devlet kurmuştur; Orhun Yazıtları onların değildir.'),
  O('Göktürk Devleti')],
 'E','Yazıtların ait olduğu devlet.',
 'Kül Tigin ve Bilge Kağan hangi devletin hükümdarlarıdır?',
 [B('Orhun Yazıtları','Kül Tigin (732) ve Bilge Kağan (735) yazıtları ile Tonyukuk yazıtı Göktürklere aittir · Türkçenin bilinen en eski yazılı belgelerindendir')],
 [('Hükümdarları bul','Soruda Bilge Kağan, Kül Tigin ve Tonyukuk geçiyor.','Bilge Kağan · Kül Tigin · Tonyukuk'),('Devleti hatırla','Bu isimler Göktürk Devleti’nin hükümdar ve devlet adamlarıdır.','Göktürk Devleti')],
 'Yazıttaki hükümdar adı, yazıtın hangi devlete ait olduğunu gösterir.','Hükümdar adları her devletle eşleştirildi.')

stm=[('Hükümdarın yönetme yetkisinin Tanrı tarafından verildiğine inanılmıştır (kut anlayışı).',True,'kut anlayışı bunu söyler'),
     ('Ülke, hanedan üyelerinin ortak malı sayılmıştır.',True,'ortak egemenlik anlayışı vardı'),
     ('Tahta yalnızca en büyük oğul çıkabilmiştir.',False,'hanedanın diğer üyeleri de tahta çıkabilirdi')]
op,isl=oncul(stm,['Yalnız I','Yalnız III','I ve II','II ve III','I, II ve III'],'C')
K.Q('0002','K-IT-02','orta','Türk devlet geleneğine ait bilgileri ayırt eder.',metin_oncul(stm,'Türk devlet geleneğiyle ilgili yukarıdaki bilgilerden hangileri doğrudur?'),
 op,'C','Doğru devlet geleneği bilgileri.',
 'Ülkenin kime ait sayıldığını düşün: tek kişiye mi, hanedana mı?',
 [B('Türk devlet geleneği','Kut: hükümdarın yönetme yetkisi Tanrı’dan gelir · Ortak egemenlik: ülke hanedanın ortak malıdır · Tahta geçişte kesin bir tek kural yoktu')],
 [('Kavramları hatırla','Kut anlayışı yetkinin kaynağını, ortak egemenlik ülkenin kime ait olduğunu anlatır.','kut · ortak egemenlik'),('Öncülleri kontrol et','I ve II bu kavramlara uyar; III’teki “yalnızca en büyük oğul” kuralı yoktur.','I, II doğru · III yanlış')],
 'Türklerde ülke hanedanın ortak malıydı; bu yüzden tahta yalnız büyük oğul çıkmak zorunda değildi.','Her öncül kut ve ortak egemenlikle kontrol edildi.',islem_son=isl)

K.Q('0003','K-IT-03','orta','Hunların batıya ilerleyişinin Avrupa’daki sonucunu metinden çıkarır.',
 '4. yüzyılın sonlarında Hunlar Orta Asya’dan batıya ilerleyerek Karadeniz’in kuzeyine ulaşmıştır. Hunların baskısı altında kalan Germen kavimleri yerlerini bırakarak Roma topraklarına yönelmiştir.\nBu bilgilere göre aşağıdakilerden hangisine ulaşılabilir?',
 [O('Hun ilerleyişinin Avrupa’da göçlere yol açtığına'),
  O('Roma İmparatorluğu’nun Hunlar tarafından tek başına yıkıldığına','Metinde Hunların Roma’yı yıktığı söylenmez; yalnız Germen kavimlerinin Roma topraklarına yöneldiği anlatılır.','dikkat'),
  O('Germen kavimlerinin Orta Asya’ya göç ettiğine','Germen kavimleri Roma topraklarına yönelmiştir, Orta Asya’ya değil; yargı metinle çelişir.','bilgi'),
  O('Germen kavimlerinin Hunlara baskı uyguladığına','Metinde baskıyı Hunlar uygular; yargı yönü tersine çevirmiştir.','dikkat'),
  O('Hunların Çin’e doğru ilerlediğine','Metinde Hunların batıya, Karadeniz’in kuzeyine ilerlediği yazar; Çin’den söz edilmez.','dikkat')],
 'A','Metinden çıkarılabilecek sonuç.',
 'Hunların baskısı kimleri nereye yönlendirdi?',
 [B('Kavimler Göçü','Hunların batıya ilerleyişi (4. yüzyılın sonları) Germen kavimlerini yerlerinden etti · Göç, Roma sınırlarında büyük değişimlere yol açtı')],
 [('Olayları sırala','Hunlar batıya ilerliyor, Germen kavimleri baskı görüyor, Roma topraklarına yöneliyor.','Hun → Germen → Roma'),('Sonucu çıkar','Bu zincir, kavimlerin yer değiştirmesinin Hun ilerleyişinden kaynaklandığını gösterir.','Hun baskısı → yer değiştirme')],
 'Neden-sonuç zincirini metindeki sıraya göre kur.','Zincirin yönü metne göre kontrol edildi.')

K.Q('0004','K-IT-04','orta','Uygurların yerleşik hayata geçişini metinden çıkarır.',
 'Uygurlar 744’te Orhun Nehri çevresinde devlet kurmuştur. 840’ta Kırgızların saldırısı üzerine bir bölümü Doğu Türkistan’a yönelmiş ve buradaki vahalarda tarıma ve şehir hayatına dayalı yerleşik bir düzen kurmuştur.\nBu bilgilere göre aşağıdakilerden hangisine ulaşılabilir?',
 [O('Uygurların İslamiyet’i kabul ettiğine','Metinde İslamiyet’ten hiç söz edilmez; dayanağı olmayan bir yargıdır.','dikkat'),
  O('Uygur Devleti’nin Kırgızlar tarafından 744’te kurulduğuna','744 Uygur Devleti’nin kuruluş yılıdır; Kırgız saldırısı 840’tadır.','dikkat'),
  O('Uygurların 840’tan önce Doğu Türkistan’da tarım yaptığına','Metne göre Doğu Türkistan’a yönelme 840’taki Kırgız saldırısından sonradır.','dikkat'),
  O('Uygurların bir bölümünün göçebelikten yerleşik hayata geçtiğine'),
  O('Uygur Devleti’nin Batı Avrupa’ya kadar genişlediğine','Metinde Uygurların Orhun ve Doğu Türkistan çevresindeki yaşamı anlatılır; Avrupa’dan söz edilmez.','dikkat')],
 'D','Metinden çıkarılabilecek sonuç.',
 'Doğu Türkistan’da kurulan düzenin özelliklerine bak: tarım ve şehir.',
 [B('Uygurlar','744’te Orhun çevresinde devlet kurdular · 840’ta Kırgız saldırısıyla dağıldılar · Doğu Türkistan’da tarıma ve şehir hayatına dayalı yerleşik düzene geçtiler')],
 [('Zamanı sırala','Önce 744’te Orhun’da devlet, sonra 840’ta saldırı ve Doğu Türkistan’a yöneliş.','744 → 840 → Doğu Türkistan'),('Yaşam biçimini oku','Doğu Türkistan’da tarıma ve şehir hayatına dayalı yerleşik düzen kurulmuş.','tarım + şehir = yerleşik')],
 'Metindeki tarih sırasına dikkat et; sırayı bozan şıkları ele.','Şıklar metindeki tarih sırası ve bilgilerle karşılaştırıldı.')

K.Q('0005','K-IT-05','kolay','Göktürklerde yönetim yapısını metinden çıkarır.',
 'Bumin Kağan, 552’de Türk boylarını birleştirerek devleti kurmuş; batıdaki toprakların yönetimini kardeşi İstemi’ye vermiştir. Devlet zamanla doğu ve batı olmak üzere iki ayrı yönetime ayrılmıştır.\nBu bilgilere göre aşağıdakilerden hangisine ulaşılamaz?',
 [O('Devletin kuruluşunda boyların birleştirildiğine','Metin Bumin’in boyları birleştirdiğini söyler; bu yargıya ulaşılır, soru ulaşılamayanı ister.','dikkat'),
  O('Çin’in Göktürk Devleti’ni 552’de yıktığına'),
  O('Batıdaki yönetimin hanedan üyesine verildiğine','İstemi, Bumin’in kardeşidir; bu yargıya ulaşılır.','dikkat'),
  O('Devletin zamanla iki ayrı yönetime ayrıldığına','Metinde devletin doğu ve batı olarak ikiye ayrıldığı yazar; bu yargıya ulaşılır.','dikkat'),
  O('Yönetim yetkisinin hanedan üyeleri arasında paylaşıldığına','Batıyı kardeşe vermek yetkinin paylaşıldığını gösterir; bu yargıya ulaşılır.','dikkat')],
 'B','Metinden çıkarılamayan yargı.',
 'Metinde Çin’den ya da devletin yıkılışından söz ediliyor mu?',
 [B('Göktürk Devleti’nin kuruluşu','Bumin Kağan (552) devleti kurdu · İstemi Yabgu batıyı yönetti · Devlet doğu ve batı olmak üzere ikiye ayrıldı · Yönetimde ortak egemenlik anlayışı vardı')],
 [('Kök “ulaşılamaz” diyor','Metinden çıkmayan yargıyı arıyoruz.','aranan: çıkmayan'),('Metni taranır','Metin kuruluşu, İstemi’yi ve ikiye ayrılmayı anlatır; Çin ve yıkılış hiç geçmez.','Çin: metinde yok')],
 'Çin’in devleti 552’de yıktığı metinde yer almaz (552 devletin kuruluş yılıdır).','Her yargı metindeki bir cümleyle eşlendi; eşlenmeyen seçildi.')

K.Q('0006','K-IT-06','kolay','Coğrafyanın yaşam biçimi ve ordu yapısına etkisini metinden çıkarır.',
 'Orta Asya bozkırlarında yaşayan Türk boyları, hayvanlarının otlak ihtiyacını karşılamak için mevsimlere göre yer değiştirmiş ve kolayca taşınabilen çadırlarda yaşamıştır. At, bu yaşam biçiminde hem ulaşım hem de savaş aracı olarak kullanılmış; bozkır boyları atlı birliklerden oluşan hareketli ordular kurmuştur.\nBu bilgilere göre aşağıdakilerden hangisine ulaşılabilir?',
 [O('Bozkır boylarının geçimini büyük ölçüde tarıma dayandırdığına','Metin hayvanlarının otlak ihtiyacı için yer değiştiren boyları anlatır; geçimin tarıma dayandığı yargısı metinde yoktur.','dikkat'),
  O('Türk boylarının yerleşik şehir hayatına geçtiğine','Metin yer değiştiren, çadırda yaşayan boyları anlatır; yargı metinle çelişir.','bilgi'),
  O('Atın hayvancılıktan daha önemli bir geçim kaynağı olduğuna','Metne göre at ulaşım ve savaş aracıdır; geçim kaynağı olduğundan söz edilmez.','dikkat'),
  O('Kalıcı taş yapıların tercih edildiğine','Metinde kolayca taşınabilen çadırlar anlatılır; yargı metinle çelişir.','bilgi'),
  O('Coğrafi koşulların yaşam biçimini etkilediğine')],
 'E','Metinden çıkarılabilecek sonuç.',
 'Otlak arayışı ve at kullanımı yaşamı ve ordu yapısını nasıl şekillendirmiş?',
 [B('Bozkır yaşamı','Hayvancılık, otlak için yer değiştirme (göçebelik) · Taşınabilir çadır (yurt) · At: ulaşım ve savaş aracı · Atlı birliklerden oluşan hareketli ordular')],
 [('İki etkiyi ayır','Bozkırdaki otlak ihtiyacı yer değiştirmeyi ve çadırı, ata dayanan yaşam ordu yapısını belirlemiş.','otlak → göçebelik · at → atlı ordu'),('Şıkları metinle karşılaştır','Her şıkkı metindeki cümleyle karşılaştır; metinde dayanağı olmayan ya da metne ters şıklar elenir.','metin-şık eşleştirmesi')],
 'Her şıkkın dayanağını metinde ara; dayanağı olan tek yargı doğrudur.','Şıklar metindeki bilgilerle tek tek karşılaştırıldı.')
K.bitir()
