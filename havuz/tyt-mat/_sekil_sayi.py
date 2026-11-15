"""tksek ve basamaksek için ortak TikZ yardımcıları (sayı konuları şekilleri)."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _hafif_mat import *
from cizim import tikz_svg
def tz(govde,ek=''):
    return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small'+ek+']\n'+govde+'\n\\end{tikzpicture}')
def nd(x,y,t,w=.9,h=.65,fill=None,st='',name=None,bold=False):
    f=f',fill={fill}' if fill else ''
    nm=f'({name})' if name else ''
    tt=f'\\textbf{{{t}}}' if bold else t
    return f'\\node[draw,minimum width={w}cm,minimum height={h}cm,inner sep=1pt{f}{(","+st) if st else ""}] {nm} at ({x:.3f},{y:.3f}) {{{tt}}};'
def tx(x,y,t,st=''): return f'\\node[{st}] at ({x:.3f},{y:.3f}) {{{t}}};'
def ln(x1,y1,x2,y2,st=''): return f'\\draw[{st}] ({x1:.3f},{y1:.3f}) -- ({x2:.3f},{y2:.3f});'
SEG={'0':'abcdef','1':'bc','2':'abdeg','3':'abcdg','4':'bcfg','5':'acdfg','6':'acdefg','7':'abc','8':'abcdefg','9':'abcdfg'}
def seg7(x,y,d,sc=1.0,on='line width=2.2pt',off='line width=2.2pt,black!12'):
    """tek haneli yedi bölmeli gösterge; (x,y) sol alt köşe; genişlik .55*sc, yükseklik 1*sc."""
    w=.5*sc; h=.5*sc; g=.07*sc
    P={'a':((g,2*h),(w-g,2*h)),'b':((w,2*h-g),(w,h+g)),'c':((w,h-g),(w,g)),'d':((g,0),(w-g,0)),'e':((0,h-g),(0,g)),'f':((0,2*h-g),(0,h+g)),'g':((g,h),(w-g,h))}
    o=[]
    for k,((x1,y1),(x2,y2)) in P.items():
        o.append(f'\\draw[{on if k in SEG[d] else off}] ({x+x1:.3f},{y+y1:.3f}) -- ({x+x2:.3f},{y+y2:.3f});')
    return '\n'.join(o)
