"""AYT Kimya · Organik Tepkimeler ve İzomeri · 20 soru. Kardeş yok, ipucu 1.
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
P=Parti('orgtepkime',KONU_AD,KEY,ders='AYT Kimya',idon='aytkim'); H.KONU=KONU_AD
KAYNAK='ÖSYM AYT 2018–2026 Kimya organik tepkime ve izomeri soruları (yalnız mantık) · MEB 12. sınıf Organik Bileşikler'
def kartla(no,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(f'K-AKORGT-{no}',alt,fikir,tuzak,z,kalip,adim,tipId,tip,KAYNAK)
TIP={'sinif':('ot-sinif','Tepkime türünü belirleme'),'kat':('ot-katilma','Katılma tepkimeleri'),'yer':('ot-yerdegistirme','Yer değiştirme tepkimeleri'),
     'ayr':('ot-ayrilma','Ayrılma tepkimeleri'),'yuk':('ot-yukseltgenme','Yükseltgenme ve indirgenme'),'kon':('ot-kondenzasyon','Kondenzasyon (ester oluşumu)'),
     'izo':('ot-izomer','Yapı, geometrik ve fonksiyonel grup izomerliği'),'hes':('ot-hesap','Organik tepkimelerde mol ve kütle hesabı'),'zin':('ot-zincir','Tepkime zincirleri')}
def Q(no,tp,z,kalip,alt,kaz,fikir,tuzak,ozet,ad,**k):
    t,tn=TIP[tp]; kartla(no[-2:],alt,fikir,tuzak,z,kalip,len(ad),t,tn)
    assert len(k['ip'])==1; mk(P,no,ad=ad,adim=len(ad),tipId=t,tip=tn,z=z,alt=alt,kaz=kaz,kalip=kalip,kart=f'K-AKORGT-{no[-2:]} ({ozet})',**k)
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

# ================= 01 · tepkime türü · kolay · tablo · olumsuz kök =================
G_=parse('CC'); assert ayni(monoklor(G_)[0],parse('CCCl'))                      # II: yer değiştirme
assert ayni(X2_ekle(parse('C=C'),'Br'),parse('BrCCBr'))                           # I: katılma
assert ayni(parse('C#C'),parse('C#C'))
assert ayni(HX_ekle(parse('C=CC'),'Br')[0],parse('CC(C)Br'))                     # V
assert ayni(H2O_ekle(parse('C=CC'))[0],parse('CC(C)O'))                          # IV
SK=tablo_svg(['No','Tepkime'],[['I','CH₃–CH₃ + Cl₂ → CH₃–CH₂Cl + HCl'],['II','CH₂=CH₂ + Br₂ → CH₂Br–CH₂Br'],['III','CH≡CH + H₂ → CH₂=CH₂'],
    ['IV','CH₃–CH=CH₂ + H₂O → CH₃–CH(OH)–CH₃'],['V','CH₃–CH=CH₂ + HBr → CH₃–CHBr–CH₃']])
S1=[('I',False,'bir hidrojen atomu klor atomuyla yer değiştirir ve iki ürün (organik ürün ile HCl) oluşur'),
    ('II',True,'çift bağ açılır ve Br₂ tek ürün verecek biçimde katılır'),('III',True,'üçlü bağ çift bağa dönüşürken H₂ katılır'),
    ('IV',True,'çift bağ açılır ve su tek ürün verecek biçimde katılır'),('V',True,'çift bağ açılır ve HBr tek ürün verecek biçimde katılır')]
yan=[(s,f'{s} numaralı tepkimeyi katılma dışı sanmış; oysa {n}, bu yüzden katılma tepkimesidir.','bilgi') for s,b,n in S1 if b]
Q('0001','sinif','kolay','tablo','Tepkime türleri','Giren ve ürün formüllerinden katılma ile yer değiştirme tepkimesini ayırt eder.',
  'Katılma tepkimesinde çoklu bağ açılır ve tek ürün oluşur; yer değiştirme tepkimesinde bir atom ya da grubun yerini başkası alır ve çoğunlukla iki ürün oluşur.','Alkanın halojenle tepkimesini de katılma sanmak.','tepkime türü tablosu',
  [A('Katılmayı tanı','Katılma tepkimesinde doymamış bileşiğin çoklu bağı açılır, giren maddelerin hepsi tek ürüne dönüşür.','Çoklu bağ açılır → tek ürün'),
   A('Girenlere bak','Beş tepkimenin dördünde çift ya da üçlü bağlı bir hidrokarbon vardır.','Doymuş hidrokarbon: yalnız bir tepkimede'),
   A('Ürünleri say','Doymuş girenli tepkimede iki ürün oluşur; biri HCl’dir, bu yer değiştirme izidir.','CH₃–CH₃ → CH₃–CH₂Cl + HCl'),
   A('Sonuç','Çoklu bağ açılmadığı için bu tepkime katılma değildir.','Katılma olmayan: I')],
  metin='Aşağıdaki tabloda bazı organik tepkimeler verilmiştir.\nBuna göre bu tepkimelerden hangisi katılma tepkimesi değildir?',
  sekil=SK,istenen='Katılma türünde olmayan tepkime.',ip=['Her tepkimede giren hidrokarbonun doymuş mu doymamış mı olduğuna ve kaç ürün oluştuğuna bak.'],
  bilgi=[B('Katılma ve yer değiştirme','Katılma: C=C ya da C≡C bağı açılır, tek ürün oluşur. Yer değiştirme: bir atom ya da grup başka bir atom ya da grupla yer değiştirir, iki ürün oluşur. Örnek: C₄H₈ + H₂ → C₄H₁₀ (katılma) · CH₄ + Br₂ → CH₃Br + HBr (yer değiştirme)')],
  puf='Girende çoklu bağ yoksa ve iki ürün çıkıyorsa tepkime katılma değil, yer değiştirmedir.',dogru='I',yan=yan,sira=['I','II','III','IV','V'])

# ================= 02 · HX katılması · kolay · şekil =================
ANA=HX_ekle(parse('C=CC'),'Br'); assert len(ANA)==1 and ayni(ANA[0],parse('CC(C)Br'))
assert not ayni(ANA[0],parse('CCCBr'))
assert ayni(X2_ekle(parse('C=CC'),'Br'),parse('BrCC(C)Br'))
assert ayni(H2_ekle(parse('C=CC')),parse('CCC'))
SK=tk(satirlar([[('m','C=CC'),('+',),('y','HBr'),('->',''),('kutu','?')]]))
o=dict(dogru='2-Bromopropan',yan=[('1,2-Dibromopropan','HBr katılmasında yalnız bir brom atomu bağlanır; iki brom atomlu ürün Br₂ katılmasıyla oluşurdu.','bilgi'),
 ('1-Bromopropan','Brom, Markovnikov kuralına göre hidrojeni az olan ikinci karbona bağlanır; uçtaki karbona bağlanan ürün ana ürün değildir.','bilgi'),
 ('3-Bromopropen','Bu bileşik çift bağı korunmuş bir yer değiştirme ürünüdür; oysa HBr çift bağa katılır.','bilgi'),
 ('Propan','Propan yalnız H₂ katılmasıyla oluşur; HBr katılmasında C–Br bağı da oluşur.','bilgi')])
Q('0002','kat','kolay','şekilli','Alkenlere HX katılması','Simetrik olmayan alkene HX katılmasında Markovnikov kuralını uygular.',
  'HX simetrik olmayan alkene katılırken hidrojen, çift bağdaki hidrojeni çok olan karbona; halojen hidrojeni az olan karbona bağlanır (Markovnikov).','Halojeni uçtaki karbona bağlamak.','HBr katılması',
  [A('Çift bağı bul','Propende çift bağ birinci ve ikinci karbonlar arasındadır.','CH₂=CH–CH₃'),A('Hidrojenleri say','Birinci karbonda iki, ikinci karbonda bir hidrojen vardır.','C1: 2 H · C2: 1 H'),
   A('Kuralı uygula','Brom, hidrojeni az olan ikinci karbona; hidrojen birinci karbona bağlanır.','CH₃–CHBr–CH₃'),A('Adlandır','Üç karbonlu zincirde brom ikinci karbondadır.','2-bromopropan')],
  metin='Şekilde propenin hidrojen bromür ile tepkimesi gösterilmiştir.\nBuna göre bu tepkimede oluşan ana ürünün adı aşağıdakilerden hangisidir?',
  sekil=SK,istenen='Ana ürünün adı.',ip=['Çift bağı oluşturan iki karbondan hangisinin daha çok hidrojen taşıdığına bak.'],
  bilgi=[B('Markovnikov kuralı','Simetrik olmayan alkene HX katıldığında X, çift bağdaki karbonlardan daha az hidrojen taşıyanına bağlanır. Örnek: 1-büten + HCl → 2-klorobütan (ana ürün)')],
  puf='HX katılmasında halojen, hidrojeni az olan karbona gider.',dogru=o['dogru'],yan=o['yan'],sira=['1-Bromopropan','1,2-Dibromopropan','3-Bromopropen','Propan','2-Bromopropan'])

# ================= 03 · ester oluşumu · kolay · şekil =================
ES=esterle(parse('CCC(=O)O'),parse('OC')); assert ayni(ES,parse('CCC(=O)OC')) and formul(ES)==(4,8,2,0)
assert sinifla(ES)=={'ester'}
assert ayni(parse('CC(=O)OCC'),parse('CC(=O)OCC')) and not ayni(parse('CC(=O)OCC'),ES) and formul(parse('CC(=O)OCC'))==formul(ES)
assert ayni(parse('CCCOC'),parse('CCCOC')) and sinifla(parse('CCCOC'))=={'eter'}
SK=tk(satirlar([[('m','CCC(=O)O'),('+',),('m','OC'),('->','H$^+$'),('kutu','X'),('+',),('y','H$_2$O')]]))
o=dict(dogru='Metil propanoat',yan=[('Etil etanoat','Bu ester etanoik asit ile etanolden oluşur; tepkimedeki asit üç karbonlu, alkol ise tek karbonludur.','bilgi'),
 ('Metil etanoat','Bu ester iki karbonlu asitten oluşur; tepkimedeki asit propanoik asit olduğundan asit kökü propanoattır.','bilgi'),
 ('Propil metanoat','Bu ester metanoik asit ile propanolden oluşur; tepkimedeki alkolün alkil grubu propil değil metildir.','bilgi'),
 ('1-Metoksipropan','Bu bileşik bir eterdir; asit ile alkolün tepkimesinde karbonil grubu korunur ve –COO– bağı kurulur, yani ester oluşur.','bilgi')])
Q('0003','kon','kolay','şekilli','Ester oluşumu','Karboksilik asit ve alkolden oluşan esteri adlandırır.',
  'Asit + alkol → ester + su; ester adı “alkolden gelen alkil grubu + asitten gelen kökün –oat’lı adı” biçimindedir.','Ester adında asit ve alkol bölümlerini karıştırmak.','asit ve alkolden ester',
  [A('Girenleri tanı','Soldaki bileşik –COOH taşıyan propanoik asit, ikincisi metanoldür.','CH₃CH₂COOH + CH₃OH'),A('Tepkimeyi yaz','Asidin –OH’si ile alkolün H’si su olarak ayrılır, kalan kısımlar birleşir.','CH₃CH₂COO–CH₃'),
   A('Adı kur','Alkolden gelen grup metil, asitten gelen kök propanoattır.','metil + propanoat'),A('Sonuç','Ürün metil propanoattır.','Metil propanoat')],
  metin='Şekilde propanoik asit ile metanolün asit katalizörlüğündeki tepkimesi gösterilmiştir. Tepkimede X organik bileşiği ile su oluşmaktadır.\nBuna göre X bileşiğinin adı aşağıdakilerden hangisidir?',
  sekil=SK,istenen='X bileşiğinin adı.',ip=['Alkolün bağlandığı alkil grubunu ve asitten gelen karbon zincirini ayrı ayrı belirle.'],
  bilgi=[B('Ester adlandırma','Ester, RCOOR′ biçimindedir: önce R′ (alkolden gelen alkil grubu), sonra RCOO– kökü (asidin adındaki –oik asit yerine –oat) yazılır. Örnek: pentanoik asit + etanol → etil pentanoat')],
  puf='Ester adı alkolden gelen alkille başlar, asitten gelen –oat ile biter.',dogru=o['dogru'],yan=o['yan'],sira=['Etil etanoat','1-Metoksipropan','Metil etanoat','Metil propanoat','Propil metanoat'])

# ================= 04 · izomer ilişkileri · orta · öncüllü · şekil =================
K_,L_,M_=parse('CC=CC'),parse('CC=CC'),parse('CC(C)=C')
ovK={3:-90}; assert cis_trans(K_,ovK)=='cis' and cis_trans(L_)=='trans'
assert ayni(K_,L_) and geo_cift(K_)==1 and not ayni(K_,M_) and formul(K_)==formul(M_)==(4,8,0,0) and geo_cift(M_)==0
d=dict(I=(True,'K ve L aynı atom bağlanma sırasına sahiptir; çift bağın aynı yanında ya da zıt yanında bulunan CH₃ grupları nedeniyle birbirinin geometrik izomeridir'),
       II=(True,'K ile M’nin molekül formülü aynı (C₄H₈), atomların bağlanma sırası farklıdır; bu yüzden yapı izomeridir'),
       III=(True,'L ile M’nin ikisi de C₄H₈ formülüne sahiptir'))
o=OC(d,sr('Yalnız I','I ve II','I ve III','II ve III','I, II ve III')); assert o['dogru']=='I, II ve III'
SK=tk(satirlar([[('m','CC=CC',ovK,'K'),('m','CC=CC',None,'L'),('m','CC(C)=C',None,'M')]],bosluk=1.3))
Q('0004','izo','orta','öncüllü','Yapı ve geometrik izomerlik','Aynı formüllü alkenlerin yapı ve geometrik izomer ilişkilerini ayırt eder.',
  'Aynı formül + farklı bağlanma sırası = yapı izomeri; aynı bağlanma sırası + çift bağa göre farklı konum = geometrik izomer.','Geometrik izomerleri yapı izomeri saymak ya da tersini düşünmek.','K, L, M alkenleri',
  [A('Formülleri yaz','Üç bileşiğin karbon ve hidrojen sayısını iskeletten bul.','K, L, M: C₄H₈'),A('Bağlanma sırasını karşılaştır','K ve L aynı iskelete sahip; M’de dallanma vardır.','K–L: aynı sıra · M: dallı'),
   A('K ve L’yi yorumla','Aynı sıra, çift bağa göre farklı konum geometrik izomerliktir.','I doğru'),A('M’yi yorumla','M, K ve L’den farklı bağlanmaya sahiptir ve formülleri aynıdır.','II ve III doğru')],
  metin='Şekilde iskelet formülleri verilen K, L ve M bileşikleri bir hidrokarbon türüne aittir.\nI. K ve L birbirinin geometrik (cis-trans) izomeridir.\nII. K ve M birbirinin yapı izomeridir.\nIII. L ve M aynı molekül formülüne sahiptir.\nBuna göre bu yargılardan hangileri doğrudur?',
  sekil=SK,istenen='Doğru olan yargılar.',ip=['Önce formülleri, sonra atomların bağlanma sırasını karşılaştır; çift bağa göre konum ayrı bir ölçüttür.'],
  bilgi=[B('İzomer türleri','Yapı izomerleri aynı molekül formülüne ama farklı atom bağlanma sırasına sahiptir. Geometrik izomerlerde bağlanma sırası aynıdır; çift bağın karbonlarındaki gruplar aynı yanda (cis) ya da zıt yanda (trans) bulunur. Örnek: 1-penten ve 2-penten yapı izomeridir; cis-2-penten ve trans-2-penten geometrik izomerdir')],
  puf='Önce formül, sonra bağlanma sırası: sıra farklıysa yapı, sıra aynı konum farklıysa geometrik izomerdir.',dogru=o['dogru'],yan=o['yan'],sira=o['sira'])

# ================= 05 · alkene katılma ürünleri · orta · öncüllü · şekil =================
X_=parse('CC=C(C)C')
ur1=H2_ekle(X_); assert ayni(ur1,parse('CCC(C)C'))
ur2=X2_ekle(X_,'Br'); assert ayni(ur2,parse('CC(Br)C(C)(C)Br'))
ur3=HX_ekle(X_,'Br'); assert len(ur3)==1 and ayni(ur3[0],parse('CCC(C)(C)Br')) and not ayni(ur3[0],parse('CC(Br)C(C)C'))
d=dict(I=(True,'X’in H₂ ile doyurulması 2-metilbütanı verir'),II=(True,'Br₂ çift bağdaki iki karbona katılır ve 2,3-dibromo-2-metilbütan oluşur'),
       III=(False,'HBr katılmasında brom, hidrojeni olmayan üçüncü karbona bağlanır; ana ürün 2-bromo-2-metilbütandır, 3-bromo-2-metilbütan değildir'))
o=OC(d,sr('Yalnız I','Yalnız II','Yalnız III','I ve II','I, II ve III')); assert o['dogru']=='I ve II'
SK=tk(satirlar([[('m','CC=C(C)C',None,'X')]]))
Q('0005','kat','orta','öncüllü','Alkenin katılma ürünleri','Bir alkenin H₂, Br₂ ve HBr ile katılma ürünlerini belirler.',
  'H₂ ve X₂ çift bağdaki iki karbona katılır; HX katılmasında halojen hidrojeni az olan karbona bağlanır.','HBr katılmasında ana ürünü Markovnikov kuralına göre değil, hidrojeni çok olan karbona X bağlayarak yazmak.','X alkeni',
  [A('X’i adlandır','Beş karbonlu ana zincirde ikinci karbonda metil, çift bağ ikinci ile üçüncü karbon arasında.','X: 2-metil-2-büten'),
   A('H₂ katılmasını yaz','Çift bağ tek bağa dönüşür, karbon iskeleti değişmez.','CH₃–CH₂–CH(CH₃)–CH₃'),
   A('Br₂ katılmasını yaz','Çift bağdaki iki karbona birer Br bağlanır.','CH₃–CHBr–CBr(CH₃)–CH₃'),
   A('HBr katılmasını yaz','Brom, hidrojeni olmayan karbona bağlanır.','CH₃–CH₂–CBr(CH₃)–CH₃')],
  metin='Şekilde iskelet formülü verilen X bileşiği ile ilgili,\nI. Ni katalizörlüğünde H₂ ile tepkimesinden 2-metilbütan oluşur.\nII. Br₂ ile tepkimesinden 2,3-dibromo-2-metilbütan oluşur.\nIII. HBr ile tepkimesinin ana ürünü 3-bromo-2-metilbütandır.\nBuna göre bu yargılardan hangileri doğrudur?',
  sekil=SK,istenen='Doğru olan yargılar.',ip=['Çift bağdaki iki karbonun hidrojen sayılarını karşılaştırıp her katılmada bağlanan atomların yerini ayrı ayrı belirle.'],
  bilgi=[B('Katılma ürünleri','H₂ (Ni) alkeni alkana çevirir. X₂ çift bağdaki iki karbona katılır. HX katılmasında X, hidrojeni az olan karbona bağlanır (Markovnikov). Örnek: propen + Br₂ → 1,2-dibromopropan')],
  puf='Doymuş ürün ve dihalojen ürünü iskeleti bozmaz; HX’te halojen hidrojeni az olan karbona gider.',dogru=o['dogru'],yan=o['yan'],sira=o['sira'])

# ================= 06 · alkan monoklorlama · orta · şekil =================
Ks,Ls,Ms=parse('CCCCC'),parse('CCC(C)C'),parse('CC(C)(C)C')
def orbit(G):
    ds=[]
    for v in G:
        if C_(G,v):
            H_=G.copy(); H_.nodes[v]['t']='C*'
            if not any(nx.is_isomorphic(H_,x,node_match=lambda a,b:a['t']==b['t'],edge_match=lambda a,b:a['o']==b['o']) for x in ds): ds.append(H_)
    return len(ds)
def gruptur(G): return len({nH(G,v) for v in G if C_(G,v) and nH(G,v)>0})
def hli(G): return sum(1 for v in G if C_(G,v) and nH(G,v)>0)
dg=[len(monoklor(g)) for g in (Ks,Ls,Ms)]; assert dg==[3,4,1]
e1=[hli(g) for g in (Ks,Ls,Ms)]; e2=[gruptur(g) for g in (Ks,Ls,Ms)]; e3=[orbit(g) for g in (Ks,Ls,Ms)]
assert e1==[5,5,4] and e2==[2,3,1] and e3==[3,4,2]
f=lambda L:' – '.join(map(str,L)); assert len({f(dg),f(e1),f(e2),f(e3),f(dg[::-1])})==5
SK=tk(satirlar([[('m','CCCCC',None,'K'),('m','CCC(C)C',None,'L'),('m','CC(C)(C)C',None,'M')]],bosluk=1.3))
Q('0006','yer','orta','şekilli','Alkanların halojenle yer değiştirmesi','Alkanın monoklorlanmasında farklı hidrojen ortamlarını sayarak ürün sayısını bulur.',
  'Ürün sayısı, hidrojen taşıyan karbonların molekül içindeki özdeş olmayan türlerinin sayısına eşittir.','Simetri ya da hidrojensiz karbonu hesaba katmamak.','K, L, M alkanları',
  [A('Simetriyi incele','Her alkanda özdeş karbonları simetri ekseniyle eşleştir.','Özdeş olanlar tek ürün verir'),
   A('K’yi say','Uçlardaki iki CH₃ özdeştir, ikinci ve dördüncü karbon özdeştir, ortadaki farklıdır.','K: 3 tür'),
   A('L ve M’yi say','L’de simetri yalnız iki CH₃ arasında; M’de dört CH₃ özdeştir ve ortadaki karbonda hidrojen yoktur.','L: 4 · M: 1'),
   A('Sonuç','Sayıları K, L, M sırasıyla yaz.','3 – 4 – 1')],
  metin='Şekilde iskelet formülleri verilen K, L ve M alkanları ışık altında yeterli Cl₂ ile ayrı ayrı tepkimeye sokuluyor. Her tepkimede yalnız bir hidrojen atomunun yerini bir klor atomu alıyor (stereoizomerler ayrı sayılmıyor).\nBuna göre K, L ve M’den oluşabilecek farklı monokloroalkan sayıları sırasıyla aşağıdakilerden hangisidir?',
  sekil=SK,istenen='K, L, M için farklı ürün sayıları.',ip=['Hidrojen taşıyan karbonlardan hangilerinin molekülde birbirine özdeş (simetrik) olduğuna bak.'],
  bilgi=[B('Yer değiştirme ve simetri','Alkan ışık altında halojenle tepkimeye girerken bir H atomu halojenle yer değiştirir. Özdeş (simetrik) karbonlardaki hidrojenler aynı ürünü verir. Örnek: propan 2 farklı monokloropropan verir (1-kloro ve 2-kloro)')],
  puf='Farklı ürün sayısı, simetriyle eşlenemeyen hidrojenli karbon türlerinin sayısıdır.',dogru=f(dg),
  yan=[(f(e1),'Hidrojen taşıyan her karbonu ayrı ürün saymış; simetriyle özdeş olanları birleştirmemiştir, bu da 5 – 5 – 4 değerini verir.','dikkat'),
       (f(e2),'Karbonları yalnız CH₃, CH₂ ve CH gruplarının türüne göre saymış; uçlardaki CH₃ gruplarının farklı ortamlarını ayırmamıştır, bu da 2 – 3 – 1 değerini verir.','bilgi'),
       (f(e3),'Hidrojeni olmayan karbonu da bir ürün kaynağı saymıştır; M’deki merkez karbon da sayılınca 3 – 4 – 2 çıkar.','bilgi'),
       (f(dg[::-1]),'Doğru sayıları bulmuş ama K, L, M sırasını ters yazmıştır, bu da 1 – 4 – 3 değerini verir.','dikkat')],
  sira=sorted([f(e1),f(e2),f(e3),f(dg[::-1])])+[f(dg)])

# ================= 07 · alkol dehidratasyonu · orta · öncüllü · şekil =================
AL={'K':'CCCO','L':'CC(C)O','M':'CC(C)CO','N':'CC(C)(C)O'}
UR={k:ayrilma(parse(v),'O') for k,v in AL.items()}
assert all(len(v)==1 for v in UR.values())
assert ayni(UR['K'][0],parse('C=CC')) and ayni(UR['L'][0],parse('C=CC')) and ayni(UR['M'][0],parse('C=C(C)C')) and ayni(UR['N'][0],parse('C=C(C)C'))
aynı=lambda a,b:ayni(UR[a][0],UR[b][0])
assert (aynı('K','N'),aynı('M','N'),aynı('L','M'))==(False,True,False)
d=dict(I=(aynı('K','N'),'K’nin ürünü propen (C₃H₆), N’nin ürünü 2-metilpropen (C₄H₈) olduğundan aynı alken oluşmaz'),
       II=(aynı('M','N'),'M ile N’nin dehidratasyonunda ikisi de 2-metilpropen verir'),
       III=(False,'L’nin ürünü propen, M’nin ürünü 2-metilpropendir; farklı karbon sayılı alkenler birbirinin geometrik izomeri olamaz'))
d['I']=(False,d['I'][1]); d['III']=(False,d['III'][1])
o=OC(d,sr('Yalnız II','Yalnız III','I ve II','I ve III','II ve III')); assert o['dogru']=='Yalnız II'
SK=tk(satirlar([[('m','CCCO',None,'K'),('m','CC(C)O',None,'L'),('m','CC(C)CO',None,'M'),('m','CC(C)(C)O',None,'N')]],bosluk=1.0))
Q('0007','ayr','orta','öncüllü','Alkollerin dehidratasyonu','Alkollerin ayrılma (su çıkışı) tepkimesinde oluşan alkenleri karşılaştırır.',
  'Alkol dehidratasyonunda –OH ile komşu karbondaki H su olarak ayrılır; farklı alkoller aynı alkeni verebilir.','Alkolün dehidratasyon ürününü alkolün adındaki karbon sayısına bakmadan eşleştirmek.','K, L, M, N alkolleri',
  [A('Ayrılmayı hatırla','–OH karbonu ile komşu karbondan H birlikte su olarak ayrılır, aralarında çift bağ oluşur.','R–CH₂–CH₂OH → R–CH=CH₂ + H₂O'),
   A('K ve L’yi çöz','İkisi de üç karbonlu iskelete sahiptir ve tek alken verir.','K, L → propen'),
   A('M ve N’yi çöz','İkisi de dört karbonlu, dallı iskelete sahiptir ve tek alken verir.','M, N → 2-metilpropen'),
   A('Yargıları değerlendir','Aynı alkeni veren çift M ile N’dir; karbon sayısı farklı ürünler birbirinin geometrik izomeri değildir.','Yalnız II doğru')],
  metin='Şekilde iskelet formülleri verilen K, L, M ve N alkolleri derişik H₂SO₄ eşliğinde ısıtılarak ayrılma (dehidratasyon) tepkimesine sokuluyor. Her alkolden yalnız bir çeşit alken oluşmaktadır.\nI. K ve N’den aynı alken oluşur.\nII. M ve N’den aynı alken oluşur.\nIII. L ve M’den oluşan alkenler birbirinin geometrik izomeridir.\nBuna göre bu yargılardan hangileri doğrudur?',
  sekil=SK,istenen='Doğru olan yargılar.',ip=['Her alkolde –OH’nin bağlı olduğu karbonu ve komşusundaki hidrojeni bulup oluşan alkenin iskeletini çiz.'],
  bilgi=[B('Dehidratasyon','Alkol, derişik H₂SO₄ ile yüksek sıcaklıkta ısıtıldığında –OH ve komşu karbondaki H su olarak ayrılır; alken oluşur. Örnek: 1-bütanol → 1-büten + H₂O')],
  puf='Dehidratasyonda karbon iskeleti değişmez; farklı alkoller aynı iskeletli alkeni verebilir.',dogru=o['dogru'],yan=o['yan'],sira=o['sira'])

# ================= 08 · indirgenme · orta · öncüllü · şekil =================
Kc,Lc=parse('CCC=O'),parse('CC(C)=O')
assert ayni(indirgen(Kc),parse('CCCO')) and ayni(indirgen(Lc),parse('CC(C)O'))
assert formul(indirgen(Kc))==formul(indirgen(Lc)) and not ayni(indirgen(Kc),indirgen(Lc))
assert sinifla(indirgen(Kc))=={'alkol'} and sinifla(indirgen(Lc))=={'alkol'}
d=dict(I=(False,'K bir aldehittir; indirgenmesinden birincil alkol olan 1-propanol oluşur, 2-propanol değil'),
       II=(True,'L bir ketondur; indirgenmesinden ikincil alkol olan 2-propanol oluşur'),
       III=(True,'1-propanol ile 2-propanol aynı formüle (C₃H₈O) sahip, bağlanması farklı yapı izomerleridir'))
o=OC(d,sr('Yalnız I','Yalnız II','I ve II','I ve III','II ve III')); assert o['dogru']=='II ve III'
SK=tk(satirlar([[('m','CCC=O',None,'K'),('m','CC(C)=O',None,'L'),('->','H$_2$ / Ni',''),('kutu','Ürünler')]],bosluk=1.2))
Q('0008','yuk','orta','öncüllü','Karbonil bileşiklerinin indirgenmesi','Aldehit ve ketonun indirgenme ürünlerini alkol sınıfı ve izomerlik yönünden değerlendirir.',
  'Aldehit indirgenince birincil, keton indirgenince ikincil alkol oluşur.','Ketonun indirgenmesiyle de birincil alkol oluştuğunu sanmak.','K, L karbonil bileşikleri',
  [A('Fonksiyonel grupları bul','K’de C=O karbonu bir karbona, L’de iki karbona bağlıdır.','K: aldehit · L: keton'),
   A('İndirgenmeyi uygula','C=O bağına H₂ katılır; karbonil karbonu –OH taşıyan karbon olur.','C=O → CH–OH'),
   A('Ürünleri yaz','K’den 1-propanol, L’den 2-propanol oluşur.','CH₃CH₂CH₂OH · CH₃CH(OH)CH₃'),
   A('Yargıları değerlendir','İki alkolün formülü aynı, bağlanma sırası farklıdır.','II ve III doğru')],
  metin='Şekilde iskelet formülleri verilen K ve L bileşikleri Ni katalizörlüğünde H₂ ile ayrı ayrı indirgeniyor.\nI. K’nin indirgenme ürünü 2-propanoldür.\nII. L’nin indirgenme ürünü 2-propanoldür.\nIII. K ve L’nin indirgenme ürünleri birbirinin yapı izomeridir.\nBuna göre bu yargılardan hangileri doğrudur?',
  sekil=SK,istenen='Doğru olan yargılar.',ip=['Karbonil karbonuna bağlı karbon sayısına göre iki bileşiğin fonksiyonel grubunu belirle, sonra indirgenme ürünlerinin yapılarını yaz.'],
  bilgi=[B('İndirgenme','Karbonil bileşiğine H₂ katılınca C=O bağı C–OH’ye dönüşür: aldehit → birincil alkol, keton → ikincil alkol. Örnek: bütanal → 1-bütanol')],
  puf='Aldehit birincil, keton ikincil alkole indirgenir; ürünlerin formülü giren ile aynı sayıda karbon taşır.',dogru=o['dogru'],yan=o['yan'],sira=o['sira'])

# ================= 09 · ester verim · zor · tablo =================
mA,mE,mS,mH=Fr(60),Fr(46),Fr(88),Fr(18); gA,gE=Fr(12),Fr(138,10); verim=Fr(75,100)
assert mA==2*12+4+32 and mE==2*12+6+16 and mS==4*12+8+32 and mH==18
nA,nE=gA/mA,gE/mE; assert (nA,nE)==(Fr(1,5),Fr(3,10)); n_s=min(nA,nE); dg9=n_s*verim*mS; assert dg9==Fr(132,10)
c1=n_s*mS; c2=nE*verim*mS; c3=n_s*verim*(mA+mE); c4=n_s*verim*(mS-mH)
assert len({dg9,c1,c2,c3,c4})==5
SK=tablo_svg(['Bileşik','Formül','Mol kütlesi (g/mol)','Konulan kütle (g)'],[['Etanoik asit','CH₃COOH','60','12'],['Etanol','C₂H₅OH','46','13,8'],['Etil etanoat','CH₃COOC₂H₅','88','–'],['Su','H₂O','18','–']])
Q('0009','hes','zor','tablo','Ester oluşumunda verim','Kondenzasyon tepkimesinde sınırlayıcı bileşen ve verimle ürün kütlesini bulur.',
  'Mol oranı 1:1:1:1 olan tepkimede sınırlayıcı bileşen ürün miktarını belirler; gerçek ürün, kuramsal ürünün verimle çarpımıdır.','Fazla bileşene göre hesap yapmak ya da verimi uygulamamak.','etanoik asit + etanol',
  [A('Denklemi yaz','Asit ile alkol 1 : 1 oranında ester ve su verir.','CH₃COOH + C₂H₅OH → CH₃COOC₂H₅ + H₂O'),
   A('Molleri bul','Konulan kütleleri mol kütlelerine böl.','Asit: 12 ÷ 60 = 0,2 mol · Etanol: 13,8 ÷ 46 = 0,3 mol'),
   A('Sınırlayıcıyı seç','Oran 1:1 olduğundan az olan mol ürün miktarını belirler.','Sınırlayıcı: asit, 0,2 mol'),
   A('Kuramsal ürün','0,2 mol ester oluşabilir.','0,2 × 88 = 17,6 g'),
   A('Verimi uygula','Gerçek kütle, kuramsal kütlenin %75’idir.','17,6 × 0,75 = 13,2 g')],
  metin='Etanoik asit ile etanolün asit katalizörlüğünde etil etanoat ve su oluşturduğu kondenzasyon tepkimesi için tabloda bazı veriler verilmiştir. Tepkime kabına tabloda belirtilen kütlelerde asit ve alkol konulmuştur.\nTepkime %75 verimle gerçekleştiğine göre oluşan etil etanoat kaç gramdır?',
  sekil=SK,istenen='Oluşan etil etanoatın kütlesi (g).',ip=['Önce iki girenin mol sayısını karşılaştırıp hangisinin tükeneceğine karar ver.'],
  bilgi=[B('Verim ve sınırlayıcı bileşen','Girenlerden önce biten sınırlayıcı bileşendir; ürünün kuramsal miktarını o belirler. Verim = gerçek ürün ÷ kuramsal ürün × 100. Örnek: kuramsal 40 g ürün, %50 verimle 20 g ürün verir')],
  puf='Sınırlayıcı bileşenle kuramsal ürünü bul, sonra verimle çarp.',dogru=dg9,
  yan=[(c1,'Verimi hesaba katmamış; 0,2 mol esterin kuramsal kütlesi olan 17,6 g değerini yazmıştır.','dikkat'),
       (c2,'Fazla olan etanole göre hesaplamış; 0,3 mol × 88 × 0,75 işlemi 19,8 g verir.','bilgi'),
       (c3,'Ürün kütlesini girenlerin mol kütleleri toplamından bulmuş, ayrılan suyu hesaba katmamıştır; 0,2 × 0,75 × 106 işlemi 15,9 g verir.','bilgi'),
       (c4,'Ester kütlesinden bir kez daha su kütlesini çıkarmıştır; 0,2 × 0,75 × 70 işlemi 10,5 g verir.','islem')])

# ================= 10 · cis-trans sayma · orta · şekil =================
CT={'K':'CC=CC','L':'C=CCC','M':'CC=C(C)C','N':'CC=CCC','P':'CC=CCl','Q':'C=C(C)C'}
GT={k:parse(v) for k,v in CT.items()}
gv={k:geo_cift(g)==1 for k,g in GT.items()}; assert gv=={'K':True,'L':False,'M':False,'N':True,'P':True,'Q':False}
def cbag(G):
    for a,b,d_ in G.edges(data=True):
        if d_['o']==2 and C_(G,a) and C_(G,b): return a,b
def her_uc_dolu(G):
    a,b=cbag(G); return all(len([w for w in G[u] if w!=v])>=1 for u,v in((a,b),(b,a)))
hc=lambda G: all(G.nodes[v]['t']=='C' for v in G)
dg10=sum(gv.values()); eA=len(GT); eB=sum(her_uc_dolu(g) for g in GT.values()); eC=sum(gv[k] and hc(GT[k]) for k in GT); eD=sum(gv[k] and not hc(GT[k]) for k in GT)
assert (dg10,eA,eB,eC,eD)==(3,6,4,2,1)
SK=tk(satirlar([[('m',CT['K'],None,'K'),('m',CT['L'],None,'L'),('m',CT['M'],None,'M')],[('m',CT['N'],None,'N'),('m',CT['P'],None,'P'),('m',CT['Q'],None,'Q')]],bosluk=1.2))
Q('0010','izo','orta','şekilli','Geometrik izomerlik koşulu','Çift bağın her karbonunda iki farklı grup bulunması koşulunu uygulayarak cis-trans izomerliğini sayar.',
  'Çift bağlı her karbonun bağlı olduğu iki grup birbirinden farklıysa bileşik cis-trans izomerliği gösterir.','Çift bağın bir karbonunda iki hidrojen ya da iki özdeş grup bulunmasını gözden kaçırmak.','K, L, M, N, P, Q alkenleri',
  [A('Koşulu hatırla','Cis-trans için çift bağın iki karbonunun her biri iki farklı atom ya da grup taşımalıdır.','Her uçta: farklı iki grup'),
   A('K, L, M’yi incele','K’nin her ucunda H ve CH₃ vardır; L’nin bir ucu CH₂, M’nin bir ucunda iki özdeş CH₃ bulunur.','K uygun · L, M uygun değil'),
   A('N, P, Q’yu incele','N ve P’nin her ucunda iki farklı grup vardır; Q’nun bir ucu CH₂’dir.','N, P uygun · Q uygun değil'),
   A('Say','Uygun olanlar K, N ve P’dir.','3')],
  metin='Şekilde iskelet formülleri verilen K, L, M, N, P ve Q bileşiklerinde çizimlerin cis ya da trans biçimde gösterilmiş olması dikkate alınmayacaktır.\nBuna göre bu bileşiklerden kaç tanesi cis-trans (geometrik) izomerliği gösterebilir?',
  sekil=SK,istenen='Geometrik izomeri olan bileşik sayısı.',ip=['Her çift bağın iki ucunda bağlı grupların birbirinden farklı olup olmadığını kontrol et.'],
  bilgi=[B('Cis-trans koşulu','Çift bağ etrafında dönme olmadığından, çift bağlı karbonların her biri iki farklı grup taşıyorsa iki geometrik izomer vardır. Örnek: 1-büten’de uçtaki karbon iki hidrojen taşıdığı için cis-trans izomeri yoktur')],
  puf='Bir uçta özdeş iki grup varsa geometrik izomerlik olmaz.',dogru=dg10,
  yan=[(eA,'Çift bağ içeren her bileşiği saymış; oysa uçlardaki gruplar farklı olmadıkça geometrik izomerlik olmaz.','bilgi'),
       (eB,'Çift bağlı her karbonda H dışında en az bir grup aranmış, uçlardaki grupların farklı olması koşulu atlanmıştır; bu yüzden M de sayılmıştır.','bilgi'),
       (eC,'Yalnız hidrokarbonları saymış; halojen içeren P bileşiğinde de iki uçtaki gruplar farklı olduğundan cis-trans vardır.','bilgi'),
       (eD,'Farklı atom (halojen) bulunmasını koşul sanmış ve yalnız P’yi saymıştır; farklı karbon grupları da yeterlidir.','bilgi')])

# ================= 11 · C5H10O2 asit-ester sayısı · orta · düz =================
L5=uret(5,2,0,1); a5=say(L5,'asit'); e5=say(L5,'ester'); assert (a5,e5)==(4,9)
fm5=sum(1 for g in L5 if sinifla(g)=={'ester'} and any(karbonil_O(g,c) and nH(g,c)==1 for c in g))
assert fm5==4
dg11=e5-a5; assert dg11==5; v11=[a5,e5,e5+a5,(e5-fm5)-a5]; assert len(set(v11+[dg11]))==5
Q('0011','izo','orta','düz','Fonksiyonel grup izomerliği (asit–ester)','Aynı formüllü karboksilik asit ve ester izomerlerini sistematik olarak sayar.',
  'Aynı molekül formülü karboksilik asit ve ester fonksiyonel gruplarını verebilir; her grup için ayrı ayrı karbon iskeletleri taranır.','Metanoat (HCOO–) esterlerini ya da dallı iskeletleri atlamak.','C₅H₁₀O₂ izomerleri',
  [A('Asitleri yaz','COOH, zincirin ucunda; geriye kalan dört karbonluk alkil grubunun 4 farklı yapısı vardır.','Bütil: 4 yapı → 4 asit'),
   A('Esterleri kurala göre grupla','Karbonil karbonuna bağlı grubun (H, CH₃, C₂H₅, C₃H₇) ve alkolden gelen grubun toplam karbon sayısı 4 olmalıdır.','Toplam alkil karbonu: 4'),
   A('Esterleri say','Alkil grubu sayıları: metanoatlar 4, etanoatlar 2, propanoatlar 1, bütanoatlar 2 (dallı olan dahil).','4 + 2 + 1 + 2 = 9'),
   A('Farkı bul','Ester sayısından asit sayısını çıkar.','9 − 4 = 5')],
  metin='C₅H₁₀O₂ molekül formülüne sahip, açık zincirli (halkasız) ve fonksiyonel grup olarak yalnız karboksilik asit ya da ester içeren bileşikler düşünülüyor (stereoizomerler ayrı sayılmıyor).\nBuna göre bu bileşiklerden ester olanların sayısı, karboksilik asit olanların sayısından kaç fazladır?',
  sekil=None,istenen='Ester sayısı ile asit sayısı arasındaki fark.',ip=['Karbon sayısı beş olan bileşiği asit ve ester için ayrı ayrı, alkil gruplarının yapılarını sayarak tara.'],
  bilgi=[B('Asit ve ester izomerliği','Karboksilik asitler (R–COOH) ile esterler (R–COO–R′) aynı genel formüle sahiptir. Örnek: C₃H₆O₂ formülü hem propanoik asiti hem de metil etanoat ile etil metanoatı verir')],
  puf='Aynı formülde ester sayısı genellikle asit sayısından çoktur; her ikisini de alkil gruplarının yapılarıyla say.',dogru=dg11,
  yan=[(a5,'Yalnız karboksilik asit sayısını yazmış; ester sayısını bulup farkı almamıştır.','dikkat'),
       (e5,'Yalnız ester sayısını yazmış; asit sayısını çıkarmamıştır.','dikkat'),
       (e5+a5,'Asit ve ester sayısını toplamış; soru farkı istemektedir.','dikkat'),
       ((e5-fm5)-a5,'Metanoat (HCOO–) esterlerini saymamış; bu da ester sayısını 5 bulmasına neden olmuştur.','bilgi')])

# ================= 12 · fonksiyonel grup izomerliği · orta · öncüllü · şekil =================
K12,L12,M12=parse('CCCC=O'),parse('CCC(C)=O'),parse('CC(C)C=O')
assert formul(K12)==formul(L12)==formul(M12)==(4,8,1,0)
assert sinifla(K12)=={'aldehit'} and sinifla(L12)=={'keton'} and sinifla(M12)=={'aldehit'}
assert sinifla(aldehit_asit(M12))=={'asit'} and not ayni(K12,M12) and not ayni(K12,L12)
d=dict(I=(True,'K bir aldehit, L bir ketondur; ikisi de C₄H₈O formüllüdür, yani fonksiyonel grup izomeridir'),
       II=(False,'L bir keton, M bir aldehittir; fonksiyonel grupları farklı olduğundan zincir değil fonksiyonel grup izomeridir'),
       III=(False,'M bir aldehittir; yükseltgenince keton değil karboksilik asit oluşur'))
o=OC(d,sr('Yalnız I','Yalnız II','I ve II','I ve III','II ve III')); assert o['dogru']=='Yalnız I'
SK=tk(satirlar([[('m','CCCC=O',None,'K'),('m','CCC(C)=O',None,'L'),('m','CC(C)C=O',None,'M')]],bosluk=1.3))
Q('0012','izo','orta','öncüllü','Fonksiyonel grup ve zincir izomerliği','Aldehit–keton fonksiyonel grup izomerliğini zincir izomerliğinden ayırt eder.',
  'Fonksiyonel grup izomerleri aynı formülde farklı fonksiyonel gruba, zincir izomerleri aynı gruba ve farklı karbon iskeletine sahiptir.','Farklı fonksiyonel gruplu izomerleri zincir izomeri saymak.','K, L, M karbonil bileşikleri',
  [A('Formülleri ve grupları bul','Üçünde de C=O vardır; karbonil karbonuna bağlı karbon sayısına bak.','K: aldehit · L: keton · M: aldehit'),
   A('I’i incele','K ve L aynı formüllü, farklı fonksiyonel gruplu bileşiklerdir.','I doğru'),
   A('II’yi incele','L ve M’nin fonksiyonel grupları farklıdır.','II yanlış'),
   A('III’ü incele','Aldehit yükseltgenince asit verir.','III yanlış')],
  metin='Şekilde iskelet formülleri verilen K, L ve M bileşikleri ile ilgili,\nI. K ve L birbirinin fonksiyonel grup izomeridir.\nII. L ve M birbirinin zincir izomeridir.\nIII. M yükseltgenirse bir keton oluşur.\nBuna göre bu yargılardan hangileri doğrudur?',
  sekil=SK,istenen='Doğru olan yargılar.',ip=['Her bileşikte C=O karbonuna bağlı karbon sayısını sayarak fonksiyonel grubu belirle.'],
  bilgi=[B('İzomer çeşitleri','Zincir izomerleri aynı fonksiyonel grubu taşır, karbon iskeleti farklıdır. Fonksiyonel grup izomerleri aynı formülde farklı grup taşır. Örnek: C₂H₆O formülü hem etanolü (alkol) hem dimetil eteri (eter) verir')],
  puf='Fonksiyonel grup farklıysa izomer fonksiyonel grup izomeridir; zincir izomerliğinde grup aynı kalır.',dogru=o['dogru'],yan=o['yan'],sira=o['sira'])

# ================= 13 · zincir: eten → ester · zor · şekil =================
A13=H2O_ekle(parse('C=C'))[0]; assert ayni(A13,parse('CCO'))
B13=yukseltgen(A13); assert ayni(B13,parse('CC=O'))
C13=aldehit_asit(B13); assert ayni(C13,parse('CC(=O)O'))
D13=esterle(C13,A13); assert ayni(D13,parse('CC(=O)OCC'))
def mkutle(G): c,h,o_,x=formul(G); assert x==0; return 12*c+h+16*o_
m13=mkutle(D13); assert m13==88
v13=[mkutle(B13),mkutle(C13),m13-18,mkutle(C13)+mkutle(A13)]; assert v13==[44,60,70,106] and len(set(v13+[m13]))==5
SK=tk(satirlar([[('m','C=C'),('->','H$_2$O','',2.0),('kutu','A'),('->','yükseltgenme','',2.6),('kutu','B')],
                [('kutu','B'),('->','yükseltgenme','',2.6),('kutu','C')],
                [('kutu','C'),('+',),('kutu','A'),('->','H$^+$','',2.0),('kutu','D'),('+',),('y','H$_2$O')]],bosluk=0.5))
Q('0013','zin','zor','şekilli','Tepkime zinciri (eten → ester)','Katılma, ardışık yükseltgenme ve kondenzasyon basamaklarını izleyerek son ürünün mol kütlesini bulur.',
  'Eten + H₂O → alkol; alkol → aldehit → karboksilik asit; asit + alkol → ester + su.','Zincirin bir basamağında durup ara ürünün mol kütlesini vermek.','eten → etil etanoat zinciri',
  [A('A’yı bul','Eten, suyla katılma tepkimesi verir ve etanol oluşur.','C₂H₄ + H₂O → C₂H₅OH'),
   A('B ve C’yi bul','Birincil alkol önce aldehite, sonra karboksilik aside yükseltgenir.','B: etanal · C: etanoik asit'),
   A('D’yi bul','C ile A’nın kondenzasyonundan ester ve su oluşur.','CH₃COOH + C₂H₅OH → CH₃COOC₂H₅ + H₂O'),
   A('Mol kütlesini hesapla','D’nin formülü C₄H₈O₂’dir.','4 × 12 + 8 × 1 + 2 × 16 = 88')],
  metin='Şekilde eten ile başlayan bir tepkime zinciri gösterilmiştir. B ve C bileşikleri, A bileşiğinin ardışık yükseltgenme ürünleridir (H: 1, C: 12, O: 16 g/mol).\nBuna göre D bileşiğinin mol kütlesi kaç g/mol’dür?',
  sekil=SK,istenen='D bileşiğinin mol kütlesi (g/mol).',ip=['Her basamaktaki tepkime türünü belirleyip bileşikleri sırayla yaz; D’nin hangi iki bileşikten oluştuğuna dikkat et.'],
  bilgi=[B('Basamaklı dönüşümler','Alkenden hidrasyonla alkol, alkolden yükseltgenmeyle aldehit ve asit, asit ile alkolden ester elde edilir. Örnek: propen → 2-propanol (katılma) → propanon (yükseltgenme)')],
  puf='Zincirde her okun türünü adlandır; ürünün formülünü bulunca mol kütlesi tek işlemdir.',dogru=m13,
  yan=[(v13[0],'Zincirde B’de durmuş; etanalin mol kütlesini yazmıştır.','dikkat'),(v13[1],'Zincirde C’de durmuş; etanoik asidin mol kütlesini yazmıştır.','dikkat'),
       (v13[2],'D’nin mol kütlesinden bir kez daha su çıkarmıştır; 88 − 18 = 70 değerini yazmıştır.','islem'),
       (v13[3],'D’yi C ile A’nın mol kütleleri toplamı sanmış, ayrılan suyu çıkarmamıştır; 60 + 46 = 106 yazmıştır.','bilgi')])

# ================= 14 · zincir: propen → keton · orta · öncüllü · şekil =================
A14=HX_ekle(parse('C=CC'),'Br'); assert len(A14)==1 and ayni(A14[0],parse('CC(C)Br'))
B14=Hdegis(A14[0],'Br','O'); assert ayni(B14,parse('CC(C)O')) and sinifla(B14)=={'alkol'}
C14=yukseltgen(B14); assert ayni(C14,parse('CC(C)=O')) and sinifla(C14)=={'keton'}
assert not ayni(A14[0],parse('CCCBr'))
d=dict(I=(False,'Markovnikov kuralına göre brom ikinci karbona bağlanır; A, 2-bromopropandır'),
       II=(False,'A’dan B’ye Br yerine OH geçer, yani iki ürünlü bir yer değiştirme olur; ayrılmada çift bağ oluşurdu'),
       III=(True,'B ikincil alkoldür ve yükseltgenince propanon (keton) oluşur'))
o=OC(d,sr('Yalnız I','Yalnız III','I ve II','I ve III','II ve III')); assert o['dogru']=='Yalnız III'
SK=tk(satirlar([[('m','C=CC'),('->','HBr','',2.0),('kutu','A'),('->','NaOH(sulu)','',2.6),('kutu','B')],[('kutu','B'),('->','yükseltgenme','',2.6),('kutu','C')]],bosluk=0.5))
Q('0014','zin','orta','öncüllü','Tepkime zinciri (propen → keton)','Katılma, yer değiştirme ve yükseltgenme basamaklarını ürünler ve tepkime türleri açısından yorumlar.',
  'HX katılması halojenli bileşik verir; halojenli bileşik sulu NaOH ile alkole dönüşür (yer değiştirme); ikincil alkol yükseltgenince keton oluşur.','Halojenin sulu NaOH ile yer değiştirmesini ayrılma sanmak.','propen → 2-propanol → propanon',
  [A('A’yı bul','HBr katılmasında brom ikinci karbona bağlanır.','A: 2-bromopropan'),A('B’yi bul','Sulu NaOH ile Br yerine OH geçer; yer değiştirme tepkimesidir.','B: 2-propanol'),
   A('C’yi bul','İkincil alkol yükseltgenince keton oluşur.','C: propanon'),A('Yargıları değerlendir','Yalnız III doğrudur.','III doğru')],
  metin='Şekilde propen ile başlayan bir tepkime zinciri gösterilmiştir.\nI. A bileşiği 1-bromopropandır.\nII. A’dan B’ye dönüşüm bir ayrılma tepkimesidir.\nIII. C bileşiği bir ketondur.\nBuna göre bu yargılardan hangileri doğrudur?',
  sekil=SK,istenen='Doğru olan yargılar.',ip=['Zincirdeki her basamağı sırayla çöz ve her okta hangi atomun/grubun nereye bağlandığını izle.'],
  bilgi=[B('Halojenli bileşiğin dönüşümü','Sulu NaOH ile halojenli bileşikte halojen –OH ile yer değiştirir ve alkol oluşur. Alkollü KOH ile ise HX ayrılır ve alken oluşur. Örnek: 1-kloropropan + NaOH(sulu) → 1-propanol + NaCl')],
  puf='Sulu NaOH yer değiştirme, alkollü KOH ayrılma verir.',dogru=o['dogru'],yan=o['yan'],sira=o['sira'])

# ================= 15 · zincir: etin → ester · zor · öncüllü · şekil =================
X15=alkin_hidrasyon(parse('C#C')); assert len(X15)==1 and ayni(X15[0],parse('CC=O')) and sinifla(X15[0])=={'aldehit'}
Y15=aldehit_asit(X15[0]); assert ayni(Y15,parse('CC(=O)O'))
Z15=esterle(Y15,parse('OC')); assert ayni(Z15,parse('CC(=O)OC')) and formul(Z15)==(3,6,2,0)
PR=parse('CCC(=O)O'); assert formul(PR)==formul(Z15) and sinifla(PR)=={'asit'} and sinifla(Z15)=={'ester'} and not ayni(PR,Z15)
assert formul(Y15)!=formul(Z15)
d=dict(I=(True,'Etine su katılınca kararlı ürün etanal (aldehit) olur; X bir aldehittir'),
       II=(False,'Y (C₂H₄O₂) ile Z (C₃H₆O₂) farklı formüllü bileşiklerdir, yapı izomeri olamazlar'),
       III=(True,'Z (metil etanoat) ile propanoik asit aynı formüle (C₃H₆O₂) ve farklı fonksiyonel gruba (ester ve asit) sahiptir'))
o=OC(d,sr('Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III')); assert o['dogru']=='I ve III'
SK=tk(satirlar([[('m','C#C'),('->','H$_2$O','',1.8),('kutu','X'),('->','yükseltgenme','',2.5),('kutu','Y')],[('kutu','Y'),('+',),('y','CH$_3$OH'),('->','H$^+$','',1.8),('kutu','Z'),('+',),('y','H$_2$O')]],bosluk=0.5))
Q('0015','zin','orta','öncüllü','Tepkime zinciri (etin → ester) ve izomerlik','Alkin hidrasyonu, yükseltgenme ve ester oluşumunu izleyip ürünlerin izomerlik ilişkisini yorumlar.',
  'Etine su katılınca aldehit; aldehit yükseltgenince asit; asit + alkol → ester; esterler aynı formüllü karboksilik asitlerin fonksiyonel grup izomeridir.','Ester ile aynı sayıda karbonlu asidi aynı formüllü sanmak ya da tersi.','etin → metil etanoat zinciri',
  [A('X’i bul','Etine su katılınca kararlı ürün aldehit olur.','X: etanal'),A('Y’yi bul','Aldehit yükseltgenince karboksilik asit oluşur.','Y: etanoik asit'),
   A('Z’yi bul','Y ile metanol ester ve su verir.','Z: metil etanoat (C₃H₆O₂)'),A('Yargıları değerlendir','Y ile Z’nin formülleri farklı; Z ile propanoik asit aynı formüllü, farklı gruplu.','I ve III doğru')],
  metin='Şekilde etin ile başlayan bir tepkime zinciri gösterilmiştir.\nI. X bileşiği bir aldehittir.\nII. Y ve Z bileşikleri birbirinin yapı izomeridir.\nIII. Z bileşiği ile propanoik asit birbirinin fonksiyonel grup izomeridir.\nBuna göre bu yargılardan hangileri doğrudur?',
  sekil=SK,istenen='Doğru olan yargılar.',ip=['Zincirdeki bileşiklerin formüllerini yazıp aynı formüllü olanların fonksiyonel gruplarını karşılaştır.'],
  bilgi=[B('Alkine su katılması','Alkine su katılınca önce kararsız bir enol oluşur ve karbonil bileşiğine dönüşür; ürün alkinin yapısına göre değişir. Örnek: 1-bütin + H₂O → 2-bütanon')],
  puf='Zincirde her basamağın ürününü yazıp formülleri ve fonksiyonel grupları karşılaştır.',dogru=o['dogru'],yan=o['yan'],sira=o['sira'])

# ================= 16 · gaz karışımı · zor · şekil =================
mE16,mEt=Fr(28),Fr(30); n_top=Fr(1,2); kt=Fr(56,10); n_eten=kt/mEt if False else kt/mE16; n_etan=n_top-n_eten; assert (n_eten,n_etan)==(Fr(1,5),Fr(3,10))
mCl=12*2+5+Fr(71,2); assert mCl==Fr(129,2)
dg16=n_etan*mCl; assert dg16==Fr('19.35')
w16=[n_eten*mCl,n_etan*(mCl+1),n_etan*(2*12+4+71),n_top*mCl]; assert w16==[Fr('12.9'),Fr('19.65'),Fr('29.7'),Fr('32.25')]
g=('\\draw[thick,rounded corners=2pt] (0,-.8) rectangle (2.6,.8);\\node[align=center,font=\\small] at (1.3,0) {\\ce{C2H4} + \\ce{C2H6}\\\\[-1pt]0,5 mol};'
   '\\draw[-{Stealth[length=2.4mm]},thick] (2.6,0) -- (3.6,0);'
   '\\draw[thick,fill=vurgu!15] (3.6,-.8) rectangle (6.2,.55);\\draw[thick] (3.6,.55) -- (3.6,.8) (6.2,.55) -- (6.2,.8);'
   '\\node[font=\\small] at (4.9,-.12) {\\ce{Br2} çözeltisi};\\node[font=\\small,align=center] at (4.9,-1.35) {kütle artışı\\\\[-1pt]5,6 g};'
   '\\draw[-{Stealth[length=2.4mm]},thick] (6.2,0) -- (7.2,0);'
   '\\draw[thick,rounded corners=2pt] (7.2,-.8) rectangle (10.0,.8);\\node[align=center,font=\\small] at (8.6,0) {yeterli \\ce{Cl2}\\\\[-1pt]ışık};'
   '\\draw[-{Stealth[length=2.4mm]},thick] (8.6,-.8) -- (8.6,-1.7);\\node[font=\\small\\bfseries] at (8.6,-2.05) {\\ce{C2H5Cl}};')
SK=tk(g)
Q('0016','hes','zor','şekilli','Gaz karışımı ve ardışık tepkimeler','Katılma ve yer değiştirme tepkimelerini ardışık uygulayarak karışım bileşimini ve ürün kütlesini bulur.',
  'Br₂ çözeltisi yalnız alkene katılır (kütle artışı alkenin kütlesidir); alkan ışıkta Cl₂ ile yer değiştirme tepkimesi verir.','Toplam mole ya da yalnız alkenin molüne göre ürün kütlesini hesaplamak.','eten–etan karışımı',
  [A('Alkeni belirle','Br₂ çözeltisinde yalnız eten tutulur; kütle artışı etenin kütlesidir.','5,6 ÷ 28 = 0,2 mol eten'),
   A('Etanı bul','Toplam moldan eten molünü çıkar.','0,5 − 0,2 = 0,3 mol etan'),
   A('Yer değiştirmeyi yaz','Etan ışıkta Cl₂ ile bir H’sini Cl ile değiştirir; 1 mol etandan 1 mol C₂H₅Cl oluşur.','C₂H₆ + Cl₂ → C₂H₅Cl + HCl'),
   A('Kütleyi hesapla','C₂H₅Cl’nin mol kütlesi 64,5 g/mol’dür.','0,3 × 64,5 = 19,35 g')],
  metin='Şekildeki düzenekte eten ve etan gazlarından oluşan karışım Br₂ çözeltisinden geçirildiğinde yalnız eten tutulmakta, etan hiçbir değişikliğe uğramadan çıkmaktadır. Çıkan gazın tamamı ışık altında yeterli Cl₂ ile tepkimeye girerek yalnız C₂H₅Cl vermektedir. Tepkimeler %100 verimle gerçekleşmektedir (H: 1, C: 12, Cl: 35,5 g/mol).\nBuna göre oluşan C₂H₅Cl kaç gramdır?',
  sekil=SK,istenen='Oluşan C₂H₅Cl’nin kütlesi (g).',ip=['Br₂ çözeltisinin kütle artışının hangi gaza ait olduğunu düşünüp etanın molünü bul.'],
  bilgi=[B('Alken–alkan ayrımı','Alkenler Br₂ çözeltisine katılma tepkimesiyle tutulur ve çözeltinin kütlesi artar; alkanlar tutulmaz. Alkanlar ışık altında halojenle yer değiştirme tepkimesi verir. Örnek: propen Br₂ çözeltisini renksizleştirir, propan renksizleştirmez')],
  puf='Br₂ çözeltisindeki kütle artışı alkenin kütlesidir; kalan gaz alkandır.',dogru=dg16,
  yan=[(w16[0],'Eten molüne göre hesaplamış; Br₂ ile tutulan etenden değil kalan etandan C₂H₅Cl oluştuğunu atlamıştır, 0,2 × 64,5 = 12,9 g bulmuştur.','dikkat'),
       (w16[1],'C₂H₅Cl’nin mol kütlesini 65,5 g/mol almış (hidrojen çıkarılmadan Cl eklenmiş); 0,3 × 65,5 = 19,65 g bulmuştur.','islem'),
       (w16[2],'Etanın iki hidrojenini de klorla değiştirmiş; 0,3 × 99 = 29,7 g (C₂H₄Cl₂) bulmuştur.','bilgi'),
       (w16[3],'Toplam mole göre hesaplamış; 0,5 × 64,5 = 32,25 g bulmuştur.','dikkat')])

# ================= 17 · cis / trans 2-büten · orta · öncüllü · şekil =================
cK,cL=parse('CC=CC'),parse('CC=CC'); assert cis_trans(cK,{3:-90})=='cis' and cis_trans(cL)=='trans'
assert ayni(cK,cL)
assert ayni(H2_ekle(cK),parse('CCCC')) and ayni(H2_ekle(cL),parse('CCCC'))
h1,h2=HX_ekle(cK,'Br'),HX_ekle(cL,'Br'); assert len(h1)==len(h2)==1 and ayni(h1[0],h2[0]) and ayni(h1[0],parse('CCC(C)Br'))
d=dict(I=(True,'K ve L’nin ikisi de H₂ ile bütana dönüşür; aynı ürün oluşur'),
       II=(True,'K ve L’ye HBr katılınca ikisi de 2-bromobütan verir'),
       III=(False,'Geometrik izomerlerin fiziksel özellikleri farklıdır; K ile L’nin kaynama noktaları birbirine eşit değildir'))
o=OC(d,sr('Yalnız III','I ve II','I ve III','II ve III','I, II ve III')); assert o['dogru']=='I ve II'
SK=tk(satirlar([[('m','CC=CC',{3:-90},'K'),('m','CC=CC',None,'L')]],bosluk=1.6))
Q('0017','kat','orta','öncüllü','Geometrik izomerlerin katılma tepkimeleri','Cis ve trans izomerlerin katılma ürünlerini ve fiziksel özelliklerini karşılaştırır.',
  'Geometrik izomerler aynı bağlanma sırasına sahip olduğundan katılma ürünleri aynıdır; fiziksel özellikleri ise farklıdır.','Geometrik izomerlerin fiziksel özelliklerinin de aynı olduğunu düşünmek.','cis-2-büten ve trans-2-büten',
  [A('K ve L’yi tanı','İki bileşik de çift bağlı dört karbonlu zincirdir; CH₃ grupları çift bağın aynı ya da zıt yanındadır.','K: cis · L: trans'),
   A('H₂ katılmasını yaz','Çift bağ açılır, iskelet aynı kalır.','Her ikisi → bütan'),
   A('HBr katılmasını yaz','Çift bağın iki ucu da özdeş (1 H, 1 CH₃) olduğundan brom iki karbondan birine bağlanır, ürün aynıdır.','Her ikisi → 2-bromobütan'),
   A('Kaynama noktasını değerlendir','Cis ve trans izomerlerin kutupluluğu ve moleküller arası etkileşimi farklı olduğundan kaynama noktaları da farklıdır.','III yanlış')],
  metin='Şekilde iskelet formülleri verilen K ve L bileşikleri geometrik izomerdir.\nI. K ve L, H₂ ile tepkimeye girdiğinde aynı ürün oluşur.\nII. K ve L’ye HBr katılması sonucu oluşan ana ürün 2-bromobütandır.\nIII. K ve L’nin kaynama noktaları birbirine eşittir.\nBuna göre bu yargılardan hangileri doğrudur?',
  sekil=SK,istenen='Doğru olan yargılar.',ip=['Geometrik izomerlerin atomlarının bağlanma sırasının ve molekül polaritesinin aynı olup olmadığını düşün.'],
  bilgi=[B('Geometrik izomerlerin özellikleri','Geometrik izomerlerde atomların bağlanma sırası aynıdır; katılma tepkimelerinde genellikle aynı ürünü verirler. Dipol momentleri farklı olduğundan kaynama noktası gibi fiziksel özellikleri farklıdır. Örnek: cis-1,2-dikloroeten ile trans-1,2-dikloroetenin kaynama noktaları farklıdır')],
  puf='Geometrik izomerler kimyasal tepkimelerde çoğu kez aynı ürünü verir, fiziksel özellikleri ise farklıdır.',dogru=o['dogru'],yan=o['yan'],sira=o['sira'])

# ================= 18 · etanol yargıları · orta · düz · olumsuz kök =================
Et=parse('CCO')
assert ayni(yukseltgen(Et),parse('CC=O')) and sinifla(yukseltgen(Et))=={'aldehit'}
assert ayni(ayrilma(Et,'O')[0],parse('C=C')) and ayni(H2O_ekle(parse('C=C'))[0],Et)
assert ayni(esterle(parse('CC(=O)O'),Et),parse('CC(=O)OCC'))
S18=[('Yükseltgenmesiyle önce etanal oluşur',True,'birincil alkol yükseltgenince önce aldehit oluşur'),
     ('Derişik H₂SO₄ ile 170 °C’ta ısıtılınca eten oluşur',True,'dehidratasyon ayrılma tepkimesidir ve alken verir'),
     ('Etanoik asitle tepkimesinden etil etanoat ve su oluşur',True,'asit ve alkol kondenzasyonla ester verir'),
     ('Eten ile suyun katılma tepkimesinden elde edilebilir',True,'alkene su katılınca alkol oluşur'),
     ('Yükseltgenmesi sonucunda doğrudan bir keton oluşur',False,'birincil alkol keton vermez; aldehit ve asit oluşur')]
o=tek(S18,hedef=False)
o['sira']=[S18[4][0],S18[0][0],S18[1][0],S18[2][0],S18[3][0]]
Q('0018','yuk','kolay','düz','Etanolün tepkimeleri','Birincil alkolün yükseltgenme, ayrılma, kondenzasyon ve katılma tepkimelerindeki rolünü ayırt eder.',
  'Birincil alkol yükseltgenince aldehit, sonra asit; derişik H₂SO₄ ile alken; asitle ester verir; alkenden hidrasyonla elde edilir.','Birincil alkolün keton verdiğini sanmak.','etanol',
  [A('Alkol sınıfını bul','Etanolde –OH, iki hidrojen taşıyan ve bir karbona bağlı karbondadır.','Birincil alkol'),
   A('Yükseltgenmeyi hatırla','Birincil alkol önce aldehit, sonra karboksilik asit verir.','Etanol → etanal → etanoik asit'),
   A('Diğer tepkimeleri kontrol et','Dehidratasyon eten, asitle kondenzasyon ester, etene su katılması etanol verir.','Bu üç ifade doğru'),
   A('Yanlışı seç','Keton, ikincil alkolün yükseltgenme ürünüdür.','Keton ifadesi yanlış')],
  metin='Etanol (C₂H₅OH) ile ilgili aşağıdakilerden hangisi yanlıştır?',
  sekil=None,istenen='Yanlış olan ifade.',ip=['Etanolün alkol sınıfını belirle ve her ifadeyi bu sınıfın tepkimeleriyle karşılaştır.'],
  bilgi=[B('Alkollerin tepkimeleri','Alkoller yükseltgenme, dehidratasyon ve karboksilik asitle ester oluşturma tepkimelerine girer. Birincil alkol aldehit ve asit, ikincil alkol keton verir. Örnek: 2-propanol → propanon')],
  puf='Alkolün sınıfı, yükseltgenme ürününü belirler.',dogru=o['dogru'],yan=o['yan'],sira=o['sira'])

# ================= 19 · tanım–dehidratasyon · zor · tablo =================
L4=uret(4,1,0,0); alk4=[g for g in L4 if sinifla(g)=={'alkol'}]
def karbinol(g): return [c for x in g if g.nodes[x]['t']=='O' and len(g[x])==1 for c in g[x]][0]
sek4=[g for g in alk4 if nH(g,karbinol(g))==1]; assert len(sek4)==1
X19=sek4[0]; assert ayni(X19,parse('CCC(C)O'))
ur19=ayrilma(X19,'O'); dg19=stereo_urun(ur19); assert len(ur19)==2 and dg19==3
pr4=[g for g in alk4 if nH(g,karbinol(g))==2]; assert len(pr4)==2
e19a=max(stereo_urun(ayrilma(g,'O')) for g in pr4)  # 1-bütanol 1; 2-metil-1-propanol 1
assert e19a==1
e19b=len(ur19); assert e19b==2
e19c=stereo_urun(uret(4,0,0,1)); assert e19c==4
e19d=len(L4); assert e19d==7
assert len({dg19,e19a,e19b,e19c,e19d})==5
SK=tablo_svg(['Özellik','X bileşiği'],[['Molekül formülü','C₄H₁₀O'],['Na metali ile tepkime','H₂ gazı açığa çıkar'],['Asitli K₂Cr₂O₇ ile ısıtma','Keton oluşur']])
Q('0019','ayr','zor','tablo','Yapı belirleme ve dehidratasyon ürünleri','Deney verilerinden alkolün yapısını bulup dehidratasyon ürünlerini cis-trans dahil sayar.',
  'Na ile H₂ veren ve yükseltgenince keton oluşturan C₄H₁₀O bileşiği ikincil alkoldür; dehidratasyonda komşu karbonlardan H ayrılarak ürün çeşitliliği oluşur.','Cis ve trans izomerleri ayrı ürün saymamak ya da alkolün sınıfını yanlış belirlemek.','X alkolü',
  [A('Fonksiyonel grubu bul','Na ile H₂ çıkışı alkoldür; yükseltgenince keton veriyorsa ikincil alkoldür.','X: ikincil alkol, C₄H₁₀O'),
   A('X’i yaz','Dört karbonlu ikincil alkol tektir: –OH ikinci karbondadır.','X: 2-bütanol'),
   A('Ayrılma ürünlerini yaz','OH ikinci karbondan, H birinci ya da üçüncü karbondan ayrılabilir.','1-büten · 2-büten'),
   A('Geometrik izomerleri say','2-büten cis ve trans olmak üzere iki biçimdedir.','1 + 2 = 3')],
  metin='Tabloda X bileşiğine ait bazı özellikler verilmiştir. X bileşiği derişik H₂SO₄ eşliğinde ısıtılarak ayrılma tepkimesine sokuluyor.\nBuna göre bu tepkimede oluşabilecek alkenlerin sayısı (cis ve trans biçimleri ayrı sayılmak üzere) kaçtır?',
  sekil=SK,istenen='Oluşabilecek farklı alken sayısı.',ip=['Tablodaki iki deney sonucundan alkolün sınıfını bulup yalnız o sınıfa uyan C₄H₁₀O yapısını yaz.'],
  bilgi=[B('Alkolün sınıfını deneyle bulma','Na metali alkolden H₂ açığa çıkarır. Yükseltgenmede birincil alkol aldehit, ikincil alkol keton verir, üçüncül alkol yükseltgenmez. Örnek: C₃H₈O formüllü ve keton veren alkol 2-propanoldür')],
  puf='Önce deney verisinden bileşiğin tek yapısını bul, sonra ürünleri geometrik izomerlerle birlikte say.',dogru=dg19,
  yan=[(e19a,'Bileşiği birincil alkol sanmış; birincil alkoller tek alken verir ve 1 bulmuştur.','bilgi'),
       (e19b,'Cis ve trans biçimlerini ayırmamış; 1-büten ile 2-bütenin toplamı olan 2 değerini yazmıştır.','dikkat'),
       (e19c,'C₄H₈ formülüne uyan bütün alkenleri saymış; 2-metilpropen X’in ürünü olamaz, 4 bulmuştur.','bilgi'),
       (e19d,'C₄H₁₀O formüllü bütün alkol ve eter izomerlerini saymıştır; bu 7 değeri alken sayısı değildir.','bilgi')])

# ================= 20 · alkil halojenür ayrılması · zor · şekil =================
CL={'K':'CCCCCl','L':'CCC(C)Cl','M':'CC(C)CCl','N':'CC(C)(C)Cl','P':'CCC(Cl)CC'}
GL={k:parse(v) for k,v in CL.items()}
urs={k:ayrilma(g,'Cl') for k,g in GL.items()}
sc={k:stereo_urun(v) for k,v in urs.items()}; assert sc=={'K':1,'L':3,'M':1,'N':1,'P':2}
nos={k:len(v) for k,v in urs.items()}; assert nos=={'K':1,'L':2,'M':1,'N':1,'P':1}
dg20=sum(1 for v in sc.values() if v==1); assert dg20==3
def beta(g):
    x=[v for v in g if g.nodes[v]['t']=='Cl'][0]; c=list(g[x])[0]; return len([w for w in g[c] if w!=x and nH(g,w)>0])
bt={k:beta(g) for k,g in GL.items()}; assert bt=={'K':1,'L':2,'M':1,'N':3,'P':2}
e20=[sum(1 for v in nos.values() if v==1),len(GL),sum(1 for v in bt.values() if v==1),1]; assert e20==[4,5,2,1]
SK=tk(satirlar([[('m',CL['K'],None,'K'),('m',CL['L'],None,'L'),('m',CL['M'],None,'M')],[('m',CL['N'],None,'N'),('m',CL['P'],None,'P')]],bosluk=1.2))
Q('0020','ayr','zor','şekilli','Alkil halojenürlerin ayrılma ürünleri','Alkil halojenürlerin HCl ayrılma tepkimesinde oluşan alken çeşitlerini geometrik izomerlerle birlikte sayar.',
  'HX ayrılması için halojenin bağlı olduğu karbonun komşularındaki farklı karbon türleri ürün çeşitliliğini belirler; cis ve trans ayrı ürün sayılır.','Komşu karbon sayısına bakıp özdeş karbonların aynı ürünü verdiğini atlamak ya da cis-trans ürünleri sayamamak.','K, L, M, N, P halojenürleri',
  [A('Ayrılmayı hatırla','Cl ile komşu karbondaki H ayrılır; aralarında çift bağ oluşur.','R–CHCl–CH₂R′ → R–CH=CHR′'),
   A('K, M, N’yi incele','Her birinde komşu karbonların hidrojenleri aynı alkeni verir.','K: 1-büten · M, N: 2-metilpropen'),
   A('L ve P’yi incele','L, 1-büten ile cis ve trans 2-büten verir (3); P ise cis ve trans 2-penten verir (2).','L: 3 · P: 2'),
   A('Say','Yalnız bir çeşit alken veren bileşikler K, M ve N’dir.','3')],
  metin='Şekilde iskelet formülleri verilen K, L, M, N ve P bileşikleri alkollü KOH çözeltisi eşliğinde ısıtıldığında, her birinden HCl ayrılarak alken oluşmaktadır. Cis ve trans biçimleri ayrı bileşik sayılacaktır.\nBuna göre bu bileşiklerden kaç tanesinden yalnız bir çeşit alken oluşur?',
  sekil=SK,istenen='Tek alken veren bileşik sayısı.',ip=['Her bileşikte Cl’nin bağlı olduğu karbonun komşularındaki hidrojenlerin özdeş olup olmadığını ve oluşan çift bağın cis-trans verip vermediğini incele.'],
  bilgi=[B('Dehidrohalojenasyon','Alkil halojenür alkollü KOH ile ısıtılınca halojenin bağlı olduğu karbonla komşu karbondan HX ayrılır, alken oluşur. Komşu karbonlar özdeş değilse birden çok alken oluşabilir. Örnek: 2-kloropropan → propen')],
  puf='Komşu karbonlar özdeşse tek yapı oluşur; ancak oluşan çift bağda cis-trans varsa iki ürün sayılır.',dogru=dg20,
  yan=[(e20[3],'Yalnız üçüncül halojenürü (N) tek ürünlü saymış; oysa K ve M de tek alken verir.','bilgi'),
       (e20[2],'Halojenli karbonun yalnız bir komşu karbonu olan bileşiklere (K, M) bakmış; N’nin üç özdeş komşusu da tek ürün verir.','bilgi'),
       (e20[0],'Cis-trans izomerlerini ayrı saymamış; P’yi de tek ürünlü sayınca 4 bulmuştur.','dikkat'),
       (e20[1],'Her halojenürden bir alken oluştuğunu görüp hepsini saymış; L ve P birden çok alken verir.','dikkat')])

# ---------- yaz ----------
for x in P.ANA: x['kardes']=None
SCR=os.environ.get('SCRATCH','/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/ot')
os.makedirs(SCR,exist_ok=True)
P.yaz(os.path.join(GD,'orgtepkime-1.json'),os.path.join(SCR,'bos-orgtepkime.json'))
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=KEY))['kartlar'].append(c['id'])
json.dump(dict(konu=KONU_AD,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2018–2026 Kimya, MEB 12. sınıf Organik Bileşikler.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','akorgtepkime.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
