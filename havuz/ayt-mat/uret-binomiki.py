"""AYT Matematik · Binom ve Olasılık, 2. dalga (20 soru). Her doğru ve çeldirici değer kaba kuvvet/sympy ile assert edilir. Kardeş yok, ipucu 1."""
import sys,os
HD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(HD,'..')
sys.path.insert(0,os.path.join(HV,'tyt-mat')); sys.path.insert(0,HV)
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
from itertools import product,combinations,permutations
from math import comb
import sympy as sp
H.KONU='Binom ve Olasılık'
HD=os.path.dirname(os.path.abspath(__file__))
SCR='/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/binomiki'; os.makedirs(SCR,exist_ok=True)
UK='amat|Binom ve Olasılık'
P=Parti('binomiki','Binom ve Olasılık',UK,ders='AYT Matematik',idon='aytmat')
KY='ÖSYM 2018–2026 AYT Matematik (binom açılımı ve olasılık soruları; yalnız mantık) · 345 AYT Matematik Soru Bankası · Bilgi Sarmal AYT denemeleri · MEB 11–12. sınıf'
def fs(x):
    x=Fr(x); return ('−' if x<0 else '')+(str(abs(x.numerator)) if x.denominator==1 else f'{abs(x.numerator)}/{x.denominator}')
def q(no,ad,dogru,yan,**k):
    vals=[Fr(dogru)]+[Fr(y[0]) for y in yan]; assert len(set(vals))==5,vals
    sira=[fs(v) for v in sorted(vals)]
    mk(P,no,ad=ad,adim=len(ad),dogru=fs(dogru),yan=[(fs(y[0]),y[1],y[2]) for y in yan],sira=sira,**k)
def qo(no,ad,dogru,yan,sira,**k): mk(P,no,ad=ad,adim=len(ad),dogru=dogru,yan=yan,sira=sira,**k)
def fig(body,font='\\small'): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font='+font+']\n'+body+'\n\\end{tikzpicture}')
def kartla(*a): kart(*a,KY)
OS3=['Yalnız I','Yalnız II','I ve II','I ve III','II ve III']
def kume(t):
    L=[r for r,v in zip(['I','II','III'],t) if v]
    return 'Yalnız '+L[0] if len(L)==1 else ' ve '.join(L) if len(L)==2 else 'I, II ve III'

# ---------- bilgi kutuları ----------
GT=B('Genel terim ve üs eşleştirme','(a + b)ⁿ açılımında (k + 1). terim C(n, k) · aⁿ⁻ᵏ · bᵏ biçimindedir. Birden çok değişken varsa her değişkenin üssü ayrı ayrı eşitlenir. Örnek: (p² + q)⁴ açılımında p⁴q² li terim için q nun üssünden k = 2 bulunur; terim C(4, 2) · p⁴ · q² = 6p⁴q² olur')
ORT=B('Katsayıların aritmetik ortalaması','katsayıların aritmetik ortalaması, katsayılar toplamının terim sayısına bölünmesidir. (a·xᵖ + b·xᵠ)ⁿ açılımında katsayılar toplamı değişkenlere 1 verilerek (a + b)ⁿ, terim sayısı n + 1 bulunur. Örnek: (2x + 1/x)³ için toplam 3³ = 27, terim sayısı 4, ortalama 27/4’tür')
KATB=B('Aynı tabanlı çarpım ve ortak çarpan','xᵐ · xⁿ = xᵐ⁺ⁿ olduğundan (x³ + x)ⁿ gibi bir ifade x’in kuvvetleri ortak çarpana alınarak sade bir binom açılımı biçiminde yazılabilir. Örnek: (x⁴ + x²)⁵ = x¹⁰ · (x² + 1)⁵ olur')
ENB=B('Ardışık terimlerin katsayı oranı','(1 + cx)ⁿ açılımında (k + 1). terimin katsayısı C(n, k) · cᵏ’dır. Ardışık iki terimin katsayıları oranlanırsa C(n, k + 1) / C(n, k) = (n − k) / (k + 1) çarpanı oluşur; oran 1’den büyükken katsayılar artar, küçükken azalır. Örnek: C(6, 3) / C(6, 2) = 4/3’tür')
PSA=B('Pascal üçgeninde satırlar','n. satırın (satırlar 0’dan başlar) sayıları (1 + x)ⁿ açılımının katsayılarıdır. x yerine 1 yazılırsa C(n, 0) + C(n, 1) + … + C(n, n) = 2ⁿ, x yerine −1 yazılırsa C(n, 0) − C(n, 1) + C(n, 2) − … = 0 elde edilir (n ≥ 1). Örnek: 4. satır 1, 4, 6, 4, 1 olup toplamı 2⁴ = 16’dır')
YEN=B('Tanımlı kurallı üçgenler','kuralla verilen bir sayı üçgeninde önce ilk birkaç satır kurala göre doğrudan hesaplanır, sonra her sayı ile Pascal üçgenindeki sayı arasındaki ilişki (ya da satır toplamları arasındaki ilişki) aranır. Örnek: her sayı üstündeki iki sayının farkı ise ilk satırlar elle kurulup düzen sınanır')
OZD=B('Binom katsayılarının özellikleri','C(n, k) = C(n, n − k); C(n, k) + C(n, k + 1) = C(n + 1, k + 1); C(n, 0) + C(n, 1) + … + C(n, n) = 2ⁿ ve tek (ya da çift) sıradaki katsayıların toplamı 2ⁿ⁻¹’dir. Örnek: C(6, 2) = C(6, 4) = 15; C(4, 1) + C(4, 2) = C(5, 2) = 10')
BAG2=B('Birleşim ve bağımsız olaylar','P(A ∪ B) = P(A) + P(B) − P(A ∩ B) dir; A ve B bağımsızsa P(A ∩ B) = P(A) · P(B) olur. Örnek: P(A) = 1/2, P(B) = 1/3 ve olaylar bağımsızsa P(A ∪ B) = 1/2 + 1/3 − 1/6 = 2/3’tür')
CRK=B('Çarklar ve bağımsız deneyler','çarkta bir bölgenin olasılığı, bölgenin merkez açısının 360°’ye oranıdır. Ayrı çarkların sonuçları birbirini etkilemez; iki çarkta istenen sonuç çiftlerinin her birinin olasılığı çarpılır, uygun çiftler toplanır. Örnek: 120° lik bölgede durma olasılığı 1/3’tür')
GRF=B('Ağ üzerinde rastgele yürüyüş','her adımda bulunulan düğümün d komşusundan biri eş olasılıkla seçilirse her komşuya geçme olasılığı 1/d’dir. Bir yürüyüşün olasılığı, adım olasılıklarının çarpımıdır; aynı sonuca götüren farklı yürüyüşlerin olasılıkları toplanır. Örnek: 2 komşulu düğümden belirli komşuya geçme olasılığı 1/2’dir')
SYM=B('Kısıtlı yerleştirmede sayma','önce kısıtı sağlayan seçimler (hangi sütun, hangi satır, hangi kişi) çarpma kuralıyla sayılır; olasılık = uygun yerleşim sayısı / bütün yerleşimlerin sayısı. n kişinin n yere dizilişi n! tanedir. Örnek: 4 kişinin 4 koltuğa oturması 4! = 24 farklı biçimdedir')
KS2=B('“En az bir” koşulu ile koşullu olasılık','“en az bir” olayının tümleyeni “hiç yok” olayıdır; koşulda bu olay verilmişse örnek uzay “hiç yok” durumları çıkarılarak daralır: P(A | B) = s(A ∩ B) / s(B). Örnek: 10 kişiden 2 kişi seçilirken en az bir seçilenin belirli bir gruptan olması, bütün seçimlerden o gruptan hiç kimsenin seçilmediği seçimlerin çıkarılmasıyla sayılır')
AGB=B('Çok aşamalı seçimde ağaç ve koşullu olasılık','aşamalar yol olarak çizilir, yol üzerindeki olasılıklar çarpılır; sonuç bilindiğinde kaynak olasılığı P(kaynak | sonuç) = (kaynak yolunun olasılığı) / (sonuca giden bütün yolların toplamı) bulunur. Örnek: sonuca iki yoldan 1/6 ve 1/12 olasılıkla ulaşılıyorsa ilk yoldan gelme olasılığı (1/6) / (1/6 + 1/12) = 2/3’tür')
IAD=B('İadesiz çekimde olasılık','çekilen nesne geri konmuyorsa ikinci çekimde torbadaki sayılar değişir: P(A ∩ B) = P(A) · P(B | A). İlk çekim bilinmiyorsa ikinci çekimin olasılığı ilk çekimin bütün sonuçları toplanarak bulunur. Örnek: 2 beyaz 1 siyah toptan iadesiz çekilirken ilk topun beyaz, ikincinin siyah olma olasılığı 2/3 · 1/2 = 1/3’tür')
TBL=B('Tablodaki dağılımlardan bileşik olay','tablodaki her satır ayrı bir sonucun olasılığıdır; birbirinden bağımsız iki dağılımda bir sonuç çiftinin olasılığı çarpılarak, aynı olaya götüren çiftler toplanarak bulunur. Örnek: 1. dağılımda sonucun 2 olma olasılığı 1/4, 2. dağılımda 5 olma olasılığı 1/2 ise bu çiftin olasılığı 1/8’dir')
ISD=B('İadesiz sıralı seçim','n nesneden sırayla, geri koymadan seçim yapılırken ilk seçim n, ikinci n − 1, üçüncü n − 2 biçiminde olur; kısıtı en dar olan seçimden başlamak sayımı kolaylaştırır. Örnek: 5 kuponla 2 kişinin sırayla birer kupon çekmesi 5 · 4 = 20 farklı biçimdedir')
RAK=B('Rakamlarla sayı yazma ve koşullar','rakamları farklı sayı yazılırken sıfır başa gelemez; çift sayı için birler basamağı, 3’e bölünme için rakamlar toplamı incelenir. Örnek: {0, 1, 2} rakamlarıyla yazılabilen rakamları farklı üç basamaklı sayılar 102, 120, 201, 210’dur')

# ---------- kartlar ----------
kartla('K-ABO2-01','Terim, katsayı ortalaması ve eşit katsayılar','Değişkenlerin üsleri ayrı eşitlenerek k bulunur; ortalama için toplam ve terim sayısı, eşit katsayılar için C(n, i) = C(n, j) ⇒ n = i + j kullanılır.','Terim sayısını n sanmak; üssü yanlış eşlemek; katsayıdaki sayıyı kuvvetlendirmeyi unutmak.','orta','düz',3,'bn-katsayi2','Terim, ortalama ve eşit katsayılar')
kartla('K-ABO2-02','Pascal satırları, özdeşlikler ve tanımlı üçgenler','Satır toplamları ve tek/çift sıradaki toplamlar x = 1, x = −1 ile; yeni kurallı üçgende satır toplamları kurala göre kurulur.','Satırı 1’den başlatmak; tek sıra toplamıyla tüm satır toplamını karıştırmak; kuraldaki ek sayıyı unutmak.','zor','şekilli',4,'bn-satir2','Pascal satırları ve özdeşlikler')
kartla('K-ABO2-03','Bağımsız olaylarda birleşim ve çarklar','P(A ∪ B) = P(A) + P(B) − P(A ∩ B); çarkta bölge olasılığı açıdan okunur, çiftler çarpılıp toplanır.','Bağımsız olayları ayrık sanmak; çarkta bölgeleri eş olasılıklı almak.','orta','şekilli',3,'ol-bagimsiz2','Bağımsız olaylar ve çarklar')
kartla('K-ABO2-04','Ağda rastgele yürüyüş','Her adımda komşu sayısına göre dal olasılıkları çarpılır, aynı düğümde biten yürüyüşler toplanır.','Komşu sayısını bütün düğümler için aynı almak; yürüyüşlerden birini atlamak.','orta','şekilli',3,'ol-graf','Ağ şemasında rastgele yürüyüş')
kartla('K-ABO2-05','Sayma yöntemleriyle olasılık (yerleştirme, rakam, kupon)','Uygun ve bütün durumlar çarpma kuralıyla sayılır; kısıt önce uygulanır, koşullu durumda payda daralır.','Sırayı ya da kısıtı unutmak; paydayı yanlış evrende saymak.','orta','şekilli',3,'ol-sayma2','Kısıtlı sayma ile olasılık')
kartla('K-ABO2-06','Koşullu olasılık (grup seçimi, kart, öncül)','Koşul örnek uzayı daraltır; “en az bir” için tümleyen sayılır; iadesiz çekimde ikinci aşama sayıları değişir.','P(A | B) ile P(B | A) karıştırmak; paydayı koşulsuz uzaydan almak.','orta','tablo',3,'ol-kosullu2','Koşullu olasılık ve iadesiz çekim')
kartla('K-ABO2-07','Çok aşamalı seçim, ağaç ve Bayes','Aşamalar çarpılır, aynı sonuca giden yollar toplanır; sonuç bilindiğinde ilgili yol toplama bölünür.','Aşama olasılığını sabit saymak; paydada yalnız bir yolu almak.','zor','şekilli',4,'ol-agac2','Çok aşamalı seçim ve ağaç')
kartla('K-ABO2-08','Tablodaki dağılımlardan bileşik olay','İki bağımsız dağılımda uygun çiftler listelenir, çarpılıp toplanır; eşitlik durumu metne göre değerlendirilir.','Eşit duruma kural dışı davranmak; çiftlerden birini atlamak.','zor','tablo',4,'ol-sure','Dağılım tablosundan bileşik olay')

# ================= şekil yardımcıları =================
def pas_fig(rows,boyali=(),cizgi=True):
    w,h=0.95,0.78; o=[]
    for r in range(rows):
        o.append(f'\\node[font=\\scriptsize,anchor=east,gray!70!black] at ({-(rows-1)/2*w-0.55:.2f},{-r*h:.2f}) {{{r}. satır}};')
        for k in range(r+1):
            x=(k-r/2)*w; y=-r*h
            if (r,k) in boyali: o.append(f'\\node[draw,thick,rounded corners=2pt,fill=orange!35,minimum width=0.62cm,minimum height=0.55cm,inner sep=1pt,font=\\bfseries] at ({x:.2f},{y:.2f}) {{{comb(r,k)}}};')
            else: o.append(f'\\node at ({x:.2f},{y:.2f}) {{{comb(r,k)}}};')
    return fig('\n'.join(o))
def tri_fig(T,rows):
    w,h=1.0,0.8; o=[]
    for r in range(rows):
        o.append(f'\\node[font=\\scriptsize,anchor=east,gray!70!black] at ({-(rows-1)/2*w-0.6:.2f},{-r*h:.2f}) {{{r}. satır}};')
        for k in range(r+1):
            x=(k-r/2)*w; y=-r*h
            fl='blue!12' if k in (0,r) else 'green!22'
            o.append(f'\\node[draw,thick,rounded corners=2pt,fill={fl},minimum width=0.62cm,minimum height=0.55cm,inner sep=1pt] at ({x:.2f},{y:.2f}) {{{T[(r,k)]}}};')
    return fig('\n'.join(o))
def cark2_fig(c1,c2):
    o=[]
    for j,(ad,dil) in enumerate([('I. çark',c1),('II. çark',c2)]):
        cx=j*4.8; r=1.7; a0=90
        for (lab,aci,renk) in dil:
            a1=a0-aci; m=(a0+a1)/2
            o.append(f'\\fill[{renk}] ({cx},0) -- ({cx+r*__import__("math").cos(__import__("math").radians(a0)):.3f},{r*__import__("math").sin(__import__("math").radians(a0)):.3f}) arc ({a0}:{a1}:{r}) -- cycle;')
            o.append(f'\\draw[thick] ({cx},0) -- +({a0}:{r});')
            o.append(f'\\node[align=center,font=\\small] at ({cx+r*0.62*__import__("math").cos(__import__("math").radians(m)):.2f},{r*0.62*__import__("math").sin(__import__("math").radians(m)):.2f}) {{\\bfseries {lab}\\\\\\scriptsize {aci}$^\\circ$}};')
            a0=a1
        o.append(f'\\draw[very thick] ({cx},0) circle ({r}); \\fill ({cx},0) circle (0.07); \\node[font=\\small\\bfseries] at ({cx},-2.2) {{{ad}}};')
    return fig('\n'.join(o))
def graf_fig():
    P_={'A':(0,1.3),'B':(1.9,2.6),'C':(3.8,1.3),'D':(1.9,0)}
    E_=[('A','B'),('B','C'),('C','D'),('D','A'),('A','C')]
    o=[f'\\draw[thick] ({P_[a][0]},{P_[a][1]}) -- ({P_[b][0]},{P_[b][1]});' for a,b in E_]
    for n,(x,y) in P_.items():
        f='green!40' if n=='A' else 'blue!15'
        o.append(f'\\node[circle,draw,thick,fill={f},minimum size=0.7cm,inner sep=0,font=\\bfseries] at ({x},{y}) {{{n}}};')
    o.append('\\node[anchor=west,font=\\small] at (-0.4,-0.9) {A: kurbağanın başlangıç düğümü};')
    return fig('\n'.join(o))
def koltuk_fig(dolu):
    o=[]
    for c in range(3):
        o.append(f'\\node[font=\\small] at ({c*1.5+0.55},-0.4) {{{c+1}. sütun}};')
        for r in range(2):
            k=dolu.get((c,r)); f_='red!35' if k=='K' else 'blue!30' if k=='E' else 'white'
            o.append(f'\\draw[thick,fill={f_},rounded corners=3pt] ({c*1.5},{r*0.95}) rectangle ({c*1.5+1.1},{r*0.95+0.8});')
            if k: o.append(f'\\node[font=\\bfseries] at ({c*1.5+0.55},{r*0.95+0.4}) {{{k}}};')
    o.append('\\node[font=\\small,anchor=west] at (4.7,1.35) {K: kız, E: erkek};')
    return fig('\n'.join(o))
def kart_fig(vals):
    o=[]
    for i,v in enumerate(vals):
        f='yellow!35'
        o.append(f'\\node[draw,thick,rounded corners=3pt,fill={f},minimum width=0.85cm,minimum height=1.2cm,font=\\Large\\bfseries] at ({i*1.05:.2f},0) {{{v}}};')
    return fig('\n'.join(o))
def torba_fig(torbalar,ok=False):
    o=[]
    for j,(ad,k,m) in enumerate(torbalar):
        x0=j*4.6; bil=['K']*k+['M']*m
        o.append(f'\\draw[very thick] ({x0},1.9) -- ({x0},0) -- ({x0+3.3},0) -- ({x0+3.3},1.9);')
        o.append(f'\\node[font=\\small\\bfseries] at ({x0+1.65},2.3) {{{ad}}};')
        for i,b in enumerate(bil):
            r,c=divmod(i,3); x=x0+0.6+c*1.05; y=0.5+r*0.85
            f='red!40' if b=='K' else 'blue!35'
            o.append(f'\\node[circle,draw,thick,fill={f},minimum size=0.72cm,inner sep=0pt,font=\\small\\bfseries] at ({x:.2f},{y:.2f}) {{{b}}};')
    if ok:
        for j in range(len(torbalar)-1): o.append(f'\\draw[-{{Stealth}},very thick,orange!80!black] ({3.45+j*4.6},1.0) -- ({4.45+j*4.6},1.0) node[midway,above,font=\\scriptsize] {{bir top}};')
    o.append('\\node[font=\\small,anchor=north west] at (0,-0.35) {K: kırmızı top \\quad M: mavi top};')
    return fig('\n'.join(o))
def kapi_fig(n):
    o=[]; ren=['red!35','blue!30','green!35','orange!40','violet!35','yellow!50']
    for j,m in enumerate(n):
        x0=j*3.5
        o.append(f'\\node[draw,very thick,fill=gray!15,minimum width=1.6cm,minimum height=0.7cm,font=\\small\\bfseries] at ({x0+1.2},2.3) {{Kapı {j+1}}};')
        o.append(f'\\draw[thick] ({x0+1.2},1.95) -- ({x0+1.2},1.6);')
        cols=3 if m>3 else m; rows=(m+cols-1)//cols
        for i in range(m):
            r,c=divmod(i,cols)
            o.append(f'\\draw[thick,fill={ren[i%6]}] ({x0+c*0.75:.2f},{1.2-r*0.75:.2f}) rectangle ({x0+c*0.75+0.6:.2f},{1.2-r*0.75-0.55:.2f});')
    o.append('\\node[font=\\small,anchor=north west] at (0,-0.6) {Renkli kareler: kapının önündeki otoparklar};')
    return fig('\n'.join(o))
def kupon_fig(v):
    o=[]
    for i,x in enumerate(v):
        o.append(f'\\node[draw,thick,dashed,rounded corners=3pt,fill=yellow!30,minimum width=1.3cm,minimum height=1.0cm,font=\\bfseries] at ({i*1.6:.1f},0) {{{x} TL}};')
    return fig('\n'.join(o))

x,y=sp.symbols('x y')
def coef(expr,var,e): return sp.Poly(sp.expand(expr*var**60),var).coeff_monomial(var**(60+e))

# ================= 01 kolay · m + n (düz) =================
Z=sp.expand((x**3+2*y)**5); m1=Z.coeff(y,2).coeff(x,9); assert m1==40
v=m1+9; assert v==49
e=[10+9, comb(5,3)*8+6, 40+6, 2*comb(5,2)+9]; assert e==[19,86,46,29] and len({v,*e})==5
q('0001',[A('Genel terimi yaz','y’nin üssü 2 olduğundan k = 2’dir; x’in kuvveti (x³)⁵⁻² = x⁹ olur.','C(5, 2) × (x³)³ × (2y)²'),
          A('m ve n değerlerini bul','C(5, 2) = 10 ve 2² = 4 çarpılır; x’in üssü 9’dur.','m = 10 × 4 = 40 · n = 9'),
          A('Toplamı hesapla','m ile n toplanır.','m + n = 40 + 9 = 49')],
 49,[(19,'(2y)² ifadesindeki 2² = 4 çarpanını unutup m = 10 almış.','dikkat'),(29,'(2y)² yerine 2 · y² yazıp m = 2 × 10 = 20 bulmuş; n = 9.','islem'),(46,'x’in üssünü (x³)² = x⁶ alıp n = 6 bulmuş; m = 40.','dikkat'),(86,'k = 3 almış: C(5, 3) × 2³ = 80 ve x⁶ ⇒ 80 + 6.','bilgi')],
 tipId='bn-katsayi2',tip='Terim, ortalama ve eşit katsayılar',z='kolay',alt='Terim Üsleri',kaz='İki değişkenli binom açılımında bir terimin katsayısını ve üssünü bulur.',kalip='düz',
 kart='K-ABO2-01 (iki değişkenli terim, m + n) · ilk terimde üslü değişken, ikinci terimde sayı katsayısı',
 metin='m ve n tam sayılar olmak üzere,\n(x³ + 2y)⁵\nifadesinin açılımında terimlerden biri m·xⁿ·y² dir.\nBuna göre m + n toplamı kaçtır?',
 istenen='m + n toplamı.',ip=['y’nin üssünden genel terimdeki k değerine geç.'],bilgi=[GT],
 puf='İki değişkenli açılımda her değişkenin üssünü ayrı ayrı genel terimle eşleştir.')

# ================= 02 kolay · bağımsız birleşim =================
pa,pu=Fr(2,5),Fr(7,10); pb=(pu-pa)/(1-pa); assert pb==Fr(1,2) and pa+pb-pa*pb==pu
e=[pu-pa, pa*pb, (pu-pa)/pa, Fr(7,10)]; assert e[0]==Fr(3,10) and e[1]==Fr(1,5) and e[2]==Fr(3,4) and len({pb,*e})==5
q('0002',[A('Birleşim formülünü yaz','Bağımsız olaylarda P(A ∩ B) = P(A) · P(B) olduğundan birleşim formülü yalnız P(B) bilinmeyenli olur.','P(A ∪ B) = P(A) + P(B) − P(A) · P(B)'),
          A('Değerleri yerine koy','P(A) = 2/5 ve P(A ∪ B) = 7/10 yazılır.','7/10 = 2/5 + P(B) × (1 − 2/5) = 2/5 + 3/5 · P(B)'),
          A('P(B) yi çöz','Denklem düzenlenir.','3/5 · P(B) = 3/10 ⇒ P(B) = 1/2')],
 pb,[(e[0],'A ve B olaylarını ayrık sanıp P(B) = P(A ∪ B) − P(A) = 7/10 − 2/5 bulmuş.','dikkat'),(e[1],'Kesişim olasılığı P(A ∩ B) = 1/5’i bulup P(B) yerine yazmış.','dikkat'),(e[2],'Denklemi 3/10 ÷ P(A) = 3/10 ÷ (2/5) biçiminde, 1 − P(A) yerine P(A) ile bölerek çözmüş.','bilgi'),(e[3],'P(B) yerine birleşimin olasılığı 7/10’u yazmış.','dikkat')],
 tipId='ol-bagimsiz2',tip='Bağımsız olaylar ve çarklar',z='kolay',alt='Bağımsız Olaylar',kaz='Bağımsız iki olayda birleşim olasılığından bilinmeyen olasılığı bulur.',kalip='düz',
 kart='K-ABO2-03 (bağımsız olayların birleşimi) · P(A) ve P(A ∪ B) verilmiş',
 metin='A ve B bağımsız olaylardır.\nP(A) = 2/5 ve P(A ∪ B) = 7/10 olduğuna göre, P(B) kaçtır?',
 istenen='P(B) değeri.',ip=['Bağımsızlık, kesişim olasılığını P(A) ve P(B) cinsinden yazmanı sağlar.'],bilgi=[BAG2],
 puf='Birleşim formülünde kesişimi bağımsızlıkla çarpım olarak yazınca denklem tek bilinmeyenli olur.')

# ================= 03 kolay · iki çark (şekil) =================
C1=[(1,90,'blue!25'),(2,90,'orange!35'),(3,90,'green!30'),(4,90,'violet!30')]
C2=[(1,180,'blue!25'),(2,90,'orange!35'),(3,90,'green!30')]
p1={a:Fr(c,360) for a,c,_ in C1}; p2={a:Fr(c,360) for a,c,_ in C2}
def PT(f): return sum(p1[a]*p2[b] for a in p1 for b in p2 if f(a,b))
v=PT(lambda a,b:a+b>=5); assert v==Fr(7,16)
e=[PT(lambda a,b:a+b>5),PT(lambda a,b:a+b==5),Fr(sum(1 for a in p1 for b in p2 if a+b>=5),16),Fr(sum(1 for a in p1 for b in p2 if a+b>=5),12)]
assert e==[Fr(3,16),Fr(1,4),Fr(3,8),Fr(1,2)] and len({v,*e})==5
q('0003',[A('Bölge olasılıklarını oku','I. çarkta her bölge 90° olduğundan 1/4; II. çarkta 1 numaralı bölge 1/2, 2 ve 3 numaralı bölgeler 1/4 olasılıklıdır.','I: 1/4 · II: 1 → 1/2, 2 → 1/4, 3 → 1/4'),
          A('Uygun çiftleri belirle','Toplamı en az 5 yapan (I, II) çiftleri bulunur.','(2, 3), (3, 2), (3, 3), (4, 1), (4, 2), (4, 3)'),
          A('Olasılıkları çarpıp topla','Her çiftin olasılığı iki çarktaki olasılıkların çarpımıdır.','1/16 + 1/16 + 1/16 + 1/8 + 1/16 + 1/16 = 7/16')],
 v,[(e[0],'“En az 5” yerine “5’ten büyük” koşulunu almış; toplamı tam 5 olan (2, 3), (3, 2), (4, 1) çiftlerini atlamış.','dikkat'),(e[1],'Toplamı yalnız tam 5 olan çiftleri (2, 3), (3, 2), (4, 1) hesaplamış.','dikkat'),(e[2],'Uygun 6 çifti doğru saymış; ama bütün çiftleri 4 · 4 = 16 sanıp 6/16 yazmış.','bilgi'),(e[3],'II. çarkın bölgelerini eş olasılıklı alıp uygun 6 çiftin 12 çifte oranını yazmış.','bilgi')],
 tipId='ol-bagimsiz2',tip='Bağımsız olaylar ve çarklar',z='kolay',alt='İki Çark',kaz='Merkez açılarla verilen iki bağımsız çarkta toplamla ilgili olasılığı hesaplar.',kalip='şekilli',
 kart='K-ABO2-03 (iki bağımsız çark) · eş olmayan merkez açılar, toplam koşulu',
 metin='Şekildeki I. çark 4, II. çark 3 bölgeye ayrılmıştır; bölgelerin numaraları ve merkez açıları şekilde gösterilmiştir. Çarkların ibreleri birbirinden bağımsız olarak çevriliyor ve her çarkta ibre bir bölgede, o bölgenin merkez açısıyla orantılı bir olasılıkla duruyor.\nBuna göre ibrelerin gösterdiği numaraların toplamının en az 5 olma olasılığı kaçtır?',
 istenen='İki numaranın toplamının en az 5 olma olasılığı.',ip=['Çarkların bölgelerinin olasılıkları eşit değildir; önce her bölgenin olasılığını açıdan oku.'],bilgi=[CRK],sekil=cark2_fig(C1,C2),
 puf='Eşit olmayan açılı çarklarda bölgeleri sayma; olasılığı merkez açıdan hesapla.')

# ================= 04 orta · katsayı ortalaması, sabit terim (düz) =================
nn=[n for n in range(1,15) if Fr((3-2)**n,n+1)==Fr(1,7)]; assert nn==[6]
v=coef((3*x**2-2/x)**6,x,0); assert v==2160==comb(6,4)*9*16
e=[comb(6,2)*81*4,comb(6,4)*16,comb(6,4)*3*16,9*16]; assert e==[4860,240,720,144] and len({v,*e})==5
q('0004',[A('n yi bul','x yerine 1 yazınca katsayılar toplamı bulunur; terim sayısı n + 1 dir.','(3 − 2)ⁿ / (n + 1) = 1/7 ⇒ n + 1 = 7 ⇒ n = 6'),
          A('Genel terimde x in kuvvetini sıfırla','(3x² − 2/x)⁶ için k. terimde x in kuvveti 2(6 − k) − k dır.','12 − 3k = 0 ⇒ k = 4'),
          A('Katsayıyı hesapla','C(6, 4) = 15, 3² = 9 ve (−2)⁴ = 16 çarpılır.','15 × 9 × 16 = 2160')],
 v,[(e[0],'k = 2 almış (üsleri ters eşlemiş): C(6, 2) × 3⁴ × (−2)² hesaplamış.','dikkat'),(e[3],'C(6, 4) = 15 çarpanını unutmuş: 9 × 16.','bilgi'),(e[1],'3² = 9 çarpanını unutup yalnız C(6, 4) × (−2)⁴ yazmış.','bilgi'),(e[2],'3’ün kuvvetini 2 yerine 1 almış: 15 × 3 × 16.','dikkat')],
 tipId='bn-katsayi2',tip='Terim, ortalama ve eşit katsayılar',z='orta',alt='Katsayı Ortalaması',kaz='Katsayıların aritmetik ortalamasından n yi bulup sabit terimi hesaplar.',kalip='düz',
 kart='K-ABO2-01 (katsayı ortalaması, sabit terim) · katsayılar toplamı 1; ortalama = 1/(n + 1)',
 metin='n bir pozitif tam sayı olmak üzere,\n(3x² − 2/x)ⁿ\nifadesinin açılımındaki tüm katsayıların aritmetik ortalaması 1/7 olduğuna göre, bu açılımdaki sabit terim kaçtır?',
 istenen='Açılımdaki sabit terim.',ip=['Ortalamanın hangi iki niceliğin oranı olduğunu yaz; her ikisi de n ye bağlıdır.'],bilgi=[GT,ORT],
 puf='Önce toplam ve terim sayısından n yi bul; sabit terimi ondan sonra ara.')

# ================= 05 orta · eşit katsayılar =================
sol=[n for n in range(5,40) if comb(n,2)==comb(n,5)]; assert sol==[7]
for n in (7,):
    Zp=sp.expand((x**3+x)**n); assert Zp.coeff(x,n+4)==Zp.coeff(x,n+10)==21
v=21; e=[comb(7,4),comb(8,2),comb(10,2),7]; assert e==[35,28,45,7] and len({v,*e})==5
q('0005',[A('İfadeyi sadeleştir','x ortak çarpana alınır.','(x³ + x)ⁿ = xⁿ · (x² + 1)ⁿ'),
          A('Terimlerin sırasını bul','(x² + 1)ⁿ açılımında (k + 1). terim C(n, k) · x²ᵏ olduğundan xⁿ⁺⁴ için k = 2, xⁿ⁺¹⁰ için k = 5 tir.','C(n, 2) = C(n, 5)'),
          A('n yi bul','Eşit binom katsayılarında alt sayıların toplamı n e eşittir.','n = 2 + 5 = 7'),
          A('k yı hesapla','Ortak katsayı hesaplanır.','k = C(7, 2) = 21')],
 v,[(e[0],'xⁿ⁺⁴ için k yerine 4 alıp katsayıyı C(7, 4) hesaplamış.','dikkat'),(e[1],'n yi 2 + 5 + 1 = 8 bulup C(8, 2) yazmış.','dikkat'),(e[2],'n yi 2 · 5 = 10 bulup C(10, 2) yazmış.','bilgi'),(e[3],'Sorulan katsayı yerine n yi vermiş.','dikkat')],
 tipId='bn-katsayi2',tip='Terim, ortalama ve eşit katsayılar',z='orta',alt='Eşit Katsayılar',kaz='Ortak çarpana alınan bir ifadenin açılımında iki terimin eşit katsayısından n ve katsayıyı bulur.',kalip='düz',
 kart='K-ABO2-01 (eşit katsayılar) · (x³ + x)ⁿ, ortak çarpanla sade biçim; üssün iki ile artışı',
 metin='n bir pozitif tam sayı olmak üzere,\n(x³ + x)ⁿ\nifadesinin açılımında hem xⁿ⁺⁴ lü terimin hem de xⁿ⁺¹⁰ lu terimin katsayısı k ya eşittir.\nBuna göre k kaçtır?',
 istenen='Eşit olan katsayının değeri.',ip=['x’i ortak çarpana alarak içte yalnız x’in kuvveti kalan bir binom elde etmeyi dene.'],bilgi=[GT,KATB],
 puf='Terimlerin kuvvetleri arasındaki farkı, genel terimdeki k nın değişimiyle karşılaştır.')

# ================= 06 orta · Pascal satırlarında karelerin toplamı (şekil) =================
BY={(0,0),(2,1),(4,2),(6,3)}
for r in range(4): assert sum(comb(r,k)**2 for k in range(r+1))==comb(2*r,r)
v=sum(comb(9,k)**2 for k in range(10)); assert v==comb(18,9)==48620
e=[2**18,comb(18,8),comb(17,8),comb(19,9)]; assert e==[262144,43758,24310,92378] and len({v,*e})==5
q('0006',[A('Örüntüyü bul','Boyalı sayılar ilk dört satırın kareler toplamıdır: 1, 2, 6, 20. Bunların üçgendeki konumu satır numarasıyla ilişkilidir.','0. satır → C(0, 0) · 1. satır → C(2, 1) · 2. satır → C(4, 2) · 3. satır → C(6, 3)'),
          A('Bağıntıyı yaz','r. satırın kareler toplamı, 2r. satırın ortadaki sayısına eşittir.','Toplam = C(2r, r)'),
          A('9. satırı hesapla','r = 9 için bağıntı uygulanır.','C(18, 9) = 48620')],
 v,[(e[0],'Satır toplamının (2⁹ = 512) karesini almış.','dikkat'),(e[1],'Ortadaki sayı yerine yanındaki sayıyı almış: C(18, 8).','dikkat'),(e[2],'Satır numarasını 2r − 1 almış: C(17, 8).','dikkat'),(e[3],'Satır numarasını 2r + 1 almış: C(19, 9).','dikkat')],
 tipId='bn-satir2',tip='Pascal satırları ve özdeşlikler',z='orta',alt='Karelerin Toplamı',kaz='Pascal üçgeninde satırlardaki sayıların kareleri toplamının üçgendeki konumunu örüntüden bulur.',kalip='şekilli',
 kart='K-ABO2-02 (satır karelerinin toplamı) · boyalı sayılar çift satırların ortadaki sayıları',
 metin='Şekilde, satırları 0’dan başlayarak numaralandırılmış Pascal üçgeninin ilk sekiz satırı verilmiştir. Üçgenin her satırındaki sayıların kareleri toplanıyor; ilk dört satır için bu toplamlar şekilde turuncu renkle boyalı sayılara eşittir.\nBuna göre aynı biçimde 9. satırdaki sayıların kareleri toplamı kaçtır?',
 istenen='9. satırdaki sayıların kareleri toplamı.',ip=['Boyalı sayıların satır numaralarını, üçgendeki satırlarıyla karşılaştır.'],bilgi=[OZD],sekil=pas_fig(8,BY),
 puf='Örüntü sorularında küçük durumlardan konum bağıntısını kurup büyük duruma uygula.')

# ================= 07 orta · ağda yürüyüş (şekil) =================
GG={'A':'BCD','B':'AC','C':'ABD','D':'AC'}
def wk(adj,s,n,e_):
    d={s:Fr(1)}
    for _ in range(n):
        nd={}
        for a,p in d.items():
            for b in adj[a]: nd[b]=nd.get(b,0)+p/len(adj[a])
        d=nd
    return d.get(e_,Fr(0))
v=wk(GG,'A',3,'A'); assert v==Fr(2,9)
e=[wk(GG,'A',2,'A'),wk(GG,'A',3,'C'),Fr(1,3)**3*2,Fr(1,3)*Fr(1,2)*Fr(1,3)*2]
assert e==[Fr(4,9),Fr(7,27),Fr(2,27),Fr(1,9)] and len({v,*e})==5
q('0007',[A('Yürüyüşleri listele','3 adımda A dan başlayıp A ya dönen bütün yürüyüşler yazılır.','A→B→C→A, A→C→B→A, A→C→D→A, A→D→C→A'),
          A('Her yürüyüşün olasılığını yaz','A ve C den 3, B ve D den 2 çizgi çıkar; her adımın olasılığı 1 / (çizgi sayısı) dır.','1/3 · 1/2 · 1/3 = 1/18 (dört yürüyüşte de 1/18)'),
          A('Olasılıkları topla','Dört yürüyüşün olasılıkları toplanır.','4 × 1/18 = 2/9')],
 v,[(e[0],'2 atlayıştan sonra A düğümünde bulunma olasılığını (4/9) hesaplamış.','dikkat'),(e[1],'3 atlayıştan sonra C düğümünde bulunma olasılığını (7/27) bulmuş.','dikkat'),(e[2],'Bütün düğümlerden 3 çizgi çıkıyormuş gibi her yürüyüşe 1/27 verip yalnız 2 yürüyüş saymış.','bilgi'),(e[3],'Her yürüyüşün olasılığını doğru (1/18) bulmuş ama yalnız 2 yürüyüş saymış.','dikkat')],
 tipId='ol-graf',tip='Ağ şemasında rastgele yürüyüş',z='orta',alt='Rastgele Yürüyüş',kaz='Ağ şemasında rastgele yürüyen bir cismin belirli düğümde bulunma olasılığını yolları sayarak bulur.',kalip='şekilli',
 kart='K-ABO2-04 (ağda rastgele yürüyüş) · dört düğümlü ağ, üç adımda başlangıca dönüş',
 metin='Şekilde dört düğümlü bir ağ gösterilmiştir. A düğümünde bulunan bir kurbağa her seferinde bulunduğu düğümden çıkan çizgilerden birini eşit olasılıkla seçip o çizginin diğer ucundaki düğüme atlıyor.\nKurbağa 3 kez atladıktan sonra tekrar A düğümünde bulunma olasılığı kaçtır?',
 istenen='3 atlayıştan sonra A düğümünde bulunma olasılığı.',ip=['Her düğümden çıkan çizgi sayısına göre bir atlayışın olasılığını bul; sonra A ya dönen yolları ara.'],bilgi=[GRF],sekil=graf_fig(),
 puf='Dal olasılığı bulunulan düğümün çizgi sayısına bağlıdır; her adımda payda değişebilir.')

# ================= 08 orta · koltuk yerleşimi (şekil) =================
DOLU={(0,1):'K',(1,1):'E'}
cnt=0
for p in permutations('KKEE'):
    on3,ar1,ar2,ar3=p; col=[('K',ar1),('E',ar2),(on3,ar3)]
    cnt+=all(a!=b for a,b in col)
assert cnt==8
v=Fr(8,24); assert v==Fr(1,3)
e=[Fr(4,24),Fr(6,24),Fr(8,16),1-v]; assert e==[Fr(1,6),Fr(1,4),Fr(1,2),Fr(2,3)] and len({v,*e})==5
q('0008',[A('Bütün yerleşimleri say','Kalan 4 çocuk (2 kız, 2 erkek) boş 4 koltuğa 4! farklı biçimde oturabilir.','4! = 24'),
          A('Uygun yerleşimleri say','1. sütunda ön koltuk kız olduğundan arka koltuğa erkek; 2. sütunda arka koltuğa kız oturmalıdır. 3. sütunda kalan kız ve erkek iki farklı biçimde oturur.','2 × 2 × 2 = 8'),
          A('Olasılığı bul','Uygun yerleşim sayısı bütün yerleşim sayısına bölünür.','8 / 24 = 1/3')],
 v,[(e[0],'3. sütundaki kız ve erkeğin iki farklı oturuş biçimini saymamış: 2 × 2 × 1 = 4 uygun.','dikkat'),(e[1],'1. sütun arka koltuk için 3 erkeği (oturmuş olanı da sayarak), 2. sütun için 2 kızı seçip son sütunu 1 biçimde saymış: 3 × 2 × 1 = 6 uygun.','bilgi'),(e[2],'Bütün yerleşimleri 2⁴ = 16 saymış (her koltuk iki durumlu); uygun yerleşimleri 8 almış.','bilgi'),(e[3],'Uygun yerleşimlerin olasılığı yerine tümleyeninin (2/3) olasılığını yazmış.','dikkat')],
 tipId='ol-sayma2',tip='Kısıtlı sayma ile olasılık',z='orta',alt='Koltuk Yerleşimi',kaz='Kısmen dolu bir koltuk düzeninde sütun kısıtını çarpma kuralıyla sayıp olasılığı hesaplar.',kalip='şekilli',
 kart='K-ABO2-05 (kısıtlı yerleştirme) · 2 × 3 koltuk, iki koltuk dolu, her sütunda farklı cinsiyet',
 metin='Şekilde, iki sıra ve üç sütundan oluşan 6 koltuk görülmektedir; iki koltuğa bir kız (K) ve bir erkek (E) çocuk oturmuştur. Kalan 2 kız ve 2 erkek çocuk boş koltuklara rastgele oturacaktır.\nBuna göre her sütunda bir kız ve bir erkek çocuğun bulunma olasılığı kaçtır?',
 istenen='Her sütunda bir kız ve bir erkek çocuğun oturma olasılığı.',ip=['Boş koltuğu bulunan her sütunda, oturmuş çocuğun cinsiyetine göre o sütunun kısıtını yaz.'],bilgi=[SYM],sekil=koltuk_fig(DOLU),
 puf='Çocukları farklı kişiler olarak say; hem pay hem payda aynı evrende sayılmalı.')

# ================= 09 orta · grup seçimi, koşullu (tablo) =================
TAB_={'Robotik':(2,3),'Satranç':(1,2),'Tiyatro':(3,1)}
kz=sum(a for a,b in TAB_.values()); er=sum(b for a,b in TAB_.values()); assert (kz,er)==(6,6)
tum=comb(12,3); ge1=tum-comb(6,3); v=Fr(comb(6,3),ge1); assert (tum,ge1,v)==(220,200,Fr(1,10))
nm=[tuple(g) for g in combinations(range(12),3)]; assert sum(1 for g in nm if any(i<6 for i in g))==200 and sum(1 for g in nm if all(i<6 for i in g))==20
e=[Fr(20,220),Fr(20,110),Fr(20,90),Fr(20,66)]; assert comb(6,1)*comb(6,2)==90 and e[0]==Fr(1,11) and e[1]==Fr(2,11) and e[2]==Fr(2,9) and len({v,*e})==5
q('0009',[A('Kız ve erkek sayılarını bul','Tablodaki sütunlar toplanır.','Kız: 2 + 1 + 3 = 6 · Erkek: 3 + 2 + 1 = 6'),
          A('Koşula uygun seçimleri say','“En az bir kız” olayının tümleyeni “üçü de erkek” olduğundan bu koşulu sağlayan seçimler bütün seçimlerden çıkarılarak bulunur.','C(12, 3) − C(6, 3) = 220 − 20 = 200'),
          A('İstenen olayın seçimlerini say','Koşulu sağlayan seçimlerden üçünün de kız olduğu seçimler sayılır.','C(6, 3) = 20'),
          A('Koşullu olasılığı yaz','İstenen seçimlerin sayısı, koşulu sağlayan seçimlerin sayısına bölünür.','20 / 200 = 1/10')],
 v,[(e[0],'Koşulu dikkate almayıp paydayı bütün seçimlerin sayısı 220 almış: 20 / 220.','dikkat'),(e[1],'“En az bir kız” koşulunda yalnız tam 3 kız ve tam 2 kız seçimlerini saymış: 20 / (20 + 90).','dikkat'),(e[2],'“En az bir kız” koşulunu “tam bir kız” okuyup paydaya yalnız C(6, 1) × C(6, 2) = 90 yazmış: 20 / 90.','bilgi'),(e[3],'Paydaya 2 kişilik seçimlerin sayısını yazmış: C(6, 3) / C(12, 2) = 20 / 66.','bilgi')],
 tipId='ol-kosullu2',tip='Koşullu olasılık ve iadesiz çekim',z='orta',alt='Grup Seçimi',kaz='“En az bir” koşulu verilen seçimde koşullu olasılığı sayarak bulur.',kalip='tablo',
 kart='K-ABO2-06 (koşullu olasılık, en az bir koşulu) · tablodan toplam kız-erkek sayıları',
 metin='Bir okulda üç kulüp bulunmaktadır; kulüplere üye olan kız ve erkek öğrenci sayıları aşağıdaki tabloda verilmiştir. Her öğrenci yalnız bir kulübe üyedir. Bu 12 öğrenci arasından rastgele 3 öğrenci seçiliyor.\nSeçilen öğrenciler arasında en az bir kız öğrenci bulunduğu bilindiğine göre, üç öğrencinin de kız olma olasılığı kaçtır?',
 istenen='Koşullu olasılık: üçü de kız | en az bir kız.',ip=['Koşul örnek uzayı daraltır; “en az bir” olayının tümleyenini kullanarak bu uzayın büyüklüğünü bul.'],bilgi=[KS2],
 sekil=tablo_svg(['Kulüp','Kız','Erkek'],[[k,a,b] for k,(a,b) in TAB_.items()]),
 puf='“En az bir” ifadesini görünce tümleyeni, yani “hiç yok” durumunu say.')

# ================= 10 orta · kartlar, koşullu (şekil) =================
KV=list(range(1,10))
pr=list(combinations(KV,2)); B_=[p for p in pr if (p[0]+p[1])%2==1]; AB_=[p for p in B_ if (p[0]*p[1])%3==0]
assert (len(pr),len(B_),len(AB_))==(36,20,11); v=Fr(11,20)
cift=[p for p in pr if (p[0]*p[1])%2==0]; e=[Fr(len(AB_),36),Fr(len(AB_),len([p for p in pr if (p[0]*p[1])%3==0])),Fr(9,20),Fr(len([p for p in pr if (p[0]*p[1])%3==0]),36)]
c3=len([p for p in pr if (p[0]*p[1])%3==0]); assert c3==21 and e==[Fr(11,36),Fr(11,21),Fr(9,20),Fr(7,12)] and len({v,*e})==5
q('0010',[A('Koşulu sağlayan çiftleri say','Toplamın tek olması için bir kart tek, diğeri çift olmalıdır: 5 tek ve 4 çift kart vardır.','5 × 4 = 20 çift'),
          A('İstenen çiftleri say','Bu 20 çiftten çarpımı 3’ün katı olanlar, 3, 6 ya da 9 kartı içerenlerdir; hiçbirini içermeyenler 1, 5, 7 ile 2, 4, 8 kartlarından oluşur.','20 − 3 × 3 = 11 çift'),
          A('Koşullu olasılığı yaz','Örnek uzay, toplamı tek olan 20 çifte daralır.','11 / 20')],
 v,[(e[0],'Koşulu dikkate almayıp paydaya bütün çiftlerin sayısını (36) yazmış: 11 / 36.','dikkat'),(e[1],'Koşulu ters yorumlamış: çarpımı 3’ün katı olan 21 çift arasında toplamı tek olanların oranını (11/21) bulmuş.','bilgi'),(e[2],'İstenen çiftleri 20 − 11 = 9 bulmuş (3’ün katı olmayanları saymış): 9/20.','dikkat'),(e[3],'Yalnız çarpımı 3’ün katı olan çiftlerin olasılığını (21/36 = 7/12) yazmış.','dikkat')],
 tipId='ol-kosullu2',tip='Koşullu olasılık ve iadesiz çekim',z='orta',alt='Kartlarla Koşullu',kaz='Numaralı kartlardan seçilen çiftlerde koşullu olasılığı sayarak hesaplar.',kalip='şekilli',
 kart='K-ABO2-06 (kartlarla koşullu olasılık) · toplam tek, çarpım 3’ün katı',
 metin='Şekilde 1’den 9’a kadar numaralanmış 9 kart görülmektedir. Bu kartlar arasından rastgele iki kart aynı anda seçiliyor.\nSeçilen kartlardaki sayıların toplamı tek olduğuna göre, bu sayıların çarpımının 3’ün katı olma olasılığı kaçtır?',
 istenen='P(çarpım 3’ün katı | toplam tek).',ip=['Toplamın tek olması için kartlardaki sayıların nasıl olması gerektiğini bul; örnek uzay bu çiftlerdir.'],bilgi=[KS2],sekil=kart_fig(KV),
 puf='Koşulu önce çiftlerin türüyle (tek–çift) ifade edip örnek uzayı onunla sınırla.')

# ================= 11 orta · öncüllü, iadesiz çekim (şekil) =================
def p2(f):
    d=[(a,b) for a in range(5) for b in range(5) if a!=b]; return Fr(sum(1 for a,b in d if f(a,b)),len(d))
rk=lambda i:i<3   # 0,1,2 kırmızı; 3,4 mavi
I_=p2(lambda a,b:rk(b)); II_=p2(lambda a,b:rk(a)!=rk(b)); III_=Fr(sum(1 for a in range(5) for b in range(5) if a!=b and (not rk(a)) and (not rk(b))),sum(1 for a in range(5) for b in range(5) if a!=b and not rk(a)))
assert (I_,II_,III_)==(Fr(3,5),Fr(3,5),Fr(1,4)) and Fr(2,5)!=III_
t=(I_==Fr(3,5),II_==Fr(3,5),III_==Fr(2,5)); assert t==(True,True,False) and kume(t)=='I ve II'
qo('0011',[A('I. önermeyi sına','İlk topun rengine göre ikinci topun kırmızı olma olasılığı hesaplanıp toplanır.','3/5 · 2/4 + 2/5 · 3/4 = 3/10 + 3/10 = 3/5 ⇒ I doğru'),
           A('II. önermeyi sına','Farklı renkli çiftler KM ya da MK biçimindedir.','3/5 · 2/4 + 2/5 · 3/4 = 3/10 + 3/10 = 3/5 ⇒ II doğru'),
           A('III. önermeyi sına','İlk top mavi ise torbada 3 kırmızı, 1 mavi top kalır; ikinci topun mavi olma olasılığı 1/4 tür.','P = 1/4 ≠ 2/5 ⇒ III yanlış'),
           A('Sonucu yaz','Doğru olanlar I ve II dir.','I ve II')],
 'I ve II',[('Yalnız I','I’i doğru bulmuş; II’de yalnız KM durumunu (3/10) hesaplayıp II’yi yanlış saymış; III’ü de yanlış kabul etmiş.','bilgi'),('Yalnız II','I’de ilk topun kırmızı çıktığını varsayıp 2/4 = 1/2 bulduğu için I’i yanlış saymış; II’yi doğru bulmuş, III’ü yanlış saymış.','dikkat'),('I ve III','II’de yalnız KM durumunu (3/10) hesaplayıp yanlış saymış; III’te top geri konmuş gibi 2/5 bulup III’ü doğru saymış.','bilgi'),('II ve III','I’de ilk topu kırmızı varsayıp 1/2 bulduğu için I’i yanlış saymış; III’te iadeli çekimdeki 2/5’i doğru kabul etmiş.','bilgi')],
 sira=OS3,
 tipId='ol-kosullu2',tip='Koşullu olasılık ve iadesiz çekim',z='orta',alt='İadesiz Çekim',kaz='İadesiz iki çekimde toplam ve koşullu olasılık önermelerini değerlendirir.',kalip='öncüllü',
 kart='K-ABO2-06 (iadesiz çekim, öncüllü) · 3 kırmızı 2 mavi, ikinci çekim ve koşullu önerme',
 metin='Şekildeki torbada 3 kırmızı ve 2 mavi top vardır. Bu torbadan rastgele bir top çekilip geri konmadan ikinci bir top çekiliyor.\nI. İkinci topun kırmızı olma olasılığı 3/5’tir.\nII. İki topun farklı renkte olma olasılığı 3/5’tir.\nIII. İlk top mavi olduğu bilindiğine göre ikinci topun mavi olma olasılığı 2/5’tir.\nBuna göre bu önermelerden hangileri doğrudur?',
 istenen='Doğru olan önermeler.',ip=['Her önermede ilk çekimin sonucuna göre torbanın içeriğinin nasıl değiştiğini ayrı ayrı yaz.'],bilgi=[IAD],sekil=torba_fig([('Torba',3,2)]),
 puf='İadesiz çekimde ikinci olasılığı hesaplarken torbadaki güncel sayıları kullan.')

# ================= 12 orta · kapı ve otopark (şekil) =================
NK=[2,3,6]
def eslesme(NK):
    pay=Fr(0)
    for g in range(len(NK)):
        pay+=Fr(1,len(NK))*Fr(1,len(NK))*Fr(1,NK[g])
    return pay
v=eslesme(NK); assert v==Fr(1,9)
# kaba kuvvet
tot=Fr(0)
for g1 in range(3):
    for o1 in range(NK[g1]):
        for g2 in range(3):
            for o2 in range(NK[g2]):
                if (g1,o1)==(g2,o2): tot+=Fr(1,3)*Fr(1,NK[g1])*Fr(1,3)*Fr(1,NK[g2])
assert tot==v
e=[Fr(1,sum(NK)),sum(Fr(1,3)*Fr(1,3)*Fr(1,n)**2 for n in NK),Fr(1,3),Fr(2,9)]
assert e==[Fr(1,11),Fr(7,162),Fr(1,3),Fr(2,9)] and e[1]==Fr(7,162) and len({v,*e})==5
q('0012',[A('Yöntemi kur','Selin’in aradığı otopark, park ettiği otoparkla ancak aynı kapıdan çıkıp o kapının önündeki aynı otoparkı seçerse aynı olur; park edilen otopark girişte belirlenir ve olasılığı toplamda 1 dir.','Aynı kapı ve aynı otopark'),
          A('Her kapı için olasılığı yaz','Girişte g. kapıyı seçme olasılığı 1/3, çıkışta aynı kapıyı seçme olasılığı 1/3, o kapının n otoparkı arasından park edilen otoparkı seçme olasılığı 1/n dir (park edilen otopark, girişte 1 olasılıkla belli olur).','Kapı 1: 1/3 · 1/3 · 1/2 · Kapı 2: 1/3 · 1/3 · 1/3 · Kapı 3: 1/3 · 1/3 · 1/6'),
          A('Olasılıkları topla','Üç ayrı durumun olasılıkları toplanır.','1/9 · (1/2 + 1/3 + 1/6) = 1/9')],
 v,[(e[0],'Kapıları hiç hesaba katmayıp 11 otoparktan birini seçmiş gibi 1/11 yazmış.','bilgi'),(e[1],'Park edilen otoparkı belirli bir otopark kabul edip hem park hem arama seçimini 1/n sayarak her kapı için (1/n)² almış: 1/9 · (1/4 + 1/9 + 1/36).','dikkat'),(e[3],'Üç kapı için bulduğu olasılığı iki kez toplamış: 2 × 1/9.','dikkat'),(e[2],'Çıkışta kapıyı seçme olasılığını (1/3) katmamış: yalnızca 1/3 · (1/2 + 1/3 + 1/6).','dikkat')],
 tipId='ol-agac2',tip='Çok aşamalı seçim ve ağaç',z='orta',alt='Kapı ve Otopark',kaz='İki aşamalı rastgele seçimde (kapı, otopark) aynı sonucun gelme olasılığını hesaplar.',kalip='hikâyeli',
 kart='K-ABO2-07 (iki aşamalı seçim, kapı ve otopark) · üç kapı, farklı otopark sayıları',
 metin='Üç kapısı bulunan bir alışveriş merkezinin kapılarının önündeki otopark sayıları şekilde gösterilmiştir. Merkeze gelen Selin, kapılardan rastgele birinin önüne gelip o kapının önündeki otoparklardan rastgele birine arabasını park ediyor. Park için seçilebilecek her otopark eşit olasılıklıdır. Alışveriş merkezinden çıkarken arabasını nereye park ettiğini ve hangi kapıdan girdiğini unuttuğu için kapıların rastgele birinden çıkıp o kapının önündeki otoparklardan rastgele birinde arabasını arıyor.\nBuna göre Selin’in aradığı otoparkın arabasını park ettiği otopark olma olasılığı kaçtır?',
 istenen='Aranan otoparkın park edilen otopark olma olasılığı.',ip=['Aynı otoparka ulaşmak için kapı ve otopark seçimlerinin ikisinin de aynı olması gerektiğini her kapı için ayrı ayrı yaz.'],bilgi=[AGB],sekil=kapi_fig(NK),
 puf='Çok aşamalı seçimlerde her aşamayı ayrı olasılık olarak yaz; kapı sayısı değişince payda da değişir.')

# ================= 13 orta · rakamlarla sayı, koşullu (düz) =================
dig=[0,1,2,3,4,5]; nums=[a*100+b*10+c for a,b,c in permutations(dig,3) if a!=0]
b5=[n for n in nums if n%5==0]; a_=[n for n in b5 if n%2==0]; assert (len(nums),len(b5),len(a_))==(100,36,20)
v=Fr(20,36); assert v==Fr(5,9)
e=[Fr(20,100),Fr(16,36),Fr(len([n for n in nums if n%2==0 and n%5==0]),len([n for n in nums if n%2==0])),Fr(20,40)]
ce=[n for n in nums if n%2==0]; assert len(ce)==52 and e==[Fr(1,5),Fr(4,9),Fr(5,13),Fr(1,2)] and len({v,*e})==5
q('0013',[A('Koşulu sağlayan sayıları say','5’e bölünen sayıların birler basamağı 0 ya da 5 tir; 0 ise 5 × 4 = 20, 5 ise başa 0 gelemeyeceğinden 4 × 4 = 16 sayı vardır.','20 + 16 = 36'),
          A('İstenen sayıları say','Bu sayılardan çift olanlar birler basamağı 0 olanlardır.','20'),
          A('Koşullu olasılığı yaz','Örnek uzay 36 sayıdır.','20 / 36 = 5/9')],
 v,[(e[0],'Koşulu dikkate almayıp paydaya bütün sayıların sayısını (100) yazmış: 20 / 100.','dikkat'),(e[2],'Koşulu ters yorumlamış: çift sayılar (52) arasında 5’e bölünenlerin oranını (20/52) bulmuş.','bilgi'),(e[1],'Çift olma durumu yerine tek olanları (birler basamağı 5: 16 sayı) saymış: 16/36.','dikkat'),(e[3],'Başa 0 gelemeyeceğini unutup birler basamağı 5 için de 5 × 4 = 20 sayı bulmuş: 20/40.','dikkat')],
 tipId='ol-sayma2',tip='Kısıtlı sayma ile olasılık',z='orta',alt='Rakamlarla Koşullu',kaz='Rakamları farklı üç basamaklı sayılarda koşullu olasılığı sayarak bulur.',kalip='düz',
 kart='K-ABO2-05 (rakamlarla sayma, koşullu) · 0 dahil altı rakam, 5’e bölünme ve çift sayı',
 metin='0, 1, 2, 3, 4 ve 5 rakamları kullanılarak rakamları birbirinden farklı üç basamaklı bütün doğal sayılar yazılıyor ve bu sayılardan biri rastgele seçiliyor.\nSeçilen sayının 5 ile tam bölündüğü bilindiğine göre, bu sayının çift olma olasılığı kaçtır?',
 istenen='P(çift | 5 ile bölünür).',ip=['Önce koşulu sağlayan sayıların birler basamağını belirle; başa gelemeyecek rakamı unutma.'],bilgi=[RAK,KS2],
 puf='Sıfır içeren rakam kümelerinde yüzler basamağını ayrıca incele.')

# ================= 14 zor · en büyük katsayılı terim (düz) =================
kf=[comb(9,k)*2**k for k in range(10)]; kmax=kf.index(max(kf)); assert kmax==6 and kf[6]==5376 and kf.count(max(kf))==1
v=kmax+1; assert v==7
e=[5,10,8,9]; assert comb(9,4)==comb(9,5) and len({v,*e})==5
q('0014',[A('Ardışık katsayıların oranını yaz','(1 + 2x)⁹ da (k + 1). terimin katsayısı C(9, k) · 2ᵏ dır; ardışık iki katsayının oranı (9 − k) / (k + 1) · 2 olur.','a(k + 1) / a(k) = 2(9 − k) / (k + 1)'),
          A('Artış koşulunu çöz','Katsayılar, oran 1 den büyük olduğu sürece artar.','2(9 − k) > k + 1 ⇒ 17 > 3k ⇒ k ≤ 5'),
          A('En büyük terimi belirle','k = 5 ten k = 6 ya geçişte katsayı hâlâ artar; k = 6 dan k = 7 ye geçişte (oran 6/7) azalır. En büyük katsayı k = 6 dadır.','k = 6 ⇒ terim sırası 6 + 1 = 7')],
 v,[(5,'Çarpan 2’yi hesaba katmayıp yalnız C(9, k) katsayılarına bakmış (ortadaki terim).','bilgi'),(10,'Açılımdaki terim sayısını (n + 1 = 10) en büyük katsayılı terimin sırası sanmış.','dikkat'),(8,'Artış koşulunu 2(9 − k) ≥ k yazıp k ≤ 6 bulmuş; en büyük terimi k = 7 sanıp 8. terim demiş.','islem'),(9,'Üssü (n = 9) en büyük katsayılı terimin sırası sanmış.','bilgi')],
 tipId='bn-katsayi2',tip='Terim, ortalama ve eşit katsayılar',z='zor',alt='En Büyük Katsayı',kaz='Binom açılımında ardışık katsayı oranından en büyük katsayılı terimi bulur.',kalip='düz',
 kart='K-ABO2-01 (en büyük katsayılı terim) · (1 + 2x)⁹, oran eşitsizliği',
 metin='(1 + 2x)⁹\nifadesinin açılımında katsayısı en büyük olan terim kaçıncı terimdir?',
 istenen='Katsayısı en büyük terimin sırası.',ip=['Ardışık terimlerin katsayılarını birbiriyle karşılaştırmanın bir yolunu bul.'],bilgi=[GT],
 puf='Büyüklük karşılaştırmalarında ardışık terimleri birbirine göre değerlendir.')

# ================= 15 zor · yeni kurallı üçgen (şekil) =================
def yeni(n):
    T={(0,0):1}
    for r in range(1,n+1):
        for k in range(r+1):
            T[(r,k)]=1 if k in (0,r) else T[(r-1,k-1)]+T[(r-1,k)]+1
    return T
T=yeni(8); assert all(T[(r,k)]==2*comb(r,k)-1 for r in range(9) for k in range(r+1))
v=sum(T[(8,k)] for k in range(9)); assert v==503==2**9-9
e=[sum(comb(8,k) for k in range(9)),sum(T[(8,k)] for k in range(9))+1,2**9-8,2**9]
e=[256,2**9-1,2**9-8,2**9]; assert e==[256,511,504,512] and len({v,*e})==5
q('0015',[A('İlk satırları hesapla','Kurala göre ilk satırlar kurulur: 2. satır 1, 3, 1; 3. satır 1, 5, 5, 1; 4. satır 1, 7, 11, 7, 1.','Satır toplamları: 1, 2, 5, 12, 27'),
          A('Pascal üçgeniyle ilişkiyi bul','Her sayının, aynı konumdaki Pascal sayısının iki katından 1 eksik olduğu görülür.','Sayı = 2 · C(n, k) − 1'),
          A('8. satırın toplamını yaz','9 sayının toplamında her sayı için 1 eksik alınır.','2 · 2⁸ − 9 = 512 − 9 = 503')],
 v,[(e[3],'Her sayının 2 · C(n, k) olduğunu görüp “−1” kısmını toplamda unutmuş: 2⁹ = 512.','dikkat'),(e[1],'Her sayıdaki “−1” için toplamda yalnız bir kez 1 çıkarmış: 512 − 1.','dikkat'),(e[2],'Eksilen 1’lerin sayısını satır numarası (8) almış: 512 − 8.','dikkat'),(e[0],'Kuralı uygulamadan 8. satırı olağan Pascal satırı gibi toplamış: 2⁸.','bilgi')],
 tipId='bn-satir2',tip='Pascal satırları ve özdeşlikler',z='zor',alt='Yeni Kurallı Üçgen',kaz='Tanımlı kurala göre kurulan sayı üçgeninde satır toplamını Pascal üçgeniyle ilişkilendirerek bulur.',kalip='yeni nesil',
 kart='K-ABO2-02 (tanımlı kurallı üçgen) · her sayı iki komşunun toplamının 1 fazlası, kenarlar 1',
 metin='Aşağıdaki sayı üçgeninde her satırın ilk ve son sayısı 1’dir; diğer sayılar, bir üst satırdaki iki komşusunun toplamından 1 fazladır. Şekilde bu üçgenin ilk beş satırı gösterilmiştir (satırlar 0’dan başlar).\nBuna göre üçgenin 8. satırındaki sayıların toplamı kaçtır?',
 istenen='8. satırdaki sayıların toplamı.',ip=['İlk satırları kurala göre yazıp bir örüntü ara.'],bilgi=[YEN,PSA],sekil=tri_fig({k:v_ for k,v_ in T.items() if k[0]<5},5),
 puf='Tanımlı kurallı üçgenlerde önce ilk satırları hesaplayıp örüntüyü gözle.')

# ================= 16 zor · öncüllü, binom özdeşlikleri (düz) =================
I1=comb(9,2)+comb(9,3)+comb(10,4)==comb(11,5)
II1=sum(comb(8,k) for k in range(0,9,2))==2**7
n3=[n for n in range(5,30) if comb(n,3)==comb(n,5)]; III1=(n3==[8])
assert (I1,II1,III1)==(False,True,True) and comb(9,2)+comb(9,3)+comb(10,4)==330==comb(11,4)!=comb(11,5)==462
qo('0016',[A('I. önermeyi sına','C(9, 2) + C(9, 3) = C(10, 3) olduğundan toplam C(10, 3) + C(10, 4) = C(11, 4) tür; bu da C(11, 5) e eşit değildir.','36 + 84 + 210 = 330 = C(11, 4) ≠ C(11, 5) = 462 ⇒ I yanlış'),
           A('II. önermeyi sına','Çift sıradaki katsayıların toplamı 2ⁿ⁻¹ dir.','2⁸⁻¹ = 128 = 2⁷ ⇒ II doğru'),
           A('III. önermeyi sına','Eşit binom katsayılarında alt sayıların toplamı n dir.','3 + 5 = 8 ⇒ III doğru'),
           A('Sonucu yaz','Doğru olan önermeler II ve III tür.','II ve III')],
 'II ve III',[('Yalnız I','Hokey sopası kuralından C(11, 5) bulup I’i doğru saymış; II’de toplamı 2⁸ sanmış; III’te n = 3 + 5 − 1 = 7 bulmuş.','bilgi'),('Yalnız II','I’in yanlış olduğunu görmüş, II’yi doğru bulmuş; III’te n = 3 + 5 + 1 = 9 bulup III’ü yanlış saymış.','dikkat'),('I ve II','I’de C(11, 5) yazılmasını doğru kabul etmiş; II’yi doğru bulmuş; III’te n = 9 bulmuş.','bilgi'),('I ve III','I’i doğru kabul etmiş; II’de çift sıralı toplamı 2⁸ sanıp yanlış bulmuş; III’ü doğru bulmuş.','bilgi')],
 sira=OS3,
 tipId='bn-satir2',tip='Pascal satırları ve özdeşlikler',z='orta',alt='Binom Özdeşlikleri',kaz='Binom katsayılarının toplam ve eşitlik özelliklerini içeren önermeleri değerlendirir.',kalip='öncüllü',
 kart='K-ABO2-02 (binom özdeşlikleri, öncüllü) · hokey sopası, çift sıra toplamı, eşit katsayı',
 metin='I. C(9, 2) + C(9, 3) + C(10, 4) = C(11, 5)\nII. C(8, 0) + C(8, 2) + C(8, 4) + C(8, 6) + C(8, 8) = 2⁷\nIII. n ≥ 5 bir tam sayı olmak üzere, C(n, 3) = C(n, 5) ise n = 8 dir.\nBuna göre yukarıdaki önermelerden hangileri doğrudur?',
 istenen='Doğru olan önermeler.',ip=['Her önermeyi ayrı ayrı sına.'],bilgi=[OZD,PSA],
 puf='Öncüllü sorularda her önermeyi birbirinden bağımsız değerlendir.')

# ================= 17 zor · servis ve yürüyüş süresi (tablo) =================
DEP={5:Fr(1,5),7:Fr(1,2),10:Fr(3,10)}; WLK={4:Fr(1,2),7:Fr(3,10),9:Fr(1,5)}
assert sum(DEP.values())==1==sum(WLK.values())
def yak(ge): return sum(pd*pw for d,pd in DEP.items() for w,pw in WLK.items() if ge(w,d))
v=yak(lambda w,d:w<=d); assert v==Fr(4,5)
e=[1-v,yak(lambda w,d:w<d),sum(pd*pw for d,pd in DEP.items() if d!=5 for w,pw in WLK.items() if w<=d),sum(pd*pw for d,pd in DEP.items() for w,pw in WLK.items() if w<=d or d==5)]
assert e==[Fr(1,5),Fr(13,20),Fr(7,10),Fr(9,10)] and len({v,*e})==5
q('0017',[A('Servis zamanına göre yakalama koşulunu yaz','Zeynep 08.00’de çıkıyor; yürüyüş süresi, servisin kalkış dakikasından büyük olmamalıdır (eşitse yakalar).','Kalkış 5: yürüyüş 4 · Kalkış 7: yürüyüş 4 ya da 7 · Kalkış 10: her süre'),
          A('Her kalkışta yakalama olasılığı','Yürüyüş süresinin dağılımı tablodan okunur.','5: 1/2 · 7: 1/2 + 3/10 = 4/5 · 10: 1'),
          A('Toplam olasılığı hesapla','Her kalkış olasılığı, yakalama olasılığıyla çarpılıp toplanır.','1/5 · 1/2 + 1/2 · 4/5 + 3/10 · 1 = 1/10 + 2/5 + 3/10 = 4/5')],
 v,[(e[0],'Yakalama olasılığı yerine kaçırma olasılığını (1 − 4/5) yazmış.','dikkat'),(e[1],'Eşitliği kaçırma saymış: kalkış 7 için yalnız 4 dakikalık yürüyüşü almış (1/2), 13/20 bulmuş.','dikkat'),(e[2],'İlk servisi (08.05) hiç hesaba katmamış: 1/2 · 4/5 + 3/10.','bilgi'),(e[3],'08.05 servisini her yürüyüş süresinde yakalanır saymış: 1/5 + 2/5 + 3/10.','islem')],
 tipId='ol-sure',tip='Dağılım tablosundan bileşik olay',z='zor',alt='Servis ve Yürüyüş',kaz='İki bağımsız süre dağılımında bir olayın olasılığını tablo okuyarak hesaplar.',kalip='tablo',
 kart='K-ABO2-08 (iki bağımsız dağılım, bileşik olay) · servis kalkış dakikası ve yürüyüş süresi',
 metin='Zeynep’in evinden okul servisinin durağına yürüyüş süresi ile servisin duraktan kalkış zamanı birbirinden bağımsızdır. Zeynep saat tam 08.00’de evden çıkıyor. Aşağıdaki tabloda servisin 08.00’dan kaç dakika sonra kalktığı ile yürüyüş süresinin dakika cinsinden olasılıkları verilmiştir. Zeynep durağa servis kalktığı anda varırsa servise yetişmektedir.\nBuna göre Zeynep’in servise yetişme olasılığı kaçtır?',
 istenen='Zeynep’in servise yetişme olasılığı.',ip=['Servisin her olası kalkış dakikası için, hangi yürüyüş sürelerinde yetişilebildiğini ayrı ayrı belirle.'],bilgi=[TBL],
 sekil=tablo_svg(['Olay','Olasılık'],[['Servis 5 dk sonra kalkar','1/5'],['Servis 7 dk sonra kalkar','1/2'],['Servis 10 dk sonra kalkar','3/10'],['Yürüyüş 4 dk sürer','1/2'],['Yürüyüş 7 dk sürer','3/10'],['Yürüyüş 9 dk sürer','1/5']]),
 puf='Bağımsız iki dağılımda önce koşulu sağlayan çiftleri belirle, sonra çarpıp topla.')

# ================= 18 zor · üç torba, art arda aktarma (şekil) =================
def zincir(I,II,III):
    tot=Fr(0); kz=Fr(0); ky=Fr(0)
    for i in range(len(I)):
        II2=II+[I[i]]
        for j in range(len(II2)):
            III2=III+[II2[j]]
            for k in range(len(III2)):
                p=Fr(1,len(I))*Fr(1,len(II2))*Fr(1,len(III2))
                if III2[k]=='K':
                    tot+=p; kz+=p*(I[i]=='K')
    return tot,kz/tot
tot,v=zincir(['K','K','M'],['K','M'],['M','M']); assert (tot,v)==(Fr(5,27),Fr(4,5))
e=[Fr(1,3),Fr(2,3)*Fr(2,3),Fr(5,9),Fr(2,3)]; assert e==[Fr(1,3),Fr(4,9),Fr(5,9),Fr(2,3)] and len({v,*e})==5
q('0018',[A('Birinci aktarımı dallandır','I. torbadan kırmızı top gelme olasılığı 2/3, mavi gelme olasılığı 1/3 tür; II. torba buna göre 2 kırmızı, 1 mavi ya da 1 kırmızı, 2 mavi top içerir.','K: 2/3 (II: 2 K, 1 M) · M: 1/3 (II: 1 K, 2 M)'),
          A('İkinci aktarımı ekle','II. torbadan III. torbaya kırmızı top gelme olasılığı birinci aktarımın sonucuna bağlıdır; III. torbada kırmızı top ancak bu aktarımla bulunur.','K–K: 2/3 · 2/3 = 4/9 · M–K: 1/3 · 1/3 = 1/9 · III de kırmızı çekme 1/3, toplam (4/9 + 1/9) · 1/3 = 5/27'),
          A('Koşullu olasılığı hesapla','Çekilen top kırmızı olduğundan III. torbaya kırmızı top aktarılmıştır; bu durumda I. torbadan kırmızı gelmiş yolun payı bulunur.','(4/9) / (4/9 + 1/9) = 4/5')],
 v,[(e[0],'Yalnız son aşamayı almış: III. torbadan kırmızı çekme olasılığı 1/3.','dikkat'),(e[1],'İlk iki aşamanın olasılığını (2/3 · 2/3 = 4/9) yazıp koşul olan topluma bölmemiş.','dikkat'),(e[2],'II. torbadan III. torbaya kırmızı top aktarılma olasılığını (5/9) yazmış.','dikkat'),(e[3],'Yalnız ilk aşamayı almış: I. torbadan kırmızı top çekme olasılığı 2/3.','dikkat')],
 tipId='ol-agac2',tip='Çok aşamalı seçim ve ağaç',z='zor',alt='Üç Torba',kaz='Art arda iki aktarımdan sonra çekilen topun rengi bilindiğinde ilk aktarılan topun rengini koşullu olasılıkla bulur.',kalip='hikâyeli',
 kart='K-ABO2-07 (art arda aktarma ve koşullu olasılık) · I → II → III torba',
 metin='Şekildeki I. torbada 2 kırmızı ve 1 mavi, II. torbada 1 kırmızı ve 1 mavi, III. torbada 2 mavi top vardır. Bir öğrenci I. torbadan rastgele bir top çekip bu topu II. torbaya atıyor; sonra II. torbadan rastgele bir top çekip bu topu III. torbaya atıyor. En sonunda III. torbadan rastgele bir top çekiyor ve çektiği topun kırmızı olduğunu görüyor.\nBuna göre I. torbadan II. torbaya atılan topun kırmızı olma olasılığı kaçtır?',
 istenen='Birinci aktarılan topun kırmızı olma olasılığı (son çekilen top kırmızı iken).',ip=['Son çekilen topun kırmızı olabilmesi için aktarımların hangi renklerle sonuçlanması gerektiğini araştır.'],bilgi=[AGB],sekil=torba_fig([('I. torba',2,1),('II. torba',1,1),('III. torba',0,2)],ok=True),
 puf='Çok aşamalı soruların sonunu bilmek, o sonuca götüren yolları sınırlar.')

# ================= 19 zor · öncüllü, hileli dört yüzlü zar (tablo) =================
PZ={1:Fr(1,2),2:Fr(1,4),3:Fr(1,8),4:Fr(1,8)}; assert sum(PZ.values())==1
def pz(f): return sum(PZ[a]*PZ[b] for a in PZ for b in PZ if f(a,b))
I_=pz(lambda a,b:a+b==5)==Fr(3,16)
II_=pz(lambda a,b:a==b)==Fr(1,4)
III_=(pz(lambda a,b:a+b==5 and b==4)/pz(lambda a,b:b==4))==Fr(1,4)
assert pz(lambda a,b:a+b==5)==Fr(3,16) and pz(lambda a,b:a==b)==Fr(11,32) and pz(lambda a,b:a+b==5 and b==4)/pz(lambda a,b:b==4)==Fr(1,2)
t=(I_,II_,III_); assert t==(True,False,False) and kume(t)=='Yalnız I'
qo('0019',[A('I. önermeyi sına','Toplamı 5 yapan sonuçlar (1, 4), (4, 1), (2, 3), (3, 2) dir.','2 · 1/2 · 1/8 + 2 · 1/4 · 1/8 = 1/8 + 1/16 = 3/16 ⇒ I doğru'),
           A('II. önermeyi sına','İki atışta aynı yüzün gelmesi 1-1, 2-2, 3-3 ve 4-4 sonuçlarıdır.','1/4 + 1/16 + 1/64 + 1/64 = 11/32 ≠ 1/4 ⇒ II yanlış'),
           A('III. önermeyi sına','İkinci atışta 4 geldiği bilindiğinde toplamın 5 olması için ilk atışın 1 gelmesi gerekir; atışlar bağımsızdır.','P = P(ilk atış 1) = 1/2 ≠ 1/4 ⇒ III yanlış'),
           A('Sonucu yaz','Yalnız I doğrudur.','Yalnız I')],
 'Yalnız I',[('Yalnız II','I’de yalnız (1, 4) ve (4, 1) sonuçlarını sayıp 1/8 bulduğu için I’i yanlış saymış; II’de yalnız 1-1 sonucunu (1/4) hesaplayıp II’yi doğru bulmuş; III’ü yanlış bulmuş.','bilgi'),('I ve II','I’i doğru bulmuş; II’de yalnız 1-1 sonucunu (1/4) hesaplayıp II’yi de doğru sanmış; III’ü yanlış bulmuş.','dikkat'),('I ve III','I’i doğru bulmuş, II’yi yanlış bulmuş; III’te ilk atışın 2 olması gerektiğini sanıp 1/4 bulmuş ve III’ü doğru kabul etmiş.','dikkat'),('II ve III','I’de yalnız (1, 4) ve (4, 1) sonuçlarını sayıp 1/8 bulduğu için I’i yanlış saymış; II’yi (1/4 ile) doğru bulmuş; III’te ilk atışın 2 olması gerektiğini sanmış.','bilgi')],
 sira=OS3,
 tipId='ol-kosullu2',tip='Koşullu olasılık ve iadesiz çekim',z='zor',alt='Hileli Zar',kaz='Olasılıkları tabloyla verilen hileli dört yüzlü zarın iki atışında toplam ve koşullu olasılık önermelerini değerlendirir.',kalip='öncüllü',
 kart='K-ABO2-06 (hileli zar, öncüllü) · eşit olmayan olasılıklar, toplam ve koşullu önerme',
 metin='Dört yüzü 1, 2, 3 ve 4 ile numaralandırılmış hileli bir zarın yüzlerinin üste gelme olasılıkları aşağıdaki tabloda verilmiştir. Bu zar art arda iki kez atılıyor ve üste gelen sayılar kaydediliyor.\nI. Sayıların toplamının 5 olma olasılığı 3/16’dır.\nII. İki atışta aynı sayının gelme olasılığı 1/4’tür.\nIII. İkinci atışta 4 geldiği bilindiğine göre, sayıların toplamının 5 olma olasılığı 1/4’tür.\nBuna göre bu önermelerden hangileri doğrudur?',
 istenen='Doğru olan önermeler.',ip=['Atışlar bağımsız olduğundan her önermede olasılıkları tablodaki değerlerin çarpımlarından kur.'],bilgi=[TBL,KOS if False else BAG2],
 sekil=tablo_svg(['Üste gelen sayı','1','2','3','4'],[['Olasılık','1/2','1/4','1/8','1/8']]),
 puf='Bağımsız atışlarda bir koşul, diğer atışın olasılık dağılımını değiştirmez.')

# ================= 20 zor · kuponla ürün alma (şekil) =================
KS_=[20,30,50,80,100]; FY=(30,50,80,60)
cnt=sum(1 for t in permutations(KS_,4) if all(t[i]>=FY[i] for i in range(4))); assert cnt==2 and len(list(permutations(KS_,4)))==120
v=Fr(2,120); assert v==Fr(1,60)
e=[Fr(4,120),Fr(8,120),Fr(4,5)*Fr(3,5)*Fr(2,5)*Fr(2,5),Fr(4*3*2*2,120)]; assert e==[Fr(1,30),Fr(1,15),Fr(48,625),Fr(2,5)] and len({v,*e})==5
q('0020',[A('En dar kısıtlı kişilerden başla','Can 80 TL ve Deniz 60 TL ürün için yalnız 80 ya da 100 TL’lik kuponları kullanabilir; bu iki kupon ikisine iki farklı biçimde dağılır.','Can, Deniz: 2 biçim'),
          A('Kalan kişileri yerleştir','Berk 50 TL ve üzeri kupon gerektirir; 80 ve 100 TL’lik kuponlar kullanıldığından yalnız 50 TL’lik kalır. Ayşe için 30 TL ve üzeri kuponlardan yalnız 30 TL’lik kalır.','Berk: 1 · Ayşe: 1 ⇒ 2 × 1 × 1 = 2 uygun'),
          A('Olasılığı bul','Uygun sıralı seçimler, bütün sıralı seçimlere bölünür.','5 × 4 × 3 × 2 = 120 ⇒ 2/120 = 1/60')],
 v,[(e[0],'Berk için 2 seçenek saymış (Can’ın ve Deniz’in kuponlarını yeterince çıkarmamış): 2 × 2 × 1 = 4 uygun.','dikkat'),(e[1],'Berk ve Ayşe için ikişer seçenek saymış: 2 × 2 × 2 = 8 uygun.','dikkat'),(e[2],'Kuponları geri konuyormuş gibi çekmiş: 4/5 · 3/5 · 2/5 · 2/5.','bilgi'),(e[3],'Uygun seçimleri 4 · 3 · 2 · 2 = 48 sayıp kuponların birbirinden farklı olması gerektiğini unutmuş.','islem')],
 tipId='ol-sayma2',tip='Kısıtlı sayma ile olasılık',z='zor',alt='Kuponla Alışveriş',kaz='İadesiz sıralı seçimde birden çok kısıtı birlikte sayıp olasılığı hesaplar.',kalip='hikâyeli',
 kart='K-ABO2-05 (iadesiz sıralı seçim, kısıtlı) · dört kişi, beş kupon, alt sınırlar',
 metin='Bir giyim mağazasının şekildeki 5 kuponunun değerleri kuponların üzerinde yazılıdır. Ayşe, Berk, Can ve Deniz sırasıyla bu kuponlardan birer tane rastgele seçiyor (seçilen kupon geri konmuyor). Kupon değeri, almak istedikleri ürünün fiyatına eşit ya da fiyattan büyükse ürünü alabiliyorlar. Ayşe’nin ürünü 30 TL, Berk’in ürünü 50 TL, Can’ın ürünü 80 TL, Deniz’in ürünü 60 TL’dir.\nBuna göre dört arkadaşın da ürününü alabilme olasılığı kaçtır?',
 istenen='Dört arkadaşın da ürününü alabilme olasılığı.',ip=['Her kişi için hangi kuponların yeterli olduğunu yaz ve kuponların tekrar kullanılamayacağını göz önünde tut.'],bilgi=[ISD],sekil=kupon_fig(KS_),
 puf='İadesiz seçimlerde kişilerin seçenekleri birbirini etkiler.')

# ---------- bitiş ----------
for qq in P.ANA: qq['kardes']=None
P.yaz(os.path.join(HD,'binomiki-1.json'),os.path.join(SCR,'bos-binomiki.json'))
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=UK))['kartlar'].append(c['id'])
json.dump(dict(konu='Binom ve Olasılık',surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 AYT Matematik çıkmış soruları ve yayın soru bankaları (yalnız mantık), MEB 11–12. sınıf müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),open(os.path.join(HV,'kartlar','binomiki.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
