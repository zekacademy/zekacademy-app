"""AYT Matematik · Logaritma (üstel ve logaritmik fonksiyonlar dahil) · 20 soruluk paket (4 kolay / 10 orta / 6 zor).
Her doğru cevap ve çeldirici değer kodla hesaplanıp assert edilir; şekiller TikZ ile aynı sayılardan üretilir.
Kardeş yok, ipucu 1. Çıktı: ayt-mat/loga-1.json, kartlar/loga.json."""
import sys,os,math,json
MD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.dirname(MD)
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
H.KONU='Logaritma'
UK='amat|Logaritma'
P=Parti('loga','Logaritma',UK,ders='AYT Matematik',idon='aytmat')
KY='ÖSYM 2018–2026 AYT Matematik (Üstel ve Logaritmik Fonksiyonlar; yalnız mantık) · Bilgi Sarmal ve Acil AYT soru bankaları (yalnız mantık) · MEB 11–12. sınıf'
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)
COL=r'\definecolor{mavi}{HTML}{2563EB}\definecolor{turu}{HTML}{EA580C}\definecolor{mor}{HTML}{7C3AED}\definecolor{yesil}{HTML}{15803D}'
def fig(body,font='\\small'): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font='+font+']\n'+COL+'\n'+body+'\n\\end{tikzpicture}')
def lg(x,b): return math.log(x)/math.log(b)

# ---------- bilgi kutuları (yalnız tanım ve gösterim; örnekler soruların sayılarından farklı) ----------
TAN=B('Logaritmanın tanımı','a > 0, a ≠ 1 ve b > 0 olmak üzere logₐb = c ⇔ aᶜ = b. Logaritma bir üs bulma işlemidir. Örnek: log₂32 = 5 çünkü 2⁵ = 32; log₃(1/9) = −2 çünkü 3⁻² = 1/9')
OZL=B('Logaritma özellikleri','logₐ(m·n) = logₐm + logₐn · logₐ(m/n) = logₐm − logₐn · logₐ(mᵏ) = k·logₐm. Taban değiştirme: logₐb = (log_c b) ÷ (log_c a). Örnek: log₆4 + log₆9 = log₆36 = 2; log₈16 = (log₂16) ÷ (log₂8) = 4/3')
UST=B('Üstel fonksiyon','a > 0 ve a ≠ 1 olmak üzere f(x) = aˣ fonksiyonu a > 1 için artan, 0 < a < 1 için azalandır; grafiği (0, 1) noktasından geçer ve x-ekseni yatay asimptottur. aᵐ·aⁿ = aᵐ⁺ⁿ. Örnek: 5ˣ⁺¹ = 5·5ˣ ve 5ˣ⁻² = 5ˣ ÷ 25')
LOF=B('Logaritma fonksiyonu','f(x) = logₐx fonksiyonu x > 0 için tanımlıdır; a > 1 ise artan, 0 < a < 1 ise azalandır; grafiği (1, 0) noktasından geçer ve y-ekseni dikey asimptottur. f(x) = logₐx ile g(x) = aˣ birbirinin ters fonksiyonudur. Örnek: f(x) = log₃x ise f(9) = 2 ve f⁻¹(2) = 9')
DEN=B('Logaritmalı denklem','Önce tabanın ve logaritması alınan ifadelerin tanım koşulları yazılır; sonra logₐu = logₐv ise u = v ve logₐu = k ise u = aᵏ kullanılır; bulunan değerler tanım koşuluna sokularak denetlenir. Örnek: log₂(x − 1) = 3 ise x − 1 = 8 ve x = 9; x > 1 koşulunu sağlar')
ESI=B('Logaritmalı eşitsizlik','Tabanı a > 1 olan logaritma artan olduğundan eşitsizliğin yönü korunur; 0 < a < 1 ise yön değişir. Tanım koşulları ayrıca yazılıp çözüm kümesiyle kesiştirilir. Örnek: log₃x < 2 ise 0 < x < 9; log₁/₂x < 2 ise x > 1/4')
MOD=B('Üstel ve logaritmik modelleme','sabit sürede değeri k katına çıkan (ya da bölünen) bir niceliğin t süre sonraki değeri N = N₀·kᵗ/ᵖ biçimindedir (p: k katına çıkma süresi). Süreyi bulmak için N/N₀ oranı k’nın kuvveti olarak yazılır. Örnek: 5 saatte yarıya inen bir maddenin 15 saat sonra miktarı başlangıcın (1/2)³ = 1/8’i olur')
DEG=B('Kuvvet ve logaritma eşitliği','aᵘ = bᵛ = k biçiminde bir eşitlikte her bir üs, k’nın taban logaritması ile bulunur: u = logₐk ve v = log_b k. Örnek: 2ᵘ = 7 ise u = log₂7 ve 1/u = log₇2')

# ---------- kartlar (her tipId için bir kart) ----------
kartla('K-ALG-01','Üstel fonksiyonu kurma ve üstel denklem','Verilen iki değerden aᵘ·b biçimindeki fonksiyonun katsayıları bulunur; üstel denklemlerde ortak çarpan 2ˣ⁺ᵐ gibi tek kuvvete dönüştürülür.','b’yi f(0) sanmak; aˣ yerine a·x hesaplamak; ortak çarpanı yanlış paylaştırmak.','kolay','şekilli',3,'alg-ustel','Üstel fonksiyon ve üstel denklem')
kartla('K-ALG-02','Logaritma özellikleri ve hesap','Çarpım, bölüm ve kuvvet kuralları ile taban değiştirme birlikte kullanılır; ifade tek bir logaritmaya ya da sabit bir sayıya indirgenir.','Bölümü çıkarma gibi okumak; taban değiştirmeyi ters yazmak; logaritmaları toplamak yerine argümanları toplamak.','orta','düz',3,'alg-ozellik','Logaritma özellikleri')
kartla('K-ALG-03','Tablo ve ok değerleriyle fonksiyon','Tabloda verilen değerlerden fonksiyonun taban ve sabiti bulunur; ters ve bileşke işlemleri tablodaki eşleşmeler izlenerek yapılır.','Ters fonksiyonu 1/f(x) sanmak; sabiti atlamak; bileşkede sırayı ters çevirmek.','kolay','tablo',3,'alg-tablo','Tablodan logaritmik ve üstel fonksiyon')
kartla('K-ALG-04','Grafikten fonksiyon bilgisi','Grafikte işaretli noktalar fonksiyonun kuralına yerleştirilir; alan, uzunluk ve ifade doğruluğu grafikten okunan değerlerle hesaplanır.','Eğrilerin hangi fonksiyona ait olduğunu karıştırmak; tabanı 1’den küçük olanı artan sanmak; yamuk alanında bölme işlemini atlamak.','orta','grafik',4,'alg-grafik','Grafik okuma ve grafikten hesap')
kartla('K-ALG-05','Logaritmalı denklem ve tanım koşulu','Logaritmalar tek logaritmaya indirilir ya da yeni değişken kullanılır; bulunan her kök tanım koşuluna sokularak denetlenir.','Tanım kümesini denetlememek; toplamı çarpım sanmak; logaritmayı üs olarak açmayı unutmak.','orta','düz',4,'alg-denklem','Logaritmalı denklem')
kartla('K-ALG-06','Üstel ve logaritmik modelleme','Sabit oranlı büyüme ya da azalmada oran, verilen iki ölçümden bulunur; istenen değere ulaşma süresi oranın kuvveti olarak yazılır.','Yarılanma sayısını bir kaydırmak; oranı süre sanmak; ondalık ve desibel formüllerinde bölme ve çarpmayı karıştırmak.','orta','hikâyeli',4,'alg-model','Üstel ve logaritmik modelleme')
kartla('K-ALG-07','Logaritmalı eşitsizlik','Önce tanım koşulu, sonra tabana göre yönü bozan ya da koruyan eşitsizlik çözülür; çözüm kümeleri sayı doğrusunda kesiştirilir.','Taban 1’den küçükken yönü değiştirmemek; sıfırı ya da taban değerini çözüm kümesine katmak; tanım koşulunu atlamak.','orta','öncüllü',4,'alg-esitsizlik','Logaritmalı eşitsizlik ve çözüm kümesi')
kartla('K-ALG-08','Akış şemasında üstel ve logaritmik işlem','Her koşul kutusunun iki kolu ayrı çözülür; bulunan değerler koşuluna dönülerek denetlenir.','Sınır değerini yanlış kola koymak; Evet ve Hayır kollarını ters okumak; bir kolu atlamak.','zor','yeni nesil',5,'alg-akis','Akış şemasında üstel ve logaritmik işlem')
kartla('K-ALG-09','Sayı doğrusunda logaritma değerleri','Sayı doğrusundaki noktalar logaritma değerleri olarak okunur; eşit aralık, toplam ve fark logaritma özellikleriyle çözülür.','Eşit aralığı argümanlar için uygulamak; noktaları karıştırmak; toplamı çarpım olarak yazmayı unutmak.','orta','şekilli',4,'alg-dogru','Sayı doğrusunda logaritma ve karşılaştırma')

# ================= çizim yardımcıları =================
def eksen(x0,x1,y0,y1,sx,sy,xt,yt,xl='$x$',yl='$y$',izgara=True,fs='\\footnotesize'):
    o=[]
    if izgara:
        for v,*_ in xt: o.append(f'\\draw[gray!30,thin] ({v*sx:.3f},{y0*sy:.3f}) -- ({v*sx:.3f},{y1*sy:.3f});')
        for v,_ in yt: o.append(f'\\draw[gray!30,thin] ({x0*sx:.3f},{v*sy:.3f}) -- ({x1*sx:.3f},{v*sy:.3f});')
    o.append(f'\\draw[-{{Stealth}},thick] ({x0*sx:.3f},0) -- ({(x1+0.5)*sx:.3f},0) node[right] {{{xl}}};')
    o.append(f'\\draw[-{{Stealth}},thick] (0,{y0*sy:.3f}) -- (0,{(y1+0.5)*sy:.3f}) node[above] {{{yl}}};')
    for t in xt:
        v,l=t[0],t[1]; an=t[2] if len(t)>2 else 'below=2pt'
        if v!=0: o.append(f'\\node[{an},font={fs},fill=white,inner sep=0.6pt] at ({v*sx:.3f},0) {{{l}}};')
    for v,l in yt:
        if v!=0: o.append(f'\\node[left=2pt,font={fs},fill=white,inner sep=0.6pt] at (0,{v*sy:.3f}) {{{l}}};')
    return '\n'.join(o)
def egri(fn,xs,sx,sy,renk,w='1.8pt'):
    pts=' '.join(f'({x*sx:.3f},{fn(x)*sy:.3f})' for x in xs)
    return f'\\draw[line width={w},{renk}] plot[smooth] coordinates {{{pts}}};'
def aralik(a,b,n): return [a+(b-a)*i/n for i in range(n+1)]
def sayidog(x0,x1,sx,etik,y=0,fs='\\footnotesize'):
    o=[f'\\draw[-{{Stealth}},thick] ({(x0-0.5)*sx:.3f},{y}) -- ({(x1+0.5)*sx:.3f},{y});']
    for v in etik:
        o.append(f'\\draw[thick] ({v*sx:.3f},{y-0.09}) -- ({v*sx:.3f},{y+0.09}); \\node[below=3pt,font={fs}] at ({v*sx:.3f},{y}) {{${v}$}};'.replace('$-','$-'))
    return '\n'.join(o)
def sutun(vals,etik,ymax,adim,sy,genis=1.0,aralik_=1.7,yetik='',renk='mavi!55',birim='',fs='\\small',deger=True):
    o=[]; n=len(vals); W=(n-1)*aralik_+genis+0.6
    for j in range(0,ymax+1,adim): o.append(f'\\draw[gray!30,thin] (-0.2,{j*sy:.3f}) -- ({W:.2f},{j*sy:.3f}); \\node[left=2pt,font=\\footnotesize] at (-0.2,{j*sy:.3f}) {{{j}}};')
    o.append(f'\\draw[thick] (-0.2,0) -- ({W:.2f},0); \\draw[thick] (-0.2,0) -- (-0.2,{ymax*sy+0.2:.2f});')
    o.append(f'\\node[font=\\footnotesize,anchor=south] at (0.3,{ymax*sy+0.25:.2f}) {{{yetik}}};')
    for i,(v,e) in enumerate(zip(vals,etik)):
        x=0.3+i*aralik_
        o.append(f'\\fill[{renk},draw=black!55,thick] ({x-genis/2:.2f},0) rectangle ({x+genis/2:.2f},{v*sy:.3f});')
        if deger: o.append(f'\\node[above=1pt,font={fs}] at ({x:.2f},{v*sy:.3f}) {{{v}{birim}}};')
        o.append(f'\\node[below=2pt,font={fs}] at ({x:.2f},0) {{{e}}};')
    return '\n'.join(o)

# ================= soru tanım düzeni: havuz + harf dengesi =================
SP=[]
STD=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
def pe(v,cel,tur): return (Fr(v),fm(v),cel,tur)
def S(no,dogru,pool,ad,**kw):
    """dogru: değer (Fraction/int) ya da (anahtar,metin); pool: (anahtar,metin,cel,tur) listesi."""
    SP.append(dict(no=no,dogru=dogru,pool=pool,ad=ad,kw=kw))
def onc(dogruset,tf,yanl_dogru,yanl_yanlis,ad,**kw):
    """öncüllü soru: tf = {1:bool,...}. yanl_dogru[i]: i. önerme yanlışken doğru sanılırsa; yanl_yanlis[i]: doğruyken yanlış sanılırsa (öğrenci hatası)."""
    T=''.join(r for r,i in (('I',1),('II',2),('III',3)) if tf[i])
    def ad_(s): return s
    def ifade(ks):
        L=[{1:'I',2:'II',3:'III'}[i] for i in sorted(ks)]
        return ('Yalnız '+L[0]) if len(L)==1 else (' ve '.join(L) if len(L)==2 else 'I, II ve III')
    dset=frozenset(i for i in (1,2,3) if tf[i]); dg=ifade(dset); assert dg==dogruset,(dg,dogruset)
    pool=[]
    for k in range(1,8):
        ks=frozenset(i for i in (1,2,3) if (k>>(i-1))&1)
        if ks==dset: continue
        t=ifade(ks); cel=[]
        for i in (1,2,3):
            if i in ks and not tf[i]: cel.append(yanl_dogru[i])
            if i not in ks and tf[i]: cel.append(yanl_yanlis[i])
        pool.append((STD.index(t),t,' '.join(cel),'bilgi'))
    return dict(dogru=(STD.index(dg),dg),pool=pool,ad=ad,**kw)

# ================= 01 kolay · işlem makinesi, üstel fonksiyon =================
a1,b1=3,-1
f1=lambda x:a1*2**x+b1
assert (f1(0),f1(1),f1(4))==(2,5,47)
assert sorted([f1(0)-0])==[2]
# a+b=2, 2a+b=5
assert (5-2,2-(5-2))==(a1,b1)
e26=Fr(3,2)*16+2; e32=2*16; e48=3*16; e23=3*(2*4)-1; e50=3*16+2; e45=3*(16-1)
assert (e26,e32,e48,e23,e50,e45)==(26,32,48,23,50,45)
o=['\\node[draw,thick,minimum width=1.7cm,minimum height=2.6cm,fill=mavi!12] (F) at (0,0) {\\large $f$};',
 '\\node[font=\\small\\bfseries] at (-3.2,1.75) {$x$}; \\node[font=\\small\\bfseries] at (3.2,1.75) {$f(x)$};']
for yy,i,k in ((0.85,0,2),(-0.85,1,5)):
    o.append(f'\\node[draw,rounded corners=3pt,minimum width=1.2cm,minimum height=0.7cm] (i{i}) at (-3.2,{yy}) {{${i}$}};')
    o.append(f'\\node[draw,rounded corners=3pt,minimum width=1.2cm,minimum height=0.7cm] (o{i}) at (3.2,{yy}) {{${k}$}};')
    o.append(f'\\draw[-{{Stealth}},thick] (i{i}.east) -- (-0.85,{yy}); \\draw[-{{Stealth}},thick] (0.85,{yy}) -- (o{i}.west);')
SK=fig('\n'.join(o))
S('0001',47,[pe(e26,'f(0) = 2 olduğundan b = 2 almış; f(1) = 2a + 2 = 5 denkleminden a = 3/2 bulup f(4) = 3/2 × 16 + 2 hesaplamış.','bilgi'),pe(e32,'f(0) = a + b = 2 iken b’yi yok sayıp a = 2 almış: f(4) = 2 × 2⁴.','bilgi'),pe(e48,'a = 3 ve b = −1 bulmuş ama f(4) hesabında b’yi eklemeyi unutmuş: 3 × 2⁴.','dikkat'),pe(e23,'2ˣ ifadesini 2 × x gibi hesaplamış: 3 × (2 × 4) − 1.','islem'),pe(e50,'a = f(1) − f(0) = 3 bulmuş ama b = f(0) = 2 yazmış: 3 × 2⁴ + 2.','bilgi'),pe(e45,'Sabit terimi üsle birlikte parantez içine almış: 3 × (2⁴ − 1).','islem')],
 [A('Denklemleri yaz','Makineye girenlerle çıkanlar f(x) = a·2ˣ + b kuralına yerleştirilir.','x = 0: a + b = 2 · x = 1: 2a + b = 5'),A('a ve b’yi bul','İki denklem taraf tarafa çıkarılır.','a = 3 · b = −1'),A('f(4)’ü hesapla','x = 4 yazılır.','3 × 2⁴ − 1 = 47')],
 tipId='alg-ustel',tip='Üstel fonksiyon ve üstel denklem',z='kolay',alt='Üstel Fonksiyon',kaz='Üstel fonksiyonun katsayılarını verilen iki değerden bulup istenen değeri hesaplar.',kalip='şekilli',
 kart='K-ALG-01 (işlem makinesi) · f(x) = a·2ˣ + b; f(0) = 2, f(1) = 5',
 metin='a ve b birer gerçel sayı olmak üzere f(x) = a·2ˣ + b kuralıyla verilen f fonksiyonu, bir işlem makinesi olarak şekilde gösterilmiştir. Makineye bazı x değerleri girildiğinde çıkan f(x) değerleri şekilde verilmiştir.\nBuna göre f(4) kaçtır?',
 istenen='f(4) değeri.',ip=['Makineye giren değerlerin her birini f(x) = a·2ˣ + b kuralında yerine yaz.'],bilgi=[UST],sekil=SK,
 puf='Verilen her giriş–çıkış çifti kuralda bir denklem verir; iki bilinmeyen için iki çift yeter.')

# ================= 02 orta · logaritma özellikleri, hesap =================
v2=lg(8,4)+lg(125,25)+lg(12,2)-lg(3,2); assert abs(v2-5)<1e-12
S('0002',5,[pe(7,'log₂12 − log₂3 farkını 12 ÷ 3 = 4 olarak yazmış: 3/2 + 3/2 + 4.','bilgi'),pe(12,'log₂12 − log₂3 farkını 12 − 3 = 9 olarak yazmış: 3/2 + 3/2 + 9.','bilgi'),pe(9,'log₄8 = 8 ÷ 4 = 2 ve log₂₅125 = 125 ÷ 25 = 5 yazmış, son iki terimden 2 bulmuş: 2 + 5 + 2.','bilgi'),pe(Fr(11,2),'log₄8 değerini 8 ÷ 4 = 2 bulmuş; diğer terimleri doğru hesaplamış: 2 + 3/2 + 2.','islem'),pe(Fr(17,2),'log₂₅125 değerini 125 ÷ 25 = 5 bulmuş: 3/2 + 5 + 2.','islem'),pe(3,'Yalnız ilk iki logaritmayı toplamış: 3/2 + 3/2.','dikkat')],
 [A('Taban değiştir','4 ve 8 aynı tabanın kuvvetidir; 25 ve 125 de öyle.','log₄8 = 3/2 · log₂₅125 = 3/2'),A('Farkı birleştir','Aynı tabanda fark, bölümün logaritmasıdır.','log₂12 − log₂3 = log₂4 = 2'),A('Topla','Üç değer toplanır.','3/2 + 3/2 + 2 = 5')],
 tipId='alg-ozellik',tip='Logaritma özellikleri',z='kolay',alt='Logaritma Özellikleri',kaz='Taban değiştirme ve bölüm kuralını birlikte kullanarak logaritmik ifadenin değerini hesaplar.',kalip='düz',
 kart='K-ALG-02 (logaritma özellikleri) · log₄8 + log₂₅125 + log₂12 − log₂3',
 metin='log₄8 + log₂₅125 + log₂12 − log₂3\nişleminin sonucu kaçtır?',
 istenen='İfadenin değeri.',ip=['Tabanları ve argümanları aynı sayının kuvveti olarak yazmayı dene.'],bilgi=[OZL],
 puf='Önce farklı tabanları ortak tabana indir, sonra toplam ve farkları tek logaritmada birleştir.')

# ================= 03 kolay · tablo, logaritma fonksiyonu =================
a3,b3=3,2
f3=lambda x:lg(x,a3)+b3
assert abs(f3(1)-2)<1e-12 and abs(f3(3)-3)<1e-12 and abs(f3(81)-6)<1e-12
SK=tablo_svg(['x','1','3'],[['f(x)','2','3']])
S('0003',6,[pe(4,'b sabitini sonuca eklemeyi unutmuş: log₃81 = 4.','dikkat'),pe(2,'b sabitini çıkarmış: log₃81 − 2 = 2.','islem'),pe(12,'f(3) = log_a3 = 3 diyerek a = ∛3 bulmuş, sabiti eklememiş: log_a81 = 12.','bilgi'),pe(14,'f(3) = log_a3 = 3 diyerek a = ∛3 bulmuş, f(1) = 2 sabitini eklemiş: 12 + 2.','bilgi'),pe(8,'Sabiti çarpan sanmış: log₃81 × 2.','islem'),pe(5,'x = 81 yerine x = 27 almış: log₃27 + 2.','dikkat')],
 [A('b’yi bul','x = 1 için logaritma 0 olduğundan f(1) = b.','b = 2'),A('Tabanı bul','f(3) = logₐ3 + 2 = 3 eşitliği taban için çözülür.','logₐ3 = 1 → a = 3'),A('f(81)’i hesapla','81 = 3⁴ olduğundan logaritma 4’tür.','f(81) = 4 + 2 = 6')],
 tipId='alg-tablo',tip='Tablodan logaritmik ve üstel fonksiyon',z='kolay',alt='Tablodan Logaritma Fonksiyonu',kaz='Tabloda verilen değerlerden logaritma fonksiyonunun tabanını ve sabitini bulup istenen değeri hesaplar.',kalip='tablo',
 kart='K-ALG-03 (tablo) · f(x) = logₐx + b; f(1) = 2, f(3) = 3',
 metin='a > 1 ve b birer gerçel sayı olmak üzere f(x) = logₐx + b fonksiyonunun bazı değerleri aşağıdaki tabloda verilmiştir.\nBuna göre f(81) kaçtır?',
 istenen='f(81) değeri.',ip=['Tabloda hangi x değerinde logaritma kısmı kolayca bulunur?'],bilgi=[TAN],sekil=SK,
 puf='Tablodaki her sütun kurala yerleştirilince bir denklem verir.')

# ================= 04 kolay · üstel denklem =================
assert 2**(4+1)+2**(4-1)==40
S('0004',4,[pe(3,'2ˣ⁻¹ = 8 bulup x − 1 = 3 eşitliğindeki 1’i eklemeyi unutmuş.','dikkat'),pe(2,'2ˣ⁻¹ = 8 = 2³ den x − 1 = 3 bulmuş ama x = 3 − 1 = 2 yazmış.','islem'),pe(8,'2ˣ⁻¹ = 8 bulup üssü değil sonucu x yerine yazmış.','bilgi'),pe(16,'2ˣ⁻¹ = 8 den 2ˣ = 16 bulup x = 16 yazmış.','bilgi')],
 [A('Ortak çarpan seç','Üsler 2ˣ⁻¹ cinsinden yazılır.','2ˣ⁺¹ = 2² × 2ˣ⁻¹ → 2ˣ⁻¹ × (4 + 1) = 40'),A('2ˣ⁻¹’i bul','40 beşe bölünür.','2ˣ⁻¹ = 8 = 2³'),A('x’i bul','Üsler eşitlenir.','x − 1 = 3 → x = 4')],
 tipId='alg-ustel',tip='Üstel fonksiyon ve üstel denklem',z='kolay',alt='Üstel Denklem',kaz='Üsleri farklı iki terimli üstel denklemi ortak çarpanla tek kuvvete dönüştürüp çözer.',kalip='düz',
 kart='K-ALG-01 (üstel denklem) · 2ˣ⁺¹ + 2ˣ⁻¹ = 40',
 metin='x bir gerçel sayı olmak üzere\n2ˣ⁺¹ + 2ˣ⁻¹ = 40\neşitliği sağlanıyor.\nBuna göre x kaçtır?',
 istenen='x değeri.',ip=['Her iki terimi aynı üstel ifadenin katı olarak yazmayı dene.'],bilgi=[UST],
 puf='Üsleri farklı terimleri en küçük üssün katı olarak yazıp ortak çarpana al.')

# ================= 05 orta · iki logaritma grafiği, yamuk alanı =================
fA=lambda x:lg(x,3); gA=lambda x:-lg(x,3)
A5,B5,C5,D5=(9,fA(9)),(9,gA(9)),(3,gA(3)),(3,fA(3))
assert (round(A5[1]),round(B5[1]),round(C5[1]),round(D5[1]))==(2,-2,-1,1)
def shoe(p): return abs(sum(p[i][0]*p[(i+1)%len(p)][1]-p[(i+1)%len(p)][0]*p[i][1] for i in range(len(p))))/2
alan5=shoe([(9,2),(9,-2),(3,-1),(3,1)]); assert alan5==18
sx5,sy5=0.72,0.78
xs=aralik(0.14,10,90)
body=[eksen(0,10,-3,3,sx5,sy5,[(1,'1'),(3,'3','below left=1pt'),(9,'9','below right=1pt')],[],izgara=False),
 f'\\fill[yesil!18] ({9*sx5:.2f},{2*sy5:.2f}) -- ({9*sx5:.2f},{-2*sy5:.2f}) -- ({3*sx5:.2f},{-1*sy5:.2f}) -- ({3*sx5:.2f},{1*sy5:.2f}) -- cycle;',
 egri(fA,xs,sx5,sy5,'mavi'),egri(gA,xs,sx5,sy5,'turu'),
 f'\\draw[dashed,gray] ({3*sx5:.2f},{-1*sy5:.2f}) -- ({3*sx5:.2f},{1*sy5:.2f}); \\draw[dashed,gray] ({9*sx5:.2f},{-2*sy5:.2f}) -- ({9*sx5:.2f},{2*sy5:.2f});',
 f'\\draw[thick] ({9*sx5:.2f},{2*sy5:.2f}) -- ({9*sx5:.2f},{-2*sy5:.2f}) -- ({3*sx5:.2f},{-1*sy5:.2f}) -- ({3*sx5:.2f},{1*sy5:.2f}) -- cycle;']
for (x,y),nm,pos in ((A5,'A','above right'),(B5,'B','below right'),(C5,'C','below left'),(D5,'D','above left')):
    body.append(f'\\fill ({x*sx5:.2f},{y*sy5:.2f}) circle (0.07); \\node[{pos},font=\\small\\bfseries] at ({x*sx5:.2f},{y*sy5:.2f}) {{{nm}}};')
body.append(f'\\node[mavi,font=\\small\\bfseries,right] at ({10*sx5:.2f},{fA(10)*sy5+0.05:.2f}) {{$y=f(x)$}}; \\node[turu,font=\\small\\bfseries,right] at ({10*sx5:.2f},{gA(10)*sy5-0.05:.2f}) {{$y=g(x)$}};')
SK=fig('\n'.join(body))
S('0005',18,[pe(6,'Yamuk alanında paralel kenarların toplamı yerine farkını almış: (4 − 2)/2 × 6.','islem'),pe(12,'Şekli üçgen sanmış: 4 × 6 ÷ 2.','bilgi'),pe(15,'|CD| için yalnız C’nin ordinatı olan 1’i kullanmış: (4 + 1)/2 × 6.','dikkat'),pe(27,'Yükseklik olarak 6 yerine 9 almış: (4 + 2)/2 × 9.','dikkat'),pe(36,'Yamuk alanında 2’ye bölmeyi unutmuş: (4 + 2) × 6.','islem')],
 [A('Ordinatları bul','A ve D f’nin, B ve C g’nin grafiği üzerindedir; x değerleri şekilden okunur.','A(9, 2) · B(9, −2) · C(3, −1) · D(3, 1)'),A('Paralel kenarlar','[AB] ve [CD] y-eksenine paraleldir; uzunlukları ordinat farklarıdır.','|AB| = 4 · |CD| = 2'),A('Yüksekliği bul','Paralel kenarlar arasındaki uzaklık apsis farkıdır.','9 − 3 = 6'),A('Alanı hesapla','Yamuk alan formülü uygulanır.','(4 + 2)/2 × 6 = 18')],
 tipId='alg-grafik',tip='Grafik okuma ve grafikten hesap',z='orta',alt='Grafikten Alan',kaz='Birbirinin simetriği olan iki logaritma grafiği üzerindeki noktalarla oluşan yamuğun alanını hesaplar.',kalip='grafik',
 kart='K-ALG-04 (iki logaritma grafiği) · f(x) = log₃x ve g(x) = −log₃x; ABCD yamuğu',
 metin='Dik koordinat düzleminde f(x) = log₃x ve g(x) = −log₃x fonksiyonlarının grafikleri çizilmiştir. A ve D noktaları f fonksiyonunun, B ve C noktaları g fonksiyonunun grafiği üzerindedir; [AB] ve [CD] doğru parçaları y-eksenine paraleldir.\nBuna göre ABCD dörtgeninin alanı kaç birimkaredir?',
 istenen='ABCD dörtgeninin alanı (birimkare).',ip=['Noktaların apsislerini şekilden oku, ordinatlarını fonksiyon kurallarından hesapla.'],bilgi=[LOF],sekil=SK,
 puf='Grafikteki noktaların yalnız bir koordinatı verilmişse diğerini fonksiyon kuralından hesapla.')

# ================= 06 orta · öncüllü, üç üstel eğri =================
aa,bb,cc=Fr(1,2),2,4
sx6,sy6=1.55,0.62
Y=lambda t:min(t,5.2)
def cut(base,x0,x1):
    xs=[x0+(x1-x0)*i/80 for i in range(81)]
    xs=[x for x in xs if float(base)**x<=5.0]
    return xs
body=[eksen(-2.3,2.4,0,5.6,sx6,sy6,[(-2,'$-2$'),(-1,'$-1$'),(1,'1'),(2,'2')],[(Fr(1,2),'1/2'),(2,'2'),(4,'4')],izgara=False)]
body.append(egri(lambda x:0.5**x,cut(0.5,-2.3,2.3),sx6,sy6,'turu')); body.append(egri(lambda x:2**x,cut(2,-2.3,2.3),sx6,sy6,'mavi')); body.append(egri(lambda x:4**x,cut(4,-2.3,2.3),sx6,sy6,'mor'))
body.append(f'\\draw[dashed,gray] ({1*sx6:.2f},0) -- ({1*sx6:.2f},{4*sy6:.2f});')
for v,c in ((0.5,'turu'),(2,'mavi'),(4,'mor')):
    body.append(f'\\draw[dashed,gray] (0,{v*sy6:.3f}) -- ({1*sx6:.2f},{v*sy6:.3f}); \\fill[{c}] ({1*sx6:.2f},{v*sy6:.3f}) circle (0.07);')
body.append(f'\\node[turu,font=\\small\\bfseries,anchor=south west] at ({-2.3*sx6:.2f},{5.0*sy6:.2f}) {{$y=a^x$}}; \\node[mor,font=\\small\\bfseries,anchor=south] at ({1.16*sx6:.2f},{5.05*sy6:.2f}) {{$y=c^x$}}; \\node[mavi,font=\\small\\bfseries,anchor=north west] at ({1.95*sx6:.2f},{3.6*sy6:.2f}) {{$y=b^x$}};')
SK=fig('\n'.join(body))
tf6={1:abs(lg(aa,2)+lg(cc,2)-1)<1e-12,2:bb**cc==cc**bb,3:float(aa)**cc>float(aa)**bb}
assert tf6=={1:True,2:True,3:False},tf6
sp=onc('I ve II',tf6,{3:'a < 1 olduğundan üssün büyüdükçe aᵘ’nun da büyüdüğünü sanmış; (1/2)⁴ = 1/16 ile (1/2)² = 1/4’ü karşılaştırmamış.'},{1:'log₂a’nın negatif olduğunu görüp toplamın da negatif olacağını sanmış; log₂(1/2) + log₂4 = −1 + 2 = 1’i hesaplamamış.',2:'b ve c tabanlarının farklı olması nedeniyle bᶜ ile cᵇ’nin eşit olamayacağını sanmış; 2⁴ = 4² = 16’yı denememiş.'},[A('Değerleri oku','Eğrilerin x = 1’deki noktaları taban değerlerini verir.','a = 1/2 · b = 2 · c = 4'),A('I’i sına','Logaritmaların toplamı hesaplanır.','log₂(1/2) + log₂4 = −1 + 2 = 1 → doğru'),A('II’yi sına','İki kuvvet hesaplanır.','2⁴ = 16 · 4² = 16 → doğru'),A('III’ü sına','Tabanı 1’den küçük üstel fonksiyon azalandır.','(1/2)⁴ = 1/16 < (1/2)² = 1/4 → yanlış')],
 tipId='alg-grafik',tip='Grafik okuma ve grafikten hesap',z='orta',alt='Üstel Grafik Öncülleri',kaz='Grafikten okunan taban değerleriyle üstel ve logaritmik ifadelerin doğruluğunu karşılaştırır.',kalip='öncüllü',
 kart='K-ALG-04 (üç üstel eğri) · tabanlar 1/2, 2, 4; log₂a + log₂c = 1, bᶜ = cᵇ, aᶜ > aᵇ',
 metin='a, b ve c pozitif gerçel sayılar olmak üzere y = aˣ, y = bˣ ve y = cˣ fonksiyonlarının grafikleri aynı dik koordinat düzleminde çizilmiştir.\nI. log₂a + log₂c = 1\nII. bᶜ = cᵇ\nIII. aᶜ > aᵇ\nifadelerinden hangileri doğrudur?',
 istenen='Doğru olan önermeler.',ip=['Her eğrinin x = 1 noktasındaki değeri tabanın kendisidir; önce üç tabanı oku.'],bilgi=[UST,OZL],sekil=SK,
 puf='Önermeleri sınamadan önce grafikten tabanların sayısal değerini yazmak işi hesaba indirger.')
S('0006',sp['dogru'],sp['pool'],sp['ad'],**{k:v for k,v in sp.items() if k not in('dogru','pool','ad')})

# ================= 07 orta · pH tablosu, hikâyeli =================
l2=Fr(3,10); l5=1-l2; l4=2*l2
phX=5-l4; phY=3-l5; assert (phX,phY,phX-phY)==(Fr(44,10),Fr(23,10),Fr(21,10))
SK=tablo_svg(['Çözelti','[H⁺] (mol/L)'],[['X','4 × 10⁻⁵'],['Y','5 × 10⁻³']])
S('0007',Fr(21,10),[pe(Fr(19,10),'log5 değerini log10 ÷ 2 = 0,5 almış: pH(Y) = 3 − 0,5 = 2,5 ve fark 4,4 − 2,5.','bilgi'),pe(Fr(17,10),'log5 yerine log2 = 0,3 almış: pH(Y) = 2,7 ve fark 4,4 − 2,7.','dikkat'),pe(Fr(7,10),'Y için pH = −log(5 × 10⁻³) = 3 + 0,7 = 3,7 almış (işaret hatası); fark 4,4 − 3,7.','islem'),pe(Fr(1,10),'10’un kuvvetlerini hiç yazmamış: pH(X) = 0,6 ve pH(Y) = 0,7.','dikkat'),pe(Fr(12,5),'log4 değerini 0,3 almış: pH(X) = 4,7 ve fark 4,7 − 2,3.','bilgi'),pe(Fr(27,10),'log5 = 1 + 0,3 = 1,3 almış: pH(Y) = 1,7 ve fark 4,4 − 1,7.','bilgi'),pe(Fr(67,10),'İki pH değerini toplamış: 4,4 + 2,3.','dikkat')],
 [A('Logaritma değerleri','log2 = 0,3 ve 5 = 10 ÷ 2 olduğundan log5 hesaplanır.','log4 = 2 × 0,3 = 0,6 · log5 = 1 − 0,3 = 0,7'),A('pH(X)','Çarpımın logaritması toplamdır.','−log(4 × 10⁻⁵) = −(0,6 − 5) = 4,4'),A('pH(Y)','Aynı işlem Y için yapılır.','−log(5 × 10⁻³) = −(0,7 − 3) = 2,3'),A('Farkı bul','Büyük pH’tan küçük pH çıkarılır.','4,4 − 2,3 = 2,1')],
 tipId='alg-model',tip='Üstel ve logaritmik modelleme',z='orta',alt='pH Hesabı',kaz='Logaritmanın çarpım ve bölüm kurallarıyla verilen tablodaki derişimlerin pH değerlerini hesaplar.',kalip='hikâyeli',
 kart='K-ALG-06 (pH tablosu) · pH = −log[H⁺], log2 = 0,3 · X: 4 × 10⁻⁵, Y: 5 × 10⁻³',
 metin='Bir kimya laboratuvarında hazırlanan X ve Y çözeltilerinin hidrojen iyonu derişimleri aşağıdaki tabloda verilmiştir. Bir çözeltinin pH değeri, hidrojen iyonu derişimi [H⁺] mol/L olmak üzere pH = −log[H⁺] bağıntısıyla bulunur (burada log, 10 tabanındaki logaritmadır). Laboratuvar sorumlusu hesaplarında log2 = 0,3 değerini kullanmaktadır.\nBuna göre Y çözeltisinin pH değeri, X çözeltisinin pH değerinden kaç eksiktir?',
 istenen='pH(X) − pH(Y) farkı.',ip=['Derişimleri a × 10ⁿ biçiminde bırakıp logaritmasını çarpım kuralıyla ayır.'],bilgi=[OZL],sekil=SK,
 puf='Tek basamaklı bir sayının logaritmasını 2 ve 10 üzerinden yazmak, verilen log2 değeriyle yetinmeni sağlar.')

# ================= 08 orta · logaritmalı denklem =================
assert abs(lg(1,3)+lg(9,3)-2)<1e-12   # x=3: log3(1)+log3(9)=2
import sympy as sp_
xx=sp_.symbols('x'); kk=sp_.solve((xx-2)*(xx+6)-9,xx); assert sorted(kk)==[-7,3]
S('0008',3,[pe(-4,'Denklemi (x − 2)(x + 6) = 9 yapıp iki kökün toplamını (−7 + 3) yazmış; tanım koşulu x > 2’yi denetlememiş.','dikkat'),pe(-7,'Kökler arasından tanım koşulunu sağlamayan −7’yi seçmiş.','dikkat'),pe(1,'Logaritmaların toplamını 2 · 3 = 6 sanıp (x − 2) + (x + 6) = 6 yazmış.','bilgi'),pe(Fr(5,2),'Logaritmaların toplamını argümanların toplamıyla eşlemiş: (x − 2) + (x + 6) = 9.','bilgi'),pe(5,'Yalnız ilk logaritmayı kullanıp x − 2 = 3 yazmış.','dikkat'),pe(21,'x² + 4x − 21 = 0 denkleminden sabit terimi x değeri sanmış.','islem')],
 [A('Tanım koşulu','Logaritmanın argümanları pozitif olmalıdır.','x − 2 > 0 ve x + 6 > 0 → x > 2'),A('Logaritmaları birleştir','Toplam, çarpımın logaritmasıdır; sonra üs şekline çevrilir.','log₃[(x − 2)(x + 6)] = 2 → (x − 2)(x + 6) = 9'),A('Denklemi çöz','İkinci derece denklem çarpanlarına ayrılır.','x² + 4x − 21 = 0 → (x + 7)(x − 3) = 0 → x = −7 ya da x = 3'),A('Kökleri ele','Yalnız x > 2 koşulunu sağlayan kök alınır.','x = 3 → toplam 3')],
 tipId='alg-denklem',tip='Logaritmalı denklem',z='orta',alt='Logaritmalı Denklem',kaz='Logaritmaların toplamını tek logaritmaya indirgeyen denklemi çözüp tanım koşuluna uymayan kökü eler.',kalip='düz',
 kart='K-ALG-05 (logaritmalı denklem) · log₃(x − 2) + log₃(x + 6) = 2',
 metin='log₃(x − 2) + log₃(x + 6) = 2\neşitliğini sağlayan x gerçel sayısı kaçtır?',
 istenen='Denklemi sağlayan x değeri.',ip=['Çözüme başlamadan önce logaritmanın içindeki iki ifadenin pozitif olması koşulunu yaz.'],bilgi=[DEN,OZL],
 puf='Bulduğun her kökü, logaritmanın tanım koşuluna geri koyarak sına.')

# ================= 09 orta · yarı ömür sütun grafiği =================
M0,T=640,12
mass=lambda t:M0*Fr(1,2)**Fr(t,T)
assert (mass(0),mass(12),mass(24))==(640,320,160)
tsure=T*math.log2(M0/20); assert abs(tsure-60)<1e-9
SK=fig(sutun([640,320,160],['0. gün','12. gün','24. gün'],800,160,0.0040,yetik='Kalan kütle (mg)',birim=''))
S('0009',60,[pe(36,'Hedefi 80 mg sanıp 640 → 80 için 3 yarılanma saymış: 3 × 12.','dikkat'),pe(48,'640 → 20 için 4 kez yarıya indiğini sanmış: 4 × 12.','islem'),pe(72,'640 ÷ 20 = 32 = 2⁶ yazıp yarılanma sayısını 6 bulmuş: 6 × 12.','islem'),pe(120,'Yarı ömrü grafikteki 0. ve 24. gün ölçümleri arası (24 gün) sanmış: 5 × 24.','bilgi'),pe(384,'640 ÷ 20 = 32 oranını yarılanma sayısı sanmış: 32 × 12.','bilgi')],
 [A('Yarı ömrü bul','Grafikte her 12 günde kütle yarıya iniyor.','640 → 320 → 160 → yarı ömür 12 gün'),A('Yarılanma sayısı','Başlangıç kütlesinin istenen kütleye oranı 2’nin kuvveti olarak yazılır.','640 ÷ 20 = 32 = 2⁵ → 5 yarılanma'),A('Süreyi hesapla','Yarılanma sayısı yarı ömürle çarpılır.','5 × 12 = 60 gün')],
 tipId='alg-model',tip='Üstel ve logaritmik modelleme',z='orta',alt='Yarı Ömür',kaz='Sütun grafikten yarı ömrü bulup bir kütleye inme süresini üstel ilişki ile hesaplar.',kalip='hikâyeli',
 kart='K-ALG-06 (yarı ömür sütun grafiği) · 640, 320, 160 mg; hedef 20 mg',
 metin='Bir araştırma laboratuvarında kullanılan radyoaktif bir izotopun kütlesi her gün aynı oranda azalarak sabit sürelerde yarıya inmektedir. Aşağıdaki sütun grafikte izotopun başlangıçta ve sonraki iki ölçümde kalan kütleleri gösterilmiştir. Laboratuvar, kalan kütle 20 mg’a düştüğünde izotopu güvenli sayıp depodan çıkaracaktır.\nBuna göre izotop başlangıçtan kaç gün sonra depodan çıkarılır?',
 istenen='İzotopun depodan çıkarılacağı gün sayısı.',ip=['Grafikteki iki ardışık sütunun oranına bak ve kütlenin 20 mg’a inmesi için bu oranın kaç kez uygulanacağını düşün.'],bilgi=[MOD],sekil=SK,
 puf='Bir niceliğin başlangıcına oranını 2’nin kuvveti yaz; üs yarılanma sayısını verir.')

# ================= 10 orta · sayı doğrusu, eş aralıklı noktalar =================
ak=[lg(3,2)+i for i in range(5)]
assert abs(ak[4]-lg(48,2))<1e-12 and abs(2**(ak[1]+ak[3])-144)<1e-9
sx=1.6
o=[sayidog(0,4,sx,[])]
lab=[('A','$\\log_2 3$'),('B',''),('C',''),('D',''),('E','$\\log_2 48$')]
for i,(n,l) in enumerate(lab):
    o.append(f'\\fill[mavi] ({i*sx:.2f},0) circle (0.09); \\node[above=4pt,font=\\small\\bfseries] at ({i*sx:.2f},0) {{{n}}};')
    if l: o.append(f'\\node[below=5pt,font=\\small] at ({i*sx:.2f},0) {{{l}}};')
SK=fig('\n'.join(o))
S('0010',144,[pe(30,'B ve D’nin koordinatları yerine argümanlarını (6 ve 24) toplamış.','bilgi'),pe(51,'Eşit aralığı argümanlara uygulayıp A ile E’nin argümanlarını toplamış: 3 + 48.','bilgi'),pe(72,'D yerine C’yi alıp B ile C’nin argümanlarını çarpmış: 6 × 12.','dikkat'),pe(288,'D yerine E’yi alıp B ile E’nin argümanlarını çarpmış: 6 × 48.','dikkat'),pe(1152,'B yerine D, D yerine E’yi alıp argümanları çarpmış: 24 × 48.','dikkat')],
 [A('Aralığı bul','4 eşit aralığın toplamı iki uç noktanın farkıdır.','log₂48 − log₂3 = log₂16 = 4 → her aralık 1'),A('B ve D’yi yaz','B, A’dan bir; D, A’dan üç aralık sonradır.','B = log₂3 + 1 = log₂6 · D = log₂3 + 3 = log₂24'),A('x’i hesapla','Logaritmalar toplanır.','x = log₂6 + log₂24 = log₂144'),A('2ˣ’i bul','2 tabanında üs ve logaritma birbirini götürür.','2ˣ = 144')],
 tipId='alg-dogru',tip='Sayı doğrusunda logaritma ve karşılaştırma',z='orta',alt='Sayı Doğrusunda Logaritma',kaz='Sayı doğrusunda eşit aralıklı noktaların koordinatlarını logaritma özellikleriyle bulup üslü ifadeyi hesaplar.',kalip='şekilli',
 kart='K-ALG-09 (eş aralıklı noktalar) · A = log₂3, E = log₂48; B ve D’nin toplamı',
 metin='Şekildeki sayı doğrusunda A, B, C, D ve E noktaları, bu sırayla ve eşit aralıklarla yerleştirilmiştir. B ve D noktalarının koordinatları toplamı x gerçel sayısıdır.\nBuna göre 2ˣ kaçtır?',
 istenen='2ˣ değeri.',ip=['Eşit aralığın değerini iki uç noktanın koordinatları farkından bul.'],bilgi=[OZL],sekil=SK,
 puf='Sayı doğrusunda eşit aralık, logaritmanın içinde çarpmayla değil logaritma değerleri arasında toplamayla uygulanır.')

# ================= 11 orta · tablo, ters ve bileşke =================
fb=lambda x:2**x+1; fbi=lambda y:int(round(math.log2(y-1)))
gT={1:17,2:9,3:5,4:3}
assert all(fbi(fb(k))==k for k in range(1,6))
v11=gT[fbi(5)]+fbi(gT[1]); assert (gT[fbi(5)],fbi(gT[1]),v11)==(9,4,13)
SK=tablo_svg(['x','1','2','3','4'],[['g(x)','17','9','5','3']])
S('0011',13,[pe(6,'(g ∘ f⁻¹)(5) için yalnız f⁻¹(5) = 2 bulup g’yi uygulamamış: 2 + 4.','dikkat'),pe(7,'f⁻¹(5) için 2ˣ = 4 → x = 4 yazmış (üssü sonuç sanmış): g(4) = 3 ve f⁻¹(17) = 4.','islem'),pe(11,'f⁻¹(5) için aynı hatayla g(4) = 3 almış; f⁻¹(17) için 2ˣ = 16 → x = 8 yazmış (yarısını almış): 3 + 8.','islem'),pe(20,'Birinci terimde f⁻¹(5) = 4 almış (g(4) = 3), ikinci terimde yalnız g(1) = 17 yazmış: 3 + 17.','bilgi'),pe(25,'İkinci terimde 2ˣ = 16 → x = 16 yazmış (üssü sonuç sanmış): 9 + 16.','islem'),pe(26,'İkinci terimde f⁻¹’i uygulamayı unutup yalnız g(1) = 17 almış: 9 + 17.','dikkat')],
 [A('f⁻¹ kuralını yaz','2ˣ + 1 = y denkleminden x çekilir.','f⁻¹(y) = log₂(y − 1)'),A('İlk terim','f⁻¹(5) bulunur, sonra g’nin tablosundan değeri okunur.','f⁻¹(5) = log₂4 = 2 → g(2) = 9'),A('İkinci terim','Önce tablodan g(1) okunur, sonra f⁻¹ uygulanır.','g(1) = 17 → f⁻¹(17) = log₂16 = 4'),A('Topla','İki terim toplanır.','9 + 4 = 13')],
 tipId='alg-tablo',tip='Tablodan logaritmik ve üstel fonksiyon',z='orta',alt='Ters ve Bileşke',kaz='Üstel fonksiyonun tersini logaritma ile yazıp tablo ile verilen bir fonksiyonla bileşkesini hesaplar.',kalip='tablo',
 kart='K-ALG-03 (tablo, ters ve bileşke) · f(x) = 2ˣ + 1; (g ∘ f⁻¹)(5) + (f⁻¹ ∘ g)(1)',
 metin='f(x) = 2ˣ + 1 fonksiyonu ile g fonksiyonunun bazı değerleri aşağıdaki tabloda verilmiştir.\nBuna göre (g ∘ f⁻¹)(5) + (f⁻¹ ∘ g)(1) toplamı kaçtır?',
 istenen='(g ∘ f⁻¹)(5) + (f⁻¹ ∘ g)(1) değeri.',ip=['f⁻¹ için 2ˣ + 1 = y eşitliğinden x’i logaritma ile çek.'],bilgi=[LOF],sekil=SK,
 puf='Bileşkede içteki fonksiyonu önce uygula; ters üstel fonksiyon logaritma olduğundan değerler 2’nin kuvvetine dönüşür.')

# ================= 12 zor · dikdörtgen, ikinci derece dönüşümü =================
for t in (1,2): assert t*(3-t)==2
x12=[5**1,5**2]; assert x12[0]*x12[1]==125
for x_ in x12: assert abs(lg(x_,5)*lg(125/x_,5)-2)<1e-12
rx,ry=5.0,2.7
o=[f'\\fill[yesil!15] (0,0) rectangle ({rx},{ry}); \\draw[thick] (0,0) rectangle ({rx},{ry});',
 f'\\node[below left] at (0,0) {{$A$}}; \\node[below right] at ({rx},0) {{$B$}}; \\node[above right] at ({rx},{ry}) {{$C$}}; \\node[above left] at (0,{ry}) {{$D$}};',
 f'\\node[below=3pt] at ({rx/2},0) {{$\\log_5 x$}}; \\node[right=3pt] at ({rx},{ry/2}) {{$\\log_5\\dfrac{{125}}{{x}}$}};',
 f'\\node at ({rx/2},{ry/2}) {{Alan $=2$ birimkare}};']
SK=fig('\n'.join(o))
S('0012',125,[pe(2,'t = 1 ve t = 2 çözümlerini x değerleri sanıp çarpmış.','bilgi'),pe(10,'t = 1 için x = 5, t = 2 için x = 2 yazmış (üssü taban gibi okumuş): 5 × 2.','bilgi'),pe(30,'x değerlerini doğru bulmuş (5 ve 25) ama çarpım yerine toplamlarını yazmış.','dikkat'),pe(625,'t = 2’nin iki kez çözüm olduğunu sanıp 25 × 25 hesaplamış.','islem'),pe(3125,'Denklemi (t − 2)(t − 3) = 0 diye çarpanlarına ayırıp x = 25 ve x = 125 bulmuş.','islem')],
 [A('Uzunlukları yaz','Kenarlar için log₅x = t denir; ikinci kenar log₅125 − log₅x ile ifade edilir.','|AB| = t · |BC| = 3 − t'),A('Alan denklemini kur','Alan 2’dir.','t(3 − t) = 2 → t² − 3t + 2 = 0'),A('t’yi bul','Denklem çarpanlarına ayrılır.','(t − 1)(t − 2) = 0 → t = 1 ya da t = 2'),A('x’leri bul','Logaritmanın tanımı kullanılır.','x = 5¹ = 5 ya da x = 5² = 25'),A('Çarpımı yaz','Elde edilen iki değer çarpılır.','5 × 25 = 125')],
 tipId='alg-denklem',tip='Logaritmalı denklem',z='zor',alt='Logaritmalı Alan Denklemi',kaz='Kenar uzunlukları logaritmik olan dikdörtgenin alan koşulunu yeni değişkenle ikinci dereceden denkleme çevirip çözer.',kalip='şekilli',
 kart='K-ALG-05 (logaritmik dikdörtgen) · |AB| = log₅x, |BC| = log₅(125/x), alan 2',
 metin='x, 1’den büyük ve 125’ten küçük bir gerçel sayı olmak üzere şekildeki ABCD dikdörtgeninin kenar uzunlukları ve alanı verilmiştir.\nBuna göre x’in alabileceği değerlerin çarpımı kaçtır?',
 istenen='x’in alabileceği değerlerin çarpımı.',ip=['log₅x yerine t yazıp diğer kenarı t cinsinden ifade et.'],bilgi=[OZL,DEN],sekil=SK,
 puf='Soruda tekrar eden ortak bir logaritmik büyüklük var mı, ona bak.')

# ================= 13 orta · öncüllü, taban değiştirme =================
aL,bL=lg(3,2),lg(5,3)
tf13={1:abs(lg(5,2)-aL*bL)<1e-12,2:abs(lg(5,6)-bL/(aL+1))<1e-9,3:abs(lg(10,3)-(1+aL*bL)/aL)<1e-12}
assert tf13=={1:True,2:False,3:True},tf13
sp=onc('I ve III',tf13,{2:'log₆5’i log₂6 = a + 1 ile ayrı ayrı bölmeyi unutup b/(a + 1) yazmış; log₂5 = ab olduğundan pay ab olmalıdır.'},{1:'Taban değiştirirken zincir kuralını (log₂3 · log₃5 = log₂5) bilmediğinden eşitliği yanlış sanmış.',3:'log₃10’u log₃2 + log₃5 olarak yazıp log₃2 = 1/a olduğunu görememiş; bu yüzden (1 + ab)/a’yı yanlış sanmış.'},[A('log₂5’i yaz','Taban değiştirme zinciri kullanılır.','log₂5 = log₂3 · log₃5 = ab'),A('I’i sına','Bulunan değer önermeyle karşılaştırılır.','log₂5 = ab → doğru'),A('II’yi sına','log₆5 = log₂5 ÷ log₂6 ve log₂6 = 1 + a.','log₆5 = ab/(a + 1) ≠ b/(a + 1) → yanlış'),A('III’ü sına','log₃10 = log₃2 + log₃5 ve log₃2 = 1/a.','log₃10 = 1/a + b = (1 + ab)/a → doğru')],
 tipId='alg-ozellik',tip='Logaritma özellikleri',z='orta',alt='Taban Değiştirme Öncülleri',kaz='Taban değiştirme ve toplam kuralıyla logaritmaların iki değişken cinsinden ifadesini karşılaştırır.',kalip='öncüllü',
 kart='K-ALG-02 (öncüllü taban değiştirme) · a = log₂3, b = log₃5; log₂5 = ab, log₆5, log₃10',
 metin='a = log₂3 ve b = log₃5 olmak üzere\nI. log₂5 = a·b\nII. log₆5 = b/(a + 1)\nIII. log₃10 = (1 + a·b)/a\nifadelerinden hangileri doğrudur?',
 istenen='Doğru olan eşitlikler.',ip=['Önce log₂5 ve log₃2’yi a ve b cinsinden yaz.'],bilgi=[OZL],
 puf='Bilinmeyen logaritmayı ortak bir tabanda (burada 2) yazıp iki değişkene dönüştür.')
S('0013',sp['dogru'],sp['pool'],sp['ad'],**{k:v for k,v in sp.items() if k not in('dogru','pool','ad')})

# ================= 14 zor · log grafiği, tam sayı koşulu =================
a14,b14,c14=2,2,1
f14=lambda x:math.log2(x-2)+1
assert abs(f14(3)-1)<1e-12 and abs(f14(6)-3)<1e-12
cz=[x for x in range(3,200) if abs(f14(x)-round(f14(x)))<1e-9 and f14(x)<5-1e-9]; assert cz==[3,4,6,10] and sum(cz)==23
e41=sum(x for x in range(3,200) if abs(f14(x)-round(f14(x)))<1e-9 and f14(x)<=5+1e-9); e75=sum(x for x in range(3,200) if abs(f14(x)-round(f14(x)))<1e-9 and f14(x)<=6+1e-9); e20=sum(cz)-3; e13=sum(x for x in range(3,200) if abs(f14(x)-round(f14(x)))<1e-9 and f14(x)<4-1e-9); e10=sum(round(f14(x)) for x in cz)
assert (e41,e75,e20,e13,e10)==(41,75,20,13,10)
sx,sy=0.62,0.58
body=[eksen(0,11,-3,5,sx,sy,[(2,'2','below left=1pt'),(3,'3','below right=1pt'),(6,'6')],[(1,'1'),(3,'3')],izgara=False),
 f'\\draw[dashed,thick,gray] ({2*sx},{-3*sy}) -- ({2*sx},{5.4*sy}); ',
 egri(f14,aralik(2.065,10.9,90),sx,sy,'mavi')]
for x,y in ((3,1),(6,3)):
    body.append(f'\\draw[dashed,gray] ({x*sx},0) -- ({x*sx},{y*sy:.2f}) -- (0,{y*sy:.2f}); \\fill[mavi] ({x*sx},{y*sy:.2f}) circle (0.08);')
body.append(f'\\node[mavi,font=\\small\\bfseries,right] at ({10.9*sx:.2f},{f14(10.9)*sy:.2f}) {{$y=f(x)$}};')
SK=fig('\n'.join(body))
S('0014',23,[pe(41,'Sabit terimi (+1) ihmal edip log₂(x − 2) < 5 çözmüş: 3 + 4 + 6 + 10 + 18.','dikkat'),pe(75,'Sabit terimi ihmal edip x − 2 ≤ 32 almış: 3 + 4 + 6 + 10 + 18 + 34.','dikkat'),pe(20,'x = 3 için log₂1 tanımsız sanıp x = 3’ü dışarıda bırakmış: 4 + 6 + 10.','bilgi'),pe(13,'f(x) < 4 almış: 3 + 4 + 6.','dikkat'),pe(10,'x değerleri yerine f(x) değerlerini toplamış: 1 + 2 + 3 + 4.','dikkat')],
 [A('Fonksiyonu bul','Dikey asimptot x = 2 olduğundan x − 2 görünür; (3, 1) c = 1, (6, 3) a = 2 verir.','f(x) = log₂(x − 2) + 1'),A('Tam sayı koşulu','x tam sayı ve f(x) tam sayı ise x − 2 = 2ᵏ olmalıdır (k ≥ 0 tam sayı).','x = 2ᵏ + 2 → f(x) = k + 1'),A('Eşitsizliği çöz','f(x) < 5 olması için k + 1 < 5, yani k ≤ 3.','k = 0, 1, 2, 3'),A('x’leri yaz','Her k için x hesaplanır.','x = 3, 4, 6, 10'),A('Topla','Dört değer toplanır.','3 + 4 + 6 + 10 = 23')],
 tipId='alg-grafik',tip='Grafik okuma ve grafikten hesap',z='zor',alt='Grafikten Tam Sayı Koşulu',kaz='Grafikten logaritma fonksiyonunun kuralını bulup tam sayı koşuluyla eşitsizliği birlikte değerlendirir.',kalip='grafik',
 kart='K-ALG-04 (kaydırılmış logaritma grafiği) · f(x) = log₂(x − 2) + 1; x ve f(x) tam sayı, f(x) < 5',
 metin='a > 1, b ve c birer gerçel sayı olmak üzere f(x) = logₐ(x − b) + c fonksiyonunun grafiği ve grafiğin dikey asimptotu şekilde gösterilmiştir; işaretli noktalar kılavuz çizgilerinin kesişimindedir.\nBuna göre hem x hem f(x) birer tam sayı olmak üzere f(x) < 5 koşulunu sağlayan x değerlerinin toplamı kaçtır?',
 istenen='Koşulu sağlayan x tam sayılarının toplamı.',ip=['Dikey asimptot logaritmanın içindeki ifadenin sıfır olduğu yerdir; önce b’yi oradan oku.'],bilgi=[LOF,ESI],sekil=SK,
 puf='Logaritma içindeki ifade ile logaritmanın değeri aynı anda tam sayıysa içeriği tabanın tam sayı kuvvetine eşitle.')

# ================= 15 zor · akış şeması =================
t1,t2=4,3
def zf(x):
    y=math.log2(x) if x>=t1 else 2**x
    return 2*y-1 if y>=t2 else 3*y-1
kok=[8,4,math.log2(3),1]
for x in kok: assert abs(zf(x)-5)<1e-9,x
# tarama: z=5 veren başka x yok
for i in range(1,4000):
    x=i/100
    if abs(zf(x)-5)<1e-9: assert any(abs(x-k)<1e-9 for k in kok),x
tamsay=[x for x in kok if abs(x-round(x))<1e-9]; assert sum(tamsay)==13
assert (8+1, 8+4, 8, 4+1, 8+4+1+2)==(9,12,8,5,15)
o=['\\tikzset{kt/.style={draw,thick,rounded corners=2pt,minimum width=2.4cm,minimum height=0.7cm,align=center},kr/.style={draw,thick,diamond,aspect=2.3,inner sep=1pt,align=center},ok/.style={-{Stealth},thick}}',
 '\\node[kt,rounded corners=8pt] (s) at (0,0) {Giriş: $x>0$};',
 f'\\node[kr] (d1) at (0,-1.7) {{$x\\geq {t1}$ mü?}};',
 '\\node[kt] (a) at (-2.8,-3.4) {$y=2^{x}$}; \\node[kt] (b) at (2.8,-3.4) {$y=\\log_2 x$};',
 f'\\node[kr] (d2) at (0,-5.1) {{$y\\geq {t2}$ mü?}};',
 '\\node[kt] (c) at (-2.8,-6.8) {$z=3y-1$}; \\node[kt] (dd) at (2.8,-6.8) {$z=2y-1$};',
 '\\node[kt,rounded corners=8pt] (e) at (0,-8.3) {Çıkış: $z$};',
 '\\draw[ok] (s) -- (d1);',
 '\\draw[ok] (d1.west) -| node[pos=0.25,above,font=\\footnotesize] {Hayır} (a.north);',
 '\\draw[ok] (d1.east) -| node[pos=0.25,above,font=\\footnotesize] {Evet} (b.north);',
 '\\draw[thick] (a.south) |- (0,-4.2); \\draw[thick] (b.south) |- (0,-4.2); \\draw[ok] (0,-4.2) -- (d2.north);',
 '\\draw[ok] (d2.west) -| node[pos=0.25,above,font=\\footnotesize] {Hayır} (c.north);',
 '\\draw[ok] (d2.east) -| node[pos=0.25,above,font=\\footnotesize] {Evet} (dd.north);',
 '\\draw[ok] (c.south) |- (e.west); \\draw[ok] (dd.south) |- (e.east);']
SK=fig('\n'.join(o))
S('0015',13,[pe(9,'x ≥ 4 koşulunda eşitlik durumunu dışarıda bırakıp x = 4’ü almamış: 8 + 1.','dikkat'),pe(12,'“Hayır” kolunda 2ˣ = 3 ve 2ˣ = 2 denklemlerini yok sayıp yalnız 8 ve 4’ü toplamış.','dikkat'),pe(8,'Yalnız “Evet–Evet” yolunu çözüp ilk değerde bırakmış.','dikkat'),pe(5,'y = 2 değerinden gelen x = 4 ve x = 1’i toplayıp y = 3’ü hiç denememiş.','dikkat'),pe(15,'log₂3 ≈ 1,58 değerini 2’ye yuvarlayıp tam sayı çözüm saymış: 8 + 4 + 1 + 2.','islem')],
 [A('İkinci kutuyu çöz','z = 5 için iki kolu ayrı çöz; sonra y’nin koşulunu denetle.','2y − 1 = 5 → y = 3 (y ≥ 3 sağlanır) · 3y − 1 = 5 → y = 2 (y < 3 sağlanır)'),A('y = 3 için x','İlk kutunun iki kolu denenir.','log₂x = 3 → x = 8 (x ≥ 4 sağlanır) · 2ˣ = 3 → x = log₂3 ≈ 1,58 (x < 4 sağlanır)'),A('y = 2 için x','İlk kutunun iki kolu yine denenir.','log₂x = 2 → x = 4 (x ≥ 4 sağlanır) · 2ˣ = 2 → x = 1 (x < 4 sağlanır)'),A('Tam sayıları seç','Dört çözümden yalnız üçü tam sayıdır.','x ∈ {8, 4, 1} · log₂3 tam sayı değil'),A('Topla','Tam sayı çözümler toplanır.','8 + 4 + 1 = 13')],
 tipId='alg-akis',tip='Akış şemasında üstel ve logaritmik işlem',z='zor',alt='Akış Şeması',kaz='Koşul kutulu akış şemasında üstel ve logaritmik işlemleri geriye doğru çözüp koşullara uyan tam sayı değerleri bulur.',kalip='yeni nesil',
 kart='K-ALG-08 (akış şeması) · iki koşul kutusu, 2ˣ ve log₂x kolları; z = 5',
 metin='Şekildeki akış şemasına bir x pozitif gerçel sayısı girilmekte ve işlemler şemanın gösterdiği yolla yapılarak çıkış değeri bulunmaktadır; eşkenar dörtgen kutular koşul sorusudur, koşul sağlanıyorsa “Evet”, sağlanmıyorsa “Hayır” okuyla ilerlenir.\nÇıkış kutusundaki z sayısı 5 olduğuna göre, bu sonucu veren x tam sayılarının toplamı kaçtır?',
 istenen='z = 5 sonucunu veren x tam sayılarının toplamı.',ip=['Çıkıştan başlayıp önce ikinci koşul kutusunun iki kolunu ayrı ayrı çöz.'],bilgi=[UST,DEN],sekil=SK,
 puf='Akış şemasında sonuçtan geriye giderken her kolu çöz ve bulduğunu o kolun koşuluna geri koyarak sına.')

# ================= 16 zor · öncüllü, sayı doğrusu, üstel kuvvetler =================
sx=1.15
o=[sayidog(-2,4,sx,[-2,-1,0,1,2,3,4])]
for v,nm,c in ((-1,'a','turu'),(1,'b','mavi'),(3,'c','mor')):
    o.append(f'\\fill[{c}] ({v*sx:.2f},0) circle (0.1); \\node[above=6pt,{c},font=\\small\\bfseries] at ({v*sx:.2f},0) {{$\\log_2 {nm}$}};')
SK=fig('\n'.join(o))
a16,b16,c16=Fr(1,2),2,8
tf16={1:float(a16)**float(c16)>b16**float(a16),2:abs(lg(b16*c16,4)-2)<1e-12,3:a16*c16<1}
assert tf16=={1:False,2:True,3:False},tf16
sp=onc('Yalnız II',tf16,{1:'a < 1 olduğundan aᶜ’nin büyük olduğunu sanmış; (1/2)⁸ = 1/256 ile 2^(1/2) ≈ 1,41’i karşılaştırmamış.',3:'a < 1 olduğunu görüp a·c’nin de 1’den küçük olacağını sanmış; a·c = 1/2 × 8 = 4 olduğunu hesaplamamış.'},{2:'log₄(b·c) = log₄16’yı hesaplamak yerine b·c = 16 değerinin 4 tabanındaki logaritmasını 2 değil 4 sanmış.'},[A('Değerleri oku','Her nokta, ilgili sayının 2 tabanındaki logaritmasıdır.','log₂a = −1 → a = 1/2 · log₂b = 1 → b = 2 · log₂c = 3 → c = 8'),A('I’i sına','(1/2)⁸ = 1/256; 2^(1/2) ≈ 1,41 olduğundan karşılaştır.','aᶜ = 1/256 < bᵃ ≈ 1,41 → yanlış'),A('II’yi sına','Çarpımı bulup 4 tabanında logaritma al.','b·c = 16 → log₄16 = 2 → doğru'),A('III’ü sına','Çarpım hesaplanır.','a·c = 4 > 1 → yanlış')],
 tipId='alg-dogru',tip='Sayı doğrusunda logaritma ve karşılaştırma',z='orta',alt='Sayı Doğrusunda Öncüller',kaz='Sayı doğrusunda verilen logaritma değerlerinden sayıları bulup üslü ve logaritmik ifadelerin doğruluğunu karşılaştırır.',kalip='öncüllü',
 kart='K-ALG-09 (öncüllü sayı doğrusu) · log₂a = −1, log₂b = 1, log₂c = 3; aᶜ, log₄(bc), a·c',
 metin='a, b ve c pozitif gerçel sayılar olmak üzere log₂a, log₂b ve log₂c değerlerinin sayı doğrusundaki yerleri şekilde gösterilmiştir.\nI. aᶜ > bᵃ\nII. log₄(b·c) = 2\nIII. a·c < 1\nifadelerinden hangileri doğrudur?',
 istenen='Doğru olan önermeler.',ip=['Sayı doğrusundaki noktaları 2 tabanında logaritma tanımıyla a, b, c sayılarına çevir.'],bilgi=[TAN,OZL],sekil=SK,
 puf='Logaritma değerleri verilmişse önce sayıların kendisini yaz; sonra önermeleri sayısal olarak sına.')
S('0016',sp['dogru'],sp['pool'],sp['ad'],**{k:v for k,v in sp.items() if k not in('dogru','pool','ad')})

# ================= 17 orta · desibel sütun grafiği =================
dB=[30,50,70,90]
I=lambda L:10**(Fr(L,10))
r17=(I(50)+I(70))/I(30); assert r17==10100
SK=fig(sutun(dB,['A','B','C','D'],100,20,0.034,genis=0.9,aralik_=1.5,yetik='Ses düzeyi (dB)',renk='turu!50',birim=''))
S('0017',10100,[pe(4,'Ses düzeyi dB değerlerini doğrudan oranlamış: (50 + 70) ÷ 30.','bilgi'),pe(60,'dB farklarını toplamış: (50 − 30) + (70 − 30).','bilgi'),pe(110,'Formülde 10 yerine 20 kullanıp 10^((L − L_A)/20) hesaplamış: 10¹ + 10².','bilgi'),pe(1000000,'Şiddet oranlarını toplamak yerine çarpmış: 10² × 10⁴.','islem'),pe(10200,'B için 10² yerine 10²’nin iki katını almış: 200 + 10000.','islem')],
 [A('Formülü kur','L = 10·log(I/I₀) olduğundan iki ses düzeyi farkı şiddet oranının logaritmasıdır.','L₂ − L₁ = 10·log(I₂/I₁)'),A('B’nin A’ya oranı','Fark 20 dB’dir.','20 = 10·log(I_B/I_A) → I_B/I_A = 10²'),A('C’nin A’ya oranı','Fark 40 dB’dir.','40 = 10·log(I_C/I_A) → I_C/I_A = 10⁴'),A('Toplam oran','Oranlar toplanır.','10² + 10⁴ = 10100')],
 tipId='alg-model',tip='Üstel ve logaritmik modelleme',z='orta',alt='Desibel',kaz='Ses düzeyi–şiddet bağıntısı ile sütun grafikten okunan düzeylerin şiddet oranlarını hesaplar.',kalip='hikâyeli',
 kart='K-ALG-06 (desibel sütun grafiği) · L = 10·log(I/I₀); A, B, C: 30, 50, 70 dB',
 metin='Bir şehirde dört farklı noktada (A, B, C, D) ölçülen ses düzeyleri aşağıdaki sütun grafikte gösterilmiştir. Ses düzeyi L desibel, ses şiddeti I ve referans şiddeti I₀ olmak üzere L = 10·log(I/I₀) bağıntısı kullanılmaktadır (burada log, 10 tabanındaki logaritmadır).\nBuna göre B ve C noktalarındaki ses şiddetlerinin toplamı, A noktasındaki ses şiddetinin kaç katıdır?',
 istenen='(I_B + I_C) ÷ I_A oranı.',ip=['Ses düzeyi farkının şiddet oranıyla ilişkisini formülden çıkar.'],bilgi=[MOD,OZL],sekil=SK,
 puf='Logaritmik ölçekte düzey farkı toplanır; gerçek şiddet oranları ise 10’un kuvvetleriyle çarpılır ya da toplanır.')

# ================= 18 zor · logₓ2 + log₂x = 5/2 =================
import itertools
t_=sp_.symbols('t'); kt_=sp_.solve(t_+1/t_-sp_.Rational(5,2),t_); assert sorted(kt_)==[sp_.Rational(1,2),2]
assert abs(sum([float(k) for k in kt_])-2.5)<1e-12
S('0018',Fr(5,2),[pe(1,'t + 1/t = 5/2 denkleminin kökleri çarpımı olan 1’i yazmış.','bilgi'),pe(2,'Yalnız büyük kök olan t = 2’yi bulup 2 yazmış.','dikkat'),pe(3,'t = 1/2’yi x = 2 sanıp x değerlerini 4 ve 2 almış: log₂(4 × 2) = 3.','islem'),pe(4,'x değerlerinden büyük olan 4’ü yazmış.','dikkat'),pe(5,'Denklemde 5/2’yi çarpıp yarıya bölmeden 5 yazmış.','islem')],
 [A('Değişken değiştir','logₓ2 = 1/log₂x olduğundan log₂x = t denir.','t + 1/t = 5/2'),A('t’yi bul','Payda eşitlenir.','2t² − 5t + 2 = 0 → t = 2 ya da t = 1/2'),A('x’leri bul','Logaritmanın tanımı kullanılır.','x = 2² = 4 ya da x = 2^(1/2) = √2'),A('İstenen ifade','İki x değerinin çarpımının 2 tabanındaki logaritması, t değerlerinin toplamıdır.','log₂(4·√2) = 2 + 1/2 = 5/2')],
 tipId='alg-denklem',tip='Logaritmalı denklem',z='zor',alt='Taban Değiştirmeli Denklem',kaz='Taban değiştirmeyle logaritmik ifadeyi yeni değişkene çevirip ikinci dereceden denklemi çözer ve kökler üzerinden ifade hesaplar.',kalip='düz',
 kart='K-ALG-05 (taban değiştirmeli denklem) · log₂x + logₓ2 = 5/2',
 metin='x pozitif ve 1’den farklı bir gerçel sayı olmak üzere\nlog₂x + logₓ2 = 5/2\neşitliğini sağlayan x değerlerinin çarpımının 2 tabanındaki logaritması kaçtır?',
 istenen='Denklemin köklerinin çarpımının 2 tabanındaki logaritması.',ip=['logₓ2 ifadesini 2 tabanında log₂x cinsinden yaz.'],bilgi=[OZL,DEN],
 puf='Taban ile argümanın yer değiştirdiği ifadeler birbirinin çarpmaya göre tersidir.')

# ================= 19 zor · aᵘ = bᵛ = k eşitliği =================
lx=lg(36,2); ly=lg(36,3)   # 1/x+1/y = m/z, x=z·lx, y=z·ly → m = 1/lx+1/ly
assert abs(1/lx+1/ly-0.5)<1e-12
S('0019',Fr(1,2),[pe(Fr(1,8),'36 = 6⁸ sanıp 1/z = 8·log_k6 yazmış: m = 1/8.','bilgi'),pe(Fr(1,4),'36 = 6⁴ sanıp 1/z = 4·log_k6 yazmış: m = 1/4.','bilgi'),pe(1,'36 yerine 6 alarak 1/x + 1/y = 1/z bulmuş.','bilgi'),pe(2,'36 = 6^(1/2) sanıp log_k6 = 2/z bulmuş: m = 2.','bilgi'),pe(4,'36 = 6^(1/4) sanıp log_k6 = 4/z bulmuş: m = 4.','bilgi'),pe(8,'36 = 6^(1/8) sanıp log_k6 = 8/z bulmuş: m = 8.','bilgi')],
 [A('Ortak değeri adlandır','Üç kuvvetin ortak değeri k olsun; üsler logaritma ile yazılır.','x = log₂k · y = log₃k · z = log₃₆k'),A('Tersleri yaz','Taban değiştirmeyle tersler başka tabanlı logaritma olur.','1/x = log_k2 · 1/y = log_k3 · 1/z = log_k36'),A('1/x + 1/y’yi hesapla','Aynı tabanda logaritmalar toplanır.','log_k2 + log_k3 = log_k6'),A('m’yi bul','36 = 6² olduğundan log_k36 = 2·log_k6.','1/z = 2·log_k6 → log_k6 = 1/(2z) → m = 1/2')],
 tipId='alg-ozellik',tip='Logaritma özellikleri',z='zor',alt='Üç Kuvvet Eşitliği',kaz='Üstel eşitlikten üsleri logaritma olarak yazıp terslerinin toplamını taban değiştirme ile hesaplar.',kalip='yeni nesil',
 kart='K-ALG-02 (üstel kuvvet eşitliği) · 2ˣ = 3ʸ = 36ᶻ; 1/x + 1/y = m/z',
 metin='x, y ve z sıfırdan ve birbirinden farklı gerçel sayılar olmak üzere\n2ˣ = 3ʸ = 36ᶻ\neşitliği sağlanmaktadır. Bu eşitliğe göre\n1/x + 1/y = m/z\nolduğuna göre m kaçtır?',
 istenen='m değeri.',ip=['Üslerin ortak değeri üzerinden x, y ve z’yi tek tabanda yaz.'],bilgi=[DEG,OZL],
 puf='Terslerin toplandığı bir ifadede logaritmanın tabanı ile argümanını değiştirmek toplamı tek logaritmaya çevirir.')

# ================= 20 orta · öncüllü, sayı doğrusunda çözüm kümesi =================
def isk(f,x): return f(x)
f1_=lambda x:x>0 and lg(x,0.5)>=-1-1e-12
f2_=lambda x:x!=0 and math.log2(x*x)<2-1e-12
f3_=lambda x:x>0 and x!=1 and (math.log(2)/math.log(x))<1-1e-12
import random
for x in [i/20 for i in range(-80,100)]:
    if x<=0: continue
    assert f1_(x)==(0<x<=2),x
for x in [i/20 for i in range(-80,100) if i]:
    assert f2_(x)==(-2<x<2),x
for x in [i/20 for i in range(1,100) if i!=20]:
    assert f3_(x)==(0<x<1 or x>2),x
tf20={1:True,2:False,3:False}   # I: boyalı küme doğru; II: 0 boyalı (yanlış); III: (0,1) eksik (yanlış)
def nokta(x,sx,dolu,y=0):
    return f'\\draw[thick,fill={"black" if dolu else "white"}] ({x*sx:.2f},{y}) circle (0.09);'
def satir(y,etiket,parcalar,noktalar,sx=0.95):
    o=[f'\\node[anchor=west,font=\\small\\bfseries] at (-3.3,{y+0.62}) {{{etiket}}};']
    o.append(f'\\draw[-{{Stealth}},thick] ({-3.3*sx:.2f},{y}) -- ({4.55*sx:.2f},{y});')
    for v in range(-3,5):
        o.append(f'\\draw[thick] ({v*sx:.2f},{y-0.07}) -- ({v*sx:.2f},{y+0.07}); \\node[below=2pt,font=\\scriptsize] at ({v*sx:.2f},{y}) {{${v}$}};')
    for a,b in parcalar: o.append(f'\\draw[line width=3.2pt,yesil!80!black] ({a*sx:.2f},{y}) -- ({b*sx:.2f},{y});')
    for x,d in noktalar: o.append(nokta(x,sx,d,y))
    return '\n'.join(o)
o=[satir(0,'I.  $\\log_{1/2}x\\geq -1$',[(0,2)],[(0,False),(2,True)]),
   satir(-1.9,'II.  $\\log_2 (x^2)<2$',[(-2,2)],[(-2,False),(0,True),(2,False)]),
   satir(-3.8,'III.  $\\log_x 2<1$',[(2,4.5)],[(2,False)])]
SK=fig('\n'.join(o))
sp=onc('Yalnız I',tf20,{2:'log₂(x²) < 2 için x² < 4 yazıp x = 0 değerinin tanım dışı olduğunu atlamış.',3:'logₓ2 < 1 için “2 < x” yazıp 0 < x < 1 aralığının da koşulu sağladığını görmemiş.'},{1:'Tabanı 1/2 olan logaritmada eşitsizlik yönünün değiştiğini bilmeden 0 < x ≤ 2 kümesini yanlış sanmış.'},[A('I’i çöz','Taban 1/2 olduğundan logaritma azalandır; yön değişir.','log₁/₂x ≥ −1 → x ≤ (1/2)⁻¹ = 2 ve x > 0 → (0, 2]'),A('II’yi çöz','Argüman pozitif ve 4’ten küçük; x = 0 için tanımsızdır.','x² < 4 ve x ≠ 0 → (−2, 2) − {0}'),A('III’ü çöz','Taban 1’den büyükse 2 < x; 0 ile 1 arasındaysa logaritma negatif olduğundan eşitsizlik sağlanır.','(0, 1) ∪ (2, ∞)'),A('Boyalı kümeleri karşılaştır','I doğru boyanmış; II’de 0 boyalı, III’te (0, 1) eksik.','Yalnız I')],
 tipId='alg-esitsizlik',tip='Logaritmalı eşitsizlik ve çözüm kümesi',z='orta',alt='Çözüm Kümesi',kaz='Tabanı 1’den küçük, argümanı kare ve tabanı değişken olan logaritmalı eşitsizliklerin çözüm kümelerini sayı doğrusunda değerlendirir.',kalip='öncüllü',
 kart='K-ALG-07 (çözüm kümesi, sayı doğrusu) · log₁/₂x ≥ −1, log₂(x²) < 2, logₓ2 < 1',
 metin='Aşağıda üç eşitsizlik verilmiş ve her birinin altındaki sayı doğrusunda bir küme koyu çizgiyle gösterilmiştir. İçi dolu nokta kümeye ait, içi boş nokta kümeye ait olmayan sınır değerini göstermektedir; koyu çizgi eksenin ucuna kadar uzanıyorsa küme sonsuza gider.\nBuna göre bu sayı doğrularından hangilerinde gösterilen küme, üstündeki eşitsizliğin gerçel sayılardaki çözüm kümesidir?',
 istenen='Boyalı kümesi çözüm kümesine eşit olan eşitsizlikler.',ip=['Her eşitsizlik için önce tanım koşulunu yaz, sonra tabanın 1’den büyük ya da küçük olmasına göre çöz.'],bilgi=[ESI,LOF],sekil=SK,
 puf='Tabanı değişkenli logaritmada taban 1’den büyük ve küçük olma durumlarını ayrı ayrı çöz.')
S('0020',sp['dogru'],sp['pool'],sp['ad'],**{k:v for k,v in sp.items() if k not in('dogru','pool','ad')})

# ================= harf dengesi ve yazım =================
def uygun(spk):
    dk=spk['dogru'][0] if isinstance(spk['dogru'],tuple) else Fr(spk['dogru'])
    ust=[p for p in spk['pool'] if p[0]>dk]; alt=[p for p in spk['pool'] if p[0]<dk]
    return [r for r in range(5) if len(alt)>=r and len(ust)>=4-r],alt,ust
OP=[uygun(s_) for s_ in SP]
import itertools as _it
def coz():
    sayi=[0]*5; sec=[None]*len(SP)
    def geri(i):
        if i==len(SP): return all(c==len(SP)//5 for c in sayi)
        for r in OP[i][0]:
            if sayi[r]<len(SP)//5:
                sayi[r]+=1; sec[i]=r
                if geri(i+1): return True
                sayi[r]-=1
        return False
    assert geri(0),'harf dengesi sağlanamadı'; return sec
SEC=coz()
for s_,r,(fe,alt,ust) in zip(SP,SEC,OP):
    dg=s_['dogru']; dk,dt=(dg[0],dg[1]) if isinstance(dg,tuple) else (Fr(dg),fm(dg))
    yan=alt[:r]+ust[:4-r]; assert len(yan)==4 and len({y[1] for y in yan}|{dt})==5
    for y in yan: assert len(y[2])>=12,(s_['no'],y)
    secenek=sorted([(dk,dt,None,None)]+[(y[0],y[1],y[2],y[3]) for y in yan],key=lambda e:e[0])
    sira=[e[1] for e in secenek]
    assert sira.index(dt)==r
    ad=s_['ad']; kw=dict(s_['kw'])
    mk(P,s_['no'],dogru=dt,yan=[(y[1],y[2],y[3]) for y in yan],sira=sira,ad=ad,adim=len(ad),**kw)

# ================= yaz =================
SCR='/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/loga'
for q_ in P.ANA: q_['kardes']=None
P.yaz(os.path.join(MD,'loga-1.json'),os.path.join(SCR,'bos-kardes.json'))
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=UK))['kartlar'].append(c['id'])
json.dump(dict(konu=P.konu_adi,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 AYT Matematik çıkmış soruları ve yayın soru bankaları (yalnız mantık), MEB 11–12. sınıf müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),open(os.path.join(HV,'kartlar','loga.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
