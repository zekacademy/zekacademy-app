"""İşçi Emek Problemleri · parti 1 (8 ana + 8 kardeş). Her cevap iki yoldan (evre hesabı + zaman taraması) doğrulanır."""
import sys,os
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,os.path.join(H,'..'))
from ortak import *
P=Parti('isciprob','İşçi Emek Problemleri','prob|İşçi Emek Problemleri')
TT=lambda **k:k
def sirali(s):
    v=[Fr(x.replace(',','.')) if '/' not in x else Fr(x) for x in s]; assert v==sorted(v) and len(set(v))==5, s
    return s
def bitis(evreler,son_hiz,hedef=1):
    """evreler: [(süre, birlikte hız)], ardından iş son_hiz ile biter. Toplam süre (yöntem 1)."""
    w=Fr(0); t=Fr(0)
    for g,h in evreler:
        assert w+g*h<hedef, 'iş evre içinde bitiyor'
        w+=g*h; t+=g
    return t+(hedef-w)/son_hiz
def tara(evreler,son_hiz,hedef=1,dt=Fr(1,240)):
    """Yöntem 2: küçük zaman adımlarıyla işi biriktir."""
    sinir=[];t=Fr(0)
    for g,h in evreler: sinir.append((t,t+g,h)); t+=g
    w=Fr(0); t=Fr(0)
    while w<hedef:
        h=next((hh for a,b,hh in sinir if a<=t<b),son_hiz); w+=h*dt; t+=dt
    return t
def iki_yol(evreler,son_hiz,hedef=1):
    a=bitis(evreler,son_hiz,hedef); b=tara(evreler,son_hiz,hedef); assert a==b,(a,b); return a

IS=B('Bir günlük iş','bir işi a günde bitiren kişi bir günde işin 1/a’sını yapar. Örnek: 6 günde bitiren bir günde 1/6’sını yapar')
BIR=B('Birlikte çalışma','birlikte çalışanların bir birim zamandaki işleri toplanır. Örnek: 1/3 + 1/6 = 1/2 ⇒ birlikte 2 günde biter')
MUS=B('Doldurma ve boşaltma','dolduran musluk havuza ekler (+), boşaltan musluk havuzdan çıkarır (−). Örnek: 1/4 − 1/6 = 1/12 ⇒ havuz 12 saatte dolar')
ISGUN=B('Toplam iş','eşit verimli işçilerde toplam iş = işçi sayısı × gün (× günlük saat). Örnek: 4 işçi 5 günde 20 işçi-günlük iş yapar')

# ===================== 0001 birlikte KOLAY
t=1/(Fr(1,6)+Fr(1,12)); assert t==4 and iki_yol([],Fr(1,6)+Fr(1,12))==4
assert Fr(6,2)==3 and 12-6==6 and Fr(6+12,2)==9 and 6+12==18
s=sirali(['3','4','6','9','18'])
P.R('0001','is-birlikte','Birlikte çalışma','kolay','Birlikte çalışma','İki makinenin bir saatlik işlerini toplayarak birlikte bitirme süresini bulur.','hikâyeli',2,
 'K-IS-01 (iki kişinin birlikte çalışması) · yeni kurgu (iki baskı makinesi)',
 'Bir matbaadaki yeni baskı makinesi bir siparişi 6 saatte, eski baskı makinesi aynı siparişi 12 saatte basabiliyor.\nİki makine birlikte çalışırsa bu sipariş kaç saatte basılır?',
 s,'B','İki makinenin birlikte siparişi bitirme süresi.',
 ['Yeni makine bir saatte siparişin kaçta kaçını basar?','Eski makinenin bir saatlik işini de bul ve topla.','Bir saatte yapılan iş 1/k ise iş k saatte biter.'],[IS,BIR],
 [A('Saatlik işler','Yeni makine saatte 1/6, eski makine saatte 1/12 iş yapar.','1/6 · 1/12'),
  A('Birlikte','Birlikte çalışınca saatlik işler toplanır.','1/6 + 1/12 = 2/12 + 1/12 = 3/12 = 1/4'),
  A('Süre','Saatte işin 1/4’ü basılıyorsa sipariş 4 saatte biter.','4 saat · kontrol: 4/6 + 4/12 = 2/3 + 1/3 = 1')],
 'Birlikte çalışmada süreler değil, birim zamanda yapılan işler toplanır.',
 dict(A='3, iki makineyi de yeni makine kadar hızlı sanmak (6 ÷ 2); eski makine daha yavaş.',C='6, sürelerin farkı (12 − 6); fark bir anlam taşımaz.',
      D='9, sürelerin ortalaması; birlikte çalışınca süre her ikisinden de kısalır.',E='18, süreleri toplamak; birlikte çalışmada saatlik işler toplanır.'),
 TT(A='bilgi',C='islem',D='bilgi',E='bilgi'))
yap=4*(Fr(1,10)+Fr(1,15)); assert yap==Fr(2,3)
assert Fr(4,25)==4*Fr(1,25) and Fr(1,10)+Fr(1,15)==Fr(1,6) and 1-yap==Fr(1,3) and 4*Fr(1,10)==Fr(2,5)
s=sirali(['4/25','1/6','1/3','2/5','2/3'])
P.K('0001','Bir arşiv odasını Ece yalnız başına 10 günde, Nil 15 günde düzenleyebiliyor. İkisi birlikte 4 gün çalışıyor.\nBuna göre bu 4 günde işin kaçta kaçı yapılmıştır?',
 s,'E','4 günde yapılan iş (işin tamamına oranı).',
 ['Ece bir günde işin kaçta kaçını yapar? Nil?','Birlikte bir günde yapılan işi bul.','4 günde yapılan iş = 4 × (bir günlük iş).'],[IS,BIR],
 [A('Günlük işler','Ece günde 1/10, Nil günde 1/15 iş yapar.','1/10 · 1/15'),
  A('Birlikte bir gün','Paydaları 30’da eşitle.','1/10 + 1/15 = 3/30 + 2/30 = 5/30 = 1/6'),
  A('4 gün','Bir günlük işi 4 ile çarp.','4 × 1/6 = 4/6 = 2/3')],
 'Belirli sürede yapılan iş = birlikte bir günlük iş × gün sayısı.',
 dict(A='4/25, süreleri toplayıp 25 günde bitecek sanmak; günlük işler toplanır.',B='1/6, birlikte bir günde yapılan iş; 4 gün çalışılmış.',
      C='1/3, kalan iş; soru yapılan işi soruyor.',D='2/5, yalnız Ece’nin 4 günlük işi; Nil’in işi eklenmemiş.'),
 TT(A='bilgi',B='dikkat',C='dikkat',D='dikkat'))

# ===================== 0002 havuz KOLAY
h=Fr(1,4)-Fr(1,6); assert h==Fr(1,12) and iki_yol([],h)==12
assert 6-4==2 and 1/(Fr(1,4)+Fr(1,6))==Fr(12,5) and Fr(4+6,2)==5 and 4+6==10
s=sirali(['2','2,4','5','10','12'])
P.R('0002','is-havuz','Havuz ve musluk','kolay','Havuz ve musluk','Dolduran ve boşaltan muslukların saatlik etkilerini işaretleriyle toplayarak dolma süresini bulur.','hikâyeli',2,
 'K-IS-03 (doldurma ve boşaltma birlikte) · yeni kurgu (su deposu)',
 'Boş bir su deposunu A musluğu 4 saatte doldurabiliyor. Deponun altındaki B musluğu ise dolu depoyu 6 saatte boşaltabiliyor.\nDepo boşken iki musluk aynı anda açılırsa depo kaç saatte dolar?',
 s,'E','İki musluk birlikte açıkken boş deponun dolma süresi.',
 ['A musluğu bir saatte deponun kaçta kaçını doldurur?','B musluğu bir saatte deponun kaçta kaçını boşaltır? Bu miktar eklenir mi, çıkarılır mı?','Bir saatte net dolan kısım 1/k ise depo k saatte dolar.'],[MUS],
 [A('Saatlik etkiler','A saatte deponun 1/4’ünü doldurur, B saatte 1/6’sını boşaltır.','+1/4 · −1/6'),
  A('Net dolum','Boşaltan musluğun etkisi çıkarılır.','1/4 − 1/6 = 3/12 − 2/12 = 1/12'),
  A('Süre','Saatte deponun 1/12’si doluyorsa depo 12 saatte dolar.','12 saat')],
 'Boşaltan muslukta işaret eksidir; net hız = dolduranlar − boşaltanlar.',
 dict(A='2, sürelerin farkı (6 − 4); saatlik işler çıkarılmalı, süreler değil.',B='2,4, B musluğunu da doldurucu sayıp saatlik işleri toplamak.',
      C='5, sürelerin ortalaması; süre ortalaması bir anlam taşımaz.',D='10, süreleri toplamak; saatlik etkiler işaretleriyle birleştirilir.'),
 TT(A='islem',B='bilgi',C='bilgi',D='bilgi'))
h=Fr(1,3)-Fr(1,12); assert h==Fr(1,4) and iki_yol([],h,Fr(1,2))==2
assert Fr(1,2)/(Fr(1,3)+Fr(1,12))==Fr(6,5) and Fr(1,2)/Fr(1,3)==Fr(3,2) and 1/h==4 and 12-3==9
s=sirali(['1,2','1,5','2','4','9'])
P.K('0002','Bir yüzme havuzunun dolum musluğu boş havuzu 3 saatte doldurabiliyor, tahliye musluğu ise dolu havuzu 12 saatte boşaltabiliyor. Havuzun yarısı doluyken iki musluk birlikte açılıyor.\nBuna göre havuz kaç saat sonra tamamen dolar?',
 s,'C','Yarısı dolu havuzun iki musluk açıkken tamamen dolma süresi.',
 ['Dolum musluğu saatte havuzun kaçta kaçını doldurur, tahliye musluğu kaçta kaçını boşaltır?','Net saatlik dolumu bul.','Havuzun tamamı değil, yalnız boş olan yarısı dolacak.'],[MUS],
 [A('Net dolum','Dolum saatte 1/3 ekler, tahliye 1/12 çıkarır.','1/3 − 1/12 = 4/12 − 1/12 = 3/12 = 1/4'),
  A('Dolacak kısım','Havuzun yarısı zaten dolu.','dolacak = 1 − 1/2 = 1/2'),
  A('Süre','Saatte 1/4 dolarsa 1/2 için gereken süre.','1/2 ÷ 1/4 = 2 saat')],
 'Havuz kısmen doluysa yalnız kalan boş kısmı net hıza böl.',
 dict(A='1,2, tahliye musluğunu da doldurucu sayıp hızları toplamak.',B='1,5, tahliye musluğunu unutup yalnız dolum musluğunu hesaba katmak.',
      D='4, boş havuzun tamamının dolma süresi; havuz yarısı dolu.',E='9, sürelerin farkı (12 − 3); saatlik işlerle çalışılmalı.'),
 TT(A='bilgi',B='dikkat',D='dikkat',E='islem'))

# ===================== 0003 ayrılma ORTA
a,z=Fr(1,10),Fr(1,15); top=iki_yol([(2,a+z)],z); assert top==12
assert 1/(a+z)==6 and top-2==10 and 2+(1-2*a)/z==14 and 1/z==15
s=sirali(['6','10','12','14','15'])
P.R('0003','is-ayrilma','Ayrılma ve sonradan katılma','orta','Ayrılma ve katılma','İşi evrelere ayırarak birlikte yapılan kısmı ve kalan işi bulur; bir kişinin toplam çalışma süresini hesaplar.','hikâyeli',3,
 'K-IS-02 (biri işi bırakıyor, kalanı diğeri bitiriyor) · yeni kurgu, istenen: bir kişinin toplam çalışma günü',
 'Bir işi Ayşe yalnız başına 10 günde, Zeynep yalnız başına 15 günde bitirebiliyor. İkisi işe birlikte başlıyor; 2 gün sonra Ayşe işi bırakıyor ve kalan işi Zeynep yalnız başına bitiriyor.\nBuna göre Zeynep bu işte toplam kaç gün çalışmıştır?',
 s,'C','Zeynep’in işin başından sonuna kadar çalıştığı gün sayısı.',
 ['İkisi birlikte bir günde işin kaçta kaçını yapar?','2 günde ne kadar iş biter, ne kadar kalır?','Kalan işi Zeynep kaç günde yapar? İlk 2 günü de unutma.'],[IS,BIR],
 [A('Birlikte bir gün','Ayşe günde 1/10, Zeynep 1/15 iş yapar.','1/10 + 1/15 = 3/30 + 2/30 = 1/6'),
  A('İlk 2 gün','Birlikte 2 gün çalışılır.','2 × 1/6 = 1/3 · kalan = 1 − 1/3 = 2/3'),
  A('Kalan iş','Zeynep günde 1/15 iş yapar.','2/3 ÷ 1/15 = 2/3 × 15 = 10 gün'),
  A('Zeynep’in günleri','Zeynep ilk 2 günde de çalıştı.','2 + 10 = 12 gün')],
 'Evreli işlerde her evrenin işini ayrı hesapla; bir kişinin süresi sorulduysa o kişinin bütün evrelerini topla.',
 dict(A='6, ikisinin birlikte işi bitirme süresi; Ayşe 2 gün sonra ayrıldı.',B='10, yalnız Ayşe ayrıldıktan sonraki günler; ilk 2 gün de Zeynep çalıştı.',
      D='14, ilk 2 günde yalnız Ayşe’nin işini (2/10) sayıp Zeynep’in o günlerdeki işini unutmak.',E='15, Zeynep’in işin tamamını yalnız yapma süresi; ilk 2 günde Ayşe de çalıştı.'),
 TT(A='dikkat',B='dikkat',D='islem',E='dikkat'))
k,o=Fr(1,20),Fr(1,30); top=iki_yol([(5,k)],k+o); assert top==14
assert (top-5)==9 and 5+(1-5*o)/(k+o)==15 and 5+1/(k+o)==17 and 1/k==20
s=sirali(['9','14','15','17','20'])
P.K('0003','Bir yazılım projesini Kaan yalnız başına 20 günde, Ozan yalnız başına 30 günde tamamlayabiliyor. Kaan projeye yalnız başlıyor; 5 gün sonra Ozan da katılıyor ve projeyi birlikte bitiriyorlar.\nBuna göre proje, başladıktan kaç gün sonra biter?',
 s,'B','Projenin başlangıcından bitişine kadar geçen gün.',
 ['Kaan 5 günde projenin kaçta kaçını yapar?','Kalan iş ne kadar? İkisi birlikte bir günde kaçta kaçını yapar?','Birlikte geçen günlere ilk 5 günü ekle.'],[IS,BIR],
 [A('İlk 5 gün','Kaan günde 1/20 iş yapar.','5 × 1/20 = 1/4 · kalan = 3/4'),
  A('Birlikte bir gün','Paydaları 60’ta eşitle.','1/20 + 1/30 = 3/60 + 2/60 = 1/12'),
  A('Kalan iş','Birlikte günde 1/12 iş yapılır.','3/4 ÷ 1/12 = 3/4 × 12 = 9 gün'),
  A('Toplam süre','İlk 5 gün ve birlikte geçen 9 gün.','5 + 9 = 14 gün')],
 'Sonradan katılmada önce yalnız yapılan işi düş; kalan iş birlikte hıza bölünür, sonra günler toplanır.',
 dict(A='9, yalnız birlikte çalışılan günler; Kaan’ın yalnız çalıştığı 5 gün eklenmemiş.',C='15, ilk 5 günü Ozan’ın hızıyla (5/30) hesaplamak; o günlerde Kaan çalıştı.',
      D='17, işin tamamını birlikte 12 günde yapacaklarını sanıp 5 gün eklemek; işin 1/4’ü zaten bitmişti.',E='20, Kaan’ın projeyi yalnız bitirme süresi; Ozan’ın katkısı unutulmuş.'),
 TT(A='dikkat',C='islem',D='dikkat',E='dikkat'))

# ===================== 0004 verim ORTA
gun=[g for g in range(1,100) if 4*9*g==5*6*12]; assert gun==[10]
assert Fr(12*5,4)==15 and Fr(12*6,9)==8 and Fr(12*4*9,5*6)==Fr('14.4')
s=sirali(['8','10','12','14,4','15'])
P.R('0004','is-verim','İşçi sayısı, süre ve verim','orta','İşçi sayısı, süre ve verim','Toplam işi işçi × gün × saat olarak hesaplar; işçi sayısı ve günlük saat değişince yeni süreyi bulur.','hikâyeli',3,
 'K-IS-04 (işçi sayısı ve günlük saat birlikte değişiyor) · yeni kurgu, sade sayılar',
 'Eşit verimle çalışan 5 işçi, günde 6 saat çalışarak bir işi 12 günde bitirebiliyor.\nAynı verimle çalışan 4 işçi günde 9 saat çalışırsa aynı işi kaç günde bitirir?',
 s,'B','4 işçinin günde 9 saat çalışarak işi bitirme süresi.',
 ['İş toplam kaç “işçi-saat” sürüyor? (işçi × saat × gün)','Yeni durumda bir günde kaç işçi-saat çalışılır?','Toplam işi yeni günlük çalışmaya böl.'],[ISGUN,B('Ters orantı','iş aynıyken çalışan sayısı ya da günlük saat artarsa gün azalır; azalırsa gün artar')],
 [A('Toplam iş','İlk durumdaki işçi-saat.','5 × 6 × 12 = 360 işçi-saat'),
  A('Yeni günlük çalışma','4 işçi günde 9 saat.','4 × 9 = 36 işçi-saat/gün'),
  A('Gün sayısı','Aynı iş, yeni günlük çalışmayla.','360 ÷ 36 = 10 gün')],
 'İş miktarı aynıysa işçi × saat × gün çarpımı da aynıdır.',
 dict(A='8, yalnız günlük saat değişimini hesaba katmak (12 × 6 ÷ 9); işçi sayısı da azaldı.',C='12, işçi azalıp saat arttığı için sürenin değişmeyeceğini sanmak; çarpımlar karşılaştırılmalı.',
      D='14,4, işçi ve saati doğru orantılı kurmak (12 × 4/5 × 9/6); bu değişkenler süreyle ters orantılıdır.',E='15, yalnız işçi sayısı değişimini hesaba katmak (12 × 5 ÷ 4); günlük saat de arttı.'),
 TT(A='dikkat',C='bilgi',D='bilgi',E='dikkat'))
birim=Fr(2400,3*10*4); uret=birim*5*8*6; assert birim==20 and uret==4800
assert 2400*Fr(6,4)==3600 and 2400*Fr(5,3)==4000 and 2400*Fr(5,3)*Fr(6,4)==6000 and 6000*Fr(10,8)==7500
s=sirali(['3600','4000','4800','6000','7500'])
P.K('0004','Bir fabrikada aynı tip 3 makine günde 10 saat çalışarak 4 günde 2400 parça üretiyor.\nAynı tip 5 makine günde 8 saat çalışırsa 6 günde kaç parça üretir?',
 s,'C','5 makinenin günde 8 saat çalışarak 6 günde ürettiği parça sayısı.',
 ['Bir makine bir saatte kaç parça üretir?','Yeni durumda toplam kaç makine-saat çalışılır?','Makine-saat ile saatlik üretimi çarp.'],[ISGUN,B('Doğru orantı','süre aynı kalıp çalışan sayısı ya da saat artarsa üretilen iş de aynı oranda artar')],
 [A('Toplam makine-saat','İlk durum.','3 × 10 × 4 = 120 makine-saat'),
  A('Saatlik üretim','Bir makinenin bir saatte ürettiği parça.','2400 ÷ 120 = 20 parça'),
  A('Yeni çalışma','5 makine, günde 8 saat, 6 gün.','5 × 8 × 6 = 240 makine-saat'),
  A('Üretim','Makine-saat × saatlik üretim.','240 × 20 = 4800 parça')],
 'Üretim sorularında önce birim üretimi (bir makine, bir saat) bul; sonra yeni duruma ölçekle.',
 dict(A='3600, yalnız gün sayısının değişimini hesaba katmak (2400 × 6/4).',B='4000, yalnız makine sayısının değişimini hesaba katmak (2400 × 5/3).',
      D='6000, günlük saatin 10’dan 8’e düştüğünü unutmak.',E='7500, saat azalınca üretimin arttığını sanmak (6000 × 10/8); saat ile üretim doğru orantılıdır.'),
 TT(A='dikkat',B='dikkat',D='dikkat',E='bilgi'))

# ===================== 0005 havuz ORTA
A_,C_=Fr(1,6),Fr(1,12); top=iki_yol([(3,A_)],A_-C_); assert top==9
assert top-3==6 and 1/(A_-C_)==12 and 3+(1-3*A_)/(A_+C_)==5 and 3+1/(A_-C_)==15
s=sirali(['5','6','9','12','15'])
P.R('0005','is-havuz','Havuz ve musluk','orta','Havuz ve musluk','Evrelere göre açık olan muslukları belirler; ilk evrede dolan kısmı düşüp kalanı net hızla tamamlar.','hikâyeli',3,
 'K-IS-03 (musluklar farklı anlarda açılıyor) · yeni kurgu (gider sonradan açılıyor), istenen: toplam süre',
 'Bir havuza su dolduran A musluğu boş havuzu 6 saatte doldurmaktadır. Havuzdaki gider ise dolu havuzu 12 saatte boşaltmaktadır. Havuz boşken yalnız A musluğu açılıyor; 3 saat sonra gider de açılıyor ve havuz dolana kadar ikisi de açık kalıyor.\nBuna göre havuz, A musluğu açıldıktan kaç saat sonra dolar?',
 s,'C','A musluğunun açılışından havuzun dolmasına kadar geçen süre.',
 ['İlk 3 saatte havuzun kaçta kaçı dolar?','Gider açıldıktan sonra havuz saatte net kaçta kaç dolar?','Kalan kısmı net hıza böl; ilk 3 saati de ekle.'],[MUS],
 [A('İlk 3 saat','Yalnız A açık; saatte 1/6 dolar.','3 × 1/6 = 1/2 · kalan = 1/2'),
  A('Net dolum','Gider açılınca saatlik dolumdan çıkar.','1/6 − 1/12 = 2/12 − 1/12 = 1/12'),
  A('Kalan süre','Kalan yarıyı net hızla doldur.','1/2 ÷ 1/12 = 6 saat'),
  A('Toplam','A’nın açılışından itibaren.','3 + 6 = 9 saat')],
 'Musluklar farklı anlarda açılıyorsa zaman çizelgesini evrelere böl; her evrede yalnız açık muslukları hesaba kat.',
 dict(A='5, gideri doldurucu sanıp hızları toplamak (1/2 ÷ 1/4 = 2 saat).',B='6, yalnız gider açıldıktan sonraki süre; ilk 3 saat eklenmemiş.',
      D='12, havuz boşken iki musluğun birlikte açılması durumundaki süre; ilk 3 saatte yalnız A açıktı.',E='15, kalan yarıyı değil havuzun tamamını net hızla doldurmak (3 + 12).'),
 TT(A='bilgi',B='dikkat',D='dikkat',E='islem'))
K_,L_,M_=Fr(1,8),Fr(1,12),Fr(1,6); top=iki_yol([(4,K_+L_-M_)],K_+L_); assert top-4==4 and K_+L_-M_==Fr(1,24)
assert Fr(1,6)/(K_+L_)==Fr(4,5) and 1/(K_+L_)==Fr(24,5) and top==8 and 1/(K_+L_-M_)==24
s=sirali(['0,8','4','4,8','8','24'])
P.K('0005','Bir sulama deposuna su dolduran K ve L muslukları boş depoyu sırasıyla 8 ve 12 saatte doldurabiliyor; M musluğu ise dolu depoyu 6 saatte boşaltabiliyor. Depo boşken üç musluk birlikte açılıyor ve 4 saat sonra M musluğu kapatılıyor.\nBuna göre depo, M musluğu kapatıldıktan kaç saat sonra dolar?',
 s,'B','M kapatıldıktan sonra deponun dolma süresi.',
 ['Üç musluk açıkken depo saatte net kaçta kaç dolar?','M kapanana kadar deponun ne kadarı doldu, ne kadarı kaldı?','M kapanınca K ve L birlikte saatte kaçta kaç doldurur?'],[MUS],
 [A('Üç musluk açık','Dolduranlar eklenir, M çıkarılır.','1/8 + 1/12 − 1/6 = 3/24 + 2/24 − 4/24 = 1/24'),
  A('İlk 4 saat','Net hızla 4 saat.','4 × 1/24 = 1/6 · kalan = 5/6'),
  A('M kapandıktan sonra','Yalnız K ve L açık.','1/8 + 1/12 = 5/24'),
  A('Kalan süre','Kalanı yeni hıza böl.','5/6 ÷ 5/24 = 5/6 × 24/5 = 4 saat')],
 'Bir musluk kapandığında net hız değişir; her evrenin hızını ayrı kur.',
 dict(A='0,8, dolan 1/6’yı kalan sanıp 1/6 ÷ 5/24 hesaplamak.',C='4,8, deponun tamamını K ve L ile doldurmak; ilk 4 saatte 1/6’sı dolmuştu.',
      D='8, depoyu ilk açılıştan itibaren ölçmek (4 + 4); soru M kapandıktan sonrasını soruyor.',E='24, M’nin kapatıldığını unutup üç muslukla dolma süresini almak.'),
 TT(A='islem',C='dikkat',D='dikkat',E='dikkat'))

# ===================== 0006 birlikte (ikişerli) ORTA
sol=[(a,b,c) for a in range(2,121) for b in range(2,121) for c in range(2,121)
     if Fr(1,a)+Fr(1,b)==Fr(1,12) and Fr(1,b)+Fr(1,c)==Fr(1,15) and Fr(1,a)+Fr(1,c)==Fr(1,20)]
assert sol==[(30,20,60)]
top=(Fr(1,12)+Fr(1,15)+Fr(1,20))/2; assert top==Fr(1,10)
assert 1/(2*top-Fr(1,15))==Fr(15,2)
s=sirali(['7,5','10','20','30','60'])
P.R('0006','is-birlikte','Birlikte çalışma','orta','Birlikte çalışma','İkişerli birlikte çalışma sürelerinden üç kişinin toplam hızını, oradan bir kişinin yalnız çalışma süresini bulur.','hikâyeli',4,
 'K-IS-01 (ikişerli birlikte süreler) · yeni kurgu (duvar ören üç usta), istenen: bir kişinin yalnız süresi',
 'Arda ile Barış bir bahçe duvarını 12 günde, Barış ile Can 15 günde, Arda ile Can ise 20 günde örebiliyor. Üçünün de çalışma hızı sabittir.\nBuna göre Arda bu duvarı yalnız başına kaç günde örer?',
 s,'D','Arda’nın duvarı yalnız başına örme süresi.',
 ['Arda, Barış ve Can’ın bir günlük işlerine a, b, c de; üç eşitlik yaz.','Üç eşitliği taraf tarafa topla: her kişi kaç kez sayıldı?','a + b + c’yi bulunca Barış ile Can’ın günlük işini çıkar.'],[IS,BIR],
 [A('Eşitlikler','Bir günlük işler: Arda a, Barış b, Can c.','a + b = 1/12 · b + c = 1/15 · a + c = 1/20'),
  A('Topla','Her kişi iki kez sayılır.','2(a + b + c) = 5/60 + 4/60 + 3/60 = 12/60 = 1/5'),
  A('Üçü birlikte','İkiye böl.','a + b + c = 1/10'),
  A('Arda','Barış ile Can’ın günlük işini çıkar.','a = 1/10 − 1/15 = 3/30 − 2/30 = 1/30 ⇒ 30 gün')],
 'İkişerli süreler verildiğinde üç eşitliği topla; her kişi iki kez sayıldığı için toplamı ikiye böl.',
 dict(A='7,5, üç eşitliğin toplamını (1/5) ikiye bölmeyi unutup a = 1/5 − 1/15 almak.',B='10, üçünün birlikte örme süresi; soru Arda’nın yalnız süresini soruyor.',
      C='20, Barış’ın yalnız süresi (b = 1/10 − 1/20); Arda için Barış ile Can’ın işi çıkarılmalı.',E='60, Can’ın yalnız süresi (c = 1/10 − 1/12).'),
 TT(A='islem',B='dikkat',C='dikkat',E='dikkat'))
sol=[(a,b,c) for a in range(2,121) for b in range(2,121) for c in range(2,121)
     if Fr(1,a)+Fr(1,b)==Fr(1,10) and Fr(1,b)+Fr(1,c)==Fr(1,12) and Fr(1,a)+Fr(1,c)==Fr(1,15)]
top=(Fr(1,10)+Fr(1,12)+Fr(1,15))/2; assert top==Fr(1,8)
e=top-Fr(1,10); assert e==Fr(1,40) and top-Fr(1,12)==Fr(1,24) and top-Fr(1,15)==Fr(7,120) and sol==[]  # Doruk'un süresi tam sayı değil; soru Efe'yi soruyor
assert Fr(1,10)-Fr(1,12)==Fr(1,60)
s=sirali(['8','15','24','40','60'])
P.K('0006','Cem ile Doruk bir bahçeyi 10 saatte, Doruk ile Efe 12 saatte, Cem ile Efe ise 15 saatte çapalayabiliyor. Üçünün de çalışma hızı sabittir.\nBuna göre Efe bu bahçeyi yalnız başına kaç saatte çapalar?',
 s,'D','Efe’nin bahçeyi yalnız başına çapalama süresi.',
 ['Her kişinin bir saatlik işine bir harf ver ve üç eşitlik yaz.','Üç eşitliği topla; her kişi kaç kez sayıldı?','Üçünün birlikte bir saatlik işinden Cem ile Doruk’unkini çıkar.'],[IS,BIR],
 [A('Eşitlikler','Saatlik işler: Cem c, Doruk d, Efe e.','c + d = 1/10 · d + e = 1/12 · c + e = 1/15'),
  A('Topla','Her kişi iki kez sayılır; paydaları 60’ta eşitle.','2(c + d + e) = 6/60 + 5/60 + 4/60 = 15/60 = 1/4'),
  A('Üçü birlikte','İkiye böl.','c + d + e = 1/8'),
  A('Efe','Cem ile Doruk’un işini çıkar.','e = 1/8 − 1/10 = 5/40 − 4/40 = 1/40 ⇒ 40 saat')],
 'Bir kişinin süresi için üçünün toplam hızından diğer ikisinin birlikte hızını çıkar.',
 dict(A='8, üçünün birlikte çapalama süresi; soru Efe’nin yalnız süresini soruyor.',B='15, Cem ile Efe’nin birlikte süresi; Efe yalnız daha uzun sürede bitirir.',
      C='24, Cem’in yalnız süresi (1/8 − 1/12 = 1/24); Efe için Cem ile Doruk’un işi çıkarılmalı.',E='60, iki ikilinin saatlik işlerinin farkını (1/10 − 1/12) Efe’nin işi sanmak.'),
 TT(A='dikkat',B='dikkat',C='dikkat',E='islem'))

# ===================== 0007 ayrılma ZOR
u,k_,c=Fr(1,12),Fr(1,18),Fr(1,36); top=iki_yol([(2,u+k_+c),(3,k_+c)],c); assert top==20
assert 1/(u+k_+c)==6 and 1/c==36 and iki_yol([(2,k_+c),(3,k_+c)],c)==26 and iki_yol([(2,u+k_+c),(3,k_)],c)==23
s=sirali(['6','15','20','23','26'])
P.R('0007','is-ayrilma','Ayrılma ve sonradan katılma','zor','Ayrılma ve katılma','Üç evreli bir işte her evrede çalışanların işini ayrı hesaplayıp kalan işi son çalışanın hızıyla tamamlar.','hikâyeli',4,
 'K-IS-02 (ekipten sırayla ayrılma) · üç kişi ve üç evre, istenen: toplam süre',
 'Bir atölyede bir dolabı usta yalnız başına 12 günde, kalfa 18 günde, çırak 36 günde yapabiliyor. Üçü işe birlikte başlıyor. 2 gün sonra usta ayrılıyor; kalfa ile çırak 3 gün daha birlikte çalıştıktan sonra kalfa da ayrılıyor ve kalan işi çırak bitiriyor.\nBuna göre dolap, işe başlandıktan kaç gün sonra biter?',
 s,'C','İşin başından dolabın bitmesine kadar geçen gün.',
 ['Bir günlük işleri 36’lık paydayla yaz: usta, kalfa, çırak günde kaç parça yapar?','İlk 2 gün ve sonraki 3 günde yapılan işleri ayrı ayrı topla.','Kalan işi çırağın günlük işine böl; bütün günleri topla.'],[IS,BIR],
 [A('Günlük işler','İşi 36 eş parça düşün.','usta 3/36 · kalfa 2/36 · çırak 1/36'),
  A('İlk 2 gün','Üçü birlikte.','2 × (3 + 2 + 1)/36 = 12/36'),
  A('Sonraki 3 gün','Kalfa ve çırak.','3 × (2 + 1)/36 = 9/36 · toplam 21/36'),
  A('Çırağın payı','Kalan iş çırağın hızıyla.','kalan 15/36 ÷ 1/36 = 15 gün'),
  A('Toplam','Üç evrenin günleri.','2 + 3 + 15 = 20 gün')],
 'Evreli işlerde her evrede kimin çalıştığını yaz; ortak payda (36 gibi) işi parça sayısına çevirir ve hesabı kolaylaştırır.',
 dict(A='6, üçünün birlikte dolabı bitirme süresi; usta 2 gün sonra ayrıldı.',B='15, yalnız çırağın son evrede çalıştığı gün; önceki 5 gün eklenmemiş.',
      D='23, ikinci evrede çırağın da çalıştığını unutmak; 3 gün boyunca kalfa ile çırak birlikte.',E='26, ilk 2 günde ustanın da çalıştığını unutmak.'),
 TT(A='dikkat',B='dikkat',D='islem',E='islem'))
g,n,e=Fr(1,15),Fr(1,10),Fr(1,30); top=iki_yol([(2,g+e),(2,g+n+e)],n+e); assert top==7
assert 1/(g+n+e)==5 and iki_yol([(2,g),(2,g+n+e)],n+e)==Fr(15,2) and iki_yol([(2,g+e),(2,g+n+e)],n)==8 and 1/n==10
s=sirali(['5','7','7,5','8','10'])
P.K('0007','Bir duvar boyama işini Gül yalnız başına 15 günde, Nur 10 günde, Ece 30 günde bitirebiliyor. Gül ile Ece işe birlikte başlıyor; 2 gün sonra Nur da onlara katılıyor. Üçü 2 gün birlikte çalıştıktan sonra Gül ayrılıyor ve kalan işi Nur ile Ece bitiriyor.\nBuna göre iş, başladıktan kaç gün sonra biter?',
 s,'B','İşin başından bitişine kadar geçen gün.',
 ['İşi 30 eş parça düşün: Gül, Nur ve Ece günde kaç parça boyar?','İlk 2 gün kimler çalıştı? Sonraki 2 gün kimler?','Kalanı Nur ile Ece’nin günlük işine böl; günleri topla.'],[IS,BIR],
 [A('Günlük işler','30’luk paydayla yaz.','Gül 2/30 · Nur 3/30 · Ece 1/30'),
  A('İlk 2 gün','Gül ve Ece.','2 × (2 + 1)/30 = 6/30'),
  A('Sonraki 2 gün','Üçü birlikte.','2 × (2 + 3 + 1)/30 = 12/30 · toplam 18/30'),
  A('Son evre','Kalanı Nur ve Ece bitirir.','kalan 12/30 ÷ (3 + 1)/30 = 3 gün'),
  A('Toplam','Üç evrenin günleri.','2 + 2 + 3 = 7 gün')],
 'Katılma ve ayrılma olan işlerde her evrenin ekibini tek tek yaz; birini unutmak en sık hatadır.',
 dict(A='5, üçünün en baştan birlikte çalışması durumundaki süre.',C='7,5, ilk 2 günde Ece’nin de çalıştığını unutmak.',
      D='8, son evrede Ece’yi unutup kalanı yalnız Nur’a yaptırmak.',E='10, Nur’un işi yalnız bitirme süresi; diğerlerinin katkısı unutulmuş.'),
 TT(A='dikkat',C='dikkat',D='dikkat',E='bilgi'))

# ===================== 0008 verim ZOR
def gecikme(isci,plan,once,ayrilan,yok):
    is_=isci*plan; w=0; gun=0
    while w<is_:
        gun+=1; w+=isci-(ayrilan if once<gun<=once+yok else 0)
    assert w==is_; return gun-plan, gun
gc,gun=gecikme(12,15,5,4,6); assert (gc,gun)==(2,17) and 12*15>5*12+6*8
assert Fr(4*6,8)==3 and gun==17 and 5+Fr(12*15-5*12,8)-15==5
s=sirali(['2','3','5','6','17'])
P.R('0008','is-verim','İşçi sayısı, süre ve verim','zor','İşçi sayısı, süre ve verim','İşçi-gün hesabıyla ara verme nedeniyle kaybedilen işi bulur ve tam ekiple telafi süresini hesaplar.','hikâyeli',4,
 'K-IS-04 (işçi sayısı değişince süre) · yeni kurgu (işçiler ayrılıp geri dönüyor), istenen: gecikme',
 'Eşit verimle çalışan 12 işçi, bir binanın tadilatını 15 günde bitirmek üzere işe başlıyor. 5. günün sonunda işçilerden 4’ü ayrılıyor; bu işçiler 6 gün sonra geri dönüyor ve tadilat 12 işçiyle tamamlanıyor.\nBuna göre tadilat, planlanandan kaç gün geç biter?',
 s,'A','Tadilatın planlanan süreden kaç gün fazla sürdüğü.',
 ['Tadilatın tamamı kaç işçi-günlük iştir?','İlk 5 günde ve sonraki 6 günde kaç işçi-günlük iş yapıldı?','Kalan işi 12 işçi kaç günde bitirir? Toplam süreyi 15 ile karşılaştır.'],[ISGUN],
 [A('Toplam iş','12 işçi 15 gün.','12 × 15 = 180 işçi-gün'),
  A('İlk 11 gün','5 gün 12 işçi, sonra 6 gün 8 işçi.','5 × 12 + 6 × 8 = 60 + 48 = 108'),
  A('Kalan iş','12 işçi geri döndü.','180 − 108 = 72 · 72 ÷ 12 = 6 gün'),
  A('Gecikme','Toplam süreyi plana göre karşılaştır.','5 + 6 + 6 = 17 gün · 17 − 15 = 2 gün')],
 'Gecikme = kaybedilen işçi-gün ÷ işi bitiren ekibin işçi sayısı.',
 dict(B='3, kaybedilen işi (4 × 6 = 24) ayrılıktan sonra kalan 8 işçiye bölmek; işi 12 işçi telafi ediyor.',C='5, ayrılan işçilerin geri döndüğünü unutup kalanı 8 işçiyle bitirmek.',
      D='6, işçilerin ayrı kaldığı gün sayısı; o sürede iş durmadı, 8 işçi çalıştı.',E='17, tadilatın toplam süresi; soru gecikmeyi soruyor.'),
 TT(B='islem',C='dikkat',D='dikkat',E='dikkat'),
 kisa='Kaybedilen iş 4 işçi × 6 gün = 24 işçi-gün; 12 işçi bunu 24 ÷ 12 = 2 günde telafi eder.')
gc,gun=gecikme(6,12,3,2,9); assert (gc,gun)==(3,15) and 6*12>3*6+9*4
assert Fr(2*9,4)==Fr(9,2)
s=sirali(['3','4,5','9','12','15'])
P.K('0008','Eşit verimle çalışan 6 kişilik bir ekip, bir yolun asfaltını 12 günde bitirmek üzere çalışmaya başlıyor. 3. günün sonunda ekipten 2 kişi başka bir işe gidiyor ve 9 gün sonra geri dönüyor; iş tam ekiple tamamlanıyor.\nBuna göre iş, planlanandan kaç gün geç tamamlanır?',
 s,'A','İşin planlanan süreden kaç gün fazla sürdüğü.',
 ['İşin tamamı kaç kişi-günlük iştir?','2 kişi yokken geçen 9 günde kaç kişi-günlük iş yapılır?','Kalan işi 6 kişi kaç günde bitirir? Toplamı 12 ile karşılaştır.'],[ISGUN],
 [A('Toplam iş','6 kişi 12 gün.','6 × 12 = 72 kişi-gün'),
  A('İlk 12 gün','3 gün 6 kişi, sonra 9 gün 4 kişi.','3 × 6 + 9 × 4 = 18 + 36 = 54'),
  A('Kalan iş','Ekip tamamlandı.','72 − 54 = 18 · 18 ÷ 6 = 3 gün'),
  A('Gecikme','Toplam süre plana göre.','3 + 9 + 3 = 15 gün · 15 − 12 = 3 gün')],
 'Bir süre eksik çalışılan işlerde kaybı kişi-gün olarak bul; telafiyi işi bitiren ekip yapar.',
 dict(B='4,5, kaybı (2 × 9 = 18) kalan 4 kişiye bölmek; telafiyi 6 kişilik ekip yapıyor.',C='9, iki kişinin ayrı kaldığı gün sayısı; o sürede 4 kişi çalıştı.',
      D='12, planlanan süre; soru gecikmeyi soruyor.',E='15, işin toplam süresi; gecikme bundan planlanan süre çıkarılarak bulunur.'),
 TT(B='islem',C='dikkat',D='dikkat',E='dikkat'),
 kisa='Kaybedilen iş 2 kişi × 9 gün = 18 kişi-gün; 6 kişi bunu 18 ÷ 6 = 3 günde telafi eder.')

P.yaz(os.path.join(H,'isciprob-1.json'),os.path.join(H,'isciprob-1-kardes.json'))
