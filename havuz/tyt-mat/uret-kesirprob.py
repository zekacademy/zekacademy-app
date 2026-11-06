"""Kesir Problemleri · iskelet havuz (8 ana + 8 kardeş). Her cevap ve ara sonuç kodla doğrulanır."""
import sys,os,json
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,os.path.join(H,'..'))
from ortak import *
TT=lambda **k:k
KONU='Kesir Problemleri'; UK='prob|Kesir Problemleri'
P=Parti('kesirprob',KONU,UK)

KARTLAR=[
 dict(id='K-KES-01',konu=KONU,alt='Kalanın kesri',fikir='Bir bütünden ardışık olarak “kalanın” kesirleri ayrılır; sondaki miktar verilip başlangıç ya da aradaki bir parça istenir.',
      tuzak='“Kalanın” kesrini bütüne uygulamak; yalnızca son adımı geri alıp durmak; istenen ara parçayı karıştırmak.',zorluk='kolay-orta',kalip='hikâyeli',adim=3,tipId='kes-kalanin',tip='Ardışık “kalanın” kesirleri',
      kaynak='ÖSYM YKS çıkmış (kitap s150 #173, sergide satılan tablolar) · Bilgi Sarmal s208 #12, s271 #4 · 3D s188 #8'),
 dict(id='K-KES-02',konu=KONU,alt='Parçadan bütüne',fikir='Bütünün bilinen kesirleri dışında kalan parçanın değeri verilir; kalan kesir bulunup bütüne, oradan istenen parçaya geçilir.',
      tuzak='Kalan kesri değil verilen kesri kullanmak; bütünü bulup istenen parçaya geçmeyi unutmak.',zorluk='kolay-orta',kalip='hikâyeli',adim=3,tipId='kes-parca',tip='Parçadan bütüne geçiş',
      kaynak='ÖSYM YKS çıkmış (kitap s1 #1, pasta dilimleri; s14 #21, boyalı kareler) · Bilgi Sarmal ve 345 SB kesir soruları'),
 dict(id='K-KES-03',konu=KONU,alt='Dolu–boş kap',fikir='Kabın dolu ve kısmen dolu kütleleri verilir; farkın içindekinin hangi kesrine karşılık geldiği bulunur, içindekinin tamamı ve boş kap hesaplanır.',
      tuzak='Farkı kalan kısmın karşılığı sanmak; boş kap ile içindekinin tamamını karıştırmak.',zorluk='orta',kalip='hikâyeli',adim=3,tipId='kes-dolu',tip='Dolu–boş kap kütlesi',
      kaynak='Bilgi Sarmal s264 #8 · 3D s144 #2, s185 #11 · Mert s181 #12'),
 dict(id='K-KES-04',konu=KONU,alt='Kesirle paylaştırma',fikir='Bir tutar kişilere ya da bölümlere bütünün ve kalanın kesirleriyle dağıtılır; iki payın farkı verilip bütün ya da bir pay istenir.',
      tuzak='“Kalanın” kesrini bütünün kesri sanmak; farkı yanlış iki pay arasında kurmak; istenen payı karıştırmak.',zorluk='orta-zor',kalip='hikâyeli',adim=4,tipId='kes-pay',tip='Kesirlerle paylaştırma',
      kaynak='Bilgi Sarmal s285 #1 · 3D s188 #8 · 345 SB kesir problemleri'),
 dict(id='K-KES-05',konu=KONU,alt='Tekrarlı süreç',fikir='Her dönem mevcut miktarın bir kesri kullanılır, ardından sabit miktar eklenir; son durum verilip işlemler sondan başa ters sırayla geri alınır.',
      tuzak='Geri dönerken işlem sırasını karıştırmak (önce bölüp sonra çıkarmak); eklemeleri yok saymak; ara günü başlangıç sanmak.',zorluk='zor',kalip='hikâyeli',adim=4,tipId='kes-surec',tip='Tekrarlı kesir süreci (sondan başa)',
      kaynak='ÖSYM YKS çıkmış (kitap s150 #173, her sergide 3/5 satış ve yenileme) · Bilgi Sarmal s271 #4'),
]
TIPLER=[dict(tipId=k['tipId'],ad=k['tip'],kartlar=[k['id']],uygulamaKonu=UK) for k in KARTLAR]
json.dump(dict(konu=KONU,surum=1,kartlar=KARTLAR,tipler=TIPLER),open(os.path.join(H,'..','kartlar','kesirprob.json'),'w'),ensure_ascii=False,indent=1)
T={k['tipId']:k['tip'] for k in KARTLAR}

KALAN=B('Kalanın kesri','“kalanın 1/3’ü” = kalan × 1/3; bütünün değil, kalanın parçasıdır. Örnek: 90’ın 1/3’ü ayrılınca 60 kalır; kalanın 1/4’ü 60 × 1/4 = 15’tir')
PARCA=B('Parçadan bütüne','bütünün a/b’si X ise bütün = X ÷ a × b. Örnek: 3/5’i 60 olan sayı 60 ÷ 3 × 5 = 100')
DOLU=B('Dolu ve boş kap','dolu kap = boş kap + içindekinin tamamı. İki tartımın farkı, aradaki eksilen miktarın kütlesidir')
GERI=B('Sondan başa çözüm','işlemleri ters sırayla ve ters işlemle geri al. “80 eklendi” ⇒ geri dönerken 80 çıkar · “1/3’ü kullanıldı” ⇒ kalan öncekinin 2/3’ü, geri dönerken 2/3’e böl')

# ===== 0001 parça KOLAY
t=Fr(1500)/(1-Fr(3,8)); assert t==2400 and t/8==300 and t*Fr(3,8)==900 and Fr(1500)/Fr(3,8)==4000 and 1500*8==12000
P.R('0001','kes-parca',T['kes-parca'],'kolay','Kalan parçadan bütün','Bütünün bir kesri tamamlandıktan sonra kalan miktardan bütünü bulur.','hikâyeli',2,
 'K-KES-02 (parçadan bütüne) · yeni kurgu (oyun güncellemesi indirme), kalan miktar verildi',
 'Kerem, telefonuna bir oyunun güncelleme dosyasını indirmektedir.\nDosyanın 3/8’i indiğinde, inmesi gereken 1500 MB daha olduğunu görmüştür.\nBuna göre güncelleme dosyasının tamamı kaç MB’tır?',
 ['300','900','2400','4000','12000'],'C','Dosyanın tamamının büyüklüğü.',
 ['Dosyanın 3/8’i indiyse kaçta kaçı inmeyi bekliyor?','1500 MB, dosyanın hangi kesrine karşılık geliyor?','Bir parçanın (1/8) kaç MB olduğunu bul.'],[PARCA],
 [A('Kalan kesir','İnen kısım 3/8; geri kalanı inmeyi bekliyor.','1 − 3/8 = 5/8'),
  A('Bir parça','5/8 = 1500 MB ise 1/8 bunun beşte biri.','1500 ÷ 5 = 300 MB'),
  A('Tamamı','8 parçanın hepsi.','8 × 300 = 2400 MB')],
 'Verilen sayı hangi parçaya aitse o parçanın kesrini kullan; “kalan” verildiyse önce kalan kesri bul.',
 dict(A='300 MB, dosyanın yalnızca 1/8’i; tamamı 8 parça.',B='900 MB, inmiş olan kısım (3/8); soru dosyanın tamamını soruyor.',D='4000 MB, 1500’ü inen kısmın (3/8) karşılığı sanmak; 1500 MB kalan kısım.',E='12000 MB, 1500’ü paydayla çarpıp paya bölmeyi unutmak.'),
 TT(A='dikkat',B='dikkat',D='dikkat',E='islem'))
v=Fr(350)/(1-Fr(2,7)); assert v==490 and v/7==70 and v*Fr(2,7)==140 and 350*Fr(5,7)==250 and Fr(350)/Fr(2,7)==1225
P.K('0001','Bir bahçe sulama deposunun 2/7’si suyla doludur.\nDepoya 350 litre daha su eklendiğinde depo tamamen dolmuştur.\nBuna göre deponun tamamı kaç litre su alır?',
 ['70','140','250','490','1225'],'D','Deponun tamamının aldığı su.',
 ['Depo 2/7 doluysa eklenen su deponun kaçta kaçını doldurdu?','350 litre o kesre karşılık gelir.','Önce 1/7’nin kaç litre olduğunu bul.'],[PARCA],
 [A('Boş kısım','Doluluk 2/7; eklenen su boş kısmı doldurdu.','1 − 2/7 = 5/7'),
  A('Bir parça','5/7 = 350 litre.','1/7 = 350 ÷ 5 = 70 litre'),
  A('Tamamı','7 parça.','7 × 70 = 490 litre')],
 'Eklenen ya da kalan miktar hangi kesre denk geliyorsa bütüne o kesirle geç.',
 dict(A='70 litre, deponun yalnızca 1/7’si.',B='140 litre, başlangıçta depoda bulunan su (2/7).',C='250 litre, 350’yi 5/7’ye bölmek yerine 5/7 ile çarpmak.',E='1225 litre, 350 litreyi deponun 2/7’si sanmak; 350 litre boş kısmı doldurdu.'),
 TT(A='dikkat',B='dikkat',C='islem',E='dikkat'))

# ===== 0002 kalanın KOLAY
m=Fr(30000)/((1-Fr(1,4))*(1-Fr(1,3))); assert m==60000
assert Fr(30000)/(1-Fr(1,4))==40000 and Fr(30000)/(1-Fr(1,4)-Fr(1,3))==72000 and 30000*3==90000 and Fr(30000)/Fr(1,4)==120000
P.R('0002','kes-kalanin',T['kes-kalanin'],'kolay','İki adımlı kalan','İki ardışık “kalanın” kesrinden sonra kalan miktardan başlangıçtaki miktarı bulur.','hikâyeli',2,
 'K-KES-01 (kalanın kesri, sondaki miktar verildi) · yeni kurgu (aile bütçesi), iki adım',
 'Bir aile, aylık gelirinin 1/4’ünü kiraya, kalan paranın 1/3’ünü de fatura ve ulaşım giderlerine ayırmaktadır.\nBu ödemelerden sonra ailenin elinde 30 000 TL kalmaktadır.\nBuna göre ailenin aylık geliri kaç TL’dir?',
 ['40 000','60 000','72 000','90 000','120 000'],'B','Ailenin aylık geliri.',
 ['Kiradan sonra gelirin kaçta kaçı kalır?','Faturalardan sonra, kalanın kaçta kaçı elde kalır?','İki kesri çarparak elde kalan kısmın gelire oranını bul.'],[KALAN],
 [A('Kiradan sonra','Gelirin 1/4’ü gitti.','kalan: 1 − 1/4 = 3/4'),
  A('Faturalardan sonra','Kalanın 1/3’ü gitti, 2/3’ü kaldı.','3/4 × 2/3 = 1/2'),
  A('Geliri bul','Gelirin yarısı 30 000 TL.','30 000 × 2 = 60 000 TL')],
 '“Kalanın” kesirlerinde elde kalan kısımları çarp; toplama ya da çıkarma yapma.',
 dict(A='40 000 TL, yalnız kira adımını geri almak (30 000 ÷ 3/4); faturalar unutuldu.',C='72 000 TL, “kalanın 1/3’ü”nü gelirin 1/3’ü sanmak (1 − 1/4 − 1/3 = 5/12).',D='90 000 TL, 30 000’i kalanın 1/3’ü sanıp 3 ile çarpmak; 30 000 kalanın 2/3’ü.',E='120 000 TL, 30 000’i gelirin 1/4’ü sanmak.'),
 TT(A='dikkat',C='bilgi',D='islem',E='dikkat'))
k=Fr(120)/((1-Fr(2,5))*Fr(1,2)); assert k==400
assert Fr(120)/(1-Fr(2,5))==200 and 120*2==240 and Fr(120)/Fr(2,5)==300 and Fr(120)/(1-Fr(2,5)-Fr(1,2))==1200
P.K('0002','Bir okul kütüphanesine bağışlanan kitapların 2/5’i hemen raflara yerleştirilmiş, kalan kitapların yarısı da depoya kaldırılmıştır.\nGeriye etiketlenmeyi bekleyen 120 kitap kalmıştır.\nBuna göre kütüphaneye kaç kitap bağışlanmıştır?',
 ['200','240','300','400','1200'],'D','Bağışlanan kitap sayısı.',
 ['Raflara yerleştirildikten sonra kitapların kaçta kaçı kaldı?','Depoya kaldırıldıktan sonra kalanın kaçta kaçı kaldı?','120 kitap bütünün hangi kesri?'],[KALAN],
 [A('Raflardan sonra','2/5’i yerleşti.','kalan: 3/5'),
  A('Depodan sonra','Kalanın yarısı depoya, yarısı ortada.','3/5 × 1/2 = 3/10'),
  A('Bütünü bul','3/10 = 120 ⇒ 1/10 = 40.','10 × 40 = 400 kitap')],
 'Kalanın kesirleri art arda geliyorsa kalan kesirleri çarp; sonra parçadan bütüne geç.',
 dict(A='200, yalnızca ilk adımı geri almak (120 ÷ 3/5); depoya kaldırılanlar unutuldu.',B='240, yalnızca son adımı geri almak (120 × 2).',C='300, 120’yi rafa yerleşen kısmın (2/5) karşılığı sanmak.',E='1200, “kalanın yarısı”nı bütünün yarısı sanmak (1 − 2/5 − 1/2 = 1/10).'),
 TT(A='dikkat',B='dikkat',C='islem',E='bilgi'))

# ===== 0003 kalanın ORTA (ara parça)
S=Fr(36)/((1-Fr(1,3))*(1-Fr(1,4))*(1-Fr(2,5))); assert S==120
sab=S/3; ogl=(S-sab)/4; aks=(S-sab-ogl)*Fr(2,5); assert (sab,ogl,aks)==(40,20,24) and S-sab-ogl-aks==36 and sab+ogl+aks==84
P.R('0003','kes-kalanin',T['kes-kalanin'],'orta','Üç adımlı kalan','Ardışık üç “kalanın” kesrinden sonra kalan miktardan bütünü ve istenen ara parçayı bulur.','hikâyeli',3,
 'K-KES-01 (kalanın kesri) · üç adım, istenen ara parça (ilk teslimat), yeni kurgu (kargo aracı)',
 'Bir kargo aracı, sabah yüklediği paketlerin 1/3’ünü öğleden önce teslim etmiştir.\nÖğleden sonra kalan paketlerin 1/4’ünü, akşam saatlerinde de geriye kalan paketlerin 2/5’ini teslim etmiştir.\nGün sonunda araçta 36 paket kaldığına göre öğleden önce teslim edilen paket sayısı kaçtır?',
 ['20','24','40','84','120'],'C','Öğleden önce teslim edilen paket sayısı.',
 ['Her teslimattan sonra paketlerin kaçta kaçı kalıyor?','Kalan kesirleri çarpıp 36’nın bütünün hangi kesri olduğunu bul.','Bütünü bulunca ilk teslimatı hesapla.'],[KALAN],
 [A('Kalan kesirler','Her teslimattan sonra kalan kısım.','2/3 · 3/4 · 3/5'),
  A('Gün sonu kesri','Kalan kesirleri çarp.','2/3 × 3/4 × 3/5 = 3/10'),
  A('Bütün','3/10 = 36 ⇒ 1/10 = 12.','toplam 120 paket'),
  A('İlk teslimat','Paketlerin 1/3’ü.','120 ÷ 3 = 40 · kontrol: 120 → 80 → 60 → 36 ✓')],
 'Ara bir parçayı sorduklarında önce bütünü bul; sonra her adımda kalanı yazarak ilerle.',
 dict(A='20, öğleden sonra teslim edilen paket sayısı (80’in 1/4’ü).',B='24, akşam teslim edilen paket sayısı (60’ın 2/5’i).',D='84, gün içinde teslim edilen paketlerin toplamı.',E='120, sabah yüklenen paketlerin tamamı; soru ilk teslimatı soruyor.'),
 TT(A='dikkat',B='dikkat',D='dikkat',E='dikkat'))
S=Fr(80)/((1-Fr(1,4))*(1-Fr(2,9))*(1-Fr(3,7))); assert S==240
ilk=S/4; yaz=(S-ilk)*Fr(2,9); son=(S-ilk-yaz)*Fr(3,7); assert (ilk,yaz,son)==(60,40,60) and S-ilk==180 and ilk+yaz+son==160
P.K('0003','Bir fidanlıktaki fidanların 1/4’ü ilkbaharda satılmıştır.\nYazın kalan fidanların 2/9’u, sonbaharda da geriye kalanların 3/7’si satılmış ve fidanlıkta 80 fidan kalmıştır.\nBuna göre yazın kaç fidan satılmıştır?',
 ['40','60','160','180','240'],'A','Yazın satılan fidan sayısı.',
 ['Her satıştan sonra fidanların kaçta kaçı kalıyor?','Kalan kesirleri çarparak 80’in bütünün kaçta kaçı olduğunu bul.','Bütünü bulduktan sonra ilkbahar satışını çıkar, yaz satışını hesapla.'],[KALAN],
 [A('Kalan kesirler','Her satıştan sonra kalan kısım.','3/4 · 7/9 · 4/7'),
  A('Son kesir','Kalan kesirleri çarp.','3/4 × 7/9 × 4/7 = 1/3'),
  A('Bütün','1/3 = 80.','toplam 240 fidan'),
  A('Yaz satışı','İlkbahardan sonra 180 fidan kaldı.','180 × 2/9 = 40 · kontrol: 240 → 180 → 140 → 80 ✓')],
 'Ara adımı istenen sorularda her adımın “kalan”ını yazmak hatayı önler.',
 dict(B='60, ilkbaharda (ya da sonbaharda) satılan fidan sayısı.',C='160, üç mevsimde satılan fidanların toplamı.',D='180, ilkbahar satışından sonra kalan fidan sayısı.',E='240, fidanların tamamı.'),
 TT(B='dikkat',C='dikkat',D='dikkat',E='dikkat'))

# ===== 0004 dolu-boş ORTA
d=2400-1680; su=Fr(d)/Fr(2,5); assert d==720 and su==1800 and 2400-su==600 and Fr(720)/Fr(3,5)==1200
P.R('0004','kes-dolu',T['kes-dolu'],'orta','İçilen su','Dolu ve kısmen boşalmış kabın kütle farkından içindekinin tamamını bulur.','hikâyeli',3,
 'K-KES-03 (dolu–boş kap) · yeni kurgu (termos), istenen içindekinin tamamı',
 'Suyla tamamen dolu bir termosun kütlesi 2400 gramdır.\nTermostaki suyun 2/5’i içildikten sonra termosun kütlesi 1680 gram olarak ölçülmüştür.\nBuna göre termos tamamen doluyken içindeki su kaç gramdır?',
 ['600','720','1200','1800','2400'],'D','Termostaki suyun tamamının kütlesi.',
 ['İki tartım arasındaki fark neyin kütlesi?','Bu fark suyun hangi kesrine karşılık gelir?','Parçadan bütüne geç.'],[DOLU,PARCA],
 [A('Farkı bul','İki tartım arasındaki fark, içilen suyun kütlesidir.','2400 − 1680 = 720 g'),
  A('Kesirle eşle','İçilen su, suyun 2/5’i.','2/5 = 720 g ⇒ 1/5 = 360 g'),
  A('Suyun tamamı','5 parça.','5 × 360 = 1800 g · boş termos 2400 − 1800 = 600 g')],
 'İki tartımın farkı yalnızca eksilen kısmın kütlesidir; kabın kütlesi farkta yok olur.',
 dict(A='600 g, boş termosun kütlesi; soru suyun tamamını soruyor.',B='720 g, yalnızca içilen suyun kütlesi.',C='1200 g, 720 g’ı kalan suyun (3/5) karşılığı sanmak; 720 g içilen kısmın kütlesi.',E='2400 g, dolu termosun kütlesi; termosun kendi kütlesi de içinde.'),
 TT(A='dikkat',B='dikkat',C='dikkat',E='bilgi'))
d=1350-550; yag=Fr(d)/Fr(2,3); assert d==800 and yag==1200 and 1350-yag==150 and yag/3==400 and 1350-400==950
P.K('0004','Zeytinyağıyla tamamen dolu bir cam şişenin kütlesi 1350 gramdır.\nŞişedeki yağın bir kısmı kullanıldıktan sonra şişenin yalnızca 1/3’ü dolu kalmış ve şişenin kütlesi 550 gram olmuştur.\nBuna göre boş şişenin kütlesi kaç gramdır?',
 ['150','400','800','950','1200'],'A','Boş şişenin kütlesi.',
 ['Şişe tam doluyken 1/3’ü dolu kalana kadar yağın kaçta kaçı kullanıldı?','İki tartımın farkı bu kesre karşılık gelir.','Yağın tamamını bul, dolu şişeden çıkar.'],[DOLU,PARCA],
 [A('Kullanılan kesir','Doluluk 1’den 1/3’e indi.','1 − 1/3 = 2/3'),
  A('Farkla eşle','Kütle farkı kullanılan yağdır.','1350 − 550 = 800 g = 2/3 ⇒ 1/3 = 400 g'),
  A('Yağın tamamı','3 parça.','3 × 400 = 1200 g'),
  A('Boş şişe','Dolu şişeden yağı çıkar.','1350 − 1200 = 150 g')],
 'Önce içindekinin tamamını bul; boş kap = dolu kap − içindekinin tamamı.',
 dict(B='400 g, şişede kalan yağın (1/3) kütlesi.',C='800 g, kullanılan yağın kütlesi.',D='950 g, dolu şişeden yalnızca kalan 1/3’lük yağı çıkarmak.',E='1200 g, yağın tamamının kütlesi; soru boş şişeyi soruyor.'),
 TT(B='dikkat',C='dikkat',D='islem',E='dikkat'))

# ===== 0005 paylaştırma ORTA
a_=Fr(1,3); b_=(1-a_)*Fr(3,8); c_=1-a_-b_; assert b_==Fr(1,4) and c_==Fr(5,12) and c_-b_==Fr(1,6)
tot=Fr(10000)/(c_-b_); assert tot==60000 and (tot*a_,tot*b_,tot*c_)==(20000,15000,25000) and 20000+15000==35000
P.R('0005','kes-pay',T['kes-pay'],'orta','İki payın farkı','Bütünün ve kalanın kesirleriyle yapılan paylaştırmada iki pay arasındaki farktan bütünü bulur.','hikâyeli',4,
 'K-KES-04 (kesirle paylaştırma) · yeni kurgu (proje ödülü), iki payın farkı verildi',
 'Üç kişilik bir proje ekibi, bir yarışmadan kazandığı para ödülünü paylaşmıştır.\nÖdülün 1/3’ünü Ali, kalan paranın 3/8’ini Burak, geriye kalan paranın tamamını da Can almıştır.\nCan’ın aldığı para, Burak’ın aldığı paradan 10 000 TL fazla olduğuna göre para ödülü kaç TL’dir?',
 ['15 000','20 000','25 000','35 000','60 000'],'E','Para ödülünün tamamı.',
 ['Ali’den sonra ödülün kaçta kaçı kaldı?','Burak’ın payını ödülün tamamına göre kesirle yaz.','Can’ın kesrinden Burak’ın kesrini çıkar; bu fark 10 000 TL.'],[KALAN],
 [A('Ali’den sonra','Ali ödülün 1/3’ünü aldı.','kalan: 2/3'),
  A('Burak’ın kesri','Kalanın 3/8’i.','2/3 × 3/8 = 1/4'),
  A('Can’ın kesri','Geriye kalan.','1 − 1/3 − 1/4 = 5/12'),
  A('Farkı eşle','Can − Burak = 10 000 TL.','5/12 − 3/12 = 2/12 = 1/6 ⇒ ödül 6 × 10 000 = 60 000 TL')],
 'Her payı bütüne göre kesirle yaz; farklar ve toplamlar ancak o zaman doğrudan karşılaştırılır.',
 dict(A='15 000 TL, Burak’ın payı.',B='20 000 TL, Ali’nin payı.',C='25 000 TL, Can’ın payı.',D='35 000 TL, Ali ile Burak’ın paylarının toplamı.'),
 TT(A='dikkat',B='dikkat',C='dikkat',D='dikkat'))
s_=Fr(2,5); f_=(1-s_)*Fr(1,4); d_=1-s_-f_; assert f_==Fr(3,20) and d_==Fr(9,20) and d_-s_==Fr(1,20)
tot=Fr(400)/(d_-s_); assert tot==8000 and (tot*s_,tot*f_,tot*d_)==(3200,1200,3600) and tot*(1-s_)==4800
P.K('0005','Bir köy kooperatifi, topladığı fındığın 2/5’ini yurt dışına satmış, kalan fındığın 1/4’ünü bir fabrikaya göndermiş, geriye kalan fındığı da depoya koymuştur.\nDepoya konan fındık, yurt dışına satılan fındıktan 400 kg fazladır.\nBuna göre depoya konan fındık kaç kilogramdır?',
 ['1200','3200','3600','4800','8000'],'C','Depoya konan fındığın kütlesi.',
 ['Satıştan sonra fındığın kaçta kaçı kaldı?','Fabrikaya giden ve depoya konan kısımları bütüne göre kesirle yaz.','Depo ile satılan arasındaki kesir farkı 400 kg.'],[KALAN],
 [A('Satıştan sonra','2/5’i satıldı.','kalan: 3/5'),
  A('Fabrika ve depo','Fabrikaya kalanın 1/4’ü; depoya kalanın 3/4’ü.','fabrika 3/5 × 1/4 = 3/20 · depo 3/5 × 3/4 = 9/20'),
  A('Farkı eşle','Depo − satılan = 9/20 − 8/20 = 1/20.','1/20 = 400 kg ⇒ toplam 8000 kg'),
  A('Depodaki fındık','Toplamın 9/20’si.','8000 × 9/20 = 3600 kg')],
 'Farkı kurmadan önce bütün payları aynı paydada (bütüne göre) yaz.',
 dict(A='1200 kg, fabrikaya gönderilen fındık.',B='3200 kg, yurt dışına satılan fındık.',D='4800 kg, satıştan sonra kalan fındık; fabrikaya gönderilen de içinde.',E='8000 kg, toplanan fındığın tamamı.'),
 TT(A='dikkat',B='dikkat',D='dikkat',E='dikkat'))

# ===== 0006 parça ORTA
r=1-Fr(2,5)-Fr(1,3); assert r==Fr(4,15); tot=Fr(48)/r; assert tot==180 and tot*Fr(2,5)==72 and tot/3==60 and tot*Fr(3,5)==108 and 72+60==132
P.R('0006','kes-parca',T['kes-parca'],'orta','Kalan parçadan bir pay','Bütünün kesirleri dışında kalan miktardan bütünü bulup istenen parçayı hesaplar.','hikâyeli',3,
 'K-KES-02 (parçadan bütüne) · iki kesir ve kalan miktar, istenen bir parça (ilk raf), yeni kurgu (kitaplık)',
 'Arda, kitaplarının 2/5’ini kitaplığının ilk rafına, 1/3’ünü de ikinci rafına dizmiştir.\nGeriye kalan 48 kitabı ise üçüncü rafa yerleştirmiştir.\nBuna göre Arda ilk rafa kaç kitap dizmiştir?',
 ['60','72','108','132','180'],'B','İlk raftaki kitap sayısı.',
 ['İlk iki rafa kitapların toplam kaçta kaçı dizildi?','48 kitap kitapların hangi kesrine denk geliyor?','Kitapların tamamını bulup ilk rafın kesriyle çarp.'],[PARCA],
 [A('Kalan kesir','İki rafın kesirlerini topla, 1’den çıkar.','1 − 2/5 − 1/3 = 15/15 − 6/15 − 5/15 = 4/15'),
  A('Bütün','4/15 = 48 ⇒ 1/15 = 12.','15 × 12 = 180 kitap'),
  A('İlk raf','Kitapların 2/5’i.','180 × 2/5 = 72 kitap')],
 'Kesirler bütüne göre verildiyse toplanır; kalan kesir 1’den çıkarılarak bulunur.',
 dict(A='60, ikinci raftaki kitap sayısı.',C='108, ilk raftan sonra kalan kitaplar (180’in 3/5’i).',D='132, ilk iki raftaki kitapların toplamı.',E='180, kitapların tamamı; soru ilk rafı soruyor.'),
 TT(A='dikkat',C='dikkat',D='dikkat',E='dikkat'))
r=1-Fr(1,4)-Fr(2,5); assert r==Fr(7,20); tot=Fr(21)/r; assert tot==60 and tot/4==15 and tot*Fr(2,5)==24 and 15+24==39 and 60-15==45
P.K('0006','Bir otoparktaki araçların 1/4’ü beyaz, 2/5’i gri renklidir.\nOtoparkta geriye kalan 21 aracın hepsi siyahtır.\nBuna göre otoparkta kaç beyaz araç vardır?',
 ['15','24','39','45','60'],'A','Beyaz araçların sayısı.',
 ['Beyaz ve gri araçlar birlikte kaçta kaç?','21 siyah araç, araçların hangi kesri?','Toplam aracı bulup beyazların kesriyle çarp.'],[PARCA],
 [A('Siyahların kesri','Beyaz ve gri kesirlerini topla, 1’den çıkar.','1 − 1/4 − 2/5 = 20/20 − 5/20 − 8/20 = 7/20'),
  A('Toplam araç','7/20 = 21 ⇒ 1/20 = 3.','20 × 3 = 60 araç'),
  A('Beyaz araçlar','Araçların 1/4’ü.','60 ÷ 4 = 15')],
 'Bütünün kesirleri verildiğinde önce eksik kesri bul; verilen sayıyı ona eşle.',
 dict(B='24, gri araç sayısı.',C='39, beyaz ve gri araçların toplamı.',D='45, beyaz olmayan araçların sayısı.',E='60, otoparktaki araçların tamamı.'),
 TT(B='dikkat',C='dikkat',D='dikkat',E='dikkat'))

# ===== 0007 süreç ZOR (sondan başa)
def ileri(S,f,a,n):
    x=Fr(S); L=[]
    for _ in range(n): x=x*(1-f)+a; L.append(x)
    return L
assert ileri(510,Fr(1,3),80,3)==[420,360,320]
geri=Fr(320)
for _ in range(3): geri=(geri-80)/(1-Fr(1,3))
assert geri==510
yanlis=Fr(320)
for _ in range(3): yanlis=yanlis/(1-Fr(1,3))-80
eksiz=Fr(320)/(1-Fr(1,3))**3; assert yanlis==700 and eksiz==1080
P.R('0007','kes-surec',T['kes-surec'],'zor','Kullanım ve ekleme','Her gün mevcut miktarın kesri kullanılıp sabit miktar eklenen süreçte son durumdan geriye giderek başlangıç miktarını bulur.','hikâyeli',4,
 'K-KES-05 (tekrarlı süreç, sondan başa) · yeni kurgu (barınak maması), her gün kesirle kullanım ve sabit bağış',
 'Bir hayvan barınağında, her sabah o anda depoda bulunan mamanın 1/3’ü kullanılmakta, her akşam da depoya 80 kg mama bağışlanmaktadır.\nBu düzen 3 gün sürmüş ve 3. günün akşamı bağış geldikten sonra depoda 320 kg mama olmuştur.\n1. günün sabahı mama kullanılmadan önce depoda kaç kilogram mama vardır?',
 ['360','420','510','700','1080'],'C','1. günün sabahındaki mama miktarı.',
 ['Son günden başla: bağış gelmeden önce depoda ne kadar mama vardı?','O miktar, sabahki mamanın kaçta kaçıdır?','Aynı iki geri adımı her gün için tekrarla.'],[GERI],
 [A('3. gün','Bağışı geri al, sonra 2/3’e böl.','320 − 80 = 240 · 240 ÷ 2/3 = 360'),
  A('2. gün','2. günün akşamı depoda 360 kg vardı.','360 − 80 = 280 · 280 ÷ 2/3 = 420'),
  A('1. gün','1. günün akşamı depoda 420 kg vardı.','420 − 80 = 340 · 340 ÷ 2/3 = 510'),
  A('Kontrol','İleri doğru hesapla.','510 → 340 + 80 = 420 → 280 + 80 = 360 → 240 + 80 = 320 ✓')],
 'Sondan başa çözümde son yapılan işlemi ilk geri al; her adımda önce ekleneni çıkar, sonra kesre böl.',
 dict(A='360 kg, 2. günün akşamındaki mama; bir gün daha geri gidilmeli.',B='420 kg, 1. günün akşamındaki mama; başlangıç değil.',D='700 kg, geri dönerken işlem sırasını karıştırmak (önce 2/3’e bölüp sonra 80 çıkarmak).',E='1080 kg, bağışları hesaba katmadan yalnızca 2/3’e üç kez bölmek.'),
 TT(A='dikkat',B='dikkat',D='islem',E='bilgi'))
assert ileri(2600,Fr(1,2),100,3)==[1400,800,500]
g=[Fr(500)]
for _ in range(3): g.append((g[-1]-100)*2)
assert g==[500,800,1400,2600]
y=[Fr(500)]
for _ in range(2): y.append(y[-1]*2-100)
e=Fr(500)*4; assert y[-1]==1700 and e==2000
P.K('0007','Bir kitap fuarındaki bir standda, her gün o gün başında standda bulunan kitapların yarısı satılmakta, gün sonunda da standa depodan 100 kitap getirilmektedir.\nFuarın 3. gününün sonunda, depodan kitaplar getirildikten sonra standda 500 kitap olmuştur.\nBuna göre 1. günün sonunda, depodan kitaplar getirildikten sonra standda kaç kitap vardır?',
 ['800','1400','1700','2000','2600'],'B','1. gün sonundaki kitap sayısı.',
 ['3. günün sonundan başla: kitaplar getirilmeden önce standda kaç kitap vardı?','Satıştan sonra kalan, gün başındakinin yarısıdır.','Kaç gün geri gitmen gerektiğini kontrol et.'],[GERI],
 [A('3. gün','Getirileni çıkar, yarıya bölmenin tersi olarak 2 ile çarp.','500 − 100 = 400 · 400 × 2 = 800'),
  A('2. gün','2. günün sonunda 800 kitap vardı.','800 − 100 = 700 · 700 × 2 = 1400'),
  A('İstenen an','2. günün başı, 1. günün sonudur.','1. gün sonu: 1400 kitap'),
  A('Kontrol','İleri doğru: 1400’ün yarısı 700, +100 = 800; 800’ün yarısı 400, +100 = 500 ✓','1400 → 800 → 500')],
 'Sondan başa çözümde istenen anı zaman çizelgesinde işaretle: 1. günün sonu = 2. günün başı.',
 dict(A='800, 2. günün sonundaki kitap sayısı; bir gün daha geri gidilmeli.',C='1700, geri dönerken işlem sırasını karıştırmak (önce 2 ile çarpıp sonra 100 çıkarmak).',D='2000, depodan gelen kitapları hesaba katmadan 2 ile iki kez çarpmak.',E='2600, fuarın başındaki kitap sayısı; soru 1. günün sonunu soruyor.'),
 TT(A='dikkat',C='islem',D='bilgi',E='dikkat'))

# ===== 0008 paylaştırma ZOR
a_=Fr(1,4); b_=(1-a_)*Fr(2,5); c_=1-a_-b_; assert b_==Fr(3,10) and c_==Fr(9,20) and (a_+b_)-c_==Fr(1,10)
tot=Fr(18000)/Fr(1,10); assert tot==180000 and (tot*a_,tot*b_,tot*c_)==(45000,54000,81000) and 45000+54000==99000
yb=Fr(2,5); yc=1-a_-yb; yt=Fr(18000)/((a_+yb)-yc); assert yt==60000 and yt*yc==21000
P.R('0008','kes-pay',T['kes-pay'],'zor','Pay ile toplamın farkı','Kalanın kesriyle yapılan paylaştırmada bir payın diğer iki payın toplamından farkını kullanarak istenen payı bulur.','hikâyeli',4,
 'K-KES-04 (kesirle paylaştırma) · fark, bir pay ile iki payın toplamı arasında; yeni kurgu (yıl sonu primi)',
 'Bir şirket, yıl sonu primi için ayırdığı paranın 1/4’ünü satış bölümüne, kalan paranın 2/5’ini üretim bölümüne, geriye kalanın tamamını da teknik bölüme vermiştir.\nTeknik bölüme verilen para, satış ve üretim bölümlerine verilen paraların toplamından 18 000 TL azdır.\nBuna göre teknik bölüme kaç TL prim verilmiştir?',
 ['21 000','45 000','54 000','81 000','99 000'],'D','Teknik bölümün aldığı prim.',
 ['Satış bölümünden sonra paranın kaçta kaçı kaldı?','Üretim bölümünün payını bütüne göre kesirle yaz; teknik bölümün kesrini bul.','Satış + üretim kesrinden teknik kesrini çıkar; bu fark 18 000 TL.'],[KALAN],
 [A('Satıştan sonra','1/4 satış bölümüne.','kalan: 3/4'),
  A('Üretim','Kalanın 2/5’i.','3/4 × 2/5 = 3/10'),
  A('Teknik','Geriye kalan.','1 − 1/4 − 3/10 = 9/20'),
  A('Farkı eşle','Satış + üretim = 5/20 + 6/20 = 11/20.','11/20 − 9/20 = 1/10 = 18 000 ⇒ toplam 180 000 TL'),
  A('Teknik bölüm','Toplamın 9/20’si.','180 000 × 9/20 = 81 000 TL')],
 'Kalanın kesrini bütüne çevirmeden fark kurma; bütün paylar aynı bütüne göre yazılmalı.',
 dict(A='21 000 TL, “kalanın 2/5’i”ni bütünün 2/5’i sanmak (teknik 7/20, toplam 60 000).',B='45 000 TL, satış bölümünün primi.',C='54 000 TL, üretim bölümünün primi.',E='99 000 TL, satış ve üretim bölümlerinin toplamı.'),
 TT(A='bilgi',B='dikkat',C='dikkat',E='dikkat'))
o_=Fr(1,3); k_=(1-o_)*Fr(3,5); d_=1-o_-k_; assert k_==Fr(2,5) and d_==Fr(4,15) and o_-d_==Fr(1,15)
tot=Fr(2400)/(o_-d_); assert tot==36000 and (tot*o_,tot*k_,tot*d_)==(12000,14400,9600) and tot*(1-o_)==24000
P.K('0008','Bir yayınevi bastığı kitapların 1/3’ünü okullara, kalan kitapların 3/5’ini kitapçılara göndermiş, geriye kalan kitapları da depoda tutmuştur.\nOkullara gönderilen kitap sayısı, depoda tutulan kitap sayısından 2400 fazladır.\nBuna göre yayınevi kaç kitap basmıştır?',
 ['9600','12 000','14 400','24 000','36 000'],'E','Basılan kitapların sayısı.',
 ['Okullara gönderildikten sonra kitapların kaçta kaçı kaldı?','Kitapçılara giden ve depoda kalan kısımları bütüne göre kesirle yaz.','Okul ile depo kesirlerinin farkı 2400 kitap.'],[KALAN],
 [A('Okullardan sonra','1/3 okullara.','kalan: 2/3'),
  A('Kitapçılar','Kalanın 3/5’i.','2/3 × 3/5 = 2/5'),
  A('Depo','Geriye kalan.','1 − 1/3 − 2/5 = 4/15'),
  A('Farkı eşle','Okul − depo = 5/15 − 4/15 = 1/15.','1/15 = 2400 ⇒ 15 × 2400 = 36 000 kitap')],
 'Paylar aynı paydaya getirilince farklar doğrudan bütünün bir kesri olur.',
 dict(A='9600, depoda tutulan kitap sayısı.',B='12 000, okullara gönderilen kitap sayısı.',C='14 400, kitapçılara gönderilen kitap sayısı.',D='24 000, okullara gönderildikten sonra kalan kitaplar.'),
 TT(A='dikkat',B='dikkat',C='dikkat',D='dikkat'))

P.yaz(os.path.join(H,'kesirprob-1.json'),os.path.join(H,'kesirprob-1-kardes.json'))
