"""TYT Tarih · İslam Medeniyetinin Doğuşu (hafif mod): 4 ana soru. Tarihsel, siyasi ve kültürel olgular; metinler özgündür."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _hafif_tar_a import *
K=Konu('islammed','İslam Medeniyetinin Doğuşu','tar|İslam Medeniyetinin Doğuşu',4)
K.zd={'kolay': 2, 'orta': 2}
K.kart('K-IM-01','Yönetim Merkezleri','Emevi ve Abbasi devletlerinin yönetim merkezlerini ayırmak.','Şam, Bağdat, Medine ve Kurtuba’yı birbirine karıştırmak.','kolay','düz',2,'im-merkez','Yönetim merkezlerini eşleştirme')
K.kart('K-IM-02','Talas ve Kâğıt','Talas Savaşı’nın kâğıt üretimine etkisini metinden çıkarmak.','Metinde olmayan sonucu (matbaa gibi) kesin sanmak ya da savaşın sonucunu ters okumak.','orta','yeni nesil',3,'im-talas','Talas Savaşı ve kâğıt')
K.kart('K-IM-03','Dönemlerin Olayları','Abbasi dönemine ait doğru ve yanlış bilgileri öncüllerle ayırmak.','Beytü’l-Hikme’yi Emevilere, Bağdat’ı Emevilere yazmak.','orta','öncüllü',3,'im-donem','Abbasi dönemi öncülleri')
K.kart('K-IM-04','Bilim ve Çeviri Hareketi','Beytü’l-Hikme metninden çıkarılamayan yargıyı bulmak.','Metinde olmayan karşılaştırmaları (Avrupa kurumları gibi) çıkarılabilir sanmak.','kolay','yeni nesil',4,'im-bilim','Beytü’l-Hikme ve bilim')

K.Q('0001','K-IM-01','kolay','Emevi Devleti’nin yönetim merkezini belirler.',
 'Muaviye, 661’de Emevi Devleti’ni kurmuştur.\nBu devletin yönetim merkezi aşağıdakilerden hangisidir?',
 [O('Mekke','Mekke, Emevi Devleti’nin yönetim merkezi olmamıştır.'),
  O('Medine','Medine ilk halifeler döneminin merkeziydi; Emevi Devleti’nin merkezi değildir.'),
  O('Şam'),
  O('Bağdat','Bağdat, Abbasi Devleti’nin başkentidir; Emeviler dönemine ait değildir.'),
  O('Kurtuba','Kurtuba, Endülüs’te kurulan Emevi devletinin merkezidir; Muaviye’nin kurduğu devletin değil.')],
 'C','Emevi Devleti’nin yönetim merkezi.',
 'Emevilerin merkezi Suriye’de bir şehirdi; Bağdat daha sonra Abbasilerin merkezi oldu.',
 [B('Yönetim merkezleri','İlk dört halife: Medine (Hz. Ali döneminde Kûfe de) · Emeviler: Şam · Abbasiler: Bağdat · Endülüs Emevileri: Kurtuba')],
 [('Soruyu oku','Soru Muaviye’nin kurduğu Emevi Devleti’nin merkezini soruyor.','devlet: Emevi'),('Şıkları eşle','Bağdat Abbasilerin, Kurtuba Endülüs Emevilerinin merkezidir; Emevilerin merkezi Şam’dır.','Emeviler = Şam')],
 'Devlet adını merkezle eşleştir: Emevi–Şam, Abbasi–Bağdat.','Merkezler devletlerle eşleştirildi.')

K.Q('0002','K-IM-02','orta','Talas Savaşı’nın kâğıt üretimine etkisini metinden çıkarır.',
 '751’de Talas’ta Abbasi ordusu ile Çin ordusu karşılaşmış ve Abbasiler savaşı kazanmıştır. Savaşta esir alınan Çinli ustalar aracılığıyla kâğıt yapım tekniği öğrenilmiş ve Semerkant’ta kâğıt üretimi başlamıştır.\nBu bilgilere göre aşağıdakilerden hangisine ulaşılabilir?',
 [O('Çin’in Orta Asya’daki egemenliğinin savaşla pekiştiğine','Abbasiler savaşı kazanmıştır; yargı sonucu tersine çevirmiştir.','dikkat'),
  O('Kâğıt bilgisinin İslam dünyasına geçtiğine'),
  O('Matbaanın Talas’ta icat edildiğine','Metinde matbaadan söz edilmez; kâğıt üretiminden söz edilir.','dikkat'),
  O('Savaşı Abbasilerin Çinlilere kaybettiğine','Metinde Abbasilerin savaşı kazandığı açıkça yazar.','dikkat'),
  O('Semerkant’ta kâğıt üretiminin başlamadığına','Metinde Semerkant’ta kâğıt üretiminin başladığı yazar; yargı metinle çelişir.','dikkat')],
 'B','Metinden çıkarılabilecek sonuç.',
 'Kâğıt yapımını öğrenen taraf kimdi, üretim nerede başladı?',
 [B('Talas Savaşı (751)','Abbasiler Çin ordusunu yendi · Çinli esirlerden kâğıt yapımı öğrenildi · Semerkant’ta kâğıt üretimi başladı')],
 [('Savaşın sonucunu bul','Abbasiler savaşı kazanmış, Çinli ustalar esir alınmış.','kazanan: Abbasiler'),('Sonucu çıkar','Öğrenilen teknikle Semerkant’ta kâğıt üretimi başlamış; bu, üretimin İslam coğrafyasında yayılmasına zemin hazırlar.','kâğıt → Semerkant → yayılma')],
 'Savaşın kazananını ve metindeki neden-sonuç zincirini doğru oku.','Şıklar metindeki savaş sonucu ve üretim bilgisiyle karşılaştırıldı.')

stm=[('Abbasi Devleti’nin başkenti Bağdat’tır.',True,'Abbasiler Bağdat’ı başkent yaptı'),
     ('Beytü’l-Hikme, Emeviler döneminde Şam’da kurulmuştur.',False,'Beytü’l-Hikme Abbasi dönemine ve Bağdat’a aittir'),
     ('Talas Savaşı’nda Abbasi ordusu Çin ordusunu yenmiştir.',True,'Abbasiler Talas’ta kazandı')]
op,isl=oncul(stm,['Yalnız I','Yalnız II','I ve II','II ve III','I ve III'],'E')
K.Q('0003','K-IM-03','orta','Abbasi dönemine ait doğru bilgileri ayırt eder.',metin_oncul(stm,'Yukarıdaki bilgilerden hangileri doğrudur?'),
 op,'E','Doğru bilgiler.',
 'Beytü’l-Hikme hangi hanedanla ve hangi şehirle anılır?',
 [B('Abbasi dönemi','Başkent: Bağdat · Bilim ve çeviri merkezi: Beytü’l-Hikme (Bağdat) · Talas Savaşı (751): Çin ordusuna karşı kazanılan zafer')],
 [('Öncülleri tek tek al','Her öncül farklı bir olgu: başkent, bilim kurumu, savaş.','I: başkent · II: kurum · III: savaş'),('Bilgiyle karşılaştır','Bağdat ve Talas doğrudur; Beytü’l-Hikme Emevilere değil Abbasilere aittir.','I, III doğru · II yanlış')],
 'Kurumu, şehri ve hanedanı birbirine karıştırma: Beytü’l-Hikme Abbasi dönemi Bağdat’tadır.','Her öncül dönem ve yerle kontrol edildi.',islem_son=isl)

K.Q('0004','K-IM-04','kolay','Çeviri ve bilim faaliyetini anlatan metinden çıkarılamayan yargıyı bulur.',
 'Abbasi halifesi Memun döneminde gelişen Bağdat’taki Beytü’l-Hikme’de Yunanca, Farsça ve Sanskritçe eserler Arapçaya çevrilmiş; Harezmî gibi bilginler burada matematik ve astronomi alanında çalışmıştır.\nBu bilgilere göre aşağıdakilerden hangisine ulaşılamaz?',
 [O('Farklı kültürlere ait eserlerden yararlanıldığına','Yunanca, Farsça ve Sanskritçe eserlerin çevrildiği yazar; bu yargıya ulaşılır, soru ulaşılamayanı ister.','dikkat'),
  O('Bağdat’ta bilimsel çalışmaların yürütüldüğüne','Metinde Bağdat’taki Beytü’l-Hikme’de çalışıldığı yazar; bu yargıya ulaşılır.','dikkat'),
  O('Matematik ve astronomiyle ilgilenen bilginlerin bulunduğuna','Harezmî gibi bilginlerin bu alanlarda çalıştığı yazar; bu yargıya ulaşılır.','dikkat'),
  O('Avrupa’da Beytü’l-Hikme’den önce akademiler kurulduğuna'),
  O('Arapçanın bilim dili olarak kullanıldığına','Eserlerin Arapçaya çevrilip çalışmalarda kullanılması bunu gösterir; bu yargıya ulaşılır.','dikkat')],
 'D','Metinden çıkarılamayan yargı.',
 'Metinde Avrupa’dan söz ediliyor mu?',
 [B('Beytü’l-Hikme','Bağdat’ta Abbasi döneminde (özellikle Memun zamanında) gelişen bilim ve çeviri merkezi · Yunanca, Farsça, Sanskritçe eserler Arapçaya çevrildi · Harezmî: matematik ve astronomi')],
 [('Kök “ulaşılamaz” diyor','Metinden çıkmayan yargıyı arıyoruz.','aranan: çıkmayan'),('Metni tara','Metin Bağdat’taki çeviri ve bilim çalışmasını anlatır; Avrupa’dan hiç söz etmez.','Avrupa: metinde yok')],
 'Metinde olmayan karşılaştırmalar (Avrupa gibi) çıkarılamaz.','Dört yargı metinde karşılık buldu; Avrupa ile ilgili olan bulmadı.')
K.bitir()
