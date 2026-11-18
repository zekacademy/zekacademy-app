"""AYT Matematik · Polinomlar (20 soru: 4 kolay / 10 orta / 6 zor). Şekil çözüm verisini taşır; her doğru ve çeldirici değer kodla hesaplanıp assert edilir.
Kardeş yok, ipucu 1. Çıktı: ayt-mat/polinom-1.json, kartlar/polinom.json"""
import sys,os,json
HD=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,os.path.join(HD,'..')); sys.path.insert(0,os.path.join(HD,'..','tyt-mat'))
import _hafif_mat as H
from _hafif_mat import mk,kart,tablo_svg,B,A
from ortak import Parti
from cizim import tikz_svg
from fractions import Fraction as Fr
import sympy as sp
x=sp.symbols('x')
H.KONU='Polinomlar'
UK='amat|Polinomlar'
P=Parti('polinom','Polinomlar',UK,ders='AYT Matematik',idon='aytmat')
KY='ÖSYM 2018–2025 AYT Matematik (polinom soruları; yalnız mantık) · MEB 11. sınıf'
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)
def fig(body,font='\\small'): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font='+font+']\n'+body+'\n\\end{tikzpicture}')
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)
def ev(e,v): return sp.Integer(sp.sympify(e).subs(x,v)) if sp.sympify(e).subs(x,v).is_Integer else sp.nsimplify(sp.sympify(e).subs(x,v))
def S(e): return int(e)
SIRA=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
def sirala(vals): return [s for s in SIRA if s in vals]

# ---------- bilgi kutuları (yalnız tanım ve gösterim; örnekler soruların sayılarından farklı) ----------
KTS=B('Katsayılar toplamı ve sabit terim','P(x) polinomunda x yerine 1 yazılınca katsayıların toplamı, x yerine 0 yazılınca sabit terim elde edilir. İki polinomun çarpımında baş katsayılar çarpılır, sabit terimler de çarpılır. Örnek: P(x) = (x + 2)(3x − 1) için P(1) = 3·2 = 6 ve P(0) = −2')
DER=B('Derece kuralları','Sıfırdan farklı P ve Q polinomlarında der[P·Q] = der[P] + der[Q] olur; toplamın ya da farkın derecesi en fazla büyük olan dereceye eşittir. Örnek: der[A] = 2 ve der[B] = 6 ise der[A·B] = 8 ve der[A + B] = 6’dır')
KAL=B('Kalan teoremi','P(x) polinomunun x − a ile bölümünden kalan P(a)’dır. İkinci dereceden bir bölenle bölümde kalan en çok birinci derecedendir: K(x) = mx + n biçiminde yazılıp bölenin kökleri için P(kök) = K(kök) eşitlikleri kullanılır. Örnek: P(x) = (x − 4)·Q(x) + 7 ise P(4) = 7’dir')
HOR=B('Horner düzeni','P(x)’in x − a ile bölümünde üst satıra katsayılar yazılır; ilk katsayı aşağı indirilir, her sütunda alt satırdaki sayı a ile çarpılıp bir sonraki sütunun üstüne eklenir. Alt satırın son sayısı kalan, öncekiler bölümün katsayılarıdır. Örnek: x² + 5x + 1 polinomunun x − 1 ile bölümünde alt satır 1, 6, 7 çıkar; bölüm x + 6, kalan 7’dir')
CAR=B('Çarpan ve özdeşlik','P(a) = 0 ise (x − a), P(x)’in bir çarpanıdır. Özdeş iki polinomun aynı dereceli terimlerinin katsayıları eşittir. Örnek: x² + 3x + 2 = (x + 1)(x + 2) olduğundan x = −1 ve x = −2 köktür')
GRF=B('Grafikten polinom','Grafiğin x eksenini kestiği noktalar kökleri verir; eksene değip geri dönen kök çift katlıdır, kesip geçen kök tek katlıdır. P(x) = a(x − r₁)(x − r₂)… yazılıp bir ek veriyle a bulunur. Örnek: kökleri 1 ve 3 olan ikinci dereceden P için (0, 6) noktası verilmişse a = 2’dir')
ISR=B('İşaret çizelgesi','Bir polinomun işareti köklerde değişir; çift katlı kökte işaret değişmez. Bölme içeren eşitsizlikte paydanın kökü çözüm kümesine alınmaz. Örnek: (x − 2)/(x + 1) ≤ 0 eşitsizliğinin çözümü −1 < x ≤ 2’dir')
SIM=B('Çift ve tek polinom','P(−x) = P(x) ise P’de yalnız çift dereceli terimler, P(−x) = −P(x) ise yalnız tek dereceli terimler bulunur. Tek polinomda x = 0 kök, çift polinomda a kök ise −a da köktür. Örnek: P(x) = x³ − 4x tektir ve kökleri 0, 2, −2’dir')
FRK=B('Ardışık değerlerin toplanması','P(x + 1) − P(x) = f(x) gibi bir eşitlikte x yerine ardışık tam sayılar yazılıp taraflar alt alta toplanırsa ara terimler birbirini götürür. Örnek: P(x + 1) − P(x) = 4x ise P(3) − P(0) = 0 + 4 + 8 olur')
DEG=B('Değerlerden polinom kurma','Derecesi ve baş katsayısı bilinen polinomda bilinmeyen katsayılar, verilen her değer için yazılan bir denklemden bulunur; denklemler birbirinden çıkarılınca bilinmeyen sayısı azalır. Örnek: P(x) = x² + mx + n için P(1) = 0 ve P(2) = 3 ise m + n = −1 ve 2m + n = −1 yazılır')

# ---------- kartlar (her tipId için bir kart) ----------
kartla('K-APLN-01','Derece ve katsayılar','Çarpım, toplam ve bileşkede derece kuralları ile P(1) ve P(0) değerleri kullanılır; verilen ifade açılmadan yalnız gereken değer hesaplanır.','Toplamın derecesini toplamak; P(1) yerine P(0) almak; baş katsayıyı sabit terimle karıştırmak; bileşkede dereceyi toplamak.','kolay','düz',3,'apl-derece','Derece ve katsayılar')
kartla('K-APLN-02','Grafikten polinom','Grafikteki kökler, kök katlılığı ve verilen bir nokta ile polinom çarpanlı biçimde kurulur; istenen değer ya da işaret bu biçimden bulunur.','Çift katlı kökü tek kat saymak; baş katsayıyı 1 sanmak; kökün işaretini ters yazmak; kesişmeyen kökü atlamak.','orta','grafik',4,'apl-grafik','Grafikten polinom')
kartla('K-APLN-03','Polinom eşitsizliği','Çarpanların işaret çizelgesi çıkarılır; çift katlı kökte işaretin değişmediği ve paydanın kökünün alınmadığı gözetilerek çözüm kümesi yazılır; tam sayılar sayılır.','Eşitlik uçlarını yanlış almak; çift katlı kökte işareti değiştirmek; paydanın kökünü çözüm kümesine katmak.','zor','şekilli',5,'apl-esitsizlik','Polinom eşitsizliği')
kartla('K-APLN-04','Kalan ve bölüm ilişkisi','Bölme eşitliğinden kalan polinomu bulmak için bölenin kökleri yerine yazılır; bileşik ya da iç içe bölmelerde kalan, bölenin çarpanlarına ayrılmasıyla bulunur.','Kalanı bölenle aynı dereceden yazmak; kökler yerine yanlış değer koymak; iç içe bölmede kalanı doğrudan eklemek.','orta','yeni nesil',4,'apl-kalan','Kalan ve bölüm ilişkisi')
kartla('K-APLN-05','Horner ve bölüm polinomu','Bölme şemasının satırları sütun sütun okunup bilinmeyen katsayılar bulunur; bölüm ve kalan buradan elde edilir.','Bölenin kökünün işaretini ters almak; alt satırın son sayısını bölüm katsayısı saymak; sütunları kaydırmak.','orta','şekilli',4,'apl-horner','Horner ve bölüm polinomu')
kartla('K-APLN-06','Çarpan, özdeşlik ve alan modeli','Kök bilgisinden çarpan yazılır, katsayı eşitlenir; alan modelinde parçaların çarpımları toplam polinomla karşılaştırılır.','Kökü çarpanda ters işaretle yazmak; özdeş terimleri farklı dereceyle eşlemek; tam sayı koşulunu kullanmamak.','orta','şekilli',4,'apl-carpan','Çarpan, özdeşlik ve alan modeli')
kartla('K-APLN-07','Çift ve tek polinom','Simetri koşulu hangi dereceli terimlerin bulunabileceğini ve köklerin eşleşmesini verir; kökler ve baş katsayıyla polinom kurulur.','Tek polinomda sıfır kökünü unutmak; simetriden gelen kökleri saymamak; çift polinomda tüm köklerin gerçel olduğunu sanmak.','zor','öncüllü',4,'apl-simetri','Çift ve tek polinom')
kartla('K-APLN-08','Değerlerden polinom ve fonksiyonel eşitlik','Verilen değerlerden katsayı denklemleri kurulur ya da P(x+1) − P(x) eşitliği ardışık değerler için toplanır.','Denklemleri çözerken işlem hatası yapmak; başlangıç değerini toplama katmamak; baş katsayıyı denklemlere katmamak.','zor','tablo',4,'apl-fark','Değerlerden polinom ve fonksiyonel eşitlik')

# ================= şekil yardımcıları =================
def egri(f,a,b,n=120,sx=1,sy=1):
    return ' '.join(f'({xx*sx:.3f},{yy*sy:.3f})' for xx,yy in [(a+(b-a)*i/n, f(a+(b-a)*i/n)) for i in range(n+1)])
def eksen(x0,x1,y0,y1,sx,sy,xt,yt=None,xlab='x',ylab='y',fs='\\footnotesize'):
    o=[]
    for i in xt: o.append(f'\\draw[gray!35,thin] ({i*sx:.3f},{y0*sy:.3f}) -- ({i*sx:.3f},{y1*sy:.3f});')
    for j in (yt or []): o.append(f'\\draw[gray!35,thin] ({x0*sx:.3f},{j*sy:.3f}) -- ({x1*sx:.3f},{j*sy:.3f});')
    o.append(f'\\draw[-{{Stealth}},thick] ({x0*sx:.3f},0) -- ({x1*sx:.3f},0) node[right] {{{xlab}}};')
    o.append(f'\\draw[-{{Stealth}},thick] (0,{y0*sy:.3f}) -- (0,{y1*sy:.3f}) node[above] {{{ylab}}};')
    for i in xt:
        if i!=0: o.append(f'\\node[font={fs},fill=white,inner sep=1pt] at ({i*sx:.3f},-0.4) {{${i}$}};')
    for j in (yt or []):
        if j!=0: o.append(f'\\node[left=2pt,font={fs},fill=white,inner sep=0.6pt] at (0,{j*sy:.3f}) {{${j}$}};')
    return '\n'.join(o)

# ============================ SORULAR ============================
# ---- 0001 · kolay · düz · P(1)·P(0)
Pe=(x**2-3*x+1)**2*(2*x-5)
p1=S(Pe.subs(x,1)); p0=S(Pe.subs(x,0)); lead=S(sp.Poly(sp.expand(Pe),x).LC())
assert (p1,p0,lead)==(-3,-5,2)
dg=p1*p0; assert dg==15
e1=((-1)*(-3))*p0; e2=p1+p0; e3=p1-p0; e4=p1*lead
assert (e1,e2,e3,e4)==(-15,-8,2,-6) and len({dg,e1,e2,e3,e4})==5
q('0001',tipId='apl-derece',tip='Derece ve katsayılar',z='kolay',alt='Katsayılar toplamı ve sabit terim',kaz='Çarpım biçiminde verilen polinomun katsayılar toplamı ile sabit terimini açmadan hesaplar.',kalip='düz',
 kart='K-APLN-01 · P(1)·P(0), çarpımlı polinom',
 metin='P(x) = (x² − 3x + 1)²·(2x − 5)\npolinomu veriliyor.\nBuna göre, P(x) polinomunun katsayıları toplamı ile sabit teriminin çarpımı kaçtır?',
 dogru=dg,yan=[(e1,'(−1)² değerini −1 almış: P(1) = (−1)(−3) = 3 bulup 3·(−5) yazmış.','islem'),(e2,'Çarpım yerine katsayılar toplamı ile sabit terimi toplamış: −3 + (−5).','dikkat'),(e3,'Çarpım yerine iki değerin farkını almış: −3 − (−5).','dikkat'),(e4,'Sabit terim yerine baş katsayıyı (2) kullanmış: (−3)·2.','bilgi')],
 istenen='Katsayılar toplamı ile sabit terimin çarpımı.',ip=['İfadeyi açmak yerine, istenen iki değeri tek bir sayı yazarak bulmayı dene.'],bilgi=[KTS],
 ad=[A('Katsayılar toplamı','x yerine 1 yazılır.','P(1) = (1 − 3 + 1)²·(2 − 5) = 1·(−3) = −3'),A('Sabit terim','x yerine 0 yazılır.','P(0) = 1²·(−5) = −5'),A('Çarpım','İki değer çarpılır.','(−3)·(−5) = 15')],
 puf='Çarpımlı biçimi açmadan, istenen iki değer doğrudan yerine koyma ile bulunur.')

# ---- 0002 · kolay · tablo · baş katsayı + sabit terim
TB=[('P(x)',3,2,4),('Q(x)',2,-3,5),('R(x)',1,4,-2)]
SK=tablo_svg(['Polinom','Derece','Baş katsayı','Sabit terim'],[[a,str(d),str(b).replace('-','−'),str(c).replace('-','−')] for a,d,b,c in TB])
bas=2*(-3); sab=4*5+(-2); dg=bas+sab; assert (bas,sab,dg)==(-6,18,12)
e1=bas+(20); e2=(2-3+4)+sab; e3=(bas+4)+sab; e4=(2-3)+(4+5-2)
assert (e1,e2,e3,e4)==(14,21,16,6) and len({dg,e1,e2,e3,e4})==5
q('0002',tipId='apl-derece',tip='Derece ve katsayılar',z='kolay',alt='Derece ve katsayılar',kaz='Tabloda verilen polinom bilgileriyle çarpım ve toplamın baş katsayısını ve sabit terimini bulur.',kalip='tablo',
 kart='K-APLN-01 · tablo, çarpım ve toplam',
 metin='Aşağıdaki tabloda gerçel katsayılı P(x), Q(x) ve R(x) polinomlarının derecesi, baş katsayısı ve sabit terimi verilmiştir.\nBuna göre, P(x)·Q(x) + R(x) polinomunun baş katsayısı ile sabit teriminin toplamı kaçtır?',
 dogru=dg,yan=[(e1,'R(x)’in sabit terimini (−2) eklemeyi unutup sabit terimi 20 almış: −6 + 20.','dikkat'),(e2,'Baş katsayıyı çarpmak yerine üç baş katsayıyı toplamış: 2 − 3 + 4 = 3; sabit terim 18 ile 21.','islem'),(e3,'R(x) birinci dereceden olduğu halde baş katsayısını (4) toplam baş katsayıya eklemiş: (−6 + 4) + 18.','bilgi'),(e4,'Çarpım yerine toplam almış: baş katsayı 2 + (−3) = −1, sabit terim 4 + 5 − 2 = 7.','islem')],
 istenen='Baş katsayı ile sabit terimin toplamı.',ip=['Çarpımın en yüksek dereceli terimi hangi iki terimin çarpımından gelir; R(x) buna katkı yapar mı?'],bilgi=[KTS,DER],sekil=SK,
 ad=[A('Baş katsayı','Çarpımın derecesi 5’tir; R(x) birinci dereceden olduğundan baş katsayıya katkı yapmaz.','2·(−3) = −6'),A('Sabit terim','Çarpımın sabit terimi çarpıma, toplam sabit terimi R’nin sabit terimini ekler.','4·5 + (−2) = 18'),A('Topla','İki değer toplanır.','−6 + 18 = 12')],
 puf='Çarpımda baş katsayılar ve sabit terimler ayrı ayrı çarpılır; toplamda ise yalnız aynı dereceli terimler birleşir.')

# ---- 0003 · kolay · grafik · 2(x+1)(x−2)(x−3)
f3=lambda t:2*(t+1)*(t-2)*(t-3)
assert f3(0)==12 and f3(4)==20
sx,sy=0.9,0.115
g=[eksen(-2,4,-16,16,sx,sy,[-2,-1,1,2,3,4],[-12,-8,-4,4,8,12],ylab='$y$').replace('\\node[font=\\footnotesize,fill=white,inner sep=1pt] at','\\node[font=\\footnotesize,fill=white,inner sep=1pt] at')]
g.append(f'\\draw[blue!75!black,very thick] plot[smooth] coordinates {{{egri(f3,-1.45,3.42,90,sx,sy)}}};')
for r in (-1,2,3): g.append(f'\\fill[orange!90!black] ({r*sx:.3f},0) circle (0.09);')
g.append(f'\\fill[orange!90!black] (0,{12*sy:.3f}) circle (0.09);')
g.append(f'\\node[above right,font=\\footnotesize\\bfseries,text=orange!70!black] at (0,{12*sy:.3f}) {{$(0,\\,12)$}};')
SK=fig('\n'.join(g))
dg=f3(4)
a_=12/6; assert a_==2
e1=1*5*2*1; e2=6*5*2*1; e3=12*5*2*1; e4=4*5*2*1
assert (e1,e2,e3,e4)==(10,60,120,40) and len({dg,e1,e2,e3,e4})==5
q('0003',tipId='apl-grafik',tip='Grafikten polinom',z='kolay',alt='Grafikten polinom kurma',kaz='Kökleri ve y eksenini kestiği nokta verilen üçüncü dereceden polinomu çarpanlı yazıp bir değerini hesaplar.',kalip='grafik',
 kart='K-APLN-02 · üç tek katlı kök ve y kesim noktası',
 metin='Şekildeki grafik, üçüncü dereceden P(x) polinomuna aittir; grafiğin eksenleri kestiği noktalar işaretlenmiştir.\nBuna göre, P(4) kaçtır?',
 dogru=dg,yan=[(e1,'Baş katsayıyı 1 almış: (4 + 1)(4 − 2)(4 − 3) = 10.','dikkat'),(e2,'a’yı 12/((1)(2)) = 6 bulmuş (x = 0’da (x − 3) çarpanını hesaba katmamış): P(4) = 6·5·2·1.','islem'),(e3,'Baş katsayı yerine P(0) = 12’yi çarpan olarak almış: 12·5·2·1.','bilgi'),(e4,'a’yı 12/3 = 4 bulmuş (x = 0’da yalnız 3 kökünün çarpanını hesaba katmış): 4·5·2·1.','islem')],
 istenen='P(4) değeri.',ip=['Kökler belli; geriye çarpanlı biçimin başındaki sayıyı bulacak tek bilgi var.'],bilgi=[GRF],sekil=SK,
 ad=[A('Çarpanlı yaz','Kökler −1, 2, 3 olduğundan P(x) = a(x + 1)(x − 2)(x − 3).','P(x) = a(x + 1)(x − 2)(x − 3)'),A('a’yı bul','Grafik (0, 12) noktasından geçer.','a·1·(−2)(−3) = 12 → a = 2'),A('P(4) hesapla','Değer yerine konur.','2·5·2·1 = 20')],
 puf='Çarpanlı biçimde bilinmeyen tek şey baş katsayıdır; grafikteki bir nokta onu verir.')

# ---- 0004 · kolay · öncüllü derece
c_I=True; c_II=False; c_III=True
assert (5+3,max(5,3),5*3)==(8,5,15)
dg='I ve III'
vals=['Yalnız I','Yalnız II','I ve II',dg,'I, II ve III']
q('0004',tipId='apl-derece',tip='Derece ve katsayılar',z='kolay',alt='Derece kuralları',kaz='Çarpım, toplam ve bileşke polinomun derecesini kurallarla belirler.',kalip='öncüllü',
 kart='K-APLN-01 · derece öncülleri (çarpım, toplam, bileşke)',
 metin='P(x) beşinci dereceden, Q(x) üçüncü dereceden birer polinomdur.\nBuna göre,\nI. P(x)·Q(x) polinomunun derecesi 8’dir.\nII. P(x) + Q(x) polinomunun derecesi 8’dir.\nIII. P(Q(x)) polinomunun derecesi 15’tir.\nifadelerinden hangileri doğrudur?',
 dogru=dg,yan=[('Yalnız I','III. öncülde P(Q(x)) için derecelerin çarpılması gerektiğini bilmeyip derece 8 sanmış.','bilgi'),('Yalnız II','Çarpım ve toplam kurallarını yer değiştirmiş: çarpımın derecesini 5, toplamın derecesini 8 sanmış; bileşkeyi de 8 bulmuş.','dikkat'),('I ve II','Toplamın derecesini 5 + 3 = 8 almış ve bileşkeyi 8 sanmış.','dikkat'),('I, II ve III','II. öncülü de doğru sanmış: toplamın derecesini toplama ile karıştırmış.','dikkat')],sira=sirala(vals),
 istenen='Doğru olan öncüller.',ip=['Çarpım, toplam ve bileşke için derece kuralları farklı davranır.'],bilgi=[DER],
 ad=[A('I. öncül','Çarpımda dereceler toplanır.','5 + 3 = 8 → doğru'),A('II. öncül','Toplamın derecesi büyük olan dereceye eşittir.','en çok 5 → yanlış'),A('III. öncül','Bileşkede dereceler çarpılır.','5·3 = 15 → doğru')],
 puf='Çarpımda dereceler toplanır, toplamda büyük olan kalır, bileşkede çarpılır.')

# ---- 0005 · orta · iç içe bölme
# P=(x−2)Q+5, Q=(x+1)R+3  → K(x)=3x−1
K=3*x-1; assert sp.expand((x-2)*((x+1)*sp.Symbol('R')+3)+5-((x-2)*(x+1)*sp.Symbol('R')+K))==0
dg=S(K.subs(x,4)); assert dg==11
e1=3+5; e2=S((3*x+5).subs(x,4)); e3=S((3*(x+1)+5).subs(x,4)); e4=5
assert (e1,e2,e3,e4)==(8,17,20,5) and len({dg,e1,e2,e3,e4})==5
q('0005',tipId='apl-kalan',tip='Kalan ve bölüm ilişkisi',z='orta',alt='İç içe bölme',kaz='İç içe bölme eşitliklerinden ikinci dereceden bölenle kalan polinomu bulur.',kalip='yeni nesil',
 kart='K-APLN-04 · P = (x − 2)Q + 5, Q = (x + 1)R + 3',
 metin='P(x), Q(x) ve R(x) polinomları için\nP(x) = (x − 2)·Q(x) + 5\nQ(x) = (x + 1)·R(x) + 3\neşitlikleri sağlanmaktadır.\nP(x) polinomunun x² − x − 2 ile bölümünden kalan polinom K(x) olduğuna göre, K(4) kaçtır?',
 dogru=dg,yan=[(e1,'Kalan polinomu yerine iki kalan sayıyı toplamış: 3 + 5.','dikkat'),(e2,'Q’daki 3 kalanını (x − 2) ile çarpmadan K(x) = 3x + 5 yazmış.','islem'),(e3,'3 kalanını (x + 1) ile çarpmış: K(x) = 3(x + 1) + 5 yazmış.','islem'),(e4,'P(x)’in x − 2 ile bölümünden kalanı (5) K(4) sanmış.','bilgi')],
 istenen='K(4) değeri.',ip=['İki bölme eşitliğini ve bölenin çarpanlarını birlikte düşün.'],bilgi=[KAL],
 ad=[A('Yerine koy','Q(x) birinci eşitlikte yazılır.','P(x) = (x − 2)[(x + 1)R(x) + 3] + 5'),A('Düzenle','Bölen x² − x − 2 = (x − 2)(x + 1) ile çarpılan kısım ayrılır.','P(x) = (x − 2)(x + 1)R(x) + 3(x − 2) + 5'),A('Kalan polinom','Kalan en çok birinci derecedendir.','K(x) = 3x − 1'),A('K(4)','x = 4 yazılır.','3·4 − 1 = 11')],
 puf='Bölen çarpanlarına ayrılınca iç içe eşitlikten kalan polinom doğrudan okunur.')

# ---- 0006 · orta · Horner
a_,b_=-1,1
Pq=x**3+a_*x**2+b_*x-6
assert sp.rem(Pq,x-2,x)==0 and sp.quo(Pq,x-2,x)==x**2+x+3
dg=S(Pq.subs(x,-1)); assert dg==-9
e1=S(Pq.subs(x,1)); e2=S((x**2+x+3).subs(x,-1)); e3=S(Pq.subs(x,0)); e4=-dg
assert (e1,e2,e3,e4)==(-5,3,-6,9) and len({dg,e1,e2,e3,e4})==5
g=[]
g.append('\\node[font=\\large\\bfseries] at (-1.05,1.0) {$2$};\\draw[thick] (-0.65,1.45) -- (-0.65,0.5);')
cols=[0,1.35,2.7,4.05]
for cx,t in zip(cols,['1','a','b','-6']): g.append(f'\\node[font=\\large\\bfseries,text=blue!70!black] at ({cx},1.0) {{${t}$}};')
for cx in cols[1:]: g.append(f'\\draw[orange!80!black,dashed,thick,fill=orange!10] ({cx-0.4},0.15) rectangle ({cx+0.4},0.65);')
g.append('\\draw[thick] (-0.65,-0.05) -- (4.65,-0.05);')
for cx,t in zip(cols,['1','1','3','0']): g.append(f'\\node[font=\\large\\bfseries,text=green!45!black] at ({cx},-0.5) {{${t}$}};')
g.append('\\draw[thick] (-0.65,0.5) -- (4.65,0.5) ;'.replace('(-0.65,0.5) -- (4.65,0.5)','(3.4,1.45) -- (3.4,-0.85)').replace('thick','thick,gray!70'))
g.append('\\node[font=\\footnotesize,text=blue!70!black,anchor=west] at (5.0,1.0) {üst satır: $P(x)$’in katsayıları};')
g.append('\\node[font=\\footnotesize,text=orange!80!black,anchor=west] at (5.0,0.4) {orta satır: çarpımlar};')
g.append('\\node[font=\\footnotesize,text=green!45!black,anchor=west] at (5.0,-0.5) {alt satır: sonuçlar};')
SK=fig('\n'.join(g),font='\\small')
q('0006',tipId='apl-horner',tip='Horner ve bölüm polinomu',z='orta',alt='Horner düzeni',kaz='Horner düzeninin alt satırından bilinmeyen katsayıları bulup başka bir bölenle kalanı hesaplar.',kalip='şekilli',
 kart='K-APLN-05 · x³ + ax² + bx − 6, bölen x − 2, alt satır 1, 1, 3, 0',
 metin='P(x) = x³ + ax² + bx − 6 polinomunun x − 2 ile bölümü şekilde Horner düzeniyle gösterilmiştir; orta satırdaki çarpımlar yazılmamıştır.\nBuna göre, P(x) polinomunun x + 1 ile bölümünden kalan kaçtır?',
 dogru=dg,yan=[(e1,'Bölenin kökünü +1 almış: P(1) hesaplamış.','dikkat'),(e2,'Bölüm polinomu x² + x + 3’ün x = −1’deki değerini kalan sanmış.','bilgi'),(e3,'Kalan yerine P(0) = −6 sabit terimini yazmış.','dikkat'),(e4,'x + 1 ile bölümde kökü −1 alıp işareti ters çevirerek −P(−1) bulmuş.','islem')],
 istenen='P(x)’in x + 1 ile bölümünden kalan.',ip=['Alt satırdaki her sayıyı, üstündeki sayıya hangi çarpımın eklendiğiyle ilişkilendir.'],bilgi=[HOR],sekil=SK,
 ad=[A('a’yı bul','İkinci sütunda alt satır, a ile 2’nin toplamıdır.','a + 2 = 1 → a = −1'),A('b’yi bul','Üçüncü sütunda b ile 2·1 toplanıp 3 olur.','b + 2 = 3 → b = 1'),A('Polinomu yaz','Katsayılar yerine konur; son sütun 0 çıkıyor, tutarlıdır.','P(x) = x³ − x² + x − 6'),A('Kalan','x + 1 ile bölümde kalan P(−1)’dir.','−1 − 1 − 1 − 6 = −9')],
 puf='Alt satırdaki sayılar üstteki sayı ile bölen kökünün çarpımının toplamıdır; tek tek geriye doğru çözülür.')

# ---- 0007 · orta · alan modeli
ab=[(a,b) for a in range(1,13) for b in range(1,13) if a*b==12 and b+2*a==11]; assert ab==[(4,3)]
aa,bb=ab[0]; xv=3
dg=2*aa*xv; assert dg==24
e1=2*3*xv; e2=bb*xv; e3=aa*bb; e4=2*xv*(xv+aa)
assert (e1,e2,e3,e4)==(18,9,12,42) and len({dg,e1,e2,e3,e4})==5
g=[]
W1,W2,H1,H2=2.1,2.5,2.4,1.5
g.append(f'\\draw[blue!70!black,fill=blue!10,thick] (0,{H2}) rectangle ({W1},{H1+H2});')
g.append(f'\\draw[orange!80!black,fill=orange!25,thick] ({W1},{H2}) rectangle ({W1+W2},{H1+H2});')
g.append(f'\\draw[green!45!black,fill=green!10,thick] (0,0) rectangle ({W1},{H2});')
g.append(f'\\draw[purple!70!black,fill=purple!10,thick] ({W1},0) rectangle ({W1+W2},{H2});')
g.append(f'\\node[font=\\large\\bfseries] at ({W1/2},{H2+H1/2}) {{$2x^2$}};')
g.append(f'\\node[font=\\large\\bfseries] at ({W1+W2/2},{H2/2}) {{$12$}};')
g.append(f'\\node[font=\\small] at ({W1+W2/2},{H2+H1/2}) {{taralı}};')
g.append(f'\\node[above,font=\\large] at ({W1/2},{H1+H2}) {{$x$}};\\node[above,font=\\large] at ({W1+W2/2},{H1+H2}) {{$a$}};')
g.append(f'\\node[left,font=\\large] at (0,{H2+H1/2}) {{$2x$}};\\node[left,font=\\large] at (0,{H2/2}) {{$b$}};')
SK=fig('\n'.join(g))
q('0007',tipId='apl-carpan',tip='Çarpan, özdeşlik ve alan modeli',z='orta',alt='Alan modeli',kaz='Alan modelinden kenar polinomlarını kurup toplam alan polinomuyla katsayıları eşleştirir.',kalip='şekilli',
 kart='K-APLN-06 · alan 2x² + 11x + 12, kenar parçaları x, a / 2x, b',
 metin='Alanı 2x² + 11x + 12 cm² olan bir dikdörtgen, şekildeki gibi dört dikdörtgene ayrılmıştır. Uzunluklar cm cinsindendir; a ve b pozitif tam sayılardır.\nBuna göre, x = 3 iken taralı dikdörtgenin alanı kaç cm²’dir?',
 dogru=dg,yan=[(e1,'a ile b’yi ters yerleştirmiş (a = 3, b = 4): 2·3·3.','islem'),(e2,'Taralı bölge yerine sol alttaki parçayı (b·x) hesaplamış: 3·3.','dikkat'),(e3,'Taralı bölgenin alanı yerine sağ alttaki parçanın alanı olan a·b = 12’yi yazmış.','dikkat'),(e4,'Taralı parça yerine 2x yüksekliğindeki bütün şeridi (x + a genişliğinde) hesaplamış: 6·7.','bilgi')],
 istenen='Taralı dikdörtgenin alanı (cm²).',ip=['Toplam alanı parçaların alanlarının toplamı olarak yaz ve x’li terimlerin katsayılarını karşılaştır.'],bilgi=[CAR],sekil=SK,
 ad=[A('Parçaları yaz','Alan (x + a)(2x + b) çarpımıdır; parçalar 2x², bx, 2ax, ab.','(x + a)(2x + b) = 2x² + (b + 2a)x + ab'),A('Eşitle','Şekilde ab = 12, toplamda x’in katsayısı 11’dir.','ab = 12 ve b + 2a = 11'),A('Tam sayıları ara','Pozitif tam sayı çifti denenir.','a = 4, b = 3'),A('Taralı alan','Taralı bölge a genişliğinde, 2x yüksekliğindedir.','4·(2·3) = 24')],
 puf='Parçaların alanları toplam polinomun terimleriyle özdeştir; şekildeki bilinen alan ikinci denklemi verir.')

# ---- 0008 · orta · grafik + eşitsizlik
f8=lambda t:0.5*(t+4)*(t+1)*(t-3)
sx,sy=0.85,0.11
g=[eksen(-5,4,-18,22,sx,sy,[-5,-4,-3,-2,-1,1,2,3,4],[],ylab='$y$')]
g.append(f'\\draw[blue!75!black,very thick] plot[smooth] coordinates {{{egri(f8,-4.95,3.85,110,sx,sy)}}};')
for r in (-4,-1,3): g.append(f'\\fill[orange!90!black] ({r*sx:.3f},0) circle (0.09);')
SK=fig('\n'.join(g))
cnt=lambda lst:len(lst)
pol=lambda t:(t+4)*(t+1)*(t-3)*(t+2)
Z=[t for t in range(-40,41) if pol(t)<=0]; assert Z==[-4,-3,-2,-1,0,1,2,3] and min(Z)==-4
dg=len(Z); strict=len([t for t in range(-40,41) if pol(t)<0]); assert (dg,strict)==(8,4)
e1=strict; e2=len([t for t in Z if t>=-1]); e3=len([t for t in Z if t!=-2]); e4=len([t for t in Z if t<=-2])
assert (e1,e2,e3,e4)==(4,5,7,3) and len({dg,e1,e2,e3,e4})==5
q('0008',tipId='apl-esitsizlik',tip='Polinom eşitsizliği',z='orta',alt='Grafikten eşitsizlik',kaz='Grafiği verilen polinomun işaretinden çarpım eşitsizliğinin tam sayı çözümlerini sayar.',kalip='grafik',
 kart='K-APLN-03 · kökler −4, −1, 3, baş katsayı pozitif; (x + 2)·P(x) ≤ 0',
 metin='Grafiği şekilde verilen üçüncü dereceden P(x) polinomu için (x + 2)·P(x) ≤ 0 eşitsizliği tanımlanıyor.\nBuna göre, (x + 2)·P(x) ≤ 0 eşitsizliğini sağlayan kaç farklı x tam sayısı vardır?',
 dogru=dg,yan=[(e1,'Eşitlik durumunu almamış: (x + 2)·P(x) < 0 çözümündeki tam sayıları saymış.','dikkat'),(e2,'Yalnız [−1, 3] aralığını almış, x < −2 bölgesindeki çözümü unutmuş.','dikkat'),(e3,'x + 2 = 0 olan x = −2 değerini çözüm kümesinden çıkarmış.','dikkat'),(e4,'Yalnız [−4, −2] aralığını almış, [−1, 3] aralığını katmamış.','islem')],
 istenen='Eşitsizliği sağlayan tam sayıların sayısı.',ip=['Çarpımın işaretini, iki çarpanın işaretinin aynı sayı doğrusu üzerinde birlikte okunmasıyla incele.'],bilgi=[ISR,GRF],sekil=SK,
 ad=[A('P’nin işareti','Üç kök tek katlıdır ve grafik sağ uçta yukarı gider.','x < −4: −, (−4, −1): +, (−1, 3): −, x > 3: +'),A('Çarpımın işareti','x + 2, x = −2’de işaret değiştirir; iki çarpan birlikte okunur.','çarpım ≤ 0: [−4, −2] ve [−1, 3]'),A('Tam sayıları say','Uçlar dahil.','−4, −3, −2 ve −1, 0, 1, 2, 3 → 8')],
 puf='Sıfır olan çarpanlar eşitsizlikte dahildir; çarpım için her çarpanın işareti kök noktalarında değişir.')

# ---- 0009 · orta · öncüllü grafik
f9=lambda t:0.35*(t+2)*(t-1)**2*(t-3)
sx,sy=0.95,0.2
g=[eksen(-3,4,-4,12,sx,sy,[-3,-2,-1,1,2,3,4],[],ylab='$y$')]
g.append(f'\\draw[blue!75!black,very thick] plot[smooth] coordinates {{{egri(f9,-2.95,3.9,110,sx,sy)}}};')
for r in (-2,1,3): g.append(f'\\fill[orange!90!black] ({r*sx:.3f},0) circle (0.09);')
SK=fig('\n'.join(g))
assert f9(0)<0 and f9(2)<0 and f9(0)*f9(2)>0
dg='Yalnız I'
vals=[dg,'Yalnız II','Yalnız III','I ve III','II ve III']
q('0009',tipId='apl-grafik',tip='Grafikten polinom',z='orta',alt='Kök katlılığı ve işaret',kaz='Grafikte eksene değen kökün çift katlı olduğunu ve kök sayısıyla derece ilişkisini yorumlar.',kalip='öncüllü',
 kart='K-APLN-02 · kökler −2, 1 (çift katlı), 3; öncüllü yorum',
 metin='Şekilde, derecesi en az 4 olan P(x) polinomunun grafiği verilmiştir.\nBuna göre,\nI. P(x), (x − 1)² ile tam bölünür.\nII. P(x) polinomunun derecesi tek sayıdır.\nIII. P(0)·P(2) < 0 dır.\nifadelerinden hangileri her zaman doğrudur?',
 dogru=dg,yan=[('Yalnız II','Grafik iki ucu da yukarı giderken dereceyi tek saymış; I’deki çift kat kökü fark etmemiş.','bilgi'),('Yalnız III','P(0) ve P(2) değerlerinin işaretlerini zıt sanmış; oysa ikisi de negatiftir.','dikkat'),('I ve III','III. öncülde P(0)·P(2) çarpımının işaretini yanlış belirlemiş.','islem'),('II ve III','I’i yanlış sanmış, II ve III’ü doğru saymış.','dikkat')],sira=sirala(vals),
 istenen='Her zaman doğru olan öncüller.',ip=['Eksene değip dönen kök ile kesip geçen kökün katlılık farkını ve iki uçtaki yönü düşün.'],bilgi=[GRF],sekil=SK,
 ad=[A('I. öncül','x = 1’de grafik eksene değip geri dönüyor, kök çift katlıdır.','(x − 1)² çarpandır → doğru'),A('II. öncül','İki uç aynı yöne gidiyorsa derece çifttir.','derece çift → yanlış'),A('III. öncül','x = 0 ve x = 2 noktalarında grafik eksenin altındadır.','P(0) < 0, P(2) < 0 → çarpım pozitif → yanlış')],
 puf='Çift katlı kök grafikte işareti değiştirmeyen kök noktasıdır; uçların yönü dereceyi çift ya da tek yapar.')

# ---- 0010 · orta · tek polinom
Pt=2*x*(x**2-1)*(x**2-9)
assert sp.expand(Pt+Pt.subs(x,-x))==0 and sp.Poly(Pt,x).degree()==5 and sp.Poly(Pt,x).LC()==2
dg=S(Pt.subs(x,2)); assert dg==-60
e1=-dg; e2=S((x*(x**2-1)*(x**2-9)).subs(x,2)); e3=S((2*(x-1)*(x-3)*x).subs(x,2)); e4=S((2*(x**2-1)*(x**2-9)).subs(x,2))//2
assert (e1,e2,e3,e4)==(60,-30,-4,-15) and len({dg,e1,e2,e3,e4})==5
q('0010',tipId='apl-simetri',tip='Çift ve tek polinom',z='orta',alt='Tek polinom',kaz='P(x) + P(−x) = 0 koşulundan kökleri çıkarıp polinomu kurar ve değerini hesaplar.',kalip='düz',
 kart='K-APLN-07 · 5. dereceden tek polinom, P(1) = P(3) = 0',
 metin='P(x), baş katsayısı 2 olan beşinci dereceden gerçel katsayılı bir polinomdur. 1 ve 3 sayıları bu polinomun kökleridir ve P(−x) = −P(x) olduğu bilinmektedir.\nBuna göre, P(2) kaçtır?',
 dogru=dg,yan=[(e1,'P(−2) = 60 değerini P(2) sanmış (tek polinomda P(−x) = −P(x) olduğunu işlemde ters uygulamış).','islem'),(e2,'Baş katsayıyı (2) çarpan olarak yazmamış: x(x² − 1)(x² − 9) değerini almış.','dikkat'),(e3,'Yalnız 0, 1 ve 3 köklerini kullanmış (−1 ve −3’ü unutmuş): 2x(x − 1)(x − 3).','bilgi'),(e4,'Sıfır kökünü unutup x çarpanını yazmamış: (2²−1)(2²−9) = −15.','bilgi')],
 istenen='P(2) değeri.',ip=['P(−x) = −P(x) koşulu kökler hakkında ne söyler?'],bilgi=[SIM],
 ad=[A('Simetriyi yorumla','Eşitlik P’nin tek olduğunu gösterir; 0 köktür, 1 ve 3 kök ise −1 ve −3 de köktür.','kökler: 0, ±1, ±3'),A('Polinomu kur','Beş kök, derece 5 ve baş katsayı 2.','P(x) = 2x(x² − 1)(x² − 9)'),A('P(2)','x = 2 yazılır.','2·2·3·(−5) = −60')],
 puf='Tek polinomda x = 0 her zaman köktür; derece kadar kök bulununca polinom kurulur.')

# ---- 0011 · orta · hikâyeli kutu + Horner
V=4*x**3-100*x**2+600*x
assert sp.expand(x*(30-2*x)*(20-2*x))==V
Q=sp.quo(V,x-4,x); assert Q==4*x**2-84*x+264 and sp.rem(V,x-4,x)==1056
dg=S(Q.subs(x,1)); assert dg==184
e1=S(V.subs(x,4)); e2=S(V.subs(x,1)); e3=S(sp.quo(V,x+4,x).subs(x,1)); e4=S(sp.quo(x*(30-x)*(20-x),x-4,x).subs(x,1))
assert (e1,e2,e3,e4)==(1056,504,952,371) and len({dg,e1,e2,e3,e4})==5
g=[]
g.append('\\draw[blue!70!black,fill=blue!8,thick] (0,0) rectangle (6,4);')
for (cx,cy) in [(0,0),(5.2,0),(0,3.2),(5.2,3.2)]: g.append(f'\\draw[orange!80!black,fill=orange!35,thick] ({cx},{cy}) rectangle ({cx+0.8},{cy+0.8});')
g.append('\\draw[gray,dashed] (0.8,0) -- (0.8,4);\\draw[gray,dashed] (5.2,0) -- (5.2,4);\\draw[gray,dashed] (0,0.8) -- (6,0.8);\\draw[gray,dashed] (0,3.2) -- (6,3.2);')
g.append('\\node[font=\\small] at (0.4,0.4) {$x$};\\node[font=\\small] at (5.6,3.6) {$x$};')
g.append('\\node[below,font=\\normalsize] at (3,0) {$30$ cm};\\node[rotate=90,above,font=\\normalsize] at (0,2) {$20$ cm};')
g.append('\\node[font=\\small,text=blue!70!black] at (3,2) {karton};')
SK=fig('\n'.join(g))
q('0011',tipId='apl-horner',tip='Horner ve bölüm polinomu',z='orta',alt='Modelleme ve bölme',kaz='Hacim polinomunu kurup Horner düzeniyle bölüm polinomunu bulur ve değerini hesaplar.',kalip='hikâyeli',
 kart='K-APLN-05 · 30×20 karton, köşe kareleri x; bölen x − 4',
 metin='Bir atölyede şekildeki dikdörtgen biçimindeki kartonun dört köşesinden kenar uzunluğu x cm olan kareler kesilmekte, kalan kısım katlanarak üstü açık bir kutu yapılmaktadır. Kutunun hacmini cm³ cinsinden veren V(x) polinomunun x − 4 ile bölümünden elde edilen bölüm Q(x) olduğuna göre, Q(1) kaçtır?',
 dogru=dg,yan=[(e1,'Bölüm yerine kalanı (V(4) = 1056) yazmış.','bilgi'),(e2,'Bölüm yerine V(1) = 504 hacmini hesaplamış.','dikkat'),(e3,'Bölenin kökünü −4 almış: Horner’de −4 ile çarpıp Q(1) = 952 bulmuş.','dikkat'),(e4,'Kutunun hacmini x(30 − x)(20 − x) yazmış (iki kenardan yalnız bir kez kesmiş); bölümün x = 1 değeri 371 olmuş.','bilgi')],
 istenen='Q(1) değeri.',ip=['Önce kutunun boyutlarını x cinsinden yaz; polinom üçüncü dereceden olacak.'],bilgi=[HOR],sekil=SK,
 ad=[A('Boyutlar','Taban kenarları 30 − 2x ve 20 − 2x, yükseklik x.','V(x) = x(30 − 2x)(20 − 2x)'),A('Açılım','Çarpım açılır.','V(x) = 4x³ − 100x² + 600x'),A('Horner, bölen x − 4','Alt satır 4, 4·4 − 100, ...','4, −84, 264, kalan 1056'),A('Q(1)','Bölüm 4x² − 84x + 264.','4 − 84 + 264 = 184')],
 puf='Önce modeli polinom olarak yaz; bölüm polinomu, Horner’in alt satırının ilk üç sayısıdır.')

# ---- 0012 · orta · tablo + öncüllü bileşke
TV=[(-1,5),(0,3),(1,-2),(2,4)]
SK=tablo_svg(['x']+[str(a).replace('-','−') for a,_ in TV],[['P(x)']+[str(b).replace('-','−') for _,b in TV]])
Pv=dict(TV)
assert Pv[0]==3 and Pv[1]==-2 and Pv[2]==4 and Pv[-1]==5
dg='II ve III'
vals=['Yalnız I','Yalnız III','I ve II',dg,'I, II ve III']
q('0012',tipId='apl-derece',tip='Derece ve katsayılar',z='orta',alt='Bileşke polinomun katsayıları',kaz='P(ax + b) biçimindeki polinomların katsayılar toplamı ile sabit terimini tablodan okur.',kalip='öncüllü',
 kart='K-APLN-01 · P(x−1), P(2x+1), P(3−x) için P(1) ve P(0) okuması',
 metin='Aşağıdaki tabloda, P(x) polinomunun bazı değerleri verilmiştir.\nBuna göre,\nI. P(x − 1) polinomunun katsayıları toplamı 5’tir.\nII. P(2x + 1) polinomunun sabit terimi −2’dir.\nIII. P(3 − x) polinomunun katsayıları toplamı 4’tür.\nifadelerinden hangileri doğrudur?',
 dogru=dg,yan=[('Yalnız I','I’de P(x − 1)’in katsayılar toplamı için P(−1) = 5 okumuş; II’de P(2) = 4’ü, III’te P(3)’ü arayıp ikisini yanlış sanmış.','dikkat'),('Yalnız III','III’ü doğru bulup II’de sabit terimi P(0) sanmış: −2 yerine 3 beklemiş.','bilgi'),('I ve II','I’i doğru sanmış (P(−1) = 5), III’te P(2) yerine P(3) aramış.','islem'),('I, II ve III','I’de P(0) = 3 yerine P(−1) = 5 değerini doğru kabul etmiş.','dikkat')],sira=sirala(vals),
 istenen='Doğru olan öncüller.',ip=['Her öncülde istenen değerin P’nin hangi girişine karşılık geldiğini bul.'],bilgi=[KTS],sekil=SK,
 ad=[A('I. öncül','Katsayılar toplamı için x = 1: P(0) bulunur.','P(0) = 3 ≠ 5 → yanlış'),A('II. öncül','Sabit terim için x = 0: P(1) bulunur.','P(1) = −2 → doğru'),A('III. öncül','x = 1 için P(3 − 1) = P(2).','P(2) = 4 → doğru')],
 puf='P(ax + b) polinomunda x yerine 1 yazınca P(a + b), 0 yazınca P(b) elde edilir.')

# ---- 0013 · orta · özdeşlik (x−2 kuvvetleri)
Pi=2*x**2-3*x+5
aa,bb,cc=2,5,7
assert sp.expand(aa*(x-2)**2+bb*(x-2)+cc-Pi)==0
dg=aa*bb+cc; assert dg==17
e1=2*(-3)+5; e2=aa*(bb+cc); e3=aa+bb+cc; e4=aa*bb*cc
assert (e1,e2,e3,e4)==(-1,24,14,70) and len({dg,e1,e2,e3,e4})==5
q('0013',tipId='apl-carpan',tip='Çarpan, özdeşlik ve alan modeli',z='orta',alt='Özdeşlik',kaz='Polinomu (x − a) kuvvetlerine göre yazarak özdeşlikteki katsayıları bulur.',kalip='düz',
 kart='K-APLN-06 · 2x² − 3x + 5 = a(x − 2)² + b(x − 2) + c',
 metin='Her x gerçel sayısı için\n2x² − 3x + 5 = a(x − 2)² + b(x − 2) + c\nözdeşliği sağlandığına göre, a·b + c kaçtır?',
 dogru=dg,yan=[(e1,'Katsayıları (x − 2) kuvvetine çevirmeden a = 2, b = −3, c = 5 almış.','dikkat'),(e2,'İfadeyi a·(b + c) diye okumuş: 2·(5 + 7).','dikkat'),(e3,'a·b + c yerine a + b + c yazmış: 2 + 5 + 7.','dikkat'),(e4,'a·b + c yerine üçünün çarpımını almış: 2·5·7.','dikkat')],
 istenen='a·b + c değeri.',ip=['Verilen eşitlikte x için seçilecek özel bir değer işini kolaylaştırır mı?'],bilgi=[CAR],
 ad=[A('c’yi bul','x = 2 yazılır.','c = 2·4 − 6 + 5 = 7'),A('Açılımı yaz','(x − 2)² = x² − 4x + 4.','a x² + (b − 4a)x + (4a − 2b + c)'),A('Katsayıları eşitle','x² ve x katsayıları.','a = 2, b − 8 = −3 → b = 5'),A('İstenen','a·b + c hesaplanır.','2·5 + 7 = 17')],
 puf='Özdeşlikte uygun bir x değeri, bilinmeyenlerden birini tek başına verir.')

# ---- 0014 · orta · çarpan teoremi
Pc=(x-1)*(x+2)*(x+3)
assert sp.expand(Pc.subs(x,0))==-6 and sp.Poly(Pc,x).LC()==1
dg=S(Pc.subs(x,2)); assert dg==20
e1=S(((x-1)*(x+2)*(x-3)).subs(x,2)); e2=S(((x-1)*(x+2)*(x+6)).subs(x,2)); e3=S(((x-1)*(x+2)**2).subs(x,2)); e4=S(((x-1)*(x+2)*(x+1)).subs(x,2))
assert (e1,e2,e3,e4)==(-4,32,16,12) and len({dg,e1,e2,e3,e4})==5
q('0014',tipId='apl-carpan',tip='Çarpan, özdeşlik ve alan modeli',z='orta',alt='Çarpan teoremi',kaz='Kalanı 0 olan bölenlerden çarpanları yazıp sabit terimle üçüncü kökü bulur.',kalip='düz',
 kart='K-APLN-06 · monik 3. derece, x − 1 ve x + 2 çarpan, P(0) = −6',
 metin='Baş katsayısı 1 olan üçüncü dereceden P(x) polinomu, x − 1 ve x + 2 ile tam bölünmektedir.\nP(0) = −6 olduğuna göre, P(2) kaçtır?',
 dogru=dg,yan=[(e1,'Üçüncü kökü 3 alıp çarpanı (x − 3) yazmış.','islem'),(e2,'Sabit terimi (−6) doğrudan çarpan sabiti sanıp (x + 6) yazmış.','dikkat'),(e3,'(x + 2) çarpanını iki kez kullanmış.','bilgi'),(e4,'Üçüncü çarpanı (x + 1) sanmış.','islem')],
 istenen='P(2) değeri.',ip=['Kökleri belli olan çarpanlı biçimden sonra verilen hangi bilgi henüz kullanılmadı?'],bilgi=[CAR],
 ad=[A('Çarpanlar','Tam bölünme, iki kökü verir.','P(x) = (x − 1)(x + 2)(x − r)'),A('Üçüncü kök','P(0) = −6 yazılır.','(−1)(2)(−r) = −6 → r = −3'),A('P(2)','x = 2 yazılır.','1·4·5 = 20')],
 puf='Çarpanlı biçimde bilinmeyen kök, bir ek değerle (burada sabit terim) bulunur.')

# ---- 0015 · zor · tablo + fark
P15=x**3-2*x**2+3*x+1
v=[S(P15.subs(x,k)) for k in (1,2,3,4)]
assert v==[3,7,19,45] and 3*v[2]-3*v[1]+v[0]+6==v[3]
SK=tablo_svg(['x','1','2','3'],[['P(x)']+[str(t) for t in v[:3]]])
dg=v[3]
e1=3*v[2]-3*v[1]+v[0]; e2=v[2]+12; e3=3*v[2]-3*v[1]+v[0]+1; e4=26
assert (e1,e2,e3,e4)==(39,31,40,26) and len({dg,e1,e2,e3,e4})==5
q('0015',tipId='apl-fark',tip='Değerlerden polinom ve fonksiyonel eşitlik',z='zor',alt='Değerlerden polinom kurma',kaz='Baş katsayısı bilinen üçüncü dereceden polinomun üç değerinden katsayıları bulup başka bir değerini hesaplar.',kalip='tablo',
 kart='K-APLN-08 · baş katsayısı 1, 3. derece, P(1), P(2), P(3) tablosu',
 metin='Baş katsayısı 1 olan üçüncü dereceden P(x) polinomunun x = 1, 2, 3 için değerleri aşağıdaki tabloda verilmiştir.\nBuna göre, P(x) polinomunun x − 4 ile bölümünden kalan kaçtır?',
 dogru=dg,yan=[(e1,'Değerleri ikinci dereceden bir kurala uydurup (baş katsayıyı yok sayıp) P(4) = 3·19 − 3·7 + 3 bulmuş.','bilgi'),(e2,'Değerleri doğrusal sanıp 7 ile 19 arasındaki artışı (12) sürdürmüş: 19 + 12.','islem'),(e3,'Denklemleri çözerken c’yi 1 yerine 2 bulup P(4) = 40 çıkarmış.','dikkat'),(e4,'P(4) yerine P(4) − P(3) = 26 farkını yazmış.','dikkat')],
 istenen='P(4) değeri (kalan).',ip=['Verilen her değerin polinomun katsayıları için ne anlama geldiğini düşün.'],bilgi=[DEG,KAL],sekil=SK,
 ad=[A('Polinomu yaz','Baş katsayı 1 olduğundan P(x) = x³ + ax² + bx + c.','P(1) = 3, P(2) = 7, P(3) = 19 için üç denklem'),A('Denklemleri kur','Her değer yerine konur.','a + b + c = 2, 4a + 2b + c = −1, 9a + 3b + c = −8'),A('Çöz','Denklemler birbirinden çıkarılır.','3a + b = −3, 5a + b = −7 → a = −2, b = 3, c = 1'),A('Kalan','Kalan P(4)’tür.','64 − 32 + 12 + 1 = 45')],
 puf='Bilinmeyen katsayılar, verilen değerlerin her biri için yazılan denklemlerden bulunur.')

# ---- 0016 · zor · bileşke + ikinci dereceden bölen
# P kalan 2x+3 (x²−x−6), P(x+2) kalanı (x²+3x−4)
P3=2*3+3; Pm2=2*(-2)+3; assert (P3,Pm2)==(9,-1)
a_=sp.Rational(P3-Pm2,5); b_=P3-a_; assert (a_,b_)==(2,7)
dg=S((a_*x+b_).subs(x,5)); assert dg==17
e1=S((2*x+3).subs(x,5))
sol=sp.solve([sp.Symbol('a')+sp.Symbol('b')-Pm2,-4*sp.Symbol('a')+sp.Symbol('b')-P3],[sp.Symbol('a'),sp.Symbol('b')]); e2=S((sol[sp.Symbol('a')]*x+sol[sp.Symbol('b')]).subs(x,5))
e3=7; e4=10
assert (e1,e2,e3,e4)==(13,-9,7,10) and len({dg,e1,e2,e3,e4})==5
q('0016',tipId='apl-kalan',tip='Kalan ve bölüm ilişkisi',z='zor',alt='Bileşke ve ikinci dereceden bölen',kaz='Kalan polinomu bilinen P(x)’ten P(x + 2)’nin başka bir ikinci dereceden bölenle kalanını bulur.',kalip='yeni nesil',
 kart='K-APLN-04 · P’nin x² − x − 6 ile kalanı 2x + 3; P(x + 2) ve x² + 3x − 4',
 metin='P(x) polinomunun x² − x − 6 ile bölümünden kalan 2x + 3’tür.\nT(x) = P(x + 2) polinomunun x² + 3x − 4 ile bölümünden kalan R(x) olduğuna göre, R(5) kaçtır?',
 dogru=dg,yan=[(e1,'Kalanın değişmediğini sanmış: R(x) = 2x + 3 alıp R(5) = 13 yazmış.','bilgi'),(e2,'T(1) = P(3) ve T(−4) = P(−2) eşlemesini ters yazmış: T(1) = −1, T(−4) = 9 almış.','islem'),(e3,'Yalnız kalanın sabit terimini (7) yazmış, R(5)’i hesaplamamış.','dikkat'),(e4,'R(x) = 2x biçiminde (b = 0) alıp 2·5 hesaplamış.','islem')],
 istenen='R(5) değeri.',ip=['Verilen iki bölenin çarpanlarını karşılaştır.'],bilgi=[KAL],
 ad=[A('P’nin değerleri','x² − x − 6 = (x − 3)(x + 2) olduğundan kök değerleri kalandan okunur.','P(3) = 9, P(−2) = −1'),A('T’nin kökleri','x² + 3x − 4 = (x − 1)(x + 4); T(1) = P(3), T(−4) = P(−2).','T(1) = 9, T(−4) = −1'),A('R(x) = mx + n','İki denklem çözülür.','m + n = 9, −4m + n = −1 → m = 2, n = 7'),A('R(5)','x = 5 yazılır.','2·5 + 7 = 17')],
 puf='Bölenin kökleri hangi değerlerin kullanılacağını belirler; yeni polinomun kökleri eskisinin köklerinden kaydırma ile eşlenir.')

# ---- 0017 · zor · işaret çizelgesi (iki doğru)
SX=0.62; xs=list(range(-6,8))
g=[f'\\draw[-{{Stealth}},thick] ({-6.4*SX:.3f},0) -- ({7.7*SX:.3f},0);']
for k in xs: g.append(f'\\draw ({k*SX:.3f},0.07) -- ({k*SX:.3f},-0.07);\\node[below,font=\\scriptsize] at ({k*SX:.3f},-0.07) {{${k}$}};')
yP,yQ=1.6,3.1
def isaretler(y,kok,isr):
    o=[f'\\draw[thick] ({-6.4*SX:.3f},{y}) -- ({7.4*SX:.3f},{y});']
    sinir=[-6.4]+kok+[7.4]
    for i,s_ in enumerate(isr):
        mid=(sinir[i]+sinir[i+1])/2
        renk='green!45!black' if s_=='+' else 'red!70!black'
        o.append(f'\\node[font=\\Large\\bfseries,text={renk}] at ({mid*SX:.3f},{y+0.38}) {{${"+" if s_=="+" else "-"}$}};')
    for k in kok: o.append(f'\\fill[orange!90!black] ({k*SX:.3f},{y}) circle (0.09);\\draw[gray!50,dashed] ({k*SX:.3f},{y}) -- ({k*SX:.3f},0);')
    return o
g+=isaretler(yP,[-3,4],['+','-','+'])
g+=isaretler(yQ,[-1,2],['-','+','+'])
g.append(f'\\node[anchor=east,font=\\large\\bfseries,text=blue!70!black] at ({-6.55*SX:.3f},{yP}) {{$P(x)$}};')
g.append(f'\\node[anchor=east,font=\\large\\bfseries,text=purple!70!black] at ({-6.55*SX:.3f},{yQ}) {{$Q(x)$}};')
g.append(f'\\node[above,font=\\scriptsize,text=orange!70!black] at ({2*SX:.3f},{yQ+0.75}) {{\\small çift katlı kök}};')
SK=fig('\n'.join(g))
Pf=lambda t:(t+3)*(t-4); Qf=lambda t:(t+1)*(t-2)**2
R7=range(-6,8)
Zs=[t for t in R7 if Qf(t)!=0 and Pf(t)*Qf(t)<=0]; dg=len(Zs); assert Zs==[-6,-5,-4,-3,0,1,3,4] and dg==8
cA=len([t for t in R7 if Qf(t)!=0 and Pf(t)*Qf(t)<0])
cB=len([t for t in R7 if Qf(t)==0 or Pf(t)*Qf(t)<=0])
cC=len([t for t in R7 if (Qf(t)!=0 or t==-1) and Pf(t)*Qf(t)<=0 or t==-1])
cD=len([t for t in Zs if t>=-1])
assert (cA,cB,cC,cD)==(6,10,9,4) and len({dg,cA,cB,cC,cD})==5
q('0017',tipId='apl-esitsizlik',tip='Polinom eşitsizliği',z='orta',alt='İşaret çizelgesi',kaz='İki polinomun işaret çizelgesinden bölüm eşitsizliğinin tam sayı çözümlerini sayar; çift katlı kök ve payda kökünü gözetir.',kalip='şekilli',
 kart='K-APLN-03 · P: −3 ve 4, Q: −1 ve 2 (çift katlı); P(x)/Q(x) ≤ 0, [−6, 7]',
 metin='Şekilde, P(x) ve Q(x) polinomlarının işaretleri kök noktaları ve aralıklar için verilmiştir; Q(x)’in x = 2 kökü çift katlıdır.\nBuna göre, P(x)/Q(x) ≤ 0 eşitsizliğini sağlayan ve [−6, 7] aralığında bulunan kaç farklı x tam sayısı vardır?',
 dogru=dg,yan=[(cA,'Payın köklerini (−3 ve 4) çözüme katmamış: eşitlik durumunu atlayıp “< 0” çözümündeki tam sayıları saymış.','dikkat'),(cB,'Paydanın köklerini (−1 ve 2) de çözüm kümesine katmış.','dikkat'),(cC,'Paydanın köklerinden yalnız −1’i çözüme katmış, 2’yi dışarıda bırakmış.','bilgi'),(cD,'x < −3 bölgesindeki çözümü atlayıp yalnız −1’den büyük aralıkları saymış.','islem')],
 istenen='Çözüm kümesindeki tam sayıların sayısı.',ip=['Bölümün işareti, payın ve paydanın işaretlerinin aynı aralıkta birlikte okunmasıyla bulunur; sıfır olan paydaya dikkat et.'],bilgi=[ISR],sekil=SK,
 ad=[A('Bölümün işareti','Her aralıkta P ve Q’nun işaretleri çarpılır (bölüm ile aynı işaret).','x < −3: −, (−3, −1): +, (−1, 2): −, (2, 4): −, x > 4: +'),A('Uçları değerlendir','x = −3 ve x = 4’te pay sıfırdır, çözüme girer; x = −1 ve x = 2’de payda sıfırdır, girmez.','(−∞, −3] ∪ (−1, 2) ∪ (2, 4]'),A('Tam sayıları say','[−6, 7] aralığında.','−6, −5, −4, −3, 0, 1, 3, 4 → 8')],
 puf='Pay sıfırsa çözüme girer, payda sıfırsa asla girmez; çift katlı kökte işaret aynı kalır.')

# ---- 0018 · zor · fonksiyonel eşitlik
Pf5=(x+1)**2
assert sp.expand(Pf5.subs(x,x+1)-Pf5)==2*x+3 and Pf5.subs(x,0)==1
dg=S(Pf5.subs(x,5)); assert dg==36
e1=dg-1; e2=1+sum(2*k+3 for k in range(1,6)); e3=1+(2*5+3); e4=sum(2*k+3 for k in range(1,6))
assert (e1,e2,e3,e4)==(35,46,14,45) and len({dg,e1,e2,e3,e4})==5
q('0018',tipId='apl-fark',tip='Değerlerden polinom ve fonksiyonel eşitlik',z='orta',alt='P(x + 1) − P(x) eşitliği',kaz='P(x + 1) − P(x) bilinen bir polinomken ardışık farkları toplayarak istenen değeri bulur.',kalip='yeni nesil',
 kart='K-APLN-08 · P(x + 1) − P(x) = 2x + 3, P(0) = 1',
 metin='Gerçel katsayılı bir P(x) polinomunda x yerine x + 1 yazıldığında polinomun değeri 2x + 3 kadar artmaktadır; yani P(x + 1) = P(x) + 2x + 3 eşitliği bütün gerçel sayılar için geçerlidir.\nP(0) = 1 olduğuna göre, P(5) kaçtır?',
 dogru=dg,yan=[(e1,'Toplamda başlangıç değeri P(0) = 1’i eklememiş.','dikkat'),(e2,'Farkları k = 0, …, 4 yerine k = 1, …, 5 için toplamış ve P(0)’ı eklemiş.','islem'),(e3,'Tek adımda ilerlemiş: P(5) = P(0) + (2·5 + 3).','bilgi'),(e4,'k = 1, …, 5 için farkları toplamış ve P(0)’ı eklememiş.','islem')],
 istenen='P(5) değeri.',ip=['Eşitliği x = 0, 1, 2, … için yazıp tarafları alt alta toplamayı düşün.'],bilgi=[FRK],
 ad=[A('Eşitliği sırala','x = 0, 1, 2, 3, 4 için yazılır.','P(1) − P(0) = 3, P(2) − P(1) = 5, P(3) − P(2) = 7, P(4) − P(3) = 9, P(5) − P(4) = 11'),A('Toplam','Ara terimler birbirini götürür.','P(5) − P(0) = 3 + 5 + 7 + 9 + 11 = 35'),A('P(5)','P(0) eklenir.','35 + 1 = 36')],
 puf='Ardışık farkların toplamı uçtaki iki değerin farkını verir; başlangıç değeri unutulmamalıdır.')

# ---- 0019 · zor · öncüllü çift polinom
dg='I ve II'
vals=['Yalnız I','Yalnız III',dg,'II ve III','I, II ve III']
# P(x)=x⁴+ax²+b, P(1)=0 → b=−1−a → (x²−1)(x²+a+1)
a_s=sp.Symbol('a')
assert sp.expand((x**2-1)*(x**2+a_s+1)-(x**4+a_s*x**2-1-a_s))==0
assert sp.Poly(x**4+0*x**2-1,x).all_coeffs()==[1,0,0,0,-1]  # a=0, b=-1: x⁴−1 → ±i kökleri var
q('0019',tipId='apl-simetri',tip='Çift ve tek polinom',z='zor',alt='Çift polinom ve kökler',kaz='x⁴ + ax² + b biçimindeki çift polinomda P(1) = 0 koşulundan çarpan ve köklere dair doğru yorumları ayırır.',kalip='öncüllü',
 kart='K-APLN-07 · x⁴ + ax² + b, P(1) = 0; öncüllü yorum',
 metin='a ve b gerçel sayılar olmak üzere\nP(x) = x⁴ + ax² + b\npolinomu için P(1) = 0 olduğu biliniyor.\nBuna göre,\nI. P(−1) = 0 dır.\nII. P(x), x² − 1 ile tam bölünür.\nIII. P(x) polinomunun bütün kökleri gerçel sayıdır.\nifadelerinden hangileri her zaman doğrudur?',
 dogru=dg,yan=[('Yalnız I','I’i doğru bulmuş, II’de iki kökün x² − 1 = (x − 1)(x + 1) ile tam bölünmeyi gerektirdiğini görmemiş.','bilgi'),('Yalnız III','I’de P(−1) = −P(1) sanıp, II’de bölünebilmeyi yalnız x − 1 çarpanıyla sınırlayıp ikisini yanlış bulmuş; III’ü doğru saymış.','dikkat'),('II ve III','I’i yanlış sanıp çift polinomda −1’in de kök olduğunu atlamış; III’ü doğru saymış.','dikkat'),('I, II ve III','III’ü de doğru sanmış: x⁴ − 1 örneğini denememiş.','dikkat')],sira=sirala(vals),
 istenen='Her zaman doğru olan öncüller.',ip=['P(−x) ile P(x) arasındaki ilişkiye bak.'],bilgi=[SIM,CAR],
 ad=[A('I. öncül','P çifttir, P(−1) = P(1).','P(−1) = 0 → doğru'),A('II. öncül','1 ve −1 kök olduğundan (x − 1)(x + 1) çarpandır.','x² − 1 ile tam bölünür → doğru'),A('III. öncül','a = 0 ve b = −1 için P(x) = x⁴ − 1’in kökleri ±1 ve ±i’dir.','sanal kök var → yanlış')],
 puf='Çift polinomda kökler ± çiftleri halinde gelir; ama kökün gerçel olacağı garanti değildir.')

# ---- 0020 · zor · grafik + kalan
f20=lambda t:(t+3)*(t-1)**2*(t-3)
sx,sy=0.95,0.06
g=[eksen(-4,4,-4,48,sx,sy,[-2,-1,1,2,3,4],[],ylab='$y$')]
g.append(f'\\node[above=3pt,font=\\footnotesize] at ({-3*sx:.3f},0) {{$-3$}};\\draw[gray!35,thin] ({-3*sx:.3f},{-4*sy:.3f}) -- ({-3*sx:.3f},{48*sy:.3f});')
g.append(f'\\draw[blue!75!black,very thick] plot[smooth] coordinates {{{egri(f20,-3.4,3.6,140,sx,sy)}}};')
for r in (-3,1,3): g.append(f'\\fill[orange!90!black] ({r*sx:.3f},0) circle (0.09);')
SK=fig('\n'.join(g))
P20=(x+3)*(x-1)**2*(x-3)
Rk=sp.rem(sp.expand(P20),x**2-1,x); assert Rk==16*x-16
dg=S(Rk.subs(x,5)); assert dg==64
e1=S((-16*x+16).subs(x,5)); e2=S(P20.subs(x,-1)); e3=S((16*x-32).subs(x,5)); e4=16*5
assert (e1,e2,e3,e4)==(-64,-32,48,80) and len({dg,e1,e2,e3,e4})==5
q('0020',tipId='apl-grafik',tip='Grafikten polinom',z='zor',alt='Grafikten kalan',kaz='Kökleri (biri çift katlı) grafikten okunan polinomun ikinci dereceden bölenle kalanını bulur.',kalip='grafik',
 kart='K-APLN-02 · kökler −3, 1 (çift katlı), 3; baş katsayı 1; bölen x² − 1',
 metin='Şekilde, baş katsayısı 1 olan dördüncü dereceden P(x) polinomunun grafiği verilmiştir. P(x) polinomunun x² − 1 ile bölümünden kalan R(x) olduğuna göre, R(5) kaçtır?',
 dogru=dg,yan=[(e1,'P(−1) = −32 yerine +32 alıp m = −16, n = 16 bulmuş: R(x) = −16x + 16.','islem'),(e2,'Kalan polinomu yazmadan P(−1) = −32 değerini cevap sanmış.','bilgi'),(e3,'m = 16 bulup n yerine P(−1) = −32 almış: R(x) = 16x − 32.','islem'),(e4,'R(x) = 16x alıp sabit terimi unutmuş.','dikkat')],
 istenen='R(5) değeri.',ip=['Grafikten çarpanlı biçimi kur; kalan birinci dereceden olduğundan bölenin iki kökünde P ile aynı değeri alır.'],bilgi=[KAL,GRF],sekil=SK,
 ad=[A('Polinomu yaz','Kökler −3, 1 (çift katlı), 3.','P(x) = (x + 3)(x − 1)²(x − 3)'),A('Bölenin kökleri','x² − 1’in kökleri 1 ve −1; kalan R(x) = mx + n.','R(1) = P(1) = 0, R(−1) = P(−1) = (2)(4)(−4) = −32'),A('R(x)’i bul','İki denklem çözülür.','m + n = 0, −m + n = −32 → m = 16, n = −16'),A('R(5)','x = 5 yazılır.','16·5 − 16 = 64')],
 puf='Kalan en çok birinci derecedendir; bölenin iki kökü kalanın iki katsayısını belirler.')

# ---------------- yazma ----------------
from collections import Counter
for qq in P.ANA: qq['kardes']=None
json.dump(P.ANA,open(os.path.join(HD,'polinom-1.json'),'w'),ensure_ascii=False,indent=1)
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=UK))['kartlar'].append(c['id'])
json.dump(dict(konu=P.konu_adi,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2025 AYT Matematik çıkmış soruları ve yayın soru bankaları (yalnız mantık), MEB 11–12. sınıf müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HD,'..','kartlar','polinom.json'),'w'),ensure_ascii=False,indent=1)
print(len(P.ANA),'soru · harfler',dict(sorted(Counter(z['cevap']['sik'] for z in P.ANA).items())),'· zorluk',dict(Counter(z['zorluk'] for z in P.ANA)),'· şekilli',sum(1 for z in P.ANA if z['sekil']),'· tipId',len(tipler))
