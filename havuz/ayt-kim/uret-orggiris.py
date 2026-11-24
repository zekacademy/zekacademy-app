"""AYT Kimya · Organik Kimyaya Giriş · 20 soru (kardeş yok, ipucu 1). Şekil verileri ve cevaplar Python'da hesaplanır (Fraction), TikZ aynı değerlerden üretilir."""
import sys,os,json,math
from itertools import combinations
HV='/home/claude/zekacademy-app/havuz'; HD=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,HV); sys.path.insert(0,HV+'/tyt-kim')
import _hafif_kim2 as H
from _hafif_kim2 import *
from fractions import Fraction as Fr
from math import gcd
HD='/home/claude/zekacademy-app/havuz/ayt-kim'
KONU_='Organik Kimyaya Giriş'; UK='akim|Organik Kimyaya Giriş'
H.KONU=KONU_
P=Parti('orggiris',KONU_,UK,ders='AYT Kimya',idon='aytkim')
KY='ÖSYM AYT Kimya 2018–2026 (yalnız mantık) · MEB 12. sınıf Karbon Kimyasına Giriş'
TIPK={}
def kartla(n,alt,fikir,tuzak,z,kalip,adim,tipad,tip):
    kart(f'K-AKOG-{n}',alt,fikir,tuzak,z,kalip,adim,f'og-{tipad}',tip,KY)
def q(no,ad,**k):
    assert len(k['ip'])==1
    mk(P,no,ad=ad,adim=len(ad),**k)
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
def tk(g,head=HEAD): return tikz_svg(head+g+TAIL)
# ---------------- yardımcılar ----------------
def yer(dogru,yan,harf):
    """metin şıkları: doğruyu istenen harfe koy, yanlışlar verilen sırayla."""
    s=[y[0] for y in yan]; s.insert('ABCDE'.index(harf),dogru); assert len(set(s))==5; return s
STD=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
def etiket(S):
    S=sorted(S,key=['I','II','III'].index)
    if len(S)==1: return 'Yalnız '+S[0]
    if len(S)==3: return 'I, II ve III'
    return ' ve '.join(S)
def oc(T,harf,why):
    """T: doğru öncüller kümesi; why[n]: gerekçe (küçük harfle başlayan yan cümle). Şık sırası alışılmış; doğru harf istenen yerde."""
    dog=etiket(T); hedef='ABCDE'.index(harf)
    for cb in combinations(range(7),5):
        L=[STD[i] for i in cb]
        if dog in L and L.index(dog)==hedef: break
    else: raise AssertionError(('uygun şık dizisi yok',dog,harf))
    yan=[]
    for o in L:
        if o==dog: continue
        S=set(o.replace('Yalnız ','').replace(', ',' ve ').split(' ve '))
        parts=[]
        for n in ['I','II','III']:
            if n in S and n not in T: parts.append(f'{n} yargısını doğru kabul etmiş; {why[n]}.')
            elif n not in S and n in T: parts.append(f'{n} yargısını yanlış kabul etmiş; {why[n]}.')
        assert parts
        yan.append((o,' '.join(parts),'bilgi'))
    return dog,yan,L
def dot(x,y,r=1.5): return f'\\fill ({x:.3f},{y:.3f}) circle ({r}pt);'
def mol(atoms,bonds,lw='.9pt'):
    """atoms: ad->(x,y,etiket|None); bonds: (a,b,mertebe). Etiketli atomlara bağ çizgisi kısaltılır."""
    o=[]
    def sh(lbl,ux,uy):
        if not lbl: return 0
        if lbl.startswith('CH'): return abs(ux)*.55+abs(uy)*.3
        return .26
    for a,b,od in bonds:
        xa,ya,la=atoms[a]; xb,yb,lb=atoms[b]; dx,dy=xb-xa,yb-ya; Lg=math.hypot(dx,dy); ux,uy=dx/Lg,dy/Lg
        sa,sb=sh(la,ux,uy),sh(lb,ux,uy); x1,y1=xa+ux*sa,ya+uy*sa; x2,y2=xb-ux*sb,yb-uy*sb; px,py=-uy,ux
        for t in {1:[0],2:[-.07,.07],3:[-.13,0,.13]}[od]:
            o.append(f'\\draw[line width={lw}] ({x1+px*t:.3f},{y1+py*t:.3f}) -- ({x2+px*t:.3f},{y2+py*t:.3f});')
    for n,(x,y,l) in atoms.items():
        if l: o.append(f'\\node at ({x:.3f},{y:.3f}) {{{l}}};')
    return '\n'.join(o)
def pol(x,y,d,r=1.0): a=math.radians(d); return (x+r*math.cos(a),y+r*math.sin(a))
def hcount(atoms_c,bonds):
    """C atomlarının H sayısı (4 − bağ mertebesi toplamı); C dışı atomlar için bağ toplamı doğrulanır."""
    tot={n:0 for n in atoms_c}
    for a,b,od in bonds:
        tot[a]+=od; tot[b]+=od
    return tot
# ---------------- kartlar ----------------
kartla('01','Organik–anorganik ayrımı','Organik bileşik: yapısında C–H bağı bulunan karbon bileşikleri; karbon içeren CO, CO₂, karbonat, bikarbonat, karbür ve siyanürler anorganik sınıfta incelenir.','Karbon içeren her bileşiği organik saymak; CCl₄ gibi H içermeyen ama organik sayılan bileşiği anorganik sanmak.','kolay','düz',2,'ayrim','Organik ve anorganik bileşiklerin ayrımı')
kartla('02','Karbonun bağ yapma özellikleri','Karbon dört değerlik elektronuyla dört kovalent bağ yapar; birbirine tek, çift, üçlü bağla bağlanıp zincir ve halka oluşturur; iyon oluşturmaz.','Karbonun elektron vererek C⁴⁺ ya da alarak C⁴⁻ oluşturduğunu düşünmek.','kolay','öncüllü',3,'karbon','Karbonun bağ yapma özellikleri ve allotroplar')
kartla('03','Sigma ve pi bağı sayımı','Her bağ çizgisinden biri σ’dır; çift bağda bir, üçlü bağda iki π bağı vardır; π sayısı = Σ(mertebe − 1).','Çoklu bağların hepsini σ saymak ya da C–H bağlarını atlamak.','orta','şekilli',3,'sigmapi','Açık formülden sigma ve pi bağı sayımı')
kartla('04','Hibritleşme türünü belirleme','Karbonun σ bağı sayısı + ortaklanmamış çift sayısı 4 ise sp³, 3 ise sp², 2 ise sp hibritleşmesi yapar; π bağı hibrit orbital kullanmaz.','Çift bağlı karbonu sp³ saymak; hibrit sayısını bağ çizgisi sayısıyla karıştırmak.','orta','şekilli',4,'hibrit','Hibritleşme türü, orbital diyagramı ve örtüşme')
kartla('05','Molekül geometrisi (VSEPR)','Merkez atom çevresindeki bağ ve ortaklanmamış elektron çiftleri birbirini en az itecek biçimde dizilir; ortaklanmamış çift bağ açısını küçültür.','Ortaklanmamış çifti geometride yok saymak; elektron çifti geometrisi ile molekül geometrisini karıştırmak.','orta','tablo',3,'geometri','Elektron çifti sayısından molekül geometrisi ve bağ açısı')
kartla('06','Basit formül ve molekül formülü','Kütlelerden mol sayısı, mol oranından basit formül bulunur; molekül formülü = basit formül × (mol kütlesi ÷ basit formül kütlesi).','Kütle oranını atom sayısı oranı saymak; n katını bütün atomlara uygulamamak.','orta','tablo',4,'formul','Basit formül, molekül formülü ve yanma analizi')
kartla('07','Yanma ürünlerinden bileşim','CO₂’deki C ve H₂O’daki H, bileşikten gelir; oksijen kütle farkından bulunur, ürünlerdeki O bileşikten gelmez.','Ürünlerdeki bütün oksijeni bileşiğe ait saymak; H₂O mol sayısını H atom sayısı almak.','zor','şekilli',5,'formul','Basit formül, molekül formülü ve yanma analizi')
kartla('08','Organik madde tanıma deneyi','Isıtılan maddeden CO₂ (kireç suyunu bulandırır) ve H₂O (susuz CuSO₄’ü maviye çevirir) çıkması C ve H varlığını gösterir; O ve organik olma sonucu kesin değildir.','Deneyden maddenin kesinlikle organik olduğunu ya da O içerdiğini sonuçlamak.','orta','şekilli',3,'ayrim','Organik ve anorganik bileşiklerin ayrımı')
# ============ 01 · kolay · olumsuz kök ============
W1=[('C₃H₈','Propanın (C₃H₈) yapısında oksijen bulunmadığı için organik olmadığını düşünmüş; oysa C–H bağları içeren hidrokarbonlar organiktir.','bilgi'),('C₆H₁₂O₆','Yapısında çok sayıda oksijen bulunduğu için anorganik sanmış; oysa C–H ve C–C bağları taşıyan glikoz organiktir.','bilgi'),('CH₃COOH','Asit olduğu için anorganik asitlerle karıştırmış; oysa C–H bağı içeren asetik asit organik bir bileşiktir.','bilgi'),('CH₃CH₂NH₂','Azot içerdiği için anorganik saymış; oysa C–H bağları taşıyan bu azotlu bileşik organiktir.','bilgi')]
q('0001',tipId='og-ayrim',tip='Organik ve anorganik bileşiklerin ayrımı',z='kolay',alt='Organik ve Anorganik Bileşikler',kaz='Karbon içeren bileşikleri organik ve anorganik olarak sınıflandırır.',kalip='düz',
 kart='K-AKOG-01 (organik–anorganik ayrımı) · karbonat ayırt etme',
 metin='Organik bileşikler, yapısında C–H bağı bulunan karbon bileşikleridir. Karbon içermelerine rağmen karbonatlar gibi bazı bileşikler anorganik sınıfında incelenir.\nBuna göre aşağıda formülleri verilen bileşiklerden hangisi organik bileşik değildir?',
 dogru='CaCO₃',yan=W1,sira=yer('CaCO₃',W1,'A'),
 istenen='Organik bileşik sınıfında yer almayan bileşik.',
 ip=['Her şıktaki karbonun hangi atomlarla bağ yaptığına ve C–H bağı bulunup bulunmadığına bak.'],
 bilgi=[B('Organik–anorganik ayrımı','Yapısında C–H bağı bulunan karbon bileşikleri organiktir. CO, CO₂, karbonatlar ve bikarbonatlar karbon içermelerine rağmen anorganik sayılır. Örnek: CH₄ organik, K₂CO₃ anorganiktir')],
 ad=[A('Ölçütü hatırla','Organik bileşiklerde karbon, C–H bağı yapar.','Organik: C–H bağlı karbon bileşiği'),A('Şıkları incele','Dört şıkta C–H bağları vardır; CaCO₃ ise Ca²⁺ ve CO₃²⁻ iyonlarından oluşur.','C₃H₈, C₆H₁₂O₆, CH₃COOH, CH₃CH₂NH₂ → organik'),A('Sonucu yaz','Karbonatlar anorganik sınıfta incelenir.','CaCO₃ → anorganik')],
 puf='Karbon içeren her bileşik organik değildir; oksit, karbonat ve bikarbonatlar anorganik sayılır.')
# ============ 02 · kolay · öncüllü ============
T2={'I','II'}
W2={'I':'karbon dört değerlik elektronuyla dört kovalent bağ yapabilir','II':'karbon atomları birbirine tek, çift ya da üçlü bağla bağlanarak zincir ve halka yapıları oluşturabilir','III':'oysa karbon bileşiklerinde iyon oluşmaz, karbon elektronlarını ortaklaşa kullanarak kovalent bağ yapar'}
d2,y2,L2=oc(T2,'B',W2)
q('0002',tipId='og-karbon',tip='Karbonun bağ yapma özellikleri ve allotroplar',z='kolay',alt='Karbonun Bağ Yapma Özellikleri',kaz='Karbon atomunun bağ yapma özelliklerini değerlik elektronlarıyla ilişkilendirir.',kalip='öncüllü',
 kart='K-AKOG-02 (karbonun bağ yapma özellikleri) · dört bağ, zincir–halka, iyon oluşturmama',
 metin='Karbon atomu, organik bileşiklerin temel yapı taşıdır ve çok sayıda farklı bileşik oluşturabilir.\nI. Karbon atomu, bileşiklerinde dört kovalent bağ yapabilir.\nII. Karbon atomları birbirine bağlanarak zincir ve halka yapıları oluşturabilir.\nIII. Karbon atomu bileşiklerinde elektron vererek C⁴⁺ iyonu hâlinde bulunur.\nBuna göre karbon atomu (₆C) ile ilgili bu yargılardan hangileri doğrudur?',
 dogru=d2,yan=y2,sira=L2,istenen='Doğru olan yargılar.',
 ip=['Karbonun değerlik elektron sayısını bul ve bu elektronları ya vermesi mi, alması mı, yoksa ortaklaşa kullanması mı gerektiğini düşün.'],
 bilgi=[B('Karbonun değerlik elektronları','₆C: 2, 4 → son katmanında 4 elektron vardır; elektron vermek ya da almak çok enerji gerektirdiğinden elektronlarını ortaklaşa kullanır ve dört kovalent bağ yapar. Örnek: ₁₄Si de aynı nedenle dört bağ yapar')],
 ad=[A('Elektron dizilimini yaz','Karbonun atom numarası 6’dır.','₆C: 2, 4 → 4 değerlik elektronu'),A('I’i değerlendir','Oktete ulaşmak için dört elektron ortaklaşa kullanılır.','4 elektron ortaklaşa → 4 kovalent bağ → I doğru'),A('II’yi değerlendir','Karbon birbirine tek, çift, üçlü bağla bağlanır; zincir ve halka oluşturur.','Zincir + halka → II doğru'),A('III’ü değerlendir','Dört elektron vermek aşırı enerji ister; karbon iyon yapmaz.','C⁴⁺ oluşmaz → III yanlış'),A('Sonucu yaz','Doğru yargılar I ve II’dir.','I ve II')],
 puf='Karbon iyon değil, kovalent bağ yapar; bu yüzden dört bağ yapıp zincir ve halka kurabilir.')
# ============ 03 · kolay · şekilli · sigma sayısı ============
at={'C1':(0,0,'C'),'C2':(1.35,0,'C'),'H1':(-1.1,0,'H'),'H2':(0,1.05,'H'),'H3':(0,-1.05,'H'),'H4':(2.45,0,'H'),'H5':(1.35,1.05,'H'),'H6':(1.35,-1.05,'H')}
bd=[('C1','C2',1)]+[('C1',h,1) for h in ('H1','H2','H3')]+[('C2',h,1) for h in ('H4','H5','H6')]
sig3=len(bd); pi3=sum(b[2]-1 for b in bd); assert (sig3,pi3)==(7,0)
assert 6==sig3-1 and 8==len(at) and 2*sig3==14
SK3=tk(mol(at,bd))
q('0003',tipId='og-sigmapi',tip='Açık formülden sigma ve pi bağı sayımı',z='kolay',alt='Sigma ve Pi Bağları',kaz='Açık formülü verilen bir molekülde sigma ve pi bağı sayısını belirler.',kalip='şekilli',
 kart='K-AKOG-03 (σ ve π bağı sayımı) · etan',sekil=SK3,
 metin='Karbon atomları arasında ve karbonla hidrojen arasında oluşan bağlar sigma (σ) ya da pi (π) bağıdır. Etan molekülünün açık formülü şekilde verilmiştir.\nBuna göre etan molekülündeki toplam σ bağı sayısı kaçtır?',
 dogru=7,yan=[(1,'Yalnız C–C bağını σ sayıp C–H bağlarını σ saymamış; oysa her tek bağ bir σ bağıdır.','bilgi'),(6,'C–H bağlarını saymış, C–C bağını atlamış.','dikkat'),(8,'Moleküldeki toplam atom sayısını (2 C + 6 H = 8) bağ sayısı sanmış.','dikkat'),(14,'Bağ çizgisi başına iki elektron düşünüp bağ yapan elektron sayısını (7 × 2 = 14) bağ sayısı olarak vermiş.','islem')],
 istenen='Moleküldeki toplam sigma bağı sayısı.',
 ip=['Şekildeki her bağ çizgisini tek tek say; çizginin kaç bağ içerdiğini bağın mertebesine göre değerlendir.'],
 bilgi=[B('σ ve π bağları','İki atom arasındaki ilk bağ her zaman σ bağıdır; çift bağda bir σ + bir π, üçlü bağda bir σ + iki π bulunur. Örnek: H–Cl molekülünde 1 σ bağı vardır')],
 ad=[A('Bağ çizgilerini say','C–H bağları ve C–C bağı ayrı sayılır.','C–H: 6 · C–C: 1'),A('Bağ türünü belirle','Hepsi tek bağdır; tek bağ bir σ bağıdır.','Tek bağ = 1 σ'),A('Toplamı bul','σ sayısı çizgi sayısına eşittir.','σ = 6 + 1 = 7')],
 puf='Tek bağların tamamı σ bağıdır; π bağı yalnız çift ve üçlü bağlarda ortaya çıkar.')
# ============ 04 · orta · şekilli · öncüllü · eten ============
at={'C1':(0,0,'C'),'C2':(1.3,0,'C')}
for i,(x,y) in enumerate([pol(0,0,120,1.05),pol(0,0,240,1.05),pol(1.3,0,60,1.05),pol(1.3,0,300,1.05)]): at[f'H{i}']=(x,y,'H')
bd=[('C1','C2',2),('C1','H0',1),('C1','H1',1),('C2','H2',1),('C2','H3',1)]
assert (len(bd),sum(b[2]-1 for b in bd))==(5,1)
SK4=tk(mol(at,bd))
T4={'I','III'}
W4={'I':'her karbon üç σ bağı yaptığı ve ortaklanmamış elektron çifti olmadığı için sp² hibritleşmesi yapar','II':'p orbitallerinin yan yana örtüşmesiyle oluşan bağ π bağıdır; σ bağı orbitallerin uç uca örtüşmesiyle oluşur','III':'sp² hibritleşmesi yapan karbonların bağları aynı düzlemde olduğundan bütün atomlar aynı düzlemdedir'}
d4,y4,L4=oc(T4,'D',W4)
q('0004',tipId='og-hibrit',tip='Hibritleşme türü, orbital diyagramı ve örtüşme',z='orta',alt='Hibritleşme',kaz='Çift bağ içeren bir molekülde hibritleşme türünü, bağların örtüşme biçimini ve geometriyi belirler.',kalip='öncüllü',
 kart='K-AKOG-04 (hibritleşme türü) · eten',sekil=SK4,
 metin='Eten (etilen) molekülünün açık formülü şekilde verilmiştir. (₁H, ₆C)\nBuna göre eten molekülü ile ilgili,\nI. Karbon atomlarının her ikisi de sp² hibritleşmesi yapmıştır.\nII. Karbon atomları arasındaki bağlardan biri, p orbitallerinin yan yana örtüşmesiyle oluşan σ bağıdır.\nIII. Molekülün bütün atomları aynı düzlemdedir.\nyargılarından hangileri doğrudur?',
 dogru=d4,yan=y4,sira=L4,istenen='Doğru olan yargılar.',
 ip=['Her karbonun kaç σ bağı yaptığını say; bu sayı hibrit orbital sayısını verir. Sonra yan yana örtüşmenin hangi bağı oluşturduğunu hatırla.'],
 bilgi=[B('Hibritleşme ve bağ türü','Merkez atomun σ bağı sayısı + ortaklanmamış çift sayısı = hibrit orbital sayısıdır: 4 → sp³, 3 → sp², 2 → sp. Hibrit orbitaller uç uca örtüşerek σ, hibritleşmeyen p orbitalleri yan yana örtüşerek π bağı yapar. Örnek: formaldehitte (CH₂O) karbon sp²’dir')],
 ad=[A('σ bağlarını say','Her karbon iki C–H ve bir C–C σ bağı yapar.','Karbon başına 3 σ → sp²'),A('I’i değerlendir','Üç hibrit orbital sp² hibritleşmesini gösterir.','I doğru'),A('II’yi değerlendir','Yan yana örtüşme π bağı verir; σ bağı uç uca örtüşmeyle oluşur.','II yanlış'),A('III’ü değerlendir','sp² hibrit orbitalleri aynı düzlemde 120° yapar; π bağı da bu düzleme dik p orbitallerinden oluşur.','III doğru'),A('Sonucu yaz','Doğru yargılar I ve III’tür.','I ve III')],
 puf='Çift bağlı karbon sp²’dir: üç σ bağı aynı düzlemdedir, π bağı bu düzlemin üstünde ve altındadır.')
# ============ 05 · orta · şekilli · öncüllü · orbital diyagramı ============
def kutu(x,y,spins):
    o=[f'\\draw[thick] ({x:.2f},{y:.2f}) rectangle ({x+.7:.2f},{y+.7:.2f});']
    if len(spins)==2:
        o.append(f'\\draw[-{{Stealth[length=1.6mm]}},thick] ({x+.22:.2f},{y+.1:.2f}) -- ({x+.22:.2f},{y+.58:.2f});')
        o.append(f'\\draw[-{{Stealth[length=1.6mm]}},thick] ({x+.48:.2f},{y+.58:.2f}) -- ({x+.48:.2f},{y+.1:.2f});')
    elif len(spins)==1:
        o.append(f'\\draw[-{{Stealth[length=1.6mm]}},thick] ({x+.35:.2f},{y+.1:.2f}) -- ({x+.35:.2f},{y+.58:.2f});')
    return o
rows=[('X',[2,1,1,0],'sp'),('Y',[1,1,1,1],'sp'),('Z',[1,1,1,1],'hib')]
eX=[2,1,1,0]; eY=[1,1,1,1]; eZ=[1,1,1,1]
assert sum(eX)==sum(eY)==sum(eZ)==4
unp=lambda L: sum(1 for e in L if e==1)
assert (unp(eX),unp(eY),unp(eZ))==(2,4,4)
g=[]
for r,(nm,L,tur_) in enumerate(rows):
    y0=-r*2.0
    g.append(f'\\node[font=\\small\\bfseries] at (0.1,{y0+.75:.2f}) {{{nm}}};')
    for i,e in enumerate(L):
        if tur_=='hib':
            x=.8+i*.85; yy=y0+.45; lab='sp$^3$'
        else:
            x=.8+(0 if i==0 else .6+i*.85); yy=y0+(.0 if i==0 else .6); lab='2s' if i==0 else '2p'
        g+=kutu(x,yy,[0]*e)
        g.append(f'\\node at ({x+.35:.2f},{yy-.3:.2f}) {{{lab}}};')
SK5=tk('\n'.join(g))
T5={'II','III'}
W5={'I':'temel hâldeki karbonun yalnız 2p orbitallerinde iki eşleşmemiş elektron vardır; 4 değildir','II':'Y’de dört orbitalin her birinde birer elektron bulunur ve eşleşmemiş elektron sayısı 4’tür','III':'Z’deki dört orbital eş enerjilidir ve 2s ile üç 2p orbitalinin karışmasıyla oluşmuştur'}
d5,y5,L5=oc(T5,'E',W5)
q('0005',tipId='og-hibrit',tip='Hibritleşme türü, orbital diyagramı ve örtüşme',z='orta',alt='Hibritleşme',kaz='Karbonun temel hâl, uyarılmış hâl ve hibrit orbital diyagramlarını yorumlar.',kalip='öncüllü',
 kart='K-AKOG-04 (hibritleşme türü) · orbital diyagramı X, Y, Z',sekil=SK5,
 metin='Karbon atomunun (₆C) değerlik katmanındaki elektronlarının, üç farklı durumdaki orbital diyagramı şekilde gösterilmiştir. Kutular orbitalleri, oklar elektronları temsil eder.\nBuna göre bu diyagramlarla ilgili,\nI. X’te eşleşmemiş elektron sayısı 4’tür.\nII. Y’de eşleşmemiş elektron sayısı 4’tür.\nIII. Z’deki dört orbital eş enerjilidir ve 2s ile 2p orbitallerinin karışmasıyla oluşmuştur.\nyargılarından hangileri doğrudur?',
 dogru=d5,yan=y5,sira=L5,istenen='Doğru olan yargılar.',
 ip=['Her diyagramda yalnız tek okla gösterilen elektronları say; eş enerjili dört kutunun neyi gösterdiğini düşün.'],
 bilgi=[B('Hibrit orbital','Bir atomun s ve p orbitalleri karışıp aynı sayıda, eş enerjili yeni orbitaller oluşturabilir: 1 s + 3 p → 4 sp³. Örnek: ₅B atomunun 1 s + 2 p orbitalinden 3 sp² orbitali oluşur')],
 ad=[A('X’i oku','2s dolu (↑↓), 2p’de iki tek elektron var.','X: eşleşmemiş = 2 → I yanlış'),A('Y’yi oku','Bir elektron 2s’den 2p’ye geçmiş; dört orbitalde birer elektron var.','Y: eşleşmemiş = 4 → II doğru'),A('Z’yi oku','Dört kutu aynı hizada ve birer elektronlu: hibrit orbitaller.','Z: 4 eş enerjili orbital → III doğru'),A('Sonucu yaz','Doğru yargılar II ve III’tür.','II ve III')],
 puf='Hibritleşmede orbital sayısı ve elektron sayısı değişmez; yalnız orbitaller karışıp eş enerjili hâle gelir.')
# ============ 06 · orta · şekilli · sp atom sayısı ============
lay=[('C1',(0,0)),]
A_=1.25
c1=(0,0); c2=(A_,0); c3=pol(*c2,-60,A_); n_=pol(*c3,-60,A_)
at={'C1':(*c1,'C'),'C2':(*c2,'C'),'C3':(*c3,'C'),'N':(*n_,'N')}
h=[pol(*c1,120,1.0),pol(*c1,240,1.0),pol(*c2,60,1.0)]
for i,p in enumerate(h): at[f'H{i}']=(*p,'H')
bd=[('C1','C2',2),('C2','C3',1),('C3','N',3),('C1','H0',1),('C1','H1',1),('C2','H2',1)]
sig6=len(bd); pi6=sum(b[2]-1 for b in bd); assert (sig6,pi6)==(6,3)
# hibritleşme: atom başına (σ sayısı + ortaklanmamış çift)
nb={}
for a,b,o in bd: nb[a]=nb.get(a,0)+1; nb[b]=nb.get(b,0)+1
hib={'C1':nb['C1'],'C2':nb['C2'],'C3':nb['C3'],'N':nb['N']+1}   # N: 1 σ + 1 ortaklanmamış çift
tur_={k:{4:'sp3',3:'sp2',2:'sp'}[v] for k,v in hib.items()}
assert tur_=={'C1':'sp2','C2':'sp2','C3':'sp','N':'sp'}
nsp=sum(1 for v in tur_.values() if v=='sp'); nsp2=sum(1 for v in tur_.values() if v=='sp2'); assert (nsp,nsp2)==(2,2)
assert 1==sum(1 for k,v in tur_.items() if v=='sp' and k.startswith('C')) and 3==pi6 and 6==sig6 and 4==nsp+nsp2
SK6=tk(mol(at,bd))
q('0006',tipId='og-hibrit',tip='Hibritleşme türü, orbital diyagramı ve örtüşme',z='orta',alt='Hibritleşme',kaz='Çoklu bağ içeren bir molekülde atomların hibritleşme türünü belirler ve sayar.',kalip='şekilli',
 kart='K-AKOG-04 (hibritleşme türü) · akrilonitril',sekil=SK6,
 metin='Akrilonitrilin (vinil siyanür) açık formülü şekilde verilmiştir. Bir atomun hibritleşmesi, o atom çevresindeki σ bağı sayısı ile ortaklanmamış elektron çifti sayısının toplamına göre belirlenir. (₁H, ₆C, ₇N)\nBuna göre bu molekülde sp hibritleşmesi yapan atomların sayısı kaçtır?',
 dogru=2,yan=[(1,'Yalnız karbon atomlarına bakmış; azotun da bir σ bağı ve bir ortaklanmamış elektron çifti olduğundan sp hibritleşmesi yaptığını görmemiş.','dikkat'),(3,'Molekülde bulunan π bağı sayısını (1 + 2 = 3) sp atomu sayısı sanmış.','bilgi'),(4,'Çoklu bağ içeren bütün atomları (sp² ve sp) sp hibritleşmesi yapmış saymış.','bilgi'),(6,'Moleküldeki σ bağı sayısını (6) hibrit atom sayısı olarak vermiş.','islem')],
 istenen='sp hibritleşmesi yapan atomların toplam sayısı.',
 ip=['Üçlü bağ yapan atomlar ile çift bağ yapan atomların çevresindeki σ bağı ve ortaklanmamış çift sayılarını ayrı ayrı bul.'],
 bilgi=[B('Atomun hibritleşmesi','σ bağı sayısı + ortaklanmamış çift sayısı: 2 → sp, 3 → sp², 4 → sp³. Örnek: HCN’de karbonun 2 σ bağı vardır → sp; CH₂O’da karbonun 3 σ bağı vardır → sp²')],
 ad=[A('Karbon atomlarını incele','CH₂= karbonu 3 σ (2 C–H, 1 C–C), =CH– karbonu 3 σ yapar; C≡ karbonu 2 σ yapar.','C₁: 3 → sp² · C₂: 3 → sp² · C₃: 2 → sp'),A('Azotu incele','Azotun C≡N bağındaki 1 σ bağı ve 1 ortaklanmamış çifti vardır.','N: 1 + 1 = 2 → sp'),A('Sayımı yap','sp hibritleşmesi yapanlar: üçlü bağlı karbon ve azot.','sp: C₃ ve N → 2')],
 puf='Üçlü bağın her iki ucundaki atom sp’dir; hibritleşmeyi karbonla sınırlama, azot ve oksijene de uygula.')
# ============ 07 · orta · tablo · geometri ============
GEO={(2,0):'doğrusal',(3,0):'düzlem üçgen',(4,0):'düzgün dörtyüzlü',(3,1):'üçgen piramit',(2,2):'kırık doğru'}
vX,vY,vZ=(3,0),(4,0),(2,2)
SK7=tablo_svg(['Molekül','Bağ yapan e⁻ çifti','Ortaklanmamış e⁻ çifti'],[['X',str(vX[0]),str(vX[1])],['Y',str(vY[0]),str(vY[1])],['Z',str(vZ[0]),str(vZ[1])]])
def f7(a,b,c): return f'X: {a}, Y: {b}, Z: {c}'
dg7=f7(GEO[vX],GEO[vY],GEO[vZ]); assert dg7=='X: düzlem üçgen, Y: düzgün dörtyüzlü, Z: kırık doğru'
W7=[(f7('düzlem üçgen','düzgün dörtyüzlü','doğrusal'),'Z’deki iki ortaklanmamış elektron çiftini geometride yok sayıp yalnız iki bağ çiftine bakarak doğrusal bulmuş.','bilgi'),
    (f7('düzgün dörtyüzlü','düzlem üçgen','kırık doğru'),'Bağ çifti sayılarını karıştırarak 3 bağ çiftli X’i dörtyüzlü, 4 bağ çiftli Y’yi düzlem üçgen saymış.','dikkat'),
    (f7('düzlem üçgen','düzgün dörtyüzlü','üçgen piramit'),'Z’yi, üç bağ çifti ve bir ortaklanmamış çifti olan amonyak gibi üçgen piramit saymış; oysa Z’de iki bağ çifti ve iki ortaklanmamış çift vardır.','bilgi'),
    (f7('düzlem üçgen','düzgün dörtyüzlü','düzgün dörtyüzlü'),'Z’nin toplam elektron çifti sayısına (2 + 2 = 4) bakıp elektron çifti geometrisini molekül geometrisi olarak vermiş.','bilgi')]
q('0007',tipId='og-geometri',tip='Elektron çifti sayısından molekül geometrisi ve bağ açısı',z='orta',alt='Molekül Geometrisi',kaz='Merkez atom çevresindeki bağ ve ortaklanmamış elektron çifti sayısından molekül geometrisini belirler.',kalip='tablo',
 kart='K-AKOG-05 (VSEPR) · tablodan geometri',sekil=SK7,
 metin='X, Y ve Z moleküllerinde merkez atom çevresindeki bağ yapan ve ortaklanmamış elektron çiftlerinin sayıları şekildeki tabloda verilmiştir. Merkez atom çevresindeki elektron çiftleri birbirini en az itecek biçimde yerleşmektedir.\nBuna göre X, Y ve Z moleküllerinin geometrileri aşağıdakilerden hangisinde doğru verilmiştir?',
 dogru=dg7,yan=W7,sira=yer(dg7,W7,'E'),istenen='X, Y ve Z moleküllerinin geometrileri.',
 ip=['Elektron çiftlerinin toplam sayısı dizilişi belirler; ancak molekül geometrisi adlandırılırken yalnız atomların konumuna bakılır.'],
 bilgi=[B('VSEPR ve molekül geometrisi','Bağ + ortaklanmamış çift sayısı 4 ise elektron çiftleri dörtyüzlü dizilir; ortaklanmamış çift sayısı arttıkça molekül geometrisi değişir: 4 bağ → dörtyüzlü, 3 bağ + 1 çift → üçgen piramit. Örnek: 3 bağ çiftli ve ortaklanmamış çifti olmayan BCl₃ düzlem üçgendir')],
 ad=[A('X’i değerlendir','3 bağ çifti, ortaklanmamış çift yok; üç atom aynı düzlemde 120° yapar.','X: düzlem üçgen'),A('Y’yi değerlendir','4 bağ çifti, ortaklanmamış çift yok; atomlar dörtyüzlünün köşelerindedir.','Y: düzgün dörtyüzlü'),A('Z’yi değerlendir','2 bağ çifti + 2 ortaklanmamış çift: toplam 4 çift dörtyüzlü dizilir, atomlar ise V biçiminde görünür.','Z: kırık doğru'),A('Şıkları eşleştir','Üç geometri birlikte aranır.','X: düzlem üçgen, Y: düzgün dörtyüzlü, Z: kırık doğru')],
 puf='Önce toplam elektron çiftine göre diziliş, sonra yalnız atomların konumuna göre molekül geometrisi adlandırılır.')
# ============ 08 · orta · grafik · bağ açısı ============
ang={'H₂O':Fr(209,2),'NH₃':Fr(107),'CH₄':Fr(219,2)}
ang={'H₂O':Fr(1045,10),'NH₃':Fr(107),'CH₄':Fr(1095,10)}
lp={'CH₄':0,'NH₃':1,'H₂O':2}
assert sorted(ang,key=lambda k:ang[k])==sorted(lp,key=lambda k:-lp[k])
bar={'X':'H₂O','Y':'CH₄','Z':'NH₃'}
vals=[float(ang[bar[k]]) for k in 'XYZ']; assert vals==[104.5,109.5,107.0]
g=('\\begin{axis}[ybar,width=7.4cm,height=5.2cm,ymin=100,ymax=112,ytick={100,102,104,106,108,110,112},symbolic x coords={X,Y,Z},xtick=data,'
   'ylabel={Bağ açısı ($^\\circ$)},bar width=.9cm,enlarge x limits=.35,nodes near coords,every node near coord/.append style={font=\\small},'
   'nodes near coords style={/pgf/number format/.cd,use comma,fixed,precision=1,fixed zerofill},ymajorgrids,major grid style={gray!35},tick label style={font=\\small},label style={font=\\small}]\n'
   '\\addplot[fill=vurgu!45,draw=black] coordinates {'+''.join(f'({k},{float(ang[bar[k]])})' for k in 'XYZ')+'};\n\\end{axis}')
SK8=tikz_svg('\\begin{tikzpicture}\n'+g+'\n\\end{tikzpicture}')
cor=', '.join(bar[k] for k in 'XYZ'); assert cor=='H₂O, CH₄, NH₃'
W8=[('CH₄, H₂O, NH₃','Ortaklanmamış çift sayısı arttıkça bağ açısının da arttığını düşünmüş; böylece en küçük açıyı CH₄’e, en büyüğünü H₂O’ya vermiş.','bilgi'),
    ('NH₃, CH₄, H₂O','H₂O’daki ortaklanmamış çift sayısını 1, NH₃’tekini 2 sanmış; bu yüzden en küçük açıyı NH₃’e, ikinci en küçüğü H₂O’ya vermiş.','bilgi'),
    ('H₂O, NH₃, CH₄','H₂O’yu doğru yerleştirmiş ama CH₄ ile NH₃’ün bağ açılarını karıştırmış; ortaklanmamış çifti olmayan CH₄’ün açısı daha büyüktür.','dikkat'),
    ('CH₄, NH₃, H₂O','Şıkkı, grafikteki çubuk sırasına bakmadan moleküllerin sıralı listesine göre yazmış; en büyük açı CH₄’e aittir ve X’te değildir.','dikkat')]
q('0008',tipId='og-geometri',tip='Elektron çifti sayısından molekül geometrisi ve bağ açısı',z='orta',alt='Molekül Geometrisi',kaz='Ortaklanmamış elektron çifti sayısının bağ açısına etkisini yorumlar.',kalip='grafik',
 kart='K-AKOG-05 (VSEPR) · bağ açısı grafiği',sekil=SK8,
 metin='Merkez atomları sp³ hibritleşmesi yapan X, Y ve Z moleküllerinin H–merkez atom–H bağ açıları grafikte verilmiştir. Moleküller CH₄, NH₃ ve H₂O’dan oluşmaktadır. (₁H, ₆C, ₇N, ₈O)\nBuna göre X, Y ve Z moleküllerinin sırasıyla hangisi olduğu aşağıdakilerden hangisinde doğru verilmiştir?',
 dogru=cor,yan=W8,sira=yer(cor,W8,'A'),istenen='X, Y ve Z moleküllerinin sırasıyla adları.',
 ip=['Üç molekülde de merkez atom sp³’tür; merkez atomdaki ortaklanmamış çift sayısını bul ve bağ açısıyla ilişkilendir.'],
 bilgi=[B('Bağ açısı ve ortaklanmamış çift','Ortaklanmamış elektron çiftleri bağ çiftlerinden daha fazla itme yapar; çift sayısı arttıkça bağ açısı 109,5°’den küçülür. Örnek: ortaklanmamış çifti olmayan SiH₄’te bağ açısı 109,5°’dir')],
 ad=[A('Lewis yapılarını yaz','CH₄’te 0, NH₃’te 1, H₂O’da 2 ortaklanmamış çift vardır.','CH₄: 0 · NH₃: 1 · H₂O: 2'),A('Açıları sırala','Ortaklanmamış çift arttıkça açı küçülür.','CH₄ (109,5°) > NH₃ (107°) > H₂O (104,5°)'),A('Grafikle eşleştir','X en küçük, Y en büyük, Z ortadadır.','X: H₂O · Y: CH₄ · Z: NH₃')],
 puf='Aynı hibritleşmede ortaklanmamış çift arttıkça bağ açısı küçülür: CH₄ > NH₃ > H₂O.')
# ============ 09 · orta · şekilli · σ − π ============
r=1.25
cA=(0,0); cB=(r,0); cC=pol(*cB,-60,r); oD=pol(*cC,-120,r); hC=pol(*cC,0,1.0); hB=pol(*cB,60,1.0)
at={'C1':(*cA,'C'),'C2':(*cB,'C'),'C3':(*cC,'C'),'O':(*oD,'O'),'Ha':(*pol(*cA,120,1.0),'H'),'Hb':(*pol(*cA,240,1.0),'H'),'Hc':(*hB,'H'),'Hd':(*hC,'H')}
bd=[('C1','C2',2),('C2','C3',1),('C3','O',2),('C1','Ha',1),('C1','Hb',1),('C2','Hc',1),('C3','Hd',1)]
s9=len(bd); p9=sum(b[2]-1 for b in bd); assert (s9,p9)==(7,2)
SK9=tk(mol(at,bd))
assert s9-p9==5 and 4==sum(b[2] for b in bd if b[2]>1) and 1==(s9-6)-0
assert s9+p9==9 and s9-4==3 and s9-0==7
q('0009',tipId='og-sigmapi',tip='Açık formülden sigma ve pi bağı sayımı',z='orta',alt='Sigma ve Pi Bağları',kaz='Çoklu bağ içeren bir molekülde sigma ve pi bağı sayılarını karşılaştırır.',kalip='şekilli',
 kart='K-AKOG-03 (σ ve π bağı sayımı) · propenal',sekil=SK9,
 metin='Propenalin (akrolein) açık formülü şekilde verilmiştir.\nBuna göre propenal molekülündeki toplam σ bağı sayısı ile toplam π bağı sayısı arasındaki fark kaçtır?',
 dogru=5,yan=[(1,'C–H bağlarını σ saymamış; yalnız C–C, C=C ve C=O bağlarındaki σ bağlarını (3) alıp π sayısıyla farkını bulmuş.','dikkat'),(3,'Her çift bağı iki π bağı sayarak π sayısını 4 bulmuş: 7 − 4 = 3.','bilgi'),(7,'Moleküldeki yalnız σ bağlarının sayısını (7) fark olarak vermiş.','dikkat'),(9,'σ ve π bağı sayılarını çıkarmak yerine toplamış (7 + 2).','islem')],
 istenen='σ bağı sayısı ile π bağı sayısı arasındaki fark.',
 ip=['Önce bütün bağ çizgilerini tek bağ gibi say; sonra her çift bağdan kaç tanesinin π olduğunu ayır.'],
 bilgi=[B('σ ve π bağlarının ayrımı','Bağ çizgisi sayısı σ bağı sayısını verir; π bağı sayısı her çoklu bağda (mertebe − 1) kadardır. Örnek: CH₂=O molekülünde 3 σ ve 1 π bağı bulunur')],
 ad=[A('Bağ çizgilerini say','Dört C–H, bir C–C, bir C=C ve bir C=O bağı bulunur.','Bağ sayısı = 4 + 1 + 1 + 1 = 7'),A('σ sayısını bul','Her bağ bir σ içerir.','σ = 7'),A('π sayısını bul','İki çift bağın her biri bir π içerir.','π = 1 + 1 = 2'),A('Farkı hesapla','σ sayısından π sayısı çıkarılır.','7 − 2 = 5')],
 puf='σ sayısı bağ çizgisi sayısına eşittir; π sayısı fazla çizgi sayısıdır.')
# ============ 10 · orta · tablo · basit formül ============
mC,mH,mO=Fr(24,10),Fr(4,10),Fr(16,10); AK={'C':12,'H':1,'O':16}
def basit(mC_,mH_,mO_,aC=12,aH=1,aO=16):
    n=[mC_/aC,mH_/aH,mO_/aO]; n=[Fr(x) for x in n]; m=min(x for x in n if x>0)
    r_=[x/m for x in n]; den=1
    for x in r_: den=den*x.denominator//gcd(den,x.denominator)
    z=[int(x*den) for x in r_]; g_=0
    for x in z: g_=gcd(g_,x)
    return tuple(x//g_ for x in z)
def formul(t): return ''.join(s+(''.join('₀₁₂₃₄₅₆₇₈₉'[int(c)] for c in str(k)) if k>1 else '') for s,k in zip('CHO',t) if k>0)
b10=basit(mC,mH,mO); assert b10==(2,4,1) and formul(b10)=='C₂H₄O'
e1=basit(mC,mH,mO,aO=8); e2=basit(mC,mH,mO,aO=32); e3=basit(mC,mH,mO,aH=2)
assert formul(e1)=='CH₂O' and formul(e2)=='C₄H₈O' and formul(e3)=='C₂H₂O'
e4=(6,1,4); assert Fr(24,10)/Fr(4,10)==6 and Fr(16,10)/Fr(4,10)==4 and formul(e4)=='C₆HO₄'
SK10=tablo_svg(['Element','Kütle (g)'],[['Karbon','2,4'],['Hidrojen','0,4'],['Oksijen','1,6']])
W10=[(formul(e4),'Kütlelerin oranını (2,4 : 0,4 : 1,6 = 6 : 1 : 4) atom sayıları oranı sanmış; kütleleri atom kütlelerine bölmemiş.','bilgi'),
     (formul(e1),'Oksijeni 16 yerine 8 g/mol alarak mol sayılarını 0,2 : 0,4 : 0,2 bulmuş.','islem'),
     (formul(e3),'Hidrojenin mol sayısını H₂ (2 g/mol) üzerinden hesaplayıp 0,2 mol bulmuş; mol sayıları 0,2 : 0,2 : 0,1 olmuş.','bilgi'),
     (formul(e2),'Oksijeni O₂ (32 g/mol) sanarak mol sayısını 0,05 bulmuş; oran 4 : 8 : 1 çıkmış.','bilgi')]
q('0010',tipId='og-formul',tip='Basit formül, molekül formülü ve yanma analizi',z='orta',alt='Basit Formül ve Molekül Formülü',kaz='Elementlerin kütlelerinden bir bileşiğin basit formülünü bulur.',kalip='tablo',
 kart='K-AKOG-06 (basit formül) · kütlelerden mol oranı',sekil=SK10,
 metin='Yalnız C, H ve O elementlerinden oluşan bir organik bileşiğin saf örneğinde bulunan elementlerin kütleleri şekildeki tabloda verilmiştir. (H = 1, C = 12, O = 16 g/mol)\nBuna göre bu bileşiğin basit formülü aşağıdakilerden hangisidir?',
 dogru=formul(b10),yan=W10,sira=yer(formul(b10),W10,'D'),istenen='Bileşiğin basit formülü.',
 ip=['Atom sayıları oranı, kütle oranı değil mol sayıları oranıdır; her kütleyi uygun mol kütlesine böl.'],
 bilgi=[B('Basit formül','Kütleler molar kütlelere bölünerek mol sayıları bulunur; mol sayıları en küçüğe bölünüp en küçük tam sayı oranına getirilir. Örnek: 1,2 g C ve 0,3 g H içeren bileşikte C : H = 0,1 : 0,3 = 1 : 3 → CH₃')],
 ad=[A('Mol sayılarını bul','Kütle ÷ mol kütlesi.','C: 2,4 ÷ 12 = 0,2 · H: 0,4 ÷ 1 = 0,4 · O: 1,6 ÷ 16 = 0,1'),A('Oranı kur','Mol sayıları en küçük değer olan 0,1’e bölünür.','C : H : O = 2 : 4 : 1'),A('Formülü yaz','Oran en küçük tam sayılardır.','C₂H₄O')],
 puf='Basit formül için kütleyi değil, kütle ÷ mol kütlesini (mol sayısını) oranla.')
# ============ 11 · orta · öncüllü · basit/molekül formülü ============
def basitf(c,h): g_=gcd(c,h); return (c//g_,h//g_)
assert basitf(2,2)==basitf(6,6)==(1,1) and basitf(4,10)==(2,5)
M_I=2*12+2; M_II=6*12+6; assert M_I!=M_II   # CH ailesi: farklı mol kütleleri (26, 78)
T11={'I','II'}
W11={'I':'C₂H₂ ve C₆H₆ formüllerinin ikisi de en küçük tam sayı oranında CH’ye sadeleşir','II':'C₄H₁₀ formülündeki indisler 2’ye bölünerek C₂H₅ elde edilir','III':'oysa aynı basit formülü paylaşan C₂H₂ (26 g/mol) ve C₆H₆ (78 g/mol) gibi bileşiklerin mol kütleleri farklıdır'}
d11,y11,L11=oc(T11,'B',W11)
q('0011',tipId='og-formul',tip='Basit formül, molekül formülü ve yanma analizi',z='orta',alt='Basit Formül ve Molekül Formülü',kaz='Basit formül ile molekül formülü arasındaki ilişkiyi yorumlar.',kalip='öncüllü',
 kart='K-AKOG-06 (basit formül) · basit–molekül formülü ilişkisi',
 metin='Basit formül, bir bileşikteki atomların en küçük tam sayılı oranını; molekül formülü ise bir molekülde bulunan gerçek atom sayılarını gösterir. Molekül formülü, basit formülün tam sayı katıdır. (H = 1, C = 12 g/mol)\nBuna göre,\nI. C₂H₂ ve C₆H₆ bileşiklerinin basit formülleri aynıdır.\nII. Molekül formülü C₄H₁₀ olan bileşiğin basit formülü C₂H₅’tir.\nIII. Basit formülleri aynı olan bileşiklerin mol kütleleri de birbirine eşittir.\nyargılarından hangileri doğrudur?',
 dogru=d11,yan=y11,sira=L11,istenen='Doğru olan yargılar.',
 ip=['Her formüldeki atom sayılarının ortak bölenine bak; aynı basit formülün farklı katlarının mol kütlesini hesaplayarak III’ü sına.'],
 bilgi=[B('Basit formül – molekül formülü','Molekül formülündeki indisler ortak bölenlerine bölününce basit formül bulunur: C₆H₁₂O₆ → CH₂O. Molekül formülü = (basit formül)ₙ ve n = mol kütlesi ÷ basit formül kütlesi’dir')],
 ad=[A('I’i değerlendir','Her iki formülde C : H = 1 : 1 oranı vardır.','C₂H₂ → CH · C₆H₆ → CH → I doğru'),A('II’yi değerlendir','4 ve 10’un ortak böleni 2’dir.','C₄H₁₀ → C₂H₅ → II doğru'),A('III’ü değerlendir','Aynı basit formülün farklı katları farklı kütleye sahiptir.','CH: 13 · C₂H₂: 26 · C₆H₆: 78 → III yanlış'),A('Sonucu yaz','Doğru yargılar I ve II’dir.','I ve II')],
 puf='Aynı basit formül aynı bileşik demek değildir; n katı değişince molekül formülü ve mol kütlesi de değişir.')
# ============ 12 · orta · tablo · organik sayısı ============
CMP=[('I','CH₃Cl',True,True),('II','H₂CO₃',False,True),('III','NaHCO₃',False,True),('IV','C₆H₁₂O₆',True,True),('V','CCl₄',True,False),('VI','Na₂CO₃',False,False),('VII','CO',False,False)]
# (no, formül, organik mi, C–H bağı var mı)
org=sum(1 for c in CMP if c[2]); assert org==3
tCH=sum(1 for c in CMP if c[3]); assert tCH==4
orgH=sum(1 for c in CMP if c[2] and c[3]); assert orgH==2
metalsiz=sum(1 for c in CMP if 'Na' not in c[1]); assert metalsiz==5
assert len(CMP)==7
SK12=tablo_svg(['Numara','Formül'],[[c[0],c[1]] for c in CMP])
q('0012',tipId='og-ayrim',tip='Organik ve anorganik bileşiklerin ayrımı',z='orta',alt='Organik ve Anorganik Bileşikler',kaz='Karbon içeren bileşikleri organik ve anorganik sınıflara ayırır.',kalip='tablo',
 kart='K-AKOG-01 (organik–anorganik ayrımı) · tablodan sayım',sekil=SK12,
 metin='Karbon içeren yedi bileşiğin formülleri şekildeki tabloda numaralandırılarak verilmiştir. Bu bileşikler, organik ve anorganik bileşik sınıflarına ayrılacaktır.\nBuna göre tablodaki bileşiklerden kaç tanesi organik bileşik sınıfında yer alır?',
 dogru=3,yan=[(2,'Organik bileşik için C–H bağının zorunlu olduğunu düşünüp H içermeyen CCl₄’ü anorganik saymış; yalnız CH₃Cl ve C₆H₁₂O₆’yı organik bulmuş.','bilgi'),(4,'Hem C hem H içeren her bileşiği organik sayıp H₂CO₃ ve NaHCO₃’ü de katmış, CCl₄’ü atlamıştır.','bilgi'),(5,'Metal içermeyen karbon bileşiklerini organik saymış; H₂CO₃’ü de CO’yu da organik grubuna katmıştır.','bilgi'),(7,'Karbon içeren her bileşiği organik saymış.','bilgi')],
 istenen='Organik bileşik sayısı.',
 ip=['Her formüldeki karbonun hangi atomlara bağlı olduğunu düşün; karbonat, bikarbonat ve karbonun oksitleri hangi gruba girer?'],
 bilgi=[B('Organik bileşikler','Organik bileşikler karbon–karbon ya da karbon–hidrojen bağı bulunan karbon bileşikleridir; CO, CO₂, H₂CO₃ ve karbonat–bikarbonat tuzları anorganik sayılır. Örnek: C₂H₆ organik, Li₂CO₃ ve CO₂ anorganiktir')],
 ad=[A('Karbonlu anorganikleri ayır','Karbonatlar, bikarbonatlar, karbonik asit ve karbon monoksit anorganiktir.','H₂CO₃, NaHCO₃, Na₂CO₃, CO → anorganik'),A('Kalanları incele','CH₃Cl ve C₆H₁₂O₆ C–H bağı içerir; CCl₄ de C–C ve C–H içermese de halojenli bir organik bileşiktir.','CH₃Cl, C₆H₁₂O₆, CCl₄ → organik'),A('Sayımı yap','Üç bileşik organik sınıftadır.','I, IV, V → 3')],
 puf='Organik demek “yalnız C–H” demek değildir; CCl₄ gibi halojenürler de organiktir, H₂CO₃ ve bikarbonatlar ise anorganiktir.')
# ============ 13 · orta · şekilli · öncüllü · allotroplar ============
g=[]
R_=1.15
g.append(dot(0,0,2.6)); 
for i,a in enumerate([45,135,225,315]):
    x,y=pol(0,0,a,R_); g.append(f'\\draw[line width=.9pt] (0,0) -- ({x:.3f},{y:.3f}) ;'); g.append(dot(x,y,2.6))
    for d in (-38,0,38):
        sx,sy=pol(x,y,a+d,.42); g.append(f'\\draw[dashed,gray,line width=.7pt] ({x+(sx-x)*.3:.3f},{y+(sy-y)*.3:.3f}) -- ({sx:.3f},{sy:.3f});')
g.append('\\node[font=\\small\\bfseries] at (0,-2.0) {X};')
rr=.7; s3=math.sqrt(3); ox=4.6
cen=[(0,0),(s3*rr,0),(s3*rr/2,1.5*rr)]
V={}; E=set()
def key(p): return (round(p[0],3),round(p[1],3))
for cx,cy in cen:
    vs=[pol(cx,cy,90+60*k,rr) for k in range(6)]
    for k in range(6):
        a_,b_=key(vs[k]),key(vs[(k+1)%6]); V[a_]=1; V[b_]=1; E.add(tuple(sorted((a_,b_))))
deg={v:0 for v in V}; nbr={v:[] for v in V}
for a_,b_ in E: deg[a_]+=1; deg[b_]+=1; nbr[a_].append(b_); nbr[b_].append(a_)
assert sorted(set(deg.values()))==[2,3] and len(V)==13 and len(E)==15
for a_,b_ in E: g.append(f'\\draw[line width=.9pt] ({a_[0]+ox:.3f},{a_[1]:.3f}) -- ({b_[0]+ox:.3f},{b_[1]:.3f});')
for v in V:
    g.append(dot(v[0]+ox,v[1],2.6))
    if deg[v]==2:
        mx=sum(n[0] for n in nbr[v])/2; my=sum(n[1] for n in nbr[v])/2; dx,dy=v[0]-mx,v[1]-my; L_=math.hypot(dx,dy)
        g.append(f'\\draw[dashed,gray,line width=.7pt] ({v[0]+ox+dx/L_*.13:.3f},{v[1]+dy/L_*.13:.3f}) -- ({v[0]+ox+dx/L_*.42:.3f},{v[1]+dy/L_*.42:.3f});')
g.append(f'\\node[font=\\small\\bfseries] at ({ox+.6:.2f},-2.0) {{Y}};')
g.append('\\node[font=\\small] at (2.3,-2.6) {$\\bullet$ : C atomu};')
SK13=tk('\n'.join(g))
T13={'I','III'}
W13={'I':'X’te her karbon dört karbon atomuna bağlıdır; dört σ bağı yapan karbon sp³ hibritleşmesi yapmıştır','II':'Y’de her karbon yalnız üç karbon atomuna bağlıdır, yani üçer σ bağı yapmıştır; dört σ bağı yapmamıştır','III':'aynı elementin farklı kristal yapılarına allotrop denir ve X ile Y ikisi de karbondur'}
d13,y13,L13=oc(T13,'E',W13)
q('0013',tipId='og-karbon',tip='Karbonun bağ yapma özellikleri ve allotroplar',z='orta',alt='Karbonun Bağ Yapma Özellikleri',kaz='Karbonun allotroplarının yapısını bağ sayısı ve hibritleşme türüyle ilişkilendirir.',kalip='öncüllü',
 kart='K-AKOG-02 (karbonun bağ yapma özellikleri) · iki allotropun yapısı',sekil=SK13,
 metin='Karbon elementinin iki farklı doğal yapısının küçük birer parçası şekilde gösterilmiştir. Kesikli çizgiler yapının aynı biçimde devam ettiğini gösterir. (₆C)\nBuna göre,\nI. X’teki karbon atomları sp³ hibritleşmesi yapmıştır.\nII. Y’deki her karbon atomu dört σ bağı yapmıştır.\nIII. X ve Y, karbonun allotroplarıdır.\nyargılarından hangileri doğrudur?',
 dogru=d13,yan=y13,sira=L13,istenen='Doğru olan yargılar.',
 ip=['Her yapıda bir karbon atomunun kaç komşu karbonla bağlandığını say; bu sayıyı σ bağı sayısı ve hibritleşme türüyle ilişkilendir.'],
 bilgi=[B('Allotrop ve hibritleşme','Aynı elementin farklı yapılarına allotrop denir. Her karbonun komşu sayısı 4 ise sp³, 3 ise sp²’dir. Örnek: fulleren yapısında her karbon üç karbona bağlıdır')],
 ad=[A('X’i incele','Her karbon dört karbonla bağlıdır.','4 σ → sp³ → I doğru'),A('Y’yi incele','Her karbon üç karbonla bağlıdır; dördüncü elektron yapıda serbestçe dolaşır.','3 σ → II yanlış'),A('Allotropu değerlendir','İkisi de karbon atomlarından oluşur ama bağlanma biçimleri farklıdır.','X, Y: allotrop → III doğru'),A('Sonucu yaz','Doğru yargılar I ve III’tür.','I ve III')],
 puf='Komşu sayısı 4 ise sp³ (elmas türü), 3 ise sp² (grafit türü); aynı elementin bu yapıları allotroptur.')
# ============ 14 · zor · şekilli · çizgi-bağ formülü + yanma ============
rr=1.1
ring=[pol(0,0,90-60*k,rr) for k in range(6)]
at={f'r{k}':(*ring[k],None) for k in range(6)}
oP=pol(*ring[0],90,rr); at['O']=(*oP,'O'); mP=pol(*ring[2],-30,rr); at['Me']=(*mP,None)
bd=[('r0','r1',1),('r1','r2',2),('r2','r3',1),('r3','r4',1),('r4','r5',1),('r5','r0',1),('r0','O',2),('r2','Me',1)]
vl={f'r{k}':0 for k in range(6)}; vl['Me']=0; vl['O']=0
for a,b,od in bd: vl[a]+=od; vl[b]+=od
Hn={k:4-v for k,v in vl.items() if k!='O'}; assert vl['O']==2
nC=7; nH=sum(Hn.values()); assert (nC,nH)==(7,10)
SK14=tk(mol(at,bd))
n14=Fr(2,10); mH2O=n14*nH/2*18; assert mH2O==18
a2=n14*nH*1; a16=n14*(Hn['r1']*0+9)/2*18; a25=n14*(2*nC)/2*18; a36=n14*nH*18
assert (a2,a16,a25,a36)==(2,Fr(162,10),Fr(252,10),36)
q('0014',tipId='og-formul',tip='Basit formül, molekül formülü ve yanma analizi',z='zor',alt='Basit Formül ve Molekül Formülü',kaz='Çizgi-bağ formülünden molekül formülünü bulur ve yanma tepkimesinde oluşan ürün miktarını hesaplar.',kalip='şekilli',
 kart='K-AKOG-06 (basit/molekül formülü) · çizgi-bağ formülü + yanma',sekil=SK14,
 metin='Yalnız C, H ve O içeren bir organik bileşiğin çizgi-bağ formülü şekilde verilmiştir. Çizgi-bağ formülünde köşeler ve uçlar karbon atomunu gösterir; karbona bağlı hidrojenler çizilmez. Bu bileşiğin 0,2 molü yeterli miktarda O₂ ile tamamen yakılıyor. (H = 1, O = 16 g/mol)\nBuna göre bu yanma sırasında oluşan H₂O kaç gramdır?',
 dogru=18,yan=[(2,'H₂O kütlesi yerine yalnız hidrojen atomlarının kütlesini (0,2 × 10 × 1 = 2 g) bulmuş.','dikkat'),(Fr(162,10),'Halkadaki =CH– karbonundaki hidrojeni saymayıp 9 hidrojen bulmuş: 0,2 × 9 ÷ 2 = 0,9 mol H₂O → 16,2 g.','dikkat'),(Fr(252,10),'Her karbon köşesine 2 hidrojen yazıp 14 hidrojen bulmuş: 0,2 × 14 ÷ 2 = 1,4 mol H₂O → 25,2 g.','bilgi'),(36,'Hidrojen atomu mol sayısını (2 mol) H₂O mol sayısı almış, ikiye bölmemiş: 2 × 18 = 36 g.','islem')],
 istenen='Yanmada oluşan H₂O’nun kütlesi (g).',
 ip=['Her karbon köşesinin dört bağ yaptığını kullanarak o köşedeki hidrojen sayısını bul; bileşiğin molekül formülünü yazdıktan sonra H atomlarının kaçının suya dönüştüğünü düşün.'],
 bilgi=[B('Çizgi-bağ formülü','Her köşe ve uç bir karbon atomudur; karbonun toplam bağ sayısı 4’e tamamlanacak kadar hidrojen bağlıdır. Örnek: yalnız bir çizgiyle bağlı uç CH₃, iki tek bağın birleştiği köşe CH₂’dir')],
 ad=[A('Hidrojenleri belirle','Karbon başına bağ toplamı 4’e tamamlanır.','C=O: 0 H · =CH–: 1 H · =C(–CH₃): 0 H · üç CH₂: 6 H · CH₃: 3 H'),A('Molekül formülünü yaz','7 karbon, 10 hidrojen, 1 oksijen vardır.','C₇H₁₀O'),A('Yanma ilişkisini kur','Her 2 H atomu 1 H₂O oluşturur.','1 mol bileşik → 5 mol H₂O'),A('Mol sayısını bul','0,2 mol bileşikten oluşan H₂O molü hesaplanır.','0,2 × 5 = 1 mol H₂O'),A('Kütleyi hesapla','H₂O’nun mol kütlesi 18 g/mol’dür.','1 × 18 = 18 g')],
 puf='Yanmada bileşikteki hidrojenin yarısı kadar mol H₂O oluşur; çizgi-bağ formülünde H sayısını karbonun dört bağından bulun.')
# ============ 15 · zor · şekilli · yanma düzeneği ============
m_b=Fr(30,10); dH2O=Fr(18,10); dCO2=Fr(44,10); Mb=60
nH2O=dH2O/18; nCO2=dCO2/44; nC=nCO2; nHh=2*nH2O; mC_=nC*12; mH_=nHh*1; mO_=m_b-mC_-mH_; nO=mO_/16
assert (nH2O,nCO2,nHh,mO_,nO)==(Fr(1,10),Fr(1,10),Fr(1,5),Fr(16,10),Fr(1,10))
rat=(nC/nO,nHh/nO,nO/nO); assert rat==(1,2,1)
n15=Fr(Mb,12+2+16); assert n15==2 and (2*1,2*2,2*1)==(2,4,2)
e_a=(1,2,1)                       # n katı unutulmuş
e_b=(2,4,1)                       # O'ya n uygulanmamış
nO_yanlis=2*nCO2+nH2O; assert nO_yanlis==Fr(3,10) and (nC/nO_yanlis,nHh/nO_yanlis)==(Fr(1,3),Fr(2,3))   # 1:2:3 oranı
e_c=(1,2,3)
nH_yanlis=nH2O; assert nH_yanlis==nC==Fr(1,10)                                                     # 1:1:1
e_d=(2,2,2)
def f3(t): return formul(t)
assert (f3((2,4,2)),f3(e_a),f3(e_b),f3(e_c),f3(e_d))==('C₂H₄O₂','CH₂O','C₂H₄O','CH₂O₃','C₂H₂O₂')
f_ok='C₂H₄O₂'
g=['\\draw[thick] (0,0) rectangle (2.8,.8);','\\fill[gray!35] (.9,.05) rectangle (1.6,.25);','\\node[font=\\small] at (1.25,.55) {bile\\c{s}ik};',
   '\\draw[-{Stealth[length=2mm]},thick] (-1.0,.4) -- (0,.4); \\node[above,font=\\small] at (-.5,.45) {O$_2$};',
   '\\fill[vurgu!35] (1.05,-.08) -- (1.45,-.08) -- (1.25,-.55) -- cycle; \\node[font=\\small] at (1.25,-.85) {\\raise.1ex\\hbox{ısıtma}};',
   '\\draw[thick] (2.8,.4) -- (3.4,.4); \\draw[thick] (4.9,.4) -- (5.5,.4); \\draw[-{Stealth[length=2mm]},thick] (7.1,.4) -- (7.9,.4);',
   '\\draw[thick,fill=gray!15] (3.4,.05) rectangle (4.9,.75); \\node[font=\\small] at (4.15,.4) {\\ce{CaCl2}};',
   '\\draw[thick,fill=gray!15] (5.5,.05) rectangle (7.1,.75); \\node[font=\\small] at (6.3,.4) {KOH};',
   '\\node[font=\\small,align=center] at (1.4,-1.5) {3,0 g\\\\bile\\c{s}ik};',
   '\\node[font=\\small,align=center] at (4.15,-.75) {kütle artışı\\\\1,8 g};',
   '\\node[font=\\small,align=center] at (6.3,-.75) {kütle artışı\\\\4,4 g};']
g=[x.replace('bile\\c{s}ik','bileşik').replace('\\raise.1ex\\hbox{ısıtma}','ısı') for x in g]
SK15=tk('\n'.join(g))
W15=[('CH₂O','C : H : O = 1 : 2 : 1 oranını bulmuş; mol kütlesinden yararlanıp n = 60 ÷ 30 = 2 katını almamış.','dikkat'),
     ('C₂H₂O₂','H₂O’nun mol sayısını (0,1) hidrojen atomu mol sayısı almış (ikiyle çarpmamış); oranı 1 : 1 : 1 bulup CHO (29 g/mol) için 60 ÷ 29 ≈ 2 katı almış.','islem'),
     ('C₂H₄O','Oranı doğru bulup n = 2 değerini yalnız C ve H atomlarına uygulamış, oksijen atomu sayısını 1 bırakmış.','islem'),
     ('CH₂O₃','Yanma ürünlerindeki bütün oksijeni (0,2 + 0,1 = 0,3 mol) bileşiğe ait saymış; oran 1 : 2 : 3 çıkmış.','bilgi')]
q('0015',tipId='og-formul',tip='Basit formül, molekül formülü ve yanma analizi',z='zor',alt='Basit Formül ve Molekül Formülü',kaz='Yanma ürünlerinin kütlelerinden bileşiğin basit ve molekül formülünü bulur.',kalip='şekilli',
 kart='K-AKOG-07 (yanma analizi) · CaCl₂ ve KOH tüpleri',sekil=SK15,
 metin='Yalnız C, H ve O içeren bir organik bileşiğin örneği, şekildeki düzenekte fazla miktarda O₂ ile tamamen yakılıyor. Yanma ürünlerinden H₂O buharı yalnız CaCl₂ tüpünde, CO₂ gazı ise yalnız KOH tüpünde tutuluyor. Tüplerin kütle artışları şekilde verilmiştir. Bileşiğin mol kütlesi 60 g/mol’dür. (H = 1, C = 12, O = 16 g/mol)\nBuna göre bileşiğin molekül formülü aşağıdakilerden hangisidir?',
 dogru=f_ok,yan=W15,sira=yer(f_ok,W15,'A'),istenen='Bileşiğin molekül formülü.',
 ip=['Her tüpteki artıştan C ve H mol sayılarını bul; oksijen miktarını bileşiğin kütlesinden yararlanarak hesapla.'],
 bilgi=[B('Yanma analizi','Bileşikteki C tamamı CO₂’ye, H tamamı H₂O’ya dönüşür: 1 mol CO₂ → 1 mol C, 1 mol H₂O → 2 mol H. Oksijen miktarı, bileşiğin kütlesinden C ve H kütleleri çıkarılarak bulunur. Örnek: 0,5 mol H₂O oluşuyorsa bileşikte 1 mol H vardır')],
 ad=[A('C ve H miktarını bul','CO₂ → C, H₂O → H (iki katı).','n(CO₂) = 4,4 ÷ 44 = 0,1 → C = 0,1 mol · n(H₂O) = 1,8 ÷ 18 = 0,1 → H = 0,2 mol'),A('O kütlesini bul','Kalan kütle oksijene aittir.','m(C) = 1,2 g, m(H) = 0,2 g → m(O) = 3,0 − 1,4 = 1,6 g'),A('O mol sayısını bul','Oksijenin mol kütlesine böl.','n(O) = 1,6 ÷ 16 = 0,1 mol'),A('Basit formülü yaz','Mol sayılarını en küçüğe böl.','C : H : O = 0,1 : 0,2 : 0,1 = 1 : 2 : 1 → CH₂O'),A('Molekül formülünü bul','n = 60 ÷ 30 = 2.','(CH₂O)₂ = C₂H₄O₂')],
 puf='Oksijen yanma ürünlerinden değil, bileşiğin kütlesinden C ve H kütleleri çıkarılarak bulunur; sonra mol kütlesiyle n katı alınır.')
# ============ 16 · zor · şekilli · öncüllü · hibritleşme + σ/π + örtüşme ============
Ca=(1.0,0); Cb=(2.2,0); Cc=(3.5,0); Cd=pol(*Cc,60,1.3); Ce=pol(*Cd,0,1.3)
at={'H0':(0,0,'H'),'Ca':(*Ca,'C'),'Cb':(*Cb,'C'),'Cc':(*Cc,'C'),'Cd':(*Cd,'C'),'Ce':(*Ce,'CH$_3$'),'Hc':(*pol(*Cc,-60,1.0),'H'),'Hd':(*pol(*Cd,120,1.0),'H')}
bd=[('H0','Ca',1),('Ca','Cb',3),('Cb','Cc',1),('Cc','Cd',2),('Cc','Hc',1),('Cd','Hd',1),('Cd','Ce',1)]
nbc={}
for a,b,o in bd: nbc[a]=nbc.get(a,0)+1; nbc[b]=nbc.get(b,0)+1
hb={k:{4:'sp3',3:'sp2',2:'sp'}[nbc[k]] for k in ['Ca','Cb','Cc','Cd']}; hb['Ce']='sp3'
assert hb=={'Ca':'sp','Cb':'sp','Cc':'sp2','Cd':'sp2','Ce':'sp3'}
sp_=sum(1 for v in hb.values() if v=='sp'); sp2_=sum(1 for v in hb.values() if v=='sp2'); sp3_=sum(1 for v in hb.values() if v=='sp3'); assert (sp_,sp2_,sp3_)==(2,2,1)
sig16=len(bd)+3; pi16=sum(b[2]-1 for b in bd); assert (sig16,pi16)==(10,3)   # CH₃'ün 3 C–H bağı eklenir
SK16=tk(mol(at,bd))
T16={'II','III'}
W16={'I':'sp hibritleşmesi yapan karbon sayısı 2, sp³ yapan karbon sayısı 1’dir; oran 2’dir, 3 değildir','II':'moleküldeki bağlar sayılınca 10 σ (CH₃’teki 3 C–H dahil) ve 3 π bağı bulunur','III':'sp hibritli karbon ile sp² hibritli karbon arasındaki tek bağ, bu iki hibrit orbitalin uç uca örtüşmesiyle oluşan σ bağıdır'}
d16,y16,L16=oc(T16,'D',W16)
q('0016',tipId='og-hibrit',tip='Hibritleşme türü, orbital diyagramı ve örtüşme',z='zor',alt='Hibritleşme',kaz='Bir molekülde hibritleşme türlerini, σ ve π bağı sayılarını ve bağların orbital örtüşmesini birlikte yorumlar.',kalip='öncüllü',
 kart='K-AKOG-04 (hibritleşme türü) · penten-in',sekil=SK16,
 metin='Bir hidrokarbonun açık formülü şekilde verilmiştir. Bir karbonun hibritleşmesi, çevresindeki σ bağı sayısına göre belirlenir. (₁H, ₆C)\nBuna göre bu molekülle ilgili,\nI. sp hibritleşmesi yapan karbon sayısı, sp³ hibritleşmesi yapan karbon sayısının 3 katıdır.\nII. Toplam 10 σ ve 3 π bağı bulunur.\nIII. Üçlü bağlı karbon ile komşusu arasındaki bağ, sp ve sp² hibrit orbitallerinin uç uca örtüşmesiyle oluşur.\nyargılarından hangileri doğrudur?',
 dogru=d16,yan=y16,sira=L16,istenen='Doğru olan yargılar.',
 ip=['Önce her karbonun σ bağı sayısını bularak hibritleşmesini belirle; sonra bağ çizgilerini σ ve π olarak ayır, CH₃ grubundaki hidrojenleri unutma.'],
 bilgi=[B('Hibrit orbitallerin örtüşmesi','Hibrit orbitallerin uç uca örtüşmesiyle σ bağı oluşur; hibritleşmeyen p orbitallerinin yan yana örtüşmesiyle π bağı oluşur. Örnek: etende C–C σ bağı sp²–sp² örtüşmesiyle, π bağı p–p örtüşmesiyle oluşur')],
 ad=[A('Hibritleşmeleri bul','2 σ → sp, 3 σ → sp², 4 σ → sp³.','Ca, Cb: sp · Cc, Cd: sp² · CH₃: sp³'),A('I’i değerlendir','2 sp ve 1 sp³ karbon var; oran 2’dir.','2 ÷ 1 = 2 → I yanlış'),A('Bağları say','σ: 1 + 1 + 1 + 1 + 1 + 1 + 1 + 3 = 10; π: 2 + 1 = 3.','II doğru'),A('III’ü değerlendir','Cb ile Cc arasındaki tek bağ, Cb’nin sp ve Cc’nin sp² orbitalinden oluşur.','III doğru'),A('Sonucu yaz','Doğru yargılar II ve III’tür.','II ve III')],
 puf='Önce her atomun hibritleşmesini bul; σ bağı hibrit orbitallerin uç uca, π bağı p orbitallerinin yan yana örtüşmesidir.')
# ============ 17 · zor · tablo · molekül formülü ============
D17=[('X',(1,2,1),60),('Y',(1,2,0),42),('Z',(1,3,0),30)]
def kut(t): return t[0]*12+t[1]*1+t[2]*16
tot_H=0; tot_C=0; fl=[]
for nm,t,M in D17:
    assert M%kut(t)==0; n=M//kut(t); tot_H+=n*t[1]; tot_C+=n*t[0]; fl.append(formul(tuple(n*x for x in t)))
assert (tot_H,tot_C,fl)==(16,7,['C₂H₄O₂','C₃H₆','C₂H₆'])
sH=sum(t[1] for _,t,_ in D17); assert sH==7
h9=2*t[1] if False else 4+2+3; assert h9==9
h14=2*sH; assert h14==14 and tot_C+tot_H==23
SK17=tablo_svg(['Bileşik','Basit formül','Mol kütlesi (g/mol)'],[['X','CH₂O','60'],['Y','CH₂','42'],['Z','CH₃','30']])
q('0017',tipId='og-formul',tip='Basit formül, molekül formülü ve yanma analizi',z='zor',alt='Basit Formül ve Molekül Formülü',kaz='Basit formül ve mol kütlesinden molekül formüllerini bulup atom sayılarını toplar.',kalip='tablo',
 kart='K-AKOG-06 (basit/molekül formülü) · üç bileşik, n katı',sekil=SK17,
 metin='X, Y ve Z organik bileşiklerinin basit formülleri ile mol kütleleri şekildeki tabloda verilmiştir. Molekül formülü, basit formülün tam sayı katıdır. (H = 1, C = 12, O = 16 g/mol)\nBuna göre bu üç bileşiğin birer molündeki toplam hidrojen atomu kaç moldür?',
 dogru=16,yan=[(7,'Basit formüllerdeki hidrojen sayılarını (2 + 2 + 3) toplamış; mol kütlesiyle n katını bulmamış.','dikkat'),(9,'Yalnız X için n = 2 bulup 4 hidrojen almış; Y ve Z’de basit formüllerdeki hidrojen sayılarını (2 + 3) kullanmış: 4 + 2 + 3 = 9.','dikkat'),(14,'Üç bileşik için de n = 2 almış: 2 × (2 + 2 + 3) = 14.','islem'),(23,'Hidrojen yerine karbon ve hidrojen atomlarının toplamını (7 + 16) vermiş.','dikkat')],
 istenen='Üç bileşiğin birer molündeki toplam H atomu (mol).',
 ip=['Her bileşiğin mol kütlesini basit formül kütlesine bölerek n değerini bul; n katını bütün atomlara uygula.'],
 bilgi=[B('Molekül formülü bulma','Molekül formülü = (basit formül)ₙ; n = mol kütlesi ÷ basit formül kütlesi. Örnek: basit formülü CH₂ olan ve mol kütlesi 28 g/mol olan bileşik için n = 28 ÷ 14 = 2, molekül formülü C₂H₄’tür')],
 ad=[A('X’i çöz','CH₂O’nun kütlesi 30 g/mol; n = 60 ÷ 30.','n = 2 → C₂H₄O₂ → 4 H'),A('Y’yi çöz','CH₂’nin kütlesi 14 g/mol; n = 42 ÷ 14.','n = 3 → C₃H₆ → 6 H'),A('Z’yi çöz','CH₃’ün kütlesi 15 g/mol; n = 30 ÷ 15.','n = 2 → C₂H₆ → 6 H'),A('Toplamı bul','Üç bileşiğin H atomu mol sayıları toplanır.','4 + 6 + 6 = 16')],
 puf='Her bileşikte n ayrı bulunur ve basit formüldeki bütün atom sayıları n ile çarpılır.')
# ============ 18 · zor · şekilli · Lewis yapıları · olumsuz kök ============
def lp(x,y,ang,r=.40,s=.075):
    cx,cy=pol(x,y,ang,r); px,py=-math.sin(math.radians(ang)),math.cos(math.radians(ang))
    return dot(cx+px*s,cy+py*s,1.5)+dot(cx-px*s,cy-py*s,1.5)
g=[]; ox=0
atx={'B':(ox,0,'B')}; bdx=[]
for i,a in enumerate((90,210,330)):
    x,y=pol(ox,0,a,1.1); atx[f'F{i}']=(x,y,'F'); bdx.append(('B',f'F{i}',1))
g.append(mol(atx,bdx))
for i,a in enumerate((90,210,330)):
    x,y=pol(ox,0,a,1.1)
    for d in (0,90,-90): g.append(lp(x,y,a+d,.38))
g.append(f'\\node[font=\\small\\bfseries] at ({ox},-1.9) {{X}};')
ox=4.4; aty={'Ol':(ox-1.3,0,'O'),'C':(ox,0,'C'),'Or':(ox+1.3,0,'O')}
g.append(mol(aty,[('Ol','C',2),('C','Or',2)]))
for x,aa in ((ox-1.3,(100,-100)),(ox+1.3,(80,-80))):
    for a in aa: g.append(lp(x,0,a,.4))
g.append(f'\\node[font=\\small\\bfseries] at ({ox},-1.9) {{Y}};')
ox=8.6; atz={'N':(ox,0,'N')}; bdz=[]
for i,a in enumerate((200,340,270)):
    x,y=pol(ox,0,a,1.1); atz[f'H{i}']=(x,y,'H'); bdz.append(('N',f'H{i}',1))
g.append(mol(atz,bdz)); g.append(lp(ox,0,90,.4))
g.append(f'\\node[font=\\small\\bfseries] at ({ox},-1.9) {{Z}};')
SK18=tk('\n'.join(g))
# VSEPR doğrulaması
vs={'X':(3,0),'Y':(2,0),'Z':(3,1)}
assert GEO[(3,0)]=='düzlem üçgen' and GEO[(3,1)]=='üçgen piramit' and GEO[(2,0)]=='doğrusal'
W18=[('X’in merkez atomu sp² hibritleşmesi yapmıştır.','B atomunun üç F ile bağ yaptığını ve ortaklanmamış çifti olmadığını (3 σ → sp²) görmeyip sp³ olması gerektiğini düşünmüş.','bilgi'),
     ('Y molekülü doğrusaldır.','İki çift bağı olan karbonun kırık yapı oluşturacağını düşünmüş; oysa merkezde ortaklanmamış çift yoktur, iki bağ bölgesi 180° yapar.','bilgi'),
     ('Z’nin geometrisi üçgen piramittir.','Azot üzerindeki ortaklanmamış çifti geometride yok sayıp düzlem üçgen bulmuş; oysa 3 bağ + 1 ortaklanmamış çift üçgen piramit verir.','bilgi'),
     ('Z’deki bağ açıları 109,5°’den küçüktür.','Ortaklanmamış çiftin bağ açısını küçülttüğünü bilmeyip NH₃’te açının 109,5° olduğunu sanmış; oysa açı yaklaşık 107°’dir.','bilgi')]
dg18='X’in geometrisi düzgün dörtyüzlüdür.'
q('0018',tipId='og-geometri',tip='Elektron çifti sayısından molekül geometrisi ve bağ açısı',z='zor',alt='Molekül Geometrisi',kaz='Lewis yapısından hibritleşme, molekül geometrisi ve bağ açısı değerlendirmesi yapar.',kalip='şekilli',
 kart='K-AKOG-05 (VSEPR) · BF₃, CO₂, NH₃ Lewis yapıları',sekil=SK18,
 metin='X, Y ve Z moleküllerinin Lewis yapıları şekilde noktalarla gösterilmiştir. Merkez atomun etrafındaki elektron çifti bölgeleri birbirini en az itecek biçimde yerleşir. (₁H, ₅B, ₆C, ₇N, ₈O, ₉F)\nBuna göre bu moleküllerle ilgili aşağıdaki ifadelerden hangisi yanlıştır?',
 dogru=dg18,yan=W18,sira=yer(dg18,W18,'E'),istenen='Yanlış olan ifade.',
 ip=['Her molekülde merkez atom çevresindeki bağ bölgesi sayısını ve ortaklanmamış çiftleri say; bağ bölgesi sayısı geometriyi, ortaklanmamış çift bağ açısını etkiler.'],
 bilgi=[B('Bağ bölgesi ve geometri','Merkez atomun bağ bölgesi sayısı (çoklu bağ tek bölge sayılır) ve ortaklanmamış çift sayısı geometriyi belirler: 2 bölge → doğrusal, 3 bölge → düzlem üçgen, 4 bölge → dörtyüzlü düzen. Örnek: BeCl₂ doğrusaldır')],
 ad=[A('X’i incele','B’nin 3 bağ bölgesi var, ortaklanmamış çifti yok: sp², düzlem üçgen.','X: sp² · düzlem üçgen · 120°'),A('Y’yi incele','C’nin iki çift bağı iki bölge sayılır: sp, doğrusal.','Y: sp · doğrusal · 180°'),A('Z’yi incele','N’nin 3 bağ bölgesi ve 1 ortaklanmamış çifti var: sp³, üçgen piramit.','Z: sp³ · üçgen piramit · ≈ 107°'),A('Şıkları kontrol et','X için “düzgün dörtyüzlü” ifadesi X’in düzlem üçgen olmasıyla çelişir.','Yanlış olan: X düzgün dörtyüzlüdür')],
 puf='Bağ bölgesi sayısı hibritleşmeyi verir, ortaklanmamış çift sayısı molekül geometrisini ve bağ açısını değiştirir.')
# ============ 19 · orta · şekilli · öncüllü · yanma deneyi ============
g=['\\draw[thick] (0,0) rectangle (2.8,.8); \\node[font=\\small] at (1.4,.4) {X + CuO};',
   '\\fill[vurgu!35] (1.15,-.08) -- (1.65,-.08) -- (1.4,-.55) -- cycle; \\node[font=\\small] at (1.4,-.8) {ısı};',
   '\\draw[thick] (2.8,.4) -- (3.3,.4); \\draw[thick] (4.7,.4) -- (5.9,.4) -- (5.9,-1.1);',
   '\\draw[thick,fill=white] (3.3,.05) rectangle (4.7,.75); \\node[font=\\small] at (4.0,.4) {\\ce{CuSO4}};',
   '\\node[font=\\small,align=center] at (4.0,-.55) {susuz\\\\beyaz toz};',
   '\\fill[vurgu!18] (5.0,-1.6) rectangle (6.8,-.35); \\draw[thick] (5.0,.2) -- (5.0,-1.6) -- (6.8,-1.6) -- (6.8,.2);',
   '\\node[font=\\small,align=center] at (5.9,-2.15) {kireç suyu};']
SK19=tk('\n'.join(g))
T19={'I'}
W19={'I':'kireç suyunu bulandıran CO₂ karbondan, susuz CuSO₄’ü maviye çeviren H₂O hidrojenden oluşur; bu iki gözlem C ve H varlığını gösterir','II':'oysa NaHCO₃ gibi anorganik bir bileşik de ısıtıldığında CO₂ ve H₂O verebilir; bu deney maddenin organik olduğunu kesinleştirmez','III':'oysa CuO oksijen verdiğinden oluşan CO₂ ve H₂O’daki oksijen X’ten gelmek zorunda değildir'}
d19,y19,L19=oc(T19,'A',W19)
q('0019',tipId='og-ayrim',tip='Organik ve anorganik bileşiklerin ayrımı',z='orta',alt='Organik ve Anorganik Bileşikler',kaz='Isıtmayla elde edilen CO₂ ve H₂O gözleminden bileşikteki elementleri yorumlar.',kalip='şekilli',
 kart='K-AKOG-08 (organik madde tanıma) · CuO ile ısıtma',sekil=SK19,
 metin='Katı hâldeki X maddesi, bakır(II) oksit (CuO) ile karıştırılıp şekildeki düzenekte kuvvetle ısıtılıyor. Çıkan gazlar önce susuz CuSO₄’ten, sonra kireç suyundan geçiriliyor. Deney sonunda beyaz renkli susuz CuSO₄’ün maviye döndüğü ve kireç suyunun bulandığı gözleniyor.\nBuna göre X maddesiyle ilgili,\nI. Yapısında karbon ve hidrojen atomları bulunur.\nII. Organik bir bileşiktir.\nIII. Yapısında oksijen atomu bulunur.\nyargılarından hangileri kesinlikle doğrudur?',
 dogru=d19,yan=y19,sira=L19,istenen='Kesinlikle doğru olan yargılar.',
 ip=['Gözlenen iki değişimin hangi maddelerin oluştuğunu gösterdiğini bul; bu maddelerdeki atomların hangi kaynaklardan gelmiş olabileceğini düşün.'],
 bilgi=[B('Organik madde tanıma','Isıtılan madde CO₂ veriyorsa kireç suyu bulanır (C varlığı); H₂O veriyorsa susuz CuSO₄ maviye döner (H varlığı). Oksijen deneyde CuO ya da havadan da gelebilir. Örnek: yalnız H₂O veren bir madde için hidrojen varlığı kesindir, ancak oksijenin kaynağı belli olmaz')],
 ad=[A('Gözlemleri yorumla','Kireç suyunun bulanması CO₂’yi, CuSO₄’ün maviye dönmesi H₂O’yu gösterir.','CO₂ → C · H₂O → H'),A('I’i değerlendir','C ve H atomları X’ten gelir.','I doğru'),A('II’yi değerlendir','Karbon ve hidrojen içeren her madde organik değildir.','II kesin değil'),A('III’ü değerlendir','CuO oksijen sağlar; X’te oksijen olup olmadığı belli olmaz.','III kesin değil'),A('Sonucu yaz','Kesin doğru olan yalnız I’dir.','Yalnız I')],
 puf='Yanma ürünleri yalnız C ve H varlığını gösterir; oksijen için ayrıca bilgi gerekir ve organik olma sonucu kesin değildir.')
# ============ 20 · zor · tablo · yüzde bileşim + gaz hacmi + σ bağı ============
pC,pH=Fr(80),Fr(20); m20=Fr(6); V20=Fr(448,100); n20=V20/Fr(224,10); assert n20==Fr(1,5); M20=m20/n20; assert M20==30
rr_=(pC/12,pH/1); assert rr_[1]/rr_[0]==3
bs=(1,3); assert M20/(12+3)==2; fm20=(2,6); sig20=(fm20[0]-1)+fm20[1]; assert sig20==7
ans20=n20*sig20; assert ans20==Fr(14,10)
d_a=(m20/15)*7; d_b=n20*6; d_c=n20*8; d_d=n20*1; assert (d_a,d_b,d_c,d_d)==(Fr(28,10),Fr(12,10),Fr(16,10),Fr(2,10))
SK20=tablo_svg(['Element','Kütlece yüzde (%)'],[['Karbon','80'],['Hidrojen','20']])
q('0020',tipId='og-formul',tip='Basit formül, molekül formülü ve yanma analizi',z='zor',alt='Basit Formül ve Molekül Formülü',kaz='Kütlece yüzde bileşim ve gaz hacminden molekül formülünü bulup moleküldeki σ bağı miktarını hesaplar.',kalip='tablo',
 kart='K-AKOG-06 (basit/molekül formülü) · yüzde bileşim, gaz hacmi, σ bağı',sekil=SK20,
 metin='Yalnız C ve H elementlerinden oluşan bir organik bileşiğin kütlece yüzde bileşimi şekildeki tabloda verilmiştir. Bu bileşiğin gaz hâldeki 6 gramı normal koşullarda 4,48 L hacim kaplamaktadır. (H = 1, C = 12 g/mol; normal koşullarda 1 mol gaz 22,4 L hacim kaplar)\nBuna göre bu bileşiğin 6 gramında toplam kaç mol σ bağı bulunur?',
 dogru=Fr(14,10),yan=[(Fr(2,10),'Sorulan σ bağı mol sayısı yerine bileşiğin mol sayısını (0,2) vermiş.','dikkat'),(Fr(12,10),'C–C bağını atlayıp yalnız 6 C–H bağını σ saymış: 0,2 × 6 = 1,2 mol.','dikkat'),(Fr(16,10),'Moleküldeki toplam atom sayısını (8) σ bağı sayısı sanmış: 0,2 × 8 = 1,6 mol.','bilgi'),(Fr(28,10),'Basit formül kütlesini (15 g/mol) mol kütlesi alıp mol sayısını 0,4 bulmuş; her molekülde 7 σ bağı olduğundan 0,4 × 7 = 2,8 mol bulmuş.','islem')],
 istenen='6 gram bileşikteki toplam σ bağı mol sayısı.',
 ip=['Önce bileşiğin mol sayısından mol kütlesini, yüzdelerden basit formülü bul; molekül formülünü belirleyip bir moleküldeki σ bağlarını say.'],
 bilgi=[B('Yüzde bileşimden formül','Yüzdeler 100 g örnekteki gram olarak alınır; mol sayıları oranlanarak basit formül, mol kütlesiyle molekül formülü bulunur. Örnek: %75 C, %25 H içeren bileşikte C : H = 6,25 : 25 = 1 : 4 → CH₄')],
 ad=[A('Mol kütlesini bul','n = V ÷ 22,4 ve M = m ÷ n.','n = 4,48 ÷ 22,4 = 0,2 mol · M = 6 ÷ 0,2 = 30 g/mol'),A('Basit formülü bul','100 g örnekte 80 g C, 20 g H vardır.','C : H = 80 ÷ 12 : 20 ÷ 1 = 6,67 : 20 = 1 : 3 → CH₃'),A('Molekül formülünü bul','CH₃ = 15 g/mol; n = 30 ÷ 15.','n = 2 → C₂H₆'),A('σ bağlarını say','Tek bağ içeren C₂H₆’da 6 C–H ve 1 C–C bağı vardır.','7 σ bağı / molekül'),A('Toplam σ miktarını hesapla','0,2 mol molekül × 7 σ.','0,2 × 7 = 1,4 mol σ')],
 puf='Mol sayısı → mol kütlesi → molekül formülü → bağ sayısı; her molekülün bağ sayısını mol sayısıyla çarp.')
# ---------------- yaz ----------------
from collections import Counter
for qq in P.ANA: qq['kardes']=None
os.makedirs(HD,exist_ok=True)
P.yaz(HD+'/orggiris-1.json','/dev/null')
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=UK))['kartlar'].append(c['id'])
json.dump(dict(konu=KONU_,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT Kimya 2018–2026 (yalnız mantık), MEB 12. sınıf kimya.',kartlar=H.KARTLAR,tipler=list(tipler.values())),open(HV+'/kartlar/akorggiris.json','w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler),'· kalıp',dict(Counter(q_['kalip'] for q_ in P.ANA)),'· şekilli',sum(1 for q_ in P.ANA if q_['sekil']))
