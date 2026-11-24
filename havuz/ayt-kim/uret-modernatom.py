"""Modern Atom Teorisi paketi için yardımcılar (kimya hesapları, şekil çizimi, öncüllü soru kurucu)."""
import sys,os,math
HV='/home/claude/zekacademy-app/havuz'
sys.path.insert(0,os.path.join(HV,'tyt-kim')); sys.path.insert(0,HV)
import _hafif_kim2 as H
from _hafif_kim2 import *
OUT=os.path.join(HV,'ayt-kim')
H.HD=OUT
KONU_='Modern Atom Teorisi'; UK='akim|Modern Atom Teorisi'
H.KONU=KONU_
P=Parti('modernatom',KONU_,UK,ders='AYT Kimya',idon='aytkim')
KY='ÖSYM AYT Kimya çıkmış soruları (yalnız mantık) · MEB 11. sınıf Modern Atom Teorisi'

SIRA=[(1,0),(2,0),(2,1),(3,0),(3,1),(4,0),(3,2),(4,1),(5,0),(4,2),(5,1)]
def alt(Z):
    c={}; k=Z
    for (n,l) in SIRA:
        t=min(2*(2*l+1),k)
        if t>0: c[(n,l)]=t
        k-=t
        if k==0: break
    assert k==0
    if Z==24: c={(1,0):2,(2,0):2,(2,1):6,(3,0):2,(3,1):6,(4,0):1,(3,2):5}
    if Z==29: c={(1,0):2,(2,0):2,(2,1):6,(3,0):2,(3,1):6,(4,0):1,(3,2):10}
    return c
def iyon(Z,yuk):
    c=dict(alt(Z))
    for _ in range(yuk):
        key=max(c,key=lambda t:(t[0],t[1])); c[key]-=1
        if c[key]==0: del c[key]
    return c
def elek(c):
    L=[]
    for (n,l),k in c.items():
        for j in range(k):
            if j<2*l+1: L.append((n,l,-l+j,0.5))
            else: L.append((n,l,-l+j-(2*l+1),-0.5))
    return L
def say(c,f): return sum(1 for e in elek(c) if f(*e))
def essiz(c): return sum(k if k<=2*l+1 else 2*(2*l+1)-k for (n,l),k in c.items())
def gecerli(n,l,ml,ms): return n>=1 and 0<=l<=n-1 and abs(ml)<=l and ms in (0.5,-0.5)
IE1={3:520,4:900,5:800,6:1090,7:1400,8:1310,9:1680,10:2080,11:496,12:738,13:578,14:787,15:1012,16:1000,17:1251,18:1521,19:419,20:590}
ATOMYARI={3:145,11:180,12:150,13:125,8:60,9:50,15:100,19:220,20:180,17:100}   # Slater atom yarıçapı (pm), yalnız eğilim denetimi
ARD={11:[496,4562,6910,9544],12:[738,1451,7733,10543],13:[578,1817,2745,11577],14:[787,1577,3232,4356,16091],15:[1012,1907,2914,4964,6274,21267]}

TIPAD={'kuantum':'Kuantum sayıları ve elektron sayımı','orbital':'Orbital şekli ve enerji sırası','dizilim':'Elektron dizilimi ve orbital diyagramı','iyon':'İyonların elektron dizilimi',
 'periyodik':'Periyodik özelliklerin karşılaştırılması','iegrafik':'Birinci iyonlaşma enerjisi grafikleri','ardisik':'Ardışık iyonlaşma enerjileri'}
TIP={}
def kt(n,alt_,fikir,tuzak,z,kalip,adim,tipad):
    kart(f'K-AKMA-{n}',alt_,fikir,tuzak,z,kalip,adim,f'ak-ma-{tipad}',TIPAD[tipad],KY); TIP[n]=(f'ak-ma-{tipad}',TIPAD[tipad])
RM='I II III'.split()
ORD=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
NAMES={'Yalnız I':{0},'Yalnız II':{1},'Yalnız III':{2},'I ve II':{0,1},'I ve III':{0,2},'II ve III':{1,2},'I, II ve III':{0,1,2}}
def kk(n,ne): return f'K-AKMA-{n} ({TIP[n][1].lower()}) · {ne}'
def q(no,n,ad,**k):
    assert len(k['ip'])==1 and 3<=len(ad)<=7
    mk(P,no,ad=ad,adim=len(ad),tipId=TIP[n][0],tip=TIP[n][1],kart=kk(n,k.pop('ne')),**k)
def sec(truth,p):
    c=[i for i,a in enumerate(ORD) if NAMES[a]==truth][0]
    assert p<=c<=p+2 or (c-p>=0 and c+(4-p)<=6),(truth,p)
    bas=c-p; assert bas>=0 and bas+4<=6
    return [ORD[i] for i in range(bas,bas+5)]
def onc(no,n,bag,stm,p,tail,ne,**k):
    truth={i for i,s in enumerate(stm) if s[1]}
    secenek=sec(truth,p); dogru=[a for a in secenek if NAMES[a]==truth][0]
    assert secenek.index(dogru)==p
    yan=[]
    for a in secenek:
        if a==dogru: continue
        S=NAMES[a]; parts=[]
        for i in sorted(S^truth):
            parts.append(f'{RM[i]}’{"i" if i<2 else "ü"} {"doğru" if i in S else "yanlış"} saymış; {stm[i][3]}')
        yan.append((a,' '.join(parts),'bilgi'))
    metin=bag+'\n'+'\n'.join(f'{RM[i]}. {s[0]}' for i,s in enumerate(stm))+'\n'+tail
    ad=[A(f'{RM[i]}. ifadeyi değerlendir',s[2],f'{RM[i]}: {"doğru" if s[1] else "yanlış"}') for i,s in enumerate(stm)]
    ad.append(A('Sonucu birleştir','Doğru bulunan ifadeler birlikte seçilir.',dogru))
    q(no,n,ad,ne=ne,metin=metin,dogru=dogru,sira=list(secenek),yan=yan,**k)
def yer(dogru,digerleri,p):
    assert len(digerleri)==4 and 0<=p<=4
    L=list(digerleri); L.insert(p,dogru); return L
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
ARR='-{Stealth[length=1.8mm,width=1.5mm]}'
def tk(g): return tikz_svg(HEAD+g+TAIL)

def kutular(satirlar,etiket_ust=True,satir_adlari=None,w=.62,aralik=.4,dy=1.15):
    g=''
    for r,satir in enumerate(satirlar):
        y=-r*dy; x=0
        if satir_adlari: g+=f'\\node[anchor=east] at (-.25,{y:.2f}) {{\\textbf{{{satir_adlari[r]}}}}};'
        for (ad,kut) in satir:
            for j,k in enumerate(kut):
                x0=x+j*w
                g+=f'\\draw[thick] ({x0:.2f},{y-.3:.2f}) rectangle ({x0+w:.2f},{y+.3:.2f});'
                cx=x0+w/2
                if k=='u': g+=f'\\draw[{ARR},thick] ({cx:.2f},{y-.22:.2f}) -- ({cx:.2f},{y+.22:.2f});'
                elif k=='ud':
                    g+=f'\\draw[{ARR},thick] ({cx-.12:.2f},{y-.22:.2f}) -- ({cx-.12:.2f},{y+.22:.2f});'
                    g+=f'\\draw[{ARR},thick] ({cx+.12:.2f},{y+.22:.2f}) -- ({cx+.12:.2f},{y-.22:.2f});'
                else: assert k==''
            if r==0 and etiket_ust: g+=f'\\node at ({x+len(kut)*w/2:.2f},{y+.58:.2f}) {{{ad}}};'
            x+=len(kut)*w+aralik
    return g
def eksen(W,Hh,ymax,ystep,ylab,xlab):
    g=f'\\draw[thick] (0,{Hh}) -- (0,0) -- ({W:.2f},0);'
    v=0
    while v<=ymax+1e-9:
        y=Hh*v/ymax
        g+=f'\\draw[gray!55,very thin] (0,{y:.3f}) -- ({W:.2f},{y:.3f}); \\draw (0,{y:.3f}) -- (-.08,{y:.3f}); \\node[anchor=east,font=\\footnotesize] at (-.1,{y:.3f}) {{{v}}};'
        v+=ystep
    g+=f'\\node[anchor=south,rotate=90,align=center] at (-1.5,{Hh/2:.2f}) {{{ylab}}};'
    g+=f'\\node[anchor=north] at ({W/2:.2f},-.85) {{{xlab}}};'
    return g
def cizgi_grafik(harfler,degerler,ymax,ystep,ylab,xlab,Hh=4.0,dx=.78):
    W=dx*(len(harfler)+.5); g=eksen(W,Hh,ymax,ystep,ylab,xlab)
    pts=[(dx*(i+.75),Hh*v/ymax) for i,v in enumerate(degerler)]
    g+='\\draw[vurgu,thick] '+' -- '.join(f'({x:.3f},{y:.3f})' for x,y in pts)+';'
    for (x,y),h in zip(pts,harfler):
        g+=f'\\fill[vurgu] ({x:.3f},{y:.3f}) circle (.075); \\node[anchor=north] at ({x:.3f},-.12) {{{h}}};'
        g+=f'\\draw[gray!55,dotted] ({x:.3f},0) -- ({x:.3f},{y:.3f});'
    return g
def cubuk_grafik(etiketler,degerler,ymax,ystep,ylab,xlab,Hh=4.0,dx=.9):
    W=dx*(len(etiketler)+.4); g=eksen(W,Hh,ymax,ystep,ylab,xlab)
    for i,(e,v) in enumerate(zip(etiketler,degerler)):
        x0=dx*(i+.3); h=Hh*v/ymax
        g+=f'\\draw[thick,fill=vurgu!30] ({x0:.3f},0) rectangle ({x0+dx*.6:.3f},{h:.3f});'
        g+=f'\\node[anchor=south,font=\\footnotesize] at ({x0+dx*.3:.3f},{h:.3f}) {{{v}}};'
        g+=f'\\node[anchor=north] at ({x0+dx*.3:.3f},-.1) {{{e}}};'
    return g
def kesit(satirlar,harfler,gruplar=('1A','2A','3A','4A','5A','6A','7A','8A'),cw=.85,ch=.8):
    g=''
    for j,gr in enumerate(gruplar): g+=f'\\node at ({(j+.5)*cw:.2f},.35) {{\\footnotesize {gr}}};'
    for i,p in enumerate(satirlar):
        y=-i*ch
        g+=f'\\node[anchor=east,font=\\footnotesize] at (-.1,{y-ch/2:.2f}) {{{p}. periyot}};'
        for j,gr in enumerate(gruplar):
            g+=f'\\draw[thick] ({j*cw:.2f},{y:.2f}) rectangle ({(j+1)*cw:.2f},{y-ch:.2f});'
            h=harfler.get((p,gr))
            if h: g+=f'\\node[font=\\large\\bfseries] at ({(j+.5)*cw:.2f},{y-ch/2:.2f}) {{{h}}};'
    return g

# ================= sorular =================
import sys,os

# ---------------- doğrulamalar (temel) ----------------
assert say(alt(26),lambda n,l,ml,ms:l==1)==12 and essiz(alt(26))==4 and alt(26)[(3,2)]==6
assert alt(25)[(3,2)]==5 and essiz(alt(25))==5 and essiz(iyon(25,2))==5 and iyon(25,2)[(3,2)]==5 and (4,0) not in iyon(25,2)
assert essiz(iyon(26,3))==5 and iyon(26,3)[(3,2)]==5
assert say(alt(17),lambda n,l,ml,ms:l==1)==11 and say(alt(17),lambda n,l,ml,ms:ml==0)==10 and say(alt(17),lambda n,l,ml,ms:l==0)==6 and say(alt(17),lambda n,l,ml,ms:n==3)==7 and essiz(alt(17))==1

# ---------------- kartlar ----------------
kt('01','Mümkün kuantum sayıları','n ≥ 1, l = 0…n−1, ml = −l…+l, ms = ±1/2 kuralları birlikte sınanır.','l ≤ n−1 koşulunu ya da ml’nin negatif değerlerini atlamak.','kolay','düz',2,'kuantum')
kt('02','Orbital şekilleri','s küreseldir (l = 0), p iki loblu (l = 1); aynı alt kabuktaki orbitaller aynı enerjili, ml değerleri farklıdır.','Aynı alt kabuktaki orbitallerin ml değerini aynı sanmak.','kolay','öncüllü',2,'orbital')
kt('03','Orbital enerji sırası','Çok elektronlu atomda enerji (n + l) ile artar; eşitlikte n büyük olan yüksektir.','Yalnız n’ye bakıp en büyük n’li orbitali en yüksek enerjili saymak.','kolay','düz',2,'orbital')
kt('04','Orbital diyagramı kuralları','Pauli ilkesi ve Hund kuralı birlikte sınanır; uyarılmış hâl kurallara aykırı değildir.','Uyarılmış hâli kurallara aykırı sanmak.','orta','öncüllü',3,'dizilim')
kt('05','Elektron dizilimi sayımı','Aufbau ile dizilim yazılır; l, ml ve eşleşmemiş elektron sayıları orbital orbital sayılır.','Alt kabukları saymada 2p ya da 3p’yi atlamak.','orta','öncüllü',3,'dizilim')
kt('06','Periyodik tablo kesiti','Aynı grupta yukarıdan aşağıya yarıçap artar; periyotta 1. iyonlaşma enerjisi genel olarak artar.','Grup ve periyot yönlerini karıştırmak.','orta','öncüllü',3,'periyodik')
kt('07','Birinci iyonlaşma enerjisi grafiği','2A > 3A ve 5A > 6A sapmaları: dolu ve yarı dolu alt kabukların kararlılığı.','Her ardışık elementte artış beklemek.','orta','grafik',3,'iegrafik')
kt('08','Dış katman dizilimi tablosu','Dış katman dizilimi grubu ve periyodu verir; iyonlaşma enerjisi sıralamasına sapmalar katılır.','Sıralamayı tek yönlü kurmak.','orta','tablo',3,'periyodik')
kt('09','İzoelektronik ve atom yarıçapı','Katman sayısı fazla olan tanecik büyüktür; elektron sayısı eşitse çekirdek yükü büyük olanın yarıçapı küçüktür.','Yarıçapı proton sayısıyla doğru orantılı sanmak.','orta','tablo',3,'periyodik')
kt('10','Atom için yargı sınaması','Verilen atom için s ve p sayıları, ml, n ve eşleşmemiş elektron değerleri tek tek sayılır.','Sayımda bir alt kabuğu atlamak.','orta','düz',3,'dizilim')
kt('11','Orbital diyagramından iyon','İyon oluşurken elektron önce en büyük n’li orbitalden gider; sonra eşleşmemiş sayılır.','İlk elektronu 3d’den vermek.','orta','şekilli',3,'iyon')
kt('12','Ardışık iyonlaşma enerjisi tablosu','Büyük sıçrama değerlik elektronları bittiğinde olur; aynı periyotta grup sırası atom numarasını belirler.','Sıçramayı yanlış basamağa koymak.','orta','öncüllü',3,'ardisik')
kt('13','ml ve n ile sayım','Verilen n ve ml için uygun l değerleri bulunur; her orbital en çok 2 elektron alır.','l = 0’ın yalnız ml = 0 verdiğini atlamak.','orta','düz',3,'kuantum')
kt('14','Katyon dizilimi yargıları','Katyonda önce 4s boşalır; eşleşmemiş elektron ve 4s doluluğu karşılaştırılır.','Önce 3d’den elektron vermek.','orta','öncüllü',3,'iyon')
kt('15','Son elektronun kuantum sayıları','Son elektronun kuantum sayılarından alt kabuktaki elektron sayısı ve atom bulunur; sonra spin sayımı yapılır.','Orbital doldurma sırasını (ml, ms) karıştırmak.','zor','düz',4,'kuantum')
kt('16','Ardışık iyonlaşma grafiği','Büyük sıçrama grup numarasını, periyot atom numarasını verir; sonra orbital sayımı yapılır.','Sıçramanın bir basamak önce ya da sonra olduğunu yanlış okumak.','zor','grafik',4,'ardisik')
kt('17','İzoelektronik iyonlar','l = 1 elektron sayısı iyon dizilimini belirler; iki iyon eşleştirilip periyodik özellikler yorumlanır.','Soy gaz dizilimini yanlış periyoda yerleştirmek.','zor','öncüllü',4,'iyon')
kt('18','Ardışık elementlerin 1. IE grafiği','Grafikteki sapmalar elementleri tanıtır; sonra dizilim ve özellik yargıları sınanır.','Grafik noktalarını yanlış elementlere eşlemek.','zor','grafik',4,'iegrafik')
kt('19','Atom yarıçapı grafiği','Yarıçaptaki ani artış yeni periyodu gösterir; elementler belirlenip l = 1 elektronları sayılır.','Yeni periyot sıçramasını elemente çevirememek.','zor','grafik',4,'periyodik')
kt('20','Kesit ve kuantum sayıları','Kesitten element bulunur; son elektronun n ve l değerleri, izoelektroniklik ve yarıçap birlikte değerlendirilir.','4. periyot s bloğunu 3d ile karıştırmak.','zor','öncüllü',4,'periyodik')
assert len(TIP)==20

def sg(ms): return '+1/2' if ms>0 else '−1/2'
def mls(m): return '0' if m==0 else (f'+{m}' if m>0 else f'−{abs(m)}')
def takim(n,l,ml,ms): return f'n = {n}, l = {l}, ml = {mls(ml)}, ms = {sg(ms)}'

# =============== 0001 · mümkün olmayan kuantum sayısı takımı · kolay · olumsuz ===============
T1=[(3,2,2,-.5),(2,1,-1,.5),(1,1,0,.5),(4,3,0,.5),(3,0,0,-.5)]
assert [gecerli(*t) for t in T1]==[True,True,False,True,True]
cel1={T1[0]:'ml = +2 değerini l = 2 için mümkün olmayan saymış; oysa l = 2 iken ml, −2’den +2’ye kadar tam sayı değerleri alır.',
 T1[1]:'ml’nin negatif değer alamayacağını düşünmüş; oysa ml, −l ile +l arasında negatif değerler de alır.',
 T1[3]:'n = 4 için l = 3’ü mümkün saymamış; oysa l, 0’dan n − 1’e kadar değer alır ve 3 = n − 1’dir.',
 T1[4]:'ms = −1/2 değerini mümkün olmayan saymış; oysa spin kuantum sayısı +1/2 ya da −1/2 olabilir.'}
yan=[(takim(*t),cel1[t],'bilgi') for t in [T1[0],T1[1],T1[3],T1[4]]]
q('0001','01',[A('Sınırları yaz','n tam sayıdır; l, 0’dan n − 1’e; ml, −l’den +l’ye kadar değer alır; ms yalnız +1/2 ya da −1/2’dir.','l: 0 … n−1 · ml: −l … +l · ms = ±1/2'),
  A('Takımları sına','Her takımda sırayla l, ml ve ms için sınırlar kontrol edilir.','(3, 2, +2, −1/2): geçerli · (2, 1, −1, +1/2): geçerli · (4, 3, 0, +1/2): geçerli · (3, 0, 0, −1/2): geçerli'),
  A('Uymayanı bul','l, en çok n − 1 olabilir; n = 1 iken yalnız l = 0 vardır.','n = 1, l = 1 → l ≤ n − 1 sağlanmaz')],
 ne='Bir elektron için mümkün olmayan kuantum sayısı takımı',z='kolay',alt='Kuantum Sayıları',kaz='n, l, ml ve ms sınırlarını kullanarak mümkün olmayan kuantum sayısı takımını belirler.',kalip='düz',
 metin='Bir atomdaki her elektron; baş kuantum sayısı (n), açısal momentum kuantum sayısı (l), manyetik kuantum sayısı (ml) ve spin kuantum sayısı (ms) olmak üzere dört kuantum sayısıyla tanımlanır. Aşağıda bir elektrona ait beş ayrı kuantum sayısı takımı verilmiştir.\nBuna göre, bu takımlardan hangisi bir elektron için mümkün değildir?',
 dogru=takim(*T1[2]),sira=yer(takim(*T1[2]),[takim(*T1[0]),takim(*T1[1]),takim(*T1[3]),takim(*T1[4])],1),yan=yan,istenen='Mümkün olmayan kuantum sayısı takımı.',
 ip=['Her kuantum sayısının alabileceği değer aralığı bir öncekine bağlıdır.'],
 bilgi=[B('Kuantum sayılarının sınırları','n = 5 iken l = 0, 1, 2, 3, 4 değerlerini alabilir; l = 2 iken ml = −2, −1, 0, +1, +2 olur; ms ise yalnız +1/2 ya da −1/2’dir')],
 puf='Önce n, sonra l, sonra ml sırasıyla sınırı kontrol et; her sayı bir öncekine bağlıdır.')

# =============== 0002 · orbital şekilleri · kolay · öncüllü + şekil ===============
g=''
g+='\\draw[fill=vurgu!25,thick] (0,0) circle (.75); \\node at (0,-1.2) {\\large\\bfseries X};'
g+='\\draw[fill=vurgu!25,thick] (3.1,.62) ellipse (.42 and .6); \\draw[fill=vurgu!25,thick] (3.1,-.62) ellipse (.42 and .6); \\fill (3.1,0) circle (.04); \\node at (3.1,-1.7) {\\large\\bfseries Y};'
g+='\\draw[fill=vurgu!25,thick] (5.62,0) ellipse (.6 and .42); \\draw[fill=vurgu!25,thick] (6.86,0) ellipse (.6 and .42); \\fill (6.24,0) circle (.04); \\node at (6.24,-1.2) {\\large\\bfseries Z};'
g+='\\draw[-{Stealth},thick] (7.9,-1.0) -- (7.9,.1) node[above] {$z$}; \\draw[-{Stealth},thick] (7.9,-1.0) -- (8.9,-1.0) node[right] {$x$};'
SK=tk(g)
onc('0002','02','Aynı enerji düzeyinde (n = 2) bulunan X, Y ve Z orbitallerinin şekilleri aşağıda gösterilmiştir.',
 [('X orbitalinin açısal momentum kuantum sayısı (l) 0’dır.',True,'Küresel orbital s orbitalidir ve l değeri 0’dır.','küresel orbitalin s türü olduğunu ve l değerinin 0 olduğunu bilmemiş.'),
  ('Y ve Z orbitalleri aynı alt kabuğa aittir.',True,'Y ve Z iki loblu p orbitalleridir; ikisi de aynı alt kabuğa aittir (n = 2, l = 1).','iki loblu orbitallerin ikisinin de p türü olduğunu görmemiş.'),
  ('Y ve Z orbitallerinin manyetik kuantum sayısı (ml) değerleri aynıdır.',False,'Aynı alt kabuktaki orbitallerin enerjisi eşittir ama ml değerleri farklıdır (−1, 0, +1).','aynı alt kabuktaki orbitallerin ml değerini aynı sanmış.')],
 1,'Buna göre, yukarıdaki ifadelerden hangileri doğrudur?',ne='X, Y, Z orbital şekilleri',z='kolay',alt='Orbitaller',kaz='Orbital şekillerinden l ve ml değerlerini yorumlar.',kalip='öncüllü',sekil=SK,
 ip=['Küresel ve iki loblu orbitallerin hangi alt kabuklara ait olduğunu düşün.'],
 bilgi=[B('Alt kabuk ve orbital','s alt kabuğunda 1, p alt kabuğunda 3 orbital vardır; aynı alt kabuktaki orbitallerin ml değerleri birbirinden farklıdır. Örnek: n = 3 için 3p orbitallerinin ml değerleri −1, 0 ve +1’dir')],
 puf='Şekil l’yi verir; aynı alt kabuktaki orbitaller aynı enerjili ama farklı ml’lidir.')

# =============== 0003 · enerjisi en yüksek orbital · kolay ===============
O3=[(2,1),(3,0),(3,2),(4,0),(3,1)]
assert max(O3,key=lambda t:(t[0]+t[1],t[0]))==(3,2) and sorted(t[0]+t[1] for t in O3)==[3,3,4,4,5]
oad=lambda t:f'n = {t[0]}, l = {t[1]}'
q('0003','03',[A('n + l değerini hesapla','Çok elektronlu atomda orbitalin enerjisi n + l değeriyle belirlenir; değer büyüdükçe enerji artar.','(2, 1): 3 · (3, 0): 3 · (3, 2): 5 · (4, 0): 4 · (3, 1): 4'),
  A('En büyüğü seç','En büyük n + l değerine sahip orbital en yüksek enerjilidir.','5 > 4 > 3'),
  A('Adı koy','l = 2 olan orbital d alt kabuğudur.','n = 3, l = 2 → 3d')],
 ne='Enerjisi en yüksek orbital',z='kolay',alt='Orbitaller',kaz='Orbitallerin enerjilerini (n + l) kuralıyla karşılaştırır.',kalip='düz',
 metin='Çok elektronlu bir atomda bazı orbitallerin baş kuantum sayısı (n) ve açısal momentum kuantum sayısı (l) değerleri aşağıdaki seçeneklerde verilmiştir.\nBuna göre, bu orbitallerden hangisinin enerjisi en yüksektir?',
 dogru=oad((3,2)),sira=yer(oad((3,2)),[oad((4,0)),oad((3,1)),oad((2,1)),oad((3,0))],0),
 yan=[(oad((4,0)),'En büyük n değerine bakıp 4s orbitalini en yüksek enerjili saymış; oysa 4s için n + l = 4’tür, 3d için bu değer 5’tir.','dikkat'),
      (oad((3,1)),'3p orbitalinin n + l değerini (4) hesaplayıp l = 2 olan orbitalle karşılaştırmamış; 3d için n + l = 5 olduğundan 3p daha düşük enerjilidir.','islem'),
      (oad((2,1)),'2p orbitalini seçmiş; oysa n + l = 3’tür ve bu değer listedeki en küçüklerden biridir.','bilgi'),
      (oad((3,0)),'Aynı n’li orbitallerde s’yi en yüksek sanmış; oysa 3s için n + l = 3’tür ve l büyüdükçe enerji artar.','bilgi')],
 istenen='Enerjisi en yüksek orbital.',ip=['Çok elektronlu atomda orbital enerjisini yalnız n belirlemez; l değerini de hesaba kat.'],
 bilgi=[B('Orbital enerji sırası','Çok elektronlu atomlarda enerji, n + l toplamı büyüdükçe artar; toplam eşitse n büyük olan daha yüksek enerjilidir. Örnek: n + l = 5 olan 4p, n + l = 4 olan 4s’den yüksek enerjilidir')],
 puf='Enerji sırası n + l ile belirlenir; yalnız n’ye bakmak yanıltır.')

# =============== 0004 · orbital diyagramları (Pauli ve Hund) · orta · öncüllü + şekil ===============
D1=[('1s',['ud']),('2s',['ud']),('2p',['u','u','u'])]
D2=[('1s',['ud']),('2s',['ud']),('2p',['ud','u',''])]
D3=[('1s',['ud']),('2s',['u']),('2p',['ud','u','u'])]
def topl(D): return sum({'u':1,'ud':2,'':0}[k] for _,ks in D for k in ks)
assert topl(D1)==topl(D2)==topl(D3)==7
SK=tk(kutular([D1,D2,D3],satir_adlari=['I','II','III'],w=.6,aralik=.45,dy=1.0))
onc('0004','04','Toplam 7 elektronu bulunan bir atomun 1s, 2s ve 2p orbitallerindeki elektron dağılımı için üç farklı diyagram çizilmiştir. Oklar elektronların spin yönlerini göstermektedir.',
 [('I numaralı diyagram, Pauli ilkesine ve Hund kuralına uygundur.',True,'2p orbitallerine elektronlar önce birer birer, aynı yönde yerleşmiştir; hiçbir orbitalde aynı yönlü iki elektron yoktur.','2p’deki tek tek yerleşmeyi hatalı saymış; elektronların önce eşleşerek dolması gerektiğini sanmış.'),
  ('II numaralı diyagram, Pauli ilkesine ve Hund kuralına uygundur.',False,'2p’de bir orbital boş kalmışken diğerinde elektronlar eşleşmiştir; bu durum Hund kuralına aykırıdır.','boş orbital varken elektronların eşleşmesini kurallara uygun saymış.'),
  ('III numaralı diyagram, Pauli ilkesine ve Hund kuralına uygundur.',True,'2s orbitalinde tek elektron, 2p’de dört elektron vardır; Pauli ve Hund’a aykırı değildir, yalnızca enerjisi daha yüksek (uyarılmış) bir dizilimdir.','2s yarı doluyken 2p’de elektron bulunmasını kurala aykırı sanmış; oysa bu yalnızca uyarılmış bir hâldir.')],
 3,'Buna göre, yukarıdaki ifadelerden hangileri doğrudur?',ne='üç orbital diyagramı',z='orta',alt='Elektron Dizilimi',kaz='Orbital diyagramlarını Pauli ilkesi ve Hund kuralı bakımından değerlendirir.',kalip='öncüllü',sekil=SK,
 ip=['Her diyagramda orbital başına elektron sayısına ve yönlerine ayrı ayrı bak.'],
 bilgi=[B('Pauli ilkesi ve Hund kuralı','Bir orbitalde en çok iki elektron bulunur ve bunların spinleri zıttır; aynı enerjili orbitallerde elektronlar önce birer birer yerleşir. Örnek: 3p⁴ diziliminde ilk üç elektron ayrı orbitallere, dördüncüsü eşleşerek girer')],
 puf='Pauli: orbitalde en çok 2 zıt yönlü elektron; Hund: boş orbital varken eşleşme olmaz. Uyarılmış hâl bu kurallara aykırı değildir.')

# =============== 0005 · 26Fe sayımı · orta · öncüllü ===============
f=alt(26)
onc('0005','05','Temel hâldeki 26Fe atomunun elektron dizilimi orbitallere yerleştirilerek elektronlar kuantum sayılarına göre sayılıyor.',
 [('3d orbitallerinde toplam 6 elektron vardır.',True,f'Dizilim 1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d⁶ biçimindedir; 3d alt kabuğunda {f[(3,2)]} elektron bulunur.','3d alt kabuğuna yerleşen elektron sayısını bulamamış.'),
  ('Eşleşmemiş elektron sayısı 6’dır.',False,'3d⁶’da beş orbitale birer elektron girdikten sonra altıncı elektron bir orbitalle eşleşir; eşleşmemiş elektron sayısı 4’tür.','3d⁶’daki 6 elektronun hepsini eşleşmemiş saymış.'),
  ('Açısal momentum kuantum sayısı (l) 1 olan toplam 12 elektron vardır.',True,'l = 1 olan elektronlar 2p⁶ ve 3p⁶’dır; toplam 12 elektron bulunur.','2p’deki 6 ve 3p’deki 6 elektronu birlikte saymayı atlamış.')],
 4,'Buna göre, yukarıdaki ifadelerden hangileri doğrudur?',ne='26Fe atomunda elektron sayımı',z='orta',alt='Elektron Dizilimi',kaz='Elektron dizilimini yazıp l ve eşleşmemiş elektron sayılarını belirler.',kalip='öncüllü',
 ip=['Önce dizilimi 4s ve 3d sırasına dikkat ederek yaz.'],
 bilgi=[B('Alt kabuk ve l','s için l = 0, p için l = 1, d için l = 2’dir. Örnek: 2p alt kabuğundaki 6 elektronun hepsi için l = 1’dir')],
 puf='Dizilimi yaz, alt kabukların l değerini yanına işaretle ve her alt kabuğu ayrı say.')
assert essiz(alt(26))==4

# =============== 0006 · periyodik tablo kesiti · orta · öncüllü + şekil ===============
SK=tk(kesit([2,3],{(2,'1A'):'T',(3,'1A'):'X',(3,'3A'):'Y',(3,'5A'):'Z'}))
assert ATOMYARI[11]>ATOMYARI[3] and IE1[15]>IE1[13] and say(alt(13),lambda n,l,ml,ms:l==1)==7
onc('0006','06','Periyodik tablonun 2. ve 3. periyotlarından alınan bir kesitte T, X, Y ve Z elementlerinin yerleri gösterilmiştir. (T, X, Y ve Z elementlerin gerçek sembolleri değildir.)',
 [('X atomunun yarıçapı T atomunun yarıçapından büyüktür.',True,'X ile T aynı grupta (1A) olup X daha alttadır; yukarıdan aşağıya katman sayısı arttığı için X’in yarıçapı büyüktür.','aynı grupta yukarıdan aşağıya yarıçapın arttığını unutmuş.'),
  ('Z atomunun birinci iyonlaşma enerjisi Y atomununkinden küçüktür.',False,'Aynı periyotta Y’den Z’ye gidildikçe çekirdek yükü artar; Z (5A) atomunun 1. iyonlaşma enerjisi Y (3A) atomununkinden büyüktür.','periyotta sağa gidildikçe çekirdek çekimi artmasına rağmen Z’nin değerini Y’den küçük saymış.'),
  ('Y atomunun temel hâlinde l = 1 olan toplam 7 elektron vardır.',True,'Y, 3A grubunda ve 3. periyottadır; dizilimi 1s² 2s² 2p⁶ 3s² 3p¹ olduğundan l = 1 olan 6 + 1 = 7 elektron bulunur.','yalnız 3p’deki 1 elektronu sayıp 2p’deki 6 elektronu atlamış.')],
 2,'Buna göre, yukarıdaki ifadelerden hangileri doğrudur?',ne='periyodik tablo kesiti',z='orta',alt='Periyodik Özellikler',kaz='Periyodik tablo kesitinden atom yarıçapı, iyonlaşma enerjisi ve l = 1 elektron sayısını yorumlar.',kalip='öncüllü',sekil=SK,
 ip=['Kesitten her elementin grup ve periyodunu bularak başla.'],
 bilgi=[B('Periyodik eğilimler','Aynı grupta yukarıdan aşağıya atom yarıçapı artar. Örnek: 2A grubunda Ca atomu, Mg atomundan büyüktür')],
 puf='Önce grup ve periyodu belirle; yarıçap ve iyonlaşma enerjisi bu konumdan, sayım dizilimden yapılır.')

# =============== 0007 · 2. periyot 1. IE grafiği · orta · grafik ===============
H7=list('KLMNRSTV'); V7=[IE1[z] for z in range(3,11)]
assert V7==[520,900,800,1090,1400,1310,1680,2080]
SK=tk(cizgi_grafik(H7,V7,2500,500,'1. iyonlaşma enerjisi\\\\(kJ/mol)','Atom numarası artan sırada elementler'))
S7=[('R’nin birinci iyonlaşma enerjisinin S’ninkinden büyük olması, R’nin 2p alt kabuğunun yarı dolu olmasıyla açıklanır.',True,''),
 ('K atomunun yarıçapı bu sekiz element içinde en küçüktür.',False,'K 1A grubundadır; aynı periyotta soldan sağa yarıçap azaldığından K’nin yarıçapı en büyüktür.'),
 ('L’nin birinci iyonlaşma enerjisinin M’ninkinden büyük olması, L’nin 2p alt kabuğunun yarı dolu olmasından kaynaklanır.',False,'L (2A) atomunun dizilimi 2s² ile biter; 2p alt kabuğu boştur. Yüksek değer, 2s alt kabuğunun tam dolu olmasıyla ilgilidir.'),
 ('N’nin birinci iyonlaşma enerjisi M’ninkinden küçüktür.',False,'Grafikte N’nin değeri M’ninkinden yüksektir; periyotta M’den N’ye geçerken çekirdek yükü artar.'),
 ('V atomu halojen (7A) grubundadır.',False,'Periyodun son elementi V, soy gazdır (8A); halojen olan T’dir.')]
assert IE1[7]>IE1[8] and IE1[4]>IE1[5] and IE1[6]>IE1[5]
dg=S7[0][0]
q('0007','07',[A('Elementleri tanı','Elementler 2. periyotta atom numarası artan sırada dizilmiştir: K 1A grubundan başlayıp V soy gaza uzanır.','K, L, M, N, R, S, T, V = 1A, 2A, 3A, 4A, 5A, 6A, 7A, 8A'),
  A('Sapmaları bul','Grafikte M ve S noktaları kendinden önceki elemente göre düşüştedir; bu sapmalar dolu ve yarı dolu alt kabukların kararlılığıyla ilgilidir.','M: 2p¹ (önceki L’de 2s² dolu) · S: 2p⁴ (önceki R’de 2p³ yarı dolu)'),
  A('Seçenekleri sına','Her seçenekteki grup, yarıçap ya da neden bu bilgilerle karşılaştırılır.','Yalnız R–S karşılaştırması ve nedeni doğrudur')],
 ne='Grafiğe göre doğru yargı',z='orta',alt='İyonlaşma Enerjisi',kaz='Birinci iyonlaşma enerjisi grafiğindeki sapmaları elektron dizilimiyle açıklar.',kalip='grafik',sekil=SK,
 metin='2. periyotta atom numaraları ardışık olan sekiz elementin birinci iyonlaşma enerjileri atom numarasına göre aşağıdaki grafikte gösterilmiştir. Elementler atom numarası artan sırada K, L, M, N, R, S, T ve V simgeleriyle belirtilmiştir.\nBuna göre aşağıdakilerden hangisi doğrudur?',
 dogru=dg,sira=yer(dg,[S7[1][0],S7[2][0],S7[3][0],S7[4][0]],3),
 yan=[(S7[i][0],S7[i][2],'bilgi' if i in (1,4) else 'dikkat') for i in (1,2,3,4)],istenen='Doğru yargı.',
 ip=['Grafikte kendinden öncekinden düşük kalan noktaların hangi elementlere ait olduğunu belirle.'],
 bilgi=[B('Yarı dolu ve dolu alt kabuk','Dolu ya da yarı dolu alt kabuklu atomlar kararlıdır. Örnek: 3. periyotta 2A grubunun (Mg) birinci iyonlaşma enerjisi 3A grubunun (Al) değerinden büyüktür')],
 puf='Düşüşler sapmadır: 2A > 3A ve 5A > 6A; nedeni dolu ya da yarı dolu alt kabuktur.')

# =============== 0008 · dış katman dizilimi tablosu · orta · tablo ===============
R8={'X':'2s²2p³','Y':'2s²2p⁴','Z':'3s²3p³','T':'3s²3p⁴'}; Zs={'X':7,'Y':8,'Z':15,'T':16}
assert sorted(Zs,key=lambda e:IE1[Zs[e]])==['T','Z','Y','X']
SK=tablo_svg(['Element','Son katman elektron dizilimi'],[[k,v] for k,v in R8.items()])
dog='T < Z < Y < X'
q('0008','08',[A('Konumları bul','Son katman dizilimlerinden grup ve periyot çıkar.','X: 5A, 2. periyot · Y: 6A, 2. periyot · Z: 5A, 3. periyot · T: 6A, 3. periyot'),
  A('Periyot ve sapma','Aynı gruptaki elementlerden üst periyottaki daha büyük iyonlaşma enerjilidir; 5A ve 6A arasında soldan sağa artış beklenirken sapma vardır.','X > Z; Y > T; 5A > 6A'),
  A('Sıralamayı kur','Her periyotta 5A elementi 6A elementinden büyüktür; ikinci periyot üçüncüden büyüktür.','T < Z < Y < X')],
 ne='X, Y, Z, T’nin 1. iyonlaşma enerjileri sıralaması',z='orta',alt='İyonlaşma Enerjisi',kaz='Dış katman dizilimlerinden grup ve periyodu bulup 1. iyonlaşma enerjilerini sıralar.',kalip='tablo',sekil=SK,
 metin='X, Y, Z ve T elementlerinin temel hâldeki son katman elektron dizilimleri aşağıdaki tabloda verilmiştir.\nBuna göre bu elementlerin birinci iyonlaşma enerjilerinin küçükten büyüğe doğru sıralanışı aşağıdakilerden hangisidir?',
 dogru=dog,sira=yer(dog,['Z < T < X < Y','Y < X < T < Z','Z < T < Y < X','T < Z < X < Y'],4),
 yan=[('Z < T < X < Y','Her periyotta soldan sağa artışı düzenli kabul edip 5A–6A sapmasını hesaba katmamış; sıralamayı Z < T ve X < Y kurmuş.','bilgi'),
      ('Y < X < T < Z','Sapmayı doğru uygulamış ama periyotta aşağı inildikçe iyonlaşma enerjisinin arttığını sanmış; 3. periyotu 2. periyottan büyük saymış.','bilgi'),
      ('Z < T < Y < X','5A–6A sapmasını yalnızca 2. periyotta uygulamış; 3. periyotta T’yi Z’den büyük saymış.','dikkat'),
      ('T < Z < X < Y','Sapmayı yalnızca 3. periyotta uygulamış; 2. periyotta Y’yi X’ten büyük saymış.','dikkat')],
 istenen='1. iyonlaşma enerjilerinin küçükten büyüğe sıralanışı.',ip=['Dizilimlerden grup ve periyodu bulduktan sonra her periyottaki ardışık gruplara ayrı ayrı bak.'],
 bilgi=[B('Grup ve periyodu bulma','Son katmanın baş kuantum sayısı periyodu, son katmandaki elektron sayısı A grubunu verir. Örnek: 3s²3p² dizilimi 3. periyot, 4A grubudur')],
 puf='Önce grup ve periyodu yaz; periyotta sağa gidildikçe artışı, 5A > 6A sapmasını ve aynı gruptaki üst periyodun büyüklüğünü birlikte uygula.')

# =============== 0009 · izoelektronik/atom yarıçapı tablosu · orta · tablo ===============
TB9={'X':(13,10),'Y':(8,10),'Z':(12,12),'T':(9,10)}
SK=tablo_svg(['Tanecik','Proton sayısı','Elektron sayısı'],[[k,str(p),str(e)] for k,(p,e) in TB9.items()])
dog='Z > Y > T > X'
# Z: Mg atomu (3 katman); Y: O²⁻, T: F⁻, X: Al³⁺ (2 katman, 10 elektron)
assert [k for k,v in TB9.items() if v[0]==v[1]]==['Z'] and sorted((k for k in 'XYT'),key=lambda k:-TB9[k][0])==['X','T','Y']
q('0009','09',[A('Taneciği tanı','Proton ve elektron sayısı eşitse atom, elektron fazlaysa anyon, eksikse katyondur.','Z: nötr atom (12 proton) · X: 3+ katyon · Y: 2− anyon · T: 1− anyon'),
  A('Katman sayısına bak','Z atomunun 12 elektronu 3 katmandadır; X, Y, T’nin 10 elektronu 2 katmandadır. Katman sayısı fazla olan büyüktür.','Z: 3 katman · X, Y, T: 2 katman'),
  A('İzoelektroniklerde sırala','Elektron sayısı eşit olan tanecikler arasında proton sayısı fazla olanın yarıçapı küçüktür.','Proton: Y 8 < T 9 < X 13 → yarıçap: Y > T > X'),
  A('Birleştir','Z en büyüktür; ardından Y, T ve X gelir.','Z > Y > T > X')],
 ne='X, Y, Z, T yarıçaplarının büyükten küçüğe sıralanışı',z='orta',alt='Periyodik Özellikler',kaz='Proton ve elektron sayısından tanecik türünü belirleyip yarıçapları karşılaştırır.',kalip='tablo',sekil=SK,
 metin='Bir atom ile üç farklı iyona ait proton ve elektron sayıları aşağıdaki tabloda verilmiştir. Tablodaki taneciklerden Z nötr bir atomdur; X, Y ve T ise iyonlardır.\nBuna göre bu taneciklerin yarıçaplarının büyükten küçüğe doğru sıralanışı aşağıdakilerden hangisidir?',
 dogru=dog,sira=yer(dog,['X > Z > T > Y','Z > X > T > Y','Y > T > X > Z','Y > T > Z > X'],4),
 yan=[('X > Z > T > Y','Yarıçapın proton sayısıyla arttığını sanıp taneciklerin proton sayısına göre sıralamış: X (13) > Z (12) > T (9) > Y (8).','bilgi'),
      ('Z > X > T > Y','Elektron sayısı fazla olan Z’yi en büyük bulmuş ama elektron sayısı eşit taneciklerde proton sayısı arttıkça yarıçap büyür sanmış: X > T > Y.','bilgi'),
      ('Y > T > X > Z','Elektron sayısı eşit taneciklerde sıralamayı doğru kurmuş; fakat elektron sayısı daha fazla olan Z’nin katman sayısını hesaba katmayıp en küçük bulmuş.','dikkat'),
      ('Y > T > Z > X','Yalnız proton sayısına bakıp proton sayısı arttıkça yarıçap küçülür sanmış: Y (8) > T (9) > Z (12) > X (13); katman sayısını hesaba katmamış.','bilgi')],
 istenen='Yarıçapların büyükten küçüğe sıralanışı.',ip=['Elektronların kaç katmanda bulunduğunu karşılaştırdıktan sonra aynı katman sayısındakileri ayrıca incele.'],
 bilgi=[B('Yarıçap karşılaştırması','Katman sayısı fazla olan tanecik daha büyüktür; elektron sayıları eşit olan taneciklerde proton sayısı fazla olanın yarıçapı daha küçüktür. Örnek: K⁺ ile Cl⁻ izoelektroniktir ve Cl⁻ daha büyüktür')],
 puf='Önce katman sayısına, katman sayısı eşitse proton sayısına bak: izoelektronikte çekirdek yükü büyüdükçe yarıçap küçülür.')

# =============== 0010 · 17Cl yargısı · orta · olumsuz ===============
C=alt(17)
sy=[('s orbitallerinde toplam 6 elektron vardır.',say(C,lambda n,l,ml,ms:l==0)==6,'Yalnız 1s ve 3s’yi saymış; 2s²’yi atlayıp 4 bulmuş. Oysa 1s², 2s² ve 3s² ile toplam 6 elektron vardır.'),
 ('Açısal momentum kuantum sayısı (l) 1 olan toplam 11 elektron vardır.',say(C,lambda n,l,ml,ms:l==1)==11,'2p⁶ ve 3p⁵’i birlikte saymayı atlamış; oysa l = 1 olan elektronlar 6 + 5 = 11’dir.'),
 ('Baş kuantum sayısı (n) 3 olan toplam 7 elektron vardır.',say(C,lambda n,l,ml,ms:n==3)==7,'3. katmandaki 3s² ve 3p⁵ elektronlarını birlikte saymayı atlamış; oysa 2 + 5 = 7 elektron vardır.'),
 ('Eşleşmemiş elektron sayısı 1’dir.',essiz(C)==1,'3p⁵’teki 5 elektronun hepsini eşleşmemiş sanmış; oysa bu alt kabukta iki orbital çiftli, biri tek elektronludur.'),
 ('Manyetik kuantum sayısı (ml) 0 olan toplam 9 elektron vardır.',say(C,lambda n,l,ml,ms:ml==0)==9,'')]
assert [s[1] for s in sy]==[True,True,True,True,False] and say(C,lambda n,l,ml,ms:ml==0)==10
q('0010','10',[A('Dizilimi yaz','17Cl atomunun elektron dizilimi orbitallere yerleştirilir.','1s² 2s² 2p⁶ 3s² 3p⁵'),
  A('Yargıları say','s, l = 1 ve n = 3 sayıları alt kabuklardan toplanır; eşleşmemiş elektron 3p’deki tek elektronludur.','s: 2 + 2 + 2 = 6 · l = 1: 6 + 5 = 11 · n = 3: 2 + 5 = 7 · eşleşmemiş: 1'),
  A('ml = 0 sayısını bul','Verilen sıraya göre 3p⁵’te ml = −1 ve ml = 0 orbitalleri çifttir, ml = +1 orbitalinde tek elektron vardır; ml = 0 orbitali doludur.','1s: 2 · 2s: 2 · 2p(ml=0): 2 · 3s: 2 · 3p(ml=0): 2 → 10'),
  A('Yanlışı seç','ml = 0 için verilen 9 değeri hesapla uyuşmaz.','Yanlış: ml = 0 olan 9 elektron')],
 ne='17Cl atomu için yanlış yargı',z='orta',alt='Elektron Dizilimi',kaz='Elektron dizilimi üzerinden s, l, n, ml ve eşleşmemiş elektron sayılarını değerlendirir.',kalip='düz',
 metin='Atom numarası 17 olan klor (Cl) atomunun temel hâldeki elektron dizilimi orbital orbital yazılıp elektronlar kuantum sayılarına göre sayılıyor. Bir p alt kabuğunda elektronlar orbitallere ml = −1, 0, +1 sırasıyla yerleşmektedir (önce birer birer, sonra eşleşerek).\nBuna göre bu atomla ilgili aşağıdakilerden hangisi yanlıştır?',
 dogru=sy[4][0],sira=yer(sy[4][0],[s[0] for s in sy[:4]],0),yan=[(s[0],s[2],'islem' if i<3 else 'bilgi') for i,s in enumerate(sy[:4])],istenen='Yanlış olan yargı.',
 ip=['Yargıları tek tek ele alıp her sayıyı dizilimdeki alt kabuklardan yeniden hesapla.'],
 bilgi=[B('ml ile sayım','Her alt kabukta ml = 0 değerine sahip tek bir orbital vardır ve bu orbital dolu ise 2 elektron içerir. Örnek: 2p⁶ alt kabuğunda ml = 0 olan 2 elektron bulunur')],
 puf='Dizilimi yaz ve her sayıyı alt kabuklar üzerinden tek tek topla; kök olumsuz olduğu için yanlışı seç.')

# =============== 0011 · orbital diyagramından iyon · orta · şekil ===============
def un_atom(): return essiz(alt(26))
c3_ilk3d=dict(alt(26)); c3_ilk3d[(3,2)]-=3
c_et=essiz(iyon(26,3)); assert c_et==5
SK=tk(kutular([[('4s',['ud']),('3d',['ud','u','u','u','u'])]],w=.62,aralik=.6))
D11=[(3,'Elektronları önce 3d’den vermiş (3d³ 4s²); oysa katyonda elektron önce en büyük n’li 4s orbitalinden alınır.','bilgi'),
     (4,'Nötr atomun eşleşmemiş elektron sayısını bulmuş; yükü hesaba katmamış.','dikkat'),
     (6,'3d orbitallerindeki elektron sayısını (6) eşleşmemiş elektron sayısı sanmış.','bilgi'),
     (1,'3d’deki tek elektronlu üç orbitalden elektron verip (↑↓ ↑ kalır) 4s²’yi korumuş; bu durumda 1 eşleşmemiş elektron bulmuş.','bilgi')]
assert 6-3-2*0>=0 and essiz(c3_ilk3d)==3 and un_atom()==4
q('0011','11',[A('Atomun dizilimini oku','Diyagramda 4s² 3d⁶ dizilimi görülür; daha içteki orbitaller tam doludur.','4s²: ↑↓ · 3d⁶: ↑↓ ↑ ↑ ↑ ↑'),
  A('3 elektron ver','X³⁺ iyonunda elektronlar önce en büyük n’li 4s orbitalinden, sonra 3d’den çıkar.','4s² → 0 · 3d⁶ → 3d⁵'),
  A('Eşleşmemişleri say','3d⁵’te beş orbitalin her birinde bir elektron vardır.','Eşleşmemiş elektron: 5')],
 ne='X³⁺ iyonunun eşleşmemiş elektron sayısı',z='orta',alt='İyonların Elektron Dizilimi',kaz='Orbital diyagramından katyonun dizilimini bulup eşleşmemiş elektron sayısını hesaplar.',kalip='şekilli',sekil=SK,
 metin='Temel hâldeki bir X atomunun 4s ve 3d orbitallerindeki elektron dağılımı şekilde verilmiştir. X atomunun daha içteki bütün orbitalleri tam doludur.\nBuna göre, X³⁺ iyonunda kaç tane elektron eşleşmemiş durumdadır?',
 dogru=5,yan=[(a,b,c) for a,b,c in D11[:2]]+[(D11[2][0],D11[2][1],D11[2][2]),(D11[3][0],D11[3][1],D11[3][2])],istenen='X³⁺ iyonundaki eşleşmemiş elektron sayısı.',
 ip=['Katyon oluşurken elektronların hangi orbitalden gittiğini belirle.'],
 bilgi=[B('Katyon dizilimi','Katyon oluşurken elektronlar önce baş kuantum sayısı en büyük olan orbitalden verilir. Örnek: Ti atomu (4s² 3d²) Ti²⁺ olurken elektronlarını 4s orbitalinden verir')],
 puf='Katyonda önce 4s boşalır; sonra 3d’deki tek elektronlu orbitalleri say.')

# =============== 0012 · ardışık iyonlaşma enerjisi tablosu · orta · öncüllü ===============
TB12=[['X']+ARD[11],['Y']+ARD[12],['Z']+ARD[13]]
SK=tablo_svg(['Element','1. IE','2. IE','3. IE','4. IE'],[[r[0]]+[str(x) for x in r[1:5]] for r in TB12])
assert [ARD[z][1]/ARD[z][0]>5 for z in (11,12,13)]==[True,False,False] and ARD[12][2]/ARD[12][1]>5 and ARD[13][3]/ARD[13][2]>3
onc('0012','12','3. periyotta bulunan X, Y ve Z elementlerinin ilk dört iyonlaşma enerjisi (kJ/mol) aşağıdaki tabloda verilmiştir.',
 [('X atomunun değerlik elektron sayısı 2’dir.',False,'X’te 1. ve 2. iyonlaşma enerjisi arasında büyük sıçrama vardır; yani yalnız 1 elektron kolay koparılır ve X’in değerlik elektron sayısı 1’dir.','X’teki büyük sıçramayı 1. ile 2. enerji arasında görmeyip değerlik elektron sayısını 2 bulmuş.'),
  ('Y atomunun temel hâlinde 3s orbitalinde 2 elektron bulunur.',True,'Y’de büyük sıçrama 2. ile 3. enerji arasındadır; değerlik elektron sayısı 2’dir ve 3. periyotta 3s² ile biter.','Y’deki sıçramanın 2. ile 3. enerji arasında olduğunu görmeyip 3s²’yi doğrulayamamış.'),
  ('Z atomunun atom numarası X atomununkinden küçüktür.',False,'Aynı periyotta grup numarası büyüdükçe atom numarası da büyür; Z’nin sıçraması 3. ile 4. enerji arasında olduğundan 3A grubundadır ve X’ten büyüktür.','sıçrama basamağını grup numarasıyla ilişkilendirmeyip Z’yi X’in solunda saymış.')],
 0,'Buna göre, yukarıdaki ifadelerden hangileri doğrudur?',ne='X, Y, Z ardışık iyonlaşma enerjileri',z='orta',alt='İyonlaşma Enerjisi',kaz='Ardışık iyonlaşma enerjisi sıçramalarından değerlik elektronunu ve grubu belirler.',kalip='öncüllü',sekil=SK,
 ip=['Her satırda değerin birden çok kat arttığı basamağı bul.'],
 bilgi=[B('Ardışık iyonlaşma enerjileri','Değerlik elektronları koparıldıktan sonra bir iç katmandan elektron koparmak gerektiğinden iyonlaşma enerjisi büyük bir sıçrama yapar. Örnek: Değerlik elektron sayısı 4 olan bir atomda sıçrama 4. ile 5. enerji arasında olur')],
 puf='Büyük sıçramadan önceki basamak sayısı değerlik elektron sayısı, yani A grubunun numarasıdır.')

# =============== 0013 · n = 3, ml = −1 · orta ===============
n3=[(3,l,-1) for l in range(0,3) if abs(-1)<=l]
assert n3==[(3,1,-1),(3,2,-1)] and 2*len(n3)==4
q('0013','13',[A('l değerlerini bul','n = 3 için l = 0, 1, 2’dir.','3s, 3p, 3d'),
  A('ml = −1 olanları seç','ml, −l ile +l arasında olduğundan ml = −1 için l en az 1 olmalıdır; l = 0’da yalnız ml = 0 vardır.','l = 1: ml = −1 var · l = 2: ml = −1 var · l = 0: yok'),
  A('Elektron sayısını bul','İki orbitalin her biri en çok 2 elektron alır.','2 orbital × 2 = 4')],
 ne='n = 3 ve ml = −1 olan elektronların en fazla sayısı',z='orta',alt='Kuantum Sayıları',kaz='n ve ml değerinden uygun orbitalleri bulup en fazla elektron sayısını hesaplar.',kalip='düz',
 metin='Bir atomda elektronların kuantum sayıları, her orbital en çok iki elektron alacak şekilde tanımlanmaktadır.\nBuna göre, baş kuantum sayısı (n) 3 ve manyetik kuantum sayısı (ml) −1 olan en çok kaç elektron bulunabilir?',
 dogru=4,yan=[(2,'Yalnız bir orbitali (3p ya da 3d) sayıp l = 1 ve l = 2 orbitallerinin ikisinin de ml = −1 verdiğini görmemiş.','dikkat'),(6,'3p alt kabuğunun üç orbitalini de saymış; oysa ml = −1 yalnız bir 3p orbitalinde bulunur.','dikkat'),
  (8,'3s ve 3p alt kabuklarını (2 + 6) birlikte sayıp ml koşulunu atlamış.','bilgi'),(10,'3d alt kabuğundaki beş orbitalin hepsini (5 × 2) saymış; ml = −1 yalnız bir 3d orbitalinde vardır.','dikkat')],istenen='En çok elektron sayısı.',
 ip=['Hangi alt kabuklarda ml = −1 değerinin bulunabileceğini l değerine bakarak ele.'],
 bilgi=[B('Alt kabuktaki orbital sayısı','Alt kabukta 2l + 1 orbital bulunur ve ml değerleri −l’den +l’ye uzanır. Örnek: n = 2 için 2s’de ml = 0, 2p’de ml = −1, 0, +1 olabilir')],
 puf='ml = −1 en az l = 1 ister; uygun her alt kabuktan yalnız bir orbital sayılır.')

# =============== 0014 · Mn ve Mn²⁺ · orta · öncüllü ===============
M=alt(25); M2=iyon(25,2)
assert M[(3,2)]==5 and (4,0) in M and (4,0) not in M2 and essiz(M)==essiz(M2)==5
onc('0014','14','Atom numarası 25 olan mangan (Mn) atomu ile Mn²⁺ iyonunun temel hâldeki elektron dizilimleri yazılıyor.',
 [('Mn atomunun 3d orbitallerinde toplam 7 elektron vardır.',False,'Mn atomunun dizilimi 4s² 3d⁵ biçimindedir; 3d alt kabuğunda 5 elektron bulunur.','4s²’den sonra kalan elektron sayısını yanlış hesaplayıp 3d’ye 7 elektron yerleştirmiş.'),
  ('Mn²⁺ iyonunun 4s orbitalinde 2 elektron bulunur.',False,'Katyonda elektronlar önce 4s orbitalinden verilir; Mn²⁺ iyonunda 4s orbitali boştur (3d⁵).','2+ yükü için elektronları 3d’den alıp 4s²’yi korumuş.'),
  ('Mn²⁺ iyonu ile Mn atomunun eşleşmemiş elektron sayıları eşittir.',True,'Her ikisinde de 3d⁵ yarı doludur ve 5 eşleşmemiş elektron bulunur; 4s² eşleşmiş elektronlardır.','Mn²⁺’nın 3d⁵ yarı dolu olduğunu görmeyip eşleşmemiş elektron sayısının değiştiğini sanmış.')],
 2,'Buna göre, yukarıdaki ifadelerden hangileri doğrudur?',ne='Mn atomu ve Mn²⁺ iyonu',z='orta',alt='İyonların Elektron Dizilimi',kaz='Atom ve katyon dizilimlerini karşılaştırıp eşleşmemiş elektron sayısını değerlendirir.',kalip='öncüllü',
 ip=['Önce her iki taneciğin dizilimini yaz; elektronların hangi alt kabuktan koptuğuna dikkat et.'],
 bilgi=[B('Eşleşmemiş elektron','Yarı dolu alt kabukta her orbitalde bir elektron bulunur ve eşleşmemiş sayısı orbital sayısına eşittir. Örnek: 2p³ diziliminde 3 eşleşmemiş elektron vardır')],
 puf='Katyonda önce 4s boşalır; 3d’deki elektron sayısı iyon oluşunca değişmeyebilir.')

# =============== 0015 · son elektronun kuantum sayıları · zor ===============
def son(Z): return elek(alt(Z))[-1]
cl=alt(17); s_=alt(16); ar=alt(18)
assert (3,1,0,-.5)==son(17) and say(cl,lambda n,l,ml,ms:ms<0)==8 and say(s_,lambda n,l,ml,ms:ms<0)==7 and say(ar,lambda n,l,ml,ms:ms<0)==9
assert [Z for Z in range(1,37) if son(Z)==(3,1,0,-.5)]==[17]
iciA=alt(17); icin=sum(1 for (n,l,ml,ms) in elek(iciA) if not (n==3 and l==1) and ms<0)
assert icin==6
q('0015','15',[A('Son elektronun yerini bul','3p alt kabuğunda elektronlar önce ml = −1, 0, +1 sırasıyla ms = +1/2 ile, sonra aynı sırayla ms = −1/2 ile yerleşir.','3p¹: (−1, +1/2) · 3p²: (0, +1/2) · 3p³: (+1, +1/2) · 3p⁴: (−1, −1/2) · 3p⁵: (0, −1/2)'),
  A('Atomu belirle','Son elektron 3p⁵ olduğundan dizilim 1s² 2s² 2p⁶ 3s² 3p⁵’tir.','Atom numarası 2 + 2 + 6 + 2 + 5 = 17'),
  A('ms = −1/2 olanları say','Her dolu orbitaldeki ikinci elektron ms = −1/2’dir; 3p⁵’te iki orbital doludur.','1s: 1 · 2s: 1 · 2p: 3 · 3s: 1 · 3p: 2'),
  A('Toplamı yaz','Orbital başına 1 elektronlar toplanır.','1 + 1 + 3 + 1 + 2 = 8')],
 ne='ms = −1/2 olan elektron sayısı',z='zor',alt='Kuantum Sayıları',kaz='Son elektronun kuantum sayılarından atomu bulup ms değerine göre elektron sayar.',kalip='düz',
 metin='Temel hâldeki bir atomda enerjisi en yüksek olan son elektronun kuantum sayıları n = 3, l = 1, ml = 0 ve ms = −1/2’dir. Aynı alt kabukta elektronlar orbitallere önce ml = −1, 0, +1 sırasıyla ms = +1/2 olacak biçimde, sonra aynı sırayla ms = −1/2 olacak biçimde yerleşmektedir.\nBuna göre, bu atomda ms = −1/2 olan toplam kaç elektron vardır?',
 dogru=8,yan=[(6,'3p alt kabuğundaki ms = −1/2 elektronlarını saymayı atlayıp yalnız 1s, 2s, 2p ve 3s’deki 6 elektronu saymış.','dikkat'),
  (7,'Son elektronu 3p⁴ (ml = −1) sanıp atomu S saymış; S atomunda ms = −1/2 olan 7 elektron vardır.','bilgi'),
  (9,'Son elektronu 3p⁶ sanıp atomu Ar saymış; Ar atomunda ms = −1/2 olan 9 elektron vardır.','bilgi'),
  (17,'Atomu doğru bulmuş ama istenen ms = −1/2 elektronlarını değil, atomun toplam elektron sayısını yazmış.','dikkat')],istenen='ms = −1/2 olan elektron sayısı.',
 ip=['Önce son elektronun alt kabuktaki sırasını bularak atomun kaç elektronlu olduğunu belirle.'],
 bilgi=[B('Alt kabuk doldurma sırası','Aynı alt kabukta elektronlar önce her orbitale birer birer (aynı spinle) yerleşir, sonra eşleşir. Örnek: 2p⁴ diziliminde dördüncü elektron ilk orbitale ikinci elektron olarak girer')],
 puf='Son elektronun (ml, ms) değeri, alt kabuğun kaçıncı elektronu olduğunu verir; atomu bulduktan sonra spinleri orbital orbital say.')

# =============== 0016 · ardışık iyonlaşma grafiği · zor ===============
V16=[1000,1900,2900,5000,6300,21300]
assert [round(x,-2) for x in ARD[15]]==[1000,1900,2900,5000,6300,21300]
SK=tk(cubuk_grafik(['1.','2.','3.','4.','5.','6.'],V16,25000,5000,'İyonlaşma enerjisi\\\\(kJ/mol)','Koparılan elektronun sırası',dx=.95))
Z16=15; atomsay=lambda Z:say(alt(Z),lambda n,l,ml,ms:l==1)
assert essiz(alt(15))==3 and essiz(alt(13))==1 and essiz(alt(14))==2 and atomsay(15)==9 and atomsay(13)==7 and atomsay(14)==8 and atomsay(16)==10 and sum(k for (n,l),k in alt(15).items() if (n,l)==(3,1))==3
q('0016','16',[A('Sıçramayı oku','İyonlaşma enerjisi 5. ile 6. elektron arasında birden çok kat artmıştır.','1.–5. enerjiler ≈ 1000–6300 · 6. enerji ≈ 21300'),
  A('Grubu ve atomu bul','5 değerlik elektronu olan 3. periyot elementi 5A grubundadır.','3s² 3p³ → 2 + 8 + 5 = 15'),
  A('Dizilimi yaz','Atom numarası 15 olan atomun dizilimi yazılır.','1s² 2s² 2p⁶ 3s² 3p³'),
  A('Eşleşmemişleri say','Hund kuralına göre 3p³’te üç orbitalin her birinde bir elektron vardır; diğer alt kabuklar tam doludur.','3p³ → 3 eşleşmemiş elektron')],
 ne='X’in eşleşmemiş elektron sayısı',z='zor',alt='İyonlaşma Enerjisi',kaz='Ardışık iyonlaşma enerjisi grafiğinden atomu belirleyip eşleşmemiş elektron sayısını bulur.',kalip='grafik',sekil=SK,
 metin='3. periyotta bulunan X atomunun ardışık iyonlaşma enerjileri (kJ/mol) aşağıdaki grafikte gösterilmiştir.\nBuna göre, X atomunun temel hâlinde kaç elektron eşleşmemiş durumdadır?',
 dogru=3,yan=[(1,'Sıçramayı 3. ile 4. elektron arasında okuyup X’i 3A grubunda (3p¹) saymış; bu durumda 1 eşleşmemiş elektron bulmuş.','bilgi'),
  (2,'Sıçramayı 4. ile 5. elektron arasında okuyup X’i 4A grubunda (3p²) saymış; bu durumda 2 eşleşmemiş elektron bulmuş.','bilgi'),
  (5,'Değerlik elektronlarının (3s² 3p³) hepsini eşleşmemiş saymış; oysa 3s² eşleşmiş elektronlardır.','dikkat'),(6,'Grafikteki 6 çubuğu eşleşmemiş elektron sayısı sanmış.','dikkat')],istenen='Eşleşmemiş elektron sayısı.',
 ip=['Çubukların büyüklüğündeki ani değişimin hangi sıradaki elektronla başladığını bul.'],
 bilgi=[B('Sıçrama ve grup','İç katmandan elektron koparmak gerektiğinde iyonlaşma enerjisi birden çok kat artar; sıçramadan önceki elektron sayısı A grubu numarasını verir. Örnek: Sıçrama 2. ile 3. elektron arasında ise atom 2A grubundadır')],
 puf='Sıçramadan önceki basamak sayısı grubu, periyot atom numarasını verir; sonra dizilimden eşleşmemiş elektronları say.')

# =============== 0017 · izoelektronik iyonlar · zor · öncüllü ===============
Xi=iyon(20,2); Yi=dict(alt(16)); Yi[(3,1)]+=2
assert sum(Xi.values())==sum(Yi.values())==18 and Xi==Yi and say(Xi,lambda n,l,ml,ms:l==1)==12
assert [Z for Z in range(3,37) if iyon(Z,2) in [alt(g) for g in (2,10,18,36)] and say(iyon(Z,2),lambda n,l,ml,ms:l==1)==12]==[20]
assert sum(k for (n,l),k in alt(20).items() if l==0)==8 and sum(k for (n,l),k in alt(20).items() if l==0)!=6
onc('0017','17','X²⁺ ve Y²⁻ iyonları izoelektroniktir. X²⁺ iyonu soy gaz elektron dizilimine sahiptir ve bu iyonda açısal momentum kuantum sayısı (l) 1 olan toplam 12 elektron bulunmaktadır.',
 [('X’in atom numarası Y’ninkinden 4 fazladır.',True,'12 elektron 2p⁶ ve 3p⁶’dır; X²⁺ 18 elektronludur, X 20 elektronlu atomdur. Y²⁻ da 18 elektronlu olduğundan Y 16 elektronludur; fark 4’tür.','iyon yüklerini ters işleyip X’in atom numarasını 16, Y’ninkini 20 bulmuş ve farkı −4 saymış.'),
  ('X atomunun elektron diziliminde s orbitallerinde toplam 8 elektron vardır.',True,'X (Z = 20) dizilimi 1s² 2s² 2p⁶ 3s² 3p⁶ 4s²’dir; s orbitallerinde 2 + 2 + 2 + 2 = 8 elektron bulunur.','4s² elektronlarını saymayı unutup s orbitallerinde yalnız 6 elektron bulmuş.'),
  ('Y atomunun yarıçapı X atomunun yarıçapından büyüktür.',False,'Y (S) 3. periyotta, X (Ca) 4. periyottadır; katman sayısı fazla olan X’in yarıçapı daha büyüktür.','anyonun atomdan büyük olmasını atoma uygulayıp Y atomunun yarıçapını büyük saymış.')],
 1,'Buna göre, yukarıdaki ifadelerden hangileri doğrudur?',ne='X²⁺ ve Y²⁻ izoelektronik iyonları',z='zor',alt='İyonların Elektron Dizilimi',kaz='l = 1 elektron sayısından iyon dizilimini bulup atomların özelliklerini karşılaştırır.',kalip='öncüllü',
 ip=['l = 1 olan elektronların hangi alt kabuklarda bulunduğunu düşünerek iyonun toplam elektron sayısına ulaş.'],
 bilgi=[B('İzoelektronik iyonlar','Elektron sayıları eşit olan taneciklere izoelektronik denir; katyonun atom numarası elektron sayısından yükü kadar fazla, anyonun ise yükü kadar azdır. Örnek: Mg²⁺ ve O²⁻ izoelektroniktir, ikisi de 10 elektronludur')],
 puf='İzoelektronik taneciklerde elektron sayıları eşittir; atom numarası iyon yüküne göre değişir.')

# =============== 0018 · ardışık beş elementin 1. IE grafiği · zor · grafik ===============
H18=['X','Y','Z','T','R']; V18=[500,740,580,790,1010]
assert [IE1[z] for z in range(11,16)]==[496,738,578,787,1012]
SK=tk(cizgi_grafik(H18,V18,1200,200,'1. iyonlaşma enerjisi\\\\(kJ/mol)','Atom numarası artan sırada elementler',dx=.95))
S18=['Y’nin birinci iyonlaşma enerjisi Z’ninkinden büyüktür; X’in ikinci iyonlaşma enerjisi ise Y’ninkinden büyüktür.',
 'T atomunun 3p orbitallerinde 3 eşleşmemiş elektron vardır; R atomunun yarıçapı T atomununkinden küçüktür.','R atomunun atom yarıçapı T atomununkinden büyüktür; Z atomunun 3p alt kabuğunda 1 elektron vardır.',
 'X’in ikinci iyonlaşma enerjisi Y’ninkinden küçüktür; Y’nin birinci iyonlaşma enerjisi Z’ninkinden büyüktür.','Y’nin birinci iyonlaşma enerjisi Z’ninkinden küçüktür; X’in ikinci iyonlaşma enerjisi Y’ninkinden büyüktür.']
assert essiz({(3,1):2})==2 and essiz({(3,1):3})==3 and ARD[11][1]>ARD[12][1] and ATOMYARI.get(15,100)<110
q('0018','18',[A('Elementleri belirle','X, 3. periyot 1A grubunda olduğundan ardışık beş element Na, Mg, Al, Si, P’dir.','X: 1A · Y: 2A · Z: 3A · T: 4A · R: 5A'),
  A('Grafikteki sapmayı bul','Y’den Z’ye değer düşer; Y’de 3s tam dolu, Z’de 3p’de tek elektron vardır.','3s² (Y) · 3s² 3p¹ (Z)'),
  A('Seçenekleri sına','Her seçeneğin iki parçası ayrı sınanır: eşleşmemiş sayısı, yarıçap eğilimi ve X⁺’nın soy gaz dizilimi nedeniyle ikinci iyonlaşma enerjisi.','T: 3p² → 2 eşleşmemiş; yarıçap: R < T; X’in 2. IE’si büyük'),
  A('Doğruyu seç','İki parçası da doğru olan tek seçenek birincisidir.','1. IE: Y > Z · 2. IE: X > Y')],
 ne='Grafiğe göre doğru yargı',z='zor',alt='İyonlaşma Enerjisi',kaz='Birinci iyonlaşma enerjisi grafiğinden elementleri belirleyip dizilim ve periyodik özellik yargılarını değerlendirir.',kalip='grafik',sekil=SK,
 metin='Atom numaraları ardışık olan beş elementin birinci iyonlaşma enerjileri atom numarasına göre aşağıdaki grafikte gösterilmiştir. Elementler atom numarası artan sırada X, Y, Z, T ve R ile simgelenmiştir. X elementi 3. periyotta ve 1A grubundadır.\nBuna göre aşağıdakilerden hangisi doğrudur?',
 dogru=S18[0],sira=yer(S18[0],[S18[1],S18[2],S18[3],S18[4]],0),
 yan=[(S18[1],'T’yi 5A grubunun elementi sanıp 3p’de 3 eşleşmemiş elektron bulmuş; T 4A grubundadır ve 3p²’de 2 eşleşmemiş elektron vardır.','bilgi'),
      (S18[2],'Periyotta soldan sağa atom yarıçapının arttığını sanmış; oysa çekirdek yükü arttığı için R’nin yarıçapı T’ninkinden küçüktür.','bilgi'),
      (S18[3],'X’in birinci iyonlaşma enerjisinin küçük olmasından ikinci enerjisinin de küçük olacağını sanmış; X⁺ soy gaz dizilimindedir ve ikinci elektron çok zor koparılır.','dikkat'),
      (S18[4],'Grafikte Y’nin değerini Z’ninkinden küçük okumuş; oysa Y’den Z’ye değer düşer, yani Y’nin birinci iyonlaşma enerjisi daha büyüktür.','dikkat')],istenen='Doğru yargı.',
 ip=['Grafikteki ilk elementten başlayarak noktaları sırayla elementlerle eşleştir.'],
 bilgi=[B('Ardışık elementleri tanıma','Atom numaraları ardışık elementler aynı periyotta soldan sağa dizilir; ilk elementin grubu bilindiğinde diğerleri de bellidir. Örnek: 2. periyotta 1A elementinden başlayarak 2A, 3A, 4A… diye gidilir')],
 puf='Önce noktaları elementlerle eşle; sonra düşüşün (Y→Z) nedenini alt kabuk doluluğuyla ilişkilendir.')

# =============== 0019 · atom yarıçapı grafiği · zor ===============
V19=[60,50,180,150,125]
assert [ATOMYARI[z] for z in (8,9,11,12,13)]==V19
SK=tk(cubuk_grafik(list('KLMNR'),V19,200,50,'Atom yarıçapı\\\\(pm)','Atom numarası artan sırada elementler',dx=1.0))
lp=lambda Z:say(alt(Z),lambda n,l,ml,ms:l==1)
assert lp(8)==4 and lp(13)==7 and lp(12)==6 and lp(7)==3 and lp(9)==5 and lp(14)==8
dg=4+7
assert dg==11 and lp(7)+lp(12)==9 and 4+lp(12)==10 and lp(9)+lp(13)==12
U=lambda Z:essiz(alt(Z))
assert U(8)==2 and U(11)==1 and U(13)==1 and U(8)+U(11)+U(13)==4 and U(8)+U(11)==3 and U(7)+U(11)+U(13)==5 and U(8)==2 and U(12)==0
q('0019','19',[A('Yeni periyodu bul','Yarıçap L’den M’ye ani bir artış gösterir; bu artış yeni periyodun başlangıcıdır ve M, 1A grubundadır.','M: 3. periyot 1A (Na)'),
  A('Elementleri eşle','Soy gaz atlandığı için L, 2. periyodun son elementidir (7A); K da 6A grubudur. N ve R de M’yi izler.','K = O; L = F; M = Na; N = Mg; R = Al'),
  A('Eşleşmemişleri say','K: 2p⁴ → 2 · M: 3s¹ → 1 · R: 3p¹ → 1','2 + 1 + 1'),
  A('Topla','Üç sayı toplanır.','2 + 1 + 1 = 4')],
 ne='K, M ve R atomlarındaki eşleşmemiş elektron sayıları toplamı',z='zor',alt='Periyodik Özellikler',kaz='Atom yarıçapı grafiğinden elementleri belirleyip eşleşmemiş elektron sayılarını toplar.',kalip='grafik',sekil=SK,
 metin='Atom numarası artan sırada K, L, M, N ve R elementlerinin atom yarıçapları aşağıdaki grafikte gösterilmiştir. Elementler birbirini izleyen elementlerdir; yalnız aradaki soy gaz atomu grafikte yer almamaktadır. K elementi 2. periyottadır.\nBuna göre, K, M ve R atomlarının temel hâldeki elektron dizilimlerindeki eşleşmemiş elektron sayıları toplamı kaçtır?',
 dogru=4,yan=[(1,'Yalnız M atomunun eşleşmemiş elektronunu (3s¹) sayıp K ve R’yi hesaba katmamış.','dikkat'),(2,'Yalnız K atomunun 2 eşleşmemiş elektronunu sayıp M ve R’yi atlamış.','dikkat'),
  (3,'R atomunu hesaba katmayıp yalnız K (2) ve M (1) için 2 + 1 = 3 bulmuş.','dikkat'),(5,'K’yi N sanıp 2p³ ile 3 eşleşmemiş elektron almış: 3 + 1 + 1 = 5 bulmuş.','bilgi')],istenen='Eşleşmemiş elektron sayıları toplamı.',
 ip=['Yarıçaptaki ani artışın hangi iki element arasında olduğunu belirle.'],
 bilgi=[B('Yarıçap ve periyot','Periyotta soldan sağa atom yarıçapı azalır; yeni bir periyoda geçilirken katman sayısı arttığı için yarıçap birden büyür. Örnek: 1A grubundaki bir atomun yarıçapı, bir önceki periyodun 7A atomundan çok büyüktür')],
 puf='Yarıçaptaki ani artış yeni periyodun 1A elementini gösterir; oradan geriye ve ileriye elementleri sırala.')

# =============== 0020 · periyodik kesit + kuantum sayıları · zor · öncüllü ===============
SK=tk(kesit([3,4],{(3,'2A'):'X',(3,'7A'):'Y',(4,'1A'):'Z',(4,'2A'):'T'}))
assert son(19)[:2]==(4,0)
y1=iyon(17,-1) if False else None
Ycl=dict(alt(17)); Ycl[(3,1)]+=1; assert Ycl==iyon(20,2)
assert IE1[19]<IE1[20] and say(alt(19),lambda n,l,ml,ms:True)==19
onc('0020','20','Periyodik tablonun 3. ve 4. periyotlarından alınan bir kesitte X, Y, Z ve T elementlerinin yerleri gösterilmiştir. (X, Y, Z ve T elementlerin gerçek sembolleri değildir.)',
 [('Z atomunun en yüksek enerjili elektronunun baş ve açısal momentum kuantum sayıları sırasıyla 3 ve 2’dir.',False,'Z, 4. periyot 1A elementidir; son elektronu 4s orbitalinde olup n = 4 ve l = 0’dır.','Z’nin son elektronunu 3d orbitaline yerleştirmiş; oysa 4s orbitali 3d’den önce dolar.'),
  ('Y⁻ iyonu ile T²⁺ iyonunun elektron dizilimleri aynıdır.',True,'Y (3. periyot 7A) Y⁻ olunca 18 elektronlu olur; T (4. periyot 2A) T²⁺ olunca 18 elektronlu olur; ikisi de 1s² 2s² 2p⁶ 3s² 3p⁶ dizilimindedir.','Y⁻ ve T²⁺ iyonlarının her ikisinin de 18 elektronlu olduğunu hesaplamamış.'),
  ('Z atomunun birinci iyonlaşma enerjisi T atomununkinden küçük, ikinci iyonlaşma enerjisi ise T atomununkinden büyüktür.',True,'Z (4s¹) ilk elektronunu T’ye (4s²) göre daha kolay verir; ancak Z⁺ iyonu soy gaz dizilimindedir ve ikinci elektron çok zor koparılır, T⁺ ise 4s¹ ile bir elektron daha kolay verir.','Z⁺’nın soy gaz dizilimine sahip olduğunu görmeyip ikinci iyonlaşma enerjisini T’ninkinden küçük sanmış.')],
 4,'Buna göre, yukarıdaki ifadelerden hangileri doğrudur?',ne='3. ve 4. periyot kesiti',z='zor',alt='Periyodik Özellikler',kaz='Periyodik tablo kesitinden elementleri belirleyip kuantum sayıları, iyon dizilimi ve yarıçap yargılarını değerlendirir.',kalip='öncüllü',sekil=SK,
 ip=['Kesitten her elementin atom numarasını bulduktan sonra yargıları tek tek sına.'],
 bilgi=[B('4. periyot başı','4. periyotta 4s alt kabuğu 3d’den önce dolar; 1A ve 2A elementlerinin son elektronları 4s’de bulunur. Örnek: 2. periyotta son elektronlar 2s’de, 3. periyotta 3s’dedir')],
 puf='Kesitten atom numarasını bul; iyonlarda elektron sayısını eşitleyerek izoelektroniği, grup ve periyotla yarıçapı değerlendir.')

bitir(P,'modernatom',UK)
import json as _j
_k=os.path.join(HV,'kartlar','modernatom.json'); _d=_j.load(open(_k)); _d['not_']='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT Kimya çıkmış soruları, MEB 11. sınıf Modern Atom Teorisi kazanımları.'
_j.dump(_d,open(os.path.join(HV,'kartlar','akmodernatom.json'),'w'),ensure_ascii=False,indent=1); os.remove(_k)
