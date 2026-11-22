"""AYT Matematik · Limit (süreklilik dahil) · 2. dalga · 20 soruluk paket (hafif mod; kardeş yok, ipucu 1).
Tek veri kaynağı: şekil, metin ve çeldirici değerleri aynı verilerden; her cevap/çeldirici sympy/Fraction ile assert edilir."""
import sys,os,json,math
HD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(HD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
from ortak import *
from cizim import tikz_svg
from _hafif_mat import tablo_svg,mk
import sympy as sp
from fractions import Fraction as Fr
x,t=sp.symbols('x t')
UK='amat|Limit'
P=Parti('limitiki','Limit',UK,ders='AYT Matematik',idon='aytmat')
KY='ÖSYM AYT Matematik 2018–2026 (Limit ve Süreklilik soruları; yalnız mantık) · yayın soru bankaları (yalnız mantık) · MEB 12. sınıf'
KART=[]
def kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip):
    KART.append(dict(id=id,konu='Limit',alt=alt,fikir=fikir,tuzak=tuzak,zorluk=z,kalip=kalip,adim=adim,tipId=tipId,tip=tip,kaynak=KY))
TIP={}
def tipkayit(tipId,tip,kid): TIP[tipId]=(tip,kid)
def fs(v):
    v=Fr(v); n='−' if v<0 else ''; v=abs(v)
    return n+(str(v.numerator) if v.denominator==1 else f'{v.numerator}/{v.denominator}')
def Q(no,tipId,z,alt,kaz,kalip,metin,dogru,yan,istenen,ip,bilgi,ad,puf,kart_ozet,sekil=None,sira=None):
    tip,kid=TIP[tipId]
    if sira is None:
        vals=[Fr(dogru)]+[Fr(y[0]) for y in yan]; assert len(set(vals))==5,('esit sik',no,vals)
        ordr=sorted(vals); sira=[fs(v) for v in ordr]; d=fs(dogru); yy=[(fs(y[0]),y[1],y[2]) for y in yan]
    else: d=dogru; yy=yan
    assert len(yy)==4 and len(set([d]+[y[0] for y in yy]))==5 and sorted(sira)==sorted([d]+[y[0] for y in yy]),(no,)
    for s_ in ad: assert not any(f'{h})' in s_['aciklama'] for h in 'ABCDE')
    mk(P,no,metin=metin,dogru=d,yan=yy,istenen=istenen,ad=ad,sekil=sekil,sira=sira,ip=ip,bilgi=bilgi,puf=puf,tipId=tipId,tip=tip,z=z,alt=alt,kaz=kaz,kalip=kalip,adim=len(ad),kart=f'{kid} ({kart_ozet})')

# ---------------- bilgi kutuları (örnekler soruların sayılarından farklı) ----------------
B_TAN=B('Tanımlı yeni kavram','soruda tanımı verilen işlem ya da kavram, tanım aynen uygulanarak hesaplanır; tanımda geçmeyen büyüklükler (örneğin fonksiyon değeri) hesaba katılmaz. Örnek: “a noktasındaki fark = sağ limit − sol limit” tanımında f(a) kullanılmaz')
B_TEK=B('Tek yönlü limit ve süreklilik','x, a’ya soldan (x → a⁻) ya da sağdan (x → a⁺) yaklaşırken f(x)’in yaklaştığı değere sol ya da sağ limit denir; ikisi eşitse limit vardır. f, a’da sürekli ise f(a) tanımlıdır ve lim f(x) = f(a)’dır. Örnek: grafikte x = 4’te içi boş (4, 1) ve içi dolu (4, 6) noktaları varsa limit 1, f(4) = 6’dır ve f süreksizdir')
B_SON=B('Sonsuzda limit','pay ve payda polinom ise limit, en büyük dereceli terimlerin oranıdır: derece eşitse baş katsayıların oranı, pay küçükse 0 olur. Örnek: lim (x→∞) (5x² + 1)/(10x² − x) = 1/2')
B_POL=B('Parametreli 0/0 limiti','pay ve payda aynı noktada sıfır olmuyorsa limit ya yok ya da ±∞’dur; limit bir gerçel sayı ise payın o noktada sıfır olması gerekir. Böylece parametre bulunur, sonra çarpan sadeleştirilir. Örnek: lim (x→1) (x² + kx − 3)/(x − 1) sonlu ise 1 + k − 3 = 0 olmalıdır')
B_BIL=B('Bileşke ve yaklaşma yönü','f(1 ± x) gibi ifadelerde x → 0⁺ iken içteki ifade 1’e hangi yönden gidiyorsa dıştaki f o yönde okunur: 1 + x → 1⁺, 1 − x → 1⁻’dir. Örnek: x → 0⁺ iken f(3 − x), f’nin 3’teki sol limitidir')
B_GEN=B('Limit özellikleri','limitler varsa toplam, fark, çarpım ve (paydanın limiti 0 değilse) bölümün limiti, limitlerin aynı işlemi ile bulunur. Limit varsa bile fonksiyonun o noktadaki değeri hakkında bir şey söylenemez. Örnek: lim f = 6, lim g = 3 ise lim (f/g) = 2’dir, f(a) bilinmez')
B_SUR=B('Süreklilik şartı','f, a’da sürekli ise sol limit = sağ limit = f(a) olur. Parçalı fonksiyonda bölünme noktalarında eşitlik kurulur; limit olup değer farklıysa ya da fonksiyon tanımsızsa süreklilik yoktur. Örnek: x < 2 için 3x, x ≥ 2 için x + k ise 6 = 2 + k’dır')
B_ARA=B('Süreklilik ve işaret','aralıkta sürekli bir h fonksiyonu hiçbir noktada 0 olmuyorsa işareti değişmez: bir noktadaki işareti her yerde geçerlidir. Örnek: h sürekli, h(x) ≠ 0 ve h(0) = −2 ise her x için h(x) < 0’dır')
B_US=B('Logaritma ve limit','ln a + ln b = ln(ab), k·ln a = ln aᵏ ve e^(ln a) = a özellikleri limitten önce kullanılır; ifade sadeleşince değer yazılır. Örnek: e^(ln(x² − 4) − ln(x − 2)) = x + 2’dir (x > 2)')
B_TRG=B('Trigonometrik limit','x → 0 iken sin(kx)/x → k ve tan(kx)/x → k olur (x radyan). Örnek: lim (x→0) tan 6x / sin 2x = 3')
B_MUT=B('Mutlak değer ve tek yönlü limit','|u| ifadesi u ≥ 0 için u, u < 0 için −u olarak açılır; x → a⁺ ve x → a⁻ için açılım ayrı yazılır. Örnek: |x − 3|/(x − 3), x → 3⁺ iken 1, x → 3⁻ iken −1’dir')

# ---------------- tip ve kartlar ----------------
tipkayit('lmx-tanim','Tanımlı kavram ve grafikte süreklilik','K-ALM2-01'); tipkayit('lmx-sonsuz','Sonsuzda limit','K-ALM2-02'); tipkayit('lmx-polin','Polinom ve parametreli limit','K-ALM2-03')
tipkayit('lmx-bilesik','Bileşke ve grafiklerle limit','K-ALM2-04'); tipkayit('lmx-genel','Limit özellikleri ve yargılar','K-ALM2-05'); tipkayit('lmx-surek','Parçalı fonksiyonda süreklilik','K-ALM2-06')
tipkayit('lmx-us','Üstel ve logaritmik ifadede limit','K-ALM2-07'); tipkayit('lmx-ara','Süreklilik ve işaret','K-ALM2-08'); tipkayit('lmx-trig','Grafikten trigonometrik limit','K-ALM2-09'); tipkayit('lmx-mutlak','Mutlak değerli ifadede tek yönlü limit','K-ALM2-10')
kart('K-ALM2-01','Tanımlı kavram ve grafikte süreklilik','Tanım aynen uygulanır; grafikte her noktada sol limit, sağ limit ve fonksiyon değeri ayrı ayrı okunur ve sınıflandırılır.','Fonksiyon değerini tanıma karıştırmak; limit varsa sürekli sanmak.','orta','grafik',3,'lmx-tanim','Tanımlı kavram ve grafikte süreklilik')
kart('K-ALM2-02','Sonsuzda limit','Rasyonel ifadelerde limit en büyük dereceli terimlerin oranına bakılarak bulunur.','Katsayıları toplamak; payın derecesini yanlış belirlemek; sabit terimlere bakmak.','kolay','düz',2,'lmx-sonsuz','Sonsuzda limit')
kart('K-ALM2-03','Polinom ve parametreli limit','Limitin sonlu olması payı sıfırlayan değeri verir; parametre bulunur, çarpan sadeleşir; polinomun köklerinden yapısı kurulur.','Payın sıfır olması koşulunu unutmak; yanlış çarpan sadeleştirmek.','orta','düz',3,'lmx-polin','Polinom ve parametreli limit')
kart('K-ALM2-04','Bileşke ve grafiklerle limit','Bileşkede içteki ifadenin yaklaşma yönü bulunur, dıştaki fonksiyon o yönde okunur; iki grafiğin işlemi limitte uygulanır.','Yaklaşma yönünü kaçırmak; değeri limit sanmak; işlemleri ters kurmak.','orta','grafik',4,'lmx-bilesik','Bileşke ve grafiklerle limit')
kart('K-ALM2-05','Limit özellikleri ve yargılar','Limit işlemleri yalnız limitler varken yazılır; yargılar tek tek sınanır.','Limitten fonksiyon değerine geçmek; limiti olmayan ifadeyi toplamak.','orta','öncüllü',4,'lmx-genel','Limit özellikleri ve yargılar')
kart('K-ALM2-06','Parçalı fonksiyonda süreklilik','Bölünme noktalarında eşitlik kurulur; birden fazla noktada koşul aranıyorsa hangisinin sağlandığı ayrı sınanır.','Tek noktayı kontrol edip bırakmak; parçaları karıştırmak.','zor','tablo',5,'lmx-surek','Parçalı fonksiyonda süreklilik')
kart('K-ALM2-07','Üstel ve logaritmik ifadede limit','Logaritma özellikleriyle ifade tek logaritmaya indirilir; e^(ln u) = u ile sadeleşir.','Katsayıyı kuvvet yapmayı unutmak; limit yerine ifadenin kendisini bulmak.','orta','düz',3,'lmx-us','Üstel ve logaritmik ifadede limit')
kart('K-ALM2-08','Süreklilik ve işaret','Sürekli ve hiç sıfır olmayan fonksiyonun işareti sabittir; bir noktadaki işaret her yerde geçerlidir.','Değerler arasında sıra aramak; işareti noktadan noktaya değişir sanmak.','zor','öncüllü',4,'lmx-ara','Süreklilik ve işaret')
kart('K-ALM2-09','Grafikten trigonometrik limit','Grafikten parametre okunur; sin(kx)/x ve tan(kx)/x limitleri k olarak kullanılır.','Parametreyi yanlış okumak; limitlerin oranını ters yazmak.','orta','grafik',4,'lmx-trig','Grafikten trigonometrik limit')
kart('K-ALM2-10','Mutlak değerli ifadede tek yönlü limit','Mutlak değer iki yanda ayrı açılır; grafikten parametre okunur; tek yönlü limitler ayrı hesaplanır.','Mutlak değeri iki yanda aynı açmak; işaret hatası.','zor','grafik',5,'lmx-mutlak','Mutlak değerli ifadede tek yönlü limit')

# ---------------- çizim yardımcıları ----------------
CF='blue!70!black'; CG='orange!90!black'; CH='violet'; CK='green!50!black'
def fig(body,font='\\small'): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font='+font+']\n'+body+'\n\\end{tikzpicture}')
def pt(p,sx,sy): return f'({p[0]*sx:.3f},{p[1]*sy:.3f})'
def AX(x0,x1,y0,y1,sx,sy=None,ox=0.0,xl=None,yl=None,grid=True,fs_='\\footnotesize',orig=True,xn=None,yn=None):
    """xl/yl: {değer: etiket} (None ise tamsayılar; boş sözlük etiket yok). ox: yatay kaydırma (cm)."""
    sy=sy or sx; o=[]
    if xl is None: xl={i:str(i) for i in range(x0,x1+1) if i!=0}
    if yl is None: yl={j:str(j) for j in range(y0,y1+1) if j!=0}
    def X(v): return f'{ox+v*sx:.3f}'
    if grid:
        for i in range(x0,x1+1): o.append(f'\\draw[gray!35,thin] ({X(i)},{y0*sy:.3f}) -- ({X(i)},{y1*sy:.3f});')
        for j in range(y0,y1+1): o.append(f'\\draw[gray!35,thin] ({X(x0)},{j*sy:.3f}) -- ({X(x1)},{j*sy:.3f});')
    o.append(f'\\draw[-{{Stealth}},thick] ({X(x0-0.3)},0) -- ({X(x1+0.8)},0) node[right] {{$x$}};')
    o.append(f'\\draw[-{{Stealth}},thick] ({X(0)},{(y0-0.3)*sy:.3f}) -- ({X(0)},{(y1+0.8)*sy:.3f}) node[above] {{$y$}};')
    for v,l in xl.items():
        an='below=2pt'
        if isinstance(l,tuple): l,an=l
        o.append(f'\\node[{an},font={fs_},fill=white,inner sep=0.5pt] at ({X(v)},0) {{${l}$}};')
    for v,l in yl.items(): o.append(f'\\node[left=2pt,font={fs_},fill=white,inner sep=0.5pt] at ({X(0)},{v*sy:.3f}) {{${l}$}};')
    if orig: o.append(f'\\node[below left,font={fs_}] at ({X(0)},0) {{$O$}};')
    return '\n'.join(o)
class C:
    """Bir grafik düzlemi: ölçek ve kaydırma tutar."""
    def __init__(s,sx,sy=None,ox=0.0): s.sx=sx; s.sy=sy or sx; s.ox=ox
    def p(s,a): return f'({s.ox+a[0]*s.sx:.3f},{a[1]*s.sy:.3f})'
    def seg(s,a,b,renk=CF,w='1.8pt'): return f'\\draw[{renk},line width={w}] {s.p(a)} -- {s.p(b)};'
    def poly(s,pts,renk=CF,w='1.8pt'): return f'\\draw[{renk},line width={w}] '+' -- '.join(s.p(a) for a in pts)+';'
    def egri(s,fn,a,b,renk=CF,n=48,w='1.8pt'):
        pts=[(a+(b-a)*i/n,fn(a+(b-a)*i/n)) for i in range(n+1)]
        return f'\\draw[{renk},line width={w}] plot[smooth] coordinates {{'+' '.join(s.p(q) for q in pts)+'};'
    def dolu(s,a,renk=CF): return f'\\fill[{renk}] {s.p(a)} circle (0.09);'
    def bos(s,a,renk=CF): return f'\\draw[{renk},thick,fill=white] {s.p(a)} circle (0.09);'
    def tx(s,a,txt,pos='above',renk=CF,fs_='\\small\\bfseries'): return f'\\node[{pos},{renk},font={fs_}] at {s.p(a)} {{{txt}}};'
    def kes(s,a,b,renk='gray'): return f'\\draw[{renk},dashed,thick] {s.p(a)} -- {s.p(b)};'

# ============ 01 kolay · tanımlı kavram: sıçrama (kırık çizgi grafik) ============
c=C(0.75)
L1={1:2,2:4,3:5}; R1={1:4,2:4,3:2}; f1={1:3,2:1,3:5}
S1={a:abs(R1[a]-L1[a]) for a in L1}; assert S1=={1:2,2:0,3:3}; v=sum(S1.values()); assert v==5
e=[sum(R1[a]-L1[a] for a in L1), sum(abs(R1[a]-f1[a]) if a==2 else S1[a] for a in L1), abs(f1[1]-L1[1])+S1[2]+S1[3], 3]
assert e==[-1,8,4,3] and v not in e
g_=[c.seg((0,1),(1,2)),c.seg((1,4),(2,4)),c.seg((2,4),(3,5)),c.seg((3,2),(5,4)),
    c.dolu((0,1)),c.bos((1,2)),c.dolu((1,3)),c.bos((1,4)),c.bos((2,4)),c.dolu((2,1)),c.dolu((3,5)),c.bos((3,2)),c.dolu((5,4)),
    c.tx((4.45,4.5),'$y=f(x)$')]
SK=fig(AX(0,5,0,5,0.75)+'\n'+'\n'.join(g_))
Q('0001','lmx-tanim','kolay','Tanımlı Kavram: Sıçrama','Tanımı verilen sıçrama kavramını grafikte okunan tek yönlü limitlerle uygular.','grafik',
 'Bir f fonksiyonunun a noktasında sol limiti ve sağ limiti varsa, bu iki limitin farkının mutlak değerine f fonksiyonunun a noktasındaki sıçraması denir ve S(a) ile gösterilir.\nŞekilde, [0, 5] aralığında tanımlı f fonksiyonunun grafiği verilmiştir. Doğru parçalarının uçları ızgara çizgilerinin kesişim noktalarındadır; içi dolu nokta grafiğe ait, içi boş nokta grafiğe ait değildir.\nBuna göre, S(1) + S(2) + S(3) toplamı kaçtır?',
 v,[(e[0],'Mutlak değeri uygulamamış, sağ limit − sol limit farklarını işaretli toplamış: 2 + 0 + (−3).','dikkat'),(e[1],'x = 2’de limitleri eşit bulmasına rağmen f(2) = 1 değerini kullanıp |4 − 1| = 3 yazmış: 2 + 3 + 3.','bilgi'),(e[2],'x = 1’de sağ limit yerine f(1) = 3 değerini kullanmış: |3 − 2| = 1; toplam 1 + 0 + 3.','bilgi'),(e[3],'Sıçramaların değerlerini değil, süreksiz olunan nokta sayısını yazmış.','dikkat')],
 'Sıçramaların toplamı.',['Tanımda yalnız iki tek yönlü limit var; her nokta için sol ve sağ yüksekliği grafikten ayrı ayrı oku.'],[B_TAN,B_TEK],
 [A('x = 1’de oku','Soldan içi boş (1, 2) noktasına, sağdan içi boş (1, 4) noktasına yaklaşılır.','S(1) = |4 − 2| = 2'),A('x = 2’de oku','Soldan da sağdan da yükseklik 4’e gider; f(2) = 1 değeri tanımda yer almaz.','S(2) = |4 − 4| = 0'),A('x = 3’te oku','Soldan 5’e, sağdan 2’ye yaklaşılır.','S(3) = |2 − 5| = 3'),A('Topla','Üç sıçrama toplanır.','2 + 0 + 3 = 5')],
 'Tanım yalnız sağ ve sol limite bakar; fonksiyon değeri sonucu etkilemez.','K-ALM2-01; sıçrama tanımı',sekil=SK)

# ============ 02 kolay · sonsuzda limit ============
ex=(2*x-1)*(3*x+4)/(x**2+x-5); v=sp.limit(ex,x,sp.oo); assert v==6 and sp.limit(ex,x,-sp.oo)==6
e=[0,2,5,Fr(4,5)]; assert 6 not in e
Q('0002','lmx-sonsuz','kolay','Rasyonel İfadenin Sonsuzdaki Limiti','Pay ve paydası polinom olan ifadenin x sonsuza giderken limitini en büyük dereceli terimlerin oranıyla bulur.','düz',
 'Pay ve paydası polinom olan bir rasyonel ifadenin değişkeni sınırsız artırıldığında ifade bir gerçel sayıya yaklaşmaktadır.\nBuna göre, lim (x→∞) (2x − 1)(3x + 4)/(x² + x − 5) limitinin değeri kaçtır?',
 v,[(e[0],'Payın derecesini 1 sanıp payın paydadan küçük dereceli olduğunu düşünmüş.','dikkat'),(e[1],'Yalnız ilk çarpandaki 2x’i alıp ikinci çarpanı hesaba katmamış: 2x/x² yerine 2 yazmış.','islem'),(e[2],'Çarpanların baş katsayılarını çarpmak yerine toplamış: 2 + 3.','islem'),(e[3],'Sabit terimlerin oranına bakmış: (−1 · 4)/(−5).','bilgi')],
 'Limitin değeri.',['Pay çarpım biçiminde; önce payın derecesini ve baş katsayısını belirle.'],[B_SON],
 [A('Payın baş terimi','İki çarpanın en büyük dereceli terimleri çarpılır.','(2x)(3x) = 6x²'),A('Payda','Paydanın baş terimi x²’dir.','x²'),A('Oranla','Derece eşit olduğundan baş katsayıların oranı alınır.','6/1 = 6')],
 'Derece eşitse limit baş katsayıların oranıdır.','K-ALM2-02; derece eşit rasyonel ifade')

# ============ 03 kolay · parametre koşullu limit ============
a_=sp.symbols('a')
av=sp.solve(4-2*a_+6,a_)[0]; assert av==5
v=sp.limit((x**2-5*x+6)/(x-2),x,2); assert v==-1 and sp.factor(x**2-5*x+6)==(x-2)*(x-3)
e=[0,1,2,5]; assert v not in e
Q('0003','lmx-polin','kolay','Parametreli Limit','Limitin sonlu olması koşulundan paydadaki sıfırı payla eşleştirip parametreyi bulur ve limiti hesaplar.','düz',
 'a bir gerçel sayı olmak üzere, lim (x→2) (x² − ax + 6)/(x − 2) limiti bir gerçel sayıdır.\nBuna göre, bu limitin değeri kaçtır?',
 v,[(e[0],'x = 2 için payı sıfır bulunca limiti 0 sanmış.','dikkat'),(e[1],'a = 5’i bulmuş ve çarpanlara ayırmış; x − 3 değerini x = 2’de 3 − 2 = 1 hesaplamış.','islem'),(e[2],'Sadeleştirmeden sonra x yerine 2 yazmayı unutup değişkenin yaklaştığı değeri yazmış.','dikkat'),(e[3],'Limit değeri yerine a parametresini yazmış.','bilgi')],
 'Limitin değeri.',['Limitin bir gerçel sayı olabilmesi için paydayı sıfırlayan değerde payın alması gereken değeri düşün.'],[B_POL],
 [A('Koşulu kur','Payda x = 2’de sıfır olduğundan pay da sıfır olmalıdır.','4 − 2a + 6 = 0 → a = 5'),A('Çarpanlara ayır','Pay x² − 5x + 6 olur.','(x − 2)(x − 3)'),A('Sadeleştir ve yaz','Ortak çarpan kalkar, x = 2 yazılır.','x − 3 → 2 − 3 = −1')],
 'Sonlu limit için payı da sıfırlayan parametreyi bul, sonra çarpanı sadeleştir.','K-ALM2-03; parametreli 0/0')

# ============ 04 orta · bileşke, parabol parçalı grafik ============
c=C(0.8)
fa=lambda u:4-u**2; fb=lambda u:u+1
L=sp.limit(4-x**2,x,1,'-'); Rr=sp.limit(x+1,x,1,'+'); assert (L,Rr)==(3,2)
v=L+2*Rr; assert v==7
e=[Rr+2*L, 1+2*1, L+Rr, 2*(L+Rr)]; assert e==[8,3,5,10] and v not in e
g_=[c.egri(fa,-2,1,CF),c.seg((1,2),(3,4)),c.dolu((-2,0)),c.bos((1,3)),c.dolu((1,1)),c.bos((1,2)),c.dolu((3,4)),c.tx((1.3,0.55),'$y=f(x)$','right')]
SK=fig(AX(-2,3,0,5,0.8)+'\n'+'\n'.join(g_))
Q('0004','lmx-bilesik','orta','İçerdeki İfadenin Yaklaşma Yönü','f(1 − x) ve f(1 + x) gibi ifadelerde x sıfıra sağdan giderken içteki ifadenin yönünü belirleyip grafikten okur.','grafik',
 'Şekilde, [−2, 3] aralığında tanımlı f fonksiyonunun grafiği verilmiştir. Grafiğin x ≤ 1 kısmı bir parabol parçasıdır; x > 1 kısmı doğru parçasıdır. Noktalar ızgara çizgilerinin kesişimindedir; içi dolu nokta grafiğe ait, içi boş nokta grafiğe ait değildir.\nBuna göre, lim (x→0⁺) [f(1 − x) + 2f(1 + x)] limitinin değeri kaçtır?',
 v,[(e[0],'Yönleri ters okumuş: f(1 − x) için sağ limiti 2, f(1 + x) için sol limiti 3 almış: 2 + 2·3.','bilgi'),(e[1],'Limit yerine f(1) = 1 değerini iki yerde de kullanmış: 1 + 2·1.','bilgi'),(e[2],'2 çarpanını unutmuş: 3 + 2.','islem'),(e[3],'2 çarpanını parantezin tamamına uygulamış: 2(3 + 2).','islem')],
 'İfadenin limiti.',['x, 0’a sağdan giderken 1 − x ve 1 + x’in 1’e hangi yönden yaklaştığını ayrı ayrı belirle.'],[B_BIL,B_TEK],
 [A('Birinci terim','x → 0⁺ iken 1 − x, 1’e soldan yaklaşır; grafik parabol parçasında (1, 3) noktasına gider.','f(1 − x) → 3'),A('İkinci terim','1 + x, 1’e sağdan yaklaşır; grafik doğru parçasında içi boş (1, 2) noktasına gider.','f(1 + x) → 2'),A('Birleştir','Limitler yerine yazılır.','3 + 2 · 2 = 7')],
 'Bileşkede önce içteki ifadenin yaklaşma yönünü bul, dıştakini o yönde oku.','K-ALM2-04; f(a ± x) biçiminde bileşke',sekil=SK)

# ============ 05 orta · tablo: tek noktada tanımlı fonksiyonda süreklilik ============
k_,m_=sp.symbols('k m')
kv=sp.solve(4+2*k_-6,k_)[0]; assert kv==1
mv=sp.limit((x**2+kv*x-6)/(x-2),x,2); assert mv==5 and sp.factor(x**2+x-6)==(x-2)*(x+3)
v=kv+mv; assert v==6
e=[kv-mv,kv,mv-kv,mv]; assert e==[-4,1,4,5] and v not in e
SK=tablo_svg(['x','f(x)'],[['x ≠ 2','(x² + kx − 6)/(x − 2)'],['x = 2','m']])
Q('0005','lmx-surek','orta','Tek Noktada Tanımlı Fonksiyonda Süreklilik','Gerçel sayılarda sürekli olan, tek noktada ayrı tanımlı fonksiyonun parametrelerini limit koşulundan bulur.','tablo',
 'k ve m gerçel sayılar olmak üzere, gerçel sayılar kümesi üzerinde tanımlı f fonksiyonunun kuralı aşağıdaki tabloda verilmiştir. f fonksiyonu x = 2 noktasında süreklidir.\nBuna göre, k + m toplamı kaçtır?',
 v,[(e[0],'k = 1 ve m = 5 değerlerini bulmuş, toplam yerine k − m yazmış.','islem'),(e[1],'Yalnız k’yi bulup m’yi toplama katmamış.','dikkat'),(e[2],'k = 1 ve m = 5 değerlerini bulmuş, toplam yerine m − k yazmış.','islem'),(e[3],'m = 5 değerini bulmuş, k’yi toplama katmamış.','dikkat')],
 'k ile m’nin toplamı.',['Süreklilik için x = 2’deki limit ile fonksiyon değerinin eşit olması gerekir; limitin sonlu olmasını sağlayan k’yi önce bul.'],[B_SUR,B_POL],
 [A('k’yi bul','x = 2’de payda sıfırdır; limit sonlu olduğundan pay da sıfır olmalıdır.','4 + 2k − 6 = 0 → k = 1'),A('Limiti hesapla','Pay (x − 2)(x + 3) biçiminde çarpanlanır ve sadeleşir.','lim (x→2) (x + 3) = 5'),A('m’yi eşitle','Süreklilikte limit, fonksiyon değerine eşittir.','m = 5'),A('Topla','k ve m toplanır.','1 + 5 = 6')],
 'Süreklilik, limit ile fonksiyon değerini eşitler; limitin sonlu olması parametreyi verir.','K-ALM2-06; tek noktada ayrı tanımlı fonksiyon',sekil=SK)

# ============ 06 orta · öncüllü, limit özellikleri ============
sira6=['Yalnız I','Yalnız II','I ve III','II ve III','I, II ve III']
fL,gL=2,-2
I6=(fL+gL==0); III6=(Fr(fL,gL)==-1); II6=False
assert (I6,II6,III6)==(True,False,True)
Q('0006','lmx-genel','orta','Limit Özelliklerini Sınama','Limit varken toplamın ve bölümün limitini yazar; limitten fonksiyon değerine geçilemeyeceğini ayırt eder.','öncüllü',
 'a bir gerçel sayı olmak üzere, gerçel sayılar kümesi üzerinde tanımlı f ve g fonksiyonları için\nlim (x→a) f(x) = 2 ve lim (x→a) g(x) = −2\neşitlikleri sağlanıyor.\nBuna göre,\nI. lim (x→a) (f(x) + g(x)) = 0\nII. f(a) + g(a) = 0\nIII. lim (x→a) f(x)/g(x) = −1\nifadelerinden hangileri her zaman doğrudur?',
 'I ve III',[('Yalnız I','III’te bölümün limitini yazmak için g(a) ≠ 0 koşulunu aramış; oysa paydanın limiti −2 ≠ 0 olduğundan III de doğrudur.','bilgi'),('Yalnız II','Limitlerin toplamının fonksiyon değerlerinin toplamı olduğunu sanmış; I ve III’ü yanlış saymış.','bilgi'),('II ve III','I’in doğru olduğunu görmeyip f(a) = 2 ve g(a) = −2 sanarak II’yi doğru saymış; III’ü de oranın limiti olarak doğru bulmuş.','dikkat'),('I, II ve III','Limit değerlerini fonksiyon değeri sanarak II’yi de doğru kabul etmiş.','bilgi')],
 'Her zaman doğru olan yargılar.',['Verilen bilgi yalnız x = a’ya yaklaşırken ne olduğunu söylüyor; fonksiyonun a’daki değeri hakkında bilgi var mı, sorgula.'],[B_GEN],
 [A('I’i sına','Limitler var olduğundan toplamın limiti limitlerin toplamıdır.','2 + (−2) = 0 → I doğru'),A('II’yi sına','f(a) ve g(a) değerleri verilmemiştir; limit değeri fonksiyon değerini belirlemez.','II her zaman doğru değil'),A('III’ü sına','Paydanın limiti 0 değildir; bölümün limiti limitlerin oranıdır.','2/(−2) = −1 → III doğru')],
 'Limit işlemleri limitler varken geçerlidir; fonksiyon değeri limitten bağımsızdır.','K-ALM2-05; limit özellikleri ve fonksiyon değeri',sira=sira6)

# ============ 07 orta · parabol grafiği, parametre ve limit ============
a7=sp.symbols('a7')
f7=a7*(x+2)*(x-3); av=sp.solve(sp.limit(f7/(x-3),x,3)-5,a7)[0]; assert av==1
v=sp.limit(f7.subs(a7,av)/(x**2-4),x,-2); assert v==sp.Rational(5,4)
e=[Fr(-5,4),Fr(25,4),5,Fr(4,5)]; assert Fr(5,4) not in e
c=C(0.7,0.28)
g_=[c.egri(lambda u:(u+2)*(u-3),-2.75,3.75,CF,60),c.dolu((-2,0)),c.dolu((3,0)),c.tx((1.1,4.2),'$y=f(x)$','right')]
SK=fig(AX(-3,4,-7,6,0.7,0.28,xl={-2:('-2','below left=3pt'),3:('3','below right=3pt')},yl={},grid=False,orig=True)+'\n'+'\n'.join(g_))
Q('0007','lmx-polin','orta','Grafiği Verilen Polinomda Limit','Parabolün x eksenini kestiği noktalardan fonksiyonu kurar, verilen limitten baş katsayıyı bulup başka bir limiti hesaplar.','grafik',
 'Şekilde, ikinci dereceden bir f polinom fonksiyonunun grafiği verilmiştir. Grafik, x eksenini yalnızca −2 ve 3 noktalarında kesmektedir.\nlim (x→3) f(x)/(x − 3) = 5\nolduğuna göre, lim (x→−2) f(x)/(x² − 4) limitinin değeri kaçtır?',
 Fr(5,4),[(e[0],'a = 1 bulmuş; sadeleştirdikten sonra paydadaki x − 2 ifadesini x = −2’de −4 yerine 4 hesaplamış: (−5)/4.','islem'),(e[1],'Baş katsayı yerine verilen limit değerini a = 5 almış: 5·(−5)/(−4).','bilgi'),(e[2],'Verilen limit değeri 5’i doğrudan cevap sanmış.','dikkat'),(e[3],'Oranı ters yazmış: (x − 2)/(x − 3) → (−4)/(−5).','islem')],
 'Limitin değeri.',['Grafikteki iki kökten f’yi baş katsayısı bilinmeyen biçimde yaz; verilen limit bu katsayıyı bulduracak.'],[B_POL],
 [A('f’yi yaz','Kökleri −2 ve 3 olan ikinci dereceden polinom, a baş katsayısıyla yazılır.','f(x) = a(x + 2)(x − 3)'),A('a’yı bul','Verilen limitte (x − 3) sadeleşir, x = 3 yazılır.','a · 5 = 5 → a = 1'),A('İstenen limiti yaz','x² − 4 = (x − 2)(x + 2) ile (x + 2) sadeleşir.','(x − 3)/(x − 2)'),A('Değeri yaz','x = −2 yazılır.','(−5)/(−4) = 5/4')],
 'Kökler çarpan olarak yazılır; verilen limit baş katsayıyı bulur.','K-ALM2-03; grafiği verilen polinom',sekil=SK)

# ============ 08 orta · f·g sürekli, parabol grafiği ============
c=C(0.8)
fp=lambda u:6-(u-2)**2
Lf=fp(3); assert Lf==5
Lg=10; prod=Lf*Lg; assert prod==50; v=Fr(prod,2); assert v==25
e=[10,20,4,50]; assert v not in e and Fr(2,5)*10==4
g_=[c.egri(fp,0,2.93,CF),c.egri(fp,3.07,4,CF),c.dolu((0,2)),c.dolu((4,2)),c.bos((3,5)),c.dolu((3,2)),c.tx((0.4,6.3),'$y=f(x)$','right')]
SK=fig(AX(0,4,0,6,0.8)+'\n'+'\n'.join(g_))
Q('0008','lmx-surek','orta','Çarpım Fonksiyonunun Sürekliliği','Grafikte limit ve fonksiyon değeri farklı olan f ile limiti bilinen g’nin çarpımının sürekliliğinden g(3)’ü bulur.','grafik',
 'Şekilde, [0, 4] aralığında tanımlı f fonksiyonunun grafiği verilmiştir. Grafik, x = 3 noktası dışında bir parabol parçasıdır; noktalar ızgara çizgilerinin kesişimindedir. İçi dolu nokta grafiğe ait, içi boş nokta grafiğe ait değildir.\n[0, 4] aralığında tanımlı g fonksiyonunun x = 3 noktasında limiti vardır ve lim (x→3) g(x) = 10’dur. f · g fonksiyonu x = 3 noktasında süreklidir.\nBuna göre, g(3) değeri kaçtır?',
 v,[(e[0],'g’nin x = 3’te sürekli olduğunu varsayıp g(3) = 10 yazmış.','bilgi'),(e[1],'f(3) = 2 ile limit değerini çarpmış: 2 · 10.','islem'),(e[2],'Eşitliği ters kurmuş: g(3) = (2/5) · 10.','islem'),(e[3],'f · g çarpımının limitini (5 · 10 = 50) g(3) olarak yazmış.','dikkat')],
 'g(3) değeri.',['Çarpımın x = 3’teki limitini ve fonksiyon değerini ayrı ayrı yaz; ikisini süreklilik eşitler.'],[B_SUR,B_GEN],
 [A('Limitleri oku','Grafikte x → 3 iken f(x), içi boş (3, 5) noktasına gider; f(3) = 2’dir.','lim f = 5 · f(3) = 2'),A('Çarpımın limiti','Her iki limit de var olduğundan çarpımın limiti çarpımdır.','lim (f·g) = 5 · 10 = 50'),A('Süreklilik şartı','Çarpım x = 3’te sürekli olduğundan limit, fonksiyon değerine eşittir.','f(3) · g(3) = 50'),A('g(3)’ü bul','f(3) = 2 yazılır.','2 · g(3) = 50 → g(3) = 25')],
 'Çarpımın sürekliliği, limit ile çarpımın değerini eşitler; her çarpanın değeri ayrı hesaba girer.','K-ALM2-06; f·g çarpımının sürekliliği',sekil=SK)

# ============ 09 orta · grafikte limit var, sürekli değil sınıflaması ============
c=C(0.75)
pts={1:(3,3,3),2:(2,4,None),3:(5,5,2),4:(3,3,None),5:(1,1,1)}   # sol,sağ,f(a)
say=0; lim_var=0
for a_k,(l_,r_,f_) in pts.items():
    lv=(l_==r_); sur=lv and f_==l_
    lim_var+=lv; say+=(lv and not sur)
assert say==2 and lim_var==4
e=[0,1,3,4]; assert say not in e
g_=[c.seg((0,1),(1,3)),c.seg((1,3),(2,2)),c.seg((2,4),(3,5)),c.seg((3,5),(4,3)),c.seg((4,3),(5,1)),c.seg((5,1),(6,2)),
    c.dolu((0,1)),c.dolu((1,3)),c.bos((2,2)),c.dolu((2,4)),c.bos((3,5)),c.dolu((3,2)),c.bos((4,3)),c.dolu((5,1)),c.dolu((6,2)),
    c.tx((5.3,3.2),'$y=f(x)$','above')]
SK=fig(AX(0,6,0,5,0.75,0.75)+'\n'+'\n'.join(g_))
Q('0009','lmx-tanim','orta','Limiti Var Ama Sürekli Olmayan Noktalar','Grafikte her noktada limit varlığı ve süreklilik şartlarını sınayıp noktaları sınıflandırır.','grafik',
 'Şekilde, [0, 6] aralığındaki bir f fonksiyonunun grafiği verilmiştir. Doğru parçalarının uçları ızgara çizgilerinin kesişim noktalarındadır; içi dolu nokta grafiğe ait, içi boş nokta grafiğe ait değildir. Bir fonksiyon, tanımsız olduğu noktada sürekli değildir.\nBuna göre, x ∈ {1, 2, 3, 4, 5} için f fonksiyonunun limitinin var olduğu hâlde sürekli olmadığı kaç farklı x değeri vardır?',
 say,[(e[0],'Limiti olan her noktada fonksiyonu sürekli sanmış.','dikkat'),(e[1],'Yalnız f(a) ≠ limit olan x = 3’ü saymış; x = 4’te grafikte nokta olmadığını fark etmemiş.','bilgi'),(e[2],'Süreksiz olan tüm noktaları saymış: x = 2, 3 ve 4.','dikkat'),(e[3],'Limiti var olan noktaların sayısını yazmış: x = 1, 3, 4 ve 5.','dikkat')],
 'Limiti olup sürekli olmayan nokta sayısı.',['Beş noktanın her birinde sol limit, sağ limit ve f(a) değerini ayrı ayrı belirle; fonksiyonun tanımsız olabileceğini de unutma.'],[B_TEK],
 [A('x = 1, 5','Her ikisinde de sol limit, sağ limit ve fonksiyon değeri eşittir.','Sürekli'),A('x = 2','Soldan 2’ye, sağdan 4’e yaklaşılır.','Limit yok'),A('x = 3','Soldan da sağdan da 5’e yaklaşılır; f(3) = 2’dir.','Limit var, sürekli değil'),A('x = 4','Soldan da sağdan da 3’e yaklaşılır; nokta içi boştur, f(4) tanımsızdır.','Limit var, sürekli değil'),A('Say','İki nokta bu koşulu sağlar.','x = 3 ve x = 4 → 2')],
 'Limitin varlığı süreklilik için gereklidir ama yetmez: değerin tanımlı ve limite eşit olması gerekir.','K-ALM2-01; limit ve süreklilik sınıflaması',sekil=SK)

# ============ 10 orta · grafikten trigonometrik limit ============
c=C(1.0,0.5)
a10=3
f10=lambda u:math.sin(a10*u)/u
assert abs(f10(math.pi/3))<1e-12 and sp.limit(sp.sin(a10*x)/x,x,0)==3
v=sp.limit((sp.sin(a10*x)/x)*sp.tan(2*x)/sp.sin(4*x),x,0); assert v==sp.Rational(3,2)
e=[3,6,9,12]; assert Fr(3,2) not in e
pi3=math.pi/3
g_=[c.egri(f10,-2.4,-0.02,CF,80),c.egri(f10,0.02,2.4,CF,80),c.bos((0,a10)),c.dolu((pi3,0)),c.dolu((-pi3,0)),c.tx((2.6,0.9),'$y=f(x)$','right')]
ax=AX(-3,3,-1,4,1.0,0.5,xl={pi3:('\\frac{\\pi}{3}','below=8pt'),-pi3:('-\\frac{\\pi}{3}','below=8pt')},yl={},grid=False,orig=True)
SK=fig(ax+'\n'+'\n'.join(g_))
Q('0010','lmx-trig','orta','Grafikten Parametre Okuyup Trigonometrik Limit','Grafiğin x eksenini kestiği noktadan sinüs ifadesindeki katsayıyı bulur, trigonometrik limit kurallarıyla limiti hesaplar.','grafik',
 'a pozitif bir gerçel sayı olmak üzere, x ≠ 0 için f(x) = sin(ax)/x kuralıyla tanımlı f fonksiyonunun grafiği şekilde verilmiştir. Grafik, x eksenini kesen en küçük pozitif x değeri π/3’tür; x = 0 noktasında grafikte içi boş bir nokta vardır.\nBuna göre, lim (x→0) f(x) · tan 2x / sin 4x limitinin değeri kaçtır?',
 Fr(3,2),[(e[0],'tan 2x / sin 4x çarpanının limitini hesaba katmamış, yalnız f(x) → 3 yazmış.','dikkat'),(e[1],'tan 2x / sin 4x oranını ters (4/2 = 2) hesaplamış: 3 · 2.','islem'),(e[2],'Oranı (2 + 4)/2 = 3 almış: 3 · 3.','islem'),(e[3],'Oranı 4 almış (yalnız sin 4x’in katsayısını): 3 · 4.','dikkat')],
 'Limitin değeri.',['sin(ax) fonksiyonunun x eksenini ilk kez pozitif tarafta kestiği noktadan a’yı bul.'],[B_TRG],
 [A('a’yı bul','sin(ax) = 0 ve ax = π için en küçük pozitif x değeri π/a’dır.','π/a = π/3 → a = 3'),A('f’nin limiti','x → 0 iken sin 3x / x → 3.','lim f(x) = 3'),A('Oranın limiti','x → 0 iken tan 2x / sin 4x → 2/4.','1/2'),A('Çarp','Limitler çarpılır.','3 · 1/2 = 3/2')],
 'Önce grafikten katsayıyı bul, sonra çarpımın limitini limitlerin çarpımı olarak yaz.','K-ALM2-09; grafikten katsayı ve trigonometrik limit',sekil=SK)

# ============ 11 orta · iki grafik: f+g ve g−h ============
c1=C(0.62,0.62,0.0); c2=C(0.62,0.62,4.6)
uL,uR,vL,vR=3,4,1,3
v=(uL-vL)+(uR-vR); assert v==3
e=[uL+uR, vL+vR, (uL+vL)+(uR+vR), (vL-uL)+(vR-uR)]; assert e==[7,4,11,-3] and v not in e
vl=lambda u:u*u/4
g1=[c1.seg((0,1),(2,3)),c1.seg((2,4),(4,0)),c1.dolu((0,1)),c1.bos((2,3)),c1.dolu((2,1)),c1.bos((2,4)),c1.dolu((4,0)),c1.tx((3.4,3.3),'$f+g$','above')]
g2=[c2.egri(vl,0,2,CG),c2.seg((2,3),(4,1),CG),c2.dolu((0,0),CG),c2.dolu((2,1),CG),c2.bos((2,3),CG),c2.dolu((4,1),CG),c2.tx((3.4,3.3),'$g-h$','above',CG)]
SK=fig(AX(0,4,0,5,0.62)+'\n'+'\n'.join(g1)+'\n'+AX(0,4,0,5,0.62,ox=4.6)+'\n'+'\n'.join(g2))
Q('0011','lmx-bilesik','orta','İki Fonksiyonun İşlem Grafiklerinden Limit','f + g ve g − h grafiklerinden f + h ifadesinin tek yönlü limitlerini bulur.','grafik',
 'Şekilde, [0, 4] aralığında tanımlı f, g ve h fonksiyonları için f + g (mavi) ve g − h (turuncu) fonksiyonlarının grafikleri verilmiştir. Noktalar ızgara çizgilerinin kesişimindedir; içi dolu nokta grafiğe ait, içi boş nokta grafiğe ait değildir.\nBuna göre, lim (x→2⁻) (f(x) + h(x)) + lim (x→2⁺) (f(x) + h(x)) toplamı kaçtır?',
 v,[(e[0],'Yalnız f + g grafiğinin sol ve sağ limitlerini toplamış: 3 + 4.','dikkat'),(e[1],'Yalnız g − h grafiğinin sol ve sağ limitlerini toplamış: 1 + 3.','dikkat'),(e[2],'f + h’yi elde etmek için iki grafiği çıkarmak yerine toplamış: (3 + 1) + (4 + 3).','islem'),(e[3],'Çıkarmayı ters kurmuş: (g − h) − (f + g) farklarını toplamış.','islem')],
 'İstenen iki limitin toplamı.',['f + h ifadesini verilen iki fonksiyonun bir işlemiyle yaz; sonra her yanda iki grafikten ayrı ayrı oku.'],[B_GEN,B_TEK],
 [A('f + h’yi kur','(f + g) − (g − h) ifadesinde g sadeleşir.','f + h = (f + g) − (g − h)'),A('Sol limit','x = 2’ye soldan f + g için 3’e, g − h için 1’e yaklaşılır.','3 − 1 = 2'),A('Sağ limit','Sağdan f + g için 4’e, g − h için 3’e yaklaşılır.','4 − 3 = 1'),A('Topla','İki limit toplanır.','2 + 1 = 3')],
 'İşlem grafiklerinde istenen fonksiyonu verilenlerin bir işlemi olarak yaz, her yan için limiti ayrı oku.','K-ALM2-04; iki işlem grafiği',sekil=SK)

# ============ 12 orta · üstel/logaritmik ifadede limit ============
ef=(x**2-9)*(x**2-x-6)/(x-3)**2; v=sp.limit(sp.cancel(ef),x,3); assert v==30 and sp.simplify(sp.cancel(ef)-(x+3)*(x+2))==0
e=[0,5,6,11]; assert (sp.limit(sp.cancel((x**2-9)*(x**2-x-6)/(x-3)),x,3),3+2,3+3,(3+3)+(3+2))==(0,5,6,11) and v not in e
Q('0012','lmx-us','orta','e Üzeri Logaritmik İfadenin Limiti','Logaritma özellikleriyle ifadeyi tek terime indirip e üzeri limitini sadeleştirerek bulur.','düz',
 '3’ten büyük gerçel sayılar kümesi üzerinde bir f fonksiyonu\nf(x) = ln(x² − 9) + ln(x² − x − 6) − 2ln(x − 3)\nbiçiminde tanımlanıyor.\nBuna göre, lim (x→3⁺) e^(f(x)) limitinin değeri kaçtır?',
 v,[(e[0],'−2ln(x − 3) teriminin katsayısını 1 sayıp paydada tek (x − 3) bırakmış; ifade (x − 3)(x + 3)(x + 2) olunca limiti 0 bulmuş.','dikkat'),(e[1],'Yalnız (x + 2) çarpanını hesaba katmış: x = 3 için 5.','dikkat'),(e[2],'Yalnız (x + 3) çarpanını hesaba katmış: x = 3 için 6.','dikkat'),(e[3],'İki çarpanın değerlerini çarpmak yerine toplamış: 6 + 5.','islem')],
 'Limitin değeri.',['e üzeri ifadeyi yazarken logaritma özelliklerini kullan; sonra paydadaki (x − 3) çarpanlarının neyle sadeleştiğine bak.'],[B_US],
 [A('Tek ifadeye indir','Toplam çarpım, katsayı kuvvet, fark bölüm olur.','e^f = (x² − 9)(x² − x − 6)/(x − 3)²'),A('Çarpanlara ayır','x² − 9 = (x − 3)(x + 3) ve x² − x − 6 = (x − 3)(x + 2).','(x − 3)²(x + 3)(x + 2)/(x − 3)²'),A('Sadeleştir','(x − 3)² kalkar.','(x + 3)(x + 2)'),A('Değeri yaz','x = 3 yazılır.','6 · 5 = 30')],
 'Logaritmaları tek ifadeye indirmek, e üzeri ifadeyi rasyonel ifadeye çevirir.','K-ALM2-07; e üzeri logaritma toplamı')

# ============ 13 orta · mutlak değerli parabol ============
c=C(0.8,0.36)
p13=lambda u:2*(u-1)*(u-3)
assert p13(0)==6 and p13(2)==-2
Rl=sp.limit(sp.Abs(2*(x-1)*(x-3))/(x-1),x,1,'+'); Ll=sp.limit(sp.Abs(2*(x-1)*(x-3))/(x-1),x,1,'-')
assert (Rl,Ll)==(4,-4); v=Rl-Ll; assert v==8
e=[-16,-8,0,4]; assert Rl*Ll==-16 and Ll-Rl==-8 and v not in e
g_=[c.egri(p13,0,3.25,CF,60),c.dolu((1,0)),c.dolu((3,0)),c.dolu((0,6)),c.tx((3.0,6.2),'$y=p(x)$','right')]
SK=fig(AX(0,4,-2,7,0.8,0.36,xl={1:('1','below left=3pt'),3:('3','below right=3pt')},yl={6:'6'},grid=False)+'\n'+'\n'.join(g_))
Q('0013','lmx-mutlak','orta','Mutlak Değerli Ağın Tek Yönlü Limitleri','Grafiği verilen ikinci dereceden polinomu kurar, mutlak değerini iki yanda ayrı açarak tek yönlü limitlerin farkını bulur.','grafik',
 'Şekilde, ikinci dereceden bir p polinom fonksiyonunun grafiği verilmiştir. Grafik, x eksenini 1 ve 3 noktalarında, y eksenini 6 noktasında kesmektedir.\nf(x) = |p(x)| olduğuna göre,\nlim (x→1⁺) f(x)/(x − 1) − lim (x→1⁻) f(x)/(x − 1)\nfarkı kaçtır?',
 v,[(e[0],'Sağ ve sol limiti 4 ve −4 bulmuş, fark yerine çarpımlarını yazmış.','islem'),(e[1],'Doğru limitleri bulmuş, çıkarmayı ters kurmuş: sol − sağ.','islem'),(e[2],'Mutlak değeri iki yanda da aynı açmış; iki limiti eşit bulup farkı 0 yazmış.','bilgi'),(e[3],'Yalnız sağ limiti bulup sol limiti hesaba katmamış.','dikkat')],
 'Verilen farkın değeri.',['Önce grafikten p’yi kur; x = 1’in iki yanında p’nin işaretini ayrı ayrı belirleyip mutlak değeri öyle aç.'],[B_MUT,B_POL],
 [A('p’yi kur','Kökler 1 ve 3; p(0) = 6 baş katsayıyı verir.','p(x) = 2(x − 1)(x − 3)'),A('Sağ limit','1 < x < 3 için p(x) < 0 olduğundan |p| = −p olur.','−2(x − 3) → 4'),A('Sol limit','x < 1 için p(x) > 0 olduğundan |p| = p olur.','2(x − 3) → −4'),A('Farkı yaz','Sağ limitten sol limit çıkarılır.','4 − (−4) = 8')],
 'Mutlak değer, bölünme noktasının iki yanında işarete göre ayrı açılır.','K-ALM2-10; grafiği verilen polinomun mutlak değeri',sekil=SK)

# ============ 14 zor · tablo: parçalı fonksiyonda yalnız bir süreksizlik noktası ============
def f14(a,u): return u**2+a if u<1 else (2*u+1 if u<=4 else 3*u-a)
# a = 2: x = 1'de sürekli (1 + 2 = 3), x = 4'te süreksiz; a = 3: x = 4'te sürekli (12 − 3 = 9), x = 1'de süreksiz
assert (1+2==3, 2*4+1==12-2)==(True,False) and (1+3==3, 2*4+1==12-3)==(False,True)
assert {f14(a_,0)+f14(a_,6) for a_ in (2,3)}=={18}
v=18
e=[15,17,20,16]
assert 2+(2*6+1)==15 and 1+(3*6-2)==17 and 2+3*6==20 and 1+(3*6-3)==16 and v not in e
SK=tablo_svg(['x aralığı','f(x)'],[['x < 1','x² + a'],['1 ≤ x ≤ 4','2x + 1'],['x > 4','3x − a']])
Q('0014','lmx-surek','zor','Yalnızca Bir Noktada Süreksiz Fonksiyon','Üç parçalı fonksiyonda iki bölünme noktasındaki süreklilik koşullarını ayrı ayrı sınayıp yalnızca bir süreksizlik olduğu bilgisinden iki durumu değerlendirir.','tablo',
 'a bir gerçel sayı olmak üzere, gerçel sayılar kümesi üzerinde tanımlı f fonksiyonunun kuralı aşağıdaki tabloda verilmiştir. f fonksiyonunun sürekli olmadığı yalnızca bir nokta vardır.\nBuna göre, a’nın bu koşulu sağlayan bütün değerleri için f(0) + f(6) toplamı kaçtır?',
 v,[(e[0],'f(6) için 2x + 1 parçasını kullanıp f(6) = 13; f(0) = a = 2 almış: 2 + 13.','islem'),(e[1],'a = 2 durumunda f(0) için ikinci parçayı kullanıp f(0) = 1; f(6) = 16 almış: 1 + 16.','islem'),(e[2],'f(6) = 3x − a’da a’yı çıkarmayı unutmuş: f(0) = 2, f(6) = 18.','dikkat'),(e[3],'a = 3 durumunda f(0) için ikinci parçayı kullanıp f(0) = 1; f(6) = 15 almış: 1 + 15.','islem')],
 'f(0) + f(6) toplamı.',['İki bölünme noktasında süreklilik koşullarını ayrı ayrı yaz ve “yalnızca bir” ifadesinin ne gerektirdiğini düşün.'],[B_SUR],
 [A('x = 1’de eşitle','Soldan 1 + a, sağdan (ve değerde) 2 · 1 + 1 değeri alınır.','1 + a = 3 → a = 2'),A('x = 4’te eşitle','Soldan (ve değerde) 2 · 4 + 1, sağdan 12 − a alınır.','9 = 12 − a → a = 3'),A('Durumları ayır','İki eşitlik aynı anda sağlanamaz; yalnız birinin sağlanması a = 2 ya da a = 3 demektir.','a = 2 veya a = 3'),A('Toplamı hesapla','f(0) = a ve f(6) = 18 − a olur; toplam a’ya bağlı değildir.','a + (18 − a) = 18')],
 'Hangi parçanın hangi değerde kullanıldığını bölünme noktalarına bakarak belirle; toplam parametreyi götürebilir.','K-ALM2-06; yalnızca bir süreksizlik noktası',sekil=SK)

# ============ 15 zor · öncüllü, iki grafik ve bileşke ============
c1=C(0.62,0.62,0.0); c2=C(0.62,0.62,4.4)
# f: (0,1)->(1,2) açık; f(1)=3; (1,4) açık -> (4,2). g: (0,3)->(2,1)->(4,3)
assert (2,4,3)==(2,4,3)
I15=True; II15=False; III15=True
# lim g = 1 (yukarıdan); f(g(2)) = f(1) = 3; lim f(g(x)) = f(1+) = 4
fR=4; fv=3; assert fR!=fv
sira15=['Yalnız I','Yalnız III','I ve II','I ve III','II ve III']
g1=[c1.seg((0,1),(1,2)),c1.seg((1,4),(4,2)),c1.dolu((0,1)),c1.bos((1,2)),c1.dolu((1,3)),c1.bos((1,4)),c1.dolu((4,2)),c1.tx((3.3,4.1),'$f$','above')]
g2=[c2.seg((0,3),(2,1),CG),c2.seg((2,1),(4,3),CG),c2.dolu((0,3),CG),c2.dolu((2,1),CG),c2.dolu((4,3),CG),c2.tx((3.4,3.9),'$g$','above',CG)]
SK=fig(AX(0,4,0,5,0.62)+'\n'+'\n'.join(g1)+'\n'+AX(0,4,0,5,0.62,ox=4.4)+'\n'+'\n'.join(g2))
Q('0015','lmx-bilesik','zor','Bileşke Fonksiyonda Süreklilik ve Limit','İç fonksiyonun yaklaşma yönünü belirleyip bileşkenin limitini fonksiyon değeriyle karşılaştırarak yargıları sınar.','öncüllü',
 'Şekilde, [0, 4] aralığında tanımlı f (mavi) ve g (turuncu) fonksiyonlarının grafikleri verilmiştir. Noktalar ızgara çizgilerinin kesişimindedir; içi dolu nokta grafiğe ait, içi boş nokta grafiğe ait değildir. g’nin grafiği iki doğru parçasından oluşur.\nBuna göre,\nI. g fonksiyonu x = 2 noktasında süreklidir.\nII. f ∘ g fonksiyonu x = 2 noktasında süreklidir.\nIII. lim (x→2) f(g(x)) = 4’tür.\nifadelerinden hangileri doğrudur?',
 'I ve III',[('Yalnız I','III’teki limiti 4 yerine f(g(2)) = 3 değeriyle karıştırıp III’ü yanlış saymış; II’yi de yanlış bulmuş.','bilgi'),('Yalnız III','I’i yanlış saymış: x = 2’de V biçiminde bir kırılma görüp g’yi süreksiz sanmış.','dikkat'),('I ve II','İç fonksiyon sürekli olunca bileşkenin de sürekli olacağını sanmış; dış fonksiyonun g(2) = 1’deki durumuna bakmamış.','bilgi'),('II ve III','Bileşkenin limiti ile değerini eşit (4 = 3) sayarak II’yi doğru kabul etmiş; I’i de yanlış saymış.','bilgi')],
 'Doğru olan yargılar.',['x → 2 iken g(x)’in 1’e hangi yönden yaklaştığına bak ve f’yi 1’de o yönde oku; sonra f(g(2)) ile karşılaştır.'],[B_BIL,B_SUR],
 [A('I’i sına','x = 2’de g(2) = 1 ve iki yandan limit de 1’dir.','g, x = 2’de sürekli → I doğru'),A('İç yönü bul','x → 2 iken g(x), 1’e büyük değerlerden (1⁺) yaklaşır.','g(x) → 1⁺'),A('III’ü sına','f’nin 1’deki sağ limiti içi boş (1, 4) noktasıdır.','lim f(g(x)) = 4 → III doğru'),A('II’yi sına','Bileşkenin x = 2’deki değeri f(g(2)) = f(1) = 3’tür; limit 4’tür.','4 ≠ 3 → II yanlış')],
 'Bileşkede iç fonksiyon sürekli olsa bile dış fonksiyonun yaklaşılan noktadaki durumu süreklilik için ayrıca sınanır.','K-ALM2-04; bileşkede limit ve süreklilik',sekil=SK,sira=sira15)

# ============ 16 zor · öncüllü, grafik ve mutlak değer/çarpım/toplam ============
c=C(0.62)
fL16,fR16,fv16=3,-3,1
# I: lim|f| = 3 var; II: g=(x-3)f -> limit 0 = g(3)=0; III: f(x)+f(6-x): limit 0, değer 2 -> süreksiz
I16=abs(fL16)==abs(fR16); II16=((3-3)*fv16==0); k_lim=fL16+fR16; k_val=fv16+fv16
assert I16 and II16 and k_lim==0 and k_val==2 and k_lim!=k_val
sira16=['Yalnız I','I ve II','I ve III','II ve III','I, II ve III']
g_=[c.seg((0,1),(3,3)),c.seg((3,-3),(6,0)),c.dolu((0,1)),c.bos((3,3)),c.dolu((3,1)),c.bos((3,-3)),c.dolu((6,0)),c.tx((4.9,1.1),'$y=f(x)$','above')]
SK=fig(AX(0,6,-3,4,0.62,0.62)+'\n'+'\n'.join(g_))
Q('0016','lmx-genel','zor','Grafikten Türetilen Fonksiyonlarda Limit ve Süreklilik','Grafiği verilen f’den türetilen |f|, (x − 3)·f(x) ve f(x) + f(6 − x) fonksiyonlarının limit ve süreklilik durumunu sınar.','öncüllü',
 'Şekilde, [0, 6] aralığında tanımlı f fonksiyonunun grafiği verilmiştir. Doğru parçalarının uçları ızgara çizgilerinin kesişim noktalarındadır; içi dolu nokta grafiğe ait, içi boş nokta grafiğe ait değildir.\nBuna göre,\nI. |f| fonksiyonunun x = 3 noktasında limiti vardır.\nII. g(x) = (x − 3) · f(x) fonksiyonu x = 3 noktasında süreklidir.\nIII. h(x) = f(x) + f(6 − x) fonksiyonu x = 3 noktasında süreklidir.\nifadelerinden hangileri doğrudur?',
 'I ve II',[('Yalnız I','II’de f’nin x = 3’te limiti olmadığı için çarpımın da limiti yoktur sanmış; oysa (x − 3) çarpanı limiti 0 yapar.','bilgi'),('I, II ve III','h’nin x = 3’te limitinin 0 olduğunu görüp sürekli saymış; h(3) = f(3) + f(3) = 2 değerini karşılaştırmamış.','dikkat'),('I ve III','II’yi yanlış saymış; III’te h’nin limitini 0 buluyor ama değerinin 2 olduğunu görmeyip sürekli sanmış.','dikkat'),('II ve III','I’i yanlış saymış (f’nin limiti yok); III’te limit 0 bulup değeri f(3) + f(3) = 2’yi karşılaştırmamış.','dikkat')],
 'Doğru olan yargılar.',['Her yargıda x = 3’ün iki yanında ifadeyi ayrı ayrı yaz: hangi yan f’nin hangi parçasını kullanıyor?'],[B_TEK,B_GEN],
 [A('I’i sına','Soldan f → 3, sağdan f → −3; mutlak değer ikisini de 3 yapar.','lim |f| = 3 → I doğru'),A('II’yi sına','f sınırlıdır ve (x − 3) → 0; çarpımın her iki yandaki limiti 0’dır, g(3) = 0 · f(3) = 0.','lim g = 0 = g(3) → II doğru'),A('III’ü sına','x → 3⁻ iken 6 − x → 3⁺; soldan 3 + (−3), sağdan (−3) + 3 değeri alınır.','lim h = 0 · h(3) = 2 · III yanlış')],
 'Limit ile fonksiyon değeri ayrı sınanır: limit 0, değer 2 ise süreklilik yoktur.','K-ALM2-05; türetilmiş fonksiyonlarda limit ve süreklilik',sekil=SK,sira=sira16)

# ============ 17 zor · süreklilik ve işaret (ara değer) ============
hf=lambda xv,fx:fx+xv-3   # f(x) ≠ 3-x  -> h=f+x-3 ≠ 0
hg=lambda xv,gx:gx-2*xv    # g(x) ≠ 2x
assert hf(0,0)==-3<0 and hg(1,5)==3>0
# h<0 ise f(x) < 3-x: f(2)<1 (D), f(4)<-1 -> f(4)>-1 Y ; g(x)>2x : g(3)>6 (D), g(0)>0 -> g(0)<0 Y
sira17=['Yalnız I','I ve II','I ve III','II ve III','I, II ve III']
Q('0017','lmx-ara','zor','Sürekli Fonksiyonun İşareti','Hiçbir yerde sıfır olmayan sürekli fonksiyonun işaretinin sabit kalmasını kullanarak fonksiyon değerleri arasındaki eşitsizlikleri sınar.','öncüllü',
 'Gerçel sayılar kümesi üzerinde tanımlı ve sürekli f ve g fonksiyonları, her x gerçel sayısı için\nf(x) ≠ 3 − x ve g(x) ≠ 2x\nkoşullarını sağlamaktadır. f(0) = 0 ve g(1) = 5 olduğu bilinmektedir.\nBuna göre,\nI. f(2) < 1\nII. g(3) > 6\nIII. f(4) > −1\nifadelerinden hangileri her zaman doğrudur?',
 'I ve II',[('Yalnız I','g(1) = 5 > 2 olduğundan g(x) − 2x’in pozitif olduğunu görmeyip II’yi sınamamış; yalnız f için işaret sabitliğini kullanmış.','dikkat'),('I, II ve III','f’nin değerlerinin sıfıra yakın kalacağını sanıp III’ü de doğru kabul etmiş; oysa f(4) < −1’dir.','bilgi'),('I ve III','g için hiç bilgi çıkarılamayacağını sanıp II’yi dışarıda bırakmış; III’ü f’nin değerleri sıfıra yakın kalır diyerek doğru saymış.','bilgi'),('II ve III','f(x) − (3 − x) farkının negatif olduğunu pozitif sanmış; I’i yanlış, III’ü doğru bulmuş.','bilgi')],
 'Her zaman doğru olan yargılar.',['f(x) + x − 3 ve g(x) − 2x ifadelerinin sürekliliğini ve sıfır değerlerini incele.'],[B_ARA],
 [A('f için fark','h(x) = f(x) + x − 3 sürekli ve hiçbir yerde 0 değil; h(0) = 0 + 0 − 3 = −3 < 0.','h(x) < 0 → f(x) < 3 − x'),A('I ve III','x = 2 ve x = 4 için eşitsizlik yazılır.','f(2) < 1 → I doğru · f(4) < −1 → III yanlış'),A('g için fark','k(x) = g(x) − 2x sürekli ve hiçbir yerde 0 değil; k(1) = 5 − 2 = 3 > 0.','k(x) > 0 → g(x) > 2x'),A('II’yi sına','x = 3 için eşitsizlik yazılır.','g(3) > 6 → II doğru')],
 'Sürekli ve hiç sıfır olmayan farkın işareti, bir noktadaki değerden her yere taşınır.','K-ALM2-08; sürekli fonksiyonun işareti',sira=sira17)

# ============ 18 zor · geometri: sonsuzda limit ============
c=C(0.62,0.62)
tt=sp.symbols('tt',positive=True)
v=sp.limit(sp.sqrt(tt**2+8*tt)-tt,tt,sp.oo); assert v==4
e=[-4,0,2,8]; assert sp.limit(8*tt/tt,tt,sp.oo)==8 and sp.limit(8*tt/(4*tt),tt,sp.oo)==2 and v not in e
tp=4.5; yp=math.sqrt(8*tp)
cc=C(0.62,0.62)
g_=[f'\\fill[blue!8] {cc.p((0,0))} -- {cc.p((tp,0))} -- {cc.p((tp,yp))} -- cycle;',cc.egri(lambda u:math.sqrt(8*u),0,8.2,CF,60),
    f'\\draw[{CG},line width=1.4pt] {cc.p((0,0))} -- {cc.p((tp,yp))};',f'\\draw[{CK},line width=1.4pt] {cc.p((tp,0))} -- {cc.p((tp,yp))};',
    f'\\draw[thick] {cc.p((tp-0.45,0))} -- {cc.p((tp-0.45,0.45))} -- {cc.p((tp,0.45))};',
    cc.dolu((tp,yp),CF),f'\\node[above left,font=\\small] at {cc.p((tp,yp))} {{$P$}};',f'\\node[below,font=\\small] at {cc.p((tp,0))} {{$H(t,0)$}};',
    cc.tx((7.8,6.0),'$y=\\sqrt{8x}$','above')]
ax=AX(0,9,0,8,0.62,0.62,xl={},yl={},grid=False,orig=True)
SK=fig(ax+'\n'+'\n'.join(g_))
Q('0018','lmx-sonsuz','zor','Geometride Sonsuzda Limit','Eğri üzerindeki noktaya bağlı iki uzunluğun farkını yazıp eşlenik yöntemiyle sonsuzdaki limitini hesaplar.','şekilli',
 'Dik koordinat düzleminde y = √(8x) eğrisi üzerinde P(t, √(8t)) noktası alınıyor (t > 0). O başlangıç noktası, H(t, 0) noktası P’nin x eksenine dik izdüşümüdür.\nBuna göre, lim (t→∞) (|OP| − |OH|) limitinin değeri kaçtır?',
 v,[(e[0],'Farkı ters kurmuş: |OH| − |OP|.','islem'),(e[1],'Büyük t için |OP| ile |OH|’yi “yaklaşık eşit” sayıp farkı 0 yazmış.','dikkat'),(e[2],'Eşlenikle çarptıktan sonra paydadaki √(t² + 8t) + t ifadesini 4t almış: 8t/(4t).','islem'),(e[3],'Eşlenik paydasında yalnız t’yi bırakmış: 8t/t.','dikkat')],
 'Verilen limitin değeri.',['|OP| ve |OH| uzunluklarını t cinsinden yaz; ∞ − ∞ belirsizliğini gidermenin yolunu düşün.'],[B_SON],
 [A('Uzunlukları yaz','OHP dik üçgeninde |OH| = t ve |PH| = √(8t) olur; hipotenüs bulunur.','|OP| = √(t² + 8t)'),A('Farkı kur','Fark √(t² + 8t) − t biçimindedir; ∞ − ∞ belirsizliği vardır.','√(t² + 8t) − t'),A('Eşlenikle çarp','Eşlenik çarpımı karelerin farkını verir.','8t / (√(t² + 8t) + t)'),A('Limiti hesapla','Pay ve payda t’ye bölünür; paydadaki kök 1’e gider.','8/(1 + 1) = 4')],
 'İki büyük uzunluğun farkında eşlenik, belirsizliği oranın limitine çevirir.','K-ALM2-02; geometri ve eşlenikle sonsuzda limit',sekil=SK)

# ============ 19 zor · mutlak değerli oran, parçalı doğru grafiği ============
c=C(0.9)
m_=sp.symbols('m_')
# sol: f(x)=2-x (x<=2) -> g sol limit: (2-x)/|x-2| = 1 ; sağ: m(x-2)/(x-2)=m
assert sp.limit((2-x)/sp.Abs(x-2),x,2,'-')==1
mv=1; v=mv*(5-2); assert v==3
e=[9,1,4,6]; assert (3*(5-2),mv,mv*(5-1),2*(5-2))==(9,1,4,6) and v not in e
g_=[c.seg((0,2),(2,0)),c.dolu((0,2)),c.dolu((2,0)),c.tx((0.55,2.45),'$y=f(x)$','right')]
SK=fig(AX(0,5,0,3,0.9)+'\n'+'\n'.join(g_))
Q('0019','lmx-mutlak','orta','Mutlak Değerli Oranın Limitinden Parametre','Grafikten sol parçayı kurup mutlak değerli oranın iki yanlı limitinin varlığından sağ parçadaki katsayıyı bulur.','grafik',
 'm bir gerçel sayı olmak üzere, gerçel sayılar kümesi üzerinde tanımlı f fonksiyonunun x ≤ 2 için f(x), şekilde verilen doğru parçasını içeren doğrunun üzerindedir; işaretli noktalar ızgara çizgilerinin kesişimindedir. x > 2 için f(x) = m(x − 2) kuralıyla tanımlıdır.\nx ≠ 2 için g(x) = f(x)/|x − 2| fonksiyonunun x = 2 noktasında limiti var olduğuna göre, f(5) değeri kaçtır?',
 v,[(e[0],'x − 2 değerini (5 − 2 = 3) m sanmış: f(5) = 3 · 3.','dikkat'),(e[1],'m = 1’i bulmuş ve f(5) yerine m’yi yazmış.','dikkat'),(e[2],'f(5) hesabında (x − 2) yerine (x − 1) yazmış: 1 · (5 − 1).','islem'),(e[3],'Sol parçanın y eksenini kestiği değer 2’yi m almış: 2 · 3.','bilgi')],
 'f(5) değeri.',['Önce grafikten x ≤ 2 kısmının kuralını yaz; sonra g’nin x = 2’de soldan ve sağdan limitini mutlak değeri açarak ayrı ayrı hesapla.'],[B_MUT,B_TEK],
 [A('Sol kuralı yaz','Doğru (0, 2) ve (2, 0) noktalarından geçer.','f(x) = 2 − x'),A('Sol limiti bul','x < 2 için |x − 2| = 2 − x olur ve sadeleşir.','lim g = (2 − x)/(2 − x) = 1'),A('Sağ limiti bul','x > 2 için |x − 2| = x − 2 olur ve sadeleşir.','lim g = m(x − 2)/(x − 2) = m'),A('m’yi bul ve f(5)’i hesapla','Limitin var olması için iki yan eşit olmalıdır.','m = 1 → f(5) = 1 · 3 = 3')],
 'Mutlak değerli oranda iki yan ayrı hesaplanır; limitin varlığı yanların eşitliğini verir.','K-ALM2-10; mutlak değerli oran ve parametre',sekil=SK)

# ============ 20 zor · parabol grafiği, kök koşullu limit ============
c=C(0.8,0.5)
cs=[]
for r in (1,3):
    cc_=-r**2; cs.append(cc_)
assert sp.limit((x**2-1)/((x-1)*(x-3)),x,1)==-1 and sp.limit((x**2-9)/((x-1)*(x-3)),x,3)==3
v=sum(cs); assert v==-10
# diğer c için limit sonsuz: c=-2 -> x^2-2 at x=1 -> -1 ≠ 0
assert sp.limit((x**2-2)/((x-1)*(x-3)),x,1,'+')==sp.oo
e=[-9,-1,9,10]; assert v not in e and (cs[0]*cs[1])==9
g_=[c.egri(lambda u:(u-1)*(u-3),0,4.2,CF,60),c.dolu((1,0)),c.dolu((3,0)),c.dolu((0,3)),c.tx((1.6,3.3),'$y=g(x)$','right')]
SK=fig(AX(0,4,-1,4,0.8,0.5,xl={1:('1','below left=3pt'),3:('3','below right=3pt')},yl={3:'3'},grid=False)+'\n'+'\n'.join(g_))
Q('0020','lmx-polin','zor','Kök Koşullu Limitte Parametre','Grafiği verilen polinomun köklerinde payın da sıfır olması koşulunu iki kök için ayrı ayrı kurup parametrenin değerlerini toplar.','grafik',
 'Şekilde, ikinci dereceden bir g polinom fonksiyonunun grafiği verilmiştir. Grafik, x eksenini 1 ve 3 noktalarında, y eksenini 3 noktasında kesmektedir. c bir gerçel sayı olmak üzere f(x) = x² + c fonksiyonu tanımlanıyor.\ng’nin kökü olan en az bir a sayısı için lim (x→a) f(x)/g(x) limiti bir gerçel sayıdır.\nBuna göre, c’nin alabileceği değerlerin toplamı kaçtır?',
 v,[(e[0],'Yalnız x = 3 kökünü düşünüp c = −9 almış.','dikkat'),(e[1],'Yalnız x = 1 kökünü düşünüp c = −1 almış.','dikkat'),(e[2],'Değerlerin toplamı yerine çarpımını almış: (−1)·(−9).','islem'),(e[3],'c değerlerini x² − c = 0 biçiminde yazıp pozitif bulmuş: 1 + 9.','islem')],
 'c’nin alabileceği değerlerin toplamı.',['Limitin sonlu olması için payın kökte alması gereken değeri belirle; g’nin iki kökü olduğunu unutma.'],[B_POL],
 [A('g’yi kur','Kökler 1 ve 3, g(0) = 3 baş katsayıyı verir.','g(x) = (x − 1)(x − 3)'),A('a = 1 durumu','Payda 1’de sıfır; limit sonlu olması için pay da 1’de sıfır olmalıdır.','1 + c = 0 → c = −1'),A('a = 3 durumu','Payda 3’te sıfır; pay da 3’te sıfır olmalıdır.','9 + c = 0 → c = −9'),A('Değerleri doğrula ve topla','İki durumda da çarpan sadeleşir ve limit sonlu çıkar; değerler toplanır.','−1 + (−9) = −10')],
 'Kökte payda sıfırsa limitin sonlu olması için pay da sıfır olmalıdır; her kök ayrı bir değer verir.','K-ALM2-03; kök koşullu limit ve parametre',sekil=SK)

#<<SON>>
# ---------------- yaz ----------------
for q_ in P.ANA: q_['kardes']=None
from collections import Counter
tipler={}
for k_ in KART: tipler.setdefault(k_['tipId'],dict(tipId=k_['tipId'],ad=k_['tip'],kartlar=[],uygulamaKonu=UK))['kartlar'].append(k_['id'])
if len(P.ANA)==20:
    json.dump(P.ANA,open(os.path.join(HD,'limitiki-1.json'),'w'),ensure_ascii=False,indent=1)
    json.dump(dict(konu='Limit',surum=2,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT Matematik 2018–2026 çıkmış soruları ve yayın soru bankaları (yalnız mantık), MEB 11–12. sınıf müfredatı.',kartlar=KART,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar','limitiki.json'),'w'),ensure_ascii=False,indent=1)
print(len(P.ANA),'soru · harfler',dict(sorted(Counter(q['cevap']['sik'] for q in P.ANA).items())),'· zorluk',dict(Counter(q['zorluk'] for q in P.ANA)),'· şekilli',sum(1 for q in P.ANA if q.get('sekil')),'· tip',len(tipler))
