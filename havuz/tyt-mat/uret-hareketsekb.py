"""Hareket Hız Problemleri · ŞEKİLLİ ek paket b (10 soru): şekil/tablo çözüm verisini taşır (hız–zaman grafiği alanı yok); her doğru ve çeldirici değer assert'lidir. Kardeş yok, ipucu 1."""
import sys,os,math,itertools
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
from math import cos,sin,radians
H.KONU='Hareket Hız Problemleri'
UK='prob|Hareket Hız Problemleri'
P=Parti('hareketsekb','Hareket Hız Problemleri',UK)
KY='ÖSYM 2018–2026 TYT Matematik (şekilli/tablolu hareket soruları; yalnız mantık) · MEB 9. sınıf problemler'
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)
def fig(body): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'+body+'\n\\end{tikzpicture}')
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)

ORT=B('Ortalama hız','ortalama hız, toplam yolun toplam süreye bölümüdür; hızların ortalaması değildir. Örnek: 30 km yolu 1 saatte, 30 km yolu 2 saatte alan aracın ortalama hızı 60 ÷ 3 = 20 km/sa’tir')
EKS=B('En kısa yol','bir noktadan diğerine gitmek için olası yolların uzunlukları tek tek toplanır ve en küçüğü seçilir; kısa görünen sokaklar toplamı küçük yapmayabilir. Örnek: 5+9 ve 8+7 uzunluklu iki yoldan 14 olan kısadır')
GAN=B('Zaman çizelgesi','çizelgede boyalı aralık hareket süresini, boş aralık beklemeyi gösterir; ortalama hızda bekleme süresi de toplam süreye katılır. Örnek: 2 saat 40 km/sa ile gidip 1 saat bekleyen araç 80 km’yi 3 saatte almış sayılır')
KM=B('Kilometre sayacı','iki okuma arasındaki fark alınan yoldur; yol bölü süre hızı verir. Saat ve dakika farkı saate çevrilirken 60 dakikanın 1 saat olduğu unutulmaz. Örnek: 45 dakika, 3/4 saattir')
PIS=B('Dikdörtgen pistte zıt yön','zıt yönlerde giden iki hareketlinin pist boyunca birbirine yaklaşma hızı hızlarının toplamıdır; ilk karşılaşmadan sonra her karşılaşma arasında toplam bir çevre yol alırlar. Örnek: çevre 120 m, hızlar 1 ve 2 m/sn ise karşılaşmalar arası 40 sn’dir')
TUR=B('Tırmanış ve iniş süreleri','farklı eğimli bölümlerde hız farklıdır; her bölümün süresi o bölümün yolu bölü o bölümün hızıyla bulunup toplanır. Örnek: 6 km’yi 12 km/sa ile ve 6 km’yi 24 km/sa ile alan 0,5 + 0,25 = 0,75 saatte gider')
DIR=B('Eşit aralıklı direkler','ardışık n direk arasında n − 1 aralık vardır; yol = aralık sayısı × bir aralığın uzunluğu. km/sa değeri 3,6 ile çarpılarak m/sn’den bulunur. Örnek: 6 direk arası 5 aralıktır; 10 m/sn hız 36 km/sa’tir')
ORH=B('Ortalama hız denetimi','iki kamera arasındaki yolun izin verilen hıza bölünmesi, bu yolu hız sınırıyla gitmenin süresini verir; daha kısa sürede alan araç sınırı aşmış sayılır. Örnek: 10 km’lik yolda 60 km/sa sınırında en az 10 dakika gerekir')
TEK=B('Tekerlek çevresi','tekerlek bir devirde çevresi kadar yol alır; çevre = 2πr; bir dakikadaki devir sayısı ile çevrenin çarpımı dakikadaki yolu verir. Örnek: çevresi 2 m olan tekerlek dakikada 10 devirle 20 m yol alır')
IKI=B('Aynı anda varma','aynı anda çıkıp aynı anda varan iki hareketlinin süreleri eşittir; bu süre bir hareketlinin yolu ve hızından bulunur, durduğu süre hareket süresinden çıkarılır. Örnek: toplam 60 dakikada 10 dakika bekleyen hareketli 50 dakika yol alır')

kartla('K-HSB-01','Üç bölümlü yol şeması','Her bölümün yolu ve hızı şemadan okunur; bölüm süreleri toplanır, toplam yol toplam süreye bölünür.','Hızların ortalamasını almak; bir bölümün süresini atlamak.','kolay','hikâyeli',4,'hrb-sema','Yol şeması ve ortalama hız')
kartla('K-HSB-02','Sokak ızgarası','Olası yolların uzunlukları ayrı ayrı toplanıp en küçüğü seçilir; km/sa m/sn’ye çevrilerek süre bulunur.','Önce yatay gitmeyi en kısa sanmak; km/sa ile m/sn’yi karıştırmak.','orta','hikâyeli',4,'hrb-izgara','Sokak ızgarası ve en kısa yol')
kartla('K-HSB-03','Hareket–bekleme çizelgesi','Boyalı bölümlerin yolları toplanır; ortalama hız toplam süreye (bekleme dahil) bölünür.','Beklemeyi süreye katmamak; hızların ortalamasını almak.','orta','grafik',4,'hrb-gantt','Zaman çizelgesi ve ortalama hız')
kartla('K-HSB-04','Kilometre sayacı okuması','İki sayaç okumasının farkından yol, saat farkından süre bulunup hız hesaplanır; kalan yol aynı hızla süreye çevrilir.','Saat farkını ondalık sanmak; hız yerine yolu kullanmak.','kolay','grafik',3,'hrb-sayac','Kilometre sayacı ve süre')
kartla('K-HSB-05','Dikdörtgen pistte karşılaşma','Başlangıçtaki yay uzunluğu ile hızlar toplamından ilk karşılaşma süresi, çevre ile hızlar toplamından sonrakiler bulunur.','Her karşılaşma arasını ilk karşılaşma süresi saymak; çevreyi yanlış toplamak.','zor','hikâyeli',4,'hrb-dortgen','Dikdörtgen pistte karşılaşma')
kartla('K-HSB-06','Tırmanış–iniş profili','Tırmanış ve inişin süreleri ayrı bulunup toplanır, gidiş-dönüş için iki katı alınır.','İniş hızını tırmanış hızı sanmak; hızların ortalamasıyla süre bulmak.','orta','hikâyeli',3,'hrb-profil','Tırmanış ve iniş süresi')
kartla('K-HSB-07','Eşit aralıklı direkler','Direk numaralarının farkı aralık sayısını verir; şemadaki bilinen aralıktan bir aralığın uzunluğu bulunur; hız km/sa’ye çevrilir.','Direk sayısını aralık sanmak; dönüşümü ters yapmak.','orta','hikâyeli',4,'hrb-direk','Eşit aralıklı direkler ve hız')
kartla('K-HSB-08','Ortalama hız denetimi','İki kamera arası uzaklık hız sınırına bölünüp saat cinsinden süre bulunur ve saniyeye çevrilir.','Saati dakika ya da saniye sanmak; km/sa ile m/sn’yi karıştırmak.','kolay','yeni nesil',3,'hrb-radar','Ortalama hız denetimi')
kartla('K-HSB-09','Tekerlek çevresi ve hız','Yarıçaptan çevre, devir sayısından dakikadaki yol, oradan km/sa hesaplanır.','Yarıçap yerine çap kullanmak; yalnız πr almak; birim çevirmek.','orta','yeni nesil',4,'hrb-tekerlek','Tekerlek devri ve hız')
kartla('K-HSB-10','Üçgen yol, iki güzergâh','Eksik kenar bulunur; iki güzergâhın uzunlukları ve süreleri eşitlenip bekleme süresi çıkarılarak hız bulunur.','Beklemeyi süreye eklemek; yolları eşit sanmak.','zor','hikâyeli',4,'hrb-ucgen','Üçgen yol ve aynı anda varış')

# ===== 01 kolay · yol şeması =====
seg=[('K','L',60,30),('L','M',120,60),('M','N',90,90)]
D=sum(d for _,_,d,_ in seg); Tm=sum(Fr(d,s) for _,_,d,s in seg); v=D/Tm
e=[Fr(sum(s for *_,s in seg),3),D/Fr(sum(Fr(d,s) for _,_,d,s in seg[:2])),Fr(seg[1][3]+seg[2][3],2),90]
assert D==270 and Tm==5 and v==54 and e==[60,Fr(135,2),75,90] and len({v,*e})==5
o=[]; xs=[0,2.0,6.0,9.0]
o.append('\\draw[thick] (0,0) -- (9,0);')
for x,nm in zip(xs,'KLMN'): o.append(f'\\fill ({x},0) circle (0.1); \\node[above=4pt] at ({x},0) {{{nm}}};')
for i,(a,b2,d,s) in enumerate(seg):
    m=(xs[i]+xs[i+1])/2
    o.append(f'\\draw[<->] ({xs[i]+0.1},-0.5) -- ({xs[i+1]-0.1},-0.5); \\node[below=1pt] at ({m},-0.5) {{{d} km}}; \\node[below=1pt,vurgu!60!black] at ({m},-1.1) {{{s} km/sa}};')
SK=fig('\n'.join(o))
q('0001',tipId='hrb-sema',tip='Yol şeması ve ortalama hız',z='kolay',alt='Yol Şeması',kaz='Üç bölümlü yolda bölüm süreleri toplanarak ortalama hız bulunur.',kalip='hikâyeli',
 kart='K-HSB-01 · 60 km@30, 120 km@60, 90 km@90',
 metin='Şekilde, bir şehirlerarası otobüsün K, L, M ve N durakları arasındaki yol uzunlukları ve otobüsün her bölümdeki hızı gösterilmiştir (şekil ölçekli çizilmemiştir). Otobüs her bölümü şekilde yazan sabit hızla gitmiş ve duraklarda hiç beklemeden yolculuğuna devam etmiştir.\nBuna göre, otobüsün K’dan N’ye kadar olan ortalama hızı kaç km/sa’tir?',
 dogru=v,yan=[(e[0],'Üç bölümün hızlarını toplayıp 3’e bölmüş: (30 + 60 + 90) ÷ 3.','dikkat'),(e[1],'Son bölümün süresini hesaba katmamış: 270 ÷ (2 + 2).','dikkat'),(e[2],'İlk bölümü atlayıp son iki hızın ortalamasını almış: (60 + 90) ÷ 2.','dikkat'),(e[3],'En büyük hızı ortalama hız sanmış.','dikkat')],
 istenen='K’dan N’ye ortalama hız (km/sa).',ip=['Her bölümün süresini o bölümün yolu ve hızıyla ayrı ayrı bul.'],bilgi=[ORT],sekil=SK,
 ad=[A('Bölüm süreleri','Yol ÷ hız.','60 ÷ 30 = 2 sa; 120 ÷ 60 = 2 sa; 90 ÷ 90 = 1 sa'),A('Toplam süre','Süreler toplanır.','2 + 2 + 1 = 5 sa'),A('Toplam yol','Yollar toplanır.','60 + 120 + 90 = 270 km'),A('Ortalama hız','Toplam yol ÷ toplam süre.','270 ÷ 5 = 54 km/sa')],
 puf='Bölümlerde geçen süreler farklıysa hızların ortalaması ortalama hızı vermez.')

# ===== 02 orta · sokak ızgarası =====
h=[[520,640],[660,640],[380,680]]; vv=[[660,500,440],[680,460,600]]
h=[[520,640],[660,640],[380,680]]
def plen(p):
    r=c=0; t=0; es=[]
    for m in p:
        if m=='R': t+=h[r][c]; es.append(h[r][c]); c+=1
        else: t+=vv[r][c]; es.append(vv[r][c]); r+=1
    return t,es
allp={''.join(p):plen(''.join(p))[0] for p in set(itertools.permutations('RRUU'))}
best=min(allp.values()); assert best==2160 and sorted(allp.values()).count(best)==1 and allp['RUUR']==2160 and len(set(allp.values()))==6
vsn=Fr(36000,3600); v=Fr(best)/vsn
hor=sum(plen('RUUR')[1][i] for i in (0,3)); ver=sum(plen('RUUR')[1][i] for i in (1,2))
e=[Fr(best)/36,Fr(ver)/vsn,Fr(hor)/vsn,Fr(best-460)/vsn]
assert v==216 and hor==1200 and ver==960 and e[0]==60 and e[1]==96 and e[2]==120 and e[3]==170 and len({v,*e})==5
X=3.0; Y=1.9; o=[]
for r in range(3):
    for c in range(2): o.append(f'\\draw[thick] ({c*X},{r*Y}) -- ({(c+1)*X},{r*Y}) node[midway,fill=white,inner sep=1.5pt] {{{h[r][c]}}};')
for r in range(2):
    for c in range(3): o.append(f'\\draw[thick] ({c*X},{r*Y}) -- ({c*X},{(r+1)*Y}) node[midway,fill=white,inner sep=1.5pt] {{{vv[r][c]}}};')
for r in range(3):
    for c in range(3): o.append(f'\\fill ({c*X},{r*Y}) circle (0.07);')
o.append(f'\\node[below left] at (0,0) {{\\textbf{{A}}}}; \\node[above right] at ({2*X},{2*Y}) {{\\textbf{{B}}}}; \\node[right=3pt] at ({2*X},0) {{(uzunluklar metre)}};')
SK=fig('\n'.join(o))
q('0002',tipId='hrb-izgara',tip='Sokak ızgarası ve en kısa yol',z='orta',alt='Sokak Izgarası',kaz='Sokak ızgarasında en kısa yolu bulup sabit hızla süreyi hesaplar.',kalip='hikâyeli',
 kart='K-HSB-02 · 3×3 ızgara, en kısa 2160 m, 36 km/sa',
 metin='Şekilde, bir mahalledeki sokaklar çizgilerle, her sokağın uzunluğu ise metre cinsinden gösterilmiştir (şekil ölçekli çizilmemiştir). Bir kurye, A noktasından B noktasına yalnız sokaklar üzerinden ve geri dönmeden en kısa yolu izleyerek sabit 36 km/sa hızla gidecektir; kavşaklarda beklemeyecektir.\nBuna göre, kurye A’dan B’ye kaç saniyede gider?',
 dogru=v,yan=[(e[0],'36 km/sa’yi 36 m/sn sanmış: 2 160 ÷ 36.','dikkat'),(e[1],'Yalnız dikey sokakların toplamını (960 m) almış: 960 ÷ 10.','dikkat'),(e[2],'Yalnız yatay sokakların toplamını (1 200 m) almış: 1 200 ÷ 10.','dikkat'),(e[3],'Yol üzerindeki bir sokağı (460 m) atlamış: 1 700 ÷ 10.','dikkat')],
 istenen='A’dan B’ye gitme süresi (sn).',ip=['İleri giden her yolun uzunluğunu sokakları toplayarak bul; en küçüğünü seç ve hızı m/sn’ye çevir.'],bilgi=[EKS],sekil=SK,
 ad=[A('Olası yollar','Her biri 2 sağa, 2 yukarı sokaktan oluşan 6 yolun uzunlukları toplanır.','En küçüğü 520 + 500 + 460 + 680 = 2160 m'),A('Hızı çevir','km/sa değeri 3,6’ya bölünür.','36 ÷ 3,6 = 10 m/sn'),A('Süre','Yol ÷ hız.','2160 ÷ 10 = 216 sn')],
 puf='Önce hızı m/sn’ye çevir, sonra en kısa yolu bul.')

# ===== 03 orta · hareket–bekleme çizelgesi =====
sg=[(8,10,60),(10.5,11.5,80),(12,13,100)]; bas,bit=8,13
yol=sum((b-a)*s for a,b,s in sg); tot=bit-bas; v=Fr(yol).limit_denominator(1)/Fr(tot).limit_denominator(1)
hareket=sum(b-a for a,b,s in sg)
e=[Fr(70),Fr(yol)/Fr(hareket).limit_denominator(1),Fr(sum(s for *_,s in sg),3),Fr(yol)]
assert yol==300 and tot==5 and hareket==4 and v==60 and e==[70,75,80,300] and len({v,*e})==5
sx=2.0; o=[f'\\draw[-{{Stealth}}] (0,-0.9) -- (10.6,-0.9);']
for t in range(8,14): o.append(f'\\draw ({(t-8)*sx},-0.83) -- ({(t-8)*sx},-0.97); \\node[below=2pt] at ({(t-8)*sx},-0.97) {{{t:02d}.00}};')
for a,b2,s in sg: o.append(f'\\filldraw[fill=vurgu!30,draw=black,thick] ({(a-8)*sx},0) rectangle ({(b2-8)*sx},0.9); \\node at ({((a+b2)/2-8)*sx},0.45) {{{s} km/sa}};')
o.append('\\draw[thick] (0,0) rectangle (10,0.9);')
o.append('\\filldraw[fill=vurgu!30,draw=black,thick] (0,1.5) rectangle (0.5,1.9); \\node[right] at (0.6,1.7) {hareket}; \\filldraw[fill=white,draw=black,thick] (2.8,1.5) rectangle (3.3,1.9); \\node[right] at (3.4,1.7) {bekleme};')
SK=fig('\n'.join(o))
q('0003',tipId='hrb-gantt',tip='Zaman çizelgesi ve ortalama hız',z='orta',alt='Zaman Çizelgesi',kaz='Hareket ve bekleme çizelgesinden toplam yolu bulup bekleme dahil ortalama hızı hesaplar.',kalip='grafik',
 kart='K-HSB-03 · 120+80+100 km, 5 saat',
 metin='Bir kargo aracının bir günlük çalışması, şekildeki zaman çizelgesinde gösterilmiştir: boyalı bölümlerde araç yazılı sabit hızla hareket etmiş, boş bölümlerde teslimat için beklemiştir. Aracın günlük raporunda ortalama hız, ilk hareketten son varışa kadar geçen bütün süre (bekleme dahil) üzerinden yazılmaktadır.\nBuna göre, aracın bu çalışmadaki ortalama hızı kaç km/sa’tir?',
 dogru=v,yan=[(e[0],'Yalnız ilk iki hızın ortalamasını almış: (60 + 80) ÷ 2.','dikkat'),(e[1],'Bekleme sürelerini süreye katmamış: 300 ÷ 4.','dikkat'),(e[2],'Üç hızın ortalamasını almış: (60 + 80 + 100) ÷ 3.','dikkat'),(e[3],'Toplam yolu (300 km) ortalama hız sanmış.','dikkat')],
 istenen='Bekleme dahil ortalama hız (km/sa).',ip=['Her boyalı bölümün süresini çizelgeden oku; ortalama hız için toplam süreyi ilk hareketten son varışa say.'],bilgi=[GAN],sekil=SK,
 ad=[A('Yollar','Hız × süre.','60 × 2 = 120; 80 × 1 = 80; 100 × 1 = 100 km'),A('Toplam yol','Yollar toplanır.','120 + 80 + 100 = 300 km'),A('Toplam süre','08.00’dan 13.00’a, bekleme dahil.','5 saat'),A('Ortalama hız','Yol ÷ süre.','300 ÷ 5 = 60 km/sa')],
 puf='Beklemeler de toplam süredendir.')

# ===== 04 kolay · kilometre sayacı =====
k1,k2=48372,48447; t1m,t2m=10*60+20,11*60+50; fark=k2-k1; dak=t2m-t1m; hiz=Fr(fark*60,dak); kalan=135; v=Fr(kalan)/hiz*60
e=[Fr(kalan,fark)*60,Fr(kalan*130,fark),Fr(kalan+fark)/hiz*60,Fr(kalan)/Fr(fark*60,120)*60]
assert fark==75 and dak==90 and hiz==50 and v==162 and e==[108,234,252,216] and len({v,*e})==5
def odo(x0,val,tm):
    o=[f'\\node at ({x0+1.1},1.1) {{Saat {tm}}};']
    for i,ch in enumerate(str(val)): o.append(f'\\node[draw,thick,fill=vurgu!10,minimum width=0.55cm,minimum height=0.85cm] at ({x0+i*0.6:.2f},0) {{\\large {ch}}};')
    o.append(f'\\node[right] at ({x0+2.95},0) {{km}};'); return o
SK=fig('\n'.join(odo(0,k1,'10.20')+odo(5.0,k2,'11.50')))
q('0004',tipId='hrb-sayac',tip='Kilometre sayacı ve süre',z='kolay',alt='Kilometre Sayacı',kaz='İki sayaç okumasından hızı bulup kalan yolun süresini hesaplar.',kalip='grafik',
 kart='K-HSB-04 · 48 372 → 48 447 km, 90 dk; 50 km/sa; kalan 135 km → 162 dk',
 metin='Bir araçta kilometre sayacının, aynı yolculuk sırasında yazılı iki saatteki okumaları şekilde gösterilmiştir. Araç bu iki okuma arasında ve sonrasında yoldan hiç ayrılmadan, hiç durmadan sabit hızla gitmiştir. Sürücü, ikinci okumada varış noktasına 135 km kaldığını navigasyondan öğrenmiştir.\nBuna göre, araç ikinci okumadan sonra varış noktasına kaç dakikada ulaşır?',
 dogru=v,yan=[(e[0],'Hız yerine iki okumadaki yolu (75 km/sa) kullanmış: 135 ÷ 75 saat.','dikkat'),(e[1],'1 saat 30 dakikayı 130 dakika sanmış.','dikkat'),(e[2],'Kalan yola aldığı yolu da ekleyip 210 km’yi 50 km/sa ile bölmüş.','dikkat'),(e[3],'Süreyi 2 saat sanıp hızı 37,5 km/sa bulmuş: 135 ÷ 37,5 saat.','dikkat')],
 istenen='İkinci okumadan varışa kadar geçen süre (dk).',ip=['İki okuma arasındaki yolu ve geçen süreyi bul; süreyi saate çevirmeye dikkat et.'],bilgi=[KM],sekil=SK,
 ad=[A('Alınan yol ve süre','Sayaç farkı ve saat farkı.','48447 − 48372 = 75 km; 10.20 ile 11.50 arası 1,5 saat'),A('Hız','Yol ÷ süre.','75 ÷ 1,5 = 50 km/sa'),A('Kalan süre','Kalan yol ÷ hız, dakikaya çevrilir.','135 ÷ 50 = 2,7 sa = 162 dk')],
 puf='1 saat 30 dakika = 1,5 saattir.')

# ===== 05 zor · dikdörtgen pist =====
a_,b_=150,50; C=2*(a_+b_); va,vb=5,3; yar=Fr(C,2); t1=yar/(va+vb); per=Fr(C,va+vb); t3=t1+2*per; v=va*t3
e=[va*t1,va*(t1+per),va*3*per,va*(t1+3*per)]
assert C==400 and t1==25 and per==50 and t3==125 and v==625 and e==[125,375,750,875] and len({v,*e})==5
W,Hh=6.0,2.0; o=[f'\\draw[thick] (0,0) rectangle ({W},{Hh});']
for x,y,nm,pos in ((0,0,'A','below left'),(W,0,'B','below right'),(W,Hh,'C','above right'),(0,Hh,'D','above left')): o.append(f'\\fill ({x},{y}) circle (0.08); \\node[{pos}] at ({x},{y}) {{{nm}}};')
o.append(f'\\draw[<->] (0,{Hh+0.55}) -- ({W},{Hh+0.55}); \\node[above=1pt] at ({W/2},{Hh+0.55}) {{{a_} m}};')
o.append(f'\\draw[<->] (-0.75,0) -- (-0.75,{Hh}); \\node[left=1pt] at (-0.75,{Hh/2}) {{{b_} m}};')
o.append('\\draw[-{Stealth[length=9pt]},very thick,vurgu!70!black] (1.4,0.3) -- (2.6,0.3); \\node[above=1pt] at (2.0,0.3) {Ali};')
o.append(f'\\draw[-{{Stealth[length=9pt]}},very thick,vurgu!70!black] ({W-0.3},1.6) -- ({W-0.3},0.6); \\node[left=2pt] at ({W-0.3},1.1) {{Barış}};')
SK=fig('\n'.join(o))
q('0005',tipId='hrb-dortgen',tip='Dikdörtgen pistte karşılaşma',z='zor',alt='Dikdörtgen Pist',kaz='Dikdörtgen pistte zıt yönlerde koşanların üçüncü karşılaşmasına kadar alınan yolu hesaplar.',kalip='hikâyeli',
 kart='K-HSB-05 · çevre 400 m, A ve C karşı köşe, 5 ve 3 m/sn',
 metin='Şekilde, dikdörtgen biçimli bir koşu pistinin boyutları ve iki sporcunun başlangıç köşeleri ile koşu yönleri gösterilmiştir. Ali ve Barış aynı anda, şekildeki yönlerde ve piste uyarak, Ali sabit 5 m/sn, Barış sabit 3 m/sn hızla koşmaya başlıyor; koşu boyunca hiç durmuyorlar ve yön değiştirmiyorlar.\nBuna göre, ikisi üçüncü kez karşılaştığında Ali toplam kaç metre koşmuş olur?',
 dogru=v,yan=[(e[0],'İlk karşılaşmadaki yolu (125 m) yazmış.','dikkat'),(e[1],'İkinci karşılaşmadaki yolu (375 m) yazmış.','dikkat'),(e[2],'Her karşılaşmanın ilk karşılaşma gibi 50 sn aralıkla olduğunu sanıp 3 × 50 sn’de koşulan yolu hesaplamış.','dikkat'),(e[3],'Dördüncü karşılaşmayı hesaplamış: 175 sn × 5.','dikkat')],
 istenen='Üçüncü karşılaşmaya kadar Ali’nin koştuğu yol (m).',ip=['Pistin çevresini bulup başlangıçta iki sporcu arasındaki yol uzunluğunun, karşı köşeler için çevrenin kaçta kaçı olduğunu düşün.'],bilgi=[PIS],sekil=SK,
 ad=[A('Çevre','Dikdörtgenin çevresi.','2 × (150 + 50) = 400 m'),A('İlk karşılaşma','Karşı köşeler arası yay çevrenin yarısıdır; hızlar toplamıyla yaklaşırlar.','200 ÷ (5 + 3) = 25 sn'),A('Sonraki karşılaşmalar','Her biri arasında toplam bir çevre yol alırlar.','400 ÷ 8 = 50 sn; üçüncü: 25 + 2 × 50 = 125 sn'),A('Ali’nin yolu','Hız × süre.','5 × 125 = 625 m')],
 puf='Karşılaşmalar arası süre, çevre bölü hızlar toplamıdır.')

# ===== 06 orta · tırmanış–iniş profili =====
dist,vu,vd,tur=8,16,32,2; tek=Fr(dist,vu)+Fr(dist,vd); v=tek*tur*60
e=[tek*60,Fr(dist,vu)*tur*60,Fr(dist,vu)*2*tur*60,Fr(2*dist,Fr(vu+vd,2))*tur*60]
assert tek==Fr(3,4) and v==90 and e==[45,60,120,80] and len({v,*e})==5
o=['\\draw[thick] (-0.8,0) -- (0,0) -- (3,1.9) -- (6,0) -- (6.8,0);','\\fill (0,0) circle (0.07); \\fill (6,0) circle (0.07); \\fill (3,1.9) circle (0.07);',
   '\\node[below=3pt] at (0,0) {A}; \\node[below=3pt] at (6,0) {C}; \\node[above=3pt] at (3,1.9) {B};',
   '\\node[above left=2pt,sloped] at (1.5,0.95) {tırmanış: 8 km}; \\node[above right=2pt,sloped] at (4.5,0.95) {iniş: 8 km};',]
SK=fig('\n'.join(o))
q('0006',tipId='hrb-profil',tip='Tırmanış ve iniş süresi',z='orta',alt='Tırmanış–İniş Profili',kaz='Tırmanış ve iniş bölümlerinin süreleri toplanarak tekrarlı turun süresi bulunur.',kalip='hikâyeli',
 kart='K-HSB-06 · 8 km @16, 8 km @32, gidiş-dönüş',
 metin='Bir bisiklet kulübü, şekildeki yan görünümü verilen parkurda antrenman yapmaktadır (şekil ölçekli çizilmemiştir). Parkur A’dan B’ye yükselen, B’den C’ye alçalan bir yoldur. Sporcu, A’dan C’ye gidip ara vermeden aynı yoldan A’ya dönmektedir (gidiş-dönüş); yolun her yükselen bölümünde sabit 16 km/sa, her alçalan bölümünde sabit 32 km/sa hızla gitmektedir.\nBuna göre, sporcunun gidiş-dönüşü kaç dakika sürer?',
 dogru=v,yan=[(e[0],'Yalnız gidişin süresini bulmuş.','dikkat'),(e[1],'Yalnız yükselen bölümlerin sürelerini toplamış: 2 × 30 dk.','dikkat'),(e[2],'İniş hızını da 16 km/sa almış: 2 × 60 dk.','dikkat'),(e[3],'Hızların ortalamasını (24 km/sa) kullanmış: 32 km ÷ 24 km/sa.','dikkat')],
 istenen='Gidiş-dönüşün süresi (dk).',ip=['Gidişte ve dönüşte yükselen ve alçalan bölümlerin sürelerini ayrı ayrı hesapla.'],bilgi=[TUR],sekil=SK,
 ad=[A('Tırmanış süresi','Yol ÷ hız.','8 ÷ 16 = 0,5 sa'),A('İniş süresi','Yol ÷ hız.','8 ÷ 32 = 0,25 sa'),A('Gidiş-dönüş','Dönüşte de bir yükselen, bir alçalan bölüm vardır; süre 2 ile çarpılır.','2 × 0,75 sa = 1,5 sa = 90 dk')],
 puf='Bölümleri ayrı süreyle çöz.')

# ===== 07 orta · direkler =====
ar1=5-2; blk=150; sp=Fr(blk,ar1); n1,n2=3,11; aral=n2-n1; yolm=aral*sp; sure=40; vms=yolm/sure; v=vms*Fr(36,10)
e=[vms,Fr((n2-n1+1)*sp,sure)*Fr(36,10),Fr(aral*Fr(blk,5-2+1),sure)*Fr(36,10),Fr(aral*blk,sure)*Fr(36,10)]
assert sp==50 and yolm==400 and vms==10 and v==36 and e==[10,Fr(81,2),27,108] and len({v,*e})==5
o=['\\draw[thick] (-0.3,0) -- (8.2,0);']
for i in range(1,13):
    x=(i-1)*0.65; o.append(f'\\draw[very thick] ({x:.2f},0) -- ({x:.2f},0.75); \\node[below=1pt] at ({x:.2f},0) {{{i}}};')
o.append(f'\\draw[<->] ({1*0.65:.2f},-0.75) -- ({4*0.65:.2f},-0.75); \\node[below=1pt] at ({2.5*0.65:.2f},-0.75) {{{blk} m}};')
o.append('\\draw[-{Stealth[length=9pt]},thick,vurgu!70!black] (-0.3,1.2) -- (1.3,1.2); \\node[right=2pt] at (1.3,1.2) {araç yönü};')
SK=fig('\n'.join(o))
q('0007',tipId='hrb-direk',tip='Eşit aralıklı direkler ve hız',z='orta',alt='Eşit Aralıklı Direkler',kaz='Eşit aralıklı direklerde aralık uzunluğunu bulup bir aracın hızını km/sa olarak hesaplar.',kalip='hikâyeli',
 kart='K-HSB-07 · 2–5 arası 150 m, 3→11 direk 40 sn',
 metin='Bir yolun kenarına, ardışık iki direk arası aynı olacak biçimde numaralı direkler dikilmiştir; direklerin bir bölümü ve 2. ile 5. direk arasındaki uzaklık şekilde gösterilmiştir. Bu yoldan sabit hızla giden bir araç, 3. direğin yanından geçtiği andan 11. direğin yanından geçtiği ana kadar 40 saniye geçirmiştir.\nBuna göre, aracın hızı kaç km/sa’tir?',
 dogru=v,yan=[(e[0],'Hızı m/sn olarak bırakmış, km/sa’ye çevirmemiş.','dikkat'),(e[1],'Direk sayısını (9) aralık sayısı sanmış: 9 × 50 ÷ 40.','dikkat'),(e[2],'2.–5. direk arasını 4 aralık sanmış: aralık 37,5 m.','dikkat'),(e[3],'Şekildeki 150 m’yi tek bir aralık sanmış: 8 × 150 ÷ 40.','dikkat')],
 istenen='Aracın hızı (km/sa).',ip=['Şekildeki iki direk numarasından aralık sayısını bul; bir aralığın uzunluğunu buradan çıkar.'],bilgi=[DIR],sekil=SK,
 ad=[A('Bir aralık','2’den 5’e 3 aralık, 150 m.','150 ÷ 3 = 50 m'),A('Alınan yol','3’ten 11’e 8 aralık.','8 × 50 = 400 m'),A('Hız (m/sn)','Yol ÷ süre.','400 ÷ 40 = 10 m/sn'),A('Hız (km/sa)','m/sn değeri 3,6 ile çarpılır.','10 × 3,6 = 36 km/sa')],
 puf='Aralık sayısı, numaraların farkıdır.')

# ===== 08 kolay · ortalama hız denetimi (yeni nesil) =====
dk,lim=Fr(9,2),90; sure_h=dk/lim; v=sure_h*3600
e=[sure_h*60,Fr(450,25),Fr(4500,lim),Fr(5*60)]
assert sure_h==Fr(1,20) and v==180 and e==[3,18,50,300] and len({v,*e})==5
o=['\\draw[very thick] (0,0) -- (9,0);']
for x,nm in ((1.0,'K'),(8.0,'L')): o.append(f'\\filldraw[fill=vurgu!30,draw=black,thick] ({x-0.28},0.25) rectangle ({x+0.28},0.75); \\fill ({x+0.28},0.5) circle (0.1); \\draw[thick] ({x},0.25) -- ({x},0); \\node[below=2pt] at ({x},0) {{{nm}}};')
o.append('\\draw[<->] (1.0,-0.75) -- (8.0,-0.75); \\node[below=1pt] at (4.5,-0.75) {4,5 km};')
o.append('\\draw[red!70!black,line width=3pt] (4.5,1.9) circle (0.58); \\node at (4.5,1.9) {\\large\\textbf{90}}; \\node[right=0.1] at (5.15,1.9) {km/sa};')
SK=fig('\n'.join(o))
q('0008',tipId='hrb-radar',tip='Ortalama hız denetimi',z='kolay',alt='Ortalama Hız Denetimi',kaz='İki kamera arası uzaklık ve hız sınırından hız sınırıyla gitmenin süresini saniye cinsinden bulur.',kalip='yeni nesil',
 kart='K-HSB-08 · 4,5 km, 90 km/sa sınır',
 metin='Şekilde, bir karayolundaki K ve L kameraları arasındaki uzaklık ve bu yolun hız sınırı gösterilmiştir. “Ortalama hız denetimi”nde bir aracın K ve L kameralarının önünden geçiş anları kaydedilir; bu iki an arasındaki süre, kameralar arasındaki yolun hız sınırıyla gidilme süresinden kısaysa araç ihlal yapmış sayılır.\nBuna göre, bir aracın ihlal yapmaması için K’dan L’ye gitmesi en az kaç saniye sürmelidir?',
 dogru=v,yan=[(e[0],'Süreyi (0,05 saat) dakikaya çevirip (3) saniye yerine dakika olarak yazmış.','dikkat'),(e[1],'Mesafeyi 450 m sanıp 25 m/sn hızla bölmüş: 450 ÷ 25.','dikkat'),(e[2],'90 km/sa’yi 90 m/sn sanmış: 4 500 ÷ 90.','dikkat'),(e[3],'0,05 saati 5 dakika sanıp saniyeye çevirmiş: 5 × 60.','dikkat')],
 istenen='İhlal olmaması için gereken en kısa süre (sn).',ip=['Önce kameralar arasındaki yolu sınır hızla gitmenin süresini saat cinsinden bul.'],bilgi=[ORH],sekil=SK,
 ad=[A('Süre (saat)','Yol ÷ hız sınırı.','4,5 ÷ 90 = 0,05 sa'),A('Dakika','1 saat 60 dakikadır.','0,05 × 60 = 3 dk'),A('Saniye','1 dakika 60 saniyedir.','3 × 60 = 180 sn')],
 puf='Süreyi önce saat olarak bul, sonra saniyeye çevir.')

# ===== 09 orta · tekerlek =====
r_,dev=35,100; cev=Fr(2*22*r_,7); mdk=cev*dev/100; v=mdk*60/1000
e=[Fr(22*r_,7)*dev/100*60/1000,Fr(2*22*2*r_,7)*dev/100*60/1000,mdk,mdk*Fr(36,10)]
assert cev==220 and mdk==220 and v==Fr(66,5) and e[0]==Fr(33,5) and e[1]==Fr(132,5) and len({v,*e})==5 and e[3]==792
o=['\\draw[very thick] (0,0) circle (1.7);','\\draw[very thick] (0,0) circle (1.45);']
for k in range(12): o.append(f'\\draw (0,0) -- ({1.45*cos(radians(30*k+15)):.3f},{1.45*sin(radians(30*k+15)):.3f});')
o.append('\\fill (0,0) circle (0.1); \\draw[thick,vurgu!70!black] (0,0) -- (1.7,0); \\node[right=4pt] at (1.7,0) {35 cm};')
SK=fig('\n'.join(o))
q('0009',tipId='hrb-tekerlek',tip='Tekerlek devri ve hız',z='orta',alt='Tekerlek ve Hız',kaz='Tekerleğin yarıçapından çevreyi, devir sayısından hızı bulup km/sa’ye çevirir.',kalip='yeni nesil',
 kart='K-HSB-09 · r=35 cm, π=22/7, 100 devir/dk',
 metin='Yarıçapı şekilde verilen bir tekerlek, düz zeminde kaymadan yuvarlanmaktadır. Kaymadan yuvarlanan tekerlek her devirde çevresine eşit yol alır ve tekerleğin merkezi de zemine paralel, sabit hızla ilerler. Tekerlek dakikada 100 tam devir yapmaktadır; hesapta π yerine 22/7 alınacaktır.\nBuna göre, tekerleğin merkezinin hızı kaç km/sa’tir?',
 dogru=v,yan=[(e[0],'Çevre yerine πr’yi almış: 110 cm.','dikkat'),(e[1],'Yarıçap yerine çapı (70 cm) kullanmış: çevre 440 cm.','dikkat'),(e[2],'Dakikadaki yolu (220 m/dk) km/sa sanmış.','dikkat'),(e[3],'m/dk değerini 3,6 ile çarparak km/sa’ye çevirmeye çalışmış.','dikkat')],
 istenen='Tekerlek merkezinin hızı (km/sa).',ip=['Önce tekerleğin bir devirdeki yolunu bul; sonra dakikadaki yolu km/sa’ye çevir.'],bilgi=[TEK],sekil=SK,
 ad=[A('Çevre','2πr.','2 × 22/7 × 35 = 220 cm'),A('Dakikadaki yol','Çevre × devir sayısı.','220 × 100 = 22 000 cm = 220 m'),A('Saatteki yol','Bir saat 60 dakikadır.','220 × 60 = 13 200 m = 13,2 km'),A('Hız','Bir saatte alınan km.','13,2 km/sa')],
 puf='Önce çevreyi bul; çevre bir devirde alınan yoldur.')

# ===== 10 zor · üçgen yol, iki güzergâh =====
ab,bc=8,15; ac=17; assert ab**2+bc**2==ac**2; v1=34; t=Fr(ac,v1); mola=Fr(10,60); yol2=ab+bc; v=Fr(yol2)/(t-mola)
e=[Fr(v1),Fr(yol2)/(t+mola),Fr(yol2)/t,Fr(yol2)/(t-Fr(1,10))]
assert t==Fr(1,2) and v==69 and e==[34,Fr(69,2),46,Fr(115,2)] and len({v,*e})==5
o=['\\draw[thick] (0,0) -- (3.2,0) -- (3.2,6.0) -- cycle;','\\draw (3.0,0) -- (3.0,0.2) -- (3.2,0.2);',
   '\\node[below left] at (0,0) {A}; \\node[below right] at (3.2,0) {B}; \\node[above right] at (3.2,6.0) {C};',
   '\\node[below=2pt] at (1.6,0) {8 km}; \\node[right=3pt] at (3.2,3.0) {15 km};']
SK=fig('\n'.join(o))
q('0010',tipId='hrb-ucgen',tip='Üçgen yol ve aynı anda varış',z='zor',alt='Üçgen Yol',kaz='Dik üçgen biçimli yolda doğrudan ve dolaylı güzergâhın uzunluklarından, beklemeyi çıkararak hızı bulur.',kalip='hikâyeli',
 kart='K-HSB-10 · 8-15-17 yol; 34 km/sa; 10 dk mola',
 metin='Şekilde, A kasabasından C kasabasına giden iki yol gösterilmiştir: doğrudan AC yolu ile B kasabası üzerinden geçen AB ve BC yolları; B’deki açı dik açıdır. Zeynep AC yolundan sabit 34 km/sa hızla, Ali ise aynı anda çıkıp AB ve BC yollarından, B’de 10 dakika dinlenerek gidiyor. İkisi C’ye aynı anda varıyor ve Ali yalnız hareket ettiği sürelerde sabit hızla gidiyor.\nBuna göre, Ali’nin hareket hâlindeki hızı kaç km/sa’tir?',
 dogru=v,yan=[(e[0],'Zeynep’in hızını Ali’nin hızı sanmış.','dikkat'),(e[1],'Dinlenmeyi hareket süresine eklemiş: 23 ÷ (0,5 + 1/6).','dikkat'),(e[2],'Dinlenmeyi hiç hesaba katmamış: 23 ÷ 0,5.','dikkat'),(e[3],'10 dakikayı 0,1 saat almış: 23 ÷ 0,4.','dikkat')],
 istenen='Ali’nin hareket hâlindeki hızı (km/sa).',ip=['Önce AC yolunun uzunluğunu bul; Zeynep’in süresiyle Ali’nin hareket süresi arasındaki ilişkiyi kur.'],bilgi=[IKI],sekil=SK,
 ad=[A('AC yolu','Dik üçgende Pisagor.','√(8² + 15²) = 17 km'),A('Zeynep’in süresi','Yol ÷ hız.','17 ÷ 34 = 0,5 sa = 30 dk'),A('Ali’nin hareket süresi','Toplam süreden dinlenme çıkarılır.','30 − 10 = 20 dk = 1/3 sa'),A('Ali’nin yolu ve hızı','AB + BC yolu hareket süresine bölünür.','23 ÷ (1/3) = 69 km/sa')],
 puf='Aynı anda varan iki yolcunun toplam süreleri eşittir.')

bitir(P,'hareketsekb',UK)
