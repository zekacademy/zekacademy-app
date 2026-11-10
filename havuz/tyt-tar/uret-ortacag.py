"""TYT Tarih · Ortaçağ’da Dünya (hafif mod): 4 ana soru. Metinler özgündür."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _hafif_tar_a import *
K=Konu('ortacag','Ortaçağ’da Dünya','tar|Ortaçağ’da Dünya',4)
K.kart('K-OD-01','Feodal Toplum Yapısı','Feodal düzende toplum sınıflarını tanımlarından bulmak.','Serf, vassal, senyör ve şövalyeyi birbirine karıştırmak.','kolay','düz',2,'od-feodal','Feodal sınıfları tanıma')
K.kart('K-OD-02','Feodal Düzenden Çıkarım','Feodal düzeni anlatan metinden çıkarılamayan yargıyı bulmak.','Metinde olmayan şehir ve tüccar rolünü feodal düzene yazmak.','orta','yeni nesil',3,'od-cikarim','Feodal düzen metninden çıkarım')
K.kart('K-OD-03','Olayların Zamanı','Orta Çağ olaylarının Katolik–Ortodoks ayrılığına göre sırasını bulmak.','Haçlı Seferleri ve Magna Carta gibi sonraki olayları ayrılıktan önce sanmak.','orta','öncüllü',3,'od-sira','Olayların sıralanması')
K.kart('K-OD-04','Haçlı Seferleri ve Ticaret','Haçlı Seferleri sonrası ticaret ve şehir gelişiminin sonucunu metinden çıkarmak.','Metinde olmayan kalıcı egemenlik ya da feodalitenin bitişi gibi sonuçları doğru saymak.','zor','yeni nesil',4,'od-hacli','Haçlı Seferleri’nin sonuçları')

K.Q('0001','K-OD-01','kolay','Feodal düzende toplum sınıflarını tanımlarından ayırt eder.',
 'Orta Çağ Avrupa’sındaki feodal düzende senyöre ait topraklarda çalışan, toprağı terk edemeyen ve ürünün bir bölümünü senyöre vermek zorunda olan köylülere ne ad verilir?',
 [O('Vassal','Vassal, senyörden toprak alıp ona askerî hizmet ve sadakat sunan soyludur; toprakta çalışan köylü değildir.'),
  O('Şövalye','Şövalye, zırhlı atlı savaşçı sınıftır; toprağa bağlı köylü değildir.'),
  O('Burjuva','Burjuva, şehirlerde yaşayan tüccar ve zanaatkârlara denir; köylü değildir.'),
  O('Serf'),
  O('Senyör','Senyör, toprağın sahibi olan soylu beydir; toprakta çalışan köylünün efendisidir.')],
 'D','Toprağa bağlı köylülerin adı.',
 'Toprağı terk edemeyen köylü, toprak sahibi mi yoksa onun çalıştırdığı kişi mi?',
 [B('Feodal toplum','Senyör: toprak sahibi soylu · Vassal: senyöre askerî hizmet sunan soylu · Şövalye: atlı savaşçı · Serf: toprağa bağlı köylü')],
 [('Tanımı oku','Soruda toprakta çalışan ve toprağı terk edemeyen köylüden söz ediliyor.','toprakta çalışan, bağlı köylü'),('Sınıfı hatırla','Feodal düzende bu köylülere serf denir.','serf = toprağa bağlı köylü')],
 'Serf toprağa bağlı köylü, senyör toprak sahibi, vassal ise ona hizmet eden soyludur.','Her sınıf tanımıyla karşılaştırıldı.')

K.Q('0002','K-OD-02','orta','Feodal düzeni anlatan metinden çıkarılamayan yargıyı belirler.',
 'Orta Çağ Avrupa’sında senyörler topraklarının bir bölümünü vassallara vermiş, vassallar karşılığında senyöre askerî hizmet ve sadakat sunmuştur. Topraklarda çalışan serfler ise toprağa bağlı yaşamış, ürünün bir bölümünü senyöre vermiştir.\nBu bilgilere göre aşağıdakilerden hangisine ulaşılamaz?',
 [O('Şehirlerde yaşayan tüccarların yönetimde belirleyici olduğuna'),
  O('Ekonominin ağırlıklı olarak toprağa dayandığına','Metindeki ilişkilerin hepsi toprak üzerine kuruludur; bu yargıya ulaşılır, soru ulaşılamayanı ister.','dikkat'),
  O('Toplumun farklı sosyal sınıflardan oluştuğuna','Senyör, vassal ve serf farklı sınıflardır; bu yargıya ulaşılır.','dikkat'),
  O('Serflerin toprağı terk etmekte serbest olmadığına','Metinde serflerin toprağa bağlı yaşadığı yazıyor; bu yargıya ulaşılır.','dikkat'),
  O('Askerî hizmete dayalı karşılıklı bağlılık ilişkilerinin bulunduğuna','Vassalın askerî hizmet ve sadakat sunması bunu gösterir; bu yargıya ulaşılır.','dikkat')],
 'A','Metinden çıkarılamayan yargı.',
 'Metinde şehir ve tüccardan söz ediliyor mu?',
 [B('Feodalite','Toprak karşılığında askerî hizmet ve sadakat · Senyör, vassal, serf · Ekonomi tarıma dayalı · Şehirler ve burjuva sınıfı feodal düzenin dışında gelişti')],
 [('Kök “ulaşılamaz” diyor','Metinden çıkmayan yargıyı arıyoruz.','aranan: çıkmayan'),('Metni yargılarla karşılaştır','Metin toprak, hizmet ve sınıfları anlatır; şehir ve tüccardan hiç söz etmez.','şehir/tüccar: metinde yok')],
 'Tüccarların yönetimdeki belirleyiciliği metinde geçmediği için ulaşılamaz.','“Ulaşılamaz” köklerinde metinde dayanağı olmayan şıkkı bul.','Dört yargı metinden çıkar; tüccarların rolü çıkmaz.')

stm=[('Batı Roma İmparatorluğu’nun yıkılması',True,'476’da yıkıldı'),
     ('Şarlman’ın (Charlemagne) Papa tarafından imparator ilan edilmesi',True,'800’de oldu'),
     ('Haçlı Seferleri’nin başlaması',False,'1096’da başladı'),
     ('Magna Carta’nın imzalanması',False,'1215’te imzalandı')]
op,isl=oncul(stm,['Yalnız I','Yalnız IV','I ve II','III ve IV','I, II ve III'],'C')
K.Q('0003','K-OD-03','orta','Orta Çağ olaylarını Katolik–Ortodoks ayrılığına göre sıralar.',metin_oncul(stm,'Yukarıdaki gelişmelerden hangileri Hristiyan kilisesinin Katolik ve Ortodoks olarak ikiye ayrılmasından (1054) önce gerçekleşmiştir?'),
 op,'C','1054’ten önceki gelişmeler.',
 'Haçlı Seferleri 11. yüzyılın sonunda başladı.',
 [B('Orta Çağ’dan tarihler','Batı Roma’nın yıkılışı: 476 · Şarlman’ın imparatorluğu: 800 · Katolik–Ortodoks ayrılığı: 1054 · Haçlı Seferleri’nin başlangıcı: 1096 · Magna Carta: 1215')],
 [('Ölçütü koy','Ölçüt yılı 1054; bu yıldan önceki olayları arıyoruz.','ölçüt: 1054'),('Öncülleri tarihle','Batı Roma 476, Şarlman 800; Haçlı Seferleri 1096, Magna Carta 1215.','I: 476 · II: 800 · III: 1096 · IV: 1215')],
 'I ve II, 1054’ten öncedir; III ve IV sonradır.','Her olayın yılı 1054 ile karşılaştırıldı.',islem_son=isl)

K.Q('0004','K-OD-04','zor','Haçlı Seferleri’nin ticaret ve şehirler üzerindeki sonucunu metinden çıkarır.',
 'Haçlı Seferleri sırasında Avrupalılar Doğu Akdeniz limanlarıyla ve Doğu pazarlarıyla yakın temas kurmuş; Doğu’dan getirilen baharat ve ipek Avrupa’da büyük talep görmüştür. Akdeniz kıyısındaki şehirlerde tüccarlar zenginleşmiş, bazı şehirler senyörlere vergi ödeyerek yönetimde özerklik elde etmiştir.\nBu bilgilere göre aşağıdakilerden hangisine ulaşılabilir?',
 [O('Haçlı Seferleri’nin Doğu’da kalıcı Avrupa egemenliği kurduğuna','Metinde Doğu’da kalıcı egemenlikten söz edilmez; dayanağı olmayan bir yargıdır.','dikkat'),
  O('Senyörlerin şehirler üzerindeki etkisinin zayıflamaya başladığına'),
  O('Feodal düzenin Haçlı Seferleri’nden önce sona erdiğine','Metin seferler sırasında ve sonrasında senyör–şehir ilişkisinden söz eder; düzenin daha önce bittiği bilgisi yoktur.','dikkat'),
  O('Ticaretin seferlerden önce de aynı canlılıkta olduğuna','Metin, seferlerle birlikte Doğu ürünlerine talebin arttığını anlatır; bu yargı metinle çelişir.','bilgi'),
  O('Köylülerin tamamının serflikten kurtulduğuna','Metin şehirlerden söz eder, köylülerin durumundan değil; “tamamı” yargısının dayanağı yoktur.','dikkat')],
 'B','Metinden çıkarılabilecek sonuç.',
 'Şehirler senyöre vergi ödeyip özerklik alırsa senyörün şehirdeki gücü ne olur?',
 [B('Haçlı Seferleri’nin sonuçları','Akdeniz ticareti canlandı · Şehirler ve burjuva sınıfı güçlendi · Feodal beylerin gücü zayıfladı · Doğu’nun bilim ve teknikleri Avrupa’ya aktarıldı')],
 [('Gelişmeleri sırala','Doğu ürünlerine talep arttı, tüccarlar zenginleşti, şehirler özerklik aldı.','talep ↑ → tüccar ↑ → şehir özerkliği'),('Sonucu çıkar','Şehirler senyöre vergi verip özerklik kazandıysa senyörün şehir üzerindeki yetkisi azalmıştır.','senyör etkisi ↓')],
 'Zincirin sonunda senyörün şehirlerdeki etkisinin azaldığı görülür.','Metindeki neden-sonuç zinciri sonuna kadar izlendi.')
K.bitir()
