"""TYT Türkçe · Cümlenin Ögeleri genişletmesi (doge): 34 soru, hafif mod. Metinler özgündür.
Çözümleme yaklaşımı (MEB/ÖSYM): hâl eki (-e, -de, -den) almış öbek = dolaylı tümleç; hâl eki almamış zaman/durum/miktar sözcükleri,
-le/ile ve edat öbekleri = zarf tümleci. Tartışmalı (-de'li yer/zaman) örnekler sorunun cevabını belirleyen yerde kullanılmadı."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from hafif_db import *
AD=A
KY='ÖSYM TYT Türkçe 2018–2026 · Bilgi Sarmal Dil Bilgisi SB (ÖSYM Tipi) · MEB Türk Dili ve Edebiyatı müfredatı'
def K(alt,fikir,tuzak,z,kalip,adim,tip): return dict(alt=alt,fikir=fikir,tuzak=tuzak,zorluk=z,kalip=kalip,adim=adim,tipId=tip,kaynak=KY)
KARTLAR={
 'K-DBOG-01':K('Yüklem','Yüklemin fiil ya da isim soylu olduğunu ve cümledeki yerini belirlemek.','Ek fiil (-di, -miş) gören her yüklemi isim soylu sanmak; hikâye/rivayet birleşik zamanlı fiili isim yüklemi saymak.','orta','düz',3,'dog-yuklem'),
 'K-DBOG-02':K('Özne','Gizli, sözde ve söz öbeği biçimindeki özneyi bulmak.','Cümlenin başındaki adı özne saymak; edilgen yüklemin öznesini eylemi yapan sanmak; öznenin yalnız bir sözcük olduğunu düşünmek.','orta','düz',3,'dog-ozne'),
 'K-DBOG-03':K('Nesne','Belirtili/belirtisiz ve öbek hâlindeki nesneyi bulmak; nesneyi dolaylı tümleçten ayırmak.','Belirtisiz nesneyi dolaylı tümleç ya da özne sanmak; -e/-den ekli öbeği nesne saymak.','orta','düz',3,'dog-nesne'),
 'K-DBOG-04':K('Dolaylı Tümleç','Yönelme (-e) ve ayrılma (-den) hâlindeki dolaylı tümleci bulmak, edat tümlecinden ayırmak.','-e ekli edat öbeğini (…a göre, …a kadar) dolaylı tümleç sanmak; nesneyi dolaylı tümleç saymak.','orta','düz',3,'dog-dolayli'),
 'K-DBOG-05':K('Zarf Tümleci','Zaman, durum, miktar ve edat tümlecini zarf tümleci olarak tanımak.','Zarf tümlecini dolaylı tümleçle karıştırmak; birden çok zarf tümlecini saymamak.','orta','düz',3,'dog-zarf'),
 'K-DBOG-06':K('Ögelerin Sıralanışı','Numaralı öbeklere bölünmüş cümlenin ögelerini sırasıyla adlandırmak.','Yer değiştiren (devrik) ögeleri sırayla yorumlamak; nesne ve dolaylı tümleci ters okumak.','zor','öncüllü',4,'dog-sira'),
 'K-DBOG-07':K('Farklı Öge','Numaralı öbeklerden ötekilerden farklı ögeyi bulmak.','Her öbeği ayrı sormadan yalnız konumuna ya da ekine bakmak.','orta','öncüllü',3,'dog-farkli'),
 'K-DBOG-08':K('Aynı Ögeyi Taşıyan Öbekler','İki numaralı öbeğin ya da cümlelerin aynı ögeyi taşıyıp taşımadığını belirlemek.','Belirtili ve belirtisiz nesneyi farklı öge sanmak; dolaylı tümleç ile zarf tümlecini eşitlemek.','orta','öncüllü',3,'dog-ayni'),
 'K-DBOG-09':K('Ara Söz ve Cümle Dışı Unsurlar','Virgülle ayrılan söz öbeğinin ara söz/hitap (öge dışı) mi, yoksa bir öge mi olduğunu ayırmak.','Virgüllerle ayrılan her sözü ara söz sanmak; hitap edilen kişiyi özne saymak.','orta','düz',3,'dog-ara'),
}
TIPLER={'dog-yuklem':'Yüklem (isim/fiil soylu)','dog-ozne':'Özne (gizli, sözde, öbek)','dog-nesne':'Nesne (belirtili/belirtisiz)','dog-dolayli':'Dolaylı tümleç','dog-zarf':'Zarf tümleci (edat tümleci dahil)','dog-sira':'Ögelerin sıralanışı','dog-farkli':'Farklı öge','dog-ayni':'Aynı ögeyi taşıyan öbekler','dog-ara':'Ara söz ve cümle dışı unsur'}
Q=kur('doge','Cümlenin Ögeleri','tr|Cümlenin Ögeleri',KARTLAR,TIPLER); Q.n=34

def yerles(dogru,yan,harf):
    L='ABCDE'; o=[None]*5; o[L.index(harf)]=(dogru,D,'','')
    it=iter(yan)
    for i in range(5):
        if o[i] is None:
            m,c,t=next(it); o[i]=(m,Y,c,t)
    return o
def Qd(no,kart,zor,kaz,adim,metin,dogru,harf,yan,istenen,ip,bilgi,adimlar,puf,kalip='düz'):
    soru(Q,no,kart,zor,kaz,adim,metin,yerles(dogru,yan,harf),harf,lambda e:e==D,istenen,ip,bilgi,adimlar,puf,kalip=kalip)
def Qx(no,kart,zor,kaz,adim,metin,sk,harf,istenen,ip,bilgi,adimlar,puf,kalip='düz'):
    """sk: A–E sırasıyla (şık, cel, tur); doğru şıkta cel None."""
    opts=[(m,D if c is None else Y,c or '',t or '') for m,c,t in sk]
    soru(Q,no,kart,zor,kaz,adim,metin,opts,harf,lambda e:e==D,istenen,ip,bilgi,adimlar,puf,kalip=kalip)
def sira(*l): return ' – '.join(l)

B_YUK=B('Yüklem türü','fiil soylu: eylem bildirir (Çocuk koştu.) · isim soylu: ad soylu sözcük + ek fiil (Çarşı kalabalıktı.) · hikâye/rivayet kipindeki -di, -miş fiile gelirse yüklem yine fiil soyludur (Gelecekti.)')
B_YUK2=B('Yüklemin yeri','yüklem cümlenin sonundaysa cümle kurallı, başta ya da ortadaysa devriktir · Çok çalıştı Kerem. → yüklem “çalıştı”')
B_OZ=B('Özne','yükleme “kim?, ne?” diye sorulunca bulunur · gizli özne: yazılmayan, kişi ekinden anlaşılan özne (Eve gelince çıktım → ben) · özne bir söz öbeği de olabilir (Sınıfımızın en çalışkan öğrencisi geldi.)')
B_SOZ=B('Sözde özne','edilgen yüklemin öznesi eylemi yapan değil, eylemden etkilenendir · Temel atıldı. (atan belli değil) · işteş (kucaklaştı) ve dönüşlü yüklemlerin öznesi gerçek öznedir')
B_NES=B('Nesne','yükleme “neyi?, kimi?, ne?” diye sorulunca bulunur · belirtili nesne -i hâl eki alır (kitabı okudu) · belirtisiz nesne ek almaz (kitap okudu)')
B_DOL=B('Dolaylı tümleç','yüklemin -e (yönelme), -de (bulunma), -den (ayrılma) hâl eklerinden birini almış tümleci: kime?, neye?, kimden? · Elif arkadaşına yazdı.')
B_EDAT=B('Edat tümleci','edat + sözcük öbeği zarf tümleci görevinde kullanılır: ile, için, gibi, göre, kadar, boyunca, rağmen · Yaşına göre olgun. → “yaşına göre” edat tümleci, dolaylı tümleç değil')
B_ZAR=B('Zarf tümleci','yükleme “ne zaman?, nasıl?, ne kadar?” soruları sorulur · hâl eki almayan zaman, durum, miktar sözcükleri: dün akşam, yavaşça, çok · akşamleyin, yazın gibi zaman ifadeleri de zarf tümlecidir')
B_ARA=B('Ara söz ve hitap','cümlenin anlamına katkı yapan ama ögesi olmayan, virgülle ayrılan söz ara sözdür (Dedem, yanılmıyorsam, buraya gelmişti.) · hitap edilen kişi de öge değildir (Çocuklar, gelin!)')
B_SIRA=B('Ögeleri sıralama','her numaralı öbeğe yükleme göre soru sor: kim? → özne · neyi? → nesne · kime? → dolaylı tümleç · ne zaman?/nasıl? → zarf tümleci · yüklem en sona ya da başa gelebilir')

# ---------- YÜKLEM ----------
Qd('0001','K-DBOG-01','kolay','Yüklemin isim soylu olduğu cümleyi belirler.',2,
 'Aşağıdaki cümlelerin hangisinin yüklemi isim soyludur?',
 'Kentin en eski çarşısı bu sokaktadır.','C',
 [('Bahçedeki gül fidanı geçen yıl dikildi.','“Dikildi”, dik- fiilinin edilgen ve geçmiş zamanlı biçimidir; yüklem fiil soyludur.','bilgi'),
  ('Konuklar akşam yemeğine gelecekti.','“Gelecekti”deki -ti hikâye ekidir ama kök “gel-” fiildir; yüklem fiil soyludur.','dikkat'),
  ('Sınav sonuçları bu hafta açıklanacak.','“Açıklanacak”, açıkla- fiilinin edilgen ve gelecek zamanlı biçimidir; yüklem fiil soyludur.','bilgi'),
  ('Çocuklar yağmurdan sonra dışarı koştu.','“Koştu” bir eylem bildirir; yüklem fiil soyludur.','bilgi')],
 'Yüklemi isim soylu olan cümle.','Yüklemin kökü bir eylemden mi, bir addan mı geliyor?',[B_YUK],
 [AD('Yüklem türünü hatırla','Eylem bildiren yüklem fiil soyludur; ad soylu sözcük + ek fiil ise isim soyludur.','eylem → fiil · ad + ek fiil → isim'),
  AD('Yüklemleri bul','A: dikildi · B: gelecekti · D: açıklanacak · E: koştu. Hepsi fiil kökünden gelir; “gelecekti”deki -ti yalnız zaman bildirir.','A, B, D, E: fiil soylu'),
  AD('İsim yüklemini seç','C’de “sokaktadır” = sokak + -ta + ek fiil -dır; çarşının yerini bildirir, eylem yoktur.','C: isim soylu')],
 'Yüklemin köküne bak: eylem kökü fiil, ad kökü isim soyludur; hikâye eki (-ti) yüklemi isim yapmaz.')

Qd('0002','K-DBOG-01','kolay','Fiil soylu yüklemi, çok sayıda isim yüklemi arasında bulur.',3,
 'Aşağıdaki cümlelerin hangisinin yüklemi fiil soyludur?',
 'Bahçemizdeki armut ağacı bu yıl meyve verdi.','D',
 [('Babamın en sevdiği yemek mercimek çorbasıdır.','“Çorbasıdır” = çorba + ek fiil -dır; yüklem isim soyludur.','bilgi'),
  ('Gösterinin ilk bölümü çok eğlenceliydi.','“Eğlenceliydi” = eğlenceli + ek fiil -di; yüklem isim soyludur.','dikkat'),
  ('Sahildeki lokanta bu mevsimde boştur.','“Boştur” = boş + ek fiil -tur; yüklem isim soyludur.','bilgi'),
  ('Küçük kardeşim dünkü yarışın birincisiydi.','“Birincisiydi” = birincisi + ek fiil -di; yüklem isim soyludur.','dikkat')],
 'Yüklemi fiil soylu olan cümle.','Hangi cümlede yüklem bir ad + ek fiil değil, doğrudan bir eylem bildiriyor?',[B_YUK],
 [AD('Aranan türü belirle','Soruda fiil soylu yüklem aranıyor; ötekilerde ek fiil görülebilir.','ad + ek fiil → isim'),
  AD('Ek fiilli yüklemleri ele','A: çorbasıdır · B: eğlenceliydi · C: boştur · E: birincisiydi. Hepsi ad soylu sözcük + ek fiildir.','A, B, C, E: isim soylu'),
  AD('Fiili seç','D’de “verdi” (ver- + -di) bir eylem bildirir; yüklem fiil soyludur.','D: fiil soylu')],
 '“-di, -dır” görünce hemen ek fiil deme: önce kök ad mı fiil mi bak.')

Qx('0003','K-DBOG-01','orta','Birden çok cümlenin yüklem türünü karşılaştırır.',3,
 'I. Yazın köyümüzün havası serindir.\nII. Elif yeni aldığı kitabı bir günde bitirdi.\nIII. Bu kentin en eski mahallesi yamaçtadır.\n\nNumaralanmış cümlelerden hangilerinin yüklemi isim soyludur?',
 [('Yalnız I','III’ün yüklemi de isim soyludur: “yamaçtadır” = yamaç + ek fiil.','dikkat'),
  ('I ve III',None,None),
  ('Yalnız III','I’in yüklemi de isim soyludur: “serindir” = serin + ek fiil -dir.','dikkat'),
  ('II ve III','II’nin yüklemi “bitirdi” fiildir; “aldığı” yalnız bir sıfat-fiildir, yüklem değildir.','bilgi'),
  ('I, II ve III','II’nin yüklemi “bitirdi” bir eylemdir; fiil soyludur.','bilgi')],
 'B','İsim soylu yüklemli cümleleri belirlemek.','Her cümlede cümlenin sonundaki yüklemi bul, kökünün ad mı fiil mi olduğuna bak.',[B_YUK],
 [AD('Yüklemleri bul','I: serindir · II: bitirdi · III: yamaçtadır. “Aldığı” yüklem değil, kitabı niteleyen sıfat-fiildir.','I: serindir · II: bitirdi · III: yamaçtadır'),
  AD('Köklerini sına','serin + -dir (ek fiil) · bitir- (fiil) · yamaç + -ta + -dır (ek fiil).','I, III: ad kökü · II: fiil kökü'),
  AD('Sonucu seç','İsim soylu yüklem I ve III’tedir.','I ve III')],
 'Cümlede birden çok fiilimsi varsa asıl yüklemi, cümleyi bitiren çekimli sözcük olarak ara.',kalip='öncüllü')

Qd('0004','K-DBOG-01','kolay','Yüklemi cümlenin sonunda olmayan (devrik) cümleyi bulur.',3,
 'Aşağıdaki cümlelerin hangisinde yüklem, cümlenin sonunda yer almamıştır?',
 'Çok çalıştı Kerem bu sınav için.','E',
 [('Eve döndüğümde herkes uyumuştu.','Yüklem “uyumuştu” cümlenin sonundadır; cümle kurallıdır.','bilgi'),
  ('Yarın sabah erkenden kalkacağız.','Yüklem “kalkacağız” cümlenin sonundadır.','bilgi'),
  ('Bahçedeki çiçekleri kardeşim suladı.','Yüklem “suladı” sondadır; yalnız nesne başa alınmıştır.','dikkat'),
  ('Köye vardığımızda hava kararmıştı.','Yüklem “kararmıştı” sondadır; “vardığımızda” yan öbektir, yüklem değildir.','dikkat')],
 'Yüklemi sonda olmayan cümle.','Her cümlenin yüklemini bulup cümlenin son sözcüğüyle karşılaştır.',[B_YUK2],
 [AD('Yüklemin yerini hatırla','Kurallı cümlede yüklem sondadır; başta ya da ortadaysa cümle devriktir.','yüklem son → kurallı'),
  AD('Yüklemleri bul','A: uyumuştu · B: kalkacağız · C: suladı · D: kararmıştı. Hepsi son sözcüktür.','A, B, C, D: sonda'),
  AD('Devriği seç','E’de yüklem “çalıştı”dır; “Kerem” ve “bu sınav için” yüklemden sonra gelmiştir.','E: devrik')],
 'Yüklem, çekimli eylemdir; cümleyi bitiren sözcük olmak zorunda değildir.')

# ---------- ÖZNE ----------
Qd('0005','K-DBOG-02','orta','Öznesi söz öbeği biçiminde olan cümleyi belirler.',3,
 'Aşağıdaki cümlelerin hangisinin öznesi bir söz öbeğidir?',
 'Sınıfımızın en çalışkan öğrencisi ödül aldı.','A',
 [('Kerem bu yaz denizde yüzmeyi öğrendi.','Özne “Kerem” tek sözcüktür; öbek olan “denizde yüzmeyi” nesnedir.','dikkat'),
  ('Yarın erkenden kalkıp yola çıkacağız.','Özne gizlidir (biz); cümlede yazılı bir özne öbeği yoktur.','bilgi'),
  ('Eski mahalledeki bakkala her sabah uğrarım.','Özne gizlidir (ben); yazılı bir öbek değildir.','bilgi'),
  ('Yeni çıkan romanı herkes merakla okudu.','Özne “herkes” tek sözcüktür; öbek olan “yeni çıkan romanı” nesnedir.','dikkat')],
 'Öznesi bir söz öbeği olan cümle.','Yükleme “kim?” diye sor; cevap birden çok sözcük mü?',[B_OZ],
 [AD('Özneyi bulma yolu','Yükleme “kim?, ne?” diye sorulur; cevap öznedir, tek sözcük ya da öbek olabilir.','yüklem + kim? → özne'),
  AD('Şıklara sor','B: Kerem · C: gizli (biz) · D: gizli (ben) · E: herkes. Hiçbirinde birden çok sözcüklü özne yok.','B, C, D, E: tek sözcük ya da gizli'),
  AD('Öbeği seç','A’da “ödül alan kim?” → sınıfımızın en çalışkan öğrencisi (ad tamlaması + sıfat).','A: özne bir öbek')],
 'Özne her zaman tek sözcük değildir; yükleme sorduğun “kim?” sorusunun cevabını sonuna kadar al.')

Qd('0006','K-DBOG-02','orta','Sözde özneyi işteş ve etken yüklemli öznelerden ayırır.',4,
 'Aşağıdaki cümlelerin hangisinin öznesi sözde (gerçek olmayan) öznedir?',
 'Yeni köprünün temeli ay sonunda atılacak.','E',
 [('Arkadaşlarım kapının önünde kucaklaştı.','“Kucaklaştı” işteş çatılıdır; özne eylemi yapan gerçek öznedir.','dikkat'),
  ('Kervan sabaha karşı kente ulaştı.','“Ulaştı” etken bir fiildir; özne eylemi yapan gerçek öznedir.','bilgi'),
  ('Çocuklar yağmur dinince sokağa fırladı.','“Fırladı” etken bir fiildir; eylemi yapan “çocuklar” gerçek öznedir.','bilgi'),
  ('Öğrenciler törende bayrağı göndere çekti.','“Çekti” etkendir; eylemi yapan “öğrenciler” gerçek öznedir.','bilgi')],
 'Öznesi sözde özne olan cümle.','Yüklem edilgen mi? Özne eylemi yapıyor mu, yoksa eylemden mi etkileniyor?',[B_SOZ],
 [AD('Sözde özneyi hatırla','Edilgen yüklemin öznesi eylemi yapan değil, ondan etkilenendir.','edilgen yüklem → sözde özne'),
  AD('Yüklemleri çöz','A: kucaklaştı (işteş) · B: ulaştı · C: fırladı · D: çekti. Hiçbiri edilgen değil; özneler eylemi yapar.','A, B, C, D: gerçek özne'),
  AD('Edilgeni seç','E’de “atılacak” = at- + -ıl (edilgen) + -acak; temeli atan belli değil, “temel” eylemden etkilenir.','E: sözde özne')],
 '-ş (işteş) ve etken yüklemler sözde özne yapmaz; yalnız edilgen (-l, -n) yüklemin öznesi sözde öznedir.')

Qx('0007','K-DBOG-02','orta','Gizli özneli cümleleri numaralı olarak belirler.',3,
 'I. Öğretmenimiz soruları tahtaya yazdı.\nII. Eve gelince çantamı masaya bıraktım.\nIII. Haberi duyunca hemen yola çıkmışlar.\n\nNumaralanmış cümlelerin hangilerinde özne gizlidir?',
 [('Yalnız II','III’te de özne gizlidir: “çıkmışlar” kişi ekinden “onlar” anlaşılır.','dikkat'),
  ('I ve II','I’de özne “öğretmenimiz” cümlede yazılıdır; gizli değildir.','dikkat'),
  ('II ve III',None,None),
  ('Yalnız III','II’de de özne gizlidir: “bıraktım” kişi ekinden “ben” anlaşılır.','dikkat'),
  ('I, II ve III','I’de özne açıktır (öğretmenimiz); gizli değildir.','bilgi')],
 'C','Öznesi gizli olan cümleleri belirlemek.','Her yükleme “kim?” diye sor; cevap cümlede yazılı mı?',[B_OZ],
 [AD('Gizli özneyi hatırla','Özne cümlede yazılı değilse ve yüklemin kişi ekinden anlaşılıyorsa gizlidir.','kişi eki → gizli özne'),
  AD('Cümleleri sına','I: yazdı → kim? → öğretmenimiz (yazılı) · II: bıraktım → ben (yazılı değil) · III: çıkmışlar → onlar (yazılı değil).','I: açık · II, III: gizli'),
  AD('Sonucu seç','Gizli özne II ve III’tedir.','II ve III')],
 'Yükleme “kim?” dediğinde cevap cümlede yoksa kişi ekine bak: özne gizlidir.',kalip='öncüllü')

Qd('0008','K-DBOG-02','orta','Uzun bir cümlede özne öbeğinin sınırlarını belirler.',4,
 'Yıllardır bu sokakta oturan yaşlı terzi dükkânını dün akşam kapattı.\n\nBu cümlede özne aşağıdakilerden hangisidir?',
 'Yıllardır bu sokakta oturan yaşlı terzi','D',
 [('yaşlı terzi dükkânını','Bu öbek özneyi ve nesneyi (dükkânını) birleştirir; özne yalnız eylemi yapan öbektir.','dikkat'),
  ('Yıllardır bu sokakta oturan','Bu, özneyi niteleyen sıfat-fiil öbeğidir; “kim kapattı?” sorusunun tam cevabı değildir.','bilgi'),
  ('dükkânını dün akşam','Bu öbek nesne (dükkânını) ve zarf tümlecidir (dün akşam); özne değildir.','dikkat'),
  ('Yıllardır bu sokakta oturan yaşlı terzi dükkânını dün akşam','Bu, yükleme kadar tüm öbekleri kapsar; nesne ve zarf tümleci özneye ait değildir.','dikkat')],
 'Cümlenin öznesi.','Yükleme “kim?” diye sor; cevabı niteleyen sözcüklerle birlikte, ama başka öge katmadan al.',[B_OZ],
 [AD('Yükleme sor','“Kapattı” yüklemine “kim kapattı?” diye sorulur.','kim kapattı?'),
  AD('Cevabın sınırını çiz','Eylemi yapan “terzi”dir; onu niteleyen “yaşlı” ve “yıllardır bu sokakta oturan” özneye aittir.','Yıllardır bu sokakta oturan yaşlı terzi'),
  AD('Öteki ögeleri ayır','“Dükkânını” nesne, “dün akşam” zarf tümlecidir; öznenin parçası değildir.','nesne ve zarf tümleci özne dışı')],
 'Özne, yükleme sorulan “kim?” sorusunun cevabı ve onu niteleyen sözcüklerin tümüdür; ötekilerle karışmasın.')

# ---------- NESNE ----------
Qd('0009','K-DBOG-03','orta','Belirtili nesnenin bulunduğu cümleyi belirler.',3,
 'Aşağıdaki cümlelerin hangisinde belirtili nesne vardır?',
 'Komşumuz bahçedeki eski ağacı kesti.','B',
 [('Bu yaz dağ köyünde birkaç hafta kalacağız.','“Kalacağız” geçişsiz bir fiildir; cümlede nesne yoktur.','bilgi'),
  ('Çocuk annesine sıkıca sarıldı.','“Annesine” yönelme hâlindeki dolaylı tümleçtir; nesne değildir.','dikkat'),
  ('Babam sabahları gazete okur.','“Gazete” belirtme hâl eki almamıştır; belirtisiz nesnedir.','dikkat'),
  ('Elif odasında müzik dinliyor.','“Müzik” belirtme hâl eki almamıştır; belirtisiz nesnedir.','dikkat')],
 'Belirtili nesnesi olan cümle.','Nesne “-i” belirtme hâl ekini almış olmalı; yalnız “neyi?” sorusuna cevap vermesi yetmez.',[B_NES],
 [AD('Belirtili nesneyi hatırla','Nesne -ı, -i, -u, -ü eki almışsa belirtilidir; ek almamışsa belirtisizdir.','kitabı → belirtili · kitap → belirtisiz'),
  AD('Şıkları ele','A: nesne yok · C: annesine (dolaylı) · D: gazete (belirtisiz) · E: müzik (belirtisiz).','A, C, D, E: belirtili nesne yok'),
  AD('Belirtiliyi seç','B’de “neyi kesti?” → ağacı; -ı eki almıştır.','B: belirtili nesne')],
 'Nesneye -i ekini eklemeden de cümle kuruluyorsa belirtisiz, eki varsa belirtilidir.')

Qd('0010','K-DBOG-03','orta','Nesnesi söz öbeği olan cümleyi belirler.',3,
 'Aşağıdaki cümlelerin hangisinin nesnesi bir söz öbeğidir?',
 'Çocuk bahçenin çiçeklerini suladı.','A',
 [('Annem sabah erkenden çayı demledi.','Nesne “çayı” tek sözcüktür.','dikkat'),
  ('Kerem yarın sınava girecek.','Nesne yoktur; “sınava” yönelme hâlindeki dolaylı tümleçtir.','bilgi'),
  ('Misafirler yemeği çabucak yedi.','Nesne “yemeği” tek sözcüktür.','dikkat'),
  ('Ayşe hızla koşup otobüse yetişti.','Nesne yoktur; “otobüse” dolaylı tümleçtir.','bilgi')],
 'Nesnesi bir söz öbeği olan cümle.','Yükleme “neyi?” diye sor; cevap birden çok sözcük mü?',[B_NES],
 [AD('Nesneyi bul','Yükleme “neyi?, ne?” diye sorulur; cevap nesnedir.','neyi? → nesne'),
  AD('Şıkları sına','B: çayı · D: yemeği (tek sözcük) · C ve E’de nesne yok (sınava, otobüse: dolaylı tümleç).','B, D: tek sözcük · C, E: nesne yok'),
  AD('Öbeği seç','A’da “neyi suladı?” → bahçenin çiçeklerini (ad tamlaması + belirtme eki).','A: öbek nesne')],
 'Nesne de özne gibi tek sözcük olmak zorunda değildir; soruya verilen cevabı tamlamasıyla birlikte al.')

Qd('0011','K-DBOG-03','orta','Nesne ile dolaylı tümlecin bir arada bulunduğu cümleyi belirler.',4,
 'Aşağıdaki cümlelerin hangisinde hem nesne hem dolaylı tümleç bulunur?',
 'Elif kitabı arkadaşına verdi.','D',
 [('Çocuklar bütün gün sessizce oynadı.','Nesne de dolaylı tümleç de yoktur; yalnız zarf tümleçleri vardır.','bilgi'),
  ('Kerem yarınki sınava hazırlanıyor.','Yalnız dolaylı tümleç var (sınava); nesne yoktur.','dikkat'),
  ('Annem akşam yemeğini erkenden hazırladı.','Yalnız nesne var (akşam yemeğini); dolaylı tümleç yoktur.','dikkat'),
  ('Öğrenciler yaşlı amcaya sevgiyle gülümsedi.','Yalnız dolaylı tümleç var (yaşlı amcaya); nesne yoktur.','dikkat')],
 'Nesne ve dolaylı tümleci birlikte taşıyan cümle.','Her cümlede hem “neyi?” hem “kime/neye?” sorularına cevap ara.',[B_NES,B_DOL],
 [AD('İki ögeyi ayır','“Neyi?” sorusuna cevap nesne, “kime?, neye?” sorusuna cevap dolaylı tümleçtir.','neyi? → nesne · kime? → dolaylı tümleç'),
  AD('Şıkları ele','A: hiçbiri · B: yalnız dolaylı · C: yalnız nesne · E: yalnız dolaylı.','A, B, C, E: yalnız biri ya da hiçbiri'),
  AD('İkisini bul','D’de “neyi verdi?” → kitabı (nesne); “kime verdi?” → arkadaşına (dolaylı tümleç).','D: nesne + dolaylı tümleç')],
 'İki ögeyi ayrı ayrı sorgula: “neyi?” ve “kime?” sorularının her ikisine de cevap varsa ikisi birliktedir.')

Qx('0012','K-DBOG-03','orta','Belirtisiz nesneli cümleleri belirtili nesne ve nesnesiz cümlelerden ayırır.',4,
 'I. Ayşe masadaki çiçekleri suladı.\nII. Kerem bu yıl yeni bir bisiklet aldı.\nIII. Kardeşim bahçeye hızla koştu.\nIV. Annem her akşam sebze çorbası pişirir.\n\nNumaralanmış cümlelerin hangilerinde belirtisiz nesne vardır?',
 [('Yalnız II','IV’te de “sebze çorbası” ek almayan belirtisiz nesnedir.','dikkat'),
  ('I ve IV','I’deki “çiçekleri” -i eki almıştır; belirtilidir, belirtisiz değil.','dikkat'),
  ('II ve IV',None,None),
  ('II, III ve IV','III’te nesne yoktur; “bahçeye” dolaylı tümleçtir.','bilgi'),
  ('I, II ve IV','I’deki nesne belirtilidir (çiçekleri).','dikkat')],
 'C','Belirtisiz nesne bulunan cümleleri belirlemek.','Önce nesneyi “neyi?/ne?” ile bul; sonra -i eki alıp almadığına bak.',[B_NES],
 [AD('Nesneleri bul','I: çiçekleri · II: yeni bir bisiklet · III: nesne yok (bahçeye: dolaylı) · IV: sebze çorbası.','I: çiçekleri · II: bisiklet · III: yok · IV: çorba'),
  AD('Belirtme ekine bak','“Çiçekleri” -i eki almış (belirtili); “bisiklet” ve “sebze çorbası” ek almamış (belirtisiz).','I: belirtili · II, IV: belirtisiz'),
  AD('Sonucu seç','Belirtisiz nesne II ve IV’tedir.','II ve IV')],
 'Önce nesnenin var olup olmadığına bak; sonra yalnız -i eki alıp almadığına.',kalip='öncüllü')

# ---------- DOLAYLI TÜMLEÇ ----------
Qd('0013','K-DBOG-04','kolay','Dolaylı tümleci olan cümleyi belirler.',2,
 'Aşağıdaki cümlelerin hangisinde dolaylı tümleç vardır?',
 'Çocuk annesine sevinçle koştu.','E',
 [('Öğrenciler dikkatle öğretmenini dinledi.','“Öğretmenini” -i eki almış belirtili nesnedir; dolaylı tümleç yoktur.','dikkat'),
  ('Kardeşim yeni bir oyuncak istiyor.','“Yeni bir oyuncak” belirtisiz nesnedir; dolaylı tümleç yoktur.','bilgi'),
  ('Ahmet sabah gazeteyi okudu.','“Gazeteyi” belirtili nesnedir; dolaylı tümleç yoktur.','bilgi'),
  ('Yağmur gece boyunca yağdı.','“Gece boyunca” edat tümlecidir (zarf tümleci); dolaylı tümleç değildir.','dikkat')],
 'Dolaylı tümleci bulunan cümle.','Yükleme “kime?, neye?” diye sor.',[B_DOL],
 [AD('Dolaylı tümleci hatırla','Yüklemin -e, -de, -den hâl ekli tümleci; “kime?, neye?, kimden?” sorularına cevap verir.','kime? neye? → dolaylı tümleç'),
  AD('Şıkları sına','A: öğretmenini (nesne) · B: oyuncak (nesne) · C: gazeteyi (nesne) · D: gece boyunca (edat tümleci).','A, B, C, D: dolaylı tümleç yok'),
  AD('Dolaylıyı seç','E’de “kime koştu?” → annesine.','E: dolaylı tümleç')],
 'Yükleme “kime/neye?” sorusu sorulduğunda cevap veren -e ekli öbek dolaylı tümleçtir.')

Qd('0014','K-DBOG-04','zor','Dolaylı tümleci bulunmayan cümleyi, -e ekli edat öbeğine aldanmadan belirler.',3,
 'Dolaylı tümleç bulunmayan cümle aşağıdakilerden hangisidir?',
 'Hepimiz sonuçları sabaha kadar bekledik.','B',
 [('Mektubu arkadaşıma gönderdim.','“Arkadaşıma” yönelme hâlindeki dolaylı tümleçtir.','bilgi'),
  ('Annem yeni aldığı kitabı kardeşime verdi.','“Kardeşime” dolaylı tümleçtir.','bilgi'),
  ('Çocuk anneannesine mektup yazdı.','“Anneannesine” dolaylı tümleçtir.','bilgi'),
  ('Öğrenciler tahtadaki soruya cevap aradı.','“Soruya” yönelme hâlindeki dolaylı tümleçtir.','bilgi')],
 'Dolaylı tümleci olmayan cümle.','Yükleme “kime?, neye?” sorusunu yönelt; edatlı öbeği dolaylı tümleç sayma.',[B_DOL,B_EDAT],
 [AD('Soruyu hatırla','Dolaylı tümleç “kime?, neye?, kimden?” sorularına cevap verir.','kime? neye? kimden?'),
  AD('Dolaylıları bul','A: arkadaşıma · C: kardeşime · D: anneannesine · E: soruya.','A, C, D, E: dolaylı tümleç var'),
  AD('Olmayanı seç','B’de “bekledik” yüklemine “neyi?” → sonuçları (nesne); “sabaha kadar” edat tümlecidir (zarf tümleci), -e eki taşısa da dolaylı tümleç değildir.','B: dolaylı tümleç yok')],
 '“-e” ekli her öbek dolaylı tümleç değildir: “kadar, göre” gibi edatlı öbekler zarf tümlecidir.')

Qd('0015','K-DBOG-04','zor','Birden çok dolaylı tümleci edat tümlecinden ayırarak sayar.',4,
 'Aşağıdaki cümlelerin hangisinde birden fazla dolaylı tümleç vardır?',
 'Kerem arkadaşından kardeşine bir kitap getirdi.','A',
 [('Elif dün öğretmenine kısa sorusunu cesaretle sordu.','Yalnız bir dolaylı tümleç var (öğretmenine).','dikkat'),
  ('Ahmet dün akşam yeni aldığı kitabını sonunda bitirdi.','Dolaylı tümleç yok; “dün akşam” zarf tümleci, “kitabını” nesnedir.','bilgi'),
  ('Kardeşim odasına girip kapıyı sessizce kapattı.','Yalnız bir dolaylı tümleç var (odasına).','dikkat'),
  ('Bu çocuk yaşıtlarına göre gerçekten çok sessizdir.','“Yaşıtlarına göre” edat tümlecidir; -e eki taşısa da dolaylı tümleç değildir.','dikkat')],
 'İkiden çok dolaylı tümleçli cümle.','Her cümlede “kimden?” ve “kime?” sorularına verilen cevapları say; edatlı öbeğe dikkat et.',[B_DOL,B_EDAT],
 [AD('Dolaylı tümleçleri say','“Kime?, neye?, kimden?” sorularına cevap veren öbekleri sayarız.','kime? kimden? → dolaylı'),
  AD('Şıkları say','B: 1 (öğretmenine) · C: 0 · D: 1 (odasına) · E: 0 (yaşıtlarına göre = edat tümleci).','B: 1 · C: 0 · D: 1 · E: 0'),
  AD('İkiliyi seç','A’da “kimden getirdi?” → arkadaşından; “kime getirdi?” → kardeşine; iki dolaylı tümleç var.','A: 2')],
 '“-e” eki gören her sözcüğü dolaylı tümleç sayma: edat (göre, kadar) alan öbek edat tümlecidir.')

# ---------- ZARF TÜMLECİ ----------
Qd('0016','K-DBOG-05','kolay','Zarf tümleci bulunan cümleyi belirler.',2,
 'Aşağıdaki cümlelerin hangisinde zarf tümleci vardır?',
 'Öğretmen soruları yavaşça anlattı.','C',
 [('Ayşe yeni aldığı defteri çantasına koydu.','Nesne (defteri) ve dolaylı tümleç (çantasına) var; zarf tümleci yoktur.','dikkat'),
  ('Kerem annesine bir mektup yazdı.','Dolaylı tümleç ve nesne var; zarf tümleci yoktur.','bilgi'),
  ('Çocuklar bahçedeki kediyi sevdi.','Yalnız nesne (bahçedeki kediyi) var; zarf tümleci yoktur.','bilgi'),
  ('Babam eski arabayı sattı.','Yalnız nesne (eski arabayı) var; zarf tümleci yoktur.','bilgi')],
 'Zarf tümleci bulunan cümle.','Yükleme “nasıl?, ne zaman?, ne kadar?” diye sor.',[B_ZAR],
 [AD('Zarf tümlecini hatırla','Yüklemin nasıl, ne zaman, ne kadar yapıldığını bildirir; hâl eki almaz.','nasıl? ne zaman? → zarf tümleci'),
  AD('Şıkları sına','A, B, D, E’de “nasıl?, ne zaman?” sorularına cevap yok; yalnız nesne ve dolaylı tümleçler var.','A, B, D, E: zarf tümleci yok'),
  AD('Zarfı seç','C’de “nasıl anlattı?” → yavaşça (durum bildirir).','C: zarf tümleci')],
 'Yükleme “nasıl?, ne zaman?, ne kadar?” sorularından birine cevap veren sözcük zarf tümlecidir.')

Qd('0017','K-DBOG-05','kolay','Zaman bildiren zarf tümlecini diğer zarf tümleçlerinden ayırır.',3,
 'Aşağıdaki cümlelerin hangisinde zaman bildiren bir zarf tümleci vardır?',
 'Misafirlerimiz akşamleyin yola çıkacak.','A',
 [('Kardeşim arkadaşlarıyla parka gitti.','“Arkadaşlarıyla” zarf tümlecidir ama zaman değil, birliktelik bildirir.','dikkat'),
  ('Çocuk hızla merdivenleri çıktı.','“Hızla” durum bildiren zarf tümlecidir; zaman bildirmez.','dikkat'),
  ('Annem sofraya sıcak yemekleri koydu.','Zaman bildiren sözcük yok; “sofraya” dolaylı tümleç, “yemekleri” nesnedir.','bilgi'),
  ('Ayşe odadaki kitapları düzenledi.','Zaman bildiren zarf tümleci yoktur; yalnız nesne (odadaki kitapları) vardır.','bilgi')],
 'Zaman bildiren zarf tümleci olan cümle.','Yükleme “ne zaman?” diye sor.',[B_ZAR],
 [AD('Zaman zarfını hatırla','Yükleme “ne zaman?” diye sorulduğunda cevap veren hâl eksiz sözcük zaman zarf tümlecidir.','ne zaman? → zaman zarf tümleci'),
  AD('Şıkları sına','B: arkadaşlarıyla (birliktelik) · C: hızla (durum) · D, E: zaman yok.','B, C: zaman değil · D, E: zaman yok'),
  AD('Zamanı seç','A’da “ne zaman çıkacak?” → akşamleyin; -leyin eki zaman bildirir.','A: zaman zarf tümleci')],
 '“Ne zaman?” sorusuna cevap veren hâl eksiz sözcük ya da -leyin gibi eklerle kurulan sözcük zaman zarf tümlecidir.')

Qd('0018','K-DBOG-05','orta','Edat tümlecini dolaylı tümleç ve öteki ögelerden ayırır.',4,
 'Aşağıdaki cümlelerin hangisinde edat tümleci vardır?',
 'Bu çocuk yaşına göre çok olgun konuşuyor.','E',
 [('Annem pazardan taze sebze aldı.','Edat yoktur; “taze sebze” nesne, “pazardan” ayrılma hâlindeki dolaylı tümleçtir.','bilgi'),
  ('Kerem yarın erkenden yola çıkacak.','Edat yoktur; “yarın erkenden” zaman bildiren zarf tümlecidir.','dikkat'),
  ('Küçük kız elindeki balonu uçurdu.','Edat yoktur; “elindeki balonu” nesnedir.','bilgi'),
  ('Öğretmen tahtadaki soruyu yeniden yazdı.','Edat yoktur; “yeniden” zarf tümleci, “tahtadaki soruyu” nesnedir.','dikkat')],
 'Edat tümleci bulunan cümle.','Cümlelerde “göre, için, kadar, gibi, ile” gibi bir edat ara.',[B_EDAT],
 [AD('Edat tümlecini hatırla','Edat + sözcük öbeği, yüklemi tamamlayan zarf tümlecidir: yaşına göre, sabaha kadar.','edat öbeği → zarf tümleci'),
  AD('Şıklarda edat ara','A, B, C, D’de “göre, için, kadar, gibi, ile” gibi bir edat yoktur.','A, B, C, D: edat tümleci yok'),
  AD('Edatlıyı seç','E’de “yaşına göre”, “göre” edatıyla kurulmuş edat tümlecidir.','E: edat tümleci')],
 'Edatın başına gelen -e, -i gibi ek hâl eki değil, edatın gerektirdiği ektir; öbek dolaylı değil zarf tümlecidir.')

Qd('0019','K-DBOG-05','zor','Cümledeki zarf tümleçlerini sayar.',4,
 'Aşağıdaki cümlelerin hangisinde birden çok zarf tümleci vardır?',
 'Çiftçi bu sabah tarlayı çabucak sürdü.','D',
 [('Küçük kız eve gelen annesine sıkıca sarıldı.','Yalnız bir zarf tümleci var (sıkıca); “annesine” dolaylı tümleçtir.','dikkat'),
  ('Öğretmen dün yeni konuyu öğrencilere anlattı.','Yalnız bir zarf tümleci var (dün).','dikkat'),
  ('Çocuklar kitaplarını çantalarına koydu.','Zarf tümleci yoktur; yalnız nesne ve dolaylı tümleç vardır.','bilgi'),
  ('Kerem sessizce odasına girdi.','Yalnız bir zarf tümleci var (sessizce); “odasına” dolaylı tümleçtir.','dikkat')],
 'İkiden çok zarf tümleçli cümle.','Her cümlede “ne zaman?” ve “nasıl?” sorularına verilen cevapları say.',[B_ZAR],
 [AD('Zarf tümleçlerini say','“Ne zaman?, nasıl?, ne kadar?” sorularının her cevabı ayrı bir zarf tümlecidir.','ne zaman? nasıl? → zarf tümleci'),
  AD('Şıkları say','A: sıkıca (1) · B: dün (1) · C: yok (0) · E: sessizce (1).','A: 1 · B: 1 · C: 0 · E: 1'),
  AD('Çoklu olanı seç','D’de “ne zaman?” → bu sabah; “nasıl?” → çabucak; iki zarf tümleci.','D: 2')],
 'Zaman, durum, miktar ve edat öbeklerini ayrı ayrı sayarsan yanılmazsın.')

# ---------- ÖGELERİN SIRALANIŞI ----------
SIRA_MET='Bu cümlenin ögeleri sırasıyla hangi seçenekte verilmiştir?'
def SQ(no,zor,kaz,adim,cumle,dogru,yan,harf,ip,adimlar,puf):
    """cumle: numaralı öbekli cümle; dogru: öge listesi; yan: 4 × (öge listesi, cel, tur)."""
    Qd(no,'K-DBOG-06',zor,kaz,adim,cumle+'\n\n'+SIRA_MET,sira(*dogru),harf,[(sira(*l),c,t) for l,c,t in yan],
       'Numaralı öbeklerin öge adları, sırasıyla.',ip,[B_SIRA],adimlar,puf,kalip='öncüllü')

SQ('0020','orta','Numaralı öbekleri özne, zarf tümleci, dolaylı tümleç, nesne ve yüklem olarak adlandırır.',3,
 'Küçük kız (I) sabah erkenden (II) annesine (III) çiçekler (IV) topladı (V).',
 ['özne','zarf tümleci','dolaylı tümleç','nesne','yüklem'],
 [(['özne','dolaylı tümleç','zarf tümleci','nesne','yüklem'],'“Sabah erkenden” ne zaman? sorusunun cevabı olduğundan zarf tümleci, “annesine” kime? sorusunun cevabı olduğundan dolaylı tümleçtir; ikisi ters yazılmış.','dikkat'),
  (['özne','zarf tümleci','nesne','nesne','yüklem'],'“Annesine” yönelme hâlindedir (kime?); nesne değil, dolaylı tümleçtir.','bilgi'),
  (['özne','zarf tümleci','dolaylı tümleç','özne','yüklem'],'“Çiçekler” “topladı” yüklemine “neyi?” sorusunun cevabıdır; özne değil, belirtisiz nesnedir.','bilgi'),
  (['özne','zarf tümleci','zarf tümleci','nesne','yüklem'],'“Annesine” zarf tümleci değil; “kime?” sorusuna cevap veren dolaylı tümleçtir.','bilgi')],
 'B','Yükleme sırayla sor: kim? → özne · ne zaman? → zarf tümleci · kime? → dolaylı tümleç · neyi? → nesne.',
 [AD('Yüklemi bul','“Topladı” yüklemdir (V).','V: yüklem'),
  AD('Yükleme sor','Kim topladı? → küçük kız · ne zaman? → sabah erkenden · kime? → annesine · neyi? → çiçekler.','I: özne · II: zarf · III: dolaylı · IV: nesne'),
  AD('Diziyi oku','Sıra: özne, zarf tümleci, dolaylı tümleç, nesne, yüklem.','B')],
 'Her numaralı öbeğe yükleme göre ayrı soru sor; sıraya değil sorulara güven.')

SQ('0021','orta','Ögelerin sırasını yer değiştirmiş (nesne başta) bir cümlede belirler.',3,
 'Yeni açılan müzeyi (I) bütün öğrenciler (II) büyük bir hayranlıkla (III) gezdi (IV).',
 ['nesne','özne','zarf tümleci','yüklem'],
 [(['özne','nesne','zarf tümleci','yüklem'],'Başta gelen “yeni açılan müzeyi” -i eki almış nesnedir; özneyi eylemi yapan “bütün öğrenciler” oluşturur.','dikkat'),
  (['nesne','özne','dolaylı tümleç','yüklem'],'“Büyük bir hayranlıkla” nasıl? sorusuna cevap verir; zarf tümlecidir, dolaylı tümleç değil.','bilgi'),
  (['zarf tümleci','özne','zarf tümleci','yüklem'],'“Yeni açılan müzeyi” neyi? sorusuna cevap veren nesnedir, zarf tümleci değil.','bilgi'),
  (['nesne','özne','nesne','yüklem'],'“Büyük bir hayranlıkla” yükleme “nasıl?” diye cevap verir; nesne değil, zarf tümlecidir.','bilgi')],
 'D','Önce yükleme “kim?” ve “neyi?” sor; baştaki öbek özne olmak zorunda değil.',
 [AD('Yüklemi bul','“Gezdi” yüklemdir (IV).','IV: yüklem'),
  AD('Yükleme sor','Neyi gezdi? → yeni açılan müzeyi · kim gezdi? → bütün öğrenciler · nasıl? → büyük bir hayranlıkla.','I: nesne · II: özne · III: zarf'),
  AD('Diziyi oku','Sıra: nesne, özne, zarf tümleci, yüklem.','D')],
 'Cümlenin başındaki öbek özne olmayabilir; “kim?” sorusunu sormadan öge adı verme.')

SQ('0022','kolay','Kısa bir isim cümlesinin ögelerini sırasıyla adlandırır.',2,
 'Bayram günü (I) köyümüzün çarşısı (II) kalabalıktı (III).',
 ['zarf tümleci','özne','yüklem'],
 [(['özne','zarf tümleci','yüklem'],'“Bayram günü” kim? sorusunun değil, ne zaman? sorusunun cevabıdır; zarf tümlecidir. Özne “köyümüzün çarşısı”dır.','bilgi'),
  (['nesne','özne','yüklem'],'“Bayram günü” neyi? sorusuna cevap vermez; zaman bildirir, zarf tümlecidir.','bilgi'),
  (['zarf tümleci','nesne','yüklem'],'“Köyümüzün çarşısı” kalabalık olan varlıktır; kim/ne? sorusunun cevabı olan öznedir, nesne değil.','bilgi'),
  (['dolaylı tümleç','özne','yüklem'],'“Bayram günü” hâl eki almamış zaman bildiren öbektir; dolaylı tümleç değil, zarf tümlecidir.','dikkat')],
 'A','Yükleme “ne zaman?” ve “ne kalabalıktı?” diye sor.',
 [AD('Yüklemi bul','“Kalabalıktı” yüklemdir (III), isim soyludur.','III: yüklem'),
  AD('Yükleme sor','Ne kalabalıktı? → köyümüzün çarşısı · ne zaman? → bayram günü.','I: zarf · II: özne'),
  AD('Diziyi oku','Sıra: zarf tümleci, özne, yüklem.','A')],
 'Zamanı bildiren hâl eksiz öbek zarf tümlecidir; özne yükleme “kim/ne?” diye sorarak bulunur.')

SQ('0023','zor','Beş ögeli bir cümlede -e ekli edat öbeğini dolaylı tümleçten ayırarak adlandırır.',4,
 'Öğretmenimiz (I) öğrencilere (II) ilgilerine göre (III) birer kitap (IV) verdi (V).',
 ['özne','dolaylı tümleç','zarf tümleci','nesne','yüklem'],
 [(['özne','dolaylı tümleç','dolaylı tümleç','nesne','yüklem'],'“İlgilerine göre” edat tümlecidir (zarf tümleci); -e eki taşısa da dolaylı tümleç değildir.','dikkat'),
  (['özne','dolaylı tümleç','zarf tümleci','dolaylı tümleç','yüklem'],'“Birer kitap” neyi? sorusunun cevabıdır; belirtisiz nesnedir, dolaylı tümleç değil.','bilgi'),
  (['özne','zarf tümleci','dolaylı tümleç','nesne','yüklem'],'Sıra ters okunmuş: “öğrencilere” kime? sorusunun cevabı (dolaylı tümleç), “ilgilerine göre” edat tümlecidir (zarf tümleci).','dikkat'),
  (['özne','nesne','zarf tümleci','nesne','yüklem'],'“Öğrencilere” yönelme hâlindedir (kime?); nesne değil, dolaylı tümleçtir.','bilgi')],
 'C','Yükleme sırayla sor: kim? kime? nasıl? neyi? “göre” edatlı öbeği ayrı değerlendir.',
 [AD('Yüklemi bul','“Verdi” yüklemdir (V).','V: yüklem'),
  AD('Yükleme sor','Kim verdi? → öğretmenimiz · kime? → öğrencilere · nasıl? → ilgilerine göre (edat öbeği) · neyi? → birer kitap.','I: özne · II: dolaylı · III: zarf · IV: nesne'),
  AD('Diziyi oku','Sıra: özne, dolaylı tümleç, zarf tümleci, nesne, yüklem.','C')],
 '“-e” eki gören her öbeği dolaylı tümleç sayma: edatla (göre, kadar) kurulan öbek zarf tümlecidir.')

SQ('0024','orta','Yüklemi başta olan (devrik) cümlenin ögelerini sırasıyla adlandırır.',3,
 'Kapatmış (I) dükkânını (II) yaşlı terzi (III).',
 ['yüklem','nesne','özne'],
 [(['yüklem','özne','nesne'],'“Dükkânını” neyi? sorusunun cevabıdır (nesne); “yaşlı terzi” kim kapatmış? sorusunun cevabıdır (özne); ikisi ters yazılmış.','dikkat'),
  (['yüklem','nesne','dolaylı tümleç'],'“Yaşlı terzi” kim kapatmış? sorusunun cevabıdır; dolaylı tümleç değil, öznedir.','bilgi'),
  (['yüklem','dolaylı tümleç','özne'],'“Dükkânını” -i eki almıştır ve neyi? sorusuna cevap verir; dolaylı tümleç değil, nesnedir.','bilgi'),
  (['özne','nesne','yüklem'],'Yüklem “kapatmış”tır ve cümlenin başındadır (devrik); sondaki “yaşlı terzi” yüklem değildir.','dikkat')],
 'E','İlk öbeğin yüklem olup olmadığına bak: yüklem cümlenin başında da olabilir.',
 [AD('Yüklemi bul','“Kapatmış” çekimli eylemdir; yüklem başa gelmiştir (I).','I: yüklem'),
  AD('Yükleme sor','Neyi kapatmış? → dükkânını · kim kapatmış? → yaşlı terzi.','II: nesne · III: özne'),
  AD('Diziyi oku','Sıra: yüklem, nesne, özne.','E')],
 'Yüklem başa taşınsa da ögelerin adı değişmez; yüklemi bul, sonra sor.')

# ---------- FARKLI ÖGE ----------
FARK='Bu cümlede numaralanmış öbeklerden hangisi öge olarak ötekilerden farklıdır?'
def FQ(no,zor,kaz,cumle,idx,celler,ip,adimlar,puf):
    """idx: doğru (farklı) numaranın 0 tabanlı indeksi; celler: 5 elemanlı (farklı için None) cel metni."""
    harf='ABCDE'[idx]
    Qx(no,'K-DBOG-07',zor,kaz,3,cumle+'\n\n'+FARK,[(r,celler[i],None if celler[i] is None else 'bilgi') for i,r in enumerate(['I','II','III','IV','V'])],harf,
       'Ögesi ötekilerden farklı olan öbek.',ip,[B_SIRA],adimlar+[AD('Sonucu seç','Ögesi ötekilerden ayrılan öbek '+['I','II','III','IV','V'][idx]+' numaralı öbektir.',['I','II','III','IV','V'][idx])],puf,kalip='öncüllü')

FQ('0025','orta','Dört özne arasından zarf tümleci olan öbeği bulur.',
 'Elif (I), Deniz (II), Kerem (III) ve ben (IV) bu gece (V) yola çıkacağız.',4,
 ['“Çıkacağız” yüklemini yapan öznelerden biridir (Elif).','“Çıkacağız” yüklemini yapan öznelerden biridir (Deniz).','“Çıkacağız” yüklemini yapan öznelerden biridir (Kerem).','“Çıkacağız” yüklemini yapan öznelerden biridir (ben).',None],
 'Her öbeğe yükleme göre “kim?, ne zaman?” diye sor.',
 [AD('Öbeklere sor','Çıkacak olan kim? → Elif, Deniz, Kerem, ben (I–IV) · ne zaman? → bu gece (V).','I–IV: özne · V: zarf tümleci'),
  AD('Farklıyı bul','Dört öbek özne; “bu gece” zaman bildiren zarf tümlecidir.','V')],
 'Sıralanan öbekler aynı yükleme bağlıysa aynı ögedir; farklı soruya cevap veren öbeği ara.')

FQ('0026','kolay','Dört belirtili nesne arasından dolaylı tümleci bulur.',
 'Kardeşim kitabı (I), defterini (II) ve kalemlerini (III) çantasına (IV) koyup ceketini (V) giydi.',3,
 ['“Kitabı” neyi? sorusunun cevabıdır; belirtili nesnedir.','“Defterini” neyi? sorusunun cevabıdır; belirtili nesnedir.','“Kalemlerini” neyi? sorusunun cevabıdır; belirtili nesnedir.',None,'“Ceketini” neyi giydi? sorusunun cevabıdır; belirtili nesnedir.'],
 'Her öbeğe “neyi?” ve “nereye?/kime?” sorularını sor.',
 [AD('Öbeklere sor','Neyi koydu? → kitabı, defterini, kalemlerini · nereye? → çantasına · neyi giydi? → ceketini.','I, II, III, V: nesne · IV: dolaylı'),
  AD('Farklıyı bul','Dört öbek -i eki almış nesnedir; “çantasına” yönelme hâlindeki dolaylı tümleçtir.','IV')],
 'Sıralanan ögeler arasında ek (-i / -e) değişen öbek farklı ögedir.')

FQ('0027','orta','Dört dolaylı tümleç arasından nesneyi bulur.',
 'Elif arkadaşına (I) ve kardeşine (II) mektubu (III) yolladı; annesine (IV) ve babasına (V) telefon etti.',2,
 ['“Kime yolladı?” sorusunun cevabıdır; dolaylı tümleçtir.','“Kime yolladı?” sorusunun cevabıdır; dolaylı tümleçtir.',None,'“Kime telefon etti?” sorusunun cevabıdır; dolaylı tümleçtir.','“Kime telefon etti?” sorusunun cevabıdır; yönelme hâlindeki dolaylı tümleçtir.'],
 'Her öbeği bağlı olduğu fiile göre sorgula; -e ekli olmayan öbeği ara.',
 [AD('Öbeklere sor','Kime yolladı? → arkadaşına, kardeşine · neyi yolladı? → mektubu · kime telefon etti? → annesine, babasına.','I, II, IV, V: dolaylı · III: nesne'),
  AD('Farklıyı bul','Dört öbek -e eki almış dolaylı tümleç; “mektubu” -i eki almış nesnedir.','III')],
 'Aynı ekle biten öbekler çoğu kez aynı ögedir; eki farklı olanı sorgula.')

# ---------- AYNI ÖGEYİ TAŞIYAN ----------
AYNI='Aşağıdaki cümlelerin hangisinde numaralanmış iki öbek aynı ögedir?'
def AQ(no,zor,kaz,metin,dogru,harf,yan,ip,adimlar,puf):
    Qd(no,'K-DBOG-08',zor,kaz,3,metin,dogru,harf,yan,'Numaralı iki öbeğin aynı öge olduğu cümle.',ip,[B_SIRA],adimlar,puf,kalip='öncüllü')

AQ('0028','orta','Zaman ve durum zarf tümlecinin aynı öge olduğunu görür.',AYNI,
 'Kerem akşamları (I) yavaşça (II) yürür.','A',
 [('Annem bize (I) çay (II) getirdi.','“Bize” dolaylı tümleç, “çay” nesnedir; farklı ögelerdir.','dikkat'),
  ('Komşumuz (I) sabaha kadar (II) bekledi.','“Komşumuz” özne, “sabaha kadar” edat tümlecidir (zarf tümleci); farklı ögelerdir.','dikkat'),
  ('Çocuk (I) kitabı (II) okudu.','“Çocuk” özne, “kitabı” nesnedir.','bilgi'),
  ('Öğretmen (I) bize (II) soru sordu.','“Öğretmen” özne, “bize” dolaylı tümleçtir.','bilgi')],
 'Her numaralı öbeğe yükleme göre soru sor.',
 [AD('Öbeklere sor','A: ne zaman? → akşamları (I) · nasıl? → yavaşça (II).','I, II: zarf tümleci'),
  AD('Şıkları ele','B: dolaylı + nesne · C: özne + zarf · D: özne + nesne · E: özne + dolaylı.','B, C, D, E: farklı ögeler'),
  AD('Sonucu seç','A’daki iki öbek de zarf tümlecidir.','A')],
 'Zaman ve durum bildiren öbeklerin ikisi de zarf tümlecidir; “nasıl?, ne zaman?” sorularını ayrı sorsan da öge adı aynıdır.')

AQ('0029','orta','Aynı yükleme bağlı sıralı iki nesnenin aynı öge olduğunu görür.','Numaralanmış öbeklerin birbiriyle aynı ögeyi taşıdığı cümle hangisidir?',
 'Elif ödevini (I) ve mektubunu (II) tamamladı.','E',
 [('Kardeşim bize (I) elma (II) getirdi.','“Bize” dolaylı tümleç, “elma” nesnedir; farklı ögelerdir.','bilgi'),
  ('Babam (I) arabayı (II) sattı.','“Babam” özne, “arabayı” nesnedir.','bilgi'),
  ('Misafirler (I) akşama kadar (II) kaldı.','“Misafirler” özne, “akşama kadar” edat tümlecidir.','bilgi'),
  ('Yaşlı adam bu akşam (I) arkadaşına (II) uğradı.','“Bu akşam” zarf tümleci, “arkadaşına” dolaylı tümleçtir.','dikkat')],
 'Her öbeğe aynı yükleme göre soru sor.',
 [AD('Öbeklere sor','E: neyi tamamladı? → ödevini (I) ve mektubunu (II).','I, II: nesne'),
  AD('Bağlantıya bak','İki öbek “ve” ile sıralanmış, aynı yükleme bağlı belirtili nesnelerdir.','I, II: aynı yüklem, aynı soru'),
  AD('Şıkları ele','A: dolaylı + nesne · B: özne + nesne · C: özne + zarf · D: zarf + dolaylı.','A, B, C, D: farklı ögeler')],
 '“Ve” ile sıralanan öbekler aynı yükleme aynı soruyu yanıtlıyorsa aynı ögedir.')

AQ('0030','zor','İki dolaylı tümleci, -e ekli edat öbeğinden ayırarak aynı öge olarak eşleştirir.','Hangi cümlede (I) ve (II) ile gösterilen öbekler öge bakımından birbirinin aynısıdır?',
 'Elif öğretmeninden (I) arkadaşına (II) bir not getirdi.','B',
 [('Dün akşam (I) komşumuz (II) çocuklarıyla birlikte geldi.','“Dün akşam” zarf tümleci, “komşumuz” özne; farklı ögelerdir.','dikkat'),
  ('Annem yemeği (I) sofraya (II) özenle koydu.','“Yemeği” nesne, “sofraya” dolaylı tümleçtir.','dikkat'),
  ('Kerem öğleye kadar (I) kardeşine (II) baktı.','“Öğleye kadar” edat tümlecidir (zarf tümleci); “kardeşine” dolaylı tümleçtir; -e eki taşısalar da farklı ögelerdir.','dikkat'),
  ('Öğretmen (I) soruyu (II) tahtaya özenle yazdı.','“Öğretmen” özne, “soruyu” nesnedir.','bilgi')],
 'Hâl eklerine ve “kimden?, kime?” sorularına bak; edatlı öbeği ayrı değerlendir.',
 [AD('Öbeklere sor','B: kimden getirdi? → öğretmeninden (I) · kime getirdi? → arkadaşına (II).','I, II: dolaylı tümleç'),
  AD('Şıkları ele','A: zarf + özne · C: zarf + dolaylı · D: özne + zarf · E: özne + nesne.','A, C, D, E: farklı ögeler'),
  AD('Sonucu seç','B’deki iki öbek de dolaylı tümleçtir (-den ve -e).','B')],
 '-den ve -e eki farklı hâl eki olsa da ikisi de dolaylı tümleç kurar.')

Qx('0031','K-DBOG-08','zor','Altı numaralı öbekten, edat tümlecini de gözeterek aynı ögeyi taşıyan ikisini bulur.',3,
 'Elif (I) geceye kadar (II) arkadaşına (III) sabırla (IV) mektubunu (V) yazdı (VI).\n\nBu cümlede numaralanmış öbeklerden hangi ikisi aynı ögedir?',
 [('I ve V','I özne, V nesnedir; aynı öge değildir.','dikkat'),
  ('II ve III','II edat tümleci (zarf tümleci), III dolaylı tümleçtir; ikisi de -e ekli olsa da aynı öge değildir.','dikkat'),
  ('II ve IV',None,None),
  ('III ve V','III dolaylı tümleç, V nesnedir; aynı öge değildir.','bilgi'),
  ('IV ve VI','IV zarf tümleci, VI yüklemdir.','bilgi')],
 'C','Aynı ögeyi taşıyan iki öbek.','Yükleme tek tek sor: kim? ne zamana kadar? kime? nasıl? neyi?',[B_SIRA],
 [AD('Yüklemi bul','“Yazdı” yüklemdir (VI).','VI: yüklem'),
  AD('Yükleme sor','Kim? → Elif (I) · ne zamana kadar? → geceye kadar (II) · kime? → arkadaşına (III) · nasıl? → sabırla (IV) · neyi? → mektubunu (V).','I: özne · II: zarf (edat tümleci) · III: dolaylı · IV: zarf · V: nesne'),
  AD('Aynı olanı seç','Edat öbeği (II) ve durum bildiren sözcük (IV) zarf tümlecidir.','II ve IV')],
 'Öge adlarını yazıp aynı adı iki kez gördüğün öbekleri eşleştir.',kalip='öncüllü')

# ---------- ARA SÖZ ----------
Qx('0032','K-DBOG-09','orta','Numaralı öbeklerden ara sözü (öge olmayan söz) bulur.',3,
 'Elif (I), yanılmıyorsam (II), bu yıl (III) ödül (IV) aldı (V).\n\nBu cümlede numaralanmış öbeklerden hangisi bir öge değil, ara sözdür?',
 [('I','“Elif” “aldı” eyleminin yapıcısıdır; özne bir ögedir.','bilgi'),
  ('II',None,None),
  ('III','“Bu yıl” ne zaman? sorusunun cevabıdır; zarf tümleci bir ögedir.','dikkat'),
  ('IV','“Ödül” neyi aldı? sorusunun cevabıdır; nesne bir ögedir.','bilgi'),
  ('V','“Aldı” yüklemdir; bir ögedir.','bilgi')],
 'B','Ara söz olan öbek.','Yükleme sorduğun sorulardan hangisine hiçbir cevap vermeyen öbek var?',[B_ARA],
 [AD('Ara sözü hatırla','Ara söz, cümlenin ögesi olmayan, virgülle ayrılıp yargı ya da açıklama katan sözdür.','öge değil'),
  AD('Öbekleri sına','I: özne · III: zarf tümleci · IV: nesne · V: yüklem. Hepsi yükleme bir soruya cevap verir.','I, III, IV, V: öge'),
  AD('Ara sözü seç','“Yanılmıyorsam” konuşanın yargısını bildirir; kaldırılsa cümlenin ögeleri değişmez, hiçbir soruya cevap olmaz.','II: ara söz')],
 'Yükleme hiçbir soruya cevap olmayan, çıkarınca cümlenin ögeleri değişmeyen söz ara sözdür.',kalip='öncüllü')

Qd('0033','K-DBOG-09','kolay','Hitabı (öge dışı) bulunan cümleyi belirler.',2,
 'Aşağıdaki cümlelerin hangisinde hitap (cümle dışı unsur) vardır?',
 'Çocuklar, yarın okula erken gelin.','A',
 [('Kerem derslerini bitirince, annesine telefon etti.','“Kerem” “telefon etti” yüklemine “kim?” sorusunun cevabı olan öznedir; hitap yoktur.','dikkat'),
  ('Yarın sabah kahvaltıdan sonra yola çıkacağız.','Cümlede hitap yoktur; tüm sözcükler ögelerdir.','bilgi'),
  ('Annem pazardan dönünce yemeği hazırladı.','Hitap yoktur; “annem” öznedir.','bilgi'),
  ('Kış gelince, kuşlar sıcak ülkelere göç eder.','Hitap yoktur; “kuşlar” öznedir.','bilgi')],
 'Hitabı olan cümle.','Yüklemin kişi ekine bak: seslenilen kişi özne olabilir mi?',[B_ARA],
 [AD('Hitabı hatırla','Seslenilen kişi öge değildir; yüklemin kişi ekiyle uyuşmayan ögedir.','hitap → cümle dışı'),
  AD('Şıkları sına','B, C, D, E’de özneler yüklemlerin kişi ekleriyle (3. kişi) uyuşuyor.','B, C, D, E: hitap yok'),
  AD('Hitabı seç','A’da yüklem “gelin” (siz) olduğundan “çocuklar” özne değil, seslenilen kişidir.','A: hitap')],
 'Seslenilen kişi yüklemle kişi bakımından uyuşmuyorsa özne değil, hitaptır.')

Qd('0034','K-DBOG-09','zor','Virgülle ayrılan sıralı öznelerle ara sözü ayırır.',4,
 'Aşağıdaki cümlelerin hangisinde virgüllerle ayrılan sözler ara söz değil, cümlenin ögesidir?',
 'Annem, babam ve ben akşam yemeğinde dedemlerde buluştuk.','C',
 [('Selin, bana kalırsa, bu yarışmayı kolayca kazandı.','“Bana kalırsa” yargı bildiren ara sözdür; öge değildir.','bilgi'),
  ('Dedem, nasıl desem, bu kitabı bana geçen yıl vermişti.','“Nasıl desem” cümleye anlam katan ara sözdür; öge değildir.','bilgi'),
  ('Müdürümüz, kusura bakmayın, konuşmasına biraz geç başladı.','“Kusura bakmayın” cümleye katılan ara sözdür; öge değildir.','bilgi'),
  ('Komşumuzun kızı, adını şimdi hatırlayamıyorum, geçen hafta üniversiteyi kazandı.','“Adını şimdi hatırlayamıyorum” ara sözdür; öge değildir.','bilgi')],
 'Virgülle ayrılan sözlerin öge olduğu cümle.','Virgülle ayrılan öbeğe yükleme göre soru sorulabiliyor mu?',[B_ARA,B_SIRA],
 [AD('Ayrımı hatırla','Ara söz yükleme hiçbir soruya cevap olmaz; sıralanan öznelerin her biri “kim?” sorusuna cevap verir.','ara söz: soruya cevap vermez'),
  AD('Virgüllü öbekleri sına','A: bana kalırsa · B: nasıl desem · D: kusura bakmayın · E: adını şimdi hatırlayamıyorum. Hiçbiri yükleme sorulan bir soruya cevap vermez.','A, B, D, E: ara söz'),
  AD('Ögeyi seç','C’de “annem”, “babam” ve “ben”, “kim buluştu?” sorusunun cevabıdır; virgülle ayrılsa da özne ögesidir.','C: öge')],
 'Virgül, ögeyi ara söz yapmaz; yükleme soru sorarak öge olup olmadığını denetle.')
bitir(Q)
