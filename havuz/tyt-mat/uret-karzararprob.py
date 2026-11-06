"""Kâr Zarar Problemleri · parti 1: 8 ana + 8 kardeş. Her cevap kodla yeniden hesaplanır (assert). Fiyatlar 2026 TL."""
import sys,os,json
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,os.path.join(H,'..'))
from ortak import *
P=Parti('karzararprob','Kâr Zarar Problemleri','prob|Kar Zarar Problemleri')
UK='prob|Kar Zarar Problemleri'
TT=lambda **k:k
def sirali(s): assert s==sorted(s) and len(set(s))==5, s
def tek_dogru(s,d): assert s.count(d)==1; return 'ABCDE'[s.index(d)]
def yaz(v): return str(v).replace('.',',') if not isinstance(v,Fr) else (str(int(v)) if v.denominator==1 else str(float(v)).replace('.',','))

KARTLAR=[
 dict(id='K-KZ-01',konu='Kâr Zarar Problemleri',alt='Alış, satış, kâr',fikir='Alış fiyatı ve kâr/zarar yüzdesinden satış fiyatı ya da satış fiyatından alış fiyatı bulunur (satış = alış × (1 ± p/100)).',tuzak='Kâr yüzdesini satış fiyatına göre almak; geriye giderken yüzdeyi satış fiyatından düşmek.',zorluk='kolay',kalip='hikâyeli',adim=2,tipId='kz-temel',tip='Alış, satış ve kâr yüzdesi',kaynak='Bilgi Sarmal (180 TL’ye alınan ürün) · 345 SB'),
 dict(id='K-KZ-02',konu='Kâr Zarar Problemleri',alt='Adet ve fiyat',fikir='Alınan ürünlerin bir kısmı satılamaz ya da adetler farklıdır; toplam alış ve toplam satış tutarı karşılaştırılarak kâr yüzdesi bulunur.',tuzak='Satılamayan ürünlerin maliyetini unutmak; kârı satış tutarına bölmek.',zorluk='orta',kalip='hikâyeli',adim=3,tipId='kz-adet',tip='Adet-fiyat ilişkisiyle kâr',kaynak='345 SB (5’inin alışı, 6’sının satışı) · 3D'),
 dict(id='K-KZ-03',konu='Kâr Zarar Problemleri',alt='Etiket ve indirim',fikir='Etiket fiyatı üzerinden indirimle satışta kâr ya da zarar edilir; alış = 100 alınıp etiket ile alış arasındaki oran bulunur.',tuzak='İndirim ve kâr yüzdelerini toplamak/çıkarmak; indirimi indirimli fiyatın yüzdesi sanmak.',zorluk='orta',kalip='hikâyeli',adim=3,tipId='kz-etiket',tip='Etiket fiyatı, indirim ve kâr',kaynak='Bilgi Sarmal (%20 indirimle %8 kâr) · Mert Hoca (kampanya broşürü)'),
 dict(id='K-KZ-04',konu='Kâr Zarar Problemleri',alt='Etiket, iki indirim, kâr',fikir='Etiket alışın belli bir yüzde fazlasıdır; art arda iki indirimden sonra kalan kâr verilir, ikinci indirim bulunur.',tuzak='İkinci indirimi etiket ya da alış fiyatına oranlamak; yüzdeleri toplayıp çıkarmak.',zorluk='zor',kalip='hikâyeli',adim=4,tipId='kz-etiket',tip='Etiket fiyatı, indirim ve kâr',kaynak='345 SB, Bilgi Sarmal (etiket kârı ve indirim zinciri)'),
 dict(id='K-KZ-05',konu='Kâr Zarar Problemleri',alt='Ardışık indirim',fikir='İkinci indirim indirimli fiyat üzerinden yapılır; son ödenen fiyattan bilinmeyen ilk ya da ikinci indirim oranı bulunur.',tuzak='İndirim yüzdelerini toplamak; indirimi yanlış fiyata oranlamak.',zorluk='orta',kalip='hikâyeli',adim=3,tipId='kz-ardisik-indirim',tip='Art arda indirimler',kaynak='345 SB (ilk indirimden sonra %16 daha) · ÖSYM 2018 (kampanyalı kalem)'),
 dict(id='K-KZ-06',konu='Kâr Zarar Problemleri',alt='Kampanya karşılaştırma',fikir='İki satıcının farklı kampanyaları (ikincisi yarı fiyatına, n al m öde, yüzde indirim) aynı alışveriş için hesaplanıp karşılaştırılır.',tuzak='Kampanyayı tüm ürünlere ya da tek ürüne uygulamak; yüzde indirimi TL sanmak.',zorluk='orta',kalip='hikâyeli',adim=3,tipId='kz-kampanya',tip='Kampanya karşılaştırma',kaynak='ÖSYM 2018 (ikincisi %50 indirimli kalem), ÖSYM 2021 (iki kırtasiyenin kampanyası)'),
 dict(id='K-KZ-07',konu='Kâr Zarar Problemleri',alt='Parça parça satış',fikir='Malın bir kısmı satılamaz, kalanın bir kısmı belli kârla satılır; toplam hedef kâr için kalan kısmın satış fiyatı bulunur.',tuzak='Hedef kâr oranını kalan kısma uygulamak; satılamayanların maliyetini unutmak; ortalama fiyatı almak.',zorluk='zor',kalip='hikâyeli',adim=5,tipId='kz-parca-satis',tip='Malın parça parça satışı',kaynak='Bilgi Sarmal (üç ürün farklı kâr/zarar) · 3D (bozulan meyve)'),
]
TIPLER={}
for k in KARTLAR: TIPLER.setdefault(k['tipId'],dict(tipId=k['tipId'],ad=k['tip'],kartlar=[],uygulamaKonu=UK))['kartlar'].append(k['id'])
json.dump(dict(konu='Kâr Zarar Problemleri',surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026, Bilgi Sarmal, 3D, Mert Hoca, 345 SB.',kartlar=KARTLAR,tipler=list(TIPLER.values())),
          open(os.path.join(H,'..','kartlar','karzararprob.json'),'w'),ensure_ascii=False,indent=1)
T={t:TIPLER[t]['ad'] for t in TIPLER}

KY=B('Kâr yüzdesi','aksi söylenmedikçe kâr ve zarar yüzdesi alış (maliyet) fiyatına göre hesaplanır. Örnek: 200 TL’ye alınıp %10 kârla satılan ürünün kârı 20 TL, satışı 220 TL’dir')
SAT=B('Satış fiyatı','kârda satış = alış × (1 + p/100) · zararda satış = alış × (1 − p/100). Örnek: 500 TL’lik ürün %20 zararla 400 TL’ye satılır')
IND=B('İndirim','indirim yüzdesi, indirimin yapıldığı fiyata göredir. Örnek: 800 TL’lik etikete %25 indirim ⇒ 800 × 0,75 = 600 TL')
ARD=B('Art arda indirim','ikinci indirim, ilk indirimden sonraki fiyat üzerinden yapılır. Örnek: 1000 TL’ye önce %20, sonra %10 indirim ⇒ 1000 × 0,8 × 0,9 = 720 TL')

# ===== 0001 temel KOLAY
a=360; sat=a*Fr(125,100); assert sat==450 and 6*(sat-a)==540
S_=Fr(a)/Fr(75,100); assert S_==480 and 6*(S_-a)==720
s=[90,450,540,720,2700]; sirali(s); assert 6*450==2700
P.R('0001','kz-temel',T['kz-temel'],'kolay','Alış, satış, kâr','Alış fiyatı ve kâr yüzdesinden bir üründeki kârı bulur; birden çok ürün için toplam kârı hesaplar.','hikâyeli',2,
 'K-KZ-01 (alış + kâr yüzdesi) · yeni kurgu (kitapçı), yeni istenen (toplam kâr)',
 'Bir kitapçı tanesini 360 TL’ye aldığı bir romanı %25 kârla satmaktadır.\nBuna göre kitapçı bu romandan 6 tane sattığında toplam kaç TL kâr eder?',
 [str(v) for v in s],tek_dogru(s,540),'6 romanın satışından elde edilen toplam kâr.',
 ['Kâr yüzdesi hangi fiyata göre hesaplanır?','Bir romandan kaç TL kâr edilir?','Bir romanın kârını satılan roman sayısıyla çarp.'],[KY,SAT],
 [A('Bir romanın kârı','Kâr alış fiyatının %25’i.','360 × 0,25 = 90 TL'),
  A('Toplam kâr','6 romanın her birinden 90 TL kâr edilir.','6 × 90 = 540 TL'),
  A('Kontrol','Satış fiyatı ile alış fiyatı arasındaki fark.','satış: 360 + 90 = 450 TL · 6 × (450 − 360) = 540 ✓')],
 'Kâr yüzdesi aksi söylenmedikçe alış fiyatına göredir; önce bir üründeki kârı bul, sonra adetle çarp.',
 dict(A='90, bir romandan elde edilen kâr; 6 roman satılmış.',B='450, bir romanın satış fiyatı; soru toplam kârı soruyor.',D='720: kârı satış fiyatının %25’i sanmak (satış 480, kâr 120 TL). Kâr yüzdesi alış fiyatına göredir.',E='2700, 6 romanın toplam satış tutarı; kâr değil.'),
 TT(A='dikkat',B='dikkat',D='bilgi',E='dikkat'))
a=60; sat=a*Fr(12,10); assert sat==72 and 20*sat==1440
s=[72,240,1200,1440,1500]; sirali(s); assert 20*(sat-a)==240 and 20*a==1200 and 20*(Fr(a)/Fr(8,10))==1500
P.K('0001','Bir manav kilogramını 60 TL’ye aldığı domatesleri %20 kârla satmaktadır.\nManav 20 kilogram domatesin tamamını sattığında kaç TL tahsil eder?',
 [str(v) for v in s],tek_dogru(s,1440),'20 kg domatesin satışından tahsil edilen para.',
 ['Bir kilogram domatesin satış fiyatı kaç TL?','Kâr yüzdesi alış fiyatına göre hesaplanır.','Satış fiyatını kilogram sayısıyla çarp.'],[KY,SAT],
 [A('Satış fiyatı','Alış fiyatına %20 kâr eklenir.','60 × 1,2 = 72 TL'),
  A('Tahsil edilen','20 kilogramın satış tutarı.','20 × 72 = 1440 TL'),
  A('Kontrol','Alış tutarı ile kârın toplamı.','20 × 60 = 1200 · 1200 × 0,2 = 240 · 1200 + 240 = 1440 ✓')],
 'Satış = alış × (1 + kâr oranı); toplam tutar için birim satış fiyatını miktarla çarp.',
 dict(A='72, bir kilogramın satış fiyatı; 20 kg satılmış.',B='240, toplam kâr; soru tahsil edilen toplam parayı soruyor.',C='1200, 20 kg domatesin alış tutarı; kâr eklenmemiş.',E='1500: kârı satış fiyatının %20’si sanmak (1 kg 75 TL). Kâr alış fiyatına göredir.'),
 TT(A='dikkat',B='dikkat',C='dikkat',E='bilgi'))

# ===== 0002 temel (geriye) KOLAY
x=Fr(1170)/Fr(13,10); assert x==900 and x*Fr(3,10)==270
s=[270,351,819,900,1521]; sirali(s); assert 1170*Fr(3,10)==351 and 1170*Fr(7,10)==819 and 1170*Fr(13,10)==1521
P.R('0002','kz-temel',T['kz-temel'],'kolay','Alış, satış, kâr','Satış fiyatı ve kâr yüzdesinden alış fiyatını bulur.','hikâyeli',2,
 'K-KZ-01 (satıştan alışa geri dönüş) · yeni kurgu (kulaklık), yeni istenen (alış fiyatı)',
 'Bir elektronik mağazası kablosuz kulaklığı %30 kârla 1170 TL’ye satmaktadır.\nBuna göre mağazanın bu kulaklığın alış fiyatı kaç TL’dir?',
 [str(v) for v in s],tek_dogru(s,900),'Kulaklığın alış fiyatı.',
 ['Alış fiyatına x de; %30 kârla satış fiyatı x’in kaç katıdır?','Satış fiyatı alışın %130’u.','Bulduğun alışa %30 ekleyerek 1170’i elde edip etmediğini kontrol et.'],[KY,SAT],
 [A('Denklemi kur','Alış x olsun; satış alışın %130’u.','x × 1,3 = 1170'),
  A('Çöz','Her iki tarafı 1,3’e böl.','x = 1170 ÷ 1,3 = 900 TL'),
  A('Kontrol','Kârı bulup alışa ekle.','900 × 0,3 = 270 · 900 + 270 = 1170 ✓')],
 'Satış fiyatından alışa dönerken yüzdeyi satış fiyatından düşme; satış fiyatını (1 + kâr oranı) değerine böl.',
 dict(A='270, kulaklıktan elde edilen kâr; soru alış fiyatını soruyor.',B='351 = 1170’in %30’u; kârı satış fiyatının yüzdesi gibi hesaplamak.',C='819 = 1170 × 0,7; kârı satış fiyatından yüzde olarak düşmek. Satış, alışın %130’udur.',E='1521 = 1170 × 1,3; kârı bir kez daha eklemek.'),
 TT(A='dikkat',B='bilgi',C='bilgi',E='dikkat'),
 kisa='Satış %130 ise %10’u 1170 ÷ 13 = 90 TL; alış (%100) = 90 × 10 = 900 TL.')
x=Fr(6800)/Fr(85,100); assert x==8000 and x-6800==1200
s=[1020,1200,5780,7820,8000]; sirali(s); assert 6800*Fr(15,100)==1020 and 6800*Fr(85,100)==5780 and 6800*Fr(115,100)==7820
P.K('0002','Ayşe iki yıl önce aldığı bisikletini %15 zararla 6800 TL’ye satmıştır.\nBuna göre Ayşe bu bisikleti kaç TL’ye almıştır?',
 [str(v) for v in s],tek_dogru(s,8000),'Bisikletin alış fiyatı.',
 ['Zarar yüzdesi hangi fiyata göredir?','%15 zararla satılan bir ürünün satış fiyatı alışın yüzde kaçıdır?','Bulduğun alıştan %15 düşerek 6800’ü kontrol et.'],[KY,SAT],
 [A('Denklemi kur','Alış x olsun; %15 zararda satış alışın %85’i.','x × 0,85 = 6800'),
  A('Çöz','Her iki tarafı 0,85’e böl.','x = 6800 ÷ 0,85 = 8000 TL'),
  A('Kontrol','Zararı bulup alıştan çıkar.','8000 × 0,15 = 1200 · 8000 − 1200 = 6800 ✓')],
 'Zararlı satışta satış fiyatı alışın (100 − zarar)%’sidir; alışı bulmak için satış fiyatını bu orana böl.',
 dict(A='1020 = 6800’ün %15’i; zararı satış fiyatına göre hesaplamak.',B='1200, zarar miktarı; soru alış fiyatını soruyor.',C='5780 = 6800 × 0,85; zararı bir kez daha düşmek.',D='7820 = 6800 × 1,15; zararı satış fiyatının %15’i kadar geri eklemek. Satış, alışın %85’idir.'),
 TT(A='bilgi',B='dikkat',C='dikkat',D='bilgi'),
 kisa='Satış %85 ise %5’i 6800 ÷ 17 = 400 TL; alış (%100) = 400 × 20 = 8000 TL.')

# ===== 0003 adet-fiyat ORTA
alis=6*40; satis=5*60; k=Fr(satis-alis,alis)*100; assert k==25
s=[20,25,50,60,125]; sirali(s); assert Fr(satis-alis,satis)*100==20 and Fr(60-40,40)*100==50 and satis-alis==60 and Fr(satis,alis)*100==125
P.R('0003','kz-adet',T['kz-adet'],'orta','Adet ve fiyat','Satılamayan ürünlerin maliyetini de katarak toplam alış ile toplam satış tutarını karşılaştırır ve kâr yüzdesini bulur.','hikâyeli',3,
 'K-KZ-02 (alınan ve satılan adetler farklı) · yeni kurgu (kafede ayran), yeni istenen (kâr yüzdesi)',
 'Bir kafe tanesini 40 TL’ye aldığı ayranları tanesi 60 TL’den satmaktadır. Kafenin aldığı her 6 ayrandan 1’i son kullanma tarihi geçtiği için satılamamakta ve atılmaktadır.\nKâr yüzdesi satın alınan tüm ayranların maliyetine göre hesaplandığına göre kafe bu satıştan yüzde kaç kâr etmektedir?',
 [str(v) for v in s],tek_dogru(s,25),'Tüm maliyete göre kâr yüzdesi.',
 ['6 ayranlık bir grup düşün: alış tutarı kaç TL?','Bu gruptan kaç ayran satılır ve kaç TL gelir elde edilir?','Kârı satış tutarına değil, alış tutarına böl.'],[KY,B('Satılamayan ürün','atılan ürünün parası da ödenmiştir; maliyete katılır ama satış tutarına girmez')],
 [A('6 ayranlık grup','Altısı da satın alınır.','alış: 6 × 40 = 240 TL'),
  A('Satış tutarı','Biri atılır, beşi satılır.','satış: 5 × 60 = 300 TL'),
  A('Kâr yüzdesi','Kârı alış tutarına böl.','300 − 240 = 60 TL · 60 ÷ 240 = 0,25 ⇒ %25')],
 'Satılamayan ürünlerin maliyeti kâr hesabında kaybolmaz; toplam alış ile toplam satışı karşılaştır.',
 dict(A='20 = 60 ÷ 300; kârı satış tutarına bölmek. Kâr yüzdesi alış tutarına göredir.',C='50, atılan ayranları unutmak: 40 TL’ye alınıp 60 TL’ye satılan tek ayranın kârı.',D='60, 6 ayranlık grupta elde edilen kâr (TL); soru yüzdeyi soruyor.',E='125, satış tutarının alış tutarına oranı (300 ÷ 240); kâr bunun 100’den fazlası.'),
 TT(A='bilgi',C='dikkat',D='dikkat',E='dikkat'))
alis=100*10; satis=80*25; k=Fr(satis-alis,alis)*100; assert k==100
s=[50,100,120,150,200]; sirali(s); assert Fr(satis-alis,satis)*100==50 and Fr(80*(25-10),alis)*100==120 and Fr(25-10,10)*100==150 and Fr(satis,alis)*100==200
P.K('0003','Bir fırın simidin tanesini 10 TL’ye mal etmektedir. Fırının her gün çıkardığı simitlerin %20’si satılamayıp bağışlanmakta, diğerleri tanesi 25 TL’den satılmaktadır.\nKâr yüzdesi üretilen tüm simitlerin maliyetine göre hesaplandığına göre fırın simitlerden yüzde kaç kâr etmektedir?',
 [str(v) for v in s],tek_dogru(s,100),'Tüm maliyete göre kâr yüzdesi.',
 ['Simit sayısını 10 al: maliyet kaç TL?','Bu 10 simidin kaçı satılır ve kaç TL gelir elde edilir?','Kârı toplam maliyete böl.'],[KY,B('Satılamayan ürün','bağışlanan ürünün de maliyeti vardır; maliyete katılır ama satış tutarına girmez')],
 [A('100 simit','Hepsinin maliyeti ödenir.','maliyet: 100 × 10 = 1000 TL'),
  A('Satış','%20’si bağışlanır, 80 simit satılır.','80 × 25 = 2000 TL'),
  A('Kâr yüzdesi','Kârı toplam maliyete böl.','2000 − 1000 = 1000 · 1000 ÷ 1000 = 1 ⇒ %100')],
 'Satılamayan ürünler maliyeti artırır, geliri artırmaz; kâr yüzdesini tüm maliyete göre hesapla.',
 dict(A='50 = 1000 ÷ 2000; kârı satış tutarına bölmek.',C='120: kârı satılan simitler üzerinden (80 × 15 = 1200) hesaplamak; bağışlanan 20 simidin 200 TL maliyetini unutmuşsun.',D='150, bağışlanan simitleri hiç hesaba katmamak (10 TL’den 25 TL’ye tek simidin kârı).',E='200, satış tutarının maliyete oranı; kâr bunun 100’den fazlası.'),
 TT(A='bilgi',C='dikkat',D='dikkat',E='dikkat'))

# ===== 0004 etiket ORTA
et=2400*Fr(105,100)/Fr(75,100); assert et==3360 and et*Fr(75,100)==2520
s=[2520,3000,3120,3150,3360]; sirali(s); assert 2400*Fr(125,100)==3000 and 2400*Fr(13,10)==3120 and 2520*Fr(125,100)==3150
P.R('0004','kz-etiket',T['kz-etiket'],'orta','Etiket ve indirim','İndirimli satıştaki kârdan satış fiyatını, sonra indirim oranından etiket fiyatını bulur.','hikâyeli',3,
 'K-KZ-03 (indirimli satışta kâr) · yeni kurgu (mont), yeni istenen (etiket fiyatı TL)',
 'Bir mağaza alış fiyatı 2400 TL olan bir montu, etiket fiyatı üzerinden %25 indirim yaparak satmıştır.\nMağaza bu satıştan %5 kâr ettiğine göre montun etiket fiyatı kaç TL’dir?',
 [str(v) for v in s],tek_dogru(s,3360),'Montun etiket fiyatı.',
 ['Önce montun kaç TL’ye satıldığını bul: alışa %5 kâr ekle.','%25 indirimden sonra etiket fiyatının yüzde kaçı ödenir?','Satış fiyatını bu orana bölerek etiket fiyatına dön.'],[KY,IND],
 [A('Satış fiyatı','%5 kâr alış fiyatına göre.','2400 × 1,05 = 2520 TL'),
  A('Etiketle ilişki','%25 indirimde etiketin %75’i ödenir.','etiket × 0,75 = 2520'),
  A('Etiket fiyatı','0,75’e böl.','2520 ÷ 0,75 = 3360 TL'),
  A('Kontrol','Etiketten %25 düş.','3360 × 0,75 = 2520 ✓ · 2520 − 2400 = 120 = 2400’ün %5’i ✓')],
 'İndirim etiketin, kâr alışın yüzdesidir; iki yüzde farklı fiyatlara ait olduğu için toplanmaz.',
 dict(A='2520, montun indirimli satış fiyatı; soru etiket fiyatını soruyor.',B='3000 = 2400 × 1,25; kârı unutup yalnız indirimi geri eklemek.',C='3120 = 2400 × 1,30; indirim ve kâr yüzdelerini toplamak.',D='3150 = 2520 × 1,25; indirimi indirimli fiyatın yüzdesi sanmak. %25, etiket fiyatının yüzdesidir.'),
 TT(A='dikkat',B='dikkat',C='bilgi',D='bilgi'))
et=Fr(90)/Fr(60,100); assert et==150 and et-100==50
s=[26,30,40,50,60]; sirali(s); assert 90*Fr(14,10)==126
P.K('0004','Bir spor mağazası sezon sonunda bir ayakkabıyı etiket fiyatı üzerinden %40 indirimle satmış ve bu satıştan %10 zarar etmiştir.\nBuna göre mağaza bu ayakkabıyı etiket fiyatından satsaydı yüzde kaç kâr ederdi?',
 [str(v) for v in s],tek_dogru(s,50),'Etiket fiyatından satıştaki kâr yüzdesi.',
 ['Alış fiyatını 100 TL al; %10 zararla satış kaç TL?','Bu fiyat etiketin %60’ıdır; etiket kaç TL?','Etiket ile alış arasındaki farkı alışa oranla.'],[KY,IND],
 [A('Alışı 100 al','%10 zararla satış.','100 × 0,9 = 90 TL'),
  A('Etiket fiyatı','%40 indirimle etiketin %60’ı ödenir.','etiket × 0,6 = 90 ⇒ etiket = 150 TL'),
  A('Kâr yüzdesi','Etiket fiyatından satışta kâr.','150 − 100 = 50 ⇒ %50')],
 'Alışı 100 almak; indirim, kâr ve zararı aynı ölçekte görmeyi sağlar.',
 dict(A='26: etiketi indirimli fiyatın %140’ı sanmak (90 × 1,4 = 126). İndirim etiket fiyatının yüzdesidir.',B='30 = 40 − 10; yüzdeleri çıkarmak. Yüzdeler farklı fiyatlara göredir.',C='40, indirim yüzdesi; soru etiketten satıştaki kârı soruyor.',E='60, indirimli fiyatın etikete oranı (%60); kâr yüzdesi değil.'),
 TT(A='bilgi',B='bilgi',C='dikkat',E='dikkat'))

# ===== 0005 ardışık indirim ORTA
ilk=Fr(2520)/Fr(9,10); assert ilk==2800; p=Fr(3500-ilk,3500)*100; assert p==20
s=[18,20,25,28,38]; sirali(s); assert Fr(3500-2520-350,3500)*100==18 and Fr(700,2800)*100==25 and Fr(3500-2520,3500)*100==28
P.R('0005','kz-ardisik-indirim',T['kz-ardisik-indirim'],'orta','Ardışık indirim','Son ödenen fiyattan ikinci indirimi geri alarak ilk indirimli fiyatı, oradan da ilk indirim oranını bulur.','hikâyeli',3,
 'K-KZ-05 (ikinci indirim indirimli fiyattan) · yeni kurgu (üyelik kartı), yeni istenen (ilk indirim oranı)',
 'Bir elektronik mağazasında etiket fiyatı 3500 TL olan bir kulaklık indirime girmiştir. Mağaza, üyelik kartı olan müşterilerine kasada indirimli fiyat üzerinden ayrıca %10 indirim yapmaktadır.\nÜyelik kartı olan Deniz bu kulaklık için 2520 TL ödediğine göre kulaklığa yapılan ilk indirim yüzde kaçtır?',
 [str(v) for v in s],tek_dogru(s,20),'İlk indirimin yüzdesi.',
 ['Kasadaki %10 indirim hangi fiyat üzerinden yapıldı?','2520 TL, indirimli fiyatın %90’ı.','İndirimli fiyat ile etiket fiyatı arasındaki farkı etiket fiyatına oranla.'],[IND,ARD],
 [A('Kasa indiriminden önce','2520 TL, indirimli fiyatın %90’ı.','indirimli × 0,9 = 2520 ⇒ indirimli = 2800 TL'),
  A('İlk indirim tutarı','Etiketten indirimli fiyata düşüş.','3500 − 2800 = 700 TL'),
  A('İlk indirim oranı','İlk indirim etiket fiyatına göre.','700 ÷ 3500 = 0,2 ⇒ %20')],
 'Art arda indirimlerde sondan başa dönerken her indirimi kendi uygulandığı fiyata göre geri al.',
 dict(A='18: kasadaki %10’u etiket fiyatından (350 TL) hesaplamak. İkinci indirim indirimli fiyatın yüzdesidir.',C='25 = 700 ÷ 2800; ilk indirimi indirimli fiyata oranlamak. İlk indirim etiket fiyatına göredir.',D='28, etiket fiyatına göre toplam indirim; soru yalnız ilk indirimi soruyor.',E='38 = 28 + 10; toplam indirime kasa indirimini eklemek. İkinci indirim zaten 28’in içinde.'),
 TT(A='bilgi',C='islem',D='dikkat',E='islem'))
ara=2400*Fr(75,100); assert ara==1800; q=Fr(ara-1440,ara)*100; assert q==20
s=[20,25,40,60,75]; sirali(s); assert Fr(360,1440)*100==25 and Fr(2400-1440,2400)*100==40 and Fr(1440,2400)*100==60
P.K('0005','Etiket fiyatı 2400 TL olan bir sırt çantası önce %25 indirime girmiştir. Bir süre sonra mağaza, indirimli fiyat üzerinden ikinci bir indirim daha yapmış ve çantanın son fiyatı 1440 TL olmuştur.\nBuna göre ikinci indirim yüzde kaçtır?',
 [str(v) for v in s],tek_dogru(s,20),'İkinci indirimin yüzdesi.',
 ['İlk indirimden sonra çanta kaç TL oldu?','İkinci indirim kaç TL?','İkinci indirimi, uygulandığı fiyata (ilk indirimli fiyata) oranla.'],[IND,ARD],
 [A('İlk indirim','%25 indirimde etiketin %75’i kalır.','2400 × 0,75 = 1800 TL'),
  A('İkinci indirim tutarı','1800 TL’den 1440 TL’ye düşüş.','1800 − 1440 = 360 TL'),
  A('Oran','360 TL, 1800 TL’nin yüzde kaçı?','360 ÷ 1800 = 0,2 ⇒ %20')],
 'Her indirimin yüzdesini, o indirimin uygulandığı fiyata göre hesapla.',
 dict(B='25 = 360 ÷ 1440; indirim tutarını son fiyata bölmek. İkinci indirim 1800 TL’nin yüzdesidir.',C='40, etiket fiyatına göre toplam indirim; soru ikinci indirimi soruyor.',D='60, son fiyatın etiket fiyatına oranı (1440 ÷ 2400).',E='75, ilk indirimden sonra kalan oran (%75); ikinci indirim değil.'),
 TT(B='islem',C='dikkat',D='dikkat',E='dikkat'))

# ===== 0006 kampanya ORTA
A_=2*(120+60); B_=4*120*Fr(8,10); assert A_==360 and B_==384 and B_-A_==24
s=[24,36,40,60,144]; sirali(s); assert (3*120+60)-B_==36 and 4*100-A_==40 and B_-4*60==144
P.R('0006','kz-kampanya',T['kz-kampanya'],'orta','Kampanya karşılaştırma','İki farklı kampanyada aynı alışverişin tutarını hesaplar ve aradaki farkı bulur.','hikâyeli',3,
 'K-KZ-06 (ikincisi yarı fiyatına ↔ yüzde indirim) · yeni kurgu (iki kırtasiye, defter), yeni istenen (tutar farkı)',
 'Etiket fiyatı 120 TL olan bir defter iki farklı kırtasiyede satılmaktadır.\nK kırtasiyesinde alınan defterler ikişerli gruplanır ve her gruptaki defterlerden biri yarı fiyatına satılır.\nL kırtasiyesinde ise tüm defterler etiket fiyatı üzerinden %20 indirimlidir.\nBu defterden 4 tane alacak olan Selin, ucuz olan kırtasiyeyi seçerse diğerine göre kaç TL daha az öder?',
 [str(v) for v in s],tek_dogru(s,24),'İki kırtasiyedeki tutarların farkı.',
 ['K kırtasiyesinde 4 defter kaç gruba ayrılır?','L kırtasiyesinde bir defter kaç TL?','İki toplam tutarı bulup farkını al.'],[IND,B('Yarı fiyatına','“yarı fiyatına” = %50 indirim. Örnek: 90 TL’lik ürün yarı fiyatına 45 TL')],
 [A('K kırtasiyesi','4 defter 2 grup; her grupta biri tam, biri yarı fiyat.','bir grup: 120 + 60 = 180 · 2 × 180 = 360 TL'),
  A('L kırtasiyesi','Her defter %20 indirimli.','120 × 0,8 = 96 · 4 × 96 = 384 TL'),
  A('Fark','K daha ucuz.','384 − 360 = 24 TL')],
 'Kampanyaları karşılaştırırken aynı alışverişin iki tutarını ayrı ayrı hesapla; “ikincisi yarı fiyatına” %25 indirime denktir.',
 dict(B='36: K’da yalnız bir defteri yarı fiyatına hesaplamak (420 TL). Her iki defterden biri indirimli.',C='40: %20 indirimi defter başına 20 TL sanmak (L’de 400 TL).',D='60, K’da bir gruptaki indirim tutarı; toplam farkı vermez.',E='144: K’da dört defterin hepsini yarı fiyatına hesaplamak (240 TL).'),
 TT(B='dikkat',C='bilgi',D='dikkat',E='dikkat'),
 kisa='“İkincisi yarı fiyatına” %25 indirim demektir: %25 − %20 = %5 fark · 4 × 120 × 0,05 = 24 TL.')
A_=9*30; B_=12*30*Fr(8,10); assert A_==270 and B_==288 and B_-A_==18
s=[12,18,42,72,90]; sirali(s); assert 10*30-B_==12 and 11*30-B_==42 and 12*6==72 and 3*30==90
P.K('0006','Bir pastanede poğaçanın tanesi 30 TL’dir ve alınan her 4 poğaçadan 1’i için ücret alınmamaktadır.\nAynı poğaçayı aynı fiyattan satan başka bir pastane ise tüm poğaçalarda %20 indirim yapmaktadır.\nBuna göre 12 poğaça almak isteyen biri ucuz olan pastaneden alırsa kaç TL daha az öder?',
 [str(v) for v in s],tek_dogru(s,18),'İki pastanedeki tutarların farkı.',
 ['12 poğaçada kaç tane 4’lü grup var; kaç poğaça ücretsiz?','İndirimli pastanede bir poğaça kaç TL?','İki toplamı karşılaştır.'],[IND,B('Ücretsiz ürün','her 4 üründen 1’i ücretsizse 4 ürüne 3 ürünün parası ödenir. Örnek: 8 ürün ⇒ 6 ürün ödenir')],
 [A('Birinci pastane','12 poğaçada 3 grup; 3 poğaça ücretsiz.','12 − 3 = 9 · 9 × 30 = 270 TL'),
  A('İkinci pastane','Her poğaça %20 indirimli.','30 × 0,8 = 24 · 12 × 24 = 288 TL'),
  A('Fark','Birinci pastane daha ucuz.','288 − 270 = 18 TL')],
 'n üründe 1 ücretsiz kampanyası 1/n oranında indirimdir; yüzde indirimle karşılaştırmak için toplamları ayrı hesapla.',
 dict(A='12: ücretsiz poğaçaları 2 saymak (300 TL). 12 poğaçada 3 tane 4’lü grup var.',C='42: yalnız 1 poğaçayı ücretsiz saymak (330 TL); her 4 poğaçada biri ücretsiz.',D='72, ikinci pastanedeki toplam indirim tutarı (12 × 6); fark değil.',E='90, birinci pastanedeki toplam indirim tutarı (3 × 30); fark değil.'),
 TT(A='islem',C='dikkat',D='dikkat',E='dikkat'))

# ===== 0007 parça satış ZOR
a,m=40,200; sat=Fr(m*90,100); m1=sat/2; m2=sat-m1; f1=a*Fr(125,100); hed=a*m*Fr(135,100)
p=(hed-m1*f1)/m2; assert (sat,m1,f1,hed,p)==(180,90,50,10800,70)
e1=a*Fr(135,100); e2=(sat*a*Fr(135,100)-m1*f1)/m2; e3=(hed-m1*f1)/100; e4=hed/sat; assert (e1,e2,e3,e4)==(54,58,63,60)
s=[54,58,60,63,70]; sirali(s); assert m1*f1+m2*p==hed
P.R('0007','kz-parca-satis',T['kz-parca-satis'],'zor','Parça parça satış','Satılamayan kısmın maliyetini de katarak hedef toplam kâra göre kalan malın birim satış fiyatını bulur.','hikâyeli',5,
 'K-KZ-07 (satılamayan kısım + farklı kârla satış, hedef toplam kâr) · yeni kurgu (manavda domates), yeni istenen (kalanın kilogram fiyatı)',
 'Bir manav kilogramını 40 TL’den 200 kilogram domates almıştır. Domateslerin %10’u ezildiği için satılamamıştır.\nManav satılabilir domateslerin yarısını %25 kârla satmıştır.\nManavın domateslere ödediği paranın tamamına göre %35 kâr etmesi için kalan domatesleri kilogramı kaç TL’den satması gerekir?',
 [str(v) for v in s],tek_dogru(s,70),'Kalan domateslerin kilogram satış fiyatı.',
 ['Manavın toplam maliyeti ve %35 kârla elde etmesi gereken toplam satış tutarı kaç TL?','Kaç kilogram domates satılabilir; yarısı kaç kilogram ve kaç TL’den satıldı?','Kalan tutarı kalan kilograma böl.'],[KY,B('Hedef satış tutarı','tüm maliyete göre %35 kâr ⇒ toplam satış tutarı = maliyet × 1,35. Satılamayan malın parası da maliyete dahildir')],
 [A('Maliyet ve hedef','Ezilen domateslerin parası da ödendi.','200 × 40 = 8000 TL · 8000 × 1,35 = 10800 TL'),
  A('Satılabilir miktar','%10 ezik.','200 × 0,9 = 180 kg · yarısı 90 kg'),
  A('İlk satış','90 kg, %25 kârla.','40 × 1,25 = 50 TL · 90 × 50 = 4500 TL'),
  A('Kalan tutar','Hedefe ulaşmak için gereken.','10800 − 4500 = 6300 TL'),
  A('Kilogram fiyatı','Kalan 90 kg.','6300 ÷ 90 = 70 TL')],
 'Hedef kâr sorularında önce “toplam kaç TL tahsil edilmeli?” sorusunu cevapla; satılamayan malın maliyetini unutma.',
 dict(A='54 = 40 × 1,35; hedef kâr oranını kalan kısma uygulamak. İlk yarı daha az kârla satıldı, ezilenler hiç satılmadı.',B='58: hedefi yalnız satılan 180 kg’ın maliyetine göre kurmak; ezilen domateslerin parası da ödendi.',C='60 = 10800 ÷ 180; ortalama satış fiyatını kalan kısmın fiyatı sanmak. İlk yarı 50 TL’den satıldı.',D='63: kalan miktarı 100 kg almak; satılabilir domates 180 kg, kalan yarısı 90 kg.'),
 TT(A='bilgi',B='dikkat',C='bilgi',D='islem'))
a,m=60,240; sat=Fr(m*75,100); m1=sat/2; m2=sat-m1; f1=a*Fr(140,100); hed=a*m*Fr(110,100)
p=(hed-m1*f1)/m2; assert (sat,m1,f1,hed,p)==(180,90,84,15840,92)
e1=a*Fr(110,100); e2=(sat*a*Fr(110,100)-m1*f1)/m2; e3=(hed-m1*f1)/120; e4=hed/sat; assert (e1,e2,e3,e4)==(66,48,69,88)
s=[48,66,69,88,92]; sirali(s)
P.K('0007','Bir kırtasiyeci tanesi 60 TL’den 240 defter almıştır. Depodaki nem nedeniyle defterlerin %25’i hasar görmüş ve satılamamıştır.\nKırtasiyeci sağlam defterlerin yarısını tanesi %40 kârla satmıştır.\nKırtasiyecinin defterlere ödediği paranın tamamına göre %10 kâr etmesi için kalan sağlam defterlerin tanesini kaç TL’den satması gerekir?',
 [str(v) for v in s],tek_dogru(s,92),'Kalan sağlam defterlerin tane fiyatı.',
 ['Toplam maliyet kaç TL ve %10 kâr için toplam kaç TL tahsil edilmeli?','Kaç defter sağlam; yarısından kaç TL elde edildi?','Kalan tutarı kalan defter sayısına böl.'],[KY,B('Hedef satış tutarı','tüm maliyete göre %10 kâr ⇒ toplam satış tutarı = maliyet × 1,1. Hasarlı malın parası da maliyete dahildir')],
 [A('Maliyet ve hedef','Hasarlı defterlerin parası da ödendi.','240 × 60 = 14400 TL · 14400 × 1,1 = 15840 TL'),
  A('Sağlam defterler','%25 hasarlı.','240 × 0,75 = 180 · yarısı 90 defter'),
  A('İlk satış','90 defter, %40 kârla.','60 × 1,4 = 84 TL · 90 × 84 = 7560 TL'),
  A('Kalan tutar','Hedefe ulaşmak için.','15840 − 7560 = 8280 TL'),
  A('Tane fiyatı','Kalan 90 defter.','8280 ÷ 90 = 92 TL')],
 'Toplam kâr hedefini önce TL’ye çevir; satılan kısımların gelirini düş, kalanı kalan adede böl.',
 dict(A='48: hedefi yalnız 180 sağlam defterin maliyetine göre kurmak; hasarlı defterlerin parası da ödendi.',B='66 = 60 × 1,1; hedef kâr oranını kalan defterlere uygulamak. Hasarlılar hiç satılmadı.',C='69: kalan defter sayısını 120 almak; sağlam defter 180, kalan yarısı 90.',D='88 = 15840 ÷ 180; ortalama satış fiyatını kalan defterlerin fiyatı sanmak.'),
 TT(A='dikkat',B='bilgi',C='islem',D='bilgi'))

# ===== 0008 etiket + iki indirim ZOR
et=2500*Fr(16,10); i1=et*Fr(75,100); son=2500*Fr(108,100); x=Fr(i1-son,i1)*100; assert (et,i1,son,x)==(4000,3000,2700,10)
s=[Fr(15,2),8,10,12,20]; sirali(s); assert Fr(300,4000)*100==Fr(15,2) and Fr(300,2500)*100==12 and Fr(i1-2500,2500)*100==20
P.R('0008','kz-etiket',T['kz-etiket'],'zor','Etiket, iki indirim, kâr','Etiket fiyatını ve art arda indirimleri sırayla hesaplayıp son kâra göre ikinci indirimin yüzdesini bulur.','hikâyeli',4,
 'K-KZ-04 (etiket kârı, iki indirim, son kâr) · yeni kurgu (mont, kasa indirimi), yeni istenen (ikinci indirim)',
 'Bir mağaza alış fiyatı 2500 TL olan bir montun etiket fiyatını, alış fiyatının %60 fazlası olarak belirlemiştir. Sezon sonunda mont, etiket fiyatı üzerinden %25 indirime girmiştir.\nKasada indirimli fiyat üzerinden ek bir indirim daha yapılınca mağaza bu satıştan %8 kâr etmiştir.\nBuna göre kasada yapılan ek indirim yüzde kaçtır?',
 [yaz(v) for v in s],tek_dogru(s,10),'Kasadaki ek indirimin yüzdesi.',
 ['Etiket fiyatı ve sezon indiriminden sonraki fiyat kaç TL?','%8 kârla montun son satış fiyatı kaç TL?','Ek indirimi, uygulandığı fiyata (sezon indirimli fiyata) oranla.'],[KY,ARD],
 [A('Etiket fiyatı','Alışın %60 fazlası.','2500 × 1,6 = 4000 TL'),
  A('Sezon indirimi','%25 indirimde %75’i ödenir.','4000 × 0,75 = 3000 TL'),
  A('Son satış fiyatı','%8 kâr alış fiyatına göre.','2500 × 1,08 = 2700 TL'),
  A('Ek indirim','3000 TL’den 2700 TL’ye düşüş.','3000 − 2700 = 300 · 300 ÷ 3000 = 0,1 ⇒ %10')],
 'Zincirde her yüzdeyi kendi tabanına göre uygula: kâr alışa, ilk indirim etikete, ek indirim indirimli fiyata göredir.',
 dict(A='7,5 = 300 ÷ 4000; ek indirimi etiket fiyatına oranlamak. Ek indirim 3000 TL’lik indirimli fiyatın yüzdesidir.',B='8, son durumdaki kâr yüzdesi; soru ek indirimi soruyor.',D='12 = 300 ÷ 2500; ek indirimi alış fiyatına oranlamak.',E='20, sezon indiriminden sonraki kâr yüzdesi (3000 TL ile 2500 TL arası).'),
 TT(A='islem',B='dikkat',D='islem',E='dikkat'))
et=1800*Fr(15,10); i1=et*Fr(8,10); son=1800*Fr(102,100); x=Fr(i1-son,i1)*100; assert (et,i1,son,x)==(2700,2160,1836,15)
s=[12,15,18,20,28]; sirali(s); assert Fr(324,2700)*100==12 and Fr(324,1800)*100==18 and Fr(i1-1800,1800)*100==20
P.K('0008','Bir ayakkabı mağazası alış fiyatı 1800 TL olan bir botun etiket fiyatını, alış fiyatının %50 fazlası olarak belirlemiştir. Bot önce etiket fiyatı üzerinden %20 indirimle satışa sunulmuştur.\nDaha sonra indirimli fiyat üzerinden bir indirim daha yapılmış ve bot bu son fiyatla satıldığında mağaza %2 kâr etmiştir.\nBuna göre ikinci indirim yüzde kaçtır?',
 [str(v) for v in s],tek_dogru(s,15),'İkinci indirimin yüzdesi.',
 ['Etiket fiyatı ve ilk indirimden sonraki fiyat kaç TL?','%2 kârla son satış fiyatı kaç TL?','İkinci indirim tutarını ilk indirimli fiyata oranla.'],[KY,ARD],
 [A('Etiket fiyatı','Alışın %50 fazlası.','1800 × 1,5 = 2700 TL'),
  A('İlk indirim','%20 indirimde %80’i ödenir.','2700 × 0,8 = 2160 TL'),
  A('Son satış fiyatı','%2 kâr alış fiyatına göre.','1800 × 1,02 = 1836 TL'),
  A('İkinci indirim','2160 TL’den 1836 TL’ye düşüş.','2160 − 1836 = 324 · 324 ÷ 2160 = 0,15 ⇒ %15')],
 'Bilinmeyen indirimi bulurken düşüş tutarını, indirimin yapıldığı fiyata böl.',
 dict(A='12 = 324 ÷ 2700; ikinci indirimi etiket fiyatına oranlamak.',C='18 = 324 ÷ 1800; ikinci indirimi alış fiyatına oranlamak.',D='20, ilk indirimden sonraki kâr yüzdesi (2160 TL ile 1800 TL arası).',E='28 = 50 − 20 − 2; yüzdeleri toplayıp çıkarmak. Her yüzde farklı bir fiyatın yüzdesidir.'),
 TT(A='islem',C='islem',D='dikkat',E='bilgi'))

P.yaz(os.path.join(H,'karzararprob-1.json'),os.path.join(H,'karzararprob-1-kardes.json'))
