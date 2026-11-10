import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_kim as H
from _hafif_kim import *
H.KONU='Asitler, Bazlar ve Tuzlar'
P=Parti('asitbaz','Asitler, Bazlar ve Tuzlar','kim|Asitler, Bazlar ve Tuzlar',ders='TYT Kimya',idon='tytkim')
KY='ÖSYM 2018–2025 (asitler ve bazlar, tepkimeleri) · MEB 10. sınıf'
kart('K-ASBZ-01','Asit özellikleri','Asit sulu çözeltisinde H⁺ verir; mavi turnusolu kırmızıya çevirir, elektriği iletir, aktif metalle H₂ gazı oluşturur.','Asit–metal tepkimesinde O₂ çıktığını sanmak.','kolay','öncüllü',2,'kim-ab-ozellik','Asitlerin genel özellikleri',KY)
kart('K-ASBZ-02','Ayıraç davranışı','Turnusol ve fenolftalein renk değişiminden çözeltinin asit, baz ya da nötr olduğu çıkarılır.','Renk değişmeyen çözeltiyi asit sanmak.','orta','düz',3,'kim-ab-ayirac','Ayıraçlarla çözelti türü',KY)
kart('K-ASBZ-03','Tuz formülü','Nötrleşmede katyon ve anyon yükleri çaprazlanarak tuzun formülü yazılır.','Yükleri indis olarak ters yazmak ya da hiç çaprazlamamak.','orta','düz',3,'kim-ab-tuz','Nötrleşme tuzunun formülü',KY)
kart('K-ASBZ-04','Asit–metal tepkimesi','Metal + asit → tuz + H₂; mol sayıları katsayılarla orantılı, kütle = mol × mol kütlesi.','Mol sayısı yerine kütle yazmak; H₂ için 2 g/mol yerine 1 g/mol kullanmak.','orta','hikâyeli',3,'kim-ab-metal','Asit–metal tepkimesinde H₂ kütlesi',KY)
kart('K-ASBZ-05','pH değeri yorumu','pH < 7 asit, 7 nötr, > 7 baz; baz eklenince pH artar, seyrelince nötre yaklaşır.','Seyreltmeyle bazik çözeltinin pH’ının arttığını sanmak.','zor','tablo',4,'kim-ab-ph','pH değerlerini yorumlama',KY)
kart('K-ASBZ-06','Nötrleşme hesabı','Denkleştirilmiş tepkimede mol oranı katsayılardan, tuz kütlesi mol × mol kütlesinden bulunur.','Tuzun mol sayısını bazın mol sayısına eşit almak; su kütlesini unutmak.','zor','hikâyeli',4,'kim-ab-notr','Nötrleşmede oluşan tuz kütlesi',KY)
# ---- 0001
d={'I':(True,'asitler mavi turnusol kâğıdını kırmızıya çevirir'),
   'II':(True,'asitler sulu çözeltisinde iyon verdiği için elektriği iletir'),
   'III':(False,'aktif metallerle tepkimede açığa çıkan gaz oksijen değil hidrojendir')}
r=onc(d,[('I','II'),('I',),('II',),('III',),('I','III')])
mk(P,'0001',tipId='kim-ab-ozellik',tip='Asitlerin genel özellikleri',z='kolay',alt='Asitler ve Bazlar',kaz='Asitlerin genel özelliklerini ayırt eder.',kalip='öncüllü',adim=2,
 kart='K-ASBZ-01 (asit özellikleri) · turnusol, iletkenlik, metal tepkimesi',
 metin='Asitlerle ilgili aşağıdaki ifadeler veriliyor.\nI. Mavi turnusol kâğıdını kırmızıya çevirir.\nII. Sulu çözeltileri elektriği iletir.\nIII. Aktif metallerle tepkimesinde oksijen gazı açığa çıkar.\nBuna göre hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Asitler için doğru olan ifadeler.',
 ip=['Asitlerin ayıraçlara, elektriğe ve metallere etkisini ayrı ayrı hatırla.'],
 bilgi=[B('Asitlerin özellikleri','Asit suda H⁺ iyonu verir; tadı ekşidir, mavi turnusolu kırmızıya çevirir, sulu çözeltisi elektriği iletir. Aktif metalle tepkimesinde H₂ gazı açığa çıkar. Örnek: Zn + 2HCl → ZnCl₂ + H₂')],
 ad=[A('Turnusol','Asit mavi turnusolu kırmızıya çevirir.','I: doğru'),A('İletkenlik','Sulu çözeltide iyonlar oluştuğu için çözelti elektriği iletir.','II: doğru'),A('Metal tepkimesi','Açığa çıkan gaz hidrojendir, oksijen değildir.','III: yanlış'),A('Sonuç','Doğru olanlar toplanır.',etk(d)+' · Sonuç: I ve II')],
 puf='Asit–aktif metal tepkimesinin gazı hep hidrojendir.')
# ---- 0002
G_=lambda a,b,c:f'X: {a}, Y: {b}, Z: {c}'
S=[(G_('baz','asit','nötr'),False,'mavi turnusolu kırmızıya çeviren X asittir, kırmızı turnusolu maviye çeviren Y bazdır'),
   (G_('asit','baz','asit'),False,'iki turnusolu da değiştirmeyen Z asit değil nötrdür'),
   (G_('nötr','baz','asit'),False,'mavi turnusolu kırmızıya çeviren X nötr değil asittir'),
   (G_('asit','nötr','baz'),False,'Y kırmızı turnusolu maviye çevirip fenolftaleini pembe yaptığı için bazdır'),
   (G_('asit','baz','nötr'),True,'')]
r=tek(S,True)
mk(P,'0002',tipId='kim-ab-ayirac',tip='Ayıraçlarla çözelti türü',z='orta',alt='Asitler ve Bazlar',kaz='Ayıraçların renk değişimlerinden çözeltilerin asit, baz ya da nötr olduğunu belirler.',kalip='düz',adim=3,
 kart='K-ASBZ-02 (ayıraç davranışı) · turnusol ve fenolftalein gözlemleri',
 metin='X, Y ve Z çözeltileriyle yapılan deneylerde şu gözlemler elde ediliyor.\nX: Mavi turnusol kâğıdını kırmızıya çevirir.\nY: Kırmızı turnusol kâğıdını maviye çevirir ve fenolftaleini pembe yapar.\nZ: Kırmızı ve mavi turnusol kâğıtlarının rengini değiştirmez.\nBuna göre X, Y ve Z çözeltilerinin türleri aşağıdakilerden hangisinde doğru verilmiştir?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='X, Y ve Z çözeltilerinin asit, baz ya da nötr olarak doğru sınıflandırması.',
 ip=['Her gözlemi ayrı değerlendir: hangi renk değişimi asite, hangisi baza, hiç değişmemesi hangisine işaret eder?'],
 bilgi=[B('Ayıraçlar','Asit mavi turnusolu kırmızıya çevirir. Baz kırmızı turnusolu maviye çevirir ve fenolftaleini pembe yapar. Nötr çözelti turnusol kâğıtlarının rengini değiştirmez. Örnek: saf su nötrdür')],
 ad=[A('X çözeltisi','Mavi turnusol kırmızıya dönüyor.','X: asit'),A('Y çözeltisi','Kırmızı turnusolun maviye dönmesi ve fenolftaleinin pembe olması baz belirtisidir.','Y: baz'),A('Z çözeltisi','İki turnusol da değişmiyor.','Z: nötr'),A('Şıkları karşılaştır','Üç sonuç aynı anda doğru olan tek şık seçilir.','X: asit · Y: baz · Z: nötr → E')],
 puf='Turnusolda değişim yoksa çözelti nötrdür; asit ya da baz değildir.')
# ---- 0003
yuk={'Al':3,'SO4':2}
idx=lambda a,b:3*a==2*b
adaylar=[(1,1),(3,2),(2,3),(2,1),(1,3)]
assert [x for x in adaylar if idx(*x)]==[(2,3)]
S=[('AlSO₄',False,'Al³⁺ ve SO₄²⁻ yükleri eşit olmadığı için tek tek birleşmez, yükler çaprazlanmalıdır'),
   ('Al₃(SO₄)₂',False,'çaprazlama ters yapılmış; Al³⁺ için indis 2, SO₄²⁻ için indis 3 olmalıdır'),
   ('Al₂(SO₄)₃',True,''),
   ('Al₂SO₄',False,'SO₄²⁻ iyonunun indisi 3 olmalıdır, yükler dengelenmemiştir'),
   ('Al(SO₄)₃',False,'toplam yük +3 − 6 = −3 olur; Al için indis 2 yazılmalıdır')]
r=tek(S,True)
mk(P,'0003',tipId='kim-ab-tuz',tip='Nötrleşme tuzunun formülü',z='orta',alt='Asitlerin ve Bazların Tepkimeleri',kaz='Asit–baz tepkimesinde oluşan tuzun formülünü iyon yüklerinden yazar.',kalip='düz',adim=3,
 kart='K-ASBZ-03 (tuz formülü) · Al(OH)₃ + H₂SO₄',
 metin='Alüminyum hidroksit [Al(OH)₃] ile sülfürik asit (H₂SO₄) çözeltisi tam nötrleşme tepkimesi veriyor.\nBuna göre tepkimede oluşan tuzun formülü aşağıdakilerden hangisidir?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Nötrleşmede oluşan tuzun formülü.',
 ip=['Tuz, bazın metal iyonu ile asidin kalıntı iyonundan oluşur; toplam yük sıfır olmalıdır.'],
 bilgi=[B('Nötrleşme','Asit + baz → tuz + su. Tuz, bazdaki metal iyonu ile asittaki negatif iyondan oluşur. Örnek: HCl + NaOH → NaCl + H₂O'),B('Yüklerin çaprazlanması','Katyonun yükü anyonun indisi, anyonun yükü katyonun indisi olur. Örnek: Ca²⁺ ve Cl⁻ → CaCl₂')],
 ad=[A('İyonları bul','Bazdan Al³⁺, asitten SO₄²⁻ iyonu gelir.','Al³⁺ · SO₄²⁻'),A('Yükleri çaprazla','Al’nin yükü SO₄’ün indisi, SO₄’ün yükü Al’nin indisi olur.','Al₂(SO₄)₃'),A('Yük dengesi kontrolü','Toplam yük sıfır olmalıdır.','2 × (+3) + 3 × (−2) = 0')],
 puf='Tuz formülünde yükleri çaprazla, sonra toplam yükün sıfır olduğunu kontrol et.')
# ---- 0004
zn=13; MZn=65; nZn=Fr(zn,MZn); nH2=nZn; mH2=nH2*2
assert nZn==Fr(1,5) and mH2==Fr(2,5) and nZn*1==Fr(1,5) and nH2*2*2==Fr(4,5) and Fr(1,5)*10==2
mk(P,'0004',tipId='kim-ab-metal',tip='Asit–metal tepkimesinde H₂ kütlesi',z='orta',alt='Asitlerin ve Bazların Tepkimeleri',kaz='Asit–metal tepkimesinde oluşan hidrojen gazının kütlesini hesaplar.',kalip='hikâyeli',adim=3,
 kart='K-ASBZ-04 (asit–metal) · 13 g çinko + HCl',
 metin='Bir öğrenci 13 g çinko (Zn) parçasını yeterince hidroklorik asit (HCl) çözeltisine atıyor ve çinkonun tamamı aşağıdaki tepkimeye göre harcanıyor.\nZn + 2HCl → ZnCl₂ + H₂\nZn: 65 g/mol, H: 1 g/mol olduğuna göre açığa çıkan H₂ gazı kaç gramdır?',
 dogru=Fr(2,5),yan=[(Fr(1,5),'H₂’nin mol sayısını (0,2) kütle olarak yazmış.','dikkat'),(Fr(4,5),'H₂’nin mol sayısını 0,4 bulmuş; HCl katsayısı olan 2’yi H₂’ye uygulamış.','bilgi'),(2,'H₂’nin mol kütlesini (2 g/mol) gazın kütlesi sanmış; mol sayısıyla çarpmamış.','islem'),(13,'Çinkonun kütlesini gazın kütlesi saymış.','dikkat')],
 istenen='Açığa çıkan H₂ gazının kütlesi (g).',
 ip=['Önce çinkonun mol sayısını bul; tepkime denkleminde Zn ile H₂ katsayıları aynıdır.'],
 bilgi=[B('Mol sayısı','Mol sayısı = kütle ÷ mol kütlesi. Örnek: 18 g su (18 g/mol) 1 moldür'),B('Katsayı = mol oranı','Denklemde katsayısı aynı olan maddelerin mol sayıları eşittir. H₂ molekülünün mol kütlesi 2 × 1 = 2 g/mol’dür')],
 ad=[A('Zn mol sayısı','Kütle mol kütlesine bölünür.','n = 13 ÷ 65 = 0,2 mol'),A('H₂ mol sayısı','Zn ve H₂ katsayıları 1’dir.','n(H₂) = 0,2 mol'),A('H₂ kütlesi','H₂’nin mol kütlesi 2 g/mol’dür.','m = 0,2 × 2 = 0,4 g')],
 puf='Önce mol, sonra katsayı oranı, en son kütle: kütle → mol → mol → kütle.')
# ---- 0005
pH={'X':3,'Y':6,'Z':7,'T':9,'U':13}
asit=[k for k,v in pH.items() if v<7]; assert asit==['X','Y']
d={'I':(True,'asit çözeltisine baz eklenince asitlik azalır ve pH değeri artar'),
   'II':(False,'bazik bir çözelti seyreltilince pH değeri 7’ye yaklaşır, yani 9’dan küçülür'),
   'III':(True,'pH değeri 7’den küçük olan X ve Y asittir, mavi turnusolu kırmızıya çevirir')}
r=onc(d,[('I',),('II',),('III',),('I','III'),('II','III')])
mk(P,'0005',tipId='kim-ab-ph',tip='pH değerlerini yorumlama',z='zor',alt='Asitler ve Bazlar',kaz='pH değerlerine göre çözeltilerin türünü ve değişim yönünü yorumlar.',kalip='tablo',adim=4,
 kart='K-ASBZ-05 (pH yorumu) · beş çözelti, baz ekleme ve seyreltme',
 metin='Aynı sıcaklıktaki beş çözeltinin pH değerleri tabloda verilmiştir.\nÇözelti | pH\nX | 3\nY | 6\nZ | 7\nT | 9\nU | 13\nBu çözeltilerle ilgili şunlar söyleniyor.\nI. X çözeltisine bir miktar U çözeltisi eklenirse karışımın pH değeri 3’ten büyük olur.\nII. T çözeltisine saf su eklenirse pH değeri 9’dan büyük olur.\nIII. X ve Y çözeltileri mavi turnusol kâğıdını kırmızıya çevirir.\nBuna göre hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan öncüller.',
 ip=['pH 7’den küçükse asit, büyükse baz; asit–baz karışınca ve çözelti seyrelince pH’ın nötr değere doğru nasıl kaydığını düşün.'],
 bilgi=[B('pH ölçeği','pH < 7 asit, pH = 7 nötr, pH > 7 bazdır. Asite baz eklenince pH artar; baza su eklenince pH 7’ye yaklaşır. Örnek: pH 2 olan çözelti pH 5 olandan daha asidiktir')],
 ad=[A('Çözelti türleri','pH değerlerine göre X ve Y asit, Z nötr, T ve U bazdır.','X: 3 · Y: 6 → asit · T: 9 · U: 13 → baz'),A('I. öncül','Asite baz katılınca asitlik azalır, pH yükselir.','pH > 3 → doğru'),A('II. öncül','Seyrelme bazlığı azaltır, pH 7’ye doğru iner.','pH < 9 → yanlış'),A('III. öncül','Asitler mavi turnusolu kırmızıya çevirir.','III: doğru · Sonuç: I ve III')],
 puf='Seyreltmek pH’ı nötr değer olan 7’ye yaklaştırır; asitte artar, bazda azalır.')
# ---- 0006
M={'Na':23,'S':32,'O':16,'H':1}
mNaOH=4; MNaOH=M['Na']+M['O']+M['H']; nNaOH=Fr(mNaOH,MNaOH); nTuz=nNaOH/2; MTuz=2*M['Na']+M['S']+4*M['O']; mTuz=nTuz*MTuz
MAs=2*M['H']+M['S']+4*M['O']; mAsit=nTuz*MAs; mSu=nNaOH*(2*M['H']+M['O'])
assert MNaOH==40 and nNaOH==Fr(1,10) and MTuz==142 and mTuz==Fr(71,10) and mAsit==Fr(49,10) and mSu==Fr(9,5) and mNaOH+mAsit==mTuz+mSu and mNaOH+mAsit==Fr(89,10) and nNaOH*MTuz==Fr(142,10) and nNaOH/4*MTuz==Fr(355,100)
mk(P,'0006',tipId='kim-ab-notr',tip='Nötrleşmede oluşan tuz kütlesi',z='zor',alt='Asitlerin ve Bazların Tepkimeleri',kaz='Nötrleşme tepkimesinde oluşan tuzun kütlesini mol oranlarıyla hesaplar.',kalip='hikâyeli',adim=4,
 kart='K-ASBZ-06 (nötrleşme hesabı) · 4 g NaOH + H₂SO₄',
 metin='Saf sodyum hidroksit (NaOH) katısından 4 g alınıp yeterli miktarda sülfürik asit (H₂SO₄) çözeltisi ile tamamen nötrleştiriliyor.\n2NaOH + H₂SO₄ → Na₂SO₄ + 2H₂O\nH: 1, O: 16, Na: 23, S: 32 g/mol olduğuna göre oluşan Na₂SO₄ tuzu kaç gramdır?',
 dogru=Fr(71,10),yan=[(Fr(355,100),'Tuzun mol sayısını NaOH’ın dörtte biri (0,025 mol) almış.','bilgi'),(Fr(49,10),'Harcanan H₂SO₄ kütlesini tuzun kütlesi sanmış.','dikkat'),(Fr(89,10),'Girenlerin toplam kütlesini yazmış; oluşan suyun kütlesini düşmemiş.','dikkat'),(Fr(142,10),'Tuzun mol sayısını NaOH ile eşit (0,1 mol) almış; katsayıyı kullanmamış.','islem')],
 istenen='Oluşan Na₂SO₄ tuzunun kütlesi (g).',
 ip=['Katsayılara göre 2 mol NaOH’tan 1 mol Na₂SO₄ oluşur; önce NaOH’ın mol sayısını bul.'],
 bilgi=[B('Mol hesabı','Mol sayısı = kütle ÷ mol kütlesi; kütle = mol sayısı × mol kütlesi. Örnek: 40 g NaOH (40 g/mol) 1 moldür'),B('Katsayı oranı','Denklemde katsayılar mol oranını verir: 2NaOH → 1 Na₂SO₄ ise NaOH’ın mol sayısının yarısı kadar tuz oluşur')],
 ad=[A('NaOH mol sayısı','NaOH’ın mol kütlesi 23 + 16 + 1 = 40 g/mol’dür.','n = 4 ÷ 40 = 0,1 mol'),A('Tuz mol sayısı','Katsayıya göre 2 mol NaOH’tan 1 mol tuz oluşur.','n(Na₂SO₄) = 0,1 ÷ 2 = 0,05 mol'),A('Tuz mol kütlesi','Na₂SO₄ = 2 × 23 + 32 + 4 × 16.','M = 46 + 32 + 64 = 142 g/mol'),A('Tuz kütlesi','Mol sayısı mol kütlesiyle çarpılır.','m = 0,05 × 142 = 7,1 g')],
 puf='Hesapta sıra hep aynı: kütle → mol → katsayı oranı → mol → kütle.')
bitir(P,'asitbaz','kim|Asitler, Bazlar ve Tuzlar')
