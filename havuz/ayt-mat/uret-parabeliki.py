"""AYT Matematik · Parabol 2. dalga (20 soru: 3 kolay / 10 orta / 7 zor). Her doğru ve çeldirici değer kodla hesaplanıp assert edilir. Kardeş yok, ipucu 1."""
import sys,os,json,math
AD=os.path.dirname(os.path.abspath(__file__)); HD=AD
sys.path.insert(0,os.path.join(HD,'..','tyt-mat')); sys.path.insert(0,os.path.join(HD,'..'))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
HD=AD
H.KONU='Parabol'
UK='amat|Parabol'
P=Parti('parabeliki','Parabol',UK,ders='AYT Matematik',idon='aytmat')
KY='ÖSYM 2018–2026 AYT Matematik (parabol, ikinci dereceden fonksiyon soruları; yalnız mantık) · MEB 10–11. sınıf'
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)
TICKS=[]
def fig(body,font='\\small'):
    t='\n'.join(TICKS); TICKS.clear()
    return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font='+font+']\n'+body+'\n'+t+'\n\\end{tikzpicture}')
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)

OKU=B('Grafikten ve tablodan okuma','Grafikte ya da tabloda verilen nokta, kök ve tepe bilgileri ile parabolün denklemi yazılır; tepe noktası biliniyorsa f(x) = a(x − r)² + k yazılır; a ise bir başka noktadan bulunur. Örnek: tepe noktası (2, 1) ve (0, 5) noktasından geçen parabol f(x) = (x − 2)² + 1 olur')
YAT=B('Yatay doğru ve parabol','y = k doğrusunun parabolle kesiştiği noktaların apsisleri f(x) = k denkleminin köklerinin; teğet olduğu noktanın apsisi ise tepe apsisidir. Örnek: f(x) = x² − 6x + 10 için f(x) = 1 denkleminin çift kökü x = 3’tür; y = 1 doğrusu parabole teğettir')
TEG=B('Teğetlik ve ortak nokta','İki grafiğin ortak noktaları f(x) = g(x) denkleminin köklerindir; tam bir ortak nokta varsa grafikler teğettir ve denklemin Δ değeri sıfırdır. Parabolün x eksenine teğet olması için Δ = 0, tepe noktasının ordinatının sıfır olması gerekir. Örnek: x² + 4x + n = 0 denkleminde Δ = 16 − 4n = 0 ise n = 4 olur')
UCG=B('Köşeleri koordinatla verilen şekillerin alanı','Üçgenin bir kenarı x ekseni ya da bir eksene paralel ise alan = (taban × yükseklik)/2 olup yükseklik karşı köşenin ordinatının mutlak değeridir. Örnek: (0, 0), (5, 0), (2, 3) köşeli üçgenin alanı 5 · 3/2 = 15/2’dir')
ESI=B('Grafikle eşitsizlik ve oran','Grafiği verilen f ve g için f(x)/g(x) ≥ 0 eşitsizliğinde f ve g’nin işaretleri ayrı ayrı okunur, g(x) = 0 olan nokta çözüme alınmaz. f(x) > g(x) çözümü, f grafiğinin g grafiğinin üstünde kaldığı apsislerdir. Örnek: f(x) = (x − 1)(x − 4) için f(x) < 0 çözümü 1 < x < 4’tür')
GOR=B('Kapalı aralıkta görüntü kümesi','f ikinci dereceden bir fonksiyon iken [m, n] aralığındaki en küçük ve en büyük değer; uç noktalardaki değerler ile tepe noktası aralığın içindeyse tepe ordinatı arasından seçilir. |f(x)| = m denkleminin kök sayısı, f(x) = m ve f(x) = −m denklemlerinin kökleri birlikte sayılarak bulunur. Örnek: f(x) = x² − 2x için [0, 3] aralığında en küçük değer −1, en büyük değer 3’tür')
UYG=B('Kâr ve yörünge uygulamaları','Miktar ve fiyatın bağlı olduğu durumlarda gelir = (birim fiyat) × (satış adedi) ikinci dereceden bir ifadedir; en büyük değeri tepe noktasında alınır. Cismin yörüngesi parabol ise koordinat sistemi, tepe noktası ya da bir köşe orijinde olacak biçimde seçilip f(x) = a(x − r)² + k yazılır. Örnek: f(x) = −2x² + 12x + 5 ifadesi x = 3’te en büyük değerini alır')
KON=B('Parametreli parabolde konum','Parabolün tepe noktası T(r, k) için r = −b/(2a) ve k = f(r) olup parametre içeren denklemlerde T, parametreye bağlı bir noktadır; T’nin bir doğru üzerinde olması bu doğrunun denklemini sağlaması demektir. Eksen konumunu değiştirmek parabolün kendisini değil yalnız a, b, c işaretlerini değiştirir: tepe apsisi y eksenine göre sağdaysa a · b < 0 olur. Örnek: f(x) = x² − 4tx + t için T(2t, t − 4t²)’dir')

kartla('K-APAR2-01','Grafik ve tablodan fonksiyon değeri','Grafikteki ya da tablodaki veriler bir denklem kurmak için kullanılır; sonra istenen değer ya da tepe bulunur.','Köklerin işaretini ters yazmak; baş katsayıyı 1 almak; y kesim noktasını baş katsayı sanmak.','kolay','grafik',3,'par-oku','Grafik ve tablodan okuma')
kartla('K-APAR2-02','Yatay doğru ve parabol','Yatay doğrunun kesim ve teğet noktalarındaki bilgiler parabolün denklemini belirler; denklem yazılıp istenen değer bulunur.','Kesim noktaları arasının tamamını yarı genişlik sanmak; teğet noktasını kök saymak; baş katsayının işaretini yanlış almak.','orta','grafik',4,'par-yatay','Yatay doğru ve parabol')
kartla('K-APAR2-03','Teğetlik ve ortak nokta sayısı','Denklemler eşitlenir; tam bir ortak nokta için Δ = 0 yazılır, bulunan değerler koşullara (işaret, konum) göre elenir ve teğet noktası kökten bulunur.','Δ = 0 yerine Δ > 0 yazmak; her iki parametre değerini de almak; teğet noktasının apsisi ile ordinatını karıştırmak.','zor','grafik',4,'par-teget','Teğetlik ve ortak nokta sayısı')
kartla('K-APAR2-04','Parabolle oluşan şekillerin alanı','Kök ve tepe noktaları koordinatla belirlenir; taban ve yükseklik ayrı bulunur; hareketli noktada alan ifadesi bir değişkenli ikinci dereceden yazılıp aralığa göre en büyük değeri alınır.','Yarıyı unutmak; baş katsayıyı 1 almak; tepe noktasının aralığın dışında kaldığını gözden kaçırmak.','zor','şekilli',4,'par-ucgen','Parabolle oluşan şekillerin alanı')
kartla('K-APAR2-05','Grafikle eşitsizlik ve oran','f ve g’nin işaret çizelgesi grafikten okunur; bölüm için paydayı sıfır yapan nokta çözümden çıkarılır; sonra aralıktaki tam sayılar listelenir.','Payda sıfır olan noktayı almak; eşitsizlik yönünü karıştırmak; yalnız parabolün işaretine bakmak.','zor','grafik',4,'par-esitsiz','Grafikle eşitsizlik ve oran')
kartla('K-APAR2-06','Kapalı aralıkta görüntü ve mutlak değer','Aralığın uç değerleri ve tepenin aralıkta olup olmadığı birlikte değerlendirilir; |f| için grafiğin x ekseninin altı yukarı katlanır ve y = m doğrusunun kesim sayısı sayılır.','Yalnız uç noktaları almak; tepe ordinatını aralığa dahil saymak; teğet olduğu m değerinde kök sayısını yanlış saymak.','orta','öncüllü',4,'par-goruntu','Kapalı aralıkta görüntü ve mutlak değer')
kartla('K-APAR2-07','Gelir ve yörünge uygulaması','Durum tek değişkenli ikinci dereceden bir ifadeye çevrilir; en büyük değer ya da yere düşme noktası denklemden bulunur; koordinat sistemi uygun seçilir.','Fiyat ve adedi yanlış bağlamak; tepe apsisini cevap sanmak; yatay uzaklığı simetriden hesaplayıp başlangıç yüksekliğini unutmak.','orta','hikâyeli',4,'par-uygulama','Gelir ve yörünge uygulaması')
kartla('K-APAR2-08','Parametreli parabolde konum','Tepe noktası parametreye bağlı yazılır ve koşul (doğru üzerinde olma, eksene göre konum) denkleme çevrilir; a, b, c işaretleri konumdan okunur.','Tepe ordinatını yanlış formülle yazmak; kökleri yalnız pozitif almak; eksen konumunun işaretlere etkisini ters yorumlamak.','zor','şekilli',4,'par-konum','Parametreli parabolde konum')

# ================= şekil yardımcıları =================
MAVI='blue!70!black'; TUR='orange!85!black'; YES='green!50!black'; MOR='violet!80!black'; KIR='red!70!black'
def axes(x0,x1,y0,y1,sx,sy,xs=1,ys=1,xl='$x$',yl='$y$',nums=True,gridy=True,ytick=None,fs='\\footnotesize',xext=0.8,yext=0.8):
    o=[]
    for i in range(x0,x1+1,xs): o.append(f'\\draw[gray!35,thin] ({i*sx:.3f},{y0*sy:.3f}) -- ({i*sx:.3f},{y1*sy:.3f});')
    if gridy:
        for j in range(y0,y1+1,ys): o.append(f'\\draw[gray!35,thin] ({x0*sx:.3f},{j*sy:.3f}) -- ({x1*sx:.3f},{j*sy:.3f});')
    o.append(f'\\draw[-{{Stealth}},thick] ({(x0-0.4)*sx:.3f},0) -- ({(x1+xext)*sx:.3f},0) node[right] {{{xl}}};')
    o.append(f'\\draw[-{{Stealth}},thick] (0,{(y0-0.4*ys)*sy:.3f}) -- (0,{(y1+yext*ys)*sy:.3f}) node[above] {{{yl}}};')
    if nums:
        for i in range(x0,x1+1,xs):
            if i!=0: TICKS.append(f'\\node[below=7pt,font={fs},fill=white,fill opacity=0.85,text opacity=1,inner sep=0.6pt] at ({i*sx:.3f},0) {{${i}$}};')
        yt=range(y0,y1+1,ys) if ytick is None else ytick
        for j in yt:
            if j!=0: TICKS.append(f'\\node[left=3pt,font={fs},fill=white,fill opacity=0.85,text opacity=1,inner sep=0.6pt] at (0,{j*sy:.3f}) {{${j}$}};')
    o.append(f'\\node[above left,font={fs}] at (0,0) {{$O$}};')
    return '\n'.join(o)
def curve(f,xa,xb,sx,sy,col,ymin,ymax,w='very thick',extra=''):
    N=600; pts=[]
    for k in range(N+1):
        x=xa+(xb-xa)*k/N; y=float(f(x))
        if ymin-1e-9<=y<=ymax+1e-9: pts.append((x,y))
    assert pts
    st=max(1,len(pts)//70); sel=pts[::st]
    if sel[-1]!=pts[-1]: sel.append(pts[-1])
    co=' '.join(f'({x*sx:.3f},{y*sy:.3f})' for x,y in sel)
    return f'\\draw[{col},{w}{extra}] plot[smooth] coordinates {{{co}}};'
def dot(x,y,sx,sy,col='black',r=0.075): return f'\\fill[{col}] ({x*sx:.3f},{y*sy:.3f}) circle ({r});'
def lab(x,y,sx,sy,txt,pos='above',col='black',fs='\\footnotesize'): return f'\\node[{pos},font={fs},text={col}] at ({x*sx:.3f},{y*sy:.3f}) {{{txt}}};'

SIRA1=['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III']
SIRA2=['Yalnız I','Yalnız III','I ve II','II ve III','I, II ve III']
def ad_(L): return ('Yalnız '+L[0]) if len(L)==1 else (' ve '.join(L) if len(L)==2 else ', '.join(L[:-1])+' ve '+L[-1])

def poly(pts,sx,sy,col): return '\\fill['+col+'] '+' -- '.join(f'({x*sx:.3f},{y*sy:.3f})' for x,y in pts)+' -- cycle;'
def seg(x1,y1,x2,y2,sx,sy,col='gray',extra=''): return f'\\draw[{col}{extra}] ({x1*sx:.3f},{y1*sy:.3f}) -- ({x2*sx:.3f},{y2*sy:.3f});'

# ================= 01 kolay · grafikten f(2) =================
f1=lambda x:-x*x-2*x+3
assert f1(-3)==0 and f1(1)==0 and f1(0)==3
v=f1(2); assert v==-5
a_=lambda a,r1,r2,x:a*(x-r1)*(x-r2)
e=[a_(-1,3,-1,2),f1(-1),a_(1,-3,1,2),a_(3,-3,1,2)]
assert e==[3,4,5,15] and len({v,*e})==5
sx=sy=0.55
body=axes(-5,3,-6,5,sx,sy)+'\n'+curve(f1,-4.4,2.4,sx,sy,MAVI,-6.2,4.6)+'\n'+dot(-3,0,sx,sy)+dot(1,0,sx,sy)+dot(0,3,sx,sy)+lab(-3.5,3.8,sx,sy,'$y=f(x)$','left',MAVI)
q('0001',tipId='par-oku',tip='Grafik ve tablodan okuma',z='kolay',alt='Grafikten Değer',kaz='Grafikte işaretli üç noktadan parabolün denklemini yazıp istenen fonksiyon değerini hesaplar.',kalip='grafik',
 kart='K-APAR2-01 (grafikten f(a)) · iki kök ve y kesim noktası',
 metin='Şekilde, gerçel sayılar kümesi üzerinde tanımlı f fonksiyonunun grafiği olan parabol verilmiştir. Parabol, işaretli üç noktadan geçmekte olup bu noktalar ızgara çizgilerinin kesişimindedir.\nBuna göre f(2) kaçtır?',
 dogru=v,yan=[(e[0],'Kökleri ters okuyup f(x) = a(x − 3)(x + 1) yazmış; a = −1 ile f(2) = −(−1)(3) hesaplamış.','dikkat'),(e[1],'f(2) yerine tepe apsisi olan −1’i yerine koymuş: f(−1) = 4.','dikkat'),(e[2],'y eksenini kestiği noktanın ordinatından a’nın işaretini alamayıp a = 1 yazmış: (x + 3)(x − 1) ifadesinde x = 2.','islem'),(e[3],'y eksenini kestiği noktanın ordinatını baş katsayı sanmış: 3(x + 3)(x − 1) ifadesinde x = 2.','dikkat')],
 istenen='f(2) değeri.',ip=['Parabolün x eksenini kestiği noktaları kullan.'],bilgi=[OKU],sekil=fig(body),
 ad=[A('Kökleri oku','Parabol x eksenini iki ızgara noktasında keser.','x = −3 ve x = 1'),A('a’yı bul','f(x) = a(x + 3)(x − 1) ve f(0) = 3.','−3a = 3 → a = −1'),A('Değeri hesapla','x = 2 yazılır.','f(2) = −(5)(1) = −5')],
 puf='Bulduğun denklemi grafikteki üçüncü noktada da dene.')

# ================= 02 kolay · tablo, en küçük değer =================
f2=lambda x:x*x-4*x+5
assert (f2(0),f2(1),f2(4))==(5,2,5)
# f(0)=f(4) -> tepe apsisi 2; f=a(x-2)^2+k
a2=Fr(f2(0)-f2(1),4-1); assert a2==1
v=f2(1)-a2*1; assert v==1
e=[2,5,f2(1)-(f2(0)-f2(1)),f2(0)-f2(1)]
assert e==[2,5,-1,3] and len({v,*e})==5
q('0002',tipId='par-oku',tip='Grafik ve tablodan okuma',z='kolay',alt='Tablodan Tepe',kaz='Tabloda verilen simetrik değerlerden tepe apsisini bulur ve parabolün en küçük değerini hesaplar.',kalip='tablo',
 kart='K-APAR2-01 (tablo, simetri) · f(0) = f(4) ve f(1)',
 metin='Aşağıdaki tabloda, grafiği parabol olan ve kolları yukarı doğru olan f fonksiyonunun bazı x değerleri için aldığı değerler verilmiştir.\nBuna göre f fonksiyonunun alabileceği en küçük değer kaçtır?',
 dogru=v,yan=[(e[0],'Tablodaki en küçük değer olan f(1) = 2’yi parabolün en küçük değeri sanmış.','dikkat'),(e[1],'Tablodaki f(0) = f(4) değerini tepe ordinatı sanmış.','dikkat'),(e[2],'Baş katsayıyı f(0) − f(1) = 3 alıp k = 2 − 3 hesaplamış; (x − 2)² farkını katmamış.','islem'),(e[3],'Tepe ordinatını f(0) − f(1) = 5 − 2 farkı olarak almış.','islem')],
 istenen='f fonksiyonunun en küçük değeri.',ip=['f(0) ve f(4) arasındaki ilişkiyi düşün.'],bilgi=[OKU],
 sekil=tablo_svg(['x','0','1','4'],[['f(x)','5','2','5']]),
 ad=[A('Simetri ekseni','f(0) = f(4) olduğundan tepe apsisi ortadadır.','x = 2'),A('Tepe biçimi','f(x) = a(x − 2)² + k yazılır, iki değer kullanılır.','4a + k = 5 ve a + k = 2 → a = 1, k = 1'),A('En küçük değer','Kollar yukarı, en küçük değer tepe ordinatıdır.','f(2) = 1')],
 puf='a ve k ile f(4) değerini de hesaplayıp tabloyla karşılaştır.')

# ================= 03 kolay · kökler ve tepe ordinatı =================
f3=lambda x:x*x-7*x+6
assert f3(1)==0 and f3(6)==0
v=Fr(-25,4); assert min(f3(Fr(k,4)) for k in range(-8,40))==v and f3(Fr(7,2))==v
e=[6+Fr(49,2),Fr(49,4),Fr(7,2),Fr(25,4)]
assert e==[Fr(61,2),Fr(49,4),Fr(7,2),Fr(25,4)] and 6-Fr(49,4)==v and len({v,*e})==5
sx=sy=0.55
body=axes(-1,8,-7,6,sx,sy)+'\n'+curve(f3,-0.4,7.4,sx,sy,MAVI,-7,6)+'\n'+dot(1,0,sx,sy)+dot(6,0,sx,sy)+lab(0.2,5.3,sx,sy,'$y=f(x)$','right',MAVI)
q('0003',tipId='par-oku',tip='Grafik ve tablodan okuma',z='kolay',alt='Tepe Ordinatı',kaz='Köklerden baş katsayısı verilen parabolün denklemini yazıp tepe noktasının ordinatını bulur.',kalip='grafik',
 kart='K-APAR2-01 (kökten tepe) · baş katsayı 1',
 metin='Şekilde, baş katsayısı 1 olan f(x) = x² + bx + c parabolünün grafiği verilmiştir; parabol x eksenini ızgara çizgilerinin kesişimindeki iki noktada kesmektedir.\nBuna göre parabolün tepe noktasının ordinatı kaçtır?',
 dogru=v,yan=[(e[0],'Tepe ordinatını c − b²/(2a) yerine c + b²/(2a) = 6 + 49/2 diye hesaplamış.','bilgi'),(e[1],'Tepe ordinatı olarak yalnız b²/(4a) = 49/4’ü yazmış; c’yi katmamış.','bilgi'),(e[2],'Tepe apsisini (1 + 6)/2 = 7/2 bulup apsisi ordinat sanmış.','dikkat'),(e[3],'Tepe ordinatını −(c − b²/(4a)) ile işaret değiştirerek yazmış.','dikkat')],
 istenen='Tepe noktasının ordinatı.',ip=['Parabolün üzerindeki işaretli noktaları kullan.'],bilgi=[OKU],sekil=fig(body),
 ad=[A('Kökleri oku','Kökler ızgaradan okunur.','x = 1 ve x = 6'),A('Denklemi yaz','Baş katsayı 1’dir.','f(x) = (x − 1)(x − 6) = x² − 7x + 6'),A('Tepe','Tepe apsisi köklerin ortası, ordinatı f(7/2).','f(7/2) = 49/4 − 49/2 + 6 = −25/4')],
 puf='Bulduğun denklemi grafikteki noktalarla sına.')

# ================= 04 orta · yatay doğrular, a+b+c =================
f4=lambda x:-x*x+4*x-1
assert f4(0)==-1 and f4(4)==-1 and f4(2)==3 and all(f4(x)<=3 for x in range(-5,9))
v=f4(1); assert v==2
def abc(a,t,k,c0): # f=a(x-t)^2+k, a belirlenir c0=f(0)
    return a
e=[1-4+7, f4(2), -1-4-1, -1+4+3]
assert e==[4,3,-6,6] and len({v,*e})==5
sx=sy=0.7
body=axes(-1,5,-3,4,sx,sy,gridy=True)+'\n'+seg(-0.8,3,5.2,3,sx,sy,TUR,',thick')+seg(-0.8,-1,5.2,-1,sx,sy,YES,',thick')+'\n'+curve(f4,-0.45,4.45,sx,sy,MAVI,-3,4)
body+='\n'+dot(2,3,sx,sy)+dot(0,-1,sx,sy)+dot(4,-1,sx,sy)+lab(2,3,sx,sy,'$A$','above')+lab(0,-1,sx,sy,'$B$','below left')+lab(4,-1,sx,sy,'$C$','below right')+lab(5.2,3,sx,sy,'$y=3$','right',TUR)+lab(5.2,-1,sx,sy,'$y=-1$','right',YES)
q('0004',tipId='par-yatay',tip='Yatay doğru ve parabol',z='orta',alt='Yatay Doğrular',kaz='İki yatay doğru ile parabolün kesim ve teğet noktalarından parabolün denklemini bulur.',kalip='grafik',
 kart='K-APAR2-02 (teğet yatay doğru + kesim) · B y ekseni üzerinde',
 metin='Şekilde, y = ax² + bx + c parabolü, y = 3 doğrusuna A noktasında teğet olup y = −1 doğrusunu B ve C noktalarında kesmektedir. B noktası y ekseni üzerindedir ve |BC| = 4 birimdir.\nBuna göre a + b + c toplamı kaçtır?',
 dogru=v,yan=[(e[0],'Kolların yönünü yukarı alıp a = 1 yazmış: (x − 2)² + 3 açılımında a + b + c.','dikkat'),(e[1],'a + b + c = f(1) yerine tepe ordinatı f(2) = 3’ü yazmış.','dikkat'),(e[2],'Simetri ekseninin işaretini ters almış: b = −4; a = −1, c = −1 ile toplamış.','islem'),(e[3],'c değerini −1 yerine tepe ordinatı 3 almış: −1 + 4 + 3.','dikkat')],
 istenen='a + b + c toplamı.',ip=['B ve C noktalarının konumunu karşılaştır.'],bilgi=[YAT],sekil=fig(body),
 ad=[A('Tepeyi bul','B(0, −1), C(4, −1) simetriktir; A tepe noktasıdır.','Tepe T(2, 3)'),A('Denklemi yaz','f(x) = a(x − 2)² + 3 ve f(0) = −1.','4a + 3 = −1 → a = −1 → f(x) = −x² + 4x − 1'),A('Topla','a + b + c = f(1).','−1 + 4 − 1 = 2')],
 puf='Bulduğun denklemde x = 4 için f(4) = −1 olduğunu denetle.')

# ================= 05 orta · iki parabol teğet =================
f5=lambda x:x*x-4*x+7
g5=lambda m:(lambda x:-x*x+m*x-1)
sol=[m for m in range(-30,31) if (4+m)**2-64==0]; assert sol==[-12,4]
m=4; xt=Fr(4+m,4); assert xt==2 and f5(2)==g5(4)(2)==3
v=3
xt2=Fr(4-12,4); assert xt2==-2 and f5(-2)==19==g5(-12)(-2)
e=[2,4,7,19]; assert len({v,*e})==5 and f5(0)==7
q('0005',tipId='par-teget',tip='Teğetlik ve ortak nokta sayısı',z='orta',alt='İki Parabol',kaz='Birbirine teğet iki parabolün denklemlerini eşitleyip Δ = 0 koşulundan parametreyi ve teğet noktasını bulur.',kalip='düz',
 kart='K-APAR2-03 (iki parabolün teğetliği) · pozitif m koşulu',
 metin='m pozitif bir gerçel sayı olmak üzere, dik koordinat düzleminde y = x² − 4x + 7 ve y = −x² + mx − 1 parabolleri birbirine teğettir.\nBuna göre, teğet noktasının ordinatı kaçtır?',
 dogru=v,yan=[(e[0],'Teğet noktasının apsisini bulup ordinatı hesaplamamış: x = (4 + 4)/4.','dikkat'),(e[1],'Δ = 0 denkleminden m = 4 değerini bulup m’nin kendisini yazmış.','dikkat'),(e[2],'Birinci parabolün y eksenini kestiği noktanın ordinatını, yani f(0)’ı yazmış.','dikkat'),(e[3],'m = −12 kökünü alıp x = −2 için f(−2) hesaplamış; m > 0 koşuluna bakmamış.','dikkat')],
 istenen='Teğet noktasının ordinatı.',ip=['İki ifadeyi eşitle; ortak noktası tek olan denklemin Δ değeri ne olur?'],bilgi=[TEG],
 ad=[A('Denklemi kur','İki ifade eşitlenir.','x² − 4x + 7 = −x² + mx − 1 → 2x² − (4 + m)x + 8 = 0'),A('Δ = 0','Tek ortak nokta için; m > 0 koşuluyla.','(4 + m)² = 64 → m = 4'),A('Noktayı bul','Çift kök x = (4 + m)/4 = 2, ordinat f(2).','4 − 8 + 7 = 3')],
 puf='Bulduğun noktayı ikinci parabolde de yerine koyup aynı ordinatı bulduğunu denetle.')

# ================= 06 orta · y ekseninin yeri (öncül yok, şekilli) =================
fa=lambda x:-(x+1)**2+3; ga=lambda x:(x+3)**2-1
ta,tb=-1,-3
ps=[-5.5,-4.5,-3.5,-2.5,-1.5]
def ok_(p): return ta>p and tb<=p and fa(p)*ga(p)<0
oks=[ok_(p) for p in ps]; assert oks==[False,False,False,True,False],oks
sx=0.72; sy=0.55
body=f'\\draw[-{{Stealth}},thick] (-6.2*{sx},0) -- (1.6*{sx},0) node[right] {{$x$}};\n'
for i,p in enumerate(ps):
    body+=f'\\draw[dashed,gray!70] ({p*sx:.3f},-2.4*{sy}) -- ({p*sx:.3f},4.1*{sy}); \\node[above,font=\\small\\bfseries] at ({p*sx:.3f},4.1*{sy}) {{{i+1}}};\n'
body+=curve(fa,-3.4,1.4,sx,sy,MAVI,-2.3,3.6)+'\n'+curve(ga,-5.2,-0.9,sx,sy,TUR,-2.3,3.6)+'\n'
body+=lab(0.9,-1.3,sx,sy,'$f$','right',MAVI)+lab(-5.0,2.8,sx,sy,'$g$','left',TUR)
sira6=['1','2','3','4','5']
q('0006',tipId='par-konum',tip='Parametreli parabolde konum',z='orta',alt='Eksenin Yeri',kaz='Parabolün katsayı çarpımlarının işaretlerini y ekseninin konumuna göre yorumlayıp ekseni belirler.',kalip='şekilli',
 kart='K-APAR2-08 (eksen konumu ve işaretler) · iki parabol, beş düşey doğru',
 metin='Aşağıda, y ekseni çizilmeden f(x) = ax² + bx + c ve g(x) = dx² + ex + h parabollerinin grafikleri verilmiştir; f mavi, g turuncudur.\nf ve g’nin katsayıları arasında\n      a · b < 0,      d · e ≥ 0      ve      c · h < 0\neşitsizlikleri olduğuna göre, y ekseni şekilde 1’den 5’e kadar numaralandırılmış doğrulardan hangisi olabilir?',
 dogru='4',yan=[('1','Bu doğruda g’nin tepesi eksenin sağında kalır; d · e < 0 olur, koşul bozulur.','dikkat'),('2','Bu doğruda da g’nin tepesi eksenin sağındadır; d · e ≥ 0 sağlanmaz.','dikkat'),('3','g’nin tepesi eksenin sağında kalmaya devam eder; d · e < 0 olur.','dikkat'),('5','Bu doğruda f ve g’nin eksen kesim noktalarının ikisi de pozitif ordinatlıdır; c · h > 0 olur.','dikkat')],
 sira=sira6,istenen='y ekseninin olabileceği doğru.',ip=['a · b < 0 ise tepe apsisi, a · b > 0 ise ters taraftadır; c ise eksen kesim ordinatıdır.'],bilgi=[KON],sekil=fig(body),
 ad=[A('f için','a · b < 0 olduğundan f’nin tepesi y ekseninin sağındadır.','Eksen, f’nin tepesinin solunda'),A('g için','d · e ≥ 0 olduğundan g’nin tepesi eksenin solunda ya da üzerindedir.','Eksen, g’nin tepesinin sağında'),A('Kesim noktaları','c · h < 0 ise y eksenini f ve g zıt işaretli noktalarda keser; bu yalnız bir doğruda sağlanır.','4 numaralı doğru')],
 puf='Seçtiğin doğruda her iki parabolün eksen kesim noktasının işaretini ayrı ayrı yaz.')

# ================= 07 orta · AB = ..., alan =================
r=1; a7=4; f7=lambda x:a7*(x-1)*(x-3)
assert f7(2)==-4 and f7(0)==12
v=Fr(1,2)*(3-1)*f7(0); assert v==12
e=[Fr(1,2)*2*3,Fr(1,2)*2*4,Fr(1,2)*3*12,2*12]
assert e==[3,4,18,24] and len({v,*e})==5
sx=0.9; sy=0.24
body=f'\\draw[-{{Stealth}},thick] (-0.6*{sx},0) -- (4.8*{sx},0) node[right] {{$x$}};\\draw[-{{Stealth}},thick] (0,-5.2*{sy}) -- (0,14*{sy}) node[above] {{$y$}};\n'
body+=poly([(1,0),(3,0),(0,12)],sx,sy,'orange!25')+'\n'+curve(f7,-0.2,4.2,sx,sy,MAVI,-5,13.5)+'\n'
body+=seg(2,-4,2,0,sx,sy,'gray',',dashed')+seg(0,-4,2,-4,sx,sy,'gray',',dashed')+seg(1,0,0,12,sx,sy,TUR,',thick')+seg(3,0,0,12,sx,sy,TUR,',thick')
body+=dot(1,0,sx,sy)+dot(3,0,sx,sy)+dot(0,12,sx,sy)+dot(2,-4,sx,sy)
body+=lab(1,0,sx,sy,'$A$','above left')+lab(3,0,sx,sy,'$B$','above right')+lab(0,12,sx,sy,'$C$','left')+lab(2,-4,sx,sy,'$T$','below')
body+=f'\\node[below,font=\\footnotesize] at (2*{sx},0.0) {{$2$}};\\node[left,font=\\footnotesize] at (0,-4*{sy}) {{$-4$}};\\node[below left,font=\\footnotesize] at (0,0) {{$O$}};'
q('0007',tipId='par-ucgen',tip='Parabolle oluşan şekillerin alanı',z='orta',alt='Üçgen Alanı',kaz='Kökler ve tepe noktasıyla verilen parabolün denklemini bulup eksen kesim noktalarından oluşan üçgenin alanını hesaplar.',kalip='şekilli',
 kart='K-APAR2-04 (A, B, C üçgeni) · kökler oranı ve tepe',
 metin='Şekilde, tepe noktası T olan f parabolünün grafiği verilmiştir. Parabol, x eksenini pozitif apsisli A ve B noktalarında, y eksenini C noktasında kesmektedir. |OB| = 3 · |OA| olup T noktasının koordinatları şekilde gösterilmiştir.\nBuna göre ABC üçgeninin alanı kaç birimkaredir?',
 dogru=v,yan=[(e[0],'Baş katsayıyı 1 alıp C(0, 3) bulmuş: 2 · 3/2.','dikkat'),(e[1],'C noktasının ordinatı yerine tepe ordinatının mutlak değerini (4) yükseklik almış.','dikkat'),(e[2],'|AB| yerine |OB| = 3 almış: 3 · 12/2.','dikkat'),(e[3],'Alan formülündeki 1/2 çarpanını unutmuş: 2 · 12.','dikkat')],
 istenen='ABC üçgeninin alanı (birimkare).',ip=['|OB| = 3 · |OA| ve T noktasını birlikte kullan.'],bilgi=[UCG],sekil=fig(body),
 ad=[A('Kökleri bul','Kökler r ve 3r, tepe apsisi bunların ortası olan 2r = 2’dir.','r = 1: A(1, 0), B(3, 0)'),A('Denklemi yaz','f(x) = a(x − 1)(x − 3); tepe ordinatı f(2) = −a = −4.','a = 4, f(0) = 12 → C(0, 12)'),A('Alan','Taban |AB| = 2, yükseklik 12.','2 · 12/2 = 12')],
 puf='Bulduğun f’de f(2) = −4 olduğunu tepe noktasıyla karşılaştır.')

# ================= 08 orta · doğru, parabol ve üçgen alanı =================
f8=lambda x:x*x-x-6; l8=lambda x:x+2
xs=[x for x in range(-20,21) if f8(x)==l8(x)]; assert xs==[-2,4]
assert f8(-2)==0 and f8(3)==0 and l8(4)==6==f8(4)
v=Fr(1,2)*5*6; assert v==15
e=[Fr(1,2)*3*6,Fr(1,2)*5*4,Fr(1,2)*6*6,5*6]
assert e==[9,10,18,30] and len({v,*e})==5
sx=0.6; sy=0.42
body=axes(-3,5,-7,7,sx,sy)+'\n'+poly([(-2,0),(3,0),(4,6)],sx,sy,'orange!25')+'\n'+curve(f8,-2.9,4.3,sx,sy,MAVI,-7,7)+'\n'+curve(l8,-3,5,sx,sy,TUR,-7,7)+'\n'
body+=dot(-2,0,sx,sy)+dot(3,0,sx,sy)+dot(4,6,sx,sy)+lab(-2,0,sx,sy,'$A$','above left')+lab(3,0,sx,sy,'$C$','above right')+lab(4,6,sx,sy,'$B$','above left')+lab(-2.9,6.2,sx,sy,'$y=f(x)$','right',MAVI)+lab(1.6,3.6,sx,sy,'$y=x+2$','below right',TUR)
q('0008',tipId='par-ucgen',tip='Parabolle oluşan şekillerin alanı',z='orta',alt='Doğru ve Parabol',kaz='Parabol ile doğrunun ortak noktasını denklemle bulup köşeleri koordinatla verilen üçgenin alanını hesaplar.',kalip='grafik',
 kart='K-APAR2-04 (doğru + parabol → üçgen) · A ortak, C kök',
 metin='Şekilde, baş katsayısı 1 olan f parabolü ile y = x + 2 doğrusu verilmiştir. A ve C noktaları parabolün x eksenini kestiği noktalardır; B noktası ise doğru ile parabolün A’dan farklı ortak noktasıdır.\nBuna göre ABC üçgeninin alanı kaç birimkaredir?',
 dogru=v,yan=[(e[0],'Taban olarak |OC| = 3’ü almış: 3 · 6/2.','dikkat'),(e[1],'Yükseklik yerine B’nin apsisini (4) kullanmış: 5 · 4/2.','dikkat'),(e[2],'Taban olarak A ile B’nin apsis farkını (6) almış: 6 · 6/2.','dikkat'),(e[3],'Alan formülündeki 1/2 çarpanını unutmuş: 5 · 6.','dikkat')],
 istenen='ABC üçgeninin alanı (birimkare).',ip=['Doğru x eksenini A’da kestiğine göre A’yı, sonra f’yi yaz.'],bilgi=[UCG],sekil=fig(body),
 ad=[A('A, C ve f','Doğru x eksenini x = −2’de keser; C’yi şekilden oku.','A(−2, 0), C(3, 0) → f(x) = (x + 2)(x − 3) = x² − x − 6'),A('B noktası','f(x) = x + 2 denklemi çözülür.','x² − 2x − 8 = 0 → x = −2 ya da 4 → B(4, 6)'),A('Alan','Taban |AC| = 5, yükseklik 6.','5 · 6/2 = 15')],
 puf='B noktasının hem doğruda hem parabolde olduğunu yerine koyarak denetle.')

# ================= 09 zor · f/g ≥ 0, tam sayı toplamı =================
f9=lambda x:(x+3)*(x-1); g9=lambda x:x+1
dom=[x for x in range(-5,5) if g9(x)!=0 and Fr(f9(x),g9(x))>=0]; assert dom==[-3,-2,1,2,3,4]
v=sum(dom); assert v==5
e1=sum(x for x in range(-5,5) if f9(x)/ (g9(x) if g9(x)!=0 else 1)<=0 and g9(x)!=0)
e2=sum(x for x in range(-5,5) if f9(x)>=0)
e3=sum(x for x in range(-5,5) if (g9(x)!=0 and Fr(f9(x),g9(x))>=0) or g9(x)==0)
e4=sum(x for x in range(-5,5) if g9(x)!=0 and Fr(f9(x),g9(x))>0)
e=[e1,e2,e3,e4]; assert e==[-11,-2,4,7] and len({v,*e})==5,e
sx=0.62; sy=0.5
body=axes(-5,4,-5,5,sx,sy)+'\n'+curve(f9,-4.2,2.2,sx,sy,MAVI,-5,5)+'\n'+seg(-5,-4,3.9,4.9,sx,sy,TUR,',very thick')+'\n'+dot(-3,0,sx,sy)+dot(1,0,sx,sy)+dot(-1,0,sx,sy)+lab(-3.9,3.4,sx,sy,'$y=f(x)$','left',MAVI)+lab(3.9,4.9,sx,sy,'$y=g(x)$','below right',TUR)
q('0009',tipId='par-esitsiz',tip='Grafikle eşitsizlik ve oran',z='orta',alt='Bölüm Eşitsizliği',kaz='Parabol ve doğrunun grafiğinden işaretleri okuyarak bölüm eşitsizliğinin çözümündeki tam sayıları bulur.',kalip='grafik',
 kart='K-APAR2-05 (f/g ≥ 0) · payda sıfır dışlanır',
 metin='Şekilde, gerçel sayılar kümesi üzerinde tanımlı ikinci dereceden f ve doğrusal g fonksiyonlarının grafikleri verilmiştir; işaretli noktalar x eksenini kesen noktalardır.\nBuna göre, f(x)/g(x) ≥ 0 eşitsizliğini sağlayan x tam sayılarından −5 ≤ x ≤ 4 aralığında bulunanların toplamı kaçtır?',
 dogru=v,yan=[(e[0],'Eşitsizliği f(x)/g(x) ≤ 0 okumuş: −5, −4, −3, 0, 1.','dikkat'),(e[1],'g’nin işaretine bakmadan yalnız f(x) ≥ 0 koşulunu almış: −5, −4, −3, 1, 2, 3, 4.','dikkat'),(e[2],'Paydayı sıfır yapan x = −1 değerini de çözüme katmış.','dikkat'),(e[3],'Eşitsizliği kesin (>) okuyup paydanın yanında f’nin köklerini de çözümden çıkarmış: −2, 2, 3, 4.','dikkat')],
 istenen='Tam sayı çözümlerinin toplamı.',ip=['Her iki grafikten işaretleri ayrı ayrı oku; g(x) = 0 olan noktaya dikkat et.'],bilgi=[ESI],sekil=fig(body),
 ad=[A('İşaretleri oku','f: x < −3 ve x > 1 için pozitif; g: x > −1 için pozitif.','f ≥ 0: x ≤ −3 ya da x ≥ 1; g > 0: x > −1'),A('Bölümü incele','x < −1 iken g < 0, bu yüzden f ≤ 0 olmalı; x > −1 iken f ≥ 0 olmalı; x = −1 alınmaz.','−3 ≤ x < −1 ya da x ≥ 1'),A('Tam sayılar','−5 ≤ x ≤ 4 aralığında: −3, −2, 1, 2, 3, 4','Toplam = −5 + 10 = 5')],
 puf='Bulduğun aralıkların dışından bir tam sayı seçip eşitsizliğin sağlanmadığını göster.')

# ================= 10 orta · gelir =================
G=lambda x:(40-x)*(200+10*x)
assert max(G(Fr(k,2)) for k in range(0,80))==9000 and G(10)==9000
v=9000
e=[10,1000,8000,G(1)]
assert -10*10**2+200*10==1000 and G(0)==8000 and G(1)==8190 and len({v,*e})==5
q('0010',tipId='par-uygulama',tip='Gelir ve yörünge uygulaması',z='orta',alt='Gelir Uygulaması',kaz='Fiyat indirimi ile satış adedinin bağlı olduğu durumda geliri ikinci dereceden fonksiyonla yazıp en büyük değerini bulur.',kalip='hikâyeli',
 kart='K-APAR2-07 (gelir fonksiyonu) · indirim ve adet',
 metin='Bir mağazada tanesi 40 TL olan bir ürün haftada 200 adet satılmaktadır. Yapılan araştırmaya göre ürünün fiyatında yapılan her 1 TL’lik indirim, haftalık satış adedini 10 adet artırmaktadır. İndirim tam TL olarak yapılacaktır.\nBuna göre mağazanın bu üründen haftalık elde edeceği gelir en fazla kaç TL olabilir?',
 dogru=v,yan=[(e[0],'Gelir ifadesinin tepe apsisini, yani indirim miktarı olan 10 TL’yi cevap sanmış.','dikkat'),(e[1],'Gelir ifadesinde sabit terim 8000’i yazmayı unutup yalnız 200x − 10x² ifadesini hesaplamış.','islem'),(e[2],'İndirim yapmadan elde edilen geliri (40 · 200) en büyük sanmış.','dikkat'),(e[3],'Tepe yerine yalnız 1 TL’lik indirimi deneyip (40 − 1)(200 + 10) hesaplamış.','dikkat')],
 istenen='Haftalık en büyük gelir (TL).',ip=['İndirim x TL ise yeni fiyatı ve yeni satış adedini x türünden yaz.'],bilgi=[UYG],
 ad=[A('Geliri yaz','İndirim x TL: fiyat 40 − x, adet 200 + 10x.','G(x) = (40 − x)(200 + 10x) = −10x² + 200x + 8000'),A('Tepe','G’nin tepe apsisi bulunur.','x = −200/(−20) = 10'),A('En büyük gelir','x = 10 için hesaplanır.','G(10) = 30 · 300 = 9000')],
 puf='Fiyat 30 TL, adet 300 olduğunda geliri doğrudan çarparak denetle.')

# ================= 11 orta · görüntü kümesi öncüllü =================
f11=lambda x:-x*x+2*x+3
def img(a,b):
    xs=[Fr(k,100) for k in range(a*100,b*100+1)]; ys=[f11(x) for x in xs]; return min(ys),max(ys)
assert img(0,2)[1]==4
assert img(-1,2)==(0,4)       # II: [0,3] yanlış
assert img(-2,0)==(-5,3)      # III: [-5,3] doğru
I11=True; II11=(img(-1,2)==(0,3)); III11=(img(-2,0)==(-5,3))
assert (I11,II11,III11)==(True,False,True)
dog=ad_(['I','III']); assert dog==SIRA1[3]
sx=sy=0.6
body=axes(-3,4,-6,5,sx,sy)+'\n'+curve(f11,-2.4,4.4,sx,sy,MAVI,-6.2,5)+'\n'+dot(-1,0,sx,sy)+dot(3,0,sx,sy)+dot(1,4,sx,sy)+dot(0,3,sx,sy)+lab(-1.6,-1.4,sx,sy,'$y=f(x)$','left',MAVI)
q('0011',tipId='par-goruntu',tip='Kapalı aralıkta görüntü ve mutlak değer',z='orta',alt='Görüntü Kümesi',kaz='Parabolün grafiğinden kapalı aralıklardaki en büyük, en küçük değerleri ve görüntü kümelerini belirler.',kalip='öncüllü',
 kart='K-APAR2-06 (aralıkta görüntü kümesi) · tepe aralık içinde ve dışında',
 metin='Şekilde, gerçel sayılar kümesi üzerinde tanımlı f fonksiyonunun grafiği olan parabol verilmiştir; işaretli noktalar ızgara çizgilerinin kesişimindedir.\nBuna göre,\nI. f fonksiyonunun [0, 2] aralığındaki en büyük değeri 4’tür.\nII. f fonksiyonunun [−1, 2] aralığındaki görüntü kümesi [0, 3] aralığıdır.\nIII. f fonksiyonunun [−2, 0] aralığındaki görüntü kümesi [−5, 3] aralığıdır.\nyargılarından hangileri doğrudur?',
 dogru=dog,yan=[(SIRA1[0],'I’i doğru bulmuş, II’nin yanlış olduğunu da görmüş; ancak III’te üst sınırı tepe ordinatı 4 sanıp görüntü kümesini [−5, 4] bulduğu için III’ü yanlış saymış.','dikkat'),(SIRA1[1],'I’de tepenin aralık içinde olduğunu görmeyip f(0) = f(2) = 3 almış; II’yi uç değerlerle [0, 3] bulup doğru saymış; III’ü [−5, 4] sanmış.','dikkat'),(SIRA1[2],'II’yi uç değerlere bakıp [0, 3] bulduğu için doğru sanmış; III’te üst sınırı tepe ordinatı 4 sanıp yanlış saymış.','dikkat'),(SIRA1[4],'Her aralıkta yalnız uç değerlere baktığı için II’yi doğru bulmuş.','dikkat')],
 sira=SIRA1,istenen='Doğru olan yargılar.',ip=['Her aralık için en büyük ve en küçük değerin nerede alındığına bak.'],bilgi=[GOR],sekil=fig(body),
 ad=[A('I’i sına','Tepe noktası (1, 4) [0, 2] içindedir.','En büyük değer 4, I doğru'),A('II’yi sına','[−1, 2] aralığında tepe içeride; f(−1) = 0, f(2) = 3.','Görüntü kümesi [0, 4], II yanlış'),A('III’ü sına','[−2, 0] aralığında f artandır: f(−2) = −5, f(0) = 3.','Görüntü kümesi [−5, 3], III doğru')],
 puf='Her yargıyı grafik üzerinde ayrı ayrı işaretleyerek sına.')

# ================= 12 orta · y = mx ile ortak nokta olmaması =================
sol=[m for m in range(-40,41) if (4+m)**2-20<0]; assert sol==list(range(-8,1))
v=sum(sol); assert v==-36
e1=sum(m for m in range(-40,41) if m*m-20<0); e2=sum(m for m in range(-40,41) if (m-4)**2-20<0); e3=sum(range(-9,2))
e=[e1,e2,e3,len(sol)]; assert e==[0,36,-44,9] and len({v,*e})==5
q('0012',tipId='par-teget',tip='Teğetlik ve ortak nokta sayısı',z='orta',alt='Ortak Nokta Yok',kaz='Doğru ile parabolün ortak noktası olmaması koşulunu Δ < 0 ile yazıp parametrenin tam sayı değerlerini bulur.',kalip='düz',
 kart='K-APAR2-03 (ortak nokta yok) · y = mx',
 metin='m bir gerçel sayı olmak üzere, dik koordinat düzleminde y = x² − 4x + 5 parabolü ile y = mx doğrusunun ortak noktası yoktur.\nBuna göre, m’nin alabileceği tam sayı değerlerinin toplamı kaçtır?',
 dogru=v,yan=[(e[0],'Denklemi x² − mx + 5 = 0 yazıp −4x terimini katmamış: m² < 20 için −4’ten 4’e toplam.','dikkat'),(e[1],'(m − 4)² < 20 yazmış (x terimini m’ye eklemek yerine çıkarmış): m = 0, …, 8.','islem'),(e[2],'√20 ≈ 4,47’yi 5’e yuvarlayıp −5 ≤ m + 4 ≤ 5 almış: m = −9, …, 1.','dikkat'),(e[3],'Toplam yerine tam sayıların sayısını yazmış.','dikkat')],
 istenen='m’nin tam sayı değerlerinin toplamı.',ip=['İki ifadeyi eşitleyip ortaya çıkan denklemin Δ değerinin işaretini incele.'],bilgi=[TEG],
 ad=[A('Denklemi kur','İfadeler eşitlenir.','x² − (4 + m)x + 5 = 0'),A('Δ < 0','Ortak nokta yok.','(4 + m)² − 20 < 0 → −4,47 < 4 + m < 4,47'),A('Tam sayılar','m + 4 ∈ {−4, …, 4}, yani m = −8, …, 0.','Toplam = −36')],
 puf='Bulduğun aralığın uçlarının tam sayı olup olmadığına bak.')

# ================= 13 zor · teğet nokta, kökler arası uzaklık =================
f13=lambda x:x*x-8*x+7
assert f13(5)==-8 and 2*5-18==-8 and all(f13(x)>=2*x-18 for x in range(-10,21)) and f13(1)==f13(7)==0
b13=[b for b in range(-30,31) if (b-2)**2==4*(7+18) or False]
v=6
D13=64-28; assert D13==36 and math.isqrt(D13)==6
e=[3,8,9,36]; assert len({v,*e})==5 and abs(f13(4))==9
sx=0.5; sy=0.19
body=f'\\draw[-{{Stealth}},thick] (-0.5*{sx},0) -- (9.6*{sx},0) node[right] {{$x$}};\\draw[-{{Stealth}},thick] (0,-11*{sy}) -- (0,17*{sy}) node[above] {{$y$}};\n'
body+=curve(f13,0.2,8.8,sx,sy,MAVI,-10,16)+'\n'+curve(lambda x:2*x-18,2.2,7.6,sx,sy,TUR,-14,-2)+'\n'+seg(5,-8,5,0,sx,sy,'gray',',dashed')+dot(5,-8,sx,sy)+lab(5,-8,sx,sy,'$T$','below right')
body+=f'\\node[above,font=\\footnotesize] at (5*{sx},0.1) {{$5$}};\\node[below left,font=\\footnotesize] at (0,0) {{$O$}};'
body+=lab(8.8,16,sx,sy,'$y=x^2+bx+c$','left',MAVI)+lab(7.6,-2.6,sx,sy,'$y=2x-18$','right',TUR)
q('0013',tipId='par-teget',tip='Teğetlik ve ortak nokta sayısı',z='zor',alt='Teğet Doğru',kaz='Bir doğruya verilen apsisli noktada teğet olan parabolün katsayılarını bulup x eksenini kestiği noktalar arasındaki uzaklığı hesaplar.',kalip='grafik',
 kart='K-APAR2-03 (verilen noktada teğet → kökler arası uzaklık)',
 metin='Şekilde, y = x² + bx + c parabolü ile y = 2x − 18 doğrusu verilmiştir. Doğru, parabola apsisi şekilde gösterilen T noktasında teğettir. Parabol x eksenini iki farklı noktada kesmektedir.\nBuna göre bu iki nokta arasındaki uzaklık kaç birimdir?',
 dogru=v,yan=[(e[0],'Kökler arasındaki uzaklığın yarısını (√Δ/2 = 3) yazmış.','dikkat'),(e[1],'Uzaklık yerine b’nin mutlak değerini (8) yazmış.','dikkat'),(e[2],'Tepe noktasının ordinatının mutlak değerini (9) uzaklık sanmış.','dikkat'),(e[3],'Karekök almayı unutup Δ = 36 değerini yazmış.','dikkat')],
 istenen='Kökler arasındaki uzaklık (birim).',ip=['T noktasının apsisini, parabol ile doğrunun ortak noktasının apsisi olarak değerlendir.'],bilgi=[TEG],sekil=fig(body),
 ad=[A('Denklemi kur','Parabol ile doğru eşitlenir.','x² + (b − 2)x + c + 18 = 0'),A('Teğetlik','x = 5 çift köktür: kökler toplamı 10, çarpımı 25.','b − 2 = −10 → b = −8; c + 18 = 25 → c = 7'),A('Uzaklık','x² − 8x + 7 = 0 kökleri bulunur.','x = 1 ve x = 7 → uzaklık 6')],
 puf='Bulduğun parabolün T noktasından geçtiğini denetle.')

# ================= 14 zor · simetrik parabol, yamuk alanı =================
f14=lambda x:x*x-4*x-5; g14=lambda x:-f14(x)
assert f14(-1)==f14(5)==0 and f14(2)==-9 and f14(0)==-5
v=Fr(1,2)*(10+18)*2; assert v==28
e=[14,20,36,56]; assert Fr(1,2)*(10+18)==14 and 10*2==20 and 18*2==36 and (10+18)*2==56 and len({v,*e})==5
sx=0.6; sy=0.32
body=axes(-2,6,-10,10,sx,sy,ys=5)+'\n'+poly([(0,5),(2,9),(2,-9),(0,-5)],sx,sy,'orange!22')+'\n'+curve(f14,-1.9,5.9,sx,sy,MAVI,-10,10)+'\n'+curve(g14,-1.9,5.9,sx,sy,YES,-10,10)+'\n'
body+=dot(0,5,sx,sy)+dot(2,9,sx,sy)+dot(2,-9,sx,sy)+dot(0,-5,sx,sy)+lab(0,5,sx,sy,'$A$','above left')+lab(2,9,sx,sy,'$B$','above right')+lab(2,-9,sx,sy,'$C$','below right')+lab(0,-5,sx,sy,'$D$','below left')
body+=lab(5.9,9,sx,sy,'$y=g(x)$','left',YES)+lab(5.9,-9.5,sx,sy,'$y=f(x)$','left',MAVI)
q('0014',tipId='par-ucgen',tip='Parabolle oluşan şekillerin alanı',z='zor',alt='Simetrik Parabol',kaz='Grafiği verilen parabolün x eksenine göre simetriğini kullanarak tepe ve y eksenini kesim noktalarının oluşturduğu yamuğun alanını hesaplar.',kalip='şekilli',
 kart='K-APAR2-04 (iki parabolün ortak şekli) · iki düşey paralel kenarlı yamuk',
 metin='Şekilde, f fonksiyonunun grafiği olan parabol ile bu grafiğin x eksenine göre simetriği olan g fonksiyonunun grafiği verilmiştir. A ve D noktaları grafiklerin y eksenini kestiği noktalar, B ve C noktaları ise g ve f’nin tepe noktalarıdır; f’nin baş katsayısı 1’dir.\nBuna göre ABCD yamuğunun alanı kaç birimkaredir?',
 dogru=v,yan=[(e[0],'Paralel kenarların ortalamasını (14) alıp yükseklik olan 2’yle çarpmayı unutmuş.','dikkat'),(e[1],'Alanı yalnız kısa kenar × yükseklik olarak (10 · 2) hesaplamış.','dikkat'),(e[2],'Alanı uzun kenar × yükseklik olarak (18 · 2) hesaplamış.','dikkat'),(e[3],'Yamuğun alan formülündeki 1/2 çarpanını unutmuş: (10 + 18) · 2.','dikkat')],
 istenen='ABCD yamuğunun alanı (birimkare).',ip=['Grafikten f’nin denklemini kurup g’nin f ile ilişkisini kullanarak A, B, C, D noktalarını yaz.'],bilgi=[UCG],sekil=fig(body),
 ad=[A('f ve g','Kökler −1 ve 5, baş katsayı 1.','f(x) = x² − 4x − 5, g(x) = −x² + 4x + 5'),A('Köşeler','Tepe noktaları ve y kesimleri bulunur.','A(0, 5), B(2, 9), C(2, −9), D(0, −5)'),A('Alan','Paralel kenarlar |AD| = 10 ve |BC| = 18, yükseklik 2.','(10 + 18) · 2/2 = 28')],
 puf='Köşe koordinatlarını şekildeki ızgarayla karşılaştırarak denetle.')

# ================= 15 orta · y = 5 doğrusu, en küçük değer =================
f15=lambda x:x*x-2*x+2
assert f15(-1)==f15(3)==5 and f15(0)==2
v=min(f15(Fr(k,4)) for k in range(-8,16)); assert v==1
fk=lambda x:(x+1)*(x-2)+5
e=[2,3,5,min(fk(Fr(k,4)) for k in range(-8,16))]
assert e==[2,3,5,Fr(11,4)] and len({v,*e})==5
sx=sy=0.75
body=f'\\draw[-{{Stealth}},thick] (-2.2*{sx},0) -- (4.2*{sx},0) node[right] {{$x$}};\\draw[-{{Stealth}},thick] (0,-0.6*{sy}) -- (0,6.4*{sy}) node[above] {{$y$}};\n'
body+=seg(-2,5,4.6,5,sx,sy,TUR,',thick')+'\n'+curve(f15,-1.6,3.6,sx,sy,MAVI,-0.5,6.2)+'\n'+dot(-1,5,sx,sy)+dot(3,5,sx,sy)+dot(0,5,sx,sy)+lab(-1,5,sx,sy,'$A$','above left')+lab(0,5,sx,sy,'$B$','above right')+lab(3,5,sx,sy,'$C$','above right')+lab(4.6,5,sx,sy,'$y=5$','right',TUR)+f'\\node[below left,font=\\footnotesize] at (0,0) {{$O$}};'
q('0015',tipId='par-yatay',tip='Yatay doğru ve parabol',z='orta',alt='Kesen Doğru',kaz='Yatay bir doğrunun parabolü kestiği noktaların uzaklıklarından parabolün denklemini bulup en küçük değerini hesaplar.',kalip='grafik',
 kart='K-APAR2-02 (y = k doğrusu, |AB| ve |BC|) · y ekseni arada',
 metin='Şekilde, baş katsayısı 1 olan f parabolü ile y = 5 doğrusu verilmiştir. Doğru, parabolü A ve C noktalarında, y eksenini B noktasında kesmektedir. |AB| = 1 birim ve |BC| = 3 birimdir.\nBuna göre f fonksiyonunun en küçük değeri kaçtır?',
 dogru=v,yan=[(e[0],'f(0) = 2’yi, yani y eksenini kestiği noktanın ordinatını en küçük değer sanmış.','dikkat'),(e[1],'Tepenin y = 5 doğrusuna uzaklığını yarı genişlik |AC|/2 = 2 sanıp 5 − 2 hesaplamış.','islem'),(e[2],'Doğrunun denklemindeki 5’i en küçük değer sanmış.','dikkat'),(e[3],'|AB| + |BC| = 3 sanıp C(2, 5) almış: (x + 1)(x − 2) + 5 ifadesinin en küçük değeri.','islem')],
 istenen='f’nin en küçük değeri.',ip=['A ve C’nin koordinatlarını yaz.'],bilgi=[YAT],sekil=fig(body),
 ad=[A('Apsisler','B(0, 5), A solda 1, C sağda 3 birim uzakta.','A(−1, 5), C(3, 5)'),A('Denklemi yaz','f(x) − 5 = (x + 1)(x − 3) (baş katsayı 1).','f(x) = x² − 2x + 2'),A('En küçük değer','Tepe apsisi (−1 + 3)/2 = 1.','f(1) = 1')],
 puf='f(−1) = f(3) = 5 olduğunu bulduğun denklemde sına.')

# ================= 16 zor · tepe noktası doğru üzerinde, tepeler arası uzaklık =================
def tepe_m(m): return (m, m*m-2*m*m+m+5)
sol=[m for m in range(-20,21) if tepe_m(m)[1]==2*tepe_m(m)[0]-1]; assert sol==[-3,2] and tepe_m(2)==(2,3) and tepe_m(-3)==(-3,-7)
(xa,ya),(xb,yb)=tepe_m(2),tepe_m(-3)
assert (xa-xb)**2+(ya-yb)**2==125
v='5√5'
sira16=['5','10','5√5','15','125']
assert abs(5*math.sqrt(5)-11.18)<0.01 and xa-xb==5 and ya-yb==10 and 5+10==15
q('0016',tipId='par-konum',tip='Parametreli parabolde konum',z='zor',alt='Tepe Noktasının Yeri',kaz='Parametreli bir parabolün tepe noktasının doğru üzerinde olması koşulundan parametre değerlerini bulup elde edilen tepe noktaları arasındaki uzaklığı hesaplar.',kalip='düz',
 kart='K-APAR2-08 (tepe noktası doğru üzerinde, iki tepe arası uzaklık) · m parametresi',
 metin='m bir gerçel sayı olmak üzere, gerçel sayılar kümesi üzerinde f(x) = x² − 2mx + m + 5 fonksiyonunun grafiğinin tepe noktası, dik koordinat düzleminde y = 2x − 1 doğrusu üzerindedir. Bu koşulu sağlayan iki farklı m değeri için elde edilen parabollerin tepe noktaları A ve B’dir.\nBuna göre |AB| uzunluğu kaç birimdir?',
 dogru=v,yan=[('5','Yalnız apsisler farkını uzunluk saymış: 2 − (−3).','dikkat'),('10','Yalnız ordinatlar farkını uzunluk saymış: 3 − (−7).','dikkat'),('15','Apsis farkı ile ordinat farkını toplamış: 5 + 10.','islem'),('125','Uzaklık formülünde karekökü almayı unutmuş: 5² + 10².','dikkat')],
 sira=sira16,istenen='|AB| uzunluğu (birim).',ip=['Tepe noktasını m türünden yaz, koordinatlarını doğru denkleminde yerine koy.'],bilgi=[KON],
 ad=[A('Tepeyi yaz','Tepe apsisi m, ordinatı f(m).','T(m, −m² + m + 5)'),A('Doğruda olsun','T, y = 2x − 1 üzerindedir.','−m² + m + 5 = 2m − 1 → m = −3 ya da m = 2 → A(2, 3), B(−3, −7)'),A('Uzaklık','Uzaklık formülü uygulanır.','√(5² + 10²) = 5√5')],
 puf='Bulduğun iki tepe noktasının da doğrunun denklemini sağladığını denetle.')

# ================= 17 zor · parabol ve doğru öncüllü =================
f17=lambda x:-x*x+4*x; g17=lambda x:x-4
xs=[x for x in range(-10,11) if f17(x)==g17(x)]; assert xs==[-1,4] and sum(xs)==3
I17=True
tams=[x for x in range(-10,11) if f17(x)>g17(x)]; assert tams==[0,1,2,3] and sum(tams)==6
II17=(sum(tams)==6); assert II17
assert sum(range(-1,5))==9
hx=max(range(-80,81),key=lambda k:f17(Fr(k,8))-g17(Fr(k,8))); xh=Fr(hx,8); assert xh==Fr(3,2) and g17(xh)==Fr(-5,2)
III17=(g17(xh)==Fr(-5,2)); assert III17 and g17(2)==-2
dog=ad_(['I','II','III']); assert dog==SIRA1[4]
sx=sy=0.62
body=axes(-2,6,-6,5,sx,sy)+'\n'+curve(f17,-1.4,5.4,sx,sy,MAVI,-6,5)+'\n'+seg(-1.5,-5.5,6,2,sx,sy,TUR,',very thick')+'\n'+dot(-1,-5,sx,sy)+dot(4,0,sx,sy)+dot(0,0,sx,sy)+lab(2,4,sx,sy,'$y=f(x)$','above',MAVI)+lab(6,2,sx,sy,'$y=g(x)$','right',TUR)
q('0017',tipId='par-esitsiz',tip='Grafikle eşitsizlik ve oran',z='zor',alt='Fark Fonksiyonu',kaz='Parabol ve doğrunun grafiğinden denklemleri okuyup ortak noktaları, f > g çözümünü ve fark fonksiyonunun en büyük olduğu noktayı yorumlar.',kalip='öncüllü',
 kart='K-APAR2-05 (f > g çözümü ve fark) · f − g ikinci dereceden',
 metin='Şekilde, f fonksiyonunun grafiği olan parabol ile g fonksiyonunun grafiği olan doğru verilmiştir; işaretli noktalar ızgara çizgilerinin kesişimindedir.\nBuna göre,\nI. f(x) = g(x) denkleminin kökleri toplamı 3’tür.\nII. f(x) > g(x) eşitsizliğini sağlayan tam sayıların toplamı 6’dır.\nIII. f(x) − g(x) farkının en büyük olduğu x değeri için g(x) = −5/2’dir.\nyargılarından hangileri doğrudur?',
 dogru=dog,yan=[(SIRA1[0],'II’de uç noktaları da alıp −1’den 4’e tam sayıların toplamını 9 bulduğu için II’yi yanlış saymış; III’te farkın en büyük olduğu x’i f’nin tepe apsisi 2 alıp g(2) = −2 bulmuş.','dikkat'),(SIRA1[1],'I’de kökler toplamını 5 (−1 ile 4’ün mutlak değerleri toplamı) sanıp I’i yanlış saymış; III’te g(2) = −2 hesaplamış.','dikkat'),(SIRA1[2],'III’te farkın en büyük olduğu x değerini f’nin tepe apsisi 2 alıp g(2) = −2 bulduğu için III’ü yanlış saymış.','dikkat'),(SIRA1[3],'II’de uç noktaları da alıp tam sayıların toplamını 9 bulduğu için II’yi yanlış saymış.','dikkat')],
 sira=SIRA1,istenen='Doğru olan yargılar.',ip=['Grafikten f ve g’yi yazıp ikisinin farkını incele.'],bilgi=[ESI],sekil=fig(body),
 ad=[A('Denklemleri yaz','Grafikten f(x) = −x² + 4x, g(x) = x − 4.','f(x) − g(x) = −x² + 3x + 4 = −(x − 4)(x + 1)'),A('I ve II','Kökler −1 ve 4; fark (−1, 4) aralığında pozitif.','I doğru (toplam 3); tam sayılar 0, 1, 2, 3 → toplam 6, II doğru'),A('III','Farkın tepe apsisi 3/2; g(3/2) = −5/2.','III doğru')],
 puf='Her yargıyı ayrı ayrı, bulduğun fark ifadesiyle sına.')

# ================= 18 zor · P noktası, üçgen alanı en büyük =================
f18=lambda x:6*x-x*x
Ar=lambda t:Fr(1,2)*6*f18(t)
assert max(Ar(Fr(k,10)) for k in range(40,51))==24 and Ar(4)==24 and Ar(5)==15 and Ar(3)==27
v=24
e=[Fr(6*4,2),Ar(5),Ar(3),2*24]
assert e==[12,15,27,48] and len({v,*e})==5
sx=0.75; sy=0.42
body=axes(-1,7,-1,10,sx,sy,xext=0.6)+'\n'+poly([(0,0),(6,0),(4.5,f18(4.5))],sx,sy,'orange!22')+'\n'+curve(f18,-0.4,6.4,sx,sy,MAVI,-1,10)+'\n'+curve(f18,4,5,sx,sy,KIR,-1,10,w='line width=3.2pt')+'\n'
body+=seg(4,0,4,8,sx,sy,'gray',',dashed')+seg(5,0,5,5,sx,sy,'gray',',dashed')+dot(6,0,sx,sy)+dot(4.5,f18(4.5),sx,sy)+lab(6,0,sx,sy,'$A$','above right')+lab(4.5,f18(4.5),sx,sy,'$P$','above right')+lab(5,9.2,sx,sy,'$y=6x-x^2$','right',MAVI)
q('0018',tipId='par-ucgen',tip='Parabolle oluşan şekillerin alanı',z='zor',alt='Hareketli Nokta',kaz='Parabol üzerinde sınırlı aralıkta hareket eden noktayla oluşan üçgenin alanının en büyük değerini bulur.',kalip='şekilli',
 kart='K-APAR2-04 (hareketli P, tepe aralığın dışında) · taban sabit',
 metin='Şekilde, y = 6x − x² parabolü x eksenini orijinde ve A noktasında kesmektedir. P noktası, parabolün apsisi 4 ile 5 arasında (uçlar dahil) kalan ve şekilde kalın çizilen yayı üzerinde hareket etmektedir.\nBuna göre O orijin olmak üzere OAP üçgeninin alanı en fazla kaç birimkare olabilir?',
 dogru=v,yan=[(e[0],'P’nin ordinatı yerine apsisini (4) yükseklik alıp 6 · 4/2 hesaplamış.','dikkat'),(e[1],'Alanı yayın sağ ucunda (x = 5) hesaplamış: 6 · 5/2.','dikkat'),(e[2],'Tepe noktasını (x = 3) aralıkta sanıp 6 · 9/2 hesaplamış.','dikkat'),(e[3],'En büyük alanı 6 · 8 olarak 1/2 çarpanını unutarak yazmış.','dikkat')],
 istenen='OAP üçgeninin en büyük alanı (birimkare).',ip=['Taban sabit; yükseklik P’nin ordinatıdır. Tepe noktasının yay üzerinde olup olmadığına bak.'],bilgi=[UCG],sekil=fig(body),
 ad=[A('A noktası','6x − x² = 0.','A(6, 0), taban |OA| = 6'),A('Yükseklik','P’nin ordinatı y = 6t − t²; tepe apsisi 3, yay 4 ≤ t ≤ 5 aralığında azalandır.','En büyük ordinat t = 4’te: 8'),A('Alan','Taban × yükseklik / 2.','6 · 8/2 = 24')],
 puf='t = 3’ün yay üzerinde olmadığını işaretle, sonra uç değerleri karşılaştır.')

# ================= 19 orta · fıskiye =================
f19=lambda x:Fr(-1,16)*(x-4)**2+4
assert f19(0)==3 and f19(12)==0
v=12
e=[4,8,16,20]
assert len({v,*e})==5 and (-Fr(1,4)*(8-4)**2+4)==0 and 8+8==16 and 4+16==20
sx=sy=0.42
body=axes(0,13,0,5,sx,sy,xs=13,ys=5,nums=False)+'\n'
body=f'\\draw[-{{Stealth}},thick] (-0.5*{sx},0) -- (13.6*{sx},0) node[right] {{yer}};\\draw[-{{Stealth}},thick] (0,-0.3*{sy}) -- (0,5.5*{sy}) node[above] {{$y$}};\n'
body+=seg(0,0,13,0,sx,sy,'green!50!black',',line width=2pt')+curve(f19,0,12.5,sx,sy,MAVI,0,4.3)+'\n'+seg(4,0,4,4,sx,sy,'gray',',dashed')+seg(0,4,4,4,sx,sy,'gray',',dashed')
body+=dot(0,3,sx,sy)+dot(4,4,sx,sy)
body+=f'\\node[left,font=\\footnotesize] at (0,3*{sy}) {{$3$ m}};\\node[left,font=\\footnotesize] at (0,4*{sy}) {{$4$ m}};\\node[below,font=\\footnotesize] at (4*{sx},0) {{$4$ m}};'
body+=lab(4,4,sx,sy,'tepe','above',MAVI)+lab(0.5,2.3,sx,sy,'fıskiye','right')
q('0019',tipId='par-uygulama',tip='Gelir ve yörünge uygulaması',z='orta',alt='Su Yörüngesi',kaz='Parabol biçimli bir yörüngenin tepe noktası ve başlangıç yüksekliğinden denklemi kurup yere düştüğü noktayı bulur.',kalip='hikâyeli',
 kart='K-APAR2-07 (yörünge, yere düşme) · başlangıç yüksekliği ≠ 0',
 metin='Bahçedeki bir fıskiyeden yatay zemine doğru fışkıran suyun yörüngesi, şekilde gösterilen bir parabol yayıdır. Fıskiye zeminden 3 metre yüksekte olup yörüngenin tepe noktasının zeminden yüksekliği ve fıskiyeye yatay uzaklığı şekilde gösterilmiştir.\nBuna göre su, fıskiyenin bulunduğu düşey doğrudan yatay olarak kaç metre ötede zemine düşer?',
 dogru=v,yan=[(e[0],'Zemine düşme uzaklığı yerine tepe noktasının yatay uzaklığını (4) yazmış.','dikkat'),(e[1],'Yörüngenin başlangıç yüksekliğini sıfır sanıp (x − 4)² = 16 bulmuş: 2 · 4.','dikkat'),(e[2],'(x − 4)² = 64 çözümünde x − 4 = 8 farkını almak yerine iki kökün uzaklığını (16) yazmış.','dikkat'),(e[3],'(x − 4)² = 64 denkleminde karekökü 16 sanıp 4 + 16 yazmış.','dikkat')],
 istenen='Suyun düştüğü noktanın yatay uzaklığı (m).',ip=['Tepe ve fıskiyenin konumu hangi denklemi belirler?'],bilgi=[UYG],sekil=fig(body),
 ad=[A('Denklemi yaz','Tepe (4, 4), fıskiye (0, 3).','y = a(x − 4)² + 4, 16a + 4 = 3 → a = −1/16'),A('Zemin','y = 0 denklemi çözülür.','(x − 4)² = 64 → x − 4 = 8 (x > 4)'),A('Uzaklık','Pozitif kök alınır.','x = 12 m')],
 puf='Bulduğun a ile x = 0 için yüksekliğin 3 olduğunu denetle.')

# ================= 20 zor · |f(x)| = m =================
f20=lambda x:x*x-2*x-8
def nk(m): return len({x for x in [Fr(k,1000) for k in range(-10000,10000)] if abs(f20(x))==m})
# kök sayısını analitik say
def kok_say(m):
    # f(x)=m ve f(x)=-m çözümleri
    s=set(); 
    for c in (m,-m):
        D=4+4*(8+c)  # x²-2x-8-c=0 : D=4-4(-8-c)
        if D>0:
            r=math.sqrt(D); s|={round((2+r)/2,9),round((2-r)/2,9)}
        elif D==0: s.add(1.0)
    return len(s)
ms=[m for m in range(1,20) if kok_say(m)==4]; assert ms==list(range(1,9)),ms
v=sum(ms); assert v==36 and kok_say(9)==3
e=[0,9,28,45]; assert sum(range(1,10))==45 and sum(range(1,8))==28 and len({v,*e})==5
sx=0.62; sy=0.3
body=axes(-3,5,-9,5,sx,sy,ys=3)+'\n'+curve(f20,-2.8,4.8,sx,sy,MAVI,-9.2,5)+'\n'+dot(-2,0,sx,sy)+dot(4,0,sx,sy)+dot(1,-9,sx,sy)+lab(-0.7,-7,sx,sy,'$y=f(x)$','left',MAVI)
q('0020',tipId='par-goruntu',tip='Kapalı aralıkta görüntü ve mutlak değer',z='zor',alt='Mutlak Değer',kaz='Parabolün mutlak değerinin grafiği ile yatay doğrunun kesim sayısından parametrenin tam sayı değerlerini bulur.',kalip='grafik',
 kart='K-APAR2-06 (|f(x)| = m kök sayısı) · tepe ordinatı −9',
 metin='Şekilde, baş katsayısı 1 olan f fonksiyonunun grafiği olan parabol verilmiştir; işaretli noktalar ızgara çizgilerinin kesişimindedir.\nm pozitif bir tam sayı olmak üzere |f(x)| = m denkleminin tam 4 farklı gerçel kökü olduğuna göre, m’nin alabileceği değerlerin toplamı kaçtır?',
 dogru=v,yan=[(e[0],'Hem pozitif hem negatif m değerlerini (−8’den 8’e) alıp toplamını yazmış.','dikkat'),(e[1],'Tepe ordinatının mutlak değerini (9) cevap sanmış.','dikkat'),(e[2],'Tepe ordinatının mutlak değerini 8 sanıp m = 8’i teğet kabul ederek dışlamış: 1’den 7’ye toplam.','dikkat'),(e[3],'m = 9 için de 4 kök olduğunu düşünüp 1’den 9’a toplamış; teğet olunca kök sayısının 3 olduğunu atlamış.','dikkat')],
 istenen='m değerlerinin toplamı.',ip=['|f|’in grafiğini çiz.'],bilgi=[GOR],sekil=fig(body),
 ad=[A('f’yi oku','Kökler −2 ve 4, tepe (1, −9).','f(x) = x² − 2x − 8'),A('|f| grafiği','Alt kısım katlanır: tepe (1, 9) ve m = 9 doğrusu teğettir.','0 < m < 9 için 4 kök, m = 9 için 3 kök'),A('Tam sayılar','m = 1, 2, …, 8.','Toplam = 36')],
 puf='m = 9 ve m = 10 için kök sayılarını ayrı ayrı say.')

# ---------- yazım ----------
SC='/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/par2'
def bitir_ayt(P,onek,k):
    HV=os.path.join(HD,'..')
    for q_ in P.ANA: q_['kardes']=None
    P.yaz(os.path.join(HD,f'{onek}-1.json'),SC+'/bos.json')
    tipler={}
    for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=k))['kartlar'].append(c['id'])
    json.dump(dict(konu=P.konu_adi,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 AYT Matematik çıkmış soruları ve yayın soru bankaları (yalnız mantık), MEB 10–11. sınıf müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar',f'{onek}.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler))
bitir_ayt(P,'parabeliki',UK)
import collections; print(collections.Counter(x['cevap']['sik'] for x in P.ANA))
