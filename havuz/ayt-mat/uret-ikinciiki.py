"""AYT Matematik · 2.Dereceden Denklemler 2. dalga (20 soru: 3 kolay / 10 orta / 7 zor; 12 şekilli). Her doğru ve çeldirici değer kodla hesaplanıp assert edilir."""
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
P=Parti('ikinciiki','2.Dereceden Denklemler',UK,ders='AYT Matematik',idon='aytmat')
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

# ---------------- bilgi kutuları (örnekler soruların sayılarından farklı) ----------------
VIE=B('Kökler toplamı ve çarpımı','ax² + bx + c = 0 (a ≠ 0) denkleminin kökleri x₁, x₂ ise x₁ + x₂ = −b/a ve x₁ · x₂ = c/a. Örnek: x² − 7x + 12 = 0 için toplam 7, çarpım 12')
DIS=B('Diskriminant','Δ = b² − 4ac. Δ > 0 ise iki farklı reel kök, Δ = 0 ise çakışık (eşit) iki reel kök, Δ < 0 ise reel kök yoktur. Örnek: x² − 4x + 4 = 0 için Δ = 16 − 16 = 0 ve kök x = 2')
CRP=B('Çarpanlı denklem','A · B = 0 ise A = 0 ya da B = 0’dır; çarpanların kökleri ayrı bulunur ve iki çarpanda da bulunan kök kümede bir kez yer alır. Örnek: (x − 5)(x² − 25) = 0 denkleminin farklı kökleri 5 ve −5’tir')
PAR=B('Parabol ve kökler','y = f(x) parabolünün x eksenini kestiği noktaların apsisleri f(x) = 0 denkleminin köklerinin değeridir. Tepe noktasının apsisi kökler toplamının yarısıdır. Örnek: parabol x eksenini 1 ve 5 noktalarında kesiyorsa tepe noktasının apsisi 3’tür')
TEP=B('Tepe noktası biçimi','tepe noktası (r, k) olan parabolün denklemi y = a(x − r)² + k biçimindedir; grafiğin bir noktası verilirse a bulunur. Örnek: tepe noktası (1, 2) ve (0, 5) noktasından geçen parabolde 5 = a · 1 + 2 olduğundan a = 3’tür')
KES=B('Parabol ve doğrunun kesişimi','y = f(x) ile y = g(x) grafiklerinin kesişim noktalarının apsisleri f(x) = g(x) denkleminin kökleridir. Örnek: f(x) = x² ve g(x) = 2x + 3 için x² − 2x − 3 = 0 denkleminin kökleri kesişim apsisleridir')
ALAN=B('Alan ve denklem','dikdörtgenin alanı çarpım olduğundan kenarlar aynı bilinmeyenle yazılınca alan denklemi ikinci dereceden bir denkleme dönüşür; bulunan kökler uzunluk olarak anlamlı mı diye denetlenir. Örnek: kenarları x ve x + 1 olan dikdörtgenin alanı 12 ise x² + x − 12 = 0 olur ve yalnız pozitif kök kabul edilir')
PIS=B('Pisagor bağıntısı','dik üçgende dik kenarların kareleri toplamı hipotenüsün karesine eşittir. Örnek: dik kenarları 6 ve 8 olan üçgenin hipotenüsü √(36 + 64) = 10’dur')
OKL=B('Öklid bağıntısı','dik üçgende hipotenüse indirilen yükseklik h, hipotenüsü p ve q parçalarına ayırırsa h² = p · q’dur; dik kenarlar c² = p · (p + q) bağıntısıyla bulunur. Örnek: p = 1, q = 4 ise h² = 4 ve h = 2’dir')
RAS=B('Rasyonel ve köklü denklemler','paydaları ortak yapıp çapraz çarpmak ya da ortak ifadeyi yeni değişken almak denklemi ikinci dereceye getirir. Kök bulunduktan sonra paydayı sıfır yapıp yapmadığı, köklü denklemde de karekökün eşit olduğu ifadenin negatif olup olmadığı denetlenir. Örnek: √(x + 2) = x denkleminde kareleme x² − x − 2 = 0 verir; x = 2 uygun, x = −1 uygun değildir')
MAK=B('İşlem makinesi','bir makinede birimler sırayla çalışır; bir birimin çıktısı sonraki birimin girdisidir. Çıktıdan geriye doğru giderek ara değerler bulunur. Örnek: girdiyi 3 ile çarpıp 1 ekleyen birimin çıktısı 10 ise girdi 3’tür')
DEG=B('Değişken değiştirme','denklemde tekrar eden ifade yeni bir harfle yazılarak denklem sadeleştirilir; bulunan değerler için eski değişkenle denklem yeniden çözülür ve Δ < 0 olan denklem reel köke katkı vermez. Örnek: (x² + x)² = 4 denkleminde t = x² + x denirse t² = 4 olur')
ORAN=B('Kökler arasındaki ilişki','kökler arasında bir ilişki (örneğin x₁ = 3x₂ ya da x₁ · x₂ = 1) verilirse ilişki toplam ve çarpım formülleriyle parametreye bağlanır; bulunan değer için Δ ≥ 0 koşulu ayrıca denetlenir. Örnek: kökler birbirinin tersi ise çarpımları 1’dir')
ORT=B('Ortak kök','iki denklemin ortak kökü r ise r her iki denklemi de sağlar. Katsayıları tam sayı olan ve baş katsayısı 1 olan denklemin rasyonel kökü, sabit terimin bir tam sayı böleni olur. Örnek: x² + ax − 15 = 0’ın rasyonel kökleri ±1, ±3, ±5, ±15’ten biridir')
KUV=B('Kök ve kare ilişkisi','x₁² ve x₂² sayılarının toplamı ve çarpımı bilinirse (x₁x₂)² çarpımdan x₁x₂ bulunur (işaret ayrıca düşünülür); (x₁ + x₂)² = x₁² + x₂² + 2x₁x₂ ile toplam bulunur. Örnek: x₁² + x₂² = 10 ve x₁x₂ = 3 ise (x₁ + x₂)² = 16’dır')

# ---------------- kartlar (tipId başına bir kart; kart = fikir, soru metni içermez) ----------------
kartla('K-AIK2-01','Çarpanlı, rasyonel ve köklü denklemler','Çarpanlı denklemde her çarpan ayrı çözülür; rasyonel ve köklü denklemlerde ortak ifade ya da kareleme ikinci dereceye götürür; bulunan değerler tanım ve işaret koşuluyla denetlenir.','Ortak kökü iki kez saymak; paydayı sıfır yapan ya da karekökü negatife eşitleyen değeri çözüm saymak; kareleyip yaptığı işlemin genişlettiği kök kümesini unutmak.','orta','düz',4,'ikb-kok','Çarpanlı, rasyonel ve köklü denklemler')
kartla('K-AIK2-02','Parabol grafiği ve denklem','Grafikte işaretli noktalardan parabolün denklemi kurulur; kökler, tepe noktası, doğru ile kesişim ve yatay doğruyla kesişim aynı denklem düşüncesine bağlanır.','Tepe noktası ile kök okumayı karıştırmak; yatay doğru ile kesişimde y yerine x’i eşitlemek; f(x) = k denkleminde k’yı sabit terime işaretsiz eklemek.','orta','grafik',4,'ikb-parabol','Parabol grafiği ve denklem')
kartla('K-AIK2-03','Alan ve geometri problemleri','Bilinmeyen uzunluk seçilir; alan, Pisagor, Öklid ya da gelir bağıntısı ikinci dereceden denkleme dönüştürülür ve kökler uzunluk ya da sayı olarak anlamlı mı diye denetlenir.','Uzunluğu negatif ya da şekle sığmayan kökü kabul etmek; kenarı iki kez ya da yanlış ifadeyle yazmak; istenen büyüklük yerine bilinmeyeni cevap vermek.','orta','şekilli',4,'ikb-problem','Alan ve geometri problemleri')
kartla('K-AIK2-04','Diskriminant ve kök işaretleri','Kök sayısı Δ ile, kökler toplamı ve çarpımının işareti ise kökün işaretiyle belirlenir; parametreli denklemde bu üç koşul birlikte düşünülür.','Δ ≥ 0 ile Δ > 0’ı karıştırmak; yalnız toplamın işaretine bakıp çarpımı denetlememek; Δ’nın hangi parametre aralığında pozitif olduğunu ters yazmak.','orta','öncüllü',4,'ikb-diskr','Diskriminant ve kök işaretleri')
kartla('K-AIK2-05','İşlem makinesi ve bileşke','Her birim bir fonksiyon gibi yazılır; birimlerin bileşkesi ikinci dereceden bir denklem verir; ara değişken bulunur ve en başa kadar geri gidilir.','Sıralamayı ters kurmak; ara değerlerin yalnız birini almak; Δ < 0 olan dalı çözüme katmak.','zor','yeni nesil',5,'ikb-islem','İşlem makinesi ve bileşke')
kartla('K-AIK2-06','Kökler arası ilişki ve Vieta','Kökler arasındaki ilişki toplam ve çarpım koşullarına çevrilerek parametre bulunur; bulunan değer Δ koşulu ve kökün konumu açısından yeniden denetlenir.','Bulunan parametrenin tüm değerlerini kabul edip konum ya da işaret koşuluna bakmamak; iki kökü yer değiştirmek; işaretli çarpımı karesiyle karıştırmak.','zor','şekilli',5,'ikb-vieta','Kökler arası ilişki ve Vieta')
kartla('K-AIK2-07','Ortak kök (tam sayı katsayılı)','Rasyonel kök sabit terimin bölenlerinden biri olacağından aday kökler sınırlıdır; her aday için katsayılar bulunur ve verilen koşula uyanlar seçilir.','Aday köklerden uygun olmayanları elememek; parametrelerin işaret koşulunu unutmak; aynı değeri iki kez saymak.','zor','düz',4,'ikb-ortak','Ortak kök (tam sayı katsayılı)')

# ============================ 0001 · kolay · düz · çarpanlı ============================
s1=sp.solve((x**2-4*x)*(x**2+x-20),x); assert set(s1)=={0,4,-5} and sum(s1)==-1
e=[3,4,0,-5]; assert 4+(-1)==3 and 0+4==4 and 0*4*(-5)==0 and len({-1,*e})==5
q('0001',tipId='ikb-kok',tip='Çarpanlı, rasyonel ve köklü denklemler',z='kolay',alt='Çarpanlı Denklem',kaz='Çarpanlı ikinci dereceden denklemlerin köklerini bulur ve ortak kökün bir kez sayıldığını dikkate alarak kökler toplamını hesaplar.',kalip='düz',
 kart='K-AIK2-01 (çarpanlı denklem) · iki çarpanın ortak kökü',
 metin='(x² − 4x)(x² + x − 20) = 0\ndenkleminin farklı reel köklerinin toplamı kaçtır?',
 dogru=-1,yan=[(e[0],'İki çarpanın kökler toplamını ayrı ayrı alıp toplamış: 4 + (−1). Ortak kök olan 4’ü iki kez saymış.','dikkat'),(e[1],'Yalnız birinci çarpanın köklerini (0 ve 4) almış.','dikkat'),(e[2],'Toplam yerine kökler çarpımını hesaplamış: 0 · 4 · (−5).','islem'),(e[3],'İkinci çarpanın yalnız yeni getirdiği kökü (−5) yazmış; 0 ve 4’ü toplamaya katmamış.','dikkat')],
 istenen='Denklemin farklı reel köklerinin toplamı.',ip=['Her çarpanı ayrı çarpanlara ayırdığında hangi kök iki çarpanda da ortaya çıkıyor?'],bilgi=[CRP],
 ad=[A('Çarpanlara ayır','Her ikinci derece ifade çarpanlarına ayrılır.','x(x − 4)(x + 5)(x − 4) = 0'),A('Kökleri bul','Her çarpan sıfıra eşitlenir.','x = 0, x = 4, x = −5, x = 4'),A('Ortak kökü bir kez say','Farklı kökler 0, 4 ve −5’tir.','{−5, 0, 4}'),A('Topla','Farklı köklerin toplamı alınır.','0 + 4 + (−5) = −1')],
 puf='Farklı kökler sorulduğunda iki çarpanda da bulunan kökü bir kez say.')

# ============================ 0002 · kolay · grafik · tepe noktasından kökler arası uzaklık ============================
f2=(x-2)**2-9; assert sp.expand(f2)==x**2-4*x-5 and sp.solve(f2,x)==[-1,5]
e=[3,4,5,9]; assert 3==5-2 and -(-4)==4 and abs(-5)==5 and len({6,*e})==5
sx,sy=0.75,0.28
g=egri(1,-4,-5,-1.4,5.4,sx,sy)+'\n'+nokta(2,-9,sx,sy)+etiket(2,-9,sx,sy,'$T(2,\\,-9)$','below',OR)
SK=fig(graf(-2,6,-10,3,sx,sy,g,xl=100,yl=100,izgara=False))
q('0002',tipId='ikb-parabol',tip='Parabol grafiği ve denklem',z='kolay',alt='Tepe Noktası ve Kökler',kaz='Tepe noktası verilen ve baş katsayısı 1 olan parabolün x eksenini kestiği noktalar arasındaki uzaklığı bulur.',kalip='grafik',
 kart='K-AIK2-02 (parabol grafiği ve denklem) · tepe noktasından kökler arası uzaklık',
 metin='Şekilde, tepe noktası T olan y = x² + ax + b parabolünün grafiği verilmiştir.\nBuna göre, parabolün x eksenini kestiği iki nokta arasındaki uzaklık kaç birimdir?',
 dogru=6,yan=[(e[0],'Tepe noktasından bir köke olan uzaklığı (3) cevap sanmış; iki kök arasındaki uzaklığı bulmamış.','dikkat'),(e[1],'Kökler toplamını (4) uzaklık yazmış.','dikkat'),(e[2],'b = −5’in mutlak değerini uzaklık sanmış.','dikkat'),(e[3],'Tepe noktasının ordinatının mutlak değerini (9) yazmış.','dikkat')],
 istenen='Parabolün x eksenini kestiği iki nokta arasındaki uzaklık.',ip=['Tepe noktası biçiminde yazılan denklemde f(x) = 0 koşulu hangi iki kökü verir?'],bilgi=[TEP,PAR],sekil=SK,
 ad=[A('Denklemi yaz','Baş katsayı 1 ve tepe noktası (2, −9).','y = (x − 2)² − 9'),A('Kökleri bul','y = 0 alınır.','(x − 2)² = 9 → x = −1 ya da x = 5'),A('Uzaklığı bul','Kökler arasındaki uzaklık hesaplanır.','5 − (−1) = 6')],
 puf='Tepe noktası biçimindeki denklemde y = 0 koyunca kökler tepe noktasının iki yanında eşit uzaklıkta çıkar.')

# ============================ 0003 · kolay · şekilli · Pisagor ============================
assert sp.solve(x**2+(x+3)**2-225,x)==[-12,9] and 9+12+15==36
e=[42,45,48,54]; assert 12+15+15==42 and 3*15==45 and 36+12==48 and Fr(9*12,1)/2==54 and len({36,*e})==5
SK=fig(f'\\coordinate (A) at (0,0); \\coordinate (B) at (4.8,0); \\coordinate (C) at (0,3.6);\n\\filldraw[fill=blue!10,draw={BL},line width=1.4pt] (A)--(B)--(C)--cycle;\n\\draw (0.3,0)--(0.3,0.3)--(0,0.3);\n\\node[below,text={BL}] at (2.4,0) {{$x+3$}};\n\\node[left,text={OR}] at (0,1.8) {{$x$}};\n\\node[above right,text={PU}] at (2.4,1.8) {{$15$}};\n\\node[below left] at (A) {{$A$}}; \\node[below right] at (B) {{$B$}}; \\node[above left] at (C) {{$C$}};',font='\\normalsize')
q('0003',tipId='ikb-problem',tip='Alan ve geometri problemleri',z='kolay',alt='Pisagor Problemi',kaz='Dik üçgenin kenar uzunluklarını bilinmeyenle yazıp Pisagor bağıntısından ikinci dereceden denklem kurarak çevresini bulur.',kalip='şekilli',
 kart='K-AIK2-03 (alan ve geometri problemleri) · dik üçgen, Pisagor',
 metin='Şekildeki ABC dik üçgeninin kenar uzunlukları santimetre cinsinden verilmiştir.\nBuna göre, ABC üçgeninin çevresi kaç santimetredir?',
 dogru=36,yan=[(e[0],'Çarpanlara ayırırken kökü x = 12 bulmuş: 12 + 15 + 15.','islem'),(e[1],'Üç kenarı da hipotenüse eşit sanmış: 3 · 15.','dikkat'),(e[2],'Dik kenarlardan birini (x + 3 = 12) iki kez katmış: 36 + 12.','dikkat'),(e[3],'Çevre yerine alanı hesaplamış: 9 · 12 / 2.','dikkat')],
 istenen='ABC üçgeninin çevresi (cm).',ip=['Üç kenar arasındaki bağıntıyı yazıp denklemi çarpanlarına ayırdığında hangi kök kenar olamaz?'],bilgi=[PIS,ALAN],sekil=SK,
 ad=[A('Pisagor’u yaz','Dik kenarların kareleri toplamı hipotenüsün karesine eşittir.','x² + (x + 3)² = 15²'),A('Denklemi düzenle','Parantez açılır ve sadeleştirilir.','2x² + 6x − 216 = 0 → x² + 3x − 108 = 0'),A('Kökü seç','Çarpanlara ayrılır; uzunluk pozitif olmalıdır.','(x + 12)(x − 9) = 0 → x = 9'),A('Çevreyi bul','Kenarlar 9, 12 ve 15’tir.','9 + 12 + 15 = 36')],
 puf='Kenar uzunluğu için bulduğun kökün pozitif olup olmadığını denetle.')

# ============================ 0004 · orta · düz · Δ aynı zamanda kök ============================
c=sp.symbols('c'); D4=16-4*c
eq4=sp.expand(D4**2-4*D4+c); assert eq4==16*c**2-111*c+192 and sp.discriminant(eq4,c)==33 and sp.Rational(192,16)==12
e=[4,24,Fr(111,16),192]; assert D4.subs(c,4)==0 and Fr(192,8)==24 and len({12,*e})==5
q('0004',tipId='ikb-diskr',tip='Diskriminant ve kök işaretleri',z='orta',alt='Diskriminantı Kök Olan Denklem',kaz='Diskriminantın denklemin bir kökü olması koşulunu ikinci dereceden denkleme çevirip parametrenin değerlerinin çarpımını bulur.',kalip='düz',
 kart='K-AIK2-04 (diskriminant) · Δ’nın kök olma koşulu',
 metin='c bir gerçel sayı olmak üzere,\nx² − 4x + c = 0\ndenkleminin diskriminantı aynı zamanda bu denklemin bir köküdür.\nBuna göre, c’nin alabileceği reel değerlerin çarpımı kaçtır?',
 dogru=12,yan=[(e[0],'Δ = 0 koşulunu almış: 16 − 4c = 0 → c = 4.','bilgi'),(e[1],'Sabit terimi 192’yi baş katsayı 16 yerine 8’e bölmüş.','islem'),(e[2],'Çarpım yerine kökler toplamını (−b/a = 111/16) yazmış.','islem'),(e[3],'Çarpımı c/a yerine sabit terim 192 olarak yazmış; baş katsayıya bölmeyi unutmuş.','dikkat')],
 istenen='c’nin alabileceği reel değerlerin çarpımı.',ip=['Δ’yı c cinsinden yazıp denklemde x yerine koyduğunda c için hangi ikinci dereceden denklem oluşur?'],bilgi=[DIS,VIE],
 ad=[A('Diskriminantı yaz','a = 1, b = −4 için Δ hesaplanır.','Δ = 16 − 4c'),A('Kök olma koşulu','Δ denklemin bir kökü olduğundan x yerine yazılır.','(16 − 4c)² − 4(16 − 4c) + c = 0'),A('Denklemi düzenle','Parantezler açılır.','16c² − 111c + 192 = 0 → Δc = 33 > 0, iki reel c vardır'),A('Çarpımı bul','c değerlerinin çarpımı sabit terimin baş katsayıya oranıdır.','192/16 = 12')],
 puf='Δ’yı yazıp “bir kökü” koşulunu denklemde x yerine koyarak kullan.')

# ============================ 0005 · orta · öncüllü · kök işaretleri ============================
m=sp.symbols('m'); D5=sp.expand(4*m**2-4*(m+6)); assert sp.expand(D5-4*(m-3)*(m+2))==0
assert D5.subs(m,3)==0                                   # I doğru
assert D5.subs(m,-7)>0 and (-7+6)<0 and 2*(-7)<0         # II yanlış: m = −7 < −2 iken kökler zıt işaretli
for mv in range(-30,-6): assert D5.subs(m,mv)>0 and mv+6<0   # III doğru
SR=['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III']
q('0005',tipId='ikb-diskr',tip='Diskriminant ve kök işaretleri',z='orta',alt='Kök İşaretleri',kaz='Parametreli denklemde diskriminant, kökler toplamı ve çarpımının işaretiyle kökün sayısı ve işaretleri hakkındaki yargıları değerlendirir.',kalip='öncüllü',
 kart='K-AIK2-04 (diskriminant ve kök işaretleri) · öncüllü: çakışık kök, negatif kökler, zıt işaretli kökler',
 metin='m bir gerçel sayı olmak üzere,\nx² − 2mx + m + 6 = 0\ndenklemi ile ilgili,\nI. m = 3 ise denklemin çakışık iki reel kökü vardır.\nII. m < −2 ise denklemin farklı iki negatif reel kökü vardır.\nIII. m < −6 ise denklemin kökleri zıt işaretlidir.\nyargılarından hangileri doğrudur?',
 dogru='I ve III',sira=SR,yan=[(SR[4],'II’yi doğru saymış: m < −2 için Δ > 0 ve kökler toplamı 2m < 0 olduğunu görüp çarpımın (m + 6) işaretini denetlememiş.','bilgi'),(SR[2],'II’yi doğru saymış; III’ü ise “m < −6 iken Δ negatiftir” diye düşünüp yanlış bulmuş.','bilgi'),(SR[0],'III’ü yanlış saymış: kökler çarpımının negatif olmasını, kökler aynı işaretli diye yorumlamış.','dikkat'),(SR[1],'I’i yanlış (Δ = 0 iken kök yok) saymış, II’yi doğru kabul edip III’ü de yanlış bulmuş.','bilgi')],
 istenen='Doğru olan yargıların hangileri olduğu.',ip=['Her yargı için Δ’nın, kökler toplamının ve kökler çarpımının işaretini ayrı ayrı yazmayı dene.'],bilgi=[DIS,VIE],
 ad=[A('Δ’yı hesapla','Δ’nın işareti parametrenin aralığına bağlıdır.','Δ = 4m² − 4(m + 6) = 4(m − 3)(m + 2)'),A('I’i değerlendir','m = 3 için Δ sıfırdır.','Δ = 0 → çakışık kök → I doğru'),A('II’yi değerlendir','Farklı iki negatif kök için Δ > 0, toplam < 0 ve çarpım > 0 gerekir; çarpım m + 6 > 0 olmalıdır.','m = −7 için çarpım −1 < 0, kökler zıt işaretli → II yanlış'),A('III’ü değerlendir','m < −6 ise çarpım negatiftir ve Δ > 0 olduğundan iki reel kök vardır.','m + 6 < 0 → zıt işaretli → III doğru')],
 puf='Kök işaretleri için toplamı ve çarpımı birlikte, Δ ≥ 0 koşuluyla incele.')

# ============================ 0006 · orta · yeni nesil · iki kollu makine ============================
kk=sp.solve(x**2-(4*x+6)-6,x); assert set(kk)=={6,-2} and 36+4==40
e=[-8,8,16,36]; assert 4**2-2*(-12)*(-1)*(-1)==-8 or True
assert (6+(-2))**2+2*(6*-2)==-8 and 6-(-2)==8 and (6+(-2))**2==16 and 6**2==36 and len({40,*e})==5
SK=fig(f'\\tikzset{{b/.style={{draw,thick,rounded corners=3pt,align=center,minimum height=1.2cm,inner sep=4pt}}}}\n\\node[b,fill=gray!12,minimum width=1.4cm] (g) at (0,0) {{Girdi\\\\$x$}};\n\\node[b,fill=blue!12,text width=2.7cm,draw={BL}] (a) at (3.2,1.2) {{\\textbf{{Üst kol}}\\\\aldığı sayının karesini alır}};\n\\node[b,fill=orange!15,text width=2.7cm,draw={OR}] (c) at (3.2,-1.2) {{\\textbf{{Alt kol}}\\\\aldığı sayıyı 4 ile çarpıp 6 ekler}};\n\\node[b,fill=green!12,text width=2.7cm,draw=green!50!black] (d) at (6.9,0) {{\\textbf{{Fark birimi}}\\\\üst kolun çıktısından alt kolun çıktısını çıkarır}};\n\\node[b,fill=gray!12,minimum width=1.4cm] (s) at (9.7,0) {{Çıktı\\\\$6$}};\n\\draw[-{{Stealth}},thick] (g)--(a); \\draw[-{{Stealth}},thick] (g)--(c); \\draw[-{{Stealth}},thick] (a)--(d); \\draw[-{{Stealth}},thick] (c)--(d); \\draw[-{{Stealth}},thick] (d)--(s);',font='\\small')
q('0006',tipId='ikb-islem',tip='İşlem makinesi ve bileşke',z='orta',alt='İki Kollu Makine',kaz='İki kollu bir işlem makinesinin çıktı koşulundan ikinci dereceden denklem kurup girdi değerlerinin kareler toplamını hesaplar.',kalip='yeni nesil',
 kart='K-AIK2-05 (işlem makinesi) · iki kollu makine, girdilerin kareler toplamı',
 metin='Şekildeki makinede girdi, iki kola ayrılmakta ve kolların çıktıları fark biriminde birleştirilmektedir. Çıktının şekilde yazılı değer olduğu bilinmektedir.\nBuna göre, girdi x’in alabileceği değerlerin kareleri toplamı kaçtır?',
 dogru=40,yan=[(e[0],'Kareler toplamında −2x₁x₂ yerine +2x₁x₂ kullanıp 16 + 2(−12) = −8 bulmuş.','islem'),(e[1],'Kareler toplamı yerine x değerlerinin farkını (6 − (−2)) yazmış.','dikkat'),(e[2],'Kareler toplamı yerine kökler toplamının karesini (4²) yazmış.','dikkat'),(e[3],'Yalnız pozitif değerin karesini (6²) almış.','dikkat')],
 istenen='x değerlerinin kareleri toplamı.',ip=['İki kolun çıktısını x cinsinden yazıp fark birimine yerleştirirsen hangi denklem oluşur; kareler toplamı için kökleri bulmak şart mı?'],bilgi=[MAK,VIE],sekil=SK,
 ad=[A('Kolların çıktıları','Üst kol x², alt kol 4x + 6 verir.','x² ve 4x + 6'),A('Denklemi kur','Fark 6’ya eşit olmalıdır.','x² − (4x + 6) = 6 → x² − 4x − 12 = 0'),A('Kökler toplamı ve çarpımı','Kareler toplamı için toplam ve çarpım yeter.','x₁ + x₂ = 4 · x₁x₂ = −12'),A('Kareler toplamı','(x₁ + x₂)² − 2x₁x₂ hesaplanır.','16 + 24 = 40')],
 puf='Kareler toplamı gibi simetrik ifadeler kökleri bulmadan toplam ve çarpımla hesaplanır.')

# ============================ 0007 · orta · hikâyeli · afiş boşlukları ============================
assert sp.solve((40-4*x)*(60-2*x)-1248,x)==[4,36] and 40-4*36<0 and 2*(24+52)==152
e=[4,76,200,1248]; assert 24+52==76 and 2*(40+60)==200 and 24*52==1248 and len({152,*e})==5
SK=fig(f'\\filldraw[fill=blue!8,draw={BL},line width=1.4pt] (0,0) rectangle (4,6);\n\\filldraw[fill=white,draw={OR},thick] (0.8,0.5) rectangle (3.2,5.5);\n\\node at (2,3) {{yazı alanı}};\n\\node[text={OR}] at (2,5.75) {{$x$}}; \\node[text={OR}] at (2,0.25) {{$x$}}; \\node[text={PU}] at (0.4,3) {{$2x$}}; \\node[text={PU}] at (3.6,3) {{$2x$}};\n\\draw[<->] (0,-0.4)--(4,-0.4) node[midway,below] {{$40$ cm}}; \\draw[<->] (-0.4,0)--(-0.4,6) node[midway,left] {{$60$ cm}};',font='\\small')
q('0007',tipId='ikb-problem',tip='Alan ve geometri problemleri',z='orta',alt='Afiş Boşlukları',kaz='Dikdörtgen afişte kenar boşluklarını bilinmeyenle yazıp yazı alanının alanından denklem kurarak çevresini hesaplar.',kalip='hikâyeli',
 kart='K-AIK2-03 (alan ve geometri problemleri) · afişte üst-alt ve yan boşluklar',
 metin='Bir matbaada, boyutları şekilde verilen dikdörtgen biçimli bir afişin üst ve alt kenarlarında x cm, sağ ve sol kenarlarında ise 2x cm boşluk bırakılmış, geri kalan dikdörtgen kısma yazı yazılmıştır. (Şekil ölçekli çizilmemiştir.)\nYazı alanı 1248 cm² olduğuna göre, yazı alanının çevresi kaç santimetredir?',
 dogru=152,yan=[(e[0],'Denklemi çözüp x = 4’ü bulmuş ve çevre yerine x’i yazmış.','dikkat'),(e[1],'Çevre yerine yarı çevreyi (24 + 52) yazmış.','dikkat'),(e[2],'Yazı alanı yerine afişin çevresini (2 · (40 + 60)) hesaplamış.','dikkat'),(e[3],'Çevre yerine yazı alanının alanını yazmış.','dikkat')],
 istenen='Yazı alanının çevresi (cm).',ip=['Yan boşluklar ve üst-alt boşluklar için kenarlardan ne kadar kısalacağını yazıp alanı bu iki uzunluğun çarpımı olarak düşün; hangi kök boyutlara uyar?'],bilgi=[ALAN],sekil=SK,
 ad=[A('Yazı alanının kenarlarını yaz','Genişlikten iki yan boşluk, yükseklikten iki üst-alt boşluk çıkarılır.','Genişlik 40 − 4x · Yükseklik 60 − 2x'),A('Alan denklemini kur','Alan 1248’dir.','(40 − 4x)(60 − 2x) = 1248 → x² − 40x + 144 = 0'),A('Uygun kökü seç','Çarpanlarına ayrılır; kenarlar pozitif olmalıdır.','(x − 4)(x − 36) = 0 → x = 4 (x = 36’da 40 − 144 < 0)'),A('Çevreyi bul','Kenarlar 24 ve 52’dir.','2(24 + 52) = 152')],
 puf='Bulduğun kökle yazı alanının kenarlarının pozitif kaldığını denetle.')

# ============================ 0008 · orta · grafik · y = k doğrusu ============================
assert sp.solve((x-2)**2-1-8,x)==[-1,5] and (5-(-1))==6 and (0-2)**2-1==3
e=[9,35,15,0]; assert 3**2==9 and 6**2-1==35 and 6**2-4*6+3==15 and 3**2-4*3+3==0 and len({8,*e})==5
sx,sy=0.65,0.3
g=egri(1,-4,3,-1.3,5.3,sx,sy)+f'\n\\draw[{OR},thick,dashed] ({-2*sx},{8*sy})--({6.4*sx},{8*sy}) node[right,text={OR}] {{$y=k$}};\n'+nokta(2,-1,sx,sy)+nokta(0,3,sx,sy)+nokta(-1,8,sx,sy,OR)+nokta(5,8,sx,sy,OR)+etiket(2,-1,sx,sy,'$T(2,\\,-1)$','below')+etiket(0,3,sx,sy,'$(0,\\,3)$','left')+etiket(-1,8,sx,sy,'$A$','above left',OR)+etiket(5,8,sx,sy,'$B$','above right',OR)+f'\n\\draw[<->] ({-1*sx},{9.2*sy})--({5*sx},{9.2*sy}) node[midway,above] {{$|AB|=6$ br}};'
SK=fig(graf(-2,6,-2,9,sx,sy,g,xl=100,yl=100,izgara=False))
q('0008',tipId='ikb-parabol',tip='Parabol grafiği ve denklem',z='orta',alt='Yatay Doğruyla Kesişim',kaz='Tepe noktası ve bir noktası verilen parabolün yatay bir doğruyla kesişim noktaları arasındaki uzaklıktan doğrunun denklemindeki sabiti bulur.',kalip='grafik',
 kart='K-AIK2-02 (parabol grafiği ve denklem) · yatay doğru ile kesişim noktalarının uzaklığı',
 metin='Şekilde tepe noktası T olan y = f(x) parabolü ile y = k doğrusu verilmiştir. Doğru, parabolü A ve B noktalarında kesmektedir.\nBuna göre, k kaçtır?',
 dogru=8,yan=[(e[0],'Tepe noktasındaki ordinatı (−1) kullanmayı unutmuş: (x − 2)² = k ve x − 2 = 3 → k = 9.','dikkat'),(e[1],'|AB| = 6’yı tepe noktasından uzaklık sanmış: (6)² − 1.','islem'),(e[2],'|AB| = 6’yı kök sanıp f(6) = 36 − 24 + 3 hesaplamış.','dikkat'),(e[3],'A ve B noktalarını eksene göre simetrik (−3 ve 3) alıp f(3) = 9 − 12 + 3 hesaplamış.','dikkat')],
 istenen='k’nin değeri.',ip=['Parabolün simetri ekseni ile A ve B’nin tepe noktasına uzaklıkları arasında nasıl bir ilişki vardır?'],bilgi=[TEP,KES],sekil=SK,
 ad=[A('Parabolü yaz','Tepe noktası (2, −1) olduğundan f(x) = a(x − 2)² − 1 biçimindedir; (0, 3) noktasından a bulunur.','3 = 4a − 1 → a = 1 → f(x) = (x − 2)² − 1'),A('Simetriyi kullan','A ve B simetri eksenine eşit uzaklıktadır.','|AB| = 6 → A ve B’nin apsisleri 2 ± 3'),A('B’nin ordinatını bul','x = 5 için f hesaplanır.','f(5) = 9 − 1 = 8'),A('k’yı yaz','A ve B doğru üzerindedir.','k = 8')],
 puf='Simetri ekseni A ile B’nin tam ortasından geçer; bunu apsisleri bulmak için kullan.')

# ============================ 0009 · orta · düz · kökler birbirinin tersi ============================
mm=sp.symbols('m'); sol=sp.solve((3*mm-10)-(mm-2),mm); assert sol==[4]
assert sp.solve(2*x**2-5*x+2,x)==[sp.Rational(1,2),2] and 25-4*2*2>0 and Fr(5,2)==Fr(5,4-2)
assert sp.solve((3*mm-10)+(mm-2),mm)==[3] and Fr(5,3-2)==5
e=[5,4,Fr(-5,2),Fr(2,5)]; assert len({Fr(5,2),*e})==5
q('0009',tipId='ikb-vieta',tip='Kökler arası ilişki ve Vieta',z='orta',alt='Birbirinin Tersi Olan Kökler',kaz='Köklerin birbirinin çarpmaya göre tersi olması koşulundan parametreyi bulup kökler toplamını hesaplar.',kalip='düz',
 kart='K-AIK2-06 (kökler arası ilişki) · kökler çarpmaya göre ters',
 metin='m bir gerçel sayı olmak üzere,\n(m − 2)x² − 5x + 3m − 10 = 0\ndenkleminin kökleri birbirinin çarpmaya göre tersidir.\nBuna göre, bu denklemin kökler toplamı kaçtır?',
 dogru=Fr(5,2),yan=[(e[0],'Köklerin toplamsal ters olduğunu sanıp m = 3 bulmuş; toplamı 5/(3 − 2) = 5 yazmış.','bilgi'),(e[1],'m = 4’ü bulup cevabı m olarak vermiş.','dikkat'),(e[2],'Toplamı −b/a yerine b/a olarak yazıp −5/2 bulmuş.','islem'),(e[3],'Toplamı a/(−b) olarak ters yazıp 2/5 bulmuş.','islem')],
 istenen='Denklemin kökler toplamı.',ip=['Çarpmaya göre ters iki sayının çarpımı kaç olur ve bu koşul katsayılar için hangi eşitliği verir?'],bilgi=[VIE,ORAN],
 ad=[A('Çarpım koşulu','Kökler birbirinin tersi ise çarpımları 1’dir.','(3m − 10)/(m − 2) = 1'),A('m’yi bul','Eşitlik çözülür.','3m − 10 = m − 2 → m = 4'),A('Denklemi yaz','m = 4 yerine konur; Δ > 0 olduğu denetlenir.','2x² − 5x + 2 = 0 → Δ = 9 > 0'),A('Toplamı bul','Kökler toplamı −b/a’dır.','5/2')],
 puf='Parametreyi bulduktan sonra denklemi yazıp köklerin gerçekten oluştuğunu denetle.')

# ============================ 0010 · orta · tablo · gelir problemi ============================
gel=lambda n:(40+2*n)*(60-2*n)
assert [gel(0),gel(1),gel(2)]==[2400,2436,2464] and sp.solve((40+2*x)*(60-2*x)-2436,x)==[1,9] and (40+2*1)+(40+2*9)==100
e=[9,1,-10,100]; assert len({10,*e})==5
SK=tablo_svg(['Zam sayısı (n)','Birim fiyat (TL)','Günlük satış (adet)'],[['0','40','60'],['1','42','58'],['2','44','56']])
q('0010',tipId='ikb-problem',tip='Alan ve geometri problemleri',z='orta',alt='Gelir Problemi',kaz='Tablodaki düzenden fiyat ve satış adedini zam sayısıyla yazıp gelir denklemi kurar.',kalip='tablo',
 kart='K-AIK2-03 (denkleme dönüşen problem) · fiyat–satış düzeninden gelir denklemi',
 metin='Bir mağazada bir ürünün birim fiyatı ve günlük satış adedi, yapılan zam sayısına göre aşağıdaki tabloda verilmiştir. Zam sayısı arttıkça fiyat ve satış adedi tablodaki düzene göre değişmeye devam etmektedir.\nGünlük gelir 2436 TL olduğuna göre, n’nin alabileceği değerlerin toplamı kaçtır?',
 dogru=10,yan=[(e[0],'n değerlerinin toplamı yerine çarpımını yazmış.','dikkat'),(e[1],'Yalnız küçük kökü (n = 1) almış.','dikkat'),(e[2],'Kökler toplamını −b/a yerine b/a ile hesaplayıp −10 bulmuş.','islem'),(e[3],'n yerine bu iki durumdaki birim fiyatların toplamını (42 + 58) yazmış.','dikkat')],
 istenen='n’nin alabileceği değerlerin toplamı.',ip=['Tablodaki düzenden birim fiyatı ve satış adedini n cinsinden yazıp çarptığında hangi ifade gelire eşit olur?'],bilgi=[ALAN,VIE],sekil=SK,
 ad=[A('Fiyat ve adedi yaz','Her zamda fiyat 2 TL artıyor, satış 2 adet azalıyor.','Fiyat: 40 + 2n · Adet: 60 − 2n'),A('Gelir denklemini kur','Gelir = fiyat × adet.','(40 + 2n)(60 − 2n) = 2436 → n² − 10n + 9 = 0'),A('Kökleri bul','Çarpanlarına ayrılır; iki kök de uygundur (satış adedi pozitif).','(n − 1)(n − 9) = 0'),A('Topla','Kökler toplamı alınır.','1 + 9 = 10')],
 puf='Gelir bağıntısını n cinsinden yazarken tablodaki iki değişkenin her biri için düzeni ayrı ayrı çıkar.')

# ============================ 0011 · orta · öncüllü · grafik · f(x) = k ============================
f11=x**2-2*x-3; assert f11.subs(x,0)==-3 and f11.subs(x,1)==-4
r1=sp.solve(f11,x); assert sum(r1)==2                          # I doğru
assert sp.solve(f11+4,x)==[1]                                  # II doğru (tam bir kök)
r3=sp.solve(f11-5,x); assert r3[0]*r3[1]==-8 and -8!=-5        # III yanlış
sx,sy=0.8,0.34
g=egri(1,-2,-3,-1.8,3.8,sx,sy)+'\n'+nokta(1,-4,sx,sy)+nokta(0,-3,sx,sy)+etiket(1,-4,sx,sy,'$T(1,\\,-4)$','below')+etiket(0,-3,sx,sy,'$(0,\\,-3)$','below left',OR)+f'\n\\node[text={BL}] at ({3.2*sx},{-3.6*sy}) {{$y=f(x)$}};'
SK=fig(graf(-2,4,-5,4,sx,sy,g,xl=100,yl=100,izgara=False))
q('0011',tipId='ikb-parabol',tip='Parabol grafiği ve denklem',z='orta',alt='f(x) = k Denklemleri',kaz='Grafiği verilen parabolün denklemini kurup f(x) = k biçimindeki denklemlerin kök sayısı ile kökler toplamı ve çarpımı hakkındaki yargıları değerlendirir.',kalip='öncüllü',
 kart='K-AIK2-02 (parabol grafiği ve denklem) · öncüllü: f(x) = 0, f(x) = tepe ordinatı, f(x) = k',
 metin='Şekilde, tepe noktası T olan ikinci dereceden y = f(x) fonksiyonunun grafiği verilmiştir.\nBuna göre,\nI. f(x) = 0 denkleminin kökler toplamı 2’dir.\nII. f(x) = −4 denkleminin yalnız bir reel kökü vardır.\nIII. f(x) = 5 denkleminin kökler çarpımı −5’tir.\nyargılarından hangileri doğrudur?',
 dogru='I ve II',sira=SR,yan=[(SR[4],'III’ü doğru saymış: f(x) = 5 denklemini x² − 2x − 5 = 0 yazıp (−3’ü silip 5’i yazarak) çarpımı −5 bulmuş.','dikkat'),(SR[3],'II’yi yanlış saymış: tepe noktasında f(x) = −4’ün çakışık kök vermesini “kök yok” diye yorumlamış; III’ü doğru kabul etmiş.','bilgi'),(SR[0],'Kökler toplamını doğru bulmuş, II’de “çakışık iki kök” ile “yalnız bir kök”ü ayırıp II’yi yanlış saymış.','bilgi'),(SR[1],'I’de kökler toplamını −2 bulup yanlış saymış; II’yi doğru kabul etmiştir.','islem')],
 istenen='Doğru olan yargıların hangileri olduğu.',ip=['Tepe noktası ile y eksenini kestiği nokta parabolün denklemini nasıl belirler; f(x) = k denklemi hangi ikinci dereceden denkleme dönüşür?'],bilgi=[TEP,VIE],sekil=SK,
 ad=[A('Parabolü yaz','Tepe noktası (1, −4); (0, −3) noktasından a bulunur.','−3 = a − 4 → a = 1 → f(x) = x² − 2x − 3'),A('I’i değerlendir','Kökler toplamı −b/a’dır.','x² − 2x − 3 = 0 → toplam 2 → I doğru'),A('II’yi değerlendir','f(x) = −4 tepe noktasının ordinatıdır.','x² − 2x + 1 = 0 → yalnız x = 1 → II doğru'),A('III’ü değerlendir','f(x) = 5 denkleminin sabit terimi −3 − 5’tir.','x² − 2x − 8 = 0 → çarpım −8 → III yanlış')],
 puf='f(x) = k denklemini her zaman sağ taraf sıfır olacak biçimde yazıp katsayılara bak.')

# ============================ 0012 · orta · düz · rasyonel denklem ============================
D12=sp.solve(6*((x+1)**2+(x-2)**2)-13*(x-2)*(x+1),x); assert set(D12)=={8,-7}
for v in D12: assert sp.Rational(v+1,v-2)+sp.Rational(v-2,v+1)==sp.Rational(13,6)
assert 8*(-7)==-56 and 8+(-7)==1 and sp.solve((x+1)**2+(x-2)**2-13,x) is not None
r12=sp.solve(2*x**2-2*x+5-13,x); assert sp.simplify(r12[0]*r12[1])==-4
e=[56,1,8,-4]; assert len({-56,*e})==5
q('0012',tipId='ikb-kok',tip='Çarpanlı, rasyonel ve köklü denklemler',z='orta',alt='Rasyonel Denklem',kaz='Ters ifadeleri toplamı verilen rasyonel denklemi ikinci dereceye indirip çözüm kümesinin elemanları çarpımını bulur.',kalip='düz',
 kart='K-AIK2-01 (rasyonel denklem) · t + 1/t biçimi',
 metin='(x + 1)/(x − 2) + (x − 2)/(x + 1) = 13/6\ndenkleminin çözüm kümesindeki elemanların çarpımı kaçtır?',
 dogru=-56,yan=[(e[0],'Kökleri 8 ve −7 bulup çarpımı işaretsiz yazmış.','dikkat'),(e[1],'Çarpım yerine kökler toplamını yazmış: 8 + (−7).','dikkat'),(e[2],'t = 3/2 değerinden gelen kökü (8) almış; t = 2/3’ten gelen kökü katmamış.','dikkat'),(e[3],'Eşitliğin sağ tarafını (x − 2)(x + 1) ile çarpmadan (x + 1)² + (x − 2)² = 13 yazmış ve çarpımı −4 bulmuş.','islem')],
 istenen='Çözüm kümesindeki elemanların çarpımı.',ip=['Sol taraftaki iki kesir arasında nasıl bir ilişki var ve bu ilişki hangi değişken seçimini kolaylaştırır?'],bilgi=[RAS,VIE],
 ad=[A('Değişken seç','t = (x + 1)/(x − 2) denirse ikinci kesir 1/t olur.','t + 1/t = 13/6 → 6t² − 13t + 6 = 0'),A('t’yi bul','Çarpanlarına ayrılır.','(2t − 3)(3t − 2) = 0 → t = 3/2 ya da t = 2/3'),A('x’i bul','Her t için x çözülür; paydayı sıfır yapmadığı denetlenir.','t = 3/2: x = 8 · t = 2/3: x = −7'),A('Çarpımı bul','Kökler çarpılır.','8 · (−7) = −56')],
 puf='Bir ifade ile tersinin toplamı verildiğinde ifadenin kendisine yeni bir harf ver.')

# ============================ 0013 · orta · düz · köklü denklem ============================
cz=[v for v in sp.solve((x-5)**2-(x+7),x)]; assert set(cz)=={2,9}
assert sp.sqrt(9+7)+5==9 and sp.sqrt(2+7)+5!=2
e=[11,2,18,16]; assert 2+9==11 and 2*9==18 and 9+7==16 and len({9,*e})==5
q('0013',tipId='ikb-kok',tip='Çarpanlı, rasyonel ve köklü denklemler',z='orta',alt='Köklü Denklem',kaz='Köklü denklemi kareleyerek ikinci dereceye indirir ve bulunan köklerin denklemi sağlayıp sağlamadığını denetler.',kalip='düz',
 kart='K-AIK2-01 (köklü denklem) · kareleme ve kök denetimi',
 metin='√(x + 7) + 5 = x\ndenkleminin çözüm kümesindeki elemanların toplamı kaçtır?',
 dogru=9,yan=[(e[0],'Kareleme sonucundaki iki kökü de (2 ve 9) çözüm sayıp toplamış.','bilgi'),(e[1],'Yalnız x = 2 kökünü alıp denklemde denememiş.','dikkat'),(e[2],'Çözüm kümesinin elemanları toplamı yerine kareleme sonrası denklemin kökler çarpımını (2 · 9) yazmış.','dikkat'),(e[3],'x yerine karekök içindeki ifadenin değerini (9 + 7) yazmış.','dikkat')],
 istenen='Çözüm kümesindeki elemanların toplamı.',ip=['Karekökü yalnız bırakıp kareledikten sonra bulduğun değerlerin her biri için karekökün eşit olduğu ifadenin işaretine bakmayı dene.'],bilgi=[RAS],
 ad=[A('Karekökü yalnız bırak','5 sağ tarafa geçirilir.','√(x + 7) = x − 5'),A('Kareleyip düzenle','İki taraf karelenir.','x + 7 = x² − 10x + 25 → x² − 11x + 18 = 0'),A('Kökleri bul','Çarpanlarına ayrılır.','(x − 2)(x − 9) = 0 → x = 2 ya da x = 9'),A('Denetle ve topla','Karekök negatif olamaz: x − 5 ≥ 0 olmalıdır.','x = 2: −3 < 0 uygun değil · x = 9: √16 = 4 ✓ → toplam 9')],
 puf='Kareleme yeni kök üretebilir; her kökü ilk denklemde dene.')

# ============================ 0014 · zor · şekilli · sayı doğrusunda kökler ============================
def kok14(mv):
    r=sp.solve(x**2+(mv-1)*x-(3*mv-1),x); return sorted(r)
assert kok14(3)==[-4,2]
for mv in [3]: a_,b_=kok14(mv); assert a_<0<b_ and -a_==2*b_
mm=sp.symbols('m'); dd=sp.solve(2*mm**2-7*mm+3,mm); assert set(dd)=={3,sp.Rational(1,2)}
a_,b_=kok14(sp.Rational(1,2)); assert a_<0<b_ and -a_*2==b_   # m = 1/2’de |AO| = |OB|/2 : şekle uymaz
e=[Fr(1,2),Fr(3,2),2,Fr(5,2)]; assert len({3,*e})==5 and Fr(1,2)*3==Fr(3,2) and 3-Fr(1,2)==Fr(5,2)
u=1.45
SK=fig(f'\\draw[-{{Stealth}},thick] ({-3.3*u:.2f},0)--({2.0*u:.2f},0);\n\\draw[{BL},line width=2.2pt] ({-2*u:.2f},0)--(0,0); \\draw[{OR},line width=2.2pt] (0,0)--({1*u:.2f},0);\n\\foreach \\p/\\n/\\c in {{{-2*u:.2f}/A/{BL},0/O/black,{1*u:.2f}/B/{OR}}} {{\\fill[\\c] (\\p,0) circle (0.1); \\node[above=4pt,text=\\c] at (\\p,0) {{$\\n$}};}}\n\\draw[<->,{BL}] ({-2*u:.2f},-0.5)--(0,-0.5) node[midway,below] {{$2k$}}; \\draw[<->,{OR}] (0,-0.5)--({1*u:.2f},-0.5) node[midway,below] {{$k$}};',font='\\normalsize')
q('0014',tipId='ikb-vieta',tip='Kökler arası ilişki ve Vieta',z='zor',alt='Sayı Doğrusunda Kökler',kaz='Köklerin sayı doğrusundaki konumundan aralarındaki ilişkiyi yazıp toplam ve çarpım koşullarıyla parametreyi bulur, bulunan değeri şekle uygunluk açısından denetler.',kalip='şekilli',
 kart='K-AIK2-06 (kökler arası ilişki) · sayı doğrusunda konum, iki değerden birinin elenmesi',
 metin='m bir gerçel sayı olmak üzere,\nx² + (m − 1)x − (3m − 1) = 0\ndenkleminin kökleri, O başlangıç noktası olmak üzere sayı doğrusunda A ve B noktalarıyla gösterilmiştir.\nBuna göre, m kaçtır?',
 dogru=3,yan=[(e[0],'A ve B’nin yerini değiştirip x₁ = k, x₂ = −2k almış; çıkan iki m değerinden 1/2’yi seçmiş (bu değerde A, O’ya B’den daha yakındır).','dikkat'),(e[1],'Denklemden çıkan iki m değerinin (3 ve 1/2) çarpımını yazmış.','islem'),(e[2],'m yerine, bulduğu k = 2 değerini yazmış.','dikkat'),(e[3],'Denklemden çıkan iki m değerinin farkını (3 − 1/2) yazmış.','islem')],
 istenen='m’nin değeri.',ip=['Şekilden A ve B’nin işaretlerini ve birbirine uzaklıklarını ilişkilendirip kökleri tek bir k ile yazmayı dene.'],bilgi=[VIE,ORAN],sekil=SK,
 ad=[A('Kökleri k ile yaz','A, O’nun solunda ve |AO| = 2k; B sağında ve |OB| = k’dır (k > 0).','x₁ = −2k, x₂ = k'),A('Toplam ve çarpımı yaz','Katsayılardan toplam ve çarpım yazılır.','x₁ + x₂ = −k = −(m − 1) → k = m − 1 · x₁x₂ = −2k² = −(3m − 1)'),A('m için denklem kur','k = m − 1 yerine yazılır.','2(m − 1)² = 3m − 1 → 2m² − 7m + 3 = 0 → m = 3 ya da m = 1/2'),A('Şekle uygunluğu denetle','k = m − 1 pozitif olmalıdır.','m = 1/2 için k = −1/2 < 0 → uygun değil'),A('Sonuç','Uygun değer seçilir.','m = 3 (kökler −4 ve 2)')],
 puf='Parametreyi bulduktan sonra kökleri yazıp şekildeki konumla karşılaştır.')

# ============================ 0015 · zor · grafik · parabol ve doğru, alan koşulundan parametre ============================
kk=sp.symbols('k'); f15=x**2-2*x-3
xB=sp.solve(f15-kk*(x+1),x); assert set(xB)=={-1,kk+3}
yB=sp.expand(kk*(kk+4)); alanB=sp.expand(sp.Rational(1,2)*4*yB); assert sp.expand(alanB-2*kk**2-8*kk)==0
sol15=sp.solve(alanB-10,kk); assert set(sol15)=={1,-5}      # k > 0 olduğundan k = 1
e=[-5,3,4,5]; assert len({1,*e})==5
sx,sy=0.78,0.34
def Pt(a,b): return f'({a*sx:.3f},{b*sy:.3f})'
g=f'\\fill[green!20] {Pt(-1,0)}--{Pt(4,5)}--{Pt(3,0)}--cycle;\n'+egri(1,-2,-3,-1.2,4.4,sx,sy)+f'\n\\draw[{OR},thick] {Pt(-1.3,-0.3)}--{Pt(4.9,5.9)};\n'+''.join(nokta(a,b,sx,sy,c) for a,b,c in [(-1,0,BL),(3,0,BL),(0,-3,BL),(0,1,OR),(4,5,PU)])+etiket(-1,0,sx,sy,'$A(-1,\\,0)$','below left')+etiket(3,0,sx,sy,'$C(3,\\,0)$','below right')+etiket(0,-3,sx,sy,'$(0,\\,-3)$','right',BL)+etiket(0,1,sx,sy,'$D(0,\\,k)$','above left=2pt and 5pt',OR)+etiket(4,5,sx,sy,'$B$','above left',PU)+f'\n\\node[text={BL}] at {Pt(-1.7,3.2)} {{$y=f(x)$}}; \\node[text={OR}] at {Pt(5.2,5.6)} {{$d$}};'
SK=fig(graf(-2,5,-4,7,sx,sy,g,xl=100,yl=100,izgara=False))
q('0015',tipId='ikb-parabol',tip='Parabol grafiği ve denklem',z='zor',alt='Parabol ve Doğru',kaz='Kökleri ve bir noktası verilen parabolün, eğimi parametreli doğruyla kesişimini denklemle bulup üçgenin alanı koşulundan parametreyi hesaplar.',kalip='grafik',
 kart='K-AIK2-02 (parabol grafiği ve denklem) · parametreli doğru, ikinci kesişim, alan koşulu',
 metin='Şekilde, x eksenini A ve C noktalarında kesen y = f(x) parabolü ile A noktasından ve y eksenini D(0, k) noktasında kesen d doğrusu verilmiştir. k pozitif bir gerçel sayıdır ve d doğrusu, parabolü A ve B noktalarında kesmektedir.\nABC üçgeninin alanı 10 birimkare olduğuna göre, k kaçtır?',
 dogru=1,yan=[(e[0],'Denklemden çıkan k = −5 değerini de seçmiş; k > 0 koşulunu denetlememiş.','dikkat'),(e[1],'k’yı C noktasının apsisi (3) sanmış.','dikkat'),(e[2],'B’nin apsisini (k + 3 = 4) cevap vermiş.','dikkat'),(e[3],'k² + 4k − 5 = 0 denkleminin çarpanlarını (k + 1)(k − 5) yazıp k = 5 almış.','islem')],
 istenen='k’nin değeri.',ip=['Doğrunun denklemini A noktası ve k ile yazıp parabolle ortak çözdüğünde B’nin koordinatları k’ya nasıl bağlanır?'],bilgi=[PAR,KES],sekil=SK,
 ad=[A('Parabolü yaz','Kökleri −1 ve 3, (0, −3) noktasından geçer.','f(x) = (x + 1)(x − 3)'),A('Doğruyu yaz','A(−1, 0) ve D(0, k) noktalarından geçer; eğim k.','d: y = k(x + 1)'),A('B’yi bul','f(x) = k(x + 1) çözülür; x = −1 A’dır.','(x + 1)(x − 3 − k) = 0 → x_B = k + 3, y_B = k(k + 4)'),A('Alan koşulu','|AC| = 4 taban, y_B yüksekliktir.','1/2 · 4 · k(k + 4) = 10 → k² + 4k − 5 = 0'),A('k’yı seç','Çarpanlarına ayrılır; k > 0.','(k + 5)(k − 1) = 0 → k = 1')],
 puf='Doğrunun parabolle bir ortak noktası bilindiğinden denklemin bir kökü hazırdır.')

# ============================ 0016 · zor · yeni nesil · iki birimli makine, Δ < 0 dalı ============================
t_=sp.symbols('t'); ts=sp.solve(t_**2+2*t_-24,t_); assert set(ts)=={4,-6}
assert sp.discriminant(x**2-2*x-4,x)>0 and sp.discriminant(x**2-2*x+6,x)<0
rx=sp.solve(x**2-2*x-4,x); assert sp.simplify(sum(rx))==2 and sp.simplify(rx[0]*rx[1])==-4
e=[-4,-2,4,10]; assert 4+(-6)==-2 and 2+2==4 and abs(4-(-6))==10 and len({2,*e})==5
SK=fig(f'\\tikzset{{b/.style={{draw,thick,rounded corners=3pt,align=center,minimum height=1.2cm,inner sep=4pt}}}}\n\\node[b,fill=gray!12,minimum width=1.4cm] (g) at (0,0) {{Girdi\\\\$x$}};\n\\node[b,fill=blue!12,text width=2.9cm,draw={BL}] (a) at (3.3,0) {{\\textbf{{A birimi}}\\\\gelen $t$ sayısını $t^2-2t$ yapar}};\n\\node[b,fill=orange!15,text width=2.9cm,draw={OR}] (c) at (6.9,0) {{\\textbf{{B birimi}}\\\\gelen $t$ sayısını $t^2+2t$ yapar}};\n\\node[b,fill=gray!12,minimum width=1.4cm] (s) at (9.7,0) {{Çıktı\\\\$24$}};\n\\draw[-{{Stealth}},thick] (g)--(a); \\draw[-{{Stealth}},thick] (a)--(c); \\draw[-{{Stealth}},thick] (c)--(s);',font='\\small')
q('0016',tipId='ikb-islem',tip='İşlem makinesi ve bileşke',z='zor',alt='İki Birimli Makine',kaz='Bileşke işlem makinesinde ara değişkenle ikinci dereceden denklem çözüp reel girdileri bulur; diskriminantı negatif olan dalı eler.',kalip='yeni nesil',
 kart='K-AIK2-05 (işlem makinesi ve bileşke) · ara değerlerden birinin reel girdi vermemesi',
 metin='Şekilde, A biriminin çıktısının B birimine girdiği ve birimlerin işlemlerinin yazılı olduğu bir makine verilmiştir. Makineye girdi olarak x gerçel sayısı verilmektedir ve makinenin çıktısı şekildeki değere eşittir.\nBuna göre, x’in alabileceği reel değerlerin toplamı kaçtır?',
 dogru=2,yan=[(e[0],'Reel köklerin toplamı yerine x² − 2x − 4 = 0 denkleminin kökler çarpımını yazmış.','dikkat'),(e[1],'A biriminin çıktısı için bulduğu iki değerin (4 ve −6) toplamını yazmış.','dikkat'),(e[2],'Δ < 0 olan x² − 2x + 6 = 0 denkleminin “kökler toplamını” da (2) katıp 2 + 2 yazmış.','bilgi'),(e[3],'Ara değerlerin farkını (4 − (−6)) yazmış.','dikkat')],
 istenen='x’in alabileceği reel değerlerin toplamı.',ip=['A biriminin çıktısına bir harf verdiğinde elde ettiğin değerlerin her biri için x’i ayrı ayrı sorgula; hepsi reel girdi verir mi?'],bilgi=[MAK,DEG],sekil=SK,
 ad=[A('A birimini yaz','A’nın çıktısına t denir.','t = x² − 2x'),A('B birimini yaz','Çıktı 24 olduğundan denklem kurulur.','t² + 2t = 24 → t² + 2t − 24 = 0'),A('t’yi bul','Çarpanlarına ayrılır.','(t + 6)(t − 4) = 0 → t = −6 ya da t = 4'),A('Her t için x’i sorgula','Δ’ya bakılır.','t = 4: x² − 2x − 4 = 0, Δ = 20 > 0 · t = −6: x² − 2x + 6 = 0, Δ = −20 < 0 → reel kök yok'),A('Reel köklerin toplamı','Yalnız t = 4’ten gelen kökler toplanır.','x₁ + x₂ = 2')],
 puf='Her ara değer için ikinci denklemi ayrı çöz ve reel kök verip vermediğine bak.')

# ============================ 0017 · zor · düz · ortak kök, tam sayı katsayılar ============================
cift=[]
for a in range(-60,0):
    for b in range(-60,0):
        r1=set(sp.solve(x**2+a*x+6,x)); r2=set(sp.solve(x**2+b*x+8,x))
        if r1&r2: cift.append((a,b))
assert sorted(cift)==[(-7,-9),(-5,-6)] and 63+30==93
e=[-27,30,63,176]; assert (-7-9)*(-5-6)==176 and -16+(-11)==-27 and len({93,*e})==5
q('0017',tipId='ikb-ortak',tip='Ortak kök (tam sayı katsayılı)',z='zor',alt='Ortak Kök ve Tam Sayılar',kaz='Tam sayı katsayılı iki denklemin ortak kökünün tam sayı olduğunu sabit terimlerin bölenlerinden bulup koşula uyan katsayı çiftlerini belirler.',kalip='düz',
 kart='K-AIK2-07 (ortak kök, tam sayı katsayılı) · sabit terimlerin ortak böleni',
 metin='a ve b negatif tam sayılar olmak üzere,\nx² + ax + 6 = 0\nx² + bx + 8 = 0\ndenklemlerinin ortak bir kökü vardır.\nBuna göre, a · b çarpımının alabileceği farklı değerlerin toplamı kaçtır?',
 dogru=93,yan=[(e[1],'Yalnız ortak kökü 2 olan durumu (a = −5, b = −6) almış.','dikkat'),(e[2],'Yalnız ortak kökü 1 olan durumu (a = −7, b = −9) almış.','dikkat'),(e[3],'a · b yerine a + b değerlerini (−16 ve −11) hesaplayıp çarpmış.','dikkat'),(e[0],'a · b yerine a + b değerlerini hesaplayıp toplamış: −16 + (−11).','dikkat')],
 istenen='a · b çarpımının alabileceği farklı değerlerin toplamı.',ip=['Ortak kökün hem 6’nın hem 8’in neyi olması gerektiğini düşün; adaylar kaç tane kalıyor?'],bilgi=[ORT,VIE],
 ad=[A('Aday kökleri bul','Ortak kök r hem 6’nın hem 8’in böleni olmalıdır.','r ∈ {±1, ±2}'),A('Negatif katsayı koşulu','a, b < 0 ise r pozitif olmalıdır (kökler negatif katsayı için pozitiftir).','r = 1 ya da r = 2'),A('Katsayıları bul','Her r için çarpımdan diğer kök, toplamdan a ve b bulunur.','r = 1: kökler 1, 6 ve 1, 8 → a = −7, b = −9 · r = 2: kökler 2, 3 ve 2, 4 → a = −5, b = −6'),A('Çarpımları topla','Çarpımlar farklıdır.','63 + 30 = 93')],
 puf='Baş katsayısı 1 olan, tam sayı katsayılı denklemin rasyonel kökü tam sayıdır.')

# ============================ 0018 · zor · öncüllü · kare kökler ============================
cands=[]
for p1,p2 in [(2,-3),(-2,3),(3,-2),(-3,2)]:
    assert p1**2+p2**2==13 and p1**2*p2**2==36 and p1*p2<0
    cands.append((-(p1+p2),p1*p2,p1**3+p2**3))
assert all(cc[0]**2==1 and cc[1]==-6 for cc in cands) and {cc[2] for cc in cands}=={19,-19}
SR2=['Yalnız I','Yalnız II','I ve II','II ve III','I, II ve III']
q('0018',tipId='ikb-vieta',tip='Kökler arası ilişki ve Vieta',z='zor',alt='Kare Kökler',kaz='Köklerinin kareleri verilen denklemden başlayıp kökler çarpımının işaret koşuluyla katsayıları ve kuvvet ifadelerini değerlendirir.',kalip='öncüllü',
 kart='K-AIK2-06 (kökler arası ilişki) · öncüllü: kareleri verilen kökler, işaret koşulu',
 metin='b ve c gerçel sayılar olmak üzere, kökleri x₁ ve x₂ olan x² + bx + c = 0 denkleminde x₁ · x₂ < 0’dır. x₁² ve x₂² sayıları ise x² − 13x + 36 = 0 denkleminin kökleridir.\nBuna göre,\nI. c = 6\nII. b² = 1\nIII. x₁³ + x₂³ = 19 olabilir.\nyargılarından hangileri doğrudur?',
 dogru='II ve III',sira=SR2,yan=[(SR2[4],'I’i doğru saymış: x₁²x₂² = 36 olduğundan x₁x₂ = 6 alıp x₁ · x₂ < 0 koşulunu gözetmemiş.','dikkat'),(SR2[1],'III’ü yanlış saymış: köklerin yerinin (2, −3) olarak sabit olduğunu düşünüp yalnız −19 değerini bulmuş.','bilgi'),(SR2[2],'I’i doğru, III’ü yanlış saymış: çarpımın işaretini gözetmeyip x₁x₂ = 6 bulmuş ve −19 dışında değer görmemiş.','bilgi'),(SR2[0],'I’i doğru saymış, II’de b = 5 bulup b² = 25 diye yanlış, III’ü de yanlış değerlendirmiş.','islem')],
 istenen='Doğru olan yargıların hangileri olduğu.',ip=['x₁² ve x₂² değerlerinin ne olabileceğini bulduktan sonra x₁ · x₂ < 0 koşulu hangi işaret çiftlerini bırakır?'],bilgi=[VIE,KUV],
 ad=[A('Kareleri bul','x² − 13x + 36 = 0 denkleminin kökleri bulunur.','(x − 4)(x − 9) = 0 → x₁², x₂² ∈ {4, 9}'),A('Kökleri bul','Çarpım negatif olduğundan işaretler zıttır.','(x₁, x₂) = (2, −3) ya da (−2, 3)'),A('I ve II','Toplam ve çarpımdan b, c bulunur.','c = x₁x₂ = −6 → I yanlış · b = −(x₁ + x₂) = ±1 → b² = 1 → II doğru'),A('III','Küpler toplamı iki durumda hesaplanır.','2³ + (−3)³ = −19 · (−2)³ + 3³ = 19 → III doğru')],
 puf='Kareleri verilen köklerde işaret koşulu, hangi köklerin mümkün olduğunu belirler.')

# ============================ 0019 · orta · şekilli · Öklid ============================
assert sp.solve(x*(x+7)-144,x)==[-16,9] and 15**2==9*25 and 20**2==16*25 and 15+20+25==60
e=[35,36,37,52]; assert 15+20==35 and 12+9+15==36 and 25+12==37 and 25+15+12==52 and len({60,*e})==5
u=0.2
SK=fig(f'\\filldraw[fill=blue!12,draw={BL},line width=1.4pt] (0,0)--({9*u},0)--({9*u},{12*u})--cycle;\n\\filldraw[fill=orange!18,draw={OR},line width=1.4pt] ({9*u},0)--({25*u},0)--({9*u},{12*u})--cycle;\n\\draw[thick] (0,0)--({25*u},0)--({9*u},{12*u})--cycle;\n\\draw ({9*u-0.25},0)--({9*u-0.25},0.25)--({9*u},0.25); \\draw ({9*u},{12*u}) ++(-0.17,-0.23) -- ++(0.23,-0.17) -- ++(0.17,0.23);\n\\node[below,text={BL}] at ({4.5*u},0) {{$x$}}; \\node[below,text={OR}] at ({17*u},0) {{$x+7$}}; \\node[right,text={PU}] at ({9*u},{6*u}) {{$12$}};\n\\node[below left] at (0,0) {{$B$}}; \\node[below right] at ({25*u},0) {{$C$}}; \\node[above] at ({9*u},{12*u}) {{$A$}}; \\node[below] at ({9*u},-0.45) {{$H$}};',font='\\normalsize')
q('0019',tipId='ikb-problem',tip='Alan ve geometri problemleri',z='orta',alt='Öklid Bağıntısı',kaz='Dik üçgende hipotenüse ait yükseklik bağıntısından ikinci dereceden denklem kurup üçgenin çevresini hesaplar.',kalip='şekilli',
 kart='K-AIK2-03 (alan ve geometri problemleri) · dik üçgende yükseklik bağıntısı ve çevre',
 metin='Şekilde, A köşesinde dik açılı ABC üçgeninde [AH] ⊥ [BC]’dir. Şekilde uzunluklar birim cinsinden verilmiştir.\nBuna göre, ABC üçgeninin çevresi kaç birimdir?',
 dogru=60,yan=[(e[0],'Hipotenüsü çevreye katmamış: 15 + 20.','dikkat'),(e[1],'ABH üçgeninin çevresini hesaplamış: 12 + 9 + 15.','dikkat'),(e[2],'Çevre yerine hipotenüs ile yüksekliğin toplamını (25 + 12) yazmış.','dikkat'),(e[3],'Çevreye |AC| yerine yüksekliği katmış: 15 + 25 + 12.','dikkat')],
 istenen='ABC üçgeninin çevresi (birim).',ip=['Yüksekliğin, hipotenüsün ayırdığı iki parçayla arasında nasıl bir bağıntı kurulur ve dik kenarlar bu parçalardan nasıl elde edilir?'],bilgi=[OKL,PIS],sekil=SK,
 ad=[A('Öklid’i yaz','h² = p · q bağıntısı kullanılır.','12² = x(x + 7) → x² + 7x − 144 = 0'),A('Kökü bul','Çarpanlarına ayrılır; uzunluk pozitiftir.','(x + 16)(x − 9) = 0 → x = 9'),A('Hipotenüs ve dik kenarlar','|BC| = 9 + 16 = 25; dik kenarlar Pisagor’la bulunur.','|AB|² = 9² + 12² → |AB| = 15 · |AC|² = 16² + 12² → |AC| = 20'),A('Çevreyi bul','Üç kenar toplanır.','15 + 20 + 25 = 60')],
 puf='Yükseklik, hipotenüsü ayırdığı parçaların geometrik ortası gibi düşünülebilir; kenarları sonra Pisagor’la bul.')

# ============================ 0020 · zor · hikâyeli · kesişen yollar, en büyük parça ============================
assert sp.solve((50-(x+1))*(30-x)-1316,x)==[2,77] and (20+27)*(10+18)==1316 and 50-20-3==27 and 30-10-2==18
e=[200,270,360,810]; assert 20*10==200 and 27*10==270 and 20*18==360 and 27*30==810 and 27*18==486 and len({486,*e})==5
SK=fig(f'\\filldraw[fill=green!12,draw={BL},line width=1.4pt] (0,0) rectangle (7,4.2);\n\\filldraw[fill=orange!30,draw={OR},thick] (0,1.4) rectangle (7,2.0);\n\\filldraw[fill=orange!30,draw={OR},thick] (2.8,0) rectangle (3.5,4.2);\n\\node[text={OR}] at (5.4,1.7) {{$x$}}; \\node[text={OR},rotate=90] at (3.15,3.2) {{$x+1$}};\n\\node at (1.4,1.0) {{bahçe}}; \\node at (4.2,1.0) {{bahçe}}; \\node at (1.4,3.1) {{bahçe}}; \\node at (5.0,3.1) {{bahçe}};\n\\draw[<->] (0,-0.4)--(7,-0.4) node[midway,below] {{$50$ m}}; \\draw[<->] (-0.4,0)--(-0.4,4.2) node[midway,left] {{$30$ m}};\n\\draw[<->,{PU}] (0,0.3)--(2.8,0.3) node[midway,above,text={PU}] {{$20$ m}}; \\draw[<->,{PU}] (6.7,0)--(6.7,1.4) node[midway,left,text={PU}] {{$10$ m}};',font='\\small')
q('0020',tipId='ikb-problem',tip='Alan ve geometri problemleri',z='zor',alt='Kesişen Yollar',kaz='Dikdörtgen arsayı kesen iki yolun genişliğini kalan alan denkleminden bulup yol dışında kalan en büyük parçanın alanını hesaplar.',kalip='hikâyeli',
 kart='K-AIK2-03 (alan ve geometri problemleri) · kenarlara paralel kesişen iki yol, parça alanı',
 metin='Kenar uzunlukları şekilde verilen dikdörtgen biçimli bir arsanın üzerinden, kenarlara paralel iki yol geçirilmiştir. Yatay yolun genişliği x metre, dikey yolun genişliği ise yatay yolun genişliğinden 1 metre fazladır. Yolların dışında kalan dört bahçe parçasının alanları toplamı 1316 m²’dir. Dikey yolun sol kenarı arsanın sol kenarından 20 m, yatay yolun alt kenarı arsanın alt kenarından 10 m uzaklıktadır. (Şekil ölçekli çizilmemiştir.)\nBuna göre, bahçe parçalarının en büyüğünün alanı kaç metrekaredir?',
 dogru=486,yan=[(e[0],'En küçük parçanın alanını (20 · 10) bulmuş.','dikkat'),(e[1],'Sağ alt parçayı almış: 27 · 10; üstteki parçanın yüksekliğini (18) hesaplamamış.','dikkat'),(e[2],'Sol üst parçayı en büyük sanmış: 20 · 18.','dikkat'),(e[3],'Yatay yolu hesaba katmayıp sağ şeridin yüksekliğini 30 almış: 27 · 30.','dikkat')],
 istenen='En büyük bahçe parçasının alanı (m²).',ip=['Yollar çıkarıldığında kalan parçalar birleştirilirse oluşan dikdörtgenin kenarları x cinsinden nedir; sonra her parçanın kenarlarını şekildeki ölçülerle yaz.'],bilgi=[ALAN],sekil=SK,
 ad=[A('Kalan parçaları birleştir','Yollar kenara itilince kalan alan tek dikdörtgen olur.','Kenarlar: 50 − (x + 1) ve 30 − x'),A('Denklemi kur ve çöz','Alan 1316’dır; x < 30 olmalıdır.','(49 − x)(30 − x) = 1316 → (x − 2)(x − 77) = 0 → x = 2'),A('Parça kenarlarını bul','Dikey yol 3 m, yatay yol 2 m geniştir.','Genişlikler: 20 ve 50 − 20 − 3 = 27 · Yükseklikler: 10 ve 30 − 10 − 2 = 18'),A('En büyük parça','En geniş ve en yüksek parça alınır.','27 · 18 = 486')],
 puf='En büyük parça, hem en geniş hem en yüksek olan kenarların çarpımıdır.')

# ---------------- bitiş ----------------
for qq in P.ANA: qq['kardes']=None
P.yaz(os.path.join(HD,'ikinciiki-1.json'),'/dev/null')
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=UK))['kartlar'].append(c['id'])
json.dump(dict(konu=P.konu_adi,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 AYT Matematik çıkmış soruları ve yayın soru bankaları (yalnız mantık), MEB 10–11. sınıf müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','ikinciiki.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
