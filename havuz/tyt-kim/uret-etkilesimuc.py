"""TYT Kimya · Kimyasal Türler Arası Etkileşimler · 3. ek paket (etkilesimuc): 10 soru, kardeş yok, ipucu 1.
Şekil verileri Python'da hesaplanır; TikZ bu değerlerden üretilir. Öncüllerin doğru/yanlış değeri tek yerde (d sözlüğü) tanımlanır."""
import sys,os,math,random,itertools
from fractions import Fraction as Fr
GD=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,GD)
import _hafif_kim2 as H
from _hafif_kim2 import *
from _hafif_kim import onc as _onc_eski, tek
KONU_='Kimyasal Türler Arası Etkileşimler'; UK='kim|Kimyasal Türler Arası Etkileşimler'
H.KONU=KONU_
P=Parti('etkilesimuc',KONU_,UK,ders='TYT Kimya',idon='tytkim')
KY='ÖSYM 2018–2026 TYT Kimya (yalnız mantık) · MEB 10. sınıf Kimyasal Türler Arası Etkileşimler'
MAP={}
for _n,_t in [(('01','06','10'),('bag','Bağ türü ve bileşik oluşumu')),(('02','07'),('kati','Katı türleri ve erime noktası')),
              (('03','04','05'),('zayif','Zayıf etkileşimler ve polarlık')),(('08',),('olay','Hâl değişimi ve kimyasal olayda kopan etkileşimler')),
              (('09',),('polar','Elektronegatiflik ve bağ polarlığı'))]:
    for _x in _n: MAP[_x]=_t
assert len(MAP)==10
def kartla(n,alt,fikir,tuzak,z,kalip,adim):
    a,b=MAP[n]; kart(f'K-KMET3-{n}',alt,fikir,tuzak,z,kalip,adim,f'km-et3-{a}',b,KY)
def q(no,ad,**k):
    assert len(k['ip'])==1
    k['tipId']='km-et3-'+MAP[no[-2:]][0]; k['tip']=MAP[no[-2:]][1]
    ne=k.pop('ne'); k['kart']=f"K-KMET3-{no[-2:]} ({MAP[no[-2:]][1].lower()}) · {ne}"
    mk(P,no,ad=ad,adim=len(ad),**k)
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
ARR='-{Stealth[length=1.9mm,width=1.7mm]}'
def tk(g): return tikz_svg(HEAD+g+TAIL)

# ---------- öncüllü yardımcıları ----------
def _anah(s): return (len(s),tuple(s))
def onc_t(d,hedef):
    etiket=sorted(d,key=lambda x:['I','II','III','IV'].index(x))
    T=frozenset(k for k,v in d.items() if v[0])
    ad=lambda s:tuple(sorted(s,key=lambda x:['I','II','III','IV'].index(x)))
    adaylar=[]
    for n in range(1,min(3,len(etiket))+1):
        for c in itertools.combinations(etiket,n): adaylar.append(c)
    adaylar=sorted(adaylar,key=_anah); kt=_anah(ad(T))
    alt=[c for c in adaylar if _anah(c)<kt]; ust=[c for c in adaylar if _anah(c)>kt]
    assert hedef<=len(alt) and 4-hedef<=len(ust),('hedef uygun degil',T,hedef,len(alt),len(ust))
    uz=lambda c:len(frozenset(c)^T)
    sa=sorted(alt,key=lambda c:(uz(c),-adaylar.index(c)))[:hedef]
    su=sorted(ust,key=lambda c:(uz(c),adaylar.index(c)))[:4-hedef]
    ops=sorted(sa+[ad(T)]+su,key=_anah)
    assert ops.index(ad(T))==hedef
    return _onc_eski(d,ops)
def tek_t(dogru,yanlislar,hedef,hedef_bool=True):
    S=[(m,not hedef_bool,n) for m,n in yanlislar]
    S.insert(hedef,(dogru[0],hedef_bool,dogru[1]))
    return tek(S,hedef_bool)
def cap(s): return ('İ' if s[0]=='i' else s[0].upper())+s[1:]
def oy(d,anahtarlar=None):
    return ' · '.join(f'{k}: '+('doğru' if d[k][0] else 'yanlış') for k in (anahtarlar or d))
def adim_onc(d,keys,baslik=None):
    ac=' '.join(cap(d[k][1])+'.' for k in keys)
    return A(baslik or ('. '.join(keys)+'. öncül' if len(keys)==1 else ' ve '.join(keys)+'. öncüller'),ac,oy(d,keys))

# ---------- çizim yardımcıları ----------
def disc(x,y,r=.12,f='vurgu!25'): return f'\\draw[thin,fill={f}] ({x:.3f},{y:.3f}) circle ({r});'
def nokta(x,y,r=.06): return f'\\fill ({x:.3f},{y:.3f}) circle ({r});'
def uzak(p,L,m): return all((p[0]-a)**2+(p[1]-b)**2>=m*m for a,b in L)
def rastgele(n,x1,x2,y1,y2,m,seed,L0=()):
    rng=random.Random(seed)
    for deneme in range(2000):
        L=list(L0); new=[]
        for _ in range(4000):
            p=(rng.uniform(x1,x2),rng.uniform(y1,y2))
            if uzak(p,L,m): L.append(p); new.append(p)
            if len(new)==n: return new
    raise RuntimeError('yerlesmedi')
def kap(x0,W=2.4,Hh=2.2): return f'\\draw[thick] ({x0},{Hh}) -- ({x0},0) -- ({x0+W},0) -- ({x0+W},{Hh});'
def beher(x,lv,w=1.7,h=2.3,fill='vurgu!15'):
    return f'\\fill[{fill}] ({x},0) rectangle ({x+w},{lv});\\draw[thick] ({x},{h}) -- ({x},0) -- ({x+w},0) -- ({x+w},{h});'
def eksen(xm,ym,sx,sy,xt,yt,xl,yl,xtik=True,grid=True,xlpos=None):
    s=''
    if grid:
        for v in yt:
            if v!=0: s+=f'\\draw[black!15] (0,{v*sy:.3f}) -- ({xm*sx:.3f},{v*sy:.3f});'
        for v in xt:
            if v!=0: s+=f'\\draw[black!15] ({v*sx:.3f},0) -- ({v*sx:.3f},{ym*sy:.3f});'
    s+=f'\\draw[thick,{ARR}] (0,0) -- ({xm*sx+.35:.3f},0);\\draw[thick,{ARR}] (0,0) -- (0,{ym*sy+.35:.3f});'
    if xtik:
        for v in xt: s+=f'\\draw[thick] ({v*sx:.3f},0) -- ({v*sx:.3f},-.07) node[below,font=\\footnotesize] {{{v}}};'
    for v in yt: s+=f'\\draw[thick] (0,{v*sy:.3f}) -- (-.07,{v*sy:.3f}) node[left,font=\\footnotesize] {{{v if v>=0 else "$-$"+str(-v)}}};'
    s+=f'\\node[below,font=\\footnotesize] at ({xm*sx/2 if xlpos is None else xlpos:.3f},{-.55 if xtik else -.2}) {{{xl}}};'
    s+=f'\\node[above,font=\\footnotesize] at (0,{ym*sy+.4:.3f}) {{{yl}}};'
    return s
def egri(pts,sx,sy,stil='thick'):
    c=' '.join(f'({x*sx:.3f},{y*sy:.3f})' for x,y in pts)
    return f'\\draw[{stil}] plot[smooth,tension=.7] coordinates {{{c}}};'

# ============================================================ KARTLAR
kartla('01','Periyodik tablo kesitinde bileşik türü','Grup numarasından değerlik elektronu bulunur; metal + ametal iyonik, ametal + ametal kovalent bileşik verir; formül yüklerin dengelenmesiyle yazılır.','İki ametal arasında da iyonik bağ oluştuğunu sanmak; 2A + 6A bileşiğinin formülünü YZ₂ yazmak.','kolay','öncüllü',3)
kartla('02','Kovalent ağ ve molekül yapılı katılar','Elmas ve kuvars gibi kovalent ağ katılarda erimek için kovalent bağlar kopar, erime noktası çok yüksektir; moleküler katılarda yalnız zayıf etkileşimler zayıflar.','Her kovalent bileşiğin erime noktasının düşük olduğunu sanmak; I₂’nin erirken kovalent bağlarının koptuğunu düşünmek.','kolay','tablo',3)
kartla('03','Su ve buzda hidrojen bağı','Hidrojen bağı, N, O ya da F’ye bağlı H ile komşu molekülün elektronegatif atomu arasında kurulur; buzda düzenli ve boşluklu bir yapı oluşturur.','Hidrojen bağını molekül içi kovalent bağla karıştırmak.','orta','öncüllü',4)
kartla('04','Polar ve apolar sıvıların elektrik yükü etkisi','Yüklü çubuk polar molekülleri yönlendirip çeker; apolar sıvı akışı sapmaz; polar sıvılar apolar sıvılarla karışmaz.','Apolar sıvıda hiç etkileşim olmadığını sanmak; akışın sapmasını sıvı kütlesine bağlamak.','orta','şekilli',3)
kartla('05','Hidrojen bağının koşulu','Hidrojen bağı için H atomu N, O ya da F atomuna bağlı olmalıdır; aynı molekül formülüne sahip maddelerde bu bağı yapabilen kaynama noktası yüksektir.','Aynı mol kütleli maddelerin kaynama noktasının aynı olacağını sanmak; C–H bağındaki H’yi hidrojen bağı yapabilir saymak.','orta','şekilli',3)
kartla('06','İyonik bileşikte iyon yükü ve boyutu','Erime noktası iyon yükü arttıkça ve iyonlar küçüldükçe yükselir; karşılaştırma için bir etken sabit tutulur.','Yalnız yüke ya da yalnız boyuta bakmak; anyon boyutunu katyondan ayrı düşünmemek.','orta','öncüllü',4)
kartla('07','Periyodik özelliğe göre erime noktası','Metalik bağ değerlik elektronu arttıkça güçlenir; kovalent ağ yapıda erime noktası çok yüksektir; moleküler maddelerde London kuvvetleri zayıftır, erime noktası düşüktür.','Düşük erime noktasını molekül içi bağın zayıflığına bağlamak; soy gazları kovalent bağlı saymak.','orta','grafik',3)
kartla('08','Olaylarda kopan etkileşimler','Hâl değişiminde yalnız moleküller arası etkileşimler (ya da iyonik/metalik bağ) zayıflar; kimyasal değişimde kovalent bağlar kopar.','Elektroliz ya da yanmada moleküller arası etkileşimlerin koptuğunu sanmak.','kolay','tablo',3)
kartla('09','Elektronegatiflik farkı ve bağ polarlığı','Bağ yapan atomların elektronegatiflik farkı büyüdükçe bağ daha polardır; aynı atomlar arasındaki bağ apolardır.','Elektronegatifliği yüksek elementi içeren bağı otomatik en polar saymak; farkı almadan toplamak.','kolay','hikâyeli',2)
kartla('10','Bohr modelinden bileşik oluşumu','Katman diyagramından değerlik elektronu bulunur; metal elektron verir, ametal alır; iki ametal elektron ortaklaşa kullanır.','Ametal–ametal bileşikte elektron aktarımı olduğunu sanmak; iyon yüklerini yanlış dengelemek.','orta','öncüllü',4)

# ============================================================ 01 · periyodik tablo kesiti (kolay, öncüllü, şekil)
POS={'X':(3,1),'Y':(3,2),'Z':(2,6),'T':(3,7)}     # (periyot, A grubu)
g=''
for c in range(8): g+=f'\\node[font=\\footnotesize] at ({c*.85+.42:.2f},1.95) {{{c+1}A}};'
for rr,(per,y0) in enumerate([(2,.95),(3,.1)]):
    g+=f'\\node[font=\\footnotesize,anchor=east] at (-.1,{y0+.42:.2f}) {{{per}. periyot}};'
    for c in range(8): g+=f'\\draw ({c*.85:.2f},{y0}) rectangle ({c*.85+.85:.2f},{y0+.85});'
for nm,(per,grp) in POS.items():
    y0={2:.95,3:.1}[per]; g+=f'\\node[font=\\bfseries] at ({(grp-1)*.85+.42:.2f},{y0+.42:.2f}) {{{nm}}};'
SK1=tk(g)
dig={'X':1,'Y':2,'Z':6,'T':7}
yuk={'X':1,'Y':2,'Z':-2,'T':-1}
assert yuk['X']+(-yuk['T'] and yuk['T'])==0                       # XT
assert yuk['Y']+yuk['Z']==0                                         # YZ
metal={k:dig[k]<=2 for k in dig}; assert metal['X'] and metal['Y'] and not metal['Z'] and not metal['T']
d={'I':(True,'X (1A metal) ile T (7A ametal) arasında elektron aktarımı olur; +1 ve −1 yükler 1 : 1 oranında birleştiğinden formül XT’dir'),
   'II':(True,'Y (2A metal) +2, Z (6A ametal) −2 yüklü iyon verir; yükler dengelendiğinden formül YZ’dir ve bağ iyoniktir'),
   'III':(False,'Z ve T iki ametaldir; elektronlarını ortaklaşa kullanarak kovalent bağ yaparlar, iyonik bağ oluşmaz')}
r=onc_t(d,1)
q('0001',ad=[A('Grup numaralarını oku','A grubu numarası değerlik elektronu sayısını verir; X, Y metal; Z, T ametaldir.','X: 1 · Y: 2 · Z: 6 · T: 7 değerlik elektronu'),adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),A('Sonucu yaz','Doğru olan öncüller bir arada yazılır.',oy(d)+' · Sonuç: '+r['dogru'])],
 alt='Güçlü Etkileşimler',z='kolay',kaz='Periyodik tablodaki konumdan bileşiğin bağ türünü ve formülünü belirler.',kalip='öncüllü',ne='X, Y, Z, T harflerinin tablodaki yerleri',
 metin='Şekilde, periyodik tablonun bir bölümünde X, Y, Z ve T elementlerinin yerleri gösterilmiştir (harfler gerçek element sembolü değildir).\nI. X ile T’nin oluşturduğu bileşik iyonik bağlıdır ve formülü XT’dir.\nII. Y ile Z’nin oluşturduğu bileşik iyonik bağlıdır ve formülü YZ’dir.\nIII. Z ile T atomları arasında iyonik bağ oluşur.\nBuna göre hangileri doğrudur?',
 sekil=SK1,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan öncüller.',
 ip=['Her elementin A grubundan değerlik elektronunu bul; metal mi ametal mi olduğuna bak.'],
 bilgi=[B('Bağ türü','Metal ile ametal arasında elektron aktarımıyla iyonik bağ, iki ametal arasında elektron ortaklığıyla kovalent bağ oluşur. İyonik bileşik formülünde toplam yük sıfır olur. Örnek: 3A metali ile 5A ametali 1 : 1 oranında birleşir')],
 puf='Her atomun grubundan değerlik elektronuna ve metal ya da ametal oluşuna bak.')

# ============================================================ 02 · kovalent ağ katılar (kolay, tablo)
TAB=[('Elmas','Katı','3550'),('Kuvars (SiO₂)','Katı','1710'),('İyot (I₂)','Katı','114'),('Azot (N₂)','Gaz','−210')]
SK2=tablo_svg(['Madde','Oda koşullarında hâli','Erime noktası (°C)'],[list(t) for t in TAB])
dg=('Elmas ve kuvarsta atomlar kovalent bağlarla ağ biçiminde bağlıdır; erimeleri için bu bağlar koptuğundan erime noktaları yüksektir.','erime noktası çok yüksek olan, atomları ağ biçiminde kovalent bağlı katılar böyle açıklanır')
yl=[('I₂ katısı erirken molekül içindeki I–I bağları kopar.','erimede yalnız moleküller arası London kuvvetleri zayıflar; molekül içi bağlar kopmaz'),
    ('N₂’nin erime noktasının düşük olması N≡N bağının zayıf olmasındandır.','erimede N≡N bağı kopmaz; düşük erime noktası moleküller arası London kuvvetlerinin zayıflığındandır'),
    ('Tablodaki dört maddenin hepsi moleküllerden oluşur.','elmas ve kuvars ayrı moleküllerden değil, ağ biçiminde bağlı atomlardan oluşur'),
    ('Kuvarsın erime noktası, elmasınkinden yüksektir.','tabloya göre elmasın erime noktası (3550 °C) kuvarsınkinden (1710 °C) yüksektir')]
r=tek_t(dg,yl,0,True)
q('0002',ad=[A('Tabloyu oku','Hâl ve erime noktalarına bakılır.','Elmas 3550 · Kuvars 1710 · İyot 114 · N₂ −210'),A('Yüksek erime noktalılar','Elmas ve kuvars çok yüksek erime noktalıdır; bu, ağ yapıdaki kovalent bağlarla ilişkilidir.','Elmas, kuvars: kovalent ağ'),A('Düşük erime noktalılar','I₂ ve N₂ moleküllerdir; yalnız zayıf etkileşimler zayıflar.','I₂, N₂: London kuvvetleri'),A('Yargıları sına','Her yargı bu bilgiyle karşılaştırılır.','Doğru yargı: kovalent ağ açıklaması')],
 alt='Katı Türleri',z='kolay',kaz='Erime noktası ve yapı verisinden kovalent ağ ve molekül yapılı katıları ayırt eder.',kalip='tablo',ne='elmas, kuvars, iyot ve N₂ tablosu',
 metin='Bir öğrenci, dört maddenin oda koşullarındaki hâlini ve erime noktalarını tablodaki gibi derlemiş ve maddelerin yapılarını tartışmıştır.\nBuna göre aşağıdakilerden hangisi doğrudur?',
 sekil=SK2,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargı.',
 ip=['Erime sırasında hangi etkileşimlerin zayıflaması gerektiğini her madde için düşün.'],
 bilgi=[B('Katı türleri','Kovalent ağ katılarda atomların hepsi kovalent bağlarla birbirine bağlıdır; erimek için bu bağların koparılması gerekir. Moleküler katılar ise molekül içi bağlarını korur, yalnız moleküller arası etkileşimleri zayıflar')],
 puf='Erime noktası çok yüksekse ağ yapılı, çok düşükse moleküler katı düşün; hâl değişiminde molekül içi bağ kopmaz.')

# ============================================================ 03 · buz ve su (orta, öncüllü, şekil)
def su_mol(x,y,ang):
    s=f'\\fill[black!45] ({x:.2f},{y:.2f}) circle (.17);'
    for da in (52,-52):
        a=math.radians(ang+da); s+=f'\\draw[fill=white] ({x+.33*math.cos(a):.2f},{y+.33*math.sin(a):.2f}) circle (.09);'
    return s
def hpos(x,y,ang): return (x+.33*math.cos(math.radians(ang+52)),y+.33*math.sin(math.radians(ang+52)))
BUZ=[(1.1*math.cos(math.radians(60*k+30)),1.1*math.sin(math.radians(60*k+30))) for k in range(6)]
SU=[(-.45,.35),(.45,.45),(-.1,-.35),(.55,-.4),(-.65,-.5),(.05,.95)]
assert len(BUZ)==len(SU)==6
g='\\draw[thick] (-1.9,-1.9) rectangle (1.9,1.9);\\draw[thick] (3.4,-1.9) rectangle (7.2,1.9);'
for k in range(6):
    x,y=BUZ[k]; xn,yn=BUZ[(k+1)%6]
    phi=math.degrees(math.atan2(yn-y,xn-x)); ang=phi-52
    g+=su_mol(x,y,ang)
    hx,hy=hpos(x,y,ang)
    g+=f'\\draw[dashed,vurgu,thick,shorten >=.22cm] ({hx:.2f},{hy:.2f}) -- ({xn:.2f},{yn:.2f});'
for i_,(x,y) in enumerate(SU): g+=su_mol(5.3+x,y+.1,[20,80,140,200,260,320][i_])
g+='\\node[below] at (0,-1.95) {Buz}; \\node[below] at (5.3,-1.95) {Sıvı su}; \\draw[dashed,vurgu,thick] (-1.6,-3.0) -- (-.9,-3.0); \\node[right,font=\\footnotesize] at (-.8,-3.0) {: buz modelinde hidrojen bağı (her kapta 6 H$_2$O molekülü, aynı kütle)};'
SK3=tk(g)
d={'I':(True,'buzda moleküller hidrojen bağlarıyla düzenli ve boşluklu dizilir; aynı kütle sıvı suya göre daha geniş hacim kaplar'),
   'II':(False,'erirken yalnız moleküller arası hidrojen bağlarının bir bölümü zayıflar; molekül içindeki O–H kovalent bağları kopmaz'),
   'III':(True,'sıvı suda da moleküller arasında hidrojen bağları vardır; yalnız buzdaki kadar düzenli değildir')}
r=onc_t(d,2)
q('0003',ad=[A('Şekli incele','Buz modelinde hidrojen bağları gösterilmiş, sıvı su modelinde gösterilmemiştir.','Kaplar özdeş; molekül sayısı aynı'),adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),A('Sonucu yaz','Doğru olan öncüller bir arada yazılır.',oy(d)+' · Sonuç: '+r['dogru'])],
 alt='Zayıf Etkileşimler',z='orta',kaz='Buz ve sıvı suyun yapısını hidrojen bağları açısından yorumlar.',kalip='öncüllü',ne='buz ve sıvı su modelleri, hidrojen bağları',
 metin='Bir öğretmen, aynı kütledeki buz ve sıvı suyun (0 °C) moleküler yapısını şekildeki gibi modelleyerek öğrencilere yorumlatıyor. Buz modelinde kesikli çizgiler hidrojen bağlarını göstermektedir; her kapta aynı sayıda H₂O molekülü vardır ve kaplar özdeştir.\nI. Buzun hacmi, aynı kütledeki sıvı suyun hacminden büyüktür.\nII. Buz erirken H₂O molekülleri içindeki O–H bağları kopar.\nIII. Sıvı su moleküllerinin arasında da hidrojen bağları bulunur.\nBuna göre hangileri doğrudur?',
 sekil=SK3,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan öncüller.',
 ip=['Hâl değişiminde hangi bağların etkilendiğini ve şekildeki dizilişi birlikte düşün.'],
 bilgi=[B('Hidrojen bağı','Hidrojen bağı, N, O ya da F atomuna bağlı H ile başka bir molekülün N, O ya da F atomu arasındaki zayıf etkileşimlerin en güçlüsüdür')],
 puf='Her yargıda hangi tür bağın söz konusu olduğunu ve şekildeki dizilişi birlikte değerlendir.')

# ============================================================ 04 · yüklü çubuk ve akan sıvı (orta, şekil)
g=''
for x in (0.8,4.2):
    g+=f'\\draw[thick] ({x-.18},5.4) rectangle ({x+.18},4.5); \\draw[thick] ({x-.06},4.5) -- ({x-.06},4.2) -- ({x+.06},4.2) -- ({x+.06},4.5);'
g+='\\draw[vurgu,very thick] (0.8,4.2) .. controls (0.8,3.0) and (1.05,2.0) .. (1.5,0.3);'
g+='\\draw[vurgu,very thick] (4.2,4.2) -- (4.2,0.3);'
for x in (1.35,4.75):
    g+=f'\\draw[thick,fill=black!12] ({x},2.6) rectangle ({x+1.0},2.9); \\node[font=\\footnotesize] at ({x+.5},2.75) {{$-\\;-\\;-$}};'
g+='\\node[font=\\bfseries] at (0.8,-.3) {K}; \\node[font=\\bfseries] at (4.2,-.3) {L};'
SK4=tk(g)
dg=('K sıvısının molekülleri polardır; bu yüzden K sıvısının akışı yüklü çubuğa doğru sapmıştır.','polar moleküller çubuğun yüküyle etkileşip ona doğru yönelir; apolar moleküller sapmaz')
yl=[('K sıvısı apolar moleküllerden oluşur.','akışı sapan K’nın molekülleri kalıcı dipole sahiptir, yani polardır'),
    ('L sıvısının molekülleri polardır.','akışı sapmayan L apolar moleküllerden oluşur'),
    ('L sıvısının moleküller arasında hiçbir etkileşim bulunmaz.','apolar moleküller arasında da London kuvvetleri vardır'),
    ('K ve L sıvıları birbiri içinde her oranda karışır.','polar ve apolar sıvılar genellikle karışmaz (benzer benzeri çözer)')]
r=tek_t(dg,yl,4,True)
q('0004',ad=[A('Akışları karşılaştır','K’nın akışı çubuğa doğru sapmış, L’ninki doğrudan düşmüştür.','K: sapıyor · L: sapmıyor'),A('Sonucu yorumla','Yüklü çubuk yalnız polar molekülleri etkiler.','K polar, L apolar'),A('Yargıları sına','Polar–apolar sıvı özellikleri ve London kuvvetleri her yargıyla karşılaştırılır.','K polar → doğru yargı bulunur')],
 alt='Zayıf Etkileşimler',z='orta',kaz='Yüklü çubukla sıvı akışının sapmasından molekülün polar ya da apolar olduğunu çıkarır.',kalip='şekilli',ne='iki büretten akan K ve L sıvıları, yüklü çubuk',
 metin='Biri polar, diğeri apolar moleküllerden oluşan K ve L sıvıları iki ayrı büretten ince bir akıntı hâlinde akıtılıyor. Öğrenci, yünle sürterek (−) yüklediği bir plastik çubuğu her akıntının yanına yaklaştırıyor. Şekilde, çubuk yakındayken akıntıların aldığı yollar gösterilmiştir.\nBuna göre aşağıdakilerden hangisi doğrudur?',
 sekil=SK4,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargı.',
 ip=['Yüklü bir cismin hangi tür moleküllere etki edeceğini düşün.'],
 bilgi=[B('Polar ve apolar moleküller','Polar moleküllerde kalıcı dipol vardır ve yüklü cisimle etkileşir; apolar moleküllerde kalıcı dipol yoktur. Benzer benzeri çözer: polar sıvı polar sıvıda, apolar sıvı apolar sıvıda çözünür')],
 puf='Yüklü cismin hangi moleküllerin yönünü değiştirebileceğini düşün.')

# ============================================================ 05 · metanol–dimetil eter (orta, şekil)
def mol(yo,atoms,bonds):
    s=''
    for (x1,y1),(x2,y2) in bonds: s+=f'\\draw[shorten >=.16cm,shorten <=.16cm] ({x1},{y1+yo}) -- ({x2},{y2+yo});'
    for (x,y),t in atoms: s+=f'\\node[font=\\small] at ({x},{y+yo}) {{{t}}};'
    return s
C1=(1.5,1.0); O=(2.3,1.0)
CK=(2.3,1.0); OK=(3.1,1.0)
Ka=[(C1,'C'),((1.5,1.8),'H'),((1.5,.2),'H'),((.7,1.0),'H'),(CK,'C'),((2.3,1.8),'H'),((2.3,.2),'H'),(OK,'O'),((3.9,1.0),'H')]
Kb=[(C1,(1.5,1.8)),(C1,(1.5,.2)),(C1,(.7,1.0)),(C1,CK),(CK,(2.3,1.8)),(CK,(2.3,.2)),(CK,OK),(OK,(3.9,1.0))]
C2=(3.1,1.0)
La=[(C1,'C'),((1.5,1.8),'H'),((1.5,.2),'H'),((.7,1.0),'H'),(O,'O'),(C2,'C'),((3.1,1.8),'H'),((3.1,.2),'H'),((3.9,1.0),'H')]
Lb=[(C1,(1.5,1.8)),(C1,(1.5,.2)),(C1,(.7,1.0)),(C1,O),(O,C2),(C2,(3.1,1.8)),(C2,(3.1,.2)),(C2,(3.9,1.0))]
g=mol(0,Ka,Kb)+mol(-2.7,La,Lb)
g+='\\node[font=\\bfseries] at (0,1.0) {K}; \\node[font=\\bfseries] at (0,-1.7) {L};'
g+='\\node[anchor=west,font=\\small] at (4.6,1.0) {Kaynama noktası: 78 $^\\circ$C}; \\node[anchor=west,font=\\small] at (4.6,-1.7) {Kaynama noktası: $-24\\,^\\circ$C};'
SK5=tk(g)
dg=('K moleküllerinde O atomuna bağlı H atomu bulunur; bu nedenle K molekülleri arasında hidrojen bağı oluşur.','H atomu O’ya bağlıysa hidrojen bağı kurulabilir ve kaynama noktası yükselir')
yl=[('L molekülleri arasında hidrojen bağı bulunur, K’de yalnız London kuvvetleri vardır.','H atomu O’ya bağlı olan K’dir; L’de H yalnız C’ye bağlıdır, hidrojen bağı kuramaz'),
    ('İki maddenin molekül formülü aynı olduğundan kaynama noktaları da aynı olmalıdır.','aynı molekül formülü, aynı etkileşim demek değildir; hidrojen bağı yapabilen K’nin kaynama noktası daha yüksektir'),
    ('L’nin kaynama noktasının düşük olması C–O bağlarının zayıf olmasındandır.','kaynama sırasında molekül içi bağlar değil, moleküller arası etkileşimler zayıflar'),
    ('K’nin kaynama noktasının yüksek olması, K’deki bağların iyonik karakterde olmasındandır.','K’deki bütün bağlar kovalenttir; fark moleküller arası hidrojen bağındandır')]
r=tek_t(dg,yl,1,True)
q('0005',ad=[A('Formülleri incele','İki molekülün atomları aynı (C₂H₆O) ama bağlanma biçimi farklıdır.','K: H₃C–CH₂–OH; L: H₃C–O–CH₃'),A('Hidrojen bağı koşulu','H atomu N, O ya da F’ye bağlı olmalıdır.','K: O–H var → H bağı · L: O–H yok'),A('Kaynama noktasıyla ilişkilendir','Hidrojen bağı yapan maddenin molekülleri arasındaki çekim daha güçlüdür.','K: 78 °C > L: −24 °C'),A('Yargıları sına','Her yargı bu açıklamayla karşılaştırılır.','Doğru yargı: K’de H bağı var')],
 alt='Zayıf Etkileşimler',z='orta',kaz='Açık formülden hidrojen bağı yapabilme koşulunu değerlendirip kaynama noktalarını yorumlar.',kalip='şekilli',ne='K ve L açık formülleri, 78 ve −24 °C',
 metin='K ve L sıvıları aynı molekül formülüne (C₂H₆O) sahip iki farklı maddedir. Bu maddelerin açık formülleri ve 1 atm basınçtaki kaynama noktaları şekilde verilmiştir. Öğretmen, iki maddenin kaynama noktaları arasındaki farkın nedenini sorar.\nBuna göre aşağıdakilerden hangisi doğrudur?',
 sekil=SK5,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargı.',
 ip=['Her molekülde H atomunun hangi atoma bağlı olduğuna bak.'],
 bilgi=[B('Hidrojen bağı koşulu','Hidrojen bağı için molekülde N, O ya da F atomuna bağlı bir H atomu bulunmalıdır. Bu bağı yapabilen madde, benzer büyüklükteki diğerlerinden daha yüksek sıcaklıkta kaynar. Örnek: NH₃ hidrojen bağı yapar, CH₄ yapamaz')],
 puf='H, N–O–F’ye bağlıysa hidrojen bağı yapılır; aynı formül aynı kaynama noktası demek değildir.')

# ============================================================ 06 · iyonik bileşik erime noktası (zor, öncüllü, tablo)
ION=[('Na⁺','+1',102),('K⁺','+1',138),('Ca²⁺','+2',100),('F⁻','−1',133),('Cl⁻','−1',181),('Br⁻','−1',196),('O²⁻','−2',140)]
SK6=tablo_svg(['İyon','Yük','Yarıçap (pm)'],[[a,b,str(c)] for a,b,c in ION])
rad={a:c for a,b,c in ION}; yk={'Na⁺':1,'K⁺':1,'Ca²⁺':2,'F⁻':-1,'Cl⁻':-1,'Br⁻':-1,'O²⁻':-2}
def kuvvet(k,a): return Fr(yk[k]*(-yk[a]),rad[k]+rad[a])
assert kuvvet('Na⁺','Cl⁻')>kuvvet('K⁺','Cl⁻') and kuvvet('Ca²⁺','O²⁻')>kuvvet('K⁺','F⁻') and kuvvet('K⁺','F⁻')>kuvvet('K⁺','Cl⁻') and kuvvet('Na⁺','Cl⁻')>kuvvet('Na⁺','Br⁻')
d={'I':(False,'iyon yükleri eşittir ama K⁺ (138 pm), Na⁺’dan (102 pm) büyüktür; iyonlar arası uzaklık arttığından KCl’nin erime noktası NaCl’den düşüktür'),
   'II':(True,'CaO’da yükler +2 ve −2, KF’de +1 ve −1’dir; yük çarpımı çok büyük olduğundan CaO’nun erime noktası daha yüksektir'),
   'III':(True,'yükler eşit; F⁻ (133 pm), Cl⁻’dan (181 pm) küçüktür; iyonlar arası uzaklık azaldığından KF’nin erime noktası KCl’den yüksektir')}
r=onc_t(d,3)
q('0006',ad=[A('Tabloyu oku','Yük ve yarıçaplar karşılaştırma için kullanılır.','Na⁺ 102 · K⁺ 138 · F⁻ 133 · Cl⁻ 181 · Br⁻ 196'),adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),A('Sonucu yaz','Doğru olan öncüller bir arada yazılır.',oy(d)+' · Sonuç: '+r['dogru'])],
 alt='Güçlü Etkileşimler',z='orta',kaz='İyon yükü ve yarıçapına göre iyonik bileşiklerin erime noktalarını karşılaştırır.',kalip='öncüllü',ne='yedi iyonun yük ve yarıçap tablosu',
 metin='Aynı kristal düzenine sahip iyonik bileşiklerin erime noktası, iyonlar arasındaki çekim kuvvetine bağlıdır. Bu kuvvet iyon yükleri büyüdükçe artar, iyonların yarıçapları (dolayısıyla aralarındaki uzaklık) büyüdükçe azalır. Bazı iyonların yük ve yarıçapları tabloda verilmiştir.\nI. KCl’nin erime noktası NaCl’den yüksektir.\nII. CaO’nun erime noktası KF’den yüksektir.\nIII. KF’nin erime noktası KCl’den yüksektir.\nBuna göre hangileri doğrudur?',
 sekil=SK6,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan öncüller.',
 ip=['Karşılaştırdığın iki bileşikte yükler mi, yarıçaplar mı farklı? Önce bunu belirle.'],
 bilgi=[B('İyonik bileşik ve erime noktası','İyonlar arası çekim kuvveti yüklerin çarpımıyla doğru, iyonlar arası uzaklıkla ters orantılıdır. Çekim büyükse bileşiğin erime noktası yüksektir. Örnek: aralarındaki uzaklık aynıysa +3 ve −1 yüklü iyonlar arasındaki çekim, +1 ve −1 yüklü iyonlar arasındakinden büyüktür')],
 puf='Karşılaştırırken bir etkeni (yük ya da boyut) eşit tut; çekim büyükse erime noktası yüksektir.')

# ============================================================ 07 · 2. periyot erime noktaları (orta, grafik)
EL=[('Li',181),('Be',1287),('C',3550),('N₂',-210),('O₂',-218),('F₂',-220),('Ne',-249)]
Sy7=.0011
g=''
for v in (1000,2000,3000): g+=f'\\draw[black!15] (0,{v*Sy7:.2f}) -- (6.8,{v*Sy7:.2f});'
g+=f'\\draw[thick,{ARR}] (0,0) -- (7.0,0); \\draw[thick,{ARR}] (0,-.4) -- (0,4.2);'
for v in (0,1000,2000,3000): g+=f'\\draw (0,{v*Sy7:.2f}) -- (-.08,{v*Sy7:.2f}) node[left,font=\\footnotesize] {{{v}}};'
g+='\\node[above,font=\\footnotesize] at (0.5,4.2) {Erime noktası ($^\\circ$C)};'
for i,(nm,v) in enumerate(EL):
    x=.5+i*.92; y=v*Sy7
    g+=f'\\draw[fill=vurgu!30,thick] ({x-.3:.2f},0) rectangle ({x+.3:.2f},{y:.3f});'
    g+=f'\\node[font=\\small\\bfseries] at ({x:.2f},-.65) {{{"\\ce{"+nm.replace("₂","2")+"}" if "₂" in nm else nm}}};'
SK7=tk(g)
v={n:t for n,t in EL}
assert v['Li']<v['Be']<v['C'] and max(v['N₂'],v['O₂'],v['F₂'],v['Ne'])<0
dg=('Li’dan C’ye erime noktasının artması, metalik bağdan kovalent ağ yapıya geçişle ilişkilidir.','Li ve Be metalik bağlıdır (değerlik elektronu artınca bağ güçlenir); elmas (C) ağ biçiminde kovalent bağlıdır ve çok yüksek erime noktalıdır')
yl=[('N₂, O₂ ve F₂’nin erime noktalarının düşük olması, molekül içi kovalent bağların zayıf olmasındandır.','erimede molekül içi bağlar kopmaz; düşük erime noktası zayıf London kuvvetlerinden kaynaklanır'),
    ('Ne’nin erime noktasının düşük olması, atomları arasında kovalent bağ bulunmasındandır.','Ne tek atomlu bir soy gazdır; atomları arasında yalnızca London kuvvetleri vardır'),
    ('Be’nin erime noktasının Li’dan yüksek olması, Be’nin daha az değerlik elektronu bulunmasındandır.','Be’nin 2 değerlik elektronu vardır (Li’nin 1’i); değerlik elektronu arttıkça metalik bağ güçlenir'),
    ('C’nin yüksek erime noktası, moleküller arası London kuvvetlerinin güçlü olmasındandır.','C (elmas) moleküllerden değil, kovalent bağlarla ağ biçiminde bağlı atomlardan oluşur')]
r=tek_t(dg,yl,4,True)
q('0007',ad=[A('Grafiği oku','Li ve Be’nin erime noktaları orta düzeyde; C çok yüksek; N₂, O₂, F₂ ve Ne çok düşüktür.','Li: 181 · Be: 1287 · C: 3550 · diğerleri < 0'),A('Yapıları eşleştir','Li, Be metalik; C kovalent ağ; N₂, O₂, F₂ moleküler, Ne tek atomlu soy gazdır.','Metalik → kovalent ağ → London kuvvetleri'),A('Yargıları sına','Her yargı bu yapı–özellik eşlemesiyle karşılaştırılır.','Doğru yargı: Li→C artışı yapı değişimidir')],
 alt='Güçlü Etkileşimler',z='orta',kaz='Erime noktası–element grafiğini bağ türü ve yapıyla ilişkilendirir.',kalip='grafik',ne='Li, Be, C, N₂, O₂, F₂, Ne erime noktaları',
 metin='Atom numarası 3 ile 10 arasında olan ve 2. periyotta bulunan bazı maddelerin 1 atm basınçta erime noktaları grafikte verilmiştir. Grafikte karbon, elmas hâlindeki kovalent ağ yapısıyla gösterilmiş; azot, oksijen ve flor ise iki atomlu moleküller olarak yer almıştır.\nBuna göre aşağıdakilerden hangisi doğrudur?',
 sekil=SK7,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargı.',
 ip=['Her maddenin yapı taşını ve erimede zayıflayan etkileşimi düşün.'],
 bilgi=[B('Yapı ve erime noktası','Metalik bağ değerlik elektronu arttıkça güçlenir; kovalent ağ katılarda erime için kovalent bağlar koparıldığından erime noktası çok yüksektir; moleküler maddeler ile soy gazlarda yalnız zayıf London kuvvetleri zayıfladığından erime noktası düşüktür')],
 puf='Erime noktasını yapı taşı ve erimede zayıflayan etkileşim belirler.')

# ============================================================ 08 · kopan etkileşimler (orta, tablo, olumsuz kök)
SATIR=[('Kuru buzun (katı CO₂) süblimleşmesi','London kuvvetleri',True),('Yemek tuzunun (NaCl) erimesi','İyonik bağ',True),('Demirin erimesi','Metalik bağ',True),('Suyun elektrolizle H₂ ve O₂’ye ayrışması','London kuvvetleri',False),('Amonyağın (NH₃) sıvıdan buharlaşması','Hidrojen bağı',True)]
SK8=tablo_svg(['Olay','Kopan ya da zayıflayan etkileşim'],[[a,b] for a,b,_ in SATIR])
assert sum(1 for *_,ok in SATIR if not ok)==1
ACK={'Kuru buzun süblimleşmesi':'süblimleşmede CO₂ moleküllerini bir arada tutan London kuvvetleri zayıflar','Yemek tuzunun erimesi':'NaCl erirken iyonları tutan iyonik bağlar zayıflar','Demirin erimesi':'metalik bağ zayıflar','Amonyağın buharlaşması':'NH₃ molekülleri arasındaki hidrojen bağları zayıflar'}
op=['Kuru buzun süblimleşmesi','Yemek tuzunun erimesi','Demirin erimesi','Suyun elektrolizi','Amonyağın buharlaşması']
dogru8='Suyun elektrolizi'
q('0008',ad=[A('Her satırı sına','Olayın fiziksel mi kimyasal mı olduğuna bakılır; fiziksel değişimde moleküller arası etkileşimler, iyonik ve metalik katılarda iyonik ve metalik bağ zayıflar.','Süblimleşme, erime, buharlaşma: fiziksel'),A('Elektrolizi incele','Elektrolizde su molekülleri H₂ ve O₂’ye ayrışır; bu kimyasal değişimde H–O kovalent bağları kopar.','Kopan: kovalent bağ'),A('Sonucu yaz','Tabloda London kuvvetleri yazılan satır kimyasal olaya ait olduğundan yanlıştır.','Yanlış satır: suyun elektrolizi')],
 alt='Güçlü ve Zayıf Etkileşimler',z='kolay',kaz='Fiziksel ve kimyasal olaylarda hangi etkileşimlerin koptuğunu ayırt eder.',kalip='tablo',ne='beş olay ve kopan etkileşimler tablosu',
 metin='Bir öğrenci, günlük hayattan ve laboratuvardan beş olayı, bu olaylarda kopan ya da zayıflayan etkileşim türüyle birlikte tabloda göstermiştir. Öğretmeni, satırlardan birinde etkileşimin yanlış yazıldığını söylüyor.\nBuna göre hangi olay için yazılan etkileşim yanlıştır?',
 sekil=SK8,dogru=dogru8,sira=op,yan=[(o,'Bu olayın satırını yanlış sanmış; oysa '+ACK[o]+'.','bilgi') for o in op if o!=dogru8],
 istenen='Etkileşimi yanlış yazılan olay.',ip=['Her olayda tanecik düzeyinde ne olduğunu düşün.'],
 bilgi=[B('Fiziksel ve kimyasal değişim','Fiziksel değişimde maddenin kimliği değişmez; yalnız taneciklerin dizilişi ve aralarındaki etkileşim değişir. Kimyasal değişimde atomlar arasındaki bağlar kopar, yenileri oluşur')],
 puf='Hâl değişiminde molekül içi bağ kopmaz; kimyasal ayrışmada kopar.')

# ============================================================ 09 · bağ polarlığı (kolay, hikâyeli)
EN={'H':Fr(21,10),'C':Fr(25,10),'N':Fr(3),'O':Fr(35,10),'F':Fr(4),'Cl':Fr(32,10)}
fark=lambda a,b:abs(EN[a]-EN[b])
B9={'N–H':fark('N','H'),'O–H':fark('O','H'),'C–F':fark('C','F'),'C–Cl':fark('C','Cl'),'N–Cl':fark('N','Cl')}
assert max(B9,key=B9.get)=='C–F' and B9['N–Cl']==Fr(2,10) and B9['O–H']==Fr(14,10) and B9['C–F']==Fr(15,10)
dg=('C–F bağı','elektronegatiflik farkı 4,0 − 2,5 = 1,5 ile en büyüktür')
yl=[('N–H bağı','elektronegatiflik farkı 3,0 − 2,1 = 0,9’dur, C–F’nin farkı (1,5) daha büyüktür'),('O–H bağı','elektronegatiflik farkı 3,5 − 2,1 = 1,4’tür; C–F’nin farkı (1,5) bundan büyüktür'),('C–Cl bağı','elektronegatiflik farkı 3,2 − 2,5 = 0,7’dir, en polar değildir'),('N–Cl bağı','elektronegatiflik farkı 3,2 − 3,0 = 0,2’dir; fark küçüktür, en polar değildir')]
r=tek_t(dg,yl,2,True)
q('0009',ad=[A('Farkları hesapla','Bağın polarlığı, atomların elektronegatiflik farkına bağlıdır.','N–H: 0,9 · O–H: 1,4 · C–F: 1,5 · C–Cl: 0,7 · N–Cl: 0,2'),A('Karşılaştır','Fark büyüdükçe bağ daha polardır.','1,5 > 1,4 > 0,9 > 0,7 > 0,2'),A('Sonucu yaz','En büyük farka sahip bağ en polar olandır.','En polar: C–F')],
 alt='Bağ Polarlığı',z='kolay',kaz='Elektronegatiflik farkına göre bağların polarlığını karşılaştırır.',kalip='hikâyeli',ne='H, C, N, O, F, Cl elektronegatiflikleri',
 metin='Bir öğrenci, kimya dersinde bağların polarlığını karşılaştırmak için bazı elementlerin elektronegatiflik değerlerini defterine yazmıştır: H: 2,1; C: 2,5; N: 3,0; O: 3,5; F: 4,0; Cl: 3,2. Öğretmeni, bağ yapan iki atomun elektronegatiflik farkı büyüdükçe bağın daha polar olduğunu hatırlatıyor.\nBuna göre aşağıdaki bağlardan hangisi en polardır?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='En polar bağ.',
 ip=['Her bağ için iki atomun elektronegatiflik farkını bul ve karşılaştır.'],
 bilgi=[B('Bağ polarlığı','İki atom arasındaki elektronegatiflik farkı büyüdükçe bağ elektronları daha çok elektronegatif atoma çekilir ve bağ daha polar olur. Aynı elektronegatifliğe sahip atomlar arasındaki bağ apolardır. Örnek: H₂’deki bağ apolar, H–Cl bağı polardır')],
 puf='Bağın polarlığı için elektronegatiflik farkına bak; en büyük fark en polar bağdır.')

# ============================================================ 10 · Bohr modeli ve bileşik oluşumu (zor, öncüllü, şekil)
ATOM={'X':[2,8,2],'Y':[2,6],'Z':[2,8,7]}
def bohr(x0,sayi,kat):
    s=f'\\draw[fill=white] ({x0},0) circle (.3); \\node[font=\\scriptsize] at ({x0},0) {{+{sayi}}};'
    for i,n in enumerate(kat):
        r_=.62+.32*i; s+=f'\\draw[black!50] ({x0},0) circle ({r_});'
        for k in range(n):
            a=2*math.pi*k/n+i*.5; s+=f'\\fill ({x0+r_*math.cos(a):.2f},{r_*math.sin(a):.2f}) circle (.055);'
    return s
g=''
for nm,x0 in zip('XYZ',(0,3.3,6.6)):
    kat=ATOM[nm]; g+=bohr(x0,sum(kat),kat)+f'\\node[font=\\bfseries] at ({x0},-1.65) {{{nm}}};'
SK10=tk(g)
assert sum(ATOM['X'])==12 and ATOM['X'][-1]==2 and ATOM['Y'][-1]==6 and ATOM['Z'][-1]==7
d={'I':(False,'X 2 elektron verip X²⁺, Y 2 elektron alıp Y²⁻ olur; yükler eşit olduğundan formül XY’dir, XY₂ değildir'),
   'II':(True,'Z’nin 7 değerlik elektronu vardır; Z atomları 1 elektron alarak Z⁻ iyonuna dönüşür (XZ₂ bileşiğinde)'),
   'III':(False,'Y ve Z iki ametaldir; elektron aktarımı değil, elektron ortaklığıyla kovalent bağ oluşur')}
r=onc_t(d,0)
q('0010',ad=[A('Katmanları say','Son katmandaki elektron sayısı değerlik elektronudur.','X: 2 · Y: 6 · Z: 7'),A('Türleri belirle','X metaldir (elektron verir); Y ve Z ametaldir (elektron alır ya da ortaklaşa kullanır).','X: X²⁺ · Y: Y²⁻ · Z: Z⁻'),adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),A('Sonucu yaz','Doğru olan öncüller bir arada yazılır.',oy(d)+' · Sonuç: '+r['dogru'])],
 alt='Güçlü Etkileşimler',z='orta',kaz='Katman diyagramından değerlik elektronlarını bulup oluşan bileşiklerin formülünü ve bağ türünü yorumlar.',kalip='öncüllü',ne='X, Y, Z atomlarının katman dizilimleri',
 metin='Şekilde X, Y ve Z atomlarının katman (Bohr) modelleri verilmiştir; çekirdekteki sayı proton sayısını, noktalar elektronları göstermektedir (harfler gerçek element sembolü değildir).\nI. X ile Y’nin oluşturduğu bileşiğin formülü XY₂’dir.\nII. X ile Z’nin oluşturduğu bileşikte Z atomları elektron alır.\nIII. Y ile Z arasında oluşan bileşikte atomlar elektron aktarımıyla bağlanır.\nBuna göre hangileri doğrudur?',
 sekil=SK10,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan öncüller.',
 ip=['Her atomun son katmanındaki elektron sayısına bakarak metal ya da ametal olduğunu belirle.'],
 bilgi=[B('Katman diyagramı','Son katmandaki elektron sayısı değerlik elektronu sayısıdır. Az değerlik elektronlu metaller elektron verir, çok değerlik elektronlu ametaller elektron alır. İki ametal elektronlarını ortaklaşa kullanır')],
 puf='Son katmandaki elektronlar bağın türünü belirler: metal verir, ametal alır ya da ortaklaşa kullanır.')

bitir(P,'etkilesimuc',UK)
