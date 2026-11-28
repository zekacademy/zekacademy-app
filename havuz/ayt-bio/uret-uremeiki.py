"""AYT Biyoloji · Üreme Sistemi ve Embriyonik Gelişim · 2. dalga · 10 soru. Sayılar Python'da hesaplanır, öncüllerin doğru/yanlış değeri tek yerde tutulur. Şekiller TikZ/pgfplots (cizim.tikz_svg)."""
import sys,os,json,math,itertools
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-bio')); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
import _hafif_bio as H
from _hafif_bio import *
from cizim import tikz_svg
import gorsel as G
KONU='Üreme Sistemi ve Embriyonik Gelişim'; H.KONU=KONU
P=Parti('uremeiki',KONU,'abio|'+KONU,ders='AYT Biyoloji',idon='aytbio')
KY='ÖSYM AYT 2018–2026 Biyoloji (Üreme Sistemi ve Embriyonik Gelişim) soruları (yalnız mantık) · MEB 11–12. sınıf biyoloji'
TIPAD={'uk-embriyo':'Embriyonik gelişim evreleri ve tabakalar','uk-hormon':'Üreme hormonları ve geri bildirim','uk-gamet':'Gametogenez ve kromozom dağılımı','uk-disi':'Dişi üreme sistemi ve yumurtalık döngüsü','uk-saglik':'Üreme sağlığı ve doğum kontrolü'}
NK=[0]
def Q(tipId,z,alt,fikir,tuzak,kalip,metin,istenen,ip,bilgi,ad,puf,sekil=None,dogru=None,yan=None,sira=None,kaz=None,kisa=None):
    tip=TIPAD[tipId]; NK[0]+=1; n=NK[0]; no=f'{n:04d}'; kid=f'K-ABUR2-{n:02d}'
    assert 3<=len(ad)<=7
    kart(kid,alt,fikir,tuzak,z,kalip,len(ad),tipId,tip,KY)
    mk(P,no,ad=ad,adim=len(ad),tipId=tipId,tip=tip,z=z,alt=alt,kaz=kaz or alt+' konusunda yorum yapar.',kart=f'{kid} ({alt}) · özgün kurgu',kalip=kalip,
       metin=metin,dogru=dogru,yan=yan,istenen=istenen,ip=[ip],bilgi=bilgi,puf=puf,sekil=sekil,sira=sira,kisa=kisa)
RM=['I','II','III']
OS=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
OSET={'Yalnız I':{0},'Yalnız II':{1},'Yalnız III':{2},'I ve II':{0,1},'I ve III':{0,2},'II ve III':{1,2},'I, II ve III':{0,1,2}}
def onc(truth,neden,harf,yanlis_sor=False):
    """truth: 3 bool; neden: her öncülün neden doğru/yanlış olduğunu anlatan cümle parçası; harf: doğru şık konumu."""
    T={i for i in range(3) if truth[i]}
    anahtar={i for i in range(3) if not truth[i]} if yanlis_sor else T
    dog=[s for s in OS if OSET[s]==anahtar]; assert len(dog)==1; dog=dog[0]; p='ABCDE'.index(harf); ix=OS.index(dog)
    for comb in itertools.combinations(range(7),5):
        if ix in comb and comb.index(ix)==p: sec=[OS[j] for j in comb]; break
    else: raise AssertionError(('şık konumu mümkün değil',dog,harf))
    yan=[]
    for s_ in sec:
        if s_==dog: continue
        S_=OSET[s_]; parca=[]
        for i in sorted(S_^anahtar):
            sanilan=(i in S_) if not yanlis_sor else (i not in S_)
            assert sanilan!=truth[i]
            parca.append(f'{RM[i]}. öncülü '+('doğru' if sanilan else 'yanlış')+f' sanmış; oysa {neden[i]}.')
        yan.append((s_,' '.join(parca),'bilgi'))
    return dog,yan,sec
def oadim(truth,neden):
    return [A(f'{RM[i]}. öncülü incele',neden[i][0].upper()+neden[i][1:]+'.',f'{RM[i]}: '+('doğru' if truth[i] else 'yanlış')) for i in range(3)]
def etiket_oncul(a,b_,c): return f'I. {a}\nII. {b_}\nIII. {c}\n'
def yer(dogru,digerler,harf):
    i='ABCDE'.index(harf); d=list(digerler); assert len(d)==4
    return d[:i]+[dogru]+d[i:]
def tk(body,scale=1.0): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small,scale=%s]\n%s\n\\end{tikzpicture}'%(scale,body))
def sayi(x,y,n,extra=''):
    return f'\\node[circle,draw,inner sep=1.3pt,fill=white,font=\\small\\bfseries{extra}] at ({x:.2f},{y:.2f}) {{{n}}};'
def pgf(govde,w='7cm',h='5.4cm',ek=''):
    return tikz_svg('\\begin{tikzpicture}[font=\\small]\n\\begin{axis}[width='+w+',height='+h+',tick label style={font=\\small},label style={font=\\small},'+ek+']\n'+govde+'\n\\end{axis}\n\\end{tikzpicture}')
def tab(bas,sat,cw=6.3,ilk_kalin=True):
    """Tablo SVG'si; yazı 11 px, sütun genişliği içeriğe göre."""
    n=len(bas); assert all(len(r)==n for r in sat)
    gen=[int(cw*max(len(str(x)) for x in [bas[j]]+[r[j] for r in sat])+22) for j in range(n)]
    W=sum(gen)+4; assert W<=500,('tablo çok geniş',W); h=27; Hh=h*(len(sat)+1)+4; b=[]; xs=[2]
    for g in gen: xs.append(xs[-1]+g)
    b.append(f'<rect x="2" y="2" width="{W-4}" height="{h}" style="fill:currentColor;stroke:none" fill-opacity=".08"/>')
    for j,s in enumerate(bas): b.append(G._t((xs[j]+xs[j+1])/2,2+h/2+4,str(s),size=11.5,bold=True))
    for i,row in enumerate(sat):
        y=2+h*(i+1)
        for j,s in enumerate(row): b.append(G._t((xs[j]+xs[j+1])/2,y+h/2+4,str(s),size=11.5,bold=(j==0 and ilk_kalin)))
    for i in range(len(sat)+2): b.append(f'<line x1="2" y1="{2+h*i}" x2="{W-2}" y2="{2+h*i}" stroke-width="{1.4 if i in (0,1,len(sat)+1) else 1}"/>')
    for x in xs: b.append(f'<line x1="{x}" y1="2" x2="{x}" y2="{2+h*(len(sat)+1)}" stroke-width="1"/>')
    return G._svg(W,Hh,''.join(b))

# =============== kromozom çizimi (2n=4: bir uzun, bir kısa homolog çifti) ===============
# =============== ŞEKİLLER ===============
def sek_norula(N):
    b=[]
    b.append('\\draw[line width=2.4pt,fill=white] (0,0) ellipse (3.1 and 2.1);')
    b.append('\\draw[line width=1.6pt,fill=cyan!15] (0,.95) circle (.55);\\draw[line width=1.1pt,fill=white] (0,.95) circle (.2);')
    b.append('\\draw[line width=1.2pt,fill=gray!45] (0,.1) circle (.24);')
    for sg in (-1,1): b.append(f'\\draw[line width=1.3pt,fill=pink!35] ({sg*1.35:.2f},.45) ellipse (.6 and .42);')
    b.append('\\draw[line width=1.6pt,fill=lime!22] (0,-.95) ellipse (.95 and .55);\\draw[line width=1.1pt,fill=white] (0,-.95) ellipse (.45 and .22);')
    b.append(f'\\draw[line width=1pt] (-1.9,2.55)--(-.45,1.2);'+sayi(-2.0,2.7,N['sinir']))
    b.append(f'\\draw[line width=1pt] (.95,-.02)--(.28,.07);'+sayi(1.15,-.04,N['noto']))
    b.append(f'\\draw[line width=1pt] (-4.1,-1.5)--(-.8,-1.0);'+sayi(-4.3,-1.6,N['bag']))
    b.append(f'\\draw[line width=1pt] (4.0,1.6)--(1.8,.7);'+sayi(4.2,1.75,N['somit']))
    b.append(f'\\draw[line width=1pt] (-4.1,.6)--(-3.0,.35);'+sayi(-4.3,.65,N['dis']))
    return tk('\n'.join(b),.85)
def sek_tubul(N):
    b=[]
    b.append('\\draw[line width=2pt,fill=vurgu!6] (-3.7,0)--(-3.7,4.7)--(3.7,4.7)--(3.7,0)--cycle;')
    b.append('\\draw[line width=1pt,fill=white] (-3.0,3.7) rectangle (3.0,4.6);\\node[font=\\small] at (.0,4.15) {Tübül boşluğu};')
    b.append('\\draw[line width=2.4pt] (-3.9,0)--(3.9,0);')
    # 1 spermatogonyum
    b.append('\\draw[line width=1.3pt,fill=cyan!15] (-2.7,.5) circle (.34);\\draw[line width=1.3pt] (-2.82,.45)--(-2.62,.58) (-2.78,.62)--(-2.58,.42);')
    # 2 birincil spermatosit
    b.append('\\draw[line width=1.3pt,fill=cyan!25] (-.95,1.35) circle (.58);\\foreach \\a in {-.2,0,.2}{\\draw[line width=1.4pt] (-.95+\\a,1.12)--(-.95+\\a,1.62);}')
    # 3 spermatit
    b.append('\\draw[line width=1.3pt,fill=cyan!15] (.85,2.2) circle (.3);\\draw[line width=1.4pt] (.79,2.1)--(.79,2.32);\\draw[line width=1.4pt] (.92,2.1)--(.92,2.32);')
    # 4 sperm
    b.append('\\draw[line width=1.3pt,fill=cyan!30,rotate around={35:(2.3,2.85)}] (2.3,2.85) ellipse (.3 and .2);\\draw[line width=1.5pt] (2.52,3.03) .. controls (2.8,3.4) and (2.5,3.6) .. (2.9,3.95);')
    # 5 Leydig
    b.append('\\draw[line width=1.3pt,fill=orange!30] (0,-1.15) ellipse (.8 and .5);\\draw[line width=1.1pt,fill=orange!55] (.1,-1.15) circle (.18);')
    b.append('\\node[font=\\small] at (-2.6,-1.15) {Tübüller arası};')
    for k,(x,y,lx,ly) in {'spg':(-2.7,.15,-3.35,-.55),'prim':(-.95,.77,-1.9,-.55),'spt':(.85,1.9,2.15,1.35),'sperm':(2.6,2.7,3.35,2.1),'ley':(.7,-1.0,2.0,-1.0)}.items():
        b.append(f'\\draw[line width=1pt] ({x},{y})--({lx},{ly});'+sayi(lx,ly,N[k]))
    return tk('\n'.join(b),.8)
def sek_yumurtalik(N):
    b=[]
    b.append('\\draw[line width=1.8pt,fill=pink!20] plot[smooth cycle] coordinates {(-3.4,.2) (-2.9,1.7) (-1.2,2.5) (1.3,2.5) (3.0,1.7) (3.5,.0) (2.9,-1.7) (1.0,-2.5) (-1.5,-2.5) (-3.0,-1.6)};')
    b.append('\\draw[line width=1.2pt,fill=white] (-2.4,.5) circle (.3);\\draw[line width=1pt,fill=blue!25] (-2.4,.5) circle (.12);')
    b.append('\\draw[line width=1.3pt,fill=orange!18] (-1.5,-1.4) circle (.62);\\draw[line width=1pt,fill=blue!25] (-1.5,-1.4) circle (.2);')
    b.append('\\draw[line width=1.5pt,fill=orange!18] (1.2,-1.1) circle (.95);\\draw[line width=1pt,fill=white] (1.4,-1.1) circle (.55);\\draw[line width=1pt,fill=blue!25] (.62,-.8) circle (.17);')
    b.append('\\draw[line width=1.5pt,fill=orange!18] (2.1,.8) arc (180:430:.5);\\draw[line width=1.5pt] (2.1,.8) arc (180:130:.5);\\draw[line width=1pt,fill=blue!25] (3.35,2.0) circle (.14);\\draw[-{Stealth[length=2mm]},line width=1pt] (2.8,1.45)--(3.2,1.85);')
    b.append('\\draw[line width=1.3pt,fill=yellow!45] plot[smooth cycle] coordinates {(-.7,1.2) (-.3,1.95) (.4,1.95) (.8,1.3) (.4,.75) (-.3,.75)};')
    for x1,y1,x2,y2 in [(-2.4,.12,-1.95,-.75),(-.88,-1.4,.15,-1.25),(1.75,-.3,2.25,.3),(2.1,1.2,.95,1.5)]:
        b.append(f'\\draw[-{{Stealth[length=2.4mm,width=2mm]}},line width=1.4pt] ({x1},{y1})--({x2},{y2});')
    for k,(x,y,lx,ly) in {'prim':(-2.65,.6,-3.9,1.0),'gel':(-1.9,-1.8,-2.9,-2.9),'olgun':(1.3,-2.0,1.3,-3.0),'ovu':(3.0,.9,4.2,.4),'cl':(-.2,1.98,-.4,3.1)}.items():
        b.append(f'\\draw[line width=1pt] ({x},{y})--({lx},{ly});'+sayi(lx,ly,N[k]))
    return tk('\n'.join(b),.8)
YAS=[20,25,30,35,40,44,47,50,53,56,60]
EST5=[8.2,8.2,8.1,7.9,7.6,7,5.2,3.0,1.8,1.2,1.0]; FSH5=[1.4,1.4,1.5,1.5,1.7,2.3,4.0,6.5,8.2,9.0,9.2]
assert EST5[-1]<EST5[0] and FSH5[-1]>FSH5[0] and all(a>=b for a,b in zip(EST5,EST5[1:])) and all(a<=b for a,b in zip(FSH5,FSH5[1:]))
def sek_menopoz():
    b=['\\addplot[smooth,line width=1.6pt,vurgu] coordinates {'+' '.join(f'({x},{y})' for x,y in zip(YAS,EST5))+'};',
       '\\addplot[smooth,line width=1.6pt,black,dashed] coordinates {'+' '.join(f'({x},{y})' for x,y in zip(YAS,FSH5))+'};',
       '\\node[font=\\small\\bfseries] at (axis cs:23,9.0) {K};','\\node[font=\\small\\bfseries] at (axis cs:23,2.3) {L};']
    return pgf('\n'.join(b),w='7.6cm',h='5.4cm',ek='xmin=18,xmax=62,ymin=0,ymax=10.5,xtick={20,30,40,50,60},ytick=\\empty,axis lines=left,xlabel={Yaş},ylabel={Kandaki derişim (göreli)}')
def sek_kesik(Nm):
    b=[]
    # erkek
    b.append('\\draw[line width=1.5pt,fill=orange!20] (-3.3,3.0) ellipse (.8 and .55);\\node[font=\\small] at (-3.3,3.0) {Mesane};')
    b.append('\\draw[line width=3pt,yellow!70!orange] (-3.3,2.45)--(-3.3,-1.7);')
    b.append('\\draw[line width=1.5pt,fill=orange!25,rotate around={-12:(-1.5,-.4)}] (-1.5,-.4) ellipse (.55 and .95);')
    b.append('\\draw[line width=2.4pt,brown!70,line cap=round] (-1.1,.2) .. controls (-.7,-.4) and (-.9,-1.0) .. (-1.4,-1.3);')
    b.append('\\draw[line width=2.2pt,blue!60!black] (-1.35,.55) .. controls (-1.3,1.7) and (-1.4,2.4) .. (-1.9,2.55);')
    b.append('\\draw[line width=2.2pt,blue!60!black] (-2.2,2.55) .. controls (-2.8,2.3) and (-3.1,2.1) .. (-3.3,1.0);')
    b.append('\\node[font=\\small] at (-1.0,-.4) {};')
    b.append('\\draw[line width=2pt,red!75] (-1.75,2.7)--(-2.05,2.4);\\draw[line width=2pt,red!75] (-2.05,2.7)--(-1.75,2.4);')
    b.append('\\node[font=\\small,anchor=west] at (-.7,-.1) {Testis};\\node[font=\\small,anchor=west] at (-.7,-1.2) {Epididim};')
    b.append(sayi(-1.9,3.35,Nm['K'],''))
    # kadın
    b.append('\\draw[line width=1.6pt,fill=pink!35] (4.6,-1.6) .. controls (3.8,-.5) and (3.8,.4) .. (3.7,1.1) .. controls (4.2,1.5) and (5.0,1.5) .. (5.5,1.1) .. controls (5.4,.4) and (5.4,-.5) .. (4.6,-1.6);')
    b.append('\\draw[line width=2.4pt,blue!60!black] (3.85,1.0) .. controls (3.0,1.6) and (2.4,1.9) .. (1.5,1.5);\\draw[line width=2.4pt,blue!60!black] (5.35,1.0) .. controls (6.1,1.6) and (6.7,1.9) .. (7.5,1.5);')
    b.append('\\draw[line width=1.4pt,fill=orange!25] (1.2,1.1) ellipse (.45 and .6);\\draw[line width=1.4pt,fill=orange!25] (7.8,1.1) ellipse (.45 and .6);')
    b.append('\\draw[line width=2pt,red!75] (2.55,1.95)--(2.85,1.6);\\draw[line width=2pt,red!75] (2.85,1.95)--(2.55,1.6);')
    b.append('\\node[font=\\small] at (4.6,2.0) {Uterus};\\node[font=\\small] at (1.1,2.1) {Yumurtalık};')
    b.append(sayi(2.7,2.55,Nm['L'],''))
    return tk('\n'.join(b),.75)
def sek_ebeveyn():
    b=[]
    b.append('\\draw[line width=1.6pt,fill=white] (-1.9,2.3) rectangle (-1.2,3.0);\\node[font=\\small] at (-1.55,3.35) {Baba};')
    b.append('\\draw[line width=1.6pt,fill=white] (1.5,2.65) circle (.37);\\node[font=\\small] at (1.5,3.35) {Anne};')
    b.append('\\draw[line width=1.5pt] (-1.2,2.65)--(1.13,2.65);')
    b.append('\\draw[line width=1.5pt] (-.03,2.65)--(-.03,1.3);')
    b.append('\\draw[line width=1.6pt,fill=black] (-.4,.55) rectangle (.34,1.3);\\node[font=\\small] at (-.03,.2) {47, XXY};')
    b.append('\\draw[line width=1.6pt,fill=black] (2.5,-.6) rectangle (3.0,-.1);\\node[font=\\small,anchor=west] at (3.2,-.35) {Hemofili};')
    b.append('\\draw[line width=1.6pt,fill=white] (-1.2,-.6) rectangle (-.7,-.1);\\node[font=\\small,anchor=west] at (-.5,-.35) {Sağlıklı};')
    return tk('\n'.join(b),.9)
# =============== SORULAR ===============
ROM5=['I','II','III','IV','V']
# ---------- 01 · nörula kesiti · kolay · şekilli · C ----------
TAB1={'I':'ektoderm','II':'mezoderm','III':'endoderm','IV':'mezoderm','V':'ektoderm'}
assert [k for k,v in TAB1.items() if v=='endoderm']==['III']
N1=dict(sinir='I',noto='II',bag='III',somit='IV',dis='V')
Q('uk-embriyo','kolay','Embriyonik tabakalardan gelişen yapılar','Gastrula evresinde oluşan üç tabaka, vücudun doku ve organ sistemlerine ayrılır; bir yapının hangi tabakadan geliştiği, ait olduğu sistemin kökenine bakılarak bulunur.','Sindirim kanalının iç yüzeyini ya da vücut yüzeyini yanlış tabakayla eşleştirmek; notokordu endoderm saymak.','şekilli',
 'Şekilde, nörula evresindeki bir omurgalı embriyonun enine kesiti gösterilmiştir. I numaralı yapı ileride beyin ve omuriliği oluşturacak nöral tüp, II numaralı yapı sırt boyunca uzanan notokord, III numaralı yapı sindirim kanalının iç yüzeyini oluşturan boşluklu yapı, IV numaralı yapı ileride iskelet kaslarını oluşturacak somit, V numaralı yapı ise vücudu dıştan saran tabakadır.\nBuna göre, numaralı yapılardan hangisi endoderm tabakasından gelişmiştir?',
 'Endoderm tabakasından gelişen yapının numarası.','Her yapının ait olduğu doku ya da organ sistemini belirle; sonra bu sistemin hangi embriyonik tabakadan geliştiğini düşün.',
 [B('Embriyonik tabakalar','Gastrula evresinde embriyo ektoderm, mezoderm ve endoderm adlı üç tabakadan oluşur. Vücuttaki tüm doku ve organlar bu tabakaların farklılaşmasıyla meydana gelir. Örnek: Çok hücreli bir canlının tüm hücreleri tek bir zigottan türediği için ortak bir kaynaktan farklılaşmıştır')],
 [A('Yapıları sistemlere ayır','I nöral tüp sinir sistemine, II notokord iskelet eksenine, III sindirim kanalı iç yüzeyine, IV somit iskelet kaslarına, V dış tabaka ise vücut yüzeyine aittir.','I: sinir · II: eksen iskelet · III: sindirim · IV: kas · V: dış yüzey'),
  A('Tabaka kökenlerini eşleştir','Sinir sistemi ve vücut yüzeyinin dış tabakası ektodermden; notokord ile iskelet kasları mezodermden; sindirim kanalının iç yüzeyi endodermden gelişir.','I, V: ektoderm · II, IV: mezoderm · III: endoderm'),
  A('Endodermi bul','Yalnız sindirim kanalının iç yüzeyini oluşturan yapı endodermden gelişir.','Endoderm: III')],
 'Yapıların ait olduğu sistemi bul; sonra tabakasını eşleştir.',sekil=sek_norula(N1),dogru='III',sira=ROM5,
 yan=[('I','I numaralı nöral tüp sinir sistemini oluşturur; sinir sistemi ektodermden geliştiği için bu yapı endoderm kökenli değildir.','bilgi'),
      ('II','II numaralı notokord mezodermden gelişir; mezoderm kökenli bir yapı olduğundan endoderm kökenli sayılmaz.','bilgi'),
      ('IV','IV numaralı somit iskelet kaslarını oluşturur; kaslar mezodermden geliştiği için bu yapı endoderm kökenli değildir.','bilgi'),
      ('V','V numaralı dış tabaka epidermisi oluşturur; epidermis ektodermden geliştiği için bu yapı endoderm kökenli değildir.','bilgi')])
# ---------- 02 · emzirme hormonları · kolay · düz · A ----------
H2='Oksitosin – Prolaktin'
O2=['Prolaktin – Oksitosin','Oksitosin – Östrojen','Östrojen – Prolaktin','FSH – Oksitosin']
Q('uk-hormon','kolay','Süt üretimi ve süt sürmesi','Doğum sonrasında süt üretimi hipofiz ön lobundan salgılanan hormonla, sütün meme ucuna akması ise hipotalamusta sentezlenip hipofiz arka lobundan salgılanan hormonla sağlanır.','Süt üretimi ile süt sürmesini sağlayan hormonların görevini birbirine karıştırmak.','düz',
 'Doğumdan sonra emzirme döneminde bebeğin memeyi emmesi, hipotalamus yoluyla hipofizin arka lobundan bir hormonun salgılanmasını uyarır. Bu hormon meme kanallarının çevresindeki düz kasların kasılmasına yol açarak sütün meme ucuna akmasını sağlar. Süt üretimi ise hipofizin ön lobundan salgılanan başka bir hormonun etkisiyle sürer.\nBuna göre, sütün meme ucuna akmasını sağlayan hormon ile süt üretimini uyaran hormon sırasıyla aşağıdakilerden hangisidir?',
 'Süt sürmesini sağlayan ve süt üretimini uyaran hormonlar.','Hipofizin hangi lobunun hangi hormonu salgıladığını ve bu hormonların süt üzerindeki farklı etkilerini hatırla.',
 [B('Emzirme dönemi hormonları','Hipofiz ön lobu ve arka lobu farklı hormonlar salgılar. Emzirme sırasında bu hormonlar sütün hem oluşmasında hem de dışarı akışında rol oynar. Örnek: Büyüme hormonu da hipofizin ön lobundan salgılanan bir hormondur')],
 [A('Verilen bilgiyi çöz','Arka lobdan salgılanan hormon sütün akmasını, ön lobdan salgılanan hormon süt üretimini sağlar.','arka lob → akış · ön lob → üretim'),
  A('Hormonları adlandır','Hipofiz arka lobundan salgılanan ve düz kasları kasan hormon oksitosindir; ön lobdan salgılanan ve süt üretimini uyaran hormon prolaktindir.','arka lob: oksitosin · ön lob: prolaktin'),
  A('Sırayı yaz','Önce süt akışını sağlayan, sonra süt üretimini uyaran hormon yazılır.','Oksitosin – Prolaktin')],
 'Arka lob hormonunu kas kasılmasıyla, ön lob hormonunu süt üretimiyle ilişkilendir.',dogru=H2,sira=yer(H2,O2,'A'),
 yan=[(O2[0],'Süt akışı ile süt üretimini sağlayan hormonların yerini değiştirmiş; oysa süt akışını oksitosin, süt üretimini prolaktin sağlar.','bilgi'),
      (O2[1],'Süt üretimini östrojenin uyardığını sanmış; oysa süt üretimini hipofiz ön lobundan salgılanan prolaktin uyarır.','bilgi'),
      (O2[2],'Süt akışını östrojenin sağladığını sanmış; oysa süt akışını hipofiz arka lobundan salgılanan oksitosin sağlar.','bilgi'),
      (O2[3],'Süt akışını sağlayan hormonu doğru bulmuş ama süt üretimini FSH’nin uyardığını sanmış; oysa FSH folikül gelişimini ve spermatogenezi destekler, süt üretimini prolaktin uyarır.','bilgi')])
# ---------- 03 · seminifer tübül · orta · öncüllü · B ----------
T3=[True,True,False]
N3=dict(spg=1,prim=2,spt=3,sperm=4,ley=5)
n3=['spermatogonyum mitozla bölünerek hem sayısını korur hem de büyüyerek birincil spermatosite dönüşecek hücreleri oluşturur',
    'spermatit, mayoz II sonunda oluşan n kromozomlu bir hücredir ve kromozomları tek kromatitlidir',
    'Leydig hücreleri testosteronu LH’nin etkisiyle salgılar; FSH ise Sertoli hücreleri üzerinden spermatogenezi destekler']
d3,y3,s3=onc(T3,n3,'B')
Q('uk-gamet','orta','Seminifer tübül ve Leydig hücreleri','Spermatogonyum mitozla çoğalır; spermatit mayoz II sonunda oluşan tek kromatitli n kromozomlu hücredir; Leydig hücreleri LH ile testosteron salgılar.','Leydig hücresinin FSH ile uyarıldığını sanmak; spermatiti çift kromatitli saymak.','öncüllü',
 'Şekilde, bir erkeğin testisindeki seminifer tübül duvarının bir bölümü ile tübüller arasında bulunan bir hücre gösterilmiştir. 1, 2, 3 ve 4 numaralı hücreler sırasıyla spermatogonyum, birincil spermatosit, spermatit ve sperm hücresidir; 5 numaralı hücre ise tübüller arasındaki Leydig hücresidir.\n'
 +etiket_oncul(f'{N3["spg"]} numaralı hücre mitozla bölünerek hem sayısını korur hem de {N3["prim"]} numaralı hücrenin kaynağını oluşturur.',f'{N3["spt"]} numaralı hücrenin kromozomlarının tamamı tek kromatitlidir.',f'{N3["ley"]} numaralı hücre, FSH’nin etkisiyle testosteron salgılar.')+'Buna göre, yukarıdaki yargılardan hangileri doğrudur?',
 'Şekildeki hücrelerle ilgili doğru yargılar.','Her yargıdaki hücrenin sperm oluşumundaki yerini ve hangi hormonla uyarıldığını ayrı ayrı düşün.',
 [B('Spermatogenez ve testisin hormon hücreleri','Spermatogenez seminifer tübüllerde gerçekleşir; tübüllerin dışında, aralarındaki dokuda ise hormon salgılayan hücreler bulunur. Hipofiz hormonları bu iki hücre grubunu farklı biçimde uyarır. Örnek: Mitoz kromozom sayısını korurken mayoz yarıya indirir')],
 oadim(T3,n3)+[A('Sonuç','Doğru yargılar I ve II’dir.','I ve II')],'Üç yargıyı ayrı ayrı sına; hormon–hücre eşleşmesine özellikle dikkat et.',sekil=sek_tubul(N3),dogru=d3,yan=y3,sira=s3)
# ---------- 04 · yumurtalık döngüsü · orta · şekilli · olumsuz · B ----------
N4=dict(prim=2,gel=5,olgun=1,ovu=4,cl=3)
assert sorted(N4.values())==[1,2,3,4,5]
S4=dict(
 y=f'{N4["cl"]} numaralı yapı, döllenme gerçekleşmediğinde gerilemez ve progesteron salgısını sonraki döngüde de sürdürür.',
 a=f'{N4["prim"]} numaralı yapıdaki birincil oosit, mayoz I’e doğumdan önce başlamıştır.',
 b=f'{N4["gel"]} numaralı yapıdaki folikül hücreleri, FSH etkisiyle çoğalır ve östrojen salgılar.',
 c=f'{N4["ovu"]} numaralı olayın gerçekleşmesinde LH derişiminin ani artışı etkilidir.',
 d=f'{N4["olgun"]} numaralı yapıdaki oosit, folikülden atılmadan hemen önce mayoz I’i tamamlayarak ikincil oosit hâline gelir.')
Q('uk-disi','orta','Yumurtalıkta folikül gelişimi ve korpus luteum','Folikül FSH ile gelişir ve östrojen salgılar; ovulasyon LH artışıyla olur; folikülden kalan hücreler korpus luteumu oluşturur ve döllenme olmazsa korpus luteum gerilemeye uğrar.','Korpus luteumun döllenme olmasa da kalıcı olduğunu sanmak; mayoz I’in ovulasyondan sonra tamamlandığını düşünmek.','şekilli',
 'Şekilde, sağlıklı bir kadının yumurtalığında bir menstrüasyon döngüsü sırasında gerçekleşen olaylar numaralandırılarak gösterilmiştir. Oklar olayların oluş sırasını göstermektedir.\nBuna göre, numaralı yapı ve olaylarla ilgili aşağıdakilerden hangisi yanlıştır?',
 'Yumurtalıktaki yapı ve olaylarla ilgili yanlış ifade.','Şekildeki okları izleyerek her yapının hangi evreye ait olduğunu belirle; sonra hormon ve mayoz bilgisini o evreyle eşleştir.',
 [B('Yumurtalık döngüsü','Yumurtalıkta foliküller, ovulasyon ve ovulasyondan sonra oluşan yapı sırasıyla ilerleyen evreleri oluşturur. Bu evrelerin her birinde farklı hormonlar etkilidir. Örnek: Ovulasyon sırasında foliküldeki oosit yumurtalıktan dışarı atılır')],
 [A('Evreleri sırala','Oklar izlendiğinde yapılar sırasıyla birincil oosit içeren primer folikül, gelişen folikül, olgun folikül, ovulasyon ve korpus luteumdur.',f'{N4["prim"]} → {N4["gel"]} → {N4["olgun"]} → {N4["ovu"]} → {N4["cl"]}'),
  A('İfadeleri sına','Primer folikülde oosit doğum öncesi mayoza başlamıştır; gelişen folikül FSH ile östrojen salgılar; ovulasyon LH artışıyla olur; oosit atılmadan önce mayoz I’i bitirir.','Dört ifade doğru'),
  A('Korpus luteumu değerlendir','Döllenme olmazsa korpus luteum yaklaşık iki hafta sonra dejenere olur ve progesteron salgısı durur.',f'{N4["cl"]}: kalıcı değil'),
  A('Yanlışı seç','Korpus luteumun gerilemediğini söyleyen ifade yanlıştır.',f'Yanlış: {N4["cl"]} numaralı yapı ifadesi')],
 'Evre sırasını belirle; her evrenin hormonunu ve süresini hatırla.',sekil=sek_yumurtalik(N4),dogru=S4['y'],sira=yer(S4['y'],[S4['a'],S4['b'],S4['c'],S4['d']],'B'),
 yan=[(S4['a'],'Birincil oositlerin mayoz I’e doğum öncesinde başladığı doğrudur; ifade doğrudur, bu yüzden yanlış ifade değildir.','bilgi'),
      (S4['b'],'Gelişen folikül hücrelerinin FSH etkisiyle çoğalıp östrojen salgılaması doğrudur; ifade doğrudur, bu yüzden yanlış ifade değildir.','bilgi'),
      (S4['c'],'Ovulasyon LH derişiminin ani artışıyla gerçekleşir; ifade doğrudur, bu yüzden yanlış ifade değildir.','bilgi'),
      (S4['d'],'Oosit ovulasyondan hemen önce mayoz I’i tamamlayıp ikincil oosit olur; ifade doğrudur, bu yüzden yanlış ifade değildir.','bilgi')])
# ---------- 05 · menopoz grafiği · orta · olumsuz · E ----------
S5=dict(
 y='55 yaşında kandaki östrojenin düşük olması, yumurtalıkların FSH’ye verdiği yanıtın artmasıyla açıklanır.',
 a='Menopoza girmiş bir kadında ovulasyon gerçekleşmez ve menstrüasyon sona erer.',
 b='L eğrisi FSH’ye aittir.',
 c='K eğrisindeki azalma, yumurtalıkta östrojen salgılayan foliküllerin azalmasıyla ilişkilidir.',
 d='55 yaşında FSH derişiminin yüksek olması, östrojenin hipofiz üzerindeki baskılayıcı etkisinin azalmasından kaynaklanır.')
Q('uk-hormon','orta','Menopoz ve hormon değişimleri','Menopozda yumurtalık işlevi azalır; östrojen düşer ve negatif geri bildirim zayıfladığı için hipofizden FSH ile LH salgısı artar.','Menopozda FSH’nin östrojenle birlikte azaldığını sanmak; yumurtalıkların hormon yanıtının arttığını düşünmek.','grafik',
 'Sağlıklı bir kadında yaşa bağlı olarak kandaki östrojen ve FSH derişimlerindeki değişim grafikte K ve L eğrileriyle gösterilmiştir. Eğrilerden biri östrojene, diğeri FSH’ye aittir. Kadında menopoz yaklaşık 50 yaşında başlamıştır.\nBuna göre, aşağıdakilerden hangisi yanlıştır?',
 'Yanlış olan ifade.','Hangi eğrinin hangi hormona ait olduğunu, yumurtalık ile hipofiz arasındaki ilişkiden çıkar.',
 [B('Yaşlanma ve üreme hormonları','Kadında yumurtalık işlevi yaşla birlikte değişir ve bu durum hipotalamus–hipofiz–yumurtalık ilişkisini etkiler. Örnek: Erkekte testosteron salgısı da yaşla yavaşça azalır')],
 [A('Eğrileri tanı','Yumurtalık işlevi bozulunca östrojen düşer; östrojen düşünce hipofiz üzerindeki baskı azalır ve FSH artar. Buna göre K östrojene, L FSH’ye aittir.','K: östrojen · L: FSH'),
  A('Doğru ifadeleri ayır','Menopozda ovulasyon ve menstrüasyon sona erer; östrojen azalması folikül azalmasıyla ilişkilidir; FSH artışı baskının azalmasından kaynaklanır.','Dört ifade doğru'),
  A('Yumurtalık yanıtını değerlendir','Menopozda yumurtalıkta FSH’ye yanıt veren folikül kalmadığı için yanıt azalır, artmaz.','Yanıt ↓'),
  A('Yanlışı seç','Yumurtalık yanıtının arttığını söyleyen ifade yanlıştır.','Yanlış: yanıt artışı ifadesi')],
 'Menopozda yumurtalığın hormona yanıt kapasitesinin nasıl değiştiğini düşün.',sekil=sek_menopoz(),dogru=S5['y'],sira=yer(S5['y'],[S5['a'],S5['b'],S5['c'],S5['d']],'E'),
 yan=[(S5['a'],'Menopozda foliküller kalmadığı için ovulasyon ve menstrüasyon sona erer; ifade doğrudur, bu yüzden yanlış ifade değildir.','bilgi'),
      (S5['b'],'Östrojen azalınca baskı zayıfladığı için artan eğri FSH’ye aittir; ifade doğrudur, bu yüzden yanlış ifade değildir.','bilgi'),
      (S5['c'],'Östrojeni foliküller salgıladığı için foliküllerin azalması östrojeni azaltır; ifade doğrudur, bu yüzden yanlış ifade değildir.','bilgi'),
      (S5['d'],'Östrojen negatif geri bildirimle hipofizi baskılar; östrojen azalınca FSH artar, ifade doğrudur, bu yüzden yanlış ifade değildir.','bilgi')])
# ---------- 06 · blastomer sayısı · orta · tablo · A ----------
VT=160; KR=6
def hucre_sayisi(b): return 2**b
def hac(b): return Fr(VT,hucre_sayisi(b))
def top_kr(b): return KR*hucre_sayisi(b)
K6=hac(3); L6=hucre_sayisi(4); M6=top_kr(3)
assert (K6,L6,M6)==(20,16,48) and hac(4)==10 and hac(2)==40 and top_kr(4)==96
SK6=tab(['Bölünme sayısı','Hücre sayısı','Hücre hacmi','Toplam kromozom'],[['0',1,int(hac(0)),top_kr(0)],['1',2,int(hac(1)),top_kr(1)],['2',4,int(hac(2)),top_kr(2)],['3',8,'K','M'],['4','L',int(hac(4)),top_kr(4)]],cw=6.0)
D6=f'{K6} – {L6} – {M6}'
O6=[f'{K6} – {L6} – {KR}',f'{K6} – {2*4} – {M6}',f'{VT} – {L6} – {M6}',f'{K6} – {2**5} – {M6}']
assert len({D6,*O6})==5
Q('uk-embriyo','orta','Yarılma bölünmelerinde hücre sayısı ve hacmi','Yarılma (segmentasyon) evresinde zigot art arda mitozla bölünür; embriyonun toplam hacmi artmaz, hücre sayısı her bölünmede iki katına çıkar, hücreler küçülür, her hücre aynı sayıda kromozom taşır.','Yarılmada hücre hacminin korunduğunu sanmak; hücre sayısını bölünme sayısıyla doğru orantılı saymak; kromozom sayısını bölünmeyle azalan ya da sabit toplam saymak.','tablo',
 'Kromozom sayısı 2n = 6 olan bir canlıda zigot, art arda mitoz bölünmelerle çoğalarak embriyonun yarılma evrelerini oluşturmaktadır. Bu evrelerde embriyonun toplam hacmi değişmemekte, her bölünmede hücreler eşit büyüklükte iki yavru hücre oluşturmaktadır. Tabloda embriyonun bölünme sayısına göre hücre sayısı, bir hücrenin hacmi (birim) ve embriyonun hücrelerindeki toplam kromozom sayısı verilmiştir.\nBuna göre, tablodaki K, L ve M değerleri sırasıyla aşağıdakilerden hangisinde doğru verilmiştir?',
 'K, L ve M değerleri.','Önce hücre sayısının bölünme sayısıyla nasıl değiştiğini, sonra toplam hacim ve kromozom sayısının nasıl hesaplandığını düşün.',
 [B('Yarılma bölünmeleri','Döllenmeden sonra zigot, büyümeden art arda mitozla bölünür ve hücre sayısı artar. Her yavru hücre ana hücre ile aynı kalıtsal bilgiyi taşır. Örnek: Mitoz bölünmede kromozom sayısı korunur')],
 [A('Hücre sayısını bul','Her bölünmede hücre sayısı iki katına çıkar; 4 bölünme sonunda 2⁴ hücre bulunur.',f'L = 2⁴ = {L6}'),
  A('Hücre hacmini bul','Toplam hacim sabittir; 3 bölünme sonunda 8 hücre vardır ve her biri toplam hacmin sekizde birini kaplar.',f'K = {VT} ÷ 8 = {K6}'),
  A('Toplam kromozom sayısını bul','Her hücre 6 kromozom taşır; 3 bölünme sonunda 8 hücre vardır.',f'M = 8 × 6 = {M6}'),
  A('Değerleri yaz','Üç değer sırasıyla yazılır.',D6)],
 'Hücre sayısını, sonra hücre başına hacmi ve kromozomu hesapla.',sekil=SK6,dogru=D6,sira=yer(D6,O6,'A'),
 yan=[(O6[0],f'Toplam kromozom sayısının zigottaki gibi {KR} kaldığını sanmış (M = {KR}); oysa her hücre {KR} kromozom taşıdığı için 8 hücrede toplam {M6} kromozom bulunur.','islem'),
      (O6[1],'Hücre sayısını bölünme sayısı × 2 gibi hesaplamış (L = 8); oysa her bölünmede hücre sayısı iki katına çıktığı için 4 bölünmede 16 hücre bulunur.','islem'),
      (O6[2],f'Yarılmada hücre hacminin değişmediğini sanmış (K = {VT}); oysa toplam hacim sabit kaldığı için hücre sayısı arttıkça her hücrenin hacmi küçülür.','bilgi'),
      (O6[3],'Bölünme sayısını bir fazla alarak 2⁵ hücre bulmuş (L = 32); oysa tabloda 4 bölünme sonrası 2⁴ = 16 hücre vardır.','islem')])
# ---------- 07 · vazektomi / tüp bağlama · orta · öncüllü · C ----------
T7=[True,False,True]
N7=dict(K='K',L='L')
n7=['testosteron kandan yayılan bir hormondur; sperm kanalının kesilmesi testisin hormon salgısını etkilemez ve ikincil eşey karakterleri korunur',
    'tuba kesilse de yumurtalıktaki folikül gelişimi, ovulasyon ve hormon döngüsü sürer, bu yüzden menstrüasyon da devam eder',
    'sperm kanalı kesilen erkekte spermler üretrada karışamaz; seminal vezikül ve prostatın salgıları ise meniyi oluşturmayı sürdürür']
d7,y7,s7=onc(T7,n7,'C')
Q('uk-saglik','orta','Sperm kanalı ve tuba kesilmesinin sonuçları','Sperm kanalının ya da tubanın kesilmesi gametlerin taşınmasını engeller; hormon salgısı ve döngü gibi diğer işlevler değişmez.','Kesilen kanalın hormon salgısını da durdurduğunu sanmak.','öncüllü',
 'Şekilde, bir erkekte ve bir kadında üreme sisteminin birer bölümü gösterilmiştir. Doğum kontrolü amacıyla erkekte K noktasından sperm kanalı, kadında L noktasından tuba kesilmiş ve uçlar bağlanmıştır. İki bireyde de hipotalamus ve hipofiz sağlıklıdır; başka bir müdahale yapılmamıştır.\n'
 +etiket_oncul('K noktasından kesilen erkekte testosteron salgısı sürer ve ikincil eşey karakterleri korunur.','L noktasından kesilen kadında ovulasyon gerçekleşmez; bu nedenle menstrüasyon sona erer.','K noktasından kesilen erkekte boşalan meni sıvısında sperm hücresi bulunmaz, ancak meni sıvısı oluşmaya devam eder.')+'Buna göre, yukarıdaki yargılardan hangileri doğrudur?',
 'Doğru yargılar.','Kesilen kanalın yalnız gametlerin geçişini mi, yoksa hormon salgısını ve döngüyü de mi etkilediğini ayrı ayrı sorgula.',
 [B('Doğum kontrol yöntemleri','Doğum kontrolünde gametlerin buluşmasını engelleyen yöntemlerin bir bölümü, üreme sisteminin kanallarını kesmeyi ya da bağlamayı içerir. Örnek: Prezervatif spermin vajinaya ulaşmasını engelleyen bir engel yöntemidir')],
 oadim(T7,n7)+[A('Sonuç','Doğru yargılar I ve III’tür.','I ve III')],'Her yargıda kesilen kanalın görevini ve bunun hormon salgısına etkisini ayrı ayrı sına.',sekil=sek_kesik(N7),dogru=d7,yan=y7,sira=s7)
# ---------- 08 · yumurtalık ve hipofiz çıkarma deneyi · zor · tablo · olumsuz · E ----------
G8={'K':(5,5,50),'L':(18,20,2),'M':(6,6,50),'N':(1,1,3)}
assert G8['L'][0]>G8['K'][0] and G8['L'][1]>G8['K'][1] and G8['M'][0]<G8['L'][0] and G8['M'][2]==G8['K'][2] and G8['N'][2]<G8['K'][2] and G8['N'][0]<G8['K'][0]
SK8=tab(['Grup','FSH','LH','Östrojen'],[[g,*G8[g]] for g in 'KLMN'],cw=6.3)
S8=dict(
 y='L grubuna FSH ve LH verilseydi kandaki östrojen derişiminin K grubundakine ulaşması beklenirdi.',
 a='L grubunda FSH ve LH derişimlerinin artması, östrojenin hipofiz üzerindeki baskılayıcı etkisinin ortadan kalkmasıyla açıklanır.',
 b='L ve M grupları karşılaştırıldığında östrojenin FSH ve LH salgısını baskıladığı sonucuna varılır.',
 c='N grubunda östrojen derişiminin düşük olması, yumurtalıkların hipofiz hormonlarıyla uyarılamamasıyla açıklanabilir.',
 d='K, L ve N grupları birlikte değerlendirildiğinde yumurtalıkların östrojen salgısının hipofiz hormonlarına bağlı olduğu ve hipofiz hormonlarının östrojenle denetlendiği sonucuna varılır.')
Q('uk-hormon','zor','Hipotalamus–hipofiz–yumurtalık ekseni ve geri bildirim','Yumurtalık östrojen salgılamak için FSH ve LH’ye ihtiyaç duyar; östrojen ise hipofizden FSH ve LH salgısını negatif geri bildirimle baskılar. Bu iki yön birlikte düşünülmelidir.','Yumurtalığı çıkarılmış hayvana FSH verilince östrojenin yükseleceğini sanmak; östrojenin hipofizi uyardığını düşünmek.','tablo',
 'Aynı yaş ve kütledeki sağlıklı dişi sıçanlar dört gruba ayrılmıştır. K grubuna uygulama yapılmamış, L grubunun yumurtalıkları alınmış, M grubunun yumurtalıkları alınmış ve kandaki östrojen derişimini K grubundakine ulaştıracak miktarda östrojen verilmiş, N grubunun ise hipofizi alınmıştır. Birkaç hafta sonra kandaki hormon derişimleri ölçülmüş ve sonuçlar tabloda göreli birimle verilmiştir.\nBuna göre, aşağıdakilerden hangisi söylenemez?',
 'Söylenemeyecek ifade.','Her grupta hangi organın eksik olduğunu ve eksik organın hangi hormon yolunu kestiğini yaz; geri bildirimin yönünü ayrı düşün.',
 [B('Hipotalamus–hipofiz–yumurtalık ilişkisi','Hipofizin salgıladığı hormonlar yumurtalığı etkiler; yumurtalığın salgıladığı hormonlar da hipofizi etkiler. Bu karşılıklı ilişki hormon düzeylerini dengede tutar. Örnek: Tiroksin düzeyi de hipofiz hormonuyla karşılıklı denetlenir')],
 [A('Grupları yorumla','L’de yumurtalık yok: östrojen çok düşük, FSH ve LH yüksek. M’de östrojen verilince FSH ve LH K düzeyine iner. N’de hipofiz yok: FSH, LH ve östrojen düşük.','L: E↓ FSH,LH↑ · M: FSH,LH normal · N: hepsi ↓'),
  A('Doğru ifadeleri ayır','L’deki artış baskının kalkmasıyla, L–M farkı östrojenin baskılamasıyla, N’deki düşük östrojen yumurtalığın uyarılamamasıyla açıklanır; K, L, N birlikte iki yönlü denetimi gösterir.','Dört ifade doğru'),
  A('Beklentiyi sına','L grubunun yumurtalığı yoktur; FSH ve LH verilse bile östrojen salgılayacak doku bulunmadığı için östrojen K düzeyine çıkmaz.','L + FSH, LH → östrojen ≈ düşük'),
  A('Söylenemeyeni seç','Östrojenin K düzeyine ulaşacağını söyleyen ifade söylenemez.','Cevap: L’ye hormon verilmesi ifadesi')],
 'Her grupta eksik olan organı belirle; hormon verilmesinin sonucunu o organın var olup olmadığına göre değerlendir.',sekil=SK8,dogru=S8['y'],sira=yer(S8['y'],[S8['a'],S8['b'],S8['c'],S8['d']],'E'),
 yan=[(S8['a'],'L’de yumurtalık olmadığı için östrojen azalmış, negatif geri bildirim kalkmış ve FSH ile LH 18 ve 20’ye çıkmıştır; ifade söylenebilir.','islem'),
      (S8['b'],'L’de östrojen 2 iken FSH ve LH yüksek, M’de östrojen 50 iken 6 ve 6’dır; östrojen artınca FSH ve LH düştüğü için ifade söylenebilir.','islem'),
      (S8['c'],'N’de hipofiz olmadığı için yumurtalık FSH ve LH uyarısı almaz ve östrojen düşük kalır; ifade söylenebilir.','bilgi'),
      (S8['d'],'N, yumurtalığın hipofize bağlı olduğunu; L ve K ise östrojenin hipofiz hormonlarını denetlediğini gösterir; ifade söylenebilir.','bilgi')])
# ---------- 09 · hemofili + XXY · zor · öncüllü · D ----------
T9=[False,True,True]
n9=['annenin mayoz I’inde homolog X’ler birlikte ayrılsaydı yumurta hücresi hem normal hem çekinik alel taşırdı (XH Xh); bu yumurta Y’li spermle birleşince çocuk hemofili olmazdı',
    'çocuk iki çekinik alel taşıyor ve babası sağlıklı (XHY) olduğu için çekinik alelleri anneden almıştır; anne sağlıklı olduğundan heterozigottur (XH Xh)',
    'yumurta hücresindeki iki X kromozomunun ikisi de çekinik alel taşır (Xh Xh); bu ancak mayoz II’de kardeş kromatitlerin ayrılmamasıyla oluşur']
d9,y9,s9=onc(T9,n9,'D')
Q('uk-gamet','zor','X’e bağlı kalıtım ve ayrılmama','Ayrılmama mayoz I’de olursa homolog kromozomlar birlikte, mayoz II’de olursa kardeş kromatitler birlikte gametlere gider; gametteki alel çeşidi bunu ayırt eder.','Mayoz I ve mayoz II ayrılmamasının gamet genotiplerini aynı sanmak.','öncüllü',
 'Şekilde, hemofili bakımından sağlıklı olan bir anne ile babanın hem hemofili hem de Klinefelter sendromlu (47, XXY) bir erkek çocuğu gösterilmiştir. Hemofili, X kromozomu üzerindeki çekinik bir genle belirlenir. Çocuğun kromozom sayısındaki bozukluk, ebeveynlerden yalnız birinin gamet oluşumu sırasında gerçekleşen tek bir ayrılmama olayından kaynaklanmıştır; başka bir mutasyon yoktur.\n'
 +etiket_oncul('Ayrılmama olayı annenin mayoz I evresinde gerçekleşmiştir.','Çocuğun annesi, hemofili geni bakımından heterozigottur.','Çocuğun oluştuğu yumurta hücresinde bulunan iki X kromozomunun taşıdığı aleller birbirinin aynısıdır.')+'Buna göre, yukarıdaki yargılardan hangileri doğrudur?',
 'Doğru yargılar.','Çocuğun genotipinden başlayıp çekinik alellerin hangi ebeveynden geldiğini bul; sonra hangi mayoz basamağında ayrılmamanın bunu verebileceğini düşün.',
 [B('Kromozom sayısı bozuklukları','Mayozda kromozomların ya da kromatitlerin ayrılmaması gametlerde fazla ya da eksik kromozom oluşmasına yol açar. Bu gametler döllenmeye katılırsa zigotun kromozom sayısı değişir. Örnek: Down sendromunda 21. kromozom üç tanedir')],
 oadim(T9,n9)+[A('Sonuç','Doğru yargılar II ve III’tür.','II ve III')],'Çocuğun genotipini yaz; çekinik alellerin yalnız anneden gelebileceğini ve yumurtadaki iki alelin aynı olması gerektiğini kullan.',sekil=sek_ebeveyn(),dogru=d9,yan=y9,sira=s9)
# ---------- 10 · kısırlık nedenleri tablosu · zor · tablo · D ----------
R10={'K':('+','+',5,15),'L':('+','+',5,3),'M':('−','−',1,1),'N':('+','−',5,15)}
def durum(r):
    ov,mens,fsh,prog=r
    if ov=='−' and fsh<3: return 'hipofiz'
    if ov=='+' and mens=='−': return 'uterus'
    if ov=='+' and mens=='+' and prog>=10: return 'tuba'
    if ov=='+' and mens=='+' and prog<10: return 'korpus'
    raise AssertionError(r)
DD={durum(r):k for k,r in R10.items()}
assert DD=={'hipofiz':'M','uterus':'N','tuba':'K','korpus':'L'}
SK10=tab(['Kadın','Ovulasyon','Menstrüasyon','FSH','Progesteron'],[[k,*R10[k]] for k in 'KLMN'],cw=6.3)
D10=f"{DD['hipofiz']} – {DD['tuba']} – {DD['uterus']}"
O10=[f"{DD['hipofiz']} – {DD['korpus']} – {DD['uterus']}",f"{DD['uterus']} – {DD['tuba']} – {DD['hipofiz']}",f"{DD['hipofiz']} – {DD['uterus']} – {DD['tuba']}",f"{DD['korpus']} – {DD['tuba']} – {DD['uterus']}"]
assert D10=='M – K – N' and len({D10,*O10})==5
Q('uk-saglik','zor','Kısırlık nedenlerinin hormon ve döngü verilerinden çıkarılması','Hipofiz hormonları olmayınca ovulasyon ve döngü durur; tuba kesintisi hormon döngüsünü etkilemez; uterus olmayınca menstrüasyon olmaz; korpus luteum yetersizliğinde progesteron düşük kalır.','Düşük progesteronu tuba tıkanıklığına ya da hipofiz yetersizliğine bağlamak; uterusu olmayan kadında ovulasyonun da durduğunu sanmak.','tablo',
 'Dört kadından birinin hipofizi FSH ve LH salgılayamamakta, birinin iki tüpü kesilip bağlanmış, birinin uterusu ameliyatla alınmış, birinde ise korpus luteum yeterli progesteron salgılayamamaktadır. Kadınların yumurtalıkları hipofiz hormonları varsa normal çalışmaktadır. Tabloda; ovulasyon ve menstrüasyonun gerçekleşip gerçekleşmediği (+ var, − yok) ile ovulasyondan yedi gün sonra ölçülen FSH ve progesteron derişimleri göreli birimle verilmiştir.\nBuna göre, hipofizi FSH ve LH salgılayamayan, iki tüpü bağlanmış ve uterusu alınmış kadınlar sırasıyla hangi harflerle gösterilmiştir?',
 'Üç kadının harfleri.','Her durumun ovulasyonu, menstrüasyonu ve hormon düzeylerini ayrı ayrı nasıl etkileyeceğini önce kendin yaz; sonra tabloyla eşleştir.',
 [B('Kısırlığın nedenleri','Kısırlık; hormon salgısındaki, gamet oluşumundaki ya da gametlerin ve embriyonun taşınmasındaki bozukluklardan kaynaklanabilir. Örnek: Sperm sayısının çok az olması erkek kısırlığının nedenlerinden biridir')],
 [A('Her durumun sonucunu yaz','Hipofiz hormonu yoksa ovulasyon, menstrüasyon ve FSH düşer; tuba kesilse de hormonlar ve döngü sürer; uterus alınınca kanama olmaz ama ovulasyon sürer; korpus luteum yetersizse progesteron düşük kalır.','hipofiz: ovulasyon − · tuba: normal döngü · uterus: kanama − · korpus: progesteron ↓'),
  A('Tabloyu eşleştir','Ovulasyonu ve FSH’si düşük olan kadın hipofiz yetersizliğindedir; ovulasyonu olup kanaması olmayan kadının uterusu yoktur; ovulasyonu, kanaması ve normal progesteronu olan kadında yalnız tuba sorunu vardır; progesteronu düşük kadında korpus luteum yetersizdir.','M: hipofiz · N: uterus · K: tuba · L: korpus luteum'),
  A('Sırayı yaz','Önce hipofiz, sonra tuba, en son uterus yazılır.',D10)],
 'Önce her durumun sonucunu kendin yaz, sonra tabloya bak.',sekil=SK10,dogru=D10,sira=yer(D10,O10,'D'),
 yan=[(O10[0],'Tüpleri bağlı kadını progesteronu düşük kadın (L) sanmış; oysa tuba kesilmesi hormon salgısını etkilemez, progesteronu düşük olan kadında korpus luteum yetersizdir.','bilgi'),
      (O10[1],'Hipofiz yetersizliği ile uterusun alınmasını karıştırmış (N – K – M); oysa ovulasyonu ve FSH’si düşük olan kadın hipofiz yetersizliğindedir, kanaması olmayıp ovulasyonu süren kadın ise uterusu alınmış olandır.','bilgi'),
      (O10[2],'Tüpleri bağlı kadını uterusu alınmış, uterusu alınmış kadını tüpleri bağlı sanmış (M – N – K); oysa kanaması olmayan kadının uterusu yoktur, döngüsü tam olan kadın ise tuba sorunludur.','bilgi'),
      (O10[3],'Hipofiz yetersizliğini progesteronu düşük kadınla (L) eşleştirmiş; oysa hipofiz yetersizliğinde ovulasyon da olmaz, L’de ise ovulasyon vardır ve yalnız progesteron düşüktür.','bilgi')])
# ---------- bitir ----------
def bitir_ab():
    for qq in P.ANA: qq['kardes']=None
    P.yaz(os.path.join(GD,'uremeiki-1.json'),'/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/bos-uremeiki.json')
    tipler={}
    for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu='abio|'+KONU))['kartlar'].append(c['id'])
    json.dump(dict(konu=KONU,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2018–2026 biyoloji soruları (yalnız mantık), MEB 11–12. sınıf biyoloji.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar','aburemeiki.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler),'sorular',len(P.ANA))
bitir_ab()
