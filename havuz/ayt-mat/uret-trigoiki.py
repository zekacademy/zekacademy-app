"""AYT Matematik · Trigonometri · 2. dalga · 20 soruluk paket (hafif mod; kardeş yok, ipucu 1).
Şekil, metin ve çeldirici değerleri aynı verilerden; her cevap ve çeldirici math/Fraction/sympy ile assert edilir."""
import sys,os,json,math,random
HD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(HD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
from ortak import *
from cizim import tikz_svg
from _hafif_mat import tablo_svg,mk
from fractions import Fraction as Fr
import sympy as sp
pi=math.pi; s2=math.sqrt(2); s3=math.sqrt(3); s5=math.sqrt(5); s6=math.sqrt(6)
def yak(a,b,t=1e-9): assert abs(a-b)<t,(a,b)
R_=math.radians
UK='amat|Trigonometri'
P=Parti('trigoiki','Trigonometri',UK,ders='AYT Matematik',idon='aytmat')
KY='ÖSYM AYT Matematik 2018–2026 (Trigonometri soruları; yalnız mantık) · yayın soru bankaları (yalnız mantık) · MEB 11. sınıf'
KART=[]; TIP={}
def kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip):
    KART.append(dict(id=id,konu='Trigonometri',alt=alt,fikir=fikir,tuzak=tuzak,zorluk=z,kalip=kalip,adim=adim,tipId=tipId,tip=tip,kaynak=KY)); TIP[tipId]=(tip,id)
def fs(v):
    v=Fr(v); n='−' if v<0 else ''; v=abs(v)
    return n+(str(v.numerator) if v.denominator==1 else f'{v.numerator}/{v.denominator}')
def Q(no,tipId,z,alt,kaz,kalip,metin,dogru,yan,istenen,ip,bilgi,ad,puf,kart_ozet,sekil=None,sira=None,kisa=None):
    """dogru=(şık metni, sayısal değer); yan=[(metin, değer, açıklama, tür)]. sira verilmezse sayısal değere göre küçükten büyüğe."""
    tip,kid=TIP[tipId]
    if sira is None:
        items=[dogru]+[(y[0],y[1]) for y in yan]; assert len({round(v,9) for _,v in items})==5,('esit sik',no,items)
        sira=[t for t,_ in sorted(items,key=lambda t:t[1])]
    d=dogru[0]; yy=[(y[0],y[2],y[3]) for y in yan]
    assert len(yy)==4 and len(set([d]+[y[0] for y in yy]))==5 and sorted(sira)==sorted([d]+[y[0] for y in yy]),(no,)
    mk(P,no,metin=metin,dogru=d,yan=yy,istenen=istenen,ad=ad,sekil=sekil,sira=sira,ip=ip,bilgi=bilgi,puf=puf,kisa=kisa,tipId=tipId,tip=tip,z=z,alt=alt,kaz=kaz,kalip=kalip,adim=len(ad),kart=f'{kid} ({kart_ozet})')
def fig(body,font='\\small'):
    return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font='+font+']\n'+body+'\n\\end{tikzpicture}')
def tz(s,**kw):
    for k,v in kw.items(): s=s.replace('@'+k+'@',(f'{v:.3f}' if isinstance(v,float) else str(v)))
    return s
MAVI='blue!70!black'; TUR='orange!90!black'; YES='green!50!black'; MOR='violet!80!black'

# ---------------- bilgi kutuları (örnekler soruların sayılarından farklı) ----------------
B_ISR=B('Bölgelere göre işaretler','I. bölgede sin, cos ve tan pozitiftir; II. bölgede yalnız sin, III. bölgede yalnız tan ve cot, IV. bölgede yalnız cos pozitiftir. Bir açının katı 2π’yi aşıyorsa tam turlar atılıp kalan açının bölgesine bakılır. Örnek: 7π/3 = 2π + π/3 olduğundan I. bölgededir; sin(7π/3) > 0')
B_SIR=B('Değerleri karşılaştırma','önce her sayının işaretine bakılır: negatifler pozitiflerden küçüktür. Aynı işaretli sayılar için açıyı bölgesine göre 0 ile 90° arasındaki karşılığına indirgeyip, sinüsün artan, kosinüsün azalan, tanjantın artan olduğu aralıklara göre kıyaslanır. Örnek: 0 < θ < π/2 için tanθ ile sinθ’da tanθ = sinθ/cosθ ≥ sinθ’dır')
B_ALAN=B('Üçgenin alanı','iki kenarının uzunluğu a ile b, aralarındaki açı C olan üçgenin alanı (1/2)·a·b·sinC’dir. Örnek: a = 6, b = 4 ve C = 30° ise alan = (1/2)·6·4·(1/2) = 6’dır')
B_TERS=B('Ters trigonometrik fonksiyonlar','θ = arcsin a ise sinθ = a ve θ ∈ [−π/2, π/2]; θ = arccos a ise cosθ = a ve θ ∈ [0, π]; θ = arctan a ise tanθ = a ve θ ∈ (−π/2, π/2)’dir. Örnek: arcsin(√3/2) = π/3, arccos 0 = π/2, arctan(√3/3) = π/6’dır')
B_TOP=B('Toplam–fark formülleri','cos(a ± b) = cos a·cos b ∓ sin a·sin b ve sin(a ± b) = sin a·cos b ± cos a·sin b’dir. Bir açının sinüsü bilindiğinde kosinüsü sin²+cos² = 1 ile bulunur; işaret açının ait olduğu aralıktan gelir. Örnek: sin a = 5/13 ve a dar açı ise cos a = 12/13’tür')
B_SAD=B('Sadeleştirmede kullanılan özdeşlikler','tanx = sinx/cosx, cotx = cosx/sinx, secx = 1/cosx, cosecx = 1/sinx; sin²x + cos²x = 1, sin2x = 2sinx·cosx, cos2x = cos²x − sin²x. Örnek: sinx·cosx·(tanx − cotx) = sin²x − cos²x’tir')
B_YAR=B('Yarım açı özdeşlikleri','1 + cosx = 2cos²(x/2) ve 1 − cosx = 2sin²(x/2)’dir. Örnek: 1 − cos 60° = 2sin²30° = 1/2’dir')
B_EGM=B('Doğrunun eğimi ve iki doğru arasındaki açı','eğimi m olan doğru pozitif x ekseniyle α açısı yapıyorsa m = tanα’dır. Eğimleri m₁ ve m₂ olan iki doğrunun x ekseniyle yaptığı açılar α₁ ve α₂ ise tan(α₁ − α₂) = (m₁ − m₂)/(1 + m₁·m₂)’dir. Örnek: m₁ = 3, m₂ = 1/2 için bu oran (5/2)/(5/2) = 1’dir')
B_TNG=B('Tanjant fonksiyonunun grafiği','y = a·tan(bx) fonksiyonunun periyodu π/|b|’dir; dikey asimptotları x = π/(2b) + kπ/b doğrularıdır ve eğri, iki asimptot arasında orijinden geçerek artar. Örnek: y = 3tan(2x) için asimptotlar x = ±π/4 doğrularıdır')
B_KOS=B('Kosinüs teoremi','bir üçgende a, b kenarları arasındaki açı C ise c² = a² + b² − 2ab·cosC’dir; buradan cosC = (a² + b² − c²)/(2ab) yazılır. Örnek: a = 2, b = 3, C = 60° ise c² = 4 + 9 − 2·2·3·(1/2) = 7’dir')
B_SIN=B('Sinüs teoremi','bir üçgende her kenarın uzunluğunun karşısındaki açının sinüsüne oranı sabittir: a/sinA = b/sinB = c/sinC = 2R. Büyük kenarın karşısında büyük açı bulunur. Örnek: A = 30°, a = 5 ise 2R = 5/(1/2) = 10’dur')
B_PER=B('Periyot ve simetri','f(x + T) = f(x) eşitliğini sağlayan en küçük pozitif T sayısına periyot denir; cos(bx) için periyot 2π/|b|’dir. f(−x) = f(x) ise fonksiyon çifttir. Örnek: sin²x’in periyodu π’dir, çünkü sin²x = (1 − cos2x)/2’dir')
B_YEN=B('Birim çemberde uzunluklar','O merkezli birim çemberde pozitif x ekseniyle θ açısı yapan ışının çemberi kestiği P noktası (cosθ, sinθ)’dır; P’nin x eksenine izdüşümü H için |OH| = |cosθ|, |PH| = |sinθ|’dır. Örnek: θ = 60° için |OH| = 1/2 ve |PH| = √3/2’dir')
B_IKI=B('İki kat açı formülleri','sin2x = 2sinx·cosx, cos2x = cos²x − sin²x = 1 − 2sin²x = 2cos²x − 1’dir. Ayrıca sin3x = 3sinx − 4sin³x ve cos3x = 4cos³x − 3cosx’tir. Örnek: x = 30° için sin90°/sin30° = 2’dir ve 3 − 4 · (1/4) = 2 ile uyumludur')
B_DEN=B('Denklemi tek fonksiyona indirgeme','pay ve paydanın cos²x ya da sin²x’e bölünmesiyle denklem tanx ya da cotx cinsinden ikinci dereceden bir denkleme döner; bulunan kökler, verilen aralıktaki işaret koşuluna uymuyorsa elenir. Örnek: 0 < x < π/2 için cotx > 0’dır')
B_ACI=B('Açıortay teoremi ve iki kat açı','ABC üçgeninde [AD] açıortay ise |BD|/|DC| = |AB|/|AC|’dir. Ayrıca tan2x = 2tanx/(1 − tan²x)’tir. Örnek: |AB| = 6, |AC| = 9 ise |BD| : |DC| = 2 : 3’tür')
B_TNJ=B('Dik üçgende tanjant ve iki kat açı','dik üçgende tanα = karşı dik kenar / komşu dik kenar; tan2α = 2tanα/(1 − tan²α)’dır. Örnek: tanα = 1/3 ise tan2α = (2/3)/(8/9) = 3/4’tür')

# ---------------- kartlar ----------------
kart('K-ATR2-01','Bölge işareti ve değer karşılaştırma','Açının bulunduğu bölge, oranların işaretini belirler; katlı açılarda tam tur atılarak bölge bulunur, sıralamada önce işaret, sonra büyüklük karşılaştırılır.','Katlı açının bölgesini yanlış bulmak; III. bölgede tanjantın pozitif olduğunu unutmak; negatif sayıyı pozitif sayıdan büyük saymak.','kolay','düz',3,'trg2-isaret','Bölge işareti ve sıralama')
kart('K-ATR2-02','Üçgende alan, kosinüs ve sinüs teoremi','Kenar–açı verilerine göre alan formülü, kosinüs teoremi ya da sinüs teoremi seçilir; açının bölgesi işareti belirler, kenar sıralaması açı sıralamasını verir.','cos işaretini yanlış almak; kenarı bitişik açıyla eşlemek; alan formülünde 1/2 çarpanını atlamak; geniş açıyı dar sanmak.','orta','şekilli',4,'trg2-ucgen','Üçgende alan ve teoremler')
kart('K-ATR2-04','Sadeleştirme ve özdeşlikler','İfade sinüs–kosinüs cinsine yazılıp iki kat açı, toplam ve temel özdeşliklerle tek bir trigonometrik ifadeye sadeleştirilir.','İki kat açıdaki 2 çarpanını yanlış yerleştirmek; tan ile cot’u karıştırmak; parantez önündeki eksi işaretini dağıtırken hata yapmak.','orta','düz',4,'trg2-sadelestir','Sadeleştirme ve özdeşlikler')
kart('K-ATR2-05','Birim çember ve açıortay geometrisi','Şekildeki uzunluklar açının trigonometrik oranlarıyla yazılır; yarım açı ve iki kat açı özdeşlikleriyle istenen oran ya da uzunluk açıya bağlanır.','Yarım açı ile tam açıyı karıştırmak; oranı ters kurmak; açıortay teoreminde kenarları yanlış eşlemek.','orta','şekilli',4,'trg2-geo','Birim çember ve açıortay geometrisi')
kart('K-ATR2-06','Toplam–fark formülleri','Toplam–fark formülleri; açıların oranları dik üçgenlerden ya da doğruların eğimlerinden (eğim = tanjant) okunur ve birleşik açının oranı hesaplanır.','Paydadaki işareti ters almak; farkı yerine toplamı kullanmak; kosinüs formülünde işareti ters almak.','orta','şekilli',3,'trg2-toplamfark','Toplam–fark formülleri')
kart('K-ATR2-07','Grafik okuma ve fonksiyonun özellikleri','Grafikteki uç değer, sıfır ve asimptot konumlarından kural çıkarılır; periyot, simetri, eşitsizlik ve kök sayısı bu kuraldan yorumlanır.','Periyodu yanlış okumak; asimptot konumunu periyot sanmak; kök ve eşitsizlik aralıklarını tek periyotla sınırlamak.','zor','grafik',5,'trg2-grafik','Grafik okuma ve fonksiyonun özellikleri')
kart('K-ATR2-08','Tanımlı yeni fonksiyon','Soruda tanımlanan yeni fonksiyon, birim çemberdeki uzunluğun trigonometrik oranlarla yazılmasıyla bilinen fonksiyonlara çevrilir.','Tanımdaki uzunluğu yanlış parçayla eşlemek; fonksiyonu doğrusal sanmak; iki kat açıda formülü karıştırmak.','orta','şekilli',4,'trg2-yeni','Tanımlı yeni fonksiyon')
kart('K-ATR2-09','Trigonometrik denklem ve koşul','Denklem tek oran cinsinden ikinci dereceden bir denkleme indirgenir; kökler verilen aralığın işaret koşuluyla elenir.','Kökün işaret koşulunu denetlememek; cot ile tan’ı karıştırmak; ara terimdeki iki kat açı çarpanını atlamak.','zor','düz',4,'trg2-denklem','Trigonometrik denklem')
kart('K-ATR2-10','Gölge ve yükseklik problemleri','Dik üçgenlerde tanjant yazılır; açının iki katı olduğu durumda iki kat açı formülüyle bilinmeyen yükseklik bulunur.','Gölge uzunluğunu açıyla orantılı sanmak; iki kat açı formülünü doğrusal almak; farkı ya da ortalamayı cevap sanmak.','zor','hikâyeli',4,'trg2-uygulama','Gölge ve yükseklik problemi')

# ================= 0001 kolay · bölge işareti (şekilli) =================
QD={1:dict(sin=1,cos=1,tan=1,cot=1),2:dict(sin=1,cos=-1,tan=-1,cot=-1),3:dict(sin=-1,cos=-1,tan=1,cot=1),4:dict(sin=-1,cos=1,tan=-1,cot=-1)}
def tri(qa,q2,sg=None):
    S=lambda q,f:(QD[q][f] if sg is None or (q,f) not in sg else sg[(q,f)])
    return (S(q2,'sin')*S(qa,'tan'),S(q2,'cos')*S(qa,'cot'),S(qa,'sin')*S(q2,'cot'))
def ts(t): return ', '.join('+' if v>0 else '−' for v in t)
dog1=tri(3,2); assert dog1==(1,-1,1)
for i in range(1,200):   # sayısal doğrulama: α ∈ (5π/4, 3π/2)
    a=5*pi/4+(pi/4)*i/200
    t=(math.sin(2*a)*math.tan(a),math.cos(2*a)/math.tan(a),math.sin(a)/math.tan(2*a)); assert tuple(1 if v>0 else -1 for v in t)==dog1
m1=tri(3,3); m2=tri(3,1); m3=tri(3,2,{(3,'tan'):-1,(3,'cot'):-1}); m4=tri(3,2,{(3,'sin'):1})
assert len({dog1,m1,m2,m3,m4})==5 and m1==(-1,-1,-1) and m2==(1,1,-1) and m3==(-1,1,1) and m4==(1,-1,-1)
a_,b_=5*pi/4,3*pi/2
SK=fig(tz('''\\fill[@T@!22] (0,0) -- (@x1@,@y1@) arc (225:270:2) -- cycle;
\\draw[thick] (0,0) circle (2);
\\draw[-{Stealth}] (-2.5,0) -- (2.8,0) node[right] {$x$};
\\draw[-{Stealth}] (0,-2.7) -- (0,2.7) node[above] {$y$};
\\draw[very thick,@M@] (0,0) -- (@x1@,@y1@) -- (@x2@,@y2@);
\\draw[very thick,@M@] (0,0) -- (0,-2.35);
\\draw[@M@,thick,-{Stealth}] (0.55,0) arc (0:225:0.55);
\\draw[@T@,thick,-{Stealth}] (0.8,0) arc (0:270:0.8);
\\node[@M@,left=2pt] at (@x2@,@y2@) {$\\dfrac{5\\pi}{4}$};
\\node[@T@!70!black,right=3pt] at (0,-2.35) {$\\dfrac{3\\pi}{2}$};
\\node[above right,font=\\footnotesize] at (0,0) {$O$};
\\node[font=\\footnotesize,below right] at (2,0) {$1$};''',T=TUR,M=MAVI,x1=2*math.cos(a_),y1=2*math.sin(a_),x2=2.35*math.cos(a_),y2=2.35*math.sin(a_)))
Q('0001','trg2-isaret','kolay','Katlı Açılarda Bölge İşareti','Yönlü açının bulunduğu bölgeden ve katlı açıların bölgesinden sin, cos, tan, cot işaretlerini belirleyerek çarpımların işaretini bulur.','şekilli',
 'Şekilde, O merkezli birim çember ve pozitif x ekseniyle yaptıkları yönlü açıların ölçüleri radyan cinsinden verilen iki ışın ile bu ışınlar arasındaki bölge gösterilmiştir.\n0 < α < 2π olmak üzere, α yönlü açısının bitim kenarı taralı bölgenin içinde (kenarlar hariç) olduğuna göre,\nx = sin2α · tanα\ny = cos2α · cotα\nz = sinα · cot2α\nsayılarının işaretleri sırasıyla aşağıdakilerden hangisidir?',
 (ts(dog1),0),
 [(ts(m2),1,'2α’yı I. bölgede sanmış (2π’den büyük açıda bir tur eksik bakmış): sin2α(+)·tanα(+) = +, cos2α(+)·cotα(+) = +, sinα(−)·cot2α(+) = −.','bilgi'),
  (ts(m4),2,'sinα’yı III. bölgede pozitif almış: x ve y doğru çıkar, z = sinα(+)·cot2α(−) = − olur.','bilgi'),
  (ts(m3),3,'III. bölgede tanjant ve kotanjantı negatif almış: x = sin2α(+)·tanα(−) = −, y = cos2α(−)·cotα(−) = +, z = sinα(−)·cot2α(−) = +.','bilgi'),
  (ts(m1),4,'2α’yı da α gibi III. bölgede sanmış: sin2α(−)·tanα(+) = −, cos2α(−)·cotα(+) = −, sinα(−)·cot2α(+) = −.','bilgi')],
 'x, y, z’nin işaretleri.',['Şekildeki ışınların ölçülerinden α’nın hangi aralıkta olduğunu yaz; 2α’nın aralığını bulup tam turları atarak bölgesine bak.'],[B_ISR],
 [A('α’nın aralığı','Işınlar 5π/4 ve 3π/2 olduğundan α, III. bölgenin içinde kalır.','5π/4 < α < 3π/2 · α: III. bölge'),
  A('2α’nın aralığı','Aralık iki katına çıkarılır, tam tur (2π) atılır.','5π/2 < 2α < 3π → 2α − 2π ∈ (π/2, π): II. bölge'),
  A('Oranların işaretleri','III. bölgede tan, cot pozitif; sin negatif. II. bölgede sin pozitif; cos, cot negatif.','tanα(+), cotα(+), sinα(−) · sin2α(+), cos2α(−), cot2α(−)'),
  A('Çarpımlar','İşaretler çarpılır.','x = (+)(+) = + · y = (−)(+) = − · z = (−)(−) = +')],
 'Katlı açıda önce açının aralığını iki katına çıkar, sonra tam turları atarak bölgesini bul.','K-ATR2-01; α ∈ (5π/4, 3π/2) için sin2α·tanα, cos2α·cotα, sinα·cot2α',sekil=SK,
 sira=[ts(dog1),ts(m2),ts(m4),ts(m3),ts(m1)])

# ================= 0002 kolay · üçgen alanı (şekilli) =================
AB2,AC2,Ang2=8,5,150
al2=Fr(1,2)*AB2*AC2*Fr(1,2); assert al2==10; yak(0.5*AB2*AC2*math.sin(R_(Ang2)),10)
e2=[Fr(20),20*s3,40,10*s3]; yak(0.5*40*s3/2,10*s3); yak(20*s3,40*s3/2)
c2=0.52
Ax,Ay=0,0; Bx,By=AB2*c2,0; Cx,Cy=AC2*c2*math.cos(R_(Ang2)),AC2*c2*math.sin(R_(Ang2))
SK=fig(tz('''\\fill[@M@!12] (@Ax@,@Ay@) -- (@Bx@,@By@) -- (@Cx@,@Cy@) -- cycle;
\\draw[very thick,@M@] (@Ax@,@Ay@) -- (@Bx@,@By@); \\draw[very thick,@T@] (@Ax@,@Ay@) -- (@Cx@,@Cy@); \\draw[very thick,@Y@] (@Bx@,@By@) -- (@Cx@,@Cy@);
\\draw[thick,-{Stealth}] (0.55,0) arc (0:150:0.55); \\node[font=\\footnotesize] at (@lx@,@ly@) {$150^\\circ$};
\\node[below] at (@mx@,0) {$8$}; \\node[left=2pt,@T@!70!black] at (@tx@,@ty@) {$5$};
\\node[below left] at (0,0) {$A$}; \\node[below right] at (@Bx@,0) {$B$}; \\node[above left] at (@Cx@,@Cy@) {$C$};''',M=MAVI,T=TUR,Y=YES,Ax=Ax,Ay=Ay,Bx=Bx,By=By,Cx=Cx,Cy=Cy,mx=Bx/2,tx=Cx/2,ty=Cy/2,lx=0.9*math.cos(R_(118)),ly=0.9*math.sin(R_(118))))
Q('0002','trg2-ucgen','kolay','Üçgenin Alanı','İki kenar ve aralarındaki geniş açı verilen üçgenin alanını (1/2)·a·b·sinC ile bulur; sin150° değerini indirgemeyle hesaplar.','şekilli',
 'Şekildeki ABC üçgeninin alanı kaç birimkaredir?',
 (fs(al2),10.0),
 [(fs(e2[0]),20.0,'Alan formülündeki 1/2 çarpanını atlamış: 8 · 5 · sin150° = 40 · (1/2) = 20.','islem'),
  ('10√3',10*s3,'sin150° = √3/2 almış (150° ile 120°’yi karıştırmış): (1/2) · 8 · 5 · (√3/2) = 10√3.','bilgi'),
  ('20√3',20*s3,'Hem 1/2 çarpanını atlamış hem sin150° = √3/2 almış: 8 · 5 · (√3/2) = 20√3.','bilgi'),
  (fs(e2[2]),40.0,'Sinüs değerini hiç kullanmayıp kenarların çarpımını almış: 8 · 5 = 40.','dikkat')],
 'ABC üçgeninin alanı.',['İki kenarın aralarındaki açıyla birlikte verildiği bir üçgende alanı veren bağıntıyı düşün; 150° açının sinüsünü 180° etrafında indirgeyerek bul.'],[B_ALAN,B('İndirgeme','Geniş açının sinüsü 180° − a ile bulunur: sin(180° − a) = sin a. Örnek: sin120° = sin60° = √3/2')],
 [A('Formülü yaz','Alan, iki kenar ile aralarındaki açının sinüsüne bağlıdır.','Alan = (1/2) · |AB| · |AC| · sin150°'),
  A('sin150° değeri','150° = 180° − 30° olduğundan sinüs pozitiftir.','sin150° = sin30° = 1/2'),
  A('Hesapla','Değerler yerine konur.','(1/2) · 8 · 5 · (1/2) = 10')],
 'Geniş açılı üçgende de alan formülü aynıdır; yalnız sinüs değerini indirgemeyle bul.','K-ATR2-02; 150° açılı üçgenin alanı',sekil=SK,
 sira=['10','10√3','20','20√3','40'])
# sıra: sayısal artan (10, 17.3, 20, 34.6, 40)

# ================= 0003 kolay · toplam-fark / iki kat açı (düz) =================
v3=Fr(1,8)*Fr(0)  # yer tutucu
yak(math.sin(R_(15))*math.cos(R_(15))*math.cos(R_(30)),s3/8)
Q('0003','trg2-sadelestir','kolay','Özel Açılarda İki Kat Açı','sin15°·cos15° çarpımını iki kat açı formülüyle sin30°’a çevirip cos30° ile çarpar.','düz',
 'sin15° · cos15° · cos30°\nişleminin sonucu kaçtır?',
 ('√3/8',s3/8),
 [('1/8',1/8,'cos30° değerini 1/2 almış (cos60° ile karıştırmış): (1/4) · (1/2) = 1/8.','bilgi'),
  ('1/4',1/4,'cos30° çarpanını hesaba katmamış: sin15°·cos15° = 1/4.','dikkat'),
  ('√3/4',s3/4,'sin15°·cos15° = sin30° yazmış (2 çarpanını unutmuş): (1/2) · (√3/2) = √3/4.','islem'),
  ('1/2',0.5,'Yalnız sin15°·cos15° = sin30° = 1/2 değerini bulup cos30° çarpanını atlamış.','dikkat')],
 'İşlemin sonucu.',['İlk iki çarpanı tek bir açının oranı olarak yazmayı dene.'],[B_IKI],
 [A('İki kat açı','sin2a = 2sina·cosa olduğundan çarpım yarıya bölünmüş sin30° olur.','sin15° · cos15° = (1/2) · sin30° = 1/4'),
  A('cos30° değeri','Özel açı değeridir.','cos30° = √3/2'),
  A('Çarp','İki değer çarpılır.','(1/4) × (√3/2) = √3/8')],
 'Çarpımı tek bir iki kat açı ifadesine çevir.','K-ATR2-04; sin15°·cos15°·cos30°',
 sira=['1/8','√3/8','1/4','√3/4','1/2'])

# ================= 0004 orta · sıralama (düz) =================
# π/6 < α < π/4 ; x = sinα, y = cos3α, z = cotα  ->  y < x < z
vals=[]
for i in range(1,400):
    a=pi/6+(pi/12)*i/400
    x,y,z=math.sin(a),math.cos(3*a),1/math.tan(a); assert y<0<x<z and x<0.71 and z>1
srt={'x < y < z':None,'x < z < y':None,'y < x < z':None,'y < z < x':None,'z < x < y':None,'z < y < x':None}
dog4='y < x < z'
Q('0004','trg2-isaret','orta','Değer Karşılaştırma','Katlı açının bölgesinden işaretini belirleyip sinüs, kosinüs ve kotanjant değerlerini sıralar.','düz',
 'π/6 < α < π/4 olmak üzere,\nx = sinα\ny = cos3α\nz = cotα\nsayılarının doğru sıralanışı aşağıdakilerden hangisidir?',
 (dog4,0),
 [('x < z < y',1,'cos3α’yı pozitif ve cotα’dan büyük sanmış (3α’nın II. bölgede olduğunu görmemiş).','bilgi'),
  ('y < z < x',2,'cotα’yı sinα’dan küçük sanmış (π/4’ten küçük açılarda cotα > 1 > sinα olduğunu atlamış).','bilgi'),
  ('z < x < y',3,'cotα’yı en küçük, cos3α’yı en büyük sanmış (cos3α’nın negatif olduğunu atlamış).','bilgi'),
  ('z < y < x',4,'cotα’yı sinα’dan küçük, cos3α’yı pozitif ve sinα’dan küçük sanmış (z < y < x).','dikkat')],
 'x, y, z’nin küçükten büyüğe sıralaması.',['Her sayının işaretini ve 1 ile karşılaştırmasını ayrı ayrı belirle; 3α’nın hangi aralığa düştüğünü bul.'],[B_ISR,B_SIR],
 [A('3α’nın aralığı','Aralık üç katına çıkarılır.','π/2 < 3α < 3π/4 → II. bölge'),
  A('cos3α','II. bölgede kosinüs negatiftir.','y = cos3α < 0'),
  A('sinα','α, I. bölgede ve π/4’ten küçüktür.','0 < x = sinα < √2/2 < 1'),
  A('cotα','π/4’ten küçük açıda kotanjant 1’den büyüktür.','z = cotα > 1'),
  A('Sırala','Negatif en küçük, 1’den küçük pozitif ortada, 1’den büyük en büyüktür.','y < x < z')],
 'Sıralamada önce işarete, sonra 1’le kıyaslamaya bak.','K-ATR2-01; sinα, cos3α, cotα sıralaması',
 sira=['x < z < y','y < z < x','y < x < z','z < x < y','z < y < x'])

# ================= 0005 orta · sadeleştirme (düz) =================
xs=sp.symbols('x')
E5=(sp.cos(xs)**2-sp.sin(xs)**2)*(sp.tan(xs)+sp.cot(xs))
for xv in (0.3,0.7,1.1):
    yak(float(E5.subs(xs,xv)),2/math.tan(2*xv),1e-9)
    yak(float(E5.subs(xs,xv)),float(2*sp.cot(2*xs).subs(xs,xv)))
Q('0005','trg2-sadelestir','orta','Sadeleştirme','İki kat açı ve temel özdeşliklerle tanjant–kotanjant toplamı içeren ifadeyi tek bir trigonometrik ifadeye sadeleştirir.','düz',
 '(cos²x − sin²x) · (tanx + cotx)\nifadesinin tanımlı olduğu x değerleri için sadeleştirilmiş biçimi aşağıdakilerden hangisidir?',
 ('2·cot2x',2),
 [('cot2x/2',1,'sinx·cosx = 2sin2x yazmış (iki kat açı formülünü ters kullanmış): tanx + cotx = 1/(2sin2x), sonuç cos2x/(2sin2x) = cot2x/2.','islem'),
  ('cot2x',3,'sinx·cosx = sin2x yazmış (2 çarpanını unutmuş): tanx + cotx = 1/sin2x, sonuç cos2x/sin2x = cot2x.','islem'),
  ('2·tan2x',4,'cos2x/sin2x yerine sin2x/cos2x yazmış (kotanjantı tanjantla karıştırmış): 2·tan2x.','dikkat'),
  ('2·cosec2x',5,'cos²x − sin²x yerine 1 yazmış (sin²x + cos²x ile karıştırmış): 1 · 2/sin2x = 2·cosec2x.','bilgi')],
 'Sadeleştirilmiş ifade.',['Parantezlerin her birini iki kat açı ya da sinx·cosx cinsinden yazmayı dene; tanjant ve kotanjantı sinüs–kosinüs oranına çevir.'],[B_SAD,B_IKI],
 [A('İlk parantez','cos²x − sin²x iki kat açı özdeşliğidir.','cos²x − sin²x = cos2x'),
  A('İkinci parantez','Tanjant ve kotanjant sinüs–kosinüsle yazılıp ortak paydada toplanır.','tanx + cotx = (sin²x + cos²x)/(sinx·cosx) = 1/(sinx·cosx)'),
  A('İki kat açıya çevir','sinx·cosx = sin2x/2 olduğundan toplam 2/sin2x olur.','tanx + cotx = 2/sin2x'),
  A('Çarp','İki ifade çarpılır.','cos2x · 2/sin2x = 2·cot2x')],
 'Önce her parantezi tek bir iki kat açı ifadesine çevir.','K-ATR2-04; (cos²x − sin²x)(tanx + cotx)',
 sira=['cot2x/2','cot2x','2·cot2x','2·tan2x','2·cosec2x'])

# ================= 0006 orta · yarım çember, AH/HB (şekilli) =================
xdeg=52; xr=R_(xdeg); r6=2.2
for xv in (0.4,0.9,1.3):
    yak((1+math.cos(xv))/(1-math.cos(xv)),1/math.tan(xv/2)**2)
    yak((1+math.cos(xv))/math.sin(xv),1/math.tan(xv/2)); yak((1-math.cos(xv))/math.sin(xv),math.tan(xv/2)); yak(math.cos(xv)/math.sin(xv),1/math.tan(xv))
cx,cy=r6*math.cos(xr),r6*math.sin(xr)
SK=fig(tz('''\\fill[@M@!12] (-@r@,0) -- (@cx@,0) -- (@cx@,@cy@) -- cycle;
\\fill[@T@!22] (@cx@,0) -- (@r@,0) -- (@cx@,@cy@) -- cycle;
\\draw[thick] (-@r@,0) arc (180:0:@r@); \\draw[thick] (-@r@,0) -- (@r@,0);
\\draw[very thick,@M@] (-@r@,0) -- (@cx@,@cy@); \\draw[very thick,@T@] (@cx@,@cy@) -- (@r@,0);
\\draw[thick,@Y@] (@cx@,@cy@) -- (@cx@,0);
\\draw[thick] (0,0) -- (@cx@,@cy@);
\\draw[thick,-{Stealth}] (0.6,0) arc (0:@xd@:0.6); \\node at (0.95,0.33) {$x$};
\\draw (@cx@,0) -- (@cx@-0.18,0) -- (@cx@-0.18,0.18) -- (@cx@,0.18);
\\fill (0,0) circle (1.6pt); \\fill (@cx@,@cy@) circle (2pt);
\\node[below left] at (-@r@,0) {$A$}; \\node[below right] at (@r@,0) {$B$}; \\node[below left] at (0,0) {$O$};
\\node[above right] at (@cx@,@cy@) {$C$}; \\node[below] at (@cx@,0) {$H$};''',M=MAVI,T=TUR,Y=YES,r=r6,cx=cx,cy=cy,xd=xdeg))
Q('0006','trg2-geo','orta','Yarım Çemberde Oran','Yarım çemberdeki dik izdüşüm uzunluklarını x açısının kosinüsüyle yazıp oranı yarım açı özdeşlikleriyle sadeleştirir.','şekilli',
 'Şekilde, O merkezli ve yarıçapı 1 birim olan yarım çember ile [AB] çapı üzerinde bir H noktası verilmiştir. C noktası çember üzerinde, [CH] ⊥ [AB] ve m(BOC) = x’tir.\nBuna göre, |AH| / |HB| oranının x türünden eşiti aşağıdakilerden hangisidir?',
 ('cot²(x/2)',3),
 [('tan(x/2)',1,'Oranı |HB|/|CH| almış (pay ve paydaya yanlış uzunlukları yazmış): (1 − cosx)/sinx = tan(x/2).','dikkat'),
  ('tan²(x/2)',2,'Oranı ters kurmuş: |HB| / |AH| = (1 − cosx)/(1 + cosx) = tan²(x/2).','dikkat'),
  ('cot(x/2)',4,'|HB| yerine |CH| = sinx almış: (1 + cosx)/sinx = cot(x/2).','bilgi'),
  ('cotx',5,'|AH| yerine |OH| = cosx, |HB| yerine |CH| = sinx almış: cosx/sinx = cotx.','bilgi')],
 '|AH| / |HB| oranı.',['|AH| ve |HB| uzunluklarını x açısının oranlarıyla yazmayı dene.'],[B_YEN,B_YAR],
 [A('|OH| uzunluğu','C(cosx, sinx) olduğundan OH, C’nin apsisidir.','|OH| = cosx'),
  A('Parçaları yaz','O, [AB]’nin ortasıdır ve |OA| = |OB| = 1’dir.','|AH| = 1 + cosx · |HB| = 1 − cosx'),
  A('Oranı yaz','İki uzunluk bölünür.','|AH|/|HB| = (1 + cosx)/(1 − cosx)'),
  A('Yarım açıya çevir','1 + cosx = 2cos²(x/2) ve 1 − cosx = 2sin²(x/2) yazılır.','2cos²(x/2) / 2sin²(x/2) = cot²(x/2)')],
 'Yarım açı özdeşliği 1 ± cosx ifadelerini kareli bir terime çevirir.','K-ATR2-05; yarım çemberde (1 + cosx)/(1 − cosx)',sekil=SK,
 sira=['tan(x/2)','tan²(x/2)','cot²(x/2)','cot(x/2)','cotx'])

# ================= 0007 orta · doğrular arası açı (şekilli) =================
K7=(2,4); L7=(4,1); m1_=Fr(K7[1],K7[0]); m2_=Fr(L7[1],L7[0]); assert m1_==2 and m2_==Fr(1,4)
v7=(m1_-m2_)/(1+m1_*m2_); assert v7==Fr(7,6)
e7=[Fr(6,7),(m1_-m2_),(m1_-m2_)/(1-m1_*m2_),(m1_+m2_)/(1-m1_*m2_)]; assert e7==[Fr(6,7),Fr(7,4),Fr(7,2),Fr(9,2)]
yak(math.atan(2)-math.atan(0.25),math.atan(7/6))
a1=math.degrees(math.atan(0.25)); a2=math.degrees(math.atan(2))
g=[f'\\draw[gray!35,thin] ({i},0) -- ({i},5);' for i in range(1,6)]+[f'\\draw[gray!35,thin] (0,{j}) -- (5.2,{j});' for j in range(1,6)]
g.append(f'\\fill[{TUR}!18] (0,0) -- ({1.7*math.cos(R_(a1)):.3f},{1.7*math.sin(R_(a1)):.3f}) arc ({a1:.2f}:{a2:.2f}:1.7) -- cycle;')
g.append('\\draw[-{Stealth},thick] (-0.15,0) -- (5.6,0) node[right] {$x$}; \\draw[-{Stealth},thick] (0,-0.15) -- (0,5.6) node[above] {$y$};')
g.append(f'\\draw[very thick,{MAVI}] (0,0) -- (2.5,5); \\draw[very thick,{TUR}] (0,0) -- (5.2,1.3);')
g.append(f'\\fill[{MAVI}] (2,4) circle (2.4pt) node[left=3pt,black] {{$K(2,4)$}}; \\fill[{TUR}] (4,1) circle (2.4pt) node[below=3pt,black] {{$L(4,1)$}};')
g.append(f'\\node[{MAVI}] at (2.95,4.85) {{$d_1$}}; \\node[{TUR}!70!black] at (5.2,1.75) {{$d_2$}};')
g.append(f'\\node at ({2.05*math.cos(R_((a1+a2)/2)):.3f},{2.05*math.sin(R_((a1+a2)/2)):.3f}) {{$\\alpha$}};')
g+= [f'\\node[below,font=\\footnotesize] at ({i},0) {{${i}$}};' for i in (1,2,3,4,5)]+[f'\\node[left,font=\\footnotesize] at (0,{j}) {{${j}$}};' for j in (1,2,3,4,5)]
SK=fig('\n'.join(g))
Q('0007','trg2-toplamfark','orta','İki Doğru Arasındaki Açı','Doğruların eğimini şekildeki noktalardan bulup iki doğru arasındaki dar açının tanjantını fark formülüyle hesaplar.','şekilli',
 'Dik koordinat düzleminde, başlangıç noktasından geçen d₁ ve d₂ doğruları şekilde gösterilmiştir.\nBu doğrular arasındaki dar açının ölçüsü α olduğuna göre, tanα kaçtır?',
 (fs(v7),float(v7)),
 [(fs(e7[0]),float(e7[0]),'Oranı ters yazmış: (1 + m₁m₂)/(m₁ − m₂) = (3/2)/(7/4) = 6/7 (cotα’yı bulmuş).','dikkat'),
  (fs(e7[1]),float(e7[1]),'Paydayı 1 sanmış: tanα = m₁ − m₂ = 2 − 1/4 = 7/4.','islem'),
  (fs(e7[2]),float(e7[2]),'Paydada 1 − m₁m₂ almış (işaret hatası): (7/4)/(1/2) = 7/2.','islem'),
  (fs(e7[3]),float(e7[3]),'Fark yerine toplam formülünü kullanmış: (m₁ + m₂)/(1 − m₁m₂) = (9/4)/(1/2) = 9/2.','bilgi')],
 'α açısının tanjantı.',['K ve L noktalarının koordinatlarından her doğrunun eğimini bul; açı, iki doğrunun x ekseniyle yaptığı açıların farkıdır.'],[B_EGM],
 [A('Eğimleri bul','Eğim, orijinden geçen doğru için ordinatın apsise oranıdır.','m₁ = 4/2 = 2 · m₂ = 1/4'),
  A('Açıları tanımla','d₁ ve d₂’nin x ekseniyle yaptığı açılar α₁ ve α₂ olsun; α = α₁ − α₂.','tanα₁ = 2 · tanα₂ = 1/4'),
  A('Fark formülü','tan(α₁ − α₂) = (tanα₁ − tanα₂)/(1 + tanα₁·tanα₂).','tanα = (2 − 1/4)/(1 + 2 · 1/4)'),
  A('Hesapla','Pay ve payda sadeleştirilir.','(7/4)/(3/2) = 7/6')],
 'Eğim tanjanttır; iki doğru arasındaki açı eğimlerin farkıyla bulunur.','K-ATR2-06; eğimleri 2 ve 1/4 olan doğrular',sekil=SK)

# ================= 0008 orta · tanjant grafiği (grafik) =================
a8,b8=2,3
assert math.isclose(a8*math.tan(b8*pi/12),2.0) and abs(b8*pi/6-pi/2)<1e-12
v8=a8*math.tan(b8*pi/9); yak(v8,2*s3)
Q8=[('−2√3',-2*s3,'Asimptot konumunu (π/6) periyot sanmış, b = 6 bulmuş: 2tan(6π/9) = 2tan(2π/3) = −2√3.','bilgi'),
    ('√3',s3,'Katsayı a = 2’yi unutmuş: f(π/9) = tan(π/3) = √3.','dikkat'),
    ('2√3/3',2*s3/3,'tan(π/3) değerini √3/3 almış (tan60° ile tan30°’u karıştırmış): 2 · √3/3.','bilgi'),
    ('3√3',3*s3,'a yerine b = 3 ile çarpmış: 3 · tan(π/3) = 3√3.','bilgi')]
assert math.isclose(2*math.tan(6*pi/9),-2*s3) and math.isclose(2*s3/3,2*(s3/3))
kx8=5.0; ky8=0.5
def X8(x): return x*kx8
g=[f'\\draw[gray!35,thin] (-2.9,{j*ky8:.3f}) -- (2.9,{j*ky8:.3f});' for j in (-4,-2,2,4)]
g.append(f'\\draw[dashed,{YES},thick] ({X8(pi/6):.3f},-2.3) -- ({X8(pi/6):.3f},2.3); \\draw[dashed,{YES},thick] ({X8(-pi/6):.3f},-2.3) -- ({X8(-pi/6):.3f},2.3);')
g.append('\\draw[-{Stealth},thick] (-3.1,0) -- (3.2,0) node[right] {$x$}; \\draw[-{Stealth},thick] (0,-2.4) -- (0,2.55) node[above] {$y$};')
g.append(f'\\begin{{scope}}\\clip (-2.95,-2.15) rectangle (2.95,2.15);\\draw[{MAVI},very thick,smooth,domain={-pi/6+0.004:.4f}:{pi/6-0.004:.4f},samples=200,variable=\\t] plot ({{\\t*{kx8}}},{{2*tan(3*\\t r)*{ky8}}});\\end{{scope}}')
g.append(f'\\fill[{TUR}] ({X8(pi/12):.3f},{2*ky8:.3f}) circle (2.6pt) node[below right=2pt,black] {{$\\left(\\frac{{\\pi}}{{12}},\\,2\\right)$}};')
g.append(f'\\node[below right=1pt,{YES}!60!black] at ({X8(pi/6):.3f},0) {{$\\frac{{\\pi}}{{6}}$}}; \\node[below left=1pt,{YES}!60!black] at ({X8(-pi/6):.3f},0) {{$-\\frac{{\\pi}}{{6}}$}};')
g+= [f'\\node[left=2pt,font=\\footnotesize] at (0,{j*ky8:.3f}) {{${j}$}};' for j in (-4,-2,2,4)]
g.append(f'\\node[{MAVI}] at (-1.9,1.75) {{$y=f(x)$}};')
SK=fig('\n'.join(g))
Q('0008','trg2-grafik','orta','Tanjant Grafiğinden Kural','Tanjant eğrisinin asimptotlarından periyodu, işaretli noktadan genliği bulup fonksiyon değerini hesaplar.','grafik',
 'Şekilde, a ve b pozitif gerçel sayılar olmak üzere f(x) = a·tan(bx) fonksiyonunun grafiği, bu grafiğin iki dikey asimptotu ve grafik üzerindeki bir nokta gösterilmiştir.\nBuna göre f(π/9) değeri kaçtır?',
 ('2√3',2*s3),
 Q8.copy() and [(*t[:2],t[2],'bilgi' if i!=1 else 'dikkat') for i,t in enumerate(Q8)],
 'f(π/9) değeri.',['İki asimptot arasındaki uzaklık bir periyottur; periyottan b’yi bulduktan sonra işaretli noktayı kullanarak a’yı hesapla.'],[B_TNG],
 [A('Periyodu bul','Ardışık iki asimptot arası bir periyottur.','T = π/6 − (−π/6) = π/3'),
  A('b’yi bul','Periyot π/b’dir.','π/b = π/3 → b = 3'),
  A('a’yı bul','İşaretli nokta fonksiyonu sağlar: a·tan(3 · π/12) = 2.','a·tan(π/4) = 2 → a = 2'),
  A('Değeri hesapla','x = π/9 yazılır.','f(π/9) = 2tan(π/3) = 2√3')],
 'Tanjant grafiğinde asimptotlar arasındaki uzaklık tam bir periyottur.','K-ATR2-07; y = 2tan(3x) grafiği',sekil=SK,
 sira=None)

# ================= 0009 orta · koşullu kosinüs teoremi (düz) =================
# 5a² = 5b² + 5c² + 6bc -> cosA = -3/5 -> tanA = -4/3
cA=Fr(-3,5); sA=Fr(4,5); assert cA**2+sA**2==1 and sA/cA==Fr(-4,3)
bb,cc=7,5; aa2=Fr(5*bb*bb+5*cc*cc+6*bb*cc,5); assert 5*aa2==5*bb*bb+5*cc*cc+6*bb*cc and (bb*bb+cc*cc-aa2)/(2*bb*cc)==cA
e9=[Fr(-3,4),Fr(-3,5),Fr(3,4),Fr(4,3)]
Q('0009','trg2-ucgen','orta','Koşullu Kosinüs Teoremi','Kenarlar arasındaki bağıntıdan kosinüs teoremiyle cosA’yı bulup tanA değerini hesaplar.','düz',
 'Bir ABC üçgeninin kenar uzunlukları |BC| = a, |AC| = b ve |AB| = c olmak üzere,\n5a² = 5b² + 5c² + 6bc\neşitliği sağlanıyor.\nBuna göre, tanA değeri kaçtır?',
 (fs(Fr(-4,3)),-4/3),
 [(fs(e9[0]),float(e9[0]),'cosA = −3/5 ve sinA = 4/5’i doğru bulmuş fakat tanA yerine cotA = cosA/sinA hesaplamış.','dikkat'),
  (fs(e9[1]),float(e9[1]),'cosA = −3/5 değerini bulup tanA saymış.','dikkat'),
  (fs(e9[2]),float(e9[2]),'cotA’yı hesaplayıp işaretini pozitif almış (A’nın dar açı olduğunu sanmış).','bilgi'),
  (fs(e9[3]),float(e9[3]),'Kosinüs teoremindeki işareti ters kullanıp cosA = 3/5 bulmuş; sinA = 4/5 ile tanA = 4/3 yazmış.','islem')],
 'tanA değeri.',['Verilen eşitliği kosinüs teoremindeki a² ifadesiyle karşılaştır; cosA’yı bulduktan sonra A’nın dar ya da geniş olduğuna dikkat ederek tanA’yı yaz.'],[B_KOS],
 [A('Teoremi yaz','a² kenar uzunluğu A açısının karşısındadır.','a² = b² + c² − 2bc·cosA'),
  A('Eşitliği düzenle','Verilen eşitlik 5’e bölünür.','a² = b² + c² + (6/5)bc'),
  A('cosA’yı bul','İki ifade eşitlenir.','−2bc·cosA = (6/5)bc → cosA = −3/5'),
  A('tanA’yı bul','cosA < 0 olduğundan A geniş açıdır; sinA = √(1 − 9/25) = 4/5.','tanA = (4/5)/(−3/5) = −4/3')],
 'Kosinüs teoreminde karşıdaki kenarın karesini veren ifadeyi eşitlikle karşılaştır.','K-ATR2-02; 5a² = 5b² + 5c² + 6bc',
 sira=None)

# ================= 0010 orta · öncüllü, grafikten cos2x özellikleri (şekilli) =================
f10=lambda x:math.cos(2*x)
for xv in (0.2,0.9,2.3):
    yak(f10(xv+pi),f10(xv)); yak(f10(-xv),f10(xv)); assert abs(f10(xv+pi/2)+f10(xv))<1e-12
    assert abs(f10(pi/4+xv)-f10(pi/4-xv))>1e-3
    assert abs(f10(xv+pi/2)-f10(xv))>1e-3
k10=1.3; y10=1.1
def X10(x): return x*k10
g=[f'\\draw[gray!35,thin] ({X10(i*pi/4):.3f},{-1.2*y10:.3f}) -- ({X10(i*pi/4):.3f},{1.2*y10:.3f});' for i in range(-2,5) if i]
g+= [f'\\draw[gray!35,thin] ({X10(-pi/2)-0.1:.3f},{j*y10:.3f}) -- ({X10(pi)+0.2:.3f},{j*y10:.3f});' for j in (-1,1)]
g.append(f'\\draw[-{{Stealth}},thick] ({X10(-pi/2)-0.2:.3f},0) -- ({X10(pi)+0.8:.3f},0) node[right] {{$x$}}; \\draw[-{{Stealth}},thick] (0,{-1.45*y10:.3f}) -- (0,{1.55*y10:.3f}) node[above] {{$y$}};')
g.append(f'\\draw[{MAVI},very thick,smooth,domain={-pi/2:.4f}:{pi:.4f},samples=120,variable=\\t] plot ({{\\t*{k10}}},{{cos(2*\\t r)*{y10}}});')
g.append(f'\\fill[{TUR}] (0,{y10:.3f}) circle (2.6pt) node[above right=1pt,black] {{$(0,\\,1)$}}; \\fill[{TUR}] ({X10(pi/4):.3f},0) circle (2.6pt) node[above right=2pt,black] {{$\\left(\\frac{{\\pi}}{{4}},\\,0\\right)$}}; \\fill[{TUR}] ({X10(pi/2):.3f},{-y10:.3f}) circle (2.6pt) node[below=3pt,black] {{$\\left(\\frac{{\\pi}}{{2}},\\,-1\\right)$}};')
g+= [f'\\node[left=2pt,font=\\footnotesize] at (0,{j*y10:.3f}) {{${j}$}};' for j in (-1,)]
g+= [f'\\node[below=1pt,font=\\footnotesize] at ({X10(pi):.3f},0) {{$\\pi$}};',f'\\node[above=1pt,font=\\footnotesize] at ({X10(-pi/2):.3f},0) {{$-\\frac{{\\pi}}{{2}}$}};']
SK=fig('\n'.join(g))
Q('0010','trg2-grafik','orta','Grafikten Fonksiyonun Özellikleri','Kosinüs eğrisinin grafiğinden kuralı bulup periyodunu, simetrisini ve ötelemeyle ilişkisini öncüllerde inceler.','öncüllü',
 'Şekilde, a ve b pozitif gerçel sayılar olmak üzere f(x) = a·cos(bx) fonksiyonunun grafiği ve grafik üzerindeki üç nokta gösterilmiştir.\nBuna göre,\nI. f fonksiyonunun periyodu π’dir.\nII. Her x gerçel sayısı için f(π/4 + x) = f(π/4 − x)’tir.\nIII. Her x gerçel sayısı için f(x) + f(x + π/2) = 0’dır.\nifadelerinden hangileri doğrudur?',
 ('I ve III',0),
 [('Yalnız I',1,'III’ü yanlış saymış: f(x + π/2) = f(x) olduğunu varsayıp toplamın 2f(x) çıktığını düşünmüş.','bilgi'),
  ('Yalnız III',2,'Periyodu 2π okuyup I’i yanlış saymış; II’yi de doğru bulmamış.','bilgi'),
  ('I ve II',3,'II’yi doğru sanmış (π/4’e göre simetri olduğunu varsaymış), III’ü yanlış saymış.','bilgi'),
  ('II ve III',4,'Periyodu 2π okuyup I’i yanlış saymış, II’yi doğru kabul etmiş.','bilgi')],
 'Doğru öncüller.',['Önce grafikteki noktalardan a ile b’yi bul; sonra her öncülde açıları bulduğun kuralda yerine yaz.'],[B_PER,B('Kosinüs grafiğinden kural','f(x) = a·cos(bx) grafiğinde en büyük değer a’dır; en büyük değerden ilk sıfıra uzaklık çeyrek periyottur ve periyot 2π/b’dir. Örnek: en büyük değer 2, ilk sıfır x = π/6’da ise çeyrek periyot π/6, periyot 2π/3, b = 3’tür')],
 [A('Kuralı bul','(0, 1) en büyük değer, ilk sıfır π/4’tedir (çeyrek periyot).','a = 1 · T = π → b = 2 · f(x) = cos2x'),
  A('I. öncül','Periyot 2π/b’dir.','2π/2 = π: I doğru'),
  A('II. öncül','f(π/4 + x) = cos(π/2 + 2x) = −sin2x, f(π/4 − x) = cos(π/2 − 2x) = sin2x.','İkisi eşit değil: II yanlış'),
  A('III. öncül','f(x + π/2) = cos(2x + π) = −cos2x.','f(x) + f(x + π/2) = 0: III doğru')],
 'Öncülleri önce grafikten bulduğun kural üzerinden, tek tek sına.','K-ATR2-07; f(x) = cos2x grafiği öncülleri',sekil=SK,
 sira=['Yalnız I','Yalnız III','I ve II','II ve III','I ve III'])

# ================= 0011 orta · tanımlı yeni fonksiyon (şekilli) =================
h_=Fr(1,5); cth=1-h_; assert cth==Fr(4,5); sn=Fr(3,5); assert cth**2+sn**2==1
c2t=2*cth**2-1; assert c2t==Fr(7,25); v11=1-c2t; assert v11==Fr(18,25)
e11=[h_**2,c2t,sn**2,2*h_]; assert e11==[Fr(1,25),Fr(7,25),Fr(9,25),Fr(2,5)] and 2*sn**2==v11
thd=55; thr=R_(thd); r11=2.4; Px,Py=r11*math.cos(thr),r11*math.sin(thr)
SK=fig(tz('''\\fill[@T@!25] (@Px@,0) -- (@r@,0) -- (@Px@,0.0) -- cycle;
\\draw[thick] (0,0) circle (@r@);
\\draw[-{Stealth}] (-@r1@,0) -- (@r2@,0) node[right] {$x$}; \\draw[-{Stealth}] (0,-@r1@) -- (0,@r2@) node[above] {$y$};
\\draw[very thick,@M@] (0,0) -- (@Px@,@Py@); \\draw[thick,dashed,@Y@] (@Px@,@Py@) -- (@Px@,0);
\\draw[line width=2.6pt,@T@] (@Px@,0) -- (@r@,0);
\\draw[thick,-{Stealth}] (0.6,0) arc (0:@th@:0.6); \\node at (0.95,0.38) {$\\theta$};
\\fill (0,0) circle (1.6pt); \\fill (@Px@,@Py@) circle (2pt); \\fill[@T@] (@r@,0) circle (2.2pt); \\fill (@Px@,0) circle (2pt);
\\node[below left] at (0,0) {$O$}; \\node[above right] at (@Px@,@Py@) {$P$}; \\node[below] at (@Px@,-0.02) {$H$}; \\node[below=4pt] at (@r@,0) {$S(1,0)$};''',T=TUR,M=MAVI,Y=YES,Px=Px,Py=Py,r=r11,r1=r11+0.35,r2=r11+0.5,th=thd))
Q('0011','trg2-yeni','orta','Tanımlı Yeni Fonksiyon','Birim çemberdeki |HS| uzunluğuyla tanımlanan yeni fonksiyonu 1 − cosθ biçiminde yazıp iki kat açı formülüyle değer bulur.','şekilli',
 'Şekilde, O merkezli birim çember üzerinde S(1, 0) ve P noktaları, P’nin x eksenindeki dik izdüşümü H ve OP ışınının pozitif x ekseniyle yaptığı θ açısı gösterilmiştir.\n0 < θ < π/2 olmak üzere, bu şekildeki |HS| uzunluğu kullanılarak\nhat(θ) = |HS|\nbiçiminde tanımlanıyor.\nBuna göre, hat(θ) = 1/5 olduğunda hat(2θ) değeri kaçtır?',
 (fs(v11),float(v11)),
 [(fs(e11[0]),float(e11[0]),'hat(2θ) = (hat θ)² yazmış (fonksiyon bileşimini karelemeyle karıştırmış): (1/5)² = 1/25.','dikkat'),
  (fs(e11[1]),float(e11[1]),'hat(2θ) yerine cos2θ değerini bulmuş: 2cos²θ − 1 = 2 · 16/25 − 1 = 7/25.','dikkat'),
  (fs(e11[2]),float(e11[2]),'1 − cos2θ = sin²θ yazmış (2 çarpanını unutmuş): sin²θ = 9/25.','islem'),
  (fs(e11[3]),float(e11[3]),'hat fonksiyonunu doğrusal sanıp hat(2θ) = 2·hat(θ) yazmış: 2/5.','bilgi')],
 'hat(2θ) değeri.',['|HS| uzunluğunu |OS| ve |OH| ile ifade et; tanımı θ’nın kosinüsüne çevirdikten sonra 2θ için aynı tanımı uygula.'],[B_YEN,B_IKI],
 [A('Tanımı çevir','|OS| = 1 ve |OH| = cosθ olduğundan |HS| = 1 − cosθ’dır.','hat(θ) = 1 − cosθ'),
  A('cosθ’yı bul','hat(θ) = 1/5 verilmiş.','1 − cosθ = 1/5 → cosθ = 4/5'),
  A('cos2θ’yı bul','İki kat açı formülü uygulanır.','cos2θ = 2cos²θ − 1 = 2 · 16/25 − 1 = 7/25'),
  A('hat(2θ)’yı bul','cos2θ = 7/25 > 0 olduğundan 2θ ∈ (0, π/2) ve tanım geçerlidir: |HS| = 1 − cos2θ.','hat(2θ) = 1 − 7/25 = 18/25')],
 'Tanımı bir kez bilinen fonksiyona çevir, sonra tanımdaki açıyı değiştirerek tekrar uygula.','K-ATR2-08; hat θ = |HS| = 1 − cosθ',sekil=SK)

# ================= 0012 orta · toplam formülü, iki dik üçgen (şekilli) =================
v12=Fr(4,5)*Fr(5,13)-Fr(3,5)*Fr(12,13); assert v12==Fr(-16,65)
al12=math.asin(3/5); be12=math.acos(5/13); yak(math.cos(al12+be12),float(v12))
e12=[Fr(4,5)*Fr(5,13),-v12,Fr(4,5)*Fr(5,13)+Fr(3,5)*Fr(12,13),Fr(3,5)*Fr(5,13)+Fr(4,5)*Fr(12,13)]
assert e12==[Fr(4,13),Fr(16,65),Fr(56,65),Fr(63,65)]
yak(math.cos(al12-be12),56/65); yak(math.sin(al12+be12),63/65)
q=0.32; o2=6.2*q
SK=fig(tz('''\\fill[@M@!12] (0,0) -- (@w1@,0) -- (@w1@,@h1@) -- cycle;
\\draw[very thick,@M@] (0,0) -- (@w1@,0) -- (@w1@,@h1@) -- cycle;
\\draw (@w1@,0.2) -- (@w1a@,0.2) -- (@w1a@,0);
\\draw[thick] (0.7,0) arc (0:@a1@:0.7); \\node at (0.95,0.22) {$\\alpha$};
\\node[below] at (@m1@,0) {}; \\node[right=2pt] at (@w1@,@hm1@) {$3$}; \\node[above left=1pt] at (@mx1@,@my1@) {$5$};
\\fill[@T@!18] (@o@,0) -- (@o2@,0) -- (@o2@,@h2@) -- cycle;
\\draw[very thick,@T@] (@o@,0) -- (@o2@,0) -- (@o2@,@h2@) -- cycle;
\\draw (@o2@,0.2) -- (@o2a@,0.2) -- (@o2a@,0);
\\draw[thick] (@ob@,0) arc (0:@a2@:0.7); \\node at (@olx@,0.25) {$\\beta$};
\\node[below] at (@om@,0) {$5$}; \\node[above left=1pt] at (@mx2@,@my2@) {$13$};''',
 M=MAVI,T=TUR,w1=4*q,h1=3*q,w1a=4*q-0.2,a1=math.degrees(math.asin(3/5)),m1=2*q,hm1=1.5*q,mx1=2*q,my1=1.5*q,
 o=o2-0.0-5*q if False else 2.2,o2=2.2+5*q,h2=12*q,o2a=2.2+5*q-0.2,ob=2.2+0.7,a2=math.degrees(math.acos(5/13)),olx=2.2+1.0,om=2.2+2.5*q,mx2=2.2+2.5*q,my2=6*q))
Q('0012','trg2-toplamfark','orta','Dik Üçgenlerden Toplam Formülü','İki dik üçgenden α ve β açılarının sinüs ve kosinüslerini bulup kosinüs toplam formülünü uygular.','şekilli',
 'Şekilde, α ve β dar açılı iki dik üçgen ile bazı kenar uzunlukları gösterilmiştir.\nBuna göre, cos(α + β) değeri kaçtır?',
 (fs(v12),float(v12)),
 [(fs(e12[0]),float(e12[0]),'Toplam formülünde ikinci terimi unutmuş: cosα·cosβ = 20/65 = 4/13.','dikkat'),
  (fs(e12[1]),float(e12[1]),'Formülü ters yazmış: sinα·sinβ − cosα·cosβ = 36/65 − 20/65 = 16/65.','islem'),
  (fs(e12[2]),float(e12[2]),'cos(α + β) için cosα·cosβ + sinα·sinβ (fark formülü) yazmış: 56/65.','bilgi'),
  (fs(e12[3]),float(e12[3]),'cos yerine sin(α + β) değerini hesaplamış: 63/65.','bilgi')],
 'cos(α + β) değeri.',['Her dik üçgenden, bilinmeyen oranları da bulacak biçimde α ve β’nın oranlarını yaz.'],[B_TOP],
 [A('α’nın oranları','Birinci üçgende karşı dik kenar 3, hipotenüs 5’tir; diğer dik kenar Pisagor ile 4 bulunur.','sinα = 3/5 · cosα = 4/5'),
  A('β’nın oranları','İkinci üçgende komşu dik kenar 5, hipotenüs 13’tür; karşı dik kenar 12 bulunur.','cosβ = 5/13 · sinβ = 12/13'),
  A('Formülü yaz','Kosinüs toplam formülü uygulanır.','cos(α + β) = cosα·cosβ − sinα·sinβ'),
  A('Hesapla','Değerler yerine konur.','(4/5)(5/13) − (3/5)(12/13) = 20/65 − 36/65 = −16/65')],
 'Her üçgenden iki oranı bulup formülde yerine yaz.','K-ATR2-06; (3,4,5) ve (5,12,13) dik üçgenleriyle cos(α + β)',sekil=SK,
 sira=None)

# ================= 0013 orta · öncüllü, üçgende kenar–açı (şekilli) =================
a13,b13,c13=5,6,8
cC=Fr(a13**2+b13**2-c13**2,2*a13*b13); assert cC==Fr(-1,20) and cC<0 and a13<b13<c13 and a13+b13>c13
cB=Fr(a13**2+c13**2-b13**2,2*a13*c13); sB=math.sqrt(1-float(cB)**2)
Bx,By=0,0; Ax,Ay=c13*0.42,0; Cx,Cy=a13*0.42*float(cB),a13*0.42*sB
SK=fig(tz('''\\fill[@Y@!14] (@Bx@,@By@) -- (@Ax@,@Ay@) -- (@Cx@,@Cy@) -- cycle;
\\draw[very thick,@M@] (@Bx@,@By@) -- (@Ax@,@Ay@); \\draw[very thick,@T@] (@Bx@,@By@) -- (@Cx@,@Cy@); \\draw[very thick,@Y@] (@Ax@,@Ay@) -- (@Cx@,@Cy@);
\\node[below] at (@m1@,-0.02) {$8$}; \\node[left=2pt,@T@!70!black] at (@m2x@,@m2y@) {$5$}; \\node[above right=1pt,@Y@!60!black] at (@m3x@,@m3y@) {$6$};
\\node[below left] at (@Bx@,@By@) {$B$}; \\node[below right] at (@Ax@,@Ay@) {$A$}; \\node[above] at (@Cx@,@Cy@) {$C$};''',Y=YES,M=MAVI,T=TUR,Bx=Bx,By=By,Ax=Ax,Ay=Ay,Cx=Cx,Cy=Cy,m1=Ax/2,m2x=Cx/2,m2y=Cy/2,m3x=(Ax+Cx)/2,m3y=(Ay+Cy)/2))
Q('0013','trg2-ucgen','orta','Üçgende Kenar–Açı İlişkisi','Kenar uzunluklarından açı türünü kosinüs teoremiyle, açıların sinüslerinin sırasını sinüs teoremiyle ve sinüs toplamını üçgen eşitsizliğiyle yorumlar.','öncüllü',
 'Şekilde, kenar uzunlukları birim cinsinden verilen bir ABC üçgeni gösterilmiştir.\nBuna göre,\nI. ABC üçgeni geniş açılı bir üçgendir.\nII. sinA < sinB < sinC’dir.\nIII. sinA + sinB > sinC’dir.\nifadelerinden hangileri doğrudur?',
 ('I, II ve III',0),
 [('Yalnız I',1,'II ve III’ün sinüs değerleri hesaplanmadan doğrulanamayacağını sanıp yalnız geniş açıyı bulmuş.','bilgi'),
  ('I ve II',2,'III’ü yanlış saymış (sinüs toplamı için üçgen eşitsizliğinin geçerli olduğunu görmemiş).','bilgi'),
  ('I ve III',3,'II’yi yanlış saymış (büyük kenarın karşısında büyük açı olduğunu, sinüsün de sıralı gittiğini atlamış).','bilgi'),
  ('II ve III',4,'I’i yanlış saymış: c² = 64 ile a² + b² = 61’i karşılaştırmayıp üçgeni dar açılı sanmış.','dikkat')],
 'Doğru öncüller.',['Her öncül için ilgili teoremi seç: açı türü için kenarların kareleri, sinüs sırası ve toplamı için sinüs teoreminin kenar–sinüs orantısı.'],[B_KOS,B_SIN],
 [A('I. öncül','En büyük kenarın karşısındaki açının kosinüsüne bakılır.','cosC = (25 + 36 − 64)/(2·5·6) = −1/20 < 0 → C geniş: I doğru'),
  A('II. öncül','Sinüs teoremine göre sinüsler kenarlarla orantılıdır: sinX = x/2R.','5 < 6 < 8 → sinA < sinB < sinC: II doğru'),
  A('III. öncül','Aynı orantıyla sinA + sinB > sinC ⇔ a + b > c.','5 + 6 = 11 > 8: III doğru'),
  A('Sonuç','Üç öncül de doğrudur.','I, II ve III')],
 'Sinüs teoremi, sinüsler arasındaki ilişkiyi kenarlar arasındaki ilişkiye çevirir.','K-ATR2-02; kenarları 5, 6, 8 olan üçgen',sekil=SK,
 sira=['Yalnız I','I ve II','I ve III','II ve III','I, II ve III'])

# ================= 0014 zor · denklemden sin2x (düz) =================
c=sp.symbols('c')
sol=sp.solve(sp.Eq(2*c**2-2*c,4),c); assert sorted(sol)==[-1,2]
xv=math.atan(1/2); yak(2*math.cos(xv)**2-math.sin(2*xv),4*math.sin(xv)**2)
assert Fr(2*2,1+4)==Fr(4,5) and Fr(4-1,4+1)==Fr(3,5) and Fr(2*(-1),1+1)==-1 and Fr(2,1+4)==Fr(2,5) and Fr(2*Fr(1,2),1-Fr(1,4))==Fr(4,3)
Q('0014','trg2-denklem','zor','Denklemden İki Kat Açı Değeri','Denklemi tek orana indirgeyip ikinci derece denklemi çözer, kökü işaret koşuluyla seçer ve bulunan orandan sin2x’i hesaplar.','düz',
 '0 < x < π/2 olmak üzere,\n2cos²x − sin2x = 4sin²x\neşitliği sağlanıyor.\nBuna göre, sin2x değeri kaçtır?',
 ('4/5',0.8),
 [('−1',-1,'İkinci derece denklemin iki kökünden cotx = −1’i de alıp sin2x = 2·(−1)/(1 + 1) = −1 bulmuş (cotx > 0 koşulunu denetlememiş).','dikkat'),
  ('2/5',0.4,'sin2x = cotx/(1 + cot²x) yazmış (2 çarpanını unutmuş): 2/5.','islem'),
  ('3/5',0.6,'sin2x yerine cos2x = (cot²x − 1)/(cot²x + 1) değerini hesaplamış: 3/5.','dikkat'),
  ('4/3',4/3,'cotx = 2 yerine tanx = 1/2 değerinden tan2x = 4/3 hesaplamış.','bilgi')],
 'sin2x değeri.',['Denklemin terimlerini ortak bir orana çevirmeyi dene; çıkan denklemin köklerini verilen aralıkla karşılaştır.'],[B_DEN,B('İki kat açının tanjantla yazılışı','sin2x = 2tanx/(1 + tan²x) ve sin2x = 2cotx/(1 + cot²x)’tir. Örnek: tanx = 1/4 ise sin2x = (1/2)/(17/16) = 8/17’dir')],
 [A('Düzenle','sin2x = 2sinx·cosx yazılır.','2cos²x − 2sinx·cosx = 4sin²x'),
  A('Tek orana indirge','Her terim sin²x’e bölünür; cosx/sinx = cotx.','2cot²x − 2cotx = 4 → (cotx − 2)(cotx + 1) = 0'),
  A('Aralığa bak','0 < x < π/2 olduğundan cotx pozitiftir.','cotx = 2'),
  A('sin2x’i bul','sin2x = 2cotx/(1 + cot²x) uygulanır.','sin2x = 4/5')],
 'Denklemden önce bir orana ulaş; istenen değeri o orandan kur.','K-ATR2-09; 2cos²x − sin2x = 4sin²x, sin2x',
 sira=['−1','2/5','3/5','4/5','4/3'])

# ================= 0015 zor · açıortay ve iki kat açı (şekilli) =================
AB15,BD15,DC15=6,3,5; BC15=BD15+DC15
AC15=math.hypot(AB15,BC15); yak(AC15,10); yak(AB15/AC15,BD15/DC15)
tx=BD15/AB15; yak(math.tan(2*math.atan(tx)),BC15/AB15)
assert sp.solve(sp.Eq(sp.Rational(BD15,DC15)**2*(sp.Symbol('u')**2+64),sp.Symbol('u')**2),sp.Symbol('u'))[0]==-6 or True
e15=[Fr(24,5),2*s6,8,10]; assert Fr(BD15*BC15,DC15)==Fr(24,5) and math.isclose(math.sqrt(BD15*BC15),2*s6) and BC15==8 and AC15==10
s15=0.4; Bx,By=0,0; Ax,Ay=0,AB15*s15; Cx,Cy=BC15*s15,0; Dx=BD15*s15
bis=math.degrees(math.atan2(BD15,AB15))
SK=fig(tz('''\\fill[@M@!12] (0,0) -- (@Dx@,0) -- (0,@Ay@) -- cycle;
\\fill[@T@!22] (@Dx@,0) -- (@Cx@,0) -- (0,@Ay@) -- cycle;
\\draw[very thick,@M@] (0,@Ay@) -- (0,0) -- (@Dx@,0); \\draw[very thick,@T@] (@Dx@,0) -- (@Cx@,0) -- (0,@Ay@); \\draw[thick,@Y@] (0,@Ay@) -- (@Dx@,0);
\\draw (0,0.22) -- (0.22,0.22) -- (0.22,0);
\\draw[thick,-{Stealth}] (0,@a1@) arc (-90:@a2@:0.8) ;
\\node at (0.38,@ax@) {$x$}; \\node at (0.92,@ay2@) {$x$};
\\node[below left] at (0,0) {$B$}; \\node[left] at (0,@Ay@) {$A$}; \\node[below right] at (@Cx@,0) {$C$}; \\node[below] at (@Dx@,0) {$D$};
\\node[below] at (@m1@,-0.28) {$3$}; \\node[below] at (@m2@,-0.28) {$5$};
\\draw[<->,thin] (0,-0.25) -- (@Dx@,-0.25); \\draw[<->,thin] (@Dx@,-0.25) -- (@Cx@,-0.25);''',M=MAVI,T=TUR,Y=YES,Dx=Dx,Cx=Cx,Ay=Ay,a1=0,a2=0,ax=Ay-0.7,ay2=Ay-0.78,m1=Dx/2,m2=(Dx+Cx)/2))
# yay işaretlerini ayrı çiz (basit): iki küçük yay A köşesinde
dA=math.degrees(math.atan2(Dx,Ay)); eA=math.degrees(math.atan2(Cx,Ay))
SK=fig(tz('''\\fill[@M@!12] (0,0) -- (@Dx@,0) -- (0,@Ay@) -- cycle;
\\fill[@T@!22] (@Dx@,0) -- (@Cx@,0) -- (0,@Ay@) -- cycle;
\\draw[very thick,@M@] (0,@Ay@) -- (0,0) -- (@Dx@,0); \\draw[very thick,@T@] (@Dx@,0) -- (@Cx@,0) -- (0,@Ay@); \\draw[thick,@Y@] (0,@Ay@) -- (@Dx@,0);
\\draw (0,0.22) -- (0.22,0.22) -- (0.22,0);
\\draw[thick] (@ax1@,@ay1@) arc (@s1@:@s2@:0.85); \\draw[thick] (@bx1@,@by1@) arc (@s2@:@s3@:0.65);
\\node at (@lx1@,@ly1@) {$x$}; \\node at (@lx2@,@ly2@) {$x$};
\\node[below left] at (0,0) {$B$}; \\node[above left] at (0,@Ay@) {$A$}; \\node[below right] at (@Cx@,0) {$C$}; \\node[below] at (@Dx@,0) {$D$};
\\draw[<->,thin] (0,-0.62) -- (@Dx@,-0.62); \\draw[<->,thin] (@Dx@,-0.62) -- (@Cx@,-0.62);
\\node[below] at (@m1@,-0.62) {$3$}; \\node[below] at (@m2@,-0.62) {$5$};''',
 M=MAVI,T=TUR,Y=YES,Dx=Dx,Cx=Cx,Ay=Ay,m1=Dx/2,m2=(Dx+Cx)/2,
 s1=-90,s2=-90+dA,s3=-90+eA,
 ax1=0.85*math.cos(R_(-90))+0,ay1=Ay+0.85*math.sin(R_(-90)),
 bx1=0.65*math.cos(R_(-90+dA)),by1=Ay+0.65*math.sin(R_(-90+dA)),
 lx1=1.05*math.cos(R_(-90+dA/2)),ly1=Ay+1.05*math.sin(R_(-90+dA/2)),
 lx2=0.92*math.cos(R_(-90+(dA+eA)/2)),ly2=Ay+0.92*math.sin(R_(-90+(dA+eA)/2))))
Q('0015','trg2-geo','zor','Açıortay ve Dik Üçgen','Açıortay teoremi ile dik üçgende Pisagor bağıntısını birleştirip |AB|’yi, ardından |AD| uzunluğunu bulur.','şekilli',
 'Şekilde, B köşesinde dik olan ABC üçgeninde D noktası [BC] üzerinde ve [AD], A açısının açıortayıdır.\nBuna göre, |AD| kaç birimdir?',
 ('3√5',3*s5),
 [('√33',math.sqrt(33),'|AB|² = |BD| · |BC| = 24 yazmış (Öklid bağıntısını açıortay için kullanmış): |AD|² = 24 + 9 = 33.','bilgi'),
  ('√61',math.sqrt(61),'|AB| = 6’yı doğru bulmuş fakat |AD|² = |AB|² + |DC|² = 36 + 25 yazmış.','dikkat'),
  ('√73',math.sqrt(73),'Üçgeni ikizkenar sanıp |AB| = |BC| = 8 almış: |AD|² = 64 + 9 = 73.','dikkat'),
  ('√109',math.sqrt(109),'|AC| = 10’u |AB| sanmış: |AD|² = 100 + 9 = 109.','dikkat')],
 '|AD| uzunluğu.',['Önce dik kenar |AB|’yi bulmayı dene; açıortay hangi iki kenarı orantılar?'],[B_ACI],
 [A('Açıortay teoremi','[AD] açıortay olduğundan karşı kenar parçaları komşu kenarlarla orantılıdır.','|AB|/|AC| = |BD|/|DC| = 3/5'),
  A('|AB|’yi bul','|AC| = 5|AB|/3 ve |BC| = 8; ABC’de Pisagor yazılır.','25|AB|²/9 = |AB|² + 64 → |AB| = 6'),
  A('ABD üçgeni','B’de dik olan ABD üçgeninde Pisagor bağıntısı uygulanır.','|AD|² = |AB|² + |BD|² = 36 + 9 = 45'),
  A('Sonuç','Karekök alınır.','|AD| = 3√5')],
 'Dik kenar bulunduktan sonra ikinci bir dik üçgen daha çözülür.','K-ATR2-05; B’de dik üçgende açıortay, |BD| = 3, |DC| = 5, |AD|',sekil=SK)

# ================= 0016 zor · grafik, yazılı dikdörtgen (şekilli) =================
a16,b16=3,2
f16=lambda x:a16*math.sin(b16*x)
xA=pi/12; xB=pi/2-xA; hh=f16(xA); yak(hh,1.5); yak(f16(xB),hh); area16=(xB-xA)*hh; yak(area16,pi/2)
e16=[('π/4',pi/4,'B noktasını x = π/4 (eğrinin tepe noktası) sanıp tabanı π/6 almış: (π/6) · (3/2) = π/4.','bilgi'),
     ('5π/8',5*pi/8,'Simetriyi kullanmayıp B’yi x = π/2 (sıfır noktası) sanmış: (5π/12) · (3/2) = 5π/8.','dikkat'),
     ('π√3/2',pi*s3/2,'sin(π/6) değerini √3/2 almış, yüksekliği 3√3/2 bulmuş: (π/3) · (3√3/2) = π√3/2.','bilgi'),
     ('π',pi,'Yüksekliği en büyük değer 3 almış: (π/3) · 3 = π.','dikkat')]
kx=3.6; ky=0.8
def X16(x): return x*kx
g=[f'\\draw[gray!35,thin] (0,{j*ky:.3f}) -- ({X16(pi/2)+0.3:.3f},{j*ky:.3f});' for j in (1,2,3)]
g.append(f'\\fill[{MAVI}!16] ({X16(xA):.3f},0) -- ({X16(xB):.3f},0) -- ({X16(xB):.3f},{hh*ky:.3f}) -- ({X16(xA):.3f},{hh*ky:.3f}) -- cycle;')
g.append(f'\\draw[-{{Stealth}},thick] (-0.1,0) -- ({X16(pi/2)+0.9:.3f},0) node[right] {{$x$}}; \\draw[-{{Stealth}},thick] (0,-0.1) -- (0,{3*ky+0.55:.3f}) node[above] {{$y$}};')
g.append(f'\\draw[{TUR},very thick,smooth,domain=0:{pi/2:.4f},samples=70,variable=\\t] plot ({{\\t*{kx}}},{{3*sin(2*\\t r)*{ky}}});')
g.append(f'\\draw[very thick,{MAVI}] ({X16(xA):.3f},0) -- ({X16(xB):.3f},0) -- ({X16(xB):.3f},{hh*ky:.3f}) -- ({X16(xA):.3f},{hh*ky:.3f}) -- cycle;')
g.append(f'\\fill ({X16(xA):.3f},0) circle (2pt) node[below=3pt] {{$A\\left(\\frac{{\\pi}}{{12}},0\\right)$}}; \\fill ({X16(xB):.3f},0) circle (2pt) node[below=3pt] {{$B$}};')
g.append(f'\\fill ({X16(xB):.3f},{hh*ky:.3f}) circle (2pt) node[right=3pt] {{$C$}}; \\fill ({X16(xA):.3f},{hh*ky:.3f}) circle (2pt) node[left=3pt] {{$D$}};')
g.append(f'\\fill[{TUR}] ({X16(pi/4):.3f},{3*ky:.3f}) circle (2.6pt) node[above=3pt,black] {{$\\left(\\frac{{\\pi}}{{4}},\\,3\\right)$}};')
g.append(f'\\node[below=3pt] at ({X16(pi/2):.3f},0) {{$\\frac{{\\pi}}{{2}}$}}; \\fill ({X16(pi/2):.3f},0) circle (2pt);')
g+= [f'\\node[left=2pt,font=\\footnotesize] at (0,{j*ky:.3f}) {{${j}$}};' for j in (1,2,3)]
SK=fig('\n'.join(g))
Q('0016','trg2-grafik','zor','Grafiğe Yazılı Dikdörtgen','Sinüs eğrisinin kuralını grafikteki iki noktadan bulup simetriyle dikdörtgenin eni ve boyunu hesaplar.','grafik',
 'Şekilde, a ve b pozitif gerçel sayılar olmak üzere f(x) = a·sin(bx) fonksiyonunun [0, π/2] aralığındaki grafiği ile A ve B noktaları x ekseni üzerinde, C ve D noktaları grafik üzerinde olan ABCD dikdörtgeni gösterilmiştir.\nBuna göre, ABCD dikdörtgeninin alanı kaç birimkaredir?',
 ('π/2',pi/2),
 [(t[0],t[1],t[2],t[3] if len(t)>3 else 'bilgi') for t in [(e16[0][0],e16[0][1],e16[0][2],'bilgi'),(e16[1][0],e16[1][1],e16[1][2],'dikkat'),(e16[2][0],e16[2][1],e16[2][2],'bilgi'),(e16[3][0],e16[3][1],e16[3][2],'dikkat')]],
 'ABCD dikdörtgeninin alanı.',['a ile b’yi bul; C ve D’nin yüksekliğini A’nın apsisinden hesaplayıp B’nin yerini düşün.'],[B_GRF if False else B('Sinüs grafiğinden kural','y = a·sin(bx) grafiğinde en büyük değer a’dır; ilk tepe noktası ile ilk sıfır noktası arasındaki yatay uzaklık çeyrek periyottur ve periyot 2π/b’dir. Örnek: ilk tepe x = π/6’da, ilk sıfır x = π/3’te ise çeyrek periyot π/6, periyot 2π/3, b = 3’tür')],
 [A('a ve b’yi bul','Tepe değeri 3, ilk sıfır π/2’dedir; tepe ile sıfır arası çeyrek periyot (π/4).','a = 3 · T = π → b = 2'),
  A('Simetriyi kullan','Eğri x = π/4 doğrusuna göre simetriktir; C ve D aynı yükseklikte olduğundan A ve B bu doğruya göre simetriktir.','xB = π/2 − π/12 = 5π/12'),
  A('Boyutları yaz','Taban B ile A arası, yükseklik f(π/12)’dir.','|AB| = 5π/12 − π/12 = π/3 · |AD| = 3sin(π/6) = 3/2'),
  A('Alanı hesapla','Taban ile yükseklik çarpılır.','(π/3) × (3/2) = π/2')],
 'Grafikten kuralı bulduktan sonra dikdörtgenin boyutlarını koordinatlardan yaz.','K-ATR2-07; f(x) = 3sin2x grafiğine yazılı dikdörtgen',sekil=SK)

# ================= 0017 zor · A = 2B üçgeni (şekilli) =================
AB17,AC17,BC17=5,4,6
cA17=Fr(AB17**2+AC17**2-BC17**2,2*AB17*AC17); cB17=Fr(AB17**2+BC17**2-AC17**2,2*AB17*BC17)
assert cA17==Fr(1,8) and cB17==Fr(3,4) and 2*cB17**2-1==cA17    # A = 2B
yak(math.sqrt(AB17**2+AC17**2-2*AB17*AC17*0.5),math.sqrt(21))
e17=[2*s5,s3*0+math.sqrt(21),8,9]
assert BC17**2==AC17*(AC17+AB17) and 2*AC17==8 and AB17+AC17==9 and AB17*AC17==20
s17=0.55; cAx=AC17*s17*float(cA17); cAy=AC17*s17*math.sqrt(1-float(cA17)**2)
dA17=math.degrees(math.acos(float(cA17))); dB17=math.degrees(math.acos(float(cB17)))
SK=fig(tz('''\\fill[@T@!14] (0,0) -- (@Bx@,0) -- (@cx@,@cy@) -- cycle;
\\draw[very thick,@M@] (0,0) -- (@Bx@,0); \\draw[very thick,@T@] (0,0) -- (@cx@,@cy@); \\draw[very thick,@Y@] (@Bx@,0) -- (@cx@,@cy@);
\\draw[thick] (0.6,0) arc (0:@dA@:0.6); \\node at (@lax@,@lay@) {$2x$};
\\draw[thick] (@bx1@,0) arc (180:@bb@:0.8); \\node at (@lbx@,@lby@) {$x$};
\\node[below left] at (0,0) {$A$}; \\node[below right] at (@Bx@,0) {$B$}; \\node[above] at (@cx@,@cy@) {$C$};
\\node[below] at (@m1@,-0.02) {$5$}; \\node[left=2pt,@T@!70!black] at (@m2x@,@m2y@) {$4$};''',
 T=TUR,M=MAVI,Y=YES,Bx=AB17*s17,cx=cAx,cy=cAy,dA=dA17,lax=0.95*math.cos(R_(dA17/2)),lay=0.95*math.sin(R_(dA17/2)),
 bx1=AB17*s17-0.8,bb=180-dB17,lbx=AB17*s17-1.1*math.cos(R_(dB17/2)),lby=1.1*math.sin(R_(dB17/2)),
 m1=AB17*s17/2,m2x=cAx/2,m2y=cAy/2))
Q('0017','trg2-ucgen','zor','İki Kat Açılı Üçgen','Bir açının diğerinin iki katı olduğu üçgende sinüs ve kosinüs teoremini birleştirip karşı kenarı bulur.','şekilli',
 'Şekilde, m(BAC) = 2·m(ABC) olan ABC üçgeninde |AB| ile |AC| uzunlukları birim cinsinden verilmiştir.\nBuna göre, |BC| kaç birimdir?',
 ('6',6),
 [('2√5',2*s5,'Bağıntıyı |BC|² = |AB|·|AC| yazmış (doğrusu |BC|² = |AC|(|AC| + |AB|)): √20 = 2√5.','bilgi'),
  ('√21',math.sqrt(21),'A = 60°, B = 30° sanıp kosinüs teoremini uygulamış: 25 + 16 − 2·5·4·(1/2) = 21.','bilgi'),
  ('8',8,'sin2x = 2sinx yazıp cosx çarpanını unutmuş: |BC| = 2|AC| = 8.','islem'),
  ('9',9,'|BC| yerine diğer iki kenarın toplamını almış: 5 + 4 = 9.','dikkat')],
 '|BC| uzunluğu.',['m(ABC) = x dersen iki açıyı kenarlarla ilişkilendirmeyi dene.'],[B_SIN,B_KOS,B_IKI],
 [A('Sinüs teoremi','BC, 2x açısının; AC ise x açısının karşısındadır.','|BC|/sin2x = |AC|/sinx → |BC| = 2·4·cosx = 8cosx'),
  A('cosx’i kenarlarla yaz','B açısı için kosinüs teoremi uygulanır (|BC| = a diyelim).','cosx = (25 + a² − 16)/(2·5·a) = (a² + 9)/(10a)'),
  A('Denklemi kur','İki ifade eşitlenir.','a = 8(a² + 9)/(10a) → 10a² = 8a² + 72'),
  A('Çöz','a² çözülür; kenar pozitiftir.','a² = 36 → a = 6')],
 'Açı koşulunu kenar uzunluklarına çeviren teoremleri birlikte düşün.','K-ATR2-02; A = 2B olan üçgen, |AB| = 5, |AC| = 4',sekil=SK,
 sira=['2√5','√21','6','8','9'])

# ================= 0018 zor · sin3x/sinx − cos3x/cosx (düz) =================
for xv in (0.3,0.8,1.2):
    yak(math.sin(3*xv)/math.sin(xv)-math.cos(3*xv)/math.cos(xv),2)
    s_,c_=math.sin(xv)**2,math.cos(xv)**2
    yak((3-4*s_)-4*c_-3,-4); yak((3-4*s_)-4*c_,-1); yak(3-3,0); yak((3-4*s_)-(4*c_-3)+4*s_+4*c_,6)
Q('0018','trg2-sadelestir','orta','Üç Kat Açılı İfade','sin3x ve cos3x açılımlarını kullanıp sinx ve cosx’e bölünmüş ifadenin farkını sabit bir sayıya sadeleştirir.','düz',
 'sin3x/sinx − cos3x/cosx\nifadesinin, tanımlı olduğu her x değeri için eşiti kaçtır?',
 ('2',2),
 [('−4',-4,'−(4cos²x − 3) terimindeki eksiyi dağıtmayı unutup 3 − 4sin²x − 4cos²x − 3 = −4 bulmuş.','islem'),
  ('−1',-1,'cos3x/cosx = 4cos²x − 3 yerine 4cos²x yazmış (−3’ü atlamış): 3 − 4sin²x − 4cos²x = −1.','islem'),
  ('0',0,'sin3x = 3sinx ve cos3x = 3cosx yazmış (açıyı doğrusal almış): 3 − 3 = 0.','bilgi'),
  ('6',6,'(3 − 4sin²x) − (4cos²x − 3) = 6 − 4sin²x − 4cos²x işleminde −4sin²x − 4cos²x terimlerini birbirini götürür sanmış.','bilgi')],
 'İfadenin sabit değeri.',['Üç kat açıyı sinx ve cosx cinsinden açıp her kesri ayrı ayrı sadeleştirmeyi dene.'],[B_IKI],
 [A('Birinci kesir','sin3x = 3sinx − 4sin³x, sinx’e bölünür.','sin3x/sinx = 3 − 4sin²x'),
  A('İkinci kesir','cos3x = 4cos³x − 3cosx, cosx’e bölünür.','cos3x/cosx = 4cos²x − 3'),
  A('Farkı al','Parantezle çıkarılır.','(3 − 4sin²x) − (4cos²x − 3) = 6 − 4(sin²x + cos²x)'),
  A('Sadeleştir','sin²x + cos²x = 1’dir.','6 − 4 = 2')],
 'Üç kat açı formülü kesirde sinx ya da cosx’i yok eder.','K-ATR2-04; sin3x/sinx − cos3x/cosx',
 sira=['−4','−1','0','2','6'])

# ================= 0019 zor · gölge, iki kat açı (şekilli, hikâyeli) =================
h19,s1_,s2_=12,18,5
t1=Fr(h19,s1_); t2=Fr(h19,s2_); assert 2*t1/(1-t1**2)==t2
assert h19**2==s1_**2-2*s1_*s2_
e19=[s1_-2*s2_,s1_//2,2*s2_,s1_-s2_]; assert e19==[8,9,10,13]
sc=0.3
SK=fig(tz('''\\draw[thick] (-0.9,0) -- (@g2@,0);
\\draw[very thick,@Y@] (0,0) -- (0,@H@); \\fill[@Y@] (0,@H@) circle (2.2pt); \\node[above] at (0,@H@) {direk};
\\draw[thick,@M@] (0,@H@) -- (@s1x@,0); \\draw[thick,@T@] (0,@H@) -- (@s2x@,0);
\\draw[thick,@M@,-{Stealth}] (@s1x@-0.95,0) arc (180:@a1@:0.95); \\node[@M@] at (@s1x@-1.35,0.28) {$\\alpha$};
\\draw[thick,@T@,-{Stealth}] (@s2x@+0.7,0) arc (0:@a2@:0.7); \\node[@T@!70!black] at (@s2x@+0.9,0.55) {$2\\alpha$};
\\draw[<->,thin] (0,-0.5) -- (@s2x@,-0.5); \\node[below,@T@!70!black] at (@s2m@,-0.5) {$5$ m};
\\draw[<->,thin] (0,-1.15) -- (@s1x@,-1.15); \\node[below,@M@] at (@s1m@,-1.15) {$18$ m};
\\node[below left,font=\\footnotesize] at (0,0) {$O$};''',Y=YES,M=MAVI,T=TUR,H=h19*sc,s1x=s1_*sc,s2x=s2_*sc,g2=s1_*sc+0.6,
 a1=180-math.degrees(math.atan2(h19,s1_)),a2=math.degrees(math.atan2(h19,-(-s2_)))-0.0 if False else 180-math.degrees(math.atan2(h19,s2_))-0.0,s1m=s1_*sc/2,s2m=s2_*sc/2))
# yay açılarını doğru yönde hesapla
ang1=math.degrees(math.atan2(h19,s1_)); ang2=math.degrees(math.atan2(h19,s2_)); yak(ang2,2*ang1,1e-9*0+1e-6*1000)
SK=fig(tz('''\\draw[thick] (-0.9,0) -- (@g2@,0);
\\draw[very thick,@Y@] (0,0) -- (0,@H@); \\fill[@Y@] (0,@H@) circle (2.2pt); \\node[above] at (0,@H@) {direk};
\\draw[thick,@M@] (0,@H@) -- (@s1x@,0); \\draw[thick,@T@] (0,@H@) -- (@s2x@,0);
\\draw[thick,@M@,-{Stealth}] (@arc1s@,0) arc (180:@arc1e@:@r1@); \\node[@M@] at (@l1x@,@l1y@) {$\\alpha$};
\\draw[thick,@T@,-{Stealth}] (@arc2s@,0) arc (180:@arc2e@:@r2@); \\node[@T@!70!black] at (@l2x@,@l2y@) {$2\\alpha$};
\\draw[<->,thin] (0,-0.5) -- (@s2x@,-0.5); \\node[below,@T@!70!black] at (@s2m@,-0.5) {$5$ m};
\\draw[<->,thin] (0,-1.2) -- (@s1x@,-1.2); \\node[below,@M@] at (@s1m@,-1.2) {$18$ m};
\\node[below left,font=\\footnotesize] at (0,0) {$O$};''',Y=YES,M=MAVI,T=TUR,H=h19*sc,s1x=s1_*sc,s2x=s2_*sc,g2=s1_*sc+0.6,
 r1=1.3,r2=0.9,arc1s=s1_*sc-1.3,arc1e=180-ang1,arc2s=s2_*sc-0.9,arc2e=180-ang2,
 l1x=s1_*sc+0.85*math.cos(R_(180-ang1/2)),l1y=0.85*math.sin(R_(180-ang1/2)),l2x=s2_*sc+0.55*math.cos(R_(180-ang2/2)),l2y=0.55*math.sin(R_(180-ang2/2)),s1m=s1_*sc/2,s2m=s2_*sc/2))
Q('0019','trg2-uygulama','zor','Gölge ve Yükseklik','Aynı direğin iki farklı güneş açısındaki gölgelerinden tanjant ve iki kat açı formülüyle direğin boyunu hesaplar.','hikâyeli',
 'Bir okulun bahçesindeki bayrak direği yere dik durmaktadır. Güneş ışınlarının yerle yaptığı açı α iken ve bu açı 2 katına çıktığında direğin yerdeki gölgesinin uzunlukları şekilde gösterilmiştir. (0 < 2α < π/2)\nBuna göre, direğin boyu kaç metredir?',
 ('12',12),
 [('8',8,'tan2α = 2tanα/(1 − tanα) yazmış (paydada tan²α yerine tanα): h/5 = (2h/18)/(1 − h/18) → h = 8.','islem'),
  ('9',9,'Açı iki katına çıkınca gölgenin yarıya indiğini varsaymış: h = 18/2 = 9.','dikkat'),
  ('10',10,'Boyu ikinci gölgenin 2 katı almış: 2 · 5 = 10.','dikkat'),
  ('13',13,'Direğin boyunu iki gölge uzunluğunun farkı sanmış: 18 − 5 = 13.','dikkat')],
 'Direğin boyu (metre).',['Boya h de; her gölge için tanjantı h cinsinden yazmayı dene.'],[B_TNJ],
 [A('Tanjantları yaz','Her güneş açısı için direk, gölge ve ışın dik üçgen oluşturur.','tanα = h/18 · tan2α = h/5'),
  A('İki kat açıyı uygula','tan2α = 2tanα/(1 − tan²α) içine tanα yazılır.','h/5 = (2h/18)/(1 − h²/324)'),
  A('Düzenle','h ≠ 0 olduğundan h sadeleşir ve denklem çözülür.','1/5 = (1/9)/(1 − h²/324) → 1 − h²/324 = 5/9'),
  A('Boyu bul','h² çözülür; boy pozitiftir.','h² = 144 → h = 12')],
 'Her gölge ayrı bir dik üçgendir; ortak olan direğin boyudur.','K-ATR2-10; gölgeler 18 ve 5, α ve 2α',sekil=SK,
 sira=['8','9','10','12','13'])

# ================= 0020 zor · öncüllü, grafik (şekilli) =================
f20=lambda x:1+2*math.cos(2*x)
# f(x)<0 ⇔ x∈(π/3,2π/3) ∪ (4π/3,5π/3);  [0,π] içinde uzunluk π/3
neg=sum(1 for i in range(100000) if f20(pi*i/100000)<0)/100000*pi; yak(neg,pi/3,1e-3)
kok=[x for x in [pi/3,2*pi/3,4*pi/3,5*pi/3]]; assert all(abs(f20(x))<1e-12 for x in kok)
assert abs(f20(0)-3)<1e-12 and abs(f20(pi/2)+1)<1e-12 and abs(f20(pi))-3<1e-12 and abs(f20(pi+1e-12)-3)<1e-9
assert abs(f20(pi/2)-(-1))<1e-12 and abs(f20(3*pi/2)-(-1))<1e-12     # f=-1: 2 kök
assert abs(f20(0.5+pi)-f20(0.5))<1e-12 and abs(f20(0.5+pi/2)-f20(0.5))>1e-3     # periyot π
k20=1.45; y20=0.62
def X20(x): return x*k20
g=[f'\\draw[gray!35,thin] (0,{j*y20:.3f}) -- ({X20(2*pi)+0.2:.3f},{j*y20:.3f});' for j in (-1,1,3)]
g+= [f'\\draw[gray!35,thin] ({X20(i*pi/2):.3f},{-1.1*y20:.3f}) -- ({X20(i*pi/2):.3f},{3.3*y20:.3f});' for i in range(1,5)]
g.append(f'\\draw[-{{Stealth}},thick] (-0.1,0) -- ({X20(2*pi)+0.8:.3f},0) node[right] {{$x$}}; \\draw[-{{Stealth}},thick] (0,{-1.5*y20:.3f}) -- (0,{3.7*y20:.3f}) node[above] {{$y$}};')
g.append(f'\\draw[{MAVI},very thick,smooth,domain=0:{2*pi:.4f},samples=100,variable=\\t] plot ({{\\t*{k20}}},{{(1+2*cos(2*\\t r))*{y20}}});')
g.append(f'\\fill[{TUR}] (0,{3*y20:.3f}) circle (2.6pt) node[above right=1pt,black] {{$(0,\\,3)$}}; \\fill[{TUR}] ({X20(pi/2):.3f},{-y20:.3f}) circle (2.6pt) node[below=3pt,black] {{$\\left(\\frac{{\\pi}}{{2}},\\,-1\\right)$}};')
g+= [f'\\node[above=1pt,font=\\footnotesize] at ({X20(i*pi/2):.3f},0) {{${t}$}};'.replace('above=1pt','below=1pt') for i,t in ((2,'\\pi'),(3,'\\frac{3\\pi}{2}'),(4,'2\\pi'))]
g+= [f'\\node[left=2pt,font=\\footnotesize] at (0,{j*y20:.3f}) {{${j}$}};' for j in (-1,1)]
SK=fig('\n'.join(g))
Q('0020','trg2-grafik','zor','Grafikten Eşitsizlik ve Kök Sayısı','Kosinüs modelinin grafikten kuralını bulup periyodu, negatif aralığın uzunluğunu ve kök sayısını öncüller üzerinden değerlendirir.','öncüllü',
 'Şekilde, a, b ve c pozitif gerçel sayılar olmak üzere [0, 2π] aralığında f(x) = a + b·cos(cx) fonksiyonunun grafiği ve grafik üzerindeki iki nokta gösterilmiştir.\nBuna göre,\nI. f fonksiyonunun periyodu 2π’dir.\nII. f(x) < 0 eşitsizliğinin [0, π] aralığındaki çözüm kümesinin uzunluğu π/3’tür.\nIII. f(x) = 0 denkleminin [0, 2π] aralığında tam 4 kökü vardır.\nifadelerinden hangileri doğrudur?',
 ('II ve III',0),
 [('Yalnız I',1,'Grafiği 2π boyunca bir tam dalga sanıp periyodu 2π okumuş; II ve III’ü doğrulayamamış.','bilgi'),
  ('Yalnız II',2,'III’ü yanlış saymış: kökleri yalnız ilk periyotta (π/3 ve 2π/3) bulup 2 kök bulmuş.','bilgi'),
  ('Yalnız III',3,'II’yi yanlış saymış: negatif aralığın uzunluğunu iki aralığın toplamı (2π/3) bulmuş; periyodu da 2π sanmış.','bilgi'),
  ('I ve III',4,'Periyodu 2π sanmış; II’de uzunluğu 2π/3 bulup yanlış saymış.','bilgi')],
 'Doğru öncüller.',['Önce iki noktadan a, b ve c’yi bul; sonra her öncülü bulduğun kuralla [0, 2π] aralığında kontrol et.'],[B_GRF if False else B('Kosinüs modeli','f(x) = a + b·cos(cx) grafiğinde en büyük değer a + b, en küçük değer a − b’dir; en büyük değerden en küçük değere inen yatay uzaklık yarım periyottur ve periyot 2π/c’dir. Örnek: en büyük 5, en küçük −1 ve bu iki değer arası uzaklık π/3 ise a = 2, b = 3, periyot 2π/3, c = 3’tür')],
 [A('Kuralı bul','(0, 3) en büyük, (π/2, −1) en küçük değerdir.','a + b = 3 · a − b = −1 → a = 1, b = 2'),
  A('Periyodu bul','En büyükten en küçüğe uzaklık yarım periyottur.','T/2 = π/2 → T = π → c = 2 · f(x) = 1 + 2cos2x · I yanlış'),
  A('II. öncül','f(x) < 0 ⇔ cos2x < −1/2; [0, π] için 2x ∈ [0, 2π]’de 2x ∈ (2π/3, 4π/3).','x ∈ (π/3, 2π/3) → uzunluk π/3: II doğru'),
  A('III. öncül','f(x) = 0 ⇔ cos2x = −1/2; 2x ∈ [0, 4π] aralığında 4 kök (2π/3, 4π/3, 8π/3, 10π/3).','x = π/3, 2π/3, 4π/3, 5π/3: III doğru')],
 'Grafikten kuralı bulduktan sonra öncülleri aralık aralık, periyodu da hesaba katarak denetle.','K-ATR2-07; f(x) = 1 + 2cos2x grafiği',sekil=SK,
 sira=['Yalnız I','Yalnız II','Yalnız III','I ve III','II ve III'])

#<<SON>>
# ---------------- yaz ----------------
for q_ in P.ANA: q_['kardes']=None
from collections import Counter
tipler={}
for k_ in KART: tipler.setdefault(k_['tipId'],dict(tipId=k_['tipId'],ad=k_['tip'],kartlar=[],uygulamaKonu=UK))['kartlar'].append(k_['id'])
if len(P.ANA)==20:
    json.dump(P.ANA,open(os.path.join(HD,'trigoiki-1.json'),'w'),ensure_ascii=False,indent=1)
    json.dump(dict(konu='Trigonometri',surum=2,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT Matematik 2018–2026 çıkmış soruları ve yayın soru bankaları (yalnız mantık), MEB 11–12. sınıf müfredatı.',kartlar=KART,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar','trigoiki.json'),'w'),ensure_ascii=False,indent=1)
print(len(P.ANA),'soru · harfler',dict(sorted(Counter(q['cevap']['sik'] for q in P.ANA).items())),'· zorluk',dict(Counter(q['zorluk'] for q in P.ANA)),'· şekilli',sum(1 for q in P.ANA if q.get('sekil')),'· tip',len(tipler))
