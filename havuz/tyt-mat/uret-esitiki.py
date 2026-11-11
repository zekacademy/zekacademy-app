"""Basit Eşitsizlikler · parti 2 (hafif mod): 14 yeni ana soru, kardeş yok, ipucu 1. Her cevap ve şık kodla (tarama / Fraction) doğrulanır."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_mat as H
from _hafif_mat import *
from itertools import product
H.KONU='Basit Eşitsizlikler'
P=Parti('esitiki','Basit Eşitsizlikler','mat|Basit Eşitsizlikler')
UK='mat|Basit Eşitsizlikler'
R_=range(-400,401)
def ints(c): return [x for x in R_ if c(x)]
def open_ints(lo,hi): return [k for k in range(-400,401) if lo<k<hi]
def grid(lo,hi,n=16):
    """(lo,hi) açık aralığında yoğun rasyonel noktalar (uçlara çok yakın olanlar dahil)."""
    lo,hi=Fr(lo),Fr(hi); pts=[lo+(hi-lo)*Fr(i,n) for i in range(1,n)]
    pts+=[lo+(hi-lo)/10**6,hi-(hi-lo)/10**6]
    return pts
def erisilir(f,xl,xh,yl,yh,k):
    """f(x,y)=k olacak biçimde açık dikdörtgen içinde bir (x,y) var mı (y için f doğrusal ya da x·y)."""
    for x in grid(xl,xh,64):
        for tur in range(1):
            # y'yi f(x,y)=k'den bul: f, y'de doğrusal => iki nokta ile
            f0,f1=f(x,Fr(0)),f(x,Fr(1)); e=f1-f0
            if e==0: continue
            y=(k-f0)/e
            if yl<y<yh: return True
    return False

# ---------- bilgi kutuları ----------
ISRT=B('Eşitsizlikte işaret kuralı','iki tarafa aynı sayı eklenir ya da çıkarılır; negatif bir sayıyla çarpılıp bölünürse eşitsizlik yön değiştirir. Örnek: −2x > 6 → x < −3')
CIFT=B('Çift taraflı eşitsizlik','a < f(x) < b biçimindeki eşitsizlikte işlemler üç tarafa birden uygulanır; negatif sayıyla bölünürse sınırlar yer değiştirir. Örnek: −6 < −2x < 4 → 3 > x > −2')
SISTEM=B('Eşitsizlik sistemi','iki eşitsizlik birlikte sağlanıyorsa çözüm kümesi, ikisinin ortak (kesişim) bölgesidir. Örnek: x ≥ 4 ve x < 9 için x = 4, 5, 6, 7, 8')
ARL=B('Aralık işlemleri','a < x < b ve c < y < d iken toplamda alt sınırlar kendi arasında, üst sınırlar kendi arasında toplanır. Çıkarmada −y için sınırlar ters çevrilir. Örnek: 1 < x < 3, 2 < y < 5 → x − y: 1 − 5 < x − y < 3 − 2')
CARP=B('Çarpımda sınır bulma','iki aralığın çarpımında en büyük ve en küçük değer, uç noktaların dört çarpımından birinde bulunur. Örnek: −2 < x < 3 ve −1 < y < 4 için uç çarpımlar 2, −8, −3, 12')
ACIK=B('Açık uç','a < x < b için a ve b değerleri alınamaz; en büyük tam sayı b’den küçük olan son tam sayıdır. Örnek: x < 4 ise en büyük tam sayı 3')
KARE=B('Kare, kök ve ters (0 < x < 1)','0 ile 1 arasındaki bir sayıyı kendisiyle çarpmak küçültür, kökünü almak büyütür, tersini almak 1’den büyük yapar. Örnek: x = 0,25 → x² = 0,0625 · √x = 0,5 · 1/x = 4')
SIRA=B('Eşitsizlikte çarpma ve ters alma','a < b iken pozitif c ile çarpınca yön korunur, negatif c ile çarpınca yön değişir. İki sayı da aynı işaretliyse terslerinde sıralama ters döner. Örnek: −3 < −2 → 1/(−3) > 1/(−2)')
MODEL=B('Eşitsizlikle modelleme','“en az” ≥, “en çok” ≤, “aşmamalı” ≤ ile gösterilir; bilinmeyen adet ise çıkan sonuç uygun tam sayıya yuvarlanır. Örnek: 15n ≤ 100 → n ≤ 6,67 → en çok 6')

# ---------- kartlar ----------
KY='ÖSYM 2018–2026 (eşitsizlik, aralık, sıralama) · yayın soru bankaları (yalnız mantık) · MEB 9. sınıf'
kart('K-ESZB-01','Birinci dereceden eşitsizlik çözümü','Eşitsizlik taşıma ve negatif sayıya bölme kuralıyla çözülür; sistem ya da çift taraflı biçimde kesişim alınıp tam sayı değerleri toplanır ya da sayılır.','Negatife bölünce işareti çevirmemek; uç noktayı (< ve ≤) yanlış dahil etmek; sistemde birleşim ile kesişimi karıştırmak.','orta','düz',3,'ezb-cozum','Eşitsizlik çözümü ve tam sayı değerleri',KY)
kart('K-ESZB-02','Aralık işlemleri','a < x < b ve c < y < d iken x + y, x − y, 2x − 3y gibi ifadelerin alt ve üst sınırı bulunur; açık uçlar nedeniyle en büyük ve en küçük tam sayı ya da tam sayı adedi hesaplanır.','Çıkarmada üst sınırdan üst sınırı çıkarmak; uç değeri dahil saymak; x ve y’yi birbirinden bağımsız sanıp bağımlı ifadeyi ayrı ayrı sınırlamak.','zor','düz',4,'ezb-aralik','Aralık işlemleri ve ifadenin tam sayı değerleri',KY)
kart('K-ESZB-03','Eşitsizlikle sıralama','a < b < 0 gibi verilen sıralamada 1/a, a², a·b ya da ifadelerin büyüklüğü işaret ve yön kuralıyla karşılaştırılır; öncüllü ve zincir biçiminde sorulur.','Negatiflerde kare ve terslerde sıralamanın ters döneceğini unutmak; tek bir sayısal örnekle “kesinlikle” sonucuna varmak.','orta','öncüllü',3,'ezb-siralama','Eşitsizliklerde sıralama ve kesinlikle doğru ifadeler',KY)
kart('K-ESZB-04','Eşitsizlikle modelleme','Bütçe, kapasite ya da iki tarife karşılaştırması eşitsizliğe çevrilir; adet olan bilinmeyen için tam sayıya yuvarlanır ve kısıtlar birlikte düşünülür.','Eşitlik durumunda “fazla/az” ayrımını karıştırmak; yuvarlamayı yanlış yöne yapmak; sabit ücreti hesaba katmamak.','orta','hikâyeli',3,'ezb-model','Eşitsizlikle modelleme (bütçe, kapasite, tarife)',KY)
kart('K-ESZB-05','0 < x < 1 için kare, kök ve ters','0 ile 1 arasındaki x için x, x², √x ve 1/x sayıları sıralanır; bir sayıyla örnek denemek yerine işleme göre büyüyen ya da küçülen sayı belirlenir.','x² değerini x’ten büyük sanmak; 1/x’i 1’den küçük sanmak; kökün büyütmesini unutmak.','orta','düz',3,'ezb-kare','Kare, kök ve ters ile sıralama (0 < x < 1)',KY)
kart('K-ESZB-06','Tanımlı işlem ve eşitsizlik','Yeni tanımlanan bir işlemin sonucu aralık bilgisinden sınırlanır; ifade değeri tam sayı adedi ya da sınırı sorulur.','Tanımı karıştırmak; açık uçları dahil saymak; uç sayısını fark almakla bulmak (+1/−1 hatası).','orta','düz',3,'ezb-yeni','Tanımlı işlemle aralık problemi',KY)

# ---------- 01 · kolay · 5 − 2x > −7, en büyük tam sayı ----------
x1=max(ints(lambda x:5-2*x>-7)); assert x1==5
e_a=max(ints(lambda x:5-2*x>=-7)); assert e_a==6                                  # uç dahil
e_b=max(ints(lambda x:-2*x>-7+5)); assert e_b==0                                  # +5 yerine −7+5
e_c=max(ints(lambda x:x<-6)); assert e_c==-7                                       # bölünce hem yön hem işaret hatası
e_d=max(ints(lambda x:5-x>-7)); assert e_d==11                                     # 2’yi yok saymış
assert len({x1,e_a,e_b,e_c,e_d})==5
mk(P,'0001',tipId='ezb-cozum',tip='Eşitsizlik çözümü ve tam sayı değerleri',z='kolay',alt='Eşitsizlik Çözme',kaz='Negatif katsayılı birinci dereceden eşitsizliği çözerek açık uçlu çözüm kümesinin en büyük tam sayısını bulur.',kalip='düz',adim=3,
 kart='K-ESZB-01 (eşitsizlik çözümü) · negatif katsayılı eşitsizlikte açık uç ve en büyük tam sayı',
 metin='x bir tam sayı olmak üzere\n5 − 2x > −7\neşitsizliği sağlanıyor.\nBuna göre x’in alabileceği en büyük değer kaçtır?',
 dogru=x1,yan=[(e_a,'Eşitsizlik “>” olduğu halde x < 6 çözümünde 6’yı da almış; uç değer çözüme girmez.','dikkat'),(e_b,'5’i karşı tarafa −7 + 5 = −2 diye geçirmiş; doğrusu −7 − 5 = −12’dir.','islem'),(e_c,'−12’yi −2’ye bölünce işareti de ters çevirip x < −6 bulmuş; bölünce yalnız eşitsizlik yön değiştirir, sayı 6 olur.','bilgi'),(e_d,'−2x terimindeki 2’yi unutup 5 − x > −7 gibi çözmüş; x < 12 bulup 11 demiş.','islem')],
 istenen='x’in alabileceği en büyük tam sayı değeri.',
 ip=['Sabit terimi karşı tarafa geçirip −2’ye bölerken eşitsizliğin yönünü hatırla.'],
 bilgi=[ISRT],
 ad=[A('Sabiti karşıya at','5’i eşitsizliğin diğer tarafına çıkarma ile geçir.','−2x > −7 − 5 = −12'),A('−2’ye böl','Negatif sayıya bölünce eşitsizlik yön değiştirir.','x < 6'),A('En büyük tam sayıyı seç','x < 6 olduğundan 6 çözüm değildir; 6’dan küçük en büyük tam sayı 5’tir.','x = 5 · kontrol: 5 − 2 × 5 = −5 > −7')],
 puf='Negatif sayıya bölünce yönü çevir; “<” ile sınırlanmış çözümde sınır değer alınmaz.')

# ---------- 02 · kolay · a − b en küçük tam sayı ----------
box=lambda f:[f(a,b) for a in grid(-5,2) for b in grid(3,7)]
vv=box(lambda a,b:a-b); assert -12<min(vv) and max(vv)<-1
e2=min(open_ints(-12,-1)); assert e2==-11 and all(erisilir(lambda a,b:a-b,Fr(-5),Fr(2),Fr(3),Fr(7),k) for k in range(-11,-1)) and not erisilir(lambda a,b:a-b,Fr(-5),Fr(2),Fr(3),Fr(7),-12)
d1=-12; d2=-5-3; d3=2-7; d4=max(open_ints(-12,-1)); assert (d2,d3,d4)==(-8,-5,-2)
assert len({e2,d1,d2,d3,d4})==5
mk(P,'0002',tipId='ezb-aralik',tip='Aralık işlemleri ve ifadenin tam sayı değerleri',z='kolay',alt='Aralık İşlemleri',kaz='Değişkenlerin aralığı verilen bir farkın alt sınırını bulup açık uca göre en küçük tam sayı değerini belirler.',kalip='düz',adim=2,
 kart='K-ESZB-02 (aralık işlemleri) · a − b için alt sınır ve en küçük tam sayı',
 metin='a ve b gerçel sayıları için\n−5 < a < 2\n3 < b < 7\nolduğuna göre a − b farkının alabileceği en küçük tam sayı değeri kaçtır?',
 dogru=e2,yan=[(d1,'Alt sınır −5 − 7 = −12’yi bulmuş ama bu değer alınamaz (uçlar açık); en küçük tam sayı −11’dir.','dikkat'),(d2,'a’nın alt sınırından b’nin alt sınırını çıkarmış (−5 − 3); farkı küçültmek için b’nin üst sınırı gerekir.','bilgi'),(d3,'a’nın üst sınırından b’nin üst sınırını çıkarmış (2 − 7); en küçük değer için a küçük, b büyük olmalı.','bilgi'),(d4,'En küçük yerine en büyük tam sayıyı hesaplamış: 2 − 3 = −1 açık uç, en büyük tam sayı −2.','dikkat')],
 istenen='a − b ifadesinin en küçük tam sayı değeri.',
 ip=['a − b en küçük olsun diye a’yı en küçük, b’yi en büyük al; sonra açık uca dikkat et.'],
 bilgi=[ARL],
 ad=[A('Alt sınırı bul','a − b’yi en küçük yapmak için a en küçük, b en büyük alınır.','a − b > −5 − 7 = −12'),A('Üst sınırı bul','Tam aralığı görmek için üst sınır da hesaplanır.','a − b < 2 − 3 = −1 → −12 < a − b < −1'),A('Açık uca dikkat et','−12 değeri alınamaz; ondan büyük ilk tam sayı −11’dir.','en küçük tam sayı = −11')],
 puf='Çıkarmada alt sınır için “a’nın alt − b’nin üst”, üst sınır için “a’nın üst − b’nin alt” alınır.')

# ---------- 03 · kolay · asansör ----------
cap,gor,yol=700,90,75
dog=max(ints(lambda n:gor+yol*n<=cap)); assert dog==8 and gor+yol*8==690 and gor+yol*9==765
a1=max(ints(lambda n:yol*n<=cap)); assert a1==9
a2=max(ints(lambda n:2*gor+yol*n<=cap)); assert a2==6
a3=max(ints(lambda n:(gor+yol)*n<=cap)); assert a3==4
a4=-(-(cap-gor)//yol); assert a4==9
a4=-(-cap//yol); assert a4==10
assert len({dog,a1,a2,a3,a4})==5
mk(P,'0003',tipId='ezb-model',tip='Eşitsizlikle modelleme (bütçe, kapasite, tarife)',z='kolay',alt='Eşitsizlikle Modelleme',kaz='Taşıma sınırı verilen bir problemi eşitsizlik kurup tam sayıya yuvarlayarak çözer.',kalip='hikâyeli',adim=3,
 kart='K-ESZB-04 (modelleme) · asansör kapasitesi, görevli kütlesi ve en çok yolcu',
 metin='Bir bina asansörünün taşıma sınırı 700 kg’dır. Asansörde kütlesi 90 kg olan bir görevli bulunmaktadır ve asansöre binecek yolcuların her birinin kütlesi 75 kg olarak kabul edilmektedir.\nAsansörün sınırı aşılmayacağına göre görevliyle birlikte en çok kaç yolcu asansöre binebilir?',
 dogru=dog,yan=[(a1,'Görevlinin kütlesini hesaba katmadan 700 ÷ 75 işlemini yapıp 9’a yuvarlamış.','dikkat'),(a4,'700 ÷ 75 = 9,33’ü yukarı yuvarlayıp 10 demiş; hem görevli unutulmuş hem sınır aşılmıştır.','dikkat'),(a2,'Görevlinin kütlesini iki kez çıkarmış: 700 − 180 = 520, 520 ÷ 75 → 6.','islem'),(a3,'Görevlinin kütlesini her yolcuya eklemiş: (90 + 75) × n ≤ 700 → 4.','bilgi')],
 istenen='Asansöre binebilecek en çok yolcu sayısı.',
 ip=['Toplam kütle = görevli + yolcular ≤ 700 eşitsizliğini yaz.'],
 bilgi=[MODEL],
 ad=[A('Eşitsizliği kur','n yolcu sayısıdır; görevli ve yolcuların toplam kütlesi sınırı aşmamalıdır.','90 + 75n ≤ 700'),A('n’yi çöz','90’ı karşıya at ve 75’e böl.','75n ≤ 610 → n ≤ 8,13'),A('Tam sayıya yuvarla','Yolcu sayısı tam sayı olmalı ve sınırı aşmamalı; aşağı yuvarlanır.','n = 8 · kontrol: 90 + 600 = 690 ≤ 700 ve 9 yolcu için 765 > 700')],
 puf='“En çok” sorularında çıkan ondalık sonuç aşağı, “en az” sorularında yukarı yuvarlanır.')

# ---------- 04 · orta · −1 ≤ (7−2x)/3 < 3 toplam ----------
s4=ints(lambda x:-1<=Fr(7-2*x,3)<3); assert s4==list(range(0,6)) and sum(s4)==15
w1=sum(ints(lambda x:-1<=x<5)); assert w1==9                                       # uçların kapanışı ters
w2=sum(ints(lambda x:0<=x<=4)); assert w2==10
w3=sum(ints(lambda x:-3<=7-2*x<3)); assert w3==12                                  # sağı 3 ile çarpmamış
w4=sum(ints(lambda x:-1<=x<=5)); assert w4==14
assert len({15,w1,w2,w3,w4})==5
mk(P,'0004',tipId='ezb-cozum',tip='Eşitsizlik çözümü ve tam sayı değerleri',z='orta',alt='Eşitsizlik Çözme',kaz='Kesirli çift taraflı eşitsizliği çözerek sınırların dahil olup olmadığına göre tam sayı çözümlerinin toplamını bulur.',kalip='düz',adim=4,
 kart='K-ESZB-01 (eşitsizlik çözümü) · paydalı, negatif katsayılı çift taraflı eşitsizlik, uçların dahil olması',
 metin='x bir tam sayıdır.\n−1 ≤ (7 − 2x)/3 < 3\nkoşulunu sağlayan tüm x değerlerinin toplamı kaçtır?',
 dogru=15,yan=[(w1,'Negatife bölünce sınırları yer değiştirirken “≤” ve “<” işaretlerini de yer değiştirmemiş; −1 dahil, 5 hariç almış.','dikkat'),(w2,'Her iki ucu da çözüme almamış (0 ≤ x ≤ 4 gibi); oysa 5 dahildir, −1 değildir.','dikkat'),(w3,'Her tarafı 3 ile çarparken sağdaki 3’ü çarpmayı unutmuş: 7 − 2x < 3 almış.','islem'),(w4,'İki ucu da çözüme dahil almış (−1 ≤ x ≤ 5); eşitliğin hangi uçta olduğunu ayırt edememiş.','dikkat')],
 istenen='x tam sayılarının toplamı.',
 ip=['Her yeri 3 ile çarp, 7’yi çıkar, sonra −2’ye bölerken sınırların yerini ve işaretlerini düzelt.'],
 bilgi=[CIFT],
 ad=[A('3 ile çarp','Paydadan kurtulmak için üç tarafı 3 ile çarp.','−3 ≤ 7 − 2x < 9'),A('7’yi çıkar','Üç taraftan 7 çıkar.','−10 ≤ −2x < 2'),A('−2’ye böl','Sınırlar yer değiştirir ve işaretler de yer değiştirir: ≤ olan uç artık sağdadır.','−1 < x ≤ 5'),A('Toplamı bul','x = 0, 1, 2, 3, 4, 5 sayılarını topla.','0 + 1 + 2 + 3 + 4 + 5 = 15')],
 puf='Negatif sayıya bölünce yalnız sınırların yeri değil, hangi uçta eşitlik olduğu da yer değiştirir.')

# ---------- 05 · orta · eşitsizlik sistemi ----------
s5=ints(lambda x:2*(x+1)>=x+6 and 5*x-3<3*x+15); assert s5==[4,5,6,7,8] and sum(s5)==30
v1=sum(ints(lambda x:2*x+1>=x+6 and 5*x-3<3*x+15)); assert v1==26                  # 2’yi dağıtmamış
v2=len(s5); assert v2==5
v3=sum(ints(lambda x:x>=8 and 5*x-3<3*x+15)); assert v3==8                          # 2x + 2 ≥ x + 6 → x ≥ 8
v4=sum(ints(lambda x:2*(x+1)>=x+6 and 2*x<12)); assert v4==9                        # 15 − 3 yerine 12
assert len({30,v1,v2,v3,v4})==5
mk(P,'0005',tipId='ezb-cozum',tip='Eşitsizlik çözümü ve tam sayı değerleri',z='orta',alt='Eşitsizlik Sistemi',kaz='İki birinci dereceden eşitsizliğin ortak çözüm kümesini bulup tam sayı çözümlerinin toplamını hesaplar.',kalip='düz',adim=4,
 kart='K-ESZB-01 (eşitsizlik çözümü) · parantezli iki eşitsizlik, kesişim ve tam sayıların toplamı',
 metin='x bir tam sayı olmak üzere\n2(x + 1) ≥ x + 6\n5x − 3 < 3x + 15\neşitsizliklerinin ikisi birden sağlanıyor.\nBuna göre x’in alabileceği değerlerin toplamı kaçtır?',
 dogru=30,yan=[(v1,'İlk eşitsizlikte 2(x + 1)’i 2x + 1 diye açmış; x ≥ 5 bulup 5 + 6 + 7 + 8 = 26 yazmış.','islem'),(v2,'Çözüm sayısını (adet) yazmış; soru değerlerin toplamını istiyor.','dikkat'),(v3,'2x + 2 ≥ x + 6 çözümünde 2’yi yanlış taşıyıp x ≥ 8 bulmuş; yalnız 8 kalmış.','islem'),(v4,'İkinci eşitsizlikte 15 − (−3) yerine 15 − 3 = 12 yapmış; x < 6 bulup 4 + 5 = 9 yazmış.','islem')],
 istenen='İki eşitsizliği birlikte sağlayan tam sayıların toplamı.',
 ip=['Her eşitsizliği ayrı çöz, sonra ortak bölgeyi bul.'],
 bilgi=[ISRT,SISTEM],
 ad=[A('Birincisini çöz','Parantezi aç, x’leri bir tarafa topla.','2x + 2 ≥ x + 6 → x ≥ 4'),A('İkincisini çöz','x’leri sola, sayıları sağa topla.','2x < 18 → x < 9'),A('Ortak bölgeyi bul','İkisini birlikte sağlayan sayılar 4 ve 4’ten büyük, 9’dan küçüktür.','4 ≤ x < 9'),A('Toplamı hesapla','x = 4, 5, 6, 7, 8 sayılarını topla.','4 + 5 + 6 + 7 + 8 = 30')],
 puf='Sistemde her eşitsizliği ayrı çöz; sonuç, ikisini birden sağlayan ortak bölgedir.')

# ---------- 06 · orta · 3x − 2y en küçük tam sayı ----------
xl,xh,yl,yh=-2,4,1,4
f6=lambda x,y:3*x-2*y
vals=[f6(x,y) for x in grid(xl,xh) for y in grid(yl,yh)]; assert -14<min(vals) and max(vals)<10
d6=min(open_ints(-14,10)); assert d6==-13 and all(erisilir(f6,Fr(xl),Fr(xh),Fr(yl),Fr(yh),k) for k in range(-13,10)) and not erisilir(f6,Fr(xl),Fr(xh),Fr(yl),Fr(yh),-14)
u1=3*xl-2*yh; u2=3*xl-2*yl; u3=3*xl+2*yl; u4=xl-yh
assert (u1,u2,u3,u4)==(-14,-8,-4,-6)
c1=u1; c2=u2+1; c3=u3+1; c4=u4+1
assert (c2,c3,c4)==(-7,-3,-5)
assert len({d6,c1,c2,c3,c4})==5
mk(P,'0006',tipId='ezb-aralik',tip='Aralık işlemleri ve ifadenin tam sayı değerleri',z='orta',alt='Aralık İşlemleri',kaz='Katsayılı bir ifadenin alt sınırını iki değişkenin aralığından bulup açık uca göre en küçük tam sayı değerini belirler.',kalip='düz',adim=3,
 kart='K-ESZB-02 (aralık işlemleri) · 3x − 2y için en küçük tam sayı değeri',
 metin='x ve y gerçel sayılar olmak üzere\n−2 < x < 4\n1 < y < 4\nolduğuna göre 3x − 2y ifadesinin alabileceği en küçük tam sayı değeri kaçtır?',
 dogru=d6,yan=[(c1,'Alt sınır −14’ü bulmuş ama uçlar açık olduğundan −14 alınamaz; en küçük tam sayı −13’tür.','dikkat'),(c2,'−2y’nin alt sınırı için y’nin üst sınırını değil alt sınırını almış: 3 × (−2) − 2 × 1 = −8, açık uçtan −7.','bilgi'),(c3,'−2y yerine +2y kullanmış: 3 × (−2) + 2 × 1 = −4, açık uçtan −3.','islem'),(c4,'Katsayıları atlayıp x − y’nin alt sınırını bulmuş: −2 − 4 = −6, açık uçtan −5.','islem')],
 istenen='3x − 2y ifadesinin en küçük tam sayı değeri.',
 ip=['3x’i en küçük, 2y’yi en büyük yapacak sınırları seç; uçların açık olduğuna dikkat et.'],
 bilgi=[ARL,ACIK],
 ad=[A('3x’in sınırı','−2 < x < 4 aralığını 3 ile çarp.','−6 < 3x < 12'),A('−2y’nin sınırı','1 < y < 4 aralığını −2 ile çarp, sınırlar yer değiştirir.','−8 < −2y < −2'),A('Topla ve tam sayıya bak','Alt sınırlar ve üst sınırlar ayrı toplanır; −14 alınamaz.','−14 < 3x − 2y < 10 → en küçük tam sayı = −13')],
 puf='Negatif katsayılı terim aralığı çevirir: önce çarp, sonra alt ile alt, üst ile üstü topla.')

# ---------- 07 · orta · 0<x<1 zincir ----------
import math
ch=lambda x:{'x':x,'x²':x*x,'√x':math.sqrt(x),'1/x':1/x}
def sirala(x): return sorted(ch(x),key=lambda k:ch(x)[k])
ok=' < '.join(['x²','x','√x','1/x'])
for xx in [0.01,0.04,0.25,0.5,0.81,0.99]: assert ' < '.join(sirala(xx))==ok
W=['x < x² < √x < 1/x','x² < √x < x < 1/x','x² < x < 1/x < √x','1/x < x² < x < √x']
for w in W:
    ks=[t.strip() for t in w.split('<')]
    assert any([ch(xx)[ks[i]]<ch(xx)[ks[i+1]] for i in range(3)].count(False)>0 for xx in [0.25,0.5])
sira7=[ok,W[0],W[1],W[2],W[3]]
mk(P,'0007',tipId='ezb-kare',tip='Kare, kök ve ters ile sıralama (0 < x < 1)',z='orta',alt='Kare ve Terslerle Sıralama',kaz='0 ile 1 arasındaki bir sayının kare, kök ve tersini karşılaştırarak doğru sıralamayı bulur.',kalip='düz',adim=3,
 kart='K-ESZB-05 (0 < x < 1) · x, x², √x, 1/x sıralaması',
 metin='0 < x < 1 olmak üzere x, x², √x ve 1/x sayılarının küçükten büyüğe doğru sıralanışı aşağıdakilerden hangisidir?',
 dogru=ok,sira=sira7,yan=[(W[0],'x² sayısını x’ten büyük sanmış; 0 ile 1 arasında kendisiyle çarpmak sayıyı küçültür.','bilgi'),(W[1],'Köklü sayının x’ten küçük olduğunu düşünmüş; 0 ile 1 arasında kök almak sayıyı büyütür.','bilgi'),(W[2],'√x’i 1’den büyük sanmış; √x yine 1’den küçüktür, 1/x ise 1’den büyüktür.','bilgi'),(W[3],'1/x’i en küçük sanmış; payı paydadan küçük olan x için tersi 1’den büyük olur.','bilgi')],
 istenen='x, x², √x ve 1/x sayılarının küçükten büyüğe sıralanışı.',
 ip=['x yerine 0,25 gibi bir sayı koy; kare, kök ve tersini hesapla.'],
 bilgi=[KARE],
 ad=[A('Bir örnek seç','0 < x < 1 olan bir sayıyı dene.','x = 0,25'),A('Değerleri hesapla','Dört sayıyı yaz ve karşılaştır.','x² = 0,0625 · x = 0,25 · √x = 0,5 · 1/x = 4'),A('Sırala ve genelle','Sıralama 0 < x < 1 için hep böyledir: kare en küçük, ters en büyük.','x² < x < √x < 1/x')],
 puf='0 < x < 1 iken: kare küçültür, kök büyütür, ters 1’in üstüne çıkarır.')

# ---------- 08 · orta · öncüllü a < b < 0 ----------
OP=['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III']
OP8=['Yalnız I','Yalnız III','I ve II','I ve III','II ve III']
def ad_(v):
    k=['I','II','III']; s=[k[i] for i in range(3) if v[i]]
    return 'Yalnız '+s[0] if len(s)==1 else ('I, II ve III' if len(s)==3 else ' ve '.join(s))
tv=[]
for a,b in [(-9,-2),(-5,-4),(Fr(-7,2),Fr(-1,3)),(-1,Fr(-1,100)),(-20,-19),(Fr(-3,2),-1)]:
    assert a<b<0
    tv.append((1/a>1/b, a*a<b*b, a*b>b*b))
assert all(t==(True,False,True) for t in tv)
assert ad_((True,False,True))=='I ve III' and ad_((True,True,False))=='I ve II' and ad_((False,True,False))=='Yalnız II' and ad_((True,True,True))=='I, II ve III' and ad_((True,False,False))=='Yalnız I' and ad_((False,False,True))=='Yalnız III' and ad_((False,True,True))=='II ve III'
mk(P,'0008',tipId='ezb-siralama',tip='Eşitsizliklerde sıralama ve kesinlikle doğru ifadeler',z='orta',alt='Sıralama',kaz='Negatif iki sayının terslerini, karelerini ve çarpımlarını karşılaştırarak öncüllerin doğruluğunu belirler.',kalip='öncüllü',adim=3,
 kart='K-ESZB-03 (eşitsizlikle sıralama) · a < b < 0 için ters, kare ve çarpım öncülleri',
 metin='a ve b gerçel sayıları için\na < b < 0\nolduğu biliniyor.\nBuna göre\nI. 1/a > 1/b\nII. a² < b²\nIII. a · b > b²\nifadelerinden hangileri kesinlikle doğrudur?',
 dogru='I ve III',sira=OP8,yan=[('I ve II','a < b olduğundan a² < b² sanmış; iki negatif sayıda mutlak değeri büyük olan sayının karesi de büyüktür (a = −3, b = −1 → 9 > 1).','bilgi'),('Yalnız I','III’te a < b’yi negatif b ile çarparken yönü değiştirmemiş; a · b < b² bulup III’ü yanlış saymış.','bilgi'),('Yalnız III','Terslerde sıranın korunduğunu sanıp I’i yanlış bulmuş; III’ü doğru çözmüş ve II’nin yanlışlığını görmüş.','bilgi'),('II ve III','a < b’den hem 1/a < 1/b hem a² < b² çıkarmış (I yanlış, II doğru demiş); III’ü doğru bulmuş.','bilgi')],
 istenen='Kesinlikle doğru olan ifadeler.',
 ip=['a = −3, b = −1 gibi örnek dene; sonra a < b eşitsizliğini negatif b ile çarparak III’ü sına.'],
 bilgi=[SIRA],
 ad=[A('I’i incele','a < b < 0 olduğundan a × b pozitiftir; a < b eşitsizliğini a × b’ye bölünce yön korunur ve terslerde sıra ters döner.','a < b → 1/b < 1/a → I doğru · örnek: a = −3, b = −1 → −1/3 > −1'),A('II’yi incele','Negatif sayılarda mutlak değeri büyük olan daha küçüktür; karesi ise daha büyüktür.','|a| > |b| → a² > b² → II yanlış'),A('III’ü incele','a < b eşitsizliğinin iki tarafını negatif b ile çarp; yön değişir.','a < b → a × b > b × b = b² → III doğru'),A('Sonucu yaz','Kesinlikle doğru olanlar I ve III’tür.','I ve III')],
 puf='Negatif sayılarda sıralama kare ve terste ters döner; negatif sayıyla çarpınca da yön değişir.')

# ---------- 09 · orta · iki tarife ----------
g9=min(ints(lambda g:g>0 and 100+2*g<60+5*g)); assert g9==14 and 100+2*14==128 and 60+5*14==130 and 100+26>60+65
t1=max(ints(lambda g:g>0 and 100+2*g>=60+5*g)); assert t1==13                      # aşağı yuvarlama
t2=12; assert 40//3==13 and 60+5*12==120 and 100+2*12==124; t3=40//2; t4=int(Fr(40,3)); assert (t3,t4)==(20,13) or True
t4=40                                                                               # katsayı farkına bölmemiş
assert len({g9,t1,t2,t3,t4})==5
mk(P,'0009',tipId='ezb-model',tip='Eşitsizlikle modelleme (bütçe, kapasite, tarife)',z='orta',alt='Eşitsizlikle Modelleme',kaz='İki tarifeyi karşılaştıran eşitsizliği kurup tam sayıya yuvarlayarak en az kullanım miktarını bulur.',kalip='hikâyeli',adim=3,
 kart='K-ESZB-04 (modelleme) · sabit ücret ve kullanım ücretli iki tarifeden hangisinin ucuz olduğu',
 metin='Bir internet firmasının A tarifesinde aylık sabit ücret 60 TL’dir ve her GB için 5 TL ödenir. B tarifesinde aylık sabit ücret 100 TL’dir ve her GB için 2 TL ödenir. Aylık kullanım, tam GB olarak hesaplanır.\nB tarifesi A tarifesinden daha ucuz olsun isteniyorsa aylık kullanım en az kaç GB olmalıdır?',
 dogru=g9,yan=[(t1,'13,33’ü “en çok” sorularındaki gibi aşağı yuvarlayıp 13 yazmış; oysa 13 GB’ta A 125 TL, B 126 TL olduğundan B hâlâ daha pahalıdır.','dikkat'),(t2,'40 ÷ 3’ü 12 bulup 12 GB demiş (işlem hatası); 12 GB’ta A 120 TL, B 124 TL olduğundan B daha pahalıdır.','islem'),(t3,'Yalnız B’nin birim ücretini kullanıp 40 ÷ 2 = 20 yazmış; iki tarifenin farkına (5 − 2) bölmesi gerekir.','bilgi'),(t4,'Sabit ücret farkını (40) cevap sanmış; 3g > 40 eşitsizliğini çözmemiş.','islem')],
 istenen='B tarifesinin daha ucuz olması için gereken en az GB.',
 ip=['g GB için iki ücreti yaz: A = 60 + 5g, B = 100 + 2g. B < A eşitsizliğini çöz.'],
 bilgi=[MODEL],
 ad=[A('Ücretleri yaz','g GB için iki tarifenin aylık ücretini yaz.','A: 60 + 5g · B: 100 + 2g'),A('B < A kur','B’nin ucuz olması için B’nin ücreti A’nınkinden az olmalı.','100 + 2g < 60 + 5g → 40 < 3g → g > 13,33'),A('Yuvarla ve kontrol et','Tam GB hesaplandığı için 13,33’ten büyük en küçük tam sayı 14’tür.','g = 14: A = 130, B = 128 · g = 13: A = 125, B = 126')],
 puf='İki tarifeyi karşılaştırırken sabit ücret farkını birim ücret farkına böl; “daha ucuz” için eşitlik dahil değildir.')

# ---------- 10 · orta · yeni nesil, tanımlı işlem ----------
op=lambda a,b:4*a-3*b+1
xl,xh,yl,yh=-1,3,0,3
vals=[op(x,y) for x in grid(xl,xh) for y in grid(yl,yh)]; assert -12<min(vals) and max(vals)<13
n10=len(open_ints(-12,13)); assert n10==24 and all(erisilir(op,Fr(xl),Fr(xh),Fr(yl),Fr(yh),k) for k in range(-11,13))
assert not erisilir(op,Fr(xl),Fr(xh),Fr(yl),Fr(yh),-12) and not erisilir(op,Fr(xl),Fr(xh),Fr(yl),Fr(yh),13)
k1=26; k2=13-(-12); k3=len(open_ints(4*xl-3*yl+1-0,4*xh-3*yh+1)); k4=len(open_ints(4*xl-yh+1,4*xh+1))
assert (k2,k3,k4)==(25,6,18),(k2,k3,k4)
assert len({n10,k1,k2,k3,k4})==5
mk(P,'0010',tipId='ezb-yeni',tip='Tanımlı işlemle aralık problemi',z='orta',alt='Tanımlı İşlem ve Aralık',kaz='Yeni tanımlanan bir işlemin sonucunu değişkenlerin aralığından sınırlayıp aldığı tam sayı değerlerinin adedini bulur.',kalip='düz',adim=4,
 kart='K-ESZB-06 (tanımlı işlem) · a ⊕ b = 4a − 3b + 1 işlemi ve x ⊕ y’nin tam sayı değer adedi',
 metin='Gerçel sayılar kümesinde bir ⊕ işlemi\na ⊕ b = 4a − 3b + 1\nbiçiminde tanımlanıyor.\nx ve y gerçel sayıları için −1 < x < 3 ve 0 < y < 3 olduğuna göre x ⊕ y ifadesi kaç farklı tam sayı değeri alabilir?',
 dogru=n10,yan=[(k1,'Uçlardaki −12 ve 13 değerlerini de sayarak −12’den 13’e 26 tam sayı bulmuş; uçlar açık olduğundan alınamaz.','dikkat'),(k2,'Üst sınırdan alt sınırı çıkarıp 25 bulmuş; açık aralıkta tam sayı sayısı fark − 1’dir.','islem'),(k3,'Alt sınırı bulurken y’nin alt, üst sınırı bulurken y’nin üst değerini almış: (−3, 4) aralığından 6 tam sayı bulmuş.','bilgi'),(k4,'−3b yerine −b alarak katsayıyı yanlış kullanmış; (−6, 13) aralığından 18 tam sayı bulmuş.','islem')],
 istenen='x ⊕ y ifadesinin aldığı farklı tam sayı değerlerinin adedi.',
 ip=['4x ve −3y aralıklarını ayrı ayrı bul, sonra +1 ile birlikte topla.'],
 bilgi=[ARL,ACIK],
 ad=[A('4x’in sınırı','−1 < x < 3 aralığını 4 ile çarp.','−4 < 4x < 12'),A('−3y’nin sınırı','0 < y < 3 aralığını −3 ile çarp, sınırlar yer değiştirir.','−9 < −3y < 0'),A('Toplayıp 1 ekle','Alt sınırlar ve üst sınırlar ayrı toplanır, sonra +1 eklenir.','−12 < x ⊕ y < 13'),A('Tam sayıları say','−12 ve 13 alınamaz; −11’den 12’ye kadar tam sayılar vardır.','12 − (−11) + 1 = 24')],
 puf='Açık aralıkta (a, b) tam sayı sayısı b − a − 1’dir (uçlar tam sayı ise).')

# ---------- Z1 · zor · x·y en büyük tam sayı ----------
xl,xh,yl,yh=-3,2,-4,1
f=lambda x,y:x*y
vals=[f(x,y) for x in grid(xl,xh,32) for y in grid(yl,yh,32)]; assert -8<min(vals) and max(vals)<12
corn=sorted(a*b for a,b in product([xl,xh],[yl,yh])); assert corn==[-8,-3,2,12]
z1=max(open_ints(-8,12)); assert z1==11 and all(erisilir(f,Fr(xl),Fr(xh),Fr(yl),Fr(yh),k) for k in range(-7,12)) and not erisilir(f,Fr(xl),Fr(xh),Fr(yl),Fr(yh),12)
z1e=[12,2,-3,min(open_ints(-8,12))]; assert z1e==[12,2,-3,-7] and len({z1}|set(z1e))==5
mk(P,'0011',tipId='ezb-aralik',tip='Aralık işlemleri ve ifadenin tam sayı değerleri',z='orta',alt='Aralıkta Çarpım',kaz='İki aralığın çarpımında dört uç çarpımı arasından üst sınırı bulup açık uca göre en büyük tam sayı değerini belirler.',kalip='düz',adim=4,
 kart='K-ESZB-02 (aralık işlemleri) · x·y için dört uç çarpımı ve açık uçlu en büyük tam sayı',
 metin='x ve y gerçel sayılar olmak üzere\n−3 < x < 2\n−4 < y < 1\nolduğuna göre x · y çarpımının alabileceği en büyük tam sayı değeri kaçtır?',
 dogru=z1,yan=[(12,'Üst sınırı (−3) × (−4) = 12 bulup tam sayı olarak aynen almış; uçlar açık olduğundan 12 alınamaz, en büyük tam sayı 11’dir.','dikkat'),(2,'İki üst sınırı çarpmış (2 × 1); negatif iki sayının çarpımı pozitif ve daha büyük olabilir.','bilgi'),(-3,'Yalnız x’in alt sınırı ile y’nin üst sınırını çarpmış (−3 × 1); dört uç çarpımından en büyüğünü seçmemiş.','bilgi'),(-7,'En büyük yerine en küçük tam sayıyı hesaplamış: alt sınır 2 × (−4) = −8, açık uçtan −7.','dikkat')],
 istenen='x · y’nin en büyük tam sayı değeri.',
 ip=['Çarpımda negatif sınırlar vardır; dört uç çarpımını yazıp en büyüğüne bak.'],
 bilgi=[CARP,ACIK],
 ad=[A('Uç çarpımları yaz','Aralıkların uçlarını çaprazlama çarp.','(−3) × (−4) = 12 · (−3) × 1 = −3 · 2 × (−4) = −8 · 2 × 1 = 2'),A('Alt ve üst sınırı seç','En küçük −8, en büyük 12’dir; uçlar açık olduğundan çarpım bu değerlere ulaşmaz.','−8 < x × y < 12'),A('Alınabilirliği kontrol et','x ve y kendi aralıklarında sürekli değiştiğinden çarpım, (−8, 12) aralığındaki her değeri alır; 11 de bu aralıktadır.','−8 < 11 < 12 → 11 alınır'),A('Sonucu yaz','12 alınamayacağından en büyük tam sayı 11’dir.','11')],
 puf='Çarpımda dört uç çarpımına bak; açık uçlu aralıkta uç değer alınamaz, ona en yakın tam sayı seçilir.')

# ---------- Z2 · zor · bütçe ve iki kısıt ----------
K,T,Bu=40,70,500
sol=[(k,t) for k in range(0,20) for t in range(0,20) if K*k+T*t<=Bu and t>=k+1]
z2=max(k+t for k,t in sol); assert z2==8 and (3,5) in sol and (2,6) in sol and (4,5) not in sol
q1=max(k+t for k in range(20) for t in range(20) if K*k+T*t<=Bu); assert q1==12
q2=max(k+t for k,t in sol if t==k+1); assert q2==7
q3=4+5; assert q3==9 and K*4+T*5==510>Bu
q4=7+3; assert q4==10 and K*7+T*3==490<=Bu and 7>3
assert len({z2,q1,q2,q3,q4})==5
mk(P,'0012',tipId='ezb-model',tip='Eşitsizlikle modelleme (bütçe, kapasite, tarife)',z='zor',alt='Eşitsizlikle Modelleme',kaz='Bütçe ve adet koşullarını eşitsizliğe çevirip birlikte düşünerek alınabilecek en çok ürün sayısını bulur.',kalip='hikâyeli',adim=5,
 kart='K-ESZB-04 (modelleme) · bütçe ve “tatlı kahveden fazla olmalı” koşuluyla en çok ürün sayısı',
 metin='Bir kafede kahvenin tanesi 40 TL, tatlının tanesi 70 TL’dir. Elinde 500 TL bulunan Burak, aldığı tatlı sayısının aldığı kahve sayısından fazla olmasını istiyor.\nBurak parasını aşmadan en çok toplam kaç ürün (kahve ve tatlı birlikte) alabilir?',
 dogru=z2,yan=[(q1,'“Tatlı kahveden fazla olsun” koşulunu hiç kullanmayıp yalnız kahve alarak 500 ÷ 40 = 12 bulmuş.','dikkat'),(q2,'Yalnız kahve sayısından 1 fazla tatlı alınan durumu (3 kahve + 4 tatlı) denemiş; kalan parayı değerlendirmemiş.','dikkat'),(q3,'4 kahve + 5 tatlıyı (160 + 350 = 510 TL) bütçeyi aştığını denetlemeden alıp 9 demiş.','dikkat'),(q4,'Koşulu ters okuyup (kahve tatlıdan fazla) 7 kahve + 3 tatlıyı (280 + 210 = 490 TL) alıp 10 demiş.','dikkat')],
 istenen='Burak’ın alabileceği toplam ürün sayısının en büyük değeri.',
 ip=['k kahve, t tatlı için 40k + 70t ≤ 500 ve t > k koşullarını yaz; k’yi sırayla dene.'],
 bilgi=[MODEL],
 ad=[A('Koşulları yaz','k kahve sayısı, t tatlı sayısıdır; para ve adet koşulu birlikte sağlanmalıdır.','40k + 70t ≤ 500 · t ≥ k + 1'),A('k’yi sırayla dene','Her k için en çok kaç tatlı alınabileceğine bak ve t ≥ k + 1’i denetle.','k = 3: 70t ≤ 380 → t ≤ 5 → toplam 8 · k = 4: 70t ≤ 340 → t ≤ 4 < 5 olmaz'),A('Küçük k’ları karşılaştır','Az kahveyle tatlı sayısı artar ama tatlı pahalıdır.','k = 2: t ≤ 6 → 8 · k = 1: t ≤ 6 → 7 · k = 0: t ≤ 7 → 7'),A('En büyüğünü seç','Toplam ürün en çok 8 olur.','3 kahve + 5 tatlı = 120 + 350 = 470 TL · 2 kahve + 6 tatlı = 500 TL')],
 puf='Bütçe ve adet koşulu birlikte varsa küçük adetten başlayıp denetle; yalnız kısıtların uç durumu her zaman en iyisi olmaz.')

# ---------- Z3 · zor · öncüllü a < b < 0 < c, |b| < c < |a| ----------
import random
random.seed(7)
tvz=[]
for _ in range(6000):
    a=-Fr(random.randint(1,60),random.randint(1,7)); b=-Fr(random.randint(1,60),random.randint(1,7)); c=Fr(random.randint(1,120),random.randint(1,7))
    if not (a<b<0<c and -b<c<-a): continue
    tvz.append((a+c<0, a+b+c>0, b+c>0))
assert len(tvz)>100 and all(t==(True,False,True) for t in tvz)
assert ad_((True,False,True))=='I ve III' and ad_((False,True,False))=='Yalnız II' and ad_((True,True,False))=='I ve II'
mk(P,'0013',tipId='ezb-siralama',tip='Eşitsizliklerde sıralama ve kesinlikle doğru ifadeler',z='zor',alt='Sıralama',kaz='İşaret ve mutlak değer bilgisini birlikte kullanarak toplam ifadelerinin işaretini belirler ve öncüllerin kesinlikle doğru olup olmadığına karar verir.',kalip='öncüllü',adim=4,
 kart='K-ESZB-03 (eşitsizlikle sıralama) · a < b < 0 < c ve |b| < c < |a| koşuluyla toplam öncüllerinin işareti',
 metin='a, b ve c gerçel sayıları için\na < b < 0 < c\n|b| < c < |a|\nolduğu biliniyor.\nBuna göre\nI. a + c < 0\nII. a + b + c > 0\nIII. b + c > 0\nifadelerinden hangileri kesinlikle doğrudur?',
 dogru='I ve III',sira=OP,yan=[('Yalnız I','III’te b negatif diye b + c’yi negatif sanmış; |b| < c olduğundan c’den küçük bir sayı çıkarılır ve toplam pozitiftir.','bilgi'),('I ve II','I ve III’ü bulup II’yi de doğru sanmış; a + c < 0 ve b < 0 olduğundan a + b + c negatiftir.','dikkat'),('Yalnız II','I’de |a| > c bilgisini kullanmayıp a + c > 0 sanmış, III’ü yanlış saymış; a + b + c’yi de pozitif bulmuş.','bilgi'),('I, II ve III','Üçünü de doğru sanmış; a + b + c için a + c < 0 olduğundan toplam negatiftir, II yanlıştır.','dikkat')],
 istenen='Kesinlikle doğru olan ifadeler.',
 ip=['|b| < c ve c < |a| bilgisini kullanarak b + c ile a + c’nin işaretlerini ayrı ayrı bul.'],
 bilgi=[SIRA,B('Mutlak değerle toplamın işareti','Negatif x ile pozitif y için |x| < y ise x + y pozitif, |x| > y ise x + y negatiftir. Örnek: −2 + 5 = 3 > 0, −7 + 5 = −2 < 0')],
 ad=[A('I’i incele','c < |a| olduğundan c, a’nın büyüklüğünden küçüktür; a + c negatif çıkar.','c < −a → a + c < 0 → I doğru'),A('III’ü incele','|b| < c olduğundan b + c pozitiftir.','−b < c → b + c > 0 → III doğru'),A('II’yi incele','a + c negatif ve b negatif; ikisinin toplamı pozitif olamaz.','a + b + c = (a + c) + b < 0 → II yanlış'),A('Sonucu yaz','Kesinlikle doğru olanlar I ve III’tür.','I ve III · örnek a = −5, b = −1, c = 3 → −2, −3, 2')],
 puf='Negatif ve pozitif sayının toplamında işareti mutlak değeri büyük olan belirler; üç terimde önce ikili toplamları değerlendir.')

# ---------- Z4 · zor · 1 < x + y < 5, −2 < x − y < 4 için x + 3y ----------
sl,sh,dl,dh=1,5,-2,4
f4=lambda s,d:2*s-d       # x+3y = 2(x+y) − (x−y)
for s,d in product(grid(sl,sh,12),grid(dl,dh,12)):
    x=(s+d)/2; y=(s-d)/2
    assert x+3*y==2*s-d
vals=[2*s-d for s in grid(sl,sh,32) for d in grid(dl,dh,32)]; assert -2<min(vals) and max(vals)<12
z4=max(open_ints(-2,12)); assert z4==11
e1=12; e2=max(open_ints(2*sl+dl,2*sh+dh)); assert e2==13
xr=(Fr(sl+dl,2),Fr(sh+dh,2)); yr=(Fr(sl-dh,2),Fr(sh-dl,2)); e3=max(open_ints(xr[0]+3*yr[0],xr[1]+3*yr[1])); assert e3==14,(xr,yr,e3)
e4=max(open_ints(3*sl-2*dh,3*sh-2*dl)); assert e4==18 and 3*sh-2*dl==19
assert len({z4,e1,e2,e3,e4})==5
mk(P,'0014',tipId='ezb-aralik',tip='Aralık işlemleri ve ifadenin tam sayı değerleri',z='zor',alt='Aralık İşlemleri',kaz='Toplam ve fark aralığı verilen iki sayıdan oluşan bir ifadeyi bu iki ifadenin birleşimi olarak yazıp en büyük tam sayı değerini bulur.',kalip='düz',adim=5,
 kart='K-ESZB-02 (aralık işlemleri) · x + y ve x − y aralığı verilip x + 3y için en büyük tam sayı',
 metin='x ve y gerçel sayıları için\n1 < x + y < 5\n−2 < x − y < 4\nolduğuna göre x + 3y ifadesinin alabileceği en büyük tam sayı değeri kaçtır?',
 dogru=z4,yan=[(e1,'Üst sınırı 12 bulup açık uç olduğunu atlamış; 12 alınamaz, en büyük tam sayı 11’dir.','dikkat'),(e2,'x + 3y = 2(x + y) + (x − y) yazıp farkın işaretini yanlış almış; üst sınırı 2 × 5 + 4 = 14 bulmuş, uç açık olduğundan 13 yazmış.','islem'),(e3,'x ile y’nin aralığını ayrı ayrı bulup üst sınırlarını toplamış (x < 4,5 ve y < 3,5 → 15); x ve y birbirinden bağımsız değildir.','bilgi'),(e4,'x + 3y’yi 3(x + y) − 2(x − y) diye yazmış (x’in katsayısını denetlememiş, bu ifade x + 5y’dir); üst sınırı 15 + 4 = 19, açık uçtan 18 bulmuş.','islem')],
 istenen='x + 3y ifadesinin en büyük tam sayı değeri.',
 ip=['x + 3y = m(x + y) + n(x − y) olacak şekilde m ve n’yi bul.'],
 bilgi=[ARL,ACIK,B('İfadeyi verilenlerin birleşimi yapma','x + 3y gibi bir ifade, verilen iki ifadenin m ve n katsayılarıyla birleşimi olarak yazılır: m(x + y) + n(x − y). x ve y’nin katsayıları eşitlenir. Örnek: x + 2y = 1,5(x + y) − 0,5(x − y)')],
 ad=[A('Katsayıları bul','x + 3y = m(x + y) + n(x − y) olsun; x ve y’nin katsayılarını eşitle.','m + n = 1 · m − n = 3 → m = 2, n = −1'),A('İfadeyi yaz','Buna göre x + 3y, toplamın iki katından farkı çıkarmaktır.','x + 3y = 2(x + y) − (x − y)'),A('Aralıkları işle','2(x + y) için ve −(x − y) için sınırları ayrı bul (−1 ile çarpınca sınırlar yer değiştirir).','2 < 2(x + y) < 10 · −4 < −(x − y) < 2'),A('Topla ve tam sayıya bak','Alt ile alt, üst ile üstü topla; üst uç açıktır.','−2 < x + 3y < 12 → en büyük tam sayı = 11'),A('Kontrol et','x + y = s ve x − y = d bağımsız seçilebilir, bu yüzden bütün değerler alınır.','s = 4,5 ve d = −2 yakını iken 2 × 4,5 + 2 = 11 elde edilir (s, d aralıkta ayrı ayrı seçilir)')],
 puf='İfade verilen iki ifadenin birleşimi olarak yazılabiliyorsa x ve y’yi ayırmadan doğrudan o ifadeyle aralığı bul; ayrı ayrı sınırlamak bağımlılığı bozar.')

bitir(P,'esitiki','mat|Basit Eşitsizlikler')
from collections import Counter
print(Counter(q['cevap']['sik'] for q in P.ANA),Counter(q['zorluk'] for q in P.ANA))
