"""AYT Matematik · Polinomlar 2. dalga (20 soru: 3 kolay / 10 orta / 7 zor). Şekil çözüm verisini taşır; her doğru ve çeldirici değer kodla hesaplanıp assert edilir.
Çıktı: ayt-mat/polinomiki-1.json, kartlar/polinomiki.json"""
import sys,os,json
HD=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,os.path.join(HD,'..')); sys.path.insert(0,os.path.join(HD,'..','tyt-mat'))
import _hafif_mat as H
from _hafif_mat import mk,kart,tablo_svg,B,A
from ortak import Parti
from cizim import tikz_svg
import sympy as sp
x=sp.symbols('x')
H.KONU='Polinomlar'
UK='amat|Polinomlar'
P=Parti('polinomiki','Polinomlar',UK,ders='AYT Matematik',idon='aytmat')
KY='ÖSYM 2018–2025 AYT Matematik (polinom soruları; yalnız mantık) · MEB 11. sınıf'
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)
def fig(body,font='\\small'): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font='+font+']\n'+body+'\n\\end{tikzpicture}')
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)
def S(e): return int(e)
def ms(v): return str(v).replace('-','−')
SIRA=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
def sirala(vals): return [s for s in SIRA if s in vals]

# ---------- bilgi kutuları (örnekler soruların sayılarından bağımsız) ----------
POL=B('Polinom','a₀ + a₁x + a₂x² + … + aₙxⁿ biçimindeki, x’in kuvvetleri negatif ya da kesirli olmayan ifadeye polinom denir. Polinomların toplamı ve çarpımı da polinomdur; bir polinomu başka bir polinoma bölmek ise her zaman polinom vermez. Örnek: x + 1/x polinom değildir, (x − 1)(x + 4) polinomdur')
DER=B('Derece kuralları','Sıfırdan farklı P ve Q için der[P·Q] = der[P] + der[Q]; der[P(Q(x))] = der[P]·der[Q]; der[P(xᵏ)] = k·der[P] olur. Örnek: der[A] = 2 ve der[B] = 4 ise der[A(B(x))] = 8’dir')
DEG=B('Değer ve katsayı','P(a) değeri, x yerine a yazılarak bulunur. Bir polinomun katsayılar toplamı x = 1, sabit terimi x = 0 değerinden okunur; polinom başka bir ifadenin içine yazılmışsa aynı kural o ifade üzerinden uygulanır')
KAL=B('Kalan teoremi','P(x)’in x − a ile bölümünden kalan P(a)’dır. Bölen ikinci dereceden ise kalan en çok birinci derecedendir: bölenin kökleri için P(kök) = kalan(kök) yazılır. Örnek: P(x) = (x − 3)·Q(x) + 8 ise P(3) = 8’dir')
KAT=B('Çift katlı bölen','P(x) = (x − a)²·Q(x) + mx + n ise P(a) = ma + n olur; bölümü bilinmeyen bir polinomla çarpılan terim, bölenin kökünde sıfır değerini alır. Örnek: kalan R(x) = mx + n ise R(a) = P(a)’dır')
BOL=B('Bölme eşitliği','P(x) = B(x)·Q(x) + K(x) eşitliğinde der[K] < der[B] olur. P(x) bu eşitlikten açılarak katsayı karşılaştırması yapılır. Örnek: B(x) = x − 1, Q(x) = x + 2, K = 5 ise P(x) = x² + x + 3 olur')
GRF=B('Grafikten polinom','Grafiğin x eksenini kestiği noktalar kökleri verir; eksene değip dönen kök çift katlı, kesip geçen kök tek katlıdır. P(x) = a(x − r₁)(x − r₂)… yazılıp bir ek veriyle bilinmeyen bulunur. Örnek: baş katsayısı 1 olan ikinci dereceden P için kökler 2 ve 5 ise P(x) = (x − 2)(x − 5)’tir')
ISR=B('İşaret incelemesi','Bir polinomun işareti kökünde, kök tek katlıysa değişir; çift katlıysa değişmez. Kesirli eşitsizlikte paydanın kökü çözüm kümesine alınmaz. Örnek: (x − 2)/(x + 1) ≤ 0 için −1 < x ≤ 2’dir')
KOK=B('Kökler ve katsayılar','Üçüncü dereceden x³ + ax² + bx + c polinomunun kökleri r₁, r₂, r₃ ise r₁ + r₂ + r₃ = −a, r₁r₂ + r₁r₃ + r₂r₃ = b, r₁r₂r₃ = −c olur. Örnek: x³ + 3x² + px + q için kökler toplamı −3’tür')
OZD=B('Özdeşlik','İki polinom her x için eşitse aynı dereceli terimlerin katsayıları ayrı ayrı eşittir. Örnek: (x + m)(x + n) = x² + 7x + 12 ise m + n = 7 ve mn = 12’dir')
CIFT=B('Eşitsizlik ve çift katlı kök','Her x için N(x) ≥ 0 olan bir polinom, sıfır olduğu noktalarda eksene değer; bu yüzden sıfır noktaları çift katlı köktür. Örnek: her x için x² − 2x + 1 ≥ 0 ve eşitlik yalnız x = 1’de sağlanır, çünkü x² − 2x + 1 = (x − 1)²’dir')
TAN=B('Tanımlı işlem','Tanımı verilen bir işlemde önce x yerine verilen değer yazılır, sonra bileşke ya da çarpım adım adım hesaplanır; bir polinomun x − a ile bölümünden kalan, polinomun x = a değeridir. Örnek: (A ⊕ B)(x) = A(x) + B(B(x)) ise (A ⊕ B)(0) = A(0) + B(B(0))’dır')
CIFTTEK=B('Çift ve tek ayrıştırma','P(x) + P(−x) yalnız çift dereceli terimleri 2 katıyla, P(x) − P(−x) yalnız tek dereceli terimleri 2 katıyla verir. Birincinin sabit terimi 2P(0), ikincinin sabit terimi 0’dır. Örnek: P(x) = x² + 3x ise P(x) + P(−x) = 2x², P(x) − P(−x) = 6x’tir')

# ---------- kartlar ----------
kartla('K-APLN2-01','Derece ve polinom kavramı','Verilen derece eşitliklerinden bilinmeyen dereceler bulunur; bileşke ve x’in kuvveti içeren yerine yazmalarda derece çarpılır, çarpımda toplanır; bir ifadenin polinom olup olmadığı terimlerin üslerine bakılarak anlaşılır.','Bileşkede dereceleri toplamak; x yerine xᵏ yazılınca dereceyi k ile çarpmayı unutmak; bölme içeren ifadeyi polinom saymak.','kolay','düz',3,'ik-derece','Derece ve polinom kavramı')
kartla('K-APLN2-02','Değer ve bileşke','Tablo, işlem şeması ya da tanımlı işlemde x yerine yazılan ifade adım adım uygulanır; katsayılar toplamı ve sabit terim uygun noktadaki değerden okunur.','Adımların sırasını karıştırmak; yer değiştirmeyi ters işaretle yapmak; katsayılar toplamı için yanlış noktayı seçmek.','orta','tablo',4,'ik-deger','Değer ve bileşke')
kartla('K-APLN2-03','Grafikten polinom','Grafikteki kökler, kök katlılığı ve verilen bir değerle polinom çarpanlı yazılır; gizli kalan kök bir değerden bulunur; eşitsizlikte işaret incelemesi yapılır.','Çift katlı kökü tek saymak; gizli kökün işaretini ters bulmak; paydanın kökünü çözüme katmak.','zor','grafik',5,'ik-grafik','Grafikten polinom')
kartla('K-APLN2-04','Kalan teoremi ve çift katlı bölen','Birden çok bölenin kalan bilgisi, kalan polinomun kök değerleriyle birleştirilir; çift katlı bölende kalan, bölenin kökündeki değer ve katsayı düzenlemesiyle yazılır.','Kalanın derecesini yanlış almak; çift katlı bölende kalanı doğrudan sabit saymak; kök yerine işaret hatası yapmak.','zor','yeni nesil',5,'ik-kalan','Kalan teoremi ve çift katlı bölen')
kartla('K-APLN2-05','Bölme eşitliği ve katsayılar','Bölüm, bölen ve kalan çarpılıp toplanarak bölünen polinomun katsayıları bulunur; bilinen kalan değerleriyle ikinci dereceden bir polinomun katsayıları kurulur.','Kalanı eklemeyi unutmak; açılımda terimi eksik toplamak; bölen ve kalanın işaretini karıştırmak.','orta','şekilli',4,'ik-bolme','Bölme eşitliği ve katsayılar')
kartla('K-APLN2-06','Kökler ve katsayılar','Kökler arasındaki bir koşul (eşit aralık, bilinen değer) kökleri belirler; kök toplamı ve çarpımı katsayılarla eşlenir; ikinci derecede tek kök koşulu için en küçük değer kullanılır.','Kökler toplamının işaretini ters almak; kareler toplamını toplamın karesiyle karıştırmak; tek kök koşulunu işaretiyle yanlış yazmak.','zor','şekilli',4,'ik-kok','Kökler ve katsayılar')
kartla('K-APLN2-07','Özdeşlik ve eşitsizlikten polinom','Çarpım ve yer değiştirmeden doğan özdeşliklerde katsayılar eşlenir; her x için sağlanan bir eşitsizlik ve eşitlik noktaları polinomu çift katlı çarpan olarak verir; çift–tek ayrıştırma öncülleri sınanır.','Çapraz terimleri atlamak; eşitlik noktalarını tek katlı almak; öncülü seçilen bir değerle sınayıp genellemek.','zor','öncüllü',4,'ik-ozdes','Özdeşlik ve eşitsizlikten polinom')

# ================= şekil yardımcıları =================
def egri(f,a,b,n=140,sx=1,sy=1):
    return ' '.join(f'({xx*sx:.3f},{yy*sy:.3f})' for xx,yy in [(a+(b-a)*i/n, float(f(a+(b-a)*i/n))) for i in range(n+1)])
def eksen(x0,x1,y0,y1,sx,sy,xt,xlab='$x$',ylab='$y$',fs='\\footnotesize'):
    o=[]
    for i in xt: o.append(f'\\draw[gray!35,thin] ({i*sx:.3f},{y0*sy:.3f}) -- ({i*sx:.3f},{y1*sy:.3f});')
    o.append(f'\\draw[-{{Stealth}},thick] ({x0*sx:.3f},0) -- ({x1*sx:.3f},0) node[right] {{{xlab}}};')
    o.append(f'\\draw[-{{Stealth}},thick] (0,{y0*sy:.3f}) -- (0,{y1*sy:.3f}) node[above] {{{ylab}}};')
    for i in xt:
        if i!=0: o.append(f'\\node[font={fs},fill=white,inner sep=1pt] at ({i*sx:.3f},-0.42) {{${i}$}};')
    return '\n'.join(o)

# ============================ SORULAR ============================
# ---- 0001 · kolay · düz · derece (bileşke, x² yerine yazma)
p,qd=sp.symbols('p q')
sol=sp.solve([2*p+qd-13,p+2*qd-11],[p,qd]); pp,qq=sol[p],sol[qd]; assert (pp,qq)==(5,3)
dg=S(pp*qq); e1=S(pp*pp); e2=S(2*pp); e3=S(2*pp*qq); e4=S(pp**qq); e2=S(qq**pp)
assert (dg,e1,e2,e3,e4)==(15,25,243,30,125) and len({dg,e1,e2,e3,e4})==5
q('0001',tipId='ik-derece',tip='Derece ve polinom kavramı',z='kolay',alt='Derece kuralları',kaz='Derece eşitliklerinden polinomların derecesini bulur ve bileşkenin derecesini hesaplar.',kalip='düz',
 kart='K-APLN2-01 · iki derece denklemi, bileşke',
 metin='P(x) ve Q(x) sıfırdan farklı polinomlardır.\nder[P(x²)·Q(x)] = 13\nder[P(x)·Q(x²)] = 11\nolduğuna göre, der[P(Q(x))] kaçtır?',
 dogru=dg,yan=[(e1,'P(Q(x)) yerine P(P(x)) düşünüp 5·5 almış.','dikkat'),(e2,'İç polinomun derecesini üs, dıştakini taban alıp 3⁵ bulmuş.','bilgi'),(e3,'Bileşkenin derecesini 2·5·3 olarak yazıp x² yerine yazmanın katını da çarpmış.','bilgi'),(e4,'Dıştaki polinomun derecesini taban, içtekini üs alıp 5³ bulmuş.','bilgi')],
 istenen='der[P(Q(x))] değeri.',ip=['Önce P ve Q’nun derecelerini iki bilinmeyenli bir sistemle bul.'],bilgi=[DER],
 ad=[A('Dereceleri kur','der[P] = p, der[Q] = q olsun; x² yerine yazmak dereceyi iki katına çıkarır.','2p + q = 13 ve p + 2q = 11'),A('Çöz','İkinci denklemi 2 ile çarpıp birinciden çıkar: 3p = 15.','p = 5 ve q = 3'),A('Bileşke','Bileşkenin derecesi derecelerin çarpımıdır.','der[P(Q(x))] = 5·3 = 15')],
 puf='Bileşkede dereceler çarpılır, çarpımda toplanır; x yerine x² yazmak da bir bileşkedir.')

# ---- 0002 · kolay · tablo · P(2x−1) katsayılar toplamı + sabit terim
tv={-1:7,0:3,1:-2,2:4,3:9}
SK=tablo_svg(['x']+[ms(k) for k in tv],[['P(x)']+[ms(v) for v in tv.values()]])
dg=tv[1]+tv[-1]; assert dg==5
e1=tv[1]+tv[0]; e2=tv[2]+tv[0]; e3=tv[2]+tv[-1]; e4=tv[1]*tv[-1]
assert (e1,e2,e3,e4)==(1,7,11,-14) and len({dg,e1,e2,e3,e4})==5
q('0002',tipId='ik-deger',tip='Değer ve bileşke',z='kolay',alt='Katsayılar toplamı',kaz='P(ax + b) biçimindeki polinomun katsayılar toplamını ve sabit terimini tablodan okuyarak bulur.',kalip='tablo',
 kart='K-APLN2-02 · tablo, P(2x − 1)',
 metin='Aşağıdaki tabloda, P(x) polinomunun bazı x değerleri için aldığı değerler verilmiştir.\nBuna göre, P(2x − 1) polinomunun katsayılar toplamı ile sabit teriminin toplamı kaçtır?',
 dogru=dg,yan=[(e1,'Sabit terimi P(0) almış (−1 kaymasını işlememiş): −2 + 3.','dikkat'),(e2,'Katsayılar toplamını P(2), sabit terimi P(0) saymış: 4 + 3.','islem'),(e3,'Katsayılar toplamını P(2), sabit terimi P(−1) saymış: 4 + 7.','islem'),(e4,'İki değeri toplamak yerine çarpmış: (−2)·7.','bilgi')],
 istenen='Katsayılar toplamı ile sabit terimin toplamı.',ip=['Katsayılar toplamı için x yerine 1, sabit terim için x yerine 0 yaz.'],bilgi=[DEG],sekil=SK,
 ad=[A('Katsayılar toplamı','x = 1 için 2x − 1 = 1.','P(1) = −2'),A('Sabit terim','x = 0 için 2x − 1 = −1.','P(−1) = 7'),A('Topla','İki değer toplanır.','−2 + 7 = 5')],
 puf='Katsayılar toplamı için x = 1, sabit terim için x = 0 yazılır; tablodaki değere ulaşmak için içteki ifadeyi hesapla.')

# ---- 0003 · orta · grafik · çift katlı kök + P(7)
f3=lambda t:(t+1)**2*(t-5)**2
sx,sy=0.85,0.034
g=[eksen(-2,6.6,-6,92,sx,sy,[-1,5])]
g.append(f'\\draw[blue!75!black,very thick] plot[smooth] coordinates {{{egri(f3,-1.8,5.8,160,sx,sy)}}};')
for r in (-1,5): g.append(f'\\fill[orange!90!black] ({r*sx:.3f},0) circle (0.1);')
SK=fig('\n'.join(g))
P3=(x+1)**2*(x-5)**2; dg=S(P3.subs(x,7)); assert dg==256
e1=S(((x+1)*(x-5)).subs(x,7)); e2=S(((x+1)**2).subs(x,7)); e3=S(((x+1)**2*(x-5)).subs(x,7)); e4=S(((x-1)**2*(x-5)**2).subs(x,7))
assert (e1,e2,e3,e4)==(16,64,128,144) and len({dg,e1,e2,e3,e4})==5
q('0003',tipId='ik-grafik',tip='Grafikten polinom',z='orta',alt='Çift katlı kök',kaz='Grafiğin eksene değdiği noktaları çift katlı kök olarak yorumlayıp polinomu yazar.',kalip='grafik',
 kart='K-APLN2-03 · iki çift katlı kök',
 metin='Şekilde, baş katsayısı 1 olan dördüncü dereceden P(x) polinomunun grafiği verilmiştir; grafik x eksenine yalnızca işaretli noktalarda değmektedir.\nBuna göre, P(7) kaçtır?',
 dogru=dg,yan=[(e1,'Kökleri tek katlı sayıp ikinci dereceden polinom yazmış: (8)(2).','bilgi'),(e2,'Yalnız −1 kökünü çarpan olarak yazıp (x + 1)² almış.','dikkat'),(e3,'Dördüncü derece olduğunu gözetmeyip 5 kökünü tek katlı almış: (8)²·2.','bilgi'),(e4,'−1 kökünü ters işaretle yazmış: (x − 1)²(x − 5)².','islem')],
 istenen='P(7) değeri.',ip=['Grafik eksene değiyorsa o kök kaç kez sayılır; derece ile karşılaştır.'],bilgi=[GRF],sekil=SK,
 ad=[A('Kök katlılığı','Grafik −1 ve 5’te eksene değip dönüyor; iki kök de çift katlı.','Çarpanlar (x + 1)² ve (x − 5)²'),A('Polinomu yaz','Derece 4, baş katsayı 1.','P(x) = (x + 1)²(x − 5)²'),A('Değer','x = 7 yazılır.','P(7) = 8²·2² = 256')],
 puf='Eksene değen kök çift katlıdır; iki çift katlı kök dördüncü dereceyi doldurur.')

# ---- 0004 · kolay · öncüllü · polinom mu
dogru='I ve III'; vals=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III']
q('0004',tipId='ik-derece',tip='Derece ve polinom kavramı',z='kolay',alt='Polinom kavramı',kaz='Verilen ifadelerin polinom olup olmadığını üslere ve işlemlere bakarak belirler.',kalip='öncüllü',
 kart='K-APLN2-01 · polinom olma koşulu',
 metin='I.   A(x) = 4x³ − √5·x + 1\nII.  B(x) = x² + 6/x\nIII. C(x) = (x + 2)(x² − 1)\nBuna göre, yukarıdaki ifadelerden hangileri x değişkenine bağlı bir polinomdur?',
 dogru=dogru,yan=[('Yalnız I','C(x)’i çarpım biçiminde olduğu için polinom saymamış.','bilgi'),('Yalnız II','Yalnız 6/x ifadesini polinom, diğerlerini polinom değil saymış.','bilgi'),('Yalnız III','−√5·x terimindeki kök yüzünden A’yı polinom saymamış.','bilgi'),('I ve II','6/x terimini polinom saymış (x⁻¹ negatif üslüdür), C’yi saymamış.','bilgi')],
 istenen='Polinom olan ifadeler.',ip=['Her terimde x’in üssüne bak; katsayının kök içermesi ile x’in kök ya da payda içermesini ayır.'],bilgi=[POL],sira=sirala(vals),
 ad=[A('I. ifade','Katsayı √5 sayıdır, x’in üsleri 3 ve 1.','Polinomdur'),A('II. ifade','6/x = 6x⁻¹ negatif üslüdür.','Polinom değildir'),A('III. ifade','Çarpım açılınca x³ + 2x² − x − 2 olur.','Polinomdur')],
 puf='Katsayıda kök olabilir; x’in kuvveti negatif ya da kesirli olamaz.')

# ---- 0005 · orta · düz · kalan, P(x+1)·P(x)
R5=x+4
P2=S(R5.subs(x,2)); P3v=S(R5.subs(x,3)); P1=S(R5.subs(x,1))
dg=P3v*P2; e1=P3v+P2; e2=P1*P2; e3=P2*P2; e4=P3v*P3v
assert (P2,P3v,dg)==(6,7,42) and (e1,e2,e3,e4)==(13,30,36,49) and len({dg,e1,e2,e3,e4})==5
q('0005',tipId='ik-kalan',tip='Kalan teoremi ve çift katlı bölen',z='orta',alt='Kalan ve bileşke',kaz='İkinci dereceden bölenle kalandan P’nin kök değerlerini bulup kaydırılmış polinomun kalanını hesaplar.',kalip='düz',
 kart='K-APLN2-04 · kalan x + 4, P(x+1)·P(x)',
 metin='P(x) polinomunun x² − 5x + 6 ile bölümünden kalan x + 4 tür.\nBuna göre, P(x + 1)·P(x) polinomunun x − 2 ile bölümünden kalan kaçtır?',
 dogru=dg,yan=[(e1,'Çarpım yerine toplam almış: 7 + 6.','dikkat'),(e2,'P(x + 1)’de x = 2 yazarken kaydırmayı ters yapıp P(1) = 1 + 4 = 5 almış.','islem'),(e3,'P(x + 1)’de de P(2) değerini kullanıp kaydırmayı unutmuş: 6·6.','dikkat'),(e4,'İki çarpanı da P(3) = 7 almış: 7·7.','dikkat')],
 istenen='Kalan değeri.',ip=['Bölenin kökleri 2 ve 3’tür; P’nin bu noktalardaki değerleri kalan polinomundan gelir.'],bilgi=[KAL],
 ad=[A('Kalan polinomu','x² − 5x + 6 = (x − 2)(x − 3); kök değerlerinde P ile kalan aynıdır.','P(2) = 2 + 4 = 6, P(3) = 3 + 4 = 7'),A('x − 2 ile kalan','Çarpımın x = 2 değeri alınır.','P(3)·P(2)'),A('Çarpım','Değerler yazılır.','7·6 = 42')],
 puf='Kalan istenen bir polinomun x − a ile bölümünden kalan, o polinomun x = a değeridir; iç polinomlarda x yerine a yazmayı unutma.')

# ---- 0006 · orta · öncüllü · P−Q tam bölünür
dogru='I ve II'; vals=['Yalnız I','I ve II','I ve III','II ve III','I, II ve III']
q('0006',tipId='ik-kalan',tip='Kalan teoremi ve çift katlı bölen',z='orta',alt='Kalan teoremi öncülleri',kaz='İki polinomun farkının bir çarpanla tam bölünmesinden kalan değerlerin eşitliğini çıkarır ve öncülleri sınar.',kalip='öncüllü',
 kart='K-APLN2-04 · P − Q tam bölünüyor',
 metin='P(x) ve Q(x) polinomları için P(x) − Q(x) polinomu x − 2 ile tam bölünmektedir.\nBuna göre,\nI.   P(x) ile Q(x) polinomlarının x − 2 ile bölümünden kalanlar eşittir.\nII.  P(x) + Q(x) polinomunun x − 2 ile bölümünden kalan 2·P(2) dir.\nIII. P(x)/Q(x) ifadesi bir polinomdur.\nifadelerinden hangileri her zaman doğrudur?',
 dogru=dogru,yan=[('Yalnız I','II. öncülde toplamın kalanının P(2) + Q(2) = 2P(2) olduğunu görmemiş.','bilgi'),('I ve III','Tam bölünmeyi, P’nin Q’ya bölünmesi gibi yorumlayıp III’ü doğru saymış; II’yi saymamış.','bilgi'),('II ve III','I. öncülün kalanların eşitliğini ifade ettiğini fark etmemiş; III’ü doğru saymış.','dikkat'),('I, II ve III','Farkın bölünmesini oranın polinom olmasına genellemiş.','bilgi')],
 istenen='Her zaman doğru olan öncüller.',ip=['Tam bölünme, farkın x = 2 değerinin ne olduğunu söyler.'],bilgi=[KAL],sira=sirala(vals),
 ad=[A('Koşulu yorumla','Fark x − 2 ile tam bölünür; farkın x = 2 değeri sıfırdır.','P(2) − Q(2) = 0'),A('I ve II','Kalanlar P(2) ve Q(2); toplamın kalanı P(2) + Q(2).','P(2) = Q(2): I doğru, II doğru'),A('III','P(x) = x, Q(x) = x² − 2 için P(2) = Q(2) = 2 iken P/Q polinom değildir.','III her zaman doğru değil')],
 puf='Tam bölünme farkın kök değerini sıfır yapar; kalan değerleri üzerinden çalış.')

# ---- 0007 · orta · şekilli · işlem şeması
Pm=x**2+4*x-3
Qm=Pm.subs(x,2-x); Sm=sp.expand((x+1)*Qm); Rm=sp.expand(Sm.subs(x,x-1))
dg=S(Rm.subs(x,1)); assert dg==9
e1=S(Sm.subs(x,2)); e2=S(Sm.subs(x,1)); e3=S((x*Pm.subs(x,x-3)).subs(x,1)); e4=S(Rm.subs(x,0))
assert (e1,e2,e3,e4)==(-9,4,-7,0) and len({dg,e1,e2,e3,e4})==5
g=['\\tikzset{kt/.style={draw,rounded corners=3pt,thick,align=center,minimum width=6.4cm,minimum height=0.8cm}}',
 '\\node[kt,fill=blue!12,draw=blue!70!black] (a) at (0,0) {$P(x) = x^2 + 4x - 3$};',
 '\\node[kt,fill=orange!18,draw=orange!85!black] (b) at (0,-1.6) {\\textbf{1. adım:} $x$ yerine $2 - x$ yazılır};',
 '\\node[kt,fill=orange!18,draw=orange!85!black] (c) at (0,-3.2) {\\textbf{2. adım:} sonuç $(x + 1)$ ile çarpılır};',
 '\\node[kt,fill=orange!18,draw=orange!85!black] (d) at (0,-4.8) {\\textbf{3. adım:} $x$ yerine $x - 1$ yazılır};',
 '\\node[kt,fill=green!15,draw=green!50!black] (e) at (0,-6.4) {$R(x)$};',
 '\\foreach \\u/\\v in {a/b,b/c,c/d,d/e} \\draw[-{Stealth},thick] (\\u) -- (\\v);']
SK=fig('\n'.join(g))
q('0007',tipId='ik-deger',tip='Değer ve bileşke',z='orta',alt='İşlem şeması',kaz='Ardışık işlemlerle elde edilen polinomun katsayılar toplamını adım adım hesaplar.',kalip='şekilli',
 kart='K-APLN2-02 · üç adımlı işlem şeması',
 metin='Şekildeki işlem şemasında giriş polinomu, okların yönünde üç adım uygulanarak R(x) polinomuna dönüştürülmektedir.\nBuna göre, R(x) polinomunun katsayılar toplamı kaçtır?',
 dogru=dg,yan=[(e1,'3. adımda x yerine x + 1 yazmış: S(2) = 3·P(0) = −9.','islem'),(e2,'3. adımı hiç uygulamamış: S(1) = 2·P(1) = 4.','dikkat'),(e3,'1. adımda x yerine x − 2 yazmış: R(1) = P(−2) = −7.','islem'),(e4,'Katsayılar toplamı yerine sabit terimi (x = 0) hesaplamış.','bilgi')],
 istenen='R(x) polinomunun katsayılar toplamı.',ip=['Katsayılar toplamı R(1) dir; adımları sondan başa doğru uygula.'],bilgi=[DEG],sekil=SK,
 ad=[A('R(1)’i aç','3. adımdan: R(x) = S(x − 1); S(x) = (x + 1)·Q(x).','R(1) = S(0) = 1·Q(0)'),A('Q(0)','Q(x) = P(2 − x) olduğundan Q(0) = P(2).','P(2) = 4 + 8 − 3'),A('Sonuç','Değer hesaplanır.','R(1) = 9')],
 puf='Katsayılar toplamı için x = 1 yaz; yer değiştirmeli adımları tersten uygulayarak polinomu hiç açmadan değeri bul.')

# ---- 0008 · orta · tablo · kalanlardan ikinci dereceden polinom
a8=2; P8=a8*x**2-x+3
r1=S(P8.subs(x,1)); rm=S(P8.subs(x,-1)); dg=S(P8.subs(x,3)); assert (r1,rm,dg)==(4,6,18)
e1=S((a8*x**2+x+3).subs(x,3)); e2=S((-x+5).subs(x,3)); e3=S((x**2-x+4).subs(x,3)); e4=S((2*x**2-2*x+4).subs(x,3))
assert (e1,e2,e3,e4)==(24,2,10,16) and len({dg,e1,e2,e3,e4})==5
SK=tablo_svg(['Bölen','x − 1','x + 1'],[['Kalan',str(r1),str(rm)]])
q('0008',tipId='ik-bolme',tip='Bölme eşitliği ve katsayılar',z='orta',alt='Kalanlardan polinom kurma',kaz='Bölenlerin kalanlarını P(1) ve P(−1) olarak yorumlayıp ikinci dereceden polinomu kurar.',kalip='tablo',
 kart='K-APLN2-05 · tablo, iki kalan + baş katsayı',
 metin='Baş katsayısı 2 olan ikinci dereceden P(x) polinomunun x − 1 ve x + 1 ile bölümünden kalanlar aşağıdaki tabloda verilmiştir.\nBuna göre, P(x) polinomunun x − 3 ile bölümünden kalan kaçtır?',
 dogru=dg,yan=[(e1,'Tablodaki kalanları yer değiştirip P(1) = 6, P(−1) = 4 almış: P(x) = 2x² + x + 3.','dikkat'),(e2,'İkinci derece olduğunu görmeyip iki noktadan doğru geçirmiş: P(x) = −x + 5.','bilgi'),(e3,'Baş katsayıyı 1 alıp P(x) = x² − x + 4 bulmuş.','dikkat'),(e4,'b için P(1) − P(−1) = 2b yerine b = −2 alıp P(x) = 2x² − 2x + 4 bulmuş.','islem')],
 istenen='P(3) değeri.',ip=['Kalanlar P’nin iki noktadaki değeridir; polinomu P(x) = 2x² + bx + c biçiminde yaz.'],bilgi=[KAL,BOL],sekil=SK,
 ad=[A('Denklemleri yaz','Kalanlar P(1) = 4 ve P(−1) = 6.','2 + b + c = 4 ve 2 − b + c = 6'),A('Çöz','Taraf tarafa çıkar ve topla.','b = −1, c = 3'),A('P(3)','x = 3 yazılır.','18 − 3 + 3 = 18')],
 puf='Kalan teoremiyle her kalan bir değerdir; ikinci dereceden polinom, baş katsayı ve iki değerle tamamen belirlenir.')

# ---- 0009 · orta · şekilli · bölme şeması
Bq=(x**2-2*x+1); Qq=x+4; Rr=3*x-2
Pd=sp.expand(Bq*Qq+Rr); cf=sp.Poly(Pd,x).all_coeffs(); assert cf==[1,2,-4,2]
a9,b9,c9=cf[1],cf[2],cf[3]; dg=a9*b9*c9; assert dg==-16
def abc(Pp): c=sp.Poly(sp.expand(Pp),x).all_coeffs(); return c[1]*c[2]*c[3]
e1=abc(Bq*Qq); e2=abc(Bq*Qq-Rr)
# işlem hatası: −2x·4 = −8x yazıp +x teriminin 4 ile çarpımını eklemeyi unutmuş
cc=[1,4-2,-8+3,4-2]; e3=cc[1]*cc[2]*cc[3]
e4=abc(sp.expand((x**2+2*x+1)*Qq+Rr))
assert (e1,e2,e3,e4)==(-56,-120,-20,144) and len({dg,e1,e2,e3,e4})==5
g=['\\node[anchor=east,font=\\large] at (4.0,0) {$x^3 + ax^2 + bx + c$};',
 '\\draw[thick,blue!70!black] (4.2,0.45) -- (4.2,-1.0) -- (7.6,-1.0);',
 '\\node[anchor=west,font=\\large] at (4.4,0) {$x^2 - 2x + 1$};',
 '\\node[anchor=west,font=\\large,text=orange!80!black] at (4.4,-0.6) {$x + 4$};',
 '\\node[anchor=east,font=\\small] at (0.2,-1.5) {Kalan:};',
 '\\node[anchor=west,font=\\large,text=green!45!black] at (0.3,-1.5) {$3x - 2$};',
 '\\draw[thick] (0.2,-1.0) -- (4.0,-1.0);',
 '\\node[font=\\footnotesize,text=gray!60!black] at (2.1,-0.55) {bölünen};\\node[font=\\footnotesize,text=gray!60!black] at (6.0,0.5) {bölen};\\node[font=\\footnotesize,text=gray!60!black] at (7.0,-1.3) {bölüm};']
SK=fig('\n'.join(g))
q('0009',tipId='ik-bolme',tip='Bölme eşitliği ve katsayılar',z='orta',alt='Bölme düzeninden katsayı',kaz='Bölme işleminin bölen, bölüm ve kalanından bölünen polinomun katsayılarını bulur.',kalip='şekilli',
 kart='K-APLN2-05 · bölme şeması, a·b·c',
 metin='Şekilde, üçüncü dereceden bir polinomun ikinci dereceden bir polinoma bölünmesi gösterilmiştir.\nBuna göre, a·b·c çarpımı kaçtır?',
 dogru=dg,yan=[(e1,'Kalanı eklemeyi unutup bölen ile bölümün çarpımından a = 2, b = −7, c = 4 bulmuş.','dikkat'),(e2,'Kalanı çıkarmış: P(x) = x³ + 2x² − 10x + 6.','islem'),(e3,'Çarpımda 1·x terimini hesaba katmamış: b = −8 + 3 = −5 ve c = 2.','islem'),(e4,'Bölenin işaretlerini ters yazıp (x² + 2x + 1)(x + 4) + (3x − 2) açmış.','dikkat')],
 istenen='a·b·c değeri.',ip=['Bölünen, bölen ile bölümün çarpımına kalanın eklenmesiyle bulunur.'],bilgi=[BOL],sekil=SK,
 ad=[A('Bölünen','Bölünen = bölen·bölüm + kalan.','(x² − 2x + 1)(x + 4) + (3x − 2)'),A('Aç','Çarpım açılıp kalan eklenir.','x³ + 2x² − 4x + 2'),A('Katsayılar','a = 2, b = −4, c = 2.','a·b·c = −16')],
 puf='Bölme şemasını eşitliğe çevir: bölünen = bölen·bölüm + kalan; sonra katsayıları karşılaştır.')

# ---- 0010 · orta · düz · P(x+2) verilip P(5−x)
P10=sp.expand((x-2)**2+3*(x-2)+5); assert P10==x**2-x+3
dg=S(P10.subs(x,4)); e1=S((x**2+3*x+5).subs(x,4)); e2=S(P10.subs(x,5)); e3=S(sp.expand((x+2)**2+3*(x+2)+5).subs(x,4)); e4=S(P10.subs(x,1))
assert (dg,e1,e2,e3,e4)==(15,33,23,59,3) and len({dg,e1,e2,e3,e4})==5
q('0010',tipId='ik-deger',tip='Değer ve bileşke',z='orta',alt='Yer değiştirme',kaz='P(x + a) verildiğinde P(b − x) polinomunun katsayılar toplamını yer değiştirmeyle bulur.',kalip='düz',
 kart='K-APLN2-02 · P(x+2) verilmiş, P(5−x)',
 metin='Gerçel katsayılı P(x) polinomu için\nP(x + 2) = x² + 3x + 5\neşitliği her x gerçel sayısı için sağlanmaktadır.\nBuna göre, P(5 − x) polinomunun katsayılar toplamı kaçtır?',
 dogru=dg,yan=[(e1,'P(x)’i x² + 3x + 5 almış (kaydırmayı yapmamış): P(4) = 33.','dikkat'),(e2,'x = 1 için 5 − 1 yerine 5 almış: P(5) = 23.','dikkat'),(e3,'Kaydırmayı ters yapmış: P(x) = x² + 7x + 15 ve P(4) = 59.','islem'),(e4,'P(5 − x)’te x = 1 yerine yanlışlıkla P(1) hesaplamış.','bilgi')],
 istenen='Katsayılar toplamı.',ip=['Aranan toplamı veren değeri belirle; verilen eşitlikte x’e uygun bir değer vermek yeter.'],bilgi=[DEG],
 ad=[A('Katsayılar toplamı','P(5 − x)’te x = 1 için 5 − x = 4.','P(4)'),A('Eşitlikte yer değiştir','x + 2 = 4 için x = 2.','P(4) = 2² + 3·2 + 5'),A('Hesapla','Değer bulunur.','4 + 6 + 5 = 15')],
 puf='Verilen kaydırılmış eşitlikte x’e uygun değer vererek istenen noktayı yakala; polinomu açmana gerek yok.')

# ---- 0011 · zor · grafik · eşitsizlik
f11=lambda t:-(t+3)*t**2*(t-2)
sx,sy=0.95,0.07
def kok(lo,hi,yv):
    for _ in range(60):
        m=(lo+hi)/2
        if (f11(lo)-yv)*(f11(m)-yv)<=0: hi=m
        else: lo=m
    return (lo+hi)/2
xl=kok(-4.5,-3.0,-40); xr=kok(2.0,3.5,-40)
g=[f'\\draw[blue!75!black,very thick,{{Stealth}}-{{Stealth}}] plot[smooth] coordinates {{{egri(f11,xl,xr,200,sx,sy)}}};']
g.append(eksen(-4,3.0,-44,16,sx,sy,[-3,2]))
g.append(f'\\draw[purple!80!black,dashed,thick] ({1*sx:.3f},{-3.4*sy:.3f}) -- ({1*sx:.3f},{20*sy:.3f});')
g.append(f'\\node[purple!80!black,font=\\footnotesize,fill=white,inner sep=1pt] at ({1*sx:.3f},-0.42) {{$1$}};')
g.append('\\node[font=\\footnotesize,below left] at (0,0) {$O$};')
for r in (-3,0,2): g.append(f'\\fill[orange!90!black] ({r*sx:.3f},0) circle (0.1);')
SK=fig('\n'.join(g))
Pr=-(x+3)*x**2*(x-2)
def say(cond): return sum(1 for t in range(-4,5) if cond(t))
Pf=sp.lambdify(x,Pr)
dg=say(lambda t:t!=1 and Pf(t)/(t-1)>=0); e1=say(lambda t:Pf(t)/(t-1)>=0 if t!=1 else True); e2=say(lambda t:t!=1 and Pf(t)/(t-1)>=0 and t!=0)
e3=say(lambda t:t!=1 and Pf(t)/(t-1)<=0); e4=say(lambda t:t!=1 and Pf(t)/(t-1)>0)
assert (dg,e1,e2,e3,e4)==(4,5,3,7,1) and len({dg,e1,e2,e3,e4})==5
q('0011',tipId='ik-grafik',tip='Grafikten polinom',z='zor',alt='Grafikle kesirli eşitsizlik',kaz='Grafikten işaret incelemesi yapıp çift katlı kök ve payda koşulunu gözeterek kesirli eşitsizliğin tam sayı çözümlerini sayar.',kalip='grafik',
 kart='K-APLN2-03 · çift katlı kökte işaret, payda kökü',
 metin='Şekilde, dördüncü dereceden P(x) polinomunun grafiği verilmiştir; x = 1 doğrusu kesikli çizgiyle gösterilmiştir.\nBuna göre, P(x)/(x − 1) ≥ 0 eşitsizliğini sağlayan ve [−4, 4] aralığında bulunan kaç farklı x tam sayısı vardır?',
 dogru=dg,yan=[(e1,'Paydanın kökü olan x = 1’i de çözüm saymış.','dikkat'),(e2,'x = 0 çift katlı kökünü işaret değiştirmediği için dışarıda bırakmış; oysa eşitlik sağlanır.','dikkat'),(e3,'Eşitsizliğin yönünü ters okuyup P(x)/(x − 1) ≤ 0 çözmüş.','bilgi'),(e4,'Eşitlik durumunu (kökleri) hiç almayıp yalnız > 0 çözmüş; yalnız x = −4 kalmış.','dikkat')],
 istenen='Çözüm kümesindeki tam sayı sayısı.',ip=['Pay ve paydanın işaretlerini ayrı ayrı yazıp bölümün işaretini bul; sıfır olan noktaları ayrıca incele.'],bilgi=[ISR,GRF],sekil=SK,
 ad=[A('Payın işareti','Grafikten P(x) ≥ 0 olan aralık −3 ≤ x ≤ 2; x ≤ −3 ve x ≥ 2 için P(x) ≤ 0; x = 0’da P(0) = 0.','P ≥ 0: [−3, 2], P = 0: x = −3, 0, 2'),A('Bölümün işareti','x < 1 iken payda negatif; bölüm ≥ 0 için P(x) ≤ 0. x > 1 iken payda pozitif; P(x) ≥ 0 gerekir.','x ≤ −3 ya da x = 0 ya da 1 < x ≤ 2'),A('Tam sayıları say','[−4, 4] içinde, x = 1 hariç.','−4, −3, 0, 2 → 4')],
 puf='Çift katlı kökte işaret değişmese de pay sıfır olduğu için eşitlik sağlanır; paydanın kökü ise her zaman dışarıda kalır.')

# ---- 0012 · orta · şekilli · alan modeli, özdeşlik
a12,b12=sp.symbols('a b'); sol=sp.solve([a12+b12-5,3*a12+2*b12-11],[a12,b12]); aa,bb=sol[a12],sol[b12]; assert (aa,bb)==(1,4)
prod=sp.expand((x**2+aa*x+2)*(x**2+bb*x+3)); assert sp.Poly(prod,x).all_coeffs()==[1,5,9,11,6]
dg=S(sp.Poly(prod,x).coeff_monomial(x**2)); e1=2+3; e2=S(aa*bb); e3=2+3+S(aa+bb); e4=S((aa+bb)*aa*bb); e2=S(aa*bb)
assert (dg,e1,e2,e3,e4)==(9,5,4,10,20) and len({dg,e1,e2,e3,e4})==5
W=[2.2,1.6,1.0]; Hh=[1.7,1.2,0.9]
g=[]
cl=[['x^4','ax^3','2x^2'],['bx^3','abx^2','2bx'],['3x^2','3ax','6']]
col=[['blue!15','orange!28','green!22'],['orange!28','green!22','purple!22'],['green!22','purple!22','gray!22']]
y0=0
xs=[0,W[0],W[0]+W[1],sum(W)]; ys=[0,-Hh[0],-Hh[0]-Hh[1],-sum(Hh)]
for i in range(3):
    for j in range(3):
        g.append(f'\\draw[thick,fill={col[i][j]}] ({xs[j]},{ys[i]}) rectangle ({xs[j+1]},{ys[i+1]});')
        g.append(f'\\node[font=\\small] at ({(xs[j]+xs[j+1])/2},{(ys[i]+ys[i+1])/2}) {{${cl[i][j]}$}};')
for j,l in enumerate(['x^2','ax','2']): g.append(f'\\node[above=2pt] at ({(xs[j]+xs[j+1])/2},0) {{${l}$}};')
for i,l in enumerate(['x^2','bx','3']): g.append(f'\\node[left=3pt] at (0,{(ys[i]+ys[i+1])/2}) {{${l}$}};')
g.append(f'\\node[below=6pt,font=\\normalsize,align=center] at ({sum(W)/2},{ys[3]}) {{Alan $= x^4 + 5x^3 + c\\,x^2 + 11x + 6$}};')
SK=fig('\n'.join(g))
q('0012',tipId='ik-ozdes',tip='Özdeşlik ve eşitsizlikten polinom',z='orta',alt='Alan modeli ve özdeşlik',kaz='Alan modelindeki parçaları çarpımlarıyla yazıp katsayı eşitleyerek bilinmeyen katsayıyı bulur.',kalip='şekilli',
 kart='K-APLN2-07 · 3×3 alan modeli',
 metin='Şekilde, kenar uzunlukları x² + ax + 2 ve x² + bx + 3 olan bir dikdörtgenin alanı, parçalara ayrılarak gösterilmiştir. Alan, her x için şekildeki polinoma eşittir.\nBuna göre, c kaçtır?',
 dogru=dg,yan=[(e1,'x² teriminde yalnız 2x² ve 3x² parçalarını toplayıp ab·x² parçasını katmamış.','dikkat'),(e2,'Yalnız ab·x² parçasının katsayısını almış.','dikkat'),(e3,'2 + 3 toplamına a + b’yi de ekleyip ax³ ve bx³ parçalarının katsayılarını x² e katmış.','bilgi'),(e4,'(a + b)·ab çarpımını almış.','islem')],
 istenen='c değeri.',ip=['Aynı dereceli parçaları grupla; x³ ve x için iki denklem yazıp a ile b’yi bul.'],bilgi=[OZD],sekil=SK,
 ad=[A('x³ ve x katsayıları','x³: a + b; x: 3a + 2b.','a + b = 5 ve 3a + 2b = 11'),A('a, b','İlk denklemi 2 ile çarpıp çıkar.','a = 1, b = 4'),A('x² katsayısı','Parçalar: 2x², 3x², ab·x².','c = 2 + 3 + 4 = 9')],
 puf='Alan modelinde aynı dereceli parçalar toplanır; çapraz parça (ab·x²) en çok unutulan terimdir.')

# ---- 0013 · orta · şekilli · prizma, hacimden ayrıt
Vp=sp.expand((x+1)*(x-2)*(x+3)); assert Vp==x**3+2*x**2-5*x-6
cq=sp.quo(Vp,(x+1)*(x-2),x); assert cq==x+3
dg=S(4*(x+1+x-2+cq).subs(x,5)); e1=S(4*((x+1)+(x-2)).subs(x,5)); e2=S(4*((x+1)+(x-2)+(x-3)).subs(x,5)); e3=S(((x+1)+(x-2)+cq).subs(x,5)); e4=S(Vp.subs(x,5))
assert (dg,e1,e2,e3,e4)==(68,36,44,17,144) and len({dg,e1,e2,e3,e4})==5
g=['\\draw[thick,fill=blue!14] (0,0) rectangle (3,1.8);',
 '\\draw[thick,fill=orange!20] (0,1.8) -- (1.2,2.6) -- (4.2,2.6) -- (3,1.8) -- cycle;',
 '\\draw[thick,fill=green!18] (3,0) -- (4.2,0.8) -- (4.2,2.6) -- (3,1.8) -- cycle;',
 '\\draw[thick,dashed,gray!70!black] (0,0) -- (1.2,0.8) -- (4.2,0.8);\\draw[thick,dashed,gray!70!black] (1.2,0.8) -- (1.2,2.6);',
 '\\node[below=3pt,font=\\normalsize] at (1.5,0) {$x + 1$};',
 '\\node[left=3pt,font=\\normalsize] at (0,0.9) {$x - 2$};',
 '\\node[below right=2pt,font=\\normalsize] at (3.6,0.4) {$c$};']
SK=fig('\n'.join(g))
q('0013',tipId='ik-ozdes',tip='Özdeşlik ve eşitsizlikten polinom',z='orta',alt='Hacimden ayrıt bulma',kaz='Hacim polinomunu bilinen iki ayrıta bölerek üçüncü ayrıtı bulur ve değerini hesaplar.',kalip='şekilli',
 kart='K-APLN2-07 · hacim bölme, ayrıt toplamı',
 metin='Şekildeki dikdörtgenler prizmasının ayrıt uzunlukları cm cinsinden x + 1, x − 2 ve c polinomlarıdır. Prizmanın hacmi x³ + 2x² − 5x − 6 cm³ tür.\nBuna göre, x = 5 iken prizmanın bütün ayrıtlarının uzunlukları toplamı kaç cm dir?',
 dogru=dg,yan=[(e1,'Üçüncü ayrıtı hesaba katmamış: 4·(6 + 3).','dikkat'),(e2,'c yerine x − 3 bulmuş (işaret hatası): 4·(6 + 3 + 2).','islem'),(e3,'Dört ayrıt grubu olduğunu unutup yalnız üç ayrıtı toplamış: 6 + 3 + 8.','bilgi'),(e4,'Ayrıtlar toplamı yerine hacmi, V(5) değerini hesaplamış.','dikkat')],
 istenen='Ayrıtların uzunlukları toplamı (cm).',ip=['Önce c polinomunu hacim eşitliğinden bul; dikdörtgenler prizmasının kaç ayrıtı olduğunu düşün.'],bilgi=[OZD,BOL],sekil=SK,
 ad=[A('c’yi bul','Hacim = (x + 1)(x − 2)·c; (x + 1)(x − 2) = x² − x − 2.','c = (x³ + 2x² − 5x − 6)/(x² − x − 2) = x + 3'),A('x = 5 için ayrıtlar','x + 1, x − 2 ve x + 3.','6, 3, 8'),A('Toplam','Prizmanın 12 ayrıtı vardır; her uzunluktan 4 tane.','4·(6 + 3 + 8) = 68')],
 puf='Hacim ayrıtların çarpımıdır; bölme ya da çarpanlara ayırma ile eksik ayrıtı bul; 12 ayrıtı (her uzunluktan 4) unutma.')

# ---- 0014 · zor · şekilli · kökler eşit aralıklı
P14=x**3-6*x**2+3*x+10; assert sp.expand((x+1)*(x-2)*(x-5))==P14
dg=3+10; e1=3-10; e2=3; e3=10; e4=30
assert (dg,e1,e2,e3,e4)==(13,-7,3,10,30) and len({dg,e1,e2,e3,e4})==5
g=['\\draw[-{Stealth},thick] (-0.3,0) -- (8.2,0);',
 '\\draw[thick] (2.0,0.12) -- (2.0,-0.12) node[below=3pt] {$0$};',
 '\\foreach \\p/\\l in {0.6/r_1,3.6/r_2,6.6/r_3} {\\fill[orange!90!black] (\\p,0) circle (0.11);\\node[above=6pt,font=\\normalsize] at (\\p,0) {$\\l$};}',
 '\\node[below=3pt,font=\\normalsize] at (6.6,0) {$5$};',
 '\\draw[blue!70!black,thick,{Stealth}-{Stealth}] (0.6,0.95) -- (3.6,0.95) node[midway,above] {$d$};',
 '\\draw[blue!70!black,thick,{Stealth}-{Stealth}] (3.6,0.95) -- (6.6,0.95) node[midway,above] {$d$};']
SK=fig('\n'.join(g))
q('0014',tipId='ik-kok',tip='Kökler ve katsayılar',z='zor',alt='Kökler arasında eşit aralık',kaz='Kök toplamı ve eşit aralık koşuluyla kökleri bulup b ve c katsayılarını kök–katsayı ilişkisiyle hesaplar.',kalip='şekilli',
 kart='K-APLN2-06 · eşit aralıklı üç kök',
 metin='P(x) = x³ − 6x² + bx + c polinomunun üç gerçel kökü r₁ < r₂ < r₃ olup bu kökler sayı doğrusunda şekildeki gibi eşit aralıklarla yer almaktadır (şekil ölçekli değildir).\nBuna göre, b + c toplamı kaçtır?',
 dogru=dg,yan=[(e1,'Kökler çarpımının −c’ye eşit olduğunu unutup c = r₁r₂r₃ = −10 almış: 3 + (−10).','islem'),(e2,'Yalnız b değerini vermiş.','bilgi'),(e3,'Yalnız c değerini vermiş.','bilgi'),(e4,'Toplam yerine b·c çarpımını almış.','dikkat')],
 istenen='b + c değeri.',ip=['Şekildeki bilgiyle katsayılar birlikte üç kökü de belirler; kökleri bulmadan b ve c’ye geçme.'],bilgi=[KOK],sekil=SK,
 ad=[A('Kökler toplamı','−(−6) = 6 ve eşit aralıkta r₁ + r₃ = 2r₂.','3r₂ = 6, r₂ = 2'),A('Aralık','r₃ = 5 olduğundan d = 3.','Kökler −1, 2, 5'),A('b ve c','İkili çarpımlar toplamı b, kökler çarpımı −c.','b = −2 − 5 + 10 = 3, c = 10'),A('Toplam','b + c.','13')],
 puf='Kökleri bir kez bulunca b ve c, kök–katsayı ilişkisinin diğer iki eşitliğinden gelir; işaretlere dikkat et.')

# ---- 0015 · zor · grafik · kısmi grafik, gizli kök
f15=lambda t:(t+2)*(t-1)*(t-3)*(t+5)
P15=(x+2)*(x-1)*(x-3)*(x+5); assert S(P15.subs(x,0))==30
sx,sy=0.95,0.055
g=[eksen(-3,3.8,-33,38,sx,sy,[-2,1,3])]
g.append(f'\\draw[blue!75!black,very thick] plot[smooth] coordinates {{{egri(f15,-2.55,3.3,160,sx,sy)}}};')
for r in (-2,1,3): g.append(f'\\fill[orange!90!black] ({r*sx:.3f},0) circle (0.1);')
g.append(f'\\fill[green!50!black] (0,{30*sy:.3f}) circle (0.1);\\node[green!40!black,left=4pt,font=\\footnotesize] at (0,{30*sy:.3f}) {{$30$}};')
SK=fig('\n'.join(g))
dg=S(P15.subs(x,4)); e1=S(((x+2)*(x-1)*(x-3)*(x-5)).subs(x,4)); e2=S(((x+2)*(x-1)*(x-3)).subs(x,4)); e3=S(((x-1)*(x-3)*(x+5)).subs(x,4)); e4=S(((x+2)*(x-3)*(x+5)).subs(x,4))
assert (dg,e1,e2,e3,e4)==(162,-18,18,27,54) and len({dg,e1,e2,e3,e4})==5
q('0015',tipId='ik-grafik',tip='Grafikten polinom',z='zor',alt='Kısmi grafikten gizli kök',kaz='Grafiği kısmen verilen polinomun görünmeyen kökünü y eksenini kestiği değerden bulup istenen değeri hesaplar.',kalip='grafik',
 kart='K-APLN2-03 · görünmeyen dördüncü kök',
 metin='Şekilde, baş katsayısı 1 olan, dördüncü dereceden ve kökleri birer tam sayı olan P(x) polinomunun grafiğinin bir parçası verilmiştir.\nBuna göre, P(4) kaçtır?',
 dogru=dg,yan=[(e1,'Gizli kökü +5 bulmuş (P(0) = 30 iken işaretleri hesaba katmamış).','islem'),(e2,'Dördüncü kökü hiç aramayıp üç çarpanla hesaplamış.','bilgi'),(e3,'Kök olan −2’yi çarpan olarak yazmayıp (x − 1)(x − 3)(x + 5) almış.','dikkat'),(e4,'x = 1 kökünü çarpan olarak yazmayı unutmuş: (x + 2)(x − 3)(x + 5).','dikkat')],
 istenen='P(4) değeri.',ip=['Grafikte görünmeyen bir kök de olabilir; şekildeki ek bilgi ne işe yarar?'],bilgi=[GRF],sekil=SK,
 ad=[A('Çarpanlı biçim','Görünen kökler −2, 1, 3; dördüncü kök r.','P(x) = (x + 2)(x − 1)(x − 3)(x − r)'),A('r’yi bul','P(0) = 30 yazılır: 2·(−1)·(−3)·(−r) = −6r.','−6r = 30, r = −5'),A('P(4)','x = 4 yazılır.','(6)(3)(1)(9) = 162')],
 puf='Görünmeyen kökü, grafikteki bir değerden (burada y eksenini kestiği nokta) bul; işaret hatası bu soruda en sık yapılan hatadır.')

# ---- 0016 · zor · tablo · P(x) ≥ 2x
P16=(x-1)**2*(x-3)**2+2*x; assert P16.subs(x,1)==2 and P16.subs(x,3)==6
dg=S(P16.subs(x,5)); e1=S((2*x).subs(x,5)); e2=S(((x-1)**2*(x-3)+2*x).subs(x,5)); e3=S(((x-1)**2*(x-3)**2).subs(x,5)); e4=S(((x-1)**2*(x-3)**2-2*x).subs(x,5))
assert (dg,e1,e2,e3,e4)==(74,10,42,64,54) and len({dg,e1,e2,e3,e4})==5
SK=tablo_svg(['x','1','3'],[['P(x)','2','6']])
q('0016',tipId='ik-ozdes',tip='Özdeşlik ve eşitsizlikten polinom',z='zor',alt='Eşitsizlikten polinom',kaz='Her x için sağlanan eşitsizlik ve eşitlik noktalarından polinomu çift katlı çarpanlarla kurar.',kalip='tablo',
 kart='K-APLN2-07 · P(x) ≥ 2x, eşitlik noktaları',
 metin='Baş katsayısı 1 olan dördüncü dereceden P(x) polinomu için her x gerçel sayısında P(x) ≥ 2x eşitsizliği sağlanmaktadır. Polinomun bazı değerleri aşağıdaki tabloda verilmiştir.\nBuna göre, P(5) kaçtır?',
 dogru=dg,yan=[(e1,'Eşitlik her yerde sağlanıyormuş gibi P(5) = 2·5 almış.','bilgi'),(e2,'Çift katlı kökü (x − 3)² yerine (x − 3) yazmış: derece 3’e düşmüş.','dikkat'),(e3,'P(x) − 2x yerine P(x) = (x − 1)²(x − 3)² yazıp 2x terimini eklememiş.','dikkat'),(e4,'P(x) − 2x = T(x) çıkarımında işareti ters kullanıp P(x) = T(x) − 2x yazmış.','islem')],
 istenen='P(5) değeri.',ip=['Tablodaki değerleri 2x ile karşılaştır; ne fark ediyorsun?'],bilgi=[CIFT],sekil=SK,
 ad=[A('Yeni polinom','T(x) = P(x) − 2x; T ≥ 0 ve T(1) = T(3) = 0, baş katsayı 1, derece 4.','1 ve 3 çift katlı köktür'),A('T(x)','Dördüncü dereceyi iki çift katlı kök doldurur.','T(x) = (x − 1)²(x − 3)²'),A('P(5)','P(5) = T(5) + 2·5.','16·4 + 10 = 74')],
 puf='Her x için negatif olmayan bir polinomun sıfır noktaları çift katlıdır; eşitsizliği, farkı alarak bir polinoma çevir.')

# ---- 0017 · orta · grafik · parabol, tek kök koşulu
P17=(x-1)*(x-7)+5; assert sp.expand(P17)==x**2-8*x+12
dg=4; assert sp.discriminant(sp.expand(P17)+sp.Symbol('n'),x).subs(sp.Symbol('n'),dg)==0
vmin=S(sp.expand(P17).subs(x,4)); assert vmin==-4
e1=-4; e2=9; e3=12; e4=16
assert len({dg,e1,e2,e3,e4})==5 and e2==5-vmin and e3==S(P17.subs(x,0))
f17=lambda t:t*t-8*t+12
sx,sy=0.72,0.22
g=[f'\\draw[-{{Stealth}},thick] ({-0.6*sx:.3f},0) -- ({9.2*sx:.3f},0) node[right] {{$x$}};',f'\\draw[-{{Stealth}},thick] (0,{-5.6*sy:.3f}) -- (0,{13.5*sy:.3f}) node[above] {{$y$}};',
 f'\\draw[blue!75!black,very thick] plot[smooth] coordinates {{{egri(f17,-0.3,8.3,120,sx,sy)}}};',
 f'\\draw[purple!80!black,dashed,thick] ({-0.6*sx:.3f},{5*sy:.3f}) -- ({9.0*sx:.3f},{5*sy:.3f}) node[right,font=\\footnotesize] {{$y = 5$}};']
for r in (1,7):
    g.append(f'\\draw[gray!60,dashed] ({r*sx:.3f},{5*sy:.3f}) -- ({r*sx:.3f},0);\\fill[orange!90!black] ({r*sx:.3f},{5*sy:.3f}) circle (0.1);\\node[below=2pt,font=\\footnotesize,fill=white,inner sep=1pt] at ({r*sx:.3f},0) {{${r}$}};')
SK=fig('\n'.join(g))
q('0017',tipId='ik-kok',tip='Kökler ve katsayılar',z='orta',alt='Parabol ve tek kök',kaz='Grafiği verilen baş katsayısı 1 olan ikinci dereceden polinomu kökleri belli bir doğruyla kurup tek kök koşulunu sağlayan sabiti bulur.',kalip='grafik',
 kart='K-APLN2-06 · P(x) − 5 kökleri 1 ve 7, P(x) + n tek kök',
 metin='Şekilde, baş katsayısı 1 olan ikinci dereceden P(x) polinomunun grafiği ve y = 5 doğrusu verilmiştir; doğru grafiği x = 1 ve x = 7 noktalarında kesmektedir.\nP(x) + n polinomunun yalnızca bir gerçel kökü olduğuna göre, n kaçtır?',
 dogru=dg,yan=[(e1,'En küçük değeri −4 bulup n’yi bu değerin kendisi (işareti değiştirmeden) almış.','dikkat'),(e2,'En küçük değerin y = 5 doğrusuna olan uzaklığını (5 − (−4)) almış.','bilgi'),(e3,'P(0) = 12 sabit terimini n olarak almış.','bilgi'),(e4,'Tepe noktasının apsisinin karesini almış: 4².','bilgi')],
 istenen='n değeri.',ip=['P(x) − 5 in kökleri verildiğine göre P(x) i çarpanlı yazıp 5 ekle; tek kök koşulu için ne gerekir?'],bilgi=[GRF],sekil=SK,
 ad=[A('Polinomu yaz','P(x) − 5 = (x − 1)(x − 7).','P(x) = x² − 8x + 12'),A('Tek kök koşulu','P(x) + n = x² − 8x + 12 + n için diskriminant sıfır.','64 − 4(12 + n) = 0'),A('n','Denklem çözülür.','n = 4')],
 puf='Kökleri bilinen bir polinoma sabit ekleyince grafik yukarı ya da aşağı kayar; tek kök, en düşük noktanın eksene değmesidir.')

# ---- 0018 · zor · öncüllü · çift–tek ayrıştırma
Pp=x**4-3*x**3+2*x**2-x+5
Qp=sp.expand(Pp+Pp.subs(x,-x)); Rp=sp.expand(Pp-Pp.subs(x,-x)); assert Qp==2*x**4+4*x**2+10 and Rp==-6*x**3-2*x
assert sp.rem(Qp,x**2-1,x)==16 and S(Rp.subs(x,-1))==8 and Rp.subs(x,0)==0
dogru='I ve III'; vals=['Yalnız I','Yalnız III','I ve II','I ve III','II ve III']
q('0018',tipId='ik-ozdes',tip='Özdeşlik ve eşitsizlikten polinom',z='orta',alt='Çift–tek ayrıştırma',kaz='P(x) + P(−x) ve P(x) − P(−x) polinomlarının simetri özelliklerini kullanarak kalan ve sabit terim öncüllerini sınar.',kalip='öncüllü',
 kart='K-APLN2-07 · P(x) ± P(−x), kalan öncülleri',
 metin='P(x) = x⁴ − 3x³ + 2x² − x + 5 polinomu için Q(x) = P(x) + P(−x) ve R(x) = P(x) − P(−x) polinomları tanımlanıyor.\nBuna göre,\nI.   Q(x) polinomunun x² − 1 ile bölümünden kalan 16 dır.\nII.  R(x) polinomunun x + 1 ile bölümünden kalan −8 dir.\nIII. R(x) polinomunun sabit terimi 0 dır.\nifadelerinden hangileri doğrudur?',
 dogru=dogru,yan=[('Yalnız I','R’nin tek polinom olduğunu görmeyip III’ün sabit terim sıfır olduğunu kaçırmış.','bilgi'),('Yalnız III','Q’nun x² − 1’e bölümünde kalanı 2 + 4 + 10 = 16 olarak bulamamış.','bilgi'),('I ve II','R(−1)’i R(1) = −8 sanıp II’yi doğru, III’ü (sabit terim) yanlış değerlendirmiş.','dikkat'),('II ve III','Q(1) yerine P(1) + P(1) = 8 hesaplayıp I’i yanlış bulmuş.','islem')],
 istenen='Doğru olan ifadeler.',ip=['Q ve R’yi açıp çift dereceli ve tek dereceli terimleri ayır; sonra her öncülü sına.'],bilgi=[CIFTTEK,KAL],sira=sirala(vals),
 ad=[A('Q ve R','Çift dereceli terimler Q’da 2 katıyla, tek dereceli terimler R’de 2 katıyla kalır.','Q(x) = 2x⁴ + 4x² + 10, R(x) = −6x³ − 2x'),A('I. öncül','Q yalnız çift kuvvet içerir; x² → 1 yazılır.','Q’nun kalanı 2 + 4 + 10 = 16: doğru'),A('II ve III','R(−1) = 6 + 2 = 8; R(0) = 0.','II yanlış, III doğru')],
 puf='P(x) + P(−x) çift, P(x) − P(−x) tek polinomdur; tek polinomun sabit terimi sıfırdır, çift polinomun x² − 1 ile kalanı x² → 1 yazarak bulunur.')

# ---- 0019 · zor · tablo · tanımlı işlem + ikinci dereceden bölen
Pt={1:4,2:-1,3:5}; Qt={1:2,2:3,3:1}
def op(t): return Pt[t]*Qt[t]-Pt[Qt[t]]
def r0(v1,v2): # kalan mx+n, R(1)=v1, R(2)=v2 -> R(0)
    m=v2-v1; return v1-m
v1,v2=op(1),op(2); assert (v1,v2)==(9,-8)
dg=r0(v1,v2); assert dg==26
e1=r0(v2,v1); e2=r0(Pt[1]*Qt[1]+Pt[Qt[1]],Pt[2]*Qt[2]+Pt[Qt[2]]); e3=r0(Pt[1]*Qt[1]-Qt[1],Pt[2]*Qt[2]-Qt[2]); e4=r0(0,0)
assert (dg,e1,e2,e3,e4)==(26,-25,12,18,0) and len({dg,e1,e2,e3,e4})==5
SK=tablo_svg(['x','1','2','3'],[['P(x)']+[ms(Pt[k]) for k in (1,2,3)],['Q(x)']+[ms(Qt[k]) for k in (1,2,3)]])
q('0019',tipId='ik-deger',tip='Değer ve bileşke',z='zor',alt='Tanımlı işlem ve kalan',kaz='Tanımlı bir işlemle elde edilen polinomun ikinci dereceden bölenle kalanını tablodaki değerlerle bileşke hesaplayarak bulur.',kalip='tablo',
 kart='K-APLN2-02 · (P ⊗ Q)(x) = P(x)·Q(x) − P(Q(x)), kalan polinomu',
 metin='Gerçel katsayılı P(x) ve Q(x) polinomları için (P ⊗ Q)(x) = P(x)·Q(x) − P(Q(x)) biçiminde bir polinom tanımlanıyor. P(x) ve Q(x) polinomlarının bazı değerleri aşağıdaki tabloda verilmiştir.\n(P ⊗ Q)(x) polinomunun x² − 3x + 2 ile bölümünden kalan R(x) olduğuna göre, R(0) kaçtır?',
 dogru=dg,yan=[(e1,'İki kalan değerini yer değiştirip R(1) = −8, R(2) = 9 almış: R(x) = 17x − 25.','dikkat'),(e2,'İşlemde çıkarma yerine toplama yapmış: R(1) = 7, R(2) = 2 ve R(0) = 12.','islem'),(e3,'P(Q(x)) yerine Q(x) çıkarmış: R(1) = 6, R(2) = −6 ve R(0) = 18.','bilgi'),(e4,'P(Q(x)) terimini P(x)·Q(x) saymış; fark sıfır olmuş.','bilgi')],
 istenen='R(0) değeri.',ip=['Bölenin kökleri hangi noktalardır; işlemle elde edilen polinomun bu noktalardaki değerlerini tablodan hesapla.'],bilgi=[TAN,KAL],sekil=SK,
 ad=[A('x = 1','Q(1) = 2 olduğundan P(Q(1)) = P(2).','4·2 − P(2) = 8 − (−1) = 9'),A('x = 2','Q(2) = 3 olduğundan P(Q(2)) = P(3).','(−1)·3 − P(3) = −3 − 5 = −8'),A('Kalan polinomu','x² − 3x + 2 = (x − 1)(x − 2); R(x) = mx + n.','m + n = 9, 2m + n = −8 → m = −17, n = 26'),A('R(0)','x = 0 yazılır.','R(0) = 26')],
 puf='Kalan, polinomun bölenin kök noktalarındaki değerleriyle belirlenir; bileşke içinde önce iç polinomun değerini tablodan oku.')

# ---- 0020 · zor · şekilli · (x−1)² ve x−2 ile kalan
R20=-x**2+5*x+1
assert sp.rem(R20,(x-1)**2,x)==3*x+2 and R20.subs(x,2)==7
dg=S(R20.subs(x,0)); e1=2; e2=3; e3=5; e4=7
assert dg==1 and len({dg,e1,e2,e3,e4})==5
g=['\\tikzset{kt/.style={draw,rounded corners=3pt,thick,align=center,minimum height=1.0cm}}',
 '\\node[kt,fill=blue!12,draw=blue!70!black,minimum width=1.6cm] (p) at (0,0) {$P(x)$};',
 '\\node[kt,fill=orange!18,draw=orange!85!black,minimum width=5.2cm] (r1) at (5.2,1.0) {$(x-1)^2$ ile bölümünden\\\\kalan $3x + 2$};',
 '\\node[kt,fill=green!15,draw=green!50!black,minimum width=5.2cm] (r2) at (5.2,-1.0) {$x - 2$ ile bölümünden\\\\kalan $7$};',
 '\\draw[-{Stealth},thick] (p.east) to[out=0,in=180] (r1.west);',
 '\\draw[-{Stealth},thick] (p.east) to[out=0,in=180] (r2.west);']
SK=fig('\n'.join(g))
q('0020',tipId='ik-kalan',tip='Kalan teoremi ve çift katlı bölen',z='zor',alt='Çift katlı bölenle kalan',kaz='Çift katlı ve tek katlı bölenlerin kalanlarından üçüncü dereceden bölenle kalan polinomu kurar.',kalip='şekilli',
 kart='K-APLN2-04 · (x−1)² ve x−2 kalanları, çarpım bölenle kalan',
 metin='Şekilde, P(x) polinomunun iki farklı bölenle bölümünden kalanlar gösterilmiştir. P(x) polinomunun (x − 1)²(x − 2) ile bölümünden kalan R(x) olduğuna göre, R(0) kaçtır?',
 dogru=dg,yan=[(e1,'R(x) yerine 3x + 2’yi alıp x = 0 yazmış.','bilgi'),(e2,'R(x) = a(x − 1)² + 3x + 2 yazmış, R(2) = a + 8 = 7 denkleminde işaret hatasıyla a = 1 bulmuş: R(0) = 3.','islem'),(e3,'R(0) yerine P(1) = 3 + 2 = 5 değerini vermiş.','dikkat'),(e4,'R(0) yerine x − 2 ile kalan olan 7’yi vermiş.','dikkat')],
 istenen='R(0) değeri.',ip=['R(x) ikinci dereceden olabilir; çift katlı bölenle verilen kalan, R(x)’in yazılışını sınırlar.'],bilgi=[KAT,KAL],sekil=SK,
 ad=[A('R(x)’in biçimi','R(x) = a(x − 1)² + (3x + 2) yazılabilir; R’nin (x − 1)² ile kalanı 3x + 2 olmalıdır.','R(x) = a(x − 1)² + 3x + 2'),A('a’yı bul','x − 2 ile kalan 7 olduğundan R(2) = 7.','a + 8 = 7, a = −1'),A('R(0)','x = 0 yazılır.','−1 + 2 = 1')],
 puf='Çift katlı bölenin kalanını verilen biçimde yaz; geriye kalan tek bilinmeyeni diğer bölenin kök değeri belirler.')

# ---------------- yazma ----------------
from collections import Counter
for qq in P.ANA: qq['kardes']=None
json.dump(P.ANA,open(os.path.join(HD,'polinomiki-1.json'),'w'),ensure_ascii=False,indent=1)
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=UK))['kartlar'].append(c['id'])
json.dump(dict(konu=P.konu_adi,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2025 AYT Matematik çıkmış soruları ve yayın soru bankaları (yalnız mantık), MEB 11–12. sınıf müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HD,'..','kartlar','polinomiki.json'),'w'),ensure_ascii=False,indent=1)
print(len(P.ANA),'soru · harfler',dict(sorted(Counter(z['cevap']['sik'] for z in P.ANA).items())),'· zorluk',dict(Counter(z['zorluk'] for z in P.ANA)),'· şekilli',sum(1 for z in P.ANA if z['sekil']),'· tipId',len(tipler),'· kalıp',dict(Counter(z['kalip'] for z in P.ANA)))
