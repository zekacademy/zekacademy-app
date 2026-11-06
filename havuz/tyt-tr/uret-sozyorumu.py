"""TYT Türkçe · Söz Yorumu: 4 ana + 4 kardeş. Sözler özgündür."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from tr_ortak import *
AD=A
KARTLAR={
 'K-SYO-01':dict(alt='Sözün Anlamı',fikir='Benzetme ve kinaye içeren bir sözün gerçek anlamını bırakıp asıl vermek istediği düşünceyi bulmak.',tuzak='Sözü sözcüğü sözcüğüne alıp somut bir bilgi gibi yorumlamak; sözde olmayan bir öğüt eklemek.',zorluk='kolay',kalip='düz',adim=2,tipId='soz-anlam',kaynak='ÖSYM TYT Türkçe 2018–2026 (söz yorumu: sözün anlamı)'),
 'K-SYO-02':dict(alt='Sözler Arası Anlam Yakınlığı',fikir='Verilen sözlerin ya da bir sözle başka bir ifadenin aynı düşünceyi taşıyıp taşımadığını belirlemek.',tuzak='Ortak sözcüğe ya da konuya bakıp düşüncenin yönünü atlamak.',zorluk='orta',kalip='öncüllü',adim=3,tipId='soz-iliski',kaynak='ÖSYM TYT Türkçe 2018–2026 (söz yorumu: sözlerin ilişkisi)'),
}
TIPLER={'soz-anlam':'Sözün anlamı','soz-iliski':'Sözler arası anlam yakınlığı'}
Q=Konu('sozyorumu','Söz Yorumu','tr|Söz Yorumu',KARTLAR,TIPLER)
B_SY=B('Söz yorumu','önce benzetmeleri gerçek anlamlarından ayır, sonra sözün ders vermek istediği düşünceyi bul. Örnek: “Su akar, yolunu bulur” = engellere rağmen çare bulunur')
B_SY2=B('Aşırı ve eksik yorum','şık sözde bulunmayan bir öğüt (“her zaman”, “yalnızca”) ekliyorsa ya da sözü düz anlamıyla yorumluyorsa yanlıştır')
B_YK=B('Anlam yakınlığı','iki söz aynı sonucu aynı gerekçeyle söylüyorsa anlamca yakındır. Örnek: “Acele işe şeytan karışır” ile “Telaşla yapılan iş bozulur” yakındır; “Hızlı çalışan erken bitirir” ise tersidir')
Q.KADIM={
 '0001':[AD('Benzetmeyi çöz','Çiçek = emek verilen şey, koku = sonuçtur; su vermek emek vermektir.','su vermek = emek'),AD('Sözü sadeleştir','Emek vermeyen, sonuçtan yakınmamalı demek istiyor.','özet: emek ver, sonra bekle'),AD('Şıkları ele','B ve E sözün düz anlamına, C aşırı genellemeye, D konudan sapmaya takılıyor. A özetle aynıdır.','A: doğru')],
 '0002':[AD('Benzetmeleri eşle','Fırtına = zorluk, yelkenler = araçlar, rota = izlenen yol.','fırtına → zorluk · rota → yol'),AD('Mesajı çıkar','Zorluktan sonra yalnızca araçlara bakmak yetmez; gidilen yön de değerlendirilmeli.','özet'),AD('Şıkları ele','A ve D sözün düz anlamına, B ters anlama, E sözde olmayan karamsarlığa gidiyor. C asıl düşünceyi veriyor.','C: doğru')],
 '0003':[AD('Sözün özünü çıkar','Ufka kilitlenen kişi önündeki engeli fark etmez; hedefe odaklanırken ayak altı unutulur.','hedef odağı → engeli görmez'),AD('Şıkları karşılaştır','B ve D sözün düz anlamına, C aşırı genellemeye, E sözde olmayan sonuca gidiyor.','B, C, D, E: elendi'),AD('Doğrula','A, hedefe kilitlenen kişinin engelleri fark edemeyebileceğini söylüyor; sözün özüdür.','A: doğru')],
 '0004':[AD('Sözleri ayrı ayrı yorumla','I ve II başkasını eleştirmeden önce kendine bakmayı öğütler; III herkesin görevini yerine getirmesini söyler.','I, II: öz eleştiri · III: sorumluluk'),AD('Yakın olanları eşle','I ve II aynı düşünceyi aynı yönde söylüyor; III farklı.','I ≈ II'),AD('Şıkları ele','Yalnız I, yalnız III, II ve III ve üçü birden hatalı. “I ve II” doğru.','D: doğru')],
}
Q.ekle('0001','K-SYO-01','kolay','Benzetmeli bir sözün asıl anlamını belirler.','düz',2,
 dict(metin='Kapıyı açık tutan, yalnızca misafirini değil, fırsatı da karşılar.\nBu sözle anlatılmak istenen aşağıdakilerden hangisidir?',
  dogru='Çevresine açık olan kişi, yeni imkânlarla da karşılaşır.',harf='C',
  yan=[('Misafir ağırlamak en büyük erdemdir.','Söz misafiri bir benzetme olarak kullanır; misafir ağırlamanın erdem olduğunu söylemez.','dikkat'),
       ('Evin kapısı gece gündüz açık bırakılmalıdır.','Sözün düz anlamına takılmıştır; “kapı” açıklığı bir tutumu anlatır.','bilgi'),
       ('Fırsatlar yalnızca misafirlerle gelir.','Söz “yalnızca” demiyor; misafir de benzetmedir.','dikkat'),
       ('Kapalı kapılar her zaman güvenlik sağlar.','Söz kapalılığı değil açıklığı över; sözde böyle bir yargı yoktur.','bilgi')],
  istenen='Sözün asıl anlamı.',ip=['“Kapı” ve “misafir” sözcüklerini gerçek anlamlarıyla alma.','Kapıyı açık tutmak hangi tutumu anlatıyor?','Misafirle birlikte “fırsat” da karşılanıyor: neyin bir sonucu?'],
  bilgi=[B_SY,B_SY2],
  adim=[AD('Benzetmeyi çöz','Kapıyı açık tutmak, yeniliğe ve çevreye açık olmak demektir; misafir de gelen imkândır.','kapı = açıklık'),AD('Mesajı çıkar','Açık olan hem insanları hem fırsatları karşılar.','açık olan kazanır'),AD('Şıkları ele','A, B ve D sözü düz anlamıyla alıyor, E sözde olmayan bir yargı ekliyor. C asıl düşünceyi veriyor.','C: doğru')],
  puf='Söz yorumlarında önce benzetmeleri açıkla, sonra tek cümleyle özetle.'),
 dict(metin='Çiçeğe su vermeyen, kokusundan yakınmamalı.\nBu sözle anlatılmak istenen aşağıdakilerden hangisidir?',
  dogru='Emek vermeden güzel bir sonuç beklenmemelidir.',harf='D',
  yan=[('Çiçeklerin kokusu sulamaya bağlıdır.','Sözün düz anlamına takılmıştır; çiçek bir benzetmedir.','bilgi'),
       ('Yakınan herkes çiçek yetiştirmelidir.','Söz herkese yönelik böyle bir öğüt vermiyor; aşırı bir yargıdır.','dikkat'),
       ('Kokusuz çiçekler değersizdir.','Sözde çiçeklerin değeri konusu yoktur.','dikkat'),
       ('Bahçe işleri herkese göre değildir.','Sözün konusu bahçe işleri değil, emek ve sonuç ilişkisidir.','dikkat')],
  istenen='Sözün asıl anlamı.',ip=['Su vermek ve koku sözcükleri neyi temsil ediyor?','Sözün asıl öğüdü nedir?','Sözü gerçek bahçıvanlıkla sınırlayan şıkları ele.']))
Q.ekle('0002','K-SYO-01','orta','Birden çok benzetme içeren sözün anlamını belirler.','düz',3,
 dict(metin='Yükünü hafifletmek isteyen, önce taşıdıklarının hepsinin kendisine ait olup olmadığına bakmalıdır.\nBu sözle anlatılmak istenen aşağıdakilerden hangisidir?',
  dogru='Kişi, kendisine ait olmayan sorumlulukları ve kaygıları sırtlanmaktan kaçınmalıdır.',harf='A',
  yan=[('Yükü olan kişi her zaman başkalarından yardım istemelidir.','Söz yardım istemekten söz etmez; “her zaman” ifadesi de aşırıdır.','dikkat'),
       ('Taşınan her yük, kişinin kendi hatasının sonucudur.','Sözde yükün hatadan kaynaklandığına dair bir yargı yoktur.','bilgi'),
       ('Hafifletmek yerine yükü artırmak gerekir.','Sözün tersini söyler.','bilgi'),
       ('Taşıma işlerinde ağırlık önceden hesaplanmalıdır.','Sözün düz anlamına takılmıştır; yük bir benzetmedir.','bilgi')],
  istenen='Sözün asıl anlamı.',ip=['“Yük” burada somut bir ağırlık mı?','“Kendisine ait olup olmadığı” hangi tavsiyeyi hazırlıyor?','Yükü sorumluluk ve kaygı olarak oku.'],
  bilgi=[B_SY,B_SY2],
  adim=[AD('Benzetmeleri eşle','Yük = sorumluluk ve kaygılar; hafifletmek = rahatlamak.','yük → sorumluluk'),AD('Koşula bak','“Kendisine ait olup olmadığına bakmalı”: önce neyin kendi payına düştüğü ayrılmalı.','ayır: kendinin / başkasının'),AD('Şıkları ele','B sözde olmayan bir neden ekliyor, C ters, D düz anlama, E yardıma kayıyor. A özdür.','A: doğru')],
  puf='“Önce … bakmalı” biçimindeki sözler genellikle bir ön ayrım ya da kontrol öğütler.'),
 dict(metin='Her fırtınadan sonra yelkeni değil, rotayı gözden geçirmek gerekir.\nBu sözle anlatılmak istenen aşağıdakilerden hangisidir?',
  dogru='Zor bir dönemden sonra yapılması gereken, yalnızca araçları değil izlenen yolu da yeniden değerlendirmektir.',harf='C',
  yan=[('Fırtınalı havada denize açılmamalıdır.','Söz denize açılmayı yasaklamaz; fırtına bir benzetmedir.','bilgi'),
       ('Yelkenlerin bakımı, rotayı belirlemekten önemlidir.','Söz yelkeni değil rotayı öne çıkarır.','bilgi'),
       ('Zor zamanlarda pes etmek en doğru karardır.','Sözde pes etmek öğütlenmez; yön değerlendirmesi öğütlenir.','dikkat'),
       ('Rotası değişmeyen kişiler hiç fırtınaya yakalanmaz.','Söz fırtınaya yakalanmamaktan söz etmez.','dikkat')],
  istenen='Sözün asıl anlamı.',ip=['Fırtına, yelken ve rota neyi temsil ediyor?','Sözde hangisi gözden geçirilmeli, hangisi değil?','Düz anlama gidenleri ele.']))
Q.ekle('0003','K-SYO-02','orta','Verilen sözle aynı düşünceyi taşıyan ifadeyi belirler.','düz',3,
 dict(metin='Küçük adımları küçümseyen, uzun yolu tamamlayamaz.\nAşağıdakilerden hangisi bu sözle anlamca en yakındır?',
  dogru='Büyük başarılar, küçük çabaların birikmesiyle ortaya çıkar.',harf='E',
  yan=[('Uzun yolculuklarda hızlı yürümek başarıyı belirler.','Sözün konusu hız değil, küçük adımların değeridir.','dikkat'),
       ('Küçük adımlar attığı için başarısız olanlar çoktur.','Sözün tersini söyler.','bilgi'),
       ('Uzun yolculuklar yalnızca iyi hazırlananlar tarafından tamamlanır.','Hazırlık söz konusu değildir; “yalnızca” da aşırıdır.','dikkat'),
       ('Adımlarını sıklaştıran kişi hedefe daha çabuk ulaşır.','Söz hız artırmayı değil, küçük adımları önemsemeyi söyler.','dikkat')],
  istenen='Sözle anlamca en yakın ifade.',ip=['“Küçük adımlar” neyin benzetmesi?','Söz, küçük adımları küçümsemenin sonucunu anlatıyor.','Küçük çabaların toplamını öne çıkaran şıkkı ara.'],
  bilgi=[B_YK],
  adim=[AD('Sözü yorumla','Küçük adımlar = küçük çabalar; uzun yol = büyük hedef.','küçük çaba → büyük hedef'),AD('Mesajı çıkar','Küçük çabalar önemsenmezse büyük hedefe varılamaz.','küçük çaba gereklidir'),AD('Şıkları ele','A hıza, B ters anlama, C hazırlığa, D hız artırmaya kayıyor. E birikimi öne çıkarıyor.','E: doğru')],
  puf='Yakın anlam sorularında sözün gerekçesini ve sonucunu şıkta aynı yönde arayın.'),
 dict(metin='Gözünü ufka diken, ayağının altındaki çukuru görmez.\nAşağıdakilerden hangisi bu sözle anlamca en yakındır?',
  dogru='Büyük hedefe kilitlenen kişi, önündeki küçük engelleri fark etmeyebilir.',harf='A',
  yan=[('Hedefi olmayan kişi hiçbir engelle karşılaşmaz.','Sözde hedefsiz kişiden söz edilmez; “hiçbir” genellemesi de aşırıdır.','dikkat'),
       ('Ufuk, yalnızca uzun yola çıkanlara görünür.','Sözün düz anlamına takılmıştır.','bilgi'),
       ('Yüksek hedefi olanlar çukurlara hiç düşmez.','Sözün tersidir.','bilgi'),
       ('Engelleri gören herkes hedefe ulaşır.','Sözde böyle bir sonuç yoktur.','dikkat')],
  istenen='Sözle anlamca en yakın ifade.',ip=['Ufuk ne, çukur ne demek?','Gözünü ufka dikmek hangi tutumu anlatıyor?','Sözün sonucu: nelerden habersiz kalırsın?']))
Q.ekle('0004','K-SYO-02','zor','Üç söz arasından anlamca yakın olanları belirler.','öncüllü',4,
 dict(metin='I. Aceleyle atılan adım, çoğu zaman geri dönüşü zor bir yola sokar.\nII. Acele işe şeytan karışır.\nIII. Hızlı çalışan, işini daha erken bitirir.\nYukarıdaki sözlerden hangileri anlamca birbirine yakındır?',
  dogru='I ve II',harf='B',
  yan=[('Yalnız II','I da aynı düşüncededir: acele, kötü sonuç getirir.','dikkat'),('I ve III','III hızı över, I ise acelenin zararını anlatır; yönleri zıttır.','bilgi'),('II ve III','III hızı över, II acelenin zararını anlatır; yönleri zıttır.','bilgi'),('I, II ve III','III’ün hızı olumlu görmesi, I ve II’nin acele karşıtı tutumuyla çelişir.','bilgi')],
  istenen='Anlamca yakın sözler.',ip=['Her sözün hız ve acele hakkında hangi yargıyı taşıdığını yaz.','Hızı öven söz hangisi, acelenin zararını söyleyenler hangileri?','Zıt yargı taşıyan sözü eleyince ne kalıyor?'],
  bilgi=[B_YK],
  adim=[AD('Sözleri yorumla','I: acele geri dönüşü zor sonuç doğurur. II: acele işi bozar. III: hızlı çalışmak işi erken bitirir.','I, II: acele kötü · III: hız iyi'),AD('Yönleri karşılaştır','I ve II acelenin zararını söylüyor; III hızı olumlu gösteriyor.','I ≈ II · III zıt'),AD('Şıkları ele','III’ü içeren şıklar elenir; “Yalnız II” ise I’i dışarıda bırakır.','B: doğru')],
  puf='Öncüllü yakınlık sorularında önce her öncülün yönünü (olumlu/olumsuz) yaz, sonra aynı yönde olanları eşle.'),
 dict(metin='I. Başkasının kusurunu sayan, kendi eksiğini görmez.\nII. Aynaya bakmadan başkasının yüzündeki lekeyi gösterme.\nIII. Herkes kendi payına düşeni yapmalıdır.\nYukarıdaki sözlerden hangileri anlamca birbirine yakındır?',
  dogru='I ve II',harf='D',
  yan=[('Yalnız I','II de aynı düşünceyi, öz eleştirisiz başkasını eleştirmemeyi söyler.','dikkat'),('Yalnız III','III sorumluluğu anlatır; I ve II ile aynı konuda değildir.','bilgi'),('II ve III','III öz eleştiriyi değil görev paylaşımını anlatır; II ile yakın değildir.','bilgi'),('I, II ve III','III farklı bir düşünce taşır: herkes kendi görevini yapmalıdır.','bilgi')],
  istenen='Anlamca yakın sözler.',ip=['Üç sözün ne öğütlediğini kısaca yaz.','Hangi iki söz, başkasını eleştirmeden önce kendine bakmayı öğütlüyor?','Üçüncü söz hangi konuda?']))
Q.bitir()
