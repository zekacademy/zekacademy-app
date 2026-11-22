"""AYT Matematik · Fonksiyonlar 2. dalga (20 soru): mutlak değerli/parçalı grafikler, dönüşümler, bileşke ve ters; her doğru ve çeldirici değer kodla hesaplanıp assert edilir.
Kardeş yok, ipucu 1. Çıktı: ayt-mat/fonksiki-1.json, kartlar/fonksiki.json."""
import sys,os,json,itertools
HD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(HD,'..')
sys.path.insert(0,os.path.join(HV,'tyt-mat')); sys.path.insert(0,HV)
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
HD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(HD,'..')
H.KONU='Fonksiyonlar'
UK='amat|Fonksiyonlar'
P=Parti('fonksiki','Fonksiyonlar',UK,ders='AYT Matematik',idon='aytmat')
KY='ÖSYM 2018–2026 AYT Matematik çıkmış fonksiyon soruları (grafik okuma, dönüşümler, bileşke, ters, fonksiyonel denklem; yalnız mantık) · MEB 11–12. sınıf'
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)
def fig(body,font='\\small'): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font='+font+']\n'+body+'\n\\end{tikzpicture}')
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)
def uniq(v,e): assert len({Fr(x) for x in [v]+list(e)})==5,(v,e)
MAVI='blue!70!black'; TUR='orange!90!black'; MOR='violet!80!black'; YES='vurgu!80!black'
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
    o.append(f'\\node[draw,thick,rounded corners=3pt,minimum width=1.0cm,minimum height=0.8cm] (g0) at (0,0) {{${giris}$}}; \\node[above=1pt,font=\\small] at (g0.north) {{giriş}};')
    prev='g0'
    for i,(ad,kural) in enumerate(kutular):
        nm=f'm{i}'; c=cols[i%4]
        o.append(f'\\node[draw={c},fill={c}!12,line width=1.4pt,rounded corners=3pt,minimum width=2.5cm,minimum height=1.1cm,right=0.9cm of {prev},align=center] ({nm}) {{\\textbf{{${ad}$}}\\\\[-1pt] ${kural}$}};')
        o.append(f'\\draw[-{{Stealth}},thick] ({prev}.east) -- ({nm}.west);'); prev=nm
    o.append(f'\\node[draw,thick,rounded corners=3pt,minimum width=1.0cm,minimum height=0.8cm,right=0.9cm of {prev}] (gs) {{${cikis}$}}; \\node[above=1pt,font=\\small] at (gs.north) {{çıkış}};')
    o.append(f'\\draw[-{{Stealth}},thick] ({prev}.east) -- (gs.west);')
    return '\n'.join(o)

def sols(V,k):
    """Kırık çizgi grafiğinin y=k doğrusuyla kesişim apsisleri (küme)."""
    k=Fr(k); S=set()
    for (x1,y1),(x2,y2) in zip(V,V[1:]):
        if y1==y2:
            assert y1!=k; continue
        if min(y1,y2)<=k<=max(y1,y2): S.add(Fr(x1)+Fr(k-y1,y2-y1)*(x2-x1))
    return S
def ucok(V,sx,sy,renk,w='1.8pt',sol=None,sag=None,dash='',nokta=True):
    """Uçlarında ok olan (tanım kümesi gerçel sayılar) kırık çizgi; sol/sag: ok ucunun (x,y) noktası."""
    P_=list(V)
    if sol: P_=[sol]+P_
    if sag: P_=P_+[sag]
    st=('{Stealth}-' if sol else '')+('{Stealth}' if sag else '')
    o=[f'\\draw[line width={w},{renk}{dash},{st}] '+' -- '.join(f'({x*sx:.3f},{y*sy:.3f})' for x,y in P_)+';']
    if nokta:
        for x,y in V: o.append(f'\\fill[{renk}] ({x*sx:.3f},{y*sy:.3f}) circle (0.075);')
    return '\n'.join(o)
def lab(x,y,s,renk,sx,sy,pos='right'):
    return f'\\node[{renk},font=\\small\\bfseries,fill=white,inner sep=1pt,{pos}] at ({x*sx:.3f},{y*sy:.3f}) {{${s}$}};'
SIK6=['Yalnız I','Yalnız II','I ve II','I ve III','II ve III']
SIK12=['Yalnız I','Yalnız II','I ve III','II ve III','I, II ve III']

# ---------- bilgi kutuları ----------
BMUT=B('Mutlak değerli fonksiyonların grafiği','y = |f(x)| grafiği, f’nin x-ekseninin altında kalan kısmının eksene göre yansıtılmasıyla; y = f(|x|) grafiği ise f’nin x ≥ 0 için çizilen kısmının y-eksenine göre yansıtılmasıyla elde edilir. Örnek: f(x) = x − 2 için f(0) = −2 iken |f(0)| = 2’dir ve |f(x)| grafiği x = 2 noktasında kırılır')
BYAN=B('Yansıma ve öteleme','y = −f(x) grafiği f’nin x-eksenine, y = f(−x) grafiği y-eksenine göre simetriğidir. y = f(a − x) = f(−(x − a)) için grafik önce y-eksenine göre yansıtılır, sonra a birim sağa ötelenir. Örnek: f(1) = 4 ise y = f(−x) grafiği (−1, 4) noktasından, y = −f(x) grafiği (1, −4) noktasından geçer')
BKAT=B('Katsayıların grafikteki etkisi','a > 0 için y = f(x) + a grafiği yukarı, a < 0 için aşağı kayar. b < 0 ise y = b·f(x) grafiği x-eksenine göre ters çevrilir, |b| > 1 ise dikeyde uzar. |c| > 1 ise y = f(c·x) grafiği yatayda daralır; c < 0 ise ayrıca y-eksenine göre yansır. Örnek: f(x) = x² için f(2x) = 4x² grafiği daha dardır')
BKEN=B('Fonksiyonun kendisiyle bileşkesi','f(x) = ax + b ise (f ∘ f)(x) = a·(ax + b) + b = a²x + ab + b’dir. İki doğrusal ifadenin eşitliğinde x’in katsayıları ve sabit terimler ayrı ayrı eşitlenir. Örnek: f(x) = 3x + 2 ise (f ∘ f)(x) = 9x + 8’dir')
BKES=B('Kesirli fonksiyonun tersi','y = (ax + b)/(cx + d) denkleminde x yalnız bırakılır, sonra x ile y’nin yeri değiştirilir. İki kesirli ifade her x için eşitse pay ve paydalar orantılı olmalıdır. Örnek: f(x) = (x + 1)/(x − 2) için y(x − 2) = x + 1 → x = (2y + 1)/(y − 1) olduğundan f⁻¹(x) = (2x + 1)/(x − 1)’dir')
BYAT=B('Yatay doğru ve grafik','y = k doğrusunun grafiği kestiği noktaların apsisleri f(x) = k denkleminin çözümleridir. Grafik bir noktada tepe yaparken k değerine değiyorsa o nokta yine bir çözümdür. Örnek: y = 2 doğrusu grafiği x = −1, 3 ve 5’te kesiyorsa f(x) = 2 eşitliğini sağlayan sayılar yalnızca bunlardır')
BGOR=B('Parçalı fonksiyonun görüntü kümesi','Her parçanın aldığı değerler aralık olarak yazılır; dolu uç kümeye dahil, boş uç dahil değildir; parçaların aralıkları birleştirilir. Örnek: x ∈ [0, 1) için f(x) = x ve x ∈ [1, 2] için f(x) = x + 1 ise görüntü kümesi [0, 1) ∪ [2, 3]’tür')
BSAY=B('Birebir fonksiyonların sayısı','s(A) = m, s(B) = n ve m ≤ n olmak üzere A’dan B’ye tanımlı birebir fonksiyonların sayısı n·(n − 1)·…·(n − m + 1)’dir. Koşullu sayımlarda koşulu bozan fonksiyonlar bütünden çıkarılır. Örnek: s(A) = 2, s(B) = 4 ise birebir fonksiyon sayısı 4·3 = 12’dir')
BTER=B('Ters fonksiyon','f birebir ve örten ise f(a) = b olması f⁻¹(b) = a demektir; f⁻¹ için y = f(x) denkleminde x yalnız bırakılıp x ile y’nin yeri değiştirilir. Örnek: f(x) = 4x + 1 ise f⁻¹(x) = (x − 1)/4’tür')
BTGR=B('Grafikten ters fonksiyon değeri','f birebir ve örten ise f(a) = b olması f⁻¹(b) = a demektir; grafikte y = b doğrusunun grafiği kestiği noktanın apsisi f⁻¹(b)’dir. Bileşkelerde içten dışa doğru ilerlenir. Örnek: grafik (2, 7) noktasından geçiyorsa f(2) = 7 ve f⁻¹(7) = 2’dir')
BMAK=B('Bileşke fonksiyon','(g ∘ f)(x) = g(f(x)) demektir: önce f, sonra g uygulanır. g(f(x)) ifadesi verilmişse u = f(x) yazılıp x, u cinsinden bulunarak g(u) elde edilir. Örnek: f(x) = x + 1 ve (g ∘ f)(x) = 2x ise x = u − 1 olduğundan g(u) = 2u − 2’dir')
BTRB=B('Bileşke ve ters fonksiyon','(g ∘ f)(x) verildiğinde f⁻¹ biliniyorsa u = f(x) için x = f⁻¹(u) yazılarak g(u) bulunur. g(a) = b ise g⁻¹(b) = a’dır. Örnek: f⁻¹(x) = 2x ve (g ∘ f)(x) = x + 5 ise g(u) = 2u + 5 olur; g⁻¹(9) için 2u + 5 = 9’dan u = 2 bulunur')
BFOF=B('İç içe fonksiyonlu denklemler','Bileşkeli denklemlerde iç fonksiyona yeni bir ad verilir (u = f(x)) ve denklem iki aşamada çözülür: önce u için, sonra her u için x bulunur. Çözüm sayısı ve toplamı grafikten okunur. Örnek: f(f(x)) = 4 denkleminde önce f(u) = 4 çözülür, sonra her u için f(x) = u çözülür')
BALN=B('Mutlak değer ve alan','y = |f(x)| grafiği ile x-ekseni arasındaki alan, f’nin grafiği ile eksen arasındaki alanların mutlak değerlerinin toplamıdır; grafik ekseni kestiği noktalarda parçalanır. Örnek: f(x) = x − 1 için [0, 3] aralığında |f| altındaki alan, x = 1’de ayrılan iki üçgenin alanları toplamıdır')
BFDN=B('Fonksiyonel denklem','Eşitlik her x için sağlandığından x yerine uygun değerler yazılarak bilinmeyen değerler için denklem sistemi kurulur. Örnek: f(x) + 3f(−x) = 4x ise x = 1 ve x = −1 yazılarak f(1) ve f(−1) için iki denklem elde edilir')
BPER=B('Çift ve periyodik fonksiyon','Her x için f(x + T) = f(x) ise f periyodiktir, f(x + kT) = f(x)’tir; f(−x) = f(x) ise f çifttir. Büyük bir sayı, T’nin katı atılarak küçültülür. Örnek: periyodu 3 olan g için g(100) = g(1)’dir; çift bir h için h(−2) = h(2)’dir')

# ---------- kartlar (her tipId için bir kart) ----------
kartla('K-AFNK2-01','Mutlak değerli fonksiyonların grafiği','|f(x)| ve f(|x|) grafikleri f’nin grafiğinden yansıtılarak elde edilir; denklem çözüm sayısı yatay doğrunun yeni grafiği kestiği noktalardan sayılır.','Teğet ya da köşe noktalarını saymamak; |f(x)| = k için f(x) = −k’yi unutmak; yansımayı yanlış bölgeye uygulamak.','orta','grafik',4,'fn2-mutlak','Mutlak değerli fonksiyonların grafiği')
kartla('K-AFNK2-02','Grafik dönüşümleri ve katsayı işaretleri','Dönüşmüş grafik asıl grafiğin yansıtılması, ötelenmesi ve ölçeklenmesiyle oluşur; katsayıların işareti tepe noktasının ve açıklığın yönünden okunur.','Yansıma ile ötelemenin sırasını karıştırmak; f(−x) ile −f(x)’i birbirine çevirmek; f(cx)’te tepe konumunu c ile çarpmak.','orta','grafik',4,'fn2-donusum','Grafik dönüşümleri ve katsayı işaretleri')
kartla('K-AFNK2-03','Ters fonksiyon ve bileşkesi','Ters için işlemler geri alınır; g(f(x)) verilmişse u = f(x) yazılarak kural bulunur; ters değerler grafikte yatay doğrudan okunur.','f⁻¹’i 1/f ile karıştırmak; bileşkede sırayı değiştirmek; g⁻¹ yerine g’nin değerini hesaplamak.','orta','düz',4,'fn2-ters','Ters fonksiyon ve bileşkesi')
kartla('K-AFNK2-04','Bileşke fonksiyon ve grafikli denklem','Bileşkeli denklem iki aşamada çözülür; grafikten iç değerler, sonra her iç değer için x çözümleri okunur.','Aşamalardan birini atlamak; bir çözümü iki kez saymak; makinede sırayı ters uygulamak.','zor','grafik',4,'fn2-bilesik','Bileşke fonksiyon ve grafikli denklem')
kartla('K-AFNK2-05','Parçalı fonksiyon','Her parçanın değer aralığı bulunup uçların dahil olup olmadığına bakılır; parçalar birleştirilir.','Boş uç noktayı kümeye katmak; parçalar arasındaki boşluğu görmemek; çakışan aralıkları iki kez saymak.','orta','grafik',3,'fn2-parcali','Parçalı fonksiyon')
kartla('K-AFNK2-06','Grafikten özellik okuma','Yatay doğrunun grafiği kestiği noktalar ve tek ya da periyodik fonksiyon özellikleri birlikte kullanılır.','Tek fonksiyonda işareti unutmak; periyodu yanlış almak; kesişim sayısını eksik görmek.','orta','grafik',4,'fn2-grafikoku','Grafikten özellik okuma')
kartla('K-AFNK2-07','Koşullu fonksiyon sayma','Birebir fonksiyon sayısı çarpma kuralıyla bulunur; koşulu bozan durumlar çıkarılır ve çakışanlar geri eklenir.','Çakışan durumları iki kez çıkarmak; son terimi unutmak; koşulsuz sayıyı cevap sanmak.','zor','düz',4,'fn2-sayma','Koşullu fonksiyon sayma')
kartla('K-AFNK2-08','Dönüşümlü fonksiyonel denklem','x yerine 1/x gibi dönüşmüş değer yazılarak iki bilinmeyenli denklem kurulur ve birlikte çözülür.','Tek denklemle yetinmek; eşitliği her iki yerde de aynı değere uygulamamak; kesirli sayıyla işlem hatası.','zor','düz',4,'fn2-fonkdenk','Dönüşümlü fonksiyonel denklem')

# ================= 01 kolay · mutlak değerli grafikten parametre okuma =================
a1,b1=2,-1; f1=lambda x:abs(x-a1)+b1
v=f1(7); assert v==4
e=[abs(7+a1)+b1, abs(7-a1)-b1, abs(7+a1)-b1, abs(7-a1)]
assert e==[8,6,10,5]; uniq(v,e)
sx=sy=0.7
SK=fig(graf(-1,5,-2,3,sx,sy,ucok([(2,-1)],sx,sy,MAVI,sol=(-1,2),sag=(5,2),nokta=True)+'\n'+lab(3.0,-1.4,'y=f(x)',MAVI,sx,sy,'right')))
q('0001',tipId='fn2-mutlak',tip='Mutlak değerli fonksiyonların grafiği',z='kolay',alt='Mutlak Değerli Grafik',kaz='Mutlak değerli fonksiyonun grafiğinden tepe noktasını okuyarak kuralını belirler ve değer hesaplar.',kalip='grafik',
 kart='K-AFNK2-01 (grafikten |x − a| + b parametresi) · tepe (2, −1); f(7)',
 metin='Gerçel sayılar kümesi üzerinde, a ve b gerçel sayılar olmak üzere f(x) = |x − a| + b kuralıyla tanımlanan f fonksiyonunun grafiği şekilde verilmiştir.\nBuna göre f(7) değeri kaçtır?',
 dogru=v,yan=[(e[0],'a’yı işaretini değiştirerek a = −2 almış: |7 + 2| − 1 = 8.','bilgi'),(e[1],'b’yi işaretini değiştirerek b = 1 almış: |7 − 2| + 1 = 6.','bilgi'),(e[2],'Hem a hem b’nin işaretini ters okumuş: |7 + 2| + 1 = 10.','dikkat'),(e[3],'Tepe noktasının ordinatını unutup yalnız |7 − 2| = 5 değerini yazmış.','dikkat')],
 istenen='f(7) değeri.',ip=['Grafiğin kırıldığı (tepe) noktanın koordinatlarını oku; a ve b bu noktadan belirlenir.'],bilgi=[BMUT],sekil=SK,
 ad=[A('Tepe noktasını oku','|x − a| + b grafiği x = a’da kırılır ve tepe noktasının ordinatı b’dir.','Tepe noktası (2, −1) → a = 2, b = −1'),A('Kuralı yaz','a ve b yerine yazılır.','f(x) = |x − 2| − 1'),A('f(7)','x yerine 7 yazılır.','|7 − 2| − 1 = 5 − 1 = 4')],
 puf='Tepe noktasının apsisi a, ordinatı b’dir; kuralı bulduktan sonra grafikteki bir noktayla kontrol et.')

# ================= 02 kolay · tabloyla doğrusal fonksiyon, ters =================
f2=lambda x:2*x-2; v=Fr(f2(5)+(6+2)//2); 
assert f2(5)==8 and (6+2)//2==4 and v==12
e=[ (6-2)//2+f2(5), 6//2+f2(5), 4-f2(5), f2(5)]
assert e==[10,11,-4,8]; uniq(v,e)
SK=tablo_svg(['x','0','1','2'],[['f(x)','−2','0','2']])
q('0002',tipId='fn2-ters',tip='Ters fonksiyon ve bileşkesi',z='kolay',alt='Doğrusal Fonksiyonun Tersi',kaz='Tabloyla değerleri verilen doğrusal fonksiyonun kuralını bulup tersinin ve kendisinin değerini hesaplar.',kalip='tablo',
 kart='K-AFNK2-03 (tablodan doğrusal kural, ters) · f(0) = −2, f(1) = 0, f(2) = 2; f⁻¹(6) + f(5)',
 metin='Gerçel sayılar kümesi üzerinde tanımlı doğrusal f fonksiyonunun bazı değerleri aşağıdaki tabloda verilmiştir.\nBuna göre f⁻¹(6) + f(5) toplamı kaçtır?',
 dogru=int(v),yan=[(e[0],'Tersi f⁻¹(x) = (x − 2)/2 almış (işareti ters): f⁻¹(6) = 2; 2 + 8 = 10.','islem'),(e[1],'Tersi f⁻¹(x) = x/2 almış (−2’yi hesaba katmamış): f⁻¹(6) = 3; 3 + 8 = 11.','islem'),(e[2],'Toplamak yerine f⁻¹(6) − f(5) = 4 − 8 farkını almış.','dikkat'),(e[3],'f⁻¹(6) terimini hesaba katmayıp yalnız f(5) = 8 değerini yazmış.','dikkat')],
 istenen='f⁻¹(6) + f(5) toplamı.',ip=['Tablodaki değerlerden x’in 1 artışında f(x)’in ne kadar değiştiğini bul; kuralı yazıp tersini ayrıca hesapla.'],bilgi=[BTER],sekil=SK,
 ad=[A('Kuralı bul','x 1 arttığında f(x) 2 arttığından eğim 2’dir; f(0) = −2 sabit terimi verir.','f(x) = 2x − 2'),A('Tersi bul','y = 2x − 2 denkleminde x yalnız bırakılır.','x = (y + 2)/2 → f⁻¹(x) = (x + 2)/2'),A('Değerleri hesapla','f⁻¹(6) ve f(5) bulunur.','f⁻¹(6) = 8/2 = 4; f(5) = 10 − 2 = 8'),A('Topla','İki değer toplanır.','4 + 8 = 12')],
 puf='f⁻¹(6) = a ise f(a) = 6 olmalıdır; bulduğun a’yı kuralda deneyerek kontrol et.')

# ================= 03 kolay · yansıma =================
V3=[(-3,2),(-2,-1),(0,1),(1,3),(2,0),(3,2)]
h3=lambda x:pl(V3,-x)
v=h3(2)+h3(-1); assert (pl(V3,-2),pl(V3,1),v)==(-1,3,2)
e=[pl(V3,2)+pl(V3,-1), h3(2)-h3(-1), pl(V3,-2)+pl(V3,-1), pl(V3,2)-pl(V3,-2)]
assert e==[0,-4,-1,1]; uniq(v,e)
sx=sy=0.62
SK=fig(graf(-3,3,-2,4,sx,sy,egri(V3,sx,sx,MAVI)+'\n'+lab(2.1,3.5,'y=f(x)',MAVI,sx,sy,'right')))
q('0003',tipId='fn2-donusum',tip='Grafik dönüşümleri ve katsayı işaretleri',z='kolay',alt='Y-Eksenine Göre Yansıma',kaz='f(−x) fonksiyonunun değerlerini f’nin grafiğinden okuyarak hesaplar.',kalip='grafik',
 kart='K-AFNK2-02 (h(x) = f(−x) değerleri) · köşeler (−3, 2), (−2, −1), (0, 1), (1, 3), (2, 0), (3, 2)',
 metin='f fonksiyonunun [−3, 3] aralığındaki grafiği, köşeleri kılavuz çizgilerinin kesiştiği noktalarda olan kırık çizgi olarak şekilde gösterilmiştir.\nh(x) = f(−x) kuralıyla tanımlanan h fonksiyonu için h(2) + h(−1) toplamı kaçtır?',
 dogru=int(v),yan=[(e[0],'Yansımayı uygulamamış: h yerine f’yi okuyup f(2) + f(−1) = 0 + 0 yazmış.','bilgi'),(e[1],'Toplamak yerine h(2) − h(−1) = −1 − 3 farkını almış.','dikkat'),(e[2],'h(−1) için işareti çevirmeyip f(−1) = 0 okumuş: f(−2) + f(−1) = −1 + 0.','dikkat'),(e[3],'h(x) yerine f(2) − f(−2) farkını almış: 0 − (−1).','bilgi')],
 istenen='h(2) + h(−1) toplamı.',ip=['h’nin her değeri için f’nin hangi apsisteki değerinin gerektiğini yaz; bu değerleri grafikten oku.'],bilgi=[BYAN],sekil=SK,
 ad=[A('h(2)','h(2) = f(−2) olduğundan grafikte x = −2’deki değer okunur.','f(−2) = −1'),A('h(−1)','h(−1) = f(1) olduğundan grafikte x = 1’deki değer okunur.','f(1) = 3'),A('Topla','İki değer toplanır.','−1 + 3 = 2')],
 puf='f(−x) için x’in işaretini çevirip aynı grafikten okuyabilirsin; yeni grafik çizmene gerek yok.')

# ================= 04 orta · |f(x)| = 2 çözüm sayısı =================
V4=[(-4,1),(-2,-3),(0,2),(2,-1),(4,3)]
S=sols(V4,2)|sols(V4,-2); assert sorted(S)==[Fr(-5,2),Fr(-8,5),0,Fr(7,2)] ,sorted(S)
v=len(S); assert v==4
e=[len(sols(V4,2)),3,5,8]; uniq(v,e)
sx=sy=0.6
SK=fig(graf(-4,4,-3,3,sx,sy,egri(V4,sx,sy,MAVI)+'\n'+lab(3.2,2.7,'y=f(x)',MAVI,sx,sy,'left')))
q('0004',tipId='fn2-mutlak',tip='Mutlak değerli fonksiyonların grafiği',z='orta',alt='|f(x)| = k Denklemi',kaz='Grafiği verilen fonksiyonun mutlak değeriyle kurulan denklemin çözüm sayısını yatay doğrularla belirler.',kalip='grafik',
 kart='K-AFNK2-01 (|f(x)| = 2, 4 çözüm) · köşeler (−4, 1), (−2, −3), (0, 2), (2, −1), (4, 3)',
 metin='Dik koordinat düzleminde [−4, 4] aralığında tanımlı f fonksiyonunun grafiği, köşeleri kılavuz çizgilerinin kesiştiği noktalarda olan kırık çizgi biçiminde şekilde verilmiştir.\nBuna göre |f(x)| = 2 denkleminin kaç farklı gerçel sayı çözümü vardır?',
 dogru=v,yan=[(e[0],'Mutlak değeri dikkate almayıp yalnız f(x) = 2 denklemini çözmüş: x = 0 ve x = 3,5.','bilgi'),(e[1],'f(x) = 2’den 2, f(x) = −2’den yalnız ilk parçadaki 1 çözümü sayıp 2 + 1 = 3 bulmuş.','dikkat'),(e[2],'Tepe noktası x = 0’ı iki parçanın ucu diye iki kez sayarak 5 bulmuş.','dikkat'),(e[3],'Her doğru parçasının hem y = 2 hem y = −2 ile kesiştiğini varsayıp 4·2 = 8 saymış.','islem')],
 istenen='|f(x)| = 2 denkleminin farklı çözüm sayısı.',ip=['|f(x)| = 2 eşitliğinin hangi iki ayrı denkleme dönüştüğünü yaz; her biri için y = k doğrusunun grafiği kaç noktada kestiğine bak.'],bilgi=[BMUT,BYAT],sekil=SK,
 ad=[A('Denklemi ayır','|f(x)| = 2 ise f(x) = 2 ya da f(x) = −2’dir.','f(x) = 2 veya f(x) = −2'),A('f(x) = 2','y = 2 doğrusu grafiği x = 0 (tepe) ve [2, 4] aralığındaki parçada keser.','2 çözüm'),A('f(x) = −2','y = −2 doğrusu grafiği [−4, −2] ve [−2, 0] aralığındaki parçalarda keser.','2 çözüm'),A('Say','Çözümler farklıdır.','2 + 2 = 4')],
 puf='Mutlak değerli denklemde k’nin hem pozitif hem negatif hâlini ayrı ayrı say; ortak noktaları iki kez sayma.')

# ================= 05 orta · |x − a| + |x − b| = 9 =================
f5=lambda x:abs(x+2)+abs(x-1)
V5=[(-3,5),(-2,3),(1,3),(2,5)]; assert all(f5(x)==y for x,y in V5)
R={x for x in range(-10,11) if f5(x)==9}; assert R=={-5,4}
v=-20; e=[-12,-1,-16,20]; uniq(v,e)
assert {x for x in range(-10,11) if f5(x)==7}=={-4,3}
sx,sy=0.75,0.5
SK=fig(graf(-4,3,0,6,sx,sy,ucok(V5,sx,sy,MAVI,sol=(-3.5,6),sag=(2.5,6))+'\n'+lab(2.5,5.2,'y=f(x)',MAVI,sx,sy,'right')))
q('0005',tipId='fn2-mutlak',tip='Mutlak değerli fonksiyonların grafiği',z='orta',alt='İki Mutlak Değerli Grafik',kaz='İki mutlak değer içeren fonksiyonun grafiğinden a ve b değerlerini okuyup denklemi çözer.',kalip='grafik',
 kart='K-AFNK2-01 (|x − a| + |x − b|, yatay parça) · kırılma noktaları x = −2 ve x = 1; f(x) = 9',
 metin='a < b olmak üzere gerçel sayılar kümesi üzerinde f(x) = |x − a| + |x − b| kuralıyla tanımlanan f fonksiyonunun grafiği şekilde verilmiştir.\nBuna göre f(x) = 9 denkleminin çözüm kümesindeki elemanların çarpımı kaçtır?',
 dogru=v,yan=[(e[0],'Denklemi f(x) = 7 almış: kökler −4 ve 3 olup çarpım −12 bulmuş.','dikkat'),(e[1],'Çarpım yerine kökler toplamını almış: −5 + 4 = −1.','dikkat'),(e[2],'Yalnız sağ kolu çözüp x = 4 bulmuş, sol kökü 4’ün simetriği sanıp −4 almış: 4·(−4) = −16.','islem'),(e[3],'Kökleri doğru bulmuş ancak çarpımın işaretini yanlış yazmış: (−5)·4 yerine 20.','dikkat')],
 istenen='f(x) = 9 denkleminin çözüm kümesindeki elemanların çarpımı.',ip=['Grafiğin kırıldığı iki apsisten a ve b’yi belirle; sonra mutlak değerleri açarak 9’a eşitle.'],bilgi=[BMUT,BYAT],sekil=SK,
 ad=[A('a ve b’yi oku','Grafik x = −2 ve x = 1 apsislerinde kırılır.','a = −2, b = 1 → f(x) = |x + 2| + |x − 1|'),A('Sağ kol','x ≥ 1 için iki mutlak değer de pozitif açılır.','(x + 2) + (x − 1) = 9 → x = 4'),A('Sol kol','x ≤ −2 için iki mutlak değer de ters işaretle açılır.','−(x + 2) − (x − 1) = 9 → x = −5'),A('Çarpım','−2 ≤ x ≤ 1 aralığında f(x) = 3 sabit olduğundan 9 oluşmaz; kökler çarpılır.','4 · (−5) = −20')],
 puf='Yatay parçanın yüksekliği (b − a) sabit değerdir; 9 bu değerden büyük olduğundan kökler yatay parçanın dışındadır.')

# ================= 06 orta · katsayı işaretleri =================
fb=lambda x:(x-1)**2
gA=lambda x:fb(x)+1; gB=lambda x:-Fr(1,2)*fb(x); gC=lambda x:fb(-2*x)  # a=+1, b=-1/2, c=-2
assert gC(Fr(-1,2))==4*0+ (-2*Fr(-1,2)-1)**2 and (-2*Fr(-1,2)-1)==0
def egr(fn,x0,x1,renk,n=24):
    pts=[x0+(x1-x0)*i/n for i in range(n+1)]
    return f'\\draw[line width=1.8pt,{renk}] plot[smooth] coordinates {{'+' '.join(f'({float(x)*sx:.3f},{float(fn(x))*sy:.3f})' for x in pts)+'};'
sx=sy=0.62
g6=egr(fb,-0.6,2.6,MAVI)+egr(gA,-0.6,2.6,TUR)+egr(gB,-1,3,YES)+egr(lambda x:(2*x+1)**2,-1.5,0.5,MOR)
g6+='\n'+lab(2.65,2.5,'y=f(x)',MAVI,sx,sy,'right')+lab(2.65,3.6,'y=f(x)+a',TUR,sx,sy,'right')+lab(3.0,-2,'y=b\\cdot f(x)',YES,sx,sy,'right')+lab(-1.5,3.7,'y=f(c\\cdot x)',MOR,sx,sy,'left')
SK=fig(graf(-4,3,-3,4,sx,sy,g6))
q('0006',tipId='fn2-donusum',tip='Grafik dönüşümleri ve katsayı işaretleri',z='orta',alt='Katsayıların İşareti',kaz='f(x) + a, b·f(x) ve f(c·x) grafiklerinden a, b ve c’nin işaretlerini belirler.',kalip='öncüllü',
 kart='K-AFNK2-02 (öncüllü, a > 0, b < 0, c < 0) · f(x) = (x − 1)² grafiği ve üç dönüşümü',
 metin='a, b ve c gerçel sayılar olmak üzere dik koordinat düzleminde y = f(x), y = f(x) + a, y = b·f(x) ve y = f(c·x) fonksiyonlarının grafikleri şekilde verilmiştir.\nI. a > 0 II. b < 0 III. c > 0\nBu ifadelerden hangileri doğrudur?',
 dogru='I ve II',sira=SIK6,yan=[('Yalnız I','b’nin işaretini sorgulamamış: ters çevrilmiş (aşağı açık) eğriyi b > 0 sanmış.','dikkat'),('Yalnız II','f(x) + a eğrisinin yukarı kaymasını a < 0 sanmış; yalnız ters çevrilen eğriyi b < 0 diye almış.','bilgi'),('I ve III','b < 0 olduğunu görmeyip tepesi sol tarafta kalan eğriyi c > 0 sanmış.','bilgi'),('II ve III','a’yı yanlış okumuş (a < 0 sanmış) ve tepesi sola kayan f(c·x) eğrisinden c > 0 sonucunu çıkarmış.','dikkat')],
 istenen='Doğru olan öncüllerin hangileri olduğu.',ip=['Her eğrinin tepe noktasını f’nin tepe noktasıyla karşılaştır: dikey kayma a’yı, açıklık yönü b’yi, yatay konum c’yi verir.'],bilgi=[BKAT],sekil=SK,
 ad=[A('I’i sına','f(x) + a eğrisinin tepe noktası f’ninkinin üstündedir.','a > 0 → I doğru'),A('II’yi sına','y = b·f(x) eğrisi aşağı açıktır; b < 0 ise eğri x-eksenine göre ters çevrilir.','b < 0 → II doğru'),A('III’ü sına','f(c·x) eğrisinin tepe noktası f’ninkinin tepe apsisi olan 1’in c’ye bölünmüşüdür; tepe sola, x = −1/2’ye kaymıştır.','1/c < 0 → c < 0 → III yanlış')],
 puf='f(c·x) için tepe noktasının apsisi 1/c olur; apsisin işareti c’nin işaretini verir.')

# ================= 07 orta · kesirli fonksiyon f = f⁻¹ =================
def fk(a,x): return Fr(a*x+2,x-3)
for xx in (4,5,7,-2): assert fk(3,fk(3,xx))==xx
v=fk(3,4); assert v==14
e=[fk(-3,4),fk(2,4),fk(6,4),fk(-2,4)]
assert e==[-10,10,26,-6]; uniq(v,e)
q('0007',tipId='fn2-ters',tip='Ters fonksiyon ve bileşkesi',z='orta',alt='Kesirli Fonksiyonun Tersi',kaz='Kesirli fonksiyonun tersini bulup kendisine eşit olma koşulundan bilinmeyen katsayıyı belirler.',kalip='düz',
 kart='K-AFNK2-03 (f = f⁻¹, kesirli fonksiyon) · f(x) = (ax + 2)/(x − 3)',
 metin='a bir gerçel sayı olmak üzere, x ≠ 3 için f(x) = (ax + 2)/(x − 3) kuralıyla tanımlanan f fonksiyonunun tersi kendisine eşittir.\nBuna göre f(4) değeri kaçtır?',
 dogru=int(v),yan=[(e[0],'Tersin paydasını x + a bulup x − 3 ile eşleştirerek a = −3 bulmuş: f(4) = (−12 + 2)/1.','islem'),(e[1],'Pay ile paydadaki sabitleri eşleyip a = 2 almış: f(4) = (8 + 2)/1.','bilgi'),(e[2],'y(x − 3) = ax + 2 denkleminde 3y yerine 6y yazıp a = 6 bulmuş: f(4) = (24 + 2)/1.','islem'),(e[3],'Ters kuralda pay ve paydadaki sabitlerin toplamını sıfır isteyip 2 + a = 0, a = −2 bulmuş: f(4) = (−8 + 2)/1.','bilgi')],
 istenen='f(4) değeri.',ip=['y = (ax + 2)/(x − 3) denkleminden x’i y cinsinden yaz, sonra f⁻¹’in kuralını f’nin kuralıyla karşılaştır.'],bilgi=[BKES],
 ad=[A('Tersi bul','y(x − 3) = ax + 2 denkleminde x yalnız bırakılır.','x(y − a) = 3y + 2 → f⁻¹(x) = (3x + 2)/(x − a)'),A('Eşitle','f⁻¹ ile f aynı kuraldır; paydaları karşılaştırınca x − a ile x − 3 eşit olmalıdır.','a = 3'),A('Kontrol et','a = 3 için pay da aynı çıkar.','f(x) = (3x + 2)/(x − 3) ve f⁻¹(x) = (3x + 2)/(x − 3)'),A('f(4)','x yerine 4 yazılır.','(12 + 2)/(4 − 3) = 14')],
 puf='Tersi kendisine eşit olan fonksiyonda f(f(x)) = x olur; bulduğun a’yı bir değerde bu eşitlikle sına.')

# ================= 08 orta · öncüllü sıralama =================
V8=[(-5,5),(-3,1),(-1,2),(1,3),(3,1),(5,5)]
S1=sols(V8,1); S3=sols(V8,3); assert S1=={-3,3} and S3=={-4,1,4},(S1,S3)
poss=[False]*3
for a,b in itertools.permutations(S1,2):
    for c,d in itertools.permutations(S3,2):
        if a<b<c<d: poss[0]=True
        if c<a<b<d: poss[1]=True
        if c<d<a<b: poss[2]=True
assert poss==[False,True,False]
sx=sy=0.62
SK=fig(graf(-5,5,0,5,sx,sy,egri(V8,sx,sy,MAVI)+'\n'+lab(4.4,4.6,'y=f(x)',MAVI,sx,sy,'left')))
q('0008',tipId='fn2-grafikoku',tip='Grafikten özellik okuma',z='orta',alt='Değerlerin Sıralanması',kaz='Aynı fonksiyon değerini alan sayıları grafikten bulup sıralamaların olabilirliğini sınar.',kalip='öncüllü',
 kart='K-AFNK2-06 (f(a) = f(b) = 1, f(c) = f(d) = 3; sıralama) · köşeler (−5, 5), (−3, 1), (−1, 2), (1, 3), (3, 1), (5, 5)',
 metin='f fonksiyonunun [−5, 5] aralığındaki grafiği şekilde verilmiştir; köşeler kılavuz çizgilerinin kesişimindedir. a, b, c ve d birbirinden farklı sayılardır ve\nf(c) = f(d) = 3\nf(a) = f(b) = 1\neşitliklerini sağlamaktadır.\nI. a < b < c < d II. c < a < b < d III. c < d < a < b\nBuna göre bu sıralamalardan hangileri gerçekleşebilir?',
 dogru='Yalnız II',sira=SIK6,yan=[('Yalnız I','c ve d olarak 1 ile 4’ü seçmiş; 1 < 3 olduğundan a < b < c < d sıralamasının bozulduğunu görmemiş.','dikkat'),('I ve II','I’i de doğru saymış: yalnız tek bir değer (x = 4) 3’ten büyük olduğundan c ve d ikisi birden b’nin sağında olamaz.','islem'),('I ve III','II’yi atlamış; I ve III’ü, f(x) = 3 çözümlerinden uygun olanları seçmeden doğru sanmış.','bilgi'),('II ve III','III’ü de doğru saymış: yalnız bir çözüm (x = −4) −3’ün solundadır, c ve d ikisi birden a’nın solunda olamaz.','islem')],
 istenen='Doğru olabilecek sıralamaların hangileri olduğu.',ip=['y = 1 ve y = 3 doğrularının grafiği kestiği noktaların apsislerini sıralı yaz; a, b ve c, d bu kümelerden seçilir.'],bilgi=[BYAT],sekil=SK,
 ad=[A('f(x) = 1 çözümleri','y = 1 doğrusu grafiğe yalnızca iki noktada değer: ikisi de çukur (tepe) noktasıdır.','a ve b, −3 ile 3’tür'),A('f(x) = 3 çözümleri','y = 3 doğrusu grafiği üç noktada keser.','c ve d, −4, 1 ve 4 sayılarından ikisidir'),A('I’i sına','b = 3’ün sağında yalnız 4 vardır; c ve d ikisi birden b’den büyük olamaz.','I olamaz'),A('II’yi sına','c = −4, d = 4 ve a = −3, b = 3 alınırsa c < a < b < d olur.','II olabilir'),A('III’ü sına','−3’ün solunda f(x) = 3’ün yalnız bir çözümü (x = −4) vardır; c ve d ikisi birden a’dan küçük olamaz.','III olamaz')],
 puf='Her değer için çözümleri soldan sağa sırala; sonra sıralamadaki iki sayının seçilebileceği yeterince çözüm var mı diye bak.')

# ================= 09 orta · makine, g(f(x)) =================
fm9=lambda x:3*x-2; gm9=lambda u:2*u+5
for x in range(-3,4): assert gm9(fm9(x))==6*x+1
v=gm9(5); assert v==15
e=[6*5+1,2*5+1,2*5-3,6*3+1]
assert e==[31,11,7,19]; uniq(v,e)
SK=fig(makine('x',[('f','3x-2'),('g','?')],'6x+1'))
q('0009',tipId='fn2-bilesik',tip='Bileşke fonksiyon ve grafikli denklem',z='orta',alt='Makinede g Fonksiyonunu Bulma',kaz='Bileşke değeri verilen makine sisteminde bilinmeyen ikinci fonksiyonun bir değerini hesaplar.',kalip='yeni nesil',
 kart='K-AFNK2-04 (g(f(x)) verilmiş, g bilinmiyor) · f(x) = 3x − 2, çıkış 6x + 1',
 metin='Şekildeki sistemde giriş kutusuna yazılan x gerçel sayısı önce f makinesine, ardından g makinesine girmekte ve çıkış kutusunda 6x + 1 ifadesi okunmaktadır. f makinesinin kuralı şekilde verilmiş, g makinesinin kuralı ise bilinmemektedir.\nBuna göre g(5) değeri kaçtır?',
 dogru=v,yan=[(e[0],'Çıkıştaki ifadeyi g’nin kuralı sanıp g(x) = 6x + 1 almış: g(5) = 31.','bilgi'),(e[1],'Yalnız 6x’i 3x’e böldüğü gibi 2x + 1 bulmuş: sabit terim hesabını yapmamış; g(5) = 11.','islem'),(e[2],'x = (u − 2)/3 yazıp (işareti ters kullanarak) g(u) = 2u − 3 bulmuş: g(5) = 7.','islem'),(e[3],'f(x) = 5 denkleminde x = 5 − 2 = 3 bulmuş (3’e bölmeyi unutmuş): 6·3 + 1 = 19.','islem')],
 istenen='g(5) değeri.',ip=['g makinesine giren sayı f(x)’tir; bu sayının 5 olması için x’in kaç olması gerektiğini bul.'],bilgi=[BMAK],sekil=SK,
 ad=[A('g’ye 5’in girmesi','g makinesine giren sayı f(x) olduğundan f(x) = 5 eşitliği çözülür.','3x − 2 = 5 → x = 7/3'),A('Çıkışı hesapla','Bu x için çıkış ifadesinde 6x + 1 yazılır.','6 · 7/3 + 1 = 14 + 1 = 15'),A('Sonuç','g makinesi 5’i bu çıkışa dönüştürür.','g(5) = 15')],
 puf='g(f(x)) = 6x + 1 eşitliğinde x yerine f(x) = 5 olduğu değeri yazarsan g(5) doğrudan elde edilir.')

# ================= 10 orta · parçalı fonksiyonun görüntü kümesi =================
P10=[((-3,-2),(0,1),True,False),((0,3),(2,5),True,False),((2,2),(4,4),True,True)]
im=[(-2,1,True,False),(3,5,True,False),(2,4,True,True)]
ints={n for n in range(-5,8) if any((lo<n<hi) or (n==lo and cl) or (n==hi and cr) for lo,hi,cl,cr in im)}
assert ints=={-2,-1,0,2,3,4}; v=len(ints)
e=[len({n for n in range(-5,8) if -2<=n<=4}),8,5,3]; assert e==[7,8,5,3]; uniq(v,e)
sx=sy=0.55; o=[]
for (x1,y1),(x2,y2),c1,c2 in P10: o.append(f'\\draw[line width=1.8pt,{MAVI}] ({x1*sx},{y1*sy}) -- ({x2*sx},{y2*sy});')
for (p,c) in [((-3,-2),1),((0,3),1),((2,2),1),((4,4),1),((0,1),0),((2,5),0)]:
    x,y=p; o.append(f'\\filldraw[{MAVI},fill={MAVI}] ({x*sx},{y*sy}) circle (0.1);' if c else f'\\filldraw[{MAVI},fill=white,line width=1.2pt] ({x*sx},{y*sy}) circle (0.1);')
o.append(lab(4.1,3.6,'y=f(x)',MAVI,sx,sy,'right'))
SK=fig(graf(-3,4,-2,5,sx,sy,'\n'.join(o)))
q('0010',tipId='fn2-parcali',tip='Parçalı fonksiyon',z='orta',alt='Görüntü Kümesi',kaz='Parçalı fonksiyonun grafiğinden görüntü kümesini aralıkların birleşimi olarak bulup tam sayıları sayar.',kalip='grafik',
 kart='K-AFNK2-05 (üç parçalı grafik, boş ve dolu uçlar) · parçalar [−3, 0), [0, 2), [2, 4]',
 metin='Şekilde [−3, 4] aralığında tanımlı f fonksiyonunun grafiği verilmiştir; grafik, uçları kılavuz çizgilerinin kesişiminde olan doğru parçalarından oluşmakta, içi boş noktalar ise grafiğe ait olmayan uç noktaları göstermektedir.\nBuna göre f fonksiyonunun görüntü kümesinde kaç tam sayı vardır?',
 dogru=v,yan=[(e[0],'Parçalar arasındaki boşluğu görmeden −2’den 4’e kadar tüm tam sayıları saymış.','dikkat'),(e[1],'Boş uçları da kümeye katarak 1 ve 5’i eklemiş: −2, −1, 0, 1, 2, 3, 4, 5.','dikkat'),(e[2],'[2, 5) ile [2, 4] aralıklarının birleşiminde 2’yi dışlamış: −2, −1, 0, 3, 4.','dikkat'),(e[3],'Yalnız birinci parçanın değerlerini (−2, −1, 0) sayıp diğerlerini unutmuş.','dikkat')],
 istenen='Görüntü kümesindeki tam sayıların sayısı.',ip=['Her parçanın y değerlerini bir aralık olarak yaz; uçların dolu mu boş mu olduğuna dikkat edip aralıkları birleştir.'],bilgi=[BGOR],sekil=SK,
 ad=[A('Parçaların değer aralıkları','Dolu uç dahil, boş uç hariç yazılır.','[−3, 0): [−2, 1); [0, 2): [3, 5); [2, 4]: [2, 4]'),A('Birleştir','İkinci ve üçüncü aralık [2, 5) aralığında birleşir; 1 ile 2 arasında boşluk vardır.','[−2, 1) ∪ [2, 5)'),A('Tam sayıları say','Her aralıktaki tam sayılar yazılır.','−2, −1, 0 ve 2, 3, 4 → 6')],
 puf='Görüntü kümesini sayı doğrusunda işaretle: iki aralığın arasında boşluk kalıyorsa o aradaki sayılar sayılmaz.')

# ================= 11 orta · koşullu fonksiyon sayma =================
A_=[1,2,3]; B_=[1,2,3,4]
cnt=sum(1 for t in itertools.permutations(B_,3) if t[0]!=1 and t[1]!=2)
assert cnt==14
v=cnt; e=[24,18,12,22]; assert len(list(itertools.permutations(B_,3)))==24
assert sum(1 for t in itertools.permutations(B_,3) if t[0]!=1)==18; uniq(v,e)
q('0011',tipId='fn2-sayma',tip='Koşullu fonksiyon sayma',z='orta',alt='Birebir Fonksiyon Sayısı',kaz='Bir koşulu sağlayan birebir fonksiyonların sayısını içerme–dışarma ile bulur.',kalip='düz',
 kart='K-AFNK2-07 (f(1) ≠ 1 ve f(2) ≠ 2 koşullu birebir fonksiyon) · A = {1, 2, 3}, B = {1, 2, 3, 4}',
 metin='A = {1, 2, 3} ve B = {1, 2, 3, 4} kümeleri veriliyor.\nf(1) ≠ 1 ve f(2) ≠ 2 koşullarını sağlayan birebir f: A → B fonksiyonlarının sayısı kaçtır?',
 dogru=v,yan=[(e[0],'Koşulları dikkate almayıp tüm birebir fonksiyonları saymış: 4·3·2.','dikkat'),(e[1],'Yalnız f(1) = 1 durumlarını çıkarmış: 24 − 6.','dikkat'),(e[2],'İki koşulu bozanları (6 + 6) çıkarmış, ikisini birden bozanları geri eklememiş: 24 − 12.','islem'),(e[3],'Yalnız ikisini birden bozanları (2) çıkarmış: 24 − 2.','bilgi')],
 istenen='Koşulu sağlayan birebir fonksiyon sayısı.',ip=['Tüm birebir fonksiyonların sayısından koşullardan en az birini bozanları çıkarmayı dene; çakışan durumlara dikkat et.'],bilgi=[BSAY],
 ad=[A('Tüm birebir fonksiyonlar','Üç elemanlı A’dan dört elemanlı B’ye birebir fonksiyon sayısı bulunur.','4 · 3 · 2 = 24'),A('Tek koşulu bozanlar','f(1) = 1 olanlarda kalan iki eleman 3 değerden birebir seçilir; f(2) = 2 için de aynıdır.','3 · 2 = 6 ve 6'),A('İkisini birden bozanlar','f(1) = 1 ve f(2) = 2 olanlarda kalan bir eleman 2 değer alır.','2'),A('Sonuç','Koşulu bozanlar çıkarılır, iki kez çıkarılan eklenir.','24 − 6 − 6 + 2 = 14')],
 puf='Koşulu bozan durumları çıkarırken iki koşulu birden bozanların iki kez çıkarıldığını unutma.')

# ================= 12 orta · öncüllü, ters ve bileşke grafikten =================
V12=[(0,2),(2,3),(3,5),(5,6),(6,7)]
f12=lambda x:pl(V12,x); inv12=lambda y:{y_:x for x,y_ in V12}[y]
assert f12(f12(0))==3 and inv12(inv12(6))==3 and inv12(3)+inv12(5)==5==inv12(6)
sx=sy=0.62
SK=fig(graf(0,7,0,8,sx,sy,f'\\draw[dashed,gray!80!black,line width=1.1pt] (0,0) -- ({7.4*sx},{7.4*sy}); \\node[gray!70!black,font=\\small,right] at ({1.6*sx},{0.8*sy}) {{$y=x$}};'+egri(V12,sx,sy,MAVI)+'\n'+lab(5.2,4.6,'y=f(x)',MAVI,sx,sy,'right')))
q('0012',tipId='fn2-ters',tip='Ters fonksiyon ve bileşkesi',z='orta',alt='Grafikten Ters Fonksiyon',kaz='Birebir ve örten fonksiyonun grafiğinden bileşke ve ters değerlerini okuyup öncülleri sınar.',kalip='öncüllü',
 kart='K-AFNK2-03 (grafikten f ∘ f ve f⁻¹ öncülleri) · köşeler (0, 2), (2, 3), (3, 5), (5, 6), (6, 7)',
 metin='f: [0, 6] → [2, 7] birebir ve örten fonksiyonunun grafiği şekilde verilmiştir; grafik, uçları kılavuz çizgilerinin kesişiminde olan doğru parçalarından oluşmaktadır.\nI. (f ∘ f)(0) = 3\nII. (f⁻¹ ∘ f⁻¹)(6) = 3\nIII. f⁻¹(3) + f⁻¹(5) = f⁻¹(6)\nBu ifadelerden hangileri doğrudur?',
 dogru='I, II ve III',sira=SIK12,yan=[('Yalnız I','II ve III’ü sınamadan I ile yetinmiş; oysa II’de f⁻¹(6) = 5, f⁻¹(5) = 3 ve III’te 2 + 3 = 5 = f⁻¹(6) sağlanır.','dikkat'),('Yalnız II','I’de f(0) = 2’den sonra f(2) yerine f(3) = 5’i okuyup I’i yanlış saymış; III’te de f⁻¹(5) yerine 2 okuyup III’ü yanlış saymış.','islem'),('I ve III','II’de ikinci adımda f⁻¹(5) yerine f⁻¹(3) = 2 okuyup II’yi yanlış saymış.','bilgi'),('II ve III','I’de f(2) = 3 yerine f(3) = 5 okuyup I’i yanlış saymış.','bilgi')],
 istenen='Doğru olan ifadelerin hangileri olduğu.',ip=['İçten dışa ilerle: f(…) için x’e karşılık y’yi, f⁻¹(…) için y’ye karşılık x’i okuyarak her öncülü ayrı ayrı hesapla.'],bilgi=[BTGR],sekil=SK,
 ad=[A('I’i sına','Önce f(0), sonra çıkan sayının f değeri okunur.','f(0) = 2, f(2) = 3 → I doğru'),A('II’yi sına','f⁻¹(6) için y = 6’nın apsisi, sonra bulunan değer için aynı işlem.','f⁻¹(6) = 5, f⁻¹(5) = 3 → (f⁻¹ ∘ f⁻¹)(6) = 3 → II doğru'),A('III’ü sına','Üç ters değer okunur.','f⁻¹(3) = 2, f⁻¹(5) = 3, f⁻¹(6) = 5; 2 + 3 = 5 → III doğru')],
 puf='Ters değeri bulmak için y-eksenindeki sayıdan yatay gidip grafiğe değin, oradan aşağı inerek apsisi oku.')

# ================= 13 zor · f(f(x)) en küçük değeri =================
V13=[(0,2),(1,4),(2,2),(3,0),(4,2),(5,4),(6,6)]
f13=lambda x:pl(V13,x)
X13=[x for x in (Fr(k,2) for k in range(0,13)) if f13(f13(x))==0]
assert min(f13(f13(Fr(k,4))) for k in range(0,25))==0
assert X13==[Fr(1,2),Fr(3,2),Fr(9,2)] and sum(X13)==Fr(13,2)
v=Fr(13,2); e=[3,2,6,Fr(19,2)]; assert sum(X13)-Fr(1,2)==6 and sum(X13)+3==Fr(19,2) and sum(sols(V13,3))==Fr(13,2) and sum(sols(V13,0))==3 and Fr(1,2)+Fr(3,2)==2; uniq(v,e)
sx=sy=0.62
SK=fig(graf(0,6,0,6,sx,sy,egri(V13,sx,sy,MAVI)+'\n'+lab(0.2,5.4,'y=f(x)',MAVI,sx,sy,'right')))
q('0013',tipId='fn2-bilesik',tip='Bileşke fonksiyon ve grafikli denklem',z='zor',alt='f(f(x)) En Küçük Değeri',kaz='Grafiği verilen fonksiyonun bileşkesinin en küçük değerini aldığı noktaları iki aşamada bulur.',kalip='grafik',
 kart='K-AFNK2-04 (f ∘ f en küçük değer, çözüm toplamı) · köşeler (0, 2), (1, 4), (2, 2), (3, 0), (4, 2), (5, 4), (6, 6)',
 metin='Dik koordinat düzleminde, [0, 6] aralığında tanımlı f fonksiyonunun grafiği şekilde verilmiştir. f fonksiyonunun görüntü kümesi [0, 6] aralığının bir alt kümesidir ve grafiğin köşeleri kılavuz çizgilerinin kesişim noktalarındadır.\n(f ∘ f)(x) fonksiyonu en küçük değerini x = a noktalarında almaktadır.\nBuna göre a’nın alabileceği değerlerin toplamı kaçtır?',
 dogru=v,yan=[(e[0],'Yalnız f(x) = 0 denklemini çözmüş: x = 3.','bilgi'),(e[1],'f(x) = 3 çözümlerinden yalnız ilk iki parçadakileri (1/2 ve 3/2) toplamış.','dikkat'),(e[2],'x = 1/2 çözümünü atlayıp 3/2 + 9/2 = 6 bulmuş.','dikkat'),(e[3],'Çözümlere x = 3’ü de ekleyip 13/2 + 3 bulmuş.','dikkat')],
 istenen='(f ∘ f)(x) fonksiyonunun en küçük değerini aldığı x değerlerinin toplamı.',ip=['İç fonksiyonun hangi değeri alınca dış fonksiyonun en küçük değerine ulaşıldığını grafikten bul; sonra iç fonksiyonun o değeri aldığı apsisleri oku.'],bilgi=[BFOF],sekil=SK,
 ad=[A('En küçük değer','f’nin en küçük değeri 0’dır ve x = 3’te alınır; (f ∘ f)(x) = f(f(x)) bu değere f(x) = 3 iken ulaşır.','f(x) = 3'),A('f(x) = 3 çözümleri','y = 3 doğrusu grafiği üç parçada keser.','x = 1/2, 3/2, 9/2'),A('Topla','Çözümler birbirinden farklıdır.','1/2 + 3/2 + 9/2 = 13/2')],
 puf='Dış fonksiyonun en küçük değerini aldığı apsis, iç fonksiyonun alması gereken değerdir.')

# ================= 14 orta · |f| altındaki alan =================
V14=[(0,-2),(2,2),(5,-4),(8,2)]
import math
alan=Fr(0)
for (x1,y1),(x2,y2) in zip(V14,V14[1:]):
    if y1*y2<0:
        z=Fr(x1)+Fr(-y1,y2-y1)*(x2-x1); alan+=abs(y1)*(z-x1)/2+abs(y2)*(x2-z)/2
    else: alan+=Fr(abs(y1)+abs(y2),2)*(x2-x1)
assert alan==12
imza=sum(Fr(y1+y2,2)*(x2-x1) for (x1,y1),(x2,y2) in zip(V14,V14[1:])); assert imza==-6
v=12; e=[abs(int(imza)),9,3,22]
tr=sum(Fr(abs(y1)+abs(y2),2)*(x2-x1) for (x1,y1),(x2,y2) in zip(V14,V14[1:])); assert tr==22 and e==[6,9,3,22]; uniq(v,e)
sx,sy=0.6,0.55
SK=fig(graf(0,8,-4,3,sx,sy,egri(V14,sx,sy,MAVI)+'\n'+lab(1.2,-3.3,'y=f(x)',MAVI,sx,sy,'right')))
q('0014',tipId='fn2-mutlak',tip='Mutlak değerli fonksiyonların grafiği',z='orta',alt='|f| Grafiği ve Alan',kaz='Grafiği verilen fonksiyonun mutlak değerinin x-ekseniyle arasında kalan alanı parçalayarak hesaplar.',kalip='grafik',
 kart='K-AFNK2-01 (|f| altında alan, üç eksen kesimi) · köşeler (0, −2), (2, 2), (5, −4), (8, 2)',
 metin='[0, 8] aralığında tanımlı f fonksiyonunun grafiği, birbirine bağlı doğru parçalarından oluşacak biçimde çizilmiştir; köşe noktaları kılavuz çizgilerinin kesişimindedir.\ng(x) = |f(x)| olarak tanımlandığına göre g fonksiyonunun grafiği ile x-ekseni arasında kalan bölgenin alanı kaç birimkaredir?',
 dogru=v,yan=[(e[0],'Alanları işaretli toplamış (üstteki alanlar +, alttakiler −): |3 − 9| = 6.','bilgi'),(e[1],'Yalnız x-ekseninin altında kalan alanları toplamış: 1 + 4 + 4.','dikkat'),(e[2],'Yalnız x-ekseninin üstündeki bölgelerin alanını almış: 1 + 1 + 1.','dikkat'),(e[3],'Eksenle kesişimleri (1, 3, 7) bulmadan her doğru parçasının altını yamuk alanı gibi hesaplamış.','islem')],
 istenen='g fonksiyonunun grafiği ile x-ekseni arasında kalan bölgenin alanı.',ip=['f’nin x-eksenini kestiği apsisleri bul; her parçada oluşan üçgenlerin alanını ayrı hesaplayıp pozitif olarak topla.'],bilgi=[BALN],sekil=SK,
 ad=[A('Eksen kesimleri','Doğru parçalarının x-eksenini kestiği noktalar bulunur.','x = 1, x = 3, x = 7'),A('Eksenin üstündeki bölgeler','Üç küçük üçgen oluşur: [1, 2], [2, 3] ve [7, 8] aralıklarında; her birinin tabanı 1, yüksekliği 2’dir.','1 + 1 + 1 = 3'),A('Eksenin altındaki bölgeler','Üç üçgen oluşur: [0, 1] aralığında (taban 1, yükseklik 2), [3, 5] ve [5, 7] aralıklarında (taban 2, yükseklik 4).','1 + 4 + 4 = 9'),A('Topla','Mutlak değer altta kalan alanları da pozitif yapar; alanlar toplanır.','3 + 9 = 12')],
 puf='|f|’nin alanında f’nin negatif kısmı da pozitif sayılır; x-eksenini kestiği noktalarda bölerek hesapla.')

# ================= 15 zor · g∘f ve f⁻¹ verilmiş =================
finv=lambda x:2*x-1; ff=lambda x:Fr(x+1,2); gg=lambda u:8*u-1
for x in range(-5,6): assert gg(ff(x))==4*x+3
ginv=lambda y:Fr(y+1,8)
assert ginv(23)==3 and ff(9)==5
v=ginv(23)+ff(9); assert v==8
e=[Fr(23-3,4)+5, Fr(23-5,2)+(2*9-1), 3+finv(9), ginv(23)*ff(9)]
e=[int(x) for x in e]; assert e==[10,26,20,15],e; uniq(v,e)
q('0015',tipId='fn2-ters',tip='Ters fonksiyon ve bileşkesi',z='zor',alt='Bileşke ve Terslerle Fonksiyon Bulma',kaz='Bir fonksiyonun tersi ile bileşkesi verildiğinde diğer fonksiyonu bulup ters değerini hesaplar.',kalip='düz',
 kart='K-AFNK2-03 (f⁻¹ ve g ∘ f verilmiş, g⁻¹ isteniyor) · f⁻¹(x) = 2x − 1, (g ∘ f)(x) = 4x + 3',
 metin='Gerçel sayılar kümesi üzerinde tanımlı birebir ve örten f ve g fonksiyonları için\nf⁻¹(x) = 2x − 1\n(g ∘ f)(x) = 4x + 3\neşitlikleri veriliyor.\nBuna göre g⁻¹(23) + f(9) toplamı kaçtır?',
 dogru=int(v),yan=[(e[0],'g(f(x)) ifadesini g(x) sanıp g⁻¹(23) = (23 − 3)/4 = 5 bulmuş: 5 + 5 = 10.','bilgi'),(e[1],'f⁻¹ ile f’yi karıştırıp f(x) = 2x − 1 almış: g(u) = 2u + 5, g⁻¹(23) = 9 ve f(9) = 17; 9 + 17 = 26.','bilgi'),(e[2],'f(9) yerine f⁻¹(9) = 17 almış: g⁻¹(23) = 3 olduğundan 3 + 17 = 20.','dikkat'),(e[3],'Toplamak yerine çarpmış: 3 · 5 = 15.','dikkat')],
 istenen='g⁻¹(23) + f(9) toplamı.',ip=['(g ∘ f)(x) = 6x + 1 ifadesinde u = f(x) yazıp x’i f⁻¹ yardımıyla u cinsinden ifade ederek g’nin kuralını bul.'],bilgi=[BTRB],
 ad=[A('f’yi bul','f⁻¹(x) = 2x − 1 ise f(x) için y = 2x − 1’den x çekilir.','f(x) = (x + 1)/2'),A('g’yi bul','u = f(x) için x = f⁻¹(u) = 2u − 1 olur; bu değer 4x + 3’te yerine yazılır.','g(u) = 4(2u − 1) + 3 = 8u − 1'),A('g⁻¹(23)','g(u) = 23 denklemi çözülür.','8u − 1 = 23 → u = 3'),A('f(9)','f(x) = (x + 1)/2’de x = 9.','(9 + 1)/2 = 5'),A('Topla','İki değer toplanır.','3 + 5 = 8')],
 puf='g⁻¹(23) = a demek g(a) = 23 demektir; önce g’nin kuralını bulup a’yı denklemle çöz.')

# ================= 16 zor · x ve 1/x dönüşümlü fonksiyonel denklem =================
f16=lambda x:2*x+Fr(1)/x
for x in (Fr(1,2),2,3,Fr(-1,3)): assert 2*f16(x)+f16(1/x)==5*x+4/x
u=Fr(3); vv=Fr(9,2); assert 2*u+vv==Fr(21,2) and 2*vv+u==12
assert f16(Fr(1,2))==3 and f16(2)==vv
assert Fr(21,2)/3==Fr(7,2) and u-vv==Fr(-3,2) and u+vv==Fr(15,2)
v=3; e=[Fr(7,2),Fr(9,2),Fr(-3,2),Fr(15,2)]; uniq(v,e)
q('0016',tipId='fn2-fonkdenk',tip='Dönüşümlü fonksiyonel denklem',z='zor',alt='f(x) ve f(1/x) Denklemi',kaz='x ve 1/x için yazılan iki eşitlikten oluşan sistemi çözerek fonksiyonun bir değerini bulur.',kalip='düz',
 kart='K-AFNK2-08 (2f(x) + f(1/x) = 5x + 4/x) · f(1/2)',
 metin='Sıfırdan farklı gerçel sayılar kümesi üzerinde tanımlı bir f fonksiyonu, her x ≠ 0 gerçel sayısı için\n2·f(x) + f(1/x) = 5x + 4/x\neşitliğini sağlamaktadır.\nBuna göre f(1/2) değeri kaçtır?',
 dogru=v,yan=[(e[0],'f(2) = f(1/2) alarak tek denklem kurmuş: 3·f(1/2) = 21/2.','bilgi'),(e[1],'Sistemi çözüp f(2) = 9/2’yi bulmuş, istenen f(1/2) yerine f(2)’yi yazmış.','dikkat'),(e[2],'İki denklemi taraf tarafa çıkarıp f(1/2) − f(2) = −3/2 farkını cevap sanmış.','dikkat'),(e[3],'İki denklemi toplayıp 3’e bölerek f(1/2) + f(2) = 15/2 toplamını bulmuş.','dikkat')],
 istenen='f(1/2) değeri.',ip=['Eşitlikte x = 1/2 ve x = 2 yazarak f(1/2) ve f(2) için iki denklem kur.'],bilgi=[BFDN],
 ad=[A('x = 1/2 yaz','1/x = 2 olur.','2f(1/2) + f(2) = 5/2 + 8 = 21/2'),A('x = 2 yaz','1/x = 1/2 olur.','2f(2) + f(1/2) = 10 + 2 = 12'),A('Sistemi çöz','İkinci denklemden f(2) çekilip birincide yerine yazılır.','f(2) = (12 − f(1/2))/2 → 2f(1/2) + 6 − f(1/2)/2 = 21/2 → f(1/2) = 3'),A('Kontrol','Bulunan değer ikinci denklemde sınanır.','f(2) = 9/2; 9 + 3 = 12')],
 puf='İki bilinmeyen, f(x) ve f(1/x); x ile 1/x’i sırayla yazmak iki bilinmeyenli iki denklem verir.')

# ================= 17 zor · |f(|x|)| = 1 =================
V17=[(0,2),(1,-1),(3,1),(4,-2)]
def h17(x): return abs(pl(V17,abs(x)))
pos=sols(V17,1)|sols(V17,-1); assert sorted(pos)==[Fr(1,3),1,3,Fr(11,3)]
tum={x for x in pos}|{-x for x in pos}; assert len(tum)==8
v=8; e=[4,5,6,7]; uniq(v,e)
sx=sy=0.7
SK=fig(graf(0,4,-2,3,sx,sy,egri(V17,sx,sy,MAVI)+'\n'+lab(0.1,2.55,'y=f(x)',MAVI,sx,sy,'right')))
q('0017',tipId='fn2-mutlak',tip='Mutlak değerli fonksiyonların grafiği',z='zor',alt='|f(|x|)| = k Denklemi',kaz='Grafiği yalnız x ≥ 0 için verilen fonksiyonla kurulan iki mutlak değerli ifadenin denklem çözüm sayısını bulur.',kalip='grafik',
 kart='K-AFNK2-01 (f(|x|) ve |f| birlikte, teğet noktalı) · köşeler (0, 2), (1, −1), (3, 1), (4, −2)',
 metin='Köşeleri kılavuz çizgilerinin kesişiminde olan kırık çizgiden oluşan f fonksiyonu [0, 4] aralığında tanımlıdır ve grafiği şekilde verilmiştir.\ng(x) = |f(|x|)| kuralıyla [−4, 4] aralığında tanımlanan g fonksiyonu için g(x) = 1 denkleminin kaç farklı çözümü vardır?',
 dogru=v,yan=[(e[0],'Yalnız x ≥ 0 olan çözümleri saymış: 1/3, 1, 3 ve 11/3.','dikkat'),(e[1],'x ≥ 0 için 4 çözüm bulup x = 0’ı da çözüm sayarak 5 bulmuş (oysa g(0) = 2’dir).','dikkat'),(e[2],'x = 1 teğet noktasını saymayıp x ≥ 0 için 3 çözüm bulmuş ve ikiyle çarpmış.','dikkat'),(e[3],'Simetriyi uygularken x = 3’ün karşılığı olan x = −3’ü atlamış: 4 + 3 = 7.','dikkat')],
 istenen='g(x) = 1 denkleminin farklı çözüm sayısı.',ip=['x ≥ 0 için |f(x)| = 1 denklemini iki ayrı denkleme ayır, grafikten çözümleri say; çift fonksiyon özelliğini kullanarak negatif tarafı ekle.'],bilgi=[BMUT,BYAT],sekil=SK,
 ad=[A('x ≥ 0 için','|f(x)| = 1 denklemi f(x) = 1 ve f(x) = −1 denklemlerine ayrılır.','f(x) = 1 ve f(x) = −1'),A('f(x) = 1','y = 1 doğrusu grafiği x = 1/3 civarında (birinci parçada) ve x = 3 tepe noktasında keser.','2 çözüm (1/3 ve 3)'),A('f(x) = −1','y = −1 doğrusu grafiği x = 1 (tepe noktasına değer) ve üçüncü parçada keser.','2 çözüm (1 ve 11/3)'),A('Negatif taraf','g(−x) = g(x) olduğundan her pozitif çözümün karşılığı vardır; x = 0 çözüm değildir.','4 · 2 = 8')],
 puf='f(|x|) çift fonksiyondur: yalnız pozitif tarafı çöz, sonra çözüm sayısını iki katına çık (x = 0 çözüm değilse).')

# ================= 18 zor · çift ve periyodik =================
V18=[(0,1),(1,3),(2,-1),(3,2)]
fb18=lambda x:(lambda r:(pl(V18,r) if r<=3 else pl(V18,6-r)))(Fr(x)%6)
for x in range(-20,20): assert fb18(x)==fb18(-x) and fb18(x)==fb18(x+6)
v=fb18(-7)+fb18(20)+fb18(2025); assert (fb18(-7),fb18(20),fb18(2025),v)==(3,-1,2,4)
e=[-2,-1,0,2]; uniq(v,e)
sx,sy=1.2,0.62
SK=fig(graf(0,3,-1,4,sx,sy,egri(V18,sx,sy,MAVI)+'\n'+lab(0.1,3.6,'y=f(x)',MAVI,sx,sy,'right')))
q('0018',tipId='fn2-grafikoku',tip='Grafikten özellik okuma',z='zor',alt='Çift ve Periyodik Fonksiyon',kaz='Çift ve periyodik olan fonksiyonun bir aralıktaki grafiğinden büyük apsisli değerlerini hesaplar.',kalip='grafik',
 kart='K-AFNK2-06 (çift, periyot 6, [0, 3] grafiği) · köşeler (0, 1), (1, 3), (2, −1), (3, 2)',
 metin='Gerçel sayılar kümesi üzerinde tanımlı bir f fonksiyonu çift fonksiyondur ve her x gerçel sayısı için f(x + 6) = f(x) eşitliğini sağlamaktadır. f fonksiyonunun [0, 3] aralığındaki grafiği, köşeleri kılavuz çizgilerinin kesişiminde olan kırık çizgi olarak şekilde verilmiştir.\nBuna göre f(−7) + f(20) + f(2025) toplamı kaçtır?',
 dogru=v,yan=[(e[0],'f(−7) için çift fonksiyon özelliğini bir işaret değişimi sanmış: −f(1) = −3; −3 − 1 + 2 = −2.','bilgi'),(e[1],'Periyodu 3 sanmış: f(−7) = f(2) = −1, f(20) = f(2) = −1, f(2025) = f(0) = 1; toplam −1.','islem'),(e[2],'f(−7) için f(5)’i [0, 3] dışında kalan değer sayıp grafikten f(5 − 3) = f(2) = −1 okumuş: −1 − 1 + 2 = 0.','islem'),(e[3],'f(−7) terimini hesaba katmayıp yalnız f(20) + f(2025) = −1 + 2 toplamını yazmış.','dikkat')],
 istenen='f(−7) + f(20) + f(2025) toplamı.',ip=['Her sayıyı 6’nın katını ekleyip çıkararak [−3, 3] aralığına indir; negatif kalanlarda çift fonksiyon özelliğini kullan.'],bilgi=[BPER],sekil=SK,
 ad=[A('f(−7)','−7’ye 12 eklenir; f(5) = f(−1) = f(1) olur.','f(−7) = f(5) = f(−1) = f(1) = 3'),A('f(20)','20’den 18 çıkarılır.','f(20) = f(2) = −1'),A('f(2025)','2025 = 6·337 + 3 olduğundan 2022 atılır.','f(2025) = f(3) = 2'),A('Topla','Üç değer toplanır.','3 − 1 + 2 = 4')],
 puf='Periyotla büyük sayıyı küçült; [−3, 3] dışında kalırsa bir periyot daha ekle ya da çıkar, negatif apsisleri de çift olma özelliğiyle pozitife çevir.')

# ================= 19 zor · (f ∘ g)(x) = 3 iki grafik =================
V19f=[(0,3),(1,4),(2,6),(3,5),(4,4),(5,3),(6,0)]; V19g=[(0,0),(1,2),(2,3),(3,5),(4,3),(5,0),(6,5)]
U=sols(V19f,3); assert U=={0,5}
X=set()
for u in U: X|=sols(V19g,u)
assert X=={0,3,5,6} and sum(X)==14
fg=lambda x:pl(V19f,pl(V19g,x)); assert sorted(x for x in range(0,7) if fg(x)==3)==[0,3,5,6]
assert [x for x in (Fr(k,2) for k in range(0,13)) if fg(x)==3]==[0,3,5,6]
v=14; e=[5,8,9,19]; uniq(v,e)
sx=sy=0.62
SK=fig(graf(0,6,0,6,sx,sy,egri(V19f,sx,sy,MAVI)+egri(V19g,sx,sy,TUR,nokta=True)+'\n'+lab(2.2,6.4,'y=f(x)',MAVI,sx,sy,'right')+lab(5.9,5.6,'y=g(x)',TUR,sx,sy,'left')))
q('0019',tipId='fn2-bilesik',tip='Bileşke fonksiyon ve grafikli denklem',z='zor',alt='İki Grafikle Bileşke Denklemi',kaz='İki fonksiyonun grafiğiyle kurulan bileşke denkleminin çözümlerini iki aşamada bulur.',kalip='grafik',
 kart='K-AFNK2-04 (f ∘ g iki grafik) · f: (0, 3), (1, 4), (2, 6), (3, 5), (4, 4), (5, 3), (6, 0); g: (0, 0), (1, 2), (2, 3), (3, 5), (4, 3), (5, 0), (6, 5)',
 metin='Şekilde [0, 6] aralığında tanımlı f ve g fonksiyonlarının grafikleri verilmiştir; grafikler, uçları kılavuz çizgilerinin kesişiminde olan doğru parçalarından oluşmaktadır.\nBuna göre (f ∘ g)(x) = 3 denkleminin çözüm kümesindeki elemanların toplamı kaçtır?',
 dogru=v,yan=[(e[0],'Yalnız g(x) = 0 çözümlerini (0 ve 5) toplamış.','dikkat'),(e[1],'x = 6’yı tanım kümesinin ucu sanıp dışarıda bırakmış: 0 + 3 + 5.','dikkat'),(e[2],'Yalnız g(x) = 5 çözümlerini (3 ve 6) toplamış.','dikkat'),(e[3],'x = 5 çözümünü hem g(x) = 0 hem de ayrı bir u için iki kez sayıp 14 + 5 bulmuş.','islem')],
 istenen='(f ∘ g)(x) = 3 denkleminin çözümlerinin toplamı.',ip=['g(x) = u diyerek önce f(u) = 3 olan u değerlerini f’nin grafiğinden bul; sonra her u için g(x) = u çözümlerini g’nin grafiğinden oku.'],bilgi=[BFOF],sekil=SK,
 ad=[A('u değerleri','f(u) = 3 için y = 3 doğrusu f’nin grafiğini iki noktada keser.','u = 0 ve u = 5'),A('g(x) = 0','y = 0 doğrusu g’nin grafiğini iki noktada keser.','x = 0 ve x = 5'),A('g(x) = 5','y = 5 doğrusu g’nin grafiğini iki noktada keser.','x = 3 ve x = 6'),A('Topla','Çözümler birbirinden farklıdır.','0 + 5 + 3 + 6 = 14')],
 puf='Bileşke denklemde önce dıştaki fonksiyonun grafiğiyle iç değerleri bul; sonra iç fonksiyonun grafiğine geç.')

# ================= 20 zor · h(x) = 3 − f(3 − x) =================
V20=[(-4,-1),(-3,1),(-2,3),(-1,1),(0,3),(1,0),(2,3),(3,4),(4,3)]
S20=sols(V20,3); assert S20=={-2,0,2,4}
Z={3-s for s in S20}; assert Z=={5,3,1,-1} and sum(Z)==8
assert all(-4<=3-z<=4 for z in Z)
v=8; e=[4,16,-8,12]; assert sum(S20)==4 and sum(3+s for s in S20)==16 and sum(s-3 for s in S20)==-8 and 3*len(S20)==12; uniq(v,e)
sx=sy=0.62
SK=fig(graf(-4,4,-2,5,sx,sy,egri(V20,sx,sy,MAVI)+'\n'+lab(-3.9,4.4,'y=f(x)',MAVI,sx,sy,'right')))
q('0020',tipId='fn2-donusum',tip='Grafik dönüşümleri ve katsayı işaretleri',z='zor',alt='Yansıma ve Ötelemeyle Kökler',kaz='Yansıma ve öteleme içeren dönüşümün x-eksenini kestiği noktaları f’nin grafiğinden hesaplar.',kalip='grafik',
 kart='K-AFNK2-02 (h(x) = 3 − f(3 − x) sıfırları) · köşeler (−4, −1), (−3, 1), (−2, 3), (−1, 1), (0, 3), (1, 0), (2, 3), (3, 4), (4, 3)',
 metin='[−4, 4] aralığında tanımlı f fonksiyonunun grafiği şekilde verilmiştir; grafiğin köşeleri kılavuz çizgilerinin kesişim noktalarındadır.\nh(x) = 3 − f(3 − x) kuralıyla tanımlanan h fonksiyonunun grafiğinin x-eksenini kestiği noktaların apsisleri toplamı kaçtır?',
 dogru=v,yan=[(e[0],'Dönüşümü uygulamayıp f(x) = 3 çözümlerinin toplamını almış: −2 + 0 + 2 + 4.','bilgi'),(e[1],'3 − x = s yerine x = 3 + s yazıp işareti ters çevirmiş: 3 + (−2) + 3 + 0 + 3 + 2 + 3 + 4.','islem'),(e[2],'x = s − 3 kullanmış (yansımayı unutup yalnız öteleme): (−5) + (−3) + (−1) + 1.','bilgi'),(e[3],'Kökleri 3 − s yerine yalnız 3 alıp dört kök için 3·4 yazmış.','dikkat')],
 istenen='h fonksiyonunun grafiğinin x-eksenini kestiği noktaların apsisleri toplamı.',ip=['h(x) = 0 eşitliğini f ile ifade et; f’nin hangi değeri alması gerektiğini ve bu değeri aldığı apsisleri grafikten oku.'],bilgi=[BYAN,BYAT],sekil=SK,
 ad=[A('Denklemi kur','h(x) = 0 için 3 − f(3 − x) = 0 olmalıdır.','f(3 − x) = 3'),A('f(t) = 3 çözümleri','t = 3 − x olsun; y = 3 doğrusu grafiği (tepe noktalarına değen yerler dahil) dört noktada keser.','t = −2, 0, 2, 4'),A('x değerleri','x = 3 − t formülüyle her t için x bulunur.','x = 5, 3, 1, −1'),A('Topla','Dört kök toplanır.','5 + 3 + 1 + (−1) = 8')],
 puf='3 − x ifadesi önce x’i işaret değiştirip sonra 3 birim kaydırır: t = 3 − x ise x = 3 − t’dir.')

# ---------------- bitir ----------------
for q_ in P.ANA: q_['kardes']=None
P.yaz(os.path.join(HD,'fonksiki-1.json'),'/tmp/bos-fonksiki.json')
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=UK))['kartlar'].append(c['id'])
json.dump(dict(konu='Fonksiyonlar',surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 AYT Matematik çıkmış fonksiyon soruları ve yayın soru bankaları (yalnız mantık), MEB 11–12. sınıf müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','fonksiki.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
