"""AYT Kimya · Kimyasal Tepkimelerde Enerji · 2. dalga (tepenerjiiki) · 10 soru. Her cevap ve çeldirici Fraction ile hesaplanır, assert edilir."""
import sys,os,math,json
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-kim')); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
import _hafif_kim2 as H
from _hafif_kim2 import *
from cizim import tikz_svg
KONU_='Kimyasal Tepkimelerde Enerji'; UK='akim|Kimyasal Tepkimelerde Enerji'
H.KONU=KONU_
P=Parti('tepenerjiiki',KONU_,UK,ders='AYT Kimya',idon='aytkim')
KY='ÖSYM 2019–2026 AYT Kimya (Tepkimelerde Isı Değişimi, Oluşum Entalpisi; yalnız mantık) · MEB 11. sınıf Kimyasal Tepkimelerde Enerji'
TIPLER={'te-hal':'Hâl değişimi entalpileri ve entalpi diyagramı','te-yanma':'Yanma entalpisi','te-hess':'Hess yasası ve entalpi çevrimleri','te-kalori':'Kalorimetri ve ısı hesabı',
 'te-pe':'Potansiyel enerji diyagramı','te-bag':'Bağ enerjisi ve atomlaşma'}
CARD={}
def card(no,alt,fikir,tuzak,z,kalip,adim,tipId,ozet):
    kart(f'K-AKTE2-{no:02d}',alt,fikir,tuzak,z,kalip,adim,tipId,TIPLER[tipId],KY); CARD[no]=ozet
def q(no,cn,ad,**k):
    assert len(k['ip'])==1 and 3<=len(ad)<=7
    mk(P,no,ad=ad,adim=len(ad),kart=f'K-AKTE2-{cn:02d} ('+CARD[cn]+')',tip=TIPLER[k['tipId']],**k)
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
ARR='-{Stealth[length=2.2mm,width=1.8mm]}'
def tk(g): return tikz_svg(HEAD+g+TAIL)
def pg(opts,body):
    return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n\\begin{axis}['+opts+']\n'+body+'\n\\end{axis}\n\\end{tikzpicture}')
def co(pts): return ' '.join(f'({x:.3f},{y:.4f})' for x,y in pts)
def pe_fig(nodes,ticks,labels,sc=.04):
    """nodes=[(düzey,'p'|'t'|'v')]; ticks: eksende yazılacak düzeyler; labels: {düğüm:(metin,'a'|'b')}."""
    n=len(nodes); xs=[1.0+1.75*i for i in range(n)]; top=max(l for l,_ in nodes); wd={'p':.4,'v':.25,'t':0}
    path=''; prev=None
    for i,(L_,kd) in enumerate(nodes):
        x=xs[i]; s=(x-wd[kd],L_*sc); e=(x+wd[kd],L_*sc)
        if i==0: path+=f'({s[0]:.3f},{s[1]:.3f}) '
        else:
            dx=(s[0]-prev[0])*.5; path+=f'.. controls ({prev[0]+dx:.3f},{prev[1]:.3f}) and ({s[0]-dx:.3f},{s[1]:.3f}) .. ({s[0]:.3f},{s[1]:.3f}) '
        if wd[kd]>0: path+=f'-- ({e[0]:.3f},{e[1]:.3f}) '
        prev=e
    g=f'\\draw[thick,vurgu] {path};'
    xmax=xs[-1]+.8
    g+=f'\\draw[{ARR},thick] (0,0) -- (0,{top*sc+.6:.3f}); \\draw[{ARR},thick] (0,0) -- ({xmax+.2:.3f},0);'
    g+=f'\\node[rotate=90] at (-1.0,{top*sc/2+.3:.3f}) {{Potansiyel enerji (kJ)}};\\node[below] at ({xmax/2:.3f},-.05) {{Tepkime koordinatı}};'
    for v in ticks:
        xt=None
        for i,(L_,kd) in enumerate(nodes):
            if L_==v and xt is None: xt=xs[i]-wd[kd]
        assert xt is not None,v
        g+=f'\\draw[dashed,gray] (0,{v*sc:.3f}) -- ({xt:.3f},{v*sc:.3f}); \\draw (0,{v*sc:.3f}) -- (-.08,{v*sc:.3f}); \\node[left,inner sep=2pt] at (-.05,{v*sc:.3f}) {{{v}}};'
    for i,(t,pos) in labels.items():
        L_=nodes[i][0]
        g+=(f'\\node[above] at ({xs[i]:.3f},{L_*sc+.02:.3f}) {{{t}}};' if pos=='a' else f'\\node[below] at ({xs[i]:.3f},{L_*sc-.02:.3f}) {{{t}}};')
    return tk(g)
def ladder(levels,arrows,sc,W=8.2):
    """levels: (y,metin,'a'|'b',x0); arrows: (x,y1,y2,etiket,oran)."""
    g=''
    for y,t,pos,x0 in levels:
        g+=f'\\draw[thick] ({x0},{y*sc:.3f}) -- ({W},{y*sc:.3f});'
        g+=(f'\\node[above left,inner sep=2pt] at ({W},{y*sc:.3f}) {{{t}}};' if pos=='a' else f'\\node[below left,inner sep=2pt] at ({W},{y*sc:.3f}) {{{t}}};')
    for x,y1,y2,lab,fr in arrows:
        g+=f'\\draw[vurgu,very thick,{ARR}] ({x},{y1*sc:.3f}) -- ({x},{y2*sc:.3f}); \\node[right,inner sep=3pt] at ({x},{(y1+(y2-y1)*fr)*sc:.3f}) {{{lab}}};'
    g+=f'\\node[below,gray] at ({W/2},{min(y for y,_,_,_ in levels)*sc-.55:.3f}) {{\\footnotesize Şekil ölçekli değildir.}};'
    return tk(g)
SIR=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
SETS={'Yalnız I':{'I'},'Yalnız II':{'II'},'Yalnız III':{'III'},'I ve II':{'I','II'},'I ve III':{'I','III'},'II ve III':{'II','III'},'I, II ve III':{'I','II','III'}}
def onc(truth,why,pos):
    """truth: her öncülün doğruluğu; why: öncülün gerçek durumunu anlatan olgu cümleleri (küçük harfle başlar); pos: doğru şıkkın sırası."""
    nm=['I','II','III']; C={n for n,t in zip(nm,truth) if t}
    dogru=[s for s in SIR if SETS[s]==C][0]; p=SIR.index(dogru)
    cand=[s for s in SIR if s!=dogru]
    key=lambda s:(len(SETS[s]^C),abs(SIR.index(s)-p))
    bef=sorted([s for s in cand if SIR.index(s)<p],key=key)[:pos]; aft=sorted([s for s in cand if SIR.index(s)>p],key=key)[:4-pos]
    assert len(bef)==pos and len(aft)==4-pos,(dogru,pos)
    sec=bef+aft; yan=[]
    for s in sec:
        ex=sorted(SETS[s]-C,key=nm.index); ms=sorted(C-SETS[s],key=nm.index); parts=[]
        for n in ex: parts.append(f'{n}. yargıyı da doğru sanmış; oysa {why[nm.index(n)]}.')
        for n in ms: parts.append(f'{n}. yargının doğru olduğunu görememiş; {why[nm.index(n)]}.')
        yan.append((s,' '.join(parts),'bilgi' if ex else 'dikkat'))
    sira=sorted(sec+[dogru],key=SIR.index); assert sira.index(dogru)==pos
    return dict(dogru=dogru,sira=sira,yan=yan)
def tek(opts,hedef,pos):
    h=[o for o in opts if o[1]==hedef]; assert len(h)==1
    dg=h[0]; yn=[o for o in opts if o[1]!=hedef]
    sira=yn[:pos]+[dg]+yn[pos:]
    return dict(dogru=dg[0],sira=[x[0] for x in sira],yan=[(o[0],o[2],'bilgi') for o in yn])

# ---------- bilgi kutuları (örnekler soruların maddelerini/sayılarını kullanmaz)
HALB=B('Hâl değişimi entalpileri','erime, buharlaşma ve süblimleşme ısı alan (ΔH > 0), donma, yoğuşma ve kırağılaşma ısı veren (ΔH < 0) olaylardır. Ters olayın entalpisi aynı büyüklükte, zıt işaretlidir. Entalpi yoldan bağımsız olduğundan basamak ΔH’ları toplanır. Örnek: X(k) → X(s) için +a, X(s) → X(g) için +b ise X(k) → X(g) için +(a + b) olur')
YNB=B('Molar yanma entalpisi','1 mol maddenin standart koşullarda oksijenle tam yanması sırasındaki entalpi değişimidir; ürünler kararlı hâlde (CO₂(g), H₂O(s)) olmalıdır. Karbon CO’ya dönüşüyorsa yanma tamamlanmamıştır. Örnek: CH₃OH(s) + 3/2O₂(g) → CO₂(g) + 2H₂O(s) tepkimesinin ΔH’ı CH₃OH’ın molar yanma entalpisidir')
YN2B=B('Yanma ve oluşum entalpisi ilişkisi','yanma tepkimesinde ΔH = Σ n·ΔHf(ürünler) − Σ n·ΔHf(girenler) yazılır; O₂ elementtir ve ΔHf’i sıfırdır. Üç değerden ikisi biliniyorsa üçüncüsü bulunur. Örnek: bir yanma tepkimesinde ürünlerin oluşum entalpileri toplamı −900 kJ ve ΔH = −600 kJ ise girenlerin oluşum entalpileri toplamı −300 kJ’dir')
YN3B=B('Yanma entalpilerinden tepkime entalpisi','tepkimedeki maddelerin molar yanma entalpileri biliniyorsa tepkime ΔH’ı, katsayılar hesaba katılarak girenlerin yanma entalpileri toplamından ürünlerin yanma entalpileri toplamı çıkarılarak bulunur. Yanmayan maddenin (CO₂, H₂O gibi) yanma entalpisi sıfırdır. Örnek: 2P → Q tepkimesinde P için −100, Q için −150 kJ/mol ise ΔH = 2·(−100) − (−150) = −50 kJ olur')
HESB=B('Entalpi çevrimi','iki yoldan aynı ürüne gidilirse ΔH’lar eşittir; çevrimdeki bilinmeyen basamak diğerlerinin farkından bulunur. Tepkime ΔH’ı mol sayısına orantılıdır: ΔH’ın verildiği tepkimedeki madde miktarı kadar ısı alışverişi olur. Örnek: 2A → B için ΔH = +30 kJ ise 3 mol A için +45 kJ’dir')
KALB=B('Kalorimetre ve ısı','ısı yalıtımlı kapta q = m·c·ΔT ya da q = C·ΔT (C: ısı kapasitesi) bağıntısı kullanılır. Açığa çıkan ısı, ΔH ile tepkimeye giren sınırlayıcı maddenin mol sayısının çarpımına eşittir. Örnek: ΔH = −50 kJ/mol ve 0,2 mol madde harcanıyorsa 10 kJ ısı açığa çıkar')
KAL2B=B('Birden çok olayda ısı','kapta birden çok olay oluyorsa her olayın ısısı kendi mol sayısıyla ayrı hesaplanır ve toplanır; hangi maddenin tükendiğine bakılır. Örnek: ΔH₁ = −10 kJ/mol olan olayda 2 mol, ΔH₂ = −20 kJ/mol olan olayda 1 mol madde girerse toplam ısı 40 kJ’dir')
PEB=B('Çok basamaklı tepkime','her tepe bir basamağın aktivasyon enerjisini belirler: Ea = tepe − o basamağın başlangıç düzeyi. En büyük Ea’lı basamak en yavaş basamaktır ve hızı belirler. Ters yöndeki Ea = tepe − basamağın bitiş düzeyidir. ΔH = ürün − giren düzeyidir. Örnek: ara ürün 30, ikinci tepe 80 ise ikinci basamağın Ea’sı 50 kJ’dir')
BAGB=B('Atomlaşma çevrimi','elementlerden bileşiğe oluşum, önce elementlerin gaz atomlarına ayrışması sonra atomlardan bağ oluşması olarak da düşünülebilir. ΔHf = Σ(atomlaşma ve bağ kırılma ısıları) − Σ(oluşan bağ enerjileri). Katı elementin gaz atomuna geçişi (süblimleşme) ısı alır. Örnek: ΔHf(XH₂) = süblimleşme(X) + D(H–H) − 2·D(X–H)')
VRMB=B('Verim ve ısı','verimli tepkimelerde gerçekten oluşan ürün miktarı kadar ısı alışverişi olur. Önce girenlerden teorik ürün mol sayısı hesaplanır, verim yüzdesiyle çarpılarak gerçek ürün bulunur. Örnek: 5 mol teorik ürünün %60’ı 3 moldür')

# ================ kartlar
card(1,'Hâl değişimi entalpileri','Hâl değişimi entalpileri entalpi diyagramında basamak olarak toplanır; ters olayın ΔH’ı zıt işaretlidir ve mol sayısıyla orantılıdır.','Ters olayın işaretini değiştirmemek; basamak ΔH’larından birini atlamak.','kolay','grafik',3,'te-hal','hâl değişimi entalpi diyagramı')
card(2,'Molar yanma entalpisi tanımı','Molar yanma entalpisi, 1 mol yakıtın tam yanmasındadır; ürünler CO₂(g) ve H₂O(s) olmalıdır.','Eksik yanmayı ya da 2 mollük tepkimeyi molar yanma entalpisi sanmak.','kolay','tablo',2,'te-yanma','molar yanma entalpisi tanımı')
card(3,'Yanma ve oluşum entalpisi','Yanma entalpisi ile ürünlerin oluşum entalpileri verilince yakıtın oluşum entalpisi ΔH = ΣΔHf(ürün) − ΣΔHf(giren) denkleminden çözülür.','Katsayıları unutmak; işareti ters kurmak.','orta','tablo',4,'te-yanma','yanma entalpisinden oluşum entalpisi')
card(4,'Entalpi çevriminden ayrışma ısısı','Elementlerden iki yola ilişkin ΔH’ların farkı tepkime entalpisini verir; mol sayısıyla çarpılarak ısı bulunur.','Farkı ters almak; kütleyi mole çevirmemek.','orta','şekilli',4,'te-hess','çevrimden tepkime ısısı ve yargılar')
card(5,'Nötrleşme kalorimetresi','Sınırlayıcı maddenin mol sayısıyla ısı bölünerek molar nötrleşme entalpisi bulunur; kütle toplam çözelti kütlesidir.','Fazla maddeyi mol hesabında kullanmak; J ile kJ’yi karıştırmak.','orta','grafik',4,'te-kalori','nötrleşme ısısının kalorimetrik hesabı')
card(6,'Çok basamaklı tepkime diyagramı','Basamağın Ea’sı o basamağın tepesi ile başlangıç düzeyinin farkıdır, ters yöndeki Ea tepe ile bitiş düzeyinin farkıdır; en büyük Ea’lı basamak yavaştır.','Tepe düzeyini ya da toplam yüksekliği basamağın Ea’sı sanmak.','orta','şekilli',4,'te-pe','çok basamaklı diyagram yargıları')
card(7,'Yanma entalpilerinden tepkime entalpisi','Yanma entalpileri verilince tepkime ΔH’ı katsayılar hesaba katılarak girenlerle ürünlerin yanma ısıları karşılaştırılarak bulunur; ısı mol sayısıyla orantılıdır.','Çıkarmayı ters yapmak; yanma tepkimesi olmayan maddeyi kapsam dışı bırakmak.','orta','tablo',4,'te-yanma','yanma entalpisinden tepkime ısısı')
card(8,'Çözünme ve nötrleşme ısıları','İki olayın ısıları kendi mol sayılarıyla ayrı hesaplanır; sınırlayıcı madde nötrleşme miktarını belirler, toplam ısı ısı kapasitesine bölünür.','Nötrleşmeyi fazla maddeyle hesaplamak; çözünmeyi atlamak.','zor','şekilli',6,'te-kalori','iki aşamalı kalorimetre hesabı')
card(9,'Atomlaşma çevrimiyle bağ enerjisi','Oluşum entalpisi, atomlaşma ısılarının toplamı eksi oluşan bağ enerjileridir; bağ sayısı yapıdan bulunur.','Atomlaşmayı hesaba katmamak; H₂’nin bağ enerjisini 2 ile çarpmamak.','zor','şekilli',5,'te-bag','oluşum entalpisinden C–H bağ enerjisi')
card(10,'Yanma entalpisinden oluşum ve verim','Yanma entalpilerinden oluşum entalpisi bulunur; ısı, gerçekten oluşan ürün mol sayısıyla orantılıdır.','Verimi uygulamamak ya da iki kez uygulamak; C mol sayısı ile ürün mol sayısını karıştırmak.','zor','tablo',6,'te-hess','yanma entalpilerinden oluşum ve verimli ısı')

# ================ 01 · kolay · hâl değişimi, olumsuz kök
dH_er,dH_bu=6,44; dH_su=dH_er+dH_bu; assert dH_su==50
o1=[('Erime olayı ısı alan (endotermik) bir olaydır.',True,'Şemada H₂O(k) → H₂O(s) basamağı yukarı doğrudur; entalpi artar, olay endotermiktir ve ifade doğrudur.'),
    ('1 mol H₂O(g) yoğuşarak H₂O(s) olurken 44 kJ ısı açığa çıkar.',True,'Buharlaşmanın ters olayı yoğuşmadır; ΔH = −44 kJ olduğundan 44 kJ ısı açığa çıkar ve ifade doğrudur.'),
    ('H₂O(k) → H₂O(g) olayının entalpi değişimi +50 kJ’dir.',True,'İki basamağın ΔH’ları toplanır: 6 + 44 = +50 kJ; ifade doğrudur.'),
    ('H₂O(g) → H₂O(k) olayının entalpi değişimi −38 kJ’dir.',False,'Bu olay H₂O(k) → H₂O(g) olayının tersidir; ΔH = −(6 + 44) = −50 kJ olur, −38 kJ yanlıştır.'),
    ('2 mol H₂O(k) eriyerek H₂O(s) olurken ortamdan 12 kJ ısı soğurulur.',True,'1 mol için +6 kJ olduğundan 2 mol için 2 × 6 = +12 kJ ısı alınır; ifade doğrudur.')]
assert 6+44==50 and -(6+44)!=-38 and 2*6==12 and 44-6==38
r1=tek(o1,False,0)
SK=ladder([(0,'H$_2$O(k)','a',0),(40,'H$_2$O(s)','a',0),(100,'H$_2$O(g)','a',2.3)],[(.6,0,40,'$\\Delta H_1=+6$ kJ',.5),(3.4,40,100,'$\\Delta H_2=+44$ kJ',.5)],.04)
q('0001',1,[A('Şemayı oku','Basamak ΔH’ları: H₂O(k) → H₂O(s) için +6 kJ, H₂O(s) → H₂O(g) için +44 kJ verilmiştir.','+6 kJ ve +44 kJ'),
   A('Her ifadeyi sına','Toplam, ters olay ve mol sayısı kurallarıyla beş ifade kontrol edilir.','Dört ifade şemayla uyumlu'),
   A('Hatalıyı bul','H₂O(g) → H₂O(k) olayının ΔH’ı −(6 + 44) = −50 kJ’dir, −38 kJ değildir.','−38 kJ ifadesi yanlış')],
 tipId='te-hal',z='kolay',alt='Hâl Değişimi Entalpileri',kaz='Hâl değişimlerinin entalpi şemasından toplam ve ters olay entalpilerine ilişkin yargıları değerlendirir.',kalip='grafik',
 metin='Şekilde, sabit sıcaklıkta gerçekleştiği kabul edilen hâl değişimlerinde 1 mol H₂O için entalpi değişimleri verilmiştir.\nBuna göre aşağıdakilerden hangisi yanlıştır?',
 sekil=SK,dogru=r1['dogru'],yan=r1['yan'],sira=r1['sira'],istenen='Yanlış olan ifade.',
 ip=['Her ifadede olayın yönünü ve kaç mol madde için söylendiğini şemayla karşılaştır.'],bilgi=[HALB],
 puf='Yön ters çevrilirse ΔH işaret değiştirir; art arda basamakların ΔH’ları toplanır.')

# ================ 02 · kolay · yanma tanımı, tablo, öncüllü
rx=[('I','C₂H₆(g) + 7/2O₂(g) → 2CO₂(g) + 3H₂O(s)','−1560'),('II','C(grafit) + 1/2O₂(g) → CO(g)','−110'),('III','2H₂(g) + O₂(g) → 2H₂O(s)','−572')]
SK=tablo_svg(['No','Tepkime','ΔH (kJ)'],[list(r) for r in rx])
w2=onc([True,False,False],['tepkimede 1 mol C₂H₆ tam yanarak CO₂(g) ve H₂O(s) vermektedir, bu nedenle ΔH molar yanma entalpisidir',
  'tepkimede karbon tam yanmayıp CO’ya dönüşmektedir, bu nedenle ΔH molar yanma entalpisi değildir',
  'tepkimede 2 mol H₂ yanmaktadır, ΔH 1 mol için olmadığından molar yanma entalpisi değildir'],0)
q('0002',2,[A('Tanımı hatırla','Molar yanma entalpisi 1 mol yakıtın tam yanmasındaki ΔH’tır; ürünler CO₂(g) ve H₂O(s) olur.','1 mol yakıt · tam yanma'),
   A('Tepkimeleri tara','I’de 1 mol C₂H₆ tam yanıyor; II’de ürün CO; III’te 2 mol H₂ yanıyor.','I: evet · II: hayır · III: hayır'),
   A('Sonucu birleştir','Yalnız I’in ΔH’ı molar yanma entalpisidir.','Yalnız I')],
 tipId='te-yanma',z='kolay',alt='Yanma Entalpisi',kaz='Verilen tepkimelerden hangisinin entalpi değişiminin molar yanma entalpisi olduğunu belirler.',kalip='tablo',
 metin='Standart koşullarda gerçekleşen üç tepkime ve entalpi değişimleri tabloda verilmiştir.\nBuna göre bu tepkimelerden hangilerinin ΔH değeri, yakıt olan maddenin standart molar yanma entalpisine eşittir?',
 sekil=SK,dogru=w2['dogru'],yan=w2['yan'],sira=w2['sira'],istenen='ΔH’ı molar yanma entalpisi olan tepkimeler.',
 ip=['Her tepkimede yanan madde miktarına ve ürünlerin ne olduğuna bak.'],bilgi=[YNB],
 puf='Yanma tam olmalı ve tepkimede yakıtın tam 1 molü yanmalıdır.')

# ================ 03 · orta · yanma → oluşum
hy,hco,hh2o=-2877,-394,-286
prod=4*hco+5*hh2o; assert prod==-3006
hf3=prod-hy; assert hf3==-129
w_a=-prod+0  # yer tutucu
d1=hf3*-1                               # +129 işaret
d2=(hco+hh2o)-hy; assert d2==2197       # katsayısız
d3=(4*hco+hh2o)-hy; assert d3==1015     # H₂O katsayısı 1
d4=prod+hy; assert d4==-5883            # yanma ΔH’ını toplama eklemiş
assert len({hf3,d1,d2,d3,d4})==5
SK=tablo_svg(['Madde','Entalpi türü','Değer (kJ/mol)'],[['C₄H₁₀(g)','standart yanma','−2877'],['CO₂(g)','standart oluşum','−394'],['H₂O(s)','standart oluşum','−286']])
q('0003',3,[A('Yanma tepkimesini yaz','1 mol C₄H₁₀ yanınca 4 mol CO₂ ve 5 mol H₂O(s) oluşur.','C₄H₁₀ + 13/2O₂ → 4CO₂ + 5H₂O'),
   A('Ürünlerin toplamını bul','Katsayılarla çarpılan oluşum entalpileri toplanır.','4 × (−394) + 5 × (−286) = −3006 kJ'),
   A('Yanma ΔH’ını yaz','ΔH = Σ ΔHf(ürün) − Σ ΔHf(giren); O₂ elementtir, sıfırdır.','−2877 = −3006 − ΔHf(C₄H₁₀)'),
   A('Bilinmeyeni çöz','ΔHf(C₄H₁₀) = −3006 + 2877.','ΔHf(C₄H₁₀) = −129 kJ/mol')],
 tipId='te-yanma',z='orta',alt='Yanma ve Oluşum Entalpisi',kaz='Yanma entalpisi ve ürünlerin oluşum entalpilerinden yakıtın oluşum entalpisini hesaplar.',kalip='tablo',
 metin='Tabloda bazı maddelerin 25 °C’deki standart entalpi değerleri verilmiştir.\nBuna göre C₄H₁₀(g) + 13/2O₂(g) → 4CO₂(g) + 5H₂O(s) tepkimesinden yararlanılarak C₄H₁₀(g)’nin standart oluşum entalpisi kaç kJ/mol bulunur?',
 sekil=SK,dogru=hf3,yan=[(d1,'Bulduğu −129 kJ/mol değerinin işaretini ters yazmış; ürün − giren farkını ters kurmuştur.','islem'),
  (d2,'Ürünlerin katsayılarını unutarak −394 − 286 = −680 almış ve −680 + 2877 = +2197 bulmuştur.','dikkat'),
  (d3,'H₂O’nun katsayısını 1 almış: 4 × (−394) + (−286) = −1862; −1862 + 2877 = +1015 bulmuştur.','dikkat'),
  (d4,'Yanma entalpisini ürünlerin oluşum entalpileri toplamına ekleyerek −3006 − 2877 = −5883 bulmuştur.','bilgi')],
 istenen='C₄H₁₀(g)’nin standart oluşum entalpisi (kJ/mol).',ip=['Tabloda hangi üç değerin verildiğini, hangisinin istendiğini belirle.'],bilgi=[YN2B],
 puf='Yanma ΔH’ı ile ürünlerin oluşum entalpileri toplamı arasındaki farkı bilinmeyene bağla.')

# ================ 04 · orta · CaCO₃ çevrimi, öncüllü
hfc,hfo=-1207,-1029; dH4=hfo-hfc; assert dH4==178
n4=Fr(50,100); q4=n4*dH4; assert q4==89
SK=ladder([(0,'Ca(k) + C(grafit) + 3/2O$_2$(g)','a',0),(-55,'CaO(k) + CO$_2$(g)','a',0),(-100,'CaCO$_3$(k)','b',0)],
 [(.5,0,-100,'$\\Delta H_1=-1207$ kJ',.25),(5.3,0,-55,'$\\Delta H_2=-1029$ kJ',.5)],.04)
w4=onc([True,True,False],['CaO(k) + CO₂(g) düzeyi CaCO₃(k) düzeyinden 178 kJ yukarıdadır; ayrışma tepkimesinin ΔH’ı +178 kJ’dir',
  '50 g CaCO₃ 0,5 mol eder ve 0,5 × 178 = 89 kJ ısı soğurur',
  'CaO(k) + CO₂(g) → CaCO₃(k) tepkimesinin ΔH’ı −178 kJ’dir; ısı verir, endotermik değildir'],2)
q('0004',4,[A('İki yolu karşılaştır','Elementlerden CaCO₃’a ΔH₁ = −1207, CaO + CO₂’ye ΔH₂ = −1029 kJ.','CaCO₃ daha aşağıda'),
   A('Ayrışma ΔH’ını bul','ΔH = H(ürün) − H(giren) = −1029 − (−1207).','CaCO₃ → CaO + CO₂: +178 kJ'),
   A('Kütleyi mole çevir','50 g ÷ 100 g/mol = 0,5 mol CaCO₃.','n = 0,5 mol'),
   A('Yargıları değerlendir','0,5 × 178 = 89 kJ ısı alınır; ters tepkime ekzotermiktir.','I: doğru · II: doğru · III: yanlış')],
 tipId='te-hess',z='orta',alt='Entalpi Çevrimi',kaz='Entalpi şemasından ayrışma tepkimesinin entalpisini bulur ve kütleyle ilişkilendirerek yargıları değerlendirir.',kalip='şekilli',
 metin='Şekilde, Ca(k), C(grafit) ve O₂(g) elementlerinden CaCO₃(k) ile CaO(k) + CO₂(g) karışımına ulaşılması entalpi düzeylerinde gösterilmiştir. Standart koşullarda CaCO₃’ın mol kütlesi 100 g/mol’dür.\nBuna göre,\nI. CaCO₃(k) → CaO(k) + CO₂(g) tepkimesinin entalpi değişimi +178 kJ’dir.\nII. 50 g CaCO₃(k) ayrışırken ortamdan 89 kJ ısı soğurulur.\nIII. CaO(k) + CO₂(g) → CaCO₃(k) tepkimesi endotermiktir.\nyargılarından hangileri doğrudur?',
 sekil=SK,dogru=w4['dogru'],yan=w4['yan'],sira=w4['sira'],istenen='Doğru olan yargılar.',
 ip=['Şemada hangi iki yolun aynı düzeye gittiğine dikkat et.'],bilgi=[HESB],
 puf='ΔH = ürün düzeyi − giren düzeyi; ısı, mol sayısıyla orantılıdır.')

# ================ 05 · orta · nötrleşme kalorimetresi
Vh,Mh,Vn,Mn=50,Fr(1),50,Fr(6,5)
nh=Vh*Mh/1000; nn=Vn*Mn/1000; assert (nh,nn)==(Fr(1,20),Fr(3,50)) and nh<nn
mm=Vh+Vn; Tdelta=27-20; qJ=Fr(mm)*Fr(21,5)*Tdelta; assert qJ==2940
dH5=-qJ/nh/1000; assert dH5==Fr(-294,5)
y1=-qJ/nn/1000; assert y1==-49
y2=-(Fr(Vh)*Fr(21,5)*Tdelta)/nh/1000; assert y2==Fr(-147,5)
y3=-dH5; y4=-qJ/nh; assert y4==-58800
assert len({dH5,y1,y2,y3,y4})==5
tt=[(0,20),(2,20)]+[(2+s/10,20+7*(s/10)) for s in range(1,11)]+[(10,27)]
SK=pg('width=6.8cm,height=5cm,axis lines=left,xmin=0,xmax=10,ymin=18,ymax=30,xtick={0,2,4,6,8,10},ytick distance=2,extra y ticks={27},extra y tick labels={27},grid=major,major grid style={gray!45,thin},xlabel={Zaman (dk)},ylabel={Sıcaklık ($^\\circ$C)},label style={font=\\small},tick label style={font=\\small}',
 f'\\addplot[thick,color=blue!70!black] coordinates {{{co(tt)}}};\n\\draw[dashed,gray] (axis cs:0,27) -- (axis cs:3,27);\n\\node[anchor=west,font=\\small] at (axis cs:4,22.6) {{karıştırma}};\n\\draw[-{{Stealth}},thick] (axis cs:4,22.3) -- (axis cs:2.15,20.4);')
q('0005',5,[A('Çözelti kütlesini bul','Çözeltilerin yoğunluğu 1 g/mL olduğundan iki hacim toplanır.','50 + 50 = 100 g'),
   A('Isıyı hesapla','ΔT grafikten 27 − 20 = 7 °C; q = m·c·ΔT.','q = 100 × 4,2 × 7 = 2940 J'),
   A('Sınırlayıcıyı bul','HCl 0,05 mol, NaOH 0,06 mol; tepkime 0,05 mol H₂O oluşturur.','n(H₂O) = 0,05 mol'),
   A('Molar entalpiyi yaz','ΔH = −q ÷ n ve J → kJ.','ΔH = −2940 ÷ 0,05 = −58 800 J/mol = −58,8 kJ/mol')],
 tipId='te-kalori',z='orta',alt='Nötrleşme Isısı',kaz='Kalorimetre deneyinin sıcaklık–zaman grafiğinden sınırlayıcı bileşene göre molar nötrleşme entalpisini hesaplar.',kalip='grafik',
 metin='Isı yalıtımlı bir kalorimetre kabında 50 mL 1,0 M HCl çözeltisi ile 50 mL 1,2 M NaOH çözeltisi karıştırılıyor. Karışımın sıcaklığının zamanla değişimi grafikte verilmiştir. Çözeltilerin yoğunluğu 1 g/mL, özısısı 4,2 J/g·°C’dir; kalorimetre kabı ısı almamaktadır.\nBuna göre bu sıcaklıkta H⁺(suda) + OH⁻(suda) → H₂O(s) tepkimesinin entalpi değişimi kaç kJ/mol’dür?',
 sekil=SK,dogru=dH5,yan=[(y1,'Mol sayısı olarak fazla olan NaOH’ın 0,06 molünü kullanmış: 2940 ÷ 0,06 = 49 000 J/mol = −49 kJ/mol bulmuştur.','dikkat'),
  (y2,'Çözelti kütlesini yalnız HCl çözeltisinin 50 g’ı almış: 1470 ÷ 0,05 = 29 400 J/mol = −29,4 kJ/mol bulmuştur.','islem'),
  (y3,'Hesabı doğru yapıp ısının açığa çıktığını görmemiş; ekzotermik tepkimede ΔH negatif olduğundan işareti yanlış yazmıştır.','bilgi'),
  (y4,'2940 J ÷ 0,05 mol = 58 800 J/mol değerini kJ’ye çevirmeden yazmıştır.','islem')],
 istenen='Nötrleşme tepkimesinin entalpi değişimi (kJ/mol).',ip=['Karışımda hangi maddenin artakaldığını düşün.'],bilgi=[KALB],
 puf='Molar entalpi, tepkimeye tam giren maddenin mol sayısı başınadır; birimi kJ/mol’e çevir.')

# ================ 06 · orta · üç basamaklı PE diyagramı, öncüllü
R6,T16,I6,T26,I26,T36,P6=20,80,50,130,40,90,30
ea1=T16-R6; ea2=T26-I6; ea3=T36-I26; dH6=P6-R6; rev3=T36-P6
assert (ea1,ea2,ea3,dH6,rev3)==(60,80,50,10,60) and ea2>ea1 and ea2>ea3
SK=pe_fig([(R6,'p'),(T16,'t'),(I6,'v'),(T26,'t'),(I26,'v'),(T36,'t'),(P6,'p')],[R6,P6,I26,I6,T16,T36,T26],{0:('A','a'),2:('B','b'),4:('C','b'),6:('D','a')})
w6=onc([True,False,True],['girenin düzeyi 20, ürünün düzeyi 30 kJ’dir; ΔH = 30 − 20 = +10 kJ’dir',
  'basamakların aktivasyon enerjileri 60, 80 ve 50 kJ’dir; en büyüğü ikinci basamaktadır, yavaş basamak üçüncü değil ikincidir',
  'üçüncü basamağın ters yöndeki aktivasyon enerjisi tepe − bitiş düzeyi = 90 − 30 = 60 kJ’dir'],4)
q('0006',6,[A('Düzeyleri oku','A: 20, 1. tepe: 80, B: 50, 2. tepe: 130, C: 40, 3. tepe: 90, D: 30 kJ.','20 · 80 · 50 · 130 · 40 · 90 · 30'),
   A('Basamakların Ea’sını bul','Her basamakta Ea = tepe − o basamağın başlangıcı.','Ea₁ = 60 · Ea₂ = 80 · Ea₃ = 50 kJ'),
   A('ΔH ve ters Ea’yı bul','ΔH = ürün − giren; ters Ea = tepe − bitiş düzeyi.','ΔH = +10 kJ · 3. basamak ters Ea = 60 kJ'),
   A('Yargıları sına','ΔH = +10 kJ; yavaş basamak ikincidir; üçüncü basamağın ters Ea’sı 60 kJ’dir.','I: doğru · II: yanlış · III: doğru')],
 tipId='te-pe',z='orta',alt='Çok Basamaklı Tepkime',kaz='Üç basamaklı tepkimenin potansiyel enerji diyagramından ΔH, basamak aktivasyon enerjileri ve ters yöndeki aktivasyon enerjisini değerlendirir.',kalip='şekilli',
 metin='Şekilde, A(g) → B(g) → C(g) → D(g) şeklinde üç basamakta gerçekleşen bir tepkimenin potansiyel enerji–tepkime koordinatı diyagramı verilmiştir.\nBuna göre,\nI. Tepkimenin entalpi değişimi +10 kJ’dir.\nII. Hızı belirleyen yavaş basamak, üçüncü basamaktır.\nIII. Üçüncü basamağın ters yöndeki aktivasyon enerjisi 60 kJ’dir.\nyargılarından hangileri doğrudur?',
 sekil=SK,dogru=w6['dogru'],yan=w6['yan'],sira=w6['sira'],istenen='Doğru olan yargılar.',
 ip=['Her basamağın aktivasyon enerjisini kendi başlangıç düzeyine göre ayrı ayrı değerlendir.'],bilgi=[PEB],
 puf='Basamak Ea’sı = tepe − o basamağın başlangıç düzeyidir; toplam ΔH uçların farkıdır.')

# ================ 07 · orta · yanma entalpilerinden tepkime entalpisi
yC2H2,yH2,yC2H6=-1300,-286,-1560
dH7=(yC2H2+2*yH2)-yC2H6; assert dH7==-312
n7=Fr(13,26); r7=n7*dH7; assert r7==-156
e1=dH7; e2=-r7; e3=(yC2H2+2*yH2+yC2H6)*n7; e4=(yC2H2-yC2H6)*n7
assert (e3,e4)==(-1716,130) and len({r7,e1,e2,e3,e4})==5
SK=tablo_svg(['Madde','Molar yanma entalpisi (kJ/mol)'],[['C₂H₂(g)','−1300'],['H₂(g)','−286'],['C₂H₆(g)','−1560']])
q('0007',7,[A('Hess ilişkisini kur','Yanma entalpileriyle ΔH = Σ(girenlerin yanma ΔH’ı) − Σ(ürünlerin yanma ΔH’ı).','ΔH = [ΔH(C₂H₂) + 2·ΔH(H₂)] − ΔH(C₂H₆)'),
   A('1 mol için hesapla','Değerler yerine yazılır.','(−1300 − 572) − (−1560) = −312 kJ'),
   A('Mol sayısını bul','13 g ÷ 26 g/mol.','n(C₂H₂) = 0,5 mol'),
   A('Isıyı bul','ΔH’ı mol sayısıyla çarp.','0,5 × (−312) = −156 kJ')],
 tipId='te-yanma',z='orta',alt='Yanma Entalpilerinden Tepkime Entalpisi',kaz='Yanma entalpilerinden hidrojenlenme tepkimesinin entalpisini bulur ve kütleyle ilişkilendirir.',kalip='tablo',
 metin='Tabloda bazı gazların standart molar yanma entalpileri verilmiştir. C₂H₂’nin mol kütlesi 26 g/mol’dür.\nBuna göre standart koşullarda C₂H₂(g) + 2H₂(g) → C₂H₆(g) tepkimesinde 13 g C₂H₂(g) harcandığında entalpi değişimi kaç kJ olur?',
 sekil=SK,dogru=r7,yan=[(e1,'Tepkime entalpisini (−312 kJ) bulmuş ama 13 g C₂H₂’nin 0,5 mol olduğunu hesaba katmamıştır.','dikkat'),
  (e2,'Yanma entalpilerini ürün − giren sırasıyla çıkarmış: (−1560) − (−1872) = +312; 0,5 ile çarparak +156 bulmuştur.','islem'),
  (e3,'Girenlerle ürünün yanma entalpilerini toplayıp 0,5 ile çarpmıştır: (−1300 − 572 − 1560) × 0,5 = −1716.','bilgi'),
  (e4,'H₂’nin yanma entalpisini hesaba katmamıştır: (−1300) − (−1560) = +260; 0,5 ile çarparak +130 bulmuştur.','dikkat')],
 istenen='13 g C₂H₂(g) harcanırken entalpi değişimi (kJ).',ip=['Tablodaki değerlerin hangi maddelere ait olduğuna ve tepkime katsayılarına dikkat et.'],bilgi=[YN3B],
 puf='Yanma entalpileriyle çalışırken tepkimedeki katsayıları ve harcanan madde miktarını unutma.')

# ================ 08 · zor · çözünme + nötrleşme kalorimetresi
n8N=Fr(4,40); n8H=Fr(50*1,1000); assert (n8N,n8H)==(Fr(1,10),Fr(1,20))
q8a=n8N*44; q8b=n8H*56; Q8=q8a+q8b; assert Q8==Fr(36,5)
C8=400; dT8=Q8*1000/C8; assert dT8==18
T8=20+dT8
f8=[20+(n8N*44*1000)/C8, 20+(n8H*56*1000)/C8, 20+((n8N*44+n8N*56)*1000)/C8, 20+(n8N*56*1000)/C8]
assert f8==[31,27,45,34] and T8==38 and len(set(f8+[T8]))==5
g=('\\draw[gray,dashed] (-.35,-.35) rectangle (3.35,2.75);'
   '\\fill[blue!12] (0,0) rectangle (3,1.5); \\draw[thick] (0,2.4) -- (0,0) -- (3,0) -- (3,2.4);'
   '\\node at (1.2,.95) {\\small 50 mL 1,0 M}; \\node at (1.2,.5) {\\small HCl(suda)};'
   '\\draw[thick] (2.65,.25) -- (2.65,2.9); \\draw[thick,fill=white] (2.55,2.9) rectangle (2.75,3.1);'
   '\\node[anchor=west] at (2.85,3.0) {\\small $T_i=20\\,^\\circ$C};'
   f'\\draw[vurgu,very thick,{ARR}] (.8,3.2) -- (.8,1.7); \\node[anchor=south] at (.8,3.25) {{\\small 4 g NaOH(k)}};'
   '\\node[gray] at (1.5,-.65) {\\footnotesize Isı yalıtımlı kalorimetre};')
SK=tk(g)
q('0008',8,[A('Mol sayılarını bul','NaOH: 4 ÷ 40 = 0,1 mol; HCl: 0,05 L × 1,0 M = 0,05 mol.','n(NaOH) = 0,1 · n(HCl) = 0,05 mol'),
   A('Çözünme ısısını hesapla','0,1 mol NaOH’ın tamamı çözünür.','0,1 × 44 = 4,4 kJ'),
   A('Nötrleşme ısısını hesapla','H⁺ tükenir; yalnız 0,05 mol OH⁻ nötrleşir.','0,05 × 56 = 2,8 kJ'),
   A('Toplam ısıyı bul','İki ısı toplanır.','4,4 + 2,8 = 7,2 kJ = 7200 J'),
   A('Sıcaklık artışını bul','ΔT = q ÷ C.','7200 ÷ 400 = 18 °C'),
   A('Son sıcaklığı yaz','Başlangıç 20 °C.','20 + 18 = 38 °C')],
 tipId='te-kalori',z='zor',alt='Çözünme ve Nötrleşme Isıları',kaz='Çözünme ve nötrleşme entalpilerini sınırlayıcı maddeye göre birleştirerek kalorimetredeki son sıcaklığı hesaplar.',kalip='şekilli',
 metin='Şekildeki ısı yalıtımlı kalorimetre kabında HCl çözeltisi bulunmaktadır. Bu çözeltiye şekilde belirtilen miktarda NaOH katısı ekleniyor; katının tamamı çözünüyor ve nötrleşme tam olabildiği kadar gerçekleşiyor.\nNaOH(k) → Na⁺(suda) + OH⁻(suda)    ΔH = −44 kJ/mol\nH⁺(suda) + OH⁻(suda) → H₂O(s)    ΔH = −56 kJ/mol\nKap ile içindekilerin toplam ısı kapasitesi 400 J/°C ve NaOH’ın mol kütlesi 40 g/mol olduğuna göre, karışımın en yüksek sıcaklığı kaç °C’dir?',
 sekil=SK,dogru=T8,yan=[(f8[0],'Yalnız çözünme ısısını hesaba katmış: 4400 ÷ 400 = 11 °C artış, 31 °C bulmuştur; nötrleşmeyi atlamıştır.','dikkat'),
  (f8[1],'Yalnız nötrleşme ısısını hesaba katmış: 2800 ÷ 400 = 7 °C artış, 27 °C bulmuştur; çözünmeyi atlamıştır.','dikkat'),
  (f8[2],'Nötrleşmeyi 0,1 mol OH⁻ ile hesaplamış: (4,4 + 5,6) kJ = 10 000 J, 25 °C artış ve 45 °C bulmuştur; HCl’nin yalnız 0,05 mol olduğunu görmemiştir.','bilgi'),
  (f8[3],'Çözünme ısısını hesaba katmadan nötrleşmeyi 0,1 mol için almış: 5600 ÷ 400 = 14 °C artış, 34 °C bulmuştur.','islem')],
 istenen='Karışımın ulaştığı en yüksek sıcaklık (°C).',ip=['Şekildeki verilerden iki maddenin mol sayısını bul ve karşılaştır.'],bilgi=[KAL2B],
 puf='Her olayın ısısı, o olaya gerçekten katılan madde miktarıyla hesaplanır.')

# ================ 09 · zor · atomlaşma çevrimi ve C–H bağ enerjisi
sub,hh,hfm=717,436,-75
atom=sub+2*hh; assert atom==1589
D9=Fr(atom-hfm,4); assert D9==416
g1=Fr(atom,4); g2=Fr(sub+hh-hfm,4); g3=Fr(atom+hfm,4); g4=Fr(2*hh-hfm,4)
assert (g1,g2,g3,g4)==(Fr(1589,4),Fr(1228,4),Fr(1514,4),Fr(947,4)) and len({D9,g1,g2,g3,g4})==5 and D9==max(D9,g1,g2,g3,g4)
SK=ladder([(100,'C(g) + 4H(g)','a',0),(0,'C(k) + 2H$_2$(g)','a',0),(-30,'CH$_4$(g)','b',0)],
 [(.5,0,100,'$\\Delta H_1=?$',.5),(2.0,0,-30,'$\\Delta H_3=-75$ kJ',.5),(5.9,100,-30,'$\\Delta H_2=?$',.5)],.04)
q('0009',9,[A('Atomlaşma ısısını bul','C(k) → C(g) için +717 kJ; 2 mol H₂ → 4 mol H için 2 × 436 kJ.','ΔH₁ = 717 + 872 = +1589 kJ'),
   A('Çevrimi kur','İki yoldan aynı ürüne gidilir: ΔH₁ + ΔH₂ = ΔH₃.','1589 + ΔH₂ = −75'),
   A('Bağ oluşumunu çöz','ΔH₂ = −1664 kJ; CH₄’te 4 eş C–H bağı oluşur.','4 × D(C–H) = 1664'),
   A('Bağ enerjisini bul','Bir bağ için 1664 ÷ 4.','D(C–H) = 416 kJ/mol')],
 tipId='te-bag',z='zor',alt='Atomlaşma Çevrimi',kaz='Oluşum entalpisi, atomlaşma ısısı ve H–H bağ enerjisinden yararlanarak C–H bağ enerjisini bulur.',kalip='şekilli',
 metin='Şekilde, C(k) ve H₂(g) elementlerinden CH₄(g)’ün oluşumu iki yoldan gösterilmiştir. Aşağıdaki değerler bilinmektedir.\nC(k) → C(g)    ΔH = +717 kJ/mol\nH–H bağ enerjisi = 436 kJ/mol\nCH₄’teki dört C–H bağı birbirine eşittir.\nBuna göre C–H bağ enerjisi kaç kJ/mol’dür?',
 sekil=SK,dogru=D9,yan=[(g1,'ΔH₃’ü (−75 kJ) hesaba katmamış: 1589 ÷ 4 = 397,25 bulmuştur.','dikkat'),
  (g2,'H–H bağını yalnız bir kez saymış: (717 + 436 + 75) ÷ 4 = 307 bulmuştur.','dikkat'),
  (g3,'ΔH₃’ün işaretini ters kullanmış: (1589 − 75) ÷ 4 = 378,5 bulmuştur.','islem'),
  (g4,'Karbonun atomlaşma ısısını atlamış: (872 + 75) ÷ 4 = 236,75 bulmuştur.','bilgi')],
 istenen='C–H bağ enerjisi (kJ/mol).',ip=['Şemadaki üç ΔH’ın birbirleriyle ilişkisini düşün.'],bilgi=[BAGB],
 puf='Bir bağın enerjisi, aynı tür bağların toplam enerjisinin bağ sayısına bölünmesiyle bulunur.')

# ================ 10 · zor · yanma entalpilerinden oluşum + verim
yC,yH,yE=-394,-286,-1411
hfE=2*yC+2*yH-yE; assert hfE==51
nC=Fr(120,12); nth=nC/2; nre=nth*Fr(4,5); Q10=nre*hfE; assert (nC,nth,nre,Q10)==(10,5,4,204)
h1=Fr(4,5)*hfE*1; h2=hfE; h3=Q10*Fr(4,5); h4=nth*hfE
assert (h1,h2,h3,h4)==(Fr(204,5),51,Fr(816,5),255) and len({Q10,h1,h2,h3,h4})==5
sorted_=sorted([Q10,h1,h2,h3,h4]); assert sorted_.index(Q10)==3
SK=tablo_svg(['Madde','Molar yanma entalpisi (kJ/mol)'],[['C(grafit)','−394'],['H₂(g)','−286'],['C₂H₄(g)','−1411']])
q('0010',10,[A('Oluşum entalpisini bul','2C + 2H₂ → C₂H₄: ΔH = [2·(−394) + 2·(−286)] − (−1411).','ΔHf(C₂H₄) = +51 kJ/mol'),
   A('Teorik ürünü bul','120 g ÷ 12 g/mol = 10 mol C; 2 mol C’den 1 mol C₂H₄ oluşur.','Teorik n(C₂H₄) = 5 mol'),
   A('Verimi uygula','Gerçekte oluşan miktar teorik değerin %80’idir.','5 × 0,8 = 4 mol'),
   A('Isıyı hesapla','Oluşan C₂H₄ mol sayısı ile ΔH çarpılır.','4 × 51 = 204 kJ soğurulur')],
 tipId='te-hess',z='zor',alt='Yanma Entalpisinden Oluşum ve Verim',kaz='Yanma entalpilerinden oluşum entalpisini bulur ve verimli tepkimede soğurulan ısıyı hesaplar.',kalip='tablo',
 metin='Tabloda bazı maddelerin standart molar yanma entalpileri verilmiştir.\n2C(grafit) + 2H₂(g) → C₂H₄(g)\ntepkimesi, 120 g grafit ve yeterli H₂(g) ile %80 verimle gerçekleştiriliyor. (C: 12 g/mol)\nBuna göre bu tepkimede ortamdan kaç kJ ısı soğurulur?',
 sekil=SK,dogru=Q10,yan=[(h1,'Tek tepkime ısısına (51 kJ) verimi uygulamış: 51 × 0,8 = 40,8 bulmuştur; oluşan mol sayısını hesaplamamıştır.','dikkat'),
  (h2,'Bulduğu ΔH’ı (+51 kJ) 120 g grafit için de aynen yazmıştır; mol sayısını hesaba katmamıştır.','dikkat'),
  (h3,'Verimi iki kez uygulamış: 5 mol × 0,8 × 0,8 = 3,2 mol ve 3,2 × 51 = 163,2 kJ bulmuştur.','islem'),
  (h4,'Verimi hiç uygulamamış: teorik 5 mol C₂H₄ için 5 × 51 = 255 kJ bulmuştur.','bilgi')],
 istenen='Soğurulan ısı (kJ).',ip=['Isının hangi madde miktarıyla orantılı olduğunu düşün.'],bilgi=[VRMB],
 puf='Isı, teorik değil gerçekte oluşan ürün miktarıyla orantılıdır.')

# ================ yaz
for qq in P.ANA: qq['kardes']=None
SC='/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/tepenerjiiki'; os.makedirs(SC,exist_ok=True)
P.yaz(os.path.join(GD,'tepenerjiiki-1.json'),os.path.join(SC,'bos-tepenerjiiki.json'))
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=UK))['kartlar'].append(c['id'])
json.dump(dict(konu=KONU_,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2019–2026 AYT Kimya (yalnız mantık), MEB 11. sınıf kimya.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','aktepenerjiiki.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
