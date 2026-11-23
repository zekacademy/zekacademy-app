"""AYT Fizik · Paralel Levhalar ve Sığa · 20 soru (kardeş yok, ipucu 1). Şekil verileri ve her cevap/çeldirici Python'da hesaplanıp assert edilir."""
import sys,os,json
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-fiz'))
import _hafif as H
from _hafif import *
from cizim import tikz_svg
KONUAD='Paralel Levhalar ve Sığa'; KK='afiz|Paralel Levhalar ve Sığa'
P=Parti('siga',KONUAD,KK,ders='AYT Fizik',idon='aytfiz'); H.KONU=KONUAD
ALT='Levhalar Arası Alan ve Sığaçlar'
def kartla(n,alt,fikir,tuzak,z,kalip,adim,tipId,tip):
    kart(f'K-AFSIGA-{n:02d}',alt,fikir,tuzak,z,kalip,adim,tipId,tip,'ÖSYM AYT 2018–2026 Fizik (yalnız mantık) · 345 AYT Fizik SB · MEB 12. sınıf fizik')
def q(no,n,**k):
    assert len(k['ip'])==1 and 3<=len(k['ad'])<=7
    mk(P,str(no),adim=len(k['ad']),alt=ALT,kart=f'K-AFSIGA-{n:02d}',**k)
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'; TAIL='\n\\end{tikzpicture}'
ARR='-{Stealth[length=2mm,width=1.8mm]}'
def fig(*parts): return tikz_svg(HEAD+'\n'.join(parts)+TAIL)
# ---------- çizim yardımcıları ----------
def plates(W,D,sgn=True):
    s=f'\\draw[very thick] (0,{D}) -- ({W},{D}); \\draw[very thick] (0,0) -- ({W},0);'
    if sgn:
        for i in range(1,5):
            x=W*i/5; s+=f'\\node[font=\\footnotesize] at ({x:.2f},{D+.22}) {{$+$}}; \\node[font=\\footnotesize] at ({x:.2f},-.22) {{$-$}};'
    return s
def batv(xb,D,lab,wire_to=0):
    m=D/2
    s=(f'\\draw[thick] ({xb},{D}) -- ({xb},{m+.12}); \\draw[thick] ({xb},{m-.12}) -- ({xb},0);'
       f'\\draw[very thick] ({xb-.3},{m+.12}) -- ({xb+.3},{m+.12}); \\draw[very thick] ({xb-.17},{m-.12}) -- ({xb+.17},{m-.12});'
       f'\\node[left] at ({xb-.35},{m}) {{{lab}}}; \\node[font=\\footnotesize] at ({xb+.5},{m+.28}) {{$+$}};')
    if wire_to is not None: s+=f'\\draw[thick] ({xb},{D}) -- ({wire_to},{D}); \\draw[thick] ({xb},0) -- ({wire_to},0);'
    return s
def alan_ok(W,D,n=4):
    s=''
    for i in range(1,n+1):
        x=W*i/(n+1); s+=f'\\draw[vurgu,thick,{ARR}] ({x:.2f},{D-.2:.2f}) -- ({x:.2f},{.2:.2f});'
    return s
def capH(x,y,lab,pos='above'):
    return (f'\\draw[thick] ({x-.6},{y}) -- ({x-.11},{y}); \\draw[thick] ({x+.11},{y}) -- ({x+.6},{y});'
            f'\\draw[very thick] ({x-.11},{y-.35}) -- ({x-.11},{y+.35}); \\draw[very thick] ({x+.11},{y-.35}) -- ({x+.11},{y+.35});'
            f'\\node[{pos}] at ({x},{y+.38}) {{{lab}}};')
def capV(x,y,lab,yt=None,yb=None):
    yt=y+.6 if yt is None else yt; yb=y-.6 if yb is None else yb
    return (f'\\draw[thick] ({x},{yt}) -- ({x},{y+.11}); \\draw[thick] ({x},{y-.11}) -- ({x},{yb});'
            f'\\draw[very thick] ({x-.35},{y+.11}) -- ({x+.35},{y+.11}); \\draw[very thick] ({x-.35},{y-.11}) -- ({x+.35},{y-.11});'
            f'\\node[right] at ({x+.4},{y}) {{{lab}}};')
def sw(x,y,lab):
    return (f'\\draw[thick] ({x},{y}) -- ({x+.15},{y}); \\fill ({x+.15},{y}) circle (.05); \\draw[thick] ({x+.15},{y}) -- ({x+.75},{y+.4}); \\draw[thick] ({x+.8},{y}) -- ({x+.95},{y});'
            f'\\node[above] at ({x+.5},{y+.35}) {{{lab}}};')
def dot(x,y): return f'\\fill ({x},{y}) circle (.06);'
def pg(xmax,ymax,xt,yt,xl,yl,body,w=6.4,h=5.0):
    opt=(f'width={w}cm,height={h}cm,xmin=0,xmax={xmax},ymin=0,ymax={ymax},xtick={{{xt}}},ytick={{{yt}}},grid=both,major grid style={{gray!55,thin}},'
         f'tick label style={{font=\\footnotesize}},axis lines=left,xlabel={{{xl}}},ylabel={{{yl}}},xlabel style={{font=\\small}},ylabel style={{font=\\small}}')
    return tikz_svg(HEAD+'\\begin{axis}['+opt+']\n'+body+'\n\\end{axis}'+TAIL)
ROM=('I','II','III')
def onc(truth,reasons,sira):
    def kume(l): return set(ROM) if l=='I, II ve III' else set(x for x in l.replace('Yalnız ','').replace(' ve ',' ').split())
    gercek={k for k,v in truth.items() if v}
    dog=[l for l in sira if kume(l)==gercek]; assert len(dog)==1,(sira,gercek)
    yan=[]
    for l in sira:
        if l==dog[0]: continue
        k=kume(l); c=[]
        for x in ROM:
            if x in k and x not in gercek: c.append(f'{x}. öncülü doğru saymış, oysa yanlıştır: {reasons[x]}')
            if x in gercek and x not in k: c.append(f'{x}. öncülünü yanlış saymış, oysa doğrudur: {reasons[x]}')
        yan.append((l,' '.join(c),'bilgi'))
    ad=[A(f'{x}. öncülü incele',reasons[x],f'{x}: '+('doğru' if truth[x] else 'yanlış')) for x in ROM]
    ad.append(A('Sonuca var','Doğru öncülleri birleştir.','Doğru: '+', '.join(x for x in ROM if truth[x])))
    return dog[0],yan,ad
S5=['Yalnız I','Yalnız II','I ve II','I ve III','II ve III']
# ---------- bilgi kutuları ----------
B_ALAN=B('Levhalar arası düzgün alan','Paralel levhalar arasında alan düzgündür ve E = V/d; yönü + levhadan − levhaya doğrudur. Örnek: 30 V ve 5 mm aralıklı levhalarda E = 30 ÷ 0,005 = 6000 V/m')
B_KUV=B('Alandaki yüklü parçacık','q yüklü parçacığa F = qE kuvveti etki eder (+ yük alan yönünde, − yük alana zıt yönde); a = F/m. Alana dik giren parçacık parabol çizer. Örnek: 1 μC’luk yük 2000 N/C’lik alanda 2 mN’luk kuvvet görür')
B_SIG=B('Sığa','C = q/V ve paralel levhalı sığaçta C = κ·ε₀·A/d (κ: dielektrik katsayısı). Sığa yalnız geometriye ve yalıtkana bağlıdır. Örnek: 7 μF’lık sığaç 3 V’ta 21 μC yük depolar')
B_ENJ=B('Sığaçta depolanan enerji','U = ½qV = ½CV² = q²/(2C). Örnek: 100 μF’lık sığaç 6 V’ta ½ × 100 × 36 = 1800 μJ depolar')
B_BAG=B('Sığaçların bağlanması','Seri bağlamada yükler eşittir ve 1/C = 1/C₁ + 1/C₂ + …; paralel bağlamada gerilimler eşittir ve C = C₁ + C₂ + …. Örnek: 1 μF ile 3 μF seri bağlanınca 3/4 μF, paralel bağlanınca 4 μF olur')
B_DEN=B('Dengede yüklü cisim','Dengedeki cisimde bileşke kuvvet sıfırdır: elektriksel kuvvet ağırlığa eşit büyüklükte ve zıt yöndedir. Yük, e = 1,6 × 10⁻¹⁹ C’un tam katıdır; q = n·e. Örnek: 3 fazla elektron 4,8 × 10⁻¹⁹ C eksi yük demektir')
B_YUK=B('Üreteç bağlı ya da ayrılmış','Üreteç bağlıyken potansiyel fark V sabit kalır; üreteçten ayrılmış sığaçta yük q sabit kalır. Önce hangi niceliğin sabit olduğunu belirle, sonra q = CV bağıntısını kullan')
# ================= KARTLAR =================
kartla(1,'Levhalar arası alan ve potansiyel','E = V/d; noktalar arası potansiyel farkı alan doğrultusundaki uzaklıkla orantılıdır, iş W = qΔV.','Birimi (cm → m) çevirmemek; iş hesabında tüm V’yi kullanmak.','orta','şekilli',3,'siga-alan','Levhalar arası düzgün alan ve potansiyel')
kartla(2,'Alandaki yüklü parçacığın hareketi','F = qE, a = F/m; alana dik girişte sapma y = ½at², t = ℓ/v; hızlanmada Ek = qV.','Kütleyi kg’a çevirmemek; sapmada hızın etkisini (v²) unutmak; ΔEk’yı yükün ağırlığıyla karıştırmak.','orta','şekilli',4,'siga-parcacik','Düzgün alanda yüklü parçacık hareketi')
kartla(3,'Dengede yüklü damla','qE = mg; q = n·e; E = V/d; levha aralığı ya da gerilim değişirse net kuvvet bulunur.','Uzaklığı metreye çevirmemek; üreteç bağlıyken alanın sabit kaldığını sanmak.','zor','şekilli',4,'siga-denge','Dengedeki yüklü cisim ve elektron sayısı')
kartla(4,'Sığa ve dielektrik','C = κε₀A/d; q = CV; kısmi dielektrik dolgusunda paralel bağlı iki sığaç gibi düşünülür.','Dielektriğin tüm sığacı doldurduğunu varsaymak; alanı yarılamadan toplamak.','kolay','şekilli',3,'siga-sigac','Sığanın bağlı olduğu nicelikler')
kartla(5,'Sığaçların seri–paralel bağlanması','Seri kolda yük eşit, paralelde gerilim eşit; yük ve gerilim dağılımı sığa oranlarıyla bulunur.','Seride gerilimi, paralelde yükü eşit paylaştırmak.','orta','şekilli',4,'siga-bagla','Seri ve paralel bağlı sığaçlar')
kartla(6,'Üreteç bağlı / ayrılmış sığaç','Bağlıyken V, ayrılmışken q sabittir; C değişince diğer nicelikler q = CV ile bulunur.','İki durumda sabit niceliği karıştırmak; alanın ayrılmış sığaçta d’den bağımsız olduğunu atlamak.','orta','öncüllü',3,'siga-yuk','Sığaçta yük–gerilim–enerji değişimi')
kartla(7,'Sığaçta enerji','U = ½CV² = q²/2C; enerji paylaşımında iki sığaç birleşince toplam enerji korunmaz.','½ çarpanını unutmak; yük paylaşımında enerjinin korunduğunu sanmak.','orta','şekilli',3,'siga-enerji','Sığaçta depolanan enerji')
kartla(8,'Yük–gerilim ve gerilim–uzaklık grafikleri','Grafikteki eğim sığayı (q–V) ya da q/ε₀A’yı (V–d) verir; enerji değişimi dış işe eşittir.','Eğimi sığa yerine tersiyle karıştırmak; ½ çarpanını unutmak.','zor','grafik',4,'siga-grafik','Sığaç grafikleri ve enerji')
# ================= 01 · kolay · alan =================
W,D=3.2,1.7
sk=fig(plates(W,D),batv(-1.5,D,'$200$ V'),alan_ok(W,D,3),
       f'\\draw[<->,thick] ({W+.45},0) -- ({W+.45},{D}); \\node[right] at ({W+.5},{D/2}) {{$4$ cm}};',f'\\node[right,vurgu] at ({W*.5+.1:.2f},{D/2}) {{$E$}};')
V1,d1=200,Fr(4,100); E1=V1/d1; assert E1==5000
assert Fr(V1)/4==50 and V1*d1==8 and Fr(V1)/Fr(4,10)==500 and Fr(V1)/Fr(4,1000)==50000
q('0001',1,z='kolay',kalip='şekilli',tipId='siga-alan',tip='Levhalar arası düzgün alan ve potansiyel',kaz='Paralel levhalar arasındaki düzgün alanın şiddetini E = V/d ile hesaplar.',
 metin='Şekilde, bir üretece bağlı paralel iletken levhaların arasında düzgün bir elektrik alan oluşmuştur. Üretecin potansiyel farkı ve levhalar arasındaki uzaklık şekilde verilmiştir.\nBuna göre, levhalar arasındaki elektrik alanın şiddeti kaç V/m’dir?',
 dogru=E1,yan=[(50,'Uzaklığı cm olarak bırakıp 200 ÷ 4 = 50 bulmuş; uzaklığı metreye çevirmemiştir.','islem'),(8,'Alanı potansiyel fark ile uzaklığın çarpımı sanmıştır: 200 × 0,04 = 8.','bilgi'),(500,'4 cm’yi 0,4 m yazmıştır: 200 ÷ 0,4 = 500.','islem'),(50000,'4 cm’yi 0,004 m yazmıştır: 200 ÷ 0,004 = 50 000.','islem')],
 istenen='Levhalar arası elektrik alan şiddeti (V/m).',ip=['Alan şiddetini potansiyel fark ve levha aralığıyla ilişkilendir; uzaklığın birimine dikkat et.'],bilgi=[B_ALAN],
 ad=[A('Birimi çevir','Uzaklığı metre cinsine çevir.','d = 4 cm = 0,04 m'),A('Alanı yaz','Düzgün alanda şiddet, potansiyel farkın uzaklığa oranıdır.','E = V ÷ d'),A('Hesapla','Değerleri yerine yaz.','E = 200 ÷ 0,04 = 5000 V/m')],
 puf='Düzgün alan şiddeti E = V/d’dir; önce uzaklığı metreye çevir.',sekil=sk)
# ================= 02 · kolay · F=qE, a =F/m =================
W,D=3.2,2.0
sk=fig(plates(W,D),alan_ok(W,D,3),
       f'\\fill[orange!70!black] ({W*.375:.2f},{D*.5:.2f}) circle (.15); \\node[font=\\scriptsize,white] at ({W*.375:.2f},{D*.5:.2f}) {{$+$}}; \\node[right] at ({W+.1},{D*.5+.5}) {{$q=+2\\,\\mu$C}};',
       f'\\node[right] at ({W+.1},{D*.5-.3}) {{$E=5\\times10^{{3}}$ N/C}};')
qy,Ey,my=Fr(2,10**6),5000,Fr(10,1000); F2=qy*Ey; a2=F2/my; assert F2==Fr(1,100) and a2==1
assert F2/10==Fr(1,1000) and F2*my==Fr(1,10**4) and F2/(my*10)==Fr(1,10) and F2==Fr(1,100)
q('0002',2,z='kolay',kalip='şekilli',tipId='siga-parcacik',tip='Düzgün alanda yüklü parçacık hareketi',kaz='Düzgün alandaki yüklü parçacığa etki eden kuvvetten ivmeyi hesaplar.',
 metin='Şekilde, büyüklüğü verilen düzgün elektrik alan içinde, yükü +2 μC ve kütlesi 10 g olan bir parçacık serbest bırakılıyor. Parçacığın ağırlığı ve sürtünme ihmal edilmektedir.\nBuna göre, parçacığın ivmesinin büyüklüğü kaç m/s²’dir?',
 dogru=a2,yan=[(Fr(1,1000),'Kütleyi gram olarak bırakıp 0,01 ÷ 10 = 0,001 bulmuş; kütleyi kg’a çevirmemiştir.','islem'),(Fr(1,10000),'İvmeyi kuvvet ile kütlenin çarpımı sanmıştır: 0,01 × 0,01 = 0,0001.','bilgi'),(Fr(1,100),'Kuvvetin büyüklüğünü (0,01 N) ivme olarak yazmıştır.','dikkat'),(Fr(1,10),'Kuvveti, kütle ile g’nin çarpımı olan ağırlığa (0,1 N) bölmüştür: 0,01 ÷ 0,1 = 0,1.','bilgi')],
 istenen='Parçacığın ivmesi (m/s²).',ip=['Önce alanın parçacığa uyguladığı kuvveti bul; sonra Newton’un ikinci yasasını SI birimleriyle kullan.'],bilgi=[B_KUV],
 ad=[A('Kuvveti hesapla','Elektriksel kuvvet yük ile alanın çarpımıdır; μC’yi C’ye çevir.','F = 2 × 10⁻⁶ × 5000 = 0,01 N'),A('Kütleyi çevir','Gramı kilograma çevir.','m = 10 g = 0,01 kg'),A('İvmeyi bul','İkinci yasa: ivme = kuvvet ÷ kütle.','a = 0,01 ÷ 0,01 = 1 m/s²')],
 puf='Yüklü parçacığın ivmesi a = qE/m’dir; yük μC, kütle g ise önce SI’ya çevir.',sekil=sk)
# ================= 03 · kolay · öncüllü, sığa bağlılığı =================
tr={'I':True,'II':False,'III':True}
rs={'I':'Levha alanı artınca C = κε₀A/d bağıntısına göre sığa artar.','II':'Levhalar arası uzaklık artınca sığa azalır; sığa d ile ters orantılıdır.','III':'Havadan büyük dielektrik katsayılı yalıtkan κ’yı artırır ve sığa artar.'}
d3,y3,ad3=onc(tr,rs,S5)
q('0003',4,z='kolay',kalip='öncüllü',tipId='siga-sigac',tip='Sığanın bağlı olduğu nicelikler',kaz='Paralel levhalı sığacın sığasını belirleyen nicelikleri yorumlar.',
 metin='Levhaları arasında hava bulunan paralel levhalı bir sığaçta;\nI. levhaların yüzey alanını artırmak,\nII. levhalar arasındaki uzaklığı artırmak,\nIII. levhalar arasına havadan daha büyük dielektrik katsayılı bir yalıtkan koymak\nişlemlerinden hangileri tek başına yapıldığında sığacın sığası artar?',
 dogru=d3,yan=y3,sira=S5,istenen='Sığayı artıran işlemler.',ip=['Sığanın levha alanı, levhalar arası uzaklık ve yalıtkanla nasıl değiştiğini gösteren bağıntıyı düşün.'],bilgi=[B_SIG],ad=ad3,
 puf='C = κε₀A/d: A ve κ ile doğru, d ile ters orantılı.')
# ================= 04 · orta · enerji =================
sk=fig(batv(0,2.4,'$12$ V',wire_to=None),'\\draw[thick] (0,2.4) -- (1.9,2.4);',capH(2.5,2.4,'$4\\,\\mu$F'),'\\draw[thick] (3.1,2.4) -- (4.4,2.4) -- (4.4,0) -- (0,0);')
C4,V4=4,12; q4=C4*V4; U4=Fr(1,2)*C4*V4**2
assert q4==48 and U4==288 and Fr(1,2)*C4*V4==24 and C4*V4**2==576
assert Fr(1,2)*V4**2==72 and V4**2==144
q('0004',7,z='orta',kalip='şekilli',tipId='siga-enerji',tip='Sığaçta depolanan enerji',kaz='Üretece bağlı sığaçta yükü ve depolanan enerjiyi hesaplar.',
 metin='Yüksüz bir sığaç, sığası ve üretecin potansiyel farkı şekilde verilen devrede üretece bağlanıyor. Yük akışı sona erdiğinde devredeki akım sıfır oluyor.\nBuna göre, sığaçta depolanan enerji kaç μJ’dür?',
 dogru=U4,yan=[(24,'Enerjiyi ½·C·V = ½ × 4 × 12 = 24 diye hesaplamış; gerilimin karesini almamıştır.','islem'),(48,'Sığaçta depolanan yükü (q = CV = 48 μC) enerji sanmıştır.','bilgi'),(72,'Sığayı katmadan ½·V² = ½ × 144 = 72 hesaplamıştır.','dikkat'),(576,'Enerjiyi C·V² = 4 × 144 = 576 diye yazmış; ½ çarpanını unutmuştur.','islem')],
 istenen='Sığaçta depolanan enerji (μJ).',ip=['Yük akışı bittiğinde sığaç üretecin gerilimine ulaşmıştır; enerjiyi sığa ve gerilimle ifade et.'],bilgi=[B_ENJ],
 ad=[A('Gerilimi belirle','Yük akışı bitince sığacın uçları arasındaki potansiyel fark üretecinkine eşittir.','V = 12 V'),A('Enerji bağıntısını yaz','Depolanan enerji sığa ve gerilimle bulunur.','U = ½ × C × V²'),A('Hesapla','Değerleri yerine yaz.','U = ½ × 4 × 144 = 288 μJ')],
 puf='Tam dolu sığaçta enerji U = ½CV²; gerilim kare olarak girer.',sekil=sk)
# ================= 05 · orta · seri =================
sk=fig(batv(0,2.4,'$18$ V',wire_to=None),'\\draw[thick] (0,2.4) -- (1.2,2.4);',capH(1.8,2.4,'K: $3\\,\\mu$F'),'\\draw[thick] (2.4,2.4) -- (3.4,2.4);',capH(4.0,2.4,'L: $6\\,\\mu$F'),'\\draw[thick] (4.6,2.4) -- (5.6,2.4) -- (5.6,0) -- (0,0);')
CK,CL,V5=3,6,18; Ce=Fr(CK*CL,CK+CL); q5=Ce*V5; VK=q5/CK; VL=q5/CL
assert Ce==2 and q5==36 and VK==12 and VL==6 and VK+VL==V5 and Fr(V5,2)==9
q('0005',5,z='orta',kalip='şekilli',tipId='siga-bagla',tip='Seri ve paralel bağlı sığaçlar',kaz='Seri bağlı sığaçlarda yükün eşit olduğunu kullanarak gerilim dağılımını bulur.',
 metin='Başlangıçta yüksüz olan K ve L sığaçları, sığaları ve üretecin potansiyel farkı şekilde verilen devrede üretece bağlanıyor. Yük akışı sona eriyor.\nBuna göre, L sığacının uçları arasındaki potansiyel fark kaç V’tur?',
 dogru=VL,yan=[(9,'Toplam gerilimi iki sığaca eşit paylaştırmış: 18 ÷ 2 = 9 V.','bilgi'),(12,'K sığacının gerilimini (12 V) bulup L’nin gerilimi sanmıştır.','dikkat'),(18,'Sığaçları paralel sanmış; her birinin gerilimini üretecin gerilimi (18 V) almıştır.','bilgi'),(36,'Seri kolun yükünü (36 μC) potansiyel fark olarak yazmıştır.','dikkat')],
 istenen='L sığacının uçları arasındaki potansiyel fark (V).',ip=['Seri bağlı sığaçlarda hangi niceliğin ortak olduğunu düşün; önce eşdeğer sığa ile bu ortak niceliği bul.'],bilgi=[B_BAG],
 ad=[A('Eşdeğer sığayı bul','Seri bağlı sığaçların eşdeğeri çarpım bölü toplamdır.','C = 3 × 6 ÷ 9 = 2 μF'),A('Ortak yükü bul','Seride her sığaçta yük aynıdır ve toplam gerilimden hesaplanır.','q = 2 × 18 = 36 μC'),A('L’nin gerilimi','Yükü L’nin sığasına böl.','V_L = 36 ÷ 6 = 6 V')],
 puf='Seri bağlı sığaçlarda yük ortak, gerilim sığayla ters orantılı bölüşülür; küçük sığa büyük gerilim alır.',sekil=sk)
# ================= 06 · orta · seri + paralel =================
sk=fig(batv(0,3,'$12$ V',wire_to=None),'\\draw[thick] (0,3) -- (.7,3);',capH(1.3,3,'K: $6\\,\\mu$F'),'\\draw[thick] (1.9,3) -- (5.2,3);',dot(3.2,3),dot(3.2,0),
       capV(3.2,1.5,'L: $1\\,\\mu$F',3,0),capV(5.2,1.5,'M: $2\\,\\mu$F',3,0),'\\draw[thick] (5.2,0) -- (0,0);')
C1,C2,C3,V6=1,2,6,12; Cp=C1+C2; Ce6=Fr(Cp*C3,Cp+C3); qt=Ce6*V6; V3=qt/C3; Vp=qt/Cp; qL=C1*Vp; qM=C2*Vp
assert Cp==3 and Ce6==2 and qt==24 and V3==4 and Vp==8 and qL==8 and qM==16 and qt==qL+qM and Fr(qt,2)==12
q('0006',5,z='orta',kalip='şekilli',tipId='siga-bagla',tip='Seri ve paralel bağlı sığaçlar',kaz='Karışık bağlı sığaçlarda eşdeğer sığa ve yük dağılımından bir sığacın yükünü bulur.',
 metin='Sığaları ve üretecin potansiyel farkı şekilde verilen devrede K, L ve M sığaçları başlangıçta yüksüzdür. Devre üretece bağlanıyor ve yük akışı sona eriyor.\nBuna göre, L sığacında depolanan yük kaç μC’dur?',
 dogru=qL,yan=[(4,'K sığacının gerilimini (4 V) yük olarak yazmıştır.','dikkat'),(12,'Paralel kolun toplam yükünü iki sığaca eşit paylaştırmıştır: 24 ÷ 2 = 12 μC.','bilgi'),(16,'M sığacının yükünü (2 × 8 = 16 μC) L’nin yükü sanmıştır.','dikkat'),(24,'Devrenin toplam yükünü (24 μC) L sığacının yükü saymıştır.','bilgi')],
 istenen='L sığacında depolanan yük (μC).',ip=['Önce paralel kolu tek sığaç gibi düşün; ana koldaki ortak niceliğin bu kolun gerilimini nasıl belirlediğini bul.'],bilgi=[B_BAG],
 ad=[A('Paralel kolu birleştir','L ve M paralel bağlıdır; sığaları toplanır.','C_LM = 1 + 2 = 3 μF'),A('Eşdeğer sığa','K ile bu kol seridir.','C = 6 × 3 ÷ 9 = 2 μF'),A('Toplam yük','Ana koldaki yük K’nin yüküne ve paralel kolun toplam yüküne eşittir.','q = 2 × 12 = 24 μC'),A('Paralel kolun gerilimi','Toplam yükü kolun eşdeğer sığasına böl.','V = 24 ÷ 3 = 8 V'),A('L’nin yükü','Yük = sığa × gerilim.','q_L = 1 × 8 = 8 μC')],
 puf='Önce paralel kolu birleştir; seri koldaki ortak yükle paralel kolun gerilimini bul, sonra her sığacın yükünü q = CV ile hesapla.',sekil=sk)
# ================= 07 · orta · öncüllü · üreteç bağlı, d artar =================
W,D=3.2,1.5
sk=fig(plates(W,D),batv(-1.5,D,'$V$'),f'\\draw[vurgu,very thick,{ARR}] ({W+.5},{D}) -- ({W+.5},{D+.8}); \\node[right] at ({W+.55},{D+.4}) {{üst levha}};',
       f'\\draw[<->,thick] (-.55,0) -- (-.55,{D}); \\node[font=\\footnotesize,fill=white,inner sep=1pt] at (-.55,{D/2}) {{$d$}};')
C7=lambda d: Fr(1,d); V7=10
assert C7(2)<C7(1) and V7*C7(2)<V7*C7(1) and Fr(V7,2)<Fr(V7,1) and Fr(1,2)*C7(2)*V7**2<Fr(1,2)*C7(1)*V7**2
tr={'I':False,'II':True,'III':True}
rs={'I':'Sığaç üretece bağlı kaldığı için levhalar arasındaki potansiyel fark üretecin gerilimine eşit ve sabittir.','II':'V sabit kalırken d artar; E = V/d olduğundan alan şiddeti azalır.','III':'d artınca C azalır, V sabit olduğundan U = ½CV² azalır; depolanan enerji azalır.'}
d7,y7,ad7=onc(tr,rs,S5)
q('0007',6,z='orta',kalip='öncüllü',tipId='siga-yuk',tip='Sığaçta yük–gerilim–enerji değişimi',kaz='Üretece bağlı sığaçta levhalar arası uzaklık artınca değişen nicelikleri yorumlar.',
 metin='Levhaları arasında hava bulunan yüklü paralel levhalı bir sığaç, şekildeki gibi bir üretece bağlıdır. Üreteç bağlı kalarak üst levha, levhalar paralel kalacak biçimde yavaşça yukarı çekiliyor ve levhalar arasındaki uzaklık artırılıyor.\nBuna göre;\nI. Levhalar arasındaki potansiyel fark azalır.\nII. Levhalar arasındaki elektrik alanın şiddeti azalır.\nIII. Sığaçta depolanan enerji azalır.\nyargılarından hangileri doğrudur?',
 dogru=d7,yan=y7,sira=S5,istenen='Doğru olan yargılar.',ip=['Üreteç bağlı olduğuna göre hangi niceliğin sabit kaldığını belirle; diğerlerini bu nicelik ve sığadaki değişimle yorumla.'],bilgi=[B_YUK],ad=ad7,
 puf='Üreteç bağlıyken hangi niceliğin sabit kaldığını belirle; diğer nicelikleri ondan türet.',sekil=sk)
# ================= 08 · orta · öncüllü · ayrılmış, d artar =================
W,D=3.2,1.5
sk=fig(plates(W,D),batv(-2.4,D,'$V$',wire_to=None),f'\\draw[thick] (-2.4,{D}) -- (-1.6,{D});',sw(-1.6,D,'S'),f'\\draw[thick] (-.65,{D}) -- (0,{D}); \\draw[thick] (-2.4,0) -- (0,0);',
       f'\\draw[vurgu,very thick,{ARR}] ({W+.5},{D}) -- ({W+.5},{D+.8}); \\node[right] at ({W+.55},{D+.4}) {{üst levha}};')
# yük sabit (üreteçten ayrılmış)
q8=Fr(60); C8a,C8b=Fr(6),Fr(3)
assert q8/C8b>q8/C8a and C8b<C8a
Ea=q8/(C8a); # E = q/(eps0 A) -> d'den bağımsız: aynı q, aynı A
tr={'I':True,'II':True,'III':True}
rs={'I':'d artınca C = κε₀A/d azalır.','II':'q sabit kalır, C azaldığı için V = q/C artar.','III':'E = q/(κε₀A) bağıntısında d yoktur; yük ve alan sabit olduğundan alan şiddeti değişmez.'}
S8=['Yalnız II','Yalnız III','I ve II','I ve III','I, II ve III']
d8,y8,ad8=onc(tr,rs,S8)
q('0008',6,z='orta',kalip='öncüllü',tipId='siga-yuk',tip='Sığaçta yük–gerilim–enerji değişimi',kaz='Üreteçten ayrılmış sığaçta levhalar arası uzaklık artınca değişen ve değişmeyen nicelikleri yorumlar.',
 metin='Levhaları arasında hava bulunan yüklü paralel levhalı bir sığaç, üreteçten ayrılmış hâlde şekilde gösterilmiştir. Levhalar paralel kalacak biçimde üst levha yavaşça yukarı çekiliyor ve levhalar arasındaki uzaklık artırılıyor.\nBuna göre, bu işlem sırasında;\nI. Sığacın sığası azalır.\nII. Levhalar arasındaki potansiyel fark artar.\nIII. Levhalar arasındaki elektrik alanın şiddeti değişmez.\nyargılarından hangileri doğrudur?',
 dogru=d8,yan=y8,sira=S8,istenen='Doğru olan yargılar.',ip=['Üreteç ayrıldığına göre sabit kalan niceliği bul; potansiyel farkı ve alanı bu nicelik ile sığa cinsinden yaz.'],bilgi=[B_YUK],ad=ad8,
 puf='Ayrılmış sığaçta sabit olan nicelik q’dur; gerisini q = CV ve alan–yük ilişkisiyle sen bul.',sekil=sk)
# ================= 09 · orta · sapma oranı =================
W,D=4.0,2.4; y0=1.7; dy=.9
pts=' '.join(f'({W*i/20:.2f},{y0-dy*(i/20)**2:.3f})' for i in range(21))
sk=fig(plates(W,D),batv(-1.5,D,'$V$'),
       f'\\draw[vurgu,very thick,{ARR}] (-.9,{y0}) -- (-.1,{y0}); \\node[above] at (-.55,{y0}) {{$\\vec v$}};',
       f'\\draw[vurgu,very thick] plot[smooth] coordinates {{{pts}}};',
       f'\\fill[orange!70!black] (0,{y0}) circle (.1); \\node[font=\\scriptsize] at (0,{y0}) {{$+$}};',
       f'\\draw[dashed] (0,{y0}) -- ({W+.5},{y0}); \\draw[<->,thick] ({W+.35},{y0}) -- ({W+.35},{y0-dy}); \\node[right] at ({W+.4},{y0-dy/2}) {{$y$}};')
f9=lambda Vf,vf: Fr(Vf)/Fr(vf)**2
r9=f9(2,Fr(1,2))/f9(1,1); assert r9==8 and 2*4==8 and 2+4==6 and 4*4==16 and 2==Fr(2,1) and f9(1,Fr(1,2))==4
q('0009',2,z='orta',kalip='şekilli',tipId='siga-parcacik',tip='Düzgün alanda yüklü parçacık hareketi',kaz='Alana dik giren parçacığın sapmasının potansiyel fark ve hızla nasıl değiştiğini hesaplar.',
 metin='Şekildeki paralel levhalar arasına, levhalara paralel v hızıyla giren pozitif yüklü bir parçacık levhalardan çıkarken ilk doğrultusundan y kadar sapıyor. Daha sonra levhalar arasındaki potansiyel fark 2 katına çıkarılıyor ve aynı parçacık, aynı noktadan v/2 hızıyla levhalara paralel olarak yeniden gönderiliyor.\nParçacık levhalara çarpmadan çıktığına ve ağırlığı ihmal edildiğine göre, bu durumda parçacığın sapması kaç y olur?',
 dogru=r9,yan=[(2,'Yalnız potansiyel farkın etkisini hesaba katmış, hızın değişmesini unutmuştur.','dikkat'),(4,'Yalnız hızın yarıya inmesinin etkisini (v² ile ters orantı) hesaba katmış, potansiyel farkı unutmuştur.','dikkat'),(6,'İki etkiyi çarpmak yerine toplamıştır: 2 + 4 = 6.','islem'),(16,'Potansiyel farkın etkisini de kare almıştır: 4 × 4 = 16.','bilgi')],
 istenen='Yeni sapma miktarı (y cinsinden).',ip=['Sapmayı ivme ve levhalar içinde kalma süresi cinsinden yaz; bu iki niceliğin gerilim ve hızla nasıl değiştiğine bak.'],bilgi=[B_KUV,B_ALAN],
 ad=[A('İvmeyi yaz','Alan V/d ile, ivme ise qE/m ile bulunur; ivme V ile doğru orantılıdır.','a = qV ÷ (m·d) → a′ = 2a'),A('Süreyi yaz','Levha boyunca yatay hız sabittir; süre hızla ters orantılıdır.','t = ℓ ÷ v → t′ = 2t'),A('Sapmayı yaz','Alan doğrultusunda başlangıç hızı sıfır olduğundan sapma ½at² ile bulunur.','y = ½at²'),A('Oranla','Yeni değerleri yerine koy.','y′ = ½ × 2a × (2t)² = 8 × ½at² = 8y')],
 puf='Alana dik girişte sapma y ∝ V/(d·v²) bağıntısına uyar.',sekil=sk)
# ================= 10 · zor · öncüllü · iki parçacık =================
W,D=4.2,3.3
sk=fig(plates(W,D),alan_ok(W,D,4),f'\\node[vurgu,right] at ({W+.1},{D/2}) {{$\\vec E$}};',
       f'\\fill[orange!70!black] (-1.1,2.5) circle (.12); \\draw[thick,{ARR}] (-.95,2.5) -- (-.1,2.5); \\node[above] at (-.5,2.5) {{$v$}}; \\node[left] at (-1.25,2.5) {{K: $+q,\\ m$}};',
       f'\\fill[orange!70!black] (-1.1,.9) circle (.12); \\draw[thick,{ARR}] (-.95,.9) -- (-.1,.9); \\node[above] at (-.5,.9) {{$v$}}; \\node[left] at (-1.25,.9) {{L: $+2q,\\ 4m$}};')
aK=Fr(1); aL=Fr(2,4)*aK; yK=Fr(1); yL=aL/aK*yK; dEK=1*aK*4*0+Fr(1)*yK; dEL=2*yL
assert aL==Fr(1,2) and yL==Fr(1,2) and dEL==dEK   # ΔEk = qE·y : K: q·1, L: 2q·(1/2)
tr={'I':True,'II':True,'III':False}
rs={'I':'a = qE/m olduğundan a_K = qE/m, a_L = 2qE/4m = a_K/2 olur; K’nin ivmesi daha büyüktür.','II':'Levhalara paralel yöndeki hız değişmez; ikisi de aynı v ile aynı ℓ uzunluğunu aldığından süreleri t = ℓ/v eşittir.','III':'Kinetik enerji artışı alanın yaptığı işe eşittir: K’de qE·y, L’de 2qE·(y/2) = qE·y; artışlar eşittir.'}
d10,y10,ad10=onc(tr,rs,S5)
q('0010',2,z='orta',kalip='öncüllü',tipId='siga-parcacik',tip='Düzgün alanda yüklü parçacık hareketi',kaz='Alana dik giren iki parçacığın ivme, süre ve kinetik enerji artışını karşılaştırır.',
 metin='Yer çekiminin ihmal edildiği bir ortamda, şekildeki paralel levhalar arasında düzgün bir elektrik alan vardır. Yükleri ve kütleleri şekilde verilen K ve L parçacıkları levhalara paralel ve aynı büyüklükteki v hızıyla alana giriyor ve levhalara çarpmadan levhalardan çıkıyor.\nBuna göre;\nI. K’nin ivmesi L’ninkinden büyüktür.\nII. K ve L’nin levhalar arasında kalma süreleri eşittir.\nIII. Levhalardan çıkarken K’nin kinetik enerjisindeki artış L’ninkinden büyüktür.\nyargılarından hangileri doğrudur?',
 dogru=d10,yan=y10,sira=S5,istenen='Doğru olan yargılar.',ip=['İvmeyi, süreyi ve sapmayı sırayla yük ile kütle cinsinden yaz; kinetik enerji artışını alanın yaptığı iş ile ilişkilendir.'],bilgi=[B_KUV],ad=ad10,
 puf='Alana dik girişte ivme, süre ve sapma ayrı ayrı yazılır; kinetik enerji artışı alanın yaptığı işle ilişkilidir.',sekil=sk)
# ================= 11 · orta · Millikan =================
W,D=3.0,1.8
sk=fig(plates(W,D),batv(-1.5,D,'$400$ V'),f'\\fill[gray!50,draw=black,thick] ({W/2},{D/2}) circle (.17);',
       f'\\draw[<->,thick] ({W+.45},0) -- ({W+.45},{D}); \\node[right] at ({W+.5},{D/2}) {{$2$ cm}};')
m11=Fr(16,10)*Fr(1,10**15); g11=10; Vv=400; dd=Fr(2,100); e11=Fr(16,10)*Fr(1,10**19)
E11=Vv/dd; qq=m11*g11/E11; n11=qq/e11
assert E11==20000 and n11==5
n_cm=m11*g11/(Fr(Vv)/2)/e11; n_02=m11*g11/(Fr(Vv)/Fr(2,10))/e11; n_noD=m11*g11/Vv/e11; n_prod=m11*g11/(Vv*dd)/e11
assert (n_cm,n_02,n_noD,n_prod)==(500,50,250,12500)
q('0011',3,z='orta',kalip='şekilli',tipId='siga-denge',tip='Dengedeki yüklü cisim ve elektron sayısı',kaz='Levhalar arasında dengedeki yağ damlasının yükünü ve fazla elektron sayısını hesaplar.',
 metin='Şekilde, potansiyel farkı ve aralarındaki uzaklık verilen yatay paralel levhalar arasında kütlesi 1,6 × 10⁻¹⁵ kg olan bir yağ damlası durgun hâlde dengededir. Hava direnci ve kaldırma kuvveti ihmal edilmektedir. Yağ damlasının yükü yalnız fazla ya da eksik elektronlardan oluşmaktadır.\n(g = 10 m/s², elektronun yük büyüklüğü e = 1,6 × 10⁻¹⁹ C)\nBuna göre, damlada kaç tane fazla elektron vardır?',
 dogru=n11,yan=[(50,'Levha aralığını 2 cm = 0,2 m almıştır; alan 2000 V/m çıkar ve elektron sayısı 50 olur.','islem'),(250,'Alanı V/d yerine V alıp uzaklığı hesaba katmamıştır: q = mg/V → 250 elektron.','bilgi'),(500,'Uzaklığı cm olarak bırakmıştır: E = 400 ÷ 2 = 200 V/m ve elektron sayısı 500 olur.','islem'),(12500,'Alanı V × d = 8 diye hesaplamıştır; elektron sayısı 12 500 çıkar.','bilgi')],
 istenen='Damladaki fazla elektron sayısı.',ip=['Damla durgun olduğuna göre damlaya etki eden kuvvetlerin bileşkesini yaz; alan şiddetini levha verilerinden bul.'],bilgi=[B_DEN,B_ALAN],
 ad=[A('Alanı bul','Uzaklığı metreye çevirip E = V/d yaz.','E = 400 ÷ 0,02 = 20 000 V/m'),A('Denge şartını yaz','Elektriksel kuvvet ağırlığa eşit olmalıdır.','qE = mg'),A('Yükü hesapla','Değerleri yerine koy.','q = 1,6 × 10⁻¹⁴ ÷ 20 000 = 8 × 10⁻¹⁹ C'),A('Elektron sayısı','Yükü elektronun yük büyüklüğüne böl.','n = 8 × 10⁻¹⁹ ÷ 1,6 × 10⁻¹⁹ = 5')],
 puf='Yüklü damla dengedeyse qE = mg; bulduğun yükü e’ye bölerek elektron sayısına geç.',sekil=sk)
# ================= 12 · zor · q–V grafiği + seri + enerji =================
gb=('\\addplot[thick,vurgu] coordinates {(0,0) (8,32)}; \\node[font=\\small\\bfseries,above left] at (axis cs:7.9,32) {K};\n'
    '\\addplot[thick,black] coordinates {(0,0) (4,48)}; \\node[font=\\small\\bfseries,above left] at (axis cs:3.9,48) {L};\n')
sk=pg(8,56,'0,1,2,3,4,5,6,7,8','0,8,16,24,32,40,48,56','$V$ (volt)','$q$ ($\\mu$C)',gb)
CKg=Fr(32,8); CLg=Fr(48,4); Cs=CKg*CLg/(CKg+CLg); Vs=16; qs=Cs*Vs; UL=qs**2/(2*CLg); UK=qs**2/(2*CKg); Ut=Fr(1,2)*Cs*Vs**2; Upar=Fr(1,2)*CLg*Vs**2
assert (CKg,CLg,Cs,qs)==(4,12,3,48) and UL==96 and UK==288 and Ut==384 and Upar==1536
q('0012',8,z='zor',kalip='grafik',tipId='siga-grafik',tip='Sığaç grafikleri ve enerji',kaz='Yük–gerilim grafiğinden sığaları bulup seri bağlı sığaçlarda enerjiyi hesaplar.',
 metin='Yüksüz K ve L sığaçlarının yük–gerilim grafikleri şekildeki gibidir. Bu sığaçlar birbirine seri bağlanıp potansiyel farkı 16 V olan bir üretece bağlanıyor ve yük akışı sona eriyor.\nBuna göre, L sığacında depolanan enerji kaç μJ’dür?',
 dogru=UL,yan=[(48,'Seri kolun yükünü (48 μC) enerji olarak yazmıştır.','dikkat'),(288,'K sığacında depolanan enerjiyi (q² ÷ 2C_K = 288 μJ) L’ninki sanmıştır.','dikkat'),(384,'Devrenin toplam enerjisini (½ × 3 × 256 = 384 μJ) L sığacının enerjisi saymıştır.','dikkat'),(1536,'L’nin uçlarındaki gerilimi 16 V almıştır: ½ × 12 × 256 = 1536 μJ; seri bağlamada gerilimin paylaşıldığını unutmuştur.','bilgi')],
 istenen='L sığacında depolanan enerji (μJ).',ip=['Grafiklerin eğiminin hangi büyüklüğü verdiğini düşün; seri bağlı sığaçlarda ortak olan niceliği bul.'],bilgi=[B_SIG,B_BAG,B_ENJ],
 ad=[A('Sığaları oku','Grafikte eğim q/V = C’dir.','C_K = 32 ÷ 8 = 4 μF · C_L = 48 ÷ 4 = 12 μF'),A('Eşdeğer sığa','Seri bağlı sığaçların eşdeğeri çarpım bölü toplamdır.','C = 4 × 12 ÷ 16 = 3 μF'),A('Ortak yük','Seride her sığaçtaki yük toplam yüke eşittir.','q = 3 × 16 = 48 μC'),A('L’nin enerjisi','Enerjiyi yük ve sığa ile yaz.','U_L = q² ÷ 2C_L = 2304 ÷ 24 = 96 μJ')],
 puf='Seri sığaçlarda yük ortaktır; bir sığacın enerjisi U = q²/2C ile doğrudan bulunur.',sekil=sk)
# ================= 13 · zor · ayrılmış sığaca dielektrik =================
W,D=3.0,1.5
sk=fig(plates(W,D),f'\\node[below] at ({W/2},-.35) {{$C=6\\,\\mu$F, $V=20$ V}};',
       f'\\draw[thick,fill=gray!25] ({W+.5},0.08) rectangle ({W+2.1},{D-.08}); \\node at ({W+1.3},{D/2}) {{$\\kappa=4$}}; \\draw[vurgu,very thick,{ARR}] ({W+.4},{D/2}) -- ({W-.5},{D/2});')
C13,V13,k13=6,20,4; q13=C13*V13; Cn=k13*C13; Vn=Fr(q13,Cn); Un=Fr(1,2)*Cn*Vn**2
assert q13==120 and Cn==24 and Vn==5 and Un==300 and Fr(1,2)*C13*V13**2==1200
assert Fr(1,2)*C13*Vn**2==Fr(75,1) and C13*V13**2==2400 and Fr(1,2)*Cn*V13**2==4800
W13=Fr(1,2)*C13*V13**2-Un
assert W13==900 and Un+Fr(1,2)*C13*V13**2==1500 and Fr(1,2)*Cn*V13**2-Fr(1,2)*C13*V13**2==3600
q('0013',6,z='zor',kalip='şekilli',tipId='siga-yuk',tip='Sığaçta yük–gerilim–enerji değişimi',kaz='Üreteçten ayrılmış sığaca dielektrik konurken enerji değişiminden elektriksel kuvvetlerin yaptığı işi hesaplar.',
 metin='Sığası ve levhaları arasındaki potansiyel fark şekilde verilen paralel levhalı bir sığaç üreteçle yüklendikten sonra üreteçten ayrılmıştır. Daha sonra dielektrik katsayısı şekilde verilen bir yalıtkan levha, levhaların arasını tamamen dolduracak biçimde yavaşça yerleştiriliyor.\nBuna göre, yalıtkan levha yerleştirilirken sığaç üzerinde elektriksel kuvvetlerin yaptığı iş kaç μJ’dür?',
 dogru=W13,yan=[(300,'Son durumdaki enerjiyi (½ × 24 × 25 = 300 μJ) iş saymıştır.','dikkat'),(1200,'İlk enerjiyi (½ × 6 × 400 = 1200 μJ) iş saymıştır.','dikkat'),(1500,'İlk ve son enerjiyi toplamıştır: 1200 + 300 = 1500 μJ.','islem'),(3600,'Gerilimin 20 V’ta sabit kaldığını varsaymıştır: ½ × 24 × 400 − 1200 = 3600 μJ.','bilgi')],
 istenen='Elektriksel kuvvetlerin yaptığı iş (μJ).',ip=['Üreteçten ayrılmış sığaçta hangi niceliğin korunduğunu belirle; ilk ve son enerjileri bu nicelikle karşılaştır.'],bilgi=[B_YUK,B_SIG,B_ENJ],
 ad=[A('Yükü bul','İlk durumda q = CV.','q = 6 × 20 = 120 μC'),A('Yeni sığayı bul','Dielektrik sığayı κ katına çıkarır; yük sabit kalır.','C′ = 4 × 6 = 24 μF'),A('Enerjileri hesapla','İlk enerji ½CV², son enerji q²/2C′ ile bulunur.','U₁ = ½ × 6 × 400 = 1200 μJ ; U₂ = 120² ÷ 48 = 300 μJ'),A('İşi bul','Alanın yaptığı iş enerji azalmasına eşittir.','W = 1200 − 300 = 900 μJ')],
 puf='Ayrılmış sığaçta q sabittir.',sekil=sk)
# ================= 14 · zor · yük paylaşımı, enerji kaybı =================
sk=fig(batv(0,3,'$12$ V',wire_to=None),'\\draw[thick] (0,3) -- (.5,3);',sw(.5,3,'S$_1$'),'\\draw[thick] (1.45,3) -- (2.6,3);',dot(2.6,3),capV(2.6,1.5,'C$_1$: $6\\,\\mu$F',3,0),'\\draw[thick] (2.6,3) -- (3.4,3);',sw(3.4,3,'S$_2$'),'\\draw[thick] (4.35,3) -- (5.4,3);',
       capV(5.4,1.5,'C$_2$: $3\\,\\mu$F',3,0),dot(2.6,0),'\\draw[thick] (5.4,0) -- (0,0);')
C1_,C2_,V14=6,3,12; q14=C1_*V14; Vf=Fr(q14,C1_+C2_); Ui=Fr(1,2)*C1_*V14**2; Uf=Fr(1,2)*(C1_+C2_)*Vf**2; kay=Ui-Uf; U2=Fr(1,2)*C2_*Vf**2
assert (q14,Vf,Ui,Uf,kay,U2)==(72,8,432,288,144,96)
q('0014',7,z='zor',kalip='şekilli',tipId='siga-enerji',tip='Sığaçta depolanan enerji',kaz='Yüklü sığacı yüksüz sığaçla birleştirdiğinde yük paylaşımını ve enerji kaybını hesaplar.',
 metin='Şekildeki devrede C₁ ve C₂ sığaçları başlangıçta yüksüzdür; sığaları ve üretecin potansiyel farkı şekilde verilmiştir. Önce yalnız S₁ anahtarı kapatılıyor ve C₁ tam dolunca S₁ açılıyor. Daha sonra S₂ anahtarı kapatılıyor ve yük akışı sona eriyor.\nBuna göre, S₂ kapatıldıktan sonra sığaçlarda depolanan toplam enerji, S₂ kapatılmadan önceki enerjiye göre kaç μJ azalmıştır?',
 dogru=kay,yan=[(72,'C₁’deki yükü (72 μC) enerjideki azalma olarak yazmıştır.','dikkat'),(96,'Yalnız C₂’nin son enerjisini (½ × 3 × 64 = 96 μJ) azalma saymıştır.','dikkat'),(288,'Son durumdaki toplam enerjiyi (288 μJ) azalma sanmıştır.','dikkat'),(432,'İlk enerjiyi (432 μJ) azalma sanmıştır; son enerjiyi çıkarmayı unutmuştur.','dikkat')],
 istenen='Toplam enerjideki azalma (μJ).',ip=['S₂ kapatılınca hangi niceliğin korunduğunu bul; iki durumdaki toplam enerjileri ayrı ayrı hesaplayıp karşılaştır.'],bilgi=[B_BAG,B_ENJ],
 ad=[A('İlk yük ve enerji','C₁ üretece bağlanınca dolar; S₁ açıkken yük sabit kalır.','q = 6 × 12 = 72 μC · U₁ = ½ × 6 × 144 = 432 μJ'),A('Ortak gerilimi bul','Paralel bağlanınca toplam yük korunur, sığalar toplanır.','V = 72 ÷ (6 + 3) = 8 V'),A('Son enerjiyi hesapla','Eşdeğer sığa 9 μF ve gerilim 8 V’tur.','U₂ = ½ × 9 × 64 = 288 μJ'),A('Azalmayı bul','İlk ve son enerjinin farkını al.','ΔU = 432 − 288 = 144 μJ')],
 puf='Yük paylaşımında yük korunur ama enerji korunmaz; fark ısı ve ışıma olarak kaybolur.',sekil=sk)
# ================= 15 · zor · denge sonra d değişir =================
W,D=3.0,1.8
sk=fig(plates(W,D),batv(-1.5,D,'$V$'),f'\\fill[orange!70!black] ({W/2},{D/2}) circle (.14); \\node[right] at ({W/2+.2},{D/2}) {{$q,\\ m$}};',
       f'\\draw[<->,thick] ({W+.45},0) -- ({W+.45},{D}); \\node[right] at ({W+.5},{D/2}) {{$2$ cm}};')
d_a,d_b=2,5; Eratio=Fr(d_a,d_b); net=1-Eratio; a15=net*10
assert a15==6 and Eratio*10==4 and Fr(5,2)*10-10==15 and 10==10
q('0015',3,z='zor',kalip='şekilli',tipId='siga-denge',tip='Dengedeki yüklü cisim ve elektron sayısı',kaz='Üreteç bağlıyken levhalar arası uzaklık değişince dengedeki yüklü cismin ivmesini hesaplar.',
 metin='Şekilde, üretece bağlı paralel levhalar arasında q yüklü, m kütleli bir cisim dengede durmaktadır. Üreteç bağlı kalarak üst levha yukarı çekilip levhalar arasındaki uzaklık 5 cm yapılıyor. Cisim levhalar arasında kalmaktadır ve hava direnci ihmal edilmektedir.\n(g = 10 m/s²)\nBuna göre, uzaklık değiştirildikten hemen sonra cismin ivmesinin büyüklüğü kaç m/s²’dir?',
 dogru=a15,yan=[(0,'Alanın değişmediğini sanıp dengenin korunduğunu düşünmüştür.','bilgi'),(4,'Yalnız elektriksel kuvveti hesaba katmıştır: 0,4mg ÷ m = 4 m/s².','dikkat'),(10,'Elektriksel kuvveti sıfır sanıp ivmeyi yalnız yerçekimine eşitlemiştir: a = g = 10 m/s².','bilgi'),(15,'Uzaklık artınca alanın 5/2 kat arttığını sanmıştır: (2,5mg − mg) ÷ m = 15 m/s².','bilgi')],
 istenen='Cismin ivmesinin büyüklüğü (m/s²).',ip=['İlk durumda kuvvet dengesini yaz; üreteç bağlı olduğuna göre yeni alan şiddetini ilk alanla karşılaştır.'],bilgi=[B_ALAN,B_DEN,B_YUK],
 ad=[A('İlk dengeyi yaz','Cisim durgun; elektriksel kuvvet ağırlığa eşit.','qE = mg'),A('Yeni alanı bul','V sabit, d: 2 cm → 5 cm. E = V/d olduğundan alan küçülür.','E′ = E × 2/5'),A('Yeni kuvveti bul','Elektriksel kuvvet ilk değerinin 2/5’i olur.','F′ = 0,4 mg'),A('İvmeyi hesapla','Net kuvvet ağırlık yönündedir.','m·a = mg − 0,4mg → a = 0,6 × 10 = 6 m/s²')],
 puf='Üreteç bağlıyken sabit olan nicelik V’dir.',sekil=sk)
# ================= 16 · orta · öncüllü · hızlandırılan parçacıklar =================
Wd,Hd=4.0,3.0
sk=fig(f'\\draw[very thick] (0,0) -- (0,{Hd}); \\draw[very thick] ({Wd},0) -- ({Wd},{Hd}); \\node at (0,{Hd+.25}) {{$+$}}; \\node at ({Wd},{Hd+.25}) {{$-$}};',
       f'\\draw[thick] (0,0) -- (0,-.9) -- (1.7,-.9); \\draw[thick] ({Wd},0) -- ({Wd},-.9) -- (1.95,-.9); \\draw[very thick] (1.7,-1.2) -- (1.7,-.6); \\draw[very thick] (1.95,-1.05) -- (1.95,-.75); \\node[below] at (2.0,-1.0) {{$V$}}; \\node[font=\\footnotesize] at (1.5,-.62) {{$+$}};',
       f'\\fill[orange!70!black] (.3,2.2) circle (.12); \\node[right] at (.5,2.2) {{K: $+e,\\ m$}};',f'\\fill[orange!70!black] (.3,.9) circle (.12); \\node[right] at (.5,.9) {{L: $+3e,\\ 9m$}};')
EkK=Fr(1); EkL=Fr(3); aK=Fr(1,1); aL=Fr(3,9)
tL_over_tK=(aK/aL)**Fr(1,2)
assert EkL==3*EkK and aL<aK and (aK/aL)==3   # t ∝ 1/√a → t_L = √2 t_K, süreler eşit değil
tr={'I':True,'II':False,'III':False}
rs={'I':'Kinetik enerji kazancı Ek = qV’dir; V aynı, L’nin yükü 3 katı olduğundan Ek_L = 3·Ek_K olur.','II':'a_L = 3eE/9m = a_K/3 olduğundan L daha yavaş hızlanır ve d = ½at² bağıntısına göre levhaya daha geç ulaşır; süreler eşit değildir.','III':'a = qE/m bağıntısına göre a_K = eE/m, a_L = 3eE/9m = a_K/3’tür; L’nin ivmesi K’ninkinden küçüktür.'}
S16=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III']
d16,y16,ad16=onc(tr,rs,S16)
q('0016',2,z='orta',kalip='öncüllü',tipId='siga-parcacik',tip='Düzgün alanda yüklü parçacık hareketi',kaz='Düzgün alanda durgun hâlden hızlanan iki parçacığın kinetik enerji, süre ve ivmesini karşılaştırır.',
 metin='Şekildeki paralel levhalar arasına, yükleri ve kütleleri şekilde verilen K ve L parçacıkları, pozitif levhanın yüzeyinden aynı anda durgun hâlde bırakılıyor ve her ikisi de negatif levhaya ulaşıyor. Parçacıkların ağırlıkları ve aralarındaki etkileşim ihmal edilmektedir.\nBuna göre;\nI. Negatif levhaya ulaştıklarında L’nin kinetik enerjisi K’ninkinin 3 katıdır.\nII. Negatif levhaya ulaşma süreleri eşittir.\nIII. L’nin ivmesi K’ninkinden büyüktür.\nyargılarından hangileri doğrudur?',
 dogru=d16,yan=y16,sira=S16,istenen='Doğru olan yargılar.',ip=['Kinetik enerji kazancını alanın yaptığı işle, ivmeyi ise kuvvet ve kütle ile ilişkilendirerek iki parçacığı karşılaştır.'],bilgi=[B_KUV],ad=ad16,
 puf='Aynı levhalar arasında Ek = qV; ivme a = qE/m ile bulunur.',sekil=sk)
# ================= 17 · orta · öncüllü · özdeş üç sığaç =================
sk=fig(batv(0,3,'$V$',wire_to=None),'\\draw[thick] (0,3) -- (.7,3);',capH(1.3,3,'K: $C$'),'\\draw[thick] (1.9,3) -- (5.2,3);',dot(3.2,3),dot(3.2,0),
       capV(3.2,1.5,'L: $C$',3,0),capV(5.2,1.5,'M: $C$',3,0),'\\draw[thick] (5.2,0) -- (0,0);')
Cc=Fr(1); Vt=Fr(1); Cpp=2*Cc; Cs17=Cc*Cpp/(Cc+Cpp); qtot=Cs17*Vt; qK=qtot; V23=qtot/Cpp; qL=Cc*V23; qM=qL; VK=qtot/Cc
UK17=Fr(1,2)*Cc*VK**2; UL17=Fr(1,2)*Cc*V23**2
assert qK==Fr(2,3) and qL==Fr(1,3) and qL==qM and qK==2*qL and UK17==4*UL17
tr={'I':False,'II':True,'III':False}
rs={'I':'K’nin yükü, L ve M’nin yüklerinin toplamına eşittir: q_K = q_L + q_M = 2q_L; K’nin yükü L’ninkinin 2 katıdır.','II':'L ve M paralel bağlı ve özdeştir; aynı gerilimde aynı yükü depolarlar.','III':'V_K = 2V_L olduğundan U = ½CV² bağıntısına göre U_K = 4U_L olur; 2 katı değildir.'}
S17=['Yalnız I','Yalnız II','Yalnız III','I ve III','II ve III']
d17,y17,ad17=onc(tr,rs,S17)
q('0017',5,z='orta',kalip='öncüllü',tipId='siga-bagla',tip='Seri ve paralel bağlı sığaçlar',kaz='Özdeş sığaçlı karışık devrede yük, gerilim ve enerji ilişkilerini karşılaştırır.',
 metin='Başlangıçta yüksüz olan özdeş K, L ve M sığaçları şekildeki gibi bir üretece bağlanıyor ve yük akışı sona eriyor.\nBuna göre;\nI. K sığacının yükü L sığacının yüküne eşittir.\nII. L ve M sığaçlarının yükleri eşittir.\nIII. K sığacında depolanan enerji, L sığacında depolanan enerjinin 2 katıdır.\nyargılarından hangileri doğrudur?',
 dogru=d17,yan=y17,sira=S17,istenen='Doğru olan yargılar.',ip=['Ana koldaki ve paralel kollardaki yük ilişkisini yaz; gerilimleri sığa ve yük cinsinden karşılaştır.'],bilgi=[B_BAG,B_ENJ],ad=ad17,
 puf='Seri–paralel karışık devrede hangi niceliğin hangi kolda ortak olduğunu belirle.',sekil=sk)
# ================= 18 · orta · iş =================
W,D=4.2,3.0; u=D/6
yK=D-1*u; yL=D-4*u
sk=fig(plates(W,D),batv(-1.5,D,'$120$ V'),''.join(f'\\draw[vurgu,thick,{ARR}] ({x},{D-.2}) -- ({x},.2);' for x in (.45,1.8,3.7)),
       f'\\fill (1.1,{yK}) circle (.08); \\node[above] at (1.1,{yK}) {{K}}; \\fill (2.8,{yL}) circle (.08); \\node[above] at (2.8,{yL}) {{L}};',
       f'\\draw[dashed] (2.8,{yL}) -- ({W+.6},{yL}); \\draw[dashed] (1.1,{yK}) -- ({W+.1},{yK});',
       f'\\draw[<->,thick] ({W+.1},{D}) -- ({W+.1},{yK}); \\node[right,font=\\footnotesize] at ({W+.15},{(D+yK)/2+.0}) {{$1$ cm}};',
       f'\\draw[<->,thick] ({W+.9},{D}) -- ({W+.9},{yL}); \\node[right,font=\\footnotesize] at ({W+.95},{(D+yL)/2}) {{$4$ cm}};',
       f'\\draw[<->,thick] ({W+2.0},{D}) -- ({W+2.0},0); \\node[right,font=\\footnotesize] at ({W+2.05},{D/2}) {{$6$ cm}};',
       f'\\draw[dashed] ({W+.6},0) -- ({W+2.1},0);')
V18,d18=120,Fr(6,100); E18=V18/d18; dV=E18*Fr(3,100); W18=3*dV
assert E18==2000 and dV==60 and W18==180
assert 3*E18*Fr(1,100)==60 and 3*E18*Fr(4,100)==240 and 3*E18*Fr(5,100)==300 and 3*V18==360
q('0018',1,z='orta',kalip='şekilli',tipId='siga-alan',tip='Levhalar arası düzgün alan ve potansiyel',kaz='Düzgün alanda iki nokta arasındaki potansiyel farkından alanın yaptığı işi hesaplar.',
 metin='Şekilde, potansiyel farkı verilen yatay paralel levhalar arasında düzgün bir elektrik alan vardır; K ve L noktalarının üst levhaya olan uzaklıkları ile levhalar arasındaki uzaklık şekilde gösterilmiştir. Yükü +3 μC olan noktasal bir cisim, K noktasından L noktasına götürülüyor.\nBuna göre, bu sırada elektrik alanın cisim üzerinde yaptığı iş kaç μJ’dür?',
 dogru=W18,yan=[(60,'Üst levha ile K arasındaki 1 cm’yi kullanmış: 2000 × 0,01 = 20 V ve 3 × 20 = 60 μJ.','dikkat'),(240,'L’nin üst levhaya uzaklığını (4 cm) kullanmış: 2000 × 0,04 = 80 V ve 3 × 80 = 240 μJ.','dikkat'),(300,'Uzaklıkları toplamış: 1 + 4 = 5 cm için 100 V ve 3 × 100 = 300 μJ.','islem'),(360,'Levhalar arasındaki tüm potansiyel farkı (120 V) almıştır: 3 × 120 = 360 μJ.','bilgi')],
 istenen='Elektrik alanın yaptığı iş (μJ).',ip=['Önce alan şiddetini bul; K ve L noktaları arasındaki potansiyel farkını yalnız alan doğrultusundaki uzaklık farkından hesapla.'],bilgi=[B_ALAN],
 ad=[A('Alanı bul','Levhalar arası uzaklığı metreye çevirip E = V/d yaz.','E = 120 ÷ 0,06 = 2000 V/m'),A('Uzaklık farkını bul','Potansiyel farkı alan doğrultusundaki uzaklığa bağlıdır.','Δd = 4 − 1 = 3 cm = 0,03 m'),A('Potansiyel farkı bul','ΔV = E · Δd.','ΔV = 2000 × 0,03 = 60 V'),A('İşi hesapla','Alanın yaptığı iş yük ile potansiyel farkın çarpımıdır.','W = 3 × 60 = 180 μJ')],
 puf='İki nokta arasındaki potansiyel farkı yalnız alan doğrultusundaki uzaklık farkına bağlıdır: ΔV = E·Δd.',sekil=sk)
# ================= 19 · zor · V–d grafiği =================
gb=('\\addplot[thick,vurgu] coordinates {(0,0) (5,75)};\n\\addplot[only marks,mark=*,mark size=2pt] coordinates {(2,30) (4,60)};\n'
    '\\draw[dashed] (axis cs:2,0) -- (axis cs:2,30) -- (axis cs:0,30); \\draw[dashed] (axis cs:4,0) -- (axis cs:4,60) -- (axis cs:0,60);\n')
sk=pg(5,75,'0,1,2,3,4,5','0,15,30,45,60,75','$d$ (cm)','$V$ (volt)',gb)
q19=6; V19a,V19b=30,60; U19a=Fr(1,2)*q19*V19a; U19b=Fr(1,2)*q19*V19b; W19=U19b-U19a
assert (U19a,U19b,W19)==(90,180,90) and q19*(V19b-V19a)==180 and q19*V19b==360 and V19b-V19a==30
q('0019',8,z='zor',kalip='grafik',tipId='siga-grafik',tip='Sığaç grafikleri ve enerji',kaz='V–d grafiğinden enerji değişimini hesaplayarak dış kuvvetin yaptığı işi bulur.',
 metin='Yükü 6 μC olan paralel levhalı bir sığaç üreteçten ayrılmıştır. Levhalar paralel kalacak biçimde aralarındaki uzaklık d değiştirilirken levhalar arasındaki potansiyel fark V ölçülüyor ve V–d grafiği şekildeki gibi çiziliyor.\nBuna göre, levhalar arasındaki uzaklık 2 cm’den 4 cm’ye çıkarılırken dış kuvvetin sığaç üzerinde yaptığı iş kaç μJ’dür?',
 dogru=W19,yan=[(30,'Potansiyel fark değişimini (60 − 30 = 30 V) iş olarak yazmıştır.','dikkat'),(60,'Son potansiyel farkı (60 V) iş sanmıştır.','dikkat'),(180,'½ çarpanını unutmuştur: q·ΔV = 6 × 30 = 180 μJ.','islem'),(360,'Son durumda q·V = 6 × 60 = 360 μJ hesaplamış, ½ ve ilk enerjiyi unutmuştur.','islem')],
 istenen='Dış kuvvetin yaptığı iş (μJ).',ip=['Üreteçten ayrılmış sığaçta enerji değişimi dış kuvvetin işine eşittir; iki uzaklık için depolanan enerjileri grafikteki değerlerle bul.'],bilgi=[B_ENJ,B_YUK],
 ad=[A('Grafikten oku','Noktalardaki potansiyel farkları oku.','d = 2 cm için 30 V; d = 4 cm için 60 V'),A('İlk enerjiyi bul','Enerji U = ½qV ile hesaplanır.','U₁ = ½ × 6 × 30 = 90 μJ'),A('Son enerjiyi bul','Yük sabittir.','U₂ = ½ × 6 × 60 = 180 μJ'),A('İşi hesapla','Dış kuvvetin işi enerji artışına eşittir.','W = 180 − 90 = 90 μJ')],
 puf='Ayrılmış sığaçta q sabittir.',sekil=sk)
# ================= 20 · orta · kısmi dielektrik =================
W,D=3.6,1.6
sk=fig(plates(W,D),batv(-1.5,D,'$10$ V'),f'\\fill[gray!25] ({W/2},.04) rectangle ({W},{D-.04}); \\draw[thick] ({W/2},.04) -- ({W/2},{D-.04}); \\node at ({W*.75},{D/2}) {{$\\kappa=3$}}; \\node at ({W*.25},{D/2}) {{hava}};')
C20,k20,V20=4,3,10; C20h=Fr(C20,2); C20d=k20*C20h; Ct=C20h+C20d; q20=Ct*V20
assert Ct==8 and q20==80 and C20*V20==40 and C20d*V20==60 and k20*C20*V20==120 and (C20+k20*C20)*V20==160
q('0020',4,z='orta',kalip='şekilli',tipId='siga-sigac',tip='Sığanın bağlı olduğu nicelikler',kaz='Levhalar arasının yarısı dielektrikle dolu sığacın sığasını ve yükünü hesaplar.',
 metin='Levhaları arasında hava varken sığası 4 μF olan paralel levhalı bir sığacın levhalarının alanının yarısı kadar kısım, şekildeki gibi dielektrik katsayısı verilen bir yalıtkanla dolduruluyor ve sığaç şekildeki üretece bağlanıyor. Yük akışı sona eriyor.\nBuna göre, sığaçta depolanan yük kaç μC’dur?',
 dogru=q20,yan=[(40,'Dielektriğin etkisini hesaba katmamıştır: 4 × 10 = 40 μC.','dikkat'),(60,'Yalnız dielektrikli yarının sığasını (6 μF) almıştır: 6 × 10 = 60 μC.','dikkat'),(120,'Dielektriğin tüm levhalar arasını doldurduğunu sanmıştır: 3 × 4 × 10 = 120 μC.','bilgi'),(160,'Havalı kısmı 4 μF, dielektrikli kısmı 12 μF alıp toplamıştır: 16 × 10 = 160 μC.','islem')],
 istenen='Sığaçta depolanan yük (μC).',ip=['Levha alanının iki bölgesini ayrı ayrı değerlendir; her bölgenin sığaya nasıl katkı yaptığını düşün.'],bilgi=[B_SIG,B_BAG],
 ad=[A('Bölgeleri ayır','Alanın yarısı hava, yarısı dielektriklidir; ikisi de aynı levhalar arasında olduğundan paralel bağlı iki sığaç gibidir.','C_hava ∥ C_diel'),A('Sığaları bul','Alan yarılanınca sığa yarılanır; dielektrik κ katına çıkarır.','C_hava = 4 ÷ 2 = 2 μF · C_diel = 3 × 2 = 6 μF'),A('Eşdeğer sığa','Paralel bağlı sığaçlar toplanır.','C = 2 + 6 = 8 μF'),A('Yükü hesapla','q = CV.','q = 8 × 10 = 80 μC')],
 puf='Levha alanının bölgelerini ayrı ayrı düşün.',sekil=sk)
# ================= yaz =================
def bitir_af():
    for qq in P.ANA: qq['kardes']=None
    P.yaz(os.path.join(GD,'siga-1.json'),'/tmp/bos-siga.json')
    tipler={}
    for c in KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=KK))['kartlar'].append(c['id'])
    json.dump(dict(konu=KONUAD,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2018–2026 Fizik (yalnız mantık), MEB 12. sınıf fizik müfredatı.',kartlar=KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar','afsiga.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler))
bitir_af()
