"""TYT Tarih · I. Dünya Savaşı: 4 ana soru (hafif mod)."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _hafif_tar_c import *
KY='ÖSYM 2018–2026 TYT Tarih (I. Dünya Savaşı, Osmanlı cepheleri) · MEB 11. sınıf tarih'
KARTLAR={
 'K-DSV-01':dict(alt='Osmanlı’nın savaşa girişi',fikir='Osmanlı Devleti’nin savaşa fiilen girmesini sağlayan olayı, ondan önce ve sonra olanlardan ayırmak.',tuzak='Almanya ile ittifakı savaşa giriş sanmak.',zorluk='kolay',kalip='düz',adim=2,tipId='tar-dsv-giris',kaynak=KY),
 'K-DSV-02':dict(alt='Çanakkale Cephesi',fikir='Metindeki olay sırasını (önce deniz, sonra kara harekâtı) okuyup uygun yargıyı seçmek.',tuzak='Metinde olmayan sonucu ya da sırayı tersine çevirmek.',zorluk='orta',kalip='düz',adim=3,tipId='tar-dsv-canakkale',kaynak=KY),
 'K-DSV-03':dict(alt='Osmanlı’nın savaştığı cepheler',fikir='Osmanlı Devleti’nin savaştığı ve savaşmadığı cepheleri ayırmak.',tuzak='Büyük savaşın her cephesini Osmanlı cephesi sanmak.',zorluk='orta',kalip='öncüllü',adim=3,tipId='tar-dsv-cephe',kaynak=KY),
 'K-DSV-04':dict(alt='Rusya’nın savaştan çekilmesi',fikir='Metindeki neden–sonuç bağını kurarak çıkarım yapmak.',tuzak='Antlaşmanın tarafını ya da tarihini karıştırmak.',zorluk='orta',kalip='düz',adim=4,tipId='tar-dsv-rusya',kaynak=KY),
}
TIPLER={'tar-dsv-giris':'Osmanlı’nın savaşa giriş biçimi','tar-dsv-canakkale':'Çanakkale Cephesi metin yorumu','tar-dsv-cephe':'Osmanlı’nın savaştığı cepheler','tar-dsv-rusya':'Rusya’nın savaştan çekilmesi'}
Q=Konu('dunyasavasi','I. Dünya Savaşı',KARTLAR,TIPLER)
Q.zd={'kolay': 1, 'orta': 3}

Q.S('0001','K-DSV-01','kolay','Osmanlı Devleti’nin savaşa fiilen girmesini sağlayan olayı bilir.',2,'düz',
 'Osmanlı Devleti, 1914 yılında aşağıdaki gelişmelerden hangisiyle I. Dünya Savaşı’na fiilen girmiştir?',
 'Osmanlı donanmasının Rus limanlarını bombalaması',
 [('Almanya ile gizli ittifak antlaşmasının imzalanması','Gizli ittifak antlaşması savaşa girmeden önce imzalanmıştır; bu antlaşma fiilen savaşa girmek anlamına gelmez.','dikkat'),
  ('Sarıkamış Harekâtı’nın başlatılması','Sarıkamış Harekâtı, Osmanlı Devleti savaşa girdikten sonra yapılmıştır.','bilgi'),
  ('Çanakkale Deniz Savaşı’nın yapılması','Çanakkale Deniz Savaşı 1915’tedir; Osmanlı Devleti’nin savaşa girmesinden sonradır.','bilgi'),
  ('Brest-Litovsk Antlaşması’nın imzalanması','Brest-Litovsk 1918’de Rusya ile yapılmıştır; savaşın sonlarına aittir.','bilgi')],
 'D','Osmanlı’nın savaşa fiilen girişi.','Fiilen savaşa girmek, bir saldırı eylemiyle olur; sadece ittifak yeterli değildir.',
 [B('Osmanlı’nın savaşa girişi','Önce Almanya ile gizli ittifak (Ağustos 1914) · sonra Karadeniz’de Rus limanlarının bombalanması (29 Ekim 1914) ile fiilen savaşa giriş')],
 [A('Fiilî girişi tanımla','Fiilen savaşa girmek, düşmana karşı silahlı saldırıya geçmektir.','giriş = ilk saldırı'),
  A('Şıkları tarihlendir','Gizli ittifak savaştan önce, Sarıkamış ve Çanakkale savaşa girişten sonra, Brest-Litovsk 1918’dedir.','A: önce · B, C: sonra · E: 1918'),
  A('Doğru şıkkı seç','Karadeniz’de Rus limanlarının bombalanması ilk silahlı saldırıdır.','D: doğru')],
 'Savaşa giriş sorularında ittifak ile fiilî saldırıyı ayır.')

Q.S('0002','K-DSV-02','orta','Çanakkale Cephesi bilgisinden doğrudan çıkan yargıyı seçer.',3,'düz',
 'Mart 1915’te İngiliz ve Fransız donanması Çanakkale Boğazı’nı geçmeye çalışmış, ancak mayınlar ve kıyı bataryaları yüzünden gemi kayıpları vererek geri çekilmiştir. Bunun üzerine İtilaf Devletleri kara harekâtına başlamış, Ocak 1916’da bölgeyi tamamen boşaltmıştır.\nBu bilgilere göre aşağıdakilerden hangisine ulaşılabilir?',
 'Önce deniz harekâtı denenmiş, ardından kara harekâtına geçilmiştir.',
 [('Kara harekâtı, deniz harekâtından önce yapılmıştır.','Metinde kara harekâtının deniz harekâtının ardından başladığı yazıyor; yargı sırayı tersine çeviriyor.','dikkat'),
  ('İtilaf Devletleri, kara harekâtıyla Boğaz’ı geçmeyi başarmıştır.','Metne göre İtilaf Devletleri bölgeyi boşaltmıştır; Boğaz’ı geçemedikleri anlaşılıyor.','dikkat'),
  ('Harekâtta Almanya’nın İtilaf Devletleri’ne karşı doğrudan kuvvet gönderdiği anlaşılmaktadır.','Metinde Almanya’dan söz edilmiyor; yargı metinden çıkarılamaz.','dikkat'),
  ('Çanakkale’deki çarpışmalar yalnız deniz yoluyla yürütülmüştür.','Metinde kara harekâtından da söz ediliyor; çarpışmalar yalnız denizde değildir.','dikkat')],
 'B','Metinden çıkan yargı.','Metindeki olayları tarih sırasına diz: Mart 1915, kara harekâtı, Ocak 1916.',
 [B('Çanakkale Cephesi','Mart 1915’te deniz harekâtı (18 Mart) · ardından kara harekâtı · Ocak 1916’da İtilaf Devletleri bölgeden çekildi')],
 [A('Olayları sırala','Önce donanma Boğaz’ı geçmeye çalışmış, sonra kara harekâtı başlamış, en son bölge boşaltılmıştır.','deniz → kara → çekilme'),
  A('Şıkları sına','Sırayı tersine çeviren, Boğaz’ın geçildiğini söyleyen, Almanya’yı katan ve yalnız denizden söz eden yargılar metinle uyuşmaz.','A, C, D, E: elenir'),
  A('Doğru şıkkı seç','Önce deniz, sonra kara harekâtı yargısı metinden çıkar.','B: doğru')],
 'Metin sorusunda olay sırasını kendin yaz, şıkları ona göre ele.')

Q.oncul('0003','K-DSV-03','orta','Osmanlı Devleti’nin savaştığı cepheleri ayırt eder.',3,'',
 [('Kafkas Cephesi',True,'Osmanlı Devleti Rusya’ya karşı Kafkas Cephesi’nde savaşmıştır'),('Verdun Cephesi',False,'Verdun Almanya ile Fransa arasındaki Batı Cephesi’dir; Osmanlı bu cephede savaşmamıştır'),('Kanal (Süveyş) Cephesi',True,'Osmanlı Devleti İngilizlere karşı Süveyş Kanalı’na harekât yapmıştır'),('Marne Cephesi',False,'Marne Fransa’daki Batı Cephesi’dir; Osmanlı bu cephede yer almamıştır')],
 'Yukarıdakilerden hangileri Osmanlı Devleti’nin I. Dünya Savaşı’nda savaştığı cepheler arasındadır?',
 ['I ve III','II ve IV','Yalnız I','I, II ve III','III ve IV'],'A',True,'Osmanlı’nın savaştığı cepheler.','Fransa’daki Batı Cephesi’nde Osmanlı’nın kuvveti var mıydı?',
 [B('Osmanlı cepheleri','Kafkas (Rusya) · Kanal (İngiltere) · Irak · Çanakkale · Filistin · Hicaz · Galiçya, Romanya, Makedonya (müttefiklere yardım)'),B('Batı Cephesi','Verdun ve Marne Fransa’dadır; Almanya ile Fransa/İngiltere arasında yaşanmıştır')],
 [A('Cepheleri yerlerine göre ayır','Kafkaslar ve Süveyş Osmanlı sınırlarının doğu ve güneyindedir. Verdun ve Marne Fransa’dadır.','I, III: Osmanlı sınırı · II, IV: Fransa'),
  A('Osmanlı’nın karşıtlarını hatırla','Osmanlı, Rusya’ya Kafkaslar’da, İngilizlere Süveyş’te karşı koymuştur.','Kafkas: Rusya · Kanal: İngiltere'),
  A('Sonucu bul','Osmanlı’nın savaştığı cepheler I ve III’tür.','I ve III')],
 'Cephe sorularında cephenin coğrafyasına ve karşı devlete bak.')

Q.S('0004','K-DSV-04','orta','Rusya’nın savaştan çekilmesinin sonuçlarını metinden çıkarır.',4,'düz',
 '1917’de Rusya’da yönetimi ele geçiren kadro ülkeyi savaştan çıkarmak istemiştir. Mart 1918’de Almanya ve müttefikleriyle imzalanan antlaşmada Rusya, 1878’de Osmanlı Devleti’nden aldığı Kars, Ardahan ve Batum’u Osmanlı Devleti’ne bırakmıştır.\nBu bilgilere göre aşağıdakilerden hangisine ulaşılabilir?',
 'Rusya, Kars, Ardahan ve Batum’u Osmanlı Devleti’ne bırakmıştır.',
 [('Rusya, bu antlaşmayı İtilaf Devletleri ile imzalamıştır.','Metne göre antlaşma Almanya ve müttefikleriyle imzalanmıştır; Rusya’nın karşı tarafı İtilaf değil İttifak bloğudur.','dikkat'),
  ('Rusya’daki yönetim değişikliği 1918’de olmuştur.','Metinde yönetim değişikliğinin 1917’de olduğu yazıyor; 1918 antlaşmanın tarihidir.','dikkat'),
  ('Osmanlı Devleti, antlaşmayla Kars ve Ardahan’ı Rusya’ya bırakmıştır.','Metne göre bu yerleri Rusya bırakmıştır; Osmanlı bırakmamıştır, yargı yönü tersine çeviriyor.','dikkat'),
  ('Antlaşmanın imzalandığı sırada Osmanlı Devleti savaştan çekilmiştir.','Metinde Osmanlı’nın savaştan çekildiğine dair bir bilgi yoktur; yargı metinden çıkarılamaz.','bilgi')],
 'E','Metinden çıkan yargı.','Önce yönetim değişikliğinin, sonra antlaşmanın tarihini yaz.',
 [B('Brest-Litovsk Antlaşması (Mart 1918)','Rusya, Almanya ve müttefikleriyle barış yaptı · Kars, Ardahan ve Batum Osmanlı Devleti’ne bırakıldı')],
 [A('Tarihleri ayır','Yönetim değişikliği 1917’de, antlaşma Mart 1918’dedir. Karşı taraf Almanya ve müttefikleridir.','1917: yönetim · 1918: antlaşma'),
  A('Toprak yönünü bul','Rusya 1878’de aldığı yerleri Osmanlı Devleti’ne bırakmıştır.','Rusya: bırakan · Osmanlı: geri alan'),
  A('Şıkları metinle sına','İtilaf ile imza, 1918’de yönetim değişikliği, Osmanlı’nın toprak bırakması ve savaştan çekilmesi metinle uyuşmaz.','A, B, C, D: elenir'),
  A('Doğru şıkkı seç','Rusya’nın Kars, Ardahan ve Batum’u Osmanlı Devleti’ne bıraktığı yargısı metinden doğrudan çıkar.','E: doğru')],
 'Antlaşma sorularında kimin neyi bıraktığını ayrı ayrı yaz.')
Q.bitir()
