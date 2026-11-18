"""Olasılık · ŞEKİLLİ ek paket b (10 soru): Venn, sütun/daire grafiği, ızgara yolu, koltuk planı, domino, yol ağı, zaman şeridi.
Şekil çözüm verisini taşır; her doğru ve çeldirici değer Fraction/tarama ile hesaplanıp assert edilir. Kardeş yok, ipucu 1."""
import sys,os,itertools,math
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
from math import comb,cos,sin,radians
from collections import Counter
H.KONU='Olasılık'
UK='matd|Olasılık'
P=Parti('olasisekb','Olasılık',UK)
KY='ÖSYM 2018–2026 TYT Matematik (şekilli, grafikli ve çizelgeli olasılık soruları; yalnız mantık) · MEB 10. sınıf'
def fs(x):
    x=Fr(x); return str(x.numerator) if x.denominator==1 else f'{x.numerator}/{x.denominator}'
def mkp(no,dogru,yan,**k):
    sira=[fs(v) for v in sorted({Fr(dogru),*[Fr(y[0]) for y in yan]})]; assert len(sira)==5
    mk(P,no,dogru=fs(dogru),yan=[(fs(y[0]),y[1],y[2]) for y in yan],sira=sira,**k)
def q(no,ad,**k): mkp(no,ad=ad,adim=len(ad),**k)
def fig(body,font='\\small'): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font='+font+']\n'+body+'\n\\end{tikzpicture}')
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)

# ---------- bilgi kutuları (yalnız tanım ve gösterim; örnekler soruların kurgusundan ve sayılarından farklı) ----------
TEM=B('Olasılık','eşit olasılıklı sonuçlarda bir olayın olasılığı, olayı oluşturan sonuç sayısının tüm sonuç sayısına oranıdır; değeri 0 ile 1 arasındadır. Örnek: 12 eş kartın 3’ü kırmızıysa rastgele çekilen kartın kırmızı olma olasılığı 3/12 = 1/4’tür')
VEN=B('Venn şeması','dikdörtgen tüm topluluğu, çemberler kümeleri gösterir; her bölgedeki sayı yalnızca o bölgedeki elemanların sayısıdır. Çemberlerin ortak bölgesindeki elemanlar o çemberlerin hepsine aittir. Örnek: iki çemberde yalnız birincide 7, ortak bölgede 2 kişi varsa birinci çemberin tamamında 9 kişi vardır')
SUT=B('Sütun grafiği','her sütunun yüksekliği, altındaki kategoride kaç eleman bulunduğunu gösterir; topluluğun tamamı sütun yüksekliklerinin toplamıdır. Örnek: üç sütunun yükseklikleri 5, 3 ve 2 ise topluluk 10 kişidir')
BAG=B('Bağımsız olaylar','bir olayın gerçekleşmesi diğerinin gerçekleşme olasılığını değiştirmiyorsa olaylar bağımsızdır; ardışık bağımsız olayların hepsinin birlikte olma olasılığı olasılıkların çarpımıdır. Bir olayın olmama olasılığı 1’den olma olasılığının çıkarılmasıyla bulunur. Örnek: yağış olasılığı %30 ise yağmama olasılığı %70’tir')
KOM=B('Kombinasyon','n elemanlı bir kümeden sırası önemsiz r eleman seçmenin yol sayısı C(n, r) = n! ÷ (r!(n − r)!) olarak yazılır. Örnek: 6 kişiden 2 kişilik bir ekip C(6, 2) = 15 farklı biçimde seçilir')
CAR=B('Çarpma ve toplama ilkesi','ardışık aşamalı bir işlemin toplam yol sayısı, her aşamadaki seçenek sayılarının çarpımıdır; birbirinden ayrı yollar varsa sayıları toplanır. Örnek: bir yolculuk iki aşamalıdır; ilkinde 2, ikincisinde 4 seçenek varsa 8 farklı yolculuk vardır')
DAI=B('Daire grafiği','dairenin her dilimi, bütünün yüzde kaçını oluşturduğunu gösterir; N elemanlı bir topluluğun %p’si N × p ÷ 100 elemandır. Örnek: 50 kişilik bir grupta %18’lik dilim 9 kişiyi gösterir')
DOM=B('Domino taşı','bir domino taşı iki yarıdan oluşur; her yarıda 0 ile 6 arasında nokta bulunur ve iki yarıdaki sayılar aynı olabilir. Örnek: 2 ve 5 noktalı yarılardan oluşan taş, “2–5” taşıdır; 5–2 aynı taştır')
UZN=B('Uzunluğa dayalı olasılık','sonuçlar bir doğru parçası üzerinde her noktada eş olasılıklıysa, olay olasılığı olaya uygun uzunluğun toplam uzunluğa oranıdır; ortak noktası olan aralıklar birleştirilince ortak kısım bir kez sayılır. Örnek: 40 dakikalık bir sürenin 10 dakikası uygunsa olasılık 1/4’tür')

# ---------- kartlar (her tipId için bir kart) ----------
kartla('K-OSC-01','Venn şemasından olasılık','İstenen koşulu sağlayan bölgeler belirlenip sayıları toplanır; tüm bölgelerin (dışarıdaki dahil) toplamı örnek uzayı verir.','Kesişimi iki kez ya da hiç saymamak; dışarıdaki elemanı paydaya katmamak; koşulun tümleyenini yazmak.','kolay','hikâyeli',3,'osc-venn','Venn şemasından olasılık')
kartla('K-OSC-02','Sütun grafiğinden olasılık','Sütun yükseklikleri okunur; koşulu sağlayan sütunlar toplanıp toplam frekansa oranlanır; ardışık bağımsız olaylarda dallanma tek tek hesaplanır.','“En az” ve “tam” koşulunu karıştırmak; kategori değerini kişi sayısı sanmak; bağımsız olayları toplamak.','kolay','grafik',3,'osc-grafik','Sütun grafiğinden olasılık')
kartla('K-OSC-03','Yol şemasında olasılık','Yol ya da rota sayıları çarpma ve toplama ilkesiyle bulunur; kapalı yol ve çift yönlü geçiş gibi koşullar tüm sayımda uygulanır.','Kapalı yolu atlamak; sayımda tümü yerine yalnız bir bölümü kullanmak; tek yönlü sanmak.','orta','hikâyeli',4,'osc-yol','Yol şemasında olasılık')
kartla('K-OSC-04','Daire grafiğinden iki seçim','Yüzdelerden kişi sayıları bulunur; iki farklı gruptan birer kişi seçme sayısı toplam çift sayısına oranlanır.','Geri koyarak çekim gibi hesaplamak; iki sıralamadan yalnız birini saymak; yüzdeleri toplamak.','orta','grafik',4,'osc-daire','Daire grafiğinden iki seçim')
kartla('K-OSC-05','Koltuk ve domino çiftleri','Uygun çift sayısı koşula göre elle sayılır; tüm çift sayısı C(n, 2) ile bulunur; sıra önemli olmadığından çiftler bir kez sayılır.','Koridoru ya da dolu koltuğu hesaba katmak; çiftleri sıralı saymak; sayımda nesneyi kendisiyle eşlemek.','orta','hikâyeli',4,'osc-ikili','Koltuk ve domino çiftleri')
kartla('K-OSC-06','Zaman şeridinde olasılık','Uygun zaman aralıkları şeritte işaretlenir, örtüşenler birleştirilir ve toplam uzunluk bütün uzunluğa oranlanır.','Örtüşen aralıkları iki kez saymak; yanlış yöne aralık çizmek; olayları bağımsız sanıp formül uygulamak.','zor','hikâyeli',5,'osc-zaman','Zaman şeridinde olasılık')

# ================= şekil yardımcıları =================
def barlar(vals,etik,ymax,ystep,xlab,ylab,bw=0.95,sp=1.35,sy=0.42,yetik=lambda j:str(j),vetik=lambda v:str(v)):
    o=[]; W=len(vals)*sp
    for j in range(0,ymax+1,ystep):
        o.append(f'\\draw[gray!40,thin] (0,{j*sy:.3f}) -- ({W:.3f},{j*sy:.3f}); \\node[left=2pt,font=\\footnotesize] at (0,{j*sy:.3f}) {{{yetik(j)}}};')
    o.append(f'\\draw[thick] (0,0) -- ({W+0.3:.3f},0); \\draw[thick] (0,0) -- (0,{ymax*sy+0.2:.3f});')
    for i,(v,e) in enumerate(zip(vals,etik)):
        x=sp*(i+0.5)
        o.append(f'\\filldraw[fill=vurgu!30,draw=black,thick] ({x-bw/2:.3f},0) rectangle ({x+bw/2:.3f},{v*sy:.3f});')
        o.append(f'\\node[above=1pt,font=\\small\\bfseries] at ({x:.3f},{v*sy:.3f}) {{{vetik(v)}}}; \\node[below=2pt,font=\\small] at ({x:.3f},0) {{{e}}};')
    o.append(f'\\node[font=\\small] at ({W/2:.3f},-0.95) {{{xlab}}}; \\node[font=\\small,anchor=south west] at (-0.2,{ymax*sy+0.25:.3f}) {{{ylab}}};')
    return '\n'.join(o)

# ================= 01 kolay · Venn şeması (iki küme) =================
S_,ORT,T_,DIS=14,6,9,11; N1=S_+ORT+T_+DIS; assert N1==40
v=Fr(S_+T_,N1); assert v==Fr(23,40)
e=[Fr(S_+ORT+T_,N1),Fr(S_+T_,S_+ORT+T_),Fr(S_+T_,N1-ORT),Fr((S_+ORT)+(ORT+T_),N1)]
assert e==[Fr(29,40),Fr(23,29),Fr(23,34),Fr(35,40)] and len({v,*e})==5 and v<min(e)
o=[f'\\draw[thick] (-3.1,-2.0) rectangle (3.1,2.0);',
 '\\draw[thick] (-0.85,0) circle (1.4); \\draw[thick] (0.85,0) circle (1.4);',
 '\\node[font=\\small\\bfseries] at (-1.55,1.7) {Satranç}; \\node[font=\\small\\bfseries] at (1.55,1.7) {Tiyatro};',
 f'\\node[font=\\large] at (-1.45,0) {{{S_}}}; \\node[font=\\large] at (0,0) {{{ORT}}}; \\node[font=\\large] at (1.45,0) {{{T_}}};',
 f'\\node[font=\\large] at (2.6,-1.5) {{{DIS}}};']
SK=fig('\n'.join(o))
q('0001',tipId='osc-venn',tip='Venn şemasından olasılık',z='kolay',alt='Venn Şeması',kaz='Venn şemasında bölgelerin sayılarından koşulu sağlayan öğrencileri belirleyip olasılığı hesaplar.',kalip='hikâyeli',
 kart='K-OSC-01 (iki kümeli Venn) · yalnız bir kulübe üye olan öğrenciler',
 metin='Şekilde, bir okuldaki öğrencilerin satranç ve tiyatro kulüplerine üyeliği gösterilmiştir. Dikdörtgen okulun tüm öğrencilerini, çemberler kulüpleri temsil etmekte ve her sayı, bulunduğu bölgedeki öğrenci sayısını göstermektedir. Okul müdürü, bu öğrenciler arasından rastgele bir öğrenci seçiyor.\nBuna göre seçilen öğrencinin yalnız bir kulübe üye olma olasılığı kaçtır?',
 dogru=v,yan=[(e[0],'“Yalnız bir kulüp” yerine “en az bir kulüp” koşulunu almış: kesişimdeki öğrencileri de saymış.','dikkat'),(e[1],'Paydaya kulübe üye olmayanları katmamış: yalnız kulüp üyeleri arasından seçilmiş gibi hesaplamış.','bilgi'),(e[2],'İki kulübe de üye olan öğrencileri örnek uzaydan çıkarmış: paydayı bunlar olmadan yazmış.','bilgi'),(e[3],'Her kulübün toplam üye sayısını ayrı ayrı toplamış; kesişimdeki öğrencileri iki kez saymış.','islem')],
 istenen='Seçilen öğrencinin yalnız bir kulübe üye olma olasılığı.',ip=['Hangi bölgeler “yalnız bir kulüp” koşuluna uyuyor ve tüm öğrenciler hangi bölgelerde yer alıyor?'],bilgi=[VEN],sekil=SK,
 ad=[A('Tüm öğrencileri say','Dört bölgedeki sayılar toplanır.','14 + 6 + 9 + 11 = 40'),A('Uygun bölgeleri belirle','Yalnız bir kulübe üye olanlar iki çemberin ortak olmayan bölgelerindedir.','14 + 9 = 23'),A('Olasılığı yaz','Uygun sayı tüm öğrenci sayısına oranlanır.','23/40')],
 puf='Şemada her bölgedeki sayıyı yalnızca o bölgedekileri gösteren sayı olarak oku.')

# ================= 02 kolay · sütun grafiği =================
KS=[3,6,8,7,4]; N2=sum(KS); assert N2==28
v=Fr(sum(KS[2:]),N2); assert v==Fr(19,28)
e=[Fr(KS[2],N2),Fr(sum(KS[3:]),N2),Fr(sum(KS[:3]),N2),Fr(2+3+4,0+1+2+3+4)]
assert e==[Fr(2,7),Fr(11,28),Fr(17,28),Fr(9,10)] and len({v,*e})==5
SK=fig(barlar(KS,['0','1','2','3','4'],10,2,'Okunan kitap sayısı','Öğrenci sayısı'))
q('0002',tipId='osc-grafik',tip='Sütun grafiğinden olasılık',z='kolay',alt='Sütun Grafiği',kaz='Sütun grafiğinden frekansları okuyup “en az” koşulunu sağlayan öğrencilerin olasılığını hesaplar.',kalip='grafik',
 kart='K-OSC-02 (sütun grafiği) · en az 2 kitap okuyanlar',
 metin='Şekildeki sütun grafiği, bir sınıftaki öğrencilerin geçen ay okuduğu kitap sayısına göre dağılımını göstermektedir; her sütunun üzerindeki sayı o gruptaki öğrenci sayısını belirtir. Bu sınıftan, kura ile bir öğrenci rastgele seçiliyor.\nBuna göre seçilen öğrencinin geçen ay en az 2 kitap okumuş olma olasılığı kaçtır?',
 dogru=v,yan=[(e[0],'“En az 2” koşulunu “tam 2” gibi okumuş: yalnız 2 kitap okuyanları almış.','dikkat'),(e[1],'“En az 2” yerine “2’den çok” koşulunu kullanmış: 2 kitap okuyanları katmamış.','dikkat'),(e[2],'“En az 2” yerine “en fazla 2” koşulunu kullanmış.','dikkat'),(e[3],'Sütunların altındaki kitap sayılarını öğrenci sayısı sanıp 2 + 3 + 4 toplamını 0 + 1 + 2 + 3 + 4’e oranlamış.','bilgi')],
 istenen='Seçilen öğrencinin en az 2 kitap okumuş olma olasılığı.',ip=['Hangi sütunlar “en az 2” koşuluna uyuyor ve sınıf mevcudu sütunların hangi niceliğinden bulunuyor?'],bilgi=[SUT],sekil=SK,
 ad=[A('Sınıf mevcudunu bul','Tüm sütunlardaki öğrenci sayıları toplanır.','3 + 6 + 8 + 7 + 4 = 28'),A('Uygun öğrencileri say','2, 3 ve 4 kitap okuyanlar toplanır.','8 + 7 + 4 = 19'),A('Olasılığı yaz','Uygun sayı mevcuda oranlanır.','19/28')],
 puf='Sütunun altındaki sayı kategoriyi, üstündeki sayı öğrenci sayısını gösterir.')

# ================= 03 orta · ızgara yolu, kapalı sokak =================
W3,H3=5,4; KAPALI={((0,1),(1,1))}; C3=(3,2)
def say3(kapali,a=(0,0),b=(W3,H3)):
    dp={a:1}
    for y in range(a[1],b[1]+1):
        for x in range(a[0],b[0]+1):
            if (x,y)==a: continue
            s_=0
            if x>a[0] and ((x-1,y),(x,y)) not in kapali: s_+=dp.get((x-1,y),0)
            if y>a[1] and ((x,y-1),(x,y)) not in kapali: s_+=dp.get((x,y-1),0)
            dp[(x,y)]=s_
    return dp[b]
tot=say3(KAPALI); thr=say3(KAPALI,(0,0),C3)*say3(KAPALI,C3,(W3,H3)); tot0=say3(set()); thr0=comb(5,3)*comb(4,2)
assert (tot,thr,tot0,thr0)==(91,42,126,60)
# kaba kuvvet doğrulama
brute=[]
for ad_ in itertools.combinations(range(W3+H3),W3):
    x=y=0; yol=[(0,0)]; ok=True
    for i in range(W3+H3):
        nx,ny=(x+1,y) if i in ad_ else (x,y+1)
        if ((x,y),(nx,ny)) in KAPALI: ok=False
        x,y=nx,ny; yol.append((x,y))
    if ok: brute.append(yol)
assert len(brute)==tot and sum(1 for y_ in brute if C3 in y_)==thr
v=Fr(thr,tot); assert v==Fr(6,13)
e=[Fr(thr0,tot0),Fr(1,2),Fr(thr0,tot),Fr(thr,tot-thr)]
assert e==[Fr(10,21),Fr(1,2),Fr(60,91),Fr(6,7)] and len({v,*e})==5 and v<min(e)
sx,sy=1.3,1.0; o=[]
for i in range(W3+1): o.append(f'\\draw[gray!70,thick] ({i*sx},0) -- ({i*sx},{H3*sy});')
for j in range(H3+1): o.append(f'\\draw[gray!70,thick] (0,{j*sy}) -- ({W3*sx},{j*sy});')
for i in range(W3+1):
    for j in range(H3+1): o.append(f'\\fill ({i*sx},{j*sy}) circle (0.05);')
(xa,ya),(xb,yb)=list(KAPALI)[0]
o.append(f'\\draw[white,line width=3.5pt] ({xa*sx},{ya*sy}) -- ({xb*sx},{yb*sy}); \\node[font=\\huge\\bfseries] at ({(xa+xb)/2*sx},{(ya+yb)/2*sy}) {{$\\boldsymbol{{\\times}}$}};')
o.append(f'\\node[draw,thick,fill=vurgu!25,circle,inner sep=1.5pt,font=\\small\\bfseries] at (0,0) {{A}}; \\node[draw,thick,fill=vurgu!25,circle,inner sep=1.5pt,font=\\small\\bfseries] at ({W3*sx},{H3*sy}) {{B}};')
o.append(f'\\node[draw,thick,fill=white,circle,inner sep=1.5pt,font=\\small\\bfseries] at ({C3[0]*sx},{C3[1]*sy}) {{C}};')
SK=fig('\n'.join(o))
q('0003',tipId='osc-yol',tip='Yol şemasında olasılık',z='orta',alt='Izgara Yolu',kaz='Kapalı bir sokağın bulunduğu ızgara şemasında en kısa yolların sayısını bulup belirli bir kavşaktan geçme olasılığını hesaplar.',kalip='hikâyeli',
 kart='K-OSC-03 (ızgara yolu, kapalı sokak) · 5 × 4 ızgara; kapalı sokak; C kavşağı',
 metin='Bir kurye, şekildeki mahallede A noktasındaki depodan B noktasındaki müşteriye teslimat yapacaktır. Her adımda yalnızca sağa ya da yukarı doğru bir sokak boyunca ilerleyen kurye, A’dan B’ye giden en kısa yollar arasından rastgele birini seçmektedir; bu yolların hepsi eş olasılıklıdır. Şekilde × ile işaretli sokak kapalıdır ve bu sokaktan geçilemez.\nBuna göre kuryenin seçtiği yolun C kavşağından geçme olasılığı kaçtır?',
 dogru=v,yan=[(e[0],'Kapalı sokağı hiç hesaba katmamış: C’den geçen 60 yolu tüm 126 yola oranlamış.','dikkat'),(e[1],'Yolun C’den ya geçeceğini ya geçmeyeceğini düşünüp iki durumu eş olasılıklı saymış.','bilgi'),(e[2],'Kapalı sokağı yalnızca paydada uygulamış: C’den geçen yolları 60 bulup 91 yola oranlamış.','dikkat'),(e[3],'C’den geçen yolları C’den geçmeyen yollara oranlamış: 42 ÷ 49.','islem')],
 istenen='Seçilen yolun C kavşağından geçme olasılığı.',ip=['A’dan C’ye ve C’den B’ye kaç yol var; kapalı sokak hangi sayımları etkiliyor?'],bilgi=[KOM],sekil=SK,
 ad=[A('Tüm yolları say','Sokak kapalı olmasaydı 5 sağa ve 4 yukarı adımın sıralanması kadar yol olurdu.','C(9, 4) = 126'),A('Kapalı sokağı çıkar','Kapalı sokağı kullanan yollar A’dan sokağın başına 1, sokağın ucundan B’ye 35 yoldur.','126 − 1 × 35 = 91'),A('C’den geçenleri say','A’dan C’ye 10 yoldan kapalı sokaktan geçen 3’ü çıkarılır; C’den B’ye 6 yol vardır.','(10 − 3) × 6 = 42'),A('Olasılığı yaz','Uygun yollar tüm yollara oranlanır.','42/91 = 6/13')],
 puf='Sonucu, sokak açık olsaydı bulacağın olasılıkla karşılaştırıp yorumla.')

# ================= 04 orta · daire grafiği, iki seçim =================
D4=[('Servis',40),('Yürüyerek',25),('Otobüs',20),('Bisiklet',15)]; N4=20
kis={a:N4*p//100 for a,p in D4}; assert kis=={'Servis':8,'Yürüyerek':5,'Otobüs':4,'Bisiklet':3} and sum(kis.values())==N4
v=Fr(kis['Servis']*kis['Yürüyerek'],comb(N4,2)); assert v==Fr(4,19)
e=[Fr(8,20)*Fr(5,19),Fr(40,100)*Fr(25,100),2*Fr(40,100)*Fr(25,100),Fr(40+25,100)]
assert e==[Fr(2,19),Fr(1,10),Fr(1,5),Fr(13,20)] and len({v,*e})==5
# toplu kaba kuvvet
cnt=0
kum=[a for a,p in D4 for _ in range(N4*p//100)]
for x,y in itertools.combinations(range(N4),2):
    if {kum[x],kum[y]}=={'Servis','Yürüyerek'}: cnt+=1
assert Fr(cnt,comb(N4,2))==v
o=[]; a0=90
for k,(ad_,p) in enumerate(D4):
    a1=a0-3.6*p; mid=(a0+a1)/2
    o.append(f'\\filldraw[fill=vurgu!{10+22*k},draw=black,thick] (0,0) -- ({a0}:1.55) arc({a0}:{a1}:1.55) -- cycle;')
    anc='west' if cos(radians(mid))>0.2 else ('east' if cos(radians(mid))<-0.2 else 'center')
    o.append(f'\\node[anchor={anc},align=center,font=\\small] at ({mid}:1.75) {{{ad_}\\\\\\textbf{{\\%{p}}}}};' if anc!='center' else f'\\node[anchor=north,align=center,font=\\small] at ({mid}:1.7) {{{ad_}\\\\\\textbf{{\\%{p}}}}};')
    a0=a1
SK=fig('\n'.join(o))
q('0004',tipId='osc-daire',tip='Daire grafiğinden iki seçim',z='orta',alt='Daire Grafiği',kaz='Daire grafiğindeki yüzdelerden kişi sayılarını bulup iki kişinin farklı iki gruptan seçilme olasılığını hesaplar.',kalip='grafik',
 kart='K-OSC-04 (daire grafiği) · 20 öğrenci; servis %40, yürüyerek %25',
 metin='Şekildeki daire grafiği, 20 öğrencilik bir sınıfta öğrencilerin okula gelişte kullandığı ulaşım türlerinin dağılımını yüzde olarak göstermektedir. Her öğrenci yalnızca bir ulaşım türünü kullanmaktadır. Bu sınıftan rastgele iki öğrenci birlikte seçiliyor.\nBuna göre seçilen öğrencilerden birinin servisle, diğerinin yürüyerek geldiği olasılık kaçtır?',
 dogru=v,yan=[(e[0],'İki öğrenciyi sırayla seçip yalnızca “önce servis, sonra yürüyerek” sırasını hesaplamış: 8/20 × 5/19.','dikkat'),(e[1],'Yüzdeleri doğrudan çarpıp iki sıralamadan yalnız birini almış: 0,4 × 0,25.','bilgi'),(e[2],'Seçimi geri koyarak yapıyormuş gibi iki sıralamayı da sayıp yüzdeleri çarpmış: 2 × 0,4 × 0,25.','bilgi'),(e[3],'İki yüzdeyi toplamış: servis ve yürüyerek gelenlerin toplam oranını olasılık sanmış.','islem')],
 istenen='Birinin servisle, diğerinin yürüyerek geldiği olasılık.',ip=['Yüzdeleri kişi sayısına çevirdikten sonra iki öğrencinin seçilebileceği tüm çiftlerin sayısını düşün.'],bilgi=[DAI,KOM],sekil=SK,
 ad=[A('Kişi sayılarını bul','Yüzdeler 20 ile çarpılır.','servis 8 · yürüyerek 5'),A('Uygun çiftleri say','Servisten bir, yürüyenlerden bir öğrenci seçilir.','8 × 5 = 40'),A('Tüm çiftleri say','20 öğrenciden 2 öğrenci seçilir.','C(20, 2) = 190'),A('Olasılığı yaz','Uygun çiftler tüm çiftlere oranlanır.','40/190 = 4/19')],
 puf='Aynı anda seçimde çiftlerin sırası yoktur; hem uygun hem tüm çiftleri aynı biçimde say.')

# ================= 05 orta · koltuk planı =================
OKS=3                       # koridor 3. ile 4. koltuk arasında
dolu=[{2,5},{1,4}]; bos=[[k for k in range(1,7) if k not in d] for d in dolu]
koltuk=[(r,k) for r in range(2) for k in bos[r]]; assert len(koltuk)==8
yan=lambda a,b:a[0]==b[0] and abs(a[1]-b[1])==1 and not ({a[1],b[1]}=={3,4})
cift=list(itertools.combinations(koltuk,2)); assert len(cift)==28
uy=[c for c in cift if yan(*c)]; assert len(uy)==2
v=Fr(len(uy),len(cift)); assert v==Fr(1,14)
aral=[c for c in cift if c[0][0]==c[1][0] and abs(c[0][1]-c[1][1])==1]; assert len(aral)==3        # koridoru geçen çift de sayılırsa
ond=[c for c in cift if c[0][1]==c[1][1] and c[0][0]!=c[1][0]]; assert len(ond)==2                   # ön-arka komşular
sira_=[c for c in cift if c[0][0]==c[1][0]]; assert len(sira_)==12
e=[Fr(len(aral),28),Fr(len(uy)+len(ond),28),Fr(len(uy),comb(12,2)),Fr(len(sira_),28)]
assert e==[Fr(3,28),Fr(1,7),Fr(1,33),Fr(3,7)] and len({v,*e})==5
o=[]; sz=0.75; g=0.12
def kx(k): return (k-1)*(sz+g)+(0.5 if k>OKS else 0)
for r in range(2):
    y=-r*(sz+0.25)
    o.append(f'\\node[font=\\small,anchor=east] at (-0.2,{y+sz/2:.2f}) {{{r+1}. sıra}};')
    for k in range(1,7):
        fill='gray!55' if k in dolu[r] else 'white'
        o.append(f'\\filldraw[fill={fill},draw=black,thick,rounded corners=2pt] ({kx(k):.2f},{y:.2f}) rectangle ({kx(k)+sz:.2f},{y+sz:.2f}); \\node[font=\\footnotesize] at ({kx(k)+sz/2:.2f},{y+sz/2:.2f}) {{{k}}};')
o.append(f'\\node[font=\\small] at ({kx(3)+sz+0.25+g/2:.2f},{-(sz+0.25)-0.55:.2f}) {{koridor}};')
o.append(f'\\filldraw[fill=gray!55,draw=black,thick] (0,-2.55) rectangle (0.4,-2.15); \\node[font=\\small,anchor=west] at (0.5,-2.35) {{dolu koltuk}}; \\filldraw[fill=white,draw=black,thick] (3.0,-2.55) rectangle (3.4,-2.15); \\node[font=\\small,anchor=west] at (3.5,-2.35) {{boş koltuk}};')
SK=fig('\n'.join(o))
q('0005',tipId='osc-ikili',tip='Koltuk ve domino çiftleri',z='orta',alt='Koltuk Planı',kaz='Koltuk planında koridor ve dolu koltukları dikkate alarak iki kişinin yan yana oturma olasılığını hesaplar.',kalip='hikâyeli',
 kart='K-OSC-05 (koltuk planı) · iki sıra, koridor; 8 boş koltuk; yan yana çiftler',
 metin='Bir sinema salonunun iki sıralı bir bölümündeki koltukların durumu şekilde gösterilmiştir; koltuklar her sırada 1’den 6’ya numaralanmıştır ve 3. ile 4. koltukların arasında bir koridor vardır. Zeynep ile Mert, boş koltuklar arasından rastgele iki farklı koltuk seçip oturuyor. Aynı sırada, numaraları ardışık olan ve aralarında koridor bulunmayan iki koltuk “yan yana” sayılıyor.\nBuna göre Zeynep ile Mert’in yan yana oturma olasılığı kaçtır?',
 dogru=v,yan=[(e[0],'Koridorun iki yanındaki koltukları da yan yana sayıp uygun çifti 3 bulmuş.','dikkat'),(e[1],'Önlü arkalı oturan çifti de yan yana saymış: uygun çifti 4 bulmuş.','dikkat'),(e[2],'Dolu koltukları da seçilebilir sanıp tüm çiftleri 12 koltuktan hesaplamış.','bilgi'),(e[3],'Yan yana olmayı “aynı sırada oturmak” sanıp aynı sıradaki 12 çifti saymış.','bilgi')],
 istenen='Zeynep ile Mert’in yan yana oturma olasılığı.',ip=['Önce hangi koltukların seçilebilir olduğunu belirle; sonra yan yana koşulunun bu koltuklarda hangi çiftleri sağladığına bak.'],bilgi=[KOM],sekil=SK,
 ad=[A('Boş koltukları say','Şekilde 1. sırada 4, 2. sırada 4 boş koltuk vardır.','4 + 4 = 8'),A('Tüm çiftleri say','8 koltuktan 2 koltuk seçilir.','C(8, 2) = 28'),A('Yan yana çiftleri bul','1. sırada boş ardışık çift yalnız koridorun iki yanında; 2. sırada iki ardışık çift var.','1. sıra: 0 · 2. sıra: 2'),A('Olasılığı yaz','Uygun çiftler tüm çiftlere oranlanır.','2/28 = 1/14')],
 puf='“Yan yana” sayılma koşulunu önce tek tek çiftlerde sına, sonra say.')

# ================= 06 orta · yağış olasılıkları çubuk grafiği =================
p6=[Fr(20,100),Fr(50,100),Fr(40,100)]
def tam(k): return sum(math.prod(p6[i] if i in S_ else 1-p6[i] for i in range(3)) for S_ in itertools.combinations(range(3),k))
assert [tam(k) for k in range(4)]==[Fr(6,25)*0+Fr(24,100),Fr(46,100),Fr(26,100),Fr(4,100)]
v=tam(2)+tam(3); assert v==Fr(3,10)
e=[tam(2),1-tam(0),tam(1),tam(3)]
assert e==[Fr(13,50),Fr(19,25),Fr(23,50),Fr(1,25)] and len({v,*e})==5
SK=fig(barlar([20,50,40],['Cuma','Cumartesi','Pazar'],100,20,'Gün','Yağış olasılığı (\\%)',sp=1.9,bw=1.1,sy=0.032,vetik=lambda v:f'\\%{v}'))
q('0006',tipId='osc-grafik',tip='Sütun grafiğinden olasılık',z='orta',alt='Yağış Olasılığı',kaz='Sütun grafiğinde verilen bağımsız yağış olasılıklarından “en az iki gün” olayının olasılığını hesaplar.',kalip='grafik',
 kart='K-OSC-02 (yağış çubuk grafiği) · üç gün %20, %50, %40; en az iki gün',
 metin='Bir meteoroloji istasyonu, Cuma, Cumartesi ve Pazar günleri için yağış olasılıklarını şekildeki sütun grafiğiyle duyurmuştur. Günlerdeki yağışların birbirinden bağımsız olduğu kabul edilmektedir.\nBuna göre bu üç günün en az ikisinde yağmur yağma olasılığı kaçtır?',
 dogru=v,yan=[(e[0],'“En az iki” yerine “tam iki gün” olayını hesaplamış; üç günün de yağmurlu olduğu durumu eklememiş.','dikkat'),(e[1],'“En az iki” yerine “en az bir gün” olayını hesaplamış: 1 − 0,8 × 0,5 × 0,6.','dikkat'),(e[2],'“En az iki” yerine “tam bir gün” olayını hesaplamış.','dikkat'),(e[3],'Yalnız üç günün de yağmurlu olduğu durumu almış: 0,2 × 0,5 × 0,4.','bilgi')],
 istenen='Üç günün en az ikisinde yağmur yağma olasılığı.',ip=['“En az iki” koşulunu hangi gün sayılarında yağmur yağması olarak ayırabilirsin?'],bilgi=[BAG],sekil=SK,
 ad=[A('Yağmursuz olasılıklar','Her gün için 1 − p yazılır.','0,8 · 0,5 · 0,6'),A('Tam iki gün','Üç durum toplanır: Cuma ve Cumartesi, Cuma ve Pazar, Cumartesi ve Pazar yağmurlu.','0,2·0,5·0,6 + 0,2·0,5·0,4 + 0,8·0,5·0,4 = 0,26'),A('Üç gün','Üç günde de yağmur olasılığı hesaplanır.','0,2 · 0,5 · 0,4 = 0,04'),A('Topla','İki durum toplanır.','0,26 + 0,04 = 0,30 = 3/10')],
 puf='“En az” koşulunda uygun tüm durumları (tam sayısı ve daha fazlası) ayrı ayrı yaz.')

# ================= 07 zor · Venn şeması (üç küme), iki kişi seçimi =================
R7=dict(F=8,B=6,V=5,FB=4,FV=3,BV=2,FBV=1,YOK=11); N7=sum(R7.values()); assert N7==40
yalB=R7['B']; enAz2=R7['FB']+R7['FV']+R7['BV']+R7['FBV']; assert enAz2==10
v=Fr(yalB*enAz2,comb(N7,2)); assert v==Fr(1,13)
# kaba kuvvet
kimlik=[k for k,n in R7.items() for _ in range(n)]
sy_=lambda k:0 if k=='YOK' else (1 if len(k)==1 else len(k))
c7=0
for a,b in itertools.combinations(range(N7),2):
    ka,kb=kimlik[a],kimlik[b]
    if (ka=='B' and sy_(kb)>=2) or (kb=='B' and sy_(ka)>=2): c7+=1
assert Fr(c7,comb(N7,2))==v
tam2=R7['FB']+R7['FV']+R7['BV']
e=[Fr(yalB,N7)*Fr(enAz2,N7-1),Fr(yalB,N7)*Fr(enAz2,N7),Fr(yalB*tam2,comb(N7,2)),2*Fr(yalB,N7)*Fr(enAz2,N7)]
assert e==[Fr(1,26),Fr(3,80),Fr(9,130),Fr(3,40)] and len({v,*e})==5 and v>max(e)
o=['\\draw[thick] (-3.4,-3.1) rectangle (3.4,2.7);',
 '\\draw[thick] (-0.9,0.55) circle (1.5); \\draw[thick] (0.9,0.55) circle (1.5); \\draw[thick] (0,-1.0) circle (1.5);',
 '\\node[font=\\small\\bfseries] at (-1.9,2.35) {Futbol}; \\node[font=\\small\\bfseries] at (1.9,2.35) {Basketbol}; \\node[font=\\small\\bfseries] at (0,-2.8) {Voleybol};']
for (x,y),k in [((-1.75,0.95),'F'),((1.75,0.95),'B'),((0,-1.95),'V'),((0,1.35),'FB'),((-0.95,-0.55),'FV'),((0.95,-0.55),'BV'),((0,0.15),'FBV'),((2.85,-2.5),'YOK')]:
    o.append(f'\\node[font=\\large] at ({x},{y}) {{{R7[k]}}};')
SK=fig('\n'.join(o))
q('0007',tipId='osc-venn',tip='Venn şemasından olasılık',z='zor',alt='Üç Kümeli Venn',kaz='Üç kümeli Venn şemasında bölge sayılarından koşullu iki kişilik seçimin olasılığını hesaplar.',kalip='şekilli',
 kart='K-OSC-01 (üç kümeli Venn) · yalnız basketbol ve en az iki kurs; iki kişi seçimi',
 metin='Şekilde, bir spor kompleksindeki öğrencilerin futbol, basketbol ve voleybol kurslarına katılımı gösterilmiştir. Dikdörtgen kompleksteki tüm öğrencileri, çemberler kursları temsil etmekte ve her sayı, bulunduğu bölgedeki öğrenci sayısını belirtmektedir. Bu öğrenciler arasından rastgele iki kişi birlikte seçiliyor.\nBuna göre seçilenlerden birinin yalnız basketbol kursuna katılan, diğerinin ise en az iki kursa katılan bir öğrenci olma olasılığı kaçtır?',
 dogru=v,yan=[(e[0],'İki kişiyi sırayla çekip yalnızca bir sırayı hesaplamış: 6/40 × 10/39.','dikkat'),(e[1],'İkinci seçimde havuzu yeniden 40 kişi sayıp bir sırayı almış: 6/40 × 10/40.','bilgi'),(e[2],'“En az iki kurs” yerine “tam iki kurs” koşulunu almış: üç kursa katılan öğrenciyi saymamış.','dikkat'),(e[3],'İkinci seçimde havuzu yeniden 40 kişi sayıp iki sırayı da hesaplamış: 2 × 6/40 × 10/40.','bilgi')],
 istenen='Birinin yalnız basketbol, diğerinin en az iki kurs olma olasılığı.',ip=['Şemadaki hangi bölgeler “yalnız basketbol” ve “en az iki kurs” koşullarına uyuyor ve iki kişilik seçimde bu iki grup birlikte nasıl sayılır?'],bilgi=[VEN,KOM],sekil=SK,
 ad=[A('Tüm öğrencileri say','Sekiz bölgedeki sayılar toplanır.','8 + 6 + 5 + 4 + 3 + 2 + 1 + 11 = 40'),A('İki grubu belirle','Yalnız basketbol 6 kişi; en az iki kurs, ortak bölgelerdeki 4, 3, 2 ve 1’in toplamıdır.','6 kişi ve 4 + 3 + 2 + 1 = 10 kişi'),A('Uygun çiftleri say','Her gruptan birer kişi seçilir.','6 × 10 = 60'),A('Tüm çiftleri say','40 kişiden 2 kişi seçilir.','C(40, 2) = 780'),A('Olasılığı yaz','Uygun çiftler tüm çiftlere oranlanır.','60/780 = 1/13')],
 puf='Bir bölgedeki sayıyı yalnız o bölgenin sayısı olarak oku; ortak bölgeleri hangi koşula katacağını yazarak belirle.')

# ================= 08 zor · domino taşları =================
T8=[(0,2),(0,4),(0,5),(1,3),(2,2),(4,4),(4,5)]; assert len(set(T8))==7
GOR=[(2,0),(0,4),(5,0),(3,1),(2,2),(4,4),(5,4)]; assert sorted(tuple(sorted(t)) for t in GOR)==sorted(T8)
cift8=list(itertools.combinations(T8,2)); assert len(cift8)==21
uy8=[c for c in cift8 if set(c[0])&set(c[1])]; assert len(uy8)==8
v=Fr(len(uy8),21); assert v==Fr(8,21)
# öğrenci hataları
e_sira=Fr(len(uy8),7*6)                                          # sırasız uygun / sıralı tüm çift
cifts=[t for t in T8 if t[0]==t[1]]
e_cift=Fr(len([c for c in uy8 if c[0] not in cifts and c[1] not in cifts]),21)    # çift taşları bağlanmaz sanmış
ordered=sum(1 for a in T8 for b in T8 if set(a)&set(b))           # kendisiyle eşleme dahil, geri koyarak sıralı
e_iade=Fr(ordered,49)
cnt=Counter(x for t in T8 for x in t)                              # nokta sayısına göre sayım
e_nokta=Fr(sum(k*(k-1)//2 for k in cnt.values()),21)
e=[e_sira,e_cift,e_iade,e_nokta]
assert e==[Fr(4,21),Fr(5,21),Fr(23,49),Fr(13,21)] and len({v,*e})==5
PIP={0:[],1:[(0,0)],2:[(-.2,.2),(.2,-.2)],3:[(-.2,.2),(0,0),(.2,-.2)],4:[(-.2,.2),(.2,.2),(-.2,-.2),(.2,-.2)],5:[(-.2,.2),(.2,.2),(0,0),(-.2,-.2),(.2,-.2)],6:[(-.2,.25),(-.2,0),(-.2,-.25),(.2,.25),(.2,0),(.2,-.25)]}
o=[]; tw,th=1.6,0.8
for i,(a,b) in enumerate(GOR):
    x=(i%4)*(tw+0.4) if i<4 else (i-4)*(tw+0.4)+(tw+0.4)/2; y=0 if i<4 else -(th+0.45)
    o.append(f'\\filldraw[fill=white,draw=black,line width=1.1pt,rounded corners=3pt] ({x:.2f},{y:.2f}) rectangle ({x+tw:.2f},{y+th:.2f}); \\draw[thick] ({x+tw/2:.2f},{y+0.08:.2f}) -- ({x+tw/2:.2f},{y+th-0.08:.2f});')
    for h,n in ((0,a),(1,b)):
        cx=x+tw/4+h*tw/2; cy=y+th/2
        for dx,dy in PIP[n]: o.append(f'\\fill ({cx+dx:.2f},{cy+dy:.2f}) circle (0.09);')
SK=fig('\n'.join(o))
q('0008',tipId='osc-ikili',tip='Koltuk ve domino çiftleri',z='orta',alt='Domino Taşları',kaz='Şekildeki domino taşlarından rastgele çekilen iki taşın ortak sayı taşıma olasılığını tüm çiftleri tarayarak hesaplar.',kalip='yeni nesil',
 kart='K-OSC-05 (domino) · yedi taş; ortak sayısı olan çiftler',
 metin='Şekildeki yedi domino taşı yüzü aşağı bakacak biçimde karıştırılıyor ve rastgele ikisi birlikte çekiliyor. Bir domino taşının iki yarısındaki nokta sayıları birer sayı kabul edilir; çekilen iki taşın üzerinde ortak en az bir sayı varsa bu iki taş uç uca eklenebilir.\nBuna göre çekilen iki taşın uç uca eklenebilmesi olasılığı kaçtır?',
 dogru=v,yan=[(e[0],'Uygun çiftleri doğru bulmuş (8), tüm çiftleri sıralı sayıp 7 × 6 = 42 almış.','islem'),(e[1],'İki yarısı aynı olan taşların başka bir taşla uç uca eklenemeyeceğini sanıp onları içeren çiftleri saymamış.','dikkat'),(e[2],'Taşı çektikten sonra geri koyup ikinciyi çekiyormuş gibi sıralı çiftleri saymış: aynı taşı kendisiyle de eşleştirmiş (7 + 16) ve 49’a oranlamış.','bilgi'),(e[3],'Çiftleri taşlar yerine nokta sayılarına göre saymış: çift sayılı taştaki sayıyı iki kez sayıp her sayı için C(k, 2) toplamış.','bilgi')],
 istenen='Çekilen iki taşın uç uca eklenebilmesi olasılığı.',ip=['Taşları yan yana yazıp ortak sayı taşıyan çiftleri sistemli biçimde, hiçbir çifti iki kez saymadan listele.'],bilgi=[DOM,KOM],sekil=SK,
 ad=[A('Taşları oku','Şekildeki taşlar yazılır.','0–2, 0–4, 0–5, 1–3, 2–2, 4–4, 4–5'),A('Tüm çiftleri say','7 taştan 2 taş seçilir.','C(7, 2) = 21'),A('Ortak sayılı çiftleri bul','0 sayısı üç taşta ortak; 2, 4 ve 5 sayıları için de yeni çiftler bulunur, 1–3 taşı hiçbiriyle çift oluşturmaz.','8 çift'),A('Olasılığı yaz','Uygun çiftler tüm çiftlere oranlanır.','8/21')],
 puf='Çiftleri listelerken her taşı yalnız bir kez “ilk taş” yaparak ilerle.')

# ================= 09 zor · yol ağı =================
KEN={('A','B'):2,('A','C'):3,('B','C'):1,('B','D'):2,('C','D'):2,('D','E'):3}
def yol_say(kenlar,oncelik=None):
    adj={}
    for (a,b),k in kenlar.items(): adj.setdefault(a,[]).append((b,k)); adj.setdefault(b,[]).append((a,k))
    sonuc=[]
    def git(u,gez,agirlik):
        if u=='E': sonuc.append((gez,agirlik)); return
        for w,k in adj[u]:
            if w not in gez: git(w,gez+[w],agirlik*k)
    git('A',['A'],1); return sonuc
R9=yol_say(KEN); toplam=sum(a for g,a in R9); C_den=sum(a for g,a in R9 if 'C' in g); B_den=sum(a for g,a in R9 if 'B' in g)
assert sorted(''.join(g) for g,a in R9)==['ABCDE','ABDE','ACBDE','ACDE'] and (toplam,C_den,B_den)==(60,48,42)
v=Fr(C_den,toplam); assert v==Fr(4,5)
K2=dict(KEN); del K2[('B','C')]; R9b=yol_say(K2); e1=Fr(sum(a for g,a in R9b if 'C' in g),sum(a for g,a in R9b))
e2=Fr(sum(1 for g,a in R9 if 'C' in g),len(R9))
R9c=[(g,a) for g,a in R9 if ''.join(g)!='ACBDE']; e3=Fr(sum(a for g,a in R9c if 'C' in g),sum(a for g,a in R9c))
e4=Fr(B_den,toplam)
e=[e1,e2,e3,e4]; assert e==[Fr(3,5),Fr(3,4),Fr(5,7),Fr(7,10)] and len({v,*e})==5
pos={'A':(0,0),'B':(2.8,1.6),'C':(2.8,-1.6),'D':(5.6,0),'E':(8.2,0)}
o=[]
etp={('A','B'):(0.5,'above left'),('A','C'):(0.5,'below left'),('B','D'):(0.5,'above right'),('C','D'):(0.5,'below right'),('D','E'):(0.5,'above'),('B','C'):(0.5,'right')}
for (a,b),k in KEN.items():
    (xa,ya),(xb,yb)=pos[a],pos[b]
    o.append(f'\\draw[thick] ({xa},{ya}) -- ({xb},{yb}) node[midway,fill=white,inner sep=1.5pt,font=\\small] {{{k} yol}};')
for n,(x,y) in pos.items(): o.append(f'\\node[draw,thick,circle,fill=vurgu!15,minimum size=0.75cm,inner sep=0pt,font=\\normalsize\\bfseries] at ({x},{y}) {{{n}}};')
SK=fig('\n'.join(o))
q('0009',tipId='osc-yol',tip='Yol şemasında olasılık',z='zor',alt='Şehirler Arası Yollar',kaz='Çift yönlü yol ağında çarpma ve toplama ilkesiyle tüm rotaları sayıp belirli bir şehirden geçen rota olasılığını hesaplar.',kalip='hikâyeli',
 kart='K-OSC-03 (yol ağı) · A→E rotaları; C şehrinden geçenler',
 metin='Şekilde, beş şehir ve şehirleri birleştiren yollar gösterilmiştir; her şehir çiftini birleştiren yol sayısı yolun üzerinde yazılıdır ve bütün yollar çift yönlüdür. Bir gezgin A şehrinden E şehrine, hiçbir şehre ikinci kez uğramadan gidecektir. Gezginin kullanabileceği tüm rotalar eş olasılıklıdır; aynı şehirlerden geçip farklı yolları kullanan rotalar da farklı rota sayılır.\nBuna göre gezginin seçtiği rotanın C şehrinden geçme olasılığı kaçtır?',
 dogru=v,yan=[(e[0],'B ile C şehirleri arasındaki yolu hiç kullanmamış: yalnızca A–B–D–E ve A–C–D–E rotalarını saymış.','dikkat'),(e[1],'Rotaları yolların sayısını hesaba katmadan şehir dizilimlerine göre saymış: dört şehir dizisinden üçü C’den geçiyor.','bilgi'),(e[2],'B ile C arasındaki yolu yalnız B’den C’ye doğru kullanılabilir sanmış; C’den B’ye geçen rotayı saymamış.','bilgi'),(e[3],'C yerine B şehrinden geçen rotaların oranını hesaplamış.','dikkat')],
 istenen='Seçilen rotanın C şehrinden geçme olasılığı.',ip=['A’dan E’ye hangi şehir dizilimleriyle gidilebileceğini yaz; her dizilimin kaç farklı yolla yapılabileceğine ayrıca bak.'],bilgi=[CAR],sekil=SK,
 ad=[A('Şehir dizilimlerini yaz','Hiçbir şehre ikinci kez uğramadan A’dan E’ye dört dizilim vardır.','A–B–D–E, A–C–D–E, A–B–C–D–E ve A–C–B–D–E'),A('Her dizilimin rota sayısını bul','Ardışık yolların sayıları çarpılır.','2×2×3 = 12 · 3×2×3 = 18 · 2×1×2×3 = 12 · 3×1×2×3 = 18'),A('Toplam ve uygun rotaları say','Tüm rotalar toplanır; C’den geçen üç dizilim toplanır.','12 + 18 + 12 + 18 = 60 · 18 + 12 + 18 = 48'),A('Olasılığı yaz','Uygun rotalar tüm rotalara oranlanır.','48/60 = 4/5')],
 puf='Çift yönlü yolların iki yönde de kullanılabildiğini her dizilimde yeniden kontrol et.')

# ================= 10 zor · metro, ayrık dakikalar =================
M1=[8,28,48]; M2=[14,30,52]; TOP=60
uygun=lambda L:{s_ for s_ in range(TOP) if any(s_<=t<=s_+4 for t in L)}
U1,U2=uygun(M1),uygun(M2); U=U1|U2
v=Fr(len(U),TOP); assert len(U)==26 and v==Fr(13,30)
assert sorted(U)==sorted(set(range(4,9))|set(range(10,15))|set(range(24,31))|set(range(44,53)))
ayri=lambda t:set(range(t-4,t+1))
pen=[ayri(t) for t in M1+M2]
e_say=sum(len(x) for x in pen); assert e_say==30                                   # örtüşenleri iki kez saymış
e_yalniz=sum(len(x) for x in pen if all(not(x&y) for y in pen if y is not x))     # örtüşenleri hiç saymamış
p1=Fr(len(U1),TOP); p2=Fr(len(U2),TOP); e_bag=p1+p2-p1*p2                          # bağımsız olay formülü
e_ilk=Fr(e_say-len(ayri(26)&ayri(28)) if False else e_say-3,TOP)                  # yalnız ilk örtüşmeyi düzeltmiş
assert len(ayri(28)&ayri(30))==3
e=[Fr(e_yalniz,TOP),e_bag,Fr(e_say,TOP),e_ilk]
assert e==[Fr(1,6),Fr(7,16),Fr(1,2),Fr(9,20)] and len({v,*e})==5
sc=0.14; o=[]
o.append(f'\\draw[thick] (0,0) -- ({TOP*sc:.2f},0);')
for t in range(0,TOP+1,10): o.append(f'\\draw[thick] ({t*sc:.2f},-0.07) -- ({t*sc:.2f},0.07); \\node[below=2pt,font=\\footnotesize] at ({t*sc:.2f},0) {{{t}}};')
o.append(f'\\node[font=\\small,anchor=west] at ({TOP*sc+0.2:.2f},0) {{dakika}};')
for row,(ad_,L) in enumerate((('M1',M1),('M2',M2))):
    y=0.9+row*1.0
    o.append(f'\\draw[gray!60] (0,{y}) -- ({TOP*sc:.2f},{y}); \\node[font=\\small\\bfseries,anchor=east] at (-0.15,{y}) {{{ad_}}};')
    for t in L: o.append(f'\\draw[gray!60,dotted] ({t*sc:.2f},0.07) -- ({t*sc:.2f},{y}); \\filldraw[fill=vurgu!60,draw=black] ({t*sc:.2f},{y}) circle (0.1); \\node[above=3pt,font=\\small] at ({t*sc:.2f},{y}) {{{t}}};')
SK=fig('\n'.join(o))
SAY=B('Ayrık eş olasılıklı sonuçlar','sonuçlar tek tek sayılabilen eş olasılıklı değerlerse olasılık, uygun sonuç sayısının tüm sonuç sayısına oranıdır; birden çok koşula uyan bir sonuç yalnız bir kez sayılır. Örnek: 0’dan 29’a kadar 30 tam sayıdan 5’e bölünenler 6 tanedir, olasılık 6/30 = 1/5’tir')
q('0010',tipId='osc-zaman',tip='Zaman şeridinde olasılık',z='zor',alt='Metro Sefer Çizelgesi',kaz='İki hattın sefer dakikalarının gösterildiği şeritte her trene binilebilen geliş dakikalarını sayıp ortak dakikaları bir kez sayarak olasılığı hesaplar.',kalip='hikâyeli',
 kart='K-OSC-06 (sefer dakikaları) · iki hat; 5 dakikalık uygun geliş kümeleri; örtüşmeler',
 metin='Bir metro istasyonuna M1 ve M2 hatlarının trenleri uğramaktadır. Şekilde, bir saatlik bir dilimde bu hatların trenlerinin istasyona varış dakikaları gösterilmiştir. Bir yolcu, bu dilimin 0, 1, 2, …, 59. dakikalarından birinde eş olasılıkla istasyona gelmektedir; geldiği dakikada ya da izleyen 4 dakikadan birinde (hangi hattın olduğu fark etmez) bir tren varıyorsa o trene binmektedir.\nBuna göre yolcunun bu dilimde bir trene binme olasılığı kaçtır?',
 dogru=v,yan=[(e[0],'Yalnız diğer geliş dakikalarıyla ortak elemanı olmayan iki trenin uygun dakikalarını saymış; ortak dakikası olanları hiç hesaba katmamış.','dikkat'),(e[1],'İki hattı bağımsız iki olay sanıp P(M1) + P(M2) − P(M1) × P(M2) formülünü uygulamış.','bilgi'),(e[2],'Altı trenin uygun geliş dakikalarını 5’er 5’er toplamış; ortak dakikaları iki kez saymış.','dikkat'),(e[3],'Ortak dakikası olan iki tren çiftinden yalnızca ilkinin ortak dakikalarını çıkarmış, ikincisini yine iki kez saymış.','bilgi')],
 istenen='Yolcunun bu dilimde bir trene binme olasılığı.',ip=['Her trenin varış dakikası için yolcunun hangi geliş dakikalarında o trene binebileceğini düşün.'],bilgi=[SAY],sekil=SK,
 ad=[A('Uygun dakikaları yaz','Bir t dakikasındaki tren için geliş dakikaları t − 4, …, t olur.','M1: 4–8, 24–28, 44–48 · M2: 10–14, 26–30, 48–52'),A('Ortak dakikaları birleştir','24–28 ile 26–30, 44–48 ile 48–52 kümeleri birleştirilir.','24–30 ve 44–52'),A('Dakikaları say','Birleşik kümelerin eleman sayıları toplanır.','5 + 5 + 7 + 9 = 26'),A('Olasılığı yaz','Uygun dakika sayısı 60’a oranlanır.','26/60 = 13/30')],
 puf='Aynı geliş dakikası birden çok trene uygunsa o dakikayı yalnız bir kez say.')

bitir(P,'olasisekb',UK)
