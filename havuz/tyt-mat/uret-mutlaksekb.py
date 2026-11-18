"""Mutlak Değer · ŞEKİLLİ ek paket b (mutlaksekb): 10 soru, hepsi şekilli/grafikli/tablolu. Kardeş yok, ipucu 1.
Her doğru cevap ve her çeldirici değer kodla (tarama / Fraction) hesaplanıp assert edilir. Şekil ölçüleri Python'da üretilir (bkz. havuz/URETIM-SEKIL.md)."""
import sys,os,math
from itertools import combinations
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
H.KONU='Mutlak Değer'
P=Parti('mutlaksekb','Mutlak Değer','mat|Mutlak Değer')
KY='ÖSYM 2018–2026 TYT Matematik (şekilli/grafikli/tablolu mutlak değer soruları; yalnız mantık) · MEB 9. sınıf'
TP=lambda g:tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'+g+'\n\\end{tikzpicture}')
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)
def tara(f,lo=-300,hi=300): return [x for x in range(lo,hi+1) if f(x)]
def sec(dog,havuz,harf):
    i='ABCDE'.index(harf)
    for c in combinations(havuz,4):
        v=[p[0] for p in c]
        if len({dog,*v})==5 and sum(p<dog for p in v)==i: return list(c)
    raise AssertionError(('harf tutmuyor',harf,dog,[p[0] for p in havuz]))
def hata(dog,havuz,harf): return sec(dog,havuz,harf)
def sayidog(x0,x1,s,y,etk=1,font='\\scriptsize'):
    t=f'\\draw[-{{Stealth}}] ({(x0-.5)*s:.2f},{y}) -- ({(x1+.6)*s:.2f},{y});'
    for i in range(x0,x1+1): t+=f'\\draw ({i*s:.2f},{y-.08}) -- ({i*s:.2f},{y+.08});'+(f'\\node[below=3pt,font={font}] at ({i*s:.2f},{y-.08}) {{${i}$}};' if i%etk==0 else '')
    return t

# ---------- bilgi kutuları ----------
MUT=B('Mutlak değer','bir sayının mutlak değeri, sayı doğrusunda o sayının 0’a uzaklığıdır; |x| = x (x ≥ 0 ise) ve |x| = −x (x < 0 ise). Örnek: |−7| = 7, |5| = 5')
UZ=B('İki sayı arasındaki uzaklık','a ve b sayılarının sayı doğrusundaki uzaklığı |a − b| = |b − a| ile bulunur ve her zaman 0 ya da pozitiftir. Örnek: −2 ile 5 arasındaki uzaklık |−2 − 5| = 7’dir')
ORT=B('Orta nokta','iki sayıya eşit uzaklıktaki sayı, bu iki sayının aritmetik ortalamasıdır. Örnek: 2 ile 10’a eşit uzaklıktaki sayı (2 + 10) ÷ 2 = 6’dır')
SAP=B('Aritmetik ortalama ve sapma','aritmetik ortalama, değerlerin toplamının değer sayısına bölünmesiyle bulunur; bir değerin sapması, değerle ortalama arasındaki farkın mutlak değeridir. Örnek: 2, 4 ve 9’un ortalaması 5 olup sapmaları 3, 1 ve 4’tür')
ARL=B('Mutlak değer ve eşitsizlik','mutlak değerli bir ifade, ifadenin sıfıra uzaklığıdır; bir eşitsizlikte uzaklığın sınırı iki yönde de geçerlidir. Örnek: |x| ≤ 2 koşulunu sağlayan tam sayılar −2, −1, 0, 1, 2’dir')
SAYI=B('Ardışık tam sayıların sayısı','a ile b arasındaki (uçlar dahil) tam sayıların sayısı b − a + 1’dir. Örnek: 4’ten 9’a kadar 9 − 4 + 1 = 6 tam sayı vardır')
ISL=B('Akış şemasında işlem sırası','işlemler okların yönünde sırayla uygulanır; her kutunun çıktısı bir sonraki kutunun girdisidir. Örnek: önce 3 çıkarıp sonra mutlak değerini alan makineye 1 girerse 2 çıkar')
OZ=B('Mutlak değerli ifadeler','|x + y| ile |x| + |y| her zaman eşit değildir; işareti belli sayıların mutlak değeri işaret bakılarak açılır. Örnek: x = −3, y = 5 için |x + y| = 2, |x| + |y| = 8’dir')
GRF=B('Parçalı grafik okuma','mutlak değerli bir ifadenin grafiği, mutlak değerin içi sıfır olan noktalarda kırılır ve her parça doğrusaldır. Örnek: y = |x − 1| grafiği x = 1’de kırılır')
TAK=B('Koordinat farkı','iki noktanın yatay konum farkı |x₁ − x₂|, düşey konum farkı |y₁ − y₂| ile bulunur. Örnek: (1, 4) ve (6, 2) noktalarında yatay fark 5, düşey fark 2’dir')
HAR=B('Konum–zaman grafiği','konum–zaman grafiğinde doğrunun eğimi hızı verir; iki hareketlinin arasındaki uzaklık, konumların farkının mutlak değeridir. Örnek: 10 dakikada 0’dan 300 m’ye giden birinin hızı 30 m/dk’dır')
SIR=B('Parçaları sıralı değerlendirme','bir koşulu sağlayan parçaların sayısı, koşulun sınırı büyüdükçe artar; bir sayıdan az olmayan ve bir sayıdan çok olmayan koşullarda sınırlar dahildir. Örnek: sapmaları 1, 3, 4 olan parçalarda sınır 3 ise iki parça kabul edilir')

def kk(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)
kk('K-MTB-01','Tabloda uzaklık toplamı','Tablodaki işaretli konumların merkeze uzaklığı mutlak değerle alınır; koşulu sağlayanlar toplanır.','İşaretli değerleri toplamak; eşitliği dahil etmek; yalnız bir yöndekileri saymak.','kolay','tablo',3,'mtb-tablo','Tabloda mutlak değer koşulu')
kk('K-MTB-02','Orta nokta ve uzaklık','İki noktaya eşit uzaklıktaki nokta orta noktadır; sonra üçüncü noktaya uzaklığı bulunur.','İki nokta arası uzaklığı yarılamak; yanlış noktaya uzaklığı almak.','kolay','şekilli',3,'mtb-sayidogru','Sayı doğrusunda uzaklık')
kk('K-MTB-03','Sütun grafiğinde sapma','Grafikten değerler okunup ortalama bulunur; her değerin ortalamadan uzaklığı mutlak değerle alınıp toplanır.','İşaretli sapmaları toplamak; ortalama yerine başka bir ölçü kullanmak.','orta','hikâyeli',4,'mtb-sutun','Sütun grafiğinde sapma')
kk('K-MTB-04','Mutlak değerli eşitlik öncülleri','Noktaların işaretleri sayı doğrusundan okunur; her öncülde mutlak değerlerin içinin işareti belirlenip açılır.','Toplamın mutlak değerini mutlak değerlerin toplamı sanmak; işaret yönünü yanlış okumak.','orta','öncüllü',4,'mtb-oncul','Sayı doğrusunda mutlak değerli öncüller')
kk('K-MTB-05','Mutlak değerli akış şeması','Şemadaki işlemler sırayla birleştirilir; çıkış koşulu mutlak değerli eşitsizliğe çevrilip tam sayılar sayılır.','Negatif kolu unutmak; işlem sırasını karıştırmak; uçları dahil etmek.','orta','yeni nesil',4,'mtb-akis','Akış şemasında mutlak değer')
kk('K-MTB-06','Zıplayış yolu ve uzaklık','Ardışık noktalar arası mesafeler toplanarak toplam yol; baştan sona konum farkı mutlak değerle bulunur.','Toplam yol yerine yer değiştirmeyi yazmak; başlangıç yerine sıfırdan ölçmek.','orta','hikâyeli',4,'mtb-sayidogru','Sayı doğrusunda uzaklık')
kk('K-MTB-07','Düz tabanlı mutlak değer grafiği','Grafiğin kırılma noktalarından a ve b okunur; verilen sınır eşitsizliği üç parçada çözülür.','Kolların eğimini 1 sanmak; uçları yanlış dahil etmek; yalnız bir mutlak değeri kullanmak.','zor','grafik',5,'mtb-grafik','Grafikte mutlak değer')
kk('K-MTB-08','Izgarada taksi uzaklığı','İki koordinat farkının mutlak değerlerinin toplamıyla tanımlı uzaklığa göre kavşaklar sayılır.','Izgara sınırı dışındaki noktaları saymak; “tam” ile “en çok”u karıştırmak.','zor','yeni nesil',5,'mtb-taksi','Izgarada taksi uzaklığı')
kk('K-MTB-09','Sınır değerine göre kabul sayısı','Her parçanın standarttan sapması hesaplanır; kabul sayısı koşuluna göre sınır değerinin aralığı bulunur.','“En az / en çok” sınırlarını karıştırmak; eşitliği dışarıda bırakmak; “tam” sanmak.','zor','hikâyeli',5,'mtb-tablo','Tabloda mutlak değer koşulu')
kk('K-MTB-10','İki hareketli arası uzaklık','Grafikten iki konum ifadesi yazılır; uzaklık koşulu mutlak değerli eşitsizliğe çevrilip iki durumda çözülür.','Mutlak değeri tek durumda çözmek; uçları dahil etmemek; eğimin işaretini karıştırmak.','zor','hikâyeli',5,'mtb-grafik','Grafikte mutlak değer')

# ============ 01 · kolay · atış tablosu ============
atis=[-7,4,-2,9,-5,3]
dog=sum(abs(v) for v in atis if abs(v)>3); assert dog==25
e=[sum(v for v in atis if abs(v)>3),sum(v for v in atis if v>3),sum(abs(v) for v in atis if abs(v)>=3),sum(abs(v) for v in atis)]
assert e==[1,13,28,30] and e[0]==-7+4+9-5
havuz=[(1,'Uzaklık yerine işaretli konumları toplamış: −7 + 4 + 9 − 5 = 1.','islem'),
 (13,'Yalnız merkez çizgisinin sağındaki atışları (4 ve 9) toplamış.','dikkat'),
 (28,'“3 cm’den fazla” koşulunda eşitliği de almış; uzaklığı tam 3 olan atışı da toplamış.','dikkat'),
 (30,'Koşulu hiç uygulamamış; altı atışın uzaklıklarının hepsini toplamış.','dikkat')]
sgn=lambda v:('+' if v>0 else '−')+str(abs(v))
SK=tablo_svg(['Atış','Merkez çizgisine göre konum (cm)'],[[f'{i+1}. atış',sgn(v)] for i,v in enumerate(atis)])
q('0001',tipId='mtb-tablo',tip='Tabloda mutlak değer koşulu',z='kolay',alt='Mutlak Değer Problemleri',kaz='Tablodaki işaretli konumların merkeze uzaklığını mutlak değerle alıp koşulu sağlayanların toplamını bulur.',kalip='hikâyeli',sekil=SK,
 kart='K-MTB-01 · konumlar −7, 4, −2, 9, −5, 3; uzaklığı 3’ten büyük olanların toplamı 25',
 metin='Bir okçuluk antrenmanında hedefin ortasından geçen düşey çizgiye göre altı okun saplandığı yerler aşağıdaki tabloda verilmiştir; çizginin sağı + işaretiyle, solu − işaretiyle gösterilmiştir. Bir okun merkez çizgisine olan uzaklığı, konumunun mutlak değeridir. Antrenör, merkez çizgisine uzaklığı 3 cm’den fazla olan okları “hatalı atış” saymaktadır.\nBuna göre hatalı atışların merkez çizgisine olan uzaklıklarının toplamı kaç cm’dir?',
 dogru=dog,yan=hata(dog,havuz,'C'),istenen='Hatalı atışların uzaklıkları toplamı (cm).',
 ip=['Her okun merkez çizgisine uzaklığını işaretsiz bir sayı olarak yaz, sonra hangilerinin koşulu sağladığına bak.'],bilgi=[MUT],
 ad=[A('Uzaklıkları yaz','Mutlak değer işareti kaldırır.','7, 4, 2, 9, 5, 3 cm'),A('Hatalı atışlar','Uzaklığı 3’ten fazla olanlar (3 dahil değil).','7, 4, 9, 5'),A('Topla','Hatalı atışların uzaklıkları toplanır.','7 + 4 + 9 + 5 = 25')],
 puf='Hangi atışların koşulu sağladığını işaretleyip yalnız onların uzaklıklarını topla.')

# ============ 02 · kolay · orta nokta ============
A2,B2,C2=-10,6,-4; M2=Fr(A2+B2,2); dog=abs(M2-C2)
assert M2==-2 and dog==2 and abs(A2-C2)==6 and abs(B2-C2)==10 and abs(A2-B2)==16 and Fr(abs(A2-B2),2)==8 and abs(M2-A2)==abs(M2-B2)==8
havuz=[(6,'M yerine A noktasına olan uzaklığı almış: |−10 − (−4)| = 6.','dikkat'),
 (8,'A ile B arasındaki uzaklığın yarısını (M’nin A’ya uzaklığı) bulup C’ye olan uzaklığı hesaplamamış.','dikkat'),
 (10,'M yerine B noktasına olan uzaklığı almış: |6 − (−4)| = 10.','dikkat'),
 (16,'M yerine A ile B arasındaki uzaklığı (16) yazmış.','dikkat')]
s=.34; g=sayidog(-12,8,s,0,2,'\\footnotesize')
for nm,v in (('A',A2),('B',B2),('C',C2)): g+=f'\\fill[vurgu] ({v*s:.2f},0) circle (.11);\\node[above=5pt,font=\\normalsize] at ({v*s:.2f},0) {{{nm}}};'
q('0002',tipId='mtb-sayidogru',tip='Sayı doğrusunda uzaklık',z='kolay',alt='Mutlak Değer ve Uzaklık',kaz='Sayı doğrusunda iki noktaya eşit uzaklıktaki noktayı bulup üçüncü noktaya uzaklığını mutlak değerle hesaplar.',kalip='şekilli',sekil=TP(g),
 kart='K-MTB-02 · A = −10, B = 6, C = −4; M orta nokta, |MC| = 2',
 metin='Şekildeki sayı doğrusunda A, B ve C noktalarının yerleri gösterilmiştir. Sayı doğrusu üzerindeki M noktası, A ve B noktalarına eşit uzaklıktadır.\nBuna göre M noktasının C noktasına olan uzaklığı kaç birimdir?',
 dogru=dog,yan=hata(dog,havuz,'A'),istenen='M ile C arasındaki uzaklık (birim).',
 ip=['Önce A ve B noktalarının yerlerini oku; M noktasının sayı doğrusunda nerede olduğunu bul.'],bilgi=[UZ,ORT],
 ad=[A('Noktaları oku','Şekilden A, B ve C’nin yerleri.','A = −10 · B = 6 · C = −4'),A('M noktası','A ve B’ye eşit uzaklıkta olan nokta.','(−10 + 6) ÷ 2 = −2'),A('M ile C arasındaki uzaklık','Fark mutlak değerle alınır.','|−2 − (−4)| = 2')],
 puf='İki nokta arasındaki uzaklığı her zaman büyük sayıdan küçüğü çıkararak ya da mutlak değerle bul; sonuç pozitif olur.')

# ============ 03 · orta · sütun grafiği sapma ============
gun=['Pzt','Sal','Çar','Per','Cum']; v3=[15,40,25,45,25]
ort=Fr(sum(v3),5); dog=sum(abs(v-ort) for v in v3)
med=sorted(v3)[2]
assert ort==30 and dog==50 and med==25 and sum(v-ort for v in v3)==0 and sum(v-ort for v in v3 if v>ort)==25 and sum(abs(v-med) for v in v3)==45 and max(abs(v-ort) for v in v3)==15
havuz=[(0,'Sapmaları işaretli toplamış: (15 − 30) + (40 − 30) + … = 0.','dikkat'),
 (15,'Toplam yerine en büyük sapmayı (|15 − 30| = 15) yazmış.','dikkat'),
 (25,'Yalnız ortalamadan büyük olan günlerin sapmalarını toplamış: 10 + 15 + … = 25; küçük olanların sapmalarını eklememiş.','dikkat'),
 (45,'Ortalama yerine ortancayı (25) kullanmış: 10 + 15 + 0 + 20 + 0 = 45.','dikkat')]
sy=.062; sx=.9; g=''
for y in range(0,51,5): g+=f'\\draw[gray!{45 if y%10==0 else 25}] (0,{y*sy:.3f}) -- ({5*sx+.3:.2f},{y*sy:.3f});'+(f'\\node[left=2pt,font=\\footnotesize] at (0,{y*sy:.3f}) {{${y}$}};' if y%10==0 else '')
for i,(gn,v) in enumerate(zip(gun,v3)):
    x=.3+i*sx; g+=f'\\filldraw[fill=vurgu!45,draw=vurgu!80!black] ({x:.2f},0) rectangle ({x+.55:.2f},{v*sy:.3f});\\node[below=2pt,font=\\footnotesize] at ({x+.275:.2f},0) {{{gn}}};'
g+=f'\\draw[thick,-{{Stealth}}] (0,0) -- ({5*sx+.6:.2f},0);\\draw[thick,-{{Stealth}}] (0,0) -- (0,{54*sy:.2f});\\node[font=\\footnotesize,anchor=south] at (1.1,{54*sy:.2f}) {{satılan pasta (adet)}};'
q('0003',tipId='mtb-sutun',tip='Sütun grafiğinde sapma',z='orta',alt='Mutlak Değer Problemleri',kaz='Sütun grafiğinden değerleri okuyup ortalamayı bulur ve her değerin ortalamadan sapmasını mutlak değerle alıp toplar.',kalip='hikâyeli',sekil=TP(g),
 kart='K-MTB-03 · 15, 40, 25, 45, 25; ortalama 30, sapma toplamı 50',
 metin='Bir pastanenin hafta içi beş gün boyunca sattığı pasta sayıları şekildeki sütun grafiğinde verilmiştir. Bir günün “sapması”, o günkü satış sayısı ile bu beş günün satış ortalaması arasındaki farkın mutlak değeridir.\nBuna göre beş günün sapmalarının toplamı kaçtır?',
 dogru=dog,yan=hata(dog,havuz,'E'),istenen='Beş günün sapmalarının toplamı.',
 ip=['Sütunların yüksekliklerini oku; sapmaları bulabilmek için önce hangi değere ihtiyacın olduğunu düşün.'],bilgi=[SAP,MUT],
 ad=[A('Değerleri oku','Sütun yükseklikleri.','15, 40, 25, 45, 25'),A('Ortalama','Toplam ÷ gün sayısı.','150 ÷ 5 = 30'),A('Sapmalar','Her değerin ortalamadan farkının mutlak değeri.','15, 10, 5, 15, 5'),A('Topla','Sapmalar toplanır.','15 + 10 + 5 + 15 + 5 = 50')],
 puf='Sapmaları toplamadan önce her birinin işaretsiz olduğundan emin ol.')

# ============ 04 · orta · öncüllü ============
a4,b4,c4=-5,2,4
I=lambda:abs(a4-c4)==abs(a4)+abs(c4); II=lambda:abs(a4+b4)==abs(a4)+abs(b4); III=lambda:abs(b4-c4)==abs(c4)-abs(b4)
assert (I(),II(),III())==(True,False,True)
sira=['Yalnız I','Yalnız III','I ve II','I ve III','II ve III']
# hata zincirleri (her biri bir kural yanlışından hesaplanır)
A_=lambda x,y:abs(x)+abs(y)     # |x±y| = |x|+|y| her zaman
zinc1=(abs(a4-c4)==A_(a4,c4), abs(a4+b4)==A_(a4,b4), abs(b4-c4)==abs(c4)-abs(b4))   # III’ü yanlış sanmış: |b−c| = |b|+|c|
assert abs(b4-c4)!=A_(b4,c4)
s4=.42; g=sayidog(-7,6,s4,0,99)
g+=f'\\node[below=3pt,font=\\footnotesize] at (0,-.08) {{$0$}};'
for nm,v in (('a',a4),('b',b4),('c',c4)): g+=f'\\fill[vurgu] ({v*s4:.2f},0) circle (.11);\\node[above=5pt,font=\\normalsize] at ({v*s4:.2f},0) {{${nm}$}};'
q('0004',tipId='mtb-oncul',tip='Sayı doğrusunda mutlak değerli öncüller',z='orta',alt='Mutlak Değer ve Uzaklık',kaz='Sayı doğrusunda yerleri verilen sayılar için mutlak değerli eşitliklerin doğruluğunu işaretlere bakarak sınar.',kalip='öncüllü',sekil=TP(g),
 kart='K-MTB-04 · a = −5, b = 2, c = 4; I ve III doğru',
 metin='Şekildeki sayı doğrusunda a, b ve c sayılarının yerleri gösterilmiştir; komşu iki işaret arası 1 birimdir.\nBuna göre,\nI. |a − c| = |a| + |c|\nII. |a + b| = |a| + |b|\nIII. |b − c| = |c| − |b|\neşitliklerinden hangileri doğrudur?',
 dogru='I ve III',sira=sira,
 yan=[('Yalnız I','III’ü yanlış sanmış: |b − c| = |b| + |c| = 6 diye düşünüp 2 ile karşılaştırmış; I’i doğru, II’yi yanlış bulmuş.','bilgi'),
      ('Yalnız III','I’i yanlış sanmış: |a − c| = 9 iken |a| − |c| = 1 gibi hesaplayıp karşılaştırmış; II’yi yanlış, III’ü doğru bulmuş.','islem'),
      ('I ve II','“Toplamın ya da farkın mutlak değeri, mutlak değerlerin toplamıdır” kuralını her durumda uygulamış: I ve II doğru, III yanlış çıkmıştır.','bilgi'),
      ('II ve III','Toplamın mutlak değerini mutlak değerlerin toplamı sanmış (II doğru); farkta ise mutlak değerlerin farkını almış (|a − c| = 1 diye I yanlış, III doğru).','bilgi')],
 istenen='Doğru olan eşitlikler.',
 ip=['Sayı doğrusundan a, b ve c’nin işaretlerini ve birbirlerine göre yerlerini belirle; her eşitliği ayrı ayrı sına.'],bilgi=[MUT,OZ],
 ad=[A('Yerleri oku','Şekilden sayıların değerleri.','a = −5 · b = 2 · c = 4'),A('I’i sına','İki yan ayrı ayrı hesaplanır.','|−5 − 4| = 9 · |−5| + |4| = 9 → doğru'),A('II’yi sına','İki yan ayrı ayrı hesaplanır.','|−5 + 2| = 3 · |−5| + |2| = 7 → yanlış'),A('III’ü sına','İki yan ayrı ayrı hesaplanır.','|2 − 4| = 2 · |4| − |2| = 2 → doğru')],
 puf='Her öncülde iki yanı ayrı ayrı sayıya çevirip karşılaştır; kural ezberi yerine değeri hesapla.')

# ============ 05 · orta · mutlak değerli akış şeması ============
f5=lambda x:3*abs(x-4)+5
S=tara(lambda x:f5(x)<41,-100,100); dog=len(S); assert S==list(range(-7,16)) and dog==23
e_inc=len(tara(lambda x:f5(x)<=41,-100,100)); assert e_inc==25
e_poz=len(tara(lambda x:x-4>=0 and 3*(x-4)+5<41,-100,100)); assert e_poz==12
e_5=len(tara(lambda x:3*abs(x-4)<41,-100,100)); assert e_5==27
e_c=len(tara(lambda x:abs(x-4)+5<41,-100,100)); assert e_c==71
e_sira=len(tara(lambda x:3*(abs(x-4)+5)<41,-100,100)); assert e_sira==17
havuz=[(12,'Mutlak değerin içinin negatif olduğu durumu (x < 4) hiç düşünmemiş; yalnız 4 ≤ x < 16 için 12 değer saymış.','dikkat'),
 (17,'“3 ile çarp” ve “5 ekle” işlemlerinin sırasını karıştırmış (3(|x − 4| + 5) < 41); −4’ten 12’ye 17 değer saymış.','dikkat'),
 (25,'Çıkışın 41’e eşit olmasına da izin vermiş (≤); x = −8 ve x = 16 de çözüme girmiş: −8’den 16’ya 25 değer.','dikkat'),
 (27,'“5 ekle” işlemini hesaba katmamış: 3|x − 4| < 41 → |x − 4| < 13,67; −9’dan 17’ye 27 değer saymış.','dikkat'),
 (71,'“3 ile çarp” işlemini hesaba katmamış: |x − 4| + 5 < 41 → |x − 4| < 36; −31’den 39’a 71 değer saymış.','dikkat')]
bx=lambda x,y,txt,w=2.7,h=1.2: f'\\node[draw,thick,rounded corners=3pt,fill=vurgu!12,minimum width={w}cm,minimum height={h}cm,align=center,inner sep=3pt] at ({x},{y}) {{{txt}}};'
g=bx(0,0,'Girdi\\\\$x$',1.7)+bx(3.4,0,'4 çıkar',2.5)+bx(6.9,0,'Mutlak değerini\\\\al',2.9)+bx(6.9,-2.0,'3 ile çarp',2.9)+bx(3.4,-2.0,'5 ekle',2.5)+bx(0,-2.0,'Çıkış',1.7)
g+='\\draw[-{Stealth},thick] (.85,0) -- (2.15,0);\\draw[-{Stealth},thick] (4.65,0) -- (5.45,0);\\draw[-{Stealth},thick] (6.9,-.6) -- (6.9,-1.4);\\draw[-{Stealth},thick] (5.45,-2.0) -- (4.65,-2.0);\\draw[-{Stealth},thick] (2.15,-2.0) -- (.85,-2.0);'
q('0005',tipId='mtb-akis',tip='Akış şemasında mutlak değer',z='orta',alt='Mutlak Değerli Eşitsizlikler',kaz='Mutlak değer kutusu içeren işlem şemasında çıkış koşulunu x cinsinden mutlak değerli eşitsizliğe çevirip tam sayıları sayar.',kalip='yeni nesil',sekil=TP(g),
 kart='K-MTB-05 · 3|x − 4| + 5 < 41 → x = −7, …, 15',
 metin='Şekildeki işlem şemasında, girdi olarak verilen x tam sayısına kutulardaki işlemler okların yönünde sırayla uygulanır ve sonuç çıkışta yazılır. “Mutlak değerini al” kutusu, kendisine gelen sayının mutlak değerini çıkarır.\nÇıkışta yazan sayı 41’den küçük olduğuna göre x kaç farklı tam sayı değeri alabilir?',
 dogru=dog,yan=hata(dog,havuz,'B'),istenen='x’in alabileceği tam sayı değerlerinin sayısı.',
 ip=['Şemadaki kutuların sırasını izleyerek x’ten çıkışa giden tek bir ifade yaz.'],bilgi=[ISL,ARL],
 ad=[A('Çıkışı x cinsinden yaz','Kutular sırayla uygulanır.','3 · |x − 4| + 5'),A('Eşitsizliği kur','Çıkış 41’den küçük.','3|x − 4| + 5 < 41 → |x − 4| < 12'),A('x için çöz','Uzaklık iki yöne de gidebilir; uçlar dahil değil.','−12 < x − 4 < 12 → −8 < x < 16'),A('Say','Uçlar dışarıda kalan tam sayılar.','−7’den 15’e → 15 − (−7) + 1 = 23')],
 puf='Mutlak değerli bir eşitsizlikte sınır, iki yöne de uygulanır; çözüm kümesi tek parçalı bir aralık olabilir.')

# ============ 06 · orta · kurbağa ============
pos=[-3,5,-6,-1,-10]
yol=sum(abs(pos[i+1]-pos[i]) for i in range(4)); yer=abs(pos[-1]-pos[0]); dog=yol-yer
assert yol==33 and yer==7 and dog==26 and yol+yer==40 and yol-abs(pos[-1])==23
havuz=[(7,'Toplam yol yerine son noktanın başlangıç noktasına uzaklığını (|−10 − (−3)| = 7) yazmış.','dikkat'),
 (23,'Son noktanın sayı doğrusundaki 0’a uzaklığını (10) hesaplayıp toplam yoldan çıkarmış: 33 − 10.','dikkat'),
 (33,'Fark yerine toplam yolu yazmış; yer değiştirmeyi çıkarmamış.','dikkat'),
 (40,'Yer değiştirmeyi toplam yoldan çıkarmak yerine toplamış: 33 + 7.','islem')]
s=.52; g=sayidog(-11,6,s,0,1)
lv=lambda i:.6*i
for i in range(5):
    top=lv(max(i,1)) if i<4 else lv(4)
    hi=max([lv(j) for j in range(1,5) if j==i or j==i+1] or [0])
    g+=f'\\draw[dotted,gray] ({pos[i]*s:.2f},.25) -- ({pos[i]*s:.2f},{hi:.2f});'
for i in range(1,5):
    g+=f'\\draw[-{{Stealth}},thick,vurgu!80!black] ({pos[i-1]*s:.2f},{lv(i):.2f}) -- ({pos[i]*s:.2f},{lv(i):.2f});'
for i in range(5): g+=f'\\node[circle,draw,fill=white,inner sep=0pt,font=\\footnotesize,minimum size=.5cm] at ({pos[i]*s:.2f},0) {{{'KLMNP'[i]}}};'
g+=f'\\node[font=\\footnotesize,anchor=north] at ({pos[0]*s:.2f},-.8) {{K: başlangıç}};'
q('0006',tipId='mtb-sayidogru',tip='Sayı doğrusunda uzaklık',z='orta',alt='Mutlak Değer ve Uzaklık',kaz='Sayı doğrusunda ardışık zıplayışların uzunluklarını mutlak değerle toplayıp toplam yol ile yer değiştirme arasındaki farkı bulur.',kalip='hikâyeli',sekil=TP(g),
 kart='K-MTB-06 · −3 → 5 → −6 → −1 → −10; yol 33, yer değiştirme 7',
 metin='Bir kurbağa, şekildeki sayı doğrusunda K noktasından başlayıp oklarla gösterilen yolu izleyerek sırasıyla L, M, N ve P noktalarına zıplamıştır; her zıplayışta iki nokta arasındaki yolu doğrudan almıştır. Kurbağanın aldığı toplam yol, zıplayışların uzunluklarının toplamıdır.\nBuna göre kurbağanın aldığı toplam yol ile P noktasının K noktasına olan uzaklığı arasındaki fark kaç birimdir?',
 dogru=dog,yan=hata(dog,havuz,'C'),istenen='Toplam yol ile baştan sona uzaklık arasındaki fark (birim).',
 ip=['K, L, M, N ve P noktalarının yerlerini sayı doğrusundan oku; her zıplayışın uzunluğunu ayrı ayrı bul.'],bilgi=[UZ],
 ad=[A('Noktaları oku','Harfli noktaların yerleri.','K: −3 · L: 5 · M: −6 · N: −1 · P: −10'),A('Zıplayış uzunlukları','Ardışık noktalar arası uzaklıklar.','8, 11, 5, 9'),A('Toplam yol','Uzunluklar toplanır.','8 + 11 + 5 + 9 = 33'),A('Baştan sona uzaklık','K ve P noktaları arası.','|−10 − (−3)| = 7'),A('Fark','Toplam yoldan çıkarılır.','33 − 7 = 26')],
 puf='Toplam yol, her parçanın uzunluğunun toplamıdır; baştan sona uzaklık ise yalnız iki uç noktaya bağlıdır.')

# ============ 07 · zor · düz tabanlı mutlak değer grafiği ============
a7,b7=-3,5   # f(x)=|x-a7|+|x-b7|  (kırılmalar -3 ve 5)
f7=lambda x:abs(x-a7)+abs(x-b7)
assert f7(-3)==f7(5)==8 and f7(-7)==16 and f7(9)==16 and all(f7(x)==8 for x in range(-3,6))
g7=lambda x:f7(2*x)
S=tara(lambda x:g7(x)<=14,-100,100); dog=len(S); assert S==list(range(-3,5)) and dog==8
e_k=len(tara(lambda x:g7(x)<14,-100,100)); assert e_k==6
e_egim=len(tara(lambda x:-9<=2*x<=11,-100,100)); assert e_egim==10
e_tek=len(tara(lambda x:abs(2*x-a7)<=14,-100,100)); assert e_tek==14
e_2x=len(tara(lambda x:f7(x)<=14,-100,100)); assert e_2x==15
havuz=[(6,'Eşitsizliği “<” gibi çözüp 14’e eşit olan uçları (2x = −6 ve 2x = 8) dışarıda bırakmış: −2’den 3’e 6 değer.','dikkat'),
 (10,'Kolların eğimini 1 sanmış: kırılma noktalarından 6 birim uzağa gidip −9 ≤ 2x ≤ 11 bulmuş (kollar 2 eğimlidir): −4’ten 5’e 10 değer.','dikkat'),
 (14,'Yalnız |2x + 3| terimini kullanmış: |2x + 3| ≤ 14 → −8’den 5’e 14 değer.','dikkat'),
 (15,'Girdiyi 2x yerine x almış: f(x) ≤ 14 → −6 ≤ x ≤ 8 için 15 değer saymış.','islem')]
s=.5; X0,X1,Y0,Y1=-7,9,0,16; sy=.2
g=''.join(f'\\draw[gray!{45 if i%2==0 else 28}] ({i*s:.2f},0) -- ({i*s:.2f},{Y1*sy:.2f});' for i in range(X0,X1+1))
g+=''.join(f'\\draw[gray!45] ({X0*s:.2f},{j*sy:.2f}) -- ({X1*s:.2f},{j*sy:.2f});' for j in range(Y0,Y1+1,2))
g+=f'\\draw[thick] ({X0*s:.2f},0) rectangle ({X1*s:.2f},{Y1*sy:.2f});'
g+=f'\\draw[very thick] (0,0) -- (0,{Y1*sy:.2f});\\draw[very thick] ({X0*s:.2f},0) -- ({X1*s:.2f},0);'
g+=''.join(f'\\node[below=2pt,font=\\scriptsize] at ({i*s:.2f},0) {{${i}$}};' for i in range(X0,X1+1))
g+=''.join(f'\\node[left=2pt,font=\\scriptsize] at ({X0*s:.2f},{j*sy:.2f}) {{${j}$}};' for j in range(Y0+2,Y1+1,2))
g+=f'\\draw[very thick,vurgu] ({X0*s:.2f},{f7(X0)*sy:.2f}) -- ({a7*s:.2f},{f7(a7)*sy:.2f}) -- ({b7*s:.2f},{f7(b7)*sy:.2f}) -- ({X1*s:.2f},{f7(X1)*sy:.2f});'
g+=f'\\node[font=\\small,anchor=south] at (0,{(Y1+.1)*sy:.2f}) {{$y$}};\\node[font=\\small,anchor=west] at ({(X1+.2)*s:.2f},0) {{$x$}};'
q('0007',tipId='mtb-grafik',tip='Grafikte mutlak değer',z='zor',alt='Mutlak Değer Grafiği',kaz='İki mutlak değer içeren fonksiyonun grafiğinden kırılma noktalarını okuyup verilen sınır eşitsizliğini sağlayan tam sayıları sayar.',kalip='grafik',sekil=TP(g),
 kart='K-MTB-07 · f(2x) = |2x + 3| + |2x − 5| ≤ 14 → x = −3, …, 4',
 metin='Şekilde, a < b olmak üzere a ve b gerçel sayıları için f(x) = |x − a| + |x − b| fonksiyonunun grafiği verilmiştir. Grafik, ızgaranın kare köşelerinde kırılmaktadır.\nBuna göre f(2x) ≤ 14 eşitsizliğini sağlayan kaç farklı x tam sayısı vardır?',
 dogru=dog,yan=hata(dog,havuz,'B'),istenen='f(2x) ≤ 14 eşitsizliğini sağlayan tam sayıların sayısı.',
 ip=['Grafiğin kırılma noktalarının yatay konumlarını oku; bunlar a ve b hakkında ne söylüyor?'],bilgi=[GRF,ARL],
 ad=[A('a ve b’yi oku','Grafik, mutlak değerlerin içi sıfır olan noktalarda kırılır.','a = −3 · b = 5'),A('Fonksiyonu yaz','Okunan değerler yerine konur; girdi 2x’tir.','f(2x) = |2x + 3| + |2x − 5|'),A('y = 2x için çöz','Orta bölgede f sabit 8’dir; dış kollarda f, y’ye göre 2 eğimle artar.','y ≤ −3 için 2 − 2y ≤ 14 → y ≥ −6 · y ≥ 5 için 2y − 2 ≤ 14 → y ≤ 8'),A('x’e dön ve say','−6 ≤ 2x ≤ 8; −3 ≤ y ≤ 5 bölgesinde f = 8 ≤ 14 olduğundan hepsi çözümdür.','−3 ≤ x ≤ 4 → 4 − (−3) + 1 = 8')],
 puf='Mutlak değerli fonksiyonun grafiğinde her kırılma noktasından sonra eğim değişir; sınırı kollarda kırılma noktasından itibaren değerlendir.')

# ============ 08 · zor · ızgarada taksi uzaklığı ============
W,Hh=8,6; A8,B8=(2,3),(5,5)
d=lambda p,q_:abs(p[0]-q_[0])+abs(p[1]-q_[1])
pts=[(x,y) for x in range(W+1) for y in range(Hh+1)]
big=[(x,y) for x in range(-15,24) for y in range(-15,22)]
sol=[p for p in pts if d(p,A8)==4 and d(p,B8)<=5]; dog=len(sol); assert dog==8
e_le=len([p for p in pts if d(p,A8)<=4 and d(p,B8)<=5]); assert e_le==22
e_ng=len([p for p in big if d(p,A8)==4 and d(p,B8)<=5]); assert e_ng==9
e_oA=len([p for p in pts if d(p,A8)==4]); assert e_oA==11
e_oB=len([p for p in pts if d(p,B8)<=5]); assert e_oB==41
havuz=[(9,'Izgaranın dışına taşan (2, 7) noktasını da saymış; kavşaklar y = 6’da biter.','dikkat'),
 (11,'B’ye uzaklık koşulunu uygulamamış; A’ya uzaklığı tam 4 olan bütün kavşakları saymış.','dikkat'),
 (22,'“A’ya uzaklığı tam 4” yerine “en çok 4” koşulunu almış.','dikkat'),
 (41,'A’ya uzaklık koşulunu uygulamamış; B’ye uzaklığı en çok 5 olan bütün kavşakları saymış.','dikkat')]
s=.5; g=''
for i in range(W+1): g+=f'\\draw[gray!55] ({i*s:.2f},0) -- ({i*s:.2f},{Hh*s:.2f});\\node[below=3pt,font=\\footnotesize] at ({i*s:.2f},0) {{${i}$}};'
for j in range(Hh+1): g+=f'\\draw[gray!55] (0,{j*s:.2f}) -- ({W*s:.2f},{j*s:.2f});\\node[left=3pt,font=\\footnotesize] at (0,{j*s:.2f}) {{${j}$}};'
for (x,y) in pts: g+=f'\\fill[gray!70] ({x*s:.2f},{y*s:.2f}) circle (.045);'
for nm,(x,y) in (('A',A8),('B',B8)): g+=f'\\filldraw[fill=vurgu,draw=vurgu!60!black] ({x*s:.2f},{y*s:.2f}) circle (.12);\\node[font=\\normalsize\\bfseries,anchor=south west] at ({x*s+.1:.2f},{y*s+.08:.2f}) {{{nm}}};'
q('0008',tipId='mtb-taksi',tip='Izgarada taksi uzaklığı',z='zor',alt='Mutlak Değer ve Uzaklık',kaz='Koordinat farklarının mutlak değerleri toplamıyla tanımlı uzaklığa göre ızgara noktalarını iki koşulla sayar.',kalip='yeni nesil',sekil=TP(g),
 kart='K-MTB-08 · A = (2, 3), B = (5, 5); d(P, A) = 4 ve d(P, B) ≤ 5 → 8 kavşak',
 metin='Bir şehrin sokakları şekildeki gibi birbirine dik ve eşit aralıklıdır; noktalar kavşakları göstermektedir. P(x₁, y₁) ve Q(x₂, y₂) kavşakları arasındaki yürüme uzaklığı d(P, Q) = |x₁ − x₂| + |y₁ − y₂| blok olarak tanımlanmıştır. Bir kafe, A kavşağına yürüme uzaklığı tam 4 blok ve B kavşağına yürüme uzaklığı en çok 5 blok olan bir kavşağa açılacaktır.\nBuna göre kafe, şekildeki kavşaklardan kaç farklı tanesine açılabilir?',
 dogru=dog,yan=hata(dog,havuz,'A'),istenen='Kafenin açılabileceği kavşak sayısı.',
 ip=['A ve B kavşaklarının koordinatlarını şekilden oku; her koşulu bir kavşağın koordinatları için yaz.'],bilgi=[TAK,MUT],
 ad=[A('Koordinatları oku','Şekilden A ve B kavşaklarının koordinatları.','A = (2, 3) · B = (5, 5)'),A('A koşulu','Tam 4 blok uzaklıktaki kavşaklar.','|x − 2| + |y − 3| = 4'),A('B koşulu','En çok 5 blok uzaklıktaki kavşaklar.','|x − 5| + |y − 5| ≤ 5'),A('Izgarada tara','0 ≤ x ≤ 8, 0 ≤ y ≤ 6 olan kavşaklarda iki koşulu sınar.','A koşulunu sağlayan 11 kavşaktan B koşulunu da sağlayanlar'),A('Say','İki koşulu birlikte sağlayan kavşaklar.','8 kavşak')],
 puf='Izgaranın sınırlarını da koşul say: tanımlı uzaklıkla bulunan her nokta şekilde bulunmayabilir.')

# ============ 09 · zor · parça tablosu ============
nom=120; olc=[121,108,125,118,131,122,112]
dev=sorted(abs(v-nom) for v in olc); assert dev==[1,2,2,5,8,11,12]
cnt=lambda k:sum(abs(v-nom)<=k for v in olc)
S=tara(lambda k:k>=1 and 4<=cnt(k)<=5,1,60); dog=len(S); assert S==list(range(5,11)) and dog==6
e_tam=len(tara(lambda k:k>=1 and cnt(k)==5,1,60)); assert e_tam==3 and len(tara(lambda k:k>=1 and cnt(k)==4,1,60))==3
e_8=len(tara(lambda k:k>=1 and cnt(k)>=4 and k<=8,1,60)); assert e_8==4
e_6=len(tara(lambda k:k>=1 and k>5 and cnt(k)<=5,1,60)); assert e_6==5
e_11=len(tara(lambda k:k>=1 and cnt(k)>=4 and k<=11,1,60)); assert e_11==7
havuz=[(3,'“En az 4 ve en çok 5 parça” koşulunu “tam 5 parça” diye okumuş; k = 8, 9, 10 değerlerini bulmuş.','dikkat'),
 (4,'Üst sınır için beşinci en küçük sapmayı (8) alıp k ≤ 8 demiş; k = 9 ve k = 10 değerlerini unutmuş: 5, 6, 7, 8.','dikkat'),
 (5,'Alt sınırda eşitliği dışarıda bırakmış (k > 5); 4. parça k = 5’te de kabul edilir: 6’dan 10’a 5 değer.','dikkat'),
 (7,'Üst sınırı altıncı en küçük sapmaya (11) kadar uzatmış; k = 11’de 6 parça kabul edilir: 5’ten 11’e 7 değer.','dikkat')]
SK=tablo_svg(['Parça','Ölçülen uzunluk (mm)'],[[f'P{i+1}',str(v)] for i,v in enumerate(olc)])
q('0009',tipId='mtb-tablo',tip='Tabloda mutlak değer koşulu',z='zor',alt='Mutlak Değerli Eşitsizlikler',kaz='Tablodaki parçaların standarttan sapmasını mutlak değerle bulup, kabul edilen parça sayısına koşul koyan sınır değerinin tam sayı değerlerini sayar.',kalip='hikâyeli',sekil=SK,
 kart='K-MTB-09 · standart 120 mm; sapmalar 1, 2, 2, 5, 8, 11, 12; kabul 4–5 parça → k = 5, …, 10',
 metin='Bir fabrikada üretilen 7 parçanın ölçülen uzunlukları aşağıdaki tabloda verilmiştir. Parçaların standart uzunluğu 120 mm’dir. Ölçülen uzunluğunun standarttan farkının mutlak değeri k mm’yi geçmeyen (k mm dahil) parçalar kabul edilmektedir; k pozitif bir tam sayıdır. Kalite şefi, kabul edilen parça sayısının en az 4, en çok 5 olmasını istemektedir.\nBuna göre k kaç farklı tam sayı değeri alabilir?',
 dogru=dog,yan=hata(dog,havuz,'D'),istenen='k’nin alabileceği tam sayı değerlerinin sayısı.',
 ip=['Her parçanın standarttan ne kadar saptığını işaretsiz olarak yaz; k büyüdükçe kabul edilen parça sayısının nasıl değiştiğini düşün.'],bilgi=[MUT,SIR],
 ad=[A('Sapmaları yaz','Her ölçünün 120’den farkının mutlak değeri.','1, 12, 5, 2, 11, 2, 8'),A('Küçükten büyüğe sırala','Kabul sayısı bu sıraya göre artar.','1, 2, 2, 5, 8, 11, 12'),A('En az 4 parça','Dördüncü en küçük sapma 5.','k ≥ 5'),A('En çok 5 parça','Altıncı parça (11) kabul edilmemeli.','k < 11 → k ≤ 10'),A('Say','5 ≤ k ≤ 10 tam sayıları.','10 − 5 + 1 = 6')],
 puf='“En az” ve “en çok” sınırlarını ayrı ayrı bulup birleştir; sınır değerlerde kabul sayısının nasıl değiştiğini tek tek kontrol et.')

# ============ 10 · zor · konum–zaman grafiği ============
SA=lambda t:80*t; SB=lambda t:840-60*t
assert SA(10)==800 and SB(10)==240 and SA(0)==0 and SB(0)==840 and SA(12)==960 and SB(12)==120
dif=lambda t:abs(SA(t)-SB(t))
S=tara(lambda t:0<=t<=12 and dif(t)<=280,0,12); dog=sum(S); assert S==[4,5,6,7,8] and dog==30
e_k=sum(tara(lambda t:0<=t<=12 and dif(t)<280,0,12)); assert e_k==18
e_k1=sum(tara(lambda t:0<=t<=12 and dif(t)<280 or t==4,0,12)); assert e_k1==22
e_k2=sum(tara(lambda t:0<=t<=12 and dif(t)<280 or t==8,0,12)); assert e_k2==26
e_poz=sum(tara(lambda t:0<=t<=12 and 0<=SA(t)-SB(t)<=280,0,12)); assert e_poz==21
e_neg=sum(tara(lambda t:0<=t<=12 and 0<=SB(t)-SA(t)<=280,0,12)); assert e_neg==15
havuz=[(15,'Mutlak değeri yalnız B’nin önde olduğu durum için çözmüş (840 − 140t ≤ 280 ve t ≤ 6): 4 + 5 + 6.','dikkat'),
 (18,'“280 m’yi geçmediğinde” koşulunda eşitliği dışarıda bırakmış; t = 4 ve t = 8’de uzaklık tam 280 m olduğundan bunları almamış: 5 + 6 + 7.','dikkat'),
 (21,'Mutlak değeri yalnız A’nın önde olduğu durum için çözmüş (140t − 840 ≤ 280 ve t ≥ 6): 6 + 7 + 8.','dikkat'),
 (22,'Yalnız üst sınırdaki eşitliği (t = 8) dışarıda bırakmış: 4 + 5 + 6 + 7.','dikkat'),
 (26,'Yalnız alt sınırdaki eşitliği (t = 4) dışarıda bırakmış: 5 + 6 + 7 + 8.','dikkat')]
sx,sy=.30,.0034; g=''
for t in range(0,13): g+=f'\\draw[gray!{45 if t%2==0 else 28}] ({t*sx:.2f},0) -- ({t*sx:.2f},{1000*sy:.2f});'+(f'\\node[below=2pt,font=\\footnotesize] at ({t*sx:.2f},0) {{${t}$}};' if t%2==0 else '')
for y in range(0,1001,100): g+=f'\\draw[gray!{45 if y%200==0 else 28}] (0,{y*sy:.3f}) -- ({12*sx:.2f},{y*sy:.3f});'+(f'\\node[left=2pt,font=\\footnotesize] at (0,{y*sy:.3f}) {{${y}$}};' if y%200==0 else '')
g+=f'\\draw[thick,-{{Stealth}}] (0,0) -- ({12.9*sx:.2f},0);\\draw[thick,-{{Stealth}}] (0,0) -- (0,{1060*sy:.2f});'
g+=f'\\node[font=\\footnotesize,anchor=west] at ({12.9*sx:.2f},0) {{dakika}};\\node[font=\\footnotesize,anchor=south west] at (.1,{1060*sy:.2f}) {{konum (m)}};'
for nm,F_ in (('A',SA),('B',SB)):
    g+=f'\\draw[very thick,vurgu] (0,{F_(0)*sy:.3f}) -- ({12*sx:.2f},{F_(12)*sy:.3f});\\node[font=\\small\\bfseries,anchor=west] at ({12*sx+.08:.2f},{F_(12)*sy:.3f}) {{{nm}}};'
    for tt in (0,10): g+=f'\\fill[vurgu!70!black] ({tt*sx:.2f},{F_(tt)*sy:.3f}) circle (.09);'
q('0010',tipId='mtb-grafik',tip='Grafikte mutlak değer',z='zor',alt='Mutlak Değer ve Uzaklık',kaz='Konum–zaman grafiğinden iki hareketlinin konum ifadelerini yazıp aralarındaki uzaklığın sınırını mutlak değerli eşitsizlikle çözerek tam dakika değerlerini toplar.',kalip='hikâyeli',sekil=TP(g),
 kart='K-MTB-10 · A = 80t, B = 840 − 60t; |A − B| ≤ 280 → t = 4, …, 8, toplam 30',
 metin='Doğrusal bir parkurda A ve B sporcuları, aynı anda ve birbirlerine doğru koşmaya başlamıştır; ikisi de sabit hızla koşmaktadır. Şekilde, sporcuların A sporcusunun başlangıç noktasından uzaklıklarının (m) süreye (dakika) göre değişimi gösterilmiştir ve antrenman 12 dakika sürmüştür. Sporcular, aralarındaki uzaklık 280 m’yi geçmediğinde (280 m dahil) telsizle haberleşebilmektedir.\nBuna göre sporcuların haberleşebildiği tam dakika değerlerinin (t = 0, 1, …, 12) toplamı kaçtır?',
 dogru=dog,yan=hata(dog,havuz,'E'),istenen='Haberleşme sağlanan tam dakika değerlerinin toplamı.',
 ip=['Her sporcu için grafikteki iki işaretli noktadan konum–zaman ifadesini yaz; aralarındaki uzaklığı bu ifadelerden kur.'],bilgi=[HAR,ARL],
 ad=[A('A’nın konumu','(0, 0) ve (10, 800) noktalarından hız 80 m/dk.','s_A = 80t'),A('B’nin konumu','(0, 840) ve (10, 240) noktalarından hız −60 m/dk.','s_B = 840 − 60t'),A('Uzaklık koşulu','Aralarındaki uzaklık mutlak değerle alınır.','|80t − (840 − 60t)| ≤ 280 → |140t − 840| ≤ 280'),A('Eşitsizliği çöz','İki yönlü: −280 ≤ 140t − 840 ≤ 280.','560 ≤ 140t ≤ 1120 → 4 ≤ t ≤ 8'),A('Topla','Tam dakika değerleri toplanır.','4 + 5 + 6 + 7 + 8 = 30')],
 puf='Uzaklık eşitsizliğinde mutlak değer iki yönlü bir aralık verir; uç değerler “geçmediğinde” ifadesiyle dahil olur.')

bitir(P,'mutlaksekb','mat|Mutlak Değer')
