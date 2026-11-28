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
P=Parti('modernatomiki',KONU_,UK,ders='AYT Kimya',idon='aytkim')
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

TIPAD={'model':'Bohr ve modern atom modeli','kuantum':'Kuantum sayıları ve orbitaller','dizilim':'Elektron dizilimi ve istisnalar','iyon':'İyonların orbital diyagramı','periyodik':'Periyodik özellikler ve elektron sayımı'}
TIP={}
def kt(n,alt_,fikir,tuzak,z,kalip,adim,tipad):
    kart(f'K-AKMA2-{n}',alt_,fikir,tuzak,z,kalip,adim,f'ak-ma2-{tipad}',TIPAD[tipad],KY); TIP[n]=(f'ak-ma2-{tipad}',TIPAD[tipad])
RM='I II III'.split()
ORD=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
NAMES={'Yalnız I':{0},'Yalnız II':{1},'Yalnız III':{2},'I ve II':{0,1},'I ve III':{0,2},'II ve III':{1,2},'I, II ve III':{0,1,2}}
def kk(n,ne): return f'K-AKMA2-{n} ({TIP[n][1].lower()}) · {ne}'
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
            parts.append(f'{["I’i","II’yi","III’ü"][i]} {"doğru" if i in S else "yanlış"} saymış; {stm[i][3]}')
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

def sg(ms): return '+1/2' if ms>0 else '−1/2'
def mls(m): return '0' if m==0 else (f'+{m}' if m>0 else f'−{abs(m)}')
def takim(n,l,ml,ms): return f'n = {n}, l = {l}, ml = {mls(ml)}, ms = {sg(ms)}'

# ---------------- kartlar ----------------
kt('01','Bohr ve modern atom modeli','İki modelin elektronu tanımlama biçimi ve açıkladıkları olgular ayrı ayrı karşılaştırılır; yörünge ile orbital ayrı kavramlardır.','Yörünge ile orbitali eş anlamlı saymak.','kolay','öncüllü',4,'model')
kt('02','Orbital diyagramından kuantum sayıları','Kutunun yeri ml, okun yönü ms, alt kabuğun adı n ve l değerlerini verir.','Okun yönü ile ml sırasını karıştırmak.','kolay','şekilli',3,'kuantum')
kt('03','Cr atomunda dizilim istisnası','Yarı dolu alt kabuk kararlılığı nedeniyle 4s ve 3d dolum sırası değişir; sayımlar bu dizilime göre yapılır.','Dizilimi 4s² 3d⁴ yazıp sayımları ona göre yapmak.','orta','düz',4,'dizilim')
kt('04','Bohr modelinde enerji düzeyi geçişleri','Geçişte alınan ya da verilen enerji, iki düzeyin enerjileri farkının mutlak değeridir; düzeyler arası farklar eşit değildir.','Enerjiyi n farkıyla orantılı sanmak.','orta','şekilli',3,'model')
kt('05','Anyon orbital diyagramından atom','Anyonun son orbital diyagramından elektron sayısı, buradan atom numarası ve izoelektronik taneciklerle karşılaştırma yapılır.','Anyonun elektron sayısını atomun elektron sayısı sanmak.','orta','öncüllü',4,'iyon')
kt('06','Kuantum sayıları tablosu','Üç sayı aynıysa elektronlar aynı orbitaldedir; iki sayı aynıysa aynı alt kabuktadır; enerji n + l ile belirlenir.','Yalnız n eşitliğini aynı alt kabuk saymak.','orta','tablo',3,'kuantum')
kt('07','Eşleşmemiş elektron grafiği','Grafikteki değer deseninden elementler bulunur; sonra l ve ml sayımı dizilim üzerinden yapılır.','Aynı değerli iki çubuğu birbirine karıştırmak.','orta','grafik',4,'periyodik')
kt('08','Katyon diyagramından atoma dönüş','İyonun diyagramından atomun dizilimi kurulur; sonra ml sayımı alt kabuk alt kabuk yapılır.','Atomun 4s elektronlarını sayıma katmamak.','zor','şekilli',4,'iyon')
kt('09','İstisnalı dizilimlerde iyonlar','İstisnalı ve istisnasız dizilimli atomların iyonları karşılaştırılır; elektronun hangi alt kabuktan ayrıldığı iyon dizilimini belirler.','İyon dizilimini atomun dizilimiyle karıştırmak.','zor','öncüllü',4,'dizilim')
kt('10','Kesit, ml sayımı ve izoelektronik iyonlar','Kesitten elementler bulunur; ml ve eşleşmemiş elektron sayımı ile izoelektronik iyon yarıçapı birlikte değerlendirilir.','İzoelektronik iyonlarda yarıçapı proton sayısıyla orantılı sanmak.','zor','öncüllü',4,'periyodik')
assert len(TIP)==10

def son(Z): return elek(alt(Z))[-1]
def kn(z,f): return say(alt(z),f)
L0=lambda n,l,ml,ms:l==0
L1=lambda n,l,ml,ms:l==1
M0=lambda n,l,ml,ms:ml==0

# =============== 0001 · Bohr / modern atom modeli · kolay · öncüllü + şekil ===============
g='\\draw[thick] (0,0) circle (.55); \\draw[thick] (0,0) circle (1.0); \\fill (0,0) circle (.09); \\fill[vurgu] (.55,0) circle (.08); \\fill[vurgu] (-.71,.71) circle (.08); \\node at (0,-1.5) {\\textbf{Bohr modeli}};'
g+='\\fill[vurgu!12] (4.4,0) circle (1.1); \\fill[vurgu!25] (4.4,0) circle (.78); \\fill[vurgu!45] (4.4,0) circle (.44); \\fill (4.4,0) circle (.09); \\node at (4.4,-1.5) {\\textbf{Modern atom modeli}};'
SK=tk(g)
onc('0001','01','Aşağıda bir atomun Bohr modeli ile modern atom modeline (kuantum mekaniksel model) göre gösterimleri verilmiştir.',
 [('Bohr modelinde elektronun enerjisi, bulunduğu yörüngeye bağlı olarak belirli değerler alır.',True,'Bohr modelinde elektron yalnız belirli enerjili yörüngelerde bulunabilir; enerji kesiklidir.','Bohr modelinde elektron yalnız belirli enerjili yörüngelerde bulunabilir ve enerjisi kesiklidir.'),
  ('Modern atom teorisine göre orbital, elektronun bulunma olasılığının yüksek olduğu bölgedir.',True,'Orbital, elektronun çekirdek çevresinde bulunma olasılığının yüksek olduğu üç boyutlu bölgedir.','Orbital, elektronun bulunma olasılığının yüksek olduğu bölgeyi tanımlar.'),
  ('Modern atom teorisine göre bir elektronun hem konumu hem de hızı aynı anda kesin olarak belirlenebilir.',False,'Belirsizlik ilkesine göre konum ve hız aynı anda kesin belirlenemez; yalnız bulunma olasılığı verilebilir.','Belirsizlik ilkesine göre konum ve hız aynı anda kesin olarak belirlenemez.')],
 1,'Buna göre, yukarıdaki ifadelerden hangileri doğrudur?',ne='Bohr ve modern atom modeli',z='kolay',alt='Atom Modelleri',kaz='Bohr atom modeli ile modern atom teorisini elektronun tanımlanma biçimi bakımından karşılaştırır.',kalip='öncüllü',sekil=SK,
 ip=['Her ifadeyi hangi modelin ilkelerine dayandığına bakarak ayrı ayrı sına.'],
 bilgi=[B('Atom modelleri','Bohr modeli hidrojen atomunun çizgi spektrumunu açıklamak için ileri sürülmüştür. Modern atom teorisi ise elektronun hem dalga hem tanecik özelliği taşıdığını esas alır. Örnek: de Broglie hareket eden her parçacığa bir dalga boyu karşılık geldiğini önermiştir')],
 puf='Önce her modelin elektronu nasıl tanımladığını düşün, sonra ifadeleri bu ölçüyle sına.')

# =============== 0002 · orbital diyagramı → kuantum sayıları · kolay · şekil ===============
D2=['ud','ud','u','u','u']
g=kutular([[('3d',D2)]],w=.7,aralik=.4)
j2=3; assert D2[j2]=='u'
g+=f'\\node[font=\\large\\bfseries] at ({j2*.7+.35:.2f},-.7) {{X}}; \\draw[vurgu,thick,{ARR}] ({j2*.7+.35:.2f},-.5) -- ({j2*.7+.35:.2f},-.33);'
SK=tk(g)
n2,l2,ml2,ms2=3,2,-2+j2,.5
assert gecerli(n2,l2,ml2,ms2) and ml2==1
O2=[(n2,l2,ml2,ms2),(n2,l2,ml2,-.5),(n2,l2,-ml2,ms2),(n2,1,ml2,ms2),(n2,l2,ml2+1,ms2)]
assert len(set(O2))==5 and all(isinstance(x,tuple) for x in O2)
cl2=['ms değerinin işaretini ters almış; yukarı yönlü ok ms = +1/2’ye karşılık gelir.','ml sıralamasını sağdan sola okumuş; kutular soldan sağa ml = −2’den +2’ye artar, 4. kutu ml = +1’dir.','3d alt kabuğu için l değerini 1 almış; l = 1 p alt kabuğuna aittir, d alt kabuğunda l = 2’dir.','ml değerlerini −2 yerine −1’den başlatmış; 4. kutu +2 değil +1’dir.']
q('0002','02',[A('Alt kabuğu oku','Etiket 3d olduğundan n = 3 ve d alt kabuğu için l = 2’dir.','n = 3, l = 2'),
  A('ml değerini bul','Kutular soldan sağa ml = −2, −1, 0, +1, +2’dir; X, 4. kutudadır.','ml = +1'),
  A('ms değerini bul','X’in oku yukarı yönlüdür; yukarı ok ms = +1/2 demektir.','ms = +1/2')],
 ne='Orbital diyagramı ve kuantum sayıları',z='kolay',alt='Orbital Diyagramı',kaz='Orbital diyagramında işaretli elektronun dört kuantum sayısını belirler.',kalip='şekilli',
 metin='Temel hâldeki bir atomun 3d orbitallerinin elektron dağılımı şekilde gösterilmiştir. Kutular soldan sağa ml = −2, −1, 0, +1, +2 sırasındadır; yukarı yönlü ok ms = +1/2, aşağı yönlü ok ms = −1/2 değerini göstermektedir.\nBuna göre, X ile gösterilen elektronun kuantum sayıları aşağıdakilerden hangisidir?',
 sekil=SK,dogru=takim(*O2[0]),sira=yer(takim(*O2[0]),[takim(*O2[1]),takim(*O2[2]),takim(*O2[3]),takim(*O2[4])],0),
 yan=[(takim(*O2[1]),cl2[0],'bilgi'),(takim(*O2[2]),cl2[1],'dikkat'),(takim(*O2[3]),cl2[2],'bilgi'),(takim(*O2[4]),cl2[3],'dikkat')],istenen='X elektronunun kuantum sayıları.',
 ip=['Önce alt kabuğun adından n ve l’yi, sonra kutunun yerinden ml’yi belirle.'],
 bilgi=[B('Orbital diyagramı','Her kutu bir orbitali, her ok bir elektronu gösterir. Kutunun alt kabuk içindeki sırası ml değerini, okun yönü ms değerini verir. Örnek: p alt kabuğunun üç kutusu soldan sağa ml = −1, 0, +1 sırasındadır')],
 puf='Etiketten n ve l, kutunun yerinden ml, okun yönünden ms değerini oku.')

# =============== 0003 · Cr istisnası · orta · düz ===============
cfg=alt(24); cfg0=dict(cfg); cfg0[(4,0)]=2; cfg0[(3,2)]=4
SP=lambda n,l,ml,ms:ms>0; N3=lambda n,l,ml,ms:n==3; N4=lambda n,l,ml,ms:n==4
sp,n3=say(cfg,SP),say(cfg,N3); assert (sp,n3,essiz(cfg))==(15,13,6) and sp+n3==28
assert (say(cfg0,SP),say(cfg0,N3),say(cfg0,SP)+say(cfg0,N3))==(14,12,26) and (24-essiz(cfg))//2==9 and 9+n3==22 and 24//2+n3==25
q('0003','03',[A('Dizilimi yaz','Cr atomunda yarı dolu 3d kararlılığı nedeniyle bir 4s elektronu 3d’ye geçer.','1s² 2s² 2p⁶ 3s² 3p⁶ 4s¹ 3d⁵'),
  A('ms = +1/2 olanları say','6 eşleşmemiş elektronun hepsi +1/2’dir; geri kalan 18 elektron 9 çift oluşturur ve her çiftten biri +1/2’dir.','6 + 9 = 15'),
  A('n = 3 olanları say','3. enerji düzeyinde 3s², 3p⁶ ve 3d⁵ bulunur.','2 + 6 + 5 = 13'),
  A('Topla','İki sayı toplanır.','15 + 13 = 28')],
 ne='Cr atomunda istisnalı dizilim',z='orta',alt='Elektron Dizilimi İstisnaları',kaz='Krom atomunun istisnalı dizilimine göre ms ve n kuantum sayılarına göre elektron sayımı yapar.',kalip='düz',
 metin='Atom numarası 24 olan krom (Cr) atomunun temel hâl elektron dizilimi, aynı alt kabuktaki orbitallerin yarı dolu olmasının kararlılık sağlaması nedeniyle Aufbau sırasından farklıdır. (Eşleşmemiş elektronların hepsinin spini ms = +1/2 kabul edilecektir.)\nBuna göre, Cr atomunda spin kuantum sayısı (ms) +1/2 olan elektronların sayısı ile baş kuantum sayısı (n) 3 olan elektronların sayısının toplamı kaçtır?',
 dogru=28,yan=[(26,'Dizilimi istisnasız 4s² 3d⁴ yazmış: ms = +1/2 olan 14, n = 3 olan 12 elektron sayıp 14 + 12 = 26 bulmuştur.','bilgi'),
  (15,'n = 3 olan elektronları saymayı unutmuş; yalnız ms = +1/2 olan 15 elektronu yazmıştır.','dikkat'),
  (25,'ms = +1/2 olan elektron sayısını toplam elektronun yarısı (12) almış: 12 + 13 = 25; eşleşmemiş 6 elektronun hepsi +1/2 olduğundan bu sayı 15’tir.','dikkat'),
  (22,'Eşleşmemiş elektronları +1/2 saymayıp yalnız çiftlerden gelen 9 elektronu almış: 9 + 13 = 22.','islem')],
 istenen='ms = +1/2 olan elektron sayısı ile n = 3 olan elektron sayısının toplamı.',
 ip=['Atomun dizilimini yazarken kararlılık kuralını dikkate al.'],
 bilgi=[B('Yarı dolu kararlılığı','Bir d alt kabuğu tam dolu ya da yarı dolu olduğunda daha kararlıdır; bu nedenle bazı atomlarda 4s’den 3d’ye bir elektron geçer. Örnek: 29. elementte 3d tam dolu olabilmesi için 4s’deki elektron sayısı azalır')],
 puf='Önce dizilimi yaz, sonra her sayımı alt kabuk alt kabuk yap.')

# =============== 0004 · Bohr enerji düzeyleri · orta · şekil ===============
En=lambda n:Fr(-144,n*n)
e1=abs(En(2)-En(4)); e2=abs(En(3)-En(1)); assert (e1,e2,e2-e1)==(27,128,101)
assert (abs(Fr(-144,2)-Fr(-144,4)),)==(36,); assert abs(Fr(-144,3)-Fr(-144,1))-36==60
assert e2-abs(En(2)-En(3))==108 and e2+e1==155
g=''
for n in range(1,6):
    y=(n-1)*.9; g+=f'\\draw[thick] (0,{y:.2f}) -- (3.4,{y:.2f}); \\node[anchor=east] at (-.1,{y:.2f}) {{n = {n}}};'
g+=f'\\draw[vurgu,very thick,{ARR}] (1.0,{3*.9:.2f}) -- (1.0,{1*.9+.05:.2f}); \\node[anchor=east] at (.9,{2.25:.2f}) {{\\textbf{{I}}}};'
g+=f'\\draw[very thick,{ARR}] (2.5,.05) -- (2.5,{2*.9-.05:.2f}); \\node[anchor=west] at (2.6,.45) {{\\textbf{{II}}}};'
SK=tk(g)
q('0004','04',[A('I. geçişi hesapla','n = 4’ten n = 2’ye geçişte enerji yayılır: E₄ = −9, E₂ = −36 kJ/mol.','|−36 − (−9)| = 27 kJ/mol'),
  A('II. geçişi hesapla','n = 1’den n = 3’e geçişte enerji soğurulur: E₁ = −144, E₃ = −16 kJ/mol.','|−16 − (−144)| = 128 kJ/mol'),
  A('Farkı bul','Soğurulan enerjiden yayılan enerji çıkarılır.','128 − 27 = 101 kJ/mol')],
 ne='Bohr modelinde enerji düzeyi geçişleri',z='orta',alt='Bohr Modeli',kaz='Bohr modelinde enerji düzeyleri arasındaki geçişlerde yayılan ve soğurulan enerjileri hesaplar.',kalip='şekilli',
 metin='Bohr atom modeline göre belirli bir taneciğin n. enerji düzeyindeki elektronunun enerjisi Eₙ = −144 ÷ n² (kJ/mol) bağıntısıyla verilmektedir. Bu taneciğin elektronunun yaptığı I ve II numaralı geçişler enerji düzeyleri diyagramında gösterilmiştir (düzeyler ölçekli çizilmemiştir).\nBuna göre, II. geçişte soğurulan enerji ile I. geçişte yayılan enerji arasındaki fark kaç kJ/mol’dür?',
 sekil=SK,dogru=101,yan=[(60,'Enerjiyi −144 ÷ n alarak (n² yerine n) hesaplamış: I. geçiş 36, II. geçiş 96 bulup 96 − 36 = 60 hesaplamıştır.','bilgi'),
  (108,'I. geçişi 3 → 2 sanmış: yayılan enerjiyi 20 bulup 128 − 20 = 108 hesaplamıştır; oysa I. geçiş 4 → 2’dir.','dikkat'),
  (128,'Yayılan enerjiyi çıkarmayı unutup yalnız II. geçişin enerjisini (128) vermiştir.','dikkat'),
  (155,'Farkı almak yerine iki geçişin enerjilerini toplamış: 128 + 27 = 155 bulmuştur.','islem')],
 istenen='Soğurulan ve yayılan enerjiler arasındaki fark.',
 ip=['Her geçiş için iki düzeyin enerjisini ayrı ayrı hesapla.'],
 bilgi=[B('Geçiş enerjisi','Elektron yüksek enerjili düzeyden düşüğe geçerken enerji yayar, düşükten yükseğe geçerken enerji soğurur. Alınan ya da verilen enerji iki düzeyin enerjileri farkının mutlak değeridir. Örnek: Eₙ = −50 ÷ n² olan bir taneciğin 2 → 1 geçişinde 37,5 birim enerji yayılır')],
 puf='Enerji düzeylerinin enerjilerini yaz, her geçiş için farkın mutlak değerini al, sonra isteneni hesapla.')

# =============== 0005 · anyon diyagramı · orta · öncüllü + şekil ===============
SK=tk(kutular([[('3s',['ud']),('3p',['ud','ud','ud'])]],satir_adlari=['X$^{2-}$'],w=.62,aralik=.5))
Zx=16; assert 2+2+6+2+6==18 and Zx==18-2
a5=alt(Zx); assert essiz(a5)==2 and say(a5,M0)==9
onc('0005','05','X²⁻ iyonunun 3s ve 3p orbitallerindeki elektron dağılımı şekilde gösterilmiştir. İyonun daha içteki bütün orbitalleri tam doludur. X atomu temel hâldedir.',
 [('X atomunun eşleşmemiş elektron sayısı 2’dir.',True,'X²⁻ iyonu 18 elektronludur; X atomu 16 elektronlu olup 3p⁴ ile 2 eşleşmemiş elektrona sahiptir.','X atomunun 3p alt kabuğunda 4 elektron vardır ve bunlardan 2’si eşleşmemiştir.'),
  ('X²⁻ iyonunun yarıçapı X atomunun yarıçapından küçüktür.',False,'Anyon, atoma göre daha fazla elektron taşır ve çekirdek yükü değişmediği için elektronlar arası itme artar; yarıçap büyür.','Anyonun yarıçapı, aynı çekirdek yükünde elektron sayısı arttığından atomunkinden büyüktür.'),
  ('X atomunda ml = 0 olan elektron sayısı 8’dir.',False,'1s, 2s, 3s’de 6; 2p’de 2; 3p⁴’te 1 elektron ml = 0 değerindedir; toplam 9’dur.','Her s alt kabuğunun ve dolu 2p’nin ml = 0 elektronları ile 3p’deki 1 elektron toplam 9 eder.')],
 0,'Buna göre, yukarıdaki ifadelerden hangileri doğrudur?',ne='Anyon diyagramından atoma geçiş',z='orta',alt='Anyonun Orbital Diyagramı',kaz='Anyonun orbital diyagramından atom numarasını bulup atom ve iyon özelliklerini yargılar.',kalip='öncüllü',sekil=SK,
 ip=['Önce iyondaki toplam elektron sayısından atom numarasını bul.'],
 bilgi=[B('Anyonlar','Anyon, atomun elektron almasıyla oluşur; çekirdekteki proton sayısı değişmez, elektron sayısı artar. Örnek: 9. elementin atomu 9, anyonu F⁻ ise 10 elektron taşır')],
 puf='Elektron sayısından atom numarasına, sonra atomun dizilimine geç; her ifadeyi dizilim üzerinden sına.')

# =============== 0006 · kuantum sayıları tablosu · orta · olumsuz kök ===============
R6=[('K',3,1,0,.5),('L',3,1,0,-.5),('M',3,2,0,.5),('N',4,0,0,.5),('R',3,1,-1,.5)]
assert all(gecerli(*r[1:]) for r in R6)
SK=tablo_svg(['Elektron','n','l','ml','ms'],[[r[0],str(r[1]),str(r[2]),mls(r[3]),sg(r[4])] for r in R6])
ev=lambda n,l:(n+l,n)
assert ev(3,2)>ev(4,0) and ev(3,2)>ev(3,1)
S6=[('K ve L elektronları aynı orbitaldedir.','K ve L’nin n, l ve ml değerleri aynıdır; yalnız ms değerleri zıttır. Bu şıkkı seçen, ms farkını orbital farkı sanmıştır.'),
    ('K, L ve R elektronları aynı alt kabuktadır.','Üçünün de n = 3 ve l = 1’dir; ml farkı yalnız orbitali değiştirir. Bu şıkkı seçen, ml farkını alt kabuk farkı sanmıştır.'),
    ('M elektronunun enerjisi K elektronunun enerjisinden büyüktür.','3d (n + l = 5) elektronu 3p (n + l = 4) elektronundan yüksek enerjilidir. Bu şıkkı seçen, aynı n değerinde l büyüdükçe enerjinin azaldığını sanmıştır.'),
    ('N elektronu küresel simetrik bir orbitaldedir.','l = 0 olduğundan N, s orbitalindedir ve s orbitalleri küreseldir. Bu şıkkı seçen, l = 0 değerini küresel simetriyle ilişkilendirememiştir.')]
YY='N elektronunun enerjisi, n değeri büyük olduğundan M elektronunun enerjisinden büyüktür.'
q('0006','06',[A('Elektronları tanımla','K, L, R: 3p; M: 3d; N: 4s alt kabuğundadır.','K, L, R → 3p · M → 3d · N → 4s'),
  A('Yargıları sına','Aynı orbital için n, l ve ml eşit olmalıdır; enerji n + l ile belirlenir.','M: n + l = 5 · N: n + l = 4'),
  A('Yanlışı belirle','N’nin enerjisi M’ninkinden küçüktür; yargı yanlıştır.','M’nin enerjisi N’ninkinden büyüktür')],
 ne='Kuantum sayıları tablosu',z='orta',alt='Kuantum Sayıları Tablosu',kaz='Elektronların kuantum sayılarından orbital, alt kabuk ve enerji ilişkilerini yorumlar.',kalip='tablo',
 metin='Çok elektronlu bir atomda bulunan K, L, M, N ve R elektronlarının kuantum sayıları tabloda verilmiştir.\nBuna göre, bu elektronlarla ilgili aşağıdakilerden hangisi yanlıştır?',
 sekil=SK,dogru=YY,sira=yer(YY,[x[0] for x in S6],2),yan=[(x[0],x[1],'bilgi') for x in S6],istenen='Yanlış olan yargı.',
 ip=['Aynı orbital ve aynı alt kabuk için hangi kuantum sayılarının eşit olması gerektiğini düşün.'],
 bilgi=[B('Enerji sıralaması','Çok elektronlu atomlarda orbital enerjisi n + l toplamıyla artar; toplam eşitse n büyük olanın enerjisi yüksektir. Örnek: 2p (n + l = 3) orbitali 3s (n + l = 3) orbitalinden daha düşük enerjilidir')],
 puf='Önce her elektronun alt kabuğunu yaz; sonra yargıları n, l, ml ve n + l ile sına.')

# =============== 0007 · eşleşmemiş elektron grafiği · orta ===============
Z7=[12,13,14,15,16]; U7=[essiz(alt(z)) for z in Z7]; assert U7==[0,1,2,3,2]
for per in range(1):
    cand=[z for z in range(11,19) if [essiz(alt(x)) for x in range(z,z+5)]==U7 and z+4<=18]; assert cand==[12]
SK=tk(cubuk_grafik(list('KLMNR'),U7,4,1,'Eşleşmemiş\\\\elektron sayısı','Atom numarası artan sırada elementler',dx=.95))
c7=kn(14,L1)+kn(16,L1); assert (kn(14,L1),kn(16,L1),c7)==(8,10,18)
assert (2+4,6+6,kn(14,L1)+kn(15,L1),kn(14,L1)*2)==(6,12,17,16)
q('0007','07',[A('Elementleri bul','3. periyotta ardışık beş elementte eşleşmemiş elektron sayısı 0, 1, 2, 3, 2 olan dizi Mg’den S’ye kadardır.','K = Mg, L = Al, M = Si, N = P, R = S'),
  A('M’yi say','Si: 1s² 2s² 2p⁶ 3s² 3p²; l = 1 elektronları 2p ve 3p’de bulunur.','6 + 2 = 8'),
  A('R’yi say','S: ... 3s² 3p⁴; l = 1 elektronları 2p ve 3p’de bulunur.','6 + 4 = 10'),
  A('Topla','İki atomun l = 1 elektronları toplanır.','8 + 10 = 18')],
 ne='Eşleşmemiş elektron grafiği',z='orta',alt='Eşleşmemiş Elektron Grafiği',kaz='Eşleşmemiş elektron sayısı grafiğinden elementleri belirleyip l = 1 olan elektronları sayar.',kalip='grafik',
 metin='3. periyotta bulunan, atom numaraları ardışık olan K, L, M, N ve R elementlerinin temel hâldeki atomlarının eşleşmemiş elektron sayıları grafikte gösterilmiştir. Elementler atom numarası artan sırada K’dan R’ye doğru sıralanmıştır.\nBuna göre, M ve R atomlarında açısal momentum kuantum sayısı (l) 1 olan toplam elektron sayısı kaçtır?',
 sekil=SK,dogru=18,yan=[(6,'Yalnız 3p elektronlarını saymış: 2 + 4 = 6; 2p alt kabuğundaki 6 elektronun l = 1 olduğunu atlamıştır.','dikkat'),
  (12,'Her atomda yalnız 2p’yi (6 + 6) saymış; 3p elektronlarını hesaba katmamıştır.','dikkat'),
  (16,'R’yi de Si sanarak 8 + 8 = 16 bulmuştur; R, eşleşmemiş elektron sayısı 2 olan S’dir.','bilgi'),
  (17,'R’yi N (P) sanmış: 8 + 9 = 17 bulmuştur; oysa R’nin grafikteki değeri N’den farklı olan S’tir.','bilgi')],
 istenen='M ve R atomlarındaki l = 1 elektronlarının toplamı.',
 ip=['Grafikteki değerlerin oluşturduğu deseni 3. periyot elementleriyle eşleştir.'],
 bilgi=[B('Eşleşmemiş elektron sayısı','Bir p alt kabuğu dolarken önce her orbitale birer elektron girer, sonra eşleşme başlar; bu yüzden eşleşmemiş elektron sayısı önce artar, sonra azalır. Örnek: 2. periyotta bu sayı 3A grubunda 1, 5A grubunda 3’tür')],
 puf='Grafikteki dizinin hangi ardışık elementlere ait olduğunu bul; sonra her atomun dizilimini yaz ve p elektronlarını say.')

# =============== 0008 · katyon diyagramı → atom · zor · şekil ===============
D8=['ud','ud','u','u','u']
SK=tk(kutular([[('4s',['']),('3d',D8)]],satir_adlari=['X$^{2+}$'],w=.62,aralik=.6))
at8=alt(27); ion8=iyon(27,2); assert ion8=={(1,0):2,(2,0):2,(2,1):6,(3,0):2,(3,1):6,(3,2):7} and 2+2+6+2+6+7==25
m_at=say(at8,M0); m_ion=say(ion8,M0); assert (m_at,m_ion)==(13,11)
assert m_at-3==10 and m_at-1==12 and m_at+1==14 and say(at8,lambda n,l,ml,ms:ml==0 and n<=3 and l<2)==10
q('0008','08',[A('Atomu bul','İyonda 18 + 7 = 25 elektron vardır; X²⁺ olduğundan atom 27 elektronludur.','X atomunun atom numarası 27'),
  A('Atomun dizilimini yaz','Katyon oluşurken 4s’deki 2 elektron verilmiştir; atomda 4s dolu, 3d ise 3d⁷’dir.','1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d⁷'),
  A('ml = 0 olanları say','Her s ve 2p, 3p alt kabuğunda 2’şer; 3d’de ml = 0 kutusunda 1 elektron vardır.','5 × 2 + 2 + 1 = 13'),
  A('Kontrol et','İyonda ml = 0 olan 11 elektron vardır; atomda 4s’deki 2 elektron daha eklenir.','11 + 2 = 13')],
 ne='Katyon diyagramından atoma dönüş',z='zor',alt='Katyonun Orbital Diyagramı',kaz='Katyonun orbital diyagramından atomu belirleyip ml = 0 olan elektronları sayar.',kalip='şekilli',
 metin='X²⁺ iyonunun 4s ve 3d orbitallerindeki elektron dağılımı şekilde verilmiştir. 3d orbitalleri soldan sağa ml = −2, −1, 0, +1, +2 sırasındadır; iyonun daha içteki bütün orbitalleri tam doludur.\nBuna göre, X atomunun temel hâlinde manyetik kuantum sayısı (ml) 0 olan toplam kaç elektron bulunur?',
 sekil=SK,dogru=13,yan=[(10,'4s ve 3d’deki ml = 0 elektronlarını hiç saymamış; yalnız 1s, 2s, 2p, 3s ve 3p’deki 10 elektronu almıştır.','dikkat'),
  (11,'Sayımı iyon üzerinde yapmış: 4s’deki 2 elektron atomda vardır ve ml = 0’dır; 11 + 2 = 13 olmalıdır.','bilgi'),
  (12,'3d’deki ml = 0 elektronunu atlamış: 10 + 2 = 12 bulmuştur.','dikkat'),
  (14,'3d’deki ml = 0 kutusunu dolu sanmış: 10 + 2 + 2 = 14 bulmuştur; oysa o kutuda yalnız 1 elektron vardır.','islem')],
 istenen='Atomdaki ml = 0 elektronlarının sayısı.',
 ip=['Önce iyondaki elektron sayısından atoma geç, sonra dizilimi yaz.'],
 bilgi=[B('Katyonlar','Katyon oluşurken elektronlar önce en büyük baş kuantum sayılı kabuktan verilir. Atom ile katyon arasındaki fark, verilen elektronlardır. Örnek: 2A grubundaki bir atomun 2+ yüklü iyonunda s alt kabuğunun dış elektronları kalmaz')],
 puf='İyondan atoma dönerken verilen elektronları geri ekle; sonra ml = 0 elektronlarını alt kabuk alt kabuk say.')

# =============== 0009 · Cu / Zn iyonları · zor · öncüllü ===============
cu=alt(29); zn=alt(30); assert cu[(4,0)]==1 and cu[(3,2)]==10 and zn[(4,0)]==2
assert iyon(29,1)==iyon(30,2) and (4,0) not in iyon(29,1)
assert iyon(29,2)[(3,2)]==9 and zn[(3,2)]==10 and essiz(iyon(29,2))+essiz(zn)==essiz(cu)==1
onc('0009','09','Atom numaraları 29 olan bakır (Cu) ve 30 olan çinko (Zn) elementlerinin temel hâldeki atomları ile bu atomlardan oluşan iyonlar karşılaştırılıyor. Cu atomu istisnalı elektron dizilimine sahiptir.',
 [('Cu⁺ ve Zn²⁺ iyonlarının elektron dizilimleri aynıdır.',True,'Cu⁺: 4s¹ elektronu gider, 3d¹⁰ kalır; Zn²⁺: 4s² elektronu gider, 3d¹⁰ kalır. İkisi de 28 elektronludur ve dizilimleri aynıdır.','Cu⁺ ve Zn²⁺ iyonları 28 elektronludur ve ikisinin de dizilimi 3d¹⁰ ile biter.'),
  ('Cu⁺ iyonunun 4s orbitalinde 1 elektron bulunur.',False,'Cu atomunun 4s¹ elektronu iyon oluşurken önce verilir; Cu⁺ iyonunda 4s boştur ve 3d¹⁰ doludur.','Katyon oluşurken elektron önce 4s’den verildiği için Cu⁺ iyonunda 4s boştur.'),
  ('Cu²⁺ iyonu ile Zn atomunun eşleşmemiş elektron sayılarının toplamı, Cu atomundaki eşleşmemiş elektron sayısına eşittir.',True,'Cu²⁺ iyonu 3d⁹ olduğundan 1, Zn atomu 3d¹⁰ 4s² olduğundan 0 eşleşmemiş elektrona sahiptir; Cu atomu 4s¹ 3d¹⁰ ile 1 eşleşmemiş elektron taşır, 1 + 0 = 1 eşitlik sağlanır.','Cu²⁺ iyonunda 1, Zn atomunda 0, Cu atomunda 1 eşleşmemiş elektron vardır; 1 + 0 = 1 olur.')],
 2,'Buna göre, yukarıdaki ifadelerden hangileri doğrudur?',ne='Cu ve Zn iyonları',z='zor',alt='İstisnalı Dizilimlerde İyonlar',kaz='Cu ve Zn atomlarından oluşan iyonların dizilimlerini karşılaştırarak yargıları değerlendirir.',kalip='öncüllü',
 ip=['Her iyonun elektron dizilimini, atomdan hangi elektronların ayrıldığını düşünerek yaz.'],
 bilgi=[B('Katyon dizilimi','Katyon oluşurken elektronlar önce en dıştaki, yani en büyük baş kuantum sayılı alt kabuktan verilir; bu alt kabuk boşaldıktan sonra d alt kabuğundan elektron ayrılır. Örnek: 4s² 3d⁶ dizilimli bir atomda 1+ iyon oluşurken ayrılan elektron 4s’den gelir')],
 puf='Her atomun dizilimini yazıp iyon yükü kadar elektronu önce dış kabuktan çıkar; sonra ifadeleri sına.')

# =============== 0010 · kesit, ml sayımı, izoelektronik iyonlar · zor · öncüllü ===============
SK=tk(kesit([2,3],{(2,'5A'):'X',(2,'7A'):'Y',(3,'2A'):'T',(3,'6A'):'Z'}))
assert (kn(7,lambda n,l,ml,ms:ml==-1),kn(9,lambda n,l,ml,ms:ml==-1))==(1,2)
assert kn(16,lambda n,l,ml,ms:ml==1)==3 and 12-2==10==9+1
onc('0010','10','Periyodik tablonun 2. ve 3. periyotlarından alınan bir kesitte X, Y, T ve Z elementlerinin yerleri gösterilmiştir. (X, Y, T ve Z elementlerin gerçek sembolleri değildir.) Bir p alt kabuğunun orbitallerine elektronlar ml = −1, 0, +1 sırasıyla önce birer birer yerleşir, sonra aynı sırayla eşleşir.',
 [('X atomunda ml = −1 olan elektron sayısı, Y atomundakinden fazladır.',False,'X (2. periyot 5A) atomunda 2p³ ile ml = −1 olan 1 elektron; Y (2. periyot 7A) atomunda 2p⁵ ile 2 elektron vardır.','X atomunda ml = −1 olan 1 elektron, Y atomunda 2 elektron bulunur.'),
  ('T²⁺ iyonunun yarıçapı, Y⁻ iyonunun yarıçapından küçüktür.',True,'T²⁺ ve Y⁻ iyonları 10 elektronludur; T’nin proton sayısı Y’ninkinden fazla olduğundan T²⁺ daha küçüktür.','İki iyon izoelektroniktir; proton sayısı fazla olan T²⁺ iyonunun yarıçapı daha küçüktür.'),
  ('Z atomunda ml = +1 olan elektron sayısı 3’tür.',True,'Z (3. periyot 6A) atomunda 2p’de 2, 3p⁴’te 1 elektron ml = +1 değerindedir; toplam 3’tür.','Z atomunda ml = +1 olan 2 elektron 2p’de, 1 elektron 3p’de bulunur.')],
 3,'Buna göre, yukarıdaki ifadelerden hangileri doğrudur?',ne='Kesit, ml sayımı ve izoelektronik iyonlar',z='zor',alt='Periyodik Özellikler ve ml Sayımı',kaz='Periyodik tablo kesitinden elementleri belirleyip ml sayımı ve izoelektronik iyon yarıçapı yargılarını değerlendirir.',kalip='öncüllü',sekil=SK,
 ip=['Kesitten her elementin atom numarasını bulduktan sonra yargıları tek tek sına.'],
 bilgi=[B('İzoelektronik iyonlar','Elektron sayıları eşit olan taneciklerde yarıçap, çekirdekteki proton sayısı arttıkça azalır; çünkü elektronlar çekirdeğe daha güçlü çekilir. Örnek: O²⁻ iyonunun yarıçapı N³⁻ iyonunun yarıçapından küçüktür')],
 puf='Kesitten atom numaralarını bul; ml sayımını dizilim üzerinden, iyon yarıçapını proton sayısı üzerinden değerlendir.')

# ---------------- paket denetimi ve yazım ----------------
from collections import Counter
bitir(P,'modernatomiki',UK)
import json as _j
_k=os.path.join(HV,'kartlar','modernatomiki.json'); _d=_j.load(open(_k)); _d['not_']='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT Kimya çıkmış soruları, yayın kaynakları (yalnız mantık), MEB 11. sınıf Modern Atom Teorisi kazanımları.'
_j.dump(_d,open(os.path.join(HV,'kartlar','akmodernatomiki.json'),'w'),ensure_ascii=False,indent=1); os.remove(_k)
