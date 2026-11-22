"""AYT Matematik · Logaritma (2. dalga) · 20 soruluk paket (3 kolay / 10 orta / 7 zor).
Her doğru cevap ve çeldirici değer kodla hesaplanıp assert edilir; şekiller TikZ ile aynı sayılardan üretilir.
Kardeş yok, ipucu 1. Çıktı: ayt-mat/logaiki-1.json, kartlar/logaiki.json."""
import sys,os,math,json
import sympy as sp_
MD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.dirname(MD)
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
H.KONU='Logaritma'
UK='amat|Logaritma'
P=Parti('logaiki','Logaritma',UK,ders='AYT Matematik',idon='aytmat')
KY='ÖSYM 2018–2026 AYT Matematik (Üstel ve Logaritmik Fonksiyonlar; yalnız mantık) · Bilgi Sarmal, Acil ve 345 AYT soru bankaları (yalnız mantık) · MEB 11–12. sınıf'
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)
COL=r'\definecolor{mavi}{HTML}{2563EB}\definecolor{turu}{HTML}{EA580C}\definecolor{mor}{HTML}{7C3AED}\definecolor{yesil}{HTML}{15803D}'
def fig(body,font='\\small'): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font='+font+']\n'+COL+'\n'+body+'\n\\end{tikzpicture}')
def lg(x,b): return math.log(x)/math.log(b)

TAN=B('Logaritmanın tanımı','a > 0, a ≠ 1 ve b > 0 olmak üzere logₐb = c ⇔ aᶜ = b. Örnek: log₂32 = 5 çünkü 2⁵ = 32; log₃(1/9) = −2 çünkü 3⁻² = 1/9')
OZL=B('Logaritma özellikleri','logₐ(m·n) = logₐm + logₐn · logₐ(m/n) = logₐm − logₐn · logₐ(mᵏ) = k·logₐm · a^(logₐm) = m. Taban değiştirme: logₐb = (log_c b) ÷ (log_c a); logₐb · log_b a = 1. Örnek: log₆4 + log₆9 = log₆36 = 2; log₈16 = (log₂16) ÷ (log₂8) = 4/3')
UST=B('Üstel fonksiyon','a > 0 ve a ≠ 1 olmak üzere f(x) = aˣ fonksiyonu a > 1 için artan, 0 < a < 1 için azalandır; grafiği (0, 1) noktasından geçer ve x-ekseni yatay asimptottur. f(x) = a^(x+b) + c grafiğinin yatay asimptotu y = c doğrusudur. Örnek: 5ˣ⁺¹ = 5·5ˣ ve 5ˣ⁻² = 5ˣ ÷ 25')
LOF=B('Logaritma fonksiyonu','f(x) = logₐx fonksiyonu x > 0 için tanımlıdır; a > 1 ise artan, 0 < a < 1 ise azalandır; grafiği (1, 0) noktasından geçer. f(x) = logₐx ile g(x) = aˣ birbirinin ters fonksiyonudur; grafikleri y = x doğrusuna göre simetriktir. Örnek: f(x) = log₃x ise f(9) = 2 ve f⁻¹(2) = 9')
DEN=B('Logaritmalı denklem','Önce tabanın ve logaritması alınan ifadelerin tanım koşulları yazılır; sonra logₐu = logₐv ise u = v ve logₐu = k ise u = aᵏ kullanılır; bulunan değerler tanım koşuluna sokularak denetlenir. Örnek: log₂(x − 1) = 3 ise x − 1 = 8 ve x = 9; x > 1 koşulunu sağlar')
ESI=B('Logaritmalı eşitsizlik','Tabanı a > 1 olan logaritma artan olduğundan eşitsizliğin yönü korunur; 0 < a < 1 ise yön değişir. Tanım koşulları ayrıca yazılıp çözüm kümesiyle kesiştirilir. Örnek: log₃x < 2 ise 0 < x < 9; log₁/₂x < 2 ise x > 1/4')
MOD=B('Sabit oranlı değişim','Her birim sürede aynı kat sayıyla çarpılan bir niceliğin t birim sonraki değeri N = N₀·rᵗ biçimindedir (r: bir birimdeki kat sayısı). İki ölçümden r bulunur, istenen değere ulaşma süresi r’nin kuvveti olarak yazılır. Örnek: her yıl 2 katına çıkan bir niceliğin 3 yıl sonra değeri 2³ = 8 katıdır')
OND=B('Ondalık logaritma ve basamak sayısı','Tabanı 10 olan logaritma log x ile gösterilir; log10 = 1 ve log(10ᵏ·x) = k + log x. Pozitif bir N sayısının basamak sayısı [log N] + 1 değerine eşittir ([ ]: tam kısım). Örnek: log7000 = 3 + log7 ≈ 3,85 olduğundan 7000 sayısı 4 basamaklıdır')
LOG_OLC=B('Logaritmik ölçek','Bir niceliğin logaritması ölçeğe konduğunda çarpma, ölçekte toplamaya; bölme ise çıkarmaya karşılık gelir: log(m·n) = log m + log n. Ölçekte b birim fark, nicelikler arasında tabanın b’inci kuvveti kadar bir oran demektir. Örnek: 2 tabanındaki ölçekte 3 birim fark, 2³ = 8 kat demektir')
TAM=B('Tam kısım','[t], t gerçel sayısından büyük olmayan en büyük tam sayıdır; örneğin [2,7] = 2, [−1,2] = −2 ve [4] = 4. Pozitif n için [logₐn] = k olması, aᵏ ≤ n < aᵏ⁺¹ demektir (a > 1). Örnek: [log₂n] = 3 ise 8 ≤ n < 16')

# ---------- kartlar ----------
kartla('K-ALG2-01','Ondalık logaritma, basamak sayısı ve tam kısım','Verilen log değerleri üzerinden 10 ve asal çarpanlar kullanılarak istenen değer yazılır; basamak sayısı [log N] + 1 ile bulunur; tam kısımlı toplamlarda n değerleri aᵏ ≤ n < aᵏ⁺¹ aralıklarında gruplanır.','Ondalık sayının logaritmasında 10’un kuvvetini atlamak; basamak sayısında +1’i unutmak; aralık uçlarını yanlış gruba katmak.','orta','tablo',3,'alg2-ondalik','Ondalık logaritma, basamak sayısı ve tam kısım')
kartla('K-ALG2-02','Ters fonksiyon ve y = x simetrisi','f(x) = aˣ ile logₐx birbirinin tersidir; grafikleri y = x doğrusuna göre simetriktir, noktaların koordinatları yer değiştirir; tabloda ters fonksiyon değeri, f(x) = y denklemi çözülerek bulunur.','Simetrik noktanın koordinatlarını yer değiştirmemek; ters fonksiyon değerini f(y) ile karıştırmak; sabiti atlamak.','kolay','grafik',3,'alg2-ters','Ters fonksiyon ve y = x simetrisi')
kartla('K-ALG2-03','Üslü, logaritmalı ifade ve tanımlı işlem','a^(logₐm) = m, logₐb · log_b c = logₐc gibi kurallar ifadeyi sadeleştirir; tanımlı yeni işlemde kural olduğu gibi uygulanır, ortak tabanda yazmak yol gösterir.','Farkı sayıların farkı sanmak; logₐb · log_b a = 1 kuralını yanlış çarpanlara uygulamak; tanımlı işlemde üs ile tabanı karıştırmak.','orta','düz',3,'alg2-ifade','Üslü ve logaritmalı ifadeler, tanımlı işlem')
kartla('K-ALG2-04','Logaritmik ölçek, cetvel ve eşit parçalama','Logaritmik ölçekte oran, uzaklık farkına dönüşür; iki ölçeğin kaydırılması bir sabit oranla çarpmadır; eşit uzunlukta iki bölmede toplam uzunluk iki yoldan yazılıp eşitlenir.','Oranı fark sanmak; kayma miktarını ters oranla uygulamak; parça sayısını yanlış kullanmak.','orta','grafik',4,'alg2-olcek','Logaritmik ölçek, cetvel ve çubuk')
kartla('K-ALG2-05','Grafikten üstel ve logaritmik fonksiyon bilgisi','Grafikte işaretli noktalardan taban, kayma ve sabit bulunur; yatay asimptot sabit terimi verir; log–log grafikte doğrunun denkleminden üstel ifade kurulur.','Asimptotu sabit değil ilk değer sanmak; tabanı 1’den küçük eğrinin yönünü yanlış okumak; eksen değerlerini karıştırmak.','orta','grafik',4,'alg2-grafik','Grafik okuma: üstel, logaritmik ve log–log')
kartla('K-ALG2-06','Logaritmalı denklem ve tanım koşulu','Tabanlar eşitlenir, logaritmalar tek logaritmaya indirilir ve bulunan kökler tanım koşuluna sokulur.','Tanım dışı kökü bırakmamak; taban değiştirirken katsayıyı kaçırmak; logaritmayı değerin yarısı gibi okumak.','orta','düz',4,'alg2-denklem','Logaritmalı denklem')
kartla('K-ALG2-07','Eşitsizlik ve sıralama','Üstel ve logaritmik eşitsizliklerde taban 1’den küçükse yön değişir; sayı doğrusundaki konumlardan aralık bilgisi alınıp ifadelerin her zaman doğruluğu sınanır.','Yön değiştirmeyi atlamak; tanım koşulunu unutmak; aralık bilgisiyle kesin değer varmış gibi karar vermek.','zor','şekilli',4,'alg2-esitsizlik','Eşitsizlik, aralık ve sıralama')
kartla('K-ALG2-08','Üstel büyüme modeli','İki ölçümden bir birimdeki kat sayı bulunur; istenen değere ulaşma süresi kat sayının kuvveti olarak yazılır ve başlangıç ölçüm anı hesaba katılır.','Aylık kat sayıyı iki aylık kat sayıyla karıştırmak; başlangıç ayını sıfır saymak; aralıktaki ay sayısını yanlış saymak.','orta','hikâyeli',4,'alg2-model','Üstel büyüme modeli')
kartla('K-ALG2-09','Geometrik şekilde üstel ve logaritmik uzunluklar','Kenar uzunlukları üstel ya da logaritmik ifade olan şekillerde çevre, sığma ve yay koşulları yazılıp denklem ya da çift eşitsizlik çözülür; uç değerlerin dahil olup olmadığı koşuldan okunur.','Çevre yerine yarım çevre kullanmak; teğet durumunu dışlamak; uzun kenarı sınır almak.','orta','şekilli',3,'alg2-geo','Şekilde üstel ve logaritmik uzunluk')

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


# ================= 0001 kolay · tablo, ondalık logaritma =================
l2,l3=Fr(30,100),Fr(48,100)
v1=2*l3+(1-l2)-2; assert v1==Fr(-34,100)
assert abs(math.log10(0.45)-float(v1))<0.01
e_a=2*l3+(1-l2)-1; e_b=3*l3+(1-l2)-2; e_c=2*l3+(1+l2)-2; e_d=-(2*l3+(1-l2)-1)
assert (e_a,e_b,e_c,e_d)==(Fr(66,100),Fr(14,100),Fr(26,100),Fr(-66,100)) and 2*l3+l2-2==Fr(-74,100)
SK=tablo_svg(['x','2','3'],[['log x','0,30','0,48']])
S('0001',v1,[pe(e_a,'0,45 = 45/10 yazıp 10’a bölmüş: log4,5 = 2·0,48 + (1 − 0,30) − 1 = 0,66; 0,45 = 45/100 olduğundan 2 çıkarılmalıydı.','dikkat'),pe(e_b,'log9 değerini 3·log3 diye hesaplamış (kare yerine üç katı): 1,44 + 0,70 − 2 = 0,14.','bilgi'),pe(e_c,'log5 = log10 − log2 yerine 1 + log2 yazmış: 0,96 + 1,30 − 2 = 0,26.','islem'),pe(e_d,'log4,5 = 0,66 bulup işaretini eksi yazmış: −0,66.','dikkat'),pe(Fr(-74,100),'log5 yerine log2 değerini almış: 2·0,48 + 0,30 − 2 = −0,74.','bilgi'),pe(Fr(166,100),'0,45 yerine 45 sayısının logaritmasını almış: 2·0,48 + 0,70 = 1,66.','dikkat')],
 [A('Sayıyı parçala','0,45 = 9·5 ÷ 100 ve 5 = 10 ÷ 2 olduğundan 0,45 yalnız 2, 3 ve 10’un kuvvetleriyle yazılır.','0,45 = (3² · 10) ÷ (2 · 100)'),A('Logaritmaya geç','Çarpım toplam, bölüm fark olur.','log0,45 = 2·log3 + log10 − log2 − log100'),A('Değerleri yerine koy','log10 = 1 ve log100 = 2 alınır.','2 × 0,48 + 1 − 0,30 − 2 = −0,34')],
 tipId='alg2-ondalik',tip='Ondalık logaritma, basamak sayısı ve tam kısım',z='kolay',alt='Ondalık Logaritma',kaz='Verilen yaklaşık log değerlerinden yararlanarak ondalık bir sayının logaritmasını hesaplar.',kalip='tablo',
 kart='K-ALG2-01 (ondalık logaritma, tablo) · log2 ve log3 verilir, log0,45 istenir',
 metin='x pozitif gerçel sayısının 10 tabanındaki logaritması log x ile gösterilmektedir. log2 ve log3 değerlerinin virgülden sonra iki basamağa yuvarlanmış yaklaşık değerleri aşağıdaki tabloda verilmiştir.\nBuna göre bu değerler kullanılarak log0,45 değeri kaç bulunur?',
 istenen='log0,45 değeri.',ip=['0,45 sayısını yalnız 2, 3 ve 10’un kuvvetlerinden oluşan bir kesir olarak yazmayı dene.'],bilgi=[OND,OZL],sekil=SK,
 puf='Tabloda yalnız iki asal sayı var; diğer sayılar 10, 2 ve 3 cinsinden yazılır.')

# ================= 0002 orta · cetvel, logaritmik ölçek =================
u=1.1
d=lg(48,2)-lg(30,2); x4=Fr(40*30,48)*1; assert x4==25
assert abs(lg(40,2)-d-lg(25,2))<1e-12
assert (40-(48-30),Fr(40*48,30),48*30//40,40*(48-30)//48,25)==(22,64,36,15,25)
body=[f'\\draw[line width=1.4pt] (0,1.5) -- ({6*u:.2f},1.5); \\draw[line width=1.4pt] ({d*u:.3f},0) -- ({(6+d)*u:.3f},0);']
for k in range(0,7):
    body.append(f'\\draw[thick] ({k*u:.2f},1.4) -- ({k*u:.2f},1.6); \\node[above=2pt,font=\\scriptsize] at ({k*u:.2f},1.6) {{${2**k}$}};')
body.append(f'\\draw[thick] ({d*u:.3f},-0.1) -- ({d*u:.3f},0.1); \\node[below=2pt,font=\\scriptsize] at ({d*u:.3f},-0.1) {{$1$}};')
body.append(f'\\node[font=\\small\\bfseries,anchor=east] at (-0.15,1.5) {{Üst}}; \\node[font=\\small\\bfseries,anchor=east] at ({d*u-0.15:.2f},0) {{Alt}};')
for n,c,anc in ((48,'turu','north west'),(40,'mavi','north east')):
    xp=lg(n,2)*u
    body.append(f'\\fill[{c}] ({xp:.3f},1.5) circle (0.075); \\draw[dashed,{c},thick] ({xp:.3f},1.5) -- ({xp:.3f},0); \\fill[{c}] ({xp:.3f},0) circle (0.075);')
    body.append(f'\\node[{c},font=\\small\\bfseries,anchor={anc}] at ({xp:.3f},1.38) {{${n}$}};')
body.append(f'\\node[turu,font=\\small\\bfseries,anchor=north west] at ({lg(48,2)*u:.3f},-0.1) {{$30$}}; \\node[mavi,font=\\small\\bfseries,anchor=north east] at ({lg(40,2)*u:.3f},-0.1) {{$x$}};')
SK=fig('\n'.join(body))
S('0002',25,[pe(22,'Cetvellerin kaymasını fark gibi düşünmüş: 40 − (48 − 30) = 22.','bilgi'),pe(15,'Oranı farkla karıştırıp 40 × (48 − 30) ÷ 48 hesaplamış.','islem'),pe(36,'Oranı ters yazmış: 48 × 30 ÷ 40 = 36.','dikkat'),pe(64,'Kayma oranını ters çevirmiş: 40 × 48 ÷ 30 = 64.','dikkat'),pe(40,'Kaymayı hiç dikkate almayıp üstteki 40 sayısını aynen yazmış.','dikkat')],
 [A('Kaymayı oran olarak yaz','Alttaki 30 üstteki 48 ile aynı konumdadır; uzaklıklar log₂ cinsinden olduğundan kayma oranı verir.','log₂48 − log₂30 = log₂(48/30) = log₂(8/5)'),A('x için eşitliği yaz','Üstteki 40 ile alttaki x aynı konumdadır; aynı kayma uygulanır.','log₂40 − log₂x = log₂(8/5)'),A('x’i bul','Fark logaritmaya çevrilir.','40/x = 8/5 → x = 25')],
 tipId='alg2-olcek',tip='Logaritmik ölçek, cetvel ve çubuk',z='orta',alt='Logaritmik Cetvel',kaz='Logaritmik ölçekli iki cetvelin kaymasını oran olarak yorumlayıp bilinmeyen sayıyı bulur.',kalip='şekilli',
 kart='K-ALG2-04 (logaritmik cetvel) · log₂ ölçeği, 48 ↔ 30, 40 ↔ x',
 metin='Şekilde, 1’den 64’e kadar sayıların yazılabildiği iki özdeş cetvel gösterilmiştir. Her cetvelde n sayısı, cetvelin 1 yazılı başlangıç noktasından log₂n birim uzaklıktadır. Cetveller şekildeki gibi üst üste getirildiğinde üstteki 48 sayısı alttaki 30 sayısına, üstteki 40 sayısı da alttaki x sayısına denk gelmektedir.\nBuna göre x kaçtır?',
 istenen='x sayısı.',ip=['Alttaki cetvelin ne kadar kaydığını, iki sayının uzaklık farkı olarak yaz.'],bilgi=[LOG_OLC,OZL],sekil=SK,
 puf='Logaritmik cetvelde kayma, sayılar arasında sabit bir oran demektir.')

# ================= 0003 orta · logaritmalı denklem =================
xx=sp_.symbols('x'); kk=sp_.solve((xx-1)**2-(xx+11),xx); assert sorted(kk)==[-2,5]
assert abs(lg(5-1,2)-lg(5+11,4))<1e-12
assert (-2*5,-2+5)==(-10,3)
assert 2*(13-1)==13+11
S('0003',5,[pe(-10,'(x − 1)² = x + 11 denkleminin köklerinin çarpımını yazmış: 5 · (−2).','bilgi'),pe(-2,'x² − 3x − 10 = 0 köklerinden x = −2’yi seçmiş; x − 1 < 0 olduğundan tanım dışı olduğunu görmemiş.','dikkat'),pe(3,'İki kökün toplamını yazmış: 5 + (−2).','bilgi'),pe(13,'log₄(x + 11) ifadesini (x + 11)/2 gibi okumuş: x − 1 = (x + 11)/2 → x = 13.','islem')],
 [A('Tabanı eşitle','log₄(x + 11) = ½·log₂(x + 11); eşitlik 2·log₂(x − 1) = log₂(x + 11) olur.','log₂(x − 1)² = log₂(x + 11)'),A('Denklemi çöz','Argümanlar eşitlenir.','(x − 1)² = x + 11 → x² − 3x − 10 = 0 → x = 5 ya da x = −2'),A('Tanım koşulunu denetle','x − 1 > 0 ve x + 11 > 0 olmalıdır.','x = −2 tanım dışı; x = 5')],
 tipId='alg2-denklem',tip='Logaritmalı denklem',z='orta',alt='Farklı Tabanlı Denklem',kaz='Farklı tabanlı logaritmaları aynı tabana getirerek denklemi çözer ve kökleri tanım koşuluyla denetler.',kalip='düz',
 kart='K-ALG2-06 (farklı tabanlı denklem) · log₂(x − 1) = log₄(x + 11)',
 metin='x gerçel sayısı için\nlog₂(x − 1) = log₄(x + 11)\neşitliği sağlanmaktadır.\nBuna göre x kaçtır?',
 istenen='x değeri.',ip=['İki tarafı aynı tabanda yazdıktan sonra argümanların tanım koşulunu da yaz.'],bilgi=[OZL,DEN],
 puf='Farklı tabanlı logaritmaları ortak tabana indirip argümanları eşitle; kökü tanım koşuluna sok.')

# ================= 0004 kolay · ters fonksiyon, y = x simetrisi =================
Ax,Ay=3,2**3; Bx,By=Ay,Ax; assert By==lg(Bx,2)
ab=math.hypot(Bx-Ax,By-Ay); assert abs(ab-5*math.sqrt(2))<1e-12
sx=sy=0.5
xs=aralik(-2.0,3.17,60); ys=aralik(0.26,9,70)
body=[eksen(-2.2,9,-2.2,9,sx,sy,[(i,f'${i}$') for i in range(-2,10) if i],[(i,f'${i}$') for i in range(-2,10) if i],izgara=True),
 f'\\draw[gray,dashed,thick] ({-2*sx:.2f},{-2*sy:.2f}) -- ({9.2*sx:.2f},{9.2*sy:.2f}); \\node[gray!70!black,font=\\small,anchor=west] at ({9.2*sx:.2f},{9.2*sy:.2f}) {{$y=x$}};',
 egri(lambda t:2**t,xs,sx,sy,'mavi'),egri(lambda t:lg(t,2),ys,sx,sy,'turu'),
 f'\\node[mavi,font=\\small\\bfseries,anchor=east] at ({2.45*sx:.2f},{5.3*sy:.2f}) {{$f$}}; \\node[turu,font=\\small\\bfseries,anchor=south] at ({8.4*sx:.2f},{lg(8.4,2)*sy+0.1:.2f}) {{$g$}};',
 f'\\draw[dashed,mavi] ({Ax*sx:.2f},0) -- ({Ax*sx:.2f},{Ay*sy:.2f}); \\fill ({Ax*sx:.2f},{Ay*sy:.2f}) circle (0.08); \\node[above left,font=\\small\\bfseries] at ({Ax*sx:.2f},{Ay*sy:.2f}) {{A}};']
SK=fig('\n'.join(body))
S('0004',(5*math.sqrt(2),'5√2'),[(5.0,'5','Yalnız apsisler farkını almış: 8 − 3 = 5.','bilgi'),(math.sqrt(73),'√73','A noktasının orijine uzaklığını almış: √(3² + 8²) = √73.','dikkat'),(10.0,'10','Apsis ve ordinat farklarını toplamış: 5 + 5.','islem'),(50.0,'50','Uzaklık formülünde karekökü almayı unutmuş: 5² + 5².','islem')],
 [A('A’nın ordinatını bul','A noktası f(x) = 2ˣ grafiği üzerindedir.','A(3, 8)'),A('B’yi bul','y = x’e göre simetrik noktada koordinatlar yer değiştirir; B, g(x) = log₂x üzerindedir.','B(8, 3)'),A('Uzaklığı hesapla','İki nokta arası uzaklık formülü uygulanır.','|AB| = √(5² + 5²) = 5√2')],
 tipId='alg2-ters',tip='Ters fonksiyon ve y = x simetrisi',z='kolay',alt='Ters Fonksiyon Grafiği',kaz='Üstel ve logaritmik fonksiyonların y = x doğrusuna göre simetrisini kullanarak iki nokta arasındaki uzaklığı hesaplar.',kalip='grafik',
 kart='K-ALG2-02 (y = x simetrisi) · f(x) = 2ˣ, g(x) = log₂x; |AB|',
 metin='Dik koordinat düzleminde f(x) = 2ˣ ve g(x) = log₂x fonksiyonlarının grafikleri ile y = x doğrusu çizilmiştir. A noktası f fonksiyonunun grafiği üzerindedir ve apsisi şekilde belirtilen noktadır. Şekilde gösterilmeyen B noktası g fonksiyonunun grafiği üzerindedir ve A, B noktaları y = x doğrusuna göre simetriktir.\nBuna göre |AB| kaç birimdir?',
 istenen='|AB| uzunluğu (birim).',ip=['A’nın ordinatını f kuralından bul; simetrik noktada koordinatların yer değiştirdiğini kullan.'],bilgi=[LOF,UST],sekil=SK,
 puf='y = x’e göre simetrik iki noktanın koordinatları birbirinin yer değiştirmişidir.')

# ================= 0005 zor · log–log grafik =================
# log2 y = (2/3) log2 x + 1 ; f(8)=8 ; f(a)=32 -> log2 a = 6
fx=lambda L:Fr(2,3)*L+1
assert fx(3)==3 and fx(0)==1 and fx(6)==5
fa=lambda a:2**float(fx(lg(a,2)))
assert abs(fa(8)-8)<1e-9 and abs(fa(64)-32)<1e-9
assert 2**4==16 and 2**9==512 and 2**5==32
assert (5-1)*Fr(3,2)==6 and (5+1)*Fr(3,2)==9 and 5-1==4
sx=sy=0.8
body=[eksen(0,7,0,6,sx,sy,[(i,f'${i}$') for i in range(1,8)],[(i,f'${i}$') for i in range(1,7)],xl='$\\log_2 x$',yl='$\\log_2 y$',izgara=True),
 f'\\draw[mavi,line width=2pt] (0,{1*sy}) -- ({4.5*sx},{4*sy}); \\fill[mavi] (0,{1*sy}) circle (0.08); \\fill[mavi] ({3*sx},{3*sy}) circle (0.08);']
SK=fig('\n'.join(body))
S('0005',64,[pe(8,'4 çarpanını unutup f(a) = f(8) yazmış; a = 8 bulmuş.','dikkat'),pe(16,'Doğrunun eğimini 1 sanıp log₂a + 1 = 5 yazmış: log₂a = 4.','bilgi'),pe(32,'log₂y = 5 değerini log₂x = 5 gibi okumuş (eksenleri karıştırmış): a = 2⁵.','bilgi'),pe(4,'f(a) = 4·f(8) eşitliğindeki 4 çarpanını a olarak okumuş.','bilgi'),pe(512,'Doğru denkleminde sabiti yanlış tarafa geçirmiş: log₂a = (5 + 1) · 3/2 = 9.','islem')],
 [A('Doğrunun denklemini yaz','Doğru (0, 1) ve (3, 3) noktalarından geçer; eğim 2/3’tür.','log₂y = (2/3)·log₂x + 1'),A('f(8)’i bul','log₂8 = 3 yerine konur.','log₂y = 3 → f(8) = 8'),A('f(a)’yı kur','f(a) = 4·f(8) = 32 olduğundan log₂y = 5.','(2/3)·log₂a + 1 = 5 → log₂a = 6'),A('a’yı bul','Logaritmanın tanımı kullanılır.','a = 2⁶ = 64')],
 tipId='alg2-grafik',tip='Grafik okuma: üstel, logaritmik ve log–log',z='zor',alt='Log–Log Grafik',kaz='Eksenleri logaritma olan doğrusal grafikten fonksiyonun üstel kuralını çıkarıp istenen değeri hesaplar.',kalip='grafik',
 kart='K-ALG2-05 (log–log grafik) · log₂y = (2/3)·log₂x + 1',
 metin='f: [1, ∞) → ℝ, y = f(x) fonksiyonu için log₂x ile log₂y arasındaki ilişki, birim karelere bölünmüş dik koordinat düzleminde şekilde gösterilmiştir.\nf(a) = 4·f(8) olduğuna göre a kaçtır?',
 istenen='a değeri.',ip=['Doğrunun denklemini yaz; log₂x ve log₂y değerlerini ayrı ayrı bul.'],bilgi=[LOF,OZL],sekil=SK,
 puf='Eksenlerdeki değerler logaritmadır; sonuçta sayının kendisine dönmek için tanımı kullan.')

# ================= 0006 orta · öncüllü, üç logaritma grafiği =================
a6,b6,c6=2,5,Fr(1,3)
assert lg(4,a6)==2 and abs(lg(5,b6)-1)<1e-12 and abs(lg(3,float(c6))+1)<1e-12
tf6={1:a6<b6,2:a6*c6>1,3:lg(a6,b6)<lg(b6,a6)}
assert tf6=={1:True,2:False,3:True},tf6
sx6,sy6=0.9,0.75
LC=lambda x,b:lg(x,b)
body=[eksen(0,6,-2,3,sx6,sy6,[(i,f'${i}$') for i in range(1,7)],[(i,f'${i}$') for i in range(-2,4) if i],izgara=True)]
body.append(egri(lambda x:lg(x,2),aralik(0.2,6,70),sx6,sy6,'mavi')); body.append(egri(lambda x:lg(x,5),aralik(0.1,6,70),sx6,sy6,'turu')); body.append(egri(lambda x:lg(x,1/3),aralik(0.4,6,70),sx6,sy6,'mor'))
for (x,y,c) in ((4,2,'mavi'),(5,1,'turu'),(3,-1,'mor')):
    body.append(f'\\draw[dashed,{c}] ({x*sx6:.2f},0) -- ({x*sx6:.2f},{y*sy6:.2f}) -- (0,{y*sy6:.2f}); \\fill[{c}] ({x*sx6:.2f},{y*sy6:.2f}) circle (0.08);')
body.append(f'\\node[mavi,font=\\small\\bfseries,anchor=west] at ({6.05*sx6:.2f},{lg(6,2)*sy6:.2f}) {{$y=\\log_a x$}}; \\node[turu,font=\\small\\bfseries,anchor=west] at ({6.05*sx6:.2f},{lg(6,5)*sy6:.2f}) {{$y=\\log_b x$}}; \\node[mor,font=\\small\\bfseries,anchor=west] at ({6.05*sx6:.2f},{lg(6,1/3)*sy6:.2f}) {{$y=\\log_c x$}};')
SK=fig('\n'.join(body))
sp=onc('I ve III',tf6,{2:'c = 1/3 yerine 3 okuyup a·c = 2·3 = 6 > 1 bulmuş.'},{1:'Eğrilerden yukarıda olanın tabanının daha büyük olduğunu sanıp a < b’yi yanlış bulmuş; oysa x > 1 için taban büyüdükçe logaritma küçülür.',3:'log₅2 ile log₂5’i karıştırıp küçük olan log₅2 ≈ 0,43’ün daha büyük olduğunu düşünmüş.'},
 [A('Tabanları oku','Eğrilerin işaretli noktaları logₐ4 = 2, log_b5 = 1 ve log_c3 = −1 verir.','a = 2 · b = 5 · c = 1/3'),A('I’i sına','a < b mi?','2 < 5 → doğru'),A('II’yi sına','Çarpım hesaplanır.','a·c = 2/3 < 1 → yanlış'),A('III’ü sına','log₅2 ile log₂5 birbirinin çarpmaya göre tersidir; biri 1’den küçük, diğeri büyüktür.','log₅2 < 1 < log₂5 → doğru')],
 tipId='alg2-grafik',tip='Grafik okuma: üstel, logaritmik ve log–log',z='orta',alt='Logaritma Grafikleri',kaz='Grafikte işaretli noktalardan logaritma fonksiyonlarının tabanlarını bulup öncüllü ifadeleri değerlendirir.',kalip='öncüllü',
 kart='K-ALG2-05 (üç logaritma grafiği) · log₂, log₅ ve log₁/₃',
 metin='a, b ve c pozitif ve 1’den farklı gerçel sayılar olmak üzere y = logₐx, y = log_bx ve y = log_cx fonksiyonlarının grafikleri aynı dik koordinat düzleminde çizilmiştir.\nI. a < b\nII. a·c > 1\nIII. log_ba < logₐb\nifadelerinden hangileri doğrudur?',
 istenen='Doğru olan öncüller.',ip=['Her eğrinin üzerindeki işaretli noktayı denklemde yerine yazıp tabanı bul.'],bilgi=[LOF,OZL],sekil=SK,
 puf='İşaretli bir noktadan taban bulunur; öncüller sayılarla tek tek denenir.')
S('0006',sp['dogru'],sp['pool'],sp['ad'],**{k:v for k,v in sp.items() if k not in('dogru','pool','ad')})

# ================= 0007 orta · basamak sayısı =================
lo2=Fr(301,1000)
N=4**30*5**45; assert N==2**15*10**45
assert len(str(N))==50
assert math.floor((60*lo2+45*(1-lo2)))+1==50
assert (math.floor(60*lo2+45*(1-lo2)),math.floor(60*lo2+45*lo2)+1,45+1,60+45)==(49,32,46,105)
S('0007',50,[pe(32,'log5 değerini de 0,301 alıp (60 + 45)·0,301 = 31,6 bulmuş; tam kısmına 1 eklemiş.','bilgi'),pe(46,'2¹⁵ çarpanını atıp yalnız 10⁴⁵ sayısının basamak sayısını yazmış.','dikkat'),pe(49,'Basamak sayısı için [logN] değerini almış, 1 eklemeyi unutmuş.','dikkat'),pe(105,'Üsleri toplayıp 60 + 45 diye basamak sayısı yazmış.','bilgi'),pe(45,'Sayıyı 10⁴⁵ sanıp basamak sayısını 45 yazmış (2¹⁵ çarpanını ve +1’i atlamış).','dikkat')],
 [A('Çarpanları 2 ve 5 cinsinden yaz','4³⁰ = 2⁶⁰; 5⁴⁵ ile 2⁴⁵ birleşince 10⁴⁵ olur.','N = 2⁶⁰ · 5⁴⁵ = 2¹⁵ · 10⁴⁵'),A('Logaritmayı hesapla','log2 = 0,301 kullanılır.','logN = 15 × 0,301 + 45 = 49,515'),A('Basamak sayısını bul','Basamak sayısı tam kısım artı 1’dir.','[49,515] + 1 = 50')],
 tipId='alg2-ondalik',tip='Ondalık logaritma, basamak sayısı ve tam kısım',z='orta',alt='Basamak Sayısı',kaz='Verilen log2 değerinden üstel çarpımın basamak sayısını hesaplar.',kalip='düz',
 kart='K-ALG2-01 (basamak sayısı) · log2 verilir, 4ᵃ·5ᵇ’nin basamak sayısı',
 metin='log2 = 0,301 olduğuna göre\n4³⁰ · 5⁴⁵\nsayısı kaç basamaklıdır?',
 istenen='Sayının basamak sayısı.',ip=['Sayıyı 10’un bir kuvveti ile 2’nin bir kuvvetinin çarpımı olarak yaz.'],bilgi=[OND],
 puf='Önce 10’un kuvvetini ayır; geriye kalan çarpanın logaritması basamak sayısını belirler.')

# ================= 0008 zor · tablo, ters fonksiyon ve bileşke =================
g=lambda x:2*2**x+3
assert (g(0),g(1),g(2))==(5,7,11) and g(4)==35 and g(3)==19 and g(7)==259
assert (7,35+19,2**7+3,2*2**7,2*2**8+3)==(7,54,131,256,515)
SK=tablo_svg(['x','0','1','2'],[['f(x)','5','7','11']])
S('0008',259,[pe(7,'f⁻¹(35) + f⁻¹(19) = 4 + 3 = 7 toplamını bulup f’yi uygulamayı unutmuş.','dikkat'),pe(54,'f⁻¹ yerine verilen 35 ve 19 değerlerini toplamış.','bilgi'),pe(131,'f(7) hesabında a = 2 katsayısını unutmuş: 2⁷ + 3.','islem'),pe(256,'f(7) hesabında sabit terimi unutmuş: 2·2⁷.','islem'),pe(515,'Üssü bir fazla almış: 2·2⁸ + 3.','islem')],
 [A('Denklemleri kur','Tablodaki üç değer f(x) = a·bˣ + c kuralında yerine yazılır.','a + c = 5 · ab + c = 7 · ab² + c = 11'),A('a, b ve c’yi bul','Ardışık farklar oranlanır: a(b − 1) = 2 ve ab(b − 1) = 4.','b = 2 · a = 2 · c = 3'),A('Ters fonksiyon değerlerini bul','f(x) = 35 ve f(x) = 19 denklemleri çözülür.','2ˣ⁺¹ = 32 → x = 4 · 2ˣ⁺¹ = 16 → x = 3'),A('Toplamı hesapla','İki ters fonksiyon değeri toplanır.','4 + 3 = 7'),A('f(7)’yi hesapla','Toplam f’ye yerleştirilir.','2·2⁷ + 3 = 259')],
 tipId='alg2-ters',tip='Ters fonksiyon ve y = x simetrisi',z='zor',alt='Tablodan Üstel Fonksiyon',kaz='Tablodan üç bilinmeyenli üstel fonksiyonu bulup ters fonksiyon değerlerini bileşkede kullanır.',kalip='tablo',
 kart='K-ALG2-02 (tablo, ters fonksiyon) · f(x) = a·bˣ + c; f(f⁻¹(35) + f⁻¹(19))',
 metin='a > 0, b > 1 ve c birer gerçel sayı olmak üzere f(x) = a·bˣ + c fonksiyonunun bazı değerleri aşağıdaki tabloda verilmiştir.\nBuna göre f(f⁻¹(35) + f⁻¹(19)) ifadesinin değeri kaçtır?',
 istenen='f(f⁻¹(35) + f⁻¹(19)) değeri.',ip=['Önce tablodaki üç değerle fonksiyonun kuralını bulmayı dene.'],bilgi=[UST,LOF],sekil=SK,
 puf='Ters fonksiyon değeri sorulduğunda f(x) = verilen değer denklemini çöz.')

# ================= 0009 kolay · logaritma ifadesi =================
v9=lg(3,2)*lg(16,3)+7**(lg(20,7)-lg(4,7)); assert abs(v9-9)<1e-9
assert (4+(20-4),4,5,1+5)==(20,4,5,6)
S('0009',9,[pe(20,'7^(log₇20 − log₇4) ifadesini 20 − 4 = 16 diye hesaplamış: 4 + 16.','islem'),pe(5,'Yalnız ikinci terimi hesaplamış, çarpım teriminin 4 olduğunu toplamaya katmamış.','dikkat'),pe(4,'Yalnız ilk terimi hesaplamış; üslü terimi eklememiş.','dikkat'),pe(6,'log₂3 · log₃16 çarpımını logₐb · log_ba = 1 kuralıyla 1 yazmış: 1 + 5.','bilgi')],
 [A('Çarpımı sadeleştir','Taban değiştirme ile çarpım tek logaritma olur.','log₂3 · log₃16 = log₂16 = 4'),A('Üslü terimi sadeleştir','Fark, bölümün logaritmasıdır; a^(logₐm) = m.','7^(log₇(20/4)) = 7^(log₇5) = 5'),A('Topla','İki değer toplanır.','4 + 5 = 9')],
 tipId='alg2-ifade',tip='Üslü ve logaritmalı ifadeler, tanımlı işlem',z='kolay',alt='Logaritma Hesabı',kaz='Taban değiştirme ve a^(logₐm) = m özelliklerini birlikte kullanarak ifadenin değerini bulur.',kalip='düz',
 kart='K-ALG2-03 (özellik hesabı) · log₂3·log₃16 + 7^(log₇20 − log₇4)',
 metin='log₂3 · log₃16 + 7^(log₇20 − log₇4)\nişleminin sonucu kaçtır?',
 istenen='İfadenin değeri.',ip=['Üslü terimde üsteki farkı tek logaritmada birleştir.'],bilgi=[OZL],
 puf='Önce her terimi ayrı ayrı sadeleştir, sonra topla.')

# ================= 0010 orta · dikdörtgen çevresi, üstel uzunluklar =================
xv=3; AEv,EBv,BCv=2**(xv+1),2**(xv-1),2**xv
assert 2*(AEv+EBv+BCv)==56 and AEv+EBv==20 and (AEv,EBv,BCv)==(16,4,8)
assert 2*(AEv+EBv+BCv)//2==28
assert Fr(56)/Fr(7,2)==16 and 16*Fr(5,2)==40
u=1.3
body=[f'\\fill[mavi!12] (0,0) rectangle ({5*u:.2f},{2*u:.2f}); \\draw[thick] (0,0) rectangle ({5*u:.2f},{2*u:.2f});',
 f'\\fill ({4*u:.2f},0) circle (0.07); \\draw[thick] ({4*u:.2f},0) -- ({4*u:.2f},0.12);',
 f'\\node[below left,font=\\small\\bfseries] at (0,0) {{A}}; \\node[below right,font=\\small\\bfseries] at ({5*u:.2f},0) {{B}}; \\node[above right,font=\\small\\bfseries] at ({5*u:.2f},{2*u:.2f}) {{C}}; \\node[above left,font=\\small\\bfseries] at (0,{2*u:.2f}) {{D}}; \\node[below,font=\\small\\bfseries] at ({4*u:.2f},0) {{E}};',
 f'\\node[below,font=\\normalsize] at ({2*u:.2f},-0.65) {{$2^{{x+1}}$}}; \\node[below,font=\\normalsize] at ({4.5*u:.2f},-0.65) {{$2^{{x-1}}$}}; \\node[right,font=\\normalsize] at ({5*u:.2f},{1*u:.2f}) {{$2^{{x}}$}};',
 f'\\draw[<->,thick] (0,-0.62) -- ({4*u:.2f},-0.62); \\draw[<->,thick] ({4*u:.2f},-0.62) -- ({5*u:.2f},-0.62);']
SK=fig('\n'.join(body))
S('0010',20,[pe(8,'|AB| yerine 2ˣ = 8 değerini yazmış.','bilgi'),pe(16,'Yalnız |AE| uzunluğunu yazmış: 2⁴.','dikkat'),pe(28,'Çevrenin yarısını (|AB| + |BC| = 28) |AB| olarak yazmış.','islem'),pe(40,'56’yı yarım çevre sanıp 3,5·2ˣ = 56’dan 2ˣ = 16 bulmuş: |AB| = 2,5 · 16.','dikkat'),pe(56,'Çevre değerini |AB| olarak yazmış.','dikkat')],
 [A('Çevreyi yaz','Kenarlar 2ˣ cinsinden yazılır: |AB| = 2ˣ⁺¹ + 2ˣ⁻¹ = 2,5·2ˣ ve |BC| = 2ˣ.','2·(2,5·2ˣ + 2ˣ) = 7·2ˣ = 56'),A('x’i bul','Çevre denklemi çözülür.','2ˣ = 8 → x = 3'),A('|AB|’yi hesapla','Değer yerine konur.','2⁴ + 2² = 20')],
 tipId='alg2-geo',tip='Şekilde üstel ve logaritmik uzunluk',z='orta',alt='Üstel Uzunluklar',kaz='Kenar uzunlukları üstel ifade olan dikdörtgenin çevre koşulundan x’i bulup uzunluk hesaplar.',kalip='şekilli',
 kart='K-ALG2-09 (üstel kenar uzunlukları) · |AE| = 2ˣ⁺¹, |EB| = 2ˣ⁻¹, |BC| = 2ˣ',
 metin='Şekildeki ABCD dikdörtgeninde E noktası [AB] üzerindedir; |AE|, |EB| ve |BC| uzunlukları şekilde x gerçel sayısına bağlı olarak verilmiştir (şekil ölçeklidir).\nABCD dikdörtgeninin çevresi 56 birim olduğuna göre |AB| kaç birimdir?',
 istenen='|AB| uzunluğu (birim).',ip=['Her kenarı 2ˣ cinsinden yazıp çevreyi 2ˣ’in katı olarak ifade et.'],bilgi=[UST],sekil=SK,
 puf='Üsleri farklı terimleri en küçük üssün katı olarak yazınca çevre denklemi tek bilinmeyenli olur.')

# ================= 0011 zor · sayı doğrusu, çözüm kümesi, m =================
def cozum(m): return lambda x:(x*x-3*x>0) and lg(x*x-3*x,0.5)>m+1e-12
f_=cozum(-2)
for i in range(-300,500):
    x=i/50
    assert f_(x)==((-1<x<0) or (3<x<4)),x
assert 4==(0.5)**(-2) and (1/4)**(-1)==4
sxs=1.0
o=[f'\\draw[-{{Stealth}},thick] ({-2.6*sxs:.2f},0) -- ({5.6*sxs:.2f},0);']
for v in range(-2,6): o.append(f'\\draw[thick] ({v*sxs:.2f},-0.07) -- ({v*sxs:.2f},0.07); \\node[below=3pt,font=\\small] at ({v*sxs:.2f},0) {{${v}$}};')
for a,b in ((-1,0),(3,4)): o.append(f'\\draw[line width=3.4pt,mavi!85] ({a*sxs:.2f},0) -- ({b*sxs:.2f},0);')
for v in (-1,0,3,4): o.append(f'\\draw[thick,fill=white] ({v*sxs:.2f},0) circle (0.1);')
SK=fig('\n'.join(o))
S('0011',-2,[pe(2,'Sınır değerinde (1/2)ᵐ = 4 eşitliğini m = 2 olarak çözmüş (üssün işaretini atlamış).','islem'),pe(4,'x² − 3x = 4 sınır değerini doğrudan m olarak yazmış.','bilgi'),pe(Fr(1,4),'(1/2)ᵐ = 4 eşitliğinde 4’ün tersini alıp m = 1/4 yazmış.','islem'),pe(-1,'Tabanı 1/4 okuyup (1/4)ᵐ = 4 eşitliğinden m = −1 bulmuş.','dikkat')],
 [A('Tanım koşulunu yaz','Logaritmanın argümanı pozitif olmalıdır.','x² − 3x > 0 → x < 0 ya da x > 3'),A('Eşitsizliği çöz','Taban 1/2 < 1 olduğundan eşitsizlik yön değiştirir.','x² − 3x < (1/2)ᵐ'),A('Uç noktaları kullan','Çözüm kümesinin −1 ve 4 uçları x² − 3x = (1/2)ᵐ denkleminin kökleridir; x = −1 için sol taraf 4’tür.','(1/2)ᵐ = 4'),A('m’yi bul','4 = (1/2)⁻² olduğundan üsler eşitlenir.','m = −2')],
 tipId='alg2-esitsizlik',tip='Eşitsizlik, aralık ve sıralama',z='zor',alt='Çözüm Kümesinden Parametre',kaz='Tabanı 1’den küçük logaritmalı eşitsizliğin çözüm kümesinden parametreyi bulur.',kalip='şekilli',
 kart='K-ALG2-07 (çözüm kümesi, parametre) · log₁/₂(x² − 3x) > m',
 metin='m bir gerçel sayı olmak üzere\nlog₁/₂(x² − 3x) > m\neşitsizliğinin gerçel sayılardaki çözüm kümesi, sayı doğrusunda koyu çizgiyle gösterilmiştir. İçi boş nokta, o sayının çözüm kümesine ait olmadığını göstermektedir.\nBuna göre m kaçtır?',
 istenen='m değeri.',ip=['Önce tanım koşulunu yaz ve tabanı 1 ile karşılaştır.'],bilgi=[ESI],sekil=SK,
 puf='Çözüm kümesini hangi koşulların kesiştirdiğini adım adım yaz.')

# ================= 0012 orta · hikâyeli, üstel büyüme =================
Nn=lambda t:50*3**(t-1)
assert Nn(3)==450 and Nn(6)==12150
assert 3**5==243 and 5+2==7
SK=tablo_svg(['Ay','1','3'],[['Kullanıcı sayısı','50','450']])
S('0012',6,[pe(4,'3ᵗ⁻¹ = 243 → t − 1 = 5 bulduktan sonra 1. ay başlangıç olduğundan bir daha 1 çıkarmış: t = 4.','islem'),pe(5,'Başlangıcı 0. ay sayıp 50·3ᵗ = 12 150 → 3ᵗ = 243 → t = 5 yazmış.','dikkat'),pe(7,'t − 1 = 5 bulup 1. ay ile 3. ay arasındaki 2 ayı da ekleyerek 5 + 2 yazmış.','islem'),pe(8,'t − 1 = 5 bulup 5 + 3 = 8 yazmış (3. ayı süreye eklemiş).','islem'),pe(11,'3 katını iki ayda bir sanıp 5 dönem × 2 ay = 10 ay bulmuş, 1. ayı eklemiş.','islem')],
 [A('Aylık kat sayıyı bul','1. aydan 3. aya 2 ay geçmiştir; aylık kat sayı r olsun.','50·r² = 450 → r = 3'),A('Eşitliği kur','Kullanıcı sayısı 1. aydan başlayıp (t − 1) ay boyunca r katına çıkar.','50·3ᵗ⁻¹ = 12 150 → 3ᵗ⁻¹ = 243'),A('Üsleri eşitle','243 = 3⁵.','t − 1 = 5'),A('Ayı bul','Eşitlikten t hesaplanır.','t = 6')],
 tipId='alg2-model',tip='Üstel büyüme modeli',z='orta',alt='Sabit Oranlı Artış',kaz='İki ölçümden aylık kat sayıyı bulup istenen kullanıcı sayısına ulaşılan ayı hesaplar.',kalip='hikâyeli',
 kart='K-ALG2-08 (üstel büyüme) · 50 ve 450 kullanıcı, 1. ve 3. ay',
 metin='Yeni çıkan bir mobil uygulamanın kullanıcı sayısı her ay bir önceki ayın aynı katı kadar artmakta ve bu kat sayı 1’den büyüktür. Uygulamanın 1. ve 3. aylardaki kullanıcı sayıları aşağıdaki tabloda verilmiştir.\nBuna göre uygulamanın kullanıcı sayısı kaçıncı ayda 12 150 olur?',
 istenen='Kullanıcı sayısının 12 150 olduğu ay.',ip=['İki ölçüm arasında kaç ay geçtiğini yazıp aylık kat sayıyı bul.'],bilgi=[MOD],sekil=SK,
 puf='Önce aylık kat sayıyı bul.')

# ================= 0013 zor · tanımlı işlem a★b = a^(log₂b) =================
st=lambda a,b:a**lg(b,2)
assert abs(st(81,4)-6561)<1e-6 and abs(st(9,16)-6561)<1e-6
for xx_,dv in ((81,12),(9,6),(27,9),(6561,24)):
    assert abs(lg(st(xx_,8),3)-dv)<1e-6,(xx_,dv)
assert 4==lg(81,3) and 4*8==32
S('0013',12,[pe(4,'x = 81 bulup log₃(x ★ 8) yerine yalnız log₃x değerini yazmış.','dikkat'),pe(6,'log₂4 yerine 4 alıp x = 9 bulmuş: log₃(9³) = 6.','bilgi'),pe(9,'9 ★ 16’da log₂16 yerine 3 alıp x = 27 bulmuş: log₃(27³) = 9.','islem'),pe(24,'log₂16 yerine 8 alıp x = 9⁴ = 3⁸ bulmuş: log₃((3⁸)³) = 24.','islem'),pe(32,'x = 81 bulmuş ama x ★ 8 hesabında log₂8 yerine 8 alıp log₃(81⁸) = 32 yazmış.','islem')],
 [A('Sol tarafı yaz','Tanıma göre x ★ 4 = x^(log₂4).','x ★ 4 = x²'),A('Sağ tarafı yaz','9 ★ 16 = 9^(log₂16).','9 ★ 16 = 9⁴'),A('x’i bul','x pozitif olduğundan karekök alınır.','x² = 9⁴ → x = 81'),A('x ★ 8’i hesapla','Tanım yeniden uygulanır; 81 = 3⁴.','81³ = 3¹²'),A('Logaritmayı al','3 tabanında logaritma alınır.','log₃3¹² = 12')],
 tipId='alg2-ifade',tip='Üslü ve logaritmalı ifadeler, tanımlı işlem',z='zor',alt='Tanımlı İşlem',kaz='Tanımlı işlemde üstel ve logaritmik ifadeyi uygulayıp denklem çözer ve sonucu logaritmaya taşır.',kalip='yeni nesil',
 kart='K-ALG2-03 (tanımlı işlem) · a ★ b = a^(log₂b)',
 metin='a ve b pozitif gerçel sayıları için\na ★ b = a^(log₂b)\nişlemi tanımlanıyor.\nx pozitif bir gerçel sayı olmak üzere\nx ★ 4 = 9 ★ 16\nolduğuna göre log₃(x ★ 8) kaçtır?',
 istenen='log₃(x ★ 8) değeri.',ip=['Tanımı iki tarafa ayrı ayrı uygulayıp üsleri hesapla.'],bilgi=[OZL],
 puf='Yeni işlemde sayıları tanıma olduğu gibi yerleştir.')

# ================= 0014 orta · üstel grafik, asimptot =================
f14=lambda x:3.0**(x-1)-2
assert f14(1)==-1 and f14(2)==1 and f14(4)==25
assert (27-1,27,81-1-2,81-2,27-3)==(26,27,78,79,24)
sx,sy=1.1,0.72
body=[eksen(-2.5,2.7,-2.6,4.2,sx,sy,[(i,f'${i}$') for i in range(-2,3) if i],[(i,f'${i}$') for i in (-1,1,2,3,4)],izgara=True),
 egri(f14,aralik(-2.4,2.62,70),sx,sy,'mavi'),
 f'\\draw[dashed,turu,thick] ({-2.5*sx:.2f},{-2*sy:.2f}) -- ({2.9*sx:.2f},{-2*sy:.2f}); \\node[turu,font=\\small\\bfseries,anchor=south west] at ({-2.4*sx:.2f},{-2*sy+0.03:.2f}) {{$y=-2$}};']
for (x,y) in ((1,-1),(2,1)):
    body.append(f'\\draw[dashed,gray] ({x*sx:.2f},0) -- ({x*sx:.2f},{y*sy:.2f}) -- (0,{y*sy:.2f}); \\fill[mavi] ({x*sx:.2f},{y*sy:.2f}) circle (0.08);')
SK=fig('\n'.join(body))
S('0014',25,[pe(24,'Yatay asimptotu y = −3 okuyup 3³ − 3 hesaplamış.','dikkat'),pe(26,'Sabit terimi asimptot yerine (1, −1) noktasının ordinatı olan −1 okumuş: 27 − 1.','bilgi'),pe(27,'Yatay asimptotu hesaba katmayıp yalnız 3⁴⁻¹ = 27 yazmış.','dikkat'),pe(78,'b = −1 değerini üste değil sabit terim olarak ekleyip 3⁴ − 1 − 2 hesaplamış.','islem'),pe(79,'b = −1 değerini unutup 3⁴ − 2 hesaplamış.','islem')],
 [A('Sabit terimi oku','Grafik kesikli yatay doğruya yaklaşır; y = c doğrusu yatay asimptottur.','c = −2'),A('b’yi bul','(1, −1) noktasında aᵇ⁺¹ − 2 = −1 olduğundan aᵇ⁺¹ = 1.','b + 1 = 0 → b = −1'),A('a’yı bul','(2, 1) noktasında aᵇ⁺² − 2 = 1.','a¹ = 3 → a = 3'),A('f(4)’ü hesapla','Kural: f(x) = 3ˣ⁻¹ − 2.','3³ − 2 = 25')],
 tipId='alg2-grafik',tip='Grafik okuma: üstel, logaritmik ve log–log',z='orta',alt='Üstel Fonksiyon Grafiği',kaz='Yatay asimptot ve işaretli noktalardan üstel fonksiyonun kuralını bulup değer hesaplar.',kalip='grafik',
 kart='K-ALG2-05 (üstel grafik, asimptot) · f(x) = a^(x+b) + c',
 metin='a > 1, b ve c birer gerçel sayı olmak üzere f(x) = a^(x+b) + c fonksiyonunun grafiği ve grafiğin yaklaştığı yatay doğru (kesikli çizgi) şekilde verilmiştir. Grafik, işaretli noktalardan geçmektedir.\nBuna göre f(4) kaçtır?',
 istenen='f(4) değeri.',ip=['Kesikli yatay doğrunun denkleminden sabit terimi oku, sonra işaretli noktaları yerine yaz.'],bilgi=[UST],sekil=SK,
 puf='Yatay asimptot sabit terimi verir; kalan iki bilinmeyen için iki nokta yeter.')

# ================= 0015 zor · çubuk, eşit uzunluk =================
Lv=10; assert 3*Lv==5*(Lv-4)==30
assert (5*Lv,3*40,5*(5-2)) and 3*5==15 and 3*Lv==30 and 3*40==5*(40-16)
cw=7.0
o=[]
for yy,n,lab,c in ((1.1,3,'\\log_2 x','mavi'),(0,5,'\\log_2\\frac{x}{16}','turu')):
    for i in range(n):
        o.append(f'\\fill[{c}!18] ({i*cw/n:.3f},{yy}) rectangle ({(i+1)*cw/n:.3f},{yy+0.7}); \\draw[thick] ({i*cw/n:.3f},{yy}) rectangle ({(i+1)*cw/n:.3f},{yy+0.7}); \\node[font=\\small] at ({(i+0.5)*cw/n:.3f},{yy+0.35}) {{${lab}$}};'.replace('font=\\small','font=\\normalsize'))
o.append(f'\\node[font=\\small\\bfseries,anchor=east] at (-0.15,1.45) {{1. çubuk}}; \\node[font=\\small\\bfseries,anchor=east] at (-0.15,0.35) {{2. çubuk}};')
o.append(f'\\draw[dashed,gray] (0,-0.2) -- (0,1.9); \\draw[dashed,gray] ({cw},-0.2) -- ({cw},1.9);')
SK=fig('\n'.join(o))
S('0015',30,[pe(10,'Çubuğun uzunluğu yerine bir parçanın uzunluğunu (log₂x = 10) yazmış.','dikkat'),pe(15,'log₂16 yerine 2 alıp 3L = 5(L − 2) → L = 5 bulmuş; uzunluk 3·5.','islem'),pe(50,'L = 10 bulduktan sonra 5·log₂x hesaplamış (ikinci çubuğun parça sayısı kadar).','bilgi'),pe(120,'x/16 için L − 16 yazıp 3L = 5(L − 16) → L = 40 bulmuş: 3·40.','islem'),pe(60,'İki çubuğun toplam uzunluğunu yazmış: 2 · 30.','dikkat')],
 [A('Parça uzunluğunu adlandır','log₂x = L olsun; ikinci çubuktaki parça log₂x − log₂16 = L − 4 olur.','1. çubuk: 3L · 2. çubuk: 5(L − 4)'),A('Eşit uzunluğu yaz','İki çubuk eşit uzunluktadır.','3L = 5(L − 4) → L = 10'),A('Uzunluğu bul','Çubuk 3 parçadır.','3 × 10 = 30')],
 tipId='alg2-olcek',tip='Logaritmik ölçek, cetvel ve çubuk',z='orta',alt='Eşit Parçalama',kaz='Eş parçalara bölünmüş iki çubuğun eşit uzunluğundan logaritmik bir bilinmeyeni bulur.',kalip='şekilli',
 kart='K-ALG2-04 (eşit parçalama) · 3 · log₂x = 5 · log₂(x/16)',
 metin='Aynı uzunlukta iki çubuktan birincisi 3, ikincisi 5 eş parçaya bölünmüştür. Parçaların uzunlukları (birim) şekilde logaritmik ifadelerle gösterilmiştir.\nBuna göre çubuklardan her birinin uzunluğu kaç birimdir?',
 istenen='Bir çubuğun uzunluğu (birim).',ip=['Birinci çubuktaki parça uzunluğuna bir ad ver; ikinciyi bölüm kuralıyla bu ad cinsinden yaz.'],bilgi=[OZL],sekil=SK,
 puf='İki çubuğun toplam uzunluğunu iki ayrı yoldan yazıp eşitle.')

# ================= 0016 orta · sütun grafik, logaritmik ölçek =================
hv=[6,5,13]; assert 2**(hv[2]-hv[0]-hv[1])==4
assert (2**(13-6),2**(13-5),Fr(1,4),13-6-5)==(128,256,Fr(1,4),2)
SK=fig(sutun(hv,['K','L','M'],14,1,0.3,genis=1.0,aralik_=1.7,yetik='$\\log_2$ (bakteri sayısı)',deger=False))
S('0016',4,[pe(Fr(1,4),'Oranı ters yazmış: (K · L) ÷ M = 2⁻².','dikkat'),pe(2,'Üs farkı olan 13 − 6 − 5 = 2 değerini oran sanmış.','islem'),pe(128,'M’yi yalnız K ile oranlamış: 2¹³ ÷ 2⁶.','bilgi'),pe(256,'M’yi yalnız L ile oranlamış: 2¹³ ÷ 2⁵.','bilgi'),pe(8192,'2¹³ sayısını hesaplayıp oran almamış; M’nin sayısını yazmış.','dikkat'),pe(2048,'K · L çarpımının sayısı olan 2¹¹ değerini yazmış.','dikkat')],
 [A('Sayıları yaz','Sütun yüksekliği 2 tabanındaki logaritmadır; sayı 2 üssü yüksekliktir.','K = 2⁶ · L = 2⁵ · M = 2¹³'),A('Oranı kur','Çarpımın sayısı üslerin toplamıdır.','K × L = 2¹¹'),A('Böl','Aynı tabanda bölüm, üslerin farkıdır.','M ÷ (K × L) = 2¹³⁻¹¹ = 4')],
 tipId='alg2-olcek',tip='Logaritmik ölçek, cetvel ve çubuk',z='orta',alt='Logaritmik Sütun Grafik',kaz='Sütun yüksekliği logaritma olan grafikten gerçek sayıların oranını hesaplar.',kalip='grafik',
 kart='K-ALG2-04 (logaritmik sütun grafik) · yükseklik = log₂(sayı)',
 metin='K, L ve M kültürlerindeki bakteri sayılarının 2 tabanındaki logaritmaları alınarak aşağıdaki sütun grafik çizilmiştir; her sütunun yüksekliği, ilgili kültürdeki bakteri sayısının 2 tabanındaki logaritmasına eşittir.\nBuna göre M kültüründeki bakteri sayısı, K ve L kültürlerindeki bakteri sayılarının çarpımının kaç katıdır?',
 istenen='M’nin sayısının K · L çarpımına oranı.',ip=['Her sütunun yüksekliğini 2’nin kuvveti olarak yaz.'],bilgi=[LOG_OLC],sekil=SK,
 puf='Sütun yüksekliklerini sayılara çevirip istenen oranı kur.')

# ================= 0017 orta · öncüllü, sayı doğrusunda konum =================
px,py,pz=-1.4,0.5,1.5
import itertools as _it
for xa,ya,za in _it.product([-1.95,-1.5,-1.05],[0.05,0.5,0.95],[1.05,1.5,1.95]):
    assert 2**xa<0.5 and 2**(ya+za)>2 and 2**(xa+ya)<1
tf17={1:True,2:True,3:False}
sxs=1.15
o=[f'\\draw[-{{Stealth}},thick] ({-3.5*sxs:.2f},0) -- ({3.5*sxs:.2f},0);']
for v in range(-3,4): o.append(f'\\draw[thick] ({v*sxs:.2f},-0.08) -- ({v*sxs:.2f},0.08); \\node[below=3pt,font=\\small] at ({v*sxs:.2f},0) {{${v}$}};')
for v,nm,c in ((px,'x','mavi'),(py,'y','turu'),(pz,'z','mor')):
    o.append(f'\\fill[{c}] ({v*sxs:.3f},0) circle (0.11); \\node[{c},above=4pt,font=\\large\\bfseries] at ({v*sxs:.3f},0) {{${nm}$}};')
SK=fig('\n'.join(o))
sp=onc('I ve II',tf17,{3:'y > 0 olduğunu görüp x + y toplamının da pozitif olacağını sanmış; oysa x < −1 ve y < 1 olduğundan x + y < 0 ve 2ˣ⁺ʸ < 1’dir.'},{1:'x < −1 iken 2ˣ’in 2⁻¹’den büyük olacağını sanmış; üstel fonksiyonun artan olduğunu hesaba katmamış.',2:'y + z toplamını 1’den küçük olabilir sanmış; oysa y > 0 ve z > 1 olduğundan y + z > 1’dir.'},
 [A('Aralıkları oku','Konumlar tam sayılar arasındaki bölmelerden okunur.','−2 < x < −1 · 0 < y < 1 · 1 < z < 2'),A('I’i sına','Üstel fonksiyon artandır: x < −1 ise 2ˣ < 2⁻¹.','2ˣ < 1/2 → doğru'),A('II’yi sına','y + z > 1 olduğundan 2ʸ⁺ᶻ > 2¹.','2ʸ⁺ᶻ > 2 → doğru'),A('III’ü sına','−2 < x + y < 0 olduğundan 2ˣ⁺ʸ < 1.','2ˣ⁺ʸ > 1 → yanlış')],
 tipId='alg2-esitsizlik',tip='Eşitsizlik, aralık ve sıralama',z='orta',alt='Sayı Doğrusunda Üstel Karşılaştırma',kaz='Sayı doğrusundaki konumlardan aralık bilgisi çıkarıp üstel ifadelerin her zaman doğruluğunu değerlendirir.',kalip='öncüllü',
 kart='K-ALG2-07 (sayı doğrusu, öncüllü) · 2ˣ, 2ʸ⁺ᶻ, 2ˣ⁺ʸ',
 metin='Şekildeki sayı doğrusunda x, y ve z gerçel sayılarının konumları gösterilmiştir.\nI. 2ˣ < 1/2\nII. 2ʸ⁺ᶻ > 2\nIII. 2ˣ⁺ʸ > 1\nifadelerinden hangileri her zaman doğrudur?',
 istenen='Her zaman doğru olan öncüller.',ip=['Her sayının hangi iki tam sayı arasında olduğunu yaz; toplamlar için aralıkları topla.'],bilgi=[UST,ESI],sekil=SK,
 puf='Konumlardan yalnız aralık bilgisi çıkar; ifade bütün aralıkta doğruysa “her zaman doğru”dur.')
S('0017',sp['dogru'],sp['pool'],sp['ad'],**{k:v for k,v in sp.items() if k not in('dogru','pool','ad')})

# ================= 0018 zor · tam kısım toplamı =================
def tk(n):
    k=0
    while 3**(k+1)<=n: k+=1
    return k
tp=sum(tk(n) for n in range(1,81)); assert tp==204
assert math.floor(math.log(81,3)+1e-9)==4 and tk(80)==3
ce=lambda n: 0 if n==1 else math.ceil(round(math.log(n,3),9))
assert sum(ce(n) for n in range(1,81))==280
sin_=lambda n:0 if n<=3 else 1 if n<=9 else 2 if n<=27 else 3
assert sum(sin_(n) for n in range(1,81))==201
assert sum(tk(n) for n in range(1,82))==208 and 54*3==162 and 0+1+2+3==6
S('0018',204,[pe(6,'Yalnız farklı değerleri toplamış: 0 + 1 + 2 + 3.','bilgi'),pe(162,'Yalnız değeri 3 olan 54 sayıyı hesaba katmış: 54 × 3.','dikkat'),pe(201,'Sınır değerlerini bir alt gruba koymuş (3, 9 ve 27’yi bir önceki gruba katmış).','dikkat'),pe(208,'n = 81 sayısını da toplama katmış (n = 1, …, 81).','dikkat'),pe(280,'Tam kısım yerine sayıyı yukarı yuvarlamış (ondalıklı sonuçta bir üst tam sayıyı yazmış).','bilgi')],
 [A('Grupları belirle','[log₃n] = k olması 3ᵏ ≤ n < 3ᵏ⁺¹ demektir.','k = 0: n = 1, 2 · k = 1: n = 3, …, 8 · k = 2: n = 9, …, 26 · k = 3: n = 27, …, 80'),A('Eleman sayılarını say','Her grup aralığındaki sayılar sayılır.','2 · 6 · 18 · 54'),A('Toplamı hesapla','Her grubun değeri eleman sayısıyla çarpılır.','0 + 6 + 36 + 162 = 204')],
 tipId='alg2-ondalik',tip='Ondalık logaritma, basamak sayısı ve tam kısım',z='zor',alt='Tam Kısım Toplamı',kaz='Logaritma değerlerinin tam kısımlarının toplamını sayıları aralıklara ayırarak hesaplar.',kalip='yeni nesil',
 kart='K-ALG2-01 (tam kısım toplamı) · [log₃n], n = 1, …, 80',
 metin='Bir hesap makinesi, bir n pozitif tam sayısı için log₃n değerini hesapladığında sonuç tam sayı değilse yalnız tam kısmını, tam sayı ise o sayıyı ekranda göstermektedir.\nn sırasıyla 1, 2, 3, …, 80 değerlerini aldığında ekranda görülen sayıların toplamı kaçtır?',
 istenen='Ekranda görülen sayıların toplamı.',ip=['Ekranda görülen değerin n ile nasıl değiştiğini küçük n değerleriyle incele.'],bilgi=[TAM,TAN],
 puf='Tam kısmı aynı kalan n aralıklarını bul.')

# ================= 0019 orta · çeyrek daire yayı =================
cnt=[x for x in range(1,200) if 1<=lg(x,2)<=3+1e-12]; assert cnt==list(range(2,9)) and len(cnt)==7
assert (len([x for x in range(2,8)]),len(range(1,9)),3,len([x for x in range(1,33) if 1<=lg(x,2)<=5+1e-12]))==(6,8,3,31)
uu=0.78
o=[f'\\fill[mavi!10] (0,0) rectangle ({5*uu:.2f},{3*uu:.2f}); \\draw[thick] (0,0) rectangle ({5*uu:.2f},{3*uu:.2f});',
 f'\\fill[turu!22] (0,0) -- ({1.9*uu:.2f},0) arc (0:90:{1.9*uu:.2f}) -- cycle; \\draw[turu,thick] ({1.9*uu:.2f},0) arc (0:90:{1.9*uu:.2f});',
 f'\\draw[thick,turu] (0,0) -- ({1.9*uu*math.cos(math.radians(35)):.3f},{1.9*uu*math.sin(math.radians(35)):.3f}); \\node[turu,font=\\small\\bfseries,fill=white,inner sep=1.5pt] at ({1.05*uu*math.cos(math.radians(35)):.3f},{1.05*uu*math.sin(math.radians(35)):.3f}) {{$\\log_2 x$}};',
 f'\\node[below left,font=\\small\\bfseries] at (0,0) {{A}}; \\node[below right,font=\\small\\bfseries] at ({5*uu:.2f},0) {{B}}; \\node[above right,font=\\small\\bfseries] at ({5*uu:.2f},{3*uu:.2f}) {{C}}; \\node[above left,font=\\small\\bfseries] at (0,{3*uu:.2f}) {{D}};',
 f'\\node[below=2pt,font=\\small] at ({2.5*uu:.2f},0) {{$\\log_2 32$}}; \\node[right=2pt,font=\\small] at ({5*uu:.2f},{1.5*uu:.2f}) {{$2\\cdot\\log_4 8$}};']
SK=fig('\n'.join(o))
S('0019',7,[pe(3,'Yalnız log₂x değerlerini (1, 2, 3) saymış.','bilgi'),pe(6,'x = 8 değerini sınır dışı bırakmış: 2, …, 7.','dikkat'),pe(8,'Alt sınırı unutup x = 1’i de katmış: 1, …, 8.','dikkat'),pe(31,'Sınır olarak uzun kenarı alıp log₂x ≤ 5 yazmış: x = 2, …, 32.','islem'),pe(32,'Uzun kenarı sınır alıp alt sınırı da bırakarak x = 1, …, 32 saymış.','islem')],
 [A('Kenarları hesapla','Logaritma değerleri bulunur.','2·log₄8 = 3 ve log₂32 = 5'),A('Koşulu yaz','Yay dikdörtgenin dışına taşmaması için yarıçap kısa kenarı geçmemelidir; ayrıca yarıçap en az 1’dir.','1 ≤ log₂x ≤ 3'),A('x’leri say','Tabanı 2 olan logaritma artandır.','2 ≤ x ≤ 8 → x = 2, 3, …, 8: 7 değer')],
 tipId='alg2-geo',tip='Şekilde üstel ve logaritmik uzunluk',z='orta',alt='Yay ve Dikdörtgen',kaz='Yarıçapı logaritmik ifade olan yayın dikdörtgen içinde kalma koşulundan x’in tam sayı değerlerini sayar.',kalip='şekilli',
 kart='K-ALG2-09 (yay ve dikdörtgen) · log₂x yarıçap, 2·log₄8 ve log₂32 kenar',
 metin='Şekilde kenar uzunlukları verilen ABCD dikdörtgeninin A köşesine pergelin iğnesi batırılmış ve yarıçapı log₂x birim olan çeyrek çember yayı çizilmiştir. Pergelin açıklığı en az 1 birimdir ve çizilen yay dikdörtgenin dışına taşmamaktadır (kenarlara teğet olabilir).\nBuna göre x’in alabileceği kaç tam sayı değeri vardır?',
 istenen='x’in alabileceği tam sayı değerlerinin sayısı.',ip=['Hangi kenarın yarıçapı sınırladığını düşün ve iki yanlı eşitsizliği yaz.'],bilgi=[TAN,ESI],sekil=SK,
 puf='Koşulları iki yanlı eşitsizliğe çevir.')

# ================= 0020 zor · tablo, öncüllü =================
fl=lambda x:math.log2(x+1)
assert (fl(1),fl(3),fl(7))==(1,2,3) and fl(15)==4 and 2**5-1==31
tf20={1:False,2:True,3:True}
SK=tablo_svg(['x','1','3','7'],[['f(x)','1','2','3']])
sp=onc('II ve III',tf20,{1:'f(1) = 1 için 1 + b = 2 yerine b = 2 okuyup a + b = 2 + 2 = 4 bulmuş.'},{2:'f(15) = log₂16 değerini 8 sanmış (16 ÷ 2); bu yüzden II’yi yanlış bulmuş.',3:'Ters fonksiyonu f⁻¹(y) = 2ʸ olarak yazıp 1’i çıkarmayı unutmuş: f⁻¹(5) = 32.'},
 [A('a ve b’yi bul','f(1) = 1 ve f(3) = 2 eşitlikleri üstel biçime çevrilir.','a = 1 + b · a² = 3 + b → a² − a − 2 = 0 → a = 2, b = 1'),A('I’i sına','a + b toplamı hesaplanır.','2 + 1 = 3 → I yanlış'),A('II’yi sına','f(15) = log₂16.','4 → II doğru'),A('III’ü sına','f(x) = 5 ise x + 1 = 2⁵.','f⁻¹(5) = 31 → III doğru')],
 tipId='alg2-ters',tip='Ters fonksiyon ve y = x simetrisi',z='zor',alt='Tablo ve Öncüller',kaz='Tablodan logaritma fonksiyonunun taban ve sabitini bulup ters fonksiyonla ilgili öncülleri değerlendirir.',kalip='öncüllü',
 kart='K-ALG2-02 (tablo, öncüllü) · f(x) = logₐ(x + b)',
 metin='a > 1 ve b birer gerçel sayı olmak üzere f(x) = logₐ(x + b) fonksiyonunun bazı değerleri aşağıdaki tabloda verilmiştir.\nI. a + b = 4\nII. f(15) = 4\nIII. f⁻¹(5) = 31\nifadelerinden hangileri doğrudur?',
 istenen='Doğru olan öncüller.',ip=['Tablodaki iki değeri logaritmanın üstel biçiminde yazıp a ve b için iki denklem kur.'],bilgi=[LOF,TAN],sekil=SK,
 puf='Tablodaki x değerlerine 1 eklenince tabanın kuvvetleri görünür.')
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
SCR='/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/logaiki'
for q_ in P.ANA: q_['kardes']=None
P.yaz(os.path.join(MD,'logaiki-1.json'),os.path.join(SCR,'bos-kardes.json'))
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=UK))['kartlar'].append(c['id'])
json.dump(dict(konu=P.konu_adi,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 AYT Matematik çıkmış soruları ve yayın soru bankaları (yalnız mantık), MEB 11–12. sınıf müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),open(os.path.join(HV,'kartlar','logaiki.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
