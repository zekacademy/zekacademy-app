"""TYT Türkçe · Noktalama İşaretleri (genişletme, 1. yarı): virgül, noktalı virgül, iki nokta, boşluk sırası. 25 soru (hafif mod). Metinler özgündür."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from hafif_db import *
KY='ÖSYM TYT Türkçe 2018–2026 · Bilgi Sarmal Dil Bilgisi SB (ÖSYM Tipi) · TDK Yazım Kılavuzu'
KARTLAR={
 'K-DBNK-01':dict(alt='Virgül: Eş Görevli Sözcükler',fikir='Sıralı sözcük, öbek ve sıfatlar arasına virgül konduğunu; “ve” öncesine, ad ile sıfat arasına, ögeler arasına gereksiz virgül konmadığını uygulamak.',tuzak='“ve”den önce virgül koymak; son sıfatla ad arasına virgül koymak; özne–nesne–yüklem arasına virgül koymak.',zorluk='orta',kalip='öncüllü',adim=3,tipId='dnk-virgul-es',kaynak=KY),
 'K-DBNK-02':dict(alt='Virgül: Hitap, Evet/Hayır ve Ara Söz',fikir='Cümle başındaki hitap ve cevap sözcüklerinden sonra, ara sözün iki yanında virgül kullanıldığını bilmek.',tuzak='Ara sözün yalnız bir yanına virgül koymak; özneyi hitap sanmak; özneden sonra gereksiz virgül koymak.',zorluk='orta',kalip='öncüllü',adim=3,tipId='dnk-virgul-hitap',kaynak=KY),
 'K-DBNK-03':dict(alt='Virgül: Sıralı Cümleler ve Ortak Yüklem',fikir='Sıralı cümleleri ve yüklemi ortak cümleleri ayıran virgülü yerinde kullanmak.',tuzak='Zarf-fiil öbeğinin sonuna virgül koymak; yüklemi ortak cümlelerde virgülü atlamak ya da yanlış yere koymak.',zorluk='zor',kalip='öncüllü',adim=4,tipId='dnk-virgul-cumle',kaynak=KY),
 'K-DBNK-04':dict(alt='Noktalı Virgül: Ögeleri Virgüllü Cümleler',fikir='Noktalı virgülün içinde virgül bulunan sıralı cümleleri ve öbekleri birbirinden ayırdığını bilmek.',tuzak='Noktalı virgülü sıralı sözcükler, hitap ya da özne–yüklem arasında kullanmak.',zorluk='zor',kalip='öncüllü',adim=4,tipId='dnk-noktalivirgul',kaynak=KY),
 'K-DBNK-05':dict(alt='İki Nokta: Açıklama, Örnek ve Alıntı Öncesi',fikir='İki noktanın tamamlanmış bir cümlenin sonunda, açıklama, örnek, sıralama ya da alıntıdan önce konduğunu bilmek.',tuzak='İki noktayı yüklem gelmeden, cümlenin ortasında kullanmak.',zorluk='orta',kalip='öncüllü',adim=3,tipId='dnk-ikinokta',kaynak=KY),
 'K-DBNK-06':dict(alt='Boşluk Sırası: Karışık İşaret Dizileri',fikir='Aynı cümledeki birden çok boşluğa virgül, noktalı virgül, iki nokta ve nokta kurallarını birlikte uygulamak.',tuzak='Dizinin tek bir yerindeki yanlışı gözden kaçırmak; her boşluğa tanıdık işareti koymak.',zorluk='zor',kalip='düz',adim=4,tipId='dnk-bosluk',kaynak=KY),
}
TIPLER={'dnk-virgul-es':'Virgül: eş görevli sözcükler','dnk-virgul-hitap':'Virgül: hitap, evet/hayır, ara söz','dnk-virgul-cumle':'Virgül: sıralı cümle, ortak yüklem','dnk-noktalivirgul':'Noktalı virgül','dnk-ikinokta':'İki nokta','dnk-bosluk':'Boşluk sırası'}
Q=kur('dnokta','Noktalama İşaretleri','tr|Noktalama İşaretleri',KARTLAR,TIPLER); Q.n=25
RM=['I','II','III','IV','V']
def dq(no,kart,zor,kaz,adim,kok,sek,ara,harf,kural,istenen,ip,bilgi,puf,kalip='düz'):
    """sek: 5 × (metin, noktalama_doğru_mu, açıklama[, tür]); ara: 'dogru' ya da 'yanlis' (sorulan şık)."""
    opts=[]
    for t,ok,r,*tu in sek: opts.append((t,D if ok else Y,r,(tu[0] if tu else 'bilgi')))
    hedef=D if ara=='dogru' else Y
    ans=[i for i,o in enumerate(opts) if o[1]==hedef]; assert len(ans)==1,(no,'tek cevap')
    i=ans[0]
    islem=' · '.join(f"{'ABCDE'[k]}: {'doğru' if o[1]==D else 'yanlış'}" for k,o in enumerate(opts))
    adimlar=[A('Kuralı hatırla',kural[0],kural[1]),A('Şıkları tek tek sına','Her şıktaki noktalamayı kurala göre değerlendir.',islem),A('Sonucu belirle',opts[i][2],f"{'ABCDE'[i]}: {'doğru' if ara=='dogru' else 'yanlış'}")]
    soru(Q,no,kart,zor,kaz,adim,kok,opts,harf,(lambda e,h=hedef:e==h),istenen,ip,bilgi,adimlar,puf,kalip=kalip)
def pq(no,kart,zor,kaz,adim,parca,isaret,harf,neden,kural,istenen,ip,bilgi,puf):
    """Numaralı parça: parça içindeki (I)…(V); neden: 5 numara için kısa gerekçe; harf: doğru numaranın şık harfi."""
    idx='ABCDE'.index(harf); assert len(neden)==5
    for k in range(5): assert f'({RM[k]})' in parca,(no,RM[k])
    kok=f'Bu parçada numaralanmış yerlerden hangisine {isaret} getirilmelidir?'
    opts=[(RM[k],D if k==idx else Y,neden[k],'dikkat' if k%2 else 'bilgi') for k in range(5)]
    islem=' · '.join(f"{RM[k]}: {'✓' if k==idx else '✗'}" for k in range(5))
    adimlar=[A('Kuralı hatırla',kural[0],kural[1]),A('Numaraları tek tek sına','Her numaralı yerde işaretin gerekip gerekmediğini kurala göre değerlendir.',islem),A('Sonucu belirle',neden[idx],f'{RM[idx]}: gerekli')]
    soru(Q,no,kart,zor,kaz,adim,parca+'\n'+kok,opts,harf,(lambda e:e==D),istenen,ip,bilgi,adimlar,puf,kalip='öncüllü')
B_ES=B('Eş görevli sözcükler','sıralı sözcük ve öbekler virgülle ayrılır; son iki öge arasında “ve” varsa virgül konmaz · “çam, ladin ve kayın”')
B_SIF=B('Sıfatlar arasında virgül','aynı adı niteleyen eş görevli sıfatlar virgülle ayrılır; son sıfatla ad arasına virgül konmaz · “uzun, ince bir yol”')
B_HIT=B('Hitap ve cevap sözcüğü','cümle başındaki hitap ile evet/hayır sözcüklerinden sonra virgül konur · “Sevgili Defne, hoş geldin.” “Hayır, gelmedim.”')
B_ARA=B('Ara söz','cümle içinde araya giren söz iki yanından virgülle ayrılır · “Kerem, bence, haklıydı.”')
B_SIRALI=B('Sıralı cümleler','birbirine bağlı sıralı cümleler virgülle ayrılır; ortak ögeler tekrarlanmaz · “Yağmur dindi, güneş çıktı.”')
B_UZUN=B('Uzun özne','özne uzunsa ya da yüklemle karışabilecekse özneden sonra virgül konur')
B_ORTAK=B('Yüklemi aynı cümleler','yüklemi ortak olan cümlelerde yüklem sonda tek kez söylenir, ondan önceki cümleler virgülle ayrılır · “Ali elmayı, Veli armudu yedi.”')
B_GER=B('Gereksiz virgül','özne, nesne, tümleç ve yüklem arasına; “ve”den önce; sıfatla ad arasına virgül konmaz')
B_NV=B('Noktalı virgül','içinde virgül bulunan sıralı cümleleri ya da öbekleri birbirinden ayırır · “Annem pazara gitti, sebze aldı; babam yemeği hazırladı.”')
B_IKI=B('İki nokta','tamamlanmış cümleden sonra açıklama, örnek, sıralama ya da alıntı gelecekse konur · “Şunu söyledi: Yarın gelirim.”')

# ---- Kart 01: eş görevli sözcükler ----
dq('0001','K-DBNK-01','kolay','Eş görevli sözcükler arasındaki virgülün gereksiz kullanıldığı cümleyi belirler.',2,
 'Hangisinde olmaması gereken bir yere virgül (,) konmuştur?',
 [('Sepete elma, armut ve incir koyduk.',True,'Sıralı adlar virgülle ayrılmış, “ve”den önce virgül yok; doğrudur.'),
  ('Sınıfta Elif, Kerem ve Defne ödevlerini bitirdi.',True,'Eş görevli özneler virgülle ayrılmış; doğrudur.','dikkat'),
  ('Kırmızı, mavi ve sarı boyalarla resim yaptık.',True,'Eş görevli sıfatlar virgülle ayrılmış; doğrudur.'),
  ('Dün akşam yağmurlu, soğuk, bir havada yürüdük.',False,'“Soğuk”tan sonraki virgül, son sıfatla “bir” ve ad arasına konmuştur; gereksizdir.'),
  ('Bahçede gül, lale ve sümbül açmıştı.',True,'Sıralı özneler virgülle ayrılmış; doğrudur.','dikkat')],
 'yanlis','D',('Eş görevli ögeler virgülle ayrılır; son öge ile ad ya da “ve” arasına virgül konmaz.','sıralı öge: , · son öge: ,’sız'),
 'Virgülün gereksiz kullanıldığı cümle.','Her virgülün iki yanındaki sözcükler birbirine eş görevli mi, yoksa tek bir öbeğin parçası mı?',[B_ES,B_GER],
 'Virgül eş görevli ögeleri ayırır; öbeğin içindeki son sıfat ile ad arasına virgül girmez.')

pq('0002','K-DBNK-01','orta','Sıralı adlar arasında virgül gereken yeri parçada bulur.',3,
 'Mutfağın raflarında (I) un (II) şeker ve tuz kavanozları sıralanmıştı. Annem (III) her sabah taze ekmek (IV) alıp kahvaltıyı hazırlardı. Biz de (V) sofraya oturmadan önce ellerimizi yıkardık.',
 'virgül (,)','B',
 ['Yer tümleci ile sıralama başlamadan önce virgül gerekmez; bu yerde virgül yoktur.','“un, şeker ve tuz”: eş görevli adlardan ilkinden sonra virgül gerekir.','Özne ile zarf tümleci arasında; özne kısa olduğundan virgül gerekmez.','Nesne ile zarf-fiil arasında virgül konmaz.','“de” bağlacından sonra virgül konmaz.'],
 ('Sıralanan eş görevli adlar virgülle ayrılır; son iki ad arasında “ve” varsa virgül konmaz.','un, şeker ve tuz'),
 'Virgül getirilmesi gereken yer.','Parçada üç şeyin art arda sıralandığı bir yer var; onu bul.',[B_ES],
 'Birden fazla eş görevli ad art arda sıralanıyorsa “ve”den önceki adlar virgülle ayrılır.')

dq('0003','K-DBNK-01','orta','Virgülün yerinde kullanıldığı tek cümleyi belirler.',3,
 'Aşağıdakilerden hangisi virgül (,) bakımından doğru yazılmıştır?',
 [('Pazardan domates, biber ve soğan aldık.',True,'Sıralı adlar virgülle ayrılmış, “ve”den önce virgül yok; doğrudur.'),
  ('Bu yaz Ayşe, ve Mert sahilde garsonluk yapacak.',False,'“ve” bağlacından önce virgül konmaz.'),
  ('Teyzem bize, bahçesinden taze incir getirdi.',False,'Cümlenin ögeleri (tümleç ile nesne) arasına virgül konmaz.','dikkat'),
  ('Dolabın önünde kırmızı, bir kazak duruyordu.',False,'Sıfat ile ad arasına virgül konmaz.'),
  ('Mert ile, Kerem bahçede top oynuyor.',False,'“ile” bağlacından sonra virgül konmaz; iki özne “ile” ile bağlanmıştır.','dikkat')],
 'dogru','A',('Virgül yalnız eş görevli ögeleri ayırır; “ve”, “ile”nin iki yanına virgül konmaz.','ve/ile: virgülsüz'),
 'Virgülün yerinde kullanıldığı cümle.','Virgülün iki yanındaki sözcüklere tek tek bak: eş görevli mi?',[B_ES,B_GER],
 '“ve” ve “ile” bağlayıcıdır; yanına virgül gelmez, virgül sıralamayı yapar.')

pq('0004','K-DBNK-01','orta','Eş görevli sıfatlar arasına virgül gereken yeri, öbek içindeki öteki yerlerden ayırır.',3,
 'Atölyemizin duvarlarında eski haritalar (I) ve fotoğraflar asılıdır. Masaların üzerindeki (II) boyalar (III) her sabah yeniden düzenlenir. Köşedeki (IV) rafta yaşlı (V) bilge bir ressamın kitapları durur.',
 'virgül (,)','E',
 ['“ve” bağlacından önce virgül konmaz.','Sıfat-fiil öbeği ile ad arasına virgül konmaz.','Özne ile zarf tümleci arasında; özne kısa olduğundan virgül gerekmez.','Sıfat ile ad arasına virgül konmaz.','“yaşlı” ve “bilge”: ressamı niteleyen iki eş görevli sıfat; aralarına virgül konur.'],
 ('Aynı adı niteleyen eş görevli sıfatlar virgülle ayrılır; son sıfat ile ad arasına virgül konmaz.','yaşlı, bilge bir ressam'),
 'Virgül getirilmesi gereken yer.','Hangi iki sözcük aynı adı niteliyor ve sırayla sayılabilir?',[B_SIF,B_GER],
 'Bir adı art arda iki sıfat nitelerken, sıfatlardan ilki virgülle ayrılır.')

# ---- Kart 02: hitap, evet/hayır, ara söz ----
dq('0005','K-DBNK-02','kolay','Cümle başındaki cevap ve hitap sözcüklerinden sonra virgülün yerinde olduğu cümleyi bulur.',2,
 'Hangi cümlede virgül (,) kuralına uyulmuştur?',
 [('Evet bu işi ben yaptım.',False,'“Evet” cevap sözcüğünden sonra virgül konmalıdır; burada yoktur.'),
  ('Sevgili Ayşe yarın seni bekliyorum.',False,'“Sevgili Ayşe” hitaptır; sonrasına virgül konmalıdır, burada yoktur.','dikkat'),
  ('Hayır, bu kitabı ben almadım.',True,'Cevap sözcüğünden sonra virgül konmuş; doğrudur.'),
  ('Annem, sofrayı kurdu.',False,'Özne ile nesne arasında virgül konmaz; “annem” burada hitap değil öznedir.'),
  ('Öğrenciler sınıfa, girdi.',False,'Yer tümleci ile yüklem arasında virgül konmaz.')],
 'dogru','C',('Cümle başındaki evet, hayır ve hitap sözcüklerinden sonra virgül konur.','Evet, … · Sevgili Ayşe, …'),
 'Virgülün yerinde kullanıldığı cümle.','Cümlenin başındaki sözcük bir cevap ya da seslenme mi?',[B_HIT],
 'Cümleye “Evet”, “Hayır” ya da bir seslenmeyle başlıyorsan hemen ardına virgül koy.')

pq('0006','K-DBNK-02','orta','Hitap sözcüğünden sonra virgül gereken yeri parçada belirler.',3,
 'Okul gazetemizin yeni sayısı çıktı. Genç yazarlarımız (I) bu sayı için aylarca emek verdi. Gezi yazıları ve röportajlar (II) sayfaları dolduruyor. Hazırlık sürecinde öğretmenlerimiz (III) bize destek oldu. Sevgili okurlar (IV) sizden gelecek yorumları sabırsızlıkla bekliyoruz. Gazetemizi (V) arkadaşlarınıza da önerin.',
 'virgül (,)','D',
 ['“Genç yazarlarımız” üçüncü kişi öznedir, yüklem de “verdi”dir; hitap değildir, virgül gerekmez.','Özne ile nesne arasında virgül konmaz.','Özne ile dolaylı tümleç arasında virgül gerekmez.','“Sevgili okurlar” seslenme sözüdür (hitap); sonrasına virgül konur.','Nesne ile tümleç arasında virgül konmaz.'],
 ('Cümle başında seslenme için kullanılan hitap sözcüğünden sonra virgül konur.','Sevgili okurlar, …'),
 'Virgül getirilmesi gereken yer.','Hangi cümlede okurlara doğrudan seslenilmiş?',[B_HIT],
 'Seslenilen kişi cümlenin öznesi değilse ve ikinci kişiye yönelik konuşma varsa hitaptır; virgül ister.')

dq('0007','K-DBNK-02','orta','Ara sözün virgülle yanlış ayrıldığı cümleyi belirler.',3,
 'Aşağıdaki cümlelerin hangisinde virgül (,) yanlış kullanılmıştır?',
 [('Kitabı, sanırım, dün akşam masanın üstüne bırakmışım.',True,'Ara söz iki yanından virgülle ayrılmış; doğrudur.'),
  ('Komşumuz Ahmet Bey, emekli öğretmen yarın bize gelecek.',False,'“emekli öğretmen” ara sözdür; yalnız başına virgül konmuş, ikinci virgül eksiktir.'),
  ('Elif, benim en yakın arkadaşım, bu yıl İzmir’e taşındı.',True,'Açıklayıcı ara söz iki yanından virgülle ayrılmış; doğrudur.','dikkat'),
  ('Bu proje, bence, listede ilk sırada yer almalı.',True,'“bence” ara sözü iki yanından virgülle ayrılmış; doğrudur.'),
  ('Toplantıya, bildiğim kadarıyla, herkes katılacak.',True,'Ara söz iki yanından virgülle ayrılmış; doğrudur.','dikkat')],
 'yanlis','B',('Ara söz hem başından hem sonundan virgülle ayrılır; tek tarafına virgül konmaz.',', ara söz ,'),
 'Virgül kullanımı yanlış olan cümle.','Virgülle ayrılan söz atılınca cümlenin anlamı bozulmuyor mu? Virgüller çift mi?',[B_ARA],
 'Ara söz iki virgül arasında yaşar; virgülleri say, çift değilse yanlış vardır.')

pq('0008','K-DBNK-02','zor','Açılış virgülü konmuş ara sözün kapanışına gelmesi gereken virgülü bulur.',4,
 'Okul takımının yeni kaptanı, herhâlde (I) bu yıl da Kerem olacak. Takımın (II) en genç oyuncusu da (III) Mert olacak. Antrenörler bu kararı (IV) toplantıda herkese (V) duyuracak.',
 'virgül (,)','A',
 ['“herhâlde” ara sözdür; “kaptanı,” ile açılan virgülün kapanışı burada gerekir.','Tamlayan ile tamlanan arasına virgül konmaz.','“da” bağlacından sonra virgül konmaz; özne ile yüklem arasında ayrıca virgül gerekmez.','Nesne ile zarf tümleci arasında virgül konmaz.','Dolaylı tümleç ile yüklem arasında virgül konmaz.'],
 ('Ara söz iki yanından virgülle ayrılır; açılış virgülü konduysa kapanış virgülü de gelmelidir.','kaptanı, herhâlde, bu yıl'),
 'Virgül getirilmesi gereken yer.','Parçada tek bir virgül var; onun eşini nereye koymak gerekir?',[B_ARA],
 'Cümle içinde tek başına kalmış bir virgül, kapanmamış bir ara sözün işaretidir.')

# ---- Kart 03: sıralı cümleler, uzun özne, ortak yüklem ----
dq('0009','K-DBNK-03','orta','Sıralı cümleler içinde gereksiz virgülü bulur.',3,
 'Aşağıdaki cümlelerin hangisinde virgül (,) gereksiz kullanılmıştır?',
 [('Yağmur dindi, bulutlar dağıldı, güneş yeniden göründü.',True,'Sıralı cümleler virgülle ayrılmış; doğrudur.'),
  ('Çocuklar bahçeye koştu, annem yemeği hazırladı.',True,'Sıralı iki cümle virgülle ayrılmış; doğrudur.','dikkat'),
  ('Sınav bitti, öğrenciler sınıftan çıktı.',True,'Sıralı cümleler virgülle ayrılmış; doğrudur.'),
  ('Rüzgâr sertleşti, dalgalar yükseldi, tekneler limana döndü.',True,'Sıralı üç cümle virgülle ayrılmış; doğrudur.','dikkat'),
  ('Ali sınıfa, girdi, defterini çıkardı.',False,'“sınıfa” ile “girdi” arasındaki virgül, tümleç ile yüklem arasına konmuştur; gereksizdir.')],
 'yanlis','E',('Sıralı cümleler virgülle ayrılır; bir cümlenin kendi ögeleri arasına virgül konmaz.','cümle, cümle, cümle'),
 'Virgülün gereksiz kullanıldığı cümle.','Her virgül iki ayrı cümleyi mi ayırıyor, yoksa tek cümlenin ögelerini mi?',[B_SIRALI,B_GER],
 'Bir cümlenin kendi ögeleri (özne, nesne, tümleç) ile yüklemi arasına virgül konmaz.')

pq('0010','K-DBNK-03','orta','Sıralı cümleler arasında eksik virgülü bulur.',3,
 'Gün batarken sahil canlandı. Balıkçılar (I) ağlarını topladı, çocuklar (II) kumdan kaleler yaptı (III) yaşlılar bankalara oturup (IV) denizi izledi. Hava serinlerken kalabalık (V) dağılmaya başladı.',
 'virgül (,)','C',
 ['Özne ile nesne arasında virgül konmaz.','Özne ile nesne arasında virgül konmaz.','Sıralı cümleler virgülle ayrılır; “…topladı, …yaptı,” ile aynı sıra sürmektedir.','Zarf-fiil öbeği ile nesne arasında virgül konmaz.','Özne ile yüklem arasında virgül konmaz.'],
 ('Art arda sıralanan yüklemli cümleler virgülle ayrılır.','cümle, cümle, cümle'),
 'Virgül getirilmesi gereken yer.','Parçada art arda dizilen üç cümleden hangisinin sonunda ayraç eksik?',[B_SIRALI],
 'Aynı kalıpta sıralanan cümlelerden birinin sonunda virgül eksikse sıra bozulmuştur; ayırıcıyı tamamla.')

pq('0011','K-DBNK-03','orta','Yüklemi ortak cümlelerde birinci cümlenin sonuna gelmesi gereken virgülü bulur.',3,
 'Hafta sonu bahçe (I) işleri paylaşıldı. Elif ağaçları (II) Kerem çiçekleri sulayacak. Annem bu çalışmayı (III) uzaktan izleyecek. Akşam hep birlikte (IV) bahçede çay içeceğiz. Gün batınca herkes (V) dinlenecek.',
 'virgül (,)','B',
 ['Tamlayan ile tamlanan arasına virgül konmaz.','“Elif ağaçları” ile “Kerem çiçekleri” yüklemi ortak (sulayacak) iki cümledir; birincinin sonuna virgül konur.','Nesne ile zarf tümleci arasında virgül konmaz.','Zarf tümleci ile yer tümleci arasında virgül konmaz.','Özne ile yüklem arasında virgül konmaz.'],
 ('Yüklemi ortak olan cümleler, yüklem sonda tek kez söylenerek virgülle ayrılır.','Elif ağaçları, Kerem çiçekleri sulayacak.'),
 'Virgül getirilmesi gereken yer.','Hangi cümlede iki kişi iş paylaşıyor ve yüklem yalnız bir kez söyleniyor?',[B_ORTAK],
 'Yüklem bir kez söylenip iki ayrı iş sayılıyorsa, ilk işin bittiği yerde virgül durur.')

dq('0012','K-DBNK-03','zor','Yüklemi aynı olan cümlelerde virgülün yerinde kullanıldığı cümleyi belirler.',4,
 'Aşağıdaki cümlelerden hangisinin virgül kullanımı kurallara uygundur?',
 [('Kerem tarihi Elif coğrafyayı Defne matematiği çok sevdi.',False,'Yüklemi ortak olan cümleler virgülle ayrılmalıdır; hiç virgül yoktur.'),
  ('Annem pazardan, babam marketten kardeşim fırından ekmek aldı.',False,'“babam marketten”den sonra virgül eksiktir; ortak yüklemli cümleler hepsi virgülle ayrılır.','dikkat'),
  ('Kerem kırmızıyı, Ali maviyi Zeynep, sarıyı seçti.',False,'Virgül kişi adından sonraya kaymış; ortak yüklemli cümleler “kırmızıyı,” “maviyi,” biçiminde ayrılmalıdır.'),
  ('Dedem bahçeye, ninem mutfağa, çocuklar odaya çekildi.',True,'Yüklemi ortak cümleler virgülle ayrılmış, yüklem sonda; doğrudur.'),
  ('Babam çayı demledi annem, kahvaltıyı hazırladı.',False,'Virgül, ikinci cümlenin öznesi ile nesnesi arasına konmuş; cümleleri ayıran virgül “demledi”den sonra gelmeliydi.','dikkat')],
 'dogru','D',('Yüklemi ortak olan cümleler, yüklem sonda tek kez söylenerek virgülle ayrılır.','ögeler, ögeler, yüklem'),
 'Virgülün yerinde kullanıldığı cümle.','Yüklem yalnız sonda söylenmiş; her cümlenin kendi bölümü virgülle nerede bitmeli?',[B_ORTAK],
 'Ortak yüklemli cümlelerde virgül, her cümlenin son ögesinden sonra gelir.')

# ---- Kart 04: noktalı virgül ----
dq('0013','K-DBNK-04','kolay','Noktalı virgülün yerinde kullanıldığı cümleyi belirler.',2,
 'Aşağıdaki cümlelerin hangisinde noktalı virgül (;) yerinde kullanılmıştır?',
 [('Kerem sabah erkenden kalkıp koştu, duş aldı; Elif ise kahvaltıyı hazırlayıp çayı demledi.',True,'Ögeleri virgülle ayrılmış sıralı cümleler noktalı virgülle ayrılmış; doğrudur.'),
  ('Evimizin bahçesinde bu bahar kırmızı gül; mor lale ve sarı sümbül açmıştı.',False,'Sıralı adlar virgülle ayrılır; noktalı virgül yerinde değildir.'),
  ('Sevgili dostlarım; sizi yarın akşam bizimle yemek yemeye bekliyoruz.',False,'Hitap sözcüğünden sonra virgül konur; noktalı virgül yanlıştır.','dikkat'),
  ('Yarın sabah; okula her zamankinden çok daha erken gitmeyi düşünüyorum.',False,'Zaman zarfı ile cümlenin devamı arasında noktalı virgül konmaz.'),
  ('Geçen hafta okuduğumuz roman; hepimizi çok etkileyen sürükleyici bir kitaptı.',False,'Özne ile yüklem arasına noktalı virgül konmaz.','dikkat')],
 'dogru','A',('Noktalı virgül, içinde virgül bulunan sıralı cümleleri birbirinden ayırır.','…duş aldı ; Elif ise …'),
 'Noktalı virgülün yerinde kullanıldığı cümle.','Noktalı virgülün iki yanında da yüklemli birer cümle var mı?',[B_NV],
 'Noktalı virgülün iki yanında da kendi başına birer cümle ararsın.')

pq('0014','K-DBNK-04','orta','İki ayrı cümleyi, ögeleri virgüllü olduğunda ayıran noktalı virgülün yerini bulur.',3,
 'Okulumuzun kütüphanesi (I) iki bölümden oluşur. Girişte görevli (II) öğretmen kayıt defterini (III) tutar. Öğrenciler (IV) aradıkları kitabı bulmakta zorlanmaz. Birinci rafta romanlar, öyküler ve şiir kitapları (V) ikinci rafta sözlükler, ansiklopediler ve atlaslar bulunur.',
 'noktalı virgül (;)','E',
 ['Özne ile tümleç arasında hiçbir işaret gerekmez.','Sıfat ile ad arasına işaret konmaz.','Nesne ile yüklem arasına işaret konmaz.','Özne ile nesne arasına işaret konmaz.','İki cümlenin ögeleri de virgülle ayrılmıştır; bu yüzden cümleler birbirinden noktalı virgülle ayrılır.'],
 ('Ögeleri virgülle ayrılmış sıralı cümleler noktalı virgülle ayrılır.','…kitapları ; …atlaslar bulunur'),
 'Noktalı virgül getirilmesi gereken yer.','Hangi yerde iki yan da kendi içinde virgülle sıralanmış?',[B_NV],
 'İki yanı da virgüllü cümleleri yalnız virgülle ayırırsan okur sınırı kaybeder; sınıra noktalı virgül koy.')

dq('0015','K-DBNK-04','zor','Ögeleri virgüllü öbekleri ayıran noktalı virgülün yerinde olduğu cümleyi belirler.',4,
 'Aşağıdakilerden hangisinde noktalı virgül (;) doğru kullanılmıştır?',
 [('Pazardan elma, armut; portakal, muz ve kayısı alıp eve döndük.',False,'Sıralı adlar arasında virgül kullanılır; noktalı virgül yerinde değildir.'),
  ('Dünkü toplantıya sınıfımızdan Elif; Kerem ve Ayşe de katıldı.',False,'Eş görevli özneler virgülle ayrılır; noktalı virgül yanlıştır.','dikkat'),
  ('Elif Hanım, öğretmen; Kerem Bey, müdür; Defne Hanım, hemşire geldi.',True,'Kendi içinde virgül bulunan öbekler noktalı virgülle ayrılmış; doğrudur.'),
  ('Geçen hafta birlikte okuduğumuz romanın sonu; bizi çok şaşırttı.',False,'Özne ile yüklem arasına noktalı virgül konmaz.'),
  ('Sevgili anneanne; sana bu mektubu bütün sevgimle yazıyorum.',False,'Hitap sözcüğünden sonra virgül konur; noktalı virgül yanlıştır.','dikkat')],
 'dogru','C',('Kendi içinde virgül bulunan öbekler noktalı virgülle ayrılır.','ad, unvan ; ad, unvan'),
 'Noktalı virgülün yerinde kullanıldığı cümle.','Noktalı virgülün ayırdığı parçaların içinde virgül var mı?',[B_NV],
 'Virgülle sıralanan parçaları kendi içinde virgül taşıyorsa noktalı virgülle ayır.')

pq('0016','K-DBNK-04','zor','Kimi/kimi yapısındaki virgüllü cümleleri ayıran noktalı virgülü bulur.',4,
 'Kimi öğrenciler matematik, fizik ve kimya çalışıyor (I) kimi öğrenciler tarih, coğrafya ve felsefe okuyor. Sınav haftasında kütüphane (II) tıklım tıklım doluydu. Görevli (III) öğrencilere (IV) sessiz olmalarını hatırlatıyordu. Akşam kapı (V) kapanınca herkes evine döndü.',
 'noktalı virgül (;)','A',
 ['İki yan da kendi içinde virgülle sıralanmış; cümleleri noktalı virgül ayırır.','Özne ile tümleç arasına işaret konmaz.','Özne ile dolaylı tümleç arasına işaret konmaz.','Dolaylı tümleç ile nesne arasına işaret konmaz.','Özne ile yüklem arasına işaret konmaz.'],
 ('Ögeleri virgülle ayrılmış sıralı cümleler noktalı virgülle ayrılır.','…kimya çalışıyor ; kimi…'),
 'Noktalı virgül getirilmesi gereken yer.','Hangi iki cümlenin ikisi de içinde virgül taşıyor?',[B_NV],
 'Virgülü yoğun iki cümle yan yana geliyorsa onları noktalı virgül ayırır.')

# ---- Kart 05: iki nokta ----
dq('0017','K-DBNK-05','kolay','İki noktanın tamamlanmış cümleden sonra yerinde kullanıldığı cümleyi belirler.',2,
 'Aşağıdakilerden hangisinde iki nokta (:) doğru yerde kullanılmıştır?',
 [('Okulumuzda: spor, müzik, tiyatro ve resim kulüpleri bulunuyor.',False,'İki noktadan önceki bölüm tamamlanmış bir cümle değildir; yüklem sonra gelmektedir.'),
  ('Yarın pikniğe şunları götüreceğiz: ekmek, peynir ve zeytin.',True,'Cümle tamamlanmış, ardından sıralama gelmiştir; doğrudur.'),
  ('Yarın: sabah erkenden yola çıkıp akşama kadar yürüyeceğiz.',False,'Zaman zarfından sonra, cümle sürerken iki nokta konmaz.','dikkat'),
  ('Dedem bana: köydeki bahçesini ve evini armağan etti.',False,'Dolaylı tümleçten sonra, cümle bitmeden iki nokta konmaz.'),
  ('Kerem yemekte: sıcak tarhana çorbasını afiyetle içti.',False,'Yer tümlecinden sonra, yüklem gelmeden iki nokta konmaz.','dikkat')],
 'dogru','B',('İki nokta, anlamı tamamlanmış bir cümleden sonra açıklama ya da sıralama gelecekse konur.','tam cümle : sıralama'),
 'İki noktanın yerinde kullanıldığı cümle.','İki noktadan önceki bölüm kendi başına bir cümle mi?',[B_IKI],
 'İki noktadan önceki bölümü tek başına oku; cümle bitmişse yerindedir.')

pq('0018','K-DBNK-05','orta','Örnek ve sıralama öncesi iki noktanın yerini parçada bulur.',3,
 'Yaz tatilinde çocuklarla birlikte doğa yürüyüşlerine çıktık. Çantamıza hep (II) aynı şeyleri koyardık (III) su, bisküvi ve küçük bir battaniye. Yürüyüş sırasında (IV) kuşları (V) izlerdik.'.replace('Yaz tatilinde çocuklarla','Yaz tatilinde (I) çocuklarla'),
 'iki nokta (:)','C',
 ['Zarf tümleci ile özne arasına işaret konmaz.','Tümleç ile nesne arasına iki nokta konmaz; cümle henüz bitmemiştir.','Cümle tamamlanmıştır ve ardından sıralanan örnekler gelmektedir; iki nokta konur.','Zarf tümleci ile nesne arasına iki nokta konmaz.','Nesne ile yüklem arasına iki nokta konmaz.'],
 ('Tamamlanmış cümleden sonra örnek ya da sıralama gelecekse iki nokta konur.','…koyardık: su, bisküvi…'),
 'İki nokta getirilmesi gereken yer.','Hangi cümlenin sonunda bir sıralama başlıyor?',[B_IKI],
 'Sıralama ya da örnek başlamadan hemen önce cümle tamamlanıyorsa iki nokta konur.')

dq('0019','K-DBNK-05','orta','İki noktanın cümle bitmeden gereksiz kullanıldığı cümleyi belirler.',3,
 'Aşağıdaki cümlelerin hangisinde iki nokta (:) gereksiz kullanılmıştır?',
 [('Babam sık sık şöyle derdi: “Çalışan kazanır.”',True,'Alıntıdan önce tamamlanmış cümleden sonra iki nokta konmuş; doğrudur.'),
  ('Pazar günü şu işlere bakacağız: bahçeyi sulamak, kapıyı boyamak, çatıyı onarmak.',True,'Tamamlanmış cümleden sonra sıralama geldiği için iki nokta yerindedir.','dikkat'),
  ('Tabloda üç rakam dikkat çekiyor: 12, 18 ve 24.',True,'Cümle tamamlanmış, ardından sıralama gelmiştir; doğrudur.'),
  ('Şu kuralı unutma: yanlış cevap puan kaybettirir.',True,'Açıklama öncesinde cümle tamamlanmıştır; doğrudur.','dikkat'),
  ('Sınıfta şu öğrenciler: Elif, Kerem ve Defne ödev yapıyordu.',False,'İki noktadan önceki bölüm tamamlanmamıştır; yüklem sonradan gelir, bu yüzden iki nokta gereksizdir.')],
 'yanlis','E',('İki nokta, tamamlanmış bir cümleden sonra konur; yüklemden önce konmaz.','tam cümle : açıklama'),
 'İki noktanın gereksiz kullanıldığı cümle.','İki noktadan önce yüklem söylenmiş mi?',[B_IKI],
 'İki noktadan sonra yüklem geliyorsa iki nokta yanlış yerdedir.')

pq('0020','K-DBNK-05','zor','Alıntıdan önce iki noktanın yerini, benzer yerlerden ayırarak bulur.',4,
 'Köyümüzdeki yaşlı ressam (I) çocuklara sabrın (II) önemini anlatırdı. Her derse (III) aynı sözle başlardı (IV) “Önce iyi bak, sonra çiz.” Çocuklar bu sözü (V) defterlerinin kapağına yazardı.',
 'iki nokta (:)','D',
 ['Özne ile dolaylı tümleç arasına işaret konmaz.','Tamlayan ile tamlanan arasına işaret konmaz.','Dolaylı tümleç ile zarf tümleci arasına işaret konmaz.','Cümle tamamlanmış, ardından doğrudan alıntı gelmektedir; iki nokta konur.','Nesne ile dolaylı tümleç arasına işaret konmaz.'],
 ('Doğrudan alıntıdan önce, tamamlanmış cümleden sonra iki nokta konur.','…başlardı: “Önce …”'),
 'İki nokta getirilmesi gereken yer.','Tırnak içindeki söz hangi cümlenin hemen ardından geliyor?',[B_IKI],
 'Tırnak içindeki söz yeni başlıyorsa, ondan önceki tamamlanmış cümleye iki nokta koy.')

# ---- Kart 06: boşluk sırası ----
dq('0021','K-DBNK-06','kolay','Cevap sözcüğü sonrası virgül ve cümle sonu noktayı birlikte uygular.',2,
 'Hayır ( ) o gün sinemaya gitmedik ( )\nAşağıdaki cümlede boş bırakılan yerlere sırasıyla hangi noktalama işaretleri getirilmelidir?',
 [('(;) (.)',False,'Cevap sözcüğünden sonra noktalı virgül değil virgül konur.'),
  ('(:) (.)',False,'İki nokta açıklama ya da sıralama öncesi konur; “Hayır”dan sonra konmaz.'),
  ('(,) (.)',True,'“Hayır”dan sonra virgül, bildirme cümlesinin sonuna nokta gelir.'),
  ('(,) (;)',False,'Cümle sonuna noktalı virgül değil nokta konur.','dikkat'),
  ('(,) (:)',False,'Cümle sonuna iki nokta değil nokta konur.','dikkat')],
 'dogru','C',('Cevap sözcüğünden sonra virgül, bildirme cümlesinin sonuna nokta konur.','Hayır, … .'),
 'Boşluklara sırasıyla getirilecek işaretler.','Birinci boşlukta cevap sözcüğünden sonra, ikincisinde cümle sonunda ne gelir?',[B_HIT],
 'İşaret dizilerinde önce her boşluğun kuralını ayrı ayrı bul, sonra diziyi eşleştir.')

dq('0022','K-DBNK-06','orta','Cevap sözcüğü, eş görevli özneler ve cümle sonu için işaret dizisini kurar.',3,
 'Evet ( ) Elif ( ) Kerem ve Defne bu sabah geldi ( )\nBu cümlede yay ayraçla belirtilen yerlere sırasıyla hangi işaretler konulmalıdır?',
 [('(,) (,) (.)',True,'“Evet”ten sonra virgül, eş görevli özneler arasında virgül, cümle sonunda nokta; doğrudur.'),
  ('(;) (,) (.)',False,'Cevap sözcüğünden sonra noktalı virgül konmaz; virgül gelir.'),
  ('(,) (;) (.)',False,'Eş görevli özneler arasına noktalı virgül değil virgül konur.','dikkat'),
  ('(,) (,) (:)',False,'Cümle sonuna iki nokta değil nokta konur.'),
  ('(,) (:) (.)',False,'Eş görevli özneler arasına iki nokta konmaz; virgül konur.','dikkat')],
 'dogru','A',('Cevap sözcüğünden ve eş görevli ögelerden sonra virgül, bildirme cümlesinin sonuna nokta konur.','Evet, Elif, Kerem ve … .'),
 'Boşluklara sırasıyla getirilecek işaretler.','Her boşlukta önce hangi ögenin geldiğini belirle.',[B_HIT,B_ES],
 'Dizideki tek yanlış işaret, çeldiricinin bütün dizisini geçersiz kılar; her boşluğu ayrı sına.')

dq('0023','K-DBNK-06','orta','Sıralama öncesi iki nokta, sıralı adlar arası virgül ve cümle sonu noktayı birleştirir.',3,
 'Atölyede şu araçları kullandık ( ) çekiç ( ) testere ve eğe ( )\nCümledeki boşluklara sırasıyla aşağıdaki dizilerden hangisi getirilirse noktalama doğru olur?',
 [('(,) (,) (.)',False,'“Şu araçları kullandık” cümlesi sıralamaya hazırlar; birinci boşluğa virgül değil iki nokta konur.'),
  ('(:) (,) (.)',True,'Sıralama öncesi iki nokta, sıralı adlar arasında virgül, sonda nokta; doğrudur.'),
  ('(:) (;) (.)',False,'Sıralı adlar arasında noktalı virgül değil virgül kullanılır.','dikkat'),
  ('(:) (,) (;)',False,'Cümle sonuna noktalı virgül değil nokta konur.'),
  ('(;) (,) (.)',False,'Sıralamadan önce noktalı virgül değil iki nokta konur.','dikkat')],
 'dogru','B',('Sıralama başlamadan önce iki nokta, sıralı adlar arasında virgül konur.','… kullandık: çekiç, testere ve eğe.'),
 'Boşluklara sırasıyla getirilecek işaretler.','İlk boşlukta cümle tamamlanıp sıralama başlıyor mu?',[B_IKI,B_ES],
 'Sıralama başlıyorsa iki nokta, sıralama sürüyorsa virgül.')

dq('0024','K-DBNK-06','orta','Alıntı öncesi iki nokta, alıntı içinde hitap sonrası virgül ve cümle sonu nokta dizisini kurar.',3,
 'Öğretmen sınıfa şöyle seslendi ( ) “Çocuklar ( ) lütfen sessiz olun ( )”\nYukarıdaki cümlede ( ) ile gösterilen yerlere sırasıyla hangisindeki işaretler konursa cümle doğru noktalanmış olur?',
 [('(,) (,) (.)',False,'Doğrudan alıntıdan önce, tamamlanmış cümleden sonra iki nokta konur; virgül değil.'),
  ('(:) (;) (.)',False,'Hitap sözcüğünden sonra noktalı virgül değil virgül konur.','dikkat'),
  ('(:) (,) (:)',False,'Alıntının sonuna iki nokta değil nokta konur.'),
  ('(:) (.) (.)',False,'Hitap sözcüğünden sonra nokta değil virgül konur; cümle sürmektedir.','dikkat'),
  ('(:) (,) (.)',True,'Alıntı öncesi iki nokta, hitaptan sonra virgül, alıntı sonunda nokta; doğrudur.')],
 'dogru','E',('Alıntıdan önce iki nokta, alıntı içindeki hitaptan sonra virgül, cümle sonunda nokta konur.','… seslendi: “Çocuklar, … olun.”'),
 'Boşluklara sırasıyla getirilecek işaretler.','Her boşluğun kendi kuralını (alıntı, hitap, bitiş) ayrı ayrı ara.',[B_IKI,B_HIT],
 'İç içe yapılarda işaretleri dıştan içe, sırayla çöz.')

dq('0025','K-DBNK-06','zor','Virgüllü ilk cümleyi ayıran noktalı virgülü diziye yerleştirir.',4,
 'Bahçeye gül ( ) lale ve sümbül dikildi ( ) bostana domates ( ) biber ve patlıcan ekildi ( )\nAşağıdaki cümlede ( ) bırakılan yerlere sırasıyla hangi noktalama işaretlerinin konması gerekir?',
 [('(;) (;) (,) (.)',False,'Sıralı adlar arasına noktalı virgül değil virgül konur.'),
  ('(,) (,) (,) (.)',False,'İki yan da kendi içinde virgülle sıralandığından cümleleri virgül değil noktalı virgül ayırır.','dikkat'),
  ('(,) (;) (,) (;)',False,'Cümle sonuna noktalı virgül değil nokta konur.'),
  ('(,) (;) (,) (.)',True,'Sıralı adlar arasında virgül, virgüllü cümleleri ayıran noktalı virgül, sonda nokta; doğrudur.'),
  ('(,) (:) (,) (.)',False,'İkinci cümle ilkinin açıklaması değildir; iki nokta yerinde değildir.','dikkat')],
 'dogru','D',('Sıralı adlar virgülle, içinde virgül bulunan cümleler noktalı virgülle ayrılır.','gül, lale ve sümbül dikildi ; … domates, biber … .'),
 'Boşluklara sırasıyla getirilecek işaretler.','İki cümlenin de içindeki virgüllere bak; sınırı ona göre belirle.',[B_NV,B_ES],
 'İki yanı da virgüllü cümleleri ayırırken virgül işe yaramaz; noktalı virgül gerekir.')
bitir(Q)
