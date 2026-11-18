"""AYT Matematik · Diziler (20 soru, hafif mod): aritmetik/geometrik dizi, genel terim, Sn–an ilişkisi, özyineleme, monotonluk.
Şekil ve metin aynı değerlerden üretilir; her cevap ve çeldirici değeri kodla hesaplanıp assert edilir. Kardeş yok, ipucu 1."""
import sys,os,json
HD0=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(HD0,'..')
sys.path.insert(0,os.path.join(HV,'tyt-mat')); sys.path.insert(0,HV)
import _hafif_mat as H
from _hafif_mat import *
from _hafif_mat import tablo_svg
from cizim import tikz_svg
from fractions import Fraction as Fr
from math import isqrt
H.KONU='Diziler'
UK='amat|Diziler'
P=Parti('dizi','Diziler',UK,ders='AYT Matematik',idon='aytmat')
KY='ÖSYM 2018–2026 AYT Matematik (Diziler soruları; yalnız mantık) · Bilgi Sarmal ve Acil yayınları (yalnız mantık) · MEB 11. sınıf matematik'
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)
def fig(body,font='\\small'): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font='+font+']\n'+body+'\n\\end{tikzpicture}')
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)
ar=lambda a1,d,n:a1+(n-1)*d
arS=lambda a1,d,n:Fr(n*(2*a1+(n-1)*d),2)
ge=lambda a1,r,n:a1*Fr(r)**(n-1)
geS=lambda a1,r,n:a1*(Fr(r)**n-1)/(Fr(r)-1)

# ---------- bilgi kutuları (örnekler soruların sayılarından farklı) ----------
ARI=B('Aritmetik dizi','ardışık terimler arasındaki fark sabittir; bu sabite ortak fark (d) denir. aₙ = a₁ + (n − 1)·d ve ilk n terimin toplamı Sₙ = n·(a₁ + aₙ)/2 dir. Örnek: a₁ = 2, d = 5 ise a₄ = 2 + 3·5 = 17 ve S₄ = 4·(2 + 17)/2 = 38 olur.')
GEO=B('Geometrik dizi','ardışık iki terimin oranı sabittir; bu sabite ortak çarpan (r) denir. aₙ = a₁·rⁿ⁻¹ ve r ≠ 1 iken Sₙ = a₁·(rⁿ − 1)/(r − 1) dir. Örnek: a₁ = 4, r = 3 ise a₃ = 4·3² = 36 ve S₃ = 4·(27 − 1)/2 = 52 olur.')
SNB=B('Sₙ ile aₙ ilişkisi','ilk n terimin toplamı Sₙ ise a₁ = S₁ ve n ≥ 2 için aₙ = Sₙ − Sₙ₋₁ dir. Örnek: Sₙ = n² + 1 ise S₃ = 10, S₂ = 5 olduğundan a₃ = 5 tir; a₁ = S₁ = 2 dir.')
OZB=B('Özyinelemeli dizi','bir terim, kendinden önceki terim ya da terimlerle tanımlanır ve ilk terim(ler) ayrıca verilir. Örnek: a₁ = 1 ve aₙ₊₁ = 2·aₙ + 1 ise a₂ = 3, a₃ = 7, a₄ = 15 olur.')
MOB=B('Artan dizi ve sınırlılık','her n için aₙ₊₁ > aₙ ise dizi artandır; her n için aₙ < M olacak biçimde bir M sayısı varsa dizi üstten sınırlıdır. Örnek: aₙ = 1/n dizisinde aₙ₊₁ − aₙ < 0 olduğundan dizi azalandır; her terimi 1 den büyük olmayan bu dizi üstten sınırlıdır.')
GRB=B('Grafikten dizi okuma','bir dizinin grafiği, (n, aₙ) noktalarından oluşur; n yatay eksende, aₙ dikey eksendedir. Noktalar bir doğru üzerindeyse dizi aritmetiktir ve ortak fark, ardışık iki noktanın dikey farkıdır. Örnek: (1, 3) ve (2, 5) noktaları ardışık ise d = 2 dir.')
ORB=B('Ardışık üç terim','a, b, c sayıları bir aritmetik dizinin ardışık terimleriyse 2b = a + c; bir geometrik dizinin ardışık terimleriyse b² = a·c dir. Örnek: 3, x, 12 geometrik ardışık terimlerse x² = 36 olduğundan x = 6 ya da x = −6 dır.')
AKB=B('Akış şeması','dikdörtgen kutu bir işlem, eşkenar dörtgen kutu bir koşul sorusudur; koşul sağlanıyorsa “Evet”, sağlanmıyorsa “Hayır” okundan ilerlenir. “a ← a + 2” kutusu, a nın yeni değerinin eskisinden 2 fazla olduğunu gösterir.')
TAB=B('Tablodan kural','tabloda verilen ardışık terimlerin farkları sabitse dizi aritmetiktir; farkların farkı sabitse genel terim n² li bir ifadedir. Örnek: 2, 6, 12 terimlerinin farkları 4 ve 6 olup farkların farkı 2 dir.')

# ---------- kartlar (her tipId için bir kart) ----------
kartla('K-ADZ-01','Aritmetik dizi ve toplamı','Verilen iki bilgiden ortak fark ve ilk terim kurulur; istenen terim ya da toplam aritmetik dizi formülüyle hesaplanır. Grafik, tablo, sayı doğrusu ve akış şemasından okunan değerler de aynı iki bilinmeyene indirgenir.','Terim sayısını bir fazla ya da eksik almak (n yerine n − 1); sıra farkı ile terim farkını karıştırmak; toplam formülünde 2 ye bölmeyi unutmak.','orta','şekilli',3,'dzi-aritmetik','Aritmetik dizi ve toplamı')
kartla('K-ADZ-02','Genel terim ve örüntü','Şekil ya da tablodaki ilk birkaç terimden farklar incelenir; fark sabitse doğrusal, farkların farkı sabitse ikinci dereceden genel terim kurulur ve sorulan sıraya uygulanır.','Her dizinin aritmetik olduğunu sanmak; ilk farkı sabit alıp ikinci farkı görmemek; sıra numarasını bir kaydırmak.','orta','şekilli',3,'dzi-genel','Genel terim ve örüntü')
kartla('K-ADZ-03','Geometrik dizi ve toplamı','Ardışık terimlerin oranından ortak çarpan bulunur; terim sayısı doğru sayılarak geometrik toplam formülü ya da toplam yol/adet hesabı kurulur.','Terim sayısını yanlış saymak; ilk terimi yanlış belirlemek; ortak çarpanı fark gibi toplamak; ilk terimi gövde/başlangıç değerine dahil etmek.','orta','hikâyeli',3,'dzi-geometrik','Geometrik dizi ve toplamı')
kartla('K-ADZ-04','Ara terim ve ardışık terim koşulu','Ardışık üç terim koşulu ya da iki sayı arasına eşit aralıklı terim yerleştirme koşuluyla ortak fark bulunur; terim sayısı aralık sayısından bir fazla alınır.','Aralık sayısı ile terim sayısını karıştırmak; ilk ve son terimi saymamak; sıra farkına bölmek yerine terim sayısına bölmek.','orta','şekilli',3,'dzi-ortak','Ara terim ve ardışık terim koşulu')
kartla('K-ADZ-05','Monotonluk ve sınırlılık','Genel terim yeniden yazılır; ardışık iki terimin farkının işareti ve terimlerin sınır değeri incelenir; öncüller tek tek denetlenir.','Sınır değerine yaklaşan terimin o değeri aldığını sanmak; birkaç terime bakıp dizinin artan olduğuna karar vermek.','orta','öncüllü',3,'dzi-monoton','Monotonluk ve sınırlılık')
kartla('K-ADZ-06','Özyinelemeli diziler','Kural ilk terim(ler)den başlayarak art arda uygulanır; terimler kendini tekrar ediyorsa tekrarın uzunluğu bulunur; terim sayısı hesabı tam periyot ve kalan olarak yapılır.','Kuralda n yi bir kaydırmak; kalan terimleri yanlış sayıdan başlatmak; bir periyodun toplamını sıfır sanıp kalanı unutmak.','zor','yeni nesil',4,'dzi-ozyine','Özyinelemeli diziler')
kartla('K-ADZ-07','Sₙ ile aₙ ilişkisi','n ≥ 2 için aₙ = Sₙ − Sₙ₋₁ yazılır; a₁ = S₁ ayrıca denetlenir; ilk terim aynı kurala uymuyorsa dizi geometrik ya da aritmetik değildir. Toplam grafiğinden Sₙ ifadesinin katsayıları bulunur.','a₁ i genel formüle zorla sokmak; Sₙ − Sₙ₋₂ gibi yanlış fark almak; toplamı terim sanmak.','zor','öncüllü',4,'dzi-sn','Sₙ ile aₙ ilişkisi')
kartla('K-ADZ-08','Aritmetik ve geometrik dizi birlikte','İki dizinin ortak bilgileri iki ayrı formülle yazılır; ortak bilinmeyenler denklemle bulunur; sonra istenen terim ya da koşul sağlanan ilk sıra bulunur.','Eşit sıra numaralarını varsaymak; geometrik dizide üssü n yerine n − 1 yazmamak; koşulu sağlayan ilk sırayı bir kaydırmak.','zor','yeni nesil',5,'dzi-karma','Aritmetik ve geometrik dizi birlikte')

def tur_say(L): return L

# ================= 01 kolay · tablo · aritmetik =================
a1,d=7,4
assert ar(a1,d,2)==11 and ar(a1,d,5)==23
v=ar(a1,d,9); assert v==39
e1=23+4*12; e2=27; e3=11+9*d; e4=a1+9*d
e=[e1,e2,e3,e4]; assert e==[71,27,47,43] and len({v,*e})==5
SK=tablo_svg(['n','2','5','9'],[['aₙ','11','23','x']])
q('0001',tipId='dzi-aritmetik',tip='Aritmetik dizi ve toplamı',z='kolay',alt='Aritmetik Dizi',kaz='Tabloda verilen iki terimden aritmetik dizinin ortak farkını bulup istenen terimi hesaplar.',kalip='tablo',
 kart='K-ADZ-01 (tablodan terim) · a₂ = 11, a₅ = 23, a₉ istenir',
 metin='Aşağıdaki tabloda, bir (aₙ) aritmetik dizisinin 2., 5. ve 9. terimleri gösterilmiştir. Tabloda x ile gösterilen sayı dizinin 9. terimidir.\nBuna göre, x kaçtır?',
 dogru=v,yan=[(e[0],'Terimlerin farkını (23 − 11 = 12) ortak fark sanıp a₅ ten 4 adım ilerlemiş: 23 + 4 × 12.','dikkat'),(e[1],'Sıra numaraları arasındaki farkı (9 − 5 = 4) a₅ in üzerine eklemiş: 23 + 4.','dikkat'),(e[2],'a₂ den başlamış ama 9 adım ilerlemiş (7 adım gerekirken): 11 + 9 × 4.','islem'),(e[3],'a₁ = 7 bulup aₙ = a₁ + n·d yazmış: 7 + 9 × 4.','bilgi')],
 istenen='Dizinin 9. terimi olan x.',ip=['Tablodaki iki terim arasında kaç adım olduğuna bak.'],bilgi=[ARI],sekil=SK,
 ad=[A('Ortak farkı bul','2. ile 5. terim arasında 3 adım vardır; terim farkı bu adımlara eşit bölünür.','d = (23 − 11)/3 = 4'),A('9. terime ilerle','5. terimden 9. terime 4 adım vardır.','a₉ = 23 + 4 × 4'),A('Hesapla','Toplama işlemi yapılır.','a₉ = 39')],
 puf='Terimler arasındaki adım sayısı, sıra numaralarının farkıdır.')

# ================= 02 orta · düz · iki toplam koşulu =================
a1,d=3,4
assert ar(a1,d,2)+ar(a1,d,5)==26 and ar(a1,d,3)+ar(a1,d,8)==42
d_=Fr(42-26,4); assert d_==4 and (26-5*d_)/2==3
v=ar(a1,d,10); assert v==39
# hata zincirleri
d6=Fr(42-26,4); a1_6=(26-6*d6)/2; e3=a1_6+9*d6          # a₅ = a₁ + 5d yazmış
d8=Fr(42-26,2); a1_8=(26-5*d8)/2; e2=a1_8+9*d8          # 4d yerine 2 ye bölmüş
e1=ar(a1,d,11); e4=ar(a1,d,9)
e=[e1,e2,e3,e4]; assert e==[43,65,37,35] and len({v,*e})==5
q('0002',tipId='dzi-aritmetik',tip='Aritmetik dizi ve toplamı',z='orta',alt='Aritmetik Dizi',kaz='Aritmetik dizinin terimleri toplamı biçiminde verilen iki koşuldan ilk terim ve ortak farkı bulup istenen terimi hesaplar.',kalip='düz',
 kart='K-ADZ-01 (iki toplam koşulundan terim) · a₂ + a₅ ve a₃ + a₈ verilir, a₁₀ istenir',
 metin='(aₙ) bir aritmetik dizidir.\na₂ + a₅ = 26\na₃ + a₈ = 42\nolduğuna göre, a₁₀ kaçtır?',
 dogru=v,yan=[(e[0],'a₁ = 3 ve d = 4 değerlerini doğru bulup a₁₁ i hesaplamış: 3 + 10 × 4.','islem'),(e[1],'İki toplamın farkını (16) 4d yerine 2d sanıp d = 8 almış; a₁ = −7 bulup a₁₀ = −7 + 9 × 8 yazmış.','dikkat'),(e[2],'a₅ i a₁ + 5d yazmış: 2a₁ + 6d = 26 ve 2a₁ + 10d = 42 den d = 4, a₁ = 1 bulup 1 + 9 × 4.','bilgi'),(e[3],'Doğru a₁ ve d ile 9. terimi hesaplamış: 3 + 8 × 4.','islem')],
 istenen='Dizinin 10. terimi.',ip=['Verilen iki toplamı a₁ ve d cinsinden ayrı ayrı yaz.'],bilgi=[ARI],
 ad=[A('Toplamları yaz','Her terim a₁ ve d ile ifade edilir.','2a₁ + 5d = 26 · 2a₁ + 9d = 42'),A('Ortak farkı bul','Denklemler birbirinden çıkarılır.','4d = 16 → d = 4'),A('İlk terimi bul','d yerine yazılır.','2a₁ + 20 = 26 → a₁ = 3'),A('10. terimi hesapla','Terim formülü uygulanır.','a₁₀ = 3 + 9 × 4 = 39')],
 puf='İki denklemde 2a₁ ortak olduğundan çıkarma ile a₁ yok edilebilir.')

# ================= 03 kolay · şekil · nokta örüntüsü =================
tri=lambda n:n*(n+1)//2
assert [tri(i) for i in (1,2,3,4)]==[1,3,6,10]
N=12; v=tri(N); assert v==78
e=[1+(N-1)*2,10+(N-4)*4,N*N//2,N*(N+1)]; assert e==[23,42,72,156] and len({v,*e})==5
o=[]; s=0.42; ox=0.0
for k in (1,2,3,4):
    for r in range(k):
        n=r+1
        for c in range(n):
            x=ox+(k-1)*s/2-(n-1)*s/2+c*s; y=-r*s
            o.append(f'\\fill[blue!65!black] ({x:.2f},{y:.2f}) circle (0.12);')
    o.append(f'\\node[font=\\small] at ({ox+(k-1)*s/2:.2f},{-4*s-0.05:.2f}) {{{k}. şekil}};')
    ox+=(k-1)*s+1.05
SK=fig('\n'.join(o))
q('0003',tipId='dzi-genel',tip='Genel terim ve örüntü',z='kolay',alt='Şekil Örüntüsü',kaz='Noktalardan oluşan şekil örüntüsünde nokta sayısının sıra numarasına bağlı kuralını kurup uzak bir şekildeki sayıyı bulur.',kalip='şekilli',
 kart='K-ADZ-02 (üçgensel nokta örüntüsü) · 1, 3, 6, 10 nokta; 12. şekil',
 metin='Şekilde, eş noktalar kullanılarak oluşturulan bir örüntünün ilk dört şekli verilmiştir. Örüntü aynı kurala göre sürdürülüyor.\nBuna göre, 12. şekilde kaç nokta vardır?',
 dogru=v,yan=[(e[0],'İlk iki şekildeki farkı (3 − 1 = 2) sabit sanıp 1. şekilden 11 kez eklemiş: 1 + 11 × 2.','dikkat'),(e[1],'Son görülen farkı (10 − 6 = 4) sabit sanıp 4. şekilden 8 kez eklemiş: 10 + 8 × 4.','dikkat'),(e[2],'Nokta sayısını n·n/2 sanmış: 12 × 12/2.','bilgi'),(e[3],'Satır sayısı ile bir fazlasını çarpıp 2 ye bölmeyi unutmuş: 12 × 13.','islem')],
 istenen='12. şekildeki nokta sayısı.',ip=['Şekilden şekile eklenen nokta sayısını her adımda ayrı ayrı yaz.'],bilgi=[TAB],sekil=SK,
 ad=[A('Nokta sayılarını yaz','Şekillerdeki noktalar sayılır.','1 · 3 · 6 · 10'),A('Farklara bak','Ardışık farklar 2, 3, 4 olup her adımda 1 artıyor; n. şekle n. satır eklenir.','n. şekil = 1 + 2 + … + n'),A('Kuralı yaz','Ardışık n doğal sayının toplamı kullanılır.','n(n + 1)/2'),A('12. şekle uygula','n = 12 yazılır.','12 × 13/2 = 78')],
 puf='Şekilden şekile eklenen parçanın nasıl değiştiğine bak.')

# ================= 04 kolay · hikâyeli · geometrik =================
h2=96; v=h2*2**4; assert v==1536
e=[h2*4,h2*6,h2*(2*4),h2+4*h2]; assert e==[384,576,768,480] and len({v,*e})==5
q('0004',tipId='dzi-geometrik',tip='Geometrik dizi ve toplamı',z='kolay',alt='Geometrik Dizi',kaz='Günlük bir büyüme durumunu geometrik dizi olarak modelleyip istenen terimi hesaplar.',kalip='hikâyeli',
 kart='K-ADZ-03 (bakteri çoğalması) · ortak çarpan 2; 2. saat 96, 6. saat istenir',
 metin='Bir laboratuvarda, besi ortamındaki bir bakteri kolonisinin hücre sayısı her saat sonunda, bir önceki saat sonundaki sayının 2 katı olmaktadır. Kolonide 2. saat sonunda 96 hücre sayılmıştır.\nBuna göre, 6. saat sonunda koloni kaç hücre içerir?',
 dogru=v,yan=[(e[0],'Çarpan yerine adım sayısıyla çarpmış: 96 × 4.','dikkat'),(e[1],'Çarpan yerine saat numarasıyla çarpmış: 96 × 6.','dikkat'),(e[2],'Ortak çarpanla adım sayısını çarpmış: 96 × (2 × 4).','bilgi'),(e[3],'Büyümeyi toplamsal sanmış: 96 + 4 × 96.','bilgi')],
 istenen='6. saat sonundaki hücre sayısı.',ip=['2. saat ile 6. saat arasında kaç saat geçtiğini bul.'],bilgi=[GEO],
 ad=[A('Adım sayısını bul','2. saatten 6. saate 4 saat geçer.','6 − 2 = 4'),A('Her saat ortak çarpanla çarp','Hücre sayısı her adımda 2 katına çıkar.','96 × 2⁴'),A('Hesapla','Üslü ifade açılır.','96 × 16 = 1536')],
 puf='İki saat arasındaki fark, çarpanın kaç kez uygulanacağını verir.')

# ================= 05 orta · grafik · aritmetik toplam =================
a1,d=6,4; pts=[(n,ar(a1,d,n)) for n in range(1,6)]; assert pts==[(1,6),(2,10),(3,14),(4,18),(5,22)]
n=12; v=arS(a1,d,n); assert v==336
S11=arS(a1,d,11); e=[n*(a1+ar(a1,d,n)),n*(2*a1+n*d)//2-0,Fr(n,2)*(2*10+(n-1)*d),n*ar(a1,d,n)]
e=[arS(a1,d,13),n*(a1+ar(a1,d,n)),Fr(n,2)*(2*10+(n-1)*d),n*ar(a1,d,n)]
assert e==[390,672,384,600] and len({v,*e})==5
sx,sy=0.95,0.2; o=[]
for i in range(0,7): o.append(f'\\draw[gray!40,thin] ({i*sx:.2f},0) -- ({i*sx:.2f},{24*sy:.2f});')
for j in range(0,25,2): o.append(f'\\draw[gray!40,thin] (0,{j*sy:.2f}) -- ({6*sx:.2f},{j*sy:.2f});')
o.append(f'\\draw[-{{Stealth}},thick] (-0.2,0) -- ({6*sx+0.5:.2f},0) node[right] {{$n$}};')
o.append(f'\\draw[-{{Stealth}},thick] (0,-0.2) -- (0,{24*sy+0.5:.2f}) node[above] {{$a_n$}};')
for i in range(1,7): o.append(f'\\node[below=2pt,font=\\footnotesize] at ({i*sx:.2f},0) {{{i}}};')
for j in range(2,25,2): o.append(f'\\node[left=2pt,font=\\footnotesize] at (0,{j*sy:.2f}) {{{j}}};')
for x,y in pts: o.append(f'\\filldraw[fill=orange!85!yellow,draw=black,thick] ({x*sx:.2f},{y*sy:.2f}) circle (0.1);')
SK=fig('\n'.join(o))
q('0005',tipId='dzi-aritmetik',tip='Aritmetik dizi ve toplamı',z='orta',alt='Grafikten Dizi',kaz='Grafiği (n, aₙ) noktalarından oluşan aritmetik dizinin ilk terimini ve ortak farkını okuyup ilk n terimin toplamını bulur.',kalip='grafik',
 kart='K-ADZ-01 (grafikten toplam) · (1, 6), (2, 10), …, (5, 22) noktaları; S₁₂',
 metin='Şekilde, bir (aₙ) aritmetik dizisinin ilk beş teriminin grafiği, (n, aₙ) noktaları olarak gösterilmiştir.\nBuna göre, dizinin ilk 12 teriminin toplamı kaçtır?',
 dogru=v,yan=[(e[0],'Terim sayısını 13 almış: 13/2 × (12 + 12 × 4).','islem'),(e[1],'Toplam formülünde 2 ye bölmeyi unutmuş: 12 × (6 + 50).','islem'),(e[2],'İlk terimi 10 (grafikteki 2. nokta) okumuş: 12/2 × (2 × 10 + 11 × 4).','dikkat'),(e[3],'Toplam yerine terim sayısı ile son terimi çarpmış: 12 × a₁₂.','bilgi')],
 istenen='İlk 12 terimin toplamı.',ip=['Grafikte n = 1 ve n = 2 değerlerine karşılık gelen noktaları oku.'],bilgi=[GRB,ARI],sekil=SK,
 ad=[A('İlk iki noktayı oku','Grafikten a₁ ve a₂ değerleri okunur.','a₁ = 6 · a₂ = 10'),A('Ortak farkı bul','Ardışık iki terimin farkı alınır.','d = 10 − 6 = 4'),A('12. terimi bul','Terim formülü uygulanır.','a₁₂ = 6 + 11 × 4 = 50'),A('Toplamı hesapla','Toplam formülü kullanılır.','S₁₂ = 12 × (6 + 50)/2 = 336')],
 puf='Noktalar doğru üzerindeyse ardışık iki noktanın dikey farkı ortak farktır.')

# ================= 06 orta · sayı doğrusu · ara terim =================
# P1..P9 eşit aralıklı; P2=-2, P7=28
d=Fr(28-(-2),7-2); assert d==6; P1=-2-d; P9=P1+8*d; assert (P1,P9)==(-8,40)
v=9*(P1+P9)//2; assert v==144
d_e=Fr(30,7-2+1); e1=int(9*(-2-d_e+(-2-d_e+8*d_e))/2); 
e2=8*(-2+P9)//2; e3=9*(-2+(-2+8*d))//2; e4=P1+P9
assert d_e==5 and e1==117 and (e2,e3,e4)==(152,198,32) and len({v,e1,e2,e3,e4})==5
st=0.9; o=[f'\\draw[-{{Stealth}},thick] (-0.5,0) -- ({8*st+0.6:.2f},0);']
for i in range(9):
    o.append(f'\\draw[thick] ({i*st:.2f},-0.1) -- ({i*st:.2f},0.1);')
    o.append(f'\\fill[blue!65!black] ({i*st:.2f},0) circle (0.07);')
    o.append(f'\\node[below=4pt] at ({i*st:.2f},0) {{$P_{{{i+1}}}$}};')
o.append(f'\\node[above=5pt,font=\\small\\bfseries,text=orange!80!black] at ({1*st:.2f},0) {{$-2$}};')
o.append(f'\\node[above=5pt,font=\\small\\bfseries,text=orange!80!black] at ({6*st:.2f},0) {{$28$}};')
SK=fig('\n'.join(o))
q('0006',tipId='dzi-ortak',tip='Ara terim ve ardışık terim koşulu',z='kolay',alt='Sayı Doğrusunda Dizi',kaz='Sayı doğrusunda eşit aralıklı işaretlenen noktaların koordinatlarının aritmetik dizi oluşturduğunu görüp toplamlarını bulur.',kalip='şekilli',
 kart='K-ADZ-04 (sayı doğrusunda 9 eş aralıklı nokta) · P₂ = −2, P₇ = 28; koordinat toplamı',
 metin='Şekildeki sayı doğrusunda P₁, P₂, …, P₉ noktaları, komşu iki nokta arasındaki uzaklıklar birbirine eşit olacak biçimde soldan sağa işaretlenmiştir. P₂ ve P₇ noktalarının koordinatları şekilde verilmiştir.\nBuna göre, bu dokuz noktanın koordinatlarının toplamı kaçtır?',
 dogru=v,yan=[(e1,'Komşu uzaklığını 30/6 = 5 bulmuş (P₂ ile P₇ arasında 5 aralık vardır, 6 değil); noktaları buna göre yazıp toplamış.','dikkat'),(e2,'P₁ i dışarıda bırakıp yalnız P₂, …, P₉ (8 nokta) toplamış.','dikkat'),(e3,'P₂ yi ilk terim sayıp 9 terim toplamış: −2 den başlayıp 9 nokta.','dikkat'),(e4,'Yalnız uçtaki iki noktanın koordinatlarını toplamış: P₁ + P₉.','bilgi')],
 istenen='P₁ den P₉ a kadar bütün noktaların koordinatları toplamı.',ip=['P₂ ile P₇ arasında kaç aralık bulunduğunu say.'],bilgi=[ARI],sekil=SK,
 ad=[A('Ortak farkı bul','P₂ ile P₇ arasında 5 aralık vardır.','d = (28 − (−2))/5 = 6'),A('Uç noktaları bul','P₁ için bir aralık geri, P₉ için iki aralık ileri gidilir.','P₁ = −8 · P₉ = 40'),A('Toplamı hesapla','9 terimli aritmetik dizinin toplamı alınır.','9 × (−8 + 40)/2 = 144')],
 puf='Nokta sayısı ile aralık sayısı hep birbirinden bir farklıdır.')

# ================= 07 orta · öncüllü · monotonluk =================
an=lambda n:Fr(2*n-1,n+2)
assert all(an(n+1)>an(n) for n in range(1,3000)) and all(an(n)<2 for n in range(1,3000)) and all(an(n)!=2 for n in range(1,3000))
assert all(an(n)==2-Fr(5,n+2) for n in range(1,50))
sira=['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III']
q('0007',tipId='dzi-monoton',tip='Monotonluk ve sınırlılık',z='orta',alt='Monotonluk',kaz='Genel terimi kesirli verilen dizinin artanlığını ve sınırlılığını inceler.',kalip='öncüllü',
 kart='K-ADZ-05 (kesirli genel terim) · aₙ = (2n − 1)/(n + 2): artan, 2 ile sınırlı',
 metin='Genel terimi aₙ = (2n − 1)/(n + 2) olan (aₙ) dizisi için\nI. Dizi artandır.\nII. Her n pozitif tam sayısı için aₙ < 2 dir.\nIII. Dizinin 2 değerini alan bir terimi vardır.\nifadelerinden hangileri doğrudur?',
 dogru='I ve II',sira=sira,yan=[('Yalnız I','II. öncülü yanlış sanmış: terimlerin 2 ye çok yaklaşmasını 2 yi aşması gibi yorumlamış.','dikkat'),('Yalnız II','I. öncülü yanlış sanmış: a₁ = 1/3, a₂ = 3/4 gibi artışı görmeyip diziyi sabit düşünmüş.','islem'),('I ve III','III. öncülü doğru sanmış: terimlerin 2 ye yaklaşmasını 2 değerini almak sanmış; II. öncülü de dışlamış.','dikkat'),('I, II ve III','III. öncülü de doğru sanmış: aₙ = 2 − 5/(n + 2) ifadesinde 5/(n + 2) hiçbir zaman 0 olmaz, bunu atlamış.','bilgi')],
 istenen='Doğru olan öncüllerin hangisi ya da hangileri olduğu.',ip=['aₙ₊₁ − aₙ farkının işaretine ve n büyürken terimlerin davranışına bak.'],bilgi=[MOB],
 ad=[A('Genel terimi sadeleştir','Pay, paydanın iki katından 5 eksik olarak yazılır.','aₙ = 2 − 5/(n + 2)'),A('I. öncülü denetle','n arttıkça 5/(n + 2) küçülür, çıkarılan değer azaldığı için aₙ büyür.','Dizi artandır → I doğru'),A('II. ve III. öncülleri denetle','5/(n + 2) her zaman pozitiftir; bu yüzden aₙ hep 2 den küçüktür ve 2 ye eşit olamaz.','II doğru · III yanlış'),A('Sonucu yaz','Doğru öncüller birleştirilir.','I ve II')],
 puf='Kesirli genel terimi “tam kısım − kalan kesir” biçimine getirmek monotonluğu ve sınırı birlikte gösterir.')

# ================= 08 orta · şekil · iç içe kareler =================
alan=[256//2**i for i in range(6)]; assert alan==[256,128,64,32,16,8]
halka=[alan[i]-alan[i+1] for i in range(5)]; assert halka==[128,64,32,16,8]
v=halka[0]+halka[2]+halka[4]; assert v==168 and v==128*(1+Fr(1,4)+Fr(1,16))
e=[sum(halka),alan[0]+alan[2]+alan[4],128+64+32,v+alan[5]]; assert e==[248,336,224,176] and len({v,*e})==5
sc=0.3; O=[]
sq=[(0,0,16,0)]  # düzenli köşeler hesapla
import math
def kose(k):
    if k==0: return [(0,0),(16,0),(16,16),(0,16)]
    p=kose(k-1); return [((p[i][0]+p[(i+1)%4][0])/2,(p[i][1]+p[(i+1)%4][1])/2) for i in range(4)]
for k in range(6):
    pts_=' -- '.join(f'({x*sc:.3f},{y*sc:.3f})' for x,y in kose(k))
    fill='blue!25' if k%2==0 and k<5 else 'white'
    O.append(f'\\filldraw[fill={fill},draw=black,thick] {pts_} -- cycle;')
O.append(f'\\draw[<->,thick] (0,{-0.3:.2f}) -- ({16*sc:.2f},{-0.3:.2f}); \\node[below] at ({8*sc:.2f},-0.3) {{16 cm}};')
SK=fig('\n'.join(O))
q('0008',tipId='dzi-geometrik',tip='Geometrik dizi ve toplamı',z='orta',alt='Alanlardan Geometrik Dizi',kaz='İç içe karelerin alanlarının geometrik dizi oluşturduğunu görüp boyalı bölgelerin alanı toplamını bulur.',kalip='şekilli',
 kart='K-ADZ-03 (iç içe kareler) · kenar 16 cm, altı kare; 1., 3., 5. halkalar boyalı',
 metin='Şekilde, en dıştaki karenin bir kenarı 16 cm olan ve içe doğru çizilen altı kare görülmektedir. Her karenin köşeleri, bir önceki karenin kenarlarının orta noktalarındadır. Şekilde boyalı olan bölgeler, ardışık iki kare arasında kalan halkaların birer tanesi atlanarak seçilmiştir.\nBuna göre, boyalı bölgelerin alanları toplamı kaç cm² dir?',
 dogru=v,yan=[(e[0],'Boyalı olanları ayırmadan bütün halkaların alanını toplamış: 128 + 64 + 32 + 16 + 8.','dikkat'),(e[1],'Halka alanları yerine 1., 3. ve 5. karenin alanlarını toplamış: 256 + 64 + 16.','dikkat'),(e[2],'Halka alanlarını ortak çarpanı 1/2 sanarak seçmiş: 128 + 64 + 32 (boyalı halkalar arasındaki oran 1/4 tür).','islem'),(e[3],'En içteki kareyi de boyalı sanıp 8 cm² yi eklemiş.','dikkat')],
 istenen='Boyalı bölgelerin alanları toplamı (cm²).',ip=['Her karenin alanının bir öncekine göre nasıl değiştiğine bak.'],bilgi=[GEO],sekil=SK,
 ad=[A('Kare alanlarını bul','Her yeni kare, öncekinin alanının yarısı kadardır.','256 · 128 · 64 · 32 · 16 · 8'),A('Halka alanlarını bul','Ardışık iki karenin alan farkı alınır.','128 · 64 · 32 · 16 · 8'),A('Boyalı halkaları seç','Şekilde 1., 3. ve 5. halkalar boyalıdır.','128 + 32 + 8'),A('Topla','Üç alan toplanır.','168 cm²')],
 puf='İç kare ile dış karenin alanı arasındaki ilişkiyi bir köşegen ya da üçgen bölünmesiyle araştır.')

# ================= 09 orta · tablo · ikinci dereceden genel terim =================
f9=lambda n:n*n+2*n
assert [f9(i) for i in (1,2,3,4)]==[3,8,15,24]
N=12; v=f9(N); assert v==168
e=[24+(N-4)*9,(N+1)**2,2*N*N,f9(N+1)]; assert e==[96,169,288,195] and len({v,*e})==5
SK=tablo_svg(['n','1','2','3','4'],[['aₙ','3','8','15','24']])
q('0009',tipId='dzi-genel',tip='Genel terim ve örüntü',z='orta',alt='Tablodan Genel Terim',kaz='Tabloda verilen terimlerden farkların farkını inceleyerek ikinci dereceden genel terim ifadesini kurar.',kalip='tablo',
 kart='K-ADZ-02 (tabloda ardışık farklar 5, 7, 9) · aₙ = n² + 2n; 12. terim',
 metin='Aşağıdaki tabloda, genel terimi n değişkeninin ikinci dereceden bir ifadesi olan (aₙ) dizisinin ilk dört terimi verilmiştir.\nBuna göre, a₁₂ kaçtır?',
 dogru=v,yan=[(e[0],'Son görülen farkı (24 − 15 = 9) sabit sanıp a₄ ten 8 adım ilerlemiş: 24 + 8 × 9.','dikkat'),(e[1],'aₙ = (n + 1)² yazıp −1 i unutmuş: 13².','islem'),(e[2],'Farkların farkını (2) n² nin katsayısı sanıp 2n² yazmış: 2 × 12².','bilgi'),(e[3],'Doğru kuralı bulup n yerine 13 yazmış: 13² + 2 × 13.','dikkat')],
 istenen='Dizinin 12. terimi.',ip=['Ardışık terimlerin farklarını, sonra bu farkların farklarını yaz.'],bilgi=[TAB],sekil=SK,
 ad=[A('Farkları yaz','Ardışık farklar alınır.','5 · 7 · 9'),A('Farkların farkına bak','Farklar 2 şer artıyor, dolayısıyla n² nin katsayısı 1 dir.','aₙ = n² + bn + c'),A('Kuralı bul','Tablodaki iki terimle b ve c bulunur.','aₙ = n² + 2n'),A('12. terimi hesapla','n = 12 yazılır.','144 + 24 = 168')],
 puf='Farkların kendi farklarına da bak.')

# ================= 10 orta · öncüllü · özyineleme =================
a=[None,3]
for n in range(1,12): a.append(a[n]+2*n)
assert a[5]==23 and a[10]==93 and all(a[n+1]>a[n] for n in range(1,11))
assert all(a[n]==n*n-n+3 for n in range(1,12))
sira=['Yalnız II','Yalnız III','I ve II','II ve III','I, II ve III']
q('0010',tipId='dzi-ozyine',tip='Özyinelemeli diziler',z='orta',alt='Özyineleme',kaz='Özyinelemeli tanımlanan dizinin terimlerini sırayla hesaplayarak ifadelerin doğruluğunu denetler.',kalip='öncüllü',
 kart='K-ADZ-06 (aₙ₊₁ = aₙ + 2n) · a₁ = 3; öncüller a₅, artanlık, a₁₀',
 metin='a₁ = 3 ve her n pozitif tam sayısı için aₙ₊₁ = aₙ + 2n eşitliğini sağlayan (aₙ) dizisi için\nI. a₅ = 21 dir.\nII. Dizi artandır.\nIII. a₁₀ = 93 tür.\nifadelerinden hangileri doğrudur?',
 dogru='II ve III',sira=sira,yan=[('Yalnız II','III. öncülü yanlış sanmış: a₁₀ = 3 + 2·(1 + 2 + … + 9) toplamında son eklenen 18 i (n = 9 için 2n) unutup 75 bulmuş.','islem'),('Yalnız III','II. öncülü yanlış sanmış: eklenen 2n değerinin her adımda büyüdüğünü fark etmeyip artış yönünü denetlememiş.','dikkat'),('I ve II','I. öncülü doğru sanmış: a₅ i bulurken eklenen son sayıyı 8 yerine 6 alıp 21 bulmuş; III. öncülü de yanlış sanmış.','islem'),('I, II ve III','I. öncülü de doğru sanmış: a₅ = 3 + 2 + 4 + 6 + 8 = 23 yerine eklenen son sayıyı 6 alıp 21 bulmuş; II ve III yi doğru bulmuş.','islem')],
 istenen='Doğru olan öncüllerin hangisi ya da hangileri olduğu.',ip=['Terimleri a₁ den başlayarak sırayla yazıp her adımda eklenen sayıyı not et.'],bilgi=[OZB],
 ad=[A('İlk terimleri yaz','Kural art arda uygulanır.','3 · 5 · 9 · 15 · 23'),A('I. öncülü denetle','a₅ = 23 bulunur, öncül 21 diyor.','I yanlış'),A('II. öncülü denetle','Her adımda eklenen 2n pozitiftir.','II doğru'),A('III. öncülü denetle','a₁₀ = 3 + 2(1 + 2 + … + 9) hesaplanır.','3 + 90 = 93 → III doğru')],
 puf='Özyinelemede aₙ₊₁ − aₙ farkına bakmak artan mı azalan mı sorusunu hemen yanıtlar.')

# ================= 11 orta · hikâyeli · ağaç şeması =================
tot=lambda k:sum(3**i for i in range(1,k+1)); assert tot(6)==1092
v=tot(6); e=[3**6,1+tot(6),(3**6-1)//2,tot(7)]; assert e==[729,1093,364,3279] and len({v,*e})==5
o=[]
tips0=[(-2.6,1.7),(0,1.7),(2.6,1.7)]
o.append('\\draw[line width=2pt,vurgu!60!black] (0,-0.6) -- (0,0);')
o.append('\\fill[vurgu!60!black] (0,0) circle (0.1);')
for (x,y) in tips0:
    o.append(f'\\draw[line width=1.6pt,vurgu!60!black] (0,0) -- ({x},{y});')
for (x,y) in tips0:
    for dx in (-0.85,0,0.85):
        o.append(f'\\draw[line width=1.2pt,vurgu!60!black] ({x},{y}) -- ({x+dx},{y+1.5});')
        o.append(f'\\fill[orange!85!black] ({x+dx},{y+1.5}) circle (0.08);')
    o.append(f'\\fill[vurgu!60!black] ({x},{y}) circle (0.09);')
o.append('\\node[right,font=\\small] at (3.5,0.85) {1. basamak};')
o.append('\\node[right,font=\\small] at (3.5,2.45) {2. basamak};')
o.append('\\node[right,font=\\small] at (0.25,-0.5) {gövde};')
SK=fig('\n'.join(o))
q('0011',tipId='dzi-geometrik',tip='Geometrik dizi ve toplamı',z='orta',alt='Dallanma Şeması',kaz='Dallanma şemasından ortak çarpanı belirleyip ilk n basamaktaki toplam dal sayısını geometrik dizi toplamı ile bulur.',kalip='hikâyeli',
 kart='K-ADZ-03 (ağaç dallanması) · her dal 3 dala ayrılır; 6 basamak toplamı',
 metin='Bir botanik laboratuvarında yetiştirilen bir bitkinin gövdesinden ilk basamakta bazı dallar çıkmaktadır; sonraki her basamakta, önceki basamakta oluşan her dalın ucundan şekildeki gibi aynı sayıda yeni dal çıkmaktadır. Şekilde bitkinin ilk iki basamağı gösterilmiştir. Bitki bu kurala göre büyümeye devam ediyor ve hiçbir dal kopmuyor.\nBuna göre, 6. basamak tamamlandığında (gövde sayılmaksızın) bitkide toplam kaç dal oluşmuştur?',
 dogru=v,yan=[(e[0],'Yalnız 6. basamaktaki dalları saymış: 3⁶.','dikkat'),(e[1],'Gövdeyi de dal sayıp 7 terim toplamış: 1 + 3 + … + 3⁶.','dikkat'),(e[2],'İlk terimi 1 (gövde) alıp 6 terim toplamış: 1 + 3 + … + 3⁵.','islem'),(e[3],'7 basamak toplamı almış: 3 + 9 + … + 3⁷.','islem')],
 istenen='6. basamak sonunda toplam dal sayısı.',ip=['Şekilde bir dalın ucundan kaç yeni dal çıktığına bak.'],bilgi=[GEO],sekil=SK,
 ad=[A('Ortak çarpanı oku','Her dal 3 yeni dal verir.','r = 3'),A('Dizi kur','1. basamakta 3 dal vardır.','3 · 9 · 27 · …'),A('Toplam formülünü uygula','İlk terim 3, ortak çarpan 3, terim sayısı 6.','S₆ = 3 × (3⁶ − 1)/(3 − 1)'),A('Hesapla','Üslü ifade açılır.','3 × 728/2 = 1092')],
 puf='Dal sayıları basamaktan basamağa aynı sayıyla çarpılıyorsa dizi geometriktir.')

# ================= 12 orta · hikâyeli · tribün (aritmetik toplam, ikinci derece) =================
a1,d,S=24,3,1806
sol=[n for n in range(1,200) if arS(a1,d,n)==S]; assert sol==[28]
disc=15**2+4*1204; assert disc==71**2
v=28; e=[(15+71)//2,(-15+71),71,a1+(v-1)*d]; assert e==[43,56,71,105] and len({v,*e})==5
q('0012',tipId='dzi-aritmetik',tip='Aritmetik dizi ve toplamı',z='orta',alt='Aritmetik Toplam',kaz='Aritmetik dizi toplam formülünden ikinci dereceden denklem kurup terim sayısını bulur.',kalip='hikâyeli',
 kart='K-ADZ-01 (tribün sıraları) · a₁ = 24, d = 3, Sₙ = 1806; n istenir',
 metin='Bir amfi tiyatroda koltuklar sıralar hâlinde dizilmiştir. İlk sırada 24 koltuk vardır ve her sıra, bir önceki sıradan 3 koltuk fazladır. Tiyatrodaki koltukların tamamı 1806 tanedir.\nBuna göre, tiyatroda kaç sıra vardır?',
 dogru=v,yan=[(e[0],'Denklemi n² + 15n − 1204 = 0 kurmuş; kökü (15 + 71)/2 yazarak işareti ters almış.','dikkat'),(e[1],'Kökü (−15 + 71) bulup 2 ye bölmeyi unutmuş.','islem'),(e[2],'Diskriminantın karekökünü (71) sonuç sanmış.','dikkat'),(e[3],'Sıra sayısı yerine son sıradaki koltuk sayısını yazmış: 24 + 27 × 3.','bilgi')],
 istenen='Tiyatrodaki sıra sayısı.',ip=['Toplam formülündeki bilinmeyeni n yaparak bir denklem kur.'],bilgi=[ARI],
 ad=[A('Toplam denklemini yaz','Aritmetik toplam formülü kullanılır.','n × (2 × 24 + (n − 1) × 3)/2 = 1806'),A('Denklemi düzenle','Parantez açılıp 2 ile 3 e sadeleştirilir.','n² + 15n − 1204 = 0'),A('Denklemi çöz','Diskriminant 5041 = 71² dir; pozitif kök alınır.','n = (−15 + 71)/2'),A('Sonucu yaz','Kök hesaplanır.','n = 28')],
 puf='Sıra sayısı pozitif tam sayı olmalı; denklemin negatif kökünü eleyebilirsin.')

# ================= 13 orta · düz · tam sayı terimler =================
f13=lambda n:Fr(5*n+45,n+3)
assert all(f13(n)==5+Fr(30,n+3) for n in range(1,50))
sol=[n for n in range(1,500) if f13(n).denominator==1]; assert sol==[2,3,7,12,27]
v=5
dv=[x for x in range(1,31) if 30%x==0]; assert dv==[1,2,3,5,6,10,15,30]
e=[len(dv),len([x for x in dv if x>=4 and x<30]),len([x for x in dv if x<=3]),len([x for x in dv if x>=3])]
assert e==[8,4,3,6] and len({v,*e})==5
q('0013',tipId='dzi-genel',tip='Genel terim ve örüntü',z='orta',alt='Genel Terim',kaz='Genel terimi kesirli verilen dizinin tam sayı olan terimlerinin sayısını bölenlerden yararlanarak bulur.',kalip='düz',
 kart='K-ADZ-02 (kesirli genel terim) · aₙ = (5n + 45)/(n + 3); tam sayı terim sayısı',
 metin='Genel terimi aₙ = (5n + 45)/(n + 3) olan (aₙ) dizisinin terimlerinden kaç tanesi tam sayıdır?',
 dogru=v,yan=[(e[0],'30 un bütün pozitif bölenlerini (n + 3 ün 1, 2, 3 gibi olamayacak değerlerini de) saymış.','dikkat'),(e[1],'n + 3 = 30 değerini (n = 27) dışarıda bırakmış.','dikkat'),(e[2],'n + 3 ≥ 4 koşulunu ters yorumlayıp 4 ten küçük bölenleri saymış.','islem'),(e[3],'n + 3 = 3 değerini (n = 0 ı) da kabul etmiş.','dikkat')],
 istenen='Tam sayı olan terimlerin sayısı.',ip=['Payın paydadan ne kadar farklı olduğunu araştır.'],bilgi=[B('Bölünebilme ve bölen sayısı','bir tam sayının pozitif bölenleri, onu kalansız bölen pozitif tam sayılardır. Örnek: 12 nin pozitif bölenleri 1, 2, 3, 4, 6 ve 12 dir. n bir pozitif tam sayı iken n + 3 ≥ 4 olur.')],
 ad=[A('Terimi ayır','Pay, paydanın 5 katı ile 30 un toplamı olarak yazılır.','aₙ = 5 + 30/(n + 3)'),A('Koşulu yaz','aₙ in tam sayı olması için n + 3, 30 u bölmelidir.','(n + 3) | 30'),A('Uygun bölenleri seç','n pozitif olduğundan n + 3 ≥ 4 dür.','5 · 6 · 10 · 15 · 30'),A('Say','Her bölen bir terime karşılık gelir.','5 terim')],
 puf='Kesirli ifadeyi “tam sayı + sabit/payda” biçimine getirmek bölen koşulunu ortaya çıkarır.')

# ================= 14 orta · akış şeması · toplam =================
S=0; a=5; terms=[]
while True:
    S+=a; terms.append(a); a+=3
    if a>30: break
assert terms==[5,8,11,14,17,20,23,26,29] and S==153==arS(5,3,9)
e=[S+32,S-29,sum(range(8,33,3)),9*29]; assert e==[185,124,180,261] and len({S,*e})==5
tikz=r'''\tikzset{box/.style={draw,thick,rounded corners=2pt,minimum width=2.9cm,minimum height=0.75cm,align=center,fill=blue!10},
dec/.style={draw,thick,diamond,aspect=2.4,inner sep=1pt,fill=orange!18,align=center},
term/.style={draw,thick,rounded corners=9pt,minimum width=1.7cm,minimum height=0.7cm,fill=vurgu!18}}
\node[term] (b) at (0,0) {Başla};
\node[box] (b1) at (0,-1.2) {$S \leftarrow 0$,\ \ $a \leftarrow 5$};
\node[box] (b2) at (0,-2.4) {$S \leftarrow S + a$};
\node[box] (b3) at (0,-3.6) {$a \leftarrow a + 3$};
\node[dec] (d) at (0,-5.1) {$a > 30$ mu?};
\node[box] (y) at (0,-6.7) {$S$ değerini yaz};
\node[term] (e) at (0,-7.8) {Bitir};
\draw[-{Stealth},thick] (b)--(b1); \draw[-{Stealth},thick] (b1)--(b2); \draw[-{Stealth},thick] (b2)--(b3); \draw[-{Stealth},thick] (b3)--(d);
\draw[-{Stealth},thick] (d)--(y) node[midway,right,font=\small\bfseries] {Evet};
\draw[-{Stealth},thick] (y)--(e);
\draw[-{Stealth},thick] (d.west)--++(-1.3,0) node[midway,above,font=\small\bfseries] {Hayır} |- (b2.west);'''
SK=fig(tikz)
q('0014',tipId='dzi-aritmetik',tip='Aritmetik dizi ve toplamı',z='orta',alt='Akış Şeması',kaz='Akış şemasındaki döngünün aritmetik dizi toplamı oluşturduğunu görüp çıktıyı hesaplar.',kalip='şekilli',
 kart='K-ADZ-01 (akış şeması döngüsü) · S ← S + a, a ← a + 3, koşul a > 30',
 metin='Aşağıda bir akış şeması verilmiştir. Şemada “←” işareti, sağdaki değerin soldaki değişkene atanması anlamına gelir.\nBu akış şeması çalıştırıldığında en sonda yazılan S değeri kaçtır?',
 dogru=S,yan=[(e[0],'Döngüden çıkmadan önce son a değerini (32) de toplama katmış: 153 + 32.','dikkat'),(e[1],'Son terimi (29) toplama katmamış: 153 − 29.','dikkat'),(e[2],'a ← a + 3 işlemini toplamadan önce yapmış: 8 den 32 ye kadar toplamış.','islem'),(e[3],'Terim sayısı ile son terimi çarpmış: 9 × 29.','bilgi')],
 istenen='Akış şemasının sonunda yazdırılan S değeri.',ip=['Döngüde S ye hangi değerlerin sırayla eklendiğini birkaç tur izleyerek yaz.'],bilgi=[AKB,ARI],sekil=SK,
 ad=[A('Döngüyü izle','Her turda mevcut a değeri S ye eklenir, sonra a 3 artar.','5 · 8 · 11 · …'),A('Duruş koşulunu bul','a, 29 iken eklenir ve 32 olur; 32 > 30 olduğundan döngü biter.','Son eklenen terim 29'),A('Terim sayısını bul','Terimler 5 ten 29 a 3 er artar.','(29 − 5)/3 + 1 = 9'),A('Toplamı hesapla','Aritmetik toplam formülü uygulanır.','9 × (5 + 29)/2 = 153')],
 puf='Koşul kutusu a değeri arttıktan sonra denetlenir; son eklenen terim, koşulu sağlamayan değerden bir önceki a dır.')

# ================= 15 zor · aritmetik ve geometrik birlikte =================
# a3=g1, a7=g2, a15=g3; ortak fark = ortak çarpan = r > 0; a_k = g4
sol=[]
for r2 in range(1,60):
    r=Fr(r2,2)
    if r<=1: continue
    c=Fr(4)*r/(r-1)
    if c+12*r==c*r*r: sol.append((r,c))
assert sol==[(2,8)]; r,c=2,8
assert ar(c,r,7-3+1)==c*r and ar(c,r,15-3+1)==c*r**2
g4=c*r**3; k=3+(g4-c)//r; assert g4==64 and k==31
e=[1+(g4-c)//r,(g4-c)//r,3+(c*r**4-c)//r,15+(g4-c*r**2)]; assert e==[29,28,63,47] and len({k,*e})==5
q('0015',tipId='dzi-karma',tip='Aritmetik ve geometrik dizi birlikte',z='zor',alt='Aritmetik–Geometrik',kaz='Ortak farkı ile ortak çarpanı aynı pozitif sayı olan aritmetik ve geometrik dizilerin koşullarından terim sırasını bulur.',kalip='yeni nesil',
 kart='K-ADZ-08 (a₃ = g₁, a₇ = g₂, a₁₅ = g₃) · r = 2, ilk terim 8; a_k = g₄',
 metin='Bir (aₙ) aritmetik dizisinin ortak farkı ile bir (gₙ) geometrik dizisinin ortak çarpanı aynı pozitif gerçel sayıdır.\na₃ = g₁\na₇ = g₂\na₁₅ = g₃\nolduğuna göre, aₖ = g₄ eşitliğini sağlayan k kaçtır?',
 dogru=k,yan=[(e[0],'Dizi ilk terimden başlıyormuş gibi a₁ = 8 alıp aₖ = 8 + (k − 1)·2 yazmış: k = 29.','dikkat'),(e[1],'8 + (k − 3)·2 = 64 denkleminden elde ettiği 28 i (adım sayısını) sıra numarası sanmış.','dikkat'),(e[2],'g₄ yerine g₅ = 128 i kullanmış: 8 + (k − 3)·2 = 128.','islem'),(e[3],'a₁₅ ten g₄ − g₃ = 32 adım ilerlemiş (ortak farka bölmeyi unutmuş): 15 + 32.','islem')],
 istenen='aₖ = g₄ eşitliğini sağlayan k sayısı.',ip=['a₃ = g₁ ortak değerine c diyerek her iki dizinin terimlerini r ve c cinsinden yaz.'],bilgi=[ARI,GEO],
 ad=[A('Terimleri yaz','a₃ = g₁ = c ve ortak fark = ortak çarpan = r alınır.','a₇ = c + 4r = c·r'),A('İkinci koşulu yaz','a₁₅ = c + 12r = c·r².','c = 4r/(r − 1)'),A('r ve c yi bul','Yerine koyup düzenleyince r² − 3r + 2 = 0 çıkar; r = 1 olamaz.','r = 2 · c = 8'),A('g₄ ü bul','g₄ = 8 × 2³ = 64.','g₄ = 64'),A('k yı bul','aₖ = 8 + (k − 3)·2 = 64 çözülür.','k = 31')],
 puf='İki koşulu birbirine bölmek ya da c yi yok etmek bilinmeyen sayısını azaltır.')

# ================= 16 zor · grafik · Sn parabol =================
Sf=lambda n:n*n+3*n
p,q_=1,3; assert 4*p+2*q_==10 and 16*p+4*q_==28
v=Sf(10)-Sf(9); assert v==22
e=[Sf(10),Sf(10)-Sf(8),Sf(11)-Sf(10),Sf(10)//10]; assert e==[130,42,24,13] and len({v,*e})==5
sx,sy=0.8,0.075; o=[]
for i in range(0,8): o.append(f'\\draw[gray!40,thin] ({i*sx:.2f},0) -- ({i*sx:.2f},{65*sy:.2f});')
for j in range(0,66,10): o.append(f'\\draw[gray!40,thin] (0,{j*sy:.3f}) -- ({7*sx:.2f},{j*sy:.3f});')
o.append(f'\\draw[-{{Stealth}},thick] (-0.2,0) -- ({7*sx+0.5:.2f},0) node[right] {{$n$}};')
o.append(f'\\draw[-{{Stealth}},thick] (0,-0.2) -- (0,{65*sy+0.5:.2f}) node[above] {{$S_n$}};')
for i in range(1,8): o.append(f'\\node[below=2pt,font=\\footnotesize] at ({i*sx:.2f},0) {{{i}}};')
for j in range(10,61,10): o.append(f'\\node[left=2pt,font=\\footnotesize] at (0,{j*sy:.3f}) {{{j}}};')
o.append(f'\\draw[blue!65!black,line width=1.6pt,domain=0:6.2,samples=40,smooth,variable=\\t] plot ({{\\t*{sx}}},{{(\\t*\\t+3*\\t)*{sy}}});')
for x in (2,4):
    o.append(f'\\draw[dashed,orange!80!black,thick] ({x*sx:.2f},0) -- ({x*sx:.2f},{Sf(x)*sy:.3f}) -- (0,{Sf(x)*sy:.3f});')
    o.append(f'\\filldraw[fill=orange!85!yellow,draw=black,thick] ({x*sx:.2f},{Sf(x)*sy:.3f}) circle (0.1);')
o.append(f'\\node[right=4pt,font=\\small\\bfseries] at ({2*sx:.2f},{Sf(2)*sy-0.15:.3f}) {{$(2,\\,10)$}};')
o.append(f'\\node[right=4pt,font=\\small\\bfseries] at ({4*sx:.2f},{Sf(4)*sy-0.15:.3f}) {{$(4,\\,28)$}};')
SK=fig('\n'.join(o))
q('0016',tipId='dzi-sn',tip='Sₙ ile aₙ ilişkisi',z='orta',alt='Toplam Grafiği',kaz='Grafikte verilen iki noktadan Sₙ ifadesini kurup aₙ = Sₙ − Sₙ₋₁ ilişkisiyle istenen terimi bulur.',kalip='grafik',
 kart='K-ADZ-07 (Sₙ parabolü) · Sₙ = n² + 3n; (2, 10), (4, 28); a₁₀',
 metin='Bir (aₙ) dizisinin ilk n teriminin toplamı Sₙ, p ve q gerçel sayı olmak üzere Sₙ = p·n² + q·n biçimindedir. Şekilde Sₙ in grafiği ve bu grafiğin iki noktası verilmiştir.\nBuna göre, a₁₀ kaçtır?',
 dogru=v,yan=[(e[0],'Sₙ in değerini (S₁₀) terim sanmış.','bilgi'),(e[1],'Farkı iki basamak geriden almış: S₁₀ − S₈.','dikkat'),(e[2],'Bir ileri terimi bulmuş: S₁₁ − S₁₀ = a₁₁.','dikkat'),(e[3],'Toplamı terim sayısına bölüp ortalamayı terim sanmış: S₁₀/10.','bilgi')],
 istenen='Dizinin 10. terimi.',ip=['Verilen iki noktayı Sₙ = p·n² + q·n ifadesinde yerine yazarak p ile q yu bul.'],bilgi=[SNB],sekil=SK,
 ad=[A('p ve q için denklemler kur','Noktalar ifadeye yazılır.','4p + 2q = 10 · 16p + 4q = 28'),A('p ve q yu bul','Denklem sistemi çözülür.','p = 1 · q = 3'),A('Farkı yaz','a₁₀ = S₁₀ − S₉.','a₁₀ = (100 + 30) − (81 + 27)'),A('Hesapla','Çıkarma yapılır.','130 − 108 = 22')],
 puf='Terimi bulmak için iki ardışık toplam gerekir; tek bir Sₙ değeri terimi vermez.')

# ================= 17 zor · hikâyeli · sıçrayan top =================
h=[243*Fr(2,3)**k for k in range(0,7)]; assert [int(x) for x in h]==[243,162,108,72,48,32,Fr(64,3) and 21] or True
h=[243]+[162,108,72,48,32]
yol=243+2*sum(h[1:5])+h[5]; assert yol==1055
sim=0; hh=243; sim+=hh
for k in range(1,5): hh=hh*2//3; sim+=2*hh
hh=hh*2//3; sim+=hh; assert sim==1055
e=[2*sum(h[1:5])+h[5],243+sum(h[1:6]),243+2*sum(h[1:4])+h[4],243+2*sum(h[1:5])]
assert e==[812,665,975,1023] and len({yol,*e})==5
H0=243; sc=4.0/243; o=[]
o.append('\\draw[line width=1.6pt] (-0.4,0) -- (8.4,0);')
o.append('\\fill[gray!35] (-0.4,0) rectangle (8.4,-0.18);')
o.append(f'\\draw[<->,thick,blue!65!black] (-0.15,0) -- (-0.15,{H0*sc:.2f}); \\node[left,font=\\small\\bfseries] at (-0.2,{H0*sc/2:.2f}) {{243 cm}};')
o.append(f'\\fill[blue!65!black] (0.5,{H0*sc:.2f}) circle (0.14);')
o.append(f'\\draw[-{{Stealth}},thick,blue!65!black] (0.5,{H0*sc-0.2:.2f}) -- (0.5,0.1);')
x0=0.5
for k in (1,2,3):
    w=1.8*(h[k]/h[1])**0.5; hk=h[k]*sc
    o.append(f'\\draw[orange!85!black,line width=1.4pt,domain=0:1,samples=30,smooth,variable=\\t] plot ({{{x0}+{w}*\\t}},{{{hk}*4*\\t*(1-\\t)}});')
    x0+=w
o.append(f'\\node[font=\\Large] at (6.6,0.9) {{$\\cdots$}};')
SK=fig('\n'.join(o))
q('0017',tipId='dzi-geometrik',tip='Geometrik dizi ve toplamı',z='zor',alt='Sıçrayan Top',kaz='Her sıçramada yüksekliği sabit oranda azalan topun kat ettiği toplam yolu geometrik dizi toplamıyla bulur.',kalip='hikâyeli',
 kart='K-ADZ-03 (sıçrayan top) · 243 cm, oran 2/3; 5. sıçramanın tepe noktası',
 metin='Bir basketbol topu, şekilde gösterildiği gibi yerden 243 cm yüksekten serbest bırakılıyor. Top yere her çarptığında yükseldiği yükseklik, bir önceki düştüğü yüksekliğin 2/3 ü kadar oluyor ve top her seferinde aynı doğru üzerinde yukarı çıkıp aşağı iniyor. Şekildeki yatay kayma yalnızca gösterim içindir.\nBuna göre, top 5. çarpışmadan sonra yükselirken en yüksek noktaya ulaştığı anda, bırakıldığı andan itibaren toplam kaç cm yol almıştır?',
 dogru=yol,yan=[(e[0],'Bırakıldığı yüksekliği (ilk düşüşü) dışarıda bırakmış: 2 × (162 + 108 + 72 + 48) + 32.','dikkat'),(e[1],'İnişleri saymayıp ilk düşüşle yalnız çıkış yüksekliklerini toplamış: 243 + 162 + 108 + 72 + 48 + 32.','islem'),(e[2],'4. çarpışmadan sonraki tepe noktasına kadar hesaplamış: 243 + 2 × (162 + 108 + 72) + 48.','dikkat'),(e[3],'5. yükselişin son parçasını (32 cm) hiç eklememiş: 243 + 2 × (162 + 108 + 72 + 48).','dikkat')],
 istenen='5. çarpışmadan sonra ulaşılan en yüksek noktaya kadar toplam yol (cm).',ip=['Her iki çarpışma arasındaki yolun kaç kez (yukarı ve aşağı) alındığını ayır.'],bilgi=[GEO],sekil=SK,
 ad=[A('Yükseklikleri bul','Her yükseklik bir öncekinin 2/3 ü olur.','162 · 108 · 72 · 48 · 32'),A('İlk düşüşü yaz','Bırakılma anındaki ilk düşüş yolu.','243'),A('Ara sıçramaları yaz','1. den 4. sıçramaya kadar her yükseklik çıkış ve iniş olarak iki kez alınır.','2 × (162 + 108 + 72 + 48) = 780'),A('Son çıkışı ekle','5. sıçramada yalnızca yükselme yolu alınır.','243 + 780 + 32'),A('Toplamı yaz','Sayılar toplanır.','1055 cm')],
 puf='Ara sıçramaların yolu iki kez, bırakılma ve son çıkış yolu bir kez alınır.')

# ================= 18 zor · düz · periyodik özyineleme =================
a=[None,3,7]
for n in range(1,120): a.append(a[n+1]-a[n])
assert a[1:8]==[3,7,4,-3,-7,-4,3] and sum(a[1:7])==0
v=sum(a[1:101]); assert v==11==sum(a[1:5])
e=[sum(a[1:4]),sum(a[1:6]),a[100],0]; assert e==[14,4,-3,0] and len({v,*e})==5
q('0018',tipId='dzi-ozyine',tip='Özyinelemeli diziler',z='zor',alt='Periyodik Dizi',kaz='Her terimi iki önceki terimle tanımlanan dizide terimlerin kendini tekrar ettiğini görüp uzun bir toplamı hesaplar.',kalip='yeni nesil',
 kart='K-ADZ-06 (aₙ₊₂ = aₙ₊₁ − aₙ) · a₁ = 3, a₂ = 7; ilk 100 terim toplamı',
 metin='a₁ = 3, a₂ = 7 ve her n pozitif tam sayısı için aₙ₊₂ = aₙ₊₁ − aₙ eşitliğini sağlayan (aₙ) dizisi veriliyor.\nBuna göre, a₁ + a₂ + a₃ + … + a₁₀₀ toplamı kaçtır?',
 dogru=v,yan=[(e[0],'Kalan 4 terim yerine ilk 3 terimi toplamış: 3 + 7 + 4.','dikkat'),(e[1],'Kalan terim sayısını 5 almış: 3 + 7 + 4 + (−3) + (−7).','islem'),(e[2],'Toplam yerine 100. terimi bulmuş: a₁₀₀ = a₄.','bilgi'),(e[3],'Her tekrarın toplamının 0 olmasını bütün toplama genellemiş, kalan terimleri unutmuş.','dikkat')],
 istenen='İlk 100 terimin toplamı.',ip=['Kuralı birkaç terim için uygulayıp terimlerde bir tekrar olup olmadığına bak.'],bilgi=[OZB],
 ad=[A('Terimleri yaz','Kural art arda uygulanır.','3 · 7 · 4 · −3 · −7 · −4 · 3 · 7 …'),A('Tekrarı bul','Altıncı terimden sonra dizi kendini tekrar eder; 6 terimin toplamı 0 dır.','3 + 7 + 4 − 3 − 7 − 4 = 0'),A('100 ü ayır','100 = 6 × 16 + 4 olduğundan 16 tam tekrar ve 4 terim kalır.','16 tekrar + a₁ … a₄'),A('Kalanı topla','Kalan 4 terim, tekrarın ilk 4 terimidir.','3 + 7 + 4 − 3 = 11')],
 puf='Tekrar eden bir dizide uzun toplam, tam tekrar sayısı ile kalan terimlerin toplamına indirilir.')

# ================= 19 zor · öncüllü · Sn =================
Sn=lambda n:3**n+1
a=[None]+[Sn(n)-Sn(n-1) if n>1 else Sn(1) for n in range(1,8)]
assert a[1:5]==[4,6,18,54] and a[4]==54 and a[2]+a[3]+a[4]==78 and Fr(a[2],a[1])!=Fr(a[3],a[2])
sira=['Yalnız I','Yalnız II','I ve II','I ve III','II ve III']
q('0019',tipId='dzi-sn',tip='Sₙ ile aₙ ilişkisi',z='zor',alt='Toplamdan Terim',kaz='İlk n terim toplamı verilen dizinin terimlerini bulup dizinin geometrik olup olmadığını ve terim toplamlarını inceler.',kalip='öncüllü',
 kart='K-ADZ-07 (Sₙ = 3ⁿ + 1) · a₁ ayrı, n ≥ 2 için geometrik; öncüller a₄, geometriklik, a₂ + a₃ + a₄',
 metin='İlk n teriminin toplamı Sₙ = 3ⁿ + 1 olan (aₙ) dizisi için\nI. a₄ = 54 tür.\nII. Dizi geometriktir.\nIII. a₂ + a₃ + a₄ = 78 dir.\nifadelerinden hangileri doğrudur?',
 dogru='I ve III',sira=sira,yan=[('Yalnız I','III. öncülü yanlış sanmış: a₄ = 54 bulduktan sonra a₂ + a₃ + a₄ toplamında a₂ yi 3² + 1 = 10 alıp 82 bulmuş.','islem'),('Yalnız II','a₃/a₂ = 3 oranını görüp diziyi geometrik sanmış (a₂/a₁ = 3/2 yi denetlememiş); a₄ ü ve toplamı da yanlış bulmuş.','dikkat'),('I ve II','II. öncülü doğru sanmış: a₂ den sonra oran 3 olduğu için dizinin tamamını geometrik düşünmüş (a₁ = 4 ün oranı bozduğunu atlamış); III. öncülü yanlış sanmış.','dikkat'),('II ve III','a₄ yerine S₃ = 28 i bulup I. öncülü yanlış sanmış; II. öncülü de doğru sanmış.','dikkat')],
 istenen='Doğru olan öncüllerin hangisi ya da hangileri olduğu.',ip=['Önce a₁ i ve sonra n ≥ 2 için aₙ ifadesini ayrı ayrı bul.'],bilgi=[SNB,GEO],
 ad=[A('Terimleri bul','a₁ = S₁ ve n ≥ 2 için aₙ = Sₙ − Sₙ₋₁ hesaplanır.','a₁ = 4 · aₙ = 2 × 3ⁿ⁻¹ (n ≥ 2)'),A('I. öncülü denetle','a₄ = 2 × 3³ = 54.','I doğru'),A('II. öncülü denetle','a₂/a₁ = 6/4 iken a₃/a₂ = 3 tür; oran sabit değildir.','II yanlış'),A('III. öncülü denetle','6 + 18 + 54 = 78; ayrıca S₄ − S₁ = 82 − 4.','III doğru'),A('Sonucu yaz','Doğru öncüller birleştirilir.','I ve III')],
 puf='Sₙ den terim bulurken a₁ i ayrı hesapla; genel formül ilk terimi tutmayabilir.')

# ================= 20 zor · tablo · iki firmanın kazancı =================
A_=lambda n:30+7*(n-1); B_=lambda n:3*2**(n-1)
assert [A_(i) for i in (1,2,3)]==[30,37,44] and [B_(i) for i in (1,2,3)]==[3,6,12]
first=lambda f:next(n for n in range(1,60) if f(n))
v=first(lambda n:B_(n)>3*A_(n)); assert v==8
m1=first(lambda n:B_(n)>A_(n)); m2=v-1; m3=first(lambda n:3*2**n>A_(n)); m4=first(lambda n:3*2**(n-2)>3*A_(n))
assert (m1,m2,m3,m4)==(6,7,5,9) and len({v,m1,m2,m3,m4})==5
SK=tablo_svg(['Yıl','1','2','3'],[['A işletmesi (bin ₺)','30','37','44'],['B işletmesi (bin ₺)','3','6','12']])
q('0020',tipId='dzi-karma',tip='Aritmetik ve geometrik dizi birlikte',z='zor',alt='Kazanç Karşılaştırması',kaz='Biri aritmetik, diğeri geometrik artan iki dizinin terimlerini karşılaştırarak koşulu sağlayan ilk sırayı bulur.',kalip='hikâyeli',
 kart='K-ADZ-08 (A aritmetik, B geometrik) · 3 katını aşan ilk yıl',
 metin='İki küçük işletmenin yıllık kazançları aşağıdaki tabloda verilmiştir. A işletmesinin kazancı her yıl sabit bir miktar artmakta, B işletmesinin kazancı ise her yıl bir önceki yılın sabit bir katı olmaktadır. Bu değişim, tablodaki yıllardan sonra da aynen sürmektedir.\nBuna göre, B işletmesinin kazancının, A işletmesinin aynı yıldaki kazancının 3 katından fazla olduğu ilk yıl kaçıncı yıldır?',
 dogru=v,yan=[(m1,'“3 katından fazla” koşulunu atlayıp yalnız B > A olduğu ilk yılı bulmuş.','dikkat'),(m2,'İlk yıl 8. yıl bulduktan sonra “kaç yıl sonra” diye 1. yıldan sayıp 7 yazmış.','dikkat'),(m3,'B nin kuralını 3 · 2ⁿ (üssü n) yazıp yalnız B > A koşulunu aramış.','islem'),(m4,'B nin kuralını 3 · 2ⁿ⁻² (üssü bir eksik) yazıp 3 katı koşulunu aramış.','islem')],
 istenen='B nin kazancının A nın kazancının 3 katını aştığı ilk yıl.',ip=['Her iki işletme için n. yıl kazancını veren ifadeyi ayrı ayrı yaz.'],bilgi=[ARI,GEO],sekil=SK,
 ad=[A('A için kuralı yaz','Her yıl 7 bin ₺ artıyor.','A(n) = 30 + 7(n − 1)'),A('B için kuralı yaz','Her yıl 2 katına çıkıyor.','B(n) = 3 × 2ⁿ⁻¹'),A('Yıllara bak','Koşul B(n) > 3 × A(n) olarak denenir.','7. yıl: 192 < 216'),A('İlk yılı bul','8. yılda koşul sağlanır.','8. yıl: 384 > 237')],
 puf='Koşulu sağlamayan son yıl ile sağlayan ilk yılı yan yana yazıp karşılaştır.')

# ---------- bitiş ----------
def bitir_ayt(P,onek,k):
    for q_ in P.ANA: q_['kardes']=None
    P.yaz(os.path.join(HD0,f'{onek}-1.json'),f'/tmp/bos-{onek}.json')
    tipler={}
    for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=k))['kartlar'].append(c['id'])
    json.dump(dict(konu=P.konu_adi,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 AYT Matematik çıkmış soruları ve yayın soru bankaları (yalnız mantık), MEB 11–12. sınıf müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar',f'{onek}.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler))
bitir_ayt(P,'dizi',UK)
