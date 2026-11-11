"""TYT Türkçe · Noktalama İşaretleri (2. yarı): kesme, tırnak, yay ayraç, çizgi, üç nokta, soru/ünlem. 24 soru (hafif mod)."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from hafif_db import *
AD=A
KY='ÖSYM TYT Türkçe 2018–2026 · Bilgi Sarmal Dil Bilgisi SB (ÖSYM Tipi) · TDK Yazım Kılavuzu'
def K(alt,fikir,tuzak,zor,kalip,adim,tip): return dict(alt=alt,fikir=fikir,tuzak=tuzak,zorluk=zor,kalip=kalip,adim=adim,tipId=tip,kaynak=KY)
KARTLAR={
 'K-DBNKB-01':K('Kesme İşareti · Özel Ad ve Yapım Eki','Özel adlara gelen çekim eklerini kesmeyle ayırmak; cins adlara, dil adlarına ve yapım eklerine kesme koymamak.','Yapım ekinden (Ankaralı) ya da dil adından (Türkçeyi) önce kesme koymak.','orta','öncüllü',3,'dnkb-kesme'),
 'K-DBNKB-02':K('Kesme İşareti · Kurum, Kısaltma, Sayı','Kurum, kurul, merkez adlarına gelen ekleri kesmesiz yazmak; kısaltma ve rakamlı sayılara gelen ekleri kesmeyle ayırmak.','Kurum adına kesme koymak; kurum kısaltmasına ya da sayıya gelen eki kesmesiz yazmak.','zor','öncüllü',4,'dnkb-kesme-kurum'),
 'K-DBNKB-03':K('Tırnak İşareti','Alıntı, vurgulanan söz ve eser adlarında tırnak kullanılır; sıradan özel ad ve cins adlara tırnak getirilmez.','Her özel adı ya da önemli saydığı sözcüğü tırnağa almak.','orta','öncüllü',3,'dnkb-tirnak'),
 'K-DBNKB-04':K('Yay Ayraç','Yay ayraç açıklama, tiyatro yönergesi ve kesinsizlik (?) ya da alay (!) için kullanılır; cümlenin temel ögesi ayraca alınmaz.','Kesin bilgiye (?) koymak; yüklemi ya da temel ögeyi ayraç içine almak.','orta','öncüllü',3,'dnkb-ayrac'),
 'K-DBNKB-05':K('Kısa Çizgi ve Uzun Çizgi','Kısa çizgi aralık, karşıtlık ve satır sonunda hece bölmede; uzun çizgi konuşma başında kullanılır.','Kısa çizgiyi bağlaç ya da ek yerine kullanmak; uzun çizgiyi cümle ortasına koymak; heceyi yanlış yerden bölmek.','orta','öncüllü',3,'dnkb-cizgi'),
 'K-DBNKB-06':K('Üç Nokta','Üç nokta bitmemiş cümlede, söylenmek istenmeyen sözün yerinde ve sayılabilecek başka örnekleri bulunan sözcüklerden sonra kullanılır.','Sayma sonunda virgül koymak ya da bitmiş cümlenin sonuna üç nokta koymak.','orta','öncüllü',3,'dnkb-uc-nokta'),
 'K-DBNKB-07':K('Soru ve Ünlem İşareti','Soru anlamı taşımayan (dolaylı soru) cümleler nokta ile biter; soru anlamlı cümle soru işaretiyle, duygu bildiren söz ünlemle biter.','Soru ekini ya da soru sözcüğünü görünce soru işareti koymak.','zor','öncüllü',4,'dnkb-soru-unlem'),
}
TIPLER={'dnkb-kesme':'Kesme işareti (özel ad, yapım eki)','dnkb-kesme-kurum':'Kesme işareti (kurum, kısaltma, sayı)','dnkb-tirnak':'Tırnak işareti','dnkb-ayrac':'Yay ayraç','dnkb-cizgi':'Kısa ve uzun çizgi','dnkb-uc-nokta':'Üç nokta','dnkb-soru-unlem':'Soru ve ünlem işareti'}
Q=kur('dnoktab','Noktalama İşaretleri','tr|Noktalama İşaretleri',KARTLAR,TIPLER); Q.n=24
B_KES=B('Kesme işareti','özel adlara gelen çekim ekleri kesmeyle ayrılır (Kerem’in, Erzurum’a) · yapım eki, dil adı ve cins ad kesmeyle ayrılmaz (Ankaralı, Türkçeyi)')
B_KUR=B('Kurum adı, kısaltma, sayı','kurum, kurul, merkez adlarına gelen ek kesmesiz yazılır (Türk Dil Kurumuna) · kısaltma ve rakamlı sayıya gelen ek kesmeyle ayrılır (TDK’ye, 1938’de)')
B_TIR=B('Tırnak işareti','alıntı, vurgulanan söz ve eser adlarında kullanılır (“Gri Bulutlar” adlı şiir, “sabır” sözcüğü) · sıradan özel ad ve cins ada konmaz')
B_AYR=B('Yay ayraç','açıklama, tiyatro yönergesi, kesinsizlik (?) ve alay (!) için kullanılır · cümlenin temel ögesi (yüklem gibi) ayraç içine alınmaz')
B_CIZ=B('Kısa ve uzun çizgi','kısa çizgi: aralık (12-14 Mart, Ankara-İstanbul), karşıtlık (Doğu-Batı), satır sonunda heceyi bölme · uzun çizgi: konuşma başı (— Geldin mi?) ve ara sözün iki yanı (Dedem — yaşlı bir çınar — gelir.)')
B_UC=B('Üç nokta','bitmemiş cümle, söylenmek istenmeyen söz, sayılabilecek başka örnekler (gül, lale, sümbül...) için kullanılır')
B_SOR=B('Soru ve ünlem','soru anlamlı cümle “?” ile, duygu bildiren söz “!” ile biter · soru anlamı olmayan (dolaylı) cümle nokta ile biter (“…gelir misin diye sordu.”)')
def S(kural,ex,sik,islem,son,sonislem): return [AD('Kuralı hatırla',kural,ex),AD('Seçenekleri tek tek sına',sik,islem),AD('Sonucu bul',son,sonislem)]

# 0001 kolay · A · kesme
soru(Q,'0001','K-DBNKB-01','kolay','Kesme işaretinin özel ada gelen ekte kullanıldığı cümleyi belirler.',2,
 'Hangi cümlede kesme işaretinden doğru yararlanılmıştır?',
 [('Kerem’in defterini masanın üstünde buldum.',D,'',''),
  ('Bahçedeki çiçekleri sabah’ları suluyorum.',Y,'“Sabah” cins addır; cins adlara gelen ek kesmeyle ayrılmaz.','bilgi'),
  ('Çocuklar ağaç’ın gölgesinde oyun oynadı.',Y,'“Ağaç” cins addır; kesme yalnız özel adlardan sonra kullanılır.','bilgi'),
  ('Yaz tatilinde deniz’e girmeyi çok seviyorum.',Y,'“Deniz” özel ad değil cins addır; yönelme eki kesmesiz yazılır.','dikkat'),
  ('Öğretmenimiz yarın okul’a erken gelecek.',Y,'“Okul” cins addır; kesme konmaz, “okula” yazılır.','dikkat')],
 'A',lambda t:t==D,'Kesme işaretinin yerinde kullanıldığı cümle.',
 'Kesmeli yazılan sözcüklerin hangisi bir kişi ya da yer adı?',[B_KES],
 S('Kesme, yalnız özel adlara gelen çekim ekini ayırır.','Kerem’in ✓ · okul’a ✗','B, C, D, E’de “sabah, ağaç, deniz, okul” cins addır; kesme gereksiz.','B, C, D, E: ✗','A’da “Kerem” özel addır, tamlayan eki kesmeyle ayrılmıştır.','A: ✓'),
 'Eki alan sözcük kişi ya da yer adı değilse kesme koyma.')

# 0002 orta · C · kesme
soru(Q,'0002','K-DBNKB-01','orta','Yapım ekinden önce kesme konulmayacağını bilir.',3,
 'Aşağıdaki cümlelerin hangisinde kesme işaretiyle ilgili bir yanlışlık yapılmıştır?',
 [('Yaz tatilini Ayvalık’ta geçirmeyi planlıyoruz.',D,'Yer adına gelen bulunma eki kesmeyle ayrılmıştır; doğrudur.','bilgi'),
  ('Elif’e bu akşam Kerem’le buluşacağını söyledim.',D,'Kişi adlarına gelen yönelme ve ilgi eki kesmeyle ayrılmıştır; doğrudur.','dikkat'),
  ('Karadeniz’li balıkçılar sabah erkenden denize açıldı.',Y,'',''),
  ('Kızılırmak’ın kıyısında küçük bir köy bulunuyor.',D,'Akarsu adına gelen tamlayan eki kesmeyle ayrılmıştır; doğrudur.','bilgi'),
  ('Atatürk’ün sözleri bugün de yol göstermeye devam ediyor.',D,'Özel ada gelen tamlayan eki kesmeyle ayrılmıştır; doğrudur.','dikkat')],
 'C',lambda t:t==Y,'Kesme işareti yanlış kullanılan cümle.',
 '“-lı” eki sözcüğe yeni anlam mı katıyor, yoksa yalnız sözcüğü cümleye mi bağlıyor?',[B_KES],
 S('Çekim ekleri kesmeyle ayrılır; yapım ekleri ayrılmaz.','Ayvalık’ta ✓ · Karadenizli ✓','A, B, D, E’de ekler çekim ekidir ve özel adlardan sonra kesmeyle ayrılmış.','A, B, D, E: ✓','C’deki “-lı” yapım ekidir (Karadeniz → Karadenizli); kesme konmamalıdır.','C: Karadenizli'),
 'Ek yeni bir sözcük türetiyorsa (-lı, -cı, -leş) kesme koyma.')

# 0003 orta · E · kesme · numaralı
soru(Q,'0003','K-DBNKB-01','orta','Numaralı parçada dil adına gelen ekin kesmeyle ayrılamayacağını bilir.',3,
 'Geçen yaz ailemle Erzurum’a (I) gittik. Palandöken’in (II) yamaçlarında yürüdük, geceleri Kerem’in (III) dayısının evinde kaldık. Dayısı bize kızı Ayşe’yi (IV) tanıttı. Ayşe Rusça’yı (V) çok iyi bilen komşusunu da çağırdı.\n\nBu parçada numaralanmış sözcüklerden hangisinde kesme işareti yanlış kullanılmıştır?',
 [('I',D,'Yer adına gelen yönelme eki kesmeyle ayrılmıştır; doğrudur.','bilgi'),
  ('II',D,'Dağ adına gelen tamlayan eki kesmeyle ayrılmıştır; doğrudur.','bilgi'),
  ('III',D,'Kişi adına gelen tamlayan eki kesmeyle ayrılmıştır; doğrudur.','dikkat'),
  ('IV',D,'Kişi adına gelen belirtme eki kesmeyle ayrılmıştır; doğrudur.','dikkat'),
  ('V',Y,'','')],
 'E',lambda t:t==Y,'Kesme işareti yanlış kullanılan numaralı yer.',
 'Hangi numaralı sözcük bir kişi ya da yer adı değil, bir dil adı?',[B_KES],
 S('Dil adları cins ad sayılır; ek kesmeyle ayrılmaz.','Rusçayı ✓ · Rusça’yı ✗','I–IV özel ad (Erzurum, Palandöken, Kerem, Ayşe) + çekim eki; V dil adı.','I–IV: ✓ · V: ✗','V’teki “Rusça’yı”, kesmesiz “Rusçayı” yazılmalıdır.','V: Rusçayı'),
 'Dil adlarına (Türkçe, Rusça) gelen ek kesmeyle ayrılmaz.',kalip='öncüllü')

# 0004 zor · B · kesme · numaralı
soru(Q,'0004','K-DBNKB-01','zor','Numaralı parçada kesme getirilmesi gereken tek yeri bulur.',4,
 'Kerem Bursalı (I) dedesinin anlattığı hikâyeleri dinlemek için yaz boyunca Uludağa (II) çıktı. Orada Türkçeyi (III) iyi bilen yabancı konukların da bulunduğunu öğrendi. Dönüşte Millî Eğitim Bakanlığından (IV) aldığı belgeyle Dil Derneğine (V) başvurdu.\n\nBu parçada numaralanmış sözcüklerden hangisine kesme işareti (’) getirilmelidir?',
 [('I',D,'“Bursalı” yapım ekiyle türemiştir; kesme konmaz, yazılışı doğrudur.','bilgi'),
  ('II',Y,'',''),
  ('III',D,'Dil adlarına gelen ek kesmeyle ayrılmaz; “Türkçeyi” yazılışı doğrudur.','bilgi'),
  ('IV',D,'Bakanlık bir kurumdur; kurum adına gelen ek kesmesiz yazılır.','dikkat'),
  ('V',D,'Dernek bir kuruluştur; kuruluş adına gelen ek kesmesiz yazılır.','dikkat')],
 'B',lambda t:t==Y,'Kesme işareti getirilmesi gereken numaralı yer.',
 'Beş sözcükten yalnız biri kurum, dil ya da yapım ekiyle ilgisiz, düz bir özel ad (dağ) + çekim eki.',[B_KES,B_KUR],
 S('Özel ad + çekim eki → kesme; yapım eki, dil adı, kurum adı → kesme yok.','Uludağ’a ✓ · Bursalı ✓','I yapım eki, III dil adı, IV ve V kurum/kuruluş adı; hiçbirine kesme gerekmez.','I, III, IV, V: kesmesiz doğru','II’de “Uludağ” dağ adıdır ve yönelme ekini kesmeyle ayırmak gerekir.','II: Uludağ’a'),
 'Önce kurum, dil adı ve yapım ekini ele; geriye kalan özel ad + çekim ekidir.',kalip='öncüllü')

# 0005 orta · D · kesme · kurum
soru(Q,'0005','K-DBNKB-02','orta','Kurum adına gelen ekin kesmeyle ayrılmadığını bilir.',3,
 'Kesme işareti konusunda yanlış yapılan cümle aşağıdakilerden hangisidir?',
 [('Bu yıl Türk Dil Kurumuna iki yeni uzman atandı.',D,'Kurum adına gelen ek kesmesiz yazılır; doğrudur.','bilgi'),
  ('Hacettepe Üniversitesinde okuyan kuzenim bize geldi.',D,'Üniversite bir kurumdur; ek kesmesiz yazılır, doğrudur.','bilgi'),
  ('Ablam Ankara Büyükşehir Belediyesinde göreve başladı.',D,'Belediye bir kurumdur; ek kesmesiz yazılır, doğrudur.','dikkat'),
  ('Yarışmayı Sağlık Bakanlığı’nın yetkilileri düzenledi.',Y,'',''),
  ('Mektubu Elif’in teyzesine posta yoluyla gönderdik.',D,'Kişi adına gelen tamlayan eki kesmeyle ayrılmıştır; doğrudur.','dikkat')],
 'D',lambda t:t==Y,'Kesme işareti yanlış kullanılan cümle.',
 'Kesmeli yazılan sözcüğün başındaki ad bir kişi mi, yoksa bir kurum mu?',[B_KUR],
 S('Kurum ve kuruluş adlarına gelen ekler kesmeyle ayrılmaz.','Türk Dil Kurumuna ✓','A, B, C’de kurum adına ek kesmesiz gelmiş; E’de kişi adı + ek kesmeli.','A, B, C, E: ✓','D’de “Sağlık Bakanlığı’nın” bir kurum adıdır; kesme konmaz.','D: Bakanlığının'),
 'Kurum adı + ek: kesme yok; kişi ya da yer adı + ek: kesme var.')

# 0006 zor · A · kesme · kısaltma
soru(Q,'0006','K-DBNKB-02','orta','Kısaltmaya gelen ekin kesmeyle ayrıldığı cümleyi bulur.',3,
 'Kesme işareti kullanımı bakımından doğru olan cümle aşağıdakilerden hangisidir?',
 [('Başvuru sonuçları TDK’ye posta yoluyla iletildi.',D,'',''),
  ('Salondaki öğrenci sayısı yüz’ü çoktan geçmişti.',Y,'Yazıyla yazılan sayıya gelen ek kesmeyle ayrılmaz; “yüzü” yazılır.','bilgi'),
  ('Başvurularını Etik Kurulu’na sabah erkenden iletti.',Y,'Kurul adlarına gelen ek kesmeyle ayrılmaz; “Etik Kuruluna” yazılır.','bilgi'),
  ('Okulda öğrencilere Türkçe’nin ses yapısı anlatıldı.',Y,'Dil adına gelen ek kesmeyle ayrılmaz; “Türkçenin” yazılır.','dikkat'),
  ('Bize misafir gelen aile Muğla’lı çıktı.',Y,'“-lı” yapım ekidir; kesme konmaz, “Muğlalı” yazılır.','dikkat')],
 'A',lambda t:t==D,'Kesme işaretinin yerinde kullanıldığı cümle.',
 'Kurum adı kesmesiz, ama kurumun kısaltması başka bir kural izler.',[B_KUR,B_KES],
 S('Kısaltmaya gelen ek, okunuşa göre yazılır ve kesmeyle ayrılır.','TDK’ye ✓ · yüzü ✓','B yazıyla sayı, C kurul, D dil adı, E yapım eki: dördünde de kesme yanlış.','B, C, D, E: ✗','A’da kısaltma “TDK” + yönelme eki kesmeyle ayrılmıştır.','A: TDK’ye'),
 'Kurum adı kesmesiz, kurum kısaltması ve rakamlı sayı kesmeli yazılır.')

# 0007 zor · C · kesme · numaralı
soru(Q,'0007','K-DBNKB-02','zor','Numaralı parçada kurum adına konan yanlış kesmeyi bulur.',4,
 'Yarışma 2026’da (I) Ankara’da (II) yapıldı. Sonuçlar Türk Dil Kurumu’na (III) bildirildi. Toplam 450’yi (IV) aşan katılımcı arasından birinci olan Elif ödülünü bir törende TDK’de (V) görevli bir uzmandan aldı.\n\nBu parçada numaralanmış sözcüklerden hangisinde kesme işareti yanlış kullanılmıştır?',
 [('I',D,'Rakamla yazılan sayıya gelen ek kesmeyle ayrılır; doğrudur.','bilgi'),
  ('II',D,'Yer adına gelen bulunma eki kesmeyle ayrılır; doğrudur.','bilgi'),
  ('III',Y,'',''),
  ('IV',D,'Rakamla yazılan sayıya gelen ek kesmeyle ayrılır; doğrudur.','dikkat'),
  ('V',D,'Kısaltmaya gelen ek kesmeyle ayrılır; doğrudur.','dikkat')],
 'C',lambda t:t==Y,'Kesme işareti yanlış kullanılan numaralı yer.',
 'Hangi numara, kısaltma ya da sayı değil de tam bir kurum adı taşıyor?',[B_KUR],
 S('Rakamlı sayı, kısaltma, yer adı + ek → kesme; kurum adı + ek → kesme yok.','2026’da ✓ · TDK’de ✓ · Kurumuna ✓','I ve IV rakamlı sayı, II yer adı, V kurum kısaltması (TDK); kesmeleri yerinde.','I, II, IV, V: ✓','III’te “Türk Dil Kurumu” tam bir kurum adıdır; ek kesmesiz yazılmalıdır.','III: Kurumuna'),
 'Kurumun açık adına kesme yok, kısaltmasına var: Türk Dil Kurumuna / TDK’ye.',kalip='öncüllü')

# 0008 kolay · E · tırnak
soru(Q,'0008','K-DBNKB-03','kolay','Eser adının tırnak içinde yazıldığı cümleyi belirler.',2,
 'Tırnak işaretinin yerinde kullanıldığı cümle aşağıdakilerden hangisidir?',
 [('Dün akşam arkadaşım “Kerem” ile birlikte sinemaya gittik.',Y,'Sıradan bir kişi adı tırnağa alınmaz.','bilgi'),
  ('Kitaplığın en üst rafındaki “kitapları” sabah erkenden topladım.',Y,'Sıradan bir cins ad tırnağa alınmaz; vurgu ya da alıntı yoktur.','bilgi'),
  ('Annem pazardan “elma” ile birlikte taze armut da aldı.',Y,'Cins ada gereksiz tırnak konmuş; tırnak gerektiren bir durum yok.','dikkat'),
  ('Kardeşim yarın “sabah” erkenden kalkıp okula gidecek.',Y,'Zaman bildiren sıradan sözcük tırnağa alınmaz.','dikkat'),
  ('Elif “Kırlangıç Mevsimi” adlı şiiri sınıfta arkadaşlarına okudu.',D,'','')],
 'E',lambda t:t==D,'Tırnak işaretinin yerinde kullanıldığı cümle.',
 'Tırnak içine alınan sözcükler arasında bir eser adı var mı?',[B_TIR],
 S('Eser adları, alıntılar ve vurgulanan sözler tırnak içine alınır.','“Kırlangıç Mevsimi” ✓','A–D’de tırnaklı sözcükler sıradan ad ya da cins ad; tırnağı gerektirmiyor.','A, B, C, D: ✗','E’de “Kırlangıç Mevsimi” bir şiir adıdır; tırnak yerindedir.','E: ✓'),
 'Tırnağa kural olarak eser adı, alıntı ya da özellikle vurgulanan söz girer.')

# 0009 orta · B · tırnak
soru(Q,'0009','K-DBNKB-03','orta','Tırnak işaretinin gereksiz kullanıldığı cümleyi belirler.',3,
 'Aşağıdaki cümlelerin hangisinde tırnağa gereksiz yere başvurulmuştur?',
 [('Kardeşim konuşmasında “sabır” sözcüğünü üç kez kullandı.',D,'Vurgulanan söz tırnağa alınmıştır; doğrudur.','bilgi'),
  ('Bu yıl tatilimizi “Antalya”da geçirmeyi düşünüyoruz.',Y,'',''),
  ('Elif “Yağmurdan Sonra” adlı romanı bir günde bitirdi.',D,'Eser adı tırnağa alınmıştır; doğrudur.','bilgi'),
  ('Sınıfta “mütevazı” sözcüğünün anlamını birlikte tartıştık.',D,'Üzerinde durulan sözcük tırnağa alınmıştır; doğrudur.','dikkat'),
  ('Öğretmenimiz “Okumak insanı geliştirir” diyerek konuşmasına başladı.',D,'Alıntılanan söz tırnağa alınmıştır; doğrudur.','dikkat')],
 'B',lambda t:t==Y,'Tırnak işareti yanlış kullanılan cümle.',
 'Tırnaktaki sözcük alıntı, vurgulanan söz ya da eser adı mı?',[B_TIR],
 S('Alıntı, vurgu ve eser adı tırnak ister; yer adı istemez.','“sabır” ✓ · “Antalya” ✗','A, C, D, E’de tırnak sırasıyla vurgu, eser adı, üzerinde durulan sözcük ve alıntı için kullanılmış.','A, C, D, E: ✓','B’de “Antalya” sıradan bir yer adıdır; tırnağa alınmaz.','B: Antalya’da'),
 'Özel ad olması tırnak gerektirmez; tırnak vurgu, alıntı ve eser adı içindir.')

# 0010 zor · D · tırnak · numaralı
soru(Q,'0010','K-DBNKB-03','zor','Numaralı parçada gereksiz tırnağı bulur.',4,
 'Öğretmen tahtaya “Gri Bulutlar” (I) adlı şiirin ilk dizesini yazdı. Ardından “özlem” (II) sözcüğünün anlamını sordu. Kerem bu sözün “hasret” (III) sözcüğüyle yakın anlamlı olduğunu söyledi. Ders bitince Elif “yarın” (IV) gelemeyeceğini açıkladı; Kerem ise “Yaz Yağmuru” (V) adlı kitabı alacağını belirtti.\n\nBu parçada numaralanmış yerlerden hangisinde tırnak işareti gereksiz kullanılmıştır?',
 [('I',D,'Şiir adı tırnağa alınmıştır; yerindedir.','bilgi'),
  ('II',D,'Anlamı sorulan sözcük tırnağa alınmıştır; yerindedir.','bilgi'),
  ('III',D,'Karşılaştırılan sözcük tırnağa alınmıştır; yerindedir.','dikkat'),
  ('IV',Y,'',''),
  ('V',D,'Kitap adı tırnağa alınmıştır; yerindedir.','dikkat')],
 'D',lambda t:t==Y,'Tırnak işareti gereksiz kullanılan numaralı yer.',
 'Tırnaklı sözcüklerden hangisi eser adı, üzerinde durulan söz ya da alıntı değil?',[B_TIR],
 S('Tırnak; eser adı, vurgulanan söz ve alıntı içindir.','“Gri Bulutlar” ✓ · “yarın” ✗','I ve V eser adı, II ve III üzerinde durulan sözcük.','I, II, III, V: ✓','IV’te “yarın” sıradan bir zaman sözcüğüdür; vurgulanmadığı için tırnak gereksizdir.','IV: ✗'),
 'Sıradan zaman, yer ve kişi sözlerini tırnağa alma; tırnağı eser adı, alıntı ve vurgu için sakla.',kalip='öncüllü')

# 0011 kolay · A · ayraç
soru(Q,'0011','K-DBNKB-04','kolay','Yay ayracın tiyatro yönergesi olarak kullanıldığı cümleyi belirler.',2,
 'Aşağıdaki cümlelerin hangisinde yay ayraç, tiyatro eserlerindeki yönerge amacıyla kullanılmıştır?',
 [('AYŞE (kapıyı yavaşça açarak) Yine mi geç kaldın?',D,'',''),
  ('Kitap 1950 (?) yılında basılmış, ama sayfaları sapasağlam.',Y,'Ayraç içindeki soru işareti kesinsizlik bildirir; yönerge değildir.','bilgi'),
  ('Ünlü bilgin (!) harita okumayı bile beceremedi.',Y,'Ayraç içindeki ünlem alay bildirir; yönerge değildir.','bilgi'),
  ('Sınıfın en küçüğü Elif (yedi yaşında) yarışmayı kazandı.',Y,'Ayraç içi bir açıklama ekler; sahne yönergesi değildir.','dikkat'),
  ('Okulumuzun bahçesindeki ağaç (yaklaşık yüz yaşında) çok değerlidir.',Y,'Ayraç içi açıklama bilgisidir; sahne yönergesi değildir.','dikkat')],
 'A',lambda t:t==D,'Yay ayracın tiyatro yönergesi olarak kullanıldığı cümle.',
 'Konuşan kişinin adı büyük harfle yazılıp hareketi ayraçla bildirilen cümleyi ara.',[B_AYR],
 S('Tiyatroda konuşan kişinin adından sonra hareketi ayraç içinde yazılır.','AYŞE (kapıyı açarak) …','B kesinsizlik, C alay, D ve E açıklama amacıyla ayraç kullanıyor.','B: (?) · C: (!) · D, E: açıklama','A’da konuşan kişi AYŞE’dir; ayraç içi sahne yönergesidir.','A: yönerge'),
 'Konuşan kişinin adından sonraki ayraç tiyatro yönergesidir.')

# 0012 orta · C · ayraç
soru(Q,'0012','K-DBNKB-04','orta','Kesin bilgiye (?) konulamayacağını bilir.',3,
 'Aşağıdaki cümlelerin hangisinde yay ayraç içindeki soru işareti yersiz kullanılmıştır?',
 [('Bu evin 1890 (?) yılında yapıldığını söylüyorlar.',D,'Tarih kesin değil, söylentiye dayanıyor; (?) yerindedir.','bilgi'),
  ('Mektubu yazan kişinin adı Selim (?) olarak okunuyor.',D,'Okunuşu belirsiz ad için kesinsizlik işareti yerindedir.','bilgi'),
  ('Cumhuriyet 29 Ekim 1923 (?) tarihinde ilan edildi.',Y,'',''),
  ('Çınarın yaşı 400 (?) olarak hesaplanıyor.',D,'Yaş kesin değil, hesaba dayanıyor; (?) yerindedir.','dikkat'),
  ('Şiirin yazılış tarihi 1975 (?) olarak gösteriliyor.',D,'Tarih kesin değil, “gösteriliyor” denmiş; (?) yerindedir.','dikkat')],
 'C',lambda t:t==Y,'Ayraç içindeki soru işareti yersiz kullanılan cümle.',
 'Ayraç içindeki “?” bilgiden emin olunmadığını bildirir; bilgi kesin mi?',[B_AYR],
 S('Ayraç içi “?”, bilginin kesin olmadığını bildirir.','1890 (?) → emin değiliz','A, B, D, E’de tarih, ad ya da yaş belirsiz; söylenti ve tahmin var.','A, B, D, E: ✓','C’deki 29 Ekim 1923 kesin ve bilinen bir tarihtir; (?) yersizdir.','C: ✗'),
 'Bilgi kesinse ayraç içine (?) konmaz.')

# 0013 zor · E · ayraç · numaralı cümle
soru(Q,'0013','K-DBNKB-04','zor','Yay ayraç içine yüklem alınamayacağını bilir.',4,
 'I. Dedem köye 1960 (?) yılında yerleştiklerini anlatırdı.\nII. Çınar ağacının (yüz yaşını aşkın) gölgesinde herkes dinlenirdi.\nIII. Babam arkadaşlarıyla (Kerem, Selim ve Ali) o ağacın dibinde oynarmış.\nIV. Bayramlarda köye gelen akrabalarımız (şehirde yaşayanlar) da orada toplanırdı.\nV. Güneş batınca herkes evine (dönerdi).\n\nNumaralanmış cümlelerin hangisinde yay ayraç yanlış kullanılmıştır?',
 [('I',D,'Tarih kesin olmadığı için (?) yerindedir.','bilgi'),
  ('II',D,'Ayraç içi, ağaç hakkında ek açıklama verir; yerindedir.','bilgi'),
  ('III',D,'Ayraç içi arkadaşları açıklar; yerindedir.','dikkat'),
  ('IV',D,'Ayraç içi “akrabalarımız”ı açıklar; yerindedir.','dikkat'),
  ('V',Y,'','')],
 'E',lambda t:t==Y,'Yay ayracın yanlış kullanıldığı numaralı cümle.',
 'Ayraç içindeki söz çıkarılırsa cümle yine de anlamlı ve tam kalmalı.',[B_AYR],
 S('Ayraç içi söz, cümleden çıkarılınca cümle tam kalmalıdır.','Ağacın (yüz yaşını aşkın) ✓ · evine (dönerdi) ✗','I–IV’te ayraç içi ek bilgi ya da açıklama; çıkarılınca cümle tam kalır.','I, II, III, IV: ✓','V’te yüklem “dönerdi” ayraca alınmış; çıkarınca cümle yüklemsiz kalır.','V: ✗'),
 'Cümlenin temel ögesi (özellikle yüklem) yay ayraca alınmaz.',kalip='öncüllü')

# 0014 kolay · B · çizgi · boşluk
soru(Q,'0014','K-DBNKB-05','kolay','İki tarih arasındaki aralığı kısa çizgiyle gösterir.',2,
 'Gösteri 12 ( ) 14 Mart tarihleri arasında sahnelenecektir.\n\nBu cümlede boş bırakılan yere hangi noktalama işareti getirilmelidir?',
 [('Virgül (,)','virgül','Virgül sayı aralığını göstermez; iki sayıyı ayırmak için kısa çizgi gerekir.','bilgi'),
  ('Kısa çizgi (-)','çizgi','',''),
  ('Noktalı virgül (;)','nv','Noktalı virgül cümleleri ayırır; sayı aralığı için kullanılmaz.','bilgi'),
  ('İki nokta (:)','iki','İki nokta açıklama ve sıralama öncesinde kullanılır; aralık bildirmez.','dikkat'),
  ('Üç nokta (...)','üç','Üç nokta söylenmeyen sözü gösterir; tarih aralığı için kullanılmaz.','dikkat')],
 'B',lambda t:t=='çizgi','Boşluğa getirilmesi gereken noktalama işareti.',
 'İki sayı arasında “…’dan … ’a kadar” anlamı var.',[B_CIZ],
 S('Sayı, tarih ya da yer arasındaki aralık kısa çizgiyle gösterilir.','12-14 Mart','Virgül, noktalı virgül, iki nokta ve üç nokta aralık bildirmez.','(,) (;) (:) (...): ✗','12 ile 14 arasındaki aralık kısa çizgiyle gösterilir.','(-) ✓'),
 'İki sayı arasında “ile … arası” anlamı varsa kısa çizgi koy.',kalip='öncüllü')

# 0015 orta · D · çizgi · numaralı cümle
soru(Q,'0015','K-DBNKB-05','orta','Kısa çizginin ek ya da bağlaç yerine kullanılamayacağını bilir.',3,
 'I. Sınav 12-14 Mart tarihleri arasında yapılacak.\nII. Doğu-Batı ayrımı yüzyıllardır tartışılıyor.\nIII. Atölye 1990-1995 yılları arasında üretim yaptı.\nIV. Elif dün Kerem-ile birlikte kütüphaneye gitti.\nV. Ankara-İstanbul seferi bu hafta artırıldı.\n\nNumaralanmış cümlelerin hangisinde kısa çizgi (-) yanlış kullanılmıştır?',
 [('I',D,'Tarih aralığı kısa çizgiyle gösterilmiştir; doğrudur.','bilgi'),
  ('II',D,'Karşıt iki sözcük (Doğu-Batı) kısa çizgiyle bağlanmıştır; doğrudur.','bilgi'),
  ('III',D,'Yıl aralığı kısa çizgiyle gösterilmiştir; doğrudur.','dikkat'),
  ('IV',Y,'',''),
  ('V',D,'İki yer arasındaki güzergâh kısa çizgiyle gösterilmiştir; doğrudur.','dikkat')],
 'D',lambda t:t==Y,'Kısa çizginin yanlış kullanıldığı numaralı cümle.',
 'Kısa çizgi aralık ya da karşıtlık bildirir; “ile” gibi bir sözcüğü ona bağlamak bu işlevlerden biri mi?',[B_CIZ],
 S('Kısa çizgi aralık ve karşıtlık bildirir; sözcüğü bağlaca ya da ek gibi bağlamaz.','12-14 ✓ · Doğu-Batı ✓','I, III ve V aralık, II karşıtlık bildiriyor.','I, II, III, V: ✓','IV’te “Kerem-ile” yazılışı çizgiyi bir bağ olarak kullanıyor; “Kerem ile” yazılmalıdır.','IV: ✗'),
 'Kısa çizgiyi yalnız aralık, karşıtlık ve satır sonu bölmede kullan.',kalip='öncüllü')

# 0016 kolay · A · çizgi · satır sonu
soru(Q,'0016','K-DBNKB-05','kolay','Satır sonunda sözcüğü hece sınırından böler.',2,
 'Aşağıdaki sözcüklerden hangisi satır sonunda kısa çizgiyle hece sınırından doğru bölünmüştür?',
 [('çalış-kan',D,'',''),
  ('bahç-ede',Y,'“Bahçede” bah-çe-de diye ayrılır; “bahç-” hece sınırında değildir.','bilgi'),
  ('sını-fta',Y,'“Sınıfta” sı-nıf-ta diye ayrılır; “sını-” hece sınırında değildir.','bilgi'),
  ('kel-ebek',Y,'“Kelebek” ke-le-bek diye ayrılır; “kel-” yanlış yerden bölünmüştür.','dikkat'),
  ('arkad-aş',Y,'“Arkadaş” ar-ka-daş diye ayrılır; “arkad-” hece sınırında değildir.','dikkat')],
 'A',lambda t:t==D,'Hece sınırından doğru bölünmüş sözcük.',
 'Sözcüğü yüksek sesle hecelerine ayır, sonra bölmeyi hece sınırıyla karşılaştır.',[B_CIZ],
 S('Satır sonunda sözcük, hece sınırından kısa çizgiyle bölünür.','ça-lış-kan → çalış- | kan','B, C, D, E hece sınırı dışından bölünmüş: bah-çe-de, sı-nıf-ta, ke-le-bek, ar-ka-daş.','B, C, D, E: ✗','A’da “çalış-” hece sınırında biter; bölme doğrudur.','A: ✓'),
 'Önce heceleri bul (ça-lış-kan); çizgiyi yalnız hece aralarına koy.')

# 0017 orta · C · çizgi · numaralı cümle · uzun çizgi
soru(Q,'0017','K-DBNKB-05','orta','Uzun çizginin konuşmayı başlatmak için kullanıldığı cümleyi belirler.',3,
 'I. Çocuklar bahçede — oyun oynuyordu.\nII. Elif — arkadaşım yarın okula gelecek.\nIII. — Bu kitabı kütüphaneden mi aldın?\nIV. Yarın sabah — okula erken gidecek.\nV. Dedem — bir zamanlar köyün muhtarıydı — bu yaz bize gelecek.\n\nNumaralanmış cümlelerin hangisinde uzun çizgi (—) konuşmayı başlatmak için kullanılmıştır?',
 [('I',Y,'Özne ile yüklem arasında uzun çizgi konmaz; konuşma çizgisi değildir.','bilgi'),
  ('II',Y,'Cümle içinde tek başına uzun çizgi gerekmez; konuşma yok.','bilgi'),
  ('III',D,'',''),
  ('IV',Y,'Zaman zarfından sonra uzun çizgi konmaz; konuşma yok.','dikkat'),
  ('V',Y,'Çift çizgi ara sözü ayırmıştır; konuşmayı başlatmaz.','dikkat')],
 'C',lambda t:t==D,'Uzun çizginin konuşmayı başlattığı numaralı cümle.',
 'Uzun çizgi, konuşan kişinin sözünün başladığını gösterir.',[B_CIZ],
 S('Uzun çizgi, diyalogda konuşmanın başına konur; çift çizgi ara sözü ayırır.','— Geldin mi?','I, II, IV cümle ortasında tek çizgi; V çift çizgiyle ara söz ayırıyor; hiçbiri konuşma başlatmıyor.','I, II, IV, V: ✗','III bir konuşmanın başında uzun çizgi taşır.','III: ✓'),
 'Konuşmayı başlatan uzun çizgi satır başında durur; cümle ortasındaki çizgi konuşma başlatmaz.',kalip='öncüllü')

# 0018 orta · B · üç nokta
soru(Q,'0018','K-DBNKB-06','orta','Üç noktanın söylenmek istenmeyen söz yerine kullanıldığı cümleyi belirler.',3,
 'Aşağıdaki cümlelerin hangisinde üç nokta, cümlenin ortasında söylenmek istenmeyen bir sözün yerine kullanılmıştır?',
 [('Eğer o gün erken çıksaydık belki de...',Y,'Üç nokta cümlenin yarım bırakıldığını gösterir; söylenmeyen söz yoktur.','bilgi'),
  ('Onca emeğimizi yok sayan o ... kapıyı çarpıp çıktı.',D,'',''),
  ('Bahçede çiçekler açmıştı: gül, lale, sümbül...',Y,'Üç nokta sayılabilecek başka örnekleri gösterir; söylenmeyen söz değildir.','bilgi'),
  ('Sana söylemem gereken şey şu ki aslında ben...',Y,'Üç nokta bitmemiş cümleyi gösterir; söylenmeyen söz değildir.','dikkat'),
  ('Tam o sırada kapı açıldı ve içeri giren kişi...',Y,'Üç nokta cümlenin yarım kaldığını gösterir; söylenmeyen söz yoktur.','dikkat')],
 'B',lambda t:t==D,'Üç noktanın söylenmek istenmeyen sözün yerine kullanıldığı cümle.',
 'Cümle içindeki boşluk, bir sözcüğün söylenmediğini mi, yoksa cümlenin yarım kaldığını mı gösteriyor?',[B_UC],
 S('Üç nokta; bitmemiş cümlede, söylenmeyen sözün yerinde ve sayılabilecek örnekten sonra kullanılır.','o ... kapıyı çarptı','A, D, E cümlenin yarıda kaldığını, C sayılabilecek örnekleri gösterir.','A, D, E: bitmemiş · C: örnek','B’de cümle tamam, ama bir söz (kaba bir ad) söylenmemiş; üç nokta onun yerini tutar.','B: ✓'),
 'Cümle tamamlanmış ve ortada bir söz eksikse üç nokta o sözün yerini tutuyordur.')

# 0019 orta · D · üç nokta
soru(Q,'0019','K-DBNKB-06','kolay','Üç noktanın kullanım amacı farklı olan cümleyi bulur.',2,
 'Aşağıdaki cümlelerin hangisinde üç noktanın kullanım amacı ötekilerden farklıdır?',
 [('Sana söylemem gereken çok şey var ama...',Y,'Cümle yarım kalmıştır; üç nokta bitmemiş cümle için kullanılmıştır.','bilgi'),
  ('Eğer o gün yağmur yağmasaydı belki de...',Y,'Cümle yarım kalmıştır; bitmemiş cümle amacıyla kullanılmıştır.','bilgi'),
  ('Çantamı alıp çıkarken kapıda bir ses duydum, sonra...',Y,'Cümle yarım kalmıştır; bitmemiş cümle amacıyla kullanılmıştır.','dikkat'),
  ('Müzede çok eser vardı: heykel, resim, seramik...',D,'',''),
  ('Her şey yolunda gidiyordu, tam o sırada...',Y,'Cümle yarım kalmıştır; bitmemiş cümle amacıyla kullanılmıştır.','dikkat')],
 'D',lambda t:t==D,'Üç noktanın amacı farklı olan cümle.',
 'Dört cümlede üç nokta cümleyi yarıda bırakıyor; birinde ise başka bir iş görüyor.',[B_UC],
 S('Üç nokta, bitmemiş cümleyi ya da sayılabilecek başka örnekleri gösterir.','… (yarım) · seramik... (örnek)','A, B, C, E cümleyi yarıda bırakıyor; bitmemiş cümle amacı.','A, B, C, E: bitmemiş cümle','D’de üç nokta, sayılabilecek başka eserlerin olduğunu gösteriyor.','D: örnekler'),
 'Üç nokta bazen cümleyi keser, bazen listeyi açık bırakır; amacı ayır.')

# 0020 orta · E · üç nokta · boşluk sırası
soru(Q,'0020','K-DBNKB-06','orta','Sayma cümlesinde virgül ve üç nokta işaretlerini sıralar.',3,
 'Pazardan domates ( ) biber ( ) patlıcan ( ) Eve dönünce hepsini yıkadık.\n\nParçadaki ( ) ile gösterilen yerlere sırasıyla hangi noktalama işaretleri konmalıdır?',
 [('(,) (,) (,)',Y,'Son boşlukta virgül yanlıştır; arkadan yeni cümle başlıyor, başka örnekler de üç nokta ister.','bilgi'),
  ('(;) (;) (...)',Y,'Sıralı sözcükler noktalı virgülle değil, virgülle ayrılır.','bilgi'),
  ('(,) (;) (...)',Y,'İkinci boşlukta noktalı virgül yanlıştır; sıralı sözcükler virgülle ayrılır.','dikkat'),
  ('(...) (,) (...)',Y,'İlk boşlukta üç nokta yanlıştır; sıralama henüz sürmektedir, virgül gerekir.','dikkat'),
  ('(,) (,) (...)',D,'','')],
 'E',lambda t:t==D,'Boşluklara sırasıyla getirilmesi gereken noktalama işaretleri.',
 'Sıralı sözcükleri ayıran işaretle, yeni cümleden önceki işareti ayrı düşün.',[B_UC],
 S('Sıralı sözcükler virgülle ayrılır; sayılabilecek başka örnekler üç nokta ister.','domates, biber, patlıcan...','Birinci ve ikinci boşluk sıralı sözcükleri ayırır, üçüncü boşluk cümlenin sonudur.','1: , · 2: , · 3: ...','Dizi (,) (,) (...) olur.','E: ✓'),
 'Sıralı öğeleri virgül ayırır; liste açık bırakılıyorsa son işaret üç noktadır.',kalip='öncüllü')

# 0021 kolay · A · soru
soru(Q,'0021','K-DBNKB-07','kolay','Dolaylı soru cümlesinin sonuna soru işareti konmayacağını bilir.',2,
 'Aşağıdaki cümlelerin hangisinde noktalama yanlışı vardır?',
 [('Annem bana akşam kaçta döneceğimi sordu?',Y,'',''),
  ('Yarın akşam bize gelebilecek misin?',D,'Doğrudan soru cümlesi soru işaretiyle bitmiştir; doğrudur.','bilgi'),
  ('Ne kadar güzel bir manzara bu!',D,'Beğeni bildiren cümle ünlemle bitmiştir; doğrudur.','bilgi'),
  ('Kerem sınavdan kaç aldığını kimseye söylemedi.',D,'Dolaylı anlatımda cümle noktayla bitmiştir; doğrudur.','dikkat'),
  ('Bu kitabı gerçekten sen mi yazdın?',D,'Doğrudan soru cümlesi soru işaretiyle bitmiştir; doğrudur.','dikkat')],
 'A',lambda t:t==Y,'Noktalama yanlışı bulunan cümle.',
 'Cümle gerçekten soru soruyor mu, yoksa sorulan bir şeyi mi aktarıyor?',[B_SOR],
 S('Soru anlamı taşımayan, soruyu aktaran cümle nokta ile biter.','Kaçta döneceğimi sordu.','B ve E doğrudan soru, C ünlem, D dolaylı anlatım; sonları doğru.','B, C, D, E: ✓','A’da soru aktarılıyor, sorulmuyor; sona nokta konmalıdır.','A: ? yerine .'),
 'Soru sözcüğü var diye soru işareti koyma; cümle gerçekten soruyor mu bak.')

# 0022 zor · B · soru · mi'li dolaylı
soru(Q,'0022','K-DBNKB-07','orta','Soru eki taşıyan ama soru anlamı olmayan cümleyi bulur.',3,
 'Aşağıdaki cümlelerin hangisinin sonuna soru işareti (?) konulmamalıdır?',
 [('Yarın sabah erkenden yola çıkacak mısınız',Y,'Doğrudan soru cümlesidir; sonuna soru işareti konur.','bilgi'),
  ('Gelebilir misin diye Elif’e sordum',D,'',''),
  ('Bu resmi sen mi çizdin',Y,'Doğrudan soru cümlesidir; sonuna soru işareti konur.','bilgi'),
  ('Eve geç kalırsam kızar mısın',Y,'Soru anlamlıdır; yanıt beklenir ve sonuna soru işareti konur.','dikkat'),
  ('Kapıyı kapatmayı unutmuş muyum acaba',Y,'Soru anlamlıdır; sonuna soru işareti konur.','dikkat')],
 'B',lambda t:t==D,'Sonuna soru işareti konulmaması gereken cümle.',
 'Beş cümlede de soru eki var; hangisinde soru “diye sordum” ile aktarılıyor?',[B_SOR],
 S('Soru eki taşıyan cümle her zaman soru değildir; soru aktarılıyorsa nokta konur.','…misin diye sordum.','A, C, D, E soru eklerini taşıyor ve gerçekten yanıt bekliyor.','A, C, D, E: ?','B’de “misin” eki var ama soru “diye sordum” ile aktarılıyor; sona nokta konur.','B: .'),
 'Soru eki tek başına soru işareti getirmez; yanıt bekleyen cümle soru işaretiyle biter.')

# 0023 zor · C · soru · numaralı sonlar
soru(Q,'0023','K-DBNKB-07','zor','Numaralı parçada soru işareti getirilecek yeri bulur.',4,
 'Kerem kütüphanede ders çalışırken Elif’i gördü (I) Yanına giderek sınava hazırlanıp hazırlanmadığını sordu (II) Elif “Sen de bizimle çalışmaya gelir misin (III)” diye karşılık verdi. Kerem bu teklife çok sevindi (IV) Akşam birlikte çalışmaya karar verdiler (V)\n\nBu parçada numaralanmış yerlerden hangisine soru işareti (?) getirilmelidir?',
 [('I',Y,'Olayı anlatan bildirme cümlesidir; sonuna nokta konur.','bilgi'),
  ('II',Y,'Soru dolaylı aktarılmıştır (“hazırlanıp hazırlanmadığını sordu”); nokta konur.','dikkat'),
  ('III',D,'',''),
  ('IV',Y,'Duyguyu anlatan bildirme cümlesidir; sonuna nokta konur.','bilgi'),
  ('V',Y,'Karar bildiren bildirme cümlesidir; sonuna nokta konur.','bilgi')],
 'C',lambda t:t==D,'Soru işareti getirilmesi gereken numaralı yer.',
 'Hangi yerde bir kişi gerçekten yanıt bekleyerek soru soruyor?',[B_SOR],
 S('Doğrudan soru “?” ile, soruyu aktaran ya da bilgi veren cümle nokta ile biter.','gelir misin? ✓ · hazırlanıp hazırlanmadığını sordu. ✓','I, IV, V bildirme; II soruyu aktarıyor, doğrudan soru değil.','I, II, IV, V: nokta','III’te Elif doğrudan soruyor; tırnak içindeki sözün sonuna soru işareti konur.','III: ?'),
 'Soruyu doğrudan soran söze ? , soruyu aktaran cümleye nokta konur.',kalip='öncüllü')

# 0024 zor · D · ünlem · numaralı sonlar
soru(Q,'0024','K-DBNKB-07','zor','Numaralı parçada ünlem işareti getirilecek yeri bulur.',4,
 'Akşama doğru yağmur başladı (I) Kerem yağmurun ne zaman dineceğini merak etti (II) Elif’e dönüp “Sence ne zaman dinecek (III)” diye sordu. Elif pencereye bakarak “Ne güzel bir yağmur bu (IV)” dedi. İkisi de çaylarını alıp sessizce yağmuru izlediler (V)\n\nBu parçada numaralanmış yerlerden hangisine ünlem işareti (!) getirilmelidir?',
 [('I',Y,'Olayı anlatan bildirme cümlesidir; sonuna nokta konur.','bilgi'),
  ('II',Y,'Merakı aktaran bildirme cümlesidir; sonuna nokta konur.','dikkat'),
  ('III',Y,'Doğrudan soru cümlesidir; sonuna soru işareti konur.','dikkat'),
  ('IV',D,'',''),
  ('V',Y,'Olayı anlatan bildirme cümlesidir; sonuna nokta konur.','bilgi')],
 'D',lambda t:t==D,'Ünlem işareti getirilmesi gereken numaralı yer.',
 'Hangi söz bir soru ya da bilgi değil, beğeni ve duygu bildiriyor?',[B_SOR],
 S('Beğeni, şaşkınlık gibi duygu bildiren söz ünlemle biter.','Ne güzel bir yağmur bu!','I, II, V bildirme; III soru; yalnız IV beğeni bildiriyor.','I, II, V: . · III: ? · IV: !','IV’teki “Ne güzel bir yağmur bu” beğeni bildirir; ünlem getirilir.','IV: !'),
 'Duygu, beğeni ve şaşkınlık bildiren söz ünlemle biter.',kalip='öncüllü')
bitir(Q)
