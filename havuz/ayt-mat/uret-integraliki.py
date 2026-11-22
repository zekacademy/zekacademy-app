"""AYT Matematik · İntegral 2. dalga · 20 soruluk paket (hafif mod; kardeş yok, ipucu 1).
Tek veri kaynağı: şekil, metin ve çeldirici değerleri aynı verilerden; her cevap/çeldirici sympy/Fraction ile assert edilir."""
import sys,os,json
HD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(HD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
from ortak import *
from cizim import tikz_svg
from _hafif_mat import tablo_svg,mk
import sympy as sp
from fractions import Fraction as Fr
x,t=sp.symbols('x t')
UK='amat|İntegral'
P=Parti('integraliki','İntegral',UK,ders='AYT Matematik',idon='aytmat')
KY='ÖSYM AYT Matematik 2018–2026 (İntegral soruları; yalnız mantık) · yayın soru bankaları (yalnız mantık) · MEB 12. sınıf'
KART=[]
def kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip):
    KART.append(dict(id=id,konu='İntegral',alt=alt,fikir=fikir,tuzak=tuzak,zorluk=z,kalip=kalip,adim=adim,tipId=tipId,tip=tip,kaynak=KY))
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
def I(f,a,b): return Fr(str(sp.integrate(f,(x,a,b))))

# ---------------- bilgi kutuları (tanım ve gösterim; örnekler soruların sayılarından farklı) ----------------
B_BEL=B('Belirsiz integral','türevi f olan fonksiyonlara f’nin belirsiz integrali denir. xⁿ için ∫ xⁿ dx = xⁿ⁺¹/(n + 1) + c (n ≠ −1) ve ∫ k dx = kx + c yazılır. Örnek: ∫ (4x³ − 6x) dx = x⁴ − 3x² + c')
B_ANA=B('Belirli integral','F’nin türevi f ise ∫ₐᵇ f(x) dx = F(b) − F(a) olur. Örnek: ∫₁² 3x² dx = [x³]₁² = 8 − 1 = 7')
B_ALN=B('Eğri altında kalan alan','f, [a, b] aralığında sürekli ve f(x) ≥ 0 ise f’nin grafiği, x ekseni ile x = a ve x = b doğruları arasındaki bölgenin alanı ∫ₐᵇ f(x) dx’tir. f negatifse integral negatif çıkar; alan için işaret değişimi noktalarında aralık bölünüp mutlak değerler toplanır. Örnek: y = 2x, x ekseni ve x = 3 arasındaki alan ∫₀³ 2x dx = 9')
B_IKI=B('İki eğri arasındaki alan','[a, b] aralığında f(x) ≥ g(x) ise iki grafik arasındaki alan ∫ₐᵇ (f(x) − g(x)) dx’tir. Sınırlar, eğrilerin kesişim noktalarının apsisleridir: f(x) = g(x) denkleminin kökleri. Örnek: y = 4 ve y = x² arasında sınır noktaları x = −2 ve x = 2’dir')
B_GRF=B('Grafikten integral','bir grafiğin altında kalan alanlar geometrik şekillerle (üçgen, dikdörtgen, yamuk) bulunabilir. x ekseninin altında kalan bölgenin integrale katkısı negatiftir. Örnek: bir üçgenin tabanı 4, yüksekliği 3 ve x ekseninin altındaysa ∫ değeri −6’dır')
B_RMN=B('Alt ve üst toplam','aralık eşit parçalara bölünüp her parçada f’nin değeri bir dikdörtgenin yüksekliği alınırsa toplam alan yaklaşık bulunur. f artan ise sol uç değerleriyle bulunan toplam integralden küçük, sağ uç değerleriyle bulunan toplam integralden büyüktür. Örnek: [0, 2] aralığında iki parçada f(0) = 1, f(1) = 2, f(2) = 4 ise sol uç toplamı 1 + 2 = 3, sağ uç toplamı 2 + 4 = 6’dır')
B_DEG=B('Değişken değiştirme','u = g(x) alınırsa du = g′(x) dx olur ve belirli integralde sınırlar da u cinsinden yazılır: x = a için u = g(a), x = b için u = g(b). Örnek: ∫₀¹ 2x · (x² + 1) dx için u = x² + 1 alınırsa integral ∫₁² u du = 3/2 olur')
B_OZL=B('İntegralin özellikleri','∫ₐᵇ (f ± g) dx = ∫ₐᵇ f dx ± ∫ₐᵇ g dx; ∫ₐᵇ k·f dx = k ∫ₐᵇ f dx; ∫ₐᵇ f(mx) dx = (1/m) ∫ₘₐᵐᵇ f(u) du. Tek fonksiyonda ∫₋ₐᵃ f dx = 0, çift fonksiyonda ∫₋ₐᵃ f dx = 2 ∫₀ᵃ f dx’tir. Örnek: ∫₀³ f(x) dx = 5 ise ∫₀¹ f(3x) dx = 5/3')
B_MUT=B('Mutlak değer ve parçalı integral','|f| içeren integralde f’nin işaret değiştirdiği noktalar bulunur, her aralıkta mutlak değer işareti uygun işaretle açılır. Örnek: ∫₀³ |x − 1| dx = ∫₀¹ (1 − x) dx + ∫₁³ (x − 1) dx = 1/2 + 2 = 5/2')
B_INF=B('İntegral fonksiyonu','F(x) = ∫ₐˣ f(t) dt ise F′(x) = f(x) olur: F’nin artan ya da azalan olması f’nin işaretine bağlıdır. f, x₀’da + dan − ye geçerse F, x₀’da yerel maksimuma sahiptir. Örnek: f(x) = 2x − 6 ise F′(x) = 2x − 6 ve x = 3’te F yerel minimum alır')
B_DEN=B('Sabit içeren integral denklemi','∫ₐᵇ f(t) dt bir sayıdır; ona k denir, f’nin ifadesi k cinsinden yazılıp integral alınarak k için bir denklem kurulur. Örnek: f(x) = 2x + k ve k = ∫₀¹ f(t) dt ise k = 1 + k olur ve bu durumda böyle bir f yoktur; katsayı farklıysa k çözülür')
B_TAB=B('Türev ve integral ilişkisi','∫ₐᵇ f′(x) dx = f(b) − f(a) olur; f′(mx + n) içeren integralde u = mx + n alınır ve sonuç (1/m)·(f(mb + n) − f(ma + n))’dir. Örnek: ∫₀¹ f′(3x) dx = (f(3) − f(0))/3')
import math
B_SIM=B('Sembolik alan toplamı','grafik x eksenini kesiyorsa eksenin üstünde kalan bölgeler integrale + alanları, altında kalan bölgeler − alanları katar. Örnek: üstte 5, altta 2 birimkarelik iki komşu bölge için ∫ = 5 − 2 = 3, ∫|f| = 5 + 2 = 7 olur')
B_KOK=B('Kök fonksiyonunun integrali','√x = x^(1/2) yazılır ve kuvvet kuralı uygulanır: ∫ x^(1/2) dx = (2/3)·x^(3/2) + c. Örnek: ∫₀⁴ 6√x dx = [4x^(3/2)]₀⁴ = 32')
B_YEK=B('Bölgeyi tamamlayarak alan','eğrinin ve bir yatay doğrunun y ekseniyle sınırladığı bölge, dikdörtgenden eğrinin altında kalan alan çıkarılarak ya da x = g(y) alınarak bulunur. Örnek: y = 2x² eğrisi, y = 8 doğrusu ve y ekseni arasındaki alan 2·8 − ∫₀² 2x² dx = 16 − 16/3 olur')
B_SAR=B('Aralığı kaydırmalı koşullar','her a için ∫ₐ^(a+h) f(x) dx değeri a cinsinden verilmişse a’ya uygun değerler yazılarak komşu aralıkların integralleri bulunur ve toplanır. Örnek: ∫ₐ^(a+1) f dx = 2a ise ∫₀² f dx = 0 + 2 = 2 olur')
B_SIMN=B('Noktaya göre simetri','grafik (m, n) noktasına göre simetrikse f(m + h) + f(m − h) = 2n olur ve [m − r, m + r] aralığındaki integral 2n·r’dir. Örnek: (1, 5) noktasına göre simetrik f için ∫₀² f dx = 5 · 2 = 10')
B_ZIN=B('İç fonksiyonlu türev integrali','∫ₐᵇ f′(g(x))·g′(x) dx integralinde u = g(x) alınır ve sonuç f(g(b)) − f(g(a)) olur. Örnek: ∫₀¹ f′(h(x))·h′(x) dx = f(h(1)) − f(h(0))')
B_HIZ=B('Yol ve yer değiştirme','v(t) hız ise ∫ v dt işaretli alandır ve yer değiştirmeyi, ∫ |v| dt ise alınan toplam yolu verir. Örnek: bir cisim 3 s boyunca 2 m/s hızla ileri, sonra 1 s boyunca 2 m/s hızla geri giderse yer değiştirme 6 − 2 = 4 m, yol 6 + 2 = 8 m’dir')
B_PAR=B('Parametreli integral','integralin sonucu a cinsinden hesaplanır ve verilen değerle eşitlenerek a bulunur; a bir üs ise kuvvet kuralında a + 1’e bölünür. Örnek: ∫₀¹ (a·x + 1) dx = 3 ise a/2 + 1 = 3 ve a = 4 olur')
B_PRC=B('Parçalı fonksiyonda integral','süreklilik noktasında iki parçanın değerleri eşit olur; integral, kırılma noktasında bölünerek her parçada ayrı alınır. Örnek: f(x) = x için x ≤ 2, f(x) = 6 − x için x > 2 ise ∫₀⁴ f dx = 2 + 6 = 8')
B_ICF=B('Üst sınırı fonksiyon olan integral','F(x) = ∫ₐ^(g(x)) f(t) dt ise F′(x) = f(g(x))·g′(x) olur; F’nin artanlığı bu çarpımın işaretinden okunur. Örnek: F(x) = ∫₀^(x²) (t + 3) dt ise F′(x) = (x² + 3)·2x’tir')
B_TEG=B('Teğet ve alan','y = f(x) eğrisinin x = a noktasındaki teğeti y − f(a) = f′(a)(x − a) doğrusudur. Teğet ve eğriyle sınırlı bölgenin alanı aralığa ve eksenlere göre parçalanarak integralle hesaplanır. Örnek: y = x² eğrisinin x = 1’deki teğeti y = 2x − 1’dir')

tipkayit('int2-ozellik','Aralık ve sabit çarpan özellikleri','K-AINT2-01')
tipkayit('int2-sembolik','Alanlardan integral değeri','K-AINT2-02')
tipkayit('int2-alan','Kök, kübik ve y eksenli alanlar','K-AINT2-03')
tipkayit('int2-degisken','Değişken değiştirme (kök, iç fonksiyon, tablo)','K-AINT2-04')
tipkayit('int2-parametre','Parametreli integral ve koşullar','K-AINT2-05')
tipkayit('int2-uygulama','Yol ve yer değiştirme','K-AINT2-06')
tipkayit('int2-grafik','Grafikten integral: türev grafiği, simetri, parçalı','K-AINT2-07')
tipkayit('int2-turev-alan','Teğet ve alan','K-AINT2-08')
tipkayit('int2-integral-fonk','Üst sınırı fonksiyon olan integral','K-AINT2-09')
kart('K-AINT2-01','Aralık ve sabit çarpan özellikleri','Aralığı parçalayıp birleştirerek bilinen integrallerden istenen aralığın değeri bulunur; sabit çarpan dışarı çıkar, sabit terimin integrali uzunlukla çarpılır; her a için verilen aralık koşulunda a’ya uygun değerler yazılır.','Sabit terimin integralini yalnız sabit olarak yazmak; aralıkları çıkarmak yerine toplamak; kaydırmalı koşulda aralığı yanlış a değerine bağlamak.','kolay','düz',3,'int2-ozellik','Aralık ve sabit çarpan özellikleri')
kart('K-AINT2-02','Alanlardan integral değeri','Grafikte x eksenini kesen bir fonksiyonun bölge alanları verilmişse eksenin altındaki alanlar negatif sayılır; integral işaretli toplam, mutlak değerli integral ise alanların toplamıdır; simetri ve iki grafik arasındaki farklar da bu dille okunur.','Tüm alanları toplayıp integral sanmak; altta kalan alanı pozitif almak; iki grafik arasındaki alanda f − g ile g − f işaretini karıştırmak.','orta','öncüllü',4,'int2-sembolik','Alanlardan integral değeri')
kart('K-AINT2-03','Kök, kübik ve y eksenli alanlar','Kök fonksiyonu x^(1/2) yazılarak integrallenir; y eksenine yaslanan bölgeler dikdörtgenden eğri altı çıkarılarak bulunur; kesişimi çok olan iki eğri arasında işaret değişimi kontrol edilir.','√x için ters türevde 2/3 katsayısını unutmak; bölgenin dışını eğri altı sanmak; kesişimlerde alanları işaretli toplayıp götürmek.','orta','şekilli',4,'int2-alan','Kök, kübik ve y eksenli alanlar')
kart('K-AINT2-04','Değişken değiştirme (kök, iç fonksiyon, tablo)','İç ifade u olarak seçilir, du ile çarpan katsayı ve sınırlar dönüştürülür; f′(g(x))·g′(x) kalıbında sonuç f(g(b)) − f(g(a)) olur ve değerler tablodan okunur.','Katsayı çarpanını (1/2 ya da 2) yanlış yazmak; sınırları dönüştürmemek; tabloda g’nin değerini f’nin içine koymadan doğrudan f değerlerini çıkarmak.','orta','düz',4,'int2-degisken','Değişken değiştirme (kök, iç fonksiyon, tablo)')
kart('K-AINT2-05','Parametreli integral ve koşullar','İntegral hesaplanıp a cinsinden bir denkleme dönüştürülür; ek koşullar (alan, türev değeri, tam sayı olma) parametreleri belirler ve istenen değer hesaplanır.','Üssün integralinde a + 1’e bölmemek; koşulu yanlış noktada uygulamak; parametreyi bulunca asıl soruyu atlamak.','zor','düz',4,'int2-parametre','Parametreli integral ve koşullar')
kart('K-AINT2-06','Yol ve yer değiştirme','Hız grafiğinden elde edilen integral yer değiştirmeyi verir; hız işaret değiştirirse yer değiştirme işaretli, alınan yol mutlak değerli integralle bulunur.','Negatif alanı pozitif saymak; işaret değişimini kaçırıp tek integral almak; yolu yer değiştirme sanmak.','zor','grafik',4,'int2-uygulama','Yol ve yer değiştirme')
kart('K-AINT2-07','Grafikten integral: türev grafiği, simetri, parçalı','f′ grafiğinde alan f’nin değişimini verir; noktaya göre simetri integrali dikdörtgen alanına indirir, içteki katsayı 1/m çarpanı getirir; parçalı grafikte parçaların denklemleri noktalardan yazılıp aralık bölünerek integral alınır.','Alanı fonksiyon değeri sanmak; simetriyi yok sayıp tek parçayı hesaplamak; 1/m çarpanını unutmak; parçalı grafiği tek doğru sanmak.','zor','grafik',4,'int2-grafik','Grafikten integral: türev grafiği, simetri, parçalı')
kart('K-AINT2-08','Teğet ve alan','Türevle teğet denklemi yazılır, eğri ve teğetin konumuna göre aralık bölünür ve integral alınır.','Eğimi yanlış türevden bulmak; bölgenin eksenle sınırını yok saymak; tek integralle tüm bölgeyi almaya çalışmak.','zor','şekilli',5,'int2-turev-alan','Teğet ve alan')
kart('K-AINT2-09','Üst sınırı fonksiyon olan integral','F′(x) = f(g(x))·g′(x) olduğundan F’nin kritik noktaları ve artanlığı bu çarpımın işaretinden bulunur; değerler için sınırlara dönülür.','İç fonksiyonun türevi olan çarpanı unutmak; işaret tablosunu yanlış kurmak; F(x) değerini F′ ile karıştırmak.','zor','öncüllü',5,'int2-integral-fonk','Üst sınırı fonksiyon olan integral')
# ================= şekil yardımcıları =================
def fig(body,font='\\small'):
    return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font='+font+']\n'+body+'\n\\end{tikzpicture}')
def eks(x0,x1,y0,y1,sx,sy,xt=None,yt=None,xl='$x$',yl='$y$',gx=1,gy=1,fs_='\\footnotesize',yekseni=True):
    """Izgara + eksenler. x0..x1, y0..y1 ızgara aralığı; xt/yt: etiketlenecek değerler."""
    o=[]
    xt=[i for i in range(x0,x1+1)] if xt is None else xt; yt=[j for j in range(y0,y1+1)] if yt is None else yt
    for i in range(x0,x1+1,gx): o.append(f'\\draw[gray!30,thin] ({i*sx:.3f},{y0*sy:.3f}) -- ({i*sx:.3f},{y1*sy:.3f});')
    for j in range(y0,y1+1,gy): o.append(f'\\draw[gray!30,thin] ({x0*sx:.3f},{j*sy:.3f}) -- ({x1*sx:.3f},{j*sy:.3f});')
    o.append(f'\\draw[-{{Stealth}},thick] ({(x0-0.3)*sx:.3f},0) -- ({(x1+0.6)*sx:.3f},0) node[right] {{{xl}}};')
    o.append(f'\\draw[-{{Stealth}},thick] (0,{(y0-0.3)*sy:.3f}) -- (0,{(y1+0.6)*sy:.3f}) node[above] {{{yl}}};')
    for i in xt:
        if i!=0: o.append(f'\\node[below=2pt,font={fs_}] at ({i*sx:.3f},0) {{${i}$}};')
    for j in yt:
        if j!=0: o.append(f'\\node[left=2pt,font={fs_},fill=white,fill opacity=0.0,text opacity=1,inner sep=0.6pt] at (0,{j*sy:.3f}) {{${j}$}};')
    o.append(f'\\node[below left,font={fs_}] at (0,0) {{$O$}};')
    return '\n'.join(o)
def pl(expr,a,b,sx,sy,ns=60):
    """pgf bölgesi: expr x'in TeX ifadesi (\\x kullanır)."""
    return f'plot[domain={a}:{b},samples={ns}] ({{\\x*{sx}}},{{({expr})*{sy}}})'
def altgol(expr,a,b,sx,sy,renk,op=0.28):
    return f'\\fill[{renk},fill opacity={op}] ({a*sx:.3f},0) -- {pl(expr,a,b,sx,sy)} -- ({b*sx:.3f},0) -- cycle;'
def arag(ust,alt,a,b,sx,sy,renk,op=0.3):
    return f'\\fill[{renk},fill opacity={op}] {pl(ust,a,b,sx,sy)} -- {pl(alt,b,a,sx,sy)} -- cycle;'
def egri(expr,a,b,sx,sy,renk,w='1.8pt'):
    return f'\\draw[{renk},line width={w}] {pl(expr,a,b,sx,sy,80)};'
def kes(xv,y0,y1,sx,sy,renk='black!60',st='dashed'):
    return f'\\draw[{renk},{st}] ({xv*sx:.3f},{y0*sy:.3f}) -- ({xv*sx:.3f},{y1*sy:.3f});'
def nok(xv,yv,sx,sy,r=0.065,renk='black'):
    return f'\\fill[{renk}] ({xv*sx:.3f},{yv*sy:.3f}) circle ({r});'
def poly(pts,sx,sy,renk,w='1.9pt'):
    return f'\\draw[{renk},line width={w}] '+' -- '.join(f'({a*sx:.3f},{b*sy:.3f})' for a,b in pts)+';'
def pgol(pts,sx,sy,renk,op=0.28):
    return f'\\fill[{renk},fill opacity={op}] '+' -- '.join(f'({a*sx:.3f},{b*sy:.3f})' for a,b in pts)+' -- cycle;'
MAVI='blue!75!black'; TUR='orange!90!black'; YES='green!55!black'; MOR='violet!80!black'
def poly_alan(pts):
    """Parçalı doğrusal fonksiyonun [x0,xn] işaretli integrali (köşeler arasında doğrusal)."""
    s=Fr(0)
    for (a,b),(c,d) in zip(pts,pts[1:]):
        s+=Fr(c-a)*Fr(b+d,2)
    return s
def poly_deger(pts,xv):
    for (a,b),(c,d) in zip(pts,pts[1:]):
        if a<=xv<=c: return Fr(b)+Fr(d-b,c-a)*(xv-a)
def poly_integral(pts,u,v):
    """∫_u^v (u,v köşelerde)"""
    xs=[p[0] for p in pts]; s=Fr(0)
    for (a,b),(c,d) in zip(pts,pts[1:]):
        lo,hi=max(a,u),min(c,v)
        if lo<hi: s+=(hi-lo)*(poly_deger(pts,lo)+poly_deger(pts,hi))/2
    return s
def poly_mutlak(pts,u,v):
    """∫|f| köşeler arasında doğrusal"""
    s=Fr(0)
    for (a,b),(c,d) in zip(pts,pts[1:]):
        lo,hi=max(a,u),min(c,v)
        if lo>=hi: continue
        y1,y2=poly_deger(pts,lo),poly_deger(pts,hi)
        if y1*y2>=0: s+=(hi-lo)*(abs(y1)+abs(y2))/2
        else:
            z=lo+(hi-lo)*abs(y1)/(abs(y1)+abs(y2)); s+=(z-lo)*abs(y1)/2+(hi-z)*abs(y2)/2
    return s


# ================= 01 kolay · aralık özellikleri =================
i02=Fr(14)-Fr(9); assert i02==5
v1=2*i02+2*1; assert v1==12
e1=[2*i02+1,2*i02,2*(14+9)+2,2*(9-14)+2]; assert e1==[11,10,48,-8]
Q('0001','int2-ozellik','kolay','Aralık Özellikleri','Belirli integralin aralık toplamı ve sabit çarpan özelliklerini kullanarak parçalanmış aralıkta değer hesaplar.','düz',
 'Gerçel sayılar kümesi üzerinde sürekli bir f fonksiyonu için\n∫₀⁶ f(x) dx = 14\n∫₂⁶ f(x) dx = 9\neşitlikleri veriliyor.\nBuna göre ∫₀² (2f(x) + 1) dx integralinin değeri kaçtır?',
 v1,[(e1[0],'Sabit terim 1’in integralini 1 olarak yazıp aralık uzunluğu 2 ile çarpmamış: 2·5 + 1.','islem'),(e1[1],'Sabit terimi tamamen atlayıp yalnız 2·∫₀² f(x) dx = 10 değerini yazmış.','dikkat'),(e1[2],'∫₀² f(x) dx = 14 − 9 yerine 14 + 9 = 23 almış: 2·23 + 2.','bilgi'),(e1[3],'∫₀² f(x) dx = 9 − 14 = −5 almış (çıkarmayı ters yapmış): 2·(−5) + 2.','bilgi')],
 '∫₀² (2f(x) + 1) dx değeri.',['∫₀² f(x) dx değerini verilen iki integralden nasıl elde edersin? Sabit terimin integrali hangi aralık uzunluğuna bağlıdır?'],[B_OZL,B_ANA],
 [A('Aralığı parçala','[0, 6] aralığı [0, 2] ve [2, 6] olarak ikiye ayrılır.','∫₀² f dx = ∫₀⁶ f dx − ∫₂⁶ f dx = 14 − 9 = 5'),A('Toplamı böl','Toplamın integrali integrallerin toplamıdır, sabit çarpan dışarı çıkar.','∫₀² (2f + 1) dx = 2∫₀² f dx + ∫₀² 1 dx'),A('Sabit terimi hesapla','1’in integrali aralık uzunluğudur.','∫₀² 1 dx = 2'),A('Topla','İki değer toplanır.','2·5 + 2 = 12')],
 'Önce istenen aralığı verilen aralıkların farkı olarak yaz; sabit terimin integralini uzunlukla çarp.','K-AINT2-01; f için iki aralık verili, sabit terimli integral')

# ================= 02 kolay · alanlardan integral (şekilli) =================
A1v,A2v,A3v=6,9,7; v2=A1v-A2v+A3v; assert v2==4
e2=[A1v+A2v+A3v,A1v-A2v-A3v,A1v+A2v-A3v,-A1v+A2v+A3v]; assert e2==[22,-10,8,10] and len({v2,*e2})==5
FS='1.3*sin(60*(\\x-1))'
b=['\\draw[-{Stealth},thick] (0,0) -- (7.7,0) node[right] {$x$};','\\draw[-{Stealth},thick] (0,-1.7) -- (0,1.9) node[above] {$y$};',
   altgol(FS,1,4,0.75,0.9,MAVI,0.3),altgol(FS,4,7,0.75,0.9,TUR,0.3),altgol(FS,7,9,0.75,0.9,YES,0.3),
   egri(FS,0.4,9.6,0.75,0.9,'black!75','1.8pt'),kes(9,0,1.3*math.sin(math.radians(480)),0.75,0.9,'black!60','dashed'),
   f'\\node[font=\\small] at ({2.5*.75:.3f},{0.5*.9:.3f}) {{$A_1=6$}};',f'\\node[font=\\small] at ({5.5*.75:.3f},{-0.55*.9:.3f}) {{$A_2=9$}};',f'\\node[font=\\scriptsize] at ({8.0*.75:.3f},{0.45*.9:.3f}) {{$A_3=7$}};',
   f'\\node[above right,font=\\small] at ({9.5*.75:.3f},{1.0*.9:.3f}) {{$y=f(x)$}};']
for v_,nm in ((1,'a'),(4,'b'),(7,'c'),(9,'d')): b.append(f'\\node[below=2pt,font=\\small] at ({v_*.75:.3f},0) {{${nm}$}};')
b+= [f'\\fill ({v_*.75:.3f},0) circle (0.05);' for v_ in (1,4,7,9)]
SK2=fig('\n'.join(b))
Q('0002','int2-sembolik','kolay','Boyalı Bölgelerden İntegral','Eksenin altında ve üstünde kalan bölgelerin alanlarından belirli integralin işaretli değerini bulur.','şekilli',
 'Dik koordinat düzleminde bir f fonksiyonunun grafiği verilmiştir. Grafik ile x ekseni arasında kalan, A₁, A₂ ve A₃ ile gösterilen boyalı bölgelerin alanları şekilde yazılıdır (birimkare).\nBuna göre ∫ₐᵈ f(x) dx integralinin değeri kaçtır?',
 v2,[(e2[0],'Bütün alanları toplamış; eksenin altındaki bölgenin integrale negatif katkı yaptığını unutmuş.','bilgi'),(e2[1],'İlk alanı pozitif, diğer ikisini negatif almış: 6 − 9 − 7.','dikkat'),(e2[2],'Üçüncü bölgeyi eksenin üstünde olduğu hâlde negatif almış: 6 + 9 − 7.','dikkat'),(e2[3],'Eksenin altındaki bölge yerine ilk bölgeyi negatif almış: −6 + 9 + 7.','dikkat')],
 'İntegralin işaretli değeri.',['Hangi bölgeler x ekseninin üstünde, hangisi altında? Altta kalan bölge integrale nasıl katılır?'],[B_SIM,B_GRF],
 [A('İşaretleri belirle','x ekseninin üstündeki bölgeler pozitif, altındaki bölge negatif katkı yapar.','A₁ ve A₃ pozitif · A₂ negatif'),A('İntegralin yapısı','a’dan d’ye integral üç aralığın toplamıdır.','∫ₐᵈ f dx = ∫ₐᵇ f + ∫ᵇᶜ f + ∫ᶜᵈ f'),A('Değerleri yaz','Her aralıktaki integral, işaretli alandır.','6 + (−9) + 7'),A('Topla','İşaretli alanlar toplanır.','6 − 9 + 7 = 4')],
 'Eksenin üstündeki alan +, altındaki alan − olarak yazılıp toplanır.','K-AINT2-02; üç bölgeli grafik, alanlar şekilde',sekil=SK2)

# ================= 03 kolay · √x altında alan =================
v3=I(sp.sqrt(x),0,9); assert v3==18
e3=[Fr(27),Fr(6),Fr(27,2),Fr(3)]
assert e3[0]==Fr(9)*3 and e3[1]==Fr(str(2*sp.sqrt(9)-0)) and e3[2]==Fr(27,2)/1 and len({v3,*e3})==5
sx,sy=0.72,0.85
b=[eks(0,10,0,4,sx,sy,xt=[1,2,3,4,5,6,7,8,9],yt=[1,2,3],xl='$x$',yl='$y$',fs_='\\scriptsize'),
   altgol('sqrt(\\x)',0,9,sx,sy,MAVI,0.3),egri('sqrt(\\x)',0,9.8,sx,sy,MAVI),kes(9,0,3,sx,sy,MAVI,'thick'),nok(9,3,sx,sy,0.07),
   f'\\node[right,font=\\small,{MAVI}] at ({9.8*sx:.3f},{3.1*sy:.3f}) {{$f$}};']
SK3=fig('\n'.join(b))
Q('0003','int2-alan','kolay','Kök Fonksiyonu Altında Alan','Kök fonksiyonunu kuvvet biçiminde yazıp x ekseni ve dikey doğru arasında kalan alanı belirli integralle bulur.','şekilli',
 'Şekilde, f(x) = √x fonksiyonunun grafiği, x ekseni ve x = 9 doğrusu arasında kalan bölge boyanmıştır.\nBuna göre boyalı bölgenin alanı kaç birimkaredir?',
 v3,[(e3[0],'√x’in ters türevini x^(3/2) yazıp 2/3 katsayısını unutmuş: 9^(3/2).','islem'),(e3[1],'Ters türev olarak 2√x almış (türev almaya benzer bir işlem yapmış): 2√9.','islem'),(e3[2],'x^(3/2) ifadesini 3/2 yerine 2’ye bölmüş: 27/2.','islem'),(e3[3],'Alan yerine eğrinin x = 9’daki yüksekliğini yazmış: f(9).','bilgi')],
 'Boyalı bölgenin alanı (birimkare).',['√x ifadesini bir kuvvet olarak yazıp ters türevi al.'],[B_KOK,B_ALN],
 [A('Kuvvet biçimi','Kök, 1/2 kuvveti olarak yazılır.','f(x) = x^(1/2)'),A('İntegrali kur','Alan, x = 0’dan x = 9’a belirli integraldir.','A = ∫₀⁹ x^(1/2) dx'),A('Ters türev','Kuvvet bir artırılır ve yeni kuvvete bölünür.','(2/3)·x^(3/2)'),A('Sınırları yaz','Üst sınır değerinden alt sınır değeri çıkarılır.','(2/3)·27 − 0 = 18')],
 'Köklü ifadeyi önce üslü yaz, sonra kuvvet kuralını uygula.','K-AINT2-03; f(x) = √x, x = 9',sekil=SK3)

# ================= 04 orta · kaydırmalı aralık koşulu =================
fa=x**2/2+x-sp.Rational(5,3)
for a_ in (-2,0,1,3): assert sp.simplify(sp.integrate(fa,(x,a_,a_+2))-(a_**2+4*a_))==0
G=lambda a_:a_**2+4*a_
v4=G(1)+G(3); assert v4==26 and I(fa,1,5)==26
e4=[Fr(G(1)),Fr(G(3)),Fr(G(1)+G(5)),Fr(2*G(2))]; assert e4==[5,21,50,24] and len({v4,*e4})==5
Q('0004','int2-ozellik','orta','Kaydırmalı Aralık Koşulu','Her a için verilen aralık koşulunu uygun a değerleriyle yazıp komşu aralıkların integrallerini toplar.','düz',
 'Gerçel sayılar kümesi üzerinde sürekli bir f fonksiyonu, her a gerçel sayısı için\n∫ₐ^(a+2) f(x) dx = a² + 4a\neşitliğini sağlıyor.\nBuna göre ∫₁⁵ f(x) dx integralinin değeri kaçtır?',
 v4,[(e4[0],'Yalnız a = 1 için koşulu yazıp [1, 3] aralığının değerini bulmuş; [3, 5] aralığını hesaba katmamış.','dikkat'),(e4[1],'Yalnız a = 3 için koşulu yazıp [3, 5] aralığını bulmuş; [1, 3] aralığını atlamış.','dikkat'),(e4[2],'İkinci aralık için a = 3 yerine a = 5 yazmış: (1 + 4) + (25 + 20).','islem'),(e4[3],'[1, 5] aralığını ortadaki a = 2 değeriyle iki eşit parça sanıp 2·(4 + 8) yazmış.','bilgi')],
 '∫₁⁵ f(x) dx değeri.',['[1, 5] aralığını uzunluğu 2 olan parçalara ayırdığında her parçanın başlangıç noktası ne olur?'],[B_SAR,B_OZL],
 [A('Aralığı parçala','Koşuldaki aralık uzunluğu 2 olduğundan [1, 5] iki parçaya ayrılır.','∫₁⁵ f dx = ∫₁³ f dx + ∫₃⁵ f dx'),A('Birinci parça','Başlangıç a = 1 olur.','1² + 4·1 = 5'),A('İkinci parça','Başlangıç a = 3 olur.','3² + 4·3 = 21'),A('Topla','İki parçanın değeri toplanır.','5 + 21 = 26')],
 'Aralığı koşuldaki uzunluğa böl ve her parçanın başlangıç noktasını a yerine yaz.','K-AINT2-01; ∫ₐ^(a+2) f = a² + 4a koşulu')

# ================= 05 orta · öncüllü, tek fonksiyon grafiği =================
sx,sy=1.15,0.42
F5='\\x*\\x*\\x-4*\\x'
b=[eks(-3,3,-4,4,sx,sy,xt=[-2,-1,1,2],yt=[],gy=1),altgol(F5,-2,0,sx,sy,MAVI,0.3),altgol(F5,0,2,sx,sy,TUR,0.3),egri(F5,-2.25,2.25,sx,sy,'black!75','1.9pt'),
   f'\\node[font=\\small] at ({1.0*sx:.3f},{-1.9*sy:.3f}) {{$A=4$}};',f'\\node[above right,font=\\small] at ({2.2*sx:.3f},{2.3*sy:.3f}) {{$y=f(x)$}};']
b+= [nok(0,0,sx,sy,0.06)]
SK5=fig('\n'.join(b))
assert I(x**3-4*x,0,2)==-4 and I(x**3-4*x,-2,2)==0 and I(x**3-4*x,-2,0)==4
sira5=['Yalnız I','Yalnız II','I ve II','I ve III','II ve III']
Q('0005','int2-sembolik','orta','Tek Fonksiyon ve Boyalı Bölgeler','Orijine göre simetrik grafikte bölge alanlarından işaretli ve mutlak değerli integralleri değerlendirir.','öncüllü',
 'Dik koordinat düzleminde grafiği orijine göre simetrik olan bir f fonksiyonu x eksenini yalnız −2, 0 ve 2 noktalarında kesmektedir. Grafik ile x ekseni arasında kalan boyalı bölgelerden x ekseninin altında kalanın alanı şekilde verilmiştir (birimkare).\nI. ∫₀² f(x) dx = 4\nII. ∫₋₂² f(x) dx = 0\nIII. ∫₋₂² |f(x)| dx = 8\nifadelerinden hangileri doğrudur?',
 'II ve III',[('Yalnız I','I’de eksenin altındaki alanın değerini pozitif yazmış; II ve III’ü simetriyi kullanmadan yanlış saymış.','bilgi'),('Yalnız II','III’te mutlak değeri alan yerine integralin kendisi (0) sanıp yanlış bulmuş.','dikkat'),('I ve II','I’de işareti dikkate almamış; III’te iki bölgenin alanını toplamayı akıl edememiş.','bilgi'),('I ve III','I’i doğru kabul etmiş; II’de tek fonksiyonun simetrik aralıktaki integralinin 0 olduğunu bilmeden yanlış saymış.','bilgi')],
 'Doğru olan ifadeler.',['Orijine göre simetrik grafikte x ekseninin üstündeki bölgenin alanı hakkında ne söyleyebilirsin? Eksenin altındaki alan integrale hangi işaretle katılır?'],[B_SIM,B_OZL],
 [A('Bölgeleri tanı','Simetri nedeniyle [−2, 0] aralığındaki bölge de 4 birimkaredir ve eksenin üstündedir.','üst bölge 4 · alt bölge 4'),A('I’i incele','[0, 2] aralığında grafik eksenin altındadır.','∫₀² f dx = −4 ≠ 4'),A('II’yi incele','Üst bölge + ve alt bölge − olarak toplanır.','∫₋₂² f dx = 4 − 4 = 0'),A('III’ü incele','Mutlak değerde iki alan da pozitif sayılır.','∫₋₂² |f| dx = 4 + 4 = 8 · doğru olanlar II ve III')],
 'Alt bölge − , üst bölge + ile toplanır; mutlak değerde ikisi de +’dır.','K-AINT2-02; orijine göre simetrik grafik, tek alan verili',sekil=SK5,sira=sira5)

# ================= 06 orta · x·f(x²+1) =================
S6=Fr(12); assert 6*2==12
v6=S6+2*4; assert v6==20
e6=[S6,Fr(6)+8,Fr(3)+8,S6+2*2]; assert e6==[12,14,11,16] and len({v6,*e6})==5
Q('0006','int2-degisken','orta','İç İfade ile Değişken Değiştirme','x·f(x² + 1) biçiminde bir integralden f’nin başka aralıktaki integralini bulup toplam integrale uygular.','düz',
 'Gerçel sayılar kümesi üzerinde sürekli bir f fonksiyonu için\n∫₀² x · f(x² + 1) dx = 6\neşitliği veriliyor.\nBuna göre ∫₁⁵ (f(x) + 2) dx integralinin değeri kaçtır?',
 v6,[(e6[0],'Yalnız ∫₁⁵ f(x) dx = 12 değerini yazıp +2 terimini hesaba katmamış.','dikkat'),(e6[1],'u = x² + 1 için du = 2x dx olduğunu unutup 1/2 çarpanını yazmamış: ∫₁⁵ f = 6.','islem'),(e6[2],'x dx = 2 du alıp ∫₁⁵ f(x) dx = 3 bulmuş.','islem'),(e6[3],'Sabit terimin integralini [1, 5] yerine [0, 2] uzunluğuyla hesaplamış: 12 + 4.','dikkat')],
 '∫₁⁵ (f(x) + 2) dx değeri.',['u = x² + 1 alırsan sınırlar ve x dx ifadesi nasıl değişir?'],[B_DEG,B_OZL],
 [A('Değişken değiştir','u = x² + 1 için du = 2x dx; x = 0’da u = 1, x = 2’de u = 5.','∫₀² x·f(x² + 1) dx = (1/2)·∫₁⁵ f(u) du'),A('Değeri bul','Verilen değerle eşitlenir.','(1/2)·∫₁⁵ f(u) du = 6 → ∫₁⁵ f(x) dx = 12'),A('Sabit terimi ekle','2’nin integrali aralık uzunluğu 4 ile çarpılır.','∫₁⁵ 2 dx = 8'),A('Topla','İki değer toplanır.','12 + 8 = 20')],
 'du = 2x dx ise x dx = du/2; sınırları da u cinsinden yaz.','K-AINT2-04; ∫₀² x f(x² + 1) dx = 6')

# ================= 07 orta · y eksenli bölge (kübik) =================
v7=I(8-x**3,0,2); assert v7==12
e7=[I(x**3,0,2),Fr(1,2)*2*8,Fr(2*8),Fr(2*8)+I(x**3,0,2)]; assert e7==[4,8,16,20] and len({v7,*e7})==5
sx,sy=1.5,0.4
b=[eks(0,3,0,9,sx,sy,xt=[1,2],yt=[2,4,6,8],gy=1,fs_='\\scriptsize'),arag('8','\\x*\\x*\\x',0,2,sx,sy,TUR,0.32),egri('\\x*\\x*\\x',0,2.05,sx,sy,MAVI,'2pt'),
   f'\\draw[{TUR},line width=1.8pt] (0,{8*sy:.3f}) -- ({2.8*sx:.3f},{8*sy:.3f});',nok(2,8,sx,sy,0.07),kes(2,0,8,sx,sy,'black!50','dashed'),
   f'\\node[right,font=\\small,{MAVI}] at ({2.1*sx:.3f},{7.3*sy:.3f}) {{$y=x^3$}};',f'\\node[above,font=\\small,{TUR}] at ({2.4*sx:.3f},{8*sy:.3f}) {{$y=8$}};']
SK7=fig('\n'.join(b))
Q('0007','int2-alan','orta','Eğri, Yatay Doğru ve y Ekseni','Eğri ile yatay doğrunun y ekseniyle sınırladığı bölgenin alanını dikdörtgenden eğri altı alanı çıkararak bulur.','şekilli',
 'Şekilde, y = x³ eğrisi, y = 8 doğrusu ve y ekseni ile sınırlı bölge boyanmıştır.\nBuna göre boyalı bölgenin alanı kaç birimkaredir?',
 v7,[(e7[0],'Yalnız eğrinin altında kalan alanı hesaplamış: ∫₀² x³ dx.','dikkat'),(e7[1],'Bölgeyi köşeleri (0, 0), (2, 8) ve (0, 8) olan üçgen sanmış: ½·2·8.','bilgi'),(e7[2],'Dikdörtgenin alanını (2·8) bölge alanı sanmış.','dikkat'),(e7[3],'Dikdörtgene eğri altı alanı eklemiş: 16 + 4.','islem')],
 'Boyalı bölgenin alanı (birimkare).',['Eğrinin ve y = 8 doğrusunun kesiştiği noktanın apsisi nedir? Bölge hangi iki fonksiyon arasında kalır?'],[B_YEK,B_IKI],
 [A('Kesişimi bul','x³ = 8 denkleminden sağ sınır bulunur.','x = 2'),A('Üst ve alt fonksiyonu seç','Aralıkta doğru üstte, eğri altta kalır.','üst: 8 · alt: x³'),A('İntegrali kur','Alan, üst eksi alt integralidir.','A = ∫₀² (8 − x³) dx'),A('Hesapla','Ters türev alınıp sınırlar yazılır.','[8x − x⁴/4]₀² = 16 − 4 = 12')],
 'Bölge yatay doğru ile eğri arasındaysa üst fonksiyondan alt fonksiyonu çıkar.','K-AINT2-03; y = x³, y = 8 ve y ekseni',sekil=SK7)

# ================= 08 orta · f′ grafiği ve f(10) =================
inc=I(x/2+2,4,10); assert inc==33; v8=30+inc; assert v8==63
e8=[inc,30+Fr(4)*6,Fr(7)*10,30+Fr(7)*6]; assert e8==[33,54,70,72] and len({v8,*e8})==5
sx,sy=0.55,0.55
b=[eks(0,12,0,8,sx,sy,xt=[2,4,6,8,10,12],yt=[1,2,3,4,5,6,7,8],xl='$x$',yl="$y=f'(x)$",fs_='\\scriptsize'),
   pgol([(4,0),(4,4),(10,7),(10,0)],sx,sy,YES,0.3),f'\\draw[{YES},line width=1.9pt] ({0:.3f},{2*sy:.3f}) -- ({12*sx:.3f},{8*sy:.3f});',
   nok(4,4,sx,sy,0.06),nok(10,7,sx,sy,0.06),kes(4,0,4,sx,sy,'black!60','dashed'),kes(10,0,7,sx,sy,'black!60','dashed')]
SK8=fig('\n'.join(b))
Q('0008','int2-grafik','orta','f′ Grafiğinden Fonksiyon Değeri','Türev grafiği ile x ekseni arasındaki alanı fonksiyonun değişimi olarak yorumlayıp verilen bir değere ekleyerek başka bir noktadaki değeri bulur.','grafik',
 'Şekilde, [0, 12] aralığında sürekli ve türevlenebilir bir f fonksiyonunun türevi olan f′ fonksiyonunun grafiği verilmiştir; grafik bir doğrudur ve işaretli noktalar kılavuz çizgilerinin kesiştiği noktalardır. f(4) = 30 olarak veriliyor.\nBuna göre f(10) değeri kaçtır?',
 v8,[(e8[0],'f(10) yerine yalnız f(10) − f(4) farkını (boyalı alan) yazmış.','dikkat'),(e8[1],'Boyalı bölgeyi dikdörtgen sanıp yüksekliği olarak f′(4) = 4 almış: 30 + 4·6.','bilgi'),(e8[2],'f′(10) değerini ve 10’u çarpıp f(10) sanmış: 7·10.','bilgi'),(e8[3],'Boyalı bölgeyi dikdörtgen sanıp yüksekliği olarak f′(10) = 7 almış: 30 + 7·6.','bilgi')],
 'f(10) değeri.',['Grafikten hangi büyüklüğü hesaplayabilirsin ve bu büyüklük f(10) ile f(4) arasında nasıl bir ilişki kurar?'],[B_TAB,B_GRF],
 [A('Farkı yorumla','f′’nin 4 ile 10 arasındaki integrali f’nin değişimidir; bu değer boyalı alandır.','f(10) − f(4) = ∫₄¹⁰ f′(x) dx'),A('Şekli tanı','Boyalı bölge yamuktur; paralel kenarları 4 ve 7, yüksekliği 6’dır.','alan = (4 + 7)·6/2 = 33'),A('Farkı yaz','Alan değişime eşittir.','f(10) − 30 = 33'),A('f(10)’u bul','Verilen değere eklenir.','f(10) = 30 + 33 = 63')],
 'f′ grafiği ile eksen arasındaki işaretli alan f’deki değişimdir.','K-AINT2-07; doğrusal f′ grafiği ve f(4) değeri',sekil=SK8)

# ================= 09 orta · üssü parametre =================
sol=[a_ for a_ in range(1,30) if Fr(2**(a_+1),a_+1)+6==10]; assert sol==[3]
v9=Fr(2**4-1,4); assert v9==Fr(15,4)
e9=[Fr(4),Fr(2**5-1,5),Fr(15),Fr(7)]; assert e9[0]==Fr(2**4,4) and len({v9,*e9})==5
Q('0009','int2-parametre','orta','Üssü Bilinmeyen İntegral','İntegral sonucunu üs parametresi cinsinden yazıp tam sayı koşuluyla parametreyi bulur ve başka bir aralıkta hesaplar.','düz',
 'Üssü a pozitif tam sayısı olan bir xᵃ terimi için ∫₀² (3x + xᵃ) dx integralinin değeri 10’dur.\nBuna göre xᵃ teriminin [1, 2] aralığındaki belirli integrali kaçtır?',
 v9,[(e9[0],'a = 3’ü bulduktan sonra istenen aralık yerine ∫₀² x³ dx = 4 değerini yazmış.','dikkat'),(e9[1],'2ᵃ⁺¹/(a + 1) = 4 denklemi yerine 2ᵃ/a = 4 çözüp a = 4 bulmuş: ∫₁² x⁴ dx.','islem'),(e9[2],'xᵃ⁺¹/(a + 1) yerine paydayı yazmayı unutmuş: 2⁴ − 1.','islem'),(e9[3],'Ters türev yerine fonksiyon değerlerinin farkını almış: 2³ − 1.','bilgi')],
 '∫₁² xᵃ dx değeri.',['İntegrali a cinsinden hesapla; hangi pozitif tam sayı değeri denklemi sağlar?'],[B_PAR,B_ANA],
 [A('Denklemi kur','∫₀² 3x dx = 6 olduğundan xᵃ’nın integrali 4 olmalıdır.','2ᵃ⁺¹/(a + 1) + 6 = 10 → 2ᵃ⁺¹/(a + 1) = 4'),A('a’yı bul','Pozitif tam sayılar denenir: a = 1 için 2, a = 2 için 8/3, a = 3 için 4.','a = 3'),A('İntegrali kur','İstenen integral x³’ün [1, 2] aralığındaki integralidir.','∫₁² x³ dx = [x⁴/4]₁²'),A('Hesapla','Sınır değerleri yazılır.','16/4 − 1/4 = 15/4')],
 'Üslü terimin integralini a + 1’e bölerek yaz; tam sayı koşuluyla a’yı dene.','K-AINT2-05; ∫₀² (xᵃ + 3x) dx = 10')

# ================= 10 orta · x³ ve x arasında alan =================
v10=I(x-x**3,0,1)*2; assert v10==Fr(1,2)
e10=[I(x-x**3,-1,1),I(x-x**3,0,1),I(sp.Abs(x),-1,1) if False else Fr(1),Fr(3,2)]; assert e10==[0,Fr(1,4),1,Fr(3,2)] and len({v10,*e10})==5
sx,sy=1.9,0.95
b=[eks(-2,2,-2,2,sx,sy,xt=[-1,1],yt=[-1,1],fs_='\\scriptsize'),arag('\\x*\\x*\\x','\\x',-1,0,sx,sy,TUR,0.35),arag('\\x','\\x*\\x*\\x',0,1,sx,sy,MAVI,0.3),
   egri('\\x*\\x*\\x',-1.27,1.27,sx,sy,MAVI,'2pt'),egri('\\x',-1.6,1.6,sx,sy,TUR,'2pt'),nok(-1,-1,sx,sy,0.06),nok(1,1,sx,sy,0.06),nok(0,0,sx,sy,0.06),
   f'\\node[right,font=\\small,{MAVI}] at ({1.27*sx:.3f},{1.9*sy:.3f}) {{$y=x^3$}};',f'\\node[right,font=\\small,{TUR}] at ({1.6*sx:.3f},{1.6*sy:.3f}) {{$y=x$}};']
SK10=fig('\n'.join(b))
Q('0010','int2-alan','orta','İki Eğri Arasındaki İki Bölge','Kesişim noktalarının üç olduğu iki eğri arasındaki bölgelerin alanları toplamını, işaret değişimini gözeterek hesaplar.','şekilli',
 'Şekilde, y = x³ ve y = x grafikleri ile bu grafikler arasında kalan iki bölge boyanmıştır.\nBuna göre boyalı bölgelerin alanları toplamı kaç birimkaredir?',
 v10,[(e10[0],'∫₋₁¹ (x − x³) dx’i tek integral olarak almış; iki bölgenin alanları işaretli toplanıp birbirini götürmüş.','dikkat'),(e10[1],'Yalnız sağdaki bölgenin alanını hesaplamış: ∫₀¹ (x − x³) dx.','dikkat'),(e10[2],'Alt fonksiyonu hiç çıkarmayıp ∫₋₁¹ |x| dx hesaplamış.','bilgi'),(e10[3],'|x| ile |x³| integrallerini toplamış: 1 + 1/2.','islem')],
 'Boyalı bölgelerin alanları toplamı (birimkare).',['İki grafiğin kesişim noktalarını bul. Hangi aralıkta hangi grafik üstte?'],[B_IKI,B_MUT],
 [A('Kesişimleri bul','x³ = x denkleminin kökleri sınırları verir.','x³ − x = 0 → x = −1, 0, 1'),A('Üst fonksiyonu seç','[0, 1] aralığında y = x, [−1, 0] aralığında y = x³ üsttedir.','[0, 1]: x − x³ · [−1, 0]: x³ − x'),A('İntegralleri yaz','İki bölgenin alanı birbirine eşittir (simetri).','∫₀¹ (x − x³) dx = 1/4 = ∫₋₁⁰ (x³ − x) dx'),A('Topla','İki alan toplanır.','1/4 + 1/4 = 1/2')],
 'Kesişim sayısı üçse alanı iki bölgeye ayır ve her bölgede üst eksi alt al.','K-AINT2-03; y = x³ ve y = x',sekil=SK10)

# ================= 11 orta · köklü ifade, değişken değiştirme =================
v11=Fr(str(sp.integrate((sp.sqrt(x)+1)**3/sp.sqrt(x),(x,1,4)))); assert v11==Fr(65,2)
e11=[Fr(65,4),Fr(65),Fr(130),Fr(255,2)]
assert Fr(str(2*sp.integrate(t**3,(t,2,3))))==Fr(65,2) and Fr(65,4)==Fr(65,2)/2 and 2*Fr(255,4)==Fr(255,2) and len({v11,*e11})==5
Q('0011','int2-degisken','orta','Kök İçeren Değişken Değiştirme','u = √x + 1 dönüşümüyle köklü ifadeli belirli integrali yeni sınırlarla hesaplar.','düz',
 '∫₁⁴ (√x + 1)³ / √x dx\nintegralinin değeri kaçtır?',
 v11,[(e11[0],'du = dx/(2√x) olduğundan 2 çarpanı gerekirken bu çarpanı yazmamış: (81 − 16)/4.','islem'),(e11[1],'Dönüşümden sonra 2 ve 1/4 çarpanlarını birlikte atlayıp yalnız 81 − 16 yazmış.','islem'),(e11[2],'2 çarpanını yazdıktan sonra u³’ün ters türevini u⁴ olarak bırakmış: 2·(81 − 16).','islem'),(e11[3],'u = √x + 1 almış ama sınırları x = 1 ve x = 4 olarak bırakıp u cinsinden integrali bu sınırlarla hesaplamış: 2·(256 − 1)/4.','dikkat')],
 'İntegralin değeri.',['İçteki ifadeyi u olarak seç; du’nun x cinsinden ifadesinde √x’e bölüm görünüyor mu?'],[B_DEG,B_KOK],
 [A('Dönüşümü seç','u = √x + 1 için du = dx/(2√x), yani dx/√x = 2 du.','dx/√x = 2 du'),A('Sınırları dönüştür','x = 1’de u = 2, x = 4’te u = 3.','u: 2 → 3'),A('İntegrali yaz','Köklü kısım du içinde kalır.','2·∫₂³ u³ du = 2·[u⁴/4]₂³'),A('Hesapla','Sınır değerleri yazılır.','2·(81 − 16)/4 = 65/2')],
 'Köklü ifadenin türevi paydada görünüyorsa dönüşümü o ifade olarak seç ve sınırları da değiştir.','K-AINT2-04; (√x + 1)³/√x')

# ================= 12 orta · tablo, iç fonksiyonlu =================
gx={0:1,1:4,2:5,3:3,4:2,5:0}; fx={0:3,1:2,2:7,3:9,4:6,5:11}
v12=fx[gx[2]]-fx[gx[0]]; assert v12==9
e12=[fx[2]-fx[0],fx[2],fx[gx[2]]-fx[0],fx[gx[0]]]; assert e12==[4,7,8,2] and len({v12,*e12})==5
SK12=tablo_svg(['x','0','1','2','3','4','5'],[['f(x)']+[str(fx[k]) for k in range(6)],['g(x)']+[str(gx[k]) for k in range(6)]])
Q('0012','int2-degisken','orta','f′(g(x))·g′(x) İntegrali','Tablodaki değerlerle iç fonksiyonlu türev integralini f(g(b)) − f(g(a)) biçiminde hesaplar.','tablo',
 'Gerçel sayılar kümesi üzerinde türevlenebilen f ve g fonksiyonlarının türevleri süreklidir. Bu fonksiyonların bazı değerleri aşağıdaki tabloda verilmiştir.\nBuna göre ∫₀² f′(g(x)) · g′(x) dx integralinin değeri kaçtır?',
 v12,[(e12[0],'g’yi hiç kullanmadan f(2) − f(0) hesaplamış.','dikkat'),(e12[1],'g’yi hiç kullanmadan yalnız üst sınırdaki f(2) değerini yazmış.','dikkat'),(e12[2],'Alt sınırda g(0) yerine x = 0’ı f’ye yazmış: f(g(2)) − f(0).','islem'),(e12[3],'Üst sınır değerini unutup yalnız f(g(0)) = f(1) yazmış.','dikkat')],
 'İntegralin değeri.',['u = g(x) alırsan sınırlar nereye gider? Sonra f′’nin integrali nedir?'],[B_ZIN,B_TAB],
 [A('Değişken değiştir','u = g(x) için du = g′(x) dx olur.','∫₀² f′(g(x))·g′(x) dx = ∫ f′(u) du'),A('Sınırları dönüştür','Sınırlar g ile yeni değerlere gider; değerler tablodan okunur.','x = 0 → u = g(0) = 1 · x = 2 → u = g(2) = 5'),A('Temel teoremi uygula','f′’nin integrali f’nin değer farkıdır.','f(5) − f(1)'),A('Değerleri yaz','Tablodan f(5) = 11 ve f(1) = 2 okunur.','11 − 2 = 9')],
 'f′(g(x))·g′(x) görürsen sonuç f(g(üst)) − f(g(alt)) olur.','K-AINT2-04; f ve g değerleri tabloda',sekil=SK12)

# ================= 13 orta · öncüllü, f ve g grafikleri =================
fE='\\x*\\x*\\x-2*\\x*\\x-2*\\x'
assert sp.expand(x**3-2*x**2-2*x-x-(x**3-2*x**2-3*x))==0 and sp.factor(x**3-2*x**2-3*x)==x*(x+1)*(x-3)
A1_,A2_=3,10
assert A1_-A2_==-7
sx,sy=1.25,0.62
b=['\\draw[-{Stealth},thick] (-2.2,0) -- (5.3,0) node[right] {$x$};',f'\\draw[-{{Stealth}},thick] (0,{-4.4*sy:.3f}) -- (0,{5.5*sy:.3f}) node[above] {{$y$}};',
   arag(fE,'\\x',-1,0,sx,sy,TUR,0.35),arag('\\x',fE,0,3,sx,sy,MAVI,0.3),egri(fE,-1.3,3.15,sx,sy,MOR,'2pt'),egri('\\x',-1.5,3.5,sx,sy,YES,'2pt'),
   f'\\node[font=\\small] at ({-1.5*sx:.3f},{1.6*sy:.3f}) {{$A_1$}};',f'\\draw[->,gray] ({-1.35*sx:.3f},{1.35*sy:.3f}) -- ({-0.6*sx:.3f},{0.2*sy:.3f});',f'\\node[font=\\small] at ({1.7*sx:.3f},{-1.2*sy:.3f}) {{$A_2$}};',
   f'\\node[above,font=\\small,{MOR}] at ({3.15*sx:.3f},{5.1*sy:.3f}) {{$f$}};',f'\\node[right,font=\\small,{YES}] at ({3.5*sx:.3f},{3.5*sy:.3f}) {{$g$}};']
for v_,nm,yv in ((-1,'a',-1),(3,'c',3)): b.append(nok(v_,yv,sx,sy,0.06)); b.append(kes(v_,0,yv,sx,sy,'black!55','dashed'))
b.append(nok(0,0,sx,sy,0.06))
b+= [f'\\node[above left,font=\\small] at ({-1*sx:.3f},0) {{$a$}};',f'\\node[above right,font=\\small] at (0,0) {{$b$}};',f'\\node[below,font=\\small] at ({3*sx:.3f},0) {{$c$}};']
SK13=fig('\n'.join(b))
sira13=['Yalnız I','Yalnız II','I ve II','II ve III','I, II ve III']
Q('0013','int2-sembolik','orta','İki Grafik Arasında Alan İfadeleri','İki grafiğin kesişim noktaları arasındaki bölge alanlarını f − g integralleriyle ilişkilendirip ifadelerin doğruluğunu belirler.','öncüllü',
 'Dik koordinat düzleminde f ve g fonksiyonlarının grafikleri, apsisleri a, b ve c olan noktalarda kesişmektedir. Grafikler arasında kalan boyalı bölgelerin alanları A₁ = 3 ve A₂ = 10 birimkaredir (şekil ölçekli değildir).\nI. ∫ₐᵇ (f(x) − g(x)) dx = 3\nII. ∫ᵇᶜ (g(x) − f(x)) dx = 10\nIII. ∫ₐᶜ (f(x) − g(x)) dx = −7\nifadelerinden hangileri doğrudur?',
 'I, II ve III',[('Yalnız I','II’de [b, c] aralığında g’nin f’nin üstünde olduğunu görmeyip g − f integralini negatif sanmış; III’te de −7 yerine 7 bulduğundan yanlış saymış.','dikkat'),('Yalnız II','I’de f − g integralinin f üstteyken A₁’e eşit olduğunu görmemiş; III’ü de yanlış saymış.','dikkat'),('I ve II','III’te işaretli toplam yerine alanları toplamaya çalışıp 13 bulmuş ve ifadeyi yanlış saymış.','islem'),('II ve III','I’de [a, b] aralığında f − g farkının alana eşit olduğunu fark etmeyip ifadeyi yanlış saymış.','bilgi')],
 'Doğru olan ifadeler.',['Hangi aralıkta f, hangi aralıkta g üstte? f − g farkı bu aralıklarda hangi işaretli?'],[B_SIM,B_IKI],
 [A('Üst fonksiyonu belirle','[a, b] aralığında f, g’nin üstündedir; [b, c] aralığında g, f’nin üstündedir.','[a, b]: f − g ≥ 0 · [b, c]: f − g ≤ 0'),A('I’i incele','f − g pozitif olduğundan integral alana eşittir.','∫ₐᵇ (f − g) dx = A₁ = 3 · doğru'),A('II’yi incele','Bu aralıkta g − f pozitif olduğundan integral alana eşittir.','∫ᵇᶜ (g − f) dx = A₂ = 10 · doğru'),A('III’ü incele','İki aralık işaretli toplanır.','3 + (−10) = −7 · doğru; üç ifade de doğrudur')],
 'Üstteki grafik f ise ∫(f − g) alana eşit, altındaysa alanın negatifine eşittir.','K-AINT2-02; iki grafik, üç kesişim, alanlar verili',sekil=SK13,sira=sira13)

# ================= 14 zor · teğet ve alan =================
f14=3*x**2; tg=sp.diff(f14,x).subs(x,2)*(x-2)+f14.subs(x,2); assert sp.expand(tg)==12*x-12
v14=I(f14,0,1)+I(f14-tg,1,2); assert v14==2
e14=[I(f14,0,2),I(f14,0,1),Fr(8)+6,Fr(6)]; assert e14==[8,1,14,6] and len({v14,*e14})==5
sx,sy=1.7,0.2
b=[eks(0,3,-12,16,sx,sy,xt=[1,2],yt=[-12,-8,-4,4,8,12,16],gy=4,fs_='\\scriptsize'),altgol('3*\\x*\\x',0,1,sx,sy,MAVI,0.3),
   f'\\fill[{TUR},fill opacity=0.32] ({1*sx:.3f},0) -- {pl("3*\\x*\\x",1,2,sx,sy)} -- ({2*sx:.3f},{12*sy:.3f}) -- cycle;',
   egri('3*\\x*\\x',0,2.3,sx,sy,MAVI,'2pt'),f'\\draw[{TUR},line width=1.8pt] ({0.45*sx:.3f},{(12*0.45-12)*sy:.3f}) -- ({2.35*sx:.3f},{(12*2.35-12)*sy:.3f});',
   nok(2,12,sx,sy,0.07),f'\\node[left,font=\\small] at ({2*sx:.3f},{12.3*sy:.3f}) {{$A$}};',f'\\node[right,font=\\small,{MAVI}] at ({2.3*sx:.3f},{15*sy:.3f}) {{$y=3x^2$}};']
SK14=fig('\n'.join(b))
Q('0014','int2-turev-alan','zor','Teğet, Eğri ve x Ekseni','Parabolün bir noktasındaki teğetini türevle yazıp eğri, teğet ve x ekseniyle sınırlı bölgenin alanını parçalayarak hesaplar.','şekilli',
 'Şekilde, y = 3x² parabolü ile bu parabolün A(2, 12) noktasındaki teğeti gösterilmiştir. Parabol, teğet ve x ekseni ile sınırlı bölge boyanmıştır.\nBuna göre boyalı bölgenin alanı kaç birimkaredir?',
 v14,[(e14[0],'Teğeti hiç kullanmayıp parabolün [0, 2] aralığında altında kalan alanı almış.','dikkat'),(e14[1],'Yalnız [0, 1] aralığındaki bölgeyi hesaplamış; [1, 2] aralığındaki parçayı atlamış.','dikkat'),(e14[2],'Teğetin altında kalan üçgenin alanını (6) çıkarmak yerine eklemiş: 8 + 6.','islem'),(e14[3],'Yalnız teğet ile x ekseni ve x = 2 doğrusunun oluşturduğu üçgenin alanını bulmuş.','bilgi')],
 'Boyalı bölgenin alanı (birimkare).',['Teğetin eğimini türevle bul ve doğrunun x eksenini kestiği noktayı belirle; bölge bu noktada iki parçaya ayrılır.'],[B_TEG,B_IKI],
 [A('Teğeti yaz','Türev alınır ve x = 2’de eğim bulunur.','y′ = 6x → eğim 12 · y − 12 = 12(x − 2) → y = 12x − 12'),A('Bölgeyi parçala','Teğet x eksenini x = 1’de keser; [0, 1] aralığında alt sınır x eksenidir, [1, 2] aralığında alt sınır teğettir.','[0, 1]: 3x² · [1, 2]: 3x² − (12x − 12)'),A('İntegralleri yaz','İki parçanın alanı ayrı hesaplanır.','∫₀¹ 3x² dx = 1 · ∫₁² 3(x − 2)² dx = 1'),A('Topla','İki alan toplanır.','1 + 1 = 2')],
 'Teğet eksene değiyorsa bölgeyi bu noktada böl; her parçada üst eksi alt al.','K-AINT2-08; y = 3x², A(2, 12) noktasındaki teğet',sekil=SK14)

# ================= 15 zor · parabol-doğru alanından parametre =================
a_=sp.symbols('a',positive=True); sol=sp.solve(sp.Eq(sp.integrate(a_*x-x**2-2*x,(x,0,a_-2)),36),a_); assert sol==[8]
v15=Fr(16); assert v15==Fr(8**2,4)
e15=[Fr(4),Fr(9),Fr(32),Fr(64)]; assert e15==[8//2,Fr(6**2,4),Fr(8**2,2),8**2] and len({v15,*e15})==5
sx,sy=1.4,0.7
P15='5*\\x-\\x*\\x'
b=['\\draw[-{Stealth},thick] (-0.4,0) -- (7.6,0) node[right] {$x$};','\\draw[-{Stealth},thick] (0,-0.4) -- (0,4.6) node[above] {$y$};',
   arag(P15,'2*\\x',0,3,sx,sy,MAVI,0.3),egri(P15,0,5,sx,sy,MAVI,'2pt'),egri('2*\\x',0,4.2,sx,sy,TUR,'2pt'),f'\\node[below,font=\\small] at ({5*sx:.3f},0) {{$a$}};',f'\\node[below left,font=\\small] at (0,0) {{$O$}};',
   f'\\node[font=\\small] at ({1.6*sx:.3f},{1.9*sy:.3f}) {{$A=36$}};',f'\\node[right,font=\\small,{MAVI}] at ({0.15*sx:.3f},{5.6*sy:.3f}) {{$y=ax-x^2$}};',f'\\node[right,font=\\small,{TUR}] at ({4.25*sx:.3f},{4.2*0.5*sy*2:.3f}) {{$y=2x$}};']
SK15=fig('\n'.join(b))
Q('0015','int2-parametre','zor','Parabol ve Doğru Arasındaki Alandan Parametre','Parabol ile doğru arasındaki alanı kesişim noktasını a cinsinden yazarak hesaplayıp a’yı bulur ve parabolün tepe noktasının ordinatını hesaplar.','şekilli',
 'a, 2’den büyük bir gerçel sayı olmak üzere y = ax − x² parabolü ile y = 2x doğrusu şekilde verilmiştir. Parabol ile doğru arasında kalan boyalı bölgenin alanı şekilde verilmiştir (birimkare; şekil ölçekli değildir).\nBuna göre bu parabolün tepe noktasının ordinatı kaçtır?',
 v15,[(e15[0],'a = 8’i bulup tepe noktasının ordinatı yerine apsisini (a/2) yazmış.','dikkat'),(e15[1],'Alanı parabol ile x ekseni arasında sanıp a³/6 = 36’dan a = 6 bulmuş: a²/4.','bilgi'),(e15[2],'Tepe noktasının ordinatı için a²/4 yerine a²/2 yazmış.','islem'),(e15[3],'Tepe noktasının ordinatı yerine a² değerini yazmış.','islem')],
 'Tepe noktasının ordinatı.',['Parabol ile doğrunun kesiştiği noktaların apsislerini a cinsinden bul ve alanı bu sınırlarla yaz.'],[B_PAR,B_IKI],
 [A('Kesişimleri bul','ax − x² = 2x denkleminin kökleri integralin sınırlarıdır.','x = 0, x = a − 2'),A('Alanı a cinsinden yaz','Üst fonksiyon parabol, alt fonksiyon doğrudur: (a − 2)x − x² integre edilir.','∫₀^(a−2) ((a − 2)x − x²) dx = (a − 2)³/6'),A('a’yı bul','Alan 36’ya eşitlenir.','(a − 2)³ = 216 → a = 8'),A('Tepe ordinatını bul','Tepe noktasının apsisi a/2 = 4’tür; parabolde yerine yazılır.','y = 8·4 − 16 = 16')],
 'Alanı parametre cinsinden hesaplayıp verilen değerle eşitle; sonra asıl soruyu cevapla.','K-AINT2-05; y = ax − x² ve y = 2x, alan şekilde',sekil=SK15)

# ================= 16 zor · noktaya göre simetri =================
f16=3+(x-2)**3/4; assert I(f16,0,4)==12 and I(f16.subs(x,2*x),0,2)==6 and I(f16,0,2)==5
v16=Fr(6); e16=[Fr(12),Fr(24),Fr(5),Fr(3)]; assert len({v16,*e16})==5
sx,sy=1.35,0.95
F16='3+(\\x-2)*(\\x-2)*(\\x-2)/4'
b=[eks(0,4,0,5,sx,sy,xt=[1,2,3,4],yt=[1,2,3,4,5],fs_='\\scriptsize'),egri(F16,0,4,sx,sy,MAVI,'2pt'),nok(2,3,sx,sy,0.08,'red!70!black'),
   f'\\node[above left,font=\\small] at ({2*sx:.3f},{3*sy:.3f}) {{$A$}};',f'\\node[right,font=\\small,{MAVI}] at ({4.05*sx:.3f},{4.9*sy:.3f}) {{$y=f(x)$}};']
SK16=fig('\n'.join(b))
Q('0016','int2-grafik','zor','Simetrik Grafik ve İç Katsayı','Noktaya göre simetrik grafikte integrali dikdörtgen alanına indirip f(2x) için değişken değiştirme uygular.','grafik',
 'Şekilde, [0, 4] aralığında sürekli bir f fonksiyonunun grafiği verilmiştir. Grafik, A noktasına göre simetriktir.\nBuna göre ∫₀² f(2x) dx integralinin değeri kaçtır?',
 v16,[(e16[0],'Değişken değiştirmede 1/2 çarpanını unutup ∫₀⁴ f(u) du = 12 yazmış.','islem'),(e16[1],'du = 2 dx olduğundan 2 ile çarpmış: 2·12.','islem'),(e16[2],'f(2x) yerine f(x) alıp yalnız [0, 2] aralığını (eğrinin altını) hesaplamış.','dikkat'),(e16[3],'İntegral yerine A noktasının ordinatını yazmış.','bilgi')],
 '∫₀² f(2x) dx değeri.',['Simetri merkezinin koordinatları integrali hangi şekle indirger? f(2x) için u = 2x dönüşümünde sınırlar ne olur?'],[B_SIMN,B_DEG],
 [A('Simetri merkezini oku','Grafik A(2, 3) noktasına göre simetriktir.','f(2 + h) + f(2 − h) = 6'),A('Dönüştür','u = 2x için du = 2dx; x = 0 → u = 0, x = 2 → u = 4.','∫₀² f(2x) dx = (1/2)·∫₀⁴ f(u) du'),A('Simetriyi kullan','Merkeze göre simetrik grafikte integral, yüksekliği 3 olan dikdörtgenin alanıdır.','∫₀⁴ f(u) du = 4·3 = 12'),A('Sonuç','Çarpan uygulanır.','(1/2)·12 = 6')],
 'Noktaya göre simetride integral dikdörtgen alanına eşittir; f(mx) için 1/m unutulmaz.','K-AINT2-07; A(2, 3) merkezli simetrik grafik',sekil=SK16)

# ================= 17 zor · öncüllü, üst sınırı fonksiyon =================
Fx=sp.integrate((t-1)*(t-4),(t,0,x**2)); dF=sp.expand(sp.diff(Fx,x)); assert sp.factor(dF)==2*x*(x-1)*(x+1)*(x-2)*(x+2)
assert Fr(str(Fx.subs(x,2)))==Fr(-8,3) and sp.diff(Fx,x).subs(x,sp.Rational(3,2))<0
sira17=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III']
Q('0017','int2-integral-fonk','zor','Üst Sınırı x² Olan İntegral','Üst sınırı fonksiyon olan integralin türevini zincir kuralıyla bulup kök sayısı, artanlık ve değer ifadelerini değerlendirir.','öncüllü',
 'Gerçel sayılar kümesi üzerinde\nF(x) = ∫₀^(x²) (t − 1)(t − 4) dt\nfonksiyonu tanımlanıyor.\nI. F′(x) = 0 denkleminin 5 farklı gerçel kökü vardır.\nII. F fonksiyonu (1, 2) aralığında azalandır.\nIII. F(2) > 0\nifadelerinden hangileri doğrudur?',
 'I ve II',[('Yalnız I','II’de x² − 4 çarpanının (1, 2) aralığındaki işaretini pozitif sanıp F’yi artan bulmuş; III’ü de yanlış saymıştır.','dikkat'),('Yalnız II','F′’yi 2x çarpanı olmadan (x² − 1)(x² − 4) yazıp 4 kök bulmuş; I’i yanlış saymış.','islem'),('I ve III','F(2)’yi pozitif bulmuş; II’yi yanlış saymış.','bilgi'),('Yalnız III','Köklerden birini (x = 0) atlayıp I’i yanlış saymış; II’yi de işaret tablosunu yanlış kurarak reddetmiş; III’ü [0, 4] aralığındaki alanın pozitif olduğunu varsayarak doğru bulmuş.','bilgi')],
 'Doğru olan ifadeler.',['F′(x)’i bulurken üst sınır x² olduğundan hangi çarpan ortaya çıkar? Kökleri ve işaret tablosunu incele.'],[B_ICF,B_INF],
 [A('Türevi bul','Üst sınır x² olduğundan integrandın x²’li hâli 2x ile çarpılır.','F′(x) = (x² − 1)(x² − 4)·2x'),A('I’i incele','Kökler −2, −1, 0, 1, 2’dir.','5 farklı gerçel kök · doğru'),A('II’yi incele','(1, 2) aralığında 2x > 0, x² − 1 > 0, x² − 4 < 0 olduğundan F′ < 0’dır.','F azalandır · doğru'),A('III’ü incele','F(2) = ∫₀⁴ (t² − 5t + 4) dt hesaplanır.','64/3 − 40 + 16 = −8/3 < 0 · yanlış; doğrular I ve II')],
 'Üst sınırı g(x) olan integralin türevinde g′(x) çarpanını unutma; işaret tablosunu çarpanlardan kur.','K-AINT2-09; F(x) = ∫₀^(x²) (t − 1)(t − 4) dt',sira=sira17)

# ================= 18 zor · yol ve yer değiştirme =================
v18=Fr(4)/Fr(4,3); assert v18==3
assert I(x**2-4*x+3,0,4)==Fr(4,3) and I(x**2-4*x+3,0,1)+(-I(x**2-4*x+3,1,3))+I(x**2-4*x+3,3,4)==4
e18=[Fr(1),Fr(1,3),Fr(2),Fr(4)]; assert Fr(8,3)/Fr(4,3)==2 and len({v18,*e18})==5
sx,sy=1.5,0.8
V18='(\\x-1)*(\\x-3)'
b=[eks(0,4,-1,3,sx,sy,xt=[1,2,3,4],yt=[-1,1,2,3],xl='$t$ (s)',yl='$v$ (m/s)',fs_='\\scriptsize'),altgol(V18,0,1,sx,sy,YES,0.3),altgol(V18,1,3,sx,sy,TUR,0.3),altgol(V18,3,4,sx,sy,YES,0.3),
   egri(V18,0,4.1,sx,sy,'black!75','2pt'),nok(0,3,sx,sy,0.07),nok(1,0,sx,sy,0.07),nok(3,0,sx,sy,0.07),nok(4,3,sx,sy,0.07),nok(2,-1,sx,sy,0.07)]
SK18=fig('\n'.join(b))
Q('0018','int2-uygulama','zor','Alınan Yol ve Yer Değiştirme','Hızın işaret değiştirdiği parabolik grafikte yer değiştirme ile toplam yolu integralle hesaplayıp oranlar.','grafik',
 'Doğrusal bir yolda hareket eden bir cismin hız–zaman grafiği şekildeki parabol biçimindedir; grafik üzerinde işaretli noktalar kılavuz çizgilerin kesiştiği noktalardır.\nBuna göre cismin t = 0 ile t = 4 s arasında aldığı toplam yol, bu aralıktaki yer değiştirmesinin kaç katıdır?',
 v18,[(e18[0],'Yolu ve yer değiştirmeyi aynı sanmış (işareti hesaba katmamış): oran 1.','bilgi'),(e18[1],'Oranı ters yazmış: yer değiştirme / yol.','dikkat'),(e18[2],'Alınan yolu hesaplarken son aralığı katmamış: (4/3 + 4/3) / (4/3).','dikkat'),(e18[3],'Yer değiştirmeyi 1 sanıp toplam yolu 4’e bölmeden yazmış.','bilgi')],
 'Toplam yolun yer değiştirmeye oranı.',['Grafikten v(t)’nin kuralını yaz; v(t) hangi aralıkta negatiftir ve bu aralıkta cisim ne yapar?'],[B_HIZ,B_MUT],
 [A('v(t)’yi yaz','Grafik t = 1 ve t = 3’te x eksenini keser ve (0, 3) noktasından geçer.','v(t) = (t − 1)(t − 3) = t² − 4t + 3'),A('Yer değiştirmeyi bul','İşaretli integral alınır.','∫₀⁴ v dt = [t³/3 − 2t² + 3t]₀⁴ = 4/3'),A('Toplam yolu bul','[1, 3] aralığında v < 0 olduğundan mutlak değer alınır.','4/3 + 4/3 + 4/3 = 4'),A('Oranla','Yol, yer değiştirmeye bölünür.','4 ÷ 4/3 = 3')],
 'Yer değiştirme işaretli, yol mutlak değerli integraldir; hız işaret değiştirdiği noktalarda aralığı böl.','K-AINT2-06; v(t) parabol grafiği, kökler grafikten',sekil=SK18)

# ================= 19 zor · parabol, eksen alanı ve türev koşulu =================
a1,b1=sp.symbols('a1 b1',real=True)
sl=sp.solve([sp.Eq(2*a1+b1,0)],[b1],dict=True)[0]; ar=sp.solve(sp.Eq(sp.Abs(sp.integrate(a1*x**2+sl[b1]*x,(x,0,2))),4),a1)
assert sorted(ar)==[-3,3]
fq=3*x**2-6*x; assert I(fq,0,2)==-4 and I(-fq,0,2)==4
v19=Fr(str(fq.subs(x,1))); assert v19==-3
e19=[Fr(3),Fr(-1),Fr(0),Fr(9)]
assert Fr(str((-3*x**2+6*x).subs(x,1)))==3 and Fr(str((x**2-2*x).subs(x,1)))==-1 and Fr(str(sp.diff(fq,x).subs(x,1)))==0 and 3+6==9 and len({v19,*e19})==5
Q('0019','int2-parametre','zor','Eksenle Alan ve Türev Koşulu','Türev koşuluyla katsayılar arasında ilişki kurup parabol ile x ekseni arasındaki alan koşulundan fonksiyonu belirler ve değerini hesaplar.','düz',
 'a pozitif, b gerçel sayı olmak üzere f(x) = ax² + bx fonksiyonu için f′(1) = 0 olup f fonksiyonunun grafiği ile x ekseni arasında kalan sınırlı bölgenin alanı 4 birimkaredir.\nBuna göre f(1) değeri kaçtır?',
 v19,[(e19[0],'Alanı işaretli integrale eşitleyip ∫₀² f(x) dx = 4 almış; a = −3, b = 6 bulmuş (a pozitif koşulunu atlamış): f(1) = 3.','dikkat'),(e19[1],'ax² ve bx’in ters türevlerinde 1/3 ve 1/2 çarpanlarını unutup 8a + 2b = 4a ile |4a| = 4 yazmış: a = 1, b = −2 ve f(1) = −1.','islem'),(e19[2],'a = 3 ve b = −6’yı bulup f(1) yerine f′(1) değerini yazmış.','dikkat'),(e19[3],'f(1) hesaplarken b = −6 yerine 6 yazmış: 3 + 6.','islem')],
 'f(1) değeri.',['Türev koşulu a ile b arasında nasıl bir ilişki verir? Grafiğin x eksenini kestiği noktaları bul.'],[B_PAR,B_MUT],
 [A('Türev koşulu','f′(x) = 2ax + b olduğundan x = 1’de koşul yazılır.','2a + b = 0 → b = −2a'),A('Kökleri bul','f(x) = ax(x − 2) olduğundan grafik x eksenini 0 ve 2’de keser; a > 0 ise bölge eksenin altındadır.','sınırlar 0 ve 2'),A('Alanı hesapla','Eksenin altındaki alan mutlak değerli integraldir.','|∫₀² (ax² − 2ax) dx| = |8a/3 − 4a| = 4a/3 = 4 → a = 3'),A('f(1)’i bul','Katsayılar yerine yazılır.','f(x) = 3x² − 6x → f(1) = 3 − 6 = −3')],
 'Türev koşulundan b’yi a cinsinden yaz, kökleri bulup alanı a cinsinden hesapla.','K-AINT2-05; f′(1) = 0 ve eksenle alan koşulları')

# ================= 20 zor · parçalı grafik =================
f20a=x**2+1; f20b=3*x-1; assert f20a.subs(x,1)==f20b.subs(x,1)==2 and f20b.subs(x,3)==8
v20=I(f20a,0,1)+I(f20b,1,3); assert v20==Fr(34,3)
e20=[I(f20b,1,3),Fr(3,2)+I(f20b,1,3),Fr(27,2),I(f20a,0,1)]; assert e20==[10,Fr(23,2),Fr(27,2),Fr(4,3)] and len({v20,*e20})==5
sx,sy=1.7,0.6
b=[eks(0,4,0,9,sx,sy,xt=[1,2,3,4],yt=[1,2,3,4,5,6,7,8],fs_='\\scriptsize'),egri('\\x*\\x+1',0,1,sx,sy,MAVI,'2.2pt'),f'\\draw[{TUR},line width=2.2pt] ({1*sx:.3f},{2*sy:.3f}) -- ({3*sx:.3f},{8*sy:.3f});',
   nok(0,1,sx,sy,0.07),nok(1,2,sx,sy,0.07),nok(3,8,sx,sy,0.07),f'\\node[right,font=\\small] at ({3.05*sx:.3f},{8*sy:.3f}) {{$y=f(x)$}};']
SK20=fig('\n'.join(b))
Q('0020','int2-grafik','zor','Parça Parça Tanımlı Grafik','Parabol ve doğru parçalarından oluşan sürekli grafiğin parçalarını noktalardan yazıp aralığı bölerek integral hesaplar.','grafik',
 'Şekilde, [0, 3] aralığında tanımlı ve sürekli bir f fonksiyonunun grafiği verilmiştir. Grafik, [0, 1] aralığında tepe noktası y ekseni üzerinde olan bir parabol parçası, [1, 3] aralığında ise bir doğru parçasıdır.\nBuna göre ∫₀³ f(x) dx integralinin değeri kaçtır?',
 v20,[(e20[0],'Yalnız doğru parçasının altındaki alanı (10) hesaplayıp [0, 1] aralığını katmamış.','dikkat'),(e20[1],'[0, 1] aralığındaki parçayı doğru sanıp yamuk alanı (3/2) almış: 3/2 + 10.','bilgi'),(e20[2],'Bütün grafiği (0, 1) ve (3, 8) noktalarını birleştiren tek yamuk sanmış: (1 + 8)·3/2.','bilgi'),(e20[3],'Yalnız parabol parçasının altındaki alanı (4/3) hesaplayıp doğru parçasını katmamış.','dikkat')],
 '∫₀³ f(x) dx değeri.',['İki parçanın denklemlerini grafikteki noktalardan yaz; integrali kırılma noktasında böl.'],[B_PRC,B_ANA],
 [A('Parabol parçasını yaz','Tepe noktası (0, 1) ve (1, 2) noktasından geçen parabol.','f(x) = x² + 1, 0 ≤ x ≤ 1'),A('Doğru parçasını yaz','(1, 2) ve (3, 8) noktalarından geçen doğrunun eğimi 3’tür.','f(x) = 3x − 1, 1 ≤ x ≤ 3'),A('İntegralleri yaz','Aralık kırılma noktasında bölünür.','∫₀¹ (x² + 1) dx = 4/3 · ∫₁³ (3x − 1) dx = 10'),A('Topla','İki değer toplanır.','4/3 + 10 = 34/3')],
 'Parçalı grafikte her parçanın denklemini noktalardan yaz ve kırılma noktasında böl.','K-AINT2-07; parabol ve doğru parçası, noktalar şekilde',sekil=SK20)

# ---------------- yaz ----------------
for q_ in P.ANA: q_['kardes']=None
from collections import Counter
tipler={}
for k_ in KART: tipler.setdefault(k_['tipId'],dict(tipId=k_['tipId'],ad=k_['tip'],kartlar=[],uygulamaKonu=UK))['kartlar'].append(k_['id'])
if len(P.ANA)==20:
    json.dump(P.ANA,open(os.path.join(HD,'integraliki-1.json'),'w'),ensure_ascii=False,indent=1)
    json.dump(dict(konu='İntegral',surum=2,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT Matematik 2018–2026 çıkmış soruları ve yayın soru bankaları (yalnız mantık), MEB 12. sınıf müfredatı.',kartlar=KART,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar','integraliki.json'),'w'),ensure_ascii=False,indent=1)
print(len(P.ANA),'soru · harfler',dict(sorted(Counter(q['cevap']['sik'] for q in P.ANA).items())),'· zorluk',dict(Counter(q['zorluk'] for q in P.ANA)),'· şekilli',sum(1 for q in P.ANA if q.get('sekil')),'· tip',len(tipler),'· kalıp',dict(Counter(q['kalip'] for q in P.ANA)))
