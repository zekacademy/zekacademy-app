"""TYT Geometri · Dörtgenler (hafif mod). Şekil koordinatları hesaplanır; her cevap ve çeldirici assert edilir."""
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

ONEK='dortgen'; KONU_AD='Dörtgenler'
P=Parti(ONEK,KONU_AD,'geo|Dörtgenler',ders='TYT Geometri',idon='tytgeo')
def q(no,kalip='şekilli',**k): mk(P,no,adim=len(k['ad']),kalip=kalip,**k)
konu('geo|Dörtgenler','Dörtgenler')
DIC=B('Dörtgenin iç açıları','konveks dörtgenin iç açıları toplamı 360° dir. Örnek: üç açısı 80°, 90° ve 100° olan dörtgenin dördüncü açısı 360° − 270° = 90° dir')
DKOS=B('Köşegenleri dik dörtgen','köşegenleri birbirine dik olan dörtgenin alanı, köşegen uzunlukları çarpımının yarısıdır: alan = |AC| × |BD| ÷ 2. Örnek: köşegenleri 6 cm ve 5 cm olan böyle bir dörtgenin alanı 15 cm² dir')
ACIB=B('Açıortay','bir açıyı iki eşit açıya ayıran ışındır. Üçgenin iç açıları toplamı 180° dir. Örnek: 80° lik bir açının açıortayı, 40° lik iki açı oluşturur')
ORTAT=B('Orta taban','üçgende iki kenarın orta noktalarını birleştiren doğru parçası üçüncü kenara paraleldir ve uzunluğu onun yarısıdır. Karşılıklı kenarları paralel ve eşit olan dörtgen paralelkenardır. Örnek: üçüncü kenar 14 cm ise orta taban 7 cm dir')
DIKT=B('Dikdörtgen','dört açısı 90° olan dörtgendir; alanı kenar uzunlukları çarpımına eşittir. Karşılıklı kenarlar paralel ve eşittir. Örnek: kenarları 3 cm ve 7 cm olan dikdörtgenin alanı 21 cm² dir')
ALANORAN=B('Yüksekliği ortak üçgenler','yükseklikleri ortak olan üçgenlerin alanları tabanlarıyla orantılıdır. Örnek: tabanları 2 ve 3 olan, aynı yükseklikli iki üçgenin alanları oranı 2 / 3’tür')
def kes(p1,p2,p3,p4):
    x1,y1=p1;x2,y2=p2;x3,y3=p3;x4,y4=p4; d=(x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
    return (((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4))/d,((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4))/d)
def konveks(ps):
    n=len(ps); z=[(ps[(i+1)%n][0]-ps[i][0])*(ps[(i+2)%n][1]-ps[(i+1)%n][1])-(ps[(i+1)%n][1]-ps[i][1])*(ps[(i+2)%n][0]-ps[(i+1)%n][0]) for i in range(n)]
    return all(x>0 for x in z) or all(x<0 for x in z)
def dortgen_aci(ic,L1,L2):
    """iç açıları (A,B,C,D) verilen dörtgen: AB=L1, BC=L2 verilir, CD ve DA kapanıştan çözülür."""
    ext=[180-a for a in ic]; assert sum(ext)==360
    dirs=[0,ext[1],ext[1]+ext[2],ext[1]+ext[2]+ext[3]]; u=[(cos(radians(d)),sin(radians(d))) for d in dirs]
    sx=-(L1*u[0][0]+L2*u[1][0]); sy=-(L1*u[0][1]+L2*u[1][1]); det=u[2][0]*u[3][1]-u[2][1]*u[3][0]
    L3=(sx*u[3][1]-sy*u[3][0])/det; L4=(u[2][0]*sy-u[2][1]*sx)/det; assert L3>0 and L4>0
    V=[(0,0)]
    for Lx,uu in zip((L1,L2,L3),u): V.append((V[-1][0]+Lx*uu[0],V[-1][1]+Lx*uu[1]))
    for i,a in enumerate(ic): assert abs(ang(V[i],V[(i-1)%4],V[(i+1)%4])-a)<1e-6
    assert konveks(V); return V

# ---- 01 · kolay · dörtgende iç açılar
kartla('K-GDR-01','Dörtgenin iç açıları','İç açılar toplamı 360° dir; verilenler çıkarılıp kalan, açıların oranına göre paylaştırılır.','Kalanı eşit bölmek; sorulan açı yerine komşusunu yazmak.','kolay',3,'dg-ic-aci','Dörtgende iç açılar')
a1,b1=75,105; x1=Fr(360-a1-b1,3); assert x1==60 and 2*x1==120 and Fr(180,4)==45 and Fr(180,2)==90
V1=dortgen_aci((75,105,60,120),4.6,3.2)
f=F(); f.poly(V1); ic=cen(V1)
for i,(t,lr) in enumerate((('$75^\\circ$',.95),('$105^\\circ$',.95),('$x$',.8),('$2x$',.8))): f.arc(V1[i],V1[(i-1)%4],V1[(i+1)%4],.38,t,lr)
for i,n in enumerate('ABCD'): f.vl(n,V1[i],sub(V1[i],ic),.3)
SK=f.svg()
q('0001',tipId='dg-ic-aci',tip='Dörtgende iç açılar',z='kolay',alt='İç Açılar',kaz='Dörtgenin iç açıları toplamından, oranı verilen iki açıdan birini bulur.',
 kart='K-GDR-01 (iç açılar) · 75°, 105°, x, 2x',
 metin='Şekildeki ABCD konveks dörtgeninde A ve B köşelerindeki iç açıların ölçüleri sırasıyla 75° ve 105° dir. C köşesindeki iç açının ölçüsü x, D köşesindeki iç açının ölçüsü ise 2x tir.\nBuna göre, x kaç derecedir?',
 dogru=60,yan=[(45,'Kalan toplamı 4 açıya bölmüş: 180° ÷ 4 = 45°.','islem'),(90,'C ve D açılarını eşit sanmış: 180° ÷ 2 = 90°.','bilgi'),(120,'x yerine D açısını (2x) cevap olarak yazmış.','dikkat'),(180,'C ve D açılarının toplamını (3x = 180°) x sanmış.','dikkat')],
 istenen='x = m(C) açısının ölçüsü (derece).',
 ip=['Dörtgenin dört iç açısının toplamı kaçtır ve C ile D açıları bu toplamdan geriye kalanı nasıl paylaşıyor?'],
 bilgi=[DIC],
 ad=[A('Toplamı yaz','Konveks dörtgenin iç açıları toplamı 360° dir.','75° + 105° + x + 2x = 360°'),A('Bilinenleri topla','A ve B açıları verilmiştir.','75° + 105° = 180° → 3x = 180°'),A('x i bul','Kalan 180°, x + 2x = 3x e eşittir.','x = 60°')],
 puf='Dörtgenin iç açıları toplamı 360° dir; bilinmeyen açılar kalan toplamın oranına göre paylaştırılır.',sekil=SK)

# ---- 02 · kolay · köşegenleri dik dörtgenin alanı (uçurtma)
kartla('K-GDR-02','Köşegenleri dik dörtgen','Köşegenleri dik kesişen dörtgenin alanı köşegenler çarpımının yarısıdır; köşegen parçaları toplanarak köşegenler bulunur.','Köşegen parçalarından yalnızca ikisini kullanmak; ikiye bölmeyi unutmak.','kolay',3,'dg-dik-kosegen','Köşegenleri dik dörtgenin alanı')
AE2,EC2,BE2,ED2=4,6,3,5; AC2=AE2+EC2; BD2=BE2+ED2; al2=AC2*BD2//2; assert al2==40 and al2*2==80 and al2//2==20 and (AE2*BE2+BE2*EC2)//2==(AC2*BE2)//2==15 and (EC2*ED2+ED2*AE2)//2==25 and AC2*BD2==80
s=.45; E2=(0,0); A2=(0,AE2*s); C2=(0,-EC2*s); B2=(-BE2*s,0); D2=(ED2*s,0)
assert konveks([A2,B2,C2,D2]) and abs(alan([A2,B2,C2,D2])/s**2-al2)<1e-9
f=F(); f.poly([A2,B2,C2,D2]); f.line(A2,C2,'dashed'); f.line(B2,D2,'dashed'); f.dik(E2,A2,D2,.2)
f.vl('A',A2,(0,1),.3); f.vl('B',B2,(-1,0),.3); f.vl('C',C2,(0,-1),.3); f.vl('D',D2,(1,0),.3); f.node((.22,-.22),'$E$')
f.node((-.28,AE2*s/2),'$4$'); f.node((-.28,-EC2*s/2),'$6$'); f.node((-BE2*s/2,.25),'$3$'); f.node((ED2*s/2,.25),'$5$')
SK=f.svg()
q('0002',kalip='hikâyeli',tipId='dg-dik-kosegen',tip='Köşegenleri dik dörtgenin alanı',z='kolay',alt='Köşegenleri Dik Dörtgen',kaz='Köşegenleri dik kesişen dörtgenin alanını köşegen uzunluklarından hesaplar.',
 kart='K-GDR-02 (dik köşegenler) · yelken bezi, AC = 10, BD = 8',
 metin='Şekilde dörtgen biçimli bir yelken bezi gösterilmiştir. Yelkenin iki gergi çubuğu [AC] ve [BD], E noktasında dik kesişmektedir. Çubuk parçalarının uzunlukları cm cinsinden şekilde verilmiştir.\nBuna göre, yelken bezinin alanı kaç cm² dir?',
 dogru=40,yan=[(15,'Yalnız ABC üçgeninin alanını bulmuş: 10 × 3 ÷ 2 = 15.','dikkat'),(20,'Köşegenlerin çarpımını 4 e bölmüş: 80 ÷ 4 = 20.','islem'),(25,'Yalnız ACD üçgeninin alanını bulmuş: 10 × 5 ÷ 2 = 25.','dikkat'),(80,'Köşegenlerin çarpımını (10 × 8 = 80) ikiye bölmeyi unutmuş.','bilgi')],
 istenen='Yelken bezinin alanı (cm²).',
 ip=['Çubukların tamamının uzunluğunu bulmak için şekildeki parçaları nasıl birleştirirsin? Köşegenler dik olunca alan nasıl hesaplanır?'],
 bilgi=[DKOS],
 ad=[A('Köşegenleri bul','Her çubuğun uzunluğu, E noktasının iki yanındaki parçaların toplamıdır.','|AC| = 4 + 6 = 10 · |BD| = 3 + 5 = 8'),A('Alan bağıntısını yaz','Köşegenleri dik dörtgenin alanı köşegenler çarpımının yarısıdır.','Alan = |AC| × |BD| ÷ 2'),A('Hesapla','Değerleri yerine koy.','10 × 8 ÷ 2 = 40 cm²')],
 puf='Köşegenleri dik olan her dörtgenin alanı, köşegenlerin çarpımının yarısıdır.',sekil=SK)

# ---- 03 · orta · açıortaylar
kartla('K-GDR-03','Dörtgende açıortaylar','Komşu iki açının açıortayları AKB üçgeni oluşturur; A + B toplamı C ve D den bulunur ve yarısı üçgende kullanılır.','Yarıyı almayı unutmak; C ve D toplamını doğrudan cevap yazmak.','orta',4,'dg-aciortay','Dörtgende açıortayların kesişimi')
C3,D3=80,60; AB3=360-C3-D3; xx=180-AB3//2; assert AB3==220 and xx==70 and AB3//2==110 and 180-C3==100 and C3+D3==140 and xx==(C3+D3)//2
V3=dortgen_aci((85,135,80,60),2.0,2.0); A3,B3,C3p,D3p=V3
bis=lambda V,a,b: add(un(sub(a,V)),un(sub(b,V)))
K3=kes(A3,add(A3,bis(A3,B3,D3p)),B3,add(B3,bis(B3,A3,C3p))); assert abs(ang(K3,A3,B3)-70)<1e-6 and konveks(V3) and all((K3[0]-V3[i][0])*(V3[(i+1)%4][1]-V3[i][1])-(K3[1]-V3[i][1])*(V3[(i+1)%4][0]-V3[i][0])<0 for i in range(4))
f=F(); f.poly(V3); f.line(A3,K3); f.line(B3,K3)
f.arc(A3,B3,K3,.5); f.arc(A3,K3,D3p,.5); f.arc(B3,A3,K3,.45); f.arc(B3,A3,K3,.55); f.arc(B3,K3,C3p,.45); f.arc(B3,K3,C3p,.55)
ic=cen(V3); f.arc(K3,A3,B3,.32,'$x$',.62)
f.arc(C3p,D3p,B3,.4,'$80^\\circ$',.9); f.arc(D3p,A3,C3p,.4,'$60^\\circ$',.9)
for i,n in enumerate('ABCD'): f.vl(n,V3[i],sub(V3[i],ic),.3)
f.node(add(K3,(.0,.3)),'$K$')
SK=f.svg()
q('0003',tipId='dg-aciortay',tip='Dörtgende açıortayların kesişimi',z='orta',alt='Açıortaylar',kaz='Dörtgenin komşu iki açısının açıortaylarının kesişimindeki açıyı karşıt iki açıdan bulur.',
 kart='K-GDR-03 (açıortaylar) · C = 80°, D = 60°',
 metin='Şekildeki ABCD konveks dörtgeninde [AK] ve [BK], sırasıyla A ve B köşelerindeki iç açıların açıortaylarıdır ve K noktasında kesişirler. m(C) = 80° ve m(D) = 60° dır.\nBuna göre, x = m(AKB) kaç derecedir?',
 dogru=70,yan=[(110,'(A + B) ÷ 2 = 110° değerini x sanmış; AKB üçgeninin üçüncü açısını bulmamış.','dikkat'),(100,'Yalnız C açısını kullanıp 180° − 80° = 100° yazmış.','bilgi'),(140,'C ve D açılarının toplamını (140°) x sanmış.','bilgi'),(220,'A + B toplamını (220°) bulup açıortayın yarıladığını ve üçgen açılarını kullanmamış.','dikkat')],
 istenen='x = m(AKB) açısının ölçüsü (derece).',
 ip=['A ve B açılarının toplamını C ve D açılarından bulabilir misin? AKB üçgeninin diğer iki açısı bu toplamla nasıl ilişkilidir?'],
 bilgi=[DIC,ACIB],
 ad=[A('A + B toplamını bul','Dörtgenin iç açıları toplamı 360° dir.','m(A) + m(B) = 360° − 80° − 60° = 220°'),A('Açıortay açılarını yaz','Açıortaylar A ve B açılarını ikiye böler; AKB üçgeninde bu yarım açılar yer alır.','m(KAB) + m(KBA) = 220° ÷ 2 = 110°'),A('Üçgen açılarını kullan','AKB üçgeninin iç açıları toplamı 180° dir.','x = 180° − 110° = 70°')],
 puf='Dörtgende komşu iki açının açıortaylarının kesişim açısı, karşıt iki açının toplamının yarısıdır: x = (C + D) ÷ 2.',sekil=SK)

# ---- 04 · orta · kenar orta noktaları (çevre)
kartla('K-GDR-04','Orta noktalardan paralelkenar','Ardışık kenar orta noktaları, köşegenlere paralel ve yarı uzunlukta kenarlı bir paralelkenar oluşturur; çevresi köşegenler toplamıdır.','Çevre yerine yarı toplam ya da alan hesaplamak.','orta',4,'dg-orta-nokta','Kenar orta noktalarını birleştiren dörtgen')
AC4,BD4=12,8; assert AC4+BD4==20 and (AC4+BD4)//2==10 and 2*(AC4+BD4)==40 and AC4*BD4//2==48 and AC4*BD4==96
s=.4; E4=(5*s,0); ux=(cos(radians(60)),sin(radians(60)))
A4=(0,0); C4=(AC4*s,0); B4=add(E4,mul(ux,3*s)); D4=sub(E4,mul(ux,5*s))
assert abs(dist(A4,C4)/s-12)<1e-9 and abs(dist(B4,D4)/s-8)<1e-9 and konveks([A4,B4,C4,D4])
Km,Lm,Mm,Nm=mid(A4,B4),mid(B4,C4),mid(C4,D4),mid(D4,A4)
assert abs(dist(Km,Lm)/s-6)<1e-9 and abs(dist(Lm,Mm)/s-4)<1e-9 and abs((dist(Km,Lm)+dist(Lm,Mm))*2/s-20)<1e-9
assert abs(Km[0]-Nm[0]-(Lm[0]-Mm[0]))<1e-9
f=F(); f.fill([Km,Lm,Mm,Nm]); f.poly([A4,B4,C4,D4]); f.line(A4,C4,'dashed'); f.line(B4,D4,'dashed')
for (p,q_) in((A4,B4),(B4,C4),(C4,D4),(D4,A4)): f.tick(p,mid(p,q_)); f.tick(mid(p,q_),q_)
ic=cen([A4,B4,C4,D4])
for p,n in((A4,'A'),(B4,'B'),(C4,'C'),(D4,'D')): f.vl(n,p,sub(p,ic),.3)
for p,n in((Km,'K'),(Lm,'L'),(Mm,'M'),(Nm,'N')): f.vl(n,p,sub(p,ic),.28)
f.node(add(E4,(.0,-.32)),'$E$'); f.node(add(A4,(1.15,.2)),'$12$'); f.node(add(mid(E4,D4),(.3,-.22)),'$8$')
SK=f.svg()
q('0004',tipId='dg-orta-nokta',tip='Kenar orta noktalarını birleştiren dörtgen',z='orta',alt='Orta Noktalar',kaz='Dörtgenin kenar orta noktalarını birleştirerek elde edilen paralelkenarın çevresini köşegen uzunluklarından bulur.',
 kart='K-GDR-04 (orta noktalar, çevre) · AC = 12, BD = 8',
 metin='Şekildeki ABCD dörtgeninin kenarlarının orta noktaları K, L, M ve N dir. Dörtgenin köşegenleri [AC] ve [BD] çizilmiştir ve uzunlukları |AC| = 12 cm, |BD| = 8 cm dir.\nBuna göre, KLMN dörtgeninin çevresi kaç cm dir?',
 dogru=20,yan=[(10,'Yalnız iki komşu kenarı toplamış: 6 + 4 = 10.','dikkat'),(40,'KLMN nin kenarlarını köşegenlerin kendisi sanıp çevreyi 2 × (12 + 8) = 40 bulmuş.','bilgi'),(48,'Köşegenleri dik sanıp alan formülünü kullanmış: 12 × 8 ÷ 2 = 48.','bilgi'),(96,'Çevre yerine köşegenlerin çarpımını (12 × 8 = 96) yazmış.','dikkat')],
 istenen='KLMN dörtgeninin çevresi (cm).',
 ip=['KL doğru parçası hangi üçgende orta taban olur? Aynı düşünceyi diğer üç kenar için de dene.'],
 bilgi=[ORTAT],
 ad=[A('Orta tabanları bul','ABC üçgeninde K ve L orta nokta olduğundan [KL] // [AC] dir ve |KL| = |AC| ÷ 2 dir; ACD üçgeninde de |NM| = |AC| ÷ 2 dir.','|KL| = |NM| = 12 ÷ 2 = 6'),A('Diğer kenarları bul','ABD ve BCD üçgenlerinde aynı düşünce [BD] için geçerlidir.','|KN| = |LM| = 8 ÷ 2 = 4'),A('Çevreyi hesapla','KLMN nin karşılıklı kenarları eşittir.','2 × (6 + 4) = 20 cm')],
 puf='Dörtgenin kenar orta noktalarını birleştiren paralelkenarın çevresi, köşegenlerin toplamına eşittir.',sekil=SK)

# ---- 05 · orta · eşit köşegenler, orta noktalar dörtgeni
kartla('K-GDR-05','Eşit köşegenler ve orta noktalar','Köşegenleri eşit olan dörtgenin kenar orta noktaları eşkenar dörtgen oluşturur; her kenarı köşegenin yarısıdır, çevresi köşegenin iki katıdır.','Çevreyi köşegen sanmak; bir kenarı köşegen sanmak; yarıyı iki kez almak.','orta',4,'dg-orta-nokta','Kenar orta noktalarını birleştiren dörtgen')
cev5=36; kenar5=cev5//4; AC5=2*kenar5; assert AC5==18 and kenar5==9 and Fr(kenar5,2)==Fr(9,2) and 2*cev5==72
p5,r5,q5,t5=7,11,10,8; th=radians(70); u5=(1,0); v5=(cos(th),sin(th)); s=.26
E5=(0,0); A5=mul(u5,-p5*s); C5=mul(u5,r5*s); B5=mul(v5,q5*s); D5=mul(v5,-t5*s)
assert abs(dist(A5,C5)-dist(B5,D5))<1e-9 and abs(dist(A5,C5)/s-18)<1e-9 and konveks([A5,B5,C5,D5])
K5,L5,M5,N5=mid(A5,B5),mid(B5,C5),mid(C5,D5),mid(D5,A5)
assert all(abs(dist(a,b)/s-9)<1e-9 for a,b in((K5,L5),(L5,M5),(M5,N5),(N5,K5)))
f=F(); f.fill([K5,L5,M5,N5]); f.poly([A5,B5,C5,D5]); f.line(A5,C5,'dashed'); f.line(B5,D5,'dashed'); f.tick(A5,C5,2); f.tick(B5,D5,2)
ic=E5
for p,n in((A5,'A'),(B5,'B'),(C5,'C'),(D5,'D')): f.vl(n,p,sub(p,ic),.3)
for p,n in((K5,'K'),(L5,'L'),(M5,'M'),(N5,'N')): f.vl(n,p,sub(p,ic),.28)
SK=f.svg()
q('0005',tipId='dg-orta-nokta',tip='Kenar orta noktalarını birleştiren dörtgen',z='orta',alt='Eşit Köşegenler',kaz='Köşegenleri eşit uzunlukta olan dörtgenin kenar orta noktalarının oluşturduğu dörtgenin çevresinden köşegen uzunluğunu bulur.',
 kart='K-GDR-05 (orta noktalar, eşit köşegenler) · KLMN çevresi 36',
 metin='Şekildeki ABCD dörtgeninin köşegenleri [AC] ve [BD] eşit uzunluktadır. K, L, M ve N, dörtgenin kenarlarının orta noktalarıdır ve KLMN dörtgeninin çevresi 36 cm dir.\nBuna göre, |AC| kaç cm dir?',
 dogru=18,yan=[(Fr(9,2),'KLMN nin bir kenarını (36 ÷ 4 = 9) köşegenin yarısı sanıp bir kez daha ikiye bölmüş: 9 ÷ 2 = 4,5.','islem'),(9,'KLMN nin bir kenarını (36 ÷ 4 = 9) köşegen uzunluğu sanmış.','dikkat'),(36,'KLMN nin çevresini köşegen uzunluğu olarak yazmış.','dikkat'),(72,'Çevrenin iki katını köşegen sanmış: 2 × 36 = 72.','bilgi')],
 istenen='|AC| uzunluğu (cm).',
 ip=['KLMN nin bir kenarı, köşegenlerden biriyle nasıl ilişkili? Köşegenler eşit uzunlukta olunca KLMN nin kenarları hakkında ne söylenebilir?'],
 bilgi=[ORTAT],
 ad=[A('Kenarları köşegenlerle ilişkilendir','ABC üçgeninde K ve L orta nokta olduğundan |KL| = |AC| ÷ 2; benzer biçimde |LM| = |BD| ÷ 2.','|KL| = |NM| = |AC| ÷ 2 · |LM| = |KN| = |BD| ÷ 2'),A('Eşitliği kullan','|AC| = |BD| olduğundan KLMN nin dört kenarı eşittir.','KLMN nin her kenarı |AC| ÷ 2'),A('Çevreyi yaz','Dört eşit kenarın toplamı 36 cm dir.','4 × |AC| ÷ 2 = 36 → 2 × |AC| = 36'),A('Köşegeni bul','Eşitliği çöz.','|AC| = 18 cm')],
 puf='Kenar orta noktaları dörtgeninin çevresi, köşegenlerin toplamına eşittir; köşegenler eşitse çevre köşegenin iki katıdır.',sekil=SK)

# ---- 06 · zor · köşegenlerle bölünen dörtgenin alanı
kartla('K-GDR-06','Köşegenlerle alan bölüşümü','Dörtgen köşegenlerle dört üçgene ayrılır; karşılıklı iki üçgenin alanlarının çarpımı eşittir ya da ortak yükseklik oranlarıyla dördüncü üçgen bulunur.','Dördüncü üçgenin alanını komşu üçgene eşit sanmak; üç üçgeni toplayıp bırakmak.','zor',5,'dg-kosegen-bolme','Köşegenlerle bölünen dörtgenin alanı')
S1,S2,S3=9,6,8; S4=Fr(S1*S3,S2); assert S4==12 and S1+S2+S3+S4==35 and S1+S2+S3==23 and S1+S2+S3+S2==29 and S1+S2+S3+S3==31 and S1+S2+S3+S1==32
p6,r6,q6,t6=6,4,3,4   # AE, EC, BE, ED ; köşegenler arası açı çizimde 75°
th=radians(75); E6=(0,0); A6=(-p6*.4,0); C6=(r6*.4,0); dv=(cos(th),sin(th)); B6=mul(dv,q6*.4); D6=mul(dv,-t6*.4)
# alan oranları (sin75 ortak): ABE : BEC : CDE : AED = p·q : q·r : r·t : t·p
rr=[p6*q6,q6*r6,r6*t6,t6*p6]; assert rr==[18,12,16,24] and Fr(rr[0],rr[1])==Fr(S1,S2) and Fr(rr[2],rr[1])==Fr(S3,S2) and Fr(rr[3],rr[1])==Fr(S4,S2)
V6=[A6,B6,C6,D6]; assert konveks(V6)
f=F(); f.fill([A6,E6,D6]); f.poly(V6); f.line(A6,C6); f.line(B6,D6)
ic=cen(V6)
for p,n in zip(V6,'ABCD'): f.vl(n,p,sub(p,ic),.3)
f.node(add(E6,(-.05,.27)),'$E$')
f.node(cen([A6,E6,B6]),'\\footnotesize$9$'); f.node(cen([B6,E6,C6]),'\\footnotesize$6$'); f.node(add(cen([C6,E6,D6]),(.12,-.08)),'\\footnotesize$8$')
SK=f.svg()
q('0006',tipId='dg-kosegen-bolme',tip='Köşegenlerle bölünen dörtgenin alanı',z='zor',alt='Köşegenlerle Alan',kaz='Köşegenlerin dörtgeni ayırdığı üç üçgenin alanından dördüncüsünü ortak yükseklik oranlarıyla bulur.',
 kart='K-GDR-06 (köşegenlerle alan) · alanlar 9, 6, 8',
 metin='Şekilde köşegenleri E noktasında kesişen ABCD dörtgeni, köşegenleriyle dört üçgene ayrılmıştır. ABE, BEC ve CDE üçgenlerinin alanları sırasıyla 9 cm², 6 cm² ve 8 cm² dir.\nŞekil ölçekli değildir.\nBuna göre, ABCD dörtgeninin alanı kaç cm² dir?',
 dogru=35,yan=[(23,'Taralı AED üçgenini hesaba katmamış: 9 + 6 + 8 = 23.','dikkat'),(29,'Taralı üçgenin alanını BEC ile aynı (6) sanmış: 23 + 6 = 29.','bilgi'),(31,'Taralı üçgenin alanını CDE ile aynı (8) sanmış: 23 + 8 = 31.','bilgi'),(32,'Taralı üçgenin alanını ABE ile aynı (9) sanmış: 23 + 9 = 32.','bilgi')],
 istenen='ABCD dörtgeninin alanı (cm²).',
 ip=['B ve D köşelerinden [AC] doğrusuna inen yükseklikleri düşün; |AE| ile |EC| oranı alanlarla nasıl bulunur?'],
 bilgi=[ALANORAN],
 ad=[A('|AE| : |EC| oranını bul','B den [AC] ye inen yükseklik ABE ve BEC için ortaktır; alanlar tabanlarıyla orantılıdır.','|AE| : |EC| = 9 : 6 = 3 : 2'),A('Aynı oranı ikinci çiftte kullan','D den [AC] ye inen yükseklik AED ve CDE için ortaktır; tabanlar yine |AE| ve |EC| dir.','Alan(AED) : Alan(CDE) = 3 : 2'),A('Taralı üçgeni bul','CDE nin alanı 8 olduğundan 3 : 2 oranıyla AED hesaplanır.','Alan(AED) = 8 × 3 ÷ 2 = 12'),A('Alanları topla','Dört üçgenin alanı toplanır.','9 + 6 + 8 + 12 = 35 cm²')],
 puf='Köşegenlerin ayırdığı dört üçgende karşılıklı alanların çarpımları eşittir: 9 × 8 = 6 × x.',sekil=SK)

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
