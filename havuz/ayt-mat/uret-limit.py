"""AYT Matematik · Limit (süreklilik dahil) · 20 soruluk paket (hafif mod; kardeş yok, ipucu 1).
Tek veri kaynağı: şekil, metin ve çeldirici değerleri aynı verilerden; her cevap/çeldirici sympy/Fraction ile assert edilir."""
import sys,os,json
HD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(HD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
from ortak import *
from cizim import tikz_svg
from _hafif_mat import tablo_svg,mk
import sympy as sp
from fractions import Fraction as Fr
x=sp.symbols('x')
UK='amat|Limit'
P=Parti('limit','Limit',UK,ders='AYT Matematik',idon='aytmat')
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
    mk(P,no,metin=metin,dogru=d,yan=yy,istenen=istenen,ad=ad,sekil=sekil,sira=sira,ip=ip,bilgi=bilgi,puf=puf,tipId=tipId,tip=tip,z=z,alt=alt,kaz=kaz,kalip=kalip,adim=len(ad),kart=f'{kid} ({kart_ozet})')

# ---------------- bilgi kutuları (tanım ve gösterim; örnekler soruların sayılarından farklı) ----------------
B_TEK=B('Tek yönlü limit','x, a’ya soldan yaklaşırken (x → a⁻) f(x)’in yaklaştığı değer sol limit, sağdan yaklaşırken (x → a⁺) yaklaştığı değer sağ limittir. İkisi eşitse limit vardır. Limit, f(a) değerinden bağımsızdır. Örnek: grafikte x = 1’de içi boş nokta (1, 4), içi dolu nokta (1, 0) varsa lim (x→1) f(x) = 4, f(1) = 0’dır')
B_SUR=B('Süreklilik','f, x = a noktasında sürekli ise f(a) tanımlıdır, lim (x→a) f(x) vardır ve bu limit f(a)’ya eşittir. Parçalı fonksiyonda bölünme noktasında sol limit, sağ limit ve fonksiyon değeri eşit olmalıdır. Örnek: x ≤ 1 için 2x, x > 1 için x + k ise 2 = 1 + k olmalıdır')
B_BEL=B('0/0 belirsizliği','pay ve payda aynı noktada sıfır oluyorsa ortak çarpan (x − a) çarpanlara ayırarak ya da köklü ifadede eşlenikle çarpılarak sadeleştirilir; sonra a yerine yazılır. Örnek: lim (x→5) (x² − 25)/(x − 5) = lim (x→5) (x + 5) = 10')
B_ESL=B('Eşlenik','(√A − B) ifadesinin eşleniği (√A + B)’dir ve çarpımları A − B² olur. Örnek: (√x − 3)(√x + 3) = x − 9')
B_INF=B('Sonsuzda limit ve ∞ − ∞','x → −∞ iken √(x²) = |x| = −x olur. ∞ − ∞ belirsizliğinde ifade eşlenikle çarpılıp bölünür. Örnek: x → −∞ iken √(x²) = −x; bu yüzden √(9x²) = −3x’tir')
B_ASM=B('Asimptot','lim (x→a) f(x) = ±∞ ise x = a doğrusu dikey asimptottur; lim (x→±∞) f(x) = b ise y = b doğrusu yatay asimptottur. Pay ve paydadaki ortak çarpan sadeleşirse o noktada dikey asimptot değil, grafikte boşluk oluşur. Örnek: (x − 1)/(x² − 1) için x = −1 dikey asimptot, x = 1 boşluktur')
B_ISR=B('Sonsuz limitte işaret','payın limiti sıfırdan farklı bir sayı, paydanın limiti 0 ise sonuç ±∞’dur; işaret, pay ile paydanın o yandaki işaretinin çarpımından bulunur. Örnek: pay 3, payda x → 2⁺ iken 0⁺ ise limit +∞; x → 2⁻ iken 0⁻ ise limit −∞’dur')
B_OZL=B('Limit işlemleri','limitler varsa toplamın, çarpımın ve bileşkenin limiti; limitlerin toplamı, çarpımı ve bileşkesidir: lim (f + g) = lim f + lim g. Bileşkede dış fonksiyon içerdeki limit noktasında sürekli ise lim g(f(x)) = g(lim f(x)) yazılır. Örnek: lim f = 2 ve lim g = 5 ise lim (f·g) = 10’dur')
B_TRG=B('Trigonometrik limit','x → 0 iken sin(kx)/x → k ve tan(kx)/x → k olur (x radyan). Böylece sin(ax)/sin(bx) → a/b ve sin(ax)/tan(bx) → a/b’dir. Örnek: lim (x→0) sin 6x / (3x) = 2')
B_MUT=B('Mutlak değerli limit','|u| = u (u ≥ 0), |u| = −u (u < 0) tanımıyla bölünme noktasının iki yanı ayrı yazılır. Örnek: |x − 1| ifadesi x > 1 için x − 1, x < 1 için 1 − x’tir')
B_ARA=B('Parçalı fonksiyon','her aralıkta ayrı bir kural uygulanır; limit hesabında yaklaşılan yönün düştüğü aralığın kuralı kullanılır. Örnek: x < 2 için x + 1, x ≥ 2 için 7 − x ise lim (x→2⁻) = 3, lim (x→2⁺) = 5’tir')
B_BIL=B('Bileşke ve limit','lim (x→a) f(f(x)) hesaplanırken önce içteki f(x)’in hangi değere hangi yönden yaklaştığı bulunur; sonra dıştaki f bu değerin o yanındaki limitiyle okunur. Örnek: f(x) → 2⁺ ise dışta f’nin 2’deki sağ limiti alınır')

# ---------------- tip ve kartlar ----------------
tipkayit('lm-grafik','Grafik ve tablodan limit okuma','K-ALM-01'); tipkayit('lm-belirsiz','Belirsizlik giderme','K-ALM-02'); tipkayit('lm-sonsuz','Sonsuzda limit','K-ALM-03')
tipkayit('lm-parca','Mutlak değer ve tek yönlü limit','K-ALM-04'); tipkayit('lm-surekli','Süreklilik ve parametre','K-ALM-05'); tipkayit('lm-ozellik','Limit özellikleri ve yargılar','K-ALM-06')
tipkayit('lm-asimptot','Asimptot ve sonsuz limit','K-ALM-07'); tipkayit('lm-trig','Trigonometrik limit','K-ALM-08'); tipkayit('lm-uygulama','Geometri problemlerinde limit','K-ALM-09')
kart('K-ALM-01','Grafik ve tablodan limit','Sol ve sağ limit grafikten ayrı ayrı okunur; içi dolu ve boş noktalar ayırt edilir; bileşkede iç limitin yaklaşma yönü izlenir.','Limiti fonksiyon değeriyle karıştırmak; yaklaşma yönünü unutmak; bileşkeyi çarpım sanmak.','orta','grafik',3,'lm-grafik','Grafik ve tablodan limit okuma')
kart('K-ALM-02','Belirsizlik giderme','0/0 belirsizliğinde ortak çarpan ya da eşlenik bulunur; sadeleştirdikten sonra değer yazılır.','Belirsizliği 0 sanmak; eşlenik çarpımında işaret ya da kök hatası.','orta','düz',4,'lm-belirsiz','Belirsizlik giderme')
kart('K-ALM-03','Sonsuzda limit','x → −∞ iken kökten çıkan |x| işareti hesaba katılır; ∞ − ∞ eşlenikle 0/0 ya da ∞/∞ biçimine getirilir.','√(x²) = x yazmak; eşlenik paydasındaki iki terimi yanlış toplamak.','zor','düz',5,'lm-sonsuz','Sonsuzda limit')
kart('K-ALM-04','Mutlak değer ve tek yönlü limit','Mutlak değer iki yanda ayrı açılır; tek yönlü limitler hesaplanıp işlem yapılır.','|u| için iki yanı aynı açmak; yalnız tek yönü hesaplamak.','orta','düz',4,'lm-parca','Mutlak değer ve tek yönlü limit')
kart('K-ALM-05','Süreklilik ve parametre','Bölünme noktalarında sol limit, sağ limit ve değer eşitlenir; belirsizlik varsa pay çarpanına ayrılır; çarpımın sürekliliği tek yönlü limitlerle kurulur.','Yalnız bir bölünme noktasını kullanmak; işaret hatası; süreksizlik giderilebilirken boşluğu kök sanmak.','zor','grafik',5,'lm-surekli','Süreklilik ve parametre')
kart('K-ALM-06','Limit özellikleri ve yargılar','Toplam, çarpım ve bileşke limiti ancak limitler varsa yazılır; yargılar grafik ya da tablo verisiyle tek tek sınanır.','Limit varsa fonksiyon değerine eşit sanmak; bileşkeyi değerle hesaplamak; tek yönlü limitlerle iki yanlı limiti karıştırmak.','orta','öncüllü',4,'lm-ozellik','Limit özellikleri ve yargılar')
kart('K-ALM-07','Asimptot ve sonsuz limit','Dikey asimptot paydayı sıfırlayan ve sadeleşmeyen noktadadır; yatay asimptot sonsuzdaki limittir; sonsuz limitte işaret, pay ve paydanın o yandaki işaretinden bulunur.','Sadeleşen noktada asimptot sanmak; işaret tablosunu ters okumak; çift katlı kökte işaret değişimi sanmak.','orta','grafik',4,'lm-asimptot','Asimptot ve sonsuz limit')
kart('K-ALM-08','Trigonometrik limit','sin(ax)/(bx) ve tan(ax)/(bx) türünde limitler a/b olarak bulunur.','Katsayıları çarpmak ya da çıkarmak; oranı ters yazmak.','kolay','düz',2,'lm-trig','Trigonometrik limit')
kart('K-ALM-09','Geometri problemlerinde limit','Geometrik büyüklükler değişkene bağlı yazılır; eşlenik ya da sin x/x limitiyle sonuç bulunur.','Alan formülünde ½ çarpanını unutmak; yarım açıyı unutmak; oranı ters kurmak.','zor','şekilli',5,'lm-uygulama','Geometri problemlerinde limit')

# ---------------- çizim yardımcıları ----------------
CF='blue!70!black'; CG='orange!90!black'; CH='violet'
def fig(body,font='\\small'): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font='+font+']\n'+body+'\n\\end{tikzpicture}')
def graf(x0,x1,y0,y1,s,govde,xs=1,ys=1,xt=None,yt=None,fs_='\\footnotesize'):
    sx=sy=s; o=[]
    for i in range(x0,x1+1): o.append(f'\\draw[gray!35,thin] ({i*sx:.3f},{y0*sy:.3f}) -- ({i*sx:.3f},{y1*sy:.3f});')
    for j in range(y0,y1+1): o.append(f'\\draw[gray!35,thin] ({x0*sx:.3f},{j*sy:.3f}) -- ({x1*sx:.3f},{j*sy:.3f});')
    o.append(f'\\draw[-{{Stealth}},thick] ({(x0-0.3)*sx:.3f},0) -- ({(x1+0.8)*sx:.3f},0) node[right] {{$x$}};')
    o.append(f'\\draw[-{{Stealth}},thick] (0,{(y0-0.3)*sy:.3f}) -- (0,{(y1+0.8)*sy:.3f}) node[above] {{$y$}};')
    for i in range(x0,x1+1,xs):
        if i!=0: o.append(f'\\node[below=2pt,font={fs_},fill=white,inner sep=0.5pt] at ({i*sx:.3f},0) {{${i}$}};')
    for j in range(y0,y1+1,ys):
        if j!=0: o.append(f'\\node[left=2pt,font={fs_},fill=white,inner sep=0.5pt] at (0,{j*sy:.3f}) {{${j}$}};')
    o.append(f'\\node[below right,font={fs_}] at (0,0) {{$O$}};')
    o.append(govde); return '\n'.join(o)
def seg(a,b,s,renk=CF,w='1.7pt'): return f'\\draw[{renk},line width={w}] ({a[0]*s:.3f},{a[1]*s:.3f}) -- ({b[0]*s:.3f},{b[1]*s:.3f});'
def dolu(p,s,renk=CF): return f'\\fill[{renk}] ({p[0]*s:.3f},{p[1]*s:.3f}) circle (0.09);'
def bos(p,s,renk=CF): return f'\\draw[{renk},thick,fill=white] ({p[0]*s:.3f},{p[1]*s:.3f}) circle (0.09);'

# ============ 01 kolay · grafikten limit (kırık çizgi grafik #1) ============
s=0.62
fA=lambda t: 1+t               # [0,2): doğru
fB=lambda t: 5-(t-2)           # (2,4]: (2,5)->(4,3)
fC=lambda t: 3+(t-4)           # [4,6]
f2=1
solL=fA(2); sagL=fB(2); assert (solL,sagL)==(3,5)
v=solL+sagL-f2; assert v==7
e=[solL+sagL+f2,f2+sagL-f2,solL+f2-f2,solL+sagL]; assert e==[9,5,3,8]
g_=[seg((0,1),(2,3),s),seg((2,5),(4,3),s),seg((4,3),(6,5),s),dolu((0,1),s),dolu((2,1),s),bos((2,3),s),bos((2,5),s),dolu((4,3),s),dolu((6,5),s),
    f'\\node[{CF},font=\\small\\bfseries] at ({5.3*s:.2f},{5.7*s:.2f}) {{$y=f(x)$}};']
SK=fig(graf(0,6,0,6,s,'\n'.join(g_)))
Q('0001','lm-grafik','kolay','Grafikten Tek Yönlü Limit','Grafikte sol limit, sağ limit ve fonksiyon değerini ayırt ederek işlem yapar.','grafik',
 'Şekilde, [0, 6] aralığında tanımlı bir f fonksiyonunun grafiği verilmiştir. Doğru parçalarının uçları ızgara çizgilerinin kesişim noktalarındadır; içi dolu nokta grafiğe aittir, içi boş nokta grafiğe ait değildir. Ece, grafikten bazı limit ve fonksiyon değerlerini okuyup bunlarla bir işlem yapacaktır.\nBuna göre, lim (x→2⁻) f(x) + lim (x→2⁺) f(x) − f(2) işleminin sonucu kaçtır?',
 v,
 [(e[0],'f(2) değerini çıkarmak yerine toplamış: 3 + 5 + 1.','islem'),(e[1],'Sol limit yerine f(2) = 1 değerini kullanmış: 1 + 5 − 1.','bilgi'),(e[2],'Sağ limit yerine f(2) = 1 değerini kullanmış: 3 + 1 − 1.','bilgi'),(e[3],'f(2) değerini hiç hesaba katmamış, yalnız iki yan limiti toplamış: 3 + 5.','dikkat')],
 'Sol limit, sağ limit ve f(2) değerinin işlemdeki sonucu.',['Sol limit için grafiğin x = 2’ye soldan yaklaşırken hangi yüksekliğe gittiğine bak; f(2) için ise x = 2’deki içi dolu noktaya bak.'],[B_TEK],
 [A('Sol limiti oku','x = 2’ye soldan yaklaşırken grafik içi boş (2, 3) noktasına yaklaşır.','lim (x→2⁻) f(x) = 3'),A('Sağ limiti oku','Sağdan yaklaşırken grafik içi boş (2, 5) noktasına yaklaşır.','lim (x→2⁺) f(x) = 5'),A('Fonksiyon değerini oku','x = 2’de içi dolu nokta (2, 1)’dir.','f(2) = 1'),A('İşlemi yap','Okunan üç değer işlemde yerine yazılır.','3 + 5 − 1 = 7')],
 'Limit, fonksiyonun o noktadaki değerine değil, noktaya yaklaşırken aldığı değerlere bakar.','K-ALM-01; sol/sağ limit ve f(2) ayrımı',sekil=SK)

# ============ 02 kolay · çarpanlara ayırarak 0/0 ============
ex=(x**3+8)/(x**2-4); v=sp.limit(ex,x,-2); assert v==-3
e=[0, 12/sp.Integer(4), (4-2*2+4)/sp.Integer(-4), (4+4)/sp.Integer(-4)]; e=[int(t) for t in e]; assert e==[0,3,-1,-2] and v not in e
Q('0002','lm-belirsiz','kolay','Çarpanlara Ayırarak Limit','Pay ve paydası aynı noktada sıfır olan rasyonel ifadenin limitini çarpanlara ayırarak bulur.','düz',
 'Bir rasyonel ifadenin değişkeni x = −2 değerine yaklaştırıldığında hem pay hem payda sıfıra gitmektedir; ifade sadeleştirilebilmektedir.\nBuna göre, lim (x→−2) (x³ + 8)/(x² − 4) limitinin değeri kaçtır?',
 -3,[(0,'x = −2’yi doğrudan yazıp payın 0 olduğunu görmüş ve belirsizliği 0 saymış.','dikkat'),(3,'Sadeleştirmeyi doğru yapmış ancak x − 2 ifadesini x = −2’de 4 hesaplayarak işareti kaçırmış: 12/4.','islem'),(-1,'x³ + 8 = (x + 2)(x² + 2x + 4) yazıp ikinci çarpanı x = −2’de 4 bulmuş: 4/(−4).','bilgi'),(-2,'x³ + 8 = (x + 2)(x² + 4) yazıp (−2)² + 4 = 8 hesaplamış: 8/(−4).','bilgi')],
 'Limitin değeri.',['Pay ve paydayı ayrı ayrı çarpanlarına ayırıp hangi çarpanın her ikisinde de bulunduğuna bak.'],[B_BEL,B('Özdeşlikler','x³ + a³ = (x + a)(x² − ax + a²) ve x² − a² = (x − a)(x + a). Örnek: x³ + 27 = (x + 3)(x² − 3x + 9)')],
 [A('Belirsizliği gör','x = −2 yazılınca pay ve payda 0 olur; 0/0 belirsizliği vardır.','(−2)³ + 8 = 0 · (−2)² − 4 = 0'),A('Çarpanlara ayır','Küpler toplamı ve kareler farkı açılır.','(x + 2)(x² − 2x + 4)/((x − 2)(x + 2))'),A('Sadeleştir','Ortak (x + 2) çarpanı kalkar.','(x² − 2x + 4)/(x − 2)'),A('Değeri yaz','x = −2 yazılır.','(4 + 4 + 4)/(−4) = −3')],
 'Pay ve paydayı sıfırlayan değer, ikisinde de ortak çarpan olarak bulunur.','K-ALM-02; küpler toplamı içeren 0/0')

# ============ 03 kolay · tablodan limit (tablo #1) ============
f3=lambda t:3*t+1
xs3=['0,9','0,99','0,999','1','1,001','1,01','1,1']; vv=[Fr(9,10),Fr(99,100),Fr(999,1000),None,Fr(1001,1000),Fr(101,100),Fr(11,10)]
fv=[f3(t) if t is not None else 7 for t in vv]
def dstr(t):
    t=Fr(t); s=f'{float(t):.4f}'.rstrip('0').rstrip('.'); return s.replace('.',',')
SK=tablo_svg(['x']+xs3,[['f(x)']+[dstr(t) for t in fv]])
assert [dstr(t) for t in fv]==['3,7','3,97','3,997','7','4,003','4,03','4,3']
lim3=sp.limit(3*x+1,x,1); assert lim3==4
v=lim3-7; assert v==-3
e=[7-7,4+7,3-7,7-4]; assert e==[0,11,-4,3] and v not in e
Q('0003','lm-grafik','kolay','Tablodan Limit','Fonksiyon değer tablosundaki eğilimden limiti belirler ve fonksiyon değeriyle karşılaştırır.','tablo',
 'Aşağıdaki tabloda, gerçel sayılar kümesinde tanımlı bir f fonksiyonunun x = 1 noktasının yakınındaki bazı değerleri verilmiştir. x değeri 1’e iki yandan da yaklaştıkça f(x) değerlerinin tabloda görülen eğilimi sürdürdüğü bilinmektedir.\nBuna göre, lim (x→1) f(x) − f(1) farkı kaçtır?',
 v,[(e[0],'Limitin f(1) değerine eşit olduğunu sanmış: 7 − 7.','bilgi'),(e[1],'Limiti 4 bulmuş, ancak farkı toplama çevirmiş: 4 + 7.','islem'),(e[2],'3,997 değerinin tam kısmını alıp limiti 3 sanmış: 3 − 7.','dikkat'),(e[3],'Limit ile fonksiyon değerinin sırasını ters kurmuş: 7 − 4.','islem')],
 'Limit ile fonksiyon değerinin farkı.',['Tabloda x, 1’e her iki yandan yaklaşırken f(x)’in hangi sayıya yaklaştığına bak; f(1) değeri ayrı bir sütunda.'],[B_TEK],
 [A('Soldan yaklaş','x = 0,9; 0,99; 0,999 için f(x) 3,7; 3,97; 3,997 olur ve 4’e yaklaşır.','sol limit = 4'),A('Sağdan yaklaş','x = 1,001; 1,01; 1,1 için f(x) 4,003; 4,03; 4,3 olur ve 4’e yaklaşır.','sağ limit = 4'),A('Limiti belirle','İki yan limit eşit olduğundan limit 4’tür; f(1) = 7 tablodan okunur.','lim (x→1) f(x) = 4 · f(1) = 7'),A('Farkı bul','Limitten fonksiyon değeri çıkarılır.','4 − 7 = −3')],
 'Limit, noktaya yaklaşırken değerlerin gittiği sayıdır; noktadaki değer farklı olabilir.','K-ALM-01; değer tablosundan limit',sekil=SK)

# ============ 04 kolay · trigonometrik limit ============
a4,b4=8,2
v=sp.limit(sp.sin(a4*x)/sp.tan(b4*x),x,0); assert v==4
e=[a4+b4,a4,a4*b4,a4-b4]; assert e==[10,8,16,6] and v not in e
Q('0004','lm-trig','kolay','Trigonometrik Limit','sin(ax)/tan(bx) türündeki limiti a/b olarak hesaplar.','düz',
 'x radyan cinsinden bir açının ölçüsü olmak üzere, x değeri sıfıra yaklaşırken sinüs ve tanjant ifadelerinin oranı bir sayıya yaklaşmaktadır.\nBuna göre, lim (x→0) sin 8x / tan 2x limitinin değeri kaçtır?',
 4,[(16,'Pay ve payda limitlerini 8 ve 2 bulup çarpmış: 8 × 2.','islem'),(6,'Pay ve payda katsayılarını çıkarmış: 8 − 2.','islem'),(10,'Pay ve payda katsayılarını toplamış: 8 + 2.','islem'),(8,'Paydadaki tan 2x’in katsayısını unutup yalnız sin 8x/x → 8 almış.','dikkat')],
 'Limitin değeri.',['Pay ve paydayı ayrı ayrı x ile bölüp her birinin limitine bak.'],[B_TRG],
 [A('Pay ve paydayı x’e böl','Her iki terim x ile bölünür.','(sin 8x / x)/(tan 2x / x)'),A('Limitleri yaz','sin(kx)/x ve tan(kx)/x limitleri k’dir.','8/2'),A('Sonucu bul','Oran hesaplanır.','8 ÷ 2 = 4')],
 'sin(ax) ile tan(bx) oranı x → 0 iken a/b’ye gider.','K-ALM-08; sinüs/tanjant oranı')

# ============ 05 orta · tablo ile verilen parçalı fonksiyonda süreklilik (tablo #2) ============
aa,bb=sp.symbols('a b')
c1=sp.Eq(aa*1+2,1**2+bb); c2=sp.Eq(3**2+bb,3*3-4)
sol=sp.solve([c1,c2],[aa,bb]); assert sol=={aa:-5,bb:-4}; a5,b5=-5,-4; v=a5*b5; assert v==20
assert (b5-2)*b5==24
e=[a5+b5,(b5-2)*b5,-20,b5-a5]; assert e==[-9,24,-20,1] and v not in e
SK=tablo_svg(['x aralığı','f(x)'],[['x ≤ 1','ax + 2'],['1 < x ≤ 3','x² + b'],['x > 3','3x − 4']])
Q('0005','lm-surekli','orta','İki Parametreli Süreklilik','Üç parçalı fonksiyonun gerçel sayılarda sürekli olması için bölünme noktalarında eşitlik kurup parametreleri bulur.','tablo',
 'a ve b gerçel sayılar olmak üzere, gerçel sayılar kümesi üzerinde tanımlı f fonksiyonunun kuralı aşağıdaki tabloda verilmiştir. f fonksiyonu gerçel sayılar kümesi üzerinde süreklidir.\nBuna göre, a · b çarpımı kaçtır?',
 v,[(e[0],'a = −5 ve b = −4 değerlerini doğru bulmuş, ancak çarpım yerine toplamlarını yazmış.','islem'),(e[1],'x = 1 eşitliğinde (1)² terimini unutup a + 2 = b yazmış: a = −6, b = −4 bulmuş.','islem'),(e[2],'a + 2 = 1 + b eşitliğinde a’yı 5 bulup işaret hatasıyla a = 5 almış: 5 × (−4) = −20.','islem'),(e[3],'Doğru değerleri bulmuş, ancak çarpım yerine b − a farkını yazmış.','dikkat')],
 'a ile b’nin çarpımı.',['Sürekliliğin gerektirdiği eşitliği hangi noktalarda kurman gerektiğini tablodaki aralık sınırlarından belirle.'],[B_SUR],
 [A('Bölünme noktalarını bul','Kural x = 1 ve x = 3 noktalarında değişir; süreklilik için ikisinde eşitlik gerekir.','x = 1 ve x = 3'),A('x = 3’te eşitle','Soldan x² + b, sağdan 3x − 4 değeri eşitlenir.','9 + b = 5 → b = −4'),A('x = 1’de eşitle','Soldan a + 2, sağdan 1 + b değeri eşitlenir.','a + 2 = 1 + (−4) → a = −5'),A('Çarpımı yaz','a ve b çarpılır.','(−5) × (−4) = 20')],
 'Parçalı fonksiyonda her bölünme noktası için soldan, sağdan ve değer olmak üzere bir eşitlik yazılır.','K-ALM-05; üç parçalı fonksiyon',sekil=SK)

# ============ 06 orta · grafikten f(f(x)) limiti (kırık çizgi grafik #2) ============
s=0.62
P6=dict(A=((0,1),(3,4)),B=((3,2),(4,5)),C=((4,3),(6,5)))
fq=lambda t: (1+t if t<3 else (2+3*(t-3) if t<4 else (3+(t-4) if t>4 else 2)))
assert fq(3)==2 and fq(4)==2 and fq(0)==1 and fq(2)==3
inner=4                                      # lim x->3- f(x)
v=5                                           # lim y->4- f(y): B parçası 3y-7
assert 3*4-7==5 and fq(3.999999)>4.99 and fq(4.000001)<3.01
e=[fq(4),fq(fq(3)),inner,inner**2]; assert e==[2,3,4,16] and v not in e
g_=[seg((0,1),(3,4),s),seg((3,2),(4,5),s),seg((4,3),(6,5),s),dolu((0,1),s),bos((3,4),s),dolu((3,2),s),bos((4,5),s),dolu((4,2),s),bos((4,3),s),dolu((6,5),s),
    f'\\node[{CF},font=\\small\\bfseries] at ({5.4*s:.2f},{5.75*s:.2f}) {{$y=f(x)$}};']
SK=fig(graf(0,6,0,6,s,'\n'.join(g_)))
Q('0006','lm-grafik','orta','Bileşke Fonksiyonun Limiti','Grafik yardımıyla iç fonksiyonun yaklaşma yönünü belirleyip bileşke fonksiyonun tek yönlü limitini bulur.','grafik',
 'Şekilde, [0, 6] aralığında tanımlı f fonksiyonunun grafiği verilmiştir. Doğru parçalarının uçları ızgara çizgilerinin kesişim noktalarındadır; içi dolu nokta grafiğe ait, içi boş nokta grafiğe ait değildir.\nBuna göre, lim (x→3⁻) f(f(x)) limitinin değeri kaçtır?',
 v,[(e[0],'İç limiti 4 bulmuş, sonra dış fonksiyonun 4’teki değerini okumuş: f(4) = 2.','bilgi'),(e[1],'Limit yerine x = 3 yazıp f(f(3)) = f(2) = 3 bulmuş.','bilgi'),(e[2],'Yalnız içteki f(x)’in limitini bulup dışta f almayı unutmuş.','dikkat'),(e[3],'Bileşke yerine çarpım düşünüp lim f(x) · lim f(x) = 4 × 4 yazmış.','bilgi')],
 'Bileşke fonksiyonun x → 3⁻ iken limiti.',['Önce x, 3’e soldan yaklaşırken f(x)’in hangi değere hangi yönden yaklaştığını bul; sonra dıştaki f’yi bu yönde oku.'],[B_BIL],
 [A('İç limiti bul','x, 3’e soldan yaklaşırken f(x), 4’e küçük değerlerden yaklaşır.','lim (x→3⁻) f(x) = 4⁻'),A('Dış fonksiyonu oku','y, 4’e soldan yaklaşırken grafik (3, 2) ile (4, 5) arasındaki parçada içi boş (4, 5) noktasına gider.','lim (y→4⁻) f(y) = 5'),A('Sonucu yaz','Bileşkenin limiti dış limite eşittir.','lim (x→3⁻) f(f(x)) = 5')],
 'Bileşkede önce içteki fonksiyonun hangi yönden yaklaştığını bul, sonra dıştakini o yönde oku.','K-ALM-01; bileşkenin tek yönlü limiti',sekil=SK)

# ============ 07 orta · iki grafik, öncüllü (kırık çizgi grafik #3) ============
s=0.8
fa=lambda t:t+1; ga=lambda t:4-t
lf=sp.limit(x+1,x,2); lg=sp.limit(4-x,x,2); assert (lf,lg)==(3,2)
I7=False                                   # f x=2'de sürekli değil (f(2)=1 ≠ 3)
II7=(lf+lg==5)                             # lim (f+g) = 5
III7=(ga(lf)==1)                           # lim g(f(x)) = g(3) = 1
assert (I7,II7,III7)==(False,True,True)
assert sp.limit(4-(x+1),x,2)==1 and 1+ga(2)==3 and ga(1)==3 and fa(2)-1==2
sira7=['Yalnız I','Yalnız II','I ve II','II ve III','I, II ve III']
g_=[seg((0,1),(4,5),s),seg((0,4),(4,0),s,CG),bos((2,3),s),dolu((2,1),s),dolu((2,2),s,CG),
    f'\\node[{CF},font=\\small\\bfseries] at ({3.6*s:.2f},{5.55*s:.2f}) {{$f$}};\\node[{CG},font=\\small\\bfseries] at ({0.4*s:.2f},{4.45*s:.2f}) {{$g$}};']
SK=fig(graf(0,4,0,5,s,'\n'.join(g_)))
Q('0007','lm-ozellik','orta','Limit Özellikleri ve Süreklilik','İki fonksiyonun grafiğinden toplamın ve bileşkenin limitini okuyup süreklilik yargılarını değerlendirir.','öncüllü',
 'Şekilde, gerçel sayılar kümesi üzerinde tanımlı f (mavi) ve g (turuncu) fonksiyonlarının grafikleri verilmiştir. f’nin grafiğinde x = 2’de içi boş bir nokta ve içi dolu bir nokta vardır; g’nin grafiği doğrusal ve kesiksizdir. Noktalar ızgara çizgilerinin kesişimindedir.\nBuna göre,\nI. f fonksiyonu x = 2 noktasında süreklidir.\nII. lim (x→2) (f(x) + g(x)) = 5’tir.\nIII. lim (x→2) g(f(x)) = 1’dir.\nifadelerinden hangileri doğrudur?',
 'II ve III',[('Yalnız I','Grafikteki içi dolu noktayı görüp f’yi sürekli sanmış (I); II ve III’ü değerlerle sınamış: f(2) + g(2) = 3 ile g(f(2)) = g(1) = 3 çıkınca ikisini yanlış bulmuş.','bilgi'),('Yalnız II','III’ü limit yerine değerle hesaplayıp g(f(2)) = g(1) = 3 bulmuş ve yanlış saymış; I’i doğru bulmamış.','bilgi'),('I ve II','f’yi sürekli sanmış (I doğru); III’te f(2) = 1 yazıp g(1) = 3 hesaplayarak III’ü yanlış bulmuş.','bilgi'),('I, II ve III','I’i de doğru saymış: x = 2’deki içi dolu noktanın limit ile aynı yükseklikte olduğunu düşünmüş.','dikkat')],
 'Üç yargının doğru olanları.',['x = 2’de f’nin limitini ve f(2) değerini ayrı ayrı oku; g’nin kesiksiz olduğunu bileşkede kullan.'],[B_TEK,B_OZL],
 [A('I’i sına','lim f(x) = 3 iken f(2) = 1’dir; limit ve değer farklı olduğundan f, x = 2’de sürekli değildir.','lim (x→2) f = 3 · f(2) = 1 → I yanlış'),A('II’yi sına','Limitlerin toplamı alınır: f için 3, g için 2.','3 + 2 = 5 → II doğru'),A('III’ü sına','x → 2 iken f(x) → 3 olur; g, 3’te süreklidir ve g(3) = 1’dir.','lim g(f(x)) = g(3) = 1 → III doğru'),A('Sonucu yaz','II ve III doğrudur.','II ve III')],
 'Bileşkenin limitinde dıştaki fonksiyon, içteki limit değerinde sürekliyse değer olarak okunur; içteki fonksiyonun o noktadaki değeri kullanılmaz.','K-ALM-06; iki grafik ve üç yargı',sekil=SK,sira=sira7)

# ============ 08 orta · eşlenikle belirsizlik ============
ex=(sp.sqrt(x+14)-4)/(x-2); v=sp.limit(ex,x,2); assert v==sp.Rational(1,8)
e=[0,Fr(1,16),Fr(1,6),Fr(1,4)]
assert 1/(sp.sqrt(16)+4)==sp.Rational(1,8) and Fr(1,4*4)==Fr(1,16) and Fr(1,2+4)==Fr(1,6) and Fr(1,4)==Fr(1,4)
Q('0008','lm-belirsiz','orta','Eşlenikle Limit','Köklü ifadede 0/0 belirsizliğini eşlenikle gidererek limiti hesaplar.','düz',
 'Bir köklü ifadenin payı da paydası da x = 2 değerine yaklaşırken sıfıra gitmektedir.\nBuna göre, lim (x→2) (√(x + 14) − 4)/(x − 2) limitinin değeri kaçtır?',
 Fr(1,8),[(0,'x = 2’yi doğrudan yazıp √16 − 4 = 0 bulmuş ve belirsizliği 0 saymış.','dikkat'),(Fr(1,16),'Eşlenik çarpımından sonra paydadaki ifadeyi 4 × 4 = 16 almış.','islem'),(Fr(1,6),'√16 değerini 2 hesaplayıp eşlenik toplamını 2 + 4 = 6 bulmuş.','islem'),(Fr(1,4),'Eşlenik toplamında kök terimini atlayıp yalnız 4’ü almış.','dikkat')],
 'Limitin değeri.',['Payı, eşleniğiyle çarparak kökten kurtarmayı dene.'],[B_BEL,B_ESL],
 [A('Eşlenikle çarp','Pay ve paydayı √(x + 14) + 4 ile çarp.','(x + 14 − 16)/((x − 2)(√(x + 14) + 4))'),A('Payı sadeleştir','Pay x − 2 olur ve paydadaki x − 2 ile kısalır.','1/(√(x + 14) + 4)'),A('Değeri yaz','x = 2 için √16 = 4 olur.','1/(4 + 4) = 1/8')],
 'Karekökün farkı içeren 0/0 belirsizliğinde eşlenikle çarpmak payı sadeleşen düz bir ifadeye çevirir.','K-ALM-02; kare kök içeren 0/0')

# ============ 09 orta · asimptotlardan fonksiyon (rasyonel grafik #1) ============
s=0.55
a9,b9,c9=2,3,1
fr=lambda t:Fr(a9*t+b9,t+c9)
assert fr(0)==3 and fr(-2)==1 and sp.limit((2*x+3)/(x+1),x,sp.oo)==2
v=a9+b9+c9; assert v==6
# çeldirici zincirleri
toplam=lambda a,b,c:a+b+c
e1=toplam(2,3*(-1),-1); e2=toplam(1,3,1); b_e3=1+4; e3=toplam(2,b_e3,1); e4=b9+c9
assert (-4+b_e3)==1*1 and (-4+b9)==(-1)*1 and 3*(-1)==-3
e=[e1,e2,e3,e4]; assert e==[-2,5,8,4] and v not in e
cl=lambda y0,y1:f'\\clip ({-4*s:.3f},{-3*s:.3f}) rectangle ({4*s:.3f},{6*s:.3f});'
curve=(f'\\begin{{scope}}\\clip ({-4*s:.3f},{-3*s:.3f}) rectangle ({4*s:.3f},{6*s:.3f});\n'
       f'\\draw[{CF},line width=1.7pt,samples=120,domain=-4:-1.12] plot ({{\\x*{s}}},{{(2*\\x+3)/(\\x+1)*{s}}});\n'
       f'\\draw[{CF},line width=1.7pt,samples=120,domain=-0.88:4] plot ({{\\x*{s}}},{{(2*\\x+3)/(\\x+1)*{s}}});\\end{{scope}}\n'
       f'\\draw[dashed,thick,{CG}] ({-1*s:.3f},{-3*s:.3f}) -- ({-1*s:.3f},{6*s:.3f});\\draw[dashed,thick,{CG}] ({-4*s:.3f},{2*s:.3f}) -- ({4*s:.3f},{2*s:.3f});\n'
       f'{dolu((0,3),s)}{dolu((-2,1),s)}\\node[{CF},font=\\small\\bfseries] at ({3.3*s:.2f},{3.6*s:.2f}) {{$y=f(x)$}};')
SK=fig(graf(-4,4,-3,6,s,curve))
Q('0009','lm-asimptot','orta','Asimptotlardan Fonksiyon Bulma','Grafikteki dikey ve yatay asimptotlardan ve işaretli noktadan rasyonel fonksiyonun katsayılarını bulur.','grafik',
 'a, b ve c birer gerçel sayı olmak üzere f(x) = (ax + b)/(x + c) fonksiyonunun grafiği şekilde verilmiştir. Grafiğin asimptotları turuncu kesikli doğrularla gösterilmiş, grafik üzerindeki işaretli noktalar ızgara çizgilerinin kesişimindedir.\nBuna göre, a + b + c toplamı kaçtır?',
 v,[(e[0],'Dikey asimptotu x = −1 olduğundan c = −1 almış; işaretli noktadan b = 3c = −3 bulmuş.','islem'),(e[1],'Yatay asimptot ile a’nın ilişkisini kullanmayıp a = 1 almış; b = 3 ve c = 1 bulmuş.','bilgi'),(e[2],'(−2, 1) noktasında paydayı −2 + 1 = −1 yerine 1 hesaplayıp b = 5 bulmuş.','islem'),(e[3],'a’yı toplama katmamış: b + c.','dikkat')],
 'a + b + c toplamı.',['Önce asimptotlardan a ve c’yi, sonra işaretli noktalardan birinden b’yi belirle.'],[B_ASM],
 [A('Dikey asimptottan c','Payda x + c, x = −1’de sıfır olur.','x + c = 0 → c = 1'),A('Yatay asimptottan a','x → ∞ iken f(x) → a olur; yatay asimptot y = 2’dir.','a = 2'),A('İşaretli noktadan b','(0, 3) grafik üzerindedir: f(0) = b/c.','b/1 = 3 → b = 3'),A('Kontrol et ve topla','(−2, 1) noktası da sağlanır; sonra katsayılar toplanır.','f(−2) = (−4 + 3)/(−2 + 1) = 1 · a + b + c = 2 + 3 + 1 = 6')],
 'Rasyonel fonksiyonun asimptotları, payda sıfırlayan değerden ve baş katsayıların oranından okunur.','K-ALM-07; rasyonel grafikten katsayı bulma',sekil=SK)

# ============ 10 zor · x→−∞ iken ∞ − ∞ ============
av=sp.symbols('a')
lim_=sp.limit(sp.sqrt(4*x**2-12*x)+2*x,x,-sp.oo); assert lim_==3
v=-12
# genel: x->-oo, sqrt(4x^2+ax)+2x -> -a/4
for t in (-12,4,-8): assert sp.limit(sp.sqrt(4*x**2+t*x)+2*x,x,-sp.oo)==sp.Rational(-t,4)
e=[-18,-6,6,12]; assert Fr(-3*6)==-18 and Fr(-6,2)*-1==3 and Fr(6,2)==3 and Fr(12,4)==3 and all(sp.Rational(-t,k)==3 for t,k in ((-18,6),(-6,2))) and v not in e
Q('0010','lm-sonsuz','zor','Eksi Sonsuzda Limit','x → −∞ iken kök içeren ∞ − ∞ belirsizliğinde parametreyi, mutlak değerin işaretini dikkate alarak bulur.','düz',
 'a bir gerçel sayı olmak üzere, x gerçel sayılar kümesinde eksi sonsuza giderken √(4x² + ax) + 2x ifadesi tanımlıdır ve bu ifade bir gerçel sayıya yaklaşmaktadır.\nlim (x→−∞) (√(4x² + ax) + 2x) = 3 olduğuna göre, a kaçtır?',
  v,[(-18,'√(4x²) değerini 4|x| = −4x alıp paydayı −4x − 2x = −6x bulmuş: −a/6 = 3.','islem'),(-6,'Paydadaki iki terimden birini atlayıp √(4 + a/x) + 2 yerine yalnız 2 almış: −a/2 = 3.','dikkat'),(6,'Paydada bir terimi atlamış ve işareti de ters almış: a/2 = 3.','islem'),(12,'Paydadaki −x çarpanında eksi işaretini düşürüp ax/(x · 4) = a/4 yazmış: a/4 = 3.','dikkat')],
 'a değeri.',['Eşlenikle çarptıktan sonra paydada kalan terimlerin x → −∞ iken davranışına bak.'],[B_INF,B_ESL],
 [A('Eşlenikle çarp','Pay ve paydayı √(4x² + ax) − 2x ile çarp.','(4x² + ax − 4x²)/(√(4x² + ax) − 2x)'),A('Kökü düzenle','x < 0 olduğundan √(4x²) = −2x’tir; kökten x çıkarılır.','√(4x² + ax) = −x√(4 + a/x)'),A('Paydayı sadeleştir','x → −∞ iken a/x → 0 olur; payda x(−√(4 + a/x) − 2) biçimindedir.','ax/(−x(√(4 + a/x) + 2)) = −a/(√(4 + a/x) + 2)'),A('Limiti al','a/x → 0 yazılır.','−a/(2 + 2) = −a/4'),A('Denklemi çöz','Limit 3’e eşitlenir.','−a/4 = 3 → a = −12')],
 'Kökten dışarı çıkan ifadelerin işaretine, değişkenin hangi yöne gittiğine bakarak karar ver.','K-ALM-03; eksi sonsuzda eşlenikli limit')

# ============ 11 orta · tablo, limit işlemleri (tablo #3) ============
fL,fR,fV=5,5,2; gL,gR,gV=1,3,3
SK=tablo_svg(['','f','g'],[['x → 3⁻ iken limit',str(fL),str(gL)],['x → 3⁺ iken limit',str(fR),str(gR)],['x = 3 için değer',str(fV),str(gV)]])
v=fR*gR-(fL+gL); assert v==9
e=[fV*gV-(fV+gV),fL*gL-(fR+gR),fV*gR-(fV+gL),fR*gR-(fR+gR)]; assert e==[1,-3,3,7] and v not in e
Q('0011','lm-ozellik','orta','Tek Yönlü Limit İşlemleri','Tabloda verilen tek yönlü limitlerle çarpım ve toplamın limitini hesaplar.','tablo',
 'f ve g fonksiyonlarının x = 3 noktasındaki sol limitleri, sağ limitleri ve fonksiyon değerleri aşağıdaki tabloda verilmiştir. Her iki fonksiyonun da bu noktanın iki yanındaki limitleri vardır.\nBuna göre, lim (x→3⁺) f(x) · g(x) − lim (x→3⁻) (f(x) + g(x)) işleminin sonucu kaçtır?',
 v,[(e[0],'Limitler yerine fonksiyon değerlerini kullanmış: f(3) · g(3) − (f(3) + g(3)).','bilgi'),(e[1],'İki terimde yönleri karıştırmış: birinci terimde sol, ikinci terimde sağ limitleri almış.','dikkat'),(e[2],'f için limit yerine f(3) = 2 değerini yazmış, g için limitleri doğru okumuş: 2 · 3 − (2 + 1).','bilgi'),(e[3],'İkinci terimde de sağ limitleri kullanmış: 15 − (5 + 3).','dikkat')],
 'İfadenin değeri.',['Her terimde hangi yönden yaklaşıldığına bak ve tabloda o yönün satırını kullan.'],[B_TEK,B_OZL],
 [A('Birinci terim','Sağ limitler çarpılır.','5 × 3 = 15'),A('İkinci terim','Sol limitler toplanır.','5 + 1 = 6'),A('Farkı bul','Birinci terimden ikinciyi çıkar.','15 − 6 = 9')],
 'Çarpım ve toplamın limiti, aynı yönden alınan limitlerin çarpımı ve toplamıdır.','K-ALM-06; tek yönlü limit tablosu',sekil=SK)

# ============ 12 orta · mutlak değerli ifadede tek yönlü limitler ============
fexp=(x**2-5*x+6)/sp.Abs(x-3)
lp=sp.limit(fexp,x,3,'+'); lm=sp.limit(fexp,x,3,'-'); assert (lp,lm)==(1,-1)
v=lp-lm; assert v==2
e=[lp+lm,lm-lp,lp,lm]; assert e==[0,-2,1,-1] and v not in e
Q('0012','lm-parca','orta','Mutlak Değerli İfadenin Limiti','Mutlak değeri bölünme noktasının iki yanında ayrı açarak tek yönlü limitleri bulur.','düz',
 'f(x) = (x² − 5x + 6)/|x − 3| kuralıyla gerçel sayılarda 3’ten farklı her noktada tanımlı f fonksiyonunun, x = 3 noktasında sağdan ve soldan limitleri vardır.\nBuna göre, lim (x→3⁺) f(x) − lim (x→3⁻) f(x) farkı kaçtır?',
 v,[(e[0],'İki yan limiti toplamış: 1 + (−1).','islem'),(e[1],'Çıkarmayı ters sırada yapmış: (−1) − 1.','islem'),(e[2],'Yalnız sağ limiti hesaplayıp sol limiti 0 saymış.','dikkat'),(e[3],'Yalnız sol limiti hesaplayıp sağ limiti 0 saymış.','dikkat')],
 'Sağ limit ile sol limitin farkı.',['Mutlak değerin içi x = 3’ün sağında ve solunda hangi işareti alıyor?'],[B_MUT,B_TEK],
 [A('Payı çarpanla','x² − 5x + 6 ifadesi çarpanlarına ayrılır.','(x − 2)(x − 3)'),A('Sağ limit','x > 3 iken |x − 3| = x − 3 olur ve ifade x − 2’ye sadeleşir.','lim (x→3⁺) (x − 2) = 1'),A('Sol limit','x < 3 iken |x − 3| = −(x − 3) olur ve ifade −(x − 2)’ye sadeleşir.','lim (x→3⁻) −(x − 2) = −1'),A('Farkı bul','Sağ limitten sol limit çıkarılır.','1 − (−1) = 2')],
 'Mutlak değerli ifade bölünme noktasının iki yanında ayrı kural kullandığından tek yönlü limitler birbirinden farklı çıkabilir.','K-ALM-04; mutlak değerli rasyonel ifade')

# ============ 13 zor · grafik + süreklilik, 0/0 (kırık çizgi grafik #4) ============
s=0.5
a13,b13=sp.symbols('a b'); k=sp.symbols('k')
sol=sp.solve([sp.Eq(4+2*a13+b13,0),sp.Eq(4+a13,7)],[a13,b13]); assert sol=={a13:3,b13:-10}
a_,b_=3,-10; v=a_*b_; assert v==-30 and sp.limit((x**2+3*x-10)/(x-2),x,2)==7
# çeldirici zincirleri
k_wrong=7; ea=k_wrong-2; eb=-2*k_wrong; e1=ea*eb
e2=a_+b_; e3=a_-b_; e4=a_*(2*5)
e=[e1,e2,e3,e4]; assert e==[-70,-7,13,30] and v not in e
g_=[seg((-2,-1),(2,7),s),dolu((-2,-1),s),dolu((-1,1),s),dolu((0,3),s),dolu((2,7),s),f'\\node[{CF},font=\\small\\bfseries] at ({3.0*s:.2f},{4.2*s:.2f}) {{$y=f(x)$}};']
SK=fig(graf(-2,4,-1,8,s,'\n'.join(g_)))
Q('0013','lm-surekli','zor','Grafik ve Cebirle Süreklilik','Grafikte verilen parçadan bölünme noktasındaki değeri okuyup 0/0 belirsizliği içeren parçada parametreleri süreklilikle bulur.','grafik',
 'Gerçel sayılar kümesi üzerinde sürekli bir f fonksiyonunun x ≤ 2 için grafiğinin bir parçası şekilde verilmiştir; bu parça bir doğru parçasıdır ve işaretli noktalar ızgara çizgilerinin kesişimindedir. a ve b gerçel sayılar olmak üzere x > 2 için f(x) = (x² + ax + b)/(x − 2) kuralıyla tanımlıdır.\nBuna göre, a · b çarpımı kaçtır?',
 v,[(e[0],'Sadeleşmiş ifadeyi (x − 2)(x + k) yazıp limiti x’e 2 koymadan k = 7 almış: a = 5, b = −14.','islem'),(e[1],'a = 3 ve b = −10 değerlerini bulmuş, ancak çarpım yerine toplamını yazmış.','dikkat'),(e[2],'Değerleri doğru bulmuş, ancak çarpım yerine a − b farkını yazmış.','dikkat'),(e[3],'b’yi −2k yerine +2k alıp işaret hatasıyla b = 10 bulmuş: 3 × 10.','islem')],
 'a ile b’nin çarpımı.',['Grafikten x = 2’deki değeri oku; sağdan limitin bu değere eşit olması için pay x = 2’de ne olmalı?'],[B_SUR,B_BEL],
 [A('Grafikten değeri oku','Doğru parçası (2, 7) noktasında biter ve nokta grafiğe aittir.','f(2) = 7'),A('Süreklilik koşulu','Sağdan limit de 7 olmalıdır; paydası 0’a giden ifadenin limitinin sayı olması için pay x = 2’de sıfır olmalıdır.','4 + 2a + b = 0'),A('Payı çarpanla','Pay, (x − 2) çarpanını içerir; diğer çarpan x + k alınır.','x² + ax + b = (x − 2)(x + k)'),A('Limiti kur','Sadeleştikten sonra x = 2 yazılır ve 7’ye eşitlenir.','2 + k = 7 → k = 5'),A('Katsayıları bul','Çarpanlar açılır.','x² + 3x − 10 → a = 3, b = −10'),A('Çarpımı yaz','a ve b çarpılır.','3 × (−10) = −30')],
 'Paydası sıfıra giden ifadenin limiti sayı ise pay da aynı noktada sıfırdır; çarpanlara ayırıp sadeleştirerek devam edilir.','K-ALM-05; grafik + 0/0 parçalı süreklilik',sekil=SK)

# ============ 14 orta · rasyonel grafik, öncüllü (rasyonel grafik #2) ============
s=0.5
ff=lambda t:sp.Rational(2)*t**2/(t**2-1)
fx_=2*x**2/(x**2-1)
assert sp.limit(fx_,x,sp.oo)==2 and sp.limit(fx_,x,1,'-')==-sp.oo and sp.limit(fx_,x,-1,'-')==sp.oo and sp.limit(fx_,x,-1,'+')==-sp.oo and sp.limit(fx_,x,1,'+')==sp.oo
sira14=['Yalnız I','Yalnız III','I ve II','I ve III','I, II ve III']
assert (sp.limit(fx_,x,sp.oo)==2,sp.limit(fx_,x,1,'-')==sp.oo,sp.limit(fx_,x,-1,'-')==-sp.oo)==(True,False,False)
curve=(f'\\begin{{scope}}\\clip ({-4*s:.3f},{-4*s:.3f}) rectangle ({4*s:.3f},{6*s:.3f});\n'
       f'\\draw[{CF},line width=1.7pt,samples=140,domain=-4:-1.05] plot ({{\\x*{s}}},{{2*\\x*\\x/(\\x*\\x-1)*{s}}});\n'
       f'\\draw[{CF},line width=1.7pt,samples=140,domain=1.05:4] plot ({{\\x*{s}}},{{2*\\x*\\x/(\\x*\\x-1)*{s}}});\n'
       f'\\draw[{CF},line width=1.7pt,samples=200,domain=-0.93:0.93] plot ({{\\x*{s}}},{{2*\\x*\\x/(\\x*\\x-1)*{s}}});\\end{{scope}}\n'
       f'\\draw[dashed,thick,{CG}] ({-1*s:.3f},{-4*s:.3f}) -- ({-1*s:.3f},{6*s:.3f});\\draw[dashed,thick,{CG}] ({1*s:.3f},{-4*s:.3f}) -- ({1*s:.3f},{6*s:.3f});\\draw[dashed,thick,{CG}] ({-4*s:.3f},{2*s:.3f}) -- ({4*s:.3f},{2*s:.3f});\n'
       f'{dolu((0,0),s)}\\node[{CF},font=\\small\\bfseries] at ({3.2*s:.2f},{4.4*s:.2f}) {{$y=f(x)$}};')
SK=fig(graf(-4,4,-4,6,s,curve))
Q('0014','lm-asimptot','orta','Grafikte Sonsuz Limit','Grafikteki asimptotlardan sonsuzdaki limiti ve dikey asimptot komşuluğundaki sonsuz limitleri yorumlar.','öncüllü',
 'Şekilde, gerçel sayılarda 1 ve −1 dışındaki her noktada tanımlı bir f fonksiyonunun grafiği ve asimptotları (turuncu kesikli doğrular) verilmiştir. Grafik, asimptotlara sınırsızca yaklaşmaktadır.\nBuna göre,\nI. lim (x→∞) f(x) = 2’dir.\nII. lim (x→1⁻) f(x) = +∞’dur.\nIII. lim (x→−1⁻) f(x) = −∞’dur.\nifadelerinden hangileri doğrudur?',
 'Yalnız I',[('Yalnız III','Sağdaki kolun x → ∞ iken 0’a indiğini sanıp I’i yanlış bulmuş; x = −1’e soldan yaklaşırken grafiğin aşağı gittiğini düşünüp III’ü doğru saymış.','bilgi'),('I ve II','Ortadaki kolu x = 1’e yaklaşırken yukarı gidiyor sanıp II’yi doğru bulmuş; III’ü doğru okuyup yanlış bulmuş.','dikkat'),('I ve III','x = −1’e soldan yaklaşırken soldaki kolun aşağı gittiğini sanıp III’ü doğru bulmuş.','dikkat'),('I, II ve III','Ortadaki kolu yukarı, soldaki kolu aşağı giden sanıp hem II’yi hem III’ü doğru bulmuş.','dikkat')],
 'Üç yargının doğru olanları.',['Her yargıdaki x değerine verilen yönden yaklaşırken grafiğin kolunu izle ve yukarı mı aşağı mı gittiğine bak.'],[B_ASM,B_TEK],
 [A('I’i oku','x büyüdükçe sağ kol y = 2 doğrusuna yaklaşır.','lim (x→∞) f(x) = 2 → I doğru'),A('II’yi oku','x = 1’e soldan yaklaşırken ortadaki kol aşağı iner.','lim (x→1⁻) f(x) = −∞ → II yanlış'),A('III’ü oku','x = −1’e soldan yaklaşırken soldaki kol yukarı çıkar.','lim (x→−1⁻) f(x) = +∞ → III yanlış'),A('Sonucu yaz','Yalnız I doğrudur.','Yalnız I')],
 'Bir dikey asimptotta sonsuz limitin işareti, yaklaşılan yöndeki kolun yukarı ya da aşağı gitmesinden okunur.','K-ALM-07; iki dikey asimptotlu grafik',sekil=SK,sira=sira14)

# ============ 15 orta · dikey asimptot sayısı ve parametre ============
den=x**2-5*x+6
def dikey(a):
    fr_=sp.cancel((x**2-4*x+a)/den); d=sp.denom(fr_); return sorted(sp.roots(sp.Poly(d,x)).keys())
assert dikey(4)==[3] and dikey(3)==[2] and len(dikey(0))==2 and len(dikey(5))==2 and len(dikey(7))==2
cozum=[a for a in range(-30,31) if len(dikey(a))==1]; assert cozum==[3,4]
v=sum(cozum); assert v==7
e=[4-3,3,4,2+3]; assert e==[1,3,4,5] and v not in e
Q('0015','lm-asimptot','orta','Dikey Asimptot Sayısı','Paydayı sıfırlayan noktalarda sadeleşme olup olmadığına göre dikey asimptot sayısından parametre bulur.','yeni nesil',
 'a bir gerçel sayı olmak üzere, f(x) = (x² − 4x + a)/(x² − 5x + 6) kuralıyla tanımlanan f fonksiyonunun grafiğinin tam olarak bir tane dikey asimptotu vardır.\nBuna göre, a’nın alabileceği değerlerin toplamı kaçtır?',
 v,[(e[0],'Her iki değeri bulmuş, ancak değerlerin toplamı yerine farkını yazmış: 4 − 3.','islem'),(e[1],'Yalnız payın x = 3’te sıfır olduğu durumu bulmuş: a = 3.','dikkat'),(e[2],'Yalnız payın x = 2’de sıfır olduğu durumu bulmuş: a = 4.','dikkat'),(e[3],'a değerleri yerine paydanın köklerini toplamış: 2 + 3.','bilgi')],
 'a değerlerinin toplamı.',['Paydanın kökleri iki tane; bir tanesinde dikey asimptot olmaması için pay ne olmalı?'],[B_ASM],
 [A('Paydayı çarpanla','Paydanın kökleri iki tanedir.','x² − 5x + 6 = (x − 2)(x − 3)'),A('Tam bir asimptot koşulu','İki kökten tam birinde pay da sıfır olmalıdır; sadeleşen kökte boşluk oluşur.','x = 2 ya da x = 3 payı sıfırlar'),A('x = 2 durumu','Payın 2’de sıfır olması için a bulunur.','4 − 8 + a = 0 → a = 4'),A('x = 3 durumu','Payın 3’te sıfır olması için a bulunur.','9 − 12 + a = 0 → a = 3'),A('Toplamı bul','İki değer toplanır.','4 + 3 = 7')],
 'Paydanın kökünde pay da sıfırsa dikey asimptot yerine boşluk oluşur.','K-ALM-07; parametreli asimptot sayısı')

# ============ 16 zor · dikdörtgende uzaklık farkı (geometri şeması #1) ============
import math
cee=sp.sqrt((8-x)**2+36); cef=sp.sqrt(64+(6-x)**2)
v=sp.limit((cee-cef)/x,x,0,'+'); assert v==sp.Rational(-1,5)
assert sp.simplify(cee**2-cef**2+4*x)==0
e=[-4,Fr(-4,10),0,Fr(1,5)]; assert e==[-4,Fr(-2,5),0,Fr(1,5)] and Fr(-4,20)==Fr(-1,5) and Fr(4,20)==Fr(1,5)
k_=0.62; X=2.2
o=[f'\\draw[line width=1.6pt] (0,0) rectangle ({8*k_:.2f},{6*k_:.2f});',
   f'\\draw[{CG},line width=1.8pt] ({8*k_:.2f},{6*k_:.2f}) -- ({X*k_:.2f},0);',f'\\draw[{CH},line width=1.8pt] ({8*k_:.2f},{6*k_:.2f}) -- (0,{X*k_:.2f});',
   f'\\fill ({X*k_:.2f},0) circle (0.07);\\fill (0,{X*k_:.2f}) circle (0.07);',
   f'\\node[below left] at (0,0) {{$A$}};\\node[below right] at ({8*k_:.2f},0) {{$B$}};\\node[above right] at ({8*k_:.2f},{6*k_:.2f}) {{$C$}};\\node[above left] at (0,{6*k_:.2f}) {{$D$}};',
   f'\\node[below] at ({X*k_:.2f},-0.05) {{$E$}};\\node[left] at (-0.05,{X*k_:.2f}) {{$F$}};',
   f'\\node[below] at ({(X+8)/2*k_:.2f},-0.45) {{$8$}};\\node[right] at ({8*k_+0.05:.2f},{3*k_:.2f}) {{$6$}};',
   f'\\node[above=2pt,font=\\small] at ({X/2*k_:.2f},0) {{$x$}};\\node[right=2pt,font=\\small] at (0,{X/2*k_:.2f}) {{$x$}};',
   f'\\node[{CG},font=\\small] at ({5.6*k_:.2f},{1.4*k_:.2f}) {{$|CE|$}};\\node[{CH},font=\\small] at ({2.7*k_:.2f},{5.0*k_:.2f}) {{$|CF|$}};']
SK=fig('\n'.join(o))
Q('0016','lm-uygulama','zor','Uzunluk Farkının Limiti','Geometrik uzunlukları değişkene bağlı yazıp eşlenik yöntemiyle oranın limitini hesaplar.','şekilli',
 'Şekildeki ABCD dikdörtgeninde E noktası [AB] üzerinde, F noktası [AD] üzerinde ve A’dan farklıdır; |AE| = |AF| = x olacak biçimde seçilmiştir. Şekilde dikdörtgenin kenar uzunlukları santimetre cinsinden verilmiştir ve 0 < x < 6’dır. E ve F noktaları A köşesine yaklaşırken |CE| ile |CF| uzunlukları arasındaki farkın x’e oranı incelenmektedir.\nBuna göre, lim (x→0⁺) (|CE| − |CF|)/x limitinin değeri kaçtır?',
 Fr(-1,5),[(-4,'Eşlenikle çarpıp payı −4x bulmuş, ancak paydadaki |CE| + |CF| çarpanını yazmayıp −4x/x = −4 demiş.','dikkat'),(Fr(-2,5),'Paydadaki |CE| + |CF| toplamını 20 yerine 10 almış: −4/10.','islem'),(0,'x = 0 yazıp |CE| − |CF| = 0 bulmuş ve 0/0 belirsizliğini 0 saymış.','dikkat'),(Fr(1,5),'|CE|² − |CF|² farkını −4x yerine +4x bulmuş (işaret hatası): 4/20.','islem')],
 'Limitin değeri.',['İki uzunluğu Pisagor ile x cinsinden yaz; karekökler farkı olduğundan eşlenik işine yarar.'],[B_BEL,B_ESL],
 [A('Uzunlukları yaz','E = (x, 0) ve F = (0, x) noktalarından C’ye Pisagor uygulanır.','|CE|² = (8 − x)² + 36 · |CF|² = 64 + (6 − x)²'),A('Kareler farkını bul','Eşlenik için |CE|² − |CF|² hesaplanır.','(64 − 16x + x² + 36) − (64 + 36 − 12x + x²) = −4x'),A('Eşlenikle çarp','Pay ve payda |CE| + |CF| ile çarpılır.','(|CE| − |CF|)/x = −4x/(x(|CE| + |CF|)) = −4/(|CE| + |CF|)'),A('Limiti al','x → 0 iken her iki uzunluk 10’a gider.','−4/(10 + 10) = −1/5')],
 'İki karekökün farkı içeren 0/0 belirsizliğinde, kareler farkı payı genellikle x ile sadeleşecek hale getirir.','K-ALM-09; dikdörtgende iki uzunluğun farkı',sekil=SK)

# ============ 17 zor · tablo, çarpım sürekli, öncüllü (tablo #4) ============
fL,fR,fV,gL=3,6,3,4
gR=sp.Rational(fL*gL,fR); gV=sp.Rational(fL*gL,fV); assert (gR,gV)==(2,4) and gR!=gL
I17,II17,III17=(gR==2),(gV==4),(gR==gL==gV); assert (I17,II17,III17)==(True,True,False)
sira17=['Yalnız I','I ve II','I ve III','II ve III','I, II ve III']
SK=tablo_svg(['','f','g'],[['x → 2⁻ iken limit',str(fL),str(gL)],['x → 2⁺ iken limit',str(fR),'—'],['x = 2 için değer',str(fV),'—']])
assert fL*gL//fR==2 and fL*gL//fV==4
Q('0017','lm-surekli','zor','Çarpım Fonksiyonunun Sürekliliği','Çarpım fonksiyonunun sürekli olma koşulunu tek yönlü limitlerle kurup çarpanın limit ve değerini yorumlar.','öncüllü',
 'f ve g fonksiyonlarının x = 2 noktasındaki sol limitleri, sağ limitleri ve fonksiyon değerleri aşağıdaki tabloda verilmiştir; “—” ile gösterilen değerler verilmemiştir. g fonksiyonunun x = 2 noktasında sağdan ve soldan limitleri vardır ve f · g çarpım fonksiyonu x = 2 noktasında süreklidir.\nBuna göre,\nI. lim (x→2⁺) g(x) = 2’dir.\nII. g(2) = 4’tür.\nIII. g fonksiyonu x = 2 noktasında süreklidir.\nifadelerinden hangileri doğrudur?',
 'I ve II',[('Yalnız I','Sürekli çarpımda f yerine sağ limit 6’yı kullanıp g(2) = 12/6 = 2 bulmuş; II’yi yanlış saymış.','bilgi'),('I ve III','g’nin sürekli olduğunu sanıp g(2) değerini sağ limit olan 2 almış; II’yi yanlış, III’ü doğru bulmuş.','bilgi'),('II ve III','Sağ limit için f’nin sağ limiti yerine f(2) = 3’ü kullanıp g’nin sağ limitini 4 bulmuş; böylece g’yi sürekli ve I’i yanlış saymış.','bilgi'),('I, II ve III','Çarpımın sürekli olmasından g’nin de sürekli olması gerektiğini sanmış.','dikkat')],
 'Üç yargının doğru olanları.',['Çarpımın x = 2’de sürekli olması için soldan limit, sağdan limit ve değer arasında hangi eşitlikler kurulmalı?'],[B_SUR,B_OZL],
 [A('Soldan limit','Çarpımın sol limiti, limitlerin çarpımıdır.','3 × 4 = 12'),A('Sağdan limit','Çarpımın sağ limiti de 12 olmalıdır; g’nin sağ limiti L için 6L = 12.','L = 2 → I doğru'),A('Fonksiyon değeri','Çarpımın değeri de 12 olmalıdır: f(2) · g(2) = 12.','3 × g(2) = 12 → g(2) = 4 → II doğru'),A('g’nin sürekliliği','g’nin sol limiti 4, sağ limiti 2’dir; limitler eşit olmadığından g sürekli değildir.','4 ≠ 2 → III yanlış'),A('Sonucu yaz','I ve II doğrudur.','I ve II')],
 'Çarpım fonksiyonu sürekli olsa bile çarpanlardan biri süreksiz olabilir; her çarpanın limiti ayrı ayrı sınanır.','K-ALM-05; çarpım sürekliliği tablosu',sekil=SK,sira=sira17)

# ============ 18 zor · işaret çizelgesi ile sonsuz limit, öncüllü (sayı doğrusu #1) ============
pp=-(x+1)**2*(x-3); hh=(2*x-1)/pp
assert sp.limit(hh,x,-1)==-sp.oo and sp.limit(hh,x,3,'-')==sp.oo and sp.limit(hh,x,3,'+')==-sp.oo
sira18=['Yalnız I','I ve II','I ve III','II ve III','I, II ve III']
assert (sp.limit(hh,x,-1)==-sp.oo,sp.limit(hh,x,3,'-')==-sp.oo,sp.limit(hh,x,3,'+')==sp.oo)==(True,False,False)
u=0.95
o=[f'\\draw[-{{Stealth}},thick] ({-3.3*u:.2f},0) -- ({5.3*u:.2f},0) node[right] {{$x$}};',
   f'\\draw[thick] ({-1*u:.2f},-0.15) -- ({-1*u:.2f},0.15);\\draw[thick] ({3*u:.2f},-0.15) -- ({3*u:.2f},0.15);',
   f'\\fill ({-1*u:.2f},0) circle (0.08);\\fill ({3*u:.2f},0) circle (0.08);',
   f'\\node[below=4pt] at ({-1*u:.2f},0) {{$-1$}};\\node[below=4pt] at ({3*u:.2f},0) {{$3$}};',
   f'\\node[above=6pt,draw,circle,inner sep=2pt,font=\\large\\bfseries] at ({-2.2*u:.2f},0) {{$+$}};\\node[above=6pt,draw,circle,inner sep=2pt,font=\\large\\bfseries] at ({1*u:.2f},0) {{$+$}};\\node[above=6pt,draw,circle,inner sep=3pt,font=\\large\\bfseries] at ({4.2*u:.2f},0) {{$-$}};',
   f'\\node[{CF},font=\\small\\bfseries,anchor=east] at ({-3.5*u:.2f},0.85) {{$p(x)$}};']
SK=fig('\n'.join(o))
Q('0018','lm-asimptot','orta','İşaret Çizelgesiyle Sonsuz Limit','Polinomun işaret çizelgesinden payda sıfırlanan noktalarda tek yönlü sonsuz limitlerin işaretini belirler.','öncüllü',
 'p(x) polinomunun işaret çizelgesi şekilde gösterilmiştir; −1 ve 3, p’nin kökleridir ve bu noktalar dışında p(x) ≠ 0’dır. h fonksiyonu, p(x) ≠ 0 olan her gerçel sayıda h(x) = (2x − 1)/p(x) kuralıyla tanımlanmıştır.\nBuna göre,\nI. lim (x→−1) h(x) = −∞’dur.\nII. lim (x→3⁻) h(x) = −∞’dur.\nIII. lim (x→3⁺) h(x) = +∞’dur.\nifadelerinden hangileri doğrudur?',
 'Yalnız I',[('I ve II','x = 3’ün solunda p’yi negatif okuyup II’yi doğru bulmuş; sağını doğru okuyup III’ü yanlış saymış.','dikkat'),('I ve III','x = 3’ün sağında p’yi pozitif okuyup III’ü doğru bulmuş; solunu doğru okuyup II’yi yanlış saymış.','dikkat'),('II ve III','Payın x = −1’deki değerini −3 yerine +3 alıp I’i yanlış bulmuş; x = 3 çevresinde işaretleri ters okuyup II ve III’ü doğru saymış.','dikkat'),('I, II ve III','İşaret çizelgesini x = 3 civarında ters okumuş (solda negatif, sağda pozitif sanmış); bu yüzden II ve III’ü de doğru bulmuş.','dikkat')],
 'Üç yargının doğru olanları.',['Her limit noktasında payın işaretine ve paydanın yaklaşılan yandaki işaretine ayrı ayrı bak.'],[B_ISR],
 [A('x = −1’i incele','Payın değeri −3’tür; çift katlı kökte p işaret değiştirmez, iki yanda da pozitiftir.','(−3)/0⁺ → −∞ · I doğru'),A('x = 3⁻’yi incele','Payın değeri 5’tir; 3’ün solunda p pozitiftir.','5/0⁺ → +∞ · II yanlış'),A('x = 3⁺’yı incele','3’ün sağında p negatiftir.','5/0⁻ → −∞ · III yanlış'),A('Sonucu yaz','Yalnız I doğrudur.','Yalnız I')],
 'Sonsuz limitte işareti pay ile paydanın o yandaki işareti belirler; çift katlı kökte işaret değişmez.','K-ALM-07; işaret çizelgesi ve sonsuz limit',sekil=SK,sira=sira18)

# ============ 19 zor · ikizkenar üçgende alan/taban limiti (geometri şeması #2) ============
Sx=sp.Rational(1,2)*6*6*sp.sin(x); tx=2*6*sp.sin(x/2)
v=sp.limit(Sx/tx,x,0,'+'); assert v==3
e=[0,Fr(1,3),Fr(3,2),2]; assert sp.limit(sp.sin(x)/sp.sin(x/2),x,0)==2 and sp.limit(36*sp.sin(x)/tx,x,0)==6 and sp.limit(tx/Sx,x,0)==sp.Rational(1,3) and sp.limit(Sx/(12*x),x,0)==sp.Rational(3,2)
ang=math.radians(26); L_=3.0
Ap=(0,L_*math.cos(ang)); Bp=(-L_*math.sin(ang),0); Cp=(L_*math.sin(ang),0)
o=[f'\\draw[{CF},line width=1.8pt] ({Ap[0]:.3f},{Ap[1]:.3f}) -- ({Bp[0]:.3f},0) ;\\draw[{CF},line width=1.8pt] ({Ap[0]:.3f},{Ap[1]:.3f}) -- ({Cp[0]:.3f},0);\\draw[{CG},line width=1.8pt] ({Bp[0]:.3f},0) -- ({Cp[0]:.3f},0);',
   f'\\node[above] at ({Ap[0]:.2f},{Ap[1]:.2f}) {{$A$}};\\node[below left] at ({Bp[0]:.2f},0) {{$B$}};\\node[below right] at ({Cp[0]:.2f},0) {{$C$}};',
   f'\\draw[thick] ({Ap[0]-0.55*math.sin(ang):.3f},{Ap[1]-0.55*math.cos(ang):.3f}) arc[start angle={-90-26:.0f},end angle={-90+26:.0f},radius=0.55];',
   f'\\node[font=\\small] at (0,{Ap[1]-0.95:.2f}) {{$x$}};',
   f'\\node[left=3pt] at ({Bp[0]/2+Ap[0]/2:.2f},{Ap[1]/2:.2f}) {{$6$}};\\node[right=3pt] at ({Cp[0]/2+Ap[0]/2:.2f},{Ap[1]/2:.2f}) {{$6$}};']
SK=fig('\n'.join(o))
Q('0019','lm-uygulama','zor','Üçgende Alan ve Taban Oranı','Üçgenin alanını ve taban uzunluğunu açıya bağlı yazıp sin(kx)/x türündeki limitle oranın limitini bulur.','şekilli',
 'Şekildeki ABC ikizkenar üçgeninde eş kenarların uzunlukları santimetre cinsinden verilmiştir. A köşesindeki açının ölçüsü x radyandır (0 < x < π). Üçgenin alanı S(x) cm², taban uzunluğu t(x) cm olarak tanımlanmıştır; tepe açısı sıfıra yaklaşırken alanın taban uzunluğuna oranı incelenmektedir.\nBuna göre, lim (x→0⁺) S(x)/t(x) limitinin değeri kaçtır?',
 3,[(0,'Pay ve payda x = 0’da 0 olduğundan limiti 0 saymış.','dikkat'),(Fr(1,3),'Oranı ters kurup t(x)/S(x) limitini bulmuş.','dikkat'),(Fr(3,2),'t(x) = 12 sin(x/2) ifadesinde sin(x/2)’yi x/2 yerine x sanmış: 18x/(12x).','bilgi'),(2,'Oranı sin x/sin(x/2) biçiminde bırakıp 18/12 katsayısını yazmayı unutmuş.','dikkat')],
 'Limitin değeri.',['Alanı iki kenar ve aralarındaki açının sinüsüyle, tabanı tepe açıortayını çizerek yarım açıyla yaz.'],[B_TRG,B('Üçgenin alanı','iki kenar uzunluğu ve aralarındaki açının sinüsü bilinen üçgenin alanı ½ · a · b · sin(açı) formülüyle bulunur. Örnek: kenarları 4 ve 5, aralarındaki açı 30° olan üçgenin alanı ½ × 4 × 5 × ½ = 5’tir')],
 [A('Alanı yaz','İki eş kenar ve aralarındaki açı kullanılır.','S(x) = ½ × 6 × 6 × sin x = 18 sin x'),A('Tabanı yaz','Tepe açıortayı tabanı dik ortalar; yarım taban 6 sin(x/2) olur.','t(x) = 2 × 6 × sin(x/2) = 12 sin(x/2)'),A('Oranı kur','Alanın tabana oranı yazılır.','S(x)/t(x) = 18 sin x/(12 sin(x/2))'),A('Limiti hesapla','sin x/x → 1 ve sin(x/2)/x → 1/2 yazılır.','(18 × 1)/(12 × 1/2) = 18/6'),A('Sonucu yaz','Oran sadeleştirilir.','3')],
 'x → 0 iken sin(ax)/sin(bx) oranı a/b’ye gider; yarım açı varsa b = ½ alınır.','K-ALM-09; ikizkenar üçgende alan/taban',sekil=SK)

# ============ 20 orta · boşluklu doğru grafiğinden katsayı bulma (boşluklu grafik #3) ============
s=0.5
def abc(c,r): return -(c+r),c*r,c
a20,b20,c20=abc(3,-2); v=a20+b20+c20; assert (a20,b20,c20)==(-1,-6,3) and v==-4
assert sp.cancel((x**2-x-6)/(x-3))==x+2
e1=sum(abc(5,-2)); e2=sum(abc(3,2)); e3=a20+b20; e4=1+b20+c20
e=[e1,e2,e3,e4]; assert e==[-8,4,-7,-2] and v not in e
g_=[seg((-3,-1),(6,8),s),dolu((-2,0),s),dolu((0,2),s),bos((3,5),s),f'\\node[{CF},font=\\small\\bfseries] at ({4.6*s:.2f},{3.0*s:.2f}) {{$y=f(x)$}};']
SK=fig(graf(-3,6,-1,8,s,'\n'.join(g_)))
Q('0020','lm-surekli','orta','Süreksizliği Giderilebilir Nokta','Grafikteki boşluktan paydadaki kökü ve sadeleşen çarpanı belirleyerek rasyonel fonksiyonun katsayılarını bulur.','grafik',
 'a, b ve c gerçel sayılar olmak üzere f(x) = (x² + ax + b)/(x − c) kuralıyla tanımlı f fonksiyonunun grafiği şekilde verilmiştir. Grafik, tanımsız olduğu bir noktası dışında bir doğrudur; bu noktada grafikte içi boş bir nokta gösterilmiştir. Diğer işaretli noktalar ızgara çizgilerinin kesişimindedir.\nBuna göre, a + b + c toplamı kaçtır?',
 v,[(e[0],'Boş noktanın y koordinatını (5) paydadaki kök sanıp c = 5 almış: (x − 5)(x + 2).','bilgi'),(e[1],'Doğrunun denklemini y = x − 2 yazmış: (x − 3)(x − 2) ve a = −5, b = 6.','islem'),(e[2],'c’yi toplama katmamış: a + b.','dikkat'),(e[3],'(x − 3)(x + 2) çarpımında x’in katsayısını −1 yerine +1 yazmış.','islem')],
 'a + b + c toplamı.',['Boş noktanın ne anlama geldiğini ve doğrunun denklemini işaretli noktalardan düşün.'],[B_ASM,B_BEL],
 [A('Boşluktan c’yi bul','Grafikte x = 3’te içi boş nokta vardır; payda bu değerde sıfırdır.','c = 3'),A('Doğruyu yaz','Doğru (0, 2) ve (−2, 0) noktalarından geçer.','y = x + 2'),A('Payı kur','Sadeleşen ifade x + 2 olduğundan pay (x − 3)(x + 2) olmalıdır.','(x − 3)(x + 2) = x² − x − 6 → a = −1, b = −6'),A('Toplamı bul','a, b ve c toplanır.','−1 + (−6) + 3 = −4')],
 'Grafikteki boşluk ile rasyonel ifadenin çarpan yapısı arasındaki ilişkiyi kullan.','K-ALM-05; boşluklu doğru grafiği',sekil=SK)

#<<SON>>
# ---------------- yaz ----------------
for q_ in P.ANA: q_['kardes']=None
from collections import Counter
tipler={}
for k_ in KART: tipler.setdefault(k_['tipId'],dict(tipId=k_['tipId'],ad=k_['tip'],kartlar=[],uygulamaKonu=UK))['kartlar'].append(k_['id'])
if len(P.ANA)==20:
    json.dump(P.ANA,open(os.path.join(HD,'limit-1.json'),'w'),ensure_ascii=False,indent=1)
    json.dump(dict(konu='Limit',surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT Matematik 2018–2026 çıkmış soruları ve yayın soru bankaları (yalnız mantık), MEB 11–12. sınıf müfredatı.',kartlar=KART,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar','limit.json'),'w'),ensure_ascii=False,indent=1)
print(len(P.ANA),'soru · harfler',dict(sorted(Counter(q['cevap']['sik'] for q in P.ANA).items())),'· zorluk',dict(Counter(q['zorluk'] for q in P.ANA)),'· şekilli',sum(1 for q in P.ANA if q.get('sekil')),'· tip',len(tipler))
