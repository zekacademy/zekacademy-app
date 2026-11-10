"""TYT Türkçe · Fiiller-Fiilimsiler-Ek Fiiller-Çatı: 4 ana soru (hafif mod). Metinler özgündür."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from hafif_dilbilgisi import *
AD=A
KY='ÖSYM TYT Türkçe 2018–2026 (biçim bilgisi: fiiller) ve MEB Türk Dili ve Edebiyatı müfredatı'
KARTLAR={
 'K-FF-01':dict(alt='Fiilimsiler',fikir='Fiilimsinin türünü (isim-fiil, sıfat-fiil, zarf-fiil) eklerine ve cümledeki göreve göre belirlemek.',tuzak='Fiilimsiyi yüklem sanmak; zarf-fiili sıfat-fiille karıştırmak.',zorluk='kolay',kalip='düz',adim=2,tipId='fii-fiilimsi',kaynak=KY),
 'K-FF-02':dict(alt='Fiillerde Çatı',fikir='Fiilin etken, edilgen, ettirgen ve dönüşlü çatılardan hangisinde olduğunu belirlemek.',tuzak='Çatı ekini görmeden yalnız özneye bakmak.',zorluk='orta',kalip='düz',adim=3,tipId='fii-cati',kaynak=KY),
 'K-FF-03':dict(alt='Ek Fiil',fikir='İsim soylu sözcüğü yüklem yapan ek fiili, fiil çekimindeki kip ekinden ayırmak.',tuzak='Fiile gelen -miş ekini ek fiil sanmak.',zorluk='orta',kalip='düz',adim=3,tipId='fii-ekfiil',kaynak=KY),
 'K-FF-04':dict(alt='Fiilimsi Türlerini Karşılaştırma',fikir='Aynı cümlelerde fiilimsilerin türlerini karşılaştırıp farklı olanı bulmak.',tuzak='Ek benzerliğine bakıp türleri karıştırmak.',zorluk='zor',kalip='düz',adim=4,tipId='fii-karsilastir',kaynak=KY),
}
TIPLER={'fii-fiilimsi':'Fiilimsi türü','fii-cati':'Fiillerde çatı','fii-ekfiil':'Ek fiil','fii-karsilastir':'Fiilimsi türlerini karşılaştırma'}
Q=kur('fiiller','Fiiller-Fiilimsiler-Ek Fiiller-Çatı','tr|Fiiller-Fiilimsiler-Ek Fiiller-Çatı',KARTLAR,TIPLER); Q.n=4
B_FS=B('Fiilimsiler','isim-fiil: -mak, -ma, -ış (kalkmak) · sıfat-fiil: -an, -dık, -ecek, -mış (giren öğrenci) · zarf-fiil: -arak, -ınca, -ip, -madan, -a … -a (koşarak girdi). Fiilimsiler yüklem olmaz, cümlede isim, sıfat ya da zarf görevi görür')
B_CT=B('Çatı','etken: özne işi kendisi yapar (kapıyı açtı) · edilgen: özne iş yapılan şeydir, -l/-n eki (kapı açıldı) · ettirgen: iş başkasına yaptırılır, -dır, -t eki (kestirdi) · dönüşlü: özne işi kendi üzerine yapar (yıkandı)')
B_EF=B('Ek fiil','ek fiil: isim soylu sözcüğü yüklem yapar, kip ve kişi ekleri alır (genişmiş = geniş + imiş, yorgundu = yorgun + idi). Fiile gelen -miş ise kip ekidir, ek fiil değildir (yatmış = yat- + -mış)')

# 0001 fiilimsi · kolay · B
soru(Q,'0001','K-FF-01','kolay','Fiilimsinin isim-fiil olduğu cümleyi bulur.',2,
 'Aşağıdaki cümlelerin hangisinde tırnak içindeki fiilimsi isim-fiildir?',
 [('Dün “gelen” misafirleri karşıladık.','sıfat-fiil','Gel- + -en: “misafirleri” ismini niteleyen sıfat-fiildir.','bilgi'),
  ('Sabah erken “kalkmak” bana iyi geliyor.','isim-fiil','',''),
  ('Çocuk eve neşeyle “koşarak” girdi.','zarf-fiil','Koş- + -arak: “girdi” fiilini niteleyen zarf-fiildir.','bilgi'),
  ('Yağmur “yağınca” biz yola çıkmadık.','zarf-fiil','Yağ- + -ınca: zaman bildiren zarf-fiildir.','dikkat'),
  ('Masada “okunan” kitabı hemen kapattı.','sıfat-fiil','Okun- + -an: “kitabı” ismini niteleyen sıfat-fiildir.','dikkat')],
 'B',lambda t:t=='isim-fiil','İsim-fiil olan sözcük.',
 'İsim-fiil ekleri -mak, -ma, -ış’tır; bu ekleri alan fiilimsiyi ara.',[B_FS],
 [AD('Ekleri hatırla','İsim-fiil eki -mak, -ma, -ış’tır.','isim-fiil: -mak, -ma, -ış'),AD('Şıkları çözümle','gelen ve okunan: -an (sıfat-fiil). koşarak ve yağınca: -arak, -ınca (zarf-fiil).','A, E: sıfat-fiil · C, D: zarf-fiil'),AD('İsim-fiili seç','Kalkmak: kalk- + -mak. Cümlede “kalkmak” özne görevinde bir isim gibi kullanılıyor.','B: isim-fiil')],
 'Fiilimsinin ekine bak: -mak/-ma/-ış isim-fiil, -an/-dık/-ecek sıfat-fiil, -arak/-ınca/-ip zarf-fiildir.')

# 0002 çatı · orta · D
soru(Q,'0002','K-FF-02','orta','Fiilin ettirgen çatılı olduğu cümleyi bulur.',3,
 'Aşağıdaki cümlelerin hangisinde fiil ettirgen çatılıdır?',
 [('Ayşe pencereyi açtı.','etken','Aç- kök fiil; iş doğrudan özne tarafından yapılıyor, etken çatıdır.','bilgi'),
  ('Ders bitince bahçeye çıktılar.','etken','Çık- kök fiil; çatı eki yoktur, etken çatıdır.','bilgi'),
  ('Yemek annem tarafından hazırlandı.','edilgen','Hazırla-n-: özne işi yapan değil, işten etkilenendir; edilgendir.','dikkat'),
  ('Ali saçını kestirdi.','ettirgen',' ',''),
  ('Misafirler akşam geç geldi.','etken','Gel- kök fiil; çatı eki yoktur, etken çatıdır.','bilgi')],
 'D',lambda t:t=='ettirgen','Fiilin ettirgen çatılı olduğu cümle.',
 'Ettirgen çatıda iş özne tarafından değil, başkasına yaptırılarak yapılır; -dır ve -t eklerini ara.',[B_CT],
 [AD('Ettirgen çatıyı hatırla','İş özne tarafından değil başkasına yaptırılarak gerçekleşir; -dır, -t, -ir ekleri kullanılır.','kes-tir-: yaptırma'),AD('Şıkları çözümle','açtı, çıktılar, geldi: çatı eki yok, etken. hazırlandı: -n eki ve “tarafından” ile edilgen.','A, B, E: etken · C: edilgen'),AD('Ettirgeni seç','Kestirdi: kes- + -tir. Ali saçını kendisi kesmiyor, birine kestiriyor.','D: ettirgen')],
 'Fiilde -dır/-t ekini görürsen “başkasına yaptırılıyor mu?” diye sor.')

# 0003 ek fiil · orta · A
soru(Q,'0003','K-FF-03','orta','Yüklemin rivayet anlamı katan ek fiille çekimlendiği cümleyi bulur.',3,
 'Aşağıdaki cümlelerin hangisinin yüklemi, rivayet (öğrenilen geçmiş zaman) anlamı katan ek fiille çekimlenmiştir?',
 [('Komşumuzun bahçesi çok genişmiş.','ek','',''),
  ('Çocuk akşam erkenden uyumuş.','fiil','Uyu- fiil kökü + -muş: kip ekidir, yüklem fiildir; ek fiil yoktur.','bilgi'),
  ('Annem sabah pazara gitmiş.','fiil','Git- fiil kökü + -miş: fiilin kip ekidir; ek fiil değildir.','bilgi'),
  ('Kardeşim dün gece geç yatmış.','fiil','Yat- fiil kökü + -mış: kip ekidir; ek fiil yoktur.','dikkat'),
  ('Babam bu sabah işe erken çıkmış.','fiil','Çık- fiil kökü + -mış: kip ekidir; ek fiil yoktur.','dikkat')],
 'A',lambda t:t=='ek','Yüklemi ek fiille çekimlenmiş cümle.',
 'Yüklemin kökü fiil mi, isim soylu bir sözcük mü? Fiil kökü olanlarda -miş ek fiil değildir.',[B_EF],
 [AD('Yüklemin kökünü bul','Ek fiil, isim soylu sözcüğü yüklem yapar; kökü fiilse ek fiil yoktur.','kök fiil → ek fiil yok'),AD('Şıkları çözümle','uyumuş: uyu-, gitmiş: git-, yatmış: yat-, çıkmış: çık-. Hepsi fiil kökü; -miş kip ekidir.','B, C, D, E: fiil çekimi'),AD('Ek fiili seç','Genişmiş: geniş (sıfat) + imiş. İsim soylu sözcük ek fiille yüklem olmuştur.','A: geniş+miş')],
 'Yüklemde -miş görünce önce köke bak: isim soylu ise ek fiil, fiil ise kip ekidir.')

# 0004 fiilimsi karşılaştırma · zor · E
soru(Q,'0004','K-FF-04','zor','Fiilimsilerin türünü karşılaştırarak farklı olanı belirler.',4,
 'Aşağıdaki cümlelerde tırnak içinde verilen fiilimsilerden hangisi türü bakımından diğerlerinden farklıdır?',
 [('“Bildiğimiz” yoldan gitmeyi tercih ettik.','sıfat-fiil','Bil- + -dik: “yol” ismini niteleyen sıfat-fiildir; diğerleriyle aynı türdedir.','bilgi'),
  ('Sınıfa “giren” öğrenci selam verdi.','sıfat-fiil','Gir- + -en: “öğrenci” ismini niteleyen sıfat-fiildir; diğerleriyle aynı türdedir.','bilgi'),
  ('Yarın “alacağım” kitabı sana göstereceğim.','sıfat-fiil','Al- + -acak: “kitabı” ismini niteleyen sıfat-fiildir.','dikkat'),
  ('“Yırtılmış” defteri çöpe attı.','sıfat-fiil','Yırtıl- + -mış: “defteri” ismini niteleyen sıfat-fiildir.','dikkat'),
  ('Sabah erken “kalkmak” zordur.','isim-fiil','','')],
 'E',lambda t:t=='isim-fiil','Türü diğerlerinden farklı olan fiilimsi.',
 'Önce her fiilimsinin bir isim mi niteleyip nitelemediğine bak.',[B_FS],
 [AD('Ek ve görevi yaz','Sıfat-fiil bir ismi niteler; isim-fiil isim gibi kullanılır.','sıfat-fiil: isim niteler'),AD('Dört şıkkı çöz','bildiğimiz yol, giren öğrenci, alacağım kitap, yırtılmış defter: hepsinde fiilimsi bir ismi niteliyor.','A, B, C, D: sıfat-fiil'),AD('Farklı olanı seç','“Kalkmak” bir ismi nitelemiyor, cümlede özne gibi kullanılıyor; -mak eki isim-fiil yapar.','E: isim-fiil')],
 'Farklı olanı bulurken dört şıkkın ortak özelliğini önce bul, sonra uymayanı seç.')
bitir(Q)
