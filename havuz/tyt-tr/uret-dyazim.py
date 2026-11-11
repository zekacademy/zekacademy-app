"""TYT Türkçe · Yazım Kuralları (dil bilgisi genişletmesi, 1. yarı): 25 soru, hafif mod. Metinler özgündür."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from hafif_db import *
AD=A
KY='ÖSYM TYT Türkçe 2018–2026 · Bilgi Sarmal Dil Bilgisi SB (ÖSYM Tipi) · TDK Yazım Kılavuzu'
KARTLAR={
 'K-DBYZ-01':dict(alt='De/Da Yazımı (Bağlaç ve Bulunma Eki)',fikir='Bağlaç “de/da”nın ayrı ve hiçbir zaman “te/ta” olmadığını, bulunma eki “-de/-da”nın bitişik ve sert ünsüzden sonra “-te/-ta” olduğunu ayırt etmek.',tuzak='Bağlacı ek sanıp bitişik yazmak; bağlaca “te/ta” getirmek; “ya da”, “hem de” gibi kalıpları birleştirmek.',zorluk='orta',kalip='düz',adim=3,tipId='dyz-deda',kaynak=KY),
 'K-DBYZ-02':dict(alt='Ki Yazımı (Bağlaç, İlgi Eki, Kalıplaşmış Sözcük)',fikir='Bağlaç “ki”nin ayrı, ilgi “-ki”nin bitişik yazıldığını; “sanki, çünkü” gibi kalıplaşmış sözcüklerin tek sözcük olduğunu bilmek.',tuzak='İlgi “-ki”yi ayrı yazmak; “dünkü, bugünkü” gibi ünlü uyumuna girmeyen biçimleri yanlış yazmak; kalıplaşmış sözcüğü bölmek.',zorluk='orta',kalip='düz',adim=3,tipId='dyz-ki',kaynak=KY),
 'K-DBYZ-03':dict(alt='Soru Eki “mI” ve Ona Gelen Ekler',fikir='Soru ekinin kendinden önceki sözcükten ayrı, kendisine gelen kişi ve zaman eklerinin ise soru ekine bitişik yazıldığını bilmek.',tuzak='Soru ekini bitişik yazmak; “mısın, miydi” gibi ekleri ayırmak; ek-fiil “-mIş”i soru eki sanmak.',zorluk='orta',kalip='düz',adim=3,tipId='dyz-mi',kaynak=KY),
 'K-DBYZ-04':dict(alt='Büyük Harflerin Kullanımı',fikir='Özel adlar, bölge bildiren yön adları, belirli tarihler, bayram ve eser adlarıyla yapı/yer adlarının tamamlayıcı sözcüklerinde büyük harf kuralını uygulamak.',tuzak='Yön adını her yerde büyük ya da bölge adında küçük yazmak; “Gölü, Dağı, Romanı” gibi sözcükleri küçük bırakmak.',zorluk='orta',kalip='düz',adim=3,tipId='dyz-buyuk',kaynak=KY),
 'K-DBYZ-05':dict(alt='Kısaltmaların ve Sayıların Yazımı, Gelen Ekler',fikir='Kısaltmalara ve rakamla yazılan sayılara gelen eklerin kesmeyle ayrıldığını ve okunuşa göre seçildiğini; yazıyla yazılan sayıların ayrı yazıldığını bilmek.',tuzak='Eki yazılışa göre seçmek (1960’da, TDK’a); yazıyla yazılan sayıları bitişik yazmak.',zorluk='zor',kalip='düz',adim=4,tipId='dyz-kisaltma',kaynak=KY),
 'K-DBYZ-06':dict(alt='“-ken”, “-leyin” ve “ile” Yazımı',fikir='“-ken” ve “-leyin”in sözcüğe bitişik, “ile”nin ise ayrı ya da “-le/-la” olarak bitişik yazıldığını; “-ken”den sonra gelen bağlaç “de”nin ayrı kaldığını bilmek.',tuzak='“-ken”i ve “-leyin”i ayrı yazmak; “ile” ekini ayırmak; “-kende” biçimini tek parça sanmak.',zorluk='orta',kalip='düz',adim=3,tipId='dyz-ken',kaynak=KY),
 'K-DBYZ-07':dict(alt='Düzeltme İşareti (^)',fikir='Yazılışı aynı, anlamı ayrı sözcükleri (hâlâ/hala, kâr/kar, âdet/adet, âşık/aşık) ve uzun okunan ünlü ile inceltilen k, g, l sözcüklerini (kâğıt, rüzgâr, lâkin, hükûmet) ayırmak.',tuzak='Şapkayı hiç kullanmamak ya da yanlış anlamdaki sözcüğe koymak.',zorluk='zor',kalip='düz',adim=3,tipId='dyz-duzeltme',kaynak=KY),
}
TIPLER={'dyz-deda':'De/da yazımı','dyz-ki':'Ki yazımı','dyz-mi':'Soru eki mI yazımı','dyz-buyuk':'Büyük harf kullanımı','dyz-kisaltma':'Kısaltma ve sayı yazımı','dyz-ken':'-ken, -leyin, ile yazımı','dyz-duzeltme':'Düzeltme işareti'}
Q=kur('dyazim','Yazım Kuralları','tr|Yazım Kuralları',KARTLAR,TIPLER); Q.n=25
B_DE=B('De/da','bağlaç “de/da” ayrı yazılır, asla “te/ta” olmaz (Sen de gel) · bulunma eki bitişik yazılır, sert ünsüzden sonra “-te/-ta” olur (evde, kitapta, uçakta)')
B_KI=B('Ki','bağlaç “ki” ayrı (Öyle yoruldu ki uyudu) · ilgi “-ki” bitişik (evdeki, seninki, dünkü, bugünkü) · “sanki, çünkü” tek sözcüktür')
B_MI=B('Soru eki','soru eki “mI” ayrı yazılır (geldi mi?) · ona gelen ekler bitişik yazılır (mısın, miydi, mıyız) · ek-fiil “-mIş” bitişik (hastaymış)')
B_BH=B('Büyük harf','özel adlar, bölge bildiren yön adları (Doğu Anadolu), belirli tarihler (29 Ekim), özel gün ve eser adları büyük başlar · yön adı yönü gösteriyorsa küçük (güneye gitti) · özel adı tamamlayan Gölü, Dağı, Bulvarı da büyük')
B_KS=B('Kısaltma ve sayıya ek','ek okunuşa göre seçilir, kesmeyle ayrılır: TDK’ye (te-de-ke), km’yi, 1960’ta (altmış), 40’ı (kırk) · yazıyla yazılan sayılar ayrı yazılır: yüz yirmi beş')
B_KEN=B('-ken, -leyin, ile','“-ken” ve “-leyin” bitişik yazılır (gelirken, çocukken, sabahleyin, geceleyin) · “ile” ayrı ya da ek olarak bitişik yazılır (Ali ile, kalemle, arabayla) · “gelirken de” bağlaç ayrı')
B_DZ=B('Düzeltme işareti','^ yazılışı aynı sözcükleri ayırır: hâlâ (henüz) / hala (baba kız kardeşi), kâr / kar, âdet (gelenek) / adet (sayı), âşık (sevdalı) / aşık (oyun kemiği) · k, g, l’yi inceltir: kâğıt, rüzgâr, lâkin, hükûmet')

def S(no,kart,zor,kaz,adim,kok,items,harf,istenen,ip,bilgi,adimlar,puf,kalip='düz'):
    """items: 5 × (metin, cel) ya da (metin, cel, tur); cel None ise o şık cevaptır."""
    opts=[]; 
    for i,it in enumerate(items):
        t,c=it[0],it[1]; tur=it[2] if len(it)>2 else ('dikkat' if i%2 else 'bilgi')
        opts.append((t,'T' if c is None else 'N',c or '',tur if c else ''))
    soru(Q,no,kart,zor,kaz,adim,kok,opts,harf,lambda e:e=='T',istenen,ip,bilgi,adimlar,puf,kalip=kalip)
def N(no,kart,zor,kaz,adim,parca,kok,cels,harf,istenen,ip,bilgi,adimlar,puf):
    """Numaralı parça. cels: 5 öğe (I..V sırasıyla); cevap için None, ötekiler için açıklama."""
    S(no,kart,zor,kaz,adim,parca+'\n'+kok,[(r,c) for r,c in zip(ROM[:5],cels)],harf,istenen,ip,bilgi,adimlar,puf,kalip='öncüllü')
KOK_NY='Bu parçada numaralanmış yerlerden hangisinin yazımı yanlıştır?'

# 0001 de/da · kolay · C
S('0001','K-DBYZ-01','kolay','Bağlaç “de/da” ile bulunma ekini ayırt eder.',2,
 'Aşağıdaki cümlelerin hangisinde “de/da”nın yazımı yanlıştır?',
 [('Hafta sonu dağda yürüyüş yapacağız.','Bu “-da” bulunma ekidir; sözcüğe bitişik yazılması doğrudur.'),
  ('Elif de bu yıl müzik kursuna yazıldı.','Bu “de” bağlaçtır; ayrı yazılması doğrudur.'),
  ('Kerem sinemaya gitti, Elif te evde kaldı.',None),
  ('Bu akşam bizde misafir var.','“Bizde” sözcüğündeki “-de” bulunma ekidir; bitişik yazılması doğrudur.'),
  ('Yağmur dindi, biz de yola çıktık.','Bu “de” bağlaçtır; ayrı yazılması doğrudur.')],
 'C','“De/da” yazımı yanlış olan cümle.',
 'Bağlaç olan “de/da” hiçbir zaman “te/ta” biçiminde yazılmaz.',[B_DE],
 [AD('Kuralı hatırla','Bağlaç “de/da” ayrı yazılır ve “te/ta” olmaz; bulunma eki bitişik yazılır.','bağlaç: ayrı, hep de/da'),
  AD('Şıkları sına','A’da “dağda” ve D’de “bizde” bulunma eki, B ve E’de “de” bağlaç; hepsi kurala uygun.','A, B, D, E: doğru'),
  AD('Yanlışı bul','C’deki “Elif te” bağlaçtır (“Elif de”); bağlaca “te” getirilemez.','C: Elif te ✗')],
 'Çıkarınca cümle bozulmuyorsa “de/da” bağlaçtır: ayrı yazılır ve asla “te/ta” olmaz.')

# 0002 de/da · orta · A
S('0002','K-DBYZ-01','orta','“Yine de, hem de, ya da, ek” yazımlarını ayırt eder.',3,
 'Aşağıdaki cümlelerin hangisinde “de/da” bakımından yazım yanlışı yoktur?',
 [('Çok yorgundum, yine de ödevimi bitirdim.',None),
  ('Kitaplar masa da, defterler çantada duruyor.','“Masada”daki “-da” bulunma ekidir; bitişik yazılmalıdır.'),
  ('Hem çalışıyor hem te okuyor.','“Hem de” bağlaç kalıbıdır; “te” biçimi olmaz.'),
  ('Bugün ya buluşalım yada yarın görüşelim.','“Ya da” bağlaç grubu ayrı yazılır; “yada” yanlıştır.'),
  ('Bu sözcüğü sözlük te aradım.','“Sözlükte”deki ek bulunma ekidir; bitişik yazılmalıdır.')],
 'A','De/da yazımı bakımından yanlışı bulunmayan cümle.',
 'Her cümledeki “de/da”nın bağlaç mı yoksa ek mi olduğunu belirle.',[B_DE],
 [AD('Türleri ayır','Bağlaç ayrı; ek bitişik; “ya da” ve “hem de” ayrı yazılan bağlaç gruplarıdır.','bağlaç: ayrı · ek: bitişik'),
  AD('Yanlışları ele','B’de “masada”, E’de “sözlükte” ek olduğu hâlde ayrı yazılmış. C’de “te”, D’de “yada” yanlıştır.','B, C, D, E: yanlış'),
  AD('Doğruyu seç','A’daki “yine de” ayrı yazılır ve cümlede başka yanlış yoktur.','A: doğru')],
 '“Yine de, hem de, ya da, ne de” gibi bağlaç gruplarında “de/da” hep ayrı yazılır.')

# 0003 de/da · orta · E
S('0003','K-DBYZ-01','kolay','Bulunma ekinin sert ünsüzden sonra “-ta/-te” olduğunu bilir.',3,
 'Aşağıdaki cümlelerin hangisinde bulunma ekinin yazımı yanlıştır?',
 [('Kitapta üç yeni bölüm var.','“Kitap” sert ünsüz “p” ile bittiği için ek “-ta” olmuştur; doğrudur.'),
  ('Çocuklar bahçede oynuyor.','“Bahçe” ünlüyle bittiği için ek “-de” olmuştur; doğrudur.'),
  ('Dağda kar yağışı başladı.','“Dağ” sözcüğünün sonu “ğ” yumuşak ünsüzdür; ek “-da” olur, doğrudur.'),
  ('Ağaçta kuşlar öttü.','“Ağaç” sert “ç” ile bittiği için ek “-ta” olmuştur; doğrudur.'),
  ('Çocuklar uçakda uyudu.',None)],
 'E','Bulunma eki yanlış yazılan cümle.',
 'Sert ünsüzlerle biten sözcüklerde ek “-ta/-te” olur: f, s, t, k, ç, ş, h, p.',[B_DE],
 [AD('Kuralı hatırla','Bulunma eki sert ünsüzden (f, s, t, k, ç, ş, h, p) sonra “-ta/-te”, ötekilerden sonra “-da/-de” olur.','sert ünsüz → -ta/-te'),
  AD('Şıkları sına','kitapta (p), bahçede (ünlü), dağda (ğ), ağaçta (ç): hepsi kurala uygun.','A–D: doğru'),
  AD('Yanlışı bul','“Uçak” k ile biter, sert ünsüzdür; “uçakta” yazılmalıdır, “uçakda” yanlıştır.','E: uçakta')],
 'Sözcük sert ünsüzle bitiyorsa bulunma eki “-ta/-te” olur: uçakta, kitapta, ağaçta.')

# 0004 de/da · zor · numaralı · B
N('0004','K-DBYZ-01','zor','Parçada bağlaç ve ek olan “de/da”ların yazımını ayırt eder.',4,
 'Hafta sonu ailecek köyde (I) yaşayan dedemi ziyaret ettik. Dedem hasta olsada (II) bizimle bahçede (III) çalıştı. Biz de (IV) ona yardım ettik. Akşam yorgunduk, yine de (V) yemeği birlikte hazırladık.',
 'Bu parçada numaralanmış yerlerden hangisinin yazımı yanlıştır?',
 ['“Köyde” sözcüğündeki “-de” bulunma ekidir; bitişik yazılması doğrudur.',
  None,
  '“Bahçede” sözcüğündeki “-de” bulunma ekidir; bitişik yazılması doğrudur.',
  '“Biz de” ifadesindeki “de” bağlaçtır; ayrı yazılması doğrudur.',
  '“Yine de” ifadesindeki “de” bağlaçtır; ayrı yazılması doğrudur.'],
 'B','Yazımı yanlış olan numaralanmış yer.',
 'Yazılışı yanlış sanılanları “de/da”yı çıkarıp cümleyi yeniden okuyarak sına.',[B_DE],
 [AD('Kuralı hatırla','Bağlaç “de/da” ayrı, bulunma eki “-de/-da” bitişik yazılır.','bağlaç: ayrı · ek: bitişik'),
  AD('Numaraları sına','I köyde (ek) ✓ · III bahçede (ek) ✓ · IV biz de (bağlaç) ✓ · V yine de (bağlaç) ✓.','I, III, IV, V: doğru'),
  AD('Yanlışı bul','II’deki “olsada” yanlıştır: “olsa da”. “-sa/-se” şart ekinden sonra gelen “da” bağlaçtır ve ayrı yazılır.','II: olsa da')],
 'Çıkarınca anlam bozulmuyorsa “de” bağlaçtır; “olsa da, yapsa da” gibi şart kipinden sonra gelen “da” ayrı yazılır.')

# 0005 ki · kolay · D
S('0005','K-DBYZ-02','kolay','Bağlaç “ki” ile ilgi “-ki”nin yazımını ayırt eder.',2,
 'Aşağıdaki cümlelerin hangisinde bağlaç ya da ek olan “ki” hatalı yazılmıştır?',
 [('Öyle yorgundu ki yemek yemeden uyudu.','Bağlaç olan “ki” ayrı yazılmıştır; doğrudur.'),
  ('Duvardaki saat bir süre önce durmuş.','“Duvardaki”nin “-ki” eki ilgi ekidir; bitişik yazılması doğrudur.'),
  ('Bu kalem seninkinden daha kalın.','“Seninki” ilgi zamiridir; bitişik yazılması doğrudur.'),
  ('Biliyorsunuzki çok geç kaldık.',None),
  ('Sınıfa girdiğimde gördüm ki herkes gitmiş.','Bağlaç “ki” ayrı yazılmıştır; doğrudur.')],
 'D','“Ki” yazımı yanlış olan cümle.',
 '“Ki”den önce duraksayıp cümlenin ikiye ayrıldığı yerlerde bağlaç “ki” ayrı yazılır.',[B_KI],
 [AD('Kuralı hatırla','Bağlaç “ki” iki cümleyi bağlar ve ayrı yazılır; ilgi “-ki” ekine bitişir.','bağlaç: ayrı · -ki: bitişik'),
  AD('Şıkları sına','A ve E’de bağlaç ayrı; B’de “duvardaki”, C’de “seninki” ilgi eki bitişik.','A, B, C, E: doğru'),
  AD('Yanlışı bul','D’de “biliyorsunuz ki” bağlaçtır; bitişik yazılması yanlıştır.','D: biliyorsunuz ki')],
 '“Ki” bir ismin yerini tutmuyor, ek gibi davranmıyorsa bağlaçtır ve ayrı yazılır.')

# 0006 ki · orta · B
S('0006','K-DBYZ-02','orta','“Dünkü, bugünkü” ve ilgi “-ki”nin doğru yazımını bilir.',3,
 'Aşağıdaki cümlelerden hangisi, ilgi ekinin ve “çünkü” sözcüğünün yazımı bakımından hatasızdır?',
 [('Yarın ki toplantıya herkes katılacak.','Zaman bildiren “yarın”a gelen “-ki” ek olduğu için bitişik yazılmalıdır: “yarınki”.'),
  ('Bugünkü maç için biletler tükendi.',None),
  ('Dışarı çıkmadık, çünki hava çok soğuktu.','“Çünkü” tek sözcüktür ve “-kü” ile yazılır; “çünki” yanlıştır.'),
  ('Şimdi ki durumumuz eskisinden iyi.','“Şimdiki” ilgi eki aldığı için bitişik yazılmalıdır.'),
  ('Dünki yağmurdan sonra yollar çamurlaştı.','“Dünkü” biçimi “-ki”nin ünlü uyumuna girdiği sözcüktür; “dünki” yanlıştır.')],
 'B','“Ki” yazımı doğru olan cümle.',
 '“Dünkü” ve “bugünkü” gibi sözcüklerde “-ki” ünlü uyumuna girer.',[B_KI],
 [AD('Kuralı hatırla','İlgi “-ki” bitişik yazılır; “dün”, “bugün” sözcüklerinde ü ünlüsü nedeniyle “-kü” olur; “çünkü” tek sözcüktür.','dünkü, bugünkü, çünkü'),
  AD('Şıkları ele','A’da “yarınki”, D’de “şimdiki” ayrı yazılmış. C’de “çünki”, E’de “dünki” yanlış.','A, C, D, E: yanlış'),
  AD('Doğruyu seç','B’deki “bugünkü” ilgi eki alıp ünlü uyumuna girmiş doğru biçimdir.','B: bugünkü')],
 '“Dün” ve “bugün”e gelen ilgi eki “-kü” olur; “yarın, şimdi, sonra” gibi sözcüklere “-ki” gelir.')

# 0007 ki · zor · numaralı · C
N('0007','K-DBYZ-02','zor','Parçada bağlaç “ki” ve ilgi “-ki”lerin yazımını ayırt eder.',4,
 'Sınıfımızda bu dönem kitap değişimi başladı. Öyle ki (I) herkes haftada bir kitabını arkadaşına veriyor. Benim okuduğum roman Kerem’inkine (II) göre daha kalın, Elif’in aldığı ise benimki’ne (III) benzeyecek kadar ince. Sanki (IV) kimse kitapsız kalmak istemiyor. Bugünkü (V) değişimde rafın yarısı boşaldı.',
 'Bu parçada numaralanmış yerlerden hangisinin yazımı yanlıştır?',
 ['“Öyle ki” bağlaç grubudur; ayrı yazılması doğrudur.',
  '“Kerem’inkine” ilgi zamiridir; bitişik yazılması doğrudur.',
  None,
  '“Sanki” tek sözcüktür; bitişik yazılması doğrudur.',
  '“Bugünkü” ilgi ekiyle ünlü uyumuna girmiş doğru biçimdir.'],
 'C','Yazımı yanlış olan numaralanmış yer.',
 'İlgi zamiri “-ki” bir ismin yerini tutar; ona gelen ekler de kesmesiz, bitişik yazılır.',[B_KI],
 [AD('Kuralı hatırla','Bağlaç “ki” ayrı; ilgi “-ki” bitişik; “sanki, çünkü” tek sözcük.','bağlaç ayrı · -ki bitişik'),
  AD('Numaraları sına','I “öyle ki” (bağlaç) ✓ · II “Kerem’inkine” ✓ · IV “sanki” ✓ · V “bugünkü” ✓.','I, II, IV, V: doğru'),
  AD('Yanlışı bul','III’te “benimki” ilgi zamiridir; kendisine gelen ek kesmeyle ayrılmaz, “benimkine” yazılmalıdır. Kesme yalnız özel adla ek arasına girer (Kerem’inkine).','III: benimkine')],
 'Özel ad dışındaki ilgi zamirlerine (benimki, seninki) gelen ekler kesmeyle ayrılmaz.')

# 0008 mi · kolay · E
S('0008','K-DBYZ-03','kolay','Soru ekinin ayrı yazıldığını bilir.',2,
 'Aşağıdaki cümlelerin hangisinde soru eki yanlış yazılmıştır?',
 [('Bu kitabı okudun mu?','Soru eki “mu” ayrı yazılmıştır; doğrudur.'),
  ('Sen mi aradın beni?','Soru eki “mi” ayrı yazılmıştır; doğrudur.'),
  ('Hava soğuk mu olacak?','Soru eki “mu” ayrı yazılmıştır; doğrudur.'),
  ('Yemek hazır mı?','Soru eki “mı” ayrı yazılmıştır; doğrudur.'),
  ('Çantanı yanına aldınmı?',None)],
 'E','Soru eki yanlış yazılan cümle.',
 'Soru eki her zaman kendinden önceki sözcükten ayrı yazılır.',[B_MI],
 [AD('Kuralı hatırla','Soru eki “mI” (mı, mi, mu, mü) ayrı yazılır.','mI: ayrı'),
  AD('Şıkları sına','A, B, C, D’de soru eki ayrı yazılmış.','A–D: doğru'),
  AD('Yanlışı bul','E’de “aldınmı” bitişik yazılmış; “aldın mı” olmalıdır.','E: aldın mı')],
 'Soru eki sözcüğe yapışmaz: “aldın mı”, “geldi mi”.')

# 0009 mi · orta · A
S('0009','K-DBYZ-03','orta','Soru ekine gelen eklerin bitişik yazıldığını bilir.',3,
 'Aşağıdaki cümlelerin hangisinde soru eki ve ona gelen ek yanlış yazılmıştır?',
 [('Toplantıya katılacak mı sınız?',None),
  ('Dün gece uyudun mu?','Soru eki ayrı yazılmıştır; doğrudur.'),
  ('Bu sorunun cevabını biliyor musunuz?','Kişi eki “-nuz” soru ekine bitişik yazılmıştır; doğrudur.'),
  ('Daha önce bu şehre gelmiş miydiniz?','Zaman ve kişi ekleri soru ekine bitişiktir; doğrudur.'),
  ('Kapıyı kilitlemedik mi?','Soru eki ayrı, olumsuzluk eki fiile bitiktir; doğrudur.')],
 'A','Soru ekinin ya da ona gelen ekin yazımı yanlış olan cümle.',
 'Soru ekinden sonra gelen kişi ve zaman ekleri soru ekine yapışık yazılır.',[B_MI],
 [AD('Kuralı hatırla','Soru eki ayrı yazılır; soru ekine gelen kişi ve zaman ekleri ise soru ekine bitişik yazılır (mısınız, miydiniz).','mI ayrı · ek: mI’ya bitişik'),
  AD('Şıkları sına','B, C, D, E’de soru eki ve onun ekleri kurala uygun yazılmış.','B–E: doğru'),
  AD('Yanlışı bul','A’daki “mı sınız” ayrı yazılmış; “katılacak mısınız” olmalıdır.','A: mısınız')],
 'Soru eki sözcükten ayrı, ona gelen ek soru ekine bitişik: “gelecek mi + siniz” → “gelecek misiniz”.')

# 0010 mi · zor · numaralı · D
N('0010','K-DBYZ-03','zor','Parçada soru eki ve ek-fiil yazımlarını ayırt eder.',4,
 'Sınavdan önceki gün sınıf çok gürültülüydü. Herkes birbirine soru soruyordu. Kimi tüm konuları bitirdin mi (I) diye merak ediyordu. Kimi sınav zor olacak mı (II) diye endişeleniyordu. Elif hâlâ ders çalışıyormuş (III), Kerem ise hazırmısın (IV) diye bana baktı. Ben ise sorulara gerçekten hazır mıydım (V) bilmiyordum.',
 'Bu parçada numaralanmış yerlerden hangisinin yazımı yanlıştır?',
 ['Soru eki “mi” ayrı yazılmıştır; doğrudur.',
  'Soru eki “mı” ayrı yazılmıştır; doğrudur.',
  '“Çalışıyormuş” fiildeki rivayet birleşik zamanıdır; bitişik yazılması doğrudur.',
  None,
  '“Mıydım” soru ekine bitişen ek-fiil ve kişi ekidir; bu yazılış doğrudur.'],
 'D','Yazımı yanlış olan numaralanmış yer.',
 'Soru anlamı taşıyan “mI” ayrıdır; “-mIş” rivayet ekidir.',[B_MI],
 [AD('Kuralı hatırla','Soru eki ayrı; ona gelen ek bitişik; “-mIş” rivayet eki bitişik yazılır.','mı ayrı · mıydım bitişik'),
  AD('Numaraları sına','I ve II soru eki ayrı ✓ · III “çalışıyormuş” rivayet ✓ · V “mıydım” ✓.','I, II, III, V: doğru'),
  AD('Yanlışı bul','IV’te “hazırmısın” bitişik yazılmış; soru eki ayrı olmalı: “hazır mısın”.','IV: hazır mısın')],
 '“-mış” rivayet eki ise bitişik, “mı” soru eki ise ayrı yazılır; “hazırmış” ile “hazır mı” ayrıdır.')

# 0011 büyük harf · kolay · B
S('0011','K-DBYZ-04','kolay','Özel ad tamlamalarında büyük harf kullanımını bilir.',2,
 'Aşağıdaki cümlelerin hangisinde büyük harf kullanımı yanlıştır?',
 [('Dün akşam Elif Hanım bizi aradı.','“Elif Hanım” kişi adı ve unvanı büyük başlar; doğrudur.'),
  ('Hafta sonu Erciyes dağı’na tırmandık.',None),
  ('Ankara’dan İzmir’e giden tren yarın kalkacak.','Şehir adları büyük başlar; doğrudur.'),
  ('Çocuklar Türkçe dersinde şiir okudu.','“Türkçe” dil adı olarak büyük başlar; doğrudur.'),
  ('Babam Karadeniz’de doğdu.','“Karadeniz” özel addır ve büyük başlar; doğrudur.')],
 'B','Büyük harf kullanımı yanlış olan cümle.',
 'Dağ, göl, deniz adlarının tamamlayıcı sözcükleri de özel adın parçasıdır.',[B_BH],
 [AD('Kuralı hatırla','Özel adlar büyük başlar; “Dağı, Gölü, Denizi” gibi tamamlayıcı sözcükler de özel adın parçası olduğundan büyük yazılır.','Erciyes Dağı'),
  AD('Şıkları sına','A, C, D, E’de kişi, şehir, dil ve deniz adları büyük harfle başlamış.','A, C, D, E: doğru'),
  AD('Yanlışı bul','B’de “Erciyes dağı” biçiminde “dağı” küçük yazılmış; “Erciyes Dağı” olmalıdır.','B: Erciyes Dağı')],
 'Özel adın içindeki her sözcük büyük başlar: Erciyes Dağı, Van Gölü, Marmara Denizi.')

# 0012 büyük harf · orta · numaralı · C
N('0012','K-DBYZ-04','orta','Parçada yer adlarında büyük harf kullanımını ayırt eder.',3,
 'Geçen yaz ailemle birlikte Doğu Anadolu’yu (I) dolaştık. İlk durağımız Erzurum (II) oldu. Ardından van Gölü’nün (III) kıyısında bir gece konakladık. Yol boyunca dağların eteğinde yeşil çayırlar gördük. Sonra Ağrı Dağı’nı (IV) izleyerek Kars’a (V) ulaştık.',
 'Bu parçada numaralanmış yerlerden hangisinde büyük harf kullanımı yanlıştır?',
 ['Bölge adı olan “Doğu Anadolu” büyük başlar; doğrudur.',
  'Şehir adı büyük başlamıştır; doğrudur.',
  None,
  '“Ağrı Dağı” özel ad tamlamasıdır ve her sözcüğü büyük başlar; doğrudur.',
  'Şehir adı büyük başlamıştır; doğrudur.'],
 'C','Büyük harf kullanımı yanlış olan numaralanmış yer.',
 'Özel adın tamlayıcı sözcükleri de büyük başlar.',[B_BH],
 [AD('Kuralı hatırla','Özel adlar ve bölge adları büyük başlar; “Gölü, Dağı” özel adın parçasıdır.','özel ad: her sözcük büyük'),
  AD('Numaraları sına','I Doğu Anadolu ✓ · II Erzurum ✓ · IV Ağrı Dağı ✓ · V Kars ✓.','I, II, IV, V: doğru'),
  AD('Yanlışı bul','III’te “van” küçük yazılmış; “Van Gölü” olmalıdır.','III: Van Gölü')],
 'Özel adın her bileşeni büyük başlar; “gölü, dağı, denizi” de dâhil.')

# 0013 büyük harf · orta · E (yoktur)
S('0013','K-DBYZ-04','orta','Tarih, yön, eser ve özel gün adlarında büyük harf kullanımını bilir.',3,
 'Aşağıdaki cümlelerin hangisinde büyük harflerin kullanımı bakımından bir yanlışlık yoktur?',
 [('Cumhuriyet bayramı’nı her yıl 29 Ekim’de kutlarız.','Bayram adı özel gün adıdır; “Cumhuriyet Bayramı” büyük başlar.'),
  ('Kuşlar kışın güneye, ilkbaharda Kuzeye göç eder.','Yön adı bölge bildirmediği için küçük yazılmalıdır: “kuzeye”.'),
  ('Öğretmenimiz Çalıkuşu Romanı’nı gençlere önerdi.','Eser adının dışında kalan “romanı” küçük yazılır: “Çalıkuşu romanını”.'),
  ('Yarın Atatürk bulvarı’nda yürüyüş var.','Özel adın tamamlayıcısı olan “Bulvarı” büyük başlamalıdır.'),
  ('Öğretmenler Günü’nde sınıfa çiçek getirdik.',None)],
 'E','Büyük harf kullanımında hata bulunmayan cümle.',
 'Her şıktaki hatayı ayrı ayrı bul; hatasız olan ortada kalır.',[B_BH],
 [AD('Kuralları hatırla','Özel gün ve bayram adları, ay adları ve özel adın tamamlayıcıları büyük; yön adı yönü gösteriyorsa küçük yazılır.','bayram: büyük · yön: küçük'),
  AD('Şıkları ele','A: bayramı ✗ · B: Kuzeye ✗ · C: Romanı ✗ · D: bulvarı ✗.','A–D: yanlış'),
  AD('Hatasızı seç','E’de “Öğretmenler Günü” doğru yazılmıştır.','E: doğru')],
 '“Hatasız olan” sorusunda dört yanlışı elersen cevap kendiliğinden kalır.')

# 0014 büyük harf · zor · numaralı · A
N('0014','K-DBYZ-04','zor','Parçada yön ve yer adlarında büyük harf ile küçük harf ayrımını yapar.',4,
 'Coğrafya dersinde bu hafta kıtaları işledik. Öğretmenimiz önce Türkiye’nin Güneyindeki (I) Akdeniz kıyılarını, sonra Güney Amerika’yı (II) tanıttı. Kuzey Kutbu’nda (III) yaşayan hayvanları anlatırken sınıf sessizleşti. Dersin sonunda Büyük Okyanus’un (IV) genişliğinden söz etti ve Ege Bölgesi’ni (V) haritada gösterdi.',
 'Bu parçada numaralanmış yerlerden hangisinde büyük harf kullanımı yanlıştır?',
 [None,
  '“Güney Amerika” kıta adının parçası olduğu için “Güney” büyük başlar; doğrudur.',
  '“Kuzey Kutbu” özel addır; yön adı özel adın parçası olduğu için büyük başlar.',
  '“Büyük Okyanus” özel addır; her sözcüğü büyük başlar, doğrudur.',
  '“Ege Bölgesi” özel adı büyük başlar; doğrudur.'],
 'A','Büyük harf kullanımı yanlış olan numaralanmış yer.',
 'Yön adı özel adın parçası olursa büyük, yalnız yönü gösterirse küçük yazılır.',[B_BH],
 [AD('Kuralı hatırla','Yön adı özel adın parçasıysa (Güney Amerika, Kuzey Kutbu) büyük; yalnız yönü gösteriyorsa (Türkiye’nin güneyi) küçük yazılır.','özel ad: büyük · yön: küçük'),
  AD('Numaraları sına','II Güney Amerika (özel ad) ✓ · III Kuzey Kutbu ✓ · IV Büyük Okyanus ✓ · V Ege Bölgesi ✓.','II–V: doğru'),
  AD('Yanlışı bul','I’deki “Türkiye’nin Güneyindeki” yalnız yönü gösterir, özel adın parçası değildir; “güneyindeki” küçük yazılmalıdır.','I: güneyindeki')],
 'Yön adı, bir özel adın parçasıysa büyük başlar; bu özel adı bir yöne bağlayan “güneyindeki” gibi yerlerde küçüktür.')

# 0015 kısaltma · orta · D
S('0015','K-DBYZ-05','orta','Kısaltmalara gelen eklerin okunuşa göre seçildiğini ve kesmeyle ayrıldığını bilir.',3,
 'Aşağıdaki cümlelerin hangisinde kısaltmaya gelen ekin yazımı yanlıştır?',
 [('Öğrenciler TDK’ye bir mektup yazdı.','“TDK” “te-de-ke” diye okunur; ünlüyle bittiği için ek “-ye” olur, doğrudur.'),
  ('Yolun 12 km’yi aşan bölümü kapalı.','Kısaltmaya gelen ek kesmeyle ayrılmış, “-yi” okunuşa uygun; doğrudur.'),
  ('Haberi TBMM’nin internet sitesinden okudum.','“TBMM” “me” ile biter; ilgi eki “-nin” olur, doğrudur.'),
  ('Babam yıllardır THY’da çalışıyor.',None),
  ('Bu belgeyi ABD’de yaşayan teyzem gönderdi.','“ABD” “de” ile biter; bulunma eki “-de” olur, doğrudur.')],
 'D','Kısaltmaya gelen ekin yazımı yanlış olan cümle.',
 'Kısaltmanın harf adlarını sesli oku; sonuncu harfin adındaki ünlü kalın mı, ince mi?',[B_KS],
 [AD('Kuralı hatırla','Kısaltmalara gelen ek okunuşa göre seçilir ve kesmeyle ayrılır. Ekin ünlüsü son harf adındaki ünlüye uyar (ye → e); harf adı ünlüyle bitiyorsa araya “y” girer (TDK’ye).','THY: te-ha-ye → -de'),
  AD('Şıkları sına','A: TDK’ye ✓ · B: km’yi ✓ · C: TBMM’nin ✓ · E: ABD’de ✓.','A, B, C, E: doğru'),
  AD('Yanlışı bul','D’de “THY” “te-ha-ye” diye okunur; son ünlü “e” ince olduğu için ek “-de” olmalı; “THY’da” yanlıştır.','D: THY’de')],
 'Kısaltmanın son harfini adıyla oku: “ye” ince ünlülüdür, bu yüzden “THY’de”.')

# 0016 sayı · zor · C
S('0016','K-DBYZ-05','zor','Rakamla yazılan sayılara gelen eki okunuşa göre seçer.',4,
 'Aşağıdaki cümlelerin hangisinde rakamla yazılan sayıya gelen ekin yazımı yanlıştır?',
 [('Toplantı saat 5’te başlayacak.','“Beş” sert “ş” ile bittiği için “-te” olur; doğrudur.'),
  ('Sınıfta 30’ar kişilik iki grup oluşturduk.','“Otuz”dan sonra “-ar” gelir; doğrudur.'),
  ('Köprü 2018’te hizmete açıldı.',None),
  ('Okul 2023’te yeni binasına taşındı.','“İki bin yirmi üç” sert “ç” ile bittiği için “-te” olur; doğrudur.'),
  ('Defterin 7’si bende, 9’u sende.','“Yedi” ve “dokuz” sözcüklerine gelen iyelik ekleri okunuşa uygundur; doğrudur.')],
 'C','Sayıya gelen ekin yazımı yanlış olan cümle.',
 'Sayıyı yazıyla oku: son sözcüğün son sesi sert ünsüz mü?',[B_KS],
 [AD('Kuralı hatırla','Rakamla yazılan sayıya gelen ek, sayının okunuşuna göre seçilir ve kesmeyle ayrılır.','2018 → on sekiz → -de'),
  AD('Şıkları sına','A beş → 5’te ✓ · B otuz → 30’ar ✓ · D üç → 2023’te ✓ · E yedi, dokuz → 7’si, 9’u ✓.','A, B, D, E: doğru'),
  AD('Yanlışı bul','C’de 2018 “…on sekiz” diye okunur; “z” sert ünsüz değildir (f, s, t, k, ç, ş, h, p dışındadır), ek “-de” olmalı: “2018’de”.','C: 2018’de')],
 'Sayının yazılışına değil okunuşuna bak: sert ünsüzle (kırk, beş, üç) bitiyorsa “-ta/-te”, “sekiz, dokuz” gibi z ile bitiyorsa “-da/-de”.')

# 0017 kısaltma/sayı · orta · numaralı · B
N('0017','K-DBYZ-05','orta','Parçada sayılara gelen ekleri okunuşa göre ayırt eder.',3,
 'Kulübümüz 2010’lu (I) yıllarda kuruldu. Bu yıl üyelerimiz sözlükten 100’ı (II) aşkın sözcük seçip 15’er (III) kişilik gruplara dağıttı. Yarışmaya katılan 24 öğrencinin 6’sı (IV) ödül alırken jüri üyeleri her çalışmaya 10’a (V) kadar puan verdi.',
 'Bu parçada numaralanmış yerlerden hangisinin yazımı yanlıştır?',
 ['“2010’lu” ek kesmeyle ayrılmış ve okunuşa uygundur; doğrudur.',
  None,
  '“On beş” sözcüğüne gelen “-er” eki okunuşa uygun (beşer); doğrudur.',
  '“Altı” sözcüğüne gelen iyelik eki “-sı” okunuşa uygun; doğrudur.',
  '“On” sözcüğüne gelen yönelme eki “-a” okunuşa uygun; doğrudur.'],
 'B','Yazımı yanlış olan numaralanmış yer.',
 'Sayıyı yazıyla oku ve son ünlüsünün kalın mı, ince mi ve düz mü, yuvarlak mı olduğuna bak.',[B_KS],
 [AD('Kuralı hatırla','Sayıya gelen ekler okunuşa göre seçilir; kesmeyle ayrılır.','okunuşa göre ek'),
  AD('Numaraları sına','I 2010’lu ✓ · III 15’er ✓ · IV 6’sı ✓ · V 10’a ✓.','I, III, IV, V: doğru'),
  AD('Yanlışı bul','II’de 100 “yüz” diye okunur; son ünlü “ü” (ince, yuvarlak) olduğu için ek “-ü” olmalı: “100’ü”. “100’ı” yanlıştır.','II: 100’ü')],
 'Ek, sayının yazılışına değil okunuşuna göre seçilir: 100 “yüz” olduğu için 100’ü.')

# 0018 sayı yazımı · zor · numaralı · E
N('0018','K-DBYZ-05','zor','Parçada sayı ve kısaltmalara gelen eklerin okunuşa uygunluğunu ve sayıların yazımını ayırt eder.',4,
 'Kütüphanemize bu yıl iki yüz elli (I) yeni kitap geldi. Bunların 40’ı (II) ansiklopedi, kalanı roman ve öykü kitabı. Kitapların bir bölümü TÜBİTAK’ın (III) yayınlarından, bir bölümü de bağışlardan oluşuyor. Raflarda şimdi yüz yirmi beş (IV) çocuk kitabı ve 1980’lı (V) yıllardan kalma kitaplar da var.',
 'Bu parçada numaralanmış yerlerden hangisinin yazımı yanlıştır?',
 ['Yazıyla yazılan sayının sözcükleri ayrı yazılmıştır; doğrudur.',
  '“Kırk” sert “k” ile bittiği için ek “-ı” gelmiştir; kesmeyle ayrılması doğrudur.',
  'Akronim olan “TÜBİTAK” sözcük gibi okunur; ek okunuşa göre “-ın” gelir, doğrudur.',
  'Yazıyla yazılan “yüz yirmi beş” ayrı yazılmıştır; doğrudur.',
  None],
 'E','Yazımı yanlış olan numaralanmış yer.',
 'Rakamla yazılan sayıya gelen ekin ünlüsü, sayının okunuşundaki son ünlüye uyar.',[B_KS],
 [AD('Kuralı hatırla','Rakamlı sayıya ve kısaltmaya gelen ek okunuşa göre seçilir ve kesmeyle ayrılır; yazıyla yazılan sayılar ayrı yazılır.','1980’li · 40’ı · yüz yirmi beş'),
  AD('Numaraları sına','I “iki yüz elli” ✓ · II “40’ı” ✓ · III “TÜBİTAK’ın” ✓ · IV “yüz yirmi beş” ✓.','I–IV: doğru'),
  AD('Yanlışı bul','V’te 1980 “seksen” diye biter; son ünlü “e” ince olduğu için ek “-li” olmalı: “1980’li”. “1980’lı” yanlıştır.','V: 1980’li')],
 'Ek, sayının okunuşundaki son ünlüye uyar: seksen → 1980’li, yüz → 100’ü.')

# 0019 ken · kolay · A
S('0019','K-DBYZ-06','kolay','“-ken” ekinin bitişik yazıldığını bilir.',2,
 'Aşağıdaki cümlelerin hangisinde “-ken” yanlış yazılmıştır?',
 [('Kardeşim yürür ken ağlıyordu.',None),
  ('Biz çocukken bu parkta oynardık.','“Çocukken”deki “-ken” bitişik yazılmıştır; doğrudur.'),
  ('Yemek yerken konuşmamalısın.','“Yerken” bitişik yazılmıştır; doğrudur.'),
  ('Eve dönerken markete uğradım.','“Dönerken” bitişik yazılmıştır; doğrudur.'),
  ('Ben okuldayken o hâlâ uyuyordu.','“Okuldayken” bitişik yazılmıştır; doğrudur.')],
 'A','“-ken” yazımı yanlış olan cümle.',
 '“-ken” bir ektir; ayrı sözcük gibi yazılmaz.',[B_KEN],
 [AD('Kuralı hatırla','Zarf-fiil eki “-ken” kendinden önceki sözcüğe bitişik yazılır.','yürürken, çocukken'),
  AD('Şıkları sına','B, C, D, E’de “-ken” sözcüğe bitişik yazılmış.','B–E: doğru'),
  AD('Yanlışı bul','A’da “yürür ken” ayrı yazılmış; “yürürken” olmalıdır.','A: yürürken')],
 '“-ken” ek olduğu için asla sözcükten ayrılmaz.')

# 0020 leyin · orta · D
S('0020','K-DBYZ-06','orta','“-leyin” ekinin bitişik yazıldığını bilir.',3,
 'Aşağıdaki cümlelerden hangisinde “-leyin” ekinin yazımında hata yapılmıştır?',
 [('Dedem sabahleyin erkenden kalkardı.','“-leyin” bitişik yazılmıştır; doğrudur.'),
  ('Komşumuz yaz günleri akşamleyin sahile iner.','“Akşamleyin” bitişik yazılmıştır; doğrudur.'),
  ('Kediler geceleyin daha hareketli olur.','“Geceleyin” bitişik yazılmıştır; doğrudur.'),
  ('Pazar yeri sabah leyin kurulurdu.',None),
  ('Çoğu zaman öğleyin biraz dinlenirim.','“Öğleyin” tek sözcük olarak yazılmıştır; doğrudur.')],
 'D','Yazım yanlışı bulunan cümle.',
 '“-leyin” zaman bildiren bir ektir; ünlü uyumuna uymaz ve bitişik yazılır.',[B_KEN],
 [AD('Kuralı hatırla','Günün bölümlerine gelen “-leyin” eki sözcüğe bitişik yazılır ve değişmez.','sabahleyin, akşamleyin, geceleyin'),
  AD('Şıkları sına','A “sabahleyin”, B “akşamleyin”, C “geceleyin”, E “öğleyin” doğru yazılmış.','A, B, C, E: doğru'),
  AD('Yanlışı bul','D’de “sabah leyin” ayrı yazılmış; “sabahleyin” olmalıdır.','D: sabahleyin')],
 '“-leyin” de “-ken” gibi bir ektir; sözcükten ayrılmaz.')

# 0021 ile/ken · orta · numaralı · E
N('0021','K-DBYZ-06','orta','Parçada “-ken”, “-leyin” ve “ile” yazımlarını ayırt eder.',3,
 'Hafta sonu kardeşimle (I) bisiklet turuna çıktık. Yolda giderken (II) çok yoruldum, bu yüzden bir ağacın altında Elif ile (III) dinlendik. Akşamleyin (IV) hep birlikte köye döndük. Ben çocuk yken (V) bu yolları yürüyerek gelirdim.',
 'Bu parçada numaralanmış yerlerden hangisinin yazımı yanlıştır?',
 ['“İle” ek olarak “-le” biçiminde bitişik yazılmıştır; doğrudur.',
  '“-ken” fiile bitişik yazılmıştır; doğrudur.',
  '“İle” edatı ayrı yazılmıştır; doğrudur.',
  '“-leyin” bitişik yazılmıştır; doğrudur.',
  None],
 'E','Yazımı yanlış olan numaralanmış yer.',
 '“-ken” ekinin önündeki sözcüğe bak: “-y-” kaynaştırma ünsüzü ekin değil sözcüğün yanında durur.',[B_KEN],
 [AD('Kuralı hatırla','“-ken” ve “-leyin” bitişik yazılır; “ile” ya ayrı ya da “-le/-la” olarak bitişik yazılır.','giderken · sabahleyin · ile/-le'),
  AD('Numaraları sına','I “kardeşimle” ✓ · II “giderken” ✓ · III “Elif ile” ✓ · IV “Akşamleyin” ✓.','I–IV: doğru'),
  AD('Yanlışı bul','V’te “çocuk yken” ayrı yazılmış; “çocukken” olmalıdır.','V: çocukken')],
 '“Çocukken, gençken, evdeyken”: “-ken” her zaman bitişik yazılır.')

# 0022 ken+de · zor · numaralı · B
N('0022','K-DBYZ-06','orta','Parçada “-ken” eki ile bağlaç “de”nin ve “ile”nin yazımını ayırt eder.',4,
 'Dün sabah bisikletle (I) okula giderkende (II) lastiğim patladı. Neyse ki yanımda tamir takımı vardı, bu yüzden lastiği hemen söktüm. Tamir ederken (III) yanımdan geçen komşumuz Kerem Bey ile (IV) konuştum. O, gençken (V) bisiklet yarışlarına katılmış.',
 'Bu parçada numaralanmış yerlerden hangisinin yazımı yanlıştır?',
 ['“İle” eki “-le” biçiminde sözcüğe bitişik yazılmıştır; doğrudur.',
  None,
  '“-ken” ek olarak bitişik yazılmıştır; doğrudur.',
  '“İle” edatı ayrı yazılmıştır; “Kerem Bey ile” doğrudur.',
  '“Gençken” bitişik yazılmıştır; doğrudur.'],
 'B','Yazımı yanlış olan numaralanmış yer.',
 '“-ken”den sonra gelen “de” ayrı bir sözcüktür.',[B_KEN],
 [AD('Kuralı hatırla','“-ken” bitişik yazılır; ondan sonra gelen bağlaç “de” ise ayrı yazılır.','giderken de'),
  AD('Numaraları sına','I “bisikletle” ✓ · III “ederken” ✓ · IV “Kerem Bey ile” ✓ · V “gençken” ✓.','I, III, IV, V: doğru'),
  AD('Yanlışı bul','II’deki “giderkende”, “giderken” + bağlaç “de” birleşmiş yazılmıştır; “giderken de” olmalıdır.','II: giderken de')],
 '“-ken”e bağlaç “de” getiriliyorsa ayrı yazılır: “giderken de”.')

# 0023 düzeltme · orta · C
S('0023','K-DBYZ-07','orta','Düzeltme işaretinin gerektiği yerde kullanılmasını bilir.',3,
 'Aşağıdaki cümlelerin hangisinde düzeltme işareti (^) kullanılması gereken yerde kullanılmamıştır?',
 [('Dün bir kâğıt parçasına adresini yazdı.','“Kâğıt”ta “k” inceltilmiş; yazım doğrudur.'),
  ('Rüzgâr sabaha doğru dindi.','“Rüzgâr”da “g” inceltilmiş; yazım doğrudur.'),
  ('Yolculuk hala bitmedi.',None),
  ('Lâkin yarın gelemeyeceğini söyledi.','“Lâkin”de “l” inceltilmiş; yazım doğrudur.'),
  ('Hükûmet yeni bir karar açıkladı.','“Hükûmet”te uzun “û” işaretlenmiş; yazım doğrudur.')],
 'C','Düzeltme işareti kullanılması gerekirken kullanılmamış olan cümle.',
 '“Henüz” anlamındaki sözcük ile “babanın kız kardeşi” anlamındaki sözcük aynı yazılmaz.',[B_DZ],
 [AD('Kuralı hatırla','Düzeltme işareti k, g, l ünsüzlerini inceltir ve yazılışı aynı sözcükleri ayırır: hâlâ (henüz) / hala (akraba).','hâlâ ≠ hala'),
  AD('Şıkları sına','A kâğıt ✓ · B rüzgâr ✓ · D lâkin ✓ · E hükûmet ✓.','A, B, D, E: doğru'),
  AD('Eksiği bul','C’deki “hala” “henüz” anlamındadır; “hâlâ” yazılmalıdır.','C: hâlâ')],
 '“Henüz” anlamında “hâlâ” hep şapkalıdır; “hala” ise akraba adıdır.')

# 0024 düzeltme · orta · A
S('0024','K-DBYZ-07','orta','Yazılışı aynı, anlamı ayrı sözcüklerde düzeltme işaretini doğru kullanır.',3,
 'Aşağıdaki cümlelerin hangisinde düzeltme işareti yanlış kullanılmıştır?',
 [('Sepete üç âdet elma koydum.',None),
  ('Genç ozan memleketinin güzelliğine âşık olmuş.','“Âşık” sevdalı anlamındadır; şapkalı yazılması doğrudur.'),
  ('Köyümüzde bayramda mezarlıkları ziyaret etmek eski bir âdettir.','“Âdet” gelenek anlamında; şapkalı yazılması doğrudur.'),
  ('Halam hâlâ bizde kalıyor.','“Halam” akraba, “hâlâ” henüz anlamında; her ikisi de doğrudur.'),
  ('Bu yıl şirketin kârı arttı.','“Kâr” kazanç anlamında şapkalı yazılır; doğrudur.')],
 'A','Düzeltme işareti yanlış kullanılan cümle.',
 '“Adet” sözcüğünün hangi anlamında şapka gerektiğini düşün.',[B_DZ],
 [AD('Kuralı hatırla','âdet (gelenek) ve adet (sayı); âşık (sevdalı) ve aşık (oyun kemiği); kâr (kazanç) ve kar (yağış) ayrı yazılır.','âdet: gelenek · adet: sayı'),
  AD('Şıkları sına','B âşık ✓ · C âdet (gelenek) ✓ · D halam, hâlâ ✓ · E kâr (kazanç) ✓.','B, C, D, E: doğru'),
  AD('Yanlışı bul','A’da “üç âdet” sayı bildirir; şapkasız “adet” yazılmalıdır.','A: adet')],
 'Sayı bildiren “adet” şapkasızdır; gelenek anlamındaki “âdet” şapkalıdır.')

# 0025 düzeltme · zor · numaralı · D
N('0025','K-DBYZ-07','zor','Parçada düzeltme işaretinin yazımını bütün anlam ve ses durumlarıyla sınar.',4,
 'Müzede sergilenen eski bir kâğıt (I) parçasında hükûmetin (II) bir kararı yazılıydı. Lâkin (III) karar uygulanmamış, mahkum (IV) olan genç şair bağışlanmıştı. Bu belge hâlâ (V) vitrinde duruyor.',
 'Bu parçada numaralanmış yerlerden hangisinin yazımı yanlıştır?',
 ['“Kâğıt”ta “k” inceltilmiştir; doğrudur.',
  '“Hükûmet”te uzun “û” işaretlenmiştir; doğrudur.',
  '“Lâkin”de “l” inceltilmiştir; doğrudur.',
  None,
  '“Hâlâ” henüz anlamındadır; şapkalı yazılması doğrudur.'],
 'D','Yazımı yanlış olan numaralanmış yer.',
 'Hangi sözcükte uzun okunan ünlü işaretlenmelidir?',[B_DZ],
 [AD('Kuralı hatırla','Düzeltme işareti k, g, l ünsüzlerini inceltir ve yazılışı aynı sözcükleri ayırır.','kâğıt · hükûmet · lâkin · hâlâ'),
  AD('Numaraları sına','I kâğıt ✓ · II hükûmet ✓ · III lâkin ✓ · V hâlâ ✓.','I, II, III, V: doğru'),
  AD('Yanlışı bul','IV’teki “mahkum” sözcüğünde “u” uzun okunur ve “l” inceltilir; “mahkûm” olmalıdır.','IV: mahkûm')],
 '“Kâğıt”, “lâkin”, “hükûmet”, “mahkûm”: bu sözcüklerde şapka düşmez.')

bitir(Q)
