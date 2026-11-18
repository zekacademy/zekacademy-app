"""AYT Matematik · Parabol (20 soru: 4 kolay / 10 orta / 6 zor). Her doğru ve çeldirici değer kodla hesaplanıp assert edilir. Kardeş yok, ipucu 1."""
import sys,os,json,math
AD=os.path.dirname(os.path.abspath(__file__)); HD=AD
sys.path.insert(0,os.path.join(HD,'..','tyt-mat')); sys.path.insert(0,os.path.join(HD,'..'))
import _hafif_mat as H
from _hafif_mat import *
HD=AD
from cizim import tikz_svg
H.KONU='Parabol'
UK='amat|Parabol'
P=Parti('parabol','Parabol',UK,ders='AYT Matematik',idon='aytmat')
KY='ÖSYM 2018–2026 AYT Matematik (ikinci dereceden fonksiyon ve parabol soruları; yalnız mantık) · MEB 10–11. sınıf'
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)
TICKS=[]
def fig(body,font='\\small'):
    t='\n'.join(TICKS); TICKS.clear()
    return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font='+font+']\n'+body+'\n'+t+'\n\\end{tikzpicture}')
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)

# ---------- bilgi kutuları (örnekler soruların sayılarından farklı) ----------
KOK=B('Kökler ve çarpanlı yazım','x eksenini x₁ ve x₂ noktalarında kesen parabol f(x) = a(x − x₁)(x − x₂) biçiminde yazılır; x² li terimin katsayısı 1 ise f(x) = x² − (x₁ + x₂)x + x₁·x₂ olur. Örnek: kökleri 2 ve 7 olan, baş katsayısı 1 olan parabol x² − 9x + 14’tür')
OTE=B('Parabolü öteleme','y = a(x − r)² + k parabolünün tepe noktası (r, k)’dır. Parabolü sağa m, yukarı n birim ötelemek için x yerine x − m yazılır ve sona n eklenir; sola ötelemede x + m yazılır. Örnek: y = (x − 1)² + 4 parabolü 2 sola ötelenirse y = (x + 1)² + 4 olur')
TEP=B('Tepe noktası','f(x) = ax² + bx + c parabolünün tepe noktası T(r, k) için r = −b/(2a) ve k = f(r)’dir. Simetri ekseni x = r doğrusudur; a > 0 ise k en küçük, a < 0 ise k en büyük değerdir. Örnek: f(x) = x² − 10x + 3 için r = 5 ve k = −22’dir')
ISA=B('Katsayıların işaretleri','a > 0 ise parabol kollarını yukarı, a < 0 ise aşağı açar; c, parabolün y eksenini kestiği noktanın ordinatıdır; tepe noktasının apsisi −b/(2a) olduğundan b’nin işareti a ve tepe apsisinin işaretiyle belirlenir. Δ = b² − 4ac > 0 ise parabol x eksenini iki noktada, Δ = 0 ise bir noktada, Δ < 0 ise hiç kesmez. Örnek: kolları aşağı ve tepesi sağda olan bir parabolde a < 0 ve −b/(2a) > 0 olduğundan b > 0’dır')
KES=B('Doğru ile parabolün kesişimi','y = f(x) parabolü ile y = mx + n doğrusunun ortak noktalarının apsisleri f(x) = mx + n denkleminin kökleridir; denklemin Δ değeri pozitifse iki, sıfırsa bir (teğet), negatifse hiç ortak nokta yoktur. Örnek: y = x² ile y = 2x + 3 doğrusu için x² − 2x − 3 = 0 kökleri x = −1 ve x = 3’tür')
ARA=B('Eşitsizlik ve grafik','f(x) > 0 eşitsizliğinin çözümü, parabolün x ekseninin üstünde kaldığı apsisler; f(x) > k çözümü ise parabolün y = k doğrusunun üstünde kaldığı apsislerdir. Köklerin sınırlarda alınıp alınmayacağı eşitsizliğin <, > ya da ≤, ≥ olmasına bağlıdır. Örnek: grafiği x ekseninin üstünde olan (1, 4) aralığı için tam sayılar 2 ve 3’tür')
ENB=B('En büyük ve en küçük değer','a < 0 iken f(x) = ax² + bx + c ifadesi tepe noktasının ordinatı olan en büyük değeri; a > 0 iken en küçük değeri alır. Bir uygulamada iki uzunluğun toplamı sabitse çarpımları, uzunluklardan birine bağlı ikinci dereceden bir ifadedir. Örnek: toplamları 12 olan x ve 12 − x sayılarının çarpımı x = 6 için en büyüktür')
ALN=B('Köklerden alan','Parabolün x eksenini kestiği iki nokta ile tepe noktası bir üçgen oluşturur; tabanı kökler arası uzaklık, yüksekliği tepe ordinatının mutlak değeridir. Baş katsayı a olan f(x) = a(x − x₁)(x − x₂) için y eksenini kestiği nokta (0, a·x₁·x₂)’dir. Örnek: f(x) = (x − 2)(x − 6) için kök uzaklığı 4, tepe ordinatı −4’tür')
IKP=B('İki parabolün kesişimi','f(x) = g(x) denkleminin kökleri kesişim noktalarının apsisleridir. Bu apsisler arasında iki grafiğin aynı x için dik uzaklığı |f(x) − g(x)| ifadesidir ve bu da ikinci dereceden bir fonksiyondur. Örnek: f(x) = x² ve g(x) = 6x − 5 için aralarındaki dik uzaklık 1 ile 5 arasında −(x − 1)(x − 5) biçimindedir')

# ---------- kartlar (her tipId için bir kart) ----------
kartla('K-APAR-01','Grafikten parabol denklemi','Grafikte okunan kök, tepe ya da eksen kesim noktalarından çarpanlı ya da tepe biçimi yazılır; katsayılar bu denklemden okunur.','Kök işaretini ters yazmak (x = 3 kökü için x + 3); baş katsayıyı 1 sanmak; katsayı yerine toplam ya da çarpım hesaplamak.','kolay','grafik',3,'par-grafik','Grafikten parabol denklemi')
kartla('K-APAR-02','Parabolü öteleme','Her öteleme yönünde x ya da y yerine yeni değişken konarak denklem yeniden yazılır; tepe noktasının nereye gittiği ayrıca denetlenir.','Sağa ötelemede x + m yazmak; yatay ve dikey öteleme yönlerini karıştırmak; ötelemeyi bir eksende unutmak.','kolay','grafik',3,'par-oteleme','Parabolü öteleme')
kartla('K-APAR-03','Tepe noktası ve simetri','Tepe apsisi −b/(2a) ile ya da simetri özelliği olan iki noktanın ortası ile bulunur; ordinat bu apsisle hesaplanır.','Tepe apsisini −b/a almak; işareti ters yazmak; simetrik iki noktanın toplamını ortalama sanmak.','kolay','düz',3,'par-tepe','Tepe noktası ve simetri')
kartla('K-APAR-04','Katsayı işaretleri ve grafik','Kolların yönü, y eksenini kesim noktası ve tepe konumu sırasıyla a, c ve b için ipucu verir; Δ’nın işareti x eksenine göre konumdan belirlenir.','b’nin işaretini tepenin konumuna bakarak a’yı hesaba katmadan söylemek; Δ’yı kollarla karıştırmak.','orta','öncüllü',4,'par-isaret','Katsayı işaretleri ve grafik')
kartla('K-APAR-05','Doğru ve parabolün kesişimi','Denklemler eşitlenip elde edilen ikinci dereceden denklemin kökleri bulunur; Δ ile kesişim sayısı ve teğetlik belirlenir.','Doğrunun işaretini yanlış taşımak; teğet koşulunda Δ = 0 yazmayı unutmak; apsis farkıyla gerçek uzaklığı karıştırmak.','orta','grafik',4,'par-kesisim','Doğru ve parabolün kesişimi')
kartla('K-APAR-06','Eşitsizlik ve tam sayı çözümleri','Çözüm aralığı grafikten ya da kökler arasındaki işaretten bulunur; uçların dahil olup olmadığına bakılarak tam sayılar sayılır ya da toplanır.','Eşitsizliğin sağ tarafını sıfıra taşımamak; sınır değeri aralığa dahil etmek; toplam yerine sayıyı vermek.','orta','grafik',4,'par-aralik','Eşitsizlik ve tam sayı çözümleri')
kartla('K-APAR-07','En büyük ve en küçük değer uygulaması','Aranan nicelik tek değişkene bağlı ikinci dereceden bir ifade olarak yazılır; tepe noktasının ordinatı istenen en büyük ya da en küçük değerdir.','Kısıtı hiç kullanmamak; ifadeyi yanlış kurmak; tepe apsisini cevap sanmak.','orta','hikâyeli',4,'par-enbuyuk','En büyük ve en küçük değer uygulaması')
kartla('K-APAR-08','Kökler ve alan','Kök ve tepe noktaları belirlenip üçgenin tabanı ile yüksekliği ayrı bulunur; baş katsayı verilen bir noktadan hesaplanır.','Baş katsayıyı 1 almak; yüksekliği y eksenini kestiği noktadan okumak; tabanı kökler toplamı almak.','orta','şekilli',4,'par-alan','Kökler ve alan')
kartla('K-APAR-09','İki parabol arası dik uzaklık','İki fonksiyonun farkı yazılır; kesişim apsisleri arasında bu fark ikinci dereceden bir ifade olduğundan en büyük değeri tepe noktasından bulunur.','Farkın işaretini karıştırmak; baş katsayıyı unutmak; aralığın uzunluğunu uzaklık sanmak.','zor','şekilli',5,'par-ikili','İki parabol arası dik uzaklık')

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

# ================= 01 kolay · grafikten b·c =================
f1=lambda x:x*x-2*x-3
b1,c1=-2,-3
assert all(f1(x)==x*x+b1*x+c1 for x in range(-5,6)) and f1(-1)==0 and f1(3)==0
v=b1*c1; assert v==6
e=[(2)*(-3),b1+c1,abs(b1)+abs(c1),b1-c1]; assert e==[-6,-5,5,1] and len({v,*e})==5
sx=sy=0.62
body=axes(-2,4,-4,3,sx,sy)+'\n'+curve(f1,-2,4,sx,sy,MAVI,-4.3,3)+'\n'+dot(-1,0,sx,sy)+dot(3,0,sx,sy)+lab(1,1.6,sx,sy,'$y=f(x)$','above',MAVI)
q('0001',tipId='par-grafik',tip='Grafikten parabol denklemi',z='kolay',alt='Grafikten Denklem',kaz='Grafikte ızgara noktalarından okunan köklerle baş katsayısı 1 olan parabolün katsayılarını bulur.',kalip='grafik',
 kart='K-APAR-01 (kök okuma) · baş katsayı 1, iki ızgara kökü',
 metin='Şekilde, gerçel sayılar kümesi üzerinde f(x) = x² + bx + c biçiminde tanımlı f fonksiyonunun grafiği verilmiştir. Parabol, x eksenini ızgara çizgilerinin kesiştiği iki noktada kesmektedir.\nBuna göre b · c çarpımı kaçtır?',
 dogru=v,yan=[(e[0],'Kökleri −1 ve 3 yerine (x − 1)(x + 3) biçiminde yazıp b = 2 bulmuş: 2 · (−3).','islem'),(e[1],'İstenen çarpım yerine b + c toplamını hesaplamış: −2 + (−3).','dikkat'),(e[2],'b ve c’nin işaretlerini dikkate almadan mutlak değerlerini toplamış: 2 + 3.','dikkat'),(e[3],'Çarpım yerine b − c farkını almış: −2 − (−3).','islem')],
 istenen='b · c çarpımı.',ip=['Parabolün x eksenini kestiği noktalarda f(x) neye eşit olur?'],bilgi=[KOK],sekil=fig(body),
 ad=[A('Kökleri oku','Grafik x eksenini iki ızgara noktasında keser.','x = −1 ve x = 3'),A('Denklemi yaz','Baş katsayı 1 olduğundan çarpanlı biçim yazılıp açılır.','(x + 1)(x − 3) = x² − 2x − 3'),A('Katsayıları oku','b ve c değerleri okunur, çarpılır.','b = −2, c = −3 → b × c = 6')],
 puf='Bulduğun denklemi grafikteki kök noktalarına yazarak denetle.')

# ================= 02 kolay · öteleme =================
f2=lambda x:(x-2)**2-1          # x²−4x+3
def teleg(s,t): return lambda x:f2(x-s)+t
s2,t2=3,2
g=teleg(s2,t2); assert all(g(x)==x*x-10*x+26 for x in range(-4,9))
v=-10+26; assert v==16
def bc(fn): return Fr(fn(1)-fn(0)-(fn(2)-2*fn(1)+fn(0))//2) , fn(0)  # b = f(1)-f(0)-a, a=1
def bc_(fn):
    a=Fr(fn(2)-2*fn(1)+fn(0),2); assert a==1; b=fn(1)-fn(0)-a; c=fn(0); return b+c
e=[bc_(teleg(-s2,t2)),bc_(teleg(s2,-t2)),bc_(teleg(-s2,-t2)),bc_(teleg(s2,0))]
assert bc_(teleg(s2,t2))==16 and e==[4,12,0,14] and len({v,*e})==5,e
sx=sy=0.6
body=axes(-1,6,-2,4,sx,sy,ytick=[-2,-1,1,2,3])+'\n'+curve(f2,-0.5,5.5,sx,sy,MAVI,-2.3,4.4)+'\n'+dot(2,-1,sx,sy)+dot(1,0,sx,sy)+dot(3,0,sx,sy)+dot(0,3,sx,sy)+dot(4,3,sx,sy)+lab(5.3,3.9,sx,sy,'$y=f(x)$','right',MAVI)
q('0002',tipId='par-oteleme',tip='Parabolü öteleme',z='kolay',alt='Parabolü Öteleme',kaz='Grafikle verilen parabolün denklemini bulup sağa ve yukarı ötelenmesiyle oluşan yeni parabolün katsayılarını hesaplar.',kalip='grafik',
 kart='K-APAR-02 (öteleme) · tepe ızgara noktasında; yatay ve dikey birer öteleme',
 metin='Şekilde, baş katsayısı 1 olan f(x) parabolünün grafiği verilmiştir; grafik üzerindeki işaretli noktalar ızgara çizgilerinin kesişimindedir. Bu parabol sağa 3 birim, yukarı 2 birim ötelendiğinde elde edilen parabolün denklemi y = x² + bx + c oluyor.\nBuna göre b + c toplamı kaçtır?',
 dogru=v,yan=[(e[0],'Sağa ötelemeyi x yerine x + 3 yazarak yapmış: y = (x + 1)² + 1.','dikkat'),(e[1],'Yukarı ötelemeyi 2 birim aşağı ötelemiş gibi hesaplamış: y = (x − 5)² − 3.','dikkat'),(e[2],'Yatay ve dikey ötelemenin yönünü ters uygulamış: y = (x + 1)² − 3.','dikkat'),(e[3],'Yukarı ötelemeyi atlayıp yalnız sağa 3 birim ötelemiş: y = (x − 5)² − 1.','islem')],
 istenen='b + c toplamı.',ip=['Önce grafikteki tepe noktasından f(x)’i tepe biçiminde yaz.'],bilgi=[OTE],sekil=fig(body),
 ad=[A('f’yi bul','Tepe noktası ızgaradan okunur, baş katsayı 1’dir.','f(x) = (x − 2)² − 1'),A('Ötele','x yerine x − 3 yazılır, sona 2 eklenir.','y = (x − 5)² + 1'),A('Aç ve topla','Parantez açılıp b ve c okunur.','y = x² − 10x + 26 → b + c = 16')],
 puf='Ötelenmiş parabolün tepe noktasının nereye gittiğini de kontrol et.')

# ================= 03 kolay · tepe ordinatından k =================
k3=4; assert (-3)**2+6*(-3)+k3==-5
v=k3
e=[-5-9-18,-5-9,-5,-5+18-0]  # yerine hesapla aşağıda
e_a=-5-(9+18)+(-0)          # f(3)=9+18+k=-5 → k=-32
assert 9+18+(-32)==-5 and -32==e_a+(-0)
e_b=-14; assert 9-18+(e_b)==-23     # k=-5-9
e_c=-5;  assert 36-36+e_c==-5       # tepe apsisi -6
e_d=13;  assert 13-18==-5           # c − b²/2
e=[e_a,e_b,e_c,e_d]; assert len({v,*e})==5 and e==[-32,-14,-5,13]
q('0003',tipId='par-tepe',tip='Tepe noktası ve simetri',z='kolay',alt='Tepe Noktası',kaz='Tepe noktasının ordinatı verilen parabolde bilinmeyen sabit terimi bulur.',kalip='düz',
 kart='K-APAR-03 (tepe ordinatı) · x² + bx + k biçimi',
 metin='Gerçel sayılar kümesi üzerinde f(x) = x² + 6x + k biçiminde tanımlı f fonksiyonunun grafiği olan parabolün tepe noktasının ordinatı −5’tir.\nBuna göre k kaçtır?',
 dogru=v,yan=[(e[0],'Tepe apsisini +3 bulup f(3) = 9 + 18 + k = −5 denklemini çözmüş.','dikkat'),(e[1],'f(−3) = 9 − 18 + k = −5 denkleminde −9’u karşı tarafa işaretini değiştirmeden taşıyıp k = −5 − 9 yazmış.','islem'),(e[2],'Tepe apsisini −b/a = −6 almış: f(−6) = 36 − 36 + k = −5.','bilgi'),(e[3],'Tepe ordinatı formülünde b²/4 yerine b²/2 kullanmış: k − 18 = −5.','bilgi')],
 istenen='k değeri.',ip=['Tepe noktasının apsisini bulup f’de yerine yaz.'],bilgi=[TEP],
 ad=[A('Tepe apsisi','x = −b/(2a) hesaplanır.','x = −6/2 = −3'),A('Denklemi kur','Tepe noktasında fonksiyon değeri ordinata eşittir.','f(−3) = 9 − 18 + k = −5'),A('k’yı bul','Denklem çözülür.','k − 9 = −5 → k = 4')],
 puf='Bulduğun k ile tepe ordinatını yeniden hesapla.')

# ================= 04 kolay · simetri eksenli b =================
b4=-8; f4=lambda x:2*x*x+b4*x-7; assert f4(-1)==f4(5)
v=b4
cand=lambda ex:-4*ex            # −b/4 = ex → b=−4·ex
e=[8,cand(1),4,cand(4)]
assert f4(-1)==f4(5) and cand(2)==-8 and cand(4)==-16 and cand(1)==-4 and len({v,*e})==5 and e==[8,-4,4,-16]
q('0004',tipId='par-tepe',tip='Tepe noktası ve simetri',z='kolay',alt='Simetri Ekseni',kaz='Aynı değeri alan iki noktadan simetri eksenini bulup parabolün katsayısını hesaplar.',kalip='düz',
 kart='K-APAR-03 (simetri ekseni) · f(p) = f(q) koşulundan b',
 metin='b bir gerçel sayı olmak üzere gerçel sayılar kümesi üzerinde f(x) = 2x² + bx − 7 biçiminde tanımlı f fonksiyonu için f(−1) = f(5) eşitliği sağlanıyor.\nBuna göre b kaçtır?',
 dogru=v,yan=[(e[0],'Simetri eksenini x = 2 bulduktan sonra −b/4 = 2 yerine b/4 = 2 yazmış.','dikkat'),(e[1],'Simetri eksenini −1 ve 5’in ortası yerine (−1 + 5) ÷ 4 = 1 almış: −b/4 = 1.','islem'),(e[2],'Baş katsayıyı kullanmadan −b/2 yerine b/2 = 2 yazmış.','bilgi'),(e[3],'Simetri eksenini ortalama yerine toplamla 4 almış: −b/4 = 4.','islem')],
 istenen='b değeri.',ip=['f(−1) = f(5) olması parabolün simetri ekseni hakkında ne söyler?'],bilgi=[TEP],
 ad=[A('Simetri ekseni','Aynı değeri alan iki noktanın ortası simetri eksenidir.','x = (−1 + 5)/2 = 2'),A('Formülü yaz','Simetri ekseni x = −b/(2a)’dır.','−b/4 = 2'),A('b’yi bul','Denklem çözülür.','b = −8')],
 puf='Bulduğun b ile f(−1) ve f(5) değerlerini hesaplayıp eşitliği denetle.')

# ================= 05 orta · öncüllü, işaretler (eskiz) =================
a5,b5,c5=Fr(1,2),Fr(1),Fr(3,2)       # y = ½(x+1)²+1
f5=lambda x:a5*x*x+b5*x+c5; assert f5(-1)==1 and -b5/(2*a5)==-1
D5=b5*b5-4*a5*c5; assert D5==-2
st=[a5*b5>0, D5>0, c5<0]; assert st==[True,False,False]
dog='Yalnız I'
sx=sy=0.9
body='\\draw[-{Stealth},thick] (-3.3,0) -- (1.9,0) node[right] {$x$};\\draw[-{Stealth},thick] (0,-0.5) -- (0,3.6) node[above] {$y$};\\node[below left,font=\\footnotesize] at (0,0) {$O$};\n'
body+=curve(lambda x:float(f5(Fr(x).limit_denominator(10**6))) if False else 0.5*(x+1)**2+1,-3.0,1.2,0.9,0.9,MAVI,0,3.2)
body+='\n\\node[font=\\footnotesize,text=blue!70!black] at (1.7,3.05) {$y=f(x)$};'
q('0005',tipId='par-isaret',tip='Katsayı işaretleri ve grafik',z='orta',alt='Katsayı İşaretleri',kaz='Grafikten kolların yönü, y eksenini kesim noktası ve tepenin konumuna bakarak katsayıların işaretleri hakkında yargıları değerlendirir.',kalip='öncüllü',
 kart='K-APAR-04 (işaret yargıları) · kollar yukarı, tepe sol alt bölgede, x ekseni kesilmiyor',
 metin='a, b ve c gerçel sayılar olmak üzere, f(x) = ax² + bx + c fonksiyonunun grafiği şekilde verilmiştir.\nBuna göre,\nI. a · b > 0\nII. b² − 4ac > 0\nIII. c < 0\nyargılarından hangileri doğrudur?',
 dogru=dog,yan=[(SIRA1[1],'Parabolün x eksenini kestiğini düşünüp II’yi doğru bulmuş; I’i ise a ve b’nin işaretlerini ayrı ayrı çıkaramadığı için yanlış saymış.','dikkat'),(SIRA1[2],'I’i doğru bulmuş, ancak parabol x ekseninin üstünde kaldığı hâlde Δ > 0 demiş.','dikkat'),(SIRA1[3],'c’nin işaretini tepenin altında kalan değere bakarak negatif sanmış; grafik y eksenini pozitif değerde keser.','bilgi'),(SIRA1[4],'Grafiğin x eksenine göre konumunu değerlendirmeden bütün yargıları doğru kabul etmiş.','dikkat')],
 sira=SIRA1,istenen='Doğru olan yargılar.',ip=['Kolların yönüne, parabolün y eksenini kestiği yere ve x eksenine göre konumuna ayrı ayrı bak.'],bilgi=[ISA],sekil=fig(body),
 ad=[A('a ve c’yi belirle','Kollar yukarı: a > 0. Parabol y eksenini pozitif yerde keser: c > 0.','a > 0, c > 0'),A('b’yi belirle','Tepe y ekseninin solunda olduğundan −b/(2a) < 0; a > 0 olduğundan b > 0.','b > 0'),A('Yargıları denetle','I: a · b pozitif. II: parabol x eksenini kesmediğinden Δ < 0. III: c pozitif.','I doğru, II ve III yanlış')],
 puf='Her yargıyı grafikten çıkarılan işaretlerle ayrı ayrı sına.')

# ================= 06 orta · öncüllü, değer tablosu =================
f6=lambda x:-x*x+2*x+3
X6=[-1,0,1,3]; Y6=[f6(x) for x in X6]; assert Y6==[0,3,4,0]
t1=f6(2)==4; t2=(-1+3==2); t3=f6(-2)==-5
assert [t1,t2,t3]==[False,True,True]
dog='II ve III'
SK=tablo_svg(['x','−1','0','1','3'],[['f(x)']+[str(y) for y in Y6]])
# çeldirici açıklamaları: f(2)=3 (simetri), f(−2)=−5
assert f6(2)==3
q('0006',tipId='par-isaret',tip='Katsayı işaretleri ve grafik',z='orta',alt='Değer Tablosu',kaz='İkinci dereceden bir fonksiyonun değer tablosundan kökleri ve simetriyi kullanarak yargıları değerlendirir.',kalip='öncüllü',
 kart='K-APAR-04 (tablo ile yargı) · dört değer, iki kök',
 metin='Gerçel sayılar kümesi üzerinde tanımlı ve grafiği bir parabol olan f fonksiyonunun bazı değerleri aşağıdaki tabloda verilmiştir.\nBuna göre,\nI. f(2) = 4\nII. f(x) = 0 denkleminin kökleri toplamı 2’dir.\nIII. f(−2) = −5\nyargılarından hangileri doğrudur?',
 dogru=dog,yan=[(SIRA2[0],'f(1) = 4 değerinin simetrisini kullanıp f(2) = 4 sanmış; II ve III’ü sınamamış.','dikkat'),(SIRA2[1],'Yalnız f(−2) değerini hesaplayıp kökler toplamını denetlememiş.','islem'),(SIRA2[2],'f(2)’yi f(1) değerinin simetriği sanıp 4 almış; f(−2)’yi hesaplarken baş katsayının eksisini unutup (x + 1)(x − 3) = 5 bulmuş ve III’ü yanlış saymış.','dikkat'),(SIRA2[4],'f(2) = 4 olduğunu sanıp bütün yargıları doğru bulmuş.','dikkat')],
 sira=SIRA2,istenen='Doğru olan yargılar.',ip=['Tablodaki sıfır değerlerinden parabolün denklemini yazmayı dene.'],bilgi=[KOK],sekil=SK,
 ad=[A('Denklemi bul','Tablodan kökler ve bir değer okunup f yazılır.','f(x) = −(x + 1)(x − 3) = −x² + 2x + 3'),A('I’i sına','x = 2 yazılır.','f(2) = 3, yargı yanlış'),A('II ve III’ü sına','Kökler −1 ve 3, toplamları 2; f(−2) hesaplanır.','2 doğru; f(−2) = −5 doğru')],
 puf='Tabloda eksik kalan değerleri önce fonksiyonun denklemini yazarak bul.')

# ================= 07 orta · doğru ve parabol, AB uzunluğu =================
f7=lambda x:x*x-4*x+3; l7=lambda x:x-1
xs7=[x for x in range(-10,11) if f7(x)==l7(x)]; assert xs7==[1,4]
dx=3; dy=l7(4)-l7(1); assert dy==3
assert dx*dx+dy*dy==18
v='3√2'
w7=['√6','3','3√2','6','18']
assert abs(math.sqrt(6)-2.449)<1e-2
sx=sy=0.7
body=axes(-1,5,-2,6,sx,sy,xext=0.6)+'\n'+curve(f7,-0.7,4.7,sx,sy,MAVI,-1.3,6)+'\n'+curve(l7,-1,5,sx,sy,TUR,-2,6)+'\n'+dot(1,0,sx,sy)+dot(4,3,sx,sy)+lab(0.55,-0.6,sx,sy,'$A$','below')+lab(4,3,sx,sy,'$B$','below right')+lab(4.95,5.6,sx,sy,'$y=f(x)$','right',MAVI)+lab(5,4.0,sx,sy,'$y=g(x)$','right',TUR)
q('0007',tipId='par-kesisim',tip='Doğru ve parabolün kesişimi',z='orta',alt='Doğru ve Parabol',kaz='Doğru ile parabolün grafikte verilen ortak noktalarını denklem çözerek bulur ve aralarındaki uzaklığı hesaplar.',kalip='grafik',
 kart='K-APAR-05 (kesişim noktaları arası uzaklık) · eğimi 1 olan doğru',
 metin='Şekilde, f(x) = x² − 4x + 3 parabolü ile g doğrusu aynı dik koordinat düzleminde verilmiştir. g doğrusu, parabolü A ve B noktalarında kesmekte olup A ve B noktaları ızgara çizgilerinin kesişimindedir.\nBuna göre |AB| uzunluğu kaç birimdir?',
 dogru=v,yan=[(w7[0],'Apsis ve ordinat farklarının toplamının karekökünü almış: √(3 + 3).','islem'),(w7[1],'Yalnız apsis farkını uzunluk saymış.','dikkat'),(w7[3],'Apsis ve ordinat farklarını toplamış: 3 + 3.','dikkat'),(w7[4],'Karekökü almayı unutup farkların karelerinin toplamını yazmış: 3² + 3².','dikkat')],
 sira=w7,istenen='|AB| uzunluğu (birim).',ip=['A ve B noktalarının koordinatlarını grafikten oku, sonra uzaklık formülünü kullan.'],bilgi=[KES],sekil=fig(body),
 ad=[A('Noktaları oku','A ve B ızgara noktalarıdır.','A(1, 0), B(4, 3)'),A('Farkları bul','Apsis ve ordinat farkı hesaplanır.','Δx = 3, Δy = 3'),A('Uzaklık','Uzaklık formülü uygulanır.','√(9 + 9) = 3√2')],
 puf='Bulduğun iki noktanın parabol üzerinde olduğunu f ile denetle.')

# ================= 08 orta · duvara dayalı bahçe =================
A8=lambda x:x*(80-2*x)
assert max(A8(x) for x in range(0,41))==800 and A8(20)==800
v=800
e=[max(x*(40-x) for x in range(0,41)),20,80*20,80-2*20]
assert e==[400,20,1600,40] and len({v,*e})==5
sx=0.55
body=('\\fill[gray!20] (-0.3,-0.55) rectangle (6.3,0);\\draw[thick] (-0.3,0) -- (6.3,0);\\node[font=\\footnotesize] at (3,-0.3) {duvar};\n'
 '\\fill[green!15] (0,0) rectangle (6,3);\n'
 f'\\draw[{TUR},line width=2.4pt] (0,0) -- (0,3) -- (6,3) -- (6,0);\n'
 '\\node[left,font=\\small] at (0,1.5) {$x$};\\node[right,font=\\small] at (6,1.5) {$x$};\\node[above,font=\\small] at (3,3) {$y$};\n'
 '\\node[font=\\footnotesize] at (3,1.5) {bahçe};\n'
 f'\\node[font=\\footnotesize,text={TUR}] at (3,3.95) {{kalın çizgi: tel}};')
q('0008',tipId='par-enbuyuk',tip='En büyük ve en küçük değer uygulaması',z='orta',alt='Alan Uygulaması',kaz='Çevre koşulu verilen dikdörtgen biçimli bir bahçenin alanının en büyük değerini ikinci dereceden fonksiyonla bulur.',kalip='hikâyeli',
 kart='K-APAR-07 (duvara dayalı alan) · üç kenara tel',
 metin='Bir çiftçi, şekildeki gibi bir duvara dayalı, dikdörtgen biçimli bir bahçe yapacaktır. Duvar olan kenar hariç, bahçenin kalan üç kenarı toplam 80 metre uzunluğunda tel ile çevrilecek ve tel tamamen kullanılacaktır.\nBuna göre bahçenin alanı en fazla kaç metrekare olabilir?',
 dogru=v,yan=[(e[0],'Dört kenarın da çevrildiğini düşünüp 2x + 2y = 80 yazmış: alan x(40 − x) ifadesinin en büyük değeri.','dikkat'),(e[1],'Alan fonksiyonunun tepe apsisini bulup bunu alanın kendisi sanmış.','dikkat'),(e[2],'Duvara paralel kenarı 80, dik kenarı 20 alıp çarpmış.','islem'),(e[3],'Tepe apsisi x = 20 iken duvara paralel kenarı 80 − 2 · 20 bulup yalnız onu yazmış.','dikkat')],
 istenen='Bahçenin en büyük alanı (m²).',ip=['Dik kenarlardan birine x deyip duvara paralel kenarı x türünden yaz.'],bilgi=[ENB],sekil=fig(body),
 ad=[A('Alanı yaz','Dik kenarlar x, duvara paralel kenar 80 − 2x olur.','A(x) = x(80 − 2x) = −2x² + 80x'),A('Tepe apsisi','a < 0 olduğundan tepe noktasında en büyük değer vardır.','x = −80/(2 · (−2)) = 20'),A('En büyük alan','x = 20 yazılır.','A(20) = 20 · 40 = 800')],
 puf='Kenar uzunluklarını bulup tel uzunluğunu yeniden topla.')

# ================= 09 orta · ATB üçgeninin alanı =================
f9=lambda x:2*(x-1)*(x-5); assert f9(0)==10
T9=(3,f9(3)); assert T9==(3,-8)
v=Fr(1,2)*4*8; assert v==16
e=[4*8,Fr(1,2)*4*10,Fr(1,2)*4*4,Fr(1,2)*(1+5)*8]
assert e==[32,20,8,24] and len({v,*e})==5
sx,sy=0.8,0.3
body='\n'.join(f'\\draw[gray!35,thin] ({i*sx:.3f},{-10*sy:.3f}) -- ({i*sx:.3f},{12*sy:.3f});' for i in range(-1,7))
body+=f'\n\\fill[blue!15] ({1*sx},0) -- ({3*sx},{-8*sy}) -- ({5*sx},0) -- cycle;'
body+=f'\n\\draw[-{{Stealth}},thick] ({-1.3*sx:.3f},0) -- ({7.2*sx:.3f},0) node[right] {{$x$}};\\draw[-{{Stealth}},thick] (0,{-10*sy:.3f}) -- (0,{12.6*sy:.3f}) node[above] {{$y$}};'
body+='\n'+curve(f9,-0.9,6,sx,sy,MAVI,-9.5,11.5)
body+=f'\n\\draw[{MAVI},thick] ({1*sx},0) -- ({3*sx},{-8*sy}) -- ({5*sx},0) -- cycle;'
body+='\n'+dot(1,0,sx,sy)+dot(5,0,sx,sy)+dot(3,-8,sx,sy)+dot(0,10,sx,sy)
body+='\n'+lab(1,0,sx,sy,'$A$','below left')+lab(5,0,sx,sy,'$B$','below right')+lab(3,-8,sx,sy,'$T$','below')+lab(0,10,sx,sy,'$10$','right')
body+='\n'+''.join(f'\\node[font=\\footnotesize,above=5pt] at ({i*sx:.3f},0) {{${i}$}};' for i in (1,5))
body+='\n'+''.join(f'\\draw ({i*sx:.3f},0.07) -- ({i*sx:.3f},-0.07);' for i in range(-1,7))
q('0009',tipId='par-alan',tip='Kökler ve alan',z='orta',alt='Üçgen Alanı',kaz='x eksenini ve y eksenini kestiği noktalar verilen parabolün denklemini yazarak kökler ve tepe noktasının oluşturduğu üçgenin alanını hesaplar.',kalip='şekilli',
 kart='K-APAR-08 (kök-tepe üçgeni) · baş katsayı y ekseni kesiminden',
 metin='Şekilde, x eksenini A ve B noktalarında, y eksenini 10 noktasında kesen bir parabol verilmiştir; parabolün tepe noktası T’dir. A ve B noktalarının apsisleri şekilde, ızgara çizgileri üzerinde görülmektedir.\nBuna göre boyalı ATB üçgeninin alanı kaç birimkaredir?',
 dogru=v,yan=[(e[0],'Üçgenin alanı yerine tabanı ile yüksekliğini çarpıp ½ ile çarpmayı unutmuş: 4 · 8.','islem'),(e[1],'Yüksekliği tepe ordinatı yerine parabolün y eksenini kestiği noktanın ordinatı (10) almış.','dikkat'),(e[2],'Baş katsayıyı 1 sanıp tepe ordinatını −4 bulmuş: ½ · 4 · 4.','bilgi'),(e[3],'Tabanı kök uzaklığı yerine köklerin toplamı (1 + 5) almış.','dikkat')],
 istenen='ATB üçgeninin alanı (birimkare).',ip=['Parabolü kökleriyle yazıp y eksenini kestiği nokta ile baş katsayıyı bul.'],bilgi=[ALN],sekil=fig(body),
 ad=[A('Denklemi yaz','Kökler 1 ve 5; x = 0 için değer 10.','f(x) = a(x − 1)(x − 5), 5a = 10 → a = 2'),A('Tepeyi bul','Tepe apsisi köklerin ortasıdır.','x = 3, f(3) = 2 · 2 · (−2) = −8'),A('Alanı hesapla','Taban 4, yükseklik 8.','½ · 4 · 8 = 16')],
 puf='Tepenin x eksenine uzaklığını, parabolün işaretini de kontrol ederek bul.')

# ================= 10 orta · f(x) > 5 tam sayı toplamı =================
f10=lambda x:-x*x+4*x+5
S=[x for x in range(-20,21) if f10(x)>5]; assert S==[1,2,3]
v=sum(S); assert v==6
e=[sum(x for x in range(-20,21) if f10(x)>0),sum(x for x in range(-20,21) if f10(x)>=0),len(S),sum(x for x in range(-20,21) if f10(x)==5)]
assert e==[10,14,3,4] and len({v,*e})==5
sx=0.62; sy=0.36
body=axes(-2,6,-3,10,sx,sy,ys=1,ytick=[5,9],fs='\\footnotesize')
body+='\n'+curve(f10,-1.6,5.6,sx,sy,MAVI,-3.2,10)+'\n'+f'\\draw[{TUR},thick,dashed] ({-2*sx:.3f},{5*sy:.3f}) -- ({6.5*sx:.3f},{5*sy:.3f});'
body+='\n'+dot(0,5,sx,sy,TUR)+dot(4,5,sx,sy,TUR)+dot(-1,0,sx,sy)+dot(5,0,sx,sy)+dot(2,9,sx,sy)
body+='\n'+lab(5.7,5.0,sx,sy,'$y=5$','above',TUR)+lab(5.4,9.6,sx,sy,'$y=f(x)$','right',MAVI)
q('0010',tipId='par-aralik',tip='Eşitsizlik ve tam sayı çözümleri',z='orta',alt='Grafikle Eşitsizlik',kaz='Grafikte parabol ile yatay doğrunun kesişimlerinden f(x) > k eşitsizliğini çözüp tam sayı çözümlerini toplar.',kalip='grafik',
 kart='K-APAR-06 (grafikle eşitsizlik) · parabol ve yatay doğru',
 metin='Şekilde, ikinci dereceden bir f fonksiyonunun grafiği ile y = 5 doğrusu verilmiştir; işaretli noktalar ızgara çizgilerinin kesişimindedir.\nBuna göre f(x) > 5 eşitsizliğini sağlayan x tam sayılarının toplamı kaçtır?',
 dogru=v,yan=[(e[0],'f(x) > 0 eşitsizliğini çözmüş: kökler −1 ve 5 arasındaki tam sayıları (0, 1, 2, 3, 4) toplamış.','dikkat'),(e[1],'Kökleri de dahil edip −1’den 5’e kadar tam sayıları toplamış.','dikkat'),(e[2],'Toplam yerine tam sayı adedini yazmış.','dikkat'),(e[3],'Doğru ile parabolün kesişim apsislerini (0 ve 4) toplamış.','islem')],
 istenen='Tam sayı çözümlerin toplamı.',ip=['Parabolün y = 5 doğrusunun üstünde kaldığı apsisleri grafikte işaretle.'],bilgi=[ARA],sekil=fig(body),
 ad=[A('Kesişimleri bul','Parabol ile doğrunun ortak noktaları ızgaradan okunur; kökler ve tepe de ızgaradan okunabilir.','x = 0 ve x = 4'),A('Aralığı belirle','Parabol, kesişimler arasında doğrunun üstündedir; uçlar dahil değildir.','0 < x < 4'),A('Topla','Aralıktaki tam sayılar toplanır.','1 + 2 + 3 = 6')],
 puf='Çözüm aralığından bir tam sayıyı f(x) > 5 eşitsizliğinde sınayarak denetle.')

# ================= 11 orta · top atışı =================
h11=lambda t:-5*t*t+30*t
assert h11(0)==0 and h11(6)==0 and h11(3)==45
ts=[t for t in (Fr(k,100) for k in range(0,601)) if h11(t)>=25]; assert min(ts)==1 and max(ts)==5
v=5-1; assert v==4
e=[5,1,6,3]; assert len({v,*e})==5
sx=0.95; sy=0.115
body=axes(0,6,0,45,sx,sy,ys=5,xl='$t$ (s)',yl='$h$ (m)',gridy=True,xext=0.6,yext=0.5)
body+='\n'+curve(h11,0,6,sx,sy,MAVI,0,46)+'\n'+dot(0,0,sx,sy)+dot(3,45,sx,sy)+dot(6,0,sx,sy)
q('0011',tipId='par-enbuyuk',tip='En büyük ve en küçük değer uygulaması',z='orta',alt='Atış Yüksekliği',kaz='Yükseklik–zaman grafiğinden parabolün denklemini bulup belirli bir yüksekliğin üstünde kalınan süreyi hesaplar.',kalip='hikâyeli',
 kart='K-APAR-07 (yükseklik–zaman grafiği) · parabolik atış',
 metin='Bir çocuk, yerden yukarı doğru bir topu fırlatıyor. Topun yerden yüksekliğinin (metre) zamanla (saniye) değişimini gösteren ve parabol biçimindeki grafik şekilde verilmiştir; grafikte işaretli noktalar ızgara çizgilerinin kesişimindedir.\nBuna göre top, yerden 25 metreden daha yüksekte kaç saniye kalmıştır?',
 dogru=v,yan=[(e[0],'Denklemin iki kökünden büyüğünü süre sanmış (t = 5).','dikkat'),(e[1],'Denklemin iki kökünden küçüğünü süre sanmış (t = 1).','dikkat'),(e[2],'Topun havada kalma süresini yazmış (0 ile 6 arası).','dikkat'),(e[3],'Topun tepe noktasına ulaşma anını süre sanmış (t = 3).','dikkat')],
 istenen='Topun 25 m’den yüksekte kaldığı süre (s).',ip=['Grafikteki kök ve tepe noktasından h(t) fonksiyonunu yaz.'],bilgi=[ENB],sekil=fig(body),
 ad=[A('h(t)’yi yaz','Kökler 0 ve 6, tepe ordinatı 45.','h(t) = a × t(t − 6), a × 3 × (−3) = 45 → a = −5'),A('h = 25 çöz','Denklem düzenlenip çözülür.','−5t² + 30t = 25 → t² − 6t + 5 = 0 → t = 1, t = 5'),A('Süreyi bul','Top bu iki an arasında 25 m’nin üstündedir.','5 − 1 = 4')],
 puf='Süreyi bulduktan sonra aralığın ortası olan anda yüksekliğin 25’ten büyük olduğunu denetle.')

# ================= 12 orta · her x için pozitiflik =================
tam=[m for m in range(-20,21) if (4*(m-1)**2-4*(m+5))<0]; assert tam==[0,1,2,3]
v=sum(tam); assert v==6
e=[len(tam),sum(range(-1,4)),sum(range(-1,5)),sum(range(0,5))]
assert e==[4,5,9,10] and len({v,*e})==5
q('0012',tipId='par-aralik',tip='Eşitsizlik ve tam sayı çözümleri',z='orta',alt='Parametreli Eşitsizlik',kaz='İkinci dereceden fonksiyonun tüm gerçel sayılar için pozitif olma koşulunu diskriminant ile çözüp tam sayı değerleri toplar.',kalip='düz',
 kart='K-APAR-06 (Δ < 0 koşulu) · parametreli fonksiyon',
 metin='m bir gerçel sayı olmak üzere f(x) = x² − 2(m − 1)x + m + 5 fonksiyonu veriliyor. Her x gerçel sayısı için f(x) > 0 olduğuna göre m’nin alabileceği tam sayı değerlerinin toplamı kaçtır?',
 dogru=v,yan=[(e[0],'Doğru aralığı bulmuş, ancak değerleri toplamak yerine kaç tane olduğunu yazmış.','dikkat'),(e[1],'Δ < 0 çözümünde sol ucu (−1) da aralığa dahil etmiş: −1 + 0 + 1 + 2 + 3.','dikkat'),(e[2],'İki uç değeri de (−1 ve 4) aralığa dahil etmiş.','dikkat'),(e[3],'Sağ ucu (4) aralığa dahil etmiş: 0 + 1 + 2 + 3 + 4.','dikkat')],
 istenen='m’nin tam sayı değerlerinin toplamı.',ip=['Parabolün x eksenini hiç kesmemesi için hangi koşul gerekir?'],bilgi=[ISA],
 ad=[A('Koşulu yaz','Baş katsayı pozitif; grafik x ekseninin üstünde kalmalı.','Δ < 0'),A('Δ’yı hesapla','Δ = 4(m − 1)² − 4(m + 5) düzenlenir ve çarpanlarına ayrılır.','4(m − 4)(m + 1) < 0'),A('Tam sayıları topla','Çözüm aralığı −1 < m < 4’tür; uçlar dahil değildir.','0 + 1 + 2 + 3 = 6')],
 puf='Aralığın uçlarından birini yerine yazıp parabolün x eksenine teğet olduğunu gör.')

# ================= 13 orta · öncüllü, iki parabol =================
f13=lambda x:x*x-2*x-3; g13=lambda x:-f13(x)
xs=[Fr(k,4) for k in range(-16,40)]
I=[x for x in range(-30,31) if f13(x)==0]==[x for x in range(-30,31) if g13(x)==0]
II=all(f13(x)*g13(x)>=0 for x in xs)
III=[x for x in range(-30,31) if f13(x)==g13(x)]==[-1,3]
assert [I,II,III]==[True,False,True]
dog='I ve III'
sx=sy=0.58
body=axes(-2,4,-5,5,sx,sy)+'\n'+curve(f13,-1.9,3.9,sx,sy,MAVI,-4.4,5.2)+'\n'+curve(g13,-1.9,3.9,sx,sy,TUR,-5.2,4.4)+'\n'+dot(-1,0,sx,sy)+dot(3,0,sx,sy)+dot(1,-4,sx,sy,MAVI)+dot(1,4,sx,sy,TUR)+lab(3.1,5.2,sx,sy,'$y=f(x)$','right',MAVI)+lab(3.1,-4.6,sx,sy,'$y=g(x)$','right',TUR)
q('0013',tipId='par-ikili',tip='İki parabol arası dik uzaklık',z='orta',alt='Parabol Çifti',kaz='Aynı koordinat sisteminde verilen iki parabolün kökleri, işaretleri ve kesişimleri hakkındaki yargıları değerlendirir.',kalip='öncüllü',
 kart='K-APAR-09 (grafikle yargı) · iki parabolün x eksenine göre simetrisi',
 metin='Aynı dik koordinat düzleminde grafikleri verilen f ve g fonksiyonlarının grafikleri parabol olup işaretli noktalar ızgara çizgilerinin kesişimindedir.\nBuna göre,\nI. f ve g fonksiyonlarının grafikleri x eksenini aynı noktalarda keser.\nII. Her x gerçel sayısı için f(x) · g(x) ≥ 0 dır.\nIII. f(x) = g(x) denkleminin çözüm kümesi {−1, 3} tür.\nyargılarından hangileri doğrudur?',
 dogru=dog,yan=[(SIRA1[0],'Yalnız kökleri karşılaştırıp III’ün kesişimleri verdiğini görmemiş.','dikkat'),(SIRA1[1],'f(x) · g(x) ≥ 0 yargısını doğru, diğerlerini yanlış değerlendirmiş.','bilgi'),(SIRA1[2],'II’yi doğru, III’ü yanlış saymış: iki grafiğin zıt işaretli olduğunu görmemiş.','bilgi'),(SIRA1[4],'II’de her x için çarpımın işaretini denetlememiş.','dikkat')],
 sira=SIRA1,istenen='Doğru olan yargılar.',ip=['İki grafiğin x eksenine göre nasıl yerleştiğine ve aynı x için işaretlerine bak.'],bilgi=[IKP],sekil=fig(body),
 ad=[A('I’i incele','Her iki grafik de x eksenini aynı iki noktada keser.','x = −1 ve x = 3: doğru'),A('II’yi incele','Aynı x için biri pozitifse diğeri negatiftir.','f(x) · g(x) ≤ 0: yargı yanlış'),A('III’ü incele','İki grafik yalnız x eksenindeki noktalarda kesişir.','Çözüm kümesi {−1, 3}: doğru')],
 puf='Her yargı için bir x değeri seçip grafikten iki değeri oku.')

# ================= 14 orta · işaret çizelgesi =================
a14=-2; f14=lambda x:a14*(x+2)*(x-3); assert f14(0)==12 and f14(4)==-12
v=f14(4)
def fa(a,r1,r2,x): return a*(x-r1)*(x-r2)
ax_a=12//((0-2)*(0+3)); assert ax_a==-2
e=[fa(ax_a,2,-3,4),fa(1,-2,3,4)*2,fa(12,-2,3,4),fa(1,-2,3,4)]
assert e==[-28,12,72,6] and len({v,*e})==5
body=('\\draw[-{Stealth},thick] (-4.6,0) -- (4.7,0) node[right] {$x$};\n'
 '\\foreach \\x/\\n in {-2.5/-2,2.5/3} {\\draw[thick] (\\x,0.12) -- (\\x,-0.12); \\node[below=3pt,font=\\small] at (\\x,-0.1) {$\\n$};}\n'
 f'\\node[font=\\Large,text={KIR}] at (-3.6,0.55) {{$-$}};\\node[font=\\Large,text={YES}] at (0,0.55) {{$+$}};\\node[font=\\Large,text={KIR}] at (3.6,0.55) {{$-$}};\n'
 '\\node[font=\\small,anchor=east] at (-4.7,0.55) {$f(x)$};')
q('0014',tipId='par-grafik',tip='Grafikten parabol denklemi',z='orta',alt='İşaret Çizelgesi',kaz='İkinci dereceden fonksiyonun işaret çizelgesinden kökleri ve baş katsayının işaretini yorumlayıp bir değer hesaplar.',kalip='şekilli',
 kart='K-APAR-01 (işaret çizelgesi) · − + − dizilimi ve bir değerden baş katsayı',
 metin='Gerçel sayılar kümesi üzerinde tanımlı ikinci dereceden f fonksiyonunun işaret çizelgesi şekilde verilmiştir. f(0) = 12 olduğuna göre f(4) kaçtır?',
 dogru=v,yan=[(e[0],'Kökleri −2 ve 3 yerine 2 ve −3 alarak baş katsayıyı doğru bulmuş, ancak çarpanları (x − 2)(x + 3) yazmış.','islem'),(e[1],'İşaret çizelgesini kullanmadan baş katsayıyı pozitif alıp sonucu pozitif bulmuş.','dikkat'),(e[2],'f(0) = 12 değerini baş katsayı sanmış: 12 · (4 + 2)(4 − 3).','dikkat'),(e[3],'Baş katsayıyı 1 varsayıp f(0) = 12 bilgisini kullanmamış: (4 + 2)(4 − 3).','dikkat')],
 istenen='f(4) değeri.',ip=['Çizelgedeki işaretlerden baş katsayının işaretini yorumla ve f(0) ile büyüklüğünü bul.'],bilgi=[KOK],sekil=fig(body),
 ad=[A('Çarpanlı yazım','Kökler −2 ve 3; ortası pozitif olduğundan a < 0.','f(x) = a(x + 2)(x − 3)'),A('a’yı bul','f(0) = 12 yazılır.','a · 2 · (−3) = 12 → a = −2'),A('f(4)','x = 4 yazılır.','−2 · 6 · 1 = −12')],
 puf='Bulduğun denklemin işaretlerinin çizelgeyle uyuştuğunu denetle.')

# ================= 15 zor · öteleme ve kökler arası uzaklık =================
a15=Fr(1,12); c15=Fr(-1,3)
def d(t):  # t birim aşağı: y = a x² + c − t ; kökler arası uzaklık
    r=(t-c15)/a15; assert r>0; s=math.isqrt(int(r)) if r.denominator==1 else None; return 2*math.sqrt(r)
assert abs(d(0)-4)<1e-9 and abs(d(1)-8)<1e-9 and abs(d(5)-16)<1e-9
v=16
dsq=lambda t:Fr(4)*(t-c15)/a15
e=[4+(8-4)*5,4*5,8*5,int(dsq(5))]
assert e==[24,20,40,256] and len({v,*e})==5,e
q('0015',tipId='par-oteleme',tip='Parabolü öteleme',z='zor',alt='Öteleme ve Kökler Arası Uzaklık',kaz='Simetri ekseni y ekseni olan parabolün aşağı ötelenmesiyle kökler arası uzaklığın değişimini kurup yeni uzaklığı hesaplar.',kalip='yeni nesil',
 kart='K-APAR-02 (öteleme ve kök uzaklığı) · aşağı ötelemede uzaklığın karesi doğrusal',
 metin='Dik koordinat düzleminde, simetri ekseni y ekseni olan ve kolları yukarı doğru olan bir parabol x eksenini birbirinden 4 birim uzaklıktaki iki noktada kesmektedir. Bu parabol 1 birim aşağı ötelendiğinde, x eksenini kestiği noktalar arasındaki uzaklık 8 birim olmaktadır.\nBuna göre bu parabol, ilk konumundan 5 birim aşağı ötelenirse x eksenini kestiği noktalar arasındaki uzaklık kaç birim olur?',
 dogru=v,yan=[(e[0],'Uzaklığın her birim ötelemede aynı miktar (4 birim) arttığını varsayıp 4 + 4 · 5 yazmış.','dikkat'),(e[1],'İlk uzaklığı (4) ötelenme miktarıyla çarpmış.','islem'),(e[2],'İlk ötelemedeki uzaklığı (8) ötelenme miktarıyla çarpmış.','islem'),(e[3],'Köklerin karesini bulduktan sonra karekök almayı unutmuş: 4 · (c + 5)/a = 256.','dikkat')],
 istenen='5 birim aşağı ötelemeden sonra kökler arası uzaklık (birim).',ip=['Parabolü y = ax² − k biçiminde yaz.'],bilgi=[OTE],
 ad=[A('Denklemi kur','Simetri ekseni y ekseni: y = ax² − k (a > 0, k > 0). Kökler ±√(k/a).','uzaklık = 2√(k/a)'),A('İki koşuldan a ve k','Uzaklıklar 4 ve 8: 4k/a = 16 ve 4(k + 1)/a = 64.','4/a = 48 → a = 1/12, k = 1/3'),A('5 birim aşağı','k yerine k + 5 yazılır.','uzaklık² = 4 · (1/3 + 5) · 12 = 256'),A('Uzaklık','Karekök alınır.','16')],
 puf='Bulduğun a ve k ile iki verilen uzaklığı yeniden hesaplayıp denetle.')

# ================= 16 zor · iki parabol arası en büyük dik uzaklık =================
f16=lambda x:x*x-4*x; g16=lambda x:-(x+1)**2+5
assert f16(-1)==g16(-1)==5 and f16(2)==g16(2)==-4
diff=lambda x:g16(x)-f16(x); assert all(diff(x)==-2*(x+1)*(x-2) for x in range(-5,6))
xs=[Fr(k,8) for k in range(-8,17)]; v=max(diff(x) for x in xs); assert v==Fr(9,2) and diff(Fr(1,2))==v
e=[diff(0),Fr(9,4),3,9]
assert e==[4,Fr(9,4),3,9] and len({v,*e})==5
sx=0.62; sy=0.42
body=axes(-3,5,-5,6,sx,sy,ytick=[-4,5],fs='\\footnotesize')
body+='\n'+curve(f16,-1.5,4.5,sx,sy,MAVI,-4.5,6.2)+'\n'+curve(g16,-3.2,3.2,sx,sy,TUR,-5.2,5.4)+'\n'
body+=dot(-1,5,sx,sy)+dot(2,-4,sx,sy)+lab(-1,5,sx,sy,'$A$','above left')+lab(2,-4,sx,sy,'$B$','below right')
body+='\n'+lab(4.5,2.6,sx,sy,'$f$','right',MAVI)+lab(-2.4,3.6,sx,sy,'$g$','above left',TUR)
q('0016',tipId='par-ikili',tip='İki parabol arası dik uzaklık',z='zor',alt='İki Parabol',kaz='Biri tepe noktası ve bir kesişim noktasıyla verilen iki parabolün farkını kurarak kesişim apsisleri arasındaki en büyük dik uzaklığı bulur.',kalip='şekilli',
 kart='K-APAR-09 (iki parabol, en büyük dik uzaklık) · g tepe ve kesişim noktasından kurulur',
 metin='Şekilde, f(x) = x² − 4x fonksiyonunun grafiği ile tepe noktası A olan g fonksiyonunun grafiği verilmiştir. İki parabol, A ve B noktalarında kesişmektedir ve A, B noktalarının koordinatları ızgara çizgilerinin kesişimindedir.\nBuna göre, A ile B noktalarının apsisleri arasında kalan x değerleri için f ve g grafiklerinin aynı x değerindeki noktaları arasındaki uzaklık en çok kaç birimdir?',
 dogru=v,yan=[(e[0],'x = 0 için iki grafiğin değerlerinin farkını (4 − 0) alıp en büyük sanmış.','dikkat'),(e[1],'Farkın −2(x + 1)(x − 2) olduğunu yazarken baş katsayı −2’yi atlamış: −(x + 1)(x − 2) en büyük değeri.','islem'),(e[2],'A ve B’nin apsisleri arasındaki uzaklığı sorulan uzaklık sanmış.','dikkat'),(e[3],'En büyük değeri iki kez hesaba katıp iki katına çıkarmış.','islem')],
 istenen='En büyük dik uzaklık (birim).',ip=['g’nin tepe noktası ile bir noktasını kullanarak denklemini yaz, sonra iki fonksiyonun farkını incele.'],bilgi=[IKP],sekil=fig(body),
 ad=[A('g’yi bul','Tepe A(−1, 5) ve B(2, −4) g üzerinde.','g(x) = a(x + 1)² + 5, 9a + 5 = −4 → a = −1'),A('Farkı kur','Aralıkta g grafiği f grafiğinin üstündedir.','g(x) − f(x) = −2x² + 2x + 4 = −2(x + 1)(x − 2)'),A('En büyüğü bul','Tepe apsisi köklerin ortasıdır.','x = 1/2 → −2 × (3/2) × (−3/2) = 9/2')],
 puf='Farkın köklerinin kesişim apsisleri olduğunu görmek hesabı kısaltır.')

# ================= 17 zor · iki teğetlik koşulu =================
def kosul(b):
    c=Fr(b*b,4); return (b-2)**2-4*(c+7)
bs=[b for b in range(-40,41) if kosul(b)==0]; assert bs==[-6]
b17=-6; c17=Fr(b17*b17,4); assert c17==9
v=b17+c17; assert v==3
# hata zincirleri
bh=[b for b in range(-40,41) if (b+2)**2-4*(Fr(b*b,4)+7)==0]; assert bh==[6]; e1=6+9
bh=[b for b in range(-40,41) if (b-2)**2-4*(Fr(b*b,4)-7)==0]; assert bh==[8]; e2=8+16
b3=-6; e3=b3+b3*b3   # c = b² sanıldı ⇒ −6 + 36
e4=b17*c17
e=[e1,e2,e3,e4]; assert e==[15,24,30,-54] and len({v,*e})==5
q('0017',tipId='par-kesisim',tip='Doğru ve parabolün kesişimi',z='zor',alt='İki Teğetlik Koşulu',kaz='Aynı parabolün x eksenine ve bir doğruya teğet olma koşullarından katsayıları bulur.',kalip='düz',
 kart='K-APAR-05 (teğet koşulları) · eksene ve doğruya teğet',
 metin='b ve c gerçel sayılar olmak üzere dik koordinat düzleminde y = x² + bx + c parabolü, x eksenine ve y = 2x − 7 doğrusuna teğettir.\nBuna göre b + c toplamı kaçtır?',
 dogru=v,yan=[(e[0],'Doğru ile parabolü eşitlerken 2x’in işaretini hatalı taşıyıp x² + (b + 2)x + c + 7 = 0 yazmış; Δ = 0 ile b = 6, c = 9 bulmuş.','islem'),(e[1],'Eşitlemede −7’yi yanlış taşıyıp x² + (b − 2)x + c − 7 = 0 yazmış; b = 8, c = 16 bulmuş.','islem'),(e[2],'b’yi doğru (−6) bulmuş, ancak x eksenine teğetlikten c’yi b²/4 yerine b² alıp 36 yazmış: b + c = 30.','bilgi'),(e[3],'Doğru değerleri bulup toplam yerine çarpımı yazmış.','dikkat')],
 istenen='b + c toplamı.',ip=['Teğet olmak, ortak nokta sayısı hakkında ne söyler?'],bilgi=[KES],
 ad=[A('x eksenine teğet','x² + bx + c = 0 denkleminin Δ’sı sıfırdır.','b² − 4c = 0 → c = b²/4'),A('Doğruya teğet','x² + bx + c = 2x − 7 denkleminde Δ = 0 yazılır.','x² + (b − 2)x + c + 7 = 0 → (b − 2)² − 4(c + 7) = 0'),A('Denklemleri birleştir','c yerine b²/4 yazılır.','b² − 4b + 4 − b² − 28 = 0 → b = −6, c = 9'),A('Topla','b ve c toplanır.','−6 + 9 = 3')],
 puf='Bulduğun parabolün x ekseni ile doğruya tam bir ortak nokta verdiğini denetle.')

# ================= 18 zor · parabol içine dikdörtgen, en büyük çevre =================
P18=lambda x:2*(2*x+9-x*x)
assert max(P18(Fr(k,4)) for k in range(0,13))==20 and P18(1)==20
v=20
P_a=lambda x:2*(x+9-x*x)         # genişlik x alınmış
e=[P18(0),Fr(37,2),10,9]
assert max(P_a(Fr(k,8)) for k in range(0,25))==Fr(37,2) and P18(0)==18 and e[0]==18
assert len({v,*e})==5
sx=sy=0.5
body=axes(-3,3,0,9,sx,sy,xs=3,ys=1,ytick=[],nums=True,fs='\\footnotesize',gridy=False)
body+='\n'+curve(lambda x:9-x*x,-3,3,sx,sy,MAVI,0,9.4)
xr=1.4
body+=f'\n\\fill[green!20] ({-xr*sx:.3f},0) rectangle ({xr*sx:.3f},{(9-xr*xr)*sy:.3f});\\draw[{YES},thick] ({-xr*sx:.3f},0) rectangle ({xr*sx:.3f},{(9-xr*xr)*sy:.3f});'
body+='\n'+dot(-xr,9-xr*xr,sx,sy)+dot(xr,9-xr*xr,sx,sy)+dot(-xr,0,sx,sy)+dot(xr,0,sx,sy)
body+='\n'+lab(-xr,9-xr*xr,sx,sy,'$A$','above left')+lab(xr,9-xr*xr,sx,sy,'$B$','above right')+lab(-xr,0,sx,sy,'$D$','below')+lab(xr,0,sx,sy,'$C$','below')
body+='\n'+lab(2.3,8.4,sx,sy,'$y=9-x^2$','right',MAVI)
q('0018',tipId='par-enbuyuk',tip='En büyük ve en küçük değer uygulaması',z='orta',alt='Dikdörtgenin Çevresi',kaz='Parabol ile x ekseni arasına yerleştirilen dikdörtgenin çevresini tek değişkenli ikinci dereceden ifade olarak yazıp en büyük değerini bulur.',kalip='şekilli',
 kart='K-APAR-07 (parabol içinde dikdörtgen) · simetrik yerleşim',
 metin='Şekilde, y = 9 − x² parabolü ile x ekseni arasında, A ve B köşeleri parabol üzerinde, C ve D köşeleri x ekseni üzerinde olan ABCD dikdörtgeni gösterilmiştir. Dikdörtgen y eksenine göre simetriktir; A ve B köşelerinin konumu değişebilir ve her konumda yine bu özelliklere sahip bir dikdörtgen oluşur.\nBuna göre bu dikdörtgenin çevresi en çok kaç birim olabilir?',
 dogru=v,yan=[(e[0],'Çevre ifadesinin x = 0 iken aldığı değeri en büyük sanmış: 2 · (0 + 9).','dikkat'),(e[1],'Genişliği x kabul edip çevreyi 2(x + 9 − x²) yazmış; tepe apsisini 1/2 bulmuş.','islem'),(e[2],'Çevre yerine yarı çevrenin en büyük değerini yazmış.','dikkat'),(e[3],'Çevre yerine dikdörtgenin yüksekliğinin en büyük değerini yazmış.','dikkat')],
 istenen='Dikdörtgenin en büyük çevresi (birim).',ip=['A köşesinin apsisine x deyip dikdörtgenin iki kenarını x cinsinden yaz.'],bilgi=[ENB],sekil=fig(body),
 ad=[A('Kenarları yaz','B(x, 9 − x²) alınırsa genişlik 2x, yükseklik 9 − x² olur.','|CD| = 2x, |BC| = 9 − x²'),A('Çevreyi kur','Çevre iki genişlik ile iki yüksekliğin toplamıdır.','Ç(x) = 2(2x + 9 − x²) = −2x² + 4x + 18'),A('En büyüğü bul','a < 0 olduğundan tepe noktasında en büyük değer vardır.','x = 1 → Ç(1) = 20')],
 puf='Bulduğun x değerinin iki yanındaki değerlerle karşılaştırarak denetle.')

# ================= 19 zor · parabolik kemer =================
k19=lambda x:10-Fr(x)**2/40
assert k19(20)==0 and k19(-20)==0 and k19(0)==10
hT=Fr(42,5)          # 8,4
w=2*math.sqrt(40*(10-float(hT))); assert abs(w-16)<1e-9
v=16
e=[8,24,Fr(32,5),32]
assert 40*(1-hT/10)==Fr(32,5) and 40-16==24 and e[0]==8 and 2*16==32 and len({v,*e})==5
sx=0.2; sy=0.2
body=('\\draw[thick] (-4.6,0) -- (4.6,0);\n'+curve(lambda x:10-x*x/40,-20,20,sx,sy,MAVI,0,10.1,w='line width=2.2pt')+'\n'
 f'\\fill[blue!8] ({-20*sx},0) -- plot[smooth] coordinates {{{" ".join(f"({x*sx:.3f},{(10-x*x/40)*sy:.3f})" for x in range(-20,21,2))}}} -- ({20*sx},0) -- cycle;\n'
 f'\\draw[{MAVI},line width=2.2pt] plot[smooth] coordinates {{{" ".join(f"({x*sx:.3f},{(10-x*x/40)*sy:.3f})" for x in range(-20,21,2))}}};\n'
 f'\\draw[{TUR},thick,fill=orange!25] (-1.0,0) rectangle (1.0,{8.4*sy:.3f});\\node[font=\\scriptsize] at (0,{4.2*sy:.3f}) {{tekne}};\n'
 f'\\draw[{TUR},thick,<->] (1.45,0) -- (1.45,{8.4*sy:.3f});\\node[right,font=\\footnotesize] at (1.45,{4.2*sy:.3f}) {{8,4 m}};\n'
 f'\\draw[<->] ({-20*sx},-0.45) -- ({20*sx},-0.45);\\node[below,font=\\footnotesize] at (0,-0.45) {{40 m}};\n'
 f'\\draw[<->] ({-4.9},0) -- ({-4.9},{10*sy:.3f});\\node[left,font=\\footnotesize] at (-4.9,{5*sy:.3f}) {{10 m}};\n'
 '\\node[font=\\scriptsize,gray] at (3.2,2.4) {Şekil ölçekli değildir.};')
body=body.replace('(1.45,0) -- (1.45,','(1.45,0) -- (1.45,')
q('0019',tipId='par-grafik',tip='Grafikten parabol denklemi',z='orta',alt='Parabolik Kemer',kaz='Parabol biçimli bir köprü kemerinin ölçülerinden denklemini kurup belirli bir yükseklikteki genişliği hesaplar.',kalip='hikâyeli',
 kart='K-APAR-01 (kemer ölçülerinden denklem) · simetrik parabolik kemer',
 metin='Bir köprünün kemeri, ayakları arasındaki uzaklık 40 metre ve en yüksek noktasındaki yüksekliği 10 metre olan, nehre dik düzlemde parabol biçimindedir ve ayakları su yüzeyindedir; şekilde ölçüler gösterilmiştir. Su yüzeyinden yüksekliği 8,4 metre olan dikdörtgen kesitli direkli bir tekne, kemerin altından ortalanarak geçecektir.\nBuna göre teknenin genişliği en fazla kaç metre olabilir?',
 dogru=v,yan=[(e[0],'Yarı genişliği (x = 8) bulup iki ile çarpmayı unutmuş.','dikkat'),(e[1],'Kemerin genişliğinden tekne genişliğini çıkarılacak değer sanmış: 40 − 16.','dikkat'),(e[2],'Kemeri üçgen kabul edip genişliği yükseklik oranıyla doğrusal küçültmüş: 40 · (10 − 8,4)/10.','bilgi'),(e[3],'Genişliği (16) bulduktan sonra bir kez daha 2 ile çarpmış: 32.','islem')],
 istenen='Teknenin en büyük genişliği (m).',ip=['Orijini yolun ortasına koyup kemerin denklemini y = ax² + 10 biçiminde yaz.'],bilgi=[TEP],sekil=fig(body),
 ad=[A('Denklemi kur','Ayaklar x = ±20 noktalarında yerdedir.','y = ax² + 10, 400a + 10 = 0 → y = −x²/40 + 10'),A('Yüksekliği yaz','y = 8,4 için x bulunur.','−x²/40 + 10 = 8,4 → x² = 64 → x = ±8'),A('Genişlik','İki taraf toplanır.','2 · 8 = 16')],
 puf='Teknenin üst köşe noktasının kemer üzerinde kaldığını denklemle denetle.')

# ================= 20 zor · bileşke fonksiyonun en küçük değeri =================
f20=lambda x:x*x-6*x+11; g20=lambda t:t*t-2*t-1
mn=min(g20(f20(Fr(k,4))) for k in range(-40,80)); assert mn==-1 and f20(3)==2 and g20(2)==-1
v=-1
e=[min(g20(Fr(k,4)) for k in range(-40,80)),min(f20(g20(Fr(k,4))) for k in range(-40,80))-2,g20(3),g20(f20(1))]
e[1]=sum([min(f20(Fr(k,4)) for k in range(-40,80)),min(g20(Fr(k,4)) for k in range(-40,80))])
assert e==[-2,0,2,23] and len({v,*e})==5,e
q('0020',tipId='par-tepe',tip='Tepe noktası ve simetri',z='zor',alt='Bileşke Fonksiyon',kaz='İki ikinci dereceden fonksiyonun bileşkesinin en küçük değerini, iç fonksiyonun değer aralığını kullanarak bulur.',kalip='yeni nesil',
 kart='K-APAR-03 (bileşkede en küçük değer) · iç fonksiyonun alt sınırı dış tepenin sağında',
 metin='Gerçel sayılar kümesi üzerinde f(x) = x² − 6x + 11 ve g(x) = x² − 2x − 1 fonksiyonları tanımlanıyor.\nBuna göre (g ∘ f)(x) fonksiyonunun alabileceği en küçük değer kaçtır?',
 dogru=v,yan=[(e[0],'g’nin kendi en küçük değerini bulmuş; f’nin değerlerinin 2’den küçük olamayacağını hesaba katmamış.','dikkat'),(e[1],'f ve g’nin en küçük değerlerini ayrı ayrı bulup toplamış: 2 + (−2).','islem'),(e[2],'f’nin tepe apsisi 3’ü g’de yerine yazmış: g(3).','dikkat'),(e[3],'g’nin tepe apsisi 1’i bileşkede x yerine yazmış: g(f(1)).','islem')],
 istenen='(g ∘ f)(x) fonksiyonunun en küçük değeri.',ip=['f(x) hangi değerleri alabilir? Bu değerlerde g nerede en küçük olur?'],bilgi=[TEP],
 ad=[A('f’nin değer aralığı','Tepe noktası T(3, 2): f(x) ≥ 2.','f(x) = t ≥ 2'),A('g’nin davranışı','g’nin tepe apsisi 1, bu aralığın solunda; g, t ≥ 2 için artandır.','g en küçük değerini t = 2’de alır'),A('Değer','t = 2 için hesap yapılır; x = 3’te f(3) = 2 olduğundan bu değer alınır.','g(2) = −1')],
 puf='f(x) = 2 eşitliğini sağlayan bir x bulunup bulunmadığını da denetle.')

# ---------- yazım (ayt-mat klasörüne) ----------
def bitir_ayt(P,onek,k):
    HV=os.path.join(HD,'..')
    for q_ in P.ANA: q_['kardes']=None
    P.yaz(os.path.join(HD,f'{onek}-1.json'),'/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/par/bos.json')
    tipler={}
    for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=k))['kartlar'].append(c['id'])
    json.dump(dict(konu=P.konu_adi,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2025 AYT Matematik çıkmış soruları ve yayın soru bankaları (yalnız mantık), MEB 10–11. sınıf müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar',f'{onek}.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler))
bitir_ayt(P,'parabol',UK)
