"""TYT Türkçe · Fiiller-Fiilimsiler-Ek Fiiller-Çatı genişletme: 26 soru (hafif mod). Metinler özgündür."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from hafif_db import *
AD=A
KY='ÖSYM TYT Türkçe 2018–2026 · Bilgi Sarmal Dil Bilgisi SB (ÖSYM Tipi) · TDK Yazım Kılavuzu'
def K(alt,fikir,tuzak,zor,kalip,adim,tip): return dict(alt=alt,fikir=fikir,tuzak=tuzak,zorluk=zor,kalip=kalip,adim=adim,tipId=tip,kaynak=KY)
KARTLAR={
 'K-DBFL-01':K('Kip ve Kişi','Yüklemin haber ya da dilek kipinde, hangi zamanda ve olumlu/olumsuz olduğunu ekinden çıkarmak.','-miş, -sa gibi ekleri tek tek tanımadan cümlenin anlamına bakmak.','orta','düz',3,'dfl-kip'),
 'K-DBFL-02':K('Birleşik Zamanlı Fiiller','Basit çekimi hikâye, rivayet ya da şart ek fiiliyle kurulan birleşik çekimden ayırmak.','Tek başına -miş ya da -sa ekini birleşik zaman saymak.','orta','düz',3,'dfl-birlesik'),
 'K-DBFL-03':K('Ek Fiil','Ek fiilin ad soylu sözcüğü yüklem yapma görevini, fiile gelen birleşik zaman görevinden ayırmak.','Fiil çekimindeki -dı, -miş eklerini ek fiil sanmak.','orta','öncüllü',3,'dfl-ekfiil'),
 'K-DBFL-04':K('Fiilimsiler','Fiilimsinin türünü (isim-fiil, sıfat-fiil, zarf-fiil) ekine ve cümledeki görevine göre belirlemek.','Aynı ekin farklı görevlerini karıştırmak; -ma olumsuzluk ekini isim-fiil sanmak.','orta','öncüllü',3,'dfl-fiilimsi'),
 'K-DBFL-05':K('Kalıcı Adlaşma','Fiilimsi gibi görünen ama sözlüğe ad olarak girmiş sözcükleri fiilimsiden ayırmak.','Her -ma, -mak, -ak sonlu sözcüğü fiilimsi saymak.','zor','öncüllü',4,'dfl-kalici'),
 'K-DBFL-06':K('Etken–Edilgen Çatı','Öznenin işi yapan mı, işten etkilenen mi olduğuna bakarak çatıyı belirlemek.','Kökü l/n ile biten fiili edilgen sanmak (doldu, güldü).','orta','öncüllü',3,'dfl-cati'),
 'K-DBFL-07':K('Geçişlilik ve Dönüşlü–İşteş Çatı','Nesne alıp almadığına göre geçişliliği, ek ve anlama göre dönüşlü ve işteş çatıyı ayırmak.','Kökte yer alan -ş ve -n sesini çatı eki sanmak.','orta','öncüllü',3,'dfl-gecis'),
 'K-DBFL-08':K('Fiilde Anlam (Birleşik Fiil)','Yeterlik, tezlik, sürerlik ve yaklaşma anlamı katan birleşik fiilleri ayırmak.','Yardımcı fiilin kendi anlamıyla anlam katan ekleri karıştırmak.','orta','öncüllü',3,'dfl-anlam'),
}
TIPLER={'dfl-kip':'Kip ve kişi','dfl-birlesik':'Birleşik zamanlı fiiller','dfl-ekfiil':'Ek fiil','dfl-fiilimsi':'Fiilimsiler','dfl-kalici':'Kalıcı adlaşma','dfl-cati':'Etken–edilgen çatı','dfl-gecis':'Geçişlilik, dönüşlü ve işteş çatı','dfl-anlam':'Fiilde anlam (yeterlik, tezlik, sürerlik, yaklaşma)'}
Q=kur('dfiil','Fiiller-Fiilimsiler-Ek Fiiller-Çatı','tr|Fiiller-Fiilimsiler-Ek Fiiller-Çatı',KARTLAR,TIPLER); Q.n=26

def S(no,kart,zor,kaz,adim,metin,dogru,yan,harf,istenen,ip,bilgi,adimlar,puf,kalip='düz'):
    """dogru: doğru şık metni; yan: 4×(metin,cel,tur); doğru şık verilen harfe yerleşir."""
    L='ABCDE'; yi=iter(yan); opts=[]
    for l in L:
        if l==harf: opts.append((dogru,D,'',''))
        else:
            m,c,t=next(yi); opts.append((m,Y,c,t))
    soru(Q,no,kart,zor,kaz,adim,metin,opts,harf,lambda e:e==D,istenen,ip,bilgi,adimlar,puf,kalip=kalip)
def SF(no,kart,zor,kaz,adim,metin,sik,harf,istenen,ip,bilgi,adimlar,puf,kalip='öncüllü'):
    """sik: sabit sırada 5×(metin,cel,tur); doğru şıkta cel=None."""
    opts=[(m,(D if c is None else Y),(c or ''),(t or '')) for m,c,t in sik]
    soru(Q,no,kart,zor,kaz,adim,metin,opts,harf,lambda e:e==D,istenen,ip,bilgi,adimlar,puf,kalip=kalip)

B_KIP=B('Kip ve kişi','haber kipleri: -dı, -mış, -yor, -acak, -ar/-ır, -maz · dilek kipleri: -sa (şart), -a (istek), -malı (gereklilik), emir (otur, gelsin) · okuyalım = oku- + -alım: istek kipi')
B_BIR=B('Birleşik zamanlı fiil','basit çekimli fiil + ek fiil (idi, imiş, ise): geliyordu (şimdiki zamanın hikâyesi), geliyormuş (şimdiki zamanın rivayeti), gelirse (geniş zamanın şartı). Tek başına -dı, -mış, -sa basit çekimdir: geldi, gelmiş, gelse')
B_EK=B('Ek fiil','iki görevi vardır: 1) ad soylu sözcüğü yüklem yapar (güzeldi = güzel + idi, karlıymış = karlı + imiş) · 2) fiil çekimini birleşik zamanlı yapar (geliyordu = geliyor + idi)')
B_FS=B('Fiilimsiler','isim-fiil: -mak, -ma, -ış (okumak, gülüş) · sıfat-fiil: -an, -dık, -acak, -mış, -ar, -maz (giren öğrenci) · zarf-fiil: -arak, -ınca, -ip, -ken, -madan, -ır … -maz (koşarak girdi). Fiilimsiler yüklem olmaz')
B_KA=B('Kalıcı adlaşma','fiilimsi gibi görünen bazı sözcükler sözlüğe ad olarak girmiştir; bunlar fiilimsi değil addır: akıntı, yazı, süpürge, yemek, açıklama · örnek: “Süpürge köşede duruyor.” (ad) / “Yaptığı yemeği beğendik.” (sıfat-fiil)')
B_ET=B('Etken ve edilgen çatı','etken: işi özne yapar (Ali kapıyı açtı) · edilgen: özne işi yapan değil, işten etkilenendir; -l, -n eki alır (Kapı açıldı) · kökü l/n ile biten fiil edilgen olmaz: gül-, bul- kök fiildir')
B_GE=B('Geçişlilik ve çatı','geçişli fiil nesne alır (kitap okur: belirtisiz nesne), geçişsiz fiil nesne almaz (atladı) · dönüşlü: iş öznenin kendisine döner, -n eki (yıkandı, tarandı) · işteş: iş birlikte ya da karşılıklı yapılır, -ş eki (görüştü) · koş-, çalış- kök fiildir')
B_AN=B('Fiilde anlam','yeterlik: -ebil (kaldırabilir) · tezlik: -iver (açıverdi) · sürerlik: -edur, -egel, -ekal (yazadurmak, gidegelmek, donakalmak) · yaklaşma: -eyaz (düşeyazdı)')

# 1
S('0001','K-DBFL-01','kolay','Dilek kipiyle çekimlenmiş yüklemi bulur.',2,
 'Aşağıdaki cümlelerin hangisinin yüklemi dilek kipiyle çekimlenmiştir?',
 'Bu akşam sinemaya gidelim.',
 [('Yarın sabah erkenden yola çıkacağız.','Çık-acağız: gelecek zaman, haber kipidir; dilek kipi değildir.','bilgi'),
  ('Çocuklar bahçede top oynuyor.','Oyna-yor: şimdiki zaman, haber kipidir.','bilgi'),
  ('Kardeşim dün akşam erken uyudu.','Uyu-du: di’li geçmiş zaman, haber kipidir.','dikkat'),
  ('Annem her sabah çay içer.','İç-er: geniş zaman, haber kipidir.','dikkat')],
 'A','Dilek kipli yüklem.','Kipin türünü ekten çıkar: -yor, -du, -er, -acak haber; -elim dilektir.',[B_KIP],
 [AD('Kipleri ayır','Haber kipleri iş ve oluşu bildirir. Dilek kipleri istek, emir, şart ya da gereklilik anlatır.','haber: -dı, -yor, -acak, -ar · dilek: -a, -sa, -malı, emir'),
  AD('Şıkları çözümle','Çıkacağız: gelecek zaman; oynuyor: şimdiki zaman; uyudu: di’li geçmiş; içer: geniş zaman.','B, C, D, E: haber kipi'),
  AD('Dilek kipini seç','Gidelim: git- + -elim. İstek kipinin 1. çoğul kişisidir; bir istek ve öneri bildirir.','A: istek kipi (dilek)')],
 'Yüklemi “haber mi, dilek mi?” diye sınarken -a, -sa, -malı ve emir biçimlerini dilek kipi say.')
# 2
S('0002','K-DBFL-01','orta','Numaralanmış fiiller arasında dilek kipini bulur.',3,
 'Kerem sabah pencereyi açtı (I). Dışarıda kar yağıyordu (II). Annesi içeriden seslendi (III). “Kalın bir mont giy (IV),” dedi. Kerem, “Okula varınca ısınırım (V),” diye karşılık verdi.\nBu parçada numaralanmış fiillerden hangisi dilek kipiyle çekimlenmiştir?',
 'IV',
 [('I','Aç-tı: di’li geçmiş zaman, haber kipidir.','bilgi'),('II','Yağ-ıyor-du: şimdiki zamanın hikâyesi, haber kipidir.','bilgi'),('III','Seslen-di: di’li geçmiş zaman, haber kipidir.','dikkat'),('V','Isın-ır-ım: geniş zaman, haber kipidir.','dikkat')],
 'D','Dilek kipiyle çekimli fiil.','Fiilin bir şeyi olmuş gibi mi anlattığına, yoksa bir emir ya da istek mi bildirdiğine bak.',[B_KIP],
 [AD('Ölçütü hatırla','Emir, istek, şart ve gereklilik dilek kipidir; geri kalanlar haber kipidir.','emir, istek, şart, gereklilik → dilek'),
  AD('Numaraları çözümle','I açtı, III seslendi: di’li geçmiş. II yağıyordu: şimdiki zamanın hikâyesi. V ısınırım: geniş zaman.','I, II, III, V: haber'),
  AD('Dilek kipini seç','IV’teki “giy” annenin verdiği bir emirdir; emir kipi dilek kipidir.','IV: emir (dilek)')],
 'Anlamca emir ya da istek bildiren fiili görünce haber kipi aramayı bırak: dilek kipidir.',kalip='öncüllü')
# 3
S('0003','K-DBFL-01','orta','Olumsuz gelecek zamanlı yüklemi belirler.',3,
 'Aşağıdaki cümlelerin hangisinin yüklemi hem olumsuz hem de gelecek zaman kipindedir?',
 'Yarın toplantıya katılmayacağım.',
 [('Bu sorunu bir türlü çözemedik.','Çöz-e-me-di-k: olumsuz ama di’li geçmiş zamandadır.','bilgi'),('Sınav sonuçları akşama açıklanacak.','Açıkla-n-acak: gelecek zaman ama olumludur.','bilgi'),('Kimseye bir şey söylemem.','Söyle-me-m: olumsuz ama geniş zamandadır.','dikkat'),('Babam akşam eve gelmedi.','Gel-me-di: olumsuz ama di’li geçmiş zamandadır.','dikkat')],
 'B','Olumsuz gelecek zamanlı yüklem.','Hem olumsuzluk ekini (-ma/-me) hem de gelecek zaman ekini (-acak/-ecek) ara.',[B_KIP],
 [AD('İki ölçütü yaz','Yüklemde olumsuzluk eki -ma/-me, gelecek zaman eki -acak/-ecek olmalı.','-ma/-me + -acak/-ecek'),
  AD('Şıkları sına','Çözemedik ve gelmedi: -di’li geçmiş. Açıklanacak: olumlu gelecek. Söylemem: olumsuz geniş zaman.','A, C, D, E: tek ölçüt sağlıyor'),
  AD('İkisini sağlayanı seç','Katıl-ma-yacak-ım: olumsuzluk eki ve gelecek zaman eki birlikte var.','B: doğru')],
 'Kip sorularında olumsuzluk eki ile zaman ekini ayrı ayrı bulup yan yana yaz.')
# 4
S('0004','K-DBFL-02','kolay','Birleşik zamanlı fiili bulur.',2,
 'Aşağıdaki cümlelerin hangisinin yüklemi birleşik zamanlı bir fiildir?',
 'Çocuklar parkta oynuyordu.',
 [('Annem kapıyı yavaşça açtı.','Aç-tı: basit çekimdir, ek fiil almamıştır.','bilgi'),('Yarın erken kalkacağız.','Kalk-acağız: gelecek zamanın basit çekimidir.','bilgi'),('Bu kitabı sen okudun.','Oku-du-n: di’li geçmiş zamanın basit çekimidir.','dikkat'),('Annem sofrayı hazırlıyor.','Hazırla-yor: şimdiki zamanın basit çekimidir.','dikkat')],
 'C','Birleşik zamanlı yüklem.','Fiilin kip ekinden sonra bir ek fiil (idi, imiş, ise) var mı?',[B_BIR],
 [AD('Tanımı hatırla','Birleşik zamanlı fiil, basit çekimli fiile ek fiilin gelmesiyle kurulur.','fiil + kip + ek fiil'),
  AD('Şıkları çöz','Açtı, kalkacağız, okudun, hazırlıyor: tek kip eki var; ek fiil yok.','A, B, D, E: basit çekim'),
  AD('Birleşiği seç','Oyna-yor-du: şimdiki zamanın hikâyesi (yor + idi).','C: birleşik')],
 'Yüklemde iki kip eki yan yana görüyorsan (-yor-du, -miş-ti, -acak-tı) birleşik zamanlıdır.')
# 5
S('0005','K-DBFL-02','orta','Rivayet birleşik zamanı ayırt eder.',3,
 'Aşağıdaki cümlelerin hangisinin yüklemi, ek fiilin rivayeti (imiş) ile kurulmuş birleşik zamanlı bir fiildir?',
 'Dün burada yağmur yağıyormuş.',
 [('Sınava çok iyi hazırlanmıştı.','Hazırlan-mış-tı: ek fiilin hikâyesiyle kurulmuş birleşik zamandır; rivayet değil hikâyedir.','bilgi'),('Çocuk akşam erkenden uyumuş.','Uyu-muş: -muş burada kip ekidir; ek fiil (imiş) yoktur, basit çekimdir.','bilgi'),('Yarın erken kalkarsa yetişir.','Yüklem “yetişir”: geniş zamanın basit çekimidir; “kalkarsa” yan cümle fiilidir, rivayet yoktur.','dikkat'),('Bu işi kısa sürede başaracaktı.','Başar-acak-tı: gelecek zamanın hikâyesidir; rivayet değildir.','dikkat')],
 'C','Rivayet birleşik zamanlı yüklem.','Ek fiilin hangi biçimi (idi, imiş, ise) gelmiş? “imiş” aranıyor.',[B_BIR],
 [AD('Biçimleri ayır','Ek fiil üç biçimde gelir: idi (hikâye), imiş (rivayet), ise (şart).','idi · imiş · ise'),
  AD('Şıkları çöz','hazırlanmıştı: hikâye. uyumuş: basit çekim (-miş kip eki). yetişir: basit çekim. başaracaktı: hikâye.','A, B, D, E: rivayet değil'),
  AD('Rivayeti seç','Yağ-ıyor-muş: şimdiki zaman + imiş, yani rivayet birleşik zamanıdır.','C: doğru')],
 '-miş eki fiil kökünden hemen sonra geliyorsa kip eki; başka bir kipten sonra geliyorsa ek fiildir.')
# 6
S('0006','K-DBFL-02','zor','Parçadaki fiiller arasında rivayet birleşik zamanı bulur.',4,
 'Köye vardığımızda (I) akşam olmuştu (II). Hava soğuk olsaydı (III), dedem bizi bahçede bekleyemezdi. Ama o, kapının önünde bekliyormuş (IV). Anneannem de sofrayı çoktan kurmuştu (V).\nBu parçada numaralanmış sözcüklerden hangisi, ek fiilin rivayeti ile kurulmuş birleşik zamanlı bir fiildir?',
 'IV',
 [('I','Var-dığ-ımız-da: zarf-fiil ekli sözcüktür; yüklem değildir.','bilgi'),('II','Ol-muş-tu: ek fiilin hikâyesidir, rivayet değildir.','bilgi'),('III','Ol-sa-ydı: şartın hikâyesidir, rivayet değildir.','dikkat'),('V','Kur-muş-tu: ek fiilin hikâyesidir, rivayet değildir.','dikkat')],
 'D','Rivayet birleşik zamanlı fiil.','Her numarada ek fiilin biçimine bak: idi, imiş, ise.',[B_BIR],
 [AD('Ek fiil biçimlerini yaz','Rivayet için ek fiil “imiş” olmalı.','imiş → -mış, -miş'),
  AD('Numaraları çöz','I vardığımızda: zarf-fiil. II olmuştu, V kurmuştu: hikâye. III olsaydı: şartın hikâyesi.','I, II, III, V: rivayet değil'),
  AD('Rivayeti seç','Bekli-yor-muş: şimdiki zaman + imiş.','IV: şimdiki zamanın rivayeti')],
 'Birleşik zamanlı fiilde ikinci ek “-di, -miş, -se” ise hikâye, rivayet, şart ayrımını bu ek verir.',kalip='öncüllü')
# 7
S('0007','K-DBFL-03','kolay','Ek fiilin ad soylu sözcüğü yüklem yaptığı cümleyi bulur.',2,
 'Aşağıdaki cümlelerin hangisinde ek fiil, ad soylu bir sözcüğü yüklem yapmıştır?',
 'Bu şehrin havası oldukça temizdir.',
 [('Çocuklar bahçede oynuyordu.','Oyna-yor-du: ek fiil fiil çekimini birleşik zamanlı yapmıştır.','bilgi'),('Sabah erkenden yola çıkmıştık.','Çık-mış-tı-k: ek fiil fiil çekimine eklenmiştir.','bilgi'),('Misafirler akşam gelirse sevinirim.','Gelir-se: ek fiil fiil çekimine eklenmiştir.','dikkat'),('Annem pazara gidiyormuş.','Gid-iyor-muş: ek fiil fiil çekimine eklenmiştir.','dikkat')],
 'E','Ad soylu yüklem yapan ek fiil.','Yüklemin kökü fiil mi, ad soylu mu? Ek fiil sorusunda isim kökü ara.',[B_EK],
 [AD('İki görevi ayır','Ek fiil ya ad soylu sözcüğe yüklem yapar ya da fiil çekimini birleşik yapar.','ad + ek fiil · fiil + ek fiil'),
  AD('Köklere bak','oynuyordu: oyna-; çıkmıştık: çık-; gelirse: gel-; gidiyormuş: git-. Hepsi fiil kökü.','A, B, C, D: fiil + ek fiil'),
  AD('Ad soylu yükleme ulaş','Temiz-dir: temiz (sıfat) + ek fiil (-dir).','Doğru şık')],
 'Yüklemin kökü fiil değil ad ya da sıfatsa, yüklemi yapan ek fiildir.')
# 8
SF('0008','K-DBFL-03','orta','Ek fiilin ad soylu sözcüğü yüklem yaptığı cümleleri seçer.',3,
 'I. Sabah pencereden bakınca dağlar karlıymış.\nII. Çocuklar uzun süre parkta oynuyormuş.\nIII. Bu çorba bugün çok tuzluydu.\nYukarıdaki cümlelerin hangilerinde ek fiil, ad soylu bir sözcüğü yüklem yapmıştır?',
 [('Yalnız I','III’te de ad soylu sözcüğü yüklem yapan ek fiil var; yalnız I demek eksik kalır.','dikkat'),('Yalnız II','Oyna-yor-muş: ek fiil fiil çekimine eklenmiştir; ad soylu sözcük yüklem değildir.','bilgi'),('I ve II','II’de yüklem fiil kökünden oluşur; ek fiil birleşik zaman kurmuştur.','bilgi'),('I ve III',None,None),('II ve III','II’de ek fiil fiil çekimine gelmiştir; ad soylu sözcüğü yüklem yapmamıştır.','dikkat')],
 'D','Ek fiille ad soylu yüklem.','Yüklemin kökünü bul: karlı, oyna-, tuzlu.',[B_EK],
 [AD('Ölçütü hatırla','Ek fiil ad soylu sözcüğün yanındaysa onu yüklem yapar; fiilin yanındaysa birleşik zaman yapar.','ad + ek fiil · fiil + ek fiil'),
  AD('Cümleleri çöz','I karlı + imiş. II oyna-yor + muş (fiil). III tuzlu + idi.','I ✓ · II ✗ · III ✓'),
  AD('Doğru şıkkı seç','Ad soylu yüklem I ve III’tedir.','D: I ve III')],
 'Yüklemin ilk parçası sıfat ya da isimse ek fiil ad soylu sözcüğü yüklem yapıyordur.',kalip='öncüllü')
# 9
S('0009','K-DBFL-03','orta','Yüklemde ek fiil bulunmayan cümleyi bulur.',3,
 'Gölün çevresi sessizdi (I). Kıyıda birkaç balıkçı oturuyordu (II). Uzaktaki dağlar henüz karlıymış (III). Rüzgâr hafif ve serindi (IV). Su, sabahın ilk ışıklarıyla birlikte kıpırdanmaya başladı (V).\nBu parçada numaralanmış yüklemlerden hangisinde ek fiil yoktur?',
 'V',
 [('I','Sessiz + idi: ek fiil ad soylu sözcüğü yüklem yapmıştır.','bilgi'),('II','Otur-uyor + idi: ek fiil birleşik zaman kurmuştur.','bilgi'),('III','Karlı + imiş: ek fiil ad soylu sözcüğü yüklem yapmıştır.','dikkat'),('IV','Serin + idi: ek fiil ad soylu sözcüğü yüklem yapmıştır.','dikkat')],
 'E','Ek fiili bulunmayan yüklem.','Basit çekimli bir fiil kipten başka ek almaz; -di burada kip ekidir.',[B_EK,B_BIR],
 [AD('Ek fiili hatırla','Ek fiil ya ad soylu sözcüğü yüklem yapar ya da fiilden sonra birleşik zaman kurar.','ad + ek fiil · fiil + kip + ek fiil'),
  AD('Numaraları çöz','I sessizdi, III karlıymış, IV serindi: ad + ek fiil. II oturuyordu: şimdiki zaman + idi.','I, II, III, IV: ek fiil var'),
  AD('Ek fiilsizi seç','Başla-dı: -dı fiilin kip ekidir (di’li geçmiş); ek fiil yoktur.','V: ek fiil yok')],
 'Fiile doğrudan -dı/-mış geliyorsa bunlar kip ekidir; ek fiil olmaları için başka bir kipten sonra gelmeleri gerekir.',kalip='öncüllü')
# 10
S('0010','K-DBFL-04','kolay','Cümlede zarf-fiil bulunduğunu belirler.',2,
 'Aşağıdaki cümlelerin hangisinde zarf-fiil vardır?',
 'Çocuk yavaşça kapıyı açarak içeri girdi.',
 [('Yüzmeyi küçük yaşta babasından öğrendi.','Yüz-me-yi: -ma eki isim-fiil yapar; zarf-fiil yoktur.','bilgi'),('Kapıdan giren çocuk herkese selam verdi.','Gir-en: -an eki sıfat-fiil yapar.','bilgi'),('Okunacak kitapları dikkatle masaya koydu.','Oku-n-acak: -acak sıfat-fiil yapar.','dikkat'),('Bu dar yoldan yaya geçmek güvenli değil.','Geç-mek: -mak isim-fiil yapar.','dikkat')],
 'C','Zarf-fiil içeren cümle.','Zarf-fiil, fiili niteler; -arak, -ınca, -ip ekleriyle kurulur.',[B_FS],
 [AD('Ekleri hatırla','Zarf-fiil ekleri: -arak, -ınca, -ip, -ken, -madan.','-arak, -ınca, -ip'),
  AD('Şıkları çöz','yüzmeyi, geçmek: isim-fiil. giren, okunacak: sıfat-fiil.','A, B, D, E: zarf-fiil yok'),
  AD('Zarf-fiili seç','Aç-arak: -arak eki; “girdi” fiilinin nasıl yapıldığını bildirmektedir.','C: zarf-fiil')],
 'Fiilimsi hangi sözcüğü nitelediğine bakılarak ayrılır: ismi niteliyorsa sıfat-fiil, fiili niteliyorsa zarf-fiil.')
# 11
S('0011','K-DBFL-04','orta','Sıfat-fiil içeren cümleyi bulur.',3,
 'Aşağıdaki cümlelerin hangisinde sıfat-fiil vardır?',
 'Dün aldığım kitabı bitirdim.',
 [('Konuyu dikkatle okuyunca anladım.','Oku-yunca: zarf-fiildir; sıfat-fiil yoktur.','bilgi'),('Koşmak sağlık için yararlıdır.','Koş-mak: isim-fiildir; sıfat-fiil yoktur.','bilgi'),('Kapıyı açar açmaz içeri girdi.','Aç-ar aç-maz: zarf-fiildir.','dikkat'),('Çocuklar okula yürüyerek gitti.','Yürü-yerek: zarf-fiildir.','dikkat')],
 'A','Sıfat-fiil içeren cümle.','Fiilimsi bir ismi mi niteliyor?',[B_FS],
 [AD('Sıfat-fiili tanı','Sıfat-fiil bir ismi niteler; -an, -dık, -acak, -mış ekleri alır.','-an, -dık, -acak, -mış'),
  AD('Şıkları çöz','okuyunca, açar açmaz, yürüyerek: zarf-fiil. Koşmak: isim-fiil.','B, C, D, E: sıfat-fiil yok'),
  AD('Sıfat-fiili bul','Al-dığ-ım: “kitabı” ismini niteliyor; -dık eki sıfat-fiil yapmış.','A: sıfat-fiil')],
 'Fiilimsinin hemen ardından bir isim geliyor ve onu niteliyorsa sıfat-fiildir.')
# 12
S('0012','K-DBFL-04','orta','Numaralı fiilimsiler arasında isim-fiili ayırır.',3,
 'Sahile inen (I) yolda yürümek (II) insana iyi gelir. Güneş batarken (III) denizin rengi değişir. Bu manzarayı gören (IV) herkes burayı sever. Kimileri de tatilini burada geçirerek (V) dinlenir.\nBu parçada numaralanmış fiilimsilerden hangisi isim-fiildir?',
 'II',
 [('I','İn-en: “yol” ismini niteleyen sıfat-fiildir.','bilgi'),('III','Bat-arken: zaman bildiren zarf-fiildir.','bilgi'),('IV','Gör-en: “herkes” zamirini niteleyen sıfat-fiildir.','dikkat'),('V','Geçir-erek: “dinlenir” fiilini niteleyen zarf-fiildir.','dikkat')],
 'B','İsim-fiil olan fiilimsi.','İsim-fiil, cümlede isim gibi kullanılır; -mak, -ma, -ış ekleri alır.',[B_FS],
 [AD('Ölçütü hatırla','İsim-fiil: -mak/-ma/-ış eki; cümlede isim görevindedir.','-mak, -ma, -ış'),
  AD('Numaraları çöz','I inen, IV gören: sıfat-fiil. III batarken, V geçirerek: zarf-fiil.','I, III, IV, V: isim-fiil değil'),
  AD('İsim-fiili seç','Yürü-mek: cümlede özne görevinde isim gibi kullanılmış.','II: isim-fiil')],
 'Fiilimsi cümlede özne, nesne gibi isim görevi yapıyorsa isim-fiildir.',kalip='öncüllü')
# 13
S('0013','K-DBFL-04','zor','Cümlede hem sıfat-fiil hem zarf-fiil bulunanı ayırır.',4,
 'Aşağıdaki cümlelerin hangisinde hem sıfat-fiil hem de zarf-fiil vardır?',
 'Ağaca tırmanan çocuk yere düşünce ağladı.',
 [('Sabah erkenden kalkarak yürüyüşe çıkmak güzeldir.','Kalk-arak zarf-fiil, çık-mak isim-fiildir; sıfat-fiil yoktur.','bilgi'),('Gülmek ve oynamak çocukların hakkıdır.','Gül-mek ve oyna-mak: iki isim-fiildir; sıfat-fiil de zarf-fiil de yoktur.','bilgi'),('Bahçeye giren kedinin yediği balık eskiydi.','Gir-en ve ye-diği: iki sıfat-fiildir; zarf-fiil yoktur.','dikkat'),('Eve gelip yemek yiyerek dinlendi.','Gel-ip ve ye-yerek: iki zarf-fiildir; sıfat-fiil yoktur.','dikkat')],
 'A','Hem sıfat-fiil hem zarf-fiil içeren cümle.','Her cümledeki fiilimsileri bulup türlerini yan yana yaz.',[B_FS],
 [AD('Fiilimsileri türleriyle yaz','Her şıkta fiilimsi türlerini ayrı ayrı belirle.','sıfat-fiil: ismi niteler · zarf-fiil: fiili niteler'),
  AD('Şıkları çöz','B: zarf + isim. C: isim + isim. D: sıfat + sıfat. E: zarf + zarf. ("yemek" burada kalıcı addır.)','B, C, D, E: ikisi birden yok'),
  AD('İkisini içereni seç','A: tırman-an (çocuğu niteler: sıfat-fiil) ve düş-ünce (ağladı: zarf-fiil).','A: doğru')],
 'Çift fiilimsili cümlede her fiilimsinin neyi nitelediğini ayrı ayrı yaz; sonra ölçütle karşılaştır.')
# 14
S('0014','K-DBFL-04','orta','“-ma” ekinin olumsuzluk görevini isim-fiil görevinden ayırır.',4,
 'Sabah erkenden uyanmayı (I) kendime alışkanlık edindim. Havanın soğuk olması (II) beni vazgeçirmedi. Arkadaşlarım gelmedi (III) diye yürüyüşü bırakmam. Yürürken düşünmeyi (IV) severim; yoldaşımla ise yürüyüşten sonra konuşurum (V).\nBu parçada numaralanmış sözcüklerden hangisinde “-ma/-me” eki olumsuzluk bildirmektedir?',
 'III',
 [('I','Uyan-ma-yı: -ma isim-fiil yapar; olumsuzluk eki değildir.','bilgi'),('II','Ol-ma-sı: -ma isim-fiil yapar; olumsuzluk eki değildir.','bilgi'),('IV','Düşün-me-yi: -me isim-fiil yapar.','dikkat'),('V','Konuş-ur-um: geniş zaman eki var; -ma/-me eki yoktur.','dikkat')],
 'C','“-ma/-me” eki olumsuzluk bildiren sözcük.','Olumsuzluk eki -ma/-me, kipten önce gelir; isim-fiil eki sözcüğü ad yapar.',[B_FS],
 [AD('Aynı eki ayır','-ma/-me hem olumsuzluk hem isim-fiil eki olabilir. Olumsuzluk eki fiili olumsuz yapar; isim-fiil eki fiili ada çevirir.','gel-me-di (olumsuz) · gel-me-yi (isim-fiil)'),
  AD('Numaraları çöz','I uyanmayı, II olması, IV düşünmeyi: isim-fiildir. V konuşurum: -ma/-me eki yok.','I, II, IV: isim-fiil · V: olumsuzluk eki yok'),
  AD('Olumsuzluğu bul','Gel-me-di: -me olumsuzluk eki, -di kip eki; fiil olumsuz ve yüklemdir.','III: olumsuzluk')],
 '-ma/-me’den sonra kip ekleri (-dı, -yor, -ecek) geliyorsa olumsuzluk; ad çekim ekleri (-yı, -sı) geliyorsa isim-fiildir.',kalip='öncüllü')
# 15
S('0015','K-DBFL-05','orta','Kalıcı adlaşmış sözcüğü fiilimsiden ayırır.',3,
 'Aşağıdaki cümlelerin hangisinde tırnak içindeki sözcük fiilimsi değil, kalıcı olarak ad olmuş bir sözcüktür?',
 'Tatlı olarak çilekli “dondurma” yedik.',
 [('Sabahları “koşmak” bana çok iyi geliyor.','Koş-mak: -mak eki isim-fiil yapmıştır; fiilimsidir.','bilgi'),('Kapıdan “giren” kişi bize baktı.','Gir-en: sıfat-fiildir; ismi niteliyor.','bilgi'),('Eve “gelince” seni arayacağım.','Gel-ince: zarf-fiildir.','dikkat'),('Yarın “okuyacağım” kitabı seçtim.','Oku-yacağ-ım: sıfat-fiildir; “kitabı” niteliyor.','dikkat')],
 'B','Kalıcı adlaşmış sözcük.','Sözlükte ad olarak yer alan, fiil anlamı taşımayan sözcüğü ara.',[B_KA],
 [AD('Tuzağı hatırla','Bazı -ma, -mak sonlu sözcükler ad olmuştur; bunlar fiilimsi sayılmaz.','akıntı, yazı, süpürge'),
  AD('Şıkları çöz','koşmak: isim-fiil; giren, okuyacağım: sıfat-fiil; gelince: zarf-fiil.','A, C, D, E: fiilimsi'),
  AD('Adlaşmışı seç','“Dondurma” burada bir yiyecek adıdır; “dondurmak” eylemi yapılmıyor.','B: ad')],
 'Sözcük bir eylem değil, bir nesne ya da yiyecek adı bildiriyorsa fiilimsi değildir.')
# 16
S('0016','K-DBFL-05','orta','Parçada fiilimsi olmayan sözcüğü bulur.',4,
 'Pazar günü ailece kıra gittik. Kırda yürümek (I) hepimize iyi geldi. Babam ağacın gölgesinde oturup (II) çay içti. Çocuklar da gülen (III) yüzlerle koşuşup (IV) durdu. Annemin yaptığı dolma (V) çok lezzetliydi.\nBu parçada numaralanmış sözcüklerden hangisi fiilimsi değildir?',
 'V',
 [('I','Yürü-mek: isim-fiildir.','bilgi'),('II','Otur-up: zarf-fiildir.','bilgi'),('III','Gül-en: “yüzlerle” sözcüğünü niteleyen sıfat-fiildir.','dikkat'),('IV','Koşuş-up: zarf-fiildir.','dikkat')],
 'E','Fiilimsi olmayan sözcük.','Yemek adı bildiren sözcüğün fiil anlamı kalmış mı?',[B_KA,B_FS],
 [AD('Tuzağı hatırla','Süpürge gibi kalıcı adlaşmış sözcükler fiilimsi sayılmaz.','akıntı, süpürge → ad'),
  AD('Numaraları çöz','I yürümek: isim-fiil. II oturup, IV koşuşup: zarf-fiil. III gülen: sıfat-fiil.','I, II, III, IV: fiilimsi'),
  AD('Fiilimsi olmayanı seç','V’teki “dolma” bir yemek adıdır; fiil anlamı kalmamıştır.','V: kalıcı ad')],
 'Sözlüğe ad olarak girmiş, nesne ya da yiyecek bildiren -ma/-mak sonlu sözcüklere fiilimsi deme.',kalip='öncüllü')
# 17
S('0017','K-DBFL-05','zor','Hem fiilimsi hem kalıcı adlaşmış sözcük içeren cümleyi bulur.',4,
 'Aşağıdaki cümlelerin hangisinde hem fiilimsi hem de kalıcı olarak ad olmuş bir sözcük bulunur?',
 'Çakmağını değiştirmek istedi.',
 [('Çocuklar gülerek sınıfa girdi.','Gül-erek zarf-fiildir; kalıcı ad yoktur.','bilgi'),('Uzaktan dönen tekerleğin sesini duydu.','Dön-en sıfat-fiildir; kalıcı adlaşmış sözcük yoktur.','bilgi'),('Misafirler gelince sofrayı hazırladık.','Gel-ince zarf-fiildir; kalıcı ad yoktur.','dikkat'),('Yağmur şiddetle başlayınca eve koştu.','Başla-yınca zarf-fiildir; kalıcı ad yoktur.','dikkat')],
 'C','Fiilimsi ve kalıcı ad içeren cümle.','İki şeyi ayrı ayrı ara: fiilimsi ve eylem anlamı kalmamış ad.',[B_KA,B_FS],
 [AD('İki ölçütü yaz','Cümlede hem fiilimsi hem de eylem anlamı kalmamış bir ad bulunmalı.','fiilimsi + kalıcı ad'),
  AD('Şıkları çöz','A, B, D, E yalnız fiilimsi içeriyor: gülerek; dönen; gelince; başlayınca. Hiçbirinde kalıcı ad yok.','A, B, D, E: yalnız fiilimsi'),
  AD('İkisini içereni seç','Çakmak: kalıcı ad (bir araç). Değiştirmek: isim-fiil (istedi’nin nesnesi).','C: ikisi de var')],
 'Kalıcı adı ve fiilimsiyi ayrı ayrı işaretle; sonra hangi şıkta ikisinin birlikte olduğuna bak.')
# 18
S('0018','K-DBFL-06','kolay','Edilgen çatılı fiili bulur.',2,
 'Aşağıdaki cümlelerin hangisinde fiil edilgen çatılıdır?',
 'Yeni köprü gelecek ay açılacak.',
 [('Çocuk akşama kadar bahçede koştu.','Koş-tu: kök fiildir, çatı eki yoktur; etken çatıdır.','bilgi'),('Annem bugün akşam yemeği pişirdi.','Pişir-di: özne işi kendisi yapıyor; etken çatıdır.','bilgi'),('Kardeşim odanın penceresini kapattı.','Kapat-tı: özne işi kendisi yapıyor; etken çatıdır.','dikkat'),('Misafirler yarın akşam gelecek.','Gel-ecek: özne işi kendisi yapıyor; etken çatıdır.','dikkat')],
 'D','Edilgen çatılı yüklem.','Özne işi yapan mı, işten etkilenen mi?',[B_ET],
 [AD('Çatıyı hatırla','Edilgende özne işi yapmaz, işten etkilenir; fiil -l/-n eki alır.','Köprü açıldı'),
  AD('Şıkları çöz','Koştu, pişirdi, kapattı, gelecek: iş özne tarafından yapılıyor.','A, B, C, E: etken'),
  AD('Edilgeni seç','Aç-ıl-acak: işi yapan belli değil; köprü işten etkilenen.','D: edilgen')],
 'İşi kimin yaptığı belli değilse ve özne işten etkileniyorsa fiil edilgendir.')
# 19
S('0019','K-DBFL-06','orta','Etken cümlenin edilgen biçimini belirler.',3,
 '“Komşumuz bahçedeki ağacı kesti.” cümlesinin edilgen çatılı biçimi aşağıdakilerin hangisidir?',
 'Bahçedeki ağaç komşumuz tarafından kesildi.',
 [('Komşumuz bahçedeki ağacı çocuklara kestirdi.','Kes-tir-di: ettirgen çatıdır; özne işi başkasına yaptırıyor.','bilgi'),('Komşumuz bahçedeki ağacı sabah kesecek.','Kes-ecek: etken çatıdır; özne işi kendisi yapıyor.','bilgi'),('Bahçedeki ağacı komşumuz akşam kesmişti.','Kes-miş-ti: etken çatıdır; nesne yine “ağacı”.','dikkat'),('Komşumuz bahçedeki ağaçla gün boyu uğraştı.','Uğraş-tı: etken çatıdır; anlam da değişmiştir.','dikkat')],
 'E','Edilgen çatılı karşılık.','Edilgende nesne özneye dönüşür, fiil -l/-n eki alır.',[B_ET],
 [AD('Dönüşümü hatırla','Etken cümledeki nesne edilgende özne olur; fiil edilgenleşir.','nesne → özne · kes → kes-il'),
  AD('Şıkları çöz','Kestirdi: ettirgen. Kesecek, kesmişti, uğraştı: özne hâlâ işi yapan.','A, B, C, D: etken ya da ettirgen'),
  AD('Edilgeni seç','Kes-il-di: “ağaç” özne oldu; yapan kişi “tarafından” ile belirtildi.','E: edilgen')],
 'Etkenden edilgene geçerken nesne özne olur, özne “tarafından” ile bildirilebilir.')
# 20
S('0020','K-DBFL-06','orta','Kökü l ile biten etken fiili edilgenden ayırır.',4,
 'Okulumuzun bahçesine yeni bir sahne kuruldu (I). Gösteri saati yaklaşınca salon doldu (II). Konuşmalar dikkatle dinlendi (III). Sahne arkasında sürpriz bir ödül dağıtıldı (IV). Gösteri sonunda herkes alkışlandı (V).\nBu parçada numaralanmış fiillerden hangisi etken çatılıdır?',
 'II',
 [('I','Kur-ul-du: -ul edilgen ekidir.','bilgi'),('III','Dinle-n-di: -n edilgen ekidir.','bilgi'),('IV','Dağıt-ıl-dı: -ıl edilgen ekidir.','dikkat'),('V','Alkışla-n-dı: -n edilgen ekidir.','dikkat')],
 'B','Etken çatılı fiil.','Kökü l ya da n ile bitiyor diye çatı eki sanma; kökü tek başına anlamlı mı diye bak.',[B_ET],
 [AD('Tuzağı hatırla','Gül-, bul- gibi kökü l ile biten fiillerde -l çatı eki değil kökün parçasıdır.','gül- kök · kur-ul- edilgen'),
  AD('Numaraları çöz','kuruldu, dinlendi, dağıtıldı, alkışlandı: kök + edilgen eki.','I, III, IV, V: edilgen'),
  AD('Etkeni seç','Dol-du: kök fiil + di’li geçmiş; çatı eki yok, salon işi kendisi yapıyor.','II: etken')],
 'Fiilden çatı ekini atınca kalan parça anlamlı bir fiil değilse -l/-n kökün parçasıdır.',kalip='öncüllü')
# 21
SF('0021','K-DBFL-07','orta','Geçişli fiilleri nesne almasına göre belirler.',3,
 'I. Küçük kedi sessizce pencereden atladı.\nII. Annem her akşam sofra kurar.\nIII. Öğretmen tahtaya bir şey yazdı.\nYukarıdaki cümlelerin hangilerinde yüklem geçişli bir fiildir?',
 [('Yalnız I','Atla-dı: nesne almaz; geçişsiz fiildir.','bilgi'),('Yalnız II','III’te de belirtisiz nesne “bir şey” vardır; yalnız II demek eksik kalır.','dikkat'),('I ve II','I’deki “atladı” geçişsiz fiildir.','bilgi'),('I ve III','I’deki “atladı” geçişsiz fiildir.','dikkat'),('II ve III',None,None)],
 'E','Geçişli yüklemli cümleler.','Yükleme “neyi?” ya da “kimi?” diye sor; belirtisiz nesne de nesnedir.',[B_GE],
 [AD('Ölçütü hatırla','Geçişli fiil nesne alır: “neyi, kimi?” sorusuna yanıt verir; nesne belirtisiz olabilir.','neyi? → nesne → geçişli'),
  AD('Cümleleri çöz','I: “neyi” sorusunun yanıtı yok (pencereden zarf tümleci). II: sofra kurar → neyi? sofra. III: neyi? bir şey.','I ✗ · II ✓ · III ✓'),
  AD('Doğru şıkkı seç','Geçişli yüklemler II ve III’tedir.','E: II ve III')],
 'Belirtisiz nesne de nesnedir: “gazete okur”, “sofra kurar” geçişlidir.',kalip='öncüllü')
# 22
S('0022','K-DBFL-07','orta','Dönüşlü çatılı fiili belirler.',3,
 'Aşağıdaki cümlelerin hangisinde fiil dönüşlü çatılıdır?',
 'Kerem sabah aceleyle giyindi.',
 [('Köprü iki yılda yapıldı.','Yap-ıl-dı: edilgen çatıdır; işi yapan belli değil.','bilgi'),('Öğretmen öğrencilere ödev yazdırdı.','Yaz-dır-dı: ettirgen çatıdır; iş başkasına yaptırılıyor.','bilgi'),('Konuklar yarın karşılanacak.','Karşıla-n-acak: edilgen çatıdır; özne işten etkileniyor.','dikkat'),('Misafirler salonda oturdu.','Otur-du: kök fiil; etken çatıdır.','dikkat')],
 'A','Dönüşlü çatılı fiil.','Dönüşlü çatıda iş öznenin kendi üzerinde gerçekleşir; -n eki alır.',[B_GE,B_ET],
 [AD('Dönüşlü çatıyı hatırla','İşi özne yapar ve işten yine özne etkilenir; fiil -n alır.','yıka-n-: kendini yıkamak'),
  AD('Şıkları çöz','B yapıldı ve D karşılanacak: edilgen; C yazdırdı: ettirgen; E oturdu: etken.','B, C, D, E: dönüşlü değil'),
  AD('Dönüşlüyü seç','Giy-in-di: Kerem giyen de giyilen de kendisidir.','A: dönüşlü')],
 'Hem işi yapan hem işten etkilenen özne ise ve fiilde -n varsa dönüşlüdür (yıkandı, tarandı).')
# 23
S('0023','K-DBFL-07','orta','İşteş çatılı fiili -ş sesli kök fiillerden ayırır.',4,
 'Aşağıdaki cümlelerin hangisinde fiil işteş çatılıdır?',
 'Komşular sabah sokakta selamlaştı.',
 [('İki arkadaş uzun süre sohbet ettiler.','Et-ti-ler: yardımcı fiilli birleşik fiil; çatı eki yoktur, etken çatıdır.','bilgi'),('Hasta çocuğu hemen hastaneye götürdük.','Götür-dü-k: kök fiil; çatı eki yok, etken.','dikkat'),('Kardeşim yarın bizimle gelecek.','Gel-ecek: kök fiil; çatı eki yok, etken.','dikkat'),('Çocuklar bahçede top oynadı.','Oyna-dı: kök fiil; çatı eki yoktur, etken çatıdır.','bilgi')],
 'B','İşteş çatılı fiil.','İşteş çatıda iş karşılıklı ya da birlikte yapılır; -ş çatı ekidir.',[B_GE],
 [AD('İşteşi hatırla','İşteşte iş birlikte ya da karşılıklı yapılır; fiil -ş eki alır.','selamla-ş-: karşılıklı selamlama'),
  AD('Şıkları çöz','sohbet ettiler, götürdük, gelecek, oynadı: çatı eki yok; etken.','A, C, D, E: işteş değil'),
  AD('İşteşi seç','Selamla-ş-tı: komşuların karşılıklı selamlaşmasını bildirir; -ş işteş çatı ekidir.','B: işteş')],
 'Fiilde -ş görünce önce kök mü ek mi diye bak; karşılıklılık anlamı varsa işteştir.')
# 24
S('0024','K-DBFL-08','orta','Yeterlik anlamlı birleşik fiili belirler.',3,
 'Aşağıdaki cümlelerin hangisinde yüklem yeterlik anlamı taşımaktadır?',
 'Bu yükü tek başına kaldırabilirim.',
 [('Çocuk hemen kapıyı açıverdi.','Aç-ıver-di: “-ıver” tezlik anlamı katar.','bilgi'),('Köylüler bu geleneği yüzyıllardır sürdüregelmiştir.','Sürdür-e-gel-miş: “-e gel” sürerlik anlamı katar.','bilgi'),('Küçük kız yerdeki taşa takılıp yuvarlanayazdı.','Yuvarlan-a-yaz-dı: “-a yaz” yaklaşma anlamı katar.','dikkat'),('Yarın erkenden kalkmak istiyorum.','İste-yor-um: yardımcı fiil anlam katmaz; yeterlik yoktur.','dikkat')],
 'C','Yeterlik anlamlı yüklem.','Yeterlik, “yapabilme gücü”nü bildirir; -ebil eki aranır.',[B_AN],
 [AD('Anlam türlerini yaz','yeterlik -ebil, tezlik -iver, sürerlik -edur/-egel/-ekal, yaklaşma -eyaz.','yeterlik: -ebil'),
  AD('Şıkları çöz','açıverdi: tezlik. sürdüregelmiştir: sürerlik. yuvarlanayazdı: yaklaşma. istiyorum: ek yok.','A, B, D, E: yeterlik değil'),
  AD('Yeterliği seç','Kaldır-abil-ir-im: yükü kaldırma gücünü bildiriyor.','C: yeterlik')],
 'Fiildeki -ebil eki “yapabilme gücünü” bildiriyorsa yeterlik anlamıdır.')
# 25
SF('0025','K-DBFL-08','zor','Birleşik fiillerin anlam özelliklerini sırayla eşleştirir.',4,
 'I. Telaşla merdivenden düşeyazdı.\nII. Haberi alınca hemen yola çıkıverdi.\nIII. Kardeşim ağır çantayı tek başına taşıyabiliyor.\nYukarıdaki cümlelerin yüklemlerinde sırasıyla hangi anlam özellikleri vardır?',
 [('yaklaşma – tezlik – yeterlik',None,None),('tezlik – yaklaşma – yeterlik','I’deki “-eyaz” yaklaşma, II’deki “-iver” tezliktir; sıra ters verilmiş.','bilgi'),('yaklaşma – yeterlik – tezlik','II’deki “-ıver” tezlik, III’teki “-ebil” yeterliktir; sıra yanlış.','dikkat'),('yeterlik – tezlik – yaklaşma','Sıra tam tersine verilmiş; I yaklaşma, III yeterliktir.','dikkat'),('sürerlik – tezlik – yeterlik','I’de “-eyaz” sürerlik değil yaklaşma anlamı katar.','bilgi')],
 'A','Anlam özelliklerinin sıralaması.','Her yüklemde yardımcı fiili bul: yaz-, ver-, bil-.',[B_AN],
 [AD('Ekleri hatırla','-eyaz yaklaşma, -iver tezlik, -ebil yeterlik bildirir.','yaz → yaklaşma · ver → tezlik · bil → yeterlik'),
  AD('Yüklemleri çöz','I düş-e-yaz-dı. II çık-ıver-di. III taşı-yabil-iyor.','I: -eyaz · II: -iver · III: -ebil'),
  AD('Sırayı kur','Yaklaşma, tezlik, yeterlik sırası A şıkkında verilmiş.','A: doğru')],
 'Birleşik fiilde asıl fiile eklenen yardımcı fiili (yaz-, ver-, bil-, dur-, kal-) bulursan anlamı kesinleşir.',kalip='öncüllü')
# 26
S('0026','K-DBFL-08','orta','Sürerlik anlamlı birleşik fiili belirler.',3,
 'Aşağıdaki cümlelerin hangisinde yüklem sürerlik anlamı taşımaktadır?',
 'Kuşun uçuşuna öylece bakakaldı.',
 [('Misafir gelince hemen sofrayı kuruverdik.','Kur-uver-di-k: “-iver” tezlik anlamı katar.','bilgi'),('Kardeşim bu çantayı sırtında taşıyabiliyor.','Taşı-yabil-iyor: “-ebil” yeterlik anlamı katar.','bilgi'),('Pasta fırında neredeyse yanayazdı.','Yan-a-yaz-dı: “-a yaz” yaklaşma anlamı katar.','dikkat'),('Kardeşim yarın bize uğrayacak.','Uğra-yacak: yardımcı fiil yok; sürerlik anlamı yoktur.','dikkat')],
 'D','Sürerlik anlamlı yüklem.','Sürerlik, işin uzun süre devam ettiğini bildirir; -edur, -egel, -ekal ekleri aranır.',[B_AN],
 [AD('Anlam türlerini hatırla','Sürerlik eylemin sürüp gitmesini anlatır: yazadurmak, gidegelmek, donakalmak.','-edur · -egel · -ekal'),
  AD('Şıkları çöz','kuruverdik: tezlik. taşıyabiliyor: yeterlik. yanayazdı: yaklaşma. uğrayacak: ek anlam yok.','A, B, C, E: sürerlik değil'),
  AD('Sürerliği seç','Bak-a-kal-dı: bir durumda sürüp kalmayı anlatıyor.','D: sürerlik')],
 'Yardımcı fiil dur-, gel-, kal- ise ve asıl fiile -a/-e ile bağlanıyorsa sürerliktir.')
bitir(Q)
