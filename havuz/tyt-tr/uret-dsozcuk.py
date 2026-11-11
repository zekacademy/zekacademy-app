"""TYT Türkçe · Sözcük Türleri genişletmesi: 41 soru (hafif mod). Metinler özgündür."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from hafif_db import *
import hafif_db
_soru0=hafif_db.soru
HATALAR=[]
def soru(*a,**k):
    try: _soru0(*a,**k)
    except AssertionError as e:
        HATALAR.append(e.args)
AD=A
KY='ÖSYM TYT Türkçe 2018–2026 · Bilgi Sarmal Dil Bilgisi SB (ÖSYM Tipi) · TDK Yazım Kılavuzu'
def kart(alt,fikir,tuzak,zor,kalip,adim,tip): return dict(alt=alt,fikir=fikir,tuzak=tuzak,zorluk=zor,kalip=kalip,adim=adim,tipId=tip,kaynak=KY)
KARTLAR={
 'K-DBST-01':kart('Ad: somut, soyut, topluluk, özel, cins','Adı anlam bakımından (somut/soyut, topluluk, özel/cins) sınıflamak; sıfatın ad görevine geçtiği yerleri bulmak.','Tekil görünen topluluk adını cins ad saymak; adlaşmış sıfatı sıfat saymak.','orta','öncüllü',3,'dst-ad'),
 'K-DBST-02':kart('Sıfat: niteleme ve belirtme','Niteleme ve belirtme (işaret, sayı, belgisiz, soru) sıfatlarını ve sıfat-fiillerin sıfat görevini ayırt etmek.','İsmin önünde duran işaret/soru sözcüğünü zamir sanmak; sıfat-fiili fiil saymak.','orta','öncüllü',3,'dst-sifat'),
 'K-DBST-03':kart('Zamir: kişi, dönüşlülük, işaret, belgisiz, soru, ilgi','Zamir türlerini tanımak; zamiri aynı sözcüğün sıfat kullanımından ayırmak.','Yanında isim bulunan bu/şu/hangi sözcüğünü zamir saymak; -ki’li sıfatı ilgi zamiri sanmak.','orta','öncüllü',3,'dst-zamir'),
 'K-DBST-04':kart('Zarf: durum, zaman, miktar, yer-yön, soru','Zarfın fiil, sıfat ya da zarfı niteleyen sözcük olduğunu ve alt türlerini bilmek.','Soru zarfını soru zamiri ya da soru sıfatı ile karıştırmak; zarfı sıfat saymak.','orta','öncüllü',3,'dst-zarf'),
 'K-DBST-05':kart('Edat','Edatları (gibi, için, göre, rağmen, doğru, başka…) tanımak ve aynı biçimli sıfat/zarf kullanımlarından ayırmak.','Doğru, başka, karşı gibi sözcüklerin her kullanımını edat saymak.','orta','öncüllü',3,'dst-edat'),
 'K-DBST-06':kart('Bağlaç: ve, ama, fakat, ki, de, ile','Bağlaçları anlam ilişkisine göre ayırmak; ile’nin bağlaç ve edat kullanımını, ki’yi ayırt etmek.','Ekleme bildiren ile’yi her durumda edat saymak; ilgi zamirini ya da -ki’li sıfatı bağlaç sanmak.','orta','öncüllü',3,'dst-baglac'),
 'K-DBST-07':kart('Türce farklı olan sözcük','Aynı biçimdeki sözcüğün farklı cümlelerde farklı türde kullanılmasından yararlanarak türce farklı olanı bulmak.','Sözcüğün türünü cümleye bakmadan yargılamak.','zor','öncüllü',4,'dst-farkli'),
 'K-DBST-08':kart('Ortak özellik: iki sözcüğün türü','Aynı cümlede ya da parçada iki sözcüğün türlerini birlikte değerlendirmek.','Yalnız tek sözcüğü çözüp ikinciyi gözden kaçırmak.','zor','öncüllü',4,'dst-ortak'),
}
TIPLER={'dst-ad':'Ad (somut, soyut, topluluk, özel, cins)','dst-sifat':'Sıfat (niteleme, belirtme, sıfat-fiil)','dst-zamir':'Zamir (adıl)','dst-zarf':'Zarf','dst-edat':'Edat','dst-baglac':'Bağlaç','dst-farkli':'Türce farklı olan sözcük','dst-ortak':'Ortak özellik (iki sözcüğün türü)'}
Q=kur('dsozcuk','Sözcük Türleri','tr|Sözcük Türleri',KARTLAR,TIPLER); Q.n=41
ROMS=['I','II','III','IV','V']
def fmt(l): return ' + '.join(l) if isinstance(l,tuple) else l

def C5(no,kart,zor,kaz,adim,kok,opts,harf,kural,istenen,ip,bilgi,kuraltxt,kisa,puf):
    """5 cümle: opts=[(cümle,etiket,gerekçe)] A–E. kural(etiket) tam bir şıkta doğru."""
    ix='ABCDE'.index(harf); assert [i for i,o in enumerate(opts) if kural(o[1])]==[ix],(no,'kural')
    so=[(o[0],D if i==ix else Y,o[2],'bilgi' if i%2 else 'dikkat') for i,o in enumerate(opts)]
    ad=[AD('Ölçütü hatırla',kuraltxt,kisa),
        AD('Şıkları tek tek çözümle','Her şıkta tırnaklı sözcüğün cümledeki göreve göre türü belirlenir.',' · '.join(f'{"ABCDE"[i]}: {fmt(o[1])}' for i,o in enumerate(opts))),
        AD('Doğru şıkkı seç',opts[ix][2],f'{harf}: {fmt(opts[ix][1])} ✓')]
    soru(Q,no,kart,zor,kaz,adim,kok,so,harf,lambda e:e==D,istenen,ip,bilgi,ad,puf)

def P(no,kart,zor,kaz,adim,parca,kok,items,harf,kural,istenen,ip,bilgi,kuraltxt,kisa,puf):
    """Numaralı parça: items=[(sözcük,tür,gerekçe)]×5; harf numaranın konumu."""
    ix='ABCDE'.index(harf); assert len(items)==5 and [i for i,o in enumerate(items) if kural(o[1])]==[ix],(no,'kural')
    so=[(ROMS[i],D if i==ix else Y,f'“{o[0]}” ({o[1]}): {o[2]}. Aranan sözcük bu değildir.','bilgi' if i%2 else 'dikkat') for i,o in enumerate(items)]
    ad=[AD('Ölçütü hatırla',kuraltxt,kisa),
        AD('Numaraları tek tek çözümle','Her numaralı sözcüğün parçadaki göreve göre türü belirlenir.',' · '.join(f'{ROMS[i]}: {o[0]} {o[1]}' for i,o in enumerate(items))),
        AD('Doğru numarayı seç',f'“{items[ix][0]}”: {items[ix][2]}.',f'{ROMS[ix]}: {items[ix][1]} ✓')]
    soru(Q,no,kart,zor,kaz,adim,parca+'\n'+kok,so,harf,lambda e:e==D,istenen,ip,bilgi,ad,puf,kalip='öncüllü')

B_AD=B('Ad (isim)','somut ad beş duyuyla algılanır (kitap) · soyut ad algılanmaz, düşünülür (sevgi) · topluluk adı tekil biçimiyle birden çok varlığı anlatır (sürü, ordu)')
B_OC=B('Özel ve cins ad','özel ad tek varlığa verilir (Ankara, Elif) · cins ad aynı türün tümüne verilir (şehir, kuş)')
B_ADL=B('Adlaşma','sıfat ismin yerine geçip ad görevinde kullanılırsa ad olur · yaşlı adam (sıfat), yaşlılar geldi (ad)')
B_SF=B('Sıfat','ismi niteler (niteleme: soğuk hava) ya da belirtir (işaret: bu, şu · sayı: üç · belgisiz: bazı · soru: hangi, kaç)')
B_SFF=B('Sıfat-fiil','-an, -ası, -mış, -ecek gibi ekler fiilden sıfat yapar; ismi niteliyorsa sıfat görevindedir · koşan çocuk')
B_ZM=B('Zamir (adıl)','ismin yerini tutar: kişi (ben), dönüşlülük (kendi), işaret (bunu), belgisiz (herkes), soru (kim), ilgi (seninki) · ismi niteliyorsa sıfattır (bu kitap)')
B_ZF=B('Zarf','fiili, sıfatı ya da başka bir zarfı niteler: durum (yavaş), zaman (yarın), miktar (oldukça), yer-yön (içeri), soru (niçin)')
B_ED=B('Edat','tek başına anlamı olmayan, bağlandığı sözcükle görev yapan sözcük: gibi, için, göre, rağmen, ile (araç, birliktelik)')
B_BG=B('Bağlaç','sözcükleri ya da cümleleri bağlar: ve, ama, fakat, çünkü, veya, ki · ile, “ve” yerine konabiliyorsa bağlaçtır (kalem ile defter)')

# ===== K1 AD =====
C5('0001','K-DBST-01','kolay','Tırnaklı sözcüğün topluluk adı olduğu cümleyi bulur.',2,
 'Tırnak içine alınan sözcüklerden hangisi bir topluluk adıdır?',
 [('Bahçedeki “çocuklar” ağaca tırmandı.','çoğul cins ad','“Çocuklar”, çoğul eki almış bir cins addır; tek başına topluluk anlamı yoktur.'),
  ('Masanın üstünde “kitap” duruyordu.','somut cins ad','“Kitap”, tek bir varlığı anlatan somut bir cins addır.'),
  ('Yamaçtaki “sürü” ağıla döndü.','topluluk adı','“Sürü”, tekil biçimiyle birçok hayvanı birden anlatır; topluluk adıdır.'),
  ('“Sevgi” insanı güzelleştirir.','soyut ad','“Sevgi”, duyularla algılanmayan soyut bir addır.'),
  ('“Ankara” kışın soğuk olur.','özel ad','“Ankara”, tek bir şehre verilmiş özel addır.')],
 'C',lambda t:t=='topluluk adı','Tırnaklı sözcüğün topluluk adı olduğu cümle.',
 'Tekil biçimde olup birçok varlığı bir arada anlatan sözcüğü ara.',[B_AD],
 'Topluluk adı tekil biçimiyle birden çok varlığı anlatır.','topluluk adı: sürü, ordu, koro','Tekil görünüp çokluk bildiren ad topluluk adıdır; çoğul ekli sözcük topluluk adı sayılmaz.')

P('0002','K-DBST-01','orta','Parçadaki adlardan soyut olanı belirler.',3,
 'Kış boyunca karla kaplı kalan köyde, bahar gelince herkesin yüzünde bir umut (I) belirdi. Çocuklar dere (II) kıyısında oyun oynadı, kadınlar taş fırında ekmek (III) pişirdi, erkekler bahçenin kapısını ve çiti (IV) onardı. Akşam olunca sofraya oturuldu; kimse çorba (V) içmeye acele etmedi.',
 'Bu parçada numaralanmış sözcüklerden hangisi soyut addır?',
 [('umut','soyut ad','duyularla algılanmaz, yalnız düşünülür'),('dere','somut ad','gözle görülür, bir yer adı'),('ekmek','somut ad','dokunulup tadılabilir'),('çiti','somut ad','görülüp dokunulabilir'),('çorba','somut ad','tadılabilir, görülür')],
 'A',lambda t:t=='soyut ad','Soyut ad olan numaralı sözcük.',
 'Hangisini gözle görüp eline alamazsın?',[B_AD],
 'Soyut ad beş duyuyla algılanamayan, yalnız zihinde var olan varlıkları adlandırır.','soyut: umut, sevgi, korku','Beş duyunun hiçbiriyle algılanamayan ad soyuttur.')

C5('0003','K-DBST-01','orta','İki tırnaklı adın soyut–somut sırasını belirler.',3,
 'Hangi cümlede tırnaklı adlardan birincisi soyut, ikincisi somut anlamlıdır?',
 [('“Korku” ve “umut” aynı yürekte yaşar.',('soyut','soyut'),'“Korku” da “umut” da algılanmayan, soyut adlardır; ikincisi somut değildir.'),
  ('Yamaçtaki “ağaç” “kuşlara” yuva oldu.',('somut','somut'),'“Ağaç” ve “kuşlar” görülebilen somut adlardır; ilki soyut değildir.'),
  ('Kerem “kitabı” bitirince “mutluluk” duydu.',('somut','soyut'),'Sıra ters: “kitap” somut, “mutluluk” soyuttur; istenen soyut–somut sırasıdır.'),
  ('“Sevgi” ve “saygı” komşuluğun temelidir.',('soyut','soyut'),'“Sevgi” de “saygı” da soyut addır; ikincisi somut değildir.'),
  ('“Özgürlük” isteyen kuş “kafesten” kaçtı.',('soyut','somut'),'“Özgürlük” soyut, “kafes” somut addır.')],
 'E',lambda t:t==('soyut','somut'),'İlki soyut, ikincisi somut ad olan cümle.',
 'Her tırnaklı sözcüğü ayrı ayrı sına; sıraya da dikkat et.',[B_AD],
 'Aranan sıra: önce soyut, sonra somut ad.','soyut: algılanmaz · somut: algılanır','İki sözcüklü sorularda hem türleri hem sırayı denetle.')

P('0004','K-DBST-01','orta','Sıfatın ad görevinde kullanıldığı sözcüğü bulur.',4,
 'Eski (I) kütüphanenin kapısında bekleyen yaşlı (II) içeri alındı. Raflarda tozlu (III) kitaplar, renkli (IV) haritalar ve kalın (V) ciltler duruyordu.',
 'Bu parçada numaralanmış sözcüklerden hangisi ad görevinde kullanılmıştır?',
 [('Eski','sıfat','“eski kütüphane” biçiminde ismi niteler'),('yaşlı','ad','“bekleyen” sözcüğünün nitelediği isimdir; sıfat ismin yerine geçip özne olmuş, adlaşmıştır'),('tozlu','sıfat','“tozlu kitaplar” biçiminde ismi niteler'),('renkli','sıfat','“renkli haritalar” biçiminde ismi niteler'),('kalın','sıfat','“kalın ciltler” biçiminde ismi niteler')],
 'B',lambda t:t=='ad','Ad görevinde olan numaralı sözcük.',
 'Hangi sözcüğün ardında nitelediği bir isim yok?',[B_ADL],
 'Nitelediği isim düşen sıfat, ismin yerini tutarsa ad görevindedir.','sıfat + isim → sıfat; sıfat tek başına öge → ad','Sıfat tek başına özne ya da nesneyse adlaşmıştır.')

C5('0005','K-DBST-01','kolay','Tırnaklı sözcüğün cins ad olduğu cümleyi bulur.',2,
 'Cins ad olarak kullanılan sözcük, hangi cümlede tırnak içine alınmıştır?',
 [('“Elif” bu akşam bize gelecek.','özel ad','“Elif”, tek bir kişiye verilmiş özel addır.'),
  ('“Karadeniz” yaz aylarında kalabalıktır.','özel ad','“Karadeniz”, tek bir denizin özel adıdır.'),
  ('Yıllar sonra “Sakarya” kıyısına döndü.','özel ad','“Sakarya”, bir ırmağın özel adıdır.'),
  ('“Kuş” pencereden içeri girdi.','cins ad','“Kuş”, aynı türün tümüne verilen ortak bir addır.'),
  ('“Kerem” sınavı birinci bitirdi.','özel ad','“Kerem”, bir kişi adı olduğundan özel addır.')],
 'D',lambda t:t=='cins ad','Cins ad olan tırnaklı sözcük.',
 'Tek bir varlığa mı, yoksa bir türün tümüne mi verilmiş ad?',[B_OC],
 'Aynı türdeki varlıkların hepsine verilen ad cins addır.','özel: tek varlık · cins: tür','Büyük harfle başlayan kişi, yer adları özel; türü anlatan ortak adlar cinstir.')

P('0006','K-DBST-01','orta','Parçadaki topluluk adını belirler.',3,
 'Cumartesi sabahı otobüs (I) kalkarken öğrenci kafilesi (II) şarkılar söylüyordu. Yamaçlara (III) varınca Uludağ’ın (IV) karlı zirvesi göründü; herkes büyük bir sevinç (V) duydu.',
 'Bu parçada numaralanmış sözcüklerden hangisi topluluk adıdır?',
 [('otobüs','somut cins ad','tek bir taşıtı anlatır'),('kafile','topluluk adı','tekil biçimiyle birçok kişiyi bir arada anlatır'),('Yamaçlara','somut cins ad','bir yer şeklini anlatan ortak ad; çoğul ek almıştır'),('Uludağ’ın','özel ad','tek bir dağın adıdır'),('sevinç','soyut ad','algılanmayan bir duygudur')],
 'B',lambda t:t=='topluluk adı','Topluluk adı olan numaralı sözcük.',
 'Tekil olduğu hâlde birçok kişiyi anlatan sözcüğü ara.',[B_AD],
 'Topluluk adı tekil biçimiyle birden çok varlığı anlatır.','topluluk adı: kafile, sürü, ordu','Çoğul eki almadan “birçok” anlamı veren ad topluluk adıdır.')

# ===== K2 SIFAT =====
C5('0007','K-DBST-02','kolay','Belgisiz sıfatı diğer sıfat türlerinden ayırır.',2,
 'Varlıkların sayısını belirsiz bırakan sıfat, hangi cümlede tırnak içindedir?',
 [('Parkta “bazı” çocuklar oynuyordu.','belgisiz sıfat','“Bazı”, “çocuklar” ismini belirsiz bir sayıyla belirtir; belgisiz sıfattır.'),
  ('Raftan “bu” kitabı dün aldım.','işaret sıfatı','“Bu”, “kitap” ismini işaret ederek belirtir; işaret sıfatıdır.'),
  ('Elif “yeşil” bir kazak giymişti.','niteleme sıfatı','“Yeşil”, “kazak” ismini renk bakımından niteler; niteleme sıfatıdır.'),
  ('Sen “hangi” yolu seçtin?','soru sıfatı','“Hangi”, “yol” ismini soruyla belirtir; soru sıfatıdır.'),
  ('Sınıfa “dört” yeni öğrenci geldi.','sayı sıfatı','“Dört”, “öğrenci” ismini sayısıyla belirtir; sayı sıfatıdır.')],
 'A',lambda t:t=='belgisiz sıfat','Belgisiz sıfat olan tırnaklı sözcük.',
 'Sayısı ya da miktarı belirsiz bırakan sözcüğü ara.',[B_SF],
 'Belgisiz sıfat varlıkların sayısını belirsiz bırakarak belirtir (bazı, birkaç, her).','belgisiz sıfat: bazı, birkaç, her, bütün','Belirsizlik bildiren, isimden önce gelen sözcük belgisiz sıfattır.')

C5('0008','K-DBST-02','kolay','Niteleme sıfatını belirtme sıfatlarından ayırır.',3,
 'İsme bir özellik katan (niteleme) sıfat, tırnak içinde hangisinde verilmiştir?',
 [('“Şu” evde kimse oturmuyor.','işaret sıfatı','“Şu”, “ev” ismini işaret eder; belirtme sıfatıdır, nitelik bildirmez.'),
  ('Sınıfa “iki” öğrenci katıldı.','sayı sıfatı','“İki”, sayı bildirir; belirtme sıfatıdır.'),
  ('“Kaç” kişi geldi?','soru sıfatı','“Kaç”, “kişi” ismini soruyla belirtir; belirtme sıfatıdır.'),
  ('“Soğuk” bir rüzgâr esiyordu.','niteleme sıfatı','“Soğuk”, “rüzgâr” ismine bir nitelik katar; niteleme sıfatıdır.'),
  ('Sınavda “birkaç” soru zordu.','belgisiz sıfat','“Birkaç”, soruların sayısını belirsiz bırakır; belirtme sıfatıdır.')],
 'D',lambda t:t=='niteleme sıfatı','Niteleme sıfatı olan tırnaklı sözcük.',
 'İsme sayı ya da yer göstermeyip özellik katan sözcüğü seç.',[B_SF],
 'Niteleme sıfatı ismin renk, biçim, durum gibi özelliğini bildirir.','niteleme: özellik · belirtme: işaret, sayı, belgisiz, soru','Özellik bildiriyorsa niteleme, sayı/işaret/belirsizlik/soru bildiriyorsa belirtme sıfatıdır.')

C5('0009','K-DBST-02','zor','Fiilden türeyen sıfat-fiilin sıfat görevini bulur.',4,
 'Fiil kökünden türediği hâlde bir ismi niteleyen sözcük, hangi cümlede tırnak içindedir?',
 [('Kitabı “okuyarak” öğrendi.','zarf görevli zarf-fiil','“Okuyarak”, “öğrendi” fiilini niteler; zarf-fiildir, zarf görevindedir.'),
  ('“Okumak” insanı geliştirir.','ad görevli isim-fiil','“Okumak”, cümlenin öznesi olan isim-fiildir; ad görevindedir.'),
  ('“Koşan” çocuk yorulup durdu.','sıfat görevli sıfat-fiil','“Koşan”, “çocuk” ismini niteler; sıfat-fiildir, sıfat görevindedir.'),
  ('“Yazar” yeni romanını tanıttı.','kalıcı ad','“Yazar”, fiil kökünden türemiş olsa da kalıcı ad olmuştur; fiilimsi değildir, ismi de niteleyen bir sözcük değildir.'),
  ('“Çalışanlar” erkenden işe başladı.','ad görevli sıfat-fiil','“Çalışanlar”, sıfat-fiilin adlaşmış hâlidir; cümlenin öznesi olarak ad görevindedir.')],
 'C',lambda t:t=='sıfat görevli sıfat-fiil','Sıfat görevinde olan fiilden türemiş sözcük.',
 'İsmin önünde duran, o ismi niteleyen sözcüğü bul.',[B_SFF],
 'Fiilimsinin görevi, cümlede ne işe yaradığıyla belirlenir.','sıfat-fiil + isim → sıfat','Fiilimsi ismi niteliyorsa sıfat, fiili niteliyorsa zarf, özne ya da nesneyse ad görevindedir.')

P('0010','K-DBST-02','zor','Parçada sıfat olmayan sözcüğü bulur.',4,
 'Şehir müzesinde büyük (I) bir sergi açıldı. İki (II) ressamın bazı (III) eserleri, ilginç (IV) bir heykel ve bir seramik grubu salonda yer aldı. Sergiyi gezenler (V) tabloları uzun uzun inceledi.',
 'Bu parçada numaralanmış sözcüklerden hangisi sıfat değildir?',
 [('büyük','niteleme sıfatı','“büyük sergi” biçiminde ismi niteler'),('İki','sayı sıfatı','“iki ressam” biçiminde ismi belirtir'),('bazı','belgisiz sıfat','“bazı eserler” biçiminde ismi belirtir'),('ilginç','niteleme sıfatı','“ilginç heykel” biçiminde ismi niteler'),('gezenler','ad','“gezen” sıfat-fiili ismin yerine geçip özne olmuştur; adlaşmıştır')],
 'E',lambda t:t=='ad','Sıfat olmayan numaralı sözcük.',
 'Hangi sözcük bir ismi nitelemiyor, kendisi bir öge?',[B_SF,B_ADL],
 'Sıfat bir ismi niteler ya da belirtir; tek başına özne olan sözcük ad görevindedir.','sıfat: isim niteler · tek başına öge: ad','İsmi nitelemeyen, kendisi özne ya da nesne olan sözcük sıfat değildir.')

C5('0011','K-DBST-02','orta','İki tırnaklı sözcüğün zarf–sıfat sırasını belirler.',3,
 'İlki fiili, ikincisi ismi niteleyen tırnaklı sözcükler hangi cümlededir?',
 [('“Kısa” bir yolu “hızlı” yürüdük.',('sıfat','zarf'),'“Kısa”, “yol” ismini niteler (sıfat); “hızlı”, “yürüdük” fiilini niteler (zarf). Sıra ters.'),
  ('Rüzgâr “sert” esti, “kuru” yapraklar savruldu.',('zarf','sıfat'),'“Sert”, “esti” fiilini niteler (zarf); “kuru”, “yapraklar” ismini niteler (sıfat).'),
  ('Çocuk “erken” kalkıp “iyi” uyudu.',('zarf','zarf'),'“Erken” ve “iyi” fiilleri niteler; ikisi de zarftır.'),
  ('“Sıcak” çorbayı “tatlı” bir gülümsemeyle sundu.',('sıfat','sıfat'),'“Sıcak” çorbayı, “tatlı” gülümsemeyi niteler; ikisi de sıfattır.'),
  ('“Yaşlı” kadın “torununa” baktı.',('sıfat','ad'),'“Yaşlı” sıfat; “torun” ise ad soylu bir sözcüktür, zarf değildir.')],
 'B',lambda t:t==('zarf','sıfat'),'İlki zarf, ikincisi sıfat olan cümle.',
 'Önce fiili, sonra ismi niteleyen sözcüğü ara.',[B_SF,B_ZF],
 'Aranan sıra: fiili niteleyen (zarf), sonra ismi niteleyen (sıfat).','zarf → fiil · sıfat → isim','Her sözcüğün neyi nitelediğine bak, sonra sıraya bak.')

P('0012','K-DBST-02','orta','Parçada sayı sıfatını belirler.',3,
 'Yüksek (I) dağların eteğinde bazı (II) gruplar kamp kurmuştu. Akşam üç (III) çadırın önünde ateş yakıldı; bu (IV) sıcaklık herkese iyi geldi. Sabaha kadar her (V) çadırdan şarkı sesi yükseldi.',
 'Bu parçada numaralanmış sözcüklerden hangisi sayı sıfatıdır?',
 [('Yüksek','niteleme sıfatı','“yüksek dağlar” biçiminde nitelik bildirir'),('bazı','belgisiz sıfat','“bazı gruplar” biçiminde belirsizlik bildirir'),('üç','sayı sıfatı','“üç çadır” biçiminde sayı bildirir'),('bu','işaret sıfatı','“bu sıcaklık” biçiminde işaret bildirir'),('her','belgisiz sıfat','“her çadır” biçiminde belirsizlik bildirir')],
 'C',lambda t:t=='sayı sıfatı','Sayı sıfatı olan numaralı sözcük.',
 'İsmin kaç tane olduğunu belirten sözcüğü ara.',[B_SF],
 'Sayı sıfatı varlıkların sayısını kesin olarak belirtir (üç çadır).','sayı sıfatı: iki, üç, ilk, ikişer','Sayıyı kesin bildiren, isimden önce gelen sözcük sayı sıfatıdır.')

# ===== K3 ZAMİR =====
C5('0013','K-DBST-03','kolay','Dönüşlülük zamirini diğer zamir türlerinden ayırır.',2,
 'Eylemin yapana döndüğünü gösteren zamir, hangi cümlede tırnak içine alınmıştır?',
 [('“Sen” bu akşam bize mutlaka gel.','kişi zamiri','“Sen”, ikinci kişinin yerini tutan kişi zamiridir.'),
  ('“Bunu” sana geçen hafta ben aldım.','işaret zamiri','“Bunu”, yakındaki bir varlığı gösterip adının yerini tutar; işaret zamiridir.'),
  ('“Herkes” erkenden salona girdi.','belgisiz zamir','“Herkes”, kimlikleri belirsiz bir topluluğun yerini tutar; belgisiz zamirdir.'),
  ('“Kim” bu saatte kapıyı çaldı?','soru zamiri','“Kim”, kişiyi sormak için kullanılan soru zamiridir.'),
  ('Elif “kendini” aynada izledi.','dönüşlülük zamiri','“Kendini”, eylemi yapanın kendisine döndüğünü gösteren dönüşlülük zamiridir.')],
 'E',lambda t:t=='dönüşlülük zamiri','Dönüşlülük zamiri olan tırnaklı sözcük.',
 'İş yapanın kendisine döndüğü sözcüğü bul.',[B_ZM],
 'Dönüşlülük zamiri “kendi” sözcüğüdür; eylemin yapanın kendisine döndüğünü gösterir.','kendi (+ ek) → dönüşlülük zamiri','“Kendi” ve ekli biçimleri dönüşlülük zamiridir.')

P('0014','K-DBST-03','orta','Parçada zamir olmayan sözcüğü bulur.',3,
 'Bu (I) romanı bana Elif verdi; ben (II) de hemen okumaya başladım. Sayfaları çevirirken kendimi (III) hikâyenin içinde buldum. Kimse (IV) rahatsız etmesin diye kapıyı kapattım. Sonunda bunu (V) herkese önerdim.',
 'Bu parçada numaralanmış sözcüklerden hangisi zamir değildir?',
 [('Bu','işaret sıfatı','“bu roman” biçiminde isim niteler; ismin yerini tutmaz'),('ben','kişi zamiri','birinci kişinin yerini tutar'),('kendimi','dönüşlülük zamiri','eylemin yapana döndüğünü gösterir'),('Kimse','belgisiz zamir','belirsiz bir kişinin yerini tutar'),('bunu','işaret zamiri','yakın bir varlığın yerini tutar')],
 'A',lambda t:t=='işaret sıfatı','Zamir olmayan numaralı sözcük.',
 'Yanında nitelediği bir isim bulunan sözcüğü ara.',[B_ZM],
 'Zamir ismin yerini tutar; ismi niteleyen sözcük sıfattır.','yerini tutuyor → zamir · niteliyor → sıfat','Aynı biçimdeki sözcük isimle birlikteyse sıfat, tek başınaysa zamirdir.')

C5('0015','K-DBST-03','orta','İlgi zamirini -ki’li sıfatlardan ve öteki zamirlerden ayırır.',3,
 'Tırnaklı sözcüklerden hangisi, bir ismin yerini tutan -ki’li bir zamirdir?',
 [('“Bugünkü” toplantı kısa sürdü.','sıfat','“Bugünkü”, “toplantı” ismini niteler; sıfattır, ismin yerini tutmaz.'),
  ('“Hiçbiri” yarın gelmeyecek.','belgisiz zamir','“Hiçbiri”, ismin yerini tutar ama -ki’li değildir; belgisiz zamirdir.'),
  ('Haberleri “dünkü” gazeteden okudum.','sıfat','“Dünkü”, “gazete” ismini niteler; sıfattır.'),
  ('Defterim eksik, “seninki” tam.','ilgi zamiri','“Seninki”, “senin defterin” sözünün yerini tutar; ilgi zamiridir.'),
  ('“Duvardaki” resim çok eskiydi.','sıfat','“Duvardaki”, “resim” ismini niteler; sıfattır.')],
 'D',lambda t:t=='ilgi zamiri','İlgi zamiri olan tırnaklı sözcük.',
 'Hangi -ki’li sözcüğün yanında nitelediği isim yok?',[B_ZM],
 'İlgi zamiri, ismin yerini tutan -ki’li sözcüktür (seninki); isim niteleyen -ki’li sözcük sıfattır.','-ki + isim → sıfat · -ki tek başına → zamir','-ki’li sözcüğün ardındaki isme bak: varsa sıfat, yoksa zamir.')

C5('0016','K-DBST-03','zor','İki belgisiz sözcüğün zamir–sıfat sırasını belirler.',4,
 'Tırnaktaki iki sözcükten birincisi ismin yerini tutuyor, ikincisi ismi niteliyorsa aranan cümle hangisidir?',
 [('“Kimi” çocuklar sustu, “kimi” oynadı.',('sıfat','zamir'),'İlk “kimi”, “çocuklar” ismini niteler (sıfat); ikincisi ismin yerini tutar (zamir). Sıra ters.'),
  ('“Kimi” geldi, “bazı” konuklar kaldı.',('zamir','sıfat'),'İlk “kimi”, ismin yerini tutar (belgisiz zamir); “bazı”, “konuklar” ismini niteler (sıfat).'),
  ('“Birkaç” kişi geldi, “bazı” konuklar da gitti.',('sıfat','sıfat'),'İkisi de bir isim belirtir: birkaç kişi, bazı konuklar. İkisi de sıfattır.'),
  ('“Hepsi” geldi, “kimisi” gitti.',('zamir','zamir'),'İkisi de ismin yerini tutar. İkisi de zamirdir.'),
  ('“Birkaç” arkadaş geldi, “hepsi” sevindi.',('sıfat','zamir'),'“Birkaç”, “arkadaş” ismini niteler (sıfat); “hepsi”, ismin yerini tutar (zamir). Sıra ters.')],
 'B',lambda t:t==('zamir','sıfat'),'İlki zamir, ikincisi sıfat olan cümle.',
 'Her sözcüğün yanında bir isim olup olmadığına bak.',[B_ZM],
 'Aranan sıra: önce ismin yerini tutan (zamir), sonra ismi niteleyen (sıfat).','yerini tutar → zamir · isim niteler → sıfat','Çift sorularında her sözcüğü ayrı çöz, sonra sıraya bak.')

P('0017','K-DBST-03','orta','Parçada belgisiz zamiri belirler.',3,
 'Biz (I) kulübe varınca kendimizi (II) salona attık. Masanın başında biri (III) oturmuş gazete okuyordu. Ona selam verdik; o da bize şunu (IV) sordu: “Bugün ne (V) yaptınız?”',
 'Bu parçada numaralanmış sözcüklerden hangisi belgisiz zamirdir?',
 [('Biz','kişi zamiri','birinci çoğul kişinin yerini tutar'),('kendimizi','dönüşlülük zamiri','eylemin yapana döndüğünü gösterir'),('biri','belgisiz zamir','kim olduğu belli olmayan bir kişinin yerini tutar'),('şunu','işaret zamiri','gösterilen bir şeyin yerini tutar'),('ne','soru zamiri','bir şeyi sormak için kullanılır')],
 'C',lambda t:t=='belgisiz zamir','Belgisiz zamir olan numaralı sözcük.',
 'Kim olduğu belli olmayan bir kişiyi anlatan sözcük hangisi?',[B_ZM],
 'Belgisiz zamir, belirsiz bir kişi ya da varlığın yerini tutar (biri, kimse, hepsi).','belgisiz zamir: biri, kimse, hepsi, herkes','Kimliği belli olmayan kişi ya da şeyin yerini tutan sözcük belgisiz zamirdir.')

P('0018','K-DBST-03','orta','Soru zamirini soru sıfatı ve soru zarfından ayırır.',4,
 'Resepsiyondaki görevli yeni gelen misafirlere şunları sordu: “Rezervasyonu kim (I) yaptı? Hangi (II) odayı istiyorsunuz? Kaç (III) kişi kalacaksınız? Yolculuk nasıl (IV) geçti? Niçin (V) geciktiniz?”',
 'Bu parçada numaralanmış sözcüklerden hangisi soru zamiridir?',
 [('kim','soru zamiri','rezervasyonu yapan kişinin yerini tutarak soru sorar'),('Hangi','soru sıfatı','“hangi oda” biçiminde ismi belirtir'),('kaç','soru sıfatı','“kaç kişi” biçiminde ismi belirtir'),('nasıl','soru zarfı','“geçti” fiilini niteler'),('Niçin','soru zarfı','“geciktiniz” fiilini niteler')],
 'A',lambda t:t=='soru zamiri','Soru zamiri olan numaralı sözcük.',
 'Hangisi yanında isim almadan kişinin yerini tutuyor?',[B_ZM,B_ZF],
 'Soru sözcüğü isim yerini tutarsa zamir, isim niteliyorsa sıfat, fiil niteliyorsa zarftır.','yerini tutar → zamir · isim niteler → sıfat · fiil niteler → zarf','Soru sözcüğünün neyle ilişkili olduğuna bak.')

# ===== K4 ZARF =====
C5('0019','K-DBST-04','kolay','Zaman zarfını diğer zarf türlerinden ayırır.',2,
 'Eylemin zamanını bildiren zarf, hangi cümlede tırnak içinde verilmiştir?',
 [('Misafirler “içeri” girdi.','yer-yön zarfı','“İçeri”, “girdi” fiilinin yönünü bildirir; yer-yön zarfıdır.'),
  ('Sınıf “oldukça” sessizdi.','miktar zarfı','“Oldukça”, “sessiz” sıfatının derecesini bildirir; miktar zarfıdır.'),
  ('Kerem “güzel” konuştu.','durum zarfı','“Güzel”, “konuştu” fiilinin nasıl yapıldığını bildirir; durum zarfıdır.'),
  ('Kitabı “yarın” getireceğim.','zaman zarfı','“Yarın”, “getireceğim” fiilinin zamanını bildirir; zaman zarfıdır.'),
  ('“Niçin” aradın?','soru zarfı','“Niçin”, “aradın” fiilinin nedenini sorar; soru zarfıdır.')],
 'D',lambda t:t=='zaman zarfı','Zaman zarfı olan tırnaklı sözcük.',
 'Eylemin ne zaman olduğunu bildiren sözcüğü ara.',[B_ZF],
 'Zaman zarfı eylemin ne zaman olduğunu bildirir (yarın, şimdi, dün).','zaman zarfı: ne zaman?','Fiile “ne zaman?” diye sorunca cevap veren sözcük zaman zarfıdır.')

C5('0020','K-DBST-04','zor','Başka bir zarfı niteleyen zarfı bulur.',4,
 'Bir zarfı niteleyen zarf, hangi cümlede tırnak içindedir?',
 [('Kış bu yıl “erken” bastırdı.','fiili niteleyen zarf','“Erken”, “bastırdı” fiilini niteler; zarfı değil fiili niteleyen zarftır.'),
  ('Evde “çok” kitap ve defter var.','belgisiz sıfat','“Çok”, “kitap” ismini belirtir; sıfattır, zarf değildir.'),
  ('Bu konu bugün “çok” zordu.','sıfatı niteleyen zarf','“Çok”, “zor” sıfatının derecesini bildirir; sıfatı niteleyen zarftır, zarfı değil.'),
  ('Bu kitabı hepimiz “çok” sevdik.','fiili niteleyen zarf','“Çok”, “sevdim” fiilini niteler; fiili niteleyen zarftır.'),
  ('Kerem yarışı “pek” hızlı bitirdi.','zarfı niteleyen zarf','“Pek”, “hızlı” durum zarfının derecesini bildirir; zarfı niteleyen zarftır.')],
 'E',lambda t:t=='zarfı niteleyen zarf','Bir zarfı niteleyen zarfın olduğu cümle.',
 'Tırnaklı sözcüğün nitelediği sözcüğün de fiili niteleyip nitelemediğine bak.',[B_ZF],
 'Zarf yalnız fiili değil, sıfatı ve başka bir zarfı da niteleyebilir.','pek hızlı bitirdi: zarf → zarf','Tırnaklı sözcüğün nitelediği sözcüğün türüne bak: o da zarfsa aranan cümledir.')

P('0021','K-DBST-04','orta','Parçada yer-yön zarfını belirler.',3,
 'Gezi otobüsünden inen çocuklar hemen (I) okula yöneldi. Kapıdan içeri (II) girip sessizce (III) sıraya dizildiler. Oldukça (IV) yorgundular, ama çantalarını dikkatlice (V) taşıdılar.',
 'Bu parçada numaralanmış sözcüklerden hangisi yer-yön zarfıdır?',
 [('hemen','zaman zarfı','“yöneldi” eyleminin zamanını bildirir'),('içeri','yer-yön zarfı','“girip” eyleminin yönünü bildirir'),('sessizce','durum zarfı','“dizildiler” eyleminin nasıl yapıldığını bildirir'),('Oldukça','miktar zarfı','“yorgun” sıfatının derecesini bildirir'),('dikkatlice','durum zarfı','“taşıdılar” eyleminin nasıl yapıldığını bildirir')],
 'B',lambda t:t=='yer-yön zarfı','Yer-yön zarfı olan numaralı sözcük.',
 'Eylemin hangi yöne ya da yere doğru olduğunu bildiren sözcük hangisi?',[B_ZF],
 'Yer-yön zarfı eylemin yönünü bildirir (içeri, dışarı, yukarı, ileri).','yer-yön zarfı: nereye?','Fiile “nereye?” diye sorunca cevap veren yönlü sözcük yer-yön zarfıdır.')

P('0022','K-DBST-04','zor','Aynı sözcüğün sıfat ve zarf kullanımını parçada ayırır.',4,
 'Balıkçılar sabah erken (I) kalktı. Rüzgâr hızlı (II) esiyordu; bu yüzden hızlı (III) bir tekne seçtiler. Tekne yavaş (IV) ilerledi, ağlar aşağı (V) sarkıtıldı. Kıyıdaki çocuklar onları uzaktan izledi.',
 'Bu parçada numaralanmış sözcüklerden hangisi türce ötekilerden farklıdır?',
 [('erken','zaman zarfı','“kalktı” eyleminin zamanını bildirir'),('hızlı','durum zarfı','“esiyordu” eyleminin nasıl olduğunu bildirir'),('hızlı','niteleme sıfatı','“tekne” ismini niteler'),('yavaş','durum zarfı','“ilerledi” eylemini niteler'),('aşağı','yer-yön zarfı','“sarkıtıldı” eyleminin yönünü bildirir')],
 'C',lambda t:t=='niteleme sıfatı','Türce ötekilerden farklı olan numaralı sözcük.',
 'Her sözcüğün neyi nitelediğine bak.',[B_SF,B_ZF],
 'Dört zarf, bir sıfat vardır; farklı olan isim niteleyendir.','sıfat → isim · zarf → fiil/sıfat','Aynı biçimli sözcüğün türünü, nitelediği sözcük belirler.')

C5('0023','K-DBST-04','orta','Soru zarfını soru zamiri ve sıfatından ayırır.',3,
 'Hangi cümlede soru sözcüğü, zarf görevinde kullanılmıştır?',
 [('“Niçin” erken ayrıldın?','soru zarfı','“Niçin”, “ayrıldın” fiilinin nedenini sorar; soru zarfıdır.'),
  ('“Kim” erken ayrıldı?','soru zamiri','“Kim”, kişinin yerini tutar; soru zamiridir, zarf değildir.'),
  ('“Hangi” yoldan gideceğiz?','soru sıfatı','“Hangi”, “yol” ismini belirtir; soru sıfatıdır.'),
  ('Sınıfta “kaç” öğrenci var?','soru sıfatı','“Kaç”, “öğrenci” ismini belirtir; soru sıfatıdır.'),
  ('“Ne” istersin?','soru zamiri','“Ne”, bir şeyin yerini tutar; soru zamiridir.')],
 'A',lambda t:t=='soru zarfı','Soru zarfı olan tırnaklı sözcük.',
 'Hangi soru sözcüğü fiilin nedenini ya da biçimini sorar?',[B_ZF,B_ZM],
 'Soru zarfı fiilin nasıl, niçin, ne zaman yapıldığını sorar.','soru zarfı: nasıl, niçin, ne zaman','Soru sözcüğü fiili niteliyorsa soru zarfıdır.')

# ===== K5 EDAT =====
C5('0024','K-DBST-05','kolay','Edatı diğer sözcük türlerinden ayırır.',2,
 'Aşağıdakilerden hangisinde edat tırnak içine alınmıştır?',
 [('Çocuk “hızlı” koştu.','zarf','“Hızlı”, “koştu” fiilini niteler; zarftır, edat değildir.'),
  ('Ders çalıştım, “fakat” sınavı geçemedim.','bağlaç','“Fakat”, iki cümleyi karşıtlıkla bağlar; bağlaçtır.'),
  ('“Güzel” bir şarkı dinledik.','sıfat','“Güzel”, “şarkı” ismini niteler; sıfattır.'),
  ('“Kendini” çok zorladı.','zamir','“Kendini”, ismin yerini tutan dönüşlülük zamiridir.'),
  ('Kar “gibi” beyaz bir kazak aldı.','edat','“Gibi”, “kar” sözcüğüyle birlikte benzetme bildirir; edattır.')],
 'E',lambda t:t=='edat','Edat olan tırnaklı sözcük.',
 'Hangi sözcük kendinden önceki sözcükle birlikte anlam kazanıyor?',[B_ED],
 'Edat tek başına anlamı olmayan, bir sözcükle birlikte görev yapan sözcüktür.','edat: gibi, için, göre, rağmen','Benzetme (gibi), amaç/neden (için), ölçü (göre) bildiren yardımcı sözcükler edattır.')

C5('0025','K-DBST-05','kolay','Edatları anlam ilişkilerine göre ayırır.',3,
 'Hangi cümlede tırnaklı edat, karşıtlık (ödün) anlamı katar?',
 [('Bu hediyeyi annem “için” aldım.','amaç bildiren edat','“İçin”, amaç bildirir; karşıtlık değildir.'),
  ('Hava durumuna “göre” yarın yağmur yağacak.','ölçü bildiren edat','“Göre”, ölçüt bildirir; karşıtlık değildir.'),
  ('Kar “gibi” beyaz bir örtü serildi.','benzetme bildiren edat','“Gibi”, benzetme bildirir; karşıtlık değildir.'),
  ('Yağmura “rağmen” maça gittik.','karşıtlık bildiren edat','“Rağmen”, “yağmur” engeline karşın eylemin gerçekleştiğini bildirir; karşıtlık anlamlıdır.'),
  ('Hastalığından “dolayı” derse gelemedi.','neden bildiren edat','“Dolayı”, neden bildirir; karşıtlık değildir.')],
 'D',lambda t:t=='karşıtlık bildiren edat','Karşıtlık bildiren edatın olduğu cümle.',
 'Hangi edat “engele karşın” anlamı veriyor?',[B_ED],
 '“-e rağmen”, “-e karşın” edatları engele karşın eylemin yapıldığını bildirir.','rağmen/karşın: karşıtlık · için: amaç/neden · göre: ölçü','Edatları anlam ilişkisine göre ayır.')

P('0026','K-DBST-05','orta','Parçada edatı belirler.',3,
 'Elif sepeti (I) koluna asıp bir kuş gibi (II) hafif adımlarla pazara yürüdü. Kalabalığı görünce yavaşladı, ama (III) vazgeçmedi. Sonunda aradığı kirazları (IV) buldu ve bunu (V) annesine müjdeledi.',
 'Bu parçada numaralanmış sözcüklerden hangisi edattır?',
 [('sepeti','ad','somut bir cins addır'),('gibi','edat','“kuş” sözcüğüyle birlikte benzetme bildirir'),('ama','bağlaç','iki cümleyi karşıtlıkla bağlar'),('kirazları','ad','somut bir cins addır'),('bunu','zamir','işaret zamiridir')],
 'B',lambda t:t=='edat','Edat olan numaralı sözcük.',
 'Benzetme bildiren yardımcı sözcüğü ara.',[B_ED],
 'Edat bağlandığı sözcükle birlikte anlam ilişkisi kurar.','gibi + ad → edat öbeği','Benzetme bildiren “gibi” edattır.')

C5('0027','K-DBST-05','orta','Edatı aynı cümlede başka türlerden ayırır.',3,
 'Hangi cümlede tırnaklı sözcük edat görevindedir?',
 [('Kar yağdığı “için” bütün yollar kapandı.','edat','“İçin”, “yağdığı” sözcüğüyle birlikte neden bildirir; edattır.'),
  ('Dün gece “çok” yağmur yağdı, yollar ıslandı.','belgisiz sıfat','“Çok”, “yağmur” ismini belirtir; sıfattır.'),
  ('Annem akşam yemeğine “hemen” geldi.','zaman zarfı','“Hemen”, “geldi” fiilini niteler; zarftır.'),
  ('Yarın akşam “bana” uğrar mısın, Kerem?','kişi zamiri','“Bana”, birinci kişinin yerini tutar; zamirdir.'),
  ('Masada çay “ve” kahve hazırlanmıştı herkes için.','bağlaç','“Ve”, iki ismi bağlar; bağlaçtır.')],
 'A',lambda t:t=='edat','Edat görevinde olan tırnaklı sözcük.',
 'Hangi sözcük bir sözcükle birlikte anlam ilişkisi kuruyor?',[B_ED],
 'Edat, bağlandığı sözcükle birlikte neden, amaç, benzetme gibi ilişkiler kurar; tek başına anlamı yoktur.','için/gibi/göre → edat','Sözcüğün türünü cümledeki göreviyle belirle.')

P('0028','K-DBST-05','orta','Parçada türce ötekilerden farklı sözcüğü bulur.',3,
 'Bu kitabı senin için (I) aldım. Hava durumuna göre (II) yarın (III) yağmur yağacak; yine de yağmura rağmen (IV) piknik planımızı bozmayacağız. Bahçe de evimiz gibi (V) rahat olacak.',
 'Bu parçada numaralanmış sözcüklerden hangisi türce ötekilerden farklıdır?',
 [('için','edat','“senin” sözcüğüyle birlikte amaç bildirir'),('göre','edat','“hava durumuna” sözcük öbeğiyle ölçüt bildirir'),('yarın','zaman zarfı','“yağacak” eyleminin zamanını bildirir'),('rağmen','edat','“yağmura” sözcüğüyle karşıtlık bildirir'),('gibi','edat','“evimiz” sözcüğüyle benzetme bildirir')],
 'C',lambda t:t=='zaman zarfı','Türce ötekilerden farklı olan numaralı sözcük.',
 'Her sözcüğün neye bağlandığına bak.',[B_ED,B_ZF],
 'Dört edat, bir zarf vardır; zarf fiili niteler, edat bir sözcükle birlikte görev yapar.','edat → sözcüğe bağlı · zarf → fiili niteler','Edatlar bir sözcükle birlikte, zarflar fiille ilgilidir.')

# ===== K6 BAĞLAÇ =====
C5('0029','K-DBST-06','kolay','Karşıtlık bağlacını öteki bağlaç türlerinden ayırır.',2,
 'Hangi cümlede tırnaklı bağlaç karşıtlık bildirir?',
 [('Çay “veya” kahve içebilirsiniz.','seçenek bağlacı','“Veya”, iki seçenekten birini sunar; karşıtlık bildirmez.'),
  ('Hava soğuk “ve” yağmurluydu.','ekleme bağlacı','“Ve”, iki durumu ekleyerek bağlar; karşıtlık bildirmez.'),
  ('Erken yattım, “çünkü” çok yorgundum.','neden bağlacı','“Çünkü”, neden bildirir; karşıtlık değildir.'),
  ('Çok çalıştı, “ama” kazanamadı.','karşıtlık bağlacı','“Ama”, beklenenin tersini bildirerek iki cümleyi bağlar.'),
  ('Öyle koştu “ki” nefes nefese kaldı.','sonuç bağlacı','“Ki”, sonuç bildirir; karşıtlık değildir.')],
 'D',lambda t:t=='karşıtlık bağlacı','Karşıtlık bildiren bağlacın olduğu cümle.',
 'İki yargı arasında beklenmeyen bir ters durum olan cümleyi ara.',[B_BG],
 'Karşıtlık bağlaçları: ama, fakat, lakin, ancak.','ama, fakat, lakin → karşıtlık','Bağlaçların anlam ilişkisini cümleye bakarak belirle.')

C5('0030','K-DBST-06','orta','“ile”nin bağlaç ve edat kullanımını ayırır.',3,
 '“İle” sözcüğünün bağlaç olarak kullanıldığı cümle, aşağıdakilerden hangisidir?',
 [('Sabah kuş sesi “ile” uyandık.','edat','“İle”, neden ve araç bildirir; “ve” ile değiştirilemez, edattır.'),
  ('Mektubu mavi kalem “ile” yazdı.','edat','“İle”, aracı bildirir; “ve” ile değiştirilemez, edattır.'),
  ('Misafirleri güler yüz “ile” karşıladık.','edat','“İle”, biçim bildirir; “ve” ile değiştirilemez, edattır.'),
  ('Eve uçak “ile” döndük.','edat','“İle”, aracı bildirir; “ve” ile değiştirilemez, edattır.'),
  ('Elma “ile” armut sepetin içindeydi.','bağlaç','“İle”, “elma ve armut” biçiminde “ve” yerine geçer; bağlaçtır.')],
 'E',lambda t:t=='bağlaç','“ile”nin bağlaç olduğu cümle.',
 '“İle” yerine “ve” getirince anlam bozuluyor mu?',[B_BG,B_ED],
 'Eş görevli iki sözcüğü bağlayan, yerine “ve” getirilebilen “ile” bağlaçtır; araç, birliktelik bildirirse edattır.','ile ≈ ve → bağlaç · ile = araç/birliktelik → edat','“Ve” testi: yerine ve konabiliyorsa bağlaçtır.')

P('0031','K-DBST-06','orta','Parçada bağlacı belirler.',3,
 'Kitaplığımızda roman ve (I) şiir kitapları bulunur. Bu (II) kitapları hızlı (III) okurum, bitirince (IV) sana da veririm. Kitaplar arkadaş gibi (V) vefalıdır.',
 'Bu parçada numaralanmış sözcüklerden hangisi bağlaçtır?',
 [('ve','bağlaç','“roman” ve “şiir” sözcüklerini bağlar'),('Bu','işaret sıfatı','“kitaplar” ismini belirtir'),('hızlı','durum zarfı','“okurum” fiilini niteler'),('bitirince','zarf-fiil','-ince ekiyle zaman bildiren fiilimsidir; bağlaç değildir'),('gibi','edat','“arkadaş” sözcüğüyle benzetme bildirir')],
 'A',lambda t:t=='bağlaç','Bağlaç olan numaralı sözcük.',
 'Hangi sözcük iki sözcüğü birbirine bağlıyor?',[B_BG],
 'Bağlaç eş görevli sözcükleri ya da cümleleri birbirine bağlar.','ve, ama, fakat → bağlaç','İki sözcüğü ya da cümleyi bağlayan sözcük bağlaçtır.')

C5('0032','K-DBST-06','orta','Bağlaç “ki”yi ilgi zamirinden ve -ki’li sıfattan ayırır.',3,
 'Hangi cümlede tırnaklı sözcük, iki cümleyi birbirine bağlıyor?',
 [('“Yarınki” maç ertelendi.','sıfat','“Yarınki”, “maç” ismini niteler; sıfattır.'),
  ('Öyle yoruldu “ki” uyuyakaldı.','bağlaç','“Ki”, iki cümleyi sonuç ilişkisiyle bağlar; bağlaçtır.'),
  ('Bu defter senin, “benimki” çantada.','ilgi zamiri','“Benimki”, “benim defterim” yerine geçer; zamirdir.'),
  ('“Okuldaki” kantin bugün kapalıydı.','sıfat','“Okuldaki”, “kantin” ismini niteler; sıfattır.'),
  ('Salondaki “herkes” ayağa kalktı.','belgisiz zamir','“Herkes”, belirsiz bir topluluğun yerini tutar; belgisiz zamirdir.')],
 'B',lambda t:t=='bağlaç','Bağlaç görevinde olan tırnaklı sözcük.',
 'Hangi “ki” ayrı yazılıyor ve cümleyi cümleye bağlıyor?',[B_BG],
 'Ayrı yazılan, cümleleri bağlayan “ki” bağlaçtır; sözcüğe bitişen -ki ilgi eki (sıfat ya da zamir) yapar.','ayrı “ki” → bağlaç · bitişik -ki → ek','Yazılışına ve cümledeki göreve bak.')

P('0033','K-DBST-06','zor','“ile”nin edat kullanımını bağlaçlardan ayırır.',4,
 'Elif mektubu özenle yazdı, ama (I) göndermeye çekindi. Önce zarfı kapattı ve (II) adresi mavi kalem ile (III) yazdı, çünkü (IV) mektubun yolda kaybolmasını istemiyordu. Kardeşi de (V) aynı şeyi söyledi.',
 'Bu parçada numaralanmış sözcüklerden hangisi türce ötekilerden farklıdır?',
 [('ama','bağlaç','iki cümleyi karşıtlıkla bağlar'),('ve','bağlaç','iki eylemi ekleyerek bağlar'),('ile','edat','araç bildirir; “ve” ile değiştirilemez'),('çünkü','bağlaç','iki cümleyi neden ilişkisiyle bağlar'),('de','bağlaç','“kardeşi” sözcüğünü önceki cümleye ekler')],
 'C',lambda t:t=='edat','Türce ötekilerden farklı olan numaralı sözcük.',
 'Hangi sözcük “ve” ile değiştirilirse anlam bozulur?',[B_BG,B_ED],
 'Dört bağlaç, bir edat vardır; “ile” araç bildirdiğinde edattır.','araç bildiren “ile” → edat','“İle”nin yerine “ve” getirip anlam bozulup bozulmadığına bak.')

# ===== K7 TÜRCE FARKLI =====
C5('0034','K-DBST-07','kolay','Ad görevindeki sıfatı sıfat görevlilerden ayırır.',2,
 'Tırnak içindeki sözcüklerden hangisi türce ötekilerden farklıdır?',
 [('“Güzel” bir şarkı dinledik.','sıfat','“Güzel”, “şarkı” ismini niteler; sıfattır.'),
  ('“Haftalık” plan masaya asıldı.','sıfat','“Haftalık”, “plan” ismini niteler; sıfattır.'),
  ('Sınıfa “renkli” bir resim astık.','sıfat','“Renkli”, “resim” ismini niteler; sıfattır.'),
  ('Kerem “sessiz” bir gün geçirdi.','sıfat','“Sessiz”, “gün” ismini niteler; sıfattır.'),
  ('“Güzeli” çirkinden ayırdı.','ad','“Güzeli”, sıfatın adlaşmış hâlidir; nesne olarak ad görevindedir.')],
 'E',lambda t:t=='ad','Türce ötekilerden farklı olan tırnaklı sözcük.',
 'Her cümlede tırnaklı sözcüğün neye bağlandığına bak.',[B_ADL],
 'Sıfat, ismin yerini tutarsa ad görevine geçer.','güzel + isim → sıfat · güzeli → ad','Aynı sözcüğün her cümledeki görevini ayrı ayrı belirle.')

C5('0035','K-DBST-07','kolay','“Yeni” sözcüğünün zarf kullanımını bulur.',2,
 'Hangi cümlede “yeni” sözcüğü, fiili niteleyen bir zarf olarak kullanılmıştır?',
 [('“Yeni” bir kazak aldım.','sıfat','“Yeni”, “kazak” ismini niteler; sıfattır.'),
  ('“Yenisini” beğenmedi.','ad','“Yenisini”, ismin yerini tutarak nesne olmuştur; ad görevindedir.'),
  ('Sokaktaki “yeni” bina çok yüksek.','sıfat','“Yeni”, “bina” ismini niteler; sıfattır.'),
  ('Misafirler “yeni” geldi.','zaman zarfı','“Yeni”, “geldi” fiilinin zamanını bildirir; zarftır.'),
  ('“Yeni” ayakkabılarım çok rahat.','sıfat','“Yeni”, “ayakkabılar” ismini niteler; sıfattır.')],
 'D',lambda t:t=='zaman zarfı','Zarf görevinde olan tırnaklı “yeni”.',
 '“Yeni” bir isme mi, yoksa bir fiile mi bağlı?',[B_SF,B_ZF],
 'Nitelediği sözcük isimse sıfat, fiilse zarf olur.','yeni + isim → sıfat · yeni + fiil → zarf','Aynı biçimli sözcükte türü niteleme yönü belirler.')

P('0036','K-DBST-07','kolay','Parçada türce farklı olan sözcüğü bulur.',3,
 'Bahçedeki kedi (I) yanımıza küçük (II) bir yavru (III) getirdi. Ona önce süt (IV), sonra mama (V) verdik.',
 'Bu parçada numaralanmış sözcüklerden hangisi türce ötekilerden farklıdır?',
 [('kedi','ad','somut bir cins addır'),('küçük','sıfat','“yavru” ismini niteler'),('yavru','ad','somut bir cins addır'),('süt','ad','somut bir cins addır'),('mama','ad','somut bir cins addır')],
 'B',lambda t:t=='sıfat','Türce ötekilerden farklı olan numaralı sözcük.',
 'Her sözcüğün varlık mı nitelik mi bildirdiğine bak.',[B_AD,B_SF],
 'Dört ad, bir sıfat vardır; sıfat ismi niteler.','ad: varlığı anlatır · sıfat: ismi niteler','Varlık adlandıran ad, nitelik katan sıfattır.')

P('0037','K-DBST-07','orta','Ad görevindeki renk sözcüğünü bulur.',4,
 'Kız kırmızıyı (I) en çok sevdiği için mavi (II) önlüğünü giymedi; yeşil (III) şapkasını da takmayıp sarı (IV) bir fularla gri (V) paltosunu seçti.',
 'Bu parçada numaralanmış sözcüklerden hangisi türce ötekilerden farklıdır?',
 [('kırmızıyı','ad','“sevdiği” fiilinin nesnesi olan bir renk adıdır; ad görevindedir'),('mavi','sıfat','“önlük” ismini niteler'),('yeşil','sıfat','“şapka” ismini niteler'),('sarı','sıfat','“fular” ismini niteler'),('gri','sıfat','“palto” ismini niteler')],
 'A',lambda t:t=='ad','Türce ötekilerden farklı olan numaralı sözcük.',
 'Beş renk sözcüğünden hangisinin nitelediği bir isim yok?',[B_ADL],
 'Renk sözcükleri isimle birlikte sıfat, tek başına ad görevindedir.','renk + isim → sıfat · renk (nesne) → ad','Her renk sözcüğünün yanında nitelediği isim olup olmadığına bak.')

C5('0038','K-DBST-07','zor','Aynı sözcüğün zarf ve sıfat kullanımını ayırır.',4,
 'Hangisinde “aşağı” sözcüğü, öteki dört cümledekinden ayrı bir türde karşımıza çıkar?',
 [('Kedi “aşağı” baktı.','yer-yön zarfı','“Aşağı”, “baktı” fiilinin yönünü bildirir; zarftır.'),
  ('Top merdivenlerden “aşağı” yuvarlandı.','yer-yön zarfı','“Aşağı”, “yuvarlandı” fiilinin yönünü bildirir; zarftır.'),
  ('“Aşağı” mahallede oturuyoruz.','sıfat','“Aşağı”, “mahalle” ismini niteler; sıfattır.'),
  ('Çantayı “aşağı” bıraktı.','yer-yön zarfı','“Aşağı”, “bıraktı” fiilinin yönünü bildirir; zarftır.'),
  ('Asansörle “aşağı” indik.','yer-yön zarfı','“Aşağı”, “indik” fiilinin yönünü bildirir; zarftır.')],
 'C',lambda t:t=='sıfat','Türce ötekilerden farklı olan tırnaklı sözcük.',
 '“Aşağı” sözcüğünün bağlandığı sözcüğe bak.',[B_SF,B_ZF],
 'Aynı sözcük isim niteliyorsa sıfat, fiil niteliyorsa zarftır.','aşağı + isim → sıfat · aşağı + fiil → zarf','Önce sözcüğün neyi nitelediğini bul.')

# ===== K8 ORTAK ÖZELLİK =====
C5('0039','K-DBST-08','orta','İki tırnaklı sözcüğün edat–bağlaç sırasını belirler.',3,
 'Tırnaklı sözcüklerin sırasıyla edat ve bağlaç olduğu cümle hangisidir?',
 [('“Ama” senin “gibi” düşünemem.',('bağlaç','edat'),'“Ama” bağlaç, “gibi” edattır; sıra ters.'),
  ('Senin “için” yağmura “rağmen” geldi.',('edat','edat'),'“İçin” de “rağmen” de edattır; ikinci sözcük bağlaç değildir.'),
  ('Çay “veya” kahve ister misin, “yoksa” su mu?',('bağlaç','bağlaç'),'“Veya” da “yoksa” da bağlaçtır; ilk sözcük edat değildir.'),
  ('Bu senin “için” alındı, “ama” beğenmedin.',('edat','bağlaç'),'“İçin”, “senin” ile görev yapan edattır; “ama”, cümleleri bağlayan bağlaçtır.'),
  ('“Bu” hediye “için” teşekkürler.',('sıfat','edat'),'“Bu” sıfattır; ilk sözcük edat değildir.')],
 'D',lambda t:t==('edat','bağlaç'),'İlki edat, ikincisi bağlaç olan cümle.',
 'Önce bir sözcüğe bağlı olan, sonra cümleyi bağlayan sözcüğü ara.',[B_ED,B_BG],
 'Aranan sıra: önce edat, sonra bağlaç.','edat → sözcüğe bağlı · bağlaç → cümleyi bağlar','Her iki sözcüğü ayrı çöz ve sıraya dikkat et.')

C5('0040','K-DBST-08','zor','İki tırnaklı sözcüğün zamir–zarf sırasını “çok” tuzağıyla belirler.',4,
 'Hangi cümlede önce bir zamir, sonra bir zarf tırnak içine alınmıştır?',
 [('Elif “dün” “çok” yoruldu.',('zarf','zarf'),'“Dün” ve “çok” fiili niteler; ikisi de zarftır.'),
  ('“Çok” insan “çok” yoruldu.',('sıfat','zarf'),'İlk “çok”, “insan” ismini belirtir (sıfat); ilk sözcük zamir değildir.'),
  ('“Hepsi” “çok” kitap okudu.',('zamir','sıfat'),'“Çok”, “kitap” ismini belirtir; ikinci sözcük sıfattır, zarf değildir.'),
  ('“Şimdi” “kimse” gelmedi.',('zarf','zamir'),'“Şimdi” zarf, “kimse” zamirdir; sıra ters.'),
  ('“Kimse” “çok” yorulmadı.',('zamir','zarf'),'“Kimse”, belirsiz bir kişinin yerini tutar (zamir); “çok”, “yorulmadı” fiilini niteler (zarf).')],
 'E',lambda t:t==('zamir','zarf'),'İlki zamir, ikincisi zarf olan cümle.',
 'Önce ismin yerini tutan, sonra fiili niteleyen sözcüğü ara.',[B_ZM,B_ZF],
 'Aranan sıra: önce zamir, sonra zarf.','zamir → isim yerine · zarf → fiil niteler','Çiftlerde her sözcüğü ayrı çöz, sonra sıraya bak.')

soru(Q,'0041','K-DBST-08','zor','Parçada türce aynı olan iki sözcüğü belirler.',4,
 'Ben (I) bu şehirde uzun (II) yıllar yaşadım. Sana yolu tarif edeyim: önce hızlı (III) yürü, sonra köprüden geç; karşıdaki (IV) çınarı (V) görünce sola dön.\nBu parçada numaralanmış sözcüklerden hangi ikisi türce aynıdır?',
 [('II ve IV',D,'','bilgi'),
  ('I ve II',Y,'“Ben” zamir, “uzun” sıfattır; türleri farklıdır.','dikkat'),
  ('III ve IV',Y,'“Hızlı” zarf, “karşıdaki” sıfattır; türleri farklıdır.','bilgi'),
  ('I ve V',Y,'“Ben” zamir, “çınarı” ad soylu bir sözcüktür; türleri farklıdır.','dikkat'),
  ('IV ve V',Y,'“Karşıdaki” sıfat, “çınarı” addır; türleri farklıdır.','bilgi')],
 'A',lambda e:e==D,'Türce aynı olan iki numaralı sözcük.',
 'Beş sözcüğün türünü yan yana yazıp aynı olanı ara.',[B_ZM,B_SF],
 [AD('Ölçütü hatırla','Zamir ismin yerini tutar; sıfat ismi niteler; zarf fiili niteler; ad varlığı adlandırır.','zamir · sıfat · zarf · ad'),
  AD('Numaraları çözümle','“Ben” kişi zamiri; “uzun” “yıllar” ismini niteler; “hızlı” “yürü” fiilini niteler; “karşıdaki” “çınar” ismini niteler; “çınarı” ağaç adıdır.','I: zamir · II: sıfat · III: zarf · IV: sıfat · V: ad'),
  AD('Aynı türdekileri seç','Yalnız II ve IV aynı türdedir; ikisi de ismi niteleyen sıfattır.','A: II ve IV ✓')],
 'Önce her numaranın türünü yaz, sonra şıklardaki çiftleri karşılaştır.',kalip='öncüllü')
if HATALAR:
    for h in HATALAR: print('SORUN',h)
    sys.exit(1)
bitir(Q)
print('tamam')
