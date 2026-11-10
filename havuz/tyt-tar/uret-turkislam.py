"""TYT Tarih · İlk Türk İslam Devletleri (hafif mod): 6 ana soru. Metinler özgündür."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _hafif_tar_a import *
K=Konu('turkislam','İlk Türk İslam Devletleri','tar|İlk Türk İslam Devletleri',6)
K.zd={'kolay': 1, 'orta': 5}
K.kart('K-TI-01','Karahanlı Kültür Eserleri','Eserin yazarından ve kaleme alındığı devri bulmak.','Karahanlı, Gazneli ve Büyük Selçuklu eserlerini karıştırmak.','kolay','düz',2,'ti-eser','Eserden devleti belirleme')
K.kart('K-TI-02','Dandanakan ve Kuruluş','Dandanakan Savaşı’nın siyasi sonucunu metinden çıkarmak.','Metinde olmayan sonucu (Anadolu’nun fethi, Bağdat’a giriş gibi) çıkarılabilir sanmak.','orta','yeni nesil',3,'ti-kurulus','Dandanakan ve Selçuklu kuruluşu')
K.kart('K-TI-03','Eser, Yazar ve Devlet','Eser–yazar bilgilerinin doğru olanlarını öncüllerle ayırmak.','Şehname’yi Karahanlılara, Siyasetname’yi Gaznelilere bağlamak.','orta','öncüllü',3,'ti-yazar','Eser ve yazar eşleştirme')
K.kart('K-TI-04','İktâ Sistemi','İktâ sisteminin orduya ve hazineye etkisini metinden çıkarmak.','İktâ sahibini toprağın mülk sahibi sanmak.','orta','yeni nesil',3,'ti-ikta','İktâ sistemi')
K.kart('K-TI-05','Selçuklu–Abbasi İlişkisi','Tuğrul Bey’in Bağdat’a girişinin siyasi sonucunu çıkarmak.','Halifeliğin Selçuklu hanedanına geçtiğini ya da Abbasilerin yıkıldığını sanmak.','orta','yeni nesil',4,'ti-halife','Selçukluların Bağdat’a girişi')
K.kart('K-TI-06','Nizamiye Medreseleri','Medrese kurulmasının eğitim politikasına dair çıkarımını yapmak.','Metinde olmayan ayrıntıları (ders programı, ücret) çıkarılabilir sanmak.','orta','yeni nesil',4,'ti-medrese','Nizamiye Medreseleri')

K.Q('0001','K-TI-01','kolay','Kutadgu Bilig’in yazıldığı devleti belirler.',
 'Balasagunlu Yusuf Has Hacib, Kutadgu Bilig’i hükümdara sunmuştur.\nKutadgu Bilig aşağıdaki Türk-İslam devletlerinden hangisi döneminde yazılmıştır?',
 [O('Karahanlılar'),
  O('Gazneliler','Gaznelilerin merkezi Gazne’dir; Balasagunlu Yusuf Has Hacib Gazneli değil, Karahanlı topraklarında yaşamıştır.'),
  O('Büyük Selçuklu Devleti','Büyük Selçuklu’nun ünlü eserleri arasında Siyasetname vardır; Kutadgu Bilig değil.'),
  O('Harezmşahlar','Harezmşahlar Büyük Selçuklu’dan sonra Harezm’de güçlenmiştir; Kutadgu Bilig onların döneminde yazılmamıştır.'),
  O('Tolunoğulları','Tolunoğulları Mısır’da kurulmuş bir Türk-İslam devletidir; Kutadgu Bilig Orta Asya’da yazılmıştır.')],
 'A','Kutadgu Bilig’in yazıldığı devlet.',
 'Balasagun ve Kaşgar hangi devletin önemli şehirleriydi?',
 [B('Karahanlı kültür eserleri','Kutadgu Bilig: Balasagunlu Yusuf Has Hacib · Divanü Lügati’t-Türk: Kaşgarlı Mahmud · Atabetü’l-Hakayık: Edip Ahmet Yükneki')],
 [('Eseri ve yazarı not et','Eser Kutadgu Bilig, yazarı Balasagunlu Yusuf Has Hacib.','Yusuf Has Hacib · Balasagunlu'),('Devleti hatırla','Balasagun ve Kaşgar Karahanlıların şehirleridir; eser Karahanlı hükümdarına sunulmuştur.','Karahanlılar')],
 'Eser–yazar–devlet üçlüsünü birlikte hatırla.','Eserin yazıldığı yer devletlerin merkezleriyle eşleştirildi.')

K.Q('0002','K-TI-02','orta','Dandanakan Savaşı’nın siyasi sonucunu metinden çıkarır.',
 '1040’ta Dandanakan’da Gazneli ordusunu yenen Selçuklular, Horasan’ın denetimini ele geçirmiş ve Tuğrul Bey sultan ilan edilmiştir.\nBu bilgilere göre aşağıdakilerden hangisine ulaşılabilir?',
 [O('Gaznelilerin Selçukluları Horasan’dan çıkardığına','Metinde Selçukluların Gazneli ordusunu yendiği ve Horasan’ı aldığı yazar; yargı sonucu tersine çevirmiştir.','dikkat'),
  O('Selçukluların Anadolu’yu fethettiğine','Metinde Anadolu’dan söz edilmez; savaş Horasan’da yapılmıştır.','dikkat'),
  O('Selçuklu Devleti’nin Malazgirt Savaşı’ndan sonra kurulduğuna','Metindeki tarih 1040’tır; Malazgirt 1071’dedir ve Selçuklu Devleti ondan öncedir.','bilgi'),
  O('Horasan’da Gazneli üstünlüğünün sona erdiğine'),
  O('Tuğrul Bey’in Bağdat’a girdiğine','Metinde Bağdat’tan söz edilmez; Tuğrul Bey’in Bağdat’a girişi 1055’tedir.','bilgi')],
 'D','Metinden çıkarılabilecek sonuç.',
 'Gazneli ordusunu yenen ve Horasan’ı alan taraf kimdir?',
 [B('Dandanakan Savaşı (1040)','Selçuklular Gazneli ordusunu yendi · Horasan’ın denetimi Selçuklulara geçti · Tuğrul Bey sultan ilan edildi')],
 [('Savaşın tarafını bul','Kazanan Selçuklular, yenilen Gaznelilerdir.','kazanan: Selçuklu'),('Sonucu çıkar','Selçuklular Horasan’ı alınca Gazneli üstünlüğü orada sona ermiştir.','Horasan: Selçuklu')],
 'Savaşın kazananını ve yerini metinden doğru oku.','Şıklar metindeki taraf, yer ve tarihle karşılaştırıldı.')

stm=[('Siyasetname, Büyük Selçuklu veziri Nizamülmülk tarafından yazılmıştır.',True,'Siyasetname’nin yazarı Nizamülmülk’tür'),
     ('Firdevsi’nin Şehname adlı eseri Karahanlı hükümdarına sunulmak üzere yazılmıştır.',False,'Şehname, Gazneli Sultanı Mahmud’a sunulmuştur'),
     ('Divanü Lügati’t-Türk’ün yazarı Kaşgarlı Mahmud’dur.',True,'Divanü Lügati’t-Türk Kaşgarlı Mahmud’undur')]
op,isl=oncul(stm,['Yalnız I','I ve III','II ve III','I ve II','I, II ve III'],'B')
K.Q('0003','K-TI-03','orta','Eser ve yazar bilgilerinin doğru olanlarını ayırt eder.',metin_oncul(stm,'Yukarıdaki bilgilerden hangileri doğrudur?'),
 op,'B','Doğru eser ve yazar bilgileri.',
 'Şehname hangi sultanın sarayıyla anılır?',
 [B('Türk-İslam devletlerinin eserleri','Siyasetname: Nizamülmülk (Büyük Selçuklu) · Şehname: Firdevsi (Gazneli Mahmud’a sunuldu) · Divanü Lügati’t-Türk: Kaşgarlı Mahmud · Kutadgu Bilig: Yusuf Has Hacib (Karahanlı)')],
 [('Öncülleri ayır','Üç öncül üç farklı eser–yazar ilişkisini söylüyor.','I: Siyasetname · II: Şehname · III: DLT'),('Bilgileri doğrula','Siyasetname Nizamülmülk’ün, DLT Kaşgarlı Mahmud’undur; Şehname ise Gazneli Mahmud’a sunulmuştur.','I, III doğru · II yanlış')],
 'Eserleri yazarı ve sunulduğu hükümdarla birlikte öğren; Şehname Gazneli Mahmud’la anılır.','Her öncül eser–yazar–hükümdar bilgisiyle kontrol edildi.',islem_son=isl)

K.Q('0004','K-TI-04','orta','İktâ sisteminin orduya ve hazineye etkisini metinden çıkarır.',
 'Büyük Selçuklu Devleti’nde iktâ sisteminde devlet, bir bölgenin vergi gelirlerini asker komutanlarına bırakmış; iktâ sahipleri karşılığında belirli sayıda asker beslemekle yükümlü olmuştur. Toprağın mülkiyeti ise devlete ait kalmıştır.\nBu bilgilere göre aşağıdakilerden hangisine ulaşılabilir?',
 [O('İktâ sahiplerinin toprağın mülkiyetini elde ettiğine','Metinde toprağın mülkiyetinin devlete ait kaldığı yazar; yargı metinle çelişir.','dikkat'),
  O('Ordunun maaşlarının tamamen hazineden ödendiğine','Metne göre komutanlar bölge gelirlerinden asker besler; maaşın tamamen hazineden ödendiği yazmaz.','dikkat'),
  O('Ordu giderlerinin bir kısmının iktâyla karşılandığına'),
  O('İktâ sisteminin Anadolu Selçuklu Devleti’nde kaldırıldığına','Metinde Anadolu Selçuklu Devleti’nden hiç söz edilmez.','dikkat'),
  O('İktâ topraklarının askerlere miras bırakıldığına','Metinde mülkiyetin devlete ait olduğu yazar; miras bırakmaya dair bir bilgi yoktur.','dikkat')],
 'C','Metinden çıkarılabilecek sonuç.',
 'İktâ sahibi vergi gelirleriyle ne yapmakla yükümlüydü?',
 [B('İktâ sistemi','Devlet bir bölgenin vergi gelirini asker komutanına bırakır · Komutan karşılığında asker besler · Toprağın mülkiyeti devlete aittir')],
 [('Sistemi özetle','Vergi geliri komutana bırakılıyor, komutan asker besliyor, mülkiyet devlette kalıyor.','gelir → komutan → asker'),('Sonucu çıkar','Asker beslemenin giderleri bölge gelirinden karşılandığına göre ordunun ihtiyacı kısmen iktâ gelirleriyle karşılanıyor.','ordu gideri ← iktâ geliri')],
 '“Gelir hakkı” ile “mülkiyet” farklıdır: iktâ sahibi yalnız geliri kullanır.','Şıklar metindeki gelir, asker ve mülkiyet bilgisiyle karşılaştırıldı.')

K.Q('0005','K-TI-05','orta','Tuğrul Bey’in Bağdat’a girişinin siyasi sonucunu çıkarır.',
 'Tuğrul Bey, 1055’te Bağdat’a girerek Büveyhoğulları’nın Abbasi halifesi üzerindeki denetimine son vermiş; halife de ona “Doğu ve Batı’nın Sultanı” unvanını vermiştir.\nBu bilgilere göre aşağıdakilerden hangisine ulaşılabilir?',
 [O('Abbasi Devleti’nin Bağdat’ta sona erdiğine','Halife unvan verdiğine göre Abbasi halifeliği sürmektedir; yargı metinle çelişir.','bilgi'),
  O('Büveyhoğulları’nın Selçukluları Bağdat’tan çıkardığına','Metinde Selçukluların Büveyhoğulları’nın denetimine son verdiği yazar; yargı tersine çevirmiştir.','dikkat'),
  O('Tuğrul Bey’in Anadolu’yu fethettiğine','Metinde Anadolu’dan söz edilmez; olay Bağdat’ta geçer.','dikkat'),
  O('Halifeliğin Selçuklu hanedanına geçtiğine','Halife Tuğrul Bey’e unvan vermiştir; halifelik Selçuklu hanedanına geçmemiştir.','bilgi'),
  O('Selçukluların İslam dünyasındaki etkisinin arttığına')],
 'E','Metinden çıkarılabilecek sonuç.',
 'Halife kimin denetiminden çıktı ve kime unvan verdi?',
 [B('Tuğrul Bey ve Bağdat (1055)','Selçuklular Bağdat’a girdi · Büveyhoğulları’nın halife üzerindeki denetimi sona erdi · Halife Tuğrul Bey’e “Doğu ve Batı’nın Sultanı” unvanını verdi')],
 [('Olayı çöz','Tuğrul Bey Bağdat’a giriyor, Büveyhoğulları’nın denetimi bitiyor, halife ona unvan veriyor.','Selçuklu ↑ · Büveyhoğulları ↓'),('Sonucu çıkar','Halifenin unvan vermesi Selçukluların İslam dünyasındaki siyasi etkisini artırır.','Selçuklu etkisi ↑')],
 'Unvan veren halife ayakta kaldığına göre halifelik bitmemiştir; Selçukluların etkisi artmıştır.','Her şık metindeki taraf ve olayla karşılaştırıldı.')

K.Q('0006','K-TI-06','orta','Medrese kurulmasından devletin eğitim politikasını çıkarır.',
 'Büyük Selçuklu veziri Nizamülmülk, Bağdat ve Nişabur gibi şehirlerde medreseler kurdurmuş; bu medreselerin öğretmen ve öğrenci giderleri vakıf gelirleriyle karşılanmıştır.\nBu bilgilere göre aşağıdakilerden hangisine ulaşılabilir?',
 [O('Devletin eğitim kurumlarını birden fazla şehirde desteklediğine'),
  O('Medreselerde yalnız fen bilimlerinin okutulduğuna','Metinde okutulan derslerden söz edilmez; “yalnız” yargısının dayanağı yoktur.','dikkat'),
  O('Medrese kurma geleneğinin Osmanlı Devleti’nde başladığına','Metin Büyük Selçuklu dönemini anlatır; Osmanlı’dan söz edilmez.','bilgi'),
  O('Eğitimin yalnızca Bağdat’ta yapıldığına','Metinde Nişabur da geçer; “yalnızca Bağdat” yargısı metinle çelişir.','dikkat'),
  O('Medrese giderlerinin öğrencilerden alınan ücretle karşılandığına','Metinde giderlerin vakıf gelirleriyle karşılandığı yazar; yargı metinle çelişir.','dikkat')],
 'A','Metinden çıkarılabilecek sonuç.',
 'Medreseler kaç şehirde, giderleri nasıl karşılanıyor?',
 [B('Nizamiye Medreseleri','Nizamülmülk’ün Bağdat, Nişabur gibi şehirlerde kurdurduğu medreseler · Giderler vakıf gelirleriyle karşılandı · Devlet adamı ve bilgin yetiştirdi')],
 [('Metindeki verileri say','Medreseler Bağdat ve Nişabur gibi birden çok şehirde; giderler vakıf gelirinden.','şehir: 2+ · gider: vakıf'),('Sonucu çıkar','Birden çok şehirde kurulup vakıfla desteklenen medreseler, eğitime verilen desteği gösterir.','çok şehir + destek')],
 'Metindeki sayıları ve gider kaynağını şıklarla tek tek karşılaştır.','Şıklar metindeki şehir ve gider bilgisiyle karşılaştırıldı.')
K.bitir()
