"""AYT Kimya · Organik Tepkimeler ve İzomeri · 2. dalga · 10 soru. Kardeş yok, ipucu 1.
Yapılar tek bir SMILES benzeri dizgeden hem çizilir hem çözümlenir; tepkime ürünleri ve izomer sayıları graf üzerinde kaba kuvvetle hesaplanıp assert edilir."""
import sys,os,json,math,itertools,re
from fractions import Fraction as Fr
from itertools import combinations
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-kim')); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
import _hafif_kim2 as H
from _hafif_kim2 import *
from _hafif_kim import onc,tek,etk
from cizim import tikz_svg
import networkx as nx
KONU_AD='Organik Tepkimeler ve İzomeri'; KEY='akim|Organik Tepkimeler ve İzomeri'
P=Parti('orgtepkimeiki',KONU_AD,KEY,ders='AYT Kimya',idon='aytkim'); H.KONU=KONU_AD
KAYNAK='ÖSYM AYT 2018–2026 Kimya organik tepkime ve izomeri soruları (yalnız mantık) · MEB 12. sınıf Organik Bileşikler'
def kartla(no,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(f'K-AKORGT2-{no}',alt,fikir,tuzak,z,kalip,adim,tipId,tip,KAYNAK)
TIP={'sinif':('ot-sinif','Tepkime türünü belirleme'),'kat':('ot-katilma','Katılma tepkimeleri'),'yer':('ot-yerdegistirme','Yer değiştirme tepkimeleri'),
     'ayr':('ot-ayrilma','Ayrılma tepkimeleri'),'yuk':('ot-yukseltgenme','Yükseltgenme ve indirgenme'),'kon':('ot-kondenzasyon','Kondenzasyon (ester oluşumu)'),
     'izo':('ot-izomer','Yapı, geometrik ve fonksiyonel grup izomerliği'),'hes':('ot-hesap','Organik tepkimelerde mol ve kütle hesabı'),'zin':('ot-zincir','Tepkime zincirleri')}
def Q(no,tp,z,kalip,alt,kaz,fikir,tuzak,ozet,ad,**k):
    t,tn=TIP[tp]; kartla(no[-2:],alt,fikir,tuzak,z,kalip,len(ad),t,tn)
    assert len(k['ip'])==1; mk(P,no,ad=ad,adim=len(ad),tipId=t,tip=tn,z=z,alt=alt,kaz=kaz,kalip=kalip,kart=f'K-AKORGT2-{no[-2:]} ({ozet})',**k)
ORD=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
def OC(d,sira): return onc(d,[tuple(x for x in t.replace('Yalnız ','').replace(',',' ').replace(' ve ',' ').split()) for t in sira])
def sr(*k): assert [x for x in ORD if x in k]==list(k),k; return list(k)

# ================= yapı modeli =================
VAL={'C':4,'O':2,'Cl':1,'Br':1}
def parse(smi):
    G=nx.Graph(); st=[]; prev=None; o=1; i=0
    while i<len(smi):
        ch=smi[i]
        if ch=='(': st.append(prev); i+=1; continue
        if ch==')': prev=st.pop(); i+=1; continue
        if ch=='=': o=2; i+=1; continue
        if ch=='#': o=3; i+=1; continue
        if smi[i:i+2] in ('Cl','Br'): e=smi[i:i+2]; i+=2
        else: e=ch; i+=1
        k=G.number_of_nodes(); G.add_node(k,t=e)
        if prev is not None: G.add_edge(prev,k,o=o)
        prev=k; o=1
    for v in G: assert sum(G[v][w]['o'] for w in G[v])<=VAL[G.nodes[v]['t']],(smi,v)
    return G
def nH(G,v): return VAL[G.nodes[v]['t']]-sum(G[v][w]['o'] for w in G[v])
def formul(G):
    c=sum(1 for v in G if G.nodes[v]['t']=='C'); h=sum(nH(G,v) for v in G); o=sum(1 for v in G if G.nodes[v]['t']=='O')
    x=sum(1 for v in G if G.nodes[v]['t'] in('Cl','Br'))
    return (c,h,o,x)
def ayni(A,B): return nx.is_isomorphic(A,B,node_match=lambda a,b:a['t']==b['t'],edge_match=lambda a,b:a['o']==b['o'])
def tekil(L):
    r=[]
    for g in L:
        if not any(ayni(g,x) for x in r): r.append(g)
    return r
def C_(G,v): return G.nodes[v]['t']=='C'
def karbonil_O(G,c): return [w for w in G[c] if G.nodes[w]['t']=='O' and G[c][w]['o']==2]
def sinifla(G):
    T=set()
    for v in G:
        t=G.nodes[v]['t']
        if t=='C':
            for w in G[v]:
                if C_(G,w) and G[v][w]['o']==2 and v<w: T.add('alken')
                if C_(G,w) and G[v][w]['o']==3 and v<w: T.add('alkin')
        if t!='O': continue
        ns=list(G[v])
        if len(ns)==1 and G[v][ns[0]]['o']==1:
            c=ns[0]
            if karbonil_O(G,c): T.add('asit')
            elif all(G[c][w]['o']==1 for w in G[c]): T.add('alkol')
            else: T.add('enol')
        elif len(ns)==2:
            if any(karbonil_O(G,c) for c in ns): T.add('ester')
            elif all(G[c][w]['o']==1 for c in ns for w in G[c]): T.add('eter')
            else: T.add('diger')
        elif len(ns)==1 and G[v][ns[0]]['o']==2:
            c=ns[0]; cn=[w for w in G[c] if w!=v]
            if not any(G.nodes[w]['t']=='O' for w in cn): T.add('aldehit' if len(cn)<=1 else 'keton')
    return T
def dal(G,v,par):
    return G.nodes[v]['t']+'('+','.join(sorted(str(G[v][w]['o'])+dal(G,w,v) for w in G[v] if w!=par))+')'
def geo_cift(G):
    n=0
    for a,b in G.edges:
        if G[a][b]['o']==2 and C_(G,a) and C_(G,b):
            ok=True
            for u,v in((a,b),(b,a)):
                hv=[w for w in G[u] if w!=v]
                if len(hv)==0: ok=False
                elif len(hv)==2 and str(G[u][hv[0]]['o'])+dal(G,hv[0],u)==str(G[u][hv[1]]['o'])+dal(G,hv[1],u): ok=False
            if ok: n+=1
    return n
def stereo_say(G): return 2**geo_cift(G)
# ---- kaba kuvvet izomer üretimi: asiklik, en çok bir çok katlı bağ ----
def uret(nC,nO,nX,u):
    N=nC+nO+nX; sonuc=[]
    for T in nx.nonisomorphic_trees(N):
        nodes=list(T.nodes)
        for Os in combinations(nodes,nO):
            kalan=[v for v in nodes if v not in Os]
            for Xs in combinations(kalan,nX):
                tip={v:('O' if v in Os else ('Cl' if v in Xs else 'C')) for v in nodes}
                if any(T.degree(v)!=1 for v in Xs): continue
                if any(T.degree(v)>2 for v in Os): continue
                if any(tip[a]!='C' and tip[b]!='C' for a,b in T.edges): continue
                adaylar=[None] if u==0 else [e for e in T.edges if 'Cl' not in (tip[e[0]],tip[e[1]]) and not(tip[e[0]]=='O' and tip[e[1]]=='O')]
                for e in adaylar:
                    G=nx.Graph()
                    for v in nodes: G.add_node(v,t=tip[v])
                    for a,b in T.edges: G.add_edge(a,b,o=2 if e in((a,b),(b,a)) else 1)
                    if any(sum(G[v][w]['o'] for w in G[v])>VAL[G.nodes[v]['t']] for v in G): continue
                    if any(G.nodes[v]['t']=='O' and len(G[v])==2 and any(G[v][w]['o']!=1 for w in G[v]) for v in G): continue
                    if not any(ayni(G,x) for x in sonuc): sonuc.append(G)
    return sonuc
def say(L,*siniflar):
    return sum(1 for g in L if sinifla(g)==set(siniflar))
# ---- tepkime fonksiyonları ----
def kopya(G): return G.copy()
def HX_ekle(G,X):
    """Markovnikov ana ürün(ler)i: X, hidrojeni az olan karbona."""
    r=[]
    for a,b in G.edges:
        if G[a][b]['o']==2 and C_(G,a) and C_(G,b):
            ha,hb=nH(G,a),nH(G,b)
            for hedef,eş in ((a,ha<=hb),(b,hb<=ha)):
                if eş:
                    N=kopya(G); N[a][b]['o']=1; k=max(N.nodes)+1; N.add_node(k,t=X); N.add_edge(hedef,k,o=1); r.append(N)
    return tekil(r)
def X2_ekle(G,X):
    N=kopya(G)
    for a,b in list(N.edges):
        if N[a][b]['o']==2 and C_(N,a) and C_(N,b):
            N[a][b]['o']=1
            for hedef in (a,b): k=max(N.nodes)+1; N.add_node(k,t=X); N.add_edge(hedef,k,o=1)
    return N
def H2_ekle(G):
    N=kopya(G)
    for a,b in list(N.edges):
        if N[a][b]['o']>1 and C_(N,a) and C_(N,b): N[a][b]['o']=1
    return N
def H2O_ekle(G):
    """alkene Markovnikov hidrasyon"""
    r=[]
    for a,b in G.edges:
        if G[a][b]['o']==2 and C_(G,a) and C_(G,b):
            ha,hb=nH(G,a),nH(G,b)
            for hedef,eş in ((a,ha<=hb),(b,hb<=ha)):
                if eş:
                    N=kopya(G); N[a][b]['o']=1; k=max(N.nodes)+1; N.add_node(k,t='O'); N.add_edge(hedef,k,o=1); r.append(N)
    return tekil(r)
def alkin_hidrasyon(G):
    r=[]
    for a,b in G.edges:
        if G[a][b]['o']==3:
            ha,hb=nH(G,a),nH(G,b)
            for hedef,eş in ((a,ha<=hb),(b,hb<=ha)):
                if eş:
                    N=kopya(G); N[a][b]['o']=1; k=max(N.nodes)+1; N.add_node(k,t='O'); N.add_edge(hedef,k,o=2); r.append(N)
    return tekil(r)
def ayrilma(G,cikan):
    """cikan: 'O' (alkol -> alken + H2O) ya da 'Cl'. Alkenler (stereo ayrılmamış) listesi."""
    r=[]
    for x in G:
        if G.nodes[x]['t']!=cikan or len(G[x])!=1: continue
        c=list(G[x])[0]
        for w in G[c]:
            if w!=x and C_(G,w) and nH(G,w)>0 and G[c][w]['o']==1:
                N=kopya(G); N.remove_node(x); N[c][w]['o']=2; r.append(N)
    return tekil(r)
def stereo_urun(L): return sum(stereo_say(g) for g in L)
def monoklor(G):
    r=[]
    for v in G:
        if C_(G,v) and nH(G,v)>0:
            N=kopya(G); k=max(N.nodes)+1; N.add_node(k,t='Cl'); N.add_edge(v,k,o=1); r.append(N)
    return tekil(r)
def yukseltgen(G):
    """alkol -> aldehit/keton (tek –OH varsayımı)"""
    for x in G:
        if G.nodes[x]['t']=='O' and len(G[x])==1:
            c=list(G[x])[0]
            if nH(G,c)>=1:
                N=kopya(G); N[x][c]['o']=2; return N
    return None
def aldehit_asit(G):
    N=kopya(G)
    for c in N:
        if karbonil_O(N,c) and nH(N,c)==1:
            k=max(N.nodes)+1; N.add_node(k,t='O'); N.add_edge(c,k,o=1); return N
    return None
def indirgen(G):
    N=kopya(G)
    for a,b in list(N.edges):
        if N[a][b]['o']==2 and {N.nodes[a]['t'],N.nodes[b]['t']}=={'C','O'}: N[a][b]['o']=1
    return N
def esterle(asit,alkol):
    A=kopya(asit); 
    oh=[v for v in A if A.nodes[v]['t']=='O' and len(A[v])==1 and A[v][list(A[v])[0]]['o']==1][0]; c=list(A[oh])[0]; A.remove_node(oh)
    B=nx.relabel_nodes(alkol,{v:v+1000 for v in alkol}); U=nx.compose(A,B)
    ox=[v for v in B if B.nodes[v]['t']=='O'][0]; U.add_edge(c,ox,o=1); return nx.convert_node_labels_to_integers(U)
def Hdegis(G,eski,yeni):
    N=kopya(G)
    for v in N:
        if N.nodes[v]['t']==eski: N.nodes[v]['t']=yeni
    return N
M=lambda s:parse(s)
def kalip_assert(): pass

# ================= çizim =================
BL=1.0
def yerles(G,over=None,bl=None):
    bl=bl or BL; over=over or {}
    pos={0:(0.0,0.0)}; dr={}; sg={}; par={0:None}
    def ch(v): return sorted(w for w in G[v] if w!=par[v])
    def koy(v,w,a,s):
        par[w]=v; dr[w]=over.get(w,a); sg[w]=s
        pos[w]=(pos[v][0]+bl*math.cos(math.radians(dr[w])),pos[v][1]+bl*math.sin(math.radians(dr[w])))
        yeni(w)
    def yeni(v):
        c=ch(v)
        if not c: return
        if par[v] is None:
            if len(c)==1: koy(v,c[0],30,1)
            else:
                for w,a in zip(c,[30,150,-90]): koy(v,w,a,1)
            return
        d=dr[v]; s0=sg[v]; po=G[v][par[v]]['o']
        if len(c)==1:
            w=c[0]
            if po==3 or G[v][w]['o']==3: koy(v,w,d,s0)
            else: koy(v,w,d+60*(-s0),-s0)
        elif len(c)==2: koy(v,c[0],d+60,1); koy(v,c[1],d-60,-1)
        else: koy(v,c[0],d+90,1); koy(v,c[1],d,s0); koy(v,c[2],d-90,-1)
    yeni(0); return pos,dr
def etiket(G,v,pos,par=None):
    t=G.nodes[v]['t']
    if t=='C': return None
    if t=='O' and len(G[v])==1 and G[v][list(G[v])[0]]['o']==1:
        p=list(G[v])[0]; return 'HO' if pos[v][0]<pos[p][0]-1e-6 else 'OH'
    return t
def ciz(G,ox=0.0,oy=0.0,over=None,bl=None,ad=None):
    pos,dr=yerles(G,over,bl); out=[]; sh={'OH':.3,'HO':.3,'O':.2,'Cl':.25,'Br':.28}
    E={v:etiket(G,v,pos) for v in G}
    for a,b,d in G.edges(data=True):
        p=(pos[a][0]+ox,pos[a][1]+oy); q=(pos[b][0]+ox,pos[b][1]+oy)
        dx,dy=q[0]-p[0],q[1]-p[1]; ln=math.hypot(dx,dy); ux,uy=dx/ln,dy/ln; nx_,ny_=-uy,ux
        ca=sh.get(E[a],0); cb=sh.get(E[b],0)
        p2=(p[0]+ux*ca,p[1]+uy*ca); q2=(q[0]-ux*cb,q[1]-uy*cb)
        for k in {1:[0],2:[-.06,.06],3:[-.09,0,.09]}[d['o']]:
            out.append(f'\\draw[thick] ({p2[0]+nx_*k:.3f},{p2[1]+ny_*k:.3f}) -- ({q2[0]+nx_*k:.3f},{q2[1]+ny_*k:.3f});')
    for v in G:
        if E[v]: out.append(f'\\node[inner sep=0pt,font=\\small] at ({pos[v][0]+ox:.3f},{pos[v][1]+oy:.3f}) {{{E[v]}}};')
    xs=[pos[v][0]+ox for v in G]; ys=[pos[v][1]+oy for v in G]
    pad=lambda v:.3 if E[v] else 0
    x0=min(pos[v][0]+ox-pad(v) for v in G); x1=max(pos[v][0]+ox+pad(v) for v in G); y0=min(pos[v][1]+oy-pad(v) for v in G); y1=max(pos[v][1]+oy+pad(v) for v in G)
    return out,(x0,x1,y0,y1)
def cis_trans(G,over=None):
    """ilk C=C bağı için 'cis' / 'trans' (çizimdeki koordinatlardan)"""
    pos,_=yerles(G,over)
    for a,b,d in G.edges(data=True):
        if d['o']==2 and C_(G,a) and C_(G,b):
            ua=[w for w in G[a] if w!=b]; ub=[w for w in G[b] if w!=a]; assert len(ua)==1 and len(ub)==1
            ax,ay=pos[a]; bx,by=pos[b]
            cr=lambda w:(bx-ax)*(pos[w][1]-ay)-(by-ay)*(pos[w][0]-ax)
            return 'cis' if cr(ua[0])*cr(ub[0])>0 else 'trans'
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'; TAIL='\n\\end{tikzpicture}'
ARR='-{Stealth[length=2.4mm,width=2.2mm]}'
def tk(*parts,assert_w=None):
    return tikz_svg(HEAD+'\n'.join(p if isinstance(p,str) else '\n'.join(p) for p in parts)+TAIL)
def sema(items,y=0.0,bl=0.9,bosluk=0.45,x0=0.0,ok_uz=2.0):
    """items: ('m',smi,over,etiket) | ('+',) | ('->',ust,alt[,uzunluk]) | ('kutu',metin) | ('y',metin). Soldan sağa; (kod,genişlik,alt-y) döner."""
    out=[]; x=x0; alt_en=0.0; et=[]; ymin=y
    for it in items:
        if it[0]=='m':
            G=parse(it[1]) if isinstance(it[1],str) else it[1]; over=it[2] if len(it)>2 else None; e=it[3] if len(it)>3 else None
            pos,_=yerles(G,over,bl); xs=[p[0] for p in pos.values()]; ys=[p[1] for p in pos.values()]
            ox=x-min(xs)+.3; oy=y-(min(ys)+max(ys))/2
            c,bb=ciz(G,ox,oy,over,bl); out+=c; ymin=min(ymin,bb[2])
            if e: et.append(((bb[0]+bb[1])/2,e,bb[2]))
            x=bb[1]+bosluk
        elif it[0]=='+':
            out.append(f'\\node at ({x+.1:.3f},{y:.3f}) {{\\Large +}};'); x+=.55+bosluk*.4
        elif it[0]=='->':
            L_=it[3] if len(it)>3 else ok_uz
            out.append(f'\\draw[{ARR},thick] ({x:.3f},{y:.3f}) -- ({x+L_:.3f},{y:.3f});')
            if it[1]: out.append(f'\\node[above,inner sep=2pt,font=\\small] at ({x+L_/2:.3f},{y+.02:.3f}) {{{it[1]}}};')
            if len(it)>2 and it[2]: out.append(f'\\node[below,inner sep=2pt,font=\\small] at ({x+L_/2:.3f},{y-.02:.3f}) {{{it[2]}}};')
            x+=L_+bosluk*.6; ymin=min(ymin,y-.5)
        elif it[0]=='kutu':
            w=.55+.2*len(it[1]); out.append(f'\\node[draw,thick,rounded corners=2pt,minimum width={w:.2f}cm,minimum height=.75cm,font=\\bfseries] at ({x+w/2:.3f},{y:.3f}) {{{it[1]}}};'); x+=w+bosluk*.6; ymin=min(ymin,y-.4)
        elif it[0]=='y':
            w=.17*len(it[1])+.3; out.append(f'\\node[anchor=west,inner sep=1pt] at ({x:.3f},{y:.3f}) {{{it[1]}}};'); x+=w+bosluk*.5; ymin=min(ymin,y-.3)
    for xc,e,_ in et: out.append(f'\\node[font=\\small\\bfseries] at ({xc:.3f},{ymin-.4:.3f}) {{{e}}};')
    return '\n'.join(out),x,(ymin-(.8 if et else .1))-y
def satirlar(sat,aralik=0.7,**k):
    """sat: sema öğe listeleri; üst üste dizilir."""
    kod=[]; y=0.0; en=0.0
    for it in sat:
        c,x,alt=sema(it,y=y,**k); kod.append(c); en=max(en,x); y=y+alt-1.0
    assert en<=14.2,('çok geniş',en)
    return '\n'.join(kod)
def sira_ad(Gs,etiketler,bl=0.9,bosluk=1.0):
    """yan yana moleküller, altlarında etiket"""
    items=[]
    for G,e in zip(Gs,etiketler): items.append(('m',)+tuple(G)+(e,))
    return items

# ================= doğrulamalar (genel) =================
SD=lambda s:sorted(s)
def yer(sira_,dogru_,i): 
    r=[x for x in sira_ if x!=dogru_]; return r[:i]+[dogru_]+r[i:]
def sadelik(): pass


# ================= ek yardımcılar =================
def alkinHX(G,X):
    r=[]
    for a,b in G.edges:
        if G[a][b]['o']==3:
            ha,hb=nH(G,a),nH(G,b)
            for hedef,eş in ((a,ha<=hb),(b,hb<=ha)):
                if eş:
                    N=kopya(G); N[a][b]['o']=2; k=max(N.nodes)+1; N.add_node(k,t=X); N.add_edge(hedef,k,o=1); r.append(N)
    return tekil(r)
def hidroliz(E):
    for o in E:
        if E.nodes[o]['t']=='O' and len(E[o])==2:
            cs=list(E[o]); ck=[c for c in cs if karbonil_O(E,c)]
            if ck:
                c=ck[0]; r=[x for x in cs if x!=c][0]
                N=kopya(E); N.remove_edge(o,c); k=max(N.nodes)+1; N.add_node(k,t='O'); N.add_edge(c,k,o=1)
                comps=[N.subgraph(s).copy() for s in nx.connected_components(N)]
                asit=[x for x in comps if c in x][0]; alkol=[x for x in comps if o in x][0]
                return nx.convert_node_labels_to_integers(alkol),nx.convert_node_labels_to_integers(asit)
def pg(opts,body):
    return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n\\begin{axis}['+opts+']\n'+body+'\n\\end{axis}\n\\end{tikzpicture}')
def co(pts): return ' '.join(f'({x:.3f},{y:.4f})' for x,y in pts)

# ================= 01 · fonksiyonel grup izomeri · kolay · şekil =================
K1=parse('CCO'); E1=parse('COC')
assert formul(K1)==formul(E1)==(2,6,1,0) and sinifla(K1)=={'alkol'} and sinifla(E1)=={'eter'} and not ayni(K1,E1)
for s in ('CC=O','CC(=O)O','CC(O)C','CCOC'): assert formul(parse(s))!=formul(K1),s
SK=tk(satirlar([[('m','CCO',None,'K')]]))
o=dict(dogru='Metoksimetan',yan=[('Etanal','Etanal C₂H₄O formüllüdür; K’nin formülü C₂H₆O olduğundan izomeri değildir.','bilgi'),
 ('Etanoik asit','Etanoik asit C₂H₄O₂ formüllüdür; hidrojen ve oksijen sayısı K’den farklıdır.','bilgi'),
 ('2-Propanol','2-Propanol C₃H₈O formüllüdür; karbon sayısı K’den fazla olduğundan izomeri değildir.','bilgi'),
 ('Etil metil eter','Bu bileşik bir eterdir ama C₃H₈O formüllüdür; karbon sayısı K’den farklı olduğu için izomeri sayılmaz.','dikkat')])
Q('0001','izo','kolay','şekilli','Fonksiyonel grup izomerliği','Verilen bileşiğin aynı formüllü, farklı fonksiyonel gruplu izomerini belirler.',
  'Fonksiyonel grup izomerleri aynı molekül formülüne sahiptir ama farklı fonksiyonel grup taşır; önce formül eşitliği, sonra grup farkı sınanır.','Karbon sayısı farklı bileşiği aynı gruptan sanıp izomer saymak.','alkolün fonksiyonel grup izomeri',
  [A('K’nin formülünü yaz','İskelet formülünden karbon ve hidrojen sayıları sayılır; oksijen bir tanedir.','K: C₂H₆O'),
   A('Aynı formüllüleri ayır','Şıklardan yalnız C₂H₆O formüllü olan bileşik izomer adayıdır.','Karbon, hidrojen, oksijen sayıları eşit olmalı'),
   A('Grubu karşılaştır','K bir alkoldür; aynı formüllü olan bileşikte –OH yoktur, oksijen iki karbon arasındadır.','Alkol ≠ eter'),
   A('Sonuç','Formülü aynı, fonksiyonel grubu farklı olan bileşik izomerdir.','CH₃–O–CH₃')],
  metin='Şekilde iskelet formülü verilen K bileşiği ile ilgili olarak aşağıdakilerden hangisi K’nin fonksiyonel grup izomeridir?',
  sekil=SK,istenen='K bileşiğinin fonksiyonel grup izomeri.',ip=['Önce K’nin molekül formülünü yaz; sonra şıklarda aynı formüllü olanları ayır.'],
  bilgi=[B('İzomerlik','Molekül formülleri aynı, yapıları farklı bileşiklere izomer denir. Fonksiyonel grup izomerlerinde atom sayıları aynıdır ama bileşikler farklı fonksiyonel gruplara sahiptir. Örnek: propanal ile propanon C₃H₆O formüllüdür; biri aldehit, diğeri ketondur')],
  puf='İzomer aramada ilk ölçüt molekül formülünün birebir aynı olmasıdır.',dogru=o['dogru'],yan=o['yan'],sira=['Metoksimetan','Etanal','Etanoik asit','2-Propanol','Etil metil eter'])

# ================= 02 · doyurma için H2 · kolay · şekil · sayısal =================
S2=['C=CC','C=CC=C','C#CC']; pi=[sum(G_[a][b]['o']-1 for a,b in G_.edges) for G_ in map(parse,S2)]; assert pi==[1,2,2]
n2=Fr(1,10); h2=n2*sum(pi); assert h2==Fr(1,2)
SK=tk(satirlar([[('m','C=CC',None,'K'),('m','C=CC=C',None,'L'),('m','C#CC',None,'M')]],bosluk=1.2))
Q('0002','kat','kolay','şekilli','Doyurma için gereken H₂','Çoklu bağ sayısına göre Ni katalizörlüğünde harcanan H₂ mol sayısını bulur.',
  'Her π bağı bir mol H₂ ile doyar: çift bağ 1, üçlü bağ 2 π bağıdır; harcanan H₂ molü, bileşik molü ile π bağ sayısının çarpımıdır.','Üçlü bağı tek π bağı saymak ya da çift bağlı her bileşiğe 1 mol H₂ yazmak.','H₂ ile doyurma',
  [A('π bağlarını say','Çift bağ 1, üçlü bağ 2 π bağı içerir; iskelet formüllerinden sayılır.','K: 1 · L: 2 · M: 2'),
   A('Her bileşiğin H₂ gereksinimi','Her bileşiğin 0,1 molü, π bağ sayısı kadar katı H₂ harcar.','0,1 + 0,2 + 0,2'),
   A('Topla','Üç bileşiğin gereksinimi toplanır.','0,5 mol H₂')],
  metin='Şekilde iskelet formülleri verilen K, L ve M bileşiklerinin her birinden 0,1 mol alınarak bir karışım hazırlanıyor.\nBu karışımı Ni katalizörlüğünde tamamen doyurmak için en az kaç mol H₂ gerekir?',
  sekil=SK,istenen='Gerekli H₂ mol sayısı.',ip=['Her bileşikteki çift ve üçlü bağları ayrı ayrı say; hangisinin kaç π bağı taşıdığına dikkat et.'],
  bilgi=[B('H₂ katılması','Ni katalizörlüğünde H₂ çoklu bağlara katılır; bir π bağı bir mol H₂ ile doyurulur. Örnek: 1 mol 1-büten 1 mol H₂, 1 mol 2-bütin 2 mol H₂ ile bütana dönüşür')],
  puf='Üçlü bağ iki π bağı olduğundan iki mol H₂ harcatır.',dogru=Fr(1,2),
  yan=[(Fr(3,10),'Her bileşiğe yalnız 1 mol H₂ yazmıştır; L ve M’nin ikişer π bağı olduğunu hesaba katmamıştır.','bilgi'),
       (Fr(2,5),'Üçlü bağı tek π bağı saymıştır; 0,1 × (1 + 2 + 1) işlemi 0,4 verir.','bilgi'),
       (Fr(3,5),'Üçlü bağı üç π bağı saymıştır; 0,1 × (1 + 2 + 3) işlemi 0,6 verir.','bilgi'),
       (Fr(4,5),'Her bileşiğin π bağ sayısına bir de iskelet için 1 ekleyerek 0,1 × (2 + 3 + 3) işlemi 0,8 bulmuştur.','islem')])

# ================= 03 · alkine HBr · orta · öncüllü · şekil =================
P3=parse('C#CC'); X3=alkinHX(P3,'Br'); assert len(X3)==1 and ayni(X3[0],parse('CC(Br)=C'))
Y3=HX_ekle(X3[0],'Br'); assert len(Y3)==1 and ayni(Y3[0],parse('CC(Br)(Br)C')) and not ayni(Y3[0],parse('BrCC(C)Br'))
assert ayni(X2_ekle(parse('C=CC'),'Br'),parse('BrCC(C)Br'))
d=dict(I=(True,'1 mol HBr üçlü bağa katılınca brom hidrojeni olmayan ikinci karbona bağlanır; X 2-bromopropendir'),
       II=(True,'X’in çift bağına HBr katılırken brom yine hidrojeni olmayan karbona gider; Y, iki bromu da ikinci karbonda taşır'),
       III=(False,'1,2-dibromopropan Br₂ katılmasından oluşur; HBr katılmasında iki halojen aynı karbonda toplanır'))
o=OC(d,sr('Yalnız II','I ve II','I ve III','II ve III','I, II ve III')); assert o['dogru']=='I ve II'
SK=tk(satirlar([[('m','C#CC'),('->','HBr','1 mol',2.2),('kutu','X'),('->','HBr','fazla',2.2),('kutu','Y')]],bosluk=0.5))
Q('0003','kat','orta','öncüllü','Alkine ardışık HX katılması','Alkine HBr’nin iki kez katılmasında Markovnikov kuralını uygulayarak ürünleri yorumlar.',
  'Alkine HX katılınca önce haloalken, fazla HX ile dihaloalkan oluşur; her basamakta halojen hidrojeni az olan karbona bağlanır.','Fazla HX ile iki halojeni farklı karbonlara bağlamak.','propin + 2HBr',
  [A('X’i bul','Üçlü bağ çift bağa dönerken brom, hidrojeni olmayan karbona bağlanır.','X: CH₂=CBr–CH₃'),
   A('Y’yi bul','Çift bağdaki hidrojen sayısı az olan karbona yine brom gider.','Y: CH₃–CBr₂–CH₃'),
   A('Yargıları sına','Y’de iki brom aynı karbondadır; ardışık karbonlara bağlı iki brom Br₂ katılmasının izidir.','I ve II doğru')],
  metin='Şekilde propinin hidrojen bromürle ardışık tepkimeleri gösterilmiştir. Her basamakta ana ürün oluşmaktadır.\nI. X bileşiğinin adı 2-bromopropendir.\nII. Y bileşiğinde iki brom atomu aynı karbona bağlıdır.\nIII. Y bileşiğinin adı 1,2-dibromopropandır.\nBuna göre bu yargılardan hangileri doğrudur?',
  sekil=SK,istenen='Doğru olan yargılar.',ip=['Her basamakta çoklu bağın hangi karbonunun daha az hidrojen taşıdığını belirleyip bromun yerini buna göre yaz.'],
  bilgi=[B('Alkine HX katılması','Alkine HX iki basamakta katılır: önce haloalken, sonra dihaloalkan oluşur. Her basamakta halojen, hidrojeni az olan karbona bağlanır. Örnek: 1-bütin + 2HCl → 2,2-diklorobütan')],
  puf='İki katılmada da halojen hidrojeni az olan karbona gider; Y’de halojenler yan yana değil, aynı karbondadır.',dogru=o['dogru'],yan=o['yan'],sira=o['sira'])

# ================= 04 · propanollerin yükseltgenmesi · orta · öncüllü · şekil =================
K4,L4,M4=parse('CCCO'),parse('CC(O)C'),parse('CC(C)(C)O')
a4=yukseltgen(K4); b4=yukseltgen(L4); assert ayni(a4,parse('CCC=O')) and ayni(b4,parse('CC(C)=O')) and yukseltgen(M4) is None
assert ayni(aldehit_asit(a4),parse('CCC(=O)O')) and formul(a4)==formul(b4) and sinifla(a4)=={'aldehit'} and sinifla(b4)=={'keton'}
d=dict(I=(True,'K birincil alkoldür; önce propanale, ardından propanoik aside yükseltgenir'),
       II=(False,'K’nin ilk ürünü propanal, L’nin ürünü propanondur; bunlar aynı formüllü ama farklı gruplu olduğundan zincir değil fonksiyonel grup izomeridir'),
       III=(False,'M üçüncül alkoldür; –OH taşıyan karbonda hidrojen olmadığından yükseltgenmez'))
o=OC(d,sr('Yalnız I','Yalnız II','I ve II','II ve III','I, II ve III')); assert o['dogru']=='Yalnız I'
SK=tk(satirlar([[('m','CCCO',None,'K'),('m','CC(O)C',None,'L'),('m','CC(C)(C)O',None,'M')]],bosluk=1.2))
Q('0004','yuk','orta','öncüllü','Alkollerin sınıfına göre yükseltgenmesi','Birincil, ikincil ve üçüncül alkollerin yükseltgenme ürünlerini karşılaştırır.',
  'Birincil alkol aldehit, sonra asit; ikincil alkol keton verir; üçüncül alkol yükseltgenmez. Aynı sayıda karbonlu aldehit ve keton fonksiyonel grup izomeridir.','Üçüncül alkolün de keton verdiğini sanmak; aldehit–keton ilişkisini zincir izomerliği saymak.','alkol sınıfları',
  [A('Alkolleri sınıflandır','–OH taşıyan karbona bağlı karbon sayısına bak.','K: birincil · L: ikincil · M: üçüncül'),
   A('Ürünleri yaz','Birincil alkol aldehite, ikincil alkol ketona yükseltgenir; üçüncül alkol tepkime vermez.','K → propanal · L → propanon · M → tepkime yok'),
   A('Yargıları sına','Propanal ile propanon aynı formüllü, farklı gruplu olduğundan fonksiyonel grup izomeridir.','Yalnız I doğru')],
  metin='Şekilde iskelet formülleri verilen K, L ve M alkolleri asitli K₂Cr₂O₇ çözeltisiyle ayrı ayrı yükseltgenme koşullarında tepkimeye sokuluyor.\nI. K’nin yükseltgenmesiyle önce aldehit, ardından karboksilik asit oluşur.\nII. K ve L’nin ilk yükseltgenme ürünleri birbirinin zincir izomeridir.\nIII. M’nin yükseltgenmesiyle keton oluşur.\nBuna göre bu yargılardan hangileri doğrudur?',
  sekil=SK,istenen='Doğru olan yargılar.',ip=['Her alkolde –OH taşıyan karbonun kaç hidrojen taşıdığına bak.'],
  bilgi=[B('Alkollerin yükseltgenmesi','–OH taşıyan karbonda en az bir hidrojen varsa alkol yükseltgenir. Birincil alkol aldehit ve asit, ikincil alkol keton verir; üçüncül alkol yükseltgenmez. Örnek: 2-bütanol → 2-bütanon')],
  puf='–OH’nin bağlı olduğu karbondaki hidrojen sayısı yükseltgenmenin ürününü belirler.',dogru=o['dogru'],yan=o['yan'],sira=o['sira'])

# ================= 05 · dikloropropan sayısı · orta · şekil · sayısal =================
D5=tekil([g for m in monoklor(parse('CCC')) for g in monoklor(m)]); n5=len(D5); assert n5==4 and len(monoklor(parse('CCC')))==2
assert all(formul(g)==(3,6,0,2) for g in D5)
for s in ('ClC(Cl)CC','ClCC(Cl)C','ClCCCCl','CC(Cl)(Cl)C'): assert any(ayni(parse(s),g) for g in D5),s
assert len(list(combinations(range(3),2)))+3==6
SK=tk(satirlar([[('m','CCC'),('+',),('y','2Cl$_2$'),('->','ışık','',1.6),('kutu','?'),('+',),('y','2HCl'),('y','  ')]],bosluk=0.5))
Q('0005','yer','orta','şekilli','Alkanın çok klorlanması','Propanın iki hidrojeninin klorla yer değiştirmesiyle oluşan yapı izomerlerini sayar.',
  'Alkanda iki hidrojenin klorla yer değiştirmesinde simetriyle özdeş olanlar bir sayılır; iki klor aynı karbonda ya da farklı karbonlarda bulunabilir.','Simetrik yapıları ayrı bileşik saymak ya da aynı karbonda iki klor olan yapıyı unutmak.','dikloropropan izomerleri',
  [A('Hidrojen ortamlarını bul','Propanda uç karbonlar özdeş, ortadaki karbon farklıdır.','CH₃ (6 H) · CH₂ (2 H)'),
   A('Aynı karbonda iki klor','Uç karbonda ya da ortadaki karbonda iki klor bulunabilir.','1,1-diklor · 2,2-diklor'),
   A('Farklı karbonlarda iki klor','Komşu karbonlar ve uçtaki iki karbon seçilebilir; komşu uç–orta seçimi simetriyle tek bileşik verir.','1,2-diklor · 1,3-diklor'),
   A('Say','Dört farklı yapı vardır; 1,1 ile 3,3 ve 1,2 ile 2,3 özdeştir.','4 bileşik')],
  metin='Şekilde propanın ışık altında yeterli miktarda Cl₂ ile tepkimesi gösterilmiştir. Tepkimede iki hidrojen atomu iki klor atomuyla yer değiştirmektedir.\nBuna göre C₃H₆Cl₂ formülüne sahip kaç farklı organik bileşik oluşabilir?',
  sekil=SK,istenen='Oluşabilecek farklı bileşik sayısı.',ip=['Önce iki klorun aynı karbonda olduğu yapıları, sonra farklı karbonlarda olduğu yapıları ayrı ayrı yaz ve simetrik olanları ele.'],
  bilgi=[B('Alkanlarda yer değiştirme','Alkanlar ışık altında halojenle yer değiştirme tepkimesi verir; her adımda bir hidrojen halojenle yer değiştirir ve HX oluşur. Simetri eksenine göre özdeş olan konumlar tek ürün verir. Örnek: etanın iki klorlanmasıyla 1,1- ve 1,2-dikloroetan oluşur')],
  puf='İki klorun konum çiftlerini yazarken simetri nedeniyle özdeş olanları ele.',dogru=4,
  yan=[(2,'Yalnız monoklorlu ürün sayısını (1-kloro ve 2-kloro) bulmuştur; ikinci hidrojenin yer değiştirmesini hesaba katmamıştır.','dikkat'),
       (3,'1,1-, 1,2- ve 1,3-dikloropropanı sayıp aynı karbonda iki klor taşıyan 2,2-dikloropropanı unutmuştur.','bilgi'),
       (5,'1,2-dikloropropanı CH₂Cl–CHCl–CH₃ ve CH₃–CHCl–CH₂Cl olarak iki ayrı bileşik saymıştır; oysa bunlar özdeştir.','bilgi'),
       (6,'Konum çiftlerini (1,1)(1,2)(1,3)(2,2)(2,3)(3,3) diye sıralamış; simetri nedeniyle (3,3) = (1,1) ve (2,3) = (1,2) olduğunu hesaba katmamıştır.','islem')])

# ================= 06 · zincir: etan → eten → dibromoetan · orta · şekil · olumsuz kök =================
A6=monoklor(parse('CC')); assert len(A6)==1 and ayni(A6[0],parse('CCCl'))
B6=ayrilma(A6[0],'Cl'); assert len(B6)==1 and ayni(B6[0],parse('C=C'))
C6=X2_ekle(B6[0],'Br'); assert ayni(C6,parse('BrCCBr'))
o6=tek([('1. basamakta bir hidrojen atomu klor atomuyla yer değiştirir.',True,'etanın ışıkta klorlanması yer değiştirme tepkimesidir'),
        ('A bileşiğinin adı kloroetandır.',True,'1. basamakta oluşan ürün C₂H₅Cl’dür'),
        ('2. basamakta HCl ayrılarak çift bağ oluşur.',True,'alkollü KOH ile ayrılma tepkimesi gerçekleşir ve eten oluşur'),
        ('C bileşiğinin adı 1,2-dibromoetandır.',True,'eten Br₂ ile katılma tepkimesi verir ve iki brom komşu karbonlara bağlanır'),
        ('3. basamakta B bileşiğinin bir hidrojen atomu brom atomuyla yer değiştirir.',False,'3. basamak bir katılma tepkimesidir; B’nin çift bağı açılır ve Br₂ tek ürün verecek biçimde katılır')],False,'bilgi')
sira6=['1. basamakta bir hidrojen atomu klor atomuyla yer değiştirir.','A bileşiğinin adı kloroetandır.','2. basamakta HCl ayrılarak çift bağ oluşur.','C bileşiğinin adı 1,2-dibromoetandır.','3. basamakta B bileşiğinin bir hidrojen atomu brom atomuyla yer değiştirir.']
SK=tk(satirlar([[('m','CC'),('->','Cl$_2$ / ışık','(1)',2.4),('kutu','A'),('->','alkollü KOH','(2)',2.6),('kutu','B')],[('kutu','B'),('->','Br$_2$','(3)',2.0),('kutu','C')]],bosluk=0.5))
Q('0006','zin','orta','şekilli','Tepkime zinciri (etan → eten → dibromoetan)','Yer değiştirme, ayrılma ve katılma basamaklarını art arda izleyip yargıların yanlışını bulur.',
  'Alkan ışıkta halojenle yer değiştirir; alkil halojenür alkollü KOH ile alkene dönüşür (ayrılma); alken halojenle katılma verir.','Katılma ile yer değiştirme tepkimelerini karıştırmak.','etan → kloroetan → eten → 1,2-dibromoetan',
  [A('A’yı bul','Etanın klorlanması yer değiştirmedir.','A: CH₃CH₂Cl'),A('B’yi bul','Alkollü KOH ile HCl ayrılır, çift bağ oluşur.','B: CH₂=CH₂'),
   A('C’yi bul','Çift bağa Br₂ katılır.','C: CH₂Br–CH₂Br'),A('Yargıları ele','Üçüncü basamakta çift bağ açıldığından tepkime katılmadır; yer değiştirme diyen ifade yanlıştır.','Yanlış olan: son ifade')],
  metin='Şekilde etan ile başlayan bir tepkime zinciri gösterilmiştir.\nBuna göre bu zincirle ilgili aşağıdakilerden hangisi yanlıştır?',
  sekil=SK,istenen='Yanlış olan ifade.',ip=['Zincirdeki her okta çoklu bağın oluşup oluşmadığına ya da açılıp açılmadığına bak.'],
  bilgi=[B('Alkil halojenürlerin tepkimeleri','Alkollü KOH ile ısıtılan alkil halojenürden HX ayrılır ve alken oluşur. Sulu NaOH ile halojen –OH ile yer değiştirir. Alkenler halojenle katılma tepkimesi verir. Örnek: bromoetan + alkollü KOH → eten + KBr + H₂O')],
  puf='Çoklu bağ oluşuyorsa ayrılma, çoklu bağ açılıyorsa katılma, bir atom başkasının yerini alıyorsa yer değiştirmedir.',dogru=o6['dogru'],yan=o6['yan'],sira=sira6)

# ================= 07 · Br2 grafiği · orta · grafik =================
n0=Fr(2,5)
gK=[(0,0.4),(0.4,0.0),(0.5,0.0)]; gL=[(0,0.4),(0.2,0.0),(0.5,0.0)]; gM=[(0,0.4),(0.5,0.4)]
assert Fr(2,5)/1==Fr(2,5) and Fr(2,5)/2==Fr(1,5)
SK=pg('width=7.2cm,height=5.2cm,axis lines=left,xmin=0,xmax=0.5,ymin=0,ymax=0.5,xtick={0,0.1,0.2,0.3,0.4,0.5},ytick={0,0.1,0.2,0.3,0.4,0.5},grid=major,major grid style={gray!45,thin},xlabel={Geçirilen gaz (mol)},ylabel={Br$_2$ (mol)},label style={font=\\small},tick label style={font=\\small},/pgf/number format/use comma',
 f'\\addplot[thick,color=blue!70!black] coordinates {{{co(gK)}}};\n\\addplot[thick,dashed,color=red!70!black] coordinates {{{co(gL)}}};\n\\addplot[thick,dotted,color=green!45!black] coordinates {{{co(gM)}}};\n'
 '\\node[font=\\small\\bfseries,anchor=south west] at (axis cs:0.3,0.12) {K};\n\\node[font=\\small\\bfseries,anchor=south west] at (axis cs:0.03,0.1) {L};\n\\node[font=\\small\\bfseries,anchor=south] at (axis cs:0.25,0.42) {M};')
o7=dict(dogru='K: propen · L: propin · M: propan',yan=[
 ('K: propin · L: propen · M: propan','K’nin 0,4 mol gazla, L’nin 0,2 mol gazla bitmesi K’nin 1, L’nin 2 mol Br₂ harcadığını gösterir; bu seçenekte sıra ters yazılmıştır.','dikkat'),
 ('K: propen · L: propan · M: propin','Propan Br₂ ile tepkime vermez; Br₂ miktarı değişmeyen M propandır, L ise Br₂ harcayan bir bileşik olmalıdır.','bilgi'),
 ('K: propan · L: propen · M: propin','Propan ve propen ile propin sıralaması grafikle uyuşmaz; yatay çizgi Br₂ harcamayan bileşiği, yani propanı gösterir.','bilgi'),
 ('K: 1,3-bütadien · L: propen · M: propan','1,3-bütadien iki π bağlıdır; Br₂ ile 1 : 2 harcar ve eğrisi L gibi daha dik olurdu. K’nin eğimi bir π bağına uygundur.','bilgi')])
for nm,s,p in (('propen','C=CC',1),('propin','C#CC',2),('propan','CCC',0),('butadien','C=CC=C',2)): assert sum(parse(s)[a][b]['o']-1 for a,b in parse(s).edges)==p
Q('0007','kat','orta','grafik','Br₂ ile katılma grafiği','Br₂ harcanma grafiğinden bileşiklerin π bağ sayısını çıkarır.',
  'Grafikte Br₂ ne kadar hızlı biterse bileşiğin π bağı o kadar çoktur; Br₂ miktarı değişmiyorsa bileşik doymuştur.','Eğimi bileşiğin molekül kütlesiyle ilişkilendirmek.','Br₂ harcanması',
  [A('Br₂ harcayanları ayır','Yatay çizgi Br₂ ile tepkime vermeyen doymuş bileşiği gösterir.','M doymuş'),
   A('Eğimleri karşılaştır','K’de 0,4 mol Br₂ 0,4 mol gazla, L’de 0,2 mol gazla biter.','K: 1 mol Br₂/mol · L: 2 mol Br₂/mol'),
   A('Bileşikleri eşleştir','K bir π bağlı, L iki π bağlı, M doymuştur.','K alken · L alkin · M alkan')],
  metin='Üç özdeş kapta 0,4 mol Br₂ içeren çözeltiye K, L ve M gazları ayrı ayrı geçiriliyor. Br₂ mol sayısının geçirilen gaz miktarına göre değişimi grafikte verilmiştir. Gazlar propan, propen ve propin bileşiklerinden birer tanesidir.\nBuna göre K, L ve M gazları aşağıdakilerden hangisinde doğru verilmiştir?',
  sekil=SK,istenen='K, L ve M’nin doğru eşleşmesi.',ip=['Eğrilerin Br₂ mol sayısını sıfıra indirdiği gaz miktarını bir π bağının harcadığı Br₂ ile ilişkilendir.'],
  bilgi=[B('Br₂ ile katılma','Br₂ çözeltisi doymamış hidrokarbonlara katılır ve rengi açılır; çift bağ başına 1, üçlü bağ başına 2 mol Br₂ harcanır. Alkanlar karanlıkta Br₂ ile tepkime vermez. Örnek: 1 mol 2-bütin 2 mol Br₂ harcar')],
  puf='Br₂ ne kadar çabuk bitiyorsa molekülde o kadar çok π bağı vardır.',dogru=o7['dogru'],yan=o7['yan'],sira=['K: propin · L: propen · M: propan','K: propen · L: propan · M: propin','K: propan · L: propen · M: propin','K: 1,3-bütadien · L: propen · M: propan','K: propen · L: propin · M: propan'])

# ================= 08 · karışım: H2 + Br2 + toplam · zor · tablo =================
a_,b_,c_=Fr(1,10),Fr(3,10),Fr(1,5)
tot=Fr(3,5); h2n=2*a_+b_; mg=26*a_+28*b_; assert tot==a_+b_+c_ and h2n==Fr(1,2) and mg==11 and Fr(tot*224,10)==Fr('13.44')
# çözüm: 2a+b=1/2 ; 26a+28b=11 -> b=1/2-2a
aa=Fr(11-14,26-56); bb=Fr(1,2)-2*aa; cc=tot-aa-bb; assert (aa,bb,cc)==(a_,b_,c_)
mc=cc*30; assert mc==6
vals8=[cc*30,(tot-bb)*30,(tot-aa)*30,(tot-2*aa)*30,(tot-Fr(1,2))*30]
assert vals8==[6,9,15,12,3] and len(set(vals8))==5
SK=tablo_svg(['Deney','Veri'],[['Karışım: C₂H₂, C₂H₄, C₂H₆','13,44 L (NŞA)'],['Ni ile tamamen doyurma','0,5 mol H₂ harcandı'],['Br₂ çözeltisinden geçirme','Kütle artışı 11 g']])
Q('0008','hes','zor','tablo','Üçlü gaz karışımı bileşimi','Doyurma ve Br₂ deneylerinin verilerinden üç bileşenli karışımın bileşimini çözer.',
  'Toplam mol, harcanan H₂ molü (üçlü bağ 2, çift bağ 1) ve Br₂ çözeltisinin kütle artışı (doymamışların kütlesi) üç denklem verir; doymuş bileşenin molü toplamdan kalan kısımdır.','Üçlü bağı tek π bağı saymak; kütle artışını yalnız etene yazmak.','C₂H₂, C₂H₄, C₂H₆ karışımı',
  [A('Toplam molü bul','NŞA’da 22,4 L bir mol gazdır.','13,44 ÷ 22,4 = 0,6 mol'),
   A('H₂ denklemini kur','C₂H₂ iki, C₂H₄ bir mol H₂ harcar.','2a + b = 0,5'),
   A('Kütle denklemini kur','Br₂ çözeltisinin kütlesi doymamış gazların kütlesi kadar artar.','26a + 28b = 11'),
   A('Çöz','b = 0,5 − 2a değerini kütle denkleminde yazınca a ve b bulunur.','a = 0,1 mol · b = 0,3 mol'),
   A('Etanı bul','Toplamdan doymamışlar çıkarılır ve mol kütlesiyle çarpılır.','(0,6 − 0,4) × 30 = 6 g')],
  metin='Etin (C₂H₂), eten (C₂H₄) ve etan (C₂H₆) gazlarından oluşan bir karışımla yapılan deneylerin verileri tabloda verilmiştir (H: 1, C: 12 g/mol).\nBuna göre karışımdaki etanın kütlesi kaç gramdır?',
  sekil=SK,istenen='Karışımdaki etanın kütlesi (g).',ip=['Etin ve eten için mol sayılarını bilinmeyen alıp H₂ harcanması ve kütle artışından iki denklem yaz.'],
  bilgi=[B('Karışım hesabı','Karışımdaki bileşenlerin mollerini bilinmeyen alıp her deneyden bir denklem yazılır. H₂ ya da Br₂ yalnız doymamış bileşenlere katılır; Br₂ çözeltisinin kütle artışı katılan gazın kütlesine eşittir. Örnek: 0,2 mol C₃H₆ geçirilince kütle 8,4 g artar')],
  puf='Üç bilinmeyen için üç veri: toplam mol, H₂ molü ve kütle artışı.',dogru=cc*30,
  yan=[(Fr(9),'Etanı toplam moldan yalnız eteni çıkararak bulmuştur (0,6 − 0,3 = 0,3 mol); etin molünü unutmuştur.','dikkat'),
       (Fr(15),'Etanı toplam moldan yalnız etini çıkararak bulmuştur (0,6 − 0,1 = 0,5 mol); eten molünü hesaba katmamıştır.','dikkat'),
       (Fr(12),'Etinin mol sayısı yerine harcadığı H₂ molünü (0,2) çıkarmıştır; (0,6 − 0,2) × 30 işlemi 12 verir.','islem'),
       (Fr(3),'Etinin de bir π bağı varmış gibi a + b = 0,5 almış; etan molünü 0,1 bulup 3 g yazmıştır.','bilgi')])

# ================= 09 · ester yapı belirleme · zor · öncüllü · şekil =================
ESL=[g for g in uret(4,2,0,1) if sinifla(g)=={'ester'}]; assert len(ESL)==4
UYAN=[]
for E in ESL:
    Y,Z=hidroliz(E); r=yukseltgen(Y)
    if r is not None and sinifla(r)=={'aldehit'} and (lambda t: t is not None and ayni(t,Z))(aldehit_asit(r)): UYAN.append((E,Y,Z))
assert len(UYAN)==1 and ayni(UYAN[0][0],parse('CC(=O)OCC')) and ayni(UYAN[0][1],parse('CCO')) and ayni(UYAN[0][2],parse('CC(=O)O'))
BA=parse('CCCC(=O)O'); assert formul(BA)==formul(UYAN[0][0]) and sinifla(BA)=={'asit'}
assert not ayni(UYAN[0][0],parse('CCC(=O)OC'))
d=dict(I=(False,'X etil etanoattır; metil propanoat, hidrolizinde metanol ve propanoik asit verirdi ve metanolün yükseltgenme ürünü propanoik asit değildir'),
       II=(True,'Y birincil alkol (etanol) olduğundan yükseltgenmesinde ara ürün olarak aldehit (etanal) oluşur'),
       III=(True,'X ile bütanoik asit C₄H₈O₂ formüllüdür ve ester ile karboksilik asit farklı fonksiyonel gruplardır'))
o=OC(d,sr('Yalnız I','Yalnız III','I ve II','II ve III','I, II ve III')); assert o['dogru']=='II ve III'
SK=tk(satirlar([[('kutu','X'),('+',),('y','H$_2$O'),('->','H$^+$','',1.8),('kutu','Y'),('+',),('kutu','Z')],[('kutu','Y'),('->','yükseltgenme','',2.6),('kutu','Z')]],bosluk=0.5))
Q('0009','zin','zor','şekilli','Ester yapısını bulma ve yükseltgenme','Esterin hidroliz ürünlerinin yükseltgenme ilişkisinden esterin yapısını bulur ve yargıları yorumlar.',
  'Esterin hidrolizinde asit ve alkol oluşur; alkol yükseltgenince aynı asit çıkıyorsa ikisinin karbon sayısı eşittir, ester formülündeki karbonlar iki eşit parçaya bölünür.','Alkolü yükseltgenince oluşan asidi hidrolizdeki asitten farklı sanmak.','C₄H₈O₂ esteri',
  [A('Formül bilgisini kullan','X, C₄H₈O₂ formüllü bir esterdir; hidroliz ürünleri Y (alkol) ve Z (asit).','X: C₄H₈O₂'),
   A('Y ve Z’yi ilişkilendir','Y’nin yükseltgenmesiyle Z oluşuyorsa Y ve Z aynı sayıda karbona sahiptir.','Karbon sayısı: 2 + 2'),
   A('X’i yaz','İki karbonlu asit ve iki karbonlu alkolün esteri etil etanoattır.','CH₃COOC₂H₅'),
   A('Yargıları değerlendir','Y etanoldür; birincil alkol olduğundan yükseltgenme sırasında aldehit oluşur. Bütanoik asit X ile aynı formüllü ama farklı gruplu bir bileşiktir.','II ve III doğru')],
  metin='Şekilde C₄H₈O₂ formüllü X esterinin asit katalizörlüğünde suyla tepkimesi ve Y bileşiğinin yükseltgenmesi gösterilmiştir. Y alkol, Z karboksilik asittir; Y’nin yükseltgenmesiyle Z oluşmaktadır.\nI. X bileşiğinin adı metil propanoattır.\nII. Y’nin yükseltgenmesi sırasında ara ürün olarak aldehit oluşur.\nIII. X ile bütanoik asit birbirinin fonksiyonel grup izomeridir.\nBuna göre bu yargılardan hangileri doğrudur?',
  sekil=SK,istenen='Doğru olan yargılar.',ip=['Y’nin yükseltgenme ürünü Z ise Y ile Z’nin karbon sayıları arasında nasıl bir ilişki olması gerektiğini düşün.'],
  bilgi=[B('Esterin hidrolizi','Ester, asit katalizörlüğünde su ile tepkimeye girerek kendisini oluşturan karboksilik asit ve alkole ayrılır. Asit kısmı C=O taşıyan, alkol kısmı oksijene bağlı alkil grubu olan taraftır. Örnek: propil metanoat → metanoik asit + 1-propanol')],
  puf='Alkol ve asit aynı karbon iskeletine sahipse ester iki eşit karbon yarısından oluşur.',dogru=o['dogru'],yan=o['yan'],sira=o['sira'])

# ================= 10 · C4H10O izomerleri · zor · öncüllü · düz =================
IZ=uret(4,1,0,0); assert len(IZ)==7
alk=[g for g in IZ if sinifla(g)=={'alkol'}]; ete=[g for g in IZ if sinifla(g)=={'eter'}]; assert (len(alk),len(ete))==(4,3)
yuk=[g for g in IZ if yukseltgen(g) is not None]; assert len(yuk)==3
ald=[g for g in yuk if sinifla(yukseltgen(g))=={'aldehit'}]; ket=[g for g in yuk if sinifla(yukseltgen(g))=={'keton'}]; assert (len(ald),len(ket))==(2,1)
assert len(IZ)-len(yuk)==4
d=dict(I=(True,'Dört alkol ve üç eter olmak üzere yedi açık zincirli yapı izomeri vardır'),
       II=(False,'Aldehit veren izomerler yalnız 1-bütanol ve 2-metil-1-propanoldür, yani iki tanedir; 2-bütanol keton verir'),
       III=(True,'Üç eter ve üçüncül alkol (2-metil-2-propanol) yükseltgenmez; yükseltgenemeyen izomer sayısı dörttür'))
o=OC(d,sr('Yalnız I','Yalnız II','I ve II','I ve III','II ve III')); assert o['dogru']=='I ve III'
Q('0010','yuk','zor','öncüllü','C₄H₁₀O izomerleri ve yükseltgenme','Bir molekül formülüne ait alkol ve eter izomerlerini sayıp yükseltgenme davranışlarını karşılaştırır.',
  'C₄H₁₀O için dört alkol ve üç eter yazılır; yalnız –OH taşıyan karbonunda hidrojen bulunan alkoller yükseltgenir (birincil: aldehit, ikincil: keton).','Eterleri ya da üçüncül alkolü yükseltgenebilir saymak; yapı izomerlerini eksik yazmak.','C₄H₁₀O izomerleri',
  [A('İzomerleri yaz','Dört karbonlu dört alkol ve üç eter yazılır.','4 alkol + 3 eter = 7'),
   A('Yükseltgenenleri ayır','İki birincil ve bir ikincil alkol yükseltgenir; üçüncül alkol ve eterler yükseltgenmez.','Yükseltgenen: 3 · yükseltgenmeyen: 4'),
   A('Ürünleri say','Birincil alkoller aldehit, ikincil alkol keton verir.','Aldehit: 2 · keton: 1'),
   A('Yargıları değerlendir','I ve III doğru, II yanlıştır.','I ve III')],
  metin='C₄H₁₀O molekül formülüne sahip, açık zincirli (halkasız) ve yalnız tek bağ içeren bütün yapı izomerleri ile ilgili,\nI. Toplam yedi farklı yapı izomeri vardır.\nII. Yükseltgenme sonucu aldehit veren üç izomer vardır.\nIII. Yükseltgenme koşullarında tepkime vermeyen dört izomer vardır.\nyargılarından hangileri doğrudur?',
  sekil=None,istenen='Doğru olan yargılar.',ip=['Önce alkol ve eter izomerlerini ayrı ayrı yaz, sonra her birinin –OH taşıyan karbonundaki hidrojen sayısını incele.'],
  bilgi=[B('Yapı izomerlerini sayma','Önce fonksiyonel grup türüne, sonra karbon iskeletine göre sistematik yaz; aynı bileşiği iki kez yazmamak için bağlanma sırasını karşılaştır. Örnek: C₃H₈O için iki alkol ve bir eter yazılabilir')],
  puf='İzomerleri grup türüne ve karbon iskeletine göre sırayla yaz; yükseltgenmeyi –OH taşıyan karbondaki hidrojen sayısı belirler.',dogru=o['dogru'],yan=o['yan'],sira=o['sira'])

# ================= yaz =================
for x in P.ANA: x['kardes']=None
SCR='/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/otiki'; os.makedirs(SCR,exist_ok=True)
P.yaz(os.path.join(GD,'orgtepkimeiki-1.json'),os.path.join(SCR,'bos-orgtepkimeiki.json'))
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=KEY))['kartlar'].append(c['id'])
json.dump(dict(konu=KONU_AD,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2018–2026 Kimya (yalnız mantık), MEB 12. sınıf Organik Bileşikler.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','akorgtepkimeiki.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
for q in P.ANA: print(q['id'][-4:],q['zorluk'] if 'zorluk' in q else '',q['cevap'])
