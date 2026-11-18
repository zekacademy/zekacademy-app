"""TYT Geometri · Çokgenler II (iç/dış açılar, düzgün çokgen). Şekil koordinatları hesaplanır; her cevap ve çeldirici assert edilir."""
import sys,os,math,json
from fractions import Fraction as Fr
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
HV=os.path.join(GD,'..')
from math import sin,cos,tan,radians,degrees,atan2,sqrt,pi
TIPK={}   # tipId -> uygulama konu anahtarı
def konu(k,ad): P.k=k; P.konu_adi=ad; H.KONU=ad
def kartla(id,alt,fikir,tuzak,z,adim,tipId,tip,kaynak=None):
    kart(id,alt,fikir,tuzak,z,'şekilli',adim,tipId,tip,kaynak or 'ÖSYM 2018–2026 TYT Geometri soruları (yalnız mantık) · MEB 9–10. sınıf geometri'); TIPK[tipId]=P.k
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),kalip='şekilli',**k)

# ---------------- çizim yardımcıları (cm cinsinden koordinatlar) ----------------
def add(p,q_): return (p[0]+q_[0],p[1]+q_[1])
def sub(p,q_): return (p[0]-q_[0],p[1]-q_[1])
def mul(p,s): return (p[0]*s,p[1]*s)
def ln(p): return math.hypot(*p)
def un(p): n=ln(p); return (p[0]/n,p[1]/n)
def mid(p,q_): return ((p[0]+q_[0])/2,(p[1]+q_[1])/2)
def lerp(p,q_,t): return (p[0]+(q_[0]-p[0])*t,p[1]+(q_[1]-p[1])*t)
def dist(p,q_): return ln(sub(p,q_))
def cen(ps): return (sum(p[0] for p in ps)/len(ps),sum(p[1] for p in ps)/len(ps))
def pt(p): return f'({p[0]:.3f},{p[1]:.3f})'
def ang(V,a,b):
    u=sub(a,V); v=sub(b,V); return degrees(math.acos((u[0]*v[0]+u[1]*v[1])/(ln(u)*ln(v))))
def alan(ps): return abs(sum(ps[i][0]*ps[(i+1)%len(ps)][1]-ps[(i+1)%len(ps)][0]*ps[i][1] for i in range(len(ps))))/2
class F:
    def __init__(s): s.o=[]
    def raw(s,t): s.o.append(t)
    def line(s,p,q_,st=''): s.o.append(f'\\draw[{st}] {pt(p)} -- {pt(q_)};')
    def poly(s,ps,st=''): s.o.append(f'\\draw[{st}] '+' -- '.join(map(pt,ps))+' -- cycle;')
    def fill(s,ps,st='fill=vurgu!25'): s.o.append(f'\\fill[{st}] '+' -- '.join(map(pt,ps))+' -- cycle;')
    def node(s,p,t,st=''): s.o.append(f'\\node[{st}] at {pt(p)} {{{t}}};')
    def vl(s,t,p,dv,d=.3): s.node(add(p,mul(un(dv),d)),f'${t}$')       # köşe harfi: dv yönünde dışarıda
    def sl(s,t,p,q_,ic,d=.3):                                           # kenar uzunluğu: kenar ortasında, ic noktasının tersi tarafta
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
    def par(s,p,q_):
        m=mid(p,q_); e=un(sub(q_,p)); s.o.append(f'\\draw[-{{Stealth[length=1.9mm,width=1.7mm]}}] {pt(sub(m,mul(e,.07)))} -- {pt(add(m,mul(e,.07)))};')
    def body(s): return '\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'+'\n'.join(s.o)+'\n\\end{tikzpicture}'
    def svg(s): return tikz_svg(s.body())

def reg(n,R,rot=0,c=(0,0)): return [(c[0]+R*cos(radians(rot+360*i/n)),c[1]+R*sin(radians(rot+360*i/n))) for i in range(n)]
def konveks(ps):
    n=len(ps); z=[(ps[(i+1)%n][0]-ps[i][0])*(ps[(i+2)%n][1]-ps[(i+1)%n][1])-(ps[(i+1)%n][1]-ps[i][1])*(ps[(i+2)%n][0]-ps[(i+1)%n][0]) for i in range(n)]
    return all(x>0 for x in z) or all(x<0 for x in z)
def kes(p1,p2,p3,p4):
    x1,y1=p1;x2,y2=p2;x3,y3=p3;x4,y4=p4; d=(x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
    return (((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4))/d,((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4))/d)

P=Parti('cokgeniki','Çokgenler','geo|Çokgenler',ders='TYT Geometri',idon='tytgeo')
def q(no,kalip='şekilli',**k): mk(P,no,adim=len(k['ad']),kalip=kalip,**k)
konu('geo|Çokgenler','Çokgenler')
ICTOP=B('İç ve dış açılar','n kenarlı konveks çokgenin iç açıları toplamı (n − 2) × 180° dir; dış açıları toplamı 360° dir. Bir iç açı ile komşu dış açının toplamı 180° dir. Örnek: yedigenin iç açıları toplamı 5 × 180° = 900°')
DUZ=B('Düzgün çokgen','tüm kenarları ve tüm açıları eşit olan çokgendir. n kenarlı düzgün çokgenin bir dış açısı 360° ÷ n, bir iç açısı 180° − 360° ÷ n dir. Örnek: düzgün sekizgende dış açı 45°, iç açı 135° dir')
IKIZ=B('İkizkenar üçgen','eş kenarların karşısındaki açılar eşittir; üçgenin iç açıları toplamı 180° dir. Örnek: tepe açısı 40° olan ikizkenar üçgenin taban açıları 70° şer derecedir')
ESKU=B('Eşkenar üçgen','üç kenarı eşit, üç açısı 60° dir. Örnek: bir kenarı 5 cm olan eşkenar üçgenin çevresi 15 cm dir')
TAM=B('Bir noktanın çevresindeki açılar','bir noktanın etrafındaki açıların toplamı 360° dir. Örnek: bir noktada birleşen 100°, 120° ve 140° lik üç açı aralarında boşluk bırakmaz')
def build(ext,Ls):
    """ext[i]: i. köşedeki dış açı (derece); Ls: ilk n−2 kenar. Son iki kenar kapanıştan çözülür. Köşeler V0..V(n-1); kenar i: V_i→V_(i+1)."""
    n=len(ext); assert abs(sum(ext)-360)<1e-9
    dirs=[0]
    for i in range(1,n): dirs.append(dirs[-1]+ext[i])
    u=[(cos(radians(d)),sin(radians(d))) for d in dirs]
    sx=-sum(Ls[i]*u[i][0] for i in range(n-2)); sy=-sum(Ls[i]*u[i][1] for i in range(n-2))
    det=u[n-2][0]*u[n-1][1]-u[n-2][1]*u[n-1][0]; La=(sx*u[n-1][1]-sy*u[n-1][0])/det; Lb=(u[n-2][0]*sy-u[n-2][1]*sx)/det; assert La>0 and Lb>0
    L=list(Ls)+[La,Lb]; V=[(0,0)]
    for i in range(n-1): V.append((V[-1][0]+L[i]*u[i][0],V[-1][1]+L[i]*u[i][1]))
    assert konveks(V) and dist(V[-1],V[0])-L[-1]<1e-9
    for i in range(n): assert abs(ang(V[i],V[(i-1)%n],V[(i+1)%n])-(180-ext[i]))<1e-6
    return V,dirs
def dis_ok(f,V,dirs,i,lab,r=.42,lr=.8,ln_=.7,ex_st='thin'):
    """i. köşede dış açı: önceki kenarın uzantısı ile sonraki kenar arasındaki yay."""
    n=len(V); p=dirs[(i-1)%n]; ex=(V[i][0]+ln_*cos(radians(p)),V[i][1]+ln_*sin(radians(p)))
    f.line(V[i],ex,ex_st); nxt=V[(i+1)%n]
    f.arc(V[i],ex,nxt,r,lab,lr)
def harf(f,V,dirs,names,d=.3):
    """köşe harfi: dış tarafta, önceki kenarın sağ tarafındaki 180° lik bölgede (dış açı yayıyla çakışmaz)."""
    n=len(V)
    for i,nm in enumerate(names):
        p=dirs[(i-1)%n]-90; f.node((V[i][0]+d*cos(radians(p)),V[i][1]+d*sin(radians(p))),f'${nm}$')

# =================== 01 · Dörtgende dış açılar · kolay ===================
kartla('K-GCZ-01','Dış açılardan iç açı','Konveks çokgende dış açıların toplamı 360° dir; eksik dış açı bulunup 180° den çıkarılarak iç açı elde edilir.','Dış açıyı iç açı sanmak; üç dış açının toplamını cevap yazmak; iç açıları toplayıp 360° den çıkarmayı iç–dış karıştırarak yapmak.','kolay',3,'cz-ic-dis','Çokgende iç ve dış açılar')
e1=[80,95,70,115]; assert sum(e1)==360 and 360-(80+95+70)==115 and 180-115==65
assert 180-80==100 and (180-80)+(180-95)+(180-70)==295 and 80+95+70==245
V1,d1=build(e1,[3.2,2.6]); f=F(); f.poly(V1)
for i,t in enumerate(('$80^\\circ$','$95^\\circ$','$70^\\circ$')): dis_ok(f,V1,d1,i,t)
f.arc(V1[3],V1[2],V1[0],.5,'$x$',.82)
harf(f,V1,d1,'ABCD')
SK=f.svg()
q('0001',kalip='hikâyeli',tipId='cz-ic-dis',tip='Çokgende iç ve dış açılar',z='kolay',alt='Dış Açılardan İç Açı',kaz='Dörtgenin üç dış açısı verilince dış açıların toplamından kalan köşedeki iç açıyı bulur.',
 kart='K-GCZ-01 (dış açı toplamı) · dörtgen, dış açılar 80°, 95°, 70°',
 metin='Bir belediye, ABCD konveks dörtgeni biçimindeki bir parselin sınır doğrularını A, B ve C köşelerinde uzatarak şekildeki dış açıları ölçmüştür. Parselin D köşesindeki iç açının ölçüsü x ile gösterilmiştir. Şekil ölçekli değildir.\nBuna göre, x kaç derecedir?',
 dogru=65,yan=[(100,'A köşesinin iç açısını (180° − 80°) bulup istenen köşeyi karıştırmış.','dikkat'),(115,'D köşesinin dış açısını (360° − 245°) bulmuş; iç açıya geçmemiş.','dikkat'),(245,'Verilen üç dış açının toplamını cevap yazmış.','islem'),(295,'Üç köşedeki iç açıların toplamını (100° + 85° + 110°) cevap yazmış.','bilgi')],
 istenen='x = D köşesindeki iç açının ölçüsü (derece).',
 ip=['Şekilde işaretli açıların hangileri iç, hangileri dış açı? İstenen köşedeki açıyı hangi bilgiden elde edebilirsin?'],
 bilgi=[ICTOP],
 ad=[A('Dış açılar toplamını yaz','Konveks çokgenin dış açılarının toplamı 360° dir.','80° + 95° + 70° + dD = 360°'),A('D nin dış açısını bul','Verilen üç dış açı toplamdan çıkarılır.','dD = 360° − 245° = 115°'),A('İç açıya geç','İç açı ile komşu dış açının toplamı 180° dir.','x = 180° − 115° = 65°')],
 puf='Şekilde işaretlenen her açının iç mi dış mı olduğunu belirleyip ona göre yaz.',sekil=SK)

# =================== 02 · Düzgün ongen · kolay ===================
kartla('K-GCZ-02','Düzgün ongende köşegen ile kenar arasındaki açı','Düzgün çokgende iki komşu kenar ve onları birleştiren köşegen ikizkenar üçgen oluşturur; taban açıları iç açıdan bulunur.','Dış açıyı ya da iç açıyı cevap sanmak; taban açısını tepe açısından ayırt edememek.','kolay',3,'cz-duzgun-kosegen','Düzgün çokgende köşegen açıları')
n2=10; ic2=180-360//n2; x2=(180-ic2)//2; assert ic2==144 and x2==18 and 360//n2==36 and (180-120)//2==30 and 2*36==72
R2=2.6; Pv=reg(n2,R2,90+18); nm='ABCDEFGHIJ'; ic=(0,0)
assert abs(ang(Pv[0],Pv[1],Pv[2])-18)<1e-9 and abs(ang(Pv[1],Pv[0],Pv[2])-144)<1e-9
f=F(); f.poly(Pv); f.line(Pv[0],Pv[2]); f.arc(Pv[0],Pv[1],Pv[2],.5,'$x$',.8)
for i,n_ in enumerate(nm): f.vl(n_,Pv[i],Pv[i],.32)
SK=f.svg()
q('0002',kalip='hikâyeli',tipId='cz-duzgun-kosegen',tip='Düzgün çokgende köşegen açıları',z='kolay',alt='Düzgün Ongen',kaz='Düzgün ongende iç açıyı ve ikizkenar üçgenin taban açısını kullanarak köşegenle kenar arasındaki açıyı bulur.',
 kart='K-GCZ-02 (düzgün çokgen) · ongen, m(BAC)',
 metin='Bir mimar, düzgün ongen biçimli bir kulenin taban planını şekildeki gibi çizmiş ve ABCDEFGHIJ ongeninin A ile C köşelerini bir [AC] doğru parçasıyla birleştirmiştir. Şekil ölçekli değildir.\nBuna göre, x = m(BAC) kaç derecedir?',
 dogru=18,yan=[(30,'Kenar sayısını 6 alıp altıgenin iç açısından (180° − 120°) ÷ 2 = 30° bulmuş.','bilgi'),(36,'Düzgün ongenin bir dış açısını (360° ÷ 10) cevap yazmış.','dikkat'),(72,'İki dış açıyı toplamış (36° + 36°).','dikkat'),(144,'Düzgün ongenin bir iç açısını cevap yazmış.','dikkat')],
 istenen='x = m(BAC) açısının ölçüsü (derece).',
 ip=['A, B ve C köşelerini birleştirince oluşan üçgenin hangi kenarları eşit? Tepe açısını çokgenin açılarından nasıl elde edersin?'],
 bilgi=[DUZ,IKIZ],
 ad=[A('Dış ve iç açıyı bul','Düzgün ongenin bir dış açısı 360° ÷ 10 dur.','dış açı 36° → iç açı 180° − 36° = 144°'),A('Üçgeni belirle','ABC üçgeninde |AB| = |BC| olduğundan m(BAC) = m(BCA) dır; tepe açısı B dedir.','m(ABC) = 144°'),A('Taban açısını bul','Taban açıları toplamı 180° − 144° = 36° dir.','x = 36° ÷ 2 = 18°')],
 puf='Düzgün çokgende komşu kenar çiftleri ikizkenar üçgen oluşturur; tepe açısı çokgenin bir iç açısıdır.',sekil=SK)

# =================== 03 · Yıldızın uç açıları · orta ===================
kartla('K-GCZ-03','Beş köşeli yıldızın uç açıları','Yıldızın uçlarındaki beş açının toplamı sabittir; bilinen dört açı toplamdan çıkarılır.','Uç açılarının toplamını 360° ya da 540° sanmak; beş açıyı eşit saymak; toplamı cevap yazmak.','orta',4,'cz-yildiz','Beş köşeli yıldızın uç açıları')
t3=[38,42,28,32]; x3=180-sum(t3); assert x3==40 and sum(t3)==140
tips=t3+[x3]; s3_=[t+180 for t in tips]
al=[Fr(s3_[i]-s3_[(i+1)%5]+s3_[(i+2)%5]-s3_[(i+3)%5]+s3_[(i+4)%5],2) for i in range(5)]
assert al==[106,112,110,98,114] and sum(al)==540 and all(al[i]+al[(i+1)%5]==s3_[i] for i in range(5))
ext3=[180-a for a in al]; V3,d3=build(ext3,[2.0,2.0,2.2])
def lcross(p1,p2,p3,p4): return kes(p1,p2,p3,p4)
T=[lcross(V3[(i-1)%5],V3[i],V3[(i+1)%5],V3[(i+2)%5]) for i in range(5)]
for i in range(5): assert abs(ang(T[i],V3[i],V3[(i+1)%5])-tips[i])<1e-6,(i,ang(T[i],V3[i],V3[(i+1)%5]))
c3=cen(T); f=F()
for i in range(5): f.line(T[(i-1)%5],T[(i+1)%5])
labs=['$38^\\circ$','$42^\\circ$','$28^\\circ$','$32^\\circ$','$x$']
for i in range(5):
    f.arc(T[i],V3[i],V3[(i+1)%5],.5,labs[i],1.3)
for i,nm_ in enumerate('ABCDE'): f.vl(nm_,T[i],sub(T[i],c3),.3)
SK=f.svg()
assert 180//5==36 and 540-140==400 and 360-140==220
q('0003',kalip='hikâyeli',tipId='cz-yildiz',tip='Beş köşeli yıldızın uç açıları',z='orta',alt='Yıldızın Uç Açıları',kaz='Beş köşeli yıldızın uç açılarının toplamını kullanarak bilinmeyen uç açıyı bulur.',
 kart='K-GCZ-03 (yıldız) · uç açılar 38°, 42°, 28°, 32°',
 metin='Bir sanatçı, şekildeki yıldız desenini beş doğru parçasıyla çizmiştir. Yıldızın A, B, C, D ve E uç köşelerindeki açılarından dördünün ölçüsü verilmiştir; E köşesindeki açının ölçüsü x tir. Şekil ölçekli değildir.\nBuna göre, x kaç derecedir?',
 dogru=40,yan=[(36,'Beş uç açısını eşit sayıp 180° ÷ 5 = 36° bulmuş.','dikkat'),(140,'Verilen dört açının toplamını cevap yazmış.','islem'),(220,'Uç açıları toplamını 360° alıp 360° − 140° = 220° bulmuş.','bilgi'),(400,'Uç açıları toplamını 540° alıp 540° − 140° = 400° bulmuş.','bilgi')],
 istenen='x = m(E) açısının ölçüsü (derece).',
 ip=['Yıldızın içinde oluşan beşgenin köşelerini ve uçlardaki üçgenlerin açılarını düşün; uç açıları ile beşgenin açıları arasında nasıl bir ilişki kurarsın?'],
 bilgi=[ICTOP],
 ad=[A('Uç açıyı iç beşgenle ilişkilendir','Her uç açı, ucun üçgeninde iki dış açının 180° den çıkarılmasıyla bulunur; üçgenlerin taban açıları iç beşgenin dış açılarıdır.','uç açısı = 180° − (dış açı + dış açı)'),A('Beş uç için topla','Beş üçgenin açı toplamından, iç beşgenin dış açılarının iki kez sayıldığı çıkarılır.','toplam = 5 × 180° − 2 × 360° = 180°'),A('Bilinmeyeni bul','Verilen dört uç açısı toplamdan çıkarılır.','x = 180° − (38° + 42° + 28° + 32°) = 40°')],
 puf='Uçlardaki üçgenlerin açılarını ayrı ayrı yaz; ortak (iç beşgenin dış açıları) terimleri sadeleştir.',sekil=SK)

# =================== 04 · Kare ve düzgün beşgen · orta ===================
kartla('K-GCZ-04','Ortak kenarlı kare ve düzgün beşgen','Ortak köşedeki iç açılar çıkarılınca kalan açı bulunur; eş kenarlı ikizkenar üçgenin taban açılarından hedef açı elde edilir.','Köşedeki açıyı 360° den iki iç açı çıkarmadan kullanmak; ikizkenar üçgenin tepe açısını taban açısı sanmak; açının bir tarafını diğerine karıştırmak.','orta',5,'cz-birlesim','Ortak kenarlı çokgenler')
s4=1.5; A_=(0,0); B_=(s4,0); Cq=(s4,s4); Dq=(0,s4)
Pent=[A_,B_]; hd=0   # pentagon aşağıda: B→E→F→G→A saat yönünde
pv=[A_,B_]
for k in range(3):
    hd-=72; pv.append((pv[-1][0]+s4*cos(radians(hd)),pv[-1][1]+s4*sin(radians(hd))))
E_,F_,G_=pv[2],pv[3],pv[4]; assert abs(dist(G_,A_)-s4)<1e-9
assert abs(ang(A_,B_,G_)-108)<1e-9 and abs(ang(A_,Dq,B_)-90)<1e-9
assert abs(ang(A_,Dq,G_)-(360-90-108))<1e-9 and abs(ang(Dq,A_,G_)-9)<1e-9
x4=ang(Dq,Cq,G_); assert abs(x4-99)<1e-6,x4
assert 90-9==81 and 90+9==99 and 2*9==18
f=F(); f.poly([A_,B_,Cq,Dq]); f.poly(pv); f.line(Dq,G_); f.arc(Dq,Cq,G_,.5,'$x$',.8)
f.node((A_[0]+.3,A_[1]-.28),'$A$'); f.vl('B',B_,(1,.3),.3); f.vl('C',Cq,(1,1),.3); f.vl('D',Dq,(-1,1),.3)
f.vl('E',E_,(1,-.3),.3); f.vl('F',F_,(0,-1),.3); f.vl('G',G_,(-1,-.5),.3)
SK=f.svg()
q('0004',kalip='hikâyeli',tipId='cz-birlesim',tip='Ortak kenarlı çokgenler',z='orta',alt='Kare ve Beşgen',kaz='Ortak kenarlı kare ve düzgün beşgende köşedeki açıdan ikizkenar üçgenin açılarını bulur.',
 kart='K-GCZ-04 (kare + düzgün beşgen) · ortak kenar AB, m(CDG)',
 metin='Bir cam sanatçısı, şekildeki ABCD kare biçimli ve ABEFG düzgün beşgen biçimli iki camı ortak [AB] kenarı boyunca, farklı taraflara gelecek biçimde birleştirmiş ve D ile G noktaları arasına bir çubuk takmıştır. Şekil ölçekli değildir.\nBuna göre, x = m(CDG) kaç derecedir?',
 dogru=99,yan=[(9,'Yalnız ikizkenar üçgenin taban açısını (m(ADG)) bulup x e geçmemiş.','dikkat'),(18,'Tepe açısını 180° den çıkarıp (180° − 162°) taban açısına bölmemiş.','islem'),(81,'m(ADG) yi 90° den çıkarmış; G noktası [DA] nın C ye göre diğer tarafında olduğundan 9° eklenmelidir.','dikkat'),(90,'D deki açıyı karenin köşe açısı (90°) sanmış; DG doğrusunun etkisini unutmuş.','dikkat')],
 istenen='x = m(CDG) açısının ölçüsü (derece).',
 ip=['A köşesinde hangi açılar bir araya geliyor? DAG açısını bulduktan sonra, DAG üçgeninin kenarları arasında nasıl bir ilişki var?'],
 bilgi=[DUZ,IKIZ],
 ad=[A('A daki açıyı bul','A noktası etrafındaki açılar toplamı 360° dir; kare ve beşgenin iç açıları çıkarılır.','m(DAG) = 360° − 90° − 108° = 162°'),A('Üçgenin taban açısı','|AD| = |AG| olduğundan DAG ikizkenar üçgendir.','m(ADG) = (180° − 162°) ÷ 2 = 9°'),A('x i hesapla','CDA açısı 90° dir ve G, DA nın C ye göre diğer tarafındadır; açılar toplanır.','x = 90° + 9° = 99°')],
 puf='Ortak köşede birleşen şekillerin açılarını çevirerek bir noktanın etrafındaki toplam 360° ile ilişkilendir.',sekil=SK)

# =================== 05 · Dönerek yürüyen robot · orta ===================
kartla('K-GCZ-05','Her köşede sabit açıyla dönerek yürüme','Sabit açıyla dönerek başlangıca dönen yol düzgün çokgendir; dönüş açısı dış açıdır, kenar sayısı 360° ye bölünerek, çevre kenar sayısı çarpı kenarla bulunur.','Dönüş açısını iç açı sanmak; yalnız kenar sayısını cevap yazmak; çarpma yerine bölme yapmak.','orta',4,'cz-yol','Dönüşlerle çizilen çokgen yol')
a5,L5=40,6; n5=360//a5; assert n5==9 and 360%a5==0 and n5*L5==54 and 8*L5==48 and 10*L5==60 and L5*a5==240
Ls=1.5; hd=0; pv=[(0,0)]; hs=[0]
for k in range(3): pv.append((pv[-1][0]+Ls*cos(radians(hd)),pv[-1][1]+Ls*sin(radians(hd)))); hs.append(hd+a5); hd+=a5
f=F(); f.poly(pv[:2]) if False else None
for i in range(3): f.line(pv[i],pv[i+1])
nx=add(pv[3],(.7*cos(radians(hd)),.7*sin(radians(hd)))); f.line(pv[3],nx,'dashed')
for i in (1,2):
    p=hs[i-1]; ex=(pv[i][0]+.7*cos(radians(p)),pv[i][1]+.7*sin(radians(p))); f.line(pv[i],ex,'dashed'); f.arc(pv[i],ex,pv[i+1],.42,'$40^\\circ$',.95)
f.raw(f'\\fill {pt(pv[0])} circle (1.6pt);'); f.node((-.3,-.25),'$A$'); f.node(((pv[0][0]+pv[1][0])/2,-.3),'$6$')
f.raw(f'\\draw[->] {pt(pv[0])} -- {pt((.01,0))};') if False else None
SK=f.svg()
q('0005',kalip='hikâyeli',tipId='cz-yol',tip='Dönüşlerle çizilen çokgen yol',z='orta',alt='Dönerek Yürüme',kaz='Her köşede sabit açıyla dönen yolun kenar sayısını dış açıdan bulup toplam uzunluğu hesaplar.',
 kart='K-GCZ-05 (dönüş açısı, çevre) · 40° dönüş, kenar 6 m',
 metin='Bir tarım robotu, A noktasından yola çıkarak her biri 6 m uzunluğunda doğru parçaları boyunca ilerlemektedir. Robot, her parçanın sonunda şekildeki gibi aynı yönde 40° dönüp yeni parçaya geçmekte ve bu işi, ilk kez A noktasına geri gelinceye kadar sürdürmektedir. Şekilde yolun yalnız ilk parçaları gösterilmiştir.\nBuna göre, robotun A dan çıkıp A ya geri dönene kadar aldığı toplam yol kaç metredir?',
 dogru=54,yan=[(9,'Yalnız kenar sayısını (360° ÷ 40°) bulup kenar uzunluğuyla çarpmamış.','dikkat'),(48,'Kenar sayısını 8 bulmuş.','dikkat'),(60,'Kenar sayısını 10 bulmuş.','dikkat'),(240,'Kenar sayısını bulmak yerine dönüş açısı ile kenar uzunluğunu çarpmış (40 × 6).','islem')],
 istenen='Robotun aldığı toplam yol (m).',
 ip=['Her dönüşte yön 40° değişiyor; robotun yönü toplamda ne kadar değiştiğinde ilk konumuna ve ilk yönüne döner?'],
 bilgi=[ICTOP],
 ad=[A('Yolun biçimini belirle','Robot her köşede aynı açıyla döndüğünden izlenen yol düzgün çokgendir; dönüş açısı çokgenin dış açısıdır.','dış açı = 40°'),A('Kenar sayısını bul','Dış açılar toplamı 360° olduğundan kenar sayısı 360° ÷ dış açıdır.','n = 360° ÷ 40° = 9'),A('Toplam yolu hesapla','Her kenar 6 m olan 9 kenarın uzunlukları toplanır.','9 × 6 = 54')],
 puf='Şekilde verilen açının iç mi dış mı olduğunu belirleyip yolun biçimini düşün.',sekil=SK)

# =================== 06 · Köşede buluşan kare, altıgen ve düzgün çokgen · orta ===================
kartla('K-GCZ-06','Bir köşede boşluksuz birleşen çokgenler','Bir noktada birleşen açıların toplamı 360° dir; kare ve altıgenin açıları çıkarılınca kalan iç açıdan kenar sayısı bulunur.','Kalan açıyı dış açı sanıp 360° ye bölmek; açıyı kenar sayısı sanmak; altıgenin iç açısını yanlış almak.','orta',4,'cz-birlesim','Ortak kenarlı çokgenler')
r6=360-90-120; n6=360//(180-r6); assert r6==150 and 180-r6==30 and n6==12 and 360%(180-r6)==0 and 360-90-135==135
s6=1.3; O=(0,0)
sq=[O,(s6,0),(s6,s6),(0,s6)]
hc=(-cos(radians(30))*s6, sin(radians(30))*s6); hx=[(hc[0]+s6*cos(radians(330+60*k)),hc[1]+s6*sin(radians(330+60*k))) for k in range(6)]
assert dist(hx[0],O)<1e-9 and dist(hx[1],(0,s6))<1e-9 and abs(ang(O,hx[1],hx[5])-120)<1e-9
f=F(); f.poly(sq); f.poly(hx)
f.arc(O,hx[5],(s6,0),.55,None,None,'dashed'); f.node((0,-.27),'$O$'); f.node((0,-1.05),'düzgün çokgen')
SK=f.svg()
q('0006',tipId='cz-birlesim',tip='Ortak kenarlı çokgenler',z='orta',alt='Köşede Birleşen Çokgenler',kaz='Bir köşede boşluksuz birleşen kare, düzgün altıgen ve düzgün çokgenin kenar sayısını açıların toplamından bulur.',kalip='hikâyeli',
 kart='K-GCZ-06 (köşede birleşme) · kare + altıgen + düzgün çokgen',
 metin='Bir döşeme ustası, kenar uzunlukları eşit olan bir kare, bir düzgün altıgen ve bir düzgün çokgen biçimindeki fayansı, şekildeki gibi bir O köşesinde aralarında boşluk kalmayacak biçimde bir araya getirmiştir. Şekilde düzgün çokgen fayans tamamen gösterilmemiştir ve şekil ölçekli değildir.\nBuna göre, bu düzgün çokgen kaç kenarlıdır?',
 dogru=12,yan=[(8,'Altıgenin iç açısı yerine sekizgenin iç açısını (135°) kullanarak 135° lik iç açıdan 8 kenarlı çokgeni bulmuş.','bilgi'),(20,'Altıgen yerine beşgenin iç açısını (108°) alıp 162° lik açıdan 20 kenarlı çokgeni bulmuş.','bilgi'),(30,'Dış açıyı (30°) kenar sayısı sanmış.','dikkat'),(150,'Kalan iç açıyı (150°) kenar sayısı sanmış.','dikkat')],
 istenen='Düzgün çokgenin kenar sayısı.',
 ip=['O köşesinde buluşan açıların toplamı hangi değere eşittir? Kare ve altıgenin köşedeki açıları kaçar derecedir?'],
 bilgi=[DUZ,TAM],
 ad=[A('Kalan açıyı bul','O nun etrafındaki açıların toplamı 360° dir; karenin iç açısı 90°, düzgün altıgenin iç açısı 120° dir.','360° − 90° − 120° = 150°'),A('Dış açıyı bul','Düzgün çokgenin iç açısı 150° ise dış açısı 180° ile arasındaki farktır.','180° − 150° = 30°'),A('Kenar sayısını bul','Dış açıların toplamı 360° dir.','360° ÷ 30° = 12')],
 puf='Düzgün çokgenin kenar sayısını dış açıdan bulurken önce iç açıyı bir noktanın etrafındaki açıların toplamından elde et.',sekil=SK)

# =================== 07 · Beşgende içe çizilen eşkenar üçgen · zor ===================
kartla('K-GCZ-07','Düzgün beşgende iç noktaya çizilen eşkenar üçgen','Beşgenin iç açısından 60° çıkarılınca iki ikizkenar üçgen oluşur; taban açıları bulunur ve F noktasının çevresindeki 360° dan hedef açı elde edilir.','Taban açısını bulup bırakmak; iki taban açısını toplayıp 360° den üçüncü (60°) açıyı çıkarmamak; ikizkenar üçgenin tepe açısını yanlış belirlemek.','zor',5,'cz-ic-ucgen','Düzgün çokgende iç eşkenar üçgen')
R7=1.75; Pv=reg(5,R7,234); A7,B7,C7,D7,E7=Pv; s7=dist(A7,B7)
F7=add(mid(A7,B7),mul((0,1),s7*sqrt(3)/2))
assert abs(dist(F7,A7)-s7)<1e-9 and abs(dist(F7,B7)-s7)<1e-9 and konveks(Pv)
assert abs(ang(A7,E7,B7)-108)<1e-9 and abs(ang(A7,E7,F7)-48)<1e-9 and abs(ang(F7,A7,E7)-66)<1e-9 and abs(ang(F7,B7,C7)-66)<1e-9
x7=ang(F7,E7,C7); assert abs(x7-168)<1e-9 and 360-60-66-66==168 and 66+66==132 and 360-132==228 and 108-60==48 and (180-48)//2==66
f=F(); f.poly(Pv)
for p in (A7,B7,E7,C7): f.line(F7,p)
f.arc(F7,E7,C7,.5,'$x$',.82)
f.tick(A7,B7,2); f.tick(A7,F7,2); f.tick(B7,F7,2)
ic=cen(Pv)
for i,n_ in enumerate('ABCDE'): f.vl(n_,Pv[i],sub(Pv[i],ic),.3)
f.node((F7[0],F7[1]+.0),'') if False else None
f.vl('F',F7,(0,-1),.32)
SK=f.svg()
q('0007',kalip='hikâyeli',tipId='cz-ic-ucgen',tip='Düzgün çokgende iç eşkenar üçgen',z='zor',alt='Beşgen ve Eşkenar Üçgen',kaz='Düzgün beşgenin içine çizilen eşkenar üçgenle oluşan ikizkenar üçgenlerin açılarından F noktasındaki açıyı bulur.',
 kart='K-GCZ-07 (beşgen + eşkenar üçgen) · ABF eşkenar, m(EFC)',
 metin='Bir bahçıvan, şekildeki ABCDE düzgün beşgen biçimli çiçek tarhının içinde, ABF üçgeni eşkenar olacak biçimde bir F noktası belirlemiş ve F noktasından E ve C köşelerine birer sıra çiçek dikmiştir. Şekil ölçekli değildir.\nBuna göre, x = m(EFC) kaç derecedir?',
 dogru=168,yan=[(66,'Yalnız ikizkenar üçgenin taban açısını (m(AFE)) bulup bırakmış.','dikkat'),(108,'Beşgenin bir iç açısını cevap yazmış.','dikkat'),(132,'İki taban açısını (66° + 66°) toplayıp F nin çevresindeki diğer açıları hesaba katmamış.','dikkat'),(228,'F nin çevresindeki açılardan 60° yi hesaba katmayıp 360° − 132° = 228° bulmuş.','islem')],
 istenen='x = m(EFC) açısının ölçüsü (derece).',
 ip=['Şekildeki eşit uzunluklu kenarları belirle.'],
 bilgi=[DUZ,IKIZ,ESKU],
 ad=[A('A daki açıyı böl','Beşgenin iç açısı 108°, eşkenar üçgenin açısı 60° dir.','m(EAF) = 108° − 60° = 48°'),A('Taban açısını bul','|AE| = |AB| = |AF| olduğundan AEF ikizkenar üçgendir.','m(AFE) = (180° − 48°) ÷ 2 = 66°'),A('Simetrik açıyı yaz','B de de aynı durum vardır: |BC| = |BF|, m(FBC) = 48°.','m(BFC) = 66°'),A('F nin çevresini topla','F noktası etrafındaki açılar toplamı 360° dir: 60°, 66°, 66° ve x.','x = 360° − 60° − 66° − 66° = 168°')],
 puf='Eşit kenarları şekilde işaretle; hangi üçgenler ikizkenar oldu?',sekil=SK)

# =================== 08 · Altıgenin kenarlarına kareler · zor ===================
kartla('K-GCZ-08','Altıgenin kenarlarına dışarıdan kareler','Altıgen köşesinde karelerin kenarları arasındaki açı 60° çıkar; eş kenarlı üçgenden 12 kenarın hepsi eşit bulunur ve çevre kenar sayısı çarpı kenardır.','Bağlantı parçasının uzunluğunu kenardan farklı sanmak; yalnız karelerin dış kenarlarını saymak; çevre yerine toplam kare çevresi bulmak.','orta',5,'cz-birlesim','Ortak kenarlı çokgenler')
a8=4; ext8=360-120-90-90; assert ext8==60 and 12*a8==48 and 6*a8==24 and 6*a8+6*(a8//2)==36 and 6*3*a8==72 and 6*4*a8==96
sc8=.36; H8=reg(6,a8*sc8,0); W1=[];W2=[]
for i in range(6):
    p,q2=H8[i],H8[(i+1)%6]; e=un(sub(q2,p)); nv=(e[1],-e[0])        # saat yönü olmayan düzen: dış normal
    if (nv[0]*(mid(p,q2)[0])+nv[1]*(mid(p,q2)[1]))<0: nv=(-nv[0],-nv[1])
    W1.append(add(p,mul(nv,a8*sc8))); W2.append(add(q2,mul(nv,a8*sc8)))
outer=[]
for i in range(6): outer+= [W1[i],W2[i]]
for i in range(12): assert abs(dist(outer[i],outer[(i+1)%12])-a8*sc8)<1e-9
assert konveks(outer) and abs(sum(dist(outer[i],outer[(i+1)%12]) for i in range(12))/sc8-48)<1e-9
f=F(); f.poly(H8)
for i in range(6): f.poly([H8[i],H8[(i+1)%6],W2[i],W1[i]])
f.poly(outer,'thick')
ni=un(sub((0,0),mid(H8[0],H8[1]))); pa=add(H8[0],mul(ni,.2)); pb=add(H8[1],mul(ni,.2))
f.raw(f'\\draw[<->,thin] {pt(pa)} -- {pt(pb)};'); f.node(add(mid(pa,pb),mul(ni,.3)),'$4$')
SK=f.svg()
q('0008',tipId='cz-birlesim',tip='Ortak kenarlı çokgenler',z='orta',alt='Altıgen ve Kareler',kaz='Düzgün altıgenin kenarlarına çizilen karelerin dış köşelerinden oluşan 12 kenarlı çokgenin çevresini hesaplar.',kalip='hikâyeli',
 kart='K-GCZ-08 (altıgen + 6 kare) · kenar 4, 12 kenarlı çevre',
 metin='Bir tasarımcı, kenar uzunluğu 4 cm olan düzgün altıgen biçimindeki bir parçanın her kenarına dışarıya doğru birer kare ekliyor. Komşu karelerin altıgenin ortak köşesinden çıkan kenarlarının uçları şekildeki gibi birleştirilince kalın çizgiyle gösterilen 12 kenarlı bir çokgen oluşuyor. Şekil ölçekli değildir.\nBuna göre, kalın çizgili çokgenin çevresi kaç cm dir?',
 dogru=48,yan=[(24,'Yalnız karelerin dış kenarlarını (6 × 4) saymış; birleştirme parçalarını unutmuş.','dikkat'),(36,'Birleştirme parçalarını 2 cm saymış: 6 × 4 + 6 × 2 = 36.','dikkat'),(72,'Her kareden üç kenar sayıp 6 × 3 × 4 hesaplamış.','islem'),(96,'Altı karenin çevrelerinin toplamını (6 × 16) çevre sanmış.','bilgi')],
 istenen='12 kenarlı çokgenin çevresi (cm).',
 ip=['Altıgenin bir köşesinde hangi şekillerin açıları bir araya geliyor?'],
 bilgi=[DUZ,TAM,ESKU],
 ad=[A('Köşedeki açıyı bul','Altıgenin bir köşesinde altıgenin iç açısı ve iki karenin birer köşe açısı vardır; kalan açı birleştirme üçgeninin tepe açısıdır.','360° − 120° − 90° − 90° = 60°'),A('Üçgeni tanı','Üçgenin iki kenarı kare kenarlarıdır (4 cm); tepe açısı 60° olan ikizkenar üçgen eşkenardır.','birleştirme parçası = 4 cm'),A('Kenarları say','Çokgenin 6 kenarı karelerin dış kenarları, 6 kenarı birleştirme parçalarıdır; hepsi 4 cm dir.','12 kenar × 4 cm'),A('Çevreyi hesapla','Kenar sayısı ile kenar uzunluğu çarpılır.','12 × 4 = 48')],
 puf='Köşede toplanan açıların toplamını yazarak aralarında kalan üçgenin türünü belirle.',sekil=SK)

# =================== 09 · Cebirsel iç ve dış açılar · zor ===================
kartla('K-GCZ-09','Cebirsel ifadeli iç ve dış açılar','Dış açılar iç açıya çevrilir ya da iç açılar toplamı (n − 2) × 180° denklemi kurulur; x bulunup istenen iç açı hesaplanır.','Dış açıyı iç açı gibi toplamaya katmak; yalnız x i cevap yazmak; dış açıyı iç açıya çevirmeyi unutmak.','zor',5,'cz-ic-dis','Çokgende iç ve dış açılar')
x9=40; ia=[2*x9+20,3*x9,x9+70]; de=[2*x9+5,x9+25]
Ei=180-de[1]; Di=180-de[0]; assert ia==[100,120,110] and de==[85,65] and Di==95 and Ei==115 and sum(ia)+Di+Ei==540
assert (2*x9+20)+3*x9+(x9+70)+(180-(2*x9+5))+(180-(x9+25))==540 and 3*x9+420==540
ext9=[180-ia[0],180-ia[1],180-ia[2],de[0],de[1]]; assert sum(ext9)==360
V9,d9=build(ext9,[3.0,2.4,2.6]); f=F(); f.poly(V9)
for i,t in enumerate(('$(2x+20)^\\circ$','$3x^\\circ$','$(x+70)^\\circ$')): f.arc(V9[i],V9[(i-1)%5],V9[(i+1)%5],.4,t,1.05)
dis_ok(f,V9,d9,3,'$(2x+5)^\\circ$',lr=1.15); dis_ok(f,V9,d9,4,'$(x+25)^\\circ$',lr=1.15)
harf(f,V9,d9,'ABCDE')
SK=f.svg()
q('0009',kalip='hikâyeli',tipId='cz-ic-dis',tip='Çokgende iç ve dış açılar',z='zor',alt='İç ve Dış Açılar',kaz='Cebirsel ifadelerle verilen iç ve dış açılardan x i bulup istenen iç açıyı hesaplar.',
 kart='K-GCZ-09 (cebirsel açılar, beşgen) · x = 40',
 metin='Bir harita mühendisi, ABCDE konveks beşgeni biçimindeki bir arazinin A, B ve C köşelerindeki iç açıların ölçülerini, D ve E köşelerindeki dış açıların ölçülerini ise şekildeki gibi derece cinsinden x e bağlı olarak göstermiştir. Şekil ölçekli değildir.\nBuna göre, m(AED) kaç derecedir?',
 dogru=115,yan=[(40,'Yalnız x i bulup E köşesindeki iç açıyı hesaplamamış.','dikkat'),(65,'E köşesinin dış açısını (x + 25) cevap yazmış.','dikkat'),(85,'D köşesinin dış açısını (2x + 5) cevap yazmış; istenen köşe E dir.','dikkat'),(95,'D köşesinin iç açısını (180° − 85°) bulmuş; istenen köşe E dir.','dikkat')],
 istenen='m(AED) iç açısının ölçüsü (derece).',
 ip=['Şekildeki açıların hangileri iç, hangileri dış açı? Hepsini aynı türe çevirip toplamla ilgili bir denklem kurabilir misin?'],
 bilgi=[ICTOP],
 ad=[A('Dış açıları iç açıya çevir','İç açı = 180° − dış açı.','D: 180° − (2x + 5) = 175° − 2x · E: 180° − (x + 25) = 155° − x'),A('Toplam denklemini kur','Beşgenin iç açılar toplamı 3 × 180° = 540° dir.','(2x + 20) + 3x + (x + 70) + (175 − 2x) + (155 − x) = 540 → 3x + 420 = 540'),A('x i bul','Denklem çözülür.','3x = 120 → x = 40'),A('E nin iç açısını hesapla','E nin dış açısı x + 25 = 65° dir.','m(AED) = 180° − 65° = 115°')],
 puf='Farklı türde (iç ve dış) verilen açıları önce aynı türe çevir, sonra toplam denklemini kur.',sekil=SK)

# =================== 10 · Düzgün onikigende köşegenler arası açı · orta ===================
kartla('K-GCZ-10','Düzgün onikigende köşegenler arasındaki açı','Bir köşeden çizilen köşegenler iç açıyı eş açılara böler; eş açıların sayısı sayılıp birim açıyla çarpılır.','Aradaki eş açıların sayısını yanlış saymak; köşe sayısı ile açı sayısını karıştırmak; iç açıyı cevap sanmak.','orta',4,'cz-duzgun-kosegen','Düzgün çokgende köşegen açıları')
n10=12; ic10=180-360//n10; u10=(180-ic10)//2; assert ic10==150 and u10==15 and (n10-2)*u10==ic10 and 5*u10==75 and 3*u10==45 and 4*u10==60 and 6*u10==90
R10=2.0; Pv=reg(n10,R10,90+15); ic=(0,0)
Pa=Pv
for k in range(1,12): assert abs(ang(Pa[0],Pa[k],Pa[(k+1)%12])-15)<1e-9 if k<11 else True
assert abs(ang(Pa[0],Pa[2],Pa[7])-75)<1e-9
f=F(); f.poly(Pv); f.line(Pv[0],Pv[2]); f.line(Pv[0],Pv[7]); f.arc(Pv[0],Pv[2],Pv[7],.7,'$x$',1.05)
for i,n_ in enumerate('ABCDEFGHIJKL'): f.vl(n_,Pv[i],Pv[i],.32)
SK=f.svg()
q('0010',kalip='hikâyeli',tipId='cz-duzgun-kosegen',tip='Düzgün çokgende köşegen açıları',z='orta',alt='Düzgün Onikigen',kaz='Düzgün onikigende bir köşeden çizilen iki köşegen arasındaki açıyı eş açıların sayısından bulur.',
 kart='K-GCZ-10 (düzgün onikigen) · m(CAH)',
 metin='Bir saat tasarımcısı, düzgün onikigen biçimli bir kadranın ABCDEFGHIJKL köşelerinden A köşesini C ve H köşeleriyle şekildeki gibi birleştirmiştir. Şekil ölçekli değildir.\nBuna göre, x = m(CAH) kaç derecedir?',
 dogru=75,yan=[(15,'Yalnız bir kenarın karşısındaki açıyı (m(BAC)) bulup bırakmış.','dikkat'),(45,'C ile H arasındaki eş açıları 3 tane saymış.','dikkat'),(60,'C ile H arasında kalan köşeleri (D, E, F, G) sayıp 4 eş açı almış; açı sayısı bir fazladır.','dikkat'),(90,'C ile H arasındaki eş açıları 6 tane saymış.','dikkat')],
 istenen='x = m(CAH) açısının ölçüsü (derece).',
 ip=['A köşesindeki iç açının ölçüsü kaçtır? A dan çizilebilen köşegenler bu açıyı kaç parçaya ayırır; parçalar birbirine nasıl?'],
 bilgi=[DUZ,IKIZ],
 ad=[A('İç açıyı bul','Düzgün onikigende dış açı 360° ÷ 12 = 30° dur.','iç açı = 180° − 30° = 150°'),A('Birim açıyı bul','ABC ikizkenar üçgeninde tepe açısı 150° dir. Eşit yaylara bakan çevre açılar eşit olduğundan A daki iç açı 10 eş açıya bölünür.','m(BAC) = (180° − 150°) ÷ 2 = 15°'),A('Eş açıları say','AC ile AH arasında 5 eş açı vardır.','C → D → E → F → G → H : 5 açı'),A('Hesapla','Eş açıların sayısı birim açıyla çarpılır.','5 × 15° = 75°')],
 puf='Düzgün çokgenin bir köşesinden çizilen köşegenler iç açıyı eş açılara ayırır; önce bir parçanın ölçüsünü bul.',sekil=SK)

# =================== yaz ===================
def bitir_geo(onek):
    for qq in P.ANA: qq['kardes']=None
    P.yaz(os.path.join(GD,f'{onek}-1.json'),f'/tmp/bos-{onek}.json')
    tipler={}
    for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=TIPK[c['tipId']]))['kartlar'].append(c['id'])
    json.dump(dict(konu=P.konu_adi,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 TYT Geometri çıkmış soruları (yalnız mantık), MEB 9–10. sınıf geometri müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar',f'{onek}.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler))

bitir_geo('cokgeniki')
