"""TYT Tarih · Atatürk İlkeleri: 4 ana soru (hafif mod)."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _hafif_tar_c import *
KY='ÖSYM 2018–2026 TYT Tarih (Atatürk ilkeleri) · MEB T.C. İnkılap Tarihi ve Atatürkçülük'
KARTLAR={
 'K-ILK-01':dict(alt='Laiklik ilkesi',fikir='Din ve devlet işlerinin ayrılması esasını laiklik olarak adlandırmak.',tuzak='Laikliği halkçılık ya da cumhuriyetçilikle karıştırmak.',zorluk='kolay',kalip='düz',adim=2,tipId='tar-ilk-tanim',kaynak=KY),
 'K-ILK-02':dict(alt='Devletçilik ilkesi',fikir='Karma ekonomi anlayışını metinden doğru okumak.',tuzak='Devletçiliği özel girişimi yasaklayan sistem sanmak.',zorluk='orta',kalip='düz',adim=3,tipId='tar-ilk-devletcilik',kaynak=KY),
 'K-ILK-03':dict(alt='Laiklik doğrultusundaki uygulamalar',fikir='Uygulamaları ilkelere göre ayırmak.',tuzak='Kadın haklarını ve ekonomik kuruluşları laiklikle karıştırmak.',zorluk='orta',kalip='öncüllü',adim=3,tipId='tar-ilk-uygulama',kaynak=KY),
 'K-ILK-04':dict(alt='Halkçılık ilkesi',fikir='İlkenin esaslarıyla çelişen uygulamayı bulmak.',tuzak='Ayrıcalığın kaldırılmasıyla ilgili uygulamaları ilkeyle çelişen sanmak.',zorluk='kolay',kalip='düz',adim=4,tipId='tar-ilk-halkcilik',kaynak=KY),
}
TIPLER={'tar-ilk-tanim':'Atatürk ilkesini tanımından bulma','tar-ilk-devletcilik':'Devletçilik metin yorumu','tar-ilk-uygulama':'Uygulamaları ilkeye göre ayırma','tar-ilk-halkcilik':'Halkçılık ilkesiyle çelişen uygulama'}
Q=Konu('ilkeler','Atatürk İlkeleri',KARTLAR,TIPLER)
Q.zd={'kolay': 2, 'orta': 2}

Q.S('0001','K-ILK-01','kolay','Atatürk ilkesini tanımından bulur.',2,'düz',
 'Din ve devlet işlerinin birbirinden ayrılmasını, devletin işleyişinde akıl ve bilimin esas alınmasını amaçlayan Atatürk ilkesi aşağıdakilerden hangisidir?',
 'Laiklik',
 [('Halkçılık','Halkçılık, kanun önünde eşitliği ve ayrıcalıkların kaldırılmasını anlatır; din–devlet ayrılığı değildir.','bilgi'),
  ('Cumhuriyetçilik','Cumhuriyetçilik, egemenliğin millette olduğu yönetim biçimini anlatır.','bilgi'),
  ('Devletçilik','Devletçilik ekonomi alanıyla ilgilidir; din ve devlet işlerini ilgilendirmez.','bilgi'),
  ('Milliyetçilik','Milliyetçilik, ulusal birlik ve bağımsızlık anlayışıdır; din–devlet ayrılığını anlatmaz.','bilgi')],
 'D','Din ve devlet işlerinin ayrılmasını ifade eden ilke.','Soru din ile devletin ilişkisini soruyor.',
 [B('Atatürk ilkeleri (6 ilke)','Cumhuriyetçilik · Milliyetçilik · Halkçılık · Devletçilik · Laiklik · İnkılapçılık'),B('Laiklik','din ve devlet işlerinin ayrılması · örnek: halifeliğin kaldırılması (1924)')],
 [A('Anahtar sözcüğü bul','Soruda “din ve devlet işlerinin ayrılması” anlatılıyor.','anahtar: din – devlet ayrılığı'),
  A('İlkeleri alanlarına göre ele','Halkçılık eşitlik, cumhuriyetçilik yönetim biçimi, devletçilik ekonomi, milliyetçilik ulus birliğidir.','A: eşitlik · B: yönetim · C: ekonomi · E: ulus'),
  A('Doğru şıkkı seç','Din–devlet ayrılığı laiklik ilkesidir.','D: Laiklik')],
 'İlkeyi, tanımındaki anahtar sözcükle (din–devlet, ekonomi, eşitlik) eşle.')

Q.S('0002','K-ILK-02','orta','Devletçilik anlayışını metinden yorumlar.',3,'düz',
 'Atatürk devletçiliğinde özel girişimin yapamayacağı büyük yatırımlar devlet tarafından üstlenilir. Bununla birlikte özel girişim engellenmez, aksine desteklenir.\nBu bilgilere göre aşağıdakilerden hangisine ulaşılabilir?',
 'Devletle özel girişimin birlikte yer aldığına',
 [('Özel girişimin devlet eliyle engellendiğine','Metinde özel girişimin engellenmediği, desteklendiği belirtiliyor; yargı metne ters.','bilgi'),
  ('Devletin ekonomideki yatırımlardan çekildiğine','Metne göre büyük yatırımları devlet üstlenir; devletin çekildiği söylenmiyor.','bilgi'),
  ('Yatırımların yalnız yabancı sermayeye bırakıldığına','Metinde yabancı sermayeden söz edilmiyor; yargı metinden çıkarılamaz.','dikkat'),
  ('Devletin yalnızca özel girişimin yaptığı yatırımları desteklediğine','Metne göre devlet büyük yatırımları kendisi de yapar; yalnız destek vermekle kalmaz.','dikkat')],
 'A','Metinden çıkan yargı.','Metindeki iki tarafı ayrı yaz: devletin rolü ve özel girişimin durumu.',
 [B('Devletçilik','özel girişimin yapamadığı büyük yatırımları devletin üstlenmesi · özel girişim engellenmez · karma ekonomi'),B('Örnek kuruluşlar','Sümerbank (1933), Etibank (1935)')],
 [A('İki tarafı ayır','Devlet büyük yatırımları üstlenir. Özel girişim desteklenir.','devlet: büyük yatırım · özel girişim: desteklenir'),
  A('Şıkları metinle sına','Yasaklama, devletin tamamen çekilmesi, yalnız yabancı sermaye ve yalnız destek yargıları metinle uyuşmaz.','B, C, D, E: elenir'),
  A('Doğru şıkkı seç','İkisinin birlikte yer aldığı karma anlayış metinden çıkar.','A: doğru')],
 'Devletçilikte devlet ve özel girişim birlikte vardır; ikisinden birini yok sayan şık yanlıştır.')

Q.oncul('0003','K-ILK-03','orta','Laiklik doğrultusundaki uygulamaları ayırt eder.',3,'',
 [('Sümerbank’ın kurulması',False,'Sümerbank devletçilik ilkesinin gereğidir; din–devlet ayrılığıyla ilgisi yoktur'),('Halifeliğin kaldırılması',True,'Din ve devlet işlerinin ayrılmasına yönelik adımdır'),('Kadınlara milletvekili seçme ve seçilme hakkının verilmesi',False,'Siyasal eşitlikle ilgilidir; halkçılık ilkesi kapsamındadır'),('Tevhid-i Tedrisat Kanunu’nun kabul edilmesi',True,'Eğitimin din kurumlarından alınıp devlet denetiminde birleştirilmesidir; laiklik doğrultusundadır')],
 'Yukarıdaki uygulamalardan hangileri laiklik ilkesi doğrultusunda yapılmıştır?',
 ['Yalnız I','I ve III','II ve IV','III ve IV','I, II ve IV'],'C',True,'Laiklik doğrultusundaki uygulamalar.','Din kurumlarının devlet işlerinden ayrılmasıyla ilgili olanları ara.',
 [B('Laiklik doğrultusundaki uygulamalar','halifeliğin kaldırılması (1924) · Tevhid-i Tedrisat (1924) · Şer’iye mahkemelerinin kaldırılması · anayasaya laiklik ilkesinin girmesi (1937)')],
 [A('İlkenin ölçütünü koy','Laiklik, din ve devlet işlerini ayırır. Uygulamanın bu ayrılığa hizmet etmesi gerekir.','ölçüt: din – devlet ayrılığı'),
  A('Uygulamaları sınıflandır','Sümerbank ekonomi, kadınlara seçme hakkı eşitlik alanındadır. Halifeliğin kaldırılması ve Tevhid-i Tedrisat din–devlet ayrılığına hizmet eder.','I: ekonomi · III: eşitlik · II, IV: laiklik'),
  A('Sonucu bul','Laiklik doğrultusundaki uygulamalar II ve IV’tür.','II ve IV')],
 'Uygulamayı önce ilkeyle eşle: ekonomi devletçilik, eşitlik halkçılık, din–devlet laiklik.')

Q.S('0004','K-ILK-04','kolay','Halkçılık ilkesiyle bağdaşmayan uygulamayı bulur.',4,'düz',
 'Halkçılık ilkesine göre toplum sınıflara değil, ortak çıkarları olan bireylere ayrılır. Hiçbir birey, aile ya da zümreye ayrıcalık tanınmaz; herkes kanun önünde eşittir.\nBu bilgilere göre aşağıdakilerden hangisi bu ilkeyle bağdaşmaz?',
 'Ağa ve beylerin vergi muafiyetlerinin sürdürülmesi',
 [('Kadın ve erkeğe mirasta eşit hak tanınması','Eşit hak, herkesin kanun önünde eşit sayılmasıyla bağdaşır; ilkeyle çelişmez.','dikkat'),
  ('Ağa, bey, paşa gibi lakap ve unvanların kaldırılması','Unvanların kaldırılması ayrıcalıkları ortadan kaldırır; ilkeyle çelişmez.','dikkat'),
  ('Herkesin aynı yasalara tabi olması','Herkesin aynı yasalara tabi olması kanun önünde eşitlik demektir; ilkeyle çelişmez.','dikkat'),
  ('Okulların toplumun bütün kesimlerine açık olması','Eğitimde fırsat eşitliği, ayrıcalık tanımama ilkesine uygundur; çelişmez.','dikkat')],
 'E','İlkeyle bağdaşmayan uygulama.','Ayrıcalığı sürdüren ya da yaratan şıkkı ara.',
 [B('Halkçılık','sınıf ayrımı yok · ayrıcalık yok · kanun önünde eşitlik'),B('Halkçılık örnekleri','lakap ve unvanların kaldırılması (1934) · Medeni Kanun ile eşit haklar · Halkevleri (1932)')],
 [A('İlkenin ölçütlerini yaz','Sınıf ayrımı yoktur, ayrıcalık tanınmaz, herkes kanun önünde eşittir.','ölçüt: eşitlik, ayrıcalık yok'),
  A('Kökü doğru oku','Soru ilkeyle bağdaşmayanı soruyor; dört şık eşitliği destekler.','aranan: ayrıcalık sürdüren'),
  A('Şıkları sına','Mirasta eşitlik, unvanların kaldırılması, aynı yasalar ve herkese açık okul eşitliği destekler. Vergi muafiyeti ayrıcalık sürdürür.','A–D: bağdaşır · E: ayrıcalık'),
  A('Doğru şıkkı seç','Ayrıcalıklı kesimlerin vergi muafiyeti ilkeyle bağdaşmaz.','E: doğru')],
 'Çelişki sorularında ilkenin ölçütüne en ters düşen şıkkı seç.')
Q.bitir()
