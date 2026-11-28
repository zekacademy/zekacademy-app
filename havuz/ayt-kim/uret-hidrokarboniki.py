"""AYT Kimya · Hidrokarbonlar (Alkan, Alken, Alkin) · 2. dalga · 10 soru. Yapılar SMILES benzeri dizgeyle tanımlanır; formül, ad, ürün ve izomer sayıları kodla
hesaplanır; her cevap ve çeldirici Python'da assert edilir. Şekiller TikZ (cizim.tikz_svg)."""
import sys,os,json,math,itertools,re
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-kim')); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
import _hafif_kim2 as H
from _hafif_kim2 import *
from cizim import tikz_svg
from collections import Counter
KONU='Hidrokarbonlar (Alkan, Alken, Alkin)'; H.KONU=KONU
P=Parti('hidrokarboniki',KONU,'akim|'+KONU,ders='AYT Kimya',idon='aytkim')
SUB=str.maketrans('0123456789n','₀₁₂₃₄₅₆₇₈₉ₙ')
def sb(s): return s.translate(SUB)           # C3H6 -> C₃H₆
def frm(c,h): return 'C'+(sb(str(c)) if c>1 else '')+'H'+(sb(str(h)) if h>1 else '')

# ---------------- yapı modeli (açık zincirli, halka yok) ----------------
class Mol:
    def __init__(s,smi):
        s.smi=smi; s.el=[]; s.b=[]; st=[]; prev=None; o=1; i=0
        while i<len(smi):
            ch=smi[i]
            if ch=='(': st.append(prev); i+=1; continue
            if ch==')': prev=st.pop(); i+=1; continue
            if ch=='=': o=2; i+=1; continue
            if ch=='#': o=3; i+=1; continue
            if smi[i:i+2] in ('Cl','Br'): e=smi[i:i+2]; i+=2
            else: e=ch; i+=1
            s.el.append(e); k=len(s.el)-1
            if prev is not None: s.b.append((prev,k,o))
            prev=k; o=1
        s.adj={i:[] for i in range(len(s.el))}
        for a,b_,o in s.b: s.adj[a].append((b_,o)); s.adj[b_].append((a,o))
        val={'C':4,'O':2,'Cl':1,'Br':1}
        for i,e in enumerate(s.el): assert sum(o for _,o in s.adj[i])<=val[e],(smi,i)
    def nH(s,i):
        assert s.el[i]=='C'; return 4-sum(o for _,o in s.adj[i])
    def formula(s):
        c=sum(1 for e in s.el if e=='C'); h=sum(s.nH(i) for i in range(len(s.el)) if s.el[i]=='C')
        return c,h,Counter(e for e in s.el if e!='C')
    def carbons(s): return [i for i,e in enumerate(s.el) if e=='C']
    def mult(s): return [(a,b_,o) for a,b_,o in s.b if o>1]

def enc(M,v,par,skip=()):
    ch=sorted(f'{o}'+enc(M,w,v) for w,o in M.adj[v] if w!=par)
    return M.el[v]+'('+','.join(ch)+')'
def canon(M):
    return min(enc(M,r,None) for r in range(len(M.el)))
def same(M1,M2): return canon(M1)==canon(M2)

# ---------------- IUPAC adlandırma (açık zincirli, metil/etil/halojen sübstitüent) ----------------
KOK={1:'met',2:'et',3:'prop',4:'büt',5:'pent',6:'heks',7:'hept',8:'okt',9:'non',10:'dek'}
MULT={1:'',2:'di',3:'tri',4:'tetra',5:'penta'}
def paths(M):
    C=M.carbons(); res=[]
    nb=lambda v:[w for w,_ in M.adj[v] if M.el[w]=='C']
    leaves=[v for v in C if len(nb(v))<=1]
    for a in leaves:
        for b_ in leaves:
            if a==b_ and len(C)>1: continue
            # tek yol (ağaç)
            st=[(a,[a])]
            while st:
                v,p=st.pop()
                if v==b_: res.append(p); break
                for w in nb(v):
                    if w not in p: st.append((w,p+[w]))
    return res
def dal_adi(M,v,par):
    """sübstitüent adı (yalnız doğrusal alkil/halojen)"""
    if M.el[v]=='Cl': return 'kloro'
    if M.el[v]=='Br': return 'bromo'
    if M.el[v]=='O': return 'hidroksi'
    n=0; x=v; p=par
    while True:
        n+=1; nx=[w for w,o in M.adj[x] if w!=p]
        assert all(o==1 for w,o in M.adj[x] if w!=p),'doymamış dal'
        if not nx: break
        assert len(nx)==1,'dallanmış alkil'
        p,x=x,nx[0]
    return {1:'metil',2:'etil',3:'propil'}[n]
def isim_dizi(M,path,sec_zincir=None):
    """path doğrultusunda adlandır; (anahtar, ad) döndür"""
    pos={v:i+1 for i,v in enumerate(path)}
    mlt=[]; 
    for a,b_,o in M.mult():
        assert a in pos and b_ in pos,'çok katlı bağ zincir dışında'
        mlt.append((min(pos[a],pos[b_]),o))
    subs=[]
    for v in path:
        for w,o in M.adj[v]:
            if w not in pos: subs.append((pos[v],dal_adi(M,w,v)))
    return mlt,subs
def adlandir(M,kotu_yon=False,kisa_zincir=False):
    C=M.carbons(); ad=[]
    for p in paths(M):
        if len([1 for a,b_,o in M.mult() if a in p and b_ in p])!=len(M.mult()): continue
        ad.append(((-len(p) if not kisa_zincir else len(p)),p))
    bk=min(k for k,_ in ad); best=None; adlar=set()
    for k,p in ad:
        if k!=bk: continue
        for yon in (p,p[::-1]):
            mlt,subs=isim_dizi(M,yon)
            sk=(sorted(l for l,_ in mlt),sorted(l for l,_ in subs))
            if best is None or (sk>best if kotu_yon else sk<best): best=sk
    for k,p in ad:
        if k!=bk: continue
        for yon in (p,p[::-1]):
            mlt,subs=isim_dizi(M,yon)
            sk=(sorted(l for l,_ in mlt),sorted(l for l,_ in subs))
            if sk==best: adlar.add(_ad(M,yon,mlt,subs))
    assert len(adlar)==1,('belirsiz ad',adlar)
    return adlar.pop()
def _ad(M,yon,mlt,subs):
    n=len(yon); g={}
    for l,a in subs: g.setdefault(a,[]).append(l)
    on=[]
    for a in sorted(g,key=lambda x:x.replace('ö','o').replace('ü','u')):
        ls=sorted(g[a]); on.append(','.join(map(str,ls))+'-'+MULT[len(ls)]+a)
    pre='-'.join(on)
    if not mlt: kok=KOK[n]+'an'
    else:
        l,o=mlt[0]; son='en' if o==2 else 'in'
        kok=(('' if n<=3 else f'{l}-'))+KOK[n]+son
    return (pre+'-'+kok if kok[0].isdigit() else pre+kok) if pre else kok
def buyuk(s):
    for i,ch in enumerate(s):
        if ch.isalpha(): return s[:i]+ch.upper()+s[i+1:]
    return s
def AD(smi,**k): return buyuk(adlandir(Mol(smi),**k))

# ---------------- iskelet (çizgi) formülü çizimi ----------------
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
BL=1.05   # bağ uzunluğu (cm)
def yerlesim(M,kok=0,stereo=None,ilk=30,esnek=None):
    stereo=stereo or {}; esnek=esnek or {}
    pos={kok:(0.0,0.0)}; yon={}; turn={}; par={kok:None}
    def cs(v): return [(w,o) for w,o in M.adj[v] if w!=par[v]]
    def koy(v,w,a):
        yon[w]=a; par[w]=v; pos[w]=(pos[v][0]+BL*math.cos(math.radians(a)),pos[v][1]+BL*math.sin(math.radians(a)))
    def git(v):
        ch=cs(v)
        if not ch: return
        k=len(ch)
        if par[v] is None:
            acilar=[ilk,ilk+120,ilk-120,ilk+60][:k] if k>1 else [ilk]
            for (w,o),a in zip(ch,acilar): koy(v,w,a); turn[w]=1
        else:
            phi=yon[v]; inc=[o for w,o in M.adj[v] if w==par[v]][0]; t=turn[v]; s=-t
            if v in esnek: s=esnek[v]
            if k==1:
                w,o=ch[0]
                if inc==3 or o==3: a=phi; turn[w]=t
                else:
                    st=stereo.get((par[v],v))
                    if inc==2 and st:
                        a0=par[v]; pp=pos[a0]; ppp=pos[par[a0]]
                        d=(pos[v][0]-pp[0],pos[v][1]-pp[1]); cr=lambda q:d[0]*(q[1]-pp[1])-d[1]*(q[0]-pp[0])
                        sa=1 if cr(ppp)>0 else -1
                        for ss in (1,-1):
                            aa=phi+60*ss; q=(pos[v][0]+BL*math.cos(math.radians(aa)),pos[v][1]+BL*math.sin(math.radians(aa)))
                            sg=1 if cr(q)>0 else -1
                            if (st=='cis')==(sg==sa): a=aa; s=ss
                        turn[w]=s
                    else: a=phi+60*s; turn[w]=s
                koy(v,w,a)
            elif k==2:
                (w1,o1),(w2,o2)=ch
                koy(v,w2,phi+60*s); turn[w2]=s
                koy(v,w1,phi-60*s); turn[w1]=-s
            else:
                (wa,_),(wb,_),(wc,_)=ch[:3]
                koy(v,wc,phi); turn[wc]=t
                koy(v,wa,phi+90); turn[wa]=1
                koy(v,wb,phi-90); turn[wb]=-1
        for w,o in ch: git(w)
    git(kok)
    return pos
def cizgi(M,pos,ox=0.0,oy=0.0,etiket=True):
    out=[]; L=lambda a:(pos[a][0]+ox,pos[a][1]+oy)
    for a,b_,o in M.b:
        p=L(a); q=L(b_); dx,dy=q[0]-p[0],q[1]-p[1]; ln=math.hypot(dx,dy); ux,uy=dx/ln,dy/ln; nx,ny=-uy,ux
        ca=0.0 if M.el[a]=='C' else 0.23; cb=0.0 if M.el[b_]=='C' else 0.23
        p2=(p[0]+ux*ca,p[1]+uy*ca); q2=(q[0]-ux*cb,q[1]-uy*cb)
        offs={1:[0],2:[-0.06,0.06],3:[-0.09,0,0.09]}[o]
        for d in offs:
            out.append(f'\\draw[thick] ({p2[0]+nx*d:.3f},{p2[1]+ny*d:.3f}) -- ({q2[0]+nx*d:.3f},{q2[1]+ny*d:.3f});')
    for i,e in enumerate(M.el):
        if e!='C' and etiket: x,y=L(i); out.append(f'\\node at ({x:.3f},{y:.3f}) {{\\small {"OH" if e=="O" else e}}};')
    return out
def kutu(pos,ox=0,oy=0):
    xs=[p[0]+ox for p in pos.values()]; ys=[p[1]+oy for p in pos.values()]
    return min(xs),max(xs),min(ys),max(ys)
def ciz(smi,ox=0.0,oy=0.0,ad=None,stereo=None,kok=0,ilk=30,esnek=None,ad_dy=-0.45):
    M=Mol(smi); pos=yerlesim(M,kok,stereo,ilk,esnek); out=cizgi(M,pos,ox,oy)
    x0,x1,y0,y1=kutu(pos,ox,oy)
    if ad: out.append(f'\\node at ({(x0+x1)/2:.3f},{y0+ad_dy:.3f}) {{\\textbf{{{ad}}}}};')
    return out,(x0,x1,y0,y1)
def satir(liste,aralik=1.2,dy=0.5):
    """liste: (smi,ad,stereo) üçlüleri; ortak etiket tabanı"""
    ms=[(Mol(a),b_,c) for a,b_,c in liste]; poss=[yerlesim(m,stereo=c) for m,_,c in ms]
    ymin=min(p[1] for pos in poss for p in pos.values()); out=[]; x=0.0
    for (m,ad,c),pos in zip(ms,poss):
        x0=min(p[0] for p in pos.values()); ox=x-x0; out+=cizgi(m,pos,ox,0.0)
        x1=max(p[0] for p in pos.values())+ox; out.append(f'\\node at ({(x+x1)/2:.3f},{ymin-dy:.3f}) {{\\textbf{{{ad}}}}};'); x=x1+aralik
    return out
def tk(*parts):
    return tikz_svg(HEAD+'\n'.join(p if isinstance(p,str) else '\n'.join(p) for p in parts)+TAIL)

# ---------------- izomer / ürün sayımı (kaba kuvvet) ----------------
def _agaclar(n):
    if n==1: yield []; return
    if n==2: yield [(0,1)]; return
    for seq in itertools.product(range(n),repeat=n-2):
        deg=[1]*n
        for s in seq: deg[s]+=1
        if max(deg)>4: continue
        deg2=deg[:]; edges=[]
        for s in seq:
            for j in range(n):
                if deg2[j]==1: edges.append((j,s)); deg2[j]-=1; deg2[s]-=1; break
        u=[j for j in range(n) if deg2[j]==1]; edges.append((u[0],u[1])); yield edges
def smi_of(n,edges,ciftler=(),ucler=()):
    """kenar listesinden Mol nesnesi (SMILES üretmeden doğrudan)"""
    M=Mol('C'); M.el=['C']*n; M.b=[]
    for a,b_ in edges:
        o=2 if (a,b_) in ciftler or (b_,a) in ciftler else (3 if (a,b_) in ucler or (b_,a) in ucler else 1); M.b.append((a,b_,o))
    M.adj={i:[] for i in range(n)}
    for a,b_,o in M.b: M.adj[a].append((b_,o)); M.adj[b_].append((a,o))
    return M
def izomerler(n,tur):
    """açık zincirli, tek çok katlı bağlı C_n hidrokarbonlar (tur: 'alkan','alken','alkin'); (kanonik küme, geometrik çift sayısı)"""
    G={}
    for e in _agaclar(n):
        base=smi_of(n,e)
        if tur=='alkan':
            G[canon(base)]=base; continue
        for k,(a,b_) in enumerate(e):
            o=2 if tur=='alken' else 3
            M=smi_of(n,e,ciftler=[(a,b_)] if o==2 else (),ucler=[(a,b_)] if o==3 else ())
            if all(sum(x for _,x in M.adj[i])<=4 for i in range(n)): G[canon(M)]=M
    geo=0
    for M in G.values():
        for a,b_,o in M.b:
            if o==2:
                ok=True; subs=[]
                for u,v in ((a,b_),(b_,a)):
                    ch=[w for w,_ in M.adj[u] if w!=v]
                    if not ch: ok=False
                    if len(ch)==2 and enc(M,ch[0],u)==enc(M,ch[1],u): ok=False
                if ok: geo+=1
    return G,geo
def monoklor(smi):
    M=Mol(smi); n=len(M.el); S=set()
    for i in M.carbons():
        if M.nH(i)>0:
            N=Mol(smi); N.el=N.el+['Cl']; N.b=N.b+[(i,n,1)]
            N.adj={k:[] for k in range(n+1)}
            for a,b_,o in N.b: N.adj[a].append((b_,o)); N.adj[b_].append((a,o))
            S.add(canon(N))
    return len(S)
def dogrusal_karbon(M,pos):
    """üçlü bağ içeren zincirde aynı doğru üzerindeki en fazla karbon sayısı (geometrik: koordinatlardan)"""
    C=M.carbons(); best=0
    for a in C:
        for b_ in C:
            if a<b_:
                d=(pos[b_][0]-pos[a][0],pos[b_][1]-pos[a][1]); n=[c for c in C if abs(d[0]*(pos[c][1]-pos[a][1])-d[1]*(pos[c][0]-pos[a][0]))<1e-6]
                best=max(best,len(n))
    return best

# ---------------- soru yardımcıları ----------------
TIPAD={'hk2-ozellik':'Fiziksel özellik ve ayırt etme','hk2-yapi':'Bağ yapısı ve hibritleşme','hk2-katilma':'Katılma ürünleri ve hesapları','hk2-yanma':'Yanma hesapları','hk2-eldepolimer':'Eldesi, kraking ve polimerleşme'}
NK=[0]
def Q(tipId,z,alt,fikir,tuzak,kalip,metin,istenen,ip,bilgi,ad,puf,sekil=None,dogru=None,yan=None,sira=None,kaz=None,kisa=None):
    tip=TIPAD[tipId]; NK[0]+=1; n=NK[0]; no=f'{n:04d}'; kid=f'K-AKHID2-{n:02d}'
    kart(kid,alt,fikir,tuzak,z,kalip,len(ad),tipId,tip,'ÖSYM AYT 2018–2026 Hidrokarbonlar soruları (yalnız mantık) · MEB 11. sınıf kimya')
    mk(P,no,ad=ad,adim=len(ad),tipId=tipId,tip=tip,z=z,alt=alt,kaz=kaz or alt+' konusunda yorum ve hesap yapar.',kart=f'{kid} ({alt}) · özgün kurgu',kalip=kalip,
       metin=metin,dogru=dogru,yan=yan,istenen=istenen,ip=[ip],bilgi=bilgi,puf=puf,sekil=sekil,sira=sira,kisa=kisa)
def yer(dogru,digerler,harf):
    """doğru şıkkı 'ABCDE'[harf] konumuna koyar, diğerleri sırayla"""
    i='ABCDE'.index(harf); d=list(digerler); assert len(d)==4
    return d[:i]+[dogru]+d[i:]
RM=['I','II','III']
OS=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
OSET={'Yalnız I':{0},'Yalnız II':{1},'Yalnız III':{2},'I ve II':{0,1},'I ve III':{0,2},'II ve III':{1,2},'I, II ve III':{0,1,2}}
def onc(truth,neden,harf,yanlis_sor=False):
    """truth: 3 bool (öncülün doğruluğu); neden: öncül gerçeğini anlatan cümle parçası; harf: doğru şık konumu.
    yanlis_sor: kök 'yanlıştır' ise doğru şık yanlış öncüllerin kümesidir."""
    T={i for i in range(3) if truth[i]}
    anahtar={i for i in range(3) if not truth[i]} if yanlis_sor else T
    dog=[s for s in OS if OSET[s]==anahtar]; assert len(dog)==1; dog=dog[0]; p='ABCDE'.index(harf); ix=OS.index(dog)
    for comb in itertools.combinations(range(7),5):
        if ix in comb and comb.index(ix)==p: sec=[OS[j] for j in comb]; break
    else: raise AssertionError('şık konumu mümkün değil')
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

def pgf(govde,w='7cm',h='5.4cm',ek=''):
    return tikz_svg('\\begin{tikzpicture}[font=\\small]\n\\begin{axis}[width='+w+',height='+h+',tick label style={font=\\small},label style={font=\\small},'+ek+']\n'+govde+'\n\\end{axis}\n\\end{tikzpicture}')
def ok_(x1,y1,x2,y2,et=''):
    return f'\\draw[-{{Stealth[length=2mm,width=1.8mm]}},thick] ({x1:.3f},{y1:.3f}) -- ({x2:.3f},{y2:.3f}) node[midway,above,align=center,font=\\small]{{{et}}};'
def sinif_h(c,h):
    return {2*c+2:'Alkan',2*c:'Alken',2*c-2:'Alkin'}[h]
M_H,M_C,M_O,M_Cl=1,12,16,Fr(71,2)
def mol_kur(el,b):
    N=Mol('C'); N.el=list(el); N.b=list(b); N.adj={i:[] for i in range(len(el))}
    for a,b_,o in N.b: N.adj[a].append((b_,o)); N.adj[b_].append((a,o))
    return N
def hx_katil(M,X,kez=1,ters=False):
    """HX katılması: H, H sayısı fazla karbona; X diğerine (ters=True: zıt yön). Çok katlı bağı bir derece azaltır."""
    el=list(M.el); b=list(M.b)
    for _ in range(kez):
        N=mol_kur(el,b); mb=[(a,c,o) for a,c,o in N.b if o>1]; assert len(mb)==1
        a,c,o=mb[0]; ha,hc=N.nH(a),N.nH(c); assert ha!=hc
        hedef=c if ha>hc else a        # X buraya (H sayısı az olan)
        if ters: hedef=a if hedef==c else c
        b=[(p,q,(r-1 if (p,q,r)==(a,c,o) else r)) for p,q,r in b]; el.append(X); b.append((hedef,len(el)-1,1))
    return mol_kur(el,b)
def ayni(M,smi): return same(M,Mol(smi))
def okla(smi,etiket,ox=0.0,soru='?',stereo=None):
    o,bb=ciz(smi,ox,0.0,stereo=stereo); ym=(bb[2]+bb[3])/2; x1=bb[1]
    o.append(ok_(x1+0.45,ym,x1+2.35,ym,etiket)); o.append(f'\\node[font=\\large] at ({x1+2.9:.2f},{ym:.2f}) {{{soru}}};')
    return o


def tbl(bas,sat): return tablo_svg(bas,sat)
def bsr(*v): return sorted(v)

# ================= 01 · kraking · kolay · şekilli =================
S1a='CCCCCCC'; S1b='CCCC'
assert Mol(S1a).formula()[:2]==(7,16) and Mol(S1b).formula()[:2]==(4,10)
x1c=7-4; x1h=16-10; assert (x1c,x1h)==(3,6) and sinif_h(x1c,x1h)=='Alken'
assert AD('C=CC')=='Propen'
def prop1(c,h): return {2*c+2:'Alkan',2*c:'Alken',2*c-2:'Alkin'}[h]
assert prop1(3,8)=='Alkan' and prop1(3,4)=='Alkin'
# tepkime şeması
oa,bba=ciz(S1a,0.0,0.0); xb=bba[1]+0.5; ym=(bba[2]+bba[3])/2
ob,bbb=ciz(S1b,xb+1.9+0.5,ym-0.0)
sk1=tk(oa,[ok_(xb,ym,xb+1.9,ym,'katalizör')],ob,[f'\\node at ({bbb[1]+0.55:.2f},{ym:.2f}) {{\\Large +}};',f'\\node[font=\\large] at ({bbb[1]+1.2:.2f},{ym:.2f}) {{X}};'])
d1='Propen; molekülünde bir çift bağ bulunur.'
Q('hk2-eldepolimer','kolay','Kraking (hidrokarbon parçalanması)','Kraking tepkimesinde atom sayıları korunur; uzun zincirli alkan, daha kısa bir alkan ile bir alkene parçalanır.','Ürünün de alkan olduğunu sanmak; atom sayılarının eşitliğini kontrol etmemek.','şekilli',
 'Petrol rafinerilerinde uzun zincirli hidrokarbonlar ısı ve katalizör yardımıyla daha küçük moleküllere parçalanır. Heptanın (C₇H₁₆) bu yolla parçalanması şekilde gösterilmiştir; X, bütanla birlikte oluşan tek ürün olup açık zincirlidir.\nBuna göre, X ile ilgili aşağıdakilerden hangisi doğrudur?',
 'X’in adı ve özelliği.','Girenlerdeki karbon ve hidrojen sayılarından bütanınkileri çıkararak X’in formülünü bul; sonra bu formülün hangi sınıfa uyduğuna bak.',
 [B('Kraking','Kraking, büyük hidrokarbon moleküllerinin ısı ve katalizör etkisiyle küçük moleküllere parçalanmasıdır; atom sayıları korunur. Örnek: C₆H₁₄ → C₂H₆ + C₄H₈ biçiminde parçalanabilir')],
 [A('Atom sayısını eşitle','Ürünlerdeki toplam C ve H sayısı girenlerinkine eşit olmalıdır; bütan C₄H₁₀ içerir.','C: 7 − 4 = 3; H: 16 − 10 = 6'),
  A('Formülü yaz','X’in molekül formülü C₃H₆ bulunur.','C₃H₆'),
  A('Sınıfı belirle','n = 3 için CₙH₂ₙ formülü C₃H₆’dır; alken sınıfıdır ve bir çift bağ içerir.','Propen: CH₂=CH–CH₃')],
 'Eksik kalan atomlar X’tir; formül CₙH₂ₙ ise alkendir.',sekil=sk1,
 dogru=d1,sira=yer(d1,['Propan; molekülünde yalnız tek bağ bulunur.','Propen; genel formülü CₙH₂ₙ₊₂’dir.','Propin; molekülünde bir üçlü bağ bulunur.','Propan; bromlu suyun rengini giderir.'],'A'),
 yan=[('Propan; molekülünde yalnız tek bağ bulunur.','Ürünün de alkan olduğunu düşünüp C₃H₈ yazmış; oysa C₃H₈ ile bütan birlikte 7 karbon ve 18 hidrojen eder, girenin hidrojen sayısı 16’dır.','dikkat'),
      ('Propen; genel formülü CₙH₂ₙ₊₂’dir.','Adı doğru bulmuş ama sınıfı karıştırmış; C₃H₆ için CₙH₂ₙ₊₂ bağıntısı 8 hidrojen verirdi, 6 hidrojen CₙH₂ₙ’ye uyar.','bilgi'),
      ('Propin; molekülünde bir üçlü bağ bulunur.','Hidrojen sayısını yanlış bulup C₃H₄ yazmış; oysa C₃H₄ ile bütan birlikte 14 hidrojen eder, girenin hidrojen sayısı 16’dır.','dikkat'),
      ('Propan; bromlu suyun rengini giderir.','C₃H₈ yazıp ayrıca doymuş bir bileşiğin bromlu suyun rengini giderdiğini sanmış; propan karanlıkta bromlu suyla tepkime vermez.','bilgi')])

# ================= 02 · orbital örtüşmesi ve sigma · kolay · şekilli =================
S2='CC#CC'; M2=Mol(S2); c2,h2,_=M2.formula(); assert (c2,h2)==(4,6)
sig2=len(M2.b)+h2; pi2=sum(o-1 for _,_,o in M2.b); assert sig2==9 and pi2==2 and sig2+pi2==11
assert len(M2.b)==3
sk2=tk(ciz(S2)[0])
d2='sp – sp; 9'
Q('hk2-yapi','kolay','Sigma bağı sayısı ve örtüşen orbitaller','Her tek bağ bir σ; çift bağ 1σ+1π, üçlü bağ 1σ+2π içerir. Üçlü bağın karbonları sp, çift bağın karbonları sp², tek bağlı karbonlar sp³ hibritleşmesi yapar.','π bağlarını da σ saymak; yalnız C–C bağlarını saymak; hidrojenleri unutmak.','şekilli',
 'Açık zincirli bir hidrokarbonun çizgi formülü şekilde verilmiştir (₁H, ₆C).\nBuna göre, bu bileşikte karbon–karbon üçlü bağındaki σ bağını oluşturan örtüşen orbitaller ile moleküldeki toplam σ bağı sayısı aşağıdakilerden hangisinde doğru verilmiştir?',
 'Üçlü bağdaki σ bağının orbitalleri ve toplam σ bağı sayısı.','Çizgi formülünde uçlarda ve köşelerde karbon, her karbonun bağ sayısı dörde tamamlanacak kadar hidrojen vardır; önce hidrojenleri yaz, sonra tek, çift ve üçlü bağın σ içeriğine bak.',
 [B('σ ve π bağları','Tek bağlar yalnız σ, çift bağ 1σ + 1π, üçlü bağ 1σ + 2π içerir. Örnek: CH₂=CH₂ molekülünde 1 C–C σ, 4 C–H σ olmak üzere 5 σ ve 1 π bağı vardır')],
 [A('Hidrojenleri tamamla','Köşelerdeki karbonların bağ sayısı dörde tamamlanır: uçtaki iki karbon 3’er, üçlü bağdaki iki karbon hiç hidrojen taşımaz; toplam 6 hidrojen.','C₄H₆'),
  A('Üçlü bağın σ bağı','Üçlü bağı oluşturan karbonlar sp hibritleşmesi yapar; aralarındaki σ bağı sp–sp örtüşmesidir, kalan 2 bağ π’dir.','sp – sp'),
  A('σ bağlarını say','3 C–C bağının her biri (üçlü bağ dahil) 1 σ içerir; 6 C–H bağı da σ’dır.','3 + 6 = 9 σ')],
 'Üçlü bağ: 1σ + 2π; her C–H bağı bir σ’dır.',sekil=sk2,
 dogru=d2,sira=yer(d2,['sp – sp; 3','sp – sp; 11','sp² – sp²; 9','sp³ – sp³; 9'],'E'),
 yan=[('sp – sp; 3','Orbitalleri doğru bulmuş ama yalnız karbon–karbon bağlarını sayıp C–H σ bağlarını (6 tane) hesaba katmamış.','dikkat'),
      ('sp – sp; 11','Orbitalleri doğru bulmuş ama 2 π bağını da σ bağı sayarak 9 + 2 = 11 bulmuş.','dikkat'),
      ('sp² – sp²; 9','Üçlü bağı oluşturan karbonların sp² hibritleşmesi yaptığını sanmış; sp² çift bağlı karbonlara, sp üçlü bağlı karbonlara aittir.','bilgi'),
      ('sp³ – sp³; 9','Üçlü bağdaki σ bağını, doymuş karbonlar arasındaki tek bağ gibi sp³–sp³ örtüşmesi sanmış.','bilgi')])

# ================= 03 · hibritleşme ve düzlem · orta · öncüllü =================
S3='CC(C)=CC'; M3=Mol(S3); assert M3.formula()[:2]==(5,10) and AD(S3)=='2-Metil-2-büten'
def hib(M):
    r={}
    for i in M.carbons():
        mx=max(o for _,o in M.adj[i]); r[i]={1:'sp3',2:'sp2',3:'sp'}[mx]
    return r
h3=hib(M3); sp2n=sum(1 for v in h3.values() if v=='sp2'); sp3n=sum(1 for v in h3.values() if v=='sp3')
assert (sp2n,sp3n)==(2,3)
dub=[i for i in M3.carbons() if h3[i]=='sp2']; duzlem=set(dub)|{w for i in dub for w,_ in M3.adj[i]}; assert duzlem==set(M3.carbons())
sig3=len(M3.b)+M3.formula()[1]; assert sig3==14
sk3=tk(ciz(S3)[0])
tr=[True,False,True]
nd=['çift bağı oluşturan iki karbon sp² hibritleşmesi yapar; kalan üç metil karbonu tek bağlıdır',
    'molekülde yalnız tek bağ yapan üç karbon (üç metil grubu) vardır; bunların hepsi sp³ hibritleşmesi yaptığından sp³ karbon sayısı 3’tür',
    'çift bağdaki iki karbon ve bunlara doğrudan bağlı bütün karbonlar aynı düzlemdedir; bu molekülde beş karbonun tümü bu gruba girer']
d3,y3,s3=onc(tr,nd,'E'); assert d3=='I ve III'
Q('hk2-yapi','orta','Hibritleşme ve molekül düzlemi','Çift bağlı karbonlar sp², tek bağlı karbonlar sp³ hibritleşmesi yapar; çift bağdaki karbonlar ve bunlara bağlı atomlar aynı düzlemde bulunur.','Metil gruplarını sp² saymak; düzlemde yalnız çift bağlı karbonları düşünmek.','öncüllü',
 'Açık zincirli bir hidrokarbonun çizgi formülü şekilde verilmiştir (₁H, ₆C).\n'+etiket_oncul('Molekülde sp² hibritleşmesi yapan 2 karbon atomu vardır.','Molekülde sp³ hibritleşmesi yapan 2 karbon atomu vardır.','Molekülün tüm karbon atomları aynı düzlemdedir.')+'Buna göre, yukarıdaki yargılardan hangileri doğrudur?',
 'Doğru yargıların belirlenmesi.','Her karbonun yaptığı en yüksek bağ türüne bak; çift bağın iki ucundaki karbonlara bağlanan atomların hepsinin tek düzlemde olduğunu düşün.',
 [B('Hibritleşme','Üçlü bağlı karbon sp, çift bağlı karbon sp², yalnız tek bağ yapan karbon sp³ hibritleşmesi yapar. Örnek: propende (CH₂=CH–CH₃) 2 sp² ve 1 sp³ karbon bulunur')],
 oadim(tr,nd)+[A('Sonuç','Doğru yargılar I ve III’tür.','I ve III')],
 'Her karbonun yaptığı en yüksek bağ türü hibritleşmesini belirler.',sekil=sk3,dogru=d3,yan=y3,sira=s3)

# ================= 04 · kaynama noktası · orta · tablo · olumsuz kök =================
SK={'K':('CCCC','CH₃–CH₂–CH₂–CH₃',-1),'L':('CC(C)C','CH₃–CH(CH₃)–CH₃',-12),'M':('CCCCC','CH₃–CH₂–CH₂–CH₂–CH₃',36),'N':('CC(C)CC','CH₃–CH(CH₃)–CH₂–CH₃',28)}
fK,fL,fM,fN=[Mol(SK[k][0]).formula()[:2] for k in 'KLMN']
assert fK==fL==(4,10) and fM==fN==(5,12) and same(Mol(SK['K'][0]),Mol(SK['L'][0]))==False and same(Mol(SK['M'][0]),Mol(SK['N'][0]))==False
assert SK['K'][2]>SK['L'][2] and SK['M'][2]>SK['N'][2] and SK['M'][2]>SK['K'][2]
sk4=tbl(['Bileşik','Yapı formülü','Kaynama noktası (°C)'],[[k,SK[k][1],str(SK[k][2]).replace('-','−')] for k in 'KLMN'])
tr=[True,True,False]
nd=['K ve L’nin molekül formülü C₄H₁₀’dur ve bağlanma sıraları farklıdır; yani ikisi birbirinin yapı izomeridir',
    'M ve N’nin molekül formülü C₅H₁₂’dir; N dallı olduğundan moleküller arası temas yüzeyi küçüktür, London kuvvetleri zayıftır ve kaynama noktası düşüktür',
    'alkanlar apolar bileşiklerdir ve molekülleri arasında hidrojen bağı bulunmaz; M’nin kaynama noktası, mol kütlesi büyük olduğu için London kuvvetleri daha güçlü olduğundan K’dan yüksektir']
d4,y4,s4=onc(tr,nd,'A',yanlis_sor=True); assert d4=='Yalnız III'
Q('hk2-ozellik','orta','Alkanlarda kaynama noktası','Alkanlar apolardır; molekül arası kuvvet London kuvvetidir. Karbon sayısı arttıkça kaynama noktası yükselir, aynı formülde dallanma arttıkça düşer.','Alkanlarda hidrojen bağı aramak; dallanmayı kaynama noktasını yükselten etken sanmak.','tablo',
 'Dört alkanın yapı formülleri ve normal basınçtaki kaynama noktaları tabloda verilmiştir.\n'+etiket_oncul('K ve L birbirinin yapı izomeridir.','N’nin kaynama noktasının M’den düşük olması, dallanma nedeniyle London kuvvetlerinin zayıflamasındandır.','M’nin kaynama noktasının K’dan yüksek olması, M’nin moleküller arasında hidrojen bağı yapmasındandır.')+'Buna göre, yukarıdaki yargılardan hangileri yanlıştır?',
 'Yanlış yargıların belirlenmesi.','Önce molekül formüllerini yaz; sonra apolar moleküllerde kaynama noktasını belirleyen etkenleri düşün.',
 [B('Alkanlarda kaynama noktası','Alkanlar apolar olduğundan moleküller arasında yalnız London kuvvetleri etkindir. Mol kütlesi arttıkça kaynama noktası yükselir; dallanma temas yüzeyini küçültüp onu düşürür. Örnek: Propanın kaynama noktası, etanınkinden yüksektir')],
 oadim(tr,nd)+[A('Sonuç','Yanlış olan yalnız III’tür.','Yalnız III')],
 'Alkanlarda moleküller arası kuvvet London’dır; hidrojen bağı yoktur.',sekil=sk4,dogru=d4,yan=y4,sira=s4)

# ================= 05 · Br2 tüpleri · orta · şekilli =================
nb=Fr(1,100); br=Fr(3,200)
def kalan(sinif): return {'Alkan':br,'Alken':br-nb,'Alkin':max(Fr(0),br-2*nb)}[sinif]
assert (kalan('Alkan'),kalan('Alken'),kalan('Alkin'))==(Fr(3,200),Fr(1,200),Fr(0))
gozlem=(kalan('Alkan'),kalan('Alken'),kalan('Alkin'))
def tup5(x,renk,et,alt):
    return [f'\\fill[{renk}] ({x-.45},0.1) -- ({x-.45},-1.7) arc(180:360:.45) -- ({x+.45},0.1) -- cycle;',
            f'\\draw[thick] ({x-.45},0.9) -- ({x-.45},-1.7) arc(180:360:.45) -- ({x+.45},0.9);',
            f'\\node[font=\\large\\bfseries] at ({x},1.3) {{{et}}};',
            f'\\node[align=center,font=\\small] at ({x},-2.95) {{{alt}}};']
alts=[f'kalan Br$_2$:\\\\{fm(v)} mol' for v in gozlem]
sk5=tk(tup5(0,'orange!70','X',alts[0]),tup5(2.7,'orange!25','Y',alts[1]),tup5(5.4,'white','Z',alts[2]))
perm=[('Alkan','Alken','Alkin'),('Alken','Alkan','Alkin'),('Alkan','Alkin','Alken'),('Alkin','Alken','Alkan'),('Alken','Alkin','Alkan')]
fmt5=lambda t:f'X: {t[0]}, Y: {t[1]}, Z: {t[2]}'
d5=fmt5(perm[0]); assert tuple(kalan(c) for c in perm[0])==gozlem
for t in perm[1:]: assert tuple(kalan(c) for c in t)!=gozlem
def yan5(t):
    k=[i for i in range(3) if kalan(t[i])!=gozlem[i]][0]; ad='XYZ'[k]
    return (fmt5(t),f'Bileşikleri {t[0].lower()}, {t[1].lower()}, {t[2].lower()} sırasıyla yorumlamış; oysa {ad} bileşiği {t[k].lower()} olsaydı {ad} tüpünde {fm(kalan(t[k]))} mol Br₂ kalırdı, şekilde ise {fm(gozlem[k])} mol görülüyor.','bilgi')
Q('hk2-ozellik','orta','Br₂ ile ayırt etme','Alkan karanlıkta Br₂ ile tepkime vermez; 1 mol alken 1 mol, 1 mol alkin 2 mol Br₂ bağlar. Kalan Br₂ miktarı bileşiğin sınıfını verir.','Yalnız rengin gitmesine bakıp alken ile alkini ayırmamak; Br₂ yetersizse alkinin de rengi giderdiğini görmemek.','şekilli',
 'Açık zincirli X, Y ve Z hidrokarbonlarının her birinin 0,01 molü ayrı tüplerdeki 0,015 mol Br₂ içeren CCl₄ çözeltisine ekleniyor; tüpler karanlıkta tepkime tamamlanıncaya dek bekletiliyor. Bileşiklerin her birinde en fazla bir çok katlı bağ bulunmaktadır. Tüplerin son durumu ve kalan Br₂ miktarları şekilde verilmiştir.\nBuna göre, X, Y ve Z bileşiklerinin sınıfları aşağıdakilerden hangisinde doğru verilmiştir?',
 'X, Y ve Z’nin bileşik sınıfları.','Her tüpte başlangıçtaki Br₂’den kalan miktarı çıkararak harcanan Br₂ mol sayısını bul; bunu bileşiğin mol sayısıyla karşılaştır.',
 [B('Br₂ ile katılma','Alkenin 1 molü 1 mol, alkinin 1 molü 2 mol Br₂ bağlar; alkan karanlıkta Br₂ ile tepkime vermez. Örnek: 0,2 mol propin 0,4 mol Br₂ harcar')],
 [A('Harcanan Br₂','Başlangıçta 0,015 mol Br₂ vardır; harcanan miktar başlangıçtan kalanın çıkarılmasıyla bulunur.','X: 0; Y: 0,01 mol; Z: 0,015 mol'),
  A('X’i belirle','Harcanan Br₂ yok; X karanlıkta Br₂ ile tepkime vermediğinden doymuştur.','X: alkan'),
  A('Y’yi belirle','0,01 mol bileşik 0,01 mol Br₂ harcamıştır; mol sayıları eşittir.','Y: alken'),
  A('Z’yi belirle','Z tüpünde Br₂ tamamen bitmiştir; 0,01 mol Z, 0,015 mol Br₂’yi tüketmiştir ve alken olsaydı en çok 0,01 mol tüketirdi, yani Z alkindir.','Z: alkin')],
 'Harcanan Br₂ mol sayısı bileşik mol sayısından fazlaysa bileşik alkindir.',sekil=sk5,
 dogru=d5,sira=yer(d5,[fmt5(t) for t in perm[1:]],'B'),yan=[yan5(t) for t in perm[1:]])

# ================= 06 · HX / H2O katılması · orta · öncüllü =================
def urunler(M,X):
    """Her iki yönde (yalnız tek çok katlı bağlı molekülde) HX katılma ürünlerinin kanonik kümesi"""
    el=list(M.el); b=list(M.b); mb=[(a,c,o) for a,c,o in b if o>1]; assert len(mb)==1
    a,c,o=mb[0]; r=set()
    for hed in (a,c):
        bb=[(p,q,(r_-1 if (p,q,r_)==(a,c,o) else r_)) for p,q,r_ in b]; e2=el+[X]; bb.append((hed,len(el),1)); r.add(canon(mol_kur(e2,bb)))
    return r
K6,L6,M6='CC=CC','C=CCC','CC(C)=C'
assert len(urunler(Mol(K6),'Br'))==1 and urunler(Mol(K6),'Br')=={canon(Mol('CC(Br)CC'))} and AD('CC(Br)CC')=='2-Bromobütan'
assert len(urunler(Mol(L6),'Br'))==2
sL=hx_katil(Mol(L6),'O'); assert ayni(sL,'CC(O)CC'); oc=[i for i,e in enumerate(sL.el) if e=='O'][0]; cx=sL.adj[oc][0][0]; assert sum(1 for w,_ in sL.adj[cx] if sL.el[w]=='C')==2   # ikincil alkol
assert ayni(hx_katil(Mol(M6),'Cl'),'CC(C)(Cl)C') and AD('CC(C)(Cl)C')=='2-Kloro-2-metilpropan' and ayni(hx_katil(Mol(M6),'Cl',ters=True),'CC(C)CCl') and AD('CC(C)CCl')=='1-Kloro-2-metilpropan'
sk6=tk(satir([(K6,'K',{(1,2):'trans'}),(L6,'L',None),(M6,'M',None)],aralik=1.5))
tr=[True,True,False]
nd=['K simetrik bir alkendir; çift bağın iki ucundaki karbonların hidrojen sayıları eşit olduğundan HBr hangi yönde katılırsa katılsın aynı bileşik, 2-bromobütan oluşur',
    'L’ye su katılırken Markovnikov kuralına göre OH grubu H’si az olan 2. karbona bağlanır; ana ürün olan 2-bütanolde OH’li karbon iki karbona bağlı olduğundan ikincil alkoldür',
    'M’de çift bağın bir ucunda hiç hidrojen yoktur; Cl, H’si az olan karbona bağlanacağından ana ürün 2-kloro-2-metilpropandır, 1-kloro-2-metilpropan değil']
d6,y6,s6=onc(tr,nd,'C'); assert d6=='I ve II'
Q('hk2-katilma','orta','HX ve H₂O katılması (Markovnikov)','Simetrik alkende tek ürün, asimetrik alkende ana ürün Markovnikov kuralıyla bulunur; H, H’si fazla karbona, X ya da OH ise H’si az karbona bağlanır.','Simetrik alkende iki ürün aramak; X’i H’si fazla karbona bağlamak.','öncüllü',
 'Aşağıda çizgi formülleri verilen K, L ve M, açık zincirli alkenlerdir. Katılma tepkimeleri uygun koşullarda gerçekleşmektedir.\n'+etiket_oncul('K’ye HBr katılması sonucu tek bir ürün oluşur.','L’ye su katılması sonucu oluşan ana ürün, ikincil (sekonder) alkoldür.','M’ye HCl katılması sonucu oluşan ana ürün 1-kloro-2-metilpropandır.')+'Buna göre, yukarıdaki yargılardan hangileri doğrudur?',
 'Doğru yargıların belirlenmesi.','Her alkenin çift bağındaki iki karbonun hidrojen sayılarını karşılaştır; eşitse ürün tektir, değilse Markovnikov kuralını uygula.',
 [B('Katılma ve Markovnikov kuralı','Simetrik olmayan HX ya da H₂O alkene katılırken H, çift bağdaki H sayısı fazla olan karbona gider; X ya da OH diğer karbona bağlanır. Örnek: propen + H₂O → 2-propanol')],
 oadim(tr,nd)+[A('Sonuç','Doğru yargılar I ve II’dir.','I ve II')],
 'Çift bağın iki ucundaki H sayıları eşitse tek ürün; değilse H’si az karbon halojeni ya da OH’yi alır.',sekil=sk6,dogru=d6,yan=y6,sira=s6)

# ================= 07 · alken karışımının yanması · zor · tablo =================
MX=lambda c,h:c*M_C+h*M_H
mX,mY=MX(3,6),MX(4,8); assert (mX,mY)==(42,56)
kt=Fr(84,10)
for x_ in [Fr(0),Fr(1,20),Fr(1,10),Fr(3,20)]:      # bileşimden bağımsızlık kontrolü: 42x + 56y = 8,4
    y_=(kt-42*x_)/56; nC=3*x_+4*y_; nH=6*x_+8*y_
    assert nC==Fr(3,5)-0*x_ and nH==Fr(6,5) and nC+nH/4==Fr(9,10)
nco2=Fr(3,5); nh2o=Fr(3,5); mco2=nco2*44; mh2o=nh2o*18
assert (mco2,mh2o)==(Fr(132,5),Fr(54,5)) and kt/Fr(mX,3)==Fr(3,5)
mo2=mco2+mh2o-kt; assert mo2==Fr(144,5) and mo2/32==Fr(9,10)
d7=Fr(9,10); assert nco2+nh2o/2==d7
sk7=tbl(['Bileşik','Molekül formülü','Mol kütlesi (g/mol)'],[['X','C₃H₆','42'],['Y','C₄H₈','56']])
Q('hk2-yanma','zor','Alken karışımının yanması ve kütle oranı','Aynı genel formüllü bileşiklerin karışımında bileşim bilinmese de elementlerin kütle oranı ortaktır; yanma ürünleri C ve H kütlesinden bulunur.','Karışımın mol oranını bilinmeyen sanıp çözümsüz kalmak; O₂ miktarını yalnız bir üründen bulmak.','tablo',
 'Açık zincirli X ve Y alkenlerinin bileşimi bilinmeyen bir karışımından 8,4 g alınıyor ve yeterli miktarda O₂ ile tamamen yakılıyor (ürünler CO₂ ve H₂O). X ve Y’nin molekül formülleri ile mol kütleleri tabloda verilmiştir (H: 1, C: 12, O: 16).\nBuna göre, yakma işleminde harcanan O₂ kaç moldür?',
 'Harcanan O₂ mol sayısı.','Karışımın bileşimini bilmeden C ve H kütlesine ulaşmanın yolunu ara.',
 [B('Alkenlerde kütle oranı','Aynı genel formüllü bileşik ailesinde elementlerin kütle oranı formüldeki sayılardan bulunur. Örnek: 1 mol C₃H₆ molekülünde 36 g karbon ve 6 g hidrojen bulunur')],
 [A('C ve H kütlesi','Alkenlerde kütlece C : H = 12n : 2n = 6 : 1’dir; karışımın bileşimi önemli değildir.','8,4 g → C: 7,2 g; H: 1,2 g'),
  A('Mol sayıları','7,2 g karbon 0,6 mol C atomu, 1,2 g hidrojen 1,2 mol H atomudur; her C bir CO₂, her 2 H bir H₂O verir.','CO₂: 0,6 mol; H₂O: 0,6 mol'),
  A('O₂ mol sayısı','CO₂ için 0,6 mol, H₂O için 0,6 / 2 = 0,3 mol O₂ gerekir.','0,6 + 0,3 = 0,9 mol')],
 'Yanma ürünlerindeki oksijen atomlarının toplamını O₂ molüne çevir.',sekil=sk7,
 dogru=d7,yan=[(Fr(3,5),'Yalnız CO₂ oluşumu için gereken O₂’yi (0,6 mol) bulmuş; H₂O’daki oksijeni hesaba katmamış.','dikkat'),
               (Fr(3,10),'Yalnız H₂O için düşünüp 0,6 mol O atomunu ikiye bölerek 0,3 mol O₂ bulmuş; CO₂ için gereken O₂’yi unutmuş.','dikkat'),
               (Fr(6,5),'CO₂ için 0,6 mol, H₂O için de 0,6 mol O₂ toplamış; H₂O’daki oksijen atomlarını da tam bir O₂ molekülü saymış.','bilgi'),
               (Fr(9,5),'Ürünlerdeki toplam oksijen atomu sayısını (0,6 × 2 + 0,6 = 1,8 mol) O₂ mol sayısı sanmış; O₂’nin iki atomlu olduğunu hesaba katmamış.','bilgi')])

# ================= 08 · asetilen eldesi ve Br2 · zor · düzenek =================
mCaC2=64; assert 40+2*12==mCaC2
ms=20; saf=Fr(4,5); ver=Fr(3,4)
nca=ms*saf/mCaC2; nac=nca*ver; nbr=2*nac; d8=nbr*160
assert (nca,nac,nbr,d8)==(Fr(1,4),Fr(3,16),Fr(3,8),60)
assert nac*160==30 and ms*ver/mCaC2*2*160==75 and nca*2*160==80 and Fr(ms,mCaC2)*2*160==100
assert len({30,60,75,80,100})==5
sk8=tk(['\\draw[thick] (-0.35,1.55) -- (-1.15,0) -- (1.15,0) -- (0.35,1.55);',
        '\\fill[blue!20] (-1.0,0.0) -- (-0.8,0.5) -- (0.8,0.5) -- (1.0,0.0) -- cycle;',
        '\\fill[gray!60] (-0.7,0.02) rectangle (0.2,0.2);',
        '\\draw[thick] (-0.45,1.55) -- (0.45,1.55);',
        '\\draw[thick] (0,1.55) -- (0,2.3) -- (3.6,2.3) -- (3.6,0.5);',
        '\\fill[orange!35] (2.9,-0.3) rectangle (4.3,0.9);',
        '\\draw[thick] (2.9,1.5) -- (2.9,-0.3) -- (4.3,-0.3) -- (4.3,1.5);',
        '\\node[align=center,font=\\small] at (0,-0.75) {20 g numune\\\\(kütlece \\%80 CaC$_2$)\\\\+ yeterli su};',
        '\\node[font=\\small] at (1.8,2.65) {C$_2$H$_2$ gazı};',
        '\\node[align=center,font=\\small] at (3.6,-1.0) {yeterli Br$_2$\\\\içeren CCl$_4$ çözeltisi};'])
Q('hk2-eldepolimer','zor','Asetilen eldesi, verim ve Br₂ tüketimi','CaC₂ + 2H₂O → C₂H₂ + Ca(OH)₂; saf CaC₂ mol sayısı verimle çarpılarak C₂H₂ bulunur, 1 mol alkin 2 mol Br₂ bağlar.','Saflık ya da verimi unutmak; alkine 1 mol Br₂ katıldığını sanmak.','şekilli',
 'Asetilen (C₂H₂) gazı laboratuvarda kalsiyum karbürün (CaC₂) su ile tepkimesinden elde edilir:\nCaC₂ + 2H₂O → C₂H₂ + Ca(OH)₂\nŞekildeki düzenekte, numunedeki CaC₂’den %75 verimle C₂H₂ elde ediliyor; oluşan C₂H₂ gazının tamamı yeterli miktarda Br₂ içeren CCl₄ çözeltisinden geçirilerek tepkimeye sokuluyor (C: 12, Ca: 40, Br: 80).\nBuna göre, çözeltide harcanan Br₂ kaç gramdır?',
 'Harcanan Br₂ kütlesi.','Önce numunedeki saf CaC₂ kütlesini ve mol sayısını bul; verimi uygula; sonra C₂H₂’nin Br₂ ile tepkime oranını yaz.',
 [B('Verim ve saflık','Tepkimede yararlanılan madde miktarı saf kütleyle sınırlıdır; verim, gerçekte oluşan ürünün kuramsal ürüne oranıdır. Örnek: kuramsal olarak 0,4 mol ürün veren tepkime %50 verimle 0,2 mol ürün verir')],
 [A('Saf CaC₂','20 g numunenin %80’i CaC₂’dir; mol kütlesi 40 + 24 = 64 g/mol.','16 g → 16 / 64 = 0,25 mol'),
  A('C₂H₂ miktarı','Tepkime katsayıları 1 : 1 olduğundan kuramsal 0,25 mol C₂H₂ oluşur; verim %75.','0,25 × 0,75 = 0,1875 mol'),
  A('Br₂ miktarı','Alkin 2 mol Br₂ bağlar: C₂H₂ + 2Br₂ → C₂H₂Br₄.','0,1875 × 2 = 0,375 mol'),
  A('Kütleyi bul','Br₂’nin mol kütlesi 160 g/mol.','0,375 × 160 = 60 g')],
 'Yalnız saf madde tepkimeye girer.',sekil=sk8,
 dogru=60,yan=[(30,'Alkine yalnız 1 mol Br₂ katıldığını düşünmüş; 0,1875 mol Br₂ × 160 = 30 g bulmuş.','bilgi'),
               (75,'Numunenin saflığını hesaba katmayıp 20 g’ın tamamını CaC₂ sanmış: 20 / 64 × 0,75 × 2 × 160 = 75 g.','dikkat'),
               (80,'Verimi unutmuş; 0,25 mol C₂H₂’nin tamamının oluştuğunu varsayıp 0,25 × 2 × 160 = 80 g bulmuş.','dikkat'),
               (100,'Hem saflığı hem de verimi hesaba katmamış: 20 / 64 × 2 × 160 = 100 g.','dikkat')])

# ================= 09 · alkin–alken karışımı + H2 · zor · kap şeması =================
na_=Fr(1,2); nh_=Fr(7,10)
xa=nh_-na_; xe=na_-xa     # alkin x: 2x + (0,5 − x) = 0,7
assert (xa,xe)==(Fr(1,5),Fr(3,10)) and 2*xa+xe==nh_
mA,mE=MX(2,2),MX(3,6); assert (mA,mE)==(26,42)
d9=xa*mA+xe*mE; assert d9==Fr(89,5)
assert na_*mA==13 and na_*mE==21 and xe*mA+xa*mE==Fr(81,5) and Fr(7,20)*mA+Fr(3,20)*mE==Fr(77,5)
assert len({13,Fr(77,5),Fr(81,5),d9,21})==5
def kutu9(x0,y0,w,h,metin):
    return [f'\\draw[thick] ({x0},{y0}) rectangle ({x0+w},{y0+h});',f'\\node[align=center,font=\\small] at ({x0+w/2},{y0+h/2}) {{{metin}}};']
sk9=tk(kutu9(0,0,4.2,2.0,'C$_2$H$_2$ ve C$_3$H$_6$\\\\(toplam 0,5 mol)\\\\+ H$_2$ (0,7 mol)'),[ok_(4.4,1.0,6.3,1.0,'Ni katalizörü')],kutu9(6.5,0,3.8,2.0,'Yalnız C$_2$H$_6$\\\\ve C$_3$H$_8$\\\\(H$_2$ kalmadı)'))
Q('hk2-katilma','zor','Alkin–alken karışımının hidrojenlenmesi','Alken 1 mol, alkin 2 mol H₂ bağlar; toplam karışım mol sayısı ile harcanan H₂ mol sayısından iki bilinmeyenli denklem kurulur.','Karışımın tamamına aynı sayıda H₂ bağlandığını sanmak; mol sayılarını ters yazmak.','şekilli',
 'Şekilde kapalı bir kapta, açık zincirli C₂H₂ ve C₃H₆ gazlarından oluşan karışımın H₂ ile Ni katalizörlüğünde tepkimesi gösterilmiştir; madde miktarları şekilde verilmiştir (H: 1, C: 12).\nBuna göre, başlangıçtaki karışımın kütlesi kaç gramdır?',
 'Başlangıç karışımının kütlesi.','Her gazın kaç mol H₂ bağladığını yaz.',
 [B('Hidrojenleme','Alken 1 mol, alkin 2 mol H₂ bağlayarak alkana dönüşür. Örnek: 0,2 mol propin ile 0,1 mol propen birlikte 0,5 mol H₂ harcar')],
 [A('Denklemleri kur','C₂H₂ x mol, C₃H₆ y mol olsun; x + y = 0,5 ve harcanan H₂ için 2x + y = 0,7.','x + y = 0,5; 2x + y = 0,7'),
  A('Çöz','İkinci denklemden birincisi çıkarılır.','x = 0,2 mol; y = 0,3 mol'),
  A('Kütleyi hesapla','C₂H₂ 26 g/mol, C₃H₆ 42 g/mol.','0,2 × 26 + 0,3 × 42 = 5,2 + 12,6 = 17,8 g')],
 'Her bileşiğin kaç mol H₂ bağladığını yaz.',sekil=sk9,
 dogru=d9,yan=[(13,'Karışımın tamamını C₂H₂ gibi düşünüp 0,5 × 26 = 13 g bulmuş.','dikkat'),
               (21,'Karışımın tamamını C₃H₆ gibi düşünüp 0,5 × 42 = 21 g bulmuş.','dikkat'),
               (Fr(81,5),'Mol sayılarını ters bulmuş (0,3 mol C₂H₂, 0,2 mol C₃H₆): 0,3 × 26 + 0,2 × 42 = 16,2 g.','bilgi'),
               (Fr(77,5),'0,7 mol H₂’nin hepsini alkine bağlı sanıp C₂H₂’yi 0,7 / 2 = 0,35 mol, C₃H₆’yı 0,15 mol bulmuş: 0,35 × 26 + 0,15 × 42 = 15,4 g.','bilgi')])

# ================= 10 · PVC · orta · öncüllü =================
MV='C=CCl'; Mv=Mol(MV); assert Mv.formula()[:2]==(2,3) and Mv.formula()[2]=={'Cl':1}
mv=2*M_C+3*M_H+M_Cl; assert mv==Fr(125,2) and Fr(31250)/mv==500
assert Mol('CCCl').formula()[:2]==(2,5)
sk10=tk(['\\draw[thick] (-0.95,0.55) -- (0,0) -- (0.9,0.52) -- (1.85,0);','\\draw[thick] (0.9,0.52) -- (0.9,1.35);',
         '\\node[font=\\small] at (0.9,1.62) {Cl};',
         '\\draw[thick] (-0.5,-0.55) -- (-0.7,-0.55) -- (-0.7,1.0) -- (-0.5,1.0);','\\draw[thick] (1.45,-0.55) -- (1.65,-0.55) -- (1.65,1.0) -- (1.45,1.0);',
         '\\node[font=\\small] at (1.95,-0.75) {$n$};'])
tr=[False,True,True]
nd=['polimerin tekrarlayan birimi –CH₂–CHCl– olduğundan monomerin yapısında bir çift bağ vardır; adı kloroetan değil kloroeten’dir',
    'monomerin mol kütlesi 2 × 12 + 3 × 1 + 35,5 = 62,5 g/mol’dür ve 31250 / 62,5 = 500 tekrarlayan birim bulunur',
    'monomer CH₂=CHCl çift bağı bir tane olduğundan 1 mol monomeri doyurmak için 1 mol H₂ yeterlidir; ürün kloroetandır']
d10,y10,s10=onc(tr,nd,'D'); assert d10=='II ve III'
Q('hk2-eldepolimer','orta','Katılma polimerinin monomeri ve mol kütlesi','Katılma polimerinde tekrarlayan birim monomerle aynı atomları içerir; polimerin mol kütlesi n × monomerin mol kütlesidir.','Monomerde çift bağ olduğunu görmemek; tekrar sayısını yanlış hesaplamak.','öncüllü',
 'Boru ve kablo kaplamalarında kullanılan polivinil klorürün (PVC) tekrarlayan birimi şekilde verilmiştir (H: 1, C: 12, Cl: 35,5).\n'+etiket_oncul('Monomerinin adı kloroetandır.','Mol kütlesi 31250 g/mol olan PVC molekülünde 500 tekrarlayan birim bulunur.','Monomerinin 1 molünü Ni katalizörlüğünde doyurmak için 1 mol H₂ gerekir.')+'Buna göre, yukarıdaki yargılardan hangileri doğrudur?',
 'Doğru yargıların belirlenmesi.','Polimeri oluşturan küçük molekülün yapısını düşün; her yargıyı o molekül üzerinden sına.',
 [B('Katılma polimerleşmesi','Çift bağlı monomerlerin çift bağı açılarak birbirine bağlanması katılma polimerleşmesidir; atom kaybı olmaz. Örnek: 1 mol eten 28 g ise n mol eten birleşince polietilenin mol kütlesi 28n g/mol olur')],
 oadim(tr,nd)+[A('Sonuç','Doğru yargılar II ve III’tür.','II ve III')],
 'Önce monomerin molekül formülünü ve mol kütlesini yaz.',sekil=sk10,dogru=d10,yan=y10,sira=s10)

# ================= yaz =================
def bitir_ak():
    for qq in P.ANA: qq['kardes']=None
    P.yaz(os.path.join(GD,'hidrokarboniki-1.json'),'/tmp/bos-hidrokarboniki.json')
    tipler={}
    for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu='akim|'+KONU))['kartlar'].append(c['id'])
    json.dump(dict(konu=KONU,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2018–2026 kimya soruları (yalnız mantık), MEB 11. sınıf kimya.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar','akhidrokarboniki.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler),'sorular',len(P.ANA))
bitir_ak()
