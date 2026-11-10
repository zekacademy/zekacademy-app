"""TYT Türkçe · Sözcük Türleri: 4 ana soru (hafif mod). Metinler özgündür."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from hafif_dilbilgisi import *
AD=A
KY='ÖSYM TYT Türkçe 2018–2026 (biçim bilgisi: sözcük türleri) ve MEB Türk Dili ve Edebiyatı müfredatı'
KARTLAR={
 'K-ST-01':dict(alt='Sıfat ve Zarf',fikir='Aynı sözcüğün cümledeki göreve göre sıfat ya da zarf olduğunu belirlemek.',tuzak='Sözcüğün türünü cümleye bakmadan tek başına yargılamak.',zorluk='kolay',kalip='düz',adim=2,tipId='szt-sifatzarf',kaynak=KY),
 'K-ST-02':dict(alt='Zamir (Adıl)',fikir='İsmin yerini tutan sözcüğü, ismi niteleyen işaret ve soru sıfatlarından ayırmak.',tuzak='“Bu, şu, hangi” gibi sözcükleri her zaman zamir saymak.',zorluk='orta',kalip='düz',adim=3,tipId='szt-zamir',kaynak=KY),
 'K-ST-03':dict(alt='Edat ve Bağlaç',fikir='Edatları ve bağlaçları görevlerine göre ayırt etmek.',tuzak='Cümleleri birbirine bağlayan sözcüğü edat sanmak.',zorluk='orta',kalip='düz',adim=3,tipId='szt-edatbaglac',kaynak=KY),
 'K-ST-04':dict(alt='Sözcüğün Görevi',fikir='Bir cümledeki birden fazla sözcüğün aynı anda hangi türde olduğunu belirlemek.',tuzak='Fiili niteleyen sözcüğü sıfat sanmak.',zorluk='zor',kalip='düz',adim=4,tipId='szt-gorev',kaynak=KY),
}
TIPLER={'szt-sifatzarf':'Sıfat ve zarf','szt-zamir':'Zamir (adıl)','szt-edatbaglac':'Edat ve bağlaç','szt-gorev':'Sözcüğün cümledeki görevi'}
Q=kur('sozcukturleri','Sözcük Türleri','tr|Sözcük Türleri',KARTLAR,TIPLER); Q.n=4
B_SZ=B('Sıfat ve zarf','sıfat: ismi niteler, isimden önce gelir (hızlı araba) · zarf: fiili, sıfatı ya da başka bir zarfı niteler (araba hızlı gitti). Aynı sözcük göreve göre değişir')
B_ZM=B('Zamir (adıl)','zamir ismin yerini tutar (bunu aldım). İsmin önünde onu niteleyen “bu kalem”deki gibi sözcükler sıfattır; ismin yerini tutmaz')
B_EB=B('Edat ve bağlaç','edat: tek başına anlamı olmayan, kendinden önceki sözcükle görev yapar (senin için, kar gibi, akşama kadar) · bağlaç: sözcükleri ya da cümleleri birbirine bağlar (ama, ve, fakat)')

# 0001 sıfat/zarf · kolay · C
soru(Q,'0001','K-ST-01','kolay','Tırnak içindeki sözcüğün zarf olarak kullanıldığı cümleyi bulur.',2,
 'Hangi cümlede tırnak içine alınan sözcük, fiili niteleyerek zarf görevinde kullanılmıştır?',
 [('“Hızlı” bir koşucu ödülü aldı.','sıfat','“Hızlı”, “koşucu” ismini niteler; sıfattır.','bilgi'),
  ('“Sessiz” sokakta yürüdük.','sıfat','“Sessiz”, “sokak” ismini niteler; sıfattır.','bilgi'),
  ('Çocuk eve “çabuk” döndü.','zarf','',''),
  ('Masaya “kırmızı” bir örtü serdi.','sıfat','“Kırmızı”, “örtü” ismini niteler; sıfattır.','dikkat'),
  ('“Yüksek” dağın zirvesine çıktık.','sıfat','“Yüksek”, “dağ” ismini niteler; sıfattır.','dikkat')],
 'C',lambda t:t=='zarf','Tırnak içindeki sözcüğün zarf olduğu cümle.',
 'Tırnak içindeki sözcük bir ismi mi, yoksa bir fiili mi niteliyor?',[B_SZ],
 [AD('Ölçütü hatırla','Zarf fiili niteler; sıfat ismi niteler.','zarf: fiil · sıfat: isim'),AD('Şıkları çöz','A koşucu, B sokakta, D örtü, E dağın: tırnak içindeki sözcük her seferinde bir ismi niteliyor.','A, B, D, E: sıfat'),AD('Fiili niteleyeni seç','C’de “çabuk”, “döndü” fiilinin nasıl yapıldığını söylüyor.','C: zarf')],
 'Niteleme sorularında tırnaklı sözcüğün hangi sözcüğü nitelediğine bak: isimse sıfat, fiilse zarf.')

# 0002 zamir · orta · E
soru(Q,'0002','K-ST-02','orta','İsmin yerini tutan sözcüğü (zamiri) ismi niteleyen sözcüklerden ayırır.',3,
 'Tırnaklı sözcüklerden hangisi, bir ismin yerini tutarak zamir (adıl) görevinde kullanılmıştır?',
 [('“Bu” kalemi dün aldım.','sıfat','“Bu”, “kalem” ismini niteler; işaret sıfatıdır, ismin yerini tutmaz.','bilgi'),
  ('“Hangi” kitabı okudun?','sıfat','“Hangi”, “kitap” ismini niteler; soru sıfatıdır.','bilgi'),
  ('“Şu” çantayı bana ver.','sıfat','“Şu”, “çanta” ismini niteler; işaret sıfatıdır.','dikkat'),
  ('“Kaç” kişi geldi?','sıfat','“Kaç”, “kişi” ismini niteler; soru sıfatıdır.','dikkat'),
  ('Diğerlerini bırakıp “bunu” seçtim.','zamir','','')],
 'E',lambda t:t=='zamir','Zamir olarak kullanılan sözcük.',
 'Tırnak içindeki sözcüğün hemen yanında nitelediği bir isim var mı?',[B_ZM],
 [AD('Ölçütü hatırla','Zamir tek başına bir ismin yerine geçer. Bir ismi niteliyorsa sıfattır.','yerini tutuyor → zamir'),AD('Şıkları çöz','A kalemi, B kitabı, C çantayı, D kişi: her tırnaklı sözcüğün hemen yanında nitelediği bir isim var.','A, B, C, D: sıfat'),AD('Yerini tutanı seç','E’de “bunu”, yanında isim olmadan bir nesnenin yerine geçiyor.','E: zamir')],
 'Tırnaklı sözcüğün yanında nitelediği isim yoksa ve isim yerine geçiyorsa zamirdir.')

# 0003 edat/bağlaç · orta · D
soru(Q,'0003','K-ST-03','orta','Cümleleri birbirine bağlayan sözcüğü (bağlacı) edatlardan ayırır.',3,
 'Bağlaç görevinde kullanılan tırnaklı sözcük, aşağıdakilerin hangisinde vardır?',
 [('Bu hediyeyi senin “için” aldım.','edat','“İçin”, “senin” sözcüğüyle birlikte görev yapan bir edattır.','bilgi'),
  ('Çocuklar kar “gibi” beyazdı.','edat','“Gibi”, benzetme bildiren bir edattır.','bilgi'),
  ('Yağmur dinene “kadar” bekledik.','edat','“Kadar”, sınır bildiren bir edattır.','dikkat'),
  ('Yorgundu “ama” yine de çalıştı.','bağlaç','',''),
  ('Havaya “göre” giyindik.','edat','“Göre”, “havaya” sözcüğüyle görev yapan bir edattır.','bilgi')],
 'D',lambda t:t=='bağlaç','Bağlaç olan sözcük.',
 'Tırnaklı sözcük iki cümleyi ya da iki yargıyı mı birbirine bağlıyor?',[B_EB],
 [AD('Ölçütü hatırla','Bağlaç iki cümleyi ya da iki sözcüğü bağlar; edat bir sözcükle birlikte görev yapar.','bağlaç: bağlar · edat: eşlik eder'),AD('Şıkları çöz','için, gibi, kadar, göre: her biri önündeki sözcüğe bağlı edattır.','A, B, C, E: edat'),AD('Bağlacı seç','D’de “ama”, “yorgundu” ve “yine de çalıştı” yargılarını birbirine bağlıyor.','D: bağlaç')],
 'İki ayrı yargıyı birbirine bağlayan sözcük bağlaçtır; tek bir sözcüğe eşlik eden edattır.')

# 0004 görev · zor · A
soru(Q,'0004','K-ST-04','zor','Aynı cümledeki iki sözcüğün sıfat ve zarf görevini birlikte belirler.',4,
 'Aşağıdaki cümlelerin hangisinde tırnak içindeki sözcüklerden ilki sıfat, ikincisi zarftır?',
 [('“Eski” çarşıyı “yavaş” gezdik.',('sıfat','zarf'),'',''),
  ('“Güzel” bir şarkıyı “anlamlı” bir sesle söyledi.',('sıfat','sıfat'),'İkisi de bir ismi niteler: güzel → şarkı, anlamlı → ses. İkisi de sıfattır.','dikkat'),
  ('“Hızlı” koşup “çabuk” yoruldu.',('zarf','zarf'),'İkisi de fiili niteler: hızlı koşmak, çabuk yorulmak. İkisi de zarftır.','dikkat'),
  ('“Yeşil” bahçeye “kırmızı” gül ekti.',('sıfat','sıfat'),'Yeşil → bahçe, kırmızı → gül: ikisi de isim niteler; sıfattır.','bilgi'),
  ('Çocuk “iyi” uyuyup “erken” kalktı.',('zarf','zarf'),'İkisi de fiili niteler: iyi uyumak, erken kalkmak. İkisi de zarftır.','bilgi')],
 'A',lambda t:t==('sıfat','zarf'),'İlki sıfat, ikincisi zarf olan sözcük çifti.',
 'Her tırnaklı sözcüğü ayrı ayrı ele al: hemen ardından isim mi fiil mi geliyor?',[B_SZ],
 [AD('Ölçütü yaz','Aranan çift: önce bir ismi niteleyen, sonra bir fiili niteleyen sözcük.','sıfat → isim · zarf → fiil'),AD('Her şıkkı çöz','B: güzel şarkı, anlamlı ses (iki sıfat). C: hızlı koşmak, çabuk yorulmak (iki zarf). D: yeşil bahçe, kırmızı gül (iki sıfat). E: iyi uyumak, erken kalkmak (iki zarf).','B, D: sıfat+sıfat · C, E: zarf+zarf'),AD('Aranan çifti seç','A’da “eski”, “çarşı” ismini niteler (sıfat); “yavaş”, “gezdik” fiilini niteler (zarf).','A: sıfat+zarf')],
 'İki sözcüklü sorularda her sözcüğün niteledikleri ayrı ayrı bulunur; ancak sonra çift değerlendirilir.')
bitir(Q)
