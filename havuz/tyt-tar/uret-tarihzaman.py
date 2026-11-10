"""TYT Tarih · Tarih ve Zaman (hafif mod): 4 ana soru. Metinler özgündür."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _hafif_tar_a import *
K=Konu('tarihzaman','Tarih ve Zaman','tar|Tarih ve Zaman',4)
K.zd={'kolay': 2, 'orta': 2}
K.kart('K-TZ-01','Yardımcı Bilimler','Anlatılan çalışmaya bakıp hangi yardımcı bilimin kullanıldığını bulmak.','Sikke, yazıt, belge ve kazı buluntusunu inceleyen bilimleri karıştırmak.','kolay','düz',2,'tz-yardimci','Yardımcı bilimleri eşleştirme')
K.kart('K-TZ-02','Takvimler','Hicri, Celali ve Miladi takvimlerin başlangıç ve esaslarını öncüllerle ayırmak.','Takvimlerin başlangıç olayını ve dönemini birbirine karıştırmak.','orta','öncüllü',3,'tz-takvim','Takvimlerin özelliklerini ayırt etme')
K.kart('K-TZ-03','Tarih Öncesi ve Tarihî Devirler','Yazının bulunuşunun tarih öncesi ile tarihî devirler arasında sınır olduğunu metinden çıkarmak.','Metinde olmayan çağ adlarını ve yargıları doğru saymak.','orta','yeni nesil',3,'tz-yazi','Yazı ve tarih öncesi ayrımı')
K.kart('K-TZ-04','Kaynak ve Yöntem','Tarihçinin kaynakları karşılaştırarak çalıştığını, deneyle sınama yapmadığını görmek.','Tarihî olayların deneyle yinelenebileceğini sanmak.','kolay','yeni nesil',4,'tz-kaynak','Tarih bilimi ve kaynak kullanımı')

K.Q('0001','K-TZ-01','kolay','Sikke incelemesinde yararlanılan yardımcı bilimi belirler.',
 'Bir tarihçi, bir hükümdar dönemine ait sikkelerin üzerindeki yazı ve resimleri inceleyerek o dönemin hükümdarı ve ekonomik yapısı hakkında bilgi edinmiştir.\nBu tarihçinin yararlandığı yardımcı bilim dalı aşağıdakilerden hangisidir?',
 [O('Epigrafi','Epigrafi anıt ve kaya gibi yüzeylerdeki yazıtları inceler; sikkeleri inceleyen bilim değildir.'),
  O('Nümizmatik'),
  O('Diplomatik','Diplomatik ferman, berat gibi resmî belgeleri inceler; sikke bu alana girmez.'),
  O('Arkeoloji','Arkeoloji kazı yaparak buluntuları bulur; sikke üzerindeki yazı ve resmi inceleyen dal nümizmatiktir.'),
  O('Kronoloji','Kronoloji olayların zaman sırasını ve tarihlerini inceler; sikkeyle ilgisi yoktur.')],
 'B','İncelenen buluntuya göre yardımcı bilim.',
 'Tarihçinin incelediği buluntu sikkedir; her yardımcı bilimin bir inceleme konusu vardır.',
 [B('Tarihin yardımcı bilimleri','Nümizmatik: sikkeler · Epigrafi: yazıtlar · Diplomatik: ferman, berat gibi belgeler · Arkeoloji: kazı buluntuları · Kronoloji: olayların zaman sırası')],
 [('İncelenen şeyi bul','Tarihçi, sikkelerin üzerindeki yazı ve resimlere bakıyor.','konu: sikke'),('Bilimi hatırla','Sikkeleri inceleyen yardımcı bilim dalı nümizmatiktir.','sikke = nümizmatik')],
 'Sikke, yazıt, belge ve kazı gibi her inceleme konusunun kendi yardımcı bilimi vardır.',
 'Her bilimin konusu ayrı verilip eşleştirildi.')

stm=[('Hicri takvim, Hz. Muhammed’in doğumunu başlangıç alır.',False,'Hicri takvimin başlangıcı hicrettir'),
     ('Celali takvimi, Büyük Selçuklu Sultanı Melikşah döneminde hazırlanmıştır.',True,'Celali takvimi Melikşah döneminde hazırlandı'),
     ('Miladi takvim, Hz. İsa’nın doğumunu başlangıç alır.',True,'Miladi takvimin başlangıcı Hz. İsa’nın doğumudur')]
op,isl=oncul(stm,['Yalnız I','I ve II','I ve III','II ve III','I, II ve III'],'D')
K.Q('0002','K-TZ-02','orta','Başlıca takvimlerin özelliklerini ayırt eder.',metin_oncul(stm,'Yukarıdaki takvim bilgilerinden hangileri doğrudur?'),
 op,'D','Doğru takvim bilgilerini bulma.',
 'Her takvimin başlangıç olayını ayrı ayrı düşün.',
 [B('Başlıca takvimler','Hicri: başlangıcı hicret (622), ay yılı esaslı · Celali: Melikşah döneminde hazırlandı, güneş yılı esaslı · Miladi: başlangıcı Hz. İsa’nın doğumu')],
 [('Öncülleri ayır','Üç öncül, üç farklı takvimin başlangıcını veya dönemini söylüyor.','I: Hicri · II: Celali · III: Miladi'),('Başlangıçları hatırla','Hicri takvim hicretle başlar; Celali Melikşah dönemine, Miladi Hz. İsa’nın doğumuna dayanır.','Hicri = hicret · Miladi = Hz. İsa’nın doğumu')],
 'Yalnız II ve III doğrudur; I yanlıştır.',
 'Takvimleri ayırmak için önce başlangıç olayını bil.','Her öncül başlangıç olayı ve dönemiyle kontrol edildi.',islem_son=isl)

K.Q('0003','K-TZ-03','orta','Yazının tarih öncesi ve tarihî devirleri ayırdığını metinden çıkarır.',
 'Sümerler, MÖ 3200 dolaylarında çivi yazısını kullanmaya başlamıştır. Tarihçiler, yazının bulunmasından önceki dönemi “tarih öncesi”, yazıdan sonraki dönemi “tarihî devirler” olarak adlandırır.\nBu bilgilere göre aşağıdakilerden hangisine ulaşılabilir?',
 [O('Tarih öncesi dönemlere ait yazılı kaynak bulunmadığına'),
  O('Sümerlerin Orta Çağ’da yaşadığına','Metinde Sümerlerin Orta Çağ’da yaşadığına dair bilgi yoktur; verilen tarih (MÖ 3200) çok daha eskidir.','dikkat'),
  O('Yazının bütün toplumlarda aynı anda ortaya çıktığına','Metin yazının Sümerler tarafından kullanıldığını söyler; bütün toplumlarda aynı anda çıktığı bilgisi yoktur.','dikkat'),
  O('Tarih öncesi dönemin hiç araştırılamayacağına','Metinde böyle bir bilgi yoktur; tarih öncesi, kazı buluntularıyla araştırılır.','bilgi'),
  O('Çivi yazısının Türkler tarafından bulunduğuna','Metin çivi yazısını Sümerlere bağlar; Türklerden söz etmez.','dikkat')],
 'A','Metinden çıkarılabilecek sonuç.',
 'Tarih öncesi ile tarihî devirleri ayıran ölçüt metinde açıkça verilmiş.',
 [B('Tarih öncesi ve tarihî devirler','Yazıdan önceki dönem tarih öncesi, yazıdan sonraki dönem tarihî devirlerdir · İlk yazı: Sümerlerin çivi yazısı (MÖ 3200 dolayı)')],
 [('Ölçütü bul','Metne göre dönemleri ayıran şey yazının bulunmasıdır.','ölçüt: yazı'),('Çıkarımı kur','Yazıdan önce yazı yoksa o dönemler için yazılı kaynak da yoktur.','yazıdan önce: yazılı kaynak yok')],
 'Şıkların metinde dayanağı olup olmadığına bak; yalnız metnin gösterdiğine ulaş.',
 'Metindeki ölçütten çıkan yargıyı bul, dayanağı olmayanları ele.')

K.Q('0004','K-TZ-04','kolay','Tarihçinin kaynaklarla çalışma yöntemini yorumlar.',
 'Bir tarihçi, bir olayı incelerken olaya tanık olanların anılarını ve dönemin resmî belgelerini birlikte ele almış; kaynaklar arasındaki farkları karşılaştırarak olayı yeniden kurmaya çalışmıştır.\nBu bilgilere göre aşağıdakilerden hangisine ulaşılamaz?',
 [O('Tarihçinin birden çok kaynaktan yararlandığına','Metinde anılar ve belgeler birlikte kullanıldığı için buna ulaşılır; soru ulaşılamayanı ister.','dikkat'),
  O('Kaynakların birbiriyle karşılaştırıldığına','Metinde farklar karşılaştırıldığı açıkça yazar; bu yargıya ulaşılır.','dikkat'),
  O('Tanık anlatımlarının araştırmada kaynak olarak kullanılabildiğine','Metinde tanıkların anıları ele alınmıştır; bu yargıya ulaşılır.','dikkat'),
  O('Resmî belgelerin olayın yeniden kurulmasında kullanıldığına','Metinde dönemin resmî belgeleri ele alınmıştır; bu yargıya ulaşılır.','dikkat'),
  O('Olayın deney ortamında yinelenerek sınandığına')],
 'E','Metinden çıkarılamayan yargı.',
 'Tarihî olaylar yeniden yaşanabilir mi, deneyle sınanabilir mi?',
 [B('Tarih biliminin yöntemi','Tarihî olaylar tekrar edilemez, deneyle sınanamaz · Tarihçi belge, buluntu, anı gibi kaynakları karşılaştırarak olayı yeniden kurar')],
 [('Soru kökünü oku','Kök “ulaşılamaz” diyor; yani metinden çıkmayan yargıyı arıyoruz.','aranan: çıkmayan yargı'),('Kaynakları say','Metinde tanık anıları, resmî belgeler ve karşılaştırma var; deney yok.','anı + belge + karşılaştırma')],
 'Deney yapılmadığı için olayın yinelenerek sınandığına ulaşılamaz.',
 '“Ulaşılamaz” köklerinde metinden çıkanları ele, çıkmayanı seç.','Metindeki dört yargı çıkarılabilir; deneyle sınama çıkarılamaz.')
K.bitir()
