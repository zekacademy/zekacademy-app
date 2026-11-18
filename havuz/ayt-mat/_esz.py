"""Eşitsizlikler paketi yardımcıları: aralık çözücü, şekil çizicileri."""
import sys,os
HD=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,os.path.join(HD,'..','tyt-mat')); sys.path.insert(0,os.path.join(HD,'..'))
from fractions import Fraction as Fr
from cizim import tikz_svg
def fmt(c):
    c=Fr(c); return ('−' if c<0 else '')+(str(abs(c.numerator)) if c.denominator==1 else f'{abs(c.numerator)}/{c.denominator}')
def S(pred,crit):
    crit=sorted(set(Fr(c) for c in crit)); n=len(crit)
    def P(x):
        try: return bool(pred(x))
        except ZeroDivisionError: return False
    tv=[]
    for i in range(2*n+1):
        if i%2: tv.append(P(crit[i//2]))
        else:
            k=i//2
            x=crit[0]-1 if k==0 else (crit[-1]+1 if k==n else (crit[k-1]+crit[k])/2)
            tv.append(P(x))
    runs=[];i=0
    while i<=2*n:
        if tv[i]:
            j=i
            while j+1<=2*n and tv[j+1]: j+=1
            runs.append((i,j)); i=j+1
        else: i+=1
    out=[]
    for i,j in runs:
        if i==j and i%2: out.append('{'+fmt(crit[i//2])+'}'); continue
        if i==0: l='(−∞'
        elif i%2==0: l='('+fmt(crit[i//2-1])
        else: l='['+fmt(crit[(i-1)//2])
        if j==2*n: r='∞)'
        elif j%2==0: r=fmt(crit[j//2])+')'
        else: r=fmt(crit[(j-1)//2])+']'
        out.append(l+', '+r)
    return ' ∪ '.join(out) if out else '∅'
def ints(pred,lo=-60,hi=60): return [x for x in range(lo,hi+1) if (lambda v:(pred(Fr(v)) if True else 0))(x)]
def okpred(pred):
    def P(x):
        try: return bool(pred(x))
        except ZeroDivisionError: return False
    return P
def tam(pred,lo=-60,hi=60):
    P=okpred(pred); return [x for x in range(lo,hi+1) if P(Fr(x))]
def place(dogru,yanlis,hedef):
    assert len(yanlis)==4; L=list(yanlis); L.insert('ABCDE'.index(hedef),dogru); assert len(set(L))==5,L; return L
def fig(body,font='\\small'):
    return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font='+font+']\n'+body+'\n\\end{tikzpicture}')
def axes(x0,x1,y0,y1,sx,sy,xt=None,yt=None,fs='\\footnotesize',xl='$x$',yl='$y$',grid=True):
    o=[]
    xt=list(range(x0,x1+1)) if xt is None else xt; yt=list(range(y0,y1+1)) if yt is None else yt
    if grid:
        for i in range(x0,x1+1): o.append(f'\\draw[gray!30,thin] ({i*sx:.3f},{y0*sy:.3f}) -- ({i*sx:.3f},{y1*sy:.3f});')
        for j in range(y0,y1+1): o.append(f'\\draw[gray!30,thin] ({x0*sx:.3f},{j*sy:.3f}) -- ({x1*sx:.3f},{j*sy:.3f});')
    o.append(f'\\draw[-{{Stealth}},thick] ({(x0-0.4)*sx:.3f},0) -- ({(x1+0.7)*sx:.3f},0) node[right] {{{xl}}};')
    o.append(f'\\draw[-{{Stealth}},thick] (0,{(y0-0.4)*sy:.3f}) -- (0,{(y1+0.7)*sy:.3f}) node[above] {{{yl}}};')
    for i in xt:
        if i!=0: o.append(f'\\node[below=4pt,font={fs},inner sep=0.5pt] at ({i*sx:.3f},0) {{${i}$}};'.replace('${i}$',f'${i}$'))
    for j in yt:
        if j!=0: o.append(f'\\node[left=2pt,font={fs},fill=white,inner sep=0.5pt] at (0,{j*sy:.3f}) {{${j}$}};')
    o.append(f'\\node[below right,font={fs},inner sep=1pt] at (0,0) {{$O$}};')
    return '\n'.join(o)
def curve(f,xa,xb,sx,sy,ylo,yhi,renk,w='1.7pt',step=0.04):
    segs=[];cur=[];x=xa
    n=int(round((xb-xa)/step))
    for k in range(n+1):
        x=xa+k*step; y=float(f(Fr(x).limit_denominator(1000)))
        if ylo<=y<=yhi: cur.append((x,y))
        else:
            if len(cur)>1: segs.append(cur)
            cur=[]
    if len(cur)>1: segs.append(cur)
    return '\n'.join(f'\\draw[{renk},line width={w}] '+' -- '.join(f'({a*sx:.3f},{b*sy:.3f})' for a,b in s)+';' for s in segs)
def sign_table(crit,rows,fs='\\small'):
    """crit: kritik değerler; rows: (etiket, işaretler[n+1], {indis:'0'|'∄'})."""
    n=len(crit); W=1.7; X0=1.5; xs=[X0+W*(i+1) for i in range(n)]
    o=[]; top=0.0; rh=0.85
    o.append(f'\\node[font={fs}\\bfseries] at (0.6,0) {{$x$}};')
    o.append(f'\\node[font={fs}] at ({X0+0.4},0) {{$-\\infty$}};')
    for i,c in enumerate(crit): o.append(f'\\node[font={fs}] at ({xs[i]},0) {{${fmt(c).replace("−","-")}$}};')
    o.append(f'\\node[font={fs}] at ({xs[-1]+W-0.4},0) {{$+\\infty$}};')
    H=rh*(len(rows)+0.5)
    o.append(f'\\draw[thick] (0,-0.4) -- ({xs[-1]+W},-0.4);')
    o.append(f'\\draw[thick] ({X0-0.2},0.4) -- ({X0-0.2},{-0.4-rh*len(rows)});')
    for i,xv in enumerate(xs): o.append(f'\\draw[dashed,gray] ({xv},-0.4) -- ({xv},{-0.4-rh*len(rows)});')
    for r,(lab,sg,zr) in enumerate(rows):
        y=-0.4-rh*(r+0.5)
        o.append(f'\\node[font={fs}\\bfseries] at (0.6,{y}) {{{lab}}};')
        for i,s in enumerate(sg):
            s=s.replace('-','−')
            xm=(X0+0.4) if i==0 else ((xs[-1]+W-0.4) if i==n else (xs[i-1]+xs[i])/2)
            col={'+':'blue!70!black','−':'red!70!black'}[s]
            o.append(f'\\node[font=\\large\\bfseries,text={col}] at ({xm},{y}) {{{"$+$" if s=="+" else "$-$"}}};')
        for i,z in zr.items(): o.append(f'\\node[font={fs},fill=white,inner sep=1pt] at ({xs[i]},{y}) {{{"$0$" if z=="0" else "$\\nexists$"}}};')
        o.append(f'\\draw[gray!60] (0,{-0.4-rh*(r+1)}) -- ({xs[-1]+W},{-0.4-rh*(r+1)});')
    return '\n'.join(o)
def nline(lo,hi,segs,sx=0.8,ticks=None):
    """segs: (a,b,solkapali,sagkapali) ; a/b None = sonsuz."""
    o=[f'\\draw[-{{Stealth}},thick] ({(lo-0.6)*sx:.3f},0) -- ({(hi+0.8)*sx:.3f},0) node[right] {{$x$}};']
    for t in (range(lo,hi+1) if ticks is None else ticks):
        o.append(f'\\draw[thick] ({t*sx:.3f},-0.1) -- ({t*sx:.3f},0.1); \\node[below=3pt,font=\\small] at ({t*sx:.3f},0) {{${t}$}};')
    for a,b,lc,rc in segs:
        xa=(lo-0.5)*sx if a is None else a*sx; xb=(hi+0.5)*sx if b is None else b*sx
        o.append(f'\\draw[line width=4pt,orange!85!black,opacity=.75] ({xa:.3f},0.28) -- ({xb:.3f},0.28);')
        if a is not None: o.append(f'\\draw[thick,orange!60!black,fill={"orange!85!black" if lc else "white"}] ({xa:.3f},0.28) circle (0.11);')
        if b is not None: o.append(f'\\draw[thick,orange!60!black,fill={"orange!85!black" if rc else "white"}] ({xb:.3f},0.28) circle (0.11);')
    return '\n'.join(o)
