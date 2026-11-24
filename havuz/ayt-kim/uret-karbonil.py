"""AYT Kimya · Karbonil Bileşikleri (Aldehit ve Keton) · 20 soru. Kardeş yok, ipucu 1.
Yapılar tek bir atom listesinden hem çizilir hem çözümlenir; izomer sayıları ve hesaplar kaba kuvvet/Fraction ile doğrulanır."""
import sys,os,json,math
from fractions import Fraction as Fr
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-kim'))
import _hafif_kim2 as H
from _hafif_kim2 import *
from _hafif_kim import onc,tek,etk
import networkx as nx
KONU_AD='Karbonil Bileşikleri (Aldehit ve Keton)'; KEY='akim|Karbonil Bileşikleri (Aldehit ve Keton)'
P=Parti('karbonil',KONU_AD,KEY,ders='AYT Kimya',idon='aytkim'); H.KONU=KONU_AD
KAYNAK='ÖSYM AYT 2018–2026 Kimya karbonil bileşikleri soruları (yalnız mantık) · MEB 12. sınıf Organik Bileşikler'
def kartla(no,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(f'K-AKKRB-{no}',alt,fikir,tuzak,z,kalip,adim,tipId,tip,KAYNAK)
TIP={'ad':('kr-adlandirma','Aldehit ve keton adlandırma'),'sinif':('kr-sinif','Karbonil grubu ve sınıflandırma'),'elde':('kr-elde','Elde edilme (alkol yükseltgenmesi, alkin hidrasyonu)'),
     'tep':('kr-tepkime','Yükseltgenme–indirgenme tepkimeleri'),'ayirt':('kr-tollens','Tollens ve Fehling ayıraçları'),'izo':('kr-izomer','İzomerlik'),'fiz':('kr-fiziksel','Fiziksel özellikler')}
def Q(no,tp,z,kalip,alt,kaz,fikir,tuzak,ozet,ad,**k):
    t,tn=TIP[tp]; kartla(no[-2:],alt,fikir,tuzak,z,kalip,len(ad),t,tn)
    assert len(k['ip'])==1; mk(P,no,ad=ad,adim=len(ad),tipId=t,tip=tn,z=z,alt=alt,kaz=kaz,kalip=kalip,kart=f'K-AKKRB-{no[-2:]} ({ozet})',**k)
def yer(dogru,digerler,i): return list(digerler[:i])+[dogru]+list(digerler[i:])
ORD=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
def OC(d,sira): return onc(d,[tuple(x for x in t.replace('Yalnız ','').replace(',',' ').replace(' ve ',' ').split()) for t in sira])
def sr(*k): assert [x for x in ORD if x in k]==list(k),k; return list(k)
# ---------- yapı modeli: (ad, ebeveyn, açı°, etiket, çift?) ----------
SC=0.8
def coords(spec):
    c={}
    for s in spec:
        n,p,a=s[0],s[1],s[2]
        c[n]=(0.0,0.0) if p is None else (c[p][0]+math.cos(math.radians(a)),c[p][1]+math.sin(math.radians(a)))
    return c
def graf(spec):
    G_=nx.Graph(); lab={}; ordr={}
    for s in spec:
        n,p,a,l=s[:4]; dbl=len(s)>4 and s[4]; G_.add_node(n); lab[n]=l
        if p is not None: G_.add_edge(n,p); ordr[frozenset((n,p))]=2 if dbl else 1
    return G_,lab,ordr
def formul(spec):
    G_,lab,od=graf(spec); C=sum(1 for n in lab if lab[n] is None); O=sum(1 for n in lab if lab[n] in('OH','HO','O'))
    Hs=0
    for n in lab:
        if lab[n] is None:
            val=sum(od[frozenset((n,m))] for m in G_[n]); assert val<=4,(n,val); Hs+=4-val
        elif lab[n] in('OH','HO','H'): Hs+=1
    return C,Hs,O
def sinif(spec):
    G_,lab,od=graf(spec); r=[]
    for n in lab:
        if lab[n]=='O':
            (c,)=list(G_[n]); assert od[frozenset((n,c))]==2
            hn=sum(1 for m in G_[c] if lab[m]=='H'); cn=sum(1 for m in G_[c] if lab[m] is None)
            r.append('ald' if hn==1 and cn<=1 else ('ket' if hn==0 and cn==2 else 'x'))
    assert len(r)==1 and r[0]!='x'; return r[0]
def mol_ciz(spec,ox,oy):
    c=coords(spec); g=[]; P_={s[0]:(ox+SC*c[s[0]][0],oy+SC*c[s[0]][1]) for s in spec}; lb={s[0]:s[3] for s in spec}
    xs=[];ys=[]
    for n,(x,y) in P_.items():
        xs.append(x);ys.append(y)
        if lb[n]: xs+=[x-.3,x+.3]; ys+=[y-.25,y+.25]
    sh=lambda l:0 if not l else (.2 if len(l)==1 else .36)
    for s in spec:
        n,p,a,l=s[:4]
        if p is None: continue
        dbl=len(s)>4 and s[4]; (x1,y1),(x2,y2)=P_[p],P_[n]
        d=math.hypot(x2-x1,y2-y1); ux,uy=(x2-x1)/d,(y2-y1)/d; px,py=-uy,ux
        a1=sh(lb[p])*SC/0.8*0+sh(lb[p]); a2=sh(l)
        offs=[-.045,.045] if dbl else [0]
        for o_ in offs:
            g.append(f'\\draw[thick] ({x1+ux*a1+px*o_:.3f},{y1+uy*a1+py*o_:.3f}) -- ({x2-ux*a2+px*o_:.3f},{y2-uy*a2+py*o_:.3f});')
    for n,(x,y) in P_.items():
        if lb[n]: g.append(f'\\node[inner sep=0pt,font=\\small] at ({x:.3f},{y:.3f}) {{{lb[n]}}};')
    return '\n'.join(g),(min(xs),max(xs),min(ys),max(ys))
def sahne(satir,bosluk=1.0):
    out=[]; x=0.0; parts=[]
    for spec,et in satir:
        c=coords(spec); w=[SC*c[s[0]][0] for s in spec]; ox=x-min(w)+.4
        g,bb=mol_ciz(spec,ox,0); parts.append((g,bb,et)); x=bb[1]+bosluk
    ybot=min(p[1][2] for p in parts)
    for g,bb,et in parts:
        out.append(g)
        if et: out.append(f'\\node[font=\\small\\bfseries] at ({(bb[0]+bb[1])/2:.3f},{ybot-.5:.3f}) {{{et}}};')
    return '\n'.join(out)
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'; TAIL='\n\\end{tikzpicture}'
ARR='-{Stealth[length=2.2mm,width=2mm]}'
def tk(g): return tikz_svg(HEAD+g+TAIL)
def ALD(chain_o_h=None): pass
# ---- yapılar ----
M_3MB=[('c1',None,0,None),('c2','c1',30,None),('c3','c2',-30,None),('m','c3',-90,None),('c4','c3',30,None),('o','c1',90,'O',True),('h','c1',210,'H')]          # 3-metilbütanal
M_BUTAL=[('c1',None,0,None),('c2','c1',30,None),('c3','c2',-30,None),('c4','c3',30,None),('o','c1',90,'O',True),('h','c1',210,'H')]                              # bütanal
M_2MPAL=[('c1',None,0,None),('c2','c1',30,None),('m','c2',90,None),('c3','c2',-30,None),('o','c1',90,'O',True),('h','c1',210,'H')]                                # 2-metilpropanal
M_PRPAL=[('c1',None,0,None),('c2','c1',30,None),('c3','c2',-30,None),('o','c1',90,'O',True),('h','c1',210,'H')]                                                   # propanal
M_2M3P=[('c1',None,0,None),('c2','c1',30,None),('m','c2',90,None),('c3','c2',-30,None),('o','c3',-90,'O',True),('c4','c3',30,None),('c5','c4',-30,None)]          # 2-metil-3-pentanon
M_2PNON=[('c1',None,0,None),('c2','c1',30,None),('o','c2',90,'O',True),('c3','c2',-30,None),('c4','c3',30,None),('c5','c4',-30,None)]                              # 2-pentanon
M_3PNON=[('c1',None,0,None),('c2','c1',30,None),('c3','c2',-30,None),('o','c3',-90,'O',True),('c4','c3',30,None),('c5','c4',-30,None)]                             # 3-pentanon
M_BUTNON=[('c1',None,0,None),('c2','c1',30,None),('o','c2',90,'O',True),('c3','c2',-30,None),('c4','c3',30,None)]                                                  # bütanon
M_3M2B=[('c1',None,0,None),('c2','c1',30,None),('o','c2',90,'O',True),('c3','c2',-30,None),('m','c3',-90,None),('c4','c3',30,None)]                                # 3-metil-2-bütanon
M_PENTAL=[('c1',None,0,None),('c2','c1',30,None),('c3','c2',-30,None),('c4','c3',30,None),('c5','c4',-30,None),('o','c1',90,'O',True),('h','c1',210,'H')]
M_NEOP=[('c1',None,0,None),('c2','c1',30,None),('m1','c2',90,None),('m2','c2',-30,None),('m3','c2',150,None),('o','c1',-90,'O',True),('h','c1',210,'H')]           # 2,2-dimetilpropanal (çizim: m3 ters)
M_1P=[('o',None,0,'HO'),('c1','o',-30,None),('c2','c1',30,None),('c3','c2',-30,None)]
M_1B=[('o',None,0,'HO'),('c1','o',-30,None),('c2','c1',30,None),('c3','c2',-30,None),('c4','c3',30,None)]
M_2BUT=[('a',None,0,None),('b','a',30,None),('o','b',90,'OH'),('c','b',-30,None),('d','c',30,None)]
M_TBUT=[('c',None,0,None),('m1','c',180,None),('m2','c',0,None),('m3','c',-90,None),('o','c',90,'OH')]
M_2MP1=[('o',None,0,'HO'),('c1','o',-30,None),('c2','c1',30,None),('c3','c2',-30,None),('c4','c2',90,None)]
for sp,f,s in [(M_3MB,(5,10,1),'ald'),(M_BUTAL,(4,8,1),'ald'),(M_2MPAL,(4,8,1),'ald'),(M_PRPAL,(3,6,1),'ald'),(M_2M3P,(6,12,1),'ket'),(M_2PNON,(5,10,1),'ket'),(M_3PNON,(5,10,1),'ket'),
               (M_BUTNON,(4,8,1),'ket'),(M_3M2B,(5,10,1),'ket'),(M_NEOP,(5,10,1),'ald'),(M_PENTAL,(5,10,1),'ald')]:
    assert formul(sp)==f,(sp,formul(sp)); assert sinif(sp)==s
for sp,f in [(M_1P,(3,8,1)),(M_1B,(4,10,1)),(M_2BUT,(4,10,1)),(M_TBUT,(4,10,1)),(M_2MP1,(4,10,1))]: assert formul(sp)==f
# ---------- izomer sayımı (kaba kuvvet): CnH2nO karbonil izomerleri ----------
def karbonil_izo(n):
    bul=[]
    for T in nx.nonisomorphic_trees(n+1):
        for o in T.nodes:
            if T.degree(o)!=1: continue
            (c,)=list(T[o])
            if T.degree(c)>3: continue
            if any(T.degree(m)>4 for m in T.nodes if m not in(o,c)): continue
            Hh=T.copy(); nx.set_node_attributes(Hh,{m:('O' if m==o else 'C') for m in Hh.nodes},'t')
            if any(nx.is_isomorphic(Hh,B_,node_match=lambda a,b:a['t']==b['t']) for B_,_ in bul): continue
            bul.append((Hh,o))
    r={'ald':0,'ket':0}
    for Hh,o in bul:
        (c,)=list(Hh[o]); r['ald' if Hh.degree(c)==2 else 'ket']+=1
    return r
IZ={n:karbonil_izo(n) for n in (3,4,5,6)}
assert IZ[3]=={'ald':1,'ket':1} and IZ[4]=={'ald':2,'ket':1} and IZ[5]=={'ald':4,'ket':3},IZ
MK='Şekilde iskelet formülleri verilmiştir; karbonil grubu dışında köşeler ve uçlar karbon atomunu gösterir.'
AG=108
def tek2(sec,h):
    return tek([(a,b,(n if (not n or n.endswith('.')) else n+'.')) for a,b,n in sec],h)
# ================= 01 · adlandırma · kolay · şekil =================
dg='3-metilbütanal'
yan=[('2-metilbütanal','Zinciri karbonil karbonundan değil, karbonil karbonu en büyük numarayı alacak uçtan numaralamış; aldehit karbonu her zaman 1. karbondur.','bilgi'),
     ('3-metil-2-bütanon','Uçtaki –CHO grubunu keton karbonili sanmış; –CHO’daki karbona hidrojen bağlı olduğu için bileşik aldehittir.','bilgi'),
     ('3-metilbütanoik asit','Aldehit son ekini (-al) karboksilik asit son ekiyle (-oik asit) karıştırmış.','bilgi'),
     ('3-metil-1-bütanol','Karbonil grubunu hidroksil grubu sanıp alkol adı vermiş.','bilgi')]
SK=tk(sahne([(M_3MB,None)]))
Q('0001','ad','kolay','şekilli','Aldehit adlandırma','İskelet formülü verilen aldehiti IUPAC kurallarına göre adlandırır.',
  'Aldehitte ana zincir –CHO karbonunu içeren en uzun zincirdir; –CHO karbonu 1 numaralıdır ve ad “-al” ekiyle biter.','Numaralamayı –CHO karbonundan başlatmamak ya da aldehiti keton/alkol sanmak.','aldehit adlandırma',
  [A('Karbonil grubunu tanı','Karbonil karbonuna bir H bağlıysa bileşik aldehittir.','C=O + H → aldehit (-al)'),A('Ana zinciri seç','–CHO karbonunu içeren en uzun zinciri bul.','4 karbonlu zincir → bütanal'),A('Numaralandır','–CHO karbonu 1. karbon olur; dalın bağlı olduğu karbonun numarasını oku.','Metil 3. karbonda → 3-metil'),A('Adı yaz','Dal adı ve ana zincir adı birleştirilir.','3-metilbütanal')],
  metin='Şekilde yapısı gösterilen bileşik bir aldehittir; köşe ve uç noktalarında karbon atomu bulunur, karbonil grubundaki H ayrıca yazılmıştır.\nBu bileşiğin sistematik (IUPAC) adı aşağıdakilerden hangisidir?',
  sekil=SK,istenen='Bileşiğin IUPAC adı.',ip=['Önce –CHO grubunun karbonunu bul; numaralamayı bu karbondan başlat.'],
  bilgi=[B('Aldehit adlandırma','Aldehitlerde –CHO karbonu zincirin 1. karbonudur ve numaraya gerek yoktur; ad ana zincir adına “-al” eki getirilerek yazılır. Örnek: CH₃CH₂CHO için propanal; CH₃CH(CH₃)CHO için 2-metilpropanal')],
  puf='Aldehitte numaralama her zaman –CHO karbonundan başlar.',dogru=dg,yan=yan,sira=yer(dg,[y[0] for y in yan],2))

# ================= 02 · adlandırma · orta · şekil =================
dg='2-metil-3-pentanon'
yan=[('4-metil-3-pentanon','Karbonil iki uçtan da 3. karbonda kaldığı için eşitlik varken dalın küçük numara alacağı uçtan değil, etil ucundan numaralamış.','dikkat'),
     ('2-metil-3-pentanol','Karbonil grubunu hidroksil grubu sanıp alkol adı vermiş.','bilgi'),
     ('2-metilpentanal','Ketonu aldehit sanmış; karbonil karbonuna H bağlı olmadığı için bileşik ketondur.','bilgi'),
     ('3-metil-2-pentanon','Karbonilin konumunu 2, metilin konumunu 3 almış; oysa karbonil zincirin ortasındaki 3. karbondadır.','dikkat')]
SK=tk(sahne([(M_2M3P,None)]))
Q('0002','ad','orta','şekilli','Keton adlandırma','İskelet formülü verilen ketonu karbonil ve dal konumlarına göre adlandırır.',
  'Ketonda zincir karbonile en yakın uçtan numaralanır; karbonil iki uçtan eşit uzaklıktaysa dal küçük numara alacak uçtan sayılır.','Numaralamada karbonil eşitliğini bozan dalı hesaba katmamak.','keton adlandırma',
  [A('Ana zinciri seç','Karbonil karbonunu içeren en uzun zinciri bul.','5 karbon → pentanon'),A('Karbonilin konumu','Karbonil karbonu iki uçtan da 3. sıradadır.','Eşitlik var: 3-pentanon'),A('Dalı küçük numaraya yerleştir','Eşitlikte dalın küçük numara alacağı uçtan say.','Metil 2. karbon'),A('Adı yaz','Dal ve karbonil konumu birleştirilir.','2-metil-3-pentanon')],
  metin='Aşağıdaki şekilde iskelet formülü gösterilen bileşik bir ketondur.\nBu ketonun sistematik (IUPAC) adı aşağıdakilerden hangisidir?',
  sekil=SK,istenen='Bileşiğin IUPAC adı.',ip=['Karbonil karbonunun zincirde iki uçtan da kaçıncı sırada olduğuna bak; eşitlik varsa dalı hesaba kat.'],
  bilgi=[B('Keton adlandırma','Ketonlarda ana zincir karbonil karbonunu içerir; zincir karbonil karbonuna en küçük numara gelecek uçtan numaralanır ve ad “-on” ekiyle biter. Örnek: CH₃COCH₂CH₂CH₃ için 2-pentanon')],
  puf='Ketonda önce karbonile, eşitlik varsa dala küçük numara ver.',dogru=dg,yan=yan,sira=yer(dg,[y[0] for y in yan],0))

# ================= 03 · Tollens · kolay · düz =================
sec=[('CH₃COCH₃',False,'aseton bir ketondur; keton Tollens ayıracını indirgemez, ayna oluşmaz'),('CH₃CH₂CHO',True,''),('CH₃CH₂OH',False,'etanol alkoldür ve ılımlı koşullarda Tollens ayıracıyla tepkime vermez'),
     ('CH₃CH₂COCH₃',False,'bütanon bir ketondur; ketonlar gümüş aynası oluşturmaz'),('CH₃OCH₂CH₃',False,'eterler Tollens ayıracıyla tepkime vermez')]
o=tek2(sec,True)
Q('0003','ayirt','kolay','düz','Tollens ayıracı','Tollens ayıracı ile aldehit ve ketonu ayırt eder.',
  'Tollens ayıracı (amonyaklı AgNO₃) yalnız aldehitlerle tepkimeye girer; Ag⁺ iyonları Ag katısına indirgenerek kabın çeperinde ayna oluşturur.','Ketonun da aldehit gibi gümüş aynası verdiğini sanmak.','Tollens testi',
  [A('Testin ilkesi','Tollens ayıracı yalnız aldehit grubunu yükseltger ve kendisi gümüşe indirgenir.','–CHO + Ag⁺ → –COOH + Ag'),A('Bileşikleri sınıflandır','Her formülde karbonil grubunun yerine bak.','Keton: R–CO–R · aldehit: R–CHO'),A('Alkol ve eteri ele','Bu iki grup Tollens ayıracıyla tepkime vermez.','CH₃CH₂OH, CH₃OCH₂CH₃ → tepkime yok'),A('Sonuç','Yalnız CH₃CH₂CHO aldehittir.','CH₃CH₂CHO')],
  metin='Amonyaklı gümüş nitrat çözeltisi (Tollens ayıracı) ile hafifçe ısıtılan bir organik bileşik, deney tüpünün çeperinde parlak bir gümüş tabakası oluşturuyor.\nBuna göre bu bileşik aşağıdakilerden hangisi olabilir?',
  istenen='Gümüş aynası veren bileşik.',ip=['Hangi fonksiyonel grubun Tollens ayıracını indirgeyebildiğini düşün.'],
  bilgi=[B('Tollens testi','Tollens ayıracı Ag(NH₃)₂⁺ iyonu içerir. Aldehit yükseltgenip karboksilik asit olurken Ag⁺ iyonu Ag metaline indirgenir ve tüpün çeperinde ayna oluşur. Örnek: propanal ile gümüş aynası görülür, propanon ile görülmez')],
  puf='Ayıraçlar karbonil bileşiklerini fonksiyonel gruplarına göre ayırt eder.',dogru=o['dogru'],yan=o['yan'],sira=yer('CH₃CH₂CHO',[s[0] for s in sec if not s[1]],3))

# ================= 04 · sınıflandırma · kolay · şekil · öncüllü =================
SK=tk(sahne([(M_BUTAL,'A'),(M_2PNON,'B'),(M_1P,'C')]))
d=dict(I=(True,'A’da karbonil karbonuna bir hidrojen atomu bağlıdır, yani A aldehittir'),
       II=(False,'B’de karbonil karbonuna hidrojen değil iki karbon atomu bağlıdır; hidrojen bağlı olsaydı aldehit olurdu'),
       III=(True,'C yalnız –OH grubu taşır, C=O grubu içermez; C bir alkoldür'))
o=OC(d,sr('Yalnız I','Yalnız III','I ve II','I ve III','I, II ve III')); assert o['dogru']=='I ve III'
Q('0004','sinif','kolay','öncüllü','Karbonil grubu ve sınıflandırma','Yapı formülünden bileşiğin aldehit, keton ya da alkol olduğunu belirler.',
  'Karbonil karbonuna H bağlıysa aldehit, iki karbon bağlıysa keton; yalnız –OH varsa alkoldür.','Karbonil karbonuna bağlı atomlara bakmadan uçtaki karbonu aldehit saymak.','A, B, C yapıları',
  [A('A’yı incele','C=O karbonunda bir H var.','A: aldehit → I doğru'),A('B’yi incele','C=O karbonu iki karbona bağlı.','B: keton → II yanlış'),A('C’yi incele','Yalnız –OH grubu var, C=O yok.','C: alkol → III doğru'),A('Sonuç','I ve III doğrudur.',etk(d))],
  metin=MK+'\nBuna göre,\nI. A bir aldehittir.\nII. B’nin karbonil karbonuna bir hidrojen atomu bağlıdır.\nIII. C karbonil grubu içermez.\nyargılarından hangileri doğrudur?',
  sekil=SK,istenen='Doğru olan yargılar.',ip=['Her yapıda C=O grubu olup olmadığına ve varsa bu karbona bağlı atomlara bak.'],
  bilgi=[B('Aldehit ve keton','Karbonil grubu (C=O) karbonuna bir H ve bir C ya da iki H bağlıysa bileşik aldehit, iki C bağlıysa keton olur. Örnek: CH₃CH₂CHO aldehit, CH₃COCH₃ ise ketondur')],
  puf='Karbonil karbonunda H varsa aldehit, iki karbon varsa keton.',dogru=o['dogru'],yan=o['yan'],sira=o['sira'])

# ================= 05 · elde edilme · orta · şema · öncüllü =================
assert formul([('a',None,0,None)])[0]==1
C3H8O=(3,8,1); C3H6O=(C3H8O[0],C3H8O[1]-2,1); C3H6O2=(C3H6O[0],C3H6O[1],C3H6O[2]+1)
assert C3H6O2==(3,6,2)
g=(r'\node (s) at (0,0) {\ce{CH3CH2CH2OH}};'
   r'\node[draw,thick,rounded corners=3pt,minimum width=.9cm,minimum height=.8cm] (a) at (4.9,0) {\textbf{A}};'
   r'\node[draw,thick,rounded corners=3pt,minimum width=.9cm,minimum height=.8cm] (b) at (8.6,0) {\textbf{B}};'
   f'\\draw[{ARR},thick] (s.east)+(.1,0) -- (a.west) node[midway,above=2pt,font=\\footnotesize,align=center] {{ılımlı\\\\yükseltgen}};'
   f'\\draw[{ARR},thick] (a.east) -- (b.west) node[midway,above=2pt,font=\\footnotesize,align=center] {{yükseltgen}};')
SK=tk(g)
d=dict(I=(True,'1-propanol primer alkoldür ve ılımlı yükseltgenmesiyle aldehit (propanal) verir'),
       II=(True,'aldehit yükseltgenince propanoik asit (C₃H₆O₂) oluşur'),
       III=(True,'B bir karboksilik asittir; sulu çözeltisi mavi turnusolu kırmızıya çevirir'))
o=OC(d,sr('Yalnız I','Yalnız III','I ve II','II ve III','I, II ve III')); assert o['dogru']=='I, II ve III'
Q('0005','elde','orta','öncüllü','Primer alkolden aldehit ve asit eldesi','Primer alkolün basamaklı yükseltgenme ürünlerini sınıflandırır ve formüllerini bulur.',
  'Primer alkol önce aldehite, aldehit de karboksilik aside yükseltgenir; her basamakta formül değişimi izlenir.','Primer alkolün yükseltgenmesinde ürünün doğrudan asit olduğunu ya da aldehitte durduğunu sanmak.','şema: 1-propanol → A → B',
  [A('A’yı bul','Primer alkol ılımlı yükseltgenince aldehit olur.','CH₃CH₂CH₂OH → CH₃CH₂CHO (A) → I doğru'),A('Formülü izle','Alkolden aldehite 2 H gider; aldehitten asite 1 O eklenir.','C₃H₈O → C₃H₆O → C₃H₆O₂'),A('B’nin sınıfı','Aldehit yükseltgenince karboksilik asit olur.','B: propanoik asit → II, III doğru'),A('Sonuç','Üç yargı da şema ve bilgilerle uyumludur.',etk(d))],
  metin='Şekilde 1-propanolün iki basamaklı yükseltgenmesi gösterilmiştir.\nBuna göre,\nI. A bir aldehittir.\nII. B’nin molekül formülü C₃H₆O₂’dir.\nIII. B’nin sulu çözeltisi mavi turnusolu kırmızıya çevirir.\nyargılarından hangileri doğrudur?',
  sekil=SK,istenen='Doğru olan yargılar.',ip=['Her yükseltgenme basamağında karbonil grubunun nasıl değiştiğini ve formülde ne değiştiğini izle.'],
  bilgi=[B('Primer alkolün yükseltgenmesi','Primer alkol → aldehit → karboksilik asit sırasıyla yükseltgenir. Alkolden aldehite geçerken molekül 2 H kaybeder, aldehitten asite geçerken 1 O kazanır. Örnek: CH₃CH₂OH → CH₃CHO → CH₃COOH')],
  puf='Yükseltgenme basamaklarında fonksiyonel grubun değişimini izle.',dogru=o['dogru'],yan=o['yan'],sira=o['sira'])

# ================= 06 · elde edilme · orta · şekil · öncüllü =================
SK=tk(sahne([(M_1B,'X'),(M_2BUT,'Y'),(M_TBUT,'Z')]))
d=dict(I=(True,'X primer alkoldür; yükseltgenmesiyle bütanal oluşur ve aldehit Tollens ayıracıyla gümüş aynası verir'),
       II=(False,'Y sekonder alkoldür; ürünü bir ketondur ve ketonlar Fehling ayıracıyla çökelti vermez'),
       III=(False,'Z tersiyer alkoldür; –OH taşıyan karbonunda H bulunmadığından ılımlı koşullarda yükseltgenmez'))
o=OC(d,sr('Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III')); assert o['dogru']=='Yalnız I'
Q('0006','elde','orta','öncüllü','Alkol sınıfına göre yükseltgenme ürünü','Primer, sekonder ve tersiyer alkolün ılımlı yükseltgenme ürünlerini ve bu ürünlerin ayıraçlarla davranışını birleştirir.',
  'Primer alkol aldehit, sekonder alkol keton verir; tersiyer alkol ılımlı koşullarda yükseltgenmez. Yalnız aldehit Tollens ve Fehling ile tepkime verir.','Sekonder alkolün ürününü aldehit sanmak ya da tersiyer alkolün de yükseltgendiğini düşünmek.','X, Y, Z alkolleri',
  [A('Alkolleri sınıflandır','–OH taşıyan karbona bağlı karbon sayısına bak.','X: 1° · Y: 2° · Z: 3°'),A('Ürünleri belirle','Primer → aldehit; sekonder → keton; tersiyer → tepkime yok.','X→bütanal · Y→bütanon · Z→yok'),A('Ayıraçlarla ilişkilendir','Yalnız aldehit Tollens ve Fehling ile tepkime verir.','Bütanal + Tollens → ayna'),A('Sonuç','Yalnız I doğrudur.',etk(d))],
  metin=MK+' X, Y ve Z alkollerinin her biri asitli K₂Cr₂O₇ çözeltisiyle ılımlı koşullarda ayrı ayrı yükseltgenmeye çalışılıyor.\nBuna göre,\nI. X’ten oluşan ürün Tollens ayıracı ile gümüş aynası verir.\nII. Y’den oluşan ürün Fehling ayıracı ile tuğla kırmızısı çökelti verir.\nIII. Z’den oluşan ürün bir ketondur.\nyargılarından hangileri doğrudur?',
  sekil=SK,istenen='Doğru olan yargılar.',ip=['Önce her alkolün sınıfını belirle; sonra bu sınıfın yükseltgenme ürününü bul.'],
  bilgi=[B('Alkol sınıfı ve ürün','Primer alkol → aldehit, sekonder alkol → keton verir; tersiyer alkolde –OH taşıyan karbonda H olmadığından ılımlı yükseltgenme olmaz. Örnek: 1-propanol → propanal, 2-propanol → propanon')],
  puf='Alkolün sınıfı, yükseltgenme ürününün sınıfını belirler.',dogru=o['dogru'],yan=o['yan'],sira=o['sira'])

# ================= 07 · Tollens/Fehling · orta · tablo · öncüllü =================
SK=tablo_svg(['Madde','Tollens ayıracı','Fehling ayıracı'],[['X','Gümüş aynası oluştu','Kırmızı çökelti oluştu'],['Y','Değişiklik olmadı','Değişiklik olmadı'],['Z','Gümüş aynası oluştu','Kırmızı çökelti oluştu']])
d=dict(I=(True,'iki ayıraçla da pozitif sonuç veren karbonil bileşiği aldehittir; X ve Z aldehit grubu içerir'),
       II=(True,'karbonil bileşiği olduğu bilinen Y ayıraçların ikisiyle de tepkime vermediğine göre aldehit değil ketondur'),
       III=(False,'X ve Z’nin ikisi de aldehit olsa da aynı molekül formülüne sahip oldukları belirtilmemiştir; yapı izomeri olduğu kesin değildir'))
o=OC(d,sr('Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III')); assert o['dogru']=='I ve II'
Q('0007','ayirt','orta','öncüllü','Tollens ve Fehling deney sonuçları','Tollens ve Fehling deney sonuçlarından karbonil bileşiğinin aldehit ya da keton olduğunu çıkarır.',
  'Aldehit hem Tollens hem Fehling ayıracıyla tepkime verir; keton ikisiyle de vermez. Sonuçlardan yalnız sınıf çıkarılır, izomerlik çıkarılamaz.','Deney sonucundan sınıfın ötesinde (izomerlik gibi) bir sonuç çıkarmak.','Tollens/Fehling tablosu',
  [A('Tabloyu oku','X ve Z her iki ayıraçla pozitif, Y negatif sonuç vermiş.','X, Z: +,+ · Y: −,−'),A('Sınıfı çıkar','Pozitif sonuç aldehit, negatif sonuç keton demektir.','X, Z aldehit · Y keton → I, II doğru'),A('III’ü sına','Sınıf aynı olsa da formülleri bilinmeyen bileşikler izomer olmak zorunda değildir.','III kesin değil'),A('Sonuç','I ve II kesinlikle doğrudur.',etk(d))],
  metin='X, Y ve Z maddelerinin her biri karbonil grubu içeren bir organik bileşiktir (aldehit ya da keton). Bu maddelerle yapılan Tollens ve Fehling deneylerinin sonuçları aşağıdaki tabloda verilmiştir.\nBuna göre,\nI. X ve Z aldehit grubu içerir.\nII. Y ketondur.\nIII. X ve Z birbirinin yapı izomeridir.\nyargılarından hangileri kesinlikle doğrudur?',
  sekil=SK,istenen='Kesinlikle doğru olan yargılar.',ip=['Aldehit ve ketonun iki ayıraca verdiği tepkimeleri karşılaştır; tablodan çıkarılamayan bilgiyi ayıkla.'],
  bilgi=[B('Tollens ve Fehling','Aldehit, Tollens ayıracıyla gümüş aynası, Fehling ayıracıyla tuğla kırmızısı Cu₂O çökeltisi oluşturur. Ketonlar bu ayıraçlarla tepkimeye girmez. Örnek: propanal iki testte de pozitif, propanon iki testte de negatiftir')],
  puf='Ayıraç sonuçları yalnızca fonksiyonel grubu belirler; formül hakkında bilgi vermez.',dogru=o['dogru'],yan=o['yan'],sira=o['sira'])
# ================= 08 · Tollens hesabı · orta · şekil =================
n_ald=Fr(22,10)/44; assert n_ald==Fr(1,20)
dg_=n_ald*2*AG; assert dg_==Fr(54,5)
vals=dict(d=dg_,k1=n_ald*1*AG,k3=n_ald*3*AG,k4=n_ald*4*AG,ters=n_ald/2*AG)
assert vals['k1']==Fr(27,5) and vals['k3']==Fr(81,5) and vals['k4']==Fr(108,5) and vals['ters']==Fr(27,10) and len(set(vals.values()))==5
g=(r'\draw[thick] (0,2.8) -- (0,.7) arc (180:360:.65) -- (1.3,2.8);'
   r'\fill[vurgu!15] (0,2.2) -- (0,.7) arc (180:360:.65) -- (1.3,2.2) -- cycle;\draw[thick,vurgu] (0,2.2) -- (1.3,2.2);'
   r'\draw[thick] (-.15,2.8) -- (1.45,2.8);'
   r'\node[anchor=west,align=left,font=\small] at (1.8,1.8) {\ce{CH3CHO}: 2,2 g};'
   r'\node[anchor=west,align=left,font=\small] at (1.8,1.0) {fazla miktarda\\Tollens ayıracı};'
   r'\draw[thin] (1.75,1.8) -- (1.0,1.8);\draw[thin] (1.75,1.0) -- (1.0,1.0);')
SK=tk(g)
Q('0008','ayirt','orta','şekilli','Tollens tepkimesinde gümüş miktarı','Aldehitin kütlesinden mol sayısını ve 1:2 oranıyla oluşan gümüş kütlesini hesaplar.',
  'Aldehit ile Tollens tepkimesinde 1 mol aldehitten 2 mol Ag oluşur; kütle → mol → mol oranı → kütle zinciri izlenir.','Mol oranını 1:1 almak ya da kütleyi mole çevirmeden hesaplamak.','Tollens gümüş hesabı',
  [A('Aldehit molünü bul','Kütleyi mol kütlesine böl.','2,2 / 44 = 0,05 mol'),A('Mol oranını uygula','1 mol aldehitten 2 mol Ag oluşur.','0,05 × 2 = 0,1 mol Ag'),A('Kütleye çevir','Ag mol kütlesi 108 g/mol.','0,1 × 108 = 10,8 g'),A('Sonuç','Çeperde biriken gümüş 10,8 g’dır.','10,8 g')],
  metin='Şekildeki deney tüpünde bulunan etanalin tamamı, fazla miktarda Tollens ayıracı ile tepkimeye giriyor. Tepkimede 1 mol aldehitten 2 mol Ag katısı oluşmaktadır.\n(CH₃CHO: 44 g/mol, Ag: 108 g/mol)\nBuna göre tüpün çeperinde biriken gümüş kaç gramdır?',
  sekil=SK,istenen='Oluşan Ag kütlesi (g).',ip=['Önce aldehitin mol sayısını, sonra tepkime oranından gümüşün mol sayısını bul.'],
  bilgi=[B('Mol hesabı','n = m / M. Tepkimede katsayı oranı mol oranını verir. Örnek: 1 mol X’ten 3 mol Y oluşuyorsa 0,2 mol X’ten 0,6 mol Y oluşur')],
  puf='Önce mole geç, katsayı oranını uygula, sonra kütleye dön.',dogru=vals['d'],
  yan=[(vals['k1'],'Tepkime oranını 1 mol aldehit için 1 mol Ag almış; 0,05 × 108 = 5,4 g bulmuş.','bilgi'),
       (vals['k3'],'1 mol aldehitten 3 mol Ag oluştuğunu varsayarak 0,15 × 108 = 16,2 g bulmuş.','bilgi'),
       (vals['k4'],'1 mol aldehitten 4 mol Ag oluştuğunu varsayarak 0,2 × 108 = 21,6 g bulmuş.','bilgi'),
       (vals['ters'],'Mol oranını ters çevirip Ag molünü aldehit molünün yarısı (0,025 mol) almış; 0,025 × 108 = 2,7 g bulmuş.','islem')])

# ================= 09 · indirgenme · orta · şema =================
assert (5,10,1)[1]+2==12
g1,bb=mol_ciz(M_3PNON,0.3,0)
g=(g1+f'\n\\draw[{ARR},thick] ({bb[1]+.3:.2f},.3) -- ({bb[1]+2.5:.2f},.3) node[midway,above=2pt,font=\\footnotesize] {{\\ce{{H2}}, Ni}};'
   f'\n\\node[draw,thick,rounded corners=3pt,minimum width=.9cm,minimum height=.8cm] at ({bb[1]+3.1:.2f},.3) {{\\textbf{{Y}}}};')
SK=tk(g)
dg='3-pentanol'
yan=[('1-pentanol','Hidrojenin ketonun ucundaki karbona katıldığını sanmış; oysa H₂ karbonil karbonuna ve oksijenine katılır.','bilgi'),
     ('pentanal','Ketonun indirgenmesinde aldehit oluştuğunu sanmış; indirgenme bir alkol verir, aldehit vermez.','bilgi'),
     ('2-pentanol','–OH grubunu 2. karbona yazmış; oysa C=O 3. karbonda olduğundan –OH da 3. karbonda oluşur.','dikkat'),
     ('pentan','C=O grubunun tamamen kalktığını sanmış; H₂/Ni ile yalnız C=O çift bağı doyurulur, oksijen kalır.','bilgi')]
Q('0009','tep','orta','şekilli','Ketonun indirgenmesi','Ketonun H₂/Ni ile indirgenme ürününün sekonder alkol olduğunu belirler.',
  'Keton H₂/Ni ile indirgenince karbonil çift bağı doyar; karbonil karbonu –OH taşıyan sekonder alkol karbonu olur.','İndirgenme ürününü aldehit ya da hidrokarbon sanmak.','keton + H₂/Ni',
  [A('X’i tanı','Karbonil karbonuna iki karbon bağlıdır; bileşik ketondur.','3-pentanon (C₅H₁₀O)'),A('Tepkimeyi yaz','H₂ karbonil çift bağına katılır.','C₅H₁₀O + H₂ → C₅H₁₂O'),A('Ürünü yerleştir','C=O karbonu –OH’li karbon olur.','–OH 3. karbonda'),A('Adı yaz','Sekonder alkol oluşur.','3-pentanol')],
  metin='Şekilde iskelet formülü verilen keton, Ni katalizörlüğünde H₂ ile indirgenerek Y bileşiğine dönüştürülmüştür.\nBuna göre Y bileşiğinin adı aşağıdakilerden hangisidir?',
  sekil=SK,istenen='Y’nin adı.',ip=['H₂’nin karbonil grubunun hangi bağına katıldığını ve oluşan fonksiyonel grubu düşün.'],
  bilgi=[B('Karbonil indirgenmesi','Aldehit H₂/Ni ile primer alkole, keton sekonder alkole indirgenir; C=O çift bağı doyar, oksijen –OH olarak kalır. Örnek: propanal → 1-propanol, propanon → 2-propanol')],
  puf='İndirgenme: aldehit → primer alkol, keton → sekonder alkol.',dogru=dg,yan=yan,sira=yer(dg,[y[0] for y in yan],1))

# ================= 10 · fiziksel özellikler · orta · tablo · olumsuz kök =================
tab=[('K','C₄H₁₀ (bütan)',58,'−1'),('L','C₃H₆O (propanal)',58,49),('M','C₃H₆O (propanon)',58,56),('N','C₃H₈O (1-propanol)',60,97)]
assert -1<tab[1][3]<tab[2][3]<tab[3][3]
SK=tablo_svg(['Madde','Formül ve ad','Mol kütlesi (g/mol)','Kaynama noktası (°C)'],[[a,b,str(c),str(e)] for a,b,c,e in tab])
sec=[('L ile M birbirinin fonksiyonel grup izomeridir.',True,'ikisinin de formülü C₃H₆O’dur ve biri aldehit, diğeri ketondur'),
     ('M’nin molekülleri arasında dipol–dipol etkileşimi vardır.',True,'karbonil grubu polardır ve bu da kalıcı dipol oluşturur'),
     ('N’nin kaynama noktasının yüksek olması hidrojen bağından kaynaklanır.',True,'N’de O–H bağı vardır ve moleküller arası hidrojen bağı oluşur'),
     ('K’nin kaynama noktasının düşük olması molekülleri arasında yalnız London kuvvetlerinin bulunmasından kaynaklanır.',True,'bütan apolar bir hidrokarbondur'),
     ('L’nin molekülleri arasında hidrojen bağı oluşur.',False,'')]
o=tek2(sec,False)
Q('0010','fiz','orta','tablo','Karbonil bileşiklerinin kaynama noktaları','Aldehit ve ketonun kaynama noktalarını alkan ve alkolle karşılaştırıp etkileşim türlerini yorumlar.',
  'Aldehit ve keton polardır (dipol–dipol), saf hâlde hidrojen bağı yapmazlar; kaynama noktaları aynı mol kütleli alkandan yüksek, alkolden düşüktür.','Aldehit ve ketonun saf hâlde hidrojen bağı yaptığını sanmak.','kaynama noktası tablosu',
  [A('Tabloyu yorumla','Mol kütleleri yakın olsa da kaynama noktaları farklı.','K < L < M < N'),A('Etkileşimleri ele','K: London · L, M: dipol–dipol · N: hidrojen bağı.','Sıra etkileşim gücüyle uyumlu'),A('İfadeleri sına','Aldehitte O’ya bağlı H yoktur.','L’de H bağı yok'),A('Sonuç','L propanaldir; O–H bağı taşımaz ve saf hâlde hidrojen bağı yapmaz.','L’de hidrojen bağı yoktur → ilgili ifade söylenemez')],
  metin='Aşağıdaki tabloda mol kütleleri birbirine yakın dört organik bileşiğin formülleri ve normal kaynama noktaları verilmiştir.\nBu verilere göre aşağıdakilerden hangisi söylenemez?',
  sekil=SK,istenen='Söylenemeyen ifade.',ip=['Her bileşiğin molekülleri arasındaki etkileşim türünü belirle; O atomuna bağlı H olup olmadığına bak.'],
  bilgi=[B('Karbonil bileşiklerinde etkileşim','Aldehit ve ketonda C=O polardır; moleküller arası dipol–dipol etkileşimi vardır. O–H bağı olmadığından saf hâlde hidrojen bağı yapmazlar. Örnek: etanal (CH₃CHO) molekülleri arasında hidrojen bağı bulunmaz')],
  puf='Hidrojen bağı için H atomu N, O ya da F’ye doğrudan bağlı olmalıdır.',dogru=o['dogru'],yan=o['yan'],sira=yer(o['dogru'],[s[0] for s in sec if s[1]],0))

# ================= 11 · izomer · orta · düz =================
vals=dict(d=IZ[6]['ket'],atla=IZ[6]['ket']-1,c5=IZ[5]['ket'],ald=IZ[6]['ald'],hepsi=IZ[6]['ald']+IZ[6]['ket'])
assert vals['d']==6 and len(set(vals.values()))==5
Q('0011','izo','orta','düz','Keton izomerlerini sayma','C₆H₁₂O formüllü ketonların tümünü zincir ve konum izomerliğini tarayarak sayar.',
  'Ketonlarda karbonil iç karbonda bulunur; zincir ve karbonil konumu değiştirilerek tüm yapılar taranır.','Dallanmış ketonlardan birini atlamak ya da aldehitleri de saymak.','C₆H₁₂O ketonları',
  [A('İskeletleri yaz','6 karbonlu düz, 5 karbonlu bir dallı ve 4 karbonlu iki dallı iskeletleri ayrı ayrı düşün.','düz C₆ · C₅+CH₃ · C₄+2CH₃'),A('Düz zincirde konum','Karbonil uçta olamaz (aldehit olur).','2-heksanon · 3-heksanon'),A('Dallı zincirlerde konum','Karbonil iç karbonda olmalı.','3-metil-2-pentanon · 4-metil-2-pentanon · 2-metil-3-pentanon · 3,3-dimetil-2-bütanon'),A('Say','Toplam keton sayısını bul.','2 + 4 = 6')],
  metin='Stereoizomerler ayrı sayılmayacaktır.\nMolekül formülü C₆H₁₂O olan, karbonil grubu içeren ve halka ve C=C bağı içermeyen bileşiklerden kaç tanesi ketondur?',
  istenen='C₆H₁₂O formüllü keton sayısı.',ip=['Karbonil grubunun zincir ucunda mı yoksa içte mi olması gerektiğini düşün; düz ve dallı iskeletleri ayrı tara.'],
  bilgi=[B('Yapı izomerliği','Aynı molekül formülüne sahip, atomların bağlanma düzeni farklı bileşiklere yapı izomeri denir. Örnek: C₄H₁₀ için bütan ve 2-metilpropan zincir izomeridir')],
  puf='Keton için karbonil iç karbonda olmalı; uçtaysa aldehit olur.',dogru=vals['d'],
  yan=[(vals['atla'],'Dallanmış ketonlardan birini atlayıp beş keton saymış.','dikkat'),
       (vals['c5'],'Karbon sayısını 5 alıp C₅H₁₀O formüllü ketonları saymış.','dikkat'),
       (vals['ald'],'Ketonlar yerine C₆H₁₂O formüllü aldehit izomerlerini saymış.','dikkat'),
       (vals['hepsi'],'Aldehit ve ketonların tümünü (8 + 6) saymış; soru yalnız ketonları sormaktadır.','dikkat')])

# ================= 12 · izomer · orta · şekil · öncüllü =================
SK=tk(sahne([(M_PENTAL,'A'),(M_3PNON,'B'),(M_3MB,'C')]))
assert formul(M_PENTAL)==formul(M_3PNON)==formul(M_3MB)
d=dict(I=(False,'A ile B aynı formüllü ama farklı fonksiyonel gruplu (aldehit–keton) bileşiklerdir; bu fonksiyonel grup izomerliğidir, zincir izomerliği değil'),
       II=(True,'A ve C’nin ikisi de aldehittir ve karbon iskeletleri farklıdır (düz ve dallı); zincir izomeridirler'),
       III=(True,'B keton, C aldehittir ve ikisinin de formülü C₅H₁₀O’dur; fonksiyonel grup izomeridirler'))
o=OC(d,sr('Yalnız I','Yalnız III','I ve II','I ve III','II ve III')); assert o['dogru']=='II ve III'
Q('0012','izo','orta','öncüllü','Aldehit–keton izomerliği','Aynı formüllü karbonil bileşiklerinde zincir ve fonksiyonel grup izomerliğini ayırt eder.',
  'Aynı fonksiyonel grupta iskelet farkı zincir izomerliği; aynı formülde farklı fonksiyonel grup (aldehit–keton) fonksiyonel grup izomerliğidir.','Zincir ve fonksiyonel grup izomerliğini karıştırmak.','A, B, C izomerleri',
  [A('Formülleri karşılaştır','Üç bileşiğin de formülü C₅H₁₀O.','A, B, C izomerdir'),A('A ve B','Aldehit ve keton: fonksiyonel grup farkı.','I yanlış'),A('A ve C','İkisi de aldehit, iskelet farklı.','II doğru'),A('B ve C','Keton ve aldehit: fonksiyonel grup farkı.','III doğru')],
  metin=MK+' A, B ve C bileşiklerinin molekül formülleri aynıdır.\nBuna göre,\nI. A ile B birbirinin zincir izomeridir.\nII. A ile C birbirinin zincir izomeridir.\nIII. B ile C birbirinin fonksiyonel grup izomeridir.\nyargılarından hangileri doğrudur?',
  sekil=SK,istenen='Doğru olan yargılar.',ip=['Her çiftte fonksiyonel grupların ve karbon iskeletlerinin aynı mı farklı mı olduğunu karşılaştır.'],
  bilgi=[B('İzomer türleri','Zincir izomerleri aynı fonksiyonel gruba, farklı karbon iskeletine sahiptir; fonksiyonel grup izomerleri farklı fonksiyonel gruplara sahiptir. Örnek: bütan–2-metilpropan zincir; etanol–dimetil eter fonksiyonel grup izomeridir')],
  puf='İzomer türünü fonksiyonel grupları ve iskeletleri karşılaştırarak belirle.',dogru=o['dogru'],yan=o['yan'],sira=o['sira'])

# ================= 13 · elde edilme · orta · şema =================
fE=lambda c,h,o_:(c,h,o_)
etin=(2,2,0); X=(etin[0],etin[1]+2,1); Y=(X[0],X[1]+2,1); Zf=(X[0],X[1],X[2]+1)
assert X==(2,4,1) and Y==(2,6,1) and Zf==(2,4,2)
g=(r'\node (s) at (0,0) {\ce{C2H2}};'
   r'\node[draw,thick,rounded corners=3pt,minimum width=.9cm,minimum height=.8cm] (x) at (4.2,0) {\textbf{X}};'
   r'\node[draw,thick,rounded corners=3pt,minimum width=.9cm,minimum height=.8cm] (y) at (8.0,1.1) {\textbf{Y}};'
   r'\node[draw,thick,rounded corners=3pt,minimum width=.9cm,minimum height=.8cm] (z) at (8.0,-1.1) {\textbf{Z}};'
   f'\\draw[{ARR},thick] (s.east)+(.1,0) -- (x.west) node[midway,above=2pt,font=\\footnotesize,align=center] {{\\ce{{H2O}}\\\\\\ce{{HgSO4}}}};'
   f'\\draw[{ARR},thick] (x.east) -- (y.west) node[midway,above=3pt,sloped,font=\\footnotesize] {{\\ce{{H2}}, Ni}};'
   f'\\draw[{ARR},thick] (x.east) -- (z.west) node[midway,below=3pt,sloped,font=\\footnotesize] {{Tollens ayıracı}};')
SK=tk(g)
dg='X: etanal · Y: etanol · Z: etanoik asit'
yan=[('X: etanal · Y: etanoik asit · Z: etanol','H₂/Ni ile yükseltgenme olduğunu, Tollens ayıracıyla ise indirgenme olduğunu sanmış; oysa H₂ indirger, Tollens ayıracı yükseltger.','bilgi'),
     ('X: etanol · Y: etanal · Z: etanoik asit','Etinin hidrasyonunda alkol oluştuğunu sanmış; oysa kararsız ara ürün yeniden düzenlenerek etanal verir.','bilgi'),
     ('X: etanal · Y: etanol · Z: tepkime vermez','Tollens ayıracının yalnız ketonlarla tepkime verdiğini sanmış; oysa etanal aldehittir ve gümüş aynası vererek asite yükseltgenir.','bilgi'),
     ('X: etanoik asit · Y: etanol · Z: etanal','Hidrasyon ürününü karboksilik asit sanmış; oysa C₂H₄O formülüne uyan etanal oluşur.','bilgi')]
Q('0013','elde','orta','şekilli','Etinin hidrasyonu ve ürünün tepkimeleri','Etinin hidrasyonuyla elde edilen aldehitin indirgenme ve Tollens yükseltgenme ürünlerini belirler.',
  'Etin + H₂O (HgSO₄) → etanal; etanal H₂/Ni ile etanole indirgenir, Tollens ayıracıyla etanoik asite yükseltgenir.','Hidrasyon ürününü alkol sanmak ya da indirgenme–yükseltgenme yönünü karıştırmak.','şema: etin → X → Y, Z',
  [A('X’i bul','Etinin hidrasyonu aldehit verir.','C₂H₂ + H₂O → C₂H₄O: etanal'),A('Y’yi bul','H₂/Ni karbonili indirger.','CH₃CHO → CH₃CH₂OH (C₂H₆O)'),A('Z’yi bul','Tollens ayıracı aldehiti asite yükseltger.','CH₃CHO → CH₃COOH'),A('Birleştir','Üç bileşik sırasıyla yazılır.','etanal · etanol · etanoik asit')],
  metin='Şekilde etin gazından başlayarak yapılan dönüşümler gösterilmiştir. Etinin uygun koşullarda su ile tepkimesinden kararlı X bileşiği oluşmuştur.\nBuna göre X, Y ve Z bileşikleri aşağıdakilerden hangisinde doğru verilmiştir?',
  sekil=SK,istenen='X, Y ve Z’nin adları.',ip=['Hidrasyon ürününün formülünü ve fonksiyonel grubunu belirle; H₂/Ni ile Tollens ayıracının yönlerini ayrı ayrı düşün.'],
  bilgi=[B('Alkin hidrasyonu','Alkine uygun koşullarda su katılınca kararlı ürün olarak bir karbonil bileşiği oluşur. Örnek: propinin hidrasyonundan propanon oluşur')],
  puf='Hidrasyon ürününün formülünü yazıp karbonil grubunun yerine bak.',dogru=dg,yan=yan,sira=yer(dg,[y[0] for y in yan],0))

# ================= 14 · yükseltgenme · orta · grafik · öncüllü =================
ald={0:Fr(1),10:Fr(7,10),20:Fr(2,5),30:Fr(1,5),40:Fr(1,10)}; asit={t:1-v for t,v in ald.items()}
assert all(ald[t]+asit[t]==1 for t in ald)
assert ald[20]<asit[20] and (ald[0]-ald[40])==asit[40]-asit[0] and ald[40]>0
g=('\\begin{axis}[width=7.2cm,height=5.8cm,xmin=0,xmax=45,ymin=0,ymax=1.1,xtick={0,10,20,30,40},ytick={0,0.2,0.4,0.6,0.8,1},tick label style={font=\\small},axis lines=left,'
   'xlabel={Süre (dk)},ylabel={Mol sayısı},label style={font=\\small},grid=both,grid style={gray!25}]\n'
   +'\\addplot[thick,vurgu,mark=*,mark size=2pt] coordinates {'+' '.join(f'({t},{float(v)})' for t,v in ald.items())+'};\n'
   +'\\addplot[thick,mark=square*,mark size=2pt] coordinates {'+' '.join(f'({t},{float(v)})' for t,v in asit.items())+'};\n'
   +'\\node[font=\\small\\bfseries] at (axis cs:35,0.3) {\\ce{CH3CHO}};\n\\node[font=\\small\\bfseries] at (axis cs:35,0.72) {\\ce{CH3COOH}};\n\\end{axis}')
SK=tk(g)
d=dict(I=(True,'20. dakikada etanal 0,4 mol, etanoik asit 0,6 mol’dür; etanalin mol sayısı asidinkinden azdır'),
       II=(True,'etanalin azalan mol sayısı, aynı sürede oluşan asidin mol sayısına eşittir; çünkü 1 mol aldehitten 1 mol asit oluşur ve toplam 1 mol kalır'),
       III=(False,'40. dakikada grafikte etanalin mol sayısı 0,1’dir; etanal henüz tükenmemiştir'))
o=OC(d,sr('Yalnız I','Yalnız III','I ve II','II ve III','I, II ve III')); assert o['dogru']=='I ve II'
Q('0014','tep','orta','öncüllü','Aldehit yükseltgenmesinde mol–zaman grafiği','Mol–zaman grafiğinden aldehit ve asit miktarlarının değişimini yorumlar.',
  'Aldehit yükseltgenirken mol sayısı azalır, oluşan asidin mol sayısı artar; 1 : 1 dönüşümde toplam mol sabit kalır.','Grafikteki eğrileri karıştırmak ya da tepkimenin bittiğini varsaymak.','mol–zaman grafiği',
  [A('Eğrileri ayır','Azalan eğri etanal, artan eğri etanoik asittir.','CH₃CHO ↓ · CH₃COOH ↑'),A('I’i oku','20. dakikada eğrilerin değerlerini karşılaştır.','0,4 < 0,6 → I doğru'),A('II’yi sına','Azalan ve artan mol sayılarını karşılaştır.','Azalan = artan → II doğru'),A('III’ü oku','40. dakikada etanal eğrisine bak.','0,1 mol → III yanlış')],
  metin='Etanalin bir yükseltgenle etanoik aside dönüşmesi sırasında etanal ve etanoik asidin mol sayılarının zamanla değişimi grafikte verilmiştir. Tepkimede 1 mol etanalden 1 mol etanoik asit oluşmaktadır.\nBuna göre,\nI. 20. dakikada etanalin mol sayısı etanoik asidinkinden azdır.\nII. Etanalin azalan mol sayısı, oluşan etanoik asidin mol sayısına eşittir.\nIII. 40. dakikada etanal tamamen tükenmiştir.\nyargılarından hangileri doğrudur?',
  sekil=SK,istenen='Doğru olan yargılar.',ip=['Hangi eğrinin hangi maddeye ait olduğunu belirle ve istenen anlardaki değerleri grafikten oku.'],
  bilgi=[B('Mol–zaman grafiği','Tepkimeye giren madde zamanla azalır, ürün artar; katsayılar eşitse azalan ve artan mol sayıları birbirine eşittir. Örnek: 1 : 1 tepkimede X’in 0,3 mol azalması Y’de 0,3 mol artış demektir')],
  puf='Grafikte önce eğrileri maddelerle eşleştir, sonra değerleri oku.',dogru=o['dogru'],yan=o['yan'],sira=o['sira'])

# ================= 15 · Tollens karışım · zor · şema =================
M_=72; assert 4*12+8+16==M_
mk_=Fr(288,10); ag=Fr(324,10)
nag=ag/AG; nald=nag/2; ntop=mk_/M_; nket=ntop-nald
assert nag==Fr(3,10) and nald==Fr(3,20) and ntop==Fr(2,5) and nket==Fr(1,4)
kal=nket*M_; assert kal==18 and nald*M_==Fr(54,5)
vals=dict(d=kal,bir=(ntop-nag)*M_,ald=nald*M_,yari=mk_/Fr(2),dort=(ntop-nag/4)*M_)
assert vals['bir']==Fr(36,5) and vals['dort']==Fr(117,5) and vals['yari']==Fr(72,5) and len(set(vals.values()))==5
g=(r'\node[draw,thick,rounded corners=3pt,align=center,inner sep=5pt] (k) at (0,0) {bütanal + bütanon\\karışımı: 28,8 g};'
   r'\node[draw,thick,rounded corners=3pt,align=center,inner sep=5pt] (a) at (7.6,0) {Ag katısı\\32,4 g};'
   f'\\draw[{ARR},thick] (k.east) -- (a.west) node[midway,above=2pt,font=\\footnotesize,align=center] {{fazla Tollens\\\\ayıracı}};')
SK=tk(g)
Q('0015','ayirt','zor','şekilli','Aldehit–keton karışımında Tollens hesabı','Karışımdaki yalnız aldehitin Tollens ayıracıyla gümüş oluşturduğunu kullanarak ketonun kütlesini bulur.',
  'Aynı formüllü (aynı mol kütleli) aldehit ve ketonun karışımında yalnız aldehit Ag verir; Ag molünden aldehit mol sayısı, toplam moldan keton mol sayısı bulunur.','Ketonun da gümüş verdiğini sanmak ya da mol oranını 1 : 1 almak.','karışım + Tollens',
  [A('Gümüş molünü bul','Ag kütlesini mol kütlesine böl.','32,4 / 108 = 0,3 mol Ag'),A('Aldehit molünü bul','Yalnız aldehit Ag verir, oran 1 : 2.','0,3 / 2 = 0,15 mol bütanal'),A('Toplam mole git','İki bileşiğin de formülü C₄H₈O (72 g/mol).','28,8 / 72 = 0,4 mol → keton 0,25 mol'),A('Ketonun kütlesi','Keton mol sayısını mol kütlesiyle çarp.','0,25 × 72 = 18 g')],
  metin='Şekilde bütanal ve bütanondan oluşan bir karışımın fazla miktarda Tollens ayıracı ile tepkimesi gösterilmiştir. Tepkime %100 verimle gerçekleşmekte ve 1 mol aldehitten 2 mol Ag katısı oluşmaktadır.\n(C₄H₈O: 72 g/mol, Ag: 108 g/mol)\nBuna göre karışımdaki bütanonun kütlesi kaç gramdır?',
  sekil=SK,istenen='Karışımdaki bütanonun kütlesi (g).',ip=['Hangi bileşiğin gümüş oluşturduğunu belirle; iki bileşiğin mol kütlelerinin ilişkisinden yararlan.'],
  bilgi=[B('Karışım hesabı','Karışımda yalnız bir bileşik tepkimeye girerse, onun miktarı ürün miktarından bulunur; kalan miktar toplamdan çıkarılır. Örnek: 5 mol karışımın 2 molü tepkimeye giriyorsa diğer bileşik 3 moldür')],
  puf='Karışımda tepkimeye giren bileşiği belirleyip yalnız onun miktarını üründen bul.',dogru=vals['d'],
  yan=[(vals['bir'],'Mol oranını 1 : 1 alıp aldehiti 0,3 mol bulmuş; ketonu (0,4 − 0,3) × 72 = 7,2 g hesaplamış.','bilgi'),
       (vals['ald'],'Aldehitin kütlesini (0,15 × 72 = 10,8 g) bulup ketonun kütlesi olarak yazmış.','dikkat'),
       (vals['yari'],'Karışımın yarı yarıya olduğunu varsayıp 28,8 / 2 = 14,4 g bulmuş.','bilgi'),
       (vals['dort'],'1 mol aldehitten 4 mol Ag oluştuğunu varsayarak aldehiti 0,075 mol, ketonu 0,325 mol saymış; 0,325 × 72 = 23,4 g bulmuş.','bilgi')])

# ================= 16 · alkol → karbonil · zor · şekil · öncüllü =================
M_A=M_1B; M_B=M_2BUT; M_C=M_2MP1; M_D=M_TBUT
def alk_sinif(spec):
    G_,lab,od=graf(spec)
    for n in lab:
        if lab[n] in('OH','HO'):
            (c,)=list(G_[n]); return {1:'prim',2:'sek',3:'ter'}[sum(1 for m in G_[c] if lab[m] is None)]
assert [alk_sinif(s) for s in (M_A,M_B,M_C,M_D)]==['prim','sek','prim','ter']
urun_formul={'A':(4,8,1),'B':(4,8,1),'C':(4,8,1)}   # C4H10O -2H
assert all((f[0],f[1]+2,f[2])==(4,10,1) for f in urun_formul.values())
SK=tk(sahne([(M_A,'A'),(M_B,'B'),(M_C,'C'),(M_D,'D')],bosluk=.8))
d=dict(I=(False,'D tersiyer alkol olduğundan yükseltgenmez; yalnız A ve C’nin ürünleri aldehittir ve gümüş aynası verir, yani sayı ikidir'),
       II=(False,'D tersiyer alkoldür ve ılımlı koşullarda yükseltgenmez; ürün oluşmaz, dolayısıyla keton değildir'),
       III=(True,'A’dan bütanal, C’den 2-metilpropanal oluşur; ikisi de C₄H₈O formüllü aldehittir ve karbon iskeletleri farklıdır, yani zincir izomeridir'))
o=OC(d,sr('Yalnız I','Yalnız III','I ve II','II ve III','I, II ve III')); assert o['dogru']=='Yalnız III'
Q('0016','izo','zor','öncüllü','C₄H₁₀O alkollerinin yükseltgenme ürünleri','Dört alkolün yükseltgenme ürünlerini, Tollens davranışını ve ürünlerin izomerliğini birlikte değerlendirir.',
  'Primer alkol aldehit, sekonder alkol keton verir, tersiyer yükseltgenmez; aynı formüllü aldehitler iskelet farkıyla zincir izomeridir.','Tersiyer alkolün de ürün verdiğini sanmak ya da aldehit ürünlerinin izomerliğini gözden kaçırmak.','A, B, C, D alkolleri',
  [A('Alkolleri sınıflandır','–OH’li karbona bağlı karbon sayısına bak.','A, C: primer · B: sekonder · D: tersiyer'),A('Ürünleri belirle','Primer → aldehit; sekonder → keton; tersiyer → ürün yok.','A: bütanal · B: bütanon · C: 2-metilpropanal · D: yok'),A('I ve II’yi sına','Gümüş aynası yalnız aldehitten gelir (iki ürün); D’den ürün oluşmaz.','I yanlış · II yanlış'),A('III’ü sına','Bütanal ve 2-metilpropanal aynı formülde, farklı iskelettedir.','III doğru')],
  metin=MK+' A, B, C ve D alkollerinin dördü de C₄H₁₀O formüllüdür ve her biri ılımlı koşullarda asitli K₂Cr₂O₇ ile yükseltgenmeye çalışılıyor; oluşan ürünler Tollens ayıracı ile deneniyor.\nBuna göre,\nI. Gümüş aynası veren ürün sayısı üçtür.\nII. D’den oluşan ürün bir ketondur.\nIII. A’dan ve C’den oluşan ürünler birbirinin zincir izomeridir.\nyargılarından hangileri doğrudur?',
  sekil=SK,istenen='Doğru olan yargılar.',ip=['Önce her alkolün sınıfını belirle; sonra ürünlerin sınıfını ve formülünü yazarak yargıları tek tek sına.'],
  bilgi=[B('Yükseltgenme ve izomerlik','Alkolden karbonil bileşiğine geçerken molekül 2 H kaybeder. Aynı formüllü ürünler iskelet düzenine göre zincir, fonksiyonel grubuna göre fonksiyonel grup izomeridir. Örnek: propanal ve propanon fonksiyonel grup izomeridir')],
  puf='Alkolün sınıfı, ürünün sınıfını belirler.',dogru=o['dogru'],yan=o['yan'],sira=o['sira'])

# ================= 17 · alkol → aldehit → Ag · zor · şekil =================
mol=dict(I=Fr(2,10),II=Fr(3,10),III=Fr(1,10),IV=Fr(1,10))
assert [alk_sinif(x) for x in (M_2MP1,M_2BUT,M_TBUT,M_1B)]==['prim','sek','ter','prim']
vals=dict(d=(mol['I']+mol['IV'])*2*AG,bir=(mol['I']+mol['IV'])*AG,sek=(mol['I']+mol['II']+mol['IV'])*2*AG,hepsi=sum(mol.values())*2*AG,sekter=(mol['II']+mol['III'])*2*AG)
assert vals['d']==Fr(324,5) and vals['bir']==Fr(162,5) and vals['sek']==Fr(648,5) and vals['hepsi']==Fr(756,5) and vals['sekter']==Fr(432,5) and len(set(vals.values()))==5
SK=tk(sahne([(M_2MP1,'\\textbf{I}: 0,2 mol'),(M_2BUT,'\\textbf{II}: 0,3 mol'),(M_TBUT,'\\textbf{III}: 0,1 mol'),(M_1B,'\\textbf{IV}: 0,1 mol')],bosluk=.8))
Q('0017','ayirt','zor','şekilli','Alkol karışımından gümüş eldesi','İskelet formülünden alkol sınıfını belirleyip yükseltgenebilenlerin aldehit ürününden Tollens tepkimesiyle gümüş kütlesini hesaplar.',
  'Yalnız primer alkol aldehit verir; tersiyer yükseltgenmez, sekonder keton verir. Gümüş yalnız aldehitten ve 1 : 2 oranında oluşur.','Her alkolün aldehit verdiğini varsaymak ya da oranı 1 : 1 almak.','alkol tüpleri',
  [A('Alkolleri sınıflandır','–OH’li karbona bağlı karbon sayısına bak.','I: primer · II: sekonder · III: tersiyer · IV: primer'),A('Ürünleri belirle','Yalnız primer alkolden aldehit oluşur.','I → 2-metilpropanal (0,2 mol) · IV → bütanal (0,1 mol) · II → keton · III → ürün yok'),A('Gümüşün molü','1 mol aldehitten 2 mol Ag.','(0,2 + 0,1) × 2 = 0,6 mol Ag'),A('Kütleye çevir','Ag: 108 g/mol.','0,6 × 108 = 64,8 g')],
  metin=MK+' Şekilde verilen dört ayrı tüpteki alkollerin tamamı, ılımlı koşullarda yeterli asitli K₂Cr₂O₇ ile tepkimeye sokuluyor; yükseltgenebilen alkoller %100 verimle yükseltgenmekte ve yükseltgenme aldehit ya da keton basamağında kalmaktadır. Oluşan ürünler tek kapta birleştirilip fazla Tollens ayıracı ile tamamen tepkimeye sokuluyor. Tepkimede 1 mol aldehitten 2 mol Ag katısı oluşmaktadır.\n(Ag: 108 g/mol)\nBuna göre oluşan Ag katısının kütlesi kaç gramdır?',
  sekil=SK,istenen='Oluşan Ag kütlesi (g).',ip=['Hangi tüplerde Tollens ayıracıyla tepkime verecek bir ürün oluştuğunu belirlemek için yapılara bak.'],
  bilgi=[B('Alkol sınıfı ve ürün','Primer alkol → aldehit, sekonder alkol → keton verir; tersiyer alkol ılımlı koşullarda yükseltgenmez. Örnek: 1-bütanol → bütanal, 2-bütanol → bütanon')],
  puf='Önce yapıları sınıflandır, sonra mol oranlarını uygula.',dogru=vals['d'],
  yan=[(vals['bir'],'1 mol aldehitten 1 mol Ag oluştuğunu varsayıp 0,3 × 108 = 32,4 g bulmuş.','bilgi'),
       (vals['sek'],'Sekonder alkolün de aldehit verdiğini sanmış; (0,2 + 0,3 + 0,1) × 2 × 108 = 129,6 g bulmuş.','bilgi'),
       (vals['hepsi'],'Dört alkolün de aldehit verdiğini sanmış; 0,7 × 2 × 108 = 151,2 g bulmuş.','bilgi'),
       (vals['sekter'],'Sekonder ve tersiyer alkolü aldehit veren, primer alkolleri vermeyen sanmış; 0,4 × 2 × 108 = 86,4 g bulmuş.','bilgi')])

# ================= 18 · izomer + indirgenme · zor · öncüllü =================
tum=IZ[5]['ald']+IZ[5]['ket']; assert tum==7
d=dict(I=(False,'C₅H₁₀O’nun gümüş aynası veren yani aldehit olan izomer sayısı dörttür (pentanal, 2-metilbütanal, 3-metilbütanal, 2,2-dimetilpropanal)'),
       II=(True,'her izomer indirgenince kendi iskeletini koruyan ayrı bir alkol verir; 4 primer ve 3 sekonder alkol olmak üzere 7 farklı alkol oluşur'),
       III=(False,'aldehit izomer sayısı dört, keton izomer sayısı üçtür; sayılar eşit değildir'))
o=OC(d,sr('Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III')); assert o['dogru']=='Yalnız II'
Q('0018','izo','zor','öncüllü','C₅H₁₀O izomerleri ve indirgenme ürünleri','C₅H₁₀O karbonil izomerlerini sayıp hepsinin indirgenme ürünlerini birlikte değerlendirir.',
  'C₅H₁₀O için 4 aldehit ve 3 keton vardır; her biri indirgenince iskeletini koruyan farklı bir alkol (aldehitler primer, ketonlar sekonder) verir.','Aldehit ve keton sayılarını karıştırmak ya da farklı bileşiklerin aynı alkolü vereceğini sanmak.','C₅H₁₀O karbonilleri',
  [A('İzomerleri say','Aldehit ve keton iskeletlerini ayrı tara.','4 aldehit + 3 keton = 7'),A('I’i sına','Gümüş aynası aldehitten gelir.','Aldehit sayısı 4 → “üç” yanlış'),A('II’yi sına','İndirgenmede iskelet değişmez, her izomer farklı alkol verir.','7 farklı alkol → II doğru'),A('III’ü sına','Aldehit 4, keton 3.','Eşit değil → III yanlış')],
  metin='Molekül formülü C₅H₁₀O olan, karbonil grubu içeren ve halka ve C=C bağı içermeyen bütün izomerler (aldehit ve ketonlar) dikkate alınıyor; stereoizomerler ayrı sayılmayacaktır.\nBuna göre,\nI. Tollens ayıracı ile gümüş aynası veren izomer sayısı üçtür.\nII. Bu izomerlerin tamamı H₂/Ni ile indirgenirse birbirinden farklı yedi alkol oluşur.\nIII. Keton izomerlerinin sayısı aldehit izomerlerinin sayısına eşittir.\nyargılarından hangileri doğrudur?',
  istenen='Doğru olan yargılar.',ip=['Önce aldehit ve keton izomerlerini ayrı ayrı say; sonra indirgenmede iskeletin değişip değişmediğini düşün.'],
  bilgi=[B('İndirgenme ve iskelet','Karbonil indirgenmesinde yalnız C=O doyar, karbon iskeleti değişmez; farklı iskeletli iki bileşik aynı alkolü vermez. Örnek: bütanal → 1-bütanol, bütanon → 2-bütanol')],
  puf='Aynı formüllü bileşikleri iskelet ve fonksiyonel grup bakımından ayrı ayrı sınıflandır.',dogru=o['dogru'],yan=o['yan'],sira=o['sira'])

# ================= 19 · şema · zor · öncüllü =================
Xf=(4,8,1); Yf=(4,10,1); assert (Xf[0],Xf[1]+2,Xf[2])==Yf
nX=Fr(72,10)/72; assert nX==Fr(1,10)
g=(r'\node[draw,thick,rounded corners=3pt,minimum width=.9cm,minimum height=.8cm] (x) at (0,0) {\textbf{X}};'
   r'\node[draw,thick,rounded corners=3pt,minimum width=.9cm,minimum height=.8cm] (y) at (4.0,0) {\textbf{Y}};'
   r'\node[draw,thick,rounded corners=3pt,minimum width=.9cm,minimum height=.8cm] (z) at (8.2,0) {\textbf{Z}};'
   f'\\draw[{ARR},thick] (x.east) -- (y.west) node[midway,above=2pt,font=\\footnotesize] {{\\ce{{H2}}, Ni}};'
   f'\\draw[{ARR},thick] (y.east) -- (z.west) node[midway,above=2pt,font=\\footnotesize,align=center] {{ılımlı\\\\yükseltgen}};')
SK=tk(g)
d=dict(I=(True,'C₄H₈O formüllü olup Tollens ayıracıyla tepkime vermeyen bileşik, aldehit olmadığından bütanondur'),
       II=(False,'7,2 g X, 7,2 / 72 = 0,1 mol’dür ve 1 mol karbonil 1 mol H₂ aldığından 0,1 mol H₂ gerekir; 0,2 mol değildir'),
       III=(True,'X’ten oluşan Y, 2-bütanoldür (sekonder alkol); ılımlı yükseltgenince yeniden bütanon, yani X oluşur'))
o=OC(d,sr('Yalnız I','Yalnız III','I ve II','I ve III','I, II ve III')); assert o['dogru']=='I ve III'
Q('0019','tep','zor','şekilli','İndirgenme–yükseltgenme zinciri','Tollens bilgisinden karbonil bileşiğini belirleyip indirgenme–yükseltgenme zincirini ve mol hesabını birleştirir.',
  'Tollens vermeyen C₄H₈O bütanondur; H₂/Ni ile 2-bütanole indirgenir, ılımlı yükseltgenince yine bütanona döner. 1 mol karbonil 1 mol H₂ alır.','Zincirin sonunda başka bir bileşik oluştuğunu sanmak ya da H₂ molünü yanlış oranlamak.','şema: X → Y → Z',
  [A('X’i belirle','C₄H₈O ve Tollens negatif: aldehit olamaz.','X: bütanon (keton) → I doğru'),A('Y’yi bul','Keton indirgenince sekonder alkol olur.','Y: 2-bütanol'),A('Z’yi bul','Sekonder alkol ılımlı yükseltgenince keton verir.','Z: bütanon = X → III doğru'),A('H₂ molünü hesapla','7,2 g X’in mol sayısı kadar H₂ harcanır.','7,2 / 72 = 0,1 mol → II yanlış')],
  metin='Molekül formülü C₄H₈O olan ve karbonil grubu içeren X bileşiği Tollens ayıracı ile tepkime vermemektedir. X bileşiğinden başlanarak şekildeki dönüşümler gerçekleştiriliyor.\n(C₄H₈O: 72 g/mol)\nBuna göre,\nI. X bütanondur.\nII. 7,2 g X’in tamamının indirgenmesi için 0,2 mol H₂ gerekir.\nIII. Z, X ile aynı bileşiktir.\nyargılarından hangileri doğrudur?',
  sekil=SK,istenen='Doğru olan yargılar.',ip=['Tollens sonucundan X’in sınıfını çıkar; sonra her basamakta fonksiyonel grubun nasıl değiştiğini izle.'],
  bilgi=[B('İndirgenme–yükseltgenme','Keton ile sekonder alkol, H₂/Ni ile indirgenme ve ılımlı yükseltgenme yoluyla birbirine dönüştürülebilir. Örnek: propanon ⇄ 2-propanol')],
  puf='Her basamakta fonksiyonel grubun nasıl değiştiğini izle.',dogru=o['dogru'],yan=o['yan'],sira=o['sira'])

# ================= 20 · olumsuz kök · zor · şekil =================
SK=tk(sahne([(M_NEOP,'K'),(M_3PNON,'L'),(M_3MB,'M')],bosluk=1.0))
assert formul(M_NEOP)==formul(M_3PNON)==formul(M_3MB)==(5,10,1)
sec=[('K, Tollens ayıracıyla gümüş aynası verir.',True,'K’de karbonil karbonuna H bağlıdır, yani K aldehittir ve Tollens ayıracını indirger'),
     ('L, H₂/Ni ile indirgenince sekonder alkol oluşur.',True,'L bir ketondur ve ketonlar H₂/Ni ile sekonder alkole indirgenir'),
     ('K ile M birbirinin zincir izomeridir.',True,'ikisi de C₅H₁₀O formüllü aldehittir ve karbon iskeletleri farklıdır'),
     ('L ile M birbirinin fonksiyonel grup izomeridir.',True,'ikisinin de formülü C₅H₁₀O’dur ve biri keton, diğeri aldehittir'),
     ('L, Fehling ayıracıyla tuğla kırmızısı çökelti verir.',False,'')]
o=tek2(sec,False)
Q('0020','tep','orta','şekilli','Aldehit ve ketonun tepkime ve izomerlik karşılaştırması','Aynı formüllü aldehit ve ketonun Tollens, Fehling, indirgenme ve izomerlik özelliklerini birlikte değerlendirir.',
  'Aynı formülde aldehit ve keton: aldehit Tollens/Fehling verir, keton vermez; ikisi de indirgenince alkol verir; iskelet farkı zincir, grup farkı fonksiyonel grup izomerliğidir.','Ketonun Fehling ayıracıyla çökelti verdiğini sanmak ya da izomerlik türlerini karıştırmak.','K, L, M yapıları',
  [A('Formülleri doğrula','Üç bileşiğin de formülü C₅H₁₀O.','K, L, M izomerdir'),A('Sınıfları belirle','K ve M: karbonil karbonunda H var; L: iki karbon.','K, M aldehit · L keton'),A('İfadeleri sına','Her yargıyı sınıfa göre incele.','A, B, C, D doğru'),A('Yanlışı bul','Keton Fehling ayıracıyla tepkime vermez.','L + Fehling → değişiklik yok')],
  metin=MK+' K, L ve M bileşiklerinin molekül formülleri aynıdır.\nBuna göre aşağıdaki yargılardan hangisi yanlıştır?',
  sekil=SK,istenen='Yanlış olan yargı.',ip=['Her bileşiğin sınıfını belirleyip bu sınıfın ayıraçlarla, H₂/Ni ile ve izomerlikle ilgili davranışını sırayla sına.'],
  bilgi=[B('Aldehit ve keton karşılaştırması','Aldehit Tollens ve Fehling ayıracıyla tepkime verir, keton vermez; ikisi de H₂/Ni ile alkole indirgenir. Örnek: propanal gümüş aynası verir, propanon vermez')],
  puf='Her bileşiğin sınıfını belirleyip yargıları sınıfa göre sına.',dogru=o['dogru'],yan=o['yan'],sira=yer(o['dogru'],[s[0] for s in sec if s[1]],4))

# ---------- yaz ----------
for x in P.ANA: x['kardes']=None
SCR=os.environ.get('SCRATCH','/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/kr')
os.makedirs(SCR,exist_ok=True)
P.yaz(os.path.join(GD,'karbonil-1.json'),os.path.join(SCR,'bos-karbonil.json'))
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=KEY))['kartlar'].append(c['id'])
json.dump(dict(konu=KONU_AD,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2018–2026 Kimya, MEB 12. sınıf Organik Bileşikler.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','akkarbonil.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
