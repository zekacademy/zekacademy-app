"""AYT Kimya · Alkoller ve Eterler · 20 soru. Kardeş yok, ipucu 1.
Yapılar tek bir atom listesinden hem çizilir hem çözümlenir (sınıf, formül); izomer sayıları kaba kuvvetle doğrulanır."""
import sys,os,json,math
from fractions import Fraction as Fr
from itertools import combinations_with_replacement
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-kim'))
import _hafif_kim2 as H
from _hafif_kim2 import *
from _hafif_kim import onc,tek,etk
import networkx as nx
KONU_AD='Alkoller ve Eterler'; KEY='akim|Alkoller ve Eterler'
P=Parti('alkol',KONU_AD,KEY,ders='AYT Kimya',idon='aytkim'); H.KONU=KONU_AD
KAYNAK='ÖSYM AYT 2018–2026 Kimya alkol–eter soruları (yalnız mantık) · MEB 12. sınıf Organik Bileşikler'
def kartla(no,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(f'K-AKALK-{no}',alt,fikir,tuzak,z,kalip,adim,tipId,tip,KAYNAK)
def q(no,ad,**k):
    assert len(k['ip'])==1; mk(P,no,ad=ad,adim=len(ad),**k)
TIP={'sinif':('al-sinif','Alkollerin sınıflandırılması (1°, 2°, 3°)'),'ad':('al-adlandirma','Alkol ve eter adlandırma'),'fiz':('al-fiziksel','Fiziksel özellikler ve hidrojen bağı'),
     'yuk':('al-tepkime','Alkollerin tepkimeleri ve yükseltgenme'),'eter':('al-eter','Eter oluşumu (dehidrasyon)'),'izo':('al-izomer','Yapı izomerliği')}
def Q(no,tp,z,kalip,alt,kaz,fikir,tuzak,ozet,ad,**k):
    t,tn=TIP[tp]; kartla(no[-2:],alt,fikir,tuzak,z,kalip,len(ad),t,tn)
    q(no,ad,tipId=t,tip=tn,z=z,alt=alt,kaz=kaz,kalip=kalip,kart=f'K-AKALK-{no[-2:]} ({ozet})',**k)
def nk(o):
    o['yan']=[(m,(e if e.endswith('.') else e+'.'),t) for m,e,t in o['yan']]; return o
def yer(dogru,digerler,i): return list(digerler[:i])+[dogru]+list(digerler[i:])

# ---------------- yapı modeli ----------------
# spec: (ad, ebeveyn, açı°, etiket). Etiketsiz düğüm = karbon; 'OH'/'HO' = hidroksil; 'O' = eter oksijeni.
SC=0.8
def coords(spec):
    c={}
    for n,p,a,l in spec:
        c[n]=(0.0,0.0) if p is None else (c[p][0]+math.cos(math.radians(a)),c[p][1]+math.sin(math.radians(a)))
    return c
def analiz(spec):
    G_=nx.Graph(); lab={}
    for n,p,a,l in spec:
        G_.add_node(n); lab[n]=l
        if p is not None: G_.add_edge(n,p)
    return G_,lab
def formul(spec):
    G_,lab=analiz(spec); C=sum(1 for n in lab if lab[n] is None); O=sum(1 for n in lab if lab[n] in('OH','HO','O'))
    H_=sum(4-G_.degree(n) for n in lab if lab[n] is None)+sum(1 for n in lab if lab[n] in('OH','HO'))
    return C,H_,O
def sinif(spec):
    G_,lab=analiz(spec); r=[]
    for n in lab:
        if lab[n] in('OH','HO'):
            cn=[m for m in G_[n]]; assert len(cn)==1
            r.append(sum(1 for m in G_[cn[0]] if lab[m] is None))
    assert len(r)==1; return {0:'met',1:'prim',2:'sek',3:'ter'}[r[0]]
def mol_ciz(spec,ox,oy,ad=None):
    c=coords(spec); g=[]; xs=[]; ys=[]
    P_={n:(ox+SC*c[n][0],oy+SC*c[n][1]) for n in c}
    for n,p,a,l in spec:
        x,y=P_[n]; xs.append(x); ys.append(y)
        if l: xs+= [x-.35,x+.35]; ys+=[y-.25,y+.25]
    sh=lambda l:0 if not l else (.22 if len(l)==1 else .38)
    for n,p,a,l in spec:
        if p is None: continue
        (x1,y1),(x2,y2)=P_[p],P_[n]
        lp=[s for s in spec if s[0]==p][0][3]
        g.append(f'\\draw[thick,shorten <={sh(lp)*SC:.3f}cm,shorten >={sh(l)*SC:.3f}cm] ({x1:.3f},{y1:.3f}) -- ({x2:.3f},{y2:.3f});')
    for n,p,a,l in spec:
        if l: g.append(f'\\node[inner sep=0pt,font=\\small] at ({P_[n][0]:.3f},{P_[n][1]:.3f}) {{{l}}};')
    return '\n'.join(g),(min(xs),max(xs),min(ys),max(ys))
def sahne(satirlar,bosluk=1.1,satir_ara=1.3):
    """satirlar: [[(spec,etiket),...],...]; etiketler molekülün altında."""
    out=[]; y0=0.0
    for row in satirlar:
        x=0.0; parts=[]; hmin=0; hmax=0
        for spec,et in row:
            c=coords(spec); w=[SC*c[n][0] for n in c]; h=[SC*c[n][1] for n in c]
            ox=x-min(w)+.35; g,bb=mol_ciz(spec,ox,y0-0); parts.append((g,bb,et)); x=bb[1]+bosluk
            hmin=min(hmin,bb[2]); hmax=max(hmax,bb[3])
        ytop=max(p[1][3] for p in parts); ybot=min(p[1][2] for p in parts)
        # moleküllerin y konumlarını satırın tepesine göre kaydırma: hepsi y0'dan başladı; etiket satırın altında
        for g,bb,et in parts:
            out.append(g)
            if et: out.append(f'\\node[font=\\small\\bfseries] at ({(bb[0]+bb[1])/2:.3f},{ybot-.55:.3f}) {{{et}}};')
        y0=ybot-.55-satir_ara-(ytop-ybot if False else 0)-max(0,(ytop-0))
    return '\n'.join(out)
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'; TAIL='\n\\end{tikzpicture}'
ARR='-{Stealth[length=2.2mm,width=2mm]}'
def tk(g): return tikz_svg(HEAD+g+TAIL)
# --- yapılar ---
def zincir(n,oh=None,dal=None,eter=None):
    pass
M_2BUT=[('a',None,0,None),('b','a',30,None),('o','b',90,'OH'),('c','b',-30,None),('d','c',30,None)]
M_TBUT=[('c',None,0,None),('m1','c',180,None),('m2','c',0,None),('m3','c',-90,None),('o','c',90,'OH')]       # 2-metil-2-propanol
M_3M1B=[('o',None,0,'HO'),('c1','o',-30,None),('c2','c1',30,None),('c3','c2',-30,None),('m','c3',-90,None),('c4','c3',30,None)]  # 3-metil-1-bütanol
M_4M2P=[('a',None,0,None),('b','a',30,None),('o','b',90,'OH'),('c','b',-30,None),('d','c',30,None),('m','d',90,None),('e','d',-30,None)]  # 4-metil-2-pentanol
M_2P=[('a',None,0,None),('b','a',30,None),('o','b',90,'OH'),('c','b',-30,None)]                          # 2-propanol
M_1P=[('o',None,0,'HO'),('c1','o',-30,None),('c2','c1',30,None),('c3','c2',-30,None)]                    # 1-propanol
M_3P=[('a',None,0,None),('b','a',30,None),('c','b',-30,None),('o','c',-90,'OH'),('d','c',30,None),('e','d',-30,None)]  # 3-pentanol
M_2M1P=[('o',None,0,'HO'),('c1','o',-30,None),('c2','c1',30,None),('c3','c2',-30,None),('c4','c2',90,None)]  # 2-metil-1-propanol
M_3M2B=[('a',None,0,None),('b','a',30,None),('o','b',90,'OH'),('c','b',-30,None),('m','c',-90,None),('d','c',30,None)]   # 3-metil-2-bütanol
M_2M2B=[('a',None,0,None),('b','a',30,None),('o','b',90,'OH'),('m','b',-90,None),('c','b',-30,None),('d','c',30,None)]   # 2-metil-2-bütanol
M_1B=[('o',None,0,'HO'),('c1','o',-30,None),('c2','c1',30,None),('c3','c2',-30,None),('c4','c3',30,None)]
M_METOH=[('a',None,0,None),('o','a',30,'OH')]
M_ETOH=[('a',None,0,None),('b','a',30,None),('o','b',-30,'OH')]
M_EOIP=[('a',None,0,None),('b','a',30,None),('o','b',-30,'O'),('c','o',30,None),('m','c',90,None),('d','c',-30,None)]   # 2-etoksipropan
M_MOET=[('a',None,0,None),('o','a',30,'O'),('b','o',-30,None),('c','b',30,None)]                                   # metoksietan
M_DEE=[('a',None,0,None),('b','a',30,None),('o','b',-30,'O'),('c','o',30,None),('d','c',-30,None)]                 # dietil eter

# ---------------- izomer sayımı (kaba kuvvet) ----------------
def izomerler(n):
    """CnH(2n+2)O: n+1 düğümlü ağaçlar; bir düğüm O (derece 1: alkol, 2: eter)."""
    bulunan=[]
    for T in nx.nonisomorphic_trees(n+1):
        for o in T.nodes:
            if T.degree(o) not in (1,2): continue
            if any(T.degree(m)>4 for m in T.nodes if m!=o): continue
            H_=T.copy(); nx.set_node_attributes(H_,{m:('O' if m==o else 'C') for m in H_.nodes},'t')
            if any(nx.is_isomorphic(H_,B_,node_match=lambda a,b:a['t']==b['t']) for B_,_ in bulunan): continue
            bulunan.append((H_,o))
    r={'prim':0,'sek':0,'ter':0,'eter':0}
    for H_,o in bulunan:
        if H_.degree(o)==2: r['eter']+=1
        else:
            cn=list(H_[o])[0]; k=sum(1 for m in H_[cn] if m!=o)
            r[{1:'prim',2:'sek',3:'ter'}[k]]+=1
    return r
IZ={n:izomerler(n) for n in (3,4,5)}
assert IZ[3]=={'prim':1,'sek':1,'ter':0,'eter':1}
assert IZ[4]=={'prim':2,'sek':1,'ter':1,'eter':3}
assert IZ[5]=={'prim':4,'sek':3,'ter':1,'eter':6}

# yapı çözümleme doğrulamaları
for sp,f,s in [(M_2BUT,(4,10,1),'sek'),(M_TBUT,(4,10,1),'ter'),(M_3M1B,(5,12,1),'prim'),(M_4M2P,(6,14,1),'sek'),(M_2P,(3,8,1),'sek'),(M_1P,(3,8,1),'prim'),(M_3P,(5,12,1),'sek'),
               (M_2M1P,(4,10,1),'prim'),(M_3M2B,(5,12,1),'sek'),(M_2M2B,(5,12,1),'ter'),(M_1B,(4,10,1),'prim'),(M_ETOH,(2,6,1),'prim'),(M_METOH,(1,4,1),'met')]:
    assert formul(sp)==f,(sp,formul(sp)); assert sinif(sp)==s,(sp,sinif(sp))
for sp,f in [(M_EOIP,(5,12,1)),(M_MOET,(3,8,1)),(M_DEE,(4,10,1))]: assert formul(sp)==f

ORD=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
def OC(d,sira): return onc(d,[tuple(x for x in t.replace('Yalnız ','').replace(',',' ').replace(' ve ',' ').split()) for t in sira])
def sr(*k): assert [x for x in ORD if x in k]==list(k),k; return list(k)
MK='Şekilde iskelet formülleri verilmiştir; köşeler ve uçlar karbon atomunu gösterir, karbona bağlı hidrojen atomları yazılmamıştır.'

# ================= 01 · sınıflandırma · kolay · öncüllü =================
assert sinif(M_2BUT)=='sek' and sinif(M_TBUT)=='ter' and sinif(M_3M1B)=='prim'
d=dict(I=(True,'A bileşiğinde –OH grubunun bağlı olduğu karbon atomu iki karbon atomuna bağlıdır, yani A sekonder alkoldür'),
       II=(False,'B bileşiğinde –OH taşıyan karbon üç karbon atomuna bağlıdır, yani B tersiyer alkoldür'),
       III=(False,'C bileşiğinde –OH taşıyan karbon yalnız bir karbon atomuna bağlıdır, yani C primer alkoldür'))
o=OC(d,sr('Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III')); assert o['dogru']=='Yalnız I'
SK=tk(sahne([[(M_2BUT,'A'),(M_TBUT,'B'),(M_3M1B,'C')]]))
Q('0001','sinif','kolay','öncüllü','Alkollerin sınıflandırılması','–OH grubunun bağlı olduğu karbon atomuna bakarak alkolü primer, sekonder ya da tersiyer olarak sınıflandırır.',
  '–OH taşıyan karbon atomuna bağlı karbon sayısı alkolün sınıfını belirler: 1 karbon primer, 2 karbon sekonder, 3 karbon tersiyer.','Hidroksil taşıyan karbonu, zincirdeki konumuna ya da dallanmaya bakarak yanlış sınıflandırmak.','A, B, C alkolleri',
  [A('A’yı incele','–OH’nin bağlı olduğu karbonun komşu karbonlarını say.','A: 2 karbon komşu → sekonder → I doğru'),A('B’yi incele','Merkez karbonda –OH ve üç karbon bağı vardır.','B: 3 karbon komşu → tersiyer → II yanlış'),A('C’yi incele','–OH zincirin ucundaki CH₂ karbonundadır.','C: 1 karbon komşu → primer → III yanlış'),A('Sonuç','Yalnız I öncülü doğrudur.',etk(d))],
  metin='Şekilde iskelet formülleri verilen A, B ve C bileşiklerinin üçü de alkoldür (köşeler ve uçlar karbondur).\nI. A bileşiğinde –OH grubunun bağlı olduğu karbon atomu iki karbon atomuna bağlıdır.\nII. B bileşiği primer alkoldür.\nIII. C bileşiğinde –OH grubunun bağlı olduğu karbon atomu iki karbon atomuna bağlıdır.\nBuna göre bu yargılardan hangileri doğrudur?',
  sekil=SK,istenen='Doğru olan yargılar.',ip=['Her bileşikte –OH grubunun bağlandığı karbonu bul ve o karbona bağlı diğer karbonları say.'],
  bilgi=[B('Primer, sekonder, tersiyer alkol','–OH grubunun bağlı olduğu karbon atomu bir karbona bağlıysa primer (1°), iki karbona bağlıysa sekonder (2°), üç karbona bağlıysa tersiyer (3°) alkoldür. Örnek: 1-pentanol primer, 2-pentanol sekonder, 2-metil-2-pentanol tersiyerdir')],
  puf='Alkolün sınıfı, –OH taşıyan karbonun kaç karbonla komşu olduğuna bağlıdır.',dogru=o['dogru'],yan=o['yan'],sira=o['sira'])

# ================= 02 · adlandırma · kolay · şekil =================
assert formul(M_4M2P)==(6,14,1)
dg='4-metil-2-pentanol'
yan2=[('2-metil-4-pentanol','Zinciri –OH’ye yakın uçtan değil, dalın yakın olduğu uçtan numaralandırmış; oysa –OH grubu en küçük numarayı almalıdır.','bilgi'),
      ('1,3-dimetil-1-bütanol','Ana zinciri 4 karbonlu seçmiş; –OH taşıyan en uzun zincir 5 karbonludur.','bilgi'),
      ('3-metil-2-pentanol','Metil grubunun yerini bir karbon kaydırarak 3. karbonda göstermiş.','dikkat'),
      ('4-metil-3-pentanol','–OH grubunun yerini 3. karbon olarak almış, oysa zincir –OH’ye en yakın uçtan numaralanır ve –OH 2. karbondadır.','dikkat')]
SK=tk(sahne([[(M_4M2P,None)]]))
Q('0002','ad','kolay','şekilli','Alkol adlandırma','İskelet formülü verilen alkolü IUPAC kurallarına göre adlandırır.',
  'Ana zincir –OH taşıyan en uzun zincirdir; numaralandırma –OH grubuna en küçük numara verecek uçtan başlar, dallar sonra gelir.','Numaralamayı dala yakın uçtan başlatmak ya da ana zincirde –OH’yi dışarıda bırakmak.','4-metil-2-pentanol',
  [A('Ana zinciri seç','–OH taşıyan en uzun karbon zincirini bul.','5 karbonlu zincir → pentanol'),A('Numaralandır','–OH grubu en küçük numarayı alacak uçtan say.','–OH 2. karbonda → 2-pentanol'),A('Dalı yerleştir','Metil grubunun bağlandığı karbonun numarasını yaz.','Metil 4. karbonda → 4-metil'),A('Adı yaz','Dal adı, ana zincir adı ve –OH konumu birleştirilir.','4-metil-2-pentanol')],
  metin='Bir alkolün iskelet formülü şekilde gösterilmiştir; köşe ve uç noktalarda karbon bulunur, hidrojenler yazılmamıştır.\nBu alkolün sistematik adı aşağıdakilerden hangisidir?',
  sekil=SK,istenen='Bileşiğin IUPAC adı.',ip=['Önce –OH grubunu içeren en uzun karbon zincirini belirle; numaralamayı –OH grubuna en küçük numara gelecek uçtan başlat.'],
  bilgi=[B('Alkol adlandırma','Ana zincir –OH’yi içeren en uzun zincirdir. Zincir, –OH grubu en küçük numarayı alacak uçtan numaralanır; ad “dal adı – konum – ana zincir adı” biçiminde yazılır. Örnek: CH₃–CH₂–CH(OH)–CH₃ için 2-bütanol')],
  puf='Alkolde numaralamayı her zaman –OH grubuna en küçük numara verecek uçtan başlat.',dogru=dg,yan=yan2,sira=yer(dg,[y[0] for y in yan2],4))

# ================= 03 · hidrojen bağı · kolay =================
sec=[('CH₃CH₂CH₃',False,'CH₃CH₂CH₃ yalnız C–H ve C–C bağları içerir, O–H bağı yoktur; yalnız London kuvvetleri etkindir'),('CH₃OCH₃',False,'CH₃OCH₃’te hidrojenler yalnız karbona bağlıdır; oksijen hidrojen bağı alıcısı olabilir ama saf hâlde verici H yoktur'),
     ('CH₃CH₂OH',True,''),('CH₃CH₂OCH₃',False,'CH₃CH₂OCH₃’te O–H bağı yoktur, bu yüzden saf hâlde molekülleri arasında hidrojen bağı oluşmaz'),('CH₃CH₂CH₂CH₃',False,'CH₃CH₂CH₂CH₃ apolardır ve O–H bağı içermez; yalnız London kuvvetleri etkindir')]
o=nk(tek(sec,True))
Q('0003','fiz','kolay','düz','Hidrojen bağı','Bir bileşiğin saf hâlde molekülleri arasında hidrojen bağı yapıp yapmadığını bağ yapısından belirler.',
  'Saf hâlde hidrojen bağı için molekülde N, O ya da F’ye bağlı H atomu bulunmalıdır; eterde oksijene bağlı H yoktur.','Oksijen içeren her bileşiğin hidrojen bağı yaptığını sanmak.','hidrojen bağı',
  [A('Koşulu hatırla','Hidrojen bağı için H atomu N, O ya da F’ye bağlı olmalıdır.','O–H, N–H, F–H'),A('Her bileşiği tara','Oksijenli bileşiklerde H’nin kime bağlı olduğuna bak.','CH₃CH₂OH: O–H var · eterlerde O–H yok'),A('Hidrokarbonları ele','Yalnız C ve H içeren moleküller apolardır.','CH₃CH₂CH₃, CH₃CH₂CH₂CH₃ → London'),A('Sonuç','Yalnız etanolde O–H grubu vardır.','CH₃CH₂OH')],
  metin='Aşağıdaki bileşiklerden hangisinin saf hâlde molekülleri arasında hidrojen bağı oluşur?',
  istenen='Molekülleri arasında hidrojen bağı bulunan bileşik.',ip=['Hidrojen bağı için hidrojen atomunun hangi atoma bağlı olması gerektiğini düşün.'],
  bilgi=[B('Hidrojen bağı','H atomu N, O ya da F’ye bağlıysa, bu H başka bir molekülün N, O ya da F atomunun ortaklanmamış elektron çiftiyle hidrojen bağı yapar. Örnek: CH₃NH₂ molekülleri arasında N–H···N hidrojen bağı vardır')],
  puf='Eterlerde O–H bağı yoktur; saf eter hidrojen bağı yapmaz.',dogru=o['dogru'],yan=o['yan'],sira=yer('CH₃CH₂OH',[s[0] for s in sec if s[1]==False],0))

# ================= 04 · tablo · kaynama noktası · orta · öncüllü =================
tabK=[('K','CH₃CH₂CH₂CH₂OH',74,117),('L','CH₃CH₂OCH₂CH₃',74,35),('M','CH₃CH₂CH₂CH₂CH₃',72,36)]
SK=tablo_svg(['Madde','Formül','Mol kütlesi (g/mol)','Kaynama noktası (°C)'],[[a,b,str(c),str(e)] for a,b,c,e in tabK])
d=dict(I=(False,'K ile L aynı yükseltgenme-kütle değerine sahip olsa da kaynama noktaları arasındaki fark mol kütlesinden değil moleküller arası etkileşimden gelir; mol kütleleri zaten eşittir'),
       II=(True,'K’nin –OH grubu vardır, molekülleri arasında hidrojen bağı oluşur'),
       III=(True,'K ve L’nin molekül formülü C₄H₁₀O’dur, fonksiyonel grupları farklıdır; yapı izomeridirler'))
d['I']=(False,'K ve L’nin mol kütleleri eşittir; kaynama noktası farkı hidrojen bağından kaynaklanır, mol kütlesinden değil')
o=OC(d,sr('Yalnız II','Yalnız III','I ve II','II ve III','I, II ve III')); assert o['dogru']=='II ve III'
Q('0004','fiz','orta','tablo','Kaynama noktası ve moleküller arası etkileşim','Mol kütlesi birbirine yakın alkol, eter ve alkanın kaynama noktalarını moleküller arası etkileşim türüne göre yorumlar.',
  'Mol kütlesi benzer maddelerde kaynama noktasını moleküller arası etkileşimin gücü belirler; hidrojen bağı en güçlüdür.','Kaynama noktası farkını mol kütlesine bağlamak; eter ile alkolün yapı izomeri olduğunu atlamak.','tablo: alkol, eter, alkan',
  [A('Maddeleri tanı','Formüllere bakarak K’nin alkol, L’nin eter, M’nin alkan olduğunu belirle.','K: –OH · L: –O– · M: yalnız C–H'),A('I’i incele','K ile L’nin mol kütleleri eşittir (74 g/mol).','Fark mol kütlesinden değil → I yanlış'),A('II’yi incele','K’de O–H bağı var, saf hâlde hidrojen bağı oluşur.','II doğru'),A('III’ü incele','K ve L aynı molekül formülüne (C₄H₁₀O) sahip, farklı fonksiyonel gruplu.','III doğru → II ve III')],
  metin='Aşağıdaki tabloda üç organik bileşiğin formülleri, mol kütleleri ve normal kaynama noktaları verilmiştir.\nBu verilere göre,\nI. K’nin kaynama noktasının L’den yüksek olması, K’nin mol kütlesinin daha büyük olmasından kaynaklanır.\nII. K’nin molekülleri arasında hidrojen bağı bulunur.\nIII. K ve L birbirinin yapı izomeridir.\nyargılarından hangileri doğrudur?',
  sekil=SK,istenen='Doğru olan yargılar.',ip=['Mol kütleleri karşılaştırıp kaynama noktası farkının başka bir nedenle açıklanıp açıklanamayacağına bak.'],
  bilgi=[B('Kaynama noktası ve etkileşim','Mol kütleleri yakın bileşiklerde kaynama noktası; hidrojen bağı > dipol–dipol > London sırasındaki etkileşim gücüyle artar. Örnek: etil metil eter (60 g/mol) ile 1-propanol (60 g/mol) için 1-propanolün kaynama noktası çok yüksektir')],
  puf='Mol kütlesi eşitse kaynama noktası farkı moleküller arası etkileşimden gelir.',dogru=o['dogru'],yan=o['yan'],sira=o['sira'])

# ================= 05 · grafik · orta · öncüllü =================
alkan={1:-162,2:-89,3:-42,4:-1,5:36}; alkol={1:65,2:78,3:97,4:117,5:138}
fark={n:alkol[n]-alkan[n] for n in alkan}
assert all(alkol[n]>alkan[n] for n in alkan) and all(alkol[n+1]>alkol[n] and alkan[n+1]>alkan[n] for n in range(1,5)) and all(fark[n+1]<fark[n] for n in range(1,5))
assert alkan[3]<0
g=('\\begin{axis}[width=7.4cm,height=6cm,xmin=.5,xmax=5.6,ymin=-200,ymax=170,xtick={1,2,3,4,5},ytick={-200,-100,0,100},tick label style={font=\\small},axis lines=left,'
   'xlabel={Karbon sayısı},ylabel={Kaynama noktası ($^\\circ$C)},label style={font=\\small},grid=both,grid style={gray!25}]\n'
   +'\\addplot[thick,vurgu,mark=*,mark size=2pt] coordinates {'+' '.join(f'({n},{alkol[n]})' for n in alkol)+'};\n'
   +'\\addplot[thick,mark=square*,mark size=2pt] coordinates {'+' '.join(f'({n},{alkan[n]})' for n in alkan)+'};\n'
   +'\\node[font=\\small\\bfseries] at (axis cs:2.3,104) {II};\n\\node[font=\\small\\bfseries] at (axis cs:3.6,-62) {I};\n\\end{axis}')
SK=tk(g)
d=dict(I=(True,'her karbon sayısında II serisinin değeri I serisinden yüksektir; alkoller hidrojen bağı yapar, alkanlar yapmaz'),
       II=(True,'iki seride de karbon sayısı arttıkça kaynama noktası yükselir; çünkü London kuvvetleri güçlenir'),
       III=(False,'iki seri arasındaki fark karbon sayısı arttıkça azalır (227 °C’den 102 °C’ye), artmaz'))
o=OC(d,sr('Yalnız I','Yalnız III','I ve II','I ve III','II ve III')); assert o['dogru']=='I ve II'
Q('0005','fiz','orta','grafik','Alkol ve alkan kaynama noktaları','Grafikten alkol ve alkan serilerinin kaynama noktası eğilimlerini okuyup hidrojen bağı ve London kuvvetleriyle ilişkilendirir.',
  'Aynı karbon sayısında alkolün kaynama noktası alkanınkinden yüksektir; karbon arttıkça fark küçülür çünkü London kuvvetleri baskın hâle gelir.','Farkın karbon sayısıyla artacağını sanmak ya da grafiği okurken serileri karıştırmak.','kaynama noktası grafiği',
  [A('Serileri ayır','Alkan serisinde kaynama noktaları düşük, alkol serisinde yüksektir.','I: alkan · II: 1-alkanol'),A('I’i oku','Her karbon sayısında II, I’in üstünde kalıyor.','I doğru'),A('Eğilimi oku','İki eğri de sağa doğru yükseliyor.','II doğru'),A('Farkı oku','Eğriler arasındaki dikey uzaklık sağa doğru azalıyor.','III yanlış → I ve II')],
  metin='Aşağıdaki grafikte, karbon sayıları 1–5 arasında olan bir alkan serisinin (I) ve aynı karbon sayılı 1-alkanol serisinin (II) normal kaynama noktaları gösterilmiştir.\nBuna göre,\nI. Aynı karbon sayısında alkanol, alkandan yüksek sıcaklıkta kaynar.\nII. Karbon sayısı arttıkça iki serinin kaynama noktası da yükselir.\nIII. Aynı karbon sayılı alkanol ile alkan arasındaki kaynama noktası farkı karbon sayısı arttıkça büyür.\nyargılarından hangileri doğrudur?',
  sekil=SK,istenen='Doğru olan yargılar.',ip=['İki eğri arasındaki dikey uzaklığı soldan sağa doğru karşılaştır.'],
  bilgi=[B('Alkollerde kaynama noktası','Alkol molekülleri hidrojen bağı yaptığından kaynama noktası, benzer mol kütleli alkan ve eterlerden yüksektir. Hidrokarbon kısım büyüdükçe London kuvvetleri artar. Örnek: 1-oktanolün kaynama noktası 1-bütanolden yüksektir')],
  puf='Hidrojen bağı yapan alkol, aynı karbon sayılı alkandan daha yüksek sıcaklıkta kaynar.',dogru=o['dogru'],yan=o['yan'],sira=o['sira'])

# ================= 06 · çözünürlük tablosu · orta =================
cz=[('1-Bütanol',4,'7,7'),('1-Pentanol',5,'2,2'),('1-Heksanol',6,'0,6'),('1-Heptanol',7,'0,2')]
SK=tablo_svg(['Alkol','Karbon sayısı','Çözünürlük (g/100 g su)'],[[a,str(b),c] for a,b,c in cz])
sec=[('Karbon sayısı arttıkça apolar kısım büyür, çözünürlük azalır.',True,''),
     ('Karbon sayısı arttıkça alkol molekülünün su ile yaptığı hidrojen bağı sayısı artar.',False,'tablodaki alkollerin her birinde yalnız bir –OH grubu vardır, bu yüzden karbon sayısı hidrojen bağı sayısını artırmaz'),
     ('Mol kütlesi arttıkça alkollerin suda çözünürlüğü artar.',False,'tablodaki çözünürlükler mol kütlesi arttıkça azalmaktadır'),
     ('1-Heptanol, –OH grubu taşımadığı için suyla hidrojen bağı yapamaz.',False,'1-heptanolün –OH grubu vardır ve suyla hidrojen bağı yapabilir; çözünürlüğü düşük olmasının nedeni uzun apolar kısmıdır'),
     ('Tablodaki alkollerin tümü suda her oranda çözünür.',False,'tablodaki çözünürlükler sınırlıdır ve azalmaktadır')]
o=nk(tek(sec,True))
Q('0006','fiz','orta','tablo','Alkollerin suda çözünürlüğü','Alkollerin suda çözünürlüğünü hidroksil grubu ve hidrokarbon zincir uzunluğuyla ilişkilendirir.',
  'Alkolde –OH grubu suyla hidrojen bağı yaparak çözünmeyi sağlar; hidrokarbon zincir uzadıkça apolar kısım etkisini artırır ve çözünürlük azalır.','Çözünürlüğün –OH sayısıyla değil mol kütlesiyle arttığını sanmak.','çözünürlük tablosu',
  [A('Veriyi oku','Çözünürlük 7,7’den 0,2’ye düşüyor.','Karbon ↑ → çözünürlük ↓'),A('Yapıyı düşün','Hepsinde bir –OH grubu, zincir uzunluğu farklı.','–OH sayısı sabit'),A('Nedeni bul','Uzayan zincir apolar kısmı büyütür, suyla etkileşimi zayıflatır.','Apolar kısım ↑'),A('Şıkları ele','Verilerle çelişen ya da yapıya aykırı ifadeleri ele.','Doğru ifade: apolar kısım büyür')],
  metin='Aşağıdaki tabloda aynı sıcaklıkta bazı 1-alkanollerin (her birinde bir tane –OH grubu bulunur) 100 g suda çözünen yaklaşık kütleleri verilmiştir.\nBu verilere göre aşağıdakilerden hangisi söylenebilir?',
  sekil=SK,istenen='Verilerle uyumlu ifade.',ip=['Tüm alkollerde –OH sayısı aynıdır; değişen yapı parçasının suyla etkileşimini düşün.'],
  bilgi=[B('Alkoller ve su','Alkoldeki –OH grubu suyla hidrojen bağı yapar. Hidrokarbon zincir uzadıkça molekülün apolar kısmı büyür ve suda çözünürlük azalır. Örnek: etanol suda her oranda çözünür, uzun zincirli 1-dekanol ise çok az çözünür')],
  puf='Tablodaki değişimi, yapıda değişen kısımla ilişkilendir.',dogru=o['dogru'],yan=o['yan'],sira=yer(sec[0][0],[s[0] for s in sec[1:]],3))

# ================= 07 · yükseltgenme · orta · öncüllü =================
assert sinif(M_2BUT)=='sek' and sinif(M_2M2B)=='ter' and sinif(M_2M1P)=='prim'
SK=tk(sahne([[(M_2BUT,'K'),(M_2M2B,'L'),(M_2M1P,'M')]]))
d=dict(I=(False,'sekonder alkol (K) yükseltgenince aldehit değil keton oluşur'),
       II=(False,'tersiyer alkol (L) asitli KMnO₄ ile de yükseltgenmez; bu nedenle bu öncül yanlıştır'),
       III=(True,'primer alkol (M) önce aldehite, sonra karboksilik aside yükseltgenir'))
d['I']=(False,'K sekonder alkoldür, yükseltgenince keton oluşur; aldehit oluşmaz')
d['II']=(False,'L tersiyer alkoldür, yükseltgenme ürünü vermez; bu öncül yanlıştır')
d['III']=(True,'M primer alkoldür; önce aldehite, devamında karboksilik aside yükseltgenir')
o=OC(d,sr('Yalnız II','Yalnız III','I ve III','II ve III','I, II ve III')); assert o['dogru']=='Yalnız III'
Q('0007','yuk','orta','öncüllü','Alkollerin yükseltgenmesi','Primer, sekonder ve tersiyer alkollerin yükseltgenme ürünlerini ayırt eder.',
  'Primer alkol → aldehit → karboksilik asit; sekonder alkol → keton; tersiyer alkol yükseltgenmez.','Sekonder alkolün aldehit verdiğini ya da tersiyer alkolün yükseltgenebildiğini düşünmek.','K, L, M alkolleri',
  [A('Sınıfları bul','–OH taşıyan karbona bağlı karbon sayılarına bak.','K: 2° · L: 3° · M: 1°'),A('I’i değerlendir','Sekonder alkol keton verir.','K → keton → I yanlış'),A('II’yi değerlendir','Tersiyer alkolün –OH’li karbonunda H yoktur.','L yükseltgenmez → II yanlış'),A('III’ü değerlendir','Primer alkol aldehit, sonra asit verir.','M → aldehit → asit → III doğru')],
  metin='Şekilde iskelet formülleri verilen K, L ve M alkolleri, asitli KMnO₄ çözeltisiyle ayrı ayrı tepkimeye sokuluyor.\nI. K’nin yükseltgenme ürünü bir aldehittir.\nII. L yükseltgenerek keton oluşturur.\nIII. M’nin yükseltgenme ürünü daha ileri yükseltgenerek karboksilik asit verebilir.\nBuna göre bu yargılardan hangileri doğrudur?',
  sekil=SK,istenen='Doğru olan yargılar.',ip=['Her alkolün –OH taşıyan karbonunda kaç hidrojen kaldığına bak.'],
  bilgi=[B('Alkollerin yükseltgenmesi','Primer alkol yükseltgenince aldehit, aldehit de yükseltgenince karboksilik asit; sekonder alkol keton verir; tersiyer alkolün –OH taşıyan karbonunda H bulunmadığından yükseltgenmez. Örnek: 1-propanol → propanal → propanoik asit')],
  puf='–OH’li karbonda H varsa yükseltgenme olur; ürün, H sayısına göre değişir.',dogru=o['dogru'],yan=o['yan'],sira=o['sira'])

# ================= 08 · yükseltgenme şeması · orta =================
g=('\\node[draw,thick,rounded corners=3pt,minimum width=1.5cm,minimum height=.9cm] (x) at (0,0) {\\textbf{X}};\\node[draw,thick,rounded corners=3pt,minimum width=1.5cm,minimum height=.9cm] (y) at (4,0) {\\textbf{Y}};'
   '\\node[draw,thick,rounded corners=3pt,minimum width=1.5cm,minimum height=.9cm] (z) at (8,0) {\\textbf{Z}};'
   f'\\draw[{ARR},thick] (x) -- (y) node[midway,above,font=\\footnotesize\\sffamily] {{yükseltgenme}};\\draw[{ARR},thick] (y) -- (z) node[midway,above,font=\\footnotesize\\sffamily] {{yükseltgenme}};'
   '\\node[below=2pt of x,font=\\small] {\\ce{C4H10O}};\\node[below=2pt of y,font=\\small] {\\ce{C4H8O}};\\node[below=2pt of z,font=\\small] {\\ce{C4H8O2}};')
SK=tk(g)
dg='2-metil-1-propanol'
yan8=[('1-bütanol','Dallanmayı dikkate almamış; 1-bütanol de iki kez yükseltgenir ama ana zincirinde dallanma yoktur.','dikkat'),('2-bütanol','Sekonder alkolün keton verdikten sonra yükseltgenmeye devam edebileceğini düşünmüş; Y’nin yükseltgenip Z (asit) vermesi için X primer olmalıdır.','bilgi'),
      ('2-metil-2-propanol','Tersiyer alkolü seçmiş; tersiyer alkol yükseltgenmediği için Y oluşamaz.','bilgi'),('dietil eter','Eterlerin de iki kademede yükseltgenebileceğini sanmış; eter yükseltgenmeyle Y ve Z’yi vermez.','bilgi')]
Q('0008','yuk','orta','şekilli','Yükseltgenme ürünlerinden alkol belirleme','İki kademeli yükseltgenme şemasından alkolün sınıfını ve yapısını belirler.',
  'Alkol → karbonil → karboksilik asit zinciri yalnız primer alkolde görülür; dallanma bilgisi yapıyı tek seçeneğe indirir.','Zincirin sonundaki asidi görüp primer alkolü ve dallanma bilgisini birlikte kullanmayı atlamak.','yükseltgenme şeması',
  [A('Zincirin türünü anla','Z asit olduğuna göre Y aldehit olmalıdır.','X → aldehit → asit'),A('X’in sınıfı','Aldehit ve asit veren alkol primerdir.','X: primer alkol'),A('Formülü kullan','C₄H₁₀O’lu primer alkoller: 1-bütanol ve 2-metil-1-propanol.','İki aday'),A('Dallanmayı uygula','X’in ana zincirinde dallanma var.','2-metil-1-propanol')],
  metin='Aşağıda, C₄H₁₀O molekül formüllü X bileşiğinin art arda iki kez yükseltgenmesiyle önce Y, sonra Z bileşiklerinin oluştuğu gösterilmiştir. Z bileşiği karboksilik asittir ve X’in karbon iskeletinde dallanma vardır.\nBuna göre X bileşiğinin IUPAC adı aşağıdakilerden hangisidir?',
  sekil=SK,istenen='X bileşiğinin adı.',ip=['Z’nin karboksilik asit olması X’in hangi sınıftan alkol olması gerektiğini söyler.'],
  bilgi=[B('Ardışık yükseltgenme','Primer alkol (R–CH₂OH) önce aldehite (R–CHO), sonra karboksilik aside (R–COOH) yükseltgenir; aynı karbon iskeleti korunur. Örnek: etanol → etanal → etanoik asit')],
  puf='Alkolden asit oluşuyorsa alkol primerdir.',dogru=dg,yan=yan8,sira=yer(dg,[y[0] for y in yan8],0))

# ================= 09 · dehidrasyon · orta · öncüllü =================
g=('\\node[draw,thick,rounded corners=3pt,minimum height=.9cm,inner sep=5pt] (e) at (0,0) {Etanol};'
   '\\node[draw,thick,rounded corners=3pt,minimum height=.9cm,inner sep=5pt,anchor=west] (x) at (4.6,1.1) {\\textbf{X} + su};'
   '\\node[draw,thick,rounded corners=3pt,minimum height=.9cm,inner sep=5pt,anchor=west] (y) at (4.6,-1.1) {\\textbf{Y} + su};'
   f'\\draw[{ARR},thick] (e.east) -- (x.west) node[midway,above=3pt,sloped,font=\\footnotesize\\sffamily] {{derişik \\ce{{H2SO4}}, 140 $^\\circ$C}};'
   f'\\draw[{ARR},thick] (e.east) -- (y.west) node[midway,below=3pt,sloped,font=\\footnotesize\\sffamily] {{derişik \\ce{{H2SO4}}, 170 $^\\circ$C}};')
SK=tk(g)
d=dict(I=(False,'X, iki etanol molekülünden su çıkışıyla oluşan dietil eterdir; eterlerin molekülleri arasında hidrojen bağı bulunmaz'),
       II=(True,'Y, etanolden molekül içi su çıkışıyla oluşan etendir; çift bağ içerdiği için doymamış hidrokarbondur'),
       III=(False,'X moleküller arası su çıkışıyla oluşur; molekül içi su çıkışı Y’yi verir'))
o=OC(d,sr('Yalnız I','Yalnız II','Yalnız III','I ve II','II ve III')); assert o['dogru']=='Yalnız II'
Q('0009','eter','orta','şekilli','Alkolden eter ve alken eldesi','Sıcaklığa göre alkolün dehidrasyon ürününün eter ya da alken olduğunu ayırt eder.',
  'Derişik H₂SO₄ ile düşük sıcaklıkta (140 °C) moleküller arası su çıkışıyla eter, yüksek sıcaklıkta (170 °C) molekül içi su çıkışıyla alken oluşur.','Her iki sıcaklıkta da eter ya da her ikisinde de alken oluştuğunu düşünmek.','dehidrasyon şeması',
  [A('X’i belirle','140 °C’de iki alkol molekülü su kaybederek birleşir.','2 C₂H₅OH → C₂H₅OC₂H₅ + H₂O'),A('Y’yi belirle','170 °C’de tek alkol molekülü su kaybeder.','C₂H₅OH → C₂H₄ + H₂O'),A('I ve III’ü ele','X eter olduğundan hidrojen bağı yapmaz; X moleküller arası su çıkışıyla oluşur.','I yanlış · III yanlış'),A('II’yi doğrula','Y, çift bağlı eten olduğu için doymamıştır.','II doğru')],
  metin='Etanol, derişik H₂SO₄ varlığında iki farklı sıcaklıkta ısıtıldığında şekildeki gibi X ve Y organik ürünleri ile su oluşuyor.\nBuna göre,\nI. X’in molekülleri arasında hidrojen bağı bulunur.\nII. Y doymamış hidrokarbondur.\nIII. X, etanol moleküllerinin kendi içinde su kaybetmesiyle oluşur.\nyargılarından hangileri doğrudur?',
  sekil=SK,istenen='Doğru olan yargılar.',ip=['Hangi sıcaklıkta tek molekülden, hangisinde iki molekülden su çıkışı olduğunu düşün.'],
  bilgi=[B('Alkolün dehidrasyonu','Derişik H₂SO₄ ile 140 °C’de 2 R–OH → R–O–R + H₂O (eter); 170 °C’de alkol alkene dönüşür (molekül içi su çıkışı). Örnek: metanol 140 °C’de dimetil eter verir')],
  puf='Düşük sıcaklık eter, yüksek sıcaklık alken.',dogru=o['dogru'],yan=o['yan'],sira=o['sira'])

# ================= 10 · üç alkol karışımı · zor =================
alk={'metanol':'CH3OH','etanol':'CH3CH2OH','2-propanol':'CH3CH(OH)CH3'}
beta={'metanol':False,'etanol':True,'2-propanol':True}
eterler=list(combinations_with_replacement(alk,2)); alkenler=[a for a in alk if beta[a]]
assert len(eterler)==6 and len(alkenler)==2 and len(eterler)+len(alkenler)==8
SK=tk(sahne([[(M_METOH,'metanol'),(M_ETOH,'etanol'),(M_2P,'2-propanol')]]))
yan10=[(6,'Eter sayısını doğru bulmuş (6) ama alkenleri hiç saymamış; 170 °C’de etanol ve 2-propanol alken verir.','dikkat'),(5,'Yalnız farklı alkol çiftlerinden oluşan 3 eteri sayıp aynı alkolden oluşanları (dimetil, dietil, di-izopropil) atlamış; alkenleri 2 almış.','dikkat'),
       (7,'Eterleri 6 sayıp alkenleri 1 almış; etanol ve 2-propanol alken verir.','dikkat'),(9,'Metanolün de alken verebileceğini sanıp alkenleri 3 saymış; metanolde komşu karbon yoktur.','bilgi')]
Q('0010','eter','zor','şekilli','Alkol karışımından eter ve alken','Birden fazla alkolün karışımında oluşan eter ve alken sayısını dehidrasyon koşullarına göre bulur.',
  'Karışımda eter, alkol moleküllerinin ikili birleşmelerinden; alken ise her alkolün kendi içinde su kaybından oluşur.','Aynı alkolden oluşan eterleri saymamak; metanolden alken oluştuğunu sanmak.','alkol karışımı',
  [A('Eter sayısı','3 alkolün ikili birleşmeleri, aynı alkolün kendisiyle birleşmesi dahil sayılır.','3 + 3 = 6 eter'),A('Eterleri sırala','Dimetil, dietil, di-izopropil ve üç karışık eter.','6 eter'),A('Alkenleri bul','Alkenin oluşması için –OH’li karbonun komşusunda H olmalıdır.','metanol: yok · etanol: eten · 2-propanol: propen → 2 alken'),A('Toplamı yaz','Eter ve alken sayıları toplanır.','6 + 2 = 8')],
  metin='Şekilde iskelet formülleri verilen metanol, etanol ve 2-propanolden oluşan bir karışım iki ayrı deneyde ele alınıyor:\n• Derişik H₂SO₄ ile 140 °C’de ısıtıldığında eter oluşuyor.\n• Derişik H₂SO₄ ile 170 °C’de ısıtıldığında alken oluşuyor.\nBuna göre birinci deneyde oluşabilecek farklı eter sayısı ile ikinci deneyde oluşabilecek farklı alken sayısının toplamı kaçtır?',
  sekil=SK,istenen='Farklı eter sayısı + farklı alken sayısı.',ip=['Her koşulda hangi moleküllerin birleşip hangilerinin tek başına su kaybettiğini yaz.'],
  bilgi=[B('Karışımda dehidrasyon','140 °C’de iki alkol molekülü su kaybederek R–O–R′ eterini oluşturur; R ve R′ aynı ya da farklı olabilir. 170 °C’de her alkol molekülü kendi içinde su kaybeder ve alken oluşur; –OH’li karbonun komşusunda H bulunmalıdır')],
  puf='Oluşabilecek tüm ürünleri koşula göre ayrı ayrı listele.',dogru=8,yan=yan10)

# ================= 11 · eter adlandırma · orta · şekil =================
dg='2-etoksipropan'
yan11=[('1-etoksipropan','Propan zincirinde etoksi grubunun bağlandığı karbonu 1 almış; bağlanma ortadaki (2.) karbondadır.','dikkat'),('2-metoksibütan','Ana zincir olarak bütanı seçip kısa kolu metoksi sanmış; verilen yapıda kollar 2 ve 3 karbonludur.','bilgi'),
       ('1-metoksi-2-metilpropan','Yapıdaki dallanmayı yanlış yerde kurup başka bir C₅H₁₂O izomerini yazmış.','bilgi'),('etoksietan','Karbon sayısını eksik sayıp dietil eterin adını yazmış.','islem')]
SK=tk(sahne([[(M_EOIP,None)]]))
Q('0011','ad','orta','şekilli','Eter adlandırma','İskelet formülü verilen eteri alkoksialkan kuralına göre adlandırır.',
  'Eterde uzun karbon zinciri ana zincir, kısa alkil kolu oksijenle birlikte alkoksi grubu olarak adlandırılır (alkoksialkan).','Ana zincir olarak kısa kolu seçmek ya da alkoksi grubunun bağlandığı karbonun konumunu yanlış yazmak.','alkoksialkan adlandırma',
  [A('Kolları ayır','Oksijenin iki yanındaki karbon gruplarını ayrı say.','Bir yanda 2 karbon (etil), öbür yanda 3 karbon'),A('Ana zinciri seç','Uzun kol ana zincirdir, kısa kol alkoksi olur.','Ana zincir: propan · kol: etoksi'),A('Konumu bul','Oksijenin bağlandığı karbonun numarası.','Ortadaki karbon: 2'),A('Adı yaz','Alkoksi grubu, konum ve ana zincir birleştirilir.','2-etoksipropan')],
  metin='Şekildeki iskelet formülünde oksijen atomu iki karbon grubunu birbirine bağlamaktadır; köşe ve uçlar karbondur.\nBu eter, alkoksialkan kuralına göre hangi adla anılır?',
  sekil=SK,istenen='Eterin IUPAC adı.',ip=['Oksijenin iki yanındaki karbon gruplarından hangisinin ana zincir olacağına, hangisinin alkoksi grubuna karşılık geleceğine karar ver.'],
  bilgi=[B('Eter adlandırma','Eterler R–O–R′ yapısındadır. IUPAC’ta uzun zincir ana zincirdir, oksijenli kısa kol alkoksi (metoksi, etoksi…) olarak ön ek alır: CH₃–O–CH₂CH₂CH₃ → 1-metoksipropan. Basit adlarda iki alkil adı ve “eter” yazılır: etil propil eter')],
  puf='Eterde uzun kol ana zincir, kısa kol “alkoksi”.',dogru=dg,yan=yan11,sira=yer(dg,[y[0] for y in yan11],3))

# ================= 12 · sekonder değildir · orta · olumsuz =================
sp=dict(K=M_2P,L=M_3P,M=M_2M1P,N=M_3M2B,P=M_2BUT)
assert [k for k,v in sp.items() if sinif(v)!='sek']==['M']
SK=tk(sahne([[(sp['K'],'K'),(sp['L'],'L'),(sp['M'],'M')],[(sp['N'],'N'),(sp['P'],'P')]],bosluk=1.0,satir_ara=.9))
yan12=[('K','K’de –OH’yi uçtaki karbonda sanıp primer saymış; oysa –OH ortadaki karbondadır ve karbon iki karbona bağlıdır, K sekonderdir.','bilgi'),('L','3-pentanolde uzun zinciri görüp –OH’li karbona üç karbon bağlı saymış; oysa iki karbona bağlıdır, L sekonderdir.','bilgi'),('N','N’deki metil dalını –OH’li karbona bağlı sayıp tersiyer sanmış; dal komşu karbondadır, –OH’li karbon iki karbona bağlıdır ve N sekonderdir.','bilgi'),('P','P’deki etil kolunu görünce –OH’li karbona üç karbon bağlı sanmış; oysa iki karbona bağlıdır, P sekonderdir.','bilgi')]
Q('0012','sinif','orta','şekilli','Sekonder alkol belirleme','Dallanmış yapılarda –OH’li karbonun komşu karbon sayısını sayarak alkol sınıfını bulur.',
  'Dallanma, alkolün sınıfını belirlemez; yalnız –OH taşıyan karbona doğrudan bağlı karbon sayısı önemlidir.','Dallanmış zincirde –OH’nin yakınındaki dalı sayıp primer alkolü sekonder sanmak.','K, L, M, N, P alkolleri',
  [A('Sınıfı belirleme ölçütü','–OH’li karbona bağlı karbon sayısı sayılır.','1 → primer · 2 → sekonder · 3 → tersiyer'),A('K, L, N, P’yi incele','Bu dördünde –OH’li karbon iki karbona bağlı.','K, L, N, P: sekonder'),A('M’yi incele','–OH’li karbon yalnız CH karbonuna bağlı, dal ondan sonra başlıyor.','M primer'),A('Sonuç','Sekonder olmayan alkol M’dir.','M')],
  metin='K, L, M, N ve P alkollerinin yapıları şekilde gösterilmiştir.\nBu alkollerden hangisi sekonder (2°) alkol değildir?',
  sekil=SK,istenen='Sekonder olmayan alkol.',ip=['Her alkolde –OH’nin bağlandığı karbonun doğrudan kaç karbonla komşu olduğunu say; dalın uzaklığı sonucu değiştirmez.'],
  bilgi=[B('Sınıfı belirleyen karbon','Alkolün sınıfı yalnızca –OH’nin bağlandığı karbona doğrudan bağlı karbon sayısına bağlıdır. Örnek: 2-metil-1-bütanolde –OH’li karbon tek karbona bağlıdır; dal uzakta olsa da alkol primerdir')],
  puf='Dal uzakta kalırsa sınıf değişmez; yalnız –OH’li karbonun komşularını say.',dogru='M',yan=yan12,sira=yer('M',[y[0] for y in yan12],4))

# ================= 13 · C3H8O izomerleri · orta · öncüllü =================
assert formul(M_1P)==formul(M_2P)==formul(M_MOET)==(3,8,1) and IZ[3]=={'prim':1,'sek':1,'ter':0,'eter':1}
SK=tk(sahne([[(M_1P,'I'),(M_2P,'II'),(M_MOET,'III')]]))
d=dict(I=(False,'I ile II’nin farkı –OH grubunun konumudur; bu konum izomerliğidir, zincir izomerliği değildir'),
       II=(True,'II (alkol) ile III (eter) farklı fonksiyonel gruba sahiptir; fonksiyonel grup izomeridirler'),
       III=(True,'I, II ve III’ün üçü de C₃H₈O formüllüdür; bu formülün bütün yapı izomerleridir'))
d['II']=(False,'II alkol, III eter olduğundan farkları –OH konumu değil fonksiyonel gruptur; konum izomeri değildirler')
d['III']=(True,'üç bileşiğin de molekül formülü C₃H₈O’dur')
d['I']=(False,'I ile II’de karbon iskeleti aynı, –OH’nin yeri farklıdır; bu konum izomerliğidir')
del d  # nihai öncüller aşağıda
d=dict(I=(False,'I ile II’nin karbon iskeleti aynıdır, yalnız –OH’nin yeri farklıdır; bu konum izomerliğidir, zincir izomerliği değil'),
       II=(False,'II alkol, III eterdir; aralarındaki fark fonksiyonel gruptur, konum izomerliği değildir'),
       III=(True,'I, II ve III’ün molekül formülü C₃H₈O’dur'))
o=OC(d,sr('Yalnız III','I ve II','I ve III','II ve III','I, II ve III')); assert o['dogru']=='Yalnız III'
Q('0013','izo','orta','öncüllü','Alkol–eter izomerliği','Aynı molekül formüllü alkol ve eterlerde zincir, konum ve fonksiyonel grup izomerliğini ayırt eder.',
  'Alkol ile eter fonksiyonel grup izomeridir; –OH yeri değişen alkoller konum izomeridir; karbon iskeleti değişirse zincir izomerliği vardır.','Konum izomerini zincir izomeri, fonksiyonel grup izomerini konum izomeri sanmak.','C₃H₈O izomerleri',
  [A('Formülleri say','Üç bileşiğin C ve H sayılarını yazıp karşılaştır.','Hepsi C₃H₈O'),A('I ve II’yi karşılaştır','Karbon iskeleti aynı, –OH’nin yeri farklı.','Konum izomeri → I yanlış'),A('II ve III’ü karşılaştır','Biri alkol, diğeri eter.','Fonksiyonel grup izomeri → II yanlış'),A('Sonuç','Yalnız III doğru.','III doğru')],
  metin='Yapıları şekilde gösterilen I, II ve III bileşiklerinin üçü de C₃H₈O molekül formüllüdür.\nI. I ile II zincir izomeridir.\nII. II ile III konum izomeridir.\nIII. I, II ve III birbirinin yapı izomeridir.\nBuna göre bu yargılardan hangileri doğrudur?',
  sekil=SK,istenen='Doğru olan yargılar.',ip=['Her çiftte neyin değiştiğine bak: karbon iskeleti mi, –OH yeri mi, fonksiyonel grup mu?'],
  bilgi=[B('Yapı izomerliği türleri','Aynı molekül formülüne sahip farklı yapılar yapı izomeridir: zincir izomerinde karbon iskeleti, konum izomerinde fonksiyonel grubun yeri, fonksiyonel grup izomerinde fonksiyonel grup farklıdır. Örnek: 1-bütanol ile 2-bütanol konum izomeridir')],
  puf='İskelet aynı, yer farklıysa konum; sınıf farklıysa fonksiyonel grup izomeri.',dogru=o['dogru'],yan=o['yan'],sira=o['sira'])

# ================= 14 · C5H12O primer sayısı · orta =================
yan14=[(1,'Tersiyer alkol sayısını (1) primer sanmış; primer alkol 4 tanedir.','bilgi'),(3,'Sekonder alkol sayısını (3) primer sanmış ya da 2,2-dimetil-1-propanolü atlamış.','dikkat'),(5,'Primer ve tersiyer alkolleri toplamış (4 + 1); soruda yalnız primer isteniyor.','dikkat'),(8,'Alkollerin tümünü (4 + 3 + 1) saymış; primer alkoller yalnız 4 tanedir.','dikkat')]
assert IZ[5]['prim']==4 and IZ[5]['sek']==3 and IZ[5]['ter']==1
Q('0014','izo','orta','düz','Alkol izomerlerini sayma','C₅H₁₂O formüllü alkollerin izomerlerini sınıflandırıp primer olanları sayar.',
  'Pentanın üç karbon iskeleti üzerinde –OH’nin olası yerleri taranır; –OH’li karbona komşu karbon sayısına göre sınıflandırılır.','Aynı yapıyı iki kez saymak ya da dallı iskeletlerde –OH’nin olası yerlerini atlamak.','C₅H₁₂O alkol izomerleri',
  [A('İskeletleri yaz','5 karbonlu üç iskelet: n-pentan, 2-metilbütan, 2,2-dimetilpropan.','3 iskelet'),A('–OH’yi yerleştir','Her iskelette farklı konumlara –OH koy, eş yapıları ele.','Toplam 8 alkol'),A('Sınıflandır','–OH’li karbona komşu karbon sayısına bak.','primer 4 · sekonder 3 · tersiyer 1'),A('Primerleri seç','İstenen yalnız primer alkollerdir.','4')],
  metin='Stereoizomerler ayrı sayılmayacaktır.\nC₅H₁₂O molekül formüllü bileşiklerden alkol olanlar arasında kaç tanesi primer (1°) alkoldür?',
  istenen='Primer alkol izomerlerinin sayısı.',ip=['Önce 5 karbonlu üç farklı karbon iskeletini yaz; sonra her iskelette –OH’nin uçtaki, ortadaki ve dallı karbonlardaki yerlerini tara.'],
  bilgi=[B('Alkol izomerlerini sayma','Karbon iskeletleri çizilir, –OH grubu tüm olası karbonlara yerleştirilir ve aynı çıkanlar atılır. Örnek: C₃H₈O için 2 alkol vardır: 1-propanol ve 2-propanol')],
  puf='Önce iskeletleri, sonra –OH konumlarını sistemli tara.',dogru=4,yan=yan14)

# ================= 15 · tersiyer bütanol · orta · olumsuz =================
sec=[('Tersiyer alkoldür.',True,'–OH’li karbon üç karbona bağlıdır'),('Molekül formülü C₄H₁₀O’dur.',True,'4 karbon ve 1 oksijenli doymuş alkoldür'),
     ('Asitli KMnO₄ ile yükseltgenince keton oluşur.',False,''),('2-metil-2-propanol adını alır.',True,'ana zincir 3 karbonlu, metil 2. karbonda ve –OH 2. karbondadır'),
     ('1-bütanolün yapı izomeridir.',True,'ikisinin de formülü C₄H₁₀O’dur, yapıları farklıdır')]
o=nk(tek(sec,False))
SK=tk(sahne([[(M_TBUT,'X')]]))
Q('0015','yuk','orta','şekilli','Tersiyer alkolün özellikleri','Tersiyer alkolün sınıfını, adını, izomerini ve yükseltgenmeme özelliğini birlikte değerlendirir.',
  'Tersiyer alkolün –OH’li karbonunda H yoktur; yükseltgenmez. Keton, ancak sekonder alkolden oluşur.','Tersiyer alkolün de keton verdiğini düşünmek.','tersiyer bütanol',
  [A('X’i tanı','Merkez karbonda –OH ve üç metil grubu vardır.','Tersiyer alkol'),A('Adı ve formülü','Ana zincir propan, –OH ve metil 2. karbonda.','2-metil-2-propanol · C₄H₁₀O'),A('İzomerlik','1-bütanol de C₄H₁₀O’dur.','İzomer'),A('Yükseltgenmeyi sorgula','Tersiyer alkolün –OH’li karbonunda H yok.','Yükseltgenmez → keton ifadesi yanlış')],
  metin='Yapısı şekilde gösterilen X alkolü ile ilgili olarak aşağıdakilerden hangisi yanlıştır?',
  sekil=SK,istenen='Yanlış olan ifade.',ip=['–OH taşıyan karbonda hidrojen kalıp kalmadığına bak.'],
  bilgi=[B('Tersiyer alkol','Tersiyer alkolün –OH taşıyan karbonunda hidrojen bulunmaz; bu nedenle ılımlı koşullarda yükseltgenmez. Primer alkol aldehit/asit, sekonder alkol keton verir. Örnek: 2-metil-2-bütanol yükseltgenme ürünü vermez')],
  puf='Alkolün sınıfını belirleyip yükseltgenme ürününü ona göre yorumla.',dogru=sec[2][0],yan=o['yan'],sira=yer(sec[2][0],[s[0] for s in sec if s[1]],4))

# ================= 16 · C4H10O izomerleri · zor · öncüllü =================
assert IZ[4]['prim']+IZ[4]['sek']+IZ[4]['ter']==4 and IZ[4]['eter']==3 and sum(IZ[4].values())==7
d=dict(I=(True,'C₄H₁₀O için 4 alkol (1-bütanol, 2-bütanol, 2-metil-1-propanol, 2-metil-2-propanol) ve 3 eter olmak üzere 7 yapı izomeri vardır'),
       II=(False,'eter izomerlerinin sayısı 3’tür ve alkol izomerlerinden (4) azdır'),
       III=(True,'yükseltgenince keton veren yalnız sekonder alkol 2-bütanoldür'))
o=OC(d,sr('Yalnız I','Yalnız II','I ve III','II ve III','I, II ve III')); assert o['dogru']=='I ve III'
Q('0016','izo','zor','öncüllü','C₄H₁₀O izomerleri ve yükseltgenme','C₄H₁₀O’nun alkol ve eter izomerlerini sayıp yükseltgenme ürünleriyle ilişkilendirir.',
  'Alkol ve eter izomerleri ayrı ayrı sayılır; yükseltgenme ürünü alkolün sınıfına göre değişir.','İzomer sayısını yanlış saymak; eterleri alkolden fazla sanmak; tersiyer alkolü yükseltgenebilir saymak.','C₄H₁₀O izomerleri',
  [A('Alkolleri yaz','Bütanın iki iskeleti üzerinde –OH konumlarını tara.','4 alkol: 2 primer, 1 sekonder, 1 tersiyer'),A('Eterleri yaz','O atomunu karbon zincirine yerleştir.','dietil, metil propil, metil izopropil → 3 eter'),A('I’i ve II’yi değerlendir','Toplam 4 + 3 = 7; eter sayısı alkoldan az.','I doğru · II yanlış'),A('III’ü değerlendir','Keton yalnız sekonder alkolden gelir.','Sekonder alkol 1 tane → III doğru')],
  metin='C₄H₁₀O molekül formülüne sahip, her biri yalnız tek bağlı bileşiklerden oluşan yapı izomerleri ile ilgili,\nI. Toplam yedi tane yapı izomeri vardır.\nII. Eter olan izomerlerin sayısı, alkol olan izomerlerin sayısından fazladır.\nIII. Uygun yükseltgenle yükseltgenince keton oluşturabilen yalnız bir izomer vardır.\nyargılarından hangileri doğrudur?',
  istenen='Doğru olan yargılar.',ip=['Alkolleri –OH konumuna, eterleri iki yandaki karbon gruplarına göre ayrı ayrı sayarak başla.'],
  bilgi=[B('İzomerleri sayarken','Alkol izomerleri karbon iskeleti ve –OH konumuyla, eter izomerleri oksijenin iki yanındaki karbon dağılımıyla sayılır; aynı yapının dönmüş hâlini iki kez sayma. Örnek: C₃H₈O için 2 alkol ve 1 eter, toplam 3 izomer vardır')],
  puf='İzomerleri sınıflarına ayırıp tek tek say.',dogru=o['dogru'],yan=o['yan'],sira=o['sira'])

# ================= 17 · tablo · tanıma · zor =================
SK=tablo_svg(['Madde','Na metali ile','Asitli KMnO₄ ile'],[['K','H₂ gazı çıkar','Keton oluşur'],['L','H₂ gazı çıkar','Yükseltgenmez'],['M','Tepkime vermez','Yükseltgenmez']])
dg='K: 2-bütanol, L: 2-metil-2-propanol, M: dietil eter'
yan17=[('K: 1-bütanol, L: 2-metil-2-propanol, M: dietil eter','K’nin keton verdiğini atlayıp primer alkol seçmiş; 1-bütanol aldehit ve asit verir.','bilgi'),
       ('K: 2-bütanol, L: dietil eter, M: 2-metil-2-propanol','L ile M’yi karıştırmış; Na ile H₂ çıkaran L alkol, tepkime vermeyen M eterdir.','dikkat'),
       ('K: 2-bütanol, L: 2-metil-2-propanol, M: 1-bütanol','M’yi Na ile H₂ vermeyen bileşik olarak 1-bütanol seçmiş; 1-bütanol Na ile H₂ verir ve yükseltgenir.','bilgi'),
       ('K: 2-metil-1-propanol, L: 2-bütanol, M: dietil eter','Yükseltgenmeyen L için sekonder alkol seçmiş; sekonder alkol keton verir.','bilgi')]
Q('0017','yuk','zor','tablo','Deney sonuçlarından C₄H₁₀O bileşiklerini belirleme','Na ve yükseltgen deney sonuçlarından alkol–eter ayrımı ile alkol sınıfını birlikte çıkarır.',
  'Na ile H₂ çıkışı –OH varlığını (alkol); yükseltgenme ürünü ise alkolün sınıfını gösterir. Eter her iki testte de tepkime vermez.','Yükseltgenmeyen bileşiği eter, keton oluşturanı primer alkol sanmak.','deney tablosu',
  [A('Na testini yorumla','Na ile H₂ çıkaran K ve L alkoldür; M alkol değildir.','K, L: alkol · M: eter'),A('K’yi belirle','Keton veren alkol sekonderdir.','K: 2-bütanol'),A('L’yi belirle','Alkol olup yükseltgenmeyen tersiyerdir.','L: 2-metil-2-propanol'),A('M’yi belirle','C₄H₁₀O’lu eter, simetrik olanı seçilir.','M: dietil eter')],
  metin='K, L ve M bileşiklerinin hepsinin molekül formülü C₄H₁₀O’dur. Bu bileşikler üzerinde yapılan deneylerin sonuçları aşağıdaki tabloda verilmiştir. M’nin simetrik yapılı bir bileşik olduğu bilinmektedir.\nBuna göre K, L ve M bileşikleri aşağıdakilerden hangisidir?',
  sekil=SK,istenen='K, L ve M bileşiklerinin adları.',ip=['Önce Na ile verdiği sonuca bakarak hangisinin alkol olmadığını bul; sonra alkollerin yükseltgenme sonuçlarını yorumla.'],
  bilgi=[B('Alkol ve eterin ayırt edilmesi','Alkoller Na metaliyle H₂ gazı çıkararak tepkime verir (2 R–OH + 2 Na → 2 R–ONa + H₂); eterler vermez. Yükseltgenmede ürün alkolün sınıfına göre değişir. Örnek: etanol Na ile H₂ verir, dimetil eter vermez')],
  puf='Na ile H₂ çıkarıyorsa alkoldür; sonra yükseltgenmesine bak.',dogru=dg,yan=yan17,sira=yer(dg,[y[0] for y in yan17],1))

# ================= 18 · Na + karışım · zor · düzenek =================
mE=46; mD=23; MF=46
nE=Fr(mE,MF); nH2=nE/2; V=nH2*Fr(224,10); assert V==Fr(112,10)
V22=Fr(224,10)
assert Fr(mE+mD,MF)/2*V22==Fr(168,10) and nE*V22==Fr(224,10) and Fr(mE+mD,MF)*V22==Fr(336,10) and Fr(mD,MF)/2*V22==Fr(56,10)
yan18=[(Fr(168,10),'Karışımın tamamını (1,5 mol) alkol sanmış: 0,75 mol H₂ → 16,8 L.','bilgi'),(Fr(224,10),'Yalnız etanolü almış ama 1 mol etanole 1 mol H₂ düştüğünü sanmış: 22,4 L.','islem'),
       (Fr(336,10),'Hem tüm karışımı alkol almış hem de ½ katsayısını unutmuş: 1,5 mol H₂ → 33,6 L.','islem'),(Fr(56,10),'Tepkime veren maddeyi karıştırmış: dimetil eteri (0,5 mol) alkol sanıp ½ ile 0,25 mol H₂ → 5,6 L bulmuş.','bilgi')]
g=('\\fill[vurgu!15] (0,0) -- (2,0) -- (1.55,1.0) -- (.45,1.0) -- cycle;\\draw[thick] (0,0) -- (2,0) -- (1.5,1.7) -- (1.5,2.1) -- (.5,2.1) -- (.5,1.7) -- cycle;'
   '\\draw[thick] (.45,1.0) -- (1.55,1.0);\\draw[thick] (.45,2.1) rectangle (1.55,2.35);\\fill (.7,.2) circle (.08);\\fill (1.2,.3) circle (.08);\\node[font=\\scriptsize] at (1.0,.62) {Na};'
   '\\node[align=center,font=\\small] at (1.0,-.8) {46 g \\ce{C2H5OH}\\\\ 23 g \\ce{CH3OCH3}\\\\ fazla Na};'
   '\\fill[vurgu!15] (3.6,-.2) rectangle (6.8,1.1);\\draw[thick] (3.6,1.5) -- (3.6,-.2) -- (6.8,-.2) -- (6.8,1.5);'
   '\\fill[vurgu!15] (4.85,.3) rectangle (5.55,1.9);\\draw[thick] (4.85,.3) -- (4.85,3.0) -- (5.55,3.0) -- (5.55,.3);'
   '\\draw[thick] (1.0,2.35) -- (1.0,3.5) -- (4.3,3.5) -- (4.3,.2) -- (5.2,.2) -- (5.2,1.0);'
   '\\node[font=\\small] at (5.2,2.45) {\\ce{H2}};\\node[font=\\small,anchor=west] at (5.75,2.45) {NŞA};')
SK=tk(g)
Q('0018','yuk','zor','şekilli','Na ile tepkime ve gaz hacmi','Alkol–eter karışımında yalnız alkolün Na ile tepkime verdiğini kullanarak H₂ hacmini hesaplar.',
  'Alkol Na ile 2 R–OH + 2 Na → 2 R–ONa + H₂ tepkimesini verir; eter vermez. Etanol ve dimetil eter aynı mol kütleli olsa da yalnız etanol H₂ üretir.','Karışımın tamamının tepkime verdiğini düşünmek ya da H₂ katsayısındaki ½’yi unutmak.','Na ile H₂ eldesi',
  [A('Tepkimeyi yaz','Alkol Na ile H₂ verir, eter vermez.','2 C₂H₅OH + 2 Na → 2 C₂H₅ONa + H₂'),A('Alkol molünü bul','Mol kütlesi: C₂H₅OH = 2×12 + 6×1 + 16 = 46 g/mol.','46 ÷ 46 = 1 mol etanol'),A('H₂ molünü bul','2 mol alkolden 1 mol H₂ çıkar.','1 ÷ 2 = 0,5 mol H₂'),A('Hacmi hesapla','NŞA’da 1 mol gaz 22,4 L.','0,5 × 22,4 = 11,2 L')],
  metin='Şekildeki düzenekte kütlece 46 g etanol (C₂H₅OH) ve 23 g dimetil eter (CH₃OCH₃) içeren karışıma fazla miktarda Na metali ekleniyor. Tepkime tamamlanınca açığa çıkan H₂ gazı su altında toplanıyor.\n(H: 1, C: 12, O: 16; NŞA’da 1 mol gazın hacmi 22,4 L)\nBuna göre toplanan H₂ gazının NŞA’daki hacmi kaç litredir?',
  sekil=SK,istenen='H₂ gazının NŞA’daki hacmi (L).',ip=['Karışımdaki maddelerden hangisinin Na ile tepkime verdiğini önce belirle.'],
  bilgi=[B('Alkol–sodyum tepkimesi','Alkoller Na ile alkoksit ve H₂ oluşturur: 2 R–OH + 2 Na → 2 R–ONa + H₂. Eterlerde –OH bulunmadığından tepkime olmaz. Örnek: 2 mol metanolden 1 mol H₂ çıkar')],
  puf='Yalnız –OH’li madde Na ile H₂ verir; 2 mol alkole 1 mol H₂ düşer.',dogru=Fr(112,10),yan=yan18)

# ================= 19 · kaynama noktası sıralaması · zor · şekil =================
bp={'K':117,'L':99,'M':82,'N':35}
assert bp['K']>bp['L']>bp['M']>bp['N']
assert sinif(M_1B)=='prim'
SK=tk(sahne([[(M_1B,'K'),(M_2BUT,'L'),(M_TBUT,'M'),(M_DEE,'N')]],bosluk=.9))
dg='K > L > M > N'
yan19=[('K > L > N > M','Dallı tersiyer alkolün (M) etkileşimini eterden zayıf saymış; M de hidrojen bağı yapar ve eterden yüksek sıcaklıkta kaynar.','bilgi'),
       ('L > K > M > N','Dallanma etkisini ters kurmuş: dallanma yüzey alanını azaltır, kaynama noktasını düşürür; dallanmamış K en yüksek olmalıdır.','bilgi'),
       ('N > M > L > K','Sıralamayı ters yazmış; hidrojen bağı yapan alkoller eterden yüksek sıcaklıkta kaynar.','dikkat'),
       ('M > L > K > N','Daha dallı alkolün daha yüksek kaynayacağını sanmış; dallanma London kuvvetlerini azaltır.','bilgi')]
Q('0019','fiz','zor','şekilli','Yapı izomerlerinin kaynama noktası','Aynı formüllü alkol ve eterin kaynama noktalarını hidrojen bağı ve dallanma etkisiyle sıralar.',
  'Aynı formüllü bileşiklerde hidrojen bağı yapan alkol, eterden yüksek kaynar; alkoller arasında dallanma arttıkça kaynama noktası düşer.','Yalnız hidrojen bağına bakıp dallanma etkisini atlamak ya da eteri alkollerin üstünde görmek.','C₄H₁₀O izomerleri sırası',
  [A('Grupları ayır','K, L, M alkol; N eter.','Alkoller > eter (H bağı)'),A('Alkolleri sırala','Dallanma arttıkça temas yüzeyi ve London kuvvetleri azalır.','K (dallanmamış) > L > M (en dallı)'),A('Eteri ekle','N hidrojen bağı yapmaz.','N en düşük'),A('Sıralamayı yaz','Büyükten küçüğe.','K > L > M > N')],
  metin='Yapıları şekilde gösterilen K, L, M ve N bileşiklerinin molekül formülü C₄H₁₀O’dur.\nBu bileşikler normal kaynama noktalarına göre büyükten küçüğe nasıl sıralanır?',
  sekil=SK,istenen='Kaynama noktası sıralaması (büyükten küçüğe).',ip=['Önce hidrojen bağı yapabilenleri ayır; sonra aralarında zincirdeki dallanmanın etkisini düşün.'],
  bilgi=[B('İzomerlerde kaynama noktası','Aynı formüllü izomerlerde hidrojen bağı yapanlar yüksek kaynar. Hidrokarbon kısımda dallanma arttıkça molekül küreselleşir, temas yüzeyi azalır ve kaynama noktası düşer. Örnek: pentan ile 2,2-dimetilpropan karşılaştırıldığında dallı olan daha düşük kaynar')],
  puf='Önce hidrojen bağı, sonra dallanma: dallanma arttıkça kaynama noktası düşer.',dogru=dg,yan=yan19,sira=yer(dg,[y[0] for y in yan19],4))

# ================= 20 · X şeması · zor · öncüllü =================
g=('\\node[inner sep=0pt] at (0,0) {};')
mgx,bbx=mol_ciz(M_2BUT,0.2,0.0)
g=(mgx+'\\node[font=\\small\\bfseries] at (1.0,-.65) {X};'
   '\\node[draw,thick,rounded corners=3pt,minimum width=1.2cm,minimum height=.9cm,anchor=west] (y) at (5.1,1.0) {\\textbf{Y}};'
   '\\node[draw,thick,rounded corners=3pt,minimum width=1.2cm,minimum height=.9cm,anchor=west] (z) at (5.1,-1.0) {\\textbf{Z} + su};'
   f'\\draw[{ARR},thick] (2.75,.3) -- (y.west) node[midway,above=2pt,sloped,font=\\footnotesize\\sffamily] {{asitli \\ce{{KMnO4}}}};'
   f'\\draw[{ARR},thick] (2.75,.0) -- (z.west) node[midway,below=2pt,sloped,font=\\footnotesize\\sffamily] {{\\ce{{H2SO4}}, 140 $^\\circ$C}};')
SK=tk(g)
d=dict(I=(True,'X’te –OH’li karbon iki karbona bağlıdır; X sekonder alkoldür'),
       II=(True,'sekonder alkolün yükseltgenme ürünü olan Y bir ketondur (C₄H₈O); keton, ılımlı yükseltgenle daha ileri yükseltgenmez'),
       III=(False,'iki X molekülü bir su çıkararak Z’yi verir: 2 C₄H₁₀O − H₂O = C₈H₁₈O olur, C₈H₁₆O değil'))
d['II']=(True,'Y, C₄H₈O formüllü 2-bütanondur (keton)')
yan_d=d
o=OC(d,sr('Yalnız I','Yalnız II','I ve II','II ve III','I, II ve III')); assert o['dogru']=='I ve II'
Q('0020','yuk','orta','öncüllü','Alkolün yükseltgenme ve eter ürünleri','Aynı alkolün yükseltgenme ve dehidrasyon ürünlerini formül ve sınıf bakımından birlikte değerlendirir.',
  'Yükseltgenme ve dehidrasyon ürünlerinin formülleri, kaybolan atomlar izlenerek bulunur.','Eter formülünü bulurken suyu çıkarmayı ya da molekül sayısını (2 alkol) unutmak.','2-bütanol şeması',
  [A('X’i sınıflandır','–OH’li karbon iki karbona bağlı.','X: sekonder alkol (C₄H₁₀O)'),A('Y’yi bul','Sekonder alkol yükseltgenince keton olur, 2 H kaybeder.','Y: C₄H₈O, keton'),A('Z’yi bul','140 °C’de iki alkol bir H₂O çıkararak birleşir.','2 C₄H₁₀O − H₂O = C₈H₁₈O'),A('Yargıları birleştir','I ve II uyumlu, III’teki formül hidrojen sayısında hatalı.','I ve II')],
  metin='Şekilde yapısı gösterilen X alkolü, asitli KMnO₄ ile yükseltgenince Y’yi; derişik H₂SO₄ ile 140 °C’de ısıtılınca Z eterini ve su veriyor.\nI. X sekonder alkoldür.\nII. Y’nin molekül formülü C₄H₈O’dur.\nIII. Z’nin molekül formülü C₈H₁₆O’dur.\nBuna göre bu yargılardan hangileri doğrudur?',
  sekil=SK,istenen='Doğru olan yargılar.',ip=['Yükseltgenmede kaybolan atomlarla dehidrasyonda kaybolan atomları ayrı ayrı yaz.'],
  bilgi=[B('Formül hesabı','Yükseltgenme (alkol → keton/aldehit): molekülden 2 H gider. Eter oluşumu: 2 alkol → eter + H₂O. Örnek: C₃H₈O yükseltgenince C₃H₆O; iki C₃H₈O’dan eter oluşunca C₆H₁₄O verir')],
  puf='Ürün formülünü, tepkimede kaybolan atomları sayarak kontrol et.',dogru=o['dogru'],yan=o['yan'],sira=o['sira'])

# ---------- yaz ----------
for x in P.ANA: x['kardes']=None
SCR=os.environ.get('SCRATCH','/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/alk')
os.makedirs(SCR,exist_ok=True)
P.yaz(os.path.join(GD,'alkol-1.json'),os.path.join(SCR,'bos-alkol.json'))
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=KEY))['kartlar'].append(c['id'])
json.dump(dict(konu=KONU_AD,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2018–2026 Kimya, MEB 12. sınıf Organik Bileşikler.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','akalkol.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
