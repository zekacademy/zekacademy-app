"""TYT Türkçe · Yazım Kuralları: 6 ana + 6 kardeş. Cümleler özgündür; kurallar TDK güncel yazım kılavuzuna göredir."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from tr_ortak import *
from collections import defaultdict
AD=A
def ad3(k,kb,a,ab,s,sb,t=('Kuralı hatırla','Şıkları tek tek ele','Sonucu seç')):
    return [AD(t[0],k,kb),AD(t[1],a,ab),AD(t[2],s,sb)]
KARTLAR={
 'K-YZ-01':dict(alt='de/da Yazımı',fikir='Bağlaç olan “de/da”nın ayrı, bulunma hâli eki olan “-de/-da”nın bitişik yazıldığını ayırt etmek.',tuzak='“Bende, sende” gibi ek görünümlü yazımları “ben de, sen de” anlamında doğru saymak.',zorluk='kolay',kalip='düz',adim=2,tipId='yz-deda',kaynak='ÖSYM TYT Türkçe 2018–2026 (yazım kuralları: de/da)'),
 'K-YZ-02':dict(alt='ki Yazımı',fikir='Bağlaç “ki”nin ayrı, aitlik eki “-ki”nin bitişik yazımını ve “dünkü, bugünkü” gibi ünlü uyumuna uyan biçimleri ayırt etmek.',tuzak='“Sınıftaki, benimki” gibi ek olan “ki”yi ayırmak; “dünki” yazmak.',zorluk='orta',kalip='düz',adim=3,tipId='yz-ki',kaynak='ÖSYM TYT Türkçe 2018–2026 (yazım kuralları: ki)'),
 'K-YZ-03':dict(alt='Bitişik ve Ayrı Yazılan Sözcükler',fikir='“Herkes, hiçbir, birçok, birkaç” gibi bitişik; “her şey, bu yüzden, kendi kendine” gibi ayrı yazılan sözcükleri ayırt etmek.',tuzak='“Her şey”i “herşey”, “hiçbir”i “hiç bir” yazmak.',zorluk='orta',kalip='düz',adim=3,tipId='yz-bitisik',kaynak='ÖSYM TYT Türkçe 2018–2026 (yazım kuralları: birleşik sözcükler)'),
 'K-YZ-04':dict(alt='Büyük Harflerin Kullanımı',fikir='Özel adların, dil ve kıta/deniz adlarının, unvan ve eser adlarının büyük; cins adların küçük harfle yazıldığını bilmek.',tuzak='Dil adlarını (İngilizce) ve “Güney Amerika” gibi özel adları küçük yazmak.',zorluk='orta',kalip='düz',adim=3,tipId='yz-buyuk',kaynak='ÖSYM TYT Türkçe 2018–2026 (yazım kuralları: büyük harf)'),
 'K-YZ-05':dict(alt='Kesme İşareti',fikir='Özel adlara ve sayılara gelen çekim eklerinden önce kesme konduğunu; türetme eklerinden (-lı, -çı, -çe) önce konmadığını ayırt etmek.',tuzak='“Ankaralı, Türkçe, Atatürkçü” gibi türemiş sözcüklerde kesme kullanmak.',zorluk='zor',kalip='öncüllü',adim=4,tipId='yz-kesme',kaynak='ÖSYM TYT Türkçe 2018–2026 (yazım kuralları: kesme işareti)'),
 'K-YZ-06':dict(alt='Birleşik Fiillerin Yazımı',fikir='Yardımcı fiille kurulan birleşik fiillerde ses olayı varsa bitişik (affetmek), yoksa ayrı (kabul etmek) yazıldığını bilmek.',tuzak='“Kabul etmek, teslim etmek” gibi ses olayı olmayanları bitişik yazmak.',zorluk='zor',kalip='düz',adim=4,tipId='yz-birlesikfiil',kaynak='ÖSYM TYT Türkçe 2018–2026 (yazım kuralları: birleşik fiiller)'),
}
TIPLER={'yz-deda':'de/da yazımı','yz-ki':'ki yazımı','yz-bitisik':'Bitişik ve ayrı yazılan sözcükler','yz-buyuk':'Büyük harflerin kullanımı','yz-kesme':'Kesme işareti','yz-birlesikfiil':'Birleşik fiillerin yazımı'}
Q=Konu('yazim','Yazım Kuralları','tr|Yazım Kuralları',KARTLAR,TIPLER); Q.KADIM=defaultdict(lambda:None)
B_DE=B('de/da','Bağlaç olan “de/da” (anlamı “dahi, ayrıca”) ayrı yazılır: “Sen de gel”. Bulunma hâli eki “-de/-da” sözcüğe bitişiktir: “Evde kaldım”. Deneme: “de/da”yı çıkarınca anlam bozulmuyorsa bağlaçtır')
B_KI=B('ki','Bağlaç olan “ki” ayrı yazılır: “O kadar yoruldum ki uyuyakaldım”. Aitlik eki “-ki” bitişiktir: “evdeki, benimki”. Ünlü uyumuna uyan tek istisna: dünkü, bugünkü, öbürkü')
B_BIT=B('Bitişik ve ayrı sözcükler','Bitişik: herkes, hiçbir, birçok, birkaç, neyse. Ayrı: her şey, bir şey, bu yüzden, kendi kendine, her zaman')
B_BUY=B('Büyük harf','Özel adlar, dil adları (Türkçe, İngilizce), kıta-deniz-yer adları (Güney Amerika, Karadeniz), eser adları ve unvanlar büyük harfle başlar; cins adlar (şehir, roman, deniz) küçük yazılır')
B_KES=B('Kesme işareti','Özel adlara ve sayılara gelen çekim ekleri kesmeyle ayrılır: Ayşe’nin, 1980’li, 17.30’da. Türetme eki alan sözcüklerde kesme olmaz: Ankaralı, Türkçe, Atatürkçü')
B_BF=B('Birleşik fiil yazımı','et-, ol- gibi yardımcı fiillerde ses olayı (düşme, ikizleşme) varsa bitişik yazılır: affetmek, hissetmek, reddetmek. Ses olayı yoksa ayrı: kabul etmek, teslim etmek')

# 0001 de/da · kolay
Q.ekle('0001','K-YZ-01','kolay','“de/da” bağlacı ile bulunma hâli ekini yazımda ayırt eder.','düz',2,
 dict(metin='Aşağıdaki cümlelerin hangisinde “de/da” yazımıyla ilgili bir yanlışlık vardır?',harf='C',
  dogru='Bu konuyu bende anlamadım, biraz daha anlatır mısın?',
  yan=[('Hasta olduğu için gelemedi, bir de yağmur başlayınca iyice zorlaştı.','“Bir de” bağlaçtır, ayrı yazılması doğrudur.','bilgi'),
       ('Defterini sınıfta unutmuş, çantasında da bulamamış.','“Sınıfta” ek, “çantasında da” bağlaçtır; yazım doğrudur.','dikkat'),
       ('Yarın sen de bizimle gel, ben de gelirim.','“Sen de, ben de” bağlaçtır, ayrı yazılması doğrudur.','bilgi'),
       ('Çok çalıştı da yine de başaramadı.','“Çalıştı da” ve “yine de” bağlaçtır; ayrı yazılmıştır.','dikkat')],
  istenen='“de/da” yazımı yanlış olan cümle.',ip=['“de/da”yı çıkarınca anlam bozuluyorsa ek, bozulmuyorsa bağlaçtır.','“Ben de anlamadım” mı demek istiyor, “bende” mi?','Anlamı “ben dahi” olan “de”, ayrı yazılır.'],
  bilgi=[B_DE],adim=ad3('Bağlaç “de/da” ayrı, ek “-de/-da” bitişik yazılır.','“dahi” anlamı varsa bağlaç','A: bağlaç ✓ · B: “sınıfta” ek, “çantasında da” bağlaç ✓ · C: “ben de” olmalı ✗ · D: ✓ · E: ✓','C: yanlış','“Bende anlamadım” cümlesinde “ben de” anlamı vardır; bağlaç ayrı yazılmalıydı.','C: ben de anlamadım'),
  puf='“Dahi” sözcüğünü koyabiliyorsan “de/da” bağlaçtır ve ayrı yazılır.'),
 dict(metin='Aşağıdaki cümlelerin hangisinde “de/da” yazımı doğrudur?',harf='A',
  dogru='Ben de sizinle gelmek istiyorum.',
  yan=[('Hem çalışıyor hemde okuyor.','“Hem de” bağlaç grubudur, ayrı yazılmalıydı.','bilgi'),
       ('Pazar günü kütüphaneye gideceğim, sende gelir misin?','“Sen de gelir misin?” anlamı vardır; bağlaç ayrı yazılmalıydı.','dikkat'),
       ('Yemekte ne varda soruyorsun?','“Ne var da” biçiminde bağlaç ayrı yazılır.','bilgi'),
       ('Kapıda bekleyen çocuğada bir şey verdi.','“Çocuğa da” anlamındaki bağlaç ayrı yazılmalıydı.','dikkat')],
  istenen='“de/da” yazımı doğru olan cümle.',ip=['“Dahi” sözcüğünü koyabildiğin yerde “de/da” ayrı yazılır.','Şıklarda bitişik yazılmış bağlaçları ara.','Yalnızca bir şıkta bağlaç ayrı yazılmıştır.'],
  puf=None))

# 0002 ki · orta
Q.ekle('0002','K-YZ-02','orta','Bağlaç “ki” ile aitlik ekini ve “dünkü” gibi istisnaları yazımda ayırt eder.','düz',3,
 dict(metin='Aşağıdaki cümlelerin hangisinde “ki” yazımıyla ilgili bir yanlışlık vardır?',harf='E',
  dogru='Sınıftaki öğrencilerin çoğu dünki sınavı zor bulmuş.',
  yan=[('Bugünkü toplantı yarına ertelendi.','“Bugünkü” ünlü uyumuna uyan istisnadır; yazım doğrudur.','bilgi'),
       ('O kadar yorgunum ki oturur oturmaz uyuyakalırım.','Bağlaç olan “ki” ayrı yazılmıştır; doğrudur.','dikkat'),
       ('Çantandaki kalemi bana verir misin?','Aitlik eki “-ki” bitişik yazılmıştır; doğrudur.','bilgi'),
       ('Benim fikrimle seninki aynı.','“Seninki” aitlik ekidir, bitişik yazılması doğrudur.','dikkat')],
  istenen='“ki” yazımı yanlış olan cümle.',ip=['Aitlik eki “-ki” genelde ünlü uyumuna uyar.','“Dün” sözcüğüne gelen ekin doğru biçimini düşün.','“Sınıftaki” sözcüğünü cümleden çıkarmadan, ek mi bağlaç mı olduğuna bak.'],
  bilgi=[B_KI],adim=ad3('Aitlik eki “-ki” bitişik, bağlaç “ki” ayrı yazılır; “dünkü, bugünkü” ünlü uyumuna uyar.','“-ki” istisnaları: dünkü, bugünkü','A: bugünkü ✓ · B: bağlaç ✓ · C: çantandaki ✓ · D: seninki ✓ · E: “dünki” ✗','E: yanlış','“Dünki” değil, “dünkü” yazılır.','E: dünkü olmalıydı'),
  puf='Dün, bugün, öbür sözcüklerine gelen “-ki” ünlü uyumuna uyar: dünkü, bugünkü, öbürkü.'),
 dict(metin='Aşağıdaki cümlelerin hangisinde “ki” sözcüğünün yazımı doğrudur?',harf='B',
  dogru='Evdeki herkes uyurken ben kitabımı okudum.',
  yan=[('Sınıfta ki öğrenciler yeni gelen öğretmeni karşıladı.','Aitlik eki olan “-ki”, “sınıftaki” biçiminde bitişik yazılmalıydı.','bilgi'),
       ('Annemin evi benim kinden daha büyük.','“Benimkinden” sözcüğünde ek bitişik yazılır.','bilgi'),
       ('Bende ki kitabı sana vermeyi unutmuşum.','“Bendeki” sözcüğü bitişik yazılmalıydı.','dikkat'),
       ('Dün ki konuşmayı hatırlıyor musun?','“Dünkü” bitişik yazılır; ayrı yazılması yanlıştır.','dikkat')],
  istenen='“ki” yazımı doğru olan cümle.',ip=['Bir yer ya da zaman bildiren sözcüğe gelen “-ki” bitişiktir.','Yanlış şıklarda “ki” gereksiz yere ayrılmış.','“Evdeki” sözcüğünün yazımını sınayın.'],
  puf=None))

# 0003 bitişik/ayrı · orta
Q.ekle('0003','K-YZ-03','orta','“Hiçbir, herkes, birkaç, her şey” gibi sözcüklerin bitişik/ayrı yazımını ayırt eder.','düz',3,
 dict(metin='Aşağıdaki cümlelerin hangisinde bitişik ya da ayrı yazımla ilgili bir yanlışlık vardır?',harf='A',
  dogru='Bu konuda hiç bir fikrim yok.',
  yan=[('Her şeyi baştan yapmamız gerekecek.','“Her şey” ayrı yazılmıştır; doğrudur.','bilgi'),
       ('Birkaç arkadaşımla sinemaya gittim.','“Birkaç” bitişik yazılır; doğrudur.','dikkat'),
       ('Çocuk kendi kendine yürümeyi öğrendi.','“Kendi kendine” ayrı yazılır; doğrudur.','bilgi'),
       ('Hava kapalı olduğu için maç ertelendi.','Ayrı yazılması gereken sözcükler ayrı yazılmıştır.','dikkat')],
  istenen='Bitişik/ayrı yazımı yanlış olan cümle.',ip=['“Hiç” ile “bir” birleşince tek sözcük olur.','Her şıktaki birleşik ya da ayrı sözcükleri kurala göre sına.','Yalnızca bir şıkta ayrı yazılması gereken değil, bitişik yazılması gereken sözcük var.'],
  bilgi=[B_BIT],adim=ad3('“Hiçbir” bitişik; “her şey, kendi kendine” ayrı yazılır.','hiçbir · birkaç · her şey','A: “hiç bir” ✗ · B: her şey ✓ · C: birkaç ✓ · D: kendi kendine ✓ · E: ✓','A: yanlış','“Hiç bir” bitişik yazılmalıydı: hiçbir.','A: hiçbir olmalıydı'),
  puf='Hiçbir, birçok, birkaç, herkes bitişik; her şey, bir şey, hiçbir şey ayrı yazılır.'),
 dict(metin='Aşağıdaki cümlelerin hangisinde yazım yönünden bir yanlışlık yoktur?',harf='E',
  dogru='Sınav sonuçları bu yüzden geç açıklandı.',
  yan=[('Bir çok kişi bu kararı destekledi.','“Birçok” bitişik yazılmalıydı.','bilgi'),
       ('Her kes sınav salonuna girdi.','“Herkes” bitişik yazılmalıydı.','bilgi'),
       ('Hiç bir öğrenci geç kalmadı.','“Hiçbir” bitişik yazılmalıydı.','dikkat'),
       ('Herşey yoluna girdi.','“Her şey” ayrı yazılmalıydı.','dikkat')],
  istenen='Yazımı doğru olan cümle.',ip=['Dört şıkta bitişik yazılması ya da ayrı yazılması gereken sözcükler karıştırılmış.','“Her şey” ve “herkes” aynı kural değildir.','Doğru cümlede “bu yüzden” sözcük grubu vardır.'],
  puf=None))

# 0004 büyük harf · orta
Q.ekle('0004','K-YZ-04','orta','Özel ad, dil adı ve unvanlarda büyük harf kullanımını değerlendirir.','düz',3,
 dict(metin='Aşağıdaki cümlelerin hangisinde büyük harflerin kullanımıyla ilgili bir yanlışlık vardır?',harf='D',
  dogru='Okulda ingilizce dersi bu yıl iki saate çıkarıldı.',
  yan=[('Yaz tatilinde Karadeniz’de bir hafta kalacağız.','“Karadeniz” özel addır, büyük harfle yazılmıştır.','bilgi'),
       ('Prof. Dr. Ayhan Kaya konferansı açtı.','Unvan ve özel ad büyük harfle yazılmıştır.','dikkat'),
       ('Çalıkuşu romanı Reşat Nuri Güntekin’in tanınmış eseridir.','Eser adı büyük, “romanı” cins adı küçüktür.','bilgi'),
       ('Gelecek hafta Ankara’daki toplantıya katılacağız.','“Ankara” özel addır; doğru yazılmıştır.','dikkat')],
  istenen='Büyük harf kullanımı yanlış olan cümle.',ip=['Özel adların yanında dil adlarını da incele.','Dil adları (Türkçe, Almanca…) büyük harfle başlar.','Cins adlar (roman, ders) küçük yazılır.'],
  bilgi=[B_BUY],adim=ad3('Özel adlar, dil adları ve eser adları büyük harfle başlar.','Karadeniz · İngilizce · Çalıkuşu','A: Karadeniz ✓ · B: Prof. Dr. ✓ · C: Çalıkuşu ✓ · D: “ingilizce” ✗ · E: Ankara ✓','D: yanlış','Dil adı olan “İngilizce” büyük harfle başlamalıydı.','D: İngilizce olmalıydı'),
  puf='Dil adları cümle ortasında bile büyük harfle başlar: Türkçe, Almanca, İngilizce.'),
 dict(metin='Aşağıdaki cümlelerin hangisinde büyük harf kullanımı bakımından bir yanlışlık vardır?',harf='C',
  dogru='Yaz tatilinde güney Amerika’ya gitmeyi planlıyorlar.',
  yan=[('Yarın akşam Ege Denizi kıyısında yürüyüş yapacağız.','“Ege Denizi” özel addır; doğru yazılmıştır.','dikkat'),
       ('Hasan, sabah Atatürk Bulvarı’ndan geçti.','Özel ad bulvar adının parçasıdır; doğrudur.','bilgi'),
       ('Bu yıl Cumhuriyet Bayramı kutlamaları okulda yapılacak.','Bayram adı büyük harfle yazılmıştır.','bilgi'),
       ('Dergide Tevfik Fikret’in şiirleri yayımlandı.','Kişi adı büyük yazılmış, “şiirleri” küçük kalmıştır; doğrudur.','dikkat')],
  istenen='Büyük harf kullanımı yanlış olan cümle.',ip=['Kıta adları özel addır.','Her şıkta özel adın büyük yazılıp yazılmadığına bak.','“Güney” burada yön değil, adın parçasıdır.'],
  puf=None))

# 0005 kesme · zor · öncüllü
Q.ekle('0005','K-YZ-05','zor','Çekim ekleri ile türetme eklerinin kesme işaretiyle ilişkisini değerlendirir.','öncüllü',4,
 dict(metin='I. İstanbul’lu esnaf yeni yılı karşıladı.\nII. Hatice’yle 14.00’te buluşacağız.\nIII. Çocuklar Atatürk’çü bir ortamda büyüdü.\nIV. 1990’lı yıllarda ev bilgisayarları yaygınlaştı.\nYukarıdaki numaralı cümlelerin hangilerinde kesme işareti yanlış kullanılmıştır?',harf='B',
  dogru='I ve III',
  yan=[('Yalnız I','III’te de türetme eki öncesinde kesme kullanılmış; I tek başına yetmez.','dikkat'),
       ('II ve IV','II ve IV’te kesme çekim ekinden önce kullanılmıştır; doğrudur.','bilgi'),
       ('I, II ve IV','II ve IV’ün yazımı doğrudur; III ise yanlış olduğu hâlde bu şıkta yok.','dikkat'),
       ('I, III ve IV','IV’te “1990’lı” sayıya gelen ek olduğu için kesme gerekir; yazım doğrudur.','bilgi')],
  istenen='Kesme işareti yanlış kullanılan cümleler.',ip=['Kesme işareti özel adlara gelen çekim ekleriyle sayılara gelen eklerden önce konur.','“-lı, -çı” gibi türetme eklerinden önce kesme konur mu?','Her cümlede kesme işaretinden sonra gelen eki türüne göre sınıflandır.'],
  bilgi=[B_KES],adim=[AD('Kuralı hatırla','Kesme, çekim ekinden önce konur; türetme ekinde konmaz.','Ayşe’nin · Ankaralı'),AD('I ve III’ü sına','“İstanbullu” ve “Atatürkçü” sözcüklerinde ek türetme ekidir; kesme olmaz.','I: ✗ · III: ✗'),AD('II ve IV’ü sına','“Hatice’yle” ve “14.00’te” çekim eklidir. “1990’lı” da sayıya getirilen ektir; kesme ister.','II: ✓ · IV: ✓'),AD('Sonuç','Yanlış kullanılan cümleler I ve III.','I ve III')],
  puf='İsim sözcük türetiyorsa (-lı, -çı, -ca) kesme yok; çekim ekiyse özel ad ve sayıdan sonra kesme var.'),
 dict(metin='I. Selin’in kardeşi Ayşe’yle geldi.\nII. Okula Eskişehir’li öğrenciler geldi.\nIII. Kitabı 3’üncü sayfadan okuyun.\nIV. Dersimiz Türkçe’den başlayacak.\nYukarıdaki numaralı cümlelerin hangilerinde kesme işareti yanlış kullanılmıştır?',harf='D',
  dogru='II ve IV',
  yan=[('Yalnız II','IV’te de “Türkçe’den” biçimindeki kesme yanlıştır.','dikkat'),
       ('I ve III','I ve III’te kesme çekim ekinden önce kullanılmıştır; doğrudur.','bilgi'),
       ('II ve III','III’te “3’üncü” sayıya gelen ektir; kesme doğru kullanılmıştır.','bilgi'),
       ('III ve IV','III doğru; yanlış olan II ve IV’tür.','dikkat')],
  istenen='Kesme işareti yanlış kullanılan cümleler.',ip=['Hangi sözcüklerde ek, yeni bir sözcük türetiyor?','Dil adları ve “-li” ekli yer adları türemiştir.','Sayıya gelen ek kesmeyle ayrılır.'],
  puf=None))

# 0006 birleşik fiil · zor
Q.ekle('0006','K-YZ-06','zor','Yardımcı fiille kurulan birleşik fiillerin yazımını ses olayına göre değerlendirir.','düz',4,
 dict(metin='Aşağıdaki cümlelerin hangisinde birleşik fiilin yazımı yanlıştır?',harf='C',
  dogru='Projeyi teslimetmeden önce son kez kontrol etti.',
  yan=[('Yaptığı hatayı kabul etmeyi öğrenmişti.','“Kabul etmek” ses olayı olmadığından ayrı yazılır; doğrudur.','bilgi'),
       ('Onu hiç affetmeyeceğini söyledi.','“Af” sözcüğü ikizleşir (aff-); bitişik yazılması doğrudur.','dikkat'),
       ('Önerimizi reddettiğine çok şaşırdık.','“Ret” ikizleşir (redd-); bitişik yazılması doğrudur.','bilgi'),
       ('Ondan yardım etmesini rica ettim.','“Yardım etmek” ve “rica etmek” ses olayı olmadığından ayrı yazılır.','dikkat')],
  istenen='Birleşik fiil yazımı yanlış olan cümle.',ip=['Birleşik fiilde ses düşmesi ya da ikizleşme olup olmadığına bak.','“Teslim” sözcüğüne “et-” gelince ses olayı var mı?','Ses olayı yoksa iki sözcük ayrı yazılır.'],
  bilgi=[B_BF],adim=[AD('Kuralı hatırla','Ses olayı varsa bitişik, yoksa ayrı yazılır.','affetmek · kabul etmek'),AD('Ses olaylı olanlar','“Affetmek” ve “reddetmek” ikizleşme vardır; bitişik yazım doğru.','B ✓ · D ✓'),AD('Ses olayı olmayanlar','“Kabul etmek, yardım etmek, rica etmek, teslim etmek” ses olayı olmadığından ayrı yazılır.','A ✓ · E ✓ · C: “teslimetmek” ✗'),AD('Sonuç','Yanlış yazılan birleşik fiil “teslimetmek”.','C: teslim etmek')],
  puf='Af, hiss, ret, emir gibi sözcüklerle kurulan fiillerde ses olayı vardır (bitişik); kabul, rica, teslim, tercih ayrı yazılır.'),
 dict(metin='Aşağıdaki cümlelerin hangisinde birleşik fiil yazımı yönünden bir yanlışlık vardır?',harf='A',
  dogru='Hocamız ödevlerin teslimini cuma gününe kadar kabuletti.',
  yan=[('Komutan, askerlere hemen harekete geçmelerini emretti.','“Emretmek” bitişik yazılır; doğrudur.','bilgi'),
       ('Verdiğim sözü tutamadığım için beni affet.','“Affetmek” bitişik yazılır; doğrudur.','dikkat'),
       ('Sevdiği takımın şampiyon olacağını zannediyordu.','“Zannetmek” ikizleşmeyle bitişik yazılır; doğrudur.','bilgi'),
       ('Çocuk annesine yardım etmek istedi.','“Yardım etmek” ayrı yazılır; doğrudur.','dikkat')],
  istenen='Birleşik fiil yazımı yanlış olan cümle.',ip=['Hangi birleşik fiilde ses olayı yok ama bitişik yazılmış?','Kabul sözcüğüne “et-” eklenince ses olayı var mı?','Diğer dört şıkta kural uygulanmıştır.'],
  puf=None))
Q.bitir()
