"""AYT Matematik · Diziler 2. dalga (20 soru, hafif mod): koşul ilişkileri, periyot/işaretli özyineleme, ara terim, ortak terim, teleskopik toplam, şekilli örüntüler.
Şekil ve metin aynı değerlerden üretilir; her cevap ve çeldirici değeri kodla hesaplanıp assert edilir. Kardeş yok, ipucu 1."""
import sys,os,json
HD0=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(HD0,'..')
sys.path.insert(0,os.path.join(HV,'tyt-mat')); sys.path.insert(0,HV)
import _hafif_mat as H
from _hafif_mat import *
from _hafif_mat import tablo_svg
from cizim import tikz_svg
from fractions import Fraction as Fr
import sympy as sp
H.KONU='Diziler'
UK='amat|Diziler'
P=Parti('diziiki','Diziler',UK,ders='AYT Matematik',idon='aytmat')
KY='ÖSYM 2018–2026 AYT Matematik (Diziler soruları; yalnız mantık) · Bilgi Sarmal, Acil ve 345 yayınları (yalnız mantık) · MEB 11. sınıf matematik'
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)
def fig(body,font='\\small'): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font='+font+']\n'+body+'\n\\end{tikzpicture}')
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)
ar=lambda a1,d,n:a1+(n-1)*d
arS=lambda a1,d,n:Fr(n*(2*a1+(n-1)*d),2)
BL='blue!70!black'; OR='orange!90!black'
ONC5=['Yalnız I','Yalnız III','I ve II','I ve III','II ve III']

# ---------- bilgi kutuları (örnekler soruların sayılarından farklı) ----------
ARI=B('Aritmetik dizi','ardışık terimler arasındaki fark sabittir (ortak fark d). aₙ = a₁ + (n − 1)·d ve Sₙ = n·(a₁ + aₙ)/2 dir. Örnek: a₁ = 5, d = 3 ise a₆ = 5 + 5·3 = 20 olur.')
GEO=B('Geometrik dizi','ardışık iki terimin oranı sabittir (ortak çarpan r). aₙ = a₁·rⁿ⁻¹ ve r ≠ 1 iken Sₙ = a₁·(rⁿ − 1)/(r − 1) dir. Örnek: a₁ = 2, r = 5 ise a₃ = 2·5² = 50 olur.')
ORB=B('Ardışık üç terim','a, b, c sayıları bir aritmetik dizinin ardışık terimleriyse 2b = a + c; bir geometrik dizinin ardışık terimleriyse b² = a·c dir. Örnek: 2, x, 18 geometrik ardışık ise x² = 36 dır.')
OZB=B('Özyinelemeli dizi','bir terim, kendinden önceki terimle tanımlanır ve ilk terim ayrıca verilir. Örnek: a₁ = 2 ve aₙ₊₁ = aₙ + 3n ise a₂ = 5, a₃ = 11 olur.')
SNB=B('Toplamdan terime','n ≥ 2 için aₙ = Sₙ − Sₙ₋₁ dir; a₁ = S₁ ayrıca hesaplanır. Örnek: Sₙ = n² + 1 ise a₁ = 2 ve n ≥ 2 için aₙ = 2n − 1 olur.')
ORU=B('Örüntü ve genel terim','şekilden şekile eklenen parça sayısı incelenir; fark sabitse genel terim doğrusal, farkın farkı sabitse ikinci derecedendir. Örnek: 2, 5, 8, … örüntüsünde fark 3 olduğundan aₙ = 3n − 1 dir.')
PER=B('Periyodik dizi','terimler belirli bir uzunlukta tekrar ediyorsa toplam, tam tekrarların toplamı ile kalan terimlerin toplamı olarak bulunur. Örnek: 1, 4, 1, 4, … dizisinde ilk 7 terimin toplamı 3·5 + 1 = 16 dır.')
EKS=B('Aritmetik dizide işaret','ortak farkı pozitif olan aritmetik dizide terimler artar; terimlerin işareti, dizinin sıfırı hangi sırada geçtiğine bağlıdır.')
IKD=B('İkinci dereceden genel terim','aₙ = n² + bn + c dizisinde, n = −b/2 eksenine eşit uzaklıktaki sıralarda terimler eşittir; negatif terimlerin sayısı aₙ < 0 eşitsizliğini sağlayan pozitif tam sayıların sayısıdır. Örnek: aₙ = n² − 6n için a₁ = a₅ ve a₂ = a₄ tür.')
TAB=B('Tek ve çift indisli terimler','bir geometrik dizinin tek indisli terimleri ile çift indisli terimleri ayrı geometrik dizilerdir. Örnek: 2, 6, 18, 54 dizisinde tek indisli terimler 2, 18 ve çift indisli terimler 6, 54 tür.')
TEL=B('Teleskopik toplam','ardışık terimlerde birbirini götüren parçalar sadeleşir. Örnek: 1/n − 1/(n + 1) ifadesinin n = 1, 2, 3 için toplamı 1 − 1/4 = 3/4 tür.')
ARL=B('Aralıktaki terimler','x ≡ r (mod m) biçimindeki sayılar ortak farkı m olan bir aritmetik dizi oluşturur; terim sayısı (son − ilk)/m + 1 dir. Örnek: 4 ile bölümünden kalan 1 olan iki basamaklı sayılar 13, 17, …, 97 olup (97 − 13)/4 + 1 = 22 tanedir.')
ORT=B('Ortak terimler','iki aritmetik dizinin ortak terimleri de bir aritmetik dizi oluşturur. Örnek: 2, 5, 8, … ve 3, 5, 7, … dizilerinin ortak terimleri 5, 11, 17, … biçimindedir.')
FAZ=B('Bileşik faiz','yıllık %p bileşik faizde bir yılın sonunda para (1 + p/100) katına çıkar; farklı zamanlarda yatırılan paralar ayrı ayrı büyütülüp toplanır. Örnek: %20 faizle 500 TL, 2 yıl sonra 500·1,2² = 720 TL olur.')

# ---------- kartlar (her tipId için bir kart) ----------
kartla('K-ADZ2-01','Örüntü ve genel terim','Şekil, tablo ya da sayı piramidinden terimler okunur; fark ve farkın farkı incelenerek genel terim kurulur, istenen sıraya ya da koşula uygulanır.','İlk iki farka bakıp her örüntüyü doğrusal sanmak; şekil numarası ile terim sayısını karıştırmak; satır sayısı ile bir fazlasını karıştırmak.','orta','şekilli',3,'dzi-ornt','Örüntü ve genel terim')
kartla('K-ADZ2-02','Aralıkta terim sayısı ve ara terim','Verilen aralıktaki koşulu sağlayan sayılar ya da iki sayı arasına yerleştirilen terimler tek bir dizi olarak yazılır; ilk terim, son terim ve fark belirlenir.','Uçları da sayarken bir eksik ya da fazla almak; kalan koşulunda ilk terimi yanlış belirlemek; yerleştirilen terim sayısı ile terim sayısını karıştırmak.','orta','şekilli',3,'dzi-aralik','Aralıkta terim sayısı ve ara terim')
kartla('K-ADZ2-03','Geometrik dizi koşulları','Verilen iki bilgiden ortak çarpan bulunur; terimlerin pozitifliği ya da dizinin artanlığı çözümü seçer; sonra istenen terim hesaplanır.','Negatif çarpan olasılığını unutmak; terimler arasındaki adım sayısını yanlış saymak; çarpan yerine oranı fark gibi kullanmak.','orta','grafik',3,'dzi-geobag','Geometrik dizi koşulları')
kartla('K-ADZ2-04','Koşullardan ortak fark ve eşitsizlik','Bilinmeyen ilk terim ve ortak fark, verilen terim ilişkilerinden kurulan denklem ya da eşitsizliklerle bulunur; tam sayı gibi ek koşullar çözüm kümesini daraltır.','Eşitsizlik uçlarını dahil etmek; ortak farkın sıfır olma durumunu elemeyi unutmak; terim indisini bir kaydırmak.','zor','düz',4,'dzi-bagint','Koşullardan ortak fark ve eşitsizlik')
kartla('K-ADZ2-05','Periyodik ve işaretli özyineleme','Kuralın ilk birkaç adımı yazılır; tekrar ya da çift-tek indis düzeni bulunur; sorulan terim ya da toplam tam periyot ve kalan olarak hesaplanır.','Periyodu yanlış saymak; kalan terimleri yanlış yerden başlatmak; (−1)ⁿ işaretini bir kaydırmak.','zor','şekilli',4,'dzi-ozyinek','Periyodik ve işaretli özyineleme')
kartla('K-ADZ2-06','Terimlerin işareti ve ekstremum','Genel terimin ya da şekildeki iki terimin verdiği kuraldan terimlerin işareti incelenir; terim sayısı, simetri ya da en küçük toplam bulunur; öncüller tek tek denetlenir.','Sıfır olan terimi saymak; simetri eksenini yanlış almak; negatif terim sayısını bir fazla ya da eksik bulmak.','orta','grafik',3,'dzi-ekstrem','Terimlerin işareti ve ekstremum')
kartla('K-ADZ2-07','Bileşik büyüme ve uygulama','Farklı zamanlarda yapılan işlemler ayrı ayrı bugüne ya da hedef tarihe taşınır; terimler geometrik dizi oluşturur ve toplanır.','Son yatırımın faiz getirmediğini ya da ilk yatırımın bir dönem eksik büyüdüğünü unutmak; bileşik yerine basit faiz uygulamak.','orta','hikâyeli',4,'dzi-uyg','Bileşik büyüme ve uygulama')
kartla('K-ADZ2-08','Ortak terimler','İki dizinin ortak terimleri, farkların EKOK u kadar ilerleyen yeni bir aritmetik dizi oluşturur; ilk ortak terim şekil ya da tablodan bulunur ve terim sınırı iki dizi için de denetlenir.','Yalnız şekilde görünen ortak terimi saymak; sınırı yalnız bir dizi için denetlemek; EKOK yerine çarpımı almak.','orta','şekilli',3,'dzi-ortakterim','Ortak terimler')
kartla('K-ADZ2-09','Toplam sembolü ve Sₙ','Teleskopik toplamlarda ardışık terimler sadeleşir; Sₙ verildiğinde aₙ = Sₙ − Sₙ₋₁ yazılır ve a₁ ayrıca denetlenir.','Sadeleşmeyen ilk ve son parçayı unutmak; a₁ i genel kurala zorla sokmak; üst sınırı bir kaydırmak.','orta','düz',3,'dzi-toplam','Toplam sembolü ve Sₙ')

# ================= 01 kolay · grafik · geometrik =================
g2,g4=6,24
r2=Fr(g4,g2); assert r2==4; r=2; assert r*r==4 and g2*r**2==g4
v=g4*r**2; assert v==96
e1=g4*4**2; e2=g4+2*Fr(g4-g2,2); e3=g4*r; e4=Fr(g2,r)*r**6
e=[e1,e2,e3,e4]; assert e==[384,42,48,192] and len({v,*e})==5
sx,sy=0.95,0.145; o=[]
for i in range(0,8): o.append(f'\\draw[gray!40,thin] ({i*sx:.2f},0) -- ({i*sx:.2f},{30*sy:.2f});')
for j in range(0,31,6): o.append(f'\\draw[gray!40,thin] (0,{j*sy:.2f}) -- ({7*sx:.2f},{j*sy:.2f});')
o.append(f'\\draw[-{{Stealth}},thick] (-0.2,0) -- ({7*sx+0.5:.2f},0) node[right] {{$n$}};')
o.append(f'\\draw[-{{Stealth}},thick] (0,-0.2) -- (0,{30*sy+0.5:.2f}) node[above] {{$g_n$}};')
for i in range(1,8): o.append(f'\\node[below=2pt,font=\\footnotesize] at ({i*sx:.2f},0) {{{i}}};')
for j in range(6,31,6): o.append(f'\\node[left=2pt,font=\\footnotesize] at (0,{j*sy:.2f}) {{{j}}};')
for n,y,c in [(2,g2,BL),(4,g4,OR)]:
    o.append(f'\\draw[dashed,{c}] ({n*sx:.2f},0) -- ({n*sx:.2f},{y*sy:.2f}) -- (0,{y*sy:.2f});')
    o.append(f'\\fill[{c}] ({n*sx:.2f},{y*sy:.2f}) circle (0.1);')
SK=fig('\n'.join(o))
q('0001',tipId='dzi-geobag',tip='Geometrik dizi koşulları',z='kolay',alt='Geometrik Dizi',kaz='Grafikte verilen iki terimden pozitif terimli geometrik dizinin ortak çarpanını bulup istenen terimi hesaplar.',kalip='grafik',
 kart='K-ADZ2-03 (grafikten iki terim) · g₂ ve g₄ okunur, g₆ istenir',
 metin='Şekilde, terimleri pozitif olan bir (gₙ) geometrik dizisinin 2. ve 4. terimleri, (n, gₙ) noktaları olarak gösterilmiştir.\nBuna göre, g₆ kaçtır?',
 dogru=v,yan=[(e1,'Terimlerin oranını (24/6 = 4) ortak çarpan sanıp iki adım ilerlemiş: 24 × 4².','dikkat'),(e2,'Dizi aritmetikmiş gibi ortak farkı (24 − 6)/2 = 9 bulup 24 + 2 × 9 yazmış.','bilgi'),(e3,'Doğru çarpanı (2) bulmuş ama 4. terimden 6. terime iki adım yerine tek adım ilerlemiş: 24 × 2.','dikkat'),(e4,'g₁ = 3 bulup üssü n almış: 3 × 2⁶.','islem')],
 istenen='Dizinin 6. terimi.',ip=['İki nokta arasındaki sıra farkı kadar adımda terimin kaç katına çıktığını bul.'],bilgi=[GEO],sekil=SK,
 ad=[A('Oranı bul','2. terimden 4. terime iki adım vardır; terim oranı ortak çarpanın karesidir.','r² = 24/6 = 4'),A('Çarpanı seç','Terimler pozitif olduğundan r pozitiftir.','r = 2'),A('6. terime ilerle','4. terimden 6. terime iki adım vardır.','g₆ = 24 × 2² = 96')],
 puf='İki terim arasındaki oran, adım sayısı kadar kuvvetle çarpan olarak okunur.')

# ================= 02 kolay · düz · aralıkta terim =================
ilk=next(x for x in range(100,1000) if x%7==3); son=max(x for x in range(100,1000) if x%7==3)
assert (ilk,son)==(101,997)
v=(son-ilk)//7+1; assert v==129==sum(1 for x in range(100,1000) if x%7==3)
e1=(son-ilk)//7; e2=999//7; e3=(son-3)//7+1; e4=(990-108)//7+1
e=[e1,e2,e3,e4]; assert e==[128,142,143,127] and len({v,*e})==5
q('0002',tipId='dzi-aralik',tip='Aralıkta terim sayısı ve ara terim',z='kolay',alt='Aritmetik Dizi',kaz='Bölme koşulunu sağlayan üç basamaklı sayıları aritmetik dizi olarak yazıp terim sayısını bulur.',kalip='düz',
 kart='K-ADZ2-02 (7 ye bölümünden kalan 3) · üç basamaklı sayıların adedi',
 metin='7 ile bölündüğünde 3 kalanını veren üç basamaklı doğal sayıların kaç tanesi vardır?',
 dogru=v,yan=[(e1,'Terim sayısını (son − ilk)/7 olarak bırakıp 1 eklemeyi unutmuş: (997 − 101)/7.','dikkat'),(e2,'Kalan koşulunu dikkate almadan 999 u 7 ye bölmüş: ⌊999/7⌋.','bilgi'),(e3,'Dizinin ilk terimini 3 alıp iki basamaklı sayıları da saymış: (997 − 3)/7 + 1.','dikkat'),(e4,'İlk ve son terimi (101 ve 997) dışarıda bırakıp 108 den 990 a saymış: (990 − 108)/7 + 1.','islem')],
 istenen='Koşulu sağlayan üç basamaklı sayıların adedi.',ip=['Koşulu sağlayan en küçük ve en büyük üç basamaklı sayıyı bul.'],bilgi=[ARL],
 ad=[A('İlk ve son terimi bul','7k + 3 biçimindeki sayılar arasında üç basamaklıların en küçüğü ve en büyüğü seçilir.','101 ve 997'),A('Ortak farkı yaz','Sayılar 7 şer artar.','d = 7'),A('Terim sayısını bul','aₙ = a₁ + (n − 1)·d denkleminde son terim yazılır.','(997 − 101)/7 + 1 = 129')],
 puf='Terim sayısı, adım sayısından bir fazladır.')

# ================= 03 kolay · şekilli · kibrit =================
sayi=lambda n:3*n+1
assert [sayi(i) for i in (1,2,3)]==[4,7,10]
v=next(n for n in range(1,200) if sayi(n)==100); assert v==33
e=[100//4,(100-7)//3,(100-4)//3,34]; assert e==[25,31,32,34] and len({v,*e})==5
o=[]; s=0.95; ox=0
def stick(x1,y1,x2,y2):
    import math
    L_=math.hypot(x2-x1,y2-y1); ux,uy=(x2-x1)/L_,(y2-y1)/L_; g=0.07
    a=(x1+ux*g,y1+uy*g); b=(x2-ux*g,y2-uy*g)
    o.append(f'\\draw[brown!70!black,line width=2.4pt] ({a[0]:.2f},{a[1]:.2f}) -- ({b[0]:.2f},{b[1]:.2f});')
    o.append(f'\\fill[red!75!black] ({a[0]+ux*0.07:.2f},{a[1]+uy*0.07:.2f}) circle (0.075);')
for k in (1,2,3):
    for i in range(k):
        x=ox+i*s; o.append(f'\\fill[{["blue","orange"][i%2]}!12] ({x:.2f},0) rectangle ({x+s:.2f},{s});')
    for i in range(k+1):
        x=ox+i*s; stick(x,0,x,s)
    for i in range(k):
        x=ox+i*s; stick(x,0,x+s,0); stick(x,s,x+s,s)
    o.append(f'\\node[font=\\small] at ({ox+k*s/2:.2f},-0.4) {{{k}. şekil}};')
    ox+=k*s+0.9
SK=fig('\n'.join(o))
q('0003',tipId='dzi-ornt',tip='Örüntü ve genel terim',z='kolay',alt='Şekil Örüntüsü',kaz='Kibrit çöpü örüntüsünden genel terimi kurup verilen çöp sayısına karşılık gelen şekil numarasını bulur.',kalip='şekilli',
 kart='K-ADZ2-01 (kibrit çöpüyle kare zinciri) · 4, 7, 10 çöp; 100 çöp kaçıncı şekil',
 metin='Şekilde, kibrit çöpleriyle yan yana kareler dizilerek oluşturulan bir örüntünün ilk üç şekli verilmiştir. Örüntü aynı kurala göre sürdürülüyor.\nBuna göre, 100 kibrit çöpüyle oluşturulan şekil kaçıncı şekildir?',
 dogru=v,yan=[(e[0],'Her karenin 4 çöple yapıldığını sanmış: 100/4.','bilgi'),(e[1],'Çöp sayısını 3n + 1 bulmuş ama 2. şekilden saymış: (100 − 7)/3.','dikkat'),(e[2],'Adım sayısını şekil numarası almış: (100 − 4)/3.','dikkat'),(e[3],'3n = 100 denkleminden n = 33,3 bulup yukarı yuvarlamış.','islem')],
 istenen='100 çöp kullanılan şeklin numarası.',ip=['Şekilden şekile eklenen çöp sayısına bak.'],bilgi=[ORU],sekil=SK,
 ad=[A('Çöp sayılarını yaz','Şekillerdeki çöpler sayılır.','4 · 7 · 10'),A('Genel terimi kur','Her yeni kare 3 çöp ekler.','aₙ = 4 + 3(n − 1) = 3n + 1'),A('Denklemi çöz','100 çöp için aₙ = 100 yazılır.','3n + 1 = 100 ⇒ n = 33')],
 puf='Şekilden şekile eklenen parçayı say.')

# ================= 04 zor · düz · ardışık geometrik koşulu =================
a1_,d_=sp.symbols('a1 d')
cz=sp.solve(sp.Eq((a1_+4*d_)**2,(a1_+d_)*(a1_+10*d_)),a1_)
assert cz==[2*d_] or set(cz)=={2*d_}
a1=6;d=3; assert a1==2*d and a1+(a1+d)==15
assert (a1+d,a1+4*d,a1+10*d)==(9,18,36) and 18*18==9*36
v=ar(a1,d,20); assert v==63
e1=ar(10,5,20); e2=ar(a1,d,19); e3=a1+20*d; e4=ar(5,5,20)
e=[e1,e2,e3,e4]; assert e==[105,60,66,100] and len({v,*e})==5
q('0004',tipId='dzi-bagint',tip='Koşullardan ortak fark ve eşitsizlik',z='zor',alt='Aritmetik Dizi',kaz='Aritmetik dizinin üç teriminin geometrik dizi oluşturma koşulundan ilk terim ile ortak farkın ilişkisini kurup istenen terimi bulur.',kalip='düz',
 kart='K-ADZ2-04 (a₂, a₅, a₁₁ geometrik ardışık) · a₁ = 2d bulunur, a₂₀ istenir',
 metin='Terimleri birbirinden farklı olan bir (aₙ) aritmetik dizisi için a₂, a₅ ve a₁₁ terimleri, bu sırayla bir geometrik dizinin ardışık üç terimidir.\na₁ + a₂ = 15\nolduğuna göre, a₂₀ kaçtır?',
 dogru=v,yan=[(e1,'a₁ = 2d ilişkisini bulmuş ama a₁ + a₂ = 15 i a₂ = 15 gibi okuyup d = 5, a₁ = 10 almış: 10 + 19 × 5.','dikkat'),(e2,'a₁ = 6 ve d = 3 değerlerini doğru bulup 19. terimi hesaplamış: 6 + 18 × 3.','islem'),(e3,'Doğru a₁ ve d ile a₂₀ yerine a₁ + 20d yazmış: 6 + 20 × 3.','dikkat'),(e4,'Orta terim koşulunu a₁ = d çıkarıp 3d = 15 den d = 5, a₁ = 5 bulmuş: 5 + 19 × 5.','bilgi')],
 istenen='Dizinin 20. terimi.',ip=['Geometrik dizi koşulunu a₁ ve d cinsinden yaz.'],bilgi=[ARI,ORB],
 ad=[A('Koşulu yaz','Ardışık üç terim koşulu uygulanır, terimler a₁ ve d cinsinden yazılır.','(a₁ + 4d)² = (a₁ + d)(a₁ + 10d)'),A('Sadeleştir','d ≠ 0 olduğundan d ile bölünür.','6d² = 3a₁d ⇒ a₁ = 2d'),A('Toplam koşulunu kullan','a₁ + a₂ = 2a₁ + d = 5d.','5d = 15 ⇒ d = 3 · a₁ = 6'),A('20. terimi bul','Genel terim formülü uygulanır.','a₂₀ = 6 + 19 × 3 = 63')],
 puf='“Terimleri birbirinden farklı” ifadesi ortak farkın sıfır olmadığını söyler; sadeleştirmede kullan.')

# ================= 05 orta · şekilli · iki sayı arasına geometrik =================
a,b=3,192; r=Fr(b,a)**Fr(1,6); assert r==2
t=[a*2**k for k in range(7)]; assert t[-1]==192
v=sum(t[1:-1]); assert v==186
e=[sum(t),sum(t)-a,sum(t)-b,sum(t[1:5])+b]; assert e==[381,378,189,282] and len({v,*e})==5
o=[]; w=1.0
for i in range(7):
    fill='blue!15' if i in (0,6) else 'orange!12'
    txt={0:str(a),6:str(b)}.get(i,'')
    o.append(f'\\draw[line width=1.2pt,fill={fill}] ({i*w:.2f},0) rectangle ({i*w+w:.2f},0.9);')
    if txt: o.append(f'\\node[font=\\small\\bfseries] at ({i*w+w/2:.2f},0.45) {{{txt}}};')
    o.append(f'\\node[font=\\footnotesize,gray!60!black] at ({i*w+w/2:.2f},-0.28) {{{i+1}}};')
SK=fig('\n'.join(o))
q('0005',tipId='dzi-aralik',tip='Aralıkta terim sayısı ve ara terim',z='orta',alt='Geometrik Dizi',kaz='İki uç terim verilen geometrik dizide ortak çarpanı bulup aradaki terimlerin toplamını hesaplar.',kalip='şekilli',
 kart='K-ADZ2-02 (iki sayı arasına 5 geometrik terim) · uçlar 3 ve 192, aradaki beş terimin toplamı',
 metin='Şekildeki yedi kutunun birinci ve yedinci kutularına birer sayı yazılmıştır; kutular soldan sağa 1, 2, …, 7 diye numaralanmıştır. Boş kutulara, kutulardaki sayılar soldan sağa doğru bir geometrik dizinin ardışık terimleri olacak biçimde pozitif sayılar yazılıyor.\nBuna göre, boş beş kutudaki sayıların toplamı kaçtır?',
 dogru=v,yan=[(e[0],'Yedi kutudaki bütün sayıları toplamış: 3 + 6 + … + 192.','dikkat'),(e[1],'İlk kutudaki 3 ü çıkarıp son kutudaki 192 yi toplama katmış.','dikkat'),(e[2],'Son kutudaki 192 yi çıkarıp ilk kutudaki 3 ü toplama katmış.','dikkat'),(e[3],'Son boş kutudaki sayıyı 96 yerine yedinci kutudaki 192 ile karıştırmış: 6 + 12 + 24 + 48 + 192.','islem')],
 istenen='Boş kutulardaki sayıların toplamı.',ip=['Birinci kutudan yedinci kutuya kaç adım ilerlendiğine bak.'],bilgi=[GEO],sekil=SK,
 ad=[A('Ortak çarpanı bul','Birinci kutudan yedinci kutuya altı adım vardır.','3·r⁶ = 192 ⇒ r⁶ = 64 ⇒ r = 2'),A('Aradaki terimleri yaz','Çarpan pozitif olduğundan terimler 2 ile çarpılarak ilerler.','6 · 12 · 24 · 48 · 96'),A('Topla','Beş terim toplanır.','6 + 12 + 24 + 48 + 96 = 186')],
 puf='İki uç terimi geometrik dizi formülüyle ilişkilendir.')

# ================= 06 orta · tablo · dört terim toplamı sabit =================
p1,p2,p3=6,2,9; T4=22; p4=T4-p1-p2-p3; assert p4==5
per=[p1,p2,p3,p4]; seq=lambda n:per[(n-1)%4]
assert seq(5)==6 and seq(2)==2 and seq(3)==9
for n in range(1,40): assert seq(n)+seq(n+1)+seq(n+2)+seq(n+3)==22
v=sum(seq(n) for n in range(1,31)); assert v==162
e1=7*22; e2=7*22+seq(3)+seq(4); e3=Fr(30,4)*22; e4=8*22
e=[e1,e2,e3,e4]; assert e==[154,168,165,176] and len({v,*e})==5
SK=tablo_svg(['n','2','3','5'],[['aₙ','2','9','6']])
q('0006',tipId='dzi-ozyinek',tip='Periyodik ve işaretli özyineleme',z='orta',alt='Periyodik Dizi',kaz='Ardışık dört teriminin toplamı sabit olan dizinin periyodunu bulup ilk otuz terimin toplamını hesaplar.',kalip='tablo',
 kart='K-ADZ2-05 (ardışık dört terim toplamı sabit) · tablodan terimler, S₃₀',
 metin='Herhangi ardışık 4 teriminin toplamı 22 olan bir (aₙ) dizisinin bazı terimleri aşağıdaki tabloda verilmiştir.\nBuna göre, a₁ + a₂ + a₃ + … + a₃₀ toplamı kaçtır?',
 dogru=v,yan=[(e1,'Otuz terimde yedi tam grup olduğunu görüp kalan iki terimi toplamaya katmamış: 7 × 22.','dikkat'),(e2,'Kalan iki terimi a₃ ve a₄ almış: 7 × 22 + a₃ + a₄.','dikkat'),(e3,'30/4 oranını gruplarla çarpmış: 7,5 × 22.','bilgi'),(e4,'Kalan terimler için bir grup daha ekleyip 8 grup almış: 8 × 22.','islem')],
 istenen='İlk 30 terimin toplamı.',ip=['İki ardışık dörtlü toplamı yan yana yazıp ortak terimleri sadeleştir.'],bilgi=[PER],sekil=SK,
 ad=[A('Periyodu bul','n ve n + 1 den başlayan dörtlü toplamlar eşit olduğundan aₙ = aₙ₊₄ olur.','a₁ = a₅ = 6'),A('Tek periyodu yaz','4. terim toplam koşulundan bulunur.','a₁ + a₂ + a₃ + a₄ = 22 ⇒ a₄ = 5'),A('Grupla','30 = 7 × 4 + 2; kalan terimler a₁ ve a₂ gibi başa dönenlerdir.','7 × 22 + (6 + 2)'),A('Hesapla','Toplanır.','154 + 8 = 162')],
 puf='Toplamı eşit gruplara ayırarak hesapla.')

# ================= 07 orta · düz · işaretli özyineleme =================
def rec(f,a1,N):
    a=[None,a1]
    for n in range(1,N): a.append(f(a[n],n))
    return a
A1=rec(lambda a,n:a+(-1)**n*2*n,2,30); A2=rec(lambda a,n:a+(-1)**(n+1)*2*n,2,30)
v=A1[25]-A1[20]; assert v==44
e1=A2[25]-A2[20]; e2=A1[25]-A1[19]; e3=A1[25]+A1[20]; e4=A1[24]-A1[20]
e=[e1,e2,e3,e4]; assert e==[-44,6,8,-4] and len({v,*e})==5
q('0007',tipId='dzi-ozyinek',tip='Periyodik ve işaretli özyineleme',z='orta',alt='Özyinelemeli Dizi',kaz='İşaret değiştiren özyineleme kuralından tek ve çift indisli terimlerin genel kalıbını bulup iki terimin farkını hesaplar.',kalip='düz',
 kart='K-ADZ2-05 (aₙ₊₁ = aₙ + (−1)ⁿ·2n) · a₁ = 2, a₂₅ − a₂₀',
 metin='a₁ = 2 ve her n pozitif tam sayısı için\naₙ₊₁ = aₙ + (−1)ⁿ · 2n\neşitliğini sağlayan (aₙ) dizisi veriliyor.\nBuna göre, a₂₅ − a₂₀ farkı kaçtır?',
 dogru=v,yan=[(e1,'(−1)ⁿ işaretini bir kaydırıp tek n için eklemiş, çift n için çıkarmış gibi hesaplamış; farkın işareti ters çıkmış.','dikkat'),(e2,'a₂₀ yerine a₁₉ u alıp a₂₅ − a₁₉ farkını bulmuş.','dikkat'),(e3,'Fark yerine a₂₅ + a₂₀ toplamını hesaplamış.','islem'),(e4,'Farkı a₂₅ yerine a₂₄ için hesaplamış: a₂₄ − a₂₀.','dikkat')],
 istenen='a₂₅ − a₂₀ farkı.',ip=['İlk birkaç terimi yazıp tek ve çift indisli terimlerin ayrı ayrı nasıl değiştiğine bak.'],bilgi=[OZB],
 ad=[A('İlk terimleri yaz','Kural n = 1, 2, 3, … için uygulanır.','a₂ = 0 · a₃ = 4 · a₄ = −2 · a₅ = 6'),A('Kalıbı bul','Tek indislerde terimler 2 şer artar, çift indislerde 2 şer azalır.','a₂ₖ₊₁ = 2k + 2 · a₂ₖ = 2 − 2k'),A('Terimleri hesapla','25 = 2·12 + 1 ve 20 = 2·10.','a₂₅ = 26 · a₂₀ = −18'),A('Farkı al','Çıkarma yapılır.','26 − (−18) = 44')],
 puf='Tek ve çift indisli terimleri ayrı iki dizi gibi incele.')

# ================= 08 orta · öncüllü · ikinci dereceden genel terim =================
an=lambda n:n*n-14*n+3
mn=min(range(1,60),key=an); assert mn==7 and an(7)==-46
t1=all(an(7)<=an(n) for n in range(1,100)); t2=an(4)==an(9); neg=sum(1 for n in range(1,100) if an(n)<0); t3=(neg==12)
assert (t1,t2,t3,neg)==(True,False,False,13) and an(4)==-37 and an(9)==-42
dog='Yalnız I'; sira=ONC5; assert dog in sira
q('0008',tipId='dzi-ekstrem',tip='Terimlerin işareti ve ekstremum',z='orta',alt='Genel Terim',kaz='İkinci dereceden genel terimli dizide en küçük terimi, simetriyi ve negatif terim sayısını inceler.',kalip='öncüllü',
 kart='K-ADZ2-06 (aₙ = n² − 14n + 3) · en küçük terim, simetri, negatif terim sayısı',
 metin='Genel terimi aₙ = n² − 14n + 3 olan (aₙ) dizisi için\nI. En küçük terim a₇ dir.\nII. a₄ = a₉ dur.\nIII. Dizinin tam 12 terimi negatiftir.\nifadelerinden hangileri doğrudur?',
 dogru=dog,yan=[('Yalnız III','I. öncülde en küçük terimi a₆ ya da a₈ sanmış; III. öncülde a₁₃ = −10 u saymayıp 12 negatif terim bulmuş.','dikkat'),('I ve II','Simetri eksenini n = 6,5 alıp a₄ = a₉ eşitliğini doğru sanmış (gerçek eksen n = 7, eşit olan terimler 4 ve 10 dur); III. öncülü denetlememiş.','dikkat'),('I ve III','II. öncülü doğru saymayıp I. öncülü doğru bulmuş ama negatif terimleri n = 1, …, 12 diye sayıp a₁₃ = −10 u unutmuş.','islem'),('II ve III','I. öncülü yanlış sanıp en küçük terimi başka yerde aramış; II. öncülde eksen n = 6,5 almış ve III. öncülde 12 negatif terim bulmuş.','bilgi')],
 istenen='Doğru olan öncüller.',ip=['aₙ i (n − 7)² cinsinden yazıp simetri eksenini bul.'],bilgi=[IKD],sira=sira,
 ad=[A('Tam kareye çevir','n² − 14n + 3 ifadesi (n − 7)² cinsinden yazılır.','aₙ = (n − 7)² − 46'),A('I. öncülü denetle','Terim n = 7 de en küçüktür.','a₇ = −46 en küçük · I doğru'),A('II. öncülü denetle','Eşit terimler 7 ye eşit uzaklıktaki sıralardır; 4 ün eşi 10 dur.','a₄ = −37 · a₉ = −42 · II yanlış'),A('III. öncülü denetle','aₙ < 0 için n = 1, 2, …, 13 çözümdür (a₁₃ = −10, a₁₄ = 3).','13 negatif terim · III yanlış')],
 puf='İkinci dereceden dizide simetri eksenine eşit uzaklıktaki terimler eşittir.')

# ================= 09 zor · şekilli · iki işlemli özyineleme =================
def f9(first):
    a=[None,1]
    for n in range(1,12):
        op=first if n%2==1 else ('×2' if first=='+2' else '+2')
        a.append(a[n]+2 if op=='+2' else a[n]*2)
    return a
def f9n(first,N):
    a=[None,1]
    for n in range(1,N):
        op=first if n%2==1 else ('×2' if first=='+2' else '+2')
        a.append(a[n]+2 if op=='+2' else a[n]*2)
    return a
A9=f9n('+2',24); B9=f9n('×2',24); v=A9[21]; assert v==5*2**10-4==5116
e1=B9[21]; e2=A9[20]; e3=A9[22]; e4=5*2**11-4
e=[e1,e2,e3,e4]; assert e[1:]==[2558,5118,10236] and len({v,*e})==5
o=[]; w=2.15
for i in range(5):
    o.append(f'\\node[circle,draw,thick,fill=blue!8,minimum size=0.95cm] (c{i}) at ({i*w:.2f},0) {{$a_{i+1}$}};')
o.append(f'\\node[font=\\large] (cd) at ({5*w-0.2:.2f},0) {{$\\cdots$}};')
for i in range(4):
    lab,col=[('+2',BL),('\\times 2',OR)][i%2]
    o.append(f'\\draw[-{{Stealth}},thick,{col}] (c{i}) -- node[above=1pt,{col},font=\\bfseries] {{${lab}$}} (c{i+1});')
o.append(f'\\draw[-{{Stealth}},thick,{BL}] (c4) -- node[above=1pt,{BL},font=\\bfseries] {{$+2$}} (cd);')
o.append(f'\\node[font=\\small] at (0,-0.85) {{$a_1 = 1$}};')
SK=fig('\n'.join(o))
q('0009',tipId='dzi-ozyinek',tip='Periyodik ve işaretli özyineleme',z='zor',alt='Özyinelemeli Dizi',kaz='Ardışık terimler arasında dönüşümlü uygulanan iki işlemin dizisini çözüp uzak bir terimi hesaplar.',kalip='şekilli',
 kart='K-ADZ2-05 (dönüşümlü +2 ve ×2) · a₁ = 1, a₂₁ istenir',
 metin='Şekilde, bir (aₙ) dizisinin ilk terimi ve ilk beş terimi arasındaki geçişlerde uygulanan işlemler gösterilmiştir. Terimler arasındaki geçişler, şekildeki sırayla aynı biçimde sürmektedir.\nBuna göre, a₂₁ kaçtır?',
 dogru=v,yan=[(e1,'İşlemlerin sırasını ters almış: önce ×2, sonra +2.','dikkat'),(e2,'20. terimde durmuş: a₂₀ yi bulup a₂₁ e geçişi (×2) uygulamamış.','dikkat'),(e3,'a₂₁ den sonraki +2 işlemini de uygulamış: a₂₂.','dikkat'),(e4,'Tek indisli terimleri veren bₖ = 5·2ᵏ⁻¹ − 4 kuralında üssü bir fazla almış: 5·2¹¹ − 4.','islem')],
 istenen='Dizinin 21. terimi.',ip=['İlk birkaç terimi yazıp terimlerin nasıl ilerlediğine bak.'],bilgi=[OZB],sekil=SK,
 ad=[A('İlk terimleri yaz','Şekildeki işlemler sırayla uygulanır.','1 · 3 · 6 · 8 · 16'),A('Tek indisli terimlerin kuralını bul','a₂ₖ₊₁ = 2·(a₂ₖ₋₁ + 2) olduğundan bₖ = a₂ₖ₋₁ için bₖ₊₁ = 2bₖ + 4 olur.','bₖ + 4 = 5·2ᵏ⁻¹'),A('a₂₁ i bul','21 = 2·11 − 1 olduğundan k = 11 alınır.','a₂₁ = 5·2¹⁰ − 4 = 5116')],
 puf='Özyineleme kuralını birkaç adım yazıp düzeni ara.')

# ================= 10 zor · hikâyeli · bileşik faiz, yıl başı yatırımları =================
P0=10000; k=Fr(11,10)
v=sum(P0*k**j for j in range(1,5)); assert v==51051
e1=sum(P0*k**j for j in range(0,4)); e2=4*P0+Fr(1,10)*P0*(4+3+2+1); e3=sum(P0*k**j for j in range(0,5)); e4=P0*k**4
e=[e1,e2,e3,e4]; assert e==[46410,50000,61051,14641] and len({v,*e})==5
o=[]; X=1.8
o.append(f'\\draw[-{{Stealth}},thick] (-0.3,0) -- ({4*X+0.7:.2f},0) node[right] {{zaman}};')
for i in range(5):
    o.append(f'\\draw[thick] ({i*X:.2f},-0.1) -- ({i*X:.2f},0.1);')
    o.append(f'\\node[below=3pt,font=\\small] at ({i*X:.2f},0) {{{i}. yıl sonu}};')
for i in range(4):
    o.append(f'\\draw[-{{Stealth}},very thick,{BL}] ({i*X:.2f},1.35) -- ({i*X:.2f},0.12);')
    o.append(f'\\node[above=1pt,font=\\small\\bfseries,{BL}] at ({i*X:.2f},1.35) {{10 000 TL}};')
o.append(f'\\draw[-{{Stealth}},very thick,{OR}] ({4*X:.2f},0.12) -- ({4*X:.2f},1.2);\\node[above=1pt,font=\\small\\bfseries,{OR}] at ({4*X:.2f},1.2) {{$?$}};')
SK=fig('\n'.join(o))
q('0010',tipId='dzi-uyg',tip='Bileşik büyüme ve uygulama',z='orta',alt='Bileşik Faiz',kaz='Farklı zamanlarda yatırılan paraların bileşik faizle büyümesini geometrik dizi toplamı olarak modelleyip bileşik tutarı hesaplar.',kalip='hikâyeli',
 kart='K-ADZ2-07 (yıl başı yatırımları) · yıllık %10 bileşik faiz, 4 yıl sonunda toplam',
 metin='Bir tasarruf sahibi, yıllık %10 bileşik faiz uygulayan bir hesaba, şekilde gösterilen zamanlarda ve miktarlarda para yatırmıştır. Faiz her yılın sonunda hesaptaki paraya eklenmekte, başka hiçbir para yatırılıp çekilmemektedir. Şekilde, ilk yatırım yapıldığı an 0. yıl sonu olarak işaretlenmiştir.\nBuna göre, 4. yıl sonunda hesapta kaç TL bulunur?',
 dogru=v,yan=[(e1,'Yatırımların dönem sayısını birer eksik almış: ilk yatırım 3, son yatırım 0 yıl faiz kazanmış sanmış (10 000·(1 + 1,1 + 1,1² + 1,1³)).','dikkat'),(e2,'Bileşik yerine basit faiz uygulamış: her yatırıma toplam yıl sayısı kadar %10 eklemiş.','bilgi'),(e3,'4. yıl sonunda da bir yatırım yapıldığını düşünüp beş terim toplamış: 10 000·(1 + 1,1 + … + 1,1⁴).','dikkat'),(e4,'Yalnız ilk yatırımın değerini bulmuş: 10 000 · 1,1⁴.','islem')],
 istenen='4. yıl sonundaki hesap bakiyesi.',ip=['Her yatırımın hesapta kaç yıl kaldığını ayrı ayrı yaz.'],bilgi=[FAZ,GEO],sekil=SK,
 ad=[A('Her yatırımın kaldığı süreyi yaz','Yatırımlar 0, 1, 2 ve 3. yıl sonlarında yapılmıştır; 4. yıl sonuna sırasıyla 4, 3, 2 ve 1 yıl kalır.','4 · 3 · 2 · 1 yıl'),A('Büyütülmüş tutarları yaz','Her yatırım 1,1 katsayısıyla yıl sayısı kadar büyütülür.','10 000·(1,1⁴ + 1,1³ + 1,1² + 1,1)'),A('Terimleri hesapla','Kuvvetler hesaplanır.','14 641 + 13 310 + 12 100 + 11 000'),A('Topla','Dört terim toplanır.','51 051')],
 puf='Zaman çizgisini kullanıp her yatırımı ayrı ele al.')

# ================= 11 orta · şekilli · ortak terimler =================
A11=lambda n:7+5*(n-1); B11=lambda n:3+7*(n-1)
assert [A11(i) for i in range(1,5)]==[7,12,17,22] and [B11(i) for i in range(1,5)]==[3,10,17,24]
ya={A11(i) for i in range(1,41)}; yb={B11(i) for i in range(1,41)}
ort=sorted(ya&yb); v=len(ort); assert v==6 and ort[0]==17 and ort[1]-ort[0]==35
e1=len([x for x in range(17,277,35)]); e2=202//35; e3=276//35; e4=1
e=[e1,e2,e3,e4]; assert e==[8,5,7,1] and len({v,*e})==5
o=[]; u=0.36
o.append(f'\\draw[-{{Stealth}},thick] (-0.2,0) -- ({26*u+0.5:.2f},0);')
for x in range(0,26):
    h=0.12 if x%5 else 0.2
    o.append(f'\\draw ({x*u:.2f},-{h}) -- ({x*u:.2f},{h});')
    if x%5==0: o.append(f'\\node[below=4pt,font=\\footnotesize] at ({x*u:.2f},-0.2) {{{x}}};')
for i in range(1,5):
    x=A11(i); o.append(f'\\fill[{BL}] ({x*u:.2f},0.55) circle (0.12);\\draw[{BL},dotted] ({x*u:.2f},0.43) -- ({x*u:.2f},0.05);')
    x=B11(i); o.append(f'\\fill[{OR}] ({x*u:.2f},-0.95) circle (0.12);\\draw[{OR},dotted] ({x*u:.2f},-0.83) -- ({x*u:.2f},-0.2);')
o.append(f'\\node[{BL},font=\\small\\bfseries,anchor=west] at ({-0.2:.2f},1.05) {{$a_n$ dizisinin ilk dört terimi}};')
o.append(f'\\node[{OR},font=\\small\\bfseries,anchor=west] at ({-0.2:.2f},-1.55) {{$b_n$ dizisinin ilk dört terimi}};')
SK=fig('\n'.join(o))
q('0011',tipId='dzi-ortakterim',tip='Ortak terimler',z='orta',alt='Aritmetik Dizi',kaz='Sayı doğrusunda verilen iki aritmetik dizinin ilk ortak terimini ve ortak farklarını okuyup ortak terimlerin sayısını bulur.',kalip='şekilli',
 kart='K-ADZ2-08 (iki aritmetik dizi, ortak terimler) · ilk 40 terim içinde ortak terim sayısı',
 metin='Şekildeki sayı doğrusunda, (aₙ) ve (bₙ) aritmetik dizilerinin ilk dörder terimi gösterilmiştir. Her iki dizi de aynı kurala göre sürdürülüyor.\nBuna göre, (aₙ) dizisinin ilk 40 terimi ile (bₙ) dizisinin ilk 40 teriminin ortak olan terimlerinin sayısı kaçtır?',
 dogru=v,yan=[(e1,'Üst sınır olarak b₄₀ ı (276) alıp yalnız (bₙ) dizisinin sınırını denetlemiş.','dikkat'),(e2,'Ortak terimleri 35 in katı sanıp 202/35 in tam kısmını almış.','bilgi'),(e3,'Ortak terimleri 35 in katı sanıp 276/35 in tam kısmını almış.','bilgi'),(e4,'Yalnız şekilde görünen ortak terimi (17) saymış.','dikkat')],
 istenen='İlk 40 terimler arasındaki ortak terimlerin sayısı.',ip=['Ortak terimlerin kendi aralarında ne kadar farkla ilerlediğine bak.'],bilgi=[ORT,ARI],sekil=SK,
 ad=[A('Dizileri oku','Noktaların yerleri okunur.','aₙ = 7 + 5(n − 1) · bₙ = 3 + 7(n − 1)'),A('Ortak terimlerin farkını bul','Ortak farklar 5 ve 7 dir; ortak terimler EKOK kadar ilerler.','ilk ortak terim 17 · fark 35'),A('Sınırı belirle','Terimler iki dizinin de ilk 40 teriminde bulunmalıdır; küçük olan üst sınır geçerlidir.','a₄₀ = 202 < b₄₀ = 276'),A('Say','17 + 35k ≤ 202 eşitsizliği çözülür.','k = 0, 1, …, 5 ⇒ 6 terim')],
 puf='Terimlerin hangi sıralara kadar alındığını dikkatle oku.')

# ================= 12 orta · düz · teleskopik toplam =================
f12=lambda n:sp.sqrt(n+1)-sp.sqrt(n)
for n in range(1,6): assert sp.simplify(1/(sp.sqrt(n)+sp.sqrt(n+1))-f12(n))==0
S=lambda k:sp.sqrt(k+1)-1
v=99; assert S(v)==9
e1=100; e2=80; e3=81; e4=101
assert S(80)!=9 and S(100)!=9 and S(101)!=9 and S(81)!=9
e=[e1,e2,e3,e4]; assert len({v,*e})==5
q('0012',tipId='dzi-toplam',tip='Toplam sembolü ve Sₙ',z='orta',alt='Toplam',kaz='Kök içeren terimlerin eşlenikle sadeleşen toplamını bulup eşitliği sağlayan terim sayısını hesaplar.',kalip='düz',
 kart='K-ADZ2-09 (1/(√n + √(n+1)) toplamı) · toplam 9 ise k',
 metin='k pozitif bir tam sayı olmak üzere\n1/(√1 + √2) + 1/(√2 + √3) + 1/(√3 + √4) + … + 1/(√k + √(k+1)) = 9\neşitliği sağlanıyor.\nBuna göre, k kaçtır?',
 dogru=v,yan=[(e1,'Toplamı √k − 1 bulup √k = 10 dan k = 100 yazmış.','dikkat'),(e2,'Toplamı √(k+1) olarak bırakıp (−1) i yazmamış: √(k+1) = 9 dan k = 80.','dikkat'),(e3,'Toplamı √k olarak bulup √k = 9 dan k = 81 yazmış.','dikkat'),(e4,'k + 1 = 100 bulup k yerine k + 1 i yazmış: 101.','dikkat')],
 istenen='k değeri.',ip=['Her terimin paydasını eşleniğiyle genişlet.'],bilgi=[TEL],
 ad=[A('Terimi sadeleştir','Pay ve payda √(n+1) − √n ile genişletilir.','1/(√n + √(n+1)) = √(n+1) − √n'),A('Toplamı yaz','Ardışık terimler birbirini götürür.','(√2 − √1) + (√3 − √2) + … + (√(k+1) − √k) = √(k+1) − 1'),A('Denklemi çöz','Toplam 9 a eşitlenir.','√(k+1) = 10 ⇒ k + 1 = 100'),A('k yı bul','Çıkarma yapılır.','k = 99')],
 puf='Kökün olduğu paydaları eşlenikle genişletince toplam teleskopik hâle gelir.')

# ================= 13 zor · şekilli · kare dizisi (Fibonacci tipi) =================
s=[2,2]
for i in range(4): s.append(s[-1]+s[-2])
assert s==[2,2,4,6,10,16]
v=s[0]**2+s[2]**2+s[4]**2; assert v==120
t_=Fr(84,2*(13+8)); assert t_==2 and 13*2==26 and 8*2==16
tt=84//21; e1=sum(x*x for x in s); e2=s[1]**2+s[3]**2+s[5]**2; e3=sum(x*x for x in s[:5]); e4=30*tt*tt
e=[e1,e2,e3,e4]; assert e==[416,296,160,480] and len({v,*e})==5 and e1==(s[5]+s[4])*s[5]
rect=[0,0,s[0],s[0]]; sq=[(0,0,s[0])]; dirs=['R','U','L','D','R']
x0,y0,x1,y1=0,0,s[0],s[0]
for i in range(1,6):
    z=s[i]; d=dirs[i-1]
    if d=='R': sq.append((x1,y0,z)); x1+=z; y1=max(y1,y0+z)
    elif d=='U': sq.append((x0,y1,z)); y1+=z
    elif d=='L': sq.append((x0-z,y0,z)); x0-=z
    elif d=='D': sq.append((x0,y0-z,z)); y0-=z
assert (x1-x0,y1-y0)==(26,16)
for i,(x,y,z) in enumerate(sq): assert z==s[i]
u=0.3; o=[]
for i,(x,y,z) in enumerate(sq):
    col='orange!35' if i%2==0 else 'blue!10'
    o.append(f'\\draw[line width=1pt,fill={col}] ({x*u:.2f},{y*u:.2f}) rectangle ({(x+z)*u:.2f},{(y+z)*u:.2f});')
    o.append(f'\\node[font=\\small\\bfseries] at ({(x+z/2)*u:.2f},{(y+z/2)*u:.2f}) {{$a_{i+1}$}};')
o.append(f'\\node[font=\\small,anchor=north west] at ({x0*u:.2f},{(y0-0.4)*u:.2f}) {{Turuncu kareler $a_1, a_3, a_5$ tir.}};')
SK=fig('\n'.join(o))
q('0013',tipId='dzi-ozyinek',tip='Periyodik ve işaretli özyineleme',z='zor',alt='Özyinelemeli Dizi',kaz='Kenarları ardışık iki kenarın toplamı olan karelerden oluşan şekilde özyineleme kuralıyla kenarları bulup işaretli karelerin alanını hesaplar.',kalip='yeni nesil',
 kart='K-ADZ2-05 (kenarı aₙ₊₂ = aₙ₊₁ + aₙ olan kareler) · turuncu üç karenin alanı',
 metin='Şekilde, kenar uzunlukları sırasıyla a₁, a₂, …, a₆ (cm) olan altı kare, bir dikdörtgen oluşturacak biçimde yerleştirilmiştir. Bu uzunluklar her n pozitif tam sayısı için\naₙ₊₂ = aₙ₊₁ + aₙ\neşitliğini sağlamaktadır. Ayrıca a₁ = a₂ dir ve oluşan dikdörtgenin çevresi 84 cm dir.\nBuna göre, şekildeki turuncu karelerin alanları toplamı kaç cm² dir?',
 dogru=v,yan=[(e1,'Altı karenin hepsini turuncu sanıp alanlarını toplamış.','dikkat'),(e2,'Turuncu kareleri a₂, a₄, a₆ olarak okuyup alanlarını toplamış.','dikkat'),(e3,'Turuncu kareleri ayırmadan ilk beş karenin alanlarını toplamış: a₁² + … + a₅².','dikkat'),(e4,'Çevreyi iki kenar toplamı (13a₁ + 8a₁ = 84) sanıp a₁ = 4 bulmuş; 30 · 4² yazmış.','dikkat')],
 istenen='Turuncu karelerin alanları toplamı.',ip=['Kenarları a₁ cinsinden yazmayı dene.'],bilgi=[OZB],sekil=SK,
 ad=[A('Kenarları t cinsinden yaz','Kural ardışık uygulanır.','t, t, 2t, 3t, 5t, 8t'),A('Dikdörtgenin boyutlarını oku','Şekilde en büyük kare dikdörtgenin yüksekliğidir; genişlik a₆ + a₅ tir.','13t × 8t · çevre 42t = 84 ⇒ t = 2'),A('Turuncu kareleri seç','Şekilde turuncu olanlar a₁, a₃ ve a₅ tir.','kenarlar 2 · 4 · 10'),A('Alanları topla','Her karenin alanı kenarının karesidir.','4 + 16 + 100 = 120 cm²')],
 puf='Kenarları kuraldan bulup hangi karelerin turuncu olduğunu şekilden ayır.')

# ================= 14 orta · öncüllü · Sierpinski tipi boyama =================
import math
def adimlar(N):
    kalan=[(0.0,0.0,1.0)]; out=[]
    for st in range(1,N+1):
        yeni=[];kal=[]
        for (x,y,sd) in kalan:
            h=sd/2
            yeni.append(((x+h/2,y+h*math.sqrt(3)/2),(x+h*1.5,y+h*math.sqrt(3)/2),(x+h,y)))
            kal+= [(x,y,h),(x+h,y,h),(x+h/2,y+h*math.sqrt(3)/2,h)]
        out.append((yeni,kal)); kalan=kal
    return out
AD=adimlar(3)
assert [len(a[0]) for a in AD]==[1,3,9] and [len(a[1]) for a in AD]==[3,9,27]
yeni=lambda n:3**(n-1); top=lambda n:(3**n-1)//2; kal=lambda n:3**n
t1=(yeni(4)==27); t2=(top(5)==120); t3=(kal(4)==81)
assert (t1,t2,t3)==(True,False,True) and top(5)==121
dog='I ve III'; assert dog in ONC5
o=[]; L=2.6; gap=0.55
for n in (1,2,3):
    ox=(n-1)*(L+gap)
    for st in range(1,n+1):
        for tri in AD[st-1][0]:
            pts=' -- '.join(f'({ox+L*px:.3f},{L*py:.3f})' for px,py in tri)
            fill='orange!55' if st==n else 'blue!18'
            o.append(f'\\filldraw[fill={fill},draw=black!70,line width=0.5pt] {pts} -- cycle;')
    o.append(f'\\draw[line width=1.2pt] ({ox:.3f},0) -- ({ox+L:.3f},0) -- ({ox+L/2:.3f},{L*math.sqrt(3)/2:.3f}) -- cycle;')
    o.append(f'\\node[font=\\small] at ({ox+L/2:.2f},-0.35) {{{n}. adım}};')
o.append(f'\\fill[orange!55,draw=black!70] (0,-1.0) rectangle (0.3,-0.75);\\node[anchor=west,font=\\footnotesize] at (0.38,-0.875) {{o adımda boyanan}};')
o.append(f'\\fill[blue!18,draw=black!70] ({4.2:.2f},-1.0) rectangle ({4.5:.2f},-0.75);\\node[anchor=west,font=\\footnotesize] at ({4.58:.2f},-0.875) {{önceki adımlarda boyanan}};')
SK=fig('\n'.join(o))
q('0014',tipId='dzi-ornt',tip='Örüntü ve genel terim',z='orta',alt='Geometrik Örüntü',kaz='Üçgenlerin her adımda üç katına çıktığı boyama örüntüsünde geometrik dizi kalıbını kurup sayıları denetler.',kalip='öncüllü',
 kart='K-ADZ2-01 (her adımda kalan üçgenlerin ortasını boyama) · 3ⁿ⁻¹ yeni, (3ⁿ − 1)/2 toplam',
 metin='Şekilde, bir eşkenar üçgenden başlayarak yapılan boyama işleminin ilk üç adımı gösterilmiştir. Her adımda, o ana kadar boyanmamış her küçük üçgenin kenar orta noktaları birleştirilip ortadaki ters üçgen boyanmaktadır. İşlem bu kurala göre sürdürülüyor.\nBuna göre,\nI. 4. adımda yeni boyanan üçgen sayısı 27 dir.\nII. 5. adım sonunda boyanmış toplam üçgen sayısı 120 dir.\nIII. 4. adım sonunda boyanmamış en küçük üçgenlerin sayısı 81 dir.\nifadelerinden hangileri doğrudur?',
 dogru=dog,yan=[('Yalnız I','III. öncülde 4. adımdan sonra kalan üçgenlerin 3⁴ = 81 olduğunu denetlememiş.','dikkat'),('Yalnız III','I. öncülde 4. adımda boyananı 3⁴ = 81 sanmış; III. öncülü doğru saymış.','bilgi'),('I ve II','Toplamı (3⁵ − 3)/2 = 120 alıp (ilk adımı saymamış) II. öncülü doğru sanmış, III. öncülü atlamış.','islem'),('II ve III','I. öncülde 3⁴ yerine 3³ almayıp 4. adımda 81 üçgen boyandığını sanmış; II. öncülü doğru saymış.','dikkat')],
 istenen='Doğru olan öncüller.',ip=['Adım numarası arttıkça yeni boyanan üçgen sayısının kaçla çarpıldığına bak.'],bilgi=[GEO],sira=ONC5,sekil=SK,
 ad=[A('Yeni boyananları say','1., 2., 3. adımlarda 1, 3, 9 üçgen boyanır; her adımda üç katına çıkar.','n. adımda 3ⁿ⁻¹'),A('I. öncülü denetle','n = 4 için 3³ = 27.','I doğru'),A('II. öncülü denetle','İlk beş adımın toplamı geometrik toplamdır.','1 + 3 + 9 + 27 + 81 = 121 · II yanlış'),A('III. öncülü denetle','Her adımda kalan boyanmamış üçgen sayısı 3 katına çıkar: 3, 9, 27, …','3⁴ = 81 · III doğru')],
 puf='Her adımda yeni boyanan sayı ile toplam boyalı sayıyı ayrı ayrı yaz.')

# ================= 15 orta · öncüllü · tablo Sₙ =================
Sf=lambda n:n*n+5*n+2
assert [Sf(i) for i in range(1,5)]==[8,16,26,38]
c=sp.symbols('c0 c1 c2'); n_=sp.symbols('n')
sol=sp.solve([c[0]*i*i+c[1]*i+c[2]-Sf(i) for i in (1,2,3)],c); assert (sol[c[0]],sol[c[1]],sol[c[2]])==(1,5,2)
ak=lambda n:Sf(1) if n==1 else Sf(n)-Sf(n-1)
assert ak(1)==8 and ak(2)==8 and ak(3)==10 and ak(4)==12 and ak(10)==24
t1=(ak(1)==6); t2=(ak(2)==ak(1)); t3=(ak(10)==24)
assert (t1,t2,t3)==(False,True,True)
SK=tablo_svg(['n','1','2','3','4'],[['Sₙ','8','16','26','38']])
q('0015',tipId='dzi-toplam',tip='Toplam sembolü ve Sₙ',z='orta',alt='Sₙ ile aₙ',kaz='Tabloda verilen toplam değerlerinden Sₙ ifadesini kurup terimleri ve dizinin türünü değerlendirir.',kalip='öncüllü',
 kart='K-ADZ2-09 (Sₙ = n² + 5n + 2) · a₁ ayrı, n ≥ 2 için fark',
 metin='İlk n teriminin toplamı Sₙ olan bir (aₙ) dizisi için Sₙ, n nin ikinci dereceden bir polinomudur ve ilk dört değeri aşağıdaki tabloda verilmiştir.\nBuna göre,\nI. a₁ = 6 dır.\nII. a₂ = a₁ dir.\nIII. a₁₀ = 24 tür.\nifadelerinden hangileri doğrudur?',
 dogru='II ve III',yan=[('Yalnız I','a₁ i genel formülle (2·1 + 4) hesaplayıp 6 bulmuş ve I. öncülü doğru sanmış; II. ve III. öncülleri denetlememiş.','dikkat'),('Yalnız III','a₂ yerine S₂ = 16 yı alıp a₂ = a₁ eşitliğini yanlış bulmuş; I. öncülü de yanlış bulmuş, III. öncülü doğru bulmuş.','bilgi'),('I ve II','I. ve II. öncülleri doğru sanıp III. öncülü hesaplamamış.','islem'),('I ve III','a₁ i 6 bulup I. öncülü doğru saymış, a₂ = a₁ eşitliğini yanlış bulmuş.','dikkat')],
 istenen='Doğru olan öncüller.',ip=['a₁ i S₁ den, sonraki terimleri ardışık toplamların farkından bul.'],bilgi=[SNB],sira=['Yalnız I','Yalnız III','I ve II','I ve III','II ve III'],sekil=SK,
 ad=[A('Toplam ifadesini kur','Tablodaki değerlerden Sₙ bulunur.','Sₙ = n² + 5n + 2'),A('Terimleri bul','a₁ = S₁ ve n ≥ 2 için aₙ = Sₙ − Sₙ₋₁ hesaplanır.','a₁ = 8 · aₙ = 2n + 4 (n ≥ 2)'),A('I ve II yi denetle','a₁ = S₁ = 8 ≠ 6; a₂ = S₂ − S₁ = 8.','I yanlış · II doğru (a₂ = a₁)'),A('III. yü denetle','10 ≥ 2 olduğundan genel kural geçerlidir.','a₁₀ = 24 · III doğru')],
 puf='a₁ in genel kuralı sağlayıp sağlamadığını ayrıca denetle.')

# ================= 16 orta · şekilli · tek sayı piramidi =================
rows=[];c=1
for r_ in range(1,13):
    rows.append([c+2*i for i in range(r_)]); c+=2*r_
assert rows[4]==[21,23,25,27,29] and all(sum(r)==len(r)**3 for r in rows)
satir=next(i+1 for i,r in enumerate(rows) if 99 in r); assert satir==10
v=sum(rows[9]); assert v==1000
e=[9**3,10*91,10*99,10*55]; assert e==[729,910,990,550] and 99 not in rows[8]+rows[10] and len({v,*e})==5
o=[]; w=0.95
for i in range(5):
    r=rows[i]; y=-i*0.8
    for j,x in enumerate(r):
        cx=(j-(len(r)-1)/2)*w
        o.append(f'\\node[draw,rounded corners=2pt,minimum width={w-0.1:.2f}cm,minimum height=0.6cm,fill={"blue!10" if i%2==0 else "orange!15"},font=\\small] at ({cx:.2f},{y:.2f}) {{{x}}};')
    o.append(f'\\node[font=\\footnotesize,gray!60!black,anchor=west] at ({2.5*w+0.7:.2f},{y:.2f}) {{{i+1}. satır}};')
SK=fig('\n'.join(o))
q('0016',tipId='dzi-ornt',tip='Örüntü ve genel terim',z='orta',alt='Sayı Piramidi',kaz='Tek sayıların satır satır dizildiği piramitte 99 un bulunduğu satırı bulup o satırın toplamını hesaplar.',kalip='şekilli',
 kart='K-ADZ2-01 (tek sayı piramidi) · satır numarası ve satır toplamı',
 metin='Şekilde, tek doğal sayılar küçükten büyüğe doğru, 1. satırda 1, 2. satırda 2, 3. satırda 3 sayı olacak biçimde satır satır yazılarak bir sayı piramidi oluşturuluyor. Piramidin ilk beş satırı gösterilmiştir. Yazım aynı kurala göre sürdürülüyor.\nBuna göre, 99 sayısının bulunduğu satırdaki sayıların toplamı kaçtır?',
 dogru=v,yan=[(e[0],'99 un 9. satırda olduğunu sanıp o satırın toplamını (9³) almış; ilk 9 satırda 89 a kadar yazıldığını fark etmemiş.','dikkat'),(e[1],'Satırın ilk sayısı 91 i alıp sayı adediyle çarpmış: 10 × 91.','bilgi'),(e[2],'Satırdaki sayı adedini (10) 99 ile çarpmış.','bilgi'),(e[3],'Satırın son sayısının sırasını (55) sayı adediyle çarpmış: 10 × 55.','islem')],
 istenen='99 un bulunduğu satırın toplamı.',ip=['99 un baştan kaçıncı tek sayı olduğunu ve her satırda kaç sayı yazıldığını yan yana yaz.'],bilgi=[ORU,ARI],sekil=SK,
 ad=[A('99 un sırasını bul','İlk tek sayı 1 dir; 99 baştan kaçıncı tek sayıdır?','(99 + 1)/2 = 50. sayı'),A('Satırı bul','k. satıra kadar yazılan sayı adedi 1 + 2 + … + k = k(k + 1)/2 dir; 45 < 50 ≤ 55.','9. satırın sonu 45. sayı · 10. satır 46–55. sayılar'),A('Satırın uçlarını yaz','Satırdaki ilk ve son sayı bulunur.','91 ve 109'),A('Toplamı hesapla','10 terimin toplamı aritmetik dizi formülüyle bulunur.','10·(91 + 109)/2 = 1000')],
 puf='Satır sayısı arttıkça kullanılan sayı adedi bir aritmetik dizinin toplamıdır.')

# ================= 17 zor · tablo · satır ve sütunları aritmetik tablo =================
Tf=lambda i,j:3+2*i+4*j+i*j
G=[[Tf(i,j) for j in range(1,5)] for i in range(1,5)]
assert G[0]==[10,15,20,25] and G[1][2]==25 and G[3][0]==19
for r_ in G: assert len({r_[k+1]-r_[k] for k in range(3)})==1
for j in range(4): assert len({G[k+1][j]-G[k][j] for k in range(3)})==1
al,be,ga,de=sp.symbols('al be ga de')
sol=sp.solve([ (al+be*1+ga*1+de*1)-10,(al+be*1+ga*4+de*4)-25,(al+be*4+ga*1+de*4)-19,(al+be*2+ga*3+de*6)-25],[al,be,ga,de])
assert sol[al]+sol[be]*4+sol[ga]*4+sol[de]*16==43
v=43
d_rows=[5,6]; e1=19+3*5; e2=19+3*6; e3=19+3*7; e4=19+3*4
e=[e1,e2,e3,e4]; assert e==[34,37,40,31] and len({v,*e})==5
o=[]; cs=1.05
given={(0,0):10,(0,3):25,(3,0):19,(1,2):25}
for i in range(4):
    for j in range(4):
        x=j*cs; y=-i*0.8
        if (i,j) in given: fill,txt='blue!15',str(given[(i,j)])
        elif (i,j)==(3,3): fill,txt='orange!45','$x$'
        else: fill,txt='white',''
        o.append(f'\\draw[line width=1pt,fill={fill}] ({x:.2f},{y:.2f}) rectangle ({x+cs:.2f},{y-0.8:.2f});')
        if txt: o.append(f'\\node[font=\\bfseries] at ({x+cs/2:.2f},{y-0.4:.2f}) {{{txt}}};')
SK=fig('\n'.join(o))
q('0017',tipId='dzi-ornt',tip='Örüntü ve genel terim',z='zor',alt='Aritmetik Tablo',kaz='Satırları ve sütunları aritmetik dizi olan tabloda verilen dört hücreden satır farklarının değişimini bulup istenen hücreyi hesaplar.',kalip='tablo',
 kart='K-ADZ2-01 (satır ve sütunları aritmetik tablo) · satır farkları da aritmetik, x köşe hücresi',
 metin='Şekildeki 4 × 4 tablonun her satırındaki sayılar soldan sağa, her sütunundaki sayılar yukarıdan aşağıya doğru birer aritmetik dizi oluşturmaktadır. Tabloda bazı hücrelere sayılar yazılmış, diğer hücreler boş bırakılmıştır.\nBuna göre, x kaçtır?',
 dogru=v,yan=[(e1,'4. satırın farkını 1. satırla aynı (5) alıp 19 + 3 × 5 yazmış.','dikkat'),(e2,'Satır farklarını sabit sanıp 2. satırın farkını (6) tüm satırlara uygulamış: 19 + 3 × 6.','dikkat'),(e3,'Satır farkının satır numarasıyla artığını görüp 3 adımda yalnız 2 artış almış: d₄ = 7.','islem'),(e4,'Satır farklarının azaldığını sanıp d₄ = 5 − 1 = 4 almış: 19 + 3 × 4.','dikkat')],
 istenen='x ile gösterilen hücredeki sayı.',ip=['Önce 1. sütunu ve 1. satırı tamamla, sonra 2. satırın ortak farkını bul.'],bilgi=[ARI],sekil=SK,
 ad=[A('1. sütunu ve satırı tamamla','1. satırda fark 15 / 3 = 5; 1. sütunda fark (19 − 10)/3 = 3 tür.','1. sütun: 10 · 13 · 16 · 19'),A('2. satırın farkını bul','2. satır 13 ten başlar ve 3. hücresi 25 tir.','d₂ = (25 − 13)/2 = 6'),A('Satır farklarının kuralını bul','Her sütun aritmetik olduğundan satır farkları da aritmetik dizi oluşturur.','d₁ = 5 · d₂ = 6 ⇒ d₄ = 8'),A('x i hesapla','4. satır 19 dan başlar, 3 adım ilerler.','x = 19 + 3 × 8 = 43')],
 puf='Önce satır ve sütunlarda bilinen terimleri tamamla.')

# ================= 18 orta · grafik · en küçük toplam =================
b2,b6=-30,-10; d=Fr(b6-b2,4); assert d==5; a1=b2-d; assert a1==-35
anf=lambda n:a1+(n-1)*d
Sn=lambda n:arS(a1,d,n); mnS=min(Sn(n) for n in range(1,40)); assert mnS==-140==Sn(7)==Sn(8)
v=-140
e1=Sn(6); e2=Sn(10); e3=Sn(4); a1b=-30; e4=Fr(6*(2*a1b+5*5),2);
assert (e1,e2,e3,e4)==(-135,-125,-110,-105) and len({v,e1,e2,e3,e4})==5
sx,sy=0.78,0.115; o=[]
for i in range(0,11): o.append(f'\\draw[gray!40,thin] ({i*sx:.2f},0) -- ({i*sx:.2f},{-40*sy:.2f});')
for j in range(0,41,10): o.append(f'\\draw[gray!40,thin] (0,{-j*sy:.2f}) -- ({10*sx:.2f},{-j*sy:.2f});')
o.append(f'\\draw[-{{Stealth}},thick] (-0.2,0) -- ({10*sx+0.5:.2f},0) node[right] {{$n$}};')
o.append(f'\\draw[-{{Stealth}},thick] (0,{-40*sy-0.3:.2f}) -- (0,{0.6:.2f}) node[above] {{$a_n$}};')
for i in range(1,11): o.append(f'\\node[above=2pt,font=\\footnotesize] at ({i*sx:.2f},0) {{{i}}};')
for j in range(10,41,10): o.append(f'\\node[left=2pt,font=\\footnotesize] at (0,{-j*sy:.2f}) {{$-{j}$}};')
for n,y,c in [(2,b2,BL),(6,b6,OR)]:
    o.append(f'\\draw[dashed,{c}] ({n*sx:.2f},0) -- ({n*sx:.2f},{y*sy:.2f}) -- (0,{y*sy:.2f});')
    o.append(f'\\fill[{c}] ({n*sx:.2f},{y*sy:.2f}) circle (0.1);')
SK=fig('\n'.join(o))
q('0018',tipId='dzi-ekstrem',tip='Terimlerin işareti ve ekstremum',z='orta',alt='Aritmetik Dizi',kaz='Grafikten okunan iki terimle aritmetik dizinin terimlerinin işaretini belirleyip toplamın en küçük değerini bulur.',kalip='grafik',
 kart='K-ADZ2-06 (grafikten iki terim, en küçük toplam) · a₂ = −30, a₆ = −10',
 metin='Şekilde, bir (aₙ) aritmetik dizisinin 2. ve 6. terimleri, (n, aₙ) noktaları olarak gösterilmiştir. Dizinin ilk n teriminin toplamı Sₙ ile gösteriliyor.\nBuna göre, Sₙ in alabileceği en küçük değer kaçtır?',
 dogru=v,yan=[(e1,'Toplamı en küçük sanıp 6. terimde durmuş: S₆ (a₇ = −5 negatif terim olduğundan toplam hâlâ azalır).','dikkat'),(e2,'Terim sayısını gereğinden fazla alıp toplam yeniden artarken durmuş: S₁₀.','dikkat'),(e3,'Dört terimde durmuş: S₄.','dikkat'),(e4,'Grafikteki ilk noktayı (n = 2, −30) a₁ sanmış: a₁ = −30, d = 5 ile S₆.','bilgi')],
 istenen='Sₙ in en küçük değeri.',ip=['Ortak farkı bulup terimlerin hangi sıraya kadar negatif olduğuna bak.'],bilgi=[ARI,EKS],sekil=SK,
 ad=[A('Ortak farkı bul','2. terimden 6. terime dört adım vardır.','d = (−10 − (−30))/4 = 5'),A('İlk terimi bul','a₂ = a₁ + d.','a₁ = −35'),A('İşaret değişimini bul','Terimler 5 şer artar: a₇ = −5, a₈ = 0, a₉ = 5.','a₇ ye kadar terimler negatif'),A('En küçük toplamı hesapla','Toplam, negatif terimlerin hepsi toplanınca en küçüktür (a₈ = 0 değişiklik yapmaz).','S₇ = 7·(−35 − 5)/2 = −140')],
 puf='Terimler negatif olduğu sürece toplam azalır; ilk pozitif terimden önce durulur.')

# ================= 19 zor · düz · negatif çarpanlı geometrik, S₁₀ =================
a1=3; r=-2
od=sum(a1*r**(2*k) for k in range(4)); S8=sum(a1*r**k for k in range(8)); assert (od,S8)==(255,-255)
x=sp.symbols('x'); assert sp.solve(sp.Eq(x*255,-510),x)==[-2]
SS=lambda a,r_,n:sum(a*r_**k for k in range(n))
v=SS(3,-2,10); assert v==-1023
e1=SS(3,-2,9); e2=SS(3,-2,11); e3=SS(3,2,10)
assert (e1,e2,e3)==(513,2049,3069)
e4=S8-a1*r**8-abs(a1*r**9); assert e4==-2559
e=[e1,e2,e3,e4]; assert len({v,*e})==5
q('0019',tipId='dzi-geobag',tip='Geometrik dizi koşulları',z='zor',alt='Geometrik Dizi',kaz='Tek indisli terimlerin toplamı ile ilk sekiz terimin toplamından negatif ortak çarpanı bulup ilk on terimin toplamını hesaplar.',kalip='düz',
 kart='K-ADZ2-03 (tek indisli toplam ve S₈) · r = −2, S₁₀',
 metin='(aₙ) bir geometrik dizidir ve ilk n teriminin toplamı Sₙ ile gösteriliyor.\na₁ + a₃ + a₅ + a₇ = 255\nS₈ = −255\nolduğuna göre, S₁₀ kaçtır?',
 dogru=v,yan=[(e1,'Çarpanı doğru bulup ilk 9 terimin toplamını hesaplamış: S₉.','dikkat'),(e2,'Çarpanı doğru bulup ilk 11 terimin toplamını hesaplamış: S₁₁.','dikkat'),(e3,'Oranın işaretini yok sayıp r = 2 alarak 3·(2¹⁰ − 1) yazmış.','bilgi'),(e4,'a₉ ve a₁₀ un ikisini de negatif alıp S₈ e eklemiş: −255 − 768 − 1536.','islem')],
 istenen='İlk 10 terimin toplamı S₁₀.',ip=['Tek indisli terimlerin toplamını S₈ in içinde ara.'],bilgi=[GEO,TAB],
 ad=[A('Çift indisli toplamı bul','S₈, tek ve çift indisli terimlerin toplamıdır.','a₂ + a₄ + a₆ + a₈ = −255 − 255 = −510'),A('Çarpanı bul','Çift indisli her terim, bir önceki tek indisli terimin r katıdır.','r·255 = −510 ⇒ r = −2'),A('İlk terimi bul','Tek indisli terimler a₁·(1 + r² + r⁴ + r⁶) olarak toplanır.','a₁·85 = 255 ⇒ a₁ = 3'),A('S₁₀ u hesapla','Geometrik toplam formülü uygulanır.','3·((−2)¹⁰ − 1)/(−2 − 1) = −1023')],
 puf='Verilen iki toplamdan, istenen toplamla ilişkili üçüncü bir toplam üretmeyi dene.')

# ================= 20 zor · düz · (a₁, d) ikilileri =================
def say(f1,f2,ilk=1):
    return sum(1 for a1 in range(ilk,200) for d in range(1,60) if f1(a1,d) and f2(a1,d))
S10=lambda a1,d:10*a1+45*d
v=say(lambda a,d:S10(a,d)>250,lambda a,d:a+10*d<50); assert v==42
e1=say(lambda a,d:S10(a,d)>250,lambda a,d:a+10*d<=50); e2=say(lambda a,d:S10(a,d)>=250,lambda a,d:a+10*d<50)
e3=say(lambda a,d:S10(a,d)>250,lambda a,d:a+9*d<50); e4=say(lambda a,d:True,lambda a,d:a+10*d<50)
e=[e1,e2,e3,e4]; assert len({v,*e})==5,e
q('0020',tipId='dzi-bagint',tip='Koşullardan ortak fark ve eşitsizlik',z='zor',alt='Aritmetik Dizi',kaz='Terim ve toplam eşitsizliklerini birlikte çözerek ilk terim ve ortak farkın pozitif tam sayı değerlerinden oluşan ikililerin sayısını bulur.',kalip='düz',
 kart='K-ADZ2-04 (S₁₀ ve a₁₁ eşitsizlikleri) · (a₁, d) ikililerinin sayısı',
 metin='İlk terimi a₁ ve ortak farkı d olan bir (aₙ) aritmetik dizisinde a₁ ve d pozitif tam sayılardır. Dizinin ilk 10 teriminin toplamı S₁₀ ile gösterilmektedir.\nS₁₀ > 250\na₁₁ < 50\neşitsizlikleri sağlandığına göre, (a₁, d) sıralı ikililerinin kaç tanesi vardır?',
 dogru=v,yan=[(e1,'İkinci eşitsizliği a₁₁ ≤ 50 okuyup sınır değerleri de saymış.','dikkat'),(e2,'Birinci eşitsizliği S₁₀ ≥ 250 okuyup sınır değerleri de saymış.','dikkat'),(e3,'a₁₁ i a₁ + 9d yazıp 10. terimle karıştırmış.','dikkat'),(e4,'S₁₀ > 250 koşulunu hiç kullanmayıp yalnız a₁₁ < 50 koşulunu sağlayan ikilileri saymış.','bilgi')],
 istenen='Koşulları sağlayan (a₁, d) ikililerinin sayısı.',ip=['Her d değeri için a₁ in alabileceği değerleri ayrı ayrı bul.'],bilgi=[ARI],
 ad=[A('Eşitsizlikleri a₁ ve d cinsinden yaz','S₁₀ = 10a₁ + 45d ve a₁₁ = a₁ + 10d dir.','10a₁ + 45d > 250 · a₁ + 10d < 50'),A('d için üst sınırı bul','a₁ ≥ 1 olduğundan a₁₁ < 50 koşulu d yi sınırlar.','10d < 49 ⇒ d ≤ 4'),A('Her d için a₁ aralığını yaz','Alt sınırı toplam koşulu, üst sınırı terim koşulu verir.','d = 1: 21 ≤ a₁ ≤ 39 · d = 2: 17 ≤ a₁ ≤ 29 · d = 3: 12 ≤ a₁ ≤ 19 · d = 4: 8 ≤ a₁ ≤ 9'),A('Say','Her d için değer sayıları toplanır.','19 + 13 + 8 + 2 = 42')],
 puf='Bir değişkeni sabitleyip diğerinin aralığını bul.')

# ---------- bitiş ----------
def bitir_ayt(P,onek,k):
    for q_ in P.ANA: q_['kardes']=None
    P.yaz(os.path.join(HD0,f'{onek}-1.json'),f'/tmp/bos-{onek}.json')
    tipler={}
    for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=k))['kartlar'].append(c['id'])
    json.dump(dict(konu=P.konu_adi,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 AYT Matematik çıkmış soruları ve yayın soru bankaları (yalnız mantık), MEB 11–12. sınıf müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar',f'{onek}.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler))
bitir_ayt(P,'diziiki',UK)
