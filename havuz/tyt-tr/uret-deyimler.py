"""TYT Türkçe · Deyimler ve Atasözleri: 4 ana + 4 kardeş. Yalnızca MEB kitaplarında yaygın bilinen deyim ve atasözleri kullanılmıştır."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from tr_ortak import *
AD=A
KARTLAR={
 'K-DYM-01':dict(alt='Deyimin Anlamı ve Kullanımı',fikir='Bir deyimin cümlede anlamına uygun kullanılıp kullanılmadığını belirlemek.',tuzak='Deyimi sözcük sözcük (düz anlamıyla) yorumlamak; benzer görünen deyimleri karıştırmak.',zorluk='kolay',kalip='düz',adim=2,tipId='dey-deyim',kaynak='ÖSYM TYT Türkçe 2018–2026 (deyimler)'),
 'K-DYM-02':dict(alt='Atasözünün Anlamı ve Kullanımı',fikir='Atasözünün özünü, benzetmeleri çözerek bulmak ve cümle ya da durumla eşleştirmek.',tuzak='Atasözünü düz anlamıyla yorumlamak; benzer konulu atasözlerini karıştırmak.',zorluk='orta',kalip='düz',adim=3,tipId='dey-atasozu',kaynak='ÖSYM TYT Türkçe 2018–2026 (atasözleri)'),
}
TIPLER={'dey-deyim':'Deyimin anlamı ve kullanımı','dey-atasozu':'Atasözünün anlamı ve kullanımı'}
Q=Konu('deyimler','Deyimler ve Atasözleri','tr|Deyimler ve Atasözleri',KARTLAR,TIPLER)
B_D=B('Deyim','birkaç sözcüğün birleşerek gerçek anlamından ayrı, kalıplaşmış bir anlam kazanmasıdır. Örnek: “yüreği ağzına gelmek” = çok korkmak, “göz yummak” = görmezden gelmek, “ayağı yere değmemek” = çok sevinmek')
B_D2=B('Deyimin cümlede kullanımı','deyim cümlenin anlamına uymalıdır. Örnek: “Haberi alınca ayağı yere değmedi” doğru (sevinç); “Haberi alınca ayağı yere değmedi, hüzünden ağladı” uyumsuz')
B_A=B('Atasözü','uzun deneylere dayanan, öğüt veren, kalıplaşmış sözlerdir. Çoğu benzetmelidir; özü bulunur. Örnek: “Ağaç yaş iken eğilir” = alışkanlıklar küçükken kazanılır')
B_A2=B('Atasözü – cümle eşlemesi','atasözünü sadeleştirip özünü yaz, sonra şıklardaki durumun aynı özü taşıyıp taşımadığına bak. Örnek: “Üzüm üzüme baka baka kararır” = kişi çevresinden etkilenir')
Q.KADIM={
 '0001':[AD('Deyimin anlamını hatırla','“Göz yummak”, bir yanlışı görmezden gelmektir.','göz yummak = görmezden gelmek'),AD('Cümleleri sına','A, C, D ve E’de deyimler anlamlarına ters ya da uyumsuz kullanılmış.','A, C, D, E: uyumsuz'),AD('Uygun olanı seç','B’de yöneticinin yanlışlarını görmezden gelmesi ve tepki toplaması anlamlı.','B: doğru')],
 '0002':[AD('Anlamı belirle','“Çok sevinmek” anlamına gelen deyimi arıyoruz.','aranan: çok sevinmek'),AD('Deyimlerin anlamlarını yaz','Boynu bükük: üzgün · bir kulağından girip öbüründen çıkmak: önemsememek · kolları sıvamak: işe girişmek · gözünü budaktan esirgememek: yiğit davranmak.','B, C, D, E: sevinç değil'),AD('Doğru olanı seç','“Ayakları yere değmemek” çok sevinmektir.','A: doğru')],
 '0003':[AD('Atasözünü sadeleştir','“Üzüm üzüme baka baka kararır”: kişi çevresindekilere bakarak onlar gibi olur.','özü: çevre etkiler'),AD('Şıkları ele','A üzüm rengine, B, C ve D aşırı ya da konu dışı yargılara gidiyor.','A, B, C, D: elendi'),AD('Doğrula','E, kişinin çevresindekilerden etkilendiğini söylüyor; atasözünün özüdür.','E: doğru')],
 '0004':[AD('Yargıyı çöz','Hedef: bugünkü ihtiyaçlarla birlikte gelecek için birikim yapmak.','özü: biriktirmek'),AD('Atasözlerini yorumla','I: kara gün için para ayır. II: ileride lazım olur diye sakla. III: acele iş bozar, tasarrufla ilgisi yok.','I, II: birikim · III: acele'),AD('Şıkları ele','III’ü içeren şıklar elenir; “Yalnız I” ise II’yi dışarıda bırakır.','B: I ve II')],
}
Q.ekle('0001','K-DYM-01','kolay','Deyimin cümlede anlamına uygun kullanıldığı örneği belirler.','düz',2,
 dict(metin='Hangi cümlede tırnak içine alınan deyim, kendi anlamına yakışacak biçimde kullanılmıştır?',
  dogru='Çocuk, karanlık odada tek başına kalınca “yüreği ağzına geldi”.',harf='D',
  yan=[('Haberi duyunca “ağzı kulaklarına vardı”, hemen ağlamaya başladı.','“Ağzı kulaklarına varmak” çok sevinmek demektir; ağlamayla çelişir.','bilgi'),
       ('Kardeşi “eli açık” biri olduğu için her kuruşunu sayar.','“Eli açık” cömert demektir; her kuruşu saymakla çelişir.','bilgi'),
       ('Doktorun uyarılarına “kulak asıp” ilaçlarını hiç içmedi.','“Kulak asmak” dinlemek, önemsemek demektir; ilaçları hiç içmemek bununla çelişir.','dikkat'),
       ('Aldığı hediyeye “içi içine sığmadı”, hiç heyecanlanmadı.','“İçi içine sığmamak” çok heyecanlanmak demektir; heyecanlanmamakla çelişir.','bilgi')],
  istenen='Deyimin doğru kullanıldığı cümle.',ip=['Her deyimin anlamını yaz: yüreği ağzına gelmek, ağzı kulaklarına varmak, eli açık, kulak asmak, içi içine sığmamak.','Cümlenin geri kalanı deyimin anlamıyla uyuşuyor mu?','Çelişkili cümleleri tek tek ele.'],
  bilgi=[B_D,B_D2],
  adim=[AD('Deyimlerin anlamını yaz','Yüreği ağzına gelmek: çok korkmak · ağzı kulaklarına varmak: çok sevinmek · eli açık: cömert · kulak asmak: dinlemek, önemsemek · içi içine sığmamak: çok heyecanlanmak.','anlamlar listelendi'),AD('Cümleleri sına','A, B, C ve E’de deyimin anlamı cümlenin geri kalanıyla çelişiyor.','A, B, C, E: uyumsuz'),AD('Uygun olanı seç','D’de karanlıkta yalnız kalan çocuğun korkması anlamlıdır.','D: doğru')],
  puf='Deyim sorularında deyimin anlamını sözcüğün yerine koyup cümleyi yeniden oku; çelişki çıkıyorsa yanlıştır.'),
 dict(metin='Aşağıdakilerin hangisinde tırnak içindeki deyim anlamına uygun kullanılmıştır?',
  dogru='Yönetici yanlışlara “göz yumduğu” için tepki gördü.',harf='B',
  yan=[('Sınavdan düşük not alınca “başı göğe erdi”.','“Başı göğe ermek” çok sevinmek demektir; düşük notla çelişir.','bilgi'),
       ('Cevap “dilinin ucundaydı”, hemen söyleyiverdi.','“Dilinin ucunda olmak” bildiği hâlde tam hatırlayamamak demektir; hemen söylemekle çelişir.','bilgi'),
       ('Kitabı “baştan savma” okuyup her ayrıntıyı hatırladı.','“Baştan savma” özensiz demektir; ayrıntıları hatırlamakla çelişir.','dikkat'),
       ('Çok “gözü pek” olduğundan hiçbir şeyi göze alamıyordu.','“Gözü pek” korkusuz demektir; göze alamamakla çelişir.','dikkat')],
  istenen='Deyimin doğru kullanıldığı cümle.',ip=['Deyimlerin anlamlarını tek tek yaz.','Cümlenin geri kalanı deyimin anlamıyla çelişiyor mu?','Çelişen dört cümleyi ele.']))
Q.ekle('0002','K-DYM-01','orta','Anlamı verilen deyimin geçtiği cümleyi bulur.','düz',3,
 dict(metin='Aşağıdaki cümlelerin hangisinde tırnak içindeki deyim, “kibirli olmak” anlamında kullanılmıştır?',
  dogru='Terfi aldıktan sonra “burnu havada” biri oldu.',harf='E',
  yan=[('Haberi alınca “ayağı yere değmedi”.','“Ayağı yere değmemek” çok sevinmek demektir.','bilgi'),
       ('İşin başında “kollarını sıvadı”.','“Kollarını sıvamak” işe girişmek demektir.','bilgi'),
       ('Yan odadan gelen sesleri duymak için “kulak kabarttı”.','“Kulak kabartmak” dikkatle dinlemek demektir; kibir bildirmez.','dikkat'),
       ('Sözlerimi bir kulağından alıp öbüründen çıkardı.','Bu deyim önemsememek demektir; kibir bildirmez.','dikkat')],
  istenen='“Kibirli olmak” anlamındaki deyim.',ip=['Her şıktaki deyimin anlamını yaz.','Hangi deyim bir kişinin başkalarını küçümsemesini anlatıyor?','Sevinç, işe girişmek ve önemsememek anlamındakileri ele.'],
  bilgi=[B_D],
  adim=[AD('Aranan anlamı belirle','“Kibirli olmak” anlamı aranıyor.','aranan: kibir'),AD('Deyimlerin anlamlarını yaz','Ayağı yere değmemek: sevinmek · kollarını sıvamak: işe girişmek · kulak kabartmak: dikkatle dinlemek · bir kulağından alıp öbüründen çıkarmak: önemsememek.','A, B, D: farklı'),AD('Eşleştir','“Burnu havada olmak”, kendini başkalarından üstün görüp kibirli davranmaktır.','E: doğru')],
  puf='Deyimin anlamını ezberden bilmiyorsan, cümlenin geri kalanına bakıp en uygun duyguyu sına.'),
 dict(metin='Aşağıdakilerden hangisinde tırnak içindeki deyim, “çok sevinmek” anlamında kullanılmıştır?',
  dogru='Müjdeyi alınca “ayakları yere değmedi”.',harf='A',
  yan=[('Sınav sonucunu duyunca “boynu bükük” kaldı.','“Boynu bükük” üzgün, çaresiz demektir.','bilgi'),
       ('Ağabeyim, sözlerimi “bir kulağından alıp öbüründen çıkardı”.','Bu deyim önemsememek demektir.','bilgi'),
       ('Kapıdan girer girmez “kollarını sıvadı”.','“Kollarını sıvamak” işe girişmek demektir.','dikkat'),
       ('Rakibin gücünü bilmeden “gözünü budaktan esirgemedi”.','Bu deyim, tehlikeyi göze almak demektir.','dikkat')],
  istenen='“Çok sevinmek” anlamındaki deyim.',ip=['Her deyimin anlamını yaz.','Hangi deyim bir haberden duyulan coşkuyu anlatıyor?','Üzüntü, önemsememek ve cesaret anlatanları ele.']))
Q.ekle('0003','K-DYM-02','orta','Atasözünün anlamına uygun cümleyi belirler.','düz',3,
 dict(metin='“Ağaç yaş iken eğilir.” atasözüyle anlamca örtüşen cümle aşağıdakilerden hangisidir?',
  dogru='Eğitime erken başlamak gerekir; alışkanlıklar küçükken kazanılır.',harf='A',
  yan=[('Ağaçlar eğildikçe zamanla daha sağlam ve dayanıklı büyür.','Atasözünün düz anlamına takılmıştır; ağaç bir benzetmedir.','bilgi'),
       ('Yaşlı ağaçların meyveleri, genç ağaçlarınkinden daha tatlı olur.','Konu dışıdır; atasözü meyve tadından söz etmez.','dikkat'),
       ('Büyükler, çocukların tüm davranışlarından sorumlu tutulamaz.','Atasözünün özüyle bağdaşmaz; büyüklerin yönlendirme sorumluluğunu yok sayar.','bilgi'),
       ('Eğitim, kişi yaşlandıkça çok daha kolay ve verimli hâle gelir.','Atasözünün tersini söyler: genç yaşta eğitim daha kolaydır.','bilgi')],
  istenen='Atasözüyle anlamca örtüşen cümle.',ip=['“Yaş” ağaç taze, genç ağaçtır; “eğilir” biçim verilir demek.','Atasözü hangi yaşta eğitimin daha kolay olduğunu söylüyor?','Düz anlama gidenleri ele.'],
  bilgi=[B_A,B_A2],
  adim=[AD('Atasözünü sadeleştir','Genç ağaç kolay eğilir; insan da küçükken kolay biçim alır.','özü: erken eğitim'),AD('Şıkları ele','B ve C düz anlama, D tersine, E sorumluluk konusuna gidiyor.','B, C, D, E: elendi'),AD('Doğrula','A, alışkanlıkların çocuklukta kazanıldığını ve eğitime erken başlanması gerektiğini söylüyor.','A: doğru')],
  puf='Atasözünün benzetmesini (ağaç = insan, eğilmek = biçim almak) çöz; sonra özünü şıklarda ara.'),
 dict(metin='“Üzüm üzüme baka baka kararır.” atasözüyle anlamca örtüşen cümle aşağıdakilerden hangisidir?',
  dogru='Kişi, çevresindeki insanlardan etkilenir.',harf='E',
  yan=[('Üzümler güneşi gördükçe zamanla kararır.','Atasözünün düz anlamına takılmıştır.','bilgi'),
       ('Her insan çevresiyle aynı düşünceyi taşır.','Atasözü etkilenmeyi söyler, “aynı düşünce” genellemesi yapmaz.','dikkat'),
       ('Çevresinden uzak yaşayanlar daha mutludur.','Atasözünde mutluluk konusu yoktur.','dikkat'),
       ('Bağ işleri çevresel koşullara bağlıdır.','Düz anlama gidilmiş, konu dışı bir yargıdır.','bilgi')],
  istenen='Atasözüyle anlamca örtüşen cümle.',ip=['Üzümün üzüme bakması neyin benzetmesi?','Karaması neyi anlatıyor?','Düz anlama giden şıkları ele.']))
Q.ekle('0004','K-DYM-02','zor','Üç atasözü arasından verilen yargıyla bağdaşanları belirler.','öncüllü',4,
 dict(metin='I. Gülü seven dikenine katlanır.\nII. Taşıma su ile değirmen dönmez.\nIII. Bir elin nesi var, iki elin sesi var.\nYukarıdaki atasözlerinden hangileri “Bir işi başarmak isteyen kişi, işin zorluklarına katlanmalıdır.” yargısıyla anlamca bağdaşır?',
  dogru='Yalnız I',harf='C',
  yan=[('Yalnız II','“Taşıma su ile değirmen dönmez” kalıcı kaynağı olmayan işin yürümeyeceğini söyler; zorluğa katlanmayla ilgili değildir.','bilgi'),
       ('Yalnız III','“Bir elin nesi var, iki elin sesi var” iş birliğini öğütler; zorluğa katlanmaktan söz etmez.','bilgi'),
       ('I ve III','III iş birliğini anlatır; verilen yargıyla bağdaşmaz.','dikkat'),
       ('II ve III','Her ikisi de verilen yargıdan farklı konular anlatır.','dikkat')],
  istenen='Verilen yargıyla bağdaşan atasözleri.',ip=['Her atasözünün özünü kısaca yaz: gül–diken, taşıma su, iki el.','Hangisi sevdiği şeyin zorluklarını göze almayı anlatıyor?','Yargıyla çakışmayan atasözlerini ele.'],
  bilgi=[B_A,B_A2],
  adim=[AD('Yargıyı çöz','Başarmak isteyen zorluğa katlanmalı.','yargı: zorluğa katlanmak'),AD('Atasözlerini yorumla','I: sevdiğin şeyin zorluğunu göze al. II: kalıcı kaynak olmadan iş yürümez. III: iş birliği güçtür.','I ✓ · II, III ✗'),AD('Şıkları ele','II veya III’ü içeren şıklar elenir; yalnız I kalır.','C: doğru')],
  puf='Öncüllü atasözü sorularında her öncülün özünü tek cümleyle yaz, sonra verilen yargıyla yan yana koy.'),
 dict(metin='I. Ak akçe kara gün içindir.\nII. Sakla samanı, gelir zamanı.\nIII. Acele işe şeytan karışır.\nYukarıdaki atasözlerinden hangileri “Bugünkü ihtiyaçlarını karşılarken yarının ihtiyaçları için de birikim yapmak gerekir.” yargısıyla anlamca bağdaşır?',
  dogru='I ve II',harf='B',
  yan=[('Yalnız I','II de ileride gerekecek şeyi saklamayı öğütler.','dikkat'),('I ve III','III acele etmenin zararını anlatır; birikimle ilgisi yoktur.','bilgi'),('II ve III','III acelenin zararını anlatır; birikimle ilgisi yoktur.','bilgi'),('I, II ve III','III birikimden değil, acele etmekten söz eder.','bilgi')],
  istenen='Verilen yargıyla bağdaşan atasözleri.',ip=['Her atasözünün özünü yaz: kara gün, saman, acele.','Hangileri gelecek için bir şey ayırmayı öğütlüyor?','Acele ile ilgili olanı ele.']))
Q.bitir()
