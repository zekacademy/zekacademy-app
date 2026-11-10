"""TYT Türkçe · Yazım Kuralları: 6 ana soru (hafif mod). Metinler özgündür."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from hafif_dilbilgisi import *
AD=A
KY='ÖSYM TYT Türkçe 2018–2026 (yazım kuralları) ve TDK Yazım Kılavuzu'
KARTLAR={
 'K-YAZ-01':dict(alt='De/Da Yazımı',fikir='Bağlaç olan “de/da”nın ayrı, bulunma eki “-de/-da”nın bitişik yazıldığını ayırt etmek.',tuzak='Bağlacı ek sanıp bitişik yazmak.',zorluk='kolay',kalip='düz',adim=2,tipId='yaz-deda',kaynak=KY),
 'K-YAZ-02':dict(alt='Ki ve Soru Eki “mI” Yazımı',fikir='Bağlaç “ki”nin ayrı, ilgi “-ki”nin bitişik; soru eki “mI”nın ayrı, ek-fiil “-mIş”in bitişik yazıldığını bilmek.',tuzak='İlgi zamiri “-ki”yi ayrı, soru ekini bitişik yazmak.',zorluk='orta',kalip='düz',adim=3,tipId='yaz-kimi',kaynak=KY),
 'K-YAZ-03':dict(alt='Büyük Harflerin Kullanımı',fikir='Özel adlar, unvanlar ve yer adlarındaki büyük harf kurallarını uygulamak.',tuzak='Özel adı küçük, yön adını büyük yazmak; unvanı küçük bırakmak.',zorluk='orta',kalip='düz',adim=3,tipId='yaz-buyuk',kaynak=KY),
 'K-YAZ-04':dict(alt='Sözcüklerin Yazımı',fikir='Yazılışı karıştırılan sözcüklerde (herkes, yalnız, birkaç, hiçbir, herhangi) doğru biçimi seçmek.',tuzak='Ses benzerliğine bakıp yanlış harf kullanmak; bitişik sözcüğü ayırmak.',zorluk='zor',kalip='düz',adim=4,tipId='yaz-sozcuk',kaynak=KY),
 'K-YAZ-05':dict(alt='Sayıların Yazımı',fikir='Birden çok sözcükten oluşan sayıların yazıyla ayrı yazıldığını bilmek.',tuzak='Sayıları “kırkbeş” gibi bitişik yazmak.',zorluk='zor',kalip='düz',adim=3,tipId='yaz-sayi',kaynak=KY),
}
TIPLER={'yaz-deda':'De/da yazımı','yaz-kimi':'Ki ve soru eki yazımı','yaz-buyuk':'Büyük harf kullanımı','yaz-sozcuk':'Sözcüklerin yazımı','yaz-sayi':'Sayıların yazımı'}
Q=kur('yazim','Yazım Kuralları','tr|Yazım Kuralları',KARTLAR,TIPLER); Q.n=6
Y='yanlış'; D='doğru'
B_DE=B('De/da yazımı','bağlaç “de/da” ayrı yazılır, hiçbir zaman “te/ta” olmaz, çıkarılınca cümle bozulmaz (Sen de gel) · bulunma eki “-de/-da” bitişik yazılır, “-te/-ta” olabilir (evde, kitapta)')
B_KI=B('Ki ve “mI” yazımı','bağlaç “ki” ayrı (Duydum ki geldi) · ilgi “-ki” bitişik (evdeki, seninki) · soru eki “mI” ayrı (geldi mi?) · ek-fiil “-mIş” bitişik (güzelmiş)')
B_BH=B('Büyük harf','özel adlar, unvanlar (Ahmet Bey), yer ve yapı adları (Boğaziçi Köprüsü) büyük harfle başlar · yön adları bölge bildirmiyorsa küçük yazılır (kuzeye gittik)')
B_SZ=B('Yazılışı karıştırılanlar','herkes, yalnız, birkaç, birçok, hiçbir, herhangi tek sözcüktür · herhangi bir, herhangi biri, her şey, her gün, hiç durmadan ayrı yazılır')
B_SY=B('Sayıların yazımı','yazıyla yazılan sayılar ayrı yazılır: on beş, yirmi iki, kırk beş, yüz altmış, bin dokuz yüz seksen')

# 0001 de/da · kolay · C
soru(Q,'0001','K-YAZ-01','kolay','“De/da”nın bağlaç ve bulunma eki olarak yazımını ayırt eder.',2,
 'Aşağıdaki cümlelerin hangisinde “de/da”nın yazımı yanlıştır?',
 [('Çocuk okuldan döndü, ödevini de yaptı.',D,'Bu “de” bağlaçtır (ayrıca) ve ayrı yazılmıştır; yazımı doğrudur.','dikkat'),
  ('Dün gece sinemada uzun bir film izledik.',D,'“Sinemada” sözcüğündeki “-da” bulunma ekidir; bitişik yazılması doğrudur.','bilgi'),
  ('Sabah erkenden kalktım, akşamda erken yattım.',Y,'',''),
  ('Bu işi senin de yapabileceğini düşünüyorum.',D,'Burada “de”, “bile/ayrıca” anlamlı bağlaçtır ve ayrı yazılmıştır; yazımı doğrudur.','bilgi'),
  ('Yarın da aynı saatte buluşalım.',D,'“Yarın da” ifadesinde bağlaç olan “da” ayrı yazılmıştır; yazımı doğrudur.','dikkat')],
 'C',lambda t:t==Y,'De/da yazımı yanlış olan cümle.',
 'Her “de/da”yı çıkarıp cümleyi oku; cümle bozulmuyorsa bağlaçtır ve ayrı yazılır.',[B_DE],
 [AD('Kuralı hatırla','Bağlaç “de/da” ayrı yazılır; bulunma eki “-de/-da” sözcüğe bitişik yazılır.','bağlaç: ayrı · ek: bitişik'),AD('Şıkları ele','A, D, E’de “de/da” bağlaçtır ve ayrı yazılmış. B’de “sinemada” bulunma hâlindedir ve bitişik yazılmış.','A, B, D, E: doğru'),AD('Yanlışı bul','C’de “akşam da” bağlaçtır, “ayrıca akşam” anlamı taşır; bitişik yazılması yanlıştır.','C: akşam da')],
 'Önce “de/da”yı çıkar: cümle bozulmuyorsa bağlaçtır, ayrı yazılır.')

# 0002 ki · orta · E
soru(Q,'0002','K-YAZ-02','orta','Bağlaç “ki” ile ilgi “-ki”nin yazımını ayırt eder.',3,
 'Aşağıdaki cümlelerin hangisinde “ki”nin yazımı yanlıştır?',
 [('Duydum ki yarın hava değişecekmiş.',D,'Bağlaç olan “ki” ayrı yazılmıştır; yazımı doğrudur.','dikkat'),
  ('Sanki hiçbir şey olmamış gibi davrandı.',D,'“Sanki” sözcüğünde “ki” sözcüğün parçasıdır; bitişik yazılır, doğrudur.','bilgi'),
  ('Masadaki kitabı bana uzatır mısın?',D,'“Masadaki” sözcüğündeki “-ki” ilgi ekidir; bitişik yazılır, doğrudur.','bilgi'),
  ('Biliyorsun ki yarın sınavım var.',D,'Bağlaç “ki” ayrı yazılmıştır; yazımı doğrudur.','dikkat'),
  ('Bizim bahçe sizin ki kadar büyük değil.',Y,'','')],
 'E',lambda t:t==Y,'“Ki” yazımı yanlış olan cümle.',
 '“Ki”nin bağlaç mı yoksa “-ki” ilgi eki mi olduğuna bak.',[B_KI],
 [AD('Türleri ayır','Bağlaç “ki” cümleleri bağlar ve ayrı yazılır; ilgi “-ki” bir ismin yerini tutar ya da isimden sıfat yapar, bitişik yazılır.','bağlaç: ayrı · -ki: bitişik'),AD('Şıkları ele','A ve D’de bağlaç ayrı; B’de “sanki” tek sözcük; C’de “masadaki” ilgi eki bitişik. Hepsi doğru.','A, B, C, D: doğru'),AD('Yanlışı bul','E’de “sizinki”, “sizin bahçeniz” anlamında ilgi zamiridir; bitişik yazılmalıdır.','E: sizinki')],
 '“Ki” bir ismin yerini tutuyor ya da isimden sıfat yapıyorsa (sizinki, masadaki) bitişik yazılan ilgi “-ki”dir; iki cümleyi bağlıyorsa bağlaçtır, ayrı yazılır.')

# 0003 mI · orta · A
soru(Q,'0003','K-YAZ-02','orta','Soru eki “mI” ile ek-fiil “-mIş”in yazımını ayırt eder.',3,
 'Aşağıdaki cümlelerin hangisinde soru ekinin yazımı yanlıştır?',
 [('Yarın okula gelecekmisin?',Y,'',''),
  ('Bu akşam bize gelecek misin?',D,'Soru eki “mi” kendinden önceki sözcükten ayrı yazılmıştır; doğrudur.','dikkat'),
  ('Duyduğuma göre sınav çok zormuş.',D,'“Zormuş”taki “-muş” soru eki değil, ek-fiilin rivayet biçimidir; bitişik yazılır.','bilgi'),
  ('Güzel mi güzel bir tatil geçirdik.',D,'Pekiştirme için kullanılan “mi” de ayrı yazılır; doğrudur.','bilgi'),
  ('Hasta mıydı, değil miydi bilmiyorum.',D,'“Mıydı” ve “miydi”de soru eki ayrı yazılır; doğrudur.','dikkat')],
 'A',lambda t:t==Y,'Soru ekinin yazımı yanlış olan cümle.',
 'Soru eki “mI” her zaman kendinden önceki sözcükten ayrı yazılır.',[B_KI],
 [AD('Kuralı hatırla','Soru eki “mI” ayrı yazılır; “-mIş” rivayet eki ise ek-fiildir ve bitişik yazılır.','mI: ayrı · -mIş: bitişik'),AD('Şıkları ele','B, D, E’de “mi/mı” ayrı; C’de “zormuş” bitişik ve doğru.','B, C, D, E: doğru'),AD('Yanlışı bul','A’da soru eki “gelecek misin” biçiminde ayrı yazılmalıydı.','A: gelecek misin')],
 'Soru anlamı varsa “mI” ayrı; “-mış/-miş” rivayet ekidir, bitişik yazılır.')

# 0004 büyük harf · orta · D
soru(Q,'0004','K-YAZ-03','orta','Özel ad, unvan ve yön adlarında büyük harf kullanımını bilir.',3,
 'Aşağıdaki cümlelerin hangisinde büyük harflerin kullanımı bakımından bir yanlışlık yoktur?',
 [('Yarın akşam trenle ankara’ya gideceğiz.',Y,'“Ankara” özel addır, büyük harfle başlamalıdır; cümlede yanlışlık vardır.','bilgi'),
  ('Hafta sonu Kuzeye doğru yola çıkacağız.',Y,'Yön adı bölge bildirmediği için küçük yazılmalıdır: “kuzeye”.','bilgi'),
  ('Ahmet bey bu akşam bize gelecek.',Y,'Unvan olan “Bey”, kişi adından sonra büyük yazılır: “Ahmet Bey”.','bilgi'),
  ('Yaz tatilinde Karadeniz’e gitmek istiyoruz.',D,'',''),
  ('Hafta sonu Boğaziçi köprüsünden geçtik.',Y,'Yapı adı olan “Boğaziçi Köprüsü” büyük harfle yazılır.','dikkat')],
 'D',lambda t:t==D,'Büyük harf kullanımında yanlışlık bulunmayan cümle.',
 'Her cümlede özel ad, unvan ve yön adı var mı diye bak; hangisinde bir hata yok?',[B_BH],
 [AD('Kuralları hatırla','Özel adlar, unvanlar ve yapı adları büyük; bölge bildirmeyen yön adları küçük harfle yazılır.','özel ad: büyük · yön: küçük'),AD('Şıkları tek tek ele','A: “Ankara” küçük yazılmış. B: “kuzeye” büyük yazılmış. C: “Bey” küçük yazılmış. E: “Köprüsü” küçük yazılmış.','A, B, C, E: yanlış'),AD('Hatasız olanı seç','D’de “Karadeniz” özel ad olarak büyük harfle başlıyor; başka hata yok.','D: doğru')],
 '“Hatasız olan” sorularında şıkları sırayla eleyip yanlışları işaretle; geriye kalan cevaptır.')

# 0005 sözcük yazımı · zor · B
soru(Q,'0005','K-YAZ-04','zor','Yazılışı karıştırılan sözcüklerin doğru yazımını bilir.',4,
 'Aşağıdaki cümlelerin hangisinde yazım yanlışı yoktur?',
 [('Herkez bu konuda aynı fikirdeydi.',Y,'“Herkes” sözcüğü “s” ile yazılır; “herkez” yazımı yanlıştır.','bilgi'),
  ('Bu işi herhangi biri yapabilir.',D,'',''),
  ('Yanlız başıma bu yolu yürüyemem.',Y,'Doğru yazım “yalnız”dır; “yanlız” yanlıştır.','bilgi'),
  ('Birçok kişi gelmedi, bir kaç kişi katıldı.',Y,'“Birkaç” bitişik yazılır; “bir kaç” yanlıştır.','bilgi'),
  ('Hiç bir şey söylemeden odadan çıktı.',Y,'“Hiçbir” bitişik yazılır; “hiç bir” yanlıştır.','dikkat')],
 'B',lambda t:t==D,'Yazım yanlışı bulunmayan cümle.',
 'Her cümledeki herkes, yalnız, birkaç, hiçbir, herhangi sözcüklerini ayrı ayrı denetle.',[B_SZ],
 [AD('Yazımı bilinmesi gerekenleri listele','herkes, yalnız, birkaç, hiçbir ve herhangi doğru yazımlardır; “her şey” ve “her gün” ayrı yazılır.','herkes · yalnız · birkaç · hiçbir · herhangi'),AD('Şıkları ele','A: herkez ✗. C: yanlız ✗. D: bir kaç ✗ (birkaç). E: hiç bir ✗ (hiçbir).','A, C, D, E: yanlış'),AD('Hatasız olanı seç','B’de “herhangi” bitişik, “biri” doğru yazılmıştır.','B: doğru')],
 'Sık karıştırılan sözcükleri (herkes, yalnız, birkaç, hiçbir) bir kez ezberle; her cümlede onları ara.')

# 0006 sayı · zor · C
soru(Q,'0006','K-YAZ-05','zor','Birden çok sözcükten oluşan sayıların ayrı yazıldığını bilir.',3,
 'Aşağıdaki cümlelerin hangisinde sayıların yazımı yanlıştır?',
 [('Sınıfta yirmi beş öğrenci vardı.',D,'“Yirmi beş” ayrı yazılmıştır; doğrudur.','bilgi'),
  ('Kitap üç yüz elli sayfadan oluşuyor.',D,'“Üç yüz elli” ayrı yazılmıştır; doğrudur.','bilgi'),
  ('Babam kırkbeş yaşında emekli oldu.',Y,'',''),
  ('Bu bina bin dokuz yüz seksen yılında yapıldı.',D,'“Bin dokuz yüz seksen” ayrı yazılmıştır; doğrudur.','dikkat'),
  ('Yarışmada on ikinci sırayı aldık.',D,'“On ikinci” sıra sayısı da ayrı yazılır; doğrudur.','dikkat')],
 'C',lambda t:t==Y,'Sayıların yazımı yanlış olan cümle.',
 'Birden çok sözcükten oluşan sayılar yazıyla yazılırken bitişik mi yazılır, ayrı mı?',[B_SY],
 [AD('Kuralı hatırla','Sayılar yazıyla yazılırken her sözcük ayrı yazılır.','yirmi beş · yüz altmış'),AD('Şıkları ele','A, B, D ve E’deki sayılar (yirmi beş, üç yüz elli, bin dokuz yüz seksen, on ikinci) ayrı yazılmış.','A, B, D, E: doğru'),AD('Yanlışı bul','C’deki “kırkbeş” bitişik yazılmış; doğrusu “kırk beş”tir.','C: kırk beş')],
 'Sayıyı yazıyla yazarken her basamağı ayrı yaz: kırk beş, yüz yirmi.')
bitir(Q)
