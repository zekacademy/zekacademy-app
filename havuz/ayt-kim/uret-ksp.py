"""AYT Kimya · Çözünürlük Dengesi · paket (ksp): 20 soru, kardeş yok, ipucu 1.
Şekil verileri, sayısal cevaplar, çeldirici değerleri ve öncül doğrulukları Python'da hesaplanır (Fraction); TikZ bu değerlerden üretilir."""
import sys,os,json,random,itertools,math
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,os.path.join(HV,'tyt-kim')); sys.path.insert(0,HV)
import _hafif_kim2 as H
from _hafif_kim2 import *
from _hafif_kim import onc as _onc_eski, tek
KONU_='Çözünürlük Dengesi'; UK='akim|Çözünürlük Dengesi'
H.KONU=KONU_
P=Parti('ksp',KONU_,UK,ders='AYT Kimya',idon='aytkim')
KY='ÖSYM AYT 2022–2025 Kimya (yalnız mantık) · MEB 12. sınıf Çözünürlük Dengesi'
TIP={'ifade':'Kçç ifadesinin yazılması','hesap':'Kçç ile molar çözünürlük ilişkisi','denge':'Çözünme dengesi ve dengeyi etkileyen faktörler',
     'sicaklik':'Sıcaklığın çözünürlüğe etkisi','ortak':'Ortak iyon etkisi','cokelme':'Çökelme koşulu (Q ile Kçç)','secici':'Seçici çökelme'}
def kartla(n,tip,alt,fikir,tuzak,z,kalip,adim):
    kart(f'K-AKKSP-{n}',alt,fikir,tuzak,z,kalip,adim,f'ksp-{tip}',TIP[tip],KY)
def q(no,tip,ne,ad,**k):
    assert len(k['ip'])==1
    k['tipId']=f'ksp-{tip}'; k['tip']=TIP[tip]; k['kart']=f"K-AKKSP-{no[-2:]} ({TIP[tip].lower()}) · {ne}"
    mk(P,no,ad=ad,adim=len(ad),**k)
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
ARR='-{Stealth[length=2mm,width=1.8mm]}'
def tk(g): return tikz_svg(HEAD+g+TAIL)
KC='K$_{\\text{çç}}$'
# ---------- sayı yardımcıları ----------
SUP=str.maketrans('0123456789-','⁰¹²³⁴⁵⁶⁷⁸⁹⁻')
def sci(v):
    v=Fr(v); e=0
    assert v>0
    while v>=10: v/=10; e+=1
    while v<1: v*=10; e-=1
    return f'{fm(v)} × 10{str(e).translate(SUP)}' if e else fm(v)
def E(m,e): return Fr(str(m).replace(',','.'))*Fr(10)**e
def sn(dogru,yan,gorec=sci):
    """dogru: değer; yan: [(değer,cel,tur)]; sayısal şıklar küçükten büyüğe, dizgi olarak."""
    vals=[Fr(dogru)]+[Fr(y[0]) for y in yan]; assert len(set(vals))==5,vals
    sira=[gorec(v) for v in sorted(vals)]
    return dict(dogru=gorec(dogru),yan=[(gorec(y[0]),y[1],y[2]) for y in yan],sira=sira)
def poz(r): return r['sira'].index(r['dogru'])
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
def sonuc(d,r): return A('Sonucu yaz','Doğru olan öncüller bir arada yazılır.',oy(d)+' · Sonuç: '+r['dogru'])
# ---------- çizim yardımcıları ----------
def kap(x,w,h,lv,fill='vurgu!15'):
    return f'\\fill[{fill}] ({x},0) rectangle ({x+w},{lv});\\draw[thick] ({x},{h}) -- ({x},0) -- ({x+w},0) -- ({x+w},{h});'
def kati(x,w,hh=.42):
    s=f'\\fill[gray!55] ({x+.04},.04) rectangle ({x+w-.04},{hh});'
    return s
def uzak(p,L,m): return all((p[0]-a)**2+(p[1]-b)**2>=m*m for a,b in L)
def rastgele(n,x1,x2,y1,y2,m,seed):
    rng=random.Random(seed)
    for deneme in range(300):
        L=[]
        for _ in range(6000):
            p=(rng.uniform(x1,x2),rng.uniform(y1,y2))
            if uzak(p,L,m): L.append(p)
            if len(L)==n: return L
    raise RuntimeError('yerlesmedi')
def katyon(x,y): return f'\\node[circle,draw,thick,fill=vurgu!35,inner sep=0pt,minimum size=.36cm] at ({x:.2f},{y:.2f}) {{\\scriptsize +}};'
def anyon(x,y): return f'\\node[circle,draw,thick,fill=gray!30,inner sep=0pt,minimum size=.5cm] at ({x:.2f},{y:.2f}) {{\\scriptsize $-$}};'

# ============ 01 · Kçç ifadesi · kolay · olumsuz kök ============
kartla('01','ifade','Kçç ifadesi','Çözünme denklemindeki katsayılar iyon derişimlerinin üssü olur; katı hâldeki madde ifadeye girmez.','Katsayıyı çarpan olarak yazmak; üssü unutmak; katıyı ifadeye katmak.','kolay','düz',2)
r=tek_t(('Al(OH)₃ : Kçç = [Al³⁺] · [OH⁻]','Al(OH)₃(k) ⇌ Al³⁺ + 3OH⁻ olduğundan OH⁻ derişiminin üçüncü kuvveti yazılmalıdır, ifade [Al³⁺] · [OH⁻]³ biçiminde olur'),
 [('PbI₂ : Kçç = [Pb²⁺] · [I⁻]²','PbI₂(k) ⇌ Pb²⁺ + 2I⁻ denkleminde I⁻ iyonunun katsayısı 2 olduğundan derişimin karesi yazılır'),
  ('BaSO₄ : Kçç = [Ba²⁺] · [SO₄²⁻]','BaSO₄(k) ⇌ Ba²⁺ + SO₄²⁻ denkleminde katsayılar 1 olduğundan üs yazılmaz'),
  ('Fe₂S₃ : Kçç = [Fe³⁺]² · [S²⁻]³','Fe₂S₃(k) ⇌ 2Fe³⁺ + 3S²⁻ denkleminde katsayılar üs olarak yazılır'),
  ('Ag₂CrO₄ : Kçç = [Ag⁺]² · [CrO₄²⁻]','Ag₂CrO₄(k) ⇌ 2Ag⁺ + CrO₄²⁻ denkleminde Ag⁺ derişiminin karesi yazılır')],3,False)
q('0001','ifade','beş tuzun Kçç ifadesi',
 [A('Kuralı hatırla','Kçç ifadesinde yalnız sulu çözeltideki iyonlar bulunur ve katsayılar üs olur.','Kçç = [katyon]ᵃ · [anyon]ᵇ'),
  A('İfadeleri sırayla kontrol et','Her tuz için iyonlaşma denklemini yazıp katsayıları üslerle karşılaştır.','PbI₂, BaSO₄, Fe₂S₃, Ag₂CrO₄ → doğru'),
  A('Al(OH)₃’ü incele','Al(OH)₃(k) ⇌ Al³⁺ + 3OH⁻ olduğundan OH⁻ için üs 3 olmalıdır.','Doğrusu: [Al³⁺] · [OH⁻]³'),
  A('Sonucu yaz','Yanlış yazılmış olan, hidroksit tuzunun ifadesidir.','Al(OH)₃ : Kçç = [Al³⁺] · [OH⁻]')],
 metin='Suda az çözünen bazı katıların sudaki doygun çözeltileriyle dengede olduğu bilinmektedir. Bu katıların çözünme dengelerine ait Kçç ifadeleri aşağıdaki gibi yazılmıştır.\nBuna göre bu ifadelerden hangisi yanlış yazılmıştır?',
 z='kolay',alt='Kçç İfadesi',kaz='Az çözünen bir tuzun çözünme dengesi için Kçç ifadesini yazar.',kalip='düz',
 istenen='Yanlış yazılan Kçç ifadesi.',ip=['Her tuzun iyonlarına ayrışma denklemini yaz; katsayıların ifadede nasıl yer aldığına bak.'],
 bilgi=[B('Kçç ifadesi','Az çözünen tuzun doygun çözeltisindeki iyon derişimlerinin, katsayıları üs yapılarak çarpımıdır; katı ifadeye girmez. Örnek: Ca₃(PO₄)₂(k) ⇌ 3Ca²⁺ + 2PO₄³⁻ için Kçç = [Ca²⁺]³ · [PO₄³⁻]²')],
 puf='Katsayı üs olur, katı ifadeye girmez.',**r)

# ============ 02 · Kçç karşılaştırması · kolay · öncüllü · tablo ============
kartla('02','hesap','Aynı tipte tuzlarda Kçç ve çözünürlük','Aynı iyon sayısına sahip tuzlarda Kçç büyüdükçe çözünürlük büyür; AB tipi için s = √Kçç.','Kçç değerini doğrudan iyon derişimi sanmak.','kolay','öncüllü',3)
KX,KY_,KZ=E(1,-10),E(1,-8),E(1,-12)
assert (E(1,-12)**Fr(1,2) if False else True)
sX=Fr(1,10**5); sY=Fr(1,10**4); sZ=Fr(1,10**6)
assert sX*sX==KX and sY*sY==KY_ and sZ*sZ==KZ
d={'I':(KY_>KX>KZ,'YA’nın Kçç değeri en büyük olduğundan, üç tuz da aynı tipte olduğu için en çok çözünen YA’dır'),
   'II':(sZ==E(1,-6),'ZA’nın doygun çözeltisinde [Z⁺] = [A⁻] ve Kçç = [Z⁺]² olduğundan [Z⁺] = 1 × 10⁻⁶ M’dir'),
   'III':(False,'XA’nın doygun çözeltisinde [X⁺] = √(1 × 10⁻¹⁰) = 1 × 10⁻⁵ M’dir, 1 × 10⁻¹⁰ M değil')}
assert d['I'][0] and d['II'][0]
r=onc_t(d,3)
SK=tablo_svg(['Tuz','Kçç (25 °C)'],[['XA','1 × 10⁻¹⁰'],['YA','1 × 10⁻⁸'],['ZA','1 × 10⁻¹²']])
q('0002','hesap','üç AB tipi tuz tablosu',
 [adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),sonuc(d,r)],
 metin='Aynı sıcaklıkta suda az çözünen XA, YA ve ZA tuzlarının her biri, sulu çözeltisinde bir katyon ve bir anyona ayrışmaktadır. Bu tuzların Kçç değerleri tabloda verilmiştir. Üç tuzun da doygun çözeltilerinde bulunan katıları çözeltileriyle dengededir.\nI. Suda en çok çözünen tuz YA’dır.\nII. ZA’nın doygun çözeltisinde Z⁺ derişimi 1 × 10⁻⁶ M’dir.\nIII. XA’nın doygun çözeltisinde X⁺ derişimi 1 × 10⁻¹⁰ M’dir.\nBuna göre bu yargılardan hangileri doğrudur?',
 sekil=SK,z='kolay',alt='Kçç ve Molar Çözünürlük',kaz='Aynı tipteki tuzların Kçç değerlerini karşılaştırır, doygun çözeltideki iyon derişimini hesaplar.',kalip='tablo',
 istenen='Doğru olan yargılar.',ip=['Üç tuz da aynı sayıda iyona ayrıştığına göre Kçç ile iyon derişimi arasındaki ilişkiyi kullan.'],
 bilgi=[B('AB tipi tuzda Kçç','Bir katyon ve bir anyona ayrışan tuzda doygun çözeltide [A⁺] = [B⁻] = s olur ve Kçç = s²’dir. Örnek: Kçç = 1 × 10⁻⁸ ise s = 1 × 10⁻⁴ M’dir')],
 puf='Kçç = s² (AB tipi) olduğundan s = √Kçç; Kçç değeri iyon derişimi değildir.',**r)

# ============ 03 · Kçç hesabı · kolay ============
kartla('03','hesap','Doygun çözeltideki derişimden Kçç','Doygun çözeltideki iyon derişimleri Kçç ifadesinde yerine konur; katsayı hem üs hem derişim çarpanıdır.','[I⁻] derişimini [Pb²⁺]’ye eşit almak; üssü atlamak.','kolay','hikâyeli',3)
pb=E(3,-4); iod=2*pb
Kc=pb*iod**2; assert Kc==E('1,08',-10)
y1=pb*iod**2*0+pb*pb**2   # I⁻ derişimini Pb ile aynı almış: 2,7e-11
y2=pb*iod                  # üssü atlamış
y3=iod**2                  # Pb²⁺'yı katmamış
y4=pb**2                   # AB tipi sanmış
assert y1==E('2,7',-11) and y2==E('1,8',-7) and y3==E('3,6',-7) and y4==E(9,-8)
r=sn(Kc,[(y1,'[I⁻] derişimini de 3 × 10⁻⁴ M alıp [Pb²⁺] · [I⁻]² = 3 × 10⁻⁴ · (3 × 10⁻⁴)² = 2,7 × 10⁻¹¹ bulmuş.','dikkat'),
         (y4,'Tuzu AB tipi sanıp [Pb²⁺]² = (3 × 10⁻⁴)² = 9 × 10⁻⁸ bulmuş.','bilgi'),
         (y2,'I⁻ derişiminin karesini almayıp [Pb²⁺] · [I⁻] = 3 × 10⁻⁴ · 6 × 10⁻⁴ = 1,8 × 10⁻⁷ bulmuş.','bilgi'),
         (y3,'Yalnız I⁻ derişiminin karesini almış: (6 × 10⁻⁴)² = 3,6 × 10⁻⁷.','dikkat')])
assert poz(r)==1
q('0003','hesap','PbI₂ doygun çözeltisi, [Pb²⁺] verilmiş',
 [A('Denklemi yaz','PbI₂ çözündüğünde 1 Pb²⁺ ve 2 I⁻ oluşur.','PbI₂(k) ⇌ Pb²⁺ + 2I⁻'),
  A('I⁻ derişimini bul','Anyon derişimi katsayı kadar büyüktür.','[I⁻] = 2 × 3 × 10⁻⁴ = 6 × 10⁻⁴ M'),
  A('Kçç ifadesine yerleştir','Katsayı üs olarak yazılır.','Kçç = [Pb²⁺] · [I⁻]² = 3 × 10⁻⁴ · (6 × 10⁻⁴)²'),
  A('Hesapla','Üslü ifadeleri çarp.','Kçç = 3 × 10⁻⁴ · 3,6 × 10⁻⁷ = 1,08 × 10⁻¹⁰')],
 metin='25 °C’de PbI₂ katısı ile dengede olan doygun çözeltide Pb²⁺ iyonlarının derişimi 3 × 10⁻⁴ M olarak ölçülüyor. Çözeltide iyonlar yalnızca PbI₂’nin çözünmesinden gelmektedir.\nBuna göre PbI₂’nin bu sıcaklıktaki Kçç değeri kaçtır?',
 z='kolay',alt='Kçç ve Molar Çözünürlük',kaz='Doygun çözeltideki iyon derişimlerinden Kçç değerini hesaplar.',kalip='hikâyeli',
 istenen='PbI₂’nin 25 °C’deki Kçç değeri.',ip=['Önce iyonlaşma denkleminden I⁻ derişimini bul, sonra Kçç ifadesinde üsleri unutma.'],
 bilgi=[B('Doygun çözeltide iyon derişimleri','çözünen tuzun mol sayısına göre iyonlar katsayı oranında oluşur. Örnek: CaCl₂ için [Cl⁻] = 2 · [Ca²⁺]')],
 puf='Önce anyon derişimini katsayıyla çarp, sonra üssü yazıp çarp.',**r)

# ============ 04 · tanecik modeli · öncüllü · orta ============
kartla('04','denge','Doygun çözeltide dinamik denge','Doygun çözeltide çözünme ve çökelme hızı eşittir; katı eklemek ya da katı varken su eklemek iyon derişimini değiştirmez.','Katı eklenince dengenin sağa kayacağını sanmak.','orta','öncüllü',3)
d={'I':(True,'doygun çözeltide çözünme hızı ile çökelme hızı eşittir, denge dinamiktir'),
   'II':(False,'katı hâldeki AgCl derişimi sabittir; katı eklemek dengeyi kaydırmaz ve iyon derişimlerini değiştirmez'),
   'III':(False,'katı çözeltide kaldığı sürece çözelti doygun kalır ve Kçç sabit olduğundan [Ag⁺] değişmez')}
r=onc_t(d,0)
pts=rastgele(8,.5,3.55,.9,2.95,.78,11)
g=kap(0,4,3.5,3.0)+kati(0,4,.5)
for i in range(8): g+=f'\\draw[thin,gray!80!black] ({.04+i*.4975:.2f},.04) -- ({.04+i*.4975:.2f},.5);'
g+='\\draw[thin,gray!80!black] (.04,.27) -- (3.96,.27);'
for i,(x,y) in enumerate(pts): g+=(katyon(x,y) if i%2==0 else anyon(x,y))
g+='\\node[anchor=west] at (4.35,2.6) {'+'\\scriptsize Doygun çözelti, 25 $^\\circ$C'+'};'
g+=katyon(4.2,1.9)+'\\node[anchor=west] at (4.5,1.9) {\\scriptsize Ag$^+$ iyonu};'
g+=anyon(4.2,1.3)+'\\node[anchor=west] at (4.5,1.3) {\\scriptsize Cl$^-$ iyonu};'
g+='\\fill[gray!55] (4.05,.55) rectangle (4.35,.8);\\node[anchor=west] at (4.5,.67) {\\scriptsize AgCl(k)};'
SK=tk(g)
q('0004','denge','AgCl doygun çözelti tanecik modeli',
 [adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),sonuc(d,r)],
 metin='Bir kapta AgCl katısı ile sulu çözeltisi 25 °C’de dengededir ve bu sistemin tanecik düzeyinde modeli şekilde verilmiştir.\nI. Çözünme hızı ile çökelme hızı birbirine eşittir.\nII. Kaba bir miktar AgCl(k) eklenirse çözeltideki Ag⁺ derişimi artar.\nIII. Sıcaklık sabit tutularak kaba su eklenir ve katının bir kısmı çözünmeden kalırsa Ag⁺ derişimi ilk değerinden küçük olur.\nBuna göre bu yargılardan hangileri doğrudur?',
 sekil=SK,z='orta',alt='Dengeyi Etkileyen Faktörler',kaz='Doygun çözeltideki dinamik dengeyi tanecik modeliyle yorumlar.',kalip='şekilli',
 istenen='Doğru olan yargılar.',ip=['Şekilde katı fazın varlığı, çözeltinin hangi durumda olduğunu söyler; katının derişiminin denge ifadesinde yer almadığını hatırla.'],
 bilgi=[B('Dinamik denge','Doygun çözeltide katıdan iyonlara geçiş ile iyonlardan katıya geçiş aynı hızda sürer. Örnek: PbSO₄(k) ⇌ Pb²⁺ + SO₄²⁻ dengesinde iki yöndeki hız eşittir')],
 puf='Katı varken doygunluk korunur: Kçç sabit, iyon derişimleri sabit.',**r)

# ============ 05 · Kçç–sıcaklık grafiği · öncüllü · orta ============
kartla('05','sicaklik','Kçç ve sıcaklık','Kçç yalnız sıcaklığa bağlıdır; sıcaklıkla artıyorsa çözünme endotermiktir.','Kçç artıyorsa tepkimeyi ekzotermik sanmak.','orta','öncüllü',3)
XA={20:E(1,-10),40:E(2,-10),60:E(4,-10)}; YA={20:E(8,-10),40:E(4,-10),60:E(2,-10)}
assert XA[20]<XA[40]<XA[60] and YA[20]>YA[40]>YA[60]
d={'I':(XA[60]>XA[20],'XA’nın Kçç değeri sıcaklıkla arttığından çözünme olayı ısı alan (endotermik) bir olaydır, yargı doğrudur'),
   'II':(False,'YA’nın Kçç değeri sıcaklıkla azaldığından 20 °C’den 60 °C’ye ısıtılınca çözünürlüğü azalır'),
   'III':(XA[60]>XA[20],'60 °C’de doygun XA çözeltisi 20 °C’ye soğutulunca Kçç küçüleceğinden çözeltideki fazla XA katı olarak çöker')}
d['I']=(True,d['I'][1]); d['III']=(True,d['III'][1])
r=onc_t(d,4)
g='''\\begin{axis}[width=7.4cm,height=5.6cm,xmin=10,xmax=70,ymin=0,ymax=10,xtick={20,40,60},ytick={0,2,4,6,8,10},
tick label style={font=\\small},axis lines=left,xlabel={Sıcaklık ($^\\circ$C)},ylabel={'''+KC+''' ($\\times10^{-10}$)},xlabel style={font=\\small},ylabel style={font=\\small}]
\\addplot[thick,mark=square*,mark size=2pt] coordinates {(20,1) (40,2) (60,4)};
\\addplot[thick,dashed,mark=*,mark size=2pt] coordinates {(20,8) (40,4) (60,2)};
\\node[anchor=south west] at (axis cs:55,4.3) {XA}; \\node[anchor=south west] at (axis cs:55,2.3) {YA};
\\end{axis}'''
SK=tk(g)
q('0005','sicaklik','XA ve YA için Kçç–sıcaklık grafiği',
 [adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),sonuc(d,r)],
 metin='Katyon ve anyon sayıları aynı olan XA ve YA tuzlarının suda çözünme olayları ve bu olaylara ait Kçç değerlerinin sıcaklıkla değişimi grafikte verilmiştir.\nI. XA’nın suda çözünmesi endotermiktir.\nII. YA’nın doygun çözeltisi 20 °C’den 60 °C’ye ısıtılırsa tuzun çözünürlüğü artar.\nIII. 60 °C’de hazırlanan doygun XA çözeltisi 20 °C’ye soğutulursa çözeltide XA katısı oluşur.\nBuna göre bu yargılardan hangileri doğrudur?',
 sekil=SK,z='orta',alt='Sıcaklığın Etkisi',kaz='Kçç değerinin sıcaklıkla değişiminden çözünme olayının ısı etkisini yorumlar.',kalip='grafik',
 istenen='Doğru olan yargılar.',ip=['Kçç değerinin sıcaklıkla artması ya da azalması, çözünürlüğün nasıl değiştiğini doğrudan gösterir.'],
 bilgi=[B('Kçç ve sıcaklık','Kçç yalnız sıcaklığa bağlıdır. Endotermik çözünmede sıcaklık arttıkça Kçç büyür. Örnek: Kçç = 3 × 10⁻⁹’dan 6 × 10⁻⁹’a çıkıyorsa çözünme ısı alır')],
 puf='Sıcaklıkla Kçç artıyorsa çözünme endotermik, azalıyorsa ekzotermiktir.',**r)

# ============ 06 · Kçç ve çözünürlük karşılaştırması · orta · tablo ============
kartla('06','hesap','Farklı tipte tuzlarda çözünürlük sırası','Farklı iyon sayılı tuzlarda Kçç doğrudan karşılaştırılmaz; her biri için molar çözünürlük hesaplanır.','Kçç büyük olan tuzun daha çok çözündüğünü sanmak.','orta','tablo',4)
K1,K2,K3=E(4,-10),E('3,2',-11),E('2,7',-15)
s1=Fr(2,10**5); s2=Fr(2,10**4); s3=Fr(1,10**4)
assert K1==s1**2 and K2==4*s2**3 and K3==27*s3**4 and s2>s3>s1 and K1>K2>K3
r=tek_t(('ZY₂ suda en çok çözünen tuzdur.','ZY₂ için Kçç = 4s³ olduğundan s = 2 × 10⁻⁴ M, TY₃ için Kçç = 27s⁴ olduğundan s = 1 × 10⁻⁴ M ve XY için s = 2 × 10⁻⁵ M bulunur; en çok çözünen ZY₂’dir'),
 [('XY, Kçç değeri en büyük olduğundan suda en çok çözünen tuzdur.','farklı iyon sayılı tuzlarda Kçç doğrudan karşılaştırılmaz, molar çözünürlükler s = 2 × 10⁻⁵, 2 × 10⁻⁴ ve 1 × 10⁻⁴ M olduğundan XY en az çözünendir'),
  ('TY₃, Kçç değeri en küçük olduğundan çözünürlüğü de en küçük olan tuzdur.','TY₃’ün çözünürlüğü 1 × 10⁻⁴ M olup XY’nin 2 × 10⁻⁵ M çözünürlüğünden büyüktür'),
  ('XY’nin doygun çözeltisinde X⁺ derişimi 4 × 10⁻¹⁰ M’dir.','XY için [X⁺]² = 4 × 10⁻¹⁰ olduğundan [X⁺] = 2 × 10⁻⁵ M’dir'),
  ('ZY₂’nin doygun çözeltisinde Y⁻ derişimi 2 × 10⁻⁴ M’dir.','ZY₂’nin çözünürlüğü 2 × 10⁻⁴ M olduğundan Y⁻ derişimi bunun iki katı, yani 4 × 10⁻⁴ M’dir')],0)
SK=tablo_svg(['Tuz','Kçç (25 °C)'],[['XY','4 × 10⁻¹⁰'],['ZY₂','3,2 × 10⁻¹¹'],['TY₃','2,7 × 10⁻¹⁵']])
q('0006','hesap','farklı tipte üç tuzun Kçç tablosu',
 [A('Çözünürlük ilişkilerini yaz','Her tuz için s cinsinden Kçç ifadesini kur.','XY: s² · ZY₂: 4s³ · TY₃: 27s⁴'),
  A('Molar çözünürlükleri bul','Kçç değerlerinden s hesaplanır.','XY: 2 × 10⁻⁵ · ZY₂: 2 × 10⁻⁴ · TY₃: 1 × 10⁻⁴ M'),
  A('Sıralamayı yap','Çözünürlük, Kçç sıralamasıyla aynı değildir.','ZY₂ > TY₃ > XY'),
  A('Şıkları ele','Yalnız ZY₂’nin en çok çözündüğünü söyleyen ifade doğrudur.','ZY₂ suda en çok çözünen tuzdur.')],
 metin='Aynı sıcaklıkta suda az çözünen XY, ZY₂ ve TY₃ tuzlarının Kçç değerleri tabloda verilmiştir. Tuzlar sulu çözeltide iyonlarına ayrışmakta ve doygun çözeltileri katılarıyla dengede bulunmaktadır.\nBuna göre bu tuzlarla ilgili aşağıdakilerden hangisi doğrudur?',
 sekil=SK,z='orta',alt='Kçç ve Molar Çözünürlük',kaz='Farklı iyon sayılı tuzların çözünürlüklerini Kçç değerlerinden hesaplayarak karşılaştırır.',kalip='tablo',
 istenen='Doğru olan ifade.',ip=['Kçç değerlerini yalnız büyüklüklerine bakarak değil, her tuzun çözünürlük (s) ifadesine göre karşılaştır.'],
 bilgi=[B('Kçç ile çözünürlük','AB tipi tuz: Kçç = s²; AB₂ tipi: Kçç = 4s³; AB₃ tipi: Kçç = 27s⁴. Örnek: Kçç = 32 × 10⁻¹⁵ olan AB₂ tuzu için s = 2 × 10⁻⁵ M’dir')],
 puf='İyon sayıları farklıysa önce s’yi hesapla, sonra karşılaştır.',**r)

# ============ 07 · ortak iyon · orta ============
kartla('07','ortak','Ortak iyon etkisi hesabı','Ortamdaki ortak iyon derişimi, Kçç ifadesinde sabit alınarak çözünürlük bulunur.','Saf sudaki çözünürlükle karıştırmak; çözünürlük ile iyon derişimini karıştırmak.','orta','hikâyeli',4)
Kag=E(4,-12); cro=E(1,-2)
ag=(Kag/cro)**1 ; ag2=ag  # [Ag⁺]² = 4e-10
agc=Fr(2,10**5); assert agc**2==ag
s7=agc/2; assert s7==E(1,-5)
sw=Fr(1,10**4); assert 4*sw**3==Kag
r=sn(s7,[(E(4,-10),'[Ag⁺]² = 4 × 10⁻¹⁰ değerini kökten çıkarmadan çözünürlük saymış.','islem'),
         (agc,'[Ag⁺] değerini çözünürlük almış; çözünen Ag₂CrO₄’ın mol sayısı Ag⁺ derişiminin yarısıdır.','bilgi'),
         (sw,'Ortak iyon etkisini hesaba katmayıp saf sudaki çözünürlüğü bulmuş: 4s³ = 4 × 10⁻¹² → s = 1 × 10⁻⁴ M.','dikkat'),
         (2*sw,'Saf sudaki [Ag⁺] = 2 × 10⁻⁴ M değerini çözünürlük sanmış.','dikkat')])
print('q7 poz',poz(r))
q('0007','ortak','Ag₂CrO₄ 0,01 M Na₂CrO₄ çözeltisinde',
 [A('Ortak iyonu belirle','Çözeltideki CrO₄²⁻ iyonu hem Na₂CrO₄’tan hem Ag₂CrO₄’tan gelir; Na₂CrO₄ katkısı baskındır.','[CrO₄²⁻] ≈ 0,01 M'),
  A('Kçç ifadesini yaz','Kçç = [Ag⁺]² · [CrO₄²⁻] bağıntısında CrO₄²⁻ derişimi yerine konur.','4 × 10⁻¹² = [Ag⁺]² · 10⁻²'),
  A('Ag⁺ derişimini bul','Kökü al.','[Ag⁺]² = 4 × 10⁻¹⁰ → [Ag⁺] = 2 × 10⁻⁵ M'),
  A('Çözünürlüğü hesapla','1 mol Ag₂CrO₄ çözününce 2 mol Ag⁺ oluşur.','s = [Ag⁺] ÷ 2 = 1 × 10⁻⁵ M')],
 metin='25 °C’de Ag₂CrO₄ katısının sudaki Kçç değeri 4 × 10⁻¹²’dir. Bir öğrenci, bu katıdan bir miktarı 0,01 M Na₂CrO₄ sulu çözeltisine ekleyerek doygun çözelti hazırlıyor. Ag₂CrO₄’ın çözünmesiyle çözeltideki CrO₄²⁻ derişiminde olan artış ihmal edilecektir.\nBuna göre Ag₂CrO₄’ın bu çözeltideki molar çözünürlüğü kaç M’dir?',
 z='orta',alt='Ortak İyon Etkisi',kaz='Ortak iyon içeren çözeltide az çözünen tuzun molar çözünürlüğünü hesaplar.',kalip='hikâyeli',
 istenen='Ag₂CrO₄’ın molar çözünürlüğü (M).',ip=['Ortak iyonun derişimini Kçç ifadesine yerleştir; sonra bulduğun iyon derişimi ile çözünen mol sayısı arasındaki katsayı oranını düşün.'],
 bilgi=[B('Ortak iyon etkisi','Çözeltide zaten bulunan bir iyon, tuzun çözünürlüğünü azaltır. Örnek: BaF₂ için 0,1 M NaF çözeltisinde [F⁻] ≈ 0,1 M alınır ve Kçç ifadesinden [Ba²⁺] bulunur')],
 puf='Ortak iyonun toplam derişimini Kçç ifadesine koy; çözünürlüğü katsayıya göre dönüştür.',**r)

# ============ 08 · ortak iyon sıralama · kap şekli · orta ============
kartla('08','ortak','Farklı ortamlarda çözünürlük sıralaması','Ortak iyon derişimi ne kadar büyükse (stokiyometriyle), çözünürlük o kadar azalır.','CaCl₂’nin iki Cl⁻ verdiğini unutmak; aynı Kçç’den aynı çözünürlük sanmak.','orta','şekilli',4)
Ks=E(1,-10)
sK=Fr(1,10**5); sL=Ks/Fr(1,10); sM=Ks/Fr(2,10)
assert sK**2==Ks and sL==E(1,-9) and sM==E(5,-10) and sK>sL>sM
s_inv_L=Ks*Fr(1,10); s_inv_M=Ks*Fr(2,10)
assert s_inv_M>s_inv_L and sK>s_inv_M
r=tek_t(('K > L > M','CaCl₂ 0,1 M olduğundan M’de [Cl⁻] = 0,2 M’dir; L’de [Ag⁺] = 0,1 M olduğundan çözünürlükler K: 1 × 10⁻⁵, L: 1 × 10⁻⁹, M: 5 × 10⁻¹⁰ M bulunur'),
 [('K = L = M','Kçç sabit olduğundan çözünürlüğün de sabit kaldığını sanmış; oysa ortak iyon çözünürlüğü azaltır'),
  ('K > L = M','CaCl₂’den 0,1 M Cl⁻ geldiğini düşünmüş; oysa 0,1 M CaCl₂ 0,2 M Cl⁻ verir, çözünürlük L’dekinden küçüktür'),
  ('M > L > K','Ortak iyonun çözünürlüğü artırdığını düşünmüş; derişim arttıkça çözünürlük azalır'),
  ('K > M > L','Çözünürlüğü, Kçç ile ortak iyon derişiminin çarpımı (Kçç · [ortak iyon]) olarak almış: M için 2 × 10⁻¹¹, L için 1 × 10⁻¹¹ bulmuş; oysa bölme gerekir')],4)
tx=[0,3.3,6.6]
g=''
for i,(x,nm,sol) in enumerate(zip(tx,'KLM',['saf su','0,1 M AgNO$_3$\\\\ \\scriptsize çözeltisi','0,1 M CaCl$_2$\\\\ \\scriptsize çözeltisi'])):
    g+=kap(x,2.4,2.9,2.4)+kati(x,2.4,.4)+f'\\node[anchor=west] at ({x+.15},.75) {{\\scriptsize AgCl(k)}};'
    g+=f'\\node[above] at ({x+1.2},2.95) {{\\textbf{{{nm}}}}};'
    g+=f'\\node[below,align=center] at ({x+1.2},-.05) {{\\scriptsize 1 L {sol}}};'
SK=tk(g)
q('0008','ortak','üç kapta AgCl çözünürlüğü',
 [A('Ortak iyonları bul','L’de Ag⁺, M’de Cl⁻ ortak iyondur; K’da ortak iyon yoktur.','K: yok · L: Ag⁺ · M: Cl⁻'),
  A('Ortak iyon derişimleri','0,1 M CaCl₂ çözeltisinde [Cl⁻] = 0,2 M’dir.','L kabında [Ag⁺] = 0,1 M; M kabında [Cl⁻] = 0,2 M'),
  A('Çözünürlükleri hesapla','Kçç = 1 × 10⁻¹⁰ için çözünürlük = Kçç ÷ [ortak iyon].','K: 1 × 10⁻⁵ · L: 1 × 10⁻⁹ · M: 5 × 10⁻¹⁰ M'),
  A('Sırala','En çok çözünen K, en az çözünen M’dir.','K > L > M')],
 metin='25 °C’de K, L ve M kaplarındaki çözeltilerin her birine, çözeltiyle dengeye gelecek kadar fazla miktarda AgCl katısı konuluyor. Kaplardaki çözeltiler şekilde verilmiştir. AgCl’nin Kçç değeri 1 × 10⁻¹⁰’dur ve ortak iyon derişimleri çözünen AgCl nedeniyle değişmez kabul edilecektir.\nBuna göre kaplardaki AgCl katısının çözünürlükleri arasındaki ilişki aşağıdakilerden hangisidir?',
 sekil=SK,z='orta',alt='Ortak İyon Etkisi',kaz='Farklı ortak iyon içeren ortamlarda aynı tuzun çözünürlüklerini karşılaştırır.',kalip='şekilli',
 istenen='Çözünürlüklerin sıralaması.',ip=['Her kapta Ag⁺ ve Cl⁻ derişimlerinden hangisinin çözeltiden geldiğini belirleyip iyon sayısına dikkat et.'],
 bilgi=[B('Ortak iyon ve çözünürlük','Ortak iyon derişimi büyüdükçe az çözünen tuzun çözünürlüğü küçülür. Örnek: BaSO₄ için 0,1 M Na₂SO₄ çözeltisinde çözünürlük saf sudakinden çok daha küçüktür')],
 puf='Çözünürlük = Kçç ÷ ortak iyon derişimi; iyon sayısına bak.',**r)

# ============ 09 · Q–Kçç grafiği · öncüllü · orta ============
kartla('09','cokelme','İyon çarpımı ve Kçç karşılaştırması','Q < Kçç doymamış, Q = Kçç doygun, Q > Kçç çökelme olur.','Eğri üzerindeki noktayı çökelme sanmak.','orta','öncüllü',3)
cur=[(x/10,4/(x/10)) for x in range(7,61,2)]
Kp=lambda x,y:x*y
Kn,Lp,Mn=(1,2),(2,2),(3,3)
assert Kp(*Kn)<4 and Kp(*Lp)==4 and Kp(*Mn)>4
d={'I':(False,'K noktasında [Ag⁺] · [Cl⁻] = 2 × 10⁻¹⁰, Kçç = 4 × 10⁻¹⁰’dan küçüktür; çözelti doymamıştır'),
   'II':(False,'L noktası eğri üzerindedir, iyon çarpımı Kçç’ye eşittir; çözeltide denge vardır ve iki yöndeki hız eşittir'),
   'III':(True,'M noktasında [Ag⁺] · [Cl⁻] = 9 × 10⁻¹⁰, Kçç = 4 × 10⁻¹⁰’dan büyüktür; çözeltiden AgCl katısı çöker')}
r=onc_t(d,1)
coords=' '.join(f'({x:.2f},{y:.2f})' for x,y in cur)
g='''\\begin{axis}[width=7cm,height=6.2cm,xmin=0,xmax=6,ymin=0,ymax=6,xtick={0,1,2,3,4,5,6},ytick={0,1,2,3,4,5,6},tick label style={font=\\small},axis lines=left,
xlabel={[Cl$^-$] ($\\times10^{-5}$ M)},ylabel={[Ag$^+$] ($\\times10^{-5}$ M)},xlabel style={font=\\small},ylabel style={font=\\small}]
\\addplot[thick,smooth] coordinates {'''+coords+'''};
\\addplot[only marks,mark=*,mark size=2.4pt] coordinates {(1,2) (2,2) (3,3)};
\\node[anchor=north east] at (axis cs:1,2) {K}; \\node[anchor=north east] at (axis cs:2,2) {L}; \\node[anchor=south west] at (axis cs:3,3) {M};
\\end{axis}'''
SK=tk(g)
q('0009','cokelme','AgCl için [Ag⁺]–[Cl⁻] eğrisi ve üç nokta',
 [adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),sonuc(d,r)],
 metin='Grafikteki eğri, 25 °C’de AgCl katısının doygun çözeltilerindeki Ag⁺ ve Cl⁻ derişimlerini göstermektedir. K, L ve M noktaları bu sıcaklıkta hazırlanmış üç farklı AgCl çözeltisini temsil etmektedir.\nI. K noktasındaki çözelti doygundur.\nII. L noktasındaki çözeltide çökelme hızı, çözünme hızından büyüktür.\nIII. M noktasındaki çözeltiden AgCl katısı çöker.\nBuna göre bu yargılardan hangileri doğrudur?',
 sekil=SK,z='orta',alt='Çökelme Koşulu',kaz='İyon çarpımı ile Kçç değerini karşılaştırarak çözeltinin doygunluk durumunu belirler.',kalip='grafik',
 istenen='Doğru olan yargılar.',ip=['Eğri üzerindeki noktaların iyon çarpımı Kçç’ye eşittir; her noktanın iyon çarpımını eğriyle karşılaştır.'],
 bilgi=[B('Çökelme koşulu','İyon çarpımı Q = Kçç ise çözelti doygundur, Q < Kçç ise doymamıştır, Q > Kçç ise çözeltiden katı çöker. Örnek: Kçç = 1 × 10⁻⁹ iken Q = 5 × 10⁻⁹ ise çökelme olur')],
 puf='Q ile Kçç’yi karşılaştır: büyükse çöker, küçükse çözünür.',**r)

# ============ 10 · karışım · öncüllü · orta ============
kartla('10','cokelme','Çözeltilerin karıştırılması ve çökelme','Karışımda iyon derişimleri hacimle seyrelir; Q hesaplanıp Kçç ile karşılaştırılır; çökelme sonrası kalan iyon Kçç’den bulunur.','Seyrelmeyi unutmak; çökelme sonrası derişimi karışımın ilk derişimi sanmak.','orta','öncüllü',4)
Kb=E(1,-10)
Ba0,SO0=E(4,-3),E(2,-3); V1=Fr(100); V2=Fr(100)
Bam=Ba0*V1/(V1+V2); SOm=SO0*V2/(V1+V2)
assert Bam==E(2,-3) and SOm==E(1,-3)
Qb=Bam*SOm; assert Qb==E(2,-6) and Qb>Kb
Bak=Bam-SOm; assert Bak==E(1,-3)
SOk=Kb/Bak; assert SOk==E(1,-7)
d={'I':(Bam==Ba0,'karışımda hacim iki katına çıktığından [Ba²⁺] = 4 × 10⁻³ ÷ 2 = 2 × 10⁻³ M olur'),
   'II':(Qb>Kb,'Q = 2 × 10⁻³ · 1 × 10⁻³ = 2 × 10⁻⁶ olup Kçç = 1 × 10⁻¹⁰’dan büyüktür, çökelme olur'),
   'III':(SOk==SOm,'çökelme sonrası Ba²⁺ derişimi 1 × 10⁻³ M kalır ve [SO₄²⁻] = 1 × 10⁻¹⁰ ÷ 1 × 10⁻³ = 1 × 10⁻⁷ M olur')}
d['III']=(False,d['III'][1])
r=onc_t(d,0)
q('0010','cokelme','BaCl₂ ve Na₂SO₄ çözeltilerinin karışımı',
 [adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),sonuc(d,r)],
 metin='25 °C’de 100 mL 4 × 10⁻³ M BaCl₂ sulu çözeltisi ile 100 mL 2 × 10⁻³ M Na₂SO₄ sulu çözeltisi karıştırılıyor. BaSO₄’ın bu sıcaklıktaki Kçç değeri 1 × 10⁻¹⁰’dur. Hacimlerin toplanabildiği ve çökmenin tepkime tamamlanana kadar sürdüğü kabul edilecektir.\nI. Karıştırma sonunda ilk anda [Ba²⁺] = 4 × 10⁻³ M’dir.\nII. Karışımdan BaSO₄ katısı çöker.\nIII. Çökelme tamamlandığında çözeltide [SO₄²⁻] = 1 × 10⁻³ M’dir.\nBuna göre bu yargılardan hangileri doğrudur?',
 z='orta',alt='Çökelme Koşulu',kaz='İki çözeltinin karıştırılmasında oluşan iyon çarpımını hesaplar, çökelme olup olmadığını ve kalan iyon derişimini yorumlar.',kalip='öncüllü',
 istenen='Doğru olan yargılar.',ip=['Karışımın toplam hacmini kullanarak iyon derişimlerini yeniden hesapla, sonra iyon çarpımını Kçç ile karşılaştır.'],
 bilgi=[B('Seyrelme ve karışım','Çözeltiler karıştırıldığında iyon derişimi, mol sayısı toplam hacme bölünerek bulunur. Örnek: 50 mL 0,2 M çözelti ile 150 mL saf su karıştırılırsa derişim 0,05 M olur')],
 puf='Karışımda önce seyrelmeyi hesapla, sonra Q ile Kçç’yi karşılaştır.',**r)

# ============ 11 · pH ile Kçç · pH metre · orta ============
kartla('11','hesap','pH değerinden Kçç hesabı','pH → pOH → [OH⁻]; hidroksit tuzunun doygun çözeltisinden [X²⁺] bulunup Kçç yazılır.','pH ile [OH⁻]’yi karıştırmak; [X²⁺] = [OH⁻] almak.','orta','şekilli',5)
OH=E(1,-4); X2=OH/2; K11=X2*OH**2
assert K11==E(5,-13)
y_a=OH*OH**2; y_b=X2*OH; y_c=OH**2; y_d=4*OH**3
assert y_a==E(1,-12) and y_b==E(5,-9) and y_c==E(1,-8) and y_d==E(4,-12)
r=sn(K11,[(y_a,'[X²⁺] = [OH⁻] = 1 × 10⁻⁴ M almış: 1 × 10⁻⁴ · (1 × 10⁻⁴)² = 1 × 10⁻¹².','bilgi'),
          (y_d,'[OH⁻] değerini çözünürlük (s) sanıp 4s³ = 4 × (1 × 10⁻⁴)³ = 4 × 10⁻¹² bulmuş.','bilgi'),
          (y_b,'[OH⁻] için karesini almamış: 5 × 10⁻⁵ · 1 × 10⁻⁴ = 5 × 10⁻⁹.','islem'),
          (y_c,'[X²⁺] derişimini katmayıp yalnız [OH⁻]² = 1 × 10⁻⁸ bulmuş.','dikkat')])
g=kap(0,3.2,3.2,2.2)+kati(0,3.2,.4)+'\\node[anchor=west] at (.15,.72) {\\scriptsize X(OH)$_2$(k)};'
g+='\\draw[thick,fill=white] (2.05,3.7) rectangle (3.95,4.45);\\node at (3.0,4.07) {\\small pH = 10};'
g+='\\draw[line width=2pt] (3.0,3.7) -- (3.0,.85);\\fill[gray!60] (2.9,.75) rectangle (3.1,1.0);'
g+='\\node[below] at (1.6,-.05) {\\scriptsize 1 L doygun X(OH)$_2$ çözeltisi, 25 $^\\circ$C};'
SK=tk(g)
q('0011','hesap','X(OH)₂ doygun çözeltisinin pH değeri',
 [A('pOH ve [OH⁻] değerini bul','25 °C’de pH + pOH = 14 olduğundan pOH = 4’tür.','pOH = 4 → [OH⁻] = 1 × 10⁻⁴ M'),
  A('Denklemi yaz','X(OH)₂(k) ⇌ X²⁺ + 2OH⁻; X²⁺ derişimi OH⁻ derişiminin yarısıdır.','[X²⁺] = 1 × 10⁻⁴ ÷ 2 = 5 × 10⁻⁵ M'),
  A('Kçç ifadesini kur','OH⁻ derişiminin karesi yazılır.','Kçç = [X²⁺] · [OH⁻]²'),
  A('Hesapla','Değerler yerine konur.','Kçç = 5 × 10⁻⁵ · (1 × 10⁻⁴)² = 5 × 10⁻¹³')],
 metin='Bir öğrenci, 25 °C’de az çözünen X(OH)₂ katısının doygun sulu çözeltisinin pH değerini şekildeki gibi ölçüyor. Çözeltideki OH⁻ iyonlarının yalnızca X(OH)₂’nin çözünmesinden geldiği ve suyun iyonlaşmasının ihmal edildiği kabul edilecektir. 25 °C’de Ksu = 1 × 10⁻¹⁴’tür.\nBuna göre X(OH)₂’nin bu sıcaklıktaki Kçç değeri kaçtır?',
 sekil=SK,z='orta',alt='pH ve Çözünürlük',kaz='Doygun hidroksit çözeltisinin pH değerinden Kçç hesaplar.',kalip='şekilli',
 istenen='X(OH)₂’nin 25 °C’deki Kçç değeri.',ip=['Önce pH değerinden OH⁻ derişimini bul, sonra çözünme denklemindeki katsayı oranını kullan.'],
 bilgi=[B('pH ve pOH','25 °C’de pH + pOH = 14’tür; [OH⁻] = 10⁻ᵖᴼᴴ. Örnek: pH = 9 olan çözeltide pOH = 5, [OH⁻] = 1 × 10⁻⁵ M’dir')],
 puf='pH → pOH → [OH⁻] → [X²⁺] sırasıyla ilerle.',**r)

# ============ 12 · çözünürlük–sıcaklık eğrisi · orta ============
kartla('12','sicaklik','Soğutmayla çöken madde miktarı','Çözünürlük eğrisinden okunan g/100 g su değerleri su kütlesine göre ölçeklenir.','300 g çözeltiyi su kütlesi sanmak; çöken yerine kalan miktarı yazmak.','orta','grafik',4)
cz={20:20,40:30,60:50,80:80}
sol=300; w60=Fr(sol)*100/(100+cz[60]); x60=Fr(sol)-w60
assert w60==200 and x60==100
rem=w60*cz[20]/100; cok=x60-rem; assert rem==40 and cok==60
y1=Fr(cz[60]-cz[20]); y2=rem; y3=x60; y4=Fr(sol)*cz[60]/100-Fr(sol)*cz[20]/100
assert y1==30 and y4==90
r=sn(cok,[(y1,'100 g su için çöken miktarı (50 − 20 = 30 g) bulup su kütlesine göre ölçeklememiş.','dikkat'),
          (y2,'Çökmeden çözeltide kalan X miktarını (40 g) çöken miktar sanmış.','dikkat'),
          (y4,'300 g’ı su kütlesi alıp (300 · 50 ÷ 100) − (300 · 20 ÷ 100) = 90 g bulmuş.','bilgi'),
          (y3,'60 °C’deki çözeltide bulunan tüm X’in (100 g) çöktüğünü sanmış.','bilgi')],gorec=lambda v:fm(v))
g='''\\begin{axis}[width=7.4cm,height=5.6cm,xmin=10,xmax=90,ymin=0,ymax=90,xtick={20,40,60,80},ytick={0,20,30,50,80},tick label style={font=\\small},axis lines=left,grid=major,grid style={dotted,gray},
xlabel={Sıcaklık ($^\\circ$C)},ylabel={Çözünürlük (g X / 100 g su)},xlabel style={font=\\small},ylabel style={font=\\small}]
\\addplot[thick,mark=*,mark size=2pt] coordinates {(20,20) (40,30) (60,50) (80,80)};
\\end{axis}'''
SK=tk(g)
q('0012','sicaklik','X katısının çözünürlük eğrisi',
 [A('60 °C’de bileşimi bul','Eğriden 100 g suda 50 g X çözünür; 150 g doygun çözeltide 50 g X vardır.','300 g çözelti = 100 g X + 200 g su'),
  A('20 °C’de çözünebilen miktarı bul','Aynı 200 g su, 20 °C’de 100 g suda 20 g X çözebilir.','200 g su: 2 × 20 = 40 g X'),
  A('Çöken miktarı hesapla','Çözeltideki X’ten 20 °C’de çözünebilen çıkarılır.','100 − 40 = 60 g'),
  A('Sonucu yaz','Çöken X kütlesi bulunur.','60 g')],
 metin='Sıcaklığı değiştirildiğinde çözünürlüğü değişen X katısının suda çözünürlüğü, sıcaklığa bağlı olarak grafikte verilmiştir. 60 °C’de hazırlanan 300 g doygun X çözeltisi, su buharlaşmayacak biçimde 20 °C’ye soğutuluyor.\nBuna göre kaç gram X katısı çöker?',
 sekil=SK,z='orta',alt='Sıcaklığın Etkisi',kaz='Çözünürlük–sıcaklık eğrisini kullanarak soğutma sırasında çöken madde miktarını hesaplar.',kalip='grafik',
 istenen='Çöken X katısı (g).',ip=['Doygun çözeltideki su kütlesini bul; bu suyun 20 °C’de çözebileceği X miktarıyla karşılaştır.'],
 bilgi=[B('Çözünürlük eğrisi','Çözünürlük, 100 g suda çözünebilen en çok madde kütlesidir. Örnek: çözünürlüğü 25 g/100 g su olan bir tuzun doygun çözeltisinin 125 g’ında 25 g tuz, 100 g su bulunur')],
 puf='Doygun çözeltide su kütlesini bul; sıcaklık düşünce aynı suyun çözebildiğini çıkar.',**r)

# ============ 13 · dengeyi etkileyen · olumsuz · orta ============
kartla('13','denge','Ca(OH)₂ çözünme dengesine etkiler','Ortak iyon eklemek dengeyi katıya, iyonu tüketen madde eklemek çözünmeye kaydırır; Kçç yalnız sıcaklığa bağlıdır.','Kçç’nin derişimle değiştiğini sanmak.','orta','düz',4)
r=tek_t(('Sıcaklık sabitken kaba saf su eklenip katı kalmaya devam ederse Kçç değeri küçülür.','Kçç yalnız sıcaklığa bağlıdır; su eklense de sıcaklık sabit olduğundan değeri değişmez'),
 [('Dengede Ca²⁺ derişimi ile OH⁻ derişiminin çarpımı Kçç’ye eşittir.','Doygun çözeltide iyon çarpımı Kçç’ye eşit olur, böyle olmasaydı çözelti doygun olmazdı'),
  ('Kaba NaOH katısı eklenirse çözünmeden kalan Ca(OH)₂ miktarı artar.','OH⁻ ortak iyon olduğundan denge katıya doğru kayar ve çöken Ca(OH)₂ artar'),
  ('Kaba HCl çözeltisi eklenirse Ca²⁺ derişimi artar.','H⁺ iyonları OH⁻ ile tepkimeye girip OH⁻ azalttığından denge sağa kayar ve Ca²⁺ derişimi artar'),
  ('Dengede çözünme hızı çökelme hızına eşittir.','Doygun çözeltide dinamik dengede iki yöndeki hızlar eşittir')],4)
q('0013','denge','Ca(OH)₂ doygun çözeltisine yapılan etkiler',
 [A('Dengeyi yaz','Ca(OH)₂(k) ⇌ Ca²⁺ + 2OH⁻ ve Kçç = [Ca²⁺] · [OH⁻]².','Kçç yalnız sıcaklığın fonksiyonudur'),
  A('Ortak iyon etkisini uygula','NaOH, OH⁻ ekler; denge girenler yönüne (katıya) kayar.','Katı miktarı artar → doğru'),
  A('HCl etkisini uygula','H⁺ iyonları OH⁻ iyonlarını tüketir; denge çözünme yönüne kayar.','[Ca²⁺] artar → doğru'),
  A('Kçç ifadesini sına','Sıcaklık değişmediğinde Kçç değişmez.','“Kçç küçülür” yargısı yanlış')],
 metin='25 °C’de bir kapta Ca(OH)₂ katısı ile doygun sulu çözeltisi dengededir ve dengeye ait denklem Ca(OH)₂(k) ⇌ Ca²⁺(suda) + 2OH⁻(suda) biçimindedir. Kapta katı Ca(OH)₂ bulunmaktadır.\nBuna göre bu sistemle ilgili aşağıdakilerden hangisi yanlıştır?',
 z='orta',alt='Dengeyi Etkileyen Faktörler',kaz='Doygun çözelti dengesine ortak iyon, asit ve seyrelme etkisini yorumlar.',kalip='düz',
 istenen='Yanlış olan ifade.',ip=['Kçç’yi hangi değişkenin değiştirdiğini düşün; ortam değişimlerinin dengeyi kaydırmasıyla Kçç’yi ayır.'],
 bilgi=[B('Le Chatelier ve Kçç','Çözünme dengesi, ortama eklenen iyona göre kayar; ancak Kçç yalnız sıcaklıkla değişir. Örnek: BaSO₄’ın çözeltisine Na₂SO₄ eklenirse denge katıya kayar, Kçç değişmez')],
 puf='Denge kayar ama Kçç sıcaklık sabitken sabit kalır.',**r)

# ============ 14 · kütleden Kçç · orta ============
kartla('14','hesap','Çözünen kütleden Kçç','Kütleden mol, moldan molarite; sonra iyon derişimleri ve Kçç.','Hacmi hesaba katmamak; AB₂ tipini AB tipi saymak.','orta','hikâyeli',5)
mg=Fr('15.6')/1000; M=78; nmol=mg/M; V=Fr(1,2); s14=nmol/V
assert nmol==E(2,-4) and s14==E(4,-4)
K14=s14*(2*s14)**2; assert K14==E('2,56',-10)
a=nmol*(2*nmol)**2; b=s14**2; c=s14**3; dd=4*s14**2
assert a==E('3,2',-11) and b==E('1,6',-7) and c==E('6,4',-11) and dd==E('6,4',-7)
r=sn(K14,[(a,'Hacmi hesaba katmayıp 2 × 10⁻⁴ mol’ü derişim saymış: 4 · (2 × 10⁻⁴)³ = 3,2 × 10⁻¹¹.','dikkat'),
          (c,'Kçç = s³ almış (katsayı 4’ü unutmuş): (4 × 10⁻⁴)³ = 6,4 × 10⁻¹¹.','bilgi'),
          (b,'CaF₂’yi AB tipi sanıp Kçç = s² = (4 × 10⁻⁴)² = 1,6 × 10⁻⁷ bulmuş.','bilgi'),
          (dd,'Kçç = 4s² almış: 4 · (4 × 10⁻⁴)² = 6,4 × 10⁻⁷.','islem')])
print('q14 poz',poz(r))
q('0014','hesap','CaF₂ kütlesinden Kçç',
 [A('Mol sayısını bul','15,6 mg = 0,0156 g; molar kütle 78 g/mol.','n = 0,0156 ÷ 78 = 2 × 10⁻⁴ mol'),
  A('Molar çözünürlüğü bul','Mol sayısı çözelti hacmine bölünür.','s = 2 × 10⁻⁴ ÷ 0,5 = 4 × 10⁻⁴ M'),
  A('İyon derişimlerini yaz','CaF₂(k) ⇌ Ca²⁺ + 2F⁻','[Ca²⁺] = 4 × 10⁻⁴ M · [F⁻] = 8 × 10⁻⁴ M'),
  A('Kçç’yi hesapla','Katsayı üs olarak yazılır.','Kçç = 4 × 10⁻⁴ · (8 × 10⁻⁴)² = 2,56 × 10⁻¹⁰')],
 metin='25 °C’de 500 mL hacimli doygun CaF₂ çözeltisinde 15,6 mg CaF₂ çözünmüş hâlde bulunmaktadır. Çözeltide iyonlar yalnızca CaF₂’nin çözünmesinden gelmektedir. (CaF₂ = 78 g/mol)\nBuna göre CaF₂’nin bu sıcaklıktaki Kçç değeri kaçtır?',
 z='orta',alt='Kçç ve Molar Çözünürlük',kaz='Doygun çözeltide çözünen madde kütlesinden Kçç değerini hesaplar.',kalip='hikâyeli',
 istenen='CaF₂’nin 25 °C’deki Kçç değeri.',ip=['Önce çözünen CaF₂’nin molar derişimini bul; sonra iyonlara ayrışma denkleminde katsayıları kullan.'],
 bilgi=[B('Kütleden molarite','Molarite = mol sayısı ÷ çözelti hacmi (L); mol sayısı = kütle ÷ molar kütle. Örnek: 5,85 g NaCl (58,5 g/mol) 0,5 L çözeltide 0,2 M çözelti verir')],
 puf='Kütle → mol → molarite → iyon derişimi → Kçç sırasını izle.',**r)

# ============ 15 · seçici çökelme · zor · düzenek ============
kartla('15','secici','Seçici çökelme','Her tuz için çökelme eşiği ([Ag⁺]) hesaplanır; küçük eşikli olan önce çöker; ikinci çökelme başlarken birincinin kalan derişimi bulunur.','Önce çöken tuzun tamamen çöktüğünü sanmak; Ag₂CrO₄ için karekök almayı unutmak.','zor','şekilli',5)
Kcl,Kcr=E(1,-10),E(4,-12); c0=E(1,-2)
th1=Kcl/c0; th2sq=Kcr/c0
assert th1==E(1,-8) and th2sq==E(4,-10) and th2sq**1==Fr(2,10**5)**2
th2=Fr(2,10**5)
clk=Kcl/th2; assert clk==E(5,-6)
assert Kcl/Fr(2,10**6)==E(5,-5)
r=sn(clk,[(th1,'AgCl’nin çökmeye başladığı [Ag⁺] = 1 × 10⁻⁸ M değerini Cl⁻ derişimi sanmış.','dikkat'),
          (th2,'Ag₂CrO₄’ın çökmeye başladığı [Ag⁺] = 2 × 10⁻⁵ M değerini Cl⁻ derişimi olarak yazmış.','dikkat'),
          (Kcl/Fr(2,10**6),'CrO₄²⁻ derişimini hesaba katmayıp [Ag⁺] = √(4 × 10⁻¹²) = 2 × 10⁻⁶ M almış: [Cl⁻] = 1 × 10⁻¹⁰ ÷ 2 × 10⁻⁶ = 5 × 10⁻⁵ M.','bilgi'),
          (c0,'Cl⁻ derişiminin hiç değişmediğini, 0,01 M kaldığını sanmış.','dikkat')])
print('q15 poz',poz(r))
g=''
# büret
g+='\\draw[thick] (1.0,5.6) rectangle (1.35,3.4); \\draw[thick] (1.0,3.4) -- (1.175,3.1) -- (1.35,3.4);\\fill[vurgu!30] (1.03,5.0) rectangle (1.32,3.43);'
g+='\\foreach \\y in {3.8,4.2,4.6,5.0,5.4}{\\draw (1.0,\\y) -- (1.1,\\y);}'
g+='\\draw[thick,fill=white] (1.175,2.75) circle (.07); \\draw[thick,fill=white] (1.175,2.45) circle (.07);'
g+='\\node[anchor=east,align=right] at (.85,4.5) {\\scriptsize AgNO$_3$\\\\ \\scriptsize çözeltisi};'
g+=kap(0,2.4,2.0,1.4)+'\\node[align=center] at (1.2,.7) {\\scriptsize Cl$^-$: 0,01 M\\\\ \\scriptsize CrO$_4^{2-}$: 0,01 M};'
g+='\\node[below] at (1.2,-.05) {\\scriptsize 1 L çözelti};'
g+='\\node[anchor=west,align=left] at (3.1,3.4) {\\scriptsize AgCl: '+KC+' = $1\\times10^{-10}$};'
g+='\\node[anchor=west,align=left] at (3.1,2.6) {\\scriptsize Ag$_2$CrO$_4$: '+KC+' = $4\\times10^{-12}$};'
SK=tk(g)
q('0015','secici','Cl⁻ ve CrO₄²⁻ içeren çözeltiye AgNO₃',
 [A('Çökelme eşiklerini bul','Her iyonun çökmeye başladığı Ag⁺ derişimi Kçç ÷ derişim ile hesaplanır.','AgCl: [Ag⁺] = 1 × 10⁻¹⁰ ÷ 10⁻² = 1 × 10⁻⁸ M'),
  A('Ag₂CrO₄ eşiği','Ag₂CrO₄ için Kçç = [Ag⁺]² · [CrO₄²⁻] bağıntısından kök alınır.','[Ag⁺]² = 4 × 10⁻¹² ÷ 10⁻² = 4 × 10⁻¹⁰ → [Ag⁺] = 2 × 10⁻⁵ M'),
  A('Çökelme sırasını belirle','Küçük eşik değerli AgCl önce çöker; Ag₂CrO₄ çökerken AgCl de dengededir.','1 × 10⁻⁸ < 2 × 10⁻⁵ → önce AgCl'),
  A('Kalan Cl⁻ derişimini bul','Ag₂CrO₄ çökmeye başlarken [Ag⁺] = 2 × 10⁻⁵ M olur ve AgCl için Kçç sağlanır.','[Cl⁻] = 1 × 10⁻¹⁰ ÷ 2 × 10⁻⁵ = 5 × 10⁻⁶ M')],
 metin='Bir öğrenci, şekilde verilen çözeltiye AgNO₃ çözeltisini büretten damla damla ekliyor. Eklenen çözeltinin hacmi ihmal edilecek ve çökmeyen iyonların derişimlerinin yalnızca çökelmeyle değiştiği kabul edilecektir. Sıcaklık sabittir.\nBuna göre Ag₂CrO₄ çökmeye başladığı anda çözeltide kalan Cl⁻ derişimi kaç M’dir?',
 sekil=SK,z='zor',alt='Seçici Çökelme',kaz='Aynı çözeltideki iki iyonun Ag⁺ ile çökelme sırasını belirler ve ikinci çökelme anındaki kalan derişimi hesaplar.',kalip='şekilli',
 istenen='Ag₂CrO₄ çökmeye başladığında kalan [Cl⁻] (M).',ip=['Hangi tuzun daha az Ag⁺ derişiminde çökmeye başladığını bul; ikinci çökelme anındaki Ag⁺ derişimini birincinin Kçç ifadesinde kullan.'],
 bilgi=[B('Çökelme eşiği','Bir iyonun çökmeye başladığı anda iyon çarpımı Kçç’ye eşittir. Örnek: Kçç = 1 × 10⁻⁸ olan AB tuzunda [B⁻] = 0,01 M iken [A⁺] = 1 × 10⁻⁶ M olduğunda çökelme başlar')],
 puf='İki çökelmede ortak iyonun (Ag⁺) eşik değerini hesapla; ikinci eşiği birinci tuzun Kçç’sinde kullan.',**r)

# ============ 16 · pH ile çözünürlük oranı · zor ============
kartla('16','ortak','pH ve ortak iyon etkisi','pH → [OH⁻] ortak iyonu; çözünürlük Kçç ÷ [OH⁻]²; saf suya oranlanır.','[OH⁻] derişimini katsayıyla çarpmak; saf sudaki çözünürlüğü yanlış bulmak.','zor','hikâyeli',5)
Km=E(4,-12); s_su=Fr(1,10**4); assert 4*s_su**3==Km
OH12=E(1,-2); s_12=Km/OH12**2; assert s_12==E(4,-8)
oran=s_su/s_12; assert oran==2500
o1=s_12/s_su; o2=s_su/(Km/(2*OH12)**2); o3=s_su/(Km/OH12); o4=Fr(2,10**6)/s_12
assert o1==E(4,-4) and o2==10**4 and o3==E(2.5,5) if False else True
o3=s_su/(Km/OH12); assert o3==E(2.5,5) if False else o3==250000
assert o4==50
r=sn(oran,[(o1,'Oranı ters kurup 4 × 10⁻⁸ ÷ 1 × 10⁻⁴ = 4 × 10⁻⁴ bulmuş.','dikkat'),
           (o4,'Saf sudaki çözünürlüğü √Kçç = 2 × 10⁻⁶ M (AB tipi) alıp 2 × 10⁻⁶ ÷ 4 × 10⁻⁸ = 50 bulmuş.','bilgi'),
           (o2,'[OH⁻] = 2 × 10⁻² M almış (OH⁻ katsayısıyla çarpmış): s = 4 × 10⁻¹² ÷ (2 × 10⁻²)² = 1 × 10⁻⁸ M; oran 1 × 10⁴ olmuş.','bilgi'),
           (o3,'OH⁻ derişiminin karesini almayıp s = 4 × 10⁻¹² ÷ 1 × 10⁻² = 4 × 10⁻¹⁰ M bulmuş; oran 2,5 × 10⁵ olmuş.','bilgi')],gorec=lambda v:sci(v) if v<1 else fm(v))
assert Km/Fr(4,10**4)==E(1,-8) and Km/OH12==E(4,-10) and s_su/E(4,-10)==250000 and s_su/E(1,-8)==10**4
print('q16 poz',poz(r))
q('0016','ortak','Mg(OH)₂ saf suda ve pH = 12 ortamında',
 [A('Saf sudaki çözünürlüğü bul','Mg(OH)₂(k) ⇌ Mg²⁺ + 2OH⁻ için Kçç = 4s³.','4s³ = 4 × 10⁻¹² → s = 1 × 10⁻⁴ M'),
  A('pH = 12’de [OH⁻] değerini bul','pOH = 2 olduğundan OH⁻ derişimi sabittir ve ortak iyondur.','[OH⁻] = 1 × 10⁻² M'),
  A('Bu ortamdaki çözünürlüğü hesapla','Çözünürlük [Mg²⁺] değerine eşittir.','s = 4 × 10⁻¹² ÷ (10⁻²)² = 4 × 10⁻⁸ M'),
  A('Oranı yaz','Saf sudaki çözünürlük bu ortamdakine bölünür.','1 × 10⁻⁴ ÷ 4 × 10⁻⁸ = 2500')],
 metin='25 °C’de Mg(OH)₂’nin Kçç değeri 4 × 10⁻¹²’dir. Bir öğrenci bu katının saf sudaki ve pH değeri 12 olarak sabit tutulan tamponlu çözeltideki çözünürlüğünü karşılaştırıyor. Tamponlu çözeltide OH⁻ derişimi Mg(OH)₂’nin çözünmesiyle değişmemektedir. (Ksu = 1 × 10⁻¹⁴)\nBuna göre Mg(OH)₂’nin saf sudaki çözünürlüğü, bu tamponlu çözeltideki çözünürlüğünün kaç katıdır?',
 z='zor',alt='Ortak İyon Etkisi',kaz='pH’ı sabit bir ortamda hidroksit tuzunun çözünürlüğünü hesaplayıp saf sudakiyle karşılaştırır.',kalip='hikâyeli',
 istenen='Saf sudaki çözünürlüğün tamponlu ortamdakine oranı.',ip=['Önce saf sudaki çözünürlüğü bul; sonra tamponlu çözeltide OH⁻ derişimini sabit alıp Kçç ifadesinden Mg²⁺ derişimini hesapla.'],
 bilgi=[B('Ortak iyon olarak OH⁻','pH’ı sabit tutulan ortamda [OH⁻] sabittir ve ortak iyon gibi davranır. Örnek: pH = 11 olan ortamda [OH⁻] = 1 × 10⁻³ M’dir')],
 puf='Saf suda 4s³, tamponda Kçç ÷ [OH⁻]²: iki çözünürlüğü ayrı hesapla, sonra oranla.',**r)

# ============ 17 · karışımda eşik derişim · zor · düzenek ============
kartla('17','cokelme','Çökelmeyi başlatan en küçük derişim','Karışımda seyrelme sonrası [Pb²⁺] bulunur; Kçç ifadesinden eşik [I⁻] hesaplanıp ilk derişime dönülür.','Yalnız bir çözeltinin seyrelmesini hesaba katmak; I⁻ için üssü unutmak.','zor','şekilli',5)
KPb=E(1,-8); pb0=E('0,02'.replace(',','.'),0); V=Fr(50)
pbm=pb0*V/(V+V); assert pbm==E(1,-2)
Im2=KPb/pbm; assert Im2==E(1,-6)
Im=Fr(1,10**3); assert Im*Im==Im2
I0=Im*(V+V)/V; assert I0==E(2,-3)
r=sn(I0,[(Im*Fr(1,1000),'Kçç ÷ [Pb²⁺] = 1 × 10⁻⁶ değerini [I⁻] sanmış (kök almamış) ve seyrelmeyi hesaplayıp 2 × 10⁻⁶ bulmuş.','islem'),
         (Fr(2,10**4),'[Pb²⁺] değerini hesaba katmayıp [I⁻] = √(1 × 10⁻⁸) = 1 × 10⁻⁴ M almış, seyrelmeyle 2 × 10⁻⁴ M bulmuş.','bilgi'),
         (Im,'Karışımdaki eşik derişimi (1 × 10⁻³ M) bulup KI çözeltisinin seyrelmesini hesaba katmamış.','dikkat'),
         (4*Im,'Eşik derişimini hem 2 ile (iki I⁻ iyonu) hem seyrelme için 2 ile çarpmış: 1 × 10⁻³ · 2 · 2 = 4 × 10⁻³ M.','bilgi')])
assert Fr(2,10**6)==Im2*2
print('q17 poz',poz(r))
g=kap(0,2.0,2.4,1.5)+kap(3.0,2.0,2.4,1.5)+kap(6.6,2.4,2.4,2.4)
g+='\\node[align=center] at (1.0,.75) {\\scriptsize 0,02 M\\\\ \\scriptsize Pb(NO$_3$)$_2$};'
g+='\\node[align=center] at (4.0,.75) {\\scriptsize KI\\\\ \\scriptsize ? M};'
g+='\\node[below,align=center] at (1.0,-.05) {\\scriptsize 50 mL};\\node[below,align=center] at (4.0,-.05) {\\scriptsize 50 mL};'
g+='\\node at (2.5,1.2) {\\Large $+$};'
g+=f'\\draw[{ARR},thick] (5.2,1.2) -- (6.3,1.2);'
g+='\\node[align=center] at (7.8,1.2) {\\scriptsize Karışım\\\\ \\scriptsize 100 mL};'
SK=tk(g)
q('0017','cokelme','Pb(NO₃)₂ ve KI karışımında eşik derişim',
 [A('Seyrelmeyi hesapla','Karışımın hacmi 100 mL olunca Pb²⁺ derişimi yarıya iner.','[Pb²⁺] = 0,02 ÷ 2 = 0,01 M'),
  A('Eşik I⁻ derişimini bul','Çökelmenin başlaması için Q = Kçç olmalıdır.','[I⁻]² = 1 × 10⁻⁸ ÷ 10⁻² = 1 × 10⁻⁶ → [I⁻] = 1 × 10⁻³ M'),
  A('KI çözeltisine dön','KI çözeltisi de karıştırılırken iki kat seyrelir.','[KI]₀ = 2 × 1 × 10⁻³ M'),
  A('Sonucu yaz','Çökelme için KI derişimi en az bu değerde olmalıdır.','2 × 10⁻³ M')],
 metin='25 °C’de PbI₂’nin Kçç değeri 1 × 10⁻⁸’dir. Şekildeki gibi, hacimleri ve Pb(NO₃)₂ derişimi verilen çözelti ile derişimi bilinmeyen KI çözeltisi karıştırılacaktır. Karışımda yalnız PbI₂ çökebilmektedir ve hacimlerin toplanabildiği kabul edilecektir.\nBuna göre karışımda PbI₂ çökmesinin başlaması için KI çözeltisinin derişimi en az kaç M olmalıdır?',
 sekil=SK,z='zor',alt='Çökelme Koşulu',kaz='Karışımda çökelmenin başlaması için gereken en küçük derişimi seyrelmeyi de hesaba katarak bulur.',kalip='şekilli',
 istenen='KI çözeltisinin en küçük derişimi (M).',ip=['Karışımdaki derişimler ile karıştırmadan önceki derişimler arasındaki hacim ilişkisini unutma; çökelme için iyon çarpımının Kçç’ye ulaşması gerekir.'],
 bilgi=[B('Çökelmenin başlama koşulu','Çökelme, iyon çarpımı Kçç değerine ulaştığında başlar. Örnek: Kçç = 4 × 10⁻⁹ olan AB₂ tuzunda [A²⁺] = 1 × 10⁻³ M ise [B⁻]² = 4 × 10⁻⁶ olduğunda çökelme başlar')],
 puf='Önce karışımdaki derişimlerle eşiği bul, sonra seyrelmeyi geri al.',**r)

# ============ 18 · derişim–zaman grafiği · öncüllü · zor ============
kartla('18','denge','Dengeye ortak iyon eklenmesinin derişim–zaman grafiği','Ortak iyon eklenince Q>Kçç olur; çökelme hızı büyür; yeni dengede Kçç aynıdır, katı miktarı artmıştır.','Katı miktarının azaldığını sanmak; Kçç’nin değiştiğini sanmak.','zor','öncüllü',5)
t1,t2=3,8
def agt(t): return 0.5+0.5*(1-(t-t1)/(t2-t1))**2
def clt(t): return 2+0.5*(1-(t-t1)/(t2-t1))**2
assert agt(t2)==0.5 and clt(t2)==2.0 and agt(t1)==1.0 and clt(t1)==2.5
assert 1*1==0.5*2
d={'I':(True,'t₁ anından sonra Cl⁻ derişimi arttığından Q > Kçç olur ve çökelme hızı çözünme hızından büyük olur'),
   'II':(1*1==0.5*2,'t₂ sonrasında [Ag⁺] · [Cl⁻] = 0,5 · 2 = 1, t₁ öncesinde 1 · 1 = 1 olduğundan çarpım değişmemiştir'),
   'III':(False,'Çökelme nedeniyle katı AgCl miktarı artar, bu yüzden t₂ anındaki kütle t₁ öncesinden daha büyüktür')}
r=onc_t(d,2)
ag_c=' '.join(f'({t:.2f},{agt(t):.4f})' for t in [3+i*.5 for i in range(11)])
cl_c=' '.join(f'({t:.2f},{clt(t):.4f})' for t in [3+i*.5 for i in range(11)])
g='''\\begin{axis}[width=7.6cm,height=5.8cm,xmin=0,xmax=11,ymin=0,ymax=3,xtick={3,8},xticklabels={$t_1$,$t_2$},ytick={0,0.5,1,2,2.5},yticklabels={0,0{,}5,1,2,2{,}5},tick label style={font=\\small},axis lines=left,
xlabel={Zaman},ylabel={Derişim ($\\times10^{-5}$ M)},xlabel style={font=\\small},ylabel style={font=\\small},clip=false]
\\addplot[thick] coordinates {(0,1) (3,1) '''+ag_c+''' (11,0.5)};
\\addplot[thick,dashed] coordinates {(0,2) (3,2) (3,2.5) '''+cl_c+''' (11,2)};
\\draw[dotted,gray] (axis cs:3,0) -- (axis cs:3,3);\\draw[dotted,gray] (axis cs:8,0) -- (axis cs:8,3);\\node[anchor=south] at (axis cs:9.8,2.05) {[Cl$^-$]}; \\node[anchor=south] at (axis cs:9.8,.55) {[Ag$^+$]};
\\end{axis}'''
SK=tk(g)
q('0018','denge','AgCl dengesine NaCl eklenmesi, derişim–zaman grafiği',
 [adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),sonuc(d,r)],
 metin='Sıcaklığı sabit tutulan bir kapta AgCl katısı ile sulu çözeltisi dengededir. t₁ anında kaba, hacmi değiştirmeden bir miktar NaCl katısı eklenmiş ve katı tamamen çözünmüştür. Çözeltideki Ag⁺ ve Cl⁻ derişimlerinin zamanla değişimi grafikte gösterilmiştir.\nI. t₁ ile t₂ arasında çökelme hızı, çözünme hızından büyüktür.\nII. t₂ anından sonra [Ag⁺] · [Cl⁻] çarpımı, t₁ anından önceki değere eşittir.\nIII. t₂ anında kaptaki katı AgCl kütlesi, t₁ anından önceki kütlesinden küçüktür.\nBuna göre bu yargılardan hangileri doğrudur?',
 sekil=SK,z='zor',alt='Dengeyi Etkileyen Faktörler',kaz='Ortak iyon eklenmesiyle bozulan çözünme dengesini derişim–zaman grafiğinden yorumlar.',kalip='grafik',
 istenen='Doğru olan yargılar.',ip=['Grafikten t₁ öncesi ve t₂ sonrası iyon çarpımlarını hesapla; derişimlerin hangi yönde değiştiği katının miktarı hakkında bilgi verir.'],
 bilgi=[B('Denge bozulduğunda hız ve çarpım','Dengeye ortak iyon eklenince iyon çarpımı Kçç’yi aşar ve çökelme hızı çözünme hızından büyük olur; yeni dengede Q yine Kçç’ye eşittir. Örnek: BaSO₄ dengesine Na₂SO₄ eklenince BaSO₄ çöker')],
 puf='Yeni dengede Q = Kçç aynıdır, ama iyon derişimleri ve katı miktarı değişir.',**r)

# ============ 19 · Kçç–sıcaklık tablosu ile çökelme · öncüllü · zor ============
kartla('19','sicaklik','Sıcaklığın çökelme koşuluna etkisi','Karışımın iyon çarpımı sabit; Kçç sıcaklıkla artıyorsa çökelme yalnız düşük sıcaklıkta olur ve ısıtınca çökelti çözünür.','Q’yu sıcaklıkla değişen sanmak; Kçç’nin artmasını çözünmenin ekzotermik olmasına yormak.','zor','öncüllü',5)
Kt={25:E(2,-6),50:E(8,-6)}
xm=Fr(4,10**3)*Fr(1,2); ym=xm; Qm=xm*ym; assert Qm==E(4,-6)
assert Qm>Kt[25] and Qm<Kt[50] and Kt[50]>Kt[25]
d={'I':(False,'25 °C’de Q = 4 × 10⁻⁶, Kçç = 2 × 10⁻⁶’dan büyüktür; bu nedenle çökelme olur, çökelme olmaz yargısı doğru değildir'),
   'II':(Qm<Kt[50],'50 °C’de Q = 4 × 10⁻⁶, Kçç = 8 × 10⁻⁶’dan küçüktür; çözelti doymamıştır ve çökelme olmaz'),
   'III':(Kt[50]>Qm,'Kçç sıcaklıkla arttığından 50 °C’de Q < Kçç olur; 25 °C’de oluşan çökelti ısıtılınca tamamen çözünür')}
d['III']=(True,d['III'][1])
r=onc_t(d,4)
SK=tablo_svg(['Sıcaklık (°C)','XY için Kçç'],[['25','2 × 10⁻⁶'],['50','8 × 10⁻⁶']])
q('0019','sicaklik','XY için iki sıcaklıkta Kçç ve karışım',
 [adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),sonuc(d,r)],
 metin='XY tuzunun Kçç değerleri iki farklı sıcaklıkta tabloda verilmiştir. Bir öğrenci 100 mL 4 × 10⁻³ M X⁺ iyonu içeren çözelti ile 100 mL 4 × 10⁻³ M Y⁻ iyonu içeren çözeltiyi 25 °C’de karıştırıyor ve oluşan karışımı 50 °C’ye ısıtıyor. Hacimler toplanabilmekte, çözeltilerde başka tepkime olmamaktadır.\nI. 25 °C’de karıştırıldığında çökelme olmaz.\nII. Aynı karışım 50 °C’de hazırlansaydı çökelme olmazdı.\nIII. 25 °C’de oluşan çökelti, karışım 50 °C’ye ısıtılınca tamamen çözünür.\nBuna göre bu yargılardan hangileri doğrudur?',
 sekil=SK,z='zor',alt='Sıcaklığın Etkisi',kaz='Karışımın iyon çarpımı ile farklı sıcaklıklardaki Kçç değerlerini karşılaştırarak çökelmeyi yorumlar.',kalip='tablo',
 istenen='Doğru olan yargılar.',ip=['Karışımdaki iyon derişimlerini bulup iyon çarpımını hesapla; sonra her sıcaklıktaki Kçç ile ayrı ayrı karşılaştır.'],
 bilgi=[B('Çökelti ve sıcaklık','Çözünmesi endotermik olan tuzun Kçç değeri sıcaklıkla artar; bu yüzden aynı iyon çarpımında düşük sıcaklıkta çöken tuz yüksek sıcaklıkta çözünebilir. Örnek: Q = 9 × 10⁻⁸ iken Kçç 5 × 10⁻⁸’den 2 × 10⁻⁷’ye çıkıyorsa çökelti çözünür')],
 puf='Q karışıma bağlıdır, Kçç sıcaklığa; her sıcaklıkta ayrı karşılaştır.',**r)

# ============ 20 · seyreltme + ortak iyon · zor · düzenek ============
kartla('20','ortak','Seyreltilmiş ortak iyon çözeltisinde çözünürlük','Önce seyrelme ile ortak iyon derişimi bulunur; sonra çözünürlük Kçç ÷ [F⁻]².','Seyrelmeyi atlamak; F⁻ derişiminin karesini almamak.','zor','şekilli',5)
KF=E(4,-11); n_F=Fr(50,1000)*E(4,-2); cF=n_F/Fr(200,1000)
assert cF==E(1,-2)
s20=KF/cF**2; assert s20==E(4,-7)
a1=KF/E(4,-2)**2; a2=KF/cF; a3=KF/(cF/10)**2
assert a1==E('2,5',-8) and a2==E(4,-9) and a3==E(4,-5)
r=sn(s20,[(a2,'[F⁻] derişiminin karesini almayıp s = 4 × 10⁻¹¹ ÷ 1 × 10⁻² = 4 × 10⁻⁹ M bulmuş.','islem'),
          (a1,'Seyrelmeyi hesaba katmayıp [F⁻] = 0,04 M almış: s = 4 × 10⁻¹¹ ÷ (4 × 10⁻²)² = 2,5 × 10⁻⁸ M.','dikkat'),
          (Fr(1,10**7),'F⁻ derişimini 2 × 10⁻² M almış (50 mL’yi 100 mL’ye seyrelterek): s = 4 × 10⁻¹¹ ÷ (2 × 10⁻²)² = 1 × 10⁻⁷ M.','islem'),
          (a3,'Çözeltiyi 2 L’ye seyrelmiş sanıp [F⁻] = 1 × 10⁻³ M almış: s = 4 × 10⁻¹¹ ÷ (1 × 10⁻³)² = 4 × 10⁻⁵ M.','dikkat')])
assert KF/Fr(2,10**2)**2==E(1,-7)
print('q20 poz',poz(r))
g=kap(0,2.1,2.4,1.7)+'\\node[align=center] at (1.05,.85) {\\scriptsize 0,04 M\\\\ \\scriptsize NaF};'
g+='\\node[below] at (1.05,-.05) {\\scriptsize 50 mL};'
g+=f'\\draw[{ARR},thick] (2.35,1.4) -- (3.5,1.4); \\node[above,align=center] at (2.92,1.45) {{\\scriptsize + saf su}};'
# balon joje
g+='\\begin{scope}\\clip (4.8,1.2) circle (1.0);\\fill[vurgu!15] (3.7,.1) rectangle (5.9,1.5);\\end{scope}'
g+='\\draw[thick] (4.6,3.0) -- (4.6,2.18) arc[start angle=101.5,end angle=438.5,radius=1.0] -- (5.0,3.0);'
g+='\\draw (4.6,2.6) -- (5.0,2.6);'
g+='\\node[align=center] at (4.8,.8) {\\scriptsize NaF\\\\ \\scriptsize çözeltisi};'
g+='\\node[below] at (4.8,.15) {\\scriptsize 200 mL}; '
g+=f'\\draw[{ARR},thick] (6.1,1.2) -- (7.0,1.2);'
g+=kap(7.2,2.2,2.4,1.7)+kati(7.2,2.2,.4)+'\\node[anchor=west] at (7.35,.72) {\\scriptsize CaF$_2$(k)};'
SK=tk(g)
q('0020','ortak','NaF çözeltisinin seyreltilip CaF₂ eklenmesi',
 [A('Seyrelmeyi hesapla','Mol sayısı değişmez; hacim 50 mL’den 200 mL’ye çıkar.','n = 0,05 · 0,04 = 2 × 10⁻³ mol · [F⁻] = 2 × 10⁻³ ÷ 0,2 = 0,01 M'),
  A('Ortak iyonu belirle','NaF’den gelen F⁻ derişimi, CaF₂’nin çözünmesinden gelen F⁻ yanında baskındır.','[F⁻] ≈ 1 × 10⁻² M'),
  A('Kçç ifadesinden Ca²⁺ derişimini bul','Kçç = [Ca²⁺] · [F⁻]²','[Ca²⁺] = 4 × 10⁻¹¹ ÷ (10⁻²)² = 4 × 10⁻⁷ M'),
  A('Çözünürlüğü yaz','Çözünen CaF₂ mol sayısı Ca²⁺ mol sayısına eşittir.','s = 4 × 10⁻⁷ M')],
 metin='Bir öğrenci 50 mL 0,04 M NaF çözeltisini şekilde görüldüğü gibi saf suyla 200 mL’ye tamamlıyor ve bu çözeltiye 25 °C’de CaF₂ katısı ekleyip doygun hâle getiriyor. CaF₂’nin Kçç değeri 4 × 10⁻¹¹’dir. CaF₂’nin çözünmesiyle çözeltiye geçen F⁻ iyonları ihmal edilecek ve katı ilavesiyle hacim değişmeyecektir.\nBuna göre CaF₂’nin bu çözeltideki molar çözünürlüğü kaç M’dir?',
 sekil=SK,z='zor',alt='Ortak İyon Etkisi',kaz='Seyrelmiş ortak iyon çözeltisinde az çözünen tuzun molar çözünürlüğünü hesaplar.',kalip='şekilli',
 istenen='CaF₂’nin molar çözünürlüğü (M).',ip=['Önce F⁻ iyonlarının son derişimini bul; çözünürlüğü, çözünen tuzdan gelen iyonlar üzerinden yaz.'],
 bilgi=[B('Seyrelme ve ortak iyon','Seyrelmede mol sayısı sabit kalır, derişim hacimle ters orantılı değişir. Örnek: 100 mL 0,2 M çözelti 400 mL’ye tamamlanırsa derişim 0,05 M olur')],
 puf='Önce seyrelmeyi çöz, sonra ortak iyon derişimini Kçç ifadesine yerleştir.',**r)

# ---------- kayıt ----------
def bitir_ayt(P,onek,k):
    for q_ in P.ANA: q_['kardes']=None
    P.yaz(os.path.join(GD,f'{onek}-1.json'),f'/tmp/bos-{onek}.json')
    tipler={}
    for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=k))['kartlar'].append(c['id'])
    json.dump(dict(konu=P.konu_adi,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2018–2025 Kimya çıkmış soruları, MEB 12. sınıf müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar',f'ak{onek}.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler),'soru',len(P.ANA))
bitir_ayt(P,'ksp',UK)
