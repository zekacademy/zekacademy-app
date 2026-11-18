"""AYT Matematik · Binom ve Olasılık (20 soru): binom açılımı, Pascal üçgeni, koşullu/bağımsız olasılık, ağaç, sayma ve tekrarlı deneme.
Her doğru ve çeldirici değer kodla (kaba kuvvet / sympy) hesaplanıp assert edilir. Kardeş yok, ipucu 1."""
import sys,os
HD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(HD,'..')
sys.path.insert(0,os.path.join(HV,'tyt-mat')); sys.path.insert(0,HV)
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
from itertools import product,combinations
from math import comb
import sympy as sp
H.KONU='Binom ve Olasılık'
HD=os.path.dirname(os.path.abspath(__file__))
SCR='/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/binom'; os.makedirs(SCR,exist_ok=True)
UK='amat|Binom ve Olasılık'
P=Parti('binom','Binom ve Olasılık',UK,ders='AYT Matematik',idon='aytmat')
KY='ÖSYM 2018–2026 AYT Matematik (binom açılımı ve olasılık soruları; yalnız mantık) · Bilgi Sarmal AYT denemeleri · MEB 11–12. sınıf'
def fs(x):
    x=Fr(x); s=('−' if x<0 else '')+(str(abs(x.numerator)) if x.denominator==1 else f'{abs(x.numerator)}/{x.denominator}'); return s
def q(no,ad,dogru,yan,**k):
    """Sayısal soru: değerler Fraction/int; şıklar küçükten büyüğe, kesirler a/b."""
    vals=[Fr(dogru)]+[Fr(y[0]) for y in yan]; assert len(set(vals))==5,vals
    sira=[fs(v) for v in sorted(vals)]
    mk(P,no,ad=ad,adim=len(ad),dogru=fs(dogru),yan=[(fs(y[0]),y[1],y[2]) for y in yan],sira=sira,**k)
def qo(no,ad,dogru,yan,sira,**k):
    mk(P,no,ad=ad,adim=len(ad),dogru=dogru,yan=yan,sira=sira,**k)
def fig(body,font='\\small'): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font='+font+']\n'+body+'\n\\end{tikzpicture}')
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,ky=KY): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,ky)
def tf(x): # TikZ kesir
    x=Fr(x); return f'${x.numerator}$' if x.denominator==1 else f'${x.numerator}/{x.denominator}$'
OS3=['Yalnız I','Yalnız II','I ve II','I ve III','II ve III']
def kume(t): 
    L=[r for r,v in zip(['I','II','III'],t) if v]
    return 'Yalnız '+L[0] if len(L)==1 else ' ve '.join(L) if len(L)==2 else 'I, II ve III'

# ---------- bilgi kutuları (yalnız tanım ve gösterim; örnekler soruların kurgusundan farklı) ----------
BIN=B('Binom açılımı','(a + b)ⁿ açılımında genel terim C(n, k) · aⁿ⁻ᵏ · bᵏ biçimindedir (k = 0, 1, …, n); C(n, k) = n! / (k! · (n − k)!). Örnek: (m + 3)⁴ açılımında k = 1 için terim C(4, 1) · m³ · 3 = 12m³')
KAT=B('Katsayılar toplamı','bir polinomda x yerine 1 yazılınca katsayıların toplamı elde edilir. Örnek: (2x + 1)³ açılımının katsayılar toplamı (2 + 1)³ = 27; sabit terim ise x = 0 yazılarak ya da x’siz terimden bulunur: 1')
SAB=B('Sabit terim','genel terimde x’in kuvveti 0 olan terimdir. Üslü ifadelerde xᵐ · xᵖ = xᵐ⁺ᵖ ve 1/xᵖ = x⁻ᵖ kuralları kullanılır. Örnek: (x² + 1/x)ⁿ ifadesinde k. terimin x’li kısmı x²⁽ⁿ⁻ᵏ⁾ · x⁻ᵏ = x²ⁿ⁻³ᵏ olur')
PAS=B('Pascal üçgeni','üçgenin n. satırı (satırlar 0’dan başlar) C(n, 0), C(n, 1), …, C(n, n) sayılarından oluşur; her sayı, bir üst satırdaki iki komşusunun toplamıdır: C(n, k) = C(n − 1, k − 1) + C(n − 1, k). Örnek: 3. satır 1, 3, 3, 1; 4. satırın ortadaki sayısı 3 + 3 = 6')
PAK=B('Pascal üçgeninde köşegen','üçgenin aynı sütun numarasını izleyen sayıları aşağı doğru C(k, k), C(k + 1, k), C(k + 2, k), … biçimindedir. Örnek: C(2, 2) + C(3, 2) + C(4, 2) = 1 + 3 + 6 = 10')
ORN=B('Ardışık binom katsayıları','C(n, k) = n! / (k! (n − k)!) olduğundan ardışık iki katsayı arasında n ve k’ya bağlı sade bir oran vardır. Örnek: C(7, 3) / C(7, 2) = 35 / 21 = 5/3')
KOS=B('Koşullu olasılık','B olayı gerçekleştiği bilindiğinde A’nın olasılığı P(A | B) = P(A ∩ B) / P(B) kadardır; eş olasılıklı durumlarda sonuçlar sayılır: P(A | B) = s(A ∩ B) / s(B). Örnek: 20 kişilik bir grupta 8 kişi gözlüklü, bunların 2’si öğretmense gözlüklüler arasından öğretmen seçme olasılığı 2/8’dir')
BAG=B('Bağımsız olaylar','bir olayın gerçekleşmesi diğerinin olasılığını değiştirmiyorsa olaylar bağımsızdır; bu durumda P(A ∩ B) = P(A) · P(B) olur. Örnek: P(A) = 1/2, P(B) = 1/5 ve olaylar bağımsızsa P(A ∩ B) = 1/10’dur. Birlikte gerçekleşebilen olaylar ayrık değildir')
AGA=B('Ağaç şeması ve toplam olasılık','ağaçta bir yolun olasılığı, o yoldaki dal olasılıklarının çarpımıdır; bir sonuca götüren bütün yolların olasılıkları toplanır. Örnek: ilk dal 1/2, ardından dal 1/3 ise bu yolun olasılığı 1/6’dır; aynı sonuca götüren başka bir yol 1/10 ise toplam olasılık 1/6 + 1/10 = 4/15 olur')
BAY=B('Koşullu olasılık ve ağaç','“sonuç bilindiğinde kaynağın olasılığı” P(kaynak | sonuç) = (kaynak üzerinden o sonuca giden yolun olasılığı) / (o sonuca giden bütün yolların toplamı) biçiminde hesaplanır. Örnek: bir sonuca iki yoldan 1/10 ve 1/15 olasılıkla ulaşılıyorsa ilk yoldan gelmiş olma olasılığı (1/10) / (1/10 + 1/15) = 3/5’tir')
KOM=B('Kombinasyonla olasılık','n elemanlı kümeden k eleman seçmenin C(n, k) farklı yolu vardır; aynı anda çekilen nesnelerde sıra önemli değildir. Olasılık = istenen seçimlerin sayısı / bütün seçimlerin sayısı. Örnek: 5 kırmızı, 3 mavi topluk torbadan 2 top çekilirken ikisinin de mavi olma olasılığı C(3, 2) / C(8, 2) = 3/28’dir')
TEK=B('Tekrarlı bağımsız denemeler','her denemede bir olayın olasılığı p ise n denemede o olayın tam k kez gerçekleşme olasılığı C(n, k) · pᵏ · (1 − p)ⁿ⁻ᵏ’dır. Örnek: p = 1/5 ile 3 denemede tam 1 kez gerçekleşme olasılığı C(3, 1) · (1/5) · (4/5)² = 48/125’tir')
YOL=B('Yol sayma ve olasılık','her yolun eş olasılıklı seçildiği durumda olasılık, istenen yolların sayısının bütün yolların sayısına oranıdır. Bir noktadan geçen yolların sayısı, iki parçanın yol sayılarının çarpımıdır. Örnek: 2 sağ, 2 yukarı adımla gidilen yollar C(4, 2) = 6 tanedir')
OZ=B('Binom açılımının özellikleri','(a + b)ⁿ açılımında n + 1 terim vardır; katsayılar toplamı değişkenlere 1 verilerek bulunur. İki açılımın çarpımında bir xᵐ’li terim, çarpanlardaki üslerin toplamı m olan terimlerin çarpımlarının toplamından gelir. Örnek: (1 + x)² (1 + x)³ çarpımında x² katsayısı 1 · 3 + 2 · 3 + 1 · 1 = 10’dur')

DUR_B=B('Eş olasılıklı durumlar','n tane bağımsız ve her biri iki durumlu (yanık/sönük, yazı/tura gibi) nesnenin 2ⁿ eş olasılıklı durumu vardır; olasılık, uygun durumların sayısının 2ⁿ’ye oranıdır. Örnek: 3 madeni para atıldığında 2³ = 8 durum vardır ve hepsinin yazı gelmesi 1/8’dir')

# ---------- kartlar ----------
kartla('K-ABO-01','Genel terimle belirli terim ve parametre','Genel terimde değişkenin kuvveti istenen kuvvete eşitlenerek k bulunur; k ile katsayı ya da parametre hesaplanır.','k’yı bir kaydırmak; ikinci terimin kuvvetini (işaret ve sayı katsayısı dahil) unutmak; üslü parametreden kök alırken yanlış kuvvet kullanmak.','orta','düz',3,'bn-terim','Binom açılımında terim ve parametre')
kartla('K-ABO-02','Pascal üçgeni ve katsayı ilişkileri','Üçgendeki konum C(n, k) ile eşlenir; toplama kuralı, köşegen toplamı ve ardışık katsayı oranları kullanılır.','Satır numarasını 0 yerine 1’den başlatmak; köşegen toplamında bir alt satırı ya da bir sonraki sütunu karıştırmak.','orta','şekilli',3,'bn-pascal','Pascal üçgeni ve ardışık katsayılar')
kartla('K-ABO-03','Binom özellikleri ve açılım çarpımı','Terim sayısı, katsayılar toplamı, sabit terim yargıları ayrı ayrı sınanır; iki açılımın çarpımında üs toplamı istenen kuvvete eşit olan terim çiftleri toplanır.','Terim sayısını n sanmak; katsayılar toplamında yanlış değer kullanmak; çarpımda bir terim çiftini atlamak ya da işareti kaçırmak.','zor','öncüllü',4,'bn-ozellik','Binom açılımının özellikleri ve çarpımı')
kartla('K-ABO-04','Koşullu olasılık (çizelge, şema, sayma)','Örnek uzay çizelge, Venn şeması ya da sayma ile kurulur; koşul örnek uzayı daraltır, olasılık daralan uzayda hesaplanır.','Paydayı yanlış alıp P(A | B) ile P(B | A)’yı karıştırmak; birleşim için olasılıkları kesişimi çıkarmadan toplamak.','orta','şekilli',3,'ol-kosullu','Koşullu olasılık')
kartla('K-ABO-05','Bağımsız olaylar ve bağımsızlık koşulu','P(A ∩ B) = P(A) · P(B) koşulu tablo ya da kutu verisine uygulanır; bilinmeyen bu eşitlikten bulunur.','Kesişimi boş olmayan olayları bağımsız sanmak; çapraz çarpımda yanlış hücreleri eşleştirmek.','orta','tablo',3,'ol-bagimsiz','Bağımsız olaylar')
kartla('K-ABO-06','Ağaç şeması: toplam olasılık ve Bayes','Dal olasılıkları çarpılır, aynı sonuca giden yollar toplanır; koşullu sorularda ilgili yol toplama bölünür.','Yalnız bir kolu almak; dal olasılıklarını toplamak; koşullu olasılıkta paydayı kaynağın olasılığı almak.','zor','hikâyeli',4,'ol-agac','Ağaç şeması ve koşullu olasılık')
kartla('K-ABO-07','Sayma yöntemleriyle olasılık','Elverişli ve bütün durumlar kombinasyon, yol sayma ya da liste ile sayılır; kısıtlar sayımdan önce uygulanır.','Sırayı karıştırmak; kısıtı sayımın bir kısmında unutmak; payda ile payı farklı evrenlerde saymak.','zor','hikâyeli',4,'ol-sayma','Sayma ile olasılık')
kartla('K-ABO-08','Tekrarlı bağımsız denemeler','C(n, k) pᵏ (1 − p)ⁿ⁻ᵏ kalıbı kurulur; p, şema ya da çarktan okunur; “tam k” ile “en az k” ayrılır.','C(n, k) çarpanını unutmak; q yerine p yazmak; “en az” ile “tam”ı karıştırmak.','orta','şekilli',3,'ol-tekrar','Tekrarlı bağımsız denemeler')

# ================= şekil yardımcıları =================
def pascal_fig(rows,gizli,boyali=(),etiket=True,font='\\small'):
    w,h=0.95,0.78; o=[]
    for r in range(rows):
        if etiket: o.append(f'\\node[font=\\scriptsize,anchor=east,gray!70!black] at ({-(rows-1)/2*w-0.55:.2f},{-r*h:.2f}) {{{r}. satır}};')
        for k in range(r+1):
            x=(k-r/2)*w; y=-r*h
            if (r,k) in gizli: o.append(f'\\node[draw,thick,rounded corners=2pt,fill=orange!35,minimum width=0.62cm,minimum height=0.55cm,inner sep=1pt,font=\\bfseries] at ({x:.2f},{y:.2f}) {{{gizli[(r,k)]}}};')
            elif (r,k) in boyali: o.append(f'\\node[draw,thick,rounded corners=2pt,fill=green!30,minimum width=0.62cm,minimum height=0.55cm,inner sep=1pt,font=\\bfseries] at ({x:.2f},{y:.2f}) {{{comb(r,k)}}};')
            else: o.append(f'\\node at ({x:.2f},{y:.2f}) {{{comb(r,k)}}};')
    return fig('\n'.join(o),font)
def zar_fig(A,Bm):
    s=0.72; o=[]
    for i in range(1,7):
        o.append(f'\\node[font=\\small] at ({(i-0.5)*s:.2f},0.35) {{{i}}};'); o.append(f'\\node[font=\\small] at (-0.35,{-(i-0.5)*s:.2f}) {{{i}}};')
    o.append(f'\\node[font=\\small\\bfseries] at ({3*s:.2f},0.8) {{1. zar}}; \\node[font=\\small\\bfseries,rotate=90] at (-0.85,{-3*s:.2f}) {{2. zar}};')
    for a in range(1,7):
        for b in range(1,7):
            ia=(a,b) in A; ib=(a,b) in Bm
            fill='violet!40' if ia and ib else 'blue!25' if ia else 'orange!40' if ib else 'white'
            o.append(f'\\draw[fill={fill},thick] ({(a-1)*s:.2f},{-(b-1)*s:.2f}) rectangle ({a*s:.2f},{-b*s:.2f});')
            t='A,B' if ia and ib else 'A' if ia else 'B' if ib else ''
            if t: o.append(f'\\node[font=\\footnotesize\\bfseries] at ({(a-0.5)*s:.2f},{-(b-0.5)*s:.2f}) {{{t}}};')
    lx=6*s+0.5
    for j,(f,t) in enumerate([('blue!25','A olayı'),('orange!40','B olayı'),('violet!40','A ve B (her ikisi)')]):
        o.append(f'\\draw[fill={f},thick] ({lx:.2f},{-0.3-j*0.7:.2f}) rectangle ({lx+0.45:.2f},{-0.75-j*0.7:.2f}); \\node[anchor=west,font=\\small] at ({lx+0.6:.2f},{-0.52-j*0.7:.2f}) {{{t}}};')
    return fig('\n'.join(o))
def kutu_fig(kutular):
    o=[]
    for j,(ad,k,m) in enumerate(kutular):
        x0=j*4.2; bil=['K']*k+['M']*m
        o.append(f'\\draw[very thick] ({x0},1.9) -- ({x0},0) -- ({x0+3.4},0) -- ({x0+3.4},1.9);')
        o.append(f'\\node[font=\\small\\bfseries] at ({x0+1.7},2.3) {{{ad}}};')
        for i,b in enumerate(bil):
            r,c=divmod(i,3); x=x0+0.6+c*1.05; y=0.5+r*0.85
            f='red!40' if b=='K' else 'blue!35'
            o.append(f'\\node[circle,draw,thick,fill={f},minimum size=0.75cm,inner sep=0pt,font=\\small\\bfseries] at ({x:.2f},{y:.2f}) {{{b}}};')
    o.append(f'\\node[font=\\small,anchor=north west] at (0,-0.35) {{K: kırmızı top \\quad M: mavi top}};')
    return fig('\n'.join(o))
def galton_fig(puan):
    d=0.95; o=[]; n=5
    for i in range(1,n+1):
        for j in range(i): o.append(f'\\fill ({(j-(i-1)/2)*d:.2f},{-i*d:.2f}) circle (0.09);')
    o.append(f'\\fill[red!70!black] (0,0.15) circle (0.16); \\draw[-{{Stealth}},thick] (0,-0.08) -- (0,-0.55); \\node[anchor=west,font=\\small] at (0.3,0.15) {{bilye}};')
    yb=-(n+0.55)*d; yt=-(n+1.9)*d
    for k in range(n+2): o.append(f'\\draw[thick] ({(k-n/2-0.5)*d:.2f},{yb:.2f}) -- ({(k-n/2-0.5)*d:.2f},{yt:.2f});')
    o.append(f'\\draw[thick] ({(-n/2-0.5)*d:.2f},{yt:.2f}) -- ({(n/2+0.5)*d:.2f},{yt:.2f});')
    for k,p in enumerate(puan): o.append(f'\\node[font=\\bfseries] at ({(k-n/2)*d:.2f},{(yb+yt)/2:.2f}) {{{p}}};')
    o.append(f'\\node[font=\\small,anchor=north] at (0,{yt-0.1:.2f}) {{bölmelerin puanları}};')
    return fig('\n'.join(o))
def venn_fig(a,ab,b,dis,adA,adB):
    o=['\\draw[thick] (-3.3,-1.9) rectangle (3.3,2.1);',
       '\\draw[thick,fill=blue!22,fill opacity=0.8] (-0.85,0) circle (1.45); \\draw[thick,fill=orange!30,fill opacity=0.6] (0.85,0) circle (1.45); \\draw[thick] (-0.85,0) circle (1.45);',
       f'\\node[font=\\small\\bfseries] at (-1.95,1.75) {{{adA}}}; \\node[font=\\small\\bfseries] at (1.95,1.75) {{{adB}}};',
       f'\\node[font=\\large] at (-1.5,0) {{{a}}}; \\node[font=\\large] at (0,0) {{{ab}}}; \\node[font=\\large] at (1.5,0) {{{b}}}; \\node[font=\\large] at (2.65,-1.45) {{{dis}}};']
    return fig('\n'.join(o))
def agac_fig(dallar,h=3.0,dy=0.65,x1=2.6,x2=3.4,x3=4.3,x4=6.3):
    o=['\\fill (0,0) circle (0.07);']; ny=len(dallar)
    for i,(ad,p,alt) in enumerate(dallar):
        y=(ny-1)/2*h-i*h; o.append(f'\\draw[thick] (0,0) -- ({x1},{y:.2f}) node[font=\\small,pos=0.5,fill=white,inner sep=1.5pt] {{{tf(p)}}};')
        o.append(f'\\node[draw,rounded corners=2pt,fill=blue!12,font=\\small\\bfseries,inner sep=3pt] at ({x2},{y:.2f}) {{{ad}}};')
        for j,(sn,p2) in enumerate(alt):
            yy=y+(dy if j==0 else -dy); o.append(f'\\draw[thick] ({x3},{y:.2f}) -- ({x4},{yy:.2f}) node[font=\\small,pos=0.55,fill=white,inner sep=1.5pt] {{{tf(p2)}}};')
            o.append(f'\\node[anchor=west,font=\\small] at ({x4+0.1},{yy:.2f}) {{{sn}}};')
    return fig('\n'.join(o))
def cark_fig(dil):
    r=1.9; o=[]; a0=90
    for ad,aci,renk in dil:
        a1=a0-aci; m=(a0+a1)/2
        o.append(f'\\fill[{renk}] (0,0) -- ({a0}:{r}) arc ({a0}:{a1}:{r}) -- cycle; \\draw[thick] (0,0) -- ({a0}:{r});')
        o.append(f'\\node[align=center,font=\\small] at ({m}:{r*0.62:.2f}) {{{ad}\\\\{aci}$^\\circ$}};')
        a0=a1
    o.append(f'\\draw[very thick] (0,0) circle ({r}); \\fill (0,0) circle (0.07);')
    return fig('\n'.join(o))
def yol_fig(W,Hh,kapali,C):
    s=1.0; o=[]
    for x in range(W+1): o.append(f'\\draw[gray!55] ({x*s},0) -- ({x*s},{Hh*s});')
    for y in range(Hh+1): o.append(f'\\draw[gray!55] (0,{y*s}) -- ({W*s},{y*s});')
    for x in range(W+1):
        for y in range(Hh+1): o.append(f'\\fill ({x*s},{y*s}) circle (0.045);')
    for (p1,p2) in kapali:
        o.append(f'\\draw[red!80!black,line width=2.6pt] ({p1[0]*s},{p1[1]*s}) -- ({p2[0]*s},{p2[1]*s});')
        mx,my=(p1[0]+p2[0])/2*s,(p1[1]+p2[1])/2*s
        o.append(f'\\node[font=\\footnotesize\\bfseries,fill=white,inner sep=1pt,text=red!70!black] at ({mx:.2f},{my:.2f}) {{X}};')
    o.append(f'\\node[circle,draw,thick,fill=yellow!60,minimum size=0.55cm,inner sep=0,font=\\bfseries] at (0,0) {{A}}; \\node[circle,draw,thick,fill=yellow!60,minimum size=0.55cm,inner sep=0,font=\\bfseries] at ({W*s},{Hh*s}) {{B}};')
    o.append(f'\\node[circle,draw,thick,fill=green!45,minimum size=0.5cm,inner sep=0,font=\\bfseries] at ({C[0]*s},{C[1]*s}) {{C}};')
    o.append('\\draw[red!80!black,line width=2.6pt] (0.0,-0.95) -- (0.6,-0.95); \\node[anchor=west,font=\\small] at (0.75,-0.95) {X: kapalı sokak};')
    return fig('\n'.join(o))
def lamba_fig(durum):
    o=[]
    for i,d in enumerate(durum):
        x=i*1.3; o.append(f'\\node[font=\\small] at ({x},1.0) {{{i+1}}};')
        if d=='yanik':
            import math
            ray=' '.join(f'\\draw[orange!80!black,thick] ({x+0.55*math.cos(math.radians(a)):.2f},{0.55*math.sin(math.radians(a)):.2f}) -- ({x+0.78*math.cos(math.radians(a)):.2f},{0.78*math.sin(math.radians(a)):.2f});' for a in range(0,360,45))
            o.append(f'\\node[circle,draw,thick,fill=yellow!70,minimum size=0.85cm,inner sep=0] at ({x},0) {{}}; {ray} \\node[font=\\scriptsize] at ({x},-1.0) {{yanık}};')
        elif d=='bozuk': o.append(f'\\node[circle,draw,thick,fill=gray!40,minimum size=0.85cm,inner sep=0] at ({x},0) {{}}; \\draw[thick] ({x-0.2},-0.2) -- ({x+0.2},0.2) ({x-0.2},0.2) -- ({x+0.2},-0.2); \\node[font=\\scriptsize] at ({x},-1.0) {{arızalı}};')
        else: o.append(f'\\node[circle,draw,thick,minimum size=0.85cm,inner sep=0,font=\\bfseries] at ({x},0) {{?}}; \\node[font=\\scriptsize] at ({x},-1.0) {{bilinmiyor}};')
    return fig('\n'.join(o))

x,y,t=sp.symbols('x y t')
def kat(expr,mon): return sp.Poly(sp.expand(expr),x,y).coeff_monomial(mon)

# ================= 01 kolay · terim katsayısı (düz) =================
v=kat((x-2*y)**7,x**4*y**3); assert v==comb(7,3)*(-2)**3==-280
e=[comb(7,3)*2**3, comb(7,3), comb(7,3)*2*3*(-1), comb(7,3)*(-2)**4*(-1)]; assert e==[280,35,-210,-560] and len({v,*[-e[1],e[0],e[2],e[3]]})==5
q('0001',[A('Genel terimi yaz','(x − 2y)⁷ için x⁴y³ li terimde y’nin kuvveti 3 olduğundan k = 3’tür.','C(7, 3) × x⁴ × (−2y)³'),
          A('Binom katsayısını hesapla','C(7, 3) = 7 × 6 × 5 / (3 × 2 × 1) bulunur.','C(7, 3) = 35'),
          A('Katsayıyı bul','(−2)³ = −8 olur; sayı çarpanları çarpılır.','35 × (−8) = −280')],
 -280,[(280,'(−2)³ ifadesindeki eksi işaretini atlayıp pozitif almış.','islem'),(-35,'Yalnız C(7, 3) = 35’i alıp (−2y)³ çarpanını unutmuş; işareti yine de eksi yazmış.','bilgi'),(-210,'(−2)³ yerine −2 × 3 = −6 hesaplamış: 35 × (−6).','islem'),(-560,'İkinci terimin kuvveti olarak 3 yerine x’in kuvvetini (4) kullanıp (−2)⁴ = 16 almış, işareti de eksi bırakmış.','dikkat')],
 tipId='bn-terim',tip='Binom açılımında terim ve parametre',z='kolay',alt='Terim Katsayısı',kaz='İki terimli ifadenin açılımında belirli bir terimin katsayısını genel terim formülüyle hesaplar.',kalip='düz',
 kart='K-ABO-01 (genel terimle belirli terim) · iki değişkenli, ikinci terimde katsayı ve negatif işaret',
 metin='(x − 2y)⁷ ifadesinin açılımında x⁴y³ lü terimin katsayısı kaçtır?',
 istenen='(x − 2y)⁷ açılımında x⁴y³ lü terimin katsayısı.',ip=['Genel terimde y’nin üssünü belirleyen sayı, binom katsayısının alt sayısıyla aynıdır.'],bilgi=[BIN],
 puf='İkinci terim eksi işaretli ya da katsayılıysa kuvveti alırken işaret ve katsayı birlikte kuvvetlenir.')

# ================= 02 kolay · Pascal üçgeni, eksik hücreler (şekil) =================
GZ={(4,2):'a',(6,2):'b',(6,4):'c'}
va,vb,vc=comb(4,2),comb(6,2),comb(6,4); assert (va,vb,vc)==(6,15,15) and comb(3,1)+comb(3,2)==va and comb(5,1)+comb(5,2)==vb and comb(5,3)+comb(5,4)==vc
v=va+vb+vc; assert v==36
eL=comb(3,1)+comb(5,1)+comb(5,3); eP=comb(3,1)*comb(3,2)+comb(5,1)*comb(5,2)+comb(5,3)*comb(5,4); eS=comb(5,2)+comb(7,2)+comb(7,4); eF=va+vb
assert [eL,eP,eS,eF]==[18,109,66,21] and len({v,eL,eP,eS,eF})==5
q('0002',[A('a hücresini bul','Her sayı, bir üst satırdaki iki komşusunun toplamıdır; 4. satırdaki a için 3. satırdan 3 ve 3 okunur.','a = 3 + 3 = 6'),
          A('b ve c hücrelerini bul','b’nin üstündeki sayılar 5 ve 10, c’nin üstündeki sayılar 10 ve 5’tir.','b = 5 + 10 = 15 · c = 10 + 5 = 15'),
          A('Toplamı hesapla','Üç sayı toplanır.','a + b + c = 6 + 15 + 15 = 36')],
 36,[(eL,'Her hücre için yalnız sol üstteki sayıyı almış (3, 5, 10), toplama kuralını uygulamamış.','bilgi'),(eF,'c hücresini hesaplamayı unutup yalnız a + b = 6 + 15 toplamını yazmış.','dikkat'),(eS,'Hücreleri bir alt satırdaki aynı sıradan okumuş (10, 21, 35): satır numarasını bir fazla almış.','dikkat'),(eP,'Üstteki iki sayıyı toplamak yerine çarpmış: 9, 50, 50.','bilgi')],
 tipId='bn-pascal',tip='Pascal üçgeni ve ardışık katsayılar',z='kolay',alt='Pascal Üçgeni',kaz='Pascal üçgeninde toplama kuralıyla eksik sayıları bulur.',kalip='şekilli',
 kart='K-ABO-02 (Pascal üçgeni, toplama kuralı) · üç gizli hücre, bağımsız konumlar',
 metin='Şekilde, Pascal üçgeninin ilk yedi satırı gösterilmiş; üçgendeki bazı sayıların yerine a, b ve c yazılmıştır.\nBuna göre a + b + c toplamı kaçtır?',
 istenen='Gizlenen üç sayının toplamı.',ip=['Üçgendeki her sayının, bir üst satırdaki hangi iki sayıyla ilgili olduğuna bak.'],bilgi=[PAS],sekil=pascal_fig(7,GZ),
 puf='Pascal üçgeninde eksik bir sayıyı hep bir üst satırdaki iki komşusundan kur.')

# ================= 03 kolay · zar çizelgesi, koşullu olasılık =================
S=[(a,b) for a in range(1,7) for b in range(1,7)]
A_=set(s for s in S if s[0]<s[1]); B_=set(s for s in S if s[0]+s[1] in (6,7)); AB=A_&B_
assert (len(A_),len(B_),len(AB))==(15,11,5)
v=Fr(len(AB),len(A_)); assert v==Fr(1,3)
eV=[Fr(len(AB),len(B_)),Fr(len(AB),36),Fr(len(B_),36),Fr(len(A_),36)]; assert eV==[Fr(5,11),Fr(5,36),Fr(11,36),Fr(5,12)] and len({v,*eV})==5
q('0003',[A('Çizelgeyi oku','Mavi ve mor hücreler A olayını oluşturur: A olayında 15 sonuç vardır.','s(A) = 15'),
          A('Kesişimi say','A bilindiğinde B’nin gerçekleştiği sonuçlar mor hücrelerdir.','s(A ∩ B) = 5'),
          A('Koşullu olasılığı yaz','Örnek uzay A’ya daralır; pay mor hücreler, payda A’nın tüm hücreleridir.','P(B | A) = 5/15 = 1/3')],
 Fr(1,3),[(eV[0],'Koşulu ters yorumlayıp B’nin içinde A’yı aramış: payda olarak B’nin hücre sayısı (11) almış.','bilgi'),(eV[1],'Kesişimin olasılığını (5/36) yazmış; koşul nedeniyle örnek uzayın daraldığını unutmuş.','dikkat'),(eV[2],'Yalnız B olayının olasılığını (11/36) hesaplamış.','dikkat'),(eV[3],'Yalnız A olayının olasılığını (15/36) yazmış.','dikkat')],
 tipId='ol-kosullu',tip='Koşullu olasılık',z='kolay',alt='Koşullu Olasılık',kaz='İki zar atılmasında örnek uzayı çizelgeyle kurup koşullu olasılığı hesaplar.',kalip='şekilli',
 kart='K-ABO-04 (çizelgede koşullu olasılık) · iki zar, A: birinci zar küçük; B: toplam 6 ya da 7',
 metin='Şekildeki çizelge, iki zarın birlikte atılmasıyla elde edilebilecek 36 eş olasılıklı sonucu göstermektedir. A ve B olayları çizelgede renklendirilmiş, her iki olaya ait sonuçlar ayrıca işaretlenmiştir.\nA olayı gerçekleştiği bilindiğine göre B olayının gerçekleşme olasılığı kaçtır?',
 istenen='P(B | A) değeri.',ip=['A bilindiğinde ilgilendiğin sonuçlar çizelgenin tamamı değil, yalnızca bir bölümüdür.'],bilgi=[KOS],sekil=zar_fig(A_,B_),
 puf='Koşul “bilindiğine göre” ifadesinin sonrasındaki olaydır ve paydayı belirler.')

# ================= 04 kolay · iki kutu, bağımsız çekiliş =================
v=Fr(3,4)*Fr(2,5)+Fr(1,4)*Fr(3,5); assert v==Fr(9,20)
tum=sum(1 for a in 'KKKM' for b in 'KKMMM' if a==b)/20; assert Fr(tum).limit_denominator(100)==v
eKK=Fr(3,4)*Fr(2,5); eMM=Fr(1,4)*Fr(3,5); eF=1-v; eHav=Fr(comb(5,2)+comb(4,2),comb(9,2))
assert [eKK,eMM,eF,eHav]==[Fr(3,10),Fr(3,20),Fr(11,20),Fr(4,9)] and len({v,eKK,eMM,eF,eHav})==5
q('0004',[A('Aynı renk durumlarını belirle','İki top ya ikisi de kırmızı ya da ikisi de mavi olabilir; bu iki durum birlikte gerçekleşemez.','KK ya da MM'),
          A('Her durumun olasılığı','Kutular bağımsız olduğundan her kutudaki olasılıklar çarpılır.','P(KK) = 3/4 × 2/5 = 3/10 · P(MM) = 1/4 × 3/5 = 3/20'),
          A('Olasılıkları topla','Ayrık durumların olasılıkları toplanır.','3/10 + 3/20 = 9/20')],
 v,[(eKK,'Yalnız iki topun da kırmızı olduğu durumu (3/10) hesaplamış.','dikkat'),(eMM,'Yalnız iki topun da mavi olduğu durumu (3/20) hesaplamış.','dikkat'),(eHav,'İki kutudaki 9 topu tek torbaya dökmüş gibi 2 top seçmiş: (C(5, 2) + C(4, 2)) / C(9, 2).','bilgi'),(eF,'İki topun farklı renkte olma olasılığını (11/20) bulmuş.','dikkat')],
 tipId='ol-bagimsiz',tip='Bağımsız olaylar',z='kolay',alt='Bağımsız Olaylar',kaz='İki ayrı kutudan çekilen topların renk eşleşme olasılığını bağımsızlıkla hesaplar.',kalip='şekilli',
 kart='K-ABO-05 (bağımsız çekiliş) · iki kutu, kutu başına bir top, aynı renk olma durumu',
 metin='Şekilde, kırmızı (K) ve mavi (M) toplar içeren iki kutu görülmektedir. Her kutudan rastgele birer top çekiliyor.\nBuna göre çekilen iki topun aynı renkte olma olasılığı kaçtır?',
 istenen='İki topun aynı renkte olma olasılığı.',ip=['Aynı renk olmasının hangi iki ayrı biçimde gerçekleşebileceğini listele.'],bilgi=[BAG],sekil=kutu_fig([('I. kutu',3,1),('II. kutu',2,3)]),
 puf='“Ya … ya da …” ile ayrılan durumlar toplanır, “ve” ile bağlanan bağımsız seçimler çarpılır.')

# ================= 05 orta · sabit terim ve parametre =================
a_=sp.symbols('a',positive=True)
k0=[k for k in range(9) if 3*(8-k)-k==0]; assert k0==[6]
sabit=comb(8,6)*a_**6; assert sp.simplify(sp.expand((x**3+a_/x)**8).coeff(x,0)-sabit)==0
assert sabit.subs(a_,2)==1792 and sp.solve(sp.Eq(sabit,1792),a_)==[2]
assert [4**3,8**2,Fr(64,6),Fr(1792,28)]==[64,64,Fr(32,3),64] and 4**3==64 and 8**2==64
q('0005',[A('Genel terimi yaz','İkinci terim a/x olduğundan k. terimde x’in kuvvetleri birleşir.','C(8, k) × (x³)⁸⁻ᵏ × (a/x)ᵏ = C(8, k) × aᵏ × x²⁴⁻⁴ᵏ'),
          A('Sabit terim için k’yı bul','x’in kuvveti 0 olmalı.','24 − 4k = 0 ⇒ k = 6'),
          A('Eşitliği kur','k = 6 için sabit terim 1792’ye eşitlenir.','C(8, 6) × a⁶ = 1792 ⇒ 28 × a⁶ = 1792'),
          A('a’yı çöz','a⁶ = 64 ve a pozitif olduğundan altıncı kök alınır.','a⁶ = 64 ⇒ a = 2')],
 2,[(4,'a⁶ = 64 eşitliğinden üçüncü kökü alıp a³ = 64 gibi işlem yapmış.','bilgi'),(8,'a⁶ = 64 eşitliğinden kareköke geçip a² = 64 saymış.','bilgi'),(Fr(32,3),'a⁶ = 64 eşitliğini a = 64/6 olarak çözmüş: kuvveti çarpan gibi yorumlamış.','islem'),(64,'a⁶ yerine a yazıp 28a = 1792’den a = 64 bulmuş.','islem')],
 tipId='bn-terim',tip='Binom açılımında terim ve parametre',z='orta',alt='Sabit Terim',kaz='Üslü terimli binom açılımında sabit terimi bulup parametreyi hesaplar.',kalip='düz',
 kart='K-ABO-01 (genel terimle belirli terim ve parametre) · x³ ve a/x terimleri, sabit terim verilmiş',
 metin='a pozitif bir gerçel sayı olmak üzere,\n(x³ + a/x)⁸\nifadesinin açılımındaki sabit terim 1792 olduğuna göre, a kaçtır?',
 istenen='Sabit terimi 1792 yapan a değeri.',ip=['İki terimdeki x’in kuvvetlerini genel terimde birleştirip toplam kuvveti sıfıra eşitle.'],bilgi=[BIN,SAB],
 puf='Sabit terimde önce k’yı x’in kuvvetinden bul; parametre denklemini ondan sonra kur.')

# ================= 06 orta · katsayılar toplamından n, sonra terim =================
n6=[n for n in range(1,20) if (3-1)**n==64]; assert n6==[6]
v=kat((3*x-1)**6,x**3); assert v==comb(6,3)*27*(-1)**3==-540
e=[540,comb(6,3)*(-1)**3,comb(6,3)*9*(-1)**3,comb(5,3)*27*(-1)**2]; assert e==[540,-20,-180,270] and len({v,*e})==5 and 2**6==64 and 2**5*2==64
q('0006',[A('n’yi bul','x yerine 1 yazınca katsayılar toplamı bulunur.','(3 − 1)ⁿ = 64 ⇒ 2ⁿ = 64 ⇒ n = 6'),
          A('Genel terimi yaz','(3x − 1)⁶ için x³ li terimde 3x’in kuvveti 3, (−1)’in kuvveti de 3 olur.','C(6, 3) × (3x)³ × (−1)³'),
          A('Katsayıyı hesapla','C(6, 3) = 20, 3³ = 27 ve (−1)³ = −1’dir.','20 × 27 × (−1) = −540')],
 -540,[(540,'(−1)³ çarpanının işaretini atlamış.','islem'),(-180,'3’ün kuvvetini 3 yerine 2 alıp 20 × 9 × (−1) hesaplamış.','dikkat'),(-20,'(3x)³ ifadesindeki 3³ = 27 çarpanını unutmuş.','bilgi'),(270,'Katsayılar toplamını 2ⁿ⁺¹ = 64 yazıp n = 5 bulmuş; ardından C(5, 3) × 27 × (−1)² hesaplamış.','bilgi')],
 tipId='bn-terim',tip='Binom açılımında terim ve parametre',z='orta',alt='Katsayılar Toplamı',kaz='Katsayılar toplamından n’yi bulup belirli terimin katsayısını hesaplar.',kalip='düz',
 kart='K-ABO-01 (katsayılar toplamı ve belirli terim) · n bilinmiyor, toplamdan bulunur; ikinci terim işaretli',
 metin='n pozitif bir tam sayı olmak üzere, (3x − 1)ⁿ ifadesinin açılımındaki katsayıların toplamı 64’tür.\nBuna göre bu açılımda x³ lü terimin katsayısı kaçtır?',
 istenen='(3x − 1)ⁿ açılımında x³ lü terimin katsayısı.',ip=['Önce katsayılar toplamını veren işlemi n’ye bağlı yaz; n belli olunca genel terim formülüne geç.'],bilgi=[BIN,KAT],
 puf='Katsayılar toplamı verilmişse x yerine 1 yazıp n’yi önce bul.',kisa='n = 6 bulunduktan sonra (3x − 1)⁶ için doğrudan C(6, 3) × 3³ × (−1)³ yazmak yeterlidir.')

# ================= 07 orta · öncüllü, (x² − 1/x)⁶ =================
ifd=sp.expand((x**2-1/x)**6); terim=len(sp.Add.make_args(ifd)); top=ifd.subs(x,1); sabt=ifd.coeff(x,0)
assert (terim,top,sabt)==(7,0,15)
I=(6==terim); II=(top==0); III=(sabt==15); assert (I,II,III)==(False,True,True) and kume((I,II,III))=='II ve III'
k3=comb(6,3)*(-1)**3; assert k3==-20 and (1-1)**6==0
sira=OS3; dogru=kume((I,II,III))
qo('0007',[A('I. önermeyi sına','Açılımda n + 1 terim bulunur; n = 6 için terim sayısı 7’dir, 6 değildir.','n + 1 = 7 ⇒ I yanlış'),
           A('II. önermeyi sına','Katsayılar toplamı için x = 1 yazılır.','(1² − 1/1)⁶ = 0⁶ = 0 ⇒ II doğru'),
           A('III. önermeyi sına','Genel terim C(6, k) × (x²)⁶⁻ᵏ × (−1/x)ᵏ olup x’in kuvveti 12 − 3k’dır; sıfır olması için k = 4.','C(6, 4) × (−1)⁴ = 15 ⇒ III doğru'),
           A('Sonucu yaz','Doğru olan önermeler II ve III’tür.','II ve III')],
 dogru,[('Yalnız I','I’i doğru saymış (terim sayısını n = 6 almış), II’yi yanlış saymış (toplamı 1 sanmış), III için k = 3 alıp −20 bulmuş.','bilgi'),('Yalnız II','I’in yanlış olduğunu görmüş (7 terim); II’yi doğru bulmuş; III’te k = 3 alıp −20 bulduğundan III’ü yanlış saymış.','dikkat'),('I ve II','Terim sayısını 6 sanıp I’i doğru kabul etmiş, II’yi doğru bulmuş; III’te k = 3 alıp sabit terimi −20 bulmuş.','dikkat'),('I ve III','Terim sayısını n = 6 sanmış; katsayılar toplamını 1 hesaplayıp II’yi yanlış bulmuş; sabit terimi doğru hesaplamış.','bilgi')],
 sira=sira,
 tipId='bn-ozellik',tip='Binom açılımının özellikleri ve çarpımı',z='orta',alt='Binom Özellikleri',kaz='Binom açılımında terim sayısı, katsayılar toplamı ve sabit terim yargılarını değerlendirir.',kalip='öncüllü',
 kart='K-ABO-03 (binom özellikleri) · üç yargı: terim sayısı, katsayılar toplamı, sabit terim',
 metin='Bir öğretmen, (x² − 1/x)⁶ ifadesinin açılımı için aşağıdaki önermeleri yazıyor.\nI. Açılımda 6 terim vardır.\nII. Katsayıların toplamı 0’dır.\nIII. Sabit terim 15’tir.\nBuna göre bu önermelerden hangileri doğrudur?',
 istenen='Doğru olan önermeler.',ip=['Her önermeyi ayrı ayrı sına: terim sayısı için üssü, toplam için x’e verilecek değeri, sabit terim için genel terimi düşün.'],bilgi=[BIN,KAT,SAB],
 puf='Öncüllü binom sorularında her yargı için ayrı kontrol yöntemi seç: sayma, x = 1, genel terim.')

# ================= 08 orta · Pascal köşegen toplamı (şekil) =================
BY={(r,3) for r in range(3,8)}
v=sum(comb(n,3) for n in range(3,11)); assert v==comb(11,4)==330
e=[sum(comb(n,3) for n in range(3,8)),comb(10,3),comb(11,3),comb(10,4)]; assert e==[70,120,165,210] and len({v,*e})==5
q('0008',[A('Boyalı sayıları tanı','Boyalı hücreler her satırda soldan 4. sayıdır; bunlar C(3, 3), C(4, 3), …, C(7, 3) değerleridir.','1, 4, 10, 20, 35'),
          A('Köşegen toplamı kuralını kullan','Aynı köşegen boyunca 10. satıra kadar olan toplam, son sayının bir alt satırdaki sağ komşusuna eşittir.','C(3, 3) + … + C(10, 3) = C(11, 4)'),
          A('Değeri hesapla','C(11, 4) hesaplanır.','C(11, 4) = (11 × 10 × 9 × 8) / (4 × 3 × 2 × 1) = 330')],
 v,[(70,'Toplamı yalnızca şekilde görünen 7. satıra kadar yapmış (1 + 4 + 10 + 20 + 35).','dikkat'),(120,'Toplam yerine yalnızca son boyalı sayıyı, yani 10. satırdaki C(10, 3) değerini almış.','dikkat'),(165,'Köşegen toplamının bir alt satırdaki komşusunu C(11, 3) alarak sütunu bir kaydırmış.','bilgi'),(210,'Son satırı 10 alıp toplamı C(10, 4) saymış: satırı bir kaydırmış.','bilgi')],
 tipId='bn-pascal',tip='Pascal üçgeni ve ardışık katsayılar',z='orta',alt='Pascal Köşegeni',kaz='Pascal üçgeninde bir köşegen boyunca toplamı C(n + 1, k + 1) özelliğiyle hesaplar.',kalip='şekilli',
 kart='K-ABO-02 (Pascal köşegen toplamı) · soldan 4. sayı; toplam şekildeki satırlardan daha ileri götürülüyor',
 metin='Şekilde, satırları 0’dan başlayarak numaralandırılmış Pascal üçgeninin ilk sekiz satırı verilmiştir; her satırda soldan 4. sayı yeşil renkle boyanmıştır.\nÜçgen 10. satıra kadar genişletildiğinde aynı biçimde boyanan bütün sayıların toplamı kaçtır?',
 istenen='3. satırdan 10. satıra kadar boyalı sayıların toplamı.',ip=['Boyalı sayıların üçgendeki konumuna bak.'],bilgi=[PAS,PAK],sekil=pascal_fig(8,{},BY),
 puf='Bir sayı dizisinin toplamı sorulduğunda, dizinin üçgendeki konumunu çözmeye çalış.',kisa='C(3, 3) + C(4, 3) + … + C(10, 3) toplamı, köşegen kuralıyla doğrudan C(11, 4)’tür.')

# ================= 09 orta · çivili tahta (Galton), tekrarlı deneme =================
PU=[5,2,1,3,2,5]
from collections import Counter
sayac=Counter(sum(yol) for yol in product((0,1),repeat=5)); assert [sayac[k] for k in range(6)]==[comb(5,k) for k in range(6)]
v=Fr(sum(sayac[k] for k in range(6) if PU[k]%2==1),32); assert v==Fr(11,16)
e=[Fr(4,6),Fr(5,16),Fr(22,64),Fr(sayac[2]+sayac[3],32)]; assert e==[Fr(2,3),Fr(5,16),Fr(11,32),Fr(5,8)] and len({v,*e})==5
q('0009',[A('Bölmelere düşme sayılarını bul','5 çivide her yol sağ/sol dizisidir: toplam 2⁵ = 32 yol. k kez sağa sapan yolların sayısı C(5, k)’dır.','Bölmeler için yol sayıları: 1, 5, 10, 10, 5, 1'),
          A('Puanlara bak','Tek puanlı bölmeler 1., 3., 4. ve 6. bölmelerdir (puanlar 5, 1, 3, 5).','1 + 10 + 10 + 1 = 22 yol'),
          A('Olasılığı yaz','Elverişli yol sayısı bütün yollara bölünür.','22/32 = 11/16')],
 v,[(e[1],'Çift puanlı bölmelerin olasılığını (10/32) bulmuş; sorulan tek puanı değil çifti hesaplamış.','dikkat'),(e[2],'Çivi sırasını 6 sanıp payda olarak 2⁶ = 64, pay olarak 22 alıp 22/64 yazmış.','islem'),(e[3],'Yalnız ortadaki iki bölmeyi (10 + 10 yol) sayıp 20/32 bulmuş; kenar bölmelerin 5 puanlı olduğunu atlamış.','dikkat'),(e[0],'Bölmelerin eş olasılıklı olduğunu sanıp 6 bölmenin 4’ünü almış: 4/6.','bilgi')],
 tipId='ol-tekrar',tip='Tekrarlı bağımsız denemeler',z='orta',alt='Çivili Tahta',kaz='Çivili tahtada bilyenin bölmelere düşme olasılığını binom katsayılarıyla hesaplar.',kalip='şekilli',
 kart='K-ABO-08 (tekrarlı bağımsız deneme) · beş sıra çivi, bölme puanları, puanın tek olması',
 metin='Şekilde, beş sıra çivisi olan bir tahta görülmektedir. Tahtanın tepesinden bırakılan bilye, karşılaştığı her çivide eşit olasılıkla sağa ya da sola sapıp altta bulunan altı bölmeden birine düşmektedir. Her bölmenin puanı bölmenin içinde yazılıdır.\nBuna göre bilyenin düştüğü bölmenin puanının tek sayı olma olasılığı kaçtır?',
 istenen='Bilyenin tek puanlı bir bölmeye düşme olasılığı.',ip=['Her bölmeye ulaşan yolların sayısı, sağa sapılan çivi sayısına göre değişir.'],bilgi=[PAS,TEK],sekil=galton_fig(PU),
 puf='Eşit olasılıklı sağ/sol seçimlerinde bir bölmenin olasılığı C(n, k) / 2ⁿ’dir; bölmeler eş olasılıklı değildir.')

# ================= 10 orta · iki yönlü tablo, bağımsızlık =================
a,b,c=8,12,6
sol=[X for X in range(1,100) if Fr(b,a+b+c+X)==Fr(a+b,a+b+c+X)*Fr(b+X,a+b+c+X)]; assert sol==[9]
v=9; e=[a*c//b,b+c-a,b,a*b//c]; assert (a*c%b,a*b%c)==(0,0) and e==[4,10,12,16] and len({v,*e})==5
tb=tablo_svg(['','Müzik kulübü','Spor kulübü'],[['Kız',str(a),str(b)],['Erkek',str(c),'x']])
q('0010',[A('Olasılıkları yaz','Öğrenci sayısı N = 26 + x’tir. Kız olma ve spor kulübünde olma olasılıkları ile ikisinin birlikte olasılığı tablodan okunur.','Kız olma: 20/N · Spor kulübünde olma: (12 + x)/N · İkisi birlikte: 12/N'),
          A('Bağımsızlık koşulunu kur','Bağımsız olaylarda P(K ∩ S) = P(K) × P(S) olur.','12/N = (20/N) × ((12 + x)/N)'),
          A('Denklemi çöz','Eşitlik N ile sadeleştirilir; N = 26 + x yerine yazılır.','12 × (26 + x) = 20 × (12 + x) ⇒ 312 + 12x = 240 + 20x ⇒ x = 9')],
 9,[(4,'Çapraz çarpımda eşleştirmeyi yanlış yapıp x = (8 × 6) / 12 bulmuş.','bilgi'),(10,'Satırlar arasındaki farkın sabit olduğunu sanıp 12 − 8 = x − 6 yazmış.','bilgi'),(12,'Spor kulübündeki kız ve erkek sayılarını eşit sanmış.','dikkat'),(16,'Oranları ters kurup x = (8 × 12) / 6 hesaplamış.','islem')],
 tipId='ol-bagimsiz',tip='Bağımsız olaylar',z='orta',alt='Bağımsızlık Koşulu',kaz='İki yönlü tabloda bağımsızlık koşulundan bilinmeyen sayıyı bulur.',kalip='tablo',
 kart='K-ABO-05 (bağımsızlık ve tablo) · kız-erkek × iki kulüp, bilinmeyen hücre',
 metin='Bir okulda yalnızca müzik ve spor olmak üzere iki kulüp vardır ve her öğrenci bu kulüplerden yalnız birine üyedir. Kulüplere üye olan öğrencilerin sayıları cinsiyete göre aşağıdaki tabloda verilmiştir.\nRastgele seçilen bir öğrencinin kız olması ile spor kulübüne üye olması bağımsız olaylar olduğuna göre x kaçtır?',
 istenen='Tablodaki x değeri.',ip=['Bağımsızlık, kız olma ile spor kulübünde olma olasılıklarının çarpımının ikisinin birlikte olasılığına eşit olmasıdır.'],bilgi=[BAG],sekil=tb,
 puf='Bağımsızlık verildiğinde tablodaki hücreleri toplam öğrenci sayısına göre olasılığa çevirip çarpım eşitliğini kur.')

# ================= 11 orta · ağaç şeması, toplam olasılık =================
v=Fr(1,4)*Fr(2,3)+Fr(3,4)*Fr(1,5); assert v==Fr(19,60)
e=[Fr(1,4)*Fr(2,3),Fr(3,4)*Fr(1,5),Fr(2,3)+Fr(1,5),Fr(2,3)*Fr(1,5)]; assert e==[Fr(1,6),Fr(3,20),Fr(13,15),Fr(2,15)] and len({v,*e})==5
q('0011',[A('Geç kalma yollarını belirle','Geç kalma iki yoldan gerçekleşir: yağışlı hava ve geç kalma ya da güneşli hava ve geç kalma.','Y → G ve S → G'),
          A('Yolların olasılığı','Her yolda dal olasılıkları çarpılır.','1/4 × 2/3 = 1/6 · 3/4 × 1/5 = 3/20'),
          A('Yolları topla','Bu iki yol birlikte gerçekleşemez; olasılıkları toplanır.','1/6 + 3/20 = 10/60 + 9/60 = 19/60')],
 v,[(e[0],'Yalnız yağışlı hava koluyla geç kalma yolunu almış.','dikkat'),(e[1],'Yalnız güneşli hava koluyla geç kalma yolunu almış.','dikkat'),(e[3],'İki geç kalma dalının olasılıklarını (2/3 ve 1/5) birbiriyle çarpmış; hava durumu dallarını katmamış.','bilgi'),(e[2],'Geç kalma dallarını (2/3 + 1/5) doğrudan toplamış; hava durumunun olasılığını çarpmamış.','bilgi')],
 tipId='ol-agac',tip='Ağaç şeması ve koşullu olasılık',z='orta',alt='Toplam Olasılık',kaz='İki aşamalı ağaç şemasında toplam olasılığı dal çarpımları ve toplamıyla hesaplar.',kalip='hikâyeli',
 kart='K-ABO-06 (ağaç şeması, toplam olasılık) · iki hava durumu, iki aşamalı ağaç',
 metin='Ece, her sabah okula yürüyerek gidiyor. Havanın yağışlı ya da güneşli olmasına göre yolda oyalanması değiştiği için okula geç kalma olasılığı değişiyor. Bir sabahın hava durumu ve Ece’nin geç kalma durumu, olasılıklarıyla birlikte şekildeki ağaç şemasında gösterilmiştir.\nBuna göre Ece’nin bir sabah okula geç kalma olasılığı kaçtır?',
 istenen='Ece’nin bir sabah geç kalma olasılığı.',ip=['Geç kalma sonucuna giden her yolu ayrı ayrı ele al ve yoldaki olasılıkların nasıl birleşeceğini düşün.'],bilgi=[AGA],sekil=agac_fig([('Yağışlı',Fr(1,4),[('Geç kalır',Fr(2,3)),('Zamanında',Fr(1,3))]),('Güneşli',Fr(3,4),[('Geç kalır',Fr(1,5)),('Zamanında',Fr(4,5))])],h=2.6,dy=0.6),
 puf='Ağaçta çarpma “ve” için, toplama “ya da” için kullanılır.')

# ================= 12 orta · torba, kombinasyonla olasılık =================
RN={'Kırmızı':4,'Mavi':3,'Yeşil':2}; ball=[r for r,nn in RN.items() for _ in range(nn)]
sec=list(combinations(range(9),3)); assert len(sec)==comb(9,3)==84
farkli=sum(1 for s_ in sec if len({ball[i] for i in s_})==3); hepsi=sum(1 for s_ in sec if len({ball[i] for i in s_})==1); tam2=sum(1 for s_ in sec if len({ball[i] for i in s_})==2)
assert (farkli,hepsi,tam2)==(24,5,55)
v=Fr(hepsi,84); assert v==Fr(5,84)==Fr(comb(4,3)+comb(3,3),84)
e=[Fr(farkli,84),Fr(tam2,84),Fr(tam2+hepsi,84),Fr(4,9)**3+Fr(3,9)**3+Fr(2,9)**3]; assert e==[Fr(2,7),Fr(55,84),Fr(5,7),Fr(11,81)] and len({v,*e})==5
q('0012',[A('Bütün seçimleri say','9 bilyeden 3’ü aynı anda seçildiğinden sıra önemsizdir; kombinasyon kullanılır.','C(9, 3) = 84'),
          A('Elverişli seçimleri say','Üç bilyenin aynı renk olması için üçü de kırmızı ya da üçü de mavi olmalıdır; yeşil bilye yalnız 2 tane olduğundan yeşilden 3 bilye seçilemez.','C(4, 3) + C(3, 3) + 0 = 4 + 1 + 0 = 5'),
          A('Olasılığı hesapla','Elverişli seçim sayısı bütün seçim sayısına bölünür.','5/84')],
 v,[(e[0],'Üç bilyenin hepsinin farklı renkte olduğu durumu (4 × 3 × 2 = 24 seçim) hesaplamış.','dikkat'),(e[3],'Bilyeleri iade ederek çekmiş gibi (4/9)³ + (3/9)³ + (2/9)³ hesaplamış; yeşilden üç bilye çekilemeyeceğini görmemiş.','dikkat'),(e[1],'“Üçü aynı renk” yerine tam iki bilyenin aynı renkte olduğu durumu (55 seçim) saymış.','dikkat'),(e[2],'“Üçü aynı renk” durumuna tam iki aynı renkli seçimleri de katıp en az ikisinin aynı renkte olma olasılığını (60/84) bulmuş.','dikkat')],
 tipId='ol-sayma',tip='Sayma ile olasılık',z='orta',alt='Kombinasyonla Olasılık',kaz='Torbadan aynı anda çekilen bilyelerin renk koşulunu kombinasyonla sayıp olasılığı hesaplar.',kalip='hikâyeli',
 kart='K-ABO-07 (kombinasyonla olasılık) · üç renkli bilye, hepsi aynı renk; bir renkte yeterli bilye yok',
 metin='Bir oyuncakçı, renkli bilyeleri tek bir torbada satıyor. Torbadaki bilyelerin renklere göre sayıları aşağıdaki tabloda verilmiştir. Müşteri torbadan bakmadan, aynı anda 3 bilye çekiyor.\nBuna göre çekilen üç bilyenin hepsinin aynı renkte olma olasılığı kaçtır?',
 istenen='Çekilen 3 bilyenin hepsinin aynı renkte olma olasılığı.',ip=['Her renk için o renkten üç bilye seçilip seçilemeyeceğini ayrı ayrı kontrol et.'],bilgi=[KOM],sekil=tablo_svg(['Renk','Bilye sayısı'],[[r,str(nn)] for r,nn in RN.items()]),
 puf='Kombinasyonda bir grupta yeterli eleman yoksa o grubun katkısı sıfırdır; bunu atlamamak için her grubu ayrı kontrol et.')

# ================= 13 orta · Venn şeması, öncüllü =================
a_,ab_,b_,d_=12,6,18,24; N=a_+ab_+b_+d_; assert N==60
PA=Fr(a_+ab_,N); PB=Fr(b_+ab_,N); PAB=Fr(ab_,N)
I=(Fr(ab_,ab_+b_)==Fr(1,4)); II=(PAB==PA*PB); III=(Fr(a_+ab_+b_,N)==Fr(3,5)); assert (I,II,III)==(True,False,True) and (PA,PB,PAB)==(Fr(3,10),Fr(2,5),Fr(1,10)) and PA+PB==Fr(7,10)
dogru=kume((I,II,III)); assert dogru=='I ve III'
qo('0013',[A('I. yargıyı sına','Tiyatro bilindiğinde örnek uzay tiyatro kulübündeki 6 + 18 = 24 öğrencidir; bunların 6’sı satranç kulübündedir.','P(S | T) = 6/24 = 1/4 ⇒ I doğru'),
           A('II. yargıyı sına','Bağımsızlık için P(S ∩ T) = P(S) × P(T) olmalıdır.','P(S) = 18/60, P(T) = 24/60 · 3/10 × 2/5 = 3/25 ≠ 1/10 ⇒ II yanlış'),
           A('III. yargıyı sına','En az birine üye olanlar, kulüplerin dışında kalan 24 öğrenci hariç diğerleridir.','(12 + 6 + 18)/60 = 3/5 ⇒ III doğru'),
           A('Sonucu yaz','Doğru olanlar I ve III’tür.','I ve III')],
 dogru,[('Yalnız I','II’yi doğru yorumlamış; III’te P(S) + P(T) = 3/10 + 2/5 = 7/10 yazıp birleşimin kesişimini çıkarmamış, III’ü yanlış saymış.','bilgi'),('Yalnız II','I’de payda olarak satranç kulübünü alıp 6/18 bulmuş; kesişimleri boş olmadığı için olayları bağımsız sanmış; III’te 7/10 bulmuş.','bilgi'),('I ve II','I’i doğru bulmuş; kesişimin boş olmamasını bağımsızlık sanmış; III’te kesişimi çıkarmayıp 7/10 bulmuş.','bilgi'),('II ve III','I’de payda olarak satranç kulübünü alıp 6/18 bulmuş; kesişimleri boş olmadığı için olayları bağımsız sanmış; III’ü doğru hesaplamış.','bilgi')],
 sira=OS3,
 tipId='ol-kosullu',tip='Koşullu olasılık',z='orta',alt='Venn Şeması',kaz='Venn şemasındaki öğrenci sayılarından koşullu olasılığı, bağımsızlığı ve birleşimi değerlendirir.',kalip='öncüllü',
 kart='K-ABO-04 (Venn şemasında koşullu olasılık) · iki kulüp, üç yargı: koşullu, bağımsızlık, birleşim',
 metin='Bir sınıftaki öğrencilerin satranç (S) ve tiyatro (T) kulüplerine üyeliği şekildeki Venn şemasında gösterilmiştir; şemadaki sayılar ilgili bölgedeki öğrenci sayısıdır. Sınıftan rastgele bir öğrenci seçiliyor.\nI. Seçilen öğrencinin tiyatro kulübüne üye olduğu bilindiğine göre satranç kulübüne de üye olma olasılığı 1/4’tür.\nII. Satranç kulübüne üye olma ile tiyatro kulübüne üye olma olayları bağımsızdır.\nIII. Seçilen öğrencinin iki kulüpten en az birine üye olma olasılığı 3/5’tir.\nBuna göre bu yargılardan hangileri doğrudur?',
 istenen='Doğru olan yargılar.',ip=['Her yargıyı şemadaki sayılardan ayrı ayrı hesapla; bağımsızlık için çarpım koşulunu dene.'],bilgi=[KOS,BAG],sekil=venn_fig(a_,ab_,b_,d_,'Satranç (S)','Tiyatro (T)'),
 puf='Venn şemasında koşul, paydadaki bölgeyi belirler; bağımsızlık kesişimin boş olmasıyla değil çarpım eşitliğiyle sınanır.')

# ================= 14 orta · çark, tekrarlı deneme =================
DIL=[('Kırmızı',90,'red!30'),('Mavi',120,'blue!30'),('Yeşil',150,'green!30')]; assert sum(d[1] for d in DIL)==360
pr=[Fr(d[1],360) for d in DIL]
v=sum(pr[a_i]*pr[b_i]*pr[c_i]*pr[d_i] for a_i,b_i,c_i,d_i in product(range(3),repeat=4) if [a_i,b_i,c_i,d_i].count(1)==2); assert v==Fr(8,27)==comb(4,2)*Fr(1,3)**2*Fr(2,3)**2
e=[Fr(1,3)**2*Fr(2,3)**2,1-(4*Fr(1,3)**3*Fr(2,3)+Fr(1,3)**4),1-(Fr(2,3)**4+4*Fr(1,3)*Fr(2,3)**3),4*Fr(1,3)*Fr(2,3)**3]
assert e==[Fr(4,81),Fr(8,9),Fr(11,27),Fr(32,81)] and len({v,*e})==5
q('0014',[A('Bir çevirmedeki olasılığı bul','Bölgenin olasılığı merkez açısının 360°’ye oranıdır: mavi için 120/360.','p = 1/3 · 1 − p = 2/3'),
          A('Tekrarlı deneme kalıbını kur','4 çevirmede tam 2 kez mavi gelmesi için hangi 2 çevirmenin mavi olacağı C(4, 2) yolla seçilir.','C(4, 2) × (1/3)² × (2/3)²'),
          A('Hesapla','C(4, 2) = 6; (1/3)² = 1/9; (2/3)² = 4/9.','6 × 1/9 × 4/9 = 24/81 = 8/27')],
 v,[(e[0],'C(4, 2) = 6 çarpanını (hangi çevirmelerin mavi olacağını) unutmuş.','bilgi'),(e[3],'“Tam 2 kez” yerine tam 1 kez mavi gelme olasılığını (4 × 1/3 × (2/3)³) hesaplamış.','dikkat'),(e[2],'“Tam 2 kez” yerine “en az 2 kez” mavi gelme olasılığını hesaplamış.','dikkat'),(e[1],'“Tam 2 kez” yerine “en çok 2 kez” mavi gelme olasılığını (1 − 8/81 − 1/81) hesaplamış.','dikkat')],
 tipId='ol-tekrar',tip='Tekrarlı bağımsız denemeler',z='orta',alt='Çark ve Tekrarlı Deneme',kaz='Çarkın bölge açılarından olasılığı bulup tekrarlı bağımsız denemede tam k başarı olasılığını hesaplar.',kalip='hikâyeli',
 kart='K-ABO-08 (tekrarlı bağımsız deneme) · çark açıları, dört çevirme, tam iki başarı',
 metin='Bir televizyon yarışmasında yarışmacı, şekildeki çarkı art arda 4 kez çeviriyor. Her çevirmede çarkın ibresi bölgelerden birinde duruyor; ibre bir bölgede, o bölgenin merkez açısı ile orantılı bir olasılıkla duruyor ve çevirmeler birbirini etkilemiyor.\nBuna göre ibrenin bu 4 çevirmenin tam 2 tanesinde mavi bölgede durma olasılığı kaçtır?',
 istenen='İbrenin 4 çevirmede tam 2 kez mavi bölgede durma olasılığı.',ip=['Önce tek bir çevirmede mavi bölgede durma olasılığını çarkın verisinden bul.'],bilgi=[TEK],sekil=cark_fig(DIL),
 puf='“Tam k kez” ifadesinde C(n, k) çarpanı, başarıların hangi denemelerde olacağını seçer.')

# ================= 15 zor · iki açılımın çarpımı =================
v=kat((1+x)**4*(1-2*x)**3,x**3); assert v==8
def carp(s2=-2,ihmal=(),binom2=True):
    top=0
    for i in range(4):
        j=3-i
        if i in ihmal: continue
        top+=comb(4,i)*((comb(3,j) if binom2 else 1)*s2**j)
    return top
e=[comb(4,3)*1+comb(4,0)*(-8), carp(s2=2), 4+48-36+8, 4+48+36-8]
assert e==[-4,96,24,80] and len({v,*e})==5 and carp()==8 and 4*1+6*(-6)+4*12*0==-32
q('0015',[A('Açılımları yaz','İki çarpanın açılımı ayrı ayrı yazılır.','(1 + x)⁴ = 1 + 4x + 6x² + 4x³ + x⁴ · (1 − 2x)³ = 1 − 6x + 12x² − 8x³'),
          A('x³ veren çiftleri bul','Üslerin toplamı 3 olan terim çiftleri çarpılır.','1 × (−8x³) · 4x × 12x² · 6x² × (−6x) · 4x³ × 1'),
          A('Çarpımları hesapla','Her çiftin katsayısı bulunur.','−8 · 48 · −36 · 4'),
          A('Topla','Dört çarpım toplanır.','−8 + 48 − 36 + 4 = 8')],
 8,[(-4,'Yalnız uç terim çiftlerini (1 × (−8x³) ve 4x³ × 1) almış; ortadaki iki çifti atlamış.','dikkat'),(24,'1 × (−8x³) çarpımının işaretini atlayıp +8 almış: 4 + 48 − 36 + 8.','islem'),(80,'6x² × (−6x) çarpımını +36 alıp işareti kaçırmış: 4 + 48 + 36 − 8.','islem'),(96,'(1 − 2x)³ açılımında işaretleri ihmal edip bütün terimleri pozitif almış.','islem')],
 tipId='bn-ozellik',tip='Binom açılımının özellikleri ve çarpımı',z='orta',alt='Açılım Çarpımı',kaz='İki binom açılımının çarpımında belirli bir terimin katsayısını terim çiftlerini toplayarak bulur.',kalip='düz',
 kart='K-ABO-03 (iki açılımın çarpımı) · (1 + x)⁴ ve (1 − 2x)³; işaretli ikinci çarpan',
 metin='(1 + x)⁴ · (1 − 2x)³\nçarpımının açılımında x³ lü terimin katsayısı kaçtır?',
 istenen='Çarpımda x³ lü terimin katsayısı.',ip=['x³ ü üretecek, kuvvetleri toplamı 3 olan terim çiftlerinin hepsini bir tabloda listelemeyi dene.'],bilgi=[BIN,OZ],
 puf='Çarpım açılımında istenen kuvvet, üs toplamı o kuvvete eşit olan terim çiftlerinin katsayı çarpımlarının toplamıdır.')

# ================= 16 zor · ardışık katsayı oranı =================
sol=[(n,k) for n in range(2,200) for k in range(1,n) if comb(n,k)*1==2*comb(n,k-1) and 3*comb(n,k)==2*comb(n,k+1)]; assert sol==[(14,5)]
n_,k_=sp.symbols('n k')
def coz(r1,r2):
    s=sp.solve([sp.Eq(r1,2),sp.Eq(r2,sp.Rational(3,2))],[n_,k_],dict=True); return s
dg=coz((n_-k_+1)/k_,(n_-k_)/(k_+1)); assert dg==[{n_:14,k_:5}]
eA=coz((n_-k_)/k_,(n_-k_-1)/(k_+1)); eB=coz((n_-k_+1)/k_,(n_-k_-1)/(k_+1)); eD=coz((n_-k_+1)/k_,(n_-k_+1)/(k_+1))
assert (eA[0][n_],eB[0][n_],eD[0][n_],dg[0][k_])==(15,20,8,5)
q('0016',[A('Oranları n ve k ile yaz','Ardışık üç katsayı C(n, k − 1), C(n, k), C(n, k + 1) olsun. İkinci birinciden 2 kat, üçüncü ikinciden 3/2 kat büyüktür.','C(n, k)/C(n, k − 1) = (n − k + 1)/k = 2 · C(n, k + 1)/C(n, k) = (n − k)/(k + 1) = 3/2'),
          A('k’yı bul','İlk eşitlikten n = 3k − 1 çıkar; ikinci eşitlikte yerine yazılır.','2(3k − 1 − k) = 3(k + 1) ⇒ 4k − 2 = 3k + 3 ⇒ k = 5'),
          A('n’yi hesapla','n = 3k − 1 bağıntısında k yerine 5 yazılır.','n = 3 × 5 − 1 = 14')],
 14,[(5,'Sorulan n yerine bulduğu k değerini (5) cevap yazmış.','dikkat'),(8,'İkinci oranı (n − k + 1)/(k + 1) yazıp bağıntıyı yanlış kurmuş; k = 3 ve n = 8 bulmuş.','bilgi'),(15,'Birinci oranı (n − k)/k, ikinci oranı (n − k − 1)/(k + 1) alıp indeksleri bir kaydırmış; n = 15 bulmuş.','bilgi'),(20,'Birinci oranı doğru, ikinci oranı (n − k − 1)/(k + 1) yazmış; k = 7 ve n = 20 bulmuş.','bilgi')],
 tipId='bn-pascal',tip='Pascal üçgeni ve ardışık katsayılar',z='zor',alt='Ardışık Katsayılar',kaz='(1 + x)ⁿ açılımında ardışık katsayıların oranından n’yi bulur.',kalip='düz',
 kart='K-ABO-02 (ardışık katsayı oranı) · 1 : 2 : 3 oranı, iki denklemli sistem',
 metin='n pozitif bir tam sayı olmak üzere, (1 + x)ⁿ ifadesinin açılımında ardışık üç terimin katsayıları sırasıyla 1, 2 ve 3 ile orantılıdır.\nBuna göre n kaçtır?',
 istenen='Ardışık üç katsayının 1 : 2 : 3 oranında olduğu açılımdaki n değeri.',ip=['Ardışık binom katsayıları arasında n ve k’yı içeren bir oran bağıntısı var mı?'],bilgi=[BIN,ORN],
 puf='Ardışık katsayılar arasındaki oran, n ve k’ya bağlı sade bir ifade olarak yazılabilir.')

# ================= 17 zor · üç makine, koşullu olasılık (Bayes) =================
MK=[('X makinesi',Fr(1,2),Fr(1,20)),('Y makinesi',Fr(3,10),Fr(1,10)),('Z makinesi',Fr(1,5),Fr(1,4))]; assert sum(m[1] for m in MK)==1
yol=[m[1]*m[2] for m in MK]; tum=sum(yol); assert tum==Fr(21,200)
v=yol[2]/tum; assert v==Fr(10,21)
e=[yol[2],MK[2][2],MK[2][2]/sum(m[2] for m in MK),MK[2][1]]; assert e==[Fr(1,20),Fr(1,4),Fr(5,8),Fr(1,5)] and len({v,*e})==5
q('0017',[A('Kusurlu ürüne giden yolları yaz','Her makineden kusurlu ürüne giden yolun olasılığı, makinenin üretim payı ile kusurlu oranının çarpımıdır.','X: 1/2 × 1/20 = 1/40 · Y: 3/10 × 1/10 = 3/100 · Z: 1/5 × 1/4 = 1/20'),
          A('Kusurlu olma olasılığını bul','Üç yol toplanır; ortak payda 200 alınır.','5/200 + 6/200 + 10/200 = 21/200'),
          A('Koşullu olasılığı yaz','Ürünün kusurlu olduğu bilindiğine göre Z’den gelme olasılığı, Z yolunun toplama oranıdır.','(1/20) / (21/200) = 10/21')],
 v,[(e[0],'Yalnız Z makinesi üzerinden kusurlu ürüne giden yolun olasılığını (1/20) yazmış, toplama bölmemiş.','dikkat'),(e[3],'Z makinesinin üretim payını (1/5) cevap sanmış.','bilgi'),(e[1],'Z makinesinin kusurlu üretme olasılığını (1/4) yazıp koşulun yönünü ters almış.','bilgi'),(e[2],'Kusurlu oranlarını (1/20 + 1/10 + 1/4) toplayıp üretim paylarını hesaba katmamış.','bilgi')],
 tipId='ol-agac',tip='Ağaç şeması ve koşullu olasılık',z='zor',alt='Koşullu Olasılık (Bayes)',kaz='Üç kollu ağaç şemasında kusurlu ürünün belirli makineden gelme olasılığını koşullu olasılıkla hesaplar.',kalip='hikâyeli',
 kart='K-ABO-06 (ağaç şeması, koşullu olasılık) · üç makine, kusurlu oranları, “kusurlu bilindiğine göre” sorusu',
 metin='Bir fabrikada üretilen ürünler X, Y ve Z makinelerinden birinden çıkmaktadır. Her makinenin toplam üretimdeki payı ve ürettiği ürünün kusurlu ya da sağlam çıkma olasılığı şekildeki ağaç şemasında gösterilmiştir. Gün sonunda üretimden rastgele bir ürün seçiliyor ve ürünün kusurlu olduğu görülüyor.\nBuna göre bu ürünün Z makinesinde üretilmiş olma olasılığı kaçtır?',
 istenen='Kusurlu ürünün Z makinesinden gelmiş olma olasılığı.',ip=['Kusurlu sonucuna giden bütün yolların toplamının, Z yolunun içindeki payını düşün.'],bilgi=[AGA,BAY],
 sekil=agac_fig([(m[0],m[1],[('Kusurlu',m[2]),('Sağlam',1-m[2])]) for m in MK],h=2.1,dy=0.5,x1=2.0,x2=2.9,x3=3.9,x4=5.7),
 puf='Koşullu soruda payda “bilinen sonuca giden bütün yollar”dır, yalnız kaynağın payı değil.')

# ================= 18 zor · ızgara yolları, kapalı sokak =================
W,Hh=5,3; KAP=[((2,0),(2,1)),((3,2),(4,2))]; C=(1,2)
def yollar(kap):
    cl={frozenset(c) for c in kap}; res=[]
    def go(px,py,p):
        if (px,py)==(W,Hh): res.append(p); return
        if px<W and frozenset([(px,py),(px+1,py)]) not in cl: go(px+1,py,p+[(px+1,py)])
        if py<Hh and frozenset([(px,py),(px,py+1)]) not in cl: go(px,py+1,p+[(px,py+1)])
    go(0,0,[(0,0)]); return res
ac=yollar(KAP); hep=yollar([]); assert (len(ac),len(hep))==(30,56)
K=sum(C in p for p in ac); Kh=sum(C in p for p in hep); assert (K,Kh)==(9,15)
v=Fr(K,len(ac)); assert v==Fr(3,10)
e=[Fr(Kh,len(hep)),Fr(K,len(hep)),Fr(len(ac),len(hep)),Fr(K,Kh)]; assert e==[Fr(15,56),Fr(9,56),Fr(15,28),Fr(3,5)] and len({v,*e})==5
q('0018',[A('Açık yolları say','A’dan B’ye 5 sağ, 3 yukarı adımla C(8, 3) = 56 yol vardır; kapalı sokaklardan geçenler bu sayıdan çıkarılır.','56 yoldan 26’sı kapalı sokaktan geçer ⇒ 30 açık yol'),
          A('C’den geçen açık yolları say','A’dan C’ye açık yol sayısı ile C’den B’ye açık yol sayısı çarpılır.','3 × 3 = 9'),
          A('Olasılığı yaz','Elverişli açık yol sayısı bütün açık yollara bölünür.','9/30 = 3/10')],
 v,[(e[1],'Elverişli yol sayısını doğru bulmuş (9) ama paydaya kapalı sokaklar dahil bütün 56 yolu yazmış.','dikkat'),(e[0],'Kapalı sokakları hiç dikkate almamış: C’den geçen 15 yolu 56 yola bölmüş.','dikkat'),(e[2],'Açık yolların bütün yollara oranını (30/56) hesaplamış.','dikkat'),(e[3],'Payı doğru bulup paydayı kapalı sokaklar yokmuş gibi C’den geçen 15 yol almış.','bilgi')],
 tipId='ol-sayma',tip='Sayma ile olasılık',z='zor',alt='Yol Sayma',kaz='Kapalı sokaklı ızgarada en kısa yolları sayıp bir noktadan geçme olasılığını hesaplar.',kalip='hikâyeli',
 kart='K-ABO-07 (yol sayma ve olasılık) · ızgara, iki kapalı sokak, ara nokta',
 metin='Bir mahallenin sokakları şekilde gösterilmiştir. Belediye, kırmızı ile işaretlenen iki sokağı yol çalışması nedeniyle kapatmıştır. Bir kurye A kavşağından B kavşağına, yalnızca doğuya (sağa) ve kuzeye (yukarı) giderek ve kapalı sokakları kullanmadan ulaşıyor; mümkün olan yollardan her birini eşit olasılıkla seçiyor.\nBuna göre kuryenin C kavşağından geçme olasılığı kaçtır?',
 istenen='Kuryenin C kavşağından geçme olasılığı.',ip=['Kapalı sokaklar hem elverişli yolları hem de bütün yolları etkiler; ikisini de aynı koşulla say.'],bilgi=[YOL],sekil=yol_fig(W,Hh,KAP,C),
 puf='Kısıtlı yol sayımında hem payı hem paydayı aynı kısıtla say; sonra ara noktadan geçen yolları iki parça olarak çarp.')

# ================= 19 zor · hileli para, tek/çift, öncüllü =================
p=Fr(1,3); pr_=lambda k:comb(5,k)*p**k*(1-p)**(5-k)
tab={k:sum(Fr(1,3)**sum(s)*Fr(2,3)**(5-sum(s)) for s in product((0,1),repeat=5) if sum(s)==k) for k in range(6)}; assert all(tab[k]==pr_(k) for k in range(6))
tekP=sum(tab[k] for k in (1,3,5)); cift=sum(tab[k] for k in (0,2,4)); assert (tekP,cift)==(Fr(121,243),Fr(122,243)) and cift-tekP==(Fr(2,3)-p)**5
I=(tekP>cift); II=(tab[0]<tab[1]); III=(1-tab[0]>Fr(9,10)); assert (I,II,III)==(False,True,False) and tab[0]==Fr(32,243) and tab[1]==Fr(80,243) and 1-tab[0]==Fr(211,243)
OS19=['Yalnız I','Yalnız II','I ve II','II ve III','I, II ve III']; dogru=kume((I,II,III)); assert dogru=='Yalnız II' and dogru in OS19
qo('0019',[A('Olasılıkları hesapla','Tura olasılığı 1/3, yazı olasılığı 2/3’tür; tam k kez tura gelme olasılığı C(5, k) × (1/3)ᵏ × (2/3)⁵⁻ᵏ’dır.','P(0) = 32/243 · P(1) = 80/243'),
           A('I. yargıyı sına','Çift sayıda tura gelmesi için k = 0, 2, 4; tek için k = 1, 3, 5 toplanır. Çift sayıda tura olasılığı biraz fazladır.','P(çift) = 122/243 · P(tek) = 121/243 ⇒ I yanlış'),
           A('II ve III’ü sına','32/243 < 80/243 olduğundan II doğrudur. En az bir tura olasılığı 1 − 32/243’tür; bu değer 9/10’dan küçüktür.','211/243 ≈ 0,87 < 0,9 ⇒ III yanlış'),
           A('Sonucu yaz','Yalnız II doğrudur.','Yalnız II')],
 dogru,[('Yalnız I','I’i hesapsız doğru saymış (tura az olasılıklı olduğundan tek sayıda turayı daha olası sanmış); II’de C(5, 1) çarpanını unutup P(1) = 16/243 bulduğundan II’yi yanlış saymış.','bilgi'),('I ve II','I’i hesapsız doğru saymış (tek sayıda turayı daha olası sanmış); II ve III’ü doğru değerlendirmiş.','dikkat'),('II ve III','I’i yanlış bulmuş; hiç tura gelmeme olasılığını (1/3)⁵ = 1/243 alıp III’ü doğru saymış.','bilgi'),('I, II ve III','I’i hesapsız doğru saymış; hiç tura gelmeme olasılığını (1/3)⁵ = 1/243 alıp II’yi ve III’ü doğru bulmuş.','bilgi')],
 sira=OS19,
 tipId='ol-tekrar',tip='Tekrarlı bağımsız denemeler',z='zor',alt='Hileli Para',kaz='Hileli paranın tekrarlı atışlarında tam, en az ve tek-çift olasılıklarını karşılaştırır.',kalip='öncüllü',
 kart='K-ABO-08 (tekrarlı bağımsız deneme, tek–çift) · p = 1/3, beş atış, üç yargı',
 metin='Tura gelme olasılığı 1/3 olan hileli bir madeni para art arda 5 kez atılıyor.\nI. Tura sayısının tek sayı olma olasılığı, çift sayı olma olasılığından büyüktür.\nII. Hiç tura gelmeme olasılığı, tam bir kez tura gelme olasılığından küçüktür.\nIII. En az bir kez tura gelme olasılığı 9/10’dan büyüktür.\nBuna göre bu yargılardan hangileri doğrudur?',
 istenen='Doğru olan yargılar.',ip=['Her yargıdaki olasılığı C(5, k) kalıbıyla yaz ve karşılaştırmayı pay paydası ortak olacak biçimde yap.'],bilgi=[TEK,KAT],
 puf='“En az bir” için 1 − P(hiç) kullan; olasılıkları karşılaştırırken ortak paydaya getir.')

# ================= 20 zor · lamba paneli, yeni nesil =================
DUR=['yanik','?','?','bozuk','?','?']; ser=[i for i,d in enumerate(DUR) if d=='?']
def asiri(L): return any(L[i] and L[i+1] for i in range(5))
ok=0
for s in product((0,1),repeat=4):
    L=[1,s[0],s[1],0,s[2],s[3]]; ok+=not asiri(L)
v=Fr(ok,16); assert (ok,v)==(6,Fr(3,8))
n_ok=sum(1 for s in product((0,1),repeat=6) if not asiri(s)); assert n_ok==21
e=[Fr(6,64),Fr(21,64),Fr(8,16),Fr(12,16)]
f1=sum(1 for s in product((0,1),repeat=4) if not (s[2] and s[3]) and True and not (0)); assert f1==12 and e[3]==Fr(f1,16)
f2=sum(1 for s in product((0,1),repeat=4) if s[0]==0 ); assert f2==8 and e[2]==Fr(f2,16) and len({v,*e})==5
q('0020',[A('Kurallara göre sınırla','1. lamba yanık olduğundan 2. lamba yanık olamaz; 4. lamba arızalı olduğundan 3. ve 5. lambalar için ek kısıt yoktur.','2. lamba sönük'),
          A('Kalan lambaları incele','3. lamba serbesttir (iki yanında sönük lamba var). 5. ve 6. lambaların ikisi birden yanık olamaz.','3. lamba: 2 durum · 5. ve 6.: SS, SY, YS ⇒ 3 durum'),
          A('Olasılığı bul','Durumu bilinmeyen 4 lambanın 2⁴ = 16 eş olasılıklı durumundan uygun olanlar sayılır.','(2 × 3)/16 = 6/16 = 3/8')],
 v,[(e[0],'Sabit durumdaki lambaları da değişken sayıp paydaya 2⁶ = 64 yazmış; uygun durumları 6 saymış.','dikkat'),(e[1],'1. ve 4. lambaların durumunu hiç kullanmamış: 6 lambanın kısıtsız 21 uygun dizilişini 64 durumdan almış.','dikkat'),(e[2],'5. ve 6. lambaların birlikte yanamayacağı kısıtını unutmuş; yalnız 2. lambayı sönük almış: 8/16.','dikkat'),(e[3],'1. lambanın yanık olmasının 2. lambayı etkilediğini unutmuş; yalnız 5. ve 6. lamba kısıtını uygulamış: 12/16.','dikkat')],
 tipId='ol-sayma',tip='Sayma ile olasılık',z='orta',alt='Kısıtlı Dizilim',kaz='Tanımlanan bir kısıta uyan lamba dizilimlerinin olasılığını sayarak hesaplar.',kalip='yeni nesil',
 kart='K-ABO-07 (kısıtlı dizilişte olasılık) · yan yana iki yanık lamba yasak, bazı lambalar sabit',
 metin='Bir ışık panelinde 6 lamba yan yana dizilmiştir. Yan yana bulunan herhangi iki lamba aynı anda yanıyorsa panele “aşırı yüklü” denir. Şekilde 1. lambanın yanık olduğu, 4. lambanın arızalı olduğu (hiçbir zaman yanamayacağı) ve diğer lambaların durumunun bilinmediği görülmektedir. Durumu bilinmeyen her lamba, diğerlerinden bağımsız olarak 1/2 olasılıkla yanık ya da sönüktür.\nBuna göre panelin “aşırı yüklü” olmama olasılığı kaçtır?',
 istenen='Panelin aşırı yüklü olmama olasılığı.',ip=['Önce şekildeki sabit lambaların komşularına hangi kısıtı getirdiğine bak.'],bilgi=[DUR_B],sekil=lamba_fig(DUR),
 puf='Kısıtlı dizilişlerde sabit lambalardan başlayıp zorunlu durumları belirle, sonra kalanları say.')

for qq in P.ANA: qq['kardes']=None
P.yaz(os.path.join(HD,'binom-1.json'),os.path.join(SCR,'bos-binom.json'))
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=UK))['kartlar'].append(c['id'])
json.dump(dict(konu='Binom ve Olasılık',surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 AYT Matematik çıkmış soruları ve yayın soru bankaları (yalnız mantık), MEB 11–12. sınıf müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),open(os.path.join(HV,'kartlar','binom.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
