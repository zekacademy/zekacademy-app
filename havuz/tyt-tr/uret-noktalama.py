"""TYT Türkçe · Noktalama İşaretleri: 6 ana soru (hafif mod). Metinler özgündür."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from hafif_dilbilgisi import *
AD=A
KY='ÖSYM TYT Türkçe 2018–2026 (noktalama işaretleri) ve TDK Yazım Kılavuzu'
KARTLAR={
 'K-NOK-01':dict(alt='Nokta, Soru ve Ünlem İşareti',fikir='Cümlenin anlamına göre (bildirme, soru, ünlem) uygun bitiş işaretini belirlemek.',tuzak='Dolaylı soruya soru işareti, ünlem anlamlı cümleye nokta koymak.',zorluk='kolay',kalip='düz',adim=2,tipId='nok-bitis',kaynak=KY),
 'K-NOK-02':dict(alt='Dolaylı Soru ve Bitiş İşareti',fikir='Soru sözcüğü taşıyan ama soru anlamı olmayan cümleleri tanımak.',tuzak='Soru sözcüğü görünce soru işareti koymak.',zorluk='orta',kalip='düz',adim=3,tipId='nok-dolayli',kaynak=KY),
 'K-NOK-03':dict(alt='İki Nokta',fikir='İki noktanın açıklama ve sıralama öncesinde, tamamlanmış cümleden sonra kullanıldığını bilmek.',tuzak='İki noktayı cümlenin ortasında, yüklemi tamamlanmamış yerde kullanmak.',zorluk='orta',kalip='düz',adim=3,tipId='nok-ikinokta',kaynak=KY),
 'K-NOK-04':dict(alt='Kesme İşareti',fikir='Kesme işaretinin özel adlara gelen çekim eklerinde kullanıldığını, yapım eklerinde ve cins adlarda kullanılmadığını bilmek.',tuzak='Yapım ekinden önce kesme koymak; dil adına gelen eki kesmeyle ayırmak.',zorluk='orta',kalip='düz',adim=3,tipId='nok-kesme',kaynak=KY),
 'K-NOK-05':dict(alt='Noktalı Virgül',fikir='Noktalı virgülün birbiriyle ilgili cümleleri ya da öbekleri ayırmada kullanıldığını bilmek.',tuzak='Noktalı virgülü sıralı sözcükler ya da hitap sonrasında kullanmak.',zorluk='zor',kalip='düz',adim=4,tipId='nok-noktalivirgul',kaynak=KY),
 'K-NOK-06':dict(alt='Nokta (Kısaltma, Saat, Sayı)',fikir='Noktanın kısaltma, saat, tarih ve sayılarda kullanıldığı; kurum kısaltmalarında kullanılmadığı kuralını uygulamak.',tuzak='Büyük harfli kurum kısaltmalarına nokta koymak.',zorluk='zor',kalip='düz',adim=4,tipId='nok-nokta',kaynak=KY),
}
TIPLER={'nok-bitis':'Bitiş işaretleri','nok-dolayli':'Dolaylı soru','nok-ikinokta':'İki nokta','nok-kesme':'Kesme işareti','nok-noktalivirgul':'Noktalı virgül','nok-nokta':'Nokta'}
Q=kur('noktalama','Noktalama İşaretleri','tr|Noktalama İşaretleri',KARTLAR,TIPLER); Q.n=6
Y='yanlış'; D='doğru'
B_BIT=B('Bitiş işaretleri','nokta: bildirme cümleleri (Yarın gideceğim.) · soru işareti: soru anlamlı cümleler (Kim geldi?) · ünlem: sevinç, şaşkınlık, seslenme (Ne güzel çiçek!)')
B_DOL=B('Dolaylı soru','soru sözcüğü olsa da soru sorulmuyor, bilgi veriliyorsa nokta konur · “Ne zaman döneceğini sordu.” (nokta) – “Kim geldi?” (soru işareti)')
B_IKI=B('İki nokta','açıklama ya da sıralama yapılacağı zaman, cümle tamamlandıktan sonra konur · “Şu üç konu işlendi: tarih, coğrafya, felsefe.”')
B_KES=B('Kesme işareti','özel adlara gelen çekim ekleri kesmeyle ayrılır (Ahmet’in, 1938’de) · yapım ekleri ve dil/cins adları kesmeyle ayrılmaz (Ankaralı, Türkçeyi)')
B_NV=B('Noktalı virgül','birbirine anlamca bağlı cümleleri ayırır · “Birimiz kitap okuyor; ötekimiz müzik dinliyordu.” Sıralı sözcükler için virgül kullanılır')
B_NOK=B('Nokta','kısaltmalarda (Dr., Prof.), saat (14.30), tarih (12.05.2024) ve binlik sayılarda (1.250) kullanılır · TBMM, TDK gibi büyük harfli kurum kısaltmalarında kullanılmaz')

# 0001 bitiş · kolay · B
soru(Q,'0001','K-NOK-01','kolay','Cümlenin anlamına göre uygun bitiş işaretini belirler.',2,
 'Aşağıdaki cümlelerin hangisinin sonuna nokta (.) konulmalıdır?',
 [('Bu kadar yolu nasıl yürüdün','soru','Soru anlamı taşır; sonuna soru işareti konur.','bilgi'),
  ('Yarın okula erken gideceğim','bildirme','',''),
  ('Ne kadar güzel çiçekler','ünlem','Şaşkınlık ve beğeni bildirir; sonuna ünlem işareti konur.','bilgi'),
  ('Kapıyı kim açtı','soru','Soru cümlesidir; sonuna soru işareti konur.','dikkat'),
  ('Bu akşam bize gelecek misin','soru','Soru ekiyle sorulmuş bir sorudur; sonuna soru işareti konur.','dikkat')],
 'B',lambda t:t=='bildirme','Sonuna nokta konulması gereken cümle.',
 'Cümleyi bir bilgi mi veriyor, soru mu soruyor, yoksa duygu mu bildiriyor diye sınıfla.',[B_BIT],
 [AD('Cümleleri sınıfla','Her cümlenin bildirme, soru ya da ünlem anlamı taşıdığına bak.','3 tür'),AD('Soru ve ünlemleri ele','A, D, E soru anlamlı; C ünlem anlamlıdır.','A, D, E: ? · C: !'),AD('Bildirmeyi seç','B yalnızca bilgi verir; nokta ile biter.','B: .')],
 'Cümle bilgi veriyorsa nokta, soru soruyorsa soru işareti, duygu bildiriyorsa ünlem.')

# 0002 dolaylı soru · orta · D
soru(Q,'0002','K-NOK-02','orta','Soru sözcüğü taşıyan ama soru anlamı olmayan cümlede bitiş işaretini doğru kullanır.',3,
 'Aşağıdaki cümlelerin hangisinde noktalama yanlışı vardır?',
 [('Pazardan elma, armut, portakal ve muz aldık.',D,'Sıralı sözcükler virgülle ayrılmış, cümle noktayla bitmiş; noktalama doğrudur.','bilgi'),
  ('Evet, haklısın.',D,'“Evet” cevap sözcüğünden sonra virgül konur; noktalama doğrudur.','dikkat'),
  ('Toplantıda şu konular görüşülecek: bütçe, personel, eğitim.',D,'Sıralama öncesinde tamamlanmış cümleden sonra iki nokta kullanılmıştır; doğrudur.','bilgi'),
  ('Kimin geldiğini bilmiyorum?',Y,'',''),
  ('Ne güzel bir gün!',D,'Beğeni bildiren cümle ünlemle bitmiştir; doğrudur.','dikkat')],
 'D',lambda t:t==Y,'Noktalama yanlışı bulunan cümle.',
 'Soru sözcüğü olan cümlede gerçekten soru soruluyor mu, yoksa bilgi mi veriliyor?',[B_DOL],
 [AD('Her işareti sına','Virgül, iki nokta ve ünlem kurallarına göre A, B, C ve E’yi kontrol et.','A, B, C, E: doğru'),AD('Soru anlamını ara','D’deki “kimin” soru sözcüğü olsa da cümle soru sormaz, bir durumu bildirir (dolaylı soru).','D: bildirme'),AD('Yanlışı bul','Dolaylı soruda nokta konur; D’nin sonundaki soru işareti yanlıştır.','D: ? yerine .')],
 'Soru sözcüğü gördüğünde hemen soru işareti koyma; cevabı gerçekten bekleyen bir soru var mı?')

# 0003 iki nokta · orta · A
soru(Q,'0003','K-NOK-03','orta','İki noktanın doğru yerde kullanıldığı cümleyi belirler.',3,
 'Aşağıdaki cümlelerin hangisinde iki nokta (:) yerinde kullanılmıştır?',
 [('Toplantıda şu konular ele alındı: bütçe, personel ve eğitim.',D,'',''),
  ('Dün: arkadaşlarımla sinemaya gittim.',Y,'İki nokta, cümlenin tamamlanmadığı yerde kullanılmış; zaman zarfından sonra gelmez.','bilgi'),
  ('Gitmeden önce: bana haber ver.',Y,'Cümle devam ederken yüklemden önce iki nokta konmaz.','bilgi'),
  ('Annem pazardan: elma, armut ve üzüm aldı.',Y,'İki noktadan önceki bölüm tamamlanmış bir cümle değildir; yüklem sonradan gelir.','dikkat'),
  ('Okula: servisle gidiyorum.',Y,'Cümle tamamlanmadan, yer bildiren sözcükten sonra iki nokta konmaz.','dikkat')],
 'A',lambda t:t==D,'İki noktanın yerinde kullanıldığı cümle.',
 'İki noktadan önceki bölüm, kendi başına tamamlanmış bir cümle mi?',[B_IKI],
 [AD('Kuralı hatırla','İki nokta, tamamlanmış bir cümleden sonra açıklama ya da sıralama gelecekse konur.','tam cümle + : + açıklama'),AD('Şıkları ele','B, C, D ve E’de iki noktadan önceki kısım tamamlanmış bir cümle değil; yüklem sonradan geliyor.','B, C, D, E: yanlış'),AD('Doğruyu seç','A’da “Toplantıda şu konular ele alındı” cümlesi tamamdır; ardından sıralama gelir.','A: doğru')],
 'İki noktadan önceki bölümü tek başına oku; cümle bitmişse ve açıklama ya da sıralama geliyorsa yerindedir.')

# 0004 kesme · orta · E
soru(Q,'0004','K-NOK-04','orta','Kesme işaretinin yanlış kullanıldığı cümleyi belirler.',3,
 'Aşağıdaki cümlelerin hangisinde kesme işareti (’) yanlış kullanılmıştır?',
 [('Ahmet’in kitabını sınıfta unutmuş.',D,'Özel ada gelen tamlayan eki kesmeyle ayrılmıştır; doğrudur.','bilgi'),
  ('1938’de Atatürk’ü kaybettik.',D,'Sayıya ve özel ada gelen çekim ekleri kesmeyle ayrılır; doğrudur.','bilgi'),
  ('Yabancılara Türkçeyi öğretiyor.',D,'Dil adlarına gelen ekler kesmeyle ayrılmaz; kesme konmaması doğrudur.','dikkat'),
  ('Bahçeden Hatice’ye gül topladım.',D,'Özel ada gelen yönelme eki kesmeyle ayrılmıştır; doğrudur.','bilgi'),
  ('Ankara’lı arkadaşım bizi ziyarete geldi.',Y,'','')],
 'E',lambda t:t==Y,'Kesme işareti yanlış kullanılan cümle.',
 'Kesme işareti çekim eklerinde kullanılır; yapım eklerinde kullanılır mı?',[B_KES],
 [AD('Kuralı hatırla','Özel adlara gelen çekim ekleri kesmeyle ayrılır; yapım ekleri ayrılmaz.','Ahmet’in ✓ · Ankaralı ✓'),AD('Şıkları ele','A, B, D’de çekim ekleri kesmeyle ayrılmış. C’de “Türkçeyi” dil adı olduğundan kesme yok.','A, B, C, D: doğru'),AD('Yanlışı bul','E’deki “-lı” bir yapım ekidir; “Ankaralı” kesme işaretsiz yazılmalıdır.','E: Ankaralı')],
 'Ek yeni bir sözcük (sıfat, isim) türetiyorsa kesme kullanma; yalnız çekim ekinde kullan.')

# 0005 noktalı virgül · zor · C
soru(Q,'0005','K-NOK-05','zor','Noktalı virgülün yerinde kullanıldığı cümleyi belirler.',4,
 'Aşağıdaki cümlelerin hangisinde noktalı virgül (;) yerinde kullanılmıştır?',
 [('Bahçede gül; lale; sümbül açmış.',Y,'Sıralı sözcükler virgülle ayrılır; noktalı virgül yerinde değildir.','bilgi'),
  ('Sevgili Ayşe; seni çok özledim.',Y,'Hitap sözcüğünden sonra virgül konur; noktalı virgül yanlıştır.','bilgi'),
  ('Öğrencilerin bir kısmı kütüphanede ders çalışıyor; bir kısmı ise spor salonunda antrenman yapıyor.',D,'',''),
  ('Yarın; sınavımız var.',Y,'Özne ile yüklem arasında noktalı virgül kullanılmaz.','dikkat'),
  ('Okuduğum kitap; çok güzeldi.',Y,'Özne ile yüklem birbirinden noktalı virgülle ayrılmaz.','dikkat')],
 'C',lambda t:t==D,'Noktalı virgülün yerinde kullanıldığı cümle.',
 'Noktalı virgül, birbiriyle ilgili iki ayrı cümleyi (yargıyı) ayırır; sıralı sözcükleri ya da hitabı ayırmaz.',[B_NV],
 [AD('Kuralı hatırla','Noktalı virgül, birbirine anlamca bağlı cümleleri birbirinden ayırır.','cümle ; cümle'),AD('Şıkları ele','A sıralı sözcük, B hitap, D ve E özne–yüklem; hiçbirinde ayrılacak iki cümle yok.','A, B, D, E: yanlış'),AD('Doğruyu seç','C’de iki ayrı cümle birbiriyle ilgili ve noktalı virgülle ayrılmış.','C: doğru')],
 'Noktalı virgülün iki yanında da kendi başına anlamlı birer cümle arıyorsan doğru yoldasın.')

# 0006 nokta · zor · B
soru(Q,'0006','K-NOK-06','zor','Noktanın kısaltma, saat, sayı ve tarihte kullanımını; kurum kısaltmasında kullanılmadığını bilir.',4,
 'Aşağıdaki cümlelerin hangisinde nokta (.) yanlış kullanılmıştır?',
 [('Prof. Dr. Ayşe Yılmaz konferansta konuştu.',D,'Unvan kısaltmalarının sonuna nokta konur; doğrudur.','bilgi'),
  ('Bu belgeyi T.B.M.M. Kütüphanesi’nden aldım.',Y,'',''),
  ('Kitabın fiyatı 1.250 TL idi.',D,'Binlik sayılarda basamak ayırmak için nokta kullanılır; doğrudur.','bilgi'),
  ('Toplantı saat 14.30’da başlayacak.',D,'Saat ile dakika arasında nokta kullanılır; doğrudur.','dikkat'),
  ('Mektubu 12.05.2024 tarihinde gönderdi.',D,'Tarihte gün, ay ve yıl noktayla ayrılabilir; doğrudur.','dikkat')],
 'B',lambda t:t==Y,'Nokta yanlış kullanılan cümle.',
 'Büyük harfle yazılan kurum kısaltmalarının içinde nokta olur mu?',[B_NOK],
 [AD('Kuralları hatırla','Nokta; unvan kısaltmalarında, saat, tarih ve binlik sayılarda kullanılır.','Dr. · 14.30 · 1.250'),AD('Şıkları ele','A, C, D ve E’de nokta yerinde: unvan, sayı, saat, tarih.','A, C, D, E: doğru'),AD('Yanlışı bul','B’de kurum kısaltması “TBMM” noktasız yazılmalıdır.','B: TBMM')],
 'Büyük harfli kurum kısaltmaları (TDK, TBMM) noktasız yazılır; unvan kısaltmaları (Dr., Prof.) noktalı yazılır.')
bitir(Q)
