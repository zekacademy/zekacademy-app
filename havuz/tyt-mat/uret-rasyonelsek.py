"""Rasyonel Sayılar · ŞEKİLLİ paket (14 soru): şekil/tablo çözüm verisini taşır; sayılar Fraction değerlerinden üretilir. Kardeş yok, ipucu 1."""
import sys,os,math
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
from math import cos,sin,radians
H.KONU='Rasyonel Sayılar'
P=Parti('rasyonelsek','Rasyonel Sayılar','mat|Rasyonel Sayılar')
KY='ÖSYM 2018–2026 (kesir, sayı doğrusu, ölçek okuma soruları; yalnız mantık) · MEB 6–8. sınıf'
def fs(x):
    x=Fr(x); s='−' if x<0 else ''; x=abs(x)
    return s+(str(x.numerator) if x.denominator==1 else f'{x.numerator}/{x.denominator}')
def mkf(P,no,dogru,yan,**k):
    vals=[dogru]+[y[0] for y in yan]
    if any(isinstance(v,str) for v in vals): return mk(P,no,dogru=dogru,yan=yan,**k)
    try:
        for v in vals: fm(v)
        mk(P,no,dogru=dogru,yan=yan,**k)
    except AssertionError as e:
        if 'ondalik' not in str(e): raise
        sira=[fs(v) for v in sorted(set(Fr(v) for v in vals))]
        mk(P,no,dogru=fs(dogru),yan=[(fs(y[0]),y[1],y[2]) for y in yan],sira=sira,**k)
def q(no,ad,**k): mkf(P,no,ad=ad,adim=len(ad),**k)
def tf(x):
    x=Fr(x); s='-' if x<0 else ''
    return s+(str(abs(x.numerator)) if x.denominator==1 else r'\dfrac{%d}{%d}'%(abs(x.numerator),x.denominator))
def dc(x):  # TikZ ondalık virgül
    return fm(x).replace(',','{,}')
def fig(body): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'+body+'\n\\end{tikzpicture}')
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)

SD=B('Sayı doğrusunda eşit aralık','iki nokta arası n eş parçaya bölünürse bir parça (fark) ÷ n olur. Örnek: 1/2 ile 3/2 arası 4 eş parça → parça 1/4')
KOL=B('Kesir ve alan','bir bütün n eş parçaya bölünüp k parçası alınırsa kesir k/n’dir; alanı bulmak için kesir bütünün alanıyla çarpılır. Örnek: 40 cm²’nin 3/8’i = 15 cm²')
GEN=B('Kesirlerle toplama ve çıkarma','paydalar eşitlenir, yalnız paylar işlem görür. Örnek: 5/12 + 3/8 = 10/24 + 9/24 = 19/24')
KES=B('Kesirleri karşılaştırma','paydalar eşitlenir ya da ondalığa çevrilir. Örnek: 3/5 = 0,6 ; 5/8 = 0,625 → 3/5 < 5/8')
GOS=B('Gösterge okuma','göstergenin tam dolu değeri kapasiteyi, ibrenin bölme sayısı da dolu kesri verir. Örnek: 12 bölmeli göstergede 5. çizgi 5/12’dir')
ONK=B('Ondalık sayı doğrusu','0,1’lik bölmelerde her çizgi bir önceki çizgiden 0,1 fazladır. Örnek: 1 ile 2 arasında 4. çizgi 1,4’tür')
TER=B('Terazi','denge halinde iki kefedeki kütleler eşittir; özdeş cisimler aynı kütleye sahiptir. Örnek: 2k = 3/2 kg → k = 3/4 kg')

# ---------- kartlar ----------
kartla('K-RSS-01','Sayı doğrusunda eşit aralıklı noktalar','İki uç nokta arası parça sayısı şekilden sayılır; parça uzunluğu (fark ÷ parça sayısı) bulunup istenen noktaya başlangıçtan eklenir.','Nokta sayısını parça sayısı sanmak; 0’dan saymak; yanlış uçtan saymak.','kolay','şekilli',3,'rss-dogru','Sayı doğrusunda iki kesir arasında eşit aralıklar')
kartla('K-RSS-02','Boyalı kesir modeli (dikdörtgen)','Her şekilde boyalı parça sayısı toplam parça sayısına bölünür; paydalar eşitlenip toplanır.','Payları ve paydaları ayrı toplamak; iki şekli farklı büyüklükte sanmak.','kolay','şekilli',3,'rss-boyali','Boyalı kesir modelleri')
kartla('K-RSS-03','Kesir şeritlerini sıralama','Her şeridin boyalı kesri okunur; ondalığa ya da ortak paydaya çevrilerek sıralanır.','Payı büyük kesri büyük saymak; boyasız parça sayısıyla karar vermek.','kolay','şekilli',3,'rss-serit','Kesir şeritleri')
kartla('K-RSS-04','Bindirmeli şeritlerin toplam uzunluğu','Şeritlerin uzunlukları toplanır, üst üste gelen (taralı) bölümler bir kez çıkarılır.','Bindirmeyi hiç düşmemek ya da iki kez düşmek; toplamak.','orta','şekilli',3,'rss-cetvel','Kesirli uzunluk ve bindirme')
kartla('K-RSS-05','Dairesel gösterge okuma','Göstergedeki bölme sayısından ibrenin kesri bulunur; kesir kapasiteyle çarpılıp birim tüketimle oranlanır.','Yanlış bölme sayısı; ibrenin yakın etiketine bakmak; boş kısmı dolu sanmak.','orta','şekilli',3,'rss-gosterge','Dairesel gösterge ve kesirli bölmeler')
kartla('K-RSS-06','Daire dilimleri ve alan','Dilim sayısından boyalı/boyasız kesirler bulunup bütünün alanıyla çarpılır; alanlar birleştirilir.','Boyalıyı boyasızla karıştırmak; farklı dilim sayılarını eşit sanmak.','orta','şekilli',4,'rss-boyali','Boyalı kesir modelleri')
kartla('K-RSS-07','İki terazi ve kesirli kütle','Birinci terazideki dengeden özdeş cismin kütlesi, ikincisinden diğer cismin kütlesi bulunur.','Kütleyi iki kefenin toplamına bölmek; kefeleri karıştırmak.','orta','şekilli',4,'rss-terazi','Terazi ve kesirli kütleler')
kartla('K-RSS-08','Tarif tablosu ve kesirli miktarlar','Tablodaki kesirli miktar bölünerek kaç kez yetişeceği, sonra başka malzemenin gereksinimi bulunur.','Bölme yerine çarpmak; yanlış satırı kullanmak.','orta','tablo',3,'rss-tablo','Ölçü tablosu ve kesirli miktarlar')
kartla('K-RSS-09','Ondalık sayı doğrusunda okuma','0,1’lik bölmeler sayılarak noktaların değerleri okunur, sonra işlem yapılır.','Çizgiyi bir eksik ya da fazla saymak; 0,5 çizgisini 1 sanmak.','orta','şekilli',4,'rss-ondalikdogru','Ondalık sayı doğrusu')
kartla('K-RSS-10','Ölçü kabında sıvı seviyesi','Bölme sayısından sıvı hacmi bulunur; dökme ve ekleme kesirle hesaplanır.','Kalanı dökülen sanmak; bölme değerini yanlış bulmak.','orta','şekilli',4,'rss-olcukabi','Ölçü kabı ve sıvı seviyesi')
kartla('K-RSS-11','Şeritlerde ortak boyalı bölge','Her şeritte boyalı aralığın başlangıç ve bitişi kesir olarak okunur; üç aralığın ortak kısmı, en büyük başlangıç ile en küçük bitiş arasıdır.','Boyalı bölgelerin birleşimini almak; şeritlerin hangi uçtan boyandığını karıştırmak.','zor','şekilli',5,'rss-serit','Kesir şeritleri')
kartla('K-RSS-12','Devirli ondalık sayılarla oran','Tablodaki devirli ondalık sayılar kesre çevrilir (0,(a) = a/9; 0,a(b) = (ab − a)/90); toplanıp oranlanır.','Devirli sayıyı sonlu ondalık gibi almak; 90 yerine 99 kullanmak.','zor','tablo',4,'rss-devirli','Devirli ondalık sayılarla işlem tablosu')
kartla('K-RSS-13','Kutulara kesir yerleştirme (işlem zinciri)','Sondan başa doğru her işlemin tersi sırayla uygulanır.','Tersini almamak; işlem sırasını karıştırmak; toplama/çıkarmayı tersine çevirmemek.','zor','şekilli',4,'rss-zincir','Kutulara kesir yerleştirme (işlem zinciri)')
kartla('K-RSS-14','Önce–sonra göstergesi ve ek doldurma','İki göstergeden hacimler bulunur; ek doldurma da kesirle eklenip tüketim hesaplanır.','Eklemeyi atlamak ya da çıkarmak; kesri yanlış bütüne uygulamak.','zor','şekilli',5,'rss-gosterge','Dairesel gösterge ve kesirli bölmeler')

# ---------- şekil yardımcıları ----------
def grid(cx,cols,rows,sh,w=3.2,h=2.4,cap=''):
    o=[]; cw,ch=w/cols,h/rows
    for i in range(cols*rows):
        r,c=divmod(i,cols)
        if i<sh: o.append(f'\\fill[fill=vurgu!30] ({cx+c*cw:.3f},{-r*ch:.3f}) rectangle ({cx+(c+1)*cw:.3f},{-(r+1)*ch:.3f});')
    for c in range(cols+1): o.append(f'\\draw[thin] ({cx+c*cw:.3f},0) -- ({cx+c*cw:.3f},{-h});')
    for r in range(rows+1): o.append(f'\\draw[thin] ({cx},{-r*ch:.3f}) -- ({cx+w},{-r*ch:.3f});')
    o.append(f'\\draw[thick] ({cx},0) rectangle ({cx+w},{-h});')
    o.append(f'\\node at ({cx+w/2},{-h-0.35}) {{{cap}}};')
    return '\n'.join(o)
def pie(cx,cy,n,k,r=1.25,cap=''):
    o=[]
    for i in range(n):
        a1=90-i*360/n; a2=a1-360/n
        if i<k: o.append(f'\\fill[fill=vurgu!30] ({cx},{cy}) -- ({cx+r*cos(radians(a1)):.3f},{cy+r*sin(radians(a1)):.3f}) arc[start angle={a1:.2f},end angle={a2:.2f},radius={r}] -- cycle;')
    for i in range(n):
        a=radians(90-i*360/n); o.append(f'\\draw[thin] ({cx},{cy}) -- ({cx+r*cos(a):.3f},{cy+r*sin(a):.3f});')
    o.append(f'\\draw[thick] ({cx},{cy}) circle ({r});'); o.append(f'\\node at ({cx},{cy-r-0.35}) {{{cap}}};')
    return '\n'.join(o)
def gauge(cx,cy,n,f,R=1.8,cap=''):
    o=[f'\\draw[thick] ({cx-R},{cy}) arc[start angle=180,end angle=0,radius={R}];',f'\\draw[thin] ({cx-R},{cy}) -- ({cx+R},{cy});']
    for i in range(n+1):
        th=radians(180-180*i/n); major=(i*4%n==0); r1=R-(0.34 if major else 0.17)
        o.append(f'\\draw[{"thick" if major else "thin"}] ({cx+r1*cos(th):.3f},{cy+r1*sin(th):.3f}) -- ({cx+R*cos(th):.3f},{cy+R*sin(th):.3f});')
        if major:
            lab={0:'0',n:'1'}.get(i) or '$'+tf(Fr(i,n))+'$'
            o.append(f'\\node at ({cx+(R+0.36)*cos(th):.3f},{cy+(R+0.36)*sin(th):.3f}) {{{lab}}};')
    th=radians(180-180*float(f)); o.append(f'\\draw[line width=1.5pt] ({cx},{cy}) -- ({cx+(R-0.4)*cos(th):.3f},{cy+(R-0.4)*sin(th):.3f});')
    o.append(f'\\fill ({cx},{cy}) circle (0.09);')
    if cap: o.append(f'\\node at ({cx},{cy-0.5}) {{{cap}}};')
    return '\n'.join(o)
def kap(cx,n,lvl,top,w=1.1,dh=0.5,cap=''):
    H_=n*dh; o=[f'\\fill[fill=vurgu!15] ({cx-w/2},0) rectangle ({cx+w/2},{lvl*dh});',f'\\draw[thick] ({cx-w/2},{H_}) -- ({cx-w/2},0) -- ({cx+w/2},0) -- ({cx+w/2},{H_});']
    if lvl>0: o.append(f'\\draw[line width=1.2pt] ({cx-w/2},{lvl*dh}) -- ({cx+w/2},{lvl*dh});')
    for i in range(1,n+1): o.append(f'\\draw[thin] ({cx+w/2-0.28},{i*dh}) -- ({cx+w/2},{i*dh});')
    o.append(f'\\node[right] at ({cx+w/2+0.05},{H_}) {{{top}}};'); o.append(f'\\node[right] at ({cx+w/2+0.05},0) {{0}};')
    if cap: o.append(f'\\node at ({cx},-0.4) {{{cap}}};')
    return '\n'.join(o)
def balance(cx,oy,left,right,cap=''):
    yb=4.6; yp=1.9; bh=2.2; ph=2.0; o=[f'\\begin{{scope}}[shift={{(0,{-oy})}}]']
    o.append(f'\\draw[thick] ({cx-bh},{yb}) -- ({cx+bh},{yb});'); o.append(f'\\draw[thick] ({cx},{yb}) -- ({cx},0.2);'); o.append(f'\\draw[thick] ({cx-1.0},0.2) -- ({cx+1.0},0.2);'); o.append(f'\\fill ({cx},{yb}) circle (0.09);')
    W={'jar':0.7,'box':0.8,'w':1.2}; G=0.25
    for side,items in ((-1,left),(1,right)):
        x=cx+side*bh
        o.append(f'\\draw[thin] ({x},{yb}) -- ({x-ph},{yp}); \\draw[thin] ({x},{yb}) -- ({x+ph},{yp}); \\draw[thick] ({x-ph},{yp}) -- ({x+ph},{yp});')
        tot=sum(W[i[0]] for i in items)+G*(len(items)-1); px=x-tot/2
        for it in items:
            wd=W[it[0]]; c=px+wd/2
            if it[0]=='jar': o.append(f'\\draw[fill=vurgu!15,thick] ({c-wd/2:.3f},{yp}) rectangle ({c+wd/2:.3f},{yp+0.85}); \\draw[fill=gray!70] ({c-wd/2-0.06:.3f},{yp+0.85}) rectangle ({c+wd/2+0.06:.3f},{yp+1.0});')
            elif it[0]=='box': o.append(f'\\draw[thick,fill=white,pattern=north east lines] ({c-wd/2:.3f},{yp}) rectangle ({c+wd/2:.3f},{yp+0.8});')
            else: o.append(f'\\node[draw,thick,rounded corners=1pt,fill=vurgu!15,inner sep=2pt,anchor=south,minimum width={wd}cm,minimum height=0.75cm,font=\\normalsize] at ({c:.3f},{yp}) {{{it[1]}}};')
            px+=wd+G
    o.append(f'\\node[font=\\Large\\bfseries] at ({cx-3.3},{yb+0.1}) {{{cap}}};'); o.append('\\end{scope}')
    return '\n'.join(o)

# ================= 01 kolay · sayı doğrusu =================
p,qq=Fr(1,3),Fr(3,4); n=5; stp=(qq-p)/n; v=p+3*stp; assert v==Fr(7,12) and p+5*stp==qq
e=[p+3*(qq-p)/4,3*stp,p+3*(qq-p)/6,qq-3*stp]; assert e==[Fr(31,48),Fr(1,4),Fr(13,24),Fr(1,2)] and len({v,*e})==5
o=[f'\\draw[-{{Stealth}}] (0,0) -- (10.5,0);']
for i in range(n+1):
    x=0.8+i*1.8; o.append(f'\\draw ({x:.2f},-0.12) -- ({x:.2f},0.12); \\fill ({x:.2f},0) circle (0.06);')
    o.append(f'\\node[above=3pt] at ({x:.2f},0) {{{"A" if i==0 else "B" if i==n else "KLMN"[i-1]}}};')
o.append(f'\\node[below=3pt] at (0.8,0) {{${tf(p)}$}}; \\node[below=3pt] at ({0.8+n*1.8},0) {{${tf(qq)}$}};')
SK=fig('\n'.join(o))
q('0001',tipId='rss-dogru',tip='Sayı doğrusunda iki kesir arasında eşit aralıklar',z='kolay',alt='Sayı Doğrusu',kaz='Sayı doğrusunda iki kesir arasındaki eşit aralıklı noktanın değerini bulur.',kalip='şekilli',
 kart='K-RSS-01 (sayı doğrusu) · 1/3 ile 3/4 arası 5 eş parça',
 metin='Şekildeki sayı doğrusunda A noktası 1/3’ü, B noktası 3/4’ü göstermektedir. A ile B arasındaki K, L, M ve N noktaları, A ve B ile birlikte eşit aralıklarla yerleşmiştir.\nBuna göre M noktası hangi sayıyı göstermektedir?',
 dogru=v,yan=[(e[0],'A ile B arasındaki parça sayısını 4 (nokta sayısı) almış: 1/3 + 3 × (5/12 ÷ 4).','bilgi'),(e[1],'Başlangıç noktasını 0 alıp 3 parça eklemiş: 3 × 1/12.','dikkat'),(e[2],'Parça sayısını 6 almış: 1/3 + 3 × (5/12 ÷ 6).','bilgi'),(e[3],'M’yi B’den 3 parça geri giderek bulmuş: 3/4 − 3 × 1/12.','dikkat')],
 istenen='M noktasının gösterdiği sayı.',ip=['A’dan B’ye kaç eş parça olduğunu şekilden say; bir parçanın değerini bul.'],bilgi=[SD],sekil=SK,
 ad=[A('Aralığı ölç','İki uç arasındaki fark bulunur.','3/4 − 1/3 = 9/12 − 4/12 = 5/12'),A('Bir parçayı bul','Şekilde A ile B arasında 5 eş parça vardır.','(5/12) ÷ 5 = 1/12'),A('M’ye ulaş','M, A’dan sonra 3. noktadır.','1/3 + 3 × 1/12 = 4/12 + 3/12 = 7/12')],
 puf='Parça sayısı nokta sayısından bir fazladır: uçlar dahil 6 nokta 5 parça demektir.')

# ================= 02 kolay · boyalı dikdörtgenler =================
a1,a2=Fr(5,12),Fr(3,8); v=a1+a2; assert v==Fr(19,24)
e=[Fr(5+3,12+8),a1-a2,v/2,Fr(5+3,12)]; assert e==[Fr(2,5),Fr(1,24),Fr(19,48),Fr(2,3)] and len({v,*e})==5
SK=fig(grid(0,4,3,5,cap='I')+'\n'+grid(4.2,4,2,3,cap='II'))
q('0002',tipId='rss-boyali',tip='Boyalı kesir modelleri',z='kolay',alt='Boyalı Modeller',kaz='İki şekilde boyalı kesirleri okuyup toplar.',kalip='şekilli',
 kart='K-RSS-02 (boyalı model) · iki özdeş dikdörtgen, 5/12 + 3/8',
 metin='Şekilde, birbirinin aynısı olan I ve II numaralı iki dikdörtgenin her biri eş bölgelere ayrılmış ve bazı bölgeler boyanmıştır.\nBuna göre, boyalı bölgelerin alanları toplamı, dikdörtgenlerden birinin alanının kaçta kaçıdır?',
 dogru=v,yan=[(e[0],'Payları ve paydaları ayrı ayrı toplamış: (5 + 3)/(12 + 8).','bilgi'),(e[1],'İki kesri toplamak yerine çıkarmış: 5/12 − 3/8.','dikkat'),(e[2],'İki dikdörtgenin toplam alanına oranlamış: (19/24) ÷ 2.','dikkat'),(e[3],'II’nin payını I’in paydasına yazmış: (5 + 3)/12.','islem')],
 istenen='Boyalı alanlar toplamının bir dikdörtgene oranı.',ip=['Önce her şekilde boyalı bölge sayısını toplam bölge sayısına oranla.'],bilgi=[GEN],sekil=SK,
 ad=[A('Kesirleri oku','I’de 12 bölgenin 5’i, II’de 8 bölgenin 3’ü boyalıdır.','5/12 ve 3/8'),A('Paydaları eşitle','12 ve 8’in ortak katı 24’tür.','5/12 = 10/24 · 3/8 = 9/24'),A('Topla','Dikdörtgenler özdeş olduğundan kesirler doğrudan toplanır.','10/24 + 9/24 = 19/24')],
 puf='Şekiller özdeşse boyalı kesirler aynı bütünün parçalarıdır; doğrudan toplanabilir.')

# ================= 03 kolay · kesir şeritleri =================
S={'K':(5,3),'L':(3,2),'M':(8,5),'N':(12,7)}; val={k:Fr(b,a) for k,(a,b) in S.items()}
order=lambda key,rev=False:' < '.join(sorted(S,key=key,reverse=rev))
dog=order(lambda k:val[k]); assert dog=='N < K < M < L'
e1=order(lambda k:(S[k][1],S[k][0])); e2=order(lambda k:-(S[k][0]-S[k][1])); e3=order(lambda k:val[k],True); e4='N < K < L < M'
assert e1=='L < K < M < N' and e2=='N < M < K < L' and e3=='L < M < K < N' and len({dog,e1,e2,e3,e4})==5
o=[]
for i,(k,(m,b)) in enumerate(S.items()):
    y=-i*0.95; cw=8/m
    o.append(f'\\fill[fill=vurgu!30] (0,{y}) rectangle ({cw*b},{y-0.6});')
    for j in range(m+1): o.append(f'\\draw[thin] ({cw*j:.3f},{y}) -- ({cw*j:.3f},{y-0.6});')
    o.append(f'\\draw[thick] (0,{y}) rectangle (8,{y-0.6}); \\node[left] at (-0.15,{y-0.3}) {{{k}}};')
SK=fig('\n'.join(o))
q('0003',tipId='rss-serit',tip='Kesir şeritleri',z='kolay',alt='Kesir Şeritleri',kaz='Eş şeritlerde boyalı kesirleri okuyup küçükten büyüğe sıralar.',kalip='şekilli',
 kart='K-RSS-03 (kesir şeridi) · 3/5, 2/3, 5/8, 7/12 sıralama',
 metin='Şekildeki K, L, M ve N şeritleri aynı uzunluktadır; her biri eş parçalara ayrılmış ve bir kısmı boyanmıştır.\nBuna göre, şeritlerin boyalı kesirlerinin küçükten büyüğe doğru sıralanışı aşağıdakilerden hangisidir?',
 dogru=dog,yan=[(e1,'Boyalı parça sayısı (payı) büyük olan şeridi büyük saymış.','bilgi'),(e2,'Boyasız parça sayısı fazla olan şeridi küçük saymış (5, 3, 2, 1).','islem'),(e3,'Sıralamayı büyükten küçüğe yapmış.','dikkat'),(e4,'2/3 ile 5/8’i karşılaştırırken yanlış yorumlayıp 5/8’i büyük bulmuş.','islem')],
 sira=[dog,e1,e2,e3,e4],istenen='Boyalı kesirlerin küçükten büyüğe sıralanışı.',ip=['Her şeridin boyalı kısmını kesir olarak yaz ve ortak paydaya ya da ondalığa çevir.'],bilgi=[KES],sekil=SK,
 ad=[A('Kesirleri oku','Boyalı parça / toplam parça.','K = 3/5 · L = 2/3 · M = 5/8 · N = 7/12'),A('Ondalığa çevir','Pay ÷ payda.','K = 0,6 · L ≈ 0,667 · M = 0,625 · N ≈ 0,583'),A('Sırala','Küçükten büyüğe diz.','N < K < M < L')],
 puf='Parça büyüklükleri farklıysa pay ya da boyasız parça sayısına bakmak yetmez; kesirleri ortak paydaya getir.')

# ================= 04 orta · bindirmeli şeritler =================
Ls=[Fr(5,6),Fr(3,4),Fr(2,3)]; Ov=[Fr(1,4),Fr(1,6)]; v=sum(Ls)-sum(Ov); assert v==Fr(11,6)
e=[sum(Ls),sum(Ls)-Ov[0],sum(Ls)+sum(Ov),sum(Ls)-2*sum(Ov)]; assert e==[Fr(9,4),2,Fr(8,3),Fr(17,12)] and len({v,*e})==5
U=6.0; st=[0.0]
for i in (1,2): st.append(st[-1]+float(Ls[i-1])*U-float(Ov[i-1])*U)
o=[]
for i in range(3):
    y=-i*2.1; x1=st[i]; x2=x1+float(Ls[i])*U; hh=0.8
    o.append(f'\\draw[thick] ({x1:.3f},{y}) rectangle ({x2:.3f},{y-hh});')
    if i>0: o.append(f'\\fill[gray!35] ({x1:.3f},{y}) rectangle ({x1+float(Ov[i-1])*U:.3f},{y-hh}); \\draw[thick] ({x1:.3f},{y}) rectangle ({x1+float(Ov[i-1])*U:.3f},{y-hh});')
    if i<2:
        xo=x2-float(Ov[i])*U
        o.append(f'\\fill[gray!35] ({xo:.3f},{y}) rectangle ({x2:.3f},{y-hh}); \\draw[thick] ({xo:.3f},{y}) rectangle ({x2:.3f},{y-hh}); \\node at ({(xo+x2)/2:.3f},{y-hh/2}) {{${tf(Ov[i])}$}};')
    o.append(f'\\draw[<->,thin] ({x1:.3f},{y+0.3}) -- ({x2:.3f},{y+0.3}); \\node[above] at ({(x1+x2)/2:.3f},{y+0.3}) {{${tf(Ls[i])}$ m}};')
SK=fig('\n'.join(o))
q('0004',tipId='rss-cetvel',tip='Kesirli uzunluk ve bindirme',z='orta',alt='Kesirli Uzunluk',kaz='Üst üste bindirilmiş şeritlerin toplam uzunluğunu kesirlerle bulur.',kalip='şekilli',
 kart='K-RSS-04 (şerit/bindirme) · 5/6, 3/4, 2/3 m şerit, 1/4 ve 1/6 m bindirme (veri yalnız şekilde)',
 metin='Şekilde, uzunlukları ok işaretleriyle metre cinsinden verilen üç şerit, komşu şeritlerin uçları üst üste gelecek biçimde yapıştırılmıştır. Üst üste gelen (gri) bölümlerin uzunlukları da şekilde metre cinsinden yazılıdır.\nBuna göre, yapıştırılmış şeridin toplam uzunluğu kaç metredir?',
 dogru=v,yan=[(e[0],'Bindirme bölümlerini hiç düşmemiş: 5/6 + 3/4 + 2/3.','dikkat'),(e[1],'Yalnız ilk bindirmeyi (1/4) düşmüş.','dikkat'),(e[2],'Bindirme uzunluklarını toplama eklemiş.','islem'),(e[3],'Bindirmeleri iki kez düşmüş: toplamdan 2 × (1/4 + 1/6) çıkarmış.','bilgi')],
 istenen='Yapıştırılmış şeridin toplam uzunluğu (m).',ip=['Gri bölümlerin hangi şeritlere ait olduğuna şekilde dikkat et.'],bilgi=[GEN],sekil=SK,
 ad=[A('Uzunlukları topla','Üç şeridin uzunlukları paydası 12 olacak biçimde toplanır.','10/12 + 9/12 + 8/12 = 27/12 = 9/4'),A('Bindirmeleri topla','Her gri bölüm iki şeritte sayıldığı için bir kez fazladır.','1/4 + 1/6 = 5/12'),A('Fazlayı çıkar','Toplam uzunluk bu farktır.','27/12 − 5/12 = 22/12 = 11/6 m')],
 puf='Üst üste binen bölüm toplamda iki kez sayılır; bir kez çıkarmak gerekir.')

# ================= 05 orta · gösterge (şarj) =================
f=Fr(5,12); kap_=72; v=f*kap_*Fr(100,12); assert v==250
e=[Fr(5,10)*kap_*Fr(100,12),Fr(7,12)*kap_*Fr(100,12),Fr(1,4)*kap_*Fr(100,12),Fr(5,16)*kap_*Fr(100,12)]
e=[e[0],e[1],e[2],e[3]]; assert e==[300,350,150,Fr(375,2)] and len({v,*e})==5
SK=fig(gauge(0,0,12,f,cap='Batarya göstergesi'))
q('0005',tipId='rss-gosterge',tip='Dairesel gösterge ve kesirli bölmeler',z='orta',alt='Gösterge Okuma',kaz='Dairesel göstergeden dolu kesri okuyup menzili hesaplar.',kalip='şekilli',
 kart='K-RSS-05 (gösterge) · 12 bölmeli batarya göstergesi, ibre 5/12',
 metin='Bir elektrikli aracın bataryası tam doluyken 72 kWh enerji depolamaktadır. Bataryanın göstergesi, boş (0) ile dolu (1) arasında eş bölmelere ayrılmıştır ve ibre şekildeki gibidir. Araç sabit tüketimle her 100 km’de 12 kWh enerji harcamaktadır.\nBuna göre, araç bataryadaki enerjiyle en çok kaç km yol alabilir?',
 dogru=v,yan=[(e[0],'İbreyi en yakın etiketli çizgi olan 1/2’de sanmış: 1/2 × 72 = 36 kWh → 300 km.','dikkat'),(e[1],'Dolu kısım yerine boş kısmı (7/12) okumuş.','dikkat'),(e[2],'İbreyi alttaki etiketli çizgi olan 1/4’te sanmış: 1/4 × 72 = 18 kWh → 150 km.','dikkat'),(e[3],'Göstergeyi 16 bölmeli sanıp 5/16 okumuş.','bilgi')],
 istenen='Aracın alabileceği en çok yol (km).',ip=['Göstergedeki eş bölme sayısını say; ibre kaçıncı çizgide?'],bilgi=[GOS],sekil=SK,
 ad=[A('Göstergeyi oku','Gösterge 12 eş bölmelidir; ibre 5. çizgidedir.','dolu kesri = 5/12'),A('Enerjiyi bul','Kesir kapasiteyle çarpılır.','5/12 × 72 = 30 kWh'),A('Yolu bul','Her 12 kWh için 100 km gidilir.','(30 ÷ 12) × 100 = 250 km')],
 puf='Etiketli çizgiler arasındaki küçük bölmeleri say; her bölme göstergenin eşit bir kesridir.')

# ================= 06 orta · daire dilimleri =================
alan=48; A_=Fr(5,8); B_=Fr(7,12); v=A_*alan+(1-B_)*alan; assert v==50
e=[(1-A_)*alan+(1-B_)*alan,(1-B_)*alan,(1-A_)*alan+B_*alan,A_*alan+B_*alan]; assert e==[38,20,46,58] and len({v,*e})==5
SK=fig(pie(0,0,8,5,cap='A')+'\n'+pie(3.6,0,12,7,cap='B'))
q('0006',tipId='rss-boyali',tip='Boyalı kesir modelleri',z='orta',alt='Daire Dilimleri',kaz='Daire dilimlerindeki boyalı ve boyasız kesirleri alana çevirip birleştirir.',kalip='şekilli',
 kart='K-RSS-06 (daire dilimi) · A: 5/8, B: 7/12, alan 48',
 metin='Şekildeki A ve B daireleri özdeştir ve her birinin alanı 48 cm²’dir. Dairelerin her biri eş dilimlere ayrılmış ve bazı dilimler boyanmıştır.\nBuna göre, A dairesinin boyalı bölgesi ile B dairesinin boyasız bölgesinin alanları toplamı kaç cm²’dir?',
 dogru=v,yan=[(e[0],'A’nın boyasız (18) ile B’nin boyasız (20) alanını toplamış.','dikkat'),(e[1],'Yalnız B’nin boyasız alanını (20) vermiş.','dikkat'),(e[2],'A’nın boyasız (18) ile B’nin boyalı (28) alanını toplamış.','dikkat'),(e[3],'A’nın boyalı (30) ile B’nin boyalı (28) alanını toplamış.','dikkat')],
 istenen='A’nın boyalı ile B’nin boyasız alanlarının toplamı (cm²).',ip=['A için boyalı, B için boyasız dilim sayısını ayrı ayrı kesre çevir.'],bilgi=[KOL],sekil=SK,
 ad=[A('A’nın boyalı kesri','8 dilimin 5’i boyalıdır.','5/8 × 48 = 30 cm²'),A('B’nin boyasız kesri','12 dilimin 7’si boyalı, 5’i boyasızdır.','5/12 × 48 = 20 cm²'),A('Topla','İki alan toplanır.','30 + 20 = 50 cm²')],
 puf='Önce hangi bölgenin (boyalı/boyasız) istendiğini işaretle; sonra her daire için kesri ayrı ayrı yaz.')

# ================= 07 orta · iki terazi =================
w1,w2=Fr(3,2),Fr(1,4); kav=(w1+w2)/2; kut=3-kav; v=2*kut; assert kav==Fr(7,8) and v==Fr(17,4)
e=[2*(3-(w1+w2)),kut,2*(3+kav),2*(3-(w1-w2)/2)]
assert (w1-w2)/2==Fr(5,8) and e==[Fr(5,2),Fr(17,8),Fr(31,4),Fr(19,4)] and len({v,*e})==5
SK=fig(balance(0,0,[('jar',),('jar',)],[('w','$'+tf(w1)+'$ kg'),('w','$'+tf(w2)+'$ kg')],cap='I')+'\n'+balance(0,6.3,[('jar',),('box',)],[('w','$3$ kg')],cap='II'))
q('0007',tipId='rss-terazi',tip='Terazi ve kesirli kütleler',z='orta',alt='Terazi',kaz='İki dengedeki teraziden bilinmeyen kütleleri sırayla bulur.',kalip='şekilli',
 kart='K-RSS-07 (terazi) · 2 kavanoz = 3/2 + 1/4 kg ; kavanoz + kutu = 3 kg',
 metin='Şekildeki I ve II numaralı teraziler dengededir. Kapaklı kaplar kavanozu, taralı kare kutuyu göstermektedir; tüm kavanozlar birbirinin, tüm kutular da birbirinin aynısıdır.\nBuna göre, 2 kutunun kütlesi toplam kaç kilogramdır?',
 dogru=v,yan=[(e[0],'Kavanozun kütlesini 3/2 + 1/4 = 7/4 kg almış (2’ye bölmemiş); kutu 5/4 kg, 2 kutu 5/2 kg.','dikkat'),(e[1],'Bir kutunun kütlesini (17/8 kg) vermiş; 2 kutu istenmiş.','dikkat'),(e[2],'II’de kavanozun kütlesini 3 kg’a ekleyerek kutuyu 3 + 7/8 = 31/8 kg bulmuş; 2 kutu 31/4 kg.','islem'),(e[3],'Birinci teraziden kavanozu (3/2 − 1/4) ÷ 2 = 5/8 kg bulmuş (kütleleri çıkarmış); kutu 3 − 5/8 = 19/8, 2 kutu 19/4 kg.','bilgi')],
 istenen='2 kutunun toplam kütlesi (kg).',ip=['Kavanozun kütlesi hangi terazinin dengesinden tek başına bulunabilir?'],bilgi=[TER],sekil=SK,
 ad=[A('Kavanozu bul','I’de 2 kavanoz, sağ kefedeki kütlelere eşittir.','2k = 3/2 + 1/4 = 7/4 → k = 7/8 kg'),A('Kutuyu bul','II’de kavanoz + kutu = 3 kg.','kutu = 3 − 7/8 = 17/8 kg'),A('İki kutu','Bulunan kütle 2 ile çarpılır.','2 × 17/8 = 17/4 kg')],
 puf='Önce yalnız bir cins cisim içeren dengeyi çöz; bulduğun kütleyi diğer dengede yerine koy.')

# ================= 08 orta · tablo =================
torf,perlit,komp=Fr(3,4),Fr(1,6),Fr(1,3); N=Fr(9)/torf; v=N*perlit; assert N==12 and v==2
e=[N*komp,N,Fr(9)*torf,Fr(9)/perlit]; assert e==[4,12,Fr(27,4),54] and len({v,*e})==5
SK=tablo_svg(['Malzeme','1 saksı için (litre)'],[['Torf','3/4'],['Perlit','1/6'],['Kompost','1/3']])
q('0008',tipId='rss-tablo',tip='Ölçü tablosu ve kesirli miktarlar',z='orta',alt='Ölçü Tablosu',kaz='Tablodaki kesirli miktarlarla kaç saksılık karışım yapılacağını ve gereken perliti bulur.',kalip='tablo',
 kart='K-RSS-08 (tablo) · torf 3/4, perlit 1/6, kompost 1/3 L; 9 L torf',
 metin='Bir bahçıvan, 1 saksı için gereken miktarları aşağıdaki tabloda verilen toprak karışımını hazırlayacaktır. Bahçıvanın elinde 9 litre torf vardır; perlit ve kompost yeterince bulunmaktadır.\nBahçıvan torfun tamamını kullanarak tablodaki miktarlara uygun karışım hazırlarsa kaç litre perlit gerekir?',
 dogru=v,yan=[(e[0],'Perlit yerine kompost satırını kullanmış: 12 × 1/3.','dikkat'),(e[1],'Saksı sayısını (12) perlit miktarı sanmış.','dikkat'),(e[2],'Torfu 3/4 ile çarpıp saksı sayısını 27/4 bulmuş, bunu yazmış.','bilgi'),(e[3],'9 L’yi perlit miktarına bölmüş: 9 ÷ 1/6.','islem')],
 istenen='Gereken perlit miktarı (litre).',ip=['Torfun 9 litresi, saksı başına torf miktarının kaç katıdır?'],bilgi=[B('Kesirle bölme','a ÷ (b/c) = a × c/b. Örnek: 6 ÷ 3/4 = 6 × 4/3 = 8')],sekil=SK,
 ad=[A('Tabloyu oku','Torf satırı saksı başına miktarı verir.','1 saksı: 3/4 L torf · 1/6 L perlit'),A('Saksı sayısını bul','Toplam torf, saksı başına torfa bölünür.','9 ÷ 3/4 = 9 × 4/3 = 12 saksı'),A('Perliti bul','Her saksıya 1/6 L perlit gerekir.','12 × 1/6 = 2 L')],
 puf='“Kaç saksı” sorusu bölmedir; ardından seçilen malzemenin satırını kullan.')

# ================= 09 orta · ondalık sayı doğrusu =================
k_,l_,m_=Fr('0.4'),Fr('1.3'),Fr('1.8'); v=(k_+l_)/m_; assert v==Fr(17,18)
e=[(l_-k_)/m_,m_/(k_+l_),(k_+l_)/Fr('1.7'),(k_+l_)/Fr('1.6')]; assert e==[Fr(1,2),Fr(18,17),1,Fr(17,16)] and len({v,*e})==5
o=['\\draw[-{Stealth}] (-0.3,0) -- (9.3,0);']
for i in range(21):
    x=i*0.45; h=0.2 if i%5==0 else 0.1; o.append(f'\\draw ({x},-{h}) -- ({x},{h});')
for i in (0,5,10,15,20): o.append(f'\\node[below=4pt,font=\\large] at ({i*0.45},0) {{{dc(Fr(i,10))}}};')
for nm,t in (('K',k_),('L',l_),('M',m_)): o.append(f'\\fill ({float(t)*4.5:.3f},0) circle (0.08); \\node[above=4pt,font=\\large] at ({float(t)*4.5:.3f},0) {{{nm}}};')
SK=fig('\n'.join(o))
q('0009',tipId='rss-ondalikdogru',tip='Ondalık sayı doğrusu',z='orta',alt='Ondalık Sayı Doğrusu',kaz='Ondalık sayı doğrusunda noktaların değerlerini okuyup işlem yapar.',kalip='şekilli',
 kart='K-RSS-09 (ondalık doğru) · K = 0,4 ; L = 1,3 ; M = 1,8',
 metin='Şekildeki sayı doğrusunda 0 ile 2 arası 0,1’lik bölmelere ayrılmıştır. K, L ve M noktalarının gösterdiği sayılar sırasıyla k, l ve m’dir.\nBuna göre, (k + l)/m işleminin sonucu kaçtır?',
 dogru=v,yan=[(e[0],'Toplamak yerine l − k almış: 0,9/1,8.','dikkat'),(e[1],'Kesri ters yazmış: m/(k + l).','dikkat'),(e[2],'M’yi 1,7 okumuş (bir çizgi eksik saymış): 1,7/1,7.','islem'),(e[3],'M’yi 1,6 okumuş: 1,7/1,6.','islem')],
 istenen='(k + l)/m değeri.',ip=['0,5 ve 1,5 çizgilerinden başlayarak çizgileri sayıp üç noktanın değerini oku.'],bilgi=[ONK],sekil=SK,
 ad=[A('Noktaları oku','Her çizgi 0,1’dir.','k = 0,4 · l = 1,3 · m = 1,8'),A('Toplamı bul','k ve l toplanır.','0,4 + 1,3 = 1,7'),A('Oranla','Kesir olarak yaz ve sadeleştir.','1,7/1,8 = 17/18')],
 puf='Uzun çizgilerin değerini önce belirle; kısa çizgileri ondan itibaren say.')

# ================= 10 orta · ölçü kabı =================
cap=Fr(2000); lv=cap*Fr(5,8); dok=lv*Fr(3,5); kal=lv-dok; v=cap-kal; assert lv==1250 and dok==750 and kal==500 and v==1500
e=[dok,kal,lv,cap]; assert len({v,*e})==5
SK=fig(kap(0,8,5,'2 L'))
q('0010',tipId='rss-olcukabi',tip='Ölçü kabı ve sıvı seviyesi',z='orta',alt='Ölçü Kabı',kaz='Ölçü kabındaki sıvı seviyesinden hacim bulup döküm ve ekleme hesaplar.',kalip='şekilli',
 kart='K-RSS-10 (ölçü kabı) · 2 L, 8 bölme, seviye 5',
 metin='Şekildeki ölçü kabının kapasitesi 2 litredir ve kap 8 eş bölmeye ayrılmıştır. Kabın içinde şekilde görülen seviyeye kadar su vardır. Kaptaki suyun 3/5’i döküldükten sonra kap ağzına kadar su ile doldurulacaktır. (1 L = 1000 mL)\nBuna göre, kaba kaç mL su eklenmelidir?',
 dogru=v,yan=[(e[0],'Dökülen suyu (750 mL) eklenmesi gereken sanmış.','dikkat'),(e[1],'Kalan suyu (500 mL) eklenmesi gereken sanmış.','dikkat'),(e[2],'Suyun 3/5’ini dökülen değil kalan sanmış: kalan 750 mL, eklenecek 2000 − 750 = 1250 mL.','dikkat'),(e[3],'Kabın kapasitesini (2000 mL) yazmış.','islem')],
 istenen='Eklenecek su miktarı (mL).',ip=['Önce şekildeki seviyeden başlangıçtaki su miktarını mL olarak bul.'],bilgi=[B('Bölme değeri','kapasite ÷ bölme sayısı. Örnek: 2 L ve 8 bölme → 1 bölme 2000 ÷ 8 = 250 mL')],sekil=SK,
 ad=[A('Başlangıç suyu','Bir bölme 2000 ÷ 8 = 250 mL; seviye 5. çizgidir.','5 × 250 = 1250 mL'),A('Dökülen','Suyun 3/5’i dökülür.','1250 × 3/5 = 750 mL'),A('Kalan','Başlangıç sudan dökülen çıkarılır.','1250 − 750 = 500 mL'),A('Eklenecek','Kabı doldurmak için kapasiteden kalan çıkarılır.','2000 − 500 = 1500 mL')],
 puf='Önce kapta kalan suyu bul; kabı doldurmak için eksik kalan hacmi kapasiteden çıkararak bul.')

# ================= 11 zor · üç şeritte ortak bölge =================
def aralik(m,k,son): return (Fr(m-k,m),Fr(1)) if son else (Fr(0),Fr(k,m))
Aa=(Fr(0),Fr(7,8)); Bb=(Fr(1,6),Fr(1)); Cc=(Fr(3,12),Fr(11,12))
def ort(*r): lo=max(x[0] for x in r); hi=min(x[1] for x in r); return max(hi-lo,0)*48
v=ort(Aa,Bb,Cc); assert v==30
e=[ort(Aa,Bb),ort(Bb,Cc),Fr(48),Bb[1]*0+Fr(5,6)*48]   # C yok; A yok; birleşim; B'nin boyalı uzunluğu
assert e==[34,32,48,40] and len({v,*e})==5
rows=[('A',8,0,7),('B',6,1,6),('C',12,3,11)]
o=[]
for i,(nm,m,a,b) in enumerate(rows):
    y=-i*1.0; cw=8/m
    o.append(f'\\fill[fill=vurgu!30] ({cw*a:.3f},{y}) rectangle ({cw*b:.3f},{y-0.6});')
    for j in range(m+1): o.append(f'\\draw[thin] ({cw*j:.3f},{y}) -- ({cw*j:.3f},{y-0.6});')
    o.append(f'\\draw[thick] (0,{y}) rectangle (8,{y-0.6}); \\node[left] at (-0.15,{y-0.3}) {{{nm}}};')
assert (Aa,Bb,Cc)==((Fr(rows[0][2],8),Fr(rows[0][3],8)),(Fr(rows[1][2],6),Fr(rows[1][3],6)),(Fr(rows[2][2],12),Fr(rows[2][3],12)))
SK=fig('\n'.join(o))
q('0011',tipId='rss-serit',tip='Kesir şeritleri',z='zor',alt='Şeritlerde Ortak Bölge',kaz='Üç şeritteki boyalı aralıkların ortak kısmının uzunluğunu kesirle bulur.',kalip='şekilli',
 kart='K-RSS-11 (üç şerit) · [0,7/8] ∩ [1/6,1] ∩ [1/4,11/12] = 5/8 · 48 cm',
 metin='Şekildeki A, B ve C şeritlerinin her biri 48 cm uzunluğundadır; şeritler uçları hizalı biçimde alt alta çizilmiş, eş parçalara ayrılmış ve bir kısmı boyanmıştır.\nBuna göre, üç şeritte de boyalı olan ortak bölgenin uzunluğu kaç cm’dir?',
 dogru=v,yan=[(e[0],'C şeridini hesaba katmamış: yalnız A ve B’nin ortak kısmı (1/6 ile 7/8 arası).','dikkat'),(e[1],'A şeridini hesaba katmamış: B ve C’nin ortak kısmı (1/4 ile 11/12 arası).','dikkat'),(e[2],'Ortak bölge yerine boyalı bölgelerin birleşimini (tüm şerit) almış.','bilgi'),(e[3],'Yalnız B şeridinin boyalı uzunluğunu (5/6 × 48) vermiş.','dikkat')],
 istenen='Ortak boyalı bölgenin uzunluğu (cm).',ip=['Her şeritte boyalı bölgenin sol ve sağ uçlarını şeridin kesri olarak yaz.'],bilgi=[B('Ortak bölge','aralıkların ortak kısmı, en büyük başlangıç ile en küçük bitiş arasındadır. Örnek: [1/5, 3/4] ve [2/5, 5/6] için ortak kısım [2/5, 3/4]')],sekil=SK,
 ad=[A('Aralıkları oku','Boyalı bölgenin uçları şerit uzunluğunun kesri olarak yazılır.','A: [0, 7/8] · B: [1/6, 1] · C: [3/12, 11/12] = [1/4, 11/12]'),A('Ortak başlangıç','En büyük başlangıç alınır.','en büyüğü 1/4 (C)'),A('Ortak bitiş','En küçük bitiş alınır.','en küçüğü 7/8 (A)'),A('Kesri bul','Bitiş ile başlangıç farkı.','7/8 − 1/4 = 5/8'),A('Uzunluğa çevir','Şerit 48 cm’dir.','5/8 × 48 = 30 cm')],
 puf='Boyalı bölgenin başlangıcı ve bitişi ayrı ayrı okunur; üç şeritte birden boyalı olan yerin uçları bunlardan seçilir.')

# ================= 12 zor · devirli ondalık tablosu =================
Kk,Ll,Mm=Fr(1,3),Fr(75,90),Fr(5,3); assert Ll==Fr(5,6) and Fr(83-8,90)==Ll and Fr(16,9)-Fr(1,9)==Mm
v=(Kk+Ll)/Mm; assert v==Fr(7,10)
e=[(Fr(3,10)+Fr('0.83')) /Fr('1.6'),(Fr(3,10)+Ll)/Mm,Mm/(Kk+Ll),(Ll-Kk)/Mm]
assert e==[Fr(113,160),Fr(17,25),Fr(10,7),Fr(3,10)] and len({v,*e})==5
SK=tablo_svg(['Kova','Su miktarı (litre)'],[['K','0,(3)'],['L','0,8(3)'],['M','1,(6)']])
q('0012',tipId='rss-devirli',tip='Devirli ondalık sayılarla işlem tablosu',z='zor',alt='Devirli Ondalık Tablosu',kaz='Tablodaki devirli ondalık sayıları kesre çevirip oranlar.',kalip='tablo',
 kart='K-RSS-12 (devirli tablo) · 0,(3), 0,8(3), 1,(6) → (K+L)/M = 7/10',
 metin='Aşağıdaki tabloda K, L ve M kovalarındaki su miktarları litre cinsinden ondalık gösterimle verilmiştir. (Parantez içindeki rakamlar sonsuza kadar tekrar eder.)\nBuna göre, K ve L kovalarındaki suların toplamı, M kovasındaki suyun kaçta kaçıdır?',
 dogru=v,yan=[(e[0],'Devirli sayıları sonlu ondalık gibi yazmış: (0,3 + 0,83) ÷ 1,6.','islem'),(e[1],'0,(3)’ü 3/10 almış (paydayı 9 yerine 10 yazmış): (3/10 + 5/6) ÷ 5/3.','bilgi'),(e[2],'Oranı ters kurmuş: M ÷ (K + L).','dikkat'),(e[3],'Toplamak yerine L − K almış: (5/6 − 1/3) ÷ 5/3.','dikkat')],
 istenen='(K + L) / M oranı.',ip=['Üç devirli sayıyı da kesre çevir; devir nerede başlıyor?'],bilgi=[B('Devirli ondalık sayı','0,(a) = a/9 · 0,a(b) = (ab − a)/90 · 1,(6) = 1 + 6/9. Örnek: 0,1(6) = (16 − 1)/90 = 1/6')],sekil=SK,
 ad=[A('K’yi çevir','Devri tek rakam: 0,(3) = 3/9.','K = 1/3'),A('L ve M’yi çevir','0,8(3) = (83 − 8)/90 ; 1,(6) = 1 + 6/9.','L = 75/90 = 5/6 · M = 5/3'),A('Topla','Paydayı 6’da eşitle.','1/3 + 5/6 = 7/6'),A('Oranla','Bölme, ters çarpmadır.','(7/6) ÷ (5/3) = 7/6 × 3/5 = 7/10')],
 puf='Devirli sayıyı kesre çevirirken paydadaki 9’ların ve 0’ların sayısı devrin ve devretmeyen kısmın basamak sayısına bağlıdır.')

# ================= 13 zor · işlem zinciri =================
x0=Fr(1,2); ops=[('+',Fr(3,4)),('*',Fr(4,3)),('-',Fr(1,2)),('/',Fr(2,3))]
def ileri(x):
    for o_,c in ops: x={'+':x+c,'-':x-c,'*':x*c,'/':x/c}[o_]
    return x
fin=ileri(x0); assert fin==Fr(7,4)
y=fin; y=y*Fr(2,3); y=y+Fr(1,2); y=y*Fr(3,4); y=y-Fr(3,4); assert y==x0
eB=(((fin/Fr(2,3))+Fr(1,2))*Fr(3,4))-Fr(3,4)           # ÷ 2/3'ü ters çevirmemiş
eC=(((fin*Fr(2,3))-Fr(1,2))*Fr(3,4))-Fr(3,4)           # −1/2'nin tersini yanlış (yine çıkarmış)
eD=(((fin*Fr(2,3))+Fr(1,2))*Fr(4,3))-Fr(3,4)           # ×4/3'ü ters çevirmemiş
eE=(((fin*Fr(2,3))+Fr(1,2))*Fr(3,4))                    # ilk işlemi (+3/4) geri almamış
assert [eB,eC,eD,eE]==[Fr(51,32),Fr(-1,4),Fr(53,36),Fr(5,4)] and len({x0,eB,eC,eD,eE})==5
lab={'+':'+','-':'-','*':'\\times','/':'\\div'}
o=[]
xs=[0,2.7,5.4,8.1,10.8]
for i,x in enumerate(xs):
    t={0:'$x$',4:'$'+tf(fin)+'$'}.get(i,'')
    o.append(f'\\node[draw,thick,minimum width=1.1cm,minimum height=0.9cm] (b{i}) at ({x},0) {{{t}}};')
for i,(o_,c) in enumerate(ops): o.append(f'\\draw[-{{Stealth}},thick] (b{i}.east) -- node[above=2pt] {{${lab[o_]}{tf(c)}$}} (b{i+1}.west);')
SK=fig('\n'.join(o))
q('0013',tipId='rss-zincir',tip='Kutulara kesir yerleştirme (işlem zinciri)',z='zor',alt='İşlem Zinciri',kaz='Kutulardaki işlem zincirini sondan başa tersleriyle çözer.',kalip='şekilli',
 kart='K-RSS-13 (işlem zinciri) · +3/4, ×4/3, −1/2, ÷2/3 → 7/4',
 metin='Aşağıdaki şemada her ok, soldaki kutudaki sayıya okun üzerinde yazan işlemin uygulanıp sonucun sağdaki kutuya yazılacağını göstermektedir. En sağdaki kutuda 7/4 yazmaktadır.\nBuna göre, en soldaki kutudaki x sayısı kaçtır?',
 dogru=x0,yan=[(eB,'Son oktaki ÷ 2/3 işlemini ters çevirmemiş (7/4 ÷ 2/3 almış) , diğerlerini doğru yapmış.','bilgi'),(eC,'− 1/2 işlemini geri alırken yine çıkarmış.','dikkat'),(eD,'× 4/3 işlemini geri alırken yine 4/3 ile çarpmış.','bilgi'),(eE,'İlk okun (+ 3/4) işlemini geri almamış.','dikkat')],
 istenen='x sayısı.',ip=['Sağdan sola git; her oktaki işlemin tersini uygula.'],bilgi=[B('Ters işlem','toplamanın tersi çıkarma, çarpmanın tersi bölmedir (kesre bölmek, tersiyle çarpmaktır). Örnek: x × 2/3 = 4 ise x = 4 ÷ 2/3 = 6')],sekil=SK,
 ad=[A('Son oku geri al','÷ 2/3 işleminin tersi 2/3 ile çarpmaktır.','7/4 × 2/3 = 7/6'),A('Üçüncü oku geri al','− 1/2’nin tersi + 1/2’dir.','7/6 + 1/2 = 5/3'),A('İkinci oku geri al','× 4/3’ün tersi 3/4 ile çarpmaktır.','5/3 × 3/4 = 5/4'),A('İlk oku geri al','+ 3/4’ün tersi − 3/4’tür.','5/4 − 3/4 = 1/2')],
 puf='Sondan başlayıp her adımda işlemin tersini yap; sonucu ileri doğru yürüyerek kontrol et.')

# ================= 14 zor · iki gösterge + ek doldurma =================
Cp=640; s1,s2,ekk=Fr(6,8),Fr(2,8),Fr(1,8); v=(s1*Cp+ekk*Cp-s2*Cp)/4; assert v==100 and s1*Cp+ekk*Cp<=Cp
e=[(s1*Cp-s2*Cp)/4,(s1*Cp-ekk*Cp-s2*Cp)/4,(s1*Cp+ekk*Cp-s2*Cp)/8,(s1*Cp+ekk*s1*Cp-s2*Cp)/4]; assert e==[80,60,50,95] and len({v,*e})==5
SK=fig(gauge(0,0,8,s1,cap='Sabah')+'\n'+gauge(4.8,0,8,s2,cap='Akşam'))
q('0014',tipId='rss-gosterge',tip='Dairesel gösterge ve kesirli bölmeler',z='zor',alt='Önce-Sonra Göstergesi',kaz='İki göstergeden suyun hacmini bulup ek doldurmayı da katarak tüketimi hesaplar.',kalip='şekilli',
 kart='K-RSS-14 (iki gösterge) · 640 L, 6/8 → 2/8, +1/8 kapasite',
 metin='Kapasitesi 640 litre olan bir su deposunun göstergesi 0 (boş) ile 1 (dolu) arasında 8 eş bölmelidir; sabah ve akşamki durumu şekilde verilmiştir. Gün içinde depoya yalnızca bir kez, kapasitenin 1/8’i kadar su eklenmiş, başka kayıp olmamıştır. Gün boyunca harcanan su 4 kişilik bir aile tarafından eşit kullanıldığına göre kişi başına tüketim kaç litredir?',
 dogru=v,yan=[(e[0],'Eklenen suyu hesaba katmamış: (480 − 160) ÷ 4.','dikkat'),(e[1],'Eklenen suyu (80 L) tüketimden çıkarmış: (480 − 80 − 160) ÷ 4.','dikkat'),(e[2],'Kişi sayısı yerine bölme sayısına (8) bölmüş: 400 ÷ 8.','dikkat'),(e[3],'Eklenen miktarı kapasiteye değil sabahki suya uygulamış (1/8 × 480 = 60): (480 + 60 − 160) ÷ 4.','bilgi')],
 istenen='Kişi başına tüketim (L).',ip=['Her göstergeyi litreye çevir; eklenen su depoya girdiği için tüketimi hesaplarken nasıl yer alır?'],bilgi=[GOS],sekil=SK,
 ad=[A('Sabah suyu','İbre 6. bölmededir.','6/8 × 640 = 480 L'),A('Akşam suyu','İbre 2. bölmededir.','2/8 × 640 = 160 L'),A('Eklenen su','Kapasitenin 1/8’i.','1/8 × 640 = 80 L'),A('Tüketim','Başlangıç + eklenen − sonda kalan.','480 + 80 − 160 = 400 L'),A('Kişi başı','4 kişiye eşit bölünür.','400 ÷ 4 = 100 L')],
 puf='Su miktarı korunur: başlangıç + eklenen = harcanan + kalan.')

bitir(P,'rasyonelsek','mat|Rasyonel Sayılar')
