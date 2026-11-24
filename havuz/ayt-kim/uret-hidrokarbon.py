"""AYT Kimya · Hidrokarbonlar (Alkan, Alken, Alkin) · 20 soru. Yapılar SMILES benzeri dizgeyle tanımlanır; formül, ad, izomer ve ürün sayıları kodla
hesaplanır; her cevap ve çeldirici Python'da assert edilir. Şekiller TikZ (cizim.tikz_svg)."""
import sys,os,json,math,itertools,re
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-kim')); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
import _hafif_kim2 as H
from _hafif_kim2 import *
from cizim import tikz_svg
from collections import Counter
KONU='Hidrokarbonlar (Alkan, Alken, Alkin)'; H.KONU=KONU
P=Parti('hidrokarbon',KONU,'akim|'+KONU,ders='AYT Kimya',idon='aytkim')
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
TIPAD={'hk-adlandirma':'Hidrokarbonların adlandırılması','hk-genel':'Genel formül ve bileşik sınıfı','hk-yanma':'Tam yanma tepkimeleri','hk-katilma':'Katılma tepkimeleri',
       'hk-yerdegistirme':'Alkanlarda yer değiştirme','hk-polimer':'Polimerleşme','hk-izomer':'İzomerlik'}
NK=[0]
def Q(tipId,z,alt,fikir,tuzak,kalip,metin,istenen,ip,bilgi,ad,puf,sekil=None,dogru=None,yan=None,sira=None,kaz=None,kisa=None):
    tip=TIPAD[tipId]; NK[0]+=1; n=NK[0]; no=f'{n:04d}'; kid=f'K-AKHID-{n:02d}'
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
    return f'\\draw[-{{Stealth[length=2mm,width=1.8mm]}},thick] ({x1:.3f},{y1:.3f}) -- ({x2:.3f},{y2:.3f}) node[midway,above,align=center,font=\\footnotesize]{{{et}}};'
def sinif_h(c,h):
    return {2*c+2:'Alkan',2*c:'Alken',2*c-2:'Alkin'}[h]
M_H,M_C,M_O,M_Cl=1,12,16,Fr(71,2)

# ================= 01 · adlandırma · kolay =================
S1='CC(C)C(C)CC'; M1=Mol(S1); assert M1.formula()[:2]==(7,16)
a1=AD(S1); assert a1=='2,3-Dimetilpentan'
assert AD(S1,kotu_yon=True)=='3,4-Dimetilpentan'
assert same(Mol('CC(CC)C(C)C'),M1)
assert AD('CC(C)(C)CCC')=='2,2-Dimetilpentan' and not same(Mol('CC(C)(C)CCC'),M1) and Mol('CC(C)(C)CCC').formula()[:2]==(7,16)
assert AD('CC(C)C(C)CCC')=='2,3-Dimetilheksan' and Mol('CC(C)C(C)CCC').formula()[:2]==(8,18)
assert max(len(p) for p in paths(M1))==5
sk1=tk(ciz(S1)[0])
Q('hk-adlandirma','kolay','Alkanların IUPAC adlandırması','En uzun karbon zinciri bulunur; dallar, en küçük sayıları alacak yönde numaralandırılarak adlandırılır.','Ana zinciri kısa seçmek; numaralandırmayı dallara büyük sayı verecek uçtan yapmak.','şekilli',
 'Petrolün işlenmesi sırasında elde edilen ürünlerde bulunan doymuş bir hidrokarbonun çizgi formülü şekilde verilmiştir.\nBuna göre, bu bileşiğin IUPAC adı aşağıdakilerden hangisinde doğru olarak verilmiştir?',
 'Çizgi formülü verilen alkanın IUPAC adı.','Önce en uzun karbon zincirini belirle; sonra dalların bağlı olduğu karbonlara en küçük sayılar gelecek uçtan numaralandır.',
 [B('Alkan adlandırma','En uzun karbon zinciri ana zincirdir; dallar ana zincirde en küçük sayıları alacak şekilde numaralandırılır. Örnek: 2-Metilbütan, 4 karbonlu zincirin 2. karbonuna metil bağlanmış alkandır')],
 [A('Ana zinciri bul','Yapıdaki en uzun karbon zinciri 5 karbonludur; bileşik doymuş olduğundan kök adı pentandır.','5 karbon → pentan'),
  A('Dalları belirle','Ana zincire iki ayrı karbonda birer CH₃ dalı bağlıdır; iki dal da metildir.','2 dal: metil, metil'),
  A('Numaralandır','Dallar bir uçtan başlayınca 2 ve 3, diğer uçtan başlayınca 3 ve 4. karbonlarda kalır; en küçük sayıları veren yön seçilir.','{2,3} küçük, {3,4} büyük → 2,3'),
  A('Adı yaz','Aynı dal iki kez bulunduğu için “di” öneki kullanılır.','2,3-Dimetilpentan')],
 'Önce en uzun zincir, sonra dallara en küçük sayıları verecek numaralandırma.',sekil=sk1,
 dogru=a1,sira=yer(a1,['2,2-Dimetilpentan','2,3-Dimetilheksan','2-Etil-3-metilbütan','3,4-Dimetilpentan'],'E'),
 yan=[('2,2-Dimetilpentan','İki metil grubunu aynı karbona bağlı sanmış; oysa metiller komşu karbonlardadır.','bilgi'),
      ('2,3-Dimetilheksan','Zinciri bir karbon uzun saymış; bu ad 8 karbonlu bir bileşiğe aittir, oysa şekildeki bileşik C₇H₁₆’dır.','dikkat'),
      ('2-Etil-3-metilbütan','Ana zinciri 4 karbonlu seçmiş; aynı bileşiğin en uzun zincirle adlandırılması gerekir ve 5 karbonlu zincir bulunur.','bilgi'),
      ('3,4-Dimetilpentan','Numaralandırmayı yanlış uçtan yapıp dallara 3 ve 4 sayılarını vermiş; doğru yönde sayılar 2 ve 3 olur.','bilgi')])

# ================= 02 · adlandırma · orta =================
S2='CC(C)=CC(C)(C)C'; M2=Mol(S2); assert M2.formula()[:2]==(8,16)
a2=AD(S2); assert a2=='2,4,4-Trimetil-2-penten'
k2=AD(S2,kotu_yon=True); assert k2=='2,2,4-Trimetil-3-penten'
assert AD('C=C(C)CC(C)(C)C')=='2,4,4-Trimetil-1-penten' and not same(Mol('C=C(C)CC(C)(C)C'),M2)
assert AD('CC(C)CC(C)(C)C')=='2,2,4-Trimetilpentan' and Mol('CC(C)CC(C)(C)C').formula()[:2]==(8,18)
assert M2.nH(4)==0   # 4. karbon dört karbona bağlı: çift bağ 3. ile 4. arasında olamaz
sk2=tk(ciz(S2)[0])
Q('hk-adlandirma','orta','Alkenlerin IUPAC adlandırması','Ana zincir çift bağı içeren en uzun zincirdir; numaralandırma önce çift bağa en küçük sayıyı verir, sonra dallara bakılır.','Numaralandırmayı dallara göre yapıp çift bağa büyük sayı vermek; çift bağı adda unutmak.','şekilli',
 'Yapısı şekilde gösterilen açık zincirli hidrokarbon, bromlu suyun rengini gidermektedir.\nBuna göre, bu hidrokarbonun sistematik adı aşağıdakilerden hangisidir?',
 'Çizgi formülü verilen alkenin IUPAC adı.','Çift bağı içeren en uzun zinciri seç ve numaralandırmaya çift bağa en küçük sayı gelecek uçtan başla.',
 [B('Alken adlandırma','Ana zincir çift bağı içeren en uzun zincirdir; çift bağın konumu ilk karbonunun numarasıyla belirtilir ve numaralandırmada çift bağ en küçük sayıyı alır. Örnek: 3-Metil-1-büten, çift bağı 1. karbonda olan 4 karbonlu zincirdir')],
 [A('Ana zinciri bul','Çift bağı içeren en uzun zincir 5 karbonludur; çift bağ olduğu için kök penten olur.','5 karbon + çift bağ → penten'),
  A('Çift bağa sayı ver','Soldan numaralandırınca çift bağ 2. karbonda, sağdan numaralandırınca 3. karbonda kalır; çift bağa en küçük sayı verilir.','2 < 3 → soldan'),
  A('Dalları yaz','Bu yönde 2. karbonda bir, 4. karbonda iki metil bulunur.','2,4,4-trimetil'),
  A('Adı yaz','Dal adları ve çift bağın yeri birleştirilir.','2,4,4-Trimetil-2-penten')],
 'Numaralandırmada önce çift bağa, sonra dallara en küçük sayıları ver.',sekil=sk2,
 dogru=a2,sira=yer(a2,[k2,'2,4,4-Trimetil-1-penten','2,4,4-Trimetil-3-penten','2,2,4-Trimetilpentan'],'D'),
 yan=[(k2,'Numaralandırmayı dallara göre sağ uçtan yapmış; böylece çift bağa 3 sayısı gelmiş, oysa çift bağa en küçük sayı verilmelidir.','bilgi'),
      ('2,4,4-Trimetil-1-penten','Çift bağın 1. ve 2. karbon arasında olduğunu düşünmüş; şekilde çift bağ 2. ve 3. karbon arasındadır.','dikkat'),
      ('2,4,4-Trimetil-3-penten','Çift bağın yerini sağ uçtan, dalların yerini sol uçtan numaralandırarak vermiş; 4. karbon dört karbona bağlı olduğundan çift bağ yapamaz.','bilgi'),
      ('2,2,4-Trimetilpentan','Çift bağı adlandırmaya katmamış; “-an” sonekiyle doymuş bir hidrokarbon adı vermiş, oysa bileşik C₈H₁₆’dır.','dikkat')])

# ================= 03 · adlandırma + genel · orta · öncüllü =================
S3='CC#CC(C)C'; M3=Mol(S3); assert M3.formula()[:2]==(6,10)
assert AD(S3)=='4-Metil-2-pentin'
pos3=yerlesim(M3); assert dogrusal_karbon(M3,pos3)==4 and len(M3.carbons())==6
assert M3.formula()[1]==2*6-2 and M3.formula()[1]!=2*6
tr=[True,False,False]
nd=['üçlü bağ 2. karbonda, metil 4. karbondadır; numaralandırma üçlü bağa en küçük sayıyı verecek uçtan yapılır ve ad 4-Metil-2-pentindir',
    'molekül formülü C₆H₁₀’dur; 2n − 2 = 10 sağlandığından genel formül CₙH₂ₙ₋₂’dir, CₙH₂ₙ değildir',
    'yalnız üçlü bağı oluşturan iki karbon ile onlara bağlı iki karbon (toplam 4 karbon) aynı doğru üzerindedir; kalan karbonlar bu doğrunun dışındadır']
d3,y3,s3=onc(tr,nd,'A')
sk3=tk(ciz(S3)[0])
Q('hk-adlandirma','orta','Alkinlerde ad, formül ve geometri','Alkinde üçlü bağa bağlı karbonlar doğrusal dizilir; adlandırmada üçlü bağ en küçük sayıyı alır; genel formül CₙH₂ₙ₋₂’dir.','Genel formülü alkenle karıştırmak; tüm karbonların doğrusal olduğunu sanmak.','öncüllü',
 'Çizgi formülü şekilde verilen hidrokarbon açık zincirli bir bileşiktir.\n'+etiket_oncul('Adı 4-Metil-2-pentindir.','Genel formülü CₙH₂ₙ olan hidrokarbonlar sınıfındandır.','Karbon atomlarının tümü aynı doğru üzerinde bulunur.')+'Buna göre, bu bileşikle ilgili yukarıdaki yargılardan hangileri doğrudur?',
 'Doğru yargıların belirlenmesi.','Üçlü bağın ve ona bağlı karbonların dizilişini düşün; molekül formülünü sayarak genel formülle karşılaştır.',
 [B('Alkinler','Üçlü bağ içeren açık zincirli hidrokarbonlardır; genel formül CₙH₂ₙ₋₂’dir. Üçlü bağdaki karbonlar ile bunlara bağlı atomlar aynı doğru üzerindedir. Örnek: propin C₃H₄ (3 karbon, 4 hidrojen)')],
 oadim(tr,nd)+[A('Sonuç','Yalnız I doğrudur.','Yalnız I')],
 'Alkin: CₙH₂ₙ₋₂; yalnız üçlü bağdaki karbonlar ve komşuları doğrusaldır.',sekil=sk3,dogru=d3,yan=y3,sira=s3)

# ================= 04 · genel formül · kolay · tablo =================
cl4={'X':(5,12),'Y':(5,8),'Z':(5,10)}
dog4=tuple(sinif_h(*cl4[k]) for k in 'XYZ'); assert dog4==('Alkan','Alkin','Alken')
def sinifla(esl): # esl: sınıf -> h sayısı bağıntısı
    return tuple({esl[s](5):s for s in esl}[cl4[k][1]] for k in 'XYZ')
d1=sinifla({'Alkan':lambda n:2*n+2,'Alken':lambda n:2*n-2,'Alkin':lambda n:2*n})
d2=tuple({0:'Alkin',1:'Alken',2:'Alkan'}[sorted([12,10,8],reverse=True).index(cl4[k][1])] for k in 'XYZ')
d3_=sinifla({'Alkan':lambda n:2*n,'Alken':lambda n:2*n-2,'Alkin':lambda n:2*n+2})
d4=sinifla({'Alkan':lambda n:2*n,'Alken':lambda n:2*n+2,'Alkin':lambda n:2*n-2})
assert len({dog4,d1,d2,d3_,d4})==5 and d1==('Alkan','Alken','Alkin') and d2==('Alkin','Alkan','Alken') and d3_==('Alkin','Alken','Alkan') and d4==('Alken','Alkin','Alkan')
f4=lambda t:f'X: {t[0]}, Y: {t[1]}, Z: {t[2]}'
tb4=tablo_svg(['Bileşik','Karbon atomu sayısı','Hidrojen atomu sayısı'],[[k,str(cl4[k][0]),str(cl4[k][1])] for k in 'XYZ'])
Q('hk-genel','kolay','Genel formüllere göre sınıflandırma','Açık zincirli hidrokarbonlarda H sayısı alkanda 2n+2, alkende 2n, alkinde 2n−2’dir.','Alken ile alkinin genel formüllerini karıştırmak; H sayısı çoksa doymamışlık da çoktur sanmak.','tablo',
 'Açık zincirli X, Y ve Z hidrokarbonlarının her birinde en fazla bir adet çok katlı (çift ya da üçlü) bağ bulunmaktadır. Bu bileşiklerin moleküllerindeki karbon ve hidrojen atomu sayıları aşağıdaki tabloda verilmiştir.\nBuna göre, X, Y ve Z bileşiklerinin ait olduğu sınıflar aşağıdakilerden hangisinde doğru verilmiştir?',
 'X, Y ve Z’nin bileşik sınıfları.','Aynı karbon sayısında hidrojen sayısı, alkandan alkine doğru azalır; her sınıfın genel formülüne bak.',
 [B('Genel formüller','Açık zincirli alkanlar CₙH₂ₙ₊₂, alkenler CₙH₂ₙ, alkinler CₙH₂ₙ₋₂ genel formülüne uyar. Örnek: 3 karbonlu alkan C₃H₈, alken C₃H₆, alkin C₃H₄ olur')],
 [A('Formülleri yaz','n = 5 için alkan C₅H₁₂, alken C₅H₁₀, alkin C₅H₈ olur.','alkan 12 · alken 10 · alkin 8'.replace(' · ','; ')),
  A('X’i belirle','Hidrojen sayısı en fazla olan bileşik doymuştur.','X: H = 12 → alkan'),
  A('Y ve Z’yi belirle','Y’de 8, Z’de 10 hidrojen vardır; 2n−2 alkine, 2n alkene karşılık gelir.','Y: 8 → alkin; Z: 10 → alken')],
 'Karbon sayısı eşitken hidrojen sayısı alkan > alken > alkin sırasıyla ikişer azalır.',sekil=tb4,
 dogru=f4(dog4),sira=yer(f4(dog4),[f4(d1),f4(d2),f4(d3_),f4(d4)],'A'),
 yan=[(f4(d1),'Alken için CₙH₂ₙ₋₂, alkin için CₙH₂ₙ formülünü kullanıp Y ile Z’yi birbirine karıştırmış.','bilgi'),
      (f4(d2),'Hidrojen sayısı arttıkça doymamışlığın da arttığını düşünmüş; en çok hidrojenli X’i alkin, en az hidrojenli Y’yi alkan sanmış.','bilgi'),
      (f4(d3_),'Alkan için CₙH₂ₙ, alken için CₙH₂ₙ₋₂, alkin için CₙH₂ₙ₊₂ formüllerini kullanmış.','bilgi'),
      (f4(d4),'Alkan ile alkenin genel formüllerini yer değiştirmiş; X’i alken, Z’yi alkan sanmış.','bilgi')])

# ================= 05 · genel formül · orta · grafik + öncüllü + olumsuz =================
f5={'I':lambda n:2*n+2,'II':lambda n:2*n,'III':lambda n:2*n-2}
g5=''.join(f'\\addplot[thick,{st},mark={mk_}] coordinates {{{" ".join(f"({n},{f5[k](n)})" for n in range(2,7))}}} node[pos=1,right]{{{k}}};\n'
           for k,st,mk_ in [('I','solid','*'),('II','dashed','square*'),('III','dotted','triangle*')])
sk5=pgf(g5,w='7.4cm',h='6cm',ek='xlabel={Karbon atomu sayısı},ylabel={Hidrojen atomu sayısı},xmin=1,xmax=7,ymin=0,ymax=16,xtick={2,3,4,5,6},ytick={0,2,4,6,8,10,12,14,16},grid=both,minor tick num=0')
tr=[True,True,False]
nd=['I numaralı doğru üzerindeki noktalar H = 2n + 2 bağıntısını sağlar (2 karbon için 6, 3 karbon için 8 hidrojen), yani genel formül CₙH₂ₙ₊₂’dir',
    'tam yanmada her karbon atomu bir CO₂ verdiğinden CO₂ mol sayısı yalnız karbon sayısına bağlıdır; karbon sayıları aynıysa mol sayıları da aynıdır',
    'III numaralı doğru H = 2n − 2 bağıntısını sağlar; açık zincirli ve tek çok katlı bağlı hidrokarbonlarda bu genel formül alkinlere aittir, yani molekülde çift bağ değil üçlü bağ bulunur']
d5,y5,s5=onc(tr,nd,'A',yanlis_sor=True); assert d5=='Yalnız III'
Q('hk-genel','orta','Hidrojen–karbon sayısı grafiği','Doğruların kesişim ve eğimlerinden H = 2n+2, 2n, 2n−2 bağıntıları okunur; aynı karbon sayısı aynı CO₂ mol sayısı demektir.','III. doğruyu çift bağlı sanmak; genel formülü sınıfla eşleştirmemek.','öncüllü',
 'I, II ve III numaralı doğrular, açık zincirli ve en fazla bir çok katlı bağ içeren üç ayrı hidrokarbon serisindeki bileşiklerin molekülündeki hidrojen atomu sayısının karbon atomu sayısıyla değişimini göstermektedir.\n'+etiket_oncul('I numaralı doğrudaki bileşiklerin genel formülü CₙH₂ₙ₊₂’dir.','Karbon sayıları aynı olan I ve II numaralı doğrulardaki bileşiklerin 1’er molünün tam yanmasında eşit mol CO₂ oluşur.','III numaralı doğrudaki bileşiklerin tümü molekülünde çift bağ içerir.')+'Buna göre, yukarıdaki yargılardan hangileri yanlıştır?',
 'Yanlış yargıların belirlenmesi.','Doğruların üzerinden iki noktanın koordinatını okuyup H ile n arasındaki bağıntıyı yaz; sonra genel formülleri karşılaştır.',
 [B('Genel formüller','Açık zincirli alkanlar CₙH₂ₙ₊₂, alkenler CₙH₂ₙ, alkinler CₙH₂ₙ₋₂ formülüne uyar. Örnek: 4 karbonlu alkan 10, alken 8, alkin 6 hidrojen içerir')],
 oadim(tr,nd)+[A('Sonuç','Yanlış olan yalnız III’tür.','Yalnız III')],
 'Doğrudan okunan H = f(n) bağıntısını genel formüllerle eşleştir.',sekil=sk5,dogru=d5,yan=y5,sira=s5)

# ================= 06 · yanma · orta · grafik =================
nX=Fr(1,2); co2=Fr(3,2); h2o=Fr(3,2); x6=co2/nX; y6=2*h2o/nX; assert (x6,y6)==(3,6) and y6==2*x6    # alken formülü
o2=x6+y6/4; assert o2==Fr(9,2)
assert o2*nX==Fr(9,4) and x6==3 and x6+y6/2==6 and 2*x6+y6/2==9 and 2*co2+h2o==Fr(9,2)
sk6=pgf('\\addplot[fill=vurgu!35,draw=black] coordinates {(co2,1.5) (h2o,1.5)};',w='6.4cm',h='5cm',
        ek='ybar,symbolic x coords={co2,h2o},xtick=data,xticklabels={CO$_2$,H$_2$O},bar width=30pt,ymin=0,ymax=2,ytick={0,0.5,1,1.5,2},ylabel={Mol sayısı},enlarge x limits=0.6,ymajorgrids,/pgf/number format/use comma')
Q('hk-yanma','orta','Yanma ürünlerinden formül ve O₂ gereksinimi','Ürünlerin mol sayılarından C ve H sayıları, buradan x + y/4 ile O₂ mol sayısı bulunur.','O₂ miktarını yalnız bir üründen ya da 0,5 mol üzerinden bulmak; atom sayısını O₂ mol sayısı sanmak.','grafik',
 'Doğal gaz ve LPG gibi yakıtların ana bileşenleri hidrokarbonlardır. Açık zincirli X hidrokarbonunun 0,5 molü yeterli miktarda O₂ ile tamamen yakıldığında (ürünler CO₂ ve H₂O) oluşan ürünlerin mol sayıları grafikte verilmiştir.\nBuna göre, X hidrokarbonunun 1 molünün tam yanması için gereken O₂ kaç moldür?',
 '1 mol X’in tam yanmasında harcanan O₂ mol sayısı.','Önce 1 mol X için ürünlerin mol sayılarını bul; ürünlerdeki toplam oksijen atomu sayısını O₂ molüne çevir.',
 [B('Tam yanma','CₓHᵧ + (x + y/4) O₂ → x CO₂ + (y/2) H₂O. Örnek: C₂H₆ için 2 + 6/4 = 3,5 mol O₂ gerekir')],
 [A('1 mol için ürünler','0,5 mol X 1,5 mol CO₂ ve 1,5 mol H₂O verdiğine göre 1 mol X 3 mol CO₂ ve 3 mol H₂O verir.','1 mol X → 3 CO₂ + 3 H₂O'),
  A('Formülü bul','3 mol CO₂ 3 karbon, 3 mol H₂O 6 hidrojen demektir.','x = 3, y = 6 → C₃H₆'),
  A('O₂ miktarı','Ürünlerdeki oksijen atomu 2 × 3 + 3 = 9 mol olup bir O₂ molü 2 atom verir.','9 ÷ 2 = 4,5 mol O₂'),
  A('Kontrol','x + y/4 bağıntısı da aynı sonucu verir.','3 + 6/4 = 4,5')],
 'Ürünlerdeki toplam O atomu sayısının yarısı, harcanan O₂ mol sayısıdır.',sekil=sk6,
 dogru=Fr(9,2),yan=[(Fr(9,4),'Grafikteki 0,5 mol X üzerinden hesaplamış; soru 1 mol X için O₂ miktarını sormaktadır.','dikkat'),
                    (3,'Yalnız CO₂’nin oluşumu için gereken O₂’yi (3 mol) hesaba katmış, H₂O’daki oksijeni unutmuş.','dikkat'),
                    (6,'Her H₂O için bir O₂ molü harcandığını sanıp 3 + 3 = 6 bulmuş; H₂O’daki bir oksijen atomu yarım O₂ molüdür.','bilgi'),
                    (9,'Ürünlerdeki toplam oksijen atomu sayısını (9) O₂ mol sayısı olarak almış; bir O₂ molekülü iki atom içerir.','islem')])

# ================= 07 · yanma · zor · kap şekli =================
hc,ox=10,70; sonuc=[]
for x in range(1,7):
    for y in range(2,2*x+3,2):
        if hc*x==30 and ox-hc*(x+Fr(y,4))==25: sonuc.append((x,y))
assert sonuc==[(3,6)]
assert (80-55)==hc*(1+Fr(6,4))      # sıvı H2O için toplam hacim azalması
yv=lambda ot:4*(ot-3)    # x=3 için x + y/4 = ot
assert yv(Fr(45,10))==6 and 2*3-2==4 and 2*3+2==8 and yv(Fr(55,10))==10 and yv(Fr(70,10))==16
def tup(x,h,etiket_ic='',alt='',bolme=None):
    s=[f'\\draw[thick] ({x:.2f},{h:.2f}) -- ({x:.2f},0) -- ({x+1.3:.2f},0) -- ({x+1.3:.2f},{h:.2f});',
       f'\\draw[ultra thick] ({x-0.1:.2f},{h:.2f}) -- ({x+1.4:.2f},{h:.2f});',f'\\draw[thick] ({x+0.65:.2f},{h:.2f}) -- ({x+0.65:.2f},{h+0.35:.2f}) -- ({x+0.35:.2f},{h+0.35:.2f});',
       f'\\fill[gray!15] ({x+0.03:.2f},0.03) rectangle ({x+1.27:.2f},{h-0.03:.2f});']
    if bolme:
        s.append(f'\\draw[dashed] ({x:.2f},{bolme:.2f}) -- ({x+1.3:.2f},{bolme:.2f});')
    return s
V=0.04
s7=[]
s7+=tup(0,80*V,bolme=10*V)
s7.append(f'\\node at (0.65,{5*V:.2f}) {{X}};'); s7.append(f'\\node at (0.65,{45*V:.2f}) {{O$_2$}};')
s7.append(f'\\node[left,align=right] at (-0.1,{5*V:.2f}) {{10 mL}};'); s7.append(f'\\node[left,align=right] at (-0.1,{45*V:.2f}) {{70 mL}};')
s7+=tup(3.6,55*V); s7.append(f'\\node at (4.25,{27.5*V:.2f}) {{55 mL}};')
s7+=tup(7.2,25*V); s7.append(f'\\node at (7.85,{12.5*V:.2f}) {{25 mL}};')
s7.append(ok_(1.6,1.3,3.5,1.3,'tam yanma,\\\\soğutma'))
s7.append(ok_(5.2,1.3,7.1,1.3,'KOH\\\\çözeltisi'))
s7.append('\\node[align=center,font=\\footnotesize] at (0.65,-0.55) {Başlangıç};')
s7.append('\\node[align=center,font=\\footnotesize] at (4.25,-0.55) {Yanma sonrası};')
s7.append('\\node[align=center,font=\\footnotesize] at (7.85,-0.55) {KOH’dan sonra};')
sk7=tk(*s7)
Q('hk-yanma','zor','Hacimce yanma analizi','Gaz hacimleri oranları mol oranıdır: CO₂ hacminden karbon, harcanan O₂ hacminden hidrojen sayısı bulunur.','Harcanan O₂ yerine kalan ya da toplam hacmi kullanmak; bileşiği alkan ya da alkin varsaymak.','şekilli',
 'Aynı sıcaklık ve basınçta, hacmi değişebilen bir kapta açık zincirli X hidrokarbonu ile O₂ gazı şekilde verilen hacimlerde karıştırılıp X’in tamamı yakılıyor. Tepkimeden sonra kap başlangıç sıcaklığına getirildiğinde oluşan H₂O sıvı hâldedir. Kalan gaz karışımı KOH çözeltisinden geçirildiğinde yalnız CO₂ tutulmaktadır.\nBuna göre, X hidrokarbonunun molekülündeki hidrojen atomu sayısı kaçtır?',
 'X’in molekülündeki H atomu sayısı.','KOH’ın tuttuğu gazın hacminden karbon sayısını, kullanılan O₂ hacminden hidrojen sayısını bul.',
 [B('Hacimce yanma','Aynı sıcaklık ve basınçta gaz hacimleri mol sayısıyla orantılıdır. CₓHᵧ + (x + y/4) O₂ → x CO₂ + (y/2) H₂O. Örnek: 5 mL CH₄, 10 mL O₂ ile tepkimeye girer ve 5 mL CO₂ verir')],
 [A('CO₂ hacmini bul','KOH’tan geçince 55 − 25 = 30 mL gaz tutulmuştur; bu CO₂ hacmidir. 10 mL X için 30 mL CO₂, X’te 3 karbon demektir.','CO₂ = 30 mL → x = 3'),
  A('Harcanan O₂','Kalan O₂ 25 mL olduğuna göre harcanan O₂ 70 − 25 = 45 mL’dir; 10 mL X için 4,5 hacim O₂ gerekmiştir.','45 ÷ 10 = 4,5'),
  A('H sayısını bul','Yanma denklemine göre x + y/4 = 4,5 olmalıdır.','3 + y/4 = 4,5 → y = 6'),
  A('Kontrol','Toplam azalma 80 − 55 = 25 mL; sıvı H₂O için bu azalma 10 × (1 + y/4) olmalıdır.','10 × (1 + 6/4) = 25 mL')],
 'CO₂ hacmi karbonu, harcanan O₂ hacmi x + y/4 değerini verir.',sekil=sk7,
 dogru=6,yan=[(4,'Karbon sayısını 3 bulup bileşiği alkin sanarak 2x − 2 = 4 almış; harcanan O₂ ile hidrojen sayısını doğrulamamış.','dikkat'),
              (8,'Karbon sayısını 3 bulup bileşiği alkan sanarak 2x + 2 = 8 almış; O₂ kullanımı 4,5 hacim değil 5 hacim gerektirir.','dikkat'),
              (10,'Harcanan O₂ yerine 80 − 25 = 55 mL azalmayı kullanıp 5,5 = 3 + y/4 yazmış; böylece y = 10 bulmuş.','islem'),
              (16,'Başlangıçtaki 70 mL O₂’nin tamamının harcandığını sanıp 7 = 3 + y/4 yazmış; böylece y = 16 bulmuş.','dikkat')])

# ================= 08 · yanma · zor · şema =================
a8,b8=Fr(1,10),Fr(3,10); tot=Fr(2,5); hw=Fr(18,18)
assert a8+b8==tot and 4*a8+2*b8==hw
assert a8*44==Fr(22,5) and b8*40==12 and b8*44==Fr(66,5) and tot*44==Fr(88,5) and a8*40==4
sk8=tk('\\node[draw,rounded corners,align=center,inner sep=6pt] (a) at (0,0) {Karışım\\\\\\ce{C3H8} ve \\ce{C3H4}\\\\toplam $0{,}4$ mol};',
       '\\node[draw,rounded corners,align=center,inner sep=6pt] (b) at (6.2,0) {Oluşan \\ce{H2O}\\\\$18$ g};',
       '\\draw[-{Stealth[length=2.2mm,width=2mm]},thick] (a.east) -- (b.west) node[midway,above,align=center,font=\\footnotesize]{yeterli \\ce{O2} ile\\\\tam yanma};')
Q('hk-yanma','zor','Karışımın yanması','Karışımdaki bileşenlerin mol sayıları için iki denklem (toplam mol ve H₂O mol sayısı) yazılıp çözülür.','Karışımı tek bileşen gibi düşünmek; bileşenlerin mol kütlelerini karıştırmak.','şekilli',
 'Propan (C₃H₈) ve propin (C₃H₄) gazlarından oluşan bir karışım yeterli miktarda O₂ ile tamamen yakılıyor. Karışımın toplam mol sayısı ve yanma sonucunda oluşan suyun kütlesi şekilde verilmiştir.\n(H: 1, C: 12, O: 16)\nBuna göre, başlangıçtaki karışımda bulunan propanın kütlesi kaç gramdır?',
 'Karışımdaki propanın kütlesi (g).','Her bileşenin 1 molünün tam yanmasında kaç mol H₂O oluştuğunu yaz; bilinmeyen iki mol sayısı için iki denklem kur.',
 [B('Tam yanma ve karışım','CₓHᵧ yandığında y/2 mol H₂O oluşur. Örnek: C₂H₆ için 3, C₂H₂ için 1 mol H₂O oluşur. Karışımlarda her bileşenin katkısı toplanır')],
 [A('Su miktarı','H₂O’nun mol kütlesi 18 g/mol olduğuna göre 18 g su 1 mol eder.','18 ÷ 18 = 1 mol H₂O'),
  A('Denklemleri yaz','Propandan 4, propinden 2 mol H₂O oluşur; toplam mol 0,4’tür.','a + b = 0,4 ve 4a + 2b = 1'),
  A('Çöz','İlk denklemi 2 ile çarpıp çıkarınca 2a = 0,2 olur.','a = 0,1 mol propan; b = 0,3 mol propin'),
  A('Kütleyi bul','Propanın mol kütlesi 3 × 12 + 8 = 44 g/mol’dür.','0,1 × 44 = 4,4 g')],
 'İki bilinmeyen için “toplam mol” ve “oluşan H₂O” denklemlerini birlikte çöz.',sekil=sk8,
 dogru=Fr(22,5),yan=[(4,'Propanın mol sayısını doğru bulmuş ama kütleyi hesaplarken propinin mol kütlesini (40 g/mol) kullanmış.','islem'),
                     (12,'Mol sayılarını ters atayıp propin yerine propanı hesaplamış; 0,3 mol × 40 g/mol = 12 g propinin kütlesidir.','dikkat'),
                     (Fr(66,5),'Propanın mol sayısını 0,3 almış; bu değer propinin mol sayısıdır.','dikkat'),
                     (Fr(88,5),'Karışımın tamamının propan olduğunu varsayıp 0,4 mol × 44 g/mol hesaplamış.','bilgi')])

# ================= 09 · yanma · orta · grafik + öncüllü =================
o9={'X':Fr(3),'Y':Fr(5,2),'Z':Fr(7,2)}
n9=2; assert {1.5*n9+0.5,1.5*n9,1.5*n9-0.5}=={3.5,3,2.5}
sin9={'X':'Alken','Y':'Alkin','Z':'Alkan'}
for k,v in o9.items():
    c=2; h={'Alkan':2*c+2,'Alken':2*c,'Alkin':2*c-2}[sin9[k]]; assert c+Fr(h,4)==v
h2o9={k:{'Alkan':3,'Alken':2,'Alkin':1}[sin9[k]] for k in o9}; assert h2o9['X']!=h2o9['Y']
tr=[True,False,True]
nd=['O₂ gereksinimi en az olan Y alkindir (C₂H₂); alkinin 1 molü üçlü bağı doyurmak için 2 mol Br₂ bağlar',
    'X alken (C₂H₄) olduğundan 2 mol, Y alkin (C₂H₂) olduğundan 1 mol H₂O verir; mol sayıları eşit değildir',
    'bileşiklerin karbon sayıları aynıdır (2); her karbon bir CO₂ verdiğinden Z ve X’in 1’er molü eşit sayıda (2 mol) CO₂ oluşturur']
d9,y9,s9=onc(tr,nd,'E')
sk9=pgf('\\addplot[fill=vurgu!35,draw=black] coordinates {(X,3) (Y,2.5) (Z,3.5)};',w='6.6cm',h='5.2cm',
        ek='ybar,symbolic x coords={X,Y,Z},xtick=data,bar width=26pt,ymin=0,ymax=4,ytick={0,0.5,1,1.5,2,2.5,3,3.5,4},ylabel={Harcanan O$_2$ (mol)},xlabel={Bileşik (1’er mol)},enlarge x limits=0.3,ymajorgrids,/pgf/number format/use comma')
Q('hk-yanma','orta','Yanmada O₂ gereksinimi ve sınıf belirleme','Aynı karbon sayısında hidrojen azaldıkça 1 mol bileşiğin harcadığı O₂ azalır; sıralama alkan > alken > alkin’dir.','O₂ gereksinimi çok olanı alkin sanmak; H₂O ve CO₂ mol sayılarını karıştırmak.','öncüllü',
 'Karbon atomu sayıları aynı olan açık zincirli X, Y ve Z hidrokarbonlarından biri alkan, biri alken, biri alkindir (hangisinin hangisi olduğu belirtilmemiştir). Bileşiklerin 1’er molünün tam yanması için gereken O₂ mol sayıları grafikte verilmiştir.\n'+etiket_oncul('Y’nin 1 molü, 2 mol Br₂ ile tepkimeye girer.','X ve Y’nin 1’er molünün tam yanmasında oluşan H₂O mol sayıları eşittir.','Z ve X’in 1’er molünün tam yanmasında oluşan CO₂ mol sayıları eşittir.')+'Buna göre, yukarıdaki yargılardan hangileri doğrudur?',
 'Doğru yargıların belirlenmesi.','Karbon sayısı eşitken hidrojen sayısı değiştikçe harcanan O₂ miktarı da değişir; grafikteki sıralamadan sınıfları bul.',
 [B('Yanma ve doymamışlık','Aynı karbon sayısında 1 mol bileşiğin harcadığı O₂ = x + y/4 olduğundan alkan en çok, alkin en az O₂ gerektirir. Örnek: 3 karbonlu propan 5, propen 4,5, propin 4 mol O₂ harcar')],
 [A('Sınıfları belirle','O₂ gereksinimi hidrojen sayısıyla artar; en çok O₂ harcayan alkan, en az harcayan alkindir.','Z: alkan; X: alken; Y: alkin')]+oadim(tr,nd)+[A('Sonuç','Doğru yargılar I ve III’tür.','I ve III')],
 'Aynı C sayısında O₂ gereksinimi: alkan > alken > alkin; CO₂ eşit, H₂O farklıdır.',sekil=sk9,dogru=d9,yan=y9,sira=s9)

# ---------------- katılma (Markovnikov) yardımcıları ----------------
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

# ================= 10 · katılma · orta =================
S10='CC=C(C)CC'; M10=Mol(S10); p10=hx_katil(M10,'Br')
assert ayni(p10,'CCC(C)(Br)CC') and AD('CCC(C)(Br)CC')=='3-Bromo-3-metilpentan'
assert ayni(hx_katil(M10,'Br',ters=True),'CC(Br)C(C)CC') and AD('CC(Br)C(C)CC')=='2-Bromo-3-metilpentan'
assert AD('CC(Br)C(C)(Br)CC')=='2,3-Dibromo-3-metilpentan' and AD('CC(Br)=C(C)CC')=='2-Bromo-3-metil-2-penten' and AD('CCC(C)CC')=='3-Metilpentan'
n10=['2,3-Dibromo-3-metilpentan','2-Bromo-3-metil-2-penten','2-Bromo-3-metilpentan','3-Metilpentan']
sk10=tk(okla(S10,'\\ce{HBr}'))
Q('hk-katilma','orta','Alkene HX katılması','HX katılırken H, çift bağdaki H sayısı fazla olan karbona, X ise diğerine bağlanır (Markovnikov kuralı).','X’i H’si fazla karbona bağlamak; HX yerine X₂ ya da H₂ katılmış gibi düşünmek.','şekilli',
 'Açık zincirli bir hidrokarbonun çizgi formülü ve uygun şartlarda HBr ile gerçekleşen tepkimesi şekilde gösterilmiştir.\nBuna göre, bu tepkimede oluşan ana ürünün IUPAC adı aşağıdakilerden hangisidir?',
 'HBr katılma ürününün (ana ürün) adı.','Çift bağı oluşturan iki karbonda kaç H atomu olduğuna bak; H atomu fazla olan karbon, katılan H’yi alır.',
 [B('Markovnikov kuralı','Simetrik olmayan HX alkene katılırken H, çift bağdaki H sayısı fazla olan karbona; X ise H sayısı az olan karbona bağlanır. Örnek: propen + HCl → 2-kloropropan')],
 [A('Çift bağı incele','Çift bağın bir ucunda (2. karbon) 1 H, diğer ucunda (3. karbon) hiç H yoktur.','C2: 1 H; C3: 0 H'),
  A('Katılımı belirle','H, H’si fazla olan 2. karbona; Br ise 3. karbona gider; çift bağ tek bağa dönüşür.','C2 → +H; C3 → +Br'),
  A('Ürünü yaz','3. karbona hem metil hem etil hem de Br bağlıdır; ana zincir 5 karbonludur.','CH₃CH₂C(CH₃)(Br)CH₂CH₃'),
  A('Adı yaz','Br ve metil, 3. karbonda bulunur.','3-Bromo-3-metilpentan')],
 'H’si fazla karbon H’yi, H’si az karbon halojeni alır.',sekil=sk10,
 dogru='3-Bromo-3-metilpentan',sira=yer('3-Bromo-3-metilpentan',n10,'E'),
 yan=[(n10[0],'HBr yerine Br₂ katılmış gibi düşünmüş; iki Br atomunu komşu karbonlara bağlamış.','bilgi'),
      (n10[1],'Br’un çift bağlı karbondaki H ile yer değiştirdiğini sanmış; alkenlere HBr katılma tepkimesi verir, çift bağ tek bağa dönüşür.','bilgi'),
      (n10[2],'Br’u H’si fazla olan 2. karbona bağlamış; Markovnikov kuralına göre Br, H’si az olan 3. karbona gider.','bilgi'),
      (n10[3],'Br atomunu hiç bağlamamış; HBr yerine H₂ katılmış gibi alkan yazmış.','dikkat')])

# ================= 11 · katılma · orta · grafik + öncüllü =================
tr=[False,True,True]
nd=['X, Br₂ ile karanlıkta tepkime vermediğine göre açık zincirli doymuş bir hidrokarbondur ve genel formülü CₙH₂ₙ₊₂’dir, CₙH₂ₙ değildir',
    '0,1 mol Z, 0,2 mol Br₂ bağladığından iki mol katılma gerçekleşir; H₂ da Br₂ gibi katıldığı için 0,1 mol Z’yi doyurmak 0,2 mol H₂ ister',
    'Z, mol sayısının iki katı Br₂ bağladığından iki π bağı içerir; en fazla bir çok katlı bağlı olduğuna göre bu bağ üçlü bağdır']
d11,y11,s11=onc(tr,nd,'E')
sk11=pgf('\\addplot[fill=vurgu!35,draw=black,nodes near coords] coordinates {(X,0) (Y,0.1) (Z,0.2)};',w='6.4cm',h='5cm',
         ek='ybar,symbolic x coords={X,Y,Z},xtick=data,bar width=26pt,ymin=0,ymax=0.3,ytick={0,0.1,0.2,0.3},ylabel={Harcanan Br$_2$ (mol)},xlabel={Bileşik (0,1’er mol)},enlarge x limits=0.3,ymajorgrids,/pgf/number format/use comma,point meta=explicit symbolic')
Q('hk-katilma','orta','Br₂ tüketiminden doymamışlık','Alken 1, alkin 2 mol Br₂ ya da H₂ bağlar; doymuş hidrokarbon Br₂’yi karanlıkta bağlamaz.','Br₂ tüketimini bileşik sınıfıyla ilişkilendirememek; X’i CₙH₂ₙ sanmak.','öncüllü',
 'Açık zincirli ve her birinde en fazla bir çok katlı bağ bulunan X, Y ve Z hidrokarbonlarının 0,1’er molü, karanlıkta Br₂’nin CCl₄’teki çözeltisiyle tam olarak tepkimeye sokuluyor. Harcanan Br₂ mol sayıları grafikte verilmiştir.\n'+etiket_oncul('X’in genel formülü CₙH₂ₙ’dir.','Z’nin 0,1 molünü tamamen doyurmak için 0,2 mol H₂ gerekir.','Z’nin molekülünde üçlü bağ bulunur.')+'Buna göre, yukarıdaki yargılardan hangileri doğrudur?',
 'Doğru yargıların belirlenmesi.','Bileşik başına kaç mol Br₂ harcandığını bul; çift ve üçlü bağın kaç mol katılma yaptığını düşün.',
 [B('Br₂ ile katılma','Alkenin 1 molü 1 mol, alkinin 1 molü 2 mol Br₂ bağlar; alkanlar Br₂’yi karanlıkta bağlamaz. Örnek: 0,5 mol propin 1 mol Br₂ ile tam tepkime verir')],
 oadim(tr,nd)+[A('Sonuç','Doğru yargılar II ve III’tür.','II ve III')],
 'Katılan Br₂ mol sayısı ÷ bileşik mol sayısı = çok katlı bağdaki π bağı sayısı.',sekil=sk11,dogru=d11,yan=y11,sira=s11)

# ================= 12 · katılma · orta =================
S12='C#CC(C)C'; M12=Mol(S12); p12=hx_katil(M12,'Cl',2)
assert ayni(p12,'CC(Cl)(Cl)C(C)C') and AD('CC(Cl)(Cl)C(C)C')=='2,2-Dikloro-3-metilbütan'
assert ayni(hx_katil(M12,'Cl',1),'C=C(Cl)C(C)C') and AD('C=C(Cl)C(C)C')=='2-Kloro-3-metil-1-büten'
assert ayni(hx_katil(M12,'Cl',1,ters=True),'ClC=CC(C)C') and AD('ClC=CC(C)C')=='1-Kloro-3-metil-1-büten'
assert AD('ClC(Cl)CC(C)C')=='1,1-Dikloro-3-metilbütan' and AD('ClCC(Cl)C(C)C')=='1,2-Dikloro-3-metilbütan'
n12=['1,1-Dikloro-3-metilbütan','1,2-Dikloro-3-metilbütan','1-Kloro-3-metil-1-büten','2-Kloro-3-metil-1-büten']
sk12=tk(okla(S12,'2 mol \\ce{HCl}'))
Q('hk-katilma','orta','Alkine HX katılması','Alkine iki mol HX art arda katılır; her adımda X, H sayısı az olan karbona bağlanır ve ürün aynı karbonda iki halojen taşır.','Tek mol HCl katılıp durduğunu düşünmek; iki Cl’yi farklı karbonlara bağlamak.','şekilli',
 'Çizgi formülü şekilde verilen hidrokarbonun 1 molü, uygun şartlarda 2 mol HCl ile tamamen tepkimeye giriyor.\nBuna göre, oluşan ana ürünün IUPAC adı aşağıdakilerden hangisidir?',
 'Alkine 2 mol HCl katılması ürününün adı.','Her HCl katılmasında H’yi H sayısı fazla olan karbonun aldığını düşün; ikinci katılma sırasında hangi karbonda H daha fazla?',
 [B('Alkine HX katılması','Alkine ilk HX katılınca halojenli alken, ikinci HX katılınca doymuş bileşik oluşur; her adımda Markovnikov kuralı geçerlidir. Örnek: propin + 2 HBr → 2,2-dibromopropan')],
 [A('İlk katılma','Üçlü bağın ucundaki karbonda 1 H, öteki karbonda hiç H yoktur; H uç karbona, Cl ise 2. karbona bağlanır.','C1 → +H; C2 → +Cl: 2-kloro-3-metil-1-büten'),
  A('İkinci katılma','Yeni çift bağda uç karbon 2 H, 2. karbon 0 H taşır; yine H uca, Cl 2. karbona gider.','C1 → +H; C2 → +Cl'),
  A('Ürünü yaz','2. karbonda iki Cl, 3. karbonda metil bulunur; ana zincir 4 karbonludur.','CH₃–C(Cl)₂–CH(CH₃)–CH₃'),
  A('Adı yaz','Klorlar 2. karbondadır.','2,2-Dikloro-3-metilbütan')],
 'İki HX katılınca halojenler (Markovnikov’a göre) aynı karbonda toplanır.',sekil=sk12,
 dogru='2,2-Dikloro-3-metilbütan',sira=yer('2,2-Dikloro-3-metilbütan',n12,'B'),
 yan=[(n12[0],'Cl atomlarını H’si fazla olan uç karbona bağlamış; Markovnikov kuralına göre Cl, H’si az olan 2. karbona gider.','bilgi'),
      (n12[1],'Cl atomlarını komşu karbonlara bağlamış; bu, Cl₂ katılmasında görülen sonuçtur, HCl katılmasında değil.','bilgi'),
      (n12[2],'Yalnızca 1 mol HCl katılmış ve Cl’yi uç karbona bağlamış; soruda 2 mol HCl katılıyor ve Cl, 2. karbona bağlanır.','dikkat'),
      (n12[3],'İkinci HCl’nin katılmasını hesaba katmamış; ürün, 1 mol HCl katılmış halojenli alkendir.','dikkat')])

# ================= 13 · katılma · zor · hikâyeli =================
a13,b13=Fr(1,10),Fr(1,5); assert a13+b13==Fr(3,10) and 2*a13+b13==Fr(2,5)
assert a13*40==4 and a13*42==Fr(21,5) and Fr(1,5)*40==8 and Fr(3,10)*40==12 and Fr(2,5)*40==16
Q('hk-katilma','zor','Karışımın H₂ ile doyurulması','Alkine 2 mol, alkene 1 mol H₂ katılır; karışımın toplam mol ve H₂ mol sayıları iki denklem verir.','Her bileşiğe 1 mol H₂ katıldığını sanmak; bileşenlerin mol kütlelerini karıştırmak.','hikâyeli',
 'Bir laboratuvarda propin (C₃H₄) ve propen (C₃H₆) gazlarından oluşan 0,3 mol karışım, Ni katalizörlüğünde yeterli miktarda H₂ ile tamamen doymuş hidrokarbona dönüştürülüyor. Bu işlemde toplam 0,4 mol H₂ harcanıyor.\n(H: 1, C: 12)\nBuna göre, başlangıç karışımındaki propinin kütlesi kaç gramdır?',
 'Karışımdaki propinin kütlesi (g).','Propin için kaç mol, propen için kaç mol H₂ gerektiğini yazıp iki bilinmeyenli denklem kur.',
 [B('H₂ katılması','Ni katalizörlüğünde çift bağın her molüne 1, üçlü bağın her molüne 2 mol H₂ katılır. Örnek: 1 mol etin → 2 mol H₂ ile etan; 1 mol eten → 1 mol H₂ ile etan')],
 [A('Denklemleri kur','Propin a mol, propen b mol olsun. Toplam mol 0,3; harcanan H₂ 2a + b’dir.','a + b = 0,3 ve 2a + b = 0,4'),
  A('Çöz','İkinci denklemden birincisini çıkarınca a bulunur.','a = 0,1 mol propin; b = 0,2 mol propen'),
  A('Mol kütlesi','Propinin mol kütlesi 3 × 12 + 4 = 40 g/mol’dür.','M(C₃H₄) = 40'),
  A('Kütleyi bul','Kütle = mol sayısı × mol kütlesi.','0,1 × 40 = 4 g')],
 'Alkin 2, alken 1 mol H₂ bağlar: iki denklem, iki bilinmeyen.',
 dogru=4,yan=[(Fr(21,5),'Propinin mol sayısını doğru bulmuş ama kütleyi propenin mol kütlesiyle (42 g/mol) hesaplamış.','islem'),
              (8,'Katsayıları ters yazıp a + 2b = 0,4 almış; böylece 0,2 mol propin bulmuş.','bilgi'),
              (12,'Karışımın tamamını (0,3 mol) propin saymış.','dikkat'),
              (16,'Harcanan H₂ mol sayısını (0,4 mol) propinin mol sayısı sanmış.','dikkat')])

# ================= 14 · yer değiştirme · orta · öncüllü =================
KL=[('K','CCCCC'),('L','CC(C)CC'),('M','CC(C)(C)C')]
cnt={k:monoklor(s) for k,s in KL}; assert cnt=={'K':3,'L':4,'M':1} and sum(cnt.values())==8
for k,s in KL: assert Mol(s).formula()[:2]==(5,12)
sk14=tk(satir([(s,k,None) for k,s in KL]))
tr=[False,True,False]
nd=['K’nin 3 (1-, 2- ve 3-kloropentan), L’nin 4 farklı monoklorlu türevi vardır; sayılar eşit değildir',
    'M bileşiğinde (2,2-dimetilpropan) bütün hidrojenler birbirine eşdeğerdir; hangisi Cl ile yer değiştirirse değiştirsin tek ürün oluşur',
    'türev sayıları K için 3, L için 4, M için 1 olup toplam 8’dir; 9 değildir']
d14,y14,s14=onc(tr,nd,'B')
Q('hk-yerdegistirme','orta','Monoklorlu türev sayısı','Işık altında alkanda bir H, Cl ile yer değiştirir; eşdeğer olmayan her H konumu ayrı bir ürün verir.','Eşdeğer hidrojenleri ayrı saymak; dallı alkanlarda konum sayısını eksik bulmak.','öncüllü',
 'Işık altında Cl₂ ile tepkimeye giren K, L ve M alkanlarının çizgi formülleri şekilde verilmiştir. Her tepkimede bileşiğin yalnız bir H atomu Cl ile yer değiştirmektedir (stereoizomerler ayrı sayılmaz).\n'+etiket_oncul('K ve L’nin monoklorlu türevlerinin çeşit sayıları eşittir.','M’nin monoklorlu türevi tek çeşittir.','K, L ve M’nin monoklorlu türevlerinin toplam çeşit sayısı 9’dur.')+'Buna göre, yukarıdaki yargılardan hangileri doğrudur?',
 'Doğru yargıların belirlenmesi.','Her bileşikte birbirinden farklı (eşdeğer olmayan) karbon konumlarını say; aynı konumdaki hidrojenler aynı ürünü verir.',
 [B('Alkanlarda yer değiştirme','Alkanlar ışık altında halojenle H atomu değişimi yapar (CH₄ + Cl₂ → CH₃Cl + HCl). Eşdeğer olmayan her H konumu farklı bir monohalojenli ürün verir. Örnek: bütan 2, 2-metilpropan 2 çeşit monoklorlu türev verir')],
 oadim(tr,nd)+[A('Sonuç','Doğru yargı yalnız II’dir.','Yalnız II')],
 'Monohalojenli türev sayısı = eşdeğer olmayan karbon konumlarının sayısı.',sekil=sk14,dogru=d14,yan=y14,sira=s14)

# ================= 15 · yer değiştirme · zor · şema =================
mk15={'CH₃Cl':(Fr(101,10),Fr(101,2)),'CH₂Cl₂':(Fr(17,2),Fr(85)),'CHCl₃':(Fr(239,20),Fr(239,2))}
assert 12+3+Fr(71,2)==Fr(101,2) and 12+2+71==85 and 12+1+Fr(213,2)==Fr(239,2)
mol15={k:m/M for k,(m,M) in mk15.items()}; assert list(mol15.values())==[Fr(1,5),Fr(1,10),Fr(1,10)]
hcl=mol15['CH₃Cl']*1+mol15['CH₂Cl₂']*2+mol15['CHCl₃']*3; assert hcl==Fr(7,10)
assert sum(mol15.values())==Fr(2,5) and (hcl)/2==Fr(7,20) and 2*hcl==Fr(7,5) and mol15['CH₃Cl']==Fr(1,5)
sk15=tk('\\node[draw,rounded corners,align=center,inner sep=6pt] (a) at (0,0) {\\ce{CH4} ve \\ce{Cl2}};',
        '\\node[draw,rounded corners,align=center,inner sep=5pt] (b) at (5.3,1.3) {\\ce{CH3Cl}: $10{,}1$ g};',
        '\\node[draw,rounded corners,align=center,inner sep=5pt] (c) at (5.3,0) {\\ce{CH2Cl2}: $8{,}5$ g};',
        '\\node[draw,rounded corners,align=center,inner sep=5pt] (d) at (5.3,-1.3) {\\ce{CHCl3}: $11{,}95$ g};',
        '\\draw[-{Stealth[length=2.2mm,width=2mm]},thick] (a.east) -- (b.west) ; \\node[font=\\footnotesize] at (0,-0.85) {ışık altında};',
        '\\draw[-{Stealth[length=2.2mm,width=2mm]},thick] (a.east) -- (c.west);',
        '\\draw[-{Stealth[length=2.2mm,width=2mm]},thick] (a.east) -- (d.west);')
Q('hk-yerdegistirme','zor','Metanın klorlanması ve HCl miktarı','Her yer değiştirmede bir H atomu bir Cl ile değişir ve bir HCl açığa çıkar; HCl mol sayısı, ürünlerdeki toplam Cl atomu sayısına eşittir.','Ürünlerin mol sayısını HCl mol sayısı sanmak; Cl₂ ile HCl’deki klor atomlarını karıştırmak.','şekilli',
 'Yeterli miktarda CH₄ ve Cl₂ gazları karışımı ışık altında tepkimeye sokuluyor. Tepkime sonunda oluşan organik ürünler ve kütleleri şekilde verilmiştir (CCl₄ oluşmamıştır).\n(H: 1, C: 12, Cl: 35,5)\nBuna göre, bu tepkimelerde toplam kaç mol HCl oluşmuştur?',
 'Oluşan toplam HCl mol sayısı.','Ürünlerin mol sayısını bul; her ürünün oluşması için kaç H atomunun Cl ile değiştiğini düşün.',
 [B('Metanın klorlanması','Işık altında CH₄’ün H atomları sırayla Cl ile yer değiştirir: CH₄ → CH₃Cl → CH₂Cl₂ → CHCl₃ → CCl₄. Her yer değiştirmede 1 mol HCl açığa çıkar. Örnek: 1 mol CH₂Cl₂ oluşurken 2 mol HCl oluşur')],
 [A('Mol kütleleri','CH₃Cl 50,5; CH₂Cl₂ 85; CHCl₃ 119,5 g/mol’dür.','12 + 3 + 35,5 = 50,5; 12 + 2 + 71 = 85; 12 + 1 + 106,5 = 119,5'),
  A('Mol sayıları','Kütleler mol kütlelerine bölünür.','0,2 ; 0,1 ; 0,1 mol'),
  A('HCl sayısı','CH₃Cl için 1, CH₂Cl₂ için 2, CHCl₃ için 3 yer değiştirme olur; her biri bir HCl verir.','0,2 × 1 + 0,1 × 2 + 0,1 × 3'),
  A('Toplam','Değerler toplanır.','0,2 + 0,2 + 0,3 = 0,7 mol HCl')],
 'Oluşan HCl’nin mol sayısı = ürünlerde yer değiştiren toplam H atomu sayısı (mol).',sekil=sk15,
 dogru=Fr(7,10),yan=[(Fr(1,5),'Yalnızca CH₃Cl’ün oluşumunu hesaba katmış; diğer iki ürün de HCl açığa çıkarır.','dikkat'),
                     (Fr(7,20),'Ürünlerdeki Cl atomlarının sayısını (0,7 mol) ikiye bölüp HCl mol sayısı saymış; her yer değiştirmede 1 HCl oluşur.','bilgi'),
                     (Fr(2,5),'Ürünlerin toplam mol sayısını (0,2 + 0,1 + 0,1) HCl mol sayısı almış; her üründe tek HCl oluştuğunu sanmış.','bilgi'),
                     (Fr(7,5),'Cl₂’deki toplam klor atomu sayısını (0,7 mol ürün Cl’u + 0,7 mol HCl) HCl mol sayısı olarak vermiş.','islem')])

# ================= 16 · polimerleşme · orta · öncüllü (yanlış) =================
xo=0.0; mo,bm=ciz('C=CC',0.55,0.0); ym=(bm[2]+bm[3])/2
pa=[f'\\node at (0.1,{ym:.2f}) {{$n$}};']+mo
ax=bm[1]+0.45; pa.append(ok_(ax,ym,ax+2.2,ym,'katalizör,\\\\basınç'))
oxp=ax+2.9; A_=(oxp,0.6); C1=(oxp+0.736,0.175); C2=(oxp+1.472,0.6); B_=(oxp+2.208,0.175); Mt=(oxp+1.472,1.45)
for p,q in [(A_,C1),(C1,C2),(C2,Mt),(C2,B_)]: pa.append(f'\\draw[thick] ({p[0]:.3f},{p[1]:.3f}) -- ({q[0]:.3f},{q[1]:.3f});')
xl=oxp+0.368; xr=oxp+1.84
for xb,sg in [(xl,1),(xr,-1)]:
    pa.append(f'\\draw[thick] ({xb+sg*0.12:.3f},-0.2) -- ({xb:.3f},-0.2) -- ({xb:.3f},1.55) -- ({xb+sg*0.12:.3f},1.55);')
pa.append(f'\\node at ({xr+0.22:.3f},-0.35) {{$n$}};')
sk16=tk(*pa)
tr=[False,True,False]
nd=['katılma polimerleşmesinde monomerlerin π bağları açılarak monomerler birbirine bağlanır; H₂ gibi bir yan ürün oluşmaz',
    'tekrarlayan birim C₃H₆’dır ve monomerle aynı atomları taşır; yalnız çift bağ yerine tek bağlar oluşmuştur',
    'monomerlerin çift bağları açılıp tek bağa dönüştüğünden polimer zincirinde karbonlar arasında yalnız tek bağ bulunur']
d16,y16,s16=onc(tr,nd,'D',yanlis_sor=True); assert d16=='I ve III'
Q('hk-polimer','orta','Katılma polimerleşmesi','Alkenlerin çift bağı açılarak monomerler birbirine bağlanır; yan ürün yoktur, tekrarlayan birimin formülü monomerinki ile aynıdır.','Polimerleşmede yan ürün oluştuğunu ya da polimerde çift bağ kaldığını sanmak.','öncüllü',
 'Plastik eşya yapımında kullanılan polipropilenin, propenin katılma polimerleşmesiyle oluşumu şekilde gösterilmiştir.\n'+etiket_oncul('Tepkime sırasında yan ürün olarak H₂ gazı açığa çıkar.','Polimerin tekrarlayan biriminin molekül formülü, monomerinin molekül formülüyle aynıdır.','Polimer zincirinde karbon atomları arasında çift bağ bulunur.')+'Buna göre, bu tepkimeyle ilgili yukarıdaki yargılardan hangileri yanlıştır?',
 'Yanlış yargıların belirlenmesi.','Polimerleşmede monomerlerin çift bağlarına ne olduğunu ve atomların nereye gittiğini düşün.',
 [B('Katılma polimerleşmesi','Çift bağlı monomerlerin π bağı açılır ve monomerler birbirine tek bağlarla bağlanır; yan ürün oluşmaz. Örnek: n CH₂=CH₂ → (–CH₂–CH₂–)ₙ polietilen')],
 oadim(tr,nd)+[A('Sonuç','Yanlış yargılar I ve III’tür.','I ve III')],
 'Katılma polimerinde atomlar korunur, çift bağlar tek bağa dönüşür.',sekil=sk16,dogru=d16,yan=y16,sira=s16)

# ================= 17 · polimer · zor · tablo =================
mol_pe=Fr(84,28); mol_pp=Fr(84,42); assert (mol_pe,mol_pp)==(3,2)
o2_pe=mol_pe*(2+Fr(4,4)); o2_pp=mol_pp*(3+Fr(6,4)); assert o2_pe==9 and o2_pp==Fr(9) and o2_pe+o2_pp==18
assert mol_pe*3+mol_pp*3==15 and (mol_pe+mol_pp)*Fr(9,2)==Fr(45,2) and mol_pe*(2+Fr(4,2))+mol_pp*(3+Fr(6,2))==24
tb17=tablo_svg(['Numune','Polimer','Tekrarlayan birim','Kütle (g)'],[['X','Polietilen','C₂H₄','84'],['Y','Polipropilen','C₃H₆','84']])
Q('hk-polimer','zor','Polimerlerin yanması','Polimer, tekrarlayan birimlerin molüdür; numunenin mol sayısı birimin mol kütlesinden bulunur ve birimin yanma denklemiyle ölçeklenir.','Birim başına O₂ gereksinimini yanlış formülle bulmak; iki numuneye aynı katsayıyı uygulamak.','tablo',
 'Polietilen ve polipropilenin kütleleri ve tekrarlayan birimlerinin formülleri tabloda verilmiştir. X ve Y numuneleri ayrı ayrı yeterli miktarda O₂ ile tamamen yakılıyor (ürünler CO₂ ve H₂O’dur).\n(H: 1, C: 12)\nBuna göre, iki numunenin yanması için harcanan toplam O₂ kaç moldür?',
 'Harcanan toplam O₂ mol sayısı.','Her numunedeki tekrarlayan birimin mol sayısını bul; sonra birimin yanması için gereken O₂’yi x + y/4 ile hesapla.',
 [B('Polimerin yanması','Polimerin yanması, tekrarlayan birimlerin yanması gibi hesaplanır: CₓHᵧ birimi için x + y/4 mol O₂. Örnek: 1 mol (CH₂) birimi 1,5 mol O₂ harcar')],
 [A('Mol kütleleri','C₂H₄ için 28, C₃H₆ için 42 g/mol alınır.','28 ve 42 g/mol'),
  A('Birim mol sayıları','Numune kütlesi birim mol kütlesine bölünür.','X: 84 ÷ 28 = 3 mol; Y: 84 ÷ 42 = 2 mol'),
  A('Birim başına O₂','C₂H₄ için 2 + 1 = 3 mol, C₃H₆ için 3 + 1,5 = 4,5 mol O₂ gerekir.','3 ve 4,5 mol O₂'),
  A('Toplam','Numune O₂ miktarları toplanır.','3 × 3 + 2 × 4,5 = 9 + 9 = 18 mol')],
 'Polimeri tekrarlayan birim molleri gibi düşün: mol sayısı × (x + y/4).',sekil=tb17,
 dogru=18,yan=[(9,'Yalnızca bir numunenin O₂ gereksinimini (9 mol) bulmuş; ikinci numuneyi hesaba katmamış.','dikkat'),
               (15,'Her tekrarlayan birim için C₂H₄’ün değerini (3 mol O₂) kullanmış: 3 × 3 + 2 × 3.','islem'),
               (Fr(45,2),'Her tekrarlayan birim için C₃H₆’ın değerini (4,5 mol O₂) kullanmış: 5 × 4,5.','islem'),
               (24,'O₂ gereksinimini x + y/2 ile hesaplamış (C₂H₄ için 4, C₃H₆ için 6 mol); doğru bağıntı x + y/4’tür.','bilgi')])

# ================= 18 · izomer · kolay =================
MK,ML=Mol('CCCC'),Mol('CC(C)C'); assert MK.formula()[:2]==ML.formula()[:2]==(4,10) and not same(MK,ML) and not MK.mult() and not ML.mult()
sk18=tk(satir([('CCCC','K',None),('CC(C)C','L',None)],aralik=1.8))
o18=['Aynı bileşiğin farklı gösterimleridir.','Birbirinin geometrik (cis–trans) izomeridir.','Genel formülleri farklı bileşiklerdir.','Biri doymuş, diğeri doymamış hidrokarbondur.']
Q('hk-izomer','kolay','Yapı izomerliği','Molekül formülleri aynı, bağlanma sıraları farklı bileşikler yapı izomeridir; cis–trans izomerliği için çift bağ gerekir.','Zincir uzunluğu farklı olan bileşikleri farklı formüllü sanmak.','şekilli',
 'LPG’nin bileşenlerinden olan K ve L bileşiklerinin çizgi formülleri şekilde verilmiştir.\nBuna göre, K ve L bileşikleri için aşağıdakilerden hangisi doğrudur?',
 'K ve L arasındaki ilişkinin belirlenmesi.','Her iki bileşikteki karbon ve hidrojen sayısını say; karbonların birbirine bağlanma biçimini karşılaştır.',
 [B('Yapı izomerliği','Molekül formülü aynı, atomların bağlanma sırası farklı olan bileşikler yapı (zincir) izomeridir. Örnek: pentan ile 2-metilbütan (C₅H₁₂)')],
 [A('Formülleri bul','K’de 4 karbon ve 10 hidrojen, L’de de 4 karbon ve 10 hidrojen vardır.','K: C₄H₁₀; L: C₄H₁₀'),
  A('Bağlanmayı karşılaştır','K dallanmamış zincirdir; L’de 3 karbonlu zincire bir metil bağlıdır.','K: düz zincir; L: dallı zincir'),
  A('Sonuca git','Formül aynı, bağlanma farklı olduğundan yapı izomeridir; çift bağ olmadığı için cis–trans izomerliği söz konusu değildir.','yapı izomeri')],
 'Aynı formül + farklı bağlanma sırası = yapı izomerliği.',sekil=sk18,
 dogru='Birbirinin yapı izomeridir.',sira=yer('Birbirinin yapı izomeridir.',o18,'C'),
 yan=[(o18[0],'Çizgi formüllerini farklı çizilmiş aynı molekül sanmış; oysa K’de dal yoktur, L’de metil dalı vardır.','bilgi'),
      (o18[1],'Cis–trans izomerliğini yapı izomerliğiyle karıştırmış; iki bileşikte de çift bağ yoktur.','bilgi'),
      (o18[2],'Formülleri farklı sanmış; iki bileşik de C₄H₁₀’dur ve alkan genel formülüne uyar.','dikkat'),
      (o18[3],'Birinde çift bağ bulunduğunu düşünmüş; iki bileşikte de yalnız tek bağ vardır.','dikkat')])

# ================= 19 · izomer · orta · öncüllü =================
def geometrik(M):
    for a,b_,o in M.b:
        if o==2:
            ok=True
            for u,v in ((a,b_),(b_,a)):
                ch=[w for w,_ in M.adj[u] if w!=v]
                if not ch or (len(ch)==2 and enc(M,ch[0],u)==enc(M,ch[1],u)): ok=False
            if ok: return True
    return False
K19,L19=Mol('C=CCC'),Mol('CC=CC'); assert not geometrik(K19) and geometrik(L19)
def hidrojen(M):
    return mol_kur(M.el,[(a,b_,1) for a,b_,o in M.b])
assert same(hidrojen(K19),hidrojen(L19)) and canon(hidrojen(K19))==canon(Mol('CCCC'))
def yan_taraf(smi,stereo):
    M=Mol(smi); pos=yerlesim(M,stereo=stereo); a,b_=1,2; d=(pos[b_][0]-pos[a][0],pos[b_][1]-pos[a][1])
    cr=lambda q:d[0]*(pos[q][1]-pos[a][1])-d[1]*(pos[q][0]-pos[a][0]); return cr(0)*cr(3)>0
assert yan_taraf('CC=CC',{(1,2):'cis'}) and not yan_taraf('CC=CC',{(1,2):'trans'})
sk19=tk(satir([('C=CCC','K',None),('CC=CC','L',{(1,2):'cis'}),('CC=CC','M',{(1,2):'trans'})],aralik=1.3))
tr=[True,True,False]
nd=['K’de çift bağdaki uç karbonda iki H vardır; her iki karbonunda da farklı iki grup bulunmadığından cis–trans izomerliği göstermez',
    'L ve M aynı bağlanma sırasına sahiptir; metil grupları çift bağın aynı tarafında (L) ve zıt taraflarında (M) bulunur, yani geometrik izomerdir',
    'K ve L’nin H₂ ile doyurulması aynı ürünü, n-bütanı verir; çift bağın yeri farklı olsa da doymuş ürün aynıdır']
d19,y19,s19=onc(tr,nd,'D')
Q('hk-izomer','orta','Alkenlerde konum ve geometrik izomerlik','Çift bağın yeri değişirse yapı (konum) izomeri, çift bağa bağlı karbonlarda iki farklı grup varsa cis–trans izomerliği görülür.','Uç alkende cis–trans arayıp bulmak; doyurunca farklı ürün beklemek.','öncüllü',
 'Aşağıda çizgi formülleri verilen K, L ve M bileşikleri aynı molekül formülüne sahip açık zincirli hidrokarbonlardır.\n'+etiket_oncul('K’nin cis–trans izomeri yoktur.','L ve M birbirinin geometrik izomeridir.','K ve L’nin H₂ ile tam doyurulmasında farklı ürünler oluşur.')+'Buna göre, yukarıdaki yargılardan hangileri doğrudur?',
 'Doğru yargıların belirlenmesi.','Çift bağa bağlı karbonların her birinde iki farklı grup olup olmadığına bak; sonra H₂ katılmış ürünün karbon iskeletini yaz.',
 [B('Alkenlerde izomerlik','Çift bağın konumu farklıysa konum (yapı) izomeri oluşur. Çift bağdaki her karbonda iki farklı grup varsa cis–trans izomerliği görülür. Örnek: 1-propenin (CH₂=CH–CH₃) cis–trans izomeri yoktur, çünkü uç karbonda iki H bulunur')],
 oadim(tr,nd)+[A('Sonuç','Doğru yargılar I ve II’dir.','I ve II')],
 'Cis–trans için çift bağın her ucunda iki farklı grup gerekir.',sekil=sk19,dogru=d19,yan=y19,sira=s19)

# ================= 20 · izomer · zor =================
G5,geo5=izomerler(5,'alken'); ad5={AD(smi) for smi in ['C=CCCC','CC=CCC','C=C(C)CC','C=CC(C)C','CC=C(C)C']}
assert len(G5)==5 and geo5==1 and len(G5)+geo5==6
assert {canon(Mol(s)) for s in ['C=CCCC','CC=CCC','C=C(C)CC','C=CC(C)C','CC=C(C)C']}==set(G5)
assert ad5=={'1-Penten','2-Penten','2-Metil-1-büten','3-Metil-1-büten','2-Metil-2-büten'}
unb=3; assert unb==1+2           # 1-penten, cis/trans-2-penten
assert 8==6+2 and 10==5+5       # 3-penten ayrı sayıldı; 5 halkalı yapı izomeri (siklopentan, metilsiklobütan, etilsiklopropan, 1,1- ve 1,2-dimetilsiklopropan)
Q('hk-izomer','zor','C₅H₁₀ alkenlerinin izomer sayısı','Önce yapı izomerleri (iskelet + çift bağ konumu) sayılır, sonra çift bağın her ucunda iki farklı grup bulunanlar için cis–trans eklenir.','2- ve 3-penteni ayrı saymak; cis–trans’ı unutmak; halkalı izomerleri katmak.','hikâyeli',
 'Bir öğrenci, molekül formülü C₅H₁₀ olan ve molekülünde yalnız bir çift bağ bulunan açık zincirli hidrokarbonların bütün yapı izomerlerini ve geometrik izomerlerini yazmaya çalışıyor. Cis ve trans biçimleri ayrı bileşik olarak sayılacaktır.\nBuna göre, öğrencinin yazması gereken toplam bileşik sayısı kaçtır?',
 'Açık zincirli C₅H₁₀ alkenlerinin (geometrik izomerler dahil) toplam sayısı.','Önce 5 karbonlu düz zincirde çift bağ konumlarını, sonra 4 karbonlu zincire metil bağlı yapıları yaz; ardından cis–trans yapabilenleri bul.',
 [B('Alkenlerde izomerlik','Önce karbon iskeleti, sonra çift bağın yeri değiştirilerek yapı izomerleri bulunur; çift bağdaki her karbonda iki farklı grup varsa cis–trans izomerleri de ayrı bileşiktir. Örnek: C₄H₈ açık zincirli alkenleri 4 tanedir (1-büten, cis- ve trans-2-büten, 2-metilpropen)')],
 [A('Düz zincirliler','1-Penten ve 2-penten düz zincirlidir; 3-penten, numaralandırma sağdan yapılınca 2-pentendir.','1-penten, 2-penten (2 tane)'),
  A('Dallı zincirliler','4 karbonlu zincirde metil bağlı üç alken yazılır.','2-metil-1-büten, 3-metil-1-büten, 2-metil-2-büten'),
  A('Cis–trans','Yalnız 2-pentende çift bağın her ucunda iki farklı grup (CH₃ ile H, C₂H₅ ile H) bulunur; diğerlerinde uçta iki aynı grup (H, H ya da CH₃, CH₃) vardır.','2-penten: cis ve trans'),
  A('Toplam','5 yapı izomeri vardır, 2-pentenin iki geometrik izomeri ayrı sayılınca 1 bileşik fazlalaşır.','5 + 1 = 6')],
 'Önce yapı izomerlerini say, sonra cis–trans yapabilenlere +1 ekle.',
 dogru=6,yan=[(3,'Yalnız dallanmamış zincirli alkenleri saymış (1-penten, cis- ve trans-2-penten); dallı yapıları atlamış.','dikkat'),
              (5,'Yapı izomerlerini doğru bulmuş ama 2-pentenin cis ve trans biçimlerini tek bileşik saymış.','dikkat'),
              (8,'2-penten ile 3-penteni farklı bileşik sayıp ikisine de cis–trans eklemiş; oysa 3-penten, ters numaralandırıldığında 2-pentendir.','bilgi'),
              (10,'Açık zincirli olma koşulunu unutup 5 halkalı C₅H₁₀ izomerini (siklopentan gibi) da saymış; cis–trans’ı ise hesaba katmamış.','dikkat')])

# ================= yaz =================
def bitir_ak():
    for qq in P.ANA: qq['kardes']=None
    P.yaz(os.path.join(GD,'hidrokarbon-1.json'),'/tmp/bos-hidrokarbon.json')
    tipler={}
    for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu='akim|'+KONU))['kartlar'].append(c['id'])
    json.dump(dict(konu=KONU,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2018–2026 kimya soruları (yalnız mantık), MEB 11. sınıf kimya.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar','akhidrokarbon.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler),'sorular',len(P.ANA))
bitir_ak()
