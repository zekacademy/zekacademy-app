"""Karışım Problemleri · parti 1 (8 ana + 8 kardeş). Her cevap kap benzetimiyle (yöntem 2) ve tarama ile doğrulanır."""
import sys,os
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,os.path.join(H,'..'))
from ortak import *
P=Parti('karisimprob','Karışım Problemleri','prob|Karışım Problemleri')
TT=lambda **k:k
def sirali(s):
    v=[Fr(x.replace(',','.')) for x in s]; assert v==sorted(v) and len(set(v))==5, s
    return s
class Kap:
    """m: çözünen madde miktarı, t: karışımın toplam miktarı."""
    def __init__(s,m,t): s.m=Fr(m); s.t=Fr(t)
    def oran(s): return s.m/s.t*100
    def ekle(s,madde=0,su=0): s.m+=madde; s.t+=madde+su; return s
    def buhar(s,su): assert su<s.t-s.m; s.t-=su; return s
    def al(s,miktar):
        m=s.m*Fr(miktar)/s.t; s.m-=m; s.t-=miktar; return Kap(m,miktar)
    def dok(s,k): s.m+=k.m; s.t+=k.t; return s
def tek_cozum(f,aday):
    r=[x for x in aday if f(x)]; assert len(r)==1, r; return r[0]
YARIM=[Fr(n,2) for n in range(1,4001)]

ORAN=B('Karışım oranı','oran = maddenin miktarı ÷ karışımın toplam miktarı. Örnek: 200 g tuzlu suda 30 g tuz varsa tuz oranı 30/200 = %15')
YUZ=B('Yüzde','%20 = 20/100. Örnek: 150 g’ın %20’si 150 × 20/100 = 30 g')
SABIT=B('Değişmeyen madde','su eklenir ya da buharlaşırsa tuz (şeker) miktarı değişmez; yalnız karışımın toplamı değişir')
TOPLA=B('Karışımları birleştirme','maddeler kendi arasında, toplamlar kendi arasında toplanır. Örnek: 10 g tuzlu 100 g ile 30 g tuzlu 100 g ⇒ 40/200 = %20')
CEKME=B('Karışımdan almak','alınan kısım, karışımın o anki oranında madde içerir. Örnek: %20’lik karışımdan alınan 50 g’da 10 g madde vardır')

# ===================== 0001 oran KOLAY
k=Kap(60,300); assert k.oran()==20; k.ekle(madde=60,su=140); assert k.oran()==24 and (k.m,k.t)==(120,500)
assert Fr(60,500)*100==12 and Fr(60,200)*100==30 and (20+30)/Fr(2)==25
s=sirali(['12','20','24','25','30'])
P.R('0001','kr-oran','Karışımın oranı','kolay','Karışım oranı','Karışıma eklenen tuz ve suyu hem madde hem toplam miktarına yansıtarak yeni oranı bulur.','hikâyeli',2,
 'K-KR-01 (karışıma madde ve su ekleme) · yeni sayılar, eklenen hem tuz hem su',
 'Tuz oranı %20 olan 300 gram tuzlu suya 60 gram tuz ve 140 gram su ekleniyor.\nBuna göre oluşan karışımın tuz oranı yüzde kaçtır?',
 s,'C','Yeni karışımın tuz oranı.',
 ['Başlangıçta 300 gramın içinde kaç gram tuz var?','Ekleme sonunda tuz kaç gram, karışım kaç gram oldu?','Yeni tuz miktarını yeni toplama böl.'],[ORAN,YUZ],
 [A('Başlangıçtaki tuz','300 gramın %20’si tuzdur.','300 × 20/100 = 60 g tuz'),
  A('Yeni miktarlar','Eklenen tuz hem tuza hem toplama, su yalnız toplama eklenir.','tuz: 60 + 60 = 120 g · toplam: 300 + 60 + 140 = 500 g'),
  A('Yeni oran','Tuzu toplama böl.','120/500 = 24/100 = %24')],
 'Eklenen her şey (tuz da) karışımın toplamını büyütür; oranı hep yeni tuz ÷ yeni toplam ile hesapla.',
 dict(A='12, eklenen tuzu unutup yalnız toplamı büyütmek (60/500).',B='20, eklemelerin oranı değiştirmediğini sanmak.',
      D='25, eski oran (%20) ile eklenen 200 gramın oranının (%30) ortalamasını almak; miktarlar farklı.',E='30, yalnız eklenen kısmın (60 g tuz + 140 g su) oranı.'),
 TT(A='dikkat',B='bilgi',D='bilgi',E='dikkat'))
k=Kap(60,400); assert k.oran()==15; k.ekle(madde=40,su=60); assert k.oran()==20
assert Fr(60,500)*100==12 and Fr(100,400)*100==25 and (15+40)/Fr(2)==Fr(55,2) and Fr(40,100)*100==40
s=sirali(['12','20','25','27,5','40'])
P.K('0001','Şeker oranı %15 olan 400 gram şekerli suya 40 gram şeker ve 60 gram su ekleniyor.\nBuna göre oluşan karışımın şeker oranı yüzde kaçtır?',
 s,'B','Yeni karışımın şeker oranı.',
 ['400 gramın içinde kaç gram şeker var?','Eklemelerden sonra şeker ve toplam kaç gram oldu?','Yeni şekeri yeni toplama böl.'],[ORAN,YUZ],
 [A('Başlangıçtaki şeker','400 gramın %15’i.','400 × 15/100 = 60 g'),
  A('Yeni miktarlar','Şeker hem şekere hem toplama eklenir.','şeker: 60 + 40 = 100 g · toplam: 400 + 40 + 60 = 500 g'),
  A('Yeni oran','Şekeri toplama böl.','100/500 = 20/100 = %20')],
 'Oran sorularında madde ve toplamı ayrı sütunlarda izle; en sonda böl.',
 dict(A='12, eklenen şekeri unutmak (60/500).',C='25, yeni şekeri eski toplama bölmek (100/400).',
      D='27,5, %15 ile eklenen 100 gramın oranının (%40) ortalamasını almak; miktarlar eşit değil.',E='40, yalnız eklenen 100 gramın oranı.'),
 TT(A='dikkat',C='islem',D='bilgi',E='dikkat'))

# ===================== 0002 buharlaştırma KOLAY
y=tek_cozum(lambda y:y<540 and Kap(60,600).buhar(y).oran()==15,YARIM); assert y==200
assert 600*Fr(5,100)==30 and 600-60==540
s=sirali(['30','60','200','400','540'])
P.R('0002','kr-buharlasma','Su ekleme ve buharlaştırma','kolay','Su ekleme ve buharlaştırma','Buharlaşmada tuz miktarının sabit kaldığını kullanarak yeni toplamı ve buharlaşan suyu bulur.','hikâyeli',2,
 'K-KR-03 (buharlaşınca oran artar) · yeni kurgu (kaynatma), istenen: buharlaşan su',
 'Tuz oranı %10 olan 600 gram tuzlu su bir süre kaynatılıyor ve suyun bir kısmı buharlaşıyor. Buharlaşmadan sonra karışımın tuz oranı %15 oluyor.\nBuharlaşma sırasında tuz kaybı olmadığına göre kaç gram su buharlaşmıştır?',
 s,'C','Buharlaşan suyun miktarı.',
 ['600 gramın içinde kaç gram tuz var? Buharlaşınca bu miktar değişir mi?','Aynı tuz, yeni karışımın %15’i ise yeni karışım kaç gramdır?','Eski toplamdan yeni toplamı çıkar.'],[ORAN,SABIT],
 [A('Tuz miktarı','600 gramın %10’u; buharlaşmada değişmez.','600 × 10/100 = 60 g'),
  A('Yeni toplam','60 g tuz yeni karışımın %15’i.','60 = T × 15/100 ⇒ T = 400 g'),
  A('Buharlaşan su','Toplamdaki azalma suyun buharlaşmasıdır.','600 − 400 = 200 g')],
 'Buharlaşma ve su eklemede madde miktarı sabittir: önce maddeyi bul, sonra yeni toplamı.',
 dict(A='30, oran farkını (%5) 600 ile çarpmak; tuz sabit kalır, toplam değişir.',B='60, tuzun miktarı; buharlaşan su değil.',
      D='400, buharlaşmadan sonra kalan karışım; soru buharlaşan suyu soruyor.',E='540, başlangıçtaki suyun tamamı; suyun yalnız bir kısmı buharlaştı.'),
 TT(A='bilgi',B='dikkat',D='dikkat',E='dikkat'))
x=tek_cozum(lambda x:Kap(75,250).ekle(su=x).oran()==25,YARIM); assert x==50
assert 250*Fr(5,100)==Fr(25,2) and 250-75==175
s=sirali(['12,5','50','75','175','300'])
P.K('0002','Şeker oranı %30 olan 250 gram şekerli suya bir miktar su ekleniyor ve karışımın şeker oranı %25’e düşüyor.\nBuna göre karışıma kaç gram su eklenmiştir?',
 s,'B','Eklenen suyun miktarı.',
 ['250 gramda kaç gram şeker var? Su eklenince değişir mi?','Aynı şeker yeni karışımın %25’i ise yeni karışım kaç gram?','Yeni toplamdan eski toplamı çıkar.'],[ORAN,SABIT],
 [A('Şeker miktarı','250 gramın %30’u; su eklenince değişmez.','250 × 30/100 = 75 g'),
  A('Yeni toplam','75 g, yeni karışımın %25’i.','75 = T × 25/100 ⇒ T = 300 g'),
  A('Eklenen su','Toplamdaki artış eklenen sudur.','300 − 250 = 50 g')],
 'Su eklemede madde aynı kalır; yeni toplam = madde ÷ yeni oran.',
 dict(A='12,5, oran farkını (%5) 250 ile çarpmak; şeker sabit kalır, toplam değişir.',C='75, karışımdaki şeker miktarı; eklenen su değil.',
      D='175, başlangıçtaki su miktarı (250 − 75).',E='300, su eklendikten sonraki toplam; soru eklenen suyu soruyor.'),
 TT(A='bilgi',C='dikkat',D='dikkat',E='dikkat'))

# ===================== 0003 karıştırma ORTA
k=Kap(30,300).dok(Kap(50,200)); assert k.oran()==16
assert (10+25)/Fr(2)==Fr(35,2) and Fr(10*200+25*300,500)==19
s=sirali(['16','17,5','19','35','80'])
P.R('0003','kr-karistirma','İki karışımı karıştırma','orta','İki karışımı karıştırma','İki karışımın tuz miktarlarını ve toplamlarını ayrı ayrı toplayarak yeni oranı bulur.','hikâyeli',3,
 'K-KR-02 (iki karışım birleşiyor) · yeni sayılar, istenen: yeni oran',
 'Tuz oranı %10 olan 300 gram tuzlu su ile tuz oranı %25 olan 200 gram tuzlu su bir kapta karıştırılıyor.\nBuna göre oluşan karışımın tuz oranı yüzde kaçtır?',
 s,'A','Karışımın tuz oranı.',
 ['Her karışımda kaç gram tuz var?','Birleşince toplam tuz ve toplam karışım kaç gram olur?','Sonuç %10 ile %25 arasında ve miktarı fazla olan karışıma daha yakın olmalı.'],[ORAN,TOPLA],
 [A('Birinci karışım','300 gramın %10’u.','300 × 10/100 = 30 g tuz'),
  A('İkinci karışım','200 gramın %25’i.','200 × 25/100 = 50 g tuz'),
  A('Birleştir','Tuzlar ve toplamlar ayrı ayrı toplanır.','tuz: 30 + 50 = 80 g · toplam: 300 + 200 = 500 g · 80/500 = %16')],
 'Yeni oran iki oranın arasındadır ve miktarı çok olan karışımın oranına daha yakındır; ortalama ancak miktarlar eşitse doğrudur.',
 dict(B='17,5, iki oranın aritmetik ortalaması; miktarlar eşit olmadığı için geçersiz.',C='19, miktarları oranlara ters eşlemek (%10 ile 200 g, %25 ile 300 g).',
      D='35, iki oranı toplamak; oran, toplam tuz ÷ toplam karışımdır.',E='80, karışımdaki tuzun gram cinsinden miktarı; soru oranı soruyor.'),
 TT(B='bilgi',C='dikkat',D='bilgi',E='dikkat'))
k=Kap(40,100).dok(Kap(80,400)); assert k.oran()==24
assert (40+20)/Fr(2)==30 and Fr(40*400+20*100,500)==36
s=sirali(['24','30','36','60','120'])
P.K('0003','Şeker oranı %40 olan 100 gram şurup ile şeker oranı %20 olan 400 gram şekerli su karıştırılıyor.\nBuna göre elde edilen karışımın şeker oranı yüzde kaçtır?',
 s,'A','Karışımın şeker oranı.',
 ['Şurupta ve şekerli suda kaç gram şeker var?','Toplam şekeri toplam karışıma böl.','Sonuç, miktarı çok olan karışımın oranına (%20) daha yakın olmalı.'],[ORAN,TOPLA],
 [A('Şuruptaki şeker','100 gramın %40’ı.','100 × 40/100 = 40 g'),
  A('Şekerli sudaki şeker','400 gramın %20’si.','400 × 20/100 = 80 g'),
  A('Birleştir','Şekerler ve toplamlar toplanır.','şeker: 40 + 80 = 120 g · toplam: 500 g · 120/500 = %24')],
 'İki karışım birleşince madde ve toplam ayrı ayrı toplanır; oranların ortalaması alınmaz.',
 dict(B='30, iki oranın aritmetik ortalaması; şekerli su şuruptan çok daha fazla.',C='36, miktarları oranlara ters eşlemek (%40 ile 400 g).',
      D='60, oranları toplamak.',E='120, toplam şekerin gram cinsinden miktarı; oran değil.'),
 TT(B='bilgi',C='dikkat',D='bilgi',E='dikkat'))

# ===================== 0004 alıp yerine koyma ORTA
k=Kap(100,500); al=k.al(100); assert al.m==20; k.ekle(su=100); assert k.oran()==16
x=tek_cozum(lambda x:Kap(80,500).ekle(madde=x).oran()==20,YARIM); assert x==25
assert 500*Fr(4,100)==20
s=sirali(['4','20','25','80','100'])
P.R('0004','kr-cekme','Alıp yerine koyma','orta','Alıp yerine koyma','Karışımdan alınan kısmın içindeki maddeyi hesaplar; oranı geri getirmek için eklenecek maddeyi, toplamın da arttığını hesaba katarak bulur.','hikâyeli',4,
 'K-KR-04 (alıp yerine su koyma) · yeni istenen (oranı geri getiren tuz miktarı)',
 'Tuz oranı %20 olan 500 gram tuzlu sudan 100 gram alınıyor ve yerine 100 gram su ekleniyor.\nKarışımın tuz oranının yeniden %20 olması için karışıma kaç gram tuz eklenmelidir?',
 s,'C','Oranı yeniden %20 yapmak için eklenecek tuz.',
 ['Alınan 100 gramın içinde kaç gram tuz vardı?','Su eklendikten sonra karışımda kaç gram tuz, toplam kaç gram var?','x gram tuz eklenince hem tuz hem toplam x artar; denklemi kur.'],[ORAN,CEKME],
 [A('Başlangıç','500 gramın %20’si tuz.','500 × 20/100 = 100 g tuz'),
  A('Alınan kısım','Alınan 100 g da %20 tuzludur.','100 × 20/100 = 20 g tuz gitti · kalan 80 g tuz, 400 g karışım'),
  A('Su eklenince','Toplam yeniden 500 g, tuz 80 g.','80/500 = %16'),
  A('Tuz ekle','x gram tuz hem tuza hem toplama eklenir.','(80 + x)/(500 + x) = 20/100 ⇒ 400 + 5x = 500 + x ⇒ x = 25 g')],
 'Karışıma madde eklerken toplamın da büyüdüğünü unutma; eksilen maddeyi geri koymak oranı eski hâline getirmez.',
 dict(A='4, oran farkını (%20 − %16) gram sanmak.',B='20, eksilen 20 g tuzu geri koymak; eklenen tuz toplamı da büyüttüğü için oran %20’ye ulaşmaz.',
      D='80, karışımda kalan tuz miktarı.',E='100, alınan karışımın miktarı.'),
 TT(A='dikkat',B='bilgi',D='dikkat',E='dikkat'))
k=Kap(120,300); al=k.al(60); assert al.m==24 and al.t-al.m==36; k.ekle(su=60); assert k.oran()==32 and k.m==96
y=tek_cozum(lambda y:y<204 and Kap(96,300).buhar(y).oran()==40,YARIM); assert y==60
assert 300*Fr(8,100)==24 and Fr(96,Fr(40,100))==240
s=sirali(['24','36','60','96','240'])
P.K('0004','Şeker oranı %40 olan 300 gram şerbetten 60 gram alınıp yerine 60 gram su ekleniyor. Şerbetin şeker oranını yeniden %40 yapmak için bir miktar su buharlaştırılacaktır.\nBuharlaşma sırasında şeker kaybı olmadığına göre kaç gram su buharlaştırılmalıdır?',
 s,'C','Oranı yeniden %40 yapmak için buharlaştırılacak su.',
 ['Şerbetten alınan kısımda kaç gram şeker vardı?','Su eklendikten sonra kaç gram şeker kaldı? Buharlaşmada bu değişir mi?','Kalan şeker yeni karışımın %40’ı olmalı; yeni toplamı bul.'],[ORAN,CEKME,SABIT],
 [A('Başlangıç','300 gramın %40’ı şeker.','300 × 40/100 = 120 g'),
  A('Alınan kısım','Alınan 60 g da %40 şekerlidir.','60 × 40/100 = 24 g gitti · kalan 96 g şeker'),
  A('Su eklenince','Toplam yine 300 g.','96/300 = %32'),
  A('Hedef toplam','96 g yeni karışımın %40’ı olmalı.','96 = T × 40/100 ⇒ T = 240 g · 300 − 240 = 60 g')],
 'Buharlaştırmada madde sabittir: hedef toplam = madde ÷ hedef oran.',
 dict(A='24, oran farkını (%8) 300 ile çarpmak ya da net eklenen suyu (60 − 36) buharlaştırmak; giden 24 g şeker geri gelmez.',
      B='36, yalnız alınan kısmın içindeki suyu (60 − 24) buharlaştırmak.',
      D='96, karışımda kalan şeker miktarı.',E='240, buharlaşmadan sonra olması gereken toplam; soru buharlaşan suyu soruyor.'),
 TT(A='bilgi',B='islem',D='dikkat',E='dikkat'))

# ===================== 0005 karıştırma (miktar) ORTA
x=tek_cozum(lambda x:Kap(x*Fr(40,100),x).dok(Kap(30,300)).oran()==20,YARIM); assert x==150
assert tek_cozum(lambda x:x*Fr(40,100)+30==Fr(20,100)*300,YARIM)==75 and 300*Fr(20,10)==600 and 150+300==450
s=sirali(['75','150','300','450','600'])
P.R('0005','kr-karistirma','İki karışımı karıştırma','orta','İki karışımı karıştırma','Hedef orana göre iki karışımın madde dengesini kurarak bilinmeyen karışım miktarını bulur.','hikâyeli',3,
 'K-KR-02 (hedef orana göre miktar) · yeni kurgu (meyve suyu ve içecek), mL birimi',
 'Meyve oranı %40 olan bir miktar meyve suyu, meyve oranı %10 olan 300 mililitre içecekle karıştırılıyor. Oluşan karışımın meyve oranı %20’dir.\nBuna göre karıştırılan meyve suyu kaç mililitredir?',
 s,'B','Karıştırılan %40’lık meyve suyunun miktarı.',
 ['Meyve suyuna x de: içinde kaç mL meyve var?','300 mL içecekte kaç mL meyve var?','Toplam meyve = yeni karışımın (x + 300 mL) %20’si; denklemi kur.'],[ORAN,TOPLA],
 [A('Meyve miktarları','x mL meyve suyunda ve 300 mL içecekte.','x × 40/100 = 0,4x · 300 × 10/100 = 30'),
  A('Denklem','Toplam meyve, yeni karışımın %20’si.','0,4x + 30 = 0,2 × (x + 300) = 0,2x + 60'),
  A('Çöz','x’li terimleri bir tarafa topla.','0,2x = 30 ⇒ x = 150 mL · kontrol: (60 + 30)/450 = %20')],
 'Hedef oranlı karıştırmada denklemi “toplam madde = hedef oran × toplam karışım” diye kur.',
 dict(A='75, sağ tarafta toplamı yalnız 300 almak (0,4x + 30 = 0,2 × 300).',C='300, iki karışımın eşit miktarda olduğunu sanmak; o durumda oran %25 olurdu.',
      D='450, oluşan karışımın toplam miktarı; soru meyve suyunu soruyor.',E='600, oran farklarını (20 ve 10) miktarlara ters eşlemek.'),
 TT(A='islem',C='bilgi',D='dikkat',E='bilgi'))
x=tek_cozum(lambda x:Kap(x*Fr(70,100),x).dok(Kap(80,200)).oran()==50,YARIM); assert x==100
assert 200*Fr(40,100)==80 and 100+200==300 and 200*Fr(20,10)==400
s=sirali(['80','100','200','300','400'])
P.K('0005','Bakır oranı %70 olan bir alaşımdan bir miktar, bakır oranı %40 olan 200 gramlık başka bir alaşımla birlikte eritilerek bakır oranı %50 olan yeni bir alaşım elde ediliyor.\nBuna göre bakır oranı %70 olan alaşımdan kaç gram kullanılmıştır?',
 s,'B','Kullanılan %70’lik alaşımın miktarı.',
 ['%70’lik alaşımdan x gram kullanılsın; içinde kaç gram bakır var?','200 gramlık alaşımda kaç gram bakır var?','Toplam bakır, yeni alaşımın (x + 200) %50’si olmalı.'],[ORAN,TOPLA],
 [A('Bakır miktarları','x gramlık ve 200 gramlık alaşımlarda.','0,7x · 200 × 40/100 = 80'),
  A('Denklem','Toplam bakır yeni alaşımın yarısı.','0,7x + 80 = 0,5 × (x + 200) = 0,5x + 100'),
  A('Çöz','x’li terimleri topla.','0,2x = 20 ⇒ x = 100 g · kontrol: (70 + 80)/300 = %50')],
 'Sonuç oranı hangi karışıma daha yakınsa o karışımdan daha çok kullanılmıştır; burada %50, %40’a yakın.',
 dict(A='80, 200 gramlık alaşımdaki bakır miktarı.',C='200, iki alaşımın eşit miktarda olduğunu sanmak; o durumda oran %55 olurdu.',
      D='300, yeni alaşımın toplam kütlesi.',E='400, oran farklarını miktarlara ters eşlemek.'),
 TT(A='dikkat',C='bilgi',D='dikkat',E='bilgi'))

# ===================== 0006 buharlaştırma + ekleme ORTA
k=Kap(80,500); assert k.oran()==16; k.buhar(100); assert k.oran()==20; k.ekle(madde=100); assert k.oran()==36
assert Fr(180,600)*100==30 and Fr(100,400)*100==25
s=sirali(['16','20','25','30','36'])
P.R('0006','kr-buharlasma','Su ekleme ve buharlaştırma','orta','Su ekleme ve buharlaştırma','Ardışık buharlaştırma ve madde ekleme işlemlerinde madde ve toplamı adım adım izler.','hikâyeli',3,
 'K-KR-03 (buharlaşma ve ekleme ardışık) · iki işlem, istenen: son oran',
 'Şeker oranı %16 olan 500 gram şekerli sudan 100 gram su buharlaştırılıyor. Ardından karışıma 100 gram şeker ekleniyor ve şeker tamamen çözünüyor.\nBuharlaşma sırasında şeker kaybı olmadığına göre son karışımın şeker oranı yüzde kaçtır?',
 s,'E','Son karışımın şeker oranı.',
 ['Başlangıçta kaç gram şeker var?','Buharlaşmadan sonra toplam kaç gram, şeker kaç gram?','Şeker eklenince hem şeker hem toplam artar.'],[ORAN,SABIT],
 [A('Başlangıç','500 gramın %16’sı şeker.','500 × 16/100 = 80 g'),
  A('Buharlaşma','Şeker sabit, toplam azalır.','toplam: 500 − 100 = 400 g · 80/400 = %20'),
  A('Şeker ekleme','Eklenen şeker hem şekere hem toplama girer.','şeker: 80 + 100 = 180 g · toplam: 400 + 100 = 500 g · 180/500 = %36')],
 'Her işlemden sonra “madde kaç, toplam kaç” tablosunu güncelle; buharlaşma yalnız toplamı, madde ekleme ikisini birden değiştirir.',
 dict(A='16, başlangıçtaki oran; buharlaşma ve şeker ekleme oranı artırır.',B='20, şeker eklemeyi unutup yalnız buharlaşmayı hesaplamak.',
      C='25, yalnız eklenen şekeri (100/400) hesaba katmak; karışımda zaten 80 g şeker vardı.',D='30, buharlaşmayı unutup toplamı 600 g almak.'),
 TT(A='bilgi',B='dikkat',C='dikkat',D='dikkat'))
k=Kap(40,400); assert k.oran()==10; k.buhar(150); assert k.oran()==16; k.ekle(madde=50); assert k.oran()==30
assert Fr(90,450)*100==20 and Fr(90,400)*100==Fr(45,2) and Fr(90,250)*100==36
s=sirali(['16','20','22,5','30','36'])
P.K('0006','Tuz oranı %10 olan 400 gram tuzlu sudan 150 gram su buharlaştırılıyor. Sonra karışıma 50 gram tuz eklenip tamamen çözünmesi sağlanıyor.\nBuharlaşma sırasında tuz kaybı olmadığına göre son karışımın tuz oranı yüzde kaçtır?',
 s,'D','Son karışımın tuz oranı.',
 ['400 gramda kaç gram tuz var?','Buharlaşmadan sonra toplam kaç gram oldu?','Tuz eklenince tuz ve toplam ne olur?'],[ORAN,SABIT],
 [A('Başlangıç','400 gramın %10’u tuz.','400 × 10/100 = 40 g'),
  A('Buharlaşma','Tuz sabit, toplam azalır.','toplam: 400 − 150 = 250 g · 40/250 = %16'),
  A('Tuz ekleme','Tuz ve toplam 50’şer gram artar.','tuz: 40 + 50 = 90 g · toplam: 250 + 50 = 300 g · 90/300 = %30')],
 'Buharlaşma yalnız toplamı azaltır; eklenen tuz hem tuzu hem toplamı artırır.',
 dict(A='16, tuz eklemeyi unutup yalnız buharlaşmadan sonraki oranı almak.',B='20, buharlaşmayı unutup toplamı 450 g almak.',
      C='22,5, hem buharlaşmayı hem de eklenen tuzun toplamı artırdığını unutmak (90/400).',E='36, eklenen tuzu toplama katmamak (90/250).'),
 TT(A='dikkat',B='dikkat',C='islem',E='islem'))

# ===================== 0007 alıp yerine koyma ZOR
k=Kap(20,20)
for _ in range(2): k.al(4); k.ekle(su=4)
assert k.m==Fr(64,5) and k.oran()==64 and 20*Fr(4,5)**2==Fr(64,5)
assert Fr(20-8,20)*100==60 and Fr(16,20)*100==80 and 100-64==36
s=sirali(['12,8','36','60','64','80'])
P.R('0007','kr-cekme','Alıp yerine koyma','zor','Alıp yerine koyma','Alıp yerine su koyma işleminin tekrarında her seferinde karışımın o anki oranını kullanır.','hikâyeli',4,
 'K-KR-04 (alıp yerine koyma, tekrarlı) · yeni kurgu (saf portakal suyu), iki tekrar',
 '20 litrelik bir kap saf portakal suyuyla doludur. Kaptan 4 litre portakal suyu alınıp yerine 4 litre su konuyor ve karıştırılıyor. Sonra karışımdan yine 4 litre alınıp yerine 4 litre su konuyor.\nBuna göre son durumda kaptaki karışımın portakal suyu oranı yüzde kaçtır?',
 s,'D','Son karışımın portakal suyu oranı.',
 ['İlk işlemden sonra kapta kaç litre portakal suyu kaldı?','İkinci kez alınan 4 litre saf portakal suyu mu, yoksa karışım mı?','İkinci alınan 4 litrenin içinde karışımın o anki oranında portakal suyu var.'],[ORAN,CEKME],
 [A('İlk işlem','Saf portakal suyundan 4 litre gider, yerine su gelir.','20 − 4 = 16 L portakal · oran 16/20 = %80'),
  A('İkinci alış','Alınan 4 litre %80 portakal suyudur.','4 × 80/100 = 3,2 L portakal gider'),
  A('İkinci işlem sonrası','Yerine su konunca toplam yine 20 L.','16 − 3,2 = 12,8 L portakal'),
  A('Oran','Portakal suyunu toplama böl.','12,8/20 = 64/100 = %64 · kısaca: 20 × (4/5) × (4/5) = 12,8')],
 'Alıp yerine su koyma her tekrarda maddeyi aynı kesirle (kalan/toplam) çarpar.',
 dict(A='12,8, kaptaki portakal suyunun litre cinsinden miktarı; soru oranı soruyor.',B='36, suyun oranı (7,2/20); soru portakal suyunu soruyor.',
      C='60, ikinci seferde de saf portakal suyu alındığını sanmak (20 − 8 = 12 L).',E='80, yalnız ilk işlemden sonraki oran.'),
 TT(A='dikkat',B='dikkat',C='bilgi',E='dikkat'))
k=Kap(10,50)
for _ in range(2): k.al(10); k.ekle(su=10)
assert k.oran()==Fr(64,5) and k.m==Fr(32,5)
assert Fr(10-2-2,50)*100==12 and Fr(8,50)*100==16 and 20-Fr(64,5)==Fr(36,5)
s=sirali(['6,4','7,2','12','12,8','16'])
P.K('0007','Tuz oranı %20 olan 50 kilogramlık bir tuzlu su karışımından 10 kilogram alınıp yerine 10 kilogram su konuyor ve karıştırılıyor. Bu işlem bir kez daha aynı biçimde tekrarlanıyor.\nBuna göre son karışımın tuz oranı yüzde kaçtır?',
 s,'D','Son karışımın tuz oranı.',
 ['Başlangıçta kaç kilogram tuz var?','İlk işlemde alınan 10 kg’da ne kadar tuz var? Sonra oran ne olur?','İkinci alışta alınan 10 kg, yeni oranda tuz içerir.'],[ORAN,CEKME],
 [A('Başlangıç','50 kg’ın %20’si tuz.','50 × 20/100 = 10 kg'),
  A('İlk işlem','Alınan 10 kg’da %20 tuz; yerine su gelir.','10 × 20/100 = 2 kg gider · 8 kg tuz · 8/50 = %16'),
  A('İkinci işlem','Alınan 10 kg bu kez %16 tuzludur.','10 × 16/100 = 1,6 kg gider · 8 − 1,6 = 6,4 kg'),
  A('Oran','Tuzu toplama böl.','6,4/50 = 12,8/100 = %12,8')],
 'Tekrarlı alıp yerine koymada her adımın oranı bir öncekinin (kalan ÷ toplam) katıdır: %20 × 4/5 × 4/5.',
 dict(A='6,4, kalan tuzun kilogram cinsinden miktarı; oran değil.',B='7,2, oranın ne kadar azaldığı (20 − 12,8); soru son oranı soruyor.',
      C='12, ikinci alışta da %20 oranında (2 kg) tuz gittiğini sanmak.',E='16, yalnız ilk işlemden sonraki oran.'),
 TT(A='dikkat',B='dikkat',C='bilgi',E='dikkat'))

# ===================== 0008 kaplar arası aktarım ZOR
k1=Kap(60,200); k2=Kap(30,300); k2.dok(k1.al(100)); assert k2.oran()==15; k1.dok(k2.al(100)); assert k1.oran()==Fr(45,2) and (k1.m,k1.t)==(45,200)
assert Fr(30+10,200)*100==20 and Fr(90,500)*100==18
s=sirali(['10','15','18','20','22,5'])
P.R('0008','kr-karistirma','İki karışımı karıştırma','zor','İki karışımı karıştırma','Kaplar arası aktarımda her adımdan sonra kabın tuz miktarını ve toplamını güncelleyerek son oranı bulur.','hikâyeli',5,
 'K-KR-02 (kaplar arası gidiş-dönüş aktarım) · iki kap, iki aktarım, istenen: birinci kabın son oranı',
 'Birinci kapta tuz oranı %30 olan 200 gram, ikinci kapta tuz oranı %10 olan 300 gram tuzlu su vardır. Birinci kaptan 100 gram alınıp ikinci kaba dökülüyor ve iyice karıştırılıyor. Sonra ikinci kaptan 100 gram alınıp birinci kaba dökülüyor.\nBuna göre birinci kaptaki tuzlu suyun son tuz oranı yüzde kaçtır?',
 s,'E','Birinci kabın son tuz oranı.',
 ['İlk aktarımda ikinci kaba kaç gram tuz gider?','İkinci kabın yeni tuz oranı nedir?','Geri dökülen 100 gram bu yeni oranda tuz içerir; birinci kabın tuzunu ve toplamını güncelle.'],[ORAN,TOPLA,CEKME],
 [A('Başlangıç','Her kaptaki tuz.','1. kap: 200 × 30/100 = 60 g · 2. kap: 300 × 10/100 = 30 g'),
  A('İlk aktarım','1. kaptan alınan 100 g’da %30 tuz var.','100 × 30/100 = 30 g · 1. kap: 30 g tuz, 100 g'),
  A('İkinci kap','Gelen kısım karıştırılır.','2. kap: 30 + 30 = 60 g tuz, 400 g · 60/400 = %15'),
  A('Geri aktarım','2. kaptan alınan 100 g %15 tuzludur.','100 × 15/100 = 15 g · 1. kap: 30 + 15 = 45 g tuz, 200 g'),
  A('Son oran','Birinci kabın tuzunu toplamına böl.','45/200 = 22,5/100 = %22,5')],
 'Aktarım sorularında her dökmeden sonra o kabın “madde, toplam” ikilisini yeniden yaz; alınan kısım daima o anki oranı taşır.',
 dict(A='10, ikinci kabın başlangıç oranı; soru birinci kabı soruyor.',B='15, ikinci kabın karışımdan sonraki oranı; birinci kabın oranı değil.',
      C='18, iki kaptaki tuzlu suyun tamamen karıştığını sanmak (90/500).',D='20, geri dökülen 100 gramın oranını karışmadan önceki %10 almak.'),
 TT(A='dikkat',B='dikkat',C='bilgi',D='islem'))
a=Kap(120,300); b=Kap(60,300); b.dok(a.al(100)); assert b.oran()==25; a.dok(b.al(100)); assert a.oran()==35 and (a.m,a.t)==(105,300)
assert (40+20)/Fr(2)==30 and Fr(80+25,200)*100==Fr(105,2)
s=sirali(['25','30','35','40','52,5'])
P.K('0008','A kabında şeker oranı %40 olan 300 gram, B kabında şeker oranı %20 olan 300 gram şekerli su vardır. A kabından 100 gram alınıp B kabına ekleniyor ve karıştırılıyor. Ardından B kabından 100 gram alınıp A kabına ekleniyor.\nBuna göre A kabındaki karışımın son şeker oranı yüzde kaçtır?',
 s,'C','A kabının son şeker oranı.',
 ['A’dan alınan 100 gramda kaç gram şeker var?','B kabının yeni şeker oranını bul.','B’den A’ya giden 100 gram bu yeni oranda; A’nın şekerini ve toplamını güncelle.'],[ORAN,TOPLA,CEKME],
 [A('Başlangıç','Her kaptaki şeker.','A kabı: 300 × 40/100 = 120 gram · B kabı: 300 × 20/100 = 60 gram'),
  A('İlk aktarım','A’dan alınan 100 g’da %40 şeker var.','40 g şeker gider · A: 80 g şeker, 200 g'),
  A('B kabı','Gelenle karışır.','B: 60 + 40 = 100 g şeker, 400 g · 100/400 = %25'),
  A('Geri aktarım','B’den alınan 100 g %25 şekerli.','25 g şeker · A: 80 + 25 = 105 g şeker, 300 g'),
  A('Son oran','A’nın şekerini toplamına böl.','105/300 = 35/100 = %35')],
 'Aktarımdan sonra toplamı da güncelle: A kabına 100 g eklenince A’nın toplamı da 100 g artar.',
 dict(A='25, B kabının karışımdan sonraki oranı.',B='30, iki oranın ortalaması ya da her şeyin karıştığını sanmak.',
      D='40, A kabının oranının değişmediğini sanmak; A’ya daha az şekerli karışım eklendi.',E='52,5, geri eklenen 100 gramı A’nın toplamına katmamak (105/200).'),
 TT(A='dikkat',B='bilgi',D='bilgi',E='islem'))

P.yaz(os.path.join(H,'karisimprob-1.json'),os.path.join(H,'karisimprob-1-kardes.json'))
