"""Kâr Zarar Problemleri · parti 2 (hafif mod): 24 ana soru, kardeş yok, ipucu 1. Her cevap ve çeldirici kodla doğrulanır."""
import sys,os,itertools
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_mat as H
from _hafif_mat import *
H.KONU='Kâr Zarar Problemleri'
UK='prob|Kar Zarar Problemleri'
P=Parti('karzarariki','Kâr Zarar Problemleri',UK)
F=Fr
KAR=B('Kâr ve zarar yüzdesi','aksi söylenmedikçe alış (maliyet) fiyatına göre hesaplanır; kâr = satış − alış. Örnek: 200 TL’ye alınıp 250 TL’ye satılan ürünün kârı 50 TL, kâr yüzdesi 50/200 = %25’tir')
SAT=B('Satış fiyatı','kârda satış = alış × (1 + p/100), zararda satış = alış × (1 − p/100). Örnek: 500 TL’lik ürün %20 zararla 500 × 0,8 = 400 TL’ye satılır')
IND=B('İndirim','indirim etiket fiyatı üzerinden hesaplanır: indirimli fiyat = etiket × (1 − p/100). Örnek: 800 TL etiketli ürüne %25 indirim yapılırsa 800 × 0,75 = 600 TL ödenir')
ARD=B('Ardışık indirim','ikinci indirim, birinci indirimli fiyat üzerinden yapılır; yüzdeler toplanmaz, çarpanlar çarpılır. Örnek: önce %20, sonra %10 indirim → 0,8 × 0,9 = 0,72 (toplam %28 indirim)')
SATORAN=B('Satış fiyatına göre oran','“kâr, satış fiyatının %20’si” denirse kâr = 0,2 × satış ve alış = 0,8 × satış olur; “kâr, alışın %20’si” denirse satış = 1,2 × alış olur. Örnek: satış 100 TL ise birincide alış 80 TL, ikincide alış 100/1,2 TL’dir')
KAMP=B('Kampanya hesabı','kampanya gruplarını sayıp ödenecek ürün sayısını bul. Örnek: “3 al 2 öde”de 6 ürün alan 4 ürün bedeli öder; “ikincisi %50” kampanyasında 2 ürünün bedeli 1 + 0,5 = 1,5 ürün bedelidir')
TAK=B('Taksitli satış','taksitli toplam ödeme = peşin fiyat + vade farkı; aylık taksit = toplam ÷ taksit sayısı. Örnek: peşin 1000 TL, %20 vade farkı, 5 taksit → 1200 ÷ 5 = 240 TL')
FIRE=B('Satılamayan mal','alış bedeli, satın alınan tüm mal için ödenmiştir; kâr hesabında satılamayan malın bedeli de maliyete dahildir. Örnek: 100 adet 5 TL’den alınıp 10’u satılamazsa maliyet 500 TL, satılan adet 90’dır')
KY='ÖSYM 2018–2026 TYT Matematik (kâr–zarar, yüzde problemleri) · yayın soru bankaları (yalnız mantık) · MEB 7–9. sınıf yüzde ve oran'
kart('K-KZB-01','Maliyet, satış ve kâr/zarar yüzdesi','Alış, satış ve kâr/zarar arasındaki ilişkiyle bilinmeyen değer ve yüzde bulunur.','Kâr yüzdesini satışa göre hesaplamak; kâr tutarı ile satış fiyatını karıştırmak.','kolay','hikâyeli',3,'kzb-temel','Alış, satış, kâr ve zarar yüzdesi',KY)
kart('K-KZB-02','Etiket, indirim ve kâr','Etiket fiyatı üzerinden yapılan indirimle satış fiyatı bulunur, alış fiyatıyla karşılaştırılır; maliyetine satış sınırı sorulur.','İndirim ve kâr yüzdesini birbirinden çıkarmak; yüzdeyi farklı fiyata göre almak.','orta','hikâyeli',3,'kzb-etiket','Etiket fiyatı, indirim ve kâr',KY)
kart('K-KZB-03','Kampanya ve taksit','“3 al 2 öde”, “ikincisi %50” kampanyaları ve taksitli satışta vade farkı ile kâr hesaplanır.','Kampanya gruplarını yanlış saymak; ikinci ürünü bedava sanmak; vade farkını kâr sanmak.','orta','hikâyeli',3,'kzb-kampanya','Kampanya ve taksit',KY)
kart('K-KZB-04','İki ürün, biri kârla biri zararla','İki ürünün toplam sonucu, tek tek alış ve satışları bulunarak değerlendirilir; denklem kurulur.','Eşit yüzdeleri birbirini götürür sanmak; yüzdeleri aynı fiyata göre almak.','orta','hikâyeli',3,'kzb-ikiurun','İki ürün: kâr ve zarar birlikte',KY)
kart('K-KZB-05','Toplu alım, fire ve parça satış','Toplu alınan malın bir kısmı satılamaz ya da farklı fiyatlardan satılır; toplam maliyete göre kâr/hedef fiyat bulunur.','Satılamayan malı maliyete katmamak; ortalama alınan fiyatı yanlış ağırlıklandırmak.','orta','hikâyeli',4,'kzb-toplu','Toplu alım, fire ve parça satış',KY)
kart('K-KZB-06','Satış fiyatına göre kâr / zincir kârı','Kârın satış fiyatına oranı ile alış fiyatına oranı ayrılır; ardışık kâr zincirleri çözülür.','“Satışın %20’si” ile “alışın %20’si” ifadelerini karıştırmak.','zor','hikâyeli',4,'kzb-oran','Kârın hangi fiyata göre verildiği',KY)
kart('K-KZB-07','Yeni nesil ve öncüllü kâr-zarar','Tanımlanan bir kâr payı ya da kademeli indirim kuralı uygulanır; öncüller etiket–alış ilişkisiyle sınanır.','Tanımdaki oranın hangi fiyata göre olduğunu kaçırmak; kademeleri tüm tutara uygulamak.','zor','yeni nesil',4,'kzb-yeninesil','Yeni nesil ve öncüllü kâr-zarar',KY)

def q(no,tipId,tip,z,alt,kaz,kalip,kart,metin,dogru,yan,istenen,ip,bilgi,ad,puf,sira=None,kisa=None):
    ok=len(ad)
    assert (z=='zor' and ok>=4) or (z!='zor' and ok>=3),(no,ok)
    mk(P,no,tipId=tipId,tip=tip,z=z,alt=alt,kaz=kaz,kalip=kalip,adim=ok,kart=kart,metin=metin,dogru=dogru,yan=yan,istenen=istenen,ip=ip,bilgi=bilgi,ad=ad,puf=puf,sira=sira,kisa=kisa)

# 0001 kolay · kâr yüzdesi
a,s=24,30; assert F(s-a,a)==F(1,4) and F(s-a,s)==F(1,5) and F(s,a)==F(5,4) and F(a,s)==F(4,5) and s-a==6
q('0001','kzb-temel','Alış, satış, kâr ve zarar yüzdesi','kolay','Kâr Yüzdesi','Alış ve satış fiyatından kâr yüzdesini bulur.','hikâyeli','K-KZB-01 (alış–satış → kâr yüzdesi) · market, makarna',
 'Bir market, tanesini 24 TL’ye aldığı makarnayı 30 TL’ye satmaktadır.\nBuna göre marketin bu satıştaki kâr yüzdesi kaçtır?',
 25,[(20,'Kârı (6 TL) satış fiyatına (30 TL) bölmüş. Kâr yüzdesi alış fiyatına göredir.','bilgi'),(6,'Kâr tutarını (6 TL) yüzde olarak yazmış.','dikkat'),(80,'Alış fiyatını satış fiyatına bölüp (24/30) bunu kâr yüzdesi sanmış.','bilgi'),(125,'Satış fiyatını alışa bölüp (30/24) kâr yüzdesi sanmış; satışın alışa oranı 125’tir, kâr 25 puandır.','islem')],
 'Marketin kâr yüzdesi.',['Kâr yüzdesi hangi fiyata göre hesaplanır? Önce kârın kaç TL olduğunu bul.'],[KAR],
 [A('Kârı bul','Kâr, satış fiyatı ile alış fiyatı arasındaki farktır.','30 − 24 = 6 TL'),A('Alışa oranla','Kâr yüzdesi alış fiyatına göre bulunur.','6/24 = 1/4'),A('Yüzdeye çevir','Kesri yüzde olarak yaz.','1/4 = %25')],
 'Kâr yüzdesini bulurken kârı her zaman alış fiyatına böl.')

# 0002 kolay · zarar
sat=1260; al=F(sat)/F(9,10); zr=al-sat; assert al==1400 and zr==140 and sat*F(1,10)==126 and sat*F(9,10)==1134 and sat*F(11,10)==1386
q('0002','kzb-temel','Alış, satış, kâr ve zarar yüzdesi','kolay','Zarar Tutarı','Zarar yüzdesi ve satış fiyatından alış fiyatını ve zarar tutarını bulur.','hikâyeli','K-KZB-01 (zarar yüzdesi, satıştan zarar) · ütü',
 'Bir elektrikli ev aletleri mağazası, bir ütüyü %10 zararla 1260 TL’ye satmıştır.\nBuna göre mağaza bu satıştan kaç TL zarar etmiştir?',
 140,[(126,'1260’ın %10’unu almış; zarar yüzdesi alış fiyatına göredir, satış fiyatına göre değil.','bilgi'),(1134,'Satıştan %10 düşüp (1260 − 126) alışı satıştan küçük sanmış; zararda alış, satıştan büyüktür.','bilgi'),(1386,'1260’a %10 ekleyip alış fiyatı sanmış; alış, satışın 1/0,9 katıdır.','islem'),(1400,'Alış fiyatını (1400 TL) bulup zararı hesaplamayı unutmuş.','dikkat')],
 'Mağazanın zararı (TL).',['Satış fiyatı, alış fiyatının yüzde kaçıdır? Önce alış fiyatını bul.'],[SAT,KAR],
 [A('Satışı alışla yaz','Alış x olsun; %10 zararla satış alışın %90’ıdır.','0,9 × x = 1260'),A('Alışı bul','Denklemi çöz.','x = 1260 ÷ 0,9 = 1400 TL'),A('Zararı bul','Zarar, alış ile satış farkıdır.','1400 − 1260 = 140 TL')],
 'Zararda satış, alışın (100 − p) yüzdesidir; alışı bulmadan zarar tutarı bulunmaz.')

# 0003 kolay · hedef kâr
al=1500; kr=al*F(1,5); assert al+kr==1800 and kr==300 and al*F(4,5)==1200 and F(al)/F(4,5)==1875 and al+2*kr==2100
q('0003','kzb-temel','Alış, satış, kâr ve zarar yüzdesi','kolay','Hedef Kâr','Alış fiyatı ve kâr yüzdesinden satış fiyatını bulur.','hikâyeli','K-KZB-01 (hedef kâr → satış fiyatı) · ahşap masa',
 'Bir atölye, maliyeti 1500 TL olan bir ahşap masayı maliyetinin %20’si kadar kârla satmak istemektedir.\nBuna göre masanın satış fiyatı kaç TL olmalıdır?',
 1800,[(300,'Yalnızca kârı (300 TL) bulup satış fiyatı sanmış.','dikkat'),(1200,'Maliyetin %80’ini almış; kârda satış fiyatı maliyetten büyüktür.','bilgi'),(1875,'Maliyeti 0,8’e bölmüş; kârı satış fiyatının %20’si saymış. Soruda kâr maliyete göredir.','bilgi'),(2100,'Kârı iki kez ekleyerek 1500 + 300 + 300 bulmuş.','islem')],
 'Masanın satış fiyatı (TL).',['Kâr yüzdesi hangi fiyata göre verilmiş? Önce kâr tutarını TL olarak bul.'],[KAR,SAT],
 [A('Kâr tutarını bul','Kâr maliyetin %20’sidir.','1500 × 0,2 = 300 TL'),A('Satışa ekle','Satış = maliyet + kâr.','1500 + 300 = 1800 TL'),A('Kontrol','Satış maliyetin %120’sidir.','1500 × 1,2 = 1800 ✓')],
 'Kâr maliyetin yüzdesi olarak verilmişse satış = maliyet × (1 + p/100) yazılır.')

# 0004 kolay · 3 al 2 öde
fy=48; n=10; ode=(n//3)*2+(n%3); assert ode==7 and ode*fy==336 and n*fy==480 and F(n*2,3)*fy==F(960,3)*1 and (n-2)*fy==384 and (n//3)*2*fy==288
q('0004','kzb-kampanya','Kampanya ve taksit','kolay','Üç Al İki Öde','“3 al 2 öde” kampanyasında ödenecek tutarı bulur.','hikâyeli','K-KZB-03 (3 al 2 öde) · bisküvi, 10 paket',
 'Bir markette tanesi 48 TL olan bisküvi paketlerinde “3 al 2 öde” kampanyası vardır. Kampanya her üçlü grup için ayrı ayrı geçerlidir; üçlü grubu tamamlamayan paketler için indirim yoktur.\nBuna göre bu marketten 10 paket bisküvi alan bir müşteri toplam kaç TL öder?',
 336,[(288,'Kalan 1 paketi unutup yalnızca 3 grubun bedelini (6 paket) ödemiş.','dikkat'),(320,'Kampanyayı 10 pakete orantılı uygulayıp 10 × 2/3 paket saymış; gruplar tam sayıdır.','bilgi'),(384,'Yalnız 2 tam grup görüp (10 = 3 + 3 + 4) 2 × 2 + 4 = 8 paket bedeli ödemiş.','dikkat'),(480,'Kampanyayı hiç uygulamamış (10 × 48).','dikkat')],
 'Müşterinin ödeyeceği toplam tutar (TL).',['10 paketin kaçı üçlü gruplara girer? Her gruptan ve kalandan kaç paketin parası ödenir?'],[KAMP],
 [A('Grupları say','10 = 3 + 3 + 3 + 1; üç tam grup vardır.','3 grup + 1 paket'),A('Ödenen paketi bul','Her grupta 2 paket, kalan 1 paket ücretlidir.','3 × 2 + 1 = 7 paket'),A('Tutarı hesapla','Ödenen paket sayısı × fiyat.','7 × 48 = 336 TL')],
 'Kampanyalarda önce tam grupları say; kalan ürünler tam fiyattan ödenir.')

# 0005 kolay · taksit
pes=12000; tot=pes*F(115,100); tk=tot/6; assert tot==13800 and tk==2300 and F(pes,6)==2000 and pes*F(15,100)/6==300 and 2000+1800==3800 and pes*F(15,100)==1800
q('0005','kzb-kampanya','Kampanya ve taksit','kolay','Taksit Tutarı','Peşin fiyata vade farkı ekleyerek aylık taksit tutarını bulur.','hikâyeli','K-KZB-03 (peşin–taksit farkı) · çamaşır makinesi',
 'Peşin fiyatı 12 000 TL olan bir çamaşır makinesi, taksitli satışta peşin fiyatın %15 fazlasına 6 eşit taksitle satılmaktadır.\nBuna göre aylık taksit tutarı kaç TL’dir?',
 2300,[(300,'Yalnız vade farkını (1800 TL) taksit sayısına bölmüş.','dikkat'),(3800,'Vade farkının tamamını (1800 TL) her taksite eklemiş: 2000 + 1800.','islem'),(1800,'Vade farkını (peşin fiyatın %15’i) taksit tutarı sanmış.','dikkat'),(2000,'Peşin fiyatı 6’ya bölmüş; vade farkını eklememiş.','dikkat')],
 'Aylık taksit tutarı (TL).',['Taksitli satışta toplam ödenecek tutar peşin fiyatın kaç katıdır?'],[TAK],
 [A('Toplam ödemeyi bul','Taksitli fiyat peşin fiyatın %115’idir.','12 000 × 1,15 = 13 800 TL'),A('Taksitlere böl','6 eşit taksit.','13 800 ÷ 6 = 2300 TL'),A('Kontrol','6 taksit toplamı vade farkıyla peşini verir.','6 × 2300 = 13 800 = 12 000 + 1800 ✓')],
 'Vade farkı peşin fiyata eklenir, toplam taksit sayısına bölünür.')

# 0006 orta · maliyetine satış
e=F(5,4); d=1-1/e; assert d==F(1,5) and e*(1-d)==1 and 1/e==F(4,5)
q('0006','kzb-etiket','Etiket fiyatı, indirim ve kâr','orta','Maliyetine Satış','Etiket fiyatının alıştan fazlalığı verilen ürün için maliyetine satış indirimini bulur.','hikâyeli','K-KZB-02 (maliyetine satış sınırı) · etiket %25 fazla',
 'Bir mağaza, bir ürünün etiket fiyatını alış fiyatının %25 fazlası olarak belirlemiştir.\nMağaza bu ürünü etiket fiyatı üzerinden yüzde kaç indirimle satarsa ürünü maliyetine satmış olur?',
 20,[(25,'İndirim yüzdesini etiketteki fazlalık yüzdesine eşit sanmış; indirim etiket fiyatına göredir.','bilgi'),(75,'Etiketin %25 fazla olmasından alışın etiketin %75’i olduğunu çıkarmış.','bilgi'),(80,'Alışın etiketin %80’i olduğunu bulup 80’i indirim yüzdesi sanmış.','dikkat'),(125,'Etiketin alışa oranı olan %125’i indirim yüzdesi sanmış.','dikkat')],
 'Maliyetine satış için gereken indirim yüzdesi.',['Alış fiyatına bir değer ver (örneğin 100 TL) ve etiketi bu değerden hesapla. İndirim hangi fiyata göre yüzde olarak alınıyor?'],[IND,SAT],
 [A('Fiyatları yaz','Alış 100 TL ise etiket 125 TL.','alış = 100 · etiket = 125'),A('Satışı alışa eşitle','Maliyetine satış: satış fiyatı alışa eşit.','satış = 100 TL'),A('İndirimi hesapla','İndirim etiket fiyatına oranlanır.','(125 − 100)/125 = 25/125 = 1/5 = %20')],
 'İndirim her zaman etiket fiyatına göre hesaplanır; alış fiyatına bir değer vererek çarpanları somutlaştır.')

# 0007 orta · ardışık indirim ve kâr
alis=2500; et=5000; s1=et*F(4,5); s2=s1*F(85,100); kar=s2-alis; assert s1==4000 and s2==3400 and kar==900 and F(kar,alis)==F(36,100)
assert (1-F(4,5)*F(85,100))==F(32,100) and F(kar,alis)*100==36 and (s1-alis)/alis==F(3,5) and et/alis-1==1
q('0007','kzb-etiket','Etiket fiyatı, indirim ve kâr','orta','İki İndirim ve Kâr','Etiket fiyatına ardışık iki indirim uygulanan ürünün kâr yüzdesini bulur.','hikâyeli','K-KZB-02 (ardışık indirim → kâr yüzdesi) · tablet',
 'Alış fiyatı 2500 TL, etiket fiyatı 5000 TL olan bir tablet bilgisayara mağaza önce %20 indirim yapmıştır. Daha sonra kasada, indirimli fiyat üzerinden ayrıca %15 indirim uygulanmıştır.\nBuna göre mağaza bu satıştan yüzde kaç kâr etmiştir?',
 36,[(32,'Toplam indirimi (%32) hesaplayıp kâr yüzdesi sanmış.','dikkat'),(35,'İki indirim yüzdesini toplayıp (20 + 15) bunu kâr yüzdesi sanmış.','islem'),(60,'Yalnız ilk indirimi uygulamış: 4000 − 2500 = 1500, kâr %60.','dikkat'),(100,'Etiketin alışa göre fazlalığını (%100) kâr yüzdesi sanmış.','dikkat')],
 'Mağazanın kâr yüzdesi.',['İkinci indirimin hangi fiyat üzerinden yapıldığına dikkat et; son satış fiyatını bulduktan sonra alışla karşılaştır.'],[IND,ARD,KAR],
 [A('İlk indirim','Etiketin %80’i.','5000 × 0,8 = 4000 TL'),A('İkinci indirim','İndirimli fiyatın %85’i.','4000 × 0,85 = 3400 TL'),A('Kârı bul','Satış − alış.','3400 − 2500 = 900 TL'),A('Yüzdeye çevir','Kâr alışa oranlanır.','900/2500 = 0,36 = %36')],
 'Ardışık indirimlerde her indirim bir önceki fiyat üzerinden yapılır; kâr yüzdesi son satış fiyatıyla alıştan bulunur.')

# 0008 orta · iki ürün eşit satış
S=1200; a1=F(S)/F(6,5); a2=F(S)/F(4,5); assert (a1,a2)==(1000,1500) and 2*S-(a1+a2)==-100
assert F(2*S*4,100)==96 and S*F(1,5)==240 and S-a1==200 and a2-S==300
q('0008','kzb-ikiurun','İki ürün: kâr ve zarar birlikte','orta','Eşit Satış Fiyatı','İki ürünü eşit fiyata biri kârla biri zararla satan satıcının toplam sonucunu bulur.','hikâyeli','K-KZB-04 (aynı satış, %20 kâr–%20 zarar) · ikinci el saat',
 'İkinci el eşya alım satımı yapan bir satıcı, iki saatin her birini 1200 TL’ye satmıştır. Saatlerden birini %20 kârla, diğerini %20 zararla sattığına göre satıcı bu iki satıştan toplam kaç TL zarar etmiştir?',
 100,[(96,'Kâr–zarar farkı %4 diye ezberleyip alış toplamı (2500) yerine satış toplamının (2400) %4’ünü almış.','bilgi'),(200,'Yalnız kârlı satıştaki kârı (200 TL) zarar sanmış.','dikkat'),(240,'Satış fiyatının %20’sini (240 TL) toplam zarar sanmış.','bilgi'),(300,'Yalnız zararlı satıştaki zararı (300 TL) bulup bırakmış.','dikkat')],
 'Satıcının toplam zararı (TL).',['Her saatin alış fiyatını satıştan ayrı ayrı hesapla.'],[SAT,KAR],
 [A('Kârlı saatin alışı','Satış, alışın %120’si.','1,2 × x = 1200 → x = 1000 TL'),A('Zararlı saatin alışı','Satış, alışın %80’i.','0,8 × y = 1200 → y = 1500 TL'),A('Toplamları karşılaştır','Alış toplamı ile satış toplamı.','alış: 1000 + 1500 = 2500 · satış: 2 × 1200 = 2400'),A('Sonucu yaz','Alış satıştan fazla.','2500 − 2400 = 100 TL zarar')],
 'Aynı satış fiyatıyla eşit yüzdede kâr ve zarar, alışlar farklı olduğu için sonuçta zarar bırakır.')

# 0009 orta · yumurta fire hedef kâr
n,pf,fire=400,6,80; mal=n*pf; hedef=mal*F(120,100); fy=hedef/(n-fire)
assert mal==2400 and hedef==2880 and fy==9
assert F(pf*120,100)==F(36,5) and pf*F(140,100)==F(42,5) and F(36,5)*F(120,100)==F(216,25) and F(mal)/F(8,10)/(n-fire)==F(75,8)
q('0009','kzb-toplu','Toplu alım, fire ve parça satış','orta','Fire ve Hedef Kâr','Satılamayan mal olduğunda hedef kâr için satış fiyatını bulur.','hikâyeli','K-KZB-05 (toplu alım, kırık mal, hedef kâr) · yumurta',
 'Bir market, tanesini 6 TL’den 400 yumurta satın almıştır. Yumurtalardan 80’i kırıldığı için satılamamıştır. Market, sağlam kalan yumurtaların hepsini aynı fiyattan satacak ve yumurtalara ödediği paranın tamamına göre %20 kâr elde etmek istemektedir.\nBuna göre bir yumurta kaç TL’ye satılmalıdır?',
 9,[(F(36,5),'Kırık yumurtaları hesaba katmamış; 6 × 1,2 = 7,2 TL bulmuş.','dikkat'),(F(42,5),'Kırık yüzdesini (%20) kâr yüzdesine (%20) ekleyip %40 kâr hesaplamış: 6 × 1,4 = 8,4.','islem'),(F(216,25),'7,2 TL’ye ayrıca %20 kırık payı eklemiş: 7,2 × 1,2 = 8,64.','islem'),(F(75,8),'Kârı satış gelirinin %20’si sanmış: (2400 ÷ 0,8) ÷ 320 = 9,375.','bilgi')],
 'Bir yumurtanın satış fiyatı (TL).',['Toplam maliyet kaç TL? Satış geliri bu maliyetin kaç katı olmalı ve gelir kaç yumurtadan elde edilecek?'],[KAR,FIRE],
 [A('Maliyeti bul','Tüm yumurtalar için ödenen para.','400 × 6 = 2400 TL'),A('Hedef geliri bul','Kâr %20 olacak.','2400 × 1,2 = 2880 TL'),A('Satılacak yumurta','Kırıklar satılamaz.','400 − 80 = 320 yumurta'),A('Fiyatı bul','Geliri satılan yumurtaya böl.','2880 ÷ 320 = 9 TL')],
 'Satılamayan mal maliyete dahildir ama satış gelirine katkı yapmaz; hedef geliri yalnız satılabilen mala böl.')

# 0010 orta · satış fiyatına göre kâr
al=1200; sf=F(al)/F(4,5); assert sf==1500 and sf-al==300 and sf*F(1,5)==300
dist=[(240,'Yalnızca kârı (alışın %20’si) bulmuş.','dikkat'),(1200,'Alış fiyatını satış fiyatı sanmış; kâr eklememiş.','dikkat'),(1440,'Kârı alışın %20’si almış; kâr satış fiyatının %20’sidir.','bilgi'),(960,'Alışın %80’ini almış; kâr satışın %20’si ise alış satışın %80’idir, satış alıştan büyüktür.','bilgi')]
assert al*F(1,5)==240 and al*F(6,5)==1440 and al*F(4,5)==960
q('0010','kzb-oran','Kârın hangi fiyata göre verildiği','orta','Satışa Göre Kâr','Kârın satış fiyatının yüzdesi olarak verildiği durumda satış fiyatını bulur.','hikâyeli','K-KZB-06 (kâr satış fiyatının %20’si) · yazıcı',
 'Bir mağaza, alış fiyatı 1200 TL olan bir yazıcıyı satmak istemektedir. Mağaza, kârın satış fiyatının %20’si olmasını hedeflemektedir.\nBuna göre yazıcının satış fiyatı kaç TL olmalıdır?',
 1500,dist,'Yazıcının satış fiyatı (TL).',['Kâr hangi fiyatın yüzdesi olarak verilmiş? Alışı satış cinsinden yazmayı dene.'],[SATORAN,KAR],
 [A('Alışı satışa bağla','Satış s olsun; kâr 0,2 s ise alış 0,8 s.','alış = s − 0,2 × s = 0,8 × s'),A('Denklemi kur','Alış 1200 TL.','0,8 × s = 1200'),A('Çöz','Her iki tarafı 0,8’e böl.','s = 1200 ÷ 0,8 = 1500 TL'),A('Kontrol','Kâr satışın %20’si mi?','kâr = 1500 − 1200 = 300 = 1500 × 0,2 ✓')],
 'Kâr satışın yüzdesi ise alış = satış × (1 − p/100); alışın yüzdesi ise satış = alış × (1 + p/100).')

# 0011 orta · etiket + kâr → alış
et=3600; s=et*F(3,4); al=s/F(6,5); assert s==2700 and al==2250 and s*F(4,5)==2160 and s*F(6,5)==3240 and et*F(4,5)==2880
q('0011','kzb-etiket','Etiket fiyatı, indirim ve kâr','orta','Kârdan Alış Fiyatı','İndirimli satış ve kâr yüzdesinden alış fiyatını bulur.','hikâyeli','K-KZB-02 (indirim + kâr → alış fiyatı) · akıllı saat',
 'Etiket fiyatı 3600 TL olan bir akıllı saat, etiket fiyatı üzerinden %25 indirimle satılınca mağaza %20 kâr elde etmiştir.\nBuna göre bu akıllı saatin alış fiyatı kaç TL’dir?',
 2250,[(2160,'Satış fiyatının %80’ini alış sanmış; kâr yüzdesi alışa göre olduğundan satış, alışın %120’sidir.','bilgi'),(2700,'İndirimli satış fiyatını alış fiyatı sanmış.','dikkat'),(2880,'Etiket fiyatından %20 düşmüş; %20 kâr satış fiyatı ile alış arasındadır.','bilgi'),(3240,'İndirimli fiyatı 1,2 ile çarpmış; alışı bulmak için bölmek gerekir.','islem')],
 'Akıllı saatin alış fiyatı (TL).',['Satış fiyatı etiket fiyatının kaçta kaçıdır? Satış fiyatı alışın yüzde kaçına eşittir?'],[IND,SAT],
 [A('Satış fiyatını bul','Etiketin %75’i.','3600 × 0,75 = 2700 TL'),A('Alışla ilişkilendir','%20 kârla satış alışın %120’sidir.','1,2 × x = 2700'),A('Alışı bul','1,2’ye böl.','x = 2700 ÷ 1,2 = 2250 TL')],
 'Önce satış fiyatını indirimden bul, sonra “satış = alış × (1 + kâr)” ilişkisini alış için çöz.')

# 0013 orta · karışım hedef kâr
f,b=400,600; ort=F(3*f+2*b,5); fyat=ort*F(6,5); assert ort==480 and fyat==F(2304,4) and fyat==576
assert ort*F(1,5)==F(96) and F(f+b,2)*F(6,5)==600 and b*F(6,5)==720
q('0013','kzb-toplu','Toplu alım, fire ve parça satış','orta','Karışım Satışı','Farklı fiyatlı iki malın karışımını hedef kârla satacak fiyatı bulur.','hikâyeli','K-KZB-05 (karışım maliyeti, hedef kâr) · kuruyemiş',
 'Bir kuruyemişçi, kilogramı 400 TL olan fındık ile kilogramı 600 TL olan bademi 3 : 2 kütle oranında karıştırmıştır. Karışımı, maliyetinin %20 fazlasına satacaktır.\nBuna göre karışımın kilogram satış fiyatı kaç TL’dir?',
 576,[(96,'Karışımın kilogram kârını (96 TL) satış fiyatı sanmış.','dikkat'),(480,'Karışımın maliyetini (480 TL) satış fiyatı sanmış; kâr eklememiş.','dikkat'),(600,'İki fiyatın aritmetik ortalamasını (500 TL) alıp üstüne %20 eklemiş; karışım 3 : 2 olduğundan fındık ağırlıklıdır.','bilgi'),(720,'Pahalı ürünün fiyatına (600 TL) %20 eklemiş.','dikkat')],
 'Karışımın kilogram satış fiyatı (TL).',['5 kg karışımın toplam maliyetini bul; kilogram başına maliyeti hesaplamadan kâr ekleme.'],[KAR,B('Karışım maliyeti','karışımın maliyeti, bileşenlerin kütle × fiyat toplamıdır; kilogram maliyeti toplam maliyet ÷ toplam kütledir. Örnek: 1 kg 10 TL + 1 kg 20 TL = 30 TL, kilogramı 15 TL')],
 [A('Parçaların maliyeti','3 kg fındık ve 2 kg badem alalım.','3 × 400 = 1200 · 2 × 600 = 1200'),A('Kilogram maliyeti','Toplam maliyet ÷ 5 kg.','(1200 + 1200) ÷ 5 = 480 TL'),A('Kâr ekle','Maliyetin %120’si.','480 × 1,2 = 576 TL')],
 'Karışımın birim maliyeti, ağırlıklı ortalamayla bulunur; kâr bu birim maliyete eklenir.')

# 0014 orta · yeni nesil kademeli indirim
sep=4400; ode=1000+(3000-1000)*F(9,10)+(sep-3000)*F(3,4); assert ode==3850
assert sep*F(65,100)==2860 and sep*F(3,4)==3300 and 1000+(sep-1000)*F(3,4)==3550 and 900+1800+1050==3750
q('0014','kzb-yeninesil','Yeni nesil ve öncüllü kâr-zarar','orta','Kademeli İndirim','Kademeli indirim kuralını sepet tutarına uygulayarak ödenecek tutarı bulur.','yeni nesil','K-KZB-07 (kademeli indirim kuralı) · sepet indirimi',
 'Bir mağazada sepet tutarına göre kademeli indirim uygulanmaktadır. Sepet tutarının ilk 1000 TL’lik kısmına indirim yapılmaz, 1000 TL ile 3000 TL arasındaki kısmına %10, 3000 TL’yi aşan kısmına %25 indirim yapılır. Her indirim yalnız ait olduğu kademedeki tutara uygulanır.\nİndirimsiz tutarı 4400 TL olan bir sepet için müşteri kaç TL öder?',
 3850,[(2860,'%10 ile %25’i toplayıp tüm tutara %35 indirim uygulamış.','islem'),(3300,'Tüm tutara en yüksek oran olan %25’i uygulamış.','bilgi'),(3550,'1000 TL’nin üzerindeki tüm tutara (3400 TL) %25 uygulamış.','bilgi'),(3750,'İlk 1000 TL’ye de %10 indirim uygulamış: 900 + 1800 + 1050.','bilgi')],
 'Müşterinin ödeyeceği tutar (TL).',['Sepeti kademelere ayır: her kademedeki tutarı ve o kademenin indirim oranını yaz.'],[IND],
 [A('Kademelere ayır','4400 TL, üç kısma bölünür.','1000 + 2000 + 1400 = 4400'),A('Birinci kademe','İndirim yok.','1000 TL'),A('İkinci kademe','%10 indirimle.','2000 × 0,9 = 1800 TL'),A('Üçüncü kademe','%25 indirimle.','1400 × 0,75 = 1050 TL'),A('Toplamı bul','Üç kademenin toplamı.','1000 + 1800 + 1050 = 3850 TL')],
 'Kademeli kurallarda her oran yalnız kendi aralığına uygulanır; kademeleri ayrı hesaplayıp topla.')

# 0015 orta · öncüllü (kârdan alış fiyatı)
def durum(A_):
    k=A_*F(1,5); S=A_+k
    I=(A_==2250 if k==450 else None); II=(k==S*F(1,5)); III=((2400-A_)/A_==F(1,10))
    return I,II,III
assert durum(F(2250))==(True,False,False) and F(450,2700)==F(1,6) and F(150,2250)==F(1,15)
q('0015','kzb-yeninesil','Yeni nesil ve öncüllü kâr-zarar','orta','Öncüllü Kâr Yüzdesi','Kâr tutarı ve kâr yüzdesinden alış ve satış fiyatını bulup öncülleri sınar.','öncüllü','K-KZB-07 (öncüllü: kâr tutarından alış fiyatı)',
 'Bir ürün, alış fiyatının %20 fazlasına satıldığında 450 TL kâr elde edilmektedir.\nBuna göre,\nI. Ürünün alış fiyatı 2250 TL’dir.\nII. Kâr, ürünün satış fiyatının %20’sidir.\nIII. Ürün 2400 TL’ye satılsaydı %10 kâr elde edilirdi.\nifadelerinden hangileri doğrudur?',
 'Yalnız I',[('Yalnız II','Kârı satış fiyatının %20’si alıp satışı 2250 bulmuş; bu yüzden I’i eleyip II’yi doğru saymış.','bilgi'),('I ve II','I’i doğru bulmuş; II’de 450/2700’ü %20 sanmış, oysa %16,7’dir.','islem'),('I ve III','III’te 2400 − 2250 = 150 TL’yi alışın %10’u sanmış; oysa %6,7’dir.','islem'),('I, II ve III','Öncülleri tek tek sınamadan hepsini doğru kabul etmiş.','dikkat')],
 'Doğru olan öncüllerin belirlenmesi.',['Kâr, alış fiyatının yüzde kaçı olarak verilmiş? Önce alış ve satış fiyatını bul, sonra öncülleri sına.'],[KAR,SATORAN],
 [A('Alışı bul','Kâr alışın %20’si.','0,2 × A = 450 → A = 2250 TL → I doğru'),A('Satışı bul','Satış = alış + kâr.','2250 + 450 = 2700 TL'),A('II’yi sına','Kârın satışa oranı.','450/2700 = %16,7 ≠ %20 → II yanlış'),A('III’ü sına','2400 TL’de kâr 150 TL.','150/2250 = %6,7 ≠ %10 → III yanlış')],
 'Öncülleri sınamadan önce alış ve satış fiyatını bul; yüzdelerin hangi fiyata göre olduğunu her öncülde ayrı ayrı kontrol et.',
 sira=['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III'])

# 0016 orta · iki ürün: satışa göre / alışa göre kâr
satA,satB=2000,1200; kA=satA*F(1,4); alB=F(satB)/F(5,4); kB=satB-alB
assert kA==500 and alB==960 and kB==240 and kA+kB==740
assert satA-F(satA)/F(5,4)==400 and 400+240==640
assert satB*F(1,4)==300 and 500+300==800
q('0016','kzb-ikiurun','İki ürün: kâr ve zarar birlikte','orta','İki Ürün, İki Oran','Kârı satışa göre ve alışa göre verilen iki ürünün toplam kârını bulur.','hikâyeli','K-KZB-04 (iki ürün; satışa göre / alışa göre kâr) · seramik vazo ve tablo',
 'Bir hediyelik eşya mağazası, 2000 TL’ye sattığı seramik vazoda satış fiyatının %25’i kadar kâr, 1200 TL’ye sattığı tabloda ise alış fiyatının %25’i kadar kâr etmiştir.\nBuna göre mağazanın bu iki satıştan toplam kârı kaç TL’dir?',
 740,[(240,'Yalnız tablodaki kârı bulup bırakmış.','dikkat'),(500,'Yalnız vazodaki kârı bulup bırakmış.','dikkat'),(640,'Vazodaki %25 kârı alışa göre sanıp (400 TL) tablonun kârıyla toplamış.','bilgi'),(800,'Tablodaki %25 kârı satış fiyatına göre almış (300 TL).','bilgi')],
 'Toplam kâr (TL).',['Her üründe kârın hangi fiyata göre verildiğine bak; iki kârı ayrı ayrı hesaplayıp topla.'],[SATORAN,KAR],
 [A('Vazonun kârı','Kâr satışın %25’i.','2000 × 0,25 = 500 TL'),A('Tablonun alışı','Satış alışın %125’i.','1,25 × x = 1200 → x = 960 TL'),A('Tablonun kârı','Satış − alış.','1200 − 960 = 240 TL'),A('Toplamı bul','İki kâr toplanır.','500 + 240 = 740 TL')],
 'Kârın satışa mı alışa mı göre verildiğini her üründe ayrı ayrı oku; ikisi aynı sonucu vermez.')

# 0017 orta · zarar yüzdesi
al,et,sat=3750,5000,F(5000)*F(3,5); z=al-sat; assert sat==3000 and z==750 and F(z,al)==F(1,5) and F(z,sat)==F(1,4) and F(z,et)==F(3,20) and F(sat,al)==F(4,5)
q('0017','kzb-temel','Alış, satış, kâr ve zarar yüzdesi','orta','Zarar Yüzdesi','İndirimli satışta alışın altında kalan satıştan zarar yüzdesini bulur.','hikâyeli','K-KZB-01 (etiket + indirim → zarar yüzdesi) · robot süpürge',
 'Alış fiyatı 3750 TL, etiket fiyatı 5000 TL olan bir robot süpürge, stok erimesi için etiket fiyatı üzerinden %40 indirimle satılmıştır.\nBuna göre mağaza bu satıştan yüzde kaç zarar etmiştir?',
 20,[(15,'Zararı (750 TL) etiket fiyatına bölmüş. Zarar yüzdesi alış fiyatına göredir.','bilgi'),(25,'Zararı satış fiyatına (3000 TL) bölmüş.','bilgi'),(40,'İndirim yüzdesini zarar yüzdesi sanmış.','dikkat'),(80,'Satışın alışa oranını (%80) zarar yüzdesi sanmış; zarar %20’dir.','islem')],
 'Mağazanın zarar yüzdesi.',['Önce indirimli satış fiyatını bul; sonra alışla karşılaştırıp zararın hangi fiyata oranlanacağını düşün.'],[IND,KAR],
 [A('Satış fiyatını bul','Etiketin %60’ı.','5000 × 0,6 = 3000 TL'),A('Zararı bul','Alış − satış.','3750 − 3000 = 750 TL'),A('Alışa oranla','Zarar yüzdesi alışa göre.','750/3750 = 1/5 = %20')],
 'Zarar yüzdesi de kâr gibi alış fiyatına göre bulunur; önce indirimli satış fiyatını hesapla.')

# 0018 orta · ikincisi %50
fy=640; n=5; tam=fy*n; ode=2*(fy+fy*F(1,2))+fy; ind=tam-ode
assert ode==2560 and ind==640 and F(ind,tam)==F(1,5) and F(ind,ode)==F(1,4) and F(3*fy*F(1,2),tam)==F(3,10) and F(2*fy,tam)==F(2,5)
q('0018','kzb-kampanya','Kampanya ve taksit','orta','İkincisi Yarı Fiyatına','“İkinci ürün yarı fiyatına” kampanyasında toplam indirim yüzdesini bulur.','hikâyeli','K-KZB-03 (ikincisi %50) · pantolon, 5 adet',
 'Bir giyim mağazasında tanesi 640 TL olan pantolonlarda “ikinci ürün %50 indirimli” kampanyası vardır. Alınan pantolonlar ikişerli gruplanır ve her gruptaki ikinci pantolon yarı fiyatına satılır; grubu tamamlamayan pantolon için indirim yoktur.\nBu mağazadan 5 pantolon alan bir müşteri, indirimsiz toplam tutara göre yüzde kaç indirim kazanmış olur?',
 20,[(25,'İndirimi ödenen tutara (2560 TL) oranlamış: 640/2560 = %25. İndirimsiz toplam 3200 TL’dir.','dikkat'),(30,'Üç pantolonda yarı fiyat indirimi olduğunu sanmış (3 × 320 = 960).','dikkat'),(40,'İkinci pantolonu bedava sanmış (2 × 640 = 1280 indirim).','bilgi'),(50,'Kampanya yüzdesini (%50) toplam indirim yüzdesi sanmış.','dikkat')],
 'Toplam indirim yüzdesi.',['5 pantolonun kaç ikili grubu vardır? Kaç pantolonda yarı fiyat indirimi uygulanır?'],[KAMP,IND],
 [A('İndirimsiz tutar','5 pantolon tam fiyat.','5 × 640 = 3200 TL'),A('İndirimli pantolon sayısı','2 grup vardır, her grupta 1 pantolon yarı fiyat.','2 pantolon yarı fiyatına'),A('İndirim tutarı','Yarı fiyat = 320 TL indirim.','2 × 320 = 640 TL'),A('Yüzdeye çevir','Toplam tutara oranla.','640/3200 = 1/5 = %20')],
 'Kampanya indirimini TL olarak bul, indirimsiz toplama böl; kampanya oranı ile toplam indirim oranı farklıdır.')

# 0019 zor · etiket + kampanya + kasa indirimi → kâr yüzdesi
al=1000; et=al*F(8,5); n=4; kamp=2*(et+et/2); kasa=kamp*F(9,10); kr=kasa-n*al
assert et==1600 and kamp==4800 and kasa==4320 and kr==320 and F(kr,n*al)==F(2,25)
assert F(kamp-n*al,n*al)==F(1,5) and (n*et*F(9,10)-n*al)/(n*al)==F(44,100) and 60-35==25 and 60-10==50
q('0019','kzb-kampanya','Kampanya ve taksit','zor','Kampanya ve Kasa İndirimi','Etiket, “ikincisi yarı fiyatına” kampanyası ve kasa indirimini birlikte uygulayıp kâr yüzdesini bulur.','hikâyeli','K-KZB-03 (etiket + ikincisi %50 + kasa %10 → kâr) · termos bardak',
 'Bir mağaza, alış fiyatı 1000 TL olan termos bardakların etiket fiyatını alış fiyatının %60 fazlası olarak belirlemiştir. Mağazada “ikinci ürün %50 indirimli” kampanyası vardır; alınan bardaklar ikişerli gruplanır ve her gruptaki ikinci bardak yarı fiyatına satılır. Ayrıca kasada, kampanyalı toplam tutar üzerinden %10 indirim yapılmaktadır.\nBir müşteri bu bardaklardan 4 tane aldığına göre mağaza bu satıştan yüzde kaç kâr eder?',
 8,[(20,'Kasadaki %10 indirimi uygulamamış: 4800 − 4000 = 800, kâr %20.','dikkat'),(25,'Kampanyanın toplam indirimini (%25) ve kasa indirimini (%10) toplayıp 60 − (25 + 10) = 25 bulmuş; indirimler farklı tutarlar üzerindendir.','islem'),(44,'Kampanyayı unutup yalnız %10 kasa indirimi uygulamış: 6400 × 0,9 = 5760, kâr %44.','dikkat'),(50,'60’tan yalnız kasa indirimini (%10) çıkarmış.','islem')],
 'Mağazanın kâr yüzdesi.',['Etiket fiyatını bulduktan sonra 4 bardağın kampanyalı toplamını, sonra kasa indirimli tutarı bul; kâr yüzdesinde paydaya dikkat et.'],[IND,KAMP,KAR],
 [A('Etiket fiyatı','Alışın %160’ı.','1000 × 1,6 = 1600 TL'),A('Kampanyalı tutar','2 grup; her grupta 1600 + 800.','2 × (1600 + 800) = 4800 TL'),A('Kasa indirimi','Kampanyalı tutarın %90’ı.','4800 × 0,9 = 4320 TL'),A('Kârı bul','Alış toplamı 4 × 1000.','4320 − 4000 = 320 TL'),A('Yüzdeye çevir','Kâr toplam alışa oranlanır.','320/4000 = 0,08 = %8')],
 'Kampanya ve kasa indirimi ayrı aşamalardır; her aşamayı sırayla uygula, kârı en sonda toplam alışa oranla.')

# 0020 zor · iki ürün, toplam alış ve toplam kâr → denklem
T=5000; kyz=F(5,100); x=None
sol=[(xx,T-xx) for xx in range(0,T+1) if F(15,100)*xx-F(10,100)*(T-xx)==T*kyz]
assert sol==[(3000,2000)]
x,y=sol[0]; sz=y*F(9,10); sk=x*F(115,100)
assert sz==1800 and sk==3450 and sz+sk==T*F(105,100) and y*F(11,10)==2200
q('0020','kzb-ikiurun','İki ürün: kâr ve zarar birlikte','zor','Toplam Sonuçtan Alış','Toplam alış ve toplam kârdan iki ürünün alış fiyatlarını bulup zararla satılan ürünün satışını hesaplar.','hikâyeli','K-KZB-04 (toplam alış, toplam kâr, denklem) · iki ürün, toplam sonuç',
 'Bir mağaza, alış fiyatları toplamı 5000 TL olan iki ürünün birini %15 kârla, diğerini %10 zararla satmış ve bu iki satıştan toplam alış fiyatına göre %5 kâr elde etmiştir.\nBuna göre zararla satılan ürün kaç TL’ye satılmıştır?',
 1800,[(2000,'Zararla satılan ürünün alış fiyatını (2000 TL) bulup bırakmış.','dikkat'),(2200,'Zararda satış fiyatını alışın %110’u olarak hesaplamış (2000 × 1,1).','bilgi'),(3000,'Kârla satılan ürünün alış fiyatını bulup bırakmış.','dikkat'),(3450,'Kârla satılan ürünün satış fiyatını bulup bırakmış.','dikkat')],
 'Zararla satılan ürünün satış fiyatı (TL).',['Kârla satılan ürünün alışına x de; zararlı ürünün alışını x cinsinden yaz. Toplam kârı iki farklı yoldan ifade et.'],[KAR,SAT],
 [A('Bilinmeyenleri tanımla','Kârlı ürünün alışı x, diğerinin alışı 5000 − x.','x + y = 5000'),A('Toplam kâr','Toplamda %5 kâr: 5000 × 0,05 = 250 TL.','0,15 x − 0,10 (5000 − x) = 250'),A('Denklemi çöz','Parantezi aç, düzenle.','0,25 x − 500 = 250 → x = 3000 · y = 2000'),A('Satışı bul','Zararlı ürün alışın %90’ına satıldı.','2000 × 0,9 = 1800 TL')],
 'Toplam sonuç verildiğinde her ürünün kâr–zararını tek denklemde topla; bilinmeyenleri alış fiyatları olarak seç.')

# 0021 zor · toplu alım, kırık, iki parti satış, hedef kâr
n,pf,k=500,80,60; mal=n*pf; sag=n-k; a=sag//2; b=a//2; c=sag-a-b; g1=a*105; g2=b*100; hedef=mal*F(110,100); sf=(hedef-g1-g2)/c
assert (mal,sag,a,b,c)==(40000,440,220,110,110) and g1==23100 and g2==11000 and hedef==44000 and sf==90
d1=hedef/n; d2=(hedef-g1)/(b+c); d3=hedef/sag; d4=(hedef-g1)/c
assert (d1,d2,d3,d4)==(88,95,100,190)
q('0021','kzb-toplu','Toplu alım, fire ve parça satış','zor','Parça Parça Satış','Kırık malı maliyete katarak iki farklı fiyattan yapılan satıştan sonra kalan mal için hedef kâr fiyatını bulur.','hikâyeli','K-KZB-05 (kırık mal + iki parti satış + hedef kâr) · bardak',
 'Bir toptancı, tanesini 80 TL’den 500 bardak satın almıştır. Bardakların 60’ı taşınırken kırıldığı için satılamamıştır. Sağlam kalan bardakların yarısı tanesi 105 TL’den, geri kalanların yarısı tanesi 100 TL’den satılmıştır.\nToptancı, bardaklara ödediği paranın tamamına göre %10 kâr elde etmek istediğine göre, hâlâ satılmamış olan bardakların her birini kaç TL’den satmalıdır?',
 90,[(88,'Hedef geliri kırık bardaklar dahil 500 bardağa bölmüş: 44 000 ÷ 500.','dikkat'),(95,'İkinci parti satışın gelirini hesaba katmamış: (44 000 − 23 100) ÷ 220 = 95.','dikkat'),(100,'Hedef geliri sağlam bardaklara bölüp (44 000 ÷ 440) ortalama fiyatı kalan bardakların fiyatı sanmış.','bilgi'),(190,'İkinci parti satışın gelirini unutup kalan 110 bardağa yüklemiş: (44 000 − 23 100) ÷ 110.','dikkat')],
 'Kalan bardakların tanesinin satış fiyatı (TL).',['Önce kaç bardağın sağlam olduğunu ve her satış partisinde kaç bardak satıldığını bul; hedef geliri toplam maliyetten hesapla.'],[KAR,FIRE],
 [A('Sağlam ve partiler','500 − 60 = 440 sağlam bardak.','1. parti 220 · 2. parti 110 · kalan 110'),A('Maliyet ve hedef gelir','Tüm bardaklar için ödenen paranın %110’u.','500 × 80 = 40 000 · 40 000 × 1,1 = 44 000 TL'),A('Önceki gelirler','İki parti satış.','220 × 105 = 23 100 · 110 × 100 = 11 000 → 34 100 TL'),A('Kalan bardak fiyatı','Eksik gelir ÷ kalan bardak.','(44 000 − 34 100) ÷ 110 = 9900 ÷ 110 = 90 TL')],
 'Hedef geliri toplam maliyetten bul, elde edilen gelirleri çıkar, kalanı satılmamış mal sayısına böl.')

# 0022 zor · yeni nesil kâr payı
al=1800; s=F(al)/F(3,4); etk=s/F(4,5); assert s==2400 and etk==3000 and s-al==600 and F(600,s)==F(1,4)
dd=[(s,'İndirimli satış fiyatını (2400 TL) etiket fiyatı sanmış.','dikkat'),(F(al*5,4)/F(4,5),'Satışı 2250 bulup etiketi 2250 ÷ 0,8 = 2812,5 hesaplamış.','bilgi'),(s*F(6,5),'İndirimli fiyatı 1,2 ile çarpmış; etiket, indirimli fiyatın 1/0,8 katıdır.','islem'),(al*F(5,4)*F(6,5),'Satışı 2250 bulup üstüne %20 eklemiş.','bilgi')]
vals=[v for v,_,_ in dd]; assert vals==[2400,F(2250)/F(4,5),2880,2700] and F(2250)/F(4,5)==F(5625,2)
q('0022','kzb-yeninesil','Yeni nesil ve öncüllü kâr-zarar','zor','Kâr Payı','Kârın satış fiyatına oranı olarak tanımlanan kâr payından etiket fiyatını bulur.','yeni nesil','K-KZB-07 (tanımlı kavram: kâr payı = kâr ÷ satış) · etiket fiyatı',
 'Bir mağazada “kâr payı”, bir ürünün satışından elde edilen kârın satış fiyatına oranı olarak tanımlanmaktadır. Yani kâr payı = kâr ÷ satış fiyatıdır.\nAlış fiyatı 1800 TL olan bir ürün, etiket fiyatı üzerinden %20 indirimle satıldığında kâr payı %25 olmaktadır.\nBuna göre bu ürünün etiket fiyatı kaç TL’dir?',
 3000,dd,'Ürünün etiket fiyatı (TL).',['Kâr payı hangi fiyata göre tanımlı? Alışı o fiyat cinsinden yazmayı dene.'],[SATORAN,IND],
 [A('Alışı satışa bağla','Satış s olsun; kâr payı %25 ise kâr 0,25 s.','alış = s − 0,25 s = 0,75 s'),A('Satış fiyatını bul','Alış 1800 TL.','0,75 × s = 1800 → s = 2400 TL'),A('Etikete geç','Satış, etiketin %80’i.','0,8 × E = 2400 → E = 3000 TL'),A('Kontrol','Kâr payı tanıma uyuyor mu?','kâr = 2400 − 1800 = 600 · 600/2400 = %25 ✓')],
 'Tanımda oranın hangi fiyata göre olduğunu bul; denklemi o fiyat üzerinden kur, sonra indirimi geri al.')

# 0023 zor · öncüllü
def dur(Aa):
    E=Aa*F(7,5); assert E*F(4,5)==Aa*F(28,25)
    return (E==Aa*F(7,5), E*F(3,4)==Aa*F(11,10), E*F(7,10)<Aa and E*F(7,10)==Aa*F(98,100))
for Aa in (F(1),F(2000),F(31)): assert dur(Aa)==(True,False,True)
assert F(7,5)*F(3,4)==F(21,20) and F(7,5)*F(7,10)==F(49,50)
q('0023','kzb-yeninesil','Yeni nesil ve öncüllü kâr-zarar','orta','Öncüllü Zarar ve Kâr','Etiket ve alış ilişkisinden farklı indirimlerin kâr–zarar sonucunu öncüllerle sınar.','öncüllü','K-KZB-07 (öncüllü: %12 kâr, farklı indirimler) · etiket fiyatı',
 'Bir ürün, etiket fiyatı üzerinden %20 indirimle satıldığında alış fiyatına göre %12 kâr edilmektedir.\nBuna göre,\nI. Etiket fiyatı alış fiyatının %40 fazlasıdır.\nII. Ürün etiket fiyatı üzerinden %25 indirimle satılsaydı %10 kâr edilirdi.\nIII. Ürün etiket fiyatı üzerinden %30 indirimle satılsaydı %2 zarar edilirdi.\nifadelerinden hangileri doğrudur?',
 'I ve III',[('Yalnız I','III’ü sınarken 1,4 × 0,7 = 0,98 sonucunu zarar olarak görmemiş; yalnız I’i doğru bulmuş.','islem'),('Yalnız II','I’i %40 yerine %32 (12 + 20) bulup eleyip II’yi doğru saymış.','bilgi'),('I ve II','III’te 0,98 A’yı zarar olarak görmeyip eleyip II’de 0,75 × 1,4’ü 1,1 hesaplamış.','islem'),('I, II ve III','II’de 0,75 × 1,4’ü 1,1 hesaplayıp üç öncülü de doğru bulmuş.','islem')],
 'Doğru olan öncüllerin belirlenmesi.',['Alış fiyatına bir değer ver; önce etiket fiyatını bul, sonra her indirim için satışı hesaplayıp alışla karşılaştır.'],[IND,KAR],
 [A('Etiketi bul','Satış etiketin %80’i ve alışın %112’si.','0,8 × E = 1,12 × A → E = 1,4 × A'),A('I’i sına','Etiket alışın 1,4 katı.','%40 fazla → I doğru'),A('II’yi sına','%25 indirimle satış etiketin %75’i.','0,75 × 1,4 A = 1,05 A → %5 kâr → II yanlış'),A('III’ü sına','%30 indirimle satış etiketin %70’i.','0,7 × 1,4 A = 0,98 A → %2 zarar → III doğru')],
 'Etiketi alışın katı olarak yaz; her öncül için satış fiyatını bu katsayıyla bulup alışla karşılaştır.',
 sira=['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III'])

# 0024 zor · zincir kârı
Sx=3000; Ap=F(Sx)/F(5,4); A0=Ap/F(6,5); kt=Ap-A0; kp=Sx-Ap
assert (Ap,A0,kt,kp)==(2400,2000,400,600) and kp-kt==200 and kt+kp==1000 and Sx*F(1,4)==750 and F(2250)/F(6,5)==1875 and 2250-1875==375 and 750-375==375
q('0024','kzb-oran','Kârın hangi fiyata göre verildiği','orta','Zincirleme Kâr','Alış–satış zincirinde iki aracının kârları arasındaki farkı bulur.','hikâyeli','K-KZB-06 (toptancı %20, perakendeci %25 zincir kârı) · ürün',
 'Bir toptancı, bir ürünü kendi alış fiyatının %20 fazlasına perakendeciye satmaktadır. Perakendeci de bu ürünü, kendi alış fiyatının %25 fazlasına müşteriye 3000 TL’ye satmaktadır.\nBuna göre perakendecinin bu üründen elde ettiği kâr, toptancının elde ettiği kârdan kaç TL fazladır?',
 200,[(375,'Perakendecinin kârını satışın %25’i (750 TL) alıp alışını 2250 bulmuş; toptancı kârı 375, fark 375.','bilgi'),(400,'Yalnız toptancının kârını bulup bırakmış.','dikkat'),(600,'Yalnız perakendecinin kârını bulup bırakmış.','dikkat'),(1000,'İki kârı toplamış; soru farkı soruyor.','dikkat')],
 'Perakendecinin kârı ile toptancının kârı arasındaki fark (TL).',['Zinciri sondan başa doğru çöz: perakendecinin alışı toptancının satışıdır.'],[KAR,SAT],
 [A('Perakendecinin alışı','Satış, alışın %125’i.','1,25 × x = 3000 → x = 2400 TL'),A('Perakendecinin kârı','Satış − alış.','3000 − 2400 = 600 TL'),A('Toptancının alışı','Toptancı satışı 2400 TL, alışın %120’si.','1,2 × y = 2400 → y = 2000 TL'),A('Kârları karşılaştır','Toptancı kârı 400 TL.','600 − 400 = 200 TL')],
 'Zincirlerde bir aracının satış fiyatı sonrakinin alış fiyatıdır; her halkada yüzdeyi o halkanın alışına uygula.')

# 0012 zor · taksit
tam=1550*12; pesn=F(tam)/F(124,100); al=pesn/F(5,4); kr=tam-al
assert tam==18600 and pesn==15000 and al==12000 and kr==6600 and F(kr,al)==F(11,20)
q('0012','kzb-kampanya','Kampanya ve taksit','zor','Taksitli Satışta Kâr','Taksitli satış toplamından peşin fiyatı ve alış fiyatını bulup taksitli satıştaki kâr yüzdesini hesaplar.','hikâyeli','K-KZB-03 (vade farkı + peşin kâr → taksitli kâr) · mobilya',
 'Bir mobilya mağazası, ürünleri alış fiyatının %25 fazlasına peşin satmaktadır. Taksitli satışta ise peşin fiyata %24 vade farkı eklenmekte ve tutar 12 eşit taksitte tahsil edilmektedir.\nAylık taksit tutarı 1550 TL olan bir ürün için mağazanın taksitli satıştaki kâr yüzdesi kaçtır?',
 55,[(24,'Vade farkı yüzdesini kâr yüzdesi sanmış.','dikkat'),(25,'Peşin satıştaki kâr yüzdesini vermiş; taksitli satışta vade farkı da kâra katılır.','dikkat'),(49,'Peşin kâr ile vade farkı yüzdelerini toplamış (25 + 24); vade farkı peşin fiyata uygulanır, alışa değil.','islem'),(155,'Taksitli satışın alışa oranını (%155) kâr yüzdesi sanmış.','dikkat')],
 'Taksitli satıştaki kâr yüzdesi.',['Toplam taksit tutarı peşin fiyatın kaç katıdır? Peşin fiyat da alışın kaç katıdır?'],[TAK,KAR],
 [A('Toplam ödeme','12 taksit.','1550 × 12 = 18 600 TL'),A('Peşin fiyatı bul','Toplam, peşin fiyatın %124’ü.','1,24 × P = 18 600 → P = 15 000 TL'),A('Alış fiyatını bul','Peşin fiyat, alışın %125’i.','1,25 × A = 15 000 → A = 12 000 TL'),A('Kâr yüzdesi','Taksitli satışta kâr = toplam − alış.','18 600 − 12 000 = 6600 · 6600/12 000 = %55')],
 'Vade farkı peşin fiyata, kâr yüzdesi alışa göredir; zinciri peşin fiyat üzerinden alışa kadar geri çöz.')

# sıralı no için: 0012 yukarıda tanımlandı, P.ANA'yı numaraya göre sırala
P.ANA.sort(key=lambda q_: q_['id'])
bitir(P,'karzarariki',UK)
