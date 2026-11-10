"""TYT Tarih · Türk İnkılabı: 4 ana soru (hafif mod)."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _hafif_tar_c import *
KY='ÖSYM 2018–2026 TYT Tarih (inkılaplar) · MEB T.C. İnkılap Tarihi ve Atatürkçülük'
KARTLAR={
 'K-INK-01':dict(alt='Tevhid-i Tedrisat',fikir='Eğitimin tek çatı altında toplanmasını sağlayan inkılabı bilmek.',tuzak='Harf İnkılabı’nı eğitimde birlik sanmak.',zorluk='kolay',kalip='düz',adim=2,tipId='tar-ink-egitim',kaynak=KY),
 'K-INK-02':dict(alt='Medeni Kanun',fikir='Hukuk alanındaki düzenlemelerin içeriğini metinden çıkarmak.',tuzak='Başka yıllarda verilen hakları (siyasal haklar) Medeni Kanun’a bağlamak.',zorluk='orta',kalip='düz',adim=3,tipId='tar-ink-medeni',kaynak=KY),
 'K-INK-03':dict(alt='İnkılap kronolojisi',fikir='Dört inkılabı yıllarına göre sıralamak.',tuzak='Harf İnkılabı ile Medeni Kanun’un sırasını karıştırmak.',zorluk='orta',kalip='düz',adim=3,tipId='tar-ink-sira',kaynak=KY),
 'K-INK-04':dict(alt='Takvim ve yazı alanındaki inkılaplar',fikir='Metinde olmayan bilgiyi, metne dayalı yargılardan ayırmak.',tuzak='Doğru olan ama metinde yer almayan bilgiyi metinden çıkan sanmak.',zorluk='orta',kalip='düz',adim=4,tipId='tar-ink-takvim',kaynak=KY),
}
TIPLER={'tar-ink-egitim':'Eğitim alanındaki inkılaplar','tar-ink-medeni':'Medeni Kanun metin yorumu','tar-ink-sira':'İnkılapların kronolojisi','tar-ink-takvim':'Takvim ve yazı inkılapları metin yorumu'}
Q=Konu('inkilap','Türk İnkılabı',KARTLAR,TIPLER)
Q.zd={'kolay': 1, 'orta': 3}

Q.S('0001','K-INK-01','kolay','Eğitimde birliği sağlayan inkılabı bilir.',2,'düz',
 'Bütün okulların Maarif Vekâleti’ne bağlanmasını ve medreselerin kapatılmasını sağlayan inkılap aşağıdakilerden hangisidir?',
 'Tevhid-i Tedrisat Kanunu’nun çıkarılması',
 [('Yeni Türk harflerinin kabul edilmesi','Harf İnkılabı yazı sistemini değiştirmiştir; okulların tek çatı altında toplanmasıyla ilgili değildir.','bilgi'),
  ('Medeni Kanun’un kabul edilmesi','Medeni Kanun hukuk ve aile alanındaki düzenlemedir; eğitimle ilgili değildir.','bilgi'),
  ('Şapka İktisası Kanunu’nun çıkarılması','Şapka Kanunu kıyafetle ilgilidir; okulları düzenlemez.','bilgi'),
  ('Soyadı Kanunu’nun uygulamaya konması','Soyadı Kanunu 1934’te toplumsal alanda yapılmıştır; okulları düzenlemez.','bilgi')],
 'A','Eğitimde birliği sağlayan inkılap.','Soruda “bütün okullar” ve “medreseler” geçiyor; hangi kanun bunları tek çatıda topladı?',
 [B('Tevhid-i Tedrisat Kanunu','3 Mart 1924 · bütün eğitim kurumları Maarif Vekâleti’ne bağlandı · medreseler kapatıldı')],
 [A('Soruyu alanına ayır','Okullar ve medreseler eğitim alanına girer.','alan: eğitim'),
  A('Şıkları alanlarına göre sınıfla','Harf İnkılabı yazı, Medeni Kanun hukuk, Şapka Kanunu kıyafet, Soyadı Kanunu toplumsal düzen alanındadır.','B: yazı · C: hukuk · D: kıyafet · E: soyadı'),
  A('Doğru şıkkı seç','Eğitimde birliği Tevhid-i Tedrisat Kanunu sağlamıştır.','A: doğru')],
 'İnkılap sorularında önce inkılabın hangi alanda olduğunu belirle.')

Q.S('0002','K-INK-02','orta','Medeni Kanun’un getirdiği düzenlemelerden doğrudan çıkan yargıyı seçer.',3,'düz',
 'Yeni hukuk düzeninde evlenme ancak resmî makamlar önünde yapılabilmektedir. Bir erkeğin aynı anda birden fazla kadınla evli olması yasaklanmıştır. Boşanma ise yalnızca mahkeme kararıyla gerçekleşebilmektedir.\nBu bilgilere göre aşağıdakilerden hangisine ulaşılabilir?',
 'Aile hukukunda devlet hukukunun esas alındığına',
 [('Kadınlara milletvekili seçme ve seçilme hakkı tanındığına','Metinde siyasal haklardan söz edilmiyor; bu haklar Medeni Kanun’dan sonra verilmiştir.','dikkat'),
  ('Eğitim kurumlarının tek çatı altında toplandığına','Metin aile hukukundan söz ediyor; eğitim kurumlarının birleştirilmesi metinde yok.','dikkat'),
  ('Boşanma hakkının erkeklerden alındığına','Metinde boşanma mahkeme kararına bağlanmış; erkeklerden hakkın alındığı söylenmiyor.','dikkat'),
  ('Evliliğin yalnız dinî nikâhla geçerli sayıldığına','Metne göre evlenme resmî makamlar önünde yapılır; dinî nikâh tek koşul değildir.','bilgi')],
 'E','Metinden çıkan yargı.','Evlenme, çok eşlilik ve boşanmanın hangi otoriteye bağlandığına bak.',
 [B('Medeni Kanun (1926)','İsviçre Medeni Kanunu esas alındı · resmî nikâh zorunlu · çok eşlilik yasak · boşanma mahkeme kararıyla')],
 [A('Metindeki üç kuralı çıkar','Resmî makamlar önünde evlenme, çok eşliliğin yasaklanması ve mahkeme kararıyla boşanma.','nikâh: resmî · çok eşlilik: yasak · boşanma: mahkeme'),
  A('Üç kuralın ortak noktasını bul','Üçü de aile hayatını devletin hukuk kurallarına bağlıyor.','ortak nokta: devlet hukuku'),
  A('Şıkları metinle sına','Siyasal haklar, eğitim birliği, erkeğin boşanma hakkının alınması ve dinî nikâh şartı metinde yok ya da metne ters.','A, B, C, D: elenir'),
  A('Doğru şıkkı seç','Devlet hukukunun esas alındığı yargısı metinden çıkar.','E: doğru')],
 'Üç kuralın ortak amacını bulursan doğru yargıya ulaşırsın.')

Q.S('0003','K-INK-03','orta','İnkılapları yıllarına göre sıralar.',3,'düz',
 'I. Şapka Kanunu’nun kabul edilmesi\nII. Harf İnkılabı’nın yapılması\nIII. Medeni Kanun’un kabul edilmesi\nIV. Soyadı Kanunu’nun çıkarılması\nYukarıdaki inkılaplar eskiden yeniye doğru sıralanırsa hangi sıralama elde edilir?',
 'I - III - II - IV',
 [('I - II - III - IV','Harf İnkılabı 1928’dedir; Medeni Kanun 1926’da kabul edildiğinden III, II’den önce gelir.','islem'),
  ('III - I - II - IV','Şapka Kanunu 1925’te, Medeni Kanun 1926’da kabul edildi; I, III’ten önce gelir.','islem'),
  ('I - III - IV - II','Soyadı Kanunu 1934’tedir; 1928’deki Harf İnkılabı IV’ten önce gelir.','islem'),
  ('II - I - III - IV','Harf İnkılabı 1928’dedir; Şapka (1925) ve Medeni Kanun (1926) ondan öncedir.','islem')],
 'B','Eskiden yeniye doğru doğru sıralama.','Yıllar: 1925, 1926, 1928 ve 1934 olaylarını tek tek yerleştir.',
 [B('İnkılap yılları','Şapka Kanunu 1925 · Medeni Kanun 1926 · Harf İnkılabı 1928 · Soyadı Kanunu 1934')],
 [A('Her inkılabın yılını yaz','Şapka Kanunu 1925, Medeni Kanun 1926, Harf İnkılabı 1928, Soyadı Kanunu 1934’tür.','I: 1925 · II: 1928 · III: 1926 · IV: 1934'),
  A('Yılları küçükten büyüğe diz','1925, 1926, 1928, 1934 sırası izlenir.','I → III → II → IV'),
  A('Şıkları sına','I - III - II - IV sırası yalnız B şıkkındadır.','B: doğru')],
 'Sıralama sorularında önce her olayın yılını yaz.')

Q.S('0004','K-INK-04','orta','Metinde olmayan bilgiyi metinden çıkan yargılardan ayırır.',4,'düz',
 'Cumhuriyet yönetimi 1925’te Hicrî takvim yerine Miladî takvimi benimsemiş, 1928’de ise yeni Türk harflerini kabul etmiştir. Böylece zaman ölçüsü ve yazı sistemi Batı dünyasıyla ortak bir zemine oturtulmuştur.\nBu bilgilere göre aşağıdakilerden hangisine ulaşılamaz?',
 'Yeni harflerin kabulünün ardından Millet Mektepleri’nin açıldığına',
 [('Miladî takvimin, yeni harflerden önce kabul edildiğine','Metne göre takvim 1925’te, harfler 1928’de kabul edilmiştir; bu yargı metinden çıkar.','dikkat'),
  ('Hem zaman ölçüsünde hem yazı sisteminde değişiklik yapıldığına','Metinde takvim ve yazı sistemindeki değişiklikler anlatılıyor; yargı metinden çıkar.','dikkat'),
  ('Yapılan düzenlemelerle Batı dünyasıyla uyum hedeflendiğine','Metnin son cümlesi ortak zeminden söz eder; yargı metinden çıkar.','dikkat'),
  ('Takvim ve harf düzenlemelerinin 1925–1928 arasında yapıldığına','Metinde iki düzenleme de 1925 ve 1928 yıllarıyla veriliyor; yargı metinden çıkar.','dikkat')],
 'C','Metinden ulaşılamayan yargı.','Dört şık metinde var; yalnız biri metinde hiç geçmiyor.',
 [B('Takvim ve yazı inkılapları','Miladî takvim 1925 (1926’dan itibaren uygulandı) · yeni Türk harfleri 1928 · Millet Mektepleri 1928–1929')],
 [A('Kökü doğru oku','Soru metinden çıkmayan yargıyı soruyor; dört şık metinde var, biri yok.','aranan: metinde olmayan'),
  A('Metindeki bilgileri yaz','Takvim 1925’te, harfler 1928’de, amaç Batı ile ortak zemin.','takvim: 1925 · harf: 1928 · amaç: ortak zemin'),
  A('Şıkları metinle sına','A, B, D ve E bu bilgilerden çıkıyor. Millet Mektepleri metinde hiç geçmiyor.','A, B, D, E: var · C: yok'),
  A('Doğru şıkkı seç','Millet Mektepleri doğru bir bilgi olsa da metinden çıkmaz.','C: doğru')],
 '“Ulaşılamaz” sorusunda doğru bilgi de metinde yoksa cevap olabilir.')
Q.bitir()
