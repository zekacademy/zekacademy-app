"""AYT Matematik · İntegral · 20 soruluk paket (hafif mod; kardeş yok, ipucu 1).
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
P=Parti('integral','İntegral',UK,ders='AYT Matematik',idon='aytmat')
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

# ---------------- kartlar ----------------
tipkayit('int-belirsiz','Belirsiz integral ve başlangıç koşulu','K-AINT-01')
tipkayit('int-egri-alan','Eğri ile eksen arasında alan','K-AINT-02')
tipkayit('int-iki-egri','İki eğri arasında alan','K-AINT-03')
tipkayit('int-grafik-alan','Grafikten alan ve toplam','K-AINT-04')
tipkayit('int-ozellik','İntegral özellikleri ve simetri','K-AINT-05')
tipkayit('int-degisken','Değişken değiştirme','K-AINT-06')
tipkayit('int-turev-iliski','Türev ve integral ilişkisi','K-AINT-07')
tipkayit('int-denklem','Sabit içeren integral denklemi','K-AINT-08')
tipkayit('int-uygulama','İntegralin günlük uygulamaları','K-AINT-09')
kart('K-AINT-01','Belirsiz integral ve başlangıç koşulu','Türevi verilen fonksiyonun kuvvet kuralıyla ters türevi alınır; verilen bir noktadaki değerle sabit bulunur ve istenen noktada hesaplanır.','Üssü artırıp katsayıyı bölmemek; sabiti unutmak ya da işaretini ters almak; ters türev yerine türev değerini hesaplamak.','kolay','düz',3,'int-belirsiz','Belirsiz integral ve başlangıç koşulu')
kart('K-AINT-02','Eğri ile eksen arasında alan','Sınırları grafikten okunan alanlar belirli integralle hesaplanır; eğri x eksenini kesiyorsa her işaret aralığı ayrı alınır.','İşaret değişimini görmeyip tek integral almak (alanların birbirini götürmesi); alt sınırı 0 almak; integral yerine fonksiyon değerlerinin farkını almak.','orta','şekilli',4,'int-egri-alan','Eğri ile eksen arasında alan')
kart('K-AINT-03','İki eğri arasında alan','Kesişim noktaları sınır olur; üstteki fonksiyondan alttaki çıkarılıp integral alınır; alan bir koşula bağlıysa parametre denklemden çözülür.','Eğriyi x eksenine göre ayrı ayrı integre edip toplamak; üst–alt sırasını ters almak; kesişimlerin yerine başka sınır kullanmak.','zor','şekilli',5,'int-iki-egri','İki eğri arasında alan')
kart('K-AINT-04','Grafikten alan ve toplam','Doğru parçalarından oluşan grafikte alan geometrik şekillerle, kırık olmayan grafikte alt ve üst toplam sınırlarıyla bulunur; x ekseninin altı negatif sayılır.','Üçgende ½ çarpanını unutmak; negatif bölgeyi pozitif saymak; uzaklık–zaman gibi grafiklerde alanın anlamını karıştırmak.','orta','grafik',4,'int-grafik-alan','Grafikten alan ve toplam')
kart('K-AINT-05','İntegral özellikleri ve simetri','Her ifadeye integralin toplam, sabit çarpan ve aralık özellikleri ile tek–çift fonksiyon simetrisi ayrı ayrı uygulanıp doğruluğu denetlenir.','Simetrik aralıkta her integralin sıfır olduğunu sanmak; çarpımın integralini integrallerin çarpımı sanmak; mutlak değeri açmadan integral almak.','orta','öncüllü',4,'int-ozellik','İntegral özellikleri ve simetri')
kart('K-AINT-06','Değişken değiştirme','İçteki ifade u olarak seçilir; du bulunur; sınırlar yeni değişkene dönüştürülür ya da sonuç x cinsinden yazılıp eski sınırlar kullanılır.','du’daki katsayıyı eksik ya da fazla bırakmak; sınırları değiştirmeden u cinsinden integral almak; f(mx) için 1/m çarpanını unutmak.','orta','düz',4,'int-degisken','Değişken değiştirme')
kart('K-AINT-07','Türev ve integral ilişkisi','f′ grafiği ile f’nin değişimi alandan; F(x) = ∫ₐˣ f(t) dt için F′ = f olduğundan F’nin artanlığı, uç noktaları ve değerleri f’nin işaretinden ve alanlarından bulunur.','f′ grafiğinden f(x) değerini doğrudan okumak; işaret değişiminde yerel maksimum ile minimumu karıştırmak; alt sınır değerini hesaba katmamak.','zor','grafik',5,'int-turev-iliski','Türev ve integral ilişkisi')
kart('K-AINT-08','Sabit içeren integral denklemi','Belirli integral bir sayı olduğundan k diye adlandırılır; fonksiyonun ifadesine yazılıp integral alınarak k için denklem kurulur.','Sabit terimin integralini k yerine k·(üst − alt) yazmamak; denklemde işaret hatası; k’yı bulunca asıl soruyu cevaplamamak.','zor','düz',4,'int-denklem','Sabit içeren integral denklemi')
kart('K-AINT-09','İntegralin günlük uygulamaları','Hız–zaman, debi–zaman ve alan–maliyet bağlamlarında integral toplam yol, toplam hacim ve toplam bedeli verir; birimler çarpımı sonucun birimini belirler.','Alan yerine tek bir değeri çarpmak; parçalı alanlarda aralık dışına taşmak; fiyatı yanlış bölgeye uygulamak.','orta','hikâyeli',4,'int-uygulama','İntegralin günlük uygulamaları')

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

# ================= 01 kolay · belirsiz integral =================
f1=3*x**2-4*x+1; F1=sp.integrate(f1,x)+2
assert sp.simplify(F1.subs(x,0))==2
v1=int(F1.subs(x,3)); assert v1==14
e1=[int((F1-2).subs(x,3)),int(f1.subs(x,3)),int((x**3-4*x**2+x+2).subs(x,3)),int((F1-4).subs(x,3))]
assert e1==[12,16,-4,10] and len({v1,*e1})==5
Q('0001','int-belirsiz','kolay','Başlangıç Koşulu','Türevi verilen fonksiyonun ters türevini alıp sabiti bir noktadaki değerden bularak başka bir noktadaki değeri hesaplar.','düz',
 'Gerçel sayılar kümesi üzerinde türevlenebilir bir f fonksiyonunun türevi f′(x) = 3x² − 4x + 1 biçimindedir ve f(0) = 2 olarak veriliyor.\nBuna göre f(3) değeri kaçtır?',
 v1,[(e1[0],'Ters türevi doğru alıp sabiti eklemeyi unutmuş: 27 − 18 + 3.','dikkat'),(e1[1],'Ters türev almak yerine türev fonksiyonunda x = 3 değerini hesaplamış: 27 − 12 + 1.','bilgi'),(e1[2],'−4x teriminin integralini −4x² yazmış (yeni üsse bölmemiş): x³ − 4x² + x + 2.','bilgi'),(e1[3],'f(0) = 2 koşulundan sabiti −2 bulmuş (c = −2): 27 − 18 + 3 − 2.','islem')],
 'f(3) değeri.',['f′ verildiğine göre f’yi bulmak için hangi işlemi uygulaman gerekir ve sabit nasıl belirlenir?'],[B_BEL],
 [A('Ters türevi al','Her terimde üs bir artırılıp yeni üsse bölünür; sabit c eklenir.','f(x) = x³ − 2x² + x + c'),A('Sabiti bul','f(0) = 2 koşulu x = 0 yazılarak uygulanır.','f(0) = c = 2'),A('x = 3’te hesapla','Bulunan f(x) ifadesinde x yerine 3 yazılır.','27 − 18 + 3 + 2 = 14')],
 'Ters türevde sabiti her zaman verilen noktadaki değerle belirle.','K-AINT-01; f′ verilmiş, f(0) bilinen, f(3) istenen')

# ================= 02 kolay · eğri altı alan (şekilli) =================
f2=x**2+1; v2=I(f2,1,3); assert v2==Fr(32,3)
e2=[Fr((f2.subs(x,3)-f2.subs(x,1))),I(x**2,1,3),I(f2,0,3),Fr(2*f2.subs(x,2))]
assert e2==[8,Fr(26,3),12,10]
sx,sy=1.15,0.3
b=[eks(0,4,0,14,sx,sy,xt=[1,2,3,4],yt=[2,4,6,8,10,12,14],gy=1,yl='$y$'),
   altgol('\\x*\\x+1',1,3,sx,sy,MAVI,0.3),egri('\\x*\\x+1',0,3.55,sx,sy,MAVI),
   kes(1,0,2,sx,sy,MAVI,'thick'),kes(3,0,10,sx,sy,MAVI,'thick'),
   f'\\node[right,font=\\small] at ({3.58*sx:.3f},{13.6*sy:.3f}) {{$f$}};']
SK2=fig('\n'.join(b))
Q('0002','int-egri-alan','kolay','Eğri Altındaki Alan','Grafiği verilen fonksiyonun, x ekseni ve iki dikey doğru arasında kalan bölgesinin alanını belirli integralle hesaplar.','şekilli',
 'Şekilde, f(x) = x² + 1 fonksiyonunun grafiği ile x ekseni ve iki dikey doğru arasında kalan boyalı bölge gösterilmiştir.\nBuna göre boyalı bölgenin alanı kaç birimkaredir?',
 v2,[(e2[0],'İntegral yerine f(3) − f(1) fark değerini hesaplamış: 10 − 2.','bilgi'),(e2[1],'x² + 1 ifadesinde sabit terimin integralini (x) yazmayı unutmuş: (27 − 1)/3.','islem'),(e2[2],'Alt sınır olarak 1 yerine 0 almış: ∫₀³ (x² + 1) dx.','dikkat'),(e2[3],'Bölgeyi dikdörtgen sanıp yüksekliği olarak aralığın ortasındaki f(2) = 5 değerini almış: 2 × 5.','bilgi')],
 'Boyalı bölgenin alanı (birimkare).',['Sınırları şekilden oku; alan hangi integralle ifade edilir?'],[B_ALN,B_ANA],
 [A('Sınırları oku','Boyalı bölge x ekseninden eğriye kadar uzanır; sol ve sağ dikey doğrular şekilde işaretlidir.','x = 1 ve x = 3'),A('İntegrali kur','Alan, f’nin bu aralıktaki belirli integralidir.','A = ∫₁³ (x² + 1) dx'),A('Ters türevi al','x² için x³/3, 1 için x yazılır.','[x³/3 + x]₁³'),A('Sınırları yaz','Üst sınır değerinden alt sınır değeri çıkarılır.','(9 + 3) − (1/3 + 1) = 32/3')],
 'Alan istendiğinde sınırları şekilden oku, ters türevi al ve üst eksi alt hesapla.','K-AINT-02; f(x) = x² + 1, sınırlar şekilden okunur',sekil=SK2)

# ================= 03 kolay · hız-zaman grafiği (hikâyeli) =================
pts3=[(0,0),(4,12),(10,12),(15,0)]
v3=poly_alan(pts3); assert v3==126
e3=[Fr(4*12,2)+Fr(5*12,2)+0,Fr(6*12),Fr((15+4)*12,2),Fr((15+5)*12,2)]
assert e3==[54,72,114,120] and len({v3,*e3})==5
sx,sy=0.5,0.3
b=[eks(0,16,0,14,sx,sy,xt=[2,4,6,8,10,12,14,15],yt=[2,4,6,8,10,12,14],xl='$t$ (s)',yl='$v$ (m/s)',fs_='\\scriptsize'),
   pgol(pts3,sx,sy,YES,0.28),poly(pts3,sx,sy,YES)]
SK3=fig('\n'.join(b))
Q('0003','int-uygulama','kolay','Hız–Zaman Grafiği','Hız–zaman grafiğinin altında kalan alanı geometrik şekillerle bularak alınan yolu hesaplar.','hikâyeli',
 'Bir otomobil firmasının test sürücüsü, düz bir pistte aracı hareketsiz durumdan kaldırıp önce hızlandırıyor, ardından bir süre sabit hızla gidiyor ve en sonunda frenleyerek aracı durduruyor. Aracın hızı, hareket başladıktan sonra geçen zamana bağlı olarak şekildeki grafikle gösterilmiştir.\nBuna göre araç, hareketin başından durduğu ana kadar kaç metre yol almıştır?',
 v3,[(e3[0],'Yamuğun yalnız iki üçgen parçasını toplamış, sabit hızlı bölümü hesaba katmamış.','dikkat'),(e3[1],'Yalnız sabit hızlı bölümün alanını (6 s × 12 m/s) almış.','dikkat'),(e3[2],'Grafiği yamuk sanıp üst taban olarak ilk üçgenin tabanını (4 s) almış: (15 + 4) × 12 / 2.','islem'),(e3[3],'Grafiği yamuk sanıp üst taban olarak son üçgenin tabanını (5 s) almış: (15 + 5) × 12 / 2.','islem')],
 'Aracın toplam yolu (m).',['Alınan yol, hız–zaman grafiğinde neye karşılık gelir? Grafiği tanıdığın şekillere ayır.'],[B_ALN,B_GRF],
 [A('Alanı yola çevir','Hız–zaman grafiği ile zaman ekseni arasındaki alan yolu verir.','yol = ∫ v dt = alan'),A('Şekillere ayır','Grafik, sol üçgen + ortadaki dikdörtgen + sağ üçgen biçimindedir.','4 s ve 12 m/s · 6 s ve 12 m/s · 5 s ve 12 m/s'),A('Alanları hesapla','Üçgenlerde ½ × taban × yükseklik, dikdörtgende taban × yükseklik alınır.','24 + 72 + 30'),A('Topla','Üç alan toplanır.','24 + 72 + 30 = 126')],
 'Hız–zaman grafiğinde alan yoldur; parçaları ayrı ayrı hesaplayıp topla.','K-AINT-09; hız–zaman yamuk grafiği',sekil=SK3)

# ================= 04 kolay · grafikten a bulup alan =================
a4=Fr(3,2); v4=Fr(a4*Fr(8,3)); assert v4==4 and a4*4==6
e4=[Fr(1,2)*2*6,Fr(3)*Fr(8,3),Fr(2*6),Fr(6)*Fr(8,3)]
assert e4==[6,8,12,16] and len({v4,*e4})==5
sx,sy=1.7,0.46
b=[eks(0,2,0,9,sx,sy,xt=[1,2],yt=[2,4,6,8],gy=1),altgol('1.5*\\x*\\x',0,2,sx,sy,MAVI,0.28),egri('1.5*\\x*\\x',0,2.45,sx,sy,MAVI),
   kes(2,0,6,sx,sy,MAVI,'thick'),f'\\draw[black!60,dashed] (0,{6*sy:.3f}) -- ({2*sx:.3f},{6*sy:.3f});',nok(2,6,sx,sy,0.07),
   f'\\node[above left,font=\\small] at ({2*sx:.3f},{6*sy:.3f}) {{$(2,\\,6)$}};',f'\\node[right,font=\\small] at ({2.48*sx:.3f},{8.8*sy:.3f}) {{$f$}};']
SK4=fig('\n'.join(b))
Q('0004','int-egri-alan','kolay','Katsayıyı Grafikten Bulma','Grafikteki bir noktadan fonksiyonun katsayısını bulup eğri altındaki alanı hesaplar.','şekilli',
 'a bir gerçel sayı olmak üzere f(x) = ax² fonksiyonunun grafiği şekilde verilmiştir. Grafik, x ekseni ve x = 2 doğrusu arasında kalan bölge boyanmıştır.\nBuna göre boyalı bölgenin alanı kaç birimkaredir?',
 v4,[(e4[0],'Bölgeyi, köşeleri (0, 0), (2, 0) ve (2, 6) olan bir üçgen sanmış: ½ × 2 × 6.','bilgi'),(e4[1],'(2, 6) noktasından a·2 = 6 diyerek a = 3 bulmuş (x’in karesini almamış): ∫₀² 3x² dx.','islem'),(e4[2],'Bölgeyi dikdörtgen sanmış: 2 × 6.','bilgi'),(e4[3],'a yerine f(2) = 6 değerini kullanmış: ∫₀² 6x² dx.','dikkat')],
 'Boyalı bölgenin alanı (birimkare).',['Şekilde işaretli noktayı fonksiyonda yerine koyarak katsayıyı bul.'],[B_ALN,B_ANA],
 [A('a’yı bul','İşaretli nokta eğri üzerindedir; x ve y değerleri f(x) = ax²’de yerine yazılır.','6 = a × 2² → a = 3/2'),A('İntegrali kur','Alan, x = 0’dan x = 2’ye integraldir.','A = ∫₀² (3/2) x² dx'),A('Hesapla','x² için x³/3 yazılıp sınırlar uygulanır.','(3/2) × (8/3 − 0) = 4')],
 'Katsayı bilinmiyorsa önce grafikteki noktadan bul, sonra integrali kur.','K-AINT-02; f(x) = ax² grafiği, bir nokta verili',sekil=SK4)

# ================= 05 orta · alt-üst toplam (öncüllü, şekilli) =================
p5=[(0,1),(2,2),(4,4),(6,7)]
I5=2*(2+4+7); II5=2*(1+2+4); III5=4*4+2*7
assert (I5,II5,III5)==(26,14,30)
# f artan ve sürekli → alan < sağ-uç üst sınırlar, > sol-uç alt sınırı
dogru5='I ve III'; sira5=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III']
sx,sy=0.7,0.46
b=[eks(0,6,0,8,sx,sy,xt=[2,4,6],yt=[1,2,4,7]),
   altgol('1+\\x/4+\\x*\\x/8',0,6,sx,sy,MAVI,0.2),egri('1+\\x/4+\\x*\\x/8',0,6,sx,sy,MAVI,'1.9pt')]
assert all(Fr(1)+Fr(a,4)+Fr(a*a,8)==Fr(b_) for a,b_ in p5)
for a,b_ in p5[1:]: b.append(kes(a,0,b_,sx,sy)); b.append(f'\\draw[black!60,dashed] (0,{b_*sy:.3f}) -- ({a*sx:.3f},{b_*sy:.3f});')
for a,b_ in p5: b.append(nok(a,b_,sx,sy,0.07))
b.append(f'\\node[above left,font=\\small] at ({6*sx:.3f},{7*sy:.3f}) {{$f$}};')
SK5=fig('\n'.join(b))
Q('0005','int-grafik-alan','orta','Alt ve Üst Sınır','Artan bir fonksiyonun grafiğinden okunan değerlerle alan için üst ve alt sınır niteliğindeki toplamları değerlendirir.','öncüllü',
 '[0, 6] kapalı aralığında tanımlı, sürekli ve artan bir f fonksiyonunun grafiği ile bu grafikteki dört nokta şekilde gösterilmiştir; noktaların koordinatları eksenlerdeki işaretlerden okunabilmektedir.\nBuna göre f fonksiyonunun grafiği ile x ekseni arasında kalan bölgenin alanı,\nI. 2 · (f(2) + f(4) + f(6))\nII. 2 · (f(0) + f(2) + f(4))\nIII. 4 · f(4) + 2 · f(6)\nifadelerinden hangilerinden küçüktür?',
 dogru5,[('Yalnız I','III. ifadenin de bir üst sınır olduğunu görmemiş; yalnızca sağ uç değerleriyle yazılan I’i üst sınır saymış.','bilgi'),('Yalnız II','Sol uç değerleriyle yazılan toplamı (II) üst sınır sanmış; artan fonksiyonda bunun alt sınır olduğunu bilmemiş.','bilgi'),('I ve II','Sol uç toplamını da üst sınır saymış ve III’ün [0, 4] aralığında f(4) ile sınırlandığını görmemiş.','dikkat'),('Yalnız III','I’in de bir üst sınır olduğunu görmeyip yalnızca III’ü seçmiş; sağ uç değerleriyle yazılan toplamın artan fonksiyonda alandan büyük olduğunu bilmemiş.','bilgi')],
 'Alanın hangi ifadelerden küçük olduğu.',['Her ifadedeki dikdörtgenlerin yüksekliğini, o aralıktaki en büyük ve en küçük f değeriyle karşılaştır.'],[B_RMN,B_ALN],
 [A('Değerleri oku','Grafikteki noktaların y değerleri eksenlerden okunur.','f(0) = 1, f(2) = 2, f(4) = 4, f(6) = 7'),A('Üst sınırları belirle','Artan f’de her aralıkta en büyük değer sağ uçtadır; I, [0, 6]’yı 2’şer uzunlukta üç dikdörtgenle, III ise [0, 4] ve [4, 6] aralıklarını f(4) ve f(6) ile örter.','I = 26 · III = 30'),A('II’yi incele','Sol uç değerleri her aralıkta en küçük değerdir; bu toplam alandan küçüktür.','II = 14 < alan'),A('Sonucu yaz','Alan, I ve III’ten küçük; II’den büyüktür.','I ve III')],
 'Dikdörtgen yüksekliklerini aralıktaki gerçek değerlerle karşılaştırarak her toplamın alandan büyük mü küçük mü olduğunu belirle.','K-AINT-04; artan fonksiyon, alt ve üst toplam ifadeleri',sekil=SK5,sira=sira5)

# ================= 06 orta · iki eğri arasında alan =================
v6=I(x+2-x**2,-1,2); assert v6==Fr(9,2)
Fi=x**2/2+2*x-x**3/3
e6=[I(x**2,-1,2),I(x+2-x**2,0,2),Fr(str(Fi.subs(x,2)+Fi.subs(x,-1))),I(x+2-x**2,-2,1)]
assert e6==[3,Fr(10,3),Fr(13,6),Fr(3,2)] and len({v6,*e6})==5
sx,sy=0.85,0.62
b=[eks(-2,3,0,6,sx,sy,xt=[-2,-1,1,2,3],yt=[1,2,3,4,5,6]),arag('\\x+2','\\x*\\x',-1,2,sx,sy,TUR,0.32),
   egri('\\x*\\x',-2,2.4,sx,sy,MAVI),egri('\\x+2',-2,3,sx,sy,TUR),nok(-1,1,sx,sy,0.07),nok(2,4,sx,sy,0.07),
   f'\\node[left,font=\\small,{MAVI}] at ({-2*sx:.3f},{4.35*sy:.3f}) {{$y=x^2$}};',
   f'\\node[right,font=\\small,{TUR}] at ({3.0*sx:.3f},{5*sy:.3f}) {{$y=x+2$}};']
SK6=fig('\n'.join(b))
Q('0006','int-iki-egri','orta','Eğri ve Doğru Arasında Alan','Parabol ile doğru arasında kalan bölgenin alanını kesişim noktalarını bulup iki fonksiyonun farkını integre ederek hesaplar.','şekilli',
 'Dik koordinat düzleminde bir parabol ile bir doğrunun grafikleri şekilde verilmiştir; grafiklerin denklemleri şekilde yazılıdır ve iki grafik arasında kalan bölge boyanmıştır.\nBuna göre boyalı bölgenin alanı kaç birimkaredir?',
 v6,[(e6[0],'Yalnız parabolün [−1, 2] aralığında x ekseniyle yaptığı alanı hesaplamış.','dikkat'),(e6[1],'Alt sınırı −1 yerine 0 almış: ∫₀² (x + 2 − x²) dx.','dikkat'),(e6[2],'Ters türevi doğru bulup sınır değerlerini çıkarmak yerine toplamış: F(2) + F(−1).','islem'),(e6[3],'x² − x − 2 denklemini yanlış çarpanlara ayırıp sınırları −2 ve 1 bulmuş.','islem')],
 'Boyalı bölgenin alanı (birimkare).',['Sınırlar için iki grafiğin kesiştiği noktaları bul; sonra hangi fonksiyonun üstte olduğuna bak.'],[B_IKI,B_ALN],
 [A('Kesişimi bul','İki denklem eşitlenir.','x² = x + 2 → x² − x − 2 = 0 → x = −1, x = 2'),A('Üstteki fonksiyonu seç','Aralığın içinde doğru, parabolün üstündedir.','üst: x + 2 · alt: x²'),A('İntegrali kur','Üstten alt çıkarılıp sınırlar arasında integral alınır.','A = ∫₋₁² (x + 2 − x²) dx'),A('Hesapla','Ters türev alınıp sınırlar yazılır.','[x²/2 + 2x − x³/3]₋₁² = 10/3 − (−7/6) = 9/2')],
 'İki eğri arasındaki alanda üst fonksiyondan alt fonksiyon çıkarılır; sınırlar kesişim noktalarıdır.','K-AINT-03; parabol ile doğru, kesişimler hesaplanır',sekil=SK6)

# ================= 07 orta · işaret değiştiren parabol =================
f7=x**2-4*x+3
a7=I(f7,0,1); b7=-I(f7,1,3); v7=a7+b7; assert (a7,b7,v7)==(Fr(4,3),Fr(4,3),Fr(8,3)) and I(f7,0,3)==0
Fb=x**3/3-2*x**2; e7a=abs(Fr(str(Fb.subs(x,1)-Fb.subs(x,0))))+abs(Fr(str(Fb.subs(x,3)-Fb.subs(x,1))))
Fc=x**3/3-4*x**2+3*x; e7b=abs(Fr(str(Fc.subs(x,1)-Fc.subs(x,0))))+abs(Fr(str(Fc.subs(x,3)-Fc.subs(x,1))))
e7=[Fr(0),a7,e7a,e7b]; assert e7==[0,Fr(4,3),9,18] and len({v7,*e7})==5
sx,sy=1.15,0.52
b=[eks(0,4,-2,5,sx,sy,xt=[1,2,3,4],yt=[-1,1,2,3,4,5]),
   altgol('\\x*\\x-4*\\x+3',0,1,sx,sy,MAVI,0.3),altgol('\\x*\\x-4*\\x+3',1,3,sx,sy,TUR,0.3),
   egri('\\x*\\x-4*\\x+3',-0.0,3.6,sx,sy,'black!70'),kes(3,0,0,sx,sy),nok(1,0,sx,sy,0.07),nok(3,0,sx,sy,0.07),nok(0,3,sx,sy,0.07),
   f'\\node[right,font=\\small] at ({3.65*sx:.3f},{(3.6**2-4*3.6+3)*sy:.3f}) {{$f$}};']
SK7=fig('\n'.join(b))
Q('0007','int-egri-alan','orta','İşaret Değiştiren Eğri','Grafiği x eksenini kesen fonksiyonda, eksen altındaki ve üstündeki bölgeleri ayırarak toplam alanı hesaplar.','şekilli',
 'Dik koordinat düzleminde, f(x) = x² − 4x + 3 fonksiyonunun grafiği, x ekseni ve y ekseni ile x = 3 doğrusu arasında kalan bölge şekilde iki ayrı renkle boyanmıştır.\nBuna göre boyalı bölgelerin alanları toplamı kaç birimkaredir?',
 v7,[(e7[0],'∫₀³ f(x) dx değerini hesaplayıp işaret değişimini görmemiş; alanları birbirini götürmüş.','bilgi'),(e7[1],'Yalnız x ekseninin üstündeki mavi bölgenin alanını almış.','dikkat'),(e7[2],'Ters türevde 3 sabit teriminin integralini (3x) yazmayı unutmuş: x³/3 − 2x².','islem'),(e7[3],'−4x teriminin integralini −4x² yazmış (2’ye bölmemiş): x³/3 − 4x² + 3x.','islem')],
 'Boyalı bölgelerin alanları toplamı (birimkare).',['f’nin x eksenini kestiği noktaları bul; eksenin altındaki bölge integralde nasıl görünür?'],[B_ALN,B_MUT],
 [A('Köklerini bul','f(x) = 0 denklemi çarpanlara ayrılır.','(x − 1)(x − 3) = 0 → x = 1, x = 3'),A('İşareti incele','[0, 1] aralığında f pozitif, [1, 3] aralığında negatiftir.','mavi: üstte · turuncu: altta'),A('Ters türevi al','F(x) = x³/3 − 2x² + 3x bulunur.','F(0) = 0 · F(1) = 4/3 · F(3) = 0'),A('Alanları topla','Altta kalan bölgenin integrali negatif olduğundan mutlak değer alınır.','4/3 + |0 − 4/3| = 8/3')],
 'Eğri x eksenini kesiyorsa integrali kökler arasında böl, her bölgenin alanını pozitif al.','K-AINT-02; parabol x ekseninin hem üstünde hem altında',sekil=SK7)

# ================= 08 orta · tablo, alt ve üst toplam hikâyeli =================
tq=[0,2,4,6,8]; qv=[2,3,5,8,12]; dt=2
A8=sum(qv[:-1])*dt; B8=sum(qv[1:])*dt; v8=Fr(A8+B8,2); assert (A8,B8,v8)==(36,56,46)
e8=[Fr(A8+B8,2*dt),Fr(sum(qv)),Fr(A8),Fr(sum(qv[:-1])+sum(qv[1:])*dt,2)]
assert e8==[23,30,36,37] and len({v8,*e8})==5
SK8=tablo_svg(['t (dk)']+[str(a) for a in tq],[['q (L/dk)']+[str(a) for a in qv]])
Q('0008','int-grafik-alan','orta','Ölçüm Tablosu ile Toplam','Artan bir debinin ölçüm tablosundan sol ve sağ uç toplamlarını bulup ortalamalarını hesaplar.','tablo',
 'Bir su arıtma tankına giren suyun debisi, boşken ölçüm başlatıldıktan sonra 2 dakikada bir ölçülüp tabloya işlenmiştir; debi, ölçüm süresi boyunca sürekli ve artan biçimde değişmiştir.\nHer ölçüm aralığında debi, aralığın başındaki ölçüm değerine eşitmiş gibi hesaplanan toplam su miktarı A litre, aralığın sonundaki ölçüm değerine eşitmiş gibi hesaplanan toplam su miktarı B litre olsun.\nBuna göre (A + B)/2 değeri kaçtır?',
 v8,[(e8[0],'A ve B toplamlarını hesaplarken her aralığın uzunluğu olan 2 dakikayı çarpmayı unutmuş.','dikkat'),(e8[1],'Beş ölçüm değerinin tamamını toplamış: 2 + 3 + 5 + 8 + 12.','dikkat'),(e8[2],'Yalnız A değerini (sol uç toplamını) bulup ortalamayı almamış.','dikkat'),(e8[3],'A’yı süre ile çarpmadan (18), B’yi süre ile çarpıp (56) ortalamasını almış.','islem')],
 '(A + B)/2 değeri (litre).',['Her aralıkta su miktarı debi × süre ile bulunur; A hangi ölçüm değerlerini, B hangilerini kullanır?'],[B_RMN],
 [A('A’yı hesapla','Aralık başındaki debiler (2, 3, 5, 8) süre ile çarpılıp toplanır.','2 × (2 + 3 + 5 + 8) = 36'),A('B’yi hesapla','Aralık sonundaki debiler (3, 5, 8, 12) kullanılır.','2 × (3 + 5 + 8 + 12) = 56'),A('Ortalamayı al','İki toplamın aritmetik ortalaması hesaplanır.','(36 + 56)/2 = 46')],
 'Artan debide sol uç toplamı az, sağ uç toplamı fazla verir; ikisinin ortalaması gerçeğe yaklaşır.','K-AINT-04; ölçüm tablosu, sol ve sağ uç toplamları',sekil=SK8)

# ================= 09 orta · öncüllü, özellikler ve simetri =================
a_=I(x**3+x,-2,2); b_=I(x**2,-1,1); assert a_==0 and b_==Fr(2,3)
c1=I(1-x,0,1)+I(x-1,1,2); c2=I(x-1,0,2); assert (c1,c2)==(1,0)
sira9=['Yalnız I','Yalnız II','I ve II','II ve III','I, II ve III']
Q('0009','int-ozellik','orta','Simetri ve Özellikler','Tek ve çift fonksiyonların simetrik aralıktaki integrallerini ve mutlak değerli integrali yorumlayarak doğru ifadeleri belirler.','öncüllü',
 'I. ∫₋₁¹ x² dx = 0\nII. ∫₋₂² (x³ + x) dx = 0\nIII. ∫₀² |x − 1| dx = ∫₀² (x − 1) dx\nifadelerinden hangileri doğrudur?',
 'Yalnız II',[('Yalnız I','x² için simetrik aralıkta sıfır sanıp I’i doğru bulmuş; x³ + x’i tek fonksiyon olarak görmeyip II’yi yanlış saymış.','bilgi'),('I ve II','x² için de simetrik aralıkta sıfır sonucunu uygulamış; çift fonksiyonda bu doğru değildir.','bilgi'),('II ve III','III’te mutlak değeri açmadan |x − 1| yerine (x − 1) yazılabileceğini sanmış; oysa ∫₀² |x − 1| dx = 1, ∫₀² (x − 1) dx = 0’dır.','dikkat'),('I, II ve III','Üç ifadede de integralin sıfır ya da eşit çıktığını varsaymış; I ve III’ü incelememiş.','dikkat')],
 'Doğru olan ifadeler.',['Her ifadede integrali alınan fonksiyonun tek mi çift mi olduğuna ve mutlak değerin nerede işaret değiştirdiğine bak.'],[B_OZL,B_MUT],
 [A('I’i incele','x² çift fonksiyondur; simetrik aralıkta integral 2 × ∫₀¹ x² dx olur, sıfır değildir.','∫₋₁¹ x² dx = 2/3 ≠ 0'),A('II’yi incele','x³ + x tek fonksiyondur; [−2, 2] simetriktir.','∫₋₂² (x³ + x) dx = 0'),A('III’ü incele','|x − 1|, x = 1’de işaret değiştirir; sol taraf parçalara ayrılır.','∫₀² |x − 1| dx = 1/2 + 1/2 = 1 · ∫₀² (x − 1) dx = 0'),A('Sonucu yaz','Yalnız II doğrudur.','Yalnız II')],
 'Simetrik aralıkta integral almadan önce fonksiyonun simetrisine bak.','K-AINT-05; tek–çift simetri ve mutlak değer',sira=sira9)

# ================= 10 orta · tablo + türev integral =================
fx={1:4,3:9,5:15,7:20}
t1=Fr(fx[5]-fx[1],2); t2=Fr(fx[7]-fx[3]); v10=t1+t2; assert (t1,t2,v10)==(Fr(11,2),11,Fr(33,2))
e10=[t1,t2,Fr(fx[5]-fx[1])+t2,2*(fx[5]-fx[1])+t2]
assert e10==[Fr(11,2),11,22,33] and len({v10,*e10})==5
SK10=tablo_svg(['x','1','3','5','7'],[['f(x)']+[str(fx[k]) for k in (1,3,5,7)]])
Q('0010','int-degisken','orta','f′ İçinde Doğrusal İfade','Türev fonksiyonunun içinde doğrusal ifade bulunan integrallerde değişken değiştirme ve temel teoremi tablo değerleriyle uygular.','tablo',
 'Gerçel sayılar kümesi üzerinde türevlenebilen ve f′ türev fonksiyonu sürekli olan bir f fonksiyonunun bazı değerleri aşağıdaki tabloda verilmiştir.\nBuna göre ∫₀² f′(2x + 1) dx + ∫₃⁷ f′(x) dx toplamı kaçtır?',
 v10,[(e10[0],'Yalnız birinci integrali hesaplayıp ikinciyi toplama katmamış.','dikkat'),(e10[1],'Yalnız ikinci integrali hesaplayıp birinciyi toplama katmamış.','dikkat'),(e10[2],'Birinci integralde u = 2x + 1 alırken 1/2 çarpanını yazmamış: f(5) − f(1) = 11.','bilgi'),(e10[3],'Birinci integralde dx = du/2 yerine dx = 2 du yazıp 2 ile çarpmış.','islem')],
 'İki integralin toplamı.',['f′ ve f arasındaki ilişkiyi kullan; birinci integralde içteki ifadeyi yeni bir değişken yap.'],[B_TAB,B_DEG],
 [A('Birinci integrali dönüştür','u = 2x + 1 için du = 2 dx; x = 0 iken u = 1, x = 2 iken u = 5.','∫₀² f′(2x + 1) dx = (1/2) ∫₁⁵ f′(u) du'),A('Temel teoremi uygula','f′’nin integrali f’nin değer farkıdır; değerler tablodan okunur.','(1/2) × (f(5) − f(1)) = (1/2) × (15 − 4) = 11/2'),A('İkinci integrali hesapla','Doğrudan f(7) − f(3) alınır.','20 − 9 = 11'),A('Topla','İki sonuç toplanır.','11/2 + 11 = 33/2')],
 'f′ içindeki ax + b için integralde 1/a çarpanını unutma.','K-AINT-06; f′(2x + 1) ve f′(x), değerler tabloda',sekil=SK10)

# ================= 11 orta · kemer (hikâyeli) =================
f11=4-x**2/4; v11=I(f11,-4,4); assert v11==Fr(64,3)
fiyat=150; m11=v11*fiyat; assert m11==3200
e11=[I(f11,0,4)*fiyat,Fr(1,2)*8*4*fiyat,Fr(8*4*fiyat),I(16-x**2,-4,4)*fiyat]
assert e11==[1600,2400,4800,12800] and len({m11,*e11})==5
sx,sy=0.72,0.75
b=[f'\\draw[gray!30,thin] ({-5*sx:.3f},0) -- ({5*sx:.3f},0);',
   f'\\fill[{MAVI},fill opacity=0.18] {pl("4-\\x*\\x/4",-4,4,sx,sy)} -- cycle;',
   egri('4-\\x*\\x/4',-4,4,sx,sy,MAVI,'2pt'),
   f'\\draw[-{{Stealth}},thick] ({-5*sx:.3f},0) -- ({5.3*sx:.3f},0) node[right] {{$x$ (m)}};',
   f'\\draw[-{{Stealth}},thick] (0,-0.2) -- (0,{5.2*sy:.3f}) node[above] {{$y$ (m)}};',
   nok(-4,0,sx,sy,0.07),nok(4,0,sx,sy,0.07),nok(0,4,sx,sy,0.07),
   f'\\node[below,font=\\small] at ({-4*sx:.3f},0) {{$-4$}};',f'\\node[below,font=\\small] at ({4*sx:.3f},0) {{$4$}};',
   f'\\node[above right,font=\\small] at (0,{4*sy:.3f}) {{$4$}};',f'\\node[below left,font=\\small] at (0,0) {{$O$}};']
SK11=fig('\n'.join(b))
Q('0011','int-uygulama','orta','Kemer Camı','Parabolik bir kesit için denklemi şekildeki noktalardan kurup alanı integralle bularak maliyeti hesaplar.','hikâyeli',
 'Bir yapı firması, bir giriş kapısının üst kısmını parabol biçimli kemer olarak tasarlıyor. Kemerin kesiti şekilde, ölçüleri metre olan bir dik koordinat sisteminde gösterilmiş; parabolün tepe noktası y ekseni üzerindedir ve parabol, zemin doğrusunu şekildeki iki noktada kesmektedir. Kemerin içi, metrekaresi 150 TL olan camla doldurulacaktır.\nBuna göre cam için toplam kaç TL ödenir?',
 m11,[(e11[0],'Yalnız yarım kemerin (x = 0 ile x = 4 arası) alanını hesaplayıp tam alanı bulmamış.','dikkat'),(e11[1],'Kemeri, tabanı 8 ve yüksekliği 4 olan bir üçgen sanmış: ½ × 8 × 4 × 150.','bilgi'),(e11[2],'Kemeri 8 × 4 boyutlu dikdörtgen sanmış.','bilgi'),(e11[3],'Parabolün denklemini y = 16 − x² almış (4’e bölmeyi unutmuş) ve alanı 256/3 bulmuş.','islem')],
 'Cam için ödenecek toplam tutar (TL).',['Parabolün denklemini, tepe noktası ve eksenle kesiştiği noktalardan yaz; sonra alanı integralle bul.'],[B_ALN,B_ANA],
 [A('Denklemi kur','Tepe (0, 4) ve kökler x = −4, x = 4 olduğundan y = a(x² − 16) biçimindedir; (0, 4) noktasından a bulunur.','4 = a × (−16) → a = −1/4 · y = 4 − x²/4'),A('Alanı integralle yaz','Kemerin alanı x ekseni ile parabol arasında kalan bölgedir.','A = ∫₋₄⁴ (4 − x²/4) dx'),A('Hesapla','Ters türev alınıp sınırlar yazılır.','[4x − x³/12]₋₄⁴ = (16 − 16/3) × 2 = 64/3'),A('Maliyeti bul','Alan, metrekare fiyatıyla çarpılır.','64/3 × 150 = 3200')],
 'Şekilden parabolün denklemini kur, alanı bulduktan sonra birim fiyatla çarp.','K-AINT-09; parabolik kemer kesiti, birim fiyat',sekil=SK11)

# ================= 12 orta · değişken değiştirme (düz) =================
f12=x*(x**2+3)**3; v12=I(f12,0,1); assert v12==Fr(175,8)
e12=[Fr(1,8),Fr(175,6),Fr(175,4),Fr(32)]
# 1/8 : sınırları değiştirmeden ½[u⁴/4] 0..1
assert Fr(str(sp.Rational(1,2)*(sp.Integer(1)**4/4-0)))==Fr(1,8)
assert Fr(1,2)*Fr(256-81,3)==Fr(175,6) and Fr(256-81,4)==Fr(175,4) and Fr(1,2)*Fr(4**4,4)==32
assert len({v12,*e12})==5
Q('0012','int-degisken','orta','Değişken Değiştirme','İçteki ifadeyi yeni değişken seçip sınırları dönüştürerek belirli integrali hesaplar.','düz',
 '∫₀¹ x · (x² + 3)³ dx\nintegralinin değeri kaçtır?',
 v12,[(e12[0],'u = x² + 3 alıp sınırları dönüştürmeden 0 ile 1’i u cinsinden integralde kullanmış: (1/2) × [u⁴/4]₀¹.','dikkat'),(e12[1],'u³’ün integralini u⁴/3 yazmış: (1/2) × (4⁴ − 3⁴)/3.','bilgi'),(e12[2],'x dx = du/2 çarpanını (1/2) yazmamış: (4⁴ − 3⁴)/4.','islem'),(e12[3],'Sınırları u = 0’dan u = 4’e almış: (1/2) × [u⁴/4]₀⁴.','dikkat')],
 'İntegralin değeri.',['Parantez içindeki ifadenin türevi, çarpan olarak integralde var mı? Yeni bir değişken tanımlayabilir misin?'],[B_DEG],
 [A('Değişkeni seç','İçteki ifade u alınır, türevi x dx ile ilişkilidir.','u = x² + 3 → du = 2x dx → x dx = du/2'),A('Sınırları dönüştür','x = 0 ve x = 1 değerleri u’da yerine yazılır.','x = 0 → u = 3 · x = 1 → u = 4'),A('İntegrali yaz','Yeni integral u’ya göre alınır.','(1/2) ∫₃⁴ u³ du = (1/2) × [u⁴/4]₃⁴'),A('Hesapla','Sınırlar yazılır.','(1/2) × (256 − 81)/4 = 175/8')],
 'Değişken değiştirince sınırları da yeni değişkene dönüştür.','K-AINT-06; x · (x² + 3)³ biçiminde integral')

# ================= 13 orta · öncüllü, integral özellikleri =================
fI=12; gI=5
r1=Fr(fI,2); r2=fI-2*gI; assert (r1,r2)==(6,2)
sira13=['Yalnız I','Yalnız III','I ve II','I ve III','I, II ve III']
Q('0013','int-ozellik','orta','Sınır ve Çarpan Özellikleri','Belirli integralin toplam, sabit çarpan ve f(mx) özelliklerini kullanarak verilen ifadelerin doğruluğunu belirler.','öncüllü',
 'Gerçel sayılar kümesi üzerinde sürekli f ve g fonksiyonları için\n∫₂⁶ f(x) dx = 12 ve ∫₂⁶ g(x) dx = 5\neşitlikleri veriliyor.\nI. ∫₁³ f(2x) dx = 6\nII. ∫₂⁶ (f(x) − 2g(x)) dx = 2\nIII. ∫₂⁶ f(x) · g(x) dx = 60\nifadelerinden hangileri kesinlikle doğrudur?',
 'I ve II',[('Yalnız I','II’de sabit çarpanı ve çıkarma özelliğini uygulamayı ihmal etmiş: 12 − 2 × 5 = 2 sonucuna varmamış.','islem'),('Yalnız III','Çarpımın integralini integrallerin çarpımı sanmış: 12 × 5 = 60.','bilgi'),('I ve III','II’yi yanlış sanıp III’ü doğru saymış; çarpımın integrali için böyle bir özellik yoktur.','bilgi'),('I, II ve III','Üç ifadeyi de doğru kabul etmiş; III’te integrallerin çarpımını çarpımın integraline eşit sanmış.','bilgi')],
 'Kesinlikle doğru olan ifadeler.',['f(2x) içeren integralde sınırların ve çarpanın nasıl değiştiğini düşün.'],[B_OZL,B_DEG],
 [A('I’i incele','u = 2x alınır; sınırlar 2 ve 6, çarpan 1/2 olur.','∫₁³ f(2x) dx = (1/2) ∫₂⁶ f(u) du = 6'),A('II’yi incele','Fark ve sabit çarpan integralin dışına alınır.','12 − 2 × 5 = 2'),A('III’ü incele','Çarpımın integrali integrallerin çarpımına eşit değildir; verilenlerle hesaplanamaz.','kesin değil'),A('Sonucu yaz','I ve II doğrudur.','I ve II')],
 'Verilenlerle hesaplanabilen ifadeleri ayır; hesaplanamayanı kesin sayma.','K-AINT-05; f(2x) ve doğrusal birleşim, çarpım tuzağı',sira=sira13)

# ================= 14 orta · kırık çizgi grafik, f(2x) =================
pts14=[(0,0),(2,4),(5,4),(6,0),(8,-4)]
T14=poly_alan(pts14); assert T14==14
v14=Fr(T14,2); assert v14==7
e14=[Fr(poly_mutlak(pts14,0,8),2),poly_integral(pts14,0,4),Fr(T14),Fr(2*T14)]
assert e14==[11,12,14,28] and len({v14,*e14})==5
sx,sy=0.62,0.42
b=[eks(0,8,-5,5,sx,sy,xt=[1,2,3,4,5,6,7,8],yt=[-4,-2,2,4],fs_='\\scriptsize'),
   pgol([(0,0),(2,4),(5,4),(6,0)],sx,sy,MAVI,0.25),pgol([(6,0),(8,-4)]+[(8,0)],sx,sy,TUR,0.3),
   poly(pts14,sx,sy,'black!70'),f'\\node[above,font=\\small] at ({2*sx:.3f},{4*sy:.3f}) {{$f$}};']
for p in pts14: b.append(nok(p[0],p[1],sx,sy,0.07))
SK14=fig('\n'.join(b))
Q('0014','int-degisken','orta','Grafikten f(2x) İntegrali','Doğru parçalarından oluşan f grafiğinden alanı hesaplayıp f(2x) içeren integrali değişken değiştirerek bulur.','grafik',
 'Şekilde, [0, 8] aralığında tanımlı ve sürekli bir f fonksiyonunun grafiği verilmiştir; grafik, köşeleri kılavuz çizgilerinin kesiştiği noktalarda olan doğru parçalarından oluşmaktadır.\nBuna göre ∫₀⁴ f(2x) dx integralinin değeri kaçtır?',
 v14,[(e14[0],'Alanları işaretine bakmadan toplamış (|f| alanı 22) ve 1/2 ile çarpmış.','dikkat'),(e14[1],'f(2x) yerine f(x) kabul edip ∫₀⁴ f(x) dx hesaplamış.','bilgi'),(e14[2],'u = 2x dönüşümündeki 1/2 çarpanını yazmamış: ∫₀⁸ f(u) du.','islem'),(e14[3],'1/2 yerine 2 ile çarpmış.','islem')],
 'İntegralin değeri.',['f(2x) içeren integrali f(x) cinsinden yazmanın bir yolu var mı? Grafiğin işaretli alanı gerekecek.'],[B_GRF,B_DEG],
 [A('Dönüşümü uygula','u = 2x alınır; du = 2 dx, sınırlar 0 ve 8 olur.','∫₀⁴ f(2x) dx = (1/2) ∫₀⁸ f(u) du'),A('Parçaları ayır','Grafik x ekseninin üstündeki ve altındaki şekillerden oluşur.','üçgen 4 · dikdörtgen 12 · üçgen 2 · alt üçgen −4'),A('İşaretli alanı topla','Eksenin altındaki alan negatif sayılır.','4 + 12 + 2 − 4 = 14'),A('Çarpanı uygula','İntegral, bulunan değerin yarısıdır.','(1/2) × 14 = 7')],
 'f(mx) integralinde sınırlar m katına çıkar, integral 1/m ile çarpılır.','K-AINT-06; kırık çizgi grafik, f(2x)',sekil=SK14)

# ================= 15 zor · y=12x−x² ve y=mx, alan oranı =================
m_=sp.symbols('m',positive=True)
top=I(12*x-x**2,0,12); assert top==288
c15=4; m15=12-c15
A1=lambda m:I((12-m)*x-x**2,0,12-m)  # = (12-m)^3/6
assert A1(m15)==Fr(32,3)==Fr(top,27)
sol=[s for s in sp.solve((12-m_)**3/sp.Integer(6)-sp.Rational(288,27),m_)]
assert sol==[8]
def A1c(c): return Fr(c**3,6)
e15=[4,6,3,10]
# 4: c'yi m diye almış; 6: oran 1/8 → c=6; 3: 12/4; 10: c = 6/3 = 2 → m = 12 − 2
assert A1c(6)==Fr(top,8) and 12-6==6 and Fr(12,4)==3 and 12-Fr(6,3)==10
assert len({m15,*e15})==5
sx,sy=0.36,0.105
b=[f'\\draw[-{{Stealth}},thick] (-0.3,0) -- ({13*sx:.3f},0) node[right] {{$x$}};',f'\\draw[-{{Stealth}},thick] (0,-0.2) -- (0,{38*sy:.3f}) node[above] {{$y$}};',
   f'\\fill[{MAVI},fill opacity=0.12] {pl("12*\\x-\\x*\\x",0,12,sx,sy)} -- cycle;',
   arag('12*\\x-\\x*\\x','6.5*\\x',0,5.5,sx,sy,TUR,0.38),
   egri('12*\\x-\\x*\\x',0,12,sx,sy,MAVI,'2pt'),egri('6.5*\\x',0,6.6,sx,sy,TUR,'2pt'),
   f'\\draw[thick] ({12*sx:.3f},-0.08) -- ({12*sx:.3f},0.08); \\node[below,font=\\small] at ({12*sx:.3f},-0.05) {{$12$}};',
   f'\\node[below left,font=\\small] at (0,0) {{$O$}};',
   f'\\node[above,font=\\small,{MAVI}] at ({6*sx:.3f},{36.5*sy:.3f}) {{$y=12x-x^2$}};',
   f'\\node[right,font=\\small,{TUR}] at ({6.7*sx:.3f},{43*sy:.3f}) {{$y=mx$}};']
SK15=fig('\n'.join(b))
Q('0015','int-iki-egri','zor','Doğru ile Bölünen Parabol Bölgesi','Parabol ile x ekseni arasındaki bölgeyi iki parçaya ayıran doğrunun eğimini, alan oranından belirler.','şekilli',
 '0 < m < 12 olmak üzere, dik koordinat düzleminde y = 12x − x² parabolü ile orijinden geçen y = mx doğrusu şekilde verilmiştir (şekil ölçekli değildir). Parabol ile x ekseni arasında kalan bölge mavi, parabol ile doğru arasında kalan bölge turuncu boyanmıştır.\nTuruncu bölgenin alanı, mavi bölgenin tamamının alanının 1/27’si olduğuna göre m kaçtır?',
 m15,[(e15[0],'Doğrunun parabolü kestiği noktanın apsisini (4) bulup bunu m sanmış.','dikkat'),(e15[1],'Alan oranını 1/8 almış: kesişim apsisini 6 bulup m = 6 yazmış.','dikkat'),(e15[2],'Kesişim apsisini 4 bulduktan sonra m = 12 − 4 yerine 12/4 hesaplamış.','islem'),(e15[3],'Parabolün yarı açıklığı olan 6’nın 1/3’ünü kesişim apsisi sanmış: 12 − 2.','bilgi')],
 'm’nin değeri.',['Önce mavi bölgenin tam alanını bul. Doğru ile parabol nerede kesişir ve turuncu alan bu kesişim apsisine nasıl bağlıdır?'],[B_IKI,B_ANA],
 [A('Toplam alanı bul','Parabol x eksenini 0 ve 12’de keser.','∫₀¹² (12x − x²) dx = 288'),A('Kesişimi m ile yaz','12x − x² = mx denkleminden kesişim apsisi c = 12 − m çıkar.','c = 12 − m'),A('Turuncu alanı yaz','Üst fonksiyon parabol, alt fonksiyon doğrudur.','∫₀ᶜ (c x − x²) dx = c³/6'),A('Oranı kur','c³/6 = 288/27 = 32/3 → c³ = 64','c = 4'),A('m’yi bul','Kesişim apsisinden m hesaplanır.','m = 12 − 4 = 8')],
 'Alan oranı verildiğinde alanı kesişim apsisine bağla ve küp köküyle çöz.','K-AINT-03; parabol ve orijinden geçen doğru, alan oranı 1/27',sekil=SK15)

# ================= 16 zor · f' grafiği, en büyük değer =================
pts16=[(0,0),(2,3),(4,0),(6,-2),(8,0)]
ar=[poly_integral(pts16,a,b) for a,b in ((0,4),(4,8))]; assert ar==[6,-4]
fmax=11; f0=fmax-6; f8=f0+sum(ar); assert (f0,f8)==(5,7)
assert poly_integral(pts16,0,8)==2
e16=[f0,fmax,13,15]
# 13: f(0)=11 (en büyük değeri başlangıçta sanmış) → f(8)=11+2; 15: negatif alanı da pozitif sayarak 11+4
assert 11+2==13 and 11+4==15
assert len({f8,*e16})==5
sx,sy=0.56,0.45
b=[eks(0,8,-3,4,sx,sy,xt=[1,2,3,4,5,6,7,8],yt=[-2,-1,1,2,3],yl="$y=f'(x)$",fs_='\\scriptsize'),
   pgol([(0,0),(2,3),(4,0)],sx,sy,MAVI,0.25),pgol([(4,0),(6,-2),(8,0)],sx,sy,TUR,0.3),poly(pts16,sx,sy,'black!70')]
for p in pts16: b.append(nok(p[0],p[1],sx,sy,0.07))
SK16=fig('\n'.join(b))
Q('0016','int-turev-iliski','zor','f′ Grafiği ve Ekstremum','Türev grafiğinin işaret değişiminden f’nin en büyük değerini kaydeden noktayı bulup alanlardan başka bir noktadaki değeri hesaplar.','grafik',
 'Şekilde, [0, 8] aralığında sürekli ve türevlenebilir bir f fonksiyonunun türevi olan f′ fonksiyonunun grafiği verilmiştir; grafik, köşeleri kılavuz çizgilerinin kesiştiği noktalarda olan doğru parçalarından oluşmaktadır. f fonksiyonunun [0, 8] aralığındaki en büyük değeri 11’dir.\nBuna göre f(8) değeri kaçtır?',
 f8,[(e16[0],'f(8) yerine başlangıç değeri olan f(0) = 5’i bulmuş.','dikkat'),(e16[1],'En büyük değeri f(8)’in kendisi sanmış.','bilgi'),(e16[2],'En büyük değerin f(0)’da olduğunu varsayıp tüm işaretli alanı eklemiş: 11 + 2.','bilgi'),(e16[3],'x ekseninin altındaki alanı da pozitif sayıp en büyük değere eklemiş: 11 + 4.','islem')],
 'f(8) değeri.',['f′’nin işareti nerede değişir? Bu noktada f ne olur ve işaretli alanlar f’deki değişimi nasıl verir?'],[B_INF,B_GRF],
 [A('Ekstremum noktasını bul','f′, x = 4’te + dan − ye geçtiğinden f, x = 4’te en büyük değerini alır.','f(4) = 11'),A('Alanı hesapla','[0, 4] aralığında f′ ile eksen arasındaki alan f’nin değişimidir.','f(4) − f(0) = 3 + 3 = 6 → f(0) = 5'),A('Negatif bölgeyi ekle','[4, 8] aralığında f′ negatif olduğundan f azalır.','f(8) − f(4) = −(2 + 2) = −4'),A('f(8)’i bul','En büyük değerden azalma çıkarılır.','f(8) = 11 − 4 = 7')],
 'f′ ile eksen arasındaki işaretli alan, f’nin değişimini verir; f′ işaret değiştirirse ekstremum oluşur.','K-AINT-07; f′ kırık çizgi grafiği, en büyük değer verili',sekil=SK16)

# ================= 17 zor · F(x)=∫f, öncüllü =================
pts17=[(0,0),(1,4),(2,0),(4,-3),(6,0),(7,3),(8,0)]
Fv={u:poly_integral(pts17,0,u) for u in (2,6,8)}; assert Fv=={2:4,6:-2,8:1}
assert Fv[6]<0 and Fv[8]>0 and Fv[2]>0
dogru17='II ve III'; sira17=['Yalnız II','Yalnız III','I ve II','II ve III','I, II ve III']
sx,sy=0.52,0.48
b=[eks(0,8,-4,5,sx,sy,xt=[1,2,3,4,5,6,7,8],yt=[-3,-2,-1,1,2,3,4],fs_='\\scriptsize',yl='$y=f(x)$'),
   pgol([(0,0),(1,4),(2,0)],sx,sy,MAVI,0.25),pgol([(2,0),(4,-3),(6,0)],sx,sy,TUR,0.3),pgol([(6,0),(7,3),(8,0)],sx,sy,YES,0.28),poly(pts17,sx,sy,'black!70')]
for p in pts17: b.append(nok(p[0],p[1],sx,sy,0.07))
SK17=fig('\n'.join(b))
Q('0017','int-turev-iliski','zor','İntegral Fonksiyonunun Davranışı','Grafiği verilen f için F(x) = ∫₀ˣ f(t) dt fonksiyonunun artanlık, yerel ekstremum ve değerlerini alan yorumlarıyla değerlendirir.','öncüllü',
 'Şekilde, [0, 8] aralığında sürekli bir f fonksiyonunun grafiği verilmiştir; grafik, köşeleri kılavuz çizgilerinin kesiştiği noktalarda olan doğru parçalarından oluşmaktadır. Bu aralıkta F(x) = ∫₀ˣ f(t) dt olarak tanımlanıyor.\nI. F(6) > F(0)\nII. F fonksiyonunun x = 2 noktasında yerel maksimumu vardır.\nIII. F(8) > 0\nifadelerinden hangileri doğrudur?',
 dogru17,[('Yalnız II','F(8) değerini hesaplarken yalnız ilk iki bölgeyi (4 − 6 = −2) toplamış, [6, 8] aralığındaki +3’ü eklememiş.','dikkat'),('Yalnız III','F(2) = 4 ve F(6) = −2 olduğunu görüp yerel maksimum yorumunu (II) yanlış sanmış.','bilgi'),('I ve II','F(6) değerini işaretli alanlarla değil yalnız ilk bölgenin alanıyla yorumlamış: 4 > 0.','dikkat'),('I, II ve III','F(6) değerini pozitif alanların toplamı sanmış; eksenin altındaki −6’yı hesaba katmamış.','dikkat')],
 'Doğru olan ifadeler.',['F′(x) = f(x) olduğundan F’nin işaret değişimlerine bak; F’nin değerlerini işaretli alanlardan bul.'],[B_INF,B_GRF],
 [A('Alanları hesapla','Her üçgenin alanı, ½ × taban × yükseklik ile bulunur; eksenin altındaki negatif sayılır.','[0, 2]: +4 · [2, 6]: −6 · [6, 8]: +3'),A('F değerlerini yaz','F(x) = ∫₀ˣ f(t) dt işaretli alanların birikimidir.','F(2) = 4 · F(6) = −2 · F(8) = 1'),A('I ve II’yi incele','F(6) = −2 < F(0) = 0 olduğundan I yanlış; f, x = 2’de + dan − ye geçtiğinden F orada yerel maksimum alır.','I yanlış · II doğru'),A('III’ü incele','F(8) = 1 > 0 olduğundan III doğrudur.','II ve III')],
 'F(x) = ∫ f(t) dt ise F′ = f’dir; F’nin değerlerini işaretli alanlardan topla.','K-AINT-07; F(x) = ∫₀ˣ f(t) dt, f kırık çizgi grafiği',sekil=SK17,sira=sira17)

# ================= 18 zor · integral denklemi =================
k=sp.symbols('k'); ks=sp.solve(sp.Eq(k,sp.integrate(t**2+k,(t,0,2))),k)
assert ks==[sp.Rational(-8,3)]
v18=Fr(9)+Fr(-8,3); assert v18==Fr(19,3)
e18=[Fr(9),Fr(9)+Fr(8,3),Fr(9)+Fr(8,9),Fr(-8,3)]
assert e18==[9,Fr(35,3),Fr(89,9),Fr(-8,3)] and len({v18,*e18})==5
Q('0018','int-denklem','orta','Kendi İntegralini İçeren Fonksiyon','f(x) = x² + (f’nin belirli integrali) biçimindeki denklemde sabit sayıyı bulup fonksiyonun değerini hesaplar.','düz',
 'Gerçel sayılar kümesi üzerinde sürekli bir f fonksiyonu, her x gerçel sayısı için\nf(x) = x² + ∫₀² f(t) dt\neşitliğini sağlıyor.\nBuna göre f(3) değeri kaçtır?',
 v18,[(e18[0],'Belirli integrali bir sayı olarak görmeyip f(3) için yalnız x² terimini almış.','dikkat'),(e18[1],'k = 8/3 + 2k denkleminde işareti yanlış çözüp k = 8/3 bulmuş: 9 + 8/3.','islem'),(e18[2],'k = 8/3 + 2k denklemini 3k = 8/3 diye düzenleyip k = 8/9 bulmuş.','islem'),(e18[3],'Sorunun f(3) değil de k sabitini istediğini sanıp k = −8/3 yazmış.','dikkat')],
 'f(3) değeri.',['İntegral işareti içindeki ifade bir sayıdır. Bu sayıya bir ad verip f’nin ifadesini o ad cinsinden yaz.'],[B_DEN,B_ANA],
 [A('Sayıya ad ver','Belirli integral bir sabittir; k denir.','k = ∫₀² f(t) dt → f(x) = x² + k'),A('Denklemi kur','f(t) = t² + k yazılıp integral alınır; k sabitinin integrali 0 ile 2 arasında 2k olur.','k = ∫₀² (t² + k) dt = 8/3 + 2k'),A('k’yı çöz','Denklem k için çözülür.','−k = 8/3 → k = −8/3'),A('f(3)’ü bul','k, f(x)’te yerine yazılır.','f(3) = 9 − 8/3 = 19/3')],
 'İntegral sınırları sabit ise integral bir sayıdır; ona ad verip denklemi o sayı için çöz.','K-AINT-08; f(x) = x² + ∫₀² f(t) dt')

# ================= 19 zor · F(x)=∫₂ˣ ..., yerel maksimum değeri =================
Fg=sp.integrate(t**2-4*t+3,(t,2,x)); Fd=sp.diff(Fg,x); assert sp.expand(Fd-(x**2-4*x+3))==0
kr=sp.solve(Fd,x); assert kr==[1,3]
Fmax=Fr(str(Fg.subs(x,1))); Fmin=Fr(str(Fg.subs(x,3))); assert (Fmax,Fmin)==(Fr(2,3),Fr(-2,3))
assert sp.diff(Fd,x).subs(x,1)<0 and sp.diff(Fd,x).subs(x,3)>0
Gt=t**3/3-2*t**2+3*t; e19=[Fmin,Fr(0),Fr(str(Gt.subs(t,1))),Fr(str(Gt.subs(t,3)-Gt.subs(t,1)))]
assert e19==[Fr(-2,3),0,Fr(4,3),Fr(-4,3)] and len({Fmax,*e19})==5
Q('0019','int-turev-iliski','orta','İntegral Fonksiyonunun Yerel Maksimumu','Üst sınırı değişken olan integral fonksiyonunun türevini alıp kritik noktaları ve yerel maksimum değerini bulur.','düz',
 'Gerçel sayılar kümesi üzerinde\nF(x) = ∫₂ˣ (t² − 4t + 3) dt\nfonksiyonu tanımlanıyor.\nBuna göre F fonksiyonunun yerel maksimum değeri kaçtır?',
 Fmax,[(e19[0],'Yerel maksimum ile yerel minimum noktalarını karıştırıp x = 3’teki değeri yazmış.','dikkat'),(e19[1],'Alt sınır 2 olduğundan F(2) = 0 değerini yerel maksimum sanmış.','bilgi'),(e19[2],'Ters türevi alıp x = 1’de değerlendirmiş ama alt sınır olan 2’deki değeri çıkarmayı unutmuş.','dikkat'),(e19[3],'Yerel minimum ile yerel maksimum değerinin farkını (F(3) − F(1)) hesaplamış.','dikkat')],
 'F’nin yerel maksimum değeri.',['F′(x) hangi fonksiyondur? Bu türevin işareti nerede + dan − ye geçer?'],[B_INF,B_ANA],
 [A('Türevi bul','Üst sınır x olduğundan F′ integrandın x’li halidir.','F′(x) = x² − 4x + 3 = (x − 1)(x − 3)'),A('İşareti incele','F′, x = 1’de + dan − ye, x = 3’te − den + ya geçer.','x = 1 yerel maksimum · x = 3 yerel minimum'),A('F(x)’i yaz','Ters türev alınıp 2’deki değer çıkarılır.','F(x) = x³/3 − 2x² + 3x − 2/3'),A('Değeri hesapla','Maksimum noktasında değer bulunur.','F(1) = 1/3 − 2 + 3 − 2/3 = 2/3')],
 'Üst sınırı x olan integralin türevi integrandın kendisidir; ekstremum değerinde alt sınırı unutma.','K-AINT-07; F(x) = ∫₂ˣ (t² − 4t + 3) dt')

# ================= 20 zor · bahçe, iki bölge, maliyet =================
f20=4*x-x**2; g20=x
Aust=I(f20-g20,0,3); Atum=I(f20,0,4); Aalt=Atum-Aust; assert (Aust,Atum,Aalt)==(Fr(9,2),Fr(32,3),Fr(37,6))
pr_u,pr_a=48,60
v20=Aust*pr_u+Aalt*pr_a; assert v20==586
e20=[I(f20-g20,0,4)*pr_u+(Atum-I(f20-g20,0,4))*pr_a, Atum*pr_a, I(f20,0,3)*pr_u+Aalt*pr_a, Atum*pr_a+Aust*pr_u]
sx,sy=1.25,0.95
b=[eks(0,5,0,5,sx,sy,xt=[1,2,3,4],yt=[1,2,3,4],xl='$x$ (m)',yl='$y$ (m)'),
   arag('4*\\x-\\x*\\x','\\x',0,3,sx,sy,MOR,0.32),
   f'\\fill[{YES},fill opacity=0.3] (0,0) -- ({3*sx:.3f},{3*sy:.3f}) -- {pl("4*\\x-\\x*\\x",3,4,sx,sy)} -- cycle;',
   egri('4*\\x-\\x*\\x',0,4,sx,sy,MAVI,'2pt'),f'\\draw[{TUR},line width=1.8pt] (0,0) -- ({3.6*sx:.3f},{3.6*sy:.3f});',
   nok(3,3,sx,sy,0.07),f'\\node[font=\\scriptsize] at ({1.15*sx:.3f},{2.65*sy:.3f}) {{lale}};',f'\\node[font=\\scriptsize] at ({3.2*sx:.3f},{1.0*sy:.3f}) {{sümbül}};',
   f'\\node[right,font=\\small,{MAVI}] at ({4.05*sx:.3f},{0.5*sy:.3f}) {{$y=4x-x^2$}};',f'\\node[above,font=\\small,{TUR}] at ({3.7*sx:.3f},{3.55*sy:.3f}) {{$y=x$}};']
SK20=fig('\n'.join(b))
Q('0020','int-uygulama','zor','Parkta Çiçek Bahçesi','Bir parabol ve bir doğruyla bölünen çiçek bahçesinin iki parçasının alanlarını integralle bulup fiyatlarla toplam bedeli hesaplar.','hikâyeli',
 'Bir belediye, parkın köşesindeki parabol biçimli çimlik alanı bir doğru ile ikiye ayırıp iki parçaya farklı çiçekler dikecektir. Şekilde, birimleri metre olan bir dik koordinat sisteminde alanın sınırları gösterilmiş; doğrunun üstünde kalan mor bölgeye lale, doğrunun altında kalan yeşil bölgeye sümbül dikilecektir. Dikim bedeli lale bölgesi için metrekare başına 48 TL, sümbül bölgesi için metrekare başına 60 TL’dir.\nBuna göre toplam dikim bedeli kaç TL’dir?',
 v20,[(e20[0],'Lale bölgesini hesaplarken integrali 3 yerine 4’e kadar almış (∫₀⁴ (3x − x²) dx); sümbül alanını da buna göre bulmuş.','islem'),(e20[1],'Parabolün altındaki tüm alanı (32/3) tek bölge sayıp 60 TL ile çarpmış.','bilgi'),(e20[2],'Lale bölgesi için doğruyu çıkarmadan parabolün x = 0 ile x = 3 arasındaki altında kalan alanı (9) almış.','dikkat'),(e20[3],'Sümbül bölgesi yerine parabolün altındaki tüm alanı 60 TL ile çarpıp lale bölgesini ayrıca eklemiş.','bilgi')],
 'Toplam dikim bedeli (TL).',['Parabol ile doğrunun kesişim noktasını bul. Sümbül bölgesinin sınırlarının x = 3’ten önce ve sonra farklı olduğuna dikkat et.'],[B_IKI,B_ALN],
 [A('Kesişimi bul','Parabol ve doğru eşitlenir.','4x − x² = x → x(3 − x) = 0 → x = 0, x = 3'),A('Lale alanı','Üstte parabol, altta doğru vardır.','∫₀³ (3x − x²) dx = 9/2'),A('Sümbül alanı','Parabolün altındaki tüm alandan lale alanı çıkarılır.','∫₀⁴ (4x − x²) dx − 9/2 = 32/3 − 9/2 = 37/6'),A('Bedeli hesapla','Her alan kendi fiyatıyla çarpılır.','9/2 × 48 + 37/6 × 60 = 216 + 370 = 586')],
 'Bir bölge iki parçaya bölünüyorsa toplam alandan bilinen parçayı çıkararak diğerini bul.','K-AINT-09; parabol ile doğru, iki fiyatlı bölge',sekil=SK20)

# ---------------- yaz ----------------
for q_ in P.ANA: q_['kardes']=None
from collections import Counter
tipler={}
for k_ in KART: tipler.setdefault(k_['tipId'],dict(tipId=k_['tipId'],ad=k_['tip'],kartlar=[],uygulamaKonu=UK))['kartlar'].append(k_['id'])
if len(P.ANA)==20:
    json.dump(P.ANA,open(os.path.join(HD,'integral-1.json'),'w'),ensure_ascii=False,indent=1)
    json.dump(dict(konu='İntegral',surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT Matematik 2018–2026 çıkmış soruları ve yayın soru bankaları (yalnız mantık), MEB 11–12. sınıf müfredatı.',kartlar=KART,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar','integral.json'),'w'),ensure_ascii=False,indent=1)
print(len(P.ANA),'soru · harfler',dict(sorted(Counter(q['cevap']['sik'] for q in P.ANA).items())),'· zorluk',dict(Counter(q['zorluk'] for q in P.ANA)),'· şekilli',sum(1 for q in P.ANA if q.get('sekil')),'· tip',len(tipler),'· kalıp',dict(Counter(q['kalip'] for q in P.ANA)))
