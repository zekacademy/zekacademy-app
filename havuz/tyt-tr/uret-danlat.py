"""TYT Türkçe · Anlatım Bozukluğu genişletme: 9 soru (hafif mod). Metinler özgündür."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from hafif_db import *
AD=A
KY='ÖSYM TYT Türkçe 2018–2026 · Bilgi Sarmal Dil Bilgisi SB (ÖSYM Tipi) · TDK Yazım Kılavuzu'
def K(alt,fikir,tuzak,zor,kalip,adim,tip): return dict(alt=alt,fikir=fikir,tuzak=tuzak,zorluk=zor,kalip=kalip,adim=adim,tipId=tip,kaynak=KY)
KARTLAR={
 'K-DBAB-01':K('Sözcük Düzeyinde Bozukluk','Gereksiz sözcük ya da yanlış anlamda kullanılmış sözcüğü cümlede bulmak.','Vurgu amaçlı ya da anlamı farklı sözcük çiftlerini gereksiz yineleme sanmak.','kolay','düz',2,'dab-sozcuk'),
 'K-DBAB-02':K('Mantık, Karşılaştırma ve Sıralama','Neden–sonuç, karşılaştırma ve işlerin sırası bakımından anlamca tutarsız cümleyi bulmak.','Dil bilgisi bakımından doğru görünen cümleyi anlamca da doğru saymak.','orta','düz',3,'dab-mantik'),
 'K-DBAB-03':K('Ek ve Ortak Öge Eksikliği','Birden çok yükleme ya da sözcüğe ortak olan ögenin ekinin her birine uymadığı cümleyi bulmak.','Ortak ögeyi yalnız bir yüklemle sınayıp ötekini atlamak.','orta','düz',3,'dab-ek'),
 'K-DBAB-04':K('Özne–Yüklem ve Çatı Uyumu','Özne ile yüklemin kişi/sayı uyumunu ve çatı uyuşmazlığını denetlemek.','“Tarafından” sözcüğünü görünce cümleyi doğru saymak.','zor','düz',4,'dab-uyum'),
}
TIPLER={'dab-sozcuk':'Gereksiz ya da yanlış anlamlı sözcük','dab-mantik':'Mantık, karşılaştırma ve sıralama','dab-ek':'Ek ve ortak öge eksikliği','dab-uyum':'Özne–yüklem ve çatı uyumu'}
Q=kur('danlat','Anlatım Bozukluğu','tr|Anlatım Bozukluğu',KARTLAR,TIPLER); Q.n=9
def S(no,kart,zor,kaz,adim,metin,dogru,yan,harf,istenen,ip,bilgi,adimlar,puf,kalip='düz'):
    L='ABCDE'; yi=iter(yan); opts=[]
    for l in L:
        if l==harf: opts.append((dogru,D,'',''))
        else:
            m,c,t=next(yi); opts.append((m,Y,c,t))
    soru(Q,no,kart,zor,kaz,adim,metin,opts,harf,lambda e:e==D,istenen,ip,bilgi,adimlar,puf,kalip=kalip)
KOK='Aşağıdaki cümlelerden hangisinin anlatımı bozuktur?'
KOK2='Bu cümledeki anlatım bozukluğu aşağıdakilerin hangisinden kaynaklanmaktadır?'
B_GS=B('Gereksiz sözcük','anlamca aynı olan sözcüklerin birlikte kullanılması bozukluktur: “geri iade etmek” (geri ve iade aynı anlamı taşır) · doğrusu: “iade etmek”')
B_YS=B('Yanlış anlamlı sözcük','fiilin anlamı cümleye uymuyorsa sözcük yanlış kullanılmıştır: göstermek ile sergilemek aynı değildir · “Misafire evi gösterdi” doğru, “Misafire evi sergiledi” yanlıştır')
B_MN=B('Mantık hatası','neden ile sonuç, olaylar ya da karşılaştırılan ögeler anlamca birbirini karşılamalıdır · “Yağmur yağdığı için yollar ıslandı” doğru; “…yollar kurudu” mantıkla bağdaşmaz')
B_SR=B('Sıralama yanlışlığı','işler gerçekte olduğu sırayla anlatılmalıdır · önce hamur yoğrulur, sonra fırına verilir: “Hamuru yoğurduktan sonra fırına verdi” doğru')
B_EK=B('Ek ve ortak öge','birden çok yükleme ortak olan ögenin ekleri her yüklemle uyumlu olmalıdır · “Evi ve işine bağlı” yanlış (belirtme + yönelme); “evine ve işine bağlı” doğru (iki ögede de -e)')
B_EO=B('Ortak öge','iki yüklemin ortak ögesi her yüklemin istediği ekle uyumlu olmalıdır · “Bu kitabı aldı ve okudu” doğru (ikisi de belirtme ister); “Bu kitaba baktı ve okudu” yanlış (yönelme + belirtme)')
B_UY=B('Özne–yüklem uyumu','özne ile yüklem kişi ve sayıda uyuşmalıdır: “Bizler yarın toplanacağız” doğru, “toplanacaksınız” yanlış')
B_CT=B('Çatı uyuşmazlığı','“tarafından” sözcüğü edilgen çatılı fiille kullanılır: “Mektup postacı tarafından getirildi” doğru; “…tarafından getirdi” yanlış (etken fiil)')
B_KR=B('Karşılaştırma','karşılaştırılan ögeler aynı türden olmalıdır: soru–soru, kitap–kitap · “Mağazanın fiyatları, pazardan pahalı” yanlış; “…pazarın fiyatlarından pahalı” doğru')

S('0001','K-DBAB-01','kolay','Gereksiz sözcük kullanımından doğan bozukluğu bulur.',2,'Aşağıdaki cümlelerin hangisinde anlatım bozukluğu vardır?',
 'Öğretmenimiz, anlaşılmayan konuyu bir kez daha tekrar etti.',
 [('Kış gelmeden bahçedeki ağaçları budadık.','Cümlede gereksiz sözcük ya da başka bir bozukluk yoktur; anlatım doğrudur.','bilgi'),
  ('Müze, hafta sonları ziyaretçilere ücretsiz açıktır.','Anlatım bozukluğu yoktur; sözcükler yerli yerindedir.','bilgi'),
  ('Yeni açılan kütüphane, öğrencilerin ilgisini çekmeyi başardı.','Anlatım bozukluğu yoktur; ögeler uyumludur.','dikkat'),
  ('Sabah yağan karla birlikte şehirde ulaşım aksadı.','Anlatım bozukluğu yoktur; neden ve sonuç tutarlıdır.','dikkat')],
 'A','Anlatım bozukluğu olan cümle.','Anlamca aynı olan iki sözcüğü yan yana kullanan cümleyi ara.',[B_GS],
 [AD('Bozukluk türünü hatırla','En sık bozukluk, aynı anlamı veren sözcüklerin birlikte kullanılmasıdır.','geri + iade'),
  AD('Şıkları sına','B, C, D, E’de aynı anlamı veren sözcük çifti yok; anlatım yerindedir.','B, C, D, E: doğru'),
  AD('Bozukluğu bul','“Bir kez daha” ile “tekrar” aynı anlamı taşır; biri gereksizdir.','A: gereksiz sözcük')],
 'Cümlede “geri, yine, yeniden, ayrıca” gibi sözcükleri anlamdaşıyla yan yana görürsen yinelemeye bak.')
S('0002','K-DBAB-01','orta','Yanlış anlamda kullanılan sözcüğü içeren cümleyi bulur.',2,'Aşağıdakilerden hangisinde bir anlatım bozukluğu bulunmaktadır?',
 'Sınıfımıza yeni katılan arkadaşımız, bize kendisini tanıştırdı.',
 [('Her sabah okula giderken yolda tanıdık yüzlerle karşılaşırım.','Anlatım bozukluğu yoktur; sözcükler anlamına uygun kullanılmıştır.','bilgi'),
  ('Bu akşam sinemaya gitmek yerine evde film seyredeceğiz.','Anlatım bozukluğu yoktur; sözcükler doğru kullanılmıştır.','bilgi'),
  ('Yazarın son romanı, okurlar tarafından büyük ilgiyle karşılandı.','Edilgen fiil ve “tarafından” uyumlu; bozukluk yoktur.','dikkat'),
  ('Çocuklar, bahçedeki çiçekleri sulamak için hortumu getirdi.','Anlatım bozukluğu yoktur; ögeler uyumludur.','dikkat')],
 'C','Anlatım bozukluğu olan cümle.','Fiillerin cümledeki anlamına tek tek bak.',[B_YS],
 [AD('Bozukluk türünü hatırla','Fiil anlamca cümleye uymuyorsa sözcük yanlış kullanılmıştır.','anlama uygun fiil'),
  AD('Şıkları sına','A, B, D, E’de fiiller anlama uygun: karşılaşırım, seyredeceğiz, karşılandı, getirdi.','A, B, D, E: doğru'),
  AD('Bozukluğu bul','“Tanıştırmak” iki kişiyi birbiriyle tanıştırmaktır; kişinin kendini anlatması için “tanıtmak” gerekir.','C: yanlış anlamda sözcük')],
 'Yakın anlamlı fiillerde (göstermek/sergilemek gibi) anlam farkını sınamak, bu bozukluğu yakalamanın en kısa yoludur.')
S('0003','K-DBAB-02','orta','Neden–sonuç ilişkisi bozuk olan cümleyi bulur.',3,'Aşağıdaki cümlelerin hangisi anlatım bakımından kusurludur?',
 'Havalar iyice soğuduğu için ağaçlar yaprak açmaya başladı.',
 [('Sabahtan beri yağan yağmur nedeniyle maçın ertelendiğini öğrendik.','Yağmur ile maçın ertelenmesi arasında mantık bağı var; bozukluk yoktur.','bilgi'),
  ('Kitabı çok sevdiği için aynı yazarın diğer eserlerini de okumaya başladı.','Sevmek ile yeni kitap okumak arasında tutarlı bir neden–sonuç ilişkisi var.','bilgi'),
  ('Bahçeye yeni çiçekler dikildiği için bahçe renklendi.','Çiçek dikmek ile bahçenin renklenmesi arasında tutarlı bir neden–sonuç ilişkisi var; bozukluk yoktur.','dikkat'),
  ('Sınavda başarılı olmak için gece geç saatlere kadar çalıştı.','Amaç ile eylem arasında tutarlı bir ilişki var; bozukluk yoktur.','dikkat')],
 'E','Neden–sonuç ilişkisi bozuk olan cümle.','Neden ile sonucun gerçekten birbirini doğurup doğurmadığını sına.',[B_MN],
 [AD('Ölçütü hatırla','Cümledeki neden, sonucu gerçekten doğurmalıdır.','neden → sonuç'),
  AD('Şıkları sına','Yağmur → erteleme; sevmek → okumak; çiçek → renkli bahçe; çalışmak → başarı. Hepsi tutarlı.','A, B, C, D: tutarlı'),
  AD('Bozukluğu bul','Soğuk havada ağaçlar yaprak açmaz; yaprak açma baharın sonucudur.','E: mantık hatası')],
 'Her “-diği için” cümlesinde nedeni ve sonucu ayrı yaz, sonra aralarında gerçekten bağ var mı diye bak.')
S('0004','K-DBAB-02','kolay','Sıralama yanlışlığını bozukluğun kaynağı olarak belirler.',3,
 'Çocuk kapıyı açtıktan sonra anahtarı kilide takıp çevirdi.\n'+KOK2,
 'İşlerin gerçekleşme sırasının yanlış verilmesi',
 [('Anlamca aynı sözcüklerin birlikte kullanılması','Cümlede anlamca aynı olan iki sözcük yoktur.','bilgi'),
  ('Öznenin yüklemle kişi bakımından uyuşmaması','Özne ile yüklem uyumludur; çocuk–çevirdi 3. tekil.','bilgi'),
  ('Ortak ögenin ekinin her yükleme uymaması','Ortak ögede ek uyuşmazlığı yoktur.','dikkat'),
  ('Bir sözcüğün yanlış anlamda kullanılması','Sözcüklerin hiçbiri yanlış anlamda kullanılmamıştır.','dikkat')],
 'B','Bozukluğun kaynağı.','Eylemlerin gerçek hayatta hangi sırayla yapıldığını düşün.',[B_SR],
 [AD('Olası bozuklukları listele','Gereksiz sözcük, uyumsuzluk, ek eksikliği, yanlış anlam, sıralama olabilir.','5 olasılık'),
  AD('Seçenekleri ele','Cümlede yinelenen sözcük, uyumsuz özne–yüklem, ortak ek ya da yanlış fiil anlamı yok.','A, C, D, E: yok'),
  AD('Kaynağı bul','Kapı, anahtar takılıp çevrilerek açılır; cümlede önce kapı açılmış, sonra anahtar çevrilmiş.','B: sıralama yanlışlığı')],
 'Birden çok eylemi olan cümlede eylemleri gerçek sırayla yaz; cümledeki sıraya uymuyorsa bozukluk vardır.')
S('0005','K-DBAB-03','orta','Ortak ek eksikliğinden doğan bozukluğu bulur.',3,'Aşağıdaki cümlelerden hangisinde anlatım yönünden bir yanlışlık vardır?',
 'Yeni öğrenciler, okulu ve öğretmenlerine alışmakta zorlandı.',
 [('Dedem, bahçedeki ağaçları budadıktan sonra çiçekleri suladı.','Ögeler yüklemlerle uyumlu; bozukluk yoktur.','bilgi'),
  ('Kitapçıdan hem roman hem de sözlük aldı.','Ortak yüklem “aldı” her iki nesneyle uyumludur; bozukluk yoktur.','bilgi'),
  ('Küçük kız, annesine ve babasına bir mektup yazdı.','Her iki dolaylı tümleç de -e ekiyle yazılmıştır; yüklem ikisine de uyar.','dikkat'),
  ('Takım, ilk yarıda gol atamadı ama ikinci yarıda üç gol attı.','Özne ortak ve her iki yüklem uyumludur; bozukluk yoktur.','dikkat')],
 'D','Anlatım bozukluğu olan cümle.','“Alışmak” fiili hangi hâl ekini ister? Sıralanan iki ögeye ayrı ayrı uygula.',[B_EK],
 [AD('Kuralı hatırla','Ortak yüklemin istediği ek, sıralanan her ögede bulunmalıdır.','alışmak → -e hâli'),
  AD('Şıkları sına','A, B, C, E’de ortak yüklem ve ögeler birbiriyle uyumlu.','A, B, C, E: doğru'),
  AD('Bozukluğu bul','“Okulu” belirtme hâlinde, “öğretmenlerine” yönelme hâlinde; “alışmak” -e ister, doğrusu “okula”.','D: ek eksikliği')],
 'Ortak yüklemli cümlede yükleme sırayla her ögeyi bağla: “okulu alıştı” olmuyorsa ek yanlıştır.')
S('0006','K-DBAB-04','orta','Özne–yüklem uyumsuzluğunu içeren cümleyi bulur.',3,'Aşağıdaki cümlelerin hangisinde anlatım bakımından bir bozukluk görülmektedir?',
 'Ben ve arkadaşlarım yarın pikniğe gideceksiniz.',
 [('Annem de babam da hafta sonu bizi ziyarete gelecek.','Özne “annem de babam da” 3. kişidir; yüklem “gelecek” kişi bakımından uyumludur.','bilgi'),
  ('Sen ve kardeşin bu akşam bize uğrayacaksınız.','Sen + kardeşin birlikte “siz” eder; yüklem 2. çoğul, uyumludur.','bilgi'),
  ('Siz sabah erkenden yola çıkarsanız akşama varırsınız.','Özne “siz”, yüklemler 2. çoğul; uyumludur.','dikkat'),
  ('Hepimiz bu sonuçtan çok memnun kaldık.','Özne 1. çoğul, yüklem 1. çoğul; uyumludur.','dikkat')],
 'A','Anlatım bozukluğu olan cümle.','Öznenin kişisini ve yüklemin kişi ekini yan yana yaz.',[B_UY],
 [AD('Kuralı hatırla','Özne ve yüklem kişi ve sayıda uyuşmalıdır.','biz ↔ -eceğiz'),
  AD('Şıkları sına','Sen + kardeşin = siz; siz = siz; hepimiz = biz; annem ve babam = onlar. Hepsi yüklemle uyumlu.','B, C, D, E: uyumlu'),
  AD('Uyumsuzluğu bul','“Ben ve arkadaşlarım” = biz; yüklem “gideceksiniz” (siz).','A: özne–yüklem uyumsuzluğu')],
 'Birden çok kişiyi içeren öznede kişileri topla: ben + sen = biz; sen + o = siz.')
S('0007','K-DBAB-04','kolay','“Tarafından” kullanılan cümlelerde çatı uyuşmazlığını bulur.',4,'Aşağıdakilerin hangisinde anlatımı bozan bir yanlışlık vardır?',
 'Törende okunan şiir davetliler tarafından dinledi.',
 [('Yeni binanın temeli belediye tarafından atıldı.','Atıl-dı edilgen ve “tarafından” ile uyumlu; bozukluk yoktur.','bilgi'),
  ('Okulun bahçesi gönüllü öğrenciler tarafından yeniden düzenlendi.','Düzenlen-di edilgen ve “tarafından” ile uyumlu.','bilgi'),
  ('Roman, yıllar süren bir çalışmayla tamamlanmıştır.','Tamamlan-mıştır edilgendir; “tarafından” kullanılmadığı için çatı sorunu yoktur.','dikkat'),
  ('Eski tiyatro salonunu gönüllüler kısa sürede onardı.','Onar-dı etkendir; özne “gönüllüler” işi yapan olduğundan çatı uyumludur.','dikkat')],
 'C','Çatı uyuşmazlığı olan cümle.','“Tarafından” sözcüğü hangi çatıyı gerektirir? Her şıktaki yüklemi bu çatıya göre ayır.',[B_CT],
 [AD('Kuralı hatırla','“Tarafından” sözcüğü edilgen çatılı fiille birlikte kullanılır.','… tarafından + edilgen'),
  AD('Yüklemleri sına','atıldı, düzenlendi, tamamlanmıştır: edilgen. onardı: etken, özne işi yapıyor.','A, B, D, E: uyumlu'),
  AD('Uyumsuzluğu bul','“Dinledi” etken fiildir; “şiir … tarafından dinledi” biçimi çatı bakımından uyuşmaz, doğrusu “dinlendi”.','C: çatı uyuşmazlığı')],
 '“Tarafından” gördüğünde yükleme bak: fiilde -l/-n edilgen eki yoksa bozukluk vardır.')
S('0008','K-DBAB-03','orta','Ortak ögenin her yükleme uymadığı bozukluğu belirler.',4,
 'Ayşe bu şehirde yıllarca yaşadı ve çok sevdi.\n'+KOK2,
 'Ortak ögenin her iki yüklemle uyumlu olmaması',
 [('Özne ile yüklemin kişi bakımından uyuşmaması','Özne “Ayşe”, yüklemler 3. tekil; uyum vardır.','bilgi'),
  ('Anlamca aynı sözcüklerin gereksiz yinelenmesi','Cümlede anlamca yinelenen sözcük yoktur.','bilgi'),
  ('Yüklemin çatı bakımından uyuşmaması','İki yüklem de etken çatıdadır; çatı uyuşmazlığı yoktur.','dikkat'),
  ('İşlerin gerçekleşme sırasının yanlış verilmesi','Yaşamak ile sevmek arasında sıra bakımından aykırılık yoktur.','dikkat')],
 'D','Bozukluğun kaynağı.','“Yaşadı” ile “sevdi” hangi hâl ekini ister? İkisini ortak bir ögeyle bağdaştırabiliyor musun?',[B_EO],
 [AD('Ekleri yaz','“Yaşamak” bulunma hâli (-de), “sevmek” belirtme hâli (-i) ister.','yaşadı: şehirde · sevdi: şehri'),
  AD('Seçenekleri ele','Özne–yüklem uyumlu, yineleme yok, çatılar etken, sıra tutarlı.','A, B, C, E: sorun yok'),
  AD('Kaynağı bul','“Bu şehirde” yalnız “yaşadı”ya uyar; “sevdi”nin nesnesi ayrıca gerekir (“bu şehri çok sevdi”).','D: ortak öge uyumsuzluğu')],
 'İki yüklemli cümlede ortak ögeyi sırayla her yükleme bağla; ek uymuyorsa ortak öge uyumsuzdur.')
S('0009','K-DBAB-02','orta','Karşılaştırmada eş değer olmayan ögelerden doğan bozukluğu bulur.',4,KOK,
 'Bu yılki sınavın soruları, geçen yılki sınavdan daha zordu.',
 [('Komşumuzun bahçesindeki güller, bizim bahçemizdekilerden çok daha çabuk açtı.','“Bahçemizdekiler” gülleri karşılar; karşılaştırılan ögeler aynıdır; bozukluk yoktur.','bilgi'),
  ('Bu yılki turnuvanın seviyesi, geçen yılki turnuvanın seviyesinden daha yüksekti.','Seviye ile seviye karşılaştırılıyor; ögeler eş değerdir; bozukluk yoktur.','bilgi'),
  ('Yeni telefonun kamerası, eski telefonun kamerasından çok daha iyi.','Kamera ile kamera karşılaştırılıyor; ögeler eş değerdir.','dikkat'),
  ('Ablamın okul çantası, benimkinden daha büyüktü.','“Benimki” çantayı karşılar; ögeler eş değerdir.','dikkat')],
 'B','Karşılaştırması bozuk cümle.','Karşılaştırılan iki şeyi yaz: biri “soru”, öteki ne?',[B_KR,B_MN],
 [AD('Kuralı hatırla','Karşılaştırılan iki öge aynı türden olmalıdır.','soru ↔ soru'),
  AD('Şıkları sına','Güller–güller; kamera–kamera; çanta–çanta; seviye–seviye: hepsi eş değer.','A, C, D, E: eş değer'),
  AD('Bozukluğu bul','B’de “sınavın soruları” ile “geçen yılki sınav” karşılaştırılıyor; soru ile sınav eş değer değil.','B: karşılaştırma yanlışlığı')],
 'Karşılaştırmada “-den daha” ile bağlanan iki ögeyi yan yana yaz; türleri farklıysa bozukluk vardır.')
bitir(Q)
