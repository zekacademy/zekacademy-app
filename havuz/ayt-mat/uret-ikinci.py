"""AYT Matematik · 2.Dereceden Denklemler (20 soru: 4 kolay / 10 orta / 6 zor; 10 şekilli). Her doğru ve çeldirici değer kodla hesaplanıp assert edilir."""
import sys,os
HD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(HD,'..')
sys.path.insert(0,os.path.join(HV,'tyt-mat')); sys.path.insert(0,HV)
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
import sympy as sp, json
from math import sqrt
HD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(HD,'..')
H.KONU='2.Dereceden Denklemler'
UK='amat|2.Dereceden Denklemler'
P=Parti('ikinci','2.Dereceden Denklemler',UK,ders='AYT Matematik',idon='aytmat')
KY='ÖSYM 2018–2026 AYT Matematik (2.dereceden denklem soruları; yalnız mantık) · Bilgi Sarmal ve Acil yayınları (yalnız mantık) · MEB 10–11. sınıf'
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)
def fig(body,font='\\small'): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font='+font+']\n'+body+'\n\\end{tikzpicture}')
x=sp.symbols('x')
BL='blue!70!black'; OR='orange!85!black'; PU='violet!80!black'
def eqs(s,p):
    """x² − s·x + p = 0 biçiminde yazım (kökler toplamı s, çarpımı p)."""
    t=f'x² {"−" if s>0 else "+"} {"" if abs(s)==1 else abs(s)}x' if s!=0 else 'x²'
    return t+(f' + {p}' if p>0 else f' − {-p}')+' = 0'

# ---------------- bilgi kutuları (örnekler soruların sayılarından farklı) ----------------
VIE=B('Kökler toplamı ve çarpımı','ax² + bx + c = 0 (a ≠ 0) denkleminin kökleri x₁, x₂ ise x₁ + x₂ = −b/a ve x₁ · x₂ = c/a. Örnek: x² − 7x + 12 = 0 için toplam 7, çarpım 12')
DIS=B('Diskriminant','Δ = b² − 4ac. Δ > 0 ise iki farklı reel kök, Δ = 0 ise çakışık (eşit) iki reel kök, Δ < 0 ise reel kök yoktur. Örnek: x² − 4x + 4 = 0 için Δ = 16 − 16 = 0 ve kök x = 2')
KUR=B('Kökleri verilen denklem','kökleri x₁ ve x₂ olan ikinci dereceden denklemlerden biri x² − (x₁ + x₂)x + x₁ · x₂ = 0’dır. Örnek: kökleri 2 ve 5 olan denklem x² − 7x + 10 = 0’dır')
ORT=B('Ortak kök','iki denklemin ortak kökü r ise r her iki denklemi de sağlar. Denklemler birbirinden çıkarılınca r’yi de sağlayan daha sade bir denklem elde edilir. Örnek: x² + x − 6 = 0 ve x² − 9 = 0 için ortak kök 3’tür, çünkü 9 + 3 − 6 = 0 ve 9 − 9 = 0')
PAR=B('Parabol ve kökler','y = f(x) parabolünün x eksenini kestiği noktaların apsisleri f(x) = 0 denkleminin köklerinin değeridir; parabol x eksenine teğet ise denklemin çakışık iki kökü vardır. Örnek: parabol x eksenini 1 ve 5 noktalarında kesiyorsa f(x) = 0 denkleminin kökleri 1 ve 5’tir')
KES=B('Parabol ve doğrunun kesişimi','y = f(x) ile y = g(x) grafiklerinin kesişim noktalarının apsisleri f(x) = g(x) denkleminin kökleridir. Örnek: f(x) = x² ve g(x) = 2x + 3 için x² − 2x − 3 = 0 denkleminin kökleri kesişim apsisleridir')
TEP=B('Tepe noktası biçimi','tepe noktası (r, k) olan parabolün denklemi y = a(x − r)² + k biçimindedir; grafiğin bir noktası verilirse a bulunur. Örnek: tepe noktası (1, 2) ve (0, 5) noktasından geçen parabolde 5 = a · 1 + 2 olduğundan a = 3’tür')
MUT=B('Mutlak değerli grafik','y = |f(x)| grafiği, y = f(x) grafiğinin x ekseninin altında kalan kısmının eksene göre simetriğinin alınmasıyla çizilir; böylece grafik hiçbir yerde x ekseninin altına inmez. Örnek: f(x) = x − 2 için |f(x)| grafiği (2, 0) noktasında kırılır')
DEG=B('Değişken değiştirme','denklemde tekrar eden ifade yeni bir harfle yazılarak denklem sadeleştirilir; bulunan değerler için eski değişkenle denklem yeniden çözülür. Örnek: (x² + x)² = 4 denkleminde t = x² + x denirse t² = 4 olur')
ORAN=B('Kökler arasındaki ilişki','kökler arasında bir ilişki (örneğin x₁ = 3x₂) verilirse ilişkiden yararlanılarak kökler tek bilinmeyenle yazılır, sonra toplam ve çarpım formülleri uygulanır. Örnek: x₁ = 3x₂ ise x₁ + x₂ = 4x₂ ve x₁ · x₂ = 3x₂² olur')
ALAN=B('Alan ve denklem','dikdörtgenin alanı çarpım olduğundan kenarlar aynı bilinmeyenle yazılınca alan denklemi ikinci dereceden bir denkleme dönüşür; bulunan kökler uzunluk olarak anlamlı mı diye denetlenir. Örnek: kenarları x ve x + 1 olan dikdörtgenin alanı 12 ise x² + x − 12 = 0 olur ve yalnız pozitif kök kabul edilir')
HIZ=B('Hız, yol ve süre','sabit hızla giden bir cismin yolu = hız × süre olduğundan süre = yol / hız’dır. Örnek: 90 km’lik yolu saatte 30 km hızla gidenin süresi 90/30 = 3 saattir')
TAB=B('Tablodan fonksiyon bulma','ikinci dereceden f(x) = ax² + bx + c fonksiyonunda üç değer tablodaki üç denklemi verir; denklemlerden a, b ve c bulunur. Örnek: f(0) = 4 ise c = 4 olur')
UST=B('Özdeşlik','(a − 1/a)² = a² − 2 + 1/a² ve a³ − 1/a³ = (a − 1/a)³ + 3(a − 1/a). Örnek: a − 1/a = 2 ise a² + 1/a² = 6’dır')
SAY=B('Sayı doğrusunda uzaklık','iki reel kökün sayı doğrusundaki uzaklığı |x₁ − x₂|’dir ve (x₁ − x₂)² = (x₁ + x₂)² − 4x₁x₂ ile hesaplanır. Örnek: x₁ + x₂ = 5 ve x₁ · x₂ = 4 ise |x₁ − x₂| = √(25 − 16) = 3’tür')
GRK=B('Parabolün katsayılarının işareti','y = ax² + bx + c parabolünde a > 0 ise kollar yukarı, a < 0 ise aşağıdır; c, grafiğin y eksenini kestiği değerdir; tepe noktasının apsisi −b/(2a)’dır; x eksenini iki noktada kesiyorsa Δ > 0’dır; x = 1 için y değeri a + b + c’dir. Örnek: f(x) = x² − 2x + 3 için f(1) = 1 − 2 + 3 = 2 = a + b + c’dir')

# ---------------- kartlar (tipId başına bir kart) ----------------
kartla('K-AIK-01','Kökler toplamı ve çarpımı','Kökler bulunmadan ifade, toplam ve çarpım cinsinden yazılır; x₁² + x₂², 1/x₁ + 1/x₂ ve |x₁ − x₂| gibi ifadeler özdeşliklerle bu iki değere indirgenir.','Toplamın işaretini (−b/a) ters almak; a ≠ 1 iken a’ya bölmeyi unutmak; kare toplamdan 2x₁x₂ yerine x₁x₂ çıkarmak.','orta','öncüllü',4,'ik-vieta','Kökler toplamı ve çarpımı')
kartla('K-AIK-02','Diskriminant ve kök koşulu','Kök sayısı ve türü Δ’nın işaretiyle belirlenir; parametreli denklemde Δ, parametrenin ikinci dereceden ifadesi olur ve işaret incelemesi yapılır.','Δ’da b’nin karesini almamak ya da 4ac yerine ac yazmak; Δ = 0 ile Δ ≥ 0’ı karıştırmak; uç değerleri dahil etmek.','orta','düz',3,'ik-diskr','Diskriminant ve kök koşulu')
kartla('K-AIK-03','Kökleri verilen denklem kurma','Yeni köklerin toplamı ve çarpımı eski köklerin toplam ve çarpımı cinsinden yazılır; denklem x² − Tx + Ç = 0 biçiminde kurulur.','Toplamın işaretini yanlış yazmak; eski kökler toplamını yeni kökler toplamı sanmak; çarpımı kare almadan yazmak.','orta','düz',4,'ik-kurma','Kökleri verilen denklem kurma')
kartla('K-AIK-04','Ortak kök ve kökler arası ilişki','Ortak kökte denklemler çıkarılarak kök bulunur ve yerine konur; kök ilişkisi (x₁ = 2x₂ gibi) verilirse kökler tek bilinmeyenle yazılıp çarpım ve toplam kullanılır; iki işaretli durum birlikte düşünülür.','Ortak kök bulunca parametreyi bulmayı unutmak; kök ilişkisinde yalnız bir işaret durumunu almak; ters işaretli köklü durumu atlamak.','zor','düz',4,'ik-iliski','Ortak kök ve kökler arası ilişki')
kartla('K-AIK-05','Parabol grafiği ve kökler','Grafikten kökler, tepe noktası ve eksen kesim değerleri okunur; bu veriler denklem kurmada ya da kökler toplamı ve çarpımı hesabında kullanılır; mutlak değerli grafikte doğru ile kesişim sayısı grafiğe bakılarak belirlenir.','Okunan kök işaretini ters yazmak; tepe noktası yerine kök okumak; mutlak değerli grafikte katlanan kısmı unutmak.','orta','grafik',4,'ik-parabol','Parabol grafiği ve kökler')
kartla('K-AIK-06','Denkleme dönüşen problem','Bilinmeyen uzunluk, hız ya da sayı seçilir, durum ikinci dereceden denkleme dönüştürülür; kökler soruya uygunluk (pozitiflik, sınır) için denetlenir.','Negatif kökü elemeyi unutmak; iki kökün toplamını cevap sanmak; kenar ifadesini yanlış kurmak (x yerine 2x).','orta','hikâyeli',4,'ik-problem','Denkleme dönüşen problem')
kartla('K-AIK-07','Değişken değiştirme','Tekrarlanan ifade yeni değişkenle yazılır; her değer için asıl denklem ayrı çözülür; Δ’sı negatif denklemler çözüme katılmaz.','Yeni değişkenin değerini asıl bilinmeyen sanmak; karmaşık kökleri toplama katmak; çarpanları yanlış eşleştirmek.','zor','düz',5,'ik-donus','Değişken değiştirme')
kartla('K-AIK-08','Köklerin sayı doğrusundaki konumu','Köklerin uzaklığı ya da konumu (x₁ − x₂)² = (x₁ + x₂)² − 4x₁x₂ ile parametreye bağlanır; kareköke dikkat edilir.','Uzaklığı Δ’ya eşitlemek (karekökü unutmak); işaretli farkı mutlak değersiz bırakmak.','orta','şekilli',3,'ik-konum','Köklerin sayı doğrusundaki konumu')

# ================= şekil yardımcıları =================
def graf(x0,x1,y0,y1,sx,sy,govde,xs=1,ys=1,xl=1,yl=1,xlab='x',ylab='y',fs='\\footnotesize',izgara=True,kenar=False):
    o=[]
    if izgara:
        for i in range(x0,x1+1,xs): o.append(f'\\draw[gray!30,thin] ({i*sx:.3f},{y0*sy:.3f}) -- ({i*sx:.3f},{y1*sy:.3f});')
        for j in range(y0,y1+1,ys): o.append(f'\\draw[gray!30,thin] ({x0*sx:.3f},{j*sy:.3f}) -- ({x1*sx:.3f},{j*sy:.3f});')
    o.append(f'\\draw[-{{Stealth}},thick] ({(x0-0.4)*sx:.3f},0) -- ({(x1+0.8)*sx:.3f},0) node[right] {{${xlab}$}};')
    o.append(f'\\draw[-{{Stealth}},thick] (0,{(y0-0.4)*sy:.3f}) -- (0,{(y1+0.8)*sy:.3f}) node[above] {{${ylab}$}};')
    for i in range(x0,x1+1):
        if i!=0 and i%xl==0: o.append(f'\\node[below=2pt,font={fs}] at ({i*sx:.3f},0) {{${i}$}};')
    for j in range(y0,y1+1):
        if j!=0 and j%yl==0: o.append(f'\\node[left=2pt,font={fs}] at ({(x0 if kenar else 0)*sx:.3f},{j*sy:.3f}) {{${j}$}};')
    o.append(f'\\node[below right=1pt,font={fs}] at (0,0) {{$O$}};')
    o.append(govde); return '\n'.join(o)
def egri(a,b,c,d0,d1,sx,sy,renk=BL,w='1.8pt'):
    return f'\\draw[{renk},line width={w},smooth,domain={d0}:{d1},samples=80,variable=\\t] plot ({{\\t*{sx}}},{{({a}*\\t*\\t+({b})*\\t+({c}))*{sy}}});'
def nokta(px,py,sx,sy,renk=OR,r=0.09): return f'\\fill[{renk}] ({px*sx:.3f},{py*sy:.3f}) circle ({r});'
def etiket(px,py,sx,sy,s,yon='above',renk='black',fs='\\footnotesize'): return f'\\node[{yon},font={fs},text={renk}] at ({px*sx:.3f},{py*sy:.3f}) {{{s}}};'
def oncul(listesi): return '\n'.join(f'{r} {m}' for r,m in listesi)

# ============================ 0001 · kolay · düz · Vieta ============================
r=sp.solve(2*x**2-10*x+6,x); v=sp.simplify((r[0]+1)*(r[1]+1)); assert v==9
S1,P1=5,3
e=[P1-S1+1,P1+S1,6+10+1,S1+2]; assert e==[-1,8,17,7] and len({9,*e})==5
q('0001',tipId='ik-vieta',tip='Kökler toplamı ve çarpımı',z='kolay',alt='Kökler Toplamı ve Çarpımı',kaz='İkinci dereceden denklemin köklerini bulmadan kökler toplamı ve çarpımıyla verilen ifadenin değerini hesaplar.',kalip='düz',
 kart='K-AIK-01 (kökler toplamı ve çarpımı) · (x₁ + 1)(x₂ + 1) çarpımı',
 metin='2x² − 10x + 6 = 0 denkleminin kökleri x₁ ve x₂ olduğuna göre, (x₁ + 1)(x₂ + 1) çarpımı kaçtır?',
 dogru=9,yan=[(e[0],'Kökler toplamını −b/a yerine b/a alıp −5 bulmuş: 3 − 5 + 1.','islem'),(e[1],'Çarpımı açarken sondaki +1’i unutmuş: x₁x₂ + x₁ + x₂ = 3 + 5.','dikkat'),(e[2],'Toplam ve çarpımı a = 2’ye bölmeden −b = 10 ve c = 6 almış: 6 + 10 + 1.','bilgi'),(e[3],'Çarpım yerine (x₁ + 1) + (x₂ + 1) toplamını hesaplamış: 5 + 2.','dikkat')],
 istenen='(x₁ + 1)(x₂ + 1) çarpımının değeri.',ip=['Çarpımı açtığında, kökleri tek tek bulmadan hesaplayabileceğin hangi iki büyüklük kalıyor?'],bilgi=[VIE],
 ad=[A('Toplam ve çarpımı yaz','a = 2, b = −10, c = 6 olduğundan kökler toplamı −b/a, çarpımı c/a’dır.','x₁ + x₂ = 10/2 = 5 · x₁ × x₂ = 6/2 = 3'),A('Çarpımı aç','Parantezler çarpılır ve toplam ile çarpım ayrıştırılır.','(x₁ + 1)(x₂ + 1) = x₁x₂ + x₁ + x₂ + 1'),A('Değerleri yerleştir','Bulunan toplam ve çarpım yazılır.','3 + 5 + 1 = 9')],
 puf='Köklerin kendisi sorulmuyorsa kökleri bulmadan toplam ve çarpıma indirge.')

# ============================ 0002 · kolay · şekilli · parabol grafiği ============================
a2,b2=-2,-8
assert sp.expand((x+2)*(x-4))==x**2+a2*x+b2 and a2+b2==-10
e=[sp.expand((x-2)*(x+4)).coeff(x,1)+sp.expand((x-2)*(x+4)).coeff(x,0), a2+8, -(2+4)+8, b2]; assert e==[-6,6,2,-8] and len({-10,*e})==5
sx,sy=0.5,0.3
g=egri(1,-2,-8,-2.46,4.46,sx,sy)+nokta(-2,0,sx,sy)+nokta(4,0,sx,sy)
SK=fig(graf(-3,5,-9,3,sx,sy,g,xl=1,yl=2,kenar=True))
q('0002',tipId='ik-parabol',tip='Parabol grafiği ve kökler',z='kolay',alt='Parabol Grafiği',kaz='Grafikte x eksenini kestiği noktalardan parabolün denklemindeki katsayıları bulur.',kalip='grafik',
 kart='K-AIK-05 (parabol grafiği ve kökler) · kökler grafikten okunur, katsayılar toplamı',
 metin='Şekilde y = x² + ax + b parabolünün grafiği verilmiştir.\nBuna göre, a + b toplamı kaçtır?',
 dogru=-10,yan=[(e[0],'Kökleri −2 ve 4 yerine 2 ve −4 okuyup (x − 2)(x + 4) = x² + 2x − 8 yazmış: a = 2, b = −8.','dikkat'),(e[1],'Çarpımı +8 almış (kökleri aynı işaretli sanmış): a = −2, b = 8.','islem'),(e[2],'Kökleri −2 ve 4 yerine 2 ve 4 okumuş: −a = 6 → a = −6 ve b = 8 bulup toplamı 2 yazmış.','dikkat'),(e[3],'a + b yerine yalnız b’yi (kökler çarpımını) yazmış.','dikkat')],
 istenen='a + b toplamı.',ip=['Parabolün x eksenini kestiği noktalar, y = 0 için hangi denklemin çözümüdür?'],bilgi=[PAR,VIE],sekil=SK,
 ad=[A('Kökleri oku','Parabol x eksenini iki noktada keser; bu apsisler köklerdir.','x₁ = −2 · x₂ = 4'),A('Toplam ve çarpımı yaz','Baş katsayı 1 olduğundan −a = x₁ + x₂ ve b = x₁ · x₂ olur.','−a = 2 → a = −2 · b = −8'),A('Toplamı bul','a ve b toplanır.','−2 + (−8) = −10')],
 puf='Parabolün kökleri x eksenini kestiği noktalardır; işaretlerini grafikten dikkatle oku.')

# ============================ 0003 · orta · düz · denklem kurma ============================
a_,b_=sp.symbols('a b'); S3,P3=6,4
t=sp.simplify(sp.Rational(S3**2-2*P3,P3)); assert t==7
assert eqs(7,1)=='x² − 7x + 1 = 0' and eqs(28,1)=='x² − 28x + 1 = 0'
OP=[eqs(28,1),eqs(7,1),eqs(-7,1),eqs(7,4),eqs(6,1)]
assert len(set(OP))==5 and OP[2]=='x² + 7x + 1 = 0'
q('0003',tipId='ik-kurma',tip='Kökleri verilen denklem kurma',z='orta',alt='Denklem Kurma',kaz='Bir denklemin kökleriyle ifade edilen yeni kökler için ikinci dereceden denklem kurar.',kalip='düz',
 kart='K-AIK-03 (kökleri verilen denklem kurma) · yeni kökler a/b ve b/a',
 metin='x² − 6x + 4 = 0 denkleminin kökleri a ve b olduğuna göre, kökleri a/b ve b/a olan ikinci dereceden denklem aşağıdakilerden hangisidir?',
 dogru=OP[1],sira=OP,yan=[(OP[0],'Yeni kökler toplamını a² + b² = 28 bulup b · a = 4’e bölmeyi unutmuş.','islem'),(OP[2],'Yeni kökler toplamını doğru (7) bulmuş ancak denklemde toplamın işaretini + yazmış.','bilgi'),(OP[3],'Çarpımı (a/b)(b/a) = 1 yerine a · b = 4 olarak yazmış.','dikkat'),(OP[4],'Yeni kökler toplamı yerine eski kökler toplamını (a + b = 6) denkleme yazmış.','dikkat')],
 istenen='Kökleri a/b ve b/a olan ikinci dereceden denklem.',ip=['Yeni köklerin toplamında ortak payda kullandığında payda hangi büyüklüğü verir?'],bilgi=[VIE,KUR],
 ad=[A('Eski toplam ve çarpım','Verilen denklemden a + b ve a · b yazılır.','a + b = 6 · a × b = 4'),A('Kareler toplamı','a² + b² = (a + b)² − 2ab ile hesaplanır.','36 − 8 = 28'),A('Yeni toplam ve çarpım','a/b + b/a ortak paydayla toplanır; çarpım sadeleşir.','(a² + b²)/(ab) = 28/4 = 7 · (a/b) × (b/a) = 1'),A('Denklemi kur','x² − (toplam)x + çarpım = 0 yazılır.','x² − 7x + 1 = 0')],
 puf='Yeni köklerin toplamını ve çarpımını eski toplam-çarpım cinsinden yazıp denklemi kur.')

# ============================ 0004 · orta · düz · ortak kök ============================
m=sp.symbols('m'); f1=lambda mm:x**2-(mm+1)*x+12; f2=lambda mm:x**2-(mm+3)*x+20
sol=sp.solve([f1(m).subs(x,sp.Symbol('r')),f2(m).subs(x,sp.Symbol('r'))],[m,sp.Symbol('r')],dict=True); assert len(sol)==1 and sol[0][m]==6 and sol[0][sp.Symbol('r')]==4
assert set(sp.solve(f1(6),x))&set(sp.solve(f2(6),x))=={4}
assert 16+4*(-8+1)+12==0
e=[-8,4,7,9]; assert len({6,*e})==5
q('0004',tipId='ik-iliski',tip='Ortak kök ve kökler arası ilişki',z='orta',alt='Ortak Kök',kaz='İki ikinci dereceden denklemin ortak kökünü bulup parametrenin değerini hesaplar.',kalip='düz',
 kart='K-AIK-04 (ortak kök) · iki denklem, parametre m',
 metin='m bir gerçel sayı olmak üzere,\nx² − (m + 1)x + 12 = 0\nx² − (m + 3)x + 20 = 0\ndenklemlerinin ortak bir kökü vardır.\nBuna göre, m kaçtır?',
 dogru=6,yan=[(e[0],'Çıkarmadan sonra −2x + 8 = 0’dan x = −4 bulmuş (işaret hatası); birinci denkleme yazınca 16 + 4(m + 1) + 12 = 0 ve m = −8 çıkmış.','dikkat'),(e[1],'Ortak kökü (x = 4) bulmuş ve bunu m sanıp bırakmış.','dikkat'),(e[2],'Ortak kökü yerine koyup m + 1 = 7 bulmuş, ancak son adımda 1’i çıkarmayı unutmuş.','islem'),(e[3],'Ortak kökü ikinci denkleme koyup m + 3 = 9 bulmuş ve 3’ü çıkarmayı unutmuş.','islem')],
 istenen='m’nin değeri.',ip=['Ortak kök her iki denklemi de sağlar; bundan nasıl yararlanabilirsin?'],bilgi=[ORT],
 ad=[A('Denklemleri çıkar','İkinci denklemden birinciyi çıkarınca x² terimleri sadeleşir.','[x² − (m + 3)x + 20] − [x² − (m + 1)x + 12] = 0 → −2x + 8 = 0'),A('Ortak kökü bul','Ortak kök bu denklemi de sağlar.','x = 4'),A('Birinci denkleme yaz','x = 4 yerine konur.','16 − 4(m + 1) + 12 = 0 → m + 1 = 7'),A('Parametreyi bul','m çekilir; ikinci denklemle denetlenir.','m = 6 · 16 − 36 + 20 = 0')],
 puf='Ortak kökü bulduktan sonra parametreyi bulmayı unutma ve sonucu ikinci denklemle denetle.')

# ============================ 0005 · kolay · düz · diskriminant ============================
dd=sp.discriminant(x**2-6*x+m+1,x); assert sp.solve(dd,m)==[8]
e=[9,10,3,17]; assert 36-4*9==0 and 36-4*(10-1)==0 and 36-2*(17+1)==0 and len({8,*e})==5
q('0005',tipId='ik-diskr',tip='Diskriminant ve kök koşulu',z='kolay',alt='Çakışık Kök',kaz='Denklemin eşit iki reel kökü olması koşulundan parametreyi bulur.',kalip='düz',
 kart='K-AIK-02 (diskriminant ve kök koşulu) · Δ = 0 koşulu',
 metin='m bir gerçel sayı olmak üzere, x² − 6x + m + 1 = 0 denkleminin birbirine eşit iki reel kökü vardır.\nBuna göre, m kaçtır?',
 dogru=8,yan=[(e[0],'Sabit terimi m sanıp 36 − 4m = 0 çözmüş.','dikkat'),(e[1],'Sabit terimi m − 1 alıp 36 − 4(m − 1) = 0 yazmış (işaret hatası).','islem'),(e[2],'Eşit iki kökün değerini (x = 3) bulup bunu m sanmış.','dikkat'),(e[3],'Diskriminantta 4ac yerine 2ac kullanmış: 36 − 2(m + 1) = 0.','bilgi')],
 istenen='m’nin değeri.',ip=['Eşit iki reel kök olması, diskriminant için hangi koşulu gerektirir?'],bilgi=[DIS],
 ad=[A('Katsayıları yaz','a = 1, b = −6, c = m + 1 alınır.','Δ = b² − 4ac'),A('Δ = 0 koşulu','Çakışık kök için diskriminant sıfır olmalıdır.','36 − 4(m + 1) = 0'),A('m’yi bul','Denklem çözülür.','m + 1 = 9 → m = 8')],
 puf='Eşit iki reel kök, diskriminantın sıfır olması demektir.')

# ============================ 0006 · orta · öncüllü · Vieta ============================
r6=sp.solve(x**2-4*x+2,x); r1,r2=r6
assert sp.simplify(r1**2+r2**2)==12 and sp.simplify(1/r1+1/r2)==2 and sp.simplify(abs(r1-r2))==2*sp.sqrt(2)
SR=['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III']
assert (4**2-2)==14 and sp.Rational(2,4)==sp.Rational(1,2)
q('0006',tipId='ik-vieta',tip='Kökler toplamı ve çarpımı',z='orta',alt='Kök İfadeleri',kaz='Kökler toplamı ve çarpımıyla köklerin kareleri toplamını, çarpmaya göre terslerinin toplamını ve aralarındaki farkı değerlendirir.',kalip='öncüllü',
 kart='K-AIK-01 (kökler toplamı ve çarpımı) · öncüllü: kareler toplamı, terslerin toplamı, kökler farkı',
 metin='x² − 4x + 2 = 0 denkleminin kökleri x₁ ve x₂ olmak üzere,\nI. x₁² + x₂² = 12\nII. 1/x₁ + 1/x₂ = 2\nIII. |x₁ − x₂| = 2\nifadelerinden hangileri doğrudur?',
 dogru='I ve II',sira=SR,yan=[(SR[0],'II’yi 1/x₁ + 1/x₂ = (x₁x₂)/(x₁ + x₂) = 2/4 yazarak yanlış bulmuş; III’ü doğru olarak elemiş.','bilgi'),(SR[1],'I’i (x₁ + x₂)² − x₁x₂ = 14 hesaplayarak (2x₁x₂ yerine x₁x₂ çıkarıp) yanlış bulmuş; II’yi doğru görmüş.','islem'),(SR[3],'II’de ters kesir hatası yapıp yanlış saymış; III’te (x₁ − x₂)² = 8 değerinin kareköküne 2 diyerek doğru kabul etmiş.','islem'),(SR[4],'I ve II’yi doğru bulmuş; III’te (x₁ − x₂)² = 8 değerinin karekökünü 2 alarak doğru saymış.','islem')],
 istenen='Doğru olan öncüllerin hangileri olduğu.',ip=['Her öncülü, kökler toplamı ve çarpımı cinsinden yazmayı dene.'],bilgi=[VIE,SAY],
 ad=[A('Toplam ve çarpım','Denklemden kökler toplamı ve çarpımı yazılır.','x₁ + x₂ = 4 · x₁ × x₂ = 2'),A('I’i hesapla','x₁² + x₂² = (x₁ + x₂)² − 2x₁x₂.','16 − 4 = 12 → I doğru'),A('II’yi hesapla','Ortak paydada toplanır.','(x₁ + x₂)/(x₁x₂) = 4/2 = 2 → II doğru'),A('III’ü hesapla','(x₁ − x₂)² = (x₁ + x₂)² − 4x₁x₂.','16 − 8 = 8 → |x₁ − x₂| = 2√2 ≠ 2 → III yanlış')],
 puf='Kökler arasındaki simetrik ifadeler toplam ve çarpım cinsinden yazılır; farkta karekökü unutma.')

# ============================ 0007 · orta · şekilli · parabol ve doğru ============================
f7=(x-2)**2-1; g7=2*x-2; assert sp.expand(f7)==x**2-4*x+3 and f7.subs(x,0)==3
dif=sp.expand(f7-g7); assert dif==x**2-6*x+5 and sp.Poly(dif,x).all_coeffs()[2]==5
rr=sp.solve(dif,x); assert sorted(rr)==[1,5] and rr[0]*rr[1]==5
assert sorted(sp.solve(f7,x))==[1,3] and 3*1==3
e=[1,3,6,-2]; assert 3+(-2)==1 and len({5,*e})==5
sx,sy=0.55,0.3
g=egri(1,-4,3,-0.8,5.1,sx,sy)+'\n'+f'\\draw[{OR},line width=1.8pt] ({-0.8*sx:.3f},{(2*-0.8-2)*sy:.3f}) -- ({5.1*sx:.3f},{(2*5.1-2)*sy:.3f});'
g+='\n'.join([nokta(2,-1,sx,sy,BL),nokta(0,3,sx,sy,BL),nokta(0,-2,sx,sy,OR),nokta(2,2,sx,sy,OR),
 etiket(2,-1,sx,sy,'$T(2,-1)$','below right',BL),etiket(0.1,3.1,sx,sy,'$(0,3)$','above right',BL),etiket(0.1,-2.1,sx,sy,'$(0,-2)$','below right',OR),etiket(2,2,sx,sy,'$(2,2)$','above left',OR),
 etiket(-0.8,6.84,sx,sy,'$f$','left',BL,'\\normalsize'),etiket(5.1,8.2,sx,sy,'$g$','right',OR,'\\normalsize')])
SK=fig(graf(-1,6,-4,9,sx,sy,g,xl=1,yl=2))
q('0007',tipId='ik-parabol',tip='Parabol grafiği ve kökler',z='orta',alt='Parabol ve Doğru',kaz='Tepe noktası ve bir noktası verilen parabol ile iki noktası verilen doğrunun kesişim noktalarının apsislerini denklem kurarak bulur.',kalip='grafik',
 kart='K-AIK-05 (parabol grafiği ve kökler) · parabol ile doğrunun kesişimi, apsisler çarpımı',
 metin='Şekilde, tepe noktası T olan f parabolü ile g doğrusu çizilmiştir; işaretli noktaların koordinatları şekilde verilmiştir.\nBuna göre, f ve g grafiklerinin kesişim noktalarının apsisleri çarpımı kaçtır?',
 dogru=5,yan=[(e[0],'f(x) = g(x) denklemini kurarken sabit terimleri toplamış: 3 + (−2) = 1.','islem'),(e[1],'Kesişim yerine f(x) = 0 denkleminin kökleri çarpımını (x² − 4x + 3 → 3) hesaplamış.','dikkat'),(e[2],'Çarpım yerine kesişim apsislerinin toplamını (x² − 6x + 5 → 6) almış.','dikkat'),(e[3],'Doğrunun y eksenini kestiği değeri çarpım sanmış.','dikkat')],
 istenen='Kesişim noktalarının apsisleri çarpımı.',ip=['Tepe noktası ve bir noktası verilen parabolün denklemini yazmak için hangi biçim uygundur?'],bilgi=[TEP,KES],sekil=SK,
 ad=[A('f’yi yaz','Tepe noktası (2, −1) olduğundan f(x) = a(x − 2)² − 1; (0, 3) noktasından a bulunur.','3 = 4a − 1 → a = 1 · f(x) = x² − 4x + 3'),A('g’yi yaz','(0, −2) ve (2, 2) noktalarından eğim hesaplanır.','eğim = (2 + 2)/2 = 2 · g(x) = 2x − 2'),A('Denklemi kur','f(x) = g(x) eşitlenir.','x² − 4x + 3 = 2x − 2 → x² − 6x + 5 = 0'),A('Çarpımı bul','Kökler çarpımı c/a’dır.','x₁ × x₂ = 5 (kökler 1 ve 5)')],
 puf='Grafiklerin kesişimi, fonksiyonları eşitleyip çıkan denklemin köklerini bulmaktır.')

# ============================ 0008 · orta · öncüllü · diskriminant ============================
fm_=lambda mm: x**2-2*(mm-1)*x+mm+5
d4=lambda mm:(mm-1)**2-(mm+5)
assert d4(4)==0 and d4(6)==14>0 and (-5+5)==0 and sp.Poly(fm_(-5),x).all_coeffs()[2]==0
assert (6-1)**2-4*(6+5)<0 and (4-1)**2-4*(4+5)!=0
SR=['Yalnız I','Yalnız II','I ve II','I ve III','II ve III']
q('0008',tipId='ik-diskr',tip='Diskriminant ve kök koşulu',z='orta',alt='Kök Koşulları',kaz='Parametreli denklemde belirli m değerleri için diskriminant ve sabit terimden kök durumunu değerlendirir.',kalip='öncüllü',
 kart='K-AIK-02 (diskriminant ve kök koşulu) · öncüllü: çakışık kök, kök yok, sıfır kök',
 metin='m bir gerçel sayı olmak üzere, x² − 2(m − 1)x + m + 5 = 0 denklemi için\nI. m = 4 ise denklemin eşit iki reel kökü vardır.\nII. m = 6 ise denklemin reel kökü yoktur.\nIII. m = −5 ise denklemin köklerinden biri sıfırdır.\nifadelerinden hangileri doğrudur?',
 dogru='I ve III',sira=SR,yan=[(SR[0],'III’ü “kökün 0 olması için x’in katsayısı 0 olmalı” diyerek yanlış bulmuş; I’i ve II’yi doğru değerlendirmiş.','bilgi'),(SR[1],'Δ’da b yerine (m − 1) alıp I’i yanlış, II’yi doğru bulmuş; III’ü de x katsayısına bakarak yanlış saymış.','islem'),(SR[2],'II’de denklemi x² − 10x + 11 = 0 yazıp “11 > 10 olduğundan kök yok” sanmış; III’ü x katsayısına bağlayıp yanlış bulmuş.','dikkat'),(SR[4],'Δ’yı hesaplarken b yerine (m − 1) kullanmış: I yanlış (9 − 36 ≠ 0), II doğru (25 − 44 < 0) çıkmış; III’ü doğru bulmuş.','islem')],
 istenen='Doğru olan öncüllerin hangileri olduğu.',ip=['Her öncülde m değerini yerine koyarak denklemin diskriminantına ya da sabit terimine bak.'],bilgi=[DIS,VIE],
 ad=[A('Δ ifadesini yaz','Katsayılar a = 1, b = −2(m − 1), c = m + 5; Δ/4 ile çalışmak kolaydır.','Δ/4 = (m − 1)² − (m + 5)'),A('I’i denetle','m = 4 yazılır.','9 − 9 = 0 → eşit iki kök → I doğru'),A('II’yi denetle','m = 6 yazılır.','25 − 11 = 14 > 0 → iki farklı kök → II yanlış'),A('III’ü denetle','Sabit terim sıfırsa x = 0 köktür.','m = −5 → c = 0 → denklem x² + 12x = 0, kökler 0 ve −12 → III doğru')],
 puf='Parametreli denklemde her öncül için m değerini yerine koyup denklemi sadeleştir.')

# ============================ 0009 · orta · şekilli · yürüyüş yolu ============================
xx=sp.symbols('xx'); sol=sp.solve((20-2*xx)*(14-2*xx)-160,xx); assert sorted(sol)==[2,15]
assert sp.expand((20-2*xx)*(14-2*xx)-160)==4*xx**2-68*xx+120
e=[4,5,6,15]; assert sorted(sp.solve((20-xx)*(14-xx)-160,xx))==[4,30] and sorted(sp.solve((20-2*xx)*(14-2*xx)-40,xx))==[5,12] and sorted(sp.solve((20-2*xx)*(14-2*xx)-16,xx))==[6,11]
s=0.18; W,Hh=20*s,14*s; dd_=3.2*s
SK=fig(f'''\\fill[{OR}!25] (0,0) rectangle ({W},{Hh});
\\fill[vurgu!30] ({dd_},{dd_}) rectangle ({W-dd_},{Hh-dd_});
\\draw[thick] (0,0) rectangle ({W},{Hh});
\\draw[thick,vurgu!70!black] ({dd_},{dd_}) rectangle ({W-dd_},{Hh-dd_});
\\node[font=\\small] at ({W/2},{Hh/2}) {{Çim alan}}; \\node[font=\\small\\bfseries] at ({W/2},{Hh/2-0.45}) {{160 m$^2$}};
\\node[font=\\scriptsize,{OR}!70!black] at ({W/2},{dd_/2}) {{yol}};
\\draw[<->] (0,{Hh+0.3}) -- ({W},{Hh+0.3}); \\node[above,font=\\small] at ({W/2},{Hh+0.3}) {{20 m}};
\\draw[<->] ({W+0.3},0) -- ({W+0.3},{Hh}); \\node[right,font=\\small] at ({W+0.3},{Hh/2}) {{14 m}};''')
q('0009',tipId='ik-problem',tip='Denkleme dönüşen problem',z='orta',alt='Alan Problemi',kaz='Dikdörtgen bahçenin çevresindeki eşit genişlikli yolun genişliğini ikinci dereceden denklem kurup kökleri anlamlılık açısından değerlendirerek bulur.',kalip='şekilli',
 kart='K-AIK-06 (denkleme dönüşen problem) · bahçe çevresinde eşit genişlikli yol, alan denklemi',
 metin='Şekildeki dikdörtgen biçimli bahçenin çevresine her yerde aynı genişlikte bir yürüyüş yolu yapılacaktır. Yol yapıldıktan sonra yolun iç tarafında kalan çim alanın büyüklüğü şekilde verilmiştir.\nŞekil ölçekli çizilmemiştir.\nBuna göre, yürüyüş yolunun genişliği kaç metredir?',
 dogru=2,yan=[(e[0],'Yolun genişliğini iki kenardan da çıkarmak yerine yalnız bir kez çıkarıp (20 − x)(14 − x) = 160 çözmüş: x = 4.','islem'),(e[3],'x² − 17x + 30 = 0 denkleminin kökleri 2 ve 15 iken büyük kökü seçmiş; negatif/uygunsuz kökü elemeyi unutmuş.','dikkat'),(e[1],'Çim alanı 160 yerine 40 almış (160’ı 4’e bölmüş): x² − 17x + 60 = 0, x = 5.','islem'),(e[2],'Çim alanı 160 yerine 16 almış (bir sıfırı atlamış): x² − 17x + 66 = 0, x = 6.','dikkat')],
 istenen='Yürüyüş yolunun genişliği (metre).',ip=['Yolun genişliğine x dersen çim alanın kenarları kaç olur?'],bilgi=[ALAN],sekil=SK,
 ad=[A('Çim alanın kenarları','Yol bahçenin her iki yanından da x kadar yer kaplar.','uzun kenar 20 − 2x · kısa kenar 14 − 2x'),A('Alan denklemi','Çim alan 160 m² olmalıdır.','(20 − 2x)(14 − 2x) = 160 → 4x² − 68x + 120 = 0'),A('Denklemi çöz','Her iki taraf 4’e bölünür ve çarpanlara ayrılır.','x² − 17x + 30 = 0 → (x − 2)(x − 15) = 0'),A('Kökü denetle','14 − 2x > 0 olmalıdır; x = 15 olamaz.','x = 2')],
 puf='Problemde bulduğun köklerden hangisinin durumla uyuştuğunu mutlaka denetle.')

# ============================ 0010 · orta · tablo · f(x) = 10 ============================
f10=lambda t:2*t**2-4*t-6
assert [f10(0),f10(1),f10(3)]==[-6,-8,0]
r10=sp.solve(f10(x)-10,x); assert sorted(r10)==[-2,4] and r10[0]*r10[1]==-8
e=[-16,-3,2,8]; assert sp.Rational(-16,2)==-8 and 3*-1==-3 and -2+4==2 and len({-8,*e})==5
SK=tablo_svg(['x','0','1','3'],[['f(x)','−6','−8','0']])
q('0010',tipId='ik-parabol',tip='Parabol grafiği ve kökler',z='orta',alt='Tablodan Fonksiyon',kaz='Tablodaki üç değerden ikinci dereceden fonksiyonu bulup f(x) = k denkleminin kökler çarpımını hesaplar.',kalip='tablo',
 kart='K-AIK-05 (parabol grafiği ve kökler) · tablodan f(x) = ax² + bx + c bulma, f(x) = 10',
 metin='f, ikinci dereceden bir fonksiyondur. Aşağıdaki tabloda f fonksiyonunun bazı değerleri verilmiştir.\nBuna göre, f(x) = 10 denkleminin kökler çarpımı kaçtır?',
 dogru=-8,yan=[(e[0],'f(x) = 10 denklemini 2x² − 4x − 16 = 0 yazıp çarpımı c = −16 almış; baş katsayı 2’ye bölmeyi unutmuş.','islem'),(e[1],'f(x) = 10 yerine f(x) = 0 denklemini çözmüş: çarpım −6/2 = −3.','dikkat'),(e[2],'Kökler çarpımı yerine kökler toplamını (−b/a = 2) hesaplamış.','dikkat'),(e[3],'Çarpımı −16/2 yerine −(−16)/2 = 8 alarak işaret hatası yapmış.','islem')],
 istenen='f(x) = 10 denkleminin kökler çarpımı.',ip=['Tablodaki bir değer sabit terimi doğrudan verir; kalan iki değerle ne yapabilirsin?'],bilgi=[TAB,VIE],sekil=SK,
 ad=[A('Sabit terimi bul','f(0) = c olduğundan tablodan c okunur.','c = −6'),A('Katsayıları bul','f(1) ve f(3) için iki denklem kurulur.','a + b − 6 = −8 · 9a + 3b − 6 = 0'),A('Denklemleri çöz','İlk denklemden b = −2 − a yazılır ve ikincide yerine konur.','9a − 6 − 3a − 6 = 0 → a = 2, b = −4 · f(x) = 2x² − 4x − 6'),A('f(x) = 10 denklemi','Denklem düzenlenir ve kökler çarpımı c/a alınır.','2x² − 4x − 16 = 0 → x₁ × x₂ = −16/2 = −8')],
 puf='Tablodaki değerlerden fonksiyonu bulduktan sonra istenen denklemi baştan düzenle.')

# ============================ 0011 · kolay · şekilli · dikdörtgen ============================
ss=sp.solve(xx*(xx+3)-70,xx); assert sorted(ss)==[-10,7]; cev=2*(7+10); assert cev==34
e=[10,17,20,46]; assert 7+10==17 and 2*(10+13)==46 and 2*(7+3)==20 and len({34,*e})==5
s=0.35
SK=fig(f'''\\fill[vurgu!15] (0,0) rectangle ({10*s},{7*s}); \\draw[thick] (0,0) rectangle ({10*s},{7*s});
\\node[font=\\small] at ({5*s},{3.5*s+0.2}) {{Alan}}; \\node[font=\\small\\bfseries] at ({5*s},{3.5*s-0.25}) {{70 m$^2$}};
\\draw[<->] (0,{7*s+0.3}) -- ({10*s},{7*s+0.3}); \\node[above,font=\\small] at ({5*s},{7*s+0.3}) {{$x+3$ m}};
\\draw[<->] ({-0.3},0) -- ({-0.3},{7*s}); \\node[left,font=\\small] at (-0.3,{3.5*s}) {{$x$ m}};''')
q('0011',tipId='ik-problem',tip='Denkleme dönüşen problem',z='kolay',alt='Dikdörtgen Çevresi',kaz='Kenarları bilinmeyenle verilen dikdörtgenin alanından denklem kurup çevresini hesaplar.',kalip='şekilli',
 kart='K-AIK-06 (denkleme dönüşen problem) · kenarlar x ve x + 3, alan verilmiş, çevre sorulur',
 metin='Şekildeki dikdörtgen biçimli reklam panosunun kenar uzunlukları ve alanı şekilde verilmiştir. Panonun dört kenarına baştan sona bir sıra ışıklı şerit çekilecektir.\nBuna göre, kullanılacak şerit kaç metredir?',
 dogru=34,yan=[(e[0],'Denklemi çözüp yalnız uzun kenarı (x + 3 = 10) bulmuş; çevreyi hesaplamamış.','dikkat'),(e[1],'Yarı çevreyi (7 + 10) hesaplayıp 2 ile çarpmayı unutmuş.','islem'),(e[3],'Negatif kökü (x = −10) mutlak değerle alıp kenarları 10 ve 13 saymış: 2 × (10 + 13).','dikkat'),(e[2],'Kenarları 7 ve 3 sanıp (x + 3 yerine 3’ü ikinci kenar almış) 2 × (7 + 3) hesaplamış.','dikkat')],
 istenen='Tel örgünün uzunluğu (metre).',ip=['Kenarları x ve x + 3 olan dikdörtgenin alanı hangi denklemle ifade edilir?'],bilgi=[ALAN],sekil=SK,
 ad=[A('Alan denklemi','Kenarlar çarpılıp alana eşitlenir.','x(x + 3) = 70 → x² + 3x − 70 = 0'),A('Kökleri bul','Çarpanlarına ayrılır.','(x + 10)(x − 7) = 0 → x = 7 ya da x = −10'),A('Uzunluğu denetle','Kenar uzunluğu negatif olamaz.','x = 7 · kenarlar 7 ve 10'),A('Çevreyi hesapla','Çevre = 2 × (7 + 10).','2 × 17 = 34')],
 puf='Uzunluk soruyorsan negatif kökü hemen ele.')

# ============================ 0012 · orta · şekilli · sayı doğrusunda uzaklık ============================
kk=sp.symbols('kk'); assert sp.solve(sp.Eq(36-4*(2*kk-1),16),kk)==[3]
assert sorted(sp.solve(x**2-6*x+5,x))==[1,5]
e=[sp.Rational(5,2),sp.Rational(9,2),5,2]; assert sp.solve(sp.Eq(36-8*kk,16),kk)==[sp.Rational(5,2)] and sp.solve(sp.Eq(36-4*(2*kk-1),4),kk)==[sp.Rational(9,2)] and 2*3-1==5 and 5-1==4 and len({3,*e})==5
SK=fig(f'''\\draw[-{{Stealth}},thick] (-0.5,0) -- (6.3,0) node[right] {{$x$}};
\\foreach \\p in {{0.1,1.0,1.9,2.8,3.7,4.6,5.5}} \\draw (\\p,-0.08) -- (\\p,0.08);
\\fill[{BL}] (1.0,0) circle (0.1); \\fill[{BL}] (4.6,0) circle (0.1);
\\node[below=4pt,font=\\normalsize,text={BL}] at (1.0,0) {{$x_1$}}; \\node[below=4pt,font=\\normalsize,text={BL}] at (4.6,0) {{$x_2$}};
\\draw[<->,{OR},thick] (1.0,0.65) -- (4.6,0.65); \\node[above,font=\\normalsize,text={OR}] at (2.8,0.65) {{4 birim}};
\\draw[gray,dashed] (1.0,0.1) -- (1.0,0.65); \\draw[gray,dashed] (4.6,0.1) -- (4.6,0.65);''')
q('0012',tipId='ik-konum',tip='Köklerin sayı doğrusundaki konumu',z='orta',alt='Kökler Arası Uzaklık',kaz='Köklerin sayı doğrusundaki uzaklığını (x₁ − x₂)² = (x₁ + x₂)² − 4x₁x₂ ile parametreye bağlar.',kalip='şekilli',
 kart='K-AIK-08 (köklerin sayı doğrusundaki konumu) · kökler arası uzaklık, parametre k',
 metin='k bir gerçel sayı olmak üzere, x² − 6x + 2k − 1 = 0 denkleminin iki farklı reel kökü x₁ ve x₂’dir. Bu kökler sayı doğrusunda şekildeki gibi gösterilmiş, aralarındaki uzaklık şekilde verilmiştir.\nBuna göre, k kaçtır?',
 dogru=3,yan=[(e[0],'Sabit terimi 2k alıp (x₁ − x₂)² = 36 − 8k = 16 çözmüş.','dikkat'),(e[1],'Uzaklığı Δ’ya eşitlemiş (karekökü unutmuş): 36 − 4(2k − 1) = 4.','bilgi'),(e[2],'Kökleri 1 ve 5 bulmuş, çarpım 2k − 1 = 5 olduğundan k’yı 5 olarak bırakmış.','islem'),(e[3],'Kökleri 1 ve 5 bulup 2k − 1 = 5’te −1’i karşı tarafa yanlış taşımış: 2k = 5 − 1 = 4, k = 2.','islem')],
 istenen='k’nın değeri.',ip=['İki kök arasındaki uzaklığın karesini kökler toplamı ve çarpımı cinsinden yazabilir misin?'],bilgi=[SAY],sekil=SK,
 ad=[A('Toplam ve çarpım','Denklemden kökler toplamı ve çarpımı yazılır.','x₁ + x₂ = 6 · x₁ × x₂ = 2k − 1'),A('Uzaklığın karesi','(x₁ − x₂)² = (x₁ + x₂)² − 4x₁x₂ ve uzaklık 4’tür.','16 = 36 − 4(2k − 1)'),A('k’yı çöz','Denklem düzenlenir.','8k − 4 = 20 → 8k = 24 → k = 3'),A('Denetle','k = 3 için denklem x² − 6x + 5 = 0.','kökler 1 ve 5 → uzaklık 4')],
 puf='Kökler arası uzaklık verilince (x₁ − x₂)² ifadesini toplam ve çarpımla yaz.')

# ============================ 0013 · orta · şekilli · hareket ============================
vv=sp.symbols('vv',positive=True); assert sp.solve(60/vv-60/(vv+5)-1,vv)==[15]
e=[5,12,20,35]; assert 60//5==12 and 15+5==20 and 15+20==35 and len({15,*e})==5
SK=fig(f'''\\draw[thick,{BL}] (0,0) -- (6,0); \\fill[{BL}] (0,0) circle (0.12); \\fill[{BL}] (6,0) circle (0.12);
\\node[below=4pt,font=\\normalsize\\bfseries] at (0,0) {{A}}; \\node[below=4pt,font=\\normalsize\\bfseries] at (6,0) {{B}};
\\draw[<->,{OR},thick] (0,0.55) -- (6,0.55); \\node[above,font=\\normalsize] at (3,0.55) {{60 km}};''')
q('0013',tipId='ik-problem',tip='Denkleme dönüşen problem',z='orta',alt='Hız Problemi',kaz='Yol, hız ve süre ilişkisinden ikinci dereceden denklem kurup hızı bulur.',kalip='hikâyeli',
 kart='K-AIK-06 (denkleme dönüşen problem) · hız artınca süre kısalır; denklem v² + 5v − 300 = 0',
 metin='Ayşe, şekildeki A ve B kentleri arasındaki yolu bisikletiyle sabit hızla gidiyor. Hızı saatte 5 km daha fazla olsaydı bu yolu 1 saat daha kısa sürede alacaktı.\nBuna göre, Ayşe’nin gerçek hızı saatte kaç km’dir?',
 dogru=15,yan=[(e[0],'Hızdaki artışı (5 km/sa) hızın kendisi sanmış.','dikkat'),(e[1],'Yolu 60/5 diyerek artış hızına bölmüş (12).','islem'),(e[2],'Denklemi doğru çözmüş fakat artırılmış hızı (v + 5 = 20) cevap vermiş.','dikkat'),(e[3],'Gerçek hız ile artırılmış hızı (15 + 20) toplamış.','dikkat')],
 istenen='Ayşe’nin gerçek hızı (km/sa).',ip=['Gerçek hız v olsun; iki durumdaki süreleri yol/hız ile yazıp farklarını 1 saate eşitle.'],bilgi=[HIZ],sekil=SK,
 ad=[A('Süreleri yaz','Hız v olsun; süre = yol / hız.','gerçek süre 60/v · yeni süre 60/(v + 5)'),A('Farkı kur','İki süre arasındaki fark 1 saattir.','60/v − 60/(v + 5) = 1'),A('Düzenle','Her iki taraf v(v + 5) ile çarpılır.','60(v + 5) − 60v = v² + 5v → v² + 5v − 300 = 0'),A('Çöz ve denetle','Hız pozitif olmalıdır.','(v + 20)(v − 15) = 0 → v = 15 · 60/15 = 4 saat, 60/20 = 3 saat')],
 puf='Süre farkı veren hız problemleri ikinci dereceden denklem verir; negatif hızı ele.')

# ============================ 0014 · orta · öncüllü · parabol grafiği ============================
a14,b14,c14=1,-2,-3; assert sp.expand((x+1)*(x-3))==x**2-2*x-3
assert b14**2-4*a14*c14>0 and a14*b14<0 and a14+b14+c14<0
SR=['Yalnız I','Yalnız III','I ve II','I ve III','I, II ve III']
s=0.7
SK=fig(f'''\\draw[-{{Stealth}},thick] (-2.2,0) -- (3.6,0) node[right] {{$x$}}; \\draw[-{{Stealth}},thick] (0,-3.4) -- (0,2.6) node[above] {{$y$}};
\\node[below left=1pt,font=\\small] at (0,0) {{$O$}};
\\draw[{BL},line width=1.8pt,smooth,domain=-1.55:3.55,samples=80,variable=\\t] plot ({{\\t*{s}}},{{(\\t*\\t-2*\\t-3)*{s}*0.62}});
\\draw[gray,dashed] ({s},0) -- ({s},{-4*s*0.62}); \\fill[{OR}] ({s},{-4*s*0.62}) circle (0.08);
\\draw ({s},-0.08) -- ({s},0.08); \\node[above=2pt,font=\\small] at ({s},0) {{$1$}};
\\node[{BL},font=\\normalsize] at (3.3,1.6) {{$y=ax^2+bx+c$}};''')
q('0014',tipId='ik-parabol',tip='Parabol grafiği ve kökler',z='orta',alt='Katsayıların İşareti',kaz='Parabolün grafiğinden a, b, c işaretlerini, diskriminantın işaretini ve f(1) = a + b + c değerinin işaretini yorumlar.',kalip='öncüllü',
 kart='K-AIK-05 (parabol grafiği ve kökler) · öncüllü: Δ, a·b, a + b + c işaretleri',
 metin='Şekilde y = ax² + bx + c parabolünün grafiği verilmiştir.\nBuna göre,\nI. b² − 4ac > 0\nII. a · b > 0\nIII. a + b + c > 0\nifadelerinden hangileri doğrudur?',
 dogru='Yalnız I',sira=SR,yan=[(SR[1],'Parabolün x eksenini iki noktada kesmesini Δ = 0 sanıp I’i yanlış bulmuş; x = 1’de değeri pozitif varsayıp III’ü doğru kabul etmiş.','bilgi'),(SR[2],'Tepe noktası y ekseninin sağında olduğundan b > 0 diye düşünüp II’yi doğru kabul etmiş (b işareti −b/2a’nın işaretinin tersidir).','bilgi'),(SR[3],'III’ü doğru kabul etmiş: x = 1’de grafiğin x ekseninin altında olduğunu gözden kaçırıp a > 0 olduğu için a + b + c’yi pozitif saymış.','dikkat'),(SR[4],'II’de b’nin işaretini yanlış belirlemiş, III’te de grafiğin x = 1’deki konumunu yanlış okumuş.','bilgi')],
 istenen='Doğru olan öncüllerin hangileri olduğu.',ip=['Kolların yönü, tepe noktasının konumu ve x = 1’deki grafik noktasının x eksenine göre yeri hangi işaretleri verir?'],bilgi=[GRK],sekil=SK,
 ad=[A('Kolların yönü','Kollar yukarı bakıyor.','a > 0'),A('I’i değerlendir','Parabol x eksenini iki noktada kesiyor.','Δ > 0 → I doğru'),A('II’yi değerlendir','Tepe noktası y ekseninin sağında: −b/(2a) > 0 ve a > 0.','b < 0 → a × b < 0 → II yanlış'),A('III’ü değerlendir','x = 1’de grafik x ekseninin altındadır.','f(1) = a + b + c < 0 → III yanlış')],
 puf='Katsayıların işaretini kolların yönü, y eksenini kesim noktası ve tepe noktasının konumundan oku.')

# ============================ 0015 · zor · grafik · |x² − 4x| = m ============================
def say(mv): return len(set(sp.solve(x**2-4*x-mv,x))|set(sp.solve(x**2-4*x+mv,x)))
assert [mv for mv in range(1,9) if say(mv)==3]==[4]
assert len(sp.solve(x**2-4*x-4,x))==2 and sp.solve(x**2-4*x+4,x)==[2]
tum=set(sp.solve(x**2-4*x-4,x))|{2}; assert sum(tum)==6 and len(tum)==3
e=[-4,2,4,8]; assert 4+2+2==8 and len({6,*e})==5
sx,sy=0.8,0.5
sg=egri(1,-4,0,-1,0,sx,sy)+'\n'+egri(-1,4,0,0,4,sx,sy)+'\n'+egri(1,-4,0,4,5,sx,sy)
SK=fig(graf(-1,5,0,5,sx,sy,sg+'\n'+nokta(0,0,sx,sy)+nokta(4,0,sx,sy)+f'\\node[{BL},font=\\normalsize] at ({2*sx},{5.6*sy}) {{$y=f(x)$}};',xl=1,yl=100,izgara=False,fs='\\small'))
q('0015',tipId='ik-parabol',tip='Parabol grafiği ve kökler',z='zor',alt='Mutlak Değerli Grafik',kaz='Mutlak değerli ikinci dereceden fonksiyonun grafiğinden kesişim sayısı koşulunu yorumlayıp köklerin toplamını hesaplar.',kalip='grafik',
 kart='K-AIK-05 (parabol grafiği ve kökler) · f(x) = |x² + ax + b| grafiği, f(x) = m’nin üç kökü',
 metin='Şekilde, f(x) = |x² + ax + b| fonksiyonunun grafiği verilmiştir. m bir gerçel sayı olmak üzere f(x) = m denkleminin tam üç farklı reel kökü vardır.\nBuna göre, bu köklerin toplamı kaçtır?',
 dogru=6,yan=[(e[1],'Yalnız çakışık kökü (x = 2) almış; diğer iki kökü katmamış.','dikkat'),(e[0],'Kökler toplamı yerine x² − 4x − 4 = 0 denkleminin kökler çarpımını (−4) yazmış.','dikkat'),(e[2],'Yalnızca x² − 4x − 4 = 0 denkleminin kökleri toplamını (4) almış; çakışık kökü katmamış.','islem'),(e[3],'Çakışık kökü iki kez sayıp 4 + 2 + 2 = 8 bulmuş.','islem')],
 istenen='f(x) = m denkleminin köklerinin toplamı.',ip=['Yatay bir doğrunun yüksekliği değiştikçe grafikle kesişim sayısı nasıl değişir?'],bilgi=[MUT],sekil=SK,
 ad=[A('Fonksiyonu bul','x ekseni 0 ve 4’te kesiliyor; x² + ax + b = x(x − 4).','f(x) = |x² − 4x|'),A('m değerini bul','Üç kök ancak yatay doğru, katlanan kısmın tepe noktasından geçerse oluşur; tepe noktası (2, 4).','m = 4'),A('İki denklemi yaz','f(x) = 4 ise x² − 4x = 4 ya da x² − 4x = −4.','x² − 4x − 4 = 0 · x² − 4x + 4 = 0'),A('Kökleri topla','Birinci denklemin kökleri toplamı 4, ikincinin çakışık kökü 2’dir.','(2 + 2√2) + (2 − 2√2) + 2 = 6')],
 puf='Mutlak değerli grafikte tam üç kök, yatay doğrunun katlanan kısmın tepe noktasından geçmesini ister.')

# ============================ 0016 · zor · öncüllü · a³ − 1/a³ ============================
ap=max(sp.solve(x**2-3*x-1,x)); an=min(sp.solve(x**2-3*x-1,x))
for a_v in (ap,an):
    assert sp.simplify(a_v-1/a_v)==3 and sp.simplify(a_v**2+1/a_v**2)==11 and sp.simplify(a_v**3-1/a_v**3)==36 and sp.simplify(a_v+1/a_v)**2!=9
assert sp.simplify(ap+1/ap)**2==13 and 3**2-2==7 and 3**3-3*3==18 and 27!=36
SR=['Yalnız I','Yalnız II','Yalnız III','II ve III','I, II ve III']
q('0016',tipId='ik-vieta',tip='Kökler toplamı ve çarpımı',z='zor',alt='Kök ve Özdeşlik',kaz='Denklemi sağlayan a değeri için a ile 1/a’nın toplam ve farkından üretilen kuvvet ifadelerini özdeşliklerle değerlendirir.',kalip='öncüllü',
 kart='K-AIK-01 (kökler toplamı ve çarpımı) · öncüllü: a − 1/a = 3 üzerinden kare ve küp ifadeleri',
 metin='a, x² − 3x − 1 = 0 denkleminin köklerinden biri olmak üzere,\nI. a + 1/a = 3\nII. a² + 1/a² = 11\nIII. a³ − 1/a³ = 36\nifadelerinden hangileri doğrudur?',
 dogru='II ve III',sira=SR,yan=[(SR[0],'a² − 3a − 1 = 0 eşitliğini a’ya bölürken işaret hatası yapıp a + 1/a = 3 bulmuş; II için 3² − 2 = 7, III için 3³ − 3 · 3 = 18 bularak yalnız I’i doğru saymış.','islem'),(SR[1],'a − 1/a = 3 ile II’yi doğru bulmuş; III’te küpünü alıp (a − 1/a)³ = 27 bulmuş ve 3(a − 1/a) terimini eklememiş.','bilgi'),(SR[2],'a − 1/a = 3 bulmuş, ancak II için 3² − 2 = 7 hesaplamış (kareyi açarken +2 yerine −2), böylece II’yi yanlış saymış.','islem'),(SR[4],'II ve III’ü doğru hesaplamış; I’i, a’ya bölünce çıkan −1/a terimini +1/a okuyarak doğru saymış.','dikkat')],
 istenen='Doğru olan öncüllerin hangileri olduğu.',ip=['a ≠ 0 iken denklemden a ile 1/a arasında bir bağıntı çıkarabilir misin?'],bilgi=[UST],
 ad=[A('Denklemi a’ya böl','a bir köktür ve sıfır olamaz.','a² − 3a − 1 = 0 → a − 3 − 1/a = 0 → a − 1/a = 3'),A('I’i değerlendir','a + 1/a değeri a − 1/a = 3’ten bulunamaz; a + 1/a = ±√13 çıkar.','(a + 1/a)² = 9 + 4 = 13 → I yanlış'),A('II’yi hesapla','Karesini alıp açarız.','(a − 1/a)² = a² − 2 + 1/a² = 9 → a² + 1/a² = 11 → II doğru'),A('III’ü hesapla','Küp özdeşliği kullanılır.','a³ − 1/a³ = 27 + 3 × 3 = 36 → III doğru')],
 puf='a ve 1/a içeren ifadelerde önce a ± 1/a değerini bul, sonra özdeşliklerle kuvvetlere çık.')

# ============================ 0017 · zor · düz · kök ilişkisi ============================
mm=sp.symbols('mm'); xx2=sp.symbols('xx2')
degs=[]
for r2_ in sp.solve(2*xx2**2-18,xx2):
    r1_=2*r2_; ss_=r1_+r2_; degs.append(ss_-1)
assert sorted(degs)==[-10,8] and degs[0]*degs[1]==-80
for mv in (8,-10):
    rt=sorted(sp.solve(x**2-(mv+1)*x+18,x)); assert rt[1]==2*rt[0] or rt[0]==2*rt[1]
e=[-81,-2,8,80]; assert 9*-9==-81 and 8+(-10)==-2 and len({-80,*e})==5
q('0017',tipId='ik-iliski',tip='Ortak kök ve kökler arası ilişki',z='orta',alt='Kök İlişkisi',kaz='Kökler arasında verilen oransal ilişkiden parametrenin alabileceği değerleri bulup çarpar.',kalip='düz',
 kart='K-AIK-04 (kökler arası ilişki) · x₁ = 2x₂, parametrenin değerlerinin çarpımı',
 metin='m bir gerçel sayı olmak üzere, x² − (m + 1)x + 18 = 0 denkleminin kökleri x₁ ve x₂’dir.\nx₁ = 2x₂ olduğuna göre, m’nin alabileceği değerlerin çarpımı kaçtır?',
 dogru=-80,yan=[(e[0],'m + 1 = 9 ve m + 1 = −9 değerlerini çarpmış (−81); 1’i çıkararak m’ye geçmeyi unutmuş.','dikkat'),(e[1],'m’nin iki değerinin çarpımı yerine toplamını (8 + (−10)) hesaplamış.','dikkat'),(e[2],'Yalnızca pozitif kökler durumunu alıp m = 8 bulmuş; negatif kökleri atlamış.','bilgi'),(e[3],'İki m değerini bulmuş, ancak çarpımda negatif işareti atlamış: 8 × 10.','islem')],
 istenen='m’nin alabileceği değerlerin çarpımı.',ip=['Köklerden birini diğeri cinsinden yazınca çarpım denkleminden bir bilinmeyenli bir denklem çıkar; kaç farklı çözüm var?'],bilgi=[VIE,ORAN],
 ad=[A('Kökleri tek bilinmeyenle yaz','x₂ = t dersek x₁ = 2t olur.','x₁ + x₂ = 3t · x₁ × x₂ = 2t²'),A('Çarpımdan t’yi bul','Çarpım 18’e eşittir; t iki değer alabilir.','2t² = 18 → t = 3 ya da t = −3'),A('Toplamdan m’yi bul','Toplam m + 1’e eşittir.','3t = m + 1 → t = 3: m = 8 · t = −3: m = −10'),A('Değerleri çarp','İki durum da reel kök verir.','8 × (−10) = −80')],
 puf='Kökler arasında bir ilişki verilince kökleri tek bilinmeyenle yaz; ters işaretli durumu unutma.')

# ============================ 0018 · zor · düz · kökleri a ve b ============================
sol=sp.solve([a_+b_+a_,a_*b_-b_],[a_,b_],dict=True)
nz=[s_ for s_ in sol if s_[a_]!=0 and s_[b_]!=0]; assert len(nz)==1 and nz[0][a_]==1 and nz[0][b_]==-2
aa,bb=1,-2; assert sorted(sp.solve(x**2+aa*x+bb,x))==[-2,1] and eqs(aa**2+bb**2,aa**2*bb**2)=='x² − 5x + 4 = 0'
OP=[eqs(5,-2),eqs(1,4),eqs(-5,4),eqs(5,2),eqs(5,4)]; assert len(set(OP))==5
q('0018',tipId='ik-kurma',tip='Kökleri verilen denklem kurma',z='zor',alt='Kökleri Verilen Denklem',kaz='Kökleri katsayılar olan denklemde katsayıları bulup yeni kökler için denklem kurar.',kalip='düz',
 kart='K-AIK-03 (kökleri verilen denklem kurma) · x² + ax + b = 0 denkleminin kökleri a ve b; yeni kökler a², b²',
 metin='a ve b sıfırdan farklı gerçel sayılar olmak üzere, x² + ax + b = 0 denkleminin kökleri a ve b’dir.\nBuna göre, kökleri a² ve b² olan ikinci dereceden denklem aşağıdakilerden hangisidir?',
 dogru=OP[4],sira=OP,yan=[(OP[0],'Yeni kökler toplamını a² + b² = 5 bulmuş, çarpımı a² · b² yerine a · b = −2 yazmış.','dikkat'),(OP[1],'Yeni kökler toplamı yerine (a + b)² = 1 almış; çarpımı doğru (4) bulmuş.','bilgi'),(OP[2],'Yeni kökler toplamı olan 5’i denkleme +5x yazmış (işaret hatası).','islem'),(OP[3],'Çarpımı |a · b| = 2 almış, kare almayı unutmuş.','islem')],
 istenen='Kökleri a² ve b² olan ikinci dereceden denklem.',ip=['Kökler ile katsayılar arasındaki bağıntılar a ve b için neler söylüyor?'],bilgi=[VIE,KUR],
 ad=[A('Toplam ve çarpım','Kökler a ve b; katsayılar da a ve b.','toplam: a + b = −a · çarpım: ab = b'),A('a’yı bul','Çarpım eşitliği b ≠ 0 ile sadeleşir.','a × b = b → a = 1'),A('b’yi bul','Toplam eşitliğinden b çekilir.','1 + b = −1 → b = −2'),A('Yeni toplam ve çarpım','Kökler a² = 1 ve b² = 4.','toplam 5 · çarpım 4'),A('Denklemi kur','x² − (toplam)x + çarpım = 0 yazılır.','x² − 5x + 4 = 0')],
 puf='Katsayıları da kök olan denklemlerde iki eşitlik yazıp önce a ve b’yi bul.')

# ============================ 0019 · zor · şekilli · dik üçgenin içinde dikdörtgen ============================
sol=sp.solve(sp.Rational(3,4)*(12-xx)*xx-24,xx); assert sorted(sol)==[4,8]
dik=[(4,6),(8,3)]; assert all(w*h==24 and sp.Rational(h)==9-sp.Rational(3,4)*w for w,h in dik)
cevr=[2*(w+h) for w,h in dik]; assert cevr==[20,22] and sum(cevr)==42
e=[12,20,22,24]; assert 4+8==12 and len({42,*e})==5
s=0.3
SK=fig(f'''\\fill[gray!10] (0,0) -- ({12*s},0) -- (0,{9*s}) -- cycle;
\\fill[{BL}!25,opacity=0.8] (0,0) rectangle ({3.3*s},{6.525*s}); \\draw[{BL},thick] (0,0) rectangle ({3.3*s},{6.525*s});
\\fill[{OR}!25,opacity=0.8] (0,0) rectangle ({8.6*s},{2.55*s}); \\draw[{OR},thick] (0,0) rectangle ({8.6*s},{2.55*s});
\\draw[thick] (0,0) -- ({12*s},0) -- (0,{9*s}) -- cycle;
\\draw (0.25,0) -- (0.25,0.25) -- (0,0.25);
\\node[below left,font=\\normalsize] at (0,0) {{A}}; \\node[below right,font=\\normalsize] at ({12*s},0) {{B}}; \\node[above left,font=\\normalsize] at (0,{9*s}) {{C}};
\\node[below,font=\\small] at ({6*s},-0.05) {{12}}; \\node[left,font=\\small] at (0,{4.5*s}) {{9}};
\\node[right,font=\\small,text={BL}] at ({4.4*s+0.0},{7.8*s}) {{$\\blacksquare$ Alan = 24}}; \\node[right,font=\\small,text={OR}] at ({4.4*s},{6.7*s}) {{$\\blacksquare$ Alan = 24}};''')
q('0019',tipId='ik-problem',tip='Denkleme dönüşen problem',z='zor',alt='Üçgen İçinde Dikdörtgen',kaz='Dik üçgenin içindeki dikdörtgende benzerlikten bir kenarı diğerine bağlayıp alan denklemini çözerek çevreleri bulur.',kalip='şekilli',
 kart='K-AIK-06 (denkleme dönüşen problem) · dik üçgen içinde köşesi dik açı köşesinde dikdörtgen, iki farklı yerleştirme',
 metin='Şekilde, A köşesinde dik açılı ABC üçgeni ile bu üçgenin içine yerleştirilebilen, bir köşesi A noktasında ve kenarları [AB] ile [AC] üzerinde bulunan ve karşı köşesi [BC] üzerinde olan, alanı şekilde belirtilen iki farklı dikdörtgen gösterilmiştir. Dik kenar uzunlukları şekilde santimetre cinsinden verilmiştir; şekil ölçekli çizilmemiştir.\nBuna göre, bu iki dikdörtgenin çevreleri toplamı kaç santimetredir?',
 dogru=42,yan=[(e[0],'Denklemin kökleri toplamını (4 + 8) çevreler toplamı sanmış.','dikkat'),(e[1],'Yalnız bir dikdörtgenin çevresini (4 ve 6’lı) hesaplamış.','dikkat'),(e[2],'Yalnız ikinci dikdörtgenin çevresini (8 ve 3’lü) hesaplamış.','dikkat'),(e[3],'Çevreler toplamı yerine alanı yazmış.','dikkat')],
 istenen='İki dikdörtgenin çevreleri toplamı (cm).',ip=['Dikdörtgenin köşesi hipotenüs üzerindeyse iki kenarı arasında hangi benzerlik bağıntısı vardır?'],bilgi=[ALAN],sekil=SK,
 ad=[A('Kenarları ilişkilendir','Dikdörtgenin A’daki kenarları AB ve AC üzerindedir; karşı köşe BC üzerinde olduğundan benzerlikten y = 9 − 3x/4 (x: AB üzerindeki kenar).','y/9 = (12 − x)/12'),A('Alan denklemi','x · y = 24.','x(9 − 3x/4) = 24 → x² − 12x + 32 = 0'),A('Kökleri bul','Çarpanlarına ayrılır.','(x − 4)(x − 8) = 0 → x = 4 (y = 6) ya da x = 8 (y = 3)'),A('Çevreleri bul','Her çevre 2(x + y) ile hesaplanır.','2(4 + 6) = 20 · 2(8 + 3) = 22'),A('Topla','İki çevre toplanır.','20 + 22 = 42')],
 puf='Kenarlar arasında benzerlikle bağıntı kurup alanı tek bilinmeyenli ikinci dereceden denkleme çevir.')

# ============================ 0020 · zor · düz · değişken değiştirme ============================
cz=sp.solve((x-1)*(x-2)*(x-3)*(x-4)-24,x); rel=[c for c in cz if c.is_real]
assert sorted(rel)==[0,5] and sum(rel)==5 and len(cz)==4
assert sp.expand((x-1)*(x-2)*(x-3)*(x-4))==x**4-10*x**3+35*x**2-50*x+24
e=[-10,0,2,10]; assert 1+2+3+4==10 and len({5,*e})==5
q('0020',tipId='ik-donus',tip='Değişken değiştirme',z='zor',alt='Dört Çarpanlı Denklem',kaz='Dört çarpanlı denklemi uygun gruplayıp değişken değiştirerek ikinci dereceden denkleme indirger ve reel kökleri bulur.',kalip='düz',
 kart='K-AIK-07 (değişken değiştirme) · (x − 1)(x − 2)(x − 3)(x − 4) = 24, reel kökler toplamı',
 metin='(x − 1)(x − 2)(x − 3)(x − 4) = 24\ndenkleminin reel köklerinin toplamı kaçtır?',
 dogru=5,yan=[(e[0],'t = x² − 5x değişkeninden elde ettiği t’lerin toplamını (0 + (−10)) kökler toplamı sanmış.','dikkat'),(e[1],'t(t + 10) = 0 denkleminde t’ye bölüp yalnız t = −10 almış; x² − 5x + 10 = 0’ın reel kökü olmadığından toplam 0 bulmuş.','islem'),(e[2],'Reel köklerin toplamı yerine kök sayısını (2) yazmış.','dikkat'),(e[3],'Dördüncü dereceden denklemin tüm köklerinin (karmaşık dahil) toplamını (−(−10) = 10) cevap vermiş.','bilgi')],
 istenen='Reel köklerin toplamı.',ip=['Çarpanları uygun ikiliye ayırdığında iki ikinci dereceden ifadenin x² ve x terimleri nasıl görünüyor?'],bilgi=[DEG],
 ad=[A('Çarpanları eşle','Uçtaki ve ortadaki çarpanlar birlikte çarpılır.','(x − 1)(x − 4) = x² − 5x + 4 · (x − 2)(x − 3) = x² − 5x + 6'),A('Değişken değiştir','t = x² − 5x denir.','(t + 4)(t + 6) = 24 → t² + 10t = 0'),A('t’yi bul','Çarpanlarına ayrılır.','t(t + 10) = 0 → t = 0 ya da t = −10'),A('x’i bul','Her t için x² − 5x = t çözülür.','t = 0: x = 0, x = 5 · t = −10: Δ = 25 − 40 < 0, reel kök yok'),A('Topla','Yalnız reel kökler toplanır.','0 + 5 = 5')],
 puf='Simetrik çarpanları eşleyip ortak ifadeyi yeni değişken yap; Δ < 0 olan denklemden reel kök gelmez.')

# ---------------- bitiş ----------------
for qq in P.ANA: qq['kardes']=None
P.yaz(os.path.join(HD,'ikinci-1.json'),'/dev/null')
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=UK))['kartlar'].append(c['id'])
json.dump(dict(konu=P.konu_adi,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 AYT Matematik çıkmış soruları ve yayın soru bankaları (yalnız mantık), MEB 10–11. sınıf müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','ikinci.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
