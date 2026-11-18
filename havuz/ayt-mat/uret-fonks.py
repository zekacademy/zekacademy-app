"""AYT Matematik · Fonksiyonlar (20 soru): grafik, tablo, ok şeması, makine, sayı doğrusu şemaları; her doğru ve çeldirici değer kodla hesaplanıp assert edilir.
Kardeş yok, ipucu 1. Çıktı: ayt-mat/fonks-1.json, kartlar/fonks.json."""
import sys,os,json
HD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(HD,'..')
sys.path.insert(0,os.path.join(HV,'tyt-mat')); sys.path.insert(0,HV)
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
HD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(HD,'..')
H.KONU='Fonksiyonlar'
UK='amat|Fonksiyonlar'
P=Parti('fonks','Fonksiyonlar',UK,ders='AYT Matematik',idon='aytmat')
KY='ÖSYM 2018–2026 AYT Matematik çıkmış fonksiyon soruları (bileşke, ters, grafik okuma, dönüşümler, fonksiyonel denklem; yalnız mantık) · MEB 11–12. sınıf'
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)
def fig(body,font='\\small'): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font='+font+']\n'+body+'\n\\end{tikzpicture}')
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)
def uniq(v,e): assert len({Fr(x) for x in [v]+list(e)})==5,(v,e)
MV='−'
def S(x):  # sayıyı metne yaz (eksi işareti −)
    return fm(x)
def mina(x): return fm(x)
MAVI='blue!70!black'; TUR='orange!90!black'; MOR='violet!80!black'; YES='vurgu!80!black'

# ---------- bilgi kutuları ----------
BIL=B('Bileşke fonksiyon','(f ∘ g)(x) = f(g(x)) demektir: önce içteki g, sonra dıştaki f uygulanır; genel olarak f ∘ g ile g ∘ f aynı değildir. Örnek: f(x) = x + 3, g(x) = 4x ise (f ∘ g)(2) = f(8) = 11 iken (g ∘ f)(2) = g(5) = 20’dir')
TER=B('Ters fonksiyon','birebir ve örten f için f(a) = b ise f⁻¹(b) = a’dır; f⁻¹’i bulmak için y = f(x) denkleminde x yalnız bırakılıp x ile y’nin yeri değiştirilir. Bileşkenin tersi (f ∘ g)⁻¹ = g⁻¹ ∘ f⁻¹’dir. Örnek: f(x) = 5x + 1 ise f⁻¹(x) = (x − 1)/5’tir')
DON=B('Grafik dönüşümleri','y = f(x − a) grafiği y = f(x)’in a birim sağa, y = f(x) + b grafiği b birim yukarı ötelenmişidir (a, b negatifse ters yön). Örnek: f(2) = 5 ise y = f(x − 3) + 1 grafiği (5, 6) noktasından geçer')
OZE=B('Tek, çift ve periyodik fonksiyon','her x için f(−x) = −f(x) ise f tek, f(−x) = f(x) ise çifttir; her x için f(x + T) = f(x) ise f periyodiktir ve T bir periyodudur. Örnek: f tek ve f(5) = 4 ise f(−5) = −4’tür; periyodu 3 olan g için g(10) = g(7) = g(4) = g(1)’dir')
PAR=B('Parçalı fonksiyon','her aralık için ayrı bir kural verilir; x değeri hangi aralığa düşüyorsa o kural kullanılır, aralığın uç değeri “≤” ya da “≥” içeren tarafa girer. Örnek: x < 1 için 2x, x ≥ 1 için x + 5 kuralıyla f(1) = 6, f(0) = 0’dır')
TAN=B('Birebir, örten ve bileşke','farklı elemanlar farklı elemanlara gidiyorsa fonksiyon birebir, değer kümesinin her elemanına ok geliyorsa örtendir. Birebir ve örten fonksiyonun tersi vardır. Örnek: ok şemasında B kümesinin bir elemanına iki ok geliyorsa fonksiyon birebir olamaz')
FDN=B('Fonksiyonel denklem','verilen eşitlik her x için sağlandığından x yerine uygun sayılar yazılarak denklem kurulur; bilinmeyen değerler birlikte çözülür. Örnek: f(x) + 3f(−x) = 4x ise x = 1 ve x = −1 yazılarak f(1), f(−1) için iki denklem elde edilir')
GRO=B('Grafikten bileşke ve denklem','f(f(x)) = k denkleminde önce f(u) = k çözülerek u değerleri, sonra her u için f(x) = u çözülerek x değerleri bulunur; çözüm sayısı, y = u yatay doğrusunun grafiği kestiği noktaların sayısıdır. Örnek: y = 2 doğrusu grafiği iki noktada kesiyorsa f(x) = 2 denkleminin iki çözümü vardır')

# ---------- kartlar (her tipId için bir kart) ----------
kartla('K-AFNK-01','Bileşke fonksiyon değeri','İçteki fonksiyon önce uygulanır; çıkan değer dıştaki fonksiyona girer; tablo, makine ve parametreli kurallarda sıra şemadan okunur.','Bileşke sırasını ters uygulamak; yalnız bir fonksiyonu uygulamak; parametreli denklemde ikinci köke bakmamak.','orta','tablo',3,'fn-bilesik','Bileşke fonksiyon değeri')
kartla('K-AFNK-02','Ters fonksiyon ve bileşkenin tersi','Ters için oklar ya da işlemler geriye çevrilir; bileşkenin tersi fonksiyonların terslerinin ters sırayla bileşkesidir.','f⁻¹’i 1/f sanmak; terslerin sırasını değiştirmemek; eksik okun yerini birebir-örtenlikten bulmamak.','orta','şekilli',4,'fn-ters','Ters fonksiyon ve bileşkenin tersi')
kartla('K-AFNK-03','Grafik dönüşümleri','Dönüşmüş grafiğin köşeleri asıl grafiğin köşeleriyle eşlenir; öteleme yönü ve miktarı köşe farkından okunur.','Sağa ötelemeyi +a sanmak; x ve y yönündeki kaymayı karıştırmak; çarpan ve toplamı sırayla uygulamamak.','kolay','grafik',3,'fn-donusum','Grafik dönüşümleri')
kartla('K-AFNK-04','Tek, çift ve periyodik fonksiyonlar','Verilen simetri ya da periyot ile istenen değer, bilinen bir değere indirgenir; tek ya da çift olmanın koşulları birlikte kullanılır.','Tek fonksiyonda işareti değiştirmemek; periyodu yanlış sayıda eklemek; f(0) = 0’ı unutmak.','orta','grafik',4,'fn-ozellik','Tek, çift ve periyodik fonksiyonlar')
kartla('K-AFNK-05','Parçalı fonksiyon değeri','Her giriş değeri aralıklara yerleştirilir, uç değerlerde eşitlik işaretine bakılır, iç içe değerde çıkan sayı yeniden aralığa konur.','Uç değeri yanlış aralığa koymak; ara değeri aralığa yeniden yerleştirmemek; kuralı ters aralığa uygulamak.','orta','tablo',4,'fn-parcali','Parçalı fonksiyon değeri')
kartla('K-AFNK-06','Birebir, örten ve tanım kümeleri','Fonksiyonun birebirliği ve örtenliği oklardan ya da tablodan tek tek sınanır; bileşkenin tanım kümesi iç fonksiyonun değerlerinin dış fonksiyonun tanım kümesine düşmesiyle bulunur.','Birebirliği örtenlikle karıştırmak; tanım kümesinin uçlarını yanlış dahil etmek; iç fonksiyonun kendi tanım kümesini unutmak.','orta','öncüllü',4,'fn-tanim','Birebir, örten ve tanım kümeleri')
kartla('K-AFNK-07','Fonksiyonel denklem','Verilen eşitliğe uygun değerler yazılarak bilinmeyen değerler için denklem sistemi kurulur; ya da değişken dönüşümüyle fonksiyonun kuralı bulunur.','Dönüşümde yeni değişkeni yanlış çözmek; tek denklemle yetinmek; öteleme yönünü ters kullanmak.','zor','düz',4,'fn-fonkdenk','Fonksiyonel denklem')
kartla('K-AFNK-08','Grafikten iç içe fonksiyon denklemi','Denklem iki aşamada çözülür: önce iç değerler, sonra her iç değer için x çözümleri; grafikte yatay doğrularla sayılır.','Yalnız ilk aşamayı sayıp bırakmak; bir iç değeri atlamak; aralık dışına çıkan değerlerin çözümünü saymak.','zor','grafik',4,'fn-grafikoku','Grafikten iç içe fonksiyon denklemi')

# ================= şekil yardımcıları =================
def pl(V,x):
    x=Fr(x)
    for (x1,y1),(x2,y2) in zip(V,V[1:]):
        if x1<=x<=x2: return Fr(y1)+Fr(y2-y1,x2-x1)*(x-x1)
    raise ValueError(x)
def graf(x0,x1,y0,y1,sx,sy,govde,xlab='x',ylab='y',xs=1,ys=1,fs='\\footnotesize'):
    o=[]
    for i in range(x0,x1+1,xs): o.append(f'\\draw[gray!35,thin] ({i*sx:.3f},{y0*sy:.3f}) -- ({i*sx:.3f},{y1*sy:.3f});')
    for j in range(y0,y1+1,ys): o.append(f'\\draw[gray!35,thin] ({x0*sx:.3f},{j*sy:.3f}) -- ({x1*sx:.3f},{j*sy:.3f});')
    o.append(f'\\draw[-{{Stealth}},thick] ({(x0-0.3)*sx:.3f},0) -- ({(x1+0.7)*sx:.3f},0) node[right] {{${xlab}$}};')
    o.append(f'\\draw[-{{Stealth}},thick] (0,{(y0-0.3)*sy:.3f}) -- (0,{(y1+0.7)*sy:.3f}) node[above] {{${ylab}$}};')
    for i in range(x0,x1+1,xs):
        if i!=0: o.append(f'\\node[below=2pt,font={fs}] at ({i*sx:.3f},{y0*sy:.3f}) {{${i}$}};')
    for j in range(y0,y1+1,ys):
        if j!=0: o.append(f'\\node[left=2pt,font={fs}] at ({x0*sx:.3f},{j*sy:.3f}) {{${j}$}};')
    o.append(govde); return '\n'.join(o)
def egri(V,sx,sy,renk,w='1.8pt',nokta=True,dash=''):
    o=[f'\\draw[line width={w},{renk}{dash}] '+' -- '.join(f'({x*sx:.3f},{y*sy:.3f})' for x,y in V)+';']
    if nokta:
        for x,y in V: o.append(f'\\fill[{renk}] ({x*sx:.3f},{y*sy:.3f}) circle (0.075);')
    return '\n'.join(o)
def ok3(Ae,Be,Ce,fp,gp,fcap='f',gcap='g'):
    xa,xb,xc=0,3.0,6.0; vs=0.85; h=2.1; o=[]
    for x,E,n,rn in ((xa,Ae,'A',MAVI),(xb,Be,'B',TUR),(xc,Ce,'C',YES)):
        o.append(f'\\draw[thick,{rn}] ({x},0) ellipse (0.6 and {h}); \\node[font=\\large\\bfseries] at ({x},{h+0.4}) {{{n}}};')
        for i,e in enumerate(E): o.append(f'\\node at ({x},{(len(E)-1)/2*vs-i*vs:.3f}) {{${e}$}};')
    y=lambda E,i:(len(E)-1)/2*vs-i*vs
    for a,b in fp: o.append(f'\\draw[-{{Stealth}},thick,{MAVI}] ({xa+0.33},{y(Ae,a):.3f}) -- ({xb-0.33},{y(Be,b):.3f});')
    for a,b in gp: o.append(f'\\draw[-{{Stealth}},thick,{TUR}] ({xb+0.33},{y(Be,a):.3f}) -- ({xc-0.33},{y(Ce,b):.3f});')
    o.append(f'\\node[font=\\large\\bfseries\\itshape,{MAVI}] at ({(xa+xb)/2},{-h-0.45}) {{{fcap}}}; \\node[font=\\large\\bfseries\\itshape,{TUR}] at ({(xb+xc)/2},{-h-0.45}) {{{gcap}}};')
    return '\n'.join(o)
def makine(giris,kutular,cikis):
    """kutular: [(ad, kural)] soldan sağa; giris ve cikis metin ('x' ya da sayı)."""
    o=[]; x=0.0; cols=[MAVI,TUR,YES,MOR]
    o.append(f'\\node[draw,thick,rounded corners=3pt,minimum width=1.0cm,minimum height=0.8cm] (g0) at (0,0) {{${giris}$}}; \\node[above=1pt,font=\\scriptsize] at (g0.north) {{giriş}};')
    prev='g0'
    for i,(ad,kural) in enumerate(kutular):
        nm=f'm{i}'; c=cols[i%4]
        o.append(f'\\node[draw={c},fill={c}!12,line width=1.4pt,rounded corners=3pt,minimum width=2.5cm,minimum height=1.1cm,right=0.9cm of {prev},align=center] ({nm}) {{\\textbf{{${ad}$}}\\\\[-1pt] ${kural}$}};')
        o.append(f'\\draw[-{{Stealth}},thick] ({prev}.east) -- ({nm}.west);'); prev=nm
    o.append(f'\\node[draw,thick,rounded corners=3pt,minimum width=1.0cm,minimum height=0.8cm,right=0.9cm of {prev}] (gs) {{${cikis}$}}; \\node[above=1pt,font=\\scriptsize] at (gs.north) {{çıkış}};')
    o.append(f'\\draw[-{{Stealth}},thick] ({prev}.east) -- (gs.west);')
    return '\n'.join(o)

# ================= 01 kolay · tablo ile bileşke =================
fT={1:2,2:1,3:4,4:5,5:3}; gT={1:2,2:4,3:5,4:1,5:3}
v=fT[gT[2]]+gT[fT[4]]
e=[gT[fT[2]]+fT[gT[4]], fT[gT[2]], fT[2]+gT[4]+0*1, gT[fT[4]]]
e[2]=fT[2]*0+fT[4]+gT[2]   # f ve g'yi içten dışa değil doğrudan toplamış: f(4)+g(2)
e=[e[0],e[1],e[2],e[3]]
uniq(v,e)
SK=tablo_svg(['x','1','2','3','4','5'],[['f(x)']+[str(fT[i]) for i in range(1,6)],['g(x)']+[str(gT[i]) for i in range(1,6)]])
q('0001',tipId='fn-bilesik',tip='Bileşke fonksiyon değeri',z='kolay',alt='Tabloyla Bileşke',kaz='Tabloyla verilen iki fonksiyonun bileşke değerlerini içteki fonksiyondan başlayarak hesaplar.',kalip='tablo',
 kart='K-AFNK-01 (tablo ile bileşke) · A = {1, 2, 3, 4, 5} üzerinde iki fonksiyon; (f ∘ g)(2) + (g ∘ f)(4)',
 metin='A = {1, 2, 3, 4, 5} kümesi üzerinde tanımlı f ve g fonksiyonlarının değerleri aşağıdaki tabloda verilmiştir.\nBuna göre (f ∘ g)(2) + (g ∘ f)(4) toplamı kaçtır?',
 dogru=v,yan=[(e[0],f'Bileşkelerin sırasını ters uygulamış: (g ∘ f)(2) + (f ∘ g)(4) = {gT[fT[2]]} + {fT[gT[4]]}.','dikkat'),(e[1],f'İkinci terimi toplamaya katmayıp yalnız (f ∘ g)(2) = {fT[gT[2]]} değerini yazmış.','dikkat'),(e[2],f'Bileşke yerine f(4) + g(2) = {fT[4]} + {gT[2]} toplamını almış.','islem'),(e[3],f'Birinci terimi unutup yalnız (g ∘ f)(4) = {gT[fT[4]]} değerini yazmış.','dikkat')],
 istenen='(f ∘ g)(2) + (g ∘ f)(4) toplamı.',ip=['Her terimde önce içteki fonksiyonun değerini tablodan oku, çıkan sayıyı dıştaki fonksiyonun satırında ara.'],bilgi=[BIL],sekil=SK,
 ad=[A('Birinci terim','Önce g(2), sonra f ile devam edilir.',f'g(2) = {gT[2]} → f({gT[2]}) = {fT[gT[2]]}'),A('İkinci terim','Önce f(4), sonra g ile devam edilir.',f'f(4) = {fT[4]} → g({fT[4]}) = {gT[fT[4]]}'),A('Topla','İki bileşke değeri toplanır.',f'{fT[gT[2]]} + {gT[fT[4]]} = {v}')],
 puf='Bileşkede içteki fonksiyonu yazdığın sırayla değil, parantezin içinden başlayarak uygula.')

# ================= 02 kolay · ters fonksiyon (şekilsiz) =================
f2=lambda x:2*x-6; fi2=lambda y:Fr(y+6,2)
v=fi2(8)+f2(8); assert (fi2(8),f2(8),v)==(7,10,17)
e=[Fr(8-6,2)+f2(8), 2*8+6+f2(8), Fr(8,2)+6+f2(8), fi2(8)-f2(8)]
uniq(v,e)
q('0002',tipId='fn-ters',tip='Ters fonksiyon ve bileşkenin tersi',z='kolay',alt='Ters Fonksiyon Değeri',kaz='Birinci dereceden bir fonksiyonun tersini bulup ters ve kendi değerini birlikte hesaplar.',kalip='düz',
 kart='K-AFNK-02 (doğrusal fonksiyonun tersi) · f(x) = 2x − 6; f⁻¹(8) + f(8)',
 metin='Gerçel sayılar kümesi üzerinde f(x) = 2x − 6 biçiminde tanımlanan f fonksiyonu için f⁻¹ fonksiyonu f’nin tersidir.\nBuna göre f⁻¹(8) + f(8) toplamı kaçtır?',
 dogru=v,yan=[(e[0],'Tersi bulurken işaret hatası yapıp f⁻¹(x) = (x − 6)/2 almış: f⁻¹(8) = 1.','islem'),(e[1],'Tersi f⁻¹(x) = 2x + 6 sanmış: x ile y’nin yerini değiştirip işlemleri tersine çevirmemiş.','bilgi'),(e[2],'Tersi f⁻¹(x) = x/2 + 6 yazmış; 6’yı 2’ye bölmeyi unutmuş.','islem'),(e[3],'İki değeri toplamak yerine f⁻¹(8) − f(8) farkını almış.','dikkat')],
 istenen='f⁻¹(8) + f(8) toplamı.',ip=['y = 2x − 6 eşitliğinde x’i y cinsinden yaz; f⁻¹(8) için bulduğun ifadede 8’i yerine koy.'],bilgi=[TER],
 ad=[A('Tersi bul','y = 2x − 6 denkleminde x yalnız bırakılıp x ile y’nin yeri değiştirilir.','x = (y + 6)/2 → f⁻¹(x) = (x + 6)/2'),A('f⁻¹(8)','Ters kuralda x yerine 8 yazılır.','(8 + 6)/2 = 7'),A('f(8)','Kuralda x yerine 8 yazılır.','2 × 8 − 6 = 10'),A('Topla','İki değer toplanır.','7 + 10 = 17')],
 puf='f⁻¹(8) = a ise f(a) = 8 olmalıdır; bulduğun a’yı f’de deneyerek kontrol et.')

# ================= 03 kolay · grafik dönüşümü =================
V3=[(-3,1),(-1,3),(1,-1),(3,2)]; assert all(isinstance(x,int) for p in V3 for x in p)
g3=lambda x:pl(V3,x-1)+2
v=g3(0)+g3(2)
e=[ pl(V3,0+1)+2+pl(V3,2+1)+2, pl(V3,-1)-2+pl(V3,1)-2, pl(V3,-1)+pl(V3,1), g3(0)-g3(2)]
uniq(v,e)
sx=0.62
SK=fig(graf(-3,3,-2,4,sx,sx,egri(V3,sx,sx,MAVI)+f'\n\\node[{MAVI},font=\\small\\bfseries,fill=white,inner sep=1pt] at ({2.0*sx},{3.5*sx}) {{$y=f(x)$}};',ylab='y'))
q('0003',tipId='fn-donusum',tip='Grafik dönüşümleri',z='kolay',alt='Grafikten Öteleme',kaz='Grafiği verilen fonksiyonun yatay ve düşey ötelenmesiyle oluşan yeni fonksiyonun değerlerini grafikten okuyarak hesaplar.',kalip='grafik',
 kart='K-AFNK-03 (kırık çizgi, g(x) = f(x − 1) + 2) · köşeler (−3, 1), (−1, 3), (1, −1), (3, 2)',
 metin='Şekilde [−3, 3] aralığında tanımlı f fonksiyonunun grafiği verilmiştir; grafik, uçları kılavuz çizgilerinin kesişiminde olan doğru parçalarından oluşmaktadır.\ng(x) = f(x − 1) + 2 biçiminde tanımlanan g fonksiyonu için g(0) + g(2) toplamı kaçtır?',
 dogru=v,yan=[(e[0],'Öteleme yönünü ters almış: g(x) = f(x + 1) + 2 kullanıp f(1) ve f(3) değerlerini okumuş.','bilgi'),(e[1],'Düşey ötelemeyi ters almış: f(x − 1) − 2 kullanmış.','bilgi'),(e[2],'Dönüşümün +2 kısmını hiç uygulamamış: f(−1) + f(1) toplamını yazmış.','dikkat'),(e[3],'İki değeri toplamak yerine g(0) − g(2) farkını almış.','dikkat')],
 istenen='g(0) + g(2) toplamı.',ip=['g(0) ve g(2) için f’nin hangi noktalardaki değerlerine ihtiyaç olduğunu belirle, sonra bu değerleri grafikten oku.'],bilgi=[DON],sekil=SK,
 ad=[A('g(0)','x = 0 için f(−1) okunur.',f'g(0) = f(−1) + 2 = {S(pl(V3,-1))} + 2 = {S(g3(0))}'),A('g(2)','x = 2 için f(1) okunur.',f'g(2) = f(1) + 2 = {S(pl(V3,1))} + 2 = {S(g3(2))}'),A('Topla','İki değer toplanır.',f'{S(g3(0))} + {S(g3(2))} = {S(v)}')],
 puf='g’nin tanım aralığı f’ninkinin sağa kaymış hâlidir; okuyacağın noktaların f’nin tanım aralığında kaldığını kontrol et.')

# ================= 04 kolay · makine, bileşke =================
f4=lambda x:2*x-1; g4=lambda x:x*x+1
v=g4(f4(3)); e=[f4(g4(3)),f4(3),g4(3),f4(3)+g4(3)]
assert (v,e)==(26,[19,5,10,15]); uniq(v,e)
SK=fig(makine('3',[('f','2x-1'),('g','x^2+1')],'?'))
q('0004',tipId='fn-bilesik',tip='Bileşke fonksiyon değeri',z='kolay',alt='Makine Şeması',kaz='Art arda bağlı iki makinenin kurallarını sırayla uygulayarak çıkış değerini hesaplar.',kalip='şekilli',
 kart='K-AFNK-01 (makine şeması) · giriş 3; önce 2x − 1, sonra x² + 1',
 metin='Şekildeki sistemde giriş kutusuna yazılan sayı önce f makinesine, ardından g makinesine girmekte; her makine kendisine giren sayıya üzerinde yazılı kuralı uygulayıp sonucu bir sonraki aşamaya iletmektedir.\nBuna göre çıkış kutusuna yazılması gereken sayı kaçtır?',
 dogru=v,yan=[(e[0],'Makinelerin sırasını ters uygulamış: önce g, sonra f.','dikkat'),(e[1],'Yalnız f makinesinin çıkışını yazmış.','dikkat'),(e[2],'Yalnız g makinesini girişe uygulamış.','dikkat'),(e[3],'Bileşke yerine iki makinenin girişe ayrı ayrı verdiği çıkışları toplamış.','islem')],
 istenen='Çıkış kutusuna yazılması gereken sayı.',ip=['Oklar girişten çıkışa doğru izlenir; ilk makinenin çıkışı ikinci makinenin girişidir.'],bilgi=[BIL],sekil=SK,
 ad=[A('Sırayı oku','Oklar giriş kutusundan f makinesine, oradan g makinesine gider.','g(f(3))'),A('f makinesi','Giriş f kuralından geçer.','f(3) = 2 × 3 − 1 = 5'),A('g makinesi','f’nin çıkışı g’ye girer.','g(5) = 5² + 1 = 26')],
 puf='Makine şemasında soldaki makine önce çalışır; bileşke yazarken bu sıra sağdan sola okunur.')

# ================= 05 orta · ok şeması, eksik ok, ters =================
A5,B5,C5=[1,2,3,4],[5,6,7,8],[10,20,30,40]
f5={1:7,2:5,3:8,4:6}; g5={5:30,6:40,7:10,8:20}
assert sorted(f5.values())==B5 and sorted(g5.values())==C5
gof=lambda a:g5[f5[a]]; gofi=lambda c:[a for a in A5 if gof(a)==c][0]
gi=lambda c:[b for b in B5 if g5[b]==c][0]; fi=lambda b:[a for a in A5 if f5[a]==b][0]
v=gof(1)+gofi(30); assert (gof(1),gofi(30),v)==(10,2,12)
e=[f5[1]+gofi(30), gof(1)+gi(30), gof(1)*gofi(30), gof(1)-gofi(30)]
uniq(v,e)
gc=[(B5.index(b),C5.index(c)) for b,c in g5.items() if b!=7]
SK=fig(ok3(A5,B5,C5,[(A5.index(a),B5.index(b)) for a,b in f5.items()],gc))
q('0005',tipId='fn-ters',tip='Ters fonksiyon ve bileşkenin tersi',z='orta',alt='Eksik Okla Ters',kaz='Birebir ve örten iki fonksiyonun ok şemasında eksik okun yerini bularak bileşke ve bileşkenin tersi değerlerini hesaplar.',kalip='şekilli',
 kart='K-AFNK-02 (g’de bir ok eksik) · (g ∘ f)(1) + (g ∘ f)⁻¹(30)',
 metin='A, B ve C kümeleri arasında tanımlı f: A → B ve g: B → C fonksiyonları birebir ve örtendir. Şekilde f fonksiyonunun bütün eşlemeleri, g fonksiyonunun ise yalnızca üç eşlemesi oklarla gösterilmiştir.\nBuna göre (g ∘ f)(1) + (g ∘ f)⁻¹(30) toplamı kaçtır?',
 dogru=v,yan=[(e[0],f'Birinci terimde yalnız f(1) = {f5[1]} değerini bulup g adımını uygulamamış.','dikkat'),(e[1],f'İkinci terimde (g ∘ f)⁻¹(30) yerine yalnız g⁻¹(30) = {gi(30)} değerini yazmış; f⁻¹ adımını atlamış.','bilgi'),(e[2],'İki değeri toplamak yerine çarpmış.','dikkat'),(e[3],'İki değeri toplamak yerine farkını almış.','dikkat')],
 istenen='(g ∘ f)(1) + (g ∘ f)⁻¹(30) toplamı.',ip=['g’nin oku eksik olan elemanın, C’de ok almayan elemanla eşleşmesi gerektiğini düşün.'],bilgi=[TER],sekil=SK,
 ad=[A('Eksik oku bul','B’de oku çizilmeyen eleman 7’dir; C’de ok gelmeyen tek eleman 10’dur.','g(7) = 10'),A('(g ∘ f)(1)','f(1) = 7 olduğundan g(7) bulunur.',f'f(1) = 7 → g(7) = 10'),A('Bileşkenin tersi','30’a ok gönderen B elemanı, sonra o elemana ok gönderen A elemanı bulunur.',f'g⁻¹(30) = {gi(30)} → f⁻¹({gi(30)}) = {fi(gi(30))}'),A('Topla','İki değer toplanır.',f'10 + {gofi(30)} = {v}')],
 puf='Birebir ve örten fonksiyonda her elemana tam bir ok gelir; ok almayan tek elemanı bulmak eksik oku verir.')

# ================= 06 orta · öncüllü, tablo =================
f6={1:3,2:1,3:3,4:2}; g6={1:4,2:2,3:1,4:3}
inj=lambda d:len(set(d.values()))==len(d)
gi6=lambda y:[a for a in g6 if g6[a]==y][0]
I6=inj(f6); II6=inj(g6) and gi6(1)==3; III6=(f6[g6[1]]==g6[f6[1]])
assert (I6,II6,III6)==(False,True,False)
SIK6=['Yalnız I','Yalnız II','I ve II','I ve III','II ve III']
SK=tablo_svg(['x','1','2','3','4'],[['f(x)']+[str(f6[i]) for i in range(1,5)],['g(x)']+[str(g6[i]) for i in range(1,5)]])
q('0006',tipId='fn-tanim',tip='Birebir, örten ve tanım kümeleri',z='orta',alt='Tabloyla Fonksiyon Özellikleri',kaz='Tabloyla verilen fonksiyonların birebirliğini, ters değerini ve bileşke eşitliğini sınar.',kalip='öncüllü',
 kart='K-AFNK-06 (tablo, öncüllü) · A = {1, 2, 3, 4}; f birebir değil, g birebir ve örten',
 metin='A = {1, 2, 3, 4} kümesi üzerinde tanımlı f ve g fonksiyonlarının değerleri aşağıdaki tabloda verilmiştir.\nI. f fonksiyonu birebirdir.\nII. g fonksiyonu birebir ve örten olup g⁻¹(1) = 3’tür.\nIII. (f ∘ g)(1) = (g ∘ f)(1) eşitliği sağlanır.\nBu ifadelerden hangileri doğrudur?',
 dogru='Yalnız II',sira=SIK6,yan=[('Yalnız I','I’i doğru sanıp f(1) = f(3) = 3 eşitliğini görmemiş; g⁻¹(1) = 3’ü de bulamayıp II’yi, bileşkeleri hesaplamayıp III’ü de yanlış saymış.','dikkat'),('I ve II','I’i doğru sanmış: f(1) = f(3) eşitliğini görmemiş.','dikkat'),('I ve III',f'f’yi birebir sanmış; III için (f ∘ g)(1) = {f6[g6[1]]} ile (g ∘ f)(1) = {g6[f6[1]]} değerlerinin eşit olmadığını görmemiş; g(3) = 1’i okuyamadığından II’yi de yanlış saymış.','islem'),('II ve III',f'III’ü doğru sanmış; (f ∘ g)(1) = {f6[g6[1]]} iken (g ∘ f)(1) = {g6[f6[1]]} olduğundan eşit değildir.','islem')],
 istenen='Doğru olan öncüllerin hangileri olduğu.',ip=['Her öncülü tablodan ayrı ayrı sına; birebirlik için aynı değeri alan iki farklı eleman var mı diye bak.'],bilgi=[TAN],sekil=SK,
 ad=[A('I’i sına','f(1) ve f(3) aynı değeri almaktadır.','f(1) = f(3) = 3 → birebir değil'),A('II’yi sına','g’nin değerleri 1, 2, 3, 4’ün hepsidir; g(3) = 1’dir.','birebir ve örten, g⁻¹(1) = 3'),A('III’ü sına','İki bileşke ayrı ayrı hesaplanır.',f'(f ∘ g)(1) = f(4) = {f6[g6[1]]} · (g ∘ f)(1) = g(3) = {g6[f6[1]]}'),A('Sonuç','Yalnız II doğrudur.','Yalnız II')],
 puf='Bileşke eşitliğini sınarken iki tarafı ayrı satırda, içten dışa hesapla.')

# ================= 07 orta · iki grafik, öteleme parametreleri =================
V7=[(-2,1),(0,3),(1,0),(3,2)]; sh=(3,-2)
W7=[(x+sh[0],y+sh[1]) for x,y in V7]
# g(x) = f(x + a) + b  → köşeler (x − a, y + b): a = −3, b = −2
a7,b7=-sh[0],sh[1]
assert all(pl(V7,x-sh[0])+sh[1]==Fr(y) for x,y in W7)
exp=lambda a,b:2*a+b
v=exp(a7,b7); e=[exp(-a7,b7),exp(a7,-b7),exp(-a7,-b7),exp(b7,a7)]
uniq(v,e)
sx=0.55
SK=fig(graf(-3,7,-3,4,sx,sx,egri(V7,sx,sx,MAVI)+'\n'+egri(W7,sx,sx,TUR)+f'\n\\node[{MAVI},font=\\small\\bfseries,fill=white,inner sep=1pt] at ({1.3*sx},{3.4*sx}) {{$y=f(x)$}};\n\\node[{TUR},font=\\small\\bfseries,fill=white,inner sep=1pt] at ({4.6*sx},{-2.6*sx}) {{$y=g(x)$}};',xs=1))
q('0007',tipId='fn-donusum',tip='Grafik dönüşümleri',z='orta',alt='İki Grafikten Öteleme',kaz='Aynı koordinat düzlemindeki iki grafiğin köşelerini eşleyerek g(x) = f(x + a) + b biçimindeki ötelemenin a ve b değerlerini bulur.',kalip='grafik',
 kart='K-AFNK-03 (iki kırık çizgi) · g(x) = f(x − 3) − 2; ifade 2a + b',
 metin='Dik koordinat düzleminde, uçları kılavuz çizgilerinin kesişiminde olan doğru parçalarından oluşan y = f(x) ve y = g(x) fonksiyonlarının grafikleri şekilde verilmiştir. g fonksiyonunun grafiği, f fonksiyonunun grafiğinin ötelenmesiyle elde edilmiştir ve a, b gerçel sayılar olmak üzere her x için g(x) = f(x + a) + b eşitliği sağlanmaktadır.\nBuna göre 2a + b ifadesinin değeri kaçtır?',
 dogru=v,yan=[(e[0],f'Yatay ötelemenin yönünü ters almış: a = {-a7} bulup 2·{-a7} + ({b7}) hesaplamış.','bilgi'),(e[1],f'Düşey ötelemenin yönünü ters almış: b = {-b7} bulmuş.','bilgi'),(e[2],'Hem yatay hem düşey ötelemenin yönünü ters almış: a = 3, b = 2.','bilgi'),(e[3],f'a ile b’nin yerini karıştırıp a = {b7}, b = {a7} alarak 2a + b hesaplamış.','dikkat')],
 istenen='2a + b ifadesinin değeri.',ip=['f’nin bir köşesinin g’de hangi noktaya taşındığına bak; x ve y yönündeki kaymayı ayrı ayrı yaz.'],bilgi=[DON],sekil=SK,
 ad=[A('Köşeleri eşle','f’nin (0, 3) köşesi g’nin (3, 1) köşesine karşılık gelir.','(0, 3) → (3, 1)'),A('Kaymayı bul','Grafik 3 birim sağa, 2 birim aşağı ötelenmiştir.','x: +3 · y: −2'),A('a ve b','Sağa 3 öteleme x yerine x − 3 yazmaktır, bu nedenle a = −3; aşağı 2 öteleme b = −2’dir.','a = −3, b = −2'),A('İfadeyi hesapla','a ve b yerine yazılır.',f'2 × (−3) + (−2) = {S(v)}')],
 puf='g(x) = f(x + a) + b ise g’nin grafiği f’ninkinin a birim SOLA, b birim YUKARI ötelenmişidir; a’nın işareti kaymanın ters yönündedir.')

# ================= 08 orta · tek fonksiyon, yarım grafik =================
V8=[(0,0),(1,3),(2,1),(3,-2),(4,-1)]
f8=lambda x:pl(V8,x) if x>=0 else -pl(V8,-x)
v=f8(-1)+f8(-3)-f8(4); assert v==-3+2+1==0
# daha anlamlı ifade: f(−1) + f(−3) + 2·f(−2)
v=f8(-1)+f8(-3)+2*f8(-2); assert v==-3+2-2==-3
e=[f8(1)+f8(3)+2*f8(2), f8(-1)+f8(-3)+f8(-2), f8(-1)+f8(3)+2*f8(-2), f8(-1)+f8(-3)+2*f8(2)]
uniq(v,e)
sx=0.62
SK=fig(graf(-1,4,-3,3,sx,sx,egri(V8,sx,sx,MAVI)+f'\n\\node[{MAVI},font=\\small\\bfseries,fill=white,inner sep=1pt] at ({2.55*sx},{3*sx+0.1}) {{$y=f(x)$}};'))
q('0008',tipId='fn-ozellik',tip='Tek, çift ve periyodik fonksiyonlar',z='orta',alt='Tek Fonksiyonun Grafiği',kaz='Tek fonksiyonun [0, 4] aralığındaki grafiğinden negatif değerlerdeki fonksiyon değerlerini belirleyerek ifadeyi hesaplar.',kalip='grafik',
 kart='K-AFNK-04 (yarım grafik, tek fonksiyon) · köşeler (0, 0), (1, 3), (2, 1), (3, −2), (4, −1)',
 metin='[−4, 4] aralığında tanımlı f fonksiyonu tek fonksiyondur. f fonksiyonunun [0, 4] aralığındaki grafiği, uçları kılavuz çizgilerinin kesişiminde olan doğru parçaları olarak şekilde verilmiştir.\nBuna göre f(−1) + f(−3) + 2·f(−2) ifadesinin değeri kaçtır?',
 dogru=v,yan=[(e[0],'Tek fonksiyonun işaret değiştirdiğini unutmuş: f(−x) yerine f(x) değerlerini kullanmış.','bilgi'),(e[1],'2 çarpanını yalnız f(−2) için değil de atlayıp f(−2) değerini bir kez almış.','dikkat'),(e[2],f'f(−3) yerine f(3) = {S(f8(3))} değerini yazmış; bir terimde işareti değiştirmemiş.','dikkat'),(e[3],f'f(−2) yerine f(2) = {S(f8(2))} almış; yalnız bir terimde işareti değiştirmemiş.','dikkat')],
 istenen='f(−1) + f(−3) + 2·f(−2) ifadesinin değeri.',ip=['Tek fonksiyonda f(−x) ile f(x) arasındaki ilişkiyi kullanarak negatif girişleri grafiğin bilinen kısmına taşı.'],bilgi=[OZE],sekil=SK,
 ad=[A('Tek fonksiyon kuralı','f tek olduğundan f(−x) = −f(x) yazılır.','f(−x) = −f(x)'),A('Değerleri oku','Grafikten f(1), f(2), f(3) okunur.',f'f(1) = {S(f8(1))}, f(2) = {S(f8(2))}, f(3) = {S(f8(3))}'),A('Negatif girişler','Her değerin işareti değiştirilir.',f'f(−1) = {S(f8(-1))}, f(−2) = {S(f8(-2))}, f(−3) = {S(f8(-3))}'),A('İfadeyi hesapla','Değerler yerine yazılır.',f'{S(f8(-1))} + {S(f8(-3))} + 2 × ({S(f8(-2))}) = {S(v)}')],
 puf='Tek fonksiyonun grafiği orijine göre simetriktir; bilinen yarıyı orijin etrafında 180° döndürürsen diğer yarıyı elde edersin.')

# ================= 09 orta · parçalı fonksiyon, tablo =================
def f9(x,hata=None):
    x=Fr(x)
    if x<0: return 2*x+9
    if x<4: return x*x-1
    return 12-2*x
v=f9(f9(-2))+f9(f9(3)); assert (f9(-2),f9(f9(-2)),f9(3),f9(f9(3)))==(5,2,8,-4) and v==-2
# hata 1: f(−2)'yi ikinci kuralla (aralık yanlış) hesaplamış: f(−2)=3 → f(3)=8
e1=f9(f9(3))+(f9(f9(3))*0)+f9(3)  # 8 + (−4)
e1=Fr(8)+f9(f9(3)); e1=f9(3)+f9(f9(3))   # ilk terim yerine f(−2) değil f(3)=8 alınmış: 8 + (−4)
# hata 2: iç değeri yeniden aralığa koymadan hesaplamış: f(−2)=5 ve f(3)=8 toplamı
e2=f9(-2)+f9(3)
# hata 3: ikinci terimde f(8) için ikinci kuralı kullanmış: 8²−1 = 63 → 5? birinci terim doğru (2)
e3=f9(f9(-2))+(f9(3)**2-1)
# hata 4: yalnız birinci iç içe terim
e4=f9(f9(-2))
e=[e1,e2,e3,e4]; uniq(v,e)
SK=tablo_svg(['x aralığı','f(x)'],[['x < 0','2x + 9'],['0 ≤ x < 4','x² − 1'],['x ≥ 4','12 − 2x']])
q('0009',tipId='fn-parcali',tip='Parçalı fonksiyon değeri',z='orta',alt='İç İçe Parçalı Değer',kaz='Üç aralıkla tanımlı parçalı fonksiyonda iç içe değerleri aralıklara yerleştirerek hesaplar.',kalip='tablo',
 kart='K-AFNK-05 (üç parçalı, tablo) · f(f(−2)) + f(f(3))',
 metin='Gerçel sayılar kümesi üzerinde tanımlı f fonksiyonunun kuralı, aralıklara göre aşağıdaki tabloda verilmiştir.\nBuna göre f(f(−2)) + f(f(3)) toplamı kaçtır?',
 dogru=v,yan=[(e[0],f'Birinci terim yerine f(3) = {S(f9(3))} değerini almış: {S(f9(3))} + ({S(f9(f(3)) if False else f9(f9(3)))}).','dikkat'),(e[1],f'İç içe değeri hesaplamayıp yalnız iç değerleri toplamış: f(−2) + f(3) = {S(f9(-2))} + {S(f9(3))}.','islem'),(e[2],f'İkinci terimde f(8) için de ikinci kuralı kullanmış: 8² − 1 = 63 yerine 12 − 16 = −4 alınmalıydı; sonuç {S(e3)}.','dikkat'),(e[3],f'Yalnız birinci terimi, yani f(f(−2)) = {S(f9(f9(-2)))} değerini yazmış.','dikkat')],
 istenen='f(f(−2)) + f(f(3)) toplamı.',ip=['İç değeri hesapladıktan sonra çıkan sayının hangi aralığa düştüğüne yeniden bak.'],bilgi=[PAR],sekil=SK,
 ad=[A('f(−2)','−2 < 0 olduğundan birinci kural kullanılır.','f(−2) = 2 × (−2) + 9 = 5'),A('f(f(−2))','5 ≥ 4 olduğundan üçüncü kural kullanılır.','f(5) = 12 − 10 = 2'),A('f(3)','0 ≤ 3 < 4 olduğundan ikinci kural kullanılır.','f(3) = 3² − 1 = 8'),A('f(f(3))','8 ≥ 4 olduğundan üçüncü kural kullanılır.','f(8) = 12 − 16 = −4'),A('Topla','İki değer toplanır.','2 + (−4) = −2')],
 puf='Her adımda çıkan sayıyı tablodaki aralıklarla yeniden karşılaştır; kural değişebilir.')

# ================= 10 orta · f(x − 2) = 3x + 1, değişken dönüşümü =================
fk=lambda y:3*y+7            # f(x − 2) = 3x + 1 → f(y) = 3(y + 2) + 1
assert all(fk(x-2)==3*x+1 for x in range(-5,6))
fki=lambda y:Fr(y-7,3)
v=fk(fk(1))+fki(10); assert (fk(1),fk(10),fki(10),v)==(10,37,1,38)
fa=lambda y:3*y+1; fai=lambda y:Fr(y-1,3)       # öteleme yapmadan f(x) = 3x + 1
fb=lambda y:3*(y-2)+1; fbi=lambda y:Fr(y-1,3)+2  # yönü ters
e=[fa(fa(1))+fai(10), fb(fb(1))+fbi(10), fk(fk(1)), fk(fk(1))+(10-7)]
uniq(v,e)
q('0010',tipId='fn-fonkdenk',tip='Fonksiyonel denklem',z='orta',alt='Değişken Dönüşümü',kaz='f(x − a) biçiminde verilen eşitlikten f’nin kuralını bulup değer ve ters değer hesaplar.',kalip='düz',
 kart='K-AFNK-07 (f(x − 2) = 3x + 1) · f(f(1)) + f⁻¹(10)',
 metin='Gerçel sayılar kümesi üzerinde tanımlı ve tersi bulunan bir f fonksiyonu, her x gerçel sayısı için\nf(x − 2) = 3x + 1\neşitliğini sağlamaktadır.\nBuna göre f(f(1)) + f⁻¹(10) toplamı kaçtır?',
 dogru=v,yan=[(e[0],'x − 2 yerine x yazmadan f(x) = 3x + 1 almış: f(f(1)) = 13, f⁻¹(10) = 3.','bilgi'),(e[1],'Değişken dönüşümünü ters yapıp f(x) = 3(x − 2) + 1 bulmuş.','bilgi'),(e[2],'Toplamdaki f⁻¹(10) terimini yazmamış, yalnız f(f(1)) = 37 değerini bulmuş.','dikkat'),(e[3],'f⁻¹(10) için 3a + 7 = 10 denkleminde 3’e bölmeyi unutup a = 10 − 7 = 3 almış: 37 + 3.','islem')],
 istenen='f(f(1)) + f⁻¹(10) toplamı.',ip=['f’nin kuralını bulmak için eşitliğin iki yanını parantezin içindeki ifade cinsinden okuyabileceğin bir değişken seç.'],bilgi=[FDN],
 ad=[A('Kuralı bul','x − 2 = t denirse x = t + 2 olur.','f(t) = 3(t + 2) + 1 = 3t + 7'),A('f(1) ve f(10)','Kuralda sırasıyla yazılır.','f(1) = 10 · f(10) = 37'),A('Ters değer','f(a) = 10 denkleminden a bulunur.','3a + 7 = 10 → a = 1'),A('Topla','f(f(1)) ile f⁻¹(10) toplanır.','37 + 1 = 38')],
 puf='Kuralı bulduktan sonra f(x − 2) = 3x + 1 eşitliğinde bir sayı deneyerek kuralı kontrol et.')

# ================= 11 orta · öncüllü ok şeması =================
A11,B11,C11=[1,2,3,4],['m','n','p'],[10,20,30,40]
f11={1:'n',2:'m',3:'n',4:'p'}; g11={'m':20,'n':40,'p':10}
inj=lambda d:len(set(d.values()))==len(d)
I11=inj(g11); II11=inj(f11); III11=(g11[f11[1]]==g11[f11[3]])
assert (I11,II11,III11)==(True,False,True)
SIK11=['Yalnız I','Yalnız II','I ve III','II ve III','I, II ve III']
SK=fig(ok3(A11,B11,C11,[(A11.index(a),B11.index(b)) for a,b in f11.items()],[(B11.index(b),C11.index(c)) for b,c in g11.items()]))
q('0011',tipId='fn-tanim',tip='Birebir, örten ve tanım kümeleri',z='orta',alt='Ok Şemasıyla Özellikler',kaz='Ok şemasıyla verilen iki fonksiyonun birebirliğini ve bileşke değerlerinin eşitliğini sınar.',kalip='öncüllü',
 kart='K-AFNK-06 (ok şeması, öncüllü) · f birebir değil, g birebir; (g ∘ f)(1) = (g ∘ f)(3)',
 metin='Şekilde, A = {1, 2, 3, 4}, B = {m, n, p} ve C = {10, 20, 30, 40} kümeleri arasında tanımlı f: A → B ve g: B → C fonksiyonları ok şemasıyla gösterilmiştir.\nI. g fonksiyonu birebirdir.\nII. f fonksiyonu birebirdir.\nIII. (g ∘ f)(1) = (g ∘ f)(3) eşitliği sağlanır.\nBu ifadelerden hangileri doğrudur?',
 dogru='I ve III',sira=SIK11,yan=[('Yalnız I','III’ü sınamamış; f(1) = f(3) = n olduğundan (g ∘ f)(1) = (g ∘ f)(3) olduğunu görmemiş.','dikkat'),('Yalnız II','I’i doğru bulmayıp II’yi doğru sanmış: n’ye iki ok gelmesi f’nin birebir olmadığını gösterir.','bilgi'),('II ve III','f’nin birebir olduğunu sanıp II’yi doğru saymış; g’nin birebirliğini sınamadığından I’i de doğru saymamış.','bilgi'),('I, II ve III','Üç öncülü de doğru bulmuş; f’de n’ye iki ok geldiğini fark etmemiş.','dikkat')],
 istenen='Doğru olan öncüllerin hangileri olduğu.',ip=['Birebirlik için B’nin ya da C’nin bir elemanına birden fazla ok gelip gelmediğine bak; III için iki girişin yolunu ayrı ayrı izle.'],bilgi=[TAN],sekil=SK,
 ad=[A('I’i sına','g’nin okları m, n, p’yi farklı elemanlara götürür.','g birebir'),A('II’yi sına','n’ye 1 ve 3’ten iki ok gelir.','f birebir değil'),A('III’ü sına','Her iki girişin yolu izlenir.','1 → n → 40 · 3 → n → 40'),A('Sonuç','I ve III doğrudur.','I ve III')],
 puf='Her öncülü ayrı ayrı, şemadaki okları izleyerek sına; tek bir öncüle bakıp diğerlerini tahminle bırakma.')

# ================= 12 orta · makine, parametre =================
f12=lambda x,a:3*x+a; g12=lambda x:x*x-4
sol=[a for a in range(-20,21) if g12(f12(2,a))==5]; assert sol==[-9,-3]
v=sum(sol)
e=[-3,-9,5,0]
assert g12(2)==0 and 0==5-5   # f(g(2)) = a = 5 olur
uniq(v,e)
SK=fig(makine('2',[('f','3x+a'),('g','x^2-4')],'5'))
q('0012',tipId='fn-bilesik',tip='Bileşke fonksiyon değeri',z='orta',alt='Makinede Parametre',kaz='Makine şemasıyla verilen bileşkede çıkış değerinden parametreyi ikinci dereceden denklemle bulur.',kalip='şekilli',
 kart='K-AFNK-01 (makine, parametreli) · f(x) = 3x + a, g(x) = x² − 4; giriş 2, çıkış 5',
 metin='Şekildeki sistemde giriş kutusuna 2 yazıldığında sayı önce f makinesine, sonra g makinesine girmekte ve çıkış kutusunda 5 değeri okunmaktadır. f makinesinin kuralındaki a bir gerçel sayıdır.\nBuna göre a’nın alabileceği değerlerin toplamı kaçtır?',
 dogru=v,yan=[(e[0],'(6 + a)² = 9 denkleminin yalnız 6 + a = 3 çözümünü alıp a = −3 bulmuş.','dikkat'),(e[1],'(6 + a)² = 9 denkleminin yalnız 6 + a = −3 çözümünü alıp a = −9 bulmuş.','dikkat'),(e[2],'Makinelerin sırasını ters uygulamış: g(2) = 0 olup f(0) = a = 5 bulmuş.','dikkat'),(e[3],'6 + a = 3 ve 6 + a = −3 köklerinin toplamını 0 bulup 6’yı hesaba katmamış.','islem')],
 istenen='a’nın alabileceği değerlerin toplamı.',ip=['f makinesinin çıkışı g makinesinin girişidir; bu sayıyı a cinsinden yazıp çıkışa eşitle.'],bilgi=[BIL],sekil=SK,
 ad=[A('f makinesi','f’ye giren 2 için çıkış a cinsinden yazılır.','f(2) = 6 + a'),A('g makinesi','Bu sayı g’ye girer ve çıkış 5 olur.','(6 + a)² − 4 = 5'),A('Denklemi çöz','(6 + a)² = 9 olduğundan iki durum vardır.','6 + a = 3 ya da 6 + a = −3'),A('a değerleri','İki durumdan a bulunur.','a = −3 ya da a = −9'),A('Topla','Değerler toplanır.','−3 + (−9) = −12')],
 puf='Kare alan bir makineden sonra çıkış verilmişse iç değer için iki durum olabilir; ikisini de sına.')

# ================= 13 orta · makine, giriş bulma =================
g13=lambda x:3*x+4; f13=lambda x:3*x-5
xs=[x for x in range(-30,31) if f13(g13(x))==25]; assert xs==[2]
v=2
e=[ [x for x in range(-30,31) if g13(f13(x))==25][0], Fr(25+5,3), Fr(25-4,3), Fr(25+5,3)-4 ]
assert e==[4,10,Fr(7),6]; uniq(v,e)
SK=fig(makine('x',[('g','3x+4'),('f','3x-5')],'25'))
q('0013',tipId='fn-ters',tip='Ters fonksiyon ve bileşkenin tersi',z='orta',alt='Makinede Giriş Bulma',kaz='Art arda bağlı iki makinenin çıkış değerinden girişi, makinelerin tersini ters sırayla uygulayarak bulur.',kalip='şekilli',
 kart='K-AFNK-02 (makine, bileşkenin tersi) · g(x) = 3x + 4, sonra f(x) = 3x − 5; çıkış 25',
 metin='Şekildeki sistemde giriş kutusuna yazılan x sayısı önce g makinesinden, sonra f makinesinden geçmekte ve çıkış kutusunda 25 değeri okunmaktadır.\nBuna göre giriş kutusuna yazılan x sayısı kaçtır?',
 dogru=v,yan=[(e[0],'Makinelerin sırasını ters alıp (g ∘ f)(x) = 25 denklemini çözmüş: 9x − 11 = 25.','dikkat'),(e[1],'Yalnız f makinesini geri alıp (25 + 5)/3 = 10 değerini giriş sanmış.','dikkat'),(e[2],'Geri almaya g makinesinden başlayıp (25 − 4)/3 = 7 değerini bulmuş ve devam etmemiş.','dikkat'),(e[3],'f makinesini geri alıp g’nin yaptığı 4’ü çıkarmış, fakat 3’e bölmeyi unutmuş: 10 − 4 = 6.','islem')],
 istenen='Giriş kutusuna yazılan x sayısı.',ip=['Çıkıştan başlayıp her makinenin yaptığı işlemin tersini, makinelerin sırasının tersiyle uygula.'],bilgi=[TER],sekil=SK,
 ad=[A('f makinesini geri al','f’nin tersi: 5 ekle, 3’e böl.','(25 + 5)/3 = 10'),A('g makinesini geri al','g’nin tersi: 4 çıkar, 3’e böl.','(10 − 4)/3 = 2'),A('Kontrol et','Girişten çıkışa doğru hesaplanır.','g(2) = 10 → f(10) = 25')],
 puf='Bulduğun girişi şemada baştan sona uygulayıp çıkışın 25 olduğunu doğrula.')

# ================= 14 orta · öncüllü fonksiyonel denklem (şekilsiz) =================
I14=True; II14=True; III14=False
# f(x+y)=f(x)+f(y), f(1)=3: f(0)=0, f(1/2)=3/2, f(2)=6 ama f(2²)=f(4)=12 ≠ 6² = 36
assert 2*Fr(3,2)==3 and 4*3==12 and (2*3)**2==36 and 12!=36
SIK14=['Yalnız I','Yalnız III','I ve II','II ve III','I, II ve III']
q('0014',tipId='fn-fonkdenk',tip='Fonksiyonel denklem',z='orta',alt='Toplamsal Fonksiyon',kaz='Her x ve y için f(x + y) = f(x) + f(y) eşitliğini sağlayan fonksiyonun özel değerlerini ve çarpımsal ilişkisini sınar.',kalip='öncüllü',
 kart='K-AFNK-07 (toplamsal fonksiyon, öncüllü) · f(1) = 3; f(0) = 0, f(1/2) = 3/2, f(x²) ≠ (f(x))²',
 metin='Gerçel sayılar kümesi üzerinde tanımlı bir f fonksiyonu, her x ve y gerçel sayısı için\nf(x + y) = f(x) + f(y)\neşitliğini sağlamakta ve f(1) = 3 olmaktadır.\nI. f(0) = 0’dır.\nII. f(1/2) = 3/2’dir.\nIII. Her x gerçel sayısı için f(x²) = (f(x))² eşitliği sağlanır.\nBu ifadelerden hangileri doğrudur?',
 dogru='I ve II',sira=SIK14,yan=[('Yalnız I','II’yi sınamamış: f(1/2) + f(1/2) = f(1) = 3 olduğundan f(1/2) = 3/2 bulunur.','dikkat'),('Yalnız III','III’ü doğru sanıp I ve II’yi sınamamış; x = 2 için f(4) = 12 iken (f(2))² = 36’dır.','bilgi'),('II ve III','I’i doğru bulmamış: x = y = 0 yazılırsa f(0) = 2f(0), yani f(0) = 0 olur.','islem'),('I, II ve III','III’ü doğru sanmış: f(x²) = (f(x))² eşitliği x = 2 için f(4) = 12 ≠ 36 nedeniyle sağlanmaz.','bilgi')],
 istenen='Doğru olan öncüllerin hangileri olduğu.',ip=['Verilen eşitlikte x ve y yerine uygun sayılar yazarak her öncülü ayrı ayrı sına.'],bilgi=[FDN],
 ad=[A('I’i sına','x = y = 0 yazılır.','f(0) = 2f(0) → f(0) = 0'),A('II’yi sına','x = y = 1/2 yazılır.','2f(1/2) = f(1) = 3 → f(1/2) = 3/2'),A('III’ü sına','x = 2 için iki taraf hesaplanır.','f(2) = 6, f(4) = 12 ve (f(2))² = 36'),A('Sonuç','I ve II doğru, III yanlıştır.','I ve II')],
 puf='Bir öncülün her x için doğru olduğunu göstermek zordur; tek bir x değeri çelişki verirse öncül yanlıştır.')

# ================= 15 zor · ok şeması, koşulla eksik oklar =================
A15,B15,C15=[1,2,3,4],['m','n','p','r'],[10,20,30,40]
f15={1:'n',2:'r',3:'m',4:'p'}; g15={'m':20,'n':40,'p':10,'r':30}
gof15=lambda a:g15[f15[a]]
assert gof15(2)==30 and sorted(f15.values())==sorted(B15) and sorted(g15.values())==C15
gofi15=lambda c:[a for a in A15 if gof15(a)==c][0]
v=gof15(4)+gofi15(20); assert (gof15(4),gofi15(20),v)==(10,3,13)
e=[30+gofi15(20), gof15(4), gof15(4)*gofi15(20), gof15(4)-gofi15(20)]
uniq(v,e)
fd=[(A15.index(a),B15.index(b)) for a,b in f15.items() if a!=4]; gd=[(B15.index(b),C15.index(c)) for b,c in g15.items() if b in ('m','n')]
SK=fig(ok3(A15,B15,C15,fd,gd))
q('0015',tipId='fn-ters',tip='Ters fonksiyon ve bileşkenin tersi',z='zor',alt='Koşulla Eksik Oklar',kaz='Birebir ve örten iki fonksiyonun eksik oklarını verilen bileşke koşuluyla tamamlayıp bileşke ve bileşkenin tersi değerlerini hesaplar.',kalip='şekilli',
 kart='K-AFNK-02 (iki fonksiyonda eksik oklar) · (g ∘ f)(2) = 30 koşulu; (g ∘ f)(4) + (g ∘ f)⁻¹(20)',
 metin='A, B ve C kümeleri arasında tanımlı f: A → B ve g: B → C fonksiyonları birebir ve örtendir. Şekilde f ve g fonksiyonlarının eşlemelerinden yalnızca bazıları oklarla gösterilmiştir. Ayrıca (g ∘ f)(2) = 30 olduğu bilinmektedir.\nBuna göre (g ∘ f)(4) + (g ∘ f)⁻¹(20) toplamı kaçtır?',
 dogru=v,yan=[(e[0],'g’nin eksik iki okunu ters yerleştirip g(p) = 30 almış: (g ∘ f)(4) = 30.','bilgi'),(e[1],'İkinci terimi toplama katmayıp yalnız (g ∘ f)(4) = 10 değerini yazmış.','dikkat'),(e[2],'İki değeri toplamak yerine çarpmış.','dikkat'),(e[3],'İki değeri toplamak yerine farkını almış.','dikkat')],
 istenen='(g ∘ f)(4) + (g ∘ f)⁻¹(20) toplamı.',ip=['Önce (g ∘ f)(2) = 30 koşulundan hangi B elemanının 30’a gittiğini bul; çizilmeyen okları birebir ve örtenlikten tamamla.'],bilgi=[TER],sekil=SK,
 ad=[A('g’nin eksik okları','(g ∘ f)(2) = 30 ve f(2) = r olduğundan g(r) = 30 olur; kalan eleman p, 10’a gider.','g(r) = 30 · g(p) = 10'),A('f’nin eksik oku','B’de ok almayan eleman p’dir.','f(4) = p'),A('Birinci terim','f(4) = p, sonra g(p) bulunur.','(g ∘ f)(4) = g(p) = 10'),A('İkinci terim','20’ye ok gönderen B elemanı m’dir, m’ye ok gönderen A elemanı 3’tür.','g⁻¹(20) = m → f⁻¹(m) = 3'),A('Topla','İki değer toplanır.','10 + 3 = 13')],
 puf='Bir koşul, eksik oklardan hangisinin hangi elemana gideceğini kesinleştirir; önce onu kullan.')

# ================= 16 zor · grafik, f(f(x)) = 5 =================
V16=[(0,2),(1,5),(2,1),(3,4),(4,0),(5,3),(6,6)]
def pre(V,u):
    r=set()
    for (x1,y1),(x2,y2) in zip(V,V[1:]):
        assert y1!=y2
        if min(y1,y2)<=u<=max(y1,y2): r.add(Fr(x1)+Fr(u-y1,y2-y1)*(x2-x1))
    return r
K16=5; us=sorted(pre(V16,K16)); assert us==[1,Fr(17,3)]
cn=[len(pre(V16,u)) for u in us]; assert cn==[3,1]
v=sum(cn); assert v==4
# teğet noktası (x = 2, f = 1) iki kez sayılırsa: 3 yerine 4
e=[len(us), cn[0], cn[1], v+1]
uniq(v,e)
sx=0.55
SK=fig(graf(0,6,0,6,sx,sx,egri(V16,sx,sx,MAVI)+f'\n\\node[{MAVI},font=\\small\\bfseries,fill=white,inner sep=1pt] at ({3.0*sx},{5.6*sx}) {{$y=f(x)$}};'))
q('0016',tipId='fn-grafikoku',tip='Grafikten iç içe fonksiyon denklemi',z='zor',alt='Grafikte f(f(x)) Çözüm Sayısı',kaz='Grafiği verilen fonksiyonda f(f(x)) = k denkleminin çözüm sayısını iki aşamada sayarak bulur.',kalip='grafik',
 kart='K-AFNK-08 (kırık çizgi, [0, 6]) · köşeler (0, 2), (1, 5), (2, 1), (3, 4), (4, 0), (5, 3), (6, 6); f(f(x)) = 5',
 metin='Şekilde [0, 6] aralığında tanımlı ve değer kümesi [0, 6] aralığının bir alt kümesi olan f fonksiyonunun grafiği verilmiştir; grafik, uçları kılavuz çizgilerinin kesişiminde olan doğru parçalarından oluşmaktadır.\nBuna göre f(f(x)) = 5 denkleminin kaç farklı gerçel sayı çözümü vardır?',
 dogru=v,yan=[(e[0],'Yalnız f(u) = 5 denkleminin çözüm sayısı olan 2’yi yazmış.','dikkat'),(e[1],'İç değerlerden yalnız u = 1 için f(x) = 1 denkleminin çözümlerini sayıp (3) bırakmış.','dikkat'),(e[2],'İç değerlerden yalnız büyük olanı için f(x) = u çözümünü sayıp (1) bırakmış.','dikkat'),(e[3],'x = 2 köşesinde f(x) = 1 değerini iki çözüm sanıp f(x) = 1 için 4 çözüm bulmuş.','dikkat')],
 istenen='f(f(x)) = 5 denkleminin farklı çözümlerinin sayısı.',ip=['Önce f(u) = 5 olan u değerlerini bul; sonra her u için f(x) = u eşitliğini sağlayan x sayısını ayrı ayrı say.'],bilgi=[GRO],sekil=SK,
 ad=[A('İç değerler','y = 5 doğrusunun grafiği kestiği noktalar bulunur.','u = 1 ve u = 17/3'),A('f(x) = 1 çözümleri','y = 1 doğrusu grafiği üç noktada keser; biri (2, 1) köşe noktasıdır.','3 çözüm'),A('f(x) = 17/3 çözümleri','17/3, 6’ya yakın bir değerdir; yalnız son doğru parçası bu değeri alır.','1 çözüm'),A('Toplam','Çözümler ayrı ayrı sayılır; farklı u değerleri farklı x verir.','3 + 1 = 4')],
 puf='Farklı u değerlerine ait x çözümleri hiçbir zaman çakışmaz; çünkü bir x için f(x) tek değerdir.')

# ================= 17 zor · sayı doğrusu, bileşkenin tanım kümesi =================
f17=lambda x:3*x-2
Df=lambda x:-3<=x<=2; Dg=lambda y:-5<y<=7
ints=range(-12,13)
dom=[x for x in ints if Df(x) and Dg(f17(x))]; assert dom==[0,1,2]
v=sum(dom); assert v==3
e_df=sum(x for x in ints if Dg(f17(x)))                          # Df'yi unutmuş
e_kes=sum(x for x in ints if Df(x) and Dg(x))                    # g'nin kümesini x'e uygulamış
e_kap=sum(x for x in ints if Df(x) and -5<=f17(x)<=7)            # −5 dahil
e_ac=sum(x for x in ints if -3<=x<2 and Dg(f17(x)))              # Df'nin 2 ucunu dışlamış
e=[e_df,e_kes,e_kap,e_ac]; assert e==[6,-3,2,1]; uniq(v,e)
def sd(y,a,b,aK,bK,renk,ad):
    o=[f'\\draw[-{{Stealth}},thick] (-6.4,{y}) -- (7.6,{y});']
    for i in range(-6,8): o.append(f'\\draw (-0,{y}) ++({i*1.0:.1f},0.07) -- ++(0,-0.14); \\node[below=2pt,font=\\footnotesize] at ({i*1.0:.1f},{y}) {{${i}$}};')
    o.append(f'\\draw[line width=3.2pt,{renk}] ({a:.1f},{y}) -- ({b:.1f},{y});')
    for p,k in ((a,aK),(b,bK)):
        o.append(f'\\filldraw[{renk},fill={"white" if not k else renk},thick] ({p:.1f},{y}) circle (0.12);')
    o.append(f'\\node[{renk},font=\\small\\bfseries,above=7pt] at ({(a+b)/2:.1f},{y}) {{{ad}}};')
    return '\n'.join(o)
SK=fig(sd(1.4,-3,2,True,True,MAVI,'$f$ fonksiyonunun tanım kümesi')+'\n'+sd(-0.4,-5,7,False,True,TUR,'$g$ fonksiyonunun tanım kümesi'),font='\\footnotesize')
q('0017',tipId='fn-tanim',tip='Birebir, örten ve tanım kümeleri',z='zor',alt='Bileşkenin Tanım Kümesi',kaz='İki fonksiyonun tanım kümelerini sayı doğrusunda okuyarak bileşkenin tanım kümesini bulur ve tam sayılarını toplar.',kalip='şekilli',
 kart='K-AFNK-06 (sayı doğrusu, bileşkenin tanım kümesi) · f(x) = 3x − 2; Df = [−3, 2], Dg = (−5, 7]',
 metin='f(x) = 3x − 2 kuralıyla tanımlanan f fonksiyonu ile g fonksiyonunun tanım kümeleri, sayı doğrusunda şekilde gösterilmiştir; dolu nokta uç noktanın kümeye ait olduğunu, içi boş nokta ait olmadığını belirtmektedir.\nBuna göre g ∘ f bileşke fonksiyonunun tanım kümesindeki tam sayıların toplamı kaçtır?',
 dogru=v,yan=[(e[0],'f’nin kendi tanım kümesini hesaba katmadan yalnız −5 < 3x − 2 ≤ 7 eşitsizliğini çözmüş: −1 < x ≤ 3.','dikkat'),(e[1],'f’nin değerleri yerine x’in kendisini g’nin tanım kümesiyle karşılaştırıp [−3, 2] ∩ (−5, 7] kümesini almış.','bilgi'),(e[2],'g’nin tanım kümesinin −5 ucunun içi boş olduğunu görmeyip f(x) = −5 değerini de dahil etmiş: x = −1 sayısını eklemiş.','dikkat'),(e[3],'f’nin tanım kümesinin 2 ucunu dışlamış; oysa 2 uç noktası dolu noktayla gösterilmiştir.','dikkat')],
 istenen='g ∘ f’nin tanım kümesindeki tam sayıların toplamı.',ip=['g ∘ f’nin tanımlı olması için x’in sağlaması gerekenleri şekle bakarak düşün.'],bilgi=[TAN],sekil=SK,
 ad=[A('Birinci koşul','x, f’nin tanım kümesinde olmalıdır.','−3 ≤ x ≤ 2'),A('İkinci koşul','f(x) g’nin tanım kümesine düşmelidir.','−5 < 3x − 2 ≤ 7'),A('Eşitsizliği çöz','Her tarafa 2 eklenip 3’e bölünür.','−1 < x ≤ 3'),A('Kesişim','İki koşul birlikte sağlanır.','−1 < x ≤ 2'),A('Tam sayıları topla','Bu aralıktaki tam sayılar 0, 1, 2’dir.','0 + 1 + 2 = 3')],
 puf='Bileşkenin tanım kümesi her zaman iç fonksiyonun tanım kümesinin bir alt kümesidir.')

# ================= 18 zor · tablo, bileşkenin tekrarı =================
f18={1:3,2:4,3:5,4:6,5:1,6:7,7:2}
def it(n,x):
    for _ in range(n): x=f18[x]
    return x
n1,n2=2025,2027
v=it(n1,1)+it(n2,2); assert (it(n1,1),it(n2,2),v)==(1,7,8)
e=[it(n1%4,1)+it(n2%3,2), it(n1%3+1,1)+it(n2%4+1,2), it(1,1)+it(n2,2), it(n1%7,1)+it(n2%7,2)]
assert e==[9,5,10,7]; uniq(v,e)
SK=tablo_svg(['x','1','2','3','4','5','6','7'],[['f(x)']+[str(f18[i]) for i in range(1,8)]])
q('0018',tipId='fn-bilesik',tip='Bileşke fonksiyon değeri',z='zor',alt='Bileşkenin Tekrarı',kaz='Tabloyla verilen fonksiyonun kendisiyle çok sayıda bileşkesinde değerlerin döngüsünü bulup üs sayısını döngü uzunluğuna göre indirger.',kalip='tablo',
 kart='K-AFNK-01 (tablo, döngü) · iki döngü: 1 → 3 → 5 → 1 ve 2 → 4 → 6 → 7 → 2; f²⁰²⁵(1) + f²⁰²⁷(2)',
 metin='A = {1, 2, 3, 4, 5, 6, 7} kümesi üzerinde tanımlı f fonksiyonunun değerleri aşağıdaki tabloda verilmiştir. Bir fonksiyonun kendisiyle n kez bileşkesi fⁿ ile gösterilmektedir.\nBuna göre f²⁰²⁵(1) + f²⁰²⁷(2) toplamı kaçtır?',
 dogru=v,yan=[(e[0],'Döngü uzunluklarını karıştırmış: 1’in döngüsü 3 adımlı iken 4’e, 2’nin döngüsü 4 adımlı iken 3’e göre kalan almış.','bilgi'),(e[1],'Kalanı bulduktan sonra bir adım fazla ilerlemiş: 1 için 1, 2 için 4 adım atmış.','islem'),(e[2],'1’in döngüsünde kalan 0 çıkınca başlangıçta kalmak yerine 1 adım ilerlemiş.','dikkat'),(e[3],'Her iki girişte de üssü 7’ye göre indirgeyip döngü uzunluklarına bakmamış.','bilgi')],
 istenen='f²⁰²⁵(1) + f²⁰²⁷(2) toplamı.',ip=['f’yi art arda uygulayınca değerler nasıl davranıyor?'],bilgi=[BIL],sekil=SK,
 ad=[A('1’in döngüsü','1’den başlanır, kaç adımda başa dönüldüğü bulunur.','1 → 3 → 5 → 1 (3 adım)'),A('2’nin döngüsü','2’den başlanır.','2 → 4 → 6 → 7 → 2 (4 adım)'),A('Üsleri indirge','2025, 3’ün katıdır; 2027’nin 4’e bölümünden kalan 3’tür.','f²⁰²⁵(1) = 1 · f²⁰²⁷(2) = f³(2)'),A('f³(2)','2’den üç adım ilerlenir.','2 → 4 → 6 → 7'),A('Topla','İki değer toplanır.','1 + 7 = 8')],
 puf='Döngüde n adım atmak, n’nin döngü uzunluğuna bölümünden kalan kadar adım atmakla aynıdır.')

# ================= 19 zor · fonksiyonel denklem sistemi (şekilsiz) =================
h19=lambda x:2*x*x+3*x-2
fa19=Fr(2*h19(-1)-h19(2),3); assert fa19==-6
v=fa19; e=[Fr(h19(2),3),Fr(h19(-1),3),Fr(2*h19(-1)+h19(2),3),Fr(2*h19(2)-h19(-1),3)]
assert e==[4,-1,2,9]; uniq(v,e)
q('0019',tipId='fn-fonkdenk',tip='Fonksiyonel denklem',z='zor',alt='İki Bilinmeyenli Fonksiyonel Denklem',kaz='f(x) ve f(1 − x) içeren eşitlikte x yerine iki uygun değer yazıp oluşan denklem sisteminden f değerini bulur.',kalip='düz',
 kart='K-AFNK-07 (f(x) + 2f(1 − x) = 2x² + 3x − 2) · f(2)',
 metin='Gerçel sayılar kümesi üzerinde tanımlı bir f fonksiyonu, her x gerçel sayısı için\nf(x) + 2·f(1 − x) = 2x² + 3x − 2\neşitliğini sağlamaktadır.\nBuna göre f(2) değeri kaçtır?',
 dogru=v,yan=[(e[0],'f(1 − x) terimini de f(x) sayıp 3f(2) = 12 yazmış.','bilgi'),(e[1],'x = −1 için kurduğu eşitlikte f(−1) ile f(2) terimlerini aynı sanıp 3f(2) = −3 bulmuş.','bilgi'),(e[2],'2f(−1) + 4f(2) = −6 eşitliğinden 2f(−1) + f(2) = 12’yi çıkarırken 3f(2) = −6 − 12 yerine −6 + 12 = 6 yazıp f(2) = 2 bulmuş.','islem'),(e[3],'Sistemi doğru çözüp f(−1) = 9 değerini bulmuş, fakat sorulan f(2) yerine f(−1)’i yazmış.','dikkat')],
 istenen='f(2) değeri.',ip=['x yerine iki farklı değer yazınca hangi terimler ortak görünüyor?'],bilgi=[FDN],
 ad=[A('x = 2 yaz','1 − 2 = −1 olduğundan f(−1) görünür.','f(2) + 2f(−1) = 12'),A('x = −1 yaz','1 − (−1) = 2 olduğundan f(2) görünür.','f(−1) + 2f(2) = −3'),A('Eşitliği hazırla','İkinci eşitlik 2 ile çarpılır.','2f(−1) + 4f(2) = −6'),A('Denklemleri çıkar','Birinciyi çıkarınca f(−1) yok olur.','3f(2) = −18'),A('f(2) değeri','Her iki taraf 3’e bölünür.','f(2) = −6')],
 puf='f(x) ve f(1 − x) birlikte görünüyorsa x ile 1 − x’i birbirinin yerine yazmak iki denklem verir.')

# ================= 20 zor · öncüllü, tek ve periyodik (şekilsiz) =================
SIK20=['Yalnız I','I ve II','I ve III','II ve III','I, II ve III']
fp=lambda n:{0:0,1:3,2:0,3:-3}[n%4]       # f(1) = 3, f(2) = 0, f(3) = −3, f(0) = 0
assert all(fp(-x)==-fp(x) and fp(x+4)==fp(x) for x in range(-12,13))
assert (fp(-3),fp(2),fp(102))==(3,0,0)
q('0020',tipId='fn-ozellik',tip='Tek, çift ve periyodik fonksiyonlar',z='orta',alt='Tek ve Periyodik Fonksiyon',kaz='Hem tek hem periyodik bir fonksiyonun verilen bir değerinden başka noktalardaki değerleri çıkararak öncülleri sınar.',kalip='öncüllü',
 kart='K-AFNK-04 (tek ve periyot 4, öncüllü) · f(1) = 3; f(−3) = 3, f(2) = 0, f(102) = 0',
 metin='Gerçel sayılar kümesi üzerinde tanımlı bir f fonksiyonu tek fonksiyondur ve her x gerçel sayısı için f(x + 4) = f(x) eşitliğini sağlamaktadır. Ayrıca f(1) = 3 olarak verilmiştir.\nI. f(−3) = 3’tür.\nII. f(2) = 0’dır.\nIII. f(102) = −3’tür.\nBu ifadelerden hangileri kesinlikle doğrudur?',
 dogru='I ve II',sira=SIK20,yan=[('Yalnız I','II’yi sınamamış: f(2) = f(−2) = −f(2) olduğundan f(2) = 0’dır.','islem'),('I ve III','II’yi sınamayıp III’ü doğru sanmış; oysa f(102) = f(2) = 0’dır, −3 değildir.','dikkat'),('II ve III','I’i yanlış sanmış: f(−3) = f(−3 + 4) = f(1) = 3’tür; III’ü ise f(102) = f(2) = 0 olduğu hâlde doğru saymış.','islem'),('I, II ve III','III’ü doğru sanmış: 102 = 4·25 + 2 olduğundan f(102) = f(2) = 0’dır.','dikkat')],
 istenen='Kesinlikle doğru olan öncüllerin hangileri olduğu.',ip=['Periyot ve tek fonksiyon özelliğini birlikte kullanarak her girişi f(1) = 3’ün bilindiği bir noktaya taşı.'],bilgi=[OZE],
 ad=[A('I’i sına','Periyot 4 olduğundan −3’e 4 eklenir.','f(−3) = f(1) = 3'),A('II’yi sına','2’den 4 çıkarınca −2 bulunur; tek fonksiyonda f(−2) = −f(2).','f(2) = f(−2) = −f(2) → f(2) = 0'),A('III’ü sına','102’den 4’ün katları atılır; II’deki sonuç kullanılır.','f(102) = f(2) = 0 ≠ −3'),A('Sonuç','I ve II doğru, III yanlıştır.','I ve II')],
 puf='Periyot, girişi küçük bir aralığa indirir; tek fonksiyon özelliği de negatif girişleri pozitife çevirir.')

# ---------------- bitir ----------------
for q_ in P.ANA: q_['kardes']=None
P.yaz(os.path.join(HD,'fonks-1.json'),'/tmp/bos-fonks.json')
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=UK))['kartlar'].append(c['id'])
json.dump(dict(konu='Fonksiyonlar',surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 AYT Matematik çıkmış fonksiyon soruları ve yayın soru bankaları (yalnız mantık), MEB 11–12. sınıf müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','fonks.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
