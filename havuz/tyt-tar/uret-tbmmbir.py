"""TYT Tarih · I. TBMM Dönemi: 4 ana soru (hafif mod). Önek rakam içeremediği için 'tbmmbir' (tbmm1)."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _hafif_tar_c import *
KY='ÖSYM 2018–2026 TYT Tarih (TBMM’nin açılışı, Teşkilât-ı Esasiye) · MEB 10. sınıf ve T.C. İnkılap Tarihi'
KARTLAR={
 'K-TBA-01':dict(alt='İstiklal Marşı',fikir='İstiklal Marşı’nın kabul tarihini ve şairini bilmek.',tuzak='Marşı yazan şairi dönemin başka şairleriyle karıştırmak.',zorluk='kolay',kalip='düz',adim=2,tipId='tar-tba-marsi',kaynak=KY),
 'K-TBA-02':dict(alt='TBMM’nin açılış koşulları',fikir='Metindeki olay sırasından (işgal, Meclis-i Mebusan’ın kapanması, yeni meclis) doğru çıkarımı seçmek.',tuzak='Meclis-i Mebusan’ın Ankara’ya taşındığını sanmak.',zorluk='orta',kalip='düz',adim=3,tipId='tar-tba-acilis',kaynak=KY),
 'K-TBA-03':dict(alt='I. ve II. TBMM dönemi gelişmeleri',fikir='Gelişmeleri I. ve II. TBMM dönemine ayırmak.',tuzak='Cumhuriyetin ilanını (1923) I. TBMM işi sanmak.',zorluk='orta',kalip='öncüllü',adim=3,tipId='tar-tba-donem',kaynak=KY),
 'K-TBA-04':dict(alt='Teşkilât-ı Esasiye Kanunu',fikir='Kanun maddelerinden çıkarılamayan yargıyı bulmak.',tuzak='Yasama ve yürütmenin Meclis’te toplanmasını kuvvetler ayrılığı sanmak.',zorluk='kolay',kalip='düz',adim=4,tipId='tar-tba-teskilat',kaynak=KY),
}
TIPLER={'tar-tba-marsi':'İstiklal Marşı','tar-tba-acilis':'TBMM’nin açılışı metin yorumu','tar-tba-donem':'I. ve II. TBMM dönemleri','tar-tba-teskilat':'Teşkilât-ı Esasiye Kanunu metin yorumu'}
Q=Konu('tbmmbir','I. TBMM Dönemi',KARTLAR,TIPLER)
Q.zd={'kolay': 2, 'orta': 2}

Q.S('0001','K-TBA-01','kolay','İstiklal Marşı’nın söz yazarını bilir.',2,'düz',
 'TBMM tarafından 12 Mart 1921’de millî marş olarak kabul edilen İstiklal Marşı’nın söz yazarı kimdir?',
 'Mehmet Akif Ersoy',
 [('Ziya Gökalp','Ziya Gökalp Türkçülüğün fikir adamıdır; İstiklal Marşı’nın söz yazarı değildir.','bilgi'),
  ('Namık Kemal','Namık Kemal 19. yüzyılın şairidir; marş 1921’de yazılmıştır, yazarı o değildir.','bilgi'),
  ('Tevfik Fikret','Tevfik Fikret Servet-i Fünun şairidir; İstiklal Marşı’nı yazmamıştır.','bilgi'),
  ('Yahya Kemal Beyatlı','Yahya Kemal Beyatlı dönemin başka bir şairidir; marşın söz yazarı değildir.','bilgi')],
 'E','İstiklal Marşı’nın söz yazarı.','Marşı yazan şair, ödül parasını almayı reddetmiştir.',
 [B('İstiklal Marşı','TBMM 12 Mart 1921’de kabul etti · söz yazarı Mehmet Akif Ersoy')],
 [A('Marşın tarihini hatırla','İstiklal Marşı 12 Mart 1921’de Meclis tarafından kabul edilmiştir.','kabul: 12 Mart 1921'),
  A('Şairleri ele','Ziya Gökalp fikir adamıdır; Namık Kemal ve Tevfik Fikret’in dönemi daha eskidir. Yahya Kemal marşı yazmamıştır.','A, B, C, D: yazar değil'),
  A('Doğru şıkkı seç','Marşın söz yazarı Mehmet Akif Ersoy’dur.','Mehmet Akif Ersoy')],
 'Millî Mücadele’nin simge eserlerini yazarlarıyla birlikte öğren.')

Q.S('0002','K-TBA-02','orta','TBMM’nin açılışına ilişkin metinden doğrudan çıkan yargıyı seçer.',3,'düz',
 '16 Mart 1920’de İstanbul İtilaf Devletleri tarafından resmen işgal edilmiş, bazı milletvekilleri tutuklanarak sürgüne gönderilmiştir. Meclis-i Mebusan toplanamaz hâle gelince Mustafa Kemal Paşa, Ankara’da olağanüstü yetkilere sahip bir meclisin toplanacağını duyurmuştur. Ankara’da toplanan meclise İstanbul’dan gelebilen eski mebuslar da katılmıştır.\nBu bilgilere göre aşağıdakilerden hangisine ulaşılabilir?',
 'Ankara’da meclis toplama kararı, işgalden sonra duyurulmuştur.',
 [('Meclis-i Mebusan, Ankara’ya taşınarak çalışmalarını sürdürmüştür.','Metne göre Ankara’da yeni bir meclis toplanmıştır; Meclis-i Mebusan’ın taşındığı söylenmiyor.','dikkat'),
  ('Ankara’daki meclise yalnız tutuklanan milletvekilleri katılmıştır.','Metinde tutuklananlar sürgüne gönderilmiş; meclise katılanlar İstanbul’dan gelebilen eski mebuslardır.','dikkat'),
  ('İstanbul’un işgali, Ankara’daki meclisin açılmasından sonra gerçekleşmiştir.','Metnin sırasına göre işgal (16 Mart 1920) Ankara’daki meclisin toplanmasından öncedir.','dikkat'),
  ('Ankara’daki meclis, İtilaf Devletleri’nin onayıyla toplanmıştır.','Metinde İtilaf Devletleri’nin onayından söz edilmiyor; yargı metinden çıkarılamaz.','dikkat')],
 'C','Metinden çıkan yargı.','İşgal, Meclis-i Mebusan’ın kapanması ve yeni meclis arasındaki sıralamayı yaz.',
 [B('TBMM’nin açılışı','16 Mart 1920 İstanbul’un işgali · Meclis-i Mebusan dağıldı · 23 Nisan 1920’de Ankara’da TBMM açıldı')],
 [A('Olay sırasını kur','Önce İstanbul işgal edilmiş, Meclis-i Mebusan çalışamaz olmuş, sonra Ankara’da meclis duyurulmuştur.','işgal → Mebusan kapanır → Ankara meclisi'),
  A('Şıkları sına','Mebusan’ın taşınması, yalnız tutuklananların katılması, sırayı ters çeviren ve onay içeren yargılar metne uymaz.','A, B, D, E: elenir'),
  A('Doğru şıkkı seç','Fikrin Mebusan’ın çalışamaz olmasından sonra duyurulduğu yargısı metinden çıkar.','C: doğru')],
 'Sıra sorularında önce olayları tarih sırasıyla diz.')

Q.oncul('0003','K-TBA-03','orta','Gelişmeleri I. ve II. TBMM dönemlerine ayırır.',3,'',
 [('Teşkilât-ı Esasiye Kanunu’nun kabul edilmesi',True,'20 Ocak 1921’de I. TBMM kabul etmiştir'),('Saltanatın kaldırılması',True,'1 Kasım 1922’de I. TBMM kararıyla kaldırılmıştır'),('Cumhuriyet’in ilan edilmesi',False,'29 Ekim 1923’te II. TBMM döneminde ilan edilmiştir'),('Halifeliğin kaldırılması',False,'3 Mart 1924’te II. TBMM döneminde kaldırılmıştır')],
 'Yukarıdakilerden hangileri I. TBMM Dönemi’nde (1920–1923) gerçekleşmiştir?',
 ['Yalnız IV','III ve IV','II ve III','I ve II','I, III ve IV'],'D',True,'I. TBMM dönemi gelişmeleri.','I. TBMM’nin ömrü Ağustos 1923’te sona erdi.',
 [B('TBMM dönemleri','I. TBMM: 1920–1923 · II. TBMM: Ağustos 1923’ten başlar'),B('Tarihler','Teşkilât-ı Esasiye 1921 · saltanatın kaldırılması 1922 · Cumhuriyet 1923 (Ekim) · halifeliğin kaldırılması 1924')],
 [A('Dönem sınırını koy','I. TBMM, 23 Nisan 1920’den Ağustos 1923’e kadar sürmüştür.','sınır: Ağustos 1923'),
  A('Olayları tarihlendir','Teşkilât-ı Esasiye 1921’de, saltanatın kaldırılması 1922’de oldu. Cumhuriyet Ekim 1923’te, halifelik 1924’te kaldırıldı.','I: 1921 · II: 1922 · III: 1923 (Ekim) · IV: 1924'),
  A('Sonucu bul','Ağustos 1923’ten önceki olaylar I ve II’dir.','I ve II')],
 'Dönem sorularında olayın yılını Ağustos 1923 sınırıyla karşılaştır.')

Q.S('0004','K-TBA-04','kolay','Teşkilât-ı Esasiye ilkelerinden çıkarılamayan yargıyı bulur.',4,'düz',
 'Teşkilât-ı Esasiye Kanunu’nda şu ilkeler yer almıştır: Egemenlik kayıtsız şartsız milletindir. Yönetim biçimi, halkın kendi kaderini bizzat yönetmesi esasına dayanır. Yasama ve yürütme yetkisi, milletin tek ve gerçek temsilcisi olan Meclis’te toplanmıştır.\nBu bilgilere göre aşağıdakilerden hangisine ulaşılamaz?',
 'Yürütme yetkisinin padişah tarafından Meclis adına kullanıldığına',
 [('Egemenliğin kaynağı olarak milletin gösterildiğine','Metnin ilk ilkesi egemenliği milletindir diye belirtir; bu yargı metinden çıkar.','dikkat'),
  ('Halkın yönetimde doğrudan rol almasının esas alındığına','İkinci ilke halkın kendi kaderini bizzat yönetmesinden söz eder; bu yargı metinden çıkar.','dikkat'),
  ('Meclis’in milleti temsil eden tek organ sayıldığına','Üçüncü ilkede Meclis, milletin tek ve gerçek temsilcisi diye geçer; yargı metinden çıkar.','dikkat'),
  ('Yasama ve yürütme yetkilerinin tek organda toplandığına','Üçüncü ilke bu iki yetkinin Meclis’te toplandığını belirtir; yargı metinden çıkar.','dikkat')],
 'B','Metinden ulaşılamayan yargı.','Kök “ulaşılamaz” diyor; metne ters düşen ya da metinde olmayan yargıyı ara.',
 [B('Teşkilât-ı Esasiye Kanunu (20 Ocak 1921)','İlk anayasa niteliğindeki düzenleme · egemenlik milletindir · yasama ve yürütme Meclis’te toplanır (kuvvetler birliği)'),B('“Ulaşılamaz” kökü','dört şık metinden çıkar, biri çıkmaz · çıkmayan şık doğru cevaptır')],
 [A('Kökü doğru oku','Soru metinden ulaşılamayanı soruyor; dört şık metinden çıkacak, biri çıkmayacak.','aranan: metne ters ya da metinde yok'),
  A('Şıkları teker teker sına','Millet egemenliği, halkın yönetime katılması, Meclis’in tek temsilci olması ve yetkilerin toplanması metinde var.','A, C, D, E: metinde var'),
  A('Metinle çelişeni bul','Metinde yetkiler Meclis’te toplanmıştır; yürütmenin padişah tarafından kullanıldığı yargısı metne ters düşer.','B: metinden çıkmaz'),
  A('Doğru şıkkı seç','Ulaşılamayan yargı B’dir.','B')],
 '“Ulaşılamaz” kökünde dört şıkkı metinde bul, çıkmayanı işaretle.')
Q.bitir()
