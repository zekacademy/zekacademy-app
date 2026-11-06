"""Yüzde Problemleri · parti 1: 8 ana + 8 kardeş. Her cevap kodla yeniden hesaplanır (assert)."""
import sys,os,json
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,os.path.join(H,'..'))
from ortak import *
P=Parti('yuzdeprob','Yüzde Problemleri','prob|Yüzde Problemleri')
UK='prob|Yüzde Problemleri'
TT=lambda **k:k
def sirali(s): assert s==sorted(s) and len(set(s))==5, s
def tek_dogru(siklar,dogru):
    assert siklar.count(dogru)==1
    return 'ABCDE'[siklar.index(dogru)]

# ---------- kartlar ve tipler
KARTLAR=[
 dict(id='K-YZ-01',konu='Yüzde Problemleri',alt='Parça ve bütün',fikir='Bütünün bir kısmının yüzdesi verilir; geri kalan kısmın sayısından bütün bulunur (kalan yüzde = 100 − verilen).',tuzak='Verilen sayıyı verilen yüzdeye eşlemek; yüzdeyi bilinen sayının üzerine eklemek.',zorluk='kolay',kalip='hikâyeli',adim=2,tipId='yz-parca-butun',tip='Parçadan bütüne yüzde',kaynak='ÖSYM 2021 (anketin yüzdesi) · Bilgi Sarmal, 3D'),
 dict(id='K-YZ-02',konu='Yüzde Problemleri',alt='Ardışık değişim',fikir='Bir nicelik art arda yüzdeyle değişir; ikinci yüzde yeni değerin üzerinden uygulanır (çarpanlar: 1 + p/100, 1 − q/100).',tuzak='Yüzdeleri toplamak; ikinci değişimi ilk değere uygulamak.',zorluk='kolay',kalip='hikâyeli',adim=2,tipId='yz-ardisik',tip='Ardışık yüzde değişimi',kaynak='ÖSYM 2019 (kurutma ve patlatma kaybı) · 3D, Mert Hoca'),
 dict(id='K-YZ-03',konu='Yüzde Problemleri',alt='Ardışık değişim (geriye)',fikir='Art arda kayıplardan sonra kalan miktar verilir; çarpanlar çarpılıp başlangıç miktarı geriye doğru bulunur.',tuzak='Kayıp yüzdelerini toplamak; kaybı son değerin üzerine yüzde olarak geri eklemek.',zorluk='orta',kalip='hikâyeli',adim=3,tipId='yz-ardisik',tip='Ardışık yüzde değişimi',kaynak='ÖSYM 2019 (yaş mısır → patlamış mısır) · Bilgi Sarmal'),
 dict(id='K-YZ-04',konu='Yüzde Problemleri',alt='Çarpım değişimi',fikir='Toplam = adet × birim değer; iki çarpan farklı yüzdelerle değişince toplamın değişimi çarpanların çarpımıyla bulunur.',tuzak='Yüzdeleri toplamak ya da çıkarmak; oranı (%110) artış sanmak.',zorluk='orta',kalip='hikâyeli',adim=3,tipId='yz-carpim',tip='Çarpım biçimindeki niceliklerde yüzde değişim',kaynak='3D (soru sayısı %30 fazla, puan %10 eksik) · 345 SB'),
 dict(id='K-YZ-05',konu='Yüzde Problemleri',alt='Grupların birleşimi',fikir='Farklı büyüklükteki iki grubun yüzdeleri ve birleşik yüzde verilir; sayılar üzerinden (ağırlıklı) denklem kurulur.',tuzak='Yüzdelerin düz ortalamasını almak; sayıyı yüzde sanmak.',zorluk='orta',kalip='hikâyeli',adim=3,tipId='yz-birlesim',tip='Grupların birleşiminde yüzde',kaynak='ÖSYM 2022 (iki gündeki görüşmelerin %24’ü) · Mert Hoca (sınıfların birleşimi)'),
 dict(id='K-YZ-06',konu='Yüzde Problemleri',alt='Grupların birleşimi (iki tür)',fikir='İki türün sayısı farklı yüzdelerle değişir, toplam değişim verilir; başlangıçtaki oran ağırlıklı denklemle bulunur.',tuzak='İki türü eşit sayıda varsaymak; azalışı yanlış türe uygulamak.',zorluk='zor',kalip='hikâyeli',adim=4,tipId='yz-birlesim',tip='Grupların birleşiminde yüzde',kaynak='Bilgi Sarmal, 3D (iki ürünün ayrı ayrı değişimi)'),
 dict(id='K-YZ-07',konu='Yüzde Problemleri',alt='Yüzdenin yüzdesi',fikir='Bir grup iki özelliğe göre ayrılır; “A’ların %x’i” ile “B’lerin %y’si A” gibi farklı tabanlı yüzdeler 100 kişi üzerinden birleştirilir.',tuzak='Yüzdenin hangi bütüne göre verildiğini karıştırmak (tüm grup mu, alt grup mu?).',zorluk='zor',kalip='hikâyeli',adim=5,tipId='yz-ic-ice',tip='Yüzdenin yüzdesi (iç içe gruplar)',kaynak='Bilgi Sarmal, 3D (kız-erkek ve özellik tabloları) · ÖSYM 2023'),
 dict(id='K-YZ-08',konu='Yüzde Problemleri',alt='Aktarımla eşitleme',fikir='İki kaptaki miktarlar yüzdeyle verilir; birinden ötekine aktarılan kısım bir yüzdeyle eşitlenme sağlar.',tuzak='Yüzdenin kabın hacmine mi içindekine mi göre olduğunu karıştırmak; farkın tamamını aktarmak.',zorluk='orta',kalip='hikâyeli',adim=3,tipId='yz-esitleme',tip='Yüzde aktarımıyla eşitleme',kaynak='ÖSYM 2025 (tuzluk ve karabiberlik) · 345 SB'),
]
TIPLER={}
for k in KARTLAR: TIPLER.setdefault(k['tipId'],dict(tipId=k['tipId'],ad=k['tip'],kartlar=[],uygulamaKonu=UK))['kartlar'].append(k['id'])
json.dump(dict(konu='Yüzde Problemleri',surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026, Bilgi Sarmal, 3D, Mert Hoca, 345 SB.',kartlar=KARTLAR,tipler=list(TIPLER.values())),
          open(os.path.join(H,'..','kartlar','yuzdeprob.json'),'w'),ensure_ascii=False,indent=1)
T={t:TIPLER[t]['ad'] for t in TIPLER}

YZ=B('Yüzde','%40 = 40/100 = 0,4 · 200’ün %40’ı = 200 × 0,4 = 80')
BUT=B('Yüzdesi bilinen parçadan bütün','bir sayının %60’ı 30 ise sayı = 30 ÷ 0,6 = 50')
CRP=B('Yüzde değişim çarpanı','%20 artış = × 1,2 · %25 azalış = × 0,75. Örnek: 80 önce %25 artıp sonra %20 azalırsa 80 × 1,25 × 0,8 = 80')
YUZ=B('100 üzerinden düşünmek','yüzde sorularında bütünü 100 al: “%60’ı kız” ⇒ 100 kişide 60 kız')

# ===== 0001 parça-bütün KOLAY
x=Fr(480)/Fr(60,100); assert x==800 and x*Fr(40,100)==320 and 320+480==800
s=[192,320,672,800,1200]; sirali(s); assert 480*Fr(40,100)==192 and 480+192==672 and Fr(480)/Fr(40,100)==1200
P.R('0001','yz-parca-butun',T['yz-parca-butun'],'kolay','Parça ve bütün','Bütünün bir kısmının yüzdesinden kalan kısmın yüzdesini bulur; kalan kısmın sayısından bütünü hesaplar.','hikâyeli',2,
 'K-YZ-01 (kalan kısmın sayısından bütün) · yeni kurgu (fidanlık), yeni sayılar',
 'Bir fidanlıktaki fidanların %40’ı çam, geri kalanı meşe fidanıdır.\nFidanlıkta 480 meşe fidanı olduğuna göre fidanlıkta toplam kaç fidan vardır?',
 [str(v) for v in s],tek_dogru(s,800),'Fidanlıktaki toplam fidan sayısı.',
 ['Meşe fidanları tüm fidanların yüzde kaçıdır?','Toplam fidan sayısına x de; x’in o yüzdesi 480’e eşit olmalı.','Bulduğun sayının %40’ını alıp 480’e ekleyerek kontrol et.'],[YZ,BUT],
 [A('Meşelerin yüzdesi','Çamlar %40 ise geri kalan meşeler %60’tır; 480 sayısı %60’a karşılık gelir.','100 − 40 = 60 ⇒ meşe %60'),
  A('Denklemi kur','Toplam fidan x olsun. x’in %60’ı 480’dir.','x × 60/100 = 480 · x = 480 × 100 ÷ 60 = 800'),
  A('Kontrol','Çamları bulup meşelerle topla.','800 × 0,4 = 320 çam · 320 + 480 = 800 ✓')],
 'Verilen sayının hangi yüzdeye karşılık geldiğini önce belirle; sayıyı o yüzdeye böl.',
 dict(A='192, 480’in %40’ı; yüzdeyi bilinen sayıya uygulamışsın. 480 bütün değil, bütünün %60’ı.',B='320, çam fidanlarının sayısı; soru tüm fidanları soruyor.',C='672 = 480 + 480’in %40’ı; yüzdeyi meşelerin üzerine eklemek. %40 bütünün yüzdesidir.',E='1200, 480’i fidanların %40’ı sanmak; %40 çamlar, meşeler ise %60.'),
 TT(A='bilgi',B='dikkat',C='bilgi',E='dikkat'),
 kisa='Meşeler %60 ise %10’luk dilim 480 ÷ 6 = 80; %100 = 80 × 10 = 800.')
x=Fr(340)/Fr(85,100); assert x==400
s=[51,60,355,391,400]; sirali(s); assert 340*Fr(15,100)==51 and 400*Fr(15,100)==60 and 340+51==391
P.K('0001','Bir alışveriş merkezinin otoparkındaki araçların %15’i elektrikli araçtır.\nOtoparkta elektrikli olmayan 340 araç bulunduğuna göre otoparkta kaç araç vardır?',
 [str(v) for v in s],tek_dogru(s,400),'Otoparktaki araçların sayısı.',
 ['Elektrikli olmayan araçlar tüm araçların yüzde kaçıdır?','Araç sayısına x de; x’in o yüzdesini 340’a eşitle.','Sonucun %15’ini alıp 340’a ekleyerek kontrol et.'],[YZ,BUT],
 [A('Kalan yüzde','Elektrikliler %15 ise elektrikli olmayanlar %85’tir.','100 − 15 = 85'),
  A('Denklem','Araç sayısı x olsun; x’in %85’i 340.','x × 85/100 = 340 · x = 340 × 100 ÷ 85 = 400'),
  A('Kontrol','Elektrikli araçları bulup topla.','400 × 0,15 = 60 · 60 + 340 = 400 ✓')],
 'Sayısı verilen grubun yüzdesini bul; o sayıyı bu yüzdeye bölerek bütüne ulaş.',
 dict(A='51, 340’ın %15’i; yüzdeyi bilinen sayıya uygulamışsın.',B='60, elektrikli araçların sayısı; soru tüm araçları soruyor.',C='355 = 340 + 15; yüzdeyi sayı gibi eklemek.',D='391 = 340 + 340’ın %15’i; %15 bütünün yüzdesidir, 340’ın değil.'),
 TT(A='bilgi',B='dikkat',C='bilgi',D='bilgi'),
 kisa='%85 = 340 ise %5 = 340 ÷ 17 = 20; %100 = 20 × 20 = 400.')

# ===== 0002 ardışık KOLAY
son=40*Fr(12,10)*Fr(125,100); assert son==60
s=[20,48,50,58,60]; sirali(s); assert 40*Fr(12,10)==48 and 40*Fr(125,100)==50 and 40*Fr(145,100)==58 and son-40==20
P.R('0002','yz-ardisik',T['yz-ardisik'],'kolay','Ardışık değişim','Art arda iki yüzde artışını değişim çarpanlarıyla uygular; ikinci yüzdeyi yeni değere göre hesaplar.','hikâyeli',2,
 'K-YZ-02 (art arda iki artış) · yeni kurgu (ayçiçeğinin boyu), yeni istenen (son değer)',
 'Boyu 40 cm olan bir ayçiçeği birinci hafta boyunun %20’si kadar uzamıştır.\nİkinci hafta ise birinci haftanın sonundaki boyunun %25’i kadar uzamıştır.\nBuna göre bu ayçiçeğinin ikinci haftanın sonundaki boyu kaç cm’dir?',
 [str(v) for v in s],tek_dogru(s,60),'İkinci haftanın sonundaki boy.',
 ['Birinci haftanın sonunda boy kaç cm oldu?','İkinci haftadaki %25, 40 cm’nin değil yeni boyun yüzdesidir.','Yüzdeleri toplamak doğru olur mu? Yeni boy üzerinden hesapla.'],[YZ,CRP],
 [A('Birinci hafta','%20 uzama: boy 1,2 ile çarpılır.','40 × 1,2 = 48 cm'),
  A('İkinci hafta','%25 uzama 48 cm’nin üzerinden hesaplanır.','48 × 0,25 = 12 · 48 + 12 = 60 cm'),
  A('Sonuç','İki çarpanı birlikte de uygulayabilirsin.','40 × 1,2 × 1,25 = 60 cm')],
 'Art arda yüzde değişimlerde yüzdeler toplanmaz; her değişim bir öncekinin sonucuna uygulanır.',
 dict(A='20, iki haftadaki toplam uzama; soru son boyu soruyor.',B='48, yalnız birinci haftanın sonundaki boy.',C='50, %25’i doğrudan 40 cm’ye uygulayıp birinci haftayı atlamak.',D='58, yüzdeleri toplayıp (%45) 40 cm’ye uygulamak; ikinci yüzde yeni boyun üzerinden.'),
 TT(A='dikkat',B='dikkat',C='dikkat',D='bilgi'))
son=1500*Fr(8,10)*Fr(125,100); assert son==1500
s=[300,1200,1500,1575,2250]; sirali(s); assert 1500*Fr(8,10)==1200 and 1200*Fr(25,100)==300 and 1500*Fr(105,100)==1575 and 1500*Fr(12,10)*Fr(125,100)==2250
P.K('0002','Bir gölette 1500 m³ su vardır. Yaz aylarında buharlaşma nedeniyle göletteki su %20 azalmıştır.\nSonbaharda yağan yağmurlarla göletteki su, yaz sonundaki miktarın %25’i kadar artmıştır.\nBuna göre sonbaharın sonunda gölette kaç m³ su vardır?',
 [str(v) for v in s],tek_dogru(s,1500),'Sonbahar sonundaki su miktarı.',
 ['Yaz sonunda gölette kaç m³ su kaldı?','Sonbahardaki %25, yaz sonundaki miktarın yüzdesidir.','%20 azalıp %25 artınca başa dönülür mü? Hesapla ve gör.'],[YZ,CRP],
 [A('Yaz sonu','%20 azalış: miktar 0,8 ile çarpılır.','1500 × 0,8 = 1200 m³'),
  A('Sonbahar','%25 artış 1200 m³ üzerinden.','1200 × 0,25 = 300 · 1200 + 300 = 1500 m³'),
  A('Çarpanlarla','İki çarpanın çarpımı 1 olduğundan miktar başa döner.','0,8 × 1,25 = 1 ⇒ 1500 m³')],
 '%20 azalışı geri almak için %20 değil %25 artış gerekir; çünkü artış daha küçük bir değerin üzerinden hesaplanır.',
 dict(A='300, sonbahardaki artış miktarı; soru son miktarı soruyor.',B='1200, yalnız yaz sonundaki miktar.',D='1575, yüzdeleri toplayıp (%5 artış) 1500’e uygulamak; ikinci yüzde yeni miktar üzerinden.',E='2250, yazdaki azalışı artış gibi okumak (1500 × 1,2 × 1,25).'),
 TT(A='dikkat',B='dikkat',D='bilgi',E='dikkat'))

# ===== 0003 ardışık (geriye) ORTA
x=Fr(600)/(Fr(8,10)*Fr(25,100)); assert x==3000 and x*Fr(8,10)*Fr(1,4)==600
s=[750,1260,2400,3000,12000]; sirali(s)
assert Fr(600)/Fr(8,10)==750 and 600*Fr(175,100)*Fr(12,10)==1260 and Fr(600)/Fr(25,100)==2400 and Fr(600)/Fr(5,100)==12000
P.R('0003','yz-ardisik',T['yz-ardisik'],'orta','Ardışık değişim (geriye)','Art arda iki kayıptan sonra kalan miktardan çarpanlarla başlangıç miktarını bulur.','hikâyeli',3,
 'K-YZ-03 (art arda kayıp, sondan başa) · yeni kurgu (kuru domates), yeni sayılar',
 'Bir üretici kuru domates yapmak için önce domatesleri ayıklamaktadır. Ayıklama sırasında domateslerin ağırlığının %20’si (sap, çekirdek) atılmaktadır.\nAyıklanan domatesler kurutulduğunda ağırlıklarının %75’ini kaybetmektedir.\nBuna göre bu üretici 600 gram kuru domates elde etmek için kaç gram domates kullanmalıdır?',
 [str(v) for v in s],tek_dogru(s,3000),'Gereken domates miktarı.',
 ['Domates x gram olsun; ayıklamadan sonra x’in yüzde kaçı kalır?','Kurutmada kalan dilimlerin %75’i kaybolursa yüzde kaçı kalır?','İki kalan oranı çarp ve 600’e eşitle.'],[YZ,CRP],
 [A('Ayıklama','%20 atılırsa %80 kalır.','x × 0,8'),
  A('Kurutma','Ayıklanan domatesin %75’i kaybolur, %25’i kalır.','0,8x × 0,25 = 0,2x'),
  A('Denklem','Kalan miktar 600 gram.','0,2x = 600 ⇒ x = 3000 gram'),
  A('Kontrol','İleri doğru hesapla.','3000 × 0,8 = 2400 · 2400 × 0,25 = 600 ✓')],
 'Art arda kayıplarda her adımda kalan oranı yaz ve çarp; kayıp yüzdelerini toplama.',
 dict(A='750 = 600 ÷ 0,8; yalnız ayıklamayı geri alıp kurutmayı unutmak.',B='1260 = 600 × 1,75 × 1,2; kaybı son ağırlığın üzerine yüzde olarak eklemek. Kayıp, önceki ağırlığın yüzdesidir.',C='2400 = 600 ÷ 0,25; yalnız kurutmayı geri almak, atılan %20’yi unutmak.',E='12000, kayıpları toplayıp (%95) kalanı %5 sanmak; ikinci kayıp ayıklanmış domatesin yüzdesidir.'),
 TT(A='dikkat',B='bilgi',C='dikkat',E='bilgi'))
x=Fr(1320)/(Fr(8,10)*Fr(75,100)); assert x==2200
s=[1650,1760,1980,2200,2400]; sirali(s)
assert Fr(1320)/Fr(8,10)==1650 and Fr(1320)/Fr(75,100)==1760 and 1320*Fr(125,100)*Fr(12,10)==1980 and Fr(1320)/Fr(55,100)==2400
P.K('0003','Bir kahve dükkânında çiğ kahve çekirdekleri kavrulduğunda ağırlıklarının %20’sini kaybetmektedir.\nKavrulan çekirdekler öğütülüp elendiğinde ise ağırlıklarının %25’i iri parça olarak ayrılıp atılmaktadır.\nBu dükkân 1320 gram öğütülmüş kahve elde ettiğine göre kaç gram çiğ çekirdek kavurmuştur?',
 [str(v) for v in s],tek_dogru(s,2200),'Kavrulan çiğ çekirdek miktarı.',
 ['Çiğ çekirdek x gram olsun; kavrulunca yüzde kaçı kalır?','Elemede atılan %25, kavrulmuş çekirdeğin yüzdesidir; kalan oranı yaz.','Kalan oranların çarpımını 1320’ye eşitle.'],[YZ,CRP],
 [A('Kavurma','%20 kayıp ⇒ %80 kalır.','x × 0,8'),
  A('Eleme','Kavrulmuş çekirdeğin %25’i atılır, %75’i kalır.','0,8x × 0,75 = 0,6x'),
  A('Denklem','Kalan 1320 gram.','0,6x = 1320 ⇒ x = 2200 gram'),
  A('Kontrol','İleri doğru hesapla.','2200 × 0,8 = 1760 · 1760 × 0,75 = 1320 ✓')],
 'Sondan başa giderken son miktarı kalan oranların çarpımına böl.',
 dict(A='1650 = 1320 ÷ 0,8; elemeyi hesaba katmamak.',B='1760 = 1320 ÷ 0,75; kavurma kaybını unutmak. Bu değer kavrulmuş çekirdek miktarıdır.',C='1980 = 1320 × 1,25 × 1,2; kayıpları son değerin üzerine yüzde olarak eklemek.',E='2400, kayıpları toplayıp (%45) kalanı %55 sanmak.'),
 TT(A='dikkat',B='dikkat',C='bilgi',E='bilgi'))

# ===== 0004 çarpım değişimi ORTA
o=Fr(125,100)*Fr(88,100); assert o==Fr(11,10) and 125*88==11000
s=[10,13,16,37,110]; sirali(s)
P.R('0004','yz-carpim',T['yz-carpim'],'orta','Çarpım değişimi','Adet ve birim değeri farklı yüzdelerle değişen bir toplamın yüzde değişimini bulur.','hikâyeli',3,
 'K-YZ-04 (adet × birim değer) · yeni kurgu (kargo araçları ve teslimat), yeni sayılar',
 'Bir kargo şirketi dağıtım aracı sayısını %25 artırmıştır. Aynı dönemde yoğun trafik nedeniyle araç başına günlük teslim edilen paket sayısı %12 azalmıştır.\nHer aracın günde eşit sayıda paket teslim ettiği bilindiğine göre şirketin günlük toplam teslimat sayısı yüzde kaç artmıştır?',
 [str(v) for v in s],tek_dogru(s,10),'Günlük toplam teslimattaki yüzde artış.',
 ['Toplam teslimat = araç sayısı × araç başına teslimat.','Başlangıçta 100 araç ve araç başına 100 paket al.','Yeni toplamı eski toplamla karşılaştır.'],[CRP,YUZ],
 [A('100 üzerinden başla','100 araç, her biri 100 paket.','100 × 100 = 10000 paket'),
  A('Yeni durum','Araç %25 artar, araç başı teslimat %12 azalır.','125 × 88 = 11000 paket'),
  A('Yüzde artış','Artışı ilk toplama böl.','11000 − 10000 = 1000 · 1000 ÷ 10000 = 0,1 ⇒ %10')],
 'Çarpım biçimindeki bir niceliğin yüzde değişimi, çarpanların değişim çarpanlarının çarpımıyla bulunur.',
 dict(B='13 = 25 − 12; yüzdeleri çıkarmak. Toplam bir çarpım olduğundan çarpanlar çarpılır.',C='16, çarpımı açarken işaret hatası: 25 − 12 + 3 almak; doğrusu 25 − 12 − 3 = 10.',D='37 = 25 + 12; azalışı da artış gibi eklemek.',E='110, yeni toplamın eski toplama oranı (%110); artış bunun 100’den fazlası.'),
 TT(B='bilgi',C='islem',D='dikkat',E='dikkat'),
 kisa='Değişim çarpanlarını doğrudan çarp: 1,25 × 0,88 = 1,10 ⇒ %10 artış.')
y=400*Fr(8,10)*Fr(135,100); assert y==432
s=[320,432,460,540,620]; sirali(s); assert 400*Fr(8,10)==320 and 400*Fr(115,100)==460 and 400*Fr(135,100)==540 and 400*Fr(155,100)==620
P.K('0004','Bir çiftçi geçen yıl buğday ektiği tarlasından 400 ton ürün almıştır. Bu yıl ekili alanı %20 azaltmış, yeni sulama sistemi sayesinde dekar başına aldığı ürün ise %35 artmıştır.\nDekar başına ürünün tarlanın her yerinde aynı olduğu bilindiğine göre çiftçi bu yıl kaç ton ürün almıştır?',
 [str(v) for v in s],tek_dogru(s,432),'Bu yılki toplam ürün.',
 ['Toplam ürün = ekili alan × dekar başına ürün.','Alan için çarpan 0,8; dekar başına ürün için çarpan kaç?','İki çarpanı 400 ile çarp.'],[CRP,B('Çarpımın değişimi','toplam = adet × birim değer ise iki çarpanın değişim çarpanları çarpılır. Örnek: 2 kat adet, yarı değer ⇒ toplam aynı')],
 [A('Toplamı çarpım olarak yaz','Ürün, ekili alan ile dekar başına ürünün çarpımıdır.','toplam = alan × verim'),
  A('Değişim çarpanları','Alan %20 azalır, verim %35 artar.','0,8 × 1,35 = 1,08'),
  A('Bu yılki ürün','400 tonu çarpanla çarp.','400 × 1,08 = 432 ton')],
 'İki çarpanı birden değişen bir toplamda yüzdeleri toplama; değişim çarpanlarını çarp.',
 dict(A='320, yalnız alandaki azalışı uygulamak; verim artışı unutulmuş.',C='460 = 400 × 1,15; yüzdeleri çıkarmak (35 − 20). Değişimler çarpılarak birleşir.',D='540, yalnız verim artışını uygulamak; alan azalmıştır.',E='620, azalışı da artış gibi eklemek (%20 + %35).'),
 TT(A='dikkat',C='bilgi',D='dikkat',E='dikkat'))

# ===== 0005 birleşim ORTA
xs=[x for x in range(0,101) if 30*Fr(40,100)+20*Fr(x,100)==50*Fr(52,100)]; assert xs==[70]
s=[14,26,28,64,70]; sirali(s); assert 20*Fr(70,100)==14 and 12+14==26 and Fr(14,50)*100==28 and (40+64)/2==52
P.R('0005','yz-birlesim',T['yz-birlesim'],'orta','Grupların birleşimi','Büyüklükleri farklı iki grubun yüzdelerini sayıya çevirip birleşik yüzde denklemini kurar.','hikâyeli',3,
 'K-YZ-05 (iki grup, birleşik yüzde) · yeni kurgu (yüzme kulübü), yeni istenen (ikinci grubun yüzdesi)',
 'Bir yüzme kulübünün sabah grubunda 30, akşam grubunda 20 sporcu vardır. Sabah grubundaki sporcuların %40’ı lisanslıdır.\nİki grup birlikte düşünüldüğünde sporcuların %52’si lisanslı olduğuna göre akşam grubundaki sporcuların yüzde kaçı lisanslıdır?',
 [str(v) for v in s],tek_dogru(s,70),'Akşam grubundaki lisanslı sporcuların yüzdesi.',
 ['Sabah grubunda kaç lisanslı sporcu var?','İki grupta toplam 50 sporcu var; bunların %52’si kaç kişi?','Akşamdaki lisanslı sayısını akşam grubunun mevcuduna böl.'],[YZ,B('Yüzde ↔ sayı','sayıyı bulmak için yüzdeyi grubun mevcuduyla çarp; yüzdeyi bulmak için sayıyı mevcuda bölüp 100 ile çarp. Örnek: 25 kişide 5 kişi ⇒ %20')],
 [A('Sabah grubu','30 sporcunun %40’ı.','30 × 0,4 = 12 lisanslı'),
  A('Toplam lisanslı','50 sporcunun %52’si.','50 × 0,52 = 26 lisanslı'),
  A('Akşam grubu','Fark akşam grubundaki lisanslılardır.','26 − 12 = 14 · 14 ÷ 20 = 0,7 ⇒ %70')],
 'Farklı büyüklükteki grupların yüzdeleri ortalanmaz; önce sayılara çevir, sonra topla.',
 dict(A='14, akşam grubundaki lisanslı sporcu sayısı; soru yüzdeyi soruyor.',B='26, iki gruptaki toplam lisanslı sayısı.',C='28 = 14 ÷ 50; akşamdaki lisanslıları tüm sporculara bölmek. Akşam grubunun yüzdesi için 20’ye bölünür.',D='64, yüzdelerin düz ortalamasını almak: (40 + x) ÷ 2 = 52. Gruplar eşit büyüklükte değil.'),
 TT(A='dikkat',B='dikkat',C='islem',D='bilgi'))
xs=[x for x in range(0,101) if 30*Fr(70,100)+50*Fr(x,100)==80*Fr(65,100)]; assert xs==[62]
s=[31,52,60,62,65]; sirali(s); assert 52-21==31 and (70+60)/2==65
P.K('0005','Bir bilgi yarışmasının birinci turunda 30, ikinci turunda 50 soru sorulmuştur. Ece birinci turdaki soruların %70’ini doğru cevaplamıştır.\nEce iki turdaki soruların toplamda %65’ini doğru cevapladığına göre ikinci turdaki soruların yüzde kaçını doğru cevaplamıştır?',
 [str(v) for v in s],tek_dogru(s,62),'İkinci turdaki doğru cevap yüzdesi.',
 ['Birinci turda kaç soruyu doğru cevapladı?','80 sorunun %65’i kaç soru eder?','İkinci turdaki doğru sayısını 50’ye böl.'],[YZ,B('Yüzde ↔ sayı','sayıyı bulmak için yüzdeyi grubun mevcuduyla çarp; yüzdeyi bulmak için sayıyı mevcuda bölüp 100 ile çarp. Örnek: 25 soruda 5 doğru ⇒ %20')],
 [A('Birinci tur','30 sorunun %70’i.','30 × 0,7 = 21 doğru'),
  A('İki tur birlikte','80 sorunun %65’i.','80 × 0,65 = 52 doğru'),
  A('İkinci tur','Farkı 50 soruya oranla.','52 − 21 = 31 · 31 ÷ 50 = 0,62 ⇒ %62')],
 'Birleşik yüzde verildiğinde her grubu sayıya çevir; yüzdeleri doğrudan ortalama.',
 dict(A='31, ikinci turda doğru cevaplanan soru sayısı; yüzde değil.',B='52, iki turdaki toplam doğru sayısı.',C='60, yüzdelerin düz ortalamasını almak: (70 + x) ÷ 2 = 65. Turlardaki soru sayıları farklı.',E='65, iki turun birlikte doğru yüzdesi; soru yalnız ikinci turu soruyor.'),
 TT(A='dikkat',B='dikkat',C='bilgi',E='dikkat'))

# ===== 0006 eşitleme ORTA
xs=[x for x in range(1,100) if 75-75*Fr(x,100)==15+75*Fr(x,100)]; assert xs==[40]
s=[30,40,45,60,80]; sirali(s); assert 75*Fr(40,100)==30 and 75-30==45 and Fr(60,75)*100==80
P.R('0006','yz-esitleme',T['yz-esitleme'],'orta','Aktarımla eşitleme','Kap hacmine göre verilen doluluk yüzdelerinden aktarılması gereken miktarı bulur ve bunu kaptaki miktarın yüzdesi olarak ifade eder.','hikâyeli',3,
 'K-YZ-08 (iki kap, aktarımla eşitleme) · yeni kurgu (su depoları), yeni istenen (içindekinin yüzdesi)',
 'Özdeş iki su deposundan birincisinin %75’i, ikincisinin %15’i suyla doludur.\nBirinci depodaki suyun bir kısmı ikinci depoya aktarıldığında iki depodaki su miktarları eşit olmaktadır.\nBuna göre birinci depodaki suyun yüzde kaçı aktarılmıştır?',
 [str(v) for v in s],tek_dogru(s,40),'Birinci depodaki suyun aktarılan yüzdesi.',
 ['Depoların hacmini 100 litre al; depolarda kaçar litre su var?','Eşitlenince her depoda toplam suyun yarısı olur.','Aktarılan miktarı deponun hacmine değil, birinci depodaki suya böl.'],[YUZ,YZ],
 [A('100 litre al','Depolar özdeş; hacim 100 litre olsun.','birinci: 75 L · ikinci: 15 L'),
  A('Eşit paylaşım','Toplam su değişmez; eşitlenince her depoda yarısı olur.','75 + 15 = 90 · 90 ÷ 2 = 45 L'),
  A('Aktarılan','Birinci depodan çıkan su.','75 − 45 = 30 L'),
  A('Yüzdeye çevir','30 litre, birinci depodaki 75 litrenin yüzde kaçı?','30 ÷ 75 = 0,4 ⇒ %40')],
 'Yüzdenin hangi bütüne göre sorulduğuna bak: deponun hacmine mi, depodaki suya mı?',
 dict(A='30, aktarılan suyun deponun hacmine oranı; soru birinci depodaki suyun yüzdesini soruyor.',C='45, eşitlendikten sonra her deponun doluluk yüzdesi.',D='60, iki doluluk oranının farkı; eşitlemek için farkın yarısı aktarılır.',E='80 = 60 ÷ 75; farkın tamamını aktarmak. Farkın yarısı aktarılınca eşitlenir.'),
 TT(A='dikkat',C='dikkat',D='bilgi',E='bilgi'))
xs=[x for x in range(1,100) if 60-60*Fr(x,100)==30+60*Fr(x,100)]; assert xs==[25]
s=[25,30,45,50,75]; sirali(s); assert 60*Fr(25,100)==15 and 30+15==45 and Fr(15,30)*100==50
P.K('0006','Bir okulun 10-A şubesinde 60, 10-B şubesinde 30 öğrenci kayıtlıdır. Şube mevcutlarını eşitlemek için 10-A şubesindeki öğrencilerin bir kısmı 10-B şubesine geçirilecektir.\nBuna göre 10-A şubesindeki öğrencilerin yüzde kaçı 10-B şubesine geçirilmelidir?',
 [str(v) for v in s],tek_dogru(s,25),'10-A’dan geçirilecek öğrencilerin 10-A’ya göre yüzdesi.',
 ['Eşitlenince her şubede kaç öğrenci olur?','10-A’dan kaç öğrenci çıkmalı?','Bu sayıyı 10-A’nın ilk mevcuduna böl.'],[YZ,B('Yüzdeyi bulmak','parça ÷ bütün × 100. Örnek: 40 kişiden 10 kişi ⇒ 10 ÷ 40 = 0,25 ⇒ %25')],
 [A('Eşit mevcut','Toplam öğrenci değişmez; ikiye bölünür.','60 + 30 = 90 · 90 ÷ 2 = 45'),
  A('Geçen öğrenci','10-A 45’e inmeli.','60 − 45 = 15 öğrenci'),
  A('Yüzde','15 öğrenci, 10-A’nın 60 öğrencisinin yüzde kaçı?','15 ÷ 60 = 0,25 ⇒ %25')],
 'Eşitlemede farkın yarısı aktarılır; yüzde, aktarılan miktarın çıktığı yere göre hesaplanır.',
 dict(B='30, iki şubenin mevcut farkı; farkın yarısı geçirilir ve yüzde 60’a göre hesaplanır.',C='45, eşitlendikten sonraki şube mevcudu.',D='50 = 15 ÷ 30; geçen öğrencileri 10-B’nin mevcuduna bölmek. Yüzde, 10-A’ya göre sorulmuş.',E='75, 10-A’da kalan öğrencilerin yüzdesi; soru geçenleri soruyor.'),
 TT(B='bilgi',C='dikkat',D='islem',E='dikkat'))

# ===== 0007 iç içe ZOR
N=100; kiz=60; erk=N-kiz; yer=erk*Fr(45,100); assert yer==18
yt=yer/Fr(60,100); assert yt==30; yk=yt-yer; assert yk==12 and yk/kiz==Fr(20,100)
s=[12,18,20,30,45]; sirali(s); assert (18/Fr(40,100)-18)/60*100==45
P.R('0007','yz-ic-ice',T['yz-ic-ice'],'zor','Yüzdenin yüzdesi','Farklı bütünlere göre verilen yüzdeleri 100 kişilik bir grup üzerinde birleştirip alt grubun yüzdesini bulur.','hikâyeli',5,
 'K-YZ-07 (iki özellik, farklı tabanlı yüzdeler) · yeni kurgu (yaz kampı ve yüzme), yeni istenen (alt grup içindeki oran)',
 'Bir yaz kampındaki katılımcıların %60’ı kızdır. Erkek katılımcıların %45’i yüzme bilmektedir.\nYüzme bilen katılımcıların %40’ı kız olduğuna göre kız katılımcıların yüzde kaçı yüzme bilmektedir?',
 [str(v) for v in s],tek_dogru(s,20),'Kızlar içinde yüzme bilenlerin yüzdesi.',
 ['Katılımcı sayısını 100 al; kaç kız, kaç erkek var?','Yüzme bilen erkekler, yüzme bilenlerin yüzde kaçıdır?','Yüzme bilen kız sayısını tüm kızların sayısına böl.'],[YUZ,B('Yüzdenin tabanı','“erkeklerin %45’i” erkeklere, “yüzme bilenlerin %40’ı” yüzme bilenlere göredir. Örnek: 50 erkeğin %10’u = 5 kişi')],
 [A('100 kişi al','%60 kız.','60 kız · 40 erkek'),
  A('Yüzme bilen erkekler','Erkeklerin %45’i.','40 × 0,45 = 18'),
  A('Yüzme bilenlerin tamamı','Yüzme bilenlerin %40’ı kız, %60’ı erkek; 18 kişi %60’a karşılık gelir.','18 ÷ 0,6 = 30 kişi'),
  A('Yüzme bilen kızlar','Toplamdan erkekleri çıkar.','30 − 18 = 12'),
  A('Kızlar içindeki oran','12 kız, 60 kızın yüzde kaçı?','12 ÷ 60 = 0,2 ⇒ %20')],
 'Her yüzdenin hangi gruba göre verildiğini yaz; 100 kişilik bir tablo kurup sayılarla ilerle.',
 dict(A='12, yüzme bilen kızların tüm katılımcılara oranı; soru kızlar içindeki oranı soruyor.',B='18, yüzme bilen erkeklerin tüm katılımcılara oranı.',D='30, yüzme bilenlerin tüm katılımcılara oranı.',E='45: 18’i %40’a bölmek; erkekler yüzme bilenlerin %60’ıdır, %40’ı değil.'),
 TT(A='dikkat',B='dikkat',D='dikkat',E='islem'))
yaz=25; dig=75; sd=dig*Fr(12,100); assert sd==9; st=sd/Fr(60,100); assert st==15; sy=st-sd; assert sy==6 and sy/yaz==Fr(24,100)
s=[6,15,24,40,54]; sirali(s); assert (9/Fr(40,100)-9)/25*100==54
P.K('0007','Bir şirketin çalışanlarının %25’i yazılım ekibinde, diğerleri farklı birimlerde çalışmaktadır. Yazılım ekibi dışındaki çalışanların %12’sinin yabancı dil sertifikası vardır.\nSertifikası olan çalışanların %40’ı yazılım ekibinde olduğuna göre yazılım ekibindeki çalışanların yüzde kaçının sertifikası vardır?',
 [str(v) for v in s],tek_dogru(s,24),'Yazılım ekibi içinde sertifikalıların yüzdesi.',
 ['Çalışan sayısını 100 al; yazılım ekibinde ve diğer birimlerde kaç kişi var?','Diğer birimlerdeki sertifikalılar, tüm sertifikalıların yüzde kaçıdır?','Yazılım ekibindeki sertifikalıları ekibin mevcuduna böl.'],[YUZ,B('Yüzdenin tabanı','“diğerlerinin %12’si” diğer çalışanlara, “sertifikalıların %40’ı” sertifikalılara göredir. Örnek: 50 kişinin %10’u = 5 kişi')],
 [A('100 çalışan al','%25 yazılım.','25 yazılım · 75 diğer'),
  A('Diğer birimler','75 kişinin %12’si sertifikalı.','75 × 0,12 = 9'),
  A('Tüm sertifikalılar','Sertifikalıların %60’ı diğer birimlerde; 9 kişi %60’a karşılık gelir.','9 ÷ 0,6 = 15'),
  A('Yazılımdaki sertifikalılar','Toplamdan diğerlerini çıkar.','15 − 9 = 6'),
  A('Ekip içindeki oran','6 kişi, 25 kişinin yüzde kaçı?','6 ÷ 25 = 0,24 ⇒ %24')],
 '“…’ların %x’i” ifadesinde taban daima “…’lar”dır; tabanı karıştırmamak için 100 kişilik tablo kur.',
 dict(A='6, sertifikalı yazılımcıların tüm çalışanlara oranı; soru yazılım ekibi içindeki oranı soruyor.',B='15, sertifikalıların tüm çalışanlara oranı.',D='40, sertifikalılar içindeki yazılımcı oranı; taban farklı.',E='54: 9’u %40’a bölmek; diğer birimler sertifikalıların %60’ıdır.'),
 TT(A='dikkat',B='dikkat',D='dikkat',E='islem'))

# ===== 0008 birleşim (iki tür) ZOR
rs=[r for r in range(0,101) if r*Fr(20,100)-(100-r)*Fr(10,100)==8]; assert rs==[60]
s=[40,50,60,72,80]; sirali(s); assert 60*Fr(12,10)==72 and [r for r in range(101) if r*Fr(2,10)-r*Fr(1,10)==8]==[80] and 50*Fr(2,10)-50*Fr(1,10)==5
P.R('0008','yz-birlesim',T['yz-birlesim'],'zor','Grupların birleşimi (iki tür)','İki türün farklı yüzdelerle değiştiği bir toplamda, toplam değişimden başlangıçtaki türlerin oranını bulur.','hikâyeli',4,
 'K-YZ-06 (iki türün ayrı değişimi, toplam değişim) · yeni kurgu (kütüphane), yeni istenen (başlangıç oranı)',
 'Bir kütüphanede yalnızca roman ve hikâye kitapları vardır. Yıl içinde roman sayısı %20 artmış, hikâye kitaplarının sayısı ise %10 azalmıştır.\nBu değişimlerden sonra kütüphanedeki toplam kitap sayısı %8 arttığına göre başlangıçta kitapların yüzde kaçı romandır?',
 [str(v) for v in s],tek_dogru(s,60),'Başlangıçta romanların toplam içindeki yüzdesi.',
 ['Başlangıçta 100 kitap olsun; r tanesi roman ise kaç tanesi hikâye?','Romanlardaki artış ve hikâyelerdeki azalış kaç kitap eder?','Net değişim 100 kitabın %8’i, yani 8 kitap olmalı.'],[YUZ,YZ],
 [A('100 kitap al','r roman, 100 − r hikâye.','roman: r · hikâye: 100 − r'),
  A('Değişimler','Roman %20 artar, hikâye %10 azalır.','artış: 0,2r · azalış: 0,1 × (100 − r)'),
  A('Net değişim','Toplam 100’den 108’e çıkmış.','0,2r − 0,1 × (100 − r) = 8'),
  A('Çöz','Parantezi aç ve r’yi bul.','0,2r − 10 + 0,1r = 8 · 0,3r = 18 ⇒ r = 60')],
 'İki türün farklı yüzdelerle değiştiği sorularda bütünü 100 al, her türün değişimini ayrı yaz ve net değişime eşitle.',
 dict(A='40, hikâye kitaplarının başlangıç yüzdesi; soru romanları soruyor.',B='50, iki türü eşit sayıda varsaymak; o zaman net artış %5 olur, %8 değil.',D='72, 100 kitaplık başlangıçta romanların artıştan sonraki sayısı; soru başlangıç yüzdesini soruyor.',E='80: azalışı da roman sayısına uygulamak (0,2r − 0,1r = 8); azalış hikâyelerdedir.'),
 TT(A='dikkat',B='bilgi',D='dikkat',E='islem'))
es=[e for e in range(0,101) if e*Fr(25,100)-(100-e)*Fr(15,100)==9]; assert es==[60]
s=[10,34,40,50,60]; sirali(s); assert 40*Fr(85,100)==34 and [e for e in range(101) if e*Fr(25,100)-e*Fr(15,100)==9]==[90]
P.K('0008','Bir fidanlıkta yalnızca elma ve armut fidanları yetiştirilmektedir. Bu yıl elma fidanlarının sayısı %25 artırılmış, armut fidanlarının sayısı ise %15 azaltılmıştır.\nBu değişimlerle fidanlıktaki toplam fidan sayısı %9 arttığına göre başlangıçta fidanların yüzde kaçı armut fidanıdır?',
 [str(v) for v in s],tek_dogru(s,40),'Başlangıçta armut fidanlarının yüzdesi.',
 ['Başlangıçta 100 fidan al; e tanesi elma ise kaç tanesi armut?','Elmalardaki artışı ve armutlardaki azalışı e cinsinden yaz.','Net değişim 9 fidan olmalı; e’yi bulduktan sonra sorulanın armut olduğunu unutma.'],[YUZ,YZ],
 [A('100 fidan al','e elma, 100 − e armut.','elma: e · armut: 100 − e'),
  A('Değişimler','Elma %25 artar, armut %15 azalır.','artış: 0,25e · azalış: 0,15 × (100 − e)'),
  A('Net değişim','Toplam 9 fidan artmış.','0,25e − 15 + 0,15e = 9 · 0,4e = 24 ⇒ e = 60'),
  A('İstenen','Armutlar 100 − 60.','armut: %40')],
 'Denklemi bir tür için kurup çözdükten sonra sorulan türü kontrol et.',
 dict(A='10: azalışı da elma sayısına uygulamak (0,25e − 0,15e = 9 ⇒ e = 90); azalış armutlardadır.',B='34, 100 fidanlık başlangıçta armutların azalıştan sonraki sayısı.',D='50, iki türü eşit sayıda varsaymak; o zaman net artış %5 olur, %9 değil.',E='60, elma fidanlarının başlangıç yüzdesi; soru armutları soruyor.'),
 TT(A='islem',B='dikkat',D='bilgi',E='dikkat'))

P.yaz(os.path.join(H,'yuzdeprob-1.json'),os.path.join(H,'yuzdeprob-1-kardes.json'))
