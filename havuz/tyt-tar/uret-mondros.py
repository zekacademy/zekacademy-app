"""TYT Tarih · Mondros Ateşkesi, İşgaller ve Cemiyetler: 4 ana soru (hafif mod)."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _hafif_tar_c import *
KY='ÖSYM 2018–2026 TYT Tarih (Mondros, işgaller, cemiyetler) · MEB 10. sınıf ve T.C. İnkılap Tarihi'
KARTLAR={
 'K-MND-01':dict(alt='Mondros Mütarekesi’nin imzalanması',fikir='Mütarekeyi imzalayan Osmanlı heyetinin başkanını bilmek.',tuzak='Millî Mücadele liderlerini ya da sonraki hükûmet başkanlarını imzacı sanmak.',zorluk='kolay',kalip='düz',adim=2,tipId='tar-mnd-imza',kaynak=KY),
 'K-MND-02':dict(alt='Mütarekenin işgale yol açan maddeleri',fikir='Madde metninden işgallere dayanak oluşturan hükmü çıkarmak.',tuzak='Metinde olmayan ya da metne ters yargıyı seçmek.',zorluk='orta',kalip='düz',adim=3,tipId='tar-mnd-madde',kaynak=KY),
 'K-MND-03':dict(alt='Millî ve azınlık cemiyetleri',fikir='İşgallere karşı kurulan millî cemiyetleri azınlık cemiyetlerinden ayırmak.',tuzak='Azınlık cemiyetlerini millî direniş örgütü sanmak.',zorluk='orta',kalip='öncüllü',adim=3,tipId='tar-mnd-cemiyet',kaynak=KY),
 'K-MND-04':dict(alt='Mütarekenin birinci ve yirmi dördüncü maddeleri',fikir='İki maddeden birlikte çıkarım yapmak: Boğazlar ve Vilayet-i Sitte.',tuzak='Maddelerdeki hükümleri Osmanlı lehine yorumlamak.',zorluk='orta',kalip='düz',adim=4,tipId='tar-mnd-iki-madde',kaynak=KY),
}
TIPLER={'tar-mnd-imza':'Mondros Mütarekesi’ni imzalayan heyet','tar-mnd-madde':'Mütareke maddesinden çıkarım','tar-mnd-cemiyet':'Millî ve azınlık cemiyetleri','tar-mnd-iki-madde':'İki maddeden birlikte çıkarım'}
Q=Konu('mondros','Mondros Ateşkesi, İşgaller ve Cemiyetler',KARTLAR,TIPLER)
Q.zd={'kolay': 1, 'orta': 3}

Q.S('0001','K-MND-01','kolay','Mondros Mütarekesi’ni imzalayan Osmanlı heyetinin başkanını bilir.',2,'düz',
 'Mondros Mütarekesi’ni 30 Ekim 1918’de Osmanlı Devleti adına imzalayan heyetin başkanı kimdir?',
 'Rauf Orbay',
 [('Mustafa Kemal Paşa','Mustafa Kemal Paşa mütareke sırasında Suriye cephesinde Yedinci Ordu Komutanı’ydı; imza heyetinde yer almamıştır.','bilgi'),
  ('Damat Ferit Paşa','Damat Ferit Paşa mütarekeden sonra, 1919’da sadrazam olmuştur; imzacı değildir.','bilgi'),
  ('Talat Paşa','Talat Paşa’nın hükûmeti mütarekeden önce istifa etmişti; imzayı o atmamıştır.','bilgi'),
  ('Enver Paşa','Enver Paşa savaşın sonunda yönetimden ayrılmıştı; imza heyetinde yer almamıştır.','bilgi')],
 'B','Mondros’u imzalayan heyetin başkanı.','Mütareke, Limni Adası’ndaki bir savaş gemisinde Bahriye Nazırı’nın başkanlığında imzalanmıştır.',
 [B('Mondros Mütarekesi','30 Ekim 1918 · Limni Adası’ndaki Mondros Limanı’nda İngiliz gemisi Agamemnon’da imzalandı · Osmanlı heyetinin başkanı Bahriye Nazırı Rauf Orbay')],
 [A('Mütareke tarihini hatırla','Mondros Mütarekesi 30 Ekim 1918’de imzalanmıştır.','tarih: 30 Ekim 1918'),
  A('Şıkları dönemine göre ele','Mustafa Kemal cephedeydi; Talat ve Enver Paşa mütarekeden önce yönetimden ayrılmıştı. Damat Ferit 1919’da sadrazam olmuştur.','A, C, D: imza heyetinde yok · B: 1919'),
  A('Doğru şıkkı seç','Heyetin başkanı Bahriye Nazırı Rauf Orbay’dır.','Rauf Orbay')],
 'İmza sorularında kişinin o tarihteki görevini hatırla.')

Q.S('0002','K-MND-02','orta','Mütareke maddesinden doğrudan çıkan yargıyı seçer.',3,'düz',
 'Mondros Mütarekesi’nin bir maddesinde, İtilaf Devletleri’nin güvenliğini tehdit eden bir durum ortaya çıkarsa herhangi bir stratejik noktayı işgal edebilecekleri belirtilmiştir.\nBu bilgilere göre aşağıdakilerden hangisine ulaşılabilir?',
 'İtilaf Devletleri, mütarekeye dayanarak işgal edebilecek duruma gelmiştir.',
 [('Mütareke ile Osmanlı Devleti’nin toprak bütünlüğü güvence altına alınmıştır.','Madde işgal hakkı tanıyor; toprak bütünlüğünün güvence altına alındığı sonucu metne ters düşer.','bilgi'),
  ('İşgal yetkisi yalnız Boğazlar’ı kapsamaktadır.','Metinde “herhangi bir stratejik nokta” deniyor; yetki Boğazlarla sınırlı değildir.','dikkat'),
  ('İtilaf Devletleri’nin işgal için Osmanlı hükûmetinden izin alması gerekmiştir.','Metinde izin şartı geçmiyor; madde işgal hakkını doğrudan İtilaf Devletleri’ne veriyor.','dikkat'),
  ('Osmanlı Devleti savaşa devam etme hakkını saklı tutmuştur.','Madde mütareke hükümlerinden söz ediyor; savaşa devam hakkı metinde yoktur.','bilgi')],
 'D','Maddeden çıkan yargı.','Maddede işgal hakkını kimin kullanacağını ve hangi yerleri kapsadığını bul.',
 [B('Mondros Mütarekesi’nin 7. maddesi','İtilaf Devletleri güvenliklerini tehdit eden durumda herhangi bir stratejik noktayı işgal edebilir')],
 [A('Maddeyi sadeleştir','İtilaf Devletleri tehdit hissederse herhangi bir stratejik yeri işgal edebilir.','hak sahibi: İtilaf · kapsam: herhangi bir stratejik nokta'),
  A('Şıkları maddeyle karşılaştır','Toprak bütünlüğü, yalnız Boğazlar, izin şartı ve savaşa devam hakkı maddede yoktur ya da maddeye ters düşer.','A, B, C, E: elenir'),
  A('Doğru şıkkı seç','İşgale girişebilecek duruma gelme yargısı maddeden çıkar.','D: doğru')],
 'Madde sorusunda hakkın sahibini ve kapsamını ayrı ayrı oku.')

Q.oncul('0003','K-MND-03','orta','Millî cemiyetleri azınlık cemiyetlerinden ayırt eder.',3,
 'Mondros Mütarekesi’nden sonra çeşitli cemiyetler kurulmuş ya da faaliyet göstermiştir.',
 [('Pontus Rum Cemiyeti',False,'Rumların kurduğu azınlık cemiyetidir; Türk halkının direnişi için kurulmamıştır'),('Trakya–Paşaeli Müdafaa-i Hukuk Cemiyeti',True,'Trakya’nın işgale karşı savunulması için kurulan millî cemiyettir'),('Taşnaksutyun Cemiyeti',False,'Ermenilerin siyasi amaçlı kurduğu azınlık cemiyetidir; millî direniş örgütü değildir'),('İzmir Müdafaa-i Hukuk Cemiyeti',True,'İzmir ve çevresinin işgale karşı savunulması için kurulan millî cemiyettir')],
 'Yukarıdakilerden hangileri işgallere karşı kurulan millî (Türk halkının) cemiyetlerdendir?',
 ['Yalnız I','I ve III','II ve IV','III ve IV','I, II ve IV'],'C',True,'Millî cemiyetler.','Bir cemiyetin kimin çıkarı için kurulduğuna bak.',
 [B('Mondros sonrası cemiyetler','Millî: Trakya–Paşaeli, İzmir, Doğu Anadolu Müdafaa-i Hukuk, Kilikyalılar vb. · Azınlık: Pontus Rum, Taşnak, Hınçak vb.')],
 [A('Ölçütü belirle','Millî cemiyetler işgale karşı yurdu savunmak için kurulmuştur. Azınlık cemiyetleri kendi siyasi amaçları için çalışmıştır.','ölçüt: yurdu savunma'),
  A('Cemiyetleri sınıflandır','Pontus Rum ve Taşnaksutyun azınlık cemiyetidir. Trakya–Paşaeli ve İzmir Müdafaa-i Hukuk millî cemiyettir.','I, III: azınlık · II, IV: millî'),
  A('Sonucu bul','Millî cemiyetler II ve IV’tür.','II ve IV')],
 'Cemiyet adındaki “Müdafaa-i Hukuk”, yurdu savunan millî örgütü gösterir.')

Q.S('0004','K-MND-04','orta','Mütarekenin iki maddesinden birlikte çıkarım yapar.',4,'düz',
 'Mondros Mütarekesi’nin bir maddesinde Çanakkale ve İstanbul Boğazları’nın açılacağı ve bu boğazların istihkâmlarının İtilaf Devletleri tarafından işgal edileceği yazılıdır. Bir başka maddede, Vilayet-i Sitte (altı vilayet) denilen Doğu Anadolu illerinde karışıklık çıkarsa İtilaf Devletleri’nin buraların bir kısmını işgal edebileceği belirtilmiştir.\nBu bilgilere göre aşağıdakilerden hangisine ulaşılabilir?',
 'Mütareke, Boğazlar’ın ve Doğu Anadolu’nun bir bölümünün işgaline olanak vermiştir.',
 [('Osmanlı Devleti, Boğazlar üzerindeki denetimini mütarekeden sonra da sürdürmüştür.','Metne göre Boğazlar’ın istihkâmları İtilaf Devletleri tarafından işgal edilecektir; Osmanlı denetimi sürmemiştir.','bilgi'),
  ('İşgal hakkı yalnız İstanbul ile sınırlı tutulmuştur.','Metinde Boğazlar’ın yanında Vilayet-i Sitte’den de söz ediliyor; hak yalnız İstanbul’la sınırlı değildir.','dikkat'),
  ('Vilayet-i Sitte’nin işgali Osmanlı hükûmetinin isteğine bağlanmıştır.','Metinde hükûmetin isteği şartı yok; işgal karışıklık çıkması durumuna bağlanmış.','dikkat'),
  ('Maddeler Osmanlı ordusunun güçlendirilmesini amaçlamıştır.','Maddeler işgale olanak veriyor; ordunun güçlendirilmesinden söz edilmiyor.','bilgi')],
 'A','İki maddeden çıkan yargı.','Her maddenin hangi bölgeye ve hangi hakka değindiğini ayrı yaz.',
 [B('Vilayet-i Sitte','Doğu Anadolu’daki altı vilayet: Erzurum, Van, Bitlis, Diyarbakır, Sivas, Elazığ (Mamuretülaziz)'),B('Mondros maddeleri','1. madde: Boğazlar açılır, istihkâmlar İtilaf Devletleri’nce işgal edilir · 24. madde: Vilayet-i Sitte’de karışıklıkta işgal hakkı')],
 [A('Maddeleri ayrı özetle','Bir maddede Boğazlar, başka bir maddede Doğu Anadolu’daki altı vilayet geçiyor. İkisinde de işgal hakkı İtilaf Devletleri’ne verilmiş.','1. madde: Boğazlar · 24. madde: Vilayet-i Sitte'),
  A('İki maddeyi birleştir','Böylece hem Boğazlar hem de Doğu Anadolu’nun bir kısmı işgale açık hâle gelmiştir.','sonuç: iki bölgede işgal olanağı'),
  A('Şıkları metinle sına','Osmanlı denetiminin sürmesi, yalnız İstanbul, hükûmet şartı ve ordunun güçlenmesi metinle uyuşmaz.','B, C, D, E: elenir'),
  A('Doğru şıkkı seç','İki bölgenin işgaline olanak verildiği yargısı metinden çıkar.','A: doğru')],
 'Birden çok madde varsa her birinin ne verdiğini ayrı yaz, sonra birleştir.')
Q.bitir()
