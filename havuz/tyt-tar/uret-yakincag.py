import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _hafif_tar_b import *
Q=KonuT('yakincag','Yakın Çağ Avrupa Tarihi','tar|Yakın Çağ Avrupa Tarihi',4)
Q.zd={'kolay': 2, 'orta': 2}
Q.kart('K-YKC-01','İnsan ve Yurttaş Hakları Bildirgesi','1789’da Fransa’da ilan edilen bildirgede insanların özgür ve eşit doğduğu, egemenliğin ulusa ait olduğu belirtilmiştir.','Egemenliğin kralda kaldığını sanmak.','kolay','yeni nesil',2,'ykc-bildirge','İnsan ve Yurttaş Hakları Bildirgesi')
Q.kart('K-YKC-02','Kıta Ablukası','Napolyon 1806’da İngiltere’yi ekonomik olarak zayıflatmak için Kıta Ablukası’nı ilan etmiş; ablukaya uymayan Rusya’ya yönelen 1812 seferi başarısız olmuştur.','Ablukayı İngiltere’nin uyguladığını sanmak.','orta','yeni nesil',3,'ykc-abluka','Kıta Ablukası ve Rusya seferi')
Q.kart('K-YKC-03','Viyana Kongresi','1814–1815’te toplanmış; ihtilalin milliyetçilik ve özgürlük fikirlerini engellemek, Avrupa’da güç dengesini kurmak amaçlanmıştır.','Almanya birliğini Viyana’ya bağlamak.','orta','öncüllü',3,'ykc-viyana','Viyana Kongresi’nin özellikleri')
Q.kart('K-YKC-04','Almanya’nın siyasi birliği','Bismarck önderliğindeki Prusya, Danimarka, Avusturya ve Fransa ile savaşarak 1871’de birliği sağlamıştır.','Birliğin barışla kurulduğunu sanmak.','kolay','yeni nesil',4,'ykc-almanya','Almanya’nın siyasi birliği')
# 0001 B
Q.Y('0001','K-YKC-01','kolay','İnsan ve Yurttaş Hakları Bildirgesi’nin ilkelerini yorumlar.',
 '1789’da Fransa’da ilan edilen bildirgede insanların özgür ve eşit doğduğu, egemenliğin kaynağının ulus olduğu belirtilmiştir.\nBu parçaya göre bildirge ile ilgili aşağıdakilerden hangisine ulaşılabilir?',
 'Egemenliğin kaynağı olarak ulus esas alınmıştır.',
 [('Egemenliğin kralın elinde kalacağı ilan edilmiştir.','Parçada egemenliğin kaynağının ulus olduğu yazar.','dikkat'),
  ('İnsanların doğuştan eşit olmadığı kabul edilmiştir.','Parçada insanların özgür ve eşit doğduğu belirtilir.','dikkat'),
  ('Bildirge 1789 yılından önce yayımlanmıştır.','Parçada bildirgenin 1789’da ilan edildiği yazar.','bilgi'),
  ('Haklar yalnızca soylulara tanınmıştır.','Parçada insanların eşit doğduğu belirtilir; soylulara ayrıcalık yazmaz.','dikkat')],'B',
 'Parçadan çıkarılabilecek yargının belirlenmesi.','Egemenliğin kaynağının kim olduğuna ve insanların nasıl doğduğuna bak.',
 [('İnsan ve Yurttaş Hakları Bildirgesi (1789)','Fransız İhtilali sırasında ilan edildi · İnsanlar özgür ve eşit doğar · Egemenliğin kaynağı ulustur.')],
 'Parçada iki ilke (eşitlik–özgürlük ve ulus egemenliği) verilmiş.','Özgür–eşit doğma · egemenlik ulusta','Ulus egemenliği yargısı parçayla uyuşur.','Fransız İhtilali’nin bildirgesi ulus egemenliğini ve eşitliği öne çıkarır.','Parçadaki cümleyi şıkla birebir karşılaştır; zıt anlamlı şıkları ele.','Özgün metin; MEB Fransız İhtilali')
# 0002 D
Q.Y('0002','K-YKC-02','orta','Kıta Ablukası’nın amacını ve sonucunu yorumlar.',
 'Napolyon, İngiltere’yi ekonomik olarak zayıflatmak amacıyla 1806’da Kıta Ablukası’nı ilan etmiş ve Avrupa limanlarının İngiliz mallarına kapatılmasını istemiştir. Ablukaya uymayan Rusya üzerine 1812’de sefere çıkan Fransız ordusu ağır kayıplar vermiştir.\nBu parçaya göre aşağıdakilerden hangisi söylenebilir?',
 'Ablukaya uymayan bir devlete karşı sefer düzenlenmiştir.',
 [('Abluka, İngiltere tarafından Fransa’ya karşı uygulanmıştır.','Parçada ablukayı Napolyon’un ilan ettiği yazar.','dikkat'),
  ('Rusya, ablukaya en sıkı biçimde uymuştur.','Parçada Rusya’nın ablukaya uymadığı belirtilir.','dikkat'),
  ('1812 seferi Fransa için kayıpsız sonuçlanmıştır.','Parçada ordunun ağır kayıp verdiği yazar.','dikkat'),
  ('Abluka, Avrupa limanlarını İngiliz mallarına açmayı amaçlamıştır.','Parçada limanların İngiliz mallarına kapatılmasının istendiği belirtilir.','dikkat')],'D',
 'Parçadan çıkarılabilecek yargının belirlenmesi.','Ablukayı kimin, kime karşı uyguladığına ve Rusya’nın tutumuna bak.',
 [('Kıta Ablukası (1806)','Napolyon, İngiltere’nin ticaretini zayıflatmak için ilan etti · Avrupa limanları İngiliz mallarına kapatıldı · Ablukaya uymayan Rusya’ya 1812’de sefer düzenlendi.')],
 'Parçada ablukayı ilan eden, amaç, karşı çıkan devlet ve sonuç verilmiş.','Napolyon → İngiltere · Rusya uymadı · 1812 sefer','Ablukaya uymayan Rusya’ya sefer düzenlendiği parçada yazılıdır.','Kıta Ablukası Napolyon’un İngiltere’ye karşı kullandığı ekonomik silahtır.','Eylemi yapanı ve eylemin hedefini şıklarda ters çevirmiş olabilirler; dikkat et.','Özgün metin; MEB Napolyon')
# 0003 C oncul
st=[('1814–1815 yıllarında toplanmıştır.',True,'Viyana Kongresi 1814–1815’te toplanmıştır'),
    ('Fransız İhtilali’nin yaydığı milliyetçilik ve özgürlük fikirlerinin yayılmasını engellemek amaçlanmıştır.',True,'kongre ihtilal fikirlerine karşı alınan önlemlerin merkezidir'),
    ('Almanya’nın siyasi birliği bu kongrede sağlanmıştır.',False,'Almanya’nın birliği 1871’de Prusya önderliğinde sağlanmıştır'),
    ('Avrupa’da güç dengesinin sağlanması hedeflenmiştir.',True,'kongrenin ilkelerinden biri devletler arasında güç dengesidir')]
op,dg=oncul(st,['Yalnız I','I ve II','I, II ve IV','II, III ve IV','I, III ve IV'],'C'); assert dg=={'I','II','IV'}
Q.Y2('0003','K-YKC-03','orta','Viyana Kongresi’nin amaç ve özelliklerini belirler.',
 metin_oncul('Viyana Kongresi ile ilgili şu bilgiler verilmiştir:',st,'Bu bilgilerden hangileri doğrudur?'),op,'C',
 'Doğru öncüllerin belirlenmesi.','Kongrenin tarihini ve amacını düşün; Almanya’nın birliğinin tarihini hatırla.',
 [('Viyana Kongresi','1814–1815 · Fransız İhtilali’nin milliyetçilik ve özgürlük fikirlerini engellemek, Avrupa’da güç dengesi sağlamak amaçlandı · Almanya’nın birliği 1871’de kuruldu.')],
 'Her öncülü kongrenin tarihi ve amacıyla karşılaştır.','I, II, IV doğru · III yanlış','I, II ve IV doğrudur.','Kongre ihtilale karşı eski düzeni ve güç dengesini kurmayı amaçlamıştır.','Birlikler (Almanya, İtalya) 1860–1871 arasında kurulmuştur; Viyana’dan çok sonradır.','Dört öncül, üç doğru')
# 0004 E ulaşılamaz
Q.Y('0004','K-YKC-04','kolay','Almanya’nın siyasi birliğinin nasıl sağlandığını çıkarım yoluyla değerlendirir.',
 'Almanya’da siyasi birliğin sağlanması sürecinde Prusya başbakanı Bismarck, Danimarka, Avusturya ve Fransa ile yapılan savaşlarla Alman devletlerini Prusya çevresinde toplamıştır. 1871’de Fransa’nın yenilmesinin ardından Versay Sarayı’nda Alman İmparatorluğu ilan edilmiştir.\nBu parçadaki bilgilere göre aşağıdakilerden hangisine ulaşılamaz?',
 'Danimarka, birleşme sürecinde Prusya’nın müttefiki olmuştur.',
 [('Siyasi birliğin sağlanmasında savaşlar rol oynamıştır.','Parçada birliğin Danimarka, Avusturya ve Fransa ile savaşlarla sağlandığı yazar; yargıya ulaşılabilir.','dikkat'),
  ('Prusya, birleşme sürecinin merkezinde yer almıştır.','Parçada Alman devletlerinin Prusya çevresinde toplandığı belirtilir; yargıya ulaşılabilir.','dikkat'),
  ('Alman İmparatorluğu, Fransa’nın yenilgisinden sonra ilan edilmiştir.','Parçada imparatorluğun 1871’de Fransa’nın yenilmesinin ardından ilan edildiği yazar; yargıya ulaşılabilir.','dikkat'),
  ('Birleşme sürecinde Bismarck önemli bir rol oynamıştır.','Parçada birleşmeyi yürüten kişinin Bismarck olduğu belirtilir; yargıya ulaşılabilir.','dikkat')],'E',
 'Parçadan çıkarılamayan yargının belirlenmesi.','Kök “ulaşılamaz” diyor: dört yargı parçada var, biri parçayla çelişiyor.',
 [('Almanya’nın birliği','Bismarck önderliğinde Prusya, Danimarka (1864), Avusturya (1866) ve Fransa (1870–71) ile savaştı · 1871’de Versay’da Alman İmparatorluğu ilan edildi.')],
 'Kökte “ulaşılamaz” var; dört şık parçadan çıkarılabilir.','Parçada Danimarka ile savaşıldığı yazdığı için Danimarka’nın Prusya’nın müttefiki olduğu yargısına ulaşılamaz.','Savaşlar: Danimarka, Avusturya, Fransa · Danimarka müttefik değil, savaşılan taraf','Parçadaki eylemleri (savaş, ilan) ve tarafları şıklardaki yargılarla tek tek karşılaştır.','Olumsuz kökte şıkları parçadaki ayrıntılarla tek tek karşılaştır.','Özgün metin; MEB Almanya birliği')
Q.bitir()
