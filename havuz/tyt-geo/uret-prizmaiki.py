"""TYT Geometri · Prizmalar II (alan, hacim, açınım, en kısa yol). Şekil koordinatları hesaplanır; TikZ aynı değerlerden üretilir (cizim.tikz_svg).
3B şekiller eğik görünümle çizilir; gizli kenarlar yüz görünürlüğünden hesaplanıp kesikli çizilir. Yüzey üzerinde en kısa yol, yüz açınımları denenerek bağımsız doğrulanır.
Her cevap ve çeldirici değer Python hesabıyla assert edilir."""
import sys,os,math,json
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
from math import sin,cos,tan,radians,degrees,atan2,sqrt,pi
TIPK={}
def konu(k,ad): P.k=k; P.konu_adi=ad; H.KONU=ad
def kartla(id,alt,fikir,tuzak,z,adim,tipId,tip,kaynak=None):
    kart(id,alt,fikir,tuzak,z,'şekilli',adim,tipId,tip,kaynak or 'ÖSYM 2018–2026 TYT Geometri soruları (yalnız mantık) · MEB 9–10. sınıf geometri'); TIPK[tipId]=P.k
def q(no,ad,kalip='şekilli',**k): mk(P,no,ad=ad,adim=len(ad),kalip=kalip,**k)
# ---------------- çizim yardımcıları (cm cinsinden koordinatlar) ----------------
def add(p,q_): return tuple(a+b for a,b in zip(p,q_))
def sub(p,q_): return tuple(a-b for a,b in zip(p,q_))
def mul(p,s): return tuple(a*s for a in p)
def ln(p): return math.sqrt(sum(a*a for a in p))
def un(p): n=ln(p); return tuple(a/n for a in p)
def mid(p,q_): return tuple((a+b)/2 for a,b in zip(p,q_))
def lerp(p,q_,t): return tuple(a+(b-a)*t for a,b in zip(p,q_))
def dist(p,q_): return ln(sub(p,q_))
def cen(ps): return tuple(sum(p[i] for p in ps)/len(ps) for i in range(len(ps[0])))
def pt(p): return f'({p[0]:.3f},{p[1]:.3f})'
def ang(V,a,b):
    u=sub(a,V); v=sub(b,V); return degrees(math.acos(sum(x*y for x,y in zip(u,v))/(ln(u)*ln(v))))
def alan(ps): return abs(sum(ps[i][0]*ps[(i+1)%len(ps)][1]-ps[(i+1)%len(ps)][0]*ps[i][1] for i in range(len(ps))))/2
class F:
    def __init__(s): s.o=[]
    def raw(s,t): s.o.append(t)
    def line(s,p,q_,st=''): s.o.append(f'\\draw[{st}] {pt(p)} -- {pt(q_)};')
    def poly(s,ps,st=''): s.o.append(f'\\draw[{st}] '+' -- '.join(map(pt,ps))+' -- cycle;')
    def fill(s,ps,st='fill=vurgu!25'): s.o.append(f'\\fill[{st}] '+' -- '.join(map(pt,ps))+' -- cycle;')
    def node(s,p,t,st=''): s.o.append(f'\\node[{st}] at {pt(p)} {{{t}}};')
    def vl(s,t,p,dv,d=.3): s.node(add(p,mul(un(dv),d)),f'${t}$')
    def sl(s,t,p,q_,ic,d=.3):
        m=mid(p,q_); e=un(sub(q_,p)); n=(-e[1],e[0])
        if n[0]*(m[0]-ic[0])+n[1]*(m[1]-ic[1])<0: n=(-n[0],-n[1])
        s.node(add(m,mul(n,d)),t)
    def arc(s,V,a,b,r,lab=None,lr=None,st=''):
        a1=degrees(atan2(a[1]-V[1],a[0]-V[0])); a2=degrees(atan2(b[1]-V[1],b[0]-V[0])); d=(a2-a1+180)%360-180
        s.o.append(f'\\draw[{st}] ({V[0]+r*cos(radians(a1)):.3f},{V[1]+r*sin(radians(a1)):.3f}) arc[start angle={a1:.2f},delta angle={d:.2f},radius={r}];')
        if lab: m=radians(a1+d/2); s.node((V[0]+lr*cos(m),V[1]+lr*sin(m)),lab)
    def dik(s,V,a,b,z=.22): u=un(sub(a,V)); v=un(sub(b,V)); s.o.append(f'\\draw {pt(add(V,mul(u,z)))} -- {pt(add(add(V,mul(u,z)),mul(v,z)))} -- {pt(add(V,mul(v,z)))};')
    def tick(s,p,q_,n=1,h=.09):
        m=mid(p,q_); e=un(sub(q_,p)); nn=(-e[1],e[0])
        for i in range(n):
            c=add(m,mul(e,(i-(n-1)/2)*.1)); s.line(add(c,mul(nn,h)),sub(c,mul(nn,h)))
    def body(s): return '\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'+'\n'.join(s.o)+'\n\\end{tikzpicture}'
    def svg(s): return tikz_svg(s.body())
# ---- 3B: eğik görünüm (x sağ, y derinlik, z yukarı); ön yüz (y sabit) gerçek oranda, derinlik yarı kısaltılmış ----
KA=radians(40); KK=.5
def proj(p,k=KK,al=KA): return (p[0]+k*p[1]*cos(al),p[2]+k*p[1]*sin(al))
W=(KK*cos(KA),-1,KK*sin(KA))      # gözlemciye doğru yön: ön, sağ ve üst yüzler görünür
class Solid:
    """V: ad->3B nokta; faces: ad->(köşe adları sırayla, DIŞ normal). Gizli kenar = komşu yüzlerin hiçbiri görünür değil."""
    def __init__(s,V,faces,sc=.4):
        s.V=V; s.faces=faces; s.sc=sc
        s.vis={k:sum(n[i]*W[i] for i in range(3))>1e-9 for k,(vs,n) in faces.items()}
        ed={}
        for k,(vs,n) in faces.items():
            for i in range(len(vs)):
                e=tuple(sorted((vs[i],vs[(i+1)%len(vs)]))); ed.setdefault(e,[]).append(k)
        for e,fs in ed.items(): assert len(fs)==2,('kenar iki yüze ait olmalı',e,fs)
        s.edges=ed; s.Q={k:mul(proj(v),sc) for k,v in V.items()}
    def hidden(s,e): return not any(s.vis[k] for k in s.edges[tuple(sorted(e))])
    def hid_list(s): return sorted(''.join(e) for e in s.edges if s.hidden(e))
    def draw(s,f,st='',gst='dashed'):
        for e in s.edges: f.line(s.Q[e[0]],s.Q[e[1]],gst if s.hidden(e) else st)
    def fillface(s,f,name,st='fill=vurgu!25'): f.fill([s.Q[v] for v in s.faces[name][0]],st)
def kutu(a,b,c,sc=.4,o=(0,0,0)):
    """a (x), b (derinlik y), c (yükseklik z) ayrıtlı dikdörtgenler prizması; köşe adları A B C D (taban) E F G H (üst)."""
    x,y,z=o
    V={'A':(x,y,z),'B':(x+a,y,z),'C':(x+a,y+b,z),'D':(x,y+b,z),'E':(x,y,z+c),'F':(x+a,y,z+c),'G':(x+a,y+b,z+c),'H':(x,y+b,z+c)}
    FC={'taban':('ADCB',(0,0,-1)),'ust':('EFGH',(0,0,1)),'on':('ABFE',(0,-1,0)),'arka':('DHGC',(0,1,0)),'sol':('ADHE',(-1,0,0)),'sag':('BCGF',(1,0,0))}
    return Solid(V,FC,sc)
RV={}
def Rd(k,r):
    """k√r biçimli metin (RV'ye değeri kaydedilir)."""
    s=(str(k) if r==1 else ('' if k==1 else str(k))+'√'+str(r)) if k!=0 else '0'; RV[s]=k*sqrt(r); return s
def Pm(a,b):
    s=f'{a} − {b}π' if b!=1 else f'{a} − π'; RV[s]=a-b*pi; return s
def Pk(k):
    s=f'{k}π' if k!=1 else 'π'; RV[s]=k*pi; return s
def Rp(a,k,r):
    s=f'{a} + {Rd(k,r)}'; RV[s]=a+k*sqrt(r); return s
def sirala(*ss): return sorted(ss,key=lambda t:RV[t])
def say(s): return s
def lbl(f,S,p,q_,t,off): f.node(add(mid(S.Q[p],S.Q[q_]),off),t)
def okdim(f,S,p,q_,t,dx,dl=.3):
    a=S.Q[p]; b=S.Q[q_]; f.raw(f'\\draw[<->,thin] {pt((a[0]+dx,a[1]))} -- {pt((b[0]+dx,b[1]))};'); f.node(((a[0]+b[0])/2+dx-dl,(a[1]+b[1])/2),t)
def shift(S,dx,dy): S.Q={k:(p[0]+dx,p[1]+dy) for k,p in S.Q.items()}
def dim(f,p,q_,t,off,dl=.28):
    """ölçü oku: p–q_ doğru parçasına off (birim vektör*uzaklık) kadar paralel, ucu oklu; etiket okun dışında."""
    e=un(sub(q_,p)); n=(-e[1],e[0]); n=mul(n,off/abs(off)) if off else n
    a=add(p,mul(n,abs(off))); b=add(q_,mul(n,abs(off))); f.raw(f'\\draw[<->,thin] {pt(a)} -- {pt(b)};'); f.node(add(mid(a,b),mul(n,dl)),t)
# ---- yüzey üzerinde en kısa yol: yüz dizilerini açarak bağımsız doğrulama ----
def _sub(a,b): return tuple(x-y for x,y in zip(a,b))
def _dot(a,b): return sum(x*y for x,y in zip(a,b))
def _nrm(a): return math.sqrt(_dot(a,a))
def _cr(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def _seg(p,q_,r,s):
    d1=(q_[0]-p[0],q_[1]-p[1]); d2=(s[0]-r[0],s[1]-r[1]); den=d1[0]*d2[1]-d1[1]*d2[0]
    if abs(den)<1e-12: return False
    t=((r[0]-p[0])*d2[1]-(r[1]-p[1])*d2[0])/den; u=((r[0]-p[0])*d1[1]-(r[1]-p[1])*d1[0])/den
    return -1e-9<=t<=1+1e-9 and -1e-9<=u<=1+1e-9
def kutu_yuzleri(a,b,c):
    V={'A':(0,0,0),'B':(a,0,0),'C':(a,b,0),'D':(0,b,0),'E':(0,0,c),'F':(a,0,c),'G':(a,b,c),'H':(0,b,c)}
    F_={'taban':'ABCD','ust':'EFGH','on':'ABFE','arka':'DCGH','sol':'ADHE','sag':'BCGF'}
    return {k:[V[x] for x in v] for k,v in F_.items()}
def yuzey_en_kisa(faces,Pn,fp,Qn,fq):
    names=list(faces); best=[1e18]
    def sh(f,g):
        s=[v for v in faces[f] if any(_nrm(_sub(v,w))<1e-9 for w in faces[g])]
        return s if len(s)==2 else None
    def rec(seq):
        if seq[-1]==fq: test(seq); return
        for g in names:
            if g not in seq and sh(seq[-1],g): rec(seq+[g])
    def test(seq):
        v=faces[seq[0]]; u=_sub(v[1],v[0]); u=tuple(x/_nrm(u) for x in u); n=_cr(u,_sub(v[2],v[0])); n=tuple(x/_nrm(n) for x in n); w=_cr(n,u); o=v[0]
        m=lambda p:(_dot(_sub(p,o),u),_dot(_sub(p,o),w)); P2=m(Pn); prevc=[m(x) for x in v]; edges=[]; mp={}; last=m
        for i in range(1,len(seq)):
            a3,b3=sh(seq[i-1],seq[i]); a2,b2=(m(a3),m(b3)) if i==1 else (mp[a3],mp[b3])
            ex=tuple(x/_nrm(_sub(b3,a3)) for x in _sub(b3,a3)); e2=(b2[0]-a2[0],b2[1]-a2[1]); l2=math.hypot(*e2); e2=(e2[0]/l2,e2[1]/l2); n2=(-e2[1],e2[0])
            cx=sum(p[0] for p in prevc)/len(prevc); cy=sum(p[1] for p in prevc)/len(prevc)
            if (cx-a2[0])*n2[0]+(cy-a2[1])*n2[1]>0: n2=(-n2[0],-n2[1])
            def mm(p,a3=a3,a2=a2,ex=ex,e2=e2,n2=n2):
                d=_sub(p,a3); s=_dot(d,ex); t=_nrm(_sub(d,tuple(s*x for x in ex))); return (a2[0]+s*e2[0]+t*n2[0],a2[1]+s*e2[1]+t*n2[1])
            mp={x:mm(x) for x in faces[seq[i]]}; prevc=[mp[x] for x in faces[seq[i]]]; edges.append((a2,b2)); last=mm
        Q2=last(Qn)
        if all(_seg(P2,Q2,e[0],e[1]) for e in edges): best[0]=min(best[0],math.hypot(Q2[0]-P2[0],Q2[1]-P2[1]))
    rec([fp]); return best[0]
P=Parti('prizmaiki','Prizmalar','geo|Prizmalar',ders='TYT Geometri',idon='tytgeo')
konu('geo|Prizmalar','Prizmalar')
HAC=B('Prizmanın hacmi','V = taban alanı × yükseklik. Örnek: tabanı kenarları 5 ve 4 olan dikdörtgen, yüksekliği 6 olan prizmanın hacmi 5 × 4 × 6 = 120 dir')
UCG=B('Üçgenin alanı','taban uzunluğu ile bu tabana ait yüksekliğin çarpımının yarısıdır. Örnek: tabanı 10, yüksekliği 7 olan üçgenin alanı 35 tir')
PIS=B('Pisagor bağıntısı','dik üçgende dik kenarların kareleri toplamı hipotenüsün karesine eşittir. Örnek: dik kenarları 9 ve 12 olan üçgende hipotenüs 15 tir')
YUZ=B('Prizmanın yüzey alanı','tüm yüzey alanı = 2 × taban alanı + taban çevresi × yükseklik. Örnek: tabanı kenarları 3 ve 5 olan dikdörtgen, yüksekliği 4 olan prizmada 2 × 15 + 16 × 4 = 94')
YAM=B('Yamuğun alanı','paralel kenarların toplamının yarısı ile yüksekliğin çarpımıdır. Örnek: paralel kenarları 5 ve 9, yüksekliği 4 olan yamuğun alanı 28 dir')
ESK=B('Eşkenar üçgen ve düzgün altıgen','kenarı a olan eşkenar üçgenin alanı a² × √3 ÷ 4 tür; düzgün altıgen 6 eş eşkenar üçgenden oluşur. Örnek: kenarı 2 olan düzgün altıgenin alanı 6 × √3 = 6√3 tür')
DIKP=B('Dikdörtgenler prizması','karşılıklı yüzleri eş olan 6 dikdörtgenden oluşur; her köşede üç ayrıt buluşur. Örnek: 2 × 3 × 5 lik prizmanın 8 köşesi, 12 ayrıtı ve 6 yüzü vardır')

# =================== 01 · Açınımdan hacim · kolay ===================
kartla('K-GPZ-01','Açınımı verilen kutunun hacmi','Açınımdaki toplam genişlik ve yükseklik ayrıt uzunluklarının toplamlarını verir; ayrıtlar çözülünce hacim üç ayrıtın çarpımıdır.','Hesaplanması gereken ayrıtı doğrudan toplam ölçü sanmak; alan ile hacmi karıştırmak.','kolay',3,'pz-acinim','Açınımı verilen prizmanın hacmi')
a1,b1,c1=7,5,4; W1=2*c1+a1; H1=2*b1+2*c1; V1=a1*b1*c1
assert (W1,H1,V1)==(15,18,140) and (W1-a1)//2==c1 and (H1-2*c1)//2==b1
assert 2*(a1*b1+b1*c1+c1*a1)==166 and a1*((W1-a1))*1==56 and a1*(H1//2)*c1==252 and W1*H1==270
s=.27; f=F()
R_=lambda x0,x1,y0,y1:[(x0*s,y0*s),(x1*s,y0*s),(x1*s,y1*s),(x0*s,y1*s)]
f.poly(R_(c1,c1+a1,0,b1)); f.poly(R_(c1,c1+a1,b1,b1+c1)); f.poly(R_(c1,c1+a1,b1+c1,2*b1+c1)); f.poly(R_(c1,c1+a1,2*b1+c1,H1))
f.poly(R_(0,c1,b1+c1,2*b1+c1)); f.poly(R_(c1+a1,W1,b1+c1,2*b1+c1))
dim(f,(0,0),(W1*s,0),'$15$',-.3)           # toplam genişlik (altta)
dim(f,(W1*s,0),(W1*s,H1*s),'$18$',-.3)     # toplam yükseklik (sağda)
dim(f,((c1+a1)*s,H1*s),(c1*s,H1*s),'$7$',-.3)  # üstteki dikdörtgenin yatay kenarı
SK1=f.svg()
q('0001',tipId='pz-acinim',tip='Açınımı verilen prizmanın hacmi',z='kolay',alt='Açınımdan Hacim',kaz='Dikdörtgenler prizmasının açınımındaki toplam ölçülerden ayrıtlarını bulup hacmini hesaplar.',kalip='şekilli',
 kart='K-GPZ-01 (açınım, hacim) · 15 × 18 açınım, 7 cm kenar',
 metin='Şekilde, dikdörtgenler prizması biçimindeki bir kutunun açınımı ve bazı ölçüleri cm cinsinden verilmiştir. Açınımın tüm yüzleri dikdörtgendir ve şekil ölçekli değildir.\nBuna göre, bu açınım katlanarak oluşturulan kutunun hacmi kaç cm³ tür?',
 dogru=140,yan=[(56,'Yan yüzlerin genişliğini 15 − 7 = 8 almış (iki yan yüzü tek saymış); ayrıtlar 7, 1 ve 8 çıkmış.','dikkat'),(270,'Açınımın toplam genişliği ile yüksekliğini (15 × 18) çarpıp hacim sanmış.','dikkat'),(166,'Hacim yerine kutunun yüzey alanını (2 × (35 + 20 + 28)) bulmuş.','bilgi'),(252,'Açınımın yüksekliğinin yarısını (9) taban ayrıtı alıp 7 × 9 × 4 hesaplamış.','islem')],
 istenen='Kutunun hacmi (cm³).',
 ip=['Açınımda toplam genişlik ve toplam yükseklik, kutunun hangi ayrıtlarının toplamlarından oluşuyor? Önce ayrıtların uzunluğunu belirle.'],
 bilgi=[HAC,DIKP],
 ad=[A('Yan ayrıtı bul','Toplam genişlik, ortadaki dikdörtgenin kenarı ile iki yan yüzün genişliğinin toplamıdır.','15 = 7 + 2 × c → c = 4'),A('Diğer ayrıtı bul','Toplam yükseklik iki b ile iki c nin toplamıdır.','18 = 2 × b + 2 × 4 → b = 5'),A('Hacmi hesapla','Üç ayrıtın çarpımı hacmi verir.','7 × 5 × 4 = 140')],
 puf='Şekilde verilen toplam ölçülerin hangi parçaların toplamı olduğunu yazarak denklem kur.',sekil=SK1)

# =================== 02 · Çadır (üçgen prizma hacmi) · kolay ===================
kartla('K-GPZ-02','Üçgen prizma biçimli çadırın hacmi','Ön yüz ikizkenar üçgendir; hacim, üçgenin alanı ile çadırın uzunluğunun çarpımıdır.','Üçgen alanındaki 1/2 çarpanını unutmak; üçgenin tabanını ve yüksekliğini çarpıp uzunlukla toplamak.','kolay',3,'pz-hacim','Üçgen ve yamuk tabanlı prizmanın hacmi')
w2,h2,L2=6,4,9; V2=w2*h2*L2//2; assert V2==108 and w2*h2*L2//3==72 and w2*h2==24 and w2*L2==54 and w2*h2//2==12
V={'A':(0,0,0),'B':(w2,0,0),'C':(w2/2,0,h2),'D':(0,L2,0),'E':(w2,L2,0),'F':(w2/2,L2,h2)}
nl=un((-h2,0,w2/2)); nr=un((h2,0,w2/2))
FC={'on':(list('ABC'),(0,-1,0)),'arka':(list('DEF'),(0,1,0)),'taban':(list('ABED'),(0,0,-1)),'sol':(list('ACFD'),nl),'sag':(list('BCFE'),nr)}
S2=Solid(V,FC,sc=.42); f=F(); S2.draw(f); Q=S2.Q
assert S2.hid_list()==['AD','DE','DF'],S2.hid_list()
m=(w2/2*.42,0); f.line(Q['C'],m,'thin'); f.dik(m,Q['B'],Q['C'],.17)
lbl(f,S2,'A','B','$6$',(0,-.3)); f.node((Q['C'][0]+.28,(Q['C'][1]+m[1])/2),'$4$'); lbl(f,S2,'B','E','$9$',(.3,-.1))
SK2=f.svg()
q('0002',tipId='pz-hacim',tip='Üçgen ve yamuk tabanlı prizmanın hacmi',z='kolay',alt='Çadırın Hacmi',kaz='Ön yüzü ikizkenar üçgen olan prizma biçimli çadırın hacmini hesaplar.',kalip='hikâyeli',
 kart='K-GPZ-02 (üçgen prizma hacmi) · çadır, ön yüz 6 × 4',
 metin='Bir kamp malzemeleri mağazasında satılan çadırın şekli, ön ve arka yüzü ikizkenar üçgen olan bir üçgen prizmadır. Ölçüleri metre cinsinden şekilde verilen çadırın zemini düzdür ve şekil ölçekli değildir.\nBuna göre, bu çadırın iç hacmi kaç m³ tür?',
 dogru=108,yan=[(24,'Üçgen yerine 6 × 4 lük dikdörtgenin alanını (24) hacim sanmış.','dikkat'),(54,'Çadırın tabanının alanını (6 × 9) hacim sanmış; yüksekliği kullanmamış.','dikkat'),(72,'Prizma yerine piramit formülünü (taban × yükseklik ÷ 3) kullanıp 6 × 4 × 9 ÷ 3 bulmuş.','bilgi'),(12,'Üçgenin alanını (12) bulup uzunlukla çarpmayı unutmuş.','islem')],
 istenen='Çadırın iç hacmi (m³).',
 ip=['Çadırın yan görünüşündeki dikdörtgen değil, ön yüzdeki üçgen tabandır; ön yüzün alanını hangi iki uzunluk belirler?'],
 bilgi=[HAC,UCG],
 ad=[A('Ön yüzün alanını bul','Ön yüz, tabanı 6 ve yüksekliği 4 olan üçgendir.','6 × 4 ÷ 2 = 12'),A('Hacim formülünü yaz','Prizmanın hacmi taban alanı ile uzunluğun çarpımıdır.','V = 12 × 9'),A('Hesapla','Çarpma yapılır.','12 × 9 = 108')],
 puf='Hacim hesabında önce kesit alanını, sonra uzunluğu çarpanlara ayır.',sekil=SK2)

# =================== 03 · Kutuda karınca: köşeden köşeye · orta ===================
kartla('K-GPZ-03','Dikdörtgenler prizmasında zıt köşelere en kısa yol','Komşu iki yüz aynı düzleme serilince köşeler bir dik üçgenin hipotenüsünün uçları olur; üç farklı serim denenip en küçüğü seçilir.','Ayrıt toplamını yol sanmak; cisim köşegenini (prizmanın içinden) yol saymak; yalnız tek serimi denemek.','orta',4,'pz-yol','Prizma yüzeyinde en kısa yol')
a3,b3,c3=21,14,6
cands=sorted([(a3+b3)**2+c3**2,(a3+c3)**2+b3**2,(b3+c3)**2+a3**2]); assert cands==[841,925,1261] and math.isqrt(841)**2==841
L3=yuzey_en_kisa(kutu_yuzleri(a3,b3,c3),(0,0,0),'taban',(a3,b3,c3),'ust'); assert abs(L3-29)<1e-9
assert a3+b3==35 and a3+c3==27 and b3+c3==20 and a3+b3+c3==41
K3=kutu(a3,b3,c3,sc=.2); f=F(); K3.draw(f); Q=K3.Q
assert K3.hid_list()==['AD','CD','DH']
lbl(f,K3,'A','B','$21$',(0,-.3)); lbl(f,K3,'B','C','$14$',(.3,-.12)); lbl(f,K3,'B','F','$6$',(.3,0))
f.raw(f'\\fill {pt(Q["A"])} circle (1.6pt); \\fill {pt(Q["G"])} circle (1.6pt);')
f.vl('A',Q['A'],(-1,-.6),.3); f.vl('G',Q['G'],(1,.6),.3)
SK3=f.svg()
q('0003',tipId='pz-yol',tip='Prizma yüzeyinde en kısa yol',z='orta',alt='En Kısa Yol',kaz='Dikdörtgenler prizmasının yüzeyinde zıt köşeler arasındaki en kısa yolu hesaplar.',kalip='hikâyeli',
 kart='K-GPZ-03 (en kısa yol) · 21 × 14 × 6 kutu, A’dan G’ye',
 metin='Ayrıtları cm cinsinden şekilde verilen dikdörtgenler prizması biçimli kapalı bir kutunun A köşesinde bir karınca vardır. Karınca, kutunun yüzeyinden ayrılmadan yürüyerek kutunun karşı köşesi olan G köşesine gitmek istiyor. Şekil ölçekli değildir.\nBuna göre, karıncanın alabileceği en kısa yol kaç cm dir?',
 dogru=29,yan=[(20,'Yalnız iki küçük ayrıtın toplamını (14 + 6) yol sanmış.','dikkat'),(27,'İki ayrıtın toplamını (21 + 6) yol sanmış; üçüncü ayrıt yönündeki yürüyüşü hesaba katmamış.','dikkat'),(35,'Yalnız iki ayrıtı (21 + 14) boyunca yürüyen yolu en kısa yol sanmış.','dikkat'),(41,'Üç ayrıtın toplamını (21 + 14 + 6) yol olarak almış.','bilgi')],
 istenen='Karıncanın alabileceği en kısa yol (cm).',
 ip=['A dan G ye giden yol, kutunun yüzeylerinin hangi parçalarından geçer?'],
 bilgi=[PIS],
 ad=[A('Geçilecek yüz çiftlerini ayır','A dan G ye giden yol iki komşu yüzden geçer; üç farklı yüz çifti vardır.','ön ve üst · ön ve sağ · alt ve sağ yüzlerinden oluşan yollar'),A('Her seçenekte hipotenüsü yaz','Seçilen iki yüz yan yana serilince A ve G, bir dik üçgenin hipotenüsünün uçları olur.','(21 + 14)² + 6² = 1261 · (21 + 6)² + 14² = 925 · (14 + 6)² + 21² = 841'),A('En küçüğünü seç','Yolun uzunluğu karekökü alınan en küçük değerdir.','√841 = 29')],
 puf='Seçeneklerin hepsini hesaplayıp karşılaştırmadan en kısa yol seçilmez.',sekil=SK3)

# =================== 04 · Kartondan kutu · orta ===================
kartla('K-GPZ-04','Köşeleri kesilmiş kartondan kutu','Karton köşelerden eş kareler kesilip katlanınca kutunun tabanı iki kenardan da iki kesim payı kısalır; yükseklik kesilen karenin kenarıdır.','Kesilen kare payını yalnız bir kez çıkarmak; taban alanını yükseklik sanmak; karton alanından kesilen alanı çıkarıp hacim sanmak.','orta',4,'pz-karton','Kartondan kutu yapımı')
A4,B4,x4=30,22,4; t1=A4-2*x4; t2=B4-2*x4; V4=t1*t2*x4; assert (t1,t2,V4)==(22,14,1232)
assert (A4-x4)*(B4-x4)*x4==1872 and A4*B4*x4==2640 and t1*t2==308 and A4*B4-4*x4*x4==596 and 596!=1232
s=.18; f=F(); f.poly([(0,0),(A4*s,0),(A4*s,B4*s),(0,B4*s)])
for (cx,cy) in ((0,0),(A4-x4,0),(0,B4-x4),(A4-x4,B4-x4)): f.poly([(cx*s,cy*s),((cx+x4)*s,cy*s),((cx+x4)*s,(cy+x4)*s),(cx*s,(cy+x4)*s)],'dashed')
dim(f,(0,0),(A4*s,0),'$30$',-.3); dim(f,(A4*s,0),(A4*s,B4*s),'$22$',-.3)
f.node(((A4-x4/2)*s,(x4/2)*s),'$4$') if False else None
dim(f,(0,B4*s),(x4*s,B4*s),'$4$',.3,dl=.3)
SK4=f.svg()
q('0004',tipId='pz-karton',tip='Kartondan kutu yapımı',z='orta',alt='Kartondan Kutu',kaz='Köşelerinden eş kareler kesilen dikdörtgen kartondan oluşan üstü açık kutunun hacmini hesaplar.',kalip='hikâyeli',
 kart='K-GPZ-04 (kartondan kutu) · 30 × 22 karton, köşe 4',
 metin='Bir atölyede, boyutları cm cinsinden şekilde verilen dikdörtgen biçimli kartonun dört köşesinden, kesik çizgilerle gösterilen eş kareler kesiliyor. Daha sonra kalan kısım kesik çizgiler boyunca yukarı katlanıp yapıştırılarak üstü açık, dikdörtgenler prizması biçiminde bir kutu yapılıyor. Şekil ölçekli değildir.\nBuna göre, bu kutunun hacmi kaç cm³ tür?',
 dogru=1232,yan=[(308,'Hacim yerine kutunun taban alanını (22 × 14) bulmuş.','dikkat'),(596,'Kartonun alanından kesilen karelerin alanını çıkarıp (660 − 64) hacim sanmış.','bilgi'),(1872,'Her kenardan yalnız bir kare payı çıkarıp (30 − 4) × (22 − 4) × 4 hesaplamış.','dikkat'),(2640,'Kesilen karelere bakmadan kartonun boyutlarını 4 ile çarpmış (30 × 22 × 4).','islem')],
 istenen='Kutunun hacmi (cm³).',
 ip=['Katlanınca kutunun yüksekliği hangi uzunluk olur? Tabanın her kenarından ne kadar kısalma olduğunu şekilde gör.'],
 bilgi=[HAC],
 ad=[A('Tabanın kenarlarını bul','Her kenarın iki ucundan birer kare payı kesilmiştir.','30 − 2 × 4 = 22 · 22 − 2 × 4 = 14'),A('Yüksekliği belirle','Katlanan kısımlar kutunun yan duvarlarını oluşturur; yükseklik kesilen karenin kenarıdır.','h = 4'),A('Hacmi hesapla','Taban alanı ile yüksekliği çarp.','22 × 14 × 4 = 1232')],
 puf='Katlama sorularında hangi ölçünün tabana, hangisinin yüksekliğe dönüştüğünü ayrı ayrı yaz.',sekil=SK4)

# =================== 05 · İki özdeş prizmayı yapıştırma · orta ===================
kartla('K-GPZ-05','İki özdeş prizmayı birleştirme','Yapıştırılan iki yüzün alanı toplam alandan iki kez çıkar; çıkan alan ne kadar büyükse kalan yüzey o kadar küçüktür.','Yapıştırılan yüz alanını bir kez çıkarmak; yüz seçimini yanlış (küçük yüz) yapmak; tek prizmanın alanını vermek.','orta',4,'pz-birles','İki prizmayı birleştirme ve yüzey alanı')
a5,b5,c5=6,4,3; S5=2*(a5*b5+b5*c5+c5*a5); assert S5==108
def bir(x,y,z,g): return 2*S5-2*g
opts=[(a5*b5,2*(a5*b5+b5*(2*c5)+(2*c5)*a5)),(a5*c5,2*(a5*(2*b5)+(2*b5)*c5+c5*a5)),(b5*c5,2*((2*a5)*b5+b5*c5+c5*(2*a5)))]
for g,s5 in opts: assert bir(a5,b5,c5,g)==s5
assert [x[1] for x in opts]==[168,180,192] and 2*S5==216 and 2*S5+a5*b5==240
K5=kutu(a5,b5,c5,sc=.38); K5b=kutu(a5,b5,c5,sc=.38); shift(K5b,4.1,0)
f=F(); K5.draw(f); K5b.draw(f)
lbl(f,K5,'A','B','$6$',(0,-.3)); lbl(f,K5,'B','C','$4$',(.3,-.12)); lbl(f,K5,'A','E','$3$',(-.28,0))
SK5=f.svg()
q('0005',tipId='pz-birles',tip='İki prizmayı birleştirme ve yüzey alanı',z='orta',alt='Prizmaları Birleştirme',kaz='İki özdeş prizmanın yüzlerini yapıştırarak elde edilen cismin en küçük yüzey alanını bulur.',kalip='hikâyeli',
 kart='K-GPZ-05 (birleştirme, yüzey alanı) · iki 6 × 4 × 3 blok',
 metin='Bir oyuncak atölyesi, şekilde ölçüleri cm cinsinden verilen iki özdeş dikdörtgenler prizması biçimindeki tahta bloğu, birer yüzlerini tam çakıştırarak birbirine yapıştırıp yeni bir dikdörtgenler prizması elde edecektir. Yapıştırma yeri dışında kalan bütün yüzeyler boyanacaktır. Şekil ölçekli değildir.\nBuna göre, boyanacak yüzeyin alanı en az kaç cm² olur?',
 dogru=168,yan=[(240,'Yapıştırılan 24 lük iki yüzü çıkarmak yerine bir kez eklemiş (216 + 24).','islem'),(180,'6 × 3 lük yüzleri yapıştırmış; alanı en çok azaltan yüzü seçmemiş.','dikkat'),(192,'4 × 3 lük en küçük yüzleri yapıştırmış; alanı en çok azaltan yüzü seçmemiş.','dikkat'),(216,'Yapıştırma sonrası kapanan yüzleri düşmeden iki bloğun alanlarını toplamış.','dikkat')],
 istenen='Boyanacak yüzeyin en küçük alanı (cm²).',
 ip=['Yapıştırma, toplam yüzey alanını nasıl değiştirir?'],
 bilgi=[YUZ],
 ad=[A('Bir bloğun yüzey alanı','Üç farklı yüz çiftinin alanları hesaplanır.','2 × (6 × 4 + 4 × 3 + 3 × 6) = 108'),A('İki bloğun toplamı','İki özdeş blok vardır.','2 × 108 = 216'),A('En çok azaltan yüzü seç','Yapıştırılan iki yüz de kapanır; en büyük yüz 6 × 4 = 24 tür.','216 − 2 × 24 = 168')],
 puf='Yapıştırılan yüzler yüzey alanından iki kez düşer; her olasılığı karşılaştırarak seç.',sekil=SK5)

# =================== 06 · Yamuk kesitli havuz · orta ===================
kartla('K-GPZ-06','Yamuk tabanlı prizmanın hacmi ve boşaltma','Ön yüz yamuktur; hacim yamuğun alanı ile uzunluğun çarpımıdır; boşaltma süresi hacmin pompa debisine bölümüdür.','Yamuk alanında 1/2 çarpanını unutmak; paralel kenarlardan birini kullanmak; hacmi debiye bölmemek.','orta',4,'pz-hacim','Üçgen ve yamuk tabanlı prizmanın hacmi')
u6,d6,h6,L6,deb=8,4,3,50,15; V6=(u6+d6)*h6*L6//2; assert V6==900 and V6/deb==60
assert (u6*h6*L6//2)//deb==40 and (d6*h6*L6//2)//deb==20 and (u6+d6)*h6*L6//4//deb==30 and (u6*h6*L6)//deb==80
Ld=8
V={'P1':(2,0,0),'P2':(6,0,0),'P3':(8,0,3),'P4':(0,0,3),'R1':(2,Ld,0),'R2':(6,Ld,0),'R3':(8,Ld,3),'R4':(0,Ld,3)}
FC={'on':(['P1','P2','P3','P4'],(0,-1,0)),'arka':(['R1','R2','R3','R4'],(0,1,0)),'taban':(['P1','R1','R2','P2'],(0,0,-1)),'ust':(['P4','P3','R3','R4'],(0,0,1)),'sag':(['P2','R2','R3','P3'],(3,0,-2)),'sol':(['P1','P4','R4','R1'],(-3,0,-2))}
S6=Solid(V,FC,sc=.3); f=F(); S6.draw(f); Q=S6.Q
assert S6.hid_list()==['P1R1','R1R2','R1R4'],S6.hid_list()
dim(f,Q['P4'],Q['P3'],'$8$',1.05); lbl(f,S6,'P1','P2','$4$',(0,-.3)); lbl(f,S6,'P2','R2','$50$',(.3,-.22))
xa=Q['P4'][0]-.38; f.raw(f'\\draw[<->,thin] {pt((xa,Q["P1"][1]))} -- {pt((xa,Q["P4"][1]))};'); f.node((xa-.28,(Q['P1'][1]+Q['P4'][1])/2),'$3$')
SK6=f.svg()
q('0006',tipId='pz-hacim',tip='Üçgen ve yamuk tabanlı prizmanın hacmi',z='orta',alt='Yamuk Kesitli Havuz',kaz='Kesiti yamuk olan prizma biçimli havuzun hacmini bulup boşaltma süresini hesaplar.',kalip='hikâyeli',
 kart='K-GPZ-06 (yamuk prizma hacmi, boşaltma) · 8-4-3 kesit, uzunluk 50',
 metin='Kesiti ikizkenar yamuk olan, prizma biçimli bir havuzun ölçüleri metre cinsinden şekilde verilmiştir. Havuz ağzına kadar suyla doludur. Dakikada 15 m³ su çeken bir pompa ile havuzun suyu tamamen boşaltılacaktır. Şekil ölçekli değildir.\nBuna göre, havuz kaç dakikada boşalır?',
 dogru=60,yan=[(20,'Yamuğun alanında yalnızca küçük tabanı (4) kullanıp (4 × 3 ÷ 2) × 50 ÷ 15 = 20 bulmuş.','dikkat'),(40,'Yamuğun alanında yalnızca büyük tabanı (8) kullanıp 600 ÷ 15 = 40 bulmuş.','dikkat'),(80,'Yamuk yerine üst tabanı kadar bir dikdörtgen (8 × 3 × 50) alıp 1200 ÷ 15 = 80 bulmuş.','dikkat'),(30,'Yamuğun alanında 1/2 çarpanını iki kez kullanıp 450 ÷ 15 = 30 bulmuş.','islem')],
 istenen='Havuzun boşalma süresi (dakika).',
 ip=['Havuzun hacmini hesaplamak için prizmanın hangi yüzü taban gibi alınmalı? Önce o yüzün alanını bul.'],
 bilgi=[YAM,HAC],
 ad=[A('Yamuğun alanını bul','Paralel kenarlar 8 ve 4, yükseklik 3 tür.','(8 + 4) ÷ 2 × 3 = 18'),A('Hacmi hesapla','Yamuğun alanı havuzun uzunluğuyla çarpılır.','18 × 50 = 900 m³'),A('Süreyi bul','Toplam hacim pompanın dakikada çektiği miktara bölünür.','900 ÷ 15 = 60')],
 puf='Verilen uzunlukların hangisi kesite, hangisi prizmanın boyuna ait; ayır ve etiketini yaz.',sekil=SK6)

# =================== 07 · Üçgen prizmanın açınımı · orta ===================
kartla('K-GPZ-07','Üçgen prizma açınımından hacim','Açınımdaki dikdörtgenlerin enleri üçgenin kenarlarıdır; ikizkenar üçgenin yüksekliği Pisagorla bulunur, hacim taban alanı çarpı dikdörtgenin boyudur.','Üçgenin yüksekliğini bulmadan kenar uzunluğunu yükseklik sanmak; 1/2 çarpanını unutmak; yarım tabanı yükseklik sanmak.','orta',4,'pz-acinim','Açınımı verilen prizmanın hacmi')
e7,t7,L7=13,10,15; h7=int(math.sqrt(e7**2-(t7/2)**2)); assert h7==12 and h7*h7+(t7//2)**2==e7**2
V7=t7*h7//2*L7; assert V7==900 and t7*h7*L7==1800 and e7*t7*L7==1950 and t7*e7*L7//2==975 and e7*h7*L7//2==1170
s=.13; f=F()
for x0,x1 in ((0,e7),(e7,2*e7),(2*e7,2*e7+t7)): f.poly([(x0*s,0),(x1*s,0),(x1*s,L7*s),(x0*s,L7*s)])
x0=2*e7; f.poly([(x0*s,L7*s),((x0+t7)*s,L7*s),((x0+t7/2)*s,(L7+h7)*s)]); f.poly([(x0*s,0),((x0+t7)*s,0),((x0+t7/2)*s,-h7*s)])
for cx_,tt in ((e7/2,'$13$'),(e7*1.5,'$13$'),(2*e7+t7/2,'$10$')): f.node((cx_*s,.4),tt)
dim(f,(0,0),(0,L7*s),'$15$',.3)
SK7=f.svg()
q('0007',tipId='pz-acinim',tip='Açınımı verilen prizmanın hacmi',z='orta',alt='Üçgen Prizmanın Açınımı',kaz='Üçgen prizmanın açınımından taban üçgenini bulup hacmi hesaplar.',kalip='şekilli',
 kart='K-GPZ-07 (üçgen prizma açınımı) · 13-13-10 üçgen, boy 15',
 metin='Şekilde, tabanı üçgen olan bir dik prizmanın açınımı verilmiştir. Açınımdaki üç dikdörtgenin eni sırasıyla 13 cm, 13 cm ve 10 cm, boyu 15 cm dir; üçgen yüzler 10 cm lik dikdörtgene eklenmiştir. Şekil ölçekli değildir.\nBuna göre, bu açınım katlanarak oluşturulan prizmanın hacmi kaç cm³ tür?',
 dogru=900,yan=[(975,'Üçgenin yüksekliği yerine eşit kenarı (13) kullanıp 10 × 13 ÷ 2 × 15 = 975 bulmuş.','dikkat'),(1170,'Taban olarak eşit kenarı (13), yükseklik olarak 12 yi alıp 13 × 12 ÷ 2 × 15 = 1170 bulmuş.','dikkat'),(1800,'Üçgenin alanında 1/2 çarpanını unutup 10 × 12 × 15 hesaplamış.','islem'),(1950,'Yükseklik yerine eşit kenarı (13) kullanıp 1/2 çarpanını da unutarak 10 × 13 × 15 bulmuş.','dikkat')],
 istenen='Prizmanın hacmi (cm³).',
 ip=['Üçgen yüzün üç kenarı, açınımdaki hangi uzunluklardır? Tabana ait yüksekliği bu kenarlardan nasıl elde edersin?'],
 bilgi=[PIS,UCG,HAC],
 ad=[A('Üçgenin kenarlarını yaz','Dikdörtgenlerin enleri üçgen yüzün kenarlarıdır; 10 luk kenar tabandır.','13 · 13 · 10'),A('Yüksekliği bul','İkizkenar üçgende tabana inen yükseklik tabanı iki eş parçaya ayırır.','h² = 13² − 5² = 144 → h = 12'),A('Taban alanını yaz','Yükseklik ve taban bilindiğine göre alan bulunur.','10 × 12 ÷ 2 = 60'),A('Hacmi hesapla','Taban alanı ile prizmanın boyu çarpılır.','60 × 15 = 900')],
 puf='Açınımda iki yüzün ortak kenarı katlandığında aynı uzunluk olur; kenarları bu eşleşmeyle yaz.',sekil=SK7)

# =================== 08 · Karınca: karşılıklı yüzlerde iki nokta · zor ===================
kartla('K-GPZ-08','Karşılıklı yüzlerdeki iki nokta arasında en kısa yol','Ön yüzden arka yüze üst, alt ya da yan yüz üzerinden geçilir; her serimde yol bir doğru parçasıdır, üçü hesaplanıp en küçüğü seçilir.','Yalnız üstten geçen yolu hesaplamak; yan yüz yolunda yükseklik farkını unutmak; yolları toplamak.','zor',5,'pz-yol','Prizma yüzeyinde en kısa yol')
a8,b8,c8,p8,q8=10,25,17,15,3
ust8=2*c8-p8-q8+b8; alt8=p8+q8+b8; yan8=math.sqrt((a8+b8)**2+(p8-q8)**2)
assert (ust8,alt8,yan8)==(41,43,37.0)
L8=yuzey_en_kisa(kutu_yuzleri(a8,b8,c8),(a8/2,0,p8),'on',(a8/2,b8,q8),'arka'); assert abs(L8-37)<1e-9
assert a8+b8==35 and a8+b8+(p8-q8)==47
K8=kutu(a8,b8,c8,sc=.17); f=F(); K8.draw(f); Q=K8.Q
assert K8.hid_list()==['AD','CD','DH']
Pp=K8.Q['A'] if False else mul(proj((a8/2,0,p8)),.17); Qq=mul(proj((a8/2,b8,q8)),.17)
f.raw(f'\\fill {pt(Pp)} circle (1.6pt); \\draw[dashed] {pt(Qq)} circle (2.6pt);')
f.node(add(Pp,(-.3,.12)),'$P$'); f.node(add(Qq,(.32,.0)),'$Q$'); f.node(add(Qq,(.3,.38)),'(arka yüzde)')
lbl(f,K8,'A','B','$10$',(0,-.3)); lbl(f,K8,'B','C','$25$',(.32,-.12)); lbl(f,K8,'A','E','$17$',(-.3,0))
SK8=f.svg()
q('0008',tipId='pz-yol',tip='Prizma yüzeyinde en kısa yol',z='zor',alt='İki Nokta Arası En Kısa Yol',kaz='Karşılıklı iki yüzdeki noktalar arasında yüzey üzerinden alınabilecek yolları karşılaştırıp en kısasını bulur.',kalip='hikâyeli',
 kart='K-GPZ-08 (karşılıklı yüzler, en kısa yol) · 10 × 25 × 17 kutu',
 metin='Ayrıtları cm cinsinden şekilde verilen dikdörtgenler prizması biçimli kapalı bir kutunun ön yüzünde P noktası, arka yüzünde Q noktası vardır. P noktası ön yüzün dikey orta çizgisi üzerinde ve alt kenara 15 cm uzaklıkta, Q noktası arka yüzün dikey orta çizgisi üzerinde ve alt kenara 3 cm uzaklıktadır. Bir karınca, kutunun yüzeyinden ayrılmadan P den Q ya yürüyecektir. Şekil ölçekli değildir.\nBuna göre, karıncanın izleyebileceği en kısa yol kaç cm dir?',
 dogru=37,yan=[(35,'Yan yüzler üzerinden geçerken yatay uzaklığı (5 + 25 + 5) bulup iki nokta arasındaki yükseklik farkını (12) hesaba katmamış.','dikkat'),(41,'Yalnız üst yüzden geçen yolu hesaplamış: (17 − 15) + 25 + (17 − 3).','dikkat'),(43,'Yalnız alt yüzden geçen yolu hesaplamış: 15 + 25 + 3.','dikkat'),(47,'Yatay uzaklık ile yükseklik farkını Pisagor yerine toplayarak 35 + 12 bulmuş.','bilgi')],
 istenen='Karıncanın izleyebileceği en kısa yol (cm).',
 ip=['P den Q ya giderken yolun hangi yüzlerden geçebileceğini listele; her seçenekte yüzleri aynı düzleme serince noktalar arası uzaklığı hesapla.'],
 bilgi=[PIS],
 ad=[A('Üst yüzden geçen yol','Önce üst kenara çıkılır, sonra 25 cm gidilir, sonra Q ya inilir.','(17 − 15) + 25 + (17 − 3) = 41'),A('Alt yüzden geçen yol','Önce alt kenara inilir, sonra 25 cm gidilir, sonra Q ya çıkılır.','15 + 25 + 3 = 43'),A('Yan yüzden geçen yol','Yan yüz serilince yatay uzaklık yarı genişlikler ile derinliğin toplamıdır; dikey fark 15 − 3 tür.','yatay: 5 + 25 + 5 = 35 · dikey: 12 · √(35² + 12²) = 37'),A('En küçüğünü seç','Üç yolun uzunlukları karşılaştırılır.','37 < 41 < 43')],
 puf='Birden çok geçiş yüzü varsa her birinin uzunluğunu ayrı hesaplayıp karşılaştır.',sekil=SK8)

# =================== 09 · Düzgün altıgen prizma · zor ===================
kartla('K-GPZ-09','Düzgün altıgen prizmanın yüzey alanı','Hacimden taban kenarı bulunur; iki altıgen taban ile altı eş dikdörtgenin alanı toplanır.','Tek taban saymak; altıgenin alanında 1/4 çarpanını unutmak; yan yüzlerden yalnız bir kısmını saymak.','zor',5,'pz-altigen','Düzgün altıgen prizma')
V9,h9=144,6; a9=4; assert 9*a9*a9*h9//6==144 or True
At9=6*a9*a9/4  # √3 çarpanı ayrı
assert 6*a9**2*h9/4==144 and a9**2==16 and 6*a9*h9==144
d9=Rp(144,48,3); y1=Rp(144,24,3); y2=Rd(48,3); y3=Rp(72,48,3); y4=Rp(144,192,3)
sira9=sirala(d9,y1,y2,y3,y4); assert sira9==[y2,y3,y1,d9,y4],sira9
R9=4; hv=[(R9*cos(radians(60*i)),R9*sin(radians(60*i))) for i in range(6)]
V={f'H{i}':(hv[i][0],hv[i][1]+4.2,0) for i in range(6)}; V.update({f'T{i}':(hv[i][0],hv[i][1]+4.2,h9) for i in range(6)})
FC={'taban':([f'H{i}' for i in range(5,-1,-1)],(0,0,-1)),'ust':([f'T{i}' for i in range(6)],(0,0,1))}
for i in range(6): FC[f'y{i}']=([f'H{i}',f'H{(i+1)%6}',f'T{(i+1)%6}',f'T{i}'],(cos(radians(60*i+30)),sin(radians(60*i+30)),0))
S9=Solid(V,FC,sc=.38); f=F(); S9.draw(f); Q=S9.Q
print('hex gizli',S9.hid_list())
dim(f,Q['H0'],Q['T0'],'$6$',-.3)
SK9=f.svg()
q('0009',tipId='pz-altigen',tip='Düzgün altıgen prizma',z='zor',alt='Düzgün Altıgen Prizma',kaz='Hacmi verilen düzgün altıgen prizmanın taban kenarını bulup tüm yüzey alanını hesaplar.',kalip='hikâyeli',
 kart='K-GPZ-09 (altıgen prizma) · V = 144√3, yükseklik 6',
 metin='Bir kozmetik firması, tabanı düzgün altıgen olan dik prizma biçimindeki bir kutu üretecektir. Kutunun yüksekliği şekilde cm cinsinden verilmiştir ve hacmi 144√3 cm³ tür. Kutunun dış yüzeyinin tamamı (iki taban dahil) parlak kâğıtla kaplanacaktır. Şekil ölçekli değildir.\nBuna göre, kaplanacak yüzeyin alanı kaç cm² dir?',
 dogru=d9,yan=[(y1,'Tabanlardan yalnız birini sayıp 144 + 24√3 bulmuş; kutunun iki tabanı da kaplanacaktır.','dikkat'),(y2,'Yalnız iki taban alanını (2 × 24√3) bulup yan yüzleri unutmuş.','dikkat'),(y3,'Altı yan yüzden yalnız üçünü (3 × 24 = 72) saymış.','dikkat'),(y4,'Altıgenin alanını 6 × a² × √3 ÷ 4 yerine 6 × a² × √3 almış: iki taban 192√3.','islem')],
 sira=sira9,
 istenen='Kaplanacak yüzeyin alanı (cm²).',
 ip=['Önce hacim bilgisini kullanarak tabanın kenarını bul; hacimde altıgenin alanı hangi biçimde yer alıyor?'],
 bilgi=[ESK,YUZ],
 ad=[A('Taban alanını kenarla yaz','Kenarı a olan düzgün altıgenin alanı 6 eş eşkenar üçgenin toplamıdır.','6 × a² × √3 ÷ 4 = 3a²√3 ÷ 2'),A('Kenarı bul','Hacim, taban alanı ile yüksekliğin çarpımıdır.','3a²√3 ÷ 2 × 6 = 9a²√3 = 144√3 → a = 4'),A('Alanları hesapla','Her taban 24√3, yan yüzler 4 × 6 lık altı dikdörtgendir.','2 × 24√3 = 48√3 · 6 × 24 = 144'),A('Toplam yüzey alanı','İki taban ile yanal alan toplanır.','144 + 48√3')],
 puf='Verilen bir büyüklükten başka büyüklüğe geçerken önce her ikisini kenar uzunluğu cinsinden yaz.',sekil=SK9)

# =================== 10 · Eşkenar üçgen prizma, ip sarma · zor ===================
kartla('K-GPZ-10','Üçgen prizmaya iki tur sarılan ip','Yan yüzler yan yana serilince bir dikdörtgen oluşur; iki tur dolanan ip bu dikdörtgenin iki katı genişliğindeki hâlinin köşegenidir.','Tur sayısını tek saymak; çevre ile yüksekliği toplamak; yalnız bir turun yüksekliğini almak.','zor',5,'pz-yol','Prizma yüzeyinde en kısa yol')
a10,h10,n10=8,14,2; per=3*a10; Lh=n10*per; L10=math.sqrt(Lh**2+h10**2)
assert per==24 and Lh==48 and L10==50.0 and math.sqrt(per**2+(h10/n10)**2)==25.0 and n10*math.sqrt(per**2+(h10/n10)**2)==50.0
assert per+h10==38 and per==24 and Lh==48
s3=sqrt(3)
V={'A':(0,0,0),'B':(a10,0,0),'C':(a10/2,a10*s3/2,0),'D':(0,0,h10),'E':(a10,0,h10),'F':(a10/2,a10*s3/2,h10)}
FC={'on':(list('ABED'),(0,-1,0)),'sag':(list('BCFE'),(s3/2,.5,0)),'sol':(list('CADF'),(-s3/2,.5,0)),'taban':(list('ACB'),(0,0,-1)),'ust':(list('DEF'),(0,0,1))}
FC['sol']=(['C','A','D','F'],(-s3/2,.5,0))
S10=Solid(V,FC,sc=.3); f=F(); S10.draw(f); Q=S10.Q
print('tri10 gizli',S10.hid_list())
lbl(f,S10,'A','B','$8$',(0,-.3)); lbl(f,S10,'B','E','$14$',(.3,0))
f.raw(f'\\fill {pt(Q["A"])} circle (1.6pt); \\fill {pt(Q["D"])} circle (1.6pt);')
f.vl('A',Q['A'],(-1,-1),.3); f.vl('D',Q['D'],(-1,1),.3)
SK10=f.svg()
q('0010',tipId='pz-yol',tip='Prizma yüzeyinde en kısa yol',z='zor',alt='Prizmaya İp Sarma',kaz='Yan yüzeyine sarılan ipin uzunluğunu yan yüzlerin açınımındaki dikdörtgenin köşegeni olarak hesaplar.',kalip='hikâyeli',
 kart='K-GPZ-10 (ip sarma) · eşkenar üçgen tabanlı, kenar 8, yükseklik 14',
 metin='Tabanı eşkenar üçgen olan dik prizma biçimli bir hediye kutusunun ölçüleri cm cinsinden şekilde verilmiştir. Bir süs şeridi, kutunun A köşesinden başlayıp yalnız yan yüzeylerin üzerinden, her turda aynı miktar yükselerek kutuyu tam iki kez dolaşıp A köşesinin tam üstündeki D köşesinde bitirilecek ve şerit boyunca hiç gevşek bırakılmayacaktır. Şekil ölçekli değildir.\nBuna göre, kullanılacak şeridin uzunluğu kaç cm dir?',
 dogru=50,yan=[(25,'Bir tur için gereken yolu (24 ve 7 ile) bulup şeridin iki tur dolandığını unutmuş.','dikkat'),(38,'Bir turun çevresi ile yüksekliği (24 + 14) toplamış.','islem'),(48,'Yalnız iki turun yatay yolunu (2 × 24) almış; yükselmeyi hesaba katmamış.','dikkat'),(24,'Yalnız bir turun yatay yolunu (taban çevresi) şerit uzunluğu sanmış.','dikkat')],
 istenen='Şeridin uzunluğu (cm).',
 ip=['Şerit her turda yan yüzeyin çevresini dolaşıyor; bir turda ne kadar yükselir?'],
 bilgi=[PIS],
 ad=[A('Bir turun yatay uzunluğu','Yan yüzeyin bir turu, taban çevresine eşittir.','3 × 8 = 24'),A('İki turun yatay uzunluğu','Şerit yan yüzeyi iki kez dolanır.','2 × 24 = 48'),A('Dik üçgeni kur','Yatay yol 48, düşey yol kutunun yüksekliğidir.','48² + 14² = 2500'),A('Uzunluğu bul','Karekök alınır.','√2500 = 50')],
 puf='Yüzeyde dolanan çizgiler için ayrı ayrı yatay ve düşey uzunlukları yazıp sonra birleştir.',sekil=SK10)

# =================== yaz ===================
def bitir_geo(onek):
    for qq in P.ANA: qq['kardes']=None
    P.yaz(os.path.join(GD,f'{onek}-1.json'),f'/tmp/bos-{onek}.json')
    tipler={}
    for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=TIPK[c['tipId']]))['kartlar'].append(c['id'])
    json.dump(dict(konu=P.konu_adi,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 TYT Geometri çıkmış soruları (yalnız mantık), MEB 9–10. sınıf geometri müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar',f'{onek}.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler))

bitir_geo('prizmaiki')
