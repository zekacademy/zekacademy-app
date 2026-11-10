"""TYT Tarih · Yerleşme ve Devletleşme Sürecinde Selçuklu Türkiyesi (hafif mod): 4 ana soru. Metinler özgündür."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _hafif_tar_a import *
K=Konu('selcuklu','Yerleşme ve Devletleşme Sürecinde Selçuklu Türkiyesi','tar|Yerleşme ve Devletleşme Sürecinde Selçuklu Türkiyesi',4)
K.zd={'kolay': 1, 'orta': 3}
K.kart('K-SL-01','Anadolu Beylikleri','Beyliğin merkezinden hangi beylik olduğunu bulmak.','Saltuklu, Mengücek, Danişmend ve Artuklu merkezlerini karıştırmak.','kolay','düz',2,'sl-beylik','Beyliği merkezinden tanıma')
K.kart('K-SL-02','Miryokefalon','Miryokefalon sonrası Bizans’ın durumundan Türk egemenliğine dair çıkarım yapmak.','Metinde olmayan sonucu (Bizans’ın tamamen çekilmesi gibi) doğru saymak.','orta','yeni nesil',3,'sl-miryo','Miryokefalon’un sonucu')
K.kart('K-SL-03','Olayların Sırası','Anadolu Selçuklu olaylarının Kösedağ’a göre sırasını bulmak.','Moğol egemenliğini Kösedağ’dan önce sanmak.','orta','öncüllü',3,'sl-sira','Kösedağ’a göre sıralama')
K.kart('K-SL-04','Beyliklerin Dağılımı','Beylikler metninden tek merkezden yönetim yargısının çıkarılamayacağını görmek.','Beylikleri tek bir devlete bağlı sanmak.','orta','yeni nesil',4,'sl-dagilim','Beyliklerin yayılışı')

K.Q('0001','K-SL-01','kolay','Beyliği merkezinden tanır.',
 'Malazgirt Savaşı’ndan sonra Anadolu’da kurulan Türk beyliklerinden biri, merkezi Erzurum olan beyliktir.\nBu beylik aşağıdakilerden hangisidir?',
 [O('Mengücekler','Mengücekler Erzincan, Kemah ve Divriği çevresinde kurulmuştur; merkezleri Erzurum değildir.'),
  O('Saltuklular'),
  O('Artuklular','Artuklular Hasankeyf, Mardin ve Diyarbakır çevresinde hüküm sürmüştür; merkezleri Erzurum değildir.'),
  O('Danişmendliler','Danişmendliler Sivas, Tokat ve Malatya çevresinde kurulmuştur; merkezleri Erzurum değildir.'),
  O('Çaka Beyliği','Çaka Bey İzmir çevresinde batıda bir beylik kurmuştur; Erzurum’da değil.')],
 'B','Merkezi Erzurum olan beylik.',
 'Erzurum doğu Anadolu’dadır; hangi beylik orada kuruldu?',
 [B('Anadolu’daki ilk beylikler','Saltuklular: Erzurum · Mengücekler: Erzincan, Divriği · Danişmendliler: Sivas, Tokat, Malatya · Artuklular: Hasankeyf, Mardin, Diyarbakır · Çaka Beyliği: İzmir')],
 [('Merkezi not et','Soruda aranan beyliğin merkezi Erzurum.','merkez: Erzurum'),('Beyliği eşle','Erzurum çevresindeki beylik Saltuklulardır; diğerlerinin merkezleri başka yerlerdedir.','Erzurum = Saltuklular')],
 'Beylik adını merkez şehirle birlikte öğren.','Her beylik merkeziyle eşleştirildi.')

K.Q('0002','K-SL-02','orta','Miryokefalon Savaşı’nın sonucunu metinden çıkarır.',
 '1176’da Miryokefalon’da Bizans İmparatoru I. Manuel Komnenos’un ordusu, II. Kılıçarslan komutasındaki Anadolu Selçuklu ordusu karşısında ağır bir yenilgiye uğramıştır. Bu savaştan sonra Bizans, Anadolu’ya yeniden büyük çaplı bir sefer düzenleyememiştir.\nBu bilgilere göre aşağıdakilerden hangisine ulaşılabilir?',
 [O('Bizans’ın Türkleri Anadolu’dan geri attığına','Bizans savaşı kaybetmiştir ve yeniden büyük sefer düzenleyememiştir; yargı sonucu tersine çevirmiştir.','dikkat'),
  O('Anadolu Selçuklu Devleti’nin yıkıldığına','Metinde Selçukluların galip geldiği yazar; yıkılışından söz edilmez.','dikkat'),
  O('Savaşın Malazgirt’ten önce yapıldığına','Metindeki tarih 1176’dır; Malazgirt Savaşı 1071’dedir ve daha eskidir.','bilgi'),
  O('Bizans’ın Anadolu’dan tamamen çekildiğine','Metin yalnızca büyük çaplı yeni sefer düzenlenemediğini söyler; tamamen çekilme bilgisi yoktur.','dikkat'),
  O('Anadolu’daki Türk egemenliğinin güç kazandığına')],
 'E','Metinden çıkarılabilecek sonuç.',
 'Savaşı kim kazandı, kaybeden taraf sonra ne yapamadı?',
 [B('Miryokefalon Savaşı (1176)','II. Kılıçarslan, Bizans İmparatoru I. Manuel Komnenos’u yendi · Bizans’ın Anadolu’yu geri alma gücü azaldı · Anadolu’daki Türk egemenliği güçlendi')],
 [('Savaşın sonucunu bul','Anadolu Selçuklu ordusu kazanmış, Bizans ordusu ağır yenilmiş.','kazanan: Selçuklu'),('Sonucu çıkar','Bizans yeniden büyük sefer düzenleyemediğine göre Türk egemenliği Anadolu’da güçlenmiştir.','Bizans ↓ · Türk egemenliği ↑')],
 'Savaşın kazananını ve sonradan olanı metinden doğru oku.','Her şık metindeki sonuçla karşılaştırıldı.')

stm=[('Miryokefalon Savaşı’nın yapılması',True,'1176’da yapıldı'),
     ('Babai İsyanı’nın çıkması',True,'1240’ta çıktı'),
     ('Anadolu Selçuklu Devleti’nin Moğollara vergi vermeye başlaması',False,'Kösedağ’dan sonra gerçekleşti')]
op,isl=oncul(stm,['Yalnız I','Yalnız III','I ve II','II ve III','I, II ve III'],'C')
K.Q('0003','K-SL-03','orta','Anadolu Selçuklu olaylarını Kösedağ’a göre sıralar.',metin_oncul(stm,'Yukarıdaki gelişmelerden hangileri Kösedağ Savaşı’ndan (1243) önce gerçekleşmiştir?'),
 op,'C','Kösedağ’dan önceki gelişmeler.',
 'Moğol egemenliği Kösedağ’ın sonucudur.',
 [B('Anadolu Selçuklu dönemi tarihleri','Miryokefalon: 1176 · Babai İsyanı: 1240 · Kösedağ Savaşı: 1243 (Moğollara yenilgi, ardından Moğol egemenliği)')],
 [('Ölçütü koy','Ölçüt Kösedağ Savaşı (1243); öncesindeki olayları arıyoruz.','ölçüt: 1243'),('Öncülleri tarihle','Miryokefalon 1176, Babai İsyanı 1240; Moğollara vergi Kösedağ’dan sonra.','I: 1176 · II: 1240 · III: 1243 sonrası')],
 'Moğol egemenliği ve vergi, Kösedağ yenilgisinin sonucudur; savaştan önce olamaz.','Her olay 1243 ile karşılaştırıldı.',islem_son=isl)

K.Q('0004','K-SL-04','orta','Anadolu beyliklerinin dağılımını anlatan metinden çıkarılamayan yargıyı bulur.',
 'Malazgirt’in ardından Anadolu’ya yerleşen Türkmen beyleri, fethettikleri bölgelerde yönetim kurmuştur. Erzurum çevresinde Saltuklular, Erzincan ve Divriği çevresinde Mengücekler, Sivas–Tokat–Malatya çevresinde Danişmendliler, güneydoğuda Artuklular bu beyliklerdendir.\nBu bilgilere göre aşağıdakilerden hangisine ulaşılamaz?',
 [O('Beyliklerin Anadolu’nun farklı bölgelerinde kurulduğuna','Metinde beyliklerin Erzurum, Erzincan, Sivas ve güneydoğuda kurulduğu yazar; bu yargıya ulaşılır.','dikkat'),
  O('Türkmen beylerinin fethettikleri yerlerde yönetim kurduğuna','Metin bunu açıkça söyler; bu yargıya ulaşılır, soru ulaşılamayanı ister.','dikkat'),
  O('Türklerin Anadolu’ya yerleşmesinin Malazgirt’in ardından hız kazandığına','Metindeki “Malazgirt’in ardından” ifadesi bunu gösterir; bu yargıya ulaşılır.','dikkat'),
  O('Anadolu’daki beyliklerin tek merkezden yönetildiğine'),
  O('Doğu Anadolu’da birden fazla beyliğin bulunduğuna','Saltuklu ve Mengücek beylikleri doğuda yer alır; bu yargıya ulaşılır.','dikkat')],
 'D','Metinden çıkarılamayan yargı.',
 'Her beylik kendi bölgesinde mi, yoksa tek merkeze bağlı mı anlatılıyor?',
 [B('Malazgirt sonrası beylikler','Saltuklular: Erzurum · Mengücekler: Erzincan, Divriği · Danişmendliler: Sivas, Tokat, Malatya · Artuklular: güneydoğu Anadolu · Her beylik kendi bölgesinde yönetim kurdu')],
 [('Kök “ulaşılamaz” diyor','Metinden çıkmayan yargıyı arıyoruz.','aranan: çıkmayan'),('Beylikleri bölgeleriyle oku','Beylikler farklı bölgelerde, her biri kendi yönetimiyle anlatılıyor; tek merkezden söz yok.','beylikler: ayrı bölge, ayrı yönetim')],
 'Beylikler farklı bölgelerde kendi yönetimlerini kurduğu için tek merkezden yönetildikleri söylenemez.','Dört yargı metinden çıkar; tek merkez yargısı çıkmaz.')
K.bitir()
