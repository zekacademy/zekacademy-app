"""TYT Türkçe · Cümle Türleri genişletme: 8 soru (hafif mod). Metinler özgündür."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from hafif_db import *
AD=A
KY='ÖSYM TYT Türkçe 2018–2026 · Bilgi Sarmal Dil Bilgisi SB (ÖSYM Tipi) · TDK Yazım Kılavuzu'
def K(alt,fikir,tuzak,zor,kalip,adim,tip): return dict(alt=alt,fikir=fikir,tuzak=tuzak,zorluk=zor,kalip=kalip,adim=adim,tipId=tip,kaynak=KY)
KARTLAR={
 'K-DBCT-01':K('Yapısına Göre Cümleler','Cümlenin basit, birleşik (fiilimsili, şartlı, -ki’li) ya da sıralı olduğunu yargı ve yüklem sayısına göre belirlemek.','Uzun cümleyi birleşik, fiilimsili cümleyi basit sanmak.','orta','düz',3,'dct-yapi'),
 'K-DBCT-02':K('Yüklemin Yeri ve Türü','Yüklemin cümledeki yerine göre kurallı/devrik ayrımını yapmak; yapıyla birlikte değerlendirmek.','Devrik cümleyi yalnız yapıdan ayırmaya çalışmak.','orta','düz',3,'dct-yer'),
 'K-DBCT-03':K('Anlamına Göre Cümleler','Cümlenin biçimce ve anlamca olumlu/olumsuz olup olmadığını yüklemine bakarak belirlemek.','Fiilimsideki olumsuzluğu yüklemin olumsuzluğu sanmak; soru biçimini anlamca olumlu saymak.','zor','düz',3,'dct-anlam'),
}
TIPLER={'dct-yapi':'Yapısına göre cümleler','dct-yer':'Yüklemin yerine göre cümleler','dct-anlam':'Anlamına göre cümleler'}
Q=kur('dcumle','Cümle Türleri','tr|Cümle Türleri',KARTLAR,TIPLER); Q.n=8
def S(no,kart,zor,kaz,adim,metin,dogru,yan,harf,istenen,ip,bilgi,adimlar,puf,kalip='düz'):
    L='ABCDE'; yi=iter(yan); opts=[]
    for l in L:
        if l==harf: opts.append((dogru,D,'',''))
        else:
            m,c,t=next(yi); opts.append((m,Y,c,t))
    soru(Q,no,kart,zor,kaz,adim,metin,opts,harf,lambda e:e==D,istenen,ip,bilgi,adimlar,puf,kalip=kalip)
B_YP=B('Yapısına göre cümle','basit: tek yargı, fiilimsi yok (Çocuk top oynadı) · birleşik: fiilimsi, şart ya da -ki’li yan yargı içerir (Sınava çalışırsa kazanır; Yazı yazarken güldü; Öyle yoruldum ki oturdum) · sıralı: birbirinden bağımsız birden çok yargı (Ali gitti, Ayşe geldi)')
B_YR=B('Yüklemin yerine göre','kurallı: yüklem sonda (Eve döndük) · devrik: yüklem sonda değil (Döndük eve)')
B_AN=B('Olumlu / olumsuz','cümle yüklemine göre olumlu ya da olumsuzdur; fiilimsideki olumsuzluk cümleyi olumsuz yapmaz (Teşekkür etmeden ayrıldı: olumlu) · soru biçimi anlamca olumsuz olabilir (Bunu kim bilebilir? = kimse bilemez)')

S('0001','K-DBCT-01','kolay','Fiilimsi içeren cümleyi birleşik cümle olarak ayırır.',2,
 'Aşağıdakilerden hangisinde yüklem dışında bir fiilimsi bulunduğu için cümle birleşiktir?',
 'Kardeşim yeni aldığı kitabı okuyor.',
 [('Annem akşam yemeğine çorba yaptı.','Tek yargı ve tek yüklem var; fiilimsi yok. Basit cümledir.','bilgi'),
  ('Misafirler yarın sabah erkenden gelecek.','Yalnız bir yüklem var; fiilimsi içermez. Basit cümledir.','bilgi'),
  ('Öğrenciler sınıfa sessizce girdi.','Tek yüklemli, fiilimsisiz basit cümledir.','dikkat'),
  ('Bahçedeki gül çok güzel kokuyor.','“Bahçedeki” sıfat-fiil değil, ilgi ekli sıfattır; cümle basittir.','dikkat')],
 'C','Birleşik cümle.','Yüklem dışında bir fiilimsi var mı?',[B_YP],
 [AD('Ölçütü hatırla','Birleşik cümlede fiilimsi ya da şartlı/-ki’li yan yargı bulunur.','fiilimsi → birleşik'),
  AD('Şıkları çöz','A, B, D, E’de yüklem dışında fiilimsi yok; bahçe-de-ki ilgi ekli sıfattır.','A, B, D, E: basit'),
  AD('Birleşiği seç','Al-dığ-ı: “kitabı” niteleyen sıfat-fiil; cümle birleşiktir.','C: birleşik')],
 'Yüklem dışında fiil kökünden türemiş bir sözcük görüyorsan fiilimsidir; cümle birleşiktir.')
S('0002','K-DBCT-02','kolay','Yüklemi sonda olmayan (devrik) cümleyi bulur.',2,
 'Aşağıdaki cümlelerin hangisi yüklemin yerine göre devrik cümledir?',
 'Çok severdim ben o şehri.',
 [('Bu yıl yaz erken geldi.','Yüklem “geldi” sonda; kurallı cümledir.','bilgi'),
  ('Çocuklar akşam parka gitti.','Yüklem “gitti” sonda; kurallı cümledir.','bilgi'),
  ('Sabah erkenden pazara çıktık.','Yüklem “çıktık” sonda; kurallı cümledir.','dikkat'),
  ('Yarınki toplantı saat ikide başlayacak.','Yüklem “başlayacak” sonda; kurallı cümledir.','dikkat')],
 'A','Devrik cümle.','Yüklemi cümlenin sonunda mı arıyorsun? Sonda olmayan devriktir.',[B_YR],
 [AD('Tanımı hatırla','Yüklem cümlenin sonundaysa kurallı, başka yerdeyse devrik cümledir.','yüklem sonda → kurallı'),
  AD('Şıkları çöz','geldi, gitti, çıktık, başlayacak: hepsi cümlenin son sözcüğü.','B, C, D, E: kurallı'),
  AD('Devriği seç','“Severdim” yüklemi sonda değil; ardından “ben o şehri” gelmiş.','A: devrik')],
 'Önce yüklemi bul, sonra ondan sonra kaç sözcük geldiğini say; sıfırdan fazlaysa devriktir.')
S('0003','K-DBCT-03','orta','Biçimce olumlu, anlamca olumsuz cümleyi bulur.',3,
 'Aşağıdaki cümlelerin hangisi biçimce olumlu, anlamca olumsuzdur?',
 'Bu konudan ben ne anlarım?',
 [('Dün akşam eve uğramadım.','Yüklem olumsuz ve anlam da olumsuz; biçimce olumsuz cümledir.','bilgi'),
  ('Bu gece erken yatıp sabah erken kalkacağız.','Yüklem olumlu ve anlam da olumlu cümledir.','bilgi'),
  ('Yarın bize gelecek misin?','Yüklem olumlu, bilgi isteyen gerçek bir sorudur; anlam da olumludur.','dikkat'),
  ('Bu sorunu kimse çözemedi.','Yüklem olumsuz ve anlam olumsuz; biçimce olumsuz cümledir.','dikkat')],
 'D','Biçimce olumlu, anlamca olumsuz cümle.','Yükleminin biçimine bak; sonra cümlenin gerçekte neyi reddettiğini düşün.',[B_AN],
 [AD('Tanımı hatırla','Biçim yüklemin eki, anlam cümlenin verdiği hükümdür; ikisi farklı olabilir.','biçim ↔ anlam'),
  AD('Şıkları çöz','A ve E: olumsuz–olumsuz. B ve C: olumlu–olumlu.','A, B, C, E: ikisi de aynı'),
  AD('Farklıyı seç','“Anlarım” olumlu biçimde, ama “Ben bu konudan hiçbir şey anlamam” demek istiyor.','D: olumlu biçim, olumsuz anlam')],
 'Yüklemin ekine bak: olumluysa biçim olumlu; sonra cümle bir şeyi reddediyorsa anlam olumsuzdur.')
S('0004','K-DBCT-01','kolay','Şartlı birleşik cümleyi diğer yapılardan ayırır.',3,
 'Aşağıdaki cümlelerin hangisi şartlı birleşik cümledir?',
 'Yağmur yağarsa maçı erteleyeceğiz.',
 [('Maç yarın akşam saat sekizde başlayacak.','Tek yargı var; şart yok. Basit cümledir.','bilgi'),
  ('Maçı izleyen taraftarlar çok sevindi.','“İzleyen” sıfat-fiil; cümle birleşiktir ama şartlı değildir.','bilgi'),
  ('Takım sahaya çıkar çıkmaz bir gol buldu.','“Çıkar çıkmaz” zarf-fiil; cümle birleşiktir ama şartlı değildir.','dikkat'),
  ('Stat dolu, tribünler coşkuluydu.','İki bağımsız yargı var; sıralı cümledir.','dikkat')],
 'A','Şartlı birleşik cümle.','Şart ekini (-sa/-se) taşıyan yan yargıyı ara.',[B_YP],
 [AD('Şartlıyı tanı','Şartlı birleşik cümlede yüklem dışında -sa/-se eki taşıyan bir yan yargı bulunur.','-sa/-se → şart'),
  AD('Şıkları çöz','B basit; C ve D fiilimsili birleşik (izleyen, çıkar çıkmaz); E sıralı.','B, C, D, E: şartlı değil'),
  AD('Şartlıyı seç','Yağ-ar-sa: şart eki; “maçı erteleyeceğiz” ana yargı.','A: şartlı birleşik')],
 'Cümlede -sa/-se ekli bir yan yargı varsa cümle şartlı birleşiktir.')
S('0005','K-DBCT-03','orta','Olumsuz fiilimsi taşıyan olumlu cümleyi bulur.',4,
 'Aşağıdaki cümlelerin hangisinde olumsuzluk eki taşıyan bir fiilimsi vardır, ancak cümle yüklemine göre olumludur?',
 'Çocuk kimseye görünmeden kapıdan çıktı.',
 [('Bu sabah kimseyle konuşmadık.','Yüklem olumsuz; fiilimsi yok. Cümle olumsuzdur.','bilgi'),
  ('Bu yoldan geçen kimse olmadı.','Yüklem “olmadı” olumsuz; cümle olumsuzdur. “Geçen” olumsuzluk eki almamıştır.','bilgi'),
  ('Annem akşamları ışığı söndürmez.','Yüklem olumsuz; fiilimsi yok.','dikkat'),
  ('Yarınki sınava iyi hazırlanmış çocuklar sevinçle çıktı.','Fiilimsi var ama olumsuz değil; yüklem olumludur.','dikkat')],
 'B','Olumsuz fiilimsili olumlu cümle.','İki şeyi ayrı sına: fiilimsi olumsuz mu, yüklem olumlu mu?',[B_AN,B_YP],
 [AD('İki ölçütü yaz','Fiilimsi -ma/-me almış, yüklem olumlu olacak.','fiilimsi: -madan · yüklem: olumlu'),
  AD('Şıkları çöz','A, C, D’de yüklem olumsuz; E’de fiilimsi olumsuz değil.','A, C, D, E: ölçüt yok'),
  AD('İkisini sağlayanı seç','Gör-ün-me-den: olumsuz zarf-fiil; “çıktı” olumlu.','B: doğru')],
 'Olumsuzluk ekini bulunca nerede olduğuna bak: fiilimsideyse cümle olumsuz olmaz.')
S('0006','K-DBCT-02','orta','Hem birleşik hem devrik cümleyi belirler.',4,
 'Aşağıdaki cümlelerin hangisi hem birleşik hem devrik bir cümledir?',
 'Yağmur yağınca çıkmadık dışarı.',
 [('Çocuklar parka gitti, babaları evde kaldı.','İki bağımsız yargı: sıralı cümle; yüklemler sonda, kurallıdır.','bilgi'),
  ('Eve gelen misafirler çok memnun görünüyordu.','Birleşik (gelen) ama yüklem sonda; kurallıdır.','bilgi'),
  ('Dün akşam çok güzel bir film seyrettik.','Basit ve kurallı cümledir.','dikkat'),
  ('Sevdim ben bu kasabayı.','Devrik ama tek yargılı; basit cümledir.','dikkat')],
 'E','Birleşik ve devrik cümle.','İki özelliği ayrı ayrı denetle: fiilimsi var mı, yüklem sonda mı?',[B_YP,B_YR],
 [AD('İki ölçütü yaz','Cümlede fiilimsi ya da yan yargı olacak ve yüklem sonda olmayacak.','birleşik + devrik'),
  AD('Şıkları çöz','A sıralı, B birleşik ama kurallı, C basit ve kurallı, D devrik ama basit.','A, B, C, D: ikisi birden yok'),
  AD('İkisini içereni seç','“Yağınca” zarf-fiildir (birleşik); “çıkmadık” yüklemi sonda değil (devrik).','E: birleşik + devrik')],
 'Karma soruda iki özelliği iki satırda ayrı ayrı yaz; ikisinin de “evet” çıktığı şıkkı seç.')
S('0007','K-DBCT-01','orta','Sıralı cümleyi birleşik cümlelerden ayırır.',4,
 'Aşağıdaki cümlelerin hangisi sıralı cümledir?',
 'Dışarıda kar yağıyor, biz içeride çay içiyoruz.',
 [('Eve gelir gelmez ödevlerine başladı.','Gel-ir gel-mez zarf-fiildir; cümle birleşiktir.','bilgi'),
  ('Annemin bize anlattığı masalı hâlâ hatırlıyorum.','Anlat-tığ-ı sıfat-fiildir; cümle birleşiktir.','bilgi'),
  ('Hava güzel olursa, hafta sonu pikniğe gideriz.','Ol-ur-sa şart ekli yan yargıdır; cümle birleşiktir.','dikkat'),
  ('Biliyorum ki sen bu işi başarırsın.','“Ki” ile bağlanmış yan yargı vardır; cümle birleşiktir.','dikkat')],
 'B','Sıralı cümle.','Yargıların birbirine bağlı mı, bağımsız mı olduğuna bak.',[B_YP],
 [AD('Ölçütü hatırla','Sıralı cümlede bağımsız yargılar yan yana gelir; birleşikte fiilimsi, şart ya da “ki” bir yan yargı kurar.','sıralı: bağımsız yargılar'),
  AD('Şıkları çöz','Zarf-fiil, sıfat-fiil, şart eki ve “ki”: dördü de yan yargı kurar.','birleşik: zarf-fiil, sıfat-fiil, şart, ki'),
  AD('Farklıyı seç','B: yağıyor ve içiyoruz; iki bağımsız yargı, fiilimsi yok; sıralı cümle.','B: sıralı')],
 'Fiilimsi, şart eki ya da “ki” yoksa ve iki yüklem birbirinden bağımsızsa cümle sıralıdır.')
S('0008','K-DBCT-01','orta','Numaralı cümleler arasında birleşik cümleyi bulur.',3,
 '(I) Kasaba dağların eteğinde kurulmuştur. (II) Sabahları sis gölün üzerinden yükselir. (III) Gölün kıyısında yürüyen yolcular, kuşların seslerini dinler. (IV) Akşamüstü çarşıda esnaf dükkânlarını kapatır. (V) Geceleri sokaklar sessizleşir.\nBu parçadaki numaralanmış cümlelerden hangisi birleşik cümledir?',
 'III',
 [('I','Tek yargı ve tek yüklem var; fiilimsi yoktur. Basit cümledir.','bilgi'),('II','Tek yüklem (yükselir) var; basit cümledir.','bilgi'),('IV','Tek yüklem (kapatır) var; fiilimsi yok, basit cümledir.','dikkat'),('V','Tek yüklem (sessizleşir) var; basit cümledir.','dikkat')],
 'C','Birleşik cümle.','Her cümlede yüklem dışında fiilimsi ara.',[B_YP],
 [AD('Ölçütü hatırla','Birleşik cümlede yüklem dışında fiilimsi ya da yan yargı vardır.','fiilimsi → birleşik'),
  AD('Cümleleri çöz','I kurulmuştur, II yükselir, IV kapatır, V sessizleşir: tek yüklem, fiilimsi yok.','I, II, IV, V: basit'),
  AD('Birleşiği seç','Yürü-yen: “yolcular” ismini niteleyen sıfat-fiil; III birleşiktir.','III: birleşik')],
 'Parçalı sorularda her cümlede önce yüklemi bul, sonra yüklem dışında fiilimsi var mı diye bak.',kalip='öncüllü')
bitir(Q)
