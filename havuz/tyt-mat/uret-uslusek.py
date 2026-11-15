"""Üslü Sayılar · şekilli paket (uslusek): 8 soru, hepsi şekilli/tablolu/grafikli. Kardeş yok, ipucu 1. Her cevap ve çeldirici değer kodla hesaplanıp assert edilir.
Şekil ölçüleri Python'da üretilir; TikZ gövdesi aynı değerlerden f-string ile yazılır (bkz. havuz/URETIM-SEKIL.md)."""
import sys,os,math
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
H.KONU='Üslü Sayılar'
P=Parti('uslusek','Üslü Sayılar','mat|Üslü Sayılar')
KY='ÖSYM 2018–2026 TYT Matematik (şekilli/tablolu üslü sayı soruları, yalnız mantık) · MEB 9. sınıf'
TP=lambda g:tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'+g+'\n\\end{tikzpicture}')
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)

KAT=B('Katlanarak değişim','her adımda değer sabit bir r katına çıkıyorsa n adım sonra değer, başlangıç × rⁿ olur. Örnek: 5 olan değer her adımda 3 katına çıkarsa 2 adım sonra 5 × 3² = 45 olur')
BG=B('Bilimsel gösterim','a × 10ⁿ biçimindeki sayılar bölünürken katsayılar kendi arasında, 10’un kuvvetleri kendi arasında bölünür; 10ᵐ ÷ 10ⁿ = 10ᵐ⁻ⁿ. Örnek: (8 × 10⁻³) ÷ (2 × 10⁻⁵) = 4 × 10² = 400')
KUV=B('Aynı tabanlı kuvvetler','aᵐ × aⁿ = aᵐ⁺ⁿ, aᵐ ÷ aⁿ = aᵐ⁻ⁿ ve (aᵐ)ⁿ = aᵐⁿ. Örnek: 3² × 3⁴ = 3⁶ ve (3²)³ = 3⁶')

kart('K-USS-01','Hücre bölünme ağacı','Ağaç şemasından her hücrenin kaç hücreye bölündüğü okunur; n bölünme sonunda hücre sayısı başlangıç sayısı × (bölünme çarpanı)ⁿ olur.','Başlangıçtaki hücre sayısını unutmak; üssü çarpan, çarpanı üs yapmak (3⁶ gibi); bölünme sayısını bir fazla ya da eksik almak.','kolay','şekilli',3,'uss-agac','Bölünme ağacından katlanarak artma',KY)
kart('K-USS-02','Ölçek tablosu','Tablodan iki uzunluk okunur; bilimsel gösterimde katsayılar kendi arasında, 10’un kuvvetleri üs farkıyla bölünür.','Üsleri hiç hesaba katmamak; üs farkının işaretini ters almak; katsayıları bölmek yerine çarpmak.','kolay','tablo',3,'uss-olcek','Bilimsel gösterimli ölçek tablosu',KY)
kart('K-USS-03','Katlanan kâğıt','Her katlamada alan yarıya iner; başlangıç ve son alan 2’nin kuvveti olarak yazılıp üsler karşılaştırılır.','Alan oranını katlama sayısı sanmak; üssü doğrudan sonuç yazmak; katlama sayısını bir eksik ya da fazla bulmak.','orta','şekilli',4,'uss-katla','Katlanan kâğıtta alan ve katlama sayısı',KY)
kart('K-USS-04','Yarı ömür çubuk grafiği','Çubuk grafikte ölçümler her saat yarıya iniyorsa kalan miktar başlangıç ÷ 2ⁿ’dir; eşik değerin altına inen ilk n, 2ⁿ’in başlangıç değerini geçtiği ilk n’dir.','2ⁿ değerlerini yanlış hesaplamak; eşit olmayan değeri eşikten küçük saymak; ölçüm aralığını yanlış okumak.','orta','grafik',4,'uss-yari','Yarılanma grafiğinden eşik problemi',KY)
kart('K-USS-05','Sayı piramidi','Üstteki kutu alttaki iki kutunun çarpımıysa taban ve üst kutular 2’nin kuvveti olarak yazılır; üsler toplanarak bilinmeyen üs bulunur.','Üsleri toplamak yerine çarpmak; bilinmeyen kutunun iki kez çarpıldığını gözden kaçırmak; üssü kutuya yazmak.','orta','şekilli',4,'uss-piramit','Çarpım piramidinde bilinmeyen kutu',KY)
kart('K-USS-06','İç içe kareler','Kenar orta noktalarını birleştirmek alanı yarıya indirir; alanlar 2’nin kuvvetleri olarak yazılıp ortak çarpan parantezine alınarak toplanır.','Terim sayısını yanlış almak; sonsuz toplamı sanmak; alanı yarıya değil her alanı ilk alana eşit almak.','zor','şekilli',5,'uss-ickare','İç içe karelerde alanlar toplamı',KY)
kart('K-USS-07','Göl kaplama tablosu','Tablodaki alanlar her gün iki katına çıkıyorsa n. gündeki alan başlangıç × 2ⁿ⁻¹’dir; hedef alan, 2’nin kuvveti olarak yazılıp üsler eşitlenir.','Gün numarasıyla üssü karıştırmak; yarısı yerine tamamını almak; alanı gün sanmak.','orta','tablo',4,'uss-gol','Alan tablosundan yarıya ulaşılan gün',KY)
kart('K-USS-08','Boş merkezli kare dizisi','Şekil dizisinden her adımda boyalı kare sayısının 8 katına çıktığı görülür; istenen iki şeklin sayıları üslü yazılıp çıkarılır.','8’in kuvvetini çarpımla karıştırmak; şekil numarasını bir eksik ya da fazla almak; farkı oran sanmak.','zor','şekilli',5,'uss-dizi','Örüntülü şekil dizisinde üslü sayma',KY)

# ---------- 01 · kolay · hücre ağacı ----------
n0,r1,nb=3,2,6; sayi=n0*r1**nb
assert sayi==192 and 3**6==729 and 2**6==64 and n0*r1**(nb+1)==384 and n0*nb*r1==36 and n0*r1**(nb-1)==96 and n0*r1**2==12
sp=.42; g=''
lf=lambda i:i*sp+(i//4)*.35
for r in range(3):
    xs=[lf(4*r+j) for j in range(4)]; m1=[(xs[0]+xs[1])/2,(xs[2]+xs[3])/2]; x0=(m1[0]+m1[1])/2
    for j in range(4): g+=f'\\draw ({m1[j//2]:.3f},-1) -- ({xs[j]:.3f},-2);'
    for j in range(2): g+=f'\\draw ({x0:.3f},0) -- ({m1[j]:.3f},-1);'
    for (x,y) in [(x0,0)]+[(m,-1) for m in m1]+[(x,-2) for x in xs]:
        g+=f'\\filldraw[fill=vurgu!30,draw=black] ({x:.3f},{y}) circle (.13);'
for y,t in [(0,'Başlangıç'),(-1,'1. bölünme'),(-2,'2. bölünme')]: g+=f'\\node[anchor=east] at (-.35,{y}) {{{t}}};'
sek=TP(g)
q('0001',tipId='uss-agac',tip='Bölünme ağacından katlanarak artma',z='kolay',alt='Katlanarak Artma',kaz='Bölünme şemasından bölünme çarpanını okuyup n bölünme sonundaki hücre sayısını üslü ifadeyle bulur.',kalip='şekilli',sekil=sek,
 kart='K-USS-01 (hücre bölünme ağacı) · 3 hücre, her bölünmede ikiye, 6 bölünme',
 metin='Şekilde, bir laboratuvar ortamındaki üç hücrenin ilk iki bölünmesi gösterilmiştir. Hücrelerin hepsi aynı anda ve aynı biçimde bölünmeye devam etmekte, hiçbir hücre ölmemektedir.\nBuna göre başlangıçtan itibaren 6 bölünme tamamlandığında toplam kaç hücre olur?',
 dogru=192,yan=[(36,'Üs almak yerine çarpmış: 3 × 6 × 2 = 36; oysa her bölünmede sayı 2 katına çıkar.','islem'),(64,'Başlangıçtaki 3 hücreyi hesaba katmamış; yalnız 2⁶ = 64 bulmuş.','dikkat'),(96,'5 bölünme saymış (ilk bölünmeyi atlamış): 3 × 2⁵ = 96.','dikkat'),(12,'Şekildeki son satırı (2. bölünme sonundaki 12 hücre) cevap olarak yazmış.','dikkat')],
 istenen='6 bölünme sonundaki toplam hücre sayısı.',
 ip=['Şekilde bir hücrenin her bölünmede kaç hücreye dönüştüğünü ve başlangıçta kaç hücre olduğunu say.'],
 bilgi=[KAT],
 ad=[A('Şemayı oku','Başlangıçta 3 hücre vardır; her hücre bir bölünmede 2 hücreye ayrılır.','3 → 6 → 12'),A('Üslü yaz','6 bölünme sonunda sayı, her adımda 2 katına çıkar.','3 × 2⁶'),A('Hesapla','2⁶ = 64.','3 × 64 = 192')],
 puf='Katlanarak artan sorularda başlangıç değeri ayrı bir çarpan olarak kalır: başlangıç × çarpanⁿ.')

# ---------- 02 · kolay · ölçek tablosu ----------
assert Fr(6,10**4)/Fr(3,10**5)==20 and Fr(6,10**4)/Fr(3,10**6)==200 and Fr(6,3)==2 and Fr(2,10)==Fr(1,5) and 6*3*10==180 and Fr(6,10**4)/Fr(2,10**7)==3000
sek=tablo_svg(['Cisim','Boyut (m)'],[['Kum tanesi','6 × 10⁻⁴'],['Polen tanesi','3 × 10⁻⁵'],['Küf sporu','4 × 10⁻⁶'],['Virüs','2 × 10⁻⁷']])
q('0002',tipId='uss-olcek',tip='Bilimsel gösterimli ölçek tablosu',z='kolay',alt='Bilimsel Gösterim',kaz='Tabloda bilimsel gösterimle verilen iki uzunluğun oranını katsayıları ve 10’un kuvvetlerini ayrı ayrı bölerek bulur.',kalip='tablo',sekil=sek,
 kart='K-USS-02 (ölçek tablosu) · kum tanesi ile polen tanesinin boy oranı',
 metin='Aşağıdaki tabloda bazı cisimlerin boyutları metre cinsinden bilimsel gösterimle verilmiştir.\nBuna göre kum tanesinin boyu, polen tanesinin boyunun kaç katıdır?',
 dogru=20,yan=[(2,'Yalnız katsayıları bölmüş (6 ÷ 3 = 2); 10’un kuvvetlerinin oranını hesaba katmamış.','dikkat'),(3000,'Polen yerine virüs satırını (2 × 10⁻⁷) okumuş: 6 × 10⁻⁴ ÷ 2 × 10⁻⁷ = 3000.','dikkat'),(180,'Katsayıları bölmek yerine çarpmış: 6 × 3 × 10 = 180.','islem'),(200,'Polen tanesinin boyunu 3 × 10⁻⁶ okumuş (satır kayması): 6 × 10⁻⁴ ÷ 3 × 10⁻⁶ = 200.','dikkat')],
 istenen='Kum tanesinin boyunun polen tanesinin boyuna oranı.',
 ip=['Oranı yazarken katsayılar ve 10’un kuvvetleri için ayrı ayrı bölme yap.'],
 bilgi=[BG],
 ad=[A('Değerleri oku','Tablodan iki satırı seç.','6 × 10⁻⁴ ve 3 × 10⁻⁵'),A('Oranı kur','Katsayıları ve kuvvetleri ayrı böl.','(6 ÷ 3) × (10⁻⁴ ÷ 10⁻⁵)'),A('Hesapla','10⁻⁴ ÷ 10⁻⁵ = 10⁻⁴⁺⁵ = 10¹.','2 × 10 = 20')],
 puf='Bilimsel gösterimde oran: katsayıların oranı × 10’un kuvvetlerinin oranı; üs farkını (pay − payda) hesapla.')

# ---------- 03 · orta · üçe katlanan kâğıt ----------
w3,h3=81,27; A0=w3*h3; hedef=9
assert A0==3**7 and hedef==3**2 and A0//hedef==243 and 3**5==243
nk=round(math.log(A0//hedef,3)); assert nk==5 and 3**nk*hedef==A0 and 3**2==9 and 7-1==6
sc=.04; g=''
dims=[(81,27),(27,27),(9,27)]; x0=0
for i,(a,b) in enumerate(dims):
    ww,hh=a*sc,b*sc
    g+=f'\\draw[thick] ({x0:.3f},0) rectangle ({x0+ww:.3f},{hh:.3f});'
    if i<2:
        ln,ll=(ww,'v') if a>=b else (hh,'h')
        if a>=b:
            for k in (1,2): g+=f'\\draw[dashed,vurgu,thick] ({x0+ww*k/3:.3f},-.12) -- ({x0+ww*k/3:.3f},{hh+.12:.3f});'
        else:
            for k in (1,2): g+=f'\\draw[dashed,vurgu,thick] ({x0-.12:.3f},{hh*k/3:.3f}) -- ({x0+ww+.12:.3f},{hh*k/3:.3f});'
    g+=f'\\node at ({x0+ww/2:.3f},{-.42}) {{{a} cm}};'
    if i==0: g+=f'\\node[anchor=east] at ({-.08},{hh/2:.3f}) {{{b} cm}};'
    if i<2:
        nx=x0+ww+.35; g+=f'\\draw[-{{Stealth[length=1.8mm]}}] ({nx-.15:.3f},{hh/2:.3f}) -- ({nx+.3:.3f},{hh/2:.3f});'
        x0=nx+.5
sek=TP(g)
q('0003',tipId='uss-katla',tip='Katlanan kâğıtta alan ve katlama sayısı',z='orta',alt='Katlanarak Azalma',kaz='Her katlamada alanın üçte birine indiğini kullanarak istenen alana ulaşmak için gereken katlama sayısını üslü ifadelerle bulur.',kalip='şekilli',sekil=sek,
 kart='K-USS-03 (katlanan kâğıt) · 81 × 27 cm, üçe katlama, kalan alan 9 cm², katlama sayısı',
 metin='Dikdörtgen biçimindeki bir kâğıt, şekilde ilk iki katlanışı gösterildiği gibi her seferinde kesikli çizgilerden üç eş parça üst üste gelecek biçimde katlanmakta ve katlamalar aynı biçimde sürdürülmektedir.\nKatlanmış kâğıdın alanı ilk kez 9 cm² olduğunda kâğıt kaç kez katlanmıştır?',
 dogru=5,yan=[(6,'Alan oranı 3⁵ iken ilk katlamayı da fazladan sayıp 6 bulmuş.','dikkat'),(7,'Başlangıç alanının üssünü (2187 = 3⁷) katlama sayısı sanmış.','dikkat'),(9,'Hedef alanın değerini (9) katlama sayısı sanmış.','dikkat'),(243,'Alanlar oranını (2187 ÷ 9 = 243) katlama sayısı olarak yazmış; üssü almamış.','islem')],
 istenen='Alan 9 cm² olana kadar yapılan katlama sayısı.',
 ip=['Her katlamada alanın kaçta kaçına indiğini düşün; ilk alanı 3’ün kuvveti olarak yaz.'],
 bilgi=[KAT,KUV],
 ad=[A('İlk alan','Şekildeki kenarlarla alan bulunur.','81 × 27 = 2187 = 3⁷ cm²'),A('Katlama etkisi','Her katlamada alan üçte birine iner, yani 3’e bölünür; n katlamada 3ⁿ’e bölünür.','3⁷ ÷ 3ⁿ = 9'),A('Üsleri eşitle','9 = 3² olduğundan üsler eşitlenir.','7 − n = 2'),A('Çöz','Katlama sayısını bul.','n = 5')],
 puf='Katlamalı sorularda önce alan 3’ün (ya da 2’nin) kuvveti olarak yazılır; her katlama üssü 1 azaltır.')

# ---------- 04 · orta · yarı ömür çubuk grafik ----------
m0=640; v=[m0,m0//2,m0//4]
assert v==[640,320,160] and 640==5*2**7
ilk=min(n for n in range(1,30) if Fr(m0,2**n)<1); assert ilk==10 and Fr(m0,2**9)==Fr(5,4) and Fr(m0,2**10)==Fr(5,8) and Fr(m0,2**11)<1
sc=3.2/640; g=''
for t in [0,160,320,480,640]: g+=f'\\draw ({-.08},{t*sc:.3f}) -- (0,{t*sc:.3f});\\node[anchor=east,font=\\footnotesize] at (-.1,{t*sc:.3f}) {{{t}}};'
g+=f'\\draw[thick] (0,0) -- (0,{3.8:.3f});\\draw[thick] (0,0) -- (4.6,0);\\node[font=\\footnotesize,anchor=south west] at (-.9,3.85) {{Kütle (mg)}};'
for i,(vv,nm) in enumerate(zip(v,['Başlangıç','1. saat','2. saat'])):
    xc=.9+i*1.4; g+=f'\\filldraw[fill=vurgu!35,draw=black,thick] ({xc-.4:.3f},0) rectangle ({xc+.4:.3f},{vv*sc:.3f});\\node[anchor=south] at ({xc:.3f},{vv*sc:.3f}) {{{vv}}};\\node[anchor=north,font=\\footnotesize] at ({xc:.3f},-.05) {{{nm}}};'
sek=TP(g)
q('0004',tipId='uss-yari',tip='Yarılanma grafiğinden eşik problemi',z='orta',alt='Katlanarak Azalma',kaz='Çubuk grafikten yarılanma örüntüsünü okuyup miktarın bir eşik değerin altına ilk indiği zamanı üslü ifadelerle bulur.',kalip='grafik',sekil=sek,
 kart='K-USS-04 (yarı ömür çubuk grafiği) · 640 mg, 1 mg eşiği',
 metin='Bir laboratuvarda radyoaktif bir maddenin kütlesi her saat aynı oranla azalmaktadır; ilk iki saatteki ölçümler şekildeki çubuk grafikte verilmiştir. Madde dışarıdan ek yapılmadan aynı biçimde azalmaya devam etmektedir.\nBuna göre maddenin kütlesi kaçıncı saatin sonunda ilk kez 1 mg’ın altına iner?',
 dogru=10,yan=[(9,'9. saatte 640 ÷ 512 = 1,25 mg kalmasına rağmen bunu 1 mg’ın altı saymış.','dikkat'),(8,'8. saatte 640 ÷ 256 = 2,5 mg kalmışken bunu 1 mg’a yakın sayıp yuvarlayarak orada durmuş.','dikkat'),(11,'2¹⁰ = 1024 > 640 bulup “ilk kez” ifadesi için bir saat daha eklemiş.','dikkat'),(640,'Başlangıç kütlesini (640 mg) saat sayısı sanmış.','dikkat')],
 istenen='Kütlenin ilk kez 1 mg’ın altına indiği saat.',
 ip=['Çubuklardaki iki ardışık değerin oranından her saat ne kadarının kaldığını bul.'],
 bilgi=[KAT,KUV],
 ad=[A('Örüntüyü oku','Grafikte kütle her saat yarıya iniyor.','640 → 320 → 160'),A('Genel terim','n saat sonra kütle 640 ÷ 2ⁿ mg’dır.','640 ÷ 2ⁿ < 1'),A('Eşitsizliği çöz','2ⁿ > 640 olmalı; 2⁹ = 512 yetmez, 2¹⁰ = 1024 yeter.','n ≥ 10'),A('Doğrula','10. saatte 640 ÷ 1024 = 0,625 mg < 1 mg; 9. saatte 1,25 mg > 1 mg.','n = 10')],
 puf='“İlk kez altına iner” ifadesinde sınır değere eşit ya da büyük kalan son adımı da kontrol et.')

# ---------- 05 · orta · sayı piramidi ----------
a5,c5,t5=2,4,20; x5=(t5-a5-c5)//2; assert (t5-a5-c5)%2==0 and x5==7 and 2**x5==128
assert 2**a5*2**x5*2**x5*2**c5==2**t5 and 2**(t5-a5-c5)==2**14==16384 and 2**(t5//2-a5)==256 and 2**(t5//2-c5)==64
bot=lambda s,x,y:f'\\node[draw,thick,minimum width=1.8cm,minimum height=.8cm] at ({x},{y}) {{{s}}};'
g=bot('$4$',-1.8,0)+bot('$x$',0,0)+bot('$16$',1.8,0)+bot('',-.9,.8)+bot('',.9,.8)+bot('$2^{20}$',0,1.6)
sek=TP(g)
q('0005',tipId='uss-piramit',tip='Çarpım piramidinde bilinmeyen kutu',z='orta',alt='Üslü Denklem',kaz='Çarpım piramidinde üsleri toplayarak bilinmeyen tabandaki kutuyu 2’nin kuvveti olarak bulur.',kalip='şekilli',sekil=sek,
 kart='K-USS-05 (sayı piramidi) · 4, x, 16 tabanı, tepe 2²⁰',
 metin='Şekildeki sayı piramidinde alt sıradaki kutulardan her iki komşunun çarpımı, bu ikisinin hemen üstündeki kutuya yazılmıştır. Üstteki kutu da kendi altındaki iki kutunun çarpımıdır.\nBuna göre x pozitif tam sayısı kaçtır?',
 dogru=128,yan=[(7,'Üssü (2⁷’deki 7) cevap sanmış; x’in kendisi 2⁷ = 128’dir.','dikkat'),(64,'Üstteki üssü ikiye bölüp (20 ÷ 2 = 10) 16 = 2⁴’ün üssünü çıkarmış: 10 − 4 = 6, x = 2⁶ = 64.','islem'),(14,'Üstteki üsten taban üslerini çıkarıp (20 − 6 = 14) ikiye bölmeyi unutmuş ve üssü kutuya yazmış.','dikkat'),(256,'x’in iki kez çarpıldığını görmüş ama yalnız 4 = 2² çarpanını çıkarmış (20 ÷ 2 − 2 = 8): 2⁸ = 256.','islem'),],
 istenen='Bilinmeyen x değeri.',
 ip=['Üstteki sayıyı, alttaki üç kutunun çarpımı olarak yaz; x kaç kez çarpılıyor?'],
 bilgi=[KUV],
 ad=[A('Orta kutular','4 = 2² ve 16 = 2⁴; x = 2ᵗ olsun. Orta sıra kutuları 2²·2ᵗ ve 2ᵗ·2⁴’tür.','2²⁺ᵗ ve 2ᵗ⁺⁴'),A('Tepe','Tepe, orta sıranın çarpımıdır; x iki kez çarpılır.','2²⁺ᵗ × 2ᵗ⁺⁴ = 2⁶⁺²ᵗ'),A('Üsleri eşitle','Tepe 2²⁰ olduğundan üsler eşit olmalı.','6 + 2t = 20 → t = 7'),A('x değeri','x = 2⁷.','x = 128')],
 puf='Çarpım piramidinde ortadaki kutu üst kutuya iki yoldan katılır; üs toplamında iki kez yazılmalıdır.')

# ---------- 06 · zor · iç içe kareler ----------
S=32; al=[S*S//2**k for k in range(6)]; tp=sum(al)
assert al==[1024,512,256,128,64,32] and tp==2016 and sum(S*S//2**k for k in range(5))==1984 and sum(S*S//2**k for k in range(7))==2032 and 6*1024==6144 and sum(S*S//2**k for k in range(8))==2040 and 2*1024==2048
sc=4.2/S; pts=[(0,0),(S*sc,0),(S*sc,S*sc),(0,S*sc)]; g=''
for k in range(4):
    g+='\\draw[thick] '+' -- '.join(f'({x:.3f},{y:.3f})' for x,y in pts)+' -- cycle;'
    pts=[((pts[i][0]+pts[(i+1)%4][0])/2,(pts[i][1]+pts[(i+1)%4][1])/2) for i in range(4)]
g+=f'\\node at ({S*sc/2:.3f},-.32) {{{S} cm}};'
sek=TP(g)
q('0006',tipId='uss-ickare',tip='İç içe karelerde alanlar toplamı',z='zor',alt='Büyümelerin Karşılaştırılması',kaz='Kenar orta noktalarıyla oluşan iç içe karelerin alanlarını 2’nin kuvvetleri olarak yazıp ilk altı karenin alanlar toplamını bulur.',kalip='şekilli',sekil=sek,
 kart='K-USS-06 (iç içe kareler) · kenarı 32 cm, ilk altı karenin alanlar toplamı',
 metin='Şekilde, kenar uzunluğu verilen bir karenin kenarlarının orta noktaları birleştirilerek ikinci kare, ikinci karenin kenarlarının orta noktaları birleştirilerek üçüncü kare elde edilmiştir. İşlem aynı biçimde sürdürülmektedir; şekilde ilk dört kare gösterilmiştir.\nBuna göre ilk altı karenin alanları toplamı kaç cm²’dir?',
 dogru=2016,yan=[(2032,'Yedi kare toplamış (1024 + … + 16); altı terim toplamalıydı.','dikkat'),(2040,'Sekiz kare toplamış (1024 + … + 8); altı terim toplamalıydı.','dikkat'),(2048,'Tüm alanların sonsuz toplamını (2 × 1024) yazmış; yalnız ilk altı kare isteniyor.','bilgi'),(6144,'Her karenin alanını ilk karenin alanı sanıp 6 × 1024 = 6144 bulmuş; alan her adımda yarıya iner.','islem')],
 istenen='İlk altı karenin alanları toplamı.',
 ip=['Orta noktaları birleştirince oluşan karenin alanının, dıştaki karenin alanına oranını bul.'],
 bilgi=[KUV,B('Ortak çarpan parantezi','terimlerde ortak çarpan dışarı alınır. Örnek: 3² + 3³ + 3⁴ = 3² × (1 + 3 + 9) = 117')],
 ad=[A('Alan oranı','Orta noktaları birleştirilen karenin alanı dıştakinin yarısıdır.','1. kare: 32² = 1024 = 2¹⁰ cm²'),A('Alanlar','Alanlar her adımda yarıya iner.','2¹⁰ + 2⁹ + 2⁸ + 2⁷ + 2⁶ + 2⁵'),A('Ortak çarpan','En küçük kuvvet olan 2⁵’i dışarı al.','2⁵ × (2⁵ + 2⁴ + 2³ + 2² + 2 + 1)'),A('Parantez','Parantezdeki toplam 63’tür.','32 × 63'),A('Çarp','Sonucu bul.','2016')],
 puf='Yarıya inen terimleri toplarken en küçük kuvveti ortak çarpan al; parantez 1, 2, 4, … biçiminde kolay toplanır.')

# ---------- 07 · orta · göl kaplama tablosu ----------
gun=lambda d:4*2**(d-1)
assert [gun(d) for d in (1,2,3)]==[4,8,16] and gun(10)==2048 and gun(11)==4096 and gun(9)==1024 and 4096//2==2048 and gun(12)==8192
d7=next(d for d in range(1,30) if gun(d)==2048); assert d7==10
sek=tablo_svg(['Gün','Bitkinin kapladığı alan (m²)'],[['1','4'],['2','8'],['3','16']])
q('0007',tipId='uss-gol',tip='Alan tablosundan yarıya ulaşılan gün',z='orta',alt='Katlanarak Artma',kaz='Tablodaki katlanarak artan alanı üslü ifadeyle yazıp hedef alanın yarısına ulaşılan günü bulur.',kalip='tablo',sekil=sek,
 kart='K-USS-07 (göl kaplama tablosu) · 4 m² ile başlayan, 4096 m²’lik göl, yarısı',
 metin='Bir gölde yayılan su bitkisinin ilk üç günde kapladığı alan aşağıdaki tabloda verilmiştir. Bitki aynı oranla yayılmayı sürdürmekte ve alanı 4096 m² olan gölün tamamını kaplayana kadar yok olmamaktadır.\nBuna göre bitki, gölün yarısını kaçıncı günde kaplamıştır?',
 dogru=10,yan=[(9,'n. günün alanını 4 · 2ⁿ sanıp 4 · 2ⁿ = 2048 → 2ⁿ = 512 → n = 9 bulmuş; oysa 1. günde 4 m² vardır, n. günde 4 · 2ⁿ⁻¹ olur.','dikkat'),(11,'Gölün tamamını kaplayan günü (11. gün) bulmuş; yarısı bir gün önce kaplanır.','dikkat'),(12,'2¹² = 4096 diye gölün tamamı için üsle günü eşitlemiş (n = 12); 1. günde alan 2², n. günde 2ⁿ⁺¹ olur.','bilgi'),(2048,'Gölün yarısının alanını (2048 m²) gün sayısı olarak yazmış.','dikkat')],
 istenen='Yarısının kaplandığı gün.',
 ip=['Tablodaki alanların her gün kaç katına çıktığını bul; n. günün alanını n cinsinden yaz.'],
 bilgi=[KAT,KUV],
 ad=[A('Örüntü','Alan her gün 2 katına çıkar; 1. günde 4 = 2² m² vardır.','n. gün: 4 × 2ⁿ⁻¹ = 2ⁿ⁺¹ m²'),A('Hedef','Gölün yarısı 4096 ÷ 2 = 2048 m²’dir.','2048 = 2¹¹'),A('Üsleri eşitle','Aynı tabanda üsler eşit olmalı.','n + 1 = 11'),A('Gün','n değerini bul.','n = 10')],
 puf='n. günün alanını yazarken ilk günün üssüne dikkat et: ilk gün 2², n. gün 2ⁿ⁺¹’dir.')

# ---------- 08 · zor · boş merkezli kare dizisi ----------
def dolu(k,i,j):
    for _ in range(k):
        if i%3==1 and j%3==1: return False
        i//=3; j//=3
    return True
def boyali(k): n=3**k; return sum(dolu(k,i,j) for i in range(n) for j in range(n))
assert [boyali(k) for k in (1,2,3)]==[8,64,512] and 8**5==32768 and 8**5-8**3==32256
assert 8**5-8**4==28672 and 8**5-8**2==32704 and 8**5+8**3==33280 and 8**2==64
def izg(k,cs,ox):
    n=3**k; g=''
    for i in range(n):
        for j in range(n):
            if dolu(k,i,j): g+=f'\\fill[vurgu!55] ({ox+i*cs:.3f},{j*cs:.3f}) rectangle ({ox+(i+1)*cs:.3f},{(j+1)*cs:.3f});'
    for t in range(n+1): g+=f'\\draw[line width=.3pt] ({ox+t*cs:.3f},0) -- ({ox+t*cs:.3f},{n*cs:.3f});\\draw[line width=.3pt] ({ox:.3f},{t*cs:.3f}) -- ({ox+n*cs:.3f},{t*cs:.3f});'
    return g+f'\\draw[thick] ({ox:.3f},0) rectangle ({ox+n*cs:.3f},{n*cs:.3f});'
g=izg(1,.9,0)+izg(2,.9/3,3.6)+'\\node at (1.35,-.35) {Şekil 1};\\node at (4.95,-.35) {Şekil 2};'
sek=TP(g)
q('0008',tipId='uss-dizi',tip='Örüntülü şekil dizisinde üslü sayma',z='zor',alt='Büyümelerin Karşılaştırılması',kaz='Şekil dizisindeki boyalı kare sayılarının 8 katına çıkan örüntüsünü üslü ifadeyle yazıp iki şeklin farkını bulur.',kalip='şekilli',sekil=sek,
 kart='K-USS-08 (boş merkezli kare dizisi) · Şekil 5 ile Şekil 3’ün boyalı kare farkı',
 metin='Şekilde, bir şekil dizisinin ilk iki terimi verilmiştir. Dizide her yeni şekil, bir önceki şeklin boyalı küçük karelerinin her biri Şekil 1’deki desenin aynısıyla (3 × 3’lük bir blok olarak) değiştirilerek elde edilmektedir ve bu işlem aynı biçimde sürdürülmektedir.\nBuna göre Şekil 5’teki boyalı küçük kare sayısı, Şekil 3’teki boyalı küçük kare sayısından kaç fazladır?',
 dogru=32256,yan=[(64,'Şekil 5 ile Şekil 3 arasındaki farkı üs farkı sanıp 8⁵ ÷ 8³ = 8² = 64 bulmuş; fark istendiği hâlde oran almış.','islem'),(28672,'8⁵ − 8⁴ hesaplamış (Şekil 5 ile Şekil 4); Şekil 3 ile karşılaştırmalıydı.','dikkat'),(32704,'Şekil 3 yerine Şekil 2’yi (64) çıkarmış: 32768 − 64.','dikkat'),(33280,'Farkı bulmak yerine Şekil 5 ile Şekil 3’ü toplamış: 32768 + 512.','islem')],
 istenen='Şekil 5 ile Şekil 3’teki boyalı küçük kare sayıları farkı.',
 ip=['İlk iki şekildeki boyalı kare sayılarını sayıp bir şekilden sonrakine kaç katına çıkıldığını bul.'],
 bilgi=[KAT,B('Üslü sayıyla fark','aⁿ − aᵐ hesaplanırken üsler birbirinden çıkarılmaz; her kuvvet ayrı hesaplanıp çıkarılır. Örnek: 3⁴ − 3² = 81 − 9 = 72')],
 ad=[A('Şekil 1 ve 2’yi say','Şekil 1’de 8, Şekil 2’de 64 boyalı kare vardır.','8 → 64'),A('Örüntü','Her şekilde boyalı kare sayısı 8 katına çıkar; Şekil n’de 8ⁿ kare vardır.','Şekil 3: 8³ = 512'),A('Şekil 5','8⁵ hesaplanır.','8⁵ = 32768'),A('Farkı al','İki sayıyı ayrı ayrı hesaplayıp çıkar.','32768 − 512'),A('Sonuç','Farkı bul.','32256')],
 puf='Üslü sayıların farkı üslerin farkına eşit değildir; kuvvetleri ayrı ayrı hesapla, sonra çıkar.')

bitir(P,'uslusek','mat|Üslü Sayılar')
