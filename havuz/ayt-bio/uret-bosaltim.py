"""AYT Biyoloji · Boşaltım Sistemi · 20 soru (kardeş yok, ipucu 1). Şekiller TikZ (cizim.tikz_svg) ve tablo_svg; derişim/miktar verileri
Python'da hesaplanır, her doğru şık ve çeldirici assert edilir; öncüllerin doğru/yanlış değeri tek yerde (d sözlüğü) tanımlanır."""
import sys,os,json,math
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,os.path.join(HV,'tyt-bio')); sys.path.insert(0,HV)
import _hafif_bio as H
from _hafif_bio import *
KONUAD='Boşaltım Sistemi'; KK='abio|Boşaltım Sistemi'
H.KONU=KONUAD
P=Parti('bosaltim',KONUAD,KK,ders='AYT Biyoloji',idon='aytbio')
KY='ÖSYM AYT 2018–2026 Biyoloji (yalnız mantık) · MEB 11. sınıf Boşaltım Sistemi'
NO={}
def q(n,tipId,tip,z,alt,kaz,kalip,ozet,ne,fikir,tuzak,ad,**k):
    assert len(k['ip'])==1 and 3<=len(ad)<=7
    kid=f'K-ABBOS-{n:02d}'
    kart(kid,alt,fikir,tuzak,z,kalip,len(ad),tipId,tip,KY)
    mk(P,f'{n:04d}',ad=ad,adim=len(ad),tipId=tipId,tip=tip,z=z,alt=alt,kaz=kaz,kalip=kalip,kart=f'{kid} ({ozet}) · {ne}',**k)
def qo(n,r,tipId,tip,z,alt,kaz,ozet,ne,fikir,tuzak,**k):
    q(n,tipId,tip,z,alt,kaz,'öncüllü',ozet,ne,fikir,tuzak,r['adim'],dogru=r['dogru'],yan=r['yan'],sira=r['sira'],**k)
def yer(harf,dogru,yanlar):
    sira=[None]*5; sira['ABCDE'.index(harf)]=dogru; it=iter(yanlar)
    for i in range(5):
        if sira[i] is None: sira[i]=next(it)
    assert sorted(sira)==sorted([dogru]+list(yanlar)); return sira
def tek(harf,dogru,yanlar):
    """yanlar: (şık, çeldirici açıklaması, tür) listesi → mk için dogru, yan, sira"""
    assert len(yanlar)==4 and len(set([dogru]+[y[0] for y in yanlar]))==5
    return dict(dogru=dogru,yan=yanlar,sira=yer(harf,dogru,[y[0] for y in yanlar]))
ORD=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
SETS=[{'I'},{'II'},{'III'},{'I','II'},{'I','III'},{'II','III'},{'I','II','III'}]
def onc(d,harf,mod='dogru',hedef=None):
    """d: {'I':(doğru_mu, kavram açıklaması[, etiket])}. mod='dogru' → doğru öncüller, 'yanlis' → yanlış öncüller istenir.
    Çeldirici açıklamaları ve adımlar d'den üretilir; doğru kümenin şık sırasındaki yeri harfe uygun olmalıdır."""
    T={k for k,v in d.items() if v[0]==(mod=='dogru')}; assert T in SETS,T
    p=SETS.index(T); h='ABCDE'.index(harf)
    assert max(0,p-2)<=h<=min(4,p),('harf uygun değil',T,p,h)
    ad=hedef or ('doğru' if mod=='dogru' else 'yanlış')
    mes=lambda i:len(SETS[i]^T)
    once=sorted([i for i in range(7) if i<p],key=lambda i:(mes(i),-i))[:h]
    sonra=sorted([i for i in range(7) if i>p],key=lambda i:(mes(i),i))[:4-h]
    assert len(once)==h and len(sonra)==4-h
    ops=sorted(once+[p]+sonra); assert ops.index(p)==h
    yan=[]
    for i in ops:
        if i==p: continue
        S=SETS[i]; parca=[]
        for k in sorted(S-T,key=['I','II','III'].index): parca.append(f'{k}. öncülünü {ad} saymış. Doğrusu: {d[k][1]}')
        for k in sorted(T-S,key=['I','II','III'].index): parca.append(f'{k}. öncülünü {ad} saymamış. Doğrusu: {d[k][1]}')
        yan.append((ORD[i],' '.join(parca),'bilgi'))
    steps=[]
    for k in d:
        et=d[k][2] if len(d[k])>2 else ('doğru' if d[k][0] else 'yanlış')
        steps.append(A(f'{k}. öncülü değerlendir',d[k][1],f'{k}: {et}'))
    steps.append(A('Sonucu yaz','İstenen koşulu sağlayan öncüller bir arada yazılır.','Sonuç: '+ORD[p]))
    return dict(dogru=ORD[p],yan=yan,sira=[ORD[i] for i in ops],adim=steps)
# ============================ ŞEKİLLER ============================
def tk(body,scale=1.0): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small,scale=%s]\n%s\n\\end{tikzpicture}'%(scale,body))
OKU='-{Stealth[length=2.3mm,width=1.9mm]}'
TUP='cyan!70!blue'; KAP='red!75'; VEN='blue!70'
def lab(t,x,y,x1,y1,x2,y2):
    return f'\\node[font=\\normalsize\\bfseries] at ({x},{y}) {{{t}}};\\draw[{OKU},line width=.8pt] ({x1},{y1})--({x2},{y2});'
def num(t,x,y): return f'\\node[font=\\normalsize\\bfseries,fill=white,fill opacity=0,text opacity=1] at ({x},{y}) {{{t}}};'
# nefron: kısım noktaları
def nefron(etiket,kapiller=False,oklar=''):
    b=[]
    # Bowman kapsülü ve glomerulus
    b.append('\\draw[line width=1.6pt,fill=black,fill opacity=.06] (0,6) circle (.85);\\draw[line width=1.6pt] (0,6) circle (.85);')
    b.append(f'\\draw[{KAP},line width=1.5pt] plot[smooth cycle] coordinates {{(-.35,6.15) (-.05,6.45) (.3,6.2) (.32,5.85) (0,5.62) (-.3,5.8)}};')
    b.append(f'\\draw[{KAP},line width=1.2pt] (-.1,6.0) to[bend left=40] (.2,6.1);')
    b.append(f'\\draw[{KAP},line width=1.6pt,-{{Stealth[length=2mm,width=1.6mm]}}] (1.5,7.1)--(.2,6.4);')
    b.append(f'\\draw[{KAP},line width=1.6pt] (-.2,6.4)--(-1.2,7.1);')
    # proksimal tüp (kıvrımlı)
    b.append(f'\\draw[{TUP},line width=3.2pt] plot[smooth] coordinates {{(0,5.15) (-.5,4.75) (.45,4.4) (-.5,4.0) (.4,3.65) (0,3.2)}};')
    # Henle kulpu
    b.append(f'\\draw[{TUP},line width=3.2pt] (0,3.2)--(0,.9) to[out=-90,in=-90,looseness=1.7] (1,.9)--(1,3.2);')
    # distal tüp
    b.append(f'\\draw[{TUP},line width=3.2pt] plot[smooth] coordinates {{(1,3.2) (1.7,3.55) (1.5,4.1) (2.2,4.4) (3.2,5.0)}};')
    # toplama kanalı
    b.append(f'\\draw[{TUP},line width=5pt,-{{Stealth[length=3mm,width=3mm]}}] (3.2,5.5)--(3.2,-.2);')
    b.append(etiket)
    b.append(oklar)
    return '\n'.join(b)
# --- Q1: numaralı nefron ---
def sekil_nef1():
    e=(lab('I',-2.0,6.0,-1.55,6.0,-.9,6.0)+lab('II',-1.9,4.4,-1.45,4.4,-.85,4.3)+lab('III',.5,-1.1,.5,-.75,.5,.25)+lab('IV',1.4,5.45,1.5,5.1,1.58,4.3)+lab('V',4.3,2.8,3.95,2.8,3.4,2.8))
    return tk(nefron(e),.8)
# --- Q11: altı kısım numaralı nefron ---
def sekil_nef3():
    e=(lab('III',-2.0,6.0,-1.55,6.0,-.9,6.0)+lab('V',-1.9,4.4,-1.45,4.4,-.85,4.3)+lab('I',-1.0,2.0,-.6,2.0,-.12,2.0)+lab('VI',2.1,2.0,1.7,2.0,1.12,2.0)
       +lab('II',1.4,5.45,1.5,5.1,1.58,4.3)+lab('IV',4.3,2.8,3.95,2.8,3.4,2.8))
    return tk(nefron(e),.8)

# --- Q10: kılcal damarlı nefron ve numaralı geçişler (1 süzülme, 2 geri emilim, 3 salgılama) ---
def sekil_nef2():
    kap=(f'\\draw[{KAP},line width=1.8pt] plot[smooth] coordinates {{(-1.6,5.4) (-1.25,5.0) (-1.65,4.5) (-1.25,3.9) (-1.55,3.4)}};'
         f'\\draw[{KAP},line width=1.8pt] plot[smooth] coordinates {{(2.7,3.2) (2.35,2.85) (2.75,2.5) (2.4,2.1)}};')
    ok=lambda x1,y1,x2,y2:f'\\draw[vurgu!80!black,line width=2pt,-{{Stealth[length=2.8mm,width=2.5mm]}}] ({x1},{y1})--({x2},{y2});'
    oklar=kap+ok(-.2,5.95,-.72,5.95)+ok(-.6,4.15,-1.2,4.15)+ok(2.5,3.0,1.95,3.7)
    nm=lambda t,x,y:f'\\node[font=\\normalsize\\bfseries] at ({x},{y}) {{{t}}};'
    oklar+=nm('1',-1.15,6.3)+nm('2',-.95,4.55)+nm('3',2.5,3.9)
    return tk(nefron('',oklar=oklar),.8)

# --- Q2: böbrek boyuna kesiti ---
def sekil_bobrek():
    pts=[(-1.9,.2),(-1.6,1.5),(-.6,2.4),(.8,2.5),(1.8,1.7),(1.5,.8),(.9,.3),(.9,-.3),(1.5,-.8),(1.8,-1.7),(.8,-2.5),(-.6,-2.4),(-1.6,-1.5)]
    c=(-.2,0.0); sc=.8
    ic=[(c[0]+(x-c[0])*sc,c[1]+(y-c[1])*sc) for x,y in pts]
    P_=lambda L:' '.join(f'({x:.2f},{y:.2f})' for x,y in L)
    b=[f'\\draw[line width=1.8pt,fill=orange!25] plot[smooth cycle] coordinates {{{P_(pts)}}};']
    b.append(f'\\draw[line width=1pt,dashed] plot[smooth cycle] coordinates {{{P_(ic)}}};')
    # medulla piramitleri
    for a in (100,140,180,220,260):
        r=math.radians(a); bx,by=c[0]+1.25*math.cos(r),c[1]+1.3*math.sin(r)
        t1=(c[0]+1.2*math.cos(r+.26),c[1]+1.25*math.sin(r+.26)); t2=(c[0]+1.2*math.cos(r-.26),c[1]+1.25*math.sin(r-.26))
        b.append(f'\\draw[line width=1pt,fill=red!25!orange,fill opacity=.8] ({t1[0]:.2f},{t1[1]:.2f})--({t2[0]:.2f},{t2[1]:.2f})--({c[0]+.45:.2f},{c[1]:.2f})--cycle;')
    # havuzcuk, üreter
    b.append(f'\\draw[line width=1.2pt,fill=yellow!50] ({c[0]+.45:.2f},0) to[out=60,in=180] (.95,.25)--(.95,-.35) to[out=180,in=-60] ({c[0]+.45:.2f},0);')
    b.append('\\draw[line width=3.2pt,yellow!70!orange] (1.0,-.1)--(1.5,-.4)--(1.7,-1.2)--(1.7,-3.3);')
    # damarlar
    b.append(f'\\draw[{KAP},line width=3pt] (3.0,.95)--(1.0,.7); \\draw[{VEN},line width=3pt] (3.0,.5)--(1.0,.35);')
    b.append(lab('I',-3.3,1.9,-2.9,1.9,-1.3,1.4))
    b.append(lab('II',-3.3,-1.4,-2.9,-1.4,-.9,-1.0))
    b.append(lab('III',.2,-3.4,.3,-3.05,.4,-.2))
    b.append(lab('IV',2.9,-2.3,2.5,-2.3,1.8,-2.3))
    b.append(lab('V',3.9,1.7,3.6,1.4,2.8,.95))
    return tk('\n'.join(b),.75)
# --- Q15: hemodiyaliz düzeneği ---
def sekil_diyaliz():
    b=['\\draw[line width=1.6pt] (0,1.6) rectangle (7,3.3);\\draw[line width=1.6pt] (0,-.1) rectangle (7,1.6);']
    b.append('\\draw[line width=3pt,dashed,vurgu!80!black] (0,1.6)--(7,1.6);')
    b.append(f'\\draw[{KAP},line width=2pt,-{{Stealth[length=3mm,width=2.6mm]}}] (.2,3.75)--(1.6,3.75);\\node[font=\\small,anchor=west] at (1.8,3.75) {{kanın akış yönü}};')
    b.append(f'\\draw[{VEN},line width=2pt,-{{Stealth[length=3mm,width=2.6mm]}}] (6.8,-.55)--(5.4,-.55);\\node[font=\\small,anchor=east] at (5.2,-.55) {{diyaliz sıvısının akış yönü}};')
    b.append('\\node[font=\\small\\bfseries,anchor=west] at (7.2,2.5) {kan};\\node[font=\\small\\bfseries,anchor=west] at (7.2,.6) {diyaliz sıvısı};')
    b.append('\\node[font=\\small,anchor=west,align=left] at (7.2,1.6) {yarı geçirgen\\\\zar};')
    for x,y in [(.7,2.15),(1.5,2.9),(2.3,2.2),(3.2,2.0),(4.1,2.9),(4.9,2.2),(5.7,2.8),(6.4,2.1),(1.2,2.0),(5.3,2.6)]: b.append(f'\\fill ({x},{y}) circle (.1);')
    for x,y in [(1.1,2.6),(3.0,2.75),(5.0,2.0),(6.3,2.7)]: b.append(f'\\draw[{KAP},line width=1.4pt,fill={KAP},fill opacity=.4] ({x},{y}) circle (.22);')
    for x,y in [(.8,.5),(1.7,.9)]: b.append(f'\\fill ({x},{y}) circle (.1);')
    b.append(f'\\fill (1.0,-1.35) circle (.1);\\node[font=\\small,anchor=west] at (1.25,-1.35) {{üre}};\\draw[{KAP},line width=1.4pt,fill={KAP},fill opacity=.4] (2.8,-1.35) circle (.22);\\node[font=\\small,anchor=west] at (3.1,-1.35) {{alyuvar}};')
    return tk('\n'.join(b),.62)
AX='/pgf/number format/1000 sep={},tick label style={font=\\small},label style={font=\\small},axis lines=left,every axis plot/.append style={line width=1.4pt}'
def coords(v,x0=1): return ' '.join(f'({x0+i},{y})' for i,y in enumerate(v))
# --- Q5: nefron boyunca tüp sıvısı/plazma derişim oranı ---
G5={'K':[1,0,0,0,0],'L':[1,1,Fr(8,5),3,12],'M':[1,1,Fr(3,5),Fr(3,10),Fr(1,10)]}
def sekil_g5():
    b=['\\begin{axis}[width=7.6cm,height=5.6cm,xmin=.6,xmax=5.4,ymin=0,ymax=13,xtick={1,2,3,4,5},xticklabels={I,II,III,IV,V},ytick={0,1,4,8,12},xlabel={Nefron üzerindeki kısım},ylabel={Derişim oranı},legend style={font=\\small,at={(0.03,0.97)},anchor=north west,draw=none,fill=none},'+AX+']']
    for k,(st,mk_) in zip('KLM',[('red!75','square*'),('vurgu!80!black','triangle*'),('blue!70','*')]):
        b.append(f'\\addplot[{st},mark={mk_},mark size=2.3pt] coordinates {{'+coords([float(v) for v in G5[k]])+f'}};\\addlegendentry{{{k}}}')
    b.append('\\end{axis}')
    return tk('\n'.join(b),1.0)
# --- Q6: su içildikten sonra ADH ve idrar miktarı ---
G6={'ADH':[8,3,2,5,8],'IDR':[1,5,8,4,1]}
def sekil_g6():
    b=['\\begin{axis}[width=7.6cm,height=5.6cm,xmin=-.3,xmax=4.3,ymin=0,ymax=10,xtick={0,1,2,3,4},ytick={0,2,4,6,8,10},xlabel={Zaman (saat)},ylabel={Bağıl değer},legend style={font=\\small,at={(0.5,1.03)},anchor=south,legend columns=-1,draw=none,fill=none},'+AX+']']
    for k,nm,st,mk_ in [('ADH','Kandaki ADH düzeyi','red!75','square*'),('IDR','İdrar miktarı','blue!70','*')]:
        b.append(f'\\addplot[{st},mark={mk_},mark size=2.3pt] coordinates {{'+coords(G6[k],0)+f'}};\\addlegendentry{{{nm}}}')
    b.append('\\end{axis}')
    return tk('\n'.join(b),1.0)
# --- Q8: tüp sıvısı ozmotik derişimi ---
G8={'K':[300,300,1200,100,300,1200],'L':[300,300,1200,100,100,70]}
def sekil_g8():
    b=['\\begin{axis}[width=7.8cm,height=5.8cm,xmin=.6,xmax=6.4,ymin=0,ymax=1350,xtick={1,2,3,4,5,6},xticklabels={I,II,III,IV,V,VI},ytick={0,300,600,900,1200},xlabel={Nefron üzerindeki kısım},ylabel={Ozmotik derişim (mosm/L)},legend style={font=\\small,at={(0.5,1.03)},anchor=south,legend columns=-1,draw=none,fill=none},'+AX+']']
    for k,st,mk_ in [('K','red!75','square*'),('L','blue!70','*')]:
        b.append(f'\\addplot[{st},mark={mk_},mark size=2.3pt] coordinates {{'+coords(G8[k])+f'}};\\addlegendentry{{{k}}}')
    b.append('\\end{axis}')
    return tk('\n'.join(b),.95)
# --- Q9: iki grup sonuç çubuk grafiği ---
G9={'idrar':[10,60,12],'ozm':[2000,300,1800]}
def sekil_g9():
    def ax(shift,ymax,yt,yl,key):
        return (f'\\begin{{axis}}[ybar,width=5.4cm,height=5.2cm,xshift={shift}cm,xmin=.4,xmax=3.6,xtick={{1,2,3}},xticklabels={{I,II,III}},ymin=0,ymax={ymax},ytick={{{yt}}},xlabel={{Grup}},ylabel={{{yl}}},bar width=14pt,'+AX+']'
                +f'\\addplot[fill=vurgu!45,draw=black,line width=1pt,nodes near coords,nodes near coords style={{font=\\small}}] coordinates {{'+coords(G9[key])+'};\\end{axis}')
    return tk(ax(0,80,'0,20,40,60,80','İdrar miktarı (mL/gün)','idrar')+ax(6.2,2400,'0,600,1200,1800,2400','İdrar ozmolaritesi (mosm/L)','ozm'),.78)
# --- Q14: böbrek atardamarı ve toplardamarı ---
G14={'K':(100,80),'L':(100,100),'M':(100,108)}
def sekil_g14():
    b=['\\begin{axis}[ybar,width=7.8cm,height=5.6cm,xmin=.4,xmax=3.6,xtick={1,2,3},xticklabels={K,L,M},ymin=0,ymax=130,ytick={0,50,100},xlabel={Madde},ylabel={Bağıl derişim},bar width=16pt,legend style={font=\\small,at={(0.5,1.03)},anchor=south,legend columns=-1,draw=none,fill=none},'+AX+']']
    b.append('\\addplot[fill=red!45,draw=black,line width=1pt] coordinates {'+' '.join(f'({i+1},{G14[k][0]})' for i,k in enumerate('KLM'))+'};\\addlegendentry{Böbrek atardamarı}')
    b.append('\\addplot[fill=blue!35,draw=black,line width=1pt] coordinates {'+' '.join(f'({i+1},{G14[k][1]})' for i,k in enumerate('KLM'))+'};\\addlegendentry{Böbrek toplardamarı}')
    b.append('\\end{axis}')
    return tk('\n'.join(b),.95)
# ============================ SORULAR ============================
T_YAPI=('bo-yapi','Böbrek ve nefron yapısı'); T_SUREC=('bo-surec','Süzülme, geri emilim ve salgılama'); T_TABLO=('bo-tablo','Madde derişimi tabloları ve hesaplar')
T_HORMON=('bo-hormon','ADH ve aldosteron ile su-tuz dengesi'); T_SAGLIK=('bo-saglik','Böbrek işlevi bozuklukları ve diyaliz'); T_DIGER=('bo-diger','Canlılarda boşaltım organları')
def tp(t): return dict(tipId=t[0],tip=t[1])
ROMS=['I','II','III','IV','V']
# ---------- 01 · nefron kısımları · kolay ----------
SK1=sekil_nef1()
NEF=B('Nefronun kısımları','nefron; Bowman kapsülü ve glomerulus, proksimal tüp, Henle kulpu, distal tüp ve toplama kanalından oluşur. Süzülme ilk kısımda, geri emilim ve salgılama tüp kısımlarında gerçekleşir')
q(1,*T_YAPI,'kolay','Nefron','Nefronun kısımlarını şekilden tanıyıp görevleriyle ilişkilendirir.','şekilli','nefron şeması, numaralı kısımlar','numaralı nefron kısımları',
 'Nefronda kısımlar sırasıyla Bowman kapsülü, proksimal tüp, Henle kulpu, distal tüp ve toplama kanalıdır; besin maddelerinin tamamının geri emilimi proksimal tüpte biter.','Süzülmenin olduğu kısmı geri emilim yeri saymak; glikozun geri emiliminin Henle kulpunda ya da toplama kanalında olduğunu düşünmek.',
 [A('Kısımları tanı','Kapsül ve içindeki yumak I, kapsülden sonraki kıvrımlı tüp II, U şeklindeki bölüm III, ardından gelen kıvrımlı tüp IV ve toplayıcı uzun tüp V’tir.','I: Bowman kapsülü ve glomerulus · II: proksimal tüp · III: Henle kulpu · IV: distal tüp · V: toplama kanalı'),
  A('Olayı kısma bağla','Glikoz ve amino asitler süzüntüden taşıyıcı proteinlerle geri alınır ve bu işlem ilk tüp kısmında tamamlanır.','Besinlerin tamamının geri emilimi → proksimal tüp'),
  A('Numarayı seç','Proksimal tüp şekilde II ile gösterilmiştir.','Cevap: II')],
 metin='Şekilde insan böbreğinde bulunan bir nefronun bazı kısımları I, II, III, IV ve V ile numaralandırılmıştır.\nBuna göre, süzüntüde bulunan glikoz ve amino asitlerin tamamının kana geri emildiği kısım numaralı yapılardan hangisidir?',
 dogru='II',sira=ROMS,yan=[('I','I numaralı yapı Bowman kapsülü ve glomerulustur; kandan süzülmenin gerçekleştiği yer olduğu için geri emilimle karıştırılmıştır.','bilgi'),
  ('III','III numaralı yapı Henle kulpudur; burada ağırlıklı olarak su ve tuz geri emilir, besin maddelerinin geri emilimi bundan önce tamamlanmıştır.','bilgi'),
  ('IV','IV numaralı yapı distal tüptür; tuz ve su geri emilimi ile H⁺ ve K⁺ salgılanması burada gerçekleşir, süzüntüde artık glikoz kalmaz.','bilgi'),
  ('V','V numaralı yapı toplama kanalıdır; ADH etkisiyle su geri emilir ve idrar bu kanaldan havuzcuğa ilerler.','bilgi')],
 istenen='Glikoz ve amino asitlerin tamamının geri emildiği kısmın numarası.',ip=['Besin maddelerinin süzüntüden geri alınmasının nefronun hangi bölümünde tamamlandığını düşün.'],bilgi=[NEF],
 puf='Süzüntü Henle kulpuna girmeden hangi tüp kısmında bu maddeleri kaybeder?',sekil=SK1)
# ---------- 02 · böbrek kesiti · kolay ----------
SK2=sekil_bobrek()
q(2,*T_YAPI,'kolay','Böbrek','Böbreğin kesit şemasında bölgeleri tanır ve nefron kısımlarının bulunduğu yeri belirler.','şekilli','böbrek kesiti, numaralı bölgeler','böbrek kesiti',
 'Böbreğin dış bölgesi olan korteksteki nefron kısımları Bowman kapsülü, glomerulus ve kıvrımlı tüplerdir; iç bölgedeki medullada Henle kulpları ve toplama kanalları bulunur.','Bowman kapsüllerini medullada sanmak; havuzcuğu süzülme yeri saymak.',
 [A('Bölgeleri tanı','Dış bölge korteks, iç kısımdaki piramit biçimli yapılar medulla, merkezdeki boşluk havuzcuk, aşağı uzanan tüp üreter, böbreğe giren damar böbrek atardamarıdır.','I: korteks · II: medulla · III: havuzcuk · IV: üreter · V: atardamar'),
  A('Bowman kapsüllerinin yerini bul','Glomerulus ve Bowman kapsülü, nefronun dış bölgedeki kısımlarıdır.','Bowman kapsülü → korteks'),
  A('Numarayı seç','Korteks şekilde I ile gösterilmiştir.','Cevap: I')],
 metin='Şekilde insan böbreğinin boyuna kesiti ve böbreğe bağlanan bazı yapılar I, II, III, IV ve V ile numaralandırılmıştır.\nBuna göre, nefronların Bowman kapsüllerinin ve glomeruluslarının bulunduğu bölüm numaralı yapılardan hangisidir?',
 dogru='I',sira=ROMS,yan=[('II','II numaralı bölge medulladır; Henle kulpları ve toplama kanalları burada bulunur, Bowman kapsülleri bu bölgede yer almaz.','bilgi'),
  ('III','III numaralı yapı böbrek havuzcuğudur; toplama kanallarından gelen idrar burada toplanır, süzülme yapılmaz.','bilgi'),
  ('IV','IV numaralı yapı üreterdir; idrarı havuzcuktan idrar torbasına taşır, nefron kısmı içermez.','bilgi'),
  ('V','V numaralı yapı böbrek atardamarıdır; kanı böbreğe getirir, süzülme yeri olan Bowman kapsülü bu damarın dışında kalır.','bilgi')],
 istenen='Bowman kapsüllerinin ve glomeruluslarının bulunduğu bölümün numarası.',ip=['Nefronun hangi kısımlarının böbreğin dış, hangilerinin iç bölgesinde yer aldığını hatırla.'],
 bilgi=[B('Böbreğin bölgeleri','böbrek dıştan içe korteks ve medulla bölgelerinden oluşur; medulladan sonra idrarın toplandığı havuzcuk gelir ve havuzcuktan üreter çıkar')],
 puf='Süzülme yapan yumaklar böbreğin en dış bölgesindedir; kesitte dıştan içe sırayla ilerle.',sekil=SK2)
# ---------- 03 · süzüntüde bulunmayan madde · kolay · olumsuz ----------
q(3,*T_SUREC,'kolay','Süzülme','Süzülmenin molekül büyüklüğüne bağlı olduğunu bilir ve süzüntüde bulunmayan maddeyi belirler.','düz','süzüntü içeriği','süzüntüde bulunmayan madde',
 'Glomerulustaki süzülme kan basıncıyla gerçekleşir ve molekül büyüklüğüne bağlıdır; kan hücreleri ile plazma proteinleri gibi büyük yapılar Bowman kapsülüne geçemez, küçük moleküller geçer.','Plazmadaki tüm maddelerin süzüldüğünü sanmak; ürenin süzülmediğini düşünmek.',
 [A('Süzülmenin ölçütünü hatırla','Glomerulus kılcallarından kan basıncıyla geçiş molekül büyüklüğüne bağlıdır; küçük moleküller geçer, büyükler geçemez.','Küçük: geçer · Büyük: geçemez'),
  A('Şıkları büyüklüğe göre ayır','Amino asit, glikoz, üre ve sodyum iyonu küçük yapılardır; albümin ise büyük bir plazma proteinidir.','Küçük: amino asit, glikoz, üre, Na⁺ · Büyük: albümin'),
  A('Süzüntüde bulunmayanı seç','Büyük molekül süzüntüye geçemez.','Cevap: albümin')],
 metin='Sağlıklı bir insanda kan, glomerulus kılcal damarlarından geçerken kan basıncının etkisiyle plazmanın bir kısmı Bowman kapsülüne süzülür. Bu süzülmede maddelerin geçişi, molekül büyüklüğüne bağlıdır.\nBuna göre, sağlıklı bir bireyde Bowman kapsülündeki süzüntüde bulunması beklenmeyen madde aşağıdakilerden hangisidir?',
 dogru='Albümin',sira=['Amino asit','Üre','Sodyum iyonu','Glikoz','Albümin'],yan=[('Amino asit','Amino asitler küçük moleküllüdür; plazmadan süzüntüye geçtikleri için süzüntüde bulunmaları beklenir.','bilgi'),
  ('Üre','Üre küçük bir azotlu atıktır; süzüntüye geçer ve idrarla atılır, bu nedenle süzüntüde bulunması beklenir.','bilgi'),
  ('Sodyum iyonu','Sodyum iyonları küçük olduğundan süzüntüye geçer; sonradan tüplerde geri emilir, bu yüzden süzüntüde bulunmaları beklenir.','bilgi'),
  ('Glikoz','Glikoz küçük bir moleküldür ve süzüntüde plazmadakiyle aynı derişimde bulunur; sonradan proksimal tüpte geri emilir.','bilgi')],
 istenen='Süzüntüde bulunması beklenmeyen madde.',ip=['Süzülmede geçişi sınırlayan ölçütü hatırla ve şıklardaki maddeleri bu ölçüte göre karşılaştır.'],
 bilgi=[B('Glomerulusta süzülme','kan basıncının etkisiyle plazmanın küçük molekülleri Bowman kapsülüne geçer; kan hücreleri ve plazma proteinleri kılcal damarda kalır')],
 puf='Süzülmede sınır boyuttur; plazmadaki en iri moleküllü maddeyi ara.')
# ---------- 04 · madde derişimi tablosu · zor · öncüllü ----------
T4=dict(K=(7000,0,0),L=(100,100,0),M=(30,30,1800)); SUZ,IDR=180,Fr(9,5)
def atilan_oran(m): # süzülen miktar: derişim × hacim (dL); atılan / süzülen
    p,s,i=T4[m]; return Fr(i)*IDR*10/(Fr(s)*SUZ*10) if s else None
assert T4['K'][1]==0 and T4['L'][1]==T4['L'][0] and T4['L'][2]==0 and atilan_oran('M')==Fr(3,5)
d4={'I':(True,'K maddesinin süzüntüdeki derişimi 0’dır; plazmada bulunduğu hâlde Bowman kapsülüne geçmemiş, süzülmemiştir.'),
    'II':(True,'L maddesi süzüntüde plazmadakiyle aynı derişimdedir ve idrarda bulunmaz; süzülmüş ve tamamı geri emilmiştir.'),
    'III':(False,'M maddesinden süzülen miktarın %60’ı idrarla atılmıştır; %40’ı geri emilmiştir.')}
r=onc(d4,'C')
SK4=tablo_svg(['Madde','Plazma','Süzüntü','İdrar'],[[k,*T4[k]] for k in 'KLM'])
qo(4,r,*T_TABLO,'zor','Madde derişimi tablosu','Plazma, süzüntü ve idrar derişimlerini ve su geri emilimini birlikte yorumlayarak maddelerin nefrondaki akıbetini belirler.',
 'derişim tablosu, süzülme ve geri emilim','K, L, M madde derişimi tablosu','Süzüntüde derişimi 0 olan madde süzülmemiştir; idrardaki miktar, derişim ile idrar hacminin çarpımıdır ve süzülen miktarla karşılaştırılarak geri emilim ya da salgılama anlaşılır.','Su geri emildiği için idrardaki derişim artışını maddenin geri emilmediği şeklinde yorumlamak; yalnız derişimlere bakıp hacmi unutmak.',
 metin='Tabloda sağlıklı bir bireyin plazmasında, glomerulustan Bowman kapsülüne süzülen sıvıda ve idrarında bulunan K, L ve M maddelerinin derişimleri (mg/100 mL) verilmiştir. Bu bireyde bir günde 180 L süzüntü oluşmuş ve 1,8 L idrar atılmıştır.\nBuna göre,\nI. K maddesi glomerulustan Bowman kapsülüne süzülmemiştir.\nII. L maddesi süzüldükten sonra nefron tüplerinde tamamen geri emilmiştir.\nIII. M maddesi süzüldükten sonra hiç geri emilmemiştir.\nifadelerinden hangileri doğrudur?',
 istenen='Doğru olan öncüllerin hangileri olduğu.',ip=['İdrarla atılan miktarı bulmak için derişimin yanında hacmi de hesaba kat.'],
 bilgi=[B('Süzülen ve atılan miktar','bir maddenin süzülen miktarı süzüntüdeki derişim ile süzüntü hacminin, idrarla atılan miktarı idrardaki derişim ile idrar hacminin çarpımıdır; ikisinin karşılaştırılması geri emilim ya da salgılama hakkında bilgi verir')],
 puf='Derişimler tek başına yetmez; her madde için süzülen miktarı ve atılan miktarı hacimle çarparak karşılaştır.',sekil=SK4)
# ---------- 05 · nefron boyunca derişim oranı · orta · olumsuz ----------
assert G5['K'][1]==0 and G5['L'][0]==G5['L'][1]==1 and G5['M'][0]==G5['M'][1]==1 and G5['M'][2]<G5['M'][1] and G5['M'][3]<G5['M'][2] and G5['M'][4]<G5['M'][3]
assert max(G5['L'])==G5['L'][4]>max(max(G5['K']),max(G5['M']))
S5a='K maddesinin tamamı, proksimal tüpün sonuna kadar geri emilmiştir.'
S5b='L maddesinin derişim oranındaki artış, suyun bu maddeden daha büyük oranda geri emilmesiyle ilişkilidir.'
S5c='M maddesinin derişim oranı I ile II arasında değişmemiş, sonraki kısımlarda sürekli azalmıştır.'
S5e='Tüp sıvısında en fazla derişen madde L’dir ve bu durum V numaralı kısımda görülür.'
S5d='I ile II arasında L ve M maddelerinin derişim oranlarının değişmemesi, bu kısımda bu maddelerin hiç geri emilmediğini gösterir.'
q(5,*T_SUREC,'orta','Nefronda madde geçişi','Nefron boyunca derişim oranı grafiğinden maddelerin geri emilim durumunu yorumlar.','grafik','derişim oranı grafiği, su ve madde geri emilimi','tüp sıvısı/plazma derişim oranı grafiği',
 'Derişim oranındaki değişim, maddenin geri emilimini suyun geri emilimiyle karşılaştırmayı sağlar.','Oran değişimini suyun geri emilimini hesaba katmadan yorumlamak.',
 [A('Grafiği oku','K oranı II’de 0’a düşer, L oranı V’te 12’ye ulaşır, M oranı I ile II arasında 1’de kalır ve sonra azalır.','K: 1 → 0 · L: 1 → 12 · M: 1 → 0,1'),
  A('Oran değişiminin anlamını hatırla','Oran sabitse madde ile su aynı oranda geri emilmiştir; maddeye ait geri emilim yok demek değildir.','Oran sabit → madde ve su aynı oranda geri emilir'),
  A('Şıkları sına','K, L ve M için verilen yorumlar grafikle uyumludur; I–II arasında L ve M için “hiç geri emilmedi” yorumu uyumlu değildir.','Hatalı yorum: I–II arasında geri emilim yok'),
  A('Şıkkı seç','Söylenemeyen ifade I ile II arasında hiç geri emilim olmadığını söyleyendir.','Cevap: bu ifade')],
 metin='Grafikte, bir nefronun I, II, III, IV ve V ile gösterilen kısımlarında K, L ve M maddelerinin tüp sıvısındaki derişiminin plazmadaki derişimine oranı verilmiştir. I Bowman kapsülü, II proksimal tüpün sonu, III Henle kulpunun sonu, IV distal tüpün sonu, V toplama kanalının sonudur.\nBuna göre, K, L ve M maddeleriyle ilgili aşağıdakilerden hangisi söylenemez?',
 dogru=S5d,sira=yer('C',S5d,[S5a,S5b,S5c,S5e]),yan=[(S5a,'K maddesinin oranı II’de 0’dır; bu madde proksimal tüpün sonuna kadar tamamen geri emilmiştir, ifade söylenebilir.','bilgi'),
  (S5b,'L maddesinin oranı tüp boyunca 1’den 12’ye çıkmıştır; bu, suyun maddeden daha çok geri emildiğini gösterir ve ifade söylenebilir.','bilgi'),
  (S5c,'M maddesinin oranı I ve II’de 1’dir, sonra azalarak 0,1’e düşer; ifade grafikle uyumludur ve söylenebilir.','bilgi'),
  (S5e,'L maddesinin oranı V’te 12’dir ve K ile M’nin değerlerinden büyüktür; ifade söylenebilir.','bilgi')],
 istenen='Grafiğe göre söylenemeyen ifade.',ip=['Her ifadeyi grafikteki oran değerleriyle ve suyun geri emilimiyle karşılaştır.'],
 bilgi=[B('Tüp sıvısı/plazma oranı','tüp sıvısındaki derişimin plazmadakine oranı, maddenin geri emilen su miktarına göre ne kadar geri emildiğini gösterir; oran, madde ile suyun geri emilimini karşılaştırmaya yarar')],
 puf='Her şıkkı grafikteki değerlerle tek tek sına.',sekil=sekil_g5())
# ---------- 06 · ADH ve idrar miktarı grafiği · orta · öncüllü ----------
assert G6['ADH'][1]<G6['ADH'][0] and G6['ADH'][3]>G6['ADH'][2] and G6['IDR'][2]>G6['IDR'][0] and G6['IDR'][4]<G6['IDR'][2]
d6={'I':(True,'1. saatte ADH düzeyi 0. saate göre düşmüştür; ADH azaldığında toplama kanalında geri emilen su miktarı azalır.'),
    'II':(False,'2. saatte ADH düzeyi düşük, idrar miktarı yüksektir; idrar seyreltik olduğundan ozmotik derişimi 0. saattekinden düşüktür.'),
    'III':(True,'3. ve 4. saatlerde ADH düzeyi artmış, idrar miktarı azalmıştır; ADH su geri emilimini artırarak idrar miktarını azaltır.')}
r=onc(d6,'E')
qo(6,r,*T_HORMON,'orta','ADH','ADH düzeyi ile idrar miktarı arasındaki ilişkiyi grafikten yorumlar.','ADH düzeyi ve idrar miktarı grafiği','su içildikten sonra ADH ve idrar miktarı',
 'ADH toplama kanalının suya geçirgenliğini artırır; kan plazması seyrelince ADH azalır, su geri emilimi azalır ve bol, seyreltik idrar oluşur.','ADH azaldığında idrarın daha derişik olacağını düşünmek; grafikteki zaman gecikmesini yok saymak.',
 metin='Sağlıklı bir birey 0. saatte kısa sürede 1 litre su içiyor. Sonraki 4 saat boyunca kandaki ADH düzeyi ile idrar miktarı ölçülüyor ve bağıl değerlerle grafikte gösteriliyor.\nBuna göre,\nI. 1. saatte toplama kanalından geri emilen su miktarı, 0. saatteki değerden azdır.\nII. 2. saatte idrarın ozmotik derişimi, 0. saattekinden yüksektir.\nIII. 3. ve 4. saatlerde idrar miktarındaki azalma, ADH düzeyindeki artışla uyumludur.\nifadelerinden hangileri doğrudur?',
 istenen='Doğru olan öncüllerin hangileri olduğu.',ip=['ADH düzeyindeki değişimin toplama kanalındaki su geri emilimini ve idrarın derişimini nasıl etkilediğini düşün.'],
 bilgi=[B('ADH','hipotalamusta üretilir, hipofizin arka lobundan salgılanır; distal tüp ve toplama kanalının suya geçirgenliğini artırır ve geri emilen su miktarını yükseltir')],
 puf='ADH düzeyi ile geri emilen su miktarı aynı yönde, idrar miktarı ters yönde değişir.',sekil=sekil_g6())
# ---------- 07 · aldosteron tablosu · orta · olumsuz ----------
T7={'K':('Normal',150,80),'L':('Yüksek',20,140),'M':('Düşük',280,40)}
assert T7['L'][1]<T7['K'][1]<T7['M'][1] and T7['L'][2]>T7['K'][2]>T7['M'][2]
SK7=tablo_svg(['Birey','Aldosteron','İdrar Na+','İdrar K+'],[[k,*T7[k]] for k in 'KLM'])
S7y='Aldosteron, böbrek üstü bezinin medullasında üretilir ve distal tüpte K⁺ geri emilimini artırır.'
S7b='L bireyinde distal tüp ve toplama kanalında Na⁺ geri emilimi, K bireyine göre artmıştır.'
S7c='M bireyinde kan hacminin ve kan basıncının, K bireyine göre düşük olması beklenir.'
S7d='L bireyinde idrarla atılan K⁺ miktarının artması, aldosteronun K⁺ salgılanmasını artırmasıyla açıklanır.'
S7e='Aldosteron düzeyi yüksek olan L bireyinde, Na⁺ ile birlikte suyun geri emilimi de artar.'
q(7,*T_HORMON,'orta','Aldosteron','Aldosteron düzeyine bağlı Na⁺ ve K⁺ atılımını tablodan yorumlar.','tablo','aldosteron düzeyi ve iyon atılımı tablosu','aldosteron tablosu',
 'Aldosteronun üretim yeri ve nefron tüplerindeki etkisi, tablodaki iyon atılımıyla birlikte yorumlanır.','Hormonun üretim yerini ya da etkisini yanlış hatırlamak.',
 [A('Tabloyu oku','L bireyinde idrarla Na⁺ az, K⁺ çok atılmıştır; M bireyinde Na⁺ çok, K⁺ az atılmıştır.','L: Na⁺ 20, K⁺ 140 · M: Na⁺ 280, K⁺ 40 · K: Na⁺ 150, K⁺ 80'),
  A('Aldosteronun etkisini hatırla','Aldosteron Na⁺ geri emilimini ve K⁺ salgısını artırır; su Na⁺ ile birlikte geri emilir.','Aldosteron ↑ → Na⁺ geri emilimi ↑ · K⁺ salgısı ↑'),
  A('Şıkları sına','L ve M için yazılan yorumlar tabloyla uyumludur; üretim yeri ve K⁺ etkisini söyleyen ifade bilgiyle çelişir.','Yanlış ifade: medulla ve K⁺ geri emilimi'),
  A('Şıkkı seç','Yanlış olan ifade aldosteronun üretim yeri ve etkisini yanlış veren ifadedir.','Cevap: bu ifade')],
 metin='Tabloda üç bireyin kan aldosteron düzeyleri ile bir günde idrarla attıkları Na⁺ ve K⁺ miktarları (mmol/gün) verilmiştir. K bireyi sağlıklıdır; L ve M bireylerinde ise böbrek üstü bezinin işleviyle ilgili farklı sorunlar vardır.\nBuna göre, aşağıdaki ifadelerden hangisi yanlıştır?',
 dogru=S7y,sira=yer('A',S7y,[S7b,S7c,S7d,S7e]),yan=[(S7b,'L bireyinin idrarındaki Na⁺ miktarı K bireyinkinden azdır; bu, aldosteronun Na⁺ geri emilimini artırdığını gösterir ve ifade doğrudur.','bilgi'),
  (S7c,'M bireyi Na⁺ kaybettiği için su da kaybeder; kan hacminin ve basıncının düşmesi beklenir, ifade doğrudur.','bilgi'),
  (S7d,'L bireyinin idrarındaki K⁺ miktarı K bireyinkinden fazladır; aldosteron K⁺ salgılanmasını artırır ve ifade doğrudur.','bilgi'),
  (S7e,'Su, geri emilen Na⁺ ile birlikte kana geçer; aldosteron fazlalığında su geri emilimi de artar ve ifade doğrudur.','bilgi')],
 istenen='Yanlış olan ifade.',ip=['Aldosteronun üretildiği bezi ve distal tüpte Na⁺ ile K⁺ üzerindeki etkisini hatırla.'],
 bilgi=[B('Aldosteron','böbrek üstü bezinden salgılanan, nefron tüplerinde tuz dengesini düzenleyen hormondur')],
 puf='Aldosteronun üretim yerini ve K⁺ üzerindeki etkisini tabloyla karşılaştır.',sekil=SK7)
# ---------- 08 · ozmotik derişim grafiği · zor ----------
assert G8['K'][:4]==G8['L'][:4] and G8['K'][2]==max(G8['K']) and G8['K'][3]<G8['K'][1] and G8['K'][5]>G8['K'][4]>G8['K'][3] and G8['L'][5]<G8['L'][4]==G8['L'][3]
S8e='ADH varken V ile VI arasında ozmotik derişimin artması, toplama kanalından suyun geri emilmesinden kaynaklanır.'
S8a='I ile II arasında derişimin değişmemesi, bu kısımda geri emilimin olmadığını gösterir.'
S8b='II ile III arasında ozmotik derişimin artması, tuzun tüp içine salgılanmasından kaynaklanır.'
S8c='III ile IV arasında ozmotik derişimin azalması, suyun tüp içine geçmesinden kaynaklanır.'
S8d='ADH yokken V ile VI arasında ozmotik derişimin azalması, toplama kanalının suya geçirgenliğinin artmasından kaynaklanır.'
q(8,*T_SUREC,'zor','Nefronda ozmotik derişim','Nefron boyunca ozmotik derişim değişimini ADH varlığıyla birlikte yorumlar.','grafik','tüp sıvısı ozmotik derişimi, ADH varlığı ve yokluğu','ADH varken ve yokken ozmotik derişim grafiği',
 'İnen kolda su çıkar ve derişim artar, çıkan kolda su geçmeden tuz geri alınır ve derişim azalır; distal tüp ile toplama kanalının suya geçirgenliğini ADH belirler.','Derişim artışını tuz salgısıyla açıklamak; ADH yokken toplama kanalında su geri emildiğini sanmak.',
 [A('Ortak bölümü oku','K ve L eğrileri I–IV arasında aynıdır: 300, 300, 1200 ve 100 mosm/L.','I–IV: 300 → 300 → 1200 → 100'),
  A('ADH’li durumu oku','K’de V’te 300, VI’da 1200 mosm/L’dir; ADH distal tüp ve toplama kanalını suya geçirgen yapar, su dışarı çıkar ve derişim artar.','K: V 300, VI 1200 → su geri emilimi'),
  A('ADH’siz durumu oku','L’de V’te 100, VI’da 70 mosm/L’dir; bu kısımlar suya geçirgen olmadığından su geri emilmez, tüp sıvısı seyrelmeye devam eder.','L: V 100, VI 70'),
  A('Şıkları sına','Yalnız ADH varken V–VI arasındaki artış suyun geri emilmesiyle açıklanır; diğer yorumlar mekanizmayı yanlış verir.','Doğru yorum: ADH varken V–VI arasında su geri emilimi')],
 metin='Grafikte, K ve L bireylerinin nefronlarında tüp sıvısının ozmotik derişimi I, II, III, IV, V ve VI ile gösterilen kısımlarda verilmiştir. I Bowman kapsülü, II proksimal tüpün sonu, III Henle kulpunun dönüş noktası, IV çıkan kolun sonu, V distal tüpün sonu, VI toplama kanalının sonudur. K bireyinde ADH yeterli, L bireyinde ADH yoktur.\nBuna göre, aşağıdakilerden hangisi doğrudur?',
 dogru=S8e,sira=yer('E',S8e,[S8a,S8b,S8c,S8d]),yan=[(S8a,'Derişimin değişmemesi, su ve çözünenlerin aynı oranda geri emildiğini gösterebilir; geri emilimin olmadığını göstermez, ifade yanlıştır.','bilgi'),
  (S8b,'II ile III arasındaki artış, inen kolda suyun tüpten çıkmasından kaynaklanır; tuz salgılanması bu artışın nedeni değildir.','bilgi'),
  (S8c,'III ile IV arasındaki azalma, çıkan kolda tuzun geri emilmesinden kaynaklanır; çıkan kol suya geçirgen olmadığından su tüp içine geçmez.','bilgi'),
  (S8d,'ADH yokken toplama kanalı suya geçirgen olmaz; V ile VI arasındaki azalma tuz geri emiliminden kaynaklanır, su geri emilimi artmaz.','bilgi')],
 istenen='Grafiğe göre doğru olan ifade.',ip=['İnen kol, çıkan kol ve toplama kanalının suya geçirgenliğini ve ADH’nin etkisini ayrı ayrı düşün.'],
 bilgi=[B('Derişimin değişim nedenleri','tüp sıvısının ozmotik derişimi su çıkışıyla artar, tuz geri emilimiyle azalır; su geçişi yalnız suya geçirgen kısımlarda olur')],
 puf='Her kısımda tüp sıvısına giren ya da çıkan maddeyi belirle: derişim artışı su çıkışını, azalışı tuz çıkışını gösterir.',sekil=sekil_g8())
# ---------- 09 · ADH deneyi çubuk grafikleri · orta ----------
assert G9['idrar'][1]>G9['idrar'][0] and G9['ozm'][1]<G9['ozm'][0] and abs(G9['idrar'][2]-G9['idrar'][0])<=3
S9c='II. gruptaki idrar miktarı artışı, nefronda geri emilen su miktarındaki azalmadan kaynaklanır.'
S9a='ADH, toplama kanalının suya geçirgenliğini azaltarak idrar miktarını artırır.'
S9b='II. grupta kan plazmasının ozmotik derişimi, I. gruptakinden daha düşüktür.'
S9d='III. grupta enjekte edilen ADH, idrarın ozmotik derişimini azaltmıştır.'
S9e='Hipofiz arka lobunun çıkarılması, glomerulustaki süzülmeyi durdurmuştur.'
q(9,*T_HORMON,'orta','ADH','ADH eksikliği ve takviyesi deneyinin sonuçlarını yorumlar.','grafik','ADH deneyi, idrar miktarı ve ozmolaritesi çubuk grafikleri','ADH deneyi çubuk grafikleri',
 'ADH yetersizse toplama kanalından su geri emilimi azalır; idrar çok miktarda ve seyreltik olur, ADH verilince değerler kontrole yaklaşır.','ADH’nin su geri emilimini azalttığını sanmak; hormon eksikliğinde süzülmenin durduğunu düşünmek.',
 [A('Grafikleri oku','II. grupta idrar 60 mL ve 300 mosm/L, I. grupta 10 mL ve 2000 mosm/L, III. grupta 12 mL ve 1800 mosm/L’dir.','I: 10 mL, 2000 · II: 60 mL, 300 · III: 12 mL, 1800'),
  A('Hormonun etkisini çıkar','Arka lob çıkarılınca idrar artmış ve seyrelmiş, ADH verilince değerler kontrole yaklaşmıştır.','ADH yok → bol, seyreltik idrar · ADH var → az, derişik idrar'),
  A('Nedeni belirle','İdrar miktarının artışı, toplama kanalından geri emilen su miktarının azalmasından kaynaklanır.','Geri emilen su ↓ → idrar miktarı ↑'),
  A('Şıkkı seç','Bu yorumu yapan ifade doğrudur.','Cevap: II. gruptaki artışın nedenini veren ifade')],
 metin='Bir araştırmacı sıçanları üç gruba ayırıyor. I. grup kontrol grubudur; II. grupta hipofiz arka lobu çıkarılmış; III. grupta hipofiz arka lobu çıkarılmış ve ADH enjekte edilmiştir. Bir gün sonra her grubun günlük idrar miktarı ve idrarın ozmotik derişimi ölçülmüş, sonuçlar grafiklerde gösterilmiştir.\nBuna göre, aşağıdakilerden hangisi doğrudur?',
 dogru=S9c,sira=yer('C',S9c,[S9a,S9b,S9d,S9e]),yan=[(S9a,'ADH, toplama kanalının suya geçirgenliğini artırır; geçirgenliği azalttığı yorumu verilerle çelişir ve idrar miktarını azaltır.','bilgi'),
  (S9b,'ADH’si olmayan II. grup çok su kaybettiği için kan plazmasının ozmotik derişimi I. gruptakinden yüksektir; ifade ters kurulmuştur.','bilgi'),
  (S9d,'III. grupta idrarın ozmotik derişimi II. gruptan yüksektir; enjekte edilen ADH idrarı derişik hâle getirmiştir, azaltmamıştır.','bilgi'),
  (S9e,'Süzülme glomerulusta kan basıncıyla gerçekleşir; hormon eksikliği süzülmeyi durdurmaz, II. grupta idrar oluşumu sürmektedir.','bilgi')],
 istenen='Deney sonuçlarına göre doğru olan ifade.',ip=['I, II ve III. gruplardaki idrar miktarını ve derişimini karşılaştırarak ADH’nin etkisini çıkar.'],
 bilgi=[B('ADH eksikliği','hipofiz arka lobundan ADH salgılanamazsa toplama kanalından su geri emilimi azalır ve bol miktarda seyreltik idrar atılır')],
 puf='Gruplar arasında yalnız ADH farkı var; idrar miktarı ve derişimi birlikte değişir.',sekil=sekil_g9())
# ---------- 10 · numaralı geçişler · orta · öncüllü ----------
d10={'I':(False,'1 numaralı geçiş süzülmedir; kan basıncıyla ve molekül büyüklüğüne bağlı olarak pasif gerçekleşir, ATP harcanmaz.'),
     'II':(True,'2 numaralı geçişte glikoz, proksimal tüp hücrelerindeki taşıyıcı proteinlerle ve ATP harcanarak kana geri alınır.'),
     'III':(True,'3 numaralı geçişte kandan tüpe salgılanan H⁺ iyonları, kan pH’sının dengelenmesine katkı sağlar.')}
r=onc(d10,'D')
qo(10,r,*T_SUREC,'orta','Nefronda madde geçişi','Süzülme, geri emilim ve salgılamayı oklarla gösterilen geçişlerde ayırt eder.','Nefron ve kılcal damarlar, numaralı geçiş okları','numaralı geçişler: süzülme, geri emilim, salgılama',
 'Süzülme glomerulustan kapsüle pasif; geri emilim tüpten kana, salgılama kandan tüpe doğrudur ve glikoz geri emilimi ile H⁺ salgısı taşıyıcılarla yapılır.','Süzülmeyi aktif sanmak; salgılamayı tüpten kana geçiş olarak yorumlamak.',
 metin='Şekilde bir nefron ve çevresindeki kılcal damarlar gösterilmiş; maddelerin geçiş yönleri 1, 2 ve 3 numaralı oklarla belirtilmiştir.\nBuna göre, bu geçişlerle ilgili,\nI. 1 numaralı geçiş, ATP harcanarak taşıyıcı proteinlerle gerçekleşir.\nII. 2 numaralı geçişle kana alınan maddeler arasında glikoz da vardır.\nIII. 3 numaralı geçiş kan pH’sının dengelenmesine katkı sağlar.\nifadelerinden hangileri doğrudur?',
 istenen='Doğru olan öncüllerin hangileri olduğu.',ip=['Okların yönüne bakarak her geçişin süzülme, geri emilim ya da salgılamadan hangisi olduğunu belirle.'],
 bilgi=[B('Üç temel olay','süzülme glomerulustan Bowman kapsülüne, geri emilim tüpten kılcal damara, salgılama kılcal damardan tüpe doğru madde geçişidir')],
 puf='Önce okun başlangıç ve bitiş noktasına bakıp olayı adlandır; sonra enerji gereksinimini düşün.',sekil=sekil_nef2())
# ---------- 11 · üre molekülünün yolu · orta ----------
NM={'kapsül':'III','proksimal':'V','inen':'I','çıkan':'VI','distal':'II','toplama':'IV'}
def seq(l): return ' - '.join(NM[x] for x in l)
YOL=['kapsül','proksimal','inen','çıkan','distal','toplama']
dog11=seq(YOL)
w11=[(['kapsül','proksimal','çıkan','inen','distal','toplama'],'Sıvı Henle kulpunun önce inen koluna, sonra çıkan koluna geçer; bu dizide bu iki kısım ters yazılmıştır.'),
     (['kapsül','inen','proksimal','çıkan','distal','toplama'],'Süzüntü Bowman kapsülünden sonra önce proksimal tüpe geçer; bu dizide Henle kulpunun inen kolu proksimal tüpten önce yazılmıştır.'),
     (['kapsül','proksimal','inen','çıkan','toplama','distal'],'Süzüntü toplama kanalına girmeden önce distal tüpten geçer; bu dizide bu iki kısım yer değiştirmiştir.'),
     (['proksimal','kapsül','inen','çıkan','distal','toplama'],'Süzüntü proksimal tüpe Bowman kapsülünden geçerek ulaşır; bu dizide ilk iki kısım ters yazılmıştır.')]
q(11,*T_YAPI,'orta','Nefron','Süzüntünün nefron kısımlarından geçiş sırasını belirler.','şekilli','nefron şeması, süzüntünün yolu','süzüntünün nefronda izlediği yol',
 'Süzüntü Bowman kapsülünden proksimal tüpe, Henle kulpunun inen ve çıkan koluna, distal tüpe ve toplama kanalına sırayla geçer; bu sıra değişmez.','Henle kulpunun inen ve çıkan kollarını karıştırmak; distal tüp ile toplama kanalının sırasını ters almak.',
 [A('Kısımları tanı','III Bowman kapsülü, V proksimal tüp, I Henle kulpunun inen kolu, VI çıkan kolu, II distal tüp, IV toplama kanalıdır.','III: kapsül · V: proksimal · I: inen kol · VI: çıkan kol · II: distal · IV: toplama'),
  A('Süzüntünün yolunu kur','Üre süzülür, geri emilmeden tüp boyunca ilerleyerek idrara karışır; sıra kapsülden toplama kanalına doğrudur.','Kapsül → proksimal → inen → çıkan → distal → toplama'),
  A('Dizinin numaralarını yaz','Bu sıranın numaraları, şekildeki gösterime göre yazılır.',dog11)],
 metin='Şekilde bir nefronun kısımları I, II, III, IV, V ve VI ile numaralandırılmıştır. Glomerulustan Bowman kapsülüne süzülen bir üre molekülü, nefron tüplerinde hiç geri emilmeden idrarla atılmaktadır.\nBuna göre, bu üre molekülü numaralı yapılardan hangi sırayla geçmiştir?',
 dogru=dog11,sira=yer('D',dog11,[seq(w[0]) for w in w11]),yan=[(seq(a),b,'bilgi') for a,b in w11],istenen='Üre molekülünün yapılardan geçiş sırası.',ip=['Süzüntünün Bowman kapsülünden idrar çıkışına kadar tüp boyunca ilerleme sırasını izle.'],
 bilgi=[B('Süzüntünün yolu','süzüntü nefron tüplerinde ilerlerken geri emilim ve salgılama ile içeriği değişir, sonunda toplama kanalıyla havuzcuğa ulaşır')],
 puf='Tüpü kapsülden başlayıp toplama kanalına kadar parça parça izle; U biçimli kısımda önce inen kol gelir.',sekil=sekil_nef3())
# ---------- 12 · geri emilen miktar · orta · sayısal ----------
T12={'K':(180,0),'L':(54,27),'M':(600,6)}
GE={k:v[0]-v[1] for k,v in T12.items()}; toplam=sum(GE.values()); assert toplam==801 and sum(v[1] for v in T12.values())==33 and sum(v[0] for v in T12.values())==834 and GE['K']+GE['L']==207 and GE['M']==594
SK12=tablo_svg(['Madde','Süzülen (g/gün)','İdrarla atılan (g/gün)'],[[k,*T12[k]] for k in 'KLM'])
q(12,*T_TABLO,'orta','Geri emilim hesabı','Süzülen ve atılan miktarlardan geri emilen miktarı hesaplar.','tablo','süzülen ve atılan miktar tablosu','süzülen ve atılan miktarlardan geri emilim',
 'Salgılama olmayan bir maddede geri emilen miktar, süzülen miktardan idrarla atılan miktar çıkarılarak bulunur.','Atılan miktarı geri emilen miktar sanmak; yalnız tek maddeyi hesaba katmak.',
 [A('Her maddede farkı al','Salgılama olmadığı için geri emilen miktar, süzülenle atılanın farkıdır.','Geri emilen = süzülen − atılan'),
  A('K, L ve M için hesapla','Tablodaki değerler farkta yerine konur.','K: 180 − 0 = 180 · L: 54 − 27 = 27 · M: 600 − 6 = 594'),
  A('Toplamı bul','Üç maddenin geri emilen miktarları toplanır.','180 + 27 + 594 = 801 g')],
 metin='Tabloda, sağlıklı bir bireyin böbreklerinde bir günde süzülen K, L ve M maddelerinin miktarları ile bu maddelerin idrarla atılan miktarları verilmiştir. Bu maddelerin hiçbiri nefron tüplerine salgılanmamaktadır.\nBuna göre, bu bireyde bir günde nefron tüplerinden kana geri emilen K, L ve M maddelerinin toplam miktarı kaç gramdır?',
 dogru=801,yan=[(33,'Atılan miktarların toplamı (0 + 27 + 6 = 33 g) alınmış; oysa geri emilen miktar, süzülenden atılanı çıkararak bulunur.','islem'),
  (207,'Yalnız K ve L maddelerinin geri emilen miktarları (180 + 27 = 207 g) toplanmış, M maddesi hesaba katılmamıştır.','islem'),
  (594,'Yalnız M maddesinin geri emilen miktarı (600 − 6 = 594 g) alınmış, K ve L maddeleri eklenmemiştir.','islem'),
  (834,'Süzülen miktarların toplamı (180 + 54 + 600 = 834 g) alınmış, idrarla atılan miktarlar çıkarılmamıştır.','islem')],
 istenen='Geri emilen maddelerin toplam miktarı (g).',ip=['Salgılama olmadığında geri emilen miktarı süzülen ve atılan miktarlar arasındaki ilişkiden bul.'],
 bilgi=[B('Madde bilançosu','süzülen miktar, geri emilen ve idrarla atılan miktarların toplamına eşittir; salgılama varsa atılan miktara salgılanan eklenir')],
 puf='Her madde için süzülenden atılanı çıkar, sonra üç farkı topla.',sekil=SK12)
# ---------- 13 · glikoz taşıma kapasitesi · zor · sayısal ----------
PL,GFR,TM=300,120,300   # mg/100 mL, mL/dk, mg/dk
suz=Fr(PL,100)*GFR; assert suz==360; at_dk=suz-TM; assert at_dk==60; saat=at_dk*60; assert saat==3600 and suz*60==21600 and TM*60==18000
q(13,*T_TABLO,'zor','Glikoz geri emilimi','Süzülen glikoz miktarını ve taşıma kapasitesini birlikte kullanarak idrarla atılan miktarı hesaplar.','düz','glikoz taşıma kapasitesi hesabı','glikoz süzülmesi ve en yüksek geri emilim hızı',
 'Süzülen glikoz, plazma derişimi ile süzülme hızının çarpımıdır; proksimal tüp en çok kapasitesi kadar glikoz geri emebilir, aşan kısım idrarla atılır.','Süzülen miktarı kapasiteyle karşılaştırmadan fazlalığı yok saymak; geri emilimi hesaba katmadan süzülen miktarı atılan saymak.',
 [A('Süzülen glikozu bul','Dakikada süzülen glikoz, plazma derişimi (mg/mL) ile süzülme hızının çarpımıdır.','3 mg/mL × 120 mL/dk = 360 mg/dk'),
  A('Kapasiteyle karşılaştır','Proksimal tüp dakikada en çok 300 mg geri emebilir; fazlası tüpte kalır.','360 > 300'),
  A('Dakikada atılanı bul','Geri emilemeyen miktar idrarla atılır.','360 − 300 = 60 mg/dk'),
  A('Bir saate çevir','Bir saat 60 dakikadır.','60 × 60 = 3600 mg')],
 metin='Plazma glikoz derişimi 300 mg/100 mL olan bir bireyde glomerulustan dakikada 120 mL süzüntü Bowman kapsülüne geçmektedir. Glikoz süzüntüde plazmadakiyle aynı derişimdedir ve proksimal tüp hücreleri glikozu dakikada en çok 300 mg hızla geri emebilmektedir. Salgılanma olmamaktadır.\nBuna göre, bu birey bir saatte idrarıyla kaç mg glikoz atar?',
 dogru=3600,yan=[(0,'Plazma derişimi (300 mg/100 mL) ile kapasite (300 mg/dk) sayısal olarak aynı olduğundan fazlalık olmadığı sanılmış; oysa süzülen glikoz 360 mg/dk olduğundan 60 mg/dk geri emilemez.','dikkat'),
  (60,'Dakikada atılan miktar (360 − 300 = 60 mg) bulunmuş ama bir saate çevrilmemiştir.','islem'),
  (18000,'Geri emilen miktar (300 × 60 = 18000 mg) alınmış; istenen idrarla atılan miktardır.','islem'),
  (21600,'Süzülen glikozun tamamı (360 × 60 = 21600 mg) atılmış sayılmış, geri emilim hesaba katılmamıştır.','islem')],
 istenen='Bir saatte idrarla atılan glikoz miktarı (mg).',ip=['Önce dakikada süzülen glikoz miktarını bul ve proksimal tüpün geri emilim kapasitesiyle karşılaştır.'],
 bilgi=[B('Geri emilim kapasitesi','taşıyıcı proteinlerin sayısı sınırlıdır; süzülen glikoz bu kapasiteyi aşarsa aşan kısım geri emilemez ve idrara geçer')],
 puf='Atılan, süzülen ile kapasite arasındaki farktır; hız birimini saate çevirmeyi unutma.')
# ---------- 14 · atardamar–toplardamar · orta ----------
assert G14['K'][1]<G14['K'][0] and G14['L'][0]==G14['L'][1] and G14['M'][1]>G14['M'][0]
GER={'K':('Üre','Derişimi azalan K maddesi üredir; üre glomerulustan süzülerek idrarla atıldığı için böbrek toplardamarında azalır.'),
     'L':('Plazma proteini','Derişimi değişmeyen L maddesi plazma proteinidir; proteinler süzülmediği için toplardamarda da atardamardaki düzeyde kalır.'),
     'M':('Karbondioksit','Derişimi artan M maddesi karbondioksittir; böbrek hücrelerinin solunumunda üretilir ve toplardamara geçer.')}
def perm(p): return ' – '.join(p)
dog14=perm([GER[k][0] for k in 'KLM'])
def yan14(p):
    yanl=[k for k,n in zip('KLM',p) if n!=GER[k][0]]; assert yanl
    return ' '.join(f'{k} maddesi {p["KLM".index(k)]} olarak yazılmış. {GER[k][1]}' for k in yanl)
ps=[('Karbondioksit','Üre','Plazma proteini'),('Plazma proteini','Karbondioksit','Üre'),('Plazma proteini','Üre','Karbondioksit'),('Üre','Karbondioksit','Plazma proteini')]
q(14,*T_TABLO,'orta','Böbrek dolaşımı','Böbrek atardamarı ve toplardamarındaki madde derişimi değişimini yorumlar.','grafik','böbrek atardamarı ve toplardamarı çubuk grafiği','böbrek atardamarı ve toplardamarında derişim farkı',
 'Böbrek toplardamarında üre atardamara göre azdır, plazma proteini aynı kalır, karbondioksit artar; çünkü üre süzülür, proteinler süzülmez ve böbrek hücreleri solunum yapar.','Derişimi değişmeyen maddeyi üre sanmak; karbondioksiti toplardamarda azalan saymak.',
 [A('Grafiği oku','K 100’den 80’e düşer, L 100’de kalır, M 100’den 108’e çıkar.','K: ↓ · L: = · M: ↑'),
  A('Azalan maddeyi bul','Böbrekte süzülüp idrarla atılan ve kandan uzaklaşan madde ürenin derişimini azaltır.','K → üre'),
  A('Değişmeyeni ve artanı bul','Proteinler süzülmediğinden L aynı kalır; böbrek hücreleri CO₂ ürettiğinden M artar.','L → plazma proteini · M → karbondioksit'),
  A('Diziyi yaz','Sıra K, L, M şeklindedir.','Üre – Plazma proteini – Karbondioksit')],
 metin='Grafikte, böbrek atardamarı ve böbrek toplardamarındaki kanda bulunan K, L ve M maddelerinin bağıl derişimleri gösterilmiştir. K, L ve M maddeleri sırasıyla üre, plazma proteini ve karbondioksit ya da bunların farklı bir sıralamasıdır.\nBuna göre, K, L ve M maddeleri sırasıyla aşağıdakilerin hangisinde doğru verilmiştir?',
 dogru=dog14,sira=[perm(p) for p in ps]+[dog14],yan=[(perm(p),yan14(p),'bilgi') for p in ps],
 istenen='K, L ve M maddelerinin sırasıyla adları.',ip=['Hangi maddenin süzülüp atıldığını, hangisinin süzülmediğini ve hangisinin böbrek hücrelerince üretildiğini düşün.'],
 bilgi=[B('Böbrek dolaşımı','böbrek atardamarıyla gelen kanın bir kısmı süzülür; toplardamarla ayrılan kanın içeriği süzülen ve hücrelerce kullanılan ya da üretilen maddelere göre değişir')],
 puf='Süzülüp idrarla atılan madde azalır, süzülmeyen madde sabit kalır, üretilen madde artar.',sekil=sekil_g14())
# ---------- 15 · hemodiyaliz · orta · olumsuz ----------
S15y='Kandaki üre, diyaliz sıvısına ATP harcanarak aktif taşımayla geçer.'
S15b='Yarı geçirgen zar, alyuvarların diyaliz sıvısına geçmesini engeller.'
S15c='Üre, derişimi yüksek olan kandan derişimi düşük olan diyaliz sıvısına difüzyonla geçer.'
S15d='Kan ve diyaliz sıvısının zıt yönde akması, zarın iki yanındaki derişim farkının korunmasını sağlar.'
S15e='Diyaliz sıvısındaki glikoz derişimi kandakine eşit tutulduğu için kandan net glikoz kaybı olmaz.'
q(15,*T_SAGLIK,'orta','Diyaliz','Hemodiyaliz düzeneğinde madde geçişini ve nedenlerini yorumlar.','şekilli','hemodiyaliz düzeneği','hemodiyaliz düzeneği',
 'Hemodiyalizde madde geçişi yarı geçirgen zardan difüzyonla, derişimi yüksek tarafın düşük tarafa doğru olur; zar kan hücrelerini ve büyük molekülleri geçirmez.','Diyalizdeki geçişi aktif taşıma sanmak; diyaliz sıvısında glikozun bulunmasının nedenini yanlış yorumlamak.',
 [A('Düzeneği oku','Kan ve diyaliz sıvısı zıt yönde akar, aralarında yarı geçirgen zar vardır; kanda üre ve alyuvar bulunur, diyaliz sıvısında üre yoktur.','Üre: kanda çok, diyaliz sıvısında yok'),
  A('Madde geçişini yorumla','Üre derişimi yüksek taraftan düşük tarafa difüzyonla geçer; bu pasif bir olaydır ve ATP gerektirmez.','Üre: kan → diyaliz sıvısı, difüzyon'),
  A('Şıkları sına','Alyuvar engeli, zıt akışın etkisi ve glikoz dengesi ile ilgili ifadeler düzenekle uyumludur; aktif taşıma ifadesi uyumlu değildir.','Yanlış ifade: aktif taşıma'),
  A('Şıkkı seç','Yanlış olan ifade ürenin ATP harcanarak aktif taşımayla geçtiğini söyleyendir.','Cevap: bu ifade')],
 metin='Şekilde böbrek yetmezliği olan bir hastaya uygulanan hemodiyaliz düzeneği gösterilmiştir. Kan ve diyaliz sıvısı, yarı geçirgen bir zarın iki yanından zıt yönlerde akmaktadır. Diyaliz sıvısı başlangıçta üre içermemekte, glikoz derişimi ise kandakine eşit tutulmaktadır.\nBuna göre, aşağıdaki ifadelerden hangisi yanlıştır?',
 dogru=S15y,sira=yer('A',S15y,[S15b,S15c,S15d,S15e]),yan=[(S15b,'Zar alyuvarları geçirmeyecek kadar küçük gözeneklidir; ifade doğrudur ve düzenekle uyumludur.','bilgi'),
  (S15c,'Üre derişimi kanda yüksek, diyaliz sıvısında düşüktür; difüzyon bu yönde gerçekleşir, ifade doğrudur.','bilgi'),
  (S15d,'Zıt yönlü akış, zarın iki yanında derişim farkının korunmasını sağlayarak geçişi hızlandırır; ifade doğrudur.','bilgi'),
  (S15e,'Derişimler eşit olduğunda glikozun net geçişi olmaz; ifade doğrudur.','bilgi')],
 istenen='Yanlış olan ifade.',ip=['Zar boyunca madde geçişinin hangi tür taşıma ile ve hangi derişim farkıyla gerçekleştiğini düşün.'],
 bilgi=[B('Hemodiyaliz','işlevini yitiren böbreğin yerine kandaki atıkları yarı geçirgen zar aracılığıyla diyaliz sıvısına aktaran yapay temizleme yöntemidir')],
 puf='Madde geçişinin yönünü ve enerji gereksinimini şıklarda ayrı ayrı sına.',sekil=sekil_diyaliz())
# ---------- 16 · ADH ve aldosteron birlikte · zor · öncüllü ----------
d16={'I':(True,'Kan plazmasının ozmotik derişimi arttığında ADH salgısı artar; ADH toplama kanalında geri emilen su miktarını artırarak idrarın ozmotik derişimini yükseltir.'),
     'II':(False,'Kan hacminin azalması aldosteron salgısını artırır; aldosteron distal tüpte Na⁺ geri emilimini artırır.'),
     'III':(False,'ADH ve aldosteronun etkisiyle idrarla atılan su ve Na⁺ miktarı azalır.')}
r=onc(d16,'A')
qo(16,r,*T_HORMON,'zor','ADH ve aldosteron','Su kaybı ve kan basıncı düşmesi durumunda ADH ile aldosteronun birlikte etkilerini neden–sonuç zinciriyle değerlendirir.','su kaybında ADH ve aldosteron','çok terleyen bireyde ADH ve aldosteron',
 'Plazma ozmotik derişimi artınca ADH salgısı artar ve su geri emilimi yükselir; kan hacmi ve basıncı düşünce aldosteron artar, Na⁺ geri emilimini ve K⁺ salgısını yükseltir.','Aldosteron salgısının kan hacmi azalınca azaldığını düşünmek; ADH’nin plazma derişimi artınca azaldığını sanmak.',
 metin='Sıcak havada uzun süre su içmeden çalışan ve çok terleyen bir kişide kan hacmi ve kan basıncı azalmakta, kan plazmasının ozmotik derişimi artmaktadır.\nBuna göre, bu kişide,\nI. Plazma ozmotik derişiminin artması ADH salgısını artırır; bu durum toplama kanalında geri emilen su miktarını artırarak idrarın ozmotik derişimini yükseltir.\nII. Kan hacminin azalması aldosteron salgısını azaltır; bu durum distal tüpte Na⁺ geri emilimini azaltır.\nIII. ADH ve aldosteronun etkisiyle idrarla atılan su ve Na⁺ miktarı artar.\nifadelerinden hangileri doğrudur?',
 istenen='Doğru olan öncüllerin hangileri olduğu.',ip=['Plazma derişimi ve kan hacmindeki değişimin her bir hormonun salgısını hangi yönde etkilediğini ayrı ayrı düşün.'],
 bilgi=[B('Su-tuz dengesi','kan plazmasının ozmotik derişimi ve kan hacmi, ADH ile aldosteronun salgılanmasını denetler; her iki hormon nefron tüplerinin geri emilim yeteneğini değiştirir')],
 puf='Her öncülde önce neden–sonuç zincirinin her halkasını ayrı ayrı sına.')
# ---------- 17 · nefronda olaylar · orta · olumsuz ----------
S17y='Üre gibi azotlu atıkların tamamı proksimal tüpte geri emilir ve idrarla atılmaz.'
S17a='Süzülme, kan basıncının etkisiyle ve molekül büyüklüğüne bağlı olarak gerçekleşir.'
S17c='Proksimal tüpte glikoz ve amino asitler, taşıyıcı proteinlerle ATP harcanarak geri emilir.'
S17d='Distal tüpte H⁺ ve K⁺ iyonları, kandan tüp içine salgılanır.'
S17e='Toplama kanalında ADH etkisiyle su geri emilimi artar.'
q(17,*T_SUREC,'orta','İdrar oluşumu','Nefronda süzülme, geri emilim ve salgılama olaylarını mekanizmalarıyla değerlendirir.','düz','idrar oluşumunun basamakları','nefronda idrar oluşumu',
 'Süzülme pasiftir, besin maddelerinin geri emilimi aktif taşımayla proksimal tüpte olur, H⁺ ve K⁺ distal tüpte salgılanır; üre ise kısmen geri emilir ve idrarla atılır.','Azotlu atıkların tamamen geri emildiğini düşünmek; süzülmeyi aktif saymak.',
 [A('Olayları hatırla','Süzülme glomerulusta pasif, glikoz ve amino asit geri emilimi proksimal tüpte aktif, salgılama distal tüpte, su geri emilimi toplama kanalında ADH ile olur.','Süzülme: pasif · Besin geri emilimi: aktif · Salgılama: distal tüp · Su: toplama kanalı + ADH'),
  A('Şıkları sına','Dört ifade bu bilgilerle uyumludur.','Doğru: süzülme, glikoz, salgılama, ADH'),
  A('Hatalı olanı bul','Azotlu atıklar, üre gibi, idrarla atılır; hepsi geri emilseydi vücutta birikirdi.','Üre kısmen geri emilir, idrarla atılır'),
  A('Şıkkı seç','Yanlış olan ifade azotlu atıkların tamamının geri emildiğini söyleyendir.','Cevap: bu ifade')],
 metin='Nefronda idrar oluşumu süzülme, geri emilim ve salgılama olaylarıyla gerçekleşir. Bu olaylarda madde geçişi hem pasif hem de aktif mekanizmalarla yapılır ve nefronun farklı kısımlarında farklı maddeler işlem görür.\nBuna göre, nefrondaki olaylarla ilgili aşağıdaki ifadelerden hangisi yanlıştır?',
 dogru=S17y,sira=yer('B',S17y,[S17a,S17c,S17d,S17e]),yan=[(S17a,'Glomerulusta süzülme kan basıncıyla ve molekül büyüklüğüne bağlı olarak gerçekleşir; ifade doğrudur.','bilgi'),
  (S17c,'Glikoz ve amino asitlerin geri emilimi proksimal tüpte taşıyıcı proteinlerle ve ATP harcanarak yapılır; ifade doğrudur.','bilgi'),
  (S17d,'Distal tüpte H⁺ ve K⁺ iyonları kandan tüpe salgılanır; ifade doğrudur.','bilgi'),
  (S17e,'ADH toplama kanalının suya geçirgenliğini artırır ve su geri emilimi yükselir; ifade doğrudur.','bilgi')],
 istenen='Yanlış olan ifade.',ip=['Azotlu atıkların idrarla atılıp atılmadığını ve her nefron kısmında hangi olayın gerçekleştiğini düşün.'],
 bilgi=[B('İdrar oluşumu','süzülme, geri emilim ve salgılama sonucunda su, üre ve bazı iyonlar içeren idrar oluşur; glikoz, amino asit ve proteinler sağlıklı bireyin idrarında bulunmaz')],
 puf='Her ifadeyi nefronun ilgili kısmıyla eşleştirip tek tek sına.')
# ---------- 18 · diyabet ve idrar · zor · öncüllü ----------
d18={'I':(True,'İdrarda glikoz bulunması, proksimal tüpteki taşıyıcı proteinlerin geri emilim kapasitesinin aşıldığını gösterir.'),
     'II':(True,'Tüpte kalan glikoz, tüp sıvısının ozmotik derişimini artırır ve suyun geri emilimini azaltır.'),
     'III':(False,'Bu bireyde plazma ozmotik derişimi arttığı için ADH salgısı artar; idrar miktarındaki artış ADH eksikliğine bağlı değildir.')}
r=onc(d18,'D')
qo(18,r,*T_SAGLIK,'zor','Diyabet','Yüksek kan glikozunun nefrondaki sonuçlarını ADH etkisiyle birlikte zincirleme yorumlar.','diyabette idrarda glikoz ve idrar miktarı','kontrolsüz diyabette nefron ve idrar',
 'Kan glikozu yüksekse süzülen glikoz geri emilim kapasitesini aşar ve tüpte kalan glikoz suyu tutar; bu durumda ADH düzeyi ile idrar miktarı birbirinden bağımsız değerlendirilmelidir.','İdrar miktarının artışını ADH eksikliğine bağlamak; idrarda glikozu süzülme bozukluğuna bağlamak.',
 metin='Kan glikoz düzeyi kontrolsüz biçimde yüksek olan bir bireyin idrarında glikoz bulunmakta ve bu birey sık idrara çıkmaktadır. Bireyin glomerulus süzme işlevi sağlıklıdır ve kan plazmasının ozmotik derişimi yükselmiştir.\nBuna göre,\nI. İdrarda glikoz bulunması, proksimal tüpteki taşıyıcı proteinlerin glikoz geri emilim kapasitesinin aşıldığını gösterir.\nII. Tüpte kalan glikoz, tüp sıvısının ozmotik derişimini artırarak suyun geri emilimini azaltır.\nIII. İdrar miktarındaki artış, bu bireyde ADH salgısının azalmasıyla açıklanır.\nifadelerinden hangileri doğrudur?',
 istenen='Doğru olan öncüllerin hangileri olduğu.',ip=['Süzülen glikoz miktarı arttığında geri emilimin, tüp sıvısının derişiminin ve ADH etkisinin nasıl değiştiğini sırayla düşün.'],
 bilgi=[B('Glikozun geri emilimi','glikoz proksimal tüpte taşıyıcı proteinlerle geri emilir; taşıyıcıların sayısı sınırlı olduğundan süzülen miktar belirli bir değeri aşarsa fazlası idrara geçer')],
 puf='Her öncülde olayın nedenini ve sonucunu ayrı ayrı sına.')
# ---------- 19 · glomerulus hasarı ve ödem · zor · öncüllü ----------
d19={'I':(False,'Albümin kaybı, kan plazmasının ozmotik basıncını azaltır; bu da kılcal damardan doku sıvısına su geçişini artırır.'),
     'II':(False,'Alyuvarların idrarda bulunması, süzme yüzeyinin geçirgenliğinin arttığını gösterir.'),
     'III':(True,'Plazma proteinlerinin idrarla kaybı plazmanın ozmotik basıncını azaltır; doku sıvısında su birikmesi ödeme yol açar.')}
r=onc(d19,'B')
qo(19,r,*T_SAGLIK,'zor','Glomerulus hasarı','Süzme yüzeyi hasarının idrar içeriğine ve doku sıvısı dengesine etkisini birlikte yorumlar.','glomerulus hasarı, albümin kaybı ve ödem','glomerulus hasarı ve ödem',
 'Süzme yüzeyi zarar görünce proteinler ve alyuvarlar idrara geçer; plazma proteinleri azalınca kılcal damarlarda ozmotik basınç düşer ve doku sıvısı artarak ödem oluşur.','Süzme yüzeyi hasarını geçirgenlik azalması saymak; protein kaybında plazma ozmotik basıncının arttığını düşünmek.',
 metin='Glomerulus kılcal damarlarında hasar bulunan bir bireyin idrarında albümin ve alyuvarlar saptanmış, bacaklarında ise ödem gözlenmiştir.\nBuna göre bu bireyle ilgili,\nI. Albümin kaybı, kan plazmasının ozmotik basıncını artırarak kılcal damardan doku sıvısına su geçişini artırır.\nII. Alyuvarların idrarda bulunması, süzme yüzeyinin geçirgenliğinin azaldığını gösterir.\nIII. Plazma proteinlerinin idrarla kaybı plazmanın ozmotik basıncını azaltır ve doku sıvısında su birikmesi ödeme yol açar.\nifadelerinden hangileri doğrudur?',
 istenen='Doğru olan öncüllerin hangileri olduğu.',ip=['Albümin kaybının plazma ozmotik basıncını ve süzme yüzeyinin geçirgenliğini nasıl etkilediğini ayrı ayrı düşün.'],
 bilgi=[B('Doku sıvısı ve ödem','doku sıvısı kılcal damardan sızan plazmanın bir kısmıdır; sızan sıvı miktarı kan plazmasının ozmotik basıncına bağlıdır ve doku sıvısının aşırı artması ödeme yol açar')],
 puf='Her öncülde olayın nedenini ve sonucunu ayrı ayrı sına.')
# ---------- 20 · canlılarda boşaltım · orta · öncüllü ----------
d20={'I':(True,'Planaryada boşaltım alev hücreleri aracılığıyla yapılır.'),
     'II':(True,'Yağmur solucanında halkalarda çift hâlinde bulunan nefridyumlar boşaltımı sağlar.'),
     'III':(False,'Böceklerde Malpighi tüpleri, boşaltım ürünlerini sindirim kanalına boşaltır; doğrudan vücut dışına boşaltmaz.')}
r=onc(d20,'B')
qo(20,r,*T_DIGER,'orta','Canlılarda boşaltım','Omurgasız canlı gruplarında boşaltım yapılarını eşleştirir.','canlılarda boşaltım yapıları','omurgasızlarda boşaltım organları',
 'Omurgasız gruplarında boşaltım yapıları ve ürünlerin boşaltıldığı yer gruba özgüdür.','Boşaltım yapılarını ve ürünlerin boşaltıldığı yeri gruplarla karıştırmak.',
 metin='Canlı gruplarında boşaltım, metabolizma artıklarının vücuttan uzaklaştırılmasını sağlayan farklı yapılarla gerçekleştirilir.\nBuna göre,\nI. Planaryada boşaltım, alev hücreleri aracılığıyla yapılır.\nII. Yağmur solucanında halkalarda çift hâlinde bulunan nefridyumlar boşaltımı sağlar.\nIII. Böceklerde Malpighi tüpleri, boşaltım ürünlerini doğrudan vücut dışına boşaltır.\nifadelerinden hangileri doğrudur?',
 istenen='Doğru olan öncüllerin hangileri olduğu.',ip=['Her canlı grubunun boşaltım yapısını ve bu yapının ürününü nereye ilettiğini hatırla.'],
 bilgi=[B('Boşaltım','metabolizma artıklarının vücuttan uzaklaştırılmasıdır; omurgasız grupları bu işi böbrekten farklı yapılarla gerçekleştirir')],
 puf='Her öncülde yapı ile canlı grubunu eşleştir; ürünün gittiği yeri de kontrol et.')
# ================= yaz =================
def bitir_ab():
    for qq in P.ANA: qq['kardes']=None
    P.yaz(os.path.join(GD,'bosaltim-1.json'),'/tmp/bos-bosaltim.json')
    tipler={}
    for c in KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=KK))['kartlar'].append(c['id'])
    json.dump(dict(konu=KONUAD,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2018–2026 Biyoloji (yalnız mantık), MEB 11. sınıf biyoloji müfredatı.',kartlar=KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar','abbosaltim.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler))
bitir_ab()
