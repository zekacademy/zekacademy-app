"""TYT Geometri · Üçgende Benzerlik (ikinci paket, hafif mod). Şekil koordinatları hesaplanır, TikZ aynı değerlerden üretilir; her cevap ve çeldirici assert edilir."""
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
P=Parti('benzerlikiki','Üçgende Benzerlik','geo|Üçgende Benzerlik',ders='TYT Geometri',idon='tytgeo')
BENZ=B('Benzer üçgenler','karşılıklı açıları eşit olan üçgenler benzerdir; benzer üçgenlerde karşılıklı kenarların oranı sabittir. Örnek: KLM ∼ PRS ise |KL| / |PR| = |LM| / |RS| = |KM| / |PS| dir')
ORAN=B('Benzerlik oranı ve çevre','benzer iki üçgenin çevreleri oranı, karşılıklı kenarlarının oranına eşittir. Örnek: kenar oranı 2 : 7 olan iki üçgenden küçüğünün çevresi 14 cm ise büyüğünün çevresi 49 cm’dir')
PAR=B('Paralel doğrular ve açılar','iki paralel doğruyu bir doğru kesince oluşan yöndeş açılar ve ters açılar eşittir. Örnek: d₁ // d₂ ve kesen doğru d₁ ile 70° yapıyorsa d₂ ile de aynı yönde 70° yapar')
THA=B('Thales teoremi','paralel doğrular, kendilerini kesen doğruları orantılı parçalara ayırır. Örnek: üç paralel doğru bir kesenden 2 cm ve 6 cm, diğer kesenden 5 cm ve x cm uzunluğunda parçalar ayırıyorsa 2 / 6 = 5 / x tir')
ALAN=B('Paralelkenar','karşılıklı kenarları paralel olan dörtgendir; karşılıklı kenarlarının uzunlukları eşittir. Örnek: bir paralelkenarın bir kenarı 7 cm ise karşısındaki kenarı da 7 cm’dir')
YAMUK=B('Yamuk','en az bir çift kenarı paralel olan dörtgendir; paralel kenarlara taban, diğer kenarlara yan kenar denir. Örnek: [KL] // [NM] ise KLMN bir yamuktur ve [KN], [LM] yan kenarlardır')
KENAR=B('Kenarortay','bir köşeyi karşı kenarın orta noktasına birleştiren doğru parçasıdır; orta nokta karşı kenarı iki eşit parçaya böler. Örnek: [KN], KLM üçgeninde L’ye karşı kenarın orta noktası N ise |LN| = |NM| dir')
PIS=B('Pisagor bağıntısı','dik üçgende dik kenarların kareleri toplamı hipotenüsün karesine eşittir. Örnek: dik kenarları 5 ve 12 olan üçgende hipotenüs √(25 + 144) = 13’tür')
KAT=B('Katlamada eşlik','kâğıt katlandığında üst üste gelen parçaların uzunlukları ve açıları eşit kalır; katlama çizgisi bir simetri eksenidir. Örnek: bir köşe katlanarak başka bir noktaya geliyorsa o köşeden katlama çizgisi üzerindeki herhangi bir noktaya olan uzaklık korunur')
CAPRAZ=B('Dik açı ve tümler açılar','bir doğru üzerinde yan yana duran dik açıdan geriye kalan açılar tümlerdir; toplamları 90° dir. Örnek: bir doğru üzerinde 90° ve 35° lik iki açı varsa kalan açı 55° dir')

def vlabs(f,pts,ic):
    for n_,p_ in pts: vtx(f,p_,n_,ic)
konu('geo|Üçgende Benzerlik','Üçgende Benzerlik')
def kartlab(no,alt,fikir,tuzak,z,adim,tipId,tip):
    kartla(f'K-GBI-{no:02d}',alt,fikir,tuzak,z,adim,tipId,tip)

# ===== 01 · gölge · kolay · hikâyeli =====
kartlab(1,'Gölge ve boy','Güneş ışınları paralel olduğundan aynı anda yere dik duran cisimler ve gölgeleri aynı biçimli dik üçgenler oluşturur; bilinmeyen boy gölge oranından bulunur.','Boy ile gölgeyi karıştırmak; oranı ters kurmak; farkla orantı kurmak.','kolay',3,'ge-bzi-golge','Gölge problemlerinde benzerlik')
H1,G1,g1=12,15,2; x1=H1*g1/G1; assert abs(x1-1.6)<1e-12
sc=.3; TB=(0,0); TT=(0,H1*sc); TS=(G1*sc,0); cx=6.0; CT=(cx,x1*sc); CS=(cx+g1*sc,0)
assert abs((TT[1]/(TS[0]-TT[0]))-(CT[1]/(CS[0]-CT[0])))<1e-12   # ışınlar paralel
f=F(); f.line((-1.4,0),(7.6,0)); f.line(TB,TT,'line width=2pt'); f.line(CB:=(cx,0),CT,'line width=2pt')
f.raw(f'\\fill {pt(CT)} circle (0.07);')
f.line(TT,TS,'dashed'); f.line(CT,CS,'dashed'); f.dik(TB,TT,TS,.16)
dim(f,TB,TT,'$12$ m',(-1,0),.5); dim(f,TB,TS,'$15$ m',(0,-1),.45); dim(f,CB,CS,'$2$ m',(0,-1),.45)
f.node((cx-.35,x1*sc/2+.05),'$x$')
SK=f.svg()
assert sorted([1.6,2,2.5,10,13])==sorted([x1,g1,g1*G1/H1,H1-g1,G1-g1])
q('0001',tipId='ge-bzi-golge',tip='Gölge problemlerinde benzerlik',z='kolay',kalip='hikâyeli',alt='Ağaç ve Gölge',kaz='Gölge ve boy oranlarının eşitliğinden bilinmeyen boyu bulur.',
 kart='K-GBI-01 (gölge ve boy)',
 metin='Güneşli bir günde yere dik duran 12 m boyundaki bir ağacın gölgesinin uzunluğu 15 m ölçülmüştür. Aynı anda, ağacın yakınında yere dik duran Ece’nin gölgesi 2 m uzunluğundadır. Gölgeler aynı doğrultudadır ve güneş ışınları birbirine paraleldir. Şekil ölçekli değildir.\nBuna göre, Ece’nin boyu olan x kaç metredir?',
 dogru=1.6,yan=[(2,'Gölgenin uzunluğunu (2 m) boy sanmış.','dikkat'),(2.5,'Oranı ters kurmuş: 2 × 15 ÷ 12 = 2,5.','dikkat'),(10,'Farkla orantı kurmuş: 12 − 2 = 10.','islem'),(13,'Ağacın gölgesinden Ece’nin gölgesini çıkarmış: 15 − 2 = 13.','islem')],
 istenen='Ece’nin boyu x (m).',
 ip=['Ağaç, gölgesi ve güneş ışınının yaptığı üçgen ile Ece, gölgesi ve ışının yaptığı üçgenin açıları hakkında ne söyleyebilirsin?'],
 bilgi=[BENZ],
 ad=[A('Benzer üçgenleri belirle','Her iki cisim de yere diktir; ışınlar paralel olduğundan ağaç ve Ece’nin oluşturduğu dik üçgenlerin açıları eşittir.','Ağaç üçgeni ∼ Ece üçgeni'),A('Oranı kur','Karşılıklı kenarların oranı sabittir: boy / gölge.','12 / 15 = x / 2'),A('x’i bul','İçler dışlar çarpımı.','x = 12 × 2 ÷ 15 = 1,6')],
 puf='Bulduğun değerin gerçek hayatta makul bir boy olup olmadığını kontrol et.',sekil=SK)

# ===== 02 · çevre oranı · kolay =====
kartlab(2,'Çevre oranı','Kenara paralel çizilen doğru küçük bir üçgen ayırır; çevreler arasındaki ilişki uzunluk oranıyla kurulur.','Parça/parça oranı ile benzerlik oranını karıştırmak; çevreden kenar çıkarmak.','kolay',3,'ge-bzi-oran','Benzerlik oranı ve çevre')
AD,DB,CV=6,4,35; AB=AD+DB; cv2=CV*AD/AB; assert cv2==21
A_,B_,C_=(1.9,3.7),(0,0),(5.4,0); D_=lerp(A_,B_,AD/AB); E_=lerp(A_,C_,AD/AB); assert abs(D_[1]-E_[1])<1e-9
assert abs((dist(A_,D_)+dist(D_,E_)+dist(A_,E_))/(dist(A_,B_)+dist(B_,C_)+dist(A_,C_))-.6)<1e-9
f=F(); ic=cen([A_,B_,C_]); f.poly([A_,B_,C_]); f.line(D_,E_); f.par(D_,E_); f.par(B_,C_)
f.sl('$6$',A_,D_,ic,.28); f.sl('$4$',D_,B_,ic,.28); vlabs(f,[('A',A_),('B',B_),('C',C_)],ic); f.vl('D',D_,(-1,.2),.3); f.vl('E',E_,(1,.2),.3)
f.node((2.7,-.75),'Çevre$(ABC)=35$ cm')
SK=f.svg()
assert sorted([14,21,25,29,52.5])==sorted([CV*DB/AB,cv2,CV-AB,CV-AD,CV*AD/DB])
q('0002',tipId='ge-bzi-oran',tip='Benzerlik oranı ve çevre',z='kolay',alt='Çevre Oranı',kaz='Benzerlik oranını kullanarak benzer üçgenlerin çevreleri arasındaki ilişkiyi kurar.',
 kart='K-GBI-02 (çevre oranı)',
 metin='ABC üçgeninde D noktası [AB] üzerinde, E noktası [AC] üzerindedir ve [DE] // [BC] dir. Şekilde |AD| = 6 cm, |DB| = 4 cm ve ABC üçgeninin çevresi 35 cm olarak verilmiştir. Şekil ölçekli değildir.\nBuna göre, ADE üçgeninin çevresi kaç cm’dir?',
 dogru=21,yan=[(14,'Benzerlik oranını |DB| / |AB| = 4 / 10 almış: 35 × 4 ÷ 10 = 14.','dikkat'),(25,'Büyük çevreden |AB| uzunluğunu çıkarmış: 35 − 10 = 25.','islem'),(29,'Büyük çevreden |AD| yi çıkarmış: 35 − 6 = 29.','islem'),(52.5,'Parça / parça oranını (6 / 4) benzerlik oranı sanmış: 35 × 6 ÷ 4 = 52,5.','bilgi')],
 istenen='ADE üçgeninin çevresi (cm).',
 ip=['[DE] // [BC] olduğunda hangi iki üçgenin açıları eşit olur? Benzerlik oranını hangi iki kenarın oranı olarak yazabilirsin?'],
 bilgi=[BENZ,ORAN,PAR],
 ad=[A('Benzer üçgenleri yaz','[DE] // [BC] olduğundan yöndeş açılar eşittir ve A açısı ortaktır.','ADE ∼ ABC'),A('Benzerlik oranını bul','Küçük üçgenin kenarının büyük üçgenin karşılıklı kenarına oranı.','k = |AD| / |AB| = 6 / (6 + 4) = 3 / 5'),A('Çevreyi hesapla','Çevreler de aynı oranla orantılıdır.','Çevre(ADE) = 35 × 3 ÷ 5 = 21')],
 puf='Verilen her uzunluğun hangi üçgene ait olduğunu belirleyip oranı yazmadan önce karşılıklı kenarları eşleştir.',sekil=SK)

# ===== 03 · iki paralel doğru parçası · orta =====
kartlab(3,'İki paralel doğru parçası','Tabana paralel iki doğru parçası farklı oranlarda benzer üçgenler ayırır; her biri ayrı oranla hesaplanıp toplanır.','Parçaları toplamla karıştırmak; yalnız bir parçayı bulup bırakmak; tabanı toplama katmak.','orta',4,'ge-bzi-oran','Benzerlik oranı ve çevre')
AD3,DF3,FB3,BC3=2,3,5,20; AB3=AD3+DF3+FB3; DE3=BC3*AD3/AB3; FG3=BC3*(AD3+DF3)/AB3; assert (DE3,FG3)==(4,10)
A3,B3,C3=(1.5,4.2),(0,0),(5,0); D3=lerp(A3,B3,AD3/AB3); F3=lerp(A3,B3,(AD3+DF3)/AB3); E3=lerp(A3,C3,AD3/AB3); G3=lerp(A3,C3,(AD3+DF3)/AB3)
assert abs(D3[1]-E3[1])<1e-9 and abs(F3[1]-G3[1])<1e-9 and abs(dist(D3,E3)/5*20-4)<1e-9 and abs(dist(F3,G3)/5*20-10)<1e-9
f=F(); ic=cen([A3,B3,C3]); f.poly([A3,B3,C3]); f.line(D3,E3); f.line(F3,G3); f.par(D3,E3); f.par(F3,G3); f.par(B3,C3)
f.sl('$2$',A3,D3,ic,.28); f.sl('$3$',D3,F3,ic,.28); f.sl('$5$',F3,B3,ic,.28); f.sl('$20$',B3,C3,A3,.35)
vlabs(f,[('A',A3),('B',B3),('C',C3)],ic); f.vl('D',D3,(-1,.2),.3); f.vl('E',E3,(1,.2),.3); f.vl('F',F3,(-1,.2),.3); f.vl('G',G3,(1,.2),.3)
SK=f.svg()
assert sorted([4,10,14,24,34])==sorted([DE3,FG3,DE3+FG3,DE3+BC3,DE3+FG3+BC3])
q('0003',tipId='ge-bzi-oran',tip='Benzerlik oranı ve çevre',z='orta',alt='İki Paralel Doğru',kaz='Tabana paralel iki doğru parçasının uzunluğunu ayrı benzerlik oranlarıyla bulup toplar.',
 kart='K-GBI-03 (iki paralel doğru parçası)',
 metin='ABC üçgeninde D ve F noktaları [AB] üzerinde, E ve G noktaları [AC] üzerindedir. [DE] // [FG] // [BC] dir. Şekilde |AD| = 2 cm, |DF| = 3 cm, |FB| = 5 cm ve |BC| = 20 cm olarak verilmiştir. Şekil ölçekli değildir.\nBuna göre, |DE| + |FG| toplamı kaç cm’dir?',
 dogru=14,yan=[(4,'Yalnız |DE| = 4 cm yi bulup |FG| yi hesaplamamış.','dikkat'),(10,'Yalnız |FG| = 10 cm yi bulup |DE| yi eklememiş.','dikkat'),(24,'|FG| yerine tabanı almış: 4 + 20 = 24.','bilgi'),(34,'Üç paralel doğru parçasını da toplamış: 4 + 10 + 20 = 34.','dikkat')],
 istenen='|DE| + |FG| toplamı (cm).',
 ip=['A köşesinden başlayarak [DE] ve [FG] nin hangi benzer üçgenlerin tabanları olduğunu düşün; her biri için A’dan ölçülen uzunluk farklıdır.'],
 bilgi=[BENZ,PAR],
 ad=[A('|DE| yi bul','[DE] // [BC] olduğundan ADE ∼ ABC; |AB| = 2 + 3 + 5 = 10.','|DE| / 20 = 2 / 10 → |DE| = 4'),A('|FG| yi bul','[FG] // [BC] olduğundan AFG ∼ ABC; |AF| = 2 + 3 = 5.','|FG| / 20 = 5 / 10 → |FG| = 10'),A('Toplamı yaz','İstenen iki uzunluğun toplamı.','|DE| + |FG| = 4 + 10 = 14')],
 puf='Her paralel doğru parçası için A köşesinden ona kadar olan uzunluğu ayrı ayrı yaz; sorulan ifadenin hangi parçaların toplamı olduğunu sonda tekrar oku.',sekil=SK)

# ===== 04 · yamuk, yan kenar uzantıları · orta · hikâyeli =====
kartlab(4,'Yan kenarların uzantıları','Yamuğun yan kenarları uzatılınca tabanları paralel iki üçgen oluşur; uzantı ve yan kenarlar benzerlik oranından bulunur.','Parçayı bütün sanmak; yalnız uzantıyı bulup bırakmak; tabanların farkını oran sanmak.','orta',4,'ge-bzi-yamuk','Yamukta yan kenar uzantıları')
AB4,DC4,AD4=8,20,6
# EA/(EA+AD)=AB/DC -> EA=AD*AB/(DC-AB)=6*8/12=4
EA4=AD4*AB4/(DC4-AB4); assert EA4==4; ED4=EA4+AD4; assert ED4==10 and abs(EA4/ED4-AB4/DC4)<1e-12
sD=.25; D4=(0,0); C4=(DC4*sD,0); E4=add(D4,mul((cos(radians(66)),sin(radians(66))),ED4*sD)); A4=lerp(E4,D4,EA4/ED4); B4=lerp(E4,C4,EA4/ED4)
assert abs(A4[1]-B4[1])<1e-9 and abs(dist(A4,B4)/sD-8)<1e-9 and abs(dist(A4,D4)/sD-6)<1e-9
f=F(); f.poly([A4,B4,C4,D4]); f.line(E4,A4,'dashed'); f.line(E4,B4,'dashed'); f.par(A4,B4); f.par(D4,C4); ic=cen([A4,B4,C4,D4])
f.node(add(mid(A4,B4),(0,-.3)),'$8$'); f.node(add(mid(D4,C4),(0,-.3)),'$20$'); f.sl('$6$',A4,D4,ic,.3)
vlabs(f,[('A',A4),('B',B4),('C',C4),('D',D4)],ic); f.vl('E',E4,(0,1),.3)
SK=f.svg()
assert sorted([2.4,4,6,8,10])==sorted([AD4*AB4/DC4,EA4,AD4,AB4,ED4])
q('0004',tipId='ge-bzi-yamuk',tip='Yamukta yan kenar uzantıları',z='orta',kalip='hikâyeli',alt='Yamuk Arsa',kaz='Yamuğun yan kenarlarının uzantılarıyla oluşan benzer üçgenlerden uzunluk hesaplar.',
 kart='K-GBI-04 (yan kenar uzantıları)',
 metin='Yamuk biçimli ABCD arsasında [AB] // [DC] dir. Arsanın yan kenarları olan [DA] ve [CB] doğrusal çitleri, A ve B uçlarından uzatıldığında E noktasında kesişmektedir. Şekilde |AB| = 8 m, |DC| = 20 m ve |AD| = 6 m olarak verilmiştir. Şekil ölçekli değildir.\nBuna göre, |ED| kaç metredir?',
 dogru=10,yan=[(2.4,'Oranı |AD| × |AB| ÷ |DC| diye kurmuş.','islem'),(4,'|EA| = 4 m yi bulup |ED| ye geçmemiş.','dikkat'),(6,'|ED| = |AD| yazmış.','bilgi'),(8,'|ED| yerine |AB| = 8 uzunluğunu vermiş.','dikkat')],
 istenen='|ED| uzunluğu (m).',
 ip=['EAB ve EDC üçgenlerinin açıları arasında nasıl bir ilişki var? |EA| = y diyerek |ED| yi y cinsinden yazmayı dene.'],
 bilgi=[BENZ,YAMUK],
 ad=[A('Benzer üçgenleri belirle','[AB] // [DC] olduğundan yöndeş açılar eşittir ve E açısı ortaktır.','EAB ∼ EDC'),A('Oranı kur','|EA| = y olsun; |ED| = y + 6 olur.','y / (y + 6) = 8 / 20'),A('y’yi çöz','İçler dışlar çarpımı.','20y = 8y + 48 → y = 4'),A('|ED| yi hesapla','|ED| = |EA| + |AD|.','|ED| = 4 + 6 = 10')],
 puf='Uzantıya bilinmeyen verip bütün kenarı da onun cinsinden yazmak, oranı tek denkleme dönüştürür.',sekil=SK)

# ===== 05 · paralelkenar + uzantı · orta =====
kartlab(5,'Paralelkenarda uzantı','Paralelkenarın karşılıklı kenarları paralel olduğundan bir kenarın uzantısıyla oluşan üçgenler benzerlik verir.','Oranı ters kurmak; istenen parça yerine uzantının toplamını vermek.','orta',3,'ge-bzi-paralelkenar','Paralelkenarda benzerlik')
AB5,BE5,EC5=12,3,2; CF5=AB5*EC5/BE5; assert abs(CF5-8)<1e-12; DF5=AB5+CF5
sB=.35; A5=(0,0); B5=(AB5*sB,0); C5=add(B5,mul((cos(radians(65)),sin(radians(65))),2.4)); D5=add(A5,sub(C5,B5)); E5=lerp(B5,C5,BE5/(BE5+EC5))
F5=kesis(A5,E5,D5,add(D5,(1,0))); assert abs(F5[0]-C5[0]-CF5*sB)<1e-9 and F5[1]-C5[1]<1e-9
f=F(); f.poly([A5,B5,C5,D5]); f.line(C5,F5,'dashed'); f.line(A5,F5); f.par(A5,B5); f.par(D5,C5); ic=cen([A5,B5,C5,D5])
f.node(add(mid(A5,B5),(0,-.3)),'$12$'); f.node(add(mid(B5,E5),(-.3,-.05)),'$3$'); f.node(add(mid(E5,C5),(-.3,.1)),'$2$')
vlabs(f,[('A',A5),('B',B5),('C',C5),('D',D5)],ic); f.vl('E',E5,(1,-.5),.3); f.vl('F',F5,(1,.4),.3)
SK=f.svg()
assert sorted([4.8,8,12,18,20])==sorted([AB5*EC5/(BE5+EC5),CF5,AB5,AB5*BE5/EC5,DF5])
q('0005',tipId='ge-bzi-paralelkenar',tip='Paralelkenarda benzerlik',z='orta',alt='Paralelkenar ve Uzantı',kaz='Paralelkenarda bir kenarın uzantısıyla oluşan benzer üçgenlerden uzunluk bulur.',
 kart='K-GBI-05 (paralelkenarda uzantı)',
 metin='ABCD paralelkenarında E noktası [BC] üzerindedir. [AE] doğru parçası uzatıldığında, [DC] doğru parçasının C yönündeki uzantısını F noktasında kesmektedir. Şekilde |AB| = 12 cm, |BE| = 3 cm ve |EC| = 2 cm olarak verilmiştir. Şekil ölçekli değildir.\nBuna göre, |CF| kaç cm’dir?',
 dogru=8,yan=[(4.8,'Parça / bütün oranını kullanmış: 12 × 2 ÷ 5 = 4,8.','dikkat'),(12,'|CF| = |AB| yazmış.','bilgi'),(18,'Oranı ters kurmuş: 12 × 3 ÷ 2 = 18.','dikkat'),(20,'|CF| yerine |DF| = 12 + 8 = 20 uzunluğunu vermiş.','dikkat')],
 istenen='|CF| uzunluğu (cm).',
 ip=['[AB] ve [DF] doğruları arasındaki ilişkiyi düşün; E noktasında kesişen iki doğrunun oluşturduğu hangi iki üçgenin açıları eşit?'],
 bilgi=[BENZ,ALAN,PAR],
 ad=[A('Paralelliği belirle','Paralelkenarda [AB] // [DC] dir; [CF], [DC] nin uzantısı olduğundan [AB] // [CF] olur.','[AB] // [CF]'),A('Benzer üçgenleri yaz','Ters açılar eşittir ve E noktasında karşı açılar eşittir.','EBA ∼ ECF'),A('Oranı kur ve çöz','Karşılıklı kenarların oranı sabittir.','|CF| / |AB| = |EC| / |BE| → |CF| = 12 × 2 ÷ 3 = 8')],
 puf='Benzer üçgenlerde eşleştirmeyi yaparken eşit açıların karşısındaki kenarları belirle.',sekil=SK)

# ===== 06 · Thales cebirsel · orta =====
kartlab(6,'Cebirsel Thales','Paralel doğrular kesenlerde orantılı parçalar ayırır; parçalardan biri cebirsel verilince kurulan denklemden istenen uzunluk bulunur.','x’i bulup bırakmak; parçayı toplam sanmak; oranı ters kurmak.','orta',4,'ge-bzi-thales','Thales teoremi (cebirsel)')
x6=5; AB6=2*x6-1; BC6=x6+2; DE6=18; EF6=14; assert AB6*EF6==BC6*DE6 and AB6+BC6==16
yA,yC=3.2,0; yB=yA-(yA-yC)*AB6/(AB6+BC6); A6=(0.2,yA); C6=(1.8,yC); B6=lerp(A6,C6,AB6/(AB6+BC6)); D6=(2.8,yA); F6=(5.8,yC); E6=lerp(D6,F6,DE6/(DE6+EF6)); assert abs(B6[1]-E6[1])<1e-9
f=F()
for y_ in (yA,B6[1],yC): f.line((-.8,y_),(6.3,y_)); f.par((5.6,y_),(6.1,y_))
f.line(A6,C6); f.line(D6,F6)
f.sl('$2x-1$',A6,B6,(3,1.6),.5); f.sl('$x+2$',B6,C6,(3,1.6),.5); f.sl('$18$',D6,E6,(2,1.6),.4); f.sl('$14$',E6,F6,(2,1.6),.4)
f.vl('A',A6,(-.4,1),.3); f.vl('B',B6,(-1,.5),.3); f.vl('C',C6,(-.4,-1),.3); f.vl('D',D6,(.4,1),.3); f.vl('E',E6,(1,.5),.3); f.vl('F',F6,(.4,-1),.3)
SK=f.svg()
assert sorted([5,7,9,16,32])==sorted([x6,BC6,AB6,AB6+BC6,DE6+EF6])
q('0006',tipId='ge-bzi-thales',tip='Thales teoremi (cebirsel)',z='orta',alt='Cebirsel Parçalar',kaz='Paralel doğruların ayırdığı orantılı parçalardan denklem kurarak uzunluk bulur.',
 kart='K-GBI-06 (cebirsel Thales)',
 metin='Şekilde birbirine paralel üç doğru, [AC] ve [DF] doğru parçalarını sırasıyla A, B, C ve D, E, F noktalarında kesmektedir; A ile D, B ile E, C ile F noktaları aynı paralel doğru üzerindedir. |AB| = (2x − 1) cm, |BC| = (x + 2) cm, |DE| = 18 cm ve |EF| = 14 cm dir. Şekil ölçekli değildir.\nBuna göre, |AC| kaç cm’dir?',
 dogru=16,yan=[(5,'x = 5 i bulup |AC| yi hesaplamamış.','dikkat'),(7,'|BC| = x + 2 = 7 uzunluğunu vermiş.','dikkat'),(9,'|AB| = 2x − 1 = 9 uzunluğunu vermiş.','dikkat'),(32,'|AC| yerine |DF| = 18 + 14 = 32 uzunluğunu vermiş.','dikkat')],
 istenen='|AC| uzunluğu (cm).',
 ip=['Üç paralel doğrunun iki kesende ayırdığı parçaları karşılıklı yaz; bir kesendeki iki parçanın oranı diğer kesendeki oranla ilişkilidir.'],
 bilgi=[THA],
 ad=[A('Orantıyı kur','Paralel doğrular iki kesende parçaları orantılı ayırır.','(2x − 1) / (x + 2) = 18 / 14'),A('x’i bul','İçler dışlar çarpımı.','14(2x − 1) = 18(x + 2) → 28x − 14 = 18x + 36 → x = 5'),A('Parçaları hesapla','x = 5 ile iki parçayı bul.','|AB| = 9, |BC| = 7'),A('|AC| yi bul','Parçaların toplamı.','|AC| = 9 + 7 = 16')],
 puf='Cebirsel ifadeleri doğrudan oranın içine yazıp, bulduğun x değerini parçalarda yerine koyarak denetle.',sekil=SK)

# ===== 07 · köşegenler, eşit açı · orta =====
kartlab(7,'Köşegenlerde eşit açı','İki köşegenin kesişiminde eşit açılar benzer üçgenler oluşturur; karşılıklı kenarlar doğru eşleştirilerek uzunluk bulunur.','Köşeleri harf sırasıyla eşleştirmek; çarpım yerine oranı ters yazmak.','orta',3,'ge-bzi-aa','Köşegenlerde açı eşitliği ve benzerlik')
AE7,EC7,BE7=4,9,3; ED7=AE7*EC7/BE7; assert ED7==12
s7=.38; E7=(0,0)
def pol(r,t): return (r*s7*cos(radians(t)),r*s7*sin(radians(t)))
A7=pol(AE7,160); C7=pol(EC7,-20); B7=pol(BE7,70); D7=pol(ED7,250)
assert abs(ang(A7,B7,C7)-ang(D7,B7,C7))<1e-9
f=F(); f.poly([A7,B7,C7,D7]); f.line(A7,C7); f.line(B7,D7); arct(f,A7,B7,C7,.4); arct(f,D7,B7,C7,.4)
ic=cen([A7,B7,C7,D7])
f.node(add(mid(A7,E7),(0,-.28)),'$4$'); f.node(add(mid(B7,E7),(.28,0)),'$3$'); f.node(add(mid(E7,C7),(0,.28)),'$9$')
vlabs(f,[('A',A7),('B',B7),('C',C7),('D',D7)],ic); f.vl('E',E7,(-.9,-.42),.32)
SK=f.svg()
assert sorted([6.75,9,12,13,36])==sorted([EC7*BE7/AE7,EC7,ED7,AE7+EC7,AE7*EC7])
q('0007',tipId='ge-bzi-aa',tip='Köşegenlerde açı eşitliği ve benzerlik',z='orta',alt='Eşit Açılı Köşegenler',kaz='Köşegenlerin kesişiminde eşit açılardan benzer üçgenleri bulup uzunluk hesaplar.',
 kart='K-GBI-07 (köşegenlerde eşit açı)',
 metin='Şekilde ABCD dörtgeninin köşegenleri E noktasında kesişmektedir. Yay işaretleriyle gösterildiği gibi m(BAC) = m(BDC) dir. |AE| = 4 cm, |BE| = 3 cm ve |EC| = 9 cm olarak verilmiştir. Şekil ölçekli değildir.\nBuna göre, |ED| kaç cm’dir?',
 dogru=12,yan=[(6.75,'Oranı yanlış eşleştirmiş: |ED| = |EC| × |BE| ÷ |AE| = 6,75.','dikkat'),(9,'|ED| = |EC| yazmış.','bilgi'),(13,'|ED| yerine |AC| = 4 + 9 = 13 uzunluğunu vermiş.','dikkat'),(36,'|AE| × |EC| = 36 çarpımını vermiş, |BE| ye bölmemiş.','islem')],
 istenen='|ED| uzunluğu (cm).',
 ip=['m(BAC) = m(BDC) eşitliği ve E’deki karşı açılar hangi iki üçgenin açılarını eşitler? Üçgenlerin adını yazarken eşit açıları aynı sırada yaz.'],
 bilgi=[BENZ],
 ad=[A('Benzer üçgenleri bul','m(BAE) = m(CDE) ve E’deki karşı (ters) açılar eşittir.','EAB ∼ EDC (A ↔ D, B ↔ C, E ↔ E)'),A('Oranı kur','Karşılıklı kenarların oranı sabittir.','|AE| / |DE| = |BE| / |CE| → 4 / |DE| = 3 / 9'),A('|ED| yi bul','İçler dışlar çarpımı.','|ED| = 4 × 9 ÷ 3 = 12')],
 puf='Benzer üçgenin adını yazarken eşit açıların köşelerini aynı sırayla yaz; karşılıklı kenarlar böylece görünür.',sekil=SK)

# ===== 08 · orta nokta + yardımcı paralel · zor =====
kartlab(8,'Kenarortay ve kesen doğru','Bir köşeden çizilen doğru parçalarının oranları verildiğinde kesişimin karşı kenarı böldüğü oran, uygun bir paralel çizilerek benzerliklerle bulunur.','Oranı eşleştirirken parçaları karıştırmak; F’yi orta nokta sanmak; yalnız bir benzerlik kurup bırakmak.','zor',6,'ge-bzi-yardimci','Yardımcı çizimle benzerlik')
AE8,ED8,AC8=6,4,28; # D orta nokta: G, [CF] nin orta noktası; AF:FG = AE:ED ; FG = GC  =>  AF:FC = AE : 2·ED
AF8=AC8*AE8/(AE8+2*ED8); assert abs(AF8-12)<1e-12
B8=(0,0); C8=(5.6,0); A8=(1.7,3.8); D8=mid(B8,C8); E8=lerp(A8,D8,AE8/(AE8+ED8)); F8=kesis(B8,E8,A8,C8)
assert abs(dist(A8,F8)/dist(A8,C8)*28-12)<1e-9 and abs(dist(A8,E8)/dist(E8,D8)-1.5)<1e-9
f=F(); ic=cen([A8,B8,C8]); f.poly([A8,B8,C8]); f.line(A8,D8); f.line(B8,F8); f.tick(B8,D8); f.tick(D8,C8)
f.sl('$6$',A8,E8,(0,1.5),.3); f.sl('$4$',E8,D8,(0,1.5),.3)
f.node(add(lerp(A8,C8,.72),(.38,.2)),'$28$')
vlabs(f,[('A',A8),('B',B8),('C',C8)],ic); f.vl('D',D8,(0,-1),.3); f.vl('E',E8,(.9,-.3),.3); f.vl('F',F8,(-1,.3),.3)
SK=f.svg()
assert sorted([12,14,16,16.8,21])==sorted([AF8,AC8/2,AC8*4/7,AC8*AE8/(AE8+ED8),AC8*3/4])
q('0008',tipId='ge-bzi-yardimci',tip='Yardımcı çizimle benzerlik',z='zor',alt='Kenarortay ve Kesen',kaz='Yardımcı paralel çizerek iki ayrı benzerlikten kesişim oranını bulur.',
 kart='K-GBI-08 (kenarortay ve kesen)',
 metin='ABC üçgeninde D noktası [BC] kenarının orta noktasıdır. [AD] üzerinde alınan E noktası için |AE| = 6 cm ve |ED| = 4 cm dir. [BE] doğru parçasının E yönündeki uzantısı [AC] kenarını F noktasında kesmektedir ve |AC| = 28 cm dir. Şekil ölçekli değildir.\nBuna göre, |AF| kaç cm’dir?',
 dogru=12,yan=[(14,'F noktasını [AC] nin orta noktası sanmış: 28 ÷ 2 = 14.','bilgi'),(16,'|AF| yerine |FC| = 28 × 4 ÷ 7 = 16 uzunluğunu bulmuş.','dikkat'),(16.8,'|AF| / |AC| = |AE| / |AD| yazmış: 28 × 6 ÷ 10 = 16,8.','bilgi'),(21,'Oranı 3 : 4 alıp |AF| = 28 × 3 ÷ 4 = 21 bulmuş.','dikkat')],
 istenen='|AF| uzunluğu (cm).',
 ip=['Orta nokta bilgisini hangi paralellik ya da benzerlikle kullanabilirsin? Şekle ek bir doğru çizmen gerekir mi?'],
 bilgi=[BENZ,THA,KENAR],
 ad=[A('Yardımcı paralel çiz','D’den [BF] ye paralel çizilen doğru [AC] yi G’de kessin.','[DG] // [BF]'),A('BCF üçgeninde oran','D, [BC] nin orta noktası ve [DG] // [BF] olduğundan G, [CF] nin orta noktasıdır.','|FG| = |GC|'),A('ADG üçgeninde oran','[EF] // [DG] olduğundan kenarlar orantılı bölünür.','|AF| / |FG| = |AE| / |ED| = 6 / 4 = 3 / 2'),A('Parçaları paylaştır','|AF| = 3k, |FG| = |GC| = 2k olsun.','|AC| = 3k + 2k + 2k = 7k = 28 → k = 4'),A('|AF| yi bul','|AF| = 3k.','|AF| = 3 × 4 = 12')],
 puf='Bir köşeden çıkan doğruların oranları bilindiğinde, bir paralel çizerek oranı başka bir üçgene taşıyabilirsin.',sekil=SK)

# ===== 09 · yamukta paralel doğru parçası · zor =====
kartlab(9,'Yamukta taban paralelinin uzunluğu','Tabanlara paralel olup yan kenarları oranlı bölen doğru parçasının uzunluğu, yan kenardan paralel çizilerek oluşan benzer üçgenlerle bulunur.','Aritmetik ortalama almak; oranı ters kurmak; tabanlar farkını doğrudan eklemek.','zor',5,'ge-bzi-yamuk','Yamukta yan kenar uzantıları')
AB9,DC9,AE9,ED9=10,25,6,4; EF9=AB9+(DC9-AB9)*AE9/(AE9+ED9); assert abs(EF9-19)<1e-12
s9=.2; D9=(0,0); C9=(DC9*s9,0); A9=(1.4,2.6); B9=add(A9,(AB9*s9,0)); E9=lerp(A9,D9,AE9/(AE9+ED9)); F9=lerp(B9,C9,AE9/(AE9+ED9))
assert abs(E9[1]-F9[1])<1e-9 and abs(dist(E9,F9)/s9-19)<1e-9
f=F(); ic=cen([A9,B9,C9,D9]); f.poly([A9,B9,C9,D9]); f.line(E9,F9); f.par(A9,B9); f.par(D9,C9); f.par(E9,F9)
f.node(add(mid(A9,B9),(0,.3)),'$10$'); f.node(add(mid(D9,C9),(0,-.3)),'$25$'); f.sl('$6$',A9,E9,ic,.3); f.sl('$4$',E9,D9,ic,.3)
vlabs(f,[('A',A9),('B',B9),('C',C9),('D',D9)],ic); f.vl('E',E9,(-1,0),.3); f.vl('F',F9,(1,0),.3)
SK=f.svg()
assert sorted([10,15,16,17.5,19])==sorted([AB9,DC9-AB9,(AB9*AE9+DC9*ED9)/(AE9+ED9),(AB9+DC9)/2,EF9])
q('0009',tipId='ge-bzi-yamuk',tip='Yamukta yan kenar uzantıları',z='zor',alt='Yamukta Paralel Parça',kaz='Yamukta yan kenar boyunca paralel çizerek oluşan benzer üçgenlerden paralel parçanın uzunluğunu bulur.',
 kart='K-GBI-09 (yamukta paralel doğru parçası)',
 metin='ABCD yamuğunda [AB] // [DC], |AB| = 10 cm ve |DC| = 25 cm dir. [AD] üzerindeki E noktası ile [BC] üzerindeki F noktası, [EF] // [AB] olacak biçimde alınmıştır. Şekilde |AE| = 6 cm ve |ED| = 4 cm olarak verilmiştir. Şekil ölçekli değildir.\nBuna göre, |EF| kaç cm’dir?',
 dogru=19,yan=[(10,'|EF| = |AB| yazmış.','bilgi'),(15,'Tabanların farkını (25 − 10 = 15) |EF| sanmış.','dikkat'),(16,'Ağırlıkları ters kullanmış: (10 × 6 + 25 × 4) ÷ 10 = 16.','dikkat'),(17.5,'E ve F’yi orta nokta sanıp tabanların ortalamasını almış: (10 + 25) ÷ 2.','bilgi')],
 istenen='|EF| uzunluğu (cm).',
 ip=['Yamuğu bir paralelkenar ve bir üçgene ayıran bir doğru var mı? Bu doğru hangi uzunlukları sana verir?'],
 bilgi=[BENZ,YAMUK,ALAN],
 ad=[A('Yardımcı paralel çiz','A’dan [BC] ye paralel çizilen doğru [EF] yi P, [DC] yi Q noktasında kessin.','[AQ] // [BC]'),A('Paralelkenarları bul','ABFP ve ABCQ paralelkenarlardır (karşılıklı kenarlar paralel).','|PF| = |AB| = 10, |QC| = 10 → |DQ| = 25 − 10 = 15'),A('Benzer üçgenleri kur','[EP] // [DQ] olduğundan AEP ∼ ADQ.','|EP| / |DQ| = |AE| / |AD| = 6 / 10'),A('|EP| yi hesapla','İçler dışlar çarpımı.','|EP| = 15 × 6 ÷ 10 = 9'),A('|EF| yi yaz','|EF| = |EP| + |PF|.','|EF| = 9 + 10 = 19')],
 puf='Yamuğu bir paralelkenar ve bir üçgene ayıran yardımcı çizgi, bilinmeyen parçayı üçgenin bir kenarına dönüştürür.',sekil=SK)

# ===== 10 · kâğıt katlama · zor · hikâyeli =====
kartlab(10,'Katlanmış köşe','Dikdörtgen kâğıdın bir köşesi karşı kenara katlanınca eş uzunluklar ve dik üçgenler oluşur; benzerlik ve Pisagor birlikte kullanılır.','Eş uzunlukları görememek; benzer üçgenlerin hangi köşelerinin eşleştiğini karıştırmak; BE ile FB’yi karıştırmak.','zor',6,'ge-bzi-katlama','Kâğıt katlama ve benzerlik')
W10,L10=9,15; CE10=sqrt(L10**2-W10**2); assert abs(CE10-12)<1e-12; BE10=L10-CE10; AF10=5; FB10=W10-AF10
assert abs(AF10**2-(FB10**2+BE10**2))<1e-12 and abs(CE10/FB10-W10/BE10)<1e-12   # DCE ∼ EBF : CE/BF = DC/BE
s10=.26; A10=(0,0); B10=(W10*s10,0); C10=(W10*s10,L10*s10); D10=(0,L10*s10); E10=(W10*s10,BE10*s10); F10=(AF10*s10,0)
assert abs(dist(D10,E10)-dist(D10,A10))<1e-9 and abs(dist(F10,E10)-dist(F10,A10))<1e-9
f=F(); f.fill([D10,E10,F10]); f.line(F10,A10,'dashed'); f.line(A10,D10,'dashed'); f.line(D10,C10); f.line(C10,B10); f.line(B10,F10); f.line(D10,E10); f.line(E10,F10); f.line(D10,F10)
dim(f,A10,B10,'$9$',(0,-1),.55); dim(f,A10,D10,'$15$',(-1,0),.6)
vlabs(f,[('B',B10),('C',C10)],(1.2,2)); f.vl('A',A10,(-1,-1),.3); f.vl('D',D10,(-1,1),.3); f.vl('E',E10,(1,0),.3); f.vl('F',F10,(.3,-1),.3)
SK=f.svg()
assert sorted([3,4,4.5,5,12])==sorted([BE10,FB10,W10/2,AF10,CE10])
q('0010',tipId='ge-bzi-katlama',tip='Kâğıt katlama ve benzerlik',z='zor',kalip='hikâyeli',alt='Katlanan Köşe',kaz='Katlamada oluşan eş uzunlukları ve benzer dik üçgenleri kullanarak uzunluk hesaplar.',
 kart='K-GBI-10 (katlanmış köşe)',
 metin='Dikdörtgen biçimindeki ABCD kâğıdında |AB| = 9 cm ve |AD| = 15 cm dir. Kâğıt, D köşesinden geçen ve [AB] kenarını F noktasında kesen bir doğru boyunca, A köşesi [BC] kenarı üzerindeki E noktasına gelecek biçimde katlanmıştır. Şekil, katlanmış durumu göstermekte ve ölçekli değildir.\nBuna göre, katlanmadan önce [AF] doğru parçasının uzunluğu kaç cm’dir?',
 dogru=5,yan=[(3,'|BE| = 3 cm yi bulup bırakmış.','dikkat'),(4,'|FB| = 4 cm yi |AF| sanmış.','dikkat'),(4.5,'Katlama çizgisinin [AB] yi ortaladığını sanmış: 9 ÷ 2 = 4,5.','bilgi'),(12,'|CE| = 12 cm yi vermiş.','dikkat')],
 istenen='|AF| uzunluğu (cm).',
 ip=['A, E noktasına geldiğine göre |DA| ile |DE| arasında, |FA| ile |FE| arasında nasıl bir ilişki vardır? Önce [CE] nin uzunluğunu bulmayı dene.'],
 bilgi=[BENZ,PIS,KAT],
 ad=[A('Eş uzunlukları yaz','Katlamada A noktası E noktasına gelir.','|DE| = |DA| = 15, |FE| = |FA|'),A('|CE| yi bul','DCE dik üçgeninde Pisagor.','|CE|² = 15² − 9² = 144 → |CE| = 12, |BE| = 15 − 12 = 3'),A('Benzer üçgenleri belirle','D’deki katlanmış açı dik olduğundan CED ve BFE üçgenlerinin açıları eşittir.','DCE ∼ EBF'),A('|FB| yi bul','Karşılıklı kenarlar orantılıdır.','|CE| / |FB| = |DC| / |BE| → 12 / |FB| = 9 / 3 → |FB| = 4'),A('|AF| yi hesapla','|AF| = |AB| − |FB|.','|AF| = 9 − 4 = 5')],
 puf='Katlama sorularında önce eşit olan uzunlukları ve açıları listele, sonra hangi dik üçgenlerin benzer olduğuna bak.',sekil=SK)
bitir_geo('benzerlikiki','Üçgende Benzerlik')
