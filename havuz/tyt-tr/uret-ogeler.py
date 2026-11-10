"""TYT Türkçe · Cümlenin Ögeleri: 6 ana soru (hafif mod). Metinler özgündür."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from hafif_dilbilgisi import *
AD=A
KY='ÖSYM TYT Türkçe 2018–2026 (cümlenin ögeleri) ve MEB Türk Dili ve Edebiyatı müfredatı'
KARTLAR={
 'K-OGE-01':dict(alt='Yüklem',fikir='Yüklemin fiil ya da isim soylu olduğunu (ek fiil) belirlemek.',tuzak='“-di” ekini görüp isim yüklemini fiil yüklemi sanmak.',zorluk='kolay',kalip='düz',adim=2,tipId='oge-yuklem',kaynak=KY),
 'K-OGE-02':dict(alt='Özne',fikir='Gizli özneyi yüklemdeki kişi ekinden tanımak.',tuzak='Cümledeki herhangi bir adı özne sanmak.',zorluk='orta',kalip='düz',adim=3,tipId='oge-ozne',kaynak=KY),
 'K-OGE-03':dict(alt='Nesne',fikir='Geçişli fiilin nesnesinin bulunup bulunmadığını “neyi/kimi” sorusuyla belirlemek.',tuzak='Yönelme, bulunma, ayrılma hâlindeki öbekleri nesne sanmak.',zorluk='orta',kalip='düz',adim=3,tipId='oge-nesne',kaynak=KY),
 'K-OGE-04':dict(alt='Belirtili ve Belirtisiz Nesne',fikir='Nesnenin “-i” belirtme hâli eki alıp almadığına bakarak belirtili/belirtisiz ayrımı yapmak.',tuzak='Belirtisiz nesneyi dolaylı tümleç sanmak.',zorluk='orta',kalip='düz',adim=3,tipId='oge-belirtisiz',kaynak=KY),
 'K-OGE-05':dict(alt='Sözde (Gerçek Olmayan) Özne',fikir='Edilgen çatılı yüklemin öznesinin eylemi yapan değil, eylemden etkilenen olduğunu bilmek.',tuzak='Cümlenin başındaki adı her zaman gerçek özne saymak.',zorluk='zor',kalip='düz',adim=4,tipId='oge-sozde',kaynak=KY),
 'K-OGE-06':dict(alt='Ek Fiil ve Gizli Özne',fikir='İsim yüklemi ile gizli özneyi aynı cümlede birlikte tanımak.',tuzak='Yüklemin türü ile öznenin açık/gizli olduğunu karıştırmak.',zorluk='zor',kalip='düz',adim=4,tipId='oge-ekfiil',kaynak=KY),
}
TIPLER={'oge-yuklem':'Yüklem türü','oge-ozne':'Özne','oge-nesne':'Nesne','oge-belirtisiz':'Belirtili ve belirtisiz nesne','oge-sozde':'Sözde özne','oge-ekfiil':'Ek fiil ve gizli özne'}
Q=kur('ogeler','Cümlenin Ögeleri','tr|Cümlenin Ögeleri',KARTLAR,TIPLER); Q.n=6
Y='yok'; D='var'
B_YUK=B('Yüklem türü','fiil yüklemi: eylem bildirir (Çocuk koştu.) · isim yüklemi: isim soylu sözcük + ek fiil (Konser güzeldi.)')
B_OZ=B('Özne','yükleme “kim, ne” diye sorulunca bulunur · gizli özne: cümlede yazılmayan, yüklemin kişi ekinden anlaşılan özne (Eve döndük → biz)')
B_NES=B('Nesne','geçişli fiile “neyi, kimi” (belirtisiz nesnede “ne”) sorusuyla bulunur · “Annem mektubu yazdı.” → neyi yazdı? mektubu · yönelme, bulunma, ayrılma hâlleri nesne değildir')
B_BEL=B('Belirtili / belirtisiz nesne','belirtili nesne -i (belirtme) hâl eki alır (kitabı okudu) · belirtisiz nesne ek almaz (kitap okudu)')
B_SOZ=B('Sözde özne','edilgen çatılı yüklemin öznesi eylemi yapan değil eylemden etkilenendir; buna sözde özne denir · “Mektup yazıldı.” (yapan belli de olabilir: Mektup Ali tarafından yazıldı.)')

# 0001 yüklem · kolay · E
soru(Q,'0001','K-OGE-01','kolay','Yüklemin isim soylu olduğu cümleyi belirler.',2,
 'Aşağıdaki cümlelerin hangisinin yüklemi isim soyludur?',
 [('Kapıyı yavaşça açtı.','fiil','“Açtı” eylem bildirir; yüklem fiil soyludur.','bilgi'),
  ('Çocuklar parkta oynuyordu.','fiil','“Oynuyordu” bir eylemdir; yüklem fiil soyludur.','dikkat'),
  ('Yağmur dün gece başladı.','fiil','“Başladı” fiildir; yüklem fiil soyludur.','bilgi'),
  ('Kitabı masanın üzerine bıraktım.','fiil','“Bıraktım” fiildir; yüklem fiil soyludur.','bilgi'),
  ('Bu akşamki konser çok güzeldi.','isim','','')],
 'E',lambda t:t=='isim','Yüklemi isim soylu olan cümle.',
 'Yüklem bir eylem mi bildiriyor, yoksa bir durum/nitelik mi?',[B_YUK],
 [AD('Yüklem türlerini hatırla','Eylem bildiren yüklem fiil soyludur; isim soylu sözcük + ek fiil isim yüklemidir.','fiil · isim+ek fiil'),AD('Yüklemleri bul','A: açtı, B: oynuyordu, C: başladı, D: bıraktım. Hepsi eylem bildirir.','A, B, C, D: fiil'),AD('İsim yüklemini seç','E’de “güzeldi” (güzel + ek fiil -di) konserin niteliğini bildirir.','E: isim yüklemi')],
 'Yüklem “ne yaptı?” sorusuna cevap vermiyorsa, “nasıl/ne?” diyorsa isim soyludur.')

# 0002 gizli özne · orta · A
soru(Q,'0002','K-OGE-02','orta','Gizli özneyi yüklemin kişi ekinden tanır.',3,
 'Aşağıdaki cümlelerin hangisinde özne gizlidir?',
 [('Sabah erkenden kalkıp yola çıktık.','gizli','',''),
  ('Misafirler akşam yemeğinden sonra gitti.','açık','Özne “misafirler” cümlede yazılmıştır; gizli değildir.','dikkat'),
  ('Bu mektubu Ahmet yazmış.','açık','Özne “Ahmet” cümlede açıkça yer alır.','bilgi'),
  ('Çocuklar bahçede oynuyor.','açık','Özne “çocuklar” cümlede yazılmıştır.','bilgi'),
  ('Annem yemeği hazırladı.','açık','Özne “annem” cümlede yazılmıştır.','dikkat')],
 'A',lambda t:t=='gizli','Öznesi gizli olan cümle.',
 'Yükleme “kim?” diye sor; cevap cümlede yazıyor mu?',[B_OZ],
 [AD('Yükleme sor','Her cümlede yükleme “kim?” sorusunu yönelt.','kim?'),AD('Cevabı ara','B, C, D ve E’de cevap cümlede yazılı: misafirler, Ahmet, çocuklar, annem.','B, C, D, E: özne açık'),AD('Gizliyi seç','A’da “çıktık” kişi ekinden “biz” anlaşılır; özne yazılmamıştır.','A: biz')],
 'Yükleme “kim?” diye sor; cevap cümlede yoksa ama kişi ekinden anlaşılıyorsa özne gizlidir.')

# 0003 nesne yok · orta · C
soru(Q,'0003','K-OGE-03','orta','Nesnenin bulunmadığı cümleyi belirler.',3,
 'Aşağıdaki cümlelerin hangisinde nesne yoktur?',
 [('Annem bu sabah pazardan elma aldı.',D,'“Neyi aldı?” sorusunun cevabı “elma”dır; cümlede nesne vardır.','dikkat'),
  ('Öğretmen soruları dikkatle tahtaya yazdı.',D,'“Neyi yazdı?” sorusunun cevabı “soruları”dır; nesne vardır.','bilgi'),
  ('Misafirler yemekten sonra evden ayrıldı.',Y,'',''),
  ('Ayşe odasında mektubu sessizce okudu.',D,'“Neyi okudu?” sorusunun cevabı “mektubu”dur; nesne vardır.','bilgi'),
  ('Dedem eski bahçeye yeni fidanlar dikti.',D,'“Ne dikti?” sorusunun cevabı “yeni fidanlar”dır; nesne vardır.','bilgi')],
 'C',lambda t:t==Y,'Nesnesi bulunmayan cümle.',
 'Her yükleme “neyi / kimi / ne?” sorusunu yönelt; cevap bulunamayan cümleyi ara.',[B_NES],
 [AD('Nesneyi bulma yolunu hatırla','Yükleme “neyi, kimi, ne?” sorusu sorulur; cevap nesnedir.','neyi? kimi? ne?'),AD('Şıkları ele','A: elma, B: soruları, D: mektubu, E: yeni fidanlar. Hepsi nesnedir.','A, B, D, E: nesne var'),AD('Nesnesizi seç','C’de “evden” ayrılma hâlindedir; “neyi/ne?” sorusuna cevap vermez, nesne yoktur.','C: nesne yok')],
 'Yönelme (-e), bulunma (-de), ayrılma (-den) ekli öbekler nesne olmaz.')

# 0004 belirtisiz nesne · orta · B
soru(Q,'0004','K-OGE-04','orta','Belirtisiz nesnenin bulunduğu cümleyi belirler.',3,
 'Aşağıdaki cümlelerin hangisinde belirtisiz nesne vardır?',
 [('Ayşe sabah mektubu okudu.','belirtili','“Mektubu” -u belirtme hâl ekini almıştır; belirtili nesnedir.','bilgi'),
  ('Babam yeni bir araba aldı.','belirtisiz','',''),
  ('Babam arabayı garaja çekti.','belirtili','“Arabayı” -ı hâl ekini almıştır; belirtili nesnedir.','dikkat'),
  ('Öğretmen öğrencileri salona çağırdı.','belirtili','“Öğrencileri” -i hâl ekini almıştır; belirtili nesnedir.','bilgi'),
  ('Kardeşim kitabı çantasına koydu.','belirtili','“Kitabı” belirtme hâl ekiyle kullanılmıştır; belirtilidir.','dikkat')],
 'B',lambda t:t=='belirtisiz','Belirtisiz nesne bulunan cümle.',
 'Nesne “-i” belirtme hâl eki almıyorsa belirtisizdir.',[B_BEL],
 [AD('Ayrımı hatırla','Belirtili nesne -i/-ı/-u/-ü eki alır; belirtisiz nesne ek almaz.','kitabı (belirtili) · kitap (belirtisiz)'),AD('Nesneleri bul','A: mektubu, C: arabayı, D: öğrencileri, E: kitabı. Hepsi -i hâl eki almış.','A, C, D, E: belirtili'),AD('Belirtisizi seç','B’de “yeni bir araba” ek almamış nesnedir.','B: belirtisiz')],
 'Nesneye “-i” ekini ekleyebiliyor ama eklenmemişse nesne belirtisizdir.')

# 0005 sözde özne · zor · D
soru(Q,'0005','K-OGE-05','zor','Edilgen çatılı cümledeki sözde özneyi belirler.',4,
 'Aşağıdaki cümlelerin hangisinde özne, sözde (gerçek olmayan) öznedir?',
 [('Kuşlar sabah erkenden ötmeye başladı.','gerçek','Kuşlar eylemi yapan gerçek öznedir; yüklem etkendir.','bilgi'),
  ('Öğretmen ödevleri toplayıp çıktı.','gerçek','Öğretmen eylemi yapar; gerçek özne.','dikkat'),
  ('Ayşe pencereyi açıp dışarı baktı.','gerçek','Ayşe eylemi yapan gerçek öznedir.','bilgi'),
  ('Bu mektup dün akşam yazıldı.','sözde',''.strip(),''),
  ('Kardeşim akşam erkenden uyudu.','gerçek','Kardeşim eylemi yapan gerçek öznedir.','dikkat')],
 'D',lambda t:t=='sözde','Öznesi sözde özne olan cümle.',
 'Edilgen yüklem ara; eylemi yapan değil eylemden etkilenen ad özne olmuştur.',[B_SOZ],
 [AD('Kavramı hatırla','Edilgen çatılı yüklemin öznesi eylemi yapan değil, eylemden etkilenendir (sözde özne).','edilgen yüklem → sözde özne'),AD('Yüklemleri incele','A, B, C ve E’deki yüklemler etkendir: başladı, çıktı, baktı, uyudu.','A, B, C, E: gerçek özne'),AD('Edilgeni bul','D’deki “yazıldı” edilgendir; “mektup” yazma eylemini yapmaz, ondan etkilenir.','D: sözde özne')],
 'Yüklem edilgense (-l/-n) özne eylemi yapan değil, eylemden etkilenendir: sözde özne.')

# 0006 ek fiil + gizli özne · zor · A
soru(Q,'0006','K-OGE-06','zor','Hem isim yüklemli hem öznesi gizli olan cümleyi belirler.',4,
 'Aşağıdaki cümlelerin hangisinde yüklem isim soyludur ve özne gizlidir?',
 [('Çok yorgunduk.',('isim','gizli'),'',''),
  ('Çocuklar çok yorgundu.',('isim','açık'),'Yüklem isim soyludur ama özne “çocuklar” açıkça yazılmıştır.','dikkat'),
  ('Eve erken döndük.',('fiil','gizli'),'Özne gizli (biz) ama yüklem “döndük” fiil soyludur.','bilgi'),
  ('Kitabı yarın okurum.',('fiil','gizli'),'Özne gizli (ben) ama yüklem “okurum” fiildir.','bilgi'),
  ('Ahmet eve geldi.',('fiil','açık'),'Hem yüklem fiil soyludur hem özne “Ahmet” açıktır.','dikkat')],
 'A',lambda t:t==('isim','gizli'),'Yüklemi isim soylu ve öznesi gizli olan cümle.',
 'Önce yüklemin fiil mi isim mi olduğuna, sonra öznenin yazılı olup olmadığına bak.',[B_YUK,B_OZ],
 [AD('İki ölçütü ayır','Cümlede hem yüklem türüne (fiil/isim) hem özneye (açık/gizli) bak.','yüklem + özne'),AD('Şıkları tabloya dök','A isim+gizli · B isim+açık · C fiil+gizli · D fiil+gizli · E fiil+açık.','A: isim, gizli'),AD('Sonucu seç','A’da “yorgunduk” = yorgun + ek fiil + kişi eki; “biz” özne yazılmamıştır.','A: doğru')],
 'İsim yüklemini ek fiilden, gizli özneyi kişi ekinden tanı; iki ölçütü ayrı ayrı denetle.')
bitir(Q)
