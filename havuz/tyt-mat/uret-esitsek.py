"""Basit Eşitsizlikler · şekilli paket (esitsek): 8 soru, hepsi şekilli/tablolu. Kardeş yok, ipucu 1. Her cevap ve çeldirici değer kodla hesaplanıp assert edilir.
Şekil ölçüleri Python'da üretilir; TikZ gövdesi aynı değerlerden f-string ile yazılır (bkz. havuz/URETIM-SEKIL.md)."""
import sys,os,math
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
H.KONU='Basit Eşitsizlikler'
P=Parti('esitsek','Basit Eşitsizlikler','mat|Basit Eşitsizlikler')
KY='ÖSYM 2018–2026 TYT Matematik (şekilli eşitsizlik soruları, yalnız mantık) · MEB 9. sınıf'
TP=lambda g:tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'+g+'\n\\end{tikzpicture}')
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)
def tamlar(f,lo=-300,hi=300): return [x for x in range(lo,hi+1) if f(x)]

ARA=B('Aralık gösterimi','sayı doğrusunda içi dolu nokta ucun aralığa dahil, içi boş nokta dahil olmadığını gösterir. Örnek: ● 1 ile ○ 6 arasında boyalı aralıkta 1 vardır, 6 yoktur')
SAYI=B('Ardışık tam sayıların sayısı','a ile b arasındaki (uçlar dahil) tam sayıların sayısı b − a + 1’dir. Örnek: 4’ten 9’a kadar 9 − 4 + 1 = 6 tam sayı vardır')
TER=B('Eğik terazi','terazide aşağıda kalan kefe daha ağırdır; bu bir eşitsizlik verir. Örnek: sol kefe 2m, sağ kefe 30 g ve sağ kefe aşağıdaysa 2m < 30')
CARP=B('Eşitsizlikte çarpma','bir sayıyı negatif sayıyla çarpınca sıra yön değiştirir; 0 ile 1 arasındaki pozitif sayıyla çarpınca sayı küçülür. Örnek: −4 · (1/2) = −2 ve −2 > −4')
TERS=B('Ters alma','0 ile 1 arasındaki pozitif sayının tersi 1’den büyüktür; −1 ile 0 arasındaki sayının tersi −1’den küçüktür. Örnek: 1/(−0,25) = −4 < −1')
KAP=B('Sınır ve toplam kütle','toplam kütle sınırı aşılmaz; kütleler toplanıp sınırla karşılaştırılır ve tam sayı istenirse sonuç aşağı yuvarlanır. Örnek: 20 kg sınırında 3 kg’lık kutudan 6 tane konur, çünkü 7 · 3 = 21 > 20')
TUT=B('Tablodan eşitsizlik kurma','tablodaki birim fiyatlar toplam ödeme için çarpılıp toplanır ve sınırla karşılaştırılır. Örnek: 5 TL’lik a tane ve 3 TL’lik b tane ürün için 5a + 3b ≤ sınır')
ISI=B('Doğrusal artış','başlangıç sıcaklığı t0, saatlik artış d ise t saat sonra sıcaklık t0 + d · t’dir. Örnek: 2 °C’den saatte 0,5 °C artarsa 4 saat sonra 4 °C olur')
FARK=B('Küme işlemleri','K ve L’den yalnız birinde bulunan elemanlar, K’nın L’de olmayan ve L’nin K’da olmayan elemanlarıdır. Örnek: K = {1, 2, 3}, L = {3, 4} ise bu elemanlar 1, 2 ve 4’tür')
KOLI=B('Kısıtlı en çok sayı','kütle eşitsizliği ve sayı kısıtı birlikte düşünülür; en çok ürün için kısıtı tam sağlayan sınır durumuna bakılır. Örnek: 2a + b ≤ 10 ve b ≤ a için a = 3, b = 3 uygundur; a = 4 için b ≤ 2 olur')

kart('K-ESS-01','Sayı doğrusunda aralık okuma','Dolu ve boş uçlar okunarak aralık yazılır; aralıktaki tam sayılar sayılıp toplanır.','İçi boş ucu dahil saymak; içi dolu ucu dışarıda bırakmak; toplam yerine adet yazmak.','kolay','şekilli',3,'ess-aralik','Sayı doğrusunda aralığı okuma',KY)
kart('K-ESS-02','Eğik teraziler','Aşağıdaki kefenin daha ağır olduğu her tartım bir eşitsizlik verir; iki eşitsizliğin ortak aralığındaki tam sayılar sayılır.','Kefe yönünü ters okumak; ağırlığı eşitsizliğe katmamak; uçları dahil saymak.','orta','şekilli',4,'ess-terazi','Eğik terazilerden eşitsizlik kurma',KY)
kart('K-ESS-03','Sayı doğrusunda işaret ve sıra','Sayı doğrusundaki yerlerden a, b, c için işaret ve büyüklük bilgisi alınıp her öncül ayrı ayrı sınanır.','Kesirle çarpınca büyür sanmak; negatif sayının tersinin yönünü karıştırmak.','orta','öncüllü',4,'ess-yerler','Sayı doğrusunda yerleri verilen sayılar',KY)
kart('K-ESS-04','Taşıma sınırı tabelası','Tabeladaki toplam kütle sınırından araç ve sürücü kütlesi düşülür; kalan, tek bir yükün kütlesine bölünüp aşağı yuvarlanır.','Aracı ya da sürücüyü unutmak; yukarı yuvarlamak; sürücüyü her yüke eklemek.','orta','şekilli',4,'ess-tabela','Köprü tabelası ve taşıma sınırı',KY)
kart('K-ESS-05','Fiyat tablosundan eşitsizlik','Tablodaki iki birim fiyatla toplam ödeme sınırı bir eşitsizlik olur; kişi sayısı toplamı kullanılarak tek bilinmeyene indirilir.','Bölümü yuvarlarken yön hatası; sorulan sayı yerine öteki türün sayısını yazmak; fiyatı fark yerine tek fiyata bölmek.','orta','tablo',4,'ess-tarife','Fiyat tablosu ve bütçe',KY)
kart('K-ESS-06','Termometre ve güvenli aralık','Termometredeki başlangıç değeri ve güvenli bölgenin üst sınırı okunur; doğrusal artış eşitsizliğe çevrilir ve tam saat için aşağı yuvarlanır.','Başlangıç sıcaklığını unutmak; yukarı yuvarlamak; sınırı saat sayısı sanmak.','kolay','şekilli',3,'ess-termometre','Termometrede güvenli sıcaklık aralığı',KY)
kart('K-ESS-07','İki aralığın farkı','İki aralığın dolu ve boş uçları okunur; yalnız birinde bulunan tam sayılar bulunup toplanır.','Uçların dolu ya da boş olduğunu karıştırmak; kesişim ya da birleşim toplamını yazmak.','zor','şekilli',5,'ess-kesisim','Sayı doğrusunda iki aralık',KY)
kart('K-ESS-08','Koli ve kısıtlı en çok ürün','Tablodaki kütlelerle koli kütle eşitsizliği kurulur; kitap-defter oranı kısıtı eklenip en çok ürün sayısı kısıtı tam sağlayan durumda aranır.','Boş koli kütlesini unutmak; oran kısıtını unutmak; yuvarlamada kısıtı bozmak.','zor','tablo',5,'ess-koli','Tablodan kütle sınırı ve kısıt',KY)

# ---------- 01 · kolay · sayı doğrusunda aralık ----------
lo,hi=-6,2; S=tamlar(lambda x:lo<x<=hi); top=sum(S)
assert S==[-5,-4,-3,-2,-1,0,1,2] and top==-12 and len(S)==8
assert sum(tamlar(lambda x:lo<=x<=hi))==-18 and sum(tamlar(lambda x:lo<x<hi))==-14 and sum(tamlar(lambda x:lo<=x<hi))==-20
s=.62; g=f'\\draw[-{{Stealth}}] ({-8.6*s:.2f},0) -- ({4.8*s:.2f},0);'
for i in range(-8,5): g+=f'\\draw ({i*s:.2f},-.1) -- ({i*s:.2f},.1);\\node[below=3pt,font=\\footnotesize] at ({i*s:.2f},0) {{${i}$}};'
g+=f'\\draw[line width=3pt,vurgu] ({lo*s:.2f},0) -- ({hi*s:.2f},0);\\draw[thick,fill=white] ({lo*s:.2f},0) circle (.1);\\fill[vurgu] ({hi*s:.2f},0) circle (.1);\\node[above=6pt] at ({(lo+hi)*s/2:.2f},0) {{$x$ değerleri}};'
q('0001',tipId='ess-aralik',tip='Sayı doğrusunda aralığı okuma',z='kolay',alt='Aralık Gösterimi',kaz='Sayı doğrusunda dolu ve boş uçlarla gösterilen aralıktaki tam sayıları belirleyip toplar.',kalip='şekilli',sekil=TP(g),
 kart='K-ESS-01 (aralık okuma) · (−6, 2] aralığı, tam sayıların toplamı',
 metin='Şekildeki sayı doğrusunda boyalı bölge, x gerçel sayısının alabileceği değerleri göstermektedir.\nBuna göre bu değerlerden tam sayı olanların toplamı kaçtır?',
 dogru=-12,yan=[(-18,'İki ucu da dahil sayıp −6’yı da toplamış; içi boş uç aralığa dahil değildir.','dikkat'),(-14,'İki ucu da dışarıda bırakmış; içi dolu uç (2) aralığa dahildir.','dikkat'),(-20,'Uçları ters okumuş: −6’yı dahil edip 2’yi dışarıda bırakmış.','dikkat'),(8,'Toplam yerine tam sayıların adedini (8) yazmış.','dikkat')],
 istenen='x’in alabileceği tam sayıların toplamı.',
 ip=['Boyalı aralığın iki ucundaki nokta türlerine bak; hangi uç aralığa girer?'],
 bilgi=[ARA],
 ad=[A('Aralığı oku','Sol uç içi boş, sağ uç içi doludur.','−6 < x ≤ 2'),A('Tam sayıları yaz','−5’ten 2’ye kadar tam sayılar alınır.','−5, −4, −3, −2, −1, 0, 1, 2'),A('Topla','Toplamı bul.','−5 − 4 − 3 − 2 − 1 + 0 + 1 + 2 = −12')],
 puf='Aynı büyüklükte zıt işaretli sayılar birbirini götürür: yalnız −5, −4 ve −3 kalır.')

# ---------- 02 · orta · eğik teraziler ----------
w1,m1,ag1=3,50,410; ag2=150; n2=2
xs=tamlar(lambda x:x>0 and w1*x+m1<ag1 and n2*x>ag2); assert xs==list(range(76,120)) and len(xs)==44
assert len(tamlar(lambda x:x>0 and w1*x+m1<ag1 and n2*x>=ag2))==45 and len(tamlar(lambda x:x>0 and w1*x+m1<=ag1 and n2*x>=ag2))==46
assert len(tamlar(lambda x:x>0 and w1*x+m1<ag1 and n2*x>ag2,0,119))==44 and len(range(76,119))==43
assert len(tamlar(lambda x:x>0 and w1*x<ag1 and n2*x>ag2))==61 and 76<=76 and max(tamlar(lambda x:x>0 and w1*x<ag1))==136
def terazi(cy,sol_asagi,solobj,sagobj,ad):
    th=9; h=2.3; sg=1 if sol_asagi else -1; cx=0
    yl=cy-sg*h*math.sin(math.radians(th)); yr=cy+sg*h*math.sin(math.radians(th))
    xl=cx-h*math.cos(math.radians(th)); xr=cx+h*math.cos(math.radians(th)); hw=1.85; dy=1.1
    s=f'\\draw[thick] ({xl:.3f},{yl:.3f}) -- ({xr:.3f},{yr:.3f});\\fill ({cx},{cy}) circle (.09);\\draw[thick] ({cx},{cy}) -- ({cx},{cy-3.0});\\draw[thick] ({cx-.8},{cy-3.0}) -- ({cx+.8},{cy-3.0});\\node[anchor=east] at ({xl-.1-hw+.6:.3f},{cy+.9:.3f}) {{\\bfseries {ad}}};'
    for (px,py,obj) in [(xl,yl,solobj),(xr,yr,sagobj)]:
        s+=f'\\draw ({px:.3f},{py:.3f}) -- ({px-hw:.3f},{py-dy:.3f});\\draw ({px:.3f},{py:.3f}) -- ({px+hw:.3f},{py-dy:.3f});\\draw[thick] ({px-hw:.3f},{py-dy:.3f}) -- ({px+hw:.3f},{py-dy:.3f});'
        tw=sum(.7 if o=='o' else 1.35 for o in obj)-.05; xx=px-tw/2
        for o in obj:
            if o=='o': s+=f'\\draw[fill=vurgu!30] ({xx+.3:.3f},{py-dy+.3:.3f}) circle (.3);'; xx+=.7
            else: s+=f'\\draw[fill=white] ({xx:.3f},{py-dy:.3f}) rectangle ({xx+1.3:.3f},{py-dy+.62:.3f});\\node at ({xx+.65:.3f},{py-dy+.31:.3f}) {{{o}}};'; xx+=1.35
    return s
g=terazi(0,False,['o','o','o','50 g'],['410 g'],'I')+terazi(-5.6,True,['o','o'],['150 g'],'II')
g+='\\draw[fill=vurgu!30] (-2.3,-9.1) circle (.3);\\node[anchor=west] at (-1.8,-9.1) {: bir portakal (her biri $x$ g)};'
q('0002',tipId='ess-terazi',tip='Eğik terazilerden eşitsizlik kurma',z='orta',alt='Eşitsizlik Problemleri',kaz='İki eğik terazinin verdiği eşitsizliklerin ortak çözümündeki tam sayıları sayar.',kalip='şekilli',sekil=TP(g),
 kart='K-ESS-02 (eğik teraziler) · 3x + 50 < 410 ve 2x > 150, tam sayı adedi',
 metin='Şekildeki iki teraziye, özdeş portakallar ile kütleleri üzerinde yazılı ağırlıklar konulmuştur; aşağıda kalan kefe daha ağırdır. Her portakalın kütlesi x gramdır ve x pozitif bir tam sayıdır.\nBuna göre x kaç farklı değer alabilir?',
 dogru=44,yan=[(43,'Üst sınırı 119, alt sınırı 76 bulup 119 − 76 = 43 yazmış; uçlar dahil sayılırken 1 eklenir.','dikkat'),(45,'İkinci terazide eşitlik de olabilirmiş gibi x ≥ 75 alıp 75 ile 119 arasındaki 45 değeri saymış.','dikkat'),(46,'İki teraziyi de eşitliğe izin veren (≤ ve ≥) okuyup 75’ten 120’ye 46 değer saymış.','dikkat'),(61,'Birinci terazideki 50 g’lık ağırlığı hesaba katmamış: 3x < 410, x ≤ 136 ve 76’dan 136’ya 61 değer bulmuş.','islem')],
 istenen='x’in alabileceği tam sayı değerlerinin sayısı.',
 ip=['Her teraziden, aşağıdaki kefenin daha ağır olduğunu kullanarak ayrı bir eşitsizlik yaz.'],
 bilgi=[TER,SAYI],
 ad=[A('Birinci terazi','Sağ kefe aşağıda: sağ kefe daha ağır.','3x + 50 < 410 → x < 120'),A('İkinci terazi','Sol kefe aşağıda: sol kefe daha ağır.','2x > 150 → x > 75'),A('Ortak aralık','İki koşulu birlikte yaz; uçlar dahil değildir.','75 < x < 120 → x = 76, …, 119'),A('Say','76’dan 119’a kadar.','119 − 76 + 1 = 44')],
 puf='Eğik terazide eşitlik yoktur: kefe aşağıdaysa kesin eşitsizlik (< ya da >) yazılır.')

# ---------- 03 · orta · sayı doğrusunda a, b, c ----------
a_,b_,c_=-.55,.45,1.7
for a in (-.9,-.55,-.1):
    for b in (.1,.45,.9):
        for c in (1.2,1.7,5):
            I=b*c>b; II=a*b<a; III=1/a<-1
            assert I and not II and III
            assert not (a*b<a) and a*b>a
s=2.1; g=f'\\draw[-{{Stealth}}] ({-1.7*s:.2f},0) -- ({2.4*s:.2f},0);'
for t in (-1,0,1): g+=f'\\draw ({t*s:.2f},-.1) -- ({t*s:.2f},.1);\\node[below=4pt] at ({t*s:.2f},0) {{${t}$}};'
for nm,v in (('a',a_),('b',b_),('c',c_)): g+=f'\\fill[vurgu] ({v*s:.3f},0) circle (.1);\\node[above=5pt] at ({v*s:.3f},0) {{${nm}$}};'
q('0003',tipId='ess-yerler',tip='Sayı doğrusunda yerleri verilen sayılar',z='orta',alt='Sayı Doğrusunda Sıralama',kaz='Sayı doğrusunda yerleri verilen a, b, c için çarpım ve ters ifadelerinin doğruluğunu sınar.',kalip='öncüllü',sekil=TP(g),
 kart='K-ESS-03 (sayı doğrusunda a, b, c) · a ∈ (−1, 0), b ∈ (0, 1), c > 1',
 metin='Şekildeki sayı doğrusunda a, b ve c sayılarının yerleri gösterilmiştir.\nBuna göre,\nI. b · c > b\nII. a · b < a\nIII. 1/a < −1\nifadelerinden hangileri kesinlikle doğrudur?',
 dogru='I ve III',sira=['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III'],
 yan=[('Yalnız I','III’ün doğru olduğunu görememiş; −1 ile 0 arasındaki bir sayının tersini −1’den büyük sanmış.','bilgi'),('Yalnız II','Yalnız “negatif ile çarpınca küçülür” kuralını uygulamış; I’de c > 1 olduğunu, III’te tersin −1’den küçük olduğunu görmemiş.','bilgi'),('I ve II','II’yi doğru sanmış (a negatif olduğundan çarpım küçülür demiş) ve III’ü yanlış bulmuş.','bilgi'),('I, II ve III','II’yi de doğru sanmış; b 0 ile 1 arasında olduğundan a · b sayısı a’dan büyüktür.','bilgi')],
 istenen='Kesinlikle doğru olan öncüller.',
 ip=['Şekilden her sayının hangi iki tam sayı arasında (ya da hangi sayının sağında) olduğunu belirle.'],
 bilgi=[CARP,TERS],
 ad=[A('Yerleri oku','Şekle göre sayıların aralıkları.','−1 < a < 0 · 0 < b < 1 · c > 1'),A('I’i sına','b pozitif ve c > 1 olduğundan b · c, b’den büyüktür.','b × c − b = b(c − 1) > 0 → doğru'),A('II’yi sına','a negatif, b ile 0 arasında kesir olduğundan a · b sayısı a ile 0 arasındadır.','a × b > a → II yanlış'),A('III’ü sına','−1 ile 0 arasındaki bir sayının tersi −1’den küçüktür.','1/a < −1 → doğru')],
 puf='Sayıyı kesirle çarpmak onu sıfıra yaklaştırır: negatif sayı büyür, pozitif sayı küçülür.')

# ---------- 04 · orta · köprü tabelası ----------
lim,bos,sur,sd=18000,7500,90,700
n=(lim-bos-sur)//sd; assert n==14 and n*sd<=lim-bos-sur<(n+1)*sd and bos+sur+n*sd==17390
assert (lim-bos)//(sd+sur)==13 and (lim-bos-sur)/sd>14.8 and -(-(lim-bos-sur)//sd)==15 and lim//sd==25 and (bos+sur)//sd==10
g='\\draw[thick] (0,0) rectangle (6.6,1.6);\\node at (3.3,1.15) {\\bfseries KÖPRÜ};\\node at (3.3,.5) {Toplam kütle sınırı: 18 000 kg};'
g+='\\draw[thick] (.1,-2.6) rectangle (1.9,-1.7);\\draw[thick] (1.9,-2.6) rectangle (2.6,-2.0);\\draw[fill=white,thick] (.6,-2.6) circle (.17);\\draw[fill=white,thick] (2.1,-2.6) circle (.17);\\node[align=center] at (1.35,-3.35) {Boş kamyon\\\\7 500 kg};'
g+='\\draw[thick] (3.9,-1.55) circle (.17);\\draw[thick] (3.9,-1.72) -- (3.9,-2.2);\\draw[thick] (3.55,-1.95) -- (4.25,-1.95);\\draw[thick] (3.9,-2.2) -- (3.65,-2.65);\\draw[thick] (3.9,-2.2) -- (4.15,-2.65);\\node[align=center] at (3.9,-3.35) {Sürücü\\\\90 kg};'
g+='\\draw[thick] (5.3,-2.6) rectangle (6.3,-1.6);\\draw (5.3,-2.6) -- (6.3,-1.6);\\draw (5.3,-1.6) -- (6.3,-2.6);\\node[align=center] at (5.8,-3.35) {Sandık (her biri)\\\\700 kg};'
q('0004',tipId='ess-tabela',tip='Köprü tabelası ve taşıma sınırı',z='orta',alt='Eşitsizlik Problemleri',kaz='Toplam kütle sınırından araç ve sürücü kütlesini düşüp en çok kaç özdeş yük taşınabileceğini bulur.',kalip='şekilli',sekil=TP(g),
 kart='K-ESS-04 (köprü tabelası) · 18 000 kg sınır, 7 500 kg kamyon, 90 kg sürücü, 700 kg sandık',
 metin='Şekilde, bir köprünün giriş tabelası ile köprüden geçecek kamyon, sürücü ve sandıkların kütleleri verilmiştir. Tabelada yazılan sınır, köprüden geçen aracın sürücü ve yük dahil toplam kütlesi içindir; kamyonda sürücüden ve sandıklardan başka bir yük yoktur.\nBuna göre kamyonla köprüden en çok kaç sandık geçirilebilir?',
 dogru=14,yan=[(10,'7 590 kg’ı yük kütlesi sanıp 7 590 ÷ 700 = 10,8 → 10 bulmuş; oysa 7 590 kg kamyon ve sürücünün kütlesidir, sandıklara sınırdan kalan kütle ayrılır.','dikkat'),(13,'Sürücünün 90 kg’ını her sandığa eklemiş: 10 500 ÷ 790 = 13,3 → 13.','islem'),(15,'Sürücüyü unutup 10 500 ÷ 700 = 15 bulmuş; sürücüyle birlikte 15 sandık sınırı 90 kg aşar (18 090 kg).','dikkat'),(25,'Kamyon ve sürücüyü hesaba katmamış: 18 000 ÷ 700 = 25,7 → 25.','dikkat')],
 istenen='Geçirilebilecek en çok sandık sayısı.',
 ip=['Sınırdan sandıklara ayrılabilecek kütleyi bulmak için nelerin kütlesi önce çıkarılmalı?'],
 bilgi=[KAP],
 ad=[A('Yük için kalan kütle','Toplam sınırdan kamyon ve sürücü düşülür.','18 000 − 7 500 − 90 = 10 410 kg'),A('Eşitsizlik','n sandığın kütlesi bu kalanı aşmamalı.','700 · n ≤ 10 410'),A('Çöz','Bölümü hesapla.','n ≤ 14,87'),A('Tam sayıya indir','Sandık sayısı tam sayı olup sınırı aşmamalıdır; aşağı yuvarlanır.','n = 14')],
 puf='“En çok kaç tane” sorularında bölüm ondalık çıkarsa aşağı yuvarlanır; yukarı yuvarlamak sınırı aşar.')

# ---------- 05 · orta · fiyat tablosu ----------
tam,og,kisi,tut=80,55,12,800
okmin=min(o for o in range(0,kisi+1) if tam*(kisi-o)+og*o<=tut); assert okmin==7 and tam*(kisi-6)+og*6==810>tut and tam*(kisi-7)+og*7==785<=tut
assert 160//og==2 and (tam*kisi-tut)//tam==2 and (kisi-okmin)==5 and 160//25==6 and (160+24)//25==7
sek=tablo_svg(['Bilet türü','Fiyat (TL)'],[['Tam','80'],['Öğrenci','55']])
q('0005',tipId='ess-tarife',tip='Fiyat tablosu ve bütçe',z='orta',alt='Eşitsizlik Problemleri',kaz='Tablodaki birim fiyatlardan toplam ödeme eşitsizliği kurup en az öğrenci biletini bulur.',kalip='tablo',sekil=sek,
 kart='K-ESS-05 (fiyat tablosu) · 12 kişi, en çok 800 TL, 80 ve 55 TL biletler',
 metin='Bir sinemanın tam ve öğrenci biletlerinin fiyatları aşağıdaki tabloda verilmiştir. 12 kişilik bir grubun herkesi tam ya da öğrenci bileti alacak ve bilet için toplam en çok 800 TL ödenecektir; başka bir ücret yoktur.\nBuna göre bu grupta en az kaç kişi öğrenci bileti almalıdır?',
 dogru=7,yan=[(2,'800 ÷ 80 = 10 kişinin tam bilet alabileceğini düşünüp kalan 12 − 10 = 2 kişiyi öğrenci saymış.','dikkat'),(10,'800 ÷ 80 = 10’u öğrenci sayısı sanmış; 10 öğrenci bileti de şartı sağlar ama en az sayı sorulmuştur.','dikkat'),(5,'Sorulan sayı yerine tam bilet sayısını (12 − 7 = 5) yazmış.','dikkat'),(6,'6,4’ü aşağı yuvarlamış: 6 öğrenci ile ödeme 810 TL olur, 800 TL’yi aşar.','dikkat')],
 istenen='En az öğrenci bileti sayısı.',
 ip=['Öğrenci sayısına ö dersen tam bilet sayısı kaç olur ve toplam ödeme nasıl yazılır?'],
 bilgi=[TUT],
 ad=[A('Bilet sayıları','Öğrenci sayısı ö ise tam bilet 12 − ö olur.','tam: 12 − ö · öğrenci: ö'),A('Eşitsizlik','Toplam ödeme 800 TL’yi aşmamalı.','80(12 − ö) + 55ö ≤ 800'),A('Sadeleştir','Parantezi aç, ö’yü yalnız bırak.','960 − 25ö ≤ 800 → ö ≥ 6,4'),A('Tam sayıya çevir','Öğrenci sayısı tam sayı olacağından yukarı yuvarlanır.','ö = 7')],
 puf='“En az” sorulduğunda bölüm ondalık çıkarsa yukarı, “en çok” sorulduğunda aşağı yuvarlanır.')

# ---------- 06 · kolay · termometre ----------
t0,d,ust=3,Fr(6,5),8
Ts=[h for h in range(0,30) if t0+d*h<=ust]; assert max(Ts)==4 and t0+d*4==Fr(39,5) and t0+d*5==9>ust
assert int(ust/d)==6 and -(-ust//1)==8 and t0+d*3<ust and t0+d*6==Fr(51,5)
u=.43; yy=lambda t:t*u; ymin=-2
g=f'\\draw[thick,rounded corners=2pt] (-.17,{yy(ymin)-.25:.3f}) rectangle (.17,{yy(11.5):.3f});\\fill[vurgu] (-.1,{yy(ymin)-.3:.3f}) rectangle (.1,{yy(t0):.3f});\\draw[thick,fill=vurgu] (0,{yy(ymin)-.5:.3f}) circle (.3);'
g+=f'\\draw[thick,fill=gray!30] (.55,{yy(2):.3f}) rectangle (.85,{yy(ust):.3f});\\node[anchor=west,align=center] at (.95,{yy(5):.3f}) {{güvenli\\\\bölge}};'
g+=f'\\draw[dotted] (.17,{yy(2):.3f}) -- (.55,{yy(2):.3f});\\draw[dotted] (.17,{yy(ust):.3f}) -- (.55,{yy(ust):.3f});'
for t in range(ymin,12): g+=f'\\draw (-.17,{yy(t):.3f}) -- (-.3,{yy(t):.3f});\\node[anchor=east,font=\\scriptsize] at (-.33,{yy(t):.3f}) {{${t}$}};'
g+=f'\\node[anchor=west] at (.95,{yy(11):.3f}) {{$^\\circ$C}};'
q('0006',tipId='ess-termometre',tip='Termometrede güvenli sıcaklık aralığı',z='kolay',alt='Eşitsizlik Problemleri',kaz='Termometreden başlangıç değerini ve güvenli üst sınırı okuyup doğrusal artış eşitsizliğiyle en çok kaç tam saat güvenli kalındığını bulur.',kalip='şekilli',sekil=TP(g),
 kart='K-ESS-06 (termometre) · 3 °C başlangıç, 1,2 °C/saat artış, 8 °C üst sınır',
 metin='Şekildeki termometre, bir aşı dolabının şu anki sıcaklığını (yeşil sütun) ve aşıların saklanabileceği güvenli bölgeyi göstermektedir. Elektrik kesintisi nedeniyle dolabın sıcaklığı her saat sabit olarak 1,2 °C artmaktadır. Sıcaklık sınırlar dahil güvenli bölgede kaldığı sürece aşılar bozulmaz.\nBuna göre aşıların bozulmaması için kesinti en çok kaç tam saat sürebilir?',
 dogru=4,yan=[(5,'4,17’yi yukarı yuvarlamış: 5 saat sonra sıcaklık 9 °C olur ve güvenli bölgeden çıkar.','dikkat'),(6,'Başlangıç sıcaklığını (3 °C) hesaba katmamış: 8 ÷ 1,2 = 6,7 → 6.','dikkat'),(7,'Başlangıç sıcaklığını unutup 8 ÷ 1,2 = 6,7’yi yukarı yuvarlamış.','dikkat'),(8,'Güvenli bölgenin üst sınırını (8 °C) saat sayısı sanmış.','dikkat')],
 istenen='Kesintinin sürebileceği en çok tam saat.',
 ip=['Şu anki sıcaklık ve saatlik artış t saat sonrası için nasıl bir ifade verir? Üst sınırla karşılaştır.'],
 bilgi=[ISI],
 ad=[A('Değerleri oku','Cıva seviyesi 3 °C, güvenli bölgenin üst ucu 8 °C.','başlangıç 3 °C · üst sınır 8 °C'),A('Eşitsizlik','t saat sonra sıcaklık 8 °C’yi aşmamalı.','3 + 1,2t ≤ 8 → t ≤ 4,17'),A('Tam saate çevir','Süre tam saat sayılacağından aşağı yuvarlanır.','t = 4')],
 puf='Güvenli sınırı aşmamak için bölüm ondalıksa aşağı yuvarlanır; hangi saat sonunda kaç °C olduğunu kontrol et: 4. saatte 7,8 °C, 5. saatte 9 °C.')

# ---------- 07 · zor · iki aralığın farkı ----------
Kd=lambda x:-5<=x<4; Ld=lambda x:-2<x<=8
sd=tamlar(lambda x:Kd(x)!=Ld(x)); assert sd==[-5,-4,-3,-2,4,5,6,7,8] and sum(sd)==16
assert sum(tamlar(lambda x:Kd(x) and Ld(x)))==5 and sum(tamlar(lambda x:Kd(x) or Ld(x)))==21
assert sum(tamlar(lambda x:(-5<=x<=4)!=(-2<=x<=8)))==14 and sum(tamlar(lambda x:(-5<x<4)!=(-2<x<8)))==13 and sum(tamlar(lambda x:Kd(x) and not Ld(x)))==-14
s=.5; g=''
for j,(nm,l,r,lf,rf) in enumerate((('K',-5,4,True,False),('L',-2,8,False,True))):
    y=-j*1.5; g+=f'\\draw[-{{Stealth}}] ({-6.6*s:.2f},{y}) -- ({9.8*s:.2f},{y});\\node at ({-7.4*s:.2f},{y}) {{{nm}}};'
    for i in range(-6,10): g+=f'\\draw ({i*s:.2f},{y-.1}) -- ({i*s:.2f},{y+.1});\\node[below=3pt,font=\\scriptsize] at ({i*s:.2f},{y-.05}) {{${i}$}};'
    g+=f'\\draw[line width=3pt,vurgu] ({l*s:.2f},{y}) -- ({r*s:.2f},{y});'
    g+=(f'\\fill[vurgu] ({l*s:.2f},{y}) circle (.1);' if lf else f'\\draw[thick,fill=white] ({l*s:.2f},{y}) circle (.1);')+(f'\\fill[vurgu] ({r*s:.2f},{y}) circle (.1);' if rf else f'\\draw[thick,fill=white] ({r*s:.2f},{y}) circle (.1);')
q('0007',tipId='ess-kesisim',tip='Sayı doğrusunda iki aralık',z='zor',alt='Aralıklar',kaz='Sayı doğrusunda gösterilen iki aralığın yalnız birinde bulunan tam sayıları belirleyip toplar.',kalip='şekilli',sekil=TP(g),
 kart='K-ESS-07 (iki aralığın farkı) · K = [−5, 4), L = (−2, 8]',
 metin='Şekildeki sayı doğrularında K ve L aralıkları gösterilmiştir.\nBuna göre, K ve L aralıklarından yalnız birinde bulunan tam sayıların toplamı kaçtır?',
 dogru=16,yan=[(5,'K ile L’nin ortak (kesişim) tam sayılarını toplamış: −1 + 0 + 1 + 2 + 3 = 5.','dikkat'),(13,'Dolu–boş uçları hep boş okumuş: K = (−5, 4), L = (−2, 8) için −4, −3, −2 ve 4, 5, 6, 7 → −9 + 22 = 13.','dikkat'),(14,'Dolu–boş uçları hep dolu okumuş: K = [−5, 4], L = [−2, 8] için −5, −4, −3 ve 5, 6, 7, 8 → −12 + 26 = 14.','dikkat'),(-14,'Yalnız K’de olup L’de olmayan tam sayıları toplamış; L’de olup K’de olmayanları unutmuş.','dikkat')],
 istenen='Yalnız birinde bulunan tam sayıların toplamı.',
 ip=['Her aralığın iki ucunun dolu mu boş mu olduğuna bak; iki aralığın üst üste bindiği yeri ayır.'],
 bilgi=[ARA,FARK],
 ad=[A('Aralıkları oku','Dolu uç dahil, boş uç dahil değil.','K: −5 ≤ x < 4 · L: −2 < x ≤ 8'),A('Yalnız K’de olanlar','K’de olup L’de olmayan tam sayılar (−2 K’dedir, L’de değildir).','−5, −4, −3, −2 → toplam −14'),A('Yalnız L’de olanlar','L’de olup K’de olmayan tam sayılar (4 L’dedir, K’de değildir).','4, 5, 6, 7, 8 → toplam 30'),A('Birleştir','İki grup ayrı olduğundan toplamları toplanır.','−14 + 30'),A('Sonuç','Toplamı bul.','16')],
 puf='Uçlardaki −2 ve 4 sayıları en çok karıştırılan yerlerdir: −2 yalnız K’de, 4 yalnız L’dedir; her sayıyı iki aralıkta ayrı ayrı sına.')

# ---------- 08 · zor · koli ----------
bk,kt,dt,sinir=800,450,150,10000
def en(bk_,kisit=True):
    b=None
    for k in range(1,60):
        for dd in range(1,200):
            if bk_+kt*k+dt*dd<=sinir and (dd<=2*k or not kisit):
                if b is None or k+dd>b[0]: b=(k+dd,k,dd)
    return b
assert en(bk)==(36,12,24) and en(0)[0]==39 and en(bk,False)==(59,1,58)
assert 800+450*13+150*22<=sinir<800+450*13+150*23 and 13+22==35 and 11+22==33 and 12+25==37 and bk+kt*12+dt*25<=sinir and 25>2*12
sek=tablo_svg(['Madde','Kütle (g)'],[['Boş koli','800'],['Kitap','450'],['Defter','150'],['Koli taşıma sınırı','10 000']])
q('0008',tipId='ess-koli',tip='Tablodan kütle sınırı ve kısıt',z='zor',alt='Eşitsizlik Problemleri',kaz='Tablodaki kütlelerle kurulan kütle eşitsizliğini ve ürün sayısı kısıtını birlikte kullanıp en çok ürün sayısını bulur.',kalip='tablo',sekil=sek,
 kart='K-ESS-08 (koli) · 800 + 450k + 150d ≤ 10 000, 1 ≤ k, d ≤ 2k, k + d en çok',
 metin='Bir kolinin ve içine konulacak ürünlerin kütleleri aşağıdaki tabloda verilmiştir. Koliye kitap ve defterden başka bir şey konulmayacak, koli taşıma sınırını aşmayacaktır. Koliye en az bir kitap konulacak ve defter sayısı kitap sayısının iki katını geçmeyecektir.\nBuna göre kolide en çok kaç ürün (kitap ve defter birlikte) bulunabilir?',
 dogru=36,yan=[(33,'Kitap sayısını 11 alıp 3 · 11 + d ≤ 61 ve d ≤ 22 ile 33 ürün bulmuş; kitap sayısını daha büyük almak daha çok ürün verir.','islem'),(35,'Kitap sayısını 13 alıp d ≤ 22 ile 35 ürün bulmuş; kitap sayısını 12’den büyük almak toplamı artırmaz.','islem'),(37,'Kitap 12 iken kütle sınırına göre 25 defter koyup defter sayısı kısıtını (d ≤ 24) bozmuş.','dikkat'),(39,'Boş kolinin 800 g’ını hesaba katmamış: 3k + d ≤ 66, k = 13, d = 26 ile 39 ürün bulmuş.','dikkat')],
 istenen='Kolideki en çok ürün sayısı.',
 ip=['Kitap sayısına k, defter sayısına d dersen hem kütle hem de oran kısıtını sağlayan en büyük k + d hangi durumda gerçekleşir?'],
 bilgi=[KOLI],
 ad=[A('Kütle eşitsizliği','Boş koli dahil toplam kütle sınırı aşmamalı.','800 + 450k + 150d ≤ 10 000 → 3k + d ≤ 61'),A('Oran kısıtı','Defter sayısı en çok kitabın iki katı.','d ≤ 2k'),A('En çok ürün','Defter ne kadar çoksa o kadar iyi: d = 2k alınır.','3k + 2k ≤ 61 → k ≤ 12,2 → k = 12'),A('Defter sayısını yaz','k = 12 için hem kütle hem oran kısıtı sağlanır.','d = 24 (36 + 24 = 60 ≤ 61)'),A('Toplam','Kitap ve defteri topla.','12 + 24 = 36')],
 puf='Kısıtlı en çok sorularında küçük sayılarla kısıtı deneyerek sonucu doğrula: k = 13 için d ≤ 22 olur ve toplam 35’e düşer.')

bitir(P,'esitsek','mat|Basit Eşitsizlikler')
