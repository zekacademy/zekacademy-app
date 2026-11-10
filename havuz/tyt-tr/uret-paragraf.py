"""TYT Türkçe · Paragraf: 12 ana + 12 kardeş. Metinler özgündür. Sıralama sorularının cevabı kodla türetilir."""
import sys,os,random
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from tr_ortak import *

KARTLAR={
 'K-PRG-01':dict(alt='Ana Düşünce',fikir='Parçanın tümüne yayılan asıl mesajı, ayrıntı ve örnekten ayırarak bulmak.',tuzak='Bir ayrıntıyı ana düşünce sanmak; parçada olmayan ya da parçaya ters bir genellemeyi seçmek.',zorluk='kolay',kalip='düz',adim=2,tipId='prg-ana',kaynak='ÖSYM TYT Türkçe 2018–2026 (paragrafta anlam: ana düşünce)'),
 'K-PRG-02':dict(alt='Yardımcı Düşünce ve Çıkarım',fikir='Parçada açıkça verilen ya da parçadan kesin olarak çıkarılabilen yargıyı, çıkarılamayan yargıdan ayırmak.',tuzak='Aşırı genelleme (her, hiç, tümüyle) içeren ya da parçada geçmeyen yargıyı doğru saymak; olumsuz kökü kaçırmak.',zorluk='orta',kalip='düz',adim=3,tipId='prg-yardimci',kaynak='ÖSYM TYT Türkçe 2018–2026 (paragrafta anlam: değinilmeyen / çıkarılamayan)'),
 'K-PRG-03':dict(alt='Paragraf Tamamlama',fikir='Boşluğun önündeki ve arkasındaki cümlelerin bağlaçlarına ve anlam akışına bakarak boşluğa gelecek cümleyi bulmak.',tuzak='Konuya uygun görünen ama akışı tersine çeviren ya da bağlaçla çelişen cümleyi seçmek.',zorluk='zor',kalip='düz',adim=4,tipId='prg-tamamlama',kaynak='ÖSYM TYT Türkçe 2018–2026 (paragrafın yapısı: tamamlama)'),
 'K-PRG-04':dict(alt='Cümle Sıralama',fikir='Zamirler, bağlaçlar ve sıralama sözcükleriyle numaralı cümleleri anlamlı bir bütün oluşturacak biçimde dizmek.',tuzak='Genel görünen cümleyi hemen başa koymak; bağlaç ve gönderme ilişkisini atlamak.',zorluk='orta',kalip='öncüllü',adim=4,tipId='prg-siralama',kaynak='ÖSYM TYT Türkçe 2018–2026 (paragrafın yapısı: cümle sıralama)'),
 'K-PRG-05':dict(alt='Akışı Bozan Cümle',fikir='Parçanın odağını belirleyip bu odağa hizmet etmeyen cümleyi bulmak.',tuzak='Konuyla aynı sözcükleri taşıyan ama farklı bir yönü anlatan cümleyi parçaya uygun sanmak.',zorluk='orta',kalip='öncüllü',adim=3,tipId='prg-akis',kaynak='ÖSYM TYT Türkçe 2018–2026 (paragrafın yapısı: akışı bozan cümle)'),
 'K-PRG-06':dict(alt='Anlatım Biçimleri ve Düşünceyi Geliştirme Yolları',fikir='Parçada kullanılan anlatım biçimini ya da düşünceyi geliştirme yolunu (örnekleme, benzetme, karşılaştırma vb.) tanımak.',tuzak='Benzer terimleri karıştırmak; metinde olmayan bir yöntemi var saymak.',zorluk='orta',kalip='düz',adim=3,tipId='prg-anlatim',kaynak='ÖSYM TYT Türkçe 2018–2026 (paragrafta anlatım teknikleri)'),
}
TIPLER={'prg-ana':'Ana düşünce','prg-yardimci':'Yardımcı düşünce ve çıkarım','prg-tamamlama':'Paragraf tamamlama','prg-siralama':'Cümle sıralama','prg-akis':'Akışı bozan cümle','prg-anlatim':'Anlatım biçimleri ve düşünceyi geliştirme yolları'}
Q=Konu('paragraf','Paragraf','tr|Paragraf',KARTLAR,TIPLER)

B_ANA=B('Ana düşünce','parçanın tümüne yayılan, yazarın asıl vermek istediği mesajdır. Örnek: “Düzenli çalışan başarır.” Ayrıntı ve örnekler ana düşünceyi destekler, onun yerine geçmez')
B_ANA2=B('Parçaya ters ya da parçada olmayan yargı','şık ana düşünce olacaksa parçadaki bilgilerle çelişmemeli ve parçanın tamamını kapsamalıdır. Örnek: parça “spor sağlığı korur” diyorsa “spor zararlıdır” yanlış, “herkes sporcu olmalıdır” parçada yok')
B_YARD=B('Yardımcı düşünce','ana düşünceyi açıklayan ayrıntılardır; parçada açıkça yazılanlar ya da kesin olarak çıkarılanlar yardımcı düşüncedir. Örnek: “Su hayat kaynağıdır; bitkiler susuz kurur.”')
B_KOK=B('Olumsuz soru kökü','“değinilmemiştir”, “çıkarılamaz”, “söylenemez” köklerinde doğru şık parçaya uymayan şıktır; diğer dört şıkkın her biri parçada bulunur')
B_TAM=B('Paragraf tamamlama','boşluğun öncesi ve sonrası okunur; bağlaçlar (ama, oysa, ne var ki, bu yüzden) akışın yönünü gösterir. Örnek: “Ama” ile başlayan cümle öncekine karşıt bir düşünce getirir')
B_SIRA=B('Cümle sıralama ipuçları','zamir (bu, onlar), bağlaç (çünkü, ancak, böylece) ve “önce, sonra” gibi sözcükler cümlenin yerini belirler. Örnek: “Bu yüzden …” cümlesi, nedeni anlatan cümleden sonra gelir')
B_AKIS=B('Akışı bozan cümle','parçanın odağını (neyi, hangi yönden anlattığını) belirle; konuya uygun görünse de bu odaktan sapan cümle akışı bozar. Örnek: “Spor sağlığı korur” parçasında spor ayakkabı fiyatı akışı bozar')
B_ANL=B('Anlatım biçimleri','betimleme: görünüşü sözcüklerle resmetmek · öyküleme: olayları zaman akışıyla anlatmak · açıklama: bilgi vermek · tartışma: bir görüşü savunmak. Örnek: “Kapı gıcırdayarak açıldı” öyküleyicidir')
B_GEL=B('Düşünceyi geliştirme yolları','tanımlama (“X, … olan şeydir”), örnekleme (“örneğin”), karşılaştırma (iki durumu yan yana koymak), benzetme (“… gibi”), tanık gösterme (başkasının sözüne başvurma), neden–sonuç kurma')

def AD(b,a,i): return A(b,a,i)


Q.KADIM={
 '0001':[AD('Parçayı özetle','Takım sporu çocuğa paylaşmayı ve kaybetmeyi öğretiyor.','spor → paylaşma, birlik'),AD('Son cümleye bak','“Bu alışkanlık yalnızca sahada kalmaz” sözü asıl sonucu verir: etki günlük yaşama yayılır.','sonuç: günlük yaşama yansıma'),AD('Şıkları ele','A parçaya ters, B ve C ayrıntı, E nedenselliği tersine çevirmiş.','A, B, C, E: elendi · D: doğru')],
 '0002':[AD('Karşıtlığı gör','“Oysa” ile parça, geçerli sorunun aslında yanlış kurulduğunu söyler.','önce soru bulmak → oysa soru sormak'),AD('Gerekçeye bak','Soruyu daraltma, varsayımları açma ve yön verme sıralanır; bunlar gerekçedir.','gerekçe: iyi soru düşünceyi yönlendirir'),AD('Kanıta bak','Büyük keşiflerin yeni sorulardan doğduğu söylenir; bu iddiayı destekler.','kanıt: bilim tarihi'),AD('Şıkları ele','A ve B’de aşırı ya da ters anlam var, C ayrıntı, D parçada yok. E asıl iddiadır.','E: doğru')],
 '0003':[AD('Kökü doğru oku','Parçada olmayan bilgiyi arıyoruz.','aranan: olmayan'),AD('Şıkları parçada ara','Ortam, su depolama, diken işlevi ve çiçek açma parçada geçiyor.','B, C, D, E: var'),AD('Geriye kalanı seç','Köklerden hiç söz edilmemiş.','A: yok → cevap')],
 '0004':[AD('Kökü doğru oku','Çıkarılamayan yargıyı arıyoruz; dört şık parçadan çıkar.','aranan: çıkarılamayan'),AD('Her şıkkı eşle','A: ilk cümle · B: ikinci cümle · D: üçüncü cümle · E: son cümle.','A, B, D, E: karşılığı var'),AD('Aşırı iddiayı yakala','“Yerini almalıdır” ve “her koşulda” ifadesi parçada yok; parça dengeli bir değerlendirme yapıyor.','C: çıkmaz → cevap')],
 '0005':[AD('Öncesini oku','Bir kentin tarihî dokusunu korumak, binaları “dondurmak” olarak tanımlanmıyor.','dondurmak ✗'),AD('Sonrasını oku','“Binalar kullanıldıkça yaşar” diyor; demek ki boşlukta kullanım önerilmeli.','boşluk → kullanım'),AD('Şıkları sına','A ilk cümleyle çelişir; C ve D konudan sapar; E akışı koparır. B hem “dondurmak değil”e karşılık verir hem sonraki cümleyi hazırlar.','B: doğru')],
 '0006':[AD('Öncesine bak','Hız eskiden günler alan haberi saniyelere indirdi; bu bir kolaylık.','hız → kolaylık'),AD('Bağlacı yorumla','“Ne var ki” kolaylığın karşısına bir sakınca koyacağını bildirir.','boşluk: olumsuz yön'),AD('Şıkları sına','A ve D kolaylığı sürdürür, B ve C parçadaki durumla çelişir.','A, B, C, D: elendi'),AD('Doğrula','E hızın sakıncasını (doğrulamaya zaman kalmaması) söyler.','E: doğru')],
 '0007':[AD('Girişi bul','Zamir ve bağlaç taşımayan, konuyu tanıtan cümle başa gelir.','başlangıç belli'),AD('Bağlantıları kur','“Kabuk çatladığında”, “Kök … tutunduktan sonra”, “Bu yapraklar” ifadeleri cümleleri zincirler.','zamir/bağlaç zinciri'),AD('Doğru sırayı yaz','Ekrandaki numaralarla sırayı kur.','sıra kuruldu'),AD('Soruyu yanıtla','Sondan ikinci cümlenin numarasını bul.','cevap: işaretli numara')],
 '0008':[AD('Girişi seç','Bağlaçsız, konuyu başlatan cümle başa gelir.','giriş belli'),AD('Bağlaçları sırala','“Bunun yerine, çünkü, bu deneyim, kısacası” sırayı belirler; “kısacası” sondadır.','bağlaç zinciri'),AD('Zinciri yaz','Numaralarla doğru sırayı kur.','sıra kuruldu'),AD('İstenen sırayı bul','Sondan ikinci cümlenin numarası cevaptır.','cevap: işaretli numara')],
 '0009':[AD('Odağı bul','Parça, ev bütçesinin nasıl yapıldığını anlatıyor.','odak: bütçe yapma'),AD('Cümleleri sına','I tanımlar, II ve III adımları sıralar, V sonucu söyler.','I, II, III, V: odakta'),AD('Sapmayı yakala','IV. cümle mağazaların yerinden söz eder; bütçeyle ilgisi yoktur.','IV: cevap')],
 '0010':[AD('Odağı bul','Parça, iyi bir dinlemenin nasıl olduğunu anlatıyor.','odak: iyi dinleme'),AD('Cümleleri sına','I dinlemeyi tanımlar, II ve IV dinleyicinin davranışlarını sayar, V sonuç çıkarır.','I, II, IV, V: odakta'),AD('İnce sapmayı yakala','III. cümle konuşmayla ilgilidir, dinlemeyle değil.','III: cevap')],
 '0011':[AD('Fiillere bak','“Çıktı, gördü, indi, attı” fiilleri sırayla bir olayı anlatıyor.','olay akışı var'),AD('Betimleme var mı?','Bir şeyin görünüşü uzun uzun resmedilmiyor.','betimleme ✗'),AD('Biçimi adlandır','Olayları zaman sırasıyla aktarmak öykülemedir.','cevap: öyküleyici')],
 '0012':[AD('Kökü doğru oku','“Başvurulmamıştır” diyor; parçada olmayanı arıyoruz.','aranan: olmayan'),AD('İşaretlerle eşle','“Kuraklık, … kalmasıdır” tanımlama · “yağışlı …, kurak …” karşılaştırma · “Örneğin” örnekleme · “Bu nedenle” neden–sonuç.','B, C, D, E: var'),AD('Geriye kalanı seç','Parçada “gibi, sanki” yoktur; hiçbir şey başka bir şeye benzetilmemiştir.','A: yok → cevap')],
}

# ---------- 0001 ana düşünce · kolay
Q.ekle('0001','K-PRG-01','kolay','Paragrafın ana düşüncesini belirler.','düz',2,
 dict(metin='Kitap okumayı alışkanlık hâline getirmiş insanlar, bir sorunla karşılaştıklarında çözüm yolunu çoğunlukla satırların arasında ararlar. Okudukları her yeni kitap onlara başka bir hayatı, başka bir bakış açısını tanıtır. Böylece kendi dar dünyalarının dışına çıkmayı öğrenirler. Bu yüzden düzenli okuyan biri yalnızca bilgi biriktirmekle kalmaz; karşısındakini anlama gücünü de geliştirir.\nBu parçanın ana düşüncesi aşağıdakilerden hangisidir?',
  dogru='Düzenli okumak, bilgiyi ve anlama gücünü geliştirir.',harf='C',
  yan=[('Bir sorunla karşılaşan herkes çözümü kitaplarda aramalıdır.','Parçada çözümün satırlar arasında aranması yalnızca bir ayrıntıdır ve “herkes” genellemesi parçada yoktur.','bilgi'),
       ('Her kitap, okuyucusuna farklı bir bakış açısı kazandırır.','Bu yargı parçada geçer ama ayrıntıdır; parçanın tamamını kapsayan sonuç son cümledeki “bilgi ve anlama gücü”dür.','dikkat'),
       ('İnsanlar kitabı yalnızca bilgi biriktirmek için okur.','Son cümle tam tersini söyler: okuyan kişi “yalnızca bilgi biriktirmekle kalmaz”.','bilgi'),
       ('Dar bir dünyada yaşayan insanlar kitap okumaya yönelmez.','Parça kitap okumanın dar dünyadan çıkardığını söyler; nedensellik ters çevrilmiş ve parçada bu yargı yok.','dikkat')],
  istenen='Parçanın asıl mesajı.',ip=['Son cümledeki “Bu yüzden” ifadesi sonucu verir; ona dikkat et.','Her şık parçada geçiyor mu, yoksa parçanın tamamını mı özetliyor?','Ayrıntıyı veren şıkkı ele; tümünü kapsayan şıkkı seç.'],
  bilgi=[B_ANA],
  adim=[AD('Parçayı özetle','Okuyan insan başka hayatlar tanır, dar dünyasından çıkar.','kitap → bakış açısı → anlayış'),AD('Sonuç cümlesine bak','“Bu yüzden” ile başlayan son cümle asıl sonucu söyler: bilgi ve anlama gücü artar.','sonuç: bilgi + anlama gücü'),AD('Şıkları ele','A ve B ayrıntı ya da genelleme, D parçada yok, E parçaya ters.','A: ayrıntı · B: ayrıntı · D: yok · E: ters · C: doğru')],
  puf='“Bu yüzden, dolayısıyla, sonuç olarak” ile başlayan cümle çoğu zaman ana düşüncenin habercisidir.'),
 dict(metin='Takım sporuyla uğraşan çocuklar, topu arkadaşına vermeyi, kazanmak kadar kaybetmeyi de öğrenir. Maçta herkesin ayrı bir görevi olduğunu kavrayan çocuk, başarının tek kişiyle değil birlikte çalışarak geldiğini fark eder. Bu alışkanlık yalnızca sahada kalmaz; sınıfta, evde ve arkadaş ortamında da kendini gösterir.\nBu parçanın ana düşüncesi aşağıdakilerden hangisidir?',
  dogru='Takım sporları, çocukların günlük yaşamını da olumlu etkiler.',harf='D',
  yan=[('Çocukların başarısı yalnızca bireysel yeteneklerine bağlıdır.','Parça başarının “tek kişiyle değil birlikte çalışarak” geldiğini söyler; şık parçaya terstir.','bilgi'),
       ('Kaybetmeyi öğrenmek, kazanmayı öğrenmekten daha önemlidir.','Parça iki durumu karşılaştırıp üstünlük vermez; “kazanmak kadar” der.','dikkat'),
       ('Maçta her oyuncunun ayrı bir görevi vardır.','Parçada geçen bir ayrıntıdır; parçanın tamamının vermek istediği sonuç değildir.','dikkat'),
       ('Sınıfta ve evde başarılı olan çocuklar takım sporlarına yönelir.','Parça sporun etkisini anlatır; şık nedensellik yönünü tersine çevirmiştir.','bilgi')],
  istenen='Parçanın asıl mesajı.',ip=['Parça önce sahadaki kazanımı, sonra sahanın dışındaki yansımayı anlatıyor.','Ayrıntı cümlelerini ele; hepsini çatan fikri ara.','Neden–sonuç yönü ters çevrilmiş şıklara dikkat et.']))

# ---------- 0002 ana düşünce · orta
Q.ekle('0002','K-PRG-01','orta','Karşıtlık içeren paragrafın ana düşüncesini belirler.','düz',3,
 dict(metin='Sanat eserine bakarken çoğumuz önce “Bu ne anlatıyor?” diye sorarız. Oysa bir resmin ya da müzik parçasının tek bir doğru anlamı yoktur. Aynı tablo, birinde çocukluğunun bir yazını, ötekinde yeni bir kaygıyı canlandırabilir. Eser, sanatçının elinden çıktığında tamamlanmış sayılmaz; her izleyici ona kendi yaşantısıyla yeni bir katman ekler.\nBu parçanın ana düşüncesi aşağıdakilerden hangisidir?',
  dogru='Bir sanat eseri, izleyenlerin yaşantılarına göre farklı anlamlar kazanır.',harf='A',
  yan=[('Sanatçılar, eserlerinin tek bir anlam taşımasını amaçlamalıdır.','Parça “tek bir doğru anlamı yoktur” der; şık parçaya terstir.','bilgi'),
       ('Sanat eserine bakan kişi önce eserin ne anlattığını sormalıdır.','“Çoğumuz sorarız” bir tespittir, öğüt değildir; “Oysa” ile bu bakış eleştirilir.','dikkat'),
       ('Çocukluk anıları, sanat eserlerinin en önemli ilham kaynağıdır.','Çocukluk anısı yalnızca bir örnektir; ilham kaynağı konusu parçada yoktur.','bilgi'),
       ('Sanat eseri, sanatçının elinden çıktığı anda tamamlanmış olur.','Parça “tamamlanmış sayılmaz” der; şık parçaya terstir.','dikkat')],
  istenen='Parçanın asıl mesajı.',ip=['“Oysa” sözcüğü, öncesindeki düşüncenin eleştirildiğini gösterir.','Örnekler (çocukluk, kaygı) ana düşünce değil, onu destekleyen ayrıntılardır.','Son cümlede izleyicinin rolü ne olarak sunuluyor?'],
  bilgi=[B_ANA,B_ANA2],
  adim=[AD('Karşıtlığı gör','“Oysa” ile parça, anlamı tek sanmayı eleştirir.','tek anlam ✗ → çok anlam ✓'),AD('Örneğe bak','Aynı tablo farklı kişilerde farklı duygu uyandırıyor; bu, ana fikri destekleyen örnektir.','örnek → destek'),AD('Son cümleyi oku','Eser izleyiciyle tamamlanıyor; sonuç, anlamın izleyene göre değiştiğidir.','sonuç: anlam izleyene göre değişir'),AD('Şıkları ele','B ve D parçaya ters, C ayrıntı ve yalnızca bir örnek, E parçada tersine çevrilmiş.','A: doğru')],
  puf='“Oysa, ama, fakat” sonrası çoğunlukla yazarın asıl savunduğu düşünce gelir.'),
 dict(metin='Okulda öğrenciler çoğunlukla cevap bulmakla ödüllendirilir. Oysa bir sorunun doğru sorulması, çoğu zaman cevabından daha çok emek ister. İyi soru konuyu daraltır, gizli varsayımları ortaya çıkarır ve düşünceyi yönlendirir. Bilim tarihine bakıldığında büyük keşiflerin yeni cevaplardan çok yeni sorulardan doğduğu görülür.\nBu parçanın ana düşüncesi aşağıdakilerden hangisidir?',
  dogru='Doğru soruyu sormak, çoğu zaman cevabı bulmaktan daha zor ve daha değerlidir.',harf='E',
  yan=[('Okullarda öğrencilerin cevap bulması ödüllendirilmemelidir.','Parça bir gözlem yapar ve “oysa” der; ödüllendirmenin kaldırılmasını önermez.','dikkat'),
       ('Büyük keşifler, ancak bilim insanlarının cevap ezberlemesiyle gerçekleşmiştir.','Parça keşiflerin “yeni sorulardan” doğduğunu söyler; şık parçaya terstir.','bilgi'),
       ('İyi bir soru konuyu daraltarak düşünceyi yönlendirir.','Bu yargı parçada geçen bir ayrıntıdır; parçanın tamamının sonucu değildir.','dikkat'),
       ('Bilim tarihi, yanıtı bulunamamış sorularla doludur.','Parçada böyle bir ifade yoktur; keşiflerin sorulardan doğduğu söylenir.','bilgi')],
  istenen='Parçanın asıl mesajı.',ip=['İkinci cümle, yazarın asıl iddiasını taşıyor.','Üçüncü cümle iyi sorunun özelliklerini sayar; bu bir ayrıntıdır.','Son cümle iddiayı hangi alanla destekliyor?']))

# ---------- 0003 yardımcı · kolay
Q.ekle('0003','K-PRG-02','kolay','Parçada değinilmeyen ayrıntıyı belirler.','düz',2,
 dict(metin='Zeytin ağacı, kuraklığa dayanıklı olması sayesinde Ege ve Akdeniz kıyılarındaki yamaçlarda yüzyıllardır yetiştirilir. Ağacın meyvesi sofralıkta tüketildiği gibi sıkılarak yağı da çıkarılır. Bu yağ yalnızca yemeklerde değil, sabun yapımında da kullanılır. Üstelik iyi bakılan bir zeytin ağacı yüzlerce yıl meyve vermeyi sürdürebilir.\nBu parçada zeytin ağacıyla ilgili aşağıdakilerden hangisine değinilmemiştir?',
  dogru='Gölgesinin serinlik vermesine',harf='E',
  yan=[('Yetiştirildiği bölgelere','İlk cümlede “Ege ve Akdeniz kıyılarındaki yamaçlar” denerek bu konuya değinilmiştir.','dikkat'),
       ('Kuraklığa karşı dayanıklı olmasına','İlk cümlede “kuraklığa dayanıklı olması” yazar.','dikkat'),
       ('Yağından sabun yapıldığına','Üçüncü cümlede “sabun yapımında da kullanılır” denir.','dikkat'),
       ('Uzun yıllar meyve verebilmesine','Son cümlede “yüzlerce yıl meyve vermeyi sürdürebilir” denir.','dikkat')],
  istenen='Parçada yer almayan bilgi.',ip=['Kök olumsuz: parçada bulunmayan şıkkı arıyorsun.','Her şıkkı parçada tek tek ara ve bulduğunu ele.','Hiçbir cümlede karşılığı olmayan şık cevaptır.'],
  bilgi=[B_YARD,B_KOK],
  adim=[AD('Kökü doğru oku','“Değinilmemiştir” diyor; parçada olmayanı arıyoruz.','aranan: parçada geçmeyen'),AD('Şıkları parçada ara','Bölge, kuraklık, sabun ve uzun ömür parçada var.','A, B, C, D: var'),AD('Geriye kalanı seç','Gölge ve serinlikten hiç söz edilmemiş.','E: yok → cevap')],
  puf='Olumsuz köklerde dört şıkkı parçada bulup eleyin; bulamadığınız şık cevaptır.'),
 dict(metin='Kaktüsler çöl gibi kurak bölgelerde yaşar. Gövdelerinde su depolayarak aylarca yağmursuz kalabilirler. Yaprakları dikene dönüşmüştür; bu sayede hem su kaybı azalır hem de hayvanlardan korunurlar. Bazı türler yılda yalnızca bir gece çiçek açar.\nBu parçada kaktüslerle ilgili aşağıdakilerden hangisine değinilmemiştir?',
  dogru='Köklerinin toprakta çok derine indiğine',harf='A',
  yan=[('Yaşadıkları ortamın özelliğine','İlk cümlede “çöl gibi kurak bölgelerde yaşar” denir.','dikkat'),
       ('Gövdelerinde su biriktirdiklerine','İkinci cümlede “gövdelerinde su depolayarak” yazar.','dikkat'),
       ('Dikenlerin ne işe yaradığına','Üçüncü cümlede dikenlerin su kaybını azalttığı ve koruma sağladığı belirtilir.','dikkat'),
       ('Bazı türlerin çiçek açma sıklığına','Son cümlede “yılda yalnızca bir gece çiçek açar” denir.','dikkat')],
  istenen='Parçada yer almayan bilgi.',ip=['Kök olumsuz; parçada geçmeyen bir bilgiyi arıyorsun.','Gövde, yaprak, çiçek, yaşam alanı parçada geçiyor mu, kontrol et.','Bitkinin hangi organı hiç anılmamış?']))

# ---------- 0004 yardımcı · orta
Q.ekle('0004','K-PRG-02','orta','Parçadan kesin olarak çıkarılamayacak yargıyı belirler.','düz',3,
 dict(metin='Bazı şehirler, ana caddelerin kenarına bisiklet yolu çizerek ulaşımda yeni bir dönem başlattı. Bu yollar sayesinde kısa mesafelerde araca binmek yerine pedal çevirmeyi seçenlerin sayısı arttı. Trafik yoğunluğu azaldıkça havadaki zararlı gaz miktarı da düşüyor. Ne var ki bisiklet yolları yeterli denetimle korunmazsa sürücüler yolu park yeri gibi kullanıyor ve yatırımın yararı sınırlı kalıyor.\nBu parçadan aşağıdaki yargılardan hangisi çıkarılamaz?',
  dogru='Bisiklet yolu yapılan her şehirde trafik sorunu tümüyle ortadan kalkmıştır.',harf='B',
  yan=[('Bisiklet yolları, bazı insanları kısa yolculuklarda araç kullanmaktan vazgeçirmiştir.','İkinci cümle kısa mesafede araç yerine bisiklet seçenlerin arttığını söyler; yargı çıkarılabilir.','dikkat'),
       ('Trafiğin azalması hava kalitesine olumlu yansıyabilir.','Üçüncü cümleye göre trafik azaldıkça zararlı gaz miktarı düşer; yargı çıkarılabilir.','dikkat'),
       ('Bisiklet yollarının yararı, denetim eksikliğinden zarar görebilir.','Son cümle denetimsiz yolun park yerine dönüştüğünü ve yararın sınırlı kaldığını söyler; yargı çıkarılabilir.','dikkat'),
       ('Bisiklet yolu yapmak, ulaşım politikalarında yenilik olarak görülmüştür.','İlk cümlede “yeni bir dönem başlattı” denir; yargı çıkarılabilir.','dikkat')],
  istenen='Parçadan çıkarılamayan yargı.',ip=['Kök olumsuz: çıkarılamayanı arıyorsun.','“Her, tümüyle, hiç” gibi sözcüklerle genellenen yargılara şüpheyle bak.','Parçada trafik için “azaldıkça” deniyor; “ortadan kalktı” deniyor mu?'],
  bilgi=[B_YARD,B_KOK],
  adim=[AD('Kökü doğru oku','Çıkarılamayan yargıyı arıyoruz; dört şık parçadan çıkar.','aranan: çıkarılamayan'),AD('Her şıkkı karşılığıyla eşle','A: ikinci cümle · C: üçüncü cümle · D: son cümle · E: ilk cümle.','A, C, D, E: karşılığı var'),AD('Aşırı genellemeyi yakala','“Her şehirde” ve “tümüyle ortadan kalkmıştır” iddiası parçada yok; yalnızca trafik azaldıkça düzelme var.','B: parçadan çıkmaz → cevap')],
  puf='Parçadan çıkarım sorularında “her, hiç, tümüyle, kesinlikle” içeren şık çoğunlukla parçayı aşar.'),
 dict(metin='Uzaktan eğitim, uzak köylerdeki öğrencilerin de aynı derse katılabilmesini mümkün kıldı. Ders kayıtları sayesinde anlamayan öğrenci konuyu istediği kadar yineleyebiliyor. Ancak ekran başında geçen uzun saatler dikkati dağıtıyor ve bazı öğrencilerde derse bağlılığı azaltıyor. Bu yüzden başarılı örneklerde derslerin kısa tutulduğu ve etkileşime yer verildiği görülüyor.\nBu parçadan aşağıdaki yargılardan hangisi çıkarılamaz?',
  dogru='Uzaktan eğitim, her koşulda yüz yüze eğitimin yerini almalıdır.',harf='C',
  yan=[('Uzaklık, eğitime katılmada artık tek başına engel olmaktan çıkabilir.','İlk cümle uzak köydeki öğrencinin aynı derse katılabildiğini söyler; yargı çıkarılabilir.','dikkat'),
       ('Kaydedilmiş dersler tekrar imkânı sağlar.','İkinci cümleye göre öğrenci konuyu istediği kadar yineleyebilir; yargı çıkarılabilir.','dikkat'),
       ('Ekran başında geçirilen sürenin uzaması derse bağlılığı düşürebilir.','Üçüncü cümlede bu durum açıkça yer alır; yargı çıkarılabilir.','dikkat'),
       ('Kısa ve etkileşimli dersler başarıyı olumlu etkileyebilir.','Son cümle başarılı örneklerde derslerin kısa ve etkileşimli olduğunu söyler; yargı çıkarılabilir.','dikkat')],
  istenen='Parçadan çıkarılamayan yargı.',ip=['Kök olumsuz; parçadan çıkarılamayan yargıyı arıyorsun.','Parçanın uzaktan eğitime bakışı dengeli mi, tek yönlü mü?','“Her koşulda … almalıdır” gibi bir öneri parçada var mı?']))

# ---------- 0005 tamamlama · orta
Q.ekle('0005','K-PRG-03','orta','Boşluğa gelecek cümleyi önceki ve sonraki cümlelerin akışına göre belirler.','düz',3,
 dict(metin='Bir işi öğrenmenin en kısa yolu, onu ilk günden başkasının yaptığı gibi yapmaya çalışmak değildir. Çünkü taklit, ancak yüzeydeki hareketleri öğretir. Oysa ustalık, bir hareketin neden öyle yapıldığını kavramakla başlar. ........ Nedenini bilen kişi, karşısına hiç görmediği bir durum çıksa bile doğru kararı verebilir.\nBu parçada boş bırakılan yere aşağıdakilerden hangisi getirilmelidir?',
  dogru='Bu yüzden iyi öğrenci, “nasıl”dan önce “neden” sorusunu sorar.',harf='D',
  yan=[('Her ustanın kendine özgü bir çalışma düzeni vardır.','Cümle konudan sapar; sonraki cümledeki “Nedenini bilen kişi” ifadesiyle bağ kurmaz.','dikkat'),
       ('Taklit eden kişi çok kısa sürede ustasını geçer.','Parça taklidin yüzeysel kaldığını söyler; şık bununla çelişir.','bilgi'),
       ('Kuralları ezberleyen kişi her zaman en hızlı öğrenendir.','Parça ezber/taklit yerine nedeni kavramayı över; şık bununla çelişir.','bilgi'),
       ('Hareketleri başkalarından öğrenmek zaman kaybından başka bir şey değildir.','Parça başkasından öğrenmeyi değil, yalnızca onu körü körüne taklit etmeyi eleştirir; şık aşırıdır.','bilgi')],
  istenen='Boşluğa gelecek cümle.',ip=['Boşluktan hemen sonra gelen cümle “Nedenini bilen kişi” diyor; bu ifade boşluktaki cümlede hazırlanmalı.','Boşluktaki cümle öncesindeki “neden öyle yapıldığını kavramak” düşüncesini sürdürmeli.','Parçanın taklidi yerdiğini unutma.'],
  bilgi=[B_TAM],
  adim=[AD('Öncesini oku','Parça taklidi yüzeysel bulup asıl ustalığı “nedeni kavramak” olarak tanımlıyor.','taklit ✗ · neden ✓'),AD('Sonrasını oku','“Nedenini bilen kişi” ifadesi, boşlukta nedenden söz edildiğini gösterir.','boşluk → neden'),AD('Şıkları sına','A konudan sapar; B, C, E parçanın görüşüyle çelişir. D hem öncekini sonuçlandırır hem sonrakini hazırlar.','D: doğru')],
  puf='Boşluğun hemen sonrasındaki cümlenin ilk sözcüğü (zamir, bağlaç, anahtar kavram) çoğu kez boşluğa gerekeni söyler.'),
 dict(metin='Bir şehrin tarihî dokusunu korumak, eski binaları olduğu gibi dondurmak anlamına gelmez. ........ Binalar kullanıldıkça yaşar; kullanılmayan bir yapı ne kadar güzel olursa olsun zamanla çürür.\nBu parçada boş bırakılan yere aşağıdakilerden hangisi getirilmelidir?',
  dogru='Önemli olan, bu yapıları günlük hayatın içinde yaşatmaktır.',harf='B',
  yan=[('Eski binaların hiçbirine dokunmadan bırakılması en doğru yoldur.','İlk cümle binaları “dondurmayı” reddeder; şık bununla çelişir.','bilgi'),
       ('Tarihî yapıların çoğu bugün müze olarak kullanılmaktadır.','Bu bilgi boşluktan sonraki “kullanılmayan yapı çürür” düşüncesiyle ve ilk cümleyle uyuşmaz; akışı koparır.','dikkat'),
       ('Yeni yapılar eski yapılardan her zaman daha dayanıklıdır.','Konunun korumayla ilgisi yoktur; ayrıca “her zaman” genellemesi vardır.','dikkat'),
       ('Şehirlerin tarihi yalnızca yazılı belgelerden öğrenilebilir.','Yapıların kullanımı konusundan sapar; sonraki cümleye bağlanmaz.','dikkat')],
  istenen='Boşluğa gelecek cümle.',ip=['İlk cümle bir yanlış anlamayı düzeltiyor: korumak “dondurmak” değildir.','Boşluktan sonraki cümle binaların neyle yaşadığını söylüyor.','Doğru cümle, “dondurmak” yerine olumlu bir alternatif sunmalı.']))

# ---------- 0006 tamamlama · zor
Q.ekle('0006','K-PRG-03','zor','Karşıt bağlaçlı paragrafta boşluğa gelecek cümleyi belirler.','düz',4,
 dict(metin='Gürültüye alışmış bir kent insanı, sessizliği çoğunlukla huzur olarak değil, bir eksiklik olarak yaşar. ........ Oysa sessizlik, zihnin kendi sesini duyabildiği nadir alanlardan biridir. Bu alanı yitiren kişi, düşüncelerini de başkalarının sesleri arasında kaybeder.\nBu parçada boş bırakılan yere aşağıdakilerden hangisi getirilmelidir?',
  dogru='Bu boşluğu doldurmak için televizyonu açar, hep bir ses ister.',harf='C',
  yan=[('Sessiz ortamlarda çalışan insanlar daha çok hata yapar.','Parçada hata yapma konusu yoktur; ayrıca “Oysa” ile başlayan cümleyle uyuşmaz.','dikkat'),
       ('Kentlerdeki gürültü düzeyi yıllar içinde düzenli biçimde azalmıştır.','Parça kent insanının gürültüye alıştığını söyler; şık bu durumla çelişir.','bilgi'),
       ('Sessizlik, insanın dış dünyayla bağını güçlendirir.','Sonraki “Oysa” cümlesi sessizliği iç dünya (zihin) bağlamında över; dış dünya vurgusu akışı bozar.','bilgi'),
       ('Gürültüden rahatsız olanlar kırsal bölgelere taşınmayı tercih ediyor.','Parçada taşınma konusu yoktur; “eksiklik” fikrini sürdürmez.','dikkat')],
  istenen='Boşluğa gelecek cümle.',ip=['İlk cümlede sessizlik bir “eksiklik” olarak yaşanıyor; boşluk bu eksikliğe verilen tepkiyi anlatabilir.','“Oysa” sözcüğü, boşluktaki davranışın yanlış olduğunu gösteren karşıt bir düşünce başlatır.','Boşluktaki cümle “bu” gönderiminde bulunuyorsa önceki cümleyle bağ kurar.'],
  bilgi=[B_TAM],
  adim=[AD('Öncesine bak','Kent insanı sessizliği “eksiklik” olarak yaşar.','sessizlik = eksiklik'),AD('Sonrasına bak','“Oysa” cümlesi sessizliğin aslında değerli olduğunu söyler; yani önce yapılan yanlış bir davranış anlatılmalı.','boşluk: eksikliğe tepki'),AD('Şıkları sına','A ve D konudan sapar, B ilk cümleyle çelişir, E “Oysa” bağlacının gerektirdiği karşıtlığı kuramaz.','A, B, D, E: elendi'),AD('Doğrula','C seçilince “eksiklik → doldurmaya çalışmak → oysa sessizlik değerli” akışı kurulur.','C: doğru')],
  puf='Boşluğun iki yanındaki cümleleri bağlayan “oysa, ama, ne var ki” gibi bağlaçlar akışın yönünü verir; önce yönü bul, sonra şıkları ele.'),
 dict(metin='Eskiden bir haberin ulaşması günler alırdı; bu yüzden insanlar haberi dikkatle dinler, üzerinde uzun uzun düşünürdü. Bugün ise bilgi saniyeler içinde yayılıyor. Bu hız, kuşkusuz birçok kolaylık getirdi. Ne var ki ........\nBu parçada boş bırakılan yere aşağıdakilerden hangisi getirilmelidir?',
  dogru='doğruyu sınamaya zaman kalmadığı için yanlış haberler de hızla yayılıyor.',harf='E',
  yan=[('haber almak artık eskisinden çok daha ucuz hâle geldi.','“Ne var ki” karşıt/olumsuz bir yargı bekler; şık yeni bir kolaylık ekleyerek akışı sürdürür.','dikkat'),
       ('insanlar bugün de haberleri eskisi gibi uzun uzun düşünerek değerlendiriyor.','Parça bugünün hızlı olduğunu ve eski alışkanlığın değiştiğini ima eder; şık durumla çelişir.','bilgi'),
       ('bilgiye ulaşmak için hâlâ günlerce beklemek gerekiyor.','Parça bilginin saniyeler içinde yayıldığını söyler; şık ona terstir.','bilgi'),
       ('bu kolaylık sayesinde herkes aynı anda aynı bilgiye sahip oluyor.','Bu yargı da bir kolaylıktır; “Ne var ki” ile başlayan cümleden beklenen olumsuzluğu taşımaz.','dikkat')],
  istenen='Boşluğa gelecek cümle.',ip=['“Kuşkusuz birçok kolaylık getirdi” dendikten sonra “Ne var ki” geldiğine dikkat et.','Boşluk, hızın getirdiği bir sakıncayı anlatmalı.','Parçada eskiden dikkatle dinlendiği, bugün ise hızın arttığı söyleniyor.']))

# ---------- sıralama yardımcıları
def siralama(c,roller,soru_poz,hedef_harf,seed,kok_fn):
    """c: doğru sıradaki 5 cümle; roller: her cümlenin doğru sıradaki rolü; soru_poz: 0 tabanlı istenen sıra; hedef_harf: doğru şık harfi"""
    n=5; hi='ABCDE'.index(hedef_harf); rnd=random.Random(seed)
    while True:
        perm=list(range(n)); rnd.shuffle(perm)
        metin,sira=numarali(c,perm)
        if sira[soru_poz]==ROM[hi] and sira!=ROM[:n] and perm[0]!=0: break
    dogru=ROM[hi]; assert sira[soru_poz]==dogru
    yan=[]
    for r in ROM[:n]:
        if r==dogru: continue
        pos=sira.index(r)+1
        yan.append((r,f'{r}. cümle doğru sıralamada {pos}. sıradadır ({roller[perm[ROM.index(r)]]}); istenen sırada değildir.','dikkat'))
    return metin,dogru,yan,'–'.join(sira),sira

def sira_soru(c,roller,poz,harf,seed,kok,ipuclari,adimlar_fn):
    metin,dogru,yan,dizi,sira=siralama(c,roller,poz,harf,seed,None)
    d=dict(metin=metin+'\n'+kok,dogru=dogru,harf=harf,yan=yan,istenen='İstenen sıradaki cümle.',ip=ipuclari,adim=adimlar_fn(dizi,sira,dogru),bilgi=[B_SIRA],puf='Önce bağlaç ve zamir taşımayan giriş cümlesini, sonra “bu, onlar, çünkü, böylece” gibi gönderme sözcüklerini izleyerek zinciri kur.')
    return d

import re as _re
def par(d):
    f=lambda t:_re.sub(r'^([IV]+)(\. cümle)?$',r'(\1)',t)
    d['dogru']=f(d['dogru']); d['yan']=[(f(a),b,c) for a,b,c in d['yan']]; return d
# ---------- 0007 sıralama · orta
c1=['Ormanlarda yaşayan karıncalar, yiyecek bulduklarında yuvaya dönerken yol boyunca kokulu bir iz bırakır.',
    'Yuvadaki diğer karıncalar bu kokuyu algılayıp izi takip eder.',
    'Onlar da dönüşte aynı yolu kendi kokularıyla pekiştirir.',
    'Böylece iz giderek belirginleşir ve yiyeceğe giden en kısa yol kalabalık bir sıraya dönüşür.',
    'Ancak yağmur gibi bir etki izi silerse sıra dağılır ve karıncalar yeni bir yol aramaya koyulur.']
r1=['giriş: izi bırakmayı tanıtır','“bu kokuyu” ile 1. cümleye bağlanır','“Onlar” ile 2. cümledeki karıncalara gönderme yapar','“Böylece” ile öncekilerin sonucunu verir','“Ancak” ile sonucu bozan karşıt durumu getirir']
c2=['Toprağa düşen bir tohum, yeterli nem bulduğunda dış kabuğunu yumuşatmaya başlar.',
    'Kabuk çatladığında içinden önce küçük bir kök uzar.',
    'Kök toprağa tutunduktan sonra tohumun diğer ucundan sürgün yukarı doğru büyür.',
    'Sürgün yüzeye çıkıp ışığı görünce ilk yeşil yapraklar açılır.',
    'Bu yapraklar fidanın kendi besinini üretmesini sağlayarak tohumdaki yedek besine olan ihtiyacı bitirir.']
r2=['giriş: tohumun nemle yumuşamasını anlatır','“Kabuk çatladığında” ile 1. cümlenin devamıdır','“Kök toprağa tutunduktan sonra” 2. cümledeki kökü izler','“Sürgün” ile 3. cümledeki sürgünü sürdürür','“Bu yapraklar” ile 4. cümledeki yapraklara bağlanır, sonucu verir']
def adim_sira(dizi,sira,dogru):
    return [AD('Girişi bul','Hiçbir zamir ya da bağlaç taşımayan, konuyu tanıtan cümle başa gelir.','başlangıç cümlesi belli'),
            AD('Bağlantıları kur','“Bu, onlar, böylece, ancak, sonra” gibi sözcükler her cümlenin önceki cümleye bağlandığını gösterir.','zamir/bağlaç zinciri'),
            AD('Doğru sırayı yaz','Zincir kurulunca sıra ekrandaki numaralarla yazılır.',f'sıra: {dizi}'),
            AD('İstenen sıraya bak',f'Sorunun istediği sıradaki cümlenin numarasını oku.',f'cevap: {dogru}')]
Q.ekle('0007','K-PRG-04','orta','Zamir ve bağlaçlardan yararlanarak cümleleri anlamlı bir bütün oluşturacak biçimde sıralar.','öncüllü',4,
 sira_soru(c1,r1,2,'B',11,'Bu cümleler anlamlı bir bütün oluşturacak biçimde sıralandığında baştan üçüncü cümle hangisi olur?',
   ['Zamirli cümleleri, gönderme yaptıkları cümlenin hemen arkasına koy.','Hiçbir bağlaç ya da zamir taşımayan cümle başa gelir.','Sonucu bildiren “böylece” cümlesi ve karşıtlık bildiren “ancak” cümlesi sonlara yakındır.'],adim_sira),
 par(sira_soru(c2,r2,3,'A',5,'Bu cümleler anlamlı bir bütün oluşturacak biçimde sıralandığında sondan ikinci cümle hangisi olur?',
   ['Sürecin başı, zamir ya da bağlaç taşımayan cümledir.','Sürgün, kökten sonra gelir; yapraklar da sürgünden sonra.','Sıra tamamlanınca sondan ikinciyi say.'],adim_sira)))
# sondan ikinci = baştan dördüncü (indeks 3)

# ---------- 0008 sıralama · zor
c3=['Dil, yalnızca insanların birbirini anlamasını sağlayan bir araç değildir.',
    'Aynı zamanda bir toplumun yüzyıllar boyunca biriktirdiği düşünce ve duyguları yeni kuşaklara taşır.',
    'Bunun en açık kanıtı atasözleri ve deyimlerdir.',
    'Çünkü bu kalıplar, ait oldukları halkın yaşam deneyimini birkaç sözcüğe sığdırır.',
    'Dolayısıyla bir dili öğrenen kişi, onunla birlikte o toplumun bakışını da öğrenmiş olur.']
r3=['giriş: ana iddiayı olumsuzlayarak açar','“Aynı zamanda” ile 1. cümlenin iddiasını tamamlar','“Bunun” ile 2. cümledeki taşıma işlevine gönderme yapar, kanıt gösterir','“Çünkü” ile 3. cümledeki kanıtın nedenini açıklar','“Dolayısıyla” ile sonuç çıkarır']
c4=['Alışveriş sırasında çocuğa sürekli “hayır” demek, ona para konusunda bir şey öğretmez.',
    'Bunun yerine çocuğa sınırlı bir harçlık verip kararı onun eline bırakmak daha öğretici olur.',
    'Çünkü harçlığını erken harcayan çocuk, ay sonuna doğru istediği şeyi alamayacağını kendi yaşantısıyla görür.',
    'Bu deneyim, hiçbir nasihatin anlatamayacağı biçimde, harcamadan önce düşünmeyi öğretir.',
    'Kısacası parayı yönetmeyi öğrenmenin en sağlam yolu, küçük hatalara izin vermektir.']
r4=['giriş: “hayır” demenin öğretmediğini söyler','“Bunun yerine” ile 1. cümledeki yöntemin karşıtını önerir','“Çünkü” ile 2. cümledeki önerinin nedenini açıklar','“Bu deneyim” ile 3. cümledeki yaşantıya bağlanır','“Kısacası” ile genel sonuca varır']
def adim_sira2(dizi,sira,dogru):
    return [AD('Giriş cümlesini seç','Zamir ve bağlaç taşımayan, iddiayı ilk kez ortaya koyan cümle başa gelir.','giriş belli'),
            AD('Bağlaçları sırala','“Aynı zamanda, bunun, çünkü, bu, dolayısıyla/kısacası” cümleleri öncekilerle zincirler; “çünkü” nedeni, “dolayısıyla” sonucu getirir.','neden → sonuç zinciri'),
            AD('Zinciri yaz','Ekrandaki numaralarla doğru sıra kurulur.',f'sıra: {dizi}'),
            AD('İstenen sırayı bul','Sorunun istediği sıradaki cümlenin numarası cevaptır.',f'cevap: {dogru}')]
Q.ekle('0008','K-PRG-04','zor','Neden–sonuç ve gönderme ilişkilerini birlikte kullanarak cümleleri sıralar.','öncüllü',5,
 sira_soru(c3,r3,3,'E',3,'Bu cümleler anlamlı bir bütün oluşturacak biçimde sıralandığında baştan dördüncü cümle hangisi olur?',
   ['Önce iddianın açıldığı cümleyi bul.','“Çünkü” ile başlayan cümle, açıkladığı cümlenin hemen arkasına gelir.','“Dolayısıyla” ile başlayan cümle sonuç bildirdiği için sondadır.'],adim_sira2),
 par(sira_soru(c4,r4,3,'B',7,'Bu cümleler anlamlı bir bütün oluşturacak biçimde sıralandığında sondan ikinci cümle hangisi olur?',
   ['Hiçbir bağlaç ya da zamir taşımayan cümle başa gelir.','“Çünkü” cümlesi, önerinin nedenini açıkladığı için öneri cümlesinden sonradır.','“Kısacası” ile başlayan cümle en sondadır; sondan ikinciyi onun hemen öncesinde ara.'],adim_sira2)))

# ---------- akış bozan yardımcı
def akis_soru(cumleler,roller,bozan,kok='Bu parçadaki numaralanmış cümlelerden hangisi düşüncenin akışını bozmaktadır?'):
    assert len(cumleler)==5 and len(roller)==5
    metin=' '.join(f'({ROM[i]}) {c}' for i,c in enumerate(cumleler))+'\n'+kok
    yan=[(ROM[i]+'. cümle',f'{ROM[i]}. cümle parçanın odağına hizmet eder ({roller[i]}); akışı bozmaz.','dikkat') for i in range(5) if i!=bozan]
    return dict(metin=metin,dogru=ROM[bozan]+'. cümle',harf='ABCDE'[bozan],yan=yan,istenen='Akışı bozan cümle.',bilgi=[B_AKIS],
      puf='Akışı bozan cümle çoğu zaman parçayla aynı anahtar sözcüğü taşır; asıl ölçüt sözcük değil, anlatılan yöndür.')
def adim_akis(odak,roller_ozet,bozan_ac,rom):
    return [AD('Odağı bul',odak,'odak belirlendi'),AD('Cümleleri tek tek sına',roller_ozet,'diğer cümleler odakta'),AD('Sapmayı yakala',bozan_ac,f'{rom}: odak dışı → cevap')]

# ---------- 0009 akış · orta
d=akis_soru(['Oyun, çocuğun dünyayı tanımasını ve düşünme becerisini geliştirmesini sağlar.','Evcilik oynayan çocuk, günlük yaşamdaki rolleri deneyerek toplumsal ilişkileri kavrar.','Oyuncak sektörü son yıllarda hızla büyümüş ve yeni mağazalar açılmıştır.','Birlikte oyun kuran çocuklar kural koymayı, sıra beklemeyi ve uzlaşmayı da öğrenir.','Bu nedenle oyun, çocuk gelişiminde göz ardı edilmemesi gereken bir öğrenme alanıdır.'],
 ['konuyu tanıtır','oyunun öğrettiklerine örnektir','','oyunun sosyal kazanımını anlatır','sonucu verir'],2)
d.update(ip=['Önce parçanın odağını tek cümleyle söyle: oyun neyi sağlıyor?','Her cümle bu odağa hizmet ediyor mu?','Odakla aynı sözcüğü paylaşan ama farklı konuya geçen cümleyi ara.'],
 adim=adim_akis('Parça, oyunun çocuğun gelişimine katkısını anlatıyor.','I tanıtır, II ve IV örnek ve ayrıntı verir, V sonucu söyler.','III. cümle oyunun gelişim etkisini değil, oyuncak sektörünün büyümesini anlatır.','III'))
d2=akis_soru(['Ev bütçesi yapmak, harcamaları önceden planlamak demektir.','Önce gelir yazılır, ardından kira ve faturalar gibi zorunlu giderler çıkarılır.','Kalan para, birikim ve istek harcamaları arasında paylaştırılır.','Ünlü markaların mağazaları genellikle büyük alışveriş merkezlerinde bulunur.','Bütçeyi düzenli izleyen aile, ay sonunda sürprizlerle karşılaşmaz.'],
 ['bütçenin tanımı','bütçe yapma adımı','bütçe yapma adımı','','bütçenin sonucu'],3)
d2.update(ip=['Parçanın odağı bütçenin nasıl yapıldığıdır.','Her cümle bütçe adımlarından birini ya da sonucunu anlatıyor mu?','Bütçe dışında, farklı bir konuya geçen cümleyi ara.'],
 adim=adim_akis('Parça, ev bütçesinin nasıl yapıldığını anlatıyor.','I tanımlar, II ve III adımları sıralar, V sonucu söyler.','IV. cümle markaların mağazalarının yerinden söz eder; bütçeyle ilgisi yoktur.','IV'))
Q.ekle('0009','K-PRG-05','orta','Parçanın odağını belirleyip akışı bozan cümleyi bulur.','öncüllü',3,d,par(d2))

# ---------- 0010 akış · zor
d=akis_soru(['Göçmen kuşlar, binlerce kilometre öteden bile yuvalarına dönebilir.','Bunu başarmalarında en önemli etkenlerden biri, güneşin gün içindeki konumunu ölçü almalarıdır.','Bazı türler ise geceleri yıldızların dizilişinden yararlanır.','Kuşların göç ettikleri mesafe, türden türe büyük farklılıklar gösterir.','Yeryüzünün manyetik alanını algılayabilen türler, bulutlu havalarda bile yönlerini şaşırmaz.'],
 ['yön bulma yeteneğini tanıtır','yön bulma yolu: güneş','yön bulma yolu: yıldız','','yön bulma yolu: manyetik alan'],3)
d.update(ip=['Parça kuşların bir yeteneğini, hangi yönden anlatıyor? Yöntemleri mi, süreyi mi, mesafeyi mi?','II, III ve V’in ortak noktasını bul.','Geriye kalan cümle “göç” konusuna girse de aynı yönü anlatıyor mu?'],
 adim=adim_akis('Parça, göçmen kuşların yönlerini nasıl bulduğunu (güneş, yıldız, manyetik alan) anlatıyor.','I yeteneği tanıtır; II, III ve V yön bulma yollarını sayar.','IV. cümle göç mesafesinin türlere göre değiştiğini söyler; yön bulma yolundan değil, göçün uzunluğundan söz eder.','IV'))
d2=akis_soru(['Gerçek bir dinleme, yalnızca duyulanı kulakla almaktan ibaret değildir.','İyi dinleyici, karşısındaki sözünü bitirmeden kendi cevabını hazırlamaya girişmez.','Konuşma yarışmalarında dereceye girenler çoğunlukla akıcı ve etkili konuşanlardır.','Konuşanın yüzüne bakmak ve ara sıra başıyla onaylamak, ona önemsendiğini hissettirir.','Bu davranışlar, dinlemenin duyguyla da ilgili olduğunu gösterir.'],
 ['dinlemenin yalnız duymak olmadığını söyler','dinleyicinin davranışı','','dinleyicinin davranışı','davranışlardan sonuç çıkarır'],2)
d2.update(ip=['Parçanın odağı iyi dinleyicinin ne yaptığıdır.','Her cümle dinleyen kişinin davranışı ya da dinlemenin niteliğiyle ilgili mi?','Konuşma konusuna kayan cümleyi ara.'],
 adim=adim_akis('Parça, iyi bir dinlemenin nasıl olduğunu anlatıyor.','I dinlemeyi tanımlar, II ve IV dinleyicinin davranışlarını sayar, V bunlardan sonuç çıkarır.','III. cümle dinlemeyi değil, konuşma yarışmalarındaki başarıyı anlatır.','III'))
Q.ekle('0010','K-PRG-05','zor','Aynı konu alanındaki ince sapmayı fark ederek akışı bozan cümleyi bulur.','öncüllü',4,d,par(d2))

# ---------- 0011 anlatım biçimi · kolay
SIK_ANL=['Betimleyici anlatım','Öyküleyici anlatım','Açıklayıcı anlatım','Tartışmacı anlatım','Kanıtlayıcı anlatım']
Q.ekle('0011','K-PRG-06','kolay','Parçada ağırlıklı olarak kullanılan anlatım biçimini belirler.','düz',2,
 dict(metin='Köyün girişindeki yaşlı çınar dallarını yola doğru uzatmış, gövdesi üç kişinin kucaklayamayacağı kadar kalınlaşmıştı. Yapraklarının arasından süzülen ışık, altındaki taş sıralara benekli bir gölge düşürüyordu. Kabuğundaki çatlaklar, yılların bıraktığı derin çizgiler gibiydi.\nBu parçada ağırlıklı olarak hangi anlatım biçimi kullanılmıştır?',
  dogru='Betimleyici anlatım',harf='A',
  yan=[('Öyküleyici anlatım','Parçada zaman içinde ilerleyen bir olay yok; ağacın görünüşü anlatılıyor.','bilgi'),('Açıklayıcı anlatım','Parça bilgi vermeyi değil, görüntüyü canlandırmayı amaçlar.','bilgi'),('Tartışmacı anlatım','Parçada savunulan ya da çürütülen bir görüş yoktur.','bilgi'),('Kanıtlayıcı anlatım','Parçada bir iddiayı ispatlamaya yönelik delil bulunmaz.','bilgi')],
  istenen='Ağırlıklı anlatım biçimi.',ip=['Parça bir olayı mı, bir görüntüyü mü anlatıyor?','“Düşürüyordu, gibiydi” gibi ifadeler neyi gösteriyor?','Okuyucunun gözünde ne canlanıyor?'],
  bilgi=[B_ANL],
  adim=[AD('Parçanın ne yaptığına bak','Ağacın gövdesi, yaprakları, gölgesi ve kabuğu sözcüklerle resmediliyor.','görünüş anlatılıyor'),AD('Olay var mı?','Zaman içinde gelişen bir olay ya da kişi eylemi yok.','öyküleme ✗'),AD('Biçimi adlandır','Görünüşü sözcüklerle çizmek betimlemedir.','cevap: betimleyici')],
  puf='Okuyunca bir resim canlanıyorsa betimleme, bir film akıyorsa öyküleme, bilgi ediniyorsan açıklama vardır.'),
 dict(metin='Sabah erkenden evden çıktı, iskeleye vardığında vapurun kalkmak üzere olduğunu gördü. Koşarak merdivenleri indi, tam kalkarken kendini güverteye attı. Biletçi gülümseyerek ona baktı; o da nefes nefese bir yer bulup oturdu.\nBu parçada ağırlıklı olarak hangi anlatım biçimi kullanılmıştır?',
  dogru='Öyküleyici anlatım',harf='D',
  yan=[('Betimleyici anlatım','Parçada bir görünüş ayrıntılı biçimde resmedilmiyor; eylemler sırayla veriliyor.','bilgi'),('Açıklayıcı anlatım','Parça bilgi vermiyor, bir olayı aktarıyor.','bilgi'),('Tartışmacı anlatım','Parçada bir görüş savunulmuyor.','bilgi'),('Kanıtlayıcı anlatım','Parçada ispatlanmaya çalışılan bir iddia yok.','bilgi')],
  istenen='Ağırlıklı anlatım biçimi.',ip=['Cümlelerdeki fiillere bak: çıktı, gördü, indi, attı.','Olaylar hangi sırayla aktarılıyor?','Bir görüntü mü, bir olay akışı mı var?']))

# ---------- 0012 düşünceyi geliştirme · orta
Q.ekle('0012','K-PRG-06','orta','Parçada başvurulmayan düşünceyi geliştirme yolunu belirler.','düz',3,
 dict(metin='Uyku, zihnin bakım zamanıdır; tıpkı bir bilgisayarın kapanıp yeniden açılarak toparlanması gibi, beyin de gece boyunca gün içinde edindiği bilgileri düzenler. Düzenli uyuyan öğrencilerle uykusuz kalanlar karşılaştırıldığında, ilk gruptaki öğrencilerin aynı konuyu daha çabuk kavradığı görülür. Örneğin sınavdan önceki gece sabaha kadar ders çalışan bir öğrenci, ertesi gün öğrendiklerinin büyük bölümünü karıştırabilir. Bu yüzden uykusuz geçen bir gece, öğrenmenin sonraki gününü de olumsuz etkiler.\nBu parçada aşağıdakilerden hangisine başvurulmamıştır?',
  dogru='Tanık gösterme',harf='E',
  yan=[('Benzetme','“Tıpkı bir bilgisayarın … gibi” ifadesiyle uyku bilgisayara benzetilmiştir.','dikkat'),('Karşılaştırma','Düzenli uyuyan öğrencilerle uykusuz kalanlar yan yana konup karşılaştırılmıştır.','dikkat'),('Örneklendirme','“Örneğin” ile sınav öncesi sabaha kadar çalışan öğrencinin durumu örnek olarak verilmiştir.','dikkat'),('Neden–sonuç ilişkisi kurma','“Bu yüzden” ile uykusuz gecenin sonraki günü etkilediği söylenerek neden–sonuç kurulmuştur.','dikkat')],
  istenen='Parçada kullanılmayan yöntem.',ip=['Kök olumsuz: parçada olmayan yöntemi arıyorsun.','Her yöntemin parçadaki işaretini (gibi, örneğin, karşılaştırıldığında, bu yüzden) ara.','Başkasının sözüne ya da görüşüne başvurulmuş mu?'],
  bilgi=[B_GEL,B_KOK],
  adim=[AD('Kökü doğru oku','“Başvurulmamıştır” diyor; parçada olmayan yöntemi arıyoruz.','aranan: olmayan'),AD('İşaretlerle eşle','“Tıpkı … gibi” benzetme · “karşılaştırıldığında” karşılaştırma · “Örneğin” örnekleme · “Bu yüzden” neden–sonuç.','A, B, C, D: var'),AD('Geriye kalanı seç','Parçada bir uzmanın, yazarın ya da kaynağın sözüne başvurulmamıştır.','E: yok → cevap')],
  puf='Yöntem sorularında her yöntemin dildeki işaretini bil: gibi → benzetme, örneğin → örnekleme, bu yüzden → neden–sonuç.'),
 dict(metin='Kuraklık, yağış miktarının uzun süre normalin altında kalmasıdır. Yağışlı bölgelerde bir iki aylık kuraklık fark edilmezken, kurak iklimlerde aynı süre ürünlerin kurumasına yol açar. Örneğin buğday ekilen bir tarlada çimlenme döneminde yağmur gelmezse tohumlar toprakta çürür. Bu nedenle çiftçiler, kuraklık dönemlerine uygun ürünleri seçmeye yönelir.\nBu parçada aşağıdakilerden hangisine başvurulmamıştır?',
  dogru='Benzetme',harf='A',
  yan=[('Tanımlama','İlk cümle “Kuraklık, … kalmasıdır” diyerek kavramı tanımlar.','dikkat'),('Karşılaştırma','Yağışlı bölgelerle kurak iklimler yan yana konup karşılaştırılmıştır.','dikkat'),('Örneklendirme','“Örneğin” ile buğday tarlası örnek verilmiştir.','dikkat'),('Neden–sonuç ilişkisi kurma','“Bu nedenle” ile kuraklığın çiftçilerin tercihini belirlediği söylenmiştir.','dikkat')],
  istenen='Parçada kullanılmayan yöntem.',ip=['Kök olumsuz: parçada olmayanı arıyorsun.','“Gibi, sanki, tıpkı” sözcükleri parçada var mı?','Her yöntemin dildeki işaretini bul ve işaretsizi seç.']))

Q.bitir()
