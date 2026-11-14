"""TYT Biyoloji PİLOT · 6 şekilli soru (kardeş yok, ipucu 1). Şekiller TikZ/pgfplots (cizim.tikz_svg); soyağacı, besin ağı, bölünme evreleri ve grafik
verileri Python'da hesaplanır/taranır; her doğru şık ve her çeldirici bu verilerden assert edilir."""
import sys,os,math,json,random,itertools
BD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(BD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
P=Parti('biopilot','Biyoloji','bio|Kalıtım',ders='TYT Biyoloji',idon='tytbio')
TIPK={}
KY='ÖSYM 2018–2026 TYT Biyoloji dağılımı · MEB 9–10. sınıf biyoloji'
def konu(k,ad): P.k=k; P.konu_adi=ad; H.KONU=ad
def kartla(id,alt,fikir,tuzak,z,adim,tipId,tip,kalip='şekilli'):
    kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY); TIPK[tipId]=P.k
def q(no,ad,kalip='şekilli',**k): mk(P,no,ad=ad,adim=len(ad),kalip=kalip,**k)
def yer(harf,dogru,yanlar):
    sira=[None]*5; sira['ABCDE'.index(harf)]=dogru; it=iter(yanlar)
    for i in range(5):
        if sira[i] is None: sira[i]=next(it)
    assert sorted(sira)==sorted([dogru]+list(yanlar)); return sira
def tk(body,scale=1.0): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small,scale=%s]\n%s\n\\end{tikzpicture}'%(scale,body))
OK='-{Stealth[length=2.3mm,width=1.9mm]}'

# =================== 01 · Hücre ve Organeller · kolay ===================
konu('bio|Hücre ve Organeller – Madde Geçişleri','Hücre ve Organeller – Madde Geçişleri')
kartla('K-BYP-01','Numaralı organelden görev bulma','Şematik hücrede organeller biçim, renk ve konumlarından tanınır; sorulan görev (fotosentez) yalnız ilgili organele aittir.','Bitkiye özgü olan her yapıyı fotosentezle ilişkilendirmek; mitokondriyi enerji dönüşümü yaptığı için seçmek.','kolay',3,'byp-hucre-organel','Numaralı bitki hücresinde organel ve görevi')
def kloroplast(x,y,a):
    o=f'\\begin{{scope}}[shift={{({x},{y})}},rotate={a},scale=1.25]\\draw[line width=1pt,fill=black,fill opacity=.10] (0,0) ellipse (.62 and .3);\\draw[line width=1pt] (0,0) ellipse (.62 and .3);\\draw[line width=.5pt] (0,0) ellipse (.56 and .24);'
    o+='\\draw[line width=.5pt] (-.4,0)--(.4,0);'
    for cx in (-.32,0,.32):
        for dy in (-.1,-.03,.04,.11): o+=f'\\draw[line width=.5pt,fill=black,fill opacity=.45] ({cx-.08},{dy-.02}) rectangle ({cx+.08},{dy+.02});'
    return o+'\\end{scope}'
def mito(x,y,a):
    return (f'\\begin{{scope}}[shift={{({x},{y})}},rotate={a},scale=1.35]\\draw[line width=1pt,fill=black,fill opacity=.10] (0,0) ellipse (.44 and .21);\\draw[line width=1pt] (0,0) ellipse (.44 and .21);\\draw[line width=.5pt] (0,0) ellipse (.39 and .16);'
      '\\draw[line width=.7pt] (-.31,.1)--(-.23,-.1)--(-.13,.11)--(-.03,-.11)--(.07,.11)--(.17,-.11)--(.27,.1);\\end{scope}')
b=[]
b.append('\\draw[rounded corners=14pt,line width=1.9pt] (0,0) rectangle (6.4,4.2);')
b.append('\\draw[rounded corners=12pt,line width=.6pt] (.13,.13) rectangle (6.27,4.07);')
b.append('\\draw[line width=1pt] (1.5,2.75) circle (.68);\\draw[line width=.5pt] (1.5,2.75) circle (.62);\\fill (1.68,2.9) circle (.16);')
b.append('\\draw[line width=1pt,smooth cycle,fill=black,fill opacity=.10] plot coordinates {(2.35,2.2) (2.8,3.05) (3.9,3.3) (5.0,2.9) (5.2,2.0) (4.8,1.3) (3.7,1.1) (2.7,1.5)};')
b.append('\\draw[line width=1pt,smooth cycle] plot coordinates {(2.35,2.2) (2.8,3.05) (3.9,3.3) (5.0,2.9) (5.2,2.0) (4.8,1.3) (3.7,1.1) (2.7,1.5)};')
b+= [kloroplast(1.2,.62,8),kloroplast(3.1,.55,-4),kloroplast(5.1,.62,6),mito(.95,1.5,10),mito(5.4,3.5,22)]
def lab(t,x,y,x1,y1,x2,y2):
    return f'\\node[font=\\normalsize\\bfseries] at ({x},{y}) {{{t}}};\\draw[{OK},line width=.8pt] ({x1},{y1})--({x2},{y2});'
b.append(lab('I',-1.0,3.3,-.65,3.3,-.03,3.3))        # hücre çeperi (dış çizgi)
b.append(lab('II',1.5,5.05,1.5,4.75,1.5,3.46))       # çekirdek
b.append(lab('III',3.1,-.95,3.1,-.62,3.1,.22))       # kloroplast
b.append(lab('IV',7.4,3.95,7.05,3.85,5.98,3.66))      # mitokondri
b.append(lab('V',4.0,5.05,4.0,4.75,3.95,3.33))       # koful
SK1=tk('\n'.join(b),.95)
OR1={'I':'hücre çeperi','II':'çekirdek','III':'kloroplast','IV':'mitokondri','V':'koful'}
FOTO={k:(k=='III') for k in OR1}; assert sum(FOTO.values())==1 and OR1['III']=='kloroplast'
KLO=B('Kloroplast','yalnız bitki hücrelerinde (ve alglerde) bulunan, klorofil taşıyan çift zarlı organeldir; ışık enerjisini organik maddelerin kimyasal enerjisine çevirir (fotosentez). Örnek: yaprak hücresi')
MIT=B('Mitokondri ve diğer yapılar','mitokondri organik maddeleri yıkarak ATP üretir (hücresel solunum) ve hem bitkide hem hayvanda bulunur · Çekirdek hücreyi yönetir · Koful madde depolar · Hücre çeperi bitkiye şekil verir ve korur')
q('0001',tipId='byp-hucre-organel',tip='Numaralı bitki hücresinde organel ve görevi',z='kolay',alt='Organeller',kaz='Şematik bitki hücresinde organelleri tanıyıp fotosentez yapan yapıyı belirler.',
 kart='K-BYP-01 (organel tanıma) · numaralı bitki hücresi',
 metin='Şekilde bir bitki hücresinin bazı yapıları I, II, III, IV ve V ile numaralandırılmıştır.\nBuna göre, numaralı yapılardan hangisinde ışık enerjisi kullanılarak inorganik maddelerden organik madde sentezlenir?',
 dogru='III',sira=['I','II','III','IV','V'],
 yan=[('I','I numaralı yapı hücre çeperidir; bitkiye özgü olduğundan fotosentezle karıştırılmış, oysa görevi hücreye şekil vermek ve korumaktır.','bilgi'),
      ('II','II numaralı yapı çekirdektir; hücre etkinliklerini yönetir ve kalıtım materyalini taşır, organik madde sentezi yapmaz.','bilgi'),
      ('IV','IV numaralı yapı mitokondridir; organik maddeleri yıkarak ATP üretir. “Enerji ile ilgili” diye seçilmiş ama ışıktan yararlanmaz.','bilgi'),
      ('V','V numaralı yapı büyük kofuldur; su ve çeşitli maddeleri depolar, sentez yeri değildir.','bilgi')],
 istenen='Fotosentezin gerçekleştiği yapının numarası.',
 ip=['Sorulan olayın hangi organelde gerçekleştiğini hatırla; şekildeki yapıları biçimlerine ve konumlarına bakarak tanı.'],
 bilgi=[KLO,MIT],
 ad=[A('Yapıları tanı','Dış çizgideki yapı çeper, iri çekirdek, yeşil ve yığınlı yapılar kloroplast, kıvrımlı içli oval yapı mitokondri, büyük boşluk koful.','I: çeper · II: çekirdek · III: kloroplast · IV: mitokondri · V: koful'),
     A('Olayı organele bağla','Işık enerjisiyle inorganik maddelerden organik madde sentezi fotosentezdir.','Fotosentez → kloroplast'),
     A('Numarayı seç','Kloroplast şekilde III ile gösterilmiştir.','Cevap: III')],
 puf='Işıkla organik madde sentezi yalnız klorofil taşıyan kloroplastta olur; yeşil, içi yığınlı yapıyı ara.',sekil=SK1)

# =================== 02 · Madde Geçişleri (ozmoz) · orta ===================
kartla('K-BYP-02','Yarı geçirgen zarlı U borusu','Zar yalnız suyu geçirir; su, su oranı çok (derişimi düşük) çözeltiden az (derişimi yüksek) çözeltiye pasif olarak geçer ve yüksek derişimli kolda seviye yükselir.','Çözünen maddenin zardan geçtiğini sanmak; su yönünü derişimi yüksek taraftan düşük tarafa almak; ozmozu aktif taşıma sanmak.','orta',4,'byp-ozmoz-u','Yarı geçirgen zarlı U borusunda su geçişi')
random.seed(11)
def noktalar(n,bolge,ar=.34):
    out=[]
    while len(out)<n:
        x=random.uniform(bolge[0]+.18,bolge[1]-.18); y=random.uniform(bolge[2]+.18,bolge[3]-.18)
        if all((x-a)**2+(y-b_)**2>ar**2 for a,b_ in out): out.append((x,y))
    return out
SOL=(0,1.4); SAG=(3.3,4.7); YB=3.0   # kol x aralıkları, sıvı seviyesi
CL,CR=10,30; assert CR==3*CL
# sol bölge: 0..2.05 (kol + alt kısmın sol yarısı); nokta konumlarını bölgeye sığdır
def bolgede(p,x0,x1):
    x,y=p
    return (x0<=x<=x1) and ((y<=1.2) or (SOL[0]<=x<=SOL[1]) or (SAG[0]<=x<=SAG[1]))
def nokta_uret(n,x0,x1,y_ust=2.85):
    out=[]
    while len(out)<n:
        x=random.uniform(x0+.15,x1-.15); y=random.uniform(.15,y_ust)
        if not bolgede((x,y),x0,x1): continue
        if y>1.2 and not ((SOL[0]+.15<=x<=SOL[1]-.15) or (SAG[0]+.15<=x<=SAG[1]-.15)): continue
        if all((x-a)**2+(y-b_)**2>.32**2 for a,b_ in out): out.append((x,y))
    return out
MID=2.35
dl=nokta_uret(4,0,MID); dr=nokta_uret(12,MID,4.7)
assert len(dr)==3*len(dl)
b=[]
b.append(f'\\fill[vurgu,fill opacity=.14] (0,{YB})--(0,0)--({MID},0)--({MID},1.2)--({SOL[1]},1.2)--({SOL[1]},{YB})--cycle;')
b.append(f'\\fill[vurgu,fill opacity=.14] ({SAG[0]},{YB})--({SAG[0]},1.2)--({MID},1.2)--({MID},0)--(4.7,0)--(4.7,{YB})--cycle;')
b.append(f'\\draw[line width=1.5pt] (0,3.9)--(0,0)--(4.7,0)--(4.7,3.9);\\draw[line width=1.5pt] ({SOL[1]},3.9)--({SOL[1]},1.2)--({SAG[0]},1.2)--({SAG[0]},3.9);')
b.append(f'\\draw[line width=.7pt,vurgu] (0,{YB})--({SOL[1]},{YB});\\draw[line width=.7pt,vurgu] ({SAG[0]},{YB})--(4.7,{YB});')
b.append(f'\\draw[line width=2pt,dashed,vurgu!70!black] ({MID},.02)--({MID},1.18);')
for x,y in dl+dr: b.append(f'\\fill ({x:.2f},{y:.2f}) circle (.07);')
b.append(f'\\node[font=\\small] at (.7,4.3) {{\\%{CL}}};\\node[font=\\small] at (4.0,4.3) {{\\%{CR}}};')
b.append(f'\\node[font=\\scriptsize,align=center] at ({MID},2.45) {{yarı geçirgen\\\\zar}};\\draw[{OK},line width=.7pt] ({MID},1.95)--({MID},1.26);')
b.append('\\fill (5.4,3.15) circle (.07);\\node[font=\\scriptsize,anchor=west] at (5.55,3.15) {glikoz};')
SK2=tk('\n'.join(b),.95)
# ozmoz yönü: su oranı çok (derişim düşük) → az
assert CL<CR; yon='sol→sağ'
OZ=B('Ozmoz','suyun yarı geçirgen zardan, su oranı çok (derişimi düşük) ortamdan su oranı az (derişimi yüksek) ortama geçmesidir; çözünen madde zardan geçemiyorsa denge su geçişiyle kurulur. Örnek: şeker çözeltisi olan kola su girer')
PAS=B('Pasif ve aktif taşıma','difüzyon ve ozmoz pasiftir: enerji (ATP) gerekmez, madde ya da su derişim farkı yönünde ilerler · Aktif taşıma taşıyıcı proteinle ve ATP harcanarak, derişimin az olduğu yerden çok olduğu yere yapılır')
dog2='Su sol koldan sağ kola geçer; sağ kolda seviye yükselir ve bu geçiş ATP harcanmadan gerçekleşir.'
q('0002',tipId='byp-ozmoz-u',tip='Yarı geçirgen zarlı U borusunda su geçişi',z='orta',alt='Ozmoz',kaz='Yarı geçirgen zarlı düzenekte suyun geçiş yönünü, seviye değişimini ve enerji gereksinimini yorumlar.',
 kart='K-BYP-02 (ozmoz, U borusu) · %10 ve %30 glikoz, zar yalnız suyu geçirir',
 metin='Şekildeki U şeklindeki kabın tabanında yalnızca suyu geçiren, glikozu geçirmeyen yarı geçirgen bir zar bulunmaktadır. Kolların her birine eşit hacimde, derişimleri şekilde verilen (kütlece yüzde) glikoz çözeltileri konulmuştur ve başlangıçta iki koldaki sıvı seviyeleri aynıdır. Düzenek bir süre bekletiliyor.\nBuna göre, aşağıdakilerden hangisi doğrudur?',
 dogru=dog2,sira=yer('A',dog2,['Glikoz sağ koldan sol kola geçer; iki koldaki derişimler eşitlenir ve seviyeler değişmez.','Su sağ koldan sol kola geçer; çünkü su, derişimi yüksek çözeltiden düşük çözeltiye hareket eder.','Su, derişimi az olan yerden çok olan yere geçtiği için bu hareket aktif taşımadır ve ATP harcanır.','Zar glikozu geçirmediği için madde geçişi olmaz; iki koldaki seviyeler başlangıçtaki gibi kalır.']),
 yan=[('Glikoz sağ koldan sol kola geçer; iki koldaki derişimler eşitlenir ve seviyeler değişmez.','Zar yalnız suyu geçirir; glikoz geçemez. Derişim eşitlenmesi (difüzyon) varsayılmış, oysa dengeyi su geçişi kurar.','bilgi'),
      ('Su sağ koldan sol kola geçer; çünkü su, derişimi yüksek çözeltiden düşük çözeltiye hareket eder.','Derişim, çözünenin derişimidir; su ise çözünen derişiminin düşük olduğu (su oranının çok olduğu) sol koldan sağa geçer. Su yönü ters alınmış.','bilgi'),
      ('Su, derişimi az olan yerden çok olan yere geçtiği için bu hareket aktif taşımadır ve ATP harcanır.','Yön doğru bulunmuş ama ozmoz pasif bir olaydır; suyun su oranı çok olandan az olana geçişi enerji gerektirmez. “Az → çok” çözünen için söylenir, su için değil.','bilgi'),
      ('Zar glikozu geçirmediği için madde geçişi olmaz; iki koldaki seviyeler başlangıçtaki gibi kalır.','Zar suyu geçirdiği için su hareketi olur. Glikozun geçememesi, tüm madde geçişini engellediği anlamına gelmez.','dikkat')],
 istenen='Düzenek bekletildiğinde doğru olan ifade.',
 ip=['Zarın neyi geçirip neyi geçirmediğine bak; sonra iki kolda suyun bulunma oranını karşılaştır.'],
 bilgi=[OZ,PAS],
 ad=[A('Zarın geçirgenliğini belirle','Zar yalnız suyu geçirir, glikoz zardan geçemez.','Hareket eden madde: yalnız su'),
     A('İki kolu karşılaştır','Sol kolda %10, sağ kolda %30 glikoz var; derişimi düşük olan solda su oranı daha fazladır.','Su oranı: sol > sağ'),
     A('Su geçişinin yönünü bul','Su, su oranı çok olandan az olana geçer.','Su: sol koldan sağ kola → sağ kolda seviye yükselir'),
     A('Enerji gereksinimini değerlendir','Ozmoz pasif taşımadır; ATP kullanılmaz.','ATP harcanmaz → doğru şık A')],
 puf='Zar çözüneni geçirmiyorsa hareket eden su olur: su, çözünen derişiminin düşük olduğu taraftan yükseğe, enerji harcamadan geçer.',sekil=SK2)

# =================== 03 · Kalıtım (soyağacı) · zor ===================
konu('bio|Kalıtım','Kalıtım')
kartla('K-BYP-03','Soyağacında kalıtım biçimi ve genotip','Hasta kızın sağlıklı babası eşeye bağlı kalıtımı, sağlıklı ebeveynin hasta çocuğu baskın kalıtımı dışlar; otozomal çekinikte genotipler çocuk ve ebeveynlerden kesinleştirilir, kesinleşmeyenler ayrılır.','Sağlıklı çocuğu olan bireyi homozigot baskın sanmak; “taşıyıcı olabilir” ile “taşıyıcıdır” ayrımını yapmamak; kızdaki hastalığı eşeye bağlı saymak.','zor',5,'byp-soyagaci','Soyağacında kalıtım biçimi ve genotip belirleme')
KISI={ # ad:(cinsiyet,hasta,anne,baba)
 'I-1':('E',0,None,None),'I-2':('K',0,None,None),
 'II-1':('E',0,None,None),'II-2':('K',1,'I-2','I-1'),'II-3':('K',0,'I-2','I-1'),'II-4':('E',0,'I-2','I-1'),'II-5':('K',0,None,None),
 'III-1':('E',0,'II-2','II-1'),'III-2':('K',0,'II-5','II-4'),'III-3':('E',1,'II-5','II-4')}
def allel(g): return {0:[0],1:[0,1],2:[1]}[g]
def tara(model):
    X=model in('XR','XD'); dom=model in('AD','XD'); dunya=[]
    ad=list(KISI)
    def secenek(a):
        s,h,_,_=KISI[a]; gs=[0,1] if (X and s=='E') else [0,1,2]
        out=[]
        for g in gs:
            if X and s=='E': aff=(g==1)
            else: aff=(g>=1) if dom else (g==2)
            if aff==bool(h): out.append(g)
        return out
    for tup in itertools.product(*[secenek(a) for a in ad]):
        G=dict(zip(ad,tup)); ok=True
        for a in ad:
            s,h,an,ba=KISI[a]
            if an is None: continue
            if X:
                if s=='E': iz={x for x in allel(G[an])}
                else: iz={x+G[ba] for x in allel(G[an])}      # baba hemizigot: allel = g
            else: iz={x+y for x in allel(G[an]) for y in allel(G[ba])}
            if G[a] not in iz: ok=False;break
        if ok: dunya.append(G)
    return dunya
DUNYA={m:tara(m) for m in ('AR','AD','XR','XD')}
assert DUNYA['AD']==[] and DUNYA['XR']==[] and DUNYA['XD']==[] and DUNYA['AR']    # tek geçerli model: otozomal çekinik
W=DUNYA['AR']
kesin={a:{w[a] for w in W} for a in KISI}
BELLI={a for a in KISI if len(kesin[a])==1}; BELIRSIZ={a for a in KISI if len(kesin[a])>1}
assert kesin['I-1']=={1} and kesin['I-2']=={1} and kesin['II-2']=={2} and kesin['II-4']=={1} and kesin['II-5']=={1} and kesin['III-1']=={1} and kesin['III-3']=={2}
assert kesin['II-1']=={0,1} and kesin['II-3']=={0,1} and kesin['III-2']=={0,1} and BELIRSIZ=={'II-1','II-3','III-2'}
def kesin_dogru(f): return all(f(w) for w in W)
S_DOG='II-4 ve III-1 bireyleri heterozigot genotiptedir.'
S_Y1='Hastalık, X kromozomuna bağlı çekinik bir alelle belirlenir.'
S_Y2='II-1 bireyi, sağlıklı çocuğu olduğu için homozigot baskındır.'
S_Y3='III-2 bireyi sağlıklı olduğundan homozigot baskın genotiptedir.'
S_Y4='II-3 bireyinin heterozigot olduğu kesindir; çünkü anne ve babası taşıyıcıdır.'
assert kesin_dogru(lambda w:w['II-4']==1 and w['III-1']==1)
assert not DUNYA['XR']                                                      # S_Y1: hiçbir dünyada yok
assert not kesin_dogru(lambda w:w['II-1']==0) and any(w['II-1']==1 for w in W)        # S_Y2
assert not kesin_dogru(lambda w:w['III-2']==0) and any(w['III-2']==1 for w in W)      # S_Y3
assert not kesin_dogru(lambda w:w['II-3']==1) and any(w['II-3']==0 for w in W)        # S_Y4
# çizim
XY={'I-1':(2.55,4.4),'I-2':(4.25,4.4),'II-1':(0,2.4),'II-2':(1.7,2.4),'II-3':(3.4,2.4),'II-4':(5.1,2.4),'II-5':(6.8,2.4),'III-1':(.85,.4),'III-2':(5.25,.4),'III-3':(6.65,.4)}
R=.28
b=[]
for a,(x,y) in XY.items():
    s,h,_,_=KISI[a]; fl='fill=black' if h else ''
    b.append(f'\\draw[line width=1pt,{fl}] ({x-R},{y-R}) rectangle ({x+R},{y+R});' if s=='E' else f'\\draw[line width=1pt,{fl}] ({x},{y}) circle ({R});')
    b.append(f'\\node[font=\\footnotesize] at ({x},{y-.52}) {{{a.split("-")[1]}}};')
def evlilik(a,c): 
    (x1,y),(x2,_)=XY[a],XY[c]; b.append(f'\\draw[line width=1pt] ({x1+R},{y})--({x2-R},{y});'); return (x1+x2)/2,y
def cocuk(m,ylar,cocuklar,ybar):
    xs=[XY[c][0] for c in cocuklar]; yc=XY[cocuklar[0]][1]
    if len(cocuklar)==1:
        b.append(f'\\draw[line width=1pt] ({m},{ylar})--({xs[0]},{yc+R});'); assert abs(xs[0]-m)<1e-9
    else:
        b.append(f'\\draw[line width=1pt] ({m},{ylar})--({m},{ybar});\\draw[line width=1pt] ({min(xs+[m])},{ybar})--({max(xs+[m])},{ybar});')
        for x in xs: b.append(f'\\draw[line width=1pt] ({x},{ybar})--({x},{yc+R});')
m1=evlilik('I-1','I-2'); cocuk(m1[0],m1[1],['II-2','II-3','II-4'],3.4)
m2=evlilik('II-1','II-2'); cocuk(m2[0],m2[1],['III-1'],None)
m3=evlilik('II-4','II-5'); cocuk(m3[0],m3[1],['III-2','III-3'],1.4)
for r,y in (('I',4.4),('II',2.4),('III',.4)): b.append(f'\\node[font=\\normalsize\\bfseries] at (-1.0,{y}) {{{r}}};')
SK3=tk('\n'.join(b),.95)
ALK=B('Soyağacı yorumu','Sağlıklı ebeveynlerin hasta çocuğu varsa hastalık çekiniktir ve ebeveynler taşıyıcıdır (Aa) · Hasta kızın babası sağlıklıysa hastalık eşeye bağlı olamaz (eşeye bağlı çekinikte hasta kızın babası da hasta olur) · Aa × Aa çaprazında sağlıklı çocuk AA ya da Aa olabilir')
GEN=B('Genotip belirleme','Hasta birey aa’dır · Bir bireyin hasta çocuğu varsa ve kendisi sağlıksa Aa’dır · Hasta (aa) annenin sağlıklı çocuğu, babadan A aldığı için Aa’dır · Çocuğu yalnızca sağlıklı olan bireyde AA ile Aa ayırt edilemez')
q('0003',tipId='byp-soyagaci',tip='Soyağacında kalıtım biçimi ve genotip belirleme',z='zor',alt='Soyağacı',kaz='Soyağacından kalıtım biçimini belirleyip hangi bireylerin genotipinin kesin olduğunu yorumlar.',
 kart='K-BYP-03 (soyağacı) · otozomal çekinik, 10 birey, genotipi kesin ve belirsiz bireyler',
 metin='Şekilde, tek gen çiftiyle belirlenen bir hastalığın üç kuşaklık soyağacı verilmiştir. Dolu semboller hasta, boş semboller sağlıklı bireyleri; kareler erkekleri, daireler kadınları göstermektedir. Bireyler kuşak (I, II, III) ve soldan sağa sıra numarasıyla anılır (örneğin II-4, ikinci kuşaktaki dördüncü bireydir). Aileye dışarıdan katılan bireyler de şekilde gösterilmiştir ve mutasyon gerçekleşmemiştir.\nBuna göre, aşağıdakilerden hangisi kesinlikle doğrudur?',
 dogru=S_DOG,sira=yer('D',S_DOG,[S_Y3,S_Y1,S_Y4,S_Y2]),
 yan=[(S_Y1,'II-2 hasta bir kızdır ve babası I-1 sağlıklıdır; eşeye bağlı çekinik kalıtımda hasta kızın babası da hasta olmak zorundadır. Kalıtım otozomal çekiniktir.','bilgi'),
      (S_Y2,'III-1’in sağlıklı olması II-1’in AA olduğunu göstermez: II-1 Aa da olabilir, III-1 (annesi aa olduğundan) yine sağlıklı doğar. II-1 belirsizdir.','dikkat'),
      (S_Y3,'III-2’nin anne ve babası (II-5 ve II-4) heterozigottur; sağlıklı çocuk AA ya da Aa olabilir. “Sağlıklı = homozigot baskın” varsayımı yanlıştır.','bilgi'),
      (S_Y4,'II-3’ün ebeveynleri Aa × Aa olduğundan II-3 AA (1/3) ya da Aa (2/3) olabilir; heterozigot olması kesin değildir, yalnızca olasıdır.','dikkat')],
 istenen='Soyağacına göre kesinlikle doğru olan ifade.',
 ip=['Önce hastalığın hangi kalıtım biçimiyle belirlendiğini, ebeveyn–çocuk ilişkilerinden ve hasta bireylerin cinsiyetinden çıkar.'],
 bilgi=[ALK,GEN],
 ad=[A('Kalıtım biçimini bul','Sağlıklı I-1 ile I-2’nin hasta kızı II-2 var; hasta kızın babası sağlıklı olduğundan eşeye bağlı kalıtım da dışlanır.','Hastalık otozomal çekinik'),
     A('Hastaların genotipini yaz','Hasta bireyler çekinik homozigottur.','II-2 = aa · III-3 = aa'),
     A('Genotipi kesin olanları belirle','Hasta çocuğu olan sağlıklı ebeveynler Aa’dır; annesi aa olan sağlıklı III-1, babadan A aldığı için Aa’dır.','I-1, I-2, II-4, II-5, III-1 = Aa'),
     A('Belirsiz bireyleri ayır','Yalnızca sağlıklı çocuğu olanlar ya da taşıyıcı ebeveynlerin sağlıklı çocukları AA da Aa da olabilir.','II-1, II-3, III-2: AA veya Aa'),
     A('Şıkları ele','Yalnız “II-4 ve III-1 heterozigot” her durumda geçerlidir.','Doğru: D')],
 puf='Önce kalıtım biçimini elemeyle bul, sonra yalnızca hasta çocuk ya da hasta ebeveyn yoluyla kesinleşen genotipleri yaz; geri kalanı “AA veya Aa” bırak.',sekil=SK3)

# =================== 04 · Ekosistem (besin ağı) · orta ===================
konu('bio|Ekosistem','Ekosistem')
kartla('K-BYP-04','Besin ağında trofik düzeyler','Ağdaki her canlının trofik düzeyi, yediği canlıların düzeyinden bulunur; birden fazla besin kaynağı olan canlı birden fazla düzeyde yer alabilir.','Bir canlıya tek düzey vermek; bir besin kaynağı kalkınca onu yiyenin tümüyle beslenemeyeceğini sanmak; enerjinin basamaklarda arttığını sanmak.','orta',4,'byp-besin-agi','Besin ağında trofik düzey ve enerji')
YEMEK={'Alg':[],'Su piresi':['Alg'],'İribaş':['Alg'],'Gümüş balığı':['Su piresi'],'Su yılanı':['İribaş','Gümüş balığı'],'Balıkçıl':['Gümüş balığı','Su yılanı']}
DUZ={}
def duzey(c):
    if c in DUZ: return DUZ[c]
    DUZ[c]={1} if not YEMEK[c] else {d+1 for y in YEMEK[c] for d in duzey(y)}; return DUZ[c]
for c in YEMEK: duzey(c)
assert DUZ=={'Alg':{1},'Su piresi':{2},'İribaş':{2},'Gümüş balığı':{3},'Su yılanı':{3,4},'Balıkçıl':{4,5}}
def yok_olunca(c): # c yok olursa besinsiz kalan canlılar (tüm besin kaynakları yok olanlar)
    yok={c}; ch=True
    while ch:
        ch=False
        for k,v in YEMEK.items():
            if k not in yok and v and all(x in yok for x in v): yok.add(k); ch=True
    return yok-{c}
assert yok_olunca('Gümüş balığı')=={} or yok_olunca('Gümüş balığı')==set()
POS={'Alg':(2.6,0),'Su piresi':(.9,1.6),'İribaş':(4.4,1.6),'Gümüş balığı':(.9,3.2),'Su yılanı':(3.4,4.8),'Balıkçıl':(1.9,6.4)}
b=[]
for c,(x,y) in POS.items(): b.append(f'\\node[draw,rounded corners=2pt,inner sep=3.5pt,line width=.9pt,font=\\footnotesize] ({c.replace(" ","").replace("ı","i").replace("İ","I").replace("ş","s").replace("ğ","g")}) at ({x},{y}) {{{c}}};')
def nid(c): return c.replace(" ","").replace("ı","i").replace("İ","I").replace("ş","s").replace("ğ","g")
for c,v in YEMEK.items():
    for y in v: b.append(f'\\draw[{OK},line width=.9pt] ({nid(y)})--({nid(c)});')
SK4=tk('\n'.join(b),.95)
dog4='Su yılanı 3. ve 4., balıkçıl 4. ve 5. trofik düzeyde yer alır.'
Y41='İribaş 2., su piresi 3. trofik düzeydedir.'; Y42='Gümüş balığı ortadan kalkarsa su yılanı ve balıkçıl besinsiz kalır.'
Y43='Balıkçıl yalnızca 5. trofik düzeyde yer alır.'; Y44='Gümüş balığındaki enerji miktarı, su piresindekinden daha fazladır.'
assert DUZ['İribaş']==DUZ['Su piresi']=={2}; assert yok_olunca('Gümüş balığı')==set(); assert DUZ['Balıkçıl']!={5} and 4 in DUZ['Balıkçıl']
assert DUZ['Su yılanı']=={3,4} and DUZ['Balıkçıl']=={4,5}
TRO=B('Trofik düzey','üreticiler 1. düzeydir; bir tüketicinin düzeyi, yediği canlının düzeyinin bir fazlasıdır. Birden fazla canlıyla beslenen tüketici birden çok düzeyde yer alabilir. Örnek: otçul 2., onu yiyen etçil 3. düzeydedir')
ENJ=B('Enerji akışı','enerji besin zincirinde yenenden yiyene akar; her basamakta büyük bölümü solunumda ve ısı olarak harcanır, yaklaşık onda biri bir üst basamağa geçer; bu yüzden üst basamaklarda enerji miktarı azalır')
q('0004',tipId='byp-besin-agi',tip='Besin ağında trofik düzey ve enerji',z='orta',alt='Besin Ağı',kaz='Besin ağında trofik düzeyleri belirler, canlıların alternatif besin kaynaklarını ve enerji akışını yorumlar.',
 kart='K-BYP-04 (besin ağı) · göl ekosistemi, trofik düzey',
 metin='Şekilde bir göl ekosistemindeki bazı canlılar arasındaki beslenme ilişkileri gösterilmiştir. Oklar enerjinin akış yönünü (yenen canlıdan yiyen canlıya) belirtir ve üreticiler 1. trofik düzey kabul edilmektedir.\nBuna göre, aşağıdakilerden hangisi doğrudur?',
 dogru=dog4,sira=yer('B',dog4,[Y42,Y43,Y41,Y44]),
 yan=[(Y41,'İribaş ve su piresi doğrudan alg (üretici) ile beslenir; ikisi de birincil tüketicidir ve 2. trofik düzeydedir.','dikkat'),
      (Y42,'Su yılanı İribaş ile de beslenir, balıkçıl da su yılanını yer; tek besin kaynağı kalkmadığı için ikisi de besinsiz kalmaz.','bilgi'),
      (Y43,'Balıkçıl gümüş balığını da yer (gümüş balığı 3. düzey → balıkçıl 4.); bu yüzden hem 4. hem 5. düzeydedir.','bilgi'),
      (Y44,'Enerji basamaklar çıkıldıkça azalır: gümüş balığı yalnız su piresini yediğinden onun enerjisinin yalnızca bir bölümünü alır.','bilgi')],
 istenen='Besin ağına göre doğru olan ifade.',
 ip=['Her canlının trofik düzeyini, yediği canlıların düzeyinden yola çıkarak bul; birden fazla besini olanlara dikkat et.'],
 bilgi=[TRO,ENJ],
 ad=[A('Üretici ve birincil tüketicileri bul','Alg üretici (1), onu yiyenler 2. düzeydedir.','Alg: 1 · Su piresi: 2 · İribaş: 2'),
     A('Üst basamakları hesapla','Gümüş balığı su piresini yer (3). Su yılanı İribaş’ı (2) ve gümüş balığını (3) yer.','Gümüş balığı: 3 · Su yılanı: 3 ve 4'),
     A('Balıkçılın düzeyini bul','Balıkçıl gümüş balığını (3) ve su yılanını (3, 4) yer.','Balıkçıl: 4 ve 5'),
     A('Şıkları ele','İribaş–su piresi aynı düzeydedir; besin kaynağı kalkınca alternatifi olan beslenir; enerji azalır.','Doğru: B')],
 puf='Trofik düzey = yediği canlının düzeyi + 1; birden fazla besini olan canlıda her besin ayrı düzey verir.',sekil=SK4)

# =================== 05 · Hücrede Bölünme · zor ===================
konu('bio|Hücrede Bölünme – Üreme','Hücrede Bölünme – Üreme')
kartla('K-BYP-05','Mayoz ve mitoz evrelerini şekilden ayırma','Kromozomların çift/tek kromatitli olması, homologların eşleşmesi ve kutuplardaki takım sayısı bölünme türünü ve evresini belirler.','Kromatit ayrılmasını gösteren her anafazı mayoz II saymak; metafaz–anafaz ayrımını yapmamak; mayoz I ile II’yi karıştırmak.','zor',5,'byp-mayoz-evre','Şematik bölünme evrelerini tanıma')
LC,SC='L','S'
# kromozom: (tür, boy, renk, x, y)  tür: 'D' çift kromatitli, 'T' tek kromatitli
HUC={
 'I':  dict(asama='plak',kr=[('D',LC,'k',0,.5),('D',SC,'g',0,-.5)]),                                       # mayoz II metafaz
 'II': dict(asama='kutup',kr=[('D',LC,'k',-.78,.5),('D',SC,'g',-.78,-.5),('D',LC,'g',.78,.5),('D',SC,'k',.78,-.5)]),   # mayoz I anafaz
 'III':dict(asama='kutup',kr=[('T',LC,'k',-1.05,.5),('T',LC,'g',-.7,.5),('T',SC,'k',-1.05,-.5),('T',SC,'g',-.7,-.5),
                              ('T',LC,'k',1.05,.5),('T',LC,'g',.7,.5),('T',SC,'k',1.05,-.5),('T',SC,'g',.7,-.5)]),     # mitoz anafaz
 'IV': dict(asama='plak',kr=[('D',LC,'k',-.19,.5),('D',LC,'g',.19,.5),('D',SC,'g',-.19,-.5),('D',SC,'k',.19,-.5)]),   # mayoz I metafaz
 'V':  dict(asama='kutup',kr=[('T',LC,'k',-.85,.5),('T',SC,'g',-.85,-.5),('T',LC,'k',.85,.5),('T',SC,'g',.85,-.5)]),   # mayoz II anafaz
}
def siniflandir(h):
    kr=h['kr']; gruplar=[kr] if h['asama']=='plak' else [[c for c in kr if c[3]<0],[c for c in kr if c[3]>0]]
    pl=set()
    for g in gruplar:
        nl=sum(c[1]==LC for c in g); ns=sum(c[1]==SC for c in g); assert nl==ns; pl.add(nl)
    assert len(pl)==1; ploidi=pl.pop(); dyad=all(c[0]=='D' for c in kr); tek=all(c[0]=='T' for c in kr); assert dyad!=tek
    if h['asama']=='plak': return 'Mayoz I metafaz' if ploidi==2 else 'Mayoz II metafaz'
    if tek: return 'Mitoz anafaz' if ploidi==2 else 'Mayoz II anafaz'
    return 'Mayoz I anafaz' if ploidi==1 else 'HATA'
SIN={k:siniflandir(v) for k,v in HUC.items()}
assert SIN=={'I':'Mayoz II metafaz','II':'Mayoz I anafaz','III':'Mitoz anafaz','IV':'Mayoz I metafaz','V':'Mayoz II anafaz'}
MAYOZ2={k for k,v in SIN.items() if v.startswith('Mayoz II')}; assert MAYOZ2=={'I','V'}
for k,v in HUC.items():   # sayım: 2n=4, kromatit/kromozom tutarlılığı
    toplam=len(v['kr']); kromatit=sum(2 if c[0]=='D' else 1 for c in v['kr'])
    assert (toplam,kromatit)=={'I':(2,4),'II':(4,8),'III':(8,8),'IV':(4,8),'V':(4,4)}[k],(k,toplam,kromatit)
AD_={'L':(.12,.32),'S':(.09,.21)}; REN={'k':'black','g':'vurgu'}
def kromozom(cx,cy,c):
    t,boy,renk,x,y=c; X=cx+x; Y=cy+y; col=REN[renk]
    if t=='D':
        a,bb=AD_[boy]; return f'\\draw[{col},line width=1.7pt] ({X-a:.3f},{Y-bb:.3f})--({X+a:.3f},{Y+bb:.3f});\\draw[{col},line width=1.7pt] ({X-a:.3f},{Y+bb:.3f})--({X+a:.3f},{Y-bb:.3f});'
    dx,bb=(.17,.30) if boy=='L' else (.12,.2); s=-1 if x<0 else 1; return f'\\draw[{col},line width=1.7pt] ({X-s*dx:.3f},{Y-bb:.3f})--({X:.3f},{Y:.3f})--({X-s*dx:.3f},{Y+bb:.3f});'
def hucre_ciz(cx,cy,h,et):
    o=[f'\\draw[line width=.9pt] ({cx},{cy}) ellipse (1.55 and 1.2);']
    for s in (-1,1):
        px=cx+s*1.32
        for c in h['kr']:
            if h['asama']=='plak':
                # her kromozoma iki kutuptan lif (mayoz I'de homolog yalnız kendi tarafındaki kutuptan)
                if h is HUC['IV']:
                    if (c[3]<0)==(s<0): o.append(f'\\draw[gray,line width=.6pt] ({px:.2f},{cy}) -- ({cx+c[3]:.3f},{cy+c[4]:.3f});')
                else: o.append(f'\\draw[gray,line width=.6pt] ({px:.2f},{cy}) -- ({cx+c[3]:.3f},{cy+c[4]:.3f});')
            elif (c[3]<0)==(s<0): o.append(f'\\draw[gray,line width=.6pt] ({px:.2f},{cy}) -- ({cx+c[3]:.3f},{cy+c[4]:.3f});')
        o.append(f'\\fill ({px:.2f},{cy}) circle (.055);')
    for c in h['kr']: o.append(kromozom(cx,cy,c))
    o.append(f'\\node[font=\\normalsize\\bfseries] at ({cx},{cy-1.55}) {{{et}}};')
    return '\n'.join(o)
YER={'I':(0,0),'II':(3.7,0),'III':(7.4,0),'IV':(1.85,-3.3),'V':(5.55,-3.3)}
SK5=tk('\n'.join(hucre_ciz(*YER[k],HUC[k],k) for k in HUC),.9)
dog5='I ve V'; Z51='I ve IV'; Z52='II ve IV'; Z53='III ve V'; Z54='II, III ve V'
assert {k for k,v in SIN.items() if v.startswith('Mayoz II')}=={'I','V'}
assert {k for k,v in SIN.items() if v.startswith('Mayoz I ')}=={'II','IV'}
assert {k for k,v in SIN.items() if 'metafaz' in v}=={'I','IV'} and {k for k,v in SIN.items() if 'anafaz' in v and 'Mayoz I ' not in v}=={'III','V'}
MAY=B('Mayoz evreleri','Mayoz I’de homolog kromozomlar eşleşir (metafaz I’de çiftler plakada), anafaz I’de homologlar kutuplara ayrılır; her kromozom çift kromatitli kalır ve hücreler haploit olur · Mayoz II’de kardeş kromatitler ayrılır (anafaz II): kutup başına n sayıda tek kromatitli kromozom')
MIT_=B('Mitoz anafazı','mitozda homologlar eşleşmez; anafazda kardeş kromatitler ayrılır ve her kutba 2n sayıda tek kromatitli kromozom gider. Örnek: 2n = 4 hücrede her kutupta 4 kromozom')
q('0005',tipId='byp-mayoz-evre',tip='Şematik bölünme evrelerini tanıma',z='zor',alt='Mayoz ve Mitoz Evreleri',kaz='Şematik çizimlerde kromozom ve kromatit yapısına bakarak bölünme türünü ve evresini belirler.',
 kart='K-BYP-05 (evre tanıma) · 2n = 4, beş hücre, mayoz II hücreleri',
 metin='Şekilde, 2n = 4 kromozomlu bir hayvanın eşey organındaki beş hücre, bölünmenin farklı evrelerinde şematik olarak gösterilmiştir. Siyah ve yeşil renkler yalnızca homolog kromozomları ayırt etmek içindir; krossing-over gerçekleşmemiştir. Çift kromatitli kromozomlar X biçiminde, tek kromatitli kromozomlar ise V biçiminde çizilmiştir.\nBuna göre, numaralı hücrelerden hangileri mayoz II evresinde bulunmaktadır?',
 dogru=dog5,sira=yer('E',dog5,[Z51,Z52,Z53,Z54]),
 yan=[(Z51,'I ve IV ekvator düzleminde dizilmiş iki metafaz hücresidir; ancak IV’te homolog çiftler eşleşmiştir (mayoz I), mayoz II değildir. Metafaz olmak mayoz II olmayı belirlemez.','bilgi'),
      (Z52,'II ve IV’ü mayoz II sanmak mayoz I ile II’yi karıştırmaktır: bu hücrelerde homologlar eşleşmiş (IV) ya da kutuplara ayrılmış ama kromozomlar hâlâ çift kromatitlidir (II); ikisi de mayoz I’dir.','bilgi'),
      (Z53,'III ve V’te kardeş kromatitler ayrılmıştır ama III’te her kutupta 4 kromozom (2n) vardır; bu mitoz anafazıdır. Yalnız V mayoz II’dir.','dikkat'),
      (Z54,'Anafaz hücrelerinin tümü mayoz II sayılmış; oysa II mayoz I’in anafazıdır (homologlar ayrılıyor) ve III mitoz anafazıdır.','bilgi')],
 istenen='Mayoz II evresindeki hücrelerin numaraları.',
 ip=['Her hücrede kromozomların çift mi tek kromatitli olduğuna ve her kutup ya da plakadaki kromozom takımının kaç kromozomdan oluştuğuna bak.'],
 bilgi=[MAY,MIT_],
 ad=[A('Her hücrenin kromozom yapısını oku','2n = 4: homolog çiftler bir uzun, bir kısa kromozomdan oluşur. X çift kromatitli, V tek kromatitlidir.','I: 2 X · II: kutupta 2 X · III: kutupta 4 V · IV: 2 eşleşmiş çift · V: kutupta 2 V'),
     A('Homolog ve kromatit durumunu ayır','IV’te homologlar eşleşmiş (mayoz I metafaz); II’de homologlar ayrılmış, X’ler duruyor (mayoz I anafaz).','II ve IV: mayoz I'),
     A('Mitozu ayıkla','III’te kardeş kromatitler ayrılmış ve her kutupta 4 kromozom (2n) var.','III: mitoz anafaz'),
     A('Mayoz II hücrelerini bul','Takım haploit (n = 2) ve kromatitler ya plakada çiftli (I) ya da ayrılmış (V).','I: metafaz II · V: anafaz II'),
     A('Sonucu yaz','Mayoz II evresindeki hücreler I ve V’tir.','Cevap: I ve V')],
 puf='Önce tek/çift kromatiti ve kutuptaki kromozom sayısını yaz: homologlar ayrılırken X’ler duruyorsa mayoz I, kutupta n tane V varsa mayoz II, 2n tane V varsa mitozdur.',sekil=SK5)

# =================== 06 · Canlıların Temel Bileşenleri (enzim–sıcaklık) · orta ===================
konu('bio|Canlıların Temel Bileşenleri','Canlıların Temel Bileşenleri')
kartla('K-BYP-06','Enzim etkinliği–sıcaklık grafiği','Grafikten her enzimin optimum sıcaklığı ve etkinlik düzeyi okunur; düşük sıcaklık etkinliği azaltır (geri dönüşlü), yüksek sıcaklık yapıyı bozar (geri dönüşsüz).','Düşük sıcaklıkta etkinliği az enzimin denatüre olduğunu sanmak; denatürasyonun soğutmayla geri döneceğini sanmak; etkinliğin sıcaklıkla sürekli arttığını sanmak.','orta',4,'byp-enzim-sicaklik','Enzim etkinliği–sıcaklık grafiği yorumlama',kalip='grafik')
def egri(T,topt,t0,t1,zirve,us=2.2,us2=1.5):
    if T<=t0 or T>=t1: return 0.0
    if T<=topt: return zirve*((T-t0)/(topt-t0))**us
    return zirve*(1-((T-topt)/(t1-topt))**us2)
EX=lambda T:egri(T,40,0,55,100); EY=lambda T:egri(T,60,10,75,80)
assert max(EX(t/10) for t in range(0,800))==100 and max(EY(t/10) for t in range(0,800))==80
assert EX(70)==0 and EY(20)<5 and EY(20)>0 and EY(60)>EY(20) and EX(40)>EY(40) and EY(40)<EY(60)/2 and EY(60)<EX(40)
cx=' '.join(f'({t/2:.1f},{EX(t/2):.1f})' for t in range(0,161)); cy=' '.join(f'({t/2:.1f},{EY(t/2):.1f})' for t in range(0,161))
b=['\\begin{axis}[width=7.6cm,height=5.2cm,xmin=0,xmax=80,ymin=0,ymax=115,xtick={0,10,20,30,40,50,60,70,80},ytick={0,50,100},axis lines=left,'
   'xlabel={Sıcaklık ($^\\circ$C)},ylabel={Enzim etkinliği},tick label style={font=\\footnotesize},label style={font=\\small},every axis plot/.append style={line width=1.4pt}]',
   f'\\addplot[black] coordinates {{{cx}}};',f'\\addplot[vurgu] coordinates {{{cy}}};',
   '\\node[font=\\small\\bfseries] at (axis cs:33,104) {X};\\node[font=\\small\\bfseries,vurgu] at (axis cs:66,88) {Y};','\\end{axis}']
SK6=tikz_svg('\\begin{tikzpicture}[font=\\small]\n'+'\n'.join(b)+'\n\\end{tikzpicture}')
dog6='20 °C’ta Y enzimi denatüre olmamıştır; ortam 60 °C’a ısıtılırsa etkinliği artar.'
Y61='X ve Y enzimlerinin etkinliği sıcaklık arttıkça sürekli yükselir; bu artış Y için daha yavaştır.'
Y62='Y enzimi, kendi optimum sıcaklığında X enziminin optimum sıcaklığındakinden daha yüksek etkinlik gösterir.'
Y63='70 °C’ta X enziminin yapısı bozulmuştur; ortam 40 °C’a soğutulursa X etkinliğini yeniden kazanır.'
Y64='20 °C’ta Y enzimi denatüre olmuştur; bu yüzden ortam ısıtılsa da etkinliği artmaz.'
assert EY(60)>EY(20) and EY(60)<EX(40) and EX(70)==0 and EX(40)>EX(30)>EX(20) and EX(50)<EX(40)   # Y61, Y62 yanlış; dog6 (grafik kısmı) doğru
ENZ=B('Enzim ve sıcaklık','enzimlerin etkinliği optimum sıcaklıkta en yüksektir; düşük sıcaklıkta etkinlik azalır ama enzim bozulmaz, sıcaklık artınca yeniden hızlanır · Yüksek sıcaklıkta enzimin yapısı bozulur (denatürasyon) ve soğutulunca eski hâline dönmez')
ENZ2=B('Enzimlerin özelliği','enzimler genellikle proteindir ve her enzimin optimum sıcaklığı ile pH değeri kendine özgüdür. Örnek: insan vücudundaki enzimlerin optimumu yaklaşık 37 °C’tadır')
q('0006',tipId='byp-enzim-sicaklik',tip='Enzim etkinliği–sıcaklık grafiği yorumlama',z='orta',alt='Enzimler',kaz='Enzim etkinliği–sıcaklık grafiğini okuyup düşük ve yüksek sıcaklığın enzim yapısına etkisini yorumlar.',kalip='grafik',
 kart='K-BYP-06 (enzim–sıcaklık) · X optimum 40 °C, Y optimum 60 °C',
 metin='Şekilde, X ve Y enzimlerinin etkinliğinin sıcaklıkla değişimi gösterilmiştir. Her iki enzim için de enzim miktarı, substrat miktarı ve pH eşit tutulmuştur.\nBuna göre, aşağıdakilerden hangisi doğrudur?',
 dogru=dog6,sira=yer('C',dog6,[Y63,Y61,Y64,Y62]),
 yan=[(Y61,'Grafikte etkinlik optimum sıcaklığa kadar artar, sonra azalır; sürekli artış yoktur. Her enzimin kendine özgü bir optimum sıcaklığı vardır.','bilgi'),
      (Y62,'Y’nin optimumundaki etkinlik 80, X’inki 100 düzeyindedir; Y’nin optimum sıcaklığı yüksek olsa da etkinliği X’inkinden düşüktür. Sıcaklık yüksek diye etkinlik yüksek değildir.','dikkat'),
      (Y63,'Yüksek sıcaklıkta enzimin yapısı bozulur (denatürasyon) ve bu geri dönüşsüzdür; soğutulunca X etkinliğini geri kazanamaz.','bilgi'),
      (Y64,'20 °C’ta Y’nin etkinliği düşüktür çünkü düşük sıcaklık tepkimeyi yavaşlatır; enzim bozulmaz. Sıcaklık optimuma yükseltilirse etkinlik artar. “Etkinlik az = denatüre” sanılmış.','bilgi')],
 istenen='Grafiğe ve enzim özelliklerine göre doğru olan ifade.',
 ip=['Grafikte düşük sıcaklık bölgesindeki etkinlik azalmasının nedeniyle yüksek sıcaklık bölgesindeki etkinlik kaybının nedenini ayrı ayrı düşün.'],
 bilgi=[ENZ,ENZ2],
 ad=[A('Eğrileri oku','X’in zirvesi yaklaşık 40 °C’ta (100), Y’nin zirvesi yaklaşık 60 °C’ta (80); iki eğri de zirveden sonra düşüp sıfıra iner.','Optimum sıcaklık: X için 40 °C, Y için 60 °C'),
     A('Düşük sıcaklığı değerlendir','20 °C’ta Y’nin etkinliği çok düşüktür; düşük sıcaklık etkinliği azaltır, yapıyı bozmaz.','Y, 20 °C’ta yavaş ama bozulmamış'),
     A('Yüksek sıcaklığı değerlendir','70 °C’ta X’in etkinliği sıfırdır; yüksek sıcaklık yapıyı bozar ve soğutmayla geri dönmez.','X, 70 °C’ta denatüre'),
     A('Şıkları ele','Y’yi 60 °C’a ısıtmak etkinliği artırır; diğer şıklar grafiğe ya da enzim özelliklerine aykırıdır.','Doğru: C')],
 puf='Düşük sıcaklık enzimi yavaşlatır (geri dönüşlü), yüksek sıcaklık yapıyı bozar (geri dönüşsüz); etkinlik azaldı diye denatürasyon varsayma.',sekil=SK6)

# =================== yaz ===================
for qq in P.ANA: qq['kardes']=None
P.yaz(os.path.join(BD,'biopilot-1.json'),'/tmp/bos-biopilot.json')
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=TIPK[c['tipId']]))['kartlar'].append(c['id'])
json.dump(dict(konu='Biyoloji (pilot)',surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 TYT Biyoloji dağılımı (yalnız mantık), MEB 9–10. sınıf biyoloji müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','biopilot.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
