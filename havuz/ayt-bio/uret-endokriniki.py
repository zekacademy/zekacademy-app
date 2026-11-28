"""AYT Biyoloji · Endokrin Sistem · 2. dalga · 10 soru (kardeş yok, ipucu 1). Şekil verileri Python'da hesaplanır; öncüllerin doğru/yanlış değeri tek yerde."""
import sys,os,math,json
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-bio')); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
import _hafif_bio as H
from _hafif_bio import *
from cizim import tikz_svg
H.KONU='Endokrin Sistem'
KONU_K='abio|Endokrin Sistem'
P=Parti('endokriniki','Endokrin Sistem',KONU_K,ders='AYT Biyoloji',idon='aytbio')
KY='ÖSYM AYT 2018–2026 Biyoloji (Endokrin Sistem; yalnız mantık) · MEB 12. sınıf biyoloji'
TIPLER={'en2-yapi':'Bez yapıları ve hormon–hedef hücre ilişkisi','en2-su':'Hormonlarla su ve madde dengesi','en2-ritim':'Biyolojik ritim ve melatonin',
 'en2-bozuk':'Hormon eksikliği ve fazlalığı','en2-geri':'Hipofiz–hedef bez geri bildirimi','en2-glikoz':'Kan glikozu ve glukagon'}
CARD={}
def card(no,alt,fikir,tuzak,z,kalip,adim,tipId,ozet):
    kart(f'K-ABEN2-{no:02d}',alt,fikir,tuzak,z,kalip,adim,tipId,TIPLER[tipId],KY); CARD[no]=ozet
def q(no,cn,ad,**k):
    mk(P,no,ad=ad,adim=len(ad),kart=f'K-ABEN2-{cn:02d} ('+CARD[cn]+')',tip=TIPLER[k['tipId']],**k)
SIR=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
SETS={'Yalnız I':{'I'},'Yalnız II':{'II'},'Yalnız III':{'III'},'I ve II':{'I','II'},'I ve III':{'I','III'},'II ve III':{'II','III'},'I, II ve III':{'I','II','III'}}
def onc(truth,why,pos):
    nm=['I','II','III']; C={n for n,t in zip(nm,truth) if t}
    dogru=[s for s in SIR if SETS[s]==C][0]; p=SIR.index(dogru)
    cand=[s for s in SIR if s!=dogru]
    key=lambda s:(len(SETS[s]^C),abs(SIR.index(s)-p))
    bef=sorted([s for s in cand if SIR.index(s)<p],key=key)[:pos]; aft=sorted([s for s in cand if SIR.index(s)>p],key=key)[:4-pos]
    assert len(bef)==pos and len(aft)==4-pos,(dogru,pos)
    sec=bef+aft; yan=[]
    for s in sec:
        ex=sorted(SETS[s]-C,key=nm.index); ms=sorted(C-SETS[s],key=nm.index); parts=[]
        for n in ex: parts.append(f'{n}. yargıyı da doğru saymış; oysa {why[nm.index(n)]}.')
        for n in ms: parts.append(f'{n}. yargının doğru olduğunu görememiş; {why[nm.index(n)]}.')
        yan.append((s,' '.join(parts),'bilgi' if ex else 'dikkat'))
    sira=sorted(sec+[dogru],key=SIR.index); assert sira.index(dogru)==pos
    return dict(dogru=dogru,sira=sira,yan=yan)
def tek(opts,hedef,pos):
    assert len(opts)==5
    h=[o for o in opts if o[1]==hedef]; assert len(h)==1
    for o in opts:
        if o[1]==hedef: continue
        assert o[2].endswith('.') and not o[2].endswith('..') and len(o[2])>30
    dg=h[0]; yn=[o for o in opts if o[1]!=hedef]
    sira=yn[:pos]+[dg]+yn[pos:]
    return dict(dogru=dg[0],sira=[x[0] for x in sira],yan=[(o[0],o[2],'bilgi') for o in yn])
def tk(body,scale=1.0): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small,scale=%s]\n%s\n\\end{tikzpicture}'%(scale,body))
def ck(knots,n=12):
    pts=[]
    for (t0,y0),(t1,y1) in zip(knots,knots[1:]):
        for i in range(n+(1 if (t1,y1)==knots[-1] else 0)):
            u=i/n; pts.append((t0+(t1-t0)*u,y0+(y1-y0)*(1-math.cos(math.pi*u))/2))
    return pts
def co(pts): return ' '.join(f'({x:.3f},{y:.3f})' for x,y in pts)
def pg(opts,body):
    return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n\\begin{axis}['+opts+']\n'+body+'\n\\end{axis}\n\\end{tikzpicture}')
AXO='axis lines=left,label style={font=\\small},tick label style={font=\\small}'
def etk(n,x,y,x1,y1,x2,y2): return f'\\node[draw,circle,inner sep=1.6pt,font=\\small\\bfseries] at ({x},{y}) {{{n}}};\\draw[line width=.8pt] ({x1},{y1})--({x2},{y2});'
def argmin(pts): return min(pts,key=lambda p:p[1])[0]
def argmax(pts): return max(pts,key=lambda p:p[1])[0]
# ---- bilgi kutuları (sorunun öncülünü, sonucunu ya da sayısını söylemez)
PAN=B('Pankreas','pankreas, hem sindirim sisteminin hem de endokrin sistemin parçasıdır; bölümlerinden bazıları salgılarını kanalla boşaltır, bazıları ise kanalsız olarak doğrudan kana verir. Örnek: tükürük bezleri salgılarını kanalla ağıza boşaltır')
REC=B('Hormon ve reseptör','hormonlar kanla vücuttaki bütün hücrelere ulaşabilir; bir hücrenin yanıt verebilmesi, o hormona özgü reseptöre sahip olmasına bağlıdır. Reseptör ile hormonun şekil uyumu, anahtar–kilit ilişkisine benzer. Örnek: bir enzim de yalnız şekli uyan substrata bağlanır')
BOB=B('Böbreküstü bezi','böbreküstü bezi iki bölümden oluşur: dıştaki korteks ile içteki medulla. Bölümlerin her biri farklı hormonlar üretir ve hormonların salgılanmasını uyaran etkenler de farklıdır. Örnek: kandaki bir hormon, hedef doku üzerinde başka bir bezin hormonuyla birlikte etkili olabilir')
OZM=B('Kanın ozmotik derişimi','hipotalamustaki algılayıcılar kanın ozmotik derişimini izler; derişim değiştiğinde ADH salgısı değişir ve böbrek tüplerinin su geçirgenliği buna göre ayarlanır. Örnek: terleme sonrası kan plazmasından su kaybı olur')
MEL=B('Melatonin','epifiz bezinin salgıladığı melatonin, günlük ritimlerin düzenlenmesine katılır; salgısı gün içinde sabit değildir ve ortamdaki ışıkla ilişkilidir. Örnek: epifiz, beyinde hipofizden ayrı bir yapıdır')
EKS=B('Hormon eksikliği ve fazlalığı','bir hormonun yetersiz ya da aşırı salgılanması, o hormonun hedef dokularındaki etkilerinin azalmasına ya da artmasına yol açar; yaş dönemi de belirtileri değiştirir. Örnek: bir hormonun etkisi çocukluk ve yetişkinlikte farklı belirtiler verebilir')
ESEY=B('Eşey bezleri ve hipofiz','eşey bezlerinin hormonları, hipofizin ön lobundan salgılanan hormonlarla uyarılır; eşey bezi hormonları ise hipotalamus ve hipofizi etkileyerek geri bildirim oluşturur. Örnek: ön hipofiz hormonları yalnız eşey bezlerini değil başka bezleri de uyarır')
GER2=B('Hipofiz ve hedef bez','hipofiz ön lobu bazı bezleri uyaran hormonlar salgılar; hedef bezin hormonu kanda artınca hipotalamus–hipofiz üzerindeki etkisi salgıyı azaltır, azalınca baskı kalkar. Örnek: oda ısıtıcısının termostatı, ortam ısınınca ısıtıcıyı kapatır')
SUD=B('Nefronda su ve glikoz','süzülen suyun büyük bölümü nefron tüplerinden geri emilir; geri emilimin kapsamı hormonlara ve tüp sıvısının ozmotik derişimine bağlıdır. Süzülen glikoz normalde geri emilerek kana döner. Örnek: tüp sıvısındaki çözünmüş madde fazlalığı, suyun tüpte tutulmasına yol açabilir')
GLU=B('Glikoz dengesi','kan glikozu, pankreas hormonlarının zıt etkileri ve geri bildirimle dar sınırlar içinde tutulur; kandaki değişim hormon salgısını, hormon da değişimi etkiler. Örnek: karaciğer glikozu glikojen hâlinde depolar')
DEG=B('Hormonal düzenleme','hormonlar kimyasal habercilerdir; salgıları çoğunlukla bir ölçülen değerdeki değişime bağlıdır ve etkileri bu değeri başlangıç düzeyine döndürür. Örnek: bir hormonun etkisi, kendi salgısını artırıyorsa pozitif geri bildirimden söz edilir')

# ================ 01 · kolay · pankreas şeması · olumsuz
card(1,'Pankreasın endokrin ve ekzokrin bölümleri','Pankreasta kanalı olan salgı yapıları sindirime, kanalsız hücre kümeleri kana hormon verir; yapılar ve salgı yolları şemadan eşleştirilir.','Pankreasın bütün salgısının kana ya da bütününün bağırsağa gittiğini sanmak.','kolay','şekilli',4,'en2-yapi','pankreas şemasında numaralı yapılar')
b=[]
b.append('\\draw[line width=1.2pt,fill=black,fill opacity=.05] plot[smooth cycle] coordinates {(-3.6,.6) (-2,1.5) (0,1.6) (2,1.4) (3.1,.7) (3.2,-.6) (1.5,-1.5) (-1,-1.6) (-3,-1.2)};')
b.append('\\draw[line width=2.2pt] (-3,.2)--(3.1,.2);')
b.append('\\draw[line width=1.2pt,rounded corners=6pt,fill=black,fill opacity=.1] (3.7,-1.6) rectangle (4.7,1.9);')
b.append('\\draw[line width=2.2pt,-{Stealth[length=2.6mm,width=2.2mm]}] (3.1,.2)--(3.95,.2);')
for cx in (-2.4,-.6,1.3):
    b.append(f'\\draw[line width=1pt] ({cx},.2)--({cx},.78);')
    for k in range(6):
        a=math.radians(60*k); b.append(f'\\draw[line width=1pt,fill=black,fill opacity=.2] ({cx+.26*math.cos(a):.3f},{.98+.26*math.sin(a):.3f}) circle (.17);')
b.append('\\draw[line width=1.2pt,fill=black,fill opacity=.3] (-.3,-.55) ellipse (.5 and .3);')
for dx,dy in ((-.45,-.5),(-.25,-.68),(-.05,-.5),(-.35,-.38),(-.15,-.62)): b.append(f'\\fill ({-.3+dx+.3:.2f},{dy:.2f}) circle (.04);')
b.append('\\draw[red!70!black,line width=2.6pt] (-3.1,-1.0)--(2.9,-1.0);')
b.append('\\draw[red!70!black,line width=1.6pt] (-.3,-.85)--(-.3,-1.0);')
b.append(etk(1,2.3,2.4,2.3,2.15,2.3,.27)); b.append(etk(3,-.9,2.4,-.75,2.15,-.62,1.3)); b.append(etk(2,-4.2,-.35,-3.95,-.38,-.82,-.5)); b.append(etk(4,2.7,-2.4,2.5,-2.15,1.9,-1.03))
SK1=tk('\n'.join(b),.85)
o1=[('3 numaralı yapıdaki hücreler sindirim enzimleri içeren salgı üretir.',True,'Doğru bir bilgiyi yanlış sanmış; 3 numaralı hücre grupları sindirim enzimli salgı üretir.'),
    ('1 numaralı yapı, 3 numaralı yapıların salgısını bağırsağa iletir.',True,'Doğru bir bilgiyi yanlış sanmış; 1 numaralı kanal, enzimli salgıyı bağırsağa taşır.'),
    ('2 numaralı yapının salgısı, 4 numaralı yapıya geçerek hedef hücrelere taşınır.',True,'Doğru bir bilgiyi yanlış sanmış; adacıkların hormonları kılcal damarlara geçer ve kanla taşınır.'),
    ('Pankreas, kanallı salgı yapan bölümler ile kanalsız salgı yapan bölümleri birlikte taşır.',True,'Doğru bir bilgiyi yanlış sanmış; pankreas hem kanallı hem kanalsız salgı yapan bölümlere sahiptir.'),
    ('2 numaralı yapıdaki hücrelerin salgıladığı hormonlar, 1 numaralı yapı ile bağırsağa boşaltılır.',False,'')]
w1=tek(o1,False,0)
q('0001',1,[A('Yapıları tanı','Kanalın ucu bağırsağa açılır (1); küçük hücre öbekleri bu kanala bağlanır (3); kanala bağlanmayan, kılcal damarla temas eden küme adacıktır (2); kırmızı yapı kılcal damardır (4).','1: kanal · 2: adacık · 3: kanallı bölüm · 4: kılcal damar'),
   A('Salgı yollarını ayır','Kanalla bağlı bölümlerin salgısı kanaldan bağırsağa, kanalsız bölümün salgısı kılcal damara gider.','3 → 1 → bağırsak · 2 → 4 → kan'),
   A('İfadeleri sına','Enzimli salgı, kanal ve kılcal damara ilişkin dört ifade bu yolları doğru anlatır.','Dört ifade doğru'),
   A('Yanlışı seç','Adacık hormonlarının kanal yoluyla bağırsağa boşaltılması bu yollara aykırıdır.','Yanlış: 2 → 1 → bağırsak')],
 tipId='en2-yapi',z='kolay',alt='Pankreas',kaz='Pankreasın kanallı ve kanalsız salgı yapan bölümlerini şemadan ayırt eder; salgıların izlediği yolları karşılaştırır.',kalip='şekilli',
 metin='Şekilde insan pankreasının yapısı şematik olarak gösterilmiştir. Pankreasın ortasından geçen kanal, sağ taraftaki bağırsak bölümüne açılmaktadır. Yapılar 1, 2, 3 ve 4 ile numaralandırılmıştır.\nBuna göre, numaralı yapılarla ilgili aşağıdakilerden hangisi yanlıştır?',
 sekil=SK1,dogru=w1['dogru'],yan=w1['yan'],sira=w1['sira'],istenen='Yanlış olan ifade.',
 ip=['Her yapının salgısının kanalla mı yoksa doğrudan kılcal damara mı verildiğini şekildeki bağlantılardan izle.'],bilgi=[PAN],
 puf='Önce yapıları şekildeki bağlantılarından tanı, sonra salgı yollarını karşılaştır.')

# ================ 02 · kolay · hormon–reseptör şeması · öncüllü
card(2,'Hormon–reseptör uyumu','Kan, hormonu bütün hücrelere ulaştırır; yanıtı yalnız şekli uyan reseptörü taşıyan hücre verir.','Hormonun yalnız hedef hücreye kanla taşındığını sanmak; reseptörü olmayan hücreye hiç ulaşmadığını düşünmek.','kolay','şekilli',3,'en2-yapi','kandaki hormonlar ve reseptörlü hücreler')
b=[]
b.append('\\draw[line width=1.3pt,rounded corners=10pt,fill=red,fill opacity=.08] (-4.4,3.6) rectangle (4.4,5.0);')
b.append('\\draw[line width=1.3pt,rounded corners=10pt] (-4.4,3.6) rectangle (4.4,5.0);')
def tri(x,y,r=.17): return f'\\draw[line width=1pt,fill=black,fill opacity=.45] ({x-r:.2f},{y-r*.8:.2f})--({x+r:.2f},{y-r*.8:.2f})--({x:.2f},{y+r:.2f})--cycle;'
for x,y in ((-3.6,4.5),(-1.6,4.2),(.5,4.6),(2.6,4.3),(3.7,4.7)): b.append(f'\\draw[line width=1pt,fill=black,fill opacity=.15] ({x},{y}) circle (.15);')
for x,y in ((-2.6,4.7),(-.6,4.4),(1.5,4.3),(-3.0,4.15)): b.append(tri(x,y))
b.append('\\draw[line width=1pt,fill=black,fill opacity=.15] (-3.2,5.75) circle (.15);\\node[anchor=west] at (-2.95,5.75) {X hormonu};')
b.append(tri(.4,5.75)+'\\node[anchor=west] at (.7,5.75) {Y hormonu};')
for x,n in ((-3,'K'),(0,'L'),(3,'M')):
    b.append(f'\\draw[line width=1.3pt,rounded corners=8pt,fill=black,fill opacity=.04] ({x-1.2},0) rectangle ({x+1.2},1.75);')
    b.append(f'\\draw[line width=1.3pt,rounded corners=8pt] ({x-1.2},0) rectangle ({x+1.2},1.75);')
    b.append(f'\\draw[line width=1pt,fill=black,fill opacity=.2] ({x},.85) ellipse (.5 and .3);')
    b.append(f'\\node[font=\\large\\bfseries] at ({x},-.5) {{{n}}};')
    b.append(f'\\draw[line width=.9pt,dashed,-{{Stealth[length=2mm,width=1.7mm]}}] ({x},3.6)--({x},2.25);')
b.append('\\draw[line width=1.5pt] (-3,1.75) circle (.17);')
b.append('\\draw[line width=1.5pt] (0-.17,1.75-.14)--(0+.17,1.75-.14)--(0,1.75+.17)--cycle;')
b.append('\\draw[line width=1.5pt] (3-.16,1.75-.16) rectangle (3+.16,1.75+.16);')
SK2=tk('\n'.join(b),.85)
w2=onc([True,False,True],['X hormonu yalnız şekline uyan reseptörü taşıyan hücrede etki eder','M hücresinin reseptörü ne X ne de Y hormonunun şekline uyar, bu yüzden hiçbirine yanıt vermez','reseptörü bozulan hücre, hormon kanda bulunsa bile yanıt veremez'],2)
q('0002',2,[A('Reseptörleri oku','K hücresinin reseptörü daire, L hücresinin üçgen, M hücresinin kare biçimindedir.','K: daire · L: üçgen · M: kare'),
   A('Hormonları eşleştir','X hormonu daire biçimli, Y hormonu üçgen biçimlidir; kanla üç hücreye de ulaşırlar.','X → K; Y → L; M: uyan hormon yok'),
   A('I. yargıyı değerlendir','X hormonu üç hücreye ulaşır ama yalnız şekli uyan K hücresinde etki oluşturur.','I: doğru'),
   A('II. yargıyı değerlendir','M hücresinin kare reseptörü her iki hormona da uymaz.','II: yanlış'),
   A('III. yargıyı değerlendir','Reseptörü bozulan hücre hormona yanıt veremez.','III: doğru'),
   A('Sonuç','I ve III yargıları doğrudur.','I ve III')],
 tipId='en2-yapi',z='kolay',alt='Hormon ve Hedef Hücre',kaz='Kandaki hormonların bütün hücrelere ulaşmasına karşın yalnız reseptörü uyan hücrede etki oluşturduğunu şekil üzerinde yorumlar.',kalip='şekilli',
 metin='Şekilde, bir kan damarındaki X ve Y hormonları ile bu hormonların ulaşabileceği K, L ve M hücreleri gösterilmiştir. Hücre zarlarındaki içi boş şekiller reseptörleri göstermektedir. Bir hormon, yalnız şekli kendi şekline uyan reseptörü taşıyan hücrede etki oluşturabilir.\nBuna göre,\nI. X hormonu, kan yoluyla K, L ve M hücrelerine ulaşır ancak yalnız K hücresinde etki oluşturur.\nII. M hücresi, X ve Y hormonlarının her ikisine de yanıt verir.\nIII. L hücresinin reseptörleri bozulursa Y hormonu kanda bulunsa bile bu hücrede etki oluşturamaz.\nyargılarından hangileri doğrudur?',
 sekil=SK2,dogru=w2['dogru'],yan=w2['yan'],sira=w2['sira'],istenen='Doğru olan yargılar.',
 ip=['Her hormonun şeklini, hücre zarındaki reseptörlerin şekliyle tek tek karşılaştır.'],bilgi=[REC],
 puf='Önce her hücrenin hangi hormona uyan reseptörü olduğunu belirle, sonra yargıları sına.')

# ================ 03 · orta · böbreküstü kesiti · öncüllü
card(3,'Böbreküstü bezinin bölümleri','Korteks ve medulla farklı hormonlar üretir; salgıyı uyaran etkenler (sinirsel ya da hormonal) bölüme göre değişir.','İki bölümün aynı hormonu ürettiğini ya da yalnız sinir uyarısıyla çalıştığını sanmak.','orta','şekilli',4,'en2-yapi','böbreküstü bezinin bölümleri')
b=[]
b.append('\\draw[line width=1.3pt,fill=black,fill opacity=.14] plot[smooth cycle] coordinates {(-1.7,0) (-1.1,1.4) (0,1.8) (1.2,1.3) (1.8,0) (1.0,-1.0) (-.9,-1.0)};')
b.append('\\draw[line width=1.3pt,fill=black,fill opacity=.14] plot[smooth cycle] coordinates {(-.85,.1) (-.5,.8) (0,1.0) (.6,.75) (.9,.1) (.5,-.45) (-.45,-.45)};')
b.append(etk(1,-3.1,1.2,-2.85,1.2,-1.35,.95)); b.append(etk(2,3.1,.6,2.85,.6,.5,.4))
SK3=tk('\n'.join(b),.9)
w3=onc([True,True,False],['1 numaralı bölüm olan korteks, böbrekte iyon ve su dengesini etkileyen hormonlar da üretir','2 numaralı bölüm olan medulla, sinir sisteminden gelen uyarıyla hızla hormon salgılar','2 numaralı bölümün hormonu adrenalin kan glikozunu azaltmaz, artırır'],1)
q('0003',3,[A('Bölümleri tanı','Dıştaki bölüm korteks, içteki bölüm medulladır.','1: korteks · 2: medulla'),
   A('I. yargıyı değerlendir','Korteks, kortizol ve aldosteron gibi hormonlar üretir; aldosteron böbrekte iyon geri emilimini etkiler.','I: doğru'),
   A('II. yargıyı değerlendir','Medullanın hormon salgısı sinir sisteminden gelen uyarıyla başlar.','II: doğru'),
   A('III. yargıyı değerlendir','Medullada salgılanan adrenalin kan glikozunu artırır.','III: yanlış'),
   A('Sonuç','I ve II yargıları doğrudur.','I ve II')],
 tipId='en2-yapi',z='orta',alt='Böbreküstü Bezi',kaz='Böbreküstü bezinin korteks ve medulla bölümlerinin hormonlarını, salgı uyarılarını ve etkilerini birlikte değerlendirir.',kalip='şekilli',
 metin='Şekilde insanda bir böbreküstü bezinin kesiti şematik olarak verilmiştir. Bezin dış ve iç bölümleri 1 ve 2 ile numaralandırılmıştır.\nBuna göre,\nI. 1 numaralı bölüm, böbrekte iyon ve su dengesini etkileyen hormonlar da üretir.\nII. 2 numaralı bölümün hormon salgısı, sinir sisteminden gelen uyarıyla hızla artar.\nIII. 2 numaralı bölümde salgılanan hormon, kan glikoz düzeyini azaltır.\nyargılarından hangileri doğrudur?',
 sekil=SK3,dogru=w3['dogru'],yan=w3['yan'],sira=w3['sira'],istenen='Doğru olan yargılar.',
 ip=['Bezin dış ve iç bölümlerinin farklı hormonlar ürettiğini, her hormonun kan glikozunu ya da iyon dengesini nasıl etkilediğini ayrı ayrı düşün.'],bilgi=[BOB],
 puf='Önce bölümleri tanı, sonra her bölümün hormonlarını ve etkisini yargılarla eşleştir.')

# ================ 04 · orta · grafik · su yüklemesi
card(4,'ADH, ozmotik derişim ve idrar grafiği','Kan ozmotik derişimi azalınca ADH salgısı azalır, tüp su geçirgenliği düşer ve idrar artar; grafikte değişimlerin sırası okunur.','ADH azalınca su geri emiliminin arttığını sanmak; ADH’nin ön hipofizde salgılandığını düşünmek.','orta','grafik',4,'en2-su','ozmotik derişim–ADH–idrar grafiği')
t1=1.5
OZ=ck([(0,6),(t1,6),(2.3,4.4),(6.5,6),(8,6)]); AD=ck([(0,6),(t1,6),(3.0,2.2),(6.0,6),(8,6)]); ID=ck([(0,2),(2.2,2),(4.0,7),(7.2,2),(8,2)])
assert argmin(OZ)<argmin(AD)<argmax(ID) and abs(OZ[0][1]-OZ[-1][1])<1e-9
SK4=pg(f'width=7cm,height=5.2cm,{AXO},xmin=0,xmax=8,ymin=0,ymax=8.5,xtick={{0,{t1}}},xticklabels={{0,$t_1$}},ytick=\\empty,xlabel={{Zaman}},ylabel={{Göreli değer}},legend style={{font=\\small,at={{(1.02,0.5)}},anchor=west,draw=none}}',
 f'\\addplot[thick,smooth,no marks] coordinates {{{co(OZ)}}};\\addlegendentry{{Kan ozmotik derişimi}}\n\\addplot[thick,dashed,smooth,no marks] coordinates {{{co(AD)}}};\\addlegendentry{{ADH derişimi}}\n\\addplot[very thick,dotted,smooth,no marks] coordinates {{{co(ID)}}};\\addlegendentry{{İdrar miktarı}}\n\\draw[gray,dotted] (axis cs:{t1},0) -- (axis cs:{t1},8.2);')
o4=[('İdrar miktarı artarken ADH etkisiyle böbrek tüplerinin su geçirgenliği artmıştır.',False,'ADH derişimi azaldığında tüplerin su geçirgenliği de azalır; idrar miktarının artması bu yüzdendir, geçirgenlik artmamıştır.'),
    ('ADH derişimi ile idrar miktarı aynı yönde değişmiştir.',False,'ADH derişimi azalırken idrar miktarı artmıştır; iki değer zıt yönde değişir, aynı yönde değişmemiştir.'),
    ('Kan ozmotik derişimindeki azalma, ADH salgısını artırmıştır.',False,'Kan ozmotik derişimi azaldığında ADH salgısı azalır; grafikte de ADH derişimi düşmüştür.'),
    ('t₁ anından sonra kan ozmotik derişiminin azalması ADH salgısını azaltmış, bu durum idrar miktarının artmasına yol açmıştır.',True,''),
    ('ADH, hipofizin ön lobunda üretilerek kana verilmiştir.',False,'ADH hipotalamusta üretilir ve hipofizin arka lobundan kana verilir; ön lobdan salgılanmaz.')]
w4=tek(o4,True,3)
q('0004',4,[A('Değişimleri sırala','t₁ sonrası önce kan ozmotik derişimi, sonra ADH derişimi azalmış; idrar miktarı bunlardan sonra artmıştır.','ozmotik derişim ↓ → ADH ↓ → idrar ↑'),
   A('ADH’nin etkisini hatırla','ADH, nefron tüplerinin su geçirgenliğini artırır ve su geri emilimini artırır.','ADH ↓ → geri emilim ↓'),
   A('İfadeleri sına','İki değerin zıt yönde değiştiği, ADH’nin hipotalamusta üretildiği ve geçirgenliğin azaldığı bilgileriyle diğer ifadeler elenir.','Dört ifade yanlış'),
   A('Sonucu yaz','Zinciri doğru sıralayan ifade geriye kalır.','Cevap: ozmotik derişim ↓ → ADH ↓ → idrar ↑')],
 tipId='en2-su',z='orta',alt='Su Dengesinin Hormonal Düzenlenmesi',kaz='Kan ozmotik derişimi, ADH derişimi ve idrar miktarının zamanla değişimini grafikten okuyarak neden–sonuç zincirini kurar.',kalip='grafik',
 metin='Sağlıklı bir birey, bir süre su içmeden bekledikten sonra t₁ anında kısa sürede çok miktarda su içiyor. Bireyin kan ozmotik derişimi, kandaki ADH derişimi ve idrar miktarının zamanla değişimi grafikte gösterilmiştir.\nBuna göre, grafikle ilgili aşağıdakilerden hangisi söylenebilir?',
 sekil=SK4,dogru=w4['dogru'],yan=w4['yan'],sira=w4['sira'],istenen='Grafikten söylenebilecek ifade.',
 ip=['Üç eğrinin hangisinin önce, hangisinin sonra değiştiğine bak; sonra ADH’nin nefronda ne yaptığını düşün.'],bilgi=[OZM],
 puf='Değişimlerin sırasını yaz; her değişimi bir öncekinin sonucu olarak yorumla.')

# ================ 05 · orta · tablo · hormon bozuklukları · olumsuz
card(5,'Çocukluk çağında hormon bozuklukları','Boy, zihinsel gelişim, metabolizma ve kan glikozu birlikte okunarak olası hormon bozukluğu belirlenir.','Boy kısalığının her zaman aynı hormonun eksikliğine bağlı olduğunu düşünmek; fazla hormonun etkisini eksiklikle karıştırmak.','orta','tablo',4,'en2-bozuk','tabloda belirtilerden hormon bozukluğunu belirleme')
SK5=tablo_svg(['Birey','Boy (cm)','Zihinsel gelişim','Metabolizma hızı','Açlık glikozu'],[['K','118','Normal','Normal','Normal'],['L','116','Geri','Düşük','Normal'],['M','178','Normal','Normal','Normal'],['N','150','Normal','Normal','Yüksek']])
o5=[('K bireyindeki boy kısalığı, ön hipofizden salgılanan bir hormonun yetersizliğiyle açıklanabilir.',True,'Doğru bir bilgiyi yanlış sanmış; zihinsel gelişimi ve metabolizması normal olan kısa boylu bireyde büyüme hormonu yetersizliği düşünülür.'),
    ('L bireyindeki bulgular, tiroit hormonu yetersizliğiyle açıklanabilir.',True,'Doğru bir bilgiyi yanlış sanmış; çocuklukta tiroksin eksikliği boy kısalığı, zihinsel gelişim geriliği ve düşük metabolizma hızına yol açabilir.'),
    ('M bireyinin boyunun uzunluğu, büyüme hormonunun fazla salgılanmasıyla açıklanabilir.',True,'Doğru bir bilgiyi yanlış sanmış; büyüme çağında büyüme hormonu fazlalığı aşırı boy uzamasına yol açar.'),
    ('N bireyinin açlık kan glikozunun yüksek olması, insülin etkisindeki yetersizlikle açıklanabilir.',True,'Doğru bir bilgiyi yanlış sanmış; insülin salgısı ya da etkisi yetersizse kan glikozu yüksek kalır.'),
    ('M bireyinin boyunun uzunluğu, insülin salgısının fazla olmasıyla açıklanır.',False,'')]
w5=tek(o5,False,4)
q('0005',5,[A('Tabloyu oku','K’de yalnız boy kısadır; L’de boy kısa, zihin geri, metabolizma düşüktür; M’nin boyu çok uzundur; N’de yalnız glikoz yüksektir.','Dört birey, dört farklı bulgu'),
   A('Bulguları hormonlarla eşleştir','Büyüme hormonu boyu, tiroksin metabolizmayı ve gelişimi, insülin kan glikozunu etkiler.','Büyüme hormonu · tiroksin · insülin'),
   A('Doğru açıklamaları ele','K, L, M ve N için büyüme hormonu yetersizliği, tiroksin yetersizliği, büyüme hormonu fazlalığı ve insülin yetersizliği açıklamaları bulgularla uyumludur.','Dört ifade doğru'),
   A('Yanlışı seç','Boy uzunluğunu insülin fazlalığına bağlayan ifade yanlıştır; insülin boyu değil kan glikozunu düzenler.','Yanlış: M → insülin fazlalığı')],
 tipId='en2-bozuk',z='orta',alt='Hormon Bozuklukları',kaz='Tabloda verilen belirtilerden büyüme hormonu, tiroksin ve insülin bozukluklarını ayırt eder.',kalip='tablo',
 metin='Tabloda, 12 yaşındaki dört çocuğun (K, L, M ve N) boy uzunluğu, zihinsel gelişim düzeyi, bazal metabolizma hızı ve açlık kan glikozu durumu verilmiştir. Çocukların hiçbirinde başka bir hastalık yoktur.\nBuna göre, aşağıdakilerden hangisi yanlıştır?',
 sekil=SK5,dogru=w5['dogru'],yan=w5['yan'],sira=w5['sira'],istenen='Yanlış olan ifade.',
 ip=['Her çocuğun tek farklı bulgusuna (ya da bulgu grubuna) bak ve bu bulguyu hangi hormonun düzenlediğini düşün.'],bilgi=[EKS],
 puf='Her bireyi tablodaki bulgularıyla ilgili hormona bağla, sonra ifadeleri tek tek sına.')

# ================ 06 · orta · grafik · melatonin · olumsuz
card(6,'Melatonin ve ışık','Melatonin salgısı gün içinde değişir; karanlıkta artar, ışıkta baskılanır; ışık baskısı geri dönüşlü olabilir, bir grafikten kalıcı kayıp çıkarılamaz.','Melatoninin ışıkla birlikte arttığını sanmak; gecedeki düşük salgıyı bezin tamamen bozulmasına bağlamak.','orta','grafik',4,'en2-ritim','melatonin–saat grafiği')
KM=ck([(0,8),(3,9),(6,6),(7.5,1.5),(18,1.5),(21,5),(24,8)]); LM=ck([(0,2.2),(6,2.0),(8,1.5),(18,1.5),(21,2.0),(24,2.2)])
def ort(pts,a,b): v=[y for x,y in pts if a<=x<=b]; return sum(v)/len(v)
assert ort(KM,0,5)>3*ort(KM,9,17) and abs(ort(KM,9,17)-ort(LM,9,17))<.1 and ort(LM,0,5)<2.5
SK6=pg(f'width=7cm,height=5cm,{AXO},xmin=0,xmax=24,ymin=0,ymax=10.5,xtick={{0,6,12,18,24}},ytick=\\empty,xlabel={{Günün saati}},ylabel={{Melatonin derişimi}},legend style={{font=\\small,at={{(0.5,1.04)}},anchor=south,legend columns=-1,draw=none}}',
 f'\\addplot[thick,smooth,no marks] coordinates {{{co(KM)}}};\\addlegendentry{{K}}\n\\addplot[thick,dashed,smooth,no marks] coordinates {{{co(LM)}}};\\addlegendentry{{L}}')
o6=[('Melatonin salgısı, ortamdaki ışık şiddeti arttıkça artar.',False,'')]
o6=[('L bireyinin gece saatlerinde melatonin derişiminin düşük kalması, bu bireyin epifiz bezinin hormon üretme yeteneğini kalıcı olarak yitirdiğini gösterir.',False,''),
    ('K bireyinde melatonin derişimi, gece saatlerinde gündüz saatlerine göre yüksektir.',True,'K bireyinin grafiğinde 0–5 saat arası derişim, 9–17 saat arasındakinden çok yüksektir; ifade grafikle uyumludur.'),
    ('Gündüz saatlerinde iki bireyin melatonin derişimleri birbirine yakındır.',True,'9–17 saat arasında K ve L eğrileri neredeyse üst üste gelir; ifade grafikle uyumludur.'),
    ('L bireyinin gece boyunca aydınlık ortamda kalması, melatonin salgısını baskılamış olabilir.',True,'Gece aydınlıkta kalan bireyde melatoninin düşük kalması, ışığın salgıyı baskılayabildiğini gösterir ve ifade makuldür.'),
    ('Melatonin, epifiz bezi tarafından salgılanır ve günlük biyolojik ritmin düzenlenmesine katılır.',True,'Melatonin epifiz bezinden salgılanan, biyolojik saatin düzenlenmesinde rol oynayan hormondur; ifade doğrudur.')]
w6=tek(o6,False,0)
q('0006',6,[A('K eğrisini oku','K bireyinde derişim gece saatlerinde yüksek, gündüz saatlerinde düşüktür.','K: gece ↑ · gündüz ↓'),
   A('L eğrisini oku','L bireyinde derişim gece boyunca düşük kalır; gündüz değeri K ile aynıdır.','L: gece ↓ · gündüz = K'),
   A('Doğru ifadeleri ayır','Dört ifade grafik ve melatonin bilgisiyle uyumludur.','Dört ifade doğru'),
   A('Yanlışı seç','Işıkla baskılanma geri dönüşlü olabilir; grafikteki gece değerinden bezin kalıcı olarak bozulduğu çıkarılamaz.','Yanlış: kalıcı yitirme çıkarımı')],
 tipId='en2-ritim',z='orta',alt='Epifiz Bezi ve Melatonin',kaz='Melatonin derişiminin gün içindeki değişimini ve ışığın etkisini grafikten yorumlar.',kalip='grafik',
 metin='K ve L bireyleri gündüz çalışıp gece uyuyan sağlıklı kişilerdir. K bireyi geceyi normal karanlıkta geçirirken L bireyi geceyi, ışığı sürekli açık bir odada geçirmiştir. Bu bireylerin kanındaki melatonin derişiminin gün içindeki değişimi grafikte verilmiştir.\nBuna göre, aşağıdakilerden hangisi söylenemez?',
 sekil=SK6,dogru=w6['dogru'],yan=w6['yan'],sira=w6['sira'],istenen='Söylenemeyecek ifade.',
 ip=['İki bireyin eğrilerini gündüz ve gece saatlerinde ayrı ayrı karşılaştır.'],bilgi=[MEL],
 puf='Her ifadenin grafikten mi yoksa grafiğin söyleyemediği bir varsayımdan mı çıktığını ayır.')

# ================ 07 · orta · metin · eşey bezi · öncüllü
card(7,'Eşey bezi çıkarılması ve geri bildirim','Eşey bezi çıkarılınca onun hormonu azalır; hipofiz üzerindeki baskı kalktığı için uyarıcı hormonlar artar.','Hipofizin de çalışmasının durduğunu sanmak.','orta','öncüllü',4,'en2-bozuk','testis çıkarılmasının hormon düzeylerine etkisi')
w7=onc([True,True,False],['testis çıkarılınca testosteronun hipofiz üzerindeki baskısı kalkar ve LH salgısı artar','testosteronu üreten testisler çıkarıldığı için kandaki testosteron düzeyi düşer','hipofiz sağlamdır ve çalışmayı sürdürür; baskı kalkınca LH ve FSH salgısı artar, durmaz'],1)
q('0007',7,[A('Durumu özetle','Testisler çıkarıldı; hipotalamus ve hipofiz sağlam.','Testosteron kaynağı yok'),
   A('I. yargıyı değerlendir','Testosteron azalınca hipofiz üzerindeki geri bildirim baskısı kalkar; LH artar.','I: doğru'),
   A('II. yargıyı değerlendir','Testosteronu testisler üretir; testisler çıkarılınca kandaki düzeyi azalır.','II: doğru'),
   A('III. yargıyı değerlendir','Hipofiz sağlam olduğundan LH ve FSH salgısı sürer, hatta artar.','III: yanlış'),
   A('Sonuç','I ve II yargıları gerçekleşir.','I ve II')],
 tipId='en2-bozuk',z='orta',alt='Eşey Bezi Hormonları',kaz='Eşey bezinin çıkarılmasının testosteron ve hipofiz hormonları üzerindeki etkisini geri bildirimle açıklar.',kalip='öncüllü',
 metin='Kaza nedeniyle iki testisi de çıkarılan yetişkin bir erkekte hipotalamus ve hipofiz sağlamdır ve bu kişiye herhangi bir hormon tedavisi uygulanmamaktadır.\nBu bireyin kanında bir süre sonra yapılacak ölçümlerle ilgili,\nI. LH derişiminin artması\nII. testosteron derişiminin azalması\nIII. hipofizden LH ve FSH salgılanmasının tamamen durması\nolaylarından hangilerinin gerçekleşmesi beklenir?',
 dogru=w7['dogru'],yan=w7['yan'],sira=w7['sira'],istenen='Gerçekleşmesi beklenen olaylar.',
 ip=['Testosteronun ve hipofiz hormonlarının birbirini nasıl etkilediğini, testosteron kaynağı ortadan kalkınca ne olacağıyla ilişkilendir.'],bilgi=[ESEY],
 puf='Önce hangi hormonun kaynağının kalktığını bul, sonra bunun hipofiz üzerindeki baskıyı nasıl değiştirdiğini düşün.')

# ================ 08 · zor · tablo · ACTH–kortizol · öncüllü
card(8,'ACTH–kortizol tablosu','Hipofiz hormonu ve hedef bez hormonunun birlikte okunmasıyla sorunun hipofizde mi hedef bezde mi olduğu çıkarılır; geri bildirim yönü sorgulanır.','Hedef bez hormonu düşükken uyarıcı hormonun da düşük olacağını sanmak.','zor','tablo',5,'en2-geri','ACTH–kortizol tablosundan sorunun yeri')
SK8=tablo_svg(['Birey','ACTH (pg/mL)','Kortizol (µg/dL)'],[['Normal aralık','10 – 60','5 – 25'],['K','150','2'],['L','2','45'],['M','160','48'],['N','3','2']])
w8=onc([True,False,True],['kortizol azalınca hipotalamus–hipofiz üzerindeki baskı kalkar ve ACTH salgısı artar','L bireyinde ACTH düşük olduğundan hipofiz bu yüksek kortizolu uyarmıyor; kortizolü fazla üreten bölüm böbreküstü korteksidir','N bireyinde ACTH düşüklüğü hipofizdeki işlev bozukluğundan kaynaklanır; korteks sağlam olduğundan ACTH verilirse kortizol artar'],2)
q('0008',8,[A('Normal aralıkla karşılaştır','K’de ACTH yüksek, kortizol düşüktür; L’de tersi; M’de ikisi yüksek, N’de ikisi düşüktür.','Dört farklı örüntü'),
   A('I. yargıyı değerlendir','Kortizol azalınca geri bildirim baskısı kalkar; ACTH artar. K bunun örneğidir.','I: doğru'),
   A('II. yargıyı değerlendir','L’de kortizol yüksek ama ACTH düşüktür; bu durumda hipofiz kortizolü artırmıyor, kaynak korteks hücreleridir.','II: yanlış'),
   A('III. yargıyı değerlendir','N’de ACTH düşük olduğu için korteks uyarılmamaktadır; korteks sağlamsa ACTH verilince kortizol artar.','III: doğru'),
   A('Sonuç','I ve III yargıları doğrudur.','I ve III')],
 tipId='en2-geri',z='zor',alt='Hipofiz ve Hedef Bez',kaz='ACTH ve kortizol değerlerini birlikte yorumlayarak sorunun hipofizde ya da böbreküstü korteksinde olduğunu çıkarır.',kalip='tablo',
 metin='Tabloda, bir hastanede değerlendirilen dört kişide (K, L, M ve N) kandaki ACTH ve kortizol derişimleri ile normal aralıklar verilmiştir. ACTH, hipofizin ön lobundan salgılanır ve böbreküstü korteksinden kortizol salgılanmasını uyarır. Kortizol ise hipotalamus ve hipofiz üzerinde geri bildirim oluşturur. N bireyinin böbreküstü korteksi sağlamdır.\nBuna göre,\nI. K bireyinde kortizol düşük olduğu için hipofiz üzerindeki baskı azalmıştır ve ACTH yüksektir.\nII. L bireyindeki bulgular, sorunun hipofizde olduğunu gösterir.\nIII. N bireyine dışarıdan ACTH verilirse kandaki kortizol derişiminin artması beklenir.\nyargılarından hangileri doğrudur?',
 sekil=SK8,dogru=w8['dogru'],yan=w8['yan'],sira=w8['sira'],istenen='Doğru olan yargılar.',
 ip=['Her bireyde iki hormonun yönünü ayrı ayrı yaz; sonra hangisinin diğerini uyardığını ve geri bildirimde hangisinin baskıladığını düşün.'],bilgi=[GER2],
 puf='Önce yönleri (↑ ↓) yaz, sonra ACTH’nin kortizolü uyardığını, kortizolün ise ACTH’yi baskıladığını kullan.')

# ================ 09 · zor · tablo · ADH ve glikoz
card(9,'İdrar miktarı artışının farklı nedenleri','Aynı belirti (çok idrar) farklı nedenlerle ortaya çıkabilir; nedenler ADH düzeyi ve idrar glikozu gibi bulgulardan ayrılır.','Çok idrarın her zaman ADH yetersizliğine bağlı olduğunu sanmak.','zor','tablo',5,'en2-su','tabloda çok idrarın nedenleri')
SK9=tablo_svg(['Birey','ADH düzeyi','İdrar (L/gün)','İdrarda glikoz','Kan glikozu (mg/100 mL)'],[['K','Normal','1,5','Yok','90'],['L','Çok düşük','14','Yok','90'],['M','Normal','6','Var','340']])
C9={'adh':'ADH yetersizliği nedeniyle nefron tüplerinde su geri emiliminin azalması','adhf':'ADH fazlalığı nedeniyle nefron tüplerinde su geri emiliminin azalması','glk':'süzülen glikozun tamamının geri emilememesi nedeniyle tüp sıvısının ozmotik derişiminin artması ve suyun tüpte kalması','sz':'glikozun hiç süzülmemesi nedeniyle suyun idrara geçmesi'}
def op9(l,m): return f'L bireyinde {C9[l]}, M bireyinde {C9[m]} etkili olabilir.'
o9=[(op9('adh','adh'),False,'M bireyinin ADH düzeyi normaldir ve idrarında glikoz vardır; çok idrar ADH yetersizliğiyle açıklanamaz, glikozun geri emilememesiyle açıklanır.'),
    (op9('adhf','glk'),False,'L bireyinde ADH düzeyi çok düşüktür, fazla değildir; ADH fazlalığı su geri emilimini artırır ve idrarı azaltırdı.'),
    (op9('adh','sz'),False,'Glikoz süzülür; M bireyinin idrarında glikoz bulunması glikozun süzülmediğini değil, geri emilemediğini gösterir.'),
    (op9('adh','glk'),True,''),
    (op9('glk','adh'),False,'Nedenler birbirine karıştırılmış; L bireyinde glikoz yoktur ve ADH çok düşüktür, M bireyinde ise ADH normal, idrarda glikoz vardır.')]
w9=tek(o9,True,3)
q('0009',9,[A('Tabloyu oku','L: ADH çok düşük, idrar çok, glikoz yok. M: ADH normal, idrar çok, idrarda glikoz var, kan glikozu yüksek.','İki bireyde de idrar fazla ama bulgular farklı'),
   A('L’yi yorumla','ADH azalınca nefron tüplerinin su geçirgenliği azalır; su geri emilmez ve idrar artar.','L: ADH ↓ → su geri emilimi ↓'),
   A('M’yi yorumla','Kan glikozu yüksektir; süzülen glikozun tamamı geri emilemez, idrarda kalan glikoz tüp sıvısının ozmotik derişimini artırır ve suyu tüpte tutar.','M: glikoz geri emilemez → su idrarda kalır'),
   A('Seçeneği bul','Bu iki nedeni birlikte doğru veren seçenek cevaptır.','Cevap: ADH yetersizliği ve glikoz geri emilememesi')],
 tipId='en2-su',z='zor',alt='ADH ve Kan Glikozu',kaz='İdrar miktarı artışının ADH yetersizliği ve idrarda glikoz bulunması gibi farklı nedenlerini tablodaki verilerle ayırt eder.',kalip='tablo',
 metin='Tabloda, sağlıklı K bireyi ile hastalık bulguları olan L ve M bireylerinin kanındaki ADH düzeyi, günlük idrar miktarı, idrardaki glikoz durumu ve açlık kan glikozu değerleri verilmiştir.\nBuna göre, L ve M bireylerinde idrar miktarının fazla olmasının nedenleri aşağıdakilerin hangisinde doğru verilmiştir?',
 sekil=SK9,dogru=w9['dogru'],yan=w9['yan'],sira=w9['sira'],istenen='L ve M bireylerinde idrarın fazla olmasının nedenleri.',
 ip=['Tabloda iki bireyin hangi sütunda farklılaştığını bul; her fark, idrarın fazla olmasını başka bir yolla açıklar.'],bilgi=[SUD],
 puf='Her birey için ayrı ayrı “bu bulgu su geri emilimini nasıl değiştirir?” diye sor.')

# ================ 10 · zor · grafik · glukagon
card(10,'Düşen glikoz ve glukagon geri bildirimi','Kan glikozu düşünce glukagon salgısı artar, karaciğerden glikoz salınımıyla düşüş sınırlanır; olayların sırası grafikten okunur.','Glikozu düşüren etkiyi glukagona bağlamak; değişimlerin sırasını gözden kaçırmak.','zor','grafik',5,'en2-glikoz','glikoz–glukagon grafiği')
t1,t2,t3=1.5,3.2,7.0
GL=ck([(0,90),(t1,90),(t2,55),(4.5,62),(t3,90),(9,90)]); GG=ck([(0,2),(3.0,2),(4.6,7),(6.2,4.8),(8.0,2),(9,2)])
fall=min(x for x,y in GL if y<89.5); rise=min(x for x,y in GG if y>2.05)
assert rise-fall>1.2 and abs(argmin(GL)-t2)<.05 and GL[-1][1]==90 and argmax(GG)>t2
SK10=pg(f'width=7.2cm,height=5.4cm,{AXO},xmin=0,xmax=9,ymin=0,ymax=105,xtick={{0,{t1},{t2},{t3}}},xticklabels={{0,$t_1$,$t_2$,$t_3$}},ytick={{55,90}},ylabel={{Kan glikozu (mg/100 mL)}},xlabel={{Zaman}},legend style={{font=\\small,at={{(0.5,1.04)}},anchor=south,legend columns=-1,draw=none}}',
 f'\\addplot[thick,smooth,no marks] coordinates {{{co(GL)}}};\\addlegendentry{{Kan glikozu}}\n\\addplot[thick,dashed,smooth,no marks] coordinates {{{co([(x,y*10) for x,y in GG])}}};\\addlegendentry{{Glukagon (göreli)}}')
o10=[('t₁ anından sonra kan glikozunun azalmasında glukagon derişimindeki artış etkili olmuştur.',False,'Glukagon kan glikozunu artırır; t₁ sonrasındaki düşüş dışarıdan verilen insülinin etkisidir ve glukagon artışı bu düşüşten sonra başlamıştır.'),
     ('Glukagon derişimindeki artış, kan glikozundaki azalmadan önce başlamıştır.',False,'Grafikte önce kan glikozu azalmaya başlamış, glukagon derişimi daha sonra artmıştır; sıra ifadedeki gibi değildir.'),
     ('t₂ anından sonra kan glikozunun artmasında karaciğerde glikojen sentezinin hızlanması etkili olmuştur.',False,'Karaciğerde glikojen sentezi glikozu depolar ve kan glikozunu azaltır; t₂ sonrası artış glukagonun glikojen yıkımını artırmasıyla açıklanır.'),
     ('Glukagon derişimindeki artış, dışarıdan verilen insülinin pankreasın glukagon salgılayan hücrelerini doğrudan uyarmasının sonucudur.',False,'Glukagon artışı insülinin etkisiyle değil, insülinin neden olduğu kan glikozu düşüşüyle ilişkilidir; insülin glukagon salgısını uyarmaz.'),
     ('Kan glikozunun azalması glukagon salgısını artırmış, glukagon da glikozu yükselterek düşüşü sınırlamıştır; bu bir negatif geri bildirimdir.',True,'')]
w10=tek(o10,True,4)
q('0010',10,[A('Olayları sırala','t₁’de insülin verilir; glikoz düşmeye başlar; ardından glukagon artar; glikoz t₂’den sonra yükselir.','insülin → glikoz ↓ → glukagon ↑ → glikoz ↑'),
   A('Düşüşün nedenini belirle','Glikozu düşüren, dışarıdan verilen insülindir; glukagon glikozu artırır.','Düşüş: insülin'),
   A('Artışın nedenini belirle','Glukagon, karaciğerde glikojen yıkımını artırarak glikoz salınımını sağlar ve düşüşü sınırlar.','Artış: glukagon'),
   A('Geri bildirimi adlandır','Değişim (glikoz düşüşü) bir hormonun salgısını artırıyor ve bu hormon değişimi geri çeviriyorsa negatif geri bildirimdir.','Negatif geri bildirim'),
   A('İfadeleri ele','Sıra, hormon etkisi ve geri bildirim türü yönünden doğru olan ifade kalır.','Cevap: glikoz ↓ → glukagon ↑ → glikoz ↑')],
 tipId='en2-glikoz',z='zor',alt='Kan Glikozunun Düzenlenmesi',kaz='Dışarıdan verilen insülin sonrası kan glikozu ve glukagon derişiminin değişimini grafikten okuyarak hormonların etkisini ve geri bildirimi yorumlar.',kalip='grafik',
 metin='Açlık kan glikozu normal olan sağlıklı bir bireye t₁ anında damar yoluyla insülin enjekte ediliyor. Bireyin kan glikoz düzeyi ile kandaki glukagon derişiminin zamanla değişimi grafikte verilmiştir.\nBuna göre, grafikle ilgili aşağıdakilerden hangisi söylenebilir?',
 sekil=SK10,dogru=w10['dogru'],yan=w10['yan'],sira=w10['sira'],istenen='Grafikten söylenebilecek ifade.',
 ip=['Hangi değişimin hangisinden önce başladığını belirle; sonra her hormonun glikoz üzerindeki yönünü düşün.'],bilgi=[GLU],
 puf='Önce olayları zaman sırasına diz, sonra her değişimin nedenini bir önceki olayda ara.')

# ---------------- yaz
for qq in P.ANA: qq['kardes']=None
SC='/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/endokriniki'; os.makedirs(SC,exist_ok=True)
P.yaz(os.path.join(GD,'endokriniki-1.json'),os.path.join(SC,'bos-endokriniki.json'))
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=KONU_K))['kartlar'].append(c['id'])
json.dump(dict(konu='Endokrin Sistem',surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2018–2026 Biyoloji (yalnız mantık), MEB 12. sınıf biyoloji.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','abendokriniki.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
