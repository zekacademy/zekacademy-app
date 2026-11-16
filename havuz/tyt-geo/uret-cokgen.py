"""TYT Geometri · Çokgenler (hafif mod). Şekil koordinatları hesaplanır; her cevap ve çeldirici assert edilir."""
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

ONEK='cokgen'; KONU_AD='Çokgenler'
P=Parti(ONEK,KONU_AD,'geo|Çokgenler',ders='TYT Geometri',idon='tytgeo')
def q(no,kalip='şekilli',**k): mk(P,no,adim=len(k['ad']),kalip=kalip,**k)
konu('geo|Çokgenler','Çokgenler')
ICTOP=B('İç ve dış açılar','n kenarlı konveks çokgenin iç açıları toplamı (n − 2) × 180° dir; dış açıları toplamı 360° dir. Bir iç açı ile komşu dış açının toplamı 180° dir. Örnek: yedigenin iç açıları toplamı 5 × 180° = 900°')
DUZ=B('Düzgün çokgen','tüm kenarları ve tüm açıları eşit olan çokgendir. n kenarlı düzgün çokgenin bir dış açısı 360° ÷ n, bir iç açısı 180° − 360° ÷ n dir. Örnek: düzgün sekizgende dış açı 45°, iç açı 135° dir')
KOSEG=B('Köşegen sayısı','n kenarlı çokgende bir köşeden n − 3 köşegen çizilebilir; toplam köşegen sayısı n × (n − 3) ÷ 2 dir. Örnek: yedigende bir köşeden 4, toplam 7 × 4 ÷ 2 = 14 köşegen çizilir')
ESKU=B('Eşkenar üçgen ve altıgen','kenarı a olan eşkenar üçgenin alanı a² × √3 ÷ 4 tür. Düzgün altıgenin her iç açısı 120° dir. Örnek: kenarı 2 olan eşkenar üçgenin alanı 2² × √3 ÷ 4 = √3')
OZEL=B('30°–60°–90° üçgeni','kenarları 1 : √3 : 2 oranındadır; 30° nin karşısındaki kenar en kısa kenardır. İkizkenar üçgende tepeden tabana inen yükseklik tabanı ikiye böler. Örnek: en kısa kenarı 3 olan bu üçgende diğer dik kenar 3√3, hipotenüs 6 dır')
def reg(n,R,rot=0,c=(0,0)): return [(c[0]+R*cos(radians(rot+360*i/n)),c[1]+R*sin(radians(rot+360*i/n))) for i in range(n)]
def konveks(ps):
    n=len(ps); z=[(ps[(i+1)%n][0]-ps[i][0])*(ps[(i+2)%n][1]-ps[(i+1)%n][1])-(ps[(i+1)%n][1]-ps[i][1])*(ps[(i+2)%n][0]-ps[(i+1)%n][0]) for i in range(n)]
    return all(x>0 for x in z) or all(x<0 for x in z)
def kes(p1,p2,p3,p4):
    x1,y1=p1;x2,y2=p2;x3,y3=p3;x4,y4=p4; d=(x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
    return (((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4))/d,((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4))/d)

# ---- 01 · kolay · beşgende iç açılar
kartla('K-GCK-01','Beşgende iç açılar toplamı','Beşgenin iç açıları toplamı 3 × 180° = 540° dır; bilinen açılar çıkarılıp kalan eşit iki açıya bölünür.','Dörtgen ya da altıgen toplamını kullanmak; iki açının toplamını tek açı sanmak; dış açıyı bulmak.','kolay',3,'cg-ic-toplam','Çokgende iç açılar toplamı')
iA,iB,iC=100,120,110; x1=Fr(540-(iA+iB+iC),2); assert x1==105 and Fr(360-330,2)==15 and 180-105==75 and Fr(720-330,2)==195 and 540-330==210
ext=[180-a for a in (iA,iB,iC,105,105)]; assert sum(ext)==360
dirs=[0]; 
for e in ext[1:]: dirs.append(dirs[-1]+e)           # AB, BC, CD, DE, EA yönleri (derece)
u=[(cos(radians(d)),sin(radians(d))) for d in dirs]; L=[3.6,2.6,2.8]
sx=-sum(L[i]*u[i][0] for i in range(3)); sy=-sum(L[i]*u[i][1] for i in range(3))
det=u[3][0]*u[4][1]-u[3][1]*u[4][0]; L4=(sx*u[4][1]-sy*u[4][0])/det; L5=(u[3][0]*sy-u[3][1]*sx)/det; assert L4>0 and L5>0
Ls=L+[L4,L5]; V=[(0,0)]
for i in range(4): V.append((V[-1][0]+Ls[i]*u[i][0],V[-1][1]+Ls[i]*u[i][1]))
assert konveks(V) and dist(V[4],V[0])-L5<1e-9
for i,a in enumerate((iA,iB,iC,105,105)): assert abs(ang(V[i],V[(i-1)%5],V[(i+1)%5])-a)<1e-6
f=F(); f.poly(V); ic=cen(V)
for i,(t,lr) in enumerate((('$100^\\circ$',.95),('$120^\\circ$',.95),('$110^\\circ$',.95),('$x$',.7),('$x$',.7))): f.arc(V[i],V[(i-1)%5],V[(i+1)%5],.38,t,lr)
for i,n in enumerate('ABCDE'): f.vl(n,V[i],sub(V[i],ic),.3)
SK=f.svg()
q('0001',tipId='cg-ic-toplam',tip='Çokgende iç açılar toplamı',z='kolay',alt='İç Açılar Toplamı',kaz='Beşgenin iç açılar toplamından bilinmeyen eşit iki açıyı bulur.',
 kart='K-GCK-01 (iç açılar toplamı) · beşgen, 100°, 120°, 110°',
 metin='Şekildeki ABCDE konveks beşgeninde A, B ve C köşelerindeki iç açıların ölçüleri sırasıyla 100°, 120° ve 110° dir. D ve E köşelerindeki iç açıların ölçüleri birbirine eşittir ve her biri x ile gösterilmiştir.\nBuna göre, x kaç derecedir?',
 dogru=105,yan=[(15,'Beşgen yerine dörtgenin iç açılar toplamını (360°) alıp (360° − 330°) ÷ 2 = 15 bulmuş.','bilgi'),(75,'İç açı yerine komşu dış açıyı hesaplamış: 180° − 105° = 75°.','dikkat'),(195,'Beşgen yerine altıgenin iç açılar toplamını (720°) alıp (720° − 330°) ÷ 2 = 195 bulmuş.','bilgi'),(210,'Kalan toplamı 540° − 330° = 210° bulup iki açıya bölmeyi unutmuş.','dikkat')],
 istenen='x = m(D) = m(E) açısının ölçüsü (derece).',
 ip=['Kenar sayısına bakarak çokgenin iç açıları toplamını bul; verilen üç açıyı toplamdan çıkınca kalan kaç açıya ait?'],
 bilgi=[ICTOP],
 ad=[A('İç açılar toplamını yaz','Beş kenarlı çokgenin iç açılar toplamı (5 − 2) × 180° dir.','3 × 180° = 540°'),A('Bilinen açıları çıkar','A, B ve C açıları verilmiştir.','100° + 120° + 110° = 330° → kalan 540° − 330° = 210°'),A('Eşit iki açıya böl','Kalan 210°, D ve E açılarına eşit paylaşılır.','2x = 210° → x = 105°')],
 puf='n kenarlı çokgenin iç açılar toplamı (n − 2) × 180° dir; eşit açılar kalan toplamın bölünmesiyle bulunur.',sekil=SK)

# ---- 02 · orta · düzgün beşgende uzatılan kenarlar
kartla('K-GCK-02','Düzgün çokgende dış açı','Düzgün beşgende dış açı 72° dir; uzatılan iki kenar ile BC kenarı bir üçgen oluşturur, üçüncü açı 180° den çıkarılarak bulunur.','Dış açı yerine iç açıyı (108°) kullanmak; üçgen açılar toplamını unutmak.','orta',4,'cg-duzgun-aci','Düzgün çokgende iç ve dış açı')
R2=1.7; Pv=reg(5,R2,90+36)          # A..E
Fz=kes(Pv[0],Pv[1],Pv[3],Pv[2]); assert dist(Fz,Pv[1])>0 and ((Fz[0]-Pv[1][0])*(Pv[1][0]-Pv[0][0])+(Fz[1]-Pv[1][1])*(Pv[1][1]-Pv[0][1]))>0
assert abs(ang(Fz,Pv[1],Pv[2])-36)<1e-9 and abs(ang(Pv[1],Pv[2],Fz)-72)<1e-9 and 180-2*72==36 and 108//2==54 and 2*72==144
f=F(); f.poly(Pv); f.line(Pv[1],Fz); f.line(Pv[2],Fz); f.arc(Fz,Pv[1],Pv[2],.55,'$x$',.9)
ic=cen(Pv)
for i,n in enumerate('ABCDE'): f.vl(n,Pv[i],sub(Pv[i],ic),.3)
f.vl('F',Fz,sub(Fz,ic),.3)
SK=f.svg()
q('0002',tipId='cg-duzgun-aci',tip='Düzgün çokgende iç ve dış açı',z='orta',alt='Düzgün Beşgen',kaz='Düzgün beşgenin dış açısını kullanarak uzatılan kenarların oluşturduğu üçgende açı bulur.',
 kart='K-GCK-02 (düzgün çokgen) · düzgün beşgende uzatılan iki kenar',
 metin='Şekilde bir ABCDE düzgün beşgeni ve kenarlarından ikisinin uzantıları görülmektedir. [AB] kenarı B noktası yönünde, [DC] kenarı C noktası yönünde uzatılmış ve bu uzantılar F noktasında kesişmiştir.\nBuna göre, x = m(BFC) kaç derecedir?',
 dogru=36,yan=[(54,'İç açı olan 108° nin yarısını almış.','bilgi'),(72,'Dış açıyı (72°) bulup üçgenin üçüncü açısını hesaplamadan cevap yazmış.','dikkat'),(108,'Beşgenin bir iç açısını (108°) cevap sanmış.','dikkat'),(144,'İki dış açıyı toplayıp (72° + 72° = 144°) üçgenin üçüncü açısını bulmamış.','dikkat')],
 istenen='x = m(BFC) açısının ölçüsü (derece).',
 ip=['B ve C köşelerinde uzatılan kenarlarla BC kenarı arasında kalan açılar, beşgenin hangi açısıyla ilişkilidir?'],
 bilgi=[DUZ],
 ad=[A('Dış açıyı bul','Düzgün beşgenin bir dış açısı 360° ÷ 5 dir.','360° ÷ 5 = 72°'),A('Üçgenin açılarını yaz','FBC üçgeninde B ve C açıları, uzatılan kenarların oluşturduğu dış açılara eşittir.','m(FBC) = m(FCB) = 72°'),A('Üçüncü açıyı bul','Üçgenin iç açıları toplamı 180° dir.','x = 180° − 72° − 72° = 36°')],
 puf='Düzgün n-genin uzatılan komşu kenarları arasındaki açı, iki dış açı toplamı 180° den çıkarılarak bulunur: 180° − 2 × 360°/n.',sekil=SK)

# ---- 03 · kolay · köşegen sayısı (şekilden n)
kartla('K-GCK-03','Köşegen sayısı','Bir köşeden çizilen köşegenler çokgeni n − 2 üçgene ayırır; üçgen sayısından kenar sayısı, sonra toplam köşegen sayısı bulunur.','Bir köşeden çıkan köşegen sayısını ya da kenar sayısını cevap sanmak; kenarları da saymak.','kolay',3,'cg-kosegen','Çokgende köşegen sayısı')
n3=9; assert n3-2==7 and n3-3==6 and n3*(n3-3)//2==27 and n3*(n3-1)//2==36
rad=[2.1*(1+.07*sin(3*radians(360*i/n3)+.4)) for i in range(n3)]
V3=[(rad[i]*cos(radians(90+360*i/n3)),rad[i]*sin(radians(90+360*i/n3))) for i in range(n3)]; assert konveks(V3)
f=F(); f.poly(V3)
for k in range(2,n3-1): f.line(V3[0],V3[k])
ic=cen(V3); f.vl('A',V3[0],sub(V3[0],ic),.32)
SK=f.svg()
q('0003',tipId='cg-kosegen',tip='Çokgende köşegen sayısı',z='kolay',alt='Köşegen Sayısı',kaz='Bir köşeden çizilen köşegenlerin ayırdığı üçgen sayısından kenar sayısını ve toplam köşegen sayısını bulur.',
 kart='K-GCK-03 (köşegen sayısı) · 7 üçgene ayrılan dokuzgen',
 metin='Şekildeki konveks çokgenin A köşesinden çizilebilen bütün köşegenler çizilmiş ve çokgen üçgenlere ayrılmıştır. Köşegen, komşu olmayan iki köşeyi birleştiren doğru parçasıdır.\nBuna göre, bu çokgenin tüm köşegenlerinin sayısı kaçtır?',
 dogru=27,yan=[(6,'Yalnız A köşesinden çıkan köşegenleri saymış.','dikkat'),(7,'Oluşan üçgenlerin sayısını cevap olarak yazmış.','dikkat'),(9,'Kenar sayısını (n = 9) cevap sanmış.','dikkat'),(36,'Kenarları da köşegen sayıp her köşe çiftini saymış: 9 × 8 ÷ 2 = 36.','bilgi')],
 istenen='Çokgenin tüm köşegenlerinin sayısı.',
 ip=['Bir köşeden çizilen köşegenlerle oluşan üçgen sayısı ile kenar sayısı arasında nasıl bir bağlantı var?'],
 bilgi=[KOSEG],
 ad=[A('Üçgenleri say','A köşesinden çizilen köşegenler çokgeni n − 2 üçgene ayırır; şekilde 7 üçgen vardır.','n − 2 = 7'),A('Kenar sayısını bul','Üçgen sayısına 2 eklenir.','n = 9'),A('Köşegen sayısını hesapla','Her köşeden n − 3 = 6 köşegen çıkar; her köşegen iki uçtan sayıldığı için ikiye bölünür.','9 × 6 ÷ 2 = 27')],
 puf='Üçgen sayısı = n − 2 olduğundan kenar sayısı üçgen sayısının 2 fazlasıdır; köşegen sayısı n(n − 3)/2 dir.',sekil=SK)

# ---- 04 · orta · iç açıdan köşegen sayısı (hikâyeli)
kartla('K-GCK-04','İç açıdan köşegen sayısı','Verilen iç açının dış açısı 360° ye bölünerek kenar sayısı, ardından köşegen sayısı bulunur.','Dış açı yerine iç açıyı bölmek; köşegen sayısını ikiye bölmemek; kenarları da saymak.','orta',4,'cg-kosegen','Çokgende köşegen sayısı')
n4=360//(180-156); assert 180-156==24 and n4==15 and n4*(n4-3)//2==90 and n4-3==12 and n4*(n4-1)//2==105 and n4*(n4-3)==180
Vq=(0,0); r1=(2.2*cos(radians(-78)),2.2*sin(radians(-78))); r2=(2.2*cos(radians(-78-156)),2.2*sin(radians(-78-156)))
f=F(); f.line(Vq,r1); f.line(Vq,r2); f.arc(Vq,r1,r2,.6,'$156^\\circ$',1.15)
SK=f.svg()
q('0004',kalip='hikâyeli',tipId='cg-kosegen',tip='Çokgende köşegen sayısı',z='orta',alt='İç Açıdan Köşegen',kaz='Düzgün çokgenin iç açısından kenar sayısını bulup köşegen sayısını hesaplar.',
 kart='K-GCK-04 (köşegen sayısı) · iç açısı 156° olan düzgün çokgen',
 metin='Düzgün çokgen biçimli bir parkın her köşesine birer çeşme yapılmıştır. Şekilde parkın bir köşesindeki iç açı gösterilmiştir. Park yönetimi, kenarlar boyunca olan yollar dışında, komşu olmayan her iki çeşmeyi bir patika ile birleştirecektir.\nBuna göre, toplam kaç patika yapılacaktır?',
 dogru=90,yan=[(12,'Yalnız bir çeşmeden çıkan patika sayısını (n − 3 = 12) bulmuş.','dikkat'),(15,'Çeşme sayısını (n = 15) cevap sanmış.','dikkat'),(105,'Komşu çeşmeleri de sayıp her çeşme çiftini almış: 15 × 14 ÷ 2 = 105.','bilgi'),(180,'n × (n − 3) = 180 bulup ikiye bölmeyi unutmuş.','islem')],
 istenen='Yapılacak patika sayısı.',
 ip=['Düzgün çokgende iç açı ile dış açı arasındaki ilişkiyi kullanarak önce kenar sayısını bul.'],
 bilgi=[DUZ,KOSEG],
 ad=[A('Dış açıyı bul','Bir iç açı ile komşu dış açı 180° yapar.','dış açı = 180° − 156° = 24°'),A('Kenar sayısını bul','Dış açıların toplamı 360° dir ve hepsi eşittir.','n = 360° ÷ 24° = 15'),A('Köşeden çıkan sayıyı yaz','Her çeşme, kendisi ve iki komşusu dışındakilerle birleşir.','15 − 3 = 12'),A('Toplamı hesapla','Her patika iki uçtan sayıldığı için ikiye bölünür.','15 × 12 ÷ 2 = 90')],
 puf='Düzgün çokgende iç açı verilmişse önce dış açıyı (180° − iç açı) bul; n = 360° ÷ dış açı.',sekil=SK)

# ---- 05 · orta · düzgün altıgenin alanı (hikâyeli)
kartla('K-GCK-05','Düzgün altıgenin alanı','Düzgün altıgen, merkezden köşelere çizilen doğru parçalarıyla 6 eş eşkenar üçgene ayrılır; alan = 6 × eşkenar üçgenin alanı.','Üçgen sayısını yanlış saymak; √3 çarpanını unutmak.','orta',4,'cg-altigen-alan','Düzgün altıgenin alanı')
a5=4; tri5=(a5*a5,4) ; assert 6*a5*a5//4==24            # 6·(a²√3/4) = 24√3
assert 3*4==12 and 4*4==16 and 5*4==20
s=.55; H5=reg(6,a5*s,240); O5=(0,0)
assert all(abs(dist(H5[i],H5[(i+1)%6])-a5*s)<1e-9 for i in range(6)) and abs(alan(H5)/s**2-24*sqrt(3))<1e-9 and konveks(H5)
f=F(); f.poly(H5)
for i in range(3): f.line(H5[i],H5[i+3])
for i,n in enumerate('ABCDEF'): f.vl(n,H5[i],sub(H5[i],O5),.3)
f.node(add(O5,(0,.45)),'$O$'); f.raw(f'\\fill {pt(O5)} circle (1.1pt);'); f.sl('$4$',H5[0],H5[1],O5,.3)
SK=f.svg()
q('0005',kalip='hikâyeli',tipId='cg-altigen-alan',tip='Düzgün altıgenin alanı',z='orta',alt='Altıgenin Alanı',kaz='Düzgün altıgeni eş eşkenar üçgenlere bölerek alanını hesaplar.',
 kart='K-GCK-05 (düzgün altıgen) · kenarı 4 cm',
 metin='Bir seramik atölyesinde üretilen düzgün altıgen biçimli fayansın köşegenlerinden üçü, şekilde görüldüğü gibi O noktasında kesişmektedir. Fayansın bir kenarının uzunluğu 4 cm dir ve yüzeyi tek renk sırla kaplanacaktır.\nBuna göre, sırlanacak yüzeyin alanı kaç cm² dir?',
 dogru='24√3',sira=['12√3','24','16√3','20√3','24√3'],
 yan=[('12√3','Altıgeni 3 eşkenar üçgene ayrılmış sanmış: 3 × 4√3 = 12√3.','bilgi'),('24','Eşkenar üçgenin alanında √3 çarpanını unutmuş: 6 × (4² ÷ 4) = 24.','islem'),('16√3','Altıgeni 4 eşkenar üçgene ayırıp 4 × 4√3 = 16√3 bulmuş.','bilgi'),('20√3','Altıgeni 5 eşkenar üçgene ayırıp 5 × 4√3 = 20√3 bulmuş.','bilgi')],
 istenen='Altıgen biçimli fayansın alanı (cm²).',
 ip=['O merkezi köşelere birleştirildiğinde altıgen hangi şekillere ve kaç tane parçaya ayrılır?'],
 bilgi=[ESKU],
 ad=[A('Üçgenleri tanı','O merkezi, köşelerle birleştirilince altı üçgen oluşur; merkez açıları 360° ÷ 6 = 60° dir.','OAB üçgeninde m(O) = 60°'),A('Üçgenin türünü bul','|OA| = |OB| olduğundan taban açıları da 60° dir; üçgen eşkenardır ve kenarı altıgenin kenarına eşittir.','|OA| = |OB| = |AB| = 4 cm'),A('Bir üçgenin alanını yaz','Eşkenar üçgenin alanı a² × √3 ÷ 4 tür.','4² × √3 ÷ 4 = 4√3'),A('Altıgenin alanını bul','Altı eş üçgenin alanı toplanır.','6 × 4√3 = 24√3 cm²')],
 puf='Düzgün altıgen = 6 eş eşkenar üçgen; kenarı a ise alan 6 × a²√3/4 = 3a²√3/2 dir.',sekil=SK)

# ---- 06 · zor · altıgen eksi ACE
kartla('K-GCK-06','Altıgen ve iç üçgen','Taralı bölge = altıgenin alanı − ACE üçgeninin alanı; |AC| = a√3 olduğundan ACE nin kenarı da a√3 dür.','ACE nin kenarını a sanmak; ACE yi altıgenin üçte biri sanmak; altıgenin tamamını cevap yazmak.','zor',5,'cg-altigen-bolme','Düzgün altıgende bölgelerin alanı')
a6=4; hexA=24; accA=Fr(3*a6*a6,4)  # (a√3)²√3/4 = 3a²√3/4 → katsayı 12
assert hexA-12==12 and 24-8==16 and 24-4==20 and 12==12
s=.6; H6=reg(6,a6*s,240)
assert abs(dist(H6[0],H6[2])/s-a6*sqrt(3))<1e-9 and abs(alan([H6[0],H6[2],H6[4]])/s**2-12*sqrt(3))<1e-9 and abs((alan(H6)-alan([H6[0],H6[2],H6[4]]))/s**2-12*sqrt(3))<1e-9
f=F()
for a_,b_,c_ in((0,1,2),(2,3,4),(4,5,0)): f.fill([H6[a_],H6[b_],H6[c_]])
f.poly(H6); f.poly([H6[0],H6[2],H6[4]])
for i,n in enumerate('ABCDEF'): f.vl(n,H6[i],sub(H6[i],(0,0)),.3)
f.sl('$4$',H6[0],H6[1],(0,0),.3)
SK=f.svg()
q('0006',tipId='cg-altigen-bolme',tip='Düzgün altıgende bölgelerin alanı',z='zor',alt='Altıgende Taralı Alan',kaz='Düzgün altıgende ACE üçgeninin dışında kalan bölgenin alanını altıgen ve eşkenar üçgen alanlarının farkıyla bulur.',
 kart='K-GCK-06 (altıgen ve ACE) · kenarı 4 cm',
 metin='Şekildeki ABCDEF düzgün altıgeninin bir kenarının uzunluğu 4 cm dir. Altıgenin A, C ve E köşeleri birleştirilerek ACE üçgeni oluşturulmuş ve altıgenin bu üçgenin dışında kalan üç parçası taranmıştır.\nBuna göre, taralı bölgelerin alanları toplamı kaç cm² dir?',
 dogru='12√3',sira=['12','12√3','16√3','20√3','24√3'],
 yan=[('12','√3 çarpanlarını unutarak 24 − 12 = 12 bulmuş.','islem'),('16√3','ACE üçgenini altıgenin üçte biri sanmış: 24√3 − 8√3 = 16√3.','bilgi'),('20√3','ACE üçgeninin kenarını da 4 cm sanmış: 24√3 − 4√3 = 20√3.','bilgi'),('24√3','Yalnız altıgenin alanını bulup ACE üçgenini çıkarmamış.','dikkat')],
 istenen='Taralı bölgelerin alanları toplamı (cm²).',
 ip=['ACE üçgeninin kenarı |AC| ile bulunur; |AC| uzunluğunu ABC ikizkenar üçgeninden çıkarmayı dene.'],
 bilgi=[ESKU,OZEL],
 ad=[A('Altıgenin alanını bul','Düzgün altıgen, kenarı 4 olan 6 eşkenar üçgenden oluşur.','6 × 4² × √3 ÷ 4 = 24√3'),A('|AC| yi bul','ABC ikizkenar üçgeninde m(B) = 120° dir; B den AC ye inen yükseklik 30°–60°–90° üçgenleri oluşturur.','yükseklik = 2 → |AC| = 2 × 2√3 = 4√3'),A('ACE nin türünü gör','Simetriden |AC| = |CE| = |EA| dır; ACE eşkenar üçgendir.','kenarı 4√3'),A('ACE nin alanını bul','Eşkenar üçgenin alan formülünü uygula.','(4√3)² × √3 ÷ 4 = 48 × √3 ÷ 4 = 12√3'),A('Farkı al','Taralı bölge altıgenden ACE nin çıkarılmasıyla bulunur.','24√3 − 12√3 = 12√3 cm²')],
 puf='Düzgün altıgende A, C, E köşelerini birleştiren eşkenar üçgenin alanı altıgenin yarısıdır; dışında kalan üç üçgen de yarısını oluşturur.',sekil=SK)

# =================== yaz ===================
def bitir_geo():
    for qq in P.ANA: qq['kardes']=None
    P.yaz(os.path.join(GD,ONEK+'-1.json'),'/tmp/bos-'+ONEK+'.json')
    tipler={}
    for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=TIPK[c['tipId']]))['kartlar'].append(c['id'])
    json.dump(dict(konu=KONU_AD,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 TYT Geometri çıkmış soruları (yalnız mantık), MEB 9–10. sınıf geometri müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar',ONEK+'.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler),'soru',len(P.ANA))
bitir_geo()
