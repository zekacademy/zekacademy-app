"""Kesir Problemleri · parti 2 (hafif mod): 24 ana soru, kardeş yok, ipucu 1. Her cevap ve çeldirici kodla doğrulanır."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_mat as H
from _hafif_mat import *
H.KONU='Kesir Problemleri'
UK='prob|Kesir Problemleri'
P=Parti('kesirprobiki','Kesir Problemleri',UK)

PARCA=B('Parçadan bütüne','bütünün a/b’si X ise bütün = X ÷ a × b. Örnek: 3/5’i 60 olan sayı 60 ÷ 3 × 5 = 100')
KALAN=B('Kalanın kesri','“kalanın 1/4’ü” ifadesi, o ana kadar geriye kalan miktarın 1/4’üdür; bütünün değil. Örnek: 80’in 1/2’si harcandıktan sonra kalanın 1/4’ü 10’dur')
ZINCIR=B('Ardışık kalan kesirler','ilk adımda 1/3 kullanılırsa 2/3 kalır; sonra kalanın 1/4’ü kullanılırsa kalanın 3/4’ü kalır: 2/3 × 3/4 = 1/2. Örnek: 120 TL’nin sonda kalanı 60 TL’dir')
FARK=B('Kesirlerde fark','iki kesrin farkı için paydalar eşitlenir. Örnek: 3/4 − 1/3 = 9/12 − 4/12 = 5/12')
ESIT=B('İki kesirle ifade edilen aynı miktar','A’nın 2/3’ü B’nin 3/4’üne eşitse 2A/3 = 3B/4 yazılıp ortak değer k ile A = 3k/2, B = 4k/3 bulunur; en küçük ortak payda ile oran kurulur. Örnek: 2A/3 = 3B/4 ise A : B = 9 : 8')
ART=B('Kesir kadar artırma ve azaltma','bir miktar 1/4’ü kadar artırılırsa yeni miktar 5/4 katıdır; 1/5’i kadar azaltılırsa 4/5 katıdır. Örnek: 40 TL 1/4’ü kadar artarsa 40 × 5/4 = 50 TL olur')
ARDART=B('Ardışık artış ve azalış','her değişimde çarpan ardışık uygulanır; ikincisi yeni miktarın kesriyle yapılır. Örnek: 1/2 artış sonra 1/3 azalış çarpanı 3/2 × 2/3 = 1 olur')
PAYDA=B('Eşit paylaşım','bir miktar n kişiye eşit paylaştırılırsa her pay miktarın 1/n’idir. Örnek: pastanın 1/4’ü 2 kişiye eşit bölünürse her pay pastanın 1/8’idir')
KAP=B('Kabın dolulukları','dolulukların farkı eklenen ya da alınan miktarın kapasitedeki kesridir. Örnek: 1/5 dolu kaba 15 L eklenince 1/2 dolarsa 15 L, kapasitenin 3/10’udur → kapasite 50 L')
GERI=B('Geri sarma','son durumdan başlanıp işlemler ters sırayla geri alınır: toplama çıkarmaya, çarpma bölmeye döner. Örnek: x × 3 + 4 = 19 ise x = (19 − 4) ÷ 3 = 5')
KURAL=B('Kural tanımı','soruda verilen kural olduğu gibi uygulanır, bildiğin işlemle karıştırılmaz. Örnek: a ★ b = a + 2b ise 3 ★ 4 = 3 + 8 = 11')

KY='ÖSYM 2018–2026 TYT Matematik (kesir problemleri) · yayın soru bankaları (yalnız mantık) · MEB 6–9. sınıf'
kart('K-KESB-01','Bütünün ve kalanın kesri zinciri','Bir bütünden ardışık olarak bütünün ve kalanın kesirleri ayrılır; sondaki miktar verilip bütün ya da ara bir parça istenir.','“Kalanın” kesrini bütüne uygulamak; yalnız son adımı geri almak; istenen ara parçayı karıştırmak.','orta','hikâyeli',3,'ksb-zincir','Bütünün ve kalanın kesri zinciri',KY)
kart('K-KESB-02','Kesrin tamamını bulma','Bir miktarın a/b’si verilir; bütün ve buna bağlı ikinci bir miktar hesaplanır.','Verilen sayıyı bütün sanmak; payı paydayla çarpmak; kesrin payına bölmeyi unutmak.','kolay','hikâyeli',2,'ksb-tamami','Kesrin tamamını bulma',KY)
kart('K-KESB-03','Artan–eksilen miktar','Kabın ya da pilin dolulukları kesirle verilir; doluluk farkı eklenen ya da kullanılan miktara bağlanıp kapasite bulunur.','Doluluk farkını yanlış kesre bağlamak; kapasite yerine ara miktarı vermek.','orta','hikâyeli',3,'ksb-kap','Artan–eksilen miktarlar (depo, pil)',KY)
kart('K-KESB-04','İki kesirle ifade edilen aynı miktar','Aynı miktar iki farklı kesirle verilir; ortak değerle iki çokluğun oranı kurulup istenen hesaplanır.','Kesirlerin yerlerini karıştırıp oranı ters kurmak; ortak değeri iki çokluğun toplamı sanmak.','orta','hikâyeli',4,'ksb-iki','İki farklı kesirle ifade edilen aynı miktar',KY)
kart('K-KESB-05','Kesir kadar artırma ve azaltma','Bir miktar kesri kadar artırılır ya da azaltılır; ardışık değişimlerde çarpanlar birleştirilir.','Artışı ve azalışı toplayıp net kesir bulmak; azalışı ilk miktarın kesri sanmak.','orta','hikâyeli',3,'ksb-artir','Kesir kadar artırma ve azaltma',KY)
kart('K-KESB-06','Paylaşım ve kesirlerin karşılaştırılması','Eşit paylaşımda payın kesri ve farklı kesirlerle ifade edilen ilerlemelerin farkı bir veriyle bütüne bağlanır.','Kişi sayısı farkını pay farkı sanmak; kesirleri karşılaştırırken payları ayrı ayrı çıkarmak.','orta','hikâyeli',3,'ksb-paylas','Eşit paylaşım ve kesirlerin karşılaştırılması',KY)
kart('K-KESB-07','Yeni nesil, kural tanımlı ve geri sarma','Soruda tanımlanan kuralla ya da her dönem tekrarlanan kesir işlemiyle kurulan süreç incelenir; son durumdan geri gidilir.','Tanımlı kuralı alışkın işlemle karıştırmak; geri alırken işlem sırasını bozmak.','zor','yeni nesil',4,'ksb-yeni','Yeni nesil, kural tanımlı ve geri sarma',KY)

def mkk(no,z,tipId,tip,alt,kaz,kalip,adim,kartm,**k):
    mk(P,no,tipId=tipId,tip=tip,z=z,alt=alt,kaz=kaz,kalip=kalip,adim=len(k['ad']),kart=kartm,**k)

# ---------- 01 kolay · zincir ----------
T=Fr(200); k1=T*Fr(3,8); r=T-k1; bag=r*Fr(1,5); son=r-bag
assert son==100 and bag==25 and k1==75 and T*Fr(1,5)==40 and Fr(son)*Fr(1,5)==20
mkk('0001','kolay','ksb-zincir','Bütünün ve kalanın kesri zinciri','Kalanın Kesri','Bütünün ve kalanın kesirleriyle ardışık harcamalardan ara bir tutarı bulur.','hikâyeli',2,
 'K-KESB-01 (zincir) · harçlık ve bağış, ara tutar isteniyor',
 metin='Efe, harçlığının 3/8’ini oyuncağa harcamış, kalan parasının 1/5’ini de bir hayvan barınağına bağışlamıştır.\nGeriye 100 TL’si kaldığına göre Efe’nin barınağa bağışladığı para kaç TL’dir?',
 dogru=25,yan=[(20,'Bağışı kalan 100 TL’nin 1/5’i olarak hesaplamış; bağış, oyuncaktan sonraki paranın 1/5’idir.','dikkat'),(40,'1/5’i harçlığın tamamına uygulamış; “kalanın” 1/5’i demek bütünün değil.','dikkat'),(75,'Barınağa değil oyuncağa harcanan parayı (3/8) bulmuş.','dikkat'),(200,'Harçlığın tamamını bulup durmuş; bağışı hesaplamamış.','dikkat')],
 istenen='Barınağa bağışlanan para (TL).',
 ip=['Oyuncaktan sonra kalan parayı harçlığın kesriyle yaz; 100 TL’nin bunun hangi kesrine karşılık geldiğini bul.'],
 bilgi=[KALAN],
 ad=[A('Kalan kesirleri yaz','Oyuncaktan sonra 5/8 kalır, bağıştan sonra bunun 4/5’i kalır.','5/8 × 4/5 = 1/2 → harçlığın yarısı 100 TL'),A('Harçlığı bul','Yarısı 100 TL ise tamamı 200 TL.','100 × 2 = 200 TL'),A('Bağışı hesapla','Bağış, kalan 5/8’in 1/5’idir; yani bütünün 1/8’i.','5/8 × 1/5 = 1/8 → 200 ÷ 8 = 25 TL')],
 puf='“Kalanın” kesirlerinde önce her adımdan sonra bütünün kaçta kaçı kaldığını yaz, sonra verilen sayıdan bütüne geç.')

# ---------- 02 orta · zincir (yol) ----------
T=Fr(80); g1=T*Fr(1,5); r1=T-g1; g2=r1*Fr(3,8); r2=r1-g2
assert (g1,r1,g2,r2)==(16,64,24,40) and T*Fr(3,8)==30
mkk('0002','orta','ksb-zincir','Bütünün ve kalanın kesri zinciri','Yol Problemi','Üç günde tamamlanan bir yolda ikinci günün uzunluğunu kalanın kesriyle bulur.','hikâyeli',3,
 'K-KESB-01 (zincir) · patika yürüyüşü, üç gün',
 metin='Bir doğa yürüyüşçüsü bir patikayı üç günde tamamlamıştır.\nİlk gün patikanın 1/5’ini, ikinci gün kalan yolun 3/8’ini yürümüş; üçüncü gün de kalan 40 km’yi yürümüştür.\nBuna göre yürüyüşçü ikinci gün kaç km yol almıştır?',
 dogru=24,yan=[(16,'İlk günün yolunu (patikanın 1/5’i) bulmuş.','dikkat'),(30,'3/8’i patikanın tamamına uygulamış; “kalan yolun” 3/8’i demek.','dikkat'),(40,'Üçüncü günün yolunu vermiş.','dikkat'),(80,'Patikanın tamamını bulup durmuş.','dikkat')],
 istenen='İkinci gün yürünen yol (km).',
 ip=['Üçüncü günde kalan 40 km, patikanın kaçta kaçıdır? Bunu önce bul.'],
 bilgi=[KALAN,ZINCIR],
 ad=[A('Kalan kesri bul','İlk günden sonra 4/5 kalır; ikinci günde bunun 3/8’i gidilir, 5/8’i kalır.','4/5 × 5/8 = 1/2'),A('Patikanın tamamı','Yolun yarısı 40 km.','40 × 2 = 80 km'),A('İkinci günün yolu','Kalan 4/5’in 3/8’i bütünün 3/10’udur.','80 × 4/5 = 64 → 64 × 3/8 = 24 km')],
 puf='Verilen miktar son kalansa önce o kalanın bütündeki kesrini bul; tamamını bulduktan sonra ara adımı hesapla.')

# ---------- 03 orta · zincir (kitap) ----------
T=Fr(240); a=T*Fr(1,6); r=T-a; b=r*Fr(1,5); r=r-b; c=r*Fr(3,8); r=r-c
assert r==100
yanl=lambda f:Fr(100)/f
assert yanl(Fr(5,8))==160 and yanl(Fr(4,5)*Fr(5,8))==200 and yanl(Fr(5,6)*Fr(5,8))==Fr(192) and yanl(Fr(5,6)*Fr(4,5))==150
mkk('0003','orta','ksb-zincir','Bütünün ve kalanın kesri zinciri','Kitap Sayfası','Üç ardışık okumadan sonra kalan sayfadan kitabın toplam sayfa sayısını bulur.','hikâyeli',3,
 'K-KESB-01 (zincir) · roman okuma, üç kalan',
 metin='Zeynep bir romanı günlere bölerek okumaktadır.\nİlk gün kitabın 1/6’sını, ikinci gün kalan sayfaların 1/5’ini, üçüncü gün de o anda geriye kalan sayfaların 3/8’ini okumuştur.\nDördüncü güne okunacak 100 sayfa kaldığına göre bu romanın tamamı kaç sayfadır?',
 dogru=240,yan=[(150,'Üçüncü günün kesrini hesaba katmamış; kalan 5/6 × 4/5 = 2/3 imiş gibi yapmış.','dikkat'),(160,'Yalnız son günün kesrini (kalan 5/8) kullanmış; önceki günleri hesaba katmamış.','dikkat'),(192,'İkinci günün kesrini hesaba katmamış; kalan 5/6 × 5/8 imiş gibi yapmış.','dikkat'),(200,'İlk günün kesrini hesaba katmamış; kalan 4/5 × 5/8 imiş gibi yapmış.','dikkat')],
 istenen='Romanın toplam sayfa sayısı.',
 ip=['Her günden sonra kitabın kaçta kaçının kaldığını sırayla yaz; kalanlar çarpılarak ilerler.'],
 bilgi=[ZINCIR],
 ad=[A('Kalan kesirleri çarp','Günlerden sonra kalan oranlar: 5/6, 4/5, 5/8.','5/6 × 4/5 × 5/8 = 5/12'),A('Kalanı eşitle','Sonda kalan 100 sayfa kitabın 5/12’sidir.','5/12 → 100 sayfa'),A('Tamamını bul','Bir parça 20 sayfa; 12 parçanın hepsi.','100 ÷ 5 = 20 → 20 × 12 = 240 sayfa')],
 puf='Her adımda “kalanın kesri” bir çarpan olur: 1 − kesir. Tüm çarpanları çarpıp sondaki kalanla eşitle.')

# ---------- 04 zor · zincir (kırtasiye) ----------
T=Fr(180); s1=T/3; r1=T-s1; s2=r1/4; s3=(s1+s2)*Fr(2,3); son=T-s1-s2-s3
assert (s1,s2,s3,son)==(60,30,60,30) and son==30
yl=lambda f:Fr(30)/f
assert yl(Fr(1,2))==60                                   # üçüncü günü unutmuş
assert yl(1-Fr(1,3)-Fr(1,4)-Fr(1,3)*Fr(2,3)*0-Fr(0))==yl(Fr(5,12))==72   # ikinci günü bütünün 1/4'ü, üçüncü gün yok
assert yl(1-Fr(1,2)-Fr(2,3)*Fr(1,3))==yl(Fr(5,18))==108   # üçüncü gün: yalnız ilk günün 2/3'ü
assert yl(1-Fr(1,3)-Fr(1,3))==yl(Fr(1,3))==90     # ikinci günü toplama katmamış: 1/3 + 1/3
mkk('0004','zor','ksb-zincir','Bütünün ve kalanın kesri zinciri','Kalan ve Toplam','Üç günlük satış düzeninde üçüncü günün satışını önceki günlerin toplamına bağlayarak toplam miktarı bulur.','hikâyeli',5,
 'K-KESB-01 (zincir) · koli satışı, üçüncü gün öncekilerin toplamına bağlı',
 metin='Bir kırtasiye toptancısı, elindeki defter kolilerini üç günde satmıştır.\nİlk gün kolilerin 1/3’ünü, ikinci gün kalan kolilerin 1/4’ünü satmıştır. Üçüncü gün ise ilk iki günde satılan kolilerin toplamının 2/3’ü kadar koli satmıştır.\nGeriye 30 koli kaldığına göre toptancının başlangıçta kaç kolisi vardı?',
 dogru=180,yan=[(60,'Üçüncü günün satışını hesaba katmamış; ilk iki günden sonra kalan 1/2 = 30 koli demiş.','dikkat'),(72,'İkinci günün 1/4’ünü kalan yerine bütüne uygulamış; üçüncü günü de hesaba katmamış.','dikkat'),(90,'Üçüncü günün satışını (1/3) doğru bulmuş ama ikinci günün satışını toplama katmamış; 1/3 + 1/3 = 2/3 satılmış sayıp kalan 1/3 = 30 demiş.','bilgi'),(108,'Üçüncü günü yalnız ilk günün satışının 2/3’ü olarak almış.','dikkat')],
 istenen='Başlangıçtaki koli sayısı.',
 ip=['Satışları bütünün kesri olarak yaz; üçüncü günün satışı için önce ilk iki günün toplamını kesir olarak bul.'],
 bilgi=[KALAN,ZINCIR],
 ad=[A('İlk iki gün','İlk gün 1/3; kalan 2/3’ün 1/4’ü bütünün 1/6’sıdır.','1/3 + 1/6 = 1/2'),A('Üçüncü gün','Toplamın 2/3’ü satılır.','1/2 × 2/3 = 1/3'),A('Kalanı bul','Üç günde satılan 1/2 + 1/3 = 5/6’dır.','1 − 5/6 = 1/6'),A('Başlangıç','Bütünün 1/6’sı 30 koli.','30 × 6 = 180 koli')],
 puf='Bir adımın miktarı önceki adımların toplamına bağlıysa önce hepsini bütünün kesri olarak yaz, sonra toplamı 1’den çıkar.')

# ---------- 05 kolay · tamamı ----------
assert Fr(21)/3*7==49 and Fr(21)*3/7==9 and Fr(49-21)==28 and 21*3==63 and 21*7==147 and Fr(21,7)==3
mkk('0005','kolay','ksb-tamami','Kesrin tamamını bulma','Bütünü Bulma','Bir kesrin karşılığı verilen sayıdan bütünü bulur.','hikâyeli',2,
 'K-KESB-02 (kesrin tamamı) · basketbol isabeti',
 metin='Bir basketbolcu, sezon boyunca attığı serbest atışların 3/7’sini basket yapmıştır.\nBasketle sonuçlanan atış sayısı 21 olduğuna göre bu oyuncu sezon boyunca toplam kaç serbest atış yapmıştır?',
 dogru=49,yan=[(3,'21’i yalnız paya (3) değil paydaya (7) bölmüş.','islem'),(28,'Basket olmayan atış sayısını bulmuş.','dikkat'),(63,'21’i pay (3) ile çarpmış.','islem'),(147,'21’i paydayla çarpmış; paya bölmeyi unutmuş.','islem')],
 istenen='Toplam serbest atış sayısı.',
 ip=['21 atış, atışların 3/7’sine karşılık geliyor; 1/7’si kaç atıştır?'],
 bilgi=[PARCA],
 ad=[A('Bir parça','3/7 = 21 ise 1/7 bunun üçte biridir.','21 ÷ 3 = 7 atış'),A('Tamamı','7 parçanın hepsi.','7 × 7 = 49 atış'),A('Kontrol','49 atışın 3/7’si basket olmalı.','49 ÷ 7 × 3 = 21 ✓')],
 puf='Bir miktarın a/b’si verildiyse önce a’ya bölerek 1/b’yi, sonra b ile çarparak bütünü bul.')

# ---------- 06 orta · iki kesir (kart) ----------
M,E=Fr(30),Fr(24); assert M*Fr(3,5)==E*Fr(3,4)==18 and M+E==54
x=Fr(54)/(Fr(3,5)+Fr(3,4))*1; assert x*Fr(3,5)+x*Fr(3,4)==54
assert Fr(54,2)==27 and Fr(54)/(Fr(3,5)+Fr(3,4))==Fr(40) and Fr(54)*Fr(4,9)==24
mkk('0006','orta','ksb-iki','İki farklı kesirle ifade edilen aynı miktar','Aynı Miktar','Aynı sayıyı iki kesirle ifade eden verilerden iki çokluğun oranını kurup toplamdan birini bulur.','hikâyeli',3,
 'K-KESB-04 (iki kesir) · koleksiyon kartları, toplam bilinen',
 metin='Mert ile Ece’nin toplam 54 koleksiyon kartı vardır.\nMert’in kartlarının 3/5’i, Ece’nin kartlarının 3/4’üne eşittir.\nBuna göre Mert’in kaç kartı vardır?',
 dogru=30,yan=[(18,'Eşit olan ortak sayıyı (3/5’in karşılığı) kart sayısı sanmış.','dikkat'),(24,'Oranı 4 : 5 kurmuş; Mert’e 4 parça (24) vermiş.','bilgi'),(27,'Toplamı ikiye bölmüş; iki arkadaşın eşit kartı olduğunu sanmış.','bilgi'),(40,'Ortak değere k deyip M = 3k/5, E = 3k/4 yazmış; 27k/20 = 54 → k = 40 bulup k’yı Mert’in kartı sanmış.','bilgi')],
 istenen='Mert’in kart sayısı.',
 ip=['Ortak değere k de; Mert’in ve Ece’nin kart sayısını k cinsinden yaz.'],
 bilgi=[ESIT],
 ad=[A('Eşitliği yaz','Mert’in 3/5’i Ece’nin 3/4’üne eşit.','3M/5 = 3E/4'),A('Çapraz çarp','Payları sadeleştirip içler dışlar çarpımı yap.','M/5 = E/4 → 4M = 5E → M : E = 5 : 4'),A('Toplamla eşitle','Toplam 9 parça, bir parça 6 kart.','54 ÷ 9 = 6 → M = 5 × 6 = 30')],
 puf='Payları eşit iki kesir birbirine eşitse çokluklar paydalarla doğru orantılıdır: 3M/5 = 3E/4 ise M : E = 5 : 4. Paylar farklıysa önce payları eşitle.')

# ---------- 07 zor · iki kesir (sınıf gözlük) ----------
N=Fr(120); kiz=N*Fr(3,5); erk=N-kiz; gk=kiz/4; ge=erk/3
assert (kiz,erk,gk,ge,gk+ge)==(72,48,18,16,34) and Fr(17,60)*N==34 and erk-ge==32 and kiz-gk==54 and N-34==86
mkk('0007','zor','ksb-iki','İki farklı kesirle ifade edilen aynı miktar','Kız ve Erkek Öğrenciler','Bir sınıftaki iki grubun farklı kesirlerini birleştirip toplam üzerinden istenen alt grubu bulur.','hikâyeli',5,
 'K-KESB-04 (iki kesir) · sınıfta gözlüklü kız ve erkek öğrenciler',
 metin='Bir sınıftaki öğrencilerin 3/5’i kızdır.\nKız öğrencilerin 1/4’ü, erkek öğrencilerin 1/3’ü gözlüklü olup sınıfta toplam 34 gözlüklü öğrenci vardır.\nBuna göre bu sınıfta gözlüğü olmayan erkek öğrenci sayısı kaçtır?',
 dogru=32,yan=[(16,'Gözlüklü erkek öğrenci sayısını bulmuş.','dikkat'),(48,'Sınıftaki erkek öğrenci sayısını bulmuş.','dikkat'),(54,'Gözlüksüz kız öğrenci sayısını bulmuş.','dikkat'),(86,'Sınıftaki gözlüksüz öğrencilerin tamamını bulmuş.','dikkat')],
 istenen='Gözlüğü olmayan erkek öğrenci sayısı.',
 ip=['Sınıf mevcuduna n de; gözlüklü kız ve gözlüklü erkek sayılarını n’nin kesri olarak yazıp toplamı 34’e eşitle.'],
 bilgi=[PARCA],
 ad=[A('Gruplar','Kızlar 3/5, erkekler 2/5.','Gözlüklü kız: 3/5 × 1/4 = 3/20 · gözlüklü erkek: 2/5 × 1/3 = 2/15'),A('Toplam gözlüklü','Paydalar 60’ta eşitlenir.','9/60 + 8/60 = 17/60'),A('Sınıf mevcudu','17/60 = 34 ise 1/60 = 2.','n = 2 × 60 = 120'),A('Gözlüksüz erkek','Erkekler 48, bunların 1/3’ü gözlüklü.','48 × 2/3 = 32')],
 puf='Alt grupların kesirleri farklı bütünlere uygulanıyorsa hepsini sınıf mevcudunun kesri haline getirip topla.')

# ---------- 08 kolay · kap ----------
T=Fr(60); assert T*(Fr(7,10)-Fr(2,5))==18 and Fr(18,3)*5==30 and 18*10//5==36 and Fr(18,3)*7==42 and 18*10==180
mkk('0008','kolay','ksb-kap','Artan–eksilen miktarlar (depo, pil)','Artan Miktar','Doluluk farkından yakıt tankının kapasitesini bulur.','hikâyeli',2,
 'K-KESB-03 (artan–eksilen) · yakıt tankı, doluluk farkı',
 metin='Bir otomobilin yakıt tankının 2/5’i doludur.\nTanka 18 litre benzin eklendiğinde tankın 7/10’u dolmaktadır.\nBuna göre bu tankın kapasitesi kaç litredir?',
 dogru=60,yan=[(30,'Farkı 3/10 bulup bir parçayı 6 L hesaplamış; tankı 5 parça (2/5’in paydası) sanıp 6 × 5 yapmış.','islem'),(36,'Doluluk farkını payları çıkararak 5/10 bulmuş: 18 ÷ 5 × 10.','islem'),(42,'Bir parçayı (6 L) bulup 7 ile çarpmış; bu, tankın yalnız 7/10’u.','dikkat'),(180,'18 L’yi 1/10’a karşılık sanıp paydayla çarpmış.','bilgi')],
 istenen='Tankın kapasitesi (L).',
 ip=['Eklenen 18 litre, tankın kaçta kaçıdır? Dolulukların farkını bul.'],
 bilgi=[FARK,KAP],
 ad=[A('Doluluk farkı','2/5 = 4/10; fark eklenen benzindir.','7/10 − 4/10 = 3/10'),A('Tank kapasitesi','Tankın 3/10’u 18 L ise 1/10’u 6 L.','18 ÷ 3 = 6 → 6 × 10 = 60 L'),A('Kontrol','60 L’nin 2/5’i ile 7/10’u arasındaki fark 18 L olmalı.','24 L → 42 L, 42 − 24 = 18 ✓')],
 puf='Eklenen ya da alınan miktar, iki doluluk kesrinin farkına karşılık gelir; önce paydaları eşitle.')

# ---------- 09 orta · kap (pil) ----------
assert Fr(5,6)-Fr(1,3)==Fr(1,2) and Fr(45)/Fr(1,2)==90 and Fr(5,6)*90==75 and Fr(1,3)*90==30 and 45*3==135
mkk('0009','orta','ksb-kap','Artan–eksilen miktarlar (depo, pil)','Eksilen Miktar','Pil doluluk değişiminden kullanım süresini sabit hızla orantılar.','hikâyeli',3,
 'K-KESB-03 (artan–eksilen) · telefon pili, süre',
 metin='Bir telefonun kullanımına başlandığında pilin 5/6’sı doludur.\n45 dakika sonra pilin 1/3’ü kalıyor.\nPil sabit hızla boşaldığına göre telefon kullanıma başlandığı andan itibaren kaç dakika sonra tamamen boşalır?',
 dogru=75,yan=[(30,'Kalan şarjın (1/3) bitme süresini hesaplamış.','dikkat'),(45,'Verilen süreyi cevap sanmış; telefonun tamamen boşalmasını hesaplamamış.','dikkat'),(90,'Pilin tamamen doluyken bitme süresini (90 dk) bulmuş.','dikkat'),(135,'45 dakikada pilin 1/3’ünün bittiğini sanıp tam dolu pil süresini bulmuş.','bilgi')],
 istenen='5/6 doluluktan tamamen boşalmaya kadar geçen süre (dk).',
 ip=['45 dakikada pilin kaçta kaçı bitmiştir? Pil sabit hızla boşalıyor.'],
 bilgi=[FARK],
 ad=[A('Harcanan şarj','5/6’dan 1/3’e inildi.','5/6 − 1/3 = 5/6 − 2/6 = 1/2'),A('Tam pil süresi','Pilin yarısı 45 dakika ise tamamı 90 dakika.','45 × 2 = 90 dk'),A('İstenen süre','Başlangıçta pilin 5/6’sı var.','90 × 5/6 = 75 dk')],
 puf='Sabit hızla boşalan pilde süre, harcanan şarj kesriyle doğru orantılıdır; önce tam pilin süresini bul.')

# ---------- 10 orta · kap (akvaryum) ----------
T=Fr(120); assert T*(Fr(5,6)-Fr(1,3))==60 and T*(Fr(3,4)-Fr(1,3))==50 and T*Fr(3,4)==90 and T*Fr(1,3)==40
mkk('0010','orta','ksb-kap','Artan–eksilen miktarlar (depo, pil)','Alınan ve Eklenen','Önce alınan sonra eklenen su miktarlarını doluluk kesirleriyle ilişkilendirip alınan miktarı bulur.','hikâyeli',3,
 'K-KESB-03 (artan–eksilen) · akvaryum, boşaltma ve ekleme',
 metin='Bir akvaryumun 3/4’ü suyla doluyken akvaryumdan bir miktar su boşaltılıyor ve akvaryumun 1/3’ü dolu kalıyor.\nDaha sonra akvaryuma 60 litre su eklenince akvaryumun 5/6’sı doluyor.\nBuna göre akvaryumdan boşaltılan su kaç litredir?',
 dogru=50,yan=[(40,'Boşaltmadan sonra akvaryumda kalan suyu (kapasitenin 1/3’ü) bulmuş.','dikkat'),(60,'Eklenen suyu boşaltılan su sanmış.','dikkat'),(90,'Başlangıçta akvaryumdaki suyu (3/4) bulmuş.','dikkat'),(120,'Akvaryumun kapasitesini bulup durmuş.','dikkat')],
 istenen='Boşaltılan su miktarı (L).',
 ip=['Önce eklenen 60 litrenin, kapasitenin kaçta kaçı olduğunu doluluk farkından bul.'],
 bilgi=[FARK,KAP],
 ad=[A('Kapasiteyi bul','Eklenen su 1/3’ten 5/6’ya çıkarmıştır.','5/6 − 1/3 = 1/2 → kapasite 60 × 2 = 120 L'),A('Boşaltılan kesir','3/4’ten 1/3’e inilmiştir.','3/4 − 1/3 = 9/12 − 4/12 = 5/12'),A('Boşaltılan su','Kapasitenin 5/12’si.','120 × 5/12 = 50 L')],
 puf='Önce verilen miktarı doluluk farkına bağlayıp kapasiteyi bul; sonra istenen farkı kapasitenin kesri olarak hesapla.')

# ---------- 11 zor · kap (su deposu) ----------
T=Fr(288); b=T*Fr(5,8); k=b*Fr(2,5); y=b-k
assert b==180 and k==72 and y==108 and y+36==144==T/2 and T*Fr(3,8)==108
mkk('0011','orta','ksb-kap','Artan–eksilen miktarlar (depo, pil)','Boşaltma ve Doldurma','Boşaltılan kesir ile sonradan eklenen miktarı birleştirip başlangıçtaki su miktarını bulur.','hikâyeli',4,
 'K-KESB-03 (artan–eksilen) · su deposu, suyun 2/5’i boşaltılıyor',
 metin='Bir su deposunun 5/8’i doludur.\nDepodaki suyun 2/5’i boşaltılıyor, ardından depoya 36 litre su eklenince depo tam yarısına kadar doluyor.\nBuna göre başlangıçta depoda kaç litre su vardı?',
 dogru=180,yan=[(72,'Boşaltılan su miktarını (suyun 2/5’i) vermiş.','dikkat'),(108,'Boşaltmadan sonra depoda kalan suyu vermiş.','dikkat'),(144,'Son durumdaki suyu (deponun yarısı) vermiş.','dikkat'),(288,'Deponun kapasitesini vermiş.','dikkat')],
 istenen='Başlangıçtaki su miktarı (L).',
 ip=['Boşaltmadan sonra depoda kalan suyu deponun kesri olarak yaz; 36 litre bu kesri nereye getirmiş?'],
 bilgi=[KALAN,KAP],
 ad=[A('Boşaltmadan sonra','Suyun 2/5’i çıkarsa 3/5’i kalır.','5/8 × 3/5 = 3/8 (deponun)'),A('Eklenen kesir','3/8’den 1/2’ye çıkmıştır.','1/2 − 3/8 = 1/8 → 36 L'),A('Kapasite','Deponun 1/8’i 36 L.','36 × 8 = 288 L'),A('Başlangıç','Başlangıçta deponun 5/8’i doluydu.','288 × 5/8 = 180 L')],
 puf='Kesirli boşaltma ve ekleme sorularında her aşamadaki doluluğu deponun kesri olarak yaz; verilen miktarı doluluk farkına bağla.')

# ---------- 12 orta · tamamı (iki kesir, okul) ----------
S=Fr(70); yurt=S*Fr(4,5); N=yurt/Fr(2,7)
assert yurt==56 and N==196 and S*Fr(2,7)==20 and S*Fr(7,2)==245 and yurt*7==392
mkk('0012','orta','ksb-tamami','Kesrin tamamını bulma','Aynı Miktar','Aynı sayının iki kesriyle verilen bilgiden okul mevcudunu bulur.','hikâyeli',3,
 'K-KESB-02 (kesrin tamamı) · yurtta kalan öğrenciler ve servis',
 metin='Bir okulda yurtta kalan öğrencilerin sayısı, okuldaki tüm öğrencilerin 2/7’sine eşittir.\nBu sayı, servis kullanan öğrencilerin 4/5’ine de eşittir.\nServis kullanan öğrenci sayısı 70 olduğuna göre bu okuldaki öğrenci sayısı kaçtır?',
 dogru=196,yan=[(20,'Yurtta kalanları servis kullananların 2/7’si olarak hesaplamış.','dikkat'),(56,'Yurtta kalan öğrenci sayısını bulup durmuş.','dikkat'),(245,'70’i okulun 2/7’sine karşılık sanıp 70 ÷ 2 × 7 yapmış.','dikkat'),(392,'56’yı 7 ile çarpıp 2’ye bölmeyi unutmuş.','islem')],
 istenen='Okuldaki öğrenci sayısı.',
 ip=['Yurtta kalan sayı, servis kullananların 4/5’i olarak da yazılır; önce bunu hesapla.'],
 bilgi=[PARCA,ESIT],
 ad=[A('Yurtta kalan sayısı','Servis kullananların 4/5’i.','70 × 4/5 = 56'),A('Okul mevcudu','56, okulun 2/7’si ise 1/7’si 28’dir.','56 ÷ 2 = 28'),A('Tamamı','7 parçanın hepsi.','28 × 7 = 196')],
 puf='Aynı sayı iki farklı bütünün kesriyle verilmişse önce bilinen bütünden sayıyı bul, sonra diğer bütüne geç.')

# ---------- 13 kolay · artırma ----------
assert Fr(72)*Fr(7,6)==84 and Fr(72)/6==12 and 84-14==70 and Fr(84)*Fr(7,6)==98 and Fr(84,6)==14
mkk('0013','kolay','ksb-artir','Kesir kadar artırma ve azaltma','Kesir Kadar Artış','Fiyatın kesri kadar artırılmasından eski fiyatı bulur.','hikâyeli',2,
 'K-KESB-05 (artırma) · konser bileti, tek artış',
 metin='Bir konser biletinin fiyatı, fiyatının 1/6’sı kadar artırılarak 84 TL olmuştur.\nBuna göre biletin artırmadan önceki fiyatı kaç TL’dir?',
 dogru=72,yan=[(12,'Eski fiyatın 1/6’sı olan artış miktarını vermiş.','dikkat'),(14,'84’ün 1/6’sını artış sanıp onu bulmuş.','bilgi'),(70,'84’ten 84’ün 1/6’sını çıkarmış; artışı yeni fiyatın kesri almış.','bilgi'),(98,'84’ü 7/6 ile çarpmış; eski fiyattan yeniye gitmiş.','bilgi')],
 istenen='Biletin artırmadan önceki fiyatı (TL).',
 ip=['Eski fiyata 6 parça diyelim; artırılmış fiyat kaç parçadır?'],
 bilgi=[ART],
 ad=[A('Artırılmış fiyat','Eski fiyatın 1/6’sı kadar artış, yeni fiyatı 7/6 katı yapar.','7/6 × eski = 84'),A('Eski fiyat','7 parça 84 TL ise 1 parça 12 TL.','84 ÷ 7 = 12 → 12 × 6 = 72 TL'),A('Kontrol','72 TL’nin 1/6’sı kadar artış 12 TL’dir.','72 + 12 = 84 ✓')],
 puf='“1/6’sı kadar artırma” miktarı 7/6 katına çıkarır; “1/6’sı kadar azaltma” ise 5/6 katına indirir.')

# ---------- 14 orta · ardışık artış-azalış ----------
assert Fr(540)/(1+Fr(1,2))/(1-Fr(1,4))==480 and Fr(3,2)*Fr(3,4)==Fr(9,8) and Fr(480)*Fr(9,8)==540
assert Fr(540)*Fr(2,3)==360 and Fr(540)*Fr(3,4)==405 and Fr(540)/(1+Fr(1,2)-Fr(1,4))==432 and Fr(540)*Fr(4,3)==720
mkk('0014','orta','ksb-artir','Kesir kadar artırma ve azaltma','Ardışık Değişim','Zam ve indirimi yeni fiyatın kesriyle uygulayıp ilk fiyatı bulur.','hikâyeli',3,
 'K-KESB-05 (artırma-azaltma) · mont, zam ve indirim',
 metin='Bir mağaza bir montun fiyatına, fiyatının 1/2’si kadar zam yapmıştır. Bir süre sonra zamlı fiyatın 1/4’ü kadar indirim yapmıştır.\nMontun son fiyatı 540 TL olduğuna göre zamdan önceki fiyatı kaç TL’dir?',
 dogru=480,yan=[(360,'Yalnız zammı geri almış: 540 × 2/3.','bilgi'),(405,'İndirimi geri alırken 3/4 çarpanını ters yönde kullanıp 540 × 3/4 yapmış.','bilgi'),(432,'Net artışı 1/2 − 1/4 = 1/4 sanıp 540 ÷ 5/4 hesaplamış.','bilgi'),(720,'Yalnız indirimi geri almış: 540 × 4/3.','bilgi')],
 istenen='Zamdan önceki fiyat (TL).',
 ip=['Zam ve indirimin çarpanlarını ayrı ayrı yaz ve çarp.'],
 bilgi=[ART,ARDART],
 ad=[A('Çarpanlar','1/2 zam → 3/2 katı; zamlı fiyatın 1/4’ü indirim → 3/4 katı.','3/2 × 3/4 = 9/8'),A('Denklemi kur','Son fiyat ilk fiyatın 9/8’idir.','9/8 × ilk fiyat = 540'),A('İlk fiyat','9 parça 540 TL ise 1 parça 60 TL.','540 ÷ 9 = 60 → 60 × 8 = 480 TL')],
 puf='Artış ve azalış çarpanlarını çarpıp son miktarı bu net çarpana eşitle; net değişimi kesirleri toplayarak bulma.')

# ---------- 15 orta · artırma (sarmaşık) ----------
b0=Fr(60); b1=b0*Fr(4,3); b2=b1*Fr(6,5)
assert (b1,b2)==(80,96) and b2-b0==36 and b1-b0==20 and b2-b1==16 and b0/5==12
mkk('0015','orta','ksb-artir','Kesir kadar artırma ve azaltma','Ardışık Uzama','İki haftalık uzamayı ardışık kesirlerle hesaplayıp toplam uzamayı bulur.','hikâyeli',3,
 'K-KESB-05 (artırma) · sarmaşığın boyu, iki hafta',
 metin='Bir sarmaşığın boyu ilk hafta boyunun 1/3’ü kadar uzamış, ikinci hafta da ilk haftanın sonundaki boyunun 1/5’i kadar uzamıştır.\nİki haftanın sonunda sarmaşığın boyu 96 cm olduğuna göre sarmaşık bu iki haftada toplam kaç cm uzamıştır?',
 dogru=36,yan=[(12,'İkinci haftadaki uzamayı ilk boyun 1/5’i olarak hesaplamış.','dikkat'),(16,'Yalnız ikinci haftadaki uzamayı bulmuş.','dikkat'),(20,'Yalnız ilk haftadaki uzamayı bulmuş.','dikkat'),(60,'İlk boyu bulup uzamayı hesaplamamış.','dikkat')],
 istenen='İki haftadaki toplam uzama (cm).',
 ip=['Her haftanın çarpanını yaz (örneğin 1/3’ü kadar uzama kaç katına çıkarır?) ve çarp.'],
 bilgi=[ART],
 ad=[A('Çarpanlar','Birinci hafta 4/3, ikinci hafta 6/5 katı.','4/3 × 6/5 = 8/5'),A('İlk boy','Son boy ilk boyun 8/5’i.','96 ÷ 8 × 5 = 60 cm'),A('Toplam uzama','Son boydan ilk boyu çıkar.','96 − 60 = 36 cm')],
 puf='Ardışık uzamalarda çarpanları çarpıp son boydan ilk boyu bul; uzama miktarı son boy ile ilk boyun farkıdır.')

# ---------- 16 zor · artırma (iki kişi) ----------
m=Fr(8); V=3*m; A_=4*m
assert A_-V==V/3 and A_*Fr(3,4)+V*Fr(2,3)==40 and A_==32 and V==24 and V*Fr(2,3)==16 and V+A_==56
mkk('0016','zor','ksb-artir','Kesir kadar artırma ve azaltma','Fark Kesri','Bir kişinin parasının diğerinden kesir kadar fazla olmasını iki harcamanın ardından kalan toplamla birleştirir.','hikâyeli',4,
 'K-KESB-05 (artırma) · Ali’nin parası Veli’ninkinden 1/3’ü kadar fazla',
 metin='Ali’nin parası, Veli’nin parasından Veli’nin parasının 1/3’ü kadar fazladır.\nAli kendi parasının 1/4’ünü, Veli de kendi parasının 1/3’ünü harcadıktan sonra ikisinin kalan paraları toplamı 40 TL olmaktadır.\nBuna göre Ali’nin başlangıçtaki parası kaç TL’dir?',
 dogru=32,yan=[(16,'Veli’nin harcamadan sonra kalan parasını vermiş.','dikkat'),(24,'Veli’nin başlangıçtaki parasını vermiş.','dikkat'),(40,'Harcamalardan sonra kalan toplamı cevap sanmış.','dikkat'),(56,'İki kişinin başlangıçtaki toplam parasını vermiş.','dikkat')],
 istenen='Ali’nin başlangıçtaki parası (TL).',
 ip=['Veli’nin parasını 3 birim alırsan Ali’nin parası kaç birimdir? Harcamadan sonra kalanları birim cinsinden yaz.'],
 bilgi=[ART],
 ad=[A('Parayı birimle yaz','Veli 3m, Ali 3m + m = 4m.','Ali = 4m · Veli = 3m'),A('Kalanları yaz','Ali’nin 3/4’ü, Veli’nin 2/3’ü kalır.','4m × 3/4 = 3m · 3m × 2/3 = 2m'),A('Birimi bul','Kalanların toplamı 40 TL.','3m + 2m = 5m = 40 → m = 8'),A('Ali’nin parası','Ali 4 birim.','4 × 8 = 32 TL')],
 puf='“Birinin parası diğerinden kesir kadar fazla” ifadesini iki parayı aynı birimle (3m ve 4m) yazarak ele al; kesirlerle uğraşma.')

# ---------- 17 kolay · paylaşım ----------
assert Fr(150)*6==900 and Fr(900)/Fr(3,4)==1200 and Fr(900)*Fr(3,4)==675 and Fr(900,3)==300 and Fr(900)/Fr(1,4)==3600
mkk('0017','kolay','ksb-paylas','Eşit paylaşım ve kesirlerin karşılaştırılması','Eşit Paylaşım','Pastanın bir kesrinin eşit paylaşılmasından pastanın tamamını bulur.','hikâyeli',2,
 'K-KESB-06 (paylaşım) · pastanın 3/4’ü altı kişiye',
 metin='Bir pastanın 3/4’ü 6 kişiye eşit olarak paylaştırılmış ve her kişi 150 gram pasta almıştır.\nBuna göre pastanın tamamı kaç gramdır?',
 dogru=1200,yan=[(300,'Paylaştırılan 900 gramı 3’e bölüp bir parçayı (1/4) vermiş.','dikkat'),(675,'900 gramın 3/4’ünü almış; kesri ters kullanmış.','bilgi'),(900,'Paylaştırılan pasta miktarını tamamı sanmış.','dikkat'),(3600,'900’ü 1/4’e bölmüş; pay yerine tamamlayıcı kesri (1/4) kullanmış.','bilgi')],
 istenen='Pastanın tamamı (g).',
 ip=['Önce 6 kişinin aldığı pasta toplam kaç gramdır? Bu miktar pastanın kaçta kaçıdır?'],
 bilgi=[PAYDA,PARCA],
 ad=[A('Paylaşılan miktar','6 kişi 150 gram aldı.','6 × 150 = 900 g (pastanın 3/4’ü)'),A('Pastanın tamamı','3/4’ü 900 g ise 1/4’ü 300 g.','900 ÷ 3 × 4 = 1200 g'),A('Kontrol','1200 g’ın 3/4’ü 6 kişiye 150 g’dan dağılmalı.','1200 × 3/4 = 900 = 6 × 150 ✓')],
 puf='Eşit paylaşımda önce paylaşılan toplam miktarı (kişi sayısı × pay) bul, sonra bu miktarın bütünün hangi kesri olduğuna bak.')

# ---------- 18 orta · paylaşım (pizza) ----------
assert Fr(1,5)-Fr(1,6)==Fr(1,30) and 1200//30==40 and 40*5==200 and 40*6==240 and 40*11==440
mkk('0018','orta','ksb-paylas','Eşit paylaşım ve kesirlerin karşılaştırılması','Pay Farkı','Kişi sayısı artınca eşit payın kesirce değişimini bir ağırlık farkına bağlar.','hikâyeli',3,
 'K-KESB-06 (paylaşım) · pizza, bir kişi daha katılıyor',
 metin='Bir pizza 5 kişi arasında eşit olarak paylaştırılacakken bir kişi daha gelmiş ve pizza 6 kişi arasında eşit olarak paylaştırılmıştır.\nBu durumda her kişinin payı 40 gram azaldığına göre pizzanın tamamı kaç gramdır?',
 dogru=1200,yan=[(40,'Azalma miktarını pizzanın ağırlığı sanmış.','dikkat'),(200,'Azalmayı pizzanın 1/5’ine eşitlemiş (40 × 5).','bilgi'),(240,'Azalmayı pizzanın 1/6’sına eşitlemiş (40 × 6).','bilgi'),(440,'Kişi sayılarını toplayıp 40 ile çarpmış (40 × 11).','bilgi')],
 istenen='Pizzanın tamamı (g).',
 ip=['Beş kişide bir kişinin payı pizzanın 1/5’i; altı kişide kaçta kaçı? İkisinin farkı kaç gram?'],
 bilgi=[PAYDA,FARK],
 ad=[A('Payları yaz','5 kişide pay 1/5, 6 kişide 1/6.','1/5 ve 1/6'),A('Pay farkı','Paydalar 30’da eşitlenir.','1/5 − 1/6 = 6/30 − 5/30 = 1/30'),A('Pizzanın tamamı','Pizzanın 1/30’u 40 g.','40 × 30 = 1200 g')],
 puf='Kişi sayısı değişince pay farkı 1/n − 1/(n+1) = 1/(n(n+1)) olur; bu farkı verilen miktara eşitle.')

# ---------- 19 zor · geri sarma (abone) ----------
x0=Fr(84); y1=x0*Fr(5,4)-25; y2=y1*Fr(5,4)-25
assert (y1,y2)==(80,75)
inv=lambda y:(y+25)*Fr(4,5)
assert inv(inv(y2))==84 and inv(y2)==80
assert (y2-25)*Fr(4,5)==40 and (Fr(40)-25)*Fr(4,5)==12
assert y2*Fr(16,25)==48
mkk('0019','zor','ksb-yeni','Yeni nesil, kural tanımlı ve geri sarma','Geri Sarma','Her ay tekrarlanan bir artış ve sabit kayıp düzeninde iki ay sonraki değerden başlangıcı bulur.','hikâyeli',4,
 'K-KESB-07 (geri sarma) · kanal aboneleri, 1/4 artış ve 25 kayıp',
 metin='Bir yerel haber kanalında her ay, ayın başındaki abone sayısının 1/4’ü kadar yeni abone katılmakta ve ayın sonunda 25 abone kanaldan ayrılmaktadır.\nBu düzen iki ay boyunca aynen sürmüş ve ikinci ayın sonunda, ayrılanlar da düşüldükten sonra kanalın 75 abonesi kalmıştır.\nBuna göre kanalın ilk ayın başındaki abone sayısı kaçtır?',
 dogru=84,yan=[(12,'Geri giderken ayrılanları eklemek yerine çıkarmış: (75 − 25) ÷ 5 × 4, sonra bir kez daha.','bilgi'),(48,'Ayrılan 25 abonenin etkisini yok sayıp yalnız 4/5 ile iki kez geri gitmiş.','dikkat'),(75,'Son abone sayısını başlangıç sanmış.','dikkat'),(80,'Yalnız bir ayı geri almış; birinci ayın sonundaki sayıyı bulmuş.','dikkat')],
 istenen='İlk ayın başındaki abone sayısı.',
 ip=['Son durumdan geriye doğru git; her ayda yapılan işlemleri ters sırayla geri almayı dene.'],
 bilgi=[GERI],
 ad=[A('Bir ay nasıl işliyor','x abone → x × 5/4 − 25.','x → 5x/4 − 25'),A('İkinci ayı geri al','Önce 25’i ekle, sonra 5/4’e böl.','(75 + 25) × 4/5 = 80'),A('Birinci ayı geri al','Aynı işlemi tekrarla.','(80 + 25) × 4/5 = 84'),A('Kontrol','84 × 5/4 − 25 = 80 ve 80 × 5/4 − 25 = 75.','84 → 80 → 75 ✓')],
 puf='Her adımda “artır, sonra çıkar” işlemini tersine çevirmek için önce çıkarılanı geri ekle, sonra çarpanı böl; işlem sırasını ters çevir.')

# ---------- 20 orta · karşılaştırma (parkur) ----------
par=Fr(240); a_,b_,c_=par*Fr(5,8),par*Fr(7,12),par*Fr(3,5)
assert (a_,b_,c_)==(150,140,144) and c_-b_==4 and a_-b_==10 and a_-c_==6 and Fr(5,8)-Fr(7,12)==Fr(1,24)
assert Fr(2,4)*240==120 and Fr(4)/(Fr(3,5)-Fr(7,12))==240
mkk('0020','orta','ksb-paylas','Eşit paylaşım ve kesirlerin karşılaştırılması','Kesirleri Karşılaştırma','Aynı parkurun farklı kesirlerini karşılaştırıp bir ara farktan parkur uzunluğunu ve istenen farkı bulur.','hikâyeli',3,
 'K-KESB-06 (karşılaştırma) · bisiklet turu, üç sürücü',
 metin='Üç bisikletçi aynı parkuru sürmektedir. Belirli bir anda Ali parkurun 5/8’ini, Bora 7/12’sini, Can ise 3/5’ini tamamlamıştır.\nCan ile Bora arasındaki yol farkı 4 km olduğuna göre bu anda en çok yol almış olan bisikletçi ile en az yol almış olan bisikletçi arasındaki fark kaç kilometredir?',
 dogru=10,yan=[(4,'Verilen farkı (Can ile Bora) cevap sanmış.','dikkat'),(6,'En çok yol alan Ali ile Can arasındaki farkı bulmuş.','dikkat'),(120,'Pay ve paydaları ayrı ayrı çıkarıp 5/8 − 7/12’yi (5 − 7)/(8 − 12) = 1/2 bulmuş.','bilgi'),(240,'Parkurun uzunluğunu bulup durmuş.','dikkat')],
 istenen='En çok ve en az yol alan bisikletçiler arasındaki fark (km).',
 ip=['Üç kesri 120’lik paydada yazıp kimin önde, kimin geride olduğunu belirle.'],
 bilgi=[FARK],
 ad=[A('Kesirleri karşılaştır','Payda 120: Ali 75/120, Bora 70/120, Can 72/120.','Ali en önde, Bora en geride'),A('Parkuru bul','Can − Bora farkı 2/120 = 1/60 ve 4 km.','4 × 60 = 240 km'),A('İstenen fark','Ali − Bora farkı 5/120 = 1/24.','240 × 1/24 = 10 km')],
 puf='Kesirleri ortak paydada yaz; sıralamayı ve aralarındaki farkları pay farkından oku.')

# ---------- 21 orta · öncüllü ----------
Ap,Bp,Cp=Fr(90),Fr(80),Fr(75)
assert Ap*Fr(2,3)==Bp*Fr(3,4)==Cp*Fr(4,5)==60 and Ap+Bp+Cp==245
# k ortak değer: A=3k/2,B=4k/3,C=5k/4, toplam 49k/12=245 → k=60 (tek çözüm)
k=Fr(245)*12/49; assert k==60 and (3*k/2,4*k/3,5*k/4)==(90,80,75)
I=(Ap==90); II=(Ap<Bp and Ap<Cp); III=(Ap-Bp==5)
assert (I,II,III)==(True,False,False) and Bp-Cp==5
SIRA=['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III']
mkk('0021','orta','ksb-iki','İki farklı kesirle ifade edilen aynı miktar','Öncüllü Kesir','Aynı miktarı farklı kesirlerle ifade eden paralardan çıkan sonuçları öncüllerle sınar.','öncüllü',3,
 'K-KESB-04 (iki kesir) · Ali, Bora ve Can’ın parası, öncüllü',
 metin='Ali, Bora ve Can’ın toplam 245 TL’si vardır.\nAli’nin parasının 2/3’ü, Bora’nın parasının 3/4’ü ve Can’ın parasının 4/5’i birbirine eşittir.\nBuna göre,\nI. Ali’nin parası 90 TL’dir.\nII. Üç kişi arasında en az parası olan Ali’dir.\nIII. Ali ile Bora’nın paraları arasındaki fark 5 TL’dir.\nifadelerinden hangileri doğrudur?',
 dogru='Yalnız I',sira=SIRA,yan=[('Yalnız II','Kesri en küçük olanın (2/3) parasının da en az olduğunu sanmış; Ali’nin parasını da hatalı bulmuş.','bilgi'),('I ve II','Ali’nin parasını doğru bulmuş; ama en küçük kesre sahip Ali’nin en az parası olduğunu sanmış.','bilgi'),('I ve III','Ali ile Bora arasındaki farkı (10 TL) Bora ile Can arasındaki farkla (5 TL) karıştırmış.','dikkat'),('I, II ve III','Hem küçük kesri küçük para sanmış hem de farkı 5 TL bulmuş.','bilgi')],
 istenen='Doğru olan öncüller.',
 ip=['Eşit değere k de; üç paranın k cinsinden değerini yazıp toplamı 245’e eşitle.'],
 bilgi=[ESIT],
 ad=[A('Oranı kur','Eşit değerde paralar, kesirlerin tersiyle orantılıdır.','A : B : C = 3/2 : 4/3 : 5/4 = 18 : 16 : 15'),A('Parçayı bul','Toplam 49 parça 245 TL.','245 ÷ 49 = 5 TL'),A('Paraları bul','Her parça 5 TL.','A = 90 · B = 80 · C = 75'),A('Öncülleri sına','I doğru; II yanlış (en az para 75 ile Can’da); III yanlış (90 − 80 = 10).','Yalnız I')],
 puf='Eşit kesirli ifadelerde ortak değere k de; her çokluk k’nın bir katı olur, toplamdan k bulunur.')

# ---------- 22 kolay · yeni nesil (genel isabet oranı) ----------
sol=[x for x in range(1,2000) if Fr(3+5,x+8)==Fr(2,3)]
assert sol==[4]
assert [x for x in range(1,2000) if Fr(3,x)+Fr(5,8)==Fr(2,3)]==[72]
mkk('0022','kolay','ksb-yeni','Yeni nesil, kural tanımlı ve geri sarma','Genel Oran','Tanımlanan genel isabet oranı kuralını uygulayarak bilinmeyen atış sayısını bulur.','yeni nesil',3,
 'K-KESB-07 (yeni nesil) · genel isabet oranı tanımı',
 metin='Bir basketbolcunun birden fazla maçtaki toplam isabetli atış sayısının, toplam atış sayısına oranına “genel isabet oranı” denir.\nBu oyuncu birinci maçta x atıştan 3’ünü, ikinci maçta 8 atıştan 5’ini isabet ettirmiş ve iki maçtaki genel isabet oranı 2/3 olmuştur.\nBuna göre x pozitif tam sayısı kaçtır?',
 dogru=4,yan=[(8,'2(x + 8) = 24 eşitliğini açarken 16’yı unutup 2x + 8 = 24 yazmış.','islem'),(12,'x + 8 = 12 bulup paydadaki 8’i çıkarmayı unutmuş.','islem'),(20,'x + 8 = 12 bulduktan sonra 8’i çıkarmak yerine eklemiş.','islem'),(72,'Genel oranı iki maçın oranlarının toplamı sanmış: 3/x + 5/8 = 2/3.','bilgi')],
 istenen='x’in değeri.',
 ip=['Toplam isabetli atış sayısını ve toplam atış sayısını x cinsinden yaz.'],
 bilgi=[B('Genel oran','toplam isabet ÷ toplam atış; maç oranları toplanmaz. Örnek: 2 maçta 3/5 ve 1/5 isabet için genel oran (3 + 1)/(5 + 5) = 4/10 = 2/5')],
 ad=[A('Genel oranı yaz','İsabetler ve atışlar ayrı ayrı toplanır.','(3 + 5)/(x + 8) = 8/(x + 8) = 2/3'),A('Denklemi kur','İçler dışlar çarpımı yap.','2(x + 8) = 24'),A('x’i bul','Denklemi çöz.','x + 8 = 12 → x = 4')],
 puf='Genel oran sorularında oranları değil payları ve paydaları ayrı ayrı topla.')

# ---------- 23 zor · yeni nesil (adım kuralı) ----------
par=Fr(240); kal=par; yol=[]
for kk_ in range(1,6):
    g=kal*Fr(1,kk_+1); yol.append(g); kal-=g
assert kal==40 and yol[3]==12 and kal==par/6 and par/5==48 and par/4==60 and par/3==80
mkk('0023','zor','ksb-yeni','Yeni nesil, kural tanımlı ve geri sarma','Adım Kuralı','Her adımda kalanın değişen bir kesrinin alındığı süreçte kalan mesafeyi sadeleştirerek belirli bir adımın uzunluğunu bulur.','yeni nesil',5,
 'K-KESB-07 (yeni nesil) · robot, k. adımda kalanın 1/(k+1)’i',
 metin='Uzaktan kumandalı bir robot, hedefine şu kurala göre adım adım ilerliyor:\nk. adımda robot, o adımın başında hedefe kalan uzaklığın 1/(k + 1)’i kadar yol alıyor.\n(Yani 1. adımda kalanın 1/2’sini, 2. adımda kalanın 1/3’ünü, 3. adımda kalanın 1/4’ünü, … alıyor.)\n5. adımın sonunda robotun hedefe 40 metre kaldığına göre robotun 4. adımda aldığı yol kaç metredir?',
 dogru=12,yan=[(80,'2. adımdan sonra kalan mesafeyi (uzaklığın 1/3’ü) vermiş.','dikkat'),(40,'5. adımdan sonra kalan mesafeyi vermiş.','dikkat'),(48,'4. adımın kesrini (1/5) toplam uzaklığa uygulamış.','bilgi'),(60,'4. adımın başında kalan mesafeyi (3. adımdan sonra) vermiş.','dikkat')],
 istenen='4. adımda alınan yol (m).',
 ip=['Her adımdan sonra kalan mesafeyi toplam uzaklığın kesri olarak yaz; çarpımlardaki sadeleşmeyi gözle.'],
 bilgi=[KURAL,KALAN],
 ad=[A('Her adımdan sonra kalan','k. adımdan sonra kalanın çarpanı k/(k + 1).','1/2, 1/2 × 2/3 = 1/3, 1/3 × 3/4 = 1/4, 1/4 × 4/5 = 1/5, 1/5 × 5/6 = 1/6'),A('Toplam uzaklık','5 adım sonra uzaklığın 1/6’sı kalmış.','40 × 6 = 240 m'),A('4. adımın başı','3. adımdan sonra uzaklığın 1/4’ü kalmıştı.','240 × 1/4 = 60 m'),A('4. adımın yolu','Bunun 1/5’i alınır.','60 × 1/5 = 12 m')],
 puf='Her adımda kalan çarpanları zincir halinde çarpılırsa payda ile pay birbirini götürür; k adım sonra kalan 1/(k + 1) olur.')

# ---------- 24 zor · iki kesir (ambar) ----------
m=Fr(12); A_=5*m; Bb=6*m
assert A_*Fr(2,5)==Bb*Fr(1,3)==24 and (Bb+A_/5)-(A_-A_/5)==36 and A_+Bb==132
assert 11*36==396 and 11*18==198 and 5*12==60 and 6*12==72 and 7*m-5*m==24
mkk('0024','zor','ksb-iki','İki farklı kesirle ifade edilen aynı miktar','Aktarma','İki depodaki miktarların farklı kesirlerle eşitliğini kurup bir aktarmadan sonraki farktan toplamı bulur.','hikâyeli',5,
 'K-KESB-04 (iki kesir) · iki ambarda buğday, aktarma',
 metin='İki ambarda bulunan buğdaydan, birinci ambardakinin 2/5’i ikinci ambardakinin 1/3’üne eşittir.\nBirinci ambardaki buğdayın 1/5’i ikinci ambara aktarılınca ikinci ambardaki buğday, birinci ambardakinden 36 ton fazla olmuştur.\nBuna göre iki ambarda başlangıçta toplam kaç ton buğday vardı?',
 dogru=132,yan=[(60,'Birinci ambarın başlangıçtaki miktarını (5 parça) vermiş.','dikkat'),(72,'İkinci ambarın başlangıçtaki miktarını (6 parça) vermiş.','dikkat'),(198,'Aktarma sonrası farkı 2 parça sanıp (7 − 5) bir parçayı 18 bulmuş.','bilgi'),(396,'Aktarma sonrası farkı (3 parça) bir parça sanmış; parçayı 36 almış.','dikkat')],
 istenen='Başlangıçtaki toplam buğday (ton).',
 ip=['İki ambarın başlangıç miktarlarını aynı birimle yaz; ardından aktarmayı bu birimle uygula.'],
 bilgi=[ESIT],
 ad=[A('Başlangıç oranı','2A/5 = B/3 ise A : B = 5 : 6.','A = 5m · B = 6m'),A('Aktarma','A’nın 1/5’i (m) B’ye gider.','A = 4m · B = 7m'),A('Birimi bul','Fark 36 ton.','7m − 4m = 3m = 36 → m = 12'),A('Toplam','Başlangıçta 5m + 6m.','11 × 12 = 132 ton')],
 puf='İki farklı kesirle verilen eşitlikten oran çıkar; sonrasında tüm değişimleri aynı birimle (m) yaz ve verilen farkı birime bağla.')

bitir(P,'kesirprobiki',UK)
