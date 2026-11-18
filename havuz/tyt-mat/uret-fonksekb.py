"""Fonksiyonlar · ŞEKİLLİ ek paket b (10 soru): örüntü şekli, ok şeması, grafik, tablo, akış şeması; şekil/tablo çözüm verisini taşır.
Her doğru ve çeldirici değer kodla hesaplanıp assert edilir. Kardeş yok, ipucu 1."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
H.KONU='Fonksiyonlar'
UK='matd|Fonksiyonlar'
P=Parti('fonksekb','Fonksiyonlar',UK)
KY='ÖSYM 2018–2026 TYT Matematik (şekilli, grafikli, tablolu ve şemalı fonksiyon soruları; yalnız mantık) · MEB 9. sınıf'
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)
def fig(body,font='\\small'): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font='+font+']\n'+body+'\n\\end{tikzpicture}')
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)

# ---------- bilgi kutuları (yalnız tanım ve gösterim; örnekler soruların kurgusundan ve sayılarından farklı) ----------
ORU=B('Şekil örüntüsü','art arda şekillerde nesne sayısı her adımda aynı miktar değişiyorsa, n. şekildeki sayı n’nin doğrusal bir ifadesidir; n sıra numarasını, f(n) o şekildeki nesne sayısını gösterir. Örnek: yan yana dizilen üçgenlerde 1. şekil 3, 2. şekil 5, 3. şekil 7 çöpten oluşuyorsa her adımda çöp sayısı 2 artıyor demektir')
OKB=B('Ok şemasında bileşke ve ters','(g ∘ f)(x) = g(f(x)) yazılır: x’ten f’nin oku izlenir, varılan elemandan g’nin oku izlenir. Birebir ve örten bir fonksiyonda değer kümesinin her elemanına tam bir ok gelir. Örnek: f(2) = b, g(b) = k ise (g ∘ f)(2) = k’dır')
FON=B('Grafik ve fonksiyon','bir bağıntının grafiği, tanım kümesindeki her x değerine değer kümesinden tam bir y değeri karşılık getiriyorsa fonksiyon grafiğidir. Grafikte dolu nokta o değerin grafiğe ait olduğunu, içi boş nokta ait olmadığını gösterir. Örnek: grafikte (4, 1) dolu nokta ise f(4) = 1’dir')
KAD=B('Kırık çizgi grafik','grafik köşe noktalarında doğru değiştiren doğru parçalarından oluşur; her doğru parçasında x değeri belli bir miktar arttığında y değeri hep aynı miktarda değişir. Örnek: bir doğru parçasının uçları (0, 2) ve (4, 10) ise x = 1 iken y = 4’tür')
TAR=B('Aralık tablosu ve fonksiyon','değer tablosunda bir aralığa düşen her girişe aynı çıkış karşılık gelir. “1 – 3” aralığında üst sınır dahil deniyorsa 1’in kendisi bir önceki aralığa, 3’ün kendisi bu aralığa girer. Örnek: (0 – 2] aralığı 5, (2 – 4] aralığı 9 ise 2 için 5, 3 için 9 okunur')
FFX=B('Bileşke ve eşitlik denklemi','(f ∘ f)(x) = f(f(x)) demektir: önce x için f uygulanır, çıkan değere f yine uygulanır. f(f(x)) = k denkleminde iç değer önce bir bilinmeyen gibi düşünülür. Örnek: f(3) = 7 ise f(f(3)) = f(7)’dir')
DES=B('Aralık tablosu','girişin düştüğü aralığın karşısındaki değer çıkış olarak okunur. Örnek: 1 – 3 aralığı 20, 4 – 6 aralığı 35 ise 5 için 35 okunur')
AKI=B('Akış şeması','dikdörtgen kutu bir işlem, eşkenar dörtgen kutu bir koşul sorusudur; koşul sağlanıyorsa “Evet”, sağlanmıyorsa “Hayır” okundan ilerlenir. Örnek: “x > 0 mı?” kutusuna x = 5 ile gelen sayı “Evet” okundan, x = −1 ile gelen sayı “Hayır” okundan devam eder')

# ---------- kartlar (her tipId için bir kart) ----------
kartla('K-FSC-01','Şekil örüntüsünden kural','Şekillerde nesne sayısı sayılıp adımlar arasındaki değişimden n. şekil için kural kurulur; kural istenen sıra numarasında hesaplanır.','Başlangıç değerini 1. adımın değil 0. adımın değeri sanmak; paylaşılan elemanı iki kez saymak; sıra numarasını bir kaydırmak.','kolay','hikâyeli',3,'fkc-oruntu','Şekil örüntüsünden kural')
kartla('K-FSC-02','Ok şemasında bileşke ve ters','Her fonksiyonun okları ayrı ayrı izlenir; gösterilmeyen eşleme birebir ve örtenlikten bulunur; ters için oklar geriye doğru izlenir.','Okları izlemek yerine aynı sıradaki elemanı almak; bileşkede yalnız bir fonksiyonu uygulamak; tersi bir adımda bırakmak.','kolay','şekilli',3,'fkc-bilesok','Ok şemasında bileşke ve ters')
kartla('K-FSC-03','Grafikten fonksiyon olma','Her çizimde tanım kümesindeki her x değerine kaç değer karşılık geldiği kontrol edilir; dolu ve boş uç noktalar ayrı değerlendirilir.','Süreksizliği fonksiyon olmama sanmak; boş noktayı grafiğe dahil saymak; birebirliği fonksiyon olmanın şartı sanmak.','orta','öncüllü',4,'fkc-dikey','Grafikten fonksiyon olma')
kartla('K-FSC-04','Kademeli tarife grafiği','Kırık çizginin her parçasında birim değişim ayrı bulunur; verilen değerin hangi parçaya düştüğü belirlenip o parçada hesap yapılır.','Tek bir birim fiyatı tüm grafiğe uygulamak; yanlış doğru parçasındaki eğimi kullanmak; köşeye taşınmış değeri çıkarmamak.','orta','hikâyeli',4,'fkc-kademe','Kademeli tarife grafiği')
kartla('K-FSC-05','Aralık tablosundan ücret','Her giriş değeri tablodaki aralığa yerleştirilir; sınır değerleri için aralığın hangi uca dahil olduğuna bakılır; çıkışlar işleme göre birleştirilir.','Sınır değerini yanlış aralığa koymak; toplamı tabloya sokmak; aralığı yanlış yuvarlamak.','orta','hikâyeli',4,'fkc-tarife','Aralık tablosundan ücret')
kartla('K-FSC-06','f(f(x)) denklemi','Önce iç fonksiyonun alması gereken değerler bulunur; sonra her değer için dış denklem ayrı ayrı çözülür; tüm çözümler birleştirilir.','Yalnız tek kat denklemi çözmek; bir ara değeri atlamak; ara değeri sonuç sanmak; çözüm sayısıyla toplamı karıştırmak.','zor','tablo',4,'fkc-ikikat','f(f(x)) denklemi')
kartla('K-FSC-07','Akış şemasında koşullu işlem','Her koşul kutusu için iki kol ayrı ele alınır; bulunan bilinmeyen kolun koşulunu sağlıyorsa geçerlidir.','Koşulları denetlemeden tüm kökleri almak; Evet–Hayır kollarını ters okumak; ilk bulunan kökte bırakmak.','zor','yeni nesil',5,'fkc-akis','Akış şemasında koşullu işlem')

# ================= şekil yardımcıları =================
def graf(x0,x1,y0,y1,sx,sy,govde,xs=1,ys=1,xlab='x',ylab='y',fs='\\footnotesize',sayilar=True,kenar=False,xuz=0.7):
    o=[]
    for i in range(x0,x1+1,xs): o.append(f'\\draw[gray!35,thin] ({i*sx:.3f},{y0*sy:.3f}) -- ({i*sx:.3f},{y1*sy:.3f});')
    for j in range(y0,y1+1,ys): o.append(f'\\draw[gray!35,thin] ({x0*sx:.3f},{j*sy:.3f}) -- ({x1*sx:.3f},{j*sy:.3f});')
    o.append(f'\\draw[-{{Stealth}},thick] ({(x0-0.3*xs)*sx:.3f},0) -- ({(x1+xuz*xs)*sx:.3f},0) node[right] {{{xlab}}};')
    o.append(f'\\draw[-{{Stealth}},thick] (0,{(y0-0.3*ys)*sy:.3f}) -- (0,{(y1+0.7*ys)*sy:.3f}) node[above] {{{ylab}}};')
    if sayilar and kenar:
        for i in range(x0,x1+1,xs): o.append(f'\\node[below=2pt,font={fs}] at ({i*sx:.3f},{y0*sy:.3f}) {{${i}$}};')
        for j in range(y0,y1+1,ys): o.append(f'\\node[left=2pt,font={fs}] at ({x0*sx:.3f},{j*sy:.3f}) {{${j}$}};')
    elif sayilar:
        for i in range(x0,x1+1,xs):
            if i!=0: o.append(f'\\node[below=2pt,font={fs}] at ({i*sx:.3f},0) {{${i}$}};')
        for j in range(y0,y1+1,ys):
            if j!=0: o.append(f'\\node[left=2pt,font={fs},fill=white,inner sep=0.6pt] at (0,{j*sy:.3f}) {{${j}$}};')
    o.append(govde); return '\n'.join(o)
def ok3(Ae,Be,Ce,fp,gp,fcap='f',gcap='g'):
    """Üç sütunlu ok şeması: A→B (f oku), B→C (g oku). fp, gp: (kaynak_indis, hedef_indis) listeleri."""
    xa,xb,xc=0,3.0,6.0; vs=0.85; h=2.1; o=[]
    for x,E,n in ((xa,Ae,'A'),(xb,Be,'B'),(xc,Ce,'C')):
        o.append(f'\\draw[thick] ({x},0) ellipse (0.6 and {h}); \\node[font=\\large\\bfseries] at ({x},{h+0.4}) {{{n}}};')
        for i,e in enumerate(E): o.append(f'\\node at ({x},{(len(E)-1)/2*vs-i*vs:.3f}) {{${e}$}};')
    y=lambda E,i:(len(E)-1)/2*vs-i*vs
    for a,b in fp: o.append(f'\\draw[-{{Stealth}},thick] ({xa+0.33},{y(Ae,a):.3f}) -- ({xb-0.33},{y(Be,b):.3f});')
    for a,b in gp: o.append(f'\\draw[-{{Stealth}},thick] ({xb+0.33},{y(Be,a):.3f}) -- ({xc-0.33},{y(Ce,b):.3f});')
    o.append(f'\\node[font=\\large\\bfseries\\itshape] at ({(xa+xb)/2},{-h-0.45}) {{{fcap}}}; \\node[font=\\large\\bfseries\\itshape] at ({(xb+xc)/2},{-h-0.45}) {{{gcap}}};')
    return '\n'.join(o)

# ================= 01 kolay · şekil örüntüsü (kibrit çöpü) =================
def cop(n): return 3*n+2*(n+1)           # 2 sıra, n sütun kare: yatay 3n, dikey 2(n+1)
assert [cop(1),cop(2),cop(3)]==[7,12,17]
N=20; v=cop(N); assert v==102
e=[7+5*N,12+5*N,7*N,4*(2*N)]
assert e==[107,112,140,160] and len({v,*e})==5
s=0.8; o=[]; ox=0.0
for n in (1,2,3):
    for r in range(3):
        for i in range(n): o.append(f'\\draw[line width=2.2pt,vurgu!80!black] ({ox+i*s:.2f},{r*s:.2f}) -- ({ox+(i+1)*s:.2f},{r*s:.2f});')
    for i in range(n+1):
        for r in range(2): o.append(f'\\draw[line width=2.2pt,vurgu!80!black] ({ox+i*s:.2f},{r*s:.2f}) -- ({ox+i*s:.2f},{(r+1)*s:.2f});')
    o.append(f'\\node[font=\\small] at ({ox+n*s/2:.2f},-0.55) {{{n}. şekil}};')
    ox+=n*s+1.0
SK=fig('\n'.join(o))
q('0001',tipId='fkc-oruntu',tip='Şekil örüntüsünden kural',z='kolay',alt='Şekil Örüntüsü',kaz='Kibrit çöpleriyle oluşturulan şekil örüntüsünde nesne sayısının sıra numarasına bağlı kuralını kurup uzak bir şekildeki sayıyı hesaplar.',kalip='hikâyeli',
 kart='K-FSC-01 (kibrit çöpü örüntüsü) · iki sıra kare dizisi: 7, 12, 17 çöp; n. şekil 5n + 2',
 metin='Bir matematik kulübünde Deniz, eş kibrit çöpleriyle iki sıralı kare şeritleri oluşturuyor. Şekilde, ilk üç şerit gösterilmiştir; Deniz şeritleri aynı kurala uygun biçimde büyütmeye devam edecek ve her çöpü tam bir kenar olarak kullanacaktır.\nBuna göre 20. şerit için kaç kibrit çöpü gerekir?',
 dogru=v,yan=[(e[0],'1. şeritteki 7 çöpe 20 adım için 5’er çöp eklemiş; 20. şeride varmak için 19 adım eklenmesi gerekirken 20 adım saymış: 7 + 5 × 20.','islem'),(e[1],'2. şeritteki 12 çöpten başlayıp 20 adım için 5’er çöp eklemiş; 18 adım eklemesi gerekirken 20 adım saymış: 12 + 5 × 20.','islem'),(e[2],'Her adımda ilk şerit kadar, yani 7 çöp eklendiğini sanmış: 7 × 20.','dikkat'),(e[3],'Her kareyi ayrı çöplerle yapılmış sanıp ortak kenarları saymamış: 40 kare × 4 çöp.','dikkat')],
 istenen='20. şeritte kullanılan kibrit çöpü sayısı.',ip=['İlk üç şekildeki çöp sayılarını art arda yazıp her adımda ne kadar artış olduğuna bak.'],bilgi=[ORU],sekil=SK,
 ad=[A('Çöpleri say','Şekillerdeki kibrit çöpleri sayılır.','1. şekil 7 · 2. şekil 12 · 3. şekil 17'),A('Kuralı kur','Her adımda 5 çöp artıyor; 1. şekil 7 çöpse n. şekil 5n + 2 çöptür.','f(n) = 5n + 2'),A('20. şekle uygula','n = 20 yazılır.','5 × 20 + 2 = 102')],
 puf='Kuralı yazınca 1. şekle uygulayıp şekilden saydığın sayıyla karşılaştır.')


# ================= 02 kolay · üç kümeli ok şeması, bileşke =================
Ae,Be,Ce=[1,2,3,4],['m','n','p','r'],[10,20,30,40]
f2={1:'p',2:'r',3:'n',4:'m'}; g2={'m':20,'n':30,'p':40,'r':10}
assert sorted(f2.values())==sorted(Be) and sorted(g2.values())==sorted(Ce)
gf=lambda a:g2[f2[a]]
v=gf(1)+gf(3); assert v==70
e_pos=Ce[0]+Ce[2]                                       # okları izlemeden aynı sıradaki elemanı almış (f ve g)
e_f=g2[Be[0]]+g2[Be[2]]                                 # f için sıra, g için ok
e_g=Ce[Be.index(f2[1])]+Ce[Be.index(f2[3])]             # f için ok, g için sıra
e_kay=gf(2)+gf(4)                                       # istenmeyen girişler
e=[e_pos,e_f,e_g,e_kay]; assert e==[40,60,50,30] and len({v,*e})==5
SK=fig(ok3(Ae,Be,Ce,[(Ae.index(a),Be.index(b)) for a,b in f2.items()],[(Be.index(b),Ce.index(c)) for b,c in g2.items()]))
q('0002',tipId='fkc-bilesok',tip='Ok şemasında bileşke ve ters',z='kolay',alt='Ok Şeması Bileşke',kaz='Üç kümeli ok şemasında iki fonksiyonun oklarını art arda izleyerek bileşke değerlerini hesaplar.',kalip='hikâyeli',
 kart='K-FSC-02 (üç kümeli ok şeması) · tüm oklar verilmiş; (g ∘ f)(1) + (g ∘ f)(3)',
 metin='Bir kodlama oyununda, numaralı dört kart önce f kuralıyla harfli kartlara, ardından g kuralıyla puan kartlarına dönüştürülüyor. Şekilde A kümesi numaralı kartları, B kümesi harfli kartları, C kümesi puan kartlarını göstermekte; her kuralın bütün eşlemeleri oklarla verilmiştir.\nBuna göre (g ∘ f)(1) + (g ∘ f)(3) toplamı kaçtır?',
 dogru=v,yan=[(e[0],'Okları izlemek yerine her elemanı aynı sıradaki elemanla eşlemiş: 1 ve 3 için C’nin 1. ve 3. elemanlarını almış.','dikkat'),(e[1],'f için okları izlemeyip B’de aynı sıradaki elemanı (m ve p) almış, g’nin oklarını doğru izlemiş.','bilgi'),(e[2],'f’nin oklarını doğru izlemiş, ancak g için B’deki sıraya karşılık gelen C elemanını almış.','bilgi'),(e[3],'Sorulan girişleri karıştırıp 1 ve 3 yerine 2 ve 4’ü hesaplamış.','islem')],
 istenen='(g ∘ f)(1) + (g ∘ f)(3) toplamı.',ip=['Her giriş için önce f’nin okunu, sonra varılan elemandan çıkan g okunu ayrı ayrı izle.'],bilgi=[OKB],sekil=SK,
 ad=[A('1 için okları izle','f’nin oku B’deki bir elemana, g’nin oku C’deki bir elemana gider.','1 → p → 40'),A('3 için okları izle','Aynı yol 3 için izlenir.','3 → n → 30'),A('Topla','İki bileşke değeri toplanır.','40 + 30 = 70')],
 puf='Bileşkede her okun başladığı elemanı işaretleyip yolu elemandan elemana izle.')

# ================= 03 orta · grafikten fonksiyon olma (öncüllü) =================
def fonk_mu(G,say_acik=False):
    xs=sorted({p[0] for s_ in G['segs'] for p in s_}); T=set(xs)|{Fr(a+b,2) for a,b in zip(xs,xs[1:])}
    for x0 in T:
        ys=set(); dikey=False
        for (x1,y1),(x2,y2) in G['segs']:
            if x1==x2:
                if x1==x0: dikey=True; ys.update([Fr(y1),Fr(y2)])
                continue
            if min(x1,x2)<=x0<=max(x1,x2): ys.add(Fr(y1)+Fr(y2-y1,x2-x1)*(x0-x1))
        if not say_acik: ys-={Fr(y) for (ax,y) in G['acik'] if ax==x0}
        if dikey and len(ys)>1: return False
        if len(ys)>1: return False
    return True
def kesintisiz(G): return all(a[1]==b[0] for a,b in zip(G['segs'],G['segs'][1:]))
def birebir_mi(G):
    seen={}
    for (x1,y1),(x2,y2) in G['segs']:
        for k in range(21):
            t=Fr(k,20); x=Fr(x1)+t*(x2-x1); y=Fr(y1)+t*(y2-y1)
            if (x,y) in [(Fr(a),Fr(b)) for a,b in G['acik']]: continue
            if y in seen and seen[y]!=x: return False
            seen[y]=x
    return True
GI=dict(segs=[((-3,3),(-1,-2)),((-1,-2),(1,1)),((1,1),(3,3))],acik=[],nokta=[(-3,3),(3,3)])
GII=dict(segs=[((-3,-3),(1,-1)),((1,2),(3,4))],acik=[(1,2)],nokta=[(-3,-3),(1,-1),(3,4)])
GIII=dict(segs=[((-3,-1),(0,1)),((0,1),(0,-2)),((0,-2),(3,2))],acik=[],nokta=[(-3,-1),(3,2)])
GG=[GI,GII,GIII]; RO=['I','II','III']
kume=lambda kural:' ve '.join(r for r,G_ in zip(RO,GG) if kural(G_)) if sum(1 for G_ in GG if kural(G_))<3 else None
ad_=lambda L:('Yalnız '+L[0]) if len(L)==1 else (' ve '.join(L) if len(L)==2 else ', '.join(L[:-1])+' ve '+L[-1])
def kk(kural): return ad_([r for r,G_ in zip(RO,GG) if kural(G_)])
dog=kk(lambda G_:fonk_mu(G_)); k_ke=kk(lambda G_:kesintisiz(G_)); k_ac=kk(lambda G_:fonk_mu(G_,say_acik=True)); k_br=kk(lambda G_:birebir_mi(G_)); k_hepsi=ad_(RO)
assert [dog,k_ke,k_ac,k_br,k_hepsi]==['I ve II','I ve III','Yalnız I','Yalnız II','I, II ve III'],[dog,k_ke,k_ac,k_br]
sira=['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III']
o=[]; sx=0.4
for p,G_ in enumerate(GG):
    sc=[f'\\begin{{scope}}[xshift={p*3.45}cm]']
    g_=[]
    for (a,b) in G_['segs']: g_.append(f'\\draw[line width=1.6pt] ({a[0]*sx:.2f},{a[1]*sx:.2f}) -- ({b[0]*sx:.2f},{b[1]*sx:.2f});')
    for x,y in G_['nokta']: g_.append(f'\\fill ({x*sx:.2f},{y*sx:.2f}) circle (0.07);')
    for x,y in G_['acik']: g_.append(f'\\draw[thick,fill=white] ({x*sx:.2f},{y*sx:.2f}) circle (0.075);')
    sc.append(graf(-3,3,-3,4,sx,sx,'\n'.join(g_),xlab='$x$',ylab='$y$',sayilar=False))
    sc.append(f'\\node[font=\\normalsize\\bfseries] at (0,{-3.75*sx-0.25:.2f}) {{{RO[p]}}};\\end{{scope}}')
    o.append('\n'.join(sc))
SK=fig('\n'.join(o))
q('0003',tipId='fkc-dikey',tip='Grafikten fonksiyon olma',z='orta',alt='Grafikten Fonksiyon Olma',kaz='Koordinat düzlemindeki grafiklerde dolu ve boş uç noktalarını da dikkate alarak hangilerinin fonksiyon grafiği olduğunu belirler.',kalip='öncüllü',
 kart='K-FSC-03 (üç grafik) · I kırık çizgi, II boş ve dolu noktalı sıçrama, III dikey parçalı çizim',
 metin='Bir öğretmen, gerçel sayıların [−3, 3] aralığında çizilmiş üç grafiği tahtaya asıyor. Grafiklerde doğru parçalarının uçları kılavuz çizgilerinin kesişimindedir; içi dolu nokta o noktanın grafiğe ait olduğunu, içi boş nokta ait olmadığını göstermektedir. Öğretmen, öğrencilerden bu grafiklerin hangilerinin her x değerine tam bir y değeri karşılık getirdiğini bulmalarını istiyor.\nBuna göre I, II ve III numaralı grafiklerden hangileri [−3, 3] aralığında tanımlı bir fonksiyonun grafiğidir?',
 dogru=dog,yan=[(sira[0],'İçi boş noktayı da grafiğe ait sayıp II’de x = 1 değerine iki y değeri karşılık geldiğini düşünmüş; III’ü de dikey parçası nedeniyle dışarıda bırakmış.','bilgi'),(sira[1],'Grafiğin her yatay doğruyu en fazla bir kez kesmesi gerektiğini sanmış (birebirlik); bu şart yalnız II’de sağlanıyor.','bilgi'),(sira[3],'Fonksiyonu kesintisiz çizim sanmış: II’deki sıçramayı eleyip kesintisiz çizilen I ve III’ü seçmiş; III’teki dikey parçayı fark etmemiş.','dikkat'),(sira[4],'Her çizimin tanımlı olduğuna bakıp bir x’e birden çok değer gelip gelmediğini denetlememiş.','dikkat')],
 sira=sira,istenen='Fonksiyon grafiği olanlar.',ip=['Her grafikte bir x değerini seç ve o x’e grafikte kaç farklı değerin karşılık geldiğine bak.'],bilgi=[FON],sekil=SK,
 ad=[A('I’i incele','Her x değerine grafikte tek bir y değeri karşılık gelir.','fonksiyon'),A('II’yi incele','x = 1’de dolu noktanın yanı sıra içi boş nokta var; boş nokta grafiğe ait değildir.','fonksiyon'),A('III’ü incele','x = 0’da dikey parça, birden çok değer içeriyor.','fonksiyon değil'),A('Sonuç','I ve II fonksiyon grafiğidir.','I ve II')],
 puf='Boş noktayı grafiğe dahil etmeden her x için karşılık gelen değerleri say.')

# ================= 04 orta · kademeli su tarifesi grafiği =================
V4=[(0,0),(10,50),(25,200),(35,400)]
sl=[Fr(V4[i+1][1]-V4[i][1],V4[i+1][0]-V4[i][0]) for i in range(3)]; assert sl==[5,10,20]
B4=340; v=V4[2][0]+Fr(B4-V4[2][1],sl[2]); assert v==32 and V4[2][1]<B4<V4[3][1]
e=[Fr(B4,sl[0]),V4[1][0]+Fr(B4-V4[1][1],sl[1]),Fr(B4,sl[2]),V4[2][0]+Fr(B4-V4[2][1],sl[0])]
assert e==[68,39,17,53] and len({v,*e})==5
sx,sy=0.2,0.0125
g_=['\\draw[line width=1.6pt] '+' -- '.join(f'({x*sx:.3f},{y*sy:.3f})' for x,y in V4)+';']
for x,y in V4[1:]: g_.append(f'\\draw[dashed,gray] ({x*sx:.3f},0) -- ({x*sx:.3f},{y*sy:.3f}) -- (0,{y*sy:.3f});')
for x,y in V4: g_.append(f'\\fill ({x*sx:.3f},{y*sy:.3f}) circle (0.08);')
SK=fig(graf(0,40,0,400,sx,sy,'\n'.join(g_),xs=5,ys=50,xlab='Tüketim (m$^3$)',ylab='Fatura (TL)'))
q('0004',tipId='fkc-kademe',tip='Kademeli tarife grafiği',z='orta',alt='Kademeli Tarife',kaz='Kırık çizgi grafikle verilen kademeli tarifede fatura tutarından tüketim miktarını bulur.',kalip='hikâyeli',
 kart='K-FSC-04 (kademeli su faturası) · köşeler (0, 0), (10, 50), (25, 200), (35, 400); fatura 340 TL',
 metin='Bir belediye, su tüketimini üç kademeye ayırarak ücretlendirmektedir. Şekildeki grafik, bir abonenin aylık su faturasının (sabit bedel yoktur) tüketim miktarına göre nasıl değiştiğini göstermektedir; grafikte işaretli köşe noktaları kılavuz çizgilerinin kesişimindedir. Bu ay Hakan Bey’in faturası 340 TL gelmiştir.\nBuna göre Hakan Bey bu ay kaç m³ su tüketmiştir?',
 dogru=v,yan=[(e[0],'Tüm tüketime ilk kademenin birim fiyatını uygulamış: 340 ÷ 5.','dikkat'),(e[1],'Son kademede de ikinci kademenin eğimini kullanmış: ikinci doğru parçasını 340 TL’ye kadar uzatmış.','bilgi'),(e[2],'Tüm tüketime son kademenin birim fiyatını uygulamış: 340 ÷ 20.','dikkat'),(e[3],'Son kademede ilk kademenin birim fiyatını kullanmış: 25 m³’ten sonra kalan tutarı 5’e bölmüş.','bilgi')],
 istenen='Hakan Bey’in bu ay tükettiği su miktarı (m³).',ip=['340 TL’nin grafikte hangi doğru parçasına denk geldiğini belirleyip o parçanın değişimini incele.'],bilgi=[KAD],sekil=SK,
 ad=[A('Köşeleri oku','Grafiğin köşe noktaları okunur.','(10, 50), (25, 200), (35, 400)'),A('Doğru parçasını seç','340 TL, 25 m³’teki 200 TL ile 35 m³’teki 400 TL arasında kalır.','son parça'),A('Birim fiyatı bul','Son parçada 10 m³ için 200 TL artış var.','200 ÷ 10 = 20 TL/m³'),A('Tüketimi hesapla','25 m³’ten sonra kalan tutar bu fiyata bölünür.','25 + (340 − 200) ÷ 20 = 32')],
 puf='Önce verilen tutarın hangi köşeler arasında kaldığını belirle, sonra yalnız o parçanın değişimini kullan.')

# ================= 05 orta · otopark tarifesi tablosu =================
UC=[(1,25),(3,40),(6,55),(10,75),(24,140)]
def ucret(dk,ust_dahil=True):
    for i,(ust,tl) in enumerate(UC):
        if (dk<=ust*60) if ust_dahil else (dk<ust*60): return tl
    raise ValueError
tm=lambda s:int(s[:2])*60+int(s[3:])
car=[('09:10','10:10'),('11:00','14:20'),('13:15','19:15')]; sure=[tm(b)-tm(a) for a,b in car]; assert sure==[60,200,360]
v=sum(ucret(d) for d in sure); assert v==25+55+55==135
e=[sum(ucret(d,False) for d in sure),ucret(sure[0],False)+ucret(sure[1])+ucret(sure[2]),ucret(sure[0])+ucret(180)+ucret(sure[2]),ucret(sum(sure))]
assert e==[170,150,120,140] and len({v,*e})==5
SK=tablo_svg(['Park süresi (saat)','Ücret (TL)'],[['0 – 1','25'],['1 – 3','40'],['3 – 6','55'],['6 – 10','75'],['10 – 24','140']])
q('0005',tipId='fkc-tarife',tip='Aralık tablosundan ücret',z='orta',alt='Otopark Tarifesi',kaz='Süre aralıklarına göre belirlenen ücret tablosunda sınır değerlerini doğru aralığa yerleştirerek toplam ücreti hesaplar.',kalip='hikâyeli',
 kart='K-FSC-05 (otopark tarifesi) · aralıklar (0,1], (1,3], (3,6], (6,10], (10,24]; süreler 1 sa, 3 sa 20 dk, 6 sa',
 metin='Bir alışveriş merkezinin otoparkında ücret, aracın otoparkta kaldığı süreye göre aşağıdaki tabloda verilmiştir; her aralığın üst sınırı o aralığa dahil, alt sınırı dahil değildir. Ahmet’in aracı 09:10’da girip 10:10’da, Berk’inki 11:00’da girip 14:20’de, Cansu’nunki 13:15’te girip 19:15’te çıkmıştır. Her araç aynı gün içinde otoparka tek girişle park etmiş, ücretler araçlar için ayrı ayrı ödenmiştir.\nBuna göre bu üç araç için otoparka toplam kaç TL ödenmiştir?',
 dogru=v,yan=[(e[0],'Tam saatlerde bitiş süresini bir üst aralığa yazmış: 1 saati ve 6 saati sonraki aralıkta okumuş.','dikkat'),(e[1],'Yalnız tam 1 saatlik süreyi ikinci aralıkta okumuş; 6 saati doğru yerleştirmiş.','dikkat'),(e[2],'3 saat 20 dakikayı 3 saat sayıp ikinci aralıktan ücret almış.','bilgi'),(e[3],'Üç aracın sürelerini toplayıp tek araçmış gibi tabloya sokmuş.','bilgi')],
 istenen='Toplam otopark ücreti (TL).',ip=['Her aracın kaldığı süreyi dakikaya çevirip saatlerle karşılaştır.'],bilgi=[TAR],sekil=SK,
 ad=[A('Süreleri bul','Çıkış saatinden giriş saati çıkarılır.','Ahmet 1 sa · Berk 3 sa 20 dk · Cansu 6 sa'),A('Aralıkları belirle','Üst sınır aralığa dahil olduğundan 1 saat ilk aralığa, 6 saat üçüncü aralığa girer.','1 saat: ilk aralık · 3 sa 20 dk: üçüncü aralık · 6 saat: üçüncü aralık'),A('Ücretleri oku','Tablodan ücretler okunur.','25 · 55 · 55 TL'),A('Topla','Üç ücret toplanır.','25 + 55 + 55 = 135')],
 puf='Sınır değerlerini tabloya yerleştirirken aralıkların hangi uca dahil olduğuna yeniden bak.')

# ================= 06 zor · tablo, f(f(x)) = x =================
fT={1:4,2:2,3:5,4:1,5:6,6:3}; assert sorted(fT.values())==list(range(1,7))
ff=lambda x:fT[fT[x]]
cz=[x for x in fT if ff(x)==x]; assert cz==[1,2,4]; v=sum(cz)
e_fix=sum(x for x in fT if fT[x]==x)
e_say=len(cz)
inv={b:a for a,b in fT.items()}
e_tum=sum(x for x in fT if inv[fT[x]]==x)       # bileşkeyi tablonun satırlarını ters okuyarak yapmış
e_uc=sum(x for x in fT if fT[fT[fT[x]]]==x)
e=[e_fix,e_say,e_tum,e_uc]; assert e==[2,3,21,16] and v==7 and len({v,*e})==5
SK=tablo_svg(['x','1','2','3','4','5','6'],[['f(x)']+[str(fT[i]) for i in range(1,7)]])
q('0006',tipId='fkc-ikikat',tip='f(f(x)) denklemi',z='orta',alt='f(f(x)) Denklemi',kaz='Tabloyla verilen fonksiyonda f(f(x)) = x eşitliğini sağlayan elemanları bileşke ile belirleyip toplar.',kalip='tablo',
 kart='K-FSC-06 (tablo) · f = (4, 2, 5, 1, 6, 3); f(f(x)) = x çözümleri 1, 2, 4',
 metin='A = {1, 2, 3, 4, 5, 6} kümesinden kendisine tanımlı f fonksiyonu aşağıdaki tabloda verilmiştir.\nBuna göre f(f(x)) = x eşitliğini sağlayan x ∈ A değerlerinin toplamı kaçtır?',
 dogru=v,yan=[(e[0],'Yalnız f(x) = x olan elemanı bulmuş (2); bileşke koşulunu tek kat uygulamış.','dikkat'),(e[1],'Çözümlerin toplamı yerine çözüm sayısını yazmış.','islem'),(e[2],'f(f(x)) = x eşitliğinin her x için sağlandığını sanıp A’nın bütün elemanlarını toplamış: 1 + 2 + … + 6.','bilgi'),(e[3],'f’yi iki kez değil üç kez uygulayıp f(f(f(x))) = x denklemini çözmüş.','dikkat')],
 istenen='f(f(x)) = x eşitliğini sağlayan x değerlerinin toplamı.',ip=['Her x için tablodan f(x) değerini, sonra bu değerin f ile eşini oku; sonuç x’e dönüyor mu?'],bilgi=[FFX],sekil=SK,
 ad=[A('x = 1 için bak','f(1) = 4 ve f(4) = 1.','f(f(1)) = 1 sağlar'),A('x = 2 için bak','f(2) = 2 ve f(2) = 2.','f(f(2)) = 2 sağlar'),A('x = 4 için bak','f(4) = 1 ve f(1) = 4.','f(f(4)) = 4 sağlar'),A('Kalanları ele','3 → 5 → 6, 5 → 6 → 3, 6 → 3 → 5 olduğundan 3, 5 ve 6 sağlamaz.','çözümler 1, 2, 4'),A('Topla','Sağlayan değerler toplanır.','1 + 2 + 4 = 7')],
 puf='Tablodaki bir değerden başlayıp iki adım sonra nereye varıldığını izle.')

# ================= 07 zor · akış şeması, koşullu işlem =================
t1,a1,b1,c1,t2,d2,k2,Z=3,2,-1,5,8,6,3,9
f1=lambda x:(a1*x+b1 if x>=t1 else x+c1)
f2_=lambda y:(y-d2 if y>t2 else k2*y)
ZZ=lambda x:f2_(f1(x))
def kok(chk1=True,chk2=True,sw1=False):
    R=[]
    for c2,y in [(True,Fr(Z+d2)),(False,Fr(Z,k2))]:
        if chk2 and (y>t2)!=c2: continue
        for c1_,x in [(True,Fr(y-b1,a1)),(False,y-c1)]:
            if chk1 and ((x>=t1)==c1_)==sw1: continue
            R.append(x)
    return R
tr=kok(); assert tr==[8,-2] and all(ZZ(x)==Z for x in tr); v=sum(tr); assert v==6
# bütün olası x’ler arasında başka çözüm yok (tarama)
for xx in [Fr(i,2) for i in range(-80,81)]: assert (ZZ(xx)==Z)==(xx in tr),xx
e_hic=sum(kok(False,False)); e_tek=tr[0]; e_sw=sum(kok(True,True,True))
e_ev=sum(x for c2,y in [(True,Fr(Z+d2)),(False,Fr(Z,k2))] if (y>t2)==c2 for x in [Fr(y-b1,a1)])
e=[e_hic,e_tek,e_sw,e_ev]; assert e==[18,8,12,10] and len({v,*e})==5
o=['\\tikzset{kt/.style={draw,thick,rounded corners=2pt,minimum width=2.3cm,minimum height=0.7cm,align=center},kr/.style={draw,thick,diamond,aspect=2.3,inner sep=1pt,align=center},ok/.style={-{Stealth},thick}}',
 '\\node[kt,rounded corners=8pt] (s) at (0,0) {Giriş: $x$};',
 f'\\node[kr] (d1) at (0,-1.7) {{$x\\geq {t1}$ mü?}};',
 f'\\node[kt] (a) at (-2.6,-3.4) {{$y=x+{c1}$}}; \\node[kt] (b) at (2.6,-3.4) {{$y={a1}x-{-b1}$}};',
 f'\\node[kr] (d2) at (0,-5.1) {{$y>{t2}$ mı?}};',
 f'\\node[kt] (c) at (-2.6,-6.8) {{$z={k2}y$}}; \\node[kt] (dd) at (2.6,-6.8) {{$z=y-{d2}$}};',
 '\\node[kt,rounded corners=8pt] (e) at (0,-8.3) {Çıkış: $z$};',
 '\\draw[ok] (s) -- (d1);',
 '\\draw[ok] (d1.west) -| node[pos=0.25,above,font=\\footnotesize] {Hayır} (a.north);',
 '\\draw[ok] (d1.east) -| node[pos=0.25,above,font=\\footnotesize] {Evet} (b.north);',
 '\\draw[thick] (a.south) |- (0,-4.2); \\draw[thick] (b.south) |- (0,-4.2); \\draw[ok] (0,-4.2) -- (d2.north);',
 '\\draw[ok] (d2.west) -| node[pos=0.25,above,font=\\footnotesize] {Hayır} (c.north);',
 '\\draw[ok] (d2.east) -| node[pos=0.25,above,font=\\footnotesize] {Evet} (dd.north);',
 '\\draw[ok] (c.south) |- (e.west); \\draw[ok] (dd.south) |- (e.east);']
SK=fig('\n'.join(o),font='\\small')
q('0007',tipId='fkc-akis',tip='Akış şemasında koşullu işlem',z='zor',alt='Akış Şeması',kaz='İki koşul kutulu akış şemasında çıkış değerini veren giriş değerlerini koşulları denetleyerek bulur ve toplar.',kalip='yeni nesil',
 kart='K-FSC-07 (akış şeması) · iki koşul kutusu; x ≥ 3 ve y > 8; çıkış 9 → x ∈ {−2, 8}',
 metin='Şekildeki akış şemasına bir x gerçel sayısı girilmekte ve şemanın gösterdiği yolla işlemler yapılarak çıkış değeri bulunmaktadır; eşkenar dörtgen kutular koşul sorusudur, koşul sağlanıyorsa “Evet”, sağlanmıyorsa “Hayır” okuyla ilerlenir.\nÇıkış kutusundaki z sayısı 9 olduğuna göre bu sonucu veren x değerlerinin toplamı kaçtır?',
 dogru=v,yan=[(e[0],'Koşul kutularını denetlemeden dört kolun hepsinden bulduğu x değerlerini toplamış: 8, 10, 2 ve −2.','dikkat'),(e[1],'Yalnız “Evet–Evet” yolunu çözüp bulduğu ilk değerde bırakmış: 8.','dikkat'),(e[2],'İlk koşul kutusunda “Evet” ve “Hayır” kollarını ters okumuş; böylece 10 ve 2’yi geçerli saymış.','bilgi'),(e[3],'İlk koşul kutusunda her zaman “Evet” kolunu izlemiş: 2x − 1 = 15 ve 2x − 1 = 3 denklemlerinden 8 ve 2’yi geçerli saymış.','bilgi')],
 istenen='z = 9 olduğunda giriş değerlerinin toplamı.',ip=['Çıkış değerinin hangi kutudan ve hangi koşulda üretilebildiğini düşün.'],bilgi=[AKI],sekil=SK,
 ad=[A('İkinci kutuyu çöz','z = 9 için iki kol da denenir.','y − 6 = 9 → y = 15 · 3y = 9 → y = 3'),A('Koşulları denetle','y = 15 için y > 8 doğru, y = 3 için y > 8 yanlış olduğundan iki değer de ilgili kolda geçerli.','y = 15 ve y = 3 geçerli'),A('İlk kutuyu çöz','Her y için iki kol denenir: 2x − 1 = 15 → 8, x + 5 = 15 → 10, 2x − 1 = 3 → 2, x + 5 = 3 → −2.','x ∈ {8, 10, 2, −2}'),A('Koşulları denetle','8 için x ≥ 3 doğru; 10 için x ≥ 3 doğru olduğundan Hayır kolunda olamaz; 2 için x ≥ 3 yanlış olduğundan Evet kolunda olamaz; −2 için x ≥ 3 yanlış, Hayır kolu doğru.','geçerli: 8 ve −2'),A('Topla','Geçerli değerler toplanır.','8 + (−2) = 6')],
 puf='Bulduğun her değeri, geldiği koşul kutusunun koşuluna geri koyarak sına.')

# ================= 08 zor · üç kümeli ok şeması, eksik okla bileşke ve ters =================
A8,B8,C8=[1,2,3,4],[5,6,7,8],[10,20,30,40]
f8={1:7,2:5,3:8,4:6}; g8={5:30,6:10,7:40,8:20}
assert sorted(f8.values())==B8 and sorted(g8.values())==C8
fd={a:b for a,b in f8.items() if a!=1}; gd={b:c for b,c in g8.items() if b!=7}          # şekilde verilenler
fi=[b for b in B8 if b not in fd.values()]; assert fi==[7]                               # f(1) kalan elemanla
gi=[c for c in C8 if c not in gd.values()]; assert gi==[40] and f8[1]==7                 # g(7) kalan elemanla
gf=lambda a:g8[f8[a]]; gfi=lambda c:[a for a in A8 if gf(a)==c][0]
t_a=gf(1); t_b=gfi(20); assert (t_a,t_b)==(40,3); v=t_a+t_b
e_a=t_a; e_gi=t_a+[b for b in B8 if g8[b]==20][0]; e_f=f8[1]+t_b; e_fg=f8[1]+[b for b in B8 if g8[b]==20][0]
e=[e_a,e_gi,e_f,e_fg]; assert (v,e)==(43,[40,48,10,15]) and len({v,*e})==5
SK=fig(ok3(A8,B8,C8,[(A8.index(a),B8.index(b)) for a,b in fd.items()],[(B8.index(b),C8.index(c)) for b,c in gd.items()]))
q('0008',tipId='fkc-bilesok',tip='Ok şemasında bileşke ve ters',z='orta',alt='Eksik Okla Bileşke',kaz='Birebir ve örten iki fonksiyonun ok şemasında eksik eşlemeleri bularak bileşke ve bileşkenin tersi değerlerini hesaplar.',kalip='şekilli',
 kart='K-FSC-02 (eksik oklu ok şeması) · f(1) ve g(7) çizilmemiş; (g ∘ f)(1) + (g ∘ f)⁻¹(20)',
 metin='A, B ve C kümeleri arasındaki f: A → B ve g: B → C fonksiyonları birebir ve örtendir. Şekilde, f ve g fonksiyonlarının eşlemelerinden yalnızca bazıları oklarla gösterilmiştir;\nBuna göre (g ∘ f)(1) + (g ∘ f)⁻¹(20) toplamı kaçtır?',
 dogru=v,yan=[(e[0],'Yalnız birinci terimi hesaplayıp ikinci terimi toplama katmamış.','dikkat'),(e[1],'İkinci terimde (g ∘ f)⁻¹(20) için yalnızca g⁻¹(20) değerini bulup f⁻¹ adımını uygulamamış.','bilgi'),(e[2],'Birinci terimde yalnız f(1) değerini bulup g adımını uygulamamış; ikinci terimi doğru bulmuş.','dikkat'),(e[3],'Her iki terimde de son adımı atlamış: f(1) ile g⁻¹(20) değerlerini toplamış.','bilgi')],
 istenen='(g ∘ f)(1) + (g ∘ f)⁻¹(20) toplamı.',ip=['Birebir ve örten olmak her kümede oklar için ne anlama gelir?'],bilgi=[OKB],sekil=SK,
 ad=[A('f(1)’i bul','B’de ok almayan tek eleman 1’in eşidir.','f(1) = 7'),A('g(7)’yi bul','C’de ok almayan tek eleman 7’nin eşidir.','g(7) = 40 → (g ∘ f)(1) = 40'),A('Tersin yolunu izle','20’ye ok gönderen B elemanı, sonra bu elemana ok gönderen A elemanı bulunur.','g⁻¹(20) = 8 → f⁻¹(8) = 3'),A('Topla','İki değer toplanır.','40 + 3 = 43')],
 puf='Bileşkenin tersinde oklar bileşkenin tersine, yani önce g’nin sonra f’nin okları geriye doğru izlenir.')

# ================= 09 zor · kargo tablosu, desi =================
TB=[(3,45),(6,60),(10,85),(20,130)]
def kargo(desi):
    for ust,tl in TB:
        if desi<=ust: return tl
    raise ValueError
paket=[((30,20,25),3),((40,30,15),8),((20,20,15),4)]
hd=lambda d:Fr(d[0]*d[1]*d[2],3000)
for d,kg in paket: assert hd(d).denominator==1
des=[max(hd(d),kg) for d,kg in paket]; assert des==[5,8,4]
v=sum(kargo(x) for x in des); assert v==60+85+60==205
e_kg=sum(kargo(kg) for d,kg in paket); e_hc=sum(kargo(hd(d)) for d,kg in paket); e_top=kargo(sum(des)); e_min=sum(kargo(min(hd(d),kg)) for d,kg in paket)
e=[e_top,e_min,e_hc,e_kg]; assert e==[130,150,165,190] and len({v,*e})==5
SK=tablo_svg(['Desi aralığı','Ücret (TL)'],[['1 – 3','45'],['4 – 6','60'],['7 – 10','85'],['11 – 20','130']])
q('0009',tipId='fkc-tarife',tip='Aralık tablosundan ücret',z='orta',alt='Kargo Tarifesi',kaz='Hacimsel desi ve ağırlıktan büyük olanı seçerek her koli için desi bulur, tablodan ücretleri okuyup toplar.',kalip='hikâyeli',
 kart='K-FSC-05 (kargo tarifesi) · desi = max(hacim ÷ 3000, kg); 4 aralıklı ücret tablosu; üç koli',
 metin='Bir internet mağazası, siparişlerini kolilere ayırarak kargoya vermektedir. Kargo firması, bir kolinin desisini hacmin (en × boy × yükseklik, cm³ cinsinden) 3000’e bölünmesiyle bulduğu sayı ile kolinin ağırlığının (kg) sayısal değerinden büyük olanı olarak belirlemekte ve ücreti aşağıdaki tablodan okumaktadır. Mağaza; 30 × 20 × 25 cm ölçülerinde 3 kg’lık, 40 × 30 × 15 cm ölçülerinde 8 kg’lık ve 20 × 20 × 15 cm ölçülerinde 4 kg’lık üç koliyi ayrı ayrı göndermektedir.\nBuna göre üç koli için kargo firmasına toplam kaç TL ödenir?',
 dogru=v,yan=[(e[0],'Üç kolinin desilerini toplayıp toplam desiyi tek bir kolinin desisi gibi tabloya sokmuş.','bilgi'),(e[1],'Desi olarak iki sayıdan küçüğünü almış.','dikkat'),(e[2],'Yalnız hacimsel desiye bakıp ağırlığı hiç hesaba katmamış.','dikkat'),(e[3],'Yalnız ağırlığa bakıp hacimsel desiyi hesaba katmamış.','dikkat')],
 istenen='Üç koli için ödenecek toplam kargo ücreti (TL).',ip=['Her koli için iki ayrı sayı bulup kuralın hangisini seçtiğine dikkat et; ücretleri ancak sonra topla.'],bilgi=[DES],sekil=SK,
 ad=[A('Hacimsel desileri bul','Hacim 3000’e bölünür.','15000 ÷ 3000 = 5 · 18000 ÷ 3000 = 6 · 6000 ÷ 3000 = 2'),A('Desiyi belirle','Her kolide hacimsel desi ile kg sayısından büyük olan alınır.','5 · 8 · 4'),A('Ücretleri oku','Tabloda 5 desi 4–6 aralığında, 8 desi 7–10 aralığında, 4 desi 4–6 aralığındadır.','60 · 85 · 60'),A('Topla','Üç ücret toplanır.','60 + 85 + 60 = 205')],
 puf='Tablo, desi değeri için bir ücret verir; koliler ayrı ayrı gönderildiğinden ücretler desiler toplanmadan okunur.')

# ================= 10 zor · grafik, f(f(x)) = k =================
V10=[(-4,3),(-2,-1),(0,1),(2,-3),(4,0)]
def coz(k):
    r=[]
    for (x1,y1),(x2,y2) in zip(V10,V10[1:]):
        if y1!=y2 and min(y1,y2)<=k<=max(y1,y2):
            x=Fr(x1)+Fr(k-y1,y2-y1)*(x2-x1)
            if x not in r: r.append(x)
    return r
KK=1; us=coz(KK); assert us==[-3,0]
xs=sorted({x for u in us for x in coz(u)}); assert xs==[Fr(-5,2),-1,Fr(1,2),2,4] and sum(xs)==3; v=sum(xs)
e_u=sum(us); e_say=len(xs); e_a=sum(coz(us[0])); e_b=sum(coz(us[1]))
e=[e_u,e_say,e_a,e_b]; assert e==[-3,5,2,1] and len({v,*e})==5
sx=0.55
g_=['\\draw[line width=1.6pt] '+' -- '.join(f'({x*sx:.3f},{y*sx:.3f})' for x,y in V10)+';']
for x,y in V10: g_.append(f'\\fill ({x*sx:.3f},{y*sx:.3f}) circle (0.08);')
SK=fig(graf(-4,4,-3,3,sx,sx,'\n'.join(g_),ylab='$y=f(x)$',kenar=True,xuz=1.4))
q('0010',tipId='fkc-ikikat',tip='f(f(x)) denklemi',z='zor',alt='Grafikte f(f(x))',kaz='Kırık çizgi grafikle verilen fonksiyonda f(f(x)) = k denkleminin çözümlerini iki aşamada bulup toplar.',kalip='grafik',
 kart='K-FSC-06 (kırık çizgi grafik) · köşeler (−4, 3), (−2, −1), (0, 1), (2, −3), (4, 0); f(f(x)) = 1',
 metin='Şekilde, [−4, 4] aralığında tanımlı f fonksiyonunun grafiği verilmiştir; grafik, uçları kılavuz çizgilerinin kesişiminde olan doğru parçalarından oluşmaktadır.\nBuna göre f(f(x)) = 1 denklemini sağlayan x değerlerinin toplamı kaçtır?',
 dogru=v,yan=[(e[0],'Denklemi yalnız f(u) = 1 biçiminde çözüp u değerlerini sonuç sanmış: −3 ve 0’ı toplamış.','dikkat'),(e[1],'Çözümlerin toplamı yerine çözüm sayısını yazmış.','islem'),(e[2],'f(u) = 1 için bulduğu iki değerden yalnızca ilkini (−3) kullanıp f(x) = −3 denklemini çözmüş.','bilgi'),(e[3],'Bulduğu iki değerden yalnızca 0’ı kullanıp f(x) = 0 denklemini çözmüş; −3 değerini atlamış.','bilgi')],
 istenen='f(f(x)) = 1 denklemini sağlayan x değerlerinin toplamı.',ip=['Denklemi iki aşamaya ayırmanın bir yolu var mı?'],bilgi=[FFX],sekil=SK,
 ad=[A('İç değeri bul','f(u) = 1 olan u değerleri grafikten bulunur.','u = −3 ve u = 0'),A('f(x) = −3 çöz','Grafikte yalnız (2, −3) köşesi bu değerdedir.','x = 2'),A('f(x) = 0 çöz','Her doğru parçasında 0 değeri ayrı ayrı bulunur; kesişimler x ekseninde yer alır.','x = −5/2, −1, 1/2, 4'),A('Toplam','Bütün çözümler toplanır.','2 + (−5/2) + (−1) + 1/2 + 4 = 3')],
 puf='Bulduğun ara değerlerin her biri için ayrı denklemi çözmeyi unutma.')

bitir(P,'fonksekb',UK)
