"""TYT Geometri · hafif mod üretici. Şekil koordinatları hesaplanır, TikZ aynı değerlerden üretilir; her cevap ve çeldirici assert edilir."""
import sys,os,math,json
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
HV=os.path.join(GD,'..')
from math import sin,cos,tan,radians,degrees,atan2,sqrt,pi
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
def vtx(f,P_,name,ic,d=.3): f.vl(name,P_,sub(P_,ic),d)
def tri(a,b,c,s):
    """BC=a, CA=b, AB=c → A,B,C (B orijin, BC yatay), s ölçek"""
    x=(c*c+a*a-b*b)/(2*a); y=sqrt(c*c-x*x); return (x*s,y*s),(0,0),(a*s,0)
def tri_ac(B_,C_,Bd,Cd):
    """B ve C açıları (derece) ile A (B,C yatay)"""
    a=dist(B_,C_); Ad=180-Bd-Cd; c=a*sin(radians(Cd))/sin(radians(Ad))
    return (B_[0]+c*cos(radians(Bd)),B_[1]+c*sin(radians(Bd)))
def incenter(A_,B_,C_):
    a=dist(B_,C_); b=dist(A_,C_); c=dist(A_,B_); w=a+b+c
    return ((a*A_[0]+b*B_[0]+c*C_[0])/w,(a*A_[1]+b*B_[1]+c*C_[1])/w)
def rot(p,t,o=(0,0)):
    t=radians(t); d=sub(p,o); return (o[0]+d[0]*cos(t)-d[1]*sin(t),o[1]+d[0]*sin(t)+d[1]*cos(t))
def kesis(p1,p2,p3,p4):
    x1,y1=p1;x2,y2=p2;x3,y3=p3;x4,y4=p4; d=(x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
    return (((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4))/d,((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4))/d)
TIPK={}
def konu(k,ad): P.k=k; P.konu_adi=ad; H.KONU=ad
def kartla(id,alt,fikir,tuzak,z,adim,tipId,tip):
    kart(id,alt,fikir,tuzak,z,'şekilli',adim,tipId,tip,'ÖSYM 2018–2026 TYT Geometri soruları (yalnız mantık) · MEB 9–10. sınıf geometri'); TIPK[tipId]=P.k
def q(no,ad,kalip='şekilli',**k): mk(P,no,ad=ad,adim=len(ad),kalip=kalip,**k)
def bitir_geo(onek,konuad):
    for qq in P.ANA: qq['kardes']=None
    P.yaz(os.path.join(GD,f'{onek}-1.json'),f'/tmp/bos-{onek}.json')
    tipler={}
    for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=TIPK[c['tipId']]))['kartlar'].append(c['id'])
    json.dump(dict(konu=konuad,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 TYT Geometri çıkmış soruları (yalnız mantık), MEB 9–10. sınıf geometri müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar',f'{onek}.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler))
def dim(f,p,q_,t,n,off=.6):
    """ölçü oku: p–q doğru parçasını n yönünde off kadar ötele, iki uçlu ok + ortada etiket"""
    n=un(n); p2=add(p,mul(n,off)); q2=add(q_,mul(n,off))
    f.line(p,add(p,mul(n,off+.12)),'thin'); f.line(q_,add(q_,mul(n,off+.12)),'thin')
    f.line(p2,q2,'{Stealth[length=1.6mm]}-{Stealth[length=1.6mm]}'); f.node(add(mid(p2,q2),mul(n,.24)),t)
def arct(f,V,a,b,r,n=1):
    """yay + n çentik (eş açı işareti)"""
    f.arc(V,a,b,r)
    a1=degrees(atan2(a[1]-V[1],a[0]-V[0])); a2=degrees(atan2(b[1]-V[1],b[0]-V[0])); d=(a2-a1+180)%360-180; m=radians(a1+d/2)
    e=(cos(m),sin(m)); tg=(-e[1],e[0])
    for i in range(n):
        c=add(V,mul(e,r)); c=add(c,mul(tg,(i-(n-1)/2)*.08))
        f.line(add(c,mul(e,-.07)),add(c,mul(e,.07)))
P=Parti('benzerlik','Üçgende Benzerlik','geo|Üçgende Benzerlik',ders='TYT Geometri',idon='tytgeo')
TEMEL=B('Temel orantı','bir üçgende bir kenara paralel çizilen doğru diğer iki kenarı orantılı böler: DE // BC ise AD/DB = AE/EC. Örnek: AD = 2, DB = 4 ise AE : EC = 1 : 2 dir')
KEL=B('Kelebek benzerliği','AB // CD ve köşegen/kesenler E’de kesişiyorsa EAB ve EDC üçgenleri benzerdir: AE/ED = EB/EC = AB/DC. Örnek: AB = 2, DC = 4 ise kesişim noktası her kesenleri 1 : 2 böler')
OKL=B('Dik üçgende benzerlik','hipotenüse inen yükseklik üçgeni birbirine benzer iki dik üçgene ayırır; dik kenarın karesi, hipotenüsle o kenarın izdüşümünün çarpımına eşittir: c² = p × a. Örnek: c = 6, a = 10 ise p = 3,6')
ALN=B('Benzerlikte alan oranı','benzerlik oranı k ise alanlar oranı k² dir. Örnek: kenarlar oranı 2/3 ise alanlar oranı 4/9 dur')
THA=B('Thales teoremi','paralel doğrular iki kesenden orantılı parçalar ayırır: AB / BC = DE / EF. Örnek: AB = 2, BC = 3 ise DE = 4 iken EF = 6 dır')
AAB=B('AA benzerliği','iki açısı eşit olan üçgenler benzerdir; eşit açıların karşısındaki kenarlar karşılıklıdır. Örnek: m(ADE) = m(ACB) ve ortak A açısı varsa ADE ∼ ACB (D ↔ C, E ↔ B)')
PIS=B('Pisagor bağıntısı','dik üçgende dik kenarların kareleri toplamı hipotenüsün karesine eşittir. Örnek: 3, 4, 5 üçgeni için 3² + 4² = 5²')

# ===== 01 · temel orantı · kolay =====
konu('geo|Üçgende Benzerlik','Üçgende Benzerlik')
kartla('K-GBZ-01','Paralel doğrunun kestiği kenarlar','Kenara paralel doğru diğer kenarları orantılı böler; hangi parçanın hangi parçayla oranlandığına dikkat edilir.','Parça/parça yerine parça/bütün oranını karıştırmak; oranı ters yazmak.','kolay',2,'ge-bz-temel','Temel orantı teoremi')
AD1,DB1,AE1=6,3,8; EC1=AE1*DB1/AD1; assert EC1==4
A1,B1,C1=tri(14,12,9,.34)
D1=lerp(A1,B1,AD1/(AD1+DB1)); E1=lerp(A1,C1,AE1/12)
assert abs((E1[1]-D1[1]))<1e-9 and abs(dist(E1,C1)/.34-4)<1e-9
f=F(); f.poly([A1,B1,C1]); f.line(D1,E1); f.par(D1,E1); f.par(B1,C1); ic=cen([A1,B1,C1])
f.sl('$6$',A1,D1,ic,.28); f.sl('$3$',D1,B1,ic,.28); f.sl('$8$',A1,E1,ic,.28)
for n_,p_ in (('A',A1),('B',B1),('C',C1)): vtx(f,p_,n_,ic)
f.vl('D',D1,(-1,.3),.3); f.vl('E',E1,(1,.3),.3)
SK1=f.svg()
assert sorted([4,5,8,12,16])==sorted([EC1,AE1-(AD1-DB1),AE1,AE1*(AD1+DB1)/AD1,AE1*AD1/DB1])
q('0001',tipId='ge-bz-temel',tip='Temel orantı teoremi',z='kolay',alt='Temel Orantı',kaz='Kenara paralel doğrunun ayırdığı parçalarla orantı kurar.',
 kart='K-GBZ-01 (temel orantı) · AD = 6, DB = 3, AE = 8',
 metin='ABC üçgeninin [AB] kenarı üzerinde bir D, [AC] kenarı üzerinde bir E noktası alınıp [DE] doğru parçası, [BC] kenarına paralel olacak biçimde çizilmiştir. Şekilde bazı uzunluklar cm cinsinden verilmiştir; şekil ölçekli değildir.\nBuna göre, |EC| kaç cm’dir?',
 dogru=4,yan=[(5,'Orantı yerine farkları kullanmış: 8 − (6 − 3) = 5.','islem'),(8,'|EC| = |AE| yazmış (üçgeni ikizkenar sanmış).','bilgi'),(12,'|AC| = 8 × 9 ÷ 6 = 12 uzunluğunu bulup |EC| ye geçmemiş.','dikkat'),(16,'Oranı ters kurmuş: |EC| = 8 × 6 ÷ 3 = 16.','dikkat')],
 istenen='|EC| uzunluğu (cm).',
 ip=['[DE] // [BC] olduğunda [AB] ve [AC] kenarları hangi iki parçanın oranında bölünür? Aynı üçgen kenarında karşılıklı parçaları eşleştir.'],
 bilgi=[TEMEL],
 ad=[A('Orantıyı kur','[DE] // [BC] olduğundan kenarlar orantılı bölünür.','|AD| / |DB| = |AE| / |EC|'),A('Değerleri yaz','Verilenleri yerine koy.','6 / 3 = 8 / |EC|'),A('Çöz','İçler dışlar çarpımı.','|EC| = 8 × 3 ÷ 6 = 4')],
 puf='Paralel doğruda parçalar karşılıklı eşleşir: üstteki parça / alttaki parça, iki kenarda da aynıdır.',sekil=SK1)

# ===== 02 · kelebek · kolay · hikâyeli =====
kartla('K-GBZ-02','Kelebek benzerliği','Paralel iki doğru parçasını bağlayan çapraz doğrular kelebek benzerliği oluşturur; oranlar karşılıklı yazılır.','Oranı ters yazmak; toplamayı tercih etmek.','kolay',3,'ge-bz-kelebek','Kelebek benzerliği')
AE2,ED2,AB2=5,10,9; CD2=AB2*ED2/AE2; assert CD2==18 and AE2+ED2==15
d2=sqrt(225-81); assert abs(d2-12)<1e-9; s=.25
A2=(0,AB2*s); B2=(0,0); C2=(d2*s,CD2*s); D2=(d2*s,0)
E2=kesis(A2,D2,B2,C2)
assert abs(dist(A2,E2)/s-5)<1e-9 and abs(dist(E2,D2)/s-10)<1e-9
f=F(); f.line(A2,B2,'line width=1.6pt'); f.line(C2,D2,'line width=1.6pt'); f.line(A2,D2); f.line(B2,C2); f.par(A2,B2); f.par(C2,D2)
f.line((-.5,0),(d2*s+.5,0))
f.node(add(mid(A2,E2),(0,.28)),'$5$'); f.node(add(mid(E2,D2),(0,-.28)),'$10$'); f.node((-.4,AB2*s/2),'$9$')
f.vl('A',A2,(-.5,1),.3); f.vl('B',B2,(-1,-.5),.3); f.vl('C',C2,(.5,1),.3); f.vl('D',D2,(1,-.5),.3); f.vl('E',E2,(-1,0),.3)
SK2=f.svg()
assert sorted([4.5,14,18,36,45])==sorted([AB2*AE2/ED2,AB2+AE2,CD2,2*CD2,AB2*AE2])
q('0002',tipId='ge-bz-kelebek',tip='Kelebek benzerliği',z='kolay',kalip='hikâyeli',alt='Kelebek Benzerliği',kaz='Paralel direkler arası çapraz tellerin oluşturduğu benzer üçgenlerden uzunluk bulur.',
 kart='K-GBZ-02 (kelebek) · AE = 5, ED = 10, AB = 9',
 metin='Bir meydanda zemine dik, birbirine paralel [AB] ve [CD] direkleri dikilmiştir. A noktasından D noktasına ve B noktasından C noktasına birer tel gerilmiştir; teller E noktasında kesişmektedir. Şekil ölçekli değildir; uzunluklar metre cinsindendir.\nBuna göre, |CD| kaç metredir?',
 dogru=18,yan=[(4.5,'Oranı ters yazmış: |CD| = 9 × 5 ÷ 10 = 4,5.','dikkat'),(14,'Orantı yerine toplama kullanmış: 9 + 5 = 14.','islem'),(36,'Benzerlik oranını (2) iki kez uygulamış: 9 × 2 × 2 = 36.','islem'),(45,'|CD| = |AB| × |AE| = 45 çarpmış (oranı kullanmamış).','bilgi')],
 istenen='|CD| uzunluğu (m).',
 ip=['[AB] // [CD] olduğundan E noktasında hangi iki üçgen benzerdir? Karşılıklı kenarları bulurken A ile D’nin, B ile C’nin karşılıklı olduğunu kullan.'],
 bilgi=[KEL],
 ad=[A('Benzer üçgenleri bul','[AB] // [CD] olduğundan EAB ve EDC üçgenleri (kelebek) benzerdir.','EAB ∼ EDC (A ↔ D, B ↔ C)'),A('Oranı kur','Karşılıklı kenarların oranı sabittir.','|AE| / |ED| = 5 / 10 = |AB| / |CD| = 9 / |CD|'),A('|CD| yi bul','İçler dışlar çarpımı.','|CD| = 9 × 10 ÷ 5 = 18')],
 puf='Kelebekte paralel kenarların oranı, kesişim noktasından uçlara olan uzaklıkların (çapraz) oranına eşittir.',sekil=SK2)

# ===== 03 · dik üçgende benzerlik · kolay =====
kartla('K-GBZ-03','Hipotenüse inen yükseklik','Hipotenüse inen yükseklik benzer üçgenler oluşturur; dik kenarın karesi parça × hipotenüs verir.','Yükseklik ile parçayı karıştırmak; hipotenüsü parça sanmak.','kolay',3,'ge-bz-dik','Dik üçgende benzerlik')
AB3,AC3,BC3=15,20,25; BD3=AB3**2//BC3; DC3=BC3-BD3; AD3=AB3*AC3/BC3; assert BD3==9 and DC3==16 and AD3==12 and AC3**2==DC3*BC3
sx=.2; B3=(0,0); C3=(BC3*sx,0); A3=(BD3*sx,AD3*sx); D3=(BD3*sx,0)
assert abs(ang(A3,B3,C3)-90)<1e-9
f=F(); f.poly([A3,B3,C3]); f.line(A3,D3); f.dik(A3,B3,C3); f.dik(D3,A3,C3,.18); ic=cen([A3,B3,C3])
f.sl('$15$',A3,B3,C3,.3); f.sl('$20$',A3,C3,B3,.3)
f.vl('A',A3,(0,1),.32); f.vl('B',B3,(-1,-.6),.3); f.vl('C',C3,(1,-.6),.3); f.vl('D',D3,(0,-1),.3)
SK3=f.svg()
assert sorted([9,12,16,20,25])==sorted([BD3,AD3,DC3,AC3,BC3])
q('0003',tipId='ge-bz-dik',tip='Dik üçgende benzerlik',z='kolay',alt='Dik Üçgende Benzerlik',kaz='Hipotenüse inen yükseklikle oluşan benzerlikten bir parçanın uzunluğunu bulur.',
 kart='K-GBZ-03 (dik üçgende benzerlik) · AB = 15, AC = 20',
 metin='Şekilde ABC üçgeninde m(BAC) = 90° ve D noktası [BC] üzerinde olup [AD] ⊥ [BC] dir. Kenar uzunlukları |AB| = 15 cm ve |AC| = 20 cm dir; şekil ölçekli değildir.\nBuna göre, |DC| kaç cm’dir?',
 dogru=16,yan=[(9,'|DC| yerine |BD| = 15² ÷ 25 = 9 uzunluğunu bulmuş.','dikkat'),(12,'|DC| yerine yüksekliği |AD| = 15 × 20 ÷ 25 = 12 bulmuş.','dikkat'),(20,'|DC| = |AC| = 20 yazmış.','bilgi'),(25,'|DC| yerine hipotenüsü |BC| = 25 vermiş.','dikkat')],
 istenen='|DC| uzunluğu (cm).',
 ip=['Önce hipotenüsün uzunluğunu bul. Sonra ADC ve ABC üçgenlerinin benzerliğinden |AC|, |DC| ve |BC| arasında bir bağıntı yaz.'],
 bilgi=[OKL,PIS],
 ad=[A('Hipotenüsü bul','ABC dik üçgeninde Pisagor.','|BC|² = 15² + 20² = 625 → |BC| = 25'),A('Benzerliği kur','ADC ve BAC üçgenlerinin iki açısı eşit; C açısı ortak ve ikisi de dik.','|DC| / |AC| = |AC| / |BC|'),A('|DC| yi bul','Öklid bağıntısı: |AC|² = |DC| × |BC|.','400 = |DC| × 25 → |DC| = 16')],
 puf='Dik üçgende yükseklik çizilince üç benzer üçgen oluşur; dik kenarın karesi, onun hipotenüs üzerindeki izdüşümü ile hipotenüsün çarpımıdır.',sekil=SK3)

# ===== 04 · benzerlikte alan oranı · orta · hikâyeli =====
kartla('K-GBZ-04','Yamuk alanından üçgen alanı','Kenara paralel doğru benzer üçgen oluşturur; yamuk büyük üçgenin 8/9’udur, alan oranı benzerlik oranının karesiyle bulunur.','Alan oranı yerine uzunluk oranı kullanmak; yamuğu üçgenle karıştırmak.','orta',4,'ge-bz-alan','Benzerlikte alan oranı')
AD4,DB4=3,6; Y4=72; T4=Y4*9//8; aADE=T4//9; assert T4==81 and aADE==9 and Y4+aADE==T4
A4=(1.8,3.8); B4=(0,0); C4=(5.8,0); D4=lerp(A4,B4,3/9); E4=lerp(A4,C4,3/9)
assert abs(E4[1]-D4[1])<1e-9 and abs(alan([A4,D4,E4])/alan([A4,B4,C4])-1/9)<1e-9
f=F(); f.fill([D4,B4,C4,E4]); f.poly([A4,B4,C4]); f.line(D4,E4); f.par(D4,lerp(D4,E4,.5)); f.par(B4,lerp(B4,C4,.5)); ic=cen([A4,B4,C4])
f.sl('$3$',A4,D4,ic,.28); f.sl('$6$',D4,B4,ic,.28)
for n_,p_ in (('A',A4),('B',B4),('C',C4)): vtx(f,p_,n_,ic)
f.vl('D',D4,(-1,.3),.3); f.vl('E',E4,(1,.3),.3)
f.node((2.9,-.9),'Alan$(DBCE)=72\\ \\mathrm{cm}^2$')
SK4=f.svg()
assert sorted([8,9,18,24,36])==sorted([Y4/9,aADE,Y4/4,Y4/3,Y4/2])
q('0004',tipId='ge-bz-alan',tip='Benzerlikte alan oranı',z='orta',kalip='hikâyeli',alt='Yamuktan Üçgene Alan',kaz='Benzerlik oranının karesinden yamuk ve üçgen alanlarını ilişkilendirir.',
 kart='K-GBZ-04 (alan oranı, yamuktan üçgene) · AD : DB = 3 : 6, alan(DBCE) = 72',
 metin='Üçgen biçimli bir ABC bahçesi, [BC] kenarına paralel bir çit ile bir üçgene ve bir yamuğa ayrılmıştır. Çit, [AB] ve [AC] kenarlarını sırasıyla D ve E noktalarında kesmektedir; |AD| ve |DB| uzunlukları (metre) ile taralı DBCE yamuk bölümünün alanı şekilde verilmiştir. Şekil ölçekli değildir.\nBuna göre, ADE üçgeni biçimindeki bölümün alanı kaç m²’dir?',
 dogru=9,yan=[(8,'ADE’yi yamuğun 1/9’u sanmış: 72 ÷ 9 = 8.','bilgi'),(18,'Oran 1/2 karesini (1/4) yamuğa uygulamış: 72 ÷ 4 = 18.','bilgi'),(24,'Uzunluk oranını (1/3) yamuğa uygulamış: 72 ÷ 3 = 24.','bilgi'),(36,'ADE’yi yamuğun yarısı sanmış: 72 ÷ 2 = 36 (|AD| / |DB| = 1/2 oranını alan oranı yapmış).','bilgi')],
 istenen='ADE üçgeninin alanı (m²).',
 ip=['ADE ile ABC benzerdir. Benzerlik oranını bulduktan sonra alanlar için bu oranın kuvvetini düşün; yamuk, büyük üçgenle küçük üçgenin farkıdır.'],
 bilgi=[ALN,TEMEL],
 ad=[A('Benzerlik oranını bul','[DE] // [BC] olduğundan ADE ∼ ABC.','|AD| / |AB| = 3 / (3 + 6) = 1 / 3'),A('Alan oranını yaz','Alanlar oranı benzerlik oranının karesidir.','alan(ADE) / alan(ABC) = 1 / 9'),A('Yamuğu oranla ifade et','Yamuk = ABC − ADE.','alan(DBCE) = 9k − k = 8k = 72'),A('ADE’yi bul','k, ADE’nin alanıdır.','k = 9')],
 puf='Alan oranı = (benzerlik oranı)²; yamuk = büyük üçgen − küçük üçgen olduğundan, oran 1 : 9 ise yamuk 8 paydır.',sekil=SK4)

# ===== 05 · Thales · orta · hikâyeli =====
kartla('K-GBZ-05','Paralel doğrular ve Thales','Paralel doğrular iki kesende orantılı parçalar ayırır; bir kesendeki oranla diğerinin parçaları bulunur.','Parçaları toplam sanmak; farkla orantı kurmak.','orta',3,'ge-bz-thales','Thales teoremi (paralel doğrular)')
AB5,BC5,DE5=3,5,6; EF5=DE5*BC5/AB5; assert EF5==10 and DE5+EF5==16
sy=.4; A5=(0.1,8*sy); B5=(0.5,5*sy); C5=(0.9,0); D5=(3.1,8*sy); F5=(4.5,0); E5=lerp(D5,F5,3/8)
assert abs(E5[1]-5*sy)<1e-9
f=F()
for y_ in (0,5*sy,8*sy): f.line((-.5,y_),(5.2,y_))
f.line(A5,C5); f.line(D5,F5)
f.node((.1,2.2*sy+.05),'')
f.sl('$3$',A5,B5,(5,0),.0) if False else None
f.node((B5[0]-.45,(A5[1]+B5[1])/2+.0),'$3$'); f.node((C5[0]-.45,(B5[1]+C5[1])/2),'$5$'); f.node((E5[0]+.5,(D5[1]+E5[1])/2),'$6$')
f.vl('A',A5,(-1,.7),.3); f.vl('B',B5,(-1,.9),.3); f.vl('C',C5,(-.4,-1),.3); f.vl('D',D5,(-.5,1),.3); f.vl('E',E5,(1,.9),.3); f.vl('F',F5,(.4,-1),.3)
SK5=f.svg()
assert sorted([9.6,10,11,14,16])==sorted([(DE5+EF5*0)+DE5*AB5/BC5,EF5,DE5+BC5,DE5+(DE5+BC5-AB5),DE5+EF5])
q('0005',tipId='ge-bz-thales',tip='Thales teoremi (paralel doğrular)',z='orta',kalip='hikâyeli',alt='Thales Teoremi',kaz='Paralel doğruların kesenlerde ayırdığı orantılı parçalardan uzunluk bulur.',
 kart='K-GBZ-05 (Thales) · AB = 3, BC = 5, DE = 6',
 metin='Bir şehirde birbirine paralel üç cadde, [AC] ve [DF] doğrusal yolları tarafından sırasıyla A, B, C ve D, E, F noktalarında kesilmektedir. A ile B arası 3 km, B ile C arası 5 km, D ile E arası 6 km ölçülmüştür. Şekil ölçekli değildir.\nBuna göre, D ile F arasındaki yol uzunluğu kaç km’dir?',
 dogru=16,yan=[(9.6,'Oranı ters yazmış: |EF| = 6 × 3 ÷ 5 = 3,6 ve |DF| = 6 + 3,6 = 9,6.','dikkat'),(10,'İstenen |DF| yerine |EF| uzunluğunu vermiş.','dikkat'),(11,'|DE| + |BC| = 6 + 5 = 11 yazmış (farklı yoldaki uzunluğu eklemiş).','bilgi'),(14,'Orantı yerine farkı kullanmış: |EF| = 5 + (6 − 3) = 8 ve 6 + 8 = 14.','islem')],
 istenen='|DF| uzunluğu (km).',
 ip=['Paralel doğruların kesenlerde ayırdığı parçalar birbirleriyle orantılıdır: yukarıdaki parçalar kendi aralarında, aşağıdakilerle aynı oranı verir.'],
 bilgi=[THA],
 ad=[A('Orantıyı kur','Üç paralel doğru iki yolu orantılı böler.','|AB| / |BC| = |DE| / |EF| → 3 / 5 = 6 / |EF|'),A('|EF| yi bul','İçler dışlar çarpımı.','|EF| = 6 × 5 ÷ 3 = 10'),A('|DF| yi yaz','Tüm yol iki parçanın toplamıdır.','|DF| = 6 + 10 = 16')],
 puf='Thales’te kesenlerin parçaları karşılıklı orantılıdır; bir kesendeki oranı diğerine taşı, sonra toplam sorulmuşsa parçaları topla.',sekil=SK5)

# ===== 06 · iç içe benzer üçgenler · orta =====
kartla('K-GBZ-06','Eşit açıdan iç içe benzerlik','Ortak köşe ve bir eşit açı AA benzerliği verir; karşılıklı kenarlar doğru eşleştirilir.','Köşeleri harf sırasıyla eşleştirmek (ADE ∼ ABC demek); parçayı bütün sanmak.','orta',4,'ge-bz-ice','İç içe benzer üçgenler')
AD6,DB6,AE6=4,5,3; AB6=AD6+DB6; AC6=AD6*0+AE6*AB6/AD6*0+AD6*AB6/AE6*0
AC6=12; assert AD6/AC6==AE6/AB6 and AC6-AE6==9
A6_,B6_,C6_=tri(14,AC6,AB6,.3); 
# A köşesi tepede: B,C tabanda
D6_=lerp(A6_,B6_,AD6/AB6); E6_=lerp(A6_,C6_,AE6/AC6)
assert abs(ang(D6_,A6_,E6_)-ang(C6_,A6_,B6_))<1e-9
f=F(); f.poly([A6_,B6_,C6_]); f.line(D6_,E6_); ic=cen([A6_,B6_,C6_])
f.arc(D6_,A6_,E6_,.4); f.arc(C6_,A6_,B6_,.45)
f.sl('$4$',A6_,D6_,ic,.28); f.sl('$5$',D6_,B6_,ic,.28); f.sl('$3$',A6_,E6_,ic,.28)
for n_,p_ in (('A',A6_),('B',B6_),('C',C6_)): vtx(f,p_,n_,ic)
f.vl('D',D6_,(-1,.2),.3); f.vl('E',E6_,(1,.1),.3)
SK6=f.svg()
assert sorted([3,3.75,5,9,12])==sorted([AE6,AE6*AB6/AD6-AE6,DB6,AC6-AE6,AC6])
q('0006',tipId='ge-bz-ice',tip='İç içe benzer üçgenler',z='orta',alt='İç İçe Benzer Üçgenler',kaz='Eşit açılardan benzerliği kurup eşleştirmeyi doğru yaparak uzunluk bulur.',
 kart='K-GBZ-06 (iç içe benzerlik) · AD = 4, DB = 5, AE = 3',
 metin='ABC üçgeninde D noktası [AB] üzerinde, E noktası [AC] üzerindedir ve şekilde yay işaretleriyle gösterildiği gibi m(ADE) = m(ACB) dir. Şekil ölçekli değildir; uzunluklar cm cinsindendir.\nBuna göre, |EC| kaç cm’dir?',
 dogru=9,yan=[(3,'|EC| = |AE| = 3 yazmış.','bilgi'),(3.75,'ADE ∼ ABC sanıp |AD| / |AB| = |AE| / |AC| yazmış: |AC| = 6,75 ve |EC| = 3,75.','dikkat'),(5,'Karşılıklı kenar sanıp |EC| = |DB| = 5 yazmış.','bilgi'),(12,'|EC| yerine |AC| = 12 uzunluğunu vermiş.','dikkat')],
 istenen='|EC| uzunluğu (cm).',
 ip=['Hangi iki üçgen A açısını ortak kullanıyor ve bir çift açısı daha eşit? D noktasının hangi köşeye karşılık geldiğine dikkat et.'],
 bilgi=[AAB],
 ad=[A('Benzerliği belirle','A açısı ortak, m(ADE) = m(ACB): ADE ∼ ACB (D ↔ C, E ↔ B).','|AD| / |AC| = |AE| / |AB|'),A('|AC| yi bul','|AB| = 4 + 5 = 9 cm.','4 / |AC| = 3 / 9 → |AC| = 12'),A('|EC| yi hesapla','E, [AC] üzerinde olduğundan fark alınır.','|EC| = 12 − 3 = 9')],
 puf='İç içe üçgenlerde eşit açının köşesini doğru eşle: ADE ∼ ACB yazılır, ADE ∼ ABC değil.',sekil=SK6)

# ===== 07 · kelebek + alan · orta =====
kartla('K-GBZ-07','Kelebekte alan oranı','Kelebek benzerliğinde alanlar oranı benzerlik oranının karesidir; verilen üçgenden karşıt üçgenin alanına geçilir.','Alanı oranla (karesiz) çarpmak; oranı ters kurmak; pay ya da paydanın karesini unutmak.','orta',3,'ge-bz-alan','Benzerlikte alan oranı')
aABE=8; AB7,DC7=2,5; aCDE=aABE*DC7**2/AB7**2; assert aCDE==50
sx=.6; D7=(0,0); C7=(DC7*sx,0); A7=((DC7-AB7)*sx/2,2.4); B7=(A7[0]+AB7*sx,2.4)
E7=kesis(A7,C7,B7,D7)
assert abs(dist(A7,E7)/dist(E7,C7)-AB7/DC7)<1e-9
assert abs(alan([C7,D7,E7])/alan([A7,B7,E7])-(DC7/AB7)**2)<1e-9
f=F(); f.fill([C7,D7,E7]); f.line(A7,B7); f.line(D7,C7); f.line(A7,C7); f.line(B7,D7); f.par(A7,B7); f.par(D7,C7)
f.node((mid(A7,B7)[0],A7[1]+.3),'$2$'); f.node((mid(D7,C7)[0],-.3),'$5$')
f.vl('A',A7,(-.6,1),.3); f.vl('B',B7,(.6,1),.3); f.vl('C',C7,(.6,-1),.3); f.vl('D',D7,(-.6,-1),.3); f.vl('E',E7,(-1,.1),.32)
SK7=f.svg()
assert sorted([16,20,40,50,100])==sorted([aABE*2,aABE*DC7/AB7,aABE*DC7,aCDE,aABE*DC7**2/AB7])
q('0007',tipId='ge-bz-alan',tip='Benzerlikte alan oranı',z='orta',alt='Kelebekte Alan',kaz='Kelebek benzerliğinde benzerlik oranının karesiyle karşıt üçgenin alanını bulur.',
 kart='K-GBZ-07 (kelebek, alan oranı) · AB = 2, DC = 5, alan(ABE) = 8',
 metin='Şekilde [AB] // [DC] dir; [AC] ve [BD] doğru parçaları E noktasında kesişmektedir. |AB| = 2 cm, |DC| = 5 cm ve ABE üçgeninin alanı 8 cm² dir. Şekil ölçekli değildir.\nBuna göre, taralı CDE üçgeninin alanı kaç cm²’dir?',
 dogru=50,yan=[(16,'Benzerlik oranını 2 sanıp alanı 8 × 2 = 16 bulmuş.','bilgi'),(20,'Alanı oranla (5/2) çarpmış, oranın karesini almamış: 8 × 5 ÷ 2 = 20.','islem'),(40,'Alanı |DC| ile çarpmış: 8 × 5 = 40 (karşılıklı oran kurmamış).','bilgi'),(100,'Oranın yalnız payının karesini almış: 8 × 25 ÷ 2 = 100.','islem')],
 istenen='CDE üçgeninin alanı (cm²).',
 ip=['EAB ve EDC üçgenleri benzerdir. Benzerlik oranını bul; alanlar için bu oranın hangi kuvveti kullanılır?'],
 bilgi=[KEL,ALN],
 ad=[A('Benzerliği kur','[AB] // [DC] olduğundan EAB ∼ EDC (kelebek).','k = |DC| / |AB| = 5 / 2'),A('Alan oranını yaz','Alanlar oranı benzerlik oranının karesidir.','alan(CDE) / alan(ABE) = (5 / 2)² = 25 / 4'),A('Alanı hesapla','Verilen alanı oranla çarp.','alan(CDE) = 8 × 25 ÷ 4 = 50')],
 puf='Kelebekte uzunluk oranı k ise alan oranı k² dir; küçük üçgenden büyüğe giderken k² ile çarp.',sekil=SK7)

# ===== 08 · üçgene yerleştirilmiş kare · zor · hikâyeli =====
kartla('K-GBZ-08','Üçgenin içine yerleştirilen kare','Karenin üst kenarı tabana paralel olduğundan benzerlik kurulur; oran, yükseklik ve kare kenarı üzerinden yazılır.','Karenin kenarını yüksekliğin ya da tabanın bir kesri sanmak; yüksekliği kare yüksekliğiyle karıştırmak.','zor',4,'ge-bz-ice','İç içe benzer üçgenler')
b8,h8=12,6; a8=b8*h8/(b8+h8); assert a8==4
sx=.36; B8=(0,0); C8=(b8*sx,0); A8=(4*sx,h8*sx)
D8=lerp(A8,B8,a8/h8); E8=lerp(A8,C8,a8/h8); G8=(D8[0],0); F8=(E8[0],0)
# D = A + (B-A)*t ; kare üst kenarı y = a8 -> t=(h-a)/h
D8=lerp(A8,B8,(h8-a8)/h8); E8=lerp(A8,C8,(h8-a8)/h8); G8=(D8[0],0); F8=(E8[0],0)
assert abs(D8[1]-a8*sx)<1e-9 and abs((E8[0]-D8[0])/sx-a8)<1e-9
H8=(A8[0],0)
f=F(); f.poly([A8,B8,C8]); f.poly([D8,E8,F8,G8]); f.line(A8,H8,'dashed'); f.dik(H8,A8,C8,.16)
f.node((C8[0]/2,-.8),'$12$')
xl=-.7; f.line(B8,(xl-.1,0),'thin'); f.line(A8,(xl-.1,A8[1]),'thin'); f.line((xl,0),(xl,A8[1]),'{Stealth[length=1.6mm]}-{Stealth[length=1.6mm]}'); f.node((xl-.3,A8[1]/2),'$6$')
for n_,p_ in (('A',A8),('B',B8),('C',C8)): vtx(f,p_,n_,cen([A8,B8,C8]))
f.vl('D',D8,(-.8,.8),.3); f.vl('E',E8,(.8,.8),.3); f.vl('F',F8,(.5,-1),.3); f.vl('G',G8,(-.5,-1),.3)
SK8=f.svg()
assert sorted([4,6,8,12,18])==sorted([a8,b8/2,b8*2/3,b8,b8+h8])
q('0008',tipId='ge-bz-ice',tip='İç içe benzer üçgenler',z='zor',kalip='hikâyeli',alt='Üçgenin İçindeki Kare',kaz='Üçgenin içindeki karenin kenarını benzerlikle hesaplar.',
 kart='K-GBZ-08 (üçgene kare) · taban 12, yükseklik 6',
 metin='Tabanı 12 cm ve tabana ait yüksekliği 6 cm olan ABC biçimli kartondan, bir kenarı tabanın üzerinde olacak biçimde DEFG karesi kesiliyor. Karenin D ve E köşeleri [AB] ve [AC] kenarları üzerindedir; F ve G köşeleri [BC] üzerindedir. Şekil ölçekli değildir.\nBuna göre, karenin bir kenarının uzunluğu kaç cm’dir?',
 dogru=4,yan=[(6,'Kenarı tabanın yarısı sanmış: 12 ÷ 2 = 6.','bilgi'),(8,'Kenarı tabanın 2/3’ü sanmış: 12 × 2 ÷ 3 = 8.','bilgi'),(12,'Karenin kenarını tabana eşit almış.','dikkat'),(18,'Taban ile yüksekliği toplamış: 12 + 6 = 18.','dikkat')],
 istenen='Karenin kenar uzunluğu (cm).',
 ip=['Karenin üst kenarı [DE], [BC] ye paraleldir; bu paralel hangi iki üçgeni benzer yapar? Kare kenarına a deyip yükseklikleri a cinsinden yaz.'],
 bilgi=[TEMEL,AAB],
 ad=[A('Değişkeni seç','Karenin kenarına a diyelim; A’dan [DE] ye uzaklık 6 − a olur.','|DE| = a'),A('Benzerliği kur','[DE] // [BC] olduğundan ADE ∼ ABC; oran, yüksekliklerin oranıdır.','a / 12 = (6 − a) / 6'),A('Denklemi çöz','İçler dışlar çarpımı.','6a = 12 × (6 − a) → 18a = 72'),A('Kenarı yaz','Eşitliği çöz.','a = 4')],
 puf='Üçgenin içine yerleştirilen karede tabana paralel kenar benzerlik verir: kenar / taban = (yükseklik − kenar) / yükseklik.',sekil=SK8)

# ===== 09 · alanlardan kenar · orta =====
kartla('K-GBZ-09','Alanlardan benzerlik oranı','Alanlar oranının karekökü uzunluk oranıdır; karşılıklı kenarlar bu oranla bulunur.','Alan oranını doğrudan uzunluk oranı sanmak; oranı ters yazmak.','orta',3,'ge-bz-alan','Benzerlikte alan oranı')
aA9,aD9,BC9=12,27,6; k9=sqrt(aA9/aD9); assert abs(k9-2/3)<1e-12; EF9=BC9*3/2; assert EF9==9
sx=.38; B9=(0,0); C9=(6*sx,0); A9=(2*sx,4*sx); k=1.5
E9=add((4.1,0),(0,0)); F9=(E9[0]+9*sx,0); D9=(E9[0]+2*sx*k,4*sx*k)
assert abs(alan([A9,B9,C9])-alan([D9,E9,F9])*4/9)<1e-9
f=F(); f.poly([A9,B9,C9]); f.poly([D9,E9,F9]); i1=cen([A9,B9,C9]); i2=cen([D9,E9,F9])
f.node(add(i1,(0,-.12)),'$12$ cm$^2$'); f.node(add(i2,(0,-.12)),'$27$ cm$^2$'); f.node((3*sx,-.32),'$6$ cm')
for n_,p_ in (('A',A9),('B',B9),('C',C9)): vtx(f,p_,n_,i1)
for n_,p_ in (('D',D9),('E',E9),('F',F9)): vtx(f,p_,n_,i2)
SK9=f.svg()
assert sorted([4,9,13.5,18,21])==sorted([BC9*aA9/aD9*3/2*0+BC9*2/3,EF9,BC9*aD9/aA9,BC9*3,BC9+(aD9-aA9)])
q('0009',tipId='ge-bz-alan',tip='Benzerlikte alan oranı',z='orta',alt='Alandan Uzunluğa',kaz='Benzer üçgenlerin alanlarından benzerlik oranını bulup karşılıklı kenarı hesaplar.',
 kart='K-GBZ-09 (alan oranı → uzunluk oranı) · 12 ve 27 cm², |BC| = 6',
 metin='Şekildeki ABC ve DEF üçgenleri benzerdir (A ↔ D, B ↔ E, C ↔ F). Üçgenlerin alanları sırasıyla 12 cm² ve 27 cm², |BC| = 6 cm dir. Şekil ölçekli değildir.\nBuna göre, |EF| kaç cm’dir?',
 dogru=9,yan=[(4,'Benzerlik oranını ters yazıp 6 × 2 ÷ 3 = 4 bulmuş.','dikkat'),(13.5,'Alan oranını (27 / 12) doğrudan uzunluk oranı yapmış: 6 × 27 ÷ 12.','bilgi'),(18,'Alan oranının karekökünü 3 alıp 6 × 3 = 18 yazmış.','islem'),(21,'Alanlar farkını (27 − 12 = 15) |BC| ye eklemiş: 6 + 15 = 21.','dikkat')],
 istenen='|EF| uzunluğu (cm).',
 ip=['Benzer şekillerde alan oranı, uzunluk oranıyla nasıl bağlantılıdır? Önce uzunluk oranını bul, sonra |BC| ye karşılık gelen kenarı hesapla.'],
 bilgi=[ALN],
 ad=[A('Alan oranını yaz','Alanlar oranı.','alan(DEF) / alan(ABC) = 27 / 12 = 9 / 4'),A('Uzunluk oranını bul','Uzunluk oranı alan oranının karekökü.','k = √(9 / 4) = 3 / 2'),A('|EF| yi hesapla','|EF|, |BC| nin karşılığıdır.','|EF| = 6 × 3 ÷ 2 = 9')],
 puf='Alan oranından uzunluk oranına geçerken kare kök al; uzunluk oranı büyük şekle ait olan taraf pay olmalıdır.',sekil=SK9)

# ===== 10 · yamukta köşegen kesişiminden paralel · zor =====
kartla('K-GBZ-10','Köşegen kesişiminden geçen paralel','Köşegenlerin kesişiminden tabana paralel çizilen doğru parçası iki tabanın harmonik ortalamasına eşittir; benzerliklerle bulunur.','Aritmetik ortalama kullanmak; doğru parçasının yalnız yarısını bulmak.','zor',5,'ge-bz-yamuk','Yamukta köşegenlerin kesişiminden geçen paralel')
a10,c10=6,12; EF10=2*a10*c10/(a10+c10); assert EF10==8
sx=.38; D10=(0,0); C10=(12*sx,0); A10=(2.0*sx,5.2); B10=(A10[0]+6*sx,5.2)
E10=kesis(A10,C10,B10,D10)
F10=kesis(A10,D10,E10,add(E10,(1,0))); G10=kesis(B10,C10,E10,add(E10,(1,0)))
assert abs(dist(F10,G10)/sx-8)<1e-9 and abs(dist(F10,E10)-dist(E10,G10))<1e-9
f=F(); f.poly([A10,B10,C10,D10]); f.line(A10,C10); f.line(B10,D10); f.line(F10,G10); f.par(A10,B10); f.par(D10,C10); f.par(F10,lerp(F10,G10,.4))
f.node((mid(A10,B10)[0],A10[1]+.3),'$6$'); f.node((mid(D10,C10)[0],-.3),'$12$')
for n_,p_ in (('A',A10),('B',B10),('C',C10),('D',D10)): vtx(f,p_,n_,cen([A10,B10,C10,D10]))
f.vl('F',F10,(-1,0),.3); f.vl('G',G10,(1,0),.3); f.vl('E',E10,(.1,-1.2),.28)
SK10=f.svg()
assert sorted([4,8,9,12,18])==sorted([EF10/2,EF10,(a10+c10)/2,c10,a10+c10])
q('0010',tipId='ge-bz-yamuk',tip='Yamukta köşegenlerin kesişiminden geçen paralel',z='zor',alt='Yamukta Paralel Doğru Parçası',kaz='Yamukta köşegen kesişiminden çizilen paralelin uzunluğunu iki benzerlikle bulur.',
 kart='K-GBZ-10 (köşegen kesişiminden paralel) · AB = 6, DC = 12',
 metin='Şekildeki ABCD yamuğunda [AB] // [DC] dir ve köşegenler E noktasında kesişmektedir. E noktasından [AB] ye çizilen paralel doğru [AD] yi F, [BC] yi G noktasında kesmektedir. Şekil ölçekli değildir; uzunluklar cm cinsindendir.\nBuna göre, |FG| kaç cm’dir?',
 dogru=8,yan=[(4,'Yalnız |FE| = 4 uzunluğunu bulup |EG| yi eklememiş.','dikkat'),(9,'İki tabanın aritmetik ortalamasını almış: (6 + 12) ÷ 2 = 9.','bilgi'),(12,'|FG| = |DC| = 12 yazmış.','bilgi'),(18,'İki tabanı toplayıp 6 + 12 = 18 yazmış.','bilgi')],
 istenen='|FG| uzunluğu (cm).',
 ip=['EAB ∼ EDC benzerliğinden |AE| / |AC| oranını bul; sonra ADC üçgeninde [FE] // [DC] olduğunu kullan.'],
 bilgi=[KEL,TEMEL],
 ad=[A('Köşegen oranını bul','EAB ∼ ECD (kelebek): |AE| / |EC| = |AB| / |DC| = 6 / 12.','|AE| : |EC| = 1 : 2 → |AE| / |AC| = 1 / 3'),A('|FE| yi bul','ADC üçgeninde [FE] // [DC] olduğundan AFE ∼ ADC ve |FE| / |DC| = |AE| / |AC|.','|FE| = 12 × 1 ÷ 3 = 4'),A('|EG| yi bul','BDC üçgeninde [EG] // [DC] olduğundan |EG| / |DC| = |BE| / |BD| = 1 / 3.','|EG| = 12 × 1 ÷ 3 = 4'),A('Toplamı yaz','Paralel parçası iki yarımın toplamıdır.','|FG| = 4 + 4 = 8')],
 puf='Yamukta köşegenlerin kesişiminden tabanlara paralel parça, kesişim noktasında ikiye bölünür ve uzunluğu 2ab/(a+b) dir.',sekil=SK10)
bitir_geo('benzerlik','Üçgende Benzerlik')
