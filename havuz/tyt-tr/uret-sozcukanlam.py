"""TYT Türkçe · Sözcükte Anlam: 8 ana + 8 kardeş. Metinler özgündür."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from tr_ortak import *
AD=A
KARTLAR={
 'K-SZA-01':dict(alt='Gerçek ve Mecaz Anlam',fikir='Aynı sözcüğün gerçek (temel) ve mecaz anlamda kullanıldığı cümleleri ayırt etmek.',tuzak='Alışılmış ama mecaz olan sözcük birleşimlerini (soğuk bakış, sert söz) gerçek anlam sanmak.',zorluk='kolay',kalip='düz',adim=2,tipId='szc-mecaz',kaynak='ÖSYM TYT Türkçe 2018–2026 (sözcükte anlam: gerçek-mecaz)'),
 'K-SZA-02':dict(alt='Eş, Yakın ve Zıt Anlam',fikir='Sözcük çiftlerinin eş/yakın ya da zıt anlam ilişkisini ayırt etmek.',tuzak='Yakın anlamlıyı zıt anlamlı, zıt anlamlıyı yakın anlamlı sanmak; bağlamsız anlam yüklemek.',zorluk='orta',kalip='düz',adim=3,tipId='szc-esanlam',kaynak='ÖSYM TYT Türkçe 2018–2026 (sözcükte anlam: eş-zıt anlam)'),
 'K-SZA-03':dict(alt='Çok Anlamlılık',fikir='Çok anlamlı bir sözcüğün hangi cümlede hangi anlamda kullanıldığını bağlamdan bulmak.',tuzak='Sözcüğün en sık bilinen anlamına takılıp bağlamı atlamak; yakın görünen yan anlamları aynı saymak.',zorluk='orta',kalip='düz',adim=3,tipId='szc-cokanlam',kaynak='ÖSYM TYT Türkçe 2018–2026 (sözcükte anlam: çok anlamlılık)'),
 'K-SZA-04':dict(alt='Sözcükler Arası Anlam İlişkisi',fikir='Üst–alt anlam, parça–bütün, araç–işlev gibi sözcükler arası ilişkileri tanımak.',tuzak='Yüzeysel benzerlik ya da birlikte anılmaya bakıp ilişkinin türünü ve yönünü atlamak.',zorluk='orta',kalip='düz',adim=3,tipId='szc-iliski',kaynak='ÖSYM TYT Türkçe 2018–2026 (sözcükte anlam: anlam ilişkileri)'),
}
TIPLER={'szc-mecaz':'Gerçek ve mecaz anlam','szc-esanlam':'Eş, yakın ve zıt anlam','szc-cokanlam':'Çok anlamlılık','szc-iliski':'Sözcükler arası anlam ilişkisi'}
Q=Konu('sozcukanlam','Sözcükte Anlam','tr|Sözcükte Anlam',KARTLAR,TIPLER)

B_GM=B('Gerçek ve mecaz anlam','gerçek anlam: sözcüğün ilk akla gelen, somut anlamı (sıcak süt). Mecaz anlam: sözcüğün benzetme yoluyla başka bir kavrama aktarıldığı anlam (sıcak bakış = samimi bakış)')
B_ESZ=B('Eş, yakın ve zıt anlam','eş/yakın anlamlı: aynı ya da çok yakın anlamda sözcükler (titiz – özenli). Zıt anlamlı: karşıt anlamlı sözcükler (kalıcı – geçici). Örnek: “cömert – eli açık” eş anlamlıdır, “cömert – cimri” zıttır')
B_CA=B('Çok anlamlılık','bir sözcüğün birden fazla anlamı olabilir; hangisinin kastedildiği cümledeki bağlamdan anlaşılır. Örnek: “sıcak ekmek” (ısısı yüksek) ile “sıcak bakış” (samimi) aynı sözcüğün farklı anlamlarıdır')
B_IL=B('Anlam ilişkileri','üst anlam: kapsayan sözcük (çiçek ⊃ gül, lale) · parça–bütün: sayfa – kitap · araç–işlev: makas – kesmek · meslek–yer: doktor – hastane. İlişkinin yönüne de bak')

Q.KADIM={
 '0001':[AD('Gerçek anlamı hatırla','“Sert”, gerçek anlamda dokunulduğunda yumuşak olmayan şeyler için kullanılır.','sert = yumuşak olmayan'),AD('Cümleleri tek tek oku','B, C, D ve E’deki sözcükler (kalın, taze, uzun, kuru) somut nesnelerin özelliğini anlatıyor.','B, C, D, E: gerçek anlam'),AD('Mecazı yakala','“Sert sözler” dokunulan bir şey değil, kırıcı sözlerdir; benzetmeyle aktarılmıştır.','A: mecaz')],
 '0002':[AD('Aynı sözcüğü izle','“Işık” beş cümlede de geçiyor; hangisinde somut ışık var?','ışık: 5 cümle'),AD('Mecaz örnekleri ele','A, B, D, E’de ışık; çözüm, neşe, rehber, yenilik anlamına aktarılmış.','A, B, D, E: mecaz'),AD('Gerçek olanı bul','C’de perdenin aralığından giren fiziksel ışık anlatılıyor.','C: gerçek anlam')],
 '0003':[AD('Çiftleri sınıfla','Her çiftin anlam ilişkisini yaz: yakın mı, zıt mı?','çiftler sınıflandı'),AD('Zıt çiftleri belirle','Yoksul–zengin zıt, diğer dört çift yakın anlamlı.','A, C, D, E: yakın'),AD('Farklı olanı seç','B çifti zıt, geri kalanı yakın anlamlı olduğu için farklıdır.','B: cevap')],
 '0004':[AD('Çiftleri belirle','Her cümlede tırnak içindeki iki sözcüğe bak.','5 çift'),AD('İlişkiyi adlandır','A, B, C ve D’deki çiftler zıt anlamlı (büyük–ufak, sessiz–gürültülü, dün–bugün, yeni–eski).','A, B, C, D: zıt'),AD('Yakın anlamlıyı bul','E’de “zorlu” ile “çetin” aynı anlama yakındır.','E: yakın anlamlı')],
 '0005':[AD('Örnekteki anlamı bul','“Yokuşu çıkmak”, aşağıdan yukarıya doğru gitmek demektir.','çıkmak = yukarı gitmek'),AD('Şıkları karşılaştır','B leke çıkarma, C yayımlanma, D ortaya çıkma, E dışarı çıkma anlamındadır.','B, C, D, E: farklı anlam'),AD('Aynı anlamı seç','A’da çocuk merdivenle yukarı gidiyor; örnekteki anlamla aynı.','A: doğru')],
 '0006':[AD('Anlamları ayır','“Tatlı” burada hem şekerli bir tat, hem hoş, yumuşak anlamında kullanılabilir.','tatlı: tat / hoş'),AD('Çiftleri karşılaştır','A, B, D, E’de iki cümlede “tatlı” farklı anlamdadır (tat–sevimli, tuzsuz–hoş...).','A, B, D, E: farklı'),AD('Aynı anlamlı çifti seç','C’de iki cümlede de “tatlı” yumuşak, hoş anlamındadır.','C: doğru')],
 '0007':[AD('Grupları incele','Her grupta dört sözcük var; biri diğerlerini kapsıyor mu?','4 sözcüklü gruplar'),AD('Kapsayan sözcüğü ara','A, B, C ve E’de hepsi aynı düzeyde sözcükler, kapsayıcı yok. D’de “çalgı” keman, gitar, piyanoyu kapsar.','D: çalgı = üst anlam'),AD('Doğrula','Keman, gitar, piyano çalgıdır; tersi geçerli değildir.','D: doğru')],
 '0008':[AD('Örnek ilişkiyi çöz','“Parmak – el”: parmak, elin bir parçasıdır (parça–bütün).','parça → bütün'),AD('Yönü kontrol et','Parça önce, bütün sonra gelmeli.','yön: parça–bütün'),AD('Şıkları ele','B ürün–yer, C meslek–araç, E araç–işlev, A ise ürün–yer. D’de tuş, klavyenin parçasıdır.','A: parça–bütün')],
}

# 0001 mecaz · kolay
Q.ekle('0001','K-SZA-01','kolay','Aynı sözcüğün gerçek ve mecaz anlamlı kullanımlarını ayırt eder.','düz',2,
 dict(metin='Aşağıdaki cümlelerin hangisinde tırnak içindeki sözcük mecaz anlamda kullanılmıştır?',
  dogru='Annesinin “soğuk” bakışları karşısında sustu.',harf='D',
  yan=[('Çocuk “sıcak” sütü üfleyerek içti.','“Sıcak” burada ısısı yüksek anlamında, gerçek anlamdadır.','dikkat'),
       ('Masadaki “ağır” kutuyu iki kişi kaldırdı.','“Ağır”, ağırlığı çok olan anlamında gerçektir.','dikkat'),
       ('Bahçedeki “yaşlı” ağacın gölgesine oturduk.','“Yaşlı”, uzun yıllardır var olan ağaç için gerçek anlamda kullanılmıştır.','dikkat'),
       ('Eski evin “kırık” camını tamir ettirdi.','“Kırık”, bütünlüğü bozulmuş cam için gerçek anlamdadır.','dikkat')],
  istenen='Mecaz anlamlı kullanılan sözcük.',ip=['Sözcüğü gerçek anlamıyla düşün: dokunulabilir ya da ölçülebilir mi?','Bakışın soğukluğu, termometreyle ölçülür mü?','Benzetme yoluyla başka bir kavrama aktarılmış sözcüğü ara.'],
  bilgi=[B_GM],
  adim=[AD('Gerçek anlamı hatırla','“Soğuk”, gerçek anlamda sıcaklığı düşük olan şey için kullanılır.','soğuk = sıcaklığı düşük'),AD('Cümleleri tek tek oku','A, B, C ve E’deki sözcükler (sıcak, ağır, yaşlı, kırık) somut nesnelerin özelliğini anlatıyor.','A, B, C, E: gerçek anlam'),AD('Mecazı yakala','“Soğuk bakış” sıcaklık değil, ilgisizlik ya da tepkisizlik anlatır; benzetmeyle aktarılmıştır.','D: mecaz')],
  puf='Sözcüğü nesne olarak ölçemiyor, dokunamıyorsan ve duyguyu ya da durumu anlatıyorsa mecazdır.'),
 dict(metin='Aşağıdakilerden hangisinde tırnak içindeki sözcük mecaz anlamda kullanılmıştır?',
  dogru='Müdürün “sert” sözleri herkesi susturdu.',harf='A',
  yan=[('Kapının “kalın” demir kolunu çevirdi.','“Kalın”, kalınlığı fazla olan demir kol için gerçek anlamdadır.','dikkat'),
       ('Sepetteki “taze” ekmeği masaya koydu.','“Taze”, yeni pişmiş ekmek için gerçek anlamdadır.','dikkat'),
       ('Çocuk “uzun” merdivenden dikkatle indi.','“Uzun”, boyu fazla olan merdiven için gerçek anlamdadır.','dikkat'),
       ('Bahçedeki “kuru” otları topladık.','“Kuru”, suyu çekilmiş otlar için gerçek anlamdadır.','dikkat')],
  istenen='Mecaz anlamlı kullanılan sözcük.',ip=['Hangi sözcük, dokunulabilen bir özelliği değil bir duyguyu ya da etkiyi anlatıyor?','Sözlerin “sertliği” elle ölçülür mü?','Gerçek anlamlı olanları teker teker ele.']))

# 0002 mecaz · zor
Q.ekle('0002','K-SZA-01','zor','Aynı sözcüğün mecaz anlamlı kullanımları arasında gerçek anlamlı olanı bulur.','düz',4,
 dict(metin='Aşağıdaki cümlelerin hangisinde tırnak içindeki sözcük, diğerlerinden farklı olarak gerçek anlamıyla kullanılmıştır?',
  dogru='Kekin “kokusunu” bütün ev duydu.',harf='B',
  yan=[('Bu işin “kokusunu” önceden almıştım.','Burada “koku almak”, sezmek demektir; mecaz anlamdadır.','bilgi'),
       ('Konuşmanın “tadı” bir anda kaçtı.','Tat burada keyif, hoşluk anlamındadır; mecazdır.','bilgi'),
       ('Odada “ağır” bir sessizlik vardı.','Sessizliğin ağırlığı ölçülemez; “ağır” mecaz anlamdadır.','dikkat'),
       ('Söyledikleri onun “kalbini” kırdı.','“Kalp kırmak” incitmek demektir; mecazdır.','dikkat')],
  istenen='Gerçek anlamlı kullanılan sözcük.',ip=['Soru “diğerlerinden farklı olarak gerçek” diyor; dört şık mecaz, biri gerçek.','Koku bu cümlede duyularla algılanıyor mu, yoksa bir sezgiyi mi anlatıyor?','Aynı sözcüğün iki cümlesini karşılaştır: biri duyu, diğeri sezgi.'],
  bilgi=[B_GM],
  adim=[AD('Sözcükleri eşle','Beş cümlede beş farklı sözcük var: koku, tat, ağır, kalp.','sözcük listesi'),AD('Mecazları ele','Koku almak (sezmek), tadı kaçmak (keyfi bozulmak), ağır sessizlik, kalp kırmak mecazdır.','A, C, D, E: mecaz'),AD('Gerçek olanı seç','B’deki “koku” burnun algıladığı gerçek bir duyudur.','B: gerçek anlam')],
  puf='Olumsuz ya da “farklı olan” köklerinde önce mecazları işaretle; geriye kalan gerçek anlamlıdır.'),
 dict(metin='Aşağıdaki cümlelerden hangisinde tırnak içindeki “ışık” sözcüğü, ötekilerden ayrı olarak somut anlamıyla kullanılmıştır?',
  dogru='Perdenin aralığından giren “ışık” duvara çizgi çizdi.',harf='C',
  yan=[('Bu haber, çıkmazdaki işimize “ışık” tuttu.','“Işık tutmak”, yol göstermek anlamında mecazdır.','bilgi'),
       ('Onun gelişi bu soğuk evimize “ışık” getirdi.','Burada ışık, neşe ve umut anlamında mecazdır.','bilgi'),
       ('Öğretmenin sözleri gençlere yol gösteren bir “ışık” oldu.','Burada ışık, rehber anlamında mecazdır.','dikkat'),
       ('Bu keşif, bilim dünyasına yeni bir “ışık” saçtı.','Burada ışık, yenilik ve aydınlanma anlamında mecazdır.','dikkat')],
  istenen='Gerçek anlamlı kullanılan sözcük.',ip=['Beş cümlede aynı sözcük var; hangisinde göz ışığı gerçekten görüyor?','Neşe, umut, rehber gibi anlamlar mecazdır.','Fiziksel ışığı anlatan tek cümleyi bul.']))

# 0003 eş/zıt · orta
Q.ekle('0003','K-SZA-02','orta','Sözcük çiftlerinin anlam ilişkisini ayırt eder.','düz',3,
 dict(metin='Aşağıdaki sözcük çiftlerinden hangisi anlam ilişkisi bakımından diğerlerinden farklıdır?',
  dogru='titiz – özenli',harf='E',
  yan=[('bolluk – kıtlık','Zıt anlamlı çifttir; dört çiftin ortak ilişkisidir, farklı olan değildir.','dikkat'),
       ('kalıcı – geçici','Zıt anlamlı çifttir; ortak ilişkiyi taşır.','dikkat'),
       ('sade – süslü','Zıt anlamlı çifttir; ortak ilişkiyi taşır.','dikkat'),
       ('tutumlu – savurgan','Zıt anlamlı çifttir; ortak ilişkiyi taşır.','dikkat')],
  istenen='Anlam ilişkisi diğerlerinden farklı olan çift.',ip=['Her çiftin yakın mı, zıt mı olduğunu yaz.','Dört çift aynı ilişkiyi taşıyor; birisi farklı.','Hangi çiftin sözcükleri birbirine yakın anlamlı?'],
  bilgi=[B_ESZ],
  adim=[AD('Çiftleri sınıfla','Her çiftin ilişkisini yaz: bolluk–kıtlık zıt, kalıcı–geçici zıt, sade–süslü zıt, tutumlu–savurgan zıt.','4 çift: zıt'),AD('Beşinciye bak','Titiz ile özenli birbirine yakın anlamlı sözcüklerdir.','titiz ≈ özenli'),AD('Farklı olanı seç','Dördü zıt, biri yakın anlamlı olduğu için E farklıdır.','E: cevap')],
  puf='“Farklı olan” sorularında önce çoğunluğun ilişkisini bul, sonra o ilişkiye uymayanı seç.'),
 dict(metin='Verilen çiftlerden hangisinin sözcükleri arasındaki ilişki, diğer dört çiftten ayrılmaktadır?',
  dogru='yoksul – zengin',harf='B',
  yan=[('güçlü – kuvvetli','Yakın anlamlı bir çifttir; diğerleriyle aynı ilişkiyi taşır.','dikkat'),
       ('kahraman – yiğit','Yakın anlamlı bir çifttir; ortak ilişkiyi taşır.','dikkat'),
       ('tasa – kaygı','Yakın anlamlı bir çifttir; ortak ilişkiyi taşır.','dikkat'),
       ('sakin – dingin','Yakın anlamlı bir çifttir; ortak ilişkiyi taşır.','dikkat')],
  istenen='Anlam ilişkisi diğerlerinden farklı olan çift.',ip=['Dört çiftin ortak noktasını bul.','Hangi çiftte sözcükler birbirinin karşıtı?','Karşıtlık, çoğunluğun ilişkisinden farklı mı?']))

# 0004 eş/zıt · orta
Q.ekle('0004','K-SZA-02','orta','Cümlede tırnak içindeki sözcüklerin yakın anlamlı olanını bulur.','düz',3,
 dict(metin='Aşağıdaki cümlelerin hangisinde tırnak içindeki iki sözcük birbirine yakın anlamlıdır?',
  dogru='Yağışlar “fazla” olunca tarlalar “bol” ürün verdi.',harf='A',
  yan=[('Bahçıvan “genç” fidanları “eski” bahçeye diktiler.','Genç ile eski anlamca karşıttır; yakın anlamlı değildir.','bilgi'),
       ('Bizi “sevinçle” karşılayıp “üzüntüyle” uğurladılar.','Sevinç ile üzüntü karşıt anlamlıdır.','bilgi'),
       ('Dün “uzak” köyden “yakın” kasabaya indik.','Uzak ile yakın zıt anlamlıdır.','dikkat'),
       ('Sabah “erken” kalkan akşam “yorgun” düşer.','Erken ile yorgun arasında anlam yakınlığı yoktur.','dikkat')],
  istenen='Tırnak içindeki iki sözcüğün yakın anlamlı olduğu cümle.',ip=['Her cümledeki iki sözcüğün ilişkisini belirle: yakın, zıt ya da ilgisiz.','Zıt çiftleri eleyince geriye ne kalıyor?','“Bol” sözcüğüne “fazla” sözcüğü ne kadar yakın?'],
  bilgi=[B_ESZ],
  adim=[AD('Çiftleri belirle','Her cümlede tırnak içindeki iki sözcüğe bak.','5 çift'),AD('İlişkiyi adlandır','B, C ve D çiftleri zıt, E çifti ilgisiz.','B, C, D, E: yakın değil'),AD('Yakın anlamlıyı bul','“Fazla” ile “bol” miktar bakımından birbirine yakın sözcüklerdir.','A: doğru')],
  puf='Cümledeki iki sözcüğü yan yana yazıp “bunlar aynı şeyi mi, karşıtı mı söylüyor?” diye sor.'),
 dict(metin='Aşağıdakilerden hangisinde tırnak içindeki iki sözcük birbirine yakın anlamlıdır?',
  dogru='“Zorlu” bir yolculuk, “çetin” bir sınav gibiydi.',harf='E',
  yan=[('“Büyük” bir sevinçle “ufak” bir odaya girdi.','Büyük ile ufak karşıt anlamlıdır.','bilgi'),
       ('“Sessiz” sokakta “gürültülü” bir araç geçti.','Sessiz ile gürültülü karşıt anlamlıdır.','bilgi'),
       ('“Dün” gördüğü rüya “bugün” aklından çıkmadı.','Dün ile bugün zaman bakımından ayrı sözcüklerdir; yakın anlamlı değildir.','dikkat'),
       ('“Yeni” kitabı “eski” rafa dikkatle koydu.','Yeni ile eski karşıt anlamlıdır.','dikkat')],
  istenen='Tırnak içindeki iki sözcüğün yakın anlamlı olduğu cümle.',ip=['Her cümledeki iki sözcüğü yan yana koy.','Karşıtlık kuranları ele.','Hangi çiftte iki sözcük de “güçlüğü” anlatıyor?']))

# 0005 çok anlam · kolay
Q.ekle('0005','K-SZA-03','kolay','Çok anlamlı bir sözcüğün hangi cümlede verilen anlamda kullanıldığını bulur.','düz',2,
 dict(metin='“Çocuk, ağır bir kutuyu taşıyamadı.” cümlesindeki “ağır” sözcüğüyle aynı anlamda kullanılmış “ağır” sözcüğü aşağıdakilerden hangisinde vardır?',
  dogru='Valizi o kadar ağırdı ki yerinden oynatamadık.',harf='C',
  yan=[('Ağır bir hastalıktan yeni kurtulmuştu.','Burada “ağır”, şiddetli, tehlikeli anlamındadır; ağırlığı çok olan demek değildir.','bilgi'),
       ('Ağır ağır merdiveni çıktı.','Burada “ağır ağır”, yavaş yavaş anlamındadır.','bilgi'),
       ('Ağır sözlerinden sonra özür diledi.','Burada “ağır”, incitici, kırıcı anlamındadır.','dikkat'),
       ('Ağırbaşlı tavrıyla herkesin saygısını kazandı.','Burada “ağırbaşlı” olgun, ölçülü demektir; ağırlıkla ilgisi yoktur.','dikkat')],
  istenen='“Ağır” sözcüğünün verilen anlamda kullanıldığı cümle.',ip=['Verilen cümledeki “ağır” neyi anlatıyor: tartıda ne kadar çektiğini mi?','Her şıkta “ağır” sözcüğünün karşılığını başka bir sözcükle yaz.','Yük, valiz gibi somut nesne anlatan cümleyi ara.'],
  bilgi=[B_CA],
  adim=[AD('Örnekteki anlamı bul','“Ağır kutu” ağırlığı çok olan kutudur.','ağır = ağırlığı çok'),AD('Şıkları karşılaştır','A şiddetli, B yavaş, D kırıcı, E olgun anlamındadır.','A, B, D, E: farklı anlam'),AD('Aynı anlamı seç','C’de valiz ağırlığı çok olduğu için yerinden oynatılamıyor.','C: doğru')],
  puf='Çok anlamlı sözcük sorularında sözcüğü her cümlede başka bir sözcükle değiştirip anlamı karşılaştır.'),
 dict(metin='“Hasan, yokuşu çıkınca soluklandı.” cümlesindeki “çıkmak” sözcüğüyle aynı anlamda kullanılmış “çıkmak” sözcüğü aşağıdakilerden hangisinde vardır?',
  dogru='Çocuk merdivenleri koşarak çıktı.',harf='A',
  yan=[('Gömleğe bulaşan leke bir türlü çıkmadı.','Burada “çıkmak”, silinip gitmek anlamındadır.','bilgi'),
       ('Yeni dergi her ay düzenli olarak çıkıyor.','Burada “çıkmak”, yayımlanmak anlamındadır.','bilgi'),
       ('Kitabın sonunda beklenmedik bir sürpriz çıktı.','Burada “çıkmak”, ortaya çıkmak anlamındadır.','dikkat'),
       ('Evden çıktığında yağmur başlamıştı.','Burada “çıkmak”, dışarı gitmek anlamındadır.','dikkat')],
  istenen='“Çıkmak” sözcüğünün verilen anlamda kullanıldığı cümle.',ip=['Verilen cümlede “çıkmak” aşağıdan yukarıya doğru gitmeyi anlatıyor.','Her şıkta “çıkmak” yerine başka bir fiil koy.','Yukarı doğru hareket eden cümleyi ara.']))

# 0006 çok anlam · orta
Q.ekle('0006','K-SZA-03','orta','Cümle çiftlerinde çok anlamlı sözcüğün aynı anlamda kullanılıp kullanılmadığını belirler.','düz',3,
 dict(metin='Aşağıdaki cümle çiftlerinden hangisinde tırnak içindeki sözcük her iki cümlede de aynı anlamda kullanılmıştır?',
  dogru='Bizi “sıcak” bir gülümsemeyle karşıladı. / Konuklarına her zaman “sıcak” davrandı.',harf='D',
  yan=[('Fırından “sıcak” ekmek çıktı. / “Sıcak” bir ilişkiyle birbirine bağlandılar.','İlkinde “sıcak” ısısı yüksek, ikincisinde samimi anlamındadır.','bilgi'),
       ('“Sıcak” haberi ilk o duydu. / Yaz günlerinin “sıcak” havası bunalttı.','İlkinde “sıcak” yeni, ikincisinde ısısı yüksek anlamındadır.','bilgi'),
       ('“Sıcak” çorbayı üfleyerek içti. / “Sıcak” haberleri gazeteler yazdı.','İlkinde “sıcak” ısısı yüksek, ikincisinde yeni anlamındadır.','dikkat'),
       ('Odanın “sıcak” havası uykumu getirdi. / Annesiyle “sıcak” bir sohbet etti.','İlkinde “sıcak” ısısı yüksek, ikincisinde samimi anlamındadır.','dikkat')],
  istenen='Tırnak içindeki sözcüğün iki cümlede aynı anlamda kullanıldığı çift.',ip=['Her cümlede “sıcak” sözcüğünü başka bir sözcükle değiştir: ısıtılmış, samimi, yeni.','Bir cümlede ısı, ötekinde duygu anlatan çiftleri ele.','İkisinde de aynı karşılığı veren çifti seç.'],
  bilgi=[B_CA],
  adim=[AD('Anlamları listele','“Sıcak”: ısısı yüksek, samimi ve yeni (haber) anlamlarında kullanılabilir.','sıcak: ısı / samimi / yeni'),AD('Çiftleri sına','A ısı–samimi, B yeni–ısı, C ısı–yeni, E ısı–samimi: anlam farklı.','A, B, C, E: farklı'),AD('Aynı anlamlıyı seç','D’de iki cümlede de “sıcak” samimi, içten demektir.','D: doğru')],
  puf='Çift sorularında her cümledeki sözcüğün karşılığını yan yana yaz; karşılıklar aynıysa anlam aynıdır.'),
 dict(metin='Aşağıdakilerin hangisinde, tırnak içinde verilen sözcük iki cümlede de aynı anlamı taşımaktadır?',
  dogru='Misafirlerine “tatlı” bir dille hitap etti. / Çocuğuna “tatlı” sözlerle öğüt verdi.',harf='C',
  yan=[('Çaya “tatlı” bir şeyler ekledi. / Küçük kızın “tatlı” gülüşü herkesi etkiledi.','İlkinde “tatlı” şekerli, ikincisinde sevimli anlamındadır.','bilgi'),
       ('Kuyudan “tatlı” su çıktı. / “Tatlı” bir uykuya daldı.','İlkinde “tatlı” tuzsuz, ikincisinde rahat, hoş anlamındadır.','bilgi'),
       ('Tezgâhta “tatlı” kurabiyeler satılıyordu. / “Tatlı” bir sohbetle yolu kısalttık.','İlkinde “tatlı” şekerli, ikincisinde hoş, keyifli anlamındadır.','dikkat'),
       ('“Tatlı” su balıkları akvaryumda yaşıyor. / Yeni gelen komşular çok “tatlı” insanlar.','İlkinde “tatlı” tuzsuz, ikincisinde sevimli anlamındadır.','dikkat')],
  istenen='Tırnak içindeki sözcüğün iki cümlede aynı anlamda kullanıldığı çift.',ip=['“Tatlı” sözcüğü şekerli, tuzsuz ya da hoş anlamında olabilir.','Her cümledeki karşılığı yaz.','Her iki cümlede de “yumuşak, hoş” anlamı veren çifti bul.']))

# 0007 ilişki · orta
Q.ekle('0007','K-SZA-04','orta','Sözcük gruplarında üst anlamlı sözcüğü bulur.','düz',3,
 dict(metin='Aşağıdaki sözcük gruplarının hangisinde sözcüklerden biri, diğerlerinin üst anlamlısıdır?',
  dogru='lale – gül – karanfil – çiçek',harf='B',
  yan=[('elma – armut – kiraz – şeftali','Dört sözcük de birer meyve türüdür; birini kapsayan bir sözcük yoktur.','bilgi'),
       ('kırmızı – mavi – sarı – yeşil','Dört sözcük de birer renktir; aralarında kapsayan sözcük yoktur.','bilgi'),
       ('koşmak – yürümek – sıçramak – zıplamak','Dört fiil aynı düzeyde hareket bildirir; kapsayıcı bir sözcük yok.','dikkat'),
       ('kalem – silgi – defter – cetvel','Dört sözcük de birer araç gereçtir; birini kapsayan sözcük grupta yok.','dikkat')],
  istenen='Üst anlamlı sözcüğün bulunduğu grup.',ip=['Üst anlamlı sözcük, diğerlerinin hepsini kapsar.','Her grupta “şunların hepsi bir …’dır” cümlesini kurmayı dene.','Gül, lale, karanfil birer ... midir?'],
  bilgi=[B_IL],
  adim=[AD('Grupları incele','Her grupta dört sözcük var; biri diğerlerini kapsıyor mu?','4 sözcüklü gruplar'),AD('Kapsayan sözcüğü ara','A, C, D ve E’de hepsi aynı düzeyde sözcükler. B’de “çiçek” gül, lale ve karanfili kapsar.','B: çiçek = üst anlam'),AD('Doğrula','Gül, lale, karanfil çiçektir; her çiçek gül değildir.','B: doğru')],
  puf='Üst anlam testi: “X bir Y’dir” cümlesi kurulup tersi doğru değilse Y üst anlamlıdır (gül bir çiçektir; çiçek bir gül değildir).'),
 dict(metin='Hangi sözcük grubunda bir sözcük, birlikte verilen diğer üç sözcüğün tamamını kapsar?',
  dogru='keman – gitar – piyano – çalgı',harf='D',
  yan=[('Ankara – İzmir – Bursa – Adana','Dört sözcük de birer şehir adıdır; birini kapsayan sözcük yoktur.','bilgi'),
       ('bakır – demir – altın – gümüş','Dört sözcük de birer madendir; aralarında kapsayan sözcük yok.','bilgi'),
       ('yaz – kış – ilkbahar – sonbahar','Dört sözcük de birer mevsimdir; kapsayan sözcük yok.','dikkat'),
       ('mavi – yeşil – turuncu – mor','Dört sözcük de birer renk adıdır; kapsayan sözcük yok.','dikkat')],
  istenen='Üst anlamlı sözcüğün bulunduğu grup.',ip=['Üst anlamlı sözcük diğerlerinin hepsini içine alır.','Her grupta dördünü birden kapsayan bir sözcük var mı?','Keman, gitar, piyano nedir?']))

# 0008 ilişki · zor
Q.ekle('0008','K-SZA-04','zor','Verilen sözcük çiftindeki ilişkinin türünü ve yönünü koruyan çifti bulur.','düz',4,
 dict(metin='“Tekerlek – araba” sözcükleri arasındaki ilişki (parça–bütün), aşağıdaki sözcük çiftlerinden hangisinde vardır?',
  dogru='sayfa – kitap',harf='B',
  yan=[('kütüphane – kitap','İlişki bütün–parça biçimindedir; yönü ters olduğu için verilen ilişkiden farklıdır.','dikkat'),
       ('öğretmen – okul','Meslek–çalışma yeri ilişkisi vardır; parça–bütün değildir.','bilgi'),
       ('kalem – yazı','Araç–ürün ilişkisi vardır; kalem yazının parçası değildir.','bilgi'),
       ('buğday – ekmek','Hammadde–ürün ilişkisi vardır; buğday ekmeğin parçası olarak anılmaz.','bilgi')],
  istenen='Verilen çiftle aynı ilişkiyi taşıyan çift.',ip=['Çiftte önce parça, sonra bütün gelir.','Her şıkta ilişkinin türünü (parça–bütün, meslek–yer, araç–ürün) adlandır.','Yönü ters olan çifti ele.'],
  bilgi=[B_IL],
  adim=[AD('Örnek ilişkiyi çöz','“Tekerlek – araba”: tekerlek arabanın parçasıdır.','parça → bütün'),AD('Yönü kontrol et','İlişki “parça önce, bütün sonra” biçimindedir.','yön: parça–bütün'),AD('Şıkları ele','A bütün–parça (yönü ters), C meslek–yer, D araç–ürün, E hammadde–ürün. B’de sayfa, kitabın parçasıdır.','B: doğru')],
  puf='Sözcük çifti sorularında ilişkinin türünü kadar yönünü de kontrol et; “parça–bütün” ile “bütün–parça” farklıdır.'),
 dict(metin='“Parmak – el” sözcükleri arasındaki ilişki (parça–bütün), aşağıdaki sözcük çiftlerinden hangisinde vardır?',
  dogru='tuş – klavye',harf='A',
  yan=[('ekmek – fırın','Ürün–yer ilişkisi vardır; ekmek fırının parçası değildir.','bilgi'),
       ('oduncu – balta','Meslek–araç ilişkisi vardır; parça–bütün değildir.','bilgi'),
       ('kalem – yazmak','Araç–işlev ilişkisi vardır; kalem yazmanın parçası değildir.','dikkat'),
       ('doktor – hastane','Meslek–çalışma yeri ilişkisi vardır.','dikkat')],
  istenen='Verilen çiftle aynı ilişkiyi taşıyan çift.',ip=['Parmak elin neyidir?','Her çiftin ilişkisini adlandır.','Parçayı önce, bütünü sonra veren çifti bul.']))

Q.bitir()
