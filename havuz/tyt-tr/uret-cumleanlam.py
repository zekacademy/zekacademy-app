"""TYT Türkçe · Cümlede Anlam: 8 ana + 8 kardeş. Metinler özgündür."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from tr_ortak import *

KARTLAR={
 'K-CAN-01':dict(alt='Cümleden Çıkarım',fikir='Bir cümlede açıkça ya da kesin olarak söylenenleri, aşırı genellemeden ayırarak çıkarılabilecek yargıyı bulmak.',tuzak='“Her, yalnızca, hiçbir zaman” gibi sınırı aşan yargıları ya da ters yönlü nedenselliği doğru saymak.',zorluk='kolay',kalip='düz',adim=2,tipId='can-cikarim',kaynak='ÖSYM TYT Türkçe 2018–2026 (cümlede anlam: çıkarım)'),
 'K-CAN-02':dict(alt='Anlamca Özdeş Cümle',fikir='Verilen cümleyle aynı anlama gelen cümleyi; kapsam, olumsuzluk ve mantık ilişkisini koruyarak bulmak.',tuzak='Cümlenin tersini ya da karşıtını aynı anlamda sanmak; “yalnızca” gibi sınırlayıcıları görmemek.',zorluk='orta',kalip='düz',adim=3,tipId='can-anlamdas',kaynak='ÖSYM TYT Türkçe 2018–2026 (cümlede anlam: anlamca yakın cümle)'),
 'K-CAN-03':dict(alt='Neden–Sonuç, Amaç–Sonuç, Koşul',fikir='Cümlelerdeki neden–sonuç, amaç–sonuç ve koşul–sonuç ilişkisini, bağlaç ve ek ipuçlarıyla ayırt etmek.',tuzak='Amaç ile nedeni, koşul ile nedeni birbirine karıştırmak.',zorluk='orta',kalip='düz',adim=3,tipId='can-neden',kaynak='ÖSYM TYT Türkçe 2018–2026 (cümlede anlam: neden-sonuç, amaç-sonuç)'),
 'K-CAN-04':dict(alt='Öznel ve Nesnel Yargı',fikir='Kanıtlanabilir (nesnel) yargıyı, kişiden kişiye değişen (öznel) yargıdan ayırmak.',tuzak='Bilgi gibi görünen ama değer yargısı taşıyan ifadeleri nesnel saymak.',zorluk='orta',kalip='düz',adim=3,tipId='can-yargi',kaynak='ÖSYM TYT Türkçe 2018–2026 (cümlede anlam: öznel-nesnel yargı)'),
}
TIPLER={'can-cikarim':'Cümleden çıkarım','can-anlamdas':'Anlamca özdeş cümle','can-neden':'Neden–sonuç, amaç ve koşul ilişkisi','can-yargi':'Öznel ve nesnel yargı'}
Q=Konu('cumleanlam','Cümlede Anlam','tr|Cümlede Anlam',KARTLAR,TIPLER)
AD=A

B_CIK=B('Çıkarım','cümlede açıkça yazan ya da kesin olarak sonucu çıkan yargı çıkarılabilir. “Her, hiç, yalnızca, tek” gibi sözcüklerle genelleyen şıklar cümleyi aşar. Örnek: “Çoğu öğrenci geldi” cümlesinden “hepsi geldi” çıkmaz')
B_OZD=B('Anlamca özdeş cümle','“yalnızca/ancak” içeren cümle bir koşul bildirir: “Yalnızca A olanlar B’dir” = “B olan herkes A’dır”. Tersi (“A olan herkes B’dir”) aynı anlama gelmez. Örnek: “Yalnızca bilet alanlar girer” = “Girenlerin hepsi bilet almıştır”')
B_NED=B('Neden, amaç, koşul','neden–sonuç: “…-diği için, yüzünden” · amaç–sonuç: “… için, … diye” (sonuçta ulaşılmak istenen şey) · koşul: “…-sa/-se, …-ırsa”. Örnek: “Yağmur yağdığı için ıslandık” neden; “Islanmamak için şemsiye aldık” amaç; “Yağmur yağarsa kalırız” koşul')
B_YARG=B('Nesnel ve öznel yargı','nesnel yargı: ölçülüp doğrulanabilen, kişiye göre değişmeyen yargı (“Su 100 °C’de kaynar”). Öznel yargı: kişinin beğenisine, duygusuna dayanan yargı (“Çay kahveden güzeldir”). “En güzel, bence, harika, ne yazık ki” gibi değer bildiren ifadeler öznelliğe işaret eder')

Q.KADIM={
 '0001':[AD('Kanıtı bul','Cümle, uykusuz öğrencilerin çoğunun sınavda dikkat toplamakta zorlandığını söylüyor.','uykusuzluk → dikkat sorunu'),AD('Çıkarım kuralını uygula','Çıkarım, cümledeki bilginin kesin sonucudur; “her zaman, hiç” gibi aşırı iddialar çıkmaz.','kesin sonuç aranır'),AD('Şıkları ele','Yalnızca E, ekran süresiyle göz yorgunluğu ilişkisinin olabileceğini, kesinlik iddia etmeden söyler.','E: doğru')],
 '0002':[AD('İki durumu ayır','Cümle yeşil alanların artışını ve dışarı çıkmayı birlikte anlatıyor, sonra farkı belirtiyor.','artış → dışarı çıkış (her yerde aynı değil)'),AD('Şıkları cümleyle karşılaştır','A ve D genelleme yapar, B cümlede yok, E cümledeki “aynı ölçüde değil” ifadesine terstir.','A, B, D, E: elendi'),AD('Doğru şıkkı seç','C, yeşil alanın dışarı çıkma eğilimini etkileyebileceğini temkinli söyler.','C: doğru')],
 '0003':[AD('Benzetmeyi çöz','Temel = başlangıç, süslü üst katlar = görünüş; sağlam başlamayanın zarar göreceği anlatılıyor.','temel → başlangıç'),AD('Anlamı sadeleştir','Cümle “temeli sağlam atılmayan işin sonu kötüdür” diyor.','özet'),AD('Şıkları ele','A, C, D ve E yapıdan ya da süslemeden söz ederek benzetmenin gerçek anlamına takılıyor. B özetle aynıdır.','B: doğru')],
 '0004':[AD('Koşulu bul','“Ancak üyeliği olanlar” bir koşuldur: ödünç alma için üyelik şart.','ödünç alma → üyelik'),AD('Mantığı çevir','Şart şu: ödünç alan herkes üyedir.','ödünç alan ⇒ üye'),AD('Şıkları ele','B ve C koşulu ters çevirir, D cümleye zıttır, E cümleyi yok sayar.','B, C, D, E: elendi'),AD('Kontrol et','A’da ödünç alanların hepsinin üyeliği olduğu söyleniyor; bu, cümleyle aynı anlamdır.','A: doğru')],
 '0005':[AD('Bağlaca bak','“-diği için” sözü neden bildirir.','neden bağlacı'),AD('Şıkları tara','Diğer cümlelerde neden–sonuç bağı yok; yalnızca olay, karşıtlık ya da seçenek var.','A, B, C, E: bağ yok'),AD('Sonucu yaz','“Sonuçlar açıklandı → öğrenciler heyecanlıydı” neden–sonuç ilişkisidir.','D: doğru')],
 '0006':[AD('Soruyu çöz','“Koşul” bildiren cümleyi arıyoruz: şart olan bir durum ve onun sonucu.','koşul: “-sa/-se, -ırsa”'),AD('Şıkları ayır','A amaç, B neden, C karşıtlık, D ekleme bildirir.','A, B, C, D: koşul değil'),AD('Doğrula','“Erken yatarsan … uyanırsın”: -sa/-ırsa koşul ekidir ve sonuç koşula bağlıdır.','E: doğru')],
 '0007':[AD('Nesnel yargıyı tanımla','Ölçülüp doğrulanabilen, kişiden kişiye değişmeyen yargı aranıyor.','aranan: doğrulanabilir'),AD('Öznel ifadeleri ele','“En, güzel, ilginç, bence” gibi sözler beğeniyi gösterir.','A, B, D, E: öznel'),AD('Doğrula','“Türkiye’de 81 il vardır” sayılıp doğrulanabilir.','C: nesnel')],
 '0008':[AD('Öznel işaretleri ara','Her cümlede “beğeni, tahmin, övgü, şikâyet” bildiren sözcükleri işaretle.','işaret arama'),AD('Şıkları ele','A, C, D ve E’de “güçlü, en iyi, çok güzel, ne yazık ki” gibi değer bildiren ifadeler var.','A, C, D, E: öznel'),AD('Nesnel olanı seç','B’de film bir festivalde gösterilmiş; bu bilgi doğrulanabilir.','B: nesnel')],
}

# 0001 çıkarım · kolay
Q.ekle('0001','K-CAN-01','kolay','Cümleden kesin olarak çıkarılabilecek yargıyı belirler.','düz',2,
 dict(metin='Sınav öncesi sabaha kadar uyumayan öğrencilerin çoğu, sınav sırasında dikkatini toplamakta zorlanıyor.\nBu cümleden aşağıdakilerden hangisi çıkarılabilir?',
  dogru='Uykusuzluk, dikkat üzerinde olumsuz bir etki yapabilir.',harf='B',
  yan=[('Sınav öncesi uyuyan öğrenciler her zaman başarılı olur.','Cümle uyuyanların başarısından söz etmez; “her zaman” da cümleyi aşan bir genellemedir.','bilgi'),
       ('Öğrenciler sınavdan önce hiç ders çalışmamalıdır.','Cümlede bir öğüt yoktur; yalnızca uykusuzluğun etkisi anlatılır.','dikkat'),
       ('Dikkat sorunu yaşayan öğrenciler sabaha kadar uyumaz.','Nedensellik tersine çevrilmiş: cümlede uykusuzluk dikkat sorununa yol açıyor, tersi söylenmiyor.','bilgi'),
       ('Sınavda zorlanan her öğrenci uykusuz kalmıştır.','Cümle “çoğu” der ve yalnızca uykusuzlardan söz eder; “her” genellemesi cümlede yok.','dikkat')],
  istenen='Cümleden çıkarılabilen yargı.',ip=['Cümlede “çoğu” sözcüğü var; kesin ve genel yargılara dikkat et.','Cümle hangi durumdan hangi sonuca gidiyor?','Yön tersine çevrilmiş şıkları ele.'],
  bilgi=[B_CIK],
  adim=[AD('Kanıtı bul','Cümle, uykusuz öğrencilerin çoğunun sınavda dikkat toplamakta zorlandığını söylüyor.','uykusuzluk → dikkat sorunu'),AD('Çıkarım kuralını uygula','Çıkarım, cümledeki bilginin kesin sonucudur; “her zaman, hiç” gibi aşırı iddialar çıkmaz.','kesin sonuç aranır'),AD('Şıkları ele','A, C ve D cümleyi aşıyor ya da tersine çeviriyor, E öğüt veriyor. B temkinli ve cümleyle uyumlu.','B: doğru')],
  puf='Çıkarım sorularında “her, hiç, yalnızca, kesinlikle” içeren şıkka şüpheyle bak; cümle kadar söyleyen şık doğrudur.'),
 dict(metin='Gün boyu ekran karşısında çalışanların birçoğu akşamları gözlerinde yorgunluk hissediyor.\nBu cümleden aşağıdakilerden hangisi çıkarılabilir?',
  dogru='Uzun süreli ekran kullanımı göz yorgunluğuna yol açabilir.',harf='E',
  yan=[('Gözlük kullanan herkes ekran karşısında çalışır.','Cümlede gözlükten söz edilmez; “herkes” genellemesi de cümleyi aşar.','bilgi'),
       ('Gözlerinde yorgunluk hisseden herkes ekran karşısında çalışır.','Cümle ekranda çalışanlardan yorgunluğa gider; tersi söylenmemiştir.','bilgi'),
       ('Ekran başında çalışmak insanları akşamları evden çıkmaktan alıkoyar.','Cümlede evden çıkmakla ilgili bir bilgi yok.','dikkat'),
       ('Göz yorgunluğunu önlemenin tek yolu ekrandan uzak durmaktır.','Cümle önlemeden söz etmez; “tek yol” ifadesi cümleyi aşar.','dikkat')],
  istenen='Cümleden çıkarılabilen yargı.',ip=['Cümlede “birçoğu” deniyor, “hepsi” denmiyor.','Neden hangisi, sonuç hangisi?','Çözüm önerisi sunan şıklar cümlede dayanak bulur mu?']))

# 0002 çıkarım · orta
Q.ekle('0002','K-CAN-01','orta','Karşıt iki durumu anlatan cümleden çıkarılabilecek yargıyı belirler.','düz',3,
 dict(metin='Çocuk, yaptıklarına güvenilen bir ortamda özgüven kazanırken, sürekli müdahale edilen bir ortamda bu duygusunu yitirmeye başlar.\nBu cümleden aşağıdakilerden hangisi çıkarılabilir?',
  dogru='Çocukların özgüveni, çevrenin tutumuna göre güçlenip zayıflayabilir.',harf='D',
  yan=[('Özgüvenli çocuklar hiçbir zaman müdahaleye ihtiyaç duymaz.','Cümle müdahale ihtiyacından söz etmez; “hiçbir zaman” cümleyi aşar.','bilgi'),
       ('Müdahale edilmeyen çocukların hepsi özgüvenli olur.','Cümle güvenilen ortamdan söz eder, müdahalesiz bırakılan tüm çocuklardan değil; “hepsi” genellemesi cümlede yok.','dikkat'),
       ('Özgüven yalnızca çocukluk döneminde kazanılır.','Cümlede özgüvenin başka dönemlerde kazanılıp kazanılmadığına dair bir bilgi yoktur.','bilgi'),
       ('Çocuklara güvenilmesi, onların hata yapmasını tümüyle engeller.','Cümle hata yapmadan söz etmez; “tümüyle engeller” cümleyi aşar.','dikkat')],
  istenen='Cümleden çıkarılabilen yargı.',ip=['Cümle iki ortamı karşılaştırıyor: biri özgüveni artırıyor, öbürü azaltıyor.','Ortak sonuç: özgüven neye bağlı?','“Hiçbir zaman, hepsi, tümüyle” içeren şıklara dikkat.'],
  bilgi=[B_CIK],
  adim=[AD('İki durumu ayır','Güvenilen ortamda özgüven artıyor, müdahale edilen ortamda azalıyor.','güven → artar · müdahale → azalır'),AD('Ortak sonucu bul','İki durumun ortak noktası: özgüven çevrenin tutumuna göre değişiyor.','özgüven ← çevre tutumu'),AD('Şıkları ele','A, B ve E genelleme yapıyor, C cümlede olmayan bir dönemden söz ediyor. D tam karşılığı veriyor.','D: doğru')],
  puf='Karşıt iki durum varsa çıkarım çoğu zaman ikisinin ortak sonucudur.'),
 dict(metin='Bir şehirde yeşil alanlar çoğaldıkça insanlar daha sık dışarı çıkıyor; ancak bu durum her mahallede aynı ölçüde görülmüyor.\nBu cümleden aşağıdakilerden hangisi çıkarılabilir?',
  dogru='Yeşil alanların artması, insanların dışarıda vakit geçirme eğilimini etkileyebilir.',harf='C',
  yan=[('Dışarı çıkan her insan yeşil alanları tercih eder.','Cümle yeşil alanın dışarı çıkışa etkisinden söz eder; dışarı çıkan herkesin yeşil alanı seçtiği söylenmez.','bilgi'),
       ('Yeşil alanlar yalnızca bazı mahallelerde bulunur.','Cümle farkın mahalleler arasında davranışta olduğunu söyler; yeşil alanın yalnız bazılarında bulunduğunu söylemez.','dikkat'),
       ('Mahalleler arasındaki fark, yeşil alan miktarından kaynaklanır.','Cümle farkın nedenini söylemez; nedeni yeşil alan miktarına bağlamak cümleyi aşar.','bilgi'),
       ('Yeşil alanların artması her mahallede insanları dışarı çıkarmıştır.','Cümledeki “her mahallede aynı ölçüde görülmüyor” sözüne terstir.','dikkat')],
  istenen='Cümleden çıkarılabilen yargı.',ip=['Cümle iki bölümden oluşuyor: genel bir eğilim ve bir sınırlama.','“Ancak” sonrası, genellemeyi sınırlıyor.','Her mahalle için kesin hüküm veren şıklar cümleye uymaz.']))

# 0003 anlamdaş · orta
Q.ekle('0003','K-CAN-02','orta','Benzetmeli bir cümleyle anlamca özdeş cümleyi belirler.','düz',3,
 dict(metin='Bir sorunun nedenini bilmeden ona çözüm aramak, hastalığı tanımadan ilaç vermeye benzer.\nBu cümleyle anlamca en yakın cümle aşağıdakilerden hangisidir?',
  dogru='Sorunu doğru teşhis etmeden bulunan çözüm, çoğu zaman sonuç vermez.',harf='A',
  yan=[('Her sorunun çözümü, nedenini bilen kişide bulunur.','Cümle “her” sorun için kesin bir hüküm vermez; asıl vurgu nedeni bilmeden çözüm aramanın sakıncasıdır.','bilgi'),
       ('İlaçlar, hastalığı tanımadan da iyileştirici olabilir.','Cümlenin söylediğinin tersini söyler: tanımadan verilen ilaç iyi gelir diyor.','bilgi'),
       ('Sorun çözmek isteyenler önce hastalıkları öğrenmelidir.','Hastalık benzetmenin bir parçasıdır; şık benzetmeyi gerçek anlamıyla almıştır.','dikkat'),
       ('Çözümü zor olan sorunlarda uzman desteği alınmalıdır.','Cümle uzman desteğinden söz etmez; konudan sapar.','dikkat')],
  istenen='Verilen cümleyle anlamca en yakın cümle.',ip=['Benzetmenin karşılıklarını bul: sorun = hastalık, çözüm = ilaç.','Nedeni bilmemek, hastalığı tanımamak demek.','Benzetmeyi sade bir dille yeniden yaz.'],
  bilgi=[B_OZD],
  adim=[AD('Benzetmeyi çöz','Sorun hastalığa, çözüm ilaca, nedeni bilmemek hastalığı tanımamaya karşılık gelir.','sorun = hastalık · çözüm = ilaç'),AD('Sadeleştir','Cümle, sorunu doğru tanımadan bulunan çözümün işe yaramayacağını söylüyor.','özet: teşhissiz çözüm işe yaramaz'),AD('Şıkları ele','B anlamı tersine çevirir, C benzetmeyi düz anlamıyla alır, D ve E konudan sapar. A özetle aynıdır.','A: doğru')],
  puf='Benzetmeli cümlelerde önce karşılıkları (sorun = hastalık gibi) eşle, sonra sade biçimde özetle.'),
 dict(metin='Bir işin temelini sağlam atmayanlar, üst katları ne kadar süslese de sonunda zararı görür.\nBu cümleyle anlamca en yakın cümle aşağıdakilerden hangisidir?',
  dogru='Başlangıcı sağlam olmayan bir işin sonu iyi bitmez.',harf='B',
  yan=[('Sağlam temelli işlerin üst katları süslenmemelidir.','Süslemenin yasaklanması cümlede yok; temelin önemi vurgulanıyor.','dikkat'),
       ('Her bina, temeli kadar süslü olmalıdır.','Cümle binadan ve süsten söz eden bir benzetmedir; şık benzetmeyi gerçek anlamıyla almıştır.','dikkat'),
       ('Yapı işlerinde zarar görmemek için üst katlar çok yüksek yapılmamalıdır.','Yükseklikten söz edilmiyor; benzetme gerçek anlamıyla alınmış.','bilgi'),
       ('Süslü işler her zaman temelsizdir.','Cümle böyle bir genelleme yapmaz; temelsiz işin süsle kurtarılamayacağını söyler.','bilgi')],
  istenen='Verilen cümleyle anlamca en yakın cümle.',ip=['Temel neyin, üst katlar neyin karşılığı?','Cümlenin ana yargısı: başlangıç kötüyse sonuç ne olur?','Gerçek bina bilgisi veren şıkları ele.']))

# 0004 anlamdaş · zor
Q.ekle('0004','K-CAN-02','zor','“Yalnızca/ancak” sınırlayıcılı cümlenin mantıksal karşılığını belirler.','düz',4,
 dict(metin='Yalnızca düzenli çalışanlar sınavda başarılı olur.\nBu cümleyle anlamca aynı olan cümle aşağıdakilerden hangisidir?',
  dogru='Sınavda başarılı olan herkes düzenli çalışmıştır.',harf='E',
  yan=[('Düzenli çalışan herkes sınavda başarılı olur.','Cümle düzenli çalışmayı başarı için şart koşar, yeterli saymaz; şık şartı sonuca çevirmiştir.','bilgi'),
       ('Düzenli çalışmayan bazı kişiler de sınavda başarılı olur.','Cümlenin “yalnızca” sözüne terstir.','bilgi'),
       ('Sınavda başarısız olan herkes düzenli çalışmamıştır.','Cümle başarısızların durumunu söylemez; bu yargı cümlenin tersidir, eşi değildir.','dikkat'),
       ('Düzenli çalışmanın sınav başarısı üzerinde etkisi yoktur.','Cümle düzenli çalışmayı şart koşar; etkisiz demek cümleye terstir.','bilgi')],
  istenen='Verilen cümleyle anlamca aynı olan cümle.',ip=['“Yalnızca düzenli çalışanlar” ifadesi, çalışmayı bir şart yapar.','Başarılı olanların hepsi hakkında ne söyleyebilirsin?','Şartı sonuç yapan (tersine çeviren) şıkları ele.'],
  bilgi=[B_OZD],
  adim=[AD('Şartı belirle','“Yalnızca … olanlar” demek, başarılı olmak için düzenli çalışmanın şart olduğunu gösterir.','başarı ⇒ düzenli çalışma'),AD('Mantığı çevir','Başarılı olan herkes düzenli çalışmıştır.','başarılı ⇒ çalışmış'),AD('Şıkları ele','A ve C şartı tersine çeviriyor, B ve D cümleye zıt. E aynı anlamı veriyor.','A, B, C, D: elendi'),AD('Kontrol et','E’de başarılıların hepsinin düzenli çalıştığı söyleniyor; verilen cümleyle aynı.','E: doğru')],
  puf='“Yalnızca A olanlar B’dir” cümlesi “B olan herkes A’dır” demektir; “A olan herkes B’dir” demek değildir.'),
 dict(metin='Ancak üyeliği olanlar kütüphaneden kitap ödünç alabilir.\nBu cümleyle anlamca aynı olan cümle aşağıdakilerden hangisidir?',
  dogru='Kütüphaneden kitap ödünç alan herkesin üyeliği vardır.',harf='A',
  yan=[('Üyeliği olan herkes kütüphaneden kitap ödünç alır.','Cümle üyeliği şart koşar; üye olan herkesin kitap aldığını söylemez.','bilgi'),
       ('Kitap ödünç almayanların hiçbirinin üyeliği yoktur.','Cümle üyeliği olup kitap almayanlara dair bir şey söylemez; şık şartı tersine çevirmiştir.','dikkat'),
       ('Üyeliği olmayan bazı kişiler de kitap ödünç alabilir.','Cümlenin “ancak” sözüne terstir.','bilgi'),
       ('Kütüphane üyeliği kitap ödünç almak için gerekli değildir.','Cümle üyeliği şart koşar; şık bunu yadsıyor.','bilgi')],
  istenen='Verilen cümleyle anlamca aynı olan cümle.',ip=['“Ancak” sözü hangi şartı koyuyor?','Ödünç alan herkes hakkında ne söylenebilir?','Şartı sonuç gibi sunan şıkları ele.']))

# 0005 neden-sonuç · kolay
Q.ekle('0005','K-CAN-03','kolay','Cümlelerdeki neden–sonuç ilişkisini ayırt eder.','düz',2,
 dict(metin='Aşağıdaki cümlelerin hangisinde neden–sonuç ilişkisi vardır?',
  dogru='Yol çalışması yüzünden otobüsler başka bir güzergâhtan gidiyor.',harf='C',
  yan=[('Çocuk, oyuncağını arkadaşıyla paylaştı.','Yalnızca bir eylem anlatılıyor; neden–sonuç bağı yok.','dikkat'),
       ('Yağmuru sevmiyor ama yağmurun sesini dinlemekten hoşlanıyor.','“Ama” karşıtlık bildirir; neden–sonuç bildirmez.','bilgi'),
       ('Sınıfın bir köşesinde eski bir harita asılıydı.','Durum betimlemesidir; neden–sonuç yok.','dikkat'),
       ('Sabahları ya çay içer ya da kahve.','“Ya … ya da” seçenek bildirir.','bilgi')],
  istenen='Neden–sonuç ilişkisi bulunan cümle.',ip=['Neden–sonuç ilişkisinde bir olay, bir başka olayın sebebidir.','“Yüzünden, için, çünkü” gibi sözcükler ipucudur.','Karşıtlık ve seçenek bildiren bağlaçları ele.'],
  bilgi=[B_NED],
  adim=[AD('Bağlaçları ara','“Yüzünden”, “-diği için”, “çünkü” gibi sözler neden bildirir.','neden bağlaçları'),AD('Şıkları tara','A olay, B karşıtlık, D betimleme, E seçenek bildiriyor.','A, B, D, E: bağ yok'),AD('Sonucu yaz','“Yol çalışması → otobüsler başka güzergâhtan gidiyor” bir neden–sonuç ilişkisi.','C: doğru')],
  puf='“Yüzünden, -diği için, çünkü, bu nedenle” gördüğünde neden–sonuç ilişkisini ara.'),
 dict(metin='Aşağıdakilerden hangisinde bir olay, ötekinin nedeni olarak gösterilmiştir?',
  dogru='Sonuçlar açıklandığı için öğrenciler heyecanlıydı.',harf='D',
  yan=[('Bahçedeki ağaçlar ilkbaharda çiçek açar.','Genel bir doğa bilgisidir; neden–sonuç bağı yok.','dikkat'),
       ('Hem koşmayı hem yüzmeyi seviyor.','“Hem … hem” ekleme bildirir.','bilgi'),
       ('Misafirler gelmeden önce salonu topladı.','Zaman ilişkisi var; neden–sonuç ilişkisi yok.','dikkat'),
       ('İstersen yarın da gelebilirsin.','Koşul/öneri bildirir; olaylar arasında neden bağı yok.','bilgi')],
  istenen='Neden–sonuç ilişkisi bulunan cümle.',ip=['Bir olay diğerini hangi cümlede doğuruyor?','“-diği için” gibi ekli bağlaçları ara.','Zaman, ekleme ve öneri bildiren cümleleri ele.']))

# 0006 amaç/koşul · orta
Q.ekle('0006','K-CAN-03','orta','Amaç–sonuç ilişkisini neden–sonuç, koşul ve karşıtlıktan ayırır.','düz',3,
 dict(metin='Aşağıdaki cümlelerin hangisinde amaç–sonuç ilişkisi vardır?',
  dogru='Sağlıklı kalmak için her sabah yürüyüşe çıkıyor.',harf='B',
  yan=[('Yağmur bastırdığı için maç ertelendi.','Bu cümlede maçın ertelenmesinin nedeni verilmiş; amaç değil, neden–sonuç vardır.','bilgi'),
       ('Hava açılırsa pikniğe gideceğiz.','“-ırsa” ekiyle koşul bildirilmiş; amaç yok.','bilgi'),
       ('Bu kitabı hem okudum hem de not aldım.','“Hem … hem de” ekleme bildirir.','dikkat'),
       ('Sınavı kazanamadı, fakat vazgeçmedi.','“Fakat” karşıtlık bildirir.','dikkat')],
  istenen='Amaç–sonuç ilişkisi bulunan cümle.',ip=['Amaç, yapılan işin ulaşmak istediği sonuçtur: “… için” ve geleceğe dönük bir istek.','Geçmişteki bir olayın sebebini veren cümle amaç değildir.','Koşul bildiren “-sa/-se” ekli şıkları ele.'],
  bilgi=[B_NED],
  adim=[AD('Amacı tanımla','Amaç, bir işin yapılma gerekçesi olan istenen sonuçtur: “sağlıklı kalmak için yürümek”.','iş → ulaşılmak istenen sonuç'),AD('Şıkları ayır','A neden, C koşul, D ekleme, E karşıtlık bildirir.','A, C, D, E: amaç değil'),AD('Doğrula','“Sağlıklı kalmak için yürüyüşe çıkıyor”: yürüyüşün amacı sağlıklı kalmak.','B: doğru')],
  puf='“İçin” hem neden hem amaç bildirir: geçmişte olmuş bir olaydan sonra gelirse neden, yapılacak bir iş için ulaşılmak istenen şeyi bildirirse amaçtır.'),
 dict(metin='Aşağıdaki cümlelerin hangisinde koşul–sonuç ilişkisi vardır?',
  dogru='Erken yatarsan yarın dinç uyanırsın.',harf='E',
  yan=[('Dinç uyanmak için erken yatıyor.','Bu cümle amaç–sonuç bildirir.','bilgi'),
       ('Geç yattığı için sabah zor uyandı.','Geçmiş bir olayın nedeni verilmiştir; neden–sonuç.','bilgi'),
       ('Erken yattı ama uykusu gelmedi.','“Ama” karşıtlık bildirir.','dikkat'),
       ('Çocuklar hem yedi hem içti.','“Hem … hem” ekleme bildirir.','dikkat')],
  istenen='Koşul–sonuç ilişkisi bulunan cümle.',ip=['Koşul ilişkisi “-sa/-se, -ırsa” ekleriyle kurulur.','Sonuç koşulun gerçekleşmesine bağlıdır.','Amaç ve neden bildiren cümleleri ele.']))

# 0007 yargı · orta
Q.ekle('0007','K-CAN-04','orta','Nesnel yargı taşıyan cümleyi öznel yargıdan ayırır.','düz',3,
 dict(metin='Aşağıdaki cümlelerin hangisinde nesnel bir yargı vardır?',
  dogru='Su, deniz seviyesinde 100 derecede kaynar.',harf='D',
  yan=[('Bu kentin en güzel mevsimi şüphesiz ilkbahardır.','“En güzel” bir beğeni bildirir; kişiden kişiye değişir.','bilgi'),
       ('Ankara’daki bu müze, ülkenin en ilginç müzesidir.','“En ilginç” kişisel bir değerlendirmedir.','bilgi'),
       ('Bence kısa filmler uzun filmlerden daha etkileyicidir.','“Bence” kişisel görüşü gösterir.','dikkat'),
       ('Deniz kenarında yaşamak insanı mutlu eder.','Mutluluk kişiye göre değişir; doğrulanabilir bir ölçüt yok.','dikkat')],
  istenen='Nesnel yargı taşıyan cümle.',ip=['Nesnel yargı ölçülebilir ve herkes için aynıdır.','“En güzel, bence, ilginç” gibi değer bildiren sözler öznelliğe işaret eder.','Bilimsel bir olguyu anlatan cümleyi ara.'],
  bilgi=[B_YARG],
  adim=[AD('Nesnel yargıyı tanımla','Ölçülüp doğrulanabilen, kişiden kişiye değişmeyen yargı aranıyor.','aranan: doğrulanabilir'),AD('Öznel ifadeleri ele','“En güzel, en ilginç, bence, mutlu eder” beğeni ve kanaat bildirir.','A, B, C, E: öznel'),AD('Doğrula','Suyun kaynama noktası ölçülerek doğrulanabilir.','D: nesnel')],
  puf='Ölçüp deneyle doğrulayabiliyorsan nesnel; “bence, en güzel” diye başlayıp bitiyorsa öznel.'),
 dict(metin='Aşağıdakilerden hangisi, herkesin aynı biçimde doğrulayabileceği bir bilgi bildirmektedir?',
  dogru='Türkiye’de 81 il vardır.',harf='C',
  yan=[('Bu şehrin pazarları ülkenin en renkli pazarlarıdır.','“En renkli” kişisel bir değerlendirmedir.','bilgi'),
       ('Kış, yılın en kasvetli mevsimidir.','“Kasvetli” duygusal bir yargıdır.','bilgi'),
       ('Bence yaz tatili bir hafta daha uzun olmalı.','“Bence” kişisel görüşü ve istek gösterir.','dikkat'),
       ('Bu şarkı, son yılların en iyi şarkısıdır.','“En iyi” kişisel beğeni bildirir.','dikkat')],
  istenen='Nesnel yargı taşıyan cümle.',ip=['Hangi cümleyi sayarak ya da ölçerek doğrulayabilirsin?','Beğeni bildiren sözleri ele.','“En” içeren şıklar çoğu zaman öznel yargı taşır.']))

# 0008 yargı · zor
Q.ekle('0008','K-CAN-04','zor','Bilgi görünümlü öznel ifadeleri ayıklayarak nesnel yargıyı bulur.','düz',4,
 dict(metin='Bir kitap tanıtım yazısındaki cümlelerden hangisi, kişisel değerlendirme katmadan doğrulanabilir bir bilgi vermektedir?',
  dogru='Kitap, yayımlandığı yıl satış listelerine girdi.',harf='A',
  yan=[('Ne yazık ki kitabın sonu beklediğimden zayıf.','“Ne yazık ki” ve “beklediğimden zayıf” kişisel değerlendirmedir.','bilgi'),
       ('Roman, sade diliyle okuru kolayca içine çekiyor.','“Kolayca içine çekiyor” kişiden kişiye değişen bir izlenimdir.','dikkat'),
       ('Yazarın bu kitabı, bütün eserlerinin zirvesidir.','“Zirve” bir değer yargısıdır; ölçüsü yoktur.','dikkat'),
       ('Kapak tasarımı kitabın havasını çok güzel yansıtıyor.','“Çok güzel” beğeni bildirir.','bilgi')],
  istenen='Nesnel yargı taşıyan cümle.',ip=['Beş cümlenin dördü bir duygu ya da değerlendirme taşıyor.','Satış listesine girip girmediği bir kayıttan kontrol edilebilir mi?','“Ne yazık ki, zirve, çok güzel” gibi sözcükleri işaretle.'],
  bilgi=[B_YARG],
  adim=[AD('Öznel işaretleri ara','Her cümlede beğeni, şikâyet ve övgü bildiren sözcükleri işaretle.','işaret arama'),AD('Şıkları ele','B, C, D ve E’de “ne yazık ki, kolayca içine çekiyor, zirvesidir, çok güzel” gibi değer bildiren ifadeler var.','B, C, D, E: öznel'),AD('Nesnel olanı seç','A’da kitap bir listeye girmiş; bu kayıtlardan doğrulanabilir.','A: nesnel')],
  puf='Edebî ya da bilimsel görünümlü cümlelerde de değer sözcüğü (zirve, çok güzel, ne yazık ki) varsa yargı öznel olur.'),
 dict(metin='Bir film eleştirisinden alınan aşağıdaki cümlelerden hangisi yazarın duygusunu değil, doğrulanabilir bir durumu bildirmektedir?',
  dogru='Film, uluslararası bir festivalde gösterime girdi.',harf='B',
  yan=[('Oyuncuların performansı filmin en büyük gücü.','“En büyük güç” bir değerlendirmedir.','bilgi'),
       ('Müzikler, sahnelerin havasını harika yansıtıyor.','“Harika” beğeni bildirir.','bilgi'),
       ('Bu film, yönetmenin kuşkusuz en iyi işi.','“Kuşkusuz en iyi” bir görüştür.','dikkat'),
       ('Son sahne, izleyicide unutulmaz bir etki bırakıyor.','“Unutulmaz etki” kişiye göre değişir.','dikkat')],
  istenen='Nesnel yargı taşıyan cümle.',ip=['Festivale girip girmediği kayıtlardan kontrol edilebilir.','Beğeni ve övgü bildiren sözleri ele.','Dört cümlede de bir duygu ya da değerlendirme var.']))

Q.bitir()
