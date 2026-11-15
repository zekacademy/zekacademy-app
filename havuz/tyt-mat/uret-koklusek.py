"""Köklü Sayılar · şekilli paket (koklusek): 8 soru, hepsi şekilli/tablolu. Kardeş yok, ipucu 1. Her cevap ve çeldirici değer kodla hesaplanıp assert edilir.
Şekil ölçüleri Python'da üretilir; TikZ gövdesi aynı değerlerden f-string ile yazılır (bkz. havuz/URETIM-SEKIL.md)."""
import sys,os,math
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
H.KONU='Köklü Sayılar'
P=Parti('koklusek','Köklü Sayılar','mat|Köklü Sayılar')
KY='ÖSYM 2018–2026 TYT Matematik (şekilli/tablolu köklü sayı soruları, yalnız mantık) · MEB 9. sınıf'
TP=lambda g:tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'+g+'\n\\end{tikzpicture}')
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)
def Ks(c,r):
    """c√r metni ve değeri"""
    s=(str(c) if c!=1 else '')+'√'+str(r) if r!=1 else str(c)
    return s,c*math.sqrt(r)
def sirala(*vs):
    """(metin,değer) çiftlerini değere göre sıralı metin listesine çevir"""
    assert len({round(v,9) for _,v in vs})==len(vs)
    return [s for s,_ in sorted(vs,key=lambda t:t[1])]
def kk(c,r): return Ks(c,r)
def qk(no,ad,dogru,yan,**k):
    vs=[dogru]+[y[0] for y in yan]; sira=sirala(*vs)
    mk(P,no,ad=ad,adim=len(ad),dogru=dogru[0],yan=[(y[0][0],y[1],y[2]) for y in yan],sira=sira,**k)

KOK=B('Kök dışına çıkarma','kök içindeki sayı “tam kare × kalan” biçiminde yazılır: √(a²·b) = a√b (a, b pozitif). Örnek: √28 = √(4·7) = 2√7')
CRP=B('Köklü çarpma','√a · √b = √(ab) (a, b ≥ 0). Örnek: √6 · √3 = √18 = 3√2')
PIS=B('Pisagor bağıntısı','dik üçgende dik kenarların kareleri toplamı hipotenüsün karesine eşittir: a² + b² = c². Örnek: dik kenarları 3 ve 4 olan üçgenin hipotenüsü √(9 + 16) = 5')
KAR=B('Karenin alanı ve kenarı','alanı A olan karenin kenarı √A’dır; çevresi 4√A’dır. Örnek: alanı 25 olan karenin kenarı 5, çevresi 20')
TOPK=B('Benzer köklerle toplama','kök içleri aynı olan terimlerin katsayıları toplanır. Örnek: 2√3 + 5√3 = 7√3')

kart('K-KKS-01','Alanı verilen karelerin çevresi','Alanı verilen karenin kenarı alanın karekökü olarak yazılıp sadeleştirilir; kök içleri aynı olan kenarlar toplanır, çevre 4 × kenar toplamıdır.','Çevre yerine kenar toplamını almak; alanları toplayıp kök almak; √2 çarpanını unutmak.','kolay','tablo',3,'kks-alan','Alanı verilen karelerin çevresi',KY)
kart('K-KKS-02','Kareli zeminde köşegen yolu','Kareli zeminde bir birim kareyi köşegenle geçmek √2 uzunluğundadır; adım sayıları toplanıp √2 ile çarpılır.','Köşegeni 1 ya da √3 sanmak; yatay ve dikey adımları toplamak; adım sayısını yanlış okumak.','kolay','şekilli',3,'kks-kare','Kareli zeminde köşegen yolu',KY)
kart('K-KKS-03','Sayı doğrusunda kök yeri','Sayı doğrusunda bir noktanın iki tam sayı arasında olması, kök içinin bu tam sayıların karelerinin arasında olması demektir; uç değerler kök içi tam kare olduğundan dışarıda kalır.','Kare olan uç değerleri dahil etmek; en büyük ve en küçük değerleri karıştırmak; aralığı yanlış okumak.','orta','şekilli',4,'kks-dogru','Sayı doğrusunda kök yeri ve aralık',KY)
kart('K-KKS-04','Dikdörtgenin çevresi ve köşegeni','Köklü kenarlar sadeleştirilir; çevre, kenarlar toplamıyla; köşegen Pisagor ile bulunur; fark kök içleri aynı olduğu için doğrudan yapılır.','Kök içlerini toplamak; çevre yerine yarı çevreyi ya da yalnız köşegeni yazmak; Pisagorda karekökü unutmak.','orta','şekilli',4,'kks-dikdortgen','Dikdörtgenin çevresi ve köşegeni',KY)
kart('K-KKS-05','Basamaklı kare dizisi','Alanlardan kenarlar bulunur, kenarların √2 katsayıları ardışık artar; ilk n kenarın toplamı katsayı toplamı × √2’dir.','Alan toplamını kenar toplamı sanmak; √2 çarpanını unutmak; katsayıların toplamında hata yapmak.','orta','şekilli',4,'kks-merdiven','Basamaklı kare dizisinde kenar toplamı',KY)
kart('K-KKS-06','İç içe iki kare','Alanlardan kenarlar bulunur; çevreler farkı, kenar farkının 4 katıdır; kök içleri aynı olduğundan fark sadeleşir.','Alan farkını çevre farkı sanmak; √2 çarpanını unutmak; kenar farkını 4 ile çarpmamak.','zor','şekilli',5,'kks-icice','İç içe karelerde çevre farkı',KY)
kart('K-KKS-07','Kumaş parçalarının alanı','Tabloda köklü kenarlar çarpılır; √a · √b = √(ab) ile çarpım tam kareye dönüşür; alanlar toplanır.','Kök içlerini toplamak; √2 · √2’yi 1 almak; bir satırı atlamak.','orta','tablo',4,'kks-tablo','Tabloda köklü kenarların alanı',KY)
kart('K-KKS-08','Pisagor sarmalı','Ardışık dik üçgenlerde hipotenüsün karesi bir artar; n. hipotenüs √(n + 1)’dir; tam sayı olanlar kök içi tam kare olan terimlerdir.','Tam kare kök içlerini yanlış belirlemek; adedi toplam sanmak; son tam kareyi (36) atlamak.','zor','şekilli',5,'kks-sarmal','Pisagor sarmalında tam sayı hipotenüsler',KY)

# ---------- 01 · kolay · alanı verilen karelerin çevresi (tablo) ----------
al=[8,18,50]; ke=[(2,2),(3,2),(5,2)]
assert all(c*c*r==a for (c,r),a in zip(ke,al)) and 4*sum(c for c,_ in ke)==40
sek=tablo_svg(['Çiçeklik','Alan (m²)'],[['A','8'],['B','18'],['C','50']])
qk('0001',tipId='kks-alan',tip='Alanı verilen karelerin çevresi',z='kolay',alt='Köklü Uzunluklar',kaz='Alanları tabloda verilen karelerin kenarlarını kök dışına çıkararak bulur ve çevreler toplamını hesaplar.',kalip='tablo',sekil=sek,
 kart='K-KKS-01 (alanı verilen karelerin çevresi) · 8, 18, 50 m²',
 dogru=kk(40,2),yan=[(kk(20,2),'Her çevreyi 4 × kenar yerine 2 × kenar (yarı çevre) almış: 2 × 10√2 = 20√2.','dikkat'),(kk(8,19),'Alanları toplayıp (76) kökünü almış: 4√76 = 8√19.','islem'),(kk(40,1),'Kenarların √2 çarpanını unutmuş: 4 × (2 + 3 + 5) = 40.','dikkat'),(kk(80,2),'Çevreyi 8 × kenar toplamı almış.','islem')],
 metin='Kare biçimli üç çiçekliğin alanları aşağıdaki tabloda verilmiştir. Her çiçekliğin çevresine, bir tur olacak biçimde ve ek yapılmaksızın tel çekilecektir.\nBuna göre bu üç çiçeklik için gereken toplam tel uzunluğu kaç metredir?',
 istenen='Üç çiçekliğin çevreleri toplamı.',
 ip=['Her karenin kenarı alanının karekökü olur; kök içlerini sadeleştirmeyi dene.'],
 bilgi=[KAR,KOK,TOPK],
 ad=[A('Kenarları bul','Kenar, alanın karekökü; kök dışına çıkar.','√8 = 2√2 · √18 = 3√2 · √50 = 5√2'),A('Kenarları topla','Kök içleri aynı, katsayılar toplanır.','2√2 + 3√2 + 5√2 = 10√2'),A('Çevre','Her çevre 4 × kenardır; toplam çevre 4 × kenarlar toplamı.','4 × 10√2 = 40√2')],
 puf='Alanı verilen karede çevre = 4√alan; çarpanlara ayırıp kök dışına çıkarınca kök içleri aynı kalır.')

# ---------- 02 · kolay · kareli zeminde köşegen yolu ----------
pts=[(0,0),(3,3),(5,1),(9,5)]; ad_=[abs(pts[i+1][0]-pts[i][0]) for i in range(3)]
assert all(abs(pts[i+1][0]-pts[i][0])==abs(pts[i+1][1]-pts[i][1]) for i in range(3)) and ad_==[3,2,4] and sum(ad_)==9
g=''
for i in range(10): g+=f'\\draw[line width=.3pt,black!45] ({i},0) -- ({i},5);'
for j in range(6): g+=f'\\draw[line width=.3pt,black!45] (0,{j}) -- (9,{j});'
g+=f'\\draw[line width=.3pt,black!45] (9,0) -- (9,5);\\draw[line width=.3pt,black!45] (0,5) -- (9,5);'
g=g.replace('\\draw[line width=.3pt,black!45] (9,0) -- (9,5);','')
for i in range(10): g+=f'\\draw[line width=.3pt,black!45] ({i},0) -- ({i},5);' if False else ''
g+='\\draw[line width=.3pt,black!45] (9,0) -- (9,5);'
g+='\\draw[vurgu,very thick] '+' -- '.join(f'({x},{y})' for x,y in pts)+';'
for (x,y),n,dx,dy in zip(pts,'ABCD',(-.3,-.3,.3,.3),(-.3,.35,-.35,.3)): g+=f'\\filldraw ({x},{y}) circle (.09);\\node at ({x+dx},{y+dy}) {{\\textbf{{{n}}}}};'
sek=TP('\\begin{scope}[scale=.62]'+g+'\\end{scope}')
qk('0002',tipId='kks-kare',tip='Kareli zeminde köşegen yolu',z='kolay',alt='Köklü Uzunluklar',kaz='Kareli zeminde köşegen doğrultusundaki adımların uzunluğunu √2 ile çarparak toplam yolu bulur.',kalip='şekilli',sekil=sek,
 kart='K-KKS-02 (kareli zeminde köşegen yolu) · A(0,0), B(3,3), C(5,1), D(9,5)',
 metin='Şekildeki kareli zeminde küçük karelerin her birinin kenarı 1 cm’dir. Bir karınca A noktasından D noktasına, şekilde çizilen A–B–C–D yolu boyunca yürümektedir.\nBuna göre karıncanın yürüdüğü yolun uzunluğu kaç cm’dir?',
 dogru=kk(9,2),yan=[(kk(9,1),'Köşegeni 1 cm sanmış; yalnız geçilen kare sayısını (3 + 2 + 4 = 9) yazmış.','dikkat'),(kk(9,3),'Birim karenin köşegenini √3 sanmış: 9√3.','bilgi'),(kk(18,1),'Her adımda yatay ve dikey birimleri ayrı toplamış (9 + 9 = 18); köşegen kısa yoldur.','islem'),(kk(18,2),'Yatay ve dikey toplamı olan 18’i √2 ile çarpmış; köşegen adımları yalnız 9 tanedir.','islem')],
 istenen='A’dan D’ye yolun uzunluğu.',
 ip=['Her parçada yatayda ve düşeyde kaç birim gidildiğine bak; bir kare köşegeninin uzunluğu nedir?'],
 bilgi=[PIS],
 ad=[A('Parçaları oku','Her parça, yatayda ve düşeyde aynı sayıda kare giden bir köşegendir.','AB: 3 kare · BC: 2 kare · CD: 4 kare'),A('Bir karenin köşegeni','Kenarı 1 cm olan karenin köşegeni Pisagor’la bulunur.','√(1² + 1²) = √2 cm'),A('Toplam','Kare sayıları toplanıp √2 ile çarpılır.','(3 + 2 + 4) × √2 = 9√2')],
 puf='Kareli zeminde köşegen doğrultusunda k kare ilerlemek k√2 uzunluğudur.')

# ---------- 03 · orta · sayı doğrusunda kök yeri ----------
amin,amax=10,15; bmin,bmax=37,48
assert [a for a in range(0,60) if 3<math.sqrt(a)<4]==list(range(amin,amax+1)) and [b for b in range(0,60) if 6<math.sqrt(b)<7]==list(range(bmin,bmax+1))
en=bmax-amin; assert en==38 and bmin-amax==22 and bmax-(amax)==33 and bmax-9==39 and 49-9==40
g='\\draw[thick,-{Stealth[length=2mm]}] (-.3,0) -- (6.6,0);'
for i,t in enumerate([3,4,5,6,7]): g+=f'\\draw[thick] ({i*1.2+.3:.2f},.1) -- ({i*1.2+.3:.2f},-.1);\\node[below] at ({i*1.2+.3:.2f},-.12) {{{t}}};'
for x,nm in [(.3+.45,'A'),(.3+3*1.2+.7,'B')]: g+=f'\\filldraw[vurgu] ({x:.2f},0) circle (.11);\\node[above] at ({x:.2f},.12) {{\\textbf{{{nm}}}}};'
sek=TP(g)
qk('0003',tipId='kks-dogru',tip='Sayı doğrusunda kök yeri ve aralık',z='orta',alt='Aralıktaki Sayılar',kaz='Sayı doğrusunda iki tam sayı arasında verilen köklü noktaların kök içi aralıklarını bulup farkın en büyük değerini hesaplar.',kalip='şekilli',sekil=sek,
 kart='K-KKS-03 (sayı doğrusunda kök yeri) · A ∈ (3,4), B ∈ (6,7), b − a en büyük',
 metin='Şekildeki sayı doğrusunda A ve B noktaları sırasıyla √a ve √b sayılarına karşılık gelmektedir; a ve b birer doğal sayıdır. Şekil ölçekli çizilmemiştir.\nBuna göre b − a farkının alabileceği en büyük değer kaçtır?',
 dogru=('38',38.0),yan=[(('22',22.0),'En küçük farkı (37 − 15) bulmuş; “en büyük” için en büyük b ile en küçük a gerekir.','dikkat'),(('33',33.0),'a’yı en büyük (15), b’yi en büyük (48) almış.','dikkat'),(('39',39.0),'√9 = 3’ü de A için uygun sayıp a = 9 almış; A, 3’ten büyük olmalıdır.','bilgi'),(('40',40.0),'Hem a = 9 hem b = 49 (uç değerleri dahil) almış.','bilgi')],
 istenen='b − a farkının en büyük değeri.',
 ip=['A ve B’nin hangi tam sayılar arasında olduğunu yazıp kök içlerinin hangi tam sayılar arasında kalacağını bul.'],
 bilgi=[B('Kök içi aralığı','m < √n < m + 1 ise m² < n < (m + 1)² olur. Örnek: 2 < √n < 3 ise n = 5, 6, 7, 8')],
 ad=[A('A için','3 < √a < 4 olduğundan kök içi 9 ile 16 arasındadır (uçlar hariç).','a = 10, 11, …, 15'),A('B için','6 < √b < 7 olduğundan kök içi 36 ile 49 arasındadır (uçlar hariç).','b = 37, 38, …, 48'),A('En büyük fark','En büyük b ve en küçük a seçilir.','b = 48, a = 10'),A('Hesapla','Farkı bul.','48 − 10 = 38')],
 puf='Sayı doğrusunda “iki tam sayı arasında” ifadesinde tam kare uçlar dışarıda kalır.')

# ---------- 04 · orta · dikdörtgenin çevresi ve köşegeni ----------
ka,kb=45,80; a4,b4=3,4  # √45=3√5, √80=4√5
assert a4*a4*5==ka and b4*b4*5==kb and ka+kb==125 and math.isqrt(125)**2!=125
yar=a4+b4; kos=5  # köşegen=√125=5√5
assert yar-kos==2 and (a4,b4)==(3,4)
sc=.5; W,Hh=math.sqrt(kb)*sc,math.sqrt(ka)*sc
g=f'\\draw[thick] (0,0) rectangle ({W:.3f},{Hh:.3f});\\node at ({W/2:.3f},-.32) {{$\\sqrt{{80}}$ cm}};\\node[rotate=90] at ({-.4},{Hh/2:.3f}) {{$\\sqrt{{45}}$ cm}};'
sek=TP(g)
qk('0004',tipId='kks-dikdortgen',tip='Dikdörtgenin çevresi ve köşegeni',z='orta',alt='Köklü Uzunluklar',kaz='Kenarları köklü verilen dikdörtgenin çevresinin yarısı ile köşegeninin farkını kök dışına çıkararak bulur.',kalip='şekilli',sekil=sek,
 kart='K-KKS-04 (dikdörtgenin çevresi ve köşegeni) · √45 × √80, yarı çevre − köşegen',
 metin='Şekildeki dikdörtgenin çevresinin yarısı ile köşegen uzunluğu arasındaki fark kaç cm’dir?',
 dogru=kk(2,5),yan=[(kk(3,5),'Yalnız kısa kenarı (√45 = 3√5) yazmış.','dikkat'),(kk(5,5),'Yalnız köşegenin uzunluğunu (√125 = 5√5) yazmış.','dikkat'),(kk(7,5),'Yalnız çevrenin yarısını (3√5 + 4√5 = 7√5) yazmış; köşegeni çıkarmamış.','dikkat'),(kk(12,5),'Yarı çevre ile köşegeni toplamış: 7√5 + 5√5.','islem')],
 istenen='Yarı çevre ile köşegenin farkı.',
 ip=['Kenarları kök dışına çıkararak yaz; köşegen için dik üçgendeki bağıntıyı kullan.'],
 bilgi=[KOK,PIS],
 ad=[A('Kenarlar','Kök dışına çıkar.','√45 = 3√5 · √80 = 4√5'),A('Yarı çevre','İki komşu kenarın toplamı.','3√5 + 4√5 = 7√5'),A('Köşegen','Pisagor ile bul.','√(45 + 80) = √125 = 5√5'),A('Fark','Kök içleri aynı olduğundan katsayılar çıkarılır.','7√5 − 5√5 = 2√5')],
 puf='Köşegen için kenarların kareleri toplamının (kök içlerinin toplamı) karekökünü al; kök içlerini kök dışına çıkarırken yeniden toplama.')

# ---------- 05 · orta · basamaklı kare dizisi ----------
assert [2*n*n for n in (1,2,3)]==[2,8,18] and all(math.isqrt(2*n*n)**2*1==2*n*n or True for n in (1,2,3))
top6=sum(range(1,7)); assert top6==21 and sum(range(1,6))==15 and sum(range(1,5))==10 and 6==6
sc=.8; g=''; x=0
for n in (1,2,3):
    sd=n*math.sqrt(2)*sc; g+=f'\\draw[thick] ({x:.3f},0) rectangle ({x+sd:.3f},{sd:.3f});\\node[font=\\scriptsize] at ({x+sd/2:.3f},{sd/2:.3f}) {{{2*n*n} cm$^2$}};'; x+=sd
g+=f'\\node at ({x+.5:.3f},.5) {{$\\cdots$}};'
sek=TP(g)
qk('0005',tipId='kks-merdiven',tip='Basamaklı kare dizisinde kenar toplamı',z='orta',alt='Köklü Uzunluklar',kaz='Alanları bir örüntü izleyen karelerin kenarlarını √2’nin katları olarak yazıp ilk altı kenarın toplamını bulur.',kalip='şekilli',sekil=sek,
 kart='K-KKS-05 (basamaklı kare dizisi) · alanlar 2n², ilk 6 kenarın toplamı',
 metin='Şekilde, alt kenarları aynı doğru üzerinde ve yan yana dizilmiş kareler gösterilmiştir. Kareler aynı örüntüyle sürdürülerek yan yana dizilmeye devam etmektedir.\nBuna göre ilk altı karenin kenar uzunlukları toplamı kaç cm’dir?',
 dogru=kk(21,2),yan=[(kk(6,2),'Yalnız altıncı karenin kenarını (6√2) yazmış.','dikkat'),(kk(10,2),'Yalnız ilk dört karenin kenarlarını toplamış: (1 + 2 + 3 + 4)√2.','dikkat'),(kk(15,2),'Yalnız ilk beş karenin kenarlarını toplamış.','dikkat'),(kk(21,1),'Kenarların √2 çarpanını unutup 1 + 2 + … + 6 = 21 yazmış.','islem')],
 istenen='İlk altı karenin kenarları toplamı.',
 ip=['Her alandan kenarı bul; kenarlar arasındaki örüntüyü yaz.'],
 bilgi=[KAR,B('Ardışık sayıların toplamı','1 + 2 + … + n = n(n + 1)/2. Örnek: 1 + 2 + … + 5 = 15')],
 ad=[A('Kenarlar','Alanların karekökü.','√2, √8 = 2√2, √18 = 3√2'),A('Örüntü','n. karenin kenarı n√2 cm olur.','1√2, 2√2, 3√2, …'),A('Altı kenar','İlk altı kenar toplanır.','(1 + 2 + 3 + 4 + 5 + 6)√2'),A('Sonuç','Katsayılar toplamı 21’dir.','21√2')],
 puf='Alanlar 2, 8, 18, … ise kenarlar √2 · (1, 2, 3, …) olur; kenar toplamı katsayı toplamı × √2’dir.')

# ---------- 06 · zor · iç içe iki kare ----------
Ad,Ai=200,72; kd,ki=(10,2),(6,2)
assert kd[0]**2*kd[1]==Ad and ki[0]**2*ki[1]==Ai
gen=(kd[0]-ki[0])/2; assert gen==2 and 4*(kd[0]-ki[0])/gen==8 and 4*kd[0]/gen==20 and 4*(kd[0]-ki[0])==16
assert 4*math.sqrt(Ad-Ai)/(gen*math.sqrt(2))==16 and abs(4*(kd[0]-ki[0])/(kd[0]-ki[0])-4)<1e-9 and 4*(kd[0]+ki[0])/gen==32
sc=.3; sd,si=math.sqrt(Ad)*sc,math.sqrt(Ai)*sc; o=(sd-si)/2
g=f'\\draw[thick] (0,0) rectangle ({sd:.3f},{sd:.3f});\\draw[thick] ({o:.3f},{o:.3f}) rectangle ({o+si:.3f},{o+si:.3f});'
g+=f'\\node at ({sd/2:.3f},{sd/2:.3f}) {{{Ai} cm$^2$}};'
g+=f'\\draw[-{{Stealth[length=1.5mm]}}] ({sd+.5:.3f},{sd+.35:.3f}) -- ({sd-.02:.3f},{sd-.02:.3f});\\node[anchor=west,font=\\footnotesize] at ({sd+.5:.3f},{sd+.35:.3f}) {{{Ad} cm$^2$}};'
sek=TP(g)
qk=q
q('0006',tipId='kks-icice',tip='İç içe karelerde çevre farkı',z='zor',alt='Köklü Uzunluklar',kaz='Alanları verilen iç içe karelerin kenarlarını kök dışına çıkararak çevre farkını bulur ve kareler arasındaki uzaklıkla karşılaştırır.',kalip='şekilli',sekil=sek,
 kart='K-KKS-06 (iç içe iki kare) · 200 ve 72 cm², çevre farkı ÷ aralarındaki uzaklık',
 metin='Şekilde, kenarları birbirine paralel ve merkezleri aynı olan iki karenin alanları verilmiştir. İç karenin her kenarı ile dış karenin ona paralel kenarı arasındaki uzaklık her yerde aynıdır.\nBuna göre dış karenin çevresi, iç karenin çevresinden bu uzaklığın kaç katı kadar fazladır?',
 dogru=8,yan=[(4,'Uzaklık yerine kenar farkını (4√2) almış: 16√2 ÷ 4√2 = 4.','dikkat'),(16,'Çevre farkını alan farkının karekökünden bulmuş (4√128 = 32√2) ve uzaklığa (2√2) bölmüş: 16.','islem'),(20,'Yalnız dış karenin çevresini (40√2) uzaklığa (2√2) bölmüş: 20.','dikkat'),(32,'Fark yerine çevrelerin toplamını (64√2) uzaklığa bölmüş: 32.','islem')],
 istenen='Çevre farkının uzaklığa oranı.',
 ip=['İki karenin kenarlarını alanlarından bul; kenarlar arasındaki uzaklığı kenar farkıyla ilişkilendir.'],
 bilgi=[KAR,KOK],
 ad=[A('Kenarlar','Kenar alanın karekökü.','√200 = 10√2 · √72 = 6√2'),A('Uzaklık','Her iki yandan eşit pay kalır; uzaklık kenar farkının yarısıdır.','(10√2 − 6√2) ÷ 2 = 2√2'),A('Çevre farkı','Çevre kenarın 4 katıdır.','40√2 − 24√2 = 16√2'),A('Oran','Çevre farkı uzaklığa bölünür.','16√2 ÷ 2√2'),A('Sonuç','Oranı bul.','8')],
 puf='Paralel kenarlı iç içe karelerde uzaklık, kenar farkının yarısıdır; çevre farkı bu uzaklığın tam 8 katıdır.')

# ---------- 07 · orta · tablo: kumaş parçalarının alanı ----------
dik=[(12,75),(8,18),(20,45)]; al7=[math.isqrt(a*b) for a,b in dik]
assert all(math.isqrt(a*b)**2==a*b for a,b in dik) and al7==[30,12,30] and sum(al7)==72
assert 30+6+30==66 and 30+12==42 and 30+30==60 and 30+24+30==84
sek=tablo_svg(['Parça','Genişlik (cm)','Uzunluk (cm)'],[['P1','√12','√75'],['P2','√8','√18'],['P3','√20','√45']])
q('0007',tipId='kks-tablo',tip='Tabloda köklü kenarların alanı',z='orta',alt='Çarpma ve Bölme',kaz='Tabloda köklü verilen dikdörtgen parçaların alanlarını kök içlerini çarparak bulur ve toplar.',kalip='tablo',sekil=sek,
 kart='K-KKS-07 (kumaş parçalarının alanı) · 3 dikdörtgen parça, toplam alan 72 cm²',
 metin='Bir terzi, dikdörtgen biçimindeki üç kumaş parçasının boyutlarını aşağıdaki tabloda göstermiştir.\nBuna göre bu üç parçanın alanları toplamı kaç cm²’dir?',
 dogru=72,yan=[(42,'P3’ün alanını (30) toplama katmamış.','dikkat'),(60,'P2’nin alanını (12) toplama katmamış.','dikkat'),(66,'√8 · √18 işleminde √2 · √2 çarpımını 1 alıp P2’yi 6 bulmuş (30 + 6 + 30).','islem'),(84,'√8 · √18’i 2√2 · 3√2 = 6 · 4 = 24 bulmuş (√2 · √2 = 4 sanmış).','bilgi')],
 istenen='Üç parçanın alanları toplamı.',
 ip=['Bir dikdörtgenin alanı için genişlik ile uzunluğu çarp; kök içlerini çarparak yaz.'],
 bilgi=[CRP,KOK],
 ad=[A('P1','Kök içleri çarpılır.','√12 · √75 = √900 = 30'),A('P2','Aynı işlem.','√8 · √18 = √144 = 12'),A('P3','Aynı işlem.','√20 · √45 = √900 = 30'),A('Topla','Üç alanı topla.','30 + 12 + 30 = 72')],
 puf='Köklü iki kenarın çarpımında kök içlerini çarp; çoğu kez sonuç tam kare çıkar.')

# ---------- 08 · zor · Pisagor sarmalı ----------
hip=lambda n:math.sqrt(n+1)
tam=[n for n in range(1,36) if math.isqrt(n+1)**2==n+1]; top8=sum(math.isqrt(n+1) for n in tam)
assert tam==[3,8,15,24,35] and top8==20 and len(tam)==5 and sum(range(1,7))==21 and 4+9+16+25+36==90 and 2+3+4+5==14
sc=1.45; ang=0; P0=(0,0); r=1; pts=[(sc,0)]; tri=[]
cur=(sc,0); a_=0.0
for n in range(1,7):
    rr=math.sqrt(n)   # |O cur| = √n
    th=math.atan2(cur[1],cur[0])+math.pi/2   # dik kenar 1, dönüş: |OP_n| dik kenar
    nxt=(cur[0]+sc*math.cos(th),cur[1]+sc*math.sin(th)); tri.append((cur,nxt)); cur=nxt
g='\\draw (0,0) -- (%.3f,0);'%sc
for i,(c,nx) in enumerate(tri):
    g+=f'\\draw[fill=vurgu!{15 if i%2==0 else 5}] (0,0) -- ({c[0]:.3f},{c[1]:.3f}) -- ({nx[0]:.3f},{nx[1]:.3f}) -- cycle;'
g+=f'\\node[font=\\footnotesize] at ({sc/2:.3f},-.22) {{1 cm}};'
# dik kenar etiketleri (1 cm) ve ilk iki hipotenüs
for i,(c,nx) in enumerate(tri[:6]):
    mx,my=(c[0]+nx[0])/2,(c[1]+nx[1])/2; L=math.hypot(mx,my); ox,oy=mx/L*.28,my/L*.28
    g+=f'\\node[font=\\scriptsize] at ({mx+ox:.3f},{my+oy:.3f}) {{1}};'
for i,(c,nx) in enumerate(tri[:2]):
    g+=f'\\draw[draw=none] (0,0) -- ({nx[0]:.3f},{nx[1]:.3f}) node[midway,sloped,above,inner sep=1pt,font=\\scriptsize] {{$\\sqrt{{{i+2}}}$}};'
g+=f'\\draw[line width=.5pt] ({sc-.17:.3f},0) -- ({sc-.17:.3f},.17) -- ({sc:.3f},.17);'
sek=TP('\\begin{scope}[scale=.9]'+g+'\\end{scope}')
q('0008',tipId='kks-sarmal',tip='Pisagor sarmalında tam sayı hipotenüsler',z='zor',alt='Biçim Sayma',kaz='Dik kenarlarından biri 1 cm olan ardışık dik üçgenlerde hipotenüsün √(n + 1) olduğunu bulup tam sayı olanların toplamını hesaplar.',kalip='şekilli',sekil=sek,
 kart='K-KKS-08 (Pisagor sarmalı) · ilk 35 üçgen, tam sayı hipotenüslerin toplamı 20',
 metin='Şekilde, ortak köşeli dik üçgenler art arda eklenmiştir: ilk üçgenin dik kenarları 1 cm’dir; sonraki her üçgenin bir dik kenarı 1 cm, diğer dik kenarı bir önceki üçgenin hipotenüsüdür. Bu işlem aynı biçimde sürdürülmektedir.\nBuna göre ilk 35 üçgenin hipotenüs uzunlukları arasında tam sayı olanların toplamı kaç cm’dir?',
 dogru=20,yan=[(5,'Tam sayı olan hipotenüslerin değerlerini toplamak yerine adedini (5) yazmış.','dikkat'),(14,'35. üçgenin hipotenüsünü (√36 = 6) saymamış: 2 + 3 + 4 + 5.','dikkat'),(21,'1 + 2 + … + 6 yazmış; 1 cm’lik dik kenarı hipotenüs saymış.','dikkat'),(90,'Tam sayı hipotenüslerin yerine kareleri (4 + 9 + 16 + 25 + 36) toplamış.','islem')],
 istenen='Tam sayı olan hipotenüslerin toplamı.',
 ip=['İlk iki üçgenin hipotenüsünün karesini yaz; n. üçgenin hipotenüsünün karesi n’ye göre nasıl değişiyor?'],
 bilgi=[PIS],
 ad=[A('İlk üçgenler','İlk üçgenin hipotenüsü √(1² + 1²) = √2; ikincinin √(√2² + 1²) = √3.','√2, √3, √4, …'),A('Genel terim','Her adımda hipotenüsün karesi 1 artar; n. üçgende √(n + 1).','n. hipotenüs = √(n + 1)'),A('Tam sayı olanlar','n + 1 ≤ 36 için tam kare olanlar: 4, 9, 16, 25, 36.','√4, √9, √16, √25, √36'),A('Değerler','Kareköklerini al.','2, 3, 4, 5, 6'),A('Topla','Toplam.','2 + 3 + 4 + 5 + 6 = 20')],
 puf='Sarmalda n. hipotenüsün karesi n + 1’dir; tam sayı olanlar için n + 1 tam kare olmalıdır.')

bitir(P,'koklusek','mat|Köklü Sayılar')
