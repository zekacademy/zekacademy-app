"""Fonksiyonlar · ŞEKİLLİ ek paket (7 soru): ok şeması, grafik, makine şeması, tablo; şekil çözüm verisini taşır. Her doğru ve çeldirici değer kodla assert edilir. Kardeş yok, ipucu 1."""
import sys,os,math
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
from itertools import permutations
H.KONU='Fonksiyonlar'
UK='matd|Fonksiyonlar'
P=Parti('fonksek','Fonksiyonlar',UK)
KY='ÖSYM 2018–2026 TYT Matematik (şemalı, grafikli ve tablolu fonksiyon soruları; yalnız mantık) · MEB 9. sınıf'
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)
def fig(body): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'+body+'\n\\end{tikzpicture}')
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)

OKS=B('Ok şeması','tanım kümesinin her elemanından tam bir ok çıkar; bir elemandan iki ok çıkması ya da hiç ok çıkmaması fonksiyon olmasını bozar. Değer kümesinde ok almayan eleman olabilir, birden çok ok alan eleman da olabilir. Örnek: {p, q} → {r, s} için p → r, q → r bir fonksiyondur')
BIJ=B('Birebir ve örten fonksiyon','f birebir ve örtense iki kümenin eleman sayısı eşittir, değer kümesindeki her elemana tam bir ok gelir; gösterilmeyen elemanlar kalan elemanlarla eşlenir. Örnek: {1, 2, 3} → {a, b, c} için 1 → b, 2 → a verilmişse 3 → c’dir')
LIN=B('Doğrusal fonksiyon','f(x) = ax + b için grafikten iki noktanın (x₁, y₁), (x₂, y₂) koordinatı okunur; eğim a = (y₂ − y₁)/(x₂ − x₁) bulunur, sonra b bir noktadan hesaplanır. Örnek: (0, 1) ve (2, 5) noktalarından a = 2, b = 1 olur')
BIL=B('Bileşke fonksiyon','(f ∘ g)(x) = f(g(x)): önce g, sonra f uygulanır; makine şemasında soldaki makine önce çalışır. Örnek: f(x) = x + 1, g(x) = 2x ise (f ∘ g)(3) = f(6) = 7 iken (g ∘ f)(3) = g(4) = 8’dir')
BTR=B('Bileşkenin tersi','(f ∘ g)(a) = c ise g(a) = f⁻¹(c) olur; yani a = g⁻¹(f⁻¹(c)). Birebir ve örten fonksiyonun tablosunda ters değer, değerin bulunduğu sütunun üst satırından okunur. Örnek: f(2) = 5 ise f⁻¹(5) = 2’dir')
KCZ=B('f(x) = k denkleminin çözüm sayısı','y = k yatay doğrusunun grafiği kestiği noktaların sayısıdır; dolu nokta grafiğe dahildir, içi boş nokta dahil değildir; iki doğru parçasının birleştiği köşe tek nokta sayılır. Örnek: grafik yalnız (1, 3) noktasında y = 3’ü kesiyorsa f(x) = 3’ün 1 çözümü vardır')
TER=B('Ters işlem zinciri','art arda makinelerde çıkıştan girişe gitmek için makineler sondan başa, her biri kendi terslediğiyle çalıştırılır (toplamanın tersi çıkarma, çarpmanın tersi bölme). Örnek: x → 2x → +3 ile çıkış 9 ise x = (9 − 3) ÷ 2 = 3’tür')

# ---------- kartlar ----------
kartla('K-FSK-01','Ok şemasında eksik eşleme','Birebir ve örten fonksiyonda değer kümesinde ok almamış tek eleman, oku gösterilmemiş elemanla eşlenir.','Kullanılmış bir elemanı tekrar kullanmak; yanlış x değerini okumak.','kolay','şekilli',3,'fsk-eksikok','Ok şemasında eksik eşleme')
kartla('K-FSK-02','Şemalarda fonksiyon olma','Her şemada tanım kümesinin her elemanından tam bir ok çıkıp çıkmadığına bakılır.','Fonksiyonu birebir sanmak; bir elemandan çıkan iki oku görmemek; yönü ters okumak.','orta','öncüllü',3,'fsk-fonkmu','Şemalarda fonksiyon olma')
kartla('K-FSK-03','Doğrusal fonksiyonun grafiği','Grafikte işaretli iki noktanın koordinatlarından eğim ve sabit bulunur; kural istenen noktada hesaplanır.','Eğimi ters hesaplamak; sabiti y-kesişimi yerine bir noktanın y değeri almak; işaret hatası.','orta','grafik',4,'fsk-dogrusal','Doğrusal fonksiyonun grafiği')
kartla('K-FSK-04','Makine şeması ve bileşke','Makineler şemadaki sırayla uygulanır: önce soldaki, sonra sağdaki.','Makine sırasını ters uygulamak; yalnız bir makineyi uygulamak; sonuçları toplamak.','kolay','yeni nesil',3,'fsk-makine','Makine şeması ve bileşke')
kartla('K-FSK-05','Tablo ile verilen iki fonksiyon','Bileşkenin tersi için önce dıştaki fonksiyonun, sonra içteki fonksiyonun tersi tabloda ters yönde okunur.','Bileşke sırasını karıştırmak; ters yerine doğrudan değer okumak.','orta','tablo',4,'fsk-tablo','Tablo ile verilen fonksiyonlar')
kartla('K-FSK-06','Parçalı grafikte f(x) = k çözümleri','Yatay doğrunun grafiği kestiği noktalar sayılır; açık uç, köşe ve kapalı uç dikkate alınarak k’ye göre çözüm sayısı bulunur.','Açık ucu çözüm saymak; köşeyi iki sayıp ya da hiç saymamak; kapalı ucu dışarıda bırakmak.','zor','grafik',5,'fsk-kcozum','Parçalı grafikte çözüm sayısı')
kartla('K-FSK-07','Üç makineli zincirde giriş bulma','Çıkıştan başlayarak her makinenin tersi sondan başa uygulanır.','Tersleri ileri sırayla uygulamak; bir makineyi atlamak; çarpmanın tersini çarpma yapmak.','zor','yeni nesil',4,'fsk-zincir','Ters işlem zinciri')

# ================= şekil yardımcıları =================
def okd(ox,Ae,Be,pairs,cap,yc=0.0,vs=0.8):
    o=[]; xa,xb=ox,ox+2.4
    ya=[(len(Ae)-1)/2*vs-i*vs for i in range(len(Ae))]; yb=[(len(Be)-1)/2*vs-i*vs for i in range(len(Be))]
    h=2.05
    o.append(f'\\draw[thick] ({xa},{yc}) ellipse (0.55 and {h}); \\draw[thick] ({xb},{yc}) ellipse (0.55 and {h});')
    o.append(f'\\node[font=\\normalsize\\bfseries] at ({xa},{yc+h+0.3}) {{A}}; \\node[font=\\normalsize\\bfseries] at ({xb},{yc+h+0.3}) {{B}};')
    for i,e in enumerate(Ae): o.append(f'\\node at ({xa},{yc+ya[i]}) {{${e}$}};')
    for i,e in enumerate(Be): o.append(f'\\node at ({xb},{yc+yb[i]}) {{${e}$}};')
    for a,b in pairs: o.append(f'\\draw[-{{Stealth}},thick] ({xa+0.3},{yc+ya[a]}) -- ({xb-0.3},{yc+yb[b]});')
    if cap: o.append(f'\\node[font=\\large\\bfseries] at ({(xa+xb)/2},{yc-h-0.4}) {{{cap}}};')
    return '\n'.join(o)
def graf(x0,x1,y0,y1,sx,sy,govde,xlab='x',ylab='y'):
    o=[]
    for i in range(x0,x1+1): o.append(f'\\draw[gray!35,thin] ({i*sx:.3f},{y0*sy:.3f}) -- ({i*sx:.3f},{y1*sy:.3f});')
    for j in range(y0,y1+1): o.append(f'\\draw[gray!35,thin] ({x0*sx:.3f},{j*sy:.3f}) -- ({x1*sx:.3f},{j*sy:.3f});')
    o.append(f'\\draw[-{{Stealth}},thick] ({(x0-0.3)*sx:.3f},0) -- ({(x1+0.6)*sx:.3f},0) node[right] {{${xlab}$}};')
    o.append(f'\\draw[-{{Stealth}},thick] (0,{(y0-0.3)*sy:.3f}) -- (0,{(y1+0.6)*sy:.3f}) node[above] {{${ylab}$}};')
    for i in range(x0,x1+1):
        if i!=0: o.append(f'\\draw[thick] ({i*sx:.3f},-0.05) -- ({i*sx:.3f},0.05); \\node[below=2pt,font=\\scriptsize] at ({i*sx:.3f},0) {{${i}$}};')
    for j in range(y0,y1+1):
        if j!=0: o.append(f'\\draw[thick] (-0.05,{j*sy:.3f}) -- (0.05,{j*sy:.3f}); \\node[left=2pt,font=\\scriptsize,fill=white,inner sep=0.6pt] at (0,{j*sy:.3f}) {{${j}$}};')
    o.append(govde); return '\n'.join(o)
def kutu(x,y,ust,ic,w=2.3):
    return f'\\node[draw,thick,rounded corners=3pt,minimum width={w}cm,minimum height=1.25cm,align=center,fill=vurgu!10] at ({x},{y}) {{\\textbf{{{ust}}}\\\\${ic}$}};'

# ================= 01 kolay · ok şeması, eksik eşleme =================
A_=[1,2,3,4]; B_=[3,5,7,9]; ok_={1:7,2:3,3:9}; eksik=[b for b in B_ if b not in ok_.values()]; assert eksik==[5]
f4=eksik[0]; v=ok_[1]+f4; assert v==12
e=[ok_[1]+3,ok_[1]+ok_[1],ok_[1]+9,ok_[2]+f4]
assert e==[10,14,16,8] and len({v,*e})==5
SK=fig(okd(0,A_,B_,[(0,B_.index(7)),(1,B_.index(3)),(2,B_.index(9))],''))
q('0001',tipId='fsk-eksikok',tip='Ok şemasında eksik eşleme',z='kolay',alt='Ok Şeması',kaz='Birebir ve örten fonksiyonun ok şemasında gösterilmeyen eşlemeyi bulur ve değer toplamı hesaplar.',kalip='şekilli',
 kart='K-FSK-01 (ok şeması) · {1,2,3,4} → {3,5,7,9}; 1→7, 2→3, 3→9; f(4)=5',
 metin='Bir öğrenci, dört elemanlı A kümesinden dört elemanlı B kümesine tanımlı birebir ve örten bir f fonksiyonunun ok şemasını çizmeye başlamıştır. Şekilde görüldüğü gibi, f’nin yalnızca bazı eşlemeleri oklarla gösterilmiş, kalan eşleme henüz çizilmemiştir.\nBuna göre f(1) + f(4) toplamı kaçtır?',
 dogru=v,yan=[(e[0],'f(4) yerine B’nin ilk elemanı olan 3’ü almış (zaten f(2) ile eşlendiğini görmemiş): 7 + 3.','dikkat'),(e[1],'f(4)’ü f(1) ile aynı değer (7) almış: 7 + 7; birebirliği kullanmamış.','bilgi'),(e[2],'f(4)’ü B’nin son elemanı olan 9 almış (zaten f(3) ile eşlendiğini görmemiş): 7 + 9.','dikkat'),(e[3],'f(1) yerine f(2)’yi okumuş: 3 + 5.','islem')],
 istenen='f(1) + f(4) toplamı.',ip=['f birebir ve örten olduğuna göre B’nin her elemanına kaç ok gelmesi gerekir?'],bilgi=[BIJ],sekil=SK,
 ad=[A('f(1)’i oku','Oku gösterilen eşlemeden.','f(1) = 7'),A('f(4)’ü bul','f birebir ve örten olduğundan B’de ok almayan tek eleman 4’ün eşidir.','B’de ok almayan eleman 5 → f(4) = 5'),A('Topla','İki değer toplanır.','7 + 5 = 12')],
 puf='Birebir ve örten fonksiyonda her eleman tam bir kez kullanılır; kalan eleman kalan elemanla eşlenir.')

# ================= 02 orta · şemalarda fonksiyon olma (öncüllü) =================
Ae=[1,2,3,4]; Be=['a','b','c','d']
S1=[(0,1),(1,3),(2,0),(3,2)]                 # birebir: 1→b,2→d,3→a,4→c
S2=[(0,0),(1,0),(2,1),(3,2)]                 # 1→a,2→a,3→b,4→c (d boşta)
S3=[(0,0),(1,1),(2,2),(2,3),(3,0)]           # 3 iki ok çıkarıyor
def fonk(S,n=4):
    return all(sum(1 for a,_ in S if a==i)==1 for i in range(n))
def orten(S,m=4): return all(any(b==j for _,b in S) for j in range(m))
assert [fonk(S1),fonk(S2),fonk(S3)]==[True,True,False] and orten(S3)
dog='I ve II'; sira=['Yalnız I','I ve II','I ve III','II ve III','I, II ve III']
assert dog==' ve '.join([r for r,S in zip(['I','II','III'],[S1,S2,S3]) if fonk(S)])
SK=fig(okd(0,Ae,Be,S1,'I')+'\n'+okd(4.2,Ae,Be,S2,'II')+'\n'+okd(8.4,Ae,Be,S3,'III'))
q('0002',tipId='fsk-fonkmu',tip='Şemalarda fonksiyon olma',z='orta',alt='Şemalarda Fonksiyon',kaz='Ok şemalarında tanım kümesinin her elemanından tam bir ok çıkıp çıkmadığına bakarak fonksiyon belirtenleri ayırt eder.',kalip='öncüllü',
 kart='K-FSK-02 (üç ok şeması) · I birebir, II birden çok ok alan + ok almayan eleman, III bir elemandan iki ok',
 metin='Bir öğretmen, A kümesinden B kümesine eşleme yapan üç şemayı tahtaya çizmiş ve öğrencilerden bu eşlemeleri incelemelerini istemiştir. Şemalar şekilde I, II ve III numaralarıyla verilmiştir; oklar A’nın elemanlarını B’nin elemanlarıyla eşlemektedir.\nBuna göre bu şemalardan hangileri A’dan B’ye bir fonksiyon belirtir?',
 dogru=dog,yan=[(sira[0],'Fonksiyonun birebir olması gerektiğini sanıp II’yi (a’ya iki ok giden) reddetmiş; III’teki çift oku da görmüş.','bilgi'),(sira[2],'Yalnız B’nin elemanlarına gelen oklara bakmış: I ve III’te B’nin her elemanına ok gelir, II’de d’ye gelmez; A’dan çıkan çift oku denetlememiş.','bilgi'),(sira[3],'Değer kümesinde bir elemana birden çok ok gelmesini şart sanmış (çok-bire): a’ya iki ok giden II ve III’ü seçmiş, birebir olan I’i reddetmiş.','bilgi'),(sira[4],'III’te 3’ün iki farklı elemana gittiğini görmemiş; her A elemanından en az bir ok çıkmasını yeterli sanmış.','dikkat')],
 sira=sira,istenen='A’dan B’ye fonksiyon belirten şemalar.',ip=['Her şemada A’nın her elemanından kaç ok çıktığını tek tek say.'],bilgi=[OKS],sekil=SK,
 ad=[A('I’i incele','A’nın her elemanından tam bir ok çıkıyor.','fonksiyon'),A('II’yi incele','Her elemandan tam bir ok çıkıyor; a’ya iki ok gelmesi ve d’ye ok gelmemesi fonksiyonu bozmaz.','fonksiyon'),A('III’ü incele','3 elemanından iki ok çıkıyor (c ve d’ye).','fonksiyon değil'),A('Sonuç','Yalnız I ve II fonksiyon belirtir.','I ve II')],
 puf='Fonksiyonda önemli olan tanım kümesinden çıkan oklardır; değer kümesine gelen oklara değil.')

# ================= 03 orta · doğrusal grafik =================
fa_,fb_=2,-3; ff=lambda x:fa_*x+fb_
p1,p2=(1,ff(1)),(3,ff(3)); assert p1==(1,-1) and p2==(3,3)
a_=Fr(p2[1]-p1[1],p2[0]-p1[0]); b_=p1[1]-a_*p1[0]; assert (a_,b_)==(2,-3)
v=ff(8)+ff(-1); assert v==8
g1=lambda x:2*x; g2=lambda x:2*x-1; g3=lambda x:2*x+3
e=[g1(8)+g1(-1),g2(8)+g2(-1),ff(8)-ff(-1),g3(8)+g3(-1)]
assert e==[14,12,18,20] and len({v,*e})==5
sx,sy=0.62,0.46
gb=f'\\draw[line width=1.5pt] ({-1.5*sx:.3f},{ff(-1.5)*sy:.3f}) -- ({4.5*sx:.3f},{ff(4.5)*sy:.3f});'
for p in (p1,p2): gb+=f'\n\\fill ({p[0]*sx:.3f},{p[1]*sy:.3f}) circle (0.09);'
SK=fig(graf(-3,5,-6,7,sx,sy,gb,ylab='y=f(x)'))
q('0003',tipId='fsk-dogrusal',tip='Doğrusal fonksiyonun grafiği',z='orta',alt='Doğrusal Grafik',kaz='Doğrusal fonksiyonun grafiğindeki iki noktadan kuralı bulup grafik dışındaki bir değeri hesaplar.',kalip='grafik',
 kart='K-FSK-03 (doğrusal grafik) · (1, −1) ve (3, 3) noktaları; f(x) = 2x − 3',
 metin='Şekilde, gerçel sayılarda tanımlı doğrusal bir f fonksiyonunun grafiği verilmiştir. Grafik üzerinde işaretlenmiş iki nokta, kılavuz çizgilerinin kesişim noktalarındadır; grafiğin diğer noktaları okunmak için işaretlenmemiştir.\nBuna göre f(8) + f(−1) toplamı kaçtır?',
 dogru=v,yan=[(e[0],'Sabiti 0 almış (kuralı 2x sanmış): f(8) + f(−1) = 16 − 2.','dikkat'),(e[1],'Sabiti, işaretli noktanın y değeri olan −1 almış: kuralı 2x − 1 yazmış.','bilgi'),(e[2],'f(−1) değerinin işaretini ters yazıp toplamak yerine çıkarmış: f(8) − f(−1).','islem'),(e[3],'Sabiti y eksenindeki değerin işaretini ters alarak +3 yazmış: kuralı 2x + 3 almış.','dikkat')],
 istenen='f(8) + f(−1) toplamı.',ip=['İşaretli iki noktanın koordinatlarını oku; bu noktalardan eğimi bulabilirsin.'],bilgi=[LIN],sekil=SK,
 ad=[A('Noktaları oku','Grafikteki işaretli noktalar.','(1, −1) ve (3, 3)'),A('Eğimi bul','y farkı x farkına bölünür.','a = (3 − (−1)) / (3 − 1) = 2'),A('Sabiti bul','Bir noktayı kurala yaz.','−1 = 2·1 + b → b = −3 → f(x) = 2x − 3'),A('Topla','Değerler kuralda hesaplanır.','f(8) = 13 · f(−1) = −5 → 13 + (−5) = 8')],
 puf='Önce işaretli iki noktadan kuralı yaz; grafikte görünmeyen değerleri kuraldan hesapla.')

# ================= 04 kolay · makine şeması (bileşke) =================
f_=lambda x:2*x+5; g_=lambda x:3*x-2; xin=4
v=f_(g_(xin)); assert v==25
e=[g_(f_(xin)),f_(xin),g_(xin),f_(xin)+g_(xin)]; assert e==[37,13,10,23] and len({v,*e})==5
o=['\\node[draw,thick,minimum width=1.0cm,minimum height=1.0cm] (a) at (0,0) {$4$}; \\node[above=2pt] at (0,0.5) {Giriş};',
   kutu(2.5,0,'g','x \\mapsto 3x-2'),kutu(5.6,0,'f','x \\mapsto 2x+5'),
   '\\node[draw,thick,minimum width=1.0cm,minimum height=1.0cm] (z) at (8.1,0) {$?$}; \\node[above=2pt] at (8.1,0.5) {Çıkış};',
   '\\draw[-{Stealth},thick] (0.5,0) -- (1.35,0); \\draw[-{Stealth},thick] (3.65,0) -- (4.45,0); \\draw[-{Stealth},thick] (6.75,0) -- (7.6,0);']
SK=fig('\n'.join(o))
q('0004',tipId='fsk-makine',tip='Makine şeması ve bileşke',z='kolay',alt='Makine Şeması',kaz='Art arda bağlı iki makinenin kurallarını şemadaki sırayla uygulayarak çıkış değerini bulur.',kalip='yeni nesil',
 kart='K-FSK-04 (makine şeması) · giriş 4; g: 3x − 2, sonra f: 2x + 5',
 metin='Şekildeki sistemde giriş kutusuna yazılan sayı, önce g makinesine, sonra f makinesine girmektedir. Her makine, kendisine giren sayıya üzerinde yazılı kuralı uygulayıp sonucu bir sonraki aşamaya iletir; çıkıştaki sayı başka bir işleme sokulmaz.\nBuna göre şekildeki giriş için çıkış kutusunda hangi sayı görülür?',
 dogru=v,yan=[(e[0],'Makinelerin sırasını ters uygulamış: önce f, sonra g.','dikkat'),(e[1],'Yalnız f makinesini uygulamış.','dikkat'),(e[2],'Yalnız g makinesini uygulamış.','dikkat'),(e[3],'Bileşke yerine iki makinenin çıkışını toplamış: f(4) + g(4).','bilgi')],
 istenen='Çıkış kutusundaki sayı.',ip=['Girişten çıkışa doğru ilerle; ilk makinenin çıkışı ikinci makineye giren sayıdır.'],bilgi=[BIL],sekil=SK,
 ad=[A('Sırayı belirle','Şemada oklar giriş kutusundan g makinesine, oradan f makinesine gider.','önce g, sonra f'),A('g makinesi','Giriş önce g kuralından geçer.','g(4) = 3·4 − 2 = 10'),A('f makinesi','g’nin çıkışı f’ye girer.','f(10) = 2·10 + 5 = 25')],
 puf='Şemada ok yönü sırayı verir: bileşkede önce soldaki makine çalışır.')

# ================= 05 orta · tablo ile iki fonksiyon =================
fT=(4,5,2,3,1); gT=(2,3,5,1,4)
F=lambda x:fT[x-1]; G=lambda x:gT[x-1]; Fi=lambda y:fT.index(y)+1; Gi=lambda y:gT.index(y)+1
a=[x for x in range(1,6) if F(G(x))==4]; b=[x for x in range(1,6) if G(F(x))==2]; assert a==[4] and b==[5]
v=a[0]+b[0]; assert v==9
e=[Fi(Gi(4))+Gi(Fi(2)),Fi(4)+Gi(2),F(G(4))+G(F(2)),G(Fi(4))+F(Gi(2))]
assert e==[4,2,8,6] and len({v,*e})==5
SK=tablo_svg(['x','1','2','3','4','5'],[['f(x)']+[str(t) for t in fT],['g(x)']+[str(t) for t in gT]])
q('0005',tipId='fsk-tablo',tip='Tablo ile verilen fonksiyonlar',z='orta',alt='Tablo ile Fonksiyon',kaz='Tabloda verilen iki fonksiyonun bileşkelerine ilişkin denklemlerde bilinmeyen değerleri bulur.',kalip='tablo',
 kart='K-FSK-05 (tablo) · f = (4,5,2,3,1), g = (2,3,5,1,4); (f∘g)(a) = 4, (g∘f)(b) = 2',
 metin='A = {1, 2, 3, 4, 5} kümesinden kendisine tanımlı f ve g fonksiyonları birebir ve örten olup aşağıdaki tabloda verilmiştir.\n(f ∘ g)(a) = 4 ve (g ∘ f)(b) = 2\nolduğuna göre a + b toplamı kaçtır?',
 dogru=v,yan=[(e[0],'Bileşke sırasını karıştırmış: (g ∘ f)(a) = 4 ve (f ∘ g)(b) = 2 denklemlerini çözmüş.','dikkat'),(e[1],'Bileşke yerine tek fonksiyon okumuş: f(a) = 4 ve g(b) = 2 denklemlerini çözmüş.','bilgi'),(e[2],'a ve b’yi bulmak yerine değeri hesaplamış: (f ∘ g)(4) + (g ∘ f)(2).','islem'),(e[3],'Son adımda tersi almayı unutmuş: a yerine g(f⁻¹(4)) = 2, b yerine f(g⁻¹(2)) = 4 yazmış.','bilgi')],
 istenen='a + b toplamı.',ip=['(f ∘ g)(a) = 4 ise önce f hangi değerde 4 verir, sonra g hangi değerde bu sonucu verir?'],bilgi=[BTR],sekil=SK,
 ad=[A('a’yı bul','f(g(a)) = 4 → g(a) = f⁻¹(4); tabloda f(1) = 4.','g(a) = 1 → g(4) = 1 → a = 4'),A('b’yi bul','g(f(b)) = 2 → f(b) = g⁻¹(2); tabloda g(1) = 2.','f(b) = 1 → f(5) = 1 → b = 5'),A('Topla','İki değer toplanır.','4 + 5 = 9')],
 puf='Bileşkede içteki fonksiyon önce çalışır; tersini alırken sırayı tersine çevir.')

# ================= 06 zor · parçalı grafik, f(x) = k çözüm sayısı =================
V=[(-4,1),(-2,5),(0,-1),(2,2),(4,4)]
from fractions import Fraction as Fr
def cozum(k,sag_acik=True,sol_say=True,kose_cift=False):
    xs=[]
    for i,((x1,y1),(x2,y2)) in enumerate(zip(V,V[1:])):
        if min(y1,y2)<=k<=max(y1,y2) and y1!=y2:
            x=Fr(x1)+Fr(k-y1,y2-y1)*(x2-x1)
            xs.append((i,x))
    pts=[]
    for i,x in xs:
        if sag_acik and x==V[-1][0]: continue
        if not sol_say and x==V[0][0]: continue
        pts.append(x)
    return len(pts) if kose_cift else len(set(pts))
ks=list(range(-3,9))
dog_k=[k for k in ks if cozum(k)==3]; assert dog_k==[1,2,3]; v=sum(dog_k)
e1=[k for k in ks if cozum(k,sag_acik=False)==3]            # açık uç sayıldı
e2=[k for k in ks if cozum(k,kose_cift=True)==3]            # köşe iki kez sayıldı
e3=[k for k in ks if cozum(k,sol_say=False)==3]             # sol kapalı uç sayılmadı
e=[sum(e1),sum(e2),sum(e3),len(dog_k)]
assert (e1,e2,e3)==([1,2,3,4],[1,3],[2,3]) and e==[10,4,5,3] and v==6 and len({v,*e})==5
sx,sy=0.62,0.46
gb='\\draw[line width=1.5pt] '+' -- '.join(f'({x*sx:.3f},{y*sy:.3f})' for x,y in V)+';'
for x,y in V[:-1]: gb+=f'\n\\fill ({x*sx:.3f},{y*sy:.3f}) circle (0.075);'
gb+=f'\n\\draw[thick,fill=white] ({V[-1][0]*sx:.3f},{V[-1][1]*sy:.3f}) circle (0.1);'
SK=fig(graf(-4,5,-2,7,sx,sy,gb,ylab='y=f(x)'))
q('0006',tipId='fsk-kcozum',tip='Parçalı grafikte çözüm sayısı',z='zor',alt='Parçalı Grafik',kaz='Parçalı doğrusal grafikte açık uç, köşe ve kapalı ucu dikkate alarak f(x) = k denkleminin tam üç çözümü olan tam sayı k değerlerini bulur.',kalip='grafik',
 kart='K-FSK-06 (parçalı grafik) · köşeler (−4,1), (−2,5), (0,−1), (2,2), (4,4) açık uç; k ∈ {1, 2, 3}',
 metin='Şekilde, gerçel sayıların bir alt kümesinde tanımlı f fonksiyonunun grafiği verilmiştir; grafiğin doğru parçalarının uçları kılavuz çizgilerinin kesişimindedir ve içi boş nokta, grafiğe ait olmayan noktayı gösterir.\nBuna göre f(x) = k denkleminin tam 3 farklı çözümünün olması için k’nin alabileceği tam sayı değerlerinin toplamı kaçtır?',
 dogru=v,yan=[(e[0],'İçi boş (4, 4) noktasını grafiğe dahil saymış: k = 4 için de 3 çözüm bulmuş; k değerleri 1, 2, 3, 4.','dikkat'),(e[1],'(2, 2) köşesinde birleşen iki doğru parçasını iki ayrı çözüm sayıp k = 2’yi dışarıda bırakmış; k değerleri 1, 3.','bilgi'),(e[2],'Sol uçtaki dolu (−4, 1) noktasını saymamış: k = 1 için yalnız 2 çözüm bulmuş; k değerleri 2, 3.','dikkat'),(e[3],'Toplam yerine k değerlerinin sayısını (3 tane) yazmış.','islem')],
 istenen='Tam 3 çözüm veren tam sayı k değerlerinin toplamı.',ip=['y = k yatay doğrusunu aşağıdan yukarıya kaydırıp her k için grafikle kesişim noktalarını say; köşelere ve uçlara özellikle bak.'],bilgi=[KCZ],sekil=SK,
 ad=[A('Köşeleri oku','Grafiğin köşe ve uç noktaları.','(−4, 1) dolu; (−2, 5); (0, −1); (2, 2); (4, 4) boş'),A('k = 1 için say','y = 1 doğrusu sol dolu uçta, ikinci ve üçüncü doğru parçasında grafiği keser.','3 çözüm'),A('k = 2 ve 3','k = 2’de ilk iki parça birer nokta, (2, 2) köşesi tek nokta verir; k = 3’te ilk, ikinci ve son parça birer nokta verir.','k = 2: 3 çözüm; k = 3: 3 çözüm'),A('Diğer tam sayıları ele','k = 4’te (4, 4) açık uç sayılmaz, yalnız 2 çözüm; k = 0’da 2, k = 5’te 1, k = −1’de 1 çözüm vardır.','k = 4 olmaz'),A('Topla','Uygun k değerleri 1, 2, 3.','1 + 2 + 3 = 6')],
 puf='Yatay doğruyu kaydırırken köşede iki parçanın birleştiğini, uçta ise noktanın dolu ya da boş olduğunu ayrı ayrı kontrol et.')

# ================= 07 zor · üç makineli zincir, giriş bulma =================
mf=(3,2); mg=(2,1); mh=(1,6)
ap=lambda m,x:m[0]*x+m[1]
iv=lambda m,y:Fr(y-m[1],m[0])
xg=9; cikis=ap(mh,ap(mg,ap(mf,xg))); assert cikis==65
ters=iv(mf,iv(mg,iv(mh,cikis))); assert ters==xg
yon=iv(mh,iv(mg,iv(mf,cikis)))           # tersleri ileri sırayla
atla_f=iv(mg,iv(mh,cikis))               # f’nin tersini uygulamamış
atla_h=iv(mf,iv(mg,cikis))               # h’nin tersini uygulamamış
carp=((cikis-mh[1])); carp=(carp-mg[1])*mg[0]; carp=(carp-mf[1])*mf[0]   # çarpmanın tersini bölme yerine çarpma
e=[yon,atla_f,atla_h,carp]; assert e==[4,29,10,342] and len({xg,*e})==5
o=['\\node[draw,thick,minimum width=1.1cm,minimum height=1.0cm] at (0,0) {$x$}; \\node[above=2pt] at (0,0.5) {Giriş};',
   kutu(2.3,0,'f','x \\mapsto 3x+2',w=2.2),kutu(5.0,0,'g','x \\mapsto 2x+1',w=2.2),kutu(7.7,0,'h','x \\mapsto x+6',w=2.2),
   f'\\node[draw,thick,minimum width=1.1cm,minimum height=1.0cm] at (10.2,0) {{${cikis}$}}; \\node[above=2pt] at (10.2,0.5) {{Çıkış}};',
   '\\draw[-{Stealth},thick] (0.6,0) -- (1.15,0); \\draw[-{Stealth},thick] (3.4,0) -- (3.9,0); \\draw[-{Stealth},thick] (6.1,0) -- (6.6,0); \\draw[-{Stealth},thick] (8.8,0) -- (9.6,0);']
SK=fig('\n'.join(o))
q('0007',tipId='fsk-zincir',tip='Ters işlem zinciri',z='orta',alt='Makine Zinciri',kaz='Art arda üç makinenin çıkışından makinelerin tersini sondan başa uygulayarak girişi bulur.',kalip='yeni nesil',
 kart='K-FSK-07 (makine zinciri) · f: 3x + 2, g: 2x + 1, h: x + 6; çıkış 65 → x = 9',
 metin='Şekildeki sistemde giriş kutusuna yazılan x sayısı sırasıyla f, g ve h makinelerinden geçerek çıkış kutusuna ulaşmaktadır. Her makine, kendisine giren sayıya üzerinde yazılı kuralı uygular.\nBuna göre giriş kutusuna yazılan x sayısı kaçtır?',
 dogru=xg,yan=[(e[0],'Tersleri çıkıştan başa değil, f’den başlayarak ileri sırayla uygulamış: h⁻¹(g⁻¹(f⁻¹(65))).','dikkat'),(e[1],'f makinesinin tersini uygulamayı unutmuş; g’nin girişini (29) cevap sanmış.','dikkat'),(e[2],'h makinesinin tersini uygulamamış: çıkışı doğrudan g’nin çıkışı sanmış; 65’ten başlayıp g ve f’nin tersini uygulamış.','dikkat'),(e[3],'Çarpmanın tersini bölme yerine çarpma yapmış: önce çıkarmış, sonra 2 ve 3 ile çarpmış.','bilgi')],
 istenen='Giriş kutusuna yazılan x sayısı.',ip=['Çıkıştan geriye doğru git; her makinenin yaptığı işlemin tersini sırasıyla uygula.'],bilgi=[TER],sekil=SK,
 ad=[A('h makinesini geri al','Çıkış, h’nin sonucudur; h’nin tersi 6 çıkarmaktır.','65 − 6 = 59'),A('g makinesini geri al','g(y) = 2y + 1 ise y = (59 − 1) ÷ 2.','y = 29'),A('f makinesini geri al','f(x) = 3x + 2 ise x = (29 − 2) ÷ 3.','x = 9'),A('Kontrol','Girişi ileri doğru yürüt.','f(9) = 29 → g(29) = 59 → h(59) = 65')],
 puf='Çıkıştan girişe gitmek için son makineden başla; her makinede önce eklenen sabiti geri al, sonra çarpanı böl.')

bitir(P,'fonksek',UK)
