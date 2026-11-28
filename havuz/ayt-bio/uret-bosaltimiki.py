"""AYT Biyoloji · Boşaltım Sistemi · 2. dalga · 10 soru (kardeş yok, ipucu 1). Şekiller TikZ/pgfplots ve tablo_svg; sayılar Python'da hesaplanır ve assert edilir."""
import sys,os,json,math
from collections import Counter
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,os.path.join(HV,'tyt-bio')); sys.path.insert(0,HV)
import _hafif_bio as H
from _hafif_bio import *
KONUAD='Boşaltım Sistemi'; KK='abio|Boşaltım Sistemi'
H.KONU=KONUAD
P=Parti('bosaltimiki',KONUAD,KK,ders='AYT Biyoloji',idon='aytbio')
KY='ÖSYM AYT 2018–2026 Biyoloji (yalnız mantık) · MEB 11. sınıf Boşaltım Sistemi'
SCR='/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad'
def q(n,tipId,tip,z,alt,kaz,kalip,ozet,ne,fikir,tuzak,ad,**k):
    assert len(k['ip'])==1 and 3<=len(ad)<=7
    kid=f'K-ABBOS2-{n:02d}'
    kart(kid,alt,fikir,tuzak,z,kalip,len(ad),tipId,tip,KY)
    mk(P,f'{n:04d}',ad=ad,adim=len(ad),tipId=tipId,tip=tip,z=z,alt=alt,kaz=kaz,kalip=kalip,kart=f'{kid} ({ozet}) · {ne}',**k)
def qo(n,r,tipId,tip,z,alt,kaz,ozet,ne,fikir,tuzak,**k):
    q(n,tipId,tip,z,alt,kaz,'öncüllü',ozet,ne,fikir,tuzak,r['adim'],dogru=r['dogru'],yan=r['yan'],sira=r['sira'],**k)
def yer(harf,dogru,yanlar):
    sira=[None]*5; sira['ABCDE'.index(harf)]=dogru; it=iter(yanlar)
    for i in range(5):
        if sira[i] is None: sira[i]=next(it)
    assert sorted(sira)==sorted([dogru]+list(yanlar)); return sira
ORD=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
SETS=[{'I'},{'II'},{'III'},{'I','II'},{'I','III'},{'II','III'},{'I','II','III'}]
def onc(d,harf,mod='dogru'):
    T={k for k,v in d.items() if v[0]==(mod=='dogru')}; assert T in SETS,T
    p=SETS.index(T); h='ABCDE'.index(harf)
    assert max(0,p-2)<=h<=min(4,p),('harf uygun değil',T,p,h)
    ad='doğru' if mod=='dogru' else 'yanlış'
    mes=lambda i:len(SETS[i]^T)
    once=sorted([i for i in range(7) if i<p],key=lambda i:(mes(i),-i))[:h]
    sonra=sorted([i for i in range(7) if i>p],key=lambda i:(mes(i),i))[:4-h]
    ops=sorted(once+[p]+sonra); assert ops.index(p)==h and len(ops)==5
    yan=[]
    for i in ops:
        if i==p: continue
        S=SETS[i]; parca=[]
        for k in sorted(S-T,key=['I','II','III'].index): parca.append(f'{k}. öncülünü {ad} saymış. Doğrusu: {d[k][1]}')
        for k in sorted(T-S,key=['I','II','III'].index): parca.append(f'{k}. öncülünü {ad} saymamış. Doğrusu: {d[k][1]}')
        yan.append((ORD[i],' '.join(parca),'bilgi'))
    steps=[A(f'{k}. öncülü değerlendir',d[k][1],f'{k}: '+('doğru' if d[k][0] else 'yanlış')) for k in d]
    steps.append(A('Sonucu yaz','İstenen koşulu sağlayan öncüller bir arada yazılır.','Sonuç: '+ORD[p]))
    return dict(dogru=ORD[p],yan=yan,sira=[ORD[i] for i in ops],adim=steps)
def tk(body,scale=1.0): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small,scale=%s]\n%s\n\\end{tikzpicture}'%(scale,body))
OKU='-{Stealth[length=2.3mm,width=1.9mm]}'
KAP='red!75'; VEN='blue!70'
def lab(t,x,y,x1,y1,x2,y2):
    return f'\\node[font=\\normalsize\\bfseries] at ({x},{y}) {{{t}}};\\draw[{OKU},line width=.8pt] ({x1},{y1})--({x2},{y2});'
AX='/pgf/number format/1000 sep={},tick label style={font=\\small},label style={font=\\small},axis lines=left,every axis plot/.append style={line width=1.4pt}'
def coords(v,x0=1): return ' '.join(f'({x0+i},{y})' for i,y in enumerate(v))
LEG='legend style={font=\\small,at={(0.5,1.03)},anchor=south,legend columns=-1,draw=none,fill=none}'
# ============ ŞEKİLLER ============
def sekil_yol():
    b=[]
    b.append('\\draw[line width=1.8pt,fill=orange!25] plot[smooth cycle] coordinates {(-2.9,4.6) (-2.3,5.3) (-1.4,5.2) (-1.1,4.6) (-1.45,4.1) (-1.45,3.6) (-1.1,3.0) (-1.8,2.5) (-2.7,2.8) (-3.1,3.7)};')
    b.append(f'\\draw[{KAP},line width=3pt,-{{Stealth[length=2mm,width=2mm]}}] (.5,4.7)--(-1.15,4.1);')
    b.append(f'\\draw[{VEN},line width=3pt] (-1.2,3.5)--(-.5,3.5);')
    b.append(f'\\draw[{KAP},line width=4.5pt] (.5,6.3)--(.5,2.2);\\draw[{VEN},line width=4.5pt] (-.5,2.2)--(-.5,6.3);')
    b.append('\\draw[line width=3pt,yellow!75!orange] (-1.7,2.55) to[out=-90,in=120] (-.35,1.35);')
    b.append('\\draw[line width=1.6pt,fill=yellow!40] (-.5,1.4) to[out=-60,in=60,looseness=.6] (.3,1.4) to[out=-90,in=-90,looseness=1.6] (-.5,1.4);')
    b.append('\\draw[line width=3pt,yellow!75!orange] (-.1,.15)--(-.1,-.9);')
    b.append(lab('I',-4.3,3.5,-3.85,3.5,-1.3,3.5).replace('(-3.85,3.5)--(-1.3,3.5)','(-3.9,3.35)--(-1.0,3.5)'))
    b.append(lab('II',-4.3,5.4,-3.9,5.35,-2.9,5.0))
    b.append(lab('III',-3.4,1.4,-3.0,1.5,-1.9,2.1))
    b.append(lab('IV',1.6,.8,1.2,.8,.4,.9))
    b.append(lab('V',1.2,-.6,.8,-.6,.0,-.6))
    return tk('\n'.join(b),.8)
def sekil_azot():
    b=[]
    bx=lambda x,y,t:f'\\node[draw,rounded corners=3pt,line width=1.4pt,minimum width=2.6cm,minimum height=1cm,font=\\normalsize\\bfseries,fill=black!6] at ({x},{y}) {{{t}}};'
    b+= [bx(0,3,'Amino asit'),bx(5.5,3,'Amonyak'),bx(5.5,0,'Üre (kanda)'),bx(0,0,'İdrar')]
    nm=lambda t,x,y:f'\\node[font=\\large\\bfseries,fill=white,inner sep=2pt] at ({x},{y}) {{{t}}};'
    for x1,y1,x2,y2,t,tx,ty in [(1.4,3,4.1,3,'K',2.75,3.45),(5.5,2.45,5.5,.55,'L',6.0,1.5),(4.1,0,1.4,0,'M',2.75,.45)]:
        b.append(f'\\draw[{OKU},line width=1.6pt] ({x1},{y1})--({x2},{y2});'+nm(t,tx,ty))
    return tk('\n'.join(b),.85)
def sekil_arteriyol():
    b=[]
    b.append('\\draw[line width=1.6pt,fill=black,fill opacity=.06] (0,0) circle (1.2);\\draw[line width=1.6pt] (0,0) circle (1.2);')
    b.append(f'\\draw[{KAP},line width=1.4pt] plot[smooth cycle] coordinates {{(-.6,.4) (-.2,.8) (.4,.6) (.6,.1) (.3,-.4) (-.2,-.7) (-.6,-.3)}};\\draw[{KAP},line width=1.1pt] (-.3,.1) to[bend left=50] (.25,.2);')
    b.append(f'\\draw[{KAP},line width=7pt] (-3.0,.9)--(-.9,.5);')
    b.append(f'\\draw[{KAP},line width=3pt] (-.8,-.45)--(-1.7,-.9)--(-1.7,-3.2)--(3.1,-3.2);')
    b.append(f'\\draw[cyan!70!blue,line width=4pt] (1.2,0)--(2.4,0)--(2.4,-2.4);')
    b.append(f'\\draw[{KAP},line width=1.6pt] plot[smooth] coordinates {{(3.1,-3.2) (3.5,-2.8) (3.0,-2.4) (3.5,-2.0) (3.0,-1.6) (3.5,-1.2) (3.0,-.8)}};')
    b.append(lab('I',-3.4,1.6,-3.1,1.4,-2.5,.95))
    b.append(lab('II',-2.6,-2.0,-2.2,-2.0,-1.8,-2.0))
    b.append(lab('III',0,2.2,0,1.9,0,1.3))
    b.append(lab('IV',4.5,-1.8,4.1,-1.8,3.6,-1.8))
    b.append(lab('V',3.5,.5,3.1,.3,2.5,.0))
    return tk('\n'.join(b),.8)
def sekil_damar():
    b=['\\node[draw,ellipse,line width=1.4pt,fill=red!15,minimum width=2.2cm,minimum height=1.1cm,font=\\normalsize\\bfseries] at (0,5.4) {Kalp};']
    b.append(f'\\draw[{KAP},line width=4pt,{OKU}] (.5,4.8)--(.5,.8);\\draw[{VEN},line width=4pt,{OKU}] (-.5,.8)--(-.5,4.8);')
    b.append('\\node[draw,rounded corners=4pt,line width=1.4pt,fill=brown!30,minimum width=2.2cm,minimum height=1.2cm,font=\\normalsize\\bfseries] at (-3.3,3.6) {Karaciğer};')
    b.append('\\node[draw,rounded corners=4pt,line width=1.4pt,fill=orange!30,minimum width=2.2cm,minimum height=1.2cm,font=\\normalsize\\bfseries] at (3.3,1.8) {Böbrek};')
    b.append(f'\\draw[{KAP},line width=2.6pt,{OKU}] (.5,3.9)--(-2.2,3.9);\\draw[{VEN},line width=2.6pt,{OKU}] (-2.2,3.3)--(-.5,3.3);')
    b.append(f'\\draw[{KAP},line width=2.6pt,{OKU}] (.5,2.1)--(2.2,2.1);\\draw[{VEN},line width=2.6pt,{OKU}] (2.2,1.5)--(-.5,1.5);')
    nm=lambda t,x,y:f'\\node[font=\\large\\bfseries] at ({x},{y}) {{{t}}};'
    b+= [nm('K',-1.5,4.3),nm('L',-1.5,2.9),nm('M',1.4,2.5),nm('N',1.4,1.1)]
    return tk('\n'.join(b),.8)
# Q4 kontraktil koful grafiği
G4={'K':[20,12,6,0,0],'L':[1,1,0,0,0]}; X4=[0,50,100,150,200]
def sekil_g4():
    b=['\\begin{axis}[width=7.8cm,height=5.6cm,xmin=-10,xmax=210,ymin=0,ymax=24,xtick={0,50,100,150,200},ytick={0,5,10,15,20},xlabel={Dış ortamın ozmotik derişimi (mosm/L)},ylabel={Atım sayısı (atım/dk)},'+LEG+','+AX+']']
    for k,st,mk_ in [('K','red!75','square*'),('L','blue!70','*')]:
        b.append(f'\\addplot[{st},mark={mk_},mark size=2.3pt] coordinates {{'+' '.join(f'({x},{y})' for x,y in zip(X4,G4[k]))+f'}};\\addlegendentry{{{k}}}')
    b.append('\\end{axis}')
    return tk('\n'.join(b),.95)
# Q8 glikoz grafiği
PLZ=[0,100,200,300,400,500]; TM=200; GFR=100
SUZ=[Fr(c*GFR,100) for c in PLZ]; GER=[min(s,TM) for s in SUZ]; ATL=[s-g for s,g in zip(SUZ,GER)]
assert SUZ==[0,100,200,300,400,500] and GER==[0,100,200,200,200,200] and ATL==[0,0,0,100,200,300]
def sekil_g8():
    b=['\\begin{axis}[width=7.8cm,height=5.8cm,xmin=-15,xmax=515,ymin=0,ymax=540,xtick={0,100,200,300,400,500},ytick={0,100,200,300,400,500},xlabel={Plazma glikoz derişimi (mg/100 mL)},ylabel={Glikoz miktarı (mg/dk)},legend style={font=\\small,at={(0.03,0.97)},anchor=north west,draw=none,fill=white,fill opacity=.8},'+AX+']']
    for k,v,st,mk_,ex in [('Süzülen',SUZ,'red!75','square*','line width=2.4pt'),('Geri emilen',GER,'blue!70','*','dashed'),('İdrarla atılan',ATL,'vurgu!80!black','triangle*','')]:
        b.append(f'\\addplot[{st},mark={mk_},mark size=2.3pt,{ex}] coordinates {{'+' '.join(f'({x},{float(y)})' for x,y in zip(PLZ,v))+f'}};\\addlegendentry{{{k}}}')
    b.append('\\end{axis}')
    return tk('\n'.join(b),.95)
# Q9 hacim grafiği
H9={'K':[100,35,25,12,1],'L':[100,35,25,21,15]}
def sekil_g9():
    b=['\\begin{axis}[width=7.6cm,height=5.6cm,xmin=.6,xmax=5.4,ymin=0,ymax=110,xtick={1,2,3,4,5},xticklabels={I,II,III,IV,V},ytick={0,25,50,75,100},xlabel={Nefron üzerindeki kısım},ylabel={Tüp sıvısı hacmi (birim)},'+LEG+','+AX+']']
    for k,st,mk_ in [('K','red!75','square*'),('L','blue!70','*')]:
        b.append(f'\\addplot[{st},mark={mk_},mark size=2.3pt] coordinates {{'+coords(H9[k])+f'}};\\addlegendentry{{{k}}}')
    b.append('\\end{axis}')
    return tk('\n'.join(b),.95)
# ============ SORULAR ============
T_YAPI=('bo2-yapi','Böbrek ve nefron yapısı'); T_SUREC=('bo2-surec','Nefronda madde geçişi'); T_TABLO=('bo2-tablo','Tablo ve grafik yorumu')
T_AZOT=('bo2-azot','Azotlu atıklar ve organlar'); T_DENGE=('bo2-denge','Su dengesi ve hormonlar'); T_SAGLIK=('bo2-saglik','Böbrek ve karaciğer bozuklukları')
ROMS=['I','II','III','IV','V']
# ---------- 01 · idrar yolları · kolay · olumsuz · A ----------
q(1,*T_YAPI,'kolay','İdrar yolları','İdrar yollarının bölümlerini ve idrarın bulunduğu yapıları şekilden ayırt eder.','şekilli','böbrek, damarlar ve idrar yolları şeması','idrar yolları şeması',
 'idrar böbrekte oluşur; üreterlerle mesaneye iletilir, mesanede depolanır ve üretradan atılır; böbreğe gelip giden damarlarda ise kan bulunur','Kan damarlarını idrar yolu sanmak; böbrekte oluşan idrarın yalnız mesanede bulunduğunu düşünmek.',
 [A('Yapıları tanı','Böbreğe bağlı kırmızı damar atardamar, mavi damar toplardamardır; böbrekten sarı tüp biçimli yapı çıkar, onu kese ve en sonda dar tüp izler.','I: böbrek toplardamarı · II: böbrek · III: üreter · IV: mesane · V: üretra'),
  A('İdrarın yolunu izle','İdrar nefronlarda oluşur, böbrekten üretere, oradan mesaneye ve üretraya geçer.','Böbrek → üreter → mesane → üretra'),
  A('Kan damarını ayır','Böbrek toplardamarı kan taşır; içinden idrar geçmez.','İdrar yok → I')],
 metin='Şekilde insan üriner sisteminin bir böbrek, bu böbreğe bağlanan kan damarları ve idrar yollarını gösteren bölümü verilmiştir. Yapılar I, II, III, IV ve V ile numaralandırılmıştır.\nBuna göre, sağlıklı bir bireyde numaralı yapılardan hangisinin içinde idrar bulunmaz?',
 dogru='I',sira=ROMS,yan=[('II','II numaralı yapı böbrektir; nefron tüplerinde oluşan idrar böbrek havuzcuğunda toplanır, bu yüzden içinde idrar bulunur.','bilgi'),
  ('III','III numaralı yapı üreterdir; idrarı böbrekten mesaneye iletir, bu yüzden içinde idrar bulunur.','bilgi'),
  ('IV','IV numaralı yapı mesanedir; idrar burada geçici olarak depolanır, bu yüzden içinde idrar bulunur.','bilgi'),
  ('V','V numaralı yapı üretradır; idrar mesaneden bu kanalla vücut dışına atılır, bu yüzden içinde idrar bulunur.','bilgi')],
 istenen='İçinde idrar bulunmayan yapının numarası.',ip=['İdrarın oluştuğu yerden vücuttan çıkışına kadar izlediği yolu, şekildeki yapılarla ilişkilendir.'],
 bilgi=[B('İdrar yolları','böbrekte oluşan idrar üreterle mesaneye gelir, mesanede depolanır ve üretra ile dışarı atılır')],
 puf='Önce yapıların kan damarı mı idrar yolu mu olduğunu ayır.',sekil=sekil_yol())
# ---------- 02 · azotlu atık · kolay · B ----------
S2={'ur':'Ürik asit; suda çok az çözünür, zehirliliği düşüktür','am':'Amonyak; suda çok çözünür, zehirliliği yüksektir','u1':'Üre; suda çözünmez, zehirliliği yoktur','u2':'Ürik asit; suda çok çözünür, zehirliliği yüksektir','u3':'Üre; suda çok az çözünür, zehirliliği amonyaktan yüksektir'}
q(2,*T_AZOT,'kolay','Azotlu atıklar','Canlıların yaşam ortamına göre azotlu atık türünü ve atığın özelliklerini ilişkilendirir.','düz','kapalı yumurtada gelişen embriyonun azotlu atığı','kapalı yumurtada azotlu atık',
 'amonyak çok zehirli ve suda çok çözünür olduğundan bol suyla seyreltilerek atılır; üre daha az zehirlidir; ürik asit suda çok az çözünür, en az zehirlidir ve az suyla katı hâlde atılabilir','Üreyi kuşlarda ve sürüngenlerde başlıca atık sanmak; ürik asitin zehirli olduğunu düşünmek.',
 [A('Ortamın koşulunu belirle','Embriyo su geçirmez kabuklu yumurtada gelişir; atık dışarı verilemez, içeride birikir.','Atık yumurtanın içinde depolanır'),
  A('Atık için gerekeni çıkar','Depolanacak atığın embriyoya zarar vermemesi için zehirliliği düşük olmalı, depolanması için suda az çözünmelidir.','Gerekli: az zehirli · az çözünür'),
  A('Atığı seç','Bu iki özelliği birlikte taşıyan azotlu atık ürik asittir.','Cevap: ürik asit · suda çok az çözünür · zehirliliği düşük')],
 metin='Tavuk embriyosu, gelişimi boyunca su geçirmez kabuklu yumurtanın içinde bulunur. Metabolizma sonucu oluşan azotlu atık yumurtanın dışına verilemez ve yumurtanın içinde birikir. Embriyonun zarar görmemesi için bu atığın hem az zehirli olması hem de az yer kaplayacak biçimde depolanabilmesi gerekir.\nBuna göre, tavuk embriyosunda başlıca azotlu atık ve bu atığın özelliği aşağıdakilerden hangisinde doğru verilmiştir?',
 dogru=S2['ur'],sira=yer('B',S2['ur'],[S2['am'],S2['u1'],S2['u2'],S2['u3']]),yan=[(S2['am'],'Amonyak çok zehirlidir ve çok su gerektirir; kapalı yumurtada birikirse embriyoyu zehirler, bu yüzden uygun değildir.','bilgi'),
  (S2['u1'],'Üre suda çözünür ve zehirliliği amonyaktan düşüktür ama sıfır değildir; üre yumurtada kullanılan başlıca atık değildir.','bilgi'),
  (S2['u2'],'Ürik asit suda çok az çözünür ve az zehirlidir; özellikleri ters verilmiştir.','bilgi'),
  (S2['u3'],'Üre suda çözünür ve zehirliliği amonyaktan düşüktür; verilen özellikler üreye uymaz.','bilgi')],
 istenen='Embriyonun başlıca azotlu atığı ve özelliği.',ip=['Kapalı bir ortamda biriken atığın hangi iki özelliği taşıması gerektiğini düşün.'],
 bilgi=[B('Azotlu atıklar','amonyak, üre ve ürik asit proteinlerin yıkımından oluşan azotlu atıklardır; zehirlilikleri ve çözünürlükleri birbirinden farklıdır')],
 puf='Atığın depolanması gerekiyorsa az zehirli ve suda az çözünür olanı ara.')
# ---------- 03 · amino asit → üre · orta · öncüllü · C ----------
d3={'I':(True,'K numaralı olayda amino asitlerden amino grubu ayrılır ve zehirliliği yüksek amonyak oluşur.'),
    'II':(True,'L numaralı olayda amonyak, karaciğer hücrelerinde daha az zehirli olan üreye dönüştürülür.'),
    'III':(False,'Üre böbrekte sentezlenmez; karaciğerde oluşan üre kanla böbreğe taşınır ve süzülerek atılır.')}
r=onc(d3,'C')
qo(3,r,*T_AZOT,'orta','Azotlu atıkların oluşumu','Amino asit yıkımından üre oluşumuna ve atılımına kadar olan basamakları değerlendirir.','amino asit–amonyak–üre dönüşümü şeması','amino asitten üre ve idrara giden yol',
 'amino asitlerden ayrılan amino grubu amonyağa dönüşür; amonyak karaciğerde üreye çevrilir; üre kanla böbreğe taşınır ve idrarla atılır','Üre sentezinin böbrekte olduğunu sanmak; amonyağın üreden az zehirli olduğunu düşünmek.',
 metin='Şekilde bir insanda amino asitlerin yıkımından başlayarak idrarın oluşmasına kadar gerçekleşen olaylar K, L ve M okları ile gösterilmiştir.\nBuna göre,\nI. K numaralı olayda amino asitlerden amino grubu ayrılır ve zehirliliği yüksek amonyak oluşur.\nII. L numaralı olayda amonyak, karaciğer hücrelerinde üreye dönüştürülür.\nIII. Üre, M numaralı olay sırasında böbrek hücrelerinde amonyaktan sentezlenir.\nifadelerinden hangileri doğrudur?',
 istenen='Doğru olan öncüllerin hangileri olduğu.',ip=['Üre oluşumunun ve üreyi atan organın ayrı organlar olduğunu hatırla.'],
 bilgi=[B('Üre oluşumu','amino asitlerin yıkımıyla ortaya çıkan amonyak karaciğerde üreye çevrilir; üre kanla böbreğe taşınarak idrarla atılır')],
 puf='Her ok için olayın gerçekleştiği organı ve ürünün özelliğini ayrı ayrı sına.',sekil=sekil_azot())
# ---------- 04 · kontraktil koful · orta · grafik · D ----------
S4={'a':'K grubunda dış ortamın ozmotik derişimi arttıkça hücreye giren su miktarı artar.','b':'L grubunda atım sayısının çok az olması, hücreye su girişinin durduğunu gösterir.','c':'K grubunda dış ortamın ozmotik derişimi 100 mosm/L iken atım sayısı, 50 mosm/L iken olandan fazladır.','d':'Dış ortamın ozmotik derişimi 0 mosm/L iken L grubu hücrelerinin hacminin, K grubuna göre daha hızlı artması beklenir.','e':'K grubunda 150 mosm/L iken atımın durması, kontraktil kofulun ATP kullanmadığını gösterir.'}
assert G4['K'][2]<G4['K'][1]
q(4,*T_SUREC,'orta','Kontraktil koful','Tek hücrelilerde kontraktil koful işlevini ozmotik derişim ve ATP üretimiyle birlikte yorumlar.','grafik','dış ortam derişimi–atım sayısı grafiği','kontraktil koful atım sayısı grafiği',
 'tatlı su protistlerinde hücre içi derişimi dış ortamdan yüksektir; ozmozla giren fazla suyu kontraktil koful ATP harcayarak dışarı atar, dış ortam derişimi arttıkça giren su azalır','Atım sayısının artmasını su çıkışı ile karıştırmak; ATP olmadığında hücreye su girişinin de durduğunu düşünmek.',
 [A('K grubunu oku','Dış ortam derişimi arttıkça atım sayısı 20, 12, 6 ve 0 olarak azalır.','0: 20 · 50: 12 · 100: 6 · 150: 0'),
  A('L grubunu yorumla','ATP üretimi engellenen hücrelerde kontraktil koful atım yapamaz; su yine hücreye girmeye devam eder.','L: atım ≈ 0 ama su girişi sürer'),
  A('Hacmi karşılaştır','0 mosm/L ortamda su girişi en fazladır; L grubunda bu su dışarı atılamadığı için hücre K grubundan daha hızlı şişer.','Hacim artışı: L > K'),
  A('İfadeyi seç','Bu sonucu veren ifade L grubunda hacmin daha hızlı artmasıdır.','Cevap: L grubunda hacim artışı')],
 metin='Tatlı su ortamında yaşayan paramesyumlarda kontraktil koful, hücreye ozmozla giren fazla suyu dışarı atar. Bir araştırmacı, normal paramesyumları (K) ve ATP üretimi engellenmiş paramesyumları (L), ozmotik derişimleri farklı çözeltilere koyarak dakikadaki kontraktil koful atım sayısını ölçüyor. Hücre içi sıvının ozmotik derişimi yaklaşık 150 mosm/L’dir.\nBuna göre, grafikteki sonuçlarla ilgili aşağıdakilerden hangisi söylenebilir?',
 dogru=S4['d'],sira=yer('D',S4['d'],[S4['a'],S4['b'],S4['c'],S4['e']]),yan=[(S4['a'],'Dış ortamın derişimi arttıkça hücre içi ile dış ortam arasındaki fark azalır, giren su miktarı artmaz azalır; grafikte atım sayısı 20’den 0’a düşmektedir.','bilgi'),
  (S4['b'],'L grubunda ATP olmadığı için kontraktil koful çalışamaz; su girişi ozmozla sürer, atımın azalması su girişinin durduğunu göstermez.','bilgi'),
  (S4['c'],'K grubunda 100 mosm/L iken atım sayısı 6, 50 mosm/L iken 12’dir; yani 100 mosm/L’deki değer daha azdır.','islem'),
  (S4['e'],'150 mosm/L’de dış ortam hücre içiyle aynı derişimdedir; net su girişi olmadığı için atım gerekmez, bu ATP kullanılmadığı anlamına gelmez.','bilgi')],
 istenen='Grafikten söylenebilecek ifade.',ip=['Kontraktil kofulun işlevini ve ATP olmadığında suyun hücreye girmeye devam edip etmeyeceğini düşün.'],
 bilgi=[B('Kontraktil koful','tatlı su protistlerinde hücreye ozmozla giren fazla suyu ATP harcayarak dışarı atan organeldir')],
 puf='Atım sayısı su girişiyle ilişkilidir ama atımın azalması su girişinin azaldığı anlamına gelmeyebilir; ATP etkisini ayrı düşün.',sekil=sekil_g4())
# ---------- 05 · günlük su dengesi · orta · tablo · olumsuz · E ----------
T5={'K':(1500,700,300,1500,100,900),'L':(3000,700,300,700,100,3200)}
for k,v in T5.items(): assert sum(v[:3])==sum(v[3:]),k
assert sum(T5['K'][:3])==2500 and sum(T5['L'][:3])==4000 and T5['K'][5]>T5['K'][1] and T5['L'][3]<T5['K'][3] and T5['K'][2]==T5['L'][2]
SK5=tablo_svg(['Birey','İçilen sıvı','Besin','Metabolizma','İdrar','Dışkı','Deri-akciğer'],[[k,*T5[k]] for k in 'KL'])
S5={'y':'L bireyinde idrar miktarının azalması, kandaki ADH düzeyinin azalmasıyla açıklanır.','a':'Her iki bireyde de günlük su kazancı, günlük su kaybına eşittir.','b':'Metabolizma sonucu oluşan su miktarı iki bireyde de aynıdır.','c':'K bireyinde deri ve akciğerlerden kaybedilen su miktarı, besinlerle alınan su miktarından fazladır.','d':'L bireyinde idrar miktarının K bireyine göre az olması, böbrekte su geri emiliminin arttığını gösterir.'}
q(5,*T_DENGE,'orta','Su dengesi','Günlük su kazancı ve kaybını tablodan hesaplayıp ADH ile ilişkilendirir.','tablo','günlük su kazanç ve kayıp tablosu','günlük su dengesi tablosu',
 'sağlıklı bireyde günlük su kazancı su kaybına eşittir; vücut çok su kaybedince ADH artar, böbrekte su geri emilimi artar ve idrar azalır','ADH düzeyinin su kaybında azaldığını sanmak; metabolik suyu kazanç saymamak.',
 [A('Kazanç ve kaybı topla','Her bireyde ilk üç sütun su kazancını, son üç sütun su kaybını gösterir.','K: 1500 + 700 + 300 = 2500 = 1500 + 100 + 900 · L: 3000 + 700 + 300 = 4000 = 700 + 100 + 3200'),
  A('Doğru ifadeleri ayır','Kazanç–kayıp eşitliği, metabolik su ve K’nin deri-akciğer kaybı tabloyla uyumludur.','Metabolizma: 300 = 300 · K: 900 > 700'),
  A('L bireyini yorumla','Terlemeyle çok su kaybeden L bireyinde plazmanın ozmotik derişimi artar; bu ADH salgısını artırır, su geri emilimi artar ve idrar azalır.','Ter ↑ → ADH ↑ → idrar ↓'),
  A('Yanlışı seç','İdrar azalmasını ADH’nin azalmasına bağlayan ifade yanlıştır.','Cevap: ADH azalması ifadesi')],
 metin='Tabloda, iki sağlıklı bireyin bir günde su kazancı (içilen sıvı, besinlerle alınan su, metabolizmada oluşan su) ile su kaybı (idrar, dışkı, deri ve akciğerler) mililitre cinsinden verilmiştir. K bireyi ılık bir ortamda dinlenmiş, L bireyi sıcak bir ortamda ağır iş yapmıştır.\nBuna göre, aşağıdaki ifadelerden hangisi yanlıştır?',
 dogru=S5['y'],sira=yer('E',S5['y'],[S5['a'],S5['b'],S5['c'],S5['d']]),yan=[(S5['a'],'K’de kazanç da kayıp da 2500 mL, L’de ikisi de 4000 mL’dir; eşitlik vardır ve ifade doğrudur.','islem'),
  (S5['b'],'Metabolizmada oluşan su iki bireyde de 300 mL’dir; ifade doğrudur.','islem'),
  (S5['c'],'K bireyinde deri ve akciğerlerden kayıp 900 mL, besinle alınan su 700 mL’dir; 900 > 700 olduğundan ifade doğrudur.','islem'),
  (S5['d'],'L bireyinin idrarı 700 mL, K bireyinin 1500 mL’dir; idrarın azalması su geri emiliminin arttığını gösterir ve ifade doğrudur.','bilgi')],
 istenen='Yanlış olan ifade.',ip=['Terleyen bireyin kan plazmasındaki değişimin ADH salgısını ve idrar miktarını nasıl etkilediğini düşün.'],
 bilgi=[B('Su dengesi','vücutta günlük su kazancı, su kaybına eşit olduğunda su dengesi korunur; su kaybı arttığında ADH salgısı artar ve idrar azalır')],
 puf='Önce kazanç ve kayıp toplamlarını bul, sonra hormon ve idrar ilişkisini sına.',sekil=SK5)
# ---------- 06 · glomerulus damarları · orta · olumsuz · A ----------
S6={'y':'II numaralı damardaki kanın plazma proteini derişimi ve ozmotik basıncı, I numaralı damardakine göre düşüktür.','a':'II numaralı damarın çapının I numaralı damardan dar olması, glomerulus kılcallarında kan basıncının yüksek kalmasına katkı sağlar.','b':'Glomerulus kılcalları, iki atardamar arasında yer alır.','c':'IV numaralı kılcallarda kan basıncı glomerulus kılcallarındakinden düşüktür; bu durum V numaralı yapıdan kana madde geçişini kolaylaştırır.','d':'III numaralı yapıya geçen sıvıda kan hücreleri ve büyük plazma proteinleri bulunmaz.'}
q(6,*T_YAPI,'orta','Glomerulus','Glomerulus ve nefron kılcallarının damar bağlantılarını, basınç ve ozmotik basınç farklarıyla yorumlar.','şekilli','getirici ve götürücü damar, nefron kılcalları','glomerulusa gelen ve giden damarlar',
 'glomerulus kılcalları getirici ve götürücü iki atardamar arasındadır; götürücü damar dar olduğundan basınç yüksektir; süzülmeyen büyük proteinler kanda kaldığı için götürücü damarda plazma ozmotik basıncı artar','Götürücü damarın toplardamar olduğunu sanmak; süzülmeden sonra kandaki protein derişiminin azaldığını düşünmek.',
 [A('Damarları tanı','I numaralı damar glomerulusa kan getirir, II numaralı damar glomerulustan kan çıkarır; ikisi de atardamardır.','I ve II: atardamar'),
  A('Basıncı yorumla','Götürücü damarın dar olması glomerulusta kan basıncını yüksek tutar; nefron kılcallarında basınç düşüktür.','Glomerulus: basınç yüksek · IV: basınç düşük'),
  A('Süzülmenin etkisini düşün','Sıvı ve küçük moleküller kapsüle geçer, büyük proteinler damarda kalır; bu yüzden II numaralı damarda protein derişimi ve ozmotik basınç I’den yüksektir.','II: protein derişimi ↑'),
  A('Yanlışı seç','Ozmotik basıncın düştüğünü söyleyen ifade yanlıştır.','Cevap: ozmotik basınç düşük ifadesi')],
 metin='Şekilde bir nefronun başlangıç kısmı, bu kısma kan getiren ve kandan çıkaran damarlar ile nefron tüpünü saran kılcal damarlar gösterilmiştir. Damarların çapları şekilde gerçek oranlarına uygun çizilmiştir ve yapılar I, II, III, IV ve V ile numaralandırılmıştır.\nBuna göre, sağlıklı bir bireyde numaralı yapılarla ilgili aşağıdakilerden hangisi yanlıştır?',
 dogru=S6['y'],sira=yer('A',S6['y'],[S6['a'],S6['b'],S6['c'],S6['d']]),yan=[(S6['a'],'Götürücü damarın dar olması glomerulusta basıncı yüksek tutar; ifade doğrudur.','bilgi'),
  (S6['b'],'Glomerulus kılcalları getirici ve götürücü atardamar arasındadır; ifade doğrudur.','bilgi'),
  (S6['c'],'Nefron kılcallarında basınç düşüktür; tüpten geri emilen maddeler kana kolayca geçer ve ifade doğrudur.','bilgi'),
  (S6['d'],'Kan hücreleri ve büyük proteinler süzülemez; Bowman kapsülündeki sıvıda bulunmazlar ve ifade doğrudur.','bilgi')],
 istenen='Yanlış olan ifade.',ip=['Süzülme sırasında kandan hangi maddelerin ayrıldığını, hangilerinin damarda kaldığını düşün.'],
 bilgi=[B('Glomerulus damarları','glomerulus kılcalları getirici ve götürücü atardamar arasında yer alır; süzülme kan basıncıyla gerçekleşir')],
 puf='Damarın atardamar ya da toplardamar olduğu kandaki gaz oranına değil, kalbe göre yönüne bağlıdır; şekilde damarların bağlantısına bak.',sekil=sekil_arteriyol())
# ---------- 07 · karaciğer/böbrek damarları · orta · öncüllü · C ----------
d7={'I':(True,'L numaralı damardaki kanın üre derişimi, K numaralı damardakinden yüksektir; karaciğer amonyağı üreye çevirip kana verir.'),
    'II':(True,'N numaralı damardaki kanın üre derişimi, M numaralı damardakinden düşüktür; böbrek üreyi kandan süzerek uzaklaştırır.'),
    'III':(False,'N numaralı damardaki kanın üre derişimi, K numaralı damardakinden düşüktür; çünkü K ve M aynı kandır ve böbrekten geçen kanın üresi azalır.')}
r=onc(d7,'C')
qo(7,r,*T_AZOT,'orta','Üre ve organlar','Karaciğer ve böbreğe giden ve bu organlardan çıkan damarlardaki üre derişimini karşılaştırır.','kalp, karaciğer ve böbrek damar şeması','karaciğer ve böbrek damarları',
 'karaciğerden çıkan kanda üre derişimi artar, böbrekten çıkan kanda azalır; aynı büyük atardamardan ayrılan dalların kanı özdeştir','Böbreğe giden ve böbrekten çıkan damarlardaki kanı tam tersi sanmak; atardamar kanında üreyi sıfır varsaymak.',
 metin='Şekilde, bir insanda kalpten çıkan atardamardan ayrılarak karaciğere ve böbreğe giden K ve M damarları ile bu organlardan kalbe dönen L ve N damarları gösterilmiştir. K ve M damarları aynı büyük atardamardan ayrılmıştır.\nBuna göre,\nI. L numaralı damardaki kanın üre derişimi, K numaralı damardakinden yüksektir.\nII. N numaralı damardaki kanın üre derişimi, M numaralı damardakinden düşüktür.\nIII. N numaralı damardaki kanın üre derişimi, K numaralı damardakinden yüksektir.\nifadelerinden hangileri doğrudur?',
 istenen='Doğru olan öncüllerin hangileri olduğu.',ip=['Her organdan geçen kanda hangi azotlu atığın oluştuğunu ya da uzaklaştırıldığını düşün.'],
 bilgi=[B('Karaciğer ve böbrek','karaciğer amonyağı üreye çevirir, böbrek ise üreyi kandan süzerek idrarla uzaklaştırır')],
 puf='K ve M aynı kandır; yalnız organdan geçen kandaki değişimi izle.',sekil=sekil_damar())
# ---------- 08 · glikoz eşik · zor · sayısal · B ----------
GFR2=50; PL2=500
S2s=Fr(PL2*GFR2,100); G2=min(S2s,TM); A2=S2s-G2
assert (S2s,G2,A2)==(250,200,50) and Fr(PL2*GFR,100)-min(Fr(PL2*GFR,100),TM)==300
q(8,*T_SUREC,'zor','Glikoz geri emilimi','Glikozun süzülme, geri emilim kapasitesi ve idrarla atılımını grafikten çıkarıp süzülme hızı değişimiyle birleştirir.','grafik','plazma glikozu–glikoz miktarı grafiği','glikoz süzülme ve geri emilim grafiği',
 'süzülen glikoz miktarı plazma derişimi ile süzülme hızının çarpımıdır; geri emilim en çok taşıyıcıların kapasitesi kadardır; kapasiteyi aşan miktar idrarla atılır','Süzülme hızı değişince geri emilim kapasitesinin de değiştiğini sanmak; grafikteki değeri süzülme hızını düşünmeden okumak.',
 [A('Kapasiteyi oku','Grafikte geri emilen glikoz 200 mg/dk’da sabitlenir; bu değer taşıyıcıların en çok geri emebileceği miktardır.','Kapasite: 200 mg/dk'),
  A('Yeni süzülme hızını al','Süzülme hızı 50 mL/dk olduğundan dakikada 50 mL süzüntüde 500 mg/100 mL derişimli glikoz bulunur.','500 × 50 / 100'),
  A('Süzülen miktarı hesapla','Süzülen glikoz miktarı derişim ile süzüntü hacminin çarpımına eşittir.','Süzülen = 250 mg/dk'),
  A('Geri emileni belirle','Süzülen miktar kapasiteyi aştığından geri emilen en çok kapasite kadar olur.','Geri emilen = 200 mg/dk'),
  A('Atılanı bul','İdrarla atılan, süzülenden geri emilenin çıkarılmasıyla bulunur.','250 − 200 = 50 mg/dk')],
 metin='Grafikte, glomerulustan dakikada 100 mL süzüntü geçen sağlıklı bir bireyde plazma glikoz derişimi arttıkça glikozun dakikada süzülen, geri emilen ve idrarla atılan miktarları gösterilmiştir. Glikoz tüplere salgılanmaz. Bu birey bir böbrek hastalığına yakalanıyor; glomerulustan süzülme hızı dakikada 50 mL’ye düşüyor, nefron tüplerinin glikoz geri emme kapasitesi ise değişmiyor.\nBuna göre, plazma glikoz derişimi 500 mg/100 mL olan bu hastada idrarla dakikada atılan glikoz miktarı kaç mg’dır?',
 dogru=int(A2),yan=[(0,'Süzülme hızı düştüğünde süzülen glikozun kapasiteye inip tamamen geri emildiği varsayılırsa 0 bulunur; oysa süzülen 250 mg/dk olup kapasite olan 200 mg/dk’yı aşar.','bilgi'),
  (200,'200 mg/dk geri emilen glikoz miktarıdır; idrarla atılan miktar süzülenden geri emilenin çıkarılmasıyla bulunur ve 250 − 200 = 50’dir.','islem'),
  (250,'250 mg/dk süzülen glikoz miktarıdır; geri emilimin hiç olmadığı varsayılırsa bu değer bulunur, oysa 200 mg/dk geri emilir.','islem'),
  (int(Fr(PL2*GFR,100)-min(Fr(PL2*GFR,100),TM)),'300 mg/dk grafikteki 500 mg/100 mL değeridir; süzülme hızı 100 mL/dk iken geçerlidir ve hastadaki süzülme hızının 50 mL/dk olduğu hesaba katılmamıştır.','islem')],
 istenen='Hastada idrarla dakikada atılan glikoz miktarı (mg).',ip=['Grafikteki değerlerin hangi süzülme hızı için geçerli olduğuna ve değişmeyen niceliğin ne olduğuna dikkat et.'],
 bilgi=[B('Glikozun geri emilimi','süzülen glikoz proksimal tüpte taşıyıcılarla geri emilir; taşıyıcıların kapasitesi aşıldığında fazla glikoz idrarla atılır')],
 puf='Önce yeni süzülen miktarı hesapla, sonra kapasiteyle karşılaştır.',sekil=sekil_g8())
# ---------- 09 · hacim grafiği · zor · grafik · D ----------
G9K=H9['K']; G9L=H9['L']
assert (G9K[2]-G9K[4],G9L[2]-G9L[4])==(24,10) and G9L[2]-G9L[4]<(G9K[2]-G9K[4])/2
assert G9K[0]-G9K[1]==G9L[0]-G9L[1]==65 and G9K[1]-G9K[2]==G9L[1]-G9L[2]==10 and G9L[4]/G9K[4]==15
S9={'d':'L bireyinin nefronunda III ile V arasındaki kısımda geri emilen su miktarı, K bireyinde aynı kısımda geri emilen miktarın yarısından azdır.','a':'Proksimal tüpte geri emilen su miktarı K bireyinde L bireyinden fazladır.','b':'Her iki bireyde de idrar hacmi, süzüntü hacminin %5’inden azdır.','c':'Henle kulpunda geri emilen su miktarı L bireyinde K bireyinden azdır.','e':'L bireyinin idrar hacmi, K bireyinin idrar hacminin 10 katından azdır.'}
q(9,*T_DENGE,'zor','Nefronda su geri emilimi','Nefron kısımlarında tüp sıvısı hacmi değişimini grafikten okuyup ADH’nin etkisiyle birlikte yorumlar.','grafik','nefron kısımlarında tüp sıvısı hacmi grafiği','nefronda tüp sıvısı hacmi grafiği',
 'su geri emilimi proksimal tüpte ve Henle kulpunda ADH’den bağımsız sürer; ADH distal tüpün son kısmı ile toplama kanalında su geri emilimini artırır','ADH’nin her tüp kısmında etkili olduğunu sanmak; hacim farkını geri emilen miktarla karıştırmak.',
 [A('Hacimleri oku','K: 100, 35, 25, 12, 1 · L: 100, 35, 25, 21, 15 birimdir.','I–V okumaları'),
  A('Ortak kısımları ayır','I–III arasında iki bireyin değerleri aynıdır; fark IV ve V’te başlar.','Fark: III sonrası'),
  A('Geri emilimi hesapla','III ile V arasında geri emilen su, III’teki hacim ile V’teki hacmin farkıdır.','K: 25 − 1 = 24 · L: 25 − 15 = 10'),
  A('Karşılaştır','L’de geri emilen 10 birim, K’deki 24 birimin yarısı olan 12 birimden azdır.','10 < 12'),
  A('İfadeyi seç','Bu sonuç III ile V arasındaki geri emilimin yarıdan az olduğunu söyleyen ifadeyle uyumludur.','Cevap: yarısından az')],
 metin='Grafikte, iki bireyin birer nefronunda Bowman kapsülüne giren süzüntü hacmi 100 birim kabul edilerek tüp sıvısı hacminin I, II, III, IV ve V ile gösterilen kısımlardaki değerleri verilmiştir. I Bowman kapsülü, II proksimal tüpün sonu, III Henle kulpunun sonu, IV distal tüpün sonu, V toplama kanalının sonudur. K bireyi sağlıklıdır; L bireyinde ise ADH etkisi görülmemektedir.\nBuna göre, grafikle ilgili aşağıdakilerden hangisi söylenebilir?',
 dogru=S9['d'],sira=yer('D',S9['d'],[S9['a'],S9['b'],S9['c'],S9['e']]),yan=[(S9['a'],'Proksimal tüpte geri emilen su iki bireyde de 100 − 35 = 65 birimdir; fark yoktur ve ifade yanlıştır.','islem'),
  (S9['b'],'K bireyinde idrar hacmi 1 birim olup %1’dir, L bireyinde ise 15 birimdir ve %15’tir; L için %5’ten az değildir.','islem'),
  (S9['c'],'Henle kulpunda geri emilen su iki bireyde de 35 − 25 = 10 birimdir; L bireyinde daha az değildir.','islem'),
  (S9['e'],'L bireyinin idrar hacmi 15, K bireyininki 1 birimdir; oran 15’tir ve 10 katından azdır denemez.','islem')],
 istenen='Grafikten söylenebilecek ifade.',ip=['Geri emilen suyu bulmak için iki kısım arasındaki hacim farkına bak ve ADH’nin hangi kısımlarda etkili olduğunu düşün.'],
 bilgi=[B('ADH ve su','ADH distal tüpün son kısmı ile toplama kanalının su geçirgenliğini artırarak su geri emilimini yükseltir')],
 puf='Bir kısımdaki geri emilim, giriş ve çıkış hacimlerinin farkıdır.',sekil=sekil_g9())
# ---------- 10 · karaciğer yetmezliği · zor · öncüllü · E ----------
d10={'I':(False,'Kandaki amonyağın yüksek olması böbreğin süzme işlevinin bozulduğunu göstermez; amonyak karaciğer işlev göremediği için üreye çevrilemez ve kanda birikir.'),
     'II':(True,'Üre sentezi azaldığından kandaki üre ve süzülen üre azdır; bu nedenle idrarla atılan üre miktarı sağlıklı bireye göre azdır.'),
     'III':(True,'Albümin düşük olunca plazmanın ozmotik basıncı azalır, doku sıvısının kılcal damara geri emilimi zayıflar ve ödem riski artar.')}
r=onc(d10,'E')
qo(10,r,*T_SAGLIK,'zor','Karaciğer yetmezliği','Karaciğer işlevinin bozulmasının üre, amonyak ve plazma proteinleri üzerindeki etkilerini böbrek işleviyle ayırarak değerlendirir.','karaciğer yetmezliği hasta tablosu','karaciğer yetmezliği olan birey',
 'karaciğer işlevi bozulunca amonyak üreye çevrilemez, kanda amonyak artıp üre azalır; plazma proteini sentezi de azaldığından plazma ozmotik basıncı düşer ve ödem görülebilir','Amonyak artışını böbrek hasarına bağlamak; albümin azalmasının ozmotik basıncı artırdığını düşünmek.',
 metin='Karaciğer hücrelerinin büyük bölümü işlev göremeyen bir bireyin kan tahlilinde amonyak düzeyi yüksek, üre düzeyi düşük bulunmuştur. Bu bireyin kan plazmasındaki albümin düzeyi de düşüktür; böbrekleri ise sağlıklıdır.\nBuna göre bu bireyle ilgili,\nI. Kanda amonyağın yüksek olması, böbrekte süzülme işleminin bozulduğunu gösterir.\nII. Günlük idrarla atılan üre miktarı, sağlıklı bir bireye göre azdır.\nIII. Albümin düzeyinin düşük olması, doku sıvısının kılcal damara geri dönüşünü azaltarak ödem riskini artırır.\nifadelerinden hangileri doğrudur?',
 istenen='Doğru olan öncüllerin hangileri olduğu.',ip=['Karaciğerin hangi iki işlevinin bozulduğunu ve sağlam kalan böbreğin neyi süzeceğini düşün.'],
 bilgi=[B('Karaciğerin işlevleri','karaciğer amonyağı üreye çevirir ve albümin gibi plazma proteinlerini sentezler; plazma proteinleri plazmanın ozmotik basıncını oluşturur')],
 puf='Her öncülde sorunun kaynağını karaciğer ya da böbrek olarak ayrı ayrı değerlendir.')
# ============================ YAZ ============================
assert len(P.ANA)==10
Z=Counter(x['zorluk'] for x in P.ANA); assert Z=={'kolay':2,'orta':5,'zor':3},Z
HR=Counter(x['cevap']['sik'] for x in P.ANA); assert all(HR[h]==2 for h in 'ABCDE'),HR
assert 4<=len({x['tipId'] for x in P.ANA})<=6
SEK=sum(1 for x in P.ANA if x['sekil']); assert SEK>=6,SEK
for x in P.ANA: x['kardes']=None
os.makedirs(SCR,exist_ok=True)
P.yaz(os.path.join(GD,'bosaltimiki-1.json'),SCR+'/bos-bosaltimiki.json')
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=KK))['kartlar'].append(c['id'])
json.dump(dict(konu=KONUAD,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2018–2026 Biyoloji (yalnız mantık), MEB 11. sınıf.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','abbosaltimiki.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler),'şekil',SEK)
