"""Basit Eşitsizlikler · ŞEKİLLİ ek paket b (esitsizsekb): 10 soru, hepsi şekilli/grafikli/tablolu. Kardeş yok, ipucu 1.
Her doğru cevap ve her çeldirici değer kodla (tarama / Fraction) hesaplanıp assert edilir. Şekil ölçüleri Python'da üretilir (bkz. havuz/URETIM-SEKIL.md)."""
import sys,os,math
from itertools import combinations
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
H.KONU='Basit Eşitsizlikler'
P=Parti('esitsizsekb','Basit Eşitsizlikler','mat|Basit Eşitsizlikler')
KY='ÖSYM 2018–2026 TYT Matematik (şekilli/grafikli/tablolu eşitsizlik soruları; yalnız mantık) · MEB 9. sınıf'
TP=lambda g:tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'+g+'\n\\end{tikzpicture}')
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)
def tara(f,lo=-300,hi=300): return [x for x in range(lo,hi+1) if f(x)]
def sec(dog,havuz,harf):
    """Havuzdaki hata değerlerinden 4 tanesini seçer; doğru cevap istenen harfte (sayısal sıra) kalır."""
    if harf is None: return list(havuz[:4])
    i='ABCDE'.index(harf)
    for c in combinations(havuz,4):
        v=[p[0] for p in c]
        if len({dog,*v})==5 and sum(p<dog for p in v)==i: return list(c)
    raise AssertionError(('harf tutmuyor',harf,dog,[p[0] for p in havuz]))
def hata(dog,havuz,harf,tur='dikkat'): return [(v,a,t) for v,a,t in sec(dog,[(v,a,t) for v,a,t in havuz],harf)]

# ---------- bilgi kutuları (örnekler sorulardan bağımsız) ----------
ESZ=B('Birinci dereceden eşitsizlik','eşitsizliğin iki yanına aynı sayı eklenir ya da çıkarılır; negatif bir sayıyla çarpılır ya da bölünürse eşitsizliğin yönü değişir. Örnek: −3x < 12 ise x > −4 olur')
SAYI=B('Ardışık tam sayıların sayısı','a ile b arasındaki (uçlar dahil) tam sayıların sayısı b − a + 1’dir; bir uç dahil değilse o uç sayılmaz. Örnek: 2 < x ≤ 7 için x = 3, 4, 5, 6, 7 olmak üzere 5 değer vardır')
DGR=B('Doğrusal grafik','doğrusal bir grafikte iki noktanın koordinatlarından eğim, y’deki değişimin x’teki değişime oranıdır; y = eğim · x + başlangıç değeri yazılır. Örnek: (0, 4) ve (2, 10) noktalarından geçen doğrunun eğimi 3, denklemi y = 3x + 4’tür')
HAC=B('Hacim ve seviye','bir kaba konan cismin hacmi kadar su yer değiştirir; kabın doluluk seviyesi bu hacim kadar yükselir. Örnek: 80 mL suya 15 mL’lik bir cisim konursa seviye 95 mL’ye çıkar')
UCG=B('Üçgen eşitsizliği','bir üçgende her kenar uzunluğu, diğer iki kenar uzunluğunun toplamından küçüktür. Örnek: kenarları 3, 4 ve 8 olan bir üçgen çizilemez, çünkü 8 > 3 + 4')
AGO=B('Ağırlıklı ortalama','ağırlıklı ortalama, her değerin katsayısıyla çarpımlarının toplamının katsayılar toplamına bölünmesidir. Örnek: katsayıları 1 ve 3 olan 50 ve 70 puanın ağırlıklı ortalaması (50 + 210) ÷ 4 = 65’tir')
ISL=B('Makine ve işlem sırası','işlemler okların yönünde sırayla uygulanır; ilk işlemin sonucu ikinci işlemin girdisi olur. Örnek: önce 2 ile çarpıp sonra 3 ekleyen makineye 5 girerse 13 çıkar')
YOL=B('Yol, hız ve zaman','sabit hızla alınan yol = hız × süre olduğundan süre, yolun hıza bölümüdür; saat ve dakika dönüşümünde 1 saat 60 dakikadır. Örnek: 90 km yol 60 km/sa hızla 1,5 saatte, yani 1 saat 30 dakikada alınır')
ARL=B('Aralık gösterimi','sayı doğrusunda içi dolu nokta ucun aralığa dahil olduğunu, içi boş nokta dahil olmadığını gösterir. Örnek: içi boş 1 ve içi dolu 4 ile gösterilen aralık 1 < x ≤ 4 olarak yazılır')
TAR=B('Doğrusal ücret','sabit bir ücret ile birim başına ücretin çarpımı toplanarak toplam ücret bulunur; iki ücretin karşılaştırılması bir eşitsizlik verir. Örnek: 50 TL + 3 TL/birim ile 20 TL + 5 TL/birim ücretler 15 birimde eşit olur')
KEN=B('Aralıklarda toplama ve çıkarma','a ile b aralıkları verilmişse a + b’nin aralığı uçların toplamlarıdır; −b’nin aralığı için uçların işareti değişir ve eşitsizliğin yönü ters döner. Örnek: 1 < a < 3 ve 2 < b < 5 ise 1 + 2 < a + b < 3 + 5 ve −5 < −b < −2 olur')

# ---------- kartlar (fikir; sorudan bağımsız) ----------
def kk(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)
kk('K-ESB-01','Doğrusal grafikten eşitsizlik','Grafikte okunan iki noktadan doğrunun denklemi kurulur ve verilen sınır eşitsizliğe çevrilir.','Eğimi yanlış okumak; sınır değerini yuvarlarken yukarı almak; başlangıç değerini atlamak.','kolay','grafik',3,'esb-grafik','Doğrusal grafikten eşitsizlik')
kk('K-ESB-02','Seviye ölçüsünden eşitsizlik','Kaptaki boşluk hacmi okunur; eşit parçalara bölünen hacimle karşılaştırılıp tam sayı sınırı bulunur.','Boşluk yerine su hacmini kullanmak; bölmeyi unutmak; sınırı yukarı yuvarlamak.','kolay','hikâyeli',3,'esb-kap','Ölçekli kapta eşitsizlik')
kk('K-ESB-03','Üçgenin çizilebilmesi','Kenar ifadelerinin her biri diğer ikisinin toplamından küçük tutularak x için ortak aralık bulunur.','Bir koşulu unutmak; kesirli sınırı yanlış yuvarlamak; eşitliği dahil etmek.','orta','şekilli',4,'esb-ucgen','Üçgen kenarlarında eşitsizlik')
kk('K-ESB-04','Ağırlıklı ortalama tablosu','Katsayılı puanlardan ortalama ifadesi kurulur; iki sınır eşitsizliği ve puan sınırı birlikte değerlendirilir.','Katsayıları yok saymak; puan sınırını unutmak; bölenin yanlış alınması.','orta','tablo',4,'esb-tablo','Tablo verisiyle eşitsizlik')
kk('K-ESB-05','İşlem makinesi zinciri','İki makinenin işlemleri sırayla birleştirilip x’e bağlı tek ifade yazılır; çıkış sınırı eşitsizliğe çevrilir.','İşlem sırasını karıştırmak; sınırı dahil saymak; bir makineyi atlamak.','orta','yeni nesil',4,'esb-makine','Makine zinciri ve eşitsizlik')
kk('K-ESB-06','Yol şemasında süre eşitsizliği','Şemadaki yol ve hızlardan süreler bulunur; varış saati sınırından mola süresi için eşitsizlik kurulur.','Saat–dakika dönüşümü; ortalama hız kullanmak; marjı yanlış tarafa eklemek.','orta','hikâyeli',4,'esb-yol','Yol şeması ve süre sınırı')
kk('K-ESB-07','İki aralıkta ortak tam sayılar','Sayı doğrularındaki aralıklar eşitsizliğe çevrilir; bir aralığın içindeki ifade için yeni eşitsizlik çözülüp ortak değerler bulunur.','Uç noktaların dahil olup olmadığı; negatifle çarpınca yönü çevirmemek; yalnız bir aralığı kullanmak.','zor','şekilli',5,'esb-sayidogru','Sayı doğrusunda aralıklar ve ortak değerler')
kk('K-ESB-08','İki doğrunun grafiği','Her doğrunun denklemi iki noktadan yazılır; fark ve sınır koşulları eşitsizlikle çözülür.','Doğrunun azalan olduğunu atlamak; fark yönünü ters almak; sınır eşitsizliğinde başlangıç değerini unutmak.','zor','hikâyeli',5,'esb-grafik','Doğrusal grafikten eşitsizlik')
kk('K-ESB-09','Aralıklarla sınırlı ölçüler','Her kenarın aralığı sayı doğrusundan okunur; çit uzunluğu ifadesinin sınırları uç değerlerden bulunur.','Uçların dahil olup olmadığını karıştırmak; ifadede katsayıyı yanlış kenara vermek.','zor','hikâyeli',5,'esb-sayidogru','Sayı doğrusunda aralıklar ve ortak değerler')
kk('K-ESB-10','Üç seçenekli tarife tablosu','Üç ücret ifadesi karşılaştırılır; istenen seçeneğin ikisinden de ucuz olduğu aralık bulunur.','Yalnız bir karşılaştırmayı yapmak; eşitliği dahil etmek; fark paydasında yanlış katsayı.','orta','hikâyeli',5,'esb-tablo','Tablo verisiyle eşitsizlik')

# ============ 01 · kolay · mum grafiği ============
b0,t1,b1=30,5,20; egim=Fr(b1-b0,t1); sinir=7
assert egim==-2
tmax=int((sinir-b0)/egim)  # 11
dog=max(t for t in range(0,40) if b0+egim*t>=sinir); assert dog==11 and Fr(b0-sinir)/2==Fr(23,2)
havuz=[(5,'Eğimi, y değerini x değerine bölerek 20 ÷ 5 = 4 bulmuş; 30 − 4t ≥ 7 eşitsizliğinden t ≤ 5,75 bulup 5 yazmış.','islem'),
 (12,'t ≤ 11,5 bulduktan sonra sınırı yukarı yuvarlayıp 12 almış; t = 12 için boy 6 cm olur ve koşul bozulur.','dikkat'),
 (15,'7 cm koşulunu hiç uygulamamış; mumun tamamen bittiği süreyi (30 ÷ 2) yazmış.','dikkat'),
 (23,'Boydaki azalmayı saatte 1 cm sanmış; (30 − 7) ÷ 1 = 23.','islem')]
assert 4-(1)>0 and int(7-30)/(-1)==23 and 30//2==15 and int(30-4*5.75)==7 and int((30-7)/4)==5 and 30-2*12==6<sinir
sx,sy=.42,.115
g='\\fill[gray!10] (0,0) rectangle (%.2f,%.2f);'%(14*sx,35*sy)
for t in range(0,15): g+=f'\\draw[gray!45] ({t*sx:.2f},0) -- ({t*sx:.2f},{35*sy:.2f});'+(f'\\node[below=2pt,font=\\footnotesize] at ({t*sx:.2f},0) {{${t}$}};' if t%2==0 else '')
for y in range(0,36,5): g+=f'\\draw[gray!45] (0,{y*sy:.2f}) -- ({14*sx:.2f},{y*sy:.2f});\\node[left=2pt,font=\\footnotesize] at (0,{y*sy:.2f}) {{${y}$}};'
g+=f'\\draw[thick,-{{Stealth}}] (0,0) -- ({14.6*sx:.2f},0);\\draw[thick,-{{Stealth}}] (0,0) -- (0,{37.5*sy:.2f});'
g+=f'\\node[font=\\footnotesize,anchor=west] at ({14.6*sx:.2f},-.05) {{süre (saat)}};\\node[font=\\footnotesize,anchor=south] at (1.2,{37.5*sy:.2f}) {{mumun boyu (cm)}};'
g+=f'\\draw[very thick,vurgu] (0,{b0*sy:.2f}) -- ({14*sx:.2f},{(b0+egim*14)*sy:.3f});'
for (tt,bb) in ((0,b0),(t1,b1)): g+=f'\\fill[vurgu!70!black] ({tt*sx:.2f},{bb*sy:.2f}) circle (.09);'
q('0001',tipId='esb-grafik',tip='Doğrusal grafikten eşitsizlik',z='kolay',alt='Eşitsizlik Problemleri',kaz='Doğrusal grafikten iki nokta okuyup denklemi kurar ve verilen sınıra göre tam sayı değerini bulur.',kalip='grafik',sekil=TP(g),
 kart='K-ESB-01 · y = 30 − 2t, sınır 7 cm, en çok 11 saat',
 metin='Şekildeki grafik, bir mumun yanmaya başladığı andan itibaren boyunun zamanla değişimini göstermektedir; mum sabit hızla kısalmaktadır. Mumun boyu 7 cm’nin altına inmeden önce söndürülmesi isteniyor ve süre yalnız tam saat olarak ölçülüyor.\nBuna göre mumun boyu 7 cm’den kısa olmamak koşuluyla mum en çok kaç saat yanmış olabilir?',
 dogru=dog,yan=hata(dog,havuz,'B'),istenen='Mumun yanmış olabileceği en büyük tam saat sayısı.',
 ip=['Grafikteki işaretli iki noktanın koordinatlarını oku; mumun her saatte ne kadar kısaldığını bu iki noktadan bul.'],bilgi=[DGR,ESZ],
 ad=[A('Noktaları oku','Grafikteki işaretli noktalar.','(0, 30) ve (5, 20)'),A('Boyun denklemi','Eğim = (20 − 30) ÷ 5 = −2; başlangıç boyu 30 cm.','boy = 30 − 2t'),A('Koşulu yaz ve çöz','Boy 7 cm’den kısa olmamalı.','30 − 2t ≥ 7 → t ≤ 11,5'),A('Tam sayıya çevir','Süre tam saat olduğundan 11,5’i aşmayan en büyük tam sayı alınır.','t = 11')],
 puf='Sınır değeri tam sayı çıkmıyorsa, koşulu bozmayan en büyük tam sayıyı al; yuvarladığın değeri koşula koyup kontrol et.')

# ============ 02 · kolay · mezür ============
su,ust,nb=140,250,6
bos=ust-su; dog=bos//nb; assert bos==110 and dog==18 and su+nb*dog<=ust<su+nb*(dog+1)
havuz=[(19,'110 ÷ 6 = 18,33 bulup sınırı yukarı yuvarlamış; 19 mL’lik 6 bilye seviyeyi 254 mL’ye çıkarır, su taşar.','dikkat'),
 (23,'Boşluk yerine silindirdeki su hacmini (140) 6’ya bölmüş: 140 ÷ 6 ≈ 23.','dikkat'),
 (41,'Silindirin tamamını (250) bilye sayısına bölmüş; var olan suyu hesaba katmamış: 250 ÷ 6 ≈ 41.','dikkat'),
 (110,'Bilye sayısına bölmeyi unutup boşluk hacmini (110) bir bilyenin hacmi sanmış.','dikkat'),
 (16,'Su seviyesini bir çizgi yukarıda (150 mL) okumuş; boşluğu 100 mL bulup 100 ÷ 6 ≈ 16,7 → 16 yazmış.','dikkat')]
assert 140//6==23 and 250//6==41 and 110==ust-su and su+6*19>ust
s=.03; w=1.2; g=f'\\filldraw[fill=vurgu!15,draw=none] (0,0) rectangle ({w},{su*s:.3f});\\draw[thick] (0,{ust*s+.25:.2f}) -- (0,0) -- ({w},0) -- ({w},{ust*s+.25:.2f});\\draw[line width=1.4pt,vurgu!80!black] (0,{su*s:.3f}) -- ({w},{su*s:.3f});'
for m in range(0,ust+1,10):
    L=.26 if m%50==0 else .13
    g+=f'\\draw ({w},{m*s:.3f}) -- ({w+L},{m*s:.3f});'
    g+=f'\\node[anchor=west,font=\\footnotesize] at ({w+.32},{m*s:.3f}) {{${m}$'+(' mL' if m in (0,ust) else '')+'};'
g+=f'\\draw[thick] (-.15,{ust*s:.3f}) -- ({w},{ust*s:.3f});\\node[anchor=east,font=\\footnotesize,align=right] at (-.2,{ust*s:.3f}) {{en üst\\\\çizgi}};'
g+=f'\\node[anchor=north,font=\\footnotesize] at ({w/2},-.15) {{mezür}};'
q('0002',tipId='esb-kap',tip='Ölçekli kapta eşitsizlik',z='kolay',alt='Eşitsizlik Problemleri',kaz='Mezür üzerinde okunan su hacminden boş hacmi bulup eşit hacimli bilyeler için tam sayı sınırı belirler.',kalip='hikâyeli',sekil=TP(g),
 kart='K-ESB-02 · su 140 mL, en üst çizgi 250 mL, 6 bilye, en çok 18 mL',
 metin='Bir fen laboratuvarında, şekildeki dereceli silindirdeki suyun içine hacimleri birbirine eşit 6 bilye atılacaktır. Bilyelerin hepsi suya tamamen batacak ve su, silindirin en üst çizgisini geçerse taşacaktır. Her bilyenin hacmi tam sayı mL’dir.\nBuna göre su taşmaması için bir bilyenin hacmi en çok kaç mL olabilir?',
 dogru=dog,yan=hata(dog,havuz,'B'),istenen='Bir bilyenin hacminin en büyük tam sayı değeri (mL).',
 ip=['Silindirdeki suyun hacmini ve en üst çizginin hangi değere karşılık geldiğini oku; bilyelere ayrılabilecek boşluğu düşün.'],bilgi=[HAC,ESZ],
 ad=[A('Değerleri oku','Şekilden su seviyesi ve en üst çizgi.','su: 140 mL · en üst çizgi: 250 mL'),A('Boşluk','Bilyelerin toplam hacmi bu boşluğu aşamaz.','250 − 140 = 110 mL'),A('Eşitsizlik','Her bilyenin hacmi v mL olsun.','6v ≤ 110 → v ≤ 18,33'),A('Tam sayı','Koşulu bozmayan en büyük tam sayı alınır.','v = 18')],
 puf='Sınırı tam sayıya çevirirken yukarı değil, koşulu bozmayan en büyük tam sayıyı seç.')

# ============ 03 · orta · üçgen ============
f1=lambda x:x-1; f2=lambda x:3*x-7; f3=lambda x:x+6
tri=lambda x,ge=False,sub=(0,1,2):all((f[i](x)<=sum(f[j](x) for j in range(3) if j!=i)) if ge else (f[i](x)<sum(f[j](x) for j in range(3) if j!=i)) for i in sub)
f=[f1,f2,f3]
S=tara(tri,-20,60); dog=sum(S); assert S==list(range(5,12)) and dog==56
inc=sum(tara(lambda x:tri(x,True),-20,60)); assert inc==68
pozit=sum(tara(lambda x:all(g(x)>0 for g in f) and tri(x,False,(1,)),-20,60)); assert pozit==63
ilk2=sum(tara(lambda x:tri(x,False,(0,1)),-20,60)); assert ilk2==66
x5=sum(tara(lambda x:x>5 and tri(x,False,(1,)),-20,60)); assert x5==51
x11=sum(tara(lambda x:x>4 and x<11,-20,60)); assert x11==45   # 3x-7 < 2x+4 hatası (x<11)
ikili=sum(tara(lambda x:x>5 and x<11,-20,60)); assert ikili==40
havuz=[(68,'Üçgen eşitsizliğinde eşitliği de kabul etmiş (x ≤ 12); x = 12 için kenarlar 11, 29, 18 olup 11 + 18 = 29 olduğundan üçgen çizilemez; 5’ten 12’ye değerleri toplamış.','dikkat'),
 (63,'Yalnız kenarların pozitif olması koşullarını kullanıp 3’ten 11’e değerleri toplamış.','bilgi'),
 (66,'En uzun kenarın üçgen eşitsizliğini (x + 6 < 4x − 8) kullanmamış; 1’den 11’e değerleri toplamış.','dikkat'),
 (51,'x > 14/3 koşulunu x > 5 diye yuvarlayıp 5’i dışarıda bırakmış: 6’dan 11’e değerlerin toplamı.','dikkat'),
 (45,'3x − 7 < (x − 1) + (x + 6) eşitsizliğinde sağ tarafı 2x + 4 bulup x < 11 çıkarmış; 5’ten 10’a değerleri toplamış.','islem'),
 (40,'Hem x > 5 yuvarlamasını hem de x < 11 hatasını yapıp 6’dan 10’a değerleri toplamış.','dikkat')]
# şekil: örnek x=8 için ölçekli üçgen (7, 17, 14) — şematik, boyutlar x'e bağlı
a_,b_,c_=f1(8),f2(8),f3(8)  # 7,17,14
import math as m_
sc=.27
bx=b_*sc; cx_=(b_**2+c_**2-a_**2)/(2*b_)*sc; cy_=m_.sqrt((c_*sc)**2-cx_**2)
# köşeler: A(0,0), B(bx,0), C(cx_,cy_); AB=b_ , AC=c_ , BC=a_
g=f'\\draw[thick,fill=vurgu!10] (0,0) -- ({bx:.3f},0) -- ({cx_:.3f},{cy_:.3f}) -- cycle;'
g+=f'\\node[below=3pt] at ({bx/2:.2f},0) {{$3x-7$}};'
g+=f'\\node[above left=1pt] at ({cx_/2:.2f},{cy_/2:.2f}) {{$x+6$}};'
g+=f'\\node[above right=1pt] at ({(bx+cx_)/2:.2f},{cy_/2:.2f}) {{$x-1$}};'
q('0003',tipId='esb-ucgen',tip='Üçgen kenarlarında eşitsizlik',z='orta',alt='Eşitsizlik Problemleri',kaz='Kenar uzunlukları x’e bağlı üçgenin çizilebilmesi için üçgen eşitsizliklerinden x’in tam sayı değerlerini bulup toplar.',kalip='şekilli',sekil=TP(g),
 kart='K-ESB-03 · kenarlar x − 1, 3x − 7, x + 6; x = 5 … 11, toplam 56',
 metin='Şekildeki üçgenin kenar uzunlukları santimetre cinsinden x’e bağlı olarak verilmiştir; şekil, ölçekli çizilmemiştir. x bir tam sayıdır ve verilen uzunluklarla böyle bir üçgenin çizilebilmesi isteniyor.\nBuna göre x’in alabileceği tam sayı değerlerinin toplamı kaçtır?',
 dogru=dog,yan=hata(dog,havuz,'D'),istenen='x’in alabileceği tam sayı değerlerinin toplamı.',
 ip=['Üçgenin üç kenarı için ayrı ayrı bir koşul yazman gerekecek; her koşulu x cinsinden bir eşitsizliğe çevir.'],bilgi=[UCG,SAYI],
 ad=[A('Birinci kenar','x − 1, diğer ikisinin toplamından küçük olmalı.','x − 1 < (3x − 7) + (x + 6) → x > 0'),A('İkinci kenar','3x − 7, diğer ikisinin toplamından küçük olmalı.','3x − 7 < (x − 1) + (x + 6) → x < 12'),A('Üçüncü kenar','x + 6, diğer ikisinin toplamından küçük olmalı.','x + 6 < (x − 1) + (3x − 7) → x > 14/3'),A('Ortak aralık ve topla','Üç koşulu birlikte sağlayan tam sayılar toplanır.','5 ≤ x ≤ 11 → 5 + 6 + … + 11 = 56')],
 puf='Üç koşuldan her biri farklı bir sınır verebilir; sınırları aynı sayı doğrusunda üst üste getirip karşılaştır.')

# ============ 04 · orta · ağırlıklı ortalama tablosu ============
pz=[(1,62),(2,70),(3,74)]; k4=4; top=sum(k for k,_ in pz)+k4; ten=sum(k*p for k,p in pz)
ort=lambda x:Fr(ten+k4*x,top)
S=tara(lambda x:0<=x<=100 and 75<=ort(x)<=85,-50,200); dog=len(S); assert S[0]==82 and S[-1]==100 and dog==19
nocap=len(tara(lambda x:x>=0 and 75<=ort(x)<=85,-50,200)); assert nocap==25
sade=len(tara(lambda x:0<=x<=100 and 75<=Fr(sum(p for _,p in pz)+x,4)<=85,-50,200)); assert sade==7
yuvar=len(tara(lambda x:0<=x<=100 and x>=81 and ort(x)<=85,-50,200)); assert yuvar==20
yuz99=len(tara(lambda x:0<=x<100 and 75<=ort(x)<=85,-50,200)); assert yuz99==18
top9=len(tara(lambda x:0<=x<=100 and 75<=Fr(ten+k4*x,9)<=85,-50,200)); assert top9==23
havuz=[(25,'Puanın en çok 100 olabileceğini unutmuş; 82’den 106’ya 25 değer saymış.','dikkat'),
 (7,'Katsayıları yok sayıp dört puanın düz ortalamasını (÷ 4) almış; x ≥ 94 bulup 94’ten 100’e 7 değer saymış.','dikkat'),
 (20,'4x ≥ 326 eşitsizliğinden x ≥ 81,5 bulup 81’i de almış (aşağı yuvarlamış); 81’den 100’e 20 değer saymış.','dikkat'),
 (18,'Puanın 100’ü aşamayacağını görmüş ama 100’ü dışarıda bırakmış; 82’den 99’a 18 değer saymış.','dikkat'),
 (23,'Katsayılar toplamını 10 yerine 9 almış (dördüncü katsayıyı toplamamış); x = 63’ten 85’e 23 değer saymış.','islem')]
SK=tablo_svg(['Deneme','Katsayı','Puan'],[['1. deneme','1','62'],['2. deneme','2','70'],['3. deneme','3','74'],['4. deneme','4','x']])
q('0004',tipId='esb-tablo',tip='Tablo verisiyle eşitsizlik',z='orta',alt='Eşitsizlik Problemleri',kaz='Tablodaki katsayılı puanlardan ağırlıklı ortalama ifadesi kurup iki sınıra göre tam sayı puanları sayar.',kalip='tablo',sekil=SK,
 kart='K-ESB-04 · katsayılar 1, 2, 3, 4; puanlar 62, 70, 74, x; 75 ≤ ort ≤ 85',
 metin='Bir öğrencinin dört denemesinin katsayıları ve ilk üç denemedeki puanları aşağıdaki tabloda verilmiştir. Ağırlıklı ortalama, her puanın katsayısıyla çarpımlarının toplamının katsayılar toplamına bölünmesiyle bulunur. Dördüncü denemedeki puan olan x, 0 ile 100 arasında (0 ve 100 dahil) bir tam sayıdır. Öğrencinin ağırlıklı ortalamasının 75’ten az, 85’ten fazla olmaması isteniyor.\nBuna göre x kaç farklı değer alabilir?',
 dogru=dog,yan=hata(dog,havuz,'C'),istenen='x’in alabileceği tam sayı değerlerinin sayısı.',
 ip=['Tablodaki her satırdan katsayı ile puanın çarpımını ve toplam katsayıyı bul; ortalamayı x cinsinden yaz.'],bilgi=[AGO,SAYI],
 ad=[A('Ortalamayı yaz','Çarpımlar toplamı ÷ katsayılar toplamı.','(62 + 140 + 222 + 4x) ÷ 10 = (424 + 4x) ÷ 10'),A('Alt sınır','Ortalama 75’ten az olmamalı.','424 + 4x ≥ 750 → x ≥ 81,5 → x ≥ 82'),A('Üst sınır','Ortalama 85’ten fazla olmamalı.','424 + 4x ≤ 850 → x ≤ 106,5'),A('Puan sınırı ve say','Puan en çok 100 olabilir.','82 ≤ x ≤ 100 → 100 − 82 + 1 = 19')],
 puf='Eşitsizlikten çıkan sınırı, sorudaki ek koşullarla (burada puanın alabileceği değerlerle) mutlaka karşılaştır.')

# ============ 05 · orta · iki makine ============
a1,b1,a2,b2=2,-7,3,5   # I: 2x-7 ; II: 3y+5
out=lambda x:a2*(a1*x+b1)+b2; ters=lambda x:a1*(a2*x+b2)+b1
lo_,hi_=50,110
S=tara(lambda x:lo_<out(x)<hi_,-100,100); dog=len(S); assert S==list(range(12,21)) and dog==9 and out(x:=11)==50
sw=len(tara(lambda x:lo_<ters(x)<hi_,-100,100)); assert sw==10
inc=len(tara(lambda x:lo_<=out(x)<=hi_,-100,100)); assert inc==11
soloII=len(tara(lambda x:lo_<a2*x+b2<hi_,-100,100)); assert soloII==19
soloI=len(tara(lambda x:lo_<a1*x+b1<hi_,-100,100)); assert soloI==30
havuz=[(10,'İşlem sırasını karıştırmış: önce Makine II’yi, sonra Makine I’i uygulamış; 2(3x + 5) − 7 = 6x + 3 için 8’den 17’ye 10 değer saymış.','dikkat'),
 (11,'Sonucun 50 ve 110’a eşit olmasına da izin vermiş; x = 11 için çıkış 50’dir ve “50’den büyük” koşulunu sağlamaz.','dikkat'),
 (19,'Yalnız Makine II’yi uygulamış (3x + 5); 15 < x < 35 aralığındaki 19 değeri saymış.','dikkat'),
 (30,'Yalnız Makine I’i uygulamış (2x − 7); 28,5 < x < 58,5 aralığındaki 30 değeri saymış.','dikkat')]
assert tara(lambda x:lo_<a1*x+b1<hi_,-100,100)==list(range(29,59))
bx=lambda x,y,txt,w=2.5,h=1.4: f'\\node[draw,thick,rounded corners=3pt,fill=vurgu!12,minimum width={w}cm,minimum height={h}cm,align=center,inner sep=3pt] at ({x},{y}) {{{txt}}};'
g=bx(0,0,'Girdi\\\\$x$',1.4,1.1)+bx(3.1,0,'\\textbf{Makine I}\\\\2 ile çarp,\\\\sonra 7 çıkar',2.5,1.7)+bx(6.7,0,'\\textbf{Makine II}\\\\3 ile çarp,\\\\sonra 5 ekle',2.5,1.7)+bx(9.7,0,'Sonuç',1.5,1.1)
g+='\\draw[-{Stealth},thick] (0.7,0) -- (1.85,0);\\draw[-{Stealth},thick] (4.35,0) -- (5.45,0);\\draw[-{Stealth},thick] (7.95,0) -- (8.95,0);'
q('0005',tipId='esb-makine',tip='Makine zinciri ve eşitsizlik',z='orta',alt='Eşitsizlik Çözme',kaz='İki işlem makinesini sırayla uygulayıp çıkışın verilen aralıkta kalmasını sağlayan tam sayıları sayar.',kalip='yeni nesil',sekil=TP(g),
 kart='K-ESB-05 · 2x − 7, ardından 3y + 5; 50 < sonuç < 110',
 metin='Şekilde, iki makinenin yaptığı işlemler gösterilmiştir. Makine I’e giren x tam sayısı, makinenin işlemlerinden geçtikten sonra Makine II’ye girer; Makine II’den çıkan sayı “Sonuç” olarak yazılır. Sonuç 50’den büyük ve 110’dan küçük olmaktadır.\nBuna göre x kaç farklı tam sayı değeri alabilir?',
 dogru=dog,yan=hata(dog,havuz,'A'),istenen='x’in alabileceği tam sayı değerlerinin sayısı.',
 ip=['Makinelerin işlemlerinin hangi sırayla uygulandığına dikkat ederek x’ten sonuca giden tek bir ifade yaz.'],bilgi=[ISL,ESZ],
 ad=[A('Makine I’in çıkışı','x’e önce çarpma, sonra çıkarma uygulanır.','2x − 7'),A('Makine II’nin çıkışı','Bu sonuç Makine II’ye girer.','3(2x − 7) + 5 = 6x − 16'),A('Eşitsizliği kur','Sonuç 50’den büyük, 110’dan küçük.','50 < 6x − 16 < 110 → 11 < x < 21'),A('Say','Uçlar dahil değil.','x = 12, 13, …, 20 → 9 değer')],
 puf='Çarpma ve toplama işlemlerinin sırası değişirse çıkan ifade de değişir; sırayı şekildeki oklardan takip et.')

# ============ 06 · orta · yol şeması ============
def hm(t): return f'{t//60:02d}:{t%60:02d}'
dep=8*60+30; d1,v1,d2,v2=150,75,120,80; meet=13*60+10; marj=25
t1=d1*60//v1; t2=d2*60//v2; assert (t1,t2)==(120,90) and d1*60%v1==0 and d2*60%v2==0
dog=meet-marj-dep-(t1+t2); assert dog==45 and hm(dep+t1+t2)=='12:00' and hm(meet-marj)=='12:45'
e1=meet-marj-(dep+3*60+50); e2=meet-dep-(t1+t2); e3=meet+marj-dep-(t1+t2); e4=meet-marj-dep-(d1+d2)*60//v1
assert (e1,e2,e3,e4)==(25,70,95,39)
assert meet-2*marj-dep-(t1+t2)==20 and (12*60+35)-(dep+t1+t2)==35
havuz=[(25,'3,5 saati “3 saat 50 dakika” diye yazmış; varış 12:20 olur ve kalan 25 dakikayı mola sanmış.','islem'),
 (39,'İki yolu da 75 km/sa hızla gidilmiş gibi hesaplamış: 270 ÷ 75 = 3,6 saat = 3 saat 36 dakika.','dikkat'),
 (70,'Toplantıdan önce varılması gereken 25 dakikalık payı unutmuş; toplantı saatine göre kalan süreyi yazmış.','dikkat'),
 (95,'25 dakikalık payı çıkarmak yerine toplantı saatine eklemiş.','dikkat'),
 (20,'25 dakikalık payı iki kez çıkarmış: 13:10 − 50 dk = 12:20; 12:00’dan 20 dakika kalır.','dikkat'),
 (35,'13:10’dan 25 dakikayı çıkarırken 12:35 bulmuş (60’lık dönüşümü yapamamış); 12:00’dan 35 dakika kalır.','dikkat')]
sx_=.036; yy=0
def nd(xx,txt1,txt2): return f'\\fill[vurgu] ({xx},0) circle (.12);\\node[above=6pt,align=center] at ({xx},0) {{{txt1}}};\\node[below=6pt,align=center,font=\\small] at ({xx},0) {{{txt2}}};'
g='\\draw[line width=2pt] (0,0) -- (8.6,0);'+nd(0,'Başlangıç','çıkış 08:30')+nd(4.3,'Mola yeri','')+nd(8.6,'Toplantı yeri','')
g+='\\draw[thick,<->] (0.15,1.25) -- (4.15,1.25);\\node[above] at (2.15,1.25) {150 km · 75 km/sa};\\draw[thick,<->] (4.45,1.25) -- (8.45,1.25);\\node[above] at (6.45,1.25) {120 km · 80 km/sa};'
q('0006',tipId='esb-yol',tip='Yol şeması ve süre sınırı',z='orta',alt='Eşitsizlik Problemleri',kaz='Yol şemasındaki mesafe ve hızlardan süreleri bulup varış saati sınırına göre mola süresinin en büyük tam sayı değerini belirler.',kalip='hikâyeli',sekil=TP(g),
 kart='K-ESB-06 · 150 km @ 75, 120 km @ 80, çıkış 08:30, toplantı 13:10, pay 25 dk; mola ≤ 45 dk',
 metin='Bir şirketin servis aracı, şekilde gösterilen yolu her bölümde sabit hızla giderek tamamlayacaktır. Araç, iki yol bölümünün birleştiği mola yerinde tam sayı dakika kadar bekleyecektir. Toplantı 13:10’da başlayacak olup araç toplantı yerine toplantı başlamadan en az 25 dakika önce varmak zorundadır.\nBuna göre mola süresi en çok kaç dakika olabilir?',
 dogru=dog,yan=hata(dog,havuz,'E'),istenen='Mola süresinin en büyük tam sayı değeri (dakika).',
 ip=['Şekildeki iki bölümün süresini ayrı ayrı hesaplamadan önce saatleri dakikaya çevirmeyi düşün.'],bilgi=[YOL,ESZ],
 ad=[A('Sürüş süreleri','Süre = yol ÷ hız.','150 ÷ 75 = 2 saat · 120 ÷ 80 = 1,5 saat'),A('Mola yok varsayımı','08:30’dan 3,5 saat sonrası.','08:30 + 3 sa 30 dk = 12:00'),A('Varış sınırı','Toplantıdan en az 25 dakika önce.','13:10 − 25 dk = 12:45'),A('Eşitsizlik','Mola süresi m dakika olsun.','12:00 + m ≤ 12:45 → m ≤ 45')],
 puf='Saatleri tek bir birime (dakika) çevirince sınır ve süreler aynı ölçekte karşılaştırılır.')

# ============ 07 · zor · iki aralık ============
Ka=(-1,6); La=(-3,9)   # K: (-1, 6] ; L: [-3, 9)
inK=lambda x:Ka[0]<x<=Ka[1]; inL=lambda x:La[0]<=x<La[1]
S=tara(lambda x:inK(x) and inL(3-2*x),-30,30); dog=sum(S); assert S==[0,1,2,3] and dog==6
e_inc=sum(tara(lambda x:Ka[0]<=x<=Ka[1] and inL(3-2*x),-30,30)); assert e_inc==5
e_solL=sum(tara(lambda x:inL(3-2*x),-30,30)); assert e_solL==sum(range(-2,4))==3
e_isaret=sum(tara(lambda x:inK(x) and inL(2*x-3),-30,30)); assert e_isaret==sum(range(0,6))==15
e_L=sum(tara(lambda x:inK(x) and La[0]<x<=La[1],-30,30)); assert e_L==sum(range(0,7))==21
havuz=[(3,'Yalnız L koşulunu kullanmış (−2 < x ≤ 3 → −2, …, 3); K aralığındaki alt sınırı (−1) hesaba katmamıştır.','dikkat'),
 (5,'K aralığının sol ucunu (−1) dahil sanıp −1’i de saymış: −1 + 0 + 1 + 2 + 3.','dikkat'),
 (15,'3 − 2x yerine 2x − 3 ifadesini L’ye yerleştirmiş (0 ≤ x < 6); K ile ortak değerlerin toplamını 15 bulmuş.','islem'),
 (21,'Yalnız x’in K ve L’de birlikte bulunmasını istemiş (0 ≤ x ≤ 6 gibi) ve ifadeyi dönüştürmemiş: 0 + 1 + … + 6.','dikkat')]
s=.40; X0,X1=-8,10
def aralik(y,lo,hi,loac,hiac,ad):
    t=f'\\draw[-{{Stealth}}] ({(X0-.3)*s:.2f},{y}) -- ({(X1+.5)*s:.2f},{y});'
    for i in range(X0,X1+1): t+=f'\\draw ({i*s:.2f},{y-.07}) -- ({i*s:.2f},{y+.07});\\node[below=3pt,font=\\scriptsize] at ({i*s:.2f},{y-.07}) {{${i}$}};'
    t+=f'\\draw[line width=3pt,vurgu!55] ({lo*s:.2f},{y+.0}) -- ({hi*s:.2f},{y});'
    for v,ac in ((lo,loac),(hi,hiac)): t+=f'\\filldraw[fill={"white" if ac else "vurgu!70!black"},draw=vurgu!70!black,thick] ({v*s:.2f},{y}) circle (.11);'
    t+=f'\\node[anchor=east,font=\\normalsize] at ({(X0-.45)*s:.2f},{y+.0}) {{{ad}}};'
    return t
g=aralik(0,Ka[0],Ka[1],True,False,'K')+aralik(-1.35,La[0],La[1],False,True,'L')
q('0007',tipId='esb-sayidogru',tip='Sayı doğrusunda aralıklar ve ortak değerler',z='zor',alt='Aralık İşlemleri',kaz='Sayı doğrularında verilen iki aralığı eşitsizliğe çevirip, bir aralığa ait ifade için kurulan eşitsizlikle ortak tam sayı değerlerinin toplamını bulur.',kalip='şekilli',sekil=TP(g),
 kart='K-ESB-07 · K = (−1, 6], L = [−3, 9); x ∈ K ve 3 − 2x ∈ L → x = 0, 1, 2, 3',
 metin='Şekildeki sayı doğrularında K ve L aralıkları gösterilmiştir; içi dolu nokta ucun aralığa dahil olduğunu, içi boş nokta ise dahil olmadığını belirtir. x bir tam sayıdır; x sayısı K aralığına, (3 − 2x) sayısı da L aralığına aittir.\nBuna göre x’in alabileceği değerlerin toplamı kaçtır?',
 dogru=dog,yan=hata(dog,havuz,'C'),istenen='x’in alabileceği tam sayı değerlerinin toplamı.',
 ip=['K ve L aralıklarını ayrı ayrı eşitsizlik olarak yaz; ikinci koşuldaki ifadeyi L’nin eşitsizliğinde yerine koy.'],bilgi=[ARL,ESZ],
 ad=[A('Aralıkları yaz','Boş nokta ucu dışarıda, dolu nokta içeride bırakır.','K: −1 < x ≤ 6 · L: −3 ≤ y < 9'),A('İfadeyi yerine koy','y = 3 − 2x alınır.','−3 ≤ 3 − 2x < 9'),A('x için çöz','Her yandan 3 çıkarılır, sonra −2’ye bölünür; yön değişir.','−6 ≤ −2x < 6 → −3 < x ≤ 3'),A('K ile ortak','K: −1 < x ≤ 6 ile kesiştir.','−1 < x ≤ 3 → x = 0, 1, 2, 3'),A('Topla','Bulunan tam sayılar toplanır.','0 + 1 + 2 + 3 = 6')],
 puf='Bir ifadeyi aralıkta yerine koyduğunda uç noktaların dahil olup olmaması aynen korunur; yalnız negatif çarpanda yön değişir.')

# ============ 08 · zor · iki depo grafiği ============
Pa=(40,Fr(100-40,10)); Qa=(190,Fr(150-190,10))   # P: 40+6t ; Q: 190-4t
Pf=lambda t:Pa[0]+Pa[1]*t; Qf=lambda t:Qa[0]+Qa[1]*t
assert Pa[1]==6 and Qa[1]==-4 and Pf(15)==Qf(15)==130
S=tara(lambda t:0<=t<=22 and Pf(t)-Qf(t)>=20 and Pf(t)<=160,-5,40); dog=sum(S); assert S==[17,18,19,20] and dog==74
tp=lambda f:sum(tara(f,-5,40))
e_fark=tp(lambda t:0<=t<=22 and Pf(t)>Qf(t) and Pf(t)<=160); assert e_fark==90
e_ters=tp(lambda t:0<=t<=22 and Qf(t)-Pf(t)>=20 and Pf(t)<=160); assert e_ters==91
e_sin=tp(lambda t:0<=t<=22 and Pf(t)-Qf(t)>=20 and 6*t<=160); assert e_sin==117
e_kesin=tp(lambda t:0<=t<=22 and Pf(t)-Qf(t)>20 and Pf(t)<=160); assert e_kesin==57
e_kP=tp(lambda t:0<=t<=22 and Pf(t)-Qf(t)>=20 and Pf(t)<160); assert e_kP==54
e_ikisi=tp(lambda t:0<=t<=22 and Pf(t)-Qf(t)>20 and Pf(t)<160); assert e_ikisi==37
havuz=[(37,'Hem “en az 20 litre fazla” hem de “160 litreyi geçmemiş” koşullarında eşitliği dışarıda bırakmış; 18 + 19 = 37.','dikkat'),
 (54,'“160 litreyi geçmemiş” koşulunda eşitliği dışarıda bırakmış (P < 160); 17 + 18 + 19 = 54.','dikkat'),
 (57,'“En az 20 litre fazla” koşulunda eşitliği dışarıda bırakmış (10t − 150 > 20 → t > 17); 18 + 19 + 20 = 57.','dikkat'),
 (90,'P’nin Q’dan en az 20 litre fazla olması koşulunu unutup yalnız P > Q (t > 15) almış; 16’dan 20’ye değerleri toplamış.','dikkat'),
 (91,'Farkı ters kurmuş (Q − P ≥ 20 → t ≤ 13); 0’dan 13’e değerleri toplamış.','islem'),
 (117,'P ≤ 160 koşulunda başlangıç değerini (40) hesaba katmamış: 6t ≤ 160 → t ≤ 26,6; grafikteki süreyle sınırlayıp 17’den 22’ye değerleri toplamış.','islem')]
sx,sy=.30,.0185
g=''
for t in range(0,23,2): g+=f'\\draw[gray!45] ({t*sx:.2f},0) -- ({t*sx:.2f},{200*sy:.2f});\\node[below=2pt,font=\\footnotesize] at ({t*sx:.2f},0) {{${t}$}};'
for y in range(0,201,10): g+=f'\\draw[gray!{45 if y%20==0 else 25}] (0,{y*sy:.3f}) -- ({22*sx:.2f},{y*sy:.3f});'+(f'\\node[left=2pt,font=\\footnotesize] at (0,{y*sy:.3f}) {{${y}$}};' if y%20==0 else '')
g+=f'\\draw[thick,-{{Stealth}}] (0,0) -- ({23*sx:.2f},0);\\draw[thick,-{{Stealth}}] (0,0) -- (0,{210*sy:.2f});'
g+=f'\\node[font=\\footnotesize,anchor=west] at ({23*sx:.2f},0) {{dakika}};\\node[font=\\footnotesize,anchor=south] at (1.0,{210*sy:.2f}) {{su miktarı (litre)}};'
for nm,F_ in (('P',Pf),('Q',Qf)):
    g+=f'\\draw[very thick,vurgu] (0,{F_(0)*sy:.3f}) -- ({22*sx:.2f},{F_(22)*sy:.3f});\\node[font=\\small\\bfseries,anchor=south west] at ({22*sx:.2f},{F_(22)*sy:.3f}) {{{nm}}};'
    for tt in (0,10): g+=f'\\fill[vurgu!70!black] ({tt*sx:.2f},{F_(tt)*sy:.3f}) circle (.09);'
q('0008',tipId='esb-grafik',tip='Doğrusal grafikten eşitsizlik',z='zor',alt='Eşitsizlik Problemleri',kaz='İki doğrusal grafikten denklemleri kurup fark ve üst sınır koşullarını eşitsizlikle çözerek tam dakika değerlerinin toplamını bulur.',kalip='hikâyeli',sekil=TP(g),
 kart='K-ESB-08 · P = 40 + 6t, Q = 190 − 4t; P − Q ≥ 20 ve P ≤ 160 → t = 17, …, 20, toplam 74',
 metin='Bir tesisteki P deposu doldurulurken Q deposu boşaltılmaktadır. Şekildeki grafikte, iki depodaki su miktarının dakikaya göre değişimi gösterilmiştir; her iki değişim de doğrusaldır ve işlem 22 dakika sürmüştür. Bir tam dakikada, P’deki su Q’dakinden en az 20 litre fazla olmuş ve P’deki su 160 litreyi geçmemiştir.\nBuna göre bu koşulların birlikte sağlandığı tam dakikaların toplamı kaçtır?',
 dogru=dog,yan=hata(dog,havuz,'D'),istenen='Koşulların birlikte sağlandığı tam dakika değerlerinin toplamı.',
 ip=['Her depo için grafikteki iki işaretli noktadan dakikaya bağlı su miktarı ifadesini yaz; sonra iki koşulu ayrı ayrı eşitsizliğe çevir.'],bilgi=[DGR,SAYI],
 ad=[A('P’nin ifadesi','(0, 40) ve (10, 100) noktalarından eğim 6.','P = 40 + 6t'),A('Q’nun ifadesi','(0, 190) ve (10, 150) noktalarından eğim −4.','Q = 190 − 4t'),A('Fark koşulu','P, Q’dan en az 20 litre fazla.','(40 + 6t) − (190 − 4t) ≥ 20 → t ≥ 17'),A('Üst sınır','P en çok 160 litre.','40 + 6t ≤ 160 → t ≤ 20'),A('Topla','17 ≤ t ≤ 20 ve t tam sayı.','17 + 18 + 19 + 20 = 74')],
 puf='Her koşul t için ayrı bir sınır verir; sınırları tek bir sayı doğrusunda birlikte değerlendir ve grafiğin çizildiği süreyi de kontrol et.')

# ============ 09 · zor · çit ve iki aralık ============
Ar=(4,7); Br=(9,13)   # a ∈ [4,7) , b ∈ (9,13]
inA=lambda v:Ar[0]<=v<Ar[1]; inB=lambda v:Br[0]<v<=Br[1]
# çit = 2b + a ; aralık (2*9+4, 2*13+7) = (22,33) uçlar ulaşılamaz
lo=2*Br[0]+Ar[0]; hi=2*Br[1]+Ar[1]; assert (lo,hi)==(22,33)
dog=lo+1; assert dog==23
e_inc=lo; e_yer=2*Ar[0]+Br[0]+1; e_yerinc=2*Ar[0]+Br[0]; e_iki=Ar[0]+Br[0]+1
assert (e_inc,e_yer,e_yerinc,e_iki)==(22,18,17,14)
ok=set()
for ai in range(0,3001):
    a=Fr(ai,1000)+4
    if not inA(a): continue
    for bi in range(1,4001,1):
        b=Fr(bi,1000)+9
        if inB(b):
            v=2*b+a
            if v.denominator==1: ok.add(int(v))
assert min(ok)==23 and max(ok)==32 and sorted(ok)==list(range(23,33)),sorted(ok)
havuz=[(14,'Tel uzunluğunu a + b sanmış (iki kenar); 9 + 4 = 13’ten büyük olduğundan en küçük tam sayıyı 14 bulmuş.','dikkat'),
 (17,'Çiti 2a + b sanıp (2 · 4 + 9 = 17) alt ucu ulaşılabilir kabul etmiş.','dikkat'),
 (18,'Çiti 2a + b sanmış; b > 9 olduğundan 17’ye ulaşılamaz, 18 bulmuş.','dikkat'),
 (22,'Alt ucun (2 · 9 + 4 = 22) ulaşılabilir olduğunu sanmış; oysa b > 9 olduğundan T, 22’ye ulaşamaz.','dikkat')]
s=.5; X0,X1=3,14
def ar2(y,lo,hi,loac,hiac,ad):
    t=f'\\draw[-{{Stealth}}] ({(X0-.3)*s:.2f},{y}) -- ({(X1+.5)*s:.2f},{y});'
    for i in range(X0,X1+1): t+=f'\\draw ({i*s:.2f},{y-.07}) -- ({i*s:.2f},{y+.07});\\node[below=3pt,font=\\scriptsize] at ({i*s:.2f},{y-.07}) {{${i}$}};'
    t+=f'\\draw[line width=3pt,vurgu!55] ({lo*s:.2f},{y}) -- ({hi*s:.2f},{y});'
    for v,ac in ((lo,loac),(hi,hiac)): t+=f'\\filldraw[fill={"white" if ac else "vurgu!70!black"},draw=vurgu!70!black,thick] ({v*s:.2f},{y}) circle (.11);'
    t+=f'\\node[anchor=east,font=\\normalsize] at ({(X0-.45)*s:.2f},{y}) {{{ad}}};'
    return t
W_,H_=3.6,1.9; x0=(X0+1)*s+.2
g=f'\\draw[thick] ({x0},3.9) rectangle ({x0+W_+0.0},{3.9+H_});'
g+=f'\\draw[line width=2.2pt,vurgu!80!black] ({x0},{3.9+H_}) -- ({x0+W_},{3.9+H_}) -- ({x0+W_},3.9) -- ({x0},3.9);'
g+=f'\\draw[decorate,decoration={{snake,amplitude=1.2pt,segment length=7pt}},thick] ({x0-.22},3.9) -- ({x0-.22},{3.9+H_});\\node[anchor=east,font=\\footnotesize] at ({x0-.35},{3.9+H_/2}) {{nehir}};'
g+=f'\\node[above=2pt] at ({x0+W_/2},{3.9+H_}) {{$b$}};\\node[right=2pt] at ({x0+W_},{3.9+H_/2}) {{$a$}};'
g+=f'\\node[anchor=west,font=\\footnotesize,align=left] at ({x0+W_+.9},{3.9+H_/2}) {{kalın çizgi:\\\\çit}};'
g+=ar2(2.5,Ar[0],Ar[1],False,True,'$a$')+ar2(1.0,Br[0],Br[1],True,False,'$b$')
q('0009',tipId='esb-sayidogru',tip='Sayı doğrusunda aralıklar ve ortak değerler',z='zor',alt='Aralık İşlemleri',kaz='Kenar uzunluklarının sayı doğrusunda verilen aralıklarından, belirli bir toplam ifadesinin alabileceği en küçük tam sayı değerini bulur.',kalip='hikâyeli',sekil=TP(g),
 kart='K-ESB-09 · a ∈ [4, 7), b ∈ (9, 13]; çit = 2b + a ∈ (22, 33) → en küçük tam sayı 23',
 metin='Dikdörtgen biçimli bir tarlanın bir kısa kenarı nehre bitişiktir; çit yalnız nehir tarafı dışındaki üç kenara çekilecektir. Şekilde, tarlanın kısa ve uzun kenarlarının metre cinsinden a ve b uzunluklarının alabileceği değerler sayı doğrularında gösterilmiştir (içi boş nokta uca dahil değildir). Çit için gereken telin uzunluğu tam sayı metre olarak ölçülmüştür.\nBuna göre tel uzunluğu en az kaç metre olabilir?',
 dogru=dog,yan=hata(dog,havuz,'E'),istenen='Telin alabileceği en küçük tam sayı değeri (metre).',
 ip=['Çitin hangi kenarlara çekildiğine bakarak tel uzunluğunu a ve b cinsinden yaz; sonra a ve b’nin aralıklarından bu ifadenin aralığını bul.'],bilgi=[KEN,SAYI],
 ad=[A('Tel uzunluğu','Nehir kenarı dışında iki uzun, bir kısa kenar çitle çevrilir.','T = 2b + a'),A('Aralıkları yaz','İçi dolu uç dahil, içi boş uç dahil değil.','4 ≤ a < 7 · 9 < b ≤ 13'),A('2b’nin aralığı','Eşitsizlik 2 ile çarpılır.','18 < 2b ≤ 26'),A('Toplam aralığı','Aynı yönlü eşitsizlikler toplanır; alt uç b yüzünden, üst uç a yüzünden dahil olmaz.','4 + 18 < T < 26 + 7 → 22 < T < 33'),A('En küçük tam sayı','22’ye ulaşılamaz; 22’den büyük en küçük tam sayı alınır.','T > 22 → en küçük T = 23')],
 puf='Bir toplamın alt ve üst uçlarının dahil olup olmadığı, o uca katkı yapan aralıkların uçlarına bakılarak ayrı ayrı belirlenir.')

# ============ 10 · zor · kiralama tablosu ============
Fa=(300,6); Fb=(340,4); Fc=(385,3)
cost=lambda F,x:F[0]+F[1]*x
S=tara(lambda x:x>=0 and cost(Fb,x)<cost(Fa,x) and cost(Fb,x)<cost(Fc,x),-5,400); dog=len(S); assert S==list(range(21,45)) and dog==24
e_inc=len(tara(lambda x:x>=0 and cost(Fb,x)<=cost(Fa,x) and cost(Fb,x)<=cost(Fc,x),-5,400)); assert e_inc==26
e_c=len(tara(lambda x:x>=0 and cost(Fb,x)<cost(Fc,x),-5,400)); assert e_c==45
e_pay=len(tara(lambda x:x>=0 and Fr(Fb[0]-Fa[0],Fa[1])<x and cost(Fb,x)<cost(Fc,x),-5,400)); assert e_pay==38
e_yar=len(tara(lambda x:x>=0 and cost(Fb,x)<cost(Fa,x) and cost(Fb,x)<=cost(Fc,x),-5,400)); assert e_yar==25
havuz=[(25,'Birinci koşulda sınırı dışarıda (x > 20), ikincisinde dahil (x ≤ 45) bırakarak 21’den 45’e 25 değer saymış; ikisi de kesindir.','dikkat'),
 (26,'“Daha ucuz” yerine “aynı ya da daha ucuz” koşulunu almış (20 ≤ x ≤ 45); 26 değer saymış.','dikkat'),
 (38,'A ile karşılaştırmada km başına farkı (6 − 4 = 2) yerine yalnız A’nın km ücretiyle (6) bölmüş: x > 40 ÷ 6 ≈ 6,67; 7’den 44’e 38 değer saymış.','islem'),
 (45,'B’yi yalnız C ile karşılaştırmış (x < 45); A ile karşılaştırmayı yapmadan 0’dan 44’e 45 değer saymış.','dikkat')]
SK=tablo_svg(['Firma','Günlük sabit ücret (TL)','Kilometre başına ücret (TL)'],[['A','300','6'],['B','340','4'],['C','385','3']])
q('0010',tipId='esb-tablo',tip='Tablo verisiyle eşitsizlik',z='orta',alt='Eşitsizlik Problemleri',kaz='Tablodaki üç ücret ifadesini karşılaştırıp bir seçeneğin diğer ikisinden ucuz olduğu tam sayı kilometre değerlerini sayar.',kalip='hikâyeli',sekil=SK,
 kart='K-ESB-10 · 300 + 6x, 340 + 4x, 385 + 3x; B en ucuz → 21 ≤ x ≤ 44',
 metin='Bir araç kiralama şirketinin üç firmasının fiyat tarifeleri aşağıdaki tabloda verilmiştir. Her firmada ödenecek toplam ücret, günlük sabit ücret ile gidilen kilometre başına ücretin kilometre sayısıyla çarpımının toplamıdır. Bir müşteri aracı tek günlüğüne kiralayacak ve tam sayı kadar kilometre yol gidecektir.\nBuna göre B firmasının A ve C firmalarının ikisinden de daha ucuz olduğu kaç farklı kilometre değeri vardır?',
 dogru=dog,yan=hata(dog,havuz,'A'),istenen='B firmasının en ucuz olduğu tam sayı kilometre değerlerinin sayısı.',
 ip=['Tablodaki değerlerle her firmanın x kilometre için toplam ücretini yaz; B’yi diğer iki firmayla ayrı ayrı karşılaştır.'],bilgi=[TAR,SAYI],
 ad=[A('Ücretleri yaz','Sabit ücret + km başına ücret × x.','A: 300 + 6x · B: 340 + 4x · C: 385 + 3x'),A('B, A’dan ucuz','Eşitsizliği çöz.','340 + 4x < 300 + 6x → x > 20'),A('B, C’den ucuz','Eşitsizliği çöz.','340 + 4x < 385 + 3x → x < 45'),A('Ortak aralık','İki koşul birlikte.','20 < x < 45'),A('Say','21’den 44’e tam sayılar.','44 − 21 + 1 = 24')],
 puf='“İkisinden de” ifadesi iki ayrı karşılaştırmanın birlikte sağlanması demektir; sonucu iki sınırın arasında ara.')

bitir(P,'esitsizsekb','mat|Basit Eşitsizlikler')
