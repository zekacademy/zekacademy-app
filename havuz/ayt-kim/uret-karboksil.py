"""AYT Kimya · Karboksilik Asitler ve Esterler · 20 soru. Kardeş yok, ipucu 1.
Yapılar tek bir atom listesinden hem çizilir hem çözümlenir (formül); izomer sayıları ve sayısal cevaplar kodla doğrulanır."""
import sys,os,json,math
from fractions import Fraction as Fr
from itertools import permutations
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-kim'))
import _hafif_kim2 as H
from _hafif_kim2 import *
from _hafif_kim import onc,tek,etk
import networkx as nx
KONU_AD='Karboksilik Asitler ve Esterler'; KEY='akim|Karboksilik Asitler ve Esterler'
P=Parti('karboksil',KONU_AD,KEY,ders='AYT Kimya',idon='aytkim'); H.KONU=KONU_AD
KAYNAK='ÖSYM AYT 2018–2026 Kimya karboksilik asit–ester soruları (yalnız mantık) · MEB 12. sınıf Organik Bileşikler'
def kartla(no,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(f'K-AKKAR-{no}',alt,fikir,tuzak,z,kalip,adim,tipId,tip,KAYNAK)
def q(no,ad,**k):
    assert len(k['ip'])==1; mk(P,no,ad=ad,adim=len(ad),**k)
TIP={'ad':('ka-adlandirma','Karboksilik asit ve ester adlandırma'),'sinif':('ka-sinif','Fonksiyonel grup ve yapı izomerliği'),
     'asit':('ka-asitlik','Asitlik ve asit sabiti'),'fiz':('ka-fiziksel','Fiziksel özellikler ve hidrojen bağı'),
     'tep':('ka-tepkime','Karboksilik asitlerin tepkimeleri'),'est':('ka-esterlesme','Esterleşme ve hidroliz'),
     'sab':('ka-sabun','Sabunlaşma ve sabun'),'yag':('ka-yag','Yağlar ve yağ asitleri')}
def Q(no,tp,z,kalip,alt,kaz,fikir,tuzak,ozet,ad,**k):
    t,tn=TIP[tp]; kartla(no[-2:],alt,fikir,tuzak,z,kalip,len(ad),t,tn)
    q(no,ad,tipId=t,tip=tn,z=z,alt=alt,kaz=kaz,kalip=kalip,kart=f'K-AKKAR-{no[-2:]} ({ozet})',**k)
def yer(dogru,digerler,i): return list(digerler[:i])+[dogru]+list(digerler[i:])
ORD=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
def OC(d,sira): return onc(d,[tuple(x for x in t.replace('Yalnız ','').replace(',',' ').replace(' ve ',' ').split()) for t in sira])
def sr(*k): assert [x for x in ORD if x in k]==list(k),k; return list(k)

# ---------------- yapı modeli (iskelet formülü) ----------------
# spec: (ad, ebeveyn, açı°, etiket, bağ derecesi). Etiketsiz düğüm = karbon; 'O' = oksijen; 'OH'/'HO' = hidroksil.
def konum(spec,sc,ox=0.0,oy=0.0):
    P_={}
    for n,p,a,l,o in spec:
        P_[n]=(ox,oy) if p is None else (P_[p][0]+sc*math.cos(math.radians(a)),P_[p][1]+sc*math.sin(math.radians(a)))
    return P_
def formul(spec):
    G_=nx.Graph(); lab={}
    for n,p,a,l,o in spec:
        G_.add_node(n); lab[n]=l
        if p is not None: G_.add_edge(n,p,o=o)
    C=sum(1 for n in lab if lab[n] is None); O=sum(1 for n in lab if lab[n] in('O','OH','HO'))
    H_=sum(4-sum(G_[n][m]['o'] for m in G_[n]) for n in lab if lab[n] is None)+sum(1 for n in lab if lab[n] in('OH','HO'))
    return C,H_,O
def draw(spec,ox,oy,sc=0.8,fs='\\small',sh=0.17):
    Pn=konum(spec,sc,ox,oy); lab={n:l for n,p,a,l,o in spec}; out=[]
    for n,p,a,l,o in spec:
        if p is None: continue
        (x1,y1),(x2,y2)=Pn[p],Pn[n]; L=math.hypot(x2-x1,y2-y1); ux,uy=(x2-x1)/L,(y2-y1)/L
        s1=sh if lab[p] else 0; s2=sh if l else 0
        a1=(x1+ux*s1,y1+uy*s1); a2=(x2-ux*s2,y2-uy*s2); nx_,ny_=-uy,ux
        for f in ([0] if o==1 else [-0.045,0.045]):
            out.append(f'\\draw[thick] ({a1[0]+nx_*f:.3f},{a1[1]+ny_*f:.3f}) -- ({a2[0]+nx_*f:.3f},{a2[1]+ny_*f:.3f});')
    for n,p,a,l,o in spec:
        if not l: continue
        x,y=Pn[n]
        if l=='HO': out.append(f'\\node[inner sep=0pt,anchor=east,font={fs}] at ({x+0.09:.3f},{y:.3f}) {{HO}};')
        elif l=='OH': out.append(f'\\node[inner sep=0pt,anchor=west,font={fs}] at ({x-0.09:.3f},{y:.3f}) {{OH}};')
        else: out.append(f'\\node[inner sep=0pt,font={fs}] at ({x:.3f},{y:.3f}) {{{l}}};')
    return '\n'.join(out)
def kutu(spec,sc=0.8):
    Pn=konum(spec,sc); lab={n:l for n,p,a,l,o in spec}
    xs=[Pn[n][0] for n in Pn]; ys=[Pn[n][1] for n in Pn]
    return min(xs)-.2,max(xs)+.2,min(ys)-.2,max(ys)+.2
def sahne(items,bosluk=1.0,sc=0.8):
    """items: [(spec,etiket)]; tek satır; etiketler molekülün altında, hepsi aynı hizada."""
    x=0.0; parts=[]
    for spec,et in items:
        b=kutu(spec,sc); ox=x-b[0]; parts.append((spec,et,ox,b)); x=ox+b[1]+bosluk
    ymin=min(p[3][2] for p in parts); out=[]
    for spec,et,ox,b in parts:
        out.append(draw(spec,ox,0,sc))
        if et: out.append(f'\\node[font=\\small\\bfseries] at ({ox+(b[0]+b[1])/2:.3f},{ymin-.4:.3f}) {{{et}}};')
    return '\n'.join(out)
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'; TAIL='\n\\end{tikzpicture}'
ARR='-{Stealth[length=2.2mm,width=2mm]}'
def tk(g): return tikz_svg(HEAD+g+TAIL)
def fa_nodes(nC,cis=None,pre='c'):
    """c1 yüksekte; c1→c2 aşağı (−30°). cis: çift bağın başladığı bağ numarası (kıvrım)."""
    out=[]
    for k in range(1,nC):
        if cis is None: a=-30 if k%2==1 else 30
        elif k<cis: a=-30 if k%2==1 else 30
        elif k==cis: a=0
        else: a=-30 if k%2==0 else 30
        out.append((f'{pre}{k+1}',f'{pre}{k}',a,None,2 if k==cis else 1))
    return out
def yagasit(nC,cis=None):
    return [('c1',None,0,None,1),('o1','c1',90,'O',2),('h1','c1',210,'HO',1)]+fa_nodes(nC,cis)
def formul_h(spec): return formul(spec)

# --- yapılar ---
M_3MBA=[('c1',None,0,None,1),('o','c1',90,'O',2),('h','c1',210,'HO',1),('c2','c1',-30,None,1),('c3','c2',30,None,1),('m','c3',90,None,1),('c4','c3',-30,None,1)]   # 3-metilbütanoik asit
M_PROPA=[('c1',None,0,None,1),('o','c1',90,'O',2),('h','c1',210,'HO',1),('c2','c1',-30,None,1),('c3','c2',30,None,1)]                              # propanoik asit
M_ME_ETA=[('a',None,0,None,1),('c','a',30,None,1),('od','c',90,'O',2),('oe','c',-30,'O',1),('d','oe',30,None,1)]                                  # metil etanoat
M_PROPOL=[('o',None,0,'HO',1),('c1','o',-30,None,1),('c2','c1',30,None,1),('c3','c2',-30,None,1)]                                                    # 1-propanol
M_ET_PROP=[('a',None,0,None,1),('b','a',30,None,1),('c','b',-30,None,1),('od','c',-90,'O',2),('oe','c',30,'O',1),('d','oe',-30,None,1),('e','d',30,None,1)]  # etil propanoat
M_ET_ETA=[('a',None,0,None,1),('c','a',30,None,1),('od','c',90,'O',2),('oe','c',-30,'O',1),('d','oe',30,None,1),('e','d',-30,None,1)]              # etil etanoat
assert formul(M_3MBA)==(5,10,2) and formul(M_PROPA)==(3,6,2) and formul(M_ME_ETA)==(3,6,2) and formul(M_PROPOL)==(3,8,1)
assert formul(M_ET_PROP)==(5,10,2) and formul(M_ET_ETA)==(4,8,2)
assert formul(yagasit(18))==(18,36,2) and formul(yagasit(18,9))==(18,34,2)
assert formul(yagasit(18,9)) [1]==34
# trigliserit (triolein): gliserol C3H5 + 3 × oleoil
def oleoil(): return [('o',None,0,'O',1),('c1','o',30,None,1),('co','c1',90,'O',2)]+fa_nodes(18,9)[0:0]
OLE=[('o',None,0,'O',1),('c1','o',30,None,1),('co','c1',90,'O',2)]+fa_nodes(18,9)
C_,H_,O_=formul(OLE); assert (C_,H_,O_)==(18,33,2),(C_,H_,O_)
TG=(3+3*C_,5+3*H_,3*O_); assert TG==(57,104,6)
MTG=TG[0]*12+TG[1]+TG[2]*16; assert MTG==884
ATOM={'C':12,'H':1,'O':16,'Na':23}

def alkil(n):
    if n==0: return 1
    bulunan=[]
    for T in nx.nonisomorphic_trees(n) if n>1 else [nx.empty_graph(1)]:
        for r in T.nodes:
            if T.degree(r)>3: continue
            G2=T.copy(); nx.set_node_attributes(G2,{m:(m==r) for m in G2.nodes},'r')
            if any(nx.is_isomorphic(G2,B2,node_match=lambda a,b:a['r']==b['r']) for B2 in bulunan): continue
            bulunan.append(G2)
    return len(bulunan)
assert [alkil(i) for i in range(5)]==[1,1,1,2,4]
def asit_ester(n):
    asit=alkil(n-1); ester=sum(alkil(a)*alkil(n-1-a) for a in range(0,n-1) if n-1-a>=1)
    return asit,ester

# ================= 01 · adlandırma · kolay · şekil =================
dg='3-metilbütanoik asit'
yan1=[('2-metilbütanoik asit','Numaralandırmayı karboksil karbonundan değil, zincirin öbür ucundan başlatmış; oysa karboksil karbonu her zaman 1. karbondur.','bilgi'),
      ('3-metilbütanal','Karboksil grubunu aldehit grubu gibi adlandırıp “-al” ekini kullanmış; oysa –COOH grubu “-oik asit” ekini alır.','bilgi'),
      ('3-metilbütan-1-ol','Karboksil grubundaki oksijenleri sayarak bileşiği alkol sanmış; oysa karbonu iki oksijene bağlı grup karboksildir.','bilgi'),
      ('2-metilpropil metanoat','Yapıyı asit değil ester sanıp ad vermiş; oysa şekilde karboksil grubunun –OH ucu vardır.','bilgi')]
SK=tk(sahne([(M_3MBA,None)]))
Q('0001','ad','kolay','şekilli','Karboksilik asit adlandırma','İskelet formülü verilen karboksilik asidi IUPAC kurallarına göre adlandırır.',
  'Ana zincir karboksil karbonunu içeren en uzun zincirdir; karboksil karbonu 1. karbon olur, dallar bu numaralamaya göre adlandırılır ve ad “-oik asit” ile biter.','Karboksil grubunu aldehit ya da ester gibi adlandırmak ya da numaralamayı yanlış uçtan başlatmak.','3-metilbütanoik asit',
  [A('Ana zinciri seç','Karboksil karbonunu içeren en uzun zinciri bul.','4 karbon → bütanoik asit'),A('Numaralandır','Karboksil karbonu 1. karbondur, sayım ondan başlar.','COOH karbonu = 1'),A('Dalı yerleştir','Metil grubunun bağlı olduğu karbonun numarasını oku.','Metil 3. karbonda → 3-metil'),A('Adı yaz','Dal adı, konumu ve ana zincir adı birleştirilir.','3-metilbütanoik asit')],
  metin='Bir karboksilik asidin iskelet formülü şekilde gösterilmiştir; köşe ve uç noktalarda karbon atomu bulunur, karbona bağlı hidrojen atomları yazılmamıştır.\nBuna göre bu bileşiğin sistematik adı aşağıdakilerden hangisidir?',
  sekil=SK,istenen='Bileşiğin IUPAC adı.',ip=['Karboksil grubunun karbonunu 1 kabul ederek zincirin en uzun yolunu numaralandır.'],
  bilgi=[B('Karboksilik asit adlandırma','Karboksil karbonu 1. karbon olacak biçimde en uzun zincir seçilir, dallar numaralanır ve ad “alkan adı + -oik asit” biçiminde yazılır. Örnek: CH₃–CH₂–CH₂–COOH bütanoik asit, (CH₃)₂CH–COOH 2-metilpropanoik asittir')],
  puf='Karboksilik asitte numaralama her zaman –COOH karbonundan başlar.',dogru=dg,yan=yan1,sira=yer(dg,[y[0] for y in yan1],0))

# ================= 02 · fonksiyonel grup ve izomer · kolay · öncüllü · şekil =================
assert formul(M_PROPA)==formul(M_ME_ETA)[:2]+(2,) and formul(M_PROPA)!=formul(M_PROPOL)
d=dict(I=(True,'A bileşiğinde karbon atomuna hem =O hem –OH bağlıdır; bu grup karboksildir ve A karboksilik asittir'),
       II=(True,'A ile B’nin molekül formülü C₃H₆O₂’dir, fakat atomları farklı düzende bağlıdır; iki bileşik birbirinin yapı izomeridir'),
       III=(False,'C bileşiği –OH grubu taşıyan bir alkoldür; B ise ester grubu (–COO–) içerir ve bu iki bileşiğin fonksiyonel grupları farklıdır'))
o=OC(d,sr('Yalnız I','I ve II','I ve III','II ve III','I, II ve III')); assert o['dogru']=='I ve II'
SK=tk(sahne([(M_PROPA,'A'),(M_ME_ETA,'B'),(M_PROPOL,'C')]))
Q('0002','sinif','kolay','öncüllü','Fonksiyonel grup ve izomerlik','Karboksil, ester ve hidroksil gruplarını yapıdan tanır; molekül formülünden yapı izomerliğini yorumlar.',
  'Karbonu hem çift bağlı oksijene hem –OH’ye bağlı olan grup karboksil, çift bağlı oksijen ile ikinci bir oksijen üzerinden karbon zincirine bağlı grup esterdir; aynı formüllü farklı yapılar izomerdir.','Esteri karboksilik asit sanmak ya da farklı molekül formüllü bileşikleri izomer saymak.','A, B, C bileşikleri',
  [A('A’yı incele','C=O ve –OH aynı karbona bağlı.','A: karboksilik asit → I doğru'),A('Formülleri yaz','A ve B’de 3 C, 6 H ve 2 O vardır.','A: C₃H₆O₂ · B: C₃H₆O₂'),A('Yapıları karşılaştır','Aynı formül, farklı bağlanma: izomerlik.','A ve B yapı izomeri → II doğru'),A('C’yi incele','C’de –OH vardır, ester grubu yoktur.','C: alkol, B: ester → III yanlış')],
  metin='Şekilde iskelet formülleri verilen A, B ve C bileşiklerinde köşeler ve uçlar karbon atomunu göstermektedir; karbona bağlı hidrojen atomları yazılmamıştır.\nI. A bileşiği karboksilik asittir.\nII. A ve B bileşikleri birbirinin yapı izomeridir.\nIII. B ve C bileşikleri aynı fonksiyonel grubu içerir.\nBuna göre bu yargılardan hangileri doğrudur?',
  sekil=SK,istenen='Doğru olan yargılar.',ip=['Her bileşikteki oksijen atomlarının nasıl bağlandığına bak; ardından molekül formüllerini karşılaştır.'],
  bilgi=[B('Karboksil ve ester grubu','Karboksilik asit grubu –COOH (C=O ve –OH aynı karbonda), ester grubu –COO– biçimindedir ve oksijenin diğer ucu bir alkil grubuna bağlıdır. Örnek: CH₃COOH asit, HCOOC₂H₅ esterdir; ikisinin formülü farklıdır')],
  puf='Aynı karbonda C=O ve –OH varsa asit, C=O ile birlikte –O–R varsa ester vardır.',dogru=o['dogru'],yan=o['yan'],sira=o['sira'])

# ================= 03 · adlandırma · kolay · olumsuz kök =================
sec=[('HCOOH: metanoik asit',True,'bir karbonlu karboksilik asit metanoik asit adını alır.'),
     ('CH₃CH₂COOH: propanoik asit',True,'karboksil karbonu dahil üç karbonlu zincir propanoik asittir.'),
     ('CH₃COOCH₂CH₃: etil etanoat',True,'asit kısmı iki karbonlu (etanoat), alkol kısmı etil grubudur.'),
     ('HCOOCH₂CH₃: metil etanoat',False,'adlandırmada önce alkol kökü, sonra asit kökü yazılır; bu ester etil metanoattır.'),
     ('CH₃CH₂COOCH₃: metil propanoat',True,'asit kısmı üç karbonlu (propanoat), alkol kısmı metil grubudur.')]
o=tek(sec,False)
Q('0003','ad','kolay','düz','Ester adlandırma','Basit karboksilik asit ve ester formüllerini adlarıyla eşleştirir.',
  'Ester adı “alkol kökü + asit adındaki -oik asit yerine -oat” biçimindedir: alkolden gelen grup önce, asitten gelen kısım sonra yazılır.','Asitten ve alkolden gelen kısımların sırasını karıştırmak.','ester adlandırma',
  [A('Esterin yapısını oku','–COO– grubunun C=O taşıyan tarafı asitten, oksijene bağlı alkil tarafı alkolden gelir.','R–CO–O–R′ : R asit, R′ alkol kısmı'),A('Asit kısmını adlandır','Karbon sayısına göre “-oat” adı belirlenir.','HCOO– metanoat · CH₃COO– etanoat'),A('Alkol kısmını adlandır','Oksijene bağlı alkil grubunun adı başa yazılır.','–CH₃ metil · –CH₂CH₃ etil'),A('Eşleştirmeleri denetle','Tek tek formülü ad ile karşılaştır.','HCOOCH₂CH₃ → etil metanoat')],
  metin='Bir öğrenci, karboksilik asit ve ester formüllerini ad kartlarıyla eşleştirirken aşağıdaki eşleştirmeleri yapıyor.\nBuna göre bu eşleştirmelerden hangisi yanlıştır?',
  istenen='Formülü ile adı uyuşmayan eşleştirme.',ip=['Esterlerde asit kısmını –C(=O)– grubunun bağlı olduğu tarafta, alkol kısmını oksijenin bağlandığı alkil grubunda ara.'],
  bilgi=[B('Ester adlandırma','Ester adı “alkil adı + asit adı (-oat)” biçiminde yazılır; CH₃CH₂COOCH₂CH₂CH₃ için propil propanoat. Karboksil karbonunu taşıyan taraf asit, oksijene bağlı taraf alkol kökenlidir')],
  puf='Ester adında önce oksijene bağlı alkil, sonra C=O’lu asit kısmı okunur.',dogru=o['dogru'],yan=o['yan'],sira=o['sira'])

# ================= 04 · asitlik · orta · tablo · öncüllü =================
d=dict(I=(False,'pH değeri en düşük olan, Ka değeri en büyük olan metanoik asit çözeltisidir; çünkü eşit derişimde Ka büyüdükçe [H⁺] artar ve pH azalır'),
       II=(True,'eşit derişimde Ka büyüdükçe iyonlaşma yüzdesi artar ve metanoik asidin Ka değeri üçü arasında en büyüğüdür'),
       III=(True,'Ka değeri en küçük olan propanoik asit en zayıf asittir; asit zayıfladıkça eşlenik bazı kuvvetlenir, bu yüzden propanoat iyonu en kuvvetli bazdır'))
o=OC(d,sr('Yalnız I','Yalnız II','I ve II','I ve III','II ve III')); assert o['dogru']=='II ve III'
KA={'Metanoik asit':Fr(18,10**5)*10,'Etanoik asit':Fr(18,10**5),'Propanoik asit':Fr(13,10**5)}
assert KA['Metanoik asit']>KA['Etanoik asit']>KA['Propanoik asit']
SK=tablo_svg(['Asit','Ka (25 °C)'],[['Metanoik asit','1,8 · 10⁻⁴'],['Etanoik asit','1,8 · 10⁻⁵'],['Propanoik asit','1,3 · 10⁻⁵']])
Q('0004','asit','orta','tablo','Asitlik ve Ka','Ka değerlerini karşılaştırarak karboksilik asitlerin gücünü, pH sırasını ve eşlenik baz gücünü yorumlar.',
  'Aynı derişimde Ka büyük olan asit daha çok iyonlaşır, pH’si daha düşüktür ve eşlenik bazı daha zayıftır.','Ka büyüdükçe pH’nin de büyüyeceğini sanmak ya da asit kuvveti ile eşlenik baz kuvvetini aynı yönde değerlendirmek.','Ka tablosu',
  [A('Ka değerlerini sırala','Ka büyüklüğü asit gücünü verir.','Metanoik > etanoik > propanoik'),A('I’i değerlendir','En kuvvetli asidin çözeltisinde [H⁺] en yüksektir.','En düşük pH: metanoik asit → I yanlış'),A('II’yi değerlendir','Ka büyük olan asidin iyonlaşma yüzdesi büyüktür.','Metanoik asit → II doğru'),A('III’ü değerlendir','Zayıf asidin eşlenik bazı kuvvetlidir.','Propanoik asit en zayıf → III doğru')],
  metin='Aynı sıcaklıkta üç karboksilik asidin asitlik sabitleri (Ka) tabloda verilmiştir. Bu asitlerin 0,1 M derişimli sulu çözeltileri hazırlanıyor.\nI. pH değeri en yüksek olan çözelti metanoik asit çözeltisidir.\nII. İyonlaşma yüzdesi en büyük olan asit metanoik asittir.\nIII. Eşlenik bazı en kuvvetli olan asit propanoik asittir.\nBuna göre bu yargılardan hangileri doğrudur?',
  sekil=SK,istenen='Doğru olan yargılar.',ip=['Ka değerlerini büyükten küçüğe sırala; sıradaki yerin pH, iyonlaşma yüzdesi ve eşlenik baz gücünü nasıl etkilediğini düşün.'],
  bilgi=[B('Ka ve asit gücü','Zayıf asitte Ka büyüdükçe asit kuvvetlenir; aynı derişimde [H⁺] artar, pH azalır, iyonlaşma yüzdesi artar. Bir asit ne kadar zayıfsa eşlenik bazı o kadar kuvvetlidir. Örnek: Ka = 10⁻³ olan asit, Ka = 10⁻⁶ olan asitten kuvvetlidir')],
  puf='Ka büyükse asit güçlü, pH düşük, iyonlaşma yüzdesi yüksek, eşlenik baz zayıftır.',dogru=o['dogru'],yan=o['yan'],sira=o['sira'])

# ================= 05 · kaynama noktası · orta · grafik =================
BP={'CH₃CH₂CH₂OH':97,'CH₃COOH':118,'HCOOCH₃':32}
sirala=lambda a,b,c:f'{a}, {b}, {c}'
dogru5=sirala('CH₃CH₂CH₂OH','CH₃COOH','HCOOCH₃')   # X=97, Y=118, Z=32
bx,by,bz=97,118,32; assert (BP['CH₃CH₂CH₂OH'],BP['CH₃COOH'],BP['HCOOCH₃'])==(bx,by,bz)
yan5=[(sirala('CH₃COOH','CH₃CH₂CH₂OH','HCOOCH₃'),'Alkolün kaynama noktasını asitten yüksek sanmış; oysa asit molekülleri ikişer hidrojen bağıyla dimer oluşturduğundan karboksilik asidin kaynama noktası alkolden yüksektir.','bilgi'),
      (sirala('HCOOCH₃','CH₃COOH','CH₃CH₂CH₂OH'),'Esterin kaynama noktasını alkolünkinden yüksek sanmış; oysa esterde O–H bağı yoktur ve saf esterde hidrojen bağı oluşmaz.','bilgi'),
      (sirala('CH₃CH₂CH₂OH','HCOOCH₃','CH₃COOH'),'Esteri asitten daha yüksek, asidi en düşük kaynama noktalı sanmış; oysa asit dimerleşerek üçü arasında en yüksek kaynama noktasına sahiptir.','bilgi'),
      (sirala('HCOOCH₃','CH₃CH₂CH₂OH','CH₃COOH'),'Üç bileşiğin molekül kütlelerinin eşit olmasına bakıp sıralamayı yalnız hidrojen bağı sayısına göre değil, esteri en düşük, asidi en yüksek alarak ters kurmuş; oysa asit en yüksek, ester en düşüktür ve bu sıra Z, X, Y için değil X, Y, Z için sorulmuştur.','dikkat')]
yan5[3]=(yan5[3][0],'Esteri ve alkolü ters yerleştirmiş; oysa en düşük kaynama noktası hidrojen bağı yapamayan estere, ortadaki değer alkole aittir.','bilgi')
SK=tk('''\\draw[thick,-{Stealth}] (0,0) -- (0,5.6);\\draw[thick] (0,0) -- (5.2,0);
\\foreach \\v/\\y in {0/0,20/0.8,40/1.6,60/2.4,80/3.2,100/4.0,120/4.8}{\\draw (0,\\y) -- (-.1,\\y); \\node[left,font=\\small] at (-.1,\\y) {\\v}; \\draw[dotted,gray] (0,\\y) -- (5.2,\\y);}
\\node[font=\\small,rotate=90] at (-1.0,2.8) {Normal kaynama noktası ($^\\circ$C)};
\\foreach \\x/\\h/\\n in {1.0/%.2f/X,2.7/%.2f/Y,4.4/%.2f/Z}{\\fill[vurgu!35] (\\x-.5,0) rectangle (\\x+.5,\\h); \\draw[thick] (\\x-.5,0) rectangle (\\x+.5,\\h); \\node[font=\\small\\bfseries,below] at (\\x,0) {\\n};}''' % (bx*0.04,by*0.04,bz*0.04))
Q('0005','fiz','orta','grafik','Kaynama noktası karşılaştırması','Benzer molekül kütleli asit, alkol ve esterin kaynama noktalarını hidrojen bağı türüne göre sıralar.',
  'Karboksilik asitler dimer oluşturarak, alkoller hidrojen bağıyla birbirine bağlanır; esterlerde O–H bağı olmadığından molekül kütlesi benzer bileşikler arasında kaynama noktası sırası asit > alkol > ester olur.','Hidrojen bağı yapabilen bileşiklerin kaynama noktasını esterinkiyle eşit ya da alkolünkinden düşük saymak.','kaynama noktası sütun grafiği',
  [A('Molekül kütlelerini karşılaştır','Üç bileşiğin de mol kütlesi 60 g/mol’dür.','London kuvvetleri benzer'),A('Hidrojen bağı durumunu belirle','Asit ve alkol O–H taşır; ester taşımaz.','Asit, alkol: H bağı · ester: yok'),A('Asit ile alkolü ayır','Asit moleküllerinin dimer yapması etkileşimi güçlendirir.','Asit > alkol > ester'),A('Grafikle eşleştir','Sütun yüksekliği sıralamayı belirler.','Y (en yüksek) asit · X alkol · Z (en düşük) ester')],
  metin='Molekül kütleleri birbirine eşit (60 g/mol) olan CH₃COOH, CH₃CH₂CH₂OH ve HCOOCH₃ bileşiklerinin normal kaynama noktaları şekildeki sütun grafiğinde X, Y ve Z ile gösterilmiştir.\nBuna göre X, Y ve Z ile gösterilen bileşikler sırasıyla aşağıdakilerden hangisinde doğru verilmiştir?',
  sekil=SK,istenen='X, Y ve Z’nin sırasıyla hangi bileşikler olduğu.',ip=['Hangi bileşiklerin saf hâlde hidrojen bağı yapabildiğini ve bu bağın moleküller arasında nasıl bir düzen kurduğunu düşün.'],
  bilgi=[B('Kaynama noktası ve etkileşim','Kütleleri benzer maddelerde kaynama noktasını moleküller arası etkileşim belirler. Karboksilik asitler iki hidrojen bağıyla dimer yapar, alkoller hidrojen bağı kurar, esterler yalnız dipol–dipol ve London kuvvetleri gösterir. Örnek: CH₃CH₂OH, CH₃OCH₃’ten yüksek kaynar')],
  puf='Benzer kütlede kaynama noktası sırası: karboksilik asit > alkol > ester.',dogru=dogru5,yan=yan5,sira=yer(dogru5,[y[0] for y in yan5],0))

# ================= 06 · dimer · orta · şekil · olumsuz kök =================
sec=[('Şekildeki kesikli çizgiler, iki molekül arasındaki hidrojen bağlarını göstermektedir.',True,'kesikli çizgiler O–H···O hidrojen bağlarıdır.'),
     ('Etanoik asit, saf hâlde molekülleri arasında hidrojen bağı oluşturmaz.',False,'karboksil grubundaki O–H bağı sayesinde saf etanoik asitte moleküller arasında hidrojen bağı vardır.'),
     ('Dimer oluşumu, etanoik asidin kaynama noktasının benzer kütleli alkollerinkinden yüksek olmasına katkı sağlar.',True,'ikişer hidrojen bağıyla bağlanan dimerler, ayrılması için daha çok enerji gerektiren kararlı yapılardır.'),
     ('Karboksil grubundaki C=O oksijeni, hidrojen bağında H atomunu çeken uç olarak görev yapar.',True,'çift bağlı oksijen, komşu moleküldeki O–H hidrojenine bağlanır.'),
     ('Kısa zincirli karboksilik asitler suyla hidrojen bağı yaparak çözünür.',True,'karboksil grubu su molekülleriyle hidrojen bağı kurabilir.')]
o=tek(sec,False); assert o['sira'][1]==sec[1][0]
g=('\\draw[thick] (0,0) -- (.85,.45)--(.85,.45);'
   '\\draw[thick] (0.0,0) -- (0.7,0.37);\\draw[thick] (0.04,-0.04) -- (0.74,0.33);'
   '\\draw[thick] (0,0) -- (0.7,-0.40);'
   '\\draw[thick] (3.7,0) -- (3.0,-0.37);\\draw[thick] (3.66,0.04) -- (2.96,-0.33);'
   '\\draw[thick] (3.7,0) -- (3.0,0.40);'
   '\\draw[thick] (0,0) -- (-0.75,0);\\draw[thick] (3.7,0) -- (4.45,0);'
   '\\node at (-1.1,0) {CH$_3$};\\node at (4.85,0) {CH$_3$};'
   '\\node[font=\\small] at (.85,.45) {O};\\node[font=\\small] at (.85,-.45) {O};\\node[font=\\small] at (2.85,-.45) {O};\\node[font=\\small] at (2.85,.45) {O};'
   '\\draw[thick] (.97,-.45) -- (1.35,-.45);\\node[font=\\small] at (1.5,-.45) {H};'
   '\\draw[thick] (2.73,.45) -- (2.35,.45);\\node[font=\\small] at (2.2,.45) {H};'
   '\\draw[thick,dashed] (1.65,-.45) -- (2.72,-.45);\\draw[thick,dashed] (2.05,.45) -- (.97,.45);')
g=g.replace('\\draw[thick] (0,0) -- (.85,.45)--(.85,.45);','')
SK=tk(g)
d_ok='Dimer'
Q('0006','fiz','orta','şekilli','Dimer ve hidrojen bağı','Karboksilik asitlerin dimer yapısını ve hidrojen bağının fiziksel özelliklere etkisini yorumlar.',
  'Karboksilik asitler hem O–H hem de C=O içerdiğinden iki molekül arasında iki hidrojen bağı kurarak halka biçiminde dimer oluşturur; bu, kaynama noktasını ve suda çözünürlüğü etkiler.','Asit moleküllerinin saf hâlde hidrojen bağı yapmadığını sanmak.','etanoik asit dimeri',
  [A('Şekli yorumla','İki etanoik asit molekülü kesikli çizgilerle bağlanmıştır.','İki O–H···O hidrojen bağı'),A('Koşulu hatırla','Hidrojen bağı için H atomu O ya da N’ye bağlı olmalıdır.','Karboksilde O–H var'),A('Yargıları tara','Her yargıyı bu bilgiyle karşılaştır.','Kaynama noktası yüksek, suda çözünür'),A('Yanlışı bul','Saf asitte hidrojen bağı yoktur diyen ifade yanlıştır.','Yanlış yargı seçilir')],
  metin='Etanoik asit (CH₃COOH) buhar hâlinde ve apolar çözücülerde, iki molekülün birbirine kesikli çizgilerle bağlandığı dimer yapısında bulunur. Dimer yapısı şekilde gösterilmiştir.\nBuna göre etanoik asitle ilgili aşağıdaki yargılardan hangisi yanlıştır?',
  sekil=SK,istenen='Yanlış olan yargı.',ip=['Karboksil grubundaki hangi atomların hidrojen bağına katıldığını şekilden belirle.'],
  bilgi=[B('Karboksilik asitlerde hidrojen bağı','–COOH grubundaki O–H hidrojeni, başka bir karboksil grubunun C=O oksijenine bağlanır; böylece iki molekül arasında iki hidrojen bağı oluşur. Örnek: metanoik asit de aynı biçimde dimer yapar')],
  puf='Karboksil grubu aynı anda hidrojen bağı verici (O–H) ve alıcı (C=O) olduğundan asit molekülleri dimerleşir.',dogru=o['dogru'],yan=o['yan'],sira=o['sira'])

# ================= 07 · titrasyon grafiği · orta =================
Ka0=1e-5; C0=0.1; V0=20.0; Cb=0.1
def pH_ti(V):
    lo,hi=-14.0,1.0
    def f(lh):
        h=10**lh; kw=1e-14; ct=C0*V0/(V0+V); na=Cb*V/(V0+V)
        return na+h-kw/h-ct*Ka0/(Ka0+h)
    for _ in range(200):
        mid=(lo+hi)/2
        if f(mid)>0: hi=mid
        else: lo=mid
    return -(lo+hi)/2
assert abs(pH_ti(10)-5)<0.001 and abs(pH_ti(0)-3.0)<0.02 and 8.5<pH_ti(20)<9.0
xs=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,19.5,19.8,19.9,20,20.1,20.2,20.5,21,22,23,24,26,28,30,32,34,36,38,40]
coords=' '.join(f'({x},{pH_ti(x):.3f})' for x in xs)
SK=tk('''\\begin{axis}[width=7.6cm,height=6.2cm,xmin=0,xmax=40,ymin=0,ymax=14,xtick={0,10,20,30,40},ytick={0,1,2,3,4,5,6,7,8,9,10,11,12,13,14},tick label style={font=\\small},axis lines=left,grid=major,grid style={dotted,gray},
xlabel={Eklenen NaOH çözeltisi hacmi (mL)},ylabel={pH},xlabel style={font=\\small},ylabel style={font=\\small}]
\\addplot[thick,color=vurgu] coordinates {'''+coords+'''};
\\end{axis}''')
yan7=[('1·10⁻³','Başlangıçtaki pH değerini (3) Ka değeri sanmış; oysa pH = 3 olması [H⁺] = 10⁻³ M demektir, Ka değildir.','bilgi'),
      ('1·10⁻⁷','Eğrinin pH = 7’yi kestiği noktayı kullanmış; oysa Ka, yarı eşdeğerlik noktasındaki pH’den bulunur.','bilgi'),
      ('1·10⁻⁹','Eşdeğerlik noktasındaki pH değerini (yaklaşık 9) Ka sanmış; oysa Ka’yı yarı eşdeğerlik noktasındaki pH verir.','bilgi'),
      ('1·10⁻¹²','Eğrinin sonundaki pH değerini (yaklaşık 12) kullanmış; oysa bu bölge fazla NaOH’nin etkisini gösterir.','dikkat')]
Q('0007','asit','orta','grafik','Titrasyon eğrisi ve Ka','Zayıf asit–kuvvetli baz titrasyon eğrisinde yarı eşdeğerlik noktasından pKa ve Ka değerini bulur.',
  'Zayıf asit titrasyonunda yarı eşdeğerlik noktasında [HA] = [A⁻] olduğundan pH = pKa’dır; eşdeğerlik noktasının hacminin yarısındaki pH okunur.','Başlangıç, eşdeğerlik ya da nötr pH’yi Ka sanmak.','titrasyon eğrisi',
  [A('Eşdeğerlik hacmini bul','Eğrinin dikey sıçradığı hacim eşdeğerlik noktasıdır.','Eşdeğerlik noktası: 20 mL'),A('Yarı eşdeğerlik hacmini al','Asidin yarısı nötrleşmiştir.','20 mL ÷ 2 = 10 mL'),A('pH değerini oku','Bu noktada [HA] = [A⁻] olduğundan pH = pKa’dır.','10 mL’de pH = 5'),A('Ka’yı hesapla','Ka = 10 üzeri −pKa.','Ka = 1·10⁻⁵')],
  metin='Hacmi 20 mL olan, tek protonlu zayıf bir karboksilik asit çözeltisi 0,1 M NaOH çözeltisi ile titre ediliyor. Titrasyon sırasında çözeltinin pH değerinin eklenen NaOH çözeltisi hacmiyle değişimi şekildeki grafikte verilmiştir.\nBuna göre bu asidin Ka değeri kaçtır?',
  sekil=SK,istenen='Asidin Ka değeri.',ip=['Asidin tam yarısının nötrleştiği noktadaki pH değerinin ne anlama geldiğini düşün.'],
  bilgi=[B('Yarı eşdeğerlik noktası','Zayıf asit, yarısı kadar kuvvetli bazla nötrleştirildiğinde [HA] = [A⁻] olur. Henderson eşitliğinden pH = pKa bulunur. Örnek: bu noktada pH = 4 ise pKa = 4, Ka = 10⁻⁴ olur')],
  puf='Zayıf asit titrasyonunda eşdeğerlik hacminin yarısındaki pH, pKa’ya eşittir.',dogru='1·10⁻⁵',yan=yan7,sira=['1·10⁻¹²','1·10⁻⁹','1·10⁻⁷','1·10⁻⁵','1·10⁻³'])

# ================= 08 · tepkimeler · orta · düzenek · öncüllü =================
d=dict(I=(True,'Mg gibi aktif metaller karboksilik asitle tepkimeye girerek H₂ gazı açığa çıkarır; X tüpünde gaz çıkışı gözlenir'),
       II=(True,'karboksilik asitler NaHCO₃ ile tepkimeye girerek CO₂ gazı verir; Y tüpünde gaz çıkışı gözlenir'),
       III=(False,'ester NaHCO₃ ile tepkime vermez; Z tüpünde gaz çıkışı gözlenmez'))
o=OC(d,sr('Yalnız I','Yalnız II','Yalnız III','I ve II','I, II ve III')); assert o['dogru']=='I ve II'
tp=lambda x,y,ic:(f'\\draw[thick] ({x-.5},2.4) -- ({x-.5},.65) arc(180:360:.5) -- ({x+.5},2.4);\\fill[vurgu!15] ({x-.5},1.5) -- ({x-.5},.65) arc(180:360:.5) -- ({x+.5},1.5) -- cycle;'
                   f'\\draw[thick] ({x-.5},1.5) -- ({x+.5},1.5);\\node[font=\\small\\bfseries] at ({x},2.75) {{{y}}};'
                   f'\\node[font=\\footnotesize,align=center,text width=2.3cm] at ({x},-.45) {{{ic}}};')
mg='\\fill[gray] (-.05,1.9) -- (.12,1.9) -- (.28,.7) -- (.1,.7) -- cycle;\\node[font=\\scriptsize,anchor=south] at (.05,1.95) {Mg};'
SK=tk(tp(0,'X','\\ce{CH3COOH(aq)}')+mg.replace('(-.05,','(-.05,')+tp(2.6,'Y','\\ce{NaHCO3(aq)}\\\\+ \\ce{HCOOH(aq)}')+tp(5.2,'Z','\\ce{NaHCO3(aq)}\\\\+ \\ce{CH3COOC2H5(s)}'.replace('(s)','(l)')))
Q('0008','tep','orta','öncüllü','Asitlerin tepkimeleri','Karboksilik asitlerin aktif metal ve NaHCO₃ ile tepkimelerini, esterin NaHCO₃ ile tepkimeye girmediğini ayırt eder.',
  'Karboksilik asitler aktif metalle H₂, karbonatlı ve bikarbonatlı bileşiklerle CO₂ gazı verir; ester bu tepkimeleri vermez.','Esterin de asit gibi NaHCO₃’ten CO₂ çıkardığını sanmak.','X, Y, Z tüpleri',
  [A('X tüpünü incele','Aktif metal asitle H₂ verir.','Mg + CH₃COOH → H₂ ↑'),A('Y tüpünü incele','Karboksilik asit bikarbonatı ayrıştırır.','HCOOH + NaHCO₃ → CO₂ ↑'),A('Z tüpünü incele','Esterde asidik hidrojen yoktur.','Ester + NaHCO₃ → tepkime yok'),A('Sonucu yaz','Gaz çıkışı iki tüpte gözlenir.','X ve Y')],
  metin='Üç ayrı deney tüpüne şekilde gösterilen maddeler yeterli miktarda konulmuş ve oda sıcaklığında karıştırılmıştır.\nI. X tüpünde gaz çıkışı gözlenir.\nII. Y tüpünde gaz çıkışı gözlenir.\nIII. Z tüpünde gaz çıkışı gözlenir.\nBuna göre bu yargılardan hangileri doğrudur?',
  sekil=SK,istenen='Doğru olan yargılar.',ip=['Her tüpteki maddelerden hangisinin asit gibi davranabildiğini, hangisinin davranamadığını belirle.'],
  bilgi=[B('Asitlerin tepkimeleri','Karboksilik asit + aktif metal → karboksilat tuzu + H₂; karboksilik asit + NaHCO₃ → karboksilat tuzu + CO₂ + H₂O. Örnek: 2 C₂H₅COOH + Zn → (C₂H₅COO)₂Zn + H₂')],
  puf='Gaz çıkaran karboksilik asittir; ester NaHCO₃ ve aktif metalle tepkime vermez.',dogru=o['dogru'],yan=o['yan'],sira=o['sira'])

# ================= 09 · karışım hesabı · zor =================
Mac=2*12+4*1+2*16; Mfo=12+2*1+2*16; assert (Mac,Mfo)==(60,46)
a=Fr(1,10); b=Fr(1,10); assert a+b==Fr(2,10) and 60*a+46*b==Fr(106,10)
kac=60*a
Q('0009','asit','zor','hikâyeli','Karışımın nötrleşmesi','Asit karışımının toplam mol ve kütle verisinden her bileşenin kütlesini bulur.',
  'Her iki asit de tek protonlu olduğundan harcanan NaOH mol sayısı toplam asit molüne eşittir; toplam mol ve toplam kütle birlikte iki bilinmeyenli denklemi çözer.','Toplam mol sayısını tek bir asit sanmak ya da karışımı yarı yarıya bölmek.','CH₃COOH–HCOOH karışımı',
  [A('Toplam mol sayısını bul','Tek protonlu asitlerde nNaOH = n(asit toplamı).','n(CH₃COOH) + n(HCOOH) = 0,2 mol'),A('Mol kütlelerini hesapla','C=12, H=1, O=16 ile hesaplanır.','CH₃COOH = 60 · HCOOH = 46 g/mol'),A('Kütle denklemini kur','Toplam kütle 10,6 g’dır.','60 × x + 46 × y = 10,6'),A('Denklemleri çöz','Toplam moldan y = 0,2 − x yazılır.','14x = 1,4 → x = 0,1 mol'),A('Kütleyi bul','Kütle = mol × mol kütlesi.','0,1 × 60 = 6 g')],
  metin='Bir kireç çözücü örneğinde yalnızca etanoik asit (CH₃COOH) ve metanoik asit (HCOOH) bulunmaktadır. Bu örnekten alınan 10,6 g karışımın içindeki asitlerin tamamı nötrleşirken tam olarak 0,2 mol NaOH harcanıyor (H = 1, C = 12, O = 16).\nBuna göre karışımdaki CH₃COOH kütlesi kaç gramdır?',
  istenen='Karışımdaki CH₃COOH kütlesi (g).',ip=['Harcanan NaOH mol sayısı ile asitlerin toplam mol sayısı arasındaki ilişkiyi kur; bilinmeyenleri iki denklemle çöz.'],
  bilgi=[B('Nötrleşme ve mol ilişkisi','Tek protonlu bir asit, 1 mol NaOH ile nötrleşir; bu yüzden harcanan NaOH mol sayısı asitlerin toplam mol sayısına eşittir. Örnek: C₃H₇COOH’ın 0,3 molü 0,3 mol NaOH harcar')],
  puf='Karışım sorularında toplam mol ve toplam kütle için iki denklem kur.',dogru=kac,
  yan=[(Fr(46,10)*1,'HCOOH’nin kütlesini (0,1 × 46) bulmuş; oysa sorulan CH₃COOH’ın kütlesidir.','dikkat'),
       (Fr(106,20),'Karışımı eşit kütleli iki parçaya bölüp 10,6 ÷ 2 işlemiyle 5,3 g bulmuş.','islem'),
       (Fr(92,10),'0,2 molün tamamını HCOOH sanıp 0,2 × 46 işlemini yapmış.','islem'),
       (Fr(12),'0,2 molün tamamını CH₃COOH sanıp 0,2 × 60 işlemini yapmış.','islem')])

# ================= 10 · izomer sayısı · orta =================
asit_s,ester_s=asit_ester(4); assert (asit_s,ester_s)==(2,4)
nonbranch_ester=sum(1 for a_ in range(0,3) if 3-a_>=1)  # yalnız normal alkil: 3
Q('0010','sinif','orta','düz','Karboksilik asit ve ester izomerleri','Verilen molekül formülüne uyan karboksilik asit ve ester yapı izomerlerinin sayısını sistematik biçimde belirler.',
  'Bileşiğin karboksil/ester grubu iki oksijeni, C=O ise bir çift bağı karşılar; kalan karbonlar asit için tek alkil grubunda, ester için iki alkil grubu arasında dağıtılır, dallanma sayılır.','Dallı alkil gruplarını (izopropil gibi) ya da metanoat esterlerini unutmak.','C₄H₈O₂ izomerleri',
  [A('Sınıfları belirle','C₄H₈O₂ iki oksijenli, bir halka ya da çift bağlı eşdeğeridir.','Karboksilik asit ve ester'),A('Asitleri say','Karboksil karbonu dışındaki 3 karbon bir alkil grubu oluşturur.','Bütanoik asit, 2-metilpropanoik asit → 2'),A('Esterleri say','Karbonlar R ve R′ arasında paylaşılır.','R=H, R′=C₃ (2) · R=CH₃, R′=C₂ (1) · R=C₂, R′=CH₃ (1) → 4'),A('Toplamı yaz','Asit ve ester sayıları toplanır.','2 + 4 = 6')],
  metin='Molekül formülü C₄H₈O₂ olan bileşiklerden karboksilik asit ya da ester fonksiyonel grubunu içerenler dikkate alınacaktır.\nBuna göre bu bileşiklerin birbirinden farklı yapı izomerlerinin toplam sayısı kaçtır?',
  istenen='Karboksilik asit ve ester yapı izomerlerinin toplam sayısı.',ip=['Önce karboksilik asitleri, sonra esterleri ayrı ayrı say; esterlerde asit ve alkol kısmına düşen karbon sayılarının tüm dağılımlarını dene.'],
  bilgi=[B('Asit–ester izomerliği','Aynı molekül formüllü karboksilik asit ve ester birbirinin fonksiyonel grup izomeridir. Esterde R–COO–R′ yapısında R′ en az bir karbonlu olmalıdır. Örnek: C₂H₄O₂ için CH₃COOH ve HCOOCH₃ vardır')],
  puf='Esterde karbonları asit ve alkol kısmı arasında dağıt, dallı alkil gruplarını da say.',dogru=asit_s+ester_s,
  yan=[(asit_s,'Yalnız karboksilik asit izomerlerini saymış; oysa aynı formüllü esterler de vardır.','dikkat'),
       (nonbranch_ester,'Yalnız dallanmamış alkil gruplu esterleri (3) sayıp asitleri ve dallı yapıları katmamış.','bilgi'),
       (ester_s,'Yalnız esterleri saymış; oysa karboksilik asitler de aynı formüllüdür.','dikkat'),
       (asit_s+ester_s-1,'İzopropil metanoat gibi dallı alkil grubu taşıyan bir yapıyı atlamış.','dikkat')])

# ================= 11 · esterleşme denge hesabı · orta · tablo =================
Kc=Fr(4*4,2*2); assert Kc==4
x=Fr(4); assert x*x/((6-x)*(6-x))==Kc
SK=tablo_svg(['Madde','Denge anındaki mol'],[['CH₃COOH','2'],['CH₃CH₂OH','2'],['CH₃COOCH₂CH₃','4'],['H₂O','4']])
yan11=[(Fr(2),'Kc değerini ters yazıp (1/4) hesaplamış; oysa Kc ürünlerin çarpımının girenlerin çarpımına oranıdır.','bilgi'),
       (Fr(3),'Denge sabitini kullanmadan, girenlerin yarısının ürüne dönüştüğünü varsaymış.','bilgi'),
       (Fr(24,5),'Denge ifadesinde karekök almayı atlayıp ester oranını doğrudan 4 almış (x ÷ (6 − x) = 4).','islem'),
       (Fr(6),'Tepkimenin tam verimle girenlerin tamamını ürüne çevirdiğini sanmış.','bilgi')]
assert Fr(24,5)/(6-Fr(24,5))==4 and Fr(2)/(6-2)==Fr(1,2)==Fr(1,2) and Fr(2)*Fr(2)/((6-2)**2)==Fr(1,4)
Q('0011','est','orta','tablo','Esterleşme dengesi','Tablodaki denge molünden Kc değerini bulur ve aynı sıcaklıkta başka başlangıç koşulu için denge ester miktarını hesaplar.',
  'Esterleşmede mol sayısı değişmediğinden Kc, hacimden bağımsız olarak denge mollerinin oranıdır; Kc sabit sıcaklıkta aynı kalır.','Kc’yi ters yazmak ya da karekökü ihmal etmek.','CH₃COOH + CH₃CH₂OH ⇌ CH₃COOCH₂CH₃ + H₂O',
  [A('Kc’yi yaz','Giren ve ürün sayısı eşit olduğundan hacim sadeleşir.','Kc = (ester · su) ÷ (asit · alkol)'),A('Kc’yi hesapla','Tablodaki denge mollerini yerine koy.','(4 × 4) ÷ (2 × 2) = 4'),A('Yeni denge için x tanımla','Başlangıç 6 mol asit ve 6 mol alkol; x mol ester oluşur.','x × x ÷ (6 − x)² = 4'),A('x’i çöz','Her iki tarafın karekökü alınır.','x ÷ (6 − x) = 2 → x = 4 mol')],
  metin='Sabit sıcaklıkta kapalı bir kapta gerçekleşen CH₃COOH(s) + CH₃CH₂OH(s) ⇌ CH₃COOCH₂CH₃(s) + H₂O(s) tepkimesinin denge anındaki madde miktarları tabloda verilmiştir.\nAynı sıcaklıkta, eşit hacimli başka bir kapta 6 mol CH₃COOH ve 6 mol CH₃CH₂OH ile başlanıyor.\nBuna göre bu kapta denge kurulduğunda kaç mol ester bulunur?',
  sekil=SK,istenen='Yeni denge anındaki ester mol sayısı.',ip=['Önce tablodan denge sabitini hesapla; sonra yeni kapta oluşan ester miktarını x ile göster.'],
  bilgi=[B('Denge sabiti','aA + bB ⇌ cC + dD tepkimesinde Kc = [C]ᶜ[D]ᵈ ÷ [A]ᵃ[B]ᵇ ’dir ve yalnız sıcaklığa bağlıdır. Giren ve ürün katsayıları toplamı eşitse hacim sadeleşir. Örnek: A + B ⇌ C + D için denge molleri 1, 1, 3, 3 ise Kc = 9')],
  puf='Kc yalnız sıcaklığa bağlıdır; aynı sıcaklıkta Kc’yi koruyarak yeni dengeyi kur.',dogru=Fr(4),yan=yan11)

# ================= 12 · Le Chatelier · orta · öncüllü =================
d=dict(I=(True,'ürün olan H₂O uzaklaştırılınca denge ürünler yönüne kayar ve ester miktarı artar'),
       II=(False,'Kc yalnız sıcaklığa bağlıdır; alkol eklenmesi dengeyi ester yönüne kaydırır ama Kc değerini değiştirmez'),
       III=(False,'katalizör ileri ve geri tepkime hızını eşit oranda artırır; dengeye daha çabuk ulaşılır ama denge anındaki ester miktarı değişmez'))
o=OC(d,sr('Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III')); assert o['dogru']=='Yalnız I'
Q('0012','est','orta','öncüllü','Dengeyi etkileyen etmenler','Esterleşme dengesini Le Chatelier ilkesi, Kc’nin sıcaklığa bağlılığı ve katalizörün etkisiyle yorumlar.',
  'Ürün uzaklaştırılırsa denge ürün yönüne kayar; Kc yalnız sıcaklıkla, katalizör yalnız hızla ilgilidir ve denge konumunu değiştirmez.','Katalizörün ya da derişim değişiminin Kc’yi ve denge verimini değiştirdiğini sanmak.','esterleşme dengesi',
  [A('Tepkimeyi yaz','Esterleşme tersinir bir denge tepkimesidir.','Asit + alkol ⇌ ester + su'),A('I’i değerlendir','Ürün azalırsa denge ürünler yönüne kayar.','Su çıkarılır → ester artar → I doğru'),A('II’yi değerlendir','Derişim değişimi Kc’yi değiştirmez.','Kc yalnız sıcaklığa bağlı → II yanlış'),A('III’ü değerlendir','Katalizör denge konumunu değiştirmez.','Ester miktarı aynı kalır → III yanlış')],
  metin='Bir kimyager, derişik H₂SO₄ varlığında CH₃COOH(s) + CH₃OH(s) ⇌ CH₃COOCH₃(s) + H₂O(s) tepkimesini kapalı bir kapta yürüterek metil etanoat elde etmektedir. Tepkime sabit sıcaklıkta dengeye ulaşmıştır.\nI. Ortamdan H₂O uzaklaştırılırsa denge anındaki ester miktarı artar.\nII. Kaba CH₃OH eklenirse tepkimenin Kc değeri artar.\nIII. Kaba katalizör eklenirse denge anındaki ester miktarı artar.\nBuna göre bu yargılardan hangileri doğrudur?',
  istenen='Doğru olan yargılar.',ip=['Hangi değişikliğin yalnızca dengenin yönünü, hangisinin yalnızca hızı, hangisinin denge sabitini etkilediğini ayır.'],
  bilgi=[B('Dengeyi etkileyen etmenler','Derişim değişimi dengeyi kaydırır ama Kc’yi değiştirmez; Kc yalnız sıcaklıkla değişir. Katalizör iki yöndeki hızı eşit artırır ve denge konumunu etkilemez. Örnek: N₂ + 3H₂ ⇌ 2NH₃ dengesinde NH₃ çekilirse denge sağa kayar')],
  puf='Kc’yi yalnız sıcaklık, denge konumunu derişim ve sıcaklık değiştirir; katalizör hiçbirini değiştirmez.',dogru=o['dogru'],yan=o['yan'],sira=o['sira'])

# ================= 13 · verim · zor =================
n_as=Fr(18,60); n_al=Fr(23,46); Mest=4*12+8+2*16; assert Mest==88
assert n_as==Fr(3,10) and n_al==Fr(1,2) and n_as<n_al
teorik=n_as*Mest; dog13=teorik*Fr(3,4); assert dog13==Fr(198,10)
yan13=[(Fr(135,10),'Asit kütlesinin %75’ini (18 × 0,75) alıp ester kütlesi sanmış; oysa mol sayısı ester mol kütlesiyle çarpılmalıdır.','islem'),
       (teorik,'Verimi hesaba katmamış; %100 verimle oluşacak ester kütlesini (26,4 g) vermiş.','dikkat'),
       (n_al*Fr(3,4)*Mest,'Sınırlayıcı bileşeni alkol sanıp 0,5 mol alkol üzerinden %75 verimle hesaplamış.','bilgi'),
       (n_al*Mest,'Sınırlayıcı bileşeni alkol sanmış ve verimi hesaba katmamış.','bilgi')]
assert [yy[0] for yy in yan13]==[Fr(135,10),Fr(264,10),Fr(33),Fr(44)]
Q('0013','est','zor','hikâyeli','Esterleşmede sınırlayıcı bileşen ve verim','Esterleşme tepkimesinde sınırlayıcı bileşeni belirler ve verimi kullanarak ester kütlesini hesaplar.',
  'Esterleşmede girenler 1:1 mol oranında tepkimeye girer; az olan mol sınırlayıcıdır, teorik ürün miktarı onunla bulunur ve verimle çarpılır.','Sınırlayıcı bileşeni kütleye bakarak seçmek ya da verimi unutmak.','esterleşme verimi',
  [A('Mol sayılarını bul','Mol = kütle ÷ mol kütlesi.','Asit: 18 ÷ 60 = 0,3 · alkol: 23 ÷ 46 = 0,5'),A('Sınırlayıcıyı belirle','1:1 oranda az olan mol sınırlar.','CH₃COOH sınırlayıcı'),A('Teorik ester molünü bul','Teorik ürün sınırlayıcı kadardır.','0,3 mol ester'),A('Verimi uygula','Gerçek ürün = teorik × verim.','0,3 × 0,75 = 0,225 mol'),A('Kütleye çevir','Ester mol kütlesi 88 g/mol.','0,225 × 88 = 19,8 g')],
  metin='Bir laboratuvarda 18 g etanoik asit (CH₃COOH) ile 23 g etanol (CH₃CH₂OH), derişik H₂SO₄ katalizörlüğünde tepkimeye sokularak etil etanoat elde ediliyor. Tepkime sonunda verimin %75 olduğu belirleniyor (H = 1, C = 12, O = 16).\nBuna göre oluşan etil etanoatın kütlesi kaç gramdır?',
  istenen='Oluşan etil etanoat kütlesi (g).',ip=['İki girenin mol sayısını karşılaştırarak ürün miktarını belirleyen maddeyi bul; verimi en son uygula.'],
  bilgi=[B('Sınırlayıcı bileşen ve verim','Tepkimede önce biten madde ürün miktarını belirler. Verim = gerçek ürün ÷ teorik ürün × 100’dür. Örnek: 1:1 oranında tepkimeye giren A (2 mol) ve B (3 mol) için en çok 2 mol ürün oluşur')],
  puf='Önce sınırlayıcıyı bul, teorik ürünü hesapla, en sonda verimle çarp.',dogru=dog13,yan=yan13)

# ================= 14 · hidroliz · orta · şekil =================
dg='sodyum propanoat ve etanol'
yan14=[('propanoik asit ve etanol','Bazik ortamda oluşan ürünü serbest asit sanmış; oysa NaOH asidi nötrleştirir ve karboksilat tuzu oluşur.','bilgi'),
       ('sodyum etanoat ve 1-propanol','Asit ve alkol kısımlarının karbon sayılarını ters okumuş; oysa C=O taşıyan taraf üç karbonlu, oksijene bağlı taraf iki karbonlu zincirdir.','bilgi'),
       ('sodyum propanoat ve metanol','Alkol kısmını bir karbonlu okumuş; oysa oksijene bağlı alkil grubu etil grubudur.','dikkat'),
       ('sodyum etanoat ve etanol','Asit kısmını iki karbonlu saymış; oysa C=O taşıyan zincir üç karbonludur.','dikkat')]
SK=tk(sahne([(M_ET_PROP,'X')]))
Q('0014','est','orta','şekilli','Esterin bazik hidrolizi','İskelet formülü verilen esterin NaOH ile hidrolizinde oluşan karboksilat tuzunu ve alkolü belirler.',
  'Ester NaOH ile ısıtılınca asit kısmı karboksilat tuzuna, alkol kısmı alkole dönüşür; tepkime ısıtmayla tamamlanır.','Bazik ortamda serbest karboksilik asit oluştuğunu sanmak ya da asit ve alkol kısımlarının zincirlerini karıştırmak.','etil propanoat + NaOH',
  [A('Esteri çöz','–COO– grubunun C=O’lu tarafı asitten, oksijene bağlı tarafı alkolden gelir.','Asit kısmı: 3 C · alkol kısmı: 2 C'),A('Adları belirle','Asit kısmı propanoat, alkol kısmı etil grubudur.','Propanoat, etanol'),A('Bazik ortamı uygula','Asit kısmı NaOH ile karboksilat tuzu olur.','CH₃CH₂COONa'),A('Ürünleri yaz','Alkol kısmı ayrı ürün olarak çıkar.','Sodyum propanoat + etanol')],
  metin='Şekilde iskelet formülü verilen X esteri, yeterli miktarda NaOH çözeltisi ile ısıtılarak tamamen hidroliz ediliyor.\nBuna göre bu tepkimede oluşan ürünler aşağıdakilerden hangisidir?',
  sekil=SK,istenen='Hidroliz ürünleri.',ip=['Esterin C=O taşıyan tarafını asit kısmı, oksijene bağlı tarafını alkol kısmı olarak ayırıp NaOH ile ne olduğunu düşün.'],
  bilgi=[B('Esterin hidrolizi','Ester + NaOH → karboksilat tuzu + alkol (bazik hidroliz, tepkime tamamlanır). Asitli ortamda hidroliz tersinirdir ve karboksilik asit + alkol oluşur. Örnek: CH₃COOCH₃ + NaOH → CH₃COONa + CH₃OH')],
  puf='Bazik hidrolizde asit kısmı tuz (–COONa), alkol kısmı alkol olarak ayrılır.',dogru=dg,yan=yan14,sira=yer(dg,[y[0] for y in yan14],0))

# ================= 15 · ester şeması · zor · öncüllü · şekil =================
d=dict(I=(True,'Y, sodyum etanoattır; kuvvetli asit eklenince zayıf asit olan etanoik asit serbest kalır'),
       II=(True,'Z etanoldür; yeterli yükseltgenle yükseltgenirse etanoik asit oluşur ve bu, Y’den asitle elde edilen ürünle aynıdır'),
       III=(False,'X’in formülü C₄H₈O₂, Z’nin formülü C₂H₆O’dur; formülleri farklı olduğundan yapı izomeri değildirler'))
o=OC(d,sr('Yalnız I','Yalnız II','I ve II','I ve III','II ve III')); assert o['dogru']=='I ve II'
mx=draw(M_ET_ETA,0,0)
g=(mx+'\\node[font=\\small\\bfseries] at (1.0,-.95) {X};'
   f'\\draw[{ARR},thick] (3.2,.3) -- (6.3,.3) node[midway,above=2pt,font=\\footnotesize\\sffamily] {{NaOH(aq), ısı}};'
   '\\node[font=\\small\\bfseries] at (7.2,.3) {Y + Z};')
SK=tk(g)
Q('0015','est','zor','öncüllü','Esterin hidrolizi ve ürünlerin dönüşümü','Esterin bazik hidroliz ürünlerini bulur; tuzun asitlendirilmesi ve alkolün yükseltgenmesiyle aynı asitin oluştuğunu birleştirir.',
  'Ester, NaOH ile organik tuz ve alkol verir; tuz asitlendirilince karboksilik asit, birincil alkol yeterli yükseltgenle yükseltgenince yine karboksilik asit oluşur.','Tuzun asitlendirilince ne verdiğini ve alkolün yükseltgenme ürününü ilişkilendirememek.','etil etanoat şeması',
  [A('X’i çöz','Asit kısmı iki karbonlu, alkol kısmı etil grubudur.','X: etil etanoat, C₄H₈O₂'),A('Y ve Z’yi bul','NaOH ile tuz ve alkol oluşur.','Y: CH₃COONa · Z: CH₃CH₂OH'),A('I’i değerlendir','Tuz asitlendirilince asit oluşur.','CH₃COONa + HCl → CH₃COOH → I doğru'),A('II’yi değerlendir','Birincil alkolün yükseltgenmesi asit verir.','CH₃CH₂OH → CH₃COOH → II doğru'),A('III’ü değerlendir','Formülleri karşılaştır.','C₄H₈O₂ ≠ C₂H₆O → III yanlış')],
  metin='Şekilde iskelet formülü verilen X esteri, NaOH çözeltisiyle ısıtıldığında organik bir tuz olan Y ve bir alkol olan Z oluşturuyor.\nI. Y bileşiğinin sulu çözeltisine yeterli miktarda HCl eklenirse etanoik asit oluşur.\nII. Z bileşiği yeterli miktarda yükseltgenle yükseltgenirse, I’deki ürünle aynı bileşik oluşur.\nIII. X ile Z birbirinin yapı izomeridir.\nBuna göre bu yargılardan hangileri doğrudur?',
  sekil=SK,istenen='Doğru olan yargılar.',ip=['X’in asit ve alkol kısımlarını ayırıp Y ve Z’nin yapılarını yaz; sonra I ve II’deki dönüşümleri ayrı ayrı izle.'],
  bilgi=[B('Asit–alkol–ester dönüşümleri','Ester + NaOH → karboksilat tuzu + alkol. Karboksilat tuzu + güçlü asit → karboksilik asit. Birincil alkol yeterli yükseltgenle karboksilik aside kadar yükseltgenir. Örnek: CH₃CH₂COONa + HCl → CH₃CH₂COOH + NaCl')],
  puf='Esterin bazik hidrolizinden gelen tuz asitlendirilince, alkol de yükseltgenince karboksilik asit verir.',dogru=o['dogru'],yan=o['yan'],sira=o['sira'])

# ================= 16 · ayırt etme · zor · tablo =================
cand={'I':'CH₃CH₂COOH','II':'CH₃COOCH₃','III':'CH₂=CH–COOH'}
obs={'X':('II'),'Y':('I'),'Z':('III')}
SK=tablo_svg(['Madde','NaHCO₃(aq) ile','Br₂ çözeltisi ile','NaOH(aq) ile ısıtma'],
             [['X','gaz çıkışı yok','renk değişmez','tuz ve alkol oluşur'],['Y','gaz çıkışı var','renk değişmez','tuz ve su oluşur'],['Z','gaz çıkışı var','renk açılır','tuz ve su oluşur']])
dg16='II, I, III'
yan16=[('I, II, III','X’i propanoik asit, Y’yi ester sanmış; oysa X NaHCO₃ ile gaz vermediğinden asit olamaz, NaOH ile alkol verdiğinden estere aittir.','bilgi'),
       ('I, III, II','X’i asit sanıp Z’yi ester saymış; oysa Z NaHCO₃’ten gaz çıkardığı için asittir.','bilgi'),
       ('II, III, I','Doymuş ve doymamış asitleri ters yerleştirmiş; oysa rengi açan Z’nin C=C bağı taşıyan CH₂=CH–COOH olması gerekir.','bilgi'),
       ('III, I, II','Y’yi doymuş asit bulmuş ama X’i doymamış asit, Z’yi ester saymış; oysa X gaz vermez, Z gaz verir ve brom çözeltisinin rengini açar.','bilgi')]
Q('0016','tep','zor','tablo','Asit, ester ve doymamış asidi ayırt etme','Üç ayırt edici deney sonucunu birleştirerek karboksilik asit, ester ve doymamış karboksilik asidi belirler.',
  'NaHCO₃ ile gaz karboksilik asidi gösterir; Br₂ çözeltisinin renginin açılması C=C bağını, NaOH ile ısıtılınca tuz ve alkol oluşması esteri gösterir.','Tek bir deney sonucuna bakıp üç maddeyi ayırt etmeye çalışmak.','X, Y, Z maddeleri',
  [A('NaHCO₃ sonucunu oku','Gaz veren madde karboksil grubu taşır.','Y ve Z asit · X asit değil'),A('X’i belirle','Asit olmayan ve NaOH ile tuz ve alkol veren madde estere aittir.','X: CH₃COOCH₃'),A('Br₂ sonucunu oku','Rengi açan madde C=C içerir.','Z: CH₂=CH–COOH'),A('Kalanı eşleştir','Doymuş asit kalır.','Y: CH₃CH₂COOH')],
  metin='X, Y ve Z maddeleri I. CH₃CH₂COOH, II. CH₃COOCH₃ ve III. CH₂=CH–COOH bileşiklerinden birer tanesidir. Bu maddelerle yapılan üç deneyin sonuçları tabloda verilmiştir.\nBuna göre X, Y ve Z maddeleri sırasıyla aşağıdakilerden hangisinde doğru verilmiştir?',
  sekil=SK,istenen='X, Y ve Z’nin sırasıyla hangi bileşikler olduğu.',ip=['Tablodaki her deneyin hangi fonksiyonel grubu ya da bağı ortaya koyduğunu belirleyip adayları teker teker ele.'],
  bilgi=[B('Ayırt etme deneyleri','Karboksilik asit NaHCO₃’ten CO₂ çıkarır, ester çıkarmaz. Doymamış bileşik Br₂ çözeltisinin rengini açar, doymuş bileşik açmaz. Ester NaOH ile ısıtılınca tuz ve alkol verir. Örnek: CH₃COOH gaz verir ama Br₂’nin rengini değiştirmez')],
  puf='Gaz çıkışı asidi, renk açılması C=C bağını, tuz ve alkol oluşumu esteri gösterir.',dogru=dg16,yan=yan16,sira=['I, II, III',dg16,'I, III, II','II, III, I','III, I, II'])

# ================= 17 · sabun misel · orta · şekil · öncüllü =================
d=dict(I=(True,'1 ile gösterilen hidrokarbon zinciri apolardır; apolar yağ damlasına doğru yönelir ve London kuvvetleriyle etkileşir'),
       II=(False,'sabun zayıf asidin (karboksilik asit) tuzudur; suda çözününce eşlenik baz karboksilat iyonu su ile tepkimeye girip OH⁻ oluşturduğundan çözelti bazik olur'),
       III=(True,'sert sudaki Ca²⁺ ve Mg²⁺ iyonları sabunla çözünmeyen tuzlar oluşturur; bu yüzden sabunun temizleme gücü azalır'))
o=OC(d,sr('Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III')); assert o['dogru']=='I ve III'
import math as _m
mol=[]
for i in range(8):
    th=_m.radians(45*i); hx,hy=2.0*_m.cos(th),2.0*_m.sin(th); tx,ty=0.85*_m.cos(th),0.85*_m.sin(th)
    mol.append(f'\\draw[thick] ({tx:.3f},{ty:.3f}) -- ({hx-0.18*_m.cos(th):.3f},{hy-0.18*_m.sin(th):.3f});\\draw[thick,fill=vurgu!35] ({hx:.3f},{hy:.3f}) circle (0.18);')
g=('\\draw[thick,fill=gray!30] (0,0) circle (0.75);\\node[font=\\small] at (0,0) {yağ};'+''.join(mol)+
   '\\draw[-{Stealth},thin] (3.4,0.9) -- (1.55,0.08);\\node[font=\\small\\bfseries] at (3.65,0.95) {1};'
   '\\draw[-{Stealth},thin] (3.4,-.9) -- (2.2,0.03);\\node[font=\\small\\bfseries] at (3.65,-.95) {2};')
g=g.replace('(1.55,0.08)','(1.45,0.0)')
SK=tk(g)
Q('0017','sab','orta','öncüllü','Sabunun yapısı ve temizleme','Sabun molekülünün apolar kuyruk ve polar baş yapısını, sabun çözeltisinin bazikliğini ve sert suyun etkisini yorumlar.',
  'Sabun, yağ asidinin Na tuzudur: apolar hidrokarbon kuyruk yağa, iyonik karboksilat baş suya yönelir; çözeltisi bazik olur ve sert sudaki Ca²⁺, Mg²⁺ ile çözünmeyen tuz verir.','Sabun çözeltisini asidik sanmak ya da kuyruk ve başın etkileşimlerini ters yazmak.','sabun misel yapısı',
  [A('Şekli yorumla','Yağ damlasının çevresinde sabun molekülleri dizilmiştir.','1: kuyruk (içe), 2: baş (dışa)'),A('I’i değerlendir','Apolar kuyruk apolar yağla etkileşir.','1 apolar → I doğru'),A('II’yi değerlendir','Zayıf asit tuzu suda baziktir.','RCOO⁻ + H₂O ⇌ RCOOH + OH⁻ → II yanlış'),A('III’ü değerlendir','Ca²⁺ ile çözünmeyen tuz oluşur.','Temizleme gücü azalır → III doğru')],
  metin='Şekilde, bir yağ damlasının çevresinde sabun moleküllerinin oluşturduğu yapı gösterilmiştir. 1 ve 2 ile gösterilen kısımlar sabun molekülünün iki farklı ucudur.\nI. 1 ile gösterilen kısım apolardır ve yağ damlasıyla etkileşir.\nII. Sabunun sulu çözeltisi asidik özellik gösterir.\nIII. Sert suda sabunun temizleme gücü azalır.\nBuna göre bu yargılardan hangileri doğrudur?',
  sekil=SK,istenen='Doğru olan yargılar.',ip=['Sabun molekülünün hangi ucunun hidrokarbon zinciri, hangi ucunun iyonik grup olduğunu şekildeki yerleşimden çıkar.'],
  bilgi=[B('Sabunun yapısı','Sabun, uzun zincirli yağ asidinin sodyum (ya da potasyum) tuzudur: R–COO⁻Na⁺. Apolar R kısmı yağla, iyonik –COO⁻ kısmı suyla etkileşir. Örnek: C₁₇H₃₅COONa’da C₁₇H₃₅– kuyruk, –COO⁻ baştır')],
  puf='Sabunun kuyruğu yağa, başı suya yönelir; çözeltisi bazik, sert suda etkisi azdır.',dogru=o['dogru'],yan=o['yan'],sira=o['sira'])

# ================= 18 · sabunlaşma kütle · zor · tablo =================
Mtp=806; assert Mtp==51*12+98+6*16
nTG=Fr(806,10)/Mtp; assert nTG==Fr(1,10)
mNaOH=3*nTG*40; mGli=nTG*92; msab=Fr(806,10)+mNaOH-mGli
assert mNaOH==12 and mGli==Fr(92,10) and msab==Fr(834,10)
assert Fr(806,10)-mGli==Fr(714,10)
SK=tablo_svg(['Madde','Mol kütlesi (g/mol)'],[['Tripalmitin (yağ)','806'],['NaOH','40'],['Gliserol','92']])
yan18=[(Fr(806,10)-mGli,'NaOH’nin kütlesini hesaba katmamış; oysa sabun, yağ ile NaOH’nin toplam kütlesinden gliserolün çıkarılmasıyla bulunur.','dikkat'),
       (Fr(806,10)+nTG*40-mGli,'1 mol yağın 1 mol NaOH harcadığını varsaymış; oysa üç ester bağı için 3 mol NaOH gerekir.','bilgi'),
       (Fr(806,10)+mNaOH,'Oluşan gliserolün kütlesini çıkarmayı unutmuş.','dikkat'),
       (Fr(806,10)+mNaOH+mGli,'Gliserolü çıkarmak yerine eklemiş.','islem')]
Q('0018','sab','zor','tablo','Sabunlaşma ve kütlenin korunumu','Yağın NaOH ile sabunlaşmasında harcanan NaOH ve oluşan gliserolü mol ilişkisiyle bulup kütlenin korunumuyla sabun kütlesini hesaplar.',
  '1 mol yağ (trigliserit) 3 mol NaOH ile tepkimeye girip 3 mol sabun ve 1 mol gliserol verir; sabunun kütlesi kütlenin korunumundan bulunur.','NaOH mol sayısını 1 almak ya da gliserolü kütle denkliğinde unutmak.','tripalmitin sabunlaşması',
  [A('Yağın molünü bul','Mol = kütle ÷ mol kütlesi.','80,6 ÷ 806 = 0,1 mol'),A('NaOH’yi hesapla','Üç ester bağı için 3 mol NaOH gerekir.','0,1 × 3 = 0,3 mol → 12 g'),A('Gliserolü hesapla','1 mol yağdan 1 mol gliserol oluşur.','0,1 × 92 = 9,2 g'),A('Kütlenin korunumunu uygula','Girenlerin toplamı ürünlerin toplamına eşittir.','80,6 + 12 = sabun + 9,2'),A('Sabunu bul','Sabun kütlesi çıkarma ile bulunur.','92,6 − 9,2 = 83,4 g')],
  metin='Bir sabun üreticisi, mol kütlesi tabloda verilen tripalmitin yağının 80,6 gramını yeterli miktarda NaOH ile tam verimle sabunlaştırıyor. Tepkimede yalnızca sabun ve gliserol oluşmaktadır.\nBuna göre oluşan sabunun kütlesi kaç gramdır?',
  sekil=SK,istenen='Oluşan sabunun kütlesi (g).',ip=['Yağın mol sayısından yararlanıp tepkimeye giren NaOH’nin ve oluşan gliserolün kütlelerini ayrı ayrı bul; sonra kütlenin korunumunu kullan.'],
  bilgi=[B('Sabunlaşma','Yağ (trigliserit) + 3 NaOH → 3 sabun + gliserol. Tepkimede kütle korunur. Örnek: 1 mol triester yağ 3 mol NaOH harcar ve 1 mol gliserol (C₃H₅(OH)₃) açığa çıkarır')],
  puf='Sabunlaşmada yağın her molü 3 mol NaOH harcar ve 1 mol gliserol verir.',dogru=msab,yan=yan18)

# ================= 19 · yağ asitleri · orta · şekil · öncüllü =================
d=dict(I=(True,'A’da C=C bağı yoktur (doymuş), B’de bir C=C bağı vardır (doymamış)'),
       II=(True,'B’deki cis çift bağ zincirde kıvrım oluşturur; moleküller sıkı paketlenemez, London kuvvetleri zayıflar ve erime noktası düşer'),
       III=(True,'ikisi de 18 karbonlu düz zincirlidir; B’nin C=C bağına 1 mol H₂ katılınca A elde edilir'))
o=OC(d,sr('Yalnız I','Yalnız II','I ve II','II ve III','I, II ve III')); assert o['dogru']=='I, II ve III'
A_=yagasit(18); B_=yagasit(18,9)
scl=0.42
def sahne2(rows,sc):
    out=[]; y=0.0
    for spec,et in rows:
        out.append(draw(spec,0.9,y,sc,'\\footnotesize',0.13)); out.append(f'\\node[font=\\small\\bfseries] at (-.2,{y-0.1:.3f}) {{{et}}};'); y-=1.7
    return '\n'.join(out)
SK=tk(sahne2([(A_,'A'),(B_,'B')],scl))
Q('0019','yag','orta','öncüllü','Doymuş ve doymamış yağ asitleri','Doymuş ve doymamış yağ asitlerinin yapı, erime noktası ve hidrojenleme ilişkisini yorumlar.',
  'Doymamış yağ asidinde cis çift bağ zincirde kıvrım yapar, moleküller zayıf London kuvvetleriyle bağlandığından erime noktası düşer; hidrojenleme aynı karbon sayılı doymuş yağ asidini verir.','Doymamış yağ asitlerinin erime noktasının doymuşlardan yüksek olduğunu sanmak.','A ve B yağ asitleri',
  [A('Çift bağları say','A’da yok, B’de bir tane var.','A doymuş, B doymamış → I doğru'),A('Erime noktasını yorumla','Cis çift bağ zinciri büker.','B’nin erime noktası düşük → II doğru'),A('Karbon sayılarını karşılaştır','İkisinin de zinciri 18 karbonludur.','Aynı iskelet'),A('Hidrojenlemeyi yorumla','C=C’ye H₂ katılınca tek bağ olur.','B + H₂ → A → III doğru')],
  metin='Şekilde iskelet formülleri verilen A ve B yağ asitleri aynı sayıda karbon atomu içermektedir; köşe ve uç noktalarda karbon bulunur. B’nin zincirindeki çift bağ cis düzenlidir.\nI. A doymuş, B doymamış yağ asididir.\nII. B’nin erime noktası A’nınkinden düşüktür.\nIII. B’ye katalizör varlığında H₂ katılırsa A oluşur.\nBuna göre bu yargılardan hangileri doğrudur?',
  sekil=SK,istenen='Doğru olan yargılar.',ip=['Çift bağın zincirin şeklini nasıl değiştirdiğini ve bunun moleküller arası çekimi nasıl etkilediğini düşün.'],
  bilgi=[B('Yağ asitleri','Yağ asitleri uzun zincirli karboksilik asitlerdir. Doymuş olanlarda yalnız tek bağ, doymamış olanlarda C=C vardır. Cis çift bağ zinciri büker ve erime noktasını düşürür; hidrojenleme doymamışı doymuşa çevirir. Örnek: bitkisel yağlar doymamış yağ asidi bakımından zengindir')],
  puf='Doymamış yağ asidi kıvrık olduğundan erime noktası düşüktür; hidrojenleme onu doymuşa çevirir.',dogru=o['dogru'],yan=o['yan'],sira=o['sira'])

# ================= 20 · hidrojenleme · zor · şekil =================
nTG2=Fr(884,10)/MTG; assert nTG2==Fr(1,10)
ndb=3  # şekildeki C=C sayısı
assert sum(1 for sp in [OLE]*3 for x in sp if x[4]==2 and x[3] is None)==3
mH=nTG2*ndb*2; dg20=Fr(884,10)+mH; assert dg20==Fr(89)
yan20=[(Fr(884,10),'Hidrojenleme sonunda kütlenin değişmediğini sanmış; oysa katılan H₂ kütleyi artırır.','bilgi'),
       (Fr(884,10)+nTG2*1*2,'Yalnız bir çift bağın hidrojenlendiğini kabul etmiş; oysa trigliseritte üç yağ asidi zincirinin her birinde bir C=C vardır.','dikkat'),
       (Fr(884,10)+nTG2*ndb*1,'H₂ yerine H atomunun kütlesini (1 g/mol) kullanmış.','islem'),
       (Fr(884,10)+nTG2*(ndb+3)*2,'Üç ester C=O bağını da hidrojenlenebilir sayıp 6 mol H₂ harcamış; oysa Ni katalizörüyle yalnız C=C bağları doyurulur.','bilgi')]
assert [y[0] for y in yan20]==[Fr(884,10),Fr(886,10),Fr(887,10),Fr(896,10)]
tg=''
for i,yy in enumerate([2.6,1.3,0.0]):
    tg+=draw(OLE,0.9,yy,0.40,'\\footnotesize',0.12)+f'\n\\draw[thick] (0.2,{yy:.2f}) -- (0.9-0.12+0.0,{yy:.2f});'
tg+='\n\\draw[thick] (0.2,0) -- (0.2,2.6);'
SK=tk(tg)
Q('0020','yag','zor','şekilli','Yağın hidrojenlenmesi','Şekilde verilen trigliseritteki C=C sayısından harcanan H₂ miktarını ve hidrojenleme ürününün kütlesini hesaplar.',
  'Hidrojenleme yalnız C=C bağlarına H₂ katar; her C=C için 1 mol H₂ harcanır, ester C=O bağları etkilenmez ve ürün kütlesi başlangıç kütlesi ile eklenen H₂ kütlesinin toplamıdır.','Ester C=O bağlarını da hidrojenlenebilir saymak ya da kütle artışını unutmak.','triolein hidrojenlenmesi',
  [A('Çift bağları say','Her yağ asidi zincirinde bir C=C vardır.','3 C=C → 3 mol H₂ / mol yağ'),A('Yağın molünü bul','Mol = kütle ÷ mol kütlesi.','88,4 ÷ 884 = 0,1 mol'),A('Harcanan H₂’yi hesapla','Her C=C bağına 1 mol H₂ katılır.','0,1 × 3 = 0,3 mol'),A('H₂ kütlesini bul','H₂ mol kütlesi 2 g/mol.','0,3 × 2 = 0,6 g'),A('Ürün kütlesini yaz','Kütle korunur, H₂ eklenir.','88,4 + 0,6 = 89 g')],
  metin='Şekilde yapısı gösterilen trigliserit (mol kütlesi 884 g/mol) için köşe ve uç noktalarda karbon bulunur; karbona bağlı hidrojenler yazılmamıştır. Bu trigliseritten 88,4 gramı, Ni katalizörü ve yeterli H₂ ile tamamen doymuş hâle getiriliyor ve katı yağ elde ediliyor (H = 1).\nBuna göre oluşan katı yağın kütlesi kaç gramdır?',
  sekil=SK,istenen='Hidrojenleme sonunda oluşan katı yağın kütlesi (g).',ip=['Şekilde zincirlerdeki C=C bağlarını sayarak yağın bir molünün kaç mol H₂ bağlayacağını bul.'],
  bilgi=[B('Yağların hidrojenlenmesi','Doymamış yağ, Ni katalizörüyle H₂ ile tepkimeye girince C=C bağları tek bağa dönüşür ve sıvı yağ katı yağa çevrilir. Her C=C için 1 mol H₂ gerekir. Örnek: 2 C=C içeren 1 mol yağ 2 mol H₂ bağlar')],
  puf='Hidrojenlemede yalnız C=C bağları H₂ bağlar; ürün kütlesi = yağ kütlesi + bağlanan H₂ kütlesi.',dogru=dg20,yan=yan20)

# ---------- yaz ----------
for x_ in P.ANA: x_['kardes']=None
SCR=os.environ.get('SCRATCH','/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/kar')
os.makedirs(SCR,exist_ok=True)
P.yaz(os.path.join(GD,'karboksil-1.json'),os.path.join(SCR,'bos-karboksil.json'))
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=KEY))['kartlar'].append(c['id'])
json.dump(dict(konu=KONU_AD,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2018–2026 Kimya, MEB 12. sınıf Organik Bileşikler.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','akkarboksil.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
