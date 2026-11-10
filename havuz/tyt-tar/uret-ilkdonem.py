"""TYT Tarih · İnsanlığın İlk Dönemleri (hafif mod): 4 ana soru. Metinler özgündür."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _hafif_tar_a import *
K=Konu('ilkdonem','İnsanlığın İlk Dönemleri','tar|İnsanlığın İlk Dönemleri',4)
K.zd={'kolay': 1, 'orta': 3}
K.kart('K-ID-01','Taş Devri Dönemleri','Yaşam biçiminden hangi dönemin anlatıldığını bulmak.','Paleolitik, Neolitik ve maden çağlarının özelliklerini karıştırmak.','kolay','düz',2,'id-donem','Dönemi yaşam biçiminden belirleme')
K.kart('K-ID-02','Kazı Buluntularından Çıkarım','Kazıda bulunan buluntulardan topluluğun yaşamı hakkında çıkarım yapmak.','Buluntularda olmayan bir özelliği (maden işleme gibi) çıkarılabilir sanmak.','orta','yeni nesil',3,'id-buluntu','Buluntulardan çıkarım yapma')
K.kart('K-ID-03','Tarım Devrimi ve Sonuçları','Neolitik dönemde görülen gelişmeleri öncüllerle ayırmak.','Avcı-toplayıcı dönem özelliklerini Neolitik’e, Neolitik özelliklerini Paleolitik’e yazmak.','orta','öncüllü',3,'id-neolitik','Neolitik dönem gelişmeleri')
K.kart('K-ID-04','Maden Çağları ve Ticaret','Tunç yapımı için gereken madenin ticareti nasıl etkilediğini metinden çıkarmak.','Metinde olmayan sonucu (yazı, taş aletlerin terki gibi) doğru saymak.','orta','yeni nesil',4,'id-maden','Madenlerin ticarete etkisi')

K.Q('0001','K-ID-01','kolay','Yaşam biçiminden dönemi belirler.',
 'Avcılık ve toplayıcılıkla geçinen, yiyecek bulmak için sürekli yer değiştiren, mağaralarda barınan ve ateşi ilk kez kullanmaya başlayan insanlar bu dönemde yaşamıştır.\nBu özellikler aşağıdaki dönemlerden hangisine aittir?',
 [O('Neolitik (Yeni Taş) Çağı','Neolitik’te tarım ve yerleşik hayat başlamıştır; metindeki yaşam biçimi göçebe avcılıktır.'),
  O('Kalkolitik (Bakır–Taş) Çağı','Kalkolitik’te bakır işlenmeye başlanmış ve yerleşik yaşam sürmüştür; metin göçebe yaşamı anlatır.'),
  O('Paleolitik (Eski Taş) Çağı'),
  O('Tunç Çağı','Tunç Çağı’nda madenler işlenmiş, şehirler ve ticaret gelişmiştir; metin avcı-toplayıcılığı anlatır.'),
  O('Demir Çağı','Demir Çağı, maden işlemeciliğinin geliştiği çok daha sonraki bir dönemdir; metindeki yaşam bununla uyuşmaz.')],
 'C','Metindeki yaşam biçiminin ait olduğu dönem.',
 'Yer değiştiren, avcı ve toplayıcı insan; tarım ve maden henüz yok.',
 [B('Taş Devri’nin ilk dönemi','Paleolitik (Eski Taş): avcılık, toplayıcılık, göçebe yaşam, mağara, ateşin kullanımı · Neolitik (Yeni Taş): tarım ve yerleşik hayat')],
 [('Özellikleri topla','Avcılık, toplayıcılık, yer değiştirme, mağara ve ateş metinde verilmiş.','avcı + toplayıcı + göçebe'),('Dönemi eşle','Bu yaşam biçimi Taş Devri’nin ilk dönemi Paleolitik’e aittir.','Paleolitik')],
 'Göçebe avcı-toplayıcılık Paleolitik; tarım ve yerleşik hayat Neolitik’tir.','Yaşam biçimi, her dönemin özellikleriyle karşılaştırıldı.')

K.Q('0002','K-ID-02','orta','Kazı buluntularından topluluğun yaşamı hakkında çıkarım yapar.',
 'Bir kazıda; kerpiç ev kalıntıları, ekilmiş buğday ve arpa tohumları, evcilleştirilmiş koyun ve keçi kemikleri ile ürün saklamada kullanılan çanak çömlek parçaları bulunmuştur.\nBu bilgilere göre aşağıdakilerden hangisine ulaşılamaz?',
 [O('Topluluğun yerleşik yaşama geçtiğine','Kerpiç ev kalıntıları yerleşik yaşamı gösterir; bu yargıya ulaşılır, soru ulaşılamayanı ister.','dikkat'),
  O('Tarım faaliyetinde bulunulduğuna','Ekilmiş buğday ve arpa tohumları tarımı gösterir; bu yargıya ulaşılır.','dikkat'),
  O('Hayvanların evcilleştirildiğine','Evcilleştirilmiş koyun ve keçi kemikleri bulunmuştur; bu yargıya ulaşılır.','dikkat'),
  O('Ürünlerin kaplarda saklandığına','Ürün saklamada kullanılan çanak çömlek parçaları bulunmuştur; bu yargıya ulaşılır.','dikkat'),
  O('Maden işlenip alet yapıldığına')],
 'E','Buluntulardan çıkarılamayan yargı.',
 'Buluntu listesinde maden ya da maden alet var mı?',
 [B('Neolitik dönem','Tarım ve hayvancılık, yerleşik hayat, köy, çanak çömlek · Maden işleme sonraki dönemlerde (Kalkolitik ve maden çağları) görülür')],
 [('Kök “ulaşılamaz” diyor','Metinden çıkmayan tek yargıyı arıyoruz.','aranan: çıkmayan yargı'),('Buluntuları yargılarla eşle','Ev yerleşikliği, tohum tarımı, kemik hayvancılığı, çömlek saklamayı gösterir; maden buluntusu yok.','ev · tohum · kemik · çömlek')],
 'Metinde maden ya da maden alet bulunmadığı için madenin işlendiğine ulaşılamaz.',
 'Her yargının metinde bir buluntu dayanağı var mı diye kontrol et.','Dört yargının buluntu dayanağı var; maden işleme için yok.')

stm=[('Yerleşik hayata geçilmesi',True,'tarımla birlikte yerleşik hayat başladı'),
     ('Kalıcı köylerin kurulması',True,'ilk köyler bu dönemde kuruldu'),
     ('Avcılık ve toplayıcılığın tek geçim kaynağı olarak sürmesi',False,'tarım ve hayvancılık geçim kaynağı oldu'),
     ('Artan ürünlerin takasa konu olması',True,'artı ürün takasa yol açtı')]
op,isl=oncul(stm,['I ve II','I, II ve IV','I, III ve IV','II, III ve IV','I, II, III ve IV'],'B')
K.Q('0003','K-ID-03','orta','Neolitik dönemde görülen gelişmeleri ayırt eder.',metin_oncul(stm,'Yukarıdakilerden hangileri Neolitik (Yeni Taş) Çağı’nda görülen gelişmelerdendir?'),
 op,'B','Neolitik Çağ’ın gelişmeleri.',
 'Neolitik’in anahtar sözcüğü tarımdır; tarımın sonuçlarını düşün.',
 [B('Neolitik Çağ’ın özellikleri','Tarım ve hayvancılık başladı · Yerleşik hayat, köyler · Çanak çömlek, dokuma · Artı ürün ve takas')],
 [('Anahtar olayı bul','Neolitik Çağ’da insan tarıma geçmiştir.','tarım = Neolitik'),('Sonuçlarını say','Tarım yerleşik hayatı, köyleri ve artı ürünü doğurur; yalnız avcılık sürmez.','I, II, IV doğru')],
 'Tarım devrimi yerleşik hayatı ve köyleri getirdi; avcılık-toplayıcılık tek geçim kaynağı olmaktan çıktı.',
 'Her öncül tarım devriminin bir sonucu mu diye kontrol edildi.',islem_son=isl)

K.Q('0004','K-ID-04','orta','Tunç yapımında gereken madenin ticarete etkisini çıkarır.',
 'Tunç, bakır ile kalayın karıştırılmasıyla elde edilen bir alaşımdır. Kalay yatakları yalnızca belirli bölgelerde bulunduğundan, tunç yapmak isteyen topluluklar bu madeni başka bölgelerden getirmek zorunda kalmıştır.\nBu bilgilere göre aşağıdakilerden hangisine ulaşılabilir?',
 [O('Madenlerin taşınmasının ticareti geliştirdiğine'),
  O('Kalay yataklarının bakırdan daha yaygın olduğuna','Metne göre kalay yatakları yalnız belirli bölgelerdedir; bu, kalayın yaygın olduğunu değil sınırlı olduğunu gösterir.','bilgi'),
  O('Yazının tunç alaşımıyla birlikte icat edildiğine','Metinde yazıdan hiç söz edilmez; dayanağı olmayan bir yargıdır.','dikkat'),
  O('Tunç Çağı’nda taş aletlerin tamamen terk edildiğine','Metinde taş aletlerden söz edilmez; “tamamen terk” yargısının dayanağı yoktur.','dikkat'),
  O('Tarım faaliyetlerinin Tunç Çağı’nda başladığına','Metinde tarımdan söz edilmez; üstelik tarım Neolitik Çağ’da başlamıştır.','bilgi')],
 'A','Metinden çıkarılabilecek sonuç.',
 'Kalay her yerde yoksa, olan yerden olmayan yere ne olur?',
 [B('Tunç Çağı','Tunç = bakır + kalay · Madenler işlendikçe bölgeler arası ticaret gelişti · Tarım Neolitik Çağ’da başlamıştı')],
 [('Metindeki nedeni bul','Kalay yalnız belirli bölgelerde bulunuyor.','kalay: sınırlı bölgeler'),('Sonucu çıkar','Kalayı olmayan topluluklar onu başka bölgelerden getiriyor; bu, madenin taşınması ve ticaret demektir.','kalay getirilir → ticaret')],
 'Kaynağı sınırlı bir hammadde, bölgeler arası ticareti canlandırır.',
 'Metindeki neden-sonuç zinciri takip edildi; metinde olmayan yargılar elendi.')
K.bitir()
