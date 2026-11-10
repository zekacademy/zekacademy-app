"""TYT Tarih · 20. Yüzyılda Osmanlı Devleti: 4 ana soru (hafif mod)."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _hafif_tar_c import *
KY='ÖSYM 2018–2026 TYT Tarih (II. Meşrutiyet, Trablusgarp ve Balkan Savaşları) · MEB 11. sınıf tarih'
KARTLAR={
 'K-OSM-01':dict(alt='Trablusgarp Savaşı',fikir='Savaşı bitiren antlaşmayı, öteki savaşların antlaşmalarından ayırmak.',tuzak='Londra ve Bükreş’i Trablusgarp’a bağlamak.',zorluk='kolay',kalip='düz',adim=2,tipId='tar-osm-trablus',kaynak=KY),
 'K-OSM-02':dict(alt='31 Mart Vakası',fikir='Verilen kısa bilgiden doğrudan çıkan yargıyı seçmek; metinde olmayan bilgileri elemek.',tuzak='Tarihsel olarak doğru ama metinde yer almayan ya da metinle çelişen yargıyı seçmek.',zorluk='orta',kalip='düz',adim=3,tipId='tar-osm-31mart',kaynak=KY),
 'K-OSM-03':dict(alt='II. Meşrutiyet sonrası gelişmeler',fikir='Olayları 1908 öncesi ve sonrası diye ayırmak.',tuzak='I. Meşrutiyet olaylarını (1876–1878) II. Meşrutiyet sanmak.',zorluk='orta',kalip='öncüllü',adim=3,tipId='tar-osm-donem',kaynak=KY),
 'K-OSM-04':dict(alt='Bab-ı Ali Baskını',fikir='Metindeki bilgilerden hükûmet değişikliğinin nedenini çıkarmak.',tuzak='Metinde olmayan sonuçları (Edirne’nin düşmesi vb.) olmuş saymak.',zorluk='orta',kalip='düz',adim=4,tipId='tar-osm-babiali',kaynak=KY),
}
TIPLER={'tar-osm-trablus':'Trablusgarp Savaşı ve antlaşması','tar-osm-31mart':'31 Mart Vakası metin yorumu','tar-osm-donem':'II. Meşrutiyet öncesi ve sonrası olaylar','tar-osm-babiali':'Bab-ı Ali Baskını metin yorumu'}
Q=Konu('yyyirmi','20. Yüzyılda Osmanlı Devleti',KARTLAR,TIPLER)
Q.zd={'kolay': 1, 'orta': 3}

Q.S('0001','K-OSM-01','kolay','Trablusgarp Savaşı’nı sona erdiren antlaşmayı bilir.',2,'düz',
 'İtalya’nın Trablusgarp’a saldırmasıyla başlayan ve 1911–1912 yıllarında süren savaşı sona erdiren antlaşma aşağıdakilerden hangisidir?',
 'Uşi (Ouchy) Antlaşması',
 [('Londra Antlaşması','Londra Antlaşması I. Balkan Savaşı’nı bitirmiştir; Trablusgarp İtalya ile yapılan savaştı.','bilgi'),
  ('Bükreş Antlaşması','Bükreş Antlaşması II. Balkan Savaşı’nı bitiren, Balkan devletleri arasındaki antlaşmadır.','bilgi'),
  ('İstanbul Antlaşması','İstanbul Antlaşması 1913’te Bulgaristan ile imzalanmıştır; İtalya ile ilgisi yoktur.','bilgi'),
  ('Ayastefanos Antlaşması','Ayastefanos, 1877–1878 Osmanlı–Rus Savaşı’nın sonunda imzalanmıştır.','bilgi')],
 'C','Trablusgarp Savaşı’nı bitiren antlaşma.','Savaş İtalya ile yapıldı; Balkan devletleriyle yapılan antlaşmaları ele.',
 [B('Trablusgarp Savaşı','İtalya 1911’de Trablusgarp’a saldırdı · savaş Uşi (Ouchy) Antlaşması (1912) ile bitti'),B('Balkan Savaşları antlaşmaları','Londra (I. Balkan Savaşı) · Bükreş (II. Balkan Savaşı, Balkan devletleri arasında) · İstanbul (Osmanlı–Bulgaristan)')],
 [A('Karşı tarafı bul','Soruda savaşın İtalya ile yapıldığı belirtiliyor.','savaş: Osmanlı – İtalya (1911–1912)'),
  A('Antlaşmaları tek tek ele','Londra, Bükreş ve İstanbul Balkan savaşlarına bağlıdır. Ayastefanos ise 1878’de imzalanmıştır.','Londra, Bükreş, İstanbul: Balkanlar · Ayastefanos: 93 Harbi'),
  A('Doğru şıkkı seç','İtalya ile yapılan savaşı Uşi Antlaşması bitirmiştir.','Uşi (Ouchy) Antlaşması: doğru')],
 'Antlaşmayı önce savaşın tarafına, sonra tarihine bağla.')

Q.S('0002','K-OSM-02','orta','Verilen bilgiden doğrudan çıkan yargıyı seçer.',3,'düz',
 '31 Mart Vakası’nda İstanbul’daki bazı askerî birlikler ayaklanmıştır. Selanik’ten yola çıkan Hareket Ordusu İstanbul’a girerek ayaklanmayı bastırmıştır. Bu gelişmelerin ardından II. Abdülhamid tahttan indirilmiş, yerine V. Mehmed Reşad geçirilmiştir.\nBu bilgilere göre aşağıdakilerden hangisine ulaşılabilir?',
 'Padişah değişikliği, ayaklanmanın bastırılmasından sonra gerçekleşmiştir.',
 [('Ayaklanma, kısa sürede Anadolu’nun bütün illerine yayılmıştır.','Metinde ayaklanmanın yalnızca İstanbul’daki birliklerde çıktığı anlatılıyor; Anadolu’ya yayıldığı söylenmiyor.','dikkat'),
  ('Hareket Ordusu’nun İstanbul’a Edirne’den gelen birliklerden oluştuğu anlaşılmaktadır.','Metne göre Hareket Ordusu Selanik’ten yola çıkmıştır; Edirne’den söz edilmiyor.','dikkat'),
  ('V. Mehmed Reşad’ın tahta çıkmasıyla meşrutiyet yönetimi kaldırılmıştır.','Metinde meşrutiyetin kaldırıldığına dair bir bilgi yoktur; bu yargı tarihsel olarak da yanlıştır.','bilgi'),
  ('Ayaklanmayı bastıran güçlerle padişah arasında antlaşma yapılmıştır.','Metinde böyle bir antlaşmadan söz edilmiyor; yargı metinden çıkarılamaz.','dikkat')],
 'A','Metinden doğrudan çıkan yargı.','Önce olayların sırasını yaz: ayaklanma, bastırma, padişahın değişmesi.',
 [B('Bu bilgilere göre sorularında','doğru şık metinden doğrudan çıkar · tarihsel olarak doğru olsa bile metinde olmayan yargı yanlış sayılır'),B('31 Mart Vakası','İstanbul’da çıkan ayaklanma · Hareket Ordusu müdahale etti · II. Abdülhamid tahttan indirildi')],
 [A('Olayları sıraya koy','Önce ayaklanma çıkmış, Hareket Ordusu onu bastırmış, ardından padişah değişmiştir.','ayaklanma → bastırma → tahttan indirme'),
  A('Şıkları metinle karşılaştır','Anadolu’ya yayılma, Edirne, meşrutiyetin kaldırılması ve antlaşma metinde geçmez. Yalnız olayların sırası metinde vardır.','B, C, D, E: metinde yok ya da çelişiyor'),
  A('Doğru yargıyı seç','Padişah değişikliği bastırmadan sonra olmuştur.','A: doğru')],
 'Metne dayalı soruda yalnızca metinden çıkan yargı doğrudur.')

Q.oncul('0003','K-OSM-03','orta','II. Meşrutiyet öncesi ve sonrası olayları ayırt eder.',3,'',
 [('Trablusgarp Savaşı’nın başlaması',True,'1911’de başlamıştır; II. Meşrutiyet’ten (1908) sonradır'),('Meclis-i Mebusan’ın 1877’de ilk kez toplanması',False,'Meclis-i Mebusan ilk kez 1877’de toplanmıştır; I. Meşrutiyet dönemidir'),('Bab-ı Ali Baskını’nın yapılması',True,'1913’te yapılmıştır; II. Meşrutiyet’ten sonradır'),('Kanun-ı Esasi’nin ilk kez ilan edilmesi',False,'1876’da ilan edilmiştir; II. Meşrutiyet’ten öncedir')],
 'Yukarıdaki gelişmelerden hangileri, II. Meşrutiyet’in ilanından (1908) sonra gerçekleşmiştir?',
 ['Yalnız I','II ve IV','Yalnız III','I, III ve IV','I ve III'],'E',True,'1908’den sonraki olaylar.','Meclis-i Mebusan’ın ve Kanun-ı Esasi’nin ilk kez ortaya çıktığı dönemi düşün.',
 [B('Meşrutiyet dönemleri','I. Meşrutiyet: 1876 (Kanun-ı Esasi, 1877’de ilk Meclis) · II. Meşrutiyet: 1908')],
 [A('Dönem sınırını belirle','II. Meşrutiyet 1908’de ilan edilmiştir. Ölçüt bu yıldır.','sınır: 1908'),
  A('Olayları tarihlendir','Kanun-ı Esasi 1876’da, ilk Meclis-i Mebusan 1877’de kurulmuştur. Trablusgarp Savaşı 1911’de, Bab-ı Ali Baskını 1913’te yaşanmıştır.','I: 1911 · II: 1877 · III: 1913 · IV: 1876'),
  A('Sonucu bul','1908’den sonra olanlar I ve III’tür.','I ve III')],
 'Meşrutiyet olaylarını önce 1876–1877 mi 1908 mi diye ayır.')

Q.S('0004','K-OSM-04','orta','Bab-ı Ali Baskını bilgisinden çıkarım yapar.',4,'düz',
 'Ocak 1913’te bir grup subay, hükûmetin Edirne’yi terk edeceği kaygısıyla Bab-ı Ali’yi basmıştır. Baskın sırasında Harbiye Nazırı Nazım Paşa hayatını kaybetmiş, Sadrazam Kâmil Paşa görevinden çekilmiş, yerine Mahmut Şevket Paşa getirilmiştir.\nBu bilgilere göre aşağıdakilerden hangisine ulaşılabilir?',
 'Hükûmetin değişmesinde silahlı bir müdahale etkili olmuştur.',
 [('Edirne’nin düşmesi üzerine Kâmil Paşa hükûmeti görevden alınmıştır.','Metinde hükûmetin görevden alınması Edirne’nin düşmesine değil, subayların baskınına bağlanıyor; subayların kaygısı vardı.','dikkat'),
  ('Kâmil Paşa’nın yerine Nazım Paşa sadrazam yapılmıştır.','Metne göre Nazım Paşa baskında ölmüş, sadrazam olarak Mahmut Şevket Paşa getirilmiştir.','dikkat'),
  ('Baskını yapanlar hükûmetin Bulgaristan ile barış yapmasını istemiştir.','Metindeki kaygı Edirne’nin terk edilmesidir; subayların barış isteği metinde geçmiyor.','bilgi'),
  ('Baskın, Meclis-i Mebusan toplantısı sırasında yapılmıştır.','Metinde Meclis-i Mebusan’dan söz edilmiyor; yargı metinden çıkarılamaz.','dikkat')],
 'B','Metinden çıkan yargı.','Sadrazamın değişme nedenini metinde ara.',
 [B('Bab-ı Ali Baskını (1913)','Edirne’nin terk edilmesi kaygısıyla bir grup subayın hükûmete yaptığı baskın · Harbiye Nazırı Nazım Paşa öldü · Kâmil Paşa hükûmeti düştü')],
 [A('Olay zincirini kur','Subaylar Bab-ı Ali’yi basmış, Nazım Paşa ölmüş, Kâmil Paşa çekilmiştir.','baskın → ölüm → istifa'),
  A('Hükûmet değişikliğinin nedenini bul','Sadrazamın görevden çekilmesi baskından sonra olmuştur. Yani değişiklikte silahlı müdahale etkilidir.','neden: silahlı baskın'),
  A('Metinde olmayanları ele','Edirne’nin düşmesi, Nazım Paşa’nın sadrazamlığı, barış isteği ve Meclis toplantısı metinle uyuşmaz ya da metinde yoktur.','A, C, D, E: elenir'),
  A('Doğru şıkkı seç','Yalnız B metinden doğrudan çıkar.','B: doğru')],
 'Hükûmet değişikliği gibi sonuçlarda, metindeki neden–sonuç bağını izle.')
Q.bitir()
