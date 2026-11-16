"""TYT Biyoloji · Hücre ve Organeller – Madde Geçişleri · ek paket (hucreiki): 30 soru, kardeş yok, ipucu 1.
Şekiller TikZ (cizim.tikz_svg); organeller biçimle ayırt edilir (renk ipucu yok). Hücre hacmi, kütle, derişim ve öncül doğrulukları
Python'da hesaplanır; her öncülün doğru/yanlış değeri tek yerde (d sözlüğü) tanımlanır, anahtar, adım ve çeldirici açıklamaları oradan üretilir."""
import sys,os,math,itertools
BD=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,BD)
import _hafif_bio as H
from _hafif_bio import *
KONU_='Hücre ve Organeller – Madde Geçişleri'; UK='bio|Hücre ve Organeller – Madde Geçişleri'
H.KONU=KONU_
P=Parti('hucreiki',KONU_,UK,ders='TYT Biyoloji',idon='tytbio')
KY='ÖSYM 2018–2026 TYT Biyoloji (yalnız mantık) · MEB 9. sınıf Hücre ve Organeller – Madde Geçişleri'
TIPAD={'teori':'Hücre teorisi ve tarihçe','prokaryot':'Prokaryot ve ökaryot hücre karşılaştırması','bitkihayvan':'Hayvan ve bitki hücresi farkları',
       'organel':'Organeller ve görevleri','zar':'Hücre zarının yapısı','gecis':'Hücre zarından madde geçişleri','ozmoz':'Ozmoz ve hücrenin su dengesi'}
MAP={}
for t,ns in [('teori',(1,2,3)),('prokaryot',(4,5,6)),('bitkihayvan',(7,8,9)),('organel',(10,11,12,13,14,15)),('zar',(16,17,18)),('gecis',(19,20,21,22,23)),('ozmoz',(24,25,26,27,28,29,30))]:
    for n in ns: MAP[n]=t
assert sorted(MAP)==list(range(1,31))
def q(n,ad,ne,ozet,fikir,tuzak,**k):
    """Kartı kaydeder, soruyu üretir. k: mk() argümanları (metin, dogru, yan, sira, istenen, ip, bilgi, puf, z, alt, kaz, kalip, sekil)."""
    assert len(k['ip'])==1
    tipId='by-hc2-'+MAP[n]; tip=TIPAD[MAP[n]]
    kart(f'K-BYHC2-{n:02d}',k['alt'],fikir,tuzak,k['z'],k['kalip'],len(ad),tipId,tip,KY)
    mk(P,f'{n:04d}',ad=ad,adim=len(ad),tipId=tipId,tip=tip,kart=f'K-BYHC2-{n:02d} ({ozet}) · {ne}',**k)
def qo(n,r,ne,ozet,fikir,tuzak,**k):
    q(n,r['adim'],ne,ozet,fikir,tuzak,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],**k)
def qt(n,ad,t,ne,ozet,fikir,tuzak,**k):
    q(n,ad,ne,ozet,fikir,tuzak,dogru=t['dogru'],yan=t['yan'],sira=t['sira'],**k)
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

# ============================ TikZ çizim kütüphanesi ============================
import re
def kucult(svg):
    """path d özniteliklerindeki sayıları 2 ondalığa yuvarlar (dosya boyutunu küçültür)."""
    def f(m):
        return 'd="'+re.sub(r'-?\d+\.\d+',lambda n:('%.2f'%float(n.group(0))).rstrip('0').rstrip('.') ,m.group(1))+'"'
    return re.sub(r'\bd="([^"]*)"',f,svg)
def tk(body,scale=1.0): return kucult(tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small,scale=%s]\n%s\n\\end{tikzpicture}'%(scale,body)))
OKU='-{Stealth[length=2.3mm,width=1.9mm]}'
def lab(t,x,y,x1,y1,x2,y2):
    return f'\\node[font=\\normalsize\\bfseries] at ({x},{y}) {{{t}}};\\draw[{OKU},line width=.8pt] ({x1},{y1})--({x2},{y2});'
def mito(x,y,a=0,s=1.0):
    return (f'\\begin{{scope}}[shift={{({x},{y})}},rotate={a},scale={s}]\\draw[line width=1pt,fill=black,fill opacity=.10] (0,0) ellipse (.44 and .21);\\draw[line width=1pt] (0,0) ellipse (.44 and .21);\\draw[line width=.5pt] (0,0) ellipse (.39 and .16);'
            '\\draw[line width=.7pt] (-.31,.1)--(-.23,-.1)--(-.13,.11)--(-.03,-.11)--(.07,.11)--(.17,-.11)--(.27,.1);\\end{scope}')
def kloro(x,y,a=0,s=1.0):
    o=f'\\begin{{scope}}[shift={{({x},{y})}},rotate={a},scale={s}]\\draw[line width=1pt,fill=black,fill opacity=.10] (0,0) ellipse (.52 and .27);\\draw[line width=1pt] (0,0) ellipse (.52 and .27);\\draw[line width=.5pt] (0,0) ellipse (.46 and .21);'
    for cx in (-.26,0,.26):
        for dy in (-.08,.0,.08): o+=f'\\draw[line width=.4pt,fill=black,fill opacity=.5] ({cx-.09},{dy-.03}) rectangle ({cx+.09},{dy+.03});'
    return o+'\\end{scope}'
def golgi(x,y,a=0,s=1.0):
    o=f'\\begin{{scope}}[shift={{({x},{y})}},rotate={a},scale={s}]'
    for i,w in enumerate((.55,.5,.45,.38)):
        yy=-.24+.16*i
        o+=f'\\draw[line width=1.1pt] ({-w},{yy}) to[bend right=22] ({w},{yy});'
    for vx,vy in ((-.72,.0),(-.7,.3),(.72,-.05),(.68,.34)): o+=f'\\draw[line width=.8pt] ({vx},{vy}) circle (.07);'
    return o+'\\end{scope}'
def rer(x,y,a=0,s=1.0,ribozom=True,n=3,L=1.5):
    o=f'\\begin{{scope}}[shift={{({x},{y})}},rotate={a},scale={s}]'
    for i in range(n):
        yy=.18*i
        o+=f'\\draw[line width=1pt] plot[domain=0:{L},samples=30] (\\x,{{{yy}+.05*sin(\\x*420)}});'
        if ribozom:
            xs=[.08+.14*j for j in range(int(L/.14)-1)]
            for xx in xs: o+=f'\\fill ({xx:.2f},{yy+.05*math.sin(math.radians(xx*420))+.06:.2f}) circle (.026);'
    return o+'\\end{scope}'
def lizozom(x,y,s=1.0):
    return (f'\\begin{{scope}}[shift={{({x},{y})}},scale={s}]\\draw[line width=1pt,fill=black,fill opacity=.08] (0,0) circle (.17);\\draw[line width=1pt] (0,0) circle (.17);'
            '\\fill (-.06,.05) circle (.024);\\fill (.05,.07) circle (.024);\\fill (0,-.06) circle (.024);\\fill (.07,-.04) circle (.024);\\fill (-.07,-.04) circle (.024);\\end{scope}')
def sentrozom(x,y,a=0,s=1.0):
    o=f'\\begin{{scope}}[shift={{({x},{y})}},rotate={a},scale={s}]\\draw[line width=.9pt] (-.2,-.05) rectangle (.2,.05);'
    for xx in (-.1,0,.1): o+=f'\\draw[line width=.5pt] ({xx},-.05)--({xx},.05);'
    o+='\\draw[line width=.9pt] (-.05,-.06) rectangle (.05,-.46);'
    for yy in (-.16,-.26,-.36): o+=f'\\draw[line width=.5pt] (-.05,{yy})--(.05,{yy});'
    return o+'\\end{scope}'
def nukleus(x,y,r=.55):
    return (f'\\draw[line width=1pt] ({x},{y}) circle ({r});\\draw[line width=.5pt] ({x},{y}) circle ({r-.06});'
            f'\\fill ({x+.25*r:.2f},{y+.2*r:.2f}) circle ({.26*r:.2f});'
            f'\\draw[line width=.4pt] ({x-.5*r:.2f},{y-.3*r:.2f}) to[bend left=30] ({x-.1*r:.2f},{y-.6*r:.2f});\\draw[line width=.4pt] ({x-.55*r:.2f},{y+.25*r:.2f}) to[bend right=30] ({x-.2*r:.2f},{y+.55*r:.2f});')
def blob(pts,fill=.07,lw=1.0,dash=''):
    c=' '.join(f'({x:.2f},{y:.2f})' for x,y in pts)
    return f'\\draw[line width={lw}pt,smooth cycle,fill=black,fill opacity={fill}{dash}] plot coordinates {{{c}}};\\draw[line width={lw}pt,smooth cycle{dash}] plot coordinates {{{c}}};'
def oval(cx,cy,rx,ry,n=14,pert=.05,faz=0.0):
    return [(cx+rx*(1+pert*math.sin(3*t+faz))*math.cos(t),cy+ry*(1+pert*math.sin(3*t+faz))*math.sin(t)) for t in [2*math.pi*i/n for i in range(n)]]
def hayvan_hucre(cx,cy,rx,ry,faz=0.0): return blob(oval(cx,cy,rx,ry,faz=faz),fill=0,lw=1.7)
def bitki_hucre(x0,y0,x1,y1):
    return (f'\\draw[rounded corners=9pt,line width=2.2pt] ({x0},{y0}) rectangle ({x1},{y1});'
            f'\\draw[rounded corners=7pt,line width=.9pt] ({x0+.17},{y0+.17}) rectangle ({x1-.17},{y1-.17});')
def koful(cx,cy,rx,ry,faz=0.5): return blob(oval(cx,cy,rx,ry,n=10,pert=.08,faz=faz),fill=.05,lw=.9,dash=',dashed')
def nokta(x,y,r=.05): return f'\\fill ({x:.2f},{y:.2f}) circle ({r});'

# ============================ ŞEKİLLER ============================
# --- F1: hayvan (X) ve bitki (Y) hücresi, I–V numaralı ---
def sekil_f1():
    b=[hayvan_hucre(2.3,2.0,2.2,1.9,faz=.4),nukleus(1.5,2.3,.6),sentrozom(2.95,2.7,15,1.3),mito(1.35,.8,10,1.3),mito(3.3,1.0,-25,1.3)]
    b+=[f'\\draw[line width=.8pt] (.55,3.0) circle (.12);',f'\\draw[line width=.8pt] (3.75,2.5) circle (.16);',lizozom(2.5,1.3,1.4)]
    b+=[bitki_hucre(5.6,.1,10.2,3.9),nukleus(6.65,2.85,.55),koful(8.4,2.2,1.2,.85),kloro(6.5,.95,6,1.3),kloro(8.4,.62,-4,1.3),kloro(9.5,1.5,70,1.2),mito(9.4,3.25,15,1.2)]
    b+=[lab('I',10.95,2.0,10.65,2.0,10.28,2.0),lab('II',6.5,-.8,6.5,-.45,6.5,.72),lab('III',8.4,4.75,8.4,4.4,8.4,3.02),
        lab('IV',2.95,4.65,2.95,4.3,2.95,2.9),lab('V',1.35,-.8,1.35,-.45,1.35,.58)]
    b.append('\\node[font=\\normalsize\\bfseries] at (2.3,-1.55) {X};\\node[font=\\normalsize\\bfseries] at (7.9,-1.55) {Y};')
    return tk('\n'.join(b),.82)
# --- F1b: aynı iki hücre, farklı yerleşim (Q8) ---
def sekil_f1b():
    b=[bitki_hucre(0,.1,4.6,3.9),nukleus(3.5,2.85,.55),koful(1.9,2.2,1.2,.85),kloro(3.6,.9,-6,1.3),kloro(1.7,.62,5,1.3),kloro(.85,1.5,75,1.2),mito(.85,3.25,-15,1.2)]
    b+=[hayvan_hucre(7.9,2.0,2.3,1.9,faz=1.6),nukleus(8.4,2.3,.6),sentrozom(7.0,2.8,-20,1.3),mito(8.9,.85,-12,1.3),mito(6.9,1.0,25,1.3)]
    b+=[f'\\draw[line width=.8pt] (6.1,2.4) circle (.14);',f'\\draw[line width=.8pt] (9.6,3.0) circle (.12);',f'\\draw[line width=.8pt] (9.8,1.7) circle (.1);',lizozom(7.6,1.3,1.4)]
    b+=[lab('I',-.9,2.0,-.6,2.0,-.08,2.0),lab('II',3.6,-.8,3.6,-.45,3.6,.65),lab('III',1.9,4.75,1.9,4.4,1.9,3.0),
        lab('IV',7.0,4.65,7.0,4.3,7.0,3.05),lab('V',8.9,-.8,8.9,-.45,8.9,.5)]
    b.append('\\node[font=\\normalsize\\bfseries] at (2.3,-1.55) {Y};\\node[font=\\normalsize\\bfseries] at (7.9,-1.55) {X};')
    return tk('\n'.join(b),.82)
# --- F2: üç hücre K, L, M ---
def sekil_f2():
    b=[]
    # K: bitki yaprak (duvar+kloroplast+koful)
    b+=[bitki_hucre(0,0,3.6,3.2),nukleus(.95,2.2,.42),koful(2.4,1.95,.85,.65),kloro(.9,.75,5,.85),kloro(2.4,.55,-5,.85),mito(2.95,2.65,20,.8)]
    # L: bitki kök (duvar+koful, kloroplast yok)
    X=4.6
    b+=[bitki_hucre(X,0,X+3.6,3.2),nukleus(X+.95,2.2,.42),koful(X+2.4,1.85,.9,.75),mito(X+.85,.7,10,.8),mito(X+2.7,.5,-15,.8)]
    # M: hayvan
    Z=9.3
    b+=[hayvan_hucre(Z+1.8,1.6,1.8,1.6,faz=1.1),nukleus(Z+1.2,1.85,.45),sentrozom(Z+2.35,2.1,10,.85),mito(Z+1.0,.7,10,.8),mito(Z+2.55,.75,-20,.8),
        lizozom(Z+2.4,1.1,.9),f'\\draw[line width=.8pt] ({Z+.6},2.5) circle (.1);',f'\\draw[line width=.8pt] ({Z+3.0},2.45) circle (.1);']
    b.append('\\node[font=\\large\\bfseries] at (1.8,-.55) {K};\\node[font=\\large\\bfseries] at (6.4,-.55) {L};\\node[font=\\large\\bfseries] at (11.1,-.55) {M};')
    return tk('\n'.join(b),.68)
# --- FH: hayvan hücresi, numaralı organeller (I çekirdek, II mitokondri, III Golgi, IV granüllü ER, V lizozom) ---
def sekil_fh():
    b=[hayvan_hucre(3.2,2.3,3.2,2.3,faz=.9),nukleus(2.0,2.9,.8),rer(2.1,1.15,-14,1.25,True,3,1.5),golgi(4.5,3.0,-10,1.15),mito(1.3,1.5,12,1.25),mito(5.3,.95,-20,1.25),
       lizozom(4.5,1.95,1.3)]
    b+=[nokta(5.0,2.4),nokta(5.15,2.1),nokta(3.3,3.65),nokta(3.55,3.8),nokta(1.0,2.4),nokta(.85,2.6)]
    b+=[lab('I',.2,5.4,.7,5.05,1.55,3.55),lab('II',-.95,.5,-.5,.7,.8,1.45),lab('III',6.9,4.7,6.45,4.4,4.95,3.2),
        lab('IV',3.2,-.75,3.2,-.4,3.2,.6),lab('V',7.75,2.3,7.35,2.2,4.75,2.0)]
    return tk('\n'.join(b),.85)
# --- F16: mitokondri (X) ve kloroplast (Y) iç yapı ---
def sekil_mk():
    b=[]
    # X: mitokondri (büyük): dış zar, iç zar kıvrımlı
    b.append('\\draw[line width=1.5pt,fill=black,fill opacity=.06] (2,2) ellipse (2.0 and 1.15);\\draw[line width=1.5pt] (2,2) ellipse (2.0 and 1.15);')
    iz=[(0.35,2.0),(.75,1.45),(.95,2.5),(1.3,1.0),(1.45,2.9),(1.95,1.0),(2.05,2.9),(2.6,1.0),(2.65,2.9),(3.0,1.5),(3.2,2.5),(3.55,2.0)]
    b.append('\\draw[line width=.9pt] (.55,2.0) '+' '.join(f'-- ({x},{y})' for x,y in [(.8,1.45),(1.0,2.45),(1.3,1.2),(1.55,2.75),(1.9,1.2),(2.15,2.75),(2.5,1.2),(2.75,2.75),(3.05,1.35),(3.25,2.5),(3.5,2.0)])+';')
    b.append('\\draw[line width=.9pt] (.15,2.0) ellipse (0 and 0);')
    b.append('\\draw[line width=.9pt] (2,2) ellipse (1.82 and .98);')
    # Y: kloroplast
    b.append('\\draw[line width=1.5pt,fill=black,fill opacity=.06] (7.6,2) ellipse (2.25 and 1.25);\\draw[line width=1.5pt] (7.6,2) ellipse (2.25 and 1.25);\\draw[line width=.9pt] (7.6,2) ellipse (2.07 and 1.07);')
    for cx in (6.4,7.6,8.8):
        for k in range(4):
            yy=1.5+.34*k
            b.append(f'\\draw[line width=.7pt,fill=black,fill opacity=.35] ({cx-.4},{yy-.13}) rectangle ({cx+.4},{yy+.13});')
    b.append('\\draw[line width=.5pt] (6.8,1.67)--(7.2,1.67) (8.0,1.67)--(8.4,1.67) (6.8,2.01)--(7.2,2.01) (8.0,2.01)--(8.4,2.01) (6.8,2.35)--(7.2,2.35) (8.0,2.35)--(8.4,2.35);')
    b.append('\\node[font=\\large\\bfseries] at (2,.2) {X};\\node[font=\\large\\bfseries] at (7.6,.2) {Y};')
    return tk('\n'.join(b),.8)

# --- FS: salgı proteini yolu ---
def sekil_fs():
    b=[hayvan_hucre(4.5,2.3,4.4,2.2,faz=.3),nukleus(7.0,3.0,.8),rer(5.4,.75,6,1.3,True,3,1.5),golgi(3.9,2.3,10,1.3),mito(2.3,.8,8,1.2),mito(7.6,1.7,-12,1.2)]
    for x,y in ((1.2,3.0),(1.7,2.4),(2.2,3.2),(1.5,1.7)): b.append(f'\\draw[line width=.9pt] ({x},{y}) circle (.17);')
    b+=[nokta(5.0,3.6),nokta(5.3,3.75),nokta(2.9,3.7)]
    b+=[lab('I',3.9,4.9,3.9,4.55,3.9,2.85),lab('II',6.2,-.8,6.2,-.45,6.2,.55),lab('III',1.3,4.9,1.45,4.55,1.7,3.45)]
    return tk('\n'.join(b),.85)
# --- FZ: hücre zarı kesiti (akıcı mozaik) ---
def sekil_fz():
    b=[]
    xs=[.5+.5*i for i in range(17)]
    ust=[x for x in xs if not (2.55<x<3.65 or 4.95<x<5.95)]
    alt=list(ust)
    ust=[x for x in ust if abs(x-8.0)>.2]
    b.append('\\fill '+' '.join(f'({x},3.0) circle (.16)' for x in ust)+' '+' '.join(f'({x},.4) circle (.16)' for x in alt)+';')
    b.append('\\draw[line width=.8pt] '+' '.join(f'({x-.07},2.82)--({x-.07},2.05) ({x+.07},2.82)--({x+.07},2.05)' for x in ust)+' '+' '.join(f'({x-.07},.58)--({x-.07},1.35) ({x+.07},.58)--({x+.07},1.35)' for x in alt)+';')
    b.append('\\draw[line width=1.1pt,fill=black,fill opacity=.12,rounded corners=4pt] (2.6,.1) rectangle (3.6,3.3);\\draw[line width=1.1pt,rounded corners=4pt] (2.6,.1) rectangle (3.6,3.3);')
    b.append('\\draw[line width=.7pt,dashed] (3.1,.5)--(3.1,2.9);')
    b.append('\\draw[line width=1.1pt,fill=black,fill opacity=.12,rounded corners=4pt] (5.0,.15) rectangle (5.9,3.25);\\draw[line width=1.1pt,rounded corners=4pt] (5.0,.15) rectangle (5.9,3.25);')
    b.append('\\draw[line width=1.0pt] (5.45,3.25)--(5.45,3.65)--(5.2,3.9)--(5.2,4.2) (5.45,3.65)--(5.75,3.95)--(5.75,4.25);')
    b.append('\\draw[line width=.8pt,fill=white] '+' '.join(f'({x},{y}) circle (.1)' for x,y in ((5.45,3.65),(5.2,4.2),(5.75,4.25),(5.2,3.9)))+';')
    b.append('\\draw[line width=1.1pt,fill=black,fill opacity=.12] (7.15,-.25) ellipse (.8 and .35);')
    b.append('\\draw[line width=1.1pt] (7.15,-.25) ellipse (.8 and .35);')
    b.append('\\draw[line width=1pt,fill=black,fill opacity=.45,rounded corners=2pt] (7.85,2.0) rectangle (8.15,2.75);\\fill (8.0,2.9) circle (.12);\\draw[line width=.7pt] (8.0,2.0)--(8.0,1.7);')
    b+=[lab('I',.5,5.0,.75,4.7,.8,3.3),lab('II',3.1,-1.7,3.1,-1.35,3.1,.05),lab('III',6.6,4.95,6.3,4.65,5.8,4.15),lab('IV',9.4,3.95,9.0,3.8,8.25,2.8),lab('V',7.15,-1.7,7.15,-1.35,7.15,-.62)]
    b.append('\\node[font=\\footnotesize,anchor=west] at (9.2,3.0) {hücre dışı};\\node[font=\\footnotesize,anchor=west] at (9.2,.4) {sitoplazma};')
    return tk('\n'.join(b),.8)


# --- FG: üç madde geçişi (I basit, II kolaylaştırılmış, III aktif) ---
def sekil_fg():
    b=[]
    def panel(ox,ust_n,alt_n,protein,yon,atp,etiket):
        o=f'\\draw[line width=1.3pt] ({ox},1.6)--({ox+3.3},1.6);\\draw[line width=1.3pt] ({ox},2.1)--({ox+3.3},2.1);'
        o+='\\draw[line width=.5pt] '+' '.join(f'({ox+.15+.3*i:.2f},1.6)--({ox+.15+.3*i:.2f},2.1)' for i in range(11))+';'
        if protein:
            o+=f'\\draw[line width=1.1pt,fill=white,rounded corners=3pt] ({ox+1.2},1.45) rectangle ({ox+2.1},2.25);\\draw[line width=.6pt,dashed] ({ox+1.65},1.55)--({ox+1.65},2.15);'
        pu=[(.3,3.0),(1.0,3.5),(1.6,2.9),(2.3,3.4),(2.9,2.85),(.7,2.7),(1.2,3.7),(2.7,3.7)]
        pa=[(.55,.9),(1.4,.45),(2.5,.8),(2.1,.3),(.4,.35),(2.95,.4),(1.0,1.0),(1.9,.9)]
        for (x,y) in pu[:ust_n]: o+=nokta(ox+x,y,.09)
        for (x,y) in pa[:alt_n]: o+=nokta(ox+x,y,.09)
        if yon<0: o+=f'\\draw[{OKU},line width=1.1pt] ({ox+1.65},3.0)--({ox+1.65},1.0);'
        else: o+=f'\\draw[{OKU},line width=1.1pt] ({ox+1.65},1.0)--({ox+1.65},3.0);'
        if atp: o+=f'\\node[font=\\footnotesize,anchor=west] at ({ox+2.2},2.75) {{ATP $\\rightarrow$ ADP + P}};'
        o+=f'\\node[font=\\large\\bfseries] at ({ox+1.65},-.85) {{{etiket}}};'
        return o
    b.append(panel(0,8,2,False,-1,False,'I'))
    b.append(panel(4.0,8,2,True,-1,False,'II'))
    b.append(panel(8.0,2,8,True,1,True,'III'))
    return tk('\n'.join(b),.78)
# --- FE: endositoz (X) ve ekzositoz (Y) ---
def sekil_fe():
    b=[]
    b.append('\\draw[line width=1.5pt] (0,6.2)--(.7,6.2) to[out=0,in=100] (1.0,5.3) to[out=-80,in=-100,looseness=1.5] (2.2,5.3) to[out=80,in=180] (2.5,6.2)--(5.2,6.2);')
    b.append('\\fill[black!60] (1.6,5.75) circle (.33);')
    b.append('\\draw[line width=1.5pt] (3.6,4.3) circle (.62);\\fill[black!60] (3.6,4.3) circle (.3);')
    b.append(f'\\draw[{OKU},line width=1pt] (2.4,5.1) to[bend left=25] (3.1,4.7);')
    b.append('\\node[font=\\normalsize\\bfseries] at (-.55,5.6) {X};')
    dy=-1.9
    def Y(x,y): return f'({x},{y+dy:.2f})'
    b.append('\\draw[line width=1.5pt] '+Y(0,2.2)+'--'+Y(2.9,2.2)+' to[out=0,in=-110] '+Y(3.3,3.0)+' to[out=70,in=200] '+Y(3.55,3.15)+';')
    b.append('\\draw[line width=1.5pt] '+Y(4.05,3.15)+' to[out=-20,in=110] '+Y(4.3,3.0)+' to[out=-70,in=180] '+Y(4.7,2.2)+'--'+Y(5.2,2.2)+';')
    b.append('\\draw[line width=1.5pt] '+Y(.9,.9)[:-1]+') circle (.55);\\fill[black!60] '+' '.join(f'{Y(x,y)} circle (.1)' for x,y in ((.7,.9),(1.0,1.0),(.9,.7)))+';')
    b.append('\\fill[black!60] '+' '.join(f'{Y(x,y)} circle (.1)' for x,y in ((3.65,3.6),(4.0,3.85),(3.8,4.2)))+';')
    b.append(f'\\draw[{OKU},line width=1pt] '+Y(1.6,1.2)+' to[bend left=25] '+Y(3.1,1.95)+';')
    b.append('\\node[font=\\normalsize\\bfseries] at (-.55,%.2f) {Y};'%(2.0+dy))
    b.append('\\node[font=\\footnotesize,anchor=west] at (5.35,6.5) {hücre dışı};\\node[font=\\footnotesize,anchor=west] at (5.35,5.45) {sitoplazma};')
    b.append('\\node[font=\\footnotesize,anchor=west] at (5.35,%.2f) {hücre dışı};\\node[font=\\footnotesize,anchor=west] at (5.35,%.2f) {sitoplazma};'%(2.7+dy,1.5+dy))
    return tk('\n'.join(b),.8)


import random
FP_F=(1.0,.72,.45)          # Q26: hücre zarı büzülme oranı (I, II, III)
G21=dict(egim=.7,vmax=3.1,km=.7)  # Q21: I doğrusal, II doyumlu
G25_SON=(.95,3.1,2.0)        # Q25: I, II, III eğrilerinin son hacmi (başlangıç 2,0)
# --- FO: osmometre düzeneği ---
def sekil_fo():
    rng=random.Random(5)
    def ic(y): # huni gövdesinin y'deki iç x aralığı
        if y<=2.5: return (.9+(y-.9)/1.6*1.1,3.5-(y-.9)/1.6*1.1)
        return (2.0,2.4)
    def dag(n,uygun,mes=.34):
        out=[]
        for _ in range(4000):
            x=rng.uniform(.1,4.3); y=rng.uniform(.1,5.0)
            if uygun(x,y) and all((x-a)**2+(y-b_)**2>mes**2 for a,b_ in out): out.append((x,y))
            if len(out)==n: return out
        raise RuntimeError('dağıtılamadı')
    def icte(x,y):
        if not (1.0<y<2.4): return False
        a,b_=ic(y); return a+.2<x<b_-.2 if y>2.5 else a+.2<x<b_-.2
    def disar(x,y):
        if y>2.45 or y<.15: return False
        if x<.15 or x>4.25: return False
        # huni dışında
        if y>=.8:
            a,b_=ic(min(y,2.5)) if y<=2.5 else (2.0,2.4)
            if a-.25<x<b_+.25: return False
        return True
    b=[]
    b.append('\\fill[black!7] (0,0) rectangle (4.4,2.6);')
    b.append('\\fill[black!14] (.9,.9)--(3.5,.9)--(2.4,2.5)--(2.4,2.6)--(2.0,2.6)--(2.0,2.5)--cycle;')
    b.append('\\draw[line width=1.5pt] (0,3.4)--(0,0)--(4.4,0)--(4.4,3.4);')
    b.append('\\draw[line width=1.5pt] (.9,.9)--(2.0,2.5)--(2.0,5.3) (3.5,.9)--(2.4,2.5)--(2.4,5.3);')
    b.append('\\draw[line width=2.4pt,dash pattern=on 4pt off 2.5pt] (.9,.9)--(3.5,.9);')
    b.append('\\draw[line width=.8pt] (2.4,2.6)--(2.7,2.6);')
    for x,y in dag(11,icte): b.append(nokta(x,y,.075))
    for x,y in dag(3,disar,.6): b.append(nokta(x,y,.075))
    b.append('\\node[font=\\footnotesize,anchor=west] at (2.85,3.8) {başlangıç düzeyi};\\draw[line width=.6pt] (3.0,3.65)--(2.65,2.7);')
    b.append('\\node[font=\\footnotesize,anchor=west,align=left] at (4.75,2.0) {\\%30 sakaroz\\\\çözeltisi};\\draw[line width=.6pt] (4.7,1.85)--(2.7,1.7);')
    b.append('\\node[font=\\footnotesize,anchor=west,align=left] at (4.75,.95) {\\%5 sakaroz\\\\çözeltisi};\\draw[line width=.6pt] (4.7,.95)--(4.1,.95);')
    b.append('\\node[font=\\footnotesize,anchor=west,align=left] at (4.75,.1) {yarı geçirgen zar};\\draw[line width=.6pt] (4.7,.15)--(3.4,.85);')
    return tk('\n'.join(b),.85)
# --- FP: üç bitki hücresi (plazmoliz derecesi) ---
def sekil_fp():
    b=[]
    for i,(f,et) in enumerate(zip(FP_F,('I','II','III'))):
        ox=3.8*i; cx,cy=ox+1.5,1.3
        b.append(f'\\draw[rounded corners=8pt,line width=2.2pt] ({ox},0) rectangle ({ox+3},2.6);')
        w,h=1.3*f+ (.05 if f==1 else 0),1.0*f+(.05 if f==1 else 0)
        b.append(f'\\draw[rounded corners={12 if f<1 else 8}pt,line width=.9pt] ({cx-w*1.0-(.0 if f<1 else .0):.2f},{cy-h*1.1:.2f}) rectangle ({cx+w:.2f},{cy+h*1.1:.2f});' if f<1 else '')
        kx,ky=(.95*f,.62*f) if f<1 else (1.0,.7)
        b.append(f'\\draw[line width=.8pt,dashed,fill=black,fill opacity=.06] ({cx+.12*f:.2f},{cy-.1*f:.2f}) ellipse ({kx:.2f} and {ky:.2f});')
        b.append(f'\\draw[line width=.9pt,fill=white] ({cx-.7*f-.05:.2f},{cy+.45*f+.05:.2f}) circle ({.2+.08*f:.2f});\\fill ({cx-.7*f-.05:.2f},{cy+.45*f+.05:.2f}) circle (.06);')
        b.append(f'\\node[font=\\large\\bfseries] at ({ox+1.5},-.6) {{{et}}};')
    return tk('\n'.join(b),.85)
# --- FHM: üç alyuvar ---
def sekil_fhm():
    b=[]
    # I: büzüşmüş (dikenli)
    pts=[]
    for k in range(24):
        r=.95 if k%2==0 else .78; t=2*math.pi*k/24; pts.append((1.5+r*math.cos(t),1.5+r*math.sin(t)))
    b.append('\\draw[line width=1.3pt,fill=black,fill opacity=.15] '+' -- '.join(f'({x:.2f},{y:.2f})' for x,y in pts)+' -- cycle;')
    # II: normal çukur disk
    b.append('\\draw[line width=1.5pt,fill=black,fill opacity=.15] (5.1,1.5) circle (1.0);\\draw[line width=.9pt] (5.1,1.5) circle (1.0);\\draw[line width=.9pt] (5.1,1.5) circle (.42);')
    # III: şişmiş ve parçalanmış
    cx=8.7
    for a0,a1 in ((15,150),(172,262),(285,345)):
        b.append(f'\\draw[line width=1.5pt] ({cx},1.5)+({a0}:1.3) arc ({a0}:{a1}:1.3);')
    for x,y in ((cx-.4,1.7),(cx+.3,1.2),(cx+.1,1.9),(cx-.2,1.0),(cx+1.55,2.3),(cx+1.6,.5),(cx-1.55,2.2),(cx-.1,-.1),(cx+.5,3.0)): b.append(nokta(x,y,.07))
    for et,x in (('I',1.5),('II',5.1),('III',cx)): b.append(f'\\node[font=\\large\\bfseries] at ({x},-.7) {{{et}}};')
    return tk('\n'.join(b),.8)
# --- grafik yardımcıları ---
def eksen(W,Hh,xl,yl):
    return (f'\\draw[{OKU},line width=1pt] (0,0)--({W+.3},0);\\draw[{OKU},line width=1pt] (0,0)--(0,{Hh+.3});'
            f'\\node[font=\\footnotesize,anchor=north] at ({W/2},-.15) {{{xl}}};\\node[font=\\footnotesize,rotate=90,anchor=south] at (-.15,{Hh/2}) {{{yl}}};')
def egri(pts,lw=1.5,dash=''):
    return f'\\draw[line width={lw}pt{dash}] plot[smooth] coordinates {{'+' '.join(f'({x:.2f},{y:.2f})' for x,y in pts)+'};'
# --- G21: taşıma hızı – derişim farkı ---
def sekil_g21():
    xs=[0,.3,.6,1,1.5,2,3,4,5]
    I=[(x,G21['egim']*x) for x in (0,5)]; II=[(x,G21['vmax']*x/(x+G21['km'])) for x in xs]
    b=[eksen(5,3.9,'Derişim farkı','Taşıma hızı'),egri(I) if False else f'\\draw[line width=1.5pt] (0,0)--(5,3.5);',egri(II,1.5,',dashed')]
    b.append(f'\\node[font=\\normalsize\\bfseries] at (5.45,3.55) {{I}};\\node[font=\\normalsize\\bfseries] at (5.5,{II[-1][1]:.2f}) {{II}};')
    return tk('\n'.join(b),.95)
# --- G25: hayvan hücresi hacmi – zaman ---
def sekil_g25():
    ts=[0,.5,1,1.7,2.5,3.5,4.5,6]
    f=lambda t,s,e:s+(e-s)*(1-math.exp(-t/1.2))
    I=[(t,f(t,2,G25_SON[0])) for t in ts]; II=[(t,f(t,2,G25_SON[1])) for t in ts]
    b=[eksen(6,3.8,'Zaman','Hücre hacmi'),'\\draw[line width=.6pt,dotted] (0,2)--(6,2);']
    b+=[egri(I),egri(II,1.5,',dashed'),'\\draw[line width=1.5pt,dash pattern=on 1pt off 2pt] (0,2)--(6,2);']
    b.append(f'\\node[font=\\normalsize\\bfseries] at (6.45,{I[-1][1]:.2f}) {{I}};\\node[font=\\normalsize\\bfseries] at (6.45,{II[-1][1]:.2f}) {{II}};\\node[font=\\normalsize\\bfseries] at (6.5,{G25_SON[2]}) {{III}};')
    return tk('\n'.join(b),.95)
# --- G29: bitki ve hayvan hücresi hacmi – zaman (aynı çözelti) ---
def sekil_g29():
    ts=[0,.5,1,1.7,2.5,3.5,5,6.5]
    K=[(t,2+.4*(1-math.exp(-t*1.25))) for t in ts]
    L=[(t,2+.5*t) for t in (0,1,2,3,4)]
    b=[eksen(6.5,4.6,'Zaman','Hücre hacmi'),egri(K,1.5,',dashed'),f'\\draw[line width=1.5pt] (0,2)--(4,4);']
    b.append('\\draw[line width=1.5pt] (3.85,3.85)--(4.15,4.15);\\draw[line width=1.5pt] (3.85,4.15)--(4.15,3.85);')
    b.append(f'\\node[font=\\normalsize\\bfseries] at (7.0,{K[-1][1]:.2f}) {{K}};\\node[font=\\normalsize\\bfseries] at (3.5,4.3) {{L}};')
    b.append('\\node[font=\\footnotesize,anchor=west] at (4.5,4.5) {$\\times$ : hücre parçalanmıştır};')
    return tk('\n'.join(b),.9)

# ==SORULAR==
SK={}
# ===================================== SORULAR =====================================
# ---- 01 · hücre adı (kolay) ----
BILGI_TEORI=B('Hücre teorisi','Hücre teorisi, birçok bilim insanının gözlem ve çıkarımlarının zaman içinde birleşmesiyle oluşmuştur')
qt(1,[A('Gözlemi çöz','Şişe mantarı kesitinde görülen arı peteği benzeri odacıklar, ölü bitki dokusunun hücre duvarlarıdır; bu odacıkları ilk kez adlandıran bilim insanı aranıyor.','Gözlem: mantar kesiti · Ad verme'),
      A('Katkıları ayır','Hücreyi adlandırmak, canlı hücreleri gözlemek, bitki ve hayvanların hücreden oluştuğunu belirtmek ve hücrenin hücreden oluştuğunu belirtmek farklı bilim insanlarının katkılarıdır.','Adlandırma ≠ teorinin ilkeleri'),
      A('Bilim insanını seç','Mikroskopla mantar kesitini inceleyip gördüklerine hücre adını veren bilim insanı Robert Hooke’tur.','Robert Hooke')],
 tek('C','Robert Hooke',[('Anton van Leeuwenhoek','Mikroskopla canlı tek hücreli organizmaları ve spermleri gözlediğini bilip hücre adını da onun verdiğini sanmış.','bilgi'),
   ('Matthias Schleiden','Bitkilerin hücrelerden oluştuğunu belirtmesini hücrenin adlandırılmasıyla karıştırmış.','bilgi'),
   ('Theodor Schwann','Hayvan dokularının hücrelerden oluştuğunu belirtmesini hücreyi adlandırmakla karıştırmış.','bilgi'),
   ('Rudolf Virchow','Hücrelerin kendinden önceki hücrelerden oluştuğunu belirtmesini hücrenin adlandırılması sanmış.','bilgi')]),
 'hücreyi adlandıran bilim insanı','hücre adı ve gözlem','Hücre kavramı mikroskopla yapılan ilk gözlemlerle ortaya çıkmıştır; adı koyan bilim insanı gözlemin kendisinden bilinir.','Hücreyi ilk gözleyip adlandıran ile hücre teorisinin ilkelerini belirten bilim insanlarını karıştırmak.',
 alt='Hücre teorisi ve tarihçe',z='kolay',kalip='düz',kaz='Hücre kavramını ortaya koyan bilim insanını belirler.',
 metin='17. yüzyılda bir bilim insanı, mikroskobuyla ince bir şişe mantarı kesitini inceliyor ve kesitte arı peteğini andıran küçük odacıklar görüyor. Bu odacıklara, küçük oda anlamına gelen bir sözcükten türeyen bir ad veriyor ve bu ad sonraki yıllarda canlıların yapı birimi için de kullanılıyor.\nBuna göre, hücre adını ilk kez kullanan bilim insanı aşağıdakilerden hangisidir?',
 istenen='Hücre adını ilk kez kullanan bilim insanı.',ip=['Gözlemin hangi doku üzerinde yapıldığına bak; adlandırma ile hücre teorisine katkı farklı şeylerdir.'],bilgi=[BILGI_TEORI],
 puf='Mantar kesitinde odacıkları görüp “hücre” diyen Hooke’tur; bitki, hayvan ve hücreden hücre fikri sonraki bilim insanlarına aittir.')
# ---- 02 · hücre teorisi ilkeleri (orta, yanlış öncüller) ----
d2={'I':(True,'Bütün canlılar bir ya da daha fazla hücreden oluşur; bu, hücre teorisinin ilk ilkesidir.','ilke'),
    'II':(False,'Hücreler yalnızca daha önce var olan hücrelerin bölünmesiyle oluşur; cansız maddeden kendiliğinden oluşmaz.','ilke değil'),
    'III':(False,'Hücre, tek hücreli canlılar dahil bütün canlıların yapı ve görev birimidir.','ilke değil')}
qo(2,onc(d2,'D','yanlis','ilke dışı'),'teori ilkeleri ve yanlış öncül','hücre teorisinin ilkeleri',
 'Üç öncülden hangilerinin teorinin ilkesi olmadığı sorulur; yanlış öncüller teorinin tersini söyler.','Hücrenin cansızdan kendiliğinden oluştuğunu ya da yalnız çok hücrelilerin birimi olduğunu doğru saymak.',
 alt='Hücre teorisi ve tarihçe',z='orta',kalip='öncüllü',kaz='Hücre teorisinin ilkelerini ayırt eder.',
 metin='Hücre teorisi, birçok bilim insanının gözlem ve çıkarımlarının birleştirilmesiyle oluşmuştur. Teorinin günümüzde kabul gören ilkeleri üzerine çalışan bir öğrenci, defterine aşağıdaki ifadeleri yazıyor.\nI. Canlılar bir ya da daha fazla hücreden oluşur.\nII. Yeni hücreler, cansız maddelerden kendiliğinden meydana gelir.\nIII. Hücre, yalnızca çok hücreli canlıların yapı ve görev birimidir.\nBuna göre, bu ifadelerden hangilerinin hücre teorisinin ilkeleri arasında yer aldığı söylenemez?',
 istenen='Hücre teorisinin ilkesi olmayan ifadeler.',ip=['Her ifadeyi, bildiğin hücre teorisi ilkeleriyle tek tek karşılaştır.'],bilgi=[BILGI_TEORI],
 puf='Hücre teorisinin üç ilkesini bil: canlı hücreden oluşur, hücre yapı-görev birimidir, hücre hücreden oluşur.')
# ---- 03 · bilim insanı katkıları (orta, doğru öncüller) ----
d3={'I':(False,'Bitki dokularının hücrelerden oluştuğunu belirten Schleiden’dir; Schwann hayvan dokuları için aynı sonuca ulaşmıştır.'),
    'II':(True,'Schleiden, bitkilerin hücrelerden oluştuğunu ileri sürmüştür.'),
    'III':(False,'Virchow, her hücrenin kendinden önceki bir hücreden oluştuğunu belirtmiştir; cansızdan kendiliğinden oluşum fikrine karşı çıkmıştır.')}
qo(3,onc(d3,'B','dogru'),'bilim insanı–katkı eşleştirme','Schleiden, Schwann, Virchow katkıları',
 'Bilim insanı ve katkı eşleştirmelerinde yalnız bir eşleşme doğrudur; diğerleri bitki–hayvan ya da kendiliğinden oluşumla karıştırılmıştır.','Schleiden ile Schwann’ı ve Virchow’un ilkesini birbirine karıştırmak.',
 alt='Hücre teorisi ve tarihçe',z='orta',kalip='öncüllü',kaz='Hücre teorisine katkıda bulunan bilim insanlarını katkılarıyla eşleştirir.',
 metin='Bir hücre biyolojisi kitabında, hücre teorisinin gelişimine katkıda bulunan bilim insanları ve katkıları aşağıdaki gibi eşleştirilmiştir.\nI. Schwann: Bitki dokularının hücrelerden oluştuğunu belirtmiştir.\nII. Schleiden: Bitkilerin hücrelerden oluştuğunu ileri sürmüştür.\nIII. Virchow: Hücrelerin cansız maddeden kendiliğinden oluştuğunu savunmuştur.\nBuna göre, bu eşleştirmelerden hangileri doğrudur?',
 istenen='Doğru eşleştirilen bilim insanı–katkı çiftleri.',ip=['Her bilim insanının hangi konuda çalıştığını hatırla ve eşleşmeleri tek tek sına.'],bilgi=[BILGI_TEORI],
 puf='Schleiden = bitki, Schwann = hayvan, Virchow = hücreden hücre; her isme tek anahtar sözcük bağla.')
# ---- 04 · prokaryot-ökaryot tablo (orta) ----
OZ={'Bakteri':dict(cz=0,mi=0,hd=1,kl=0,ri=1),'Hayvan':dict(cz=1,mi=1,hd=0,kl=0,ri=1),'Mantar':dict(cz=1,mi=1,hd=1,kl=0,ri=1),'Bitki':dict(cz=1,mi=1,hd=1,kl=1,ri=1)}
assert len({tuple(v.items()) for v in OZ.values()})==4
SIRA4=['Hayvan','Mantar','Bakteri','Bitki']
def tab4():
    ad=[('Çekirdek zarı','cz'),('Mitokondri','mi'),('Hücre duvarı','hd'),('Kloroplast','kl'),('Ribozom','ri')]
    sat=[[a]+['+' if OZ[h][k] else '−' for h in SIRA4] for a,k in ad]
    return tablo_svg(['Yapı','X','Y','Z','T'],sat)
SK[4]=tab4()
dog4=' – '.join(SIRA4)
qt(4,[A('Prokaryotu bul','Çekirdek zarı ve mitokondrisi olmayan hücre prokaryottur; bu hücre Z’dir ve bakteridir.','Z: bakteri'),
      A('Hücre duvarsızı bul','Ökaryot hücreler arasında hücre duvarı taşımayan tek hücre hayvan hücresidir.','X: hayvan'),
      A('Kloroplastlıyı bul','Kloroplast yalnız bitki yaprağı hücresi gibi ışıkla fotosentez yapan hücrelerde bulunur.','T: bitki'),
      A('Kalanı belirle','Çekirdek zarı, mitokondri ve hücre duvarı olup kloroplastı olmayan hücre mantar hücresidir.','Y: mantar')],
 tek('A',dog4,[('Mantar – Hayvan – Bakteri – Bitki','Hücre duvarının hayvan hücresinde, duvarsızlığın mantarda olduğunu sanıp X ile Y’yi karıştırmış.','bilgi'),
   ('Hayvan – Bitki – Bakteri – Mantar','Kloroplast satırına bakmayıp Y ve T’yi yer değiştirmiş.','dikkat'),
   ('Bakteri – Mantar – Hayvan – Bitki','Çekirdek zarı ve mitokondri satırını dikkate almadan prokaryotu X sanmış.','dikkat'),
   ('Hayvan – Mantar – Bitki – Bakteri','Hücre duvarı olan hücreleri ayırt etmeden Z ile T’yi karıştırmış.','bilgi')]),
 'dört hücrenin yapı tablosu','tablodan hücre türünü belirleme','Yapıların bulunup bulunmama örüntüsü: çekirdek zarı yok → prokaryot; duvar yok → hayvan; kloroplast var → bitki; kalan duvarlı hücre → mantar.','Mantar hücresini hayvan ya da bitki hücresiyle karıştırmak.',
 alt='Prokaryot ve ökaryot hücre',z='orta',kalip='tablo',kaz='Yapı tablosundan hücre türünü belirler.',sekil=SK[4],
 metin='Tabloda bir bakteri, bir mantar, bir bitki yaprağı ve bir hayvan hücresinde bazı yapıların bulunup bulunmadığı gösterilmiştir (+: var, −: yok). Hücreler rastgele X, Y, Z ve T harfleriyle adlandırılmıştır.\nBuna göre, X, Y, Z ve T hücreleri sırasıyla aşağıdakilerden hangisinde doğru verilmiştir?',
 istenen='X, Y, Z ve T hücrelerinin türleri.',ip=['Önce çekirdek zarına, sonra hücre duvarına ve kloroplasta bakarak hücreleri tek tek ayır.'],
 bilgi=[B('Hücre türlerinin yapısı','Prokaryot hücrede (bakteri) çekirdek zarı ve zarlı organel yoktur · Ökaryot hücrede (bitki, hayvan, mantar) vardır · Hücre duvarı bakteri, mantar ve bitkide bulunur; hayvan hücresinde bulunmaz')],
 puf='Tabloda önce çekirdek zarsız hücreyi (prokaryot), sonra duvarsızı (hayvan), sonra kloroplastlıyı (bitki) ayır; kalan mantardır.')
# ---- 05 · bakteri öncüllü (kolay) ----
d5={'I':(True,'Prokaryot hücrede çekirdek zarı yoktur; DNA sitoplazmada bulunur.'),
    'II':(False,'Prokaryot hücrede zarla çevrili organel bulunmaz; tek organeli ribozomdur.'),
    'III':(True,'Ribozom prokaryot hücrede de bulunur ve protein sentezini yapar.')}
qo(5,onc(d5,'C','dogru'),'bakteri hücresi bilgileri','prokaryot hücre özellikleri',
 'Bakteri hücresinin DNA’sının yeri, organelleri ve ribozomu üç öncülle sorulur.','Bakteride de zarlı organel (mitokondri gibi) bulunduğunu sanmak.',
 alt='Prokaryot ve ökaryot hücre',z='kolay',kalip='öncüllü',kaz='Prokaryot hücrenin yapısal özelliklerini ayırt eder.',
 metin='Bir bakteri hücresiyle ilgili öğrenciler tarafından aşağıdaki bilgiler veriliyor.\nI. Kalıtım materyali sitoplazmada bulunur.\nII. Zarla çevrili organelleri vardır.\nIII. Proteinleri ribozomlarında sentezler.\nBuna göre, bu bilgilerden hangileri doğrudur?',
 istenen='Bakteri hücresi için doğru olan bilgiler.',ip=['Bakteri prokaryottur; ökaryottaki çekirdek zarı ve zarlı organellerin bakteride bulunup bulunmadığını düşün.'],
 bilgi=[B('Ökaryot hücre','Ökaryot hücrede (bitki, hayvan, mantar) kalıtım materyali çekirdek zarıyla çevrilidir ve zarlı organeller (ER, Golgi, mitokondri gibi) bulunur')],
 puf='Prokaryotta çekirdek zarı ve zarlı organel yoktur; ortak yapılar zar, sitoplazma, DNA ve ribozomdur.')
# ---- 06 · siyanobakteri (kolay, olumsuz) ----
qt(6,[A('Hücreyi tanı','Siyanobakteri prokaryot bir hücredir; çekirdek zarı ve zarlı organel (kloroplast dahil) bulundurmaz.','prokaryot'),
      A('Doğru bilgileri ele','Hücre zarı, ribozom ve fotosentez pigmenti bu hücrede bulunur; DNA çekirdek zarıyla çevrili değildir.','Doğru bilgiler: zar, ribozom, DNA, pigment'),
      A('Söylenemeyeni seç','Kloroplast zarlı bir organeldir; prokaryot hücrede bulunmaz, bu yüzden fotosentez kloroplastta yapılamaz.','Kloroplastta fotosentez → söylenemez')],
 tek('E','Fotosentezi kloroplastlarında gerçekleştirir.',[('Hücre zarı ile çevrilidir.','Hücre zarını yalnız ökaryotlara özgü sanıp bu doğru bilgiyi söylenemez saymış.','bilgi'),
   ('Ribozomları protein sentezinde görev alır.','Prokaryotta ribozom olmadığını sanıp bu doğru bilgiyi söylenemez saymış.','bilgi'),
   ('Kalıtım materyali çekirdek zarıyla çevrili değildir.','Prokaryot hücrede çekirdek zarı bulunduğunu sanıp bu doğru bilgiyi söylenemez saymış.','bilgi'),
   ('Işık enerjisini kullanabilmesini sağlayan pigmentleri vardır.','Fotosentez için kloroplast gerektiğini düşünüp pigmentin kloroplastsız hücrede olamayacağını sanmış.','bilgi')]),
 'siyanobakteri hücresi bilgileri','kloroplastsız fotosentez','Fotosentez yapan her hücrede kloroplast bulunmaz; siyanobakteri prokaryottur ve zarlı organeli yoktur.','Fotosentez yapan her hücrenin kloroplast taşıdığını sanmak.',
 alt='Prokaryot ve ökaryot hücre',z='kolay',kalip='hikâyeli',kaz='Fotosentez yapan prokaryotun yapısını ökaryotla karşılaştırır.',
 metin='Siyanobakteriler (mavi-yeşil bakteriler), ışık enerjisini kullanarak organik madde üretebilen prokaryot canlılardır. Bir öğrenci, bir siyanobakteri hücresinin yapısını incelemek üzere hazırlık yapıyor.\nBuna göre, bu hücre ile ilgili aşağıdaki bilgilerden hangisi söylenemez?',
 istenen='Siyanobakteri hücresi için doğru olmayan bilgi.',ip=['Hücrenin hangi türe ait olduğunu düşün.'],
 bilgi=[B('Hücre türleri','Hücreler yapılarına göre prokaryot ve ökaryot olmak üzere iki ana gruba ayrılır; bakteriler prokaryot hücrelidir')],
 puf='Zarlı organel = ökaryot; prokaryot fotosentez yapsa da kloroplastı yoktur.')
# ---- 07 · F1 duvar (kolay) ----
SK[7]=sekil_f1()
qt(7,[A('Yapıları tanı','Y hücresinde dıştaki kalın çizgi hücre duvarı, yığınlı içli yapı kloroplast, kesikli çizgili büyük boşluk koful; X hücresindeki T biçimli yapı sentrozom, kıvrımlı içli oval yapı mitokondridir.','I: duvar · II: kloroplast · III: koful · IV: sentrozom · V: mitokondri'),
      A('Görevi eşleştir','Hücre zarının dışında yer alıp bitki hücresine şekil kazandıran yapı hücre duvarıdır.','Hücre duvarı'),
      A('Numarayı seç','Hücre duvarı şekilde I numarasıyla gösterilmiştir.','I')],
 dict(dogru='I',yan=[('II','II numaralı yapı kloroplasttır; sitoplazmada bulunur, hücreye şekil vermez; ışık enerjisini kullanır.','bilgi'),('III','III numaralı yapı kofuldur; hücre içinde su ve madde depolar.','bilgi'),('IV','IV numaralı yapı sentrozomdur; hayvan hücresinde bölünmeye yardım eder ve hücre zarının dışında değildir.','bilgi'),('V','V numaralı yapı mitokondridir; ATP üretir ve hücre içinde bulunur.','bilgi')],sira=['I','II','III','IV','V']),
 'duvar tanıma','bitki–hayvan hücresi şeması','Bitki hücresinde zarın dışında yer alan, şekil veren yapı hücre duvarıdır; biçimi kalın dış çizgi olarak ayırt edilir.','Hücre duvarını kloroplast ya da kofulla karıştırmak.',
 alt='Hayvan ve bitki hücresi farkları',z='kolay',kalip='şekilli',kaz='Bitki hücresindeki duvarı şekilde tanır.',sekil=SK[7],
 metin='Şekildeki X hücresi bir hayvana, Y hücresi ise bir bitkiye aittir. Bu hücrelerdeki bazı yapılar I, II, III, IV ve V ile numaralandırılmıştır.\nBuna göre, numaralı yapılardan hangisi, bitki hücresinde hücre zarının dışında bulunur ve hücrenin şeklini korumasına yardımcı olur?',
 istenen='Hücre zarının dışındaki koruyucu yapının numarası.',ip=['Hayvan hücresinde bulunmayan yapıları karşılaştır.'],
 bilgi=[B('Bitki hücresinin yapıları','Bitki hücresinin zarı, selülozdan yapılmış bir hücre duvarıyla çevrilidir · İçinde büyük merkezî koful ve ışıkla beslenen hücrelerde kloroplast bulunur')],
 puf='Şekilde en dıştaki kalın çizgi hücre duvarıdır; hayvan hücresinde zarın dışında yapı yoktur.')
# ---- 08 · F1b öncüllü (orta) ----
SK[8]=sekil_f1b()
d8={'I':(True,'Hücre duvarı ve kloroplast bitki hücresine özgüdür; hayvan hücrelerinde bulunmaz.'),
    'II':(False,'Koful hayvan hücrelerinde de bulunur (küçük ve çok sayıda); yalnızca bitki hücresine özgü değildir.'),
    'III':(True,'Mitokondri hem hayvan hem bitki hücresinde bulunur; şekilde Y hücresinde de vardır.')}
qo(8,onc(d8,'D','dogru'),'şekilde numaralı yapılar ve öncüller','bitki ve hayvan hücresi yapıları',
 'Aynı şemada bitkiye özgü yapılar, koful ve mitokondri öncüllerle sınanır.','Kofulun hayvan hücresinde hiç bulunmadığını sanmak.',
 alt='Hayvan ve bitki hücresi farkları',z='orta',kalip='öncüllü',kaz='Bitki ve hayvan hücresindeki ortak ve farklı yapıları şemada yorumlar.',sekil=SK[8],
 metin='Şekilde bir hayvan hücresi (X) ile bir bitki hücresi (Y) şematik olarak gösterilmiştir. Hücrelerdeki bazı yapılar I, II, III, IV ve V ile numaralandırılmıştır.\nI. I ve II numaralı yapılar hayvan hücrelerinde bulunmaz.\nII. III numaralı yapı yalnızca bitki hücrelerinde bulunur.\nIII. V numaralı yapı, Y hücresinde de bulunur.\nBuna göre, bu yargılardan hangileri doğrudur?',
 istenen='Şekle göre doğru olan yargılar.',ip=['Her yargıdaki numarayı şekilde bul; hangi yapıların yalnız bitkiye özgü, hangilerinin ortak olduğunu düşün.'],
 bilgi=[B('Hücre yapıları','Bitki ve hayvan hücreleri ortak organellerin yanında kendilerine özgü yapılar da taşır')],
 puf='Duvar ve kloroplast bitkiye özgüdür; mitokondri ve (küçük) koful her iki hücrede de bulunur.')
# ---- 09 · F2 üç hücre (zor) ----
SK[9]=sekil_f2()
qt(9,[A('Hücreleri tanı','K ve L hücrelerinde hücre duvarı ve büyük koful, M hücresinde ise sentrozom bulunur; yalnız K hücresinde kloroplast vardır.','K: duvar + kloroplast · L: duvar, kloroplastsız · M: sentrozomlu, duvarsız'),
      A('Hücrelerin türünü belirle','K ve L bitki hücreleridir; L aynı bitkinin kök gibi ışık almayan bir kısmından alınmıştır. M hayvan hücresidir.','K, L: bitki · M: hayvan'),
      A('Yargıları değerlendir','Üç hücrenin üçünde de çekirdek zarı vardır, yani hepsi ökaryottur; sentrozom bitki hücrelerinde bulunmaz; kloroplast eksikliği bitki hücresi olmayı engellemez.','Yalnız L’nin kloroplastsız bitki hücresi olması doğru'),
      A('Sonucu yaz','Hücre duvarı olan K ve L bitki hücresidir; L’de kloroplast bulunmaması bunu değiştirmez.','Doğru yargı belirlendi')],
 tek('B','K ve L hücrelerinin ikisinde de hücre duvarı vardır; L, kloroplastsız bir bitki hücresidir.',
  [('Yalnız K hücresi çekirdeğe sahip olduğundan ökaryot bir hücredir.','Çekirdek zarını yalnız kloroplastlı hücreye özgü sanmış; üç hücrede de çekirdek var.','bilgi'),
   ('M hücresi hücre duvarı taşımadığından prokaryot bir hücredir.','Duvarsızlığı prokaryotlukla karıştırmış; M çekirdekli ve organelli, yani ökaryottur (hayvan).','bilgi'),
   ('K ve L hücrelerinde, M hücresindeki gibi sentrozom bulunur.','Sentrozomu bitki hücresi de taşır sanmış; şekilde yalnız M’de var ve bitki hücrelerinde bulunmaz.','dikkat'),
   ('L hücresi kloroplast taşımadığından bir hayvan hücresidir.','Kloroplastı bitki hücresinin tek ayırt edici özelliği sanmış; L duvarlı ve kofullu bir bitki hücresidir.','bilgi')]),
 'üç hücre yapı karşılaştırması','bitki yaprağı ve kökü hücreleri','Kloroplast, bitkinin ışık alan hücrelerinde bulunur; kök hücresi kloroplastsız olsa da bitki hücresidir.','Kloroplastsız hücreyi bitki hücresi saymamak; duvar–sentrozom ayrımını karıştırmak.',
 alt='Hayvan ve bitki hücresi farkları',z='orta',kalip='şekilli',kaz='Bitkinin farklı kısımlarından alınan hücrelerle hayvan hücresini yapısal olarak karşılaştırır.',sekil=SK[9],
 metin='Şekilde, aynı bitkinin yaprağından ve kökünden alınan iki hücre (K ve L) ile bir hayvan hücresi (M) şematik olarak gösterilmiştir.\nBuna göre, aşağıdakilerden hangisi doğrudur?',
 istenen='Şekle göre doğru olan yargı.',ip=['Kloroplastın bitkinin her kısmında bulunup bulunmadığını düşün.'],
 bilgi=[B('Doku hücreleri','Aynı canlının farklı doku hücrelerinde organel çeşit ve sayısı işlevine göre değişir')],
 puf='Bitki hücresi duvar ve koful ile tanınır; kloroplast yalnız ışık gören bitki hücrelerinde bulunur.')
# ---- 10 · FH lizozom (kolay) ----
SK[10]=sekil_fh()
qt(10,[A('Organelleri tanı','Çift çizgili yuvarlak yapı çekirdek, kıvrımlı içli oval yapı mitokondri, yassı keseler yığını Golgi cisimciği, üzeri noktalı dalgalı borular granüllü ER, içi noktalı küçük kesecik lizozomdur.','I: çekirdek · II: mitokondri · III: Golgi · IV: granüllü ER · V: lizozom'),
       A('Görevi eşleştir','Hücre içine alınan maddeleri ve yaşlanmış organelleri sindirim enzimleriyle parçalayan organel lizozomdur.','Hücre içi sindirim → lizozom'),
       A('Numarayı seç','Lizozom şekilde V numarasıyla gösterilmiştir.','V')],
 dict(dogru='V',yan=[('I','I numaralı yapı çekirdektir; kalıtım materyalini barındırır ve hücreyi yönetir.','bilgi'),('II','II numaralı yapı mitokondridir; organik maddeleri yıkarak ATP üretir ama sindirim enzimi taşımaz.','bilgi'),('III','III numaralı yapı Golgi cisimciğidir; maddeleri paketler ve salgılar, parçalamaz.','bilgi'),('IV','IV numaralı yapı granüllü ER’dir; ribozomlarla protein sentezine ve taşınmasına katılır.','bilgi')],sira=['I','II','III','IV','V']),
 'lizozom tanıma','hayvan hücresinde numaralı organeller','Sindirim enzimli kesecik biçimi (küçük, noktalı, tek zarlı yuvarlak) ve görevi eşleştirilir.','Golgi cisimciğini keseciklerle oluşturduğu için sindirim yapan organel sanmak.',
 alt='Organeller ve görevleri',z='kolay',kalip='şekilli',kaz='Hayvan hücresinde lizozomu biçiminden tanır ve görevini bilir.',sekil=SK[10],
 metin='Şekilde bir hayvan hücresinin bazı organelleri I, II, III, IV ve V ile numaralandırılmıştır.\nBuna göre, numaralı yapılardan hangisi, hücre içine alınan besin maddelerini ve yaşlanmış organelleri sindirim enzimleriyle parçalar?',
 istenen='Hücre içi sindirimi yapan organelin numarası.',ip=['Organelleri biçimlerinden tanı; sindirim enzimlerini içinde taşıyan küçük kesecik hangisi?'],
 bilgi=[B('Organel biçimleri','Granüllü ER yüzeyinde ribozomlar bulunan yassı borulardır · Golgi cisimciği üst üste dizili yassı keselerdir · Mitokondrinin iç zarı kıvrımlıdır')],
 puf='Sindirim enzimli kesecik lizozomdur; organelleri biçimiyle (kıvrımlı mitokondri, yığınlı Golgi) tanı.')
# ---- 11 · mitokondri–kloroplast iç yapı (orta, öncüllü) ----
SK[11]=sekil_mk()
d11={'I':(True,'Mitokondrinin iç zarı kıvrımlıdır (krista); bu kıvrımlar enzimlerin yer aldığı zar yüzeyini artırır.'),
     'II':(True,'Kloroplastta klorofil, tilakoit keseciklerin üst üste dizilmesiyle oluşan grana yığınlarında bulunur.'),
     'III':(False,'Işıkla inorganik maddelerden organik madde sentezi kloroplastta yapılır; mitokondri ise organik maddeleri yıkarak ATP üretir.')}
qo(11,onc(d11,'C','dogru'),'iç yapısı çizili iki organel','mitokondri ve kloroplastın iç yapısı',
 'İç yapıdan (kıvrımlı iç zar, zar yığınları) organel tanınır; görev öncülü tersine çevrilmiştir.','Mitokondri ile kloroplastın görevlerini ve iç yapılarını karıştırmak.',
 alt='Organeller ve görevleri',z='orta',kalip='öncüllü',kaz='Mitokondri ve kloroplastın iç yapısını ve görevini ilişkilendirir.',sekil=SK[11],
 metin='Şekilde, aynı bitki hücresinde bulunan iki organelin iç yapısı X ve Y ile gösterilmiştir.\nI. X organelinin iç zarı kıvrımlıdır ve bu kıvrımlar zarın yüzeyini artırır.\nII. Y organelinde klorofil, zar keseciklerinin üst üste dizilmesiyle oluşan yığınlarda bulunur.\nIII. X organelinde ışık enerjisi kullanılarak inorganik maddelerden organik madde sentezlenir.\nBuna göre, bu yargılardan hangileri doğrudur?',
 istenen='Şekildeki organeller için doğru olan yargılar.',ip=['X ve Y’nin iç yapılarına bak: kıvrımlı iç zar ile yığınlı zar keseciklerinin hangi organelin görevine uyduğunu düşün.'],
 bilgi=[B('Organellerin zarları','Bazı organeller çift zarlıdır; iç yapıları görevlerine göre farklılaşır')],
 puf='Kıvrımlı iç zar = mitokondri (ATP üretir); yığınlı zar keseleri = kloroplast (ışıkla sentez).')
# ---- 12 · salgı proteini yolu (orta) ----
SK[12]=sekil_fs()
qt(12,[A('Yapıları tanı','Üzeri ribozom dolu dalgalı borular granüllü ER (II), yassı keseler yığını Golgi cisimciği (I), küçük yuvarlak keseler salgı keseciğidir (III).','I: Golgi · II: granüllü ER · III: kesecikler'),
       A('Yolu sırala','Salgı proteini ER yüzeyindeki ribozomda sentezlenip ER’ye girer; kesecikle Golgi’ye taşınır, orada paketlenir ve salgı keseciğiyle hücre zarına gider.','ER → Golgi → kesecik'),
       A('Numaralara çevir','ER II, Golgi I, kesecik III numarasıyla gösterilmiştir.','II → I → III')],
 tek('A','II → I → III',[('I → II → III','Golgi cisimciğinin ER’den önce geldiğini sanmış; oysa protein önce ER’ye girer.','bilgi'),
   ('III → I → II','Yolu ters sıralamış; salgı keseciği yolun sonunda yer alır.','bilgi'),
   ('II → III → I','Salgı keseciklerinin Golgi’den önce oluştuğunu sanmış; salgı keseciği Golgi’de paketlenme sonrası ayrılır.','bilgi'),
   ('I → III → II','Proteinin sentezinin Golgi’de başladığını sanmış; protein sentezi ribozomda yapılır.','bilgi')]),
 'salgı proteininin organel yolu','numaralı salgı yolu şeması','Ribozom → granüllü ER → Golgi cisimciği → salgı keseciği → hücre zarı sırası şekildeki yapılarla eşleştirilir.','Golgi cisimciğini ER’den önce sanmak.',
 alt='Organeller ve görevleri',z='orta',kalip='şekilli',kaz='Salgı proteininin hücre içi yolunu organel şemasında izler.',sekil=SK[12],
 metin='Şekilde, salgı yapan bir hayvan hücresinin bazı yapıları I, II ve III ile gösterilmiştir. Bu hücrede sentezlenerek hücre dışına salgılanan bir protein, sentezlendiği yerden başlayarak salgılanıncaya kadar bu yapılardan geçmektedir.\nBuna göre, proteinin izlediği yolun numaralarla gösterilişi aşağıdakilerden hangisinde doğru verilmiştir?',
 istenen='Salgı proteininin organel sıralaması.',ip=['Proteinin sentezlendiği yer ile paketlenip hücre dışına gönderildiği yapıyı belirle; ortadaki durağı sonra bul.'],
 bilgi=[B('Salgı hücresi','Salgı yapan hücrelerde granüllü ER ve Golgi cisimciği bol bulunur')],
 puf='Salgı proteininin yolu: ribozom → ER → Golgi → kesecik → hücre zarı.')
# ---- 13 · Golgi'yi engelleyen madde (zor) ----
qt(13,[A('Olayı kur','Salgı enzimi ribozomda sentezlenir, ER’den Golgi cisimciğine taşınır ve Golgi’de paketlenerek salgı keseciğiyle hücre dışına verilir.','Ribozom → ER → Golgi → kesecik → dışarı'),
       A('Engelin yerini bul','Madde yalnız Golgi’den salgı keseciğinin ayrılmasını engeller; ribozom ve ER etkilenmez.','Aksayan basamak: Golgi’den kesecik çıkışı'),
       A('Sonucu çıkar','Engelden önceki basamaklar çalışmaya devam ettiği için enzimler Golgi’de birikir; engelden sonraki basamak gerçekleşmediğinden salgı azalır.','Golgi’de birikme · salgı azalır'),
       A('Seçenekleri ele','Ribozomda sentez sürer, kesecik sayısı artmaz, salgı artmaz; ER ürünü doğrudan hücre zarına göndermez.','Yalnız birikme ve salgı azalması uyuyor')],
 tek('D','Enzimlerin Golgi cisimciğinde birikmesi ve hücre dışına salgılanan enzim miktarının azalması',
  [('Ribozomlarda amino asitlerin birleşmesinin hemen durması ve enzim sentezinin sona ermesi','Ribozomların etkilenmediği bilgisini görmeyip engelin sentezi de durduracağını sanmış.','dikkat'),
   ('Hücre dışına salgılanan enzim miktarının artması ve Golgi cisimciğinin küçülmesi','Engellenen basamağın salgıyı hızlandıracağını sanmış; paketleme olmadan salgı azalır.','bilgi'),
   ('Salgı keseciklerinin sayısında artış olması ve enzimlerin hücre dışına daha hızlı verilmesi','Kesecik oluşumunun engellendiğini göz ardı edip kesecik sayısının artacağını sanmış.','dikkat'),
   ('Enzimlerin endoplazmik retikulumdan doğrudan hücre zarına taşınarak salgılanmaya devam etmesi','ER’nin proteini doğrudan hücre zarına gönderebildiğini sanmış; protein önce Golgi’ye aktarılır.','bilgi')]),
 'Golgi’den kesecik çıkışının engellenmesi','salgı zincirinde engel','Zincirde bir basamak engellenirse öncesinde birikme, sonrasında azalma görülür.','Engellenen basamağın ardındaki salgıyı sürüyor saymak.',
 alt='Organeller ve görevleri',z='zor',kalip='hikâyeli',kaz='Salgı zincirinde bir basamağın engellenmesinin sonuçlarını yorumlar.',
 metin='Pankreas hücrelerinde sindirim enzimleri (protein yapılı) ribozomlarda sentezlenir ve hücre dışına salgılanır. Bir araştırmacı, bu hücrelere Golgi cisimciğinden salgı keseciklerinin ayrılmasını engelleyen bir madde uyguluyor. Maddenin ribozomları, endoplazmik retikulumu ve mitokondrileri doğrudan etkilemediği biliniyor.\nBuna göre, madde uygulanan hücrelerde kısa süre sonra aşağıdakilerden hangisinin gözlenmesi beklenir?',
 istenen='Madde uygulanan hücrelerde beklenen sonuç.',ip=['Salgı yolundaki basamakların sırasını yaz; engellenen basamaktan önceki ve sonraki basamaklara ne olacağını ayrı ayrı düşün.'],
 bilgi=[B('Salgı hücresi','Salgı yapan hücrelerde granüllü ER ve Golgi cisimciği bol bulunur; Golgi, ER’den gelen proteinleri paketleyip keseciklerle dışarı gönderir')],
 puf='Bir zincirin ortasındaki engel, öncesinde birikmeye, sonrasında eksikliğe yol açar.')
# ---- 14 · fagositoz (orta, olumsuz) ----
qt(14,[A('Olayı çöz','Akyuvar bakteriyi zarıyla çevreleyip kesecik içinde hücreye alır (fagositoz); kesecik sindirim enzimli yapıyla birleşir.','Fagositoz → hücre içi sindirim'),
       A('Doğru yargıları ayır','Kesecik zarı hücre zarından oluşur, enzimleri lizozom taşır, taşıma ATP harcatır, sindirim ürünleri sitoplazmada kullanılır.','Dört yargı doğru'),
       A('Yanlışı bul','Sindirim enzimleri ribozomda sentezlenir ve lizozomda taşınır; mitokondri ATP üretir, enzim üretip depolamaz.','Mitokondri enzim üretir → yanlış')],
 tek('B','Bakteriyi parçalayan enzimler mitokondride üretilir ve depolanır.',
  [('Bakteri, hücre zarının oluşturduğu kesecik içinde hücreye alınır.','Endositozla alınan maddenin zar kökenli keseciğe sarıldığını bilmediği için bu doğru yargıyı yanlış saymış.','bilgi'),
   ('Sindirim enzimlerini taşıyan yapılar lizozomlardır.','Hücre içi sindirimin lizozomla yapıldığını bilmediği için bu doğru yargıyı yanlış saymış.','bilgi'),
   ('Bakterinin hücre içine alınması sırasında ATP harcanır.','Fagositozu pasif taşıma sanıp ATP harcanmadığını düşünerek bu doğru yargıyı yanlış saymış.','bilgi'),
   ('Sindirim sonucu oluşan küçük moleküller sitoplazmada kullanılabilir.','Sindirim ürünlerinin hücre dışına atıldığını düşünerek bu doğru yargıyı yanlış saymış.','bilgi')]),
 'akyuvarın bakteriyi yutması','fagositoz ve lizozom','Endositozda kesecik zarı hücre zarından oluşur, ATP harcanır; sindirimi lizozom yapar.','Mitokondriyi enzim üreten organel saymak.',
 alt='Organeller ve görevleri',z='kolay',kalip='hikâyeli',kaz='Hücre içi sindirimde görevli yapıları ve süreci yorumlar.',
 metin='Vücudumuzdaki bazı akyuvar hücreleri, vücuda giren bakterileri hücre içine alarak parçalar. Bu olayda hücre zarı bakteriyi çevreleyerek bir kesecik oluşturur; kesecik daha sonra sindirim enzimleri taşıyan yapılarla birleşir.\nBuna göre, bu olayla ilgili aşağıdakilerden hangisi yanlıştır?',
 istenen='Fagositozla ilgili yanlış olan yargı.',ip=['Her yargıyı sırayla sına; yanlış olan, organelin asıl görevine uymayan yargıdır.'],
 bilgi=[B('Madde alımı','Hücre zarı, büyük parçacıkları çevreleyerek hücre içine alabilir')],
 puf='Sindirim enzimli organel lizozomdur; mitokondri ise yalnız ATP üretir.')
# ---- 15 · ribozom öncüllü yanlış (orta) ----
d15={'I':(False,'Ribozom prokaryot ve ökaryot hücrelerin hepsinde bulunur.'),
     'II':(True,'Ribozom zarsız bir organeldir.'),
     'III':(False,'Ribozomlar yalnız serbest değildir; sitoplazmada serbest ya da endoplazmik retikulum yüzeyine tutunmuş olarak bulunur.')}
qo(15,onc(d15,'E','yanlis'),'ribozom bilgileri','ribozomun özellikleri',
 'Ribozomun her hücrede bulunuşu, zarsızlığı ve bulunduğu yerler sorulur; yanlış öncüller istenir.','Ribozomu yalnız ökaryotlara özgü ve yalnız serbest sanmak.',
 alt='Organeller ve görevleri',z='kolay',kalip='öncüllü',kaz='Ribozomun yapısal ve işlevsel özelliklerini değerlendirir.',
 metin='Bir öğrenci, protein sentezinde görev alan ribozomlarla ilgili aşağıdaki bilgileri not alıyor.\nI. Yalnızca ökaryot hücrelerde bulunur.\nII. Zarla çevrili olmayan bir organeldir.\nIII. Yalnızca sitoplazmada serbest hâlde bulunur.\nBuna göre, bu bilgilerden hangileri yanlıştır?',
 istenen='Ribozom için yanlış olan bilgiler.',ip=['Ribozomun hangi hücrelerde ve hücrenin hangi bölgelerinde bulunduğunu düşün.'],
 bilgi=[B('Ribozom','Ribozom, protein sentezinde görevli bir organeldir')],
 puf='Ribozom = zarsız, her canlı hücrede var, serbest ya da ER’ye bağlı bulunur.')
# ---- 16 · FZ glikoprotein (kolay) ----
SK[16]=sekil_fz()
qt(16,[A('Yapıları tanı','Siyah başlı ve çift kuyruklu moleküller fosfolipit, zarı boydan boya geçen iri yapı protein, dalları olan zincir karbonhidrat, kuyruklar arasındaki küçük yapı kolesterol, içte yüzeye bağlı yapı yüzeyde bulunan proteindir.','I: fosfolipit · II: zarı geçen protein · III: karbonhidrat zinciri · IV: kolesterol · V: yüzeyde protein'),
       A('Görevi eşleştir','Hücrelerin birbirini ve çevresindeki maddeleri tanımasını, zar dışındaki karbonhidrat zincirleri sağlar.','Tanıma → karbonhidrat zinciri'),
       A('Numarayı seç','Dallı karbonhidrat zinciri şekilde III ile gösterilmiştir.','III')],
 dict(dogru='III',yan=[('I','I numaralı yapı fosfolipittir; zarın iskeletini oluşturur, tanıma yapmaz.','bilgi'),('II','II numaralı yapı zarı boydan boya geçen proteindir; madde geçişine yardım eder.','bilgi'),('IV','IV numaralı yapı kolesteroldür; zarın akışkanlığını ve dayanıklılığını etkiler.','bilgi'),('V','V numaralı yapı hücre içi yüzeyde bulunan proteindir; zarın dışında yer almaz.','dikkat')],sira=['I','II','III','IV','V']),
 'zar yapı tanıma','hücre zarı kesiti','Hücre zarının dış yüzünde karbonhidrat zincirleri hücre tanımasında rol alır.','Tanıma görevini zarı geçen proteinle ya da fosfolipitle karıştırmak.',
 alt='Hücre zarı',z='kolay',kalip='şekilli',kaz='Hücre zarı kesitinde yüzey işaretlerini tanır.',sekil=SK[16],
 metin='Şekilde bir hücre zarının yapısı gösterilmiştir. Zarı oluşturan bazı yapılar I, II, III, IV ve V ile numaralandırılmıştır.\nBuna göre, numaralı yapılardan hangisi, hücrelerin birbirini ve çevresindeki maddeleri tanımasında rol oynayan yüzey işaretlerinin bir parçasıdır?',
 istenen='Hücre tanımada rol alan yapının numarası.',ip=['Zarın dış yüzünü ve görevlerini düşün.'],
 bilgi=[B('Zarın yapı taşları','Hücre zarında lipitler, proteinler ve karbonhidratlar farklı görevler yapar')],
 puf='Zarın dışındaki dallı karbonhidrat zincirleri “kimlik kartı” gibidir; hücre tanımada görev alır.')
# ---- 17 · akıcı mozaik öncüllü (orta) ----
d17={'I':(True,'Fosfolipitlerin çoğu zar düzleminde yan yana hareket edebilir; zar bu yüzden akışkandır.'),
     'II':(True,'Bazı proteinler fosfolipit tabakasını boydan boya geçer, bazıları yalnızca bir yüzeyde bulunur; bu görünüm mozaik gibidir.'),
     'III':(False,'Zarın temelini çift sıra fosfolipit oluşturur; proteinler bu tabakaya gömülü ya da yüzeye bağlıdır.')}
qo(17,onc(d17,'B','dogru'),'akıcı mozaik modeli öncülleri','akıcı mozaik zar modeli',
 'Modelin “akıcı” ve “mozaik” kavramları nitel öncüllerle sorulur; üçüncü öncül zarı yalnız proteinden oluşturur.','Zarı iki kat protein tabakası sanmak, fosfolipitleri sabit sanmak.',
 alt='Hücre zarı',z='orta',kalip='öncüllü',kaz='Akıcı mozaik zar modelini nitel olarak yorumlar.',
 metin='Hücre zarının yapısını açıklayan akıcı mozaik modeli ile ilgili bir öğrenci aşağıdaki bilgileri yazıyor.\nI. Fosfolipit moleküllerinin çoğu zar düzleminde yer değiştirebilir.\nII. Proteinlerin bir kısmı fosfolipit tabakasını boydan boya geçerken bir kısmı yalnızca yüzeyde bulunur.\nIII. Zar, iki kat protein tabakasından oluşur ve fosfolipit içermez.\nBuna göre, bu bilgilerden hangileri doğrudur?',
 istenen='Akıcı mozaik modeline uygun bilgiler.',ip=['Her öncülü, zarın yapısı hakkında bildiklerinle karşılaştır.'],
 bilgi=[B('Zarın temel yapısı','Zarın iskeletini iki sıra dizilmiş fosfolipit oluşturur; fosfolipitin su seven başı dışa, su sevmeyen kuyrukları içe doğrudur')],
 puf='Akıcı = moleküller hareketlidir; mozaik = proteinler fosfolipit denizinde farklı biçimlerde dağılmıştır.')
# ---- 18 · floresan deneyi (zor) ----
qt(18,[A('Deneyi oku','İlk dakikada insan ve fare proteinleri zarın ayrı yarılarındadır; 40 dakika sonra karışmıştır; düşük sıcaklıkta karışma çok yavaştır.','Karışma: zamanla var · soğukta yavaş'),
       A('Çıkarım yap','Proteinler zarda yer değiştirerek karışabildiğine göre zar sabit değil, akışkandır; sıcaklık düşünce hareket yavaşlar.','Proteinler hareketli · hareket sıcaklığa bağlı'),
       A('Seçenekleri ele','Proteinler sabit değildir, parçalanma verisi yoktur, tek sıra lipit ve aynı protein varsayımı deneyle desteklenmez.','Yalnız hareketlilik ve sıcaklık çıkarımı uyuyor')],
 tek('A','Zar proteinleri fosfolipit tabakasında hareket edebilir ve bu hareket sıcaklık düştükçe yavaşlar.',
  [('Zar proteinleri fosfolipit tabakasında sabit konumdadır; karışma hücre içi sıvıdaki akıntıdan kaynaklanır.','Zarı sabit bir yapı sanıp karışmayı zar dışı bir etkenle açıklamış.','bilgi'),
   ('Düşük sıcaklıkta zar proteinleri parçalandığı için karışma çok yavaş gerçekleşir.','Yavaşlamayı proteinlerin parçalanmasına bağlamış; deney böyle bir veri vermiyor.','dikkat'),
   ('Zar, tek sıra fosfolipit tabakasından oluştuğu için proteinler kısa sürede karışabilmiştir.','Zarın tek sıra fosfolipitten oluştuğunu sanmış; zar çift sıra fosfolipitten oluşur.','bilgi'),
   ('İnsan ve fare hücre zarlarındaki proteinler aynı çeşit olduğu için karışma gerçekleşmiştir.','Karışmayı proteinlerin aynı oluşuna bağlamış; deney proteinlerin hareketini gösteriyor.','dikkat')]),
 'floresan işaretli zar proteinleri deneyi','zarın akışkanlığı deney yorumu','Kaynaştırılan hücrelerde işaretli proteinlerin zamanla karışması zarın akışkan olduğunu, soğukta yavaşlaması hareketin sıcaklığa bağlı olduğunu gösterir.','Zar proteinlerinin sabit olduğunu düşünmek ve veriyi fazla yorumlamak.',
 alt='Hücre zarı',z='zor',kalip='yeni nesil',kaz='Deney verisinden zarın akışkanlığı sonucuna ulaşır.',
 metin='Bir araştırmacı, insan hücresi zar proteinlerini yeşil, fare hücresi zar proteinlerini kırmızı floresan boyayla işaretleyip iki hücreyi kaynaştırıyor. Kaynaşmadan hemen sonra iki rengin hücre zarının farklı yarılarında kaldığı, 40 dakika sonra ise zarın her yerinde karıştığı görülüyor. Aynı deney düşük sıcaklıkta yapıldığında karışma çok yavaş gerçekleşiyor.\nBu deney sonuçlarına göre aşağıdakilerden hangisi söylenebilir?',
 istenen='Deney sonuçlarından çıkarılabilecek yargı.',ip=['İşaretlerin zamanla ne yaptığına ve sıcaklığın etkisine bak.'],
 bilgi=[B('Hücre zarı','Hücre zarı fosfolipit ve proteinlerden oluşur')],
 puf='Deneyde değişen şeyi (zamanla karışma) ve koşulu (sıcaklık) eşleştir; yalnız veriyle desteklenen sonucu seç.')
# ---- 19 · üç madde geçişi şeması (orta) ----
SK[19]=sekil_fg()
GT=('Basit difüzyon','Kolaylaştırılmış difüzyon','Aktif taşıma')
def uc(*i): return ' – '.join(GT[k] for k in i)
qt(19,[A('Panelleri oku','I’de taşıyıcı protein yok, madde çoktan aza geçiyor; II’de taşıyıcı protein var, madde çoktan aza geçiyor; III’te taşıyıcı protein var, madde azdan çoğa geçiyor ve ATP harcanıyor.','I: protein yok, çok → az · II: protein var, çok → az · III: protein var, az → çok, ATP'),
       A('Türleri eşleştir','Proteinsiz ve ATP’siz çoktan aza geçiş basit difüzyon, proteinli ama ATP’siz çoktan aza geçiş kolaylaştırılmış difüzyon, ATP harcayarak azdan çoğa geçiş aktif taşımadır.','I: basit · II: kolaylaştırılmış · III: aktif'),
       A('Sıralamayı yaz','Üç taşıma sırasıyla basit difüzyon, kolaylaştırılmış difüzyon ve aktif taşımadır.',uc(0,1,2))],
 tek('D',uc(0,1,2),[(uc(0,2,1),'Taşıyıcı proteinli II’yi aktif sanmış; II’de madde çoktan aza geçiyor ve ATP harcanmıyor.','bilgi'),
   (uc(1,0,2),'I’deki geçişi proteinli sanmış; I’de zarda taşıyıcı protein yok, madde doğrudan fosfolipitler arasından geçiyor.','dikkat'),
   (uc(1,2,0),'Proteinsiz I’yi proteinli, ATP harcanan III’ü basit saymış; sütunları kaydırmış.','dikkat'),
   (uc(2,1,0),'Sıralamayı tersine yazmış; ATP harcanan taşımanın III olduğunu fark etmemiş.','dikkat')]),
 'üç taşımanın şemada ayırt edilmesi','taşıyıcı protein, ATP ve yön','Madde geçişi türü; taşıyıcı protein varlığı, derişim farkına göre yön ve ATP kullanımıyla ayırt edilir.','Taşıyıcı proteinli her geçişi aktif taşıma sanmak.',
 alt='Madde geçişleri',z='orta',kalip='şekilli',kaz='Şemadaki madde geçişlerini türüne göre sınıflandırır.',sekil=SK[19],
 metin='Şekilde hücre zarından gerçekleşen üç farklı madde geçişi I, II ve III ile gösterilmiştir. Noktalar taşınan madde moleküllerini, oklar ise net geçiş yönünü göstermektedir.\nBuna göre, I, II ve III ile gösterilen madde geçişleri sırasıyla aşağıdakilerden hangisinde doğru verilmiştir?',
 istenen='I, II ve III’ün taşıma türleri.',ip=['Her panelde zarın yapısına, okun yönüne ve ek yazılara bak.'],
 bilgi=[B('Pasif ve aktif taşıma','Pasif taşıma ATP gerektirmez, aktif taşıma gerektirir')],
 puf='Önce ATP’ye, sonra taşıyıcı proteine bak: ATP varsa aktif, protein var ATP yoksa kolaylaştırılmış, ikisi de yoksa basit difüzyon.')
# ---- 20 · difüzyon öncüllü (kolay) ----
d20={'I':(True,'Difüzyonda madde, derişimin fazla olduğu yerden az olduğu yere doğru geçer.'),
     'II':(False,'Basit difüzyon pasif taşımadır; madde derişim farkı yönünde geçtiği için ATP harcanmaz.'),
     'III':(True,'Oksijen gibi küçük ve yağda çözünen moleküller fosfolipit tabakasından taşıyıcı protein olmadan geçer.')}
qo(20,onc(d20,'E','dogru'),'difüzyon bilgileri','basit difüzyon',
 'Difüzyonun yönü, ATP gereksinimi ve taşıyıcı protein gerekmediği üç öncülle sorulur.','Difüzyonu ATP harcayan bir taşıma sanmak.',
 alt='Madde geçişleri',z='kolay',kalip='öncüllü',kaz='Basit difüzyonun özelliklerini bilir.',
 metin='Kandaki oksijen, doku hücrelerine hücre zarından difüzyonla geçer. Bu olayı inceleyen bir öğrenci, difüzyonla ilgili aşağıdaki bilgileri yazıyor.\nI. Madde, derişimin fazla olduğu ortamdan az olduğu ortama doğru geçer.\nII. Basit difüzyonda madde geçişi için ATP harcanır.\nIII. Oksijen gibi küçük ve yağda çözünen moleküller zardan taşıyıcı protein olmadan geçebilir.\nBuna göre, bu bilgilerden hangileri doğrudur?',
 istenen='Difüzyon için doğru olan bilgiler.',ip=['Difüzyonun yönünü ve enerji gereksinimini düşün; gazlar zardan nasıl geçer?'],
 bilgi=[B('Difüzyon','Moleküllerin rastgele hareketi sonucu derişimin fazla olduğu yerden az olduğu yere yayılmasıdır; enerji gerektirmeyen pasif bir olaydır. Örnek: odaya sıkılan kokunun yayılması')],
 puf='Difüzyon = çoktan aza, enerjisiz; basit difüzyonda ek olarak taşıyıcı protein de yoktur.')
# ---- 21 · taşıma hızı–derişim farkı grafiği (orta, olumsuz) ----
SK[21]=sekil_g21()
g=lambda x:G21['vmax']*x/(x+G21['km']); l=lambda x:G21['egim']*x
assert g(1)>l(1) and l(5)>g(5) and g(5)<G21['vmax'] and g(5)-g(4)<.1 and l(5)>l(4)
qt(21,[A('Eğrileri oku','I numaralı eğri doğrusaldır; hız derişim farkıyla sürekli artar. II numaralı eğri hızla yükselip yatay hâle gelir; hız sabitlenir.','I: sürekli artış · II: doyum'),
       A('Türleri belirle','Doyuma ulaşmayan I basit difüzyona, taşıyıcı sayısı sınırlı olduğu için doyuma ulaşan II kolaylaştırılmış difüzyona aittir.','I: basit · II: kolaylaştırılmış'),
       A('Yargıları sına','Grafiğe göre I’de hız sürekli artar, II’de hız belli bir farktan sonra sabitlenir, küçük derişim farklarında II daha hızlıdır ve fark sıfırken hız sıfırdır.','Dört yargı grafikle uyumlu'),
       A('Çıkarılamayanı seç','Taşıyıcı proteinli taşıma doyuma ulaşan II’dir; bu nedenle I’in proteinli olduğunu söyleyen yargı grafikten çıkarılamaz.','I proteinli → çıkarılamaz')],
 tek('A','I numaralı eğri taşıyıcı protein gerektiren, II numaralı eğri ise protein gerektirmeyen difüzyona aittir.',
  [('I numaralı eğriyle gösterilen taşımada, derişim farkı arttıkça taşıma hızı sürekli artar.','Doğrusal artışı yanlış okuyup doğru yargıyı çıkarılamaz saymış.','dikkat'),
   ('II numaralı eğriyle gösterilen taşımada, belirli bir derişim farkından sonra taşıma hızı yaklaşık sabit kalır.','Eğrinin yatay kısmını hızın düşmesi sanıp doğru yargıyı çıkarılamaz saymış.','dikkat'),
   ('Derişim farkı küçükken II numaralı taşımanın hızı, I numaralı taşımanın hızından büyüktür.','Eğrilerin kesiştiği noktadan sonrasını bütün aralığa uygulayıp bu doğru yargıyı yanlış saymış.','dikkat'),
   ('Derişim farkı sıfır olduğunda her iki taşımada da taşıma hızı sıfırdır.','Eğrilerin başlangıç noktasını fark etmeyip doğru yargıyı yanlış saymış.','dikkat')]),
 'basit ve kolaylaştırılmış difüzyon hız grafiği','hız–derişim farkı grafiği','Doyuma ulaşan eğri taşıyıcı proteinin sınırlı sayısına, doğrusal eğri taşıyıcısız difüzyona karşılık gelir.','Doyumu olan taşımayı proteinsiz sanmak.',
 alt='Madde geçişleri',z='orta',kalip='grafik',kaz='Difüzyon türlerini taşıma hızı grafiğinden ayırt eder.',sekil=SK[21],
 metin='Grafikte, hücre zarından gerçekleşen iki farklı difüzyon türünde (basit difüzyon ve kolaylaştırılmış difüzyon) madde taşıma hızının zarın iki yanındaki derişim farkına bağlı değişimi gösterilmiştir. Eğriler hangi difüzyon türüne ait olduğu belirtilmeden I ve II ile adlandırılmıştır.\nBuna göre, bu grafikten aşağıdaki sonuçlardan hangisi çıkarılamaz?',
 istenen='Grafikten çıkarılamayan sonuç.',ip=['Eğrilerin biçimini karşılaştır.'],
 bilgi=[B('Taşıyıcılı taşıma','Taşıyıcılı taşıma, zardaki taşıyıcı protein sayısına bağlıdır')],
 puf='Hız bir noktadan sonra sabitleniyorsa taşıyıcı protein sayısı sınırlayıcıdır; kolaylaştırılmış difüzyon olmalıdır.')
# ---- 22 · endositoz–ekzositoz (orta) ----
SK[22]=sekil_fe()
d22={'I':(True,'Endositozda kesecik zarı, içe çöken hücre zarından oluşur.'),
     'II':(True,'Ekzositozda kesecik zarı hücre zarıyla birleşir; bu yüzden zarın yüzey alanı artar.'),
     'III':(False,'Endositoz ve ekzositoz büyük maddelerin taşınması için ATP harcanarak yapılır.')}
qo(22,onc(d22,'B','dogru'),'endositoz–ekzositoz şeması','endositoz ve ekzositoz',
 'İki olayın şeması verilir; zar kökeni, zar yüzey alanı ve ATP gereksinimi öncüllerle sorulur.','Endositoz ve ekzositozu pasif taşıma sanmak.',
 alt='Madde geçişleri',z='orta',kalip='öncüllü',kaz='Endositoz ve ekzositozu şema üzerinde yorumlar.',sekil=SK[22],
 metin='Şekilde hücre zarından gerçekleşen iki farklı taşıma olayı (X ve Y) şematik olarak gösterilmiştir.\nI. X olayında kesecik zarı, hücre zarından oluşur.\nII. Y olayında kesecik zarı hücre zarıyla birleştiği için hücre zarının yüzey alanı artar.\nIII. X ve Y olaylarının ikisinde de ATP harcanmaz.\nBuna göre, bu olaylarla ilgili yukarıdaki yargılardan hangileri doğrudur?',
 istenen='Şekildeki olaylar için doğru yargılar.',ip=['Hangi olayda maddenin hücreye girdiğini, hangisinde çıktığını bul; kesecik zarının kaynağını ve enerji gereksinimini düşün.'],
 bilgi=[B('Zarla taşıma','Büyük maddeler, zarla çevrili keseciklerle hücreye alınabilir ya da hücreden atılabilir')],
 puf='Keseciklerle taşıma (endositoz–ekzositoz) enerji ister; ekzositozda kesecik zarı hücre zarına katılır, zar alanı artar.')
# ---- 23 · ATP üretimini durduran zehir (zor, beklenemez) ----
d23={'I':(True,'Derişim farkına karşı yapılan taşıma aktif taşımadır; ATP gerektirdiğinden ATP üretimi durunca azalır.','azalır'),
     'II':(False,'Ozmoz pasif taşımadır; ATP gerektirmediği için zehirden etkilenmez.','azalmaz'),
     'III':(True,'Endositoz ATP harcanarak yapılır; ATP üretimi durunca azalır.','azalır')}
qo(23,onc(d23,'A','yanlis','azalması beklenmeyen'),'ATP üretimi durunca taşımalar','ATP gerektiren ve gerektirmeyen taşımalar',
 'ATP üretiminin durmasıyla aktif taşıma ve endositoz etkilenir, ozmoz etkilenmez.','Ozmozu da enerji gerektiren bir taşıma sanmak.',
 alt='Madde geçişleri',z='orta',kalip='öncüllü',kaz='ATP gereksinimine göre madde geçişlerinin etkilenmesini yorumlar.',
 metin='Bağırsak epitel hücrelerine, ATP üretimini durduran bir zehir uygulanıyor. Zehir madde geçişini doğrudan değil, yalnızca hücrenin ATP üretimini engelleyerek etkiliyor. Hücrelerde aşağıdaki madde geçişlerinden bazıları gerçekleşiyor.\nI. Glikozun hücre içindeki derişimi daha yüksek olmasına rağmen hücreye alınması\nII. Suyun hücre zarından ozmozla geçmesi\nIII. Hücre dışındaki büyük bir parçacığın endositozla hücreye alınması\nBuna göre, zehir uygulandıktan kısa süre sonra bu geçişlerden hangilerinde azalma beklenemez?',
 istenen='Zehir uygulanınca azalması beklenmeyen madde geçişleri.',ip=['Zehir yalnızca ATP üretimini durduruyor; hangi geçişlerin enerjiye (ATP) gereksinim duyduğunu belirle.'],
 bilgi=[B('Pasif taşıma','Pasif taşıma enerji gerektirmez')],
 puf='ATP kesilirse yalnız ATP kullanan geçişler (aktif taşıma, endositoz, ekzositoz) etkilenir; pasif olanlar sürer.')
# ---- 24 · osmometre (kolay) ----
SK[24]=sekil_fo()
qt(24,[A('Zarı değerlendir','Zar yalnızca suyu geçirir; sakaroz zarı geçemez.','Hareket eden madde: su'),
       A('Çözeltileri karşılaştır','Tüpteki çözelti daha derişiktir, yani su oranı daha azdır; kaptaki çözelti daha seyrektir.','Su oranı: kap > tüp'),
       A('Su yönünü bul','Su, su oranı çok olan kaptan az olan tüpe geçer; tüpteki sıvı seviyesi yükselir.','Su: kap → tüp · seviye yükselir')],
 tek('D','Tüpteki sıvı seviyesi yükselir; çünkü su kaptan tüpe geçer.',
  [('Tüpteki sıvı seviyesi düşer; çünkü sakaroz tüpten kaba geçer.','Zarın sakarozu geçirdiğini sanmış; zar yalnız suyu geçirir.','bilgi'),
   ('Tüpteki sıvı seviyesi değişmez; çünkü zar iki çözeltiyi birbirinden ayırır.','Zarın hiçbir maddeyi geçirmediğini sanmış; su geçişi olur.','bilgi'),
   ('Tüpteki sıvı seviyesi düşer; çünkü su tüpten kaba geçer.','Su yönünü ters almış; su, derişik çözeltiye doğru geçer.','bilgi'),
   ('Tüpteki sıvı seviyesi yükselir; çünkü sakaroz kaptan tüpe geçer.','Seviye artışını doğru bulmuş ama zardan geçen maddeyi sakaroz sanmış.','bilgi')]),
 'osmometre düzeneğinde seviye değişimi','sakaroz çözeltili osmometre','Zar çözüneni geçirmiyorsa su, seyrek çözeltiden derişik çözeltiye geçer ve derişik taraftaki seviye yükselir.','Su yönünü ters almak ya da sakarozun geçtiğini sanmak.',
 alt='Madde geçişleri',z='kolay',kalip='şekilli',kaz='Osmometre düzeneğinde suyun geçiş yönünü ve seviye değişimini belirler.',sekil=SK[24],
 metin='Şekildeki osmometrenin alt ucu, yalnızca suyu geçiren yarı geçirgen bir zarla kapatılmış ve zarlı uç, bir kaptaki çözeltiye batırılmıştır. Çözeltilerin derişimleri şekilde verilmiştir. Düzenek uygun koşullarda bir süre bekletiliyor.\nBuna göre, aşağıdakilerden hangisi gözlenir?',
 istenen='Düzenek bekletildiğinde gözlenen durum.',ip=['Zar neyi geçiriyor? Sonra iki taraftaki çözeltilerin hangisinde su oranının daha fazla olduğuna bak.'],
 bilgi=[B('Ozmoz','Ozmoz, suyun yarı geçirgen zardan, su oranı fazla (seyrek) ortamdan su oranı az (derişik) ortama geçmesidir; pasif bir olaydır')],
 puf='Zar çözüneni tutuyorsa su derişik tarafa geçer, o taraftaki seviye yükselir.')
# ---- 25 · hayvan hücresi hacim–zaman grafiği (orta) ----
SK[25]=sekil_g25()
assert G25_SON[0]<G25_SON[2]<G25_SON[1]
sonuc25='I > III > II'
qt(25,[A('Eğrileri oku','I numaralı çözeltideki hücrenin hacmi azalmış, II’deki artmış, III’teki değişmemiştir.','I: hacim azalır · II: artar · III: değişmez'),
       A('Ortamları belirle','Hacmi azalan hücre su kaybetmiştir; ortam hücreye göre derişiktir (hipertonik). Hacmi artan hücre su almıştır; ortam seyrektir (hipotonik). Değişmeyen hücrede ortam izotoniktir.','I: hipertonik · II: hipotonik · III: izotonik'),
       A('Derişimleri sırala','Hipertonik > izotonik > hipotonik olduğundan çözeltiler I, III, II sırasıyla seyrelir.',sonuc25)],
 tek('E',sonuc25,[('I > II > III','Hacmi artan hücrenin çözeltisini derişik sanıp I’den sonra II’yi yazmış.','bilgi'),
   ('II > I > III','Hacim artışını derişimin yüksekliği sanmış; su alan hücrenin ortamı seyrektir.','bilgi'),
   ('II > III > I','Sıralamayı tersine almış; hacmi azalan hücrenin ortamı en derişik olandır.','bilgi'),
   ('III > I > II','İzotonik ortamı en derişik sanmış; izotonik ortam hipertonik ile hipotonik arasındadır.','bilgi')]),
 'üç çözeltide hayvan hücresinin hacmi','hacim–zaman grafiğinden derişim sıralaması','Hacmi azalan hücre hipertonik, artan hücre hipotonik, değişmeyen hücre izotonik ortamdadır.','Su alan hücrenin çözeltisini derişik sanmak.',
 alt='Madde geçişleri',z='orta',kalip='grafik',kaz='Hacim–zaman grafiğinden çözeltilerin derişimlerini sıralar.',sekil=SK[25],
 metin='Aynı hayvan dokusundan alınan ve başlangıçta aynı hacme sahip üç hücre, I, II ve III numaralı üç farklı çözeltiye konuyor. Hücre hacimlerinin zamanla değişimi grafikte verilmiştir; hiçbir hücre parçalanmamıştır. Eğriler, hücrenin konduğu çözeltinin numarasıyla adlandırılmıştır.\nBuna göre, çözeltilerin derişimleri arasındaki ilişki aşağıdakilerden hangisinde doğru verilmiştir?',
 istenen='Çözeltilerin derişim sıralaması.',ip=['Hacmin azalması, artması ya da değişmemesi suyun hangi yönde geçtiğini gösterir; bunu çözelti–hücre derişim farkına çevir.'],
 bilgi=[B('Ortam türleri','Ortam hücre özsuyundan derişikse hipertonik, seyrekse hipotonik, eşitse izotonik adını alır · Su, seyrek ortamdan derişik ortama doğru geçer')],
 puf='Hücre küçülüyorsa ortam derişik, büyüyorsa seyrek, değişmiyorsa eşittir.')
# ---- 26 · plazmoliz derecesi (orta, öncüllü) ----
SK[26]=sekil_fp()
assert FP_F[0]==1.0 and FP_F[0]>FP_F[1]>FP_F[2]
d26={'I':(True,'I numaralı hücrede plazmoliz yoktur; çözelti hücre özsuyuna göre hipertonik olsaydı hücre su kaybederdi.'),
     'II':(True,'Plazmoliz ne kadar belirginse çözelti hücre özsuyuna göre o kadar derişiktir; III en çok, I en az büzülmüştür.'),
     'III':(False,'Plazmolizde hücre zarı ve sitoplazma büzülüp duvardan ayrılır; duvar şeklini korur.')}
qo(26,onc(d26,'C','dogru'),'plazmoliz derecesi şeması','üç bitki hücresinde plazmoliz derecesi',
 'Plazmoliz derecesinden çözelti derişimi sıralanır; hücre duvarının büzüldüğü öncülü yanlıştır.','Hücre duvarının da büzüldüğünü sanmak.',
 alt='Madde geçişleri',z='orta',kalip='öncüllü',kaz='Bitki hücresinde plazmoliz derecesini çözelti derişimiyle ilişkilendirir.',sekil=SK[26],
 metin='Şekilde, özsuyu derişimleri aynı olan üç bitki hücresi, I, II ve III numaralı farklı şeker çözeltilerine konup aynı süre bekletildikten sonraki durumlarıyla gösterilmiştir. Şeker, hücre zarından geçemez ve hücreler canlıdır.\nI. I numaralı çözelti, hücre özsuyuna göre hipertonik değildir.\nII. Çözeltilerin derişimleri III > II > I şeklindedir.\nIII. III numaralı hücrede hücre zarı, duvarla birlikte büzülmüş ve duvara bitişik kalmıştır.\nBuna göre, bu yargılardan hangileri doğrudur?',
 istenen='Şekle göre doğru olan yargılar.',ip=['Her hücrede zarın duvara göre konumuna bak.'],
 bilgi=[B('Bitki hücresi ve su','Bitki hücresi, hipertonik ortamda su kaybeder')],
 puf='Plazmolizde büzülen zar ve sitoplazmadır, duvar değil; ayrılma arttıkça çözelti derişiktir.')
# ---- 27 · patates kütle tablosu (orta) ----
CONC=[0,2,4,6,8]; SON=[Fr(118,10),Fr(109,10),Fr(102,10),Fr(96,10),Fr(91,10)]; BAS=Fr(10)
dl=[x-BAS for x in SON]; ix=[i for i in range(4) if dl[i]>0>dl[i+1]]; assert ix==[2]
alt_,ust_=CONC[ix[0]],CONC[ix[0]+1]
assert alt_==4 and ust_==6 and dl[0]>dl[1]>dl[2]>0>dl[3]>dl[4]
SK[27]=tablo_svg(['Çözeltinin derişimi (%)','Başlangıç kütlesi (g)','Son kütlesi (g)'],[[str(c),fm(BAS),fm(x)] for c,x in zip(CONC,SON)])
araliklar=[f'%{CONC[i]} ile %{CONC[i+1]} arasında' for i in range(4)]+['%8’den büyüktür']
qt(27,[A('Tabloyu oku','Kütle %0, %2 ve %4’lük çözeltilerde artmış, %6 ve %8’likte azalmıştır.','Artış: %0, %2, %4 · Azalış: %6, %8'),
       A('Değişimi yorumla','Kütle artışı hücrelerin su aldığını, azalışı su kaybettiğini gösterir; çözelti, özsuyuna eşit olduğunda kütle değişmez.','Artış → çözelti seyrek · azalış → çözelti derişik'),
       A('Aralığı bul','Kütlenin artıştan azalışa geçtiği yer %4 ile %6’lık çözeltiler arasındadır; özsuyu derişimi bu aralıktadır.','%4 ile %6 arasında')],
 dict(dogru=araliklar[2],yan=[(araliklar[0],'Kütlenin en çok arttığı çözeltileri özsuyunun derişimi sanmış; o çözeltiler özsuyundan çok daha seyrektir.','bilgi'),
      (araliklar[1],'Kütle artışının azaldığı ilk aralığı seçmiş; %4’lük çözeltide kütle hâlâ artıyor, çözelti özsuyundan seyrektir.','dikkat'),
      (araliklar[3],'Kütle azalmasının sürdüğü aralığı seçmiş; %6’lıkta kütle zaten azalmış, özsuyu daha seyrektir.','dikkat'),
      (araliklar[4],'Kütlenin azaldığı bütün çözeltilerin özsuyundan derişik olduğunu görmeyip en derişik çözeltiden fazlasını seçmiş.','bilgi')],sira=araliklar),
 'patates silindirleri kütle tablosu','tablodan özsuyu derişimi aralığı','Kütlesi değişmeyen çözelti özsuyuna eşittir; kütlenin artıştan azalışa geçtiği aralık özsuyu derişimini kapsar.','Kütle artışının en çok olduğu çözeltiyi özsuyuyla eşit saymak.',
 alt='Madde geçişleri',z='kolay',kalip='tablo',kaz='Deney tablosundan hücre özsuyu derişimini tahmin eder.',sekil=SK[27],
 metin='Bir öğrenci, aynı patatesten kesilen ve kütleleri eşit olan beş silindiri farklı derişimlerdeki şeker çözeltilerine koyuyor (%0, saf suyu gösterir). Bir süre bekledikten sonra silindirlerin kütlesini ölçüyor ve sonuçları tabloya yazıyor. Şeker, patates hücrelerinin zarından geçmemektedir.\nBuna göre, patates hücrelerinin özsuyu derişimi aşağıdaki aralıklardan hangisinde olabilir?',
 istenen='Patates hücre özsuyunun derişim aralığı.',ip=['Kütlenin yönünü her satırda yorumla.'],
 bilgi=[B('Kütle değişimi ve ozmoz','Hücreler seyrek ortamda su alır, derişik ortamda su verir')],
 puf='Kütle değişiminin işareti artıdan eksiye döndüğü aralık, özsuyuna eşit derişimi kapsar.')
# ---- 28 · alyuvar hemoliz öncüllü (zor, yanlış) ----
SK[28]=sekil_fhm()
d28={'I':(False,'Alyuvar büzüşmüştür; su kaybetmiştir, bu yüzden çözelti hipertoniktir.','hipertonik'),
     'II':(False,'İzotonik ortamda da su girişi ve çıkışı sürer; yalnız ikisi eşit olduğundan net değişim yoktur.','su geçişi var'),
     'III':(True,'Hipotonik ortamda alyuvar su alır; hücre duvarı olmadığından hacim artışı sınırlanamaz ve hücre patlar (hemoliz).','hipotonik, hemoliz')}
qo(28,onc(d28,'B','yanlis'),'üç alyuvarın durumu','alyuvarlarda büzülme ve hemoliz',
 'Büzüşen, normal ve patlayan alyuvar şekilleri ortamın türüyle ilişkilendirilir; “su alışverişi durmuştur” yanılgısı eklenmiştir.','İzotonik ortamda su geçişinin durduğunu sanmak.',
 alt='Madde geçişleri',z='zor',kalip='öncüllü',kaz='Alyuvarın şeklinden ortamın türünü ve su dengesini yorumlar.',sekil=SK[28],
 metin='Şekilde, aynı kandan alınan üç alyuvar örneği, derişimleri farklı I, II ve III numaralı üç çözeltiye konulup bir süre bekletildikten sonraki durumlarıyla gösterilmiştir. Alyuvarların başlangıçta normal biçimde olduğu bilinmektedir.\nI. I numaralı alyuvarın bulunduğu çözelti hipotoniktir.\nII. II numaralı alyuvarın hücre zarından hiç su geçişi olmamıştır.\nIII. III numaralı alyuvarın bulunduğu çözelti hipotoniktir ve alyuvar, hücre duvarı olmadığı için patlayabilmiştir.\nBuna göre, bu yargılardan hangileri yanlıştır?',
 istenen='Şekle göre yanlış olan yargılar.',ip=['Her alyuvarın şeklinden suyla ilgili durumunu çıkar.'],
 bilgi=[B('Hayvan hücresinde su dengesi','Hayvan hücresinde hücre duvarı yoktur · Hipertonik ortamda hücre büzülür, hipotonik ortamda şişer ve patlayabilir (hemoliz), izotonik ortamda şekil korunur')],
 puf='Büzüşen hücre hipertonik, patlayan hücre hipotonik ortamdadır; izotonik ortamda su yine geçer ama net değişim sıfırdır.')
# ---- 29 · bitki–hayvan hacim grafiği (zor) ----
SK[29]=sekil_g29()
qt(29,[A('Eğrileri oku','K eğrisi bir süre yükselip yatay hâle geliyor; L eğrisi sürekli yükseliyor ve hücre parçalanarak sona eriyor.','K: artar sonra sabitlenir · L: artar, parçalanır'),
       A('Ortamı değerlendir','İki hücre de su alıyor; ortam hipotoniktir. Hücre duvarı olan hücrede duvar, hacim artışını sınırlar ve hücre patlamaz.','Hipotonik ortam · duvar patlamayı önler'),
       A('Hücreleri belirle','Patlamayan K bitki hücresidir; duvarsız ve patlayan L hayvan hücresidir.','K: bitki · L: hayvan'),
       A('Yargıları ele','Sabitlenmeyi derişimlerin eşitlenmesine bağlayan, duvarın etkisini yanlış hücreye veren ya da su alma hızını gerekçe gösteren yargılar yanlıştır.','Yalnız duvarın sınırlaması doğru')],
 tek('E','K eğrisi bir bitki hücresine aittir; çünkü hücre duvarı hücrenin hacmini sınırlayarak patlamasını önler.',
  [('K eğrisi bir hayvan hücresine aittir; çünkü hayvan hücresinin hacmi bir süre sonra kendiliğinden sabitlenir.','Hacmin sabitlenmesini hayvan hücresine özgü sanmış; hayvan hücresini sınırlayan duvar yoktur, L’nin parçalanması bunu gösterir.','bilgi'),
   ('L eğrisi bir bitki hücresine aittir; çünkü hücre duvarı olan hücreler su aldığında parçalanır.','Duvarın hücreyi patlattığını sanmış; duvar patlamayı önler.','bilgi'),
   ('K eğrisindeki hacim artışının durması, hücre içi ile hücre dışı çözeltinin derişimlerinin eşitlenmesinden kaynaklanır.','Duvarın sınırlayıcı etkisini görmeyip artışın durmasını derişim eşitlenmesine bağlamış; ortam hâlâ hipotoniktir.','bilgi'),
   ('L eğrisi bir bitki hücresine aittir; çünkü bitki hücrelerine su girişi hayvan hücrelerine göre çok daha hızlıdır.','Parçalanmayı su alma hızına bağlamış; asıl fark hücre duvarının varlığıdır.','bilgi')]),
 'bitki ve hayvan hücresinin hipotonik ortamda hacmi','grafikle duvarın rolü','Hipotonik ortamda hayvan hücresi patlayabilir; bitki hücresini hücre duvarı korur ve hacim artışı bir noktada durur.','Hacim artışının durmasını derişimlerin eşitlenmesine bağlamak.',
 alt='Madde geçişleri',z='zor',kalip='grafik',kaz='Hacim–zaman grafiğinden hücre türünü ve hücre duvarının işlevini çıkarır.',sekil=SK[29],
 metin='Biri bitki, diğeri hayvan hücresi olan iki hücre, aynı hipotonik çözeltiye konuyor. Hücrelerin hacminin zamanla değişimi grafikte K ve L eğrileriyle gösterilmiştir.\nBuna göre, aşağıdakilerden hangisi söylenebilir?',
 istenen='Grafiğe göre doğru olan yargı.',ip=['Eğrilerin ilk eğimini ve sonraki gidişini karşılaştır.'],
 bilgi=[B('Hücre duvarı','Hücre duvarı bitki hücresini destekler')],
 puf='Hipotonik ortamda patlayan hücre duvarsız hayvan hücresidir; duvarlı bitki hücresinde hacim artışı sınırlanır.')
# ---- 30 · plazmoliz–deplazmoliz hesabı (zor) ----
OZS={'K':3,'L':6,'M':9,'N':12,'P':4}; OLU={'P'}; DIS=10
plaz=sorted(h for h,o in OZS.items() if h not in OLU and o<DIS); deplaz=plaz  # canlı plazmolizli hücreler saf suda deplazmoliz yapar
assert plaz==['K','L','M'] and sorted(h for h in OZS if OZS[h]>DIS)==['N']
def kume(x): return ', '.join(x[:-1])+' ve '+x[-1] if len(x)>2 else ' ve '.join(x)
ops30=['K ve L','K ve P','L ve M',kume(deplaz),'K, L, M ve P']
assert ops30[3]=='K, L ve M'
qt(30,[A('Plazmolizi bul','Hücre, özsuyundan derişik bir çözeltiye konunca su kaybeder; özsuyu %10’dan düşük olan canlı hücreler K, L ve M’dir.','K: %3 · L: %6 · M: %9 → plazmoliz'),
       A('Diğer hücreleri ele','N’nin özsuyu %12 olduğundan su alır, plazmoliz olmaz. P kaynatılarak öldürüldüğü için zarı seçici geçirgenliğini yitirmiştir ve plazmoliz yapmaz.','N: su alır · P: ölü'),
       A('Deplazmolizi belirle','Plazmoliz olan canlı hücreler saf suya alınınca su alıp eski haline döner; K, L ve M’de deplazmoliz gözlenir.','K, L ve M: plazmoliz → deplazmoliz')],
 dict(dogru='K, L ve M',yan=[('K ve L','Özsuyu %9 olan M’nin de %10’luk çözeltiden daha seyrek olduğunu görmeyip plazmolizi yalnız en düşük iki hücrede aramış.','islem'),
      ('K ve P','Ölü P hücresinin de özsuyu düşük olduğu için plazmoliz yaptığını sanmış; ölü hücrede zar seçici geçirgenliğini yitirmiştir.','bilgi'),
      ('L ve M','K hücresinin özsuyunun en düşük olduğunu, dolayısıyla çözeltiden en çok etkilenen hücre olduğunu atlamış.','dikkat'),
      ('K, L, M ve P','Ölü P hücresini de plazmoliz yapan hücrelerden saymış; ölü hücrede plazmoliz de deplazmoliz de olmaz.','bilgi')],sira=ops30),
 'beş hücrenin %10’luk çözeltideki durumu','canlı–ölü hücre ve özsuyu derişimi','Plazmoliz için hücrenin canlı olması ve çözeltinin özsuyundan derişik olması gerekir; plazmolizli canlı hücre saf suda deplazmoliz yapar.','Ölü hücrede de plazmoliz olacağını sanmak.',
 alt='Madde geçişleri',z='zor',kalip='hikâyeli',kaz='Özsuyu derişimi ve canlılık koşullarını birlikte değerlendirerek plazmoliz–deplazmoliz sonucunu bulur.',
 metin='Özsuyu derişimleri K hücresinde %3, L hücresinde %6, M hücresinde %9, N hücresinde %12 ve P hücresinde %4 olan beş bitki hücresi hazırlanıyor. P hücresi, deneyden önce kaynatılarak öldürülüyor; diğer hücreler canlıdır. Hücrelerin hepsi %10’luk şeker çözeltisine konuyor. Şeker hücre zarından geçemiyor. Bir süre sonra plazmoliz gözlenen hücreler saf suya aktarılıyor.\nBuna göre, hangi hücrelerde önce plazmoliz, sonra deplazmoliz gözlenir?',
 istenen='Plazmoliz ardından deplazmoliz gözlenen hücreler.',ip=['Plazmoliz için çözeltinin ve hücrenin hangi koşulları sağlaması gerektiğini yaz; her hücreyi bu koşullarla tek tek sına.'],
 bilgi=[B('Plazmoliz ve deplazmoliz','Hipertonik ortamda su kaybeden bitki hücresi plazmoliz olur; hipotonik ortamda su alarak eski haline dönmesine deplazmoliz denir')],
 puf='Plazmoliz için hücre canlı ve çözelti özsuyundan derişik olmalı; plazmolizli canlı hücre saf suda eski haline döner.')
# ==SONRAKI==

assert len(P.ANA)==30 and all(f'{n:04d}' in P.ANA[n-1]['id'] for n in range(1,31))
bitir(P,'hucreiki',UK)
