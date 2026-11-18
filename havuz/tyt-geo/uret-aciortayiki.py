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
def foot(P_,A_,B_):
    d=un(sub(B_,A_)); t=(P_[0]-A_[0])*d[0]+(P_[1]-A_[1])*d[1]; return add(A_,mul(d,t))
def ok(a,b,t=1e-9): assert abs(a-b)<t,(a,b)
def bis(A_,B_,C_): return lerp(B_,C_,dist(A_,B_)/(dist(A_,B_)+dist(A_,C_)))   # A köşesinden iç açıortay ayağı
ONEK='aciortayiki'; KONU_AD='Açıortay'
P=Parti(ONEK,KONU_AD,'geo|Açıortay',ders='TYT Geometri',idon='tytgeo')
konu('geo|Açıortay','Açıortay')
IC=B('İç açıortay teoremi','üçgenin bir iç açıortayı karşı kenarı, komşu kenarların oranında böler: [AD] iç açıortay ise |BD| / |DC| = |AB| / |AC| dir. Örnek: |AB| = 5 ve |AC| = 7 ise |BD| : |DC| = 5 : 7 dir')
DISB=B('Dış açıortay teoremi','üçgenin bir dış açıortayı, karşı kenarın uzantısını komşu kenarların oranında dıştan böler: A köşesindeki dış açıortay BC doğrusunu E de keserse |EB| / |EC| = |AB| / |AC| dir. Örnek: |AB| = 2 ve |AC| = 3 ise E nin B ve C ye uzaklıkları 2 : 3 oranındadır')
ACI=B('Üçgende açılar','bir üçgenin iç açılarının toplamı 180° dir. Bir dış açı, kendisine komşu olmayan iki iç açının toplamına eşittir. Açıortay, bir açıyı iki eş açıya ayırır. Örnek: iç açıları 30° ve 80° olan üçgenin üçüncü açısı 70° dir')
PARB=B('Paralel doğrular ve ikizkenar üçgen','iki paralel doğruyu bir kesen kesişince iç ters açılar eşittir; bir üçgende iki açı eşitse bu açıların karşısındaki kenarlar da eşittir. Örnek: bir üçgenin iki açısı 40° ise bu açıların karşısındaki kenarlar eşit uzunluktadır')
UZ=B('Açıortay ve uzaklık','bir açının açıortayı üzerindeki her nokta açının iki koluna eşit uzaklıktadır; uzaklık, noktadan kola indirilen dikmenin uzunluğudur')
TABAN=B('Üçgenin alanı','alan = taban × yükseklik ÷ 2 dir. Her kenar taban seçilebilir; yükseklik, o kenara karşı köşeden kenarın doğrultusuna inen dikmedir. Örnek: tabanı 9 cm, yüksekliği 4 cm olan üçgenin alanı 18 cm² dir')
SINUSA=B('Sinüs ile alan','iki kenarı a, b ve aralarındaki açısı C olan üçgenin alanı ½ × a × b × sin C dir. Örnek: kenarları 5 ve 6, aradaki açısı 90° olan üçgenin alanı ½ × 5 × 6 × 1 = 15')
KORB=B('Kenarortay','bir köşeyi karşı kenarın orta noktasına bağlayan doğru parçasıdır. Örnek: [KL] nin orta noktası M ise |KM| = |ML| dir')
PKENAR=B('Paralelkenar','karşılıklı kenarları paralel ve eşit olan dörtgendir; komşu açıları bütünler, karşılıklı açıları eşittir. Örnek: bir açısı 70° olan paralelkenarın komşu açısı 110° dir')

# ===== 01 · kolay · iç açıortay teoremiyle kenar bulma
kartla('K-GAI-01','Parçalardan kenar','İç açıortay teoremi, bilinmeyen komşu kenarı parçaların oranından bulmaya da elverir.','Oranı ters kurmak; kenar parçalarını komşu kenarlarla eşleştirmek.','kolay',3,'ai-oran','İç açıortay teoremiyle uzunluk')
s=.3; A1,B1,C1=tri(16,15,9,s); D1=bis(A1,B1,C1)
ok(dist(B1,D1)/s,6); ok(dist(D1,C1)/s,10); ok(ang(A1,B1,D1),ang(A1,D1,C1)); ok(dist(A1,C1)/s,15)
f=F(); f.poly([A1,B1,C1]); f.line(A1,D1); ic=cen([A1,B1,C1]); arct(f,A1,B1,D1,.55,1); arct(f,A1,D1,C1,.55,1)
f.sl('$9$',A1,B1,ic,.28); dim(f,B1,D1,'$6$',(0,-1),.55); dim(f,D1,C1,'$10$',(0,-1),.55)
for n_,p_ in (('A',A1),('B',B1),('C',C1)): vtx(f,p_,n_,ic)
f.vl('D',D1,(1,.7),.3)
SK=f.svg()
q('0001',tipId='ai-oran',tip='İç açıortay teoremiyle uzunluk',z='kolay',alt='Parçalardan Kenara',kaz='İç açıortayın ayırdığı parçaların uzunluklarından üçgenin bilinmeyen kenarını bulur.',
 kart='K-GAI-01 (parçalardan komşu kenar) · BD = 6, DC = 10',
 metin='Şekilde ABC üçgeninin [AD] doğru parçası, A açısının iç açıortayıdır ve D noktası [BC] üzerindedir. |AB| = 9 cm, |BD| = 6 cm ve |DC| = 10 cm dir.\nŞekil ölçekli değildir.\nBuna göre, |AC| kaç cm dir?',
 dogru=15,yan=[(5.4,'Oranı ters kurmuş: |AC| = 9 × 6 ÷ 10 = 5,4.','dikkat'),(9,'ABC üçgenini ikizkenar sanıp |AC| yi |AB| ye eşit almış.','bilgi'),(10,'Karşı kenarın parçası olan |DC| = 10 uzunluğunu |AC| sanmış.','dikkat'),(24,'Kenarları yanlış eşleyip |AB| / |BD| = |AC| / |BC| yazmış: 9 × 16 ÷ 6 = 24.','bilgi')],
 istenen='|AC| uzunluğu (cm).',
 ip=['[AD] açıortay olduğuna göre |BD| ve |DC| parçalarının oranı hangi iki kenarın oranına bağlanabilir?'],
 bilgi=[IC],
 ad=[A('Oranı yaz','[AD] iç açıortay olduğundan parçaların oranı komşu kenarların oranına eşittir.','|BD| / |DC| = |AB| / |AC|'),A('Değerleri yerleştir','Verilen uzunlukları yaz.','6 / 10 = 9 / |AC|'),A('|AC| yi bul','İçler dışlar çarpımı yap.','6 × |AC| = 90 → |AC| = 15 cm')],
 puf='Açıortay oranını yazarken pay ve paydanın hangi kenarlara ait olduğunu şekil üzerinde işaretle.',sekil=SK)

# ===== 02 · kolay · iç açıortay ve açı
kartla('K-GAI-02','İç açıortay ve dış açı','Açıortay açıyı yarılar; ADC açısı, ABD üçgeninin dış açısıdır.','Bütünler açıyı (ADB) cevap sanmak; yarılanan açıyı değil bütününü kullanmak.','kolay',3,'ai-aci','Açıortay ve açı hesabı')
B2=(0,0); C2=(6.0,0); A2=tri_ac(B2,C2,50,70); D2=bis(A2,B2,C2)
ok(ang(A2,B2,D2),30); ok(ang(D2,A2,C2),80)
f=F(); f.poly([A2,B2,C2]); f.line(A2,D2); ic=cen([A2,B2,C2])
arct(f,A2,B2,D2,.55,1); arct(f,A2,D2,C2,.55,1); f.arc(B2,C2,A2,.7,'$50^\\circ$',1.25); f.arc(C2,A2,B2,.7,'$70^\\circ$',1.25); f.arc(D2,A2,C2,.45,'$x$',.8)
for n_,p_ in (('A',A2),('B',B2),('C',C2)): vtx(f,p_,n_,ic)
f.vl('D',D2,(0,-1),.3)
SK=f.svg()
q('0002',tipId='ai-aci',tip='Açıortay ve açı hesabı',z='kolay',alt='İç Açıortay ve Açı',kaz='Üçgenin iç açıortayıyla oluşan açıları hesaplar.',
 kart='K-GAI-02 (iç açıortay, dış açı) · B = 50°, C = 70°',
 metin='Şekilde ABC üçgeninde [AD], A açısının iç açıortayıdır ve D noktası [BC] üzerindedir. m(ABC) = 50° ve m(ACB) = 70° dir.\nŞekil ölçekli değildir.\nBuna göre, x = m(ADC) kaç derecedir?',
 dogru=80,yan=[(30,'Yarılanan açıyı (m(BAD) = 30°) bulup x sanmış.','dikkat'),(60,'A açısının tamamını (m(BAC) = 60°) x sanmış.','dikkat'),(100,'Komşu açıyı (m(ADB) = 180° − 80° = 100°) x sanmış.','dikkat'),(120,'B ve C açılarının toplamını (50° + 70°) x sanmış.','islem')],
 istenen='x = m(ADC) açısının ölçüsü (derece).',
 ip=['m(BAC) kaç derecedir ve açıortay bu açıyı kaça ayırır? ADC açısı hangi üçgenin dış açısıdır?'],
 bilgi=[ACI],
 ad=[A('A açısını bul','İç açıların toplamı 180° dir.','m(BAC) = 180° − 50° − 70° = 60°'),A('Açıortayla yarıla','[AD] açıortay olduğundan m(BAD) = m(DAC) dir.','m(BAD) = 30°'),A('Dış açıyı kullan','ADC açısı, ABD üçgeninin B ve BAD açılarına komşu olmayan dış açısıdır.','x = 50° + 30° = 80°')],
 puf='Önce üçgenin eksik iç açısını bul; sonra istenen açının hangi küçük üçgende yer aldığını belirle.',sekil=SK)

# ===== 03 · orta · dış açıortaylar
kartla('K-GAI-03','İki dış açıortayın kesişimi','Dış açıortaylar, iç açılardan bağımsız olarak BEC üçgeninin açılarını belirler.','Yarılanan dış açıyı iç açı sanmak; BEC yi A açısına eşitlemek.','orta',3,'ai-dis-aci','Dış açıortaylar ve açı')
B3=(0,0); C3=(4.4,0); A3=tri_ac(B3,C3,60,80)
Bx=add(B3,mul(un(sub(B3,A3)),1.3)); Cx=add(C3,mul(un(sub(C3,A3)),1.3))
db=add(un(sub(B3,A3)),un(sub(C3,B3))); dc=add(un(sub(C3,A3)),un(sub(B3,C3)))
E3=kesis(B3,add(B3,db),C3,add(C3,dc))
ok(ang(E3,B3,C3),70); ok(ang(B3,Bx,E3),ang(B3,E3,C3)); ok(ang(C3,Cx,E3),ang(C3,E3,B3)); assert E3[1]<0
f=F(); f.poly([A3,B3,C3]); f.line(B3,Bx); f.line(C3,Cx); f.line(B3,E3); f.line(C3,E3); ic=cen([A3,B3,C3])
arct(f,B3,Bx,E3,.55,1); arct(f,B3,E3,C3,.55,1); arct(f,C3,Cx,E3,.55,2); arct(f,C3,E3,B3,.55,2); f.arc(E3,B3,C3,.55,'$x$',.95)
for n_,p_ in (('A',A3),('B',B3),('C',C3)): vtx(f,p_,n_,ic)
f.vl('E',E3,(0,-1),.3)
SK=f.svg()
q('0003',tipId='ai-dis-aci',tip='Dış açıortaylar ve açı',z='orta',alt='İki Dış Açıortay',kaz='Üçgenin iki dış açıortayının kesişimindeki açıyı hesaplar.',
 kart='K-GAI-03 (iki dış açıortay, BEC açısı) · B = 60°, C = 80°',
 metin='Şekilde ABC üçgeninin [AB ve [AC kenarları B ve C köşelerinin ötesine uzatılmıştır. B köşesindeki dış açının açıortayı ile C köşesindeki dış açının açıortayı E noktasında kesişmektedir. m(ABC) = 60° ve m(ACB) = 80° dir.\nŞekil ölçekli değildir.\nBuna göre, x = m(BEC) kaç derecedir?',
 dogru=70,yan=[(20,'Sonucu A açısının yarısı sanmış: 40° ÷ 2 = 20°.','bilgi'),(40,'BEC açısını A açısına eşit sanmış: m(BAC) = 40°.','bilgi'),(50,'90° − m(BAC) işlemini yapmış: 90° − 40° = 50°.','islem'),(60,'m(ABC) = 60° değerini x sanmış.','dikkat')],
 istenen='x = m(BEC) açısının ölçüsü (derece).',
 ip=['B ve C köşelerindeki dış açılar kaç derecedir?'],
 bilgi=[ACI],
 ad=[A('Dış açıları bul','Dış açı, komşu olmayan iki iç açının toplamına eşittir.','B dış açısı = 40° + 80° = 120° · C dış açısı = 40° + 60° = 100°'),A('Açıortayla yarıla','Dış açıortaylar bu açıları ikiye böler; bu yarılar BEC üçgeninin B ve C köşesindeki açılarıdır.','m(EBC) = 60° · m(ECB) = 50°'),A('x i bul','BEC üçgeninin iç açıları toplamı 180° dir.','x = 180° − 60° − 50° = 70°')],
 puf='Dış açıların değerlerini önce kendin hesapla; açıortayların oluşturduğu yeni üçgenin iki açısı çıkar.',sekil=SK)

# ===== 04 · orta · cebirsel iç açıortay teoremi
kartla('K-GAI-04','Cebirsel kenar uzunlukları','Kenarlar x türünden verilince açıortay oranı denklem kurar; sonuçta istenen kenarlar x ile hesaplanır.','Oranı ters yazmak; x i bulup cevap sanmak.','orta',4,'ai-oran','İç açıortay teoremiyle uzunluk')
s=.34; A4,B4,C4=tri(10,12,8,s); D4=bis(A4,B4,C4)
ok(dist(B4,D4)/s,4); ok(dist(D4,C4)/s,6); ok(ang(A4,B4,D4),ang(A4,D4,C4))
f=F(); f.poly([A4,B4,C4]); f.line(A4,D4); ic=cen([A4,B4,C4]); arct(f,A4,B4,D4,.55,1); arct(f,A4,D4,C4,.55,1)
f.sl('$x+2$',A4,B4,ic,.38); f.sl('$2x$',A4,C4,ic,.35); dim(f,B4,D4,'$4$',(0,-1),.55); dim(f,D4,C4,'$6$',(0,-1),.55)
for n_,p_ in (('A',A4),('B',B4),('C',C4)): vtx(f,p_,n_,ic)
f.vl('D',D4,(1,.7),.3)
SK=f.svg()
q('0004',tipId='ai-oran',tip='İç açıortay teoremiyle uzunluk',z='orta',alt='Cebirsel Açıortay Oranı',kaz='Kenar uzunlukları cebirsel verilen üçgende iç açıortay teoremiyle denklem kurar.',
 kart='K-GAI-04 (cebirsel kenarlar, açıortay oranı) · x + 2, 2x, 4, 6',
 metin='Şekilde ABC üçgeninin [AD] doğru parçası A açısının iç açıortayıdır ve D noktası [BC] üzerindedir. Uzunluklar cm cinsindendir: |AB| = x + 2, |AC| = 2x, |BD| = 4 ve |DC| = 6 dır.\nŞekil ölçekli değildir.\nBuna göre, |AB| + |AC| toplamı kaç cm dir?',
 dogru=20,yan=[(5,'Oranı ters kurup x = 1 bulmuş: |AB| + |AC| = 3 + 2 = 5.','dikkat'),(6,'Bulunan x değerini cevap sanmış.','dikkat'),(8,'Yalnız |AB| = x + 2 = 8 uzunluğunu hesaplamış.','dikkat'),(12,'Yalnız |AC| = 2x = 12 uzunluğunu hesaplamış.','dikkat')],
 istenen='|AB| + |AC| toplamı (cm).',
 ip=['Açıortay, [BC] kenarını hangi oranda böldü? Bu oran hangi iki kenar uzunluğunun oranına eşittir?'],
 bilgi=[IC],
 ad=[A('Oranı yaz','İç açıortay teoremine göre parçaların oranı komşu kenarların oranına eşittir.','|BD| / |DC| = |AB| / |AC| → 4 / 6 = (x + 2) / (2x)'),A('x i çöz','İçler dışlar çarpımı yap.','8x = 6x + 12 → x = 6'),A('Kenarları bul','x i yerine yaz.','|AB| = 8 · |AC| = 12'),A('Toplamı al','İstenen toplamı hesapla.','8 + 12 = 20 cm')],
 puf='Bilinmeyeni olan oranı, sayıları olan oranla eşitle; çözdükten sonra soruda tam olarak ne istendiğine geri dön.',sekil=SK)

# ===== 05 · orta · iç + dış açıortay
kartla('K-GAI-05','İç ve dış açıortayın kesişimi','Bir iç ve bir dış açıortayın kesiştiği noktada oluşan açı, üçüncü köşedeki açıyla ilişkilidir.','Bu açıyı iç açıortay formülüyle (90° + A/2) ya da dış formülle (90° − A/2) bulmaya çalışmak.','orta',4,'ai-aci','Açıortay ve açı hesabı')
B5=(0,0); C5=(6.0,0); A5=tri_ac(B5,C5,50,56)
dB=(cos(radians(25)),sin(radians(25))); dC=(cos(radians(62)),sin(radians(62)))
F5=kesis(B5,add(B5,dB),C5,add(C5,dC)); G5=add(C5,(1.3,0))
ok(ang(F5,B5,C5),37); ok(ang(C5,G5,F5),ang(C5,F5,A5)); ok(ang(B5,A5,F5),ang(B5,F5,C5))
ok(ang(C5,B5,F5),118); assert F5[0]>C5[0] and F5[1]>0
f=F(); f.poly([A5,B5,C5]); f.line(C5,G5); f.line(B5,F5); f.line(C5,F5); ic=cen([A5,B5,C5])
arct(f,B5,C5,F5,.7,1); arct(f,B5,F5,A5,.7,1); arct(f,C5,G5,F5,.55,2); arct(f,C5,F5,A5,.55,2); f.arc(F5,B5,C5,.7,'$x$',1.15)
for n_,p_ in (('A',A5),('B',B5),('C',C5)): vtx(f,p_,n_,ic)
f.vl('F',F5,(1,.5),.3)
SK=f.svg()
q('0005',tipId='ai-aci',tip='Açıortay ve açı hesabı',z='orta',alt='İç ve Dış Açıortay',kaz='Bir iç ve bir dış açıortayın kesişimindeki açıyı üçüncü köşedeki açıdan hesaplar.',
 kart='K-GAI-05 (iç ve dış açıortay, BFC açısı) · B = 50°, C = 56°',
 metin='Şekilde ABC üçgeninin B köşesindeki iç açıortay ile C köşesindeki dış açının açıortayı F noktasında kesişmektedir. [BC nin uzantısı C den sonra çizilmiştir. m(ABC) = 50° ve m(ACB) = 56° dır.\nŞekil ölçekli değildir.\nBuna göre, x = m(BFC) kaç derecedir?',
 dogru=37,yan=[(25,'Yalnız B açısının yarısını (m(FBC) = 25°) bulup x sanmış.','dikkat'),(53,'90° − m(BAC) ÷ 2 işlemini yapmış: 90° − 37° = 53°.','bilgi'),(74,'m(BAC) = 74° değerini x sanmış.','dikkat'),(127,'90° + m(BAC) ÷ 2 işlemini yapmış: 90° + 37° = 127°.','bilgi')],
 istenen='x = m(BFC) açısının ölçüsü (derece).',
 ip=['A açısı kaç derecedir? C köşesindeki dış açı kaç derecedir ve BFC üçgeninin B ve C köşesindeki açıları ne olur?'],
 bilgi=[ACI],
 ad=[A('A yı bul','İç açıların toplamı 180° dir.','m(BAC) = 180° − 50° − 56° = 74°'),A('B de yarıla','[BF iç açıortay olduğundan m(FBC) = 25° dir.','m(FBC) = 50° ÷ 2 = 25°'),A('C de dış açıyı yarıla','C köşesindeki dış açı, A ve B açılarının toplamıdır; [CF onu iki eş açıya ayırır. BFC üçgeninde C köşesindeki açı, dış açının yarısının bütünleyenidir.','dış açı = 74° + 50° = 124° → yarısı 62° → m(BCF) = 180° − 62° = 118°'),A('x i bul','BFC üçgeninin iç açıları toplamı 180° dir.','x = 180° − 25° − 118° = 37°')],
 puf='Açıortay ve dış açı birlikte geçiyorsa her köşedeki açıyı tek tek yaz; BFC üçgeninin iki açısını bulunca üçüncüsü hazırdır.',sekil=SK)

# ===== 06 · orta · açıortay ve paralel
kartla('K-GAI-06','Açıortay ve paralel: ikizkenar üçgen','Açıortay ile paralel birleşince ikizkenar üçgen çıkar; benzerlikle uzunluk bulunur.','DE yi AB ya da CE ye eşitlemek; benzerlik oranını ters kurmak.','orta',4,'ai-paralel','Açıortay ve paralel doğru')
s=.25; A6,B6,C6=tri(20,10,15,s); D6=bis(A6,B6,C6); E6=lerp(C6,A6,.4)
ok(dist(B6,D6)/s,12); ok(dist(D6,C6)/s,8); ok(dist(D6,E6)/s,6); ok(dist(A6,E6)/s,6); ok(dist(C6,E6)/s,4)
assert abs((E6[0]-D6[0])*(B6[1]-A6[1])-(E6[1]-D6[1])*(B6[0]-A6[0]))<1e-9
f=F(); f.poly([A6,B6,C6]); f.line(A6,D6); f.line(D6,E6); f.par(D6,E6); f.par(B6,A6); ic=cen([A6,B6,C6]); arct(f,A6,B6,D6,.5,1); arct(f,A6,D6,C6,.5,1)
f.sl('$15$',A6,B6,ic,.3)
dim(f,A6,C6,'$10$',(1,1),.5)
for n_,p_ in (('A',A6),('B',B6),('C',C6)): vtx(f,p_,n_,ic)
f.vl('D',D6,(0,-1),.3); f.vl('E',E6,(1,.4),.3)
SK=f.svg()
q('0006',tipId='ai-paralel',tip='Açıortay ve paralel doğru',z='orta',alt='Açıortay ve Paralel',kaz='İç açıortay ve kenara paralel doğrudan oluşan ikizkenar ve benzer üçgenlerle uzunluk bulur.',
 kart='K-GAI-06 (açıortay + paralel, DE uzunluğu) · AB = 15, AC = 10',
 metin='Şekilde ABC üçgeninin [AD] doğru parçası A açısının iç açıortayıdır; D ∈ [BC] ve E ∈ [AC] dir. [DE] // [AB], |AB| = 15 cm ve |AC| = 10 cm dir.\nŞekil ölçekli değildir.\nBuna göre, |DE| kaç cm dir?',
 dogru=6,yan=[(4,'|DE| yerine |EC| = 4 uzunluğunu bulmuş.','dikkat'),(7.5,'D yi [BC] nin orta noktası sanıp |DE| = |AB| ÷ 2 yazmış.','bilgi'),(9,'Benzerlik oranını ters kurmuş: |DE| = 15 × |BD| ÷ |BC| = 15 × 3 ÷ 5 = 9.','dikkat'),(10,'|DE| yi |AC| ye eşit almış.','bilgi')],
 istenen='|DE| uzunluğu (cm).',
 ip=['[DE] // [AB] olduğundan hangi açı eşitlikleri çıkar?'],
 bilgi=[IC],
 ad=[A('İkizkenarı bul','[DE] // [AB] olduğundan m(BAD) = m(ADE) (iç ters açı); [AD] açıortay olduğundan m(BAD) = m(DAE). ADE nin iki açısı eşittir.','|AE| = |DE| = y'),A('Benzerliği yaz','[DE] // [AB] olduğundan CDE ve CBA üçgenleri benzerdir.','|CE| / |CA| = |DE| / |AB|'),A('Değerleri yerleştir','|CE| = 10 − y, |CA| = 10, |AB| = 15.','(10 − y) / 10 = y / 15'),A('y yi çöz','İçler dışlar çarpımı.','150 − 15y = 10y → y = 6 cm')],
 puf='Paralellik gördüğün yerde eşit açıları yaz; eşit açılar çoğu zaman eşit kenarlara dönüşür.',sekil=SK)

# ===== 07 · orta · açıortay, uzaklık ve alan
kartla('K-GAI-07','Açıortay noktasından kollara uzaklık ve alan','Açıortay ayağının iki kenara uzaklığı eşittir; üçgen iki üçgenin alanlarının toplamıdır.','Yalnız bir kenarı taban almak; iki alanı toplarken ½ çarpanını atlamak.','orta',4,'ai-alan','Açıortay ve alan')
s=.4; A7=(0,0); B7=(10*s,0); cA=sqrt(1-.9**2); C7=(8*s*cA,8*s*.9); D7=bis(A7,B7,C7); E7=foot(D7,A7,B7); F7=foot(D7,A7,C7)
ok(alan([A7,B7,C7])/s**2,36); ok(dist(D7,E7),dist(D7,F7)); ok(dist(D7,E7)/s,4); ok(ang(E7,D7,A7),90); ok(ang(F7,D7,A7),90)
f=F(); f.poly([A7,B7,C7]); f.line(A7,D7); f.line(D7,E7); f.line(D7,F7); f.dik(E7,D7,A7); f.dik(F7,D7,A7); ic=cen([A7,B7,C7]); arct(f,A7,B7,D7,.55,1); arct(f,A7,D7,C7,.55,1)
dim(f,A7,B7,'$10$',(0,-1),.55); dim(f,A7,C7,'$8$',(-1,.3),.5); f.node(add(mid(D7,E7),(.28,0)),'$x$')
f.node(((B7[0]+A7[0])/2,-1.6),'Alan$(ABC)=36\\ \\mathrm{cm}^2$')
for n_,p_ in (('A',A7),('B',B7),('C',C7)): vtx(f,p_,n_,ic)
f.vl('D',D7,(1,.4),.3); f.vl('E',E7,(0,-1),.3); f.vl('F',F7,(-1,.2),.3)
SK=f.svg()
q('0007',tipId='ai-alan',tip='Açıortay ve alan',z='orta',alt='Açıortay, Uzaklık ve Alan',kaz='Açıortay ayağından kenarlara inen dikmelerin eşitliğiyle alan bağıntısından uzunluk bulur.',
 kart='K-GAI-07 (açıortay ayağından dikmeler, alan) · AB = 10, AC = 8',
 metin='Şekilde alanı 36 cm² olan ABC üçgeninde [AD] doğru parçası A açısının iç açıortayıdır ve D ∈ [BC] dir. D noktasından [AB] ye indirilen dikmenin ayağı E, [AC] ye indirilen dikmenin ayağı F dir. |AB| = 10 cm, |AC| = 8 cm ve |DE| = x tir.\nŞekil ölçekli değildir.\nBuna göre, x kaç cm dir?',
 dogru=4,yan=[(2,'Alan bağıntısında ½ çarpanını unutmuş: 36 ÷ 18 = 2.','islem'),(3.6,'Yalnız [AB] tabanını kullanmış: 36 ÷ 10 = 3,6.','bilgi'),(4.5,'Yalnız [AC] tabanını kullanmış: 36 ÷ 8 = 4,5.','bilgi'),(9,'İki kenarın ortalamasını (10 + 8) ÷ 2 = 9 alıp x sanmış.','bilgi')],
 istenen='x = |DE| uzunluğu (cm).',
 ip=['D noktasının iki kola uzaklıkları hakkında ne söylenir?'],
 bilgi=[UZ,TABAN],
 ad=[A('Dikmeleri eşitle','D açıortay üzerinde olduğundan kollara uzaklıkları eşittir.','|DF| = |DE| = x'),A('Alanı iki parçaya ayır','ABC, ABD ve ADC üçgenlerinin birleşimidir; tabanları [AB] ve [AC], yükseklikleri x tir.','Alan(ABD) = ½ × 10 × x · Alan(ADC) = ½ × 8 × x'),A('Toplamı kur','İki alanın toplamı 36 cm² dir.','5x + 4x = 36'),A('x i bul','Denklemi çöz.','9x = 36 → x = 4 cm')],
 puf='Verilen alan bilgisini kullanmanın birden fazla yolu olabilir; hangi uzunluklar şekilde bilinmiyor?',sekil=SK)

# ===== 08 · zor · iç ve dış açıortay birlikte
kartla('K-GAI-08','İç ve dış açıortayın ayakları arası uzaklık','İç açıortay D yi, dış açıortay E yi verir; E nin yeri dış açıortay oranıyla bulunur ve D ye olan uzaklık toplanır.','E yi [BC] arasında aramak; E nin hangi taraftan uzantıda olduğunu yanlış belirlemek.','zor',5,'ai-dis-oran','İç ve dış açıortay birlikte')
s=.34; A8,B8,C8=tri(9,12,6,s); D8=bis(A8,B8,C8)
u=un(sub(D8,A8)); per=(-u[1],u[0]); E8=kesis(A8,add(A8,per),B8,C8)
ok(dist(B8,D8)/s,3); ok(dist(D8,C8)/s,6); ok(dist(E8,B8)/s,9); ok(dist(E8,C8)/s,18); ok(dist(D8,E8)/s,12); assert dist(E8,C8)>dist(B8,C8) and dist(E8,B8)<dist(E8,C8)
ok(ang(A8,D8,E8),90)  # iç ve dış açıortaylar dik
f=F(); f.poly([A8,B8,C8]); f.line(A8,D8); ic=cen([A8,B8,C8]); arct(f,A8,B8,D8,.55,1); arct(f,A8,D8,C8,.55,1)
dim(f,B8,D8,'$3$',(0,-1),.55); dim(f,D8,C8,'$6$',(0,-1),.55)
for n_,p_ in (('A',A8),('B',B8),('C',C8)): vtx(f,p_,n_,ic)
f.vl('D',D8,(1,.7),.3)
SK=f.svg()
q('0008',tipId='ai-dis-oran',tip='İç ve dış açıortay birlikte',z='zor',alt='İç ve Dış Açıortay Uzunluğu',kaz='Aynı köşeden çizilen iç ve dış açıortayların karşı kenar doğrusunu kestiği noktalar arasındaki uzaklığı bulur.',
 kart='K-GAI-08 (iç ve dış açıortay, DE uzunluğu) · BD = 3, DC = 6',
 metin='Şekilde ABC üçgeninin [AD] doğru parçası A açısının iç açıortayıdır; D ∈ [BC], |BD| = 3 cm ve |DC| = 6 cm dir. A köşesindeki dış açıortay, BC doğrusunu E noktasında kesmektedir. E noktası şekilde gösterilmemiştir.\nŞekil ölçekli değildir.\nBuna göre, |DE| kaç cm dir?',
 dogru=12,yan=[(3,'|BD| = 3 uzunluğunu |DE| sanmış.','dikkat'),(6,'|DC| = 6 uzunluğunu |DE| sanmış.','dikkat'),(9,'Yalnız |BE| = 9 uzantısını bulup |DE| ye |BD| yi eklememiş.','dikkat'),(18,'|DE| yerine |CE| = 18 uzunluğunu bulmuş.','dikkat')],
 istenen='|DE| uzunluğu (cm).',
 ip=['İç açıortay teoremi |AB| : |AC| oranını verir. Aynı oran E noktasının B ve C ye uzaklıkları için ne söyler? E, B nin mi C nin mi tarafındadır?'],
 bilgi=[IC,DISB],
 ad=[A('Kenar oranını bul','İç açıortay teoremi: |AB| / |AC| = |BD| / |DC|.','|AB| / |AC| = 3 / 6 = 1 / 2'),A('E nin yerini belirle','|AB| < |AC| olduğundan E, [BC] nin B tarafındaki uzantısındadır; |EB| < |EC| dir.','E — B — D — C sıralaması'),A('Dış açıortay oranını yaz','Dış açıortay teoremi: |EB| / |EC| = |AB| / |AC|; |EC| = |EB| + |BC| = |EB| + 9.','|EB| / (|EB| + 9) = 1 / 2'),A('|EB| yi çöz','İçler dışlar çarpımı.','2|EB| = |EB| + 9 → |EB| = 9 cm'),A('|DE| yi topla','E, B, D noktaları aynı doğru üzerinde ve B, E ile D arasında.','|DE| = |EB| + |BD| = 9 + 3 = 12 cm')],
 puf='Çizilmeyen noktayı sen yerleştir: doğru üzerindeki sıralamayı belirlemeden uzunlukları toplama.',sekil=SK)

# ===== 09 · zor · açıortay + kenarortay + alan
kartla('K-GAI-09','Açıortay ve kenarortay ayakları arasındaki alan','İki ayak arasındaki parça, kenarın bir kesri olarak bulunur; alan aynı yükseklikle oranlanır.','D nin yerini ters oranla belirlemek; ADM yerine ABD ya da ABM nin alanını vermek.','zor',5,'ai-alan','Açıortay ve alan')
a9=sqrt(145); s=.5; A9,B9,C9=tri(a9,15,10,s); D9=bis(A9,B9,C9); M9=mid(B9,C9)
ok(alan([A9,B9,C9])/s**2,60); ok(ang(A9,B9,D9),ang(A9,D9,C9)); ok(dist(B9,D9)/dist(B9,C9),.4); ok(alan([A9,D9,M9])/s**2,6)
assert dist(B9,D9)<dist(B9,M9)
f=F(); f.fill([A9,D9,M9]); f.poly([A9,B9,C9]); f.line(A9,D9); f.line(A9,M9); f.tick(B9,M9); f.tick(M9,C9); ic=cen([A9,B9,C9]); arct(f,A9,B9,D9,.9,1); arct(f,A9,D9,C9,.9,1);
f.sl('$10$',A9,B9,ic,.3); f.sl('$15$',A9,C9,ic,.3); f.node((mid(B9,C9)[0],-1.25),'Alan$(ABC)=60\\ \\mathrm{cm}^2$')
for n_,p_ in (('A',A9),('B',B9),('C',C9)): vtx(f,p_,n_,ic)
f.vl('D',D9,(-.7,-1),.3); f.vl('M',M9,(.7,-1),.3)
SK=f.svg()
q('0009',tipId='ai-alan',tip='Açıortay ve alan',z='zor',alt='Açıortay, Kenarortay ve Alan',kaz='Aynı köşeden çizilen açıortay ve kenarortayın karşı kenarda ayırdığı parçanın oluşturduğu üçgenin alanını bulur.',
 kart='K-GAI-09 (açıortay + kenarortay, ADM alanı) · AB = 10, AC = 15, alan = 60',
 metin='Şekilde alanı 60 cm² olan ABC üçgeninin [AD] doğru parçası A açısının iç açıortayı, [AM] doğru parçası kenarortayıdır; D ve M noktaları [BC] üzerindedir. |AB| = 10 cm ve |AC| = 15 cm dir. Şekilde [AD] nin A açısını eş iki açıya ayırdığı, M nin ise [BC] nin orta noktası olduğu işaretlenmiştir.\nŞekil ölçekli değildir.\nBuna göre, taralı ADM üçgeninin alanı kaç cm² dir?',
 dogru=6,yan=[(12,'|DM| yi |BC| nin 1/5 i alıp 60 ÷ 5 = 12 bulmuş.','islem'),(24,'ABD üçgeninin alanını (60 × 2 ÷ 5 = 24) cevap sanmış.','dikkat'),(30,'ABM üçgeninin alanını (60 ÷ 2 = 30) cevap sanmış.','dikkat'),(36,'ADC üçgeninin alanını (60 × 3 ÷ 5 = 36) cevap sanmış.','dikkat')],
 istenen='Taralı ADM üçgeninin alanı (cm²).',
 ip=['[AD] açıortay olduğuna göre D, [BC] yi hangi oranda böler? M nin yeri bu bölünmeye göre nerededir?'],
 bilgi=[IC,KORB,TABAN],
 ad=[A('D nin yerini bul','İç açıortay teoremi: |BD| : |DC| = |AB| : |AC|.','|BD| : |DC| = 10 : 15 = 2 : 3 → |BD| = 2/5 · |BC|'),A('M nin yerini bul','M, [BC] nin orta noktasıdır.','|BM| = 1/2 · |BC|'),A('|DM| yi bul','D ile M arasındaki parça farktır.','|DM| = 1/2 · |BC| − 2/5 · |BC| = 1/10 · |BC|'),A('Alanı bul','ADM ile ABC üçgenlerinin A dan [BC] ye inen yüksekliği ortaktır; alanlar tabanlarıyla orantılıdır.','Alan(ADM) = 60 ÷ 10 = 6 cm²')],
 puf='Uzunluğu bilinmeyen iki noktayı kenarın bir kesri olarak ifade et; alanı bulmak için bu kesri kullan.',sekil=SK)

# ===== 10 · zor · paralelkenarda iki açıortay
kartla('K-GAI-10','Paralelkenarda komşu açıortaylar','Her açıortay karşı kenardan bir ikizkenar üçgen keser; iki ikizkenarın dayandığı parçalar üst üste binerse fark farklı hesaplanır.','Fazlalığı (üst üste binmeyi) görmeyip kenar farkını almak.','orta',4,'ai-paralelkenar','Paralelkenarda açıortay')
s=.33; A10=(0,0); B10=(11*s,0); D10=(7*s*cos(radians(60)),7*s*sin(radians(60))); C10=add(B10,D10)
E10=kesis(A10,(cos(radians(30)),sin(radians(30))),D10,C10); F10=kesis(B10,add(B10,(cos(radians(120)),sin(radians(120)))),D10,C10)
ok(dist(D10,E10)/s,7); ok(dist(C10,F10)/s,7); ok(dist(E10,F10)/s,3); assert E10[0]>F10[0]
ok(ang(A10,B10,E10),ang(A10,E10,D10)); ok(ang(B10,A10,F10),ang(B10,F10,C10))
f=F(); f.poly([A10,B10,C10,D10]); f.line(A10,E10); f.line(B10,F10); f.par(A10,B10); f.par(D10,C10); ic=cen([A10,B10,C10,D10]); arct(f,A10,B10,E10,.6,1); arct(f,A10,E10,D10,.6,1); arct(f,B10,A10,F10,.6,2); arct(f,B10,F10,C10,.6,2)
dim(f,A10,B10,'$11$',(0,-1),.55); f.sl('$7$',A10,D10,ic,.3)
f.vl('A',A10,(-1,-.6),.3); f.vl('B',B10,(1,-.6),.3); f.vl('C',C10,(1,.6),.3); f.vl('D',D10,(-1,.6),.3); f.vl('E',E10,(.4,1),.3); f.vl('F',F10,(-.4,1),.3)
SK=f.svg()
q('0010',tipId='ai-paralelkenar',tip='Paralelkenarda açıortay',z='orta',alt='Paralelkenarda Açıortay',kaz='Paralelkenarda iki komşu açının açıortaylarının karşı kenarda ayırdığı parçanın uzunluğunu bulur.',
 kart='K-GAI-10 (paralelkenar, iki açıortay) · AB = 11, AD = 7',
 metin='Şekildeki ABCD paralelkenarında |AB| = 11 cm ve |AD| = 7 cm dir. A ve B köşelerinden çizilen iç açıortaylar [DC] kenarını sırasıyla E ve F noktalarında kesmektedir.\nŞekil ölçekli değildir.\nBuna göre, |EF| kaç cm dir?',
 dogru=3,yan=[(4,'|EF| yi kenar farkı |AB| − |AD| = 4 sanmış.','bilgi'),(7,'|DE| = 7 uzunluğunu |EF| sanmış.','dikkat'),(14,'|DE| + |CF| = 7 + 7 = 14 toplamını bulup bırakmış.','dikkat'),(18,'|AB| + |AD| = 18 toplamını cevap sanmış.','bilgi')],
 istenen='|EF| uzunluğu (cm).',
 ip=['[AB] // [DC] olduğuna göre m(DEA) hangi açıya eşittir?'],
 bilgi=[PKENAR,PARB],
 ad=[A('ADE yi incele','[AB] // [DC] olduğundan m(DEA) = m(EAB) (iç ters açı); [AE] açıortay olduğundan m(EAB) = m(DAE). ADE nin iki açısı eşit.','|DE| = |AD| = 7'),A('BCF yi incele','Aynı biçimde [BF] açıortay ve [AB] // [DC] olduğundan BCF ikizkenar.','|CF| = |BC| = 7'),A('Yerleri belirle','[DC] = 11 dir. D den 7 ileride E, C den 7 geride F vardır; 7 + 7 > 11 olduğundan E ve F aynı sırada değil, birbirini geçer.','|DF| = 11 − 7 = 4 · |DE| = 7'),A('Farkı al','E ve F, D den sırasıyla 7 ve 4 uzaklıktadır.','|EF| = 7 − 4 = 3 cm')],
 puf='Açıortayların ayırdığı parçaları tek tek hesapla ve doğru üzerindeki yerlerini D noktasından ölçerek karşılaştır.',sekil=SK)
bitir_geo(ONEK,KONU_AD)
