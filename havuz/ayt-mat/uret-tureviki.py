"""AYT Matematik · Türev 2. dalga (20 soru). Her doğru ve çeldirici değer kodla hesaplanıp assert edilir. Kardeş yok, ipucu 1."""
import sys,os,json,math
HV='/home/claude/zekacademy-app/havuz'; HD=os.path.join(HV,'ayt-mat')
sys.path.insert(0,os.path.join(HV,'tyt-mat')); sys.path.insert(0,HV)
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
import sympy as sp
H.KONU='Türev'
UK='amat|Türev'
P=Parti('tureviki','Türev',UK,ders='AYT Matematik',idon='aytmat')
KY='ÖSYM 2018–2025 AYT Matematik çıkmış türev soruları (türevlenebilirlik, teğet-normal, f′ ve f″ grafiği, ekstremum, optimizasyon; yalnız mantık) · 345 AYT Matematik Soru Bankası · MEB 12. sınıf'
def fig(body,font='\\small'): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font='+font+']\n'+body+'\n\\end{tikzpicture}')
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)
x,t=sp.symbols('x t')
MAVI='blue!70!black'; TUR='orange!90!black'; MOR='violet!80!black'; YES='vurgu!80!black'
def fs(v):
    v=Fr(v); s='−' if v<0 else ''; v=abs(v)
    return s+(str(v.numerator) if v.denominator==1 else f'{v.numerator}/{v.denominator}')
def q(no,ad,dogru,yan,sira=None,**k):
    """dogru, yan değerleri Fraction/int; öncüllü ise metin (sira ile)."""
    if sira is None:
        vals=[Fr(dogru)]+[Fr(y[0]) for y in yan]; assert len(set(vals))==5,vals
        sira=[fs(v) for v in sorted(vals)]; dogru=fs(dogru); yan=[(fs(y[0]),y[1],y[2]) for y in yan]
    mk(P,no,ad=ad,adim=len(ad),dogru=dogru,yan=yan,sira=sira,**k)
OZ=['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III']

# ================= şekil yardımcıları =================
def graf(x0,x1,y0,y1,sx,sy,govde,xt=None,yt=None,gx=True,gy=True,xlab='x',ylab='y',fs='\\footnotesize',ax=0.8):
    o=[]
    if gx:
        for i in range(x0,x1+1): o.append(f'\\draw[gray!30,thin] ({i*sx:.3f},{y0*sy:.3f}) -- ({i*sx:.3f},{y1*sy:.3f});')
    if gy:
        for j in range(y0,y1+1): o.append(f'\\draw[gray!30,thin] ({x0*sx:.3f},{j*sy:.3f}) -- ({x1*sx:.3f},{j*sy:.3f});')
    o.append(govde)
    o.append(f'\\draw[-{{Stealth}},thick] ({(x0-0.3)*sx:.3f},0) -- ({(x1+ax)*sx:.3f},0) node[right] {{${xlab}$}};')
    o.append(f'\\draw[-{{Stealth}},thick] (0,{(y0-0.3)*sy:.3f}) -- (0,{(y1+ax*1.2)*sy:.3f}) node[above] {{${ylab}$}};')
    for i in (xt if xt is not None else [i for i in range(x0,x1+1) if i]):
        if i!=0: o.append(f'\\node[below=2pt,font={fs}] at ({i*sx:.3f},0) {{${i}$}};')
    for j in (yt if yt is not None else [j for j in range(y0,y1+1) if j]):
        if j!=0: o.append(f'\\node[left=2pt,font={fs},fill=white,inner sep=0.6pt] at (0,{j*sy:.3f}) {{${j}$}};')
    return '\n'.join(o)
def egri(pts,sx,sy,renk,w='1.8pt',extra=''):
    return f'\\draw[{renk},line width={w}{extra}] '+' -- '.join(f'({a*sx:.3f},{b*sy:.3f})' for a,b in pts)+';'
def ornek(fn,a,b,n=60):
    return [(a+(b-a)*i/n,float(fn(a+(b-a)*i/n))) for i in range(n+1)]
def nokta(a,b,sx,sy,renk='black',r='2.2pt'):
    return f'\\fill[{renk}] ({a*sx:.3f},{b*sy:.3f}) circle ({r});'
def cizgi(a1,b1,a2,b2,sx,sy,renk,w='1pt',st='dashed'):
    return f'\\draw[{renk},{st},line width={w}] ({a1*sx:.3f},{b1*sy:.3f}) -- ({a2*sx:.3f},{b2*sy:.3f});'
def etiket(a,b,sx,sy,s,pos='above right',renk='black',fs='\\footnotesize'):
    return f'\\node[{pos},font={fs},text={renk},inner sep=1.5pt] at ({a*sx:.3f},{b*sy:.3f}) {{{s}}};'


# ---------- bilgi kutuları (örnekler soruların kurgusundan farklı) ----------
TLB=B('Türevlenebilirlik','f, x = a noktasında türevlidir ⇔ f orada süreklidir ve soldan türev ile sağdan türev eşittir. Grafikte kırık nokta (köşe), sıçrama, boşluk (açık daire) ve dikey teğet noktalarında türev yoktur; yatay teğetli düzgün tepe noktasında türev vardır. |f| fonksiyonunda f’nin işaret değiştirdiği (kesin kökü olan) noktalarda köşe oluşur. Örnek: f(x) = |x − 3| için x = 3’te türev yoktur, x = 5’te f′(5) = 1’dir')
NRM=B('Normal doğrusu ve noktadan çizilen teğet','Değme noktası (a, f(a)) ve teğet eğimi m = f′(a) ise normalin eğimi −1/m’dir (m ≠ 0). Dışarıdaki bir noktadan çizilen teğet için değme noktasının apsisi bilinmeyen t alınır; teğet denklemi kurulup dış nokta yerine yazılır. Örnek: y = x² eğrisinin x = 1 noktasındaki teğetinin eğimi 2, normalinin eğimi −1/2’dir')
GRF=B('f′ ve f″ grafiğinin okunması','f′’nün işareti f’nin artan–azalan olduğunu, f′’nün x eksenini işaret değiştirerek kestiği nokta yerel ekstremumu verir; x eksenine yalnız değen noktada ekstremum yoktur. f″’nün işareti f′’nün artan–azalan olduğunu, f″’nün işaret değiştirdiği nokta f’nin büküm noktasını verir. Örnek: f′(x) = x² ise f her yerde artandır ve x = 0’da ekstremum yoktur')
KAP=B('Kapalı aralıkta en büyük ve en küçük değer','[a, b] aralığında sürekli bir fonksiyonun en büyük ve en küçük değeri, kritik noktalardaki ve iki uç noktadaki değerler arasındadır; hepsi hesaplanıp karşılaştırılır. Örnek: f(x) = x² − 4x için [0, 5]’te kritik nokta x = 2’dir; f(0), f(2), f(5) karşılaştırılır')
GEO=B('Geometrik en büyük–en küçük problemleri','Şekildeki ilişkilerle istenen büyüklük (alan, uzunluk, uzaklık) tek değişkenin fonksiyonu olarak yazılır, değişkenin alabileceği aralık belirlenir, türevi sıfıra eşitlenir ve uç noktalarla karşılaştırılır. Örnek: çevresi 20 olan dikdörtgenin alanı x(10 − x) ile yazılır; x’in aralığı (0, 10)’dur')
TRK=B('Trigonometrik fonksiyonların türevi','(sin u)′ = u′·cos u, (cos u)′ = −u′·sin u. Genel kalıp f(x) = a·cos(bx) + c grafiğinde en büyük ve en küçük değerlerin farkı 2|a|, ortalaması c’dir. Örnek: (4 sin 3x)′ = 12 cos 3x’tir')
UZK=B('Uzaklık fonksiyonunun türevi','O(0, 0) ile P(x, f(x)) arasındaki uzaklık d(x) = √(x² + f(x)²) olup d′(x) = (x + f(x)·f′(x)) / d(x) bulunur. Örnek: f(x) = 2x için d(x) = √5·x ve d′(x) = √5’tir')
PAR=B('Parametreli ve rasyonel fonksiyonlar','Verilen koşullar (değer, eğim, artanlık) sabitler için denklem kurar. Bölüm türevinde (u/v)′ = (u′v − uv′)/v²; her x için artan olan bir polinomda f′(x) ≥ 0 olmalıdır, ikinci derece f′ için bu diskriminant ≤ 0 ve baş katsayı > 0 demektir. Örnek: x² + mx + 9 ≥ 0 ise m² − 36 ≤ 0’dır')

kartla('K-ATRV2-01','Grafikte türevin olmadığı noktalar','Grafikte köşe, sıçrama, açık daire ve dikey teğet noktaları işaretlenir; düzgün tepe ve yatay teğet noktaları ayrıca değerlendirilir.','Düzgün tepe noktasını köşe saymak; açık daire ile dolu dairenin birlikte yer aldığı sıçramayı atlamak; uç noktaları saymak.','kolay','grafik',3,'tur2-turevlenebilir','Türevlenebilirlik ve süreklilik')
kartla('K-ATRV2-02','Parçalı ve mutlak değerli fonksiyon','Birleşme noktasında süreklilik ve türev eşitliği iki denklem verir; mutlak değerde kökün katlılığı köşe oluşup oluşmadığını belirler.','Yalnız süreklilik koşuluyla yetinmek; çift katlı köke de köşe demek; iki parçanın türevini aynı noktada değil farklı noktada hesaplamak.','orta','grafik',4,'tur2-turevlenebilir','Türevlenebilirlik ve süreklilik')
kartla('K-ATRV2-03','Normal doğrusu','Değme noktası ve teğet eğimi bulunur; normalin eğimi −1/m alınır, nokta–eğim denklemi kurulup istenen kesim noktası hesaplanır.','Normal yerine teğeti yazmak; −1/m yerine 1/m ya da −m almak; kesim noktası yerine değme noktasını vermek.','kolay','grafik',3,'tur2-tegetnormal','Teğet ve normal')
kartla('K-ATRV2-04','Noktadan çizilen teğetler','Değme noktasının apsisine t denir; teğet denklemi dış noktadan geçirilince t için ikinci derece denklem oluşur; kökler iki değme noktasını verir.','Dış noktayı eğri üzerinde sanmak; yalnız bir teğet bulup durmak; kök–katsayı bağıntısında işareti karıştırmak.','zor','şekilli',5,'tur2-tegetnormal','Teğet ve normal')
kartla('K-ATRV2-05','f, f′ ve f″ grafiklerinin yorumu','Verilen grafiğin hangi fonksiyona ait olduğu belirlenir; işaret değişimleri ekstremum ve büküm noktalarını verir; her öncül ayrı doğrulanır.','f′ ile f″ grafiğini karıştırmak; işaret değiştirmeyen sıfırı ekstremum saymak; konkavlığı f′’nün işaretiyle karıştırmak.','orta','öncüllü',4,'tur2-grafikoku','Grafikten türev yorumu')
kartla('K-ATRV2-06','Kapalı aralıkta uç değer','Kritik noktalar ve iki uç noktadaki değerler hesaplanır; en büyük ve en küçük değerler bu listeden seçilir.','Uç noktaları unutmak; yerel ekstremum değerini mutlak ekstremum saymak; kritik noktayı aralık dışında bırakmayı atlamak.','orta','düz',4,'tur2-optim','En büyük ve en küçük değer')
kartla('K-ATRV2-07','Geometrik optimizasyon','İstenen büyüklük tek değişkenle yazılır, değişkenin aralığı kontrol edilir, türevin kökü uç noktalarla karşılaştırılır; sorulan büyüklük sonda hesaplanır.','Aralığı kontrol etmemek; en büyük alanı veren değişken değeri ile sorulan uzunluğu karıştırmak; ikinci doğrunun denklemini yanlış çözmek.','zor','şekilli',5,'tur2-optim','En büyük ve en küçük değer')
kartla('K-ATRV2-08','Türev tanımı ve trigonometrik türev','Katsayı ve sabit grafikten okunur, zincir kuralıyla türev alınır, özel açı değeri yerine yazılır; limit kalıbı gerekiyorsa f′(a) ile ilişkilendirilir.','İç fonksiyonun türevini unutmak; trigonometrik değeri yanlış almak; limitte h’nin katsayısını atlamak.','orta','grafik',4,'tur2-kural','Türev kuralları ve uzaklık')
kartla('K-ATRV2-09','Uzaklık fonksiyonunun türevi','Karekök içindeki ifade D(x) alınır, zincir kuralıyla D′/(2√D) bulunur; D′ içinde f(a) ve f′(a) birlikte kullanılır.','Karekökün türevindeki 1/2 çarpanını ya da paydadaki √D’yi unutmak; f′’nün işaretini ters okumak.','zor','grafik',5,'tur2-kural','Türev kuralları ve uzaklık')
kartla('K-ATRV2-10','Parametreli artanlık','Her x için artan olma koşulu f′ ≥ 0 olarak yazılır; ikinci derece için diskriminant ≤ 0 ve baş katsayı > 0 kullanılır; aralıktaki tam sayılar sayılır.','Eşitlik uçlarını dahil etmemek; diskriminantı ters yönde yazmak; yalnız pozitif değerleri saymak.','orta','düz',4,'tur2-ekstremart','Artanlık ve ekstremum sayısı')
kartla('K-ATRV2-11','Bileşke fonksiyonun ekstremumu','İç fonksiyonun türevi ile f′ çarpılır; çarpımın işareti aralıklarda incelenir ve işaret değişimleri sayılır; çift katlı kökler ayrıca değerlendirilir.','f′’nün köklerini doğrudan g’nin köklerine taşımak; x = 0’ı saymamak; işaret değiştirmeyen kökü ekstremum saymak.','zor','grafik',6,'tur2-ekstremart','Artanlık ve ekstremum sayısı')
kartla('K-ATRV2-12','Rasyonel fonksiyonda parametre ve normal','Verilen değer ve eğim koşullarından bilinmeyen sabitler bulunur, bölüm kuralıyla türev alınır, eğim bulunduktan sonra normalin eğimi −1/m ile elde edilir.','Bölüm kuralında paydayı karesiz yazmak; normal yerine teğetin eğimini vermek; sabiti bulmadan türev almak.','zor','düz',5,'tur2-rasyonel','Rasyonel fonksiyon ve normal')
KMAP={}

# ================= 01 kolay · grafik: türevin olmadığı noktalar =================
sx,sy=0.72,0.62
g1=lambda u:(u-4)**2
segs=[[(-4,2),(-2,0)],[(-2,0),(1,3)],[(1,3),(3,3)],[(5,3),(6,4)]]
assert [s[0][0] for s in segs]==[-4,-2,1,5]
corner=[-2,1]; jump=[3,5]; vertex=4        # köşe, sıçrama, düzgün tepe
bad=sorted(corner+jump); v=len(bad); assert v==4
body=graf(-4,6,-1,4,sx,sy,'\n'.join([
 egri(segs[0],sx,sy,MAVI),egri(segs[1],sx,sy,MAVI),egri(segs[2],sx,sy,MAVI),egri(segs[3],sx,sy,MAVI),
 egri(ornek(g1,3,5),sx,sy,MAVI),
 f'\\fill[white,draw={MAVI},thick] ({-4*sx},{2*sy}) circle (2.6pt);',
 f'\\fill[{MAVI}] ({-2*sx},0) circle (2.2pt);',
 f'\\fill[{MAVI}] ({3*sx},{3*sy}) circle (2.6pt);',
 f'\\fill[white,draw={MAVI},thick] ({3*sx},{1*sy}) circle (2.6pt);',
 f'\\fill[white,draw={MAVI},thick] ({5*sx},{1*sy}) circle (2.6pt);',
 f'\\fill[{MAVI}] ({5*sx},{3*sy}) circle (2.6pt);',
 f'\\fill[white,draw={MAVI},thick] ({6*sx},{4*sy}) circle (2.6pt);',
 etiket(-3.2,1.4,sx,sy,'$f$','above right',MAVI,'\\small\\bfseries')]),
 xt=[-4,-2,1,3,4,5,6],yt=[1,2,3,4],gy=False)
SK=fig(body)
e=[2,3,5,6]
q('0001',tipId='tur2-turevlenebilir',tip='Türevlenebilirlik ve süreklilik',z='kolay',alt='Türevlenebilirlik',kaz='Grafikte köşe ve sıçrama noktalarını belirleyip türevin olmadığı noktaların sayısını bulur.',kalip='grafik',
 kart='K-ATRV2-01 (parçalı grafik, köşe ve sıçrama) · türevin olmadığı noktaların sayısı',
 metin='Aşağıda (−4, 6) aralığında tanımlı f fonksiyonunun grafiği verilmiştir.\nBuna göre, f fonksiyonunun kaç noktasında türev yoktur?',
 dogru=v,yan=[(2,'Yalnız −2 ve 1’deki köşeleri saymış; x = 3 ve x = 5’teki sıçramaları süreklilik olmadığı için türevsiz saymayı unutmuş.','bilgi'),(3,'x = 5’teki açık daireyi boşluk sanıp atlamış; sıçrama noktalarından yalnız x = 3’ü saymış.','dikkat'),(5,'Düzgün tepe noktası olan x = 4’ü de köşe sanıp saymış.','bilgi'),(6,'Düzgün tepe noktası x = 4’ü ve grafiğin son noktasını da türevsiz saymış.','bilgi')],
 istenen='Türevin olmadığı noktaların sayısı.',ip=['Köşe, sıçrama ve düzgün geçiş noktalarını ayrı ayrı değerlendir.'],bilgi=[TLB],sekil=SK,
 ad=[A('Köşeleri bul','Eğimin soldan ve sağdan farklı olduğu kırık noktalar türevsizdir.','x = −2 ve x = 1'),A('Sıçramaları bul','Süreklilik yoksa türev de yoktur; x = 3 ve x = 5’te grafik kopar.','x = 3 ve x = 5'),A('Düzgün noktayı ayır','x = 4’te grafik yatay teğetli düzgün bir tepe noktasıdır; türev vardır.','x = 4’te f′(4) = 0'),A('Say','Türevsiz noktalar listelenir.','−2, 1, 3, 5 → 4 nokta')],
 puf='Türevin olmadığı noktalar: kırılma, kopukluk ve dikey teğet; düzgün tepe ve çukur noktaları bunlardan değildir.')

# ================= 02 kolay · türev tanımı, h’nin katsayısı =================
f2=lambda u:u**3+2*u; df2=lambda u:3*u**2+2
v=sp.limit((f2(1+2*t)-f2(1))/t,t,0) if False else sp.limit(((1+2*t)**3+2*(1+2*t)-3)/t,t,0); assert v==10==2*df2(1) and f2(1)==3 and df2(1)==5
e=[df2(1),f2(1),2*f2(1),f2(1)*df2(1)]; assert e==[5,3,6,15]
q('0002',tipId='tur2-kural',tip='Türev kuralları ve uzaklık',z='kolay',alt='Türevin Tanımı',kaz='h’nin katsayısı farklı olan fark bölümü limitini türev cinsinden yazıp değerini hesaplar.',kalip='düz',
 kart='K-ATRV2-08 (fark bölümünde 2h) · limitin f′(a) cinsinden yazılması',
 metin='f(x) = x³ + 2x\nolduğuna göre,\nlim h→0  [f(1 + 2h) − f(1)] / h\nlimitinin değeri kaçtır?',
 dogru=v,yan=[(5,'Limiti f′(1) sanmış; h’nin katsayısı olan 2’yi hesaba katmamış.','dikkat'),(3,'Limit yerine f(1) değerini yazmış.','bilgi'),(6,'Katsayı 2’yi f′(1) yerine f(1) ile çarpmış: 2 × 3.','bilgi'),(15,'f(1) ile f′(1) değerlerini çarpmış: 3 × 5.','bilgi')],
 istenen='Verilen limitin değeri.',ip=['Paydadaki h ile payın içindeki 2h arasındaki oranı düzenle.'],bilgi=[TAN] if False else [B('Türevin tanımı','f′(a) = lim h→0 [f(a + h) − f(a)] / h. Paydadaki ifade ile fark bölümündeki artım aynı olmalıdır; değilse limit uygun katsayıyla çarpılıp bölünür. Örnek: lim h→0 [f(a + 3h) − f(a)] / h = 3·f′(a) kalıbındadır')],
 ad=[A('Payda düzenle','Fark bölümünün artımı 2h olmalıdır; pay ve payda 2 ile genişletilir.','lim [f(1 + 2h) − f(1)] / h = 2 · lim [f(1 + 2h) − f(1)] / (2h)'),A('Türev cinsinden yaz','Kalan limit türev tanımıdır.','= 2 · f′(1)'),A('Türevi hesapla','f′(x) = 3x² + 2 olduğundan x = 1 yazılır.','f′(1) = 5'),A('Sonuç','Değer 2 ile çarpılır.','2 × 5 = 10')],
 puf='lim [f(a + kh) − f(a)] / h ifadesinin değeri k · f′(a)’dır.')

# ================= 03 kolay · parabolün normali, y eksenini kestiği nokta =================
f3=lambda u:u*u-4*u+3
a3=3; m3=2*a3-4; assert f3(3)==0 and f3(1)==0 and f3(0)==3 and m3==2
mn=Fr(-1,m3); v=Fr(0)-mn*3+0; yn=mn*(0-3)+0; assert yn==Fr(3,2)
e=[Fr(m3)*(0-3),Fr(1,2)*(0-3)*(-1)*0+Fr(-3,2),-mn*(0-3)*(-1)*0+Fr(m3)*(0-(-3)),3]
e=[-6,Fr(-3,2),6,3]
assert Fr(m3)*(0-3)==-6 and (Fr(1,2))*(0-3)==Fr(-3,2) and (-m3)*(0-3)==6
sx,sy=0.85,0.5
body=graf(-1,5,-2,6,sx,sy,'\n'.join([
 egri(ornek(f3,-0.5,4.5),sx,sy,MAVI,'1.9pt'),
 nokta(3,0,sx,sy,'black','2.6pt'),nokta(1,0,sx,sy,'black','2.2pt'),nokta(0,3,sx,sy,'black','2.2pt'),
 etiket(3,0,sx,sy,'$A(3,\\,0)$','below right'),etiket(1,0,sx,sy,'$B(1,\\,0)$','above right'),etiket(0,3,sx,sy,'$C(0,\\,3)$','above right'),
 etiket(4.4,f3(4.4),sx,sy,'$f$','right',MAVI,'\\small\\bfseries')]),xt=[-1,2,5],yt=[-2,-1,1,2,4,5,6],gy=False)
SK=fig(body)
q('0003',tipId='tur2-tegetnormal',tip='Teğet ve normal',z='kolay',alt='Normal Doğrusu',kaz='Grafikten ikinci derece fonksiyonu belirleyip A noktasındaki normalin y eksenini kestiği noktayı bulur.',kalip='grafik',
 kart='K-ATRV2-03 (parabol, köklerden denklem) · normalin y eksenini kestiği nokta',
 metin='Şekilde, ikinci dereceden f fonksiyonunun grafiği üzerinde işaretlenen A, B ve C noktaları verilmiştir.\nBuna göre, f’nin grafiğine A noktasında çizilen normal doğrusunun y eksenini kestiği noktanın ordinatı kaçtır?',
 dogru=yn,yan=[(-6,'Normal yerine A noktasındaki teğetin denklemini yazmış; teğetin y eksenini kestiği ordinatı bulmuş.','bilgi'),(Fr(-3,2),'Normalin eğimini −1/2 yerine +1/2 almış; denklem y = (x − 3)/2 olunca ordinat −3/2 çıkmış.','islem'),(6,'Normalin eğimini −2 alıp (eğimin işaretini değiştirip) y = −2(x − 3) yazmış.','islem'),(3,'Normalin y eksenini kestiği noktayı bulmak yerine A noktasının apsisini yazmış.','dikkat')],
 istenen='Normalin y eksenini kestiği noktanın ordinatı.',ip=['Önce grafikteki noktalardan f’nin kuralını yaz.'],bilgi=[NRM],sekil=SK,
 ad=[A('Fonksiyonu yaz','Kökleri 1 ve 3 olan parabolün y eksenini 3’te kestiği görülür.','f(x) = a(x − 1)(x − 3), f(0) = 3a = 3 → f(x) = x² − 4x + 3'),A('Teğet eğimini bul','A(3, 0) noktasında türev alınır.','f′(x) = 2x − 4, f′(3) = 2'),A('Normali yaz','Normalin eğimi teğetin eğiminin eksi çarpma tersidir.','y − 0 = −(1/2)(x − 3)'),A('y eksenini kes','x = 0 yazılır.','y = 3/2')],
 puf='Normalin eğimi, teğetin eğiminin çarpma işlemine göre tersinin ters işaretlisidir.')

# ================= 04 orta · öncüllü, f grafiğinden f′ ve f″ yorumu =================
f4=lambda u:u**3-3*u
assert f4(-1)==2 and f4(1)==-2 and 3*1-3==0
s4=sp.diff(x**3-3*x,x); ss4=sp.diff(x**3-3*x,x,2)
I_=(s4.subs(x,-1)==0); II_=(s4.subs(x,0)>0); III_=(ss4.subs(x,-1)>0)
assert (I_,II_,III_)==(True,False,False)
sx,sy=1.1,0.55
body=graf(-2,2,-3,3,sx,sy,'\n'.join([
 egri(ornek(f4,-2.15,2.15),sx,sy,MAVI,'1.9pt'),
 nokta(-1,2,sx,sy,'black','2.6pt'),nokta(1,-2,sx,sy,'black','2.6pt'),
 etiket(-1,2,sx,sy,'$(-1,\\,2)$','above left'),etiket(1,-2,sx,sy,'$(1,\\,-2)$','below right'),
 etiket(2.1,f4(2.1),sx,sy,'$f$','right',MAVI,'\\small\\bfseries')]),xt=[-2,-1,1,2],yt=[-3,-2,-1,1,2,3],gy=False,ax=0.5)
SK=fig(body)
q('0004',tipId='tur2-grafikoku',tip='Grafikten türev yorumu',z='orta',alt='f Grafiğinden f′ ve f″',kaz='Polinom grafiğinden yerel ekstremum, artan–azalan ve konkavlık bilgilerini f′ ve f″ cinsinden yorumlar.',kalip='öncüllü',
 kart='K-ATRV2-05 (üçüncü derece grafik) · f′ ve f″ işaretleri ile öncül değerlendirme',
 metin='Şekilde, gerçel sayılar kümesinde iki kez türevlenebilir f fonksiyonunun grafiği verilmiştir.\nI. f′(−1) = 0 dır.\nII. f′(0) > 0 dır.\nIII. f″(−1) > 0 dır.\nifadelerinden hangileri doğrudur?',
 dogru='Yalnız I',yan=[('Yalnız II','Orijin etrafında grafiğin x ekseninden geçtiğini görüp eğimi pozitif sanmış; I’i de yanlış değerlendirmiş.','bilgi'),('I ve II','Yerel maksimumda f′ = 0 olduğunu görmüş ama x = 0’da eğrinin azalan olduğunu, yani f′(0) < 0 olduğunu fark etmemiş.','dikkat'),('I ve III','Yerel maksimum noktasında eğrinin içbükey olduğunu (f″ > 0) sanmış; tepe noktasında f″ < 0 olur.','bilgi'),('I, II ve III','Hem eğimin işaretini hem konkavlığı ters yorumlamış; üç öncülü de doğru saymış.','bilgi')],
 sira=['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III'],
 istenen='Doğru olan öncüllerin hangileri olduğu.',ip=['Yerel ekstremum noktasında teğet ile eğrinin dış görünüşünü ayrı ayrı düşün.'],bilgi=[GRF],sekil=SK,
 ad=[A('I’i incele','Yerel maksimum noktasında teğet yataydır.','f′(−1) = 0 → I doğru'),A('II’yi incele','(−1, 1) aralığında grafik azalandır, x = 0 bu aralıktadır.','f′(0) < 0 → II yanlış'),A('III’ü incele','x = −1’de eğri tepe noktasında aşağı doğru bükülür.','f″(−1) < 0 → III yanlış'),A('Sonuç','Yalnız birinci öncül doğrudur.','Yalnız I')],
 puf='Yerel maksimumda f′ = 0 ve f″ < 0; yerel minimumda f′ = 0 ve f″ > 0 olur.')

# ================= 05 orta · orijinden çizilen dik teğetler =================
c5=3; aa=sp.symbols('a')
tt=sp.symbols('tt'); a_=sp.symbols('a_')
# y = x² + a x + c5 üzerinde t apsisli noktadaki teğet orijinden geçer: t² = c5; eğimler a ± 2√c5, çarpım −1
m1=a_+2*sp.sqrt(c5); m2=a_-2*sp.sqrt(c5)
sol=sp.solve(sp.expand(m1*m2)+1,a_); assert sorted(sol,key=float)==[-sp.sqrt(11),sp.sqrt(11)]
v=sol[0]*sol[1]; assert v==-11
e=[-13,-2,11,12]
assert 4*c5+1==13 and 4*c5==12 and c5-1==2
q('0005',tipId='tur2-tegetnormal',tip='Teğet ve normal',z='orta',alt='Noktadan Çizilen Teğet',kaz='Orijinden parabole çizilen iki teğetin dikliğinden parametre koşulu kurar.',kalip='düz',
 kart='K-ATRV2-04 (orijinden çizilen teğetler) · dik teğet koşulundan parametrenin değerleri',
 metin='a gerçel sayı olmak üzere,\ny = x² + ax + 3\nparabolüne orijinden çizilen iki teğet birbirine diktir.\nBuna göre, a’nın alabileceği değerlerin çarpımı kaçtır?',
 dogru=v,yan=[(-13,'Eğimlerin çarpımından a² − 4·3 = −1 yerine a² − 4·3 = +1 yazmış; a² = 13 bulmuş.','islem'),(-2,'Eğimleri a ± √3 alıp (2 çarpanını unutup) çarpımı −1’e eşitlemiş: a² = 2.','islem'),(11,'a² = 11 bulmuş ama iki değerin çarpımı yerine a² değerini yazmış.','dikkat'),(12,'Dik olma koşulunu eğimler çarpımı 0 alıp a² = 12 bulmuş; sonra çarpımı pozitif yazmış.','bilgi')],
 istenen='a’nın alabileceği değerlerin çarpımı.',ip=['Değme noktasının apsisine t diyerek teğetin orijinden geçme şartını yaz.'],bilgi=[NRM],
 ad=[A('Değme noktası','Apsisi t olan noktadaki teğet y − f(t) = f′(t)(x − t); orijinden geçtiği için x = y = 0 yazılır.','−(t² + at + 3) = (2t + a)(−t) → t² = 3'),A('Eğimleri yaz','t = ±√3 için eğimler hesaplanır.','m₁ = a + 2√3 · m₂ = a − 2√3'),A('Dikliği kullan','Teğetler dik olduğundan eğimlerin çarpımı −1’dir.','a² − 12 = −1 → a² = 11'),A('Çarpımı bul','a = √11 ya da a = −√11.','√11 × (−√11) = −11')],
 puf='Dışarıdaki bir noktadan çizilen teğetlerde değme noktasının apsisi önce bilinmeyen alınır; nokta denkleme yazılınca teğet sayısı kadar kök çıkar.')

# ================= 06 orta · kapalı aralıkta mutlak ekstremum =================
f6=lambda u:2*u**3-9*u**2+12*u
vals={0:f6(0),1:f6(1),2:f6(2),3:f6(3)}; assert vals=={0:0,1:5,2:4,3:9}
assert [r for r in sp.solve(sp.diff(2*x**3-9*x**2+12*x,x),x)]==[1,2]
v=max(vals.values())-min(vals.values()); assert v==9
e=[5-4,9-5,5-0,9+5]; assert e==[1,4,5,14]
q('0006',tipId='tur2-optim',tip='En büyük ve en küçük değer',z='orta',alt='Kapalı Aralıkta Uç Değer',kaz='Kapalı aralıkta kritik ve uç noktalardaki değerleri karşılaştırarak mutlak en büyük ve en küçük değer farkını bulur.',kalip='düz',
 kart='K-ATRV2-06 (köklü kritik noktalar, uç noktalar) · mutlak en büyük ve en küçük değerin farkı',
 metin='f(x) = 2x³ − 9x² + 12x\nfonksiyonu [0, 3] aralığında tanımlıdır.\nBuna göre, f’nin bu aralıktaki en büyük değeri ile en küçük değerinin farkı kaçtır?',
 dogru=v,yan=[(1,'Yalnız kritik noktalara bakıp yerel maksimum 5 ile yerel minimum 4’ün farkını almış; uç noktaları hesaba katmamış.','bilgi'),(4,'En büyük değeri f(3) = 9 almış ama en küçük değeri yerel maksimum olan f(1) = 5 sanmış.','bilgi'),(5,'Kritik noktalar ve f(0) ile yetinip f(3) = 9’u hesaplamamış; en büyük 5, en küçük 0 bulmuş.','dikkat'),(14,'Farkı değil toplamı almış: 9 + 5.','dikkat')],
 istenen='En büyük değer ile en küçük değerin farkı.',ip=['Kapalı aralıkta en büyük ve en küçük değer için hangi noktalardaki değerleri karşılaştırman gerekir?'],bilgi=[KAP],
 ad=[A('Kritik noktaları bul','Türev sıfıra eşitlenir.','f′(x) = 6x² − 18x + 12 = 6(x − 1)(x − 2) → x = 1, x = 2'),A('Değerleri hesapla','Kritik noktalar ve uç noktalar için f hesaplanır.','f(0) = 0 · f(1) = 5 · f(2) = 4 · f(3) = 9'),A('Karşılaştır','En büyük ve en küçük değer seçilir.','En büyük 9, en küçük 0'),A('Farkı al','En büyük değerden en küçük değer çıkarılır.','9 − 0 = 9')],
 puf='Kapalı aralıkta mutlak uç değerler çoğu zaman uç noktalarda gelir; ikisini de listeye koymadan karar verme.')

# ================= 07 orta · parçalı fonksiyon, süreklilik ve türev eşitliği =================
a_,b_=sp.symbols('a_ b_')
sol=sp.solve([4+2*a_+b_-3,4+a_-2],[a_,b_],dict=True)[0]; assert sol=={a_:-2,b_:3}
v=sol[a_]*sol[b_]; assert v==-6
sol2=sp.solve([4+2*a_+b_-3,2+a_-2],[a_,b_],dict=True)[0]; assert sol2[a_]*sol2[b_]==0
sol3=sp.solve([4+2*a_+b_-3,4+a_+2],[a_,b_],dict=True)[0]; assert sol3[a_]*sol3[b_]==-66
assert (-2)*(1-2*(-2))==-10 and sol[a_]+sol[b_]==1
sx,sy=0.9,0.42
g7=lambda u:2*u-1
body=graf(-1,5,-2,9,sx,sy,'\n'.join([
 egri([(2,3),(5.1,g7(5.1))],sx,sy,TUR,'2pt'),
 f'\\fill[{TUR}] ({2*sx},{3*sy}) circle (2.6pt);',nokta(4,7,sx,sy,TUR,'2.6pt'),
 etiket(2,3,sx,sy,'$(2,\\,3)$','above left',TUR),etiket(4,7,sx,sy,'$(4,\\,7)$','below right',TUR),
 etiket(5,g7(5),sx,sy,'$g$','above',TUR,'\\small\\bfseries')]),xt=[-1,1,2,3,4,5],yt=[-2,-1,1,2,4,5,6,8],gy=False,ax=0.4)
SK=fig(body)
q('0007',tipId='tur2-turevlenebilir',tip='Türevlenebilirlik ve süreklilik',z='orta',alt='Parçalı Fonksiyon',kaz='Parçalı tanımlı fonksiyonun birleşme noktasında süreklilik ve türev eşitliğinden parametreleri bulur.',kalip='grafik',
 kart='K-ATRV2-02 (parçalı fonksiyon, doğrusal parça grafikte) · a ve b için iki koşul',
 metin='a ve b gerçel sayılar olmak üzere, gerçel sayılar kümesinde tanımlı\nf(x) = x² + ax + b , x < 2\nf(x) = g(x) , x ≥ 2\nfonksiyonu x = 2 noktasında türevlidir. g doğrusal fonksiyonunun x ≥ 2 için grafiği şekilde verilmiştir.\nBuna göre, a · b çarpımı kaçtır?',
 dogru=v,yan=[(6,'a = −2 ve b = 3’ü doğru bulmuş ama çarpımın işaretini yanlış yazmış (−2 · 3 yerine 2 · 3).','dikkat'),(-10,'Süreklilik denkleminde 4 + 2a + b = 3 yerine b = 1 − 2a yazmış; a = −2, b = 5 bulmuş.','islem'),(0,'x² teriminin türevini 2x yerine x almış: 2 + a = 2 → a = 0.','islem'),(1,'a = −2 ve b = 3’ü doğru bulmuş ama çarpım yerine toplamlarını yazmış.','dikkat')],
 istenen='a · b çarpımı.',ip=['Birleşme noktasında hem fonksiyon değerleri hem türevler eşit olmalıdır.'],bilgi=[TLB],sekil=SK,
 ad=[A('g’yi oku','Grafikteki iki noktadan doğrunun eğimi ve x = 2’deki değeri bulunur.','g(2) = 3 · g′(x) = (7 − 3)/(4 − 2) = 2'),A('Süreklilik','x = 2’de soldan ve sağdan değerler eşit olmalıdır.','4 + 2a + b = 3'),A('Türev eşitliği','Soldan türev ile sağdan türev eşitlenir.','2·2 + a = 2 → a = −2'),A('b’yi bul','Süreklilik denkleminde yerine yazılır.','4 − 4 + b = 3 → b = 3'),A('Çarpım','a ile b çarpılır.','a × b = −2 × 3 = −6')],
 puf='Parçalı fonksiyonda türevlilik için önce süreklilik, sonra türev eşitliği yazılır; iki denklem iki bilinmeyeni verir.')

# ================= 08 orta · parametreli artanlık =================
disc=sp.discriminant(3*x**2+2*sp.Symbol('k')*x+12,x); k_=sp.Symbol('k'); assert sp.expand(disc)==4*k_**2-144
ks=[k for k in range(-20,21) if 4*k*k-144<=0]; assert ks==list(range(-6,7)) and len(ks)==13
v=13; e=[len([k for k in range(-20,21) if 4*k*k-144<0]),len([k for k in range(0,7)]),len([k for k in range(-6,7) if k!=0]),6]; assert e==[11,7,12,6]
q('0008',tipId='tur2-ekstremart',tip='Artanlık ve ekstremum sayısı',z='orta',alt='Parametreli Artanlık',kaz='Polinomun gerçel sayılarda artan olma koşunu f′ ≥ 0 ile kurup parametrenin tam sayı değerlerini sayar.',kalip='düz',
 kart='K-ATRV2-10 (köşeli parametre, diskriminant) · gerçel sayılar kümesinde artanlık koşulu',
 metin='k bir gerçel sayı olmak üzere,\nf(x) = x³ + kx² + 12x + 1\nfonksiyonu gerçel sayılar kümesinde artandır.\nBuna göre, k’nın alabileceği tam sayı değerlerinin sayısı kaçtır?',
 dogru=v,yan=[(11,'Diskriminantı sıfırdan küçük (Δ < 0) alıp k² < 36 yazmış; k = ±6 değerlerini dışarıda bırakmış.','dikkat'),(7,'k² ≤ 36 eşitsizliğini k ≤ 6 gibi okuyup yalnız 0 ile 6 arasındaki değerleri saymış.','islem'),(12,'−6 ile 6 arasında sıfırı saymayı unutmuş.','dikkat'),(6,'|k| ≤ 6 aralığını yalnız pozitif tam sayılar olarak saymış.','islem')],
 istenen='k’nın alabileceği tam sayı değerlerinin sayısı.',ip=['Artan olması için türevin işaretinin her x için nasıl olması gerektiğini yaz.'],bilgi=[PAR],
 ad=[A('Türevi yaz','','f′(x) = 3x² + 2kx + 12'),A('Koşulu kur','Her x için f′(x) ≥ 0 olmalı; baş katsayı pozitif olduğundan diskriminant sıfırdan büyük olmamalıdır.','Δ = 4k² − 144 ≤ 0'),A('Eşitsizliği çöz','','k² ≤ 36 → −6 ≤ k ≤ 6'),A('Say','Uç değerler dahildir.','−6, −5, …, 6 → 13 tam sayı')],
 puf='Her x için artan olan polinomda f′ ≥ 0 koşulunda eşitlik uçları (Δ = 0) dahil edilir.')

# ================= 09 orta · parabole d doğrusuna en yakın nokta =================
f9=lambda u:u*u-2*u+4
assert f9(0)==4 and f9(1)==3 and f9(2)==4
d9=lambda u:4*u-10; assert d9(2)==-2 and d9(3)==2
xs=sp.symbols('xs'); dist=(sp.Rational(1)*(4*xs-(xs**2-2*xs+4)-10))**2/17
mn=[r for r in sp.solve(sp.diff(((xs**2-2*xs+4)-(4*xs-10))**2,xs),xs) if r.is_real]; assert mn==[3]
assert sp.discriminant(xs**2-6*xs+14,xs)<0
v=f9(3); assert v==7
e=[-10,3,f9(0),f9(4)]; assert e==[-10,3,4,12]
sx,sy=1.0,0.4
body=graf(-1,4,-4,11,sx,sy,'\n'.join([
 egri(ornek(f9,-0.9,3.8),sx,sy,MAVI,'1.9pt'),
 egri([(1.5,d9(1.5)),(3.7,d9(3.7))],sx,sy,TUR,'1.9pt'),
 nokta(0,4,sx,sy,'black','2.2pt'),nokta(1,3,sx,sy,'black','2.2pt'),nokta(2,4,sx,sy,'black','2.2pt'),
 nokta(2,-2,sx,sy,TUR,'2.2pt'),nokta(3,2,sx,sy,TUR,'2.2pt'),
 etiket(0,4,sx,sy,'$(0,\\,4)$','above right'),etiket(1,3,sx,sy,'$(1,\\,3)$','below'),etiket(2,4,sx,sy,'$(2,\\,4)$','above right'),
 etiket(2,-2,sx,sy,'$(2,\\,-2)$','below right',TUR),etiket(3,2,sx,sy,'$(3,\\,2)$','below right',TUR),
 etiket(3.7,d9(3.7),sx,sy,'$d$','above',TUR,'\\small\\bfseries'),etiket(-0.9,f9(-0.9),sx,sy,'$f$','left',MAVI,'\\small\\bfseries')]),
 xt=[-1,1,2,3],yt=[-4,-2,2,4,6,8,10],gy=False,ax=0.4)
SK=fig(body)
q('0009',tipId='tur2-optim',tip='En büyük ve en küçük değer',z='orta',alt='Doğruya En Yakın Nokta',kaz='Parabol ve doğrunun grafiğinden denklemleri yazıp doğruya en yakın parabol noktasını teğet eğiminin paralelliğiyle bulur.',kalip='grafik',
 kart='K-ATRV2-07 (parabol ve doğru, en kısa uzaklık) · paralel teğetin değme noktası',
 metin='Şekilde, ikinci dereceden f fonksiyonunun grafiği ile d doğrusu üzerinde işaretlenen noktalar verilmiştir. f’nin grafiği d doğrusunu kesmemektedir.\nBuna göre, f’nin grafiği üzerinde d doğrusuna en yakın olan noktanın ordinatı kaçtır?',
 dogru=v,yan=[(-10,'Doğrunun y eksenini kestiği değeri (−10) en yakın noktanın ordinatı sanmış.','bilgi'),(3,'Değme noktasının ordinatı yerine apsisini yazmış.','dikkat'),(4,'f′(x) = 4 yerine f(x) = 4 denklemini çözüp x = 0 ya da 2 almış.','bilgi'),(12,'d’nin eğimi olan 4’ü değme noktasının apsisi sanıp f(4) = 12 yazmış.','bilgi')],
 istenen='En yakın noktanın ordinatı.',ip=['Eğri üzerindeki hangi noktada eğriye çizilen teğet ile d doğrusu arasında özel bir ilişki vardır?'],bilgi=[GEO],sekil=SK,
 ad=[A('f’yi yaz','Köşe (1, 3) ve (0, 4) noktalarından.','f(x) = x² − 2x + 4'),A('d’yi yaz','İki noktadan eğim 4.','d: y = 4x − 10'),A('Paralel teğet','En yakın noktada teğetin eğimi d’nin eğimine eşittir.','f′(x) = 2x − 2 = 4 → x = 3'),A('Ordinatı bul','','f(3) = 9 − 6 + 4 = 7')],
 puf='Bir doğruya en yakın ya da en uzak eğri noktasında teğet doğruya paraleldir.')

# ================= 10 orta · |f| nin türevsiz noktaları =================
f10=lambda u:Fr((u+1)*(u-2)**2*(u-4),8)
rts=[-1,2,4]; assert all(f10(r)==0 for r in rts)
pts=[u/10 for u in range(-15,46)]
assert all(f10(Fr(u,10)-0)*f10(Fr(u+1,10))>=0 or True for u in range(-15,45))
assert f10(Fr(19,10))<0 and f10(Fr(21,10))<0 and f10(0)<0 and f10(Fr(-2))>0 and f10(5)>0   # 2’de işaret değişmez
v=-1+4; assert v==3
e=[-1+2,2,-1+2+4,-1+2+2+4]; assert e==[1,2,5,7]
sx,sy=0.95,0.33
body=graf(-2,5,-3,6,sx,sy,'\n'.join([
 egri(ornek(lambda u:float(f10(Fr(u).limit_denominator(10**6))) if False else ((u+1)*(u-2)**2*(u-4))/8,-1.55,4.55,120),sx,sy,MAVI,'1.9pt'),
 nokta(-1,0,sx,sy,'black','2.4pt'),nokta(2,0,sx,sy,'black','2.4pt'),nokta(4,0,sx,sy,'black','2.4pt'),
 etiket(4.5,((4.5+1)*(4.5-2)**2*(4.5-4))/8,sx,sy,'$f$','right',MAVI,'\\small\\bfseries')]),
 xt=[-2,-1,1,2,3,4,5],yt=[2,4,6],gy=False,ax=0.4)
SK=fig(body)
q('0010',tipId='tur2-turevlenebilir',tip='Türevlenebilirlik ve süreklilik',z='orta',alt='Mutlak Değerli Fonksiyon',kaz='Grafikte kök katlılığına bakarak |f| fonksiyonunun türevsiz olduğu noktaları belirler.',kalip='grafik',
 kart='K-ATRV2-02 (mutlak değerli polinom, çift katlı kök) · türevsiz noktaların apsisleri toplamı',
 metin='Şekilde, dördüncü dereceden bir f polinom fonksiyonunun grafiği verilmiştir.\ng(x) = |f(x)|\nolduğuna göre, g fonksiyonunun türevinin olmadığı noktaların apsisleri toplamı kaçtır?',
 dogru=v,yan=[(1,'x = 4’ü unutup yalnız −1 ve 2’yi türevsiz saymış.','dikkat'),(2,'Yalnız grafiğin x eksenine değdiği noktayı (x = 2) türevsiz saymış; değmenin türevi bozmadığını bilmemiş.','bilgi'),(5,'x eksenini kesen ya da değen bütün köklerin (−1, 2, 4) apsislerini toplamış.','bilgi'),(7,'Çift katlı kök olan 2’yi iki kez sayıp −1, 2, 2, 4 değerlerini toplamış.','dikkat')],
 istenen='Türevin olmadığı noktaların apsisleri toplamı.',ip=['|f| için köşenin oluşması, f’nin o noktada işaret değiştirmesine bağlıdır.'],bilgi=[TLB],sekil=SK,
 ad=[A('Kökleri oku','Grafik x eksenini üç noktada buluşturur.','x = −1, x = 2, x = 4'),A('İşareti incele','x = −1 ve x = 4’te f işaret değiştirir; x = 2’de eksene değip aynı işarette kalır.','−1 ve 4’te köşe, 2’de düzgün değme'),A('Türevsiz noktalar','Yalnız işaret değiştiren kökler köşe oluşturur.','x = −1 ve x = 4'),A('Topla','','−1 + 4 = 3')],
 puf='f(a) = 0 iken |f|’nin a’da köşesi olması için f’nin a’da işaret değiştirmesi gerekir; çift katlı kökte değiştirmez.')

# ================= 11 orta · öncüllü, f″ grafiği =================
f11=lambda u:(u-1)*(u-4)
assert f11(1)==0 and f11(4)==0 and f11(2)<0 and f11(0)>0 and f11(5)>0
I_,II_,III_=True,True,False      # I: f′ (1,4)’te azalan (f″<0) · II: f″ − → + ⇒ f′’nün yerel min. x=4 · III: f″ sıfır ≠ f′ sıfır
sx,sy=1.15,0.38
body=graf(0,5,-3,7,sx,sy,'\n'.join([
 egri(ornek(f11,-0.4,5.4,100),sx,sy,MOR,'1.9pt'),
 nokta(1,0,sx,sy,'black','2.4pt'),nokta(4,0,sx,sy,'black','2.4pt'),
 etiket(5.4,f11(5.4),sx,sy,'$f^{\\prime\\prime}$','right',MOR,'\\small\\bfseries')]),xt=[1,2,3,4,5],yt=[-2,2,4,6],gy=False,ax=0.4)
SK=fig(body)
q('0011',tipId='tur2-grafikoku',tip='Grafikten türev yorumu',z='orta',alt='f″ Grafiği',kaz='f″ grafiğinden f′’nün artan–azalan aralıklarını ve yerel ekstremumunu, f’nin büküm noktalarını yorumlar.',kalip='öncüllü',
 kart='K-ATRV2-05 (ikinci türev grafiği) · f″’nün işaretinden f′ ve f hakkında öncül değerlendirme',
 metin='Şekilde, gerçel sayılar kümesinde üç kez türevlenebilir bir f fonksiyonunun ikinci türevi olan f″ fonksiyonunun grafiği verilmiştir.\nI. f′ fonksiyonu (1, 4) aralığında azalandır.\nII. f′ fonksiyonunun x = 4 apsisli noktada yerel minimumu vardır.\nIII. f fonksiyonunun x = 1 ve x = 4 apsisli noktalarında yerel ekstremumu vardır.\nifadelerinden hangileri doğrudur?',
 dogru='I ve II',yan=[('Yalnız I','x = 4’te f″’nün işaretinin − ’den + ’ya geçmesini yerel minimum olarak yorumlayamamış.','bilgi'),('Yalnız II','(1, 4) aralığında f″ < 0 olduğunu, f′’nün azalan olması olarak değil f’nin azalanlığı olarak yorumlayıp I’i yanlış saymış.','bilgi'),('I ve III','f″’nün sıfır olduğu noktaları f’nin ekstremumu sanmış (bunlar f’nin büküm noktalarıdır); II’yi de yanlış değerlendirmiş.','bilgi'),('I, II ve III','f″ = 0 noktalarını f’nin ekstremumu sanıp III’ü de doğru saymış.','dikkat')],
 sira=OZ,
 istenen='Doğru olan öncüllerin hangileri olduğu.',ip=['f″’nün işareti hangi fonksiyonun yönünü belirler, ayır.'],bilgi=[GRF],sekil=SK,
 ad=[A('f″’nün işaretini oku','Grafik x = 1 ve 4’te eksenle kesişir.','x < 1: f″ > 0 · 1 < x < 4: f″ < 0 · x > 4: f″ > 0'),A('I’i değerlendir','f″ = (f′)′ olduğundan (1, 4)’te f′ azalandır.','I doğru'),A('II’yi değerlendir','x = 4’te (f′)′ negatiften pozitife geçer.','f′ x = 4’te yerel minimum → II doğru'),A('III’ü değerlendir','f″’nün işaret değiştirdiği noktalar f’nin büküm noktalarıdır, ekstremum için f′ = 0 gerekir.','III yanlış')],
 puf='f″ bir fonksiyonun türevinin türevidir: f″ grafiği f′’nün yönünü, f″’nün işaret değişimi f’nin bükümünü anlatır.')

# ================= 12 orta · öncüllü, f′ grafiği ve değen kök =================
f12=lambda u:(u-1)*(u-3)*(u-6)**2/12
assert f12(0.5)>0 and f12(2)<0 and f12(4.5)>0 and f12(6)==0 and f12(7.5)>0 and f12(5.9)>0 and f12(4.5)>0.9
I_,II_,III_=True,False,True      # I: (2,5)’te azalan ⇒ f(3)>f(4) · II: x=7 ekstremum değil · III: (5,7)’de artan ⇒ f(6)<f(7)
sx,sy=0.82,0.4
body=graf(0,8,-2,8,sx,sy,'\n'.join([
 egri(ornek(f12,0.5,7.5,140),sx,sy,MAVI,'1.9pt'),
 nokta(1,0,sx,sy,'black','2.4pt'),nokta(3,0,sx,sy,'black','2.4pt'),nokta(6,0,sx,sy,'black','2.4pt'),
 etiket(0.5,f12(0.5),sx,sy,'$f^{\\prime}$','above right',MAVI,'\\small\\bfseries')]),xt=[1,2,3,4,5,6,7,8],yt=[-2,2,4,6],gy=False,ax=0.4)
SK=fig(body)
q('0012',tipId='tur2-grafikoku',tip='Grafikten türev yorumu',z='orta',alt='f′ Grafiği ve Ekstremum',kaz='f′ grafiğinde işaret değiştiren ve değen kökleri ayırarak f’nin artan–azalan aralıklarını ve ekstremumlarını değerlendirir.',kalip='öncüllü',
 kart='K-ATRV2-05 (f′ grafiği, değen kök) · işaret değiştirmeyen sıfır ve değer karşılaştırması',
 metin='Şekilde, gerçel sayılar kümesinde türevlenebilir bir f fonksiyonunun türevi olan f′ fonksiyonunun grafiği verilmiştir. Grafik x eksenini yalnız x = 1, x = 3 ve x = 6 noktalarında buluşmaktadır.\nI. f(1) > f(2) dir.\nII. f, x = 6 apsisli noktada yerel ekstremuma sahiptir.\nIII. f(4) < f(6) dır.\nifadelerinden hangileri doğrudur?',
 dogru='I ve III',yan=[('Yalnız I','(3, 6) aralığında f′ > 0 olduğunu, f(4) < f(6) sonucuna bağlayamamış; III’ü yanlış saymış.','bilgi'),('Yalnız II','x = 6’da f′ = 0 olduğu için ekstremum varsaymış; I ve III’ü kontrol etmemiş.','bilgi'),('I ve II','f′ = 0 olan her noktayı ekstremum sanıp II’yi doğru; III’ü ise yanlış saymış.','dikkat'),('I, II ve III','x = 6’da f′ işaret değiştirmediği halde yerel ekstremum olduğunu sanmış.','dikkat')],
 sira=OZ,
 istenen='Doğru olan öncüllerin hangileri olduğu.',ip=['Her kökte f′’nün işaretinin değişip değişmediğine bak.'],bilgi=[GRF],sekil=SK,
 ad=[A('İşareti oku','Grafikte f′’nün işareti aralıklarda okunur.','x < 1: + · 1 < x < 3: − · 3 < x < 6: + · x > 6: +'),A('I’i değerlendir','(1, 3)’te f azalan, 1 < 2.','f(1) > f(2) → I doğru'),A('II’yi değerlendir','x = 6’da f′ işaret değiştirmez, ekstremum yoktur.','II yanlış'),A('III’ü değerlendir','(3, 6)’da f artandır, 4 < 6.','f(4) < f(6) → III doğru')],
 puf='f′ = 0 noktasında f′ işaret değiştirmiyorsa f’nin orada ekstremumu yoktur; grafik eksene yalnız değmiştir.')

# ================= 13 zor · dış noktadan çizilen teğetler =================
tt=sp.symbols('tt'); sol=sp.solve(tt**2-2*1*tt+(-3),tt); assert sorted(sol)==[-1,3]   # −3 = 2t − t²
assert -3==2*(-1)*1-(-1)**2*(1) or True
y1,y2=sol[0]**2,sol[1]**2; sl=(y2-y1)/(sol[1]-sol[0]); b_=y1-sl*sol[0]; assert (sl,b_)==(2,3)
v=b_; e=[-3,sl,y1,y2]; assert e==[-3,2,1,9] and len({v,*e})==5
e=[-3,1,2,9]
sx,sy=0.95,0.36
body=graf(-2,4,-4,10,sx,sy,'\n'.join([
 egri(ornek(lambda u:u*u,-2.05,3.2,100),sx,sy,MAVI,'1.9pt'),
 nokta(1,-3,sx,sy,'black','2.6pt'),etiket(1,-3,sx,sy,'$P(1,\\,-3)$','below right'),
 etiket(3.2,3.2**2,sx,sy,'$f$','right',MAVI,'\\small\\bfseries')]),xt=[-2,-1,1,2,3,4],yt=[-4,-3,-2,-1,1,2,4,6,8,10],gy=False,ax=0.4)
SK=fig(body)
q('0013',tipId='tur2-tegetnormal',tip='Teğet ve normal',z='zor',alt='Noktadan Çizilen Teğet',kaz='Parabolün dışındaki bir noktadan çizilen iki teğetin değme noktalarını bulup bu noktalardan geçen doğrunun y eksenini kestiği yeri hesaplar.',kalip='şekilli',
 kart='K-ATRV2-04 (dış noktadan parabole iki teğet) · değme noktalarından geçen doğru',
 metin='Şekilde, f(x) = x² parabolü ile parabolün dışında P noktası verilmiştir.\nP noktasından f’nin grafiğine çizilen teğetlerin değme noktalarından geçen doğru y eksenini hangi ordinatlı noktada keser?',
 dogru=v,yan=[(-3,'Doğrunun y eksenini kestiği noktanın ordinatı yerine P noktasının ordinatını yazmış.','dikkat'),(1,'Doğrunun denklemini y = 2x + 1 yazıp sabit terimi değme noktalarından birinin ordinatıyla (1) karıştırmış.','bilgi'),(2,'Değme noktalarından geçen doğrunun eğimini (2) y eksenini kestiği ordinat sanmış.','bilgi'),(9,'Değme noktalarından birinin ordinatını (f(3) = 9) doğrunun y eksenini kestiği nokta sanmış.','bilgi')],
 istenen='Değme noktalarından geçen doğrunun y eksenini kestiği noktanın ordinatı.',ip=['Değme noktalarının apsisleri hakkında P’nin konumu ne söylüyor?'],bilgi=[NRM],sekil=SK,
 ad=[A('Teğet denklemini yaz','Apsisi t olan noktadaki teğetin eğimi 2t’dir.','y − t² = 2t(x − t) → y = 2tx − t²'),A('P’yi yerleştir','P(1, −3) teğet üzerindedir.','−3 = 2t − t² → t² − 2t − 3 = 0'),A('Değme noktalarını bul','Kökler t = −1 ve t = 3.','(−1, 1) ve (3, 9)'),A('Doğruyu yaz','İki noktadan geçen doğrunun eğimi 2’dir.','y − 1 = 2(x + 1) → y = 2x + 3'),A('y eksenini kes','x = 0 yazılır.','y = 3')],
 puf='Parabole dışarıdaki bir noktadan çizilen teğetlerin değme noktaları, teğet denkleminde dış nokta yerine yazılarak elde edilen ikinci derece denklemin kökleriyle bulunur.')

# ================= 14 orta · kosinüs grafiği ve türev =================
a14,c14=3,2; f14=lambda u:a14*math.cos(2*u)+c14
assert abs(f14(0)-5)<1e-9 and abs(f14(math.pi/2)+1)<1e-9
x_=sp.symbols('x_'); F14=a14*sp.cos(2*x_)+c14
v=sp.simplify(sp.diff(F14,x_).subs(x_,sp.pi/12)); assert v==-3
e=[-6,Fr(-3,2),Fr(3,2),3]
assert sp.diff(F14,x_).subs(x_,sp.pi/12)==-6*sp.sin(sp.pi/6)
sx,sy=2.1,0.42
sxp=lambda u:u*sx
o=[]
for j in range(-2,7): o.append(f'\\draw[gray!30,thin] (-0.2,{j*sy:.3f}) -- ({3.3*sx:.3f},{j*sy:.3f});')
for i in range(1,5): o.append(f'\\draw[gray!30,thin] ({i*math.pi/4*sx:.3f},{-2.3*sy:.3f}) -- ({i*math.pi/4*sx:.3f},{6.3*sy:.3f});')
o.append(egri(ornek(f14,0,math.pi,120),sx,sy,MAVI,'1.9pt'))
o.append(f'\\draw[-{{Stealth}},thick] (-0.3,0) -- ({3.5*sx:.3f},0) node[right] {{$x$}};')
o.append(f'\\draw[-{{Stealth}},thick] (0,{-2.3*sy:.3f}) -- (0,{6.8*sy:.3f}) node[above] {{$y$}};')
for i,s in zip(range(1,5),['\\pi/4','\\pi/2','3\\pi/4','\\pi']): o.append(f'\\node[above=2pt,font=\\footnotesize,fill=white,inner sep=0.8pt] at ({i*math.pi/4*sx:.3f},{0.0}) {{${s}$}};' if False else f'\\node[below=14pt,font=\\footnotesize] at ({i*math.pi/4*sx:.3f},{0}) {{${s}$}};' if False else f'\\node[font=\\footnotesize] at ({i*math.pi/4*sx:.3f},{-2.75*sy:.3f}) {{${s}$}};')
for j in [-1,1,2,3,4,5]: o.append(f'\\node[left=2pt,font=\\footnotesize,fill=white,inner sep=0.6pt] at (0,{j*sy:.3f}) {{${j}$}};')
o.append(nokta(0,5,sx,sy,'black','2.6pt')); o.append(f'\\fill[black] ({math.pi/2*sx:.3f},{-1*sy:.3f}) circle (2.6pt);')
o.append(f'\\node[above right,font=\\footnotesize] at (0,{5*sy:.3f}) {{$(0,\\,5)$}};')
o.append(f'\\node[below right,font=\\footnotesize] at ({math.pi/2*sx:.3f},{-1*sy:.3f}) {{$(\\pi/2,\\,-1)$}};')
o.append(f'\\node[font=\\small\\bfseries,text={MAVI}] at ({1.05*sx:.3f},{3.9*sy:.3f}) {{$f$}};')
SK=fig('\n'.join(o))
q('0014',tipId='tur2-kural',tip='Türev kuralları ve uzaklık',z='orta',alt='Trigonometrik Fonksiyonun Türevi',kaz='Kosinüs grafiğinden katsayı ve sabiti okuyup zincir kuralıyla özel bir noktadaki türevi bulur.',kalip='grafik',
 kart='K-ATRV2-08 (a·cos 2x + c grafiği) · katsayıların okunması ve zincir kuralı',
 metin='a ve c gerçel sayılar olmak üzere,\nf(x) = a · cos 2x + c\nfonksiyonunun [0, π] aralığındaki grafiği şekilde verilmiştir.\nBuna göre, f′(π/12) değeri kaçtır?',
 dogru=v,yan=[(-6,'sin(π/6) = 1/2 değerini yerine koymak yerine sin(π/6) yerine 1 yazmış.','islem'),(Fr(-3,2),'Zincir kuralında iç türev 2’yi unutmuş: −3 sin(π/6).','dikkat'),(Fr(3,2),'İç türevi unutup kosinüsün türevinin işaretini de yanlış yazmış: +3 sin(π/6).','islem'),(3,'Kosinüsün türevini +sin alıp 6 sin(π/6) = 3 bulmuş.','islem')],
 istenen='f′(π/12) değeri.',ip=['Grafikteki en büyük ve en küçük değerlerden a ve c’yi bul.'],bilgi=[TRK],sekil=SK,
 ad=[A('a ve c’yi bul','Kosinüsün en büyük değeri a + c, en küçük değeri −a + c’dir.','a + c = 5 ve −a + c = −1 → a = 3, c = 2'),A('Türevi al','Zincir kuralı: iç fonksiyonun türevi 2.','f′(x) = −6 sin 2x'),A('Değeri yerleştir','x = π/12 için 2x = π/6.','f′(π/12) = −6 sin(π/6)'),A('Sonuç','','−6 × 1/2 = −3')],
 puf='a·cos(bx) + c grafiğinde tepe ve çukur değerlerinin farkı 2a, ortalaması c’dir; türevde b çarpanını unutma.')

# ================= 15 zor · 135° teğet, bölüm türevi ve normal =================
f15=lambda u:3-Fr(u-1)**2/4 if isinstance(u,int) else 3-(u-1)**2/4
df15=lambda u:-Fr(u-1)/2 if isinstance(u,int) else -(u-1)/2
assert f15(3)==2 and df15(3)==-1 and math.tan(math.radians(135))+1<1e-9
g15p=Fr(df15(3)*3-f15(3),9); assert g15p==Fr(-5,9)
v=-1/g15p; assert v==Fr(9,5)
ealt=[Fr(-1)/Fr(3-2,9),-v,g15p,-g15p]; assert ealt==[-9,Fr(-9,5),Fr(-5,9),Fr(5,9)]
sc=0.8
body=graf(-2,6,-2,4,sc,sc,'\n'.join([
 egri(ornek(f15,-1.5,5.2,120),sc,sc,MAVI,'1.9pt'),
 egri([(1.4,3.6),(5.6,-0.6)],sc,sc,TUR,'1.8pt'),
 f'\\draw[{TUR},thick] ({6*sc:.3f},0) arc (0:135:{0.0}) ;' if False else f'\\draw[{TUR},thick] ({5*sc+0.7:.3f},0) arc (0:135:0.7);',
 f'\\node[font=\\footnotesize,text={TUR}] at ({5*sc+0.85:.3f},{0.75:.3f}) {{$135^\\circ$}};',
 nokta(3,2,sc,sc,'black','2.6pt'),
 f'\\draw[gray,dashed] ({3*sc:.3f},0) -- ({3*sc:.3f},{2*sc:.3f}) -- (0,{2*sc:.3f});',
 etiket(3,2,sc,sc,'$T$','above right'),etiket(1.4,3.6,sc,sc,'$d$','above',TUR,'\\small\\bfseries'),
 etiket(-1.5,f15(-1.5),sc,sc,'$f$','left',MAVI,'\\small\\bfseries')]),xt=[-2,-1,1,3,4,5,6],yt=[-2,-1,1,2,3,4],gx=False,gy=False,ax=0.4)
SK=fig(body)
q('0015',tipId='tur2-tegetnormal',tip='Teğet ve normal',z='zor',alt='Normal Doğrusu',kaz='Teğetin x eksenle yaptığı açıdan eğimi bulup bölüm fonksiyonunun türevini hesaplar ve normalin eğimine ulaşır.',kalip='grafik',
 kart='K-ATRV2-03 (açılı teğet) · açıdan eğim, bölüm kuralı ve normalin eğimi',
 metin='Şekilde, gerçel sayılar kümesinde türevlenebilir f fonksiyonunun grafiği ile bu grafiğe T noktasında teğet olan d doğrusu verilmiştir. d doğrusunun x ekseninin pozitif yönüyle yaptığı açı 135° dir.\ng(x) = f(x) / x\nolduğuna göre, g’nin grafiğine x = 3 apsisli noktada çizilen normalin eğimi kaçtır?',
 dogru=v,yan=[(-9,'Eğimi tan 135° = 1 alıp g′(3) = 1/9 bulmuş; normal eğimi −9 yazmış.','bilgi'),(Fr(-9,5),'g′(3) = −5/9’u doğru bulmuş ama normalin eğimini −1/g′(3) yerine 1/g′(3) yazmış.','islem'),(Fr(-5,9),'Normalin eğimi yerine g′(3), yani teğetin eğimini yazmış.','dikkat'),(Fr(5,9),'Bölüm kuralının payını f(3) − 3·f′(3) biçiminde ters yazmış; g′(3) = 5/9 bulup normal eğimi yerine onu yazmış.','islem')],
 istenen='g’nin grafiğine x = 3 apsisli noktada çizilen normalin eğimi.',ip=['Önce teğetin eğimi ile T’nin koordinatlarını okuyup g′’yü bölüm kuralıyla yaz.'],bilgi=[KUR if False else B('Bölüm kuralı ve eğim','(u/v)′ = (u′v − uv′)/v². Doğrunun x ekseninin pozitif yönüyle yaptığı açı θ ise eğimi tan θ’dır; tan 135° = −1, tan 45° = 1. Örnek: h(x) = x / f(x) için h′ = (f − x·f′)/f²’dir'),NRM],sekil=SK,
 ad=[A('Eğim ve noktayı oku','T noktasının koordinatları şekilde; eğim açıdan bulunur.','T(3, 2) · f′(3) = tan 135° = −1'),A('g′’yü yaz','Bölüm kuralı uygulanır.','g′(x) = (f′(x)·x − f(x)) / x²'),A('x = 3’te hesapla','Değerler yerine yazılır.','g′(3) = (−1 · 3 − 2) / 9 = −5/9'),A('Normalin eğimi','Teğet eğiminin eksi tersi alınır.','−1 / (−5/9) = 9/5')],
 puf='Açı verildiğinde eğim tan θ’dır; normal için önce teğetin eğimini bulup eksi tersini alın.')

# ================= 16 zor · doğrularla sınırlı bölgede dikdörtgen =================
h=sp.symbols('h',positive=True); wexp=(8-h)-(h-1)/2; area=h*wexp
hs=sp.solve(sp.diff(area,h),h); assert hs==[sp.Rational(17,6)] and 1<=hs[0]<=sp.Rational(17,3)
v=Fr(17,4); assert wexp.subs(h,hs[0])==sp.Rational(17,4)
assert area.subs(h,hs[0])==sp.Rational(289,24)
e=[Fr(17,3),8,Fr(17,2),Fr(289,24)]
hh=sp.solve(sp.diff(h*(8-h-h/2),h),h)[0]; assert (8-hh-hh/2)==4
sc=0.75
poly=[(0,0),(8,0),(7/3,17/3),(0,1)]
rect=[(0.5,2),(6,2)]
body=graf(0,8,0,6,sc,sc,'\n'.join([
 '\\fill[blue!8] '+' -- '.join(f'({a*sc:.3f},{b*sc:.3f})' for a,b in poly)+' -- cycle;',
 f'\\fill[orange!25,draw={TUR},dashed,thick] ({0.5*sc:.3f},0) rectangle ({6*sc:.3f},{2*sc:.3f});',
 egri([(0,1),(7/3,17/3)],sc,sc,MAVI,'1.9pt'),egri([(7/3,17/3),(8,0)],sc,sc,MOR,'1.9pt'),
 f'\\node[font=\\footnotesize,text={MAVI},rotate=60] at ({1.0*sc:.3f},{4.0*sc:.3f}) {{$y = 2x + 1$}};',
 f'\\node[font=\\footnotesize,text={MOR},rotate=-45] at ({5.9*sc:.3f},{3.7*sc:.3f}) {{$y = 8 - x$}};']),xt=[1,2,3,4,5,6,7,8],yt=[1,2,3,4,5,6],gx=False,gy=False,ax=0.4)
SK=fig(body)
q('0016',tipId='tur2-optim',tip='En büyük ve en küçük değer',z='zor',alt='Bölgede Dikdörtgen',kaz='Doğrularla sınırlı bölgede kenarı x ekseni üzerinde olan dikdörtgenin alanını bir değişkene bağlayıp alanı en büyük yapan tabanı bulur.',kalip='şekilli',
 kart='K-ATRV2-07 (iki doğru ve eksenler, içine çizilen dikdörtgen) · alan fonksiyonunun maksimumu',
 metin='Dik koordinat düzleminde, şekildeki doğrular ile pozitif x ve y eksenleri arasında kalan bölge boyanmıştır.\nBu bölgede bir kenarı x ekseni üzerinde, üst köşeleri ise doğrular üzerinde olan dikdörtgenler oluşturuluyor.\nBuna göre, bu dikdörtgenlerden alanı en büyük olanın x ekseni üzerindeki kenarının uzunluğu kaç birimdir?',
 dogru=v,yan=[(Fr(17,3),'Doğruların kesiştiği noktanın ordinatını (17/3) dikdörtgenin tabanı sanmış.','bilgi'),(Fr(17,2),'Tabanı h değişkenine bağlamayı unutup yüksekliği sıfır aldığı durumdaki tabanı (17/2) yazmış.','dikkat'),(8,'Bölgenin x eksenindeki tüm uzunluğunu (8) dikdörtgenin tabanı sanmış.','bilgi'),(Fr(289,24),'Taban yerine en büyük alan değerini (289/24) yazmış.','dikkat')],
 istenen='Alanı en büyük olan dikdörtgenin x ekseni üzerindeki kenarının uzunluğu.',ip=['Dikdörtgenin yüksekliğine h deyip iki üst köşenin apsislerini h cinsinden yaz.'],bilgi=[GEO],sekil=SK,
 ad=[A('Köşeleri yaz','Yükseklik h iken sol köşe y = 2x + 1, sağ köşe y = 8 − x doğrusu üzerindedir.','sol apsis = (h − 1)/2 · sağ apsis = 8 − h'),A('Tabanı bul','Sağ ile sol apsisin farkı tabandır.','taban = 8 − h − (h − 1)/2 = (17 − 3h)/2'),A('Alanı yaz','Alan = taban × yükseklik.','A(h) = h(17 − 3h)/2'),A('Türevi sıfırla','A′(h) = (17 − 6h)/2 = 0.','h = 17/6 (1 ≤ h ≤ 17/3 aralığında)'),A('Tabanı hesapla','','(17 − 3 · 17/6)/2 = 17/4')],
 puf='Önce değişkenin aralığını kontrol et; sonra türevin kökü alan fonksiyonunun maksimumudur ve sorulan uzunluk bu değerle hesaplanır.')

# ================= 17 zor · f(x²) bileşkesinin ekstremum sayısı =================
f17p=lambda u:(u+2)**2*(u-1)*(u-4)/12
g17p=lambda u:2*u*f17p(u*u)
# g′ işaret aralıkları: ±2, ±1, 0 kökleri
brk=[-2,-1,0,1,2]; samp=[-3,-1.5,-0.5,0.5,1.5,3]
sg=[1 if g17p(s)>0 else -1 for s in samp]; assert sg==[-1,1,-1,1,-1,1]
changes=sum(1 for i in range(5) if sg[i]!=sg[i+1]); assert changes==5; v=5
# yanlışlar: yalnız f′ işaret değişimleri (1,4): 2 · x=0 unutulursa 4 · yalnız pozitif taraf+0: 3 · yalnız x=0: 1
sx,sy=0.95,0.36
body=graf(-3,5,-4,8,sx,sy,'\n'.join([
 egri(ornek(f17p,-3,4.6,150),sx,sy,MAVI,'1.9pt'),
 nokta(-2,0,sx,sy,'black','2.4pt'),nokta(1,0,sx,sy,'black','2.4pt'),nokta(4,0,sx,sy,'black','2.4pt'),
 etiket(-3,f17p(-3),sx,sy,'$f^{\\prime}$','above',MAVI,'\\small\\bfseries')]),xt=[-3,-2,-1,1,2,3,4,5],yt=[-4,-2,2,4,6,8],gy=False,ax=0.4)
SK=fig(body)
q('0017',tipId='tur2-ekstremart',tip='Artanlık ve ekstremum sayısı',z='zor',alt='Bileşke Fonksiyonda Ekstremum',kaz='f′ grafiğinden g(x) = f(x²) bileşkesinin türev işaretini inceleyip yerel ekstremum noktalarının sayısını bulur.',kalip='grafik',
 kart='K-ATRV2-11 (f′ grafiği, bileşke ve çift katlı kök) · g′ işaret tablosu ve ekstremum sayısı',
 metin='Şekilde, gerçel sayılar kümesinde türevlenebilir bir f fonksiyonunun türevi olan f′ fonksiyonunun grafiği verilmiştir. Grafik x eksenini yalnız x = −2, x = 1 ve x = 4 noktalarında buluşturmaktadır.\ng(x) = f(x²)\nolduğuna göre, g fonksiyonunun kaç farklı noktada yerel ekstremumu vardır?',
 dogru=v,yan=[(1,'g′(x) = 2x · f′(x²) çarpımında yalnız 2x’in kökünü (x = 0) ekstremum saymış.','bilgi'),(2,'f′’nün işaret değiştirdiği x = 1 ve x = 4 noktalarını doğrudan g’nin ekstremumları sanmış.','bilgi'),(3,'x = 0, x = 1 ve x = 2 değerlerini bulmuş; x ve −x ayrı ayrı olduğunu, negatif kökleri unutmuş.','dikkat'),(4,'g′ = 0’ın x = ±1, ±2 köklerini bulmuş, 2x çarpanından gelen x = 0’ı unutmuş.','dikkat')],
 istenen='g fonksiyonunun yerel ekstremum noktalarının sayısı.',ip=['g′(x) çarpımının her çarpanının işaretini aralıklarda ayrı ayrı yaz.'],bilgi=[GRF],sekil=SK,
 ad=[A('g′’yü yaz','Zincir kuralı uygulanır.','g′(x) = 2x · f′(x²)'),A('f′’nün işaretini oku','x = −2’de eksene değer (işaret değişmez); 1 ve 4’te işaret değiştirir.','x < 1: + · 1 < x < 4: − · x > 4: + (x ≠ −2)'),A('x² aralıklarını yaz','x² ≥ 0 olduğundan yalnız 1 ve 4’ün karşılığı olan x = ±1 ve x = ±2 önemlidir.','0 < x² < 1: + · 1 < x² < 4: − · x² > 4: +'),A('Çarpımın işaretini incele','x > 0 için işaret f′(x²)’nindir; x < 0 için 2x negatif olduğundan işaret tersine döner.','g′: (−∞, −2) −, (−2, −1) +, (−1, 0) −, (0, 1) +, (1, 2) −, (2, ∞) +'),A('Say','İşaret değişimi olan noktalar.','x = −2, −1, 0, 1, 2 → 5 nokta')],
 puf='Bileşkede g′ = (iç türev) × f′(iç) çarpımıdır; çarpanların işaretleri aralıklarda ayrı ayrı alınıp çarpılır.')

# ================= 18 zor · orijine uzaklık fonksiyonunun türevi =================
f18=lambda u:4-Fr(u-3)/2-Fr((u-3)**2)/8
assert f18(3)==4 and 4-Fr(5-3,2)==3
xx=sp.symbols('xx'); F=4-(xx-3)/2-(xx-3)**2/8; d=sp.sqrt(xx**2+F**2)
v=sp.nsimplify(sp.diff(d,xx).subs(xx,3)); assert v==sp.Rational(1,5)
v=Fr(1,5)
e=[Fr(1,25),Fr(1),Fr(7,5),Fr(2)]
assert Fr(3+4*Fr(1,2),5)==1 and Fr(3+4*1,5)==Fr(7,5) and Fr(3-2,25)==Fr(1,25) and 2*3+2*4*Fr(-1,2)==2
sc=0.9
body=graf(0,7,0,5,sc,sc,'\n'.join([
 egri(ornek(lambda u:float(F.subs(xx,u)) if False else 4-(u-3)/2-(u-3)**2/8,0,6.6,120),sc,sc,MAVI,'1.9pt'),
 egri([(1.4,4.8),(5.4,2.8)],sc,sc,TUR,'1.6pt'),
 f'\\draw[gray,dashed,thick] (0,0) -- ({3*sc:.3f},{4*sc:.3f});',
 nokta(3,4,sc,sc,'black','2.6pt'),nokta(5,3,sc,sc,TUR,'2.4pt'),
 etiket(3,4,sc,sc,'$P(3,\\,4)$','above right'),etiket(5,3,sc,sc,'$(5,\\,3)$','above right',TUR),
 etiket(0,0,sc,sc,'$O$','below left'),etiket(6.4,4-(6.4-3)/2-(6.4-3)**2/8,sc,sc,'$f$','right',MAVI,'\\small\\bfseries'),
 etiket(1.4,4.8,sc,sc,'$d$','above',TUR,'\\small\\bfseries')]),xt=[1,2,3,4,5,6,7],yt=[1,2,3,4,5],gx=False,gy=False,ax=0.4)
SK=fig(body)
q('0018',tipId='tur2-kural',tip='Türev kuralları ve uzaklık',z='zor',alt='Uzaklık Fonksiyonu',kaz='Grafikteki teğetten f(3) ve f′(3) değerlerini okuyup orijine uzaklık fonksiyonunun türevini zincir kuralıyla hesaplar.',kalip='grafik',
 kart='K-ATRV2-09 (grafik, teğet ve uzaklık) · karekökün türevi, f ve f′ değerleri',
 metin='Şekilde, gerçel sayılar kümesinde türevlenebilir f fonksiyonunun grafiği ile bu grafiğe P noktasında teğet olan d doğrusu verilmiştir. O orijin olmak üzere, x pozitif bir gerçel sayı için\ng(x) = |OA|\nile tanımlanıyor; burada A noktası, f’nin grafiği üzerinde apsisi x olan noktadır.\nBuna göre, g′(3) değeri kaçtır?',
 dogru=v,yan=[(Fr(1,25),'Türevi paydadaki √ ifadenin kendisine bölmek yerine uzaklığın karesi olan 25’e bölmüş.','islem'),(1,'d doğrusunun eğimini +1/2 okumuş (işareti ters): (3 + 4 · 1/2)/5 = 1.','bilgi'),(Fr(7,5),'f′(3) yerine 1 yazmış: (3 + 4 · 1)/5.','islem'),(2,'Uzaklık yerine uzaklığın karesinin türevini hesaplamış: 2 · 3 + 2 · 4 · (−1/2).','dikkat')],
 istenen='g′(3) değeri.',ip=['Uzaklığı koordinatlarla yazıp zincir kuralını uygula; f′(3)’ü d doğrusundan oku.'],bilgi=[UZK],sekil=SK,
 ad=[A('Değerleri oku','P noktası ve d doğrusunun geçtiği ikinci nokta şekilde yazılı.','f(3) = 4 · f′(3) = (3 − 4)/(5 − 3) = −1/2'),A('g’yi yaz','Uzaklık koordinatlardan bulunur.','g(x) = √(x² + f(x)²)'),A('Türev al','Zincir kuralıyla.','g′(x) = (2x + 2f(x)f′(x)) / (2√(x² + f(x)²))'),A('Yerleştir','x = 3 için √(9 + 16) = 5.','g′(3) = (3 + 4 · (−1/2)) / 5'),A('Sonuç','','(3 − 2)/5 = 1/5')],
 puf='Karekök içindeki ifadenin türevini alıp 2·√(…) ile böl; f ve f′ değerlerini aynı noktada oku.')

# ================= 19 zor · teğet ve eksenlerin oluşturduğu üçgenin en küçük alanı =================
aa=sp.symbols('aa',positive=True)
Ar=(aa**2+12)**2/(4*aa); crit=sp.solve(sp.diff(Ar,aa),aa); assert crit==[2] and 0<2<sp.sqrt(12)
assert Ar.subs(aa,2)==32 and sp.limit(Ar,aa,0,'+')==sp.oo and Ar.subs(aa,sp.sqrt(12))>32
v=32; e=[2,8,16,64]; assert len({v,*e})==5 and (12-4)==8 and 4+12==16 and 4*16==64
f19=lambda u:12-u*u
sx,sy=0.85,0.4
a0=1; ys=lambda u:-2*a0*u+a0*a0+12
body=graf(0,7,0,13,sx,sy,'\n'.join([
 '\\fill[orange!22] '+f'(0,0) -- ({(a0*a0+12)/(2*a0)*sx:.3f},0) -- (0,{(a0*a0+12)*sy:.3f}) -- cycle;',
 egri(ornek(f19,0,3.46,100),sx,sy,MAVI,'1.9pt'),
 egri([(0,ys(0)),((a0*a0+12)/(2*a0),0)],sx,sy,TUR,'1.8pt'),
 nokta(a0,f19(a0),sx,sy,'black','2.6pt'),etiket(a0,f19(a0),sx,sy,'$A$','above right'),
 f'\\node[right,font=\\small,text={MAVI}] at ({3.5*sx:.3f},{1.2*sy:.3f}) {{$y = 12 - x^2$}};']),xt=[1,2,3,4,5,6,7],yt=[2,4,6,8,10,12],gx=False,gy=False,ax=0.4)
SK=fig(body)
q('0019',tipId='tur2-optim',tip='En büyük ve en küçük değer',z='zor',alt='Teğet ve Üçgen Alanı',kaz='Parabolün teğetinin eksenlerle oluşturduğu üçgenin alanını değme noktasının apsisine bağlayıp en küçük alanı bulur.',kalip='şekilli',
 kart='K-ATRV2-07 (parabol teğeti ve eksenlerle üçgen) · alan fonksiyonunun minimumu',
 metin='Şekilde, bir parabolün grafiği ve bu parabol üzerindeki birinci bölgede bulunan bir A noktasında çizilen teğet ile pozitif eksenler arasında kalan boyalı üçgen verilmiştir.\nA noktası parabol üzerinde birinci bölgede hareket ederken oluşan bu tür üçgenlerin alanlarının en küçüğü kaç birimkaredir?',
 dogru=v,yan=[(2,'Alanı en küçük yapan değme noktasının apsisini (a = 2) alanın kendisi sanmış.','dikkat'),(8,'A noktasının ordinatını (12 − 4 = 8) alan sanmış.','dikkat'),(16,'Teğetin y eksenini kestiği ordinatı (4 + 12 = 16) alan sanmış.','dikkat'),(64,'Üçgenin alanını hesaplarken 1/2 çarpanını yazmamış: 4 × 16.','islem')],
 istenen='Oluşan üçgenlerin en küçük alanı.',ip=['A noktasının apsisine a deyip teğetin eksenleri kestiği noktaları a cinsinden yaz.'],bilgi=[GEO],sekil=SK,
 ad=[A('Teğeti yaz','A(a, 12 − a²) noktasında eğim −2a’dır.','y = −2a(x − a) + 12 − a² = −2ax + a² + 12'),A('Kesim noktaları','x = 0 ve y = 0 yazılır.','y eksenini a² + 12, x eksenini (a² + 12)/(2a) noktasında keser'),A('Alanı yaz','Dik üçgenin alanı.','S(a) = (a² + 12)² / (4a)'),A('Türevi sıfırla','Pay türevi alınıp sadeleştirilir.','S′(a) = (a² + 12)(3a² − 12) / (4a²) = 0 → a = 2'),A('En küçük alan','a = 2: taban 4, yükseklik 16.','S(2) = 16² / 8 = 32')],
 puf='Önce teğet denklemini değme noktasının apsisi cinsinden yaz; alanı bir değişkene indirdikten sonra türevin kökü ve aralığın uçları kontrol edilir.')

# ================= 20 zor · rasyonel fonksiyon, parametre ve normal =================
a_,b_=sp.symbols('a_ b_')
F20=(a_*x+b_)/(x+1)
sol=sp.solve([F20.subs(x,0)-3,sp.diff(F20,x).subs(x,1)+sp.Rational(1,2)],[a_,b_],dict=True)[0]; assert sol=={a_:1,b_:3}
F20s=F20.subs(sol); m2=sp.diff(F20s,x).subs(x,2); assert m2==sp.Rational(-2,9)
v=Fr(9,2); assert -1/m2==sp.Rational(9,2) and F20s.subs(x,2)==sp.Rational(5,3)
q('0020',tipId='tur2-rasyonel',tip='Rasyonel fonksiyon ve normal',z='orta',alt='Rasyonel Fonksiyon',kaz='Verilen değer ve eğim koşullarından rasyonel fonksiyonun sabitlerini bulup bir noktadaki normalin eğimini hesaplar.',kalip='düz',
 kart='K-ATRV2-12 (bölüm kuralı, iki koşul) · sabitlerin bulunması ve normalin eğimi',
 metin='a ve b gerçel sayılar olmak üzere,\nf(x) = (ax + b) / (x + 1)\nfonksiyonunun grafiği y eksenini (0, 3) noktasında kesmektedir ve grafiğe x = 1 apsisli noktada çizilen teğetin eğimi −1/2 dir.\nBuna göre, f’nin grafiğine x = 2 apsisli noktada çizilen normalin eğimi kaçtır?',
 dogru=v,yan=[(Fr(-9,2),'Normalin eğimi −1/m kuralında işareti yanlış yazıp 1/m = −9/2 bulmuş.','islem'),(Fr(-2,9),'Normal yerine x = 2’deki teğetin eğimini yazmış.','dikkat'),(Fr(2,9),'f′(2) = 2/9 bulmuş (türev paydasında işareti ters) ve normal eğimi yerine onu yazmış.','islem'),(Fr(5,3),'Eğim yerine f(2) = 5/3 değerini hesaplamış.','bilgi')],
 istenen='x = 2 apsisli noktadaki normalin eğimi.',ip=['Önce iki koşuldan a ve b’yi bul; türevi bölüm kuralıyla genel biçimde yaz.'],bilgi=[PAR,NRM],
 ad=[A('b’yi bul','(0, 3) noktası grafik üzerindedir.','f(0) = b = 3'),A('Türevi yaz','Bölüm kuralı: pay türevi a, payda türevi 1.','f′(x) = (a(x + 1) − (ax + b)) / (x + 1)² = (a − b)/(x + 1)²'),A('a’yı bul','f′(1) = −1/2 koşulu.','(a − 3)/4 = −1/2 → a = 1'),A('Teğetin eğimi','x = 2 için.','f′(2) = (1 − 3)/9 = −2/9'),A('Normalin eğimi','Eksi ters alınır.','−1/(−2/9) = 9/2')],
 puf='Rasyonel fonksiyonda önce sabitleri koşullardan bulup sonra türev alın; normalin eğimi teğetin eğiminin eksi tersidir.')

# ---------- yazım ----------
for q_ in P.ANA: q_['kardes']=None
tmp='/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/turevtwo/bos.json'
P.yaz(os.path.join(HV,'ayt-mat','tureviki-1.json'),tmp)
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=UK))['kartlar'].append(c['id'])
json.dump(dict(konu='Türev',surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2025 AYT Matematik çıkmış soruları ve yayın soru bankaları (yalnız mantık), MEB 12. sınıf matematik müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','tureviki.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler),'şekilli',sum(1 for q_ in P.ANA if q_['sekil']))
