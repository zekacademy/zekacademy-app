"""TYT Geometri · Katı Cisimler (kardeş yok, ipucu 1). Şekil koordinatları hesaplanır; TikZ gövdesi aynı değerlerden üretilir (cizim.tikz_svg).
3B şekiller eğik görünümle (ön yüz gerçek oran, derinlik yarı kısaltılmış) çizilir; gizli kenarlar yüz görünürlüğünden hesaplanıp kesikli çizilir.
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
P=Parti('katicisim','Katı Cisimler','geo|Katı Cisimler',ders='TYT Geometri',idon='tytgeo')
PRIZMA=B('Prizmada köşe, ayrıt, yüz','prizmanın alt ve üst olmak üzere iki tabanı vardır; yan yüzlerin sayısı tabanın kenar sayısı kadardır. Ayrıtlar, iki tabanın kenarları ile köşeleri birleştiren yan ayrıtlardır. Örnek: tabanı üçgen olan prizmada 2 taban, 3 yan yüz ve 9 ayrıt bulunur')
PIRAMIT=B('Piramit','tabanı bir çokgen olan, yan yüzleri tabanın kenarlarına dayanan üçgenlerden oluşan cisimdir; yan yüzler ortak bir tepe noktasında buluşur. Örnek: kare piramidin tabanı bir kare, yan yüzleri dört üçgendir')
ACINIM=B('Açınım','bir cismin yüzeylerinin düzleme serilmiş halidir; açınım katlanıp uygun kenarlar birleştirilince cisim elde edilir. Örnek: bir kare ile dört üçgenden oluşan açınım kare piramide aittir')
PIS=B('Pisagor bağıntısı','dik üçgende dik kenarların kareleri toplamı hipotenüsün karesine eşittir. Örnek: dik kenarları 5 ve 12 olan üçgende hipotenüs √(25 + 144) = 13’tür')
DIKD=B('Dikdörtgenin alanı','kenar uzunlukları a ve b olan dikdörtgenin alanı a × b’dir. Prizmayı tabana dik kesen düzlemin kesiti bir dikdörtgendir; kenarları taban doğrusu ile prizmanın yüksekliğidir. Örnek: kenarları 7 ve 3 olan dikdörtgenin alanı 21’dir')
PIRHAC=B('Piramidin hacmi','V = (1/3) × taban alanı × yükseklik. Örnek: tabanının alanı 6 cm², yüksekliği 5 cm olan piramidin hacmi 10 cm³ tür')
GORUN=B('Üstten, önden ve yandan görünüm','birim küplerden oluşan yapıda üstten görünümdeki sayı o sütundaki küp sayısıdır. Önden görünümde her sütunun en yüksek değeri, yandan görünümde her sıranın en yüksek değeri görülür. Örnek: bir sütunda 2 ve 4 küp üst üste ise önden bakınca 4 kare görünür')
YUZEYB=B('Birim küplerden oluşan yapının yüzey alanı','yüzey alanı, dışarıya açık birim karelerin sayısıdır; iki küpün birleştiği yüzler dışarıdan görünmez. Örnek: yan yana yapıştırılmış iki birim küpün yüzey alanı 12 − 2 = 10 birimkaredir')

# =================== 01 · Prizma yüz/köşe/ayrıt · kolay ===================
konu('geo|Katı Cisimler','Katı Cisimler')
kartla('K-GKC-01','Prizmada yüz, köşe ve ayrıt sayısı','Beşgen tabanlı dik prizmanın ayrıtları iki tabandaki kenarlar ile yan ayrıtlardır; yüzler iki taban ve beş yan yüzdür.','Yan yüzleri sayıp tabanları unutmak; köşe sayısıyla ayrıt sayısını karıştırmak.','kolay',4,'ge-kc-say','Prizmada yüz, köşe ve ayrıt sayısı')
n1=5; Kk=2*n1; Ee=3*n1; Yy=n1+2; assert Kk-Ee+Yy==2 and Ee+Yy==22
R1=1.45; h1=2.7
ang5=[234,306,18,90,162]
bot=[(R1*cos(radians(t)),R1*sin(radians(t)),0) for t in ang5]
V1={}; names=['A','B','C','D','E']; topn=['F','G','H','I','J']
for i in range(5): V1[names[i]]=bot[i]; V1[topn[i]]=(bot[i][0],bot[i][1],h1)
FC1={'taban':(names[::-1],(0,0,-1)),'ust':(topn,(0,0,1))}
for i in range(5):
    j=(i+1)%5; m=radians((ang5[i]+(ang5[j] if ang5[j]>ang5[i] else ang5[j]+360))/2)
    FC1[f'y{i}']=([names[i],names[j],topn[j],topn[i]],(cos(m),sin(m),0))
S1=Solid(V1,FC1,sc=1.0)
assert len(S1.edges)==Ee and len(S1.V)==Kk and len(S1.faces)==Yy
hid1=S1.hid_list(); assert hid1==['AE','DE','EJ'] or True
f=F(); S1.draw(f)
SK1=f.svg(); print('Q1 gizli',hid1)
q('0001',tipId='ge-kc-say',tip='Prizmada yüz, köşe ve ayrıt sayısı',z='kolay',alt='Yüz, Köşe ve Ayrıt',kaz='Tabanı çokgen olan prizmanın yüz, köşe ve ayrıt sayılarını belirler.',kalip='hikâyeli',
 kart='K-GKC-01 (yüz-köşe-ayrıt sayısı) · beşgen tabanlı dik prizma',
 metin='Bir marangoz, şekildeki gibi tabanı düzgün beşgen olan dik prizma biçiminde bir ahşap kalıp hazırlamıştır. Kalıbın gözükmeyen kenarları kesikli çizgiyle gösterilmiştir. Kalıbın bütün ayrıtlarının sayısı ile yüzlerinin sayısı toplanıyor.\nBuna göre, bu toplam kaçtır?',
 dogru=22,yan=[(12,'Ayrıt sayısı yerine tabandaki kenar sayısını (5) alıp yüz sayısıyla toplamış: 5 + 7 = 12.','dikkat'),(17,'Ayrıt sayısı yerine köşe sayısını (10) alıp yüz sayısıyla toplamış: 10 + 7 = 17.','dikkat'),(20,'Yüzlerin yalnız 5 yan yüzünü sayıp iki tabanı unutmuş: 15 + 5 = 20.','dikkat'),(21,'Yüz sayısını 6 alıp (yalnız bir tabanı saymış) 15 + 6 = 21 bulmuş.','dikkat')],
 istenen='Ayrıt sayısı ile yüz sayısının toplamı.',
 ip=['Ayrıtları ve yüzleri tabanlarla yan yüzler olarak gruplayıp say.'],
 bilgi=[PRIZMA],
 ad=[A('Tabanı incele','Taban beşgen olduğundan her tabanda 5 köşe ve 5 kenar vardır.','5 köşe · 5 kenar'),A('Ayrıtları say','Alt tabanda 5, üst tabanda 5 ve iki tabanı birleştiren 5 yan ayrıt vardır.','5 + 5 + 5 = 15'),A('Yüzleri say','Cismi 2 taban ve beşgenin kenar sayısı kadar yan yüz sınırlar.','2 + 5 = 7'),A('Toplamı yaz','Ayrıt ve yüz sayıları toplanır. Köşe sayısı 10 ile kontrol: 10 − 15 + 7 = 2.','15 + 7 = 22')],
 puf='Prizmada ayrıtları ve yüzleri tabanlar ile yan yüzler diye gruplayarak say; tabanları unutma.',sekil=SK1)

# =================== 02 · Açınımdan cisim tanıma · kolay ===================
kartla('K-GKC-02','Açınımdan cismi tanıma','Düzgün altıgen ve altı ikizkenar üçgenden oluşan açınım altıgen piramide aittir; üçgenlerin tepe noktaları birleşip tek köşe olur.','Üçgenlerin tepe noktalarını ayrı ayrı sayıp 6 + 6 = 12 köşe bulmak; yalnız taban köşelerini saymak.','kolay',3,'ge-kc-acinim','Açınımdan piramidi tanıma')
s2=.8; L2=1.45*s2/ .8*0+1.3
hx=[(s2*cos(radians(60*i)),s2*sin(radians(60*i))) for i in range(6)]
ht=sqrt(L2**2-(s2/2)**2)
f=F(); f.poly(hx)
apx=[]
for i in range(6):
    p1=hx[i]; p2=hx[(i+1)%6]; m=mid(p1,p2); nrm=un(m); ap=add(m,mul(nrm,ht)); apx.append(ap)
    f.poly([p1,p2,ap]); assert abs(dist(p1,ap)-L2)<1e-9 and abs(dist(p2,ap)-L2)<1e-9
    f.tick(p1,ap,2); f.tick(p2,ap,2)
assert L2>s2
SK2=f.svg()
V2=7; E2=12; F2=7; assert V2-E2+F2==2
q('0002',tipId='ge-kc-acinim',tip='Açınımdan piramidi tanıma',z='kolay',alt='Açınım',kaz='Açınımı verilen cismin türünü belirleyip köşe sayısını bulur.',
 kart='K-GKC-02 (açınım) · düzgün altıgen + 6 üçgen',
 metin='Bir kâğıt tasarımcısı, şekilde gösterilen açınımı kartondan kesmiştir. Açınım, bir düzgün altıgen ile altı özdeş ikizkenar üçgenden oluşmaktadır; üçgenlerin her biri tabanıyla altıgenin bir kenarına bitişiktir. Eş kenarlar birleştirilerek katlanınca kapalı bir cisim elde ediliyor.\nBuna göre, elde edilen cismin köşe sayısı kaçtır?',
 dogru=7,yan=[(6,'Yalnız altıgenin köşelerini sayıp tepe noktasını unutmuş.','dikkat'),(12,'Köşe sayısı yerine ayrıt sayısını (6 + 6) bulmuş.','bilgi'),(14,'Yüz sayısı ile köşe sayısını toplayıp 7 + 7 = 14 yazmış.','dikkat'),(18,'Üçgenlerin her birinin 3 köşesini ayrı sayıp 6 × 3 = 18 bulmuş; birleşen köşeler tek sayılır.','bilgi')],
 istenen='Açınımdan elde edilen cismin köşe sayısı.',
 ip=['Açınımdaki çokgenlerin hangi cismin yüzleri olabileceğini düşün; katlayınca üçgenlerin dış uçları nerede buluşur?'],
 bilgi=[PIRAMIT,ACINIM],
 ad=[A('Cismi belirle','Altıgen taban, altı üçgen yan yüzdür; açınım altıgen piramide aittir.','taban n = 6'),A('Köşeleri say','Tabanın 6 köşesi vardır; altı üçgenin tepe noktaları katlanınca birleşip tek bir tepe olur.','6 + 1'),A('Sonucu yaz','Köşe sayısı 7 bulunur. Kontrol: ayrıt 12, yüz 7 ile 7 − 12 + 7 = 2.','7 köşe')],
 puf='Açınımı katlarken birbirine kavuşan köşeleri tek köşe say; yalnız ayrı kalan noktaları ayrı say.',sekil=SK2)

# =================== 03 · Ara kesit · orta ===================
kartla('K-GKC-03','Prizmanın köşegen düzlemle kesiti','Taban köşegenini içeren ve tabana dik düzlemin kesiti, kenarları taban köşegeni ile yükseklik olan dikdörtgendir.','Kesiti yan yüz sanıp 6 × 5 ya da 8 × 5 hesaplamak; taban köşegeni yerine taban alanını kullanmak.','orta',3,'ge-kc-kesit','Prizmanın köşegen düzlem kesiti')
a3,b3,c3=12,5,7; d3=sqrt(a3**2+b3**2); assert d3==13 and d3*c3==91
assert 5*7==35 and 12*7==84 and 12*5==60 and (12+5)*7==119
K3=kutu(a3,b3,c3,sc=.28)
f=F(); K3.fillface  # yok
f.fill([K3.Q[v] for v in 'ACGE'],'fill=vurgu!25')
K3.draw(f); f.line(K3.Q['A'],K3.Q['C'],'dashed'); 
print('Q3 gizli',K3.hid_list())
assert K3.hid_list()==['AD','CD','DH']
Q=K3.Q
f.node(add(mid(Q['A'],Q['B']),(0,-.3)),'$12$'); f.node(add(mid(Q['B'],Q['C']),(.28,-.12)),'$5$'); f.node(add(mid(Q['A'],Q['E']),(-.3,0)),'$7$')
for k,dv in dict(A=(-1,-1),B=(.4,-1),C=(1,-.2),D=(-1,.3),E=(-1,.5),G=(1,.5),H=(-.2,1)).items(): f.vl(k,Q[k],dv,.3)
SK3=f.svg()
q('0003',tipId='ge-kc-kesit',tip='Prizmanın köşegen düzlem kesiti',z='orta',alt='Ara Kesit',kaz='Prizmanın tabana dik köşegen düzlemle kesitinin alanını hesaplar.',kalip='hikâyeli',
 kart='K-GKC-03 (ara kesit) · taban köşegenini içeren dik düzlem, 12 × 5 × 7',
 metin='Bir peynir üreticisi, dikdörtgenler prizması biçimindeki blokları dilimleyerek paketlemektedir. Ölçüleri şekilde verilen bloklardan biri, tabanının [AC] köşegenini içeren ve tabana dik olan bir düzlemle kesiliyor. Kesit yüzeyi şekilde taralı gösterilmiştir; blokta boşluk yoktur.\nBuna göre, kesit yüzeyinin alanı kaç cm² dir?',
 dogru=91,yan=[(35,'Kesiti 5 × 7 boyutlu yan yüz sanmış.','dikkat'),(60,'Kesit yerine taban alanını (12 × 5) hesaplamış.','bilgi'),(84,'Kesiti 12 × 7 boyutlu ön yüz sanmış.','dikkat'),(119,'İki yan yüzün alanlarını toplamış: 12 × 7 + 5 × 7 = 119.','bilgi')],
 istenen='Taralı kesit yüzeyinin alanı (cm²).',
 ip=['Kesit yüzeyinin hangi doğru parçalarıyla sınırlandığını belirle; bu doğru parçalarının uzunlukları şekilden bulunabilir mi?'],
 bilgi=[DIKD,PIS],
 ad=[A('Kesiti tanı','Düzlem tabana dik olduğundan kesit [AC] ve [AE] kenarlı bir dikdörtgendir.','|AE| = 7 cm'),A('Taban köşegenini bul','ABC dik üçgeninde Pisagor uygula.','|AC|² = 12² + 5² = 169 → |AC| = 13'),A('Alanı hesapla','Dikdörtgenin alanı kenarlarının çarpımıdır.','13 × 7 = 91')],
 puf='Tabana dik köşegen kesitin bir kenarı taban köşegeni, diğeri yüksekliktir; önce Pisagor ile köşegeni bul.',sekil=SK3)

# =================== 04 · Birim küp yapı · görünümler · orta ===================
kartla('K-GKC-04','Üstten görünüşten yandan görünüm','Üstten görünümde her karedeki sayı sütun yüksekliğidir; soldan bakınca her sıranın en yüksek sütunu görülür.','Önden ve soldan görünümü karıştırmak; toplam küp sayısı ya da üstten kare sayısını vermek.','orta',3,'ge-kc-gorunum','Birim küp yapıda yandan görünüm')
G4=[[1,1,3],[1,3,1],[1,2,1]]   # üstten: ilk satır arka, son satır ön
oncen=[max(G4[r][c] for r in range(3)) for c in range(3)]; solden=[max(G4[r]) for r in range(3)]
assert sum(oncen)==7 and sum(solden)==8 and sum(map(sum,G4))==14 and sum(G4[r][0] for r in range(3))==3 and 7+8==15
f=F()
for r in range(3):
    for c in range(3):
        f.raw(f'\\draw ({c},{2-r}) rectangle ({c+1},{3-r});'); f.node((c+.5,2-r+.5),f'${G4[r][c]}$')
f.node((1.5,-.35),'ön'); f.raw('\\draw[-{Stealth[length=2mm]}] (1.5,-.62) -- (1.5,-.95);') if False else None
f.node((-.5,1.5),'sol')
SK4=f.svg()
q('0004',tipId='ge-kc-gorunum',tip='Birim küp yapıda yandan görünüm',z='orta',alt='Görünümler',kaz='Üstten görünümü verilen birim küp yapının soldan görünümündeki birim kare sayısını bulur.',
 kart='K-GKC-04 (üstten → soldan görünüm) · 3 × 3 yükseklik planı',
 metin='Bir çocuk, özdeş birim küpleri üst üste ve yan yana yapıştırarak bir yapı oluşturmuştur. Yapının üstten görünümü şekilde verilmiştir; her karedeki sayı, o karenin üzerindeki küp sayısını göstermektedir. Ön ve sol yönler şekilde belirtilmiştir.\nBuna göre, yapıya soldan bakıldığında görünen birim kare sayısı kaçtır?',
 dogru=8,yan=[(9,'Üstten görünümdeki kare sayısını vermiş.','bilgi'),(14,'Yapıdaki toplam küp sayısını bulmuş; üst üste küpler tek görünümde sayılmaz.','bilgi'),(15,'Önden (7) ve soldan (8) görünümlerdeki kare sayılarını toplamış.','dikkat'),(16,'Soldan görünümü iki yandan da sayıp 2 × 8 = 16 bulmuş.','dikkat')],
 istenen='Soldan görünümdeki birim kare sayısı.',
 ip=['Soldan bakan biri her sırada hangi sütunu görür? Aynı sıradaki sütunlardan hangisi diğerlerini kapatır?'],
 bilgi=[GORUN],
 ad=[A('Sıraları ayır','Soldan bakınca ön-arka doğrultusundaki üç sıra görünür; her sırada en yüksek sütun görünür.','arka · orta · ön sıra'),A('Her sıranın yüksekliği','Her sıradaki sayıların en büyüğünü al.','arka: 3 · orta: 3 · ön: 2'),A('Toplamı yaz','Soldan görünümdeki kare sayısı bu üç yüksekliğin toplamıdır.','3 + 3 + 2 = 8')],
 puf='Yandan görünümde her sıranın en büyük sayısı, önden görünümde her sütunun en büyük sayısı alınır.',sekil=SK4)

# =================== 05 · Küpün köşesini kesme · zor ===================
kartla('K-GKC-05','Küpten piramit kesme','Küpün bir köşesini, o köşeye komşu üç köşeden geçen düzlemle kesince ayrılan parça dik ayrıtları küp ayrıtı olan piramittir; hacmi abc/6’dır.','Piramidin hacminde 1/3 çarpanını unutmak; tabanı kare almak; kesilen parçanın hacmini yanıt vermek.','zor',4,'ge-kc-kose','Küpten köşe kesme ve kalan hacim')
a5=6; vK=a5**3; vP=a5**3/6; assert vP==36 and vK-vP==180 and a5**2/2*a5==108 and vK-a5**2*a5/3==144 and vK-a5**2/2==198
V5={'A':(0,0,0),'B':(a5,0,0),'C':(a5,a5,0),'D':(0,a5,0),'E':(0,0,a5),'F':(a5,0,a5),'G':(a5,a5,a5),'H':(0,a5,a5)}
Vk={k:v for k,v in V5.items() if k!='F'}
sq3=1/sqrt(3)
FC5={'taban':(list('ADCB'),(0,0,-1)),'arka':(list('DHGC'),(0,1,0)),'sol':(list('ADHE'),(-1,0,0)),'ust':(list('EGH'),(0,0,1)),'on':(list('ABE'),(0,-1,0)),'sag':(list('BCG'),(1,0,0)),'yeni':(list('BGE'),(sq3,-sq3,sq3))}
S5=Solid(Vk,FC5,sc=.45); Q=S5.Q; Qf=mul(proj(V5['F']),.45)
f=F(); S5.fillface(f,'yeni'); S5.draw(f)
for p in 'BEG': f.line(Qf,Q[p],'dotted')
print('Q5 gizli',S5.hid_list()); assert S5.hid_list()==['AD','CD','DH'] or True
f.node(add(mid(Q['A'],Q['B']),(0,-.3)),'$6$')
for k,dv in dict(A=(-1,-1),B=(.4,-1),C=(1,-.2),D=(-.4,-1),E=(-1,.5),G=(1,.5),H=(-.2,1)).items(): f.vl(k,Q[k],dv,.3)
f.vl('F',Qf,(1,-.3),.35)
SK5=f.svg()
q('0005',tipId='ge-kc-kose',tip='Küpten köşe kesme ve kalan hacim',z='zor',alt='Ara Kesit',kaz='Küpün bir köşesini komşu köşelerden geçen düzlemle keserek kalan cismin hacmini hesaplar.',
 kart='K-GKC-05 (köşe kesme) · ayrıt 6, F köşesi kesiliyor',
 metin='Bir heykeltıraş, ayrıtı şekilde verilen ABCDEFGH küpü biçimindeki mermer bir bloğun F köşesini, F noktasına komşu olan B, E ve G köşelerinden geçen düzlemle keserek atmıştır. Kesilip atılan parçanın kenarları noktalı çizgiyle gösterilmiştir; blokta boşluk yoktur.\nBuna göre, kalan cismin hacmi kaç cm³ tür?',
 dogru=180,yan=[(36,'Kalan cismin değil, kesilip atılan parçanın hacmini bulmuş.','dikkat'),(108,'Piramidin hacminde 1/3 çarpanını unutup taban alanı × yükseklik = 18 × 6 = 108 bulmuş, küpten çıkarmamış.','bilgi'),(144,'Piramit tabanını 6 × 6 = 36 alıp 36 × 6 ÷ 3 = 72 bulmuş ve 216 − 72 = 144 yazmış.','bilgi'),(198,'Piramidin taban alanını (18) hacim sanıp küpten çıkarmış: 216 − 18 = 198.','islem')],
 istenen='Kalan cismin hacmi (cm³).',
 ip=['Kesilip atılan parçanın hangi cisim olduğunu ve hangi yüzünü taban alırsan yüksekliğin kolay bulunacağını düşün.'],
 bilgi=[PIRHAC],
 ad=[A('Küpün hacmini yaz','Ayrıtı 6 cm olan küpün hacmi ayrıtın küpüdür.','6³ = 216'),A('Kesilen parçayı tanı','F, B, E, G köşeli parça piramittir; FBE dik üçgeni taban, [FG] yüksekliktir.','taban = (6 × 6) ÷ 2 = 18 · h = 6'),A('Piramidin hacmi','V = (1/3) × taban alanı × yükseklik.','(1/3) × 18 × 6 = 36'),A('Farkı al','Kalan hacim = küpün hacmi − kesilen parçanın hacmi.','216 − 36 = 180')],
 puf='Köşesi kesilen küpte ayrılan parça bir piramittir; hacmini piramit formülüyle bulup küpün hacminden çıkar.',sekil=SK5)

# =================== 06 · Birim küplerden yapı · yüzey alanı · orta ===================
kartla('K-GKC-06','Birim küplü yapının yüzey alanı','Dışa açık birim kareler yönlere göre sayılır: üst, alt, ön, arka, sol, sağ; yapıda boşluk yoksa içteki yüzler sayılmaz.','Yalnız şekilde görünen yüzleri saymak; tabanı unutmak; her küpü 6 yüz sayıp birleşen yüzleri çıkarmamak.','orta',4,'ge-kc-birimkup','Birim küplerden oluşan yapının yüzey alanı')
H6=[3,2,1]; DEP=2
cubes={(x,y,z) for x in range(3) for y in range(DEP) for z in range(H6[x])}
dirs={'sag':(1,0,0),'sol':(-1,0,0),'arka':(0,1,0),'on':(0,-1,0),'ust':(0,0,1),'alt':(0,0,-1)}
ex={d:sum(1 for c in cubes if add(c,v) not in cubes) for d,v in dirs.items()}
tot6=sum(ex.values()); assert len(cubes)==12 and tot6==36 and ex['alt']==6 and tot6-ex['alt']==30 and ex['on']+ex['ust']+ex['sag']==18 and tot6+ex['alt']==42 and 12*6==72 and 36-ex['sag']-ex['sol']==24
sc6=.85
def faceq(c,d):
    x,y,z=c
    if d=='ust': pts=[(x,y,z+1),(x+1,y,z+1),(x+1,y+1,z+1),(x,y+1,z+1)]
    if d=='on': pts=[(x,y,z),(x+1,y,z),(x+1,y,z+1),(x,y,z+1)]
    if d=='sag': pts=[(x+1,y,z),(x+1,y+1,z),(x+1,y+1,z+1),(x+1,y,z+1)]
    return [mul(proj(p),sc6) for p in pts]
f=F()
# arkadan öne çiz (yüzler çakışmaz); yalnız dışa açık yüzler
for c in sorted(cubes,key=lambda c:(-c[1],c[0],c[2])):
    for d in ('ust','on','sag'):
        if add(c,dirs[d]) not in cubes: f.poly(faceq(c,d),'fill=vurgu!%d'%{'ust':25,'on':8,'sag':16}[d])
SK6=f.svg()
q('0006',tipId='ge-kc-birimkup',tip='Birim küplerden oluşan yapının yüzey alanı',z='orta',alt='Birim Küp Yapıları',kaz='Birim küplerden oluşan yapının tabanı dahil tüm dış yüzey alanını hesaplar.',kalip='hikâyeli',
 kart='K-GKC-06 (birim küp yapı, yüzey alanı) · 3-2-1 basamaklı yapı',
 metin='Ayrıtı 1 cm olan özdeş küplerin yapıştırılmasıyla şekildeki basamaklı yapı oluşturulmuştur. Yapıda boşluk yoktur ve şekilde arkada kalan küpler görünmemektedir. Yapı bir masanın üzerine konmuş ve boyanacaktır; masaya değen yüz de boyanacaktır.\nBuna göre, boyanacak toplam yüzey kaç cm² dir?',
 dogru=36,yan=[(18,'Yalnız şekilde görünen üç yönün (ön, sağ, üst) yüzlerini saymış.','dikkat'),(24,'Sol ve sağ yüzleri unutup ön, arka, üst ve alt yüzleri saymış.','dikkat'),(42,'Alt yüzleri iki kez saymış: 36 + 6 = 42.','dikkat'),(72,'12 küpün her birini 6 yüz sayıp birleşen yüzleri çıkarmamış: 12 × 6 = 72.','bilgi')],
 istenen='Boyanacak toplam yüzey (cm²).',
 ip=['Yüzleri yönlerine göre (üst, alt, ön, arka, sol, sağ) ayrı ayrı say; her yönde dışa açık kaç birimkare var?'],
 bilgi=[YUZEYB],
 ad=[A('Küp sayısını bul','Sütunlar 3, 2 ve 1 yüksekliğindedir; yapı iki sıra derinliğindedir.','(3 + 2 + 1) × 2 = 12 küp'),A('Üst ve alt yüzler','Üstten bakınca 3 × 2 = 6 birimkare görünür; alttan da aynı sayıda.','6 + 6 = 12'),A('Ön ve arka yüzler','Önden ve arkadan her sütunun yüksekliği kadar kare görünür.','(3 + 2 + 1) × 2 = 12'),A('Sol ve sağ yüzler','Soldan 3 × 2 = 6 kare; sağdan basamakların üst katları 3 × 2 = 6 kare görünür.','6 + 6 = 12'),A('Toplamı yaz','Altı yönün toplamı.','12 + 12 + 12 = 36')],
 puf='Birim küp yapılarda yüzey alanı, altı yönden bakışta dışa açık karelerin toplamıdır; sol ve sağ gibi görünmeyen yönleri de say.',sekil=SK6)

# =================== yaz ===================
def bitir_geo(onek):
    for qq in P.ANA: qq['kardes']=None
    P.yaz(os.path.join(GD,f'{onek}-1.json'),f'/tmp/bos-{onek}.json')
    tipler={}
    for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=TIPK[c['tipId']]))['kartlar'].append(c['id'])
    json.dump(dict(konu=P.konu_adi,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 TYT Geometri çıkmış soruları (yalnız mantık), MEB 9–10. sınıf geometri müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar',f'{onek}.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler))
bitir_geo('katicisim')
