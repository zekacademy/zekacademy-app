"""TYT Geometri · İkizkenar Üçgen (ikinci paket, hafif mod). Şekil koordinatları hesaplanır, TikZ aynı değerlerden üretilir; her cevap ve çeldirici assert edilir."""
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
P=Parti('ikizkenariki','İkizkenar Üçgen','geo|İkizkenar Üçgen',ders='TYT Geometri',idon='tytgeo')
def ayak(P_,V,W):
    u=un(sub(W,V)); t_=(P_[0]-V[0])*u[0]+(P_[1]-V[1])*u[1]; return add(V,mul(u,t_))
def vlabs(f,pts,ic):
    for n_,p_ in pts: vtx(f,p_,n_,ic)
IKIZ=B('İkizkenar üçgen','iki kenarı eşit olan üçgendir; eşit kenarların karşısındaki açılar eşittir. İç açıların toplamı 180° dir. Örnek: tepe açısı 80° olan ikizkenar üçgende taban açılarının her biri (180° − 80°) ÷ 2 = 50° dir')
DIS=B('Dış açı','üçgenin bir dış açısı, kendisine komşu olmayan iki iç açının toplamına eşittir. Örnek: iç açıları 30° ve 50° olan bir üçgenin, üçüncü köşedeki dış açısı 80° dir')
ESK=B('Eşkenar üçgen','üç kenarı eşit olan üçgendir; üç açısı da 60° dir. Örnek: kenarı 5 cm olan eşkenar üçgenin çevresi 15 cm dir')
ACIORTAY=B('Açıortay','bir açıyı iki eşit açıya ayıran doğrudur. Örnek: ölçüsü 80° olan bir açının açıortayı onu 40° ve 40° lik iki açıya ayırır')
KENARORTAY=B('Kenarortay ve çevre','bir köşeyi karşı kenarın orta noktasına birleştiren doğru parçasına kenarortay denir; orta nokta o kenarı iki eşit parçaya böler. Çevre, kenar uzunluklarının toplamıdır. Örnek: kenarları 5, 6, 7 olan üçgenin çevresi 18 dir')
ALAN=B('Üçgenin alanı','bir kenar uzunluğu ile o kenara ait yüksekliğin çarpımının yarısıdır. Örnek: tabanı 10 cm, yüksekliği 4 cm olan üçgenin alanı 10 × 4 ÷ 2 = 20 cm² dir')
PIS=B('Pisagor bağıntısı','dik üçgende dik kenarların kareleri toplamı hipotenüsün karesine eşittir. Örnek: dik kenarları 7 ve 24 olan üçgenin hipotenüsü √(49 + 576) = 25 tir')
DIKACI=B('Dik üçgende açılar','dik üçgenin iki dar açısının toplamı 90° dir. Örnek: bir dar açısı 35° olan dik üçgenin diğer dar açısı 55° dir')
PAR=B('Paralel doğrular ve açılar','iki paralel doğruyu bir doğru kesince oluşan yöndeş açılar ve ters açılar eşittir. Karşı (ters) açılar da her zaman eşittir. Örnek: paralel iki doğruyu kesen doğrunun bir yanda yaptığı iki ters açıdan biri 65° ise diğeri de 65° dir')
ESLIK=B('Üçgenlerde eşlik','karşılıklı kenarları ve açıları eşit olan üçgenlere eş üçgenler denir. İki açısı ve bir kenarı karşılıklı eşit olan üçgenler eştir. Örnek: iki üçgenin ikişer açısı 40° ve 60° ise ve 8 cm lik kenarları bu açılara göre aynı konumdaysa üçgenler eştir')
konu('geo|İkizkenar Üçgen','İkizkenar Üçgen')
def kartlab(no,alt,fikir,tuzak,z,adim,tipId,tip,kalip='şekilli'):
    kart(f'K-GIKI-{no:02d}',alt,fikir,tuzak,z,kalip,adim,tipId,tip,'ÖSYM 2018–2026 TYT Geometri soruları (yalnız mantık) · MEB 9–10. sınıf geometri'); TIPK[tipId]=P.k

# ===== 01 · çatı, dikme ile açı · kolay · hikâyeli =====
kartlab(1,'Tepeden inen dikme ve açı','İkizkenar üçgende taban açıları eşittir; dik üçgenin dar açıları tümlerdir. Dikmenin ayırdığı açı iç açılardan bulunur.','Dar açıyı bütünler sanmak; tepe açısını sorulan açı sanmak; taban açısını yarıya bölmek.','kolay',3,'ge-ik2-taban','İkizkenar üçgende açı hesabı',kalip='hikâyeli')
b1=1.7; B1=(-b1,0); C1=(b1,0); A1=(0,b1*tan(radians(66))); D1=(0,0)
assert abs(ang(B1,A1,C1)-66)<1e-9 and abs(ang(A1,D1,C1)-24)<1e-9 and abs(dist(A1,B1)-dist(A1,C1))<1e-9
f=F(); f.poly([A1,B1,C1]); f.line(A1,D1,'dashed'); f.dik(D1,A1,C1,.2); f.tick(A1,B1); f.tick(A1,C1)
f.arc(B1,C1,A1,.65,'$66^\\circ$',1.15); f.arc(A1,C1,D1,.95,'$x$',1.45)
vlabs(f,[('A',A1),('B',B1),('C',C1)],(0,1.5)); f.vl('D',D1,(0,-1),.3)
SK=f.svg()
assert sorted([24,33,48,66,114])==sorted([90-66,66//2,180-2*66,66,180-66])
q('0001',tipId='ge-ik2-taban',tip='İkizkenar üçgende açı hesabı',z='kolay',kalip='hikâyeli',alt='Çatı Açısı',kaz='İkizkenar üçgende taban açılarının eşitliğinden ve dik üçgenin açılarından bir açıyı bulur.',
 kart='K-GIKI-01 (tepeden inen dikme ve açı)',
 metin='Bir evin ön cephesindeki çatı, |AB| = |AC| olan ikizkenar üçgen biçimindedir. Çatıyı ortadan destekleyen [AD] direği, tepe noktası A’dan taban [BC] ye diktir ve D noktası taban üzerindedir. Şekilde B köşesindeki açının ölçüsü verilmiştir; şekil ölçekli değildir.\nBuna göre, x = m(CAD) kaç derecedir?',
 dogru=24,yan=[(33,'Taban açısını yarıya bölmüş: 66° ÷ 2 = 33°.','bilgi'),(48,'Tepe açısını (180° − 2 × 66° = 48°) bulup bırakmış.','dikkat'),(66,'Taban açısını x sanmış.','dikkat'),(114,'Taban açısının bütünlerini (180° − 66°) yazmış.','islem')],
 istenen='x = m(CAD) açısının ölçüsü.',
 ip=['|AB| = |AC| olduğunda C köşesindeki açı için ne söyleyebilirsin? ADC üçgeninin açıları arasındaki ilişkiyi yaz.'],
 bilgi=[IKIZ,DIKACI],
 ad=[A('C açısını bul','|AB| = |AC| olduğundan taban açıları eşittir.','m(ACB) = m(ABC) = 66°'),A('ADC üçgenini kur','[AD] ⊥ [BC] olduğundan D köşesindeki açı 90° dir; iç açılar toplamı 180°.','90° + 66° + x = 180°'),A('x’i bul','Eşitliği çöz.','x = 24°')],
 puf='Bulduğun açıyı, üçgenin diğer açılarıyla toplayarak 180° ye ulaşıp ulaşmadığını denetle.',sekil=SK)

# ===== 02 · cebirsel kenar, çevre · kolay =====
kartlab(2,'Cebirsel eş kenarlar','Eş kenarların cebirsel ifadeleri eşitlenir; bulunan x ile kenarlar ve çevre hesaplanır.','x’i bulup bırakmak; yalnız bir eş kenarı çevre sanmak; eş kenarlardan birini unutmak.','kolay',3,'ge-ik2-kenar','İkizkenar üçgende kenar ve çevre')
x2=6; ab2=3*x2-4; ac2=x2+8; bc2=10; assert ab2==ac2==14; cev2=ab2+ac2+bc2; assert cev2==38
sc=.3; B2=(-bc2/2*sc,0); C2=(bc2/2*sc,0); A2=(0,sqrt(ab2**2-(bc2/2)**2)*sc); assert abs(dist(A2,B2)/sc-14)<1e-9
f=F(); f.poly([A2,B2,C2]); f.tick(A2,B2); f.tick(A2,C2); ic=cen([A2,B2,C2])
f.sl('$3x-4$',A2,B2,C2,.8); f.sl('$x+8$',A2,C2,B2,.7); f.sl('$10$',B2,C2,A2,.3)
vlabs(f,[('A',A2),('B',B2),('C',C2)],ic)
SK=f.svg()
assert sorted([6,14,24,28,38])==sorted([x2,ab2,ab2+bc2,2*ab2,cev2])
q('0002',tipId='ge-ik2-kenar',tip='İkizkenar üçgende kenar ve çevre',z='kolay',alt='Cebirsel Kenarlar',kaz='İkizkenar üçgenin eş kenarlarından x’i bulup çevresini hesaplar.',
 kart='K-GIKI-02 (cebirsel eş kenarlar)',
 metin='Şekilde |AB| = |AC| olan bir ABC üçgeni verilmiştir. Kenar uzunlukları cm cinsinden |AB| = 3x − 4, |AC| = x + 8 ve |BC| = 10 olarak gösterilmiştir (x bir gerçek sayıdır). Şekil ölçekli değildir.\nBuna göre, ABC üçgeninin çevresi kaç cm’dir?',
 dogru=38,yan=[(6,'x = 6 yı bulup çevreyi hesaplamamış.','dikkat'),(14,'Bir eş kenarın uzunluğunu (14) çevre sanmış.','dikkat'),(24,'Eş kenarlardan yalnız birini taban ile toplamış: 14 + 10 = 24.','dikkat'),(28,'Yalnız iki eş kenarı toplamış: 14 + 14 = 28.','dikkat')],
 istenen='ABC üçgeninin çevresi (cm).',
 ip=['Eşit olan iki kenarın uzunlukları hakkında ne biliyorsun? Bu bilgiyle x i bulduktan sonra üç kenarı da yaz.'],
 bilgi=[IKIZ,B('Çevre','bir çokgenin çevresi, bütün kenar uzunluklarının toplamıdır. Örnek: kenarları 6, 6 ve 9 olan ikizkenar üçgenin çevresi 21 dir')],
 ad=[A('Eş kenarları eşitle','|AB| = |AC| olduğundan ifadeler eşittir.','3x − 4 = x + 8'),A('x’i bul','Bilinmeyenleri bir tarafa topla.','2x = 12 → x = 6'),A('Kenarları hesapla','x = 6 ile kenarlar.','|AB| = |AC| = 14, |BC| = 10'),A('Çevreyi yaz','Üç kenarın toplamı.','14 + 14 + 10 = 38')],
 puf='x’i bulduktan sonra soruda istenenin x mi, bir kenar mı, yoksa çevre mi olduğuna son kez bak.',sekil=SK)

# ===== 03 · iç açıortaylar · orta =====
kartlab(3,'Taban açıortaylarının kesişimi','İkizkenar üçgende taban açıları eşit olduğundan açıortaylar da eşit açılar ayırır; kesişim noktasındaki açı iç açılar toplamından bulunur.','Taban açısını açıortay açısı sanmak; 90° ye yarım açıyı eklemek; tepe açısının bütünlerini yazmak.','orta',4,'ge-ik2-aciortay','İkizkenar üçgende açıortaylar')
L3=5; Ab=40; B3=(-L3*sin(radians(20)),0); C3=(L3*sin(radians(20)),0); A3=(0,L3*cos(radians(20)))
K3=incenter(A3,B3,C3); D3=kesis(B3,K3,A3,C3); E3=kesis(C3,K3,A3,B3)
assert abs(ang(B3,A3,C3)-70)<1e-9 and abs(ang(B3,C3,K3)-35)<1e-9 and abs(ang(K3,B3,C3)-110)<1e-9 and abs(ang(A3,B3,C3)-40)<1e-9
f=F(); f.poly([A3,B3,C3]); f.line(B3,D3); f.line(C3,E3); f.tick(A3,B3); f.tick(A3,C3)
arct(f,B3,C3,K3,.6,1); arct(f,B3,K3,A3,.6,1); arct(f,C3,K3,B3,.6,1); arct(f,C3,A3,K3,.6,1)
f.arc(A3,B3,C3,.9,'$40^\\circ$',1.4); f.arc(K3,B3,C3,.45,'$x$',.8)
ic=cen([A3,B3,C3]); vlabs(f,[('A',A3),('B',B3),('C',C3)],ic); f.vl('D',D3,(1,.4),.3); f.vl('E',E3,(-1,.4),.3); f.vl('K',K3,(0,1),.3)
SK=f.svg()
assert sorted([35,110,125,130,140])==sorted([35,110,90+35,90+Ab,180-Ab])
q('0003',tipId='ge-ik2-aciortay',tip='İkizkenar üçgende açıortaylar',z='orta',alt='Taban Açıortayları',kaz='İkizkenar üçgenin taban açıortaylarının kesişimindeki açıyı bulur.',
 kart='K-GIKI-03 (taban açıortayları)',
 metin='Şekilde ABC üçgeninde |AB| = |AC| ve m(BAC) = 40° dir. D noktası [AC] üzerinde, E noktası [AB] üzerindedir; [BD] ve [CE], sırasıyla B ve C köşelerindeki açıların açıortaylarıdır ve K noktasında kesişmektedir. Şekil ölçekli değildir.\nBuna göre, x = m(BKC) kaç derecedir?',
 dogru=110,yan=[(35,'Açıortayın ayırdığı yarım taban açısını (35°) x sanmış.','dikkat'),(125,'90° ye yarım taban açısını eklemiş: 90° + 35° = 125°.','bilgi'),(130,'90° ye tepe açısını eklemiş: 90° + 40° = 130°.','bilgi'),(140,'Tepe açısının bütünlerini (180° − 40°) yazmış.','dikkat')],
 istenen='x = m(BKC) açısının ölçüsü.',
 ip=['ABC üçgeninin taban açılarını bul. Açıortaylar bu açıları nasıl böler ve BKC üçgeninde hangi iki açı bilinir?'],
 bilgi=[IKIZ,ACIORTAY],
 ad=[A('Taban açılarını bul','|AB| = |AC| olduğundan B ve C açıları eşittir.','m(ABC) = m(ACB) = (180° − 40°) ÷ 2 = 70°'),A('Açıortayları uygula','Açıortaylar B ve C açılarını ikiye böler.','m(KBC) = m(KCB) = 35°'),A('BKC üçgenini çöz','İç açıların toplamı 180°.','x = 180° − 35° − 35° = 110°')],
 puf='Önce hangi açıların bilindiğini şekle işle, sonra x’in bulunduğu üçgenin diğer iki açısını belirle.',sekil=SK)

# ===== 04 · çevre, kenarortay · orta · hikâyeli =====
kartlab(4,'Çevrelerden kenarortay','İkizkenar üçgende taban orta noktasına çizilen kenarortay üçgeni iki eş parçaya ayırır; iki çevre arasındaki ilişkiden ortak kenarın uzunluğu bulunur.','İki çevrenin farkını sonuç sanmak; yarım çevreyi sonuç sanmak; ortak kenarı iki kez saymak.','orta',3,'ge-ik2-kenar','İkizkenar üçgende kenar ve çevre',kalip='hikâyeli')
AB4,BD4=25,7; AD4=24; assert AB4**2==BD4**2+AD4**2; C64=2*(AB4+BD4); C56=AB4+BD4+AD4; assert (C64,C56)==(64,56) and AB4+BD4==32
s4=.17; B4=(-BD4*s4,0); C4=(BD4*s4,0); A4=(0,AD4*s4); D4=(0,0)
f=F(); f.poly([A4,B4,C4]); f.line(A4,D4); f.tick(A4,B4); f.tick(A4,C4); f.tick(B4,D4,2); f.tick(D4,C4,2)
vlabs(f,[('A',A4),('B',B4),('C',C4)],(0,2)); f.vl('D',D4,(0,-1),.3)
f.node((0,-.75),'Çevre$(ABC)=64$ cm'); f.node((0,-1.3),'Çevre$(ABD)=56$ cm')
SK=f.svg()
assert sorted([8,24,28,32,56])==sorted([C64-C56,AD4,C56//2,AB4+BD4,C56])
q('0004',tipId='ge-ik2-kenar',tip='İkizkenar üçgende kenar ve çevre',z='orta',kalip='hikâyeli',alt='Yelken ve Dikiş',kaz='İki çevre bilgisinden ikizkenar üçgenin kenarortay uzunluğunu bulur.',
 kart='K-GIKI-04 (çevrelerden kenarortay)',
 metin='İkizkenar üçgen biçimindeki bir yelken bezi, tepe noktasından taban ortasına çekilen [AD] dikişiyle iki parçaya ayrılmıştır; |AB| = |AC| dir ve D noktası [BC] nin orta noktasıdır. Şekilde yelkenin tamamının çevresi 64 cm, ABD parçasının çevresi 56 cm olarak verilmiştir. Şekil ölçekli değildir.\nBuna göre, dikişin uzunluğu olan |AD| kaç cm’dir?',
 dogru=24,yan=[(8,'İki çevrenin farkını (64 − 56 = 8) sonuç sanmış.','dikkat'),(32,'|AB| + |BD| = 32 toplamını bulup |AD| ye geçmemiş.','dikkat'),(28,'ABD çevresinin yarısını (56 ÷ 2) |AD| sanmış.','bilgi'),(56,'ABD parçasının çevresini dikişin uzunluğu sanmış.','dikkat')],
 istenen='|AD| uzunluğu (cm).',
 ip=['ABC nin çevresini hangi uzunluklarla yazarsın? ABD nin çevresini aynı uzunluklarla yazınca ne olur?'],
 bilgi=[IKIZ,KENARORTAY],
 ad=[A('ABC çevresini yaz','|AB| = |AC| ve |BD| = |DC| olduğundan çevre iki katıdır.','2(|AB| + |BD|) = 64 → |AB| + |BD| = 32'),A('ABD çevresini yaz','ABD üçgeninin üç kenarı.','|AB| + |BD| + |AD| = 56'),A('|AD| yi bul','Bilinen toplamı yerine koy.','32 + |AD| = 56 → |AD| = 24')],
 puf='Çevre problemlerinde iki üçgenin ortak ve ortak olmayan kenarlarını ayrı ayrı listele.',sekil=SK)

# ===== 05 · iç noktadan dikmeler · orta =====
kartlab(5,'Taban üzerindeki noktadan dikmeler','Taban üzerinde alınan bir noktadan eş kenarlara inen dikmeler, alanlar yardımıyla bir yüksekliğe bağlanır; nokta kaydırılsa da toplam değişmez.','Tepe yüksekliğini sonuç sanmak; alanı 2 ile çarpmayı unutmak; yarım tabanı yazmak.','orta',4,'ge-ik2-dikme','İkizkenar üçgende dikmeler ve alan')
AB5,BC5=20,24; h5=sqrt(AB5**2-(BC5/2)**2); assert abs(h5-16)<1e-12; al5=BC5*16/2; top5=2*al5/AB5; assert abs(top5-19.2)<1e-9 and abs(al5-192)<1e-9
s5=.25; B5=(-12*s5,0); C5=(12*s5,0); A5=(0,16*s5); D5=(-5*s5,0)
E5=ayak(D5,A5,B5); F5=ayak(D5,A5,C5)
assert abs((dist(D5,E5)+dist(D5,F5))/s5-19.2)<1e-9
f=F(); f.poly([A5,B5,C5]); f.line(D5,E5); f.line(D5,F5); f.dik(E5,D5,A5,.17); f.dik(F5,D5,A5,.17); f.tick(A5,B5); f.tick(A5,C5)
f.sl('$20$',A5,B5,C5,.35); dim(f,B5,C5,'$24$',(0,-1),.6)
vlabs(f,[('A',A5),('B',B5),('C',C5)],cen([A5,B5,C5])); f.vl('D',D5,(0,-1),.3); f.vl('E',E5,(-1,.3),.3); f.vl('F',F5,(1,.3),.3)
SK=f.svg()
assert sorted([9.6,12,16,19.2,24])==sorted([al5/AB5,BC5/2,h5,top5,BC5])
q('0005',tipId='ge-ik2-dikme',tip='İkizkenar üçgende dikmeler ve alan',z='orta',alt='Taban Noktasından Dikmeler',kaz='Taban üzerindeki bir noktadan eş kenarlara inen dikmelerin toplamını alan ilişkisiyle bulur.',
 kart='K-GIKI-05 (taban noktasından dikmeler)',
 metin='Şekilde ABC üçgeninde |AB| = |AC| = 20 cm ve |BC| = 24 cm dir. [BC] üzerindeki bir D noktasından [AB] ye ve [AC] ye çizilen dikmelerin ayakları sırasıyla E ve F noktalarıdır. Şekil ölçekli değildir.\nBuna göre, |DE| + |DF| toplamı kaç cm’dir?',
 dogru=19.2,yan=[(9.6,'Alanı (192) eş kenara bölmüş, 2 ile çarpmayı unutmuş: 192 ÷ 20 = 9,6.','islem'),(12,'Yarım tabanı (12) toplam sanmış.','dikkat'),(16,'Tepeden tabana inen yüksekliği (16) sonuç sanmış.','dikkat'),(24,'Taban uzunluğunu (24) sonuç sanmış.','dikkat')],
 istenen='|DE| + |DF| toplamı (cm).',
 ip=['[DE] ve [DF] hangi üçgenlerin yükseklikleridir? Bu üçgenlerin tabanları ve ABC ile ilişkisi nedir?'],
 bilgi=[IKIZ,ALAN,PIS],
 ad=[A('Yüksekliği bul','[BC] ye ait yükseklik tabanı ortalar: yarım taban 12.','h² = 20² − 12² = 256 → h = 16'),A('Alanı hesapla','Taban 24, yükseklik 16.','Alan(ABC) = 24 × 16 ÷ 2 = 192'),A('Alanı parçalara ayır','ABC = ABD + ACD; bu üçgenlerin yükseklikleri [DE] ve [DF] dir.','20 × |DE| ÷ 2 + 20 × |DF| ÷ 2 = 192'),A('Toplamı bul','Ortak çarpanı dışarı al.','20 × (|DE| + |DF|) = 384 → |DE| + |DF| = 19,2')],
 puf='Sorulan toplamın D noktasının yerine bağlı olup olmadığını, D yi başka bir yere taşıyarak düşün.',sekil=SK)

# ===== 06 · içte eşkenar · orta =====
kartlab(6,'İkizkenar üçgenin içinde eşkenar üçgen','Eşkenar üçgenin açıları 60° dir; taban açısıyla farkı küçük bir açı verir. Ortak köşeden çizilen doğru, eş üçgenler yüzünden açıyı ikiye böler.','Eşkenarın açısını taban açısına eklemek; [AD] nin tepe açısını böldüğünü görememek; ADB yi ABD sanmak.','orta',4,'ge-ik2-esk','İkizkenar ve eşkenar üçgen birlikte')
L6=7; B6=(-L6*sin(radians(20)),0); C6=(L6*sin(radians(20)),0); A6=(0,L6*cos(radians(20))); D6=(0,dist(B6,C6)*sin(radians(60)))
assert abs(dist(D6,B6)-dist(B6,C6))<1e-9 and abs(dist(D6,C6)-dist(B6,C6))<1e-9 and D6[1]<A6[1]
assert abs(ang(D6,A6,B6)-150)<1e-9 and abs(ang(B6,A6,D6)-10)<1e-9 and abs(ang(A6,B6,D6)-20)<1e-9
f=F(); f.poly([A6,B6,C6]); f.line(B6,D6); f.line(C6,D6); f.line(A6,D6); f.tick(A6,B6); f.tick(A6,C6); f.tick(B6,C6,2); f.tick(B6,D6,2); f.tick(C6,D6,2)
f.arc(B6,C6,A6,1.0,'$70^\\circ$',1.55); f.arc(D6,A6,B6,.6,'$x$',.35)
vlabs(f,[('A',A6),('B',B6),('C',C6)],cen([A6,B6,C6])); f.vl('D',D6,(1,-.4),.3)
SK=f.svg()
assert sorted([10,20,130,140,150])==sorted([70-60,20,70+60,180-40,150])
q('0006',tipId='ge-ik2-esk',tip='İkizkenar ve eşkenar üçgen birlikte',z='orta',alt='İçte Eşkenar Üçgen',kaz='İkizkenar üçgenin içine kurulan eşkenar üçgenle açıları zincirleme hesaplayıp bir açıyı bulur.',
 kart='K-GIKI-06 (içte eşkenar üçgen)',
 metin='Şekilde ABC üçgeninde |AB| = |AC| ve m(ABC) = 70° dir. Üçgenin iç bölgesindeki D noktası, BCD üçgeni eşkenar olacak biçimde alınmış ve [AD] doğru parçası çizilmiştir. Şekilde eşit çentikli doğru parçalarının uzunlukları eşittir; şekil ölçekli değildir.\nBuna göre, x = m(ADB) kaç derecedir?',
 dogru=150,yan=[(10,'m(ABD) = 70° − 60° = 10° yi bulup bırakmış.','dikkat'),(20,'m(BAD) = 20° yi bulup x sanmış.','dikkat'),(130,'Eşkenarın 60° sini taban açısına eklemiş: 70° + 60° = 130°.','bilgi'),(140,'Tepe açısının bütünlerini (180° − 40°) yazmış.','dikkat')],
 istenen='x = m(ADB) açısının ölçüsü.',
 ip=['ABC nin tepe açısını bul; eşkenar üçgenin açısı taban açısıyla birlikte ABD üçgeninin hangi açısını verir? [AD] için ne söyleyebilirsin?'],
 bilgi=[IKIZ,ESK],
 ad=[A('Tepe açısını bul','|AB| = |AC| olduğundan taban açıları eşittir.','m(BAC) = 180° − 2 × 70° = 40°'),A('ABD açısını bul','BCD eşkenar olduğundan m(DBC) = 60°.','m(ABD) = 70° − 60° = 10°'),A('[AD] nin işlevi','|AB| = |AC|, |DB| = |DC| ve [AD] ortaktır; ABD ve ACD üçgenleri eştir, bu yüzden [AD] tepe açısını ikiye böler.','m(BAD) = 40° ÷ 2 = 20°'),A('x’i bul','ABD üçgeninin iç açıları toplamı.','x = 180° − 10° − 20° = 150°')],
 puf='Şekildeki eşit çentikli parçaları ve verilen açıları listeleyip, hangi iki üçgenin ortak bir kenar paylaştığını bul.',sekil=SK)

# ===== 07 · ikizkenar dik üçgen · orta · hikâyeli =====
kartlab(7,'İkizkenar dik üçgende yükseklik ve alan','İkizkenar dik üçgende dar açılar 45° dir; hipotenüse inen yükseklik üçgeni iki küçük ikizkenar dik üçgene böler.','Yüksekliği dik kenar sanmak; ÷ 2 yi unutmak; hipotenüsü yüksekliğe eşit almak.','orta',3,'ge-ik2-dik','İkizkenar dik üçgen',kalip='hikâyeli')
h7=6; hip7=2*h7; al7=hip7*h7//2; assert al7==36 and 6*6//2==18 and hip7*h7==72 and hip7**2==144 and 6*3//2==9
s7_=.4; A7_=(0,h7*s7_); B7_=(-h7*s7_,0); C7_=(h7*s7_,0); H7_=(0,0)
assert abs(ang(A7_,B7_,C7_)-90)<1e-9 and abs(dist(A7_,B7_)-dist(A7_,C7_))<1e-9
f=F(); f.poly([A7_,B7_,C7_]); f.line(A7_,H7_); f.dik(A7_,B7_,C7_,.22); f.dik(H7_,A7_,C7_,.2); f.tick(A7_,B7_); f.tick(A7_,C7_); f.node((.3,h7*s7_/2),'$6$')
vlabs(f,[('A',A7_),('B',B7_),('C',C7_)],(0,1.2)); f.vl('H',H7_,(0,-1),.3)
SK=f.svg()
assert sorted([9,18,36,72,144])==sorted([6*3//2,6*6//2,al7,hip7*h7,hip7**2])
q('0007',tipId='ge-ik2-dik',tip='İkizkenar dik üçgen',z='orta',kalip='hikâyeli',alt='Gönye',kaz='İkizkenar dik üçgende hipotenüse inen yükseklikten alanı bulur.',
 kart='K-GIKI-07 (ikizkenar dik üçgen)',
 metin='Marangoz Ahmet’in ikizkenar dik üçgen biçimindeki gönyesinde dik açının köşesi A, hipotenüsü [BC] dir ve |AB| = |AC| dir. Dik açının köşesinden hipotenüse indirilen [AH] dikmesinin uzunluğu şekilde cm cinsinden verilmiştir. Şekil ölçekli değildir.\nBuna göre, gönyenin alanı kaç cm²’dir?',
 dogru=36,yan=[(9,'Hipotenüsü 6 sanıp yüksekliği 3 almış: 6 × 3 ÷ 2 = 9.','bilgi'),(18,'Dik kenarı 6 cm sanmış: 6 × 6 ÷ 2 = 18.','bilgi'),(72,'Hipotenüs × yükseklik = 12 × 6 = 72 yi vermiş, 2 ye bölmemiş.','islem'),(144,'Hipotenüsün karesini (12²) alan sanmış.','dikkat')],
 istenen='Gönyenin alanı (cm²).',
 ip=['ABH ve ACH üçgenlerinin açıları kaç derecedir? Bu üçgenlerde hangi kenarlar birbirine eşit olur?'],
 bilgi=[IKIZ,DIKACI,ALAN],
 ad=[A('Dar açıları bul','|AB| = |AC| ve m(A) = 90° olduğundan taban açıları eşittir.','m(B) = m(C) = 45°'),A('Küçük üçgenleri incele','ABH üçgeninde H dik, B = 45° olduğundan A açısı da 45° dir; üçgen ikizkenar dik üçgendir. Aynısı ACH için geçerlidir.','|BH| = |AH| = 6 ve |HC| = |AH| = 6'),A('Hipotenüsü yaz','[BC] iki parçanın toplamıdır.','|BC| = 6 + 6 = 12'),A('Alanı hesapla','Taban [BC], yükseklik [AH].','Alan = 12 × 6 ÷ 2 = 36')],
 puf='Hangi uzunluğun taban, hangisinin ona ait yükseklik olduğunu belirleyip alan formülüne yerleştir.',sekil=SK)

# ===== 08 · AD = AE açı zinciri · zor =====
kartlab(8,'Eşit çizgilerle açı zinciri','İkizkenar üçgen içindeki ikinci ikizkenar üçgen ve dış açılar, taban açısı ortadan kalkacak biçimde birleştirilince tek bilinmeyenli bir açı denklemi verir.','Taban açısını sayı sanmak; dış açıyı iç açıyla karıştırmak; ADE yi tepe açısı sanmak.','zor',6,'ge-ik2-zincir','İki ikizkenar üçgende açı zinciri')
L8=4.8; B8=(-L8*sin(radians(40)),0); C8=(L8*sin(radians(40)),0); A8=(0,L8*cos(radians(40)))
dv=rot(sub(B8,A8),30); D8=kesis(A8,add(A8,dv),B8,C8); E8=add(A8,mul(un(sub(C8,A8)),dist(A8,D8)))
assert abs(dist(A8,D8)-dist(A8,E8))<1e-9 and dist(A8,E8)<dist(A8,C8) and abs(ang(A8,B8,D8)-30)<1e-9 and abs(ang(D8,E8,C8)-15)<1e-9
f=F(); f.poly([A8,B8,C8]); f.line(A8,D8); f.line(D8,E8); f.tick(A8,D8,2); f.tick(A8,E8,2)
f.arc(A8,B8,D8,1.0,'$30^\\circ$',1.45); f.arc(D8,E8,C8,.6,'$x$',.95)
vlabs(f,[('A',A8),('B',B8),('C',C8)],cen([A8,B8,C8])); f.vl('D',D8,(0,-1),.3); f.vl('E',E8,(1,.3),.3)
SK=f.svg()
assert sorted([15,30,45,60,75])==sorted([15,30,30+15,2*30,(180-30)//2])
q('0008',tipId='ge-ik2-zincir',tip='İki ikizkenar üçgende açı zinciri',z='zor',alt='Eşit Çizgiler',kaz='İki ikizkenar üçgeni ve dış açıları birlikte kullanarak istenen açıyı bulur.',
 kart='K-GIKI-08 (eşit çizgilerle açı zinciri)',
 metin='Şekilde ABC üçgeninde |AB| = |AC| dir. D noktası [BC] üzerinde, E noktası [AC] üzerindedir ve |AD| = |AE| dir. Şekilde eşit çentikli doğru parçalarının uzunlukları eşittir. m(BAD) = 30° dir. Şekil ölçekli değildir.\nBuna göre, x = m(EDC) kaç derecedir?',
 dogru=15,yan=[(30,'Verilen m(BAD) = 30° yi x sanmış.','dikkat'),(45,'30° ile 15° yi toplamış.','islem'),(60,'Verilen açının iki katını (2 × 30°) almış.','islem'),(75,'(180° − 30°) ÷ 2 = 75° yazmış (ABD yi ikizkenar sanmış).','bilgi')],
 istenen='x = m(EDC) açısının ölçüsü.',
 ip=['m(ABC) = m(ACB) = c diyerek başla. ADC açısını iki ayrı biçimde yazmayı dene: biri bir dış açı, biri iki açının toplamı.'],
 bilgi=[IKIZ,DIS],
 ad=[A('Taban açısını adlandır','|AB| = |AC| olduğundan B ve C açıları eşittir.','m(ABC) = m(ACB) = c'),A('ADC yi dış açıyla yaz','ADC, ABD üçgeninin dış açısıdır.','m(ADC) = c + 30°'),A('AED yi yaz','AED, DEC üçgeninin dış açısıdır.','m(AED) = x + c'),A('ADE üçgenini kullan','|AD| = |AE| olduğundan ADE ikizkenardır.','m(ADE) = m(AED) = x + c'),A('ADC yi bir kez daha yaz','ADC = ADE + EDC.','(x + c) + x = c + 30°'),A('x’i bul','c sadeleşir.','2x = 30° → x = 15°')],
 puf='Bilinmeyen bir açıyı harfle gösterip aynı açıyı iki farklı yoldan yazmak, harfin sadeleşmesini sağlayabilir.',sekil=SK)

# ===== 09 · AB = AC, iki parça · zor =====
kartlab(9,'Tabandaki noktanın uzaklığı','Tabanda bir noktanın köşeye uzaklığı, yükseklik çizilerek iki dik üçgende Pisagor bağıntısıyla bulunur; yüksekliğin kendisi yazılmadan sadeleşir.','Yüksekliği bulmaya çalışıp takılmak; |AD| yi |AB| ye eşit sanmak; |BD| · |DC| yi |AD|² sanmak.','zor',6,'ge-ik2-yardimci','Yardımcı çizimle uzunluk')
AB9,BD9,DC9=13,4,12; BC9=BD9+DC9; h9sq=AB9**2-(BC9/2)**2; DH9=BC9/2-BD9; AD9=sqrt(h9sq+DH9**2); assert abs(AD9-11)<1e-9 and h9sq==105
s9=.3; B9=(-BC9/2*s9,0); C9=(BC9/2*s9,0); A9=(0,sqrt(h9sq)*s9); D9=(B9[0]+BD9*s9,0)
assert abs(dist(A9,B9)/s9-13)<1e-9 and abs(dist(A9,D9)/s9-11)<1e-9
f=F(); f.poly([A9,B9,C9]); f.line(A9,D9); f.tick(A9,B9); f.tick(A9,C9)
f.sl('$13$',A9,B9,C9,.35); f.sl('$4$',B9,D9,A9,.3); f.sl('$12$',D9,C9,A9,.3)
vlabs(f,[('A',A9),('B',B9),('C',C9)],cen([A9,B9,C9])); f.vl('D',D9,(0,-1),.3)
SK=f.svg()
assert sorted([4,8,9,11,13])==sorted([BD9,BC9//2,AB9-BD9,AD9,AB9])
q('0009',tipId='ge-ik2-yardimci',tip='Yardımcı çizimle uzunluk',z='zor',alt='Tabandaki Nokta',kaz='İkizkenar üçgenin tabanındaki bir noktanın tepeye uzaklığını yardımcı yükseklikle bulur.',
 kart='K-GIKI-09 (tabandaki noktanın uzaklığı)',
 metin='Şekilde ABC üçgeninde |AB| = |AC| = 13 cm dir. D noktası [BC] kenarı üzerindedir ve [AD] doğru parçası çizilmiştir. Şekilde |BD| = 4 cm ve |DC| = 12 cm olarak verilmiştir. Şekil ölçekli değildir.\nBuna göre, |AD| kaç cm’dir?',
 dogru=11,yan=[(4,'|BD| = 4 cm yi |AD| sanmış.','dikkat'),(8,'Yarım tabanı (16 ÷ 2 = 8) |AD| sanmış.','dikkat'),(9,'|AB| − |BD| = 13 − 4 = 9 yazmış.','islem'),(13,'|AD| = |AB| yazmış.','bilgi')],
 istenen='|AD| uzunluğu (cm).',
 ip=['A noktasından [BC] ye bir dikme indirsen taban nasıl bölünürdü? Oluşan dik üçgenlerin ortak kenarını düşün.'],
 bilgi=[IKIZ,PIS],
 ad=[A('Yükseklik çiz','A’dan [BC] ye inen dikmenin ayağı H olsun; ikizkenar üçgende H tabanı ortalar.','|BC| = 16 → |BH| = |HC| = 8'),A('ABH ile yüksekliği bul','Dik üçgende Pisagor.','|AH|² = 13² − 8² = 105'),A('D nin yerini belirle','|BD| = 4 olduğundan D, H nin B tarafındadır.','|DH| = 8 − 4 = 4'),A('ADH ile |AD| yi bul','Dik üçgende Pisagor.','|AD|² = 105 + 4² = 121'),A('Sonucu yaz','Karekökü al.','|AD| = 11')],
 puf='Yüksekliğin uzunluğunu doğrudan bulamasan bile karesi bir sonraki işlemde yeniden kullanılabilir.',sekil=SK)

# ===== 10 · uzantı ve paralel çizimi · zor =====
kartlab(10,'Eşit uzunluklu uzantı','İkizkenar üçgende bir kenar boyunca ve uzantısında eşit uzunluklar alınınca doğru parçası tabanı bölen noktanın yeri, yardımcı paralel ve eş üçgenlerle bulunur.','Oranı ters kurmak; F yi orta nokta ya da BC nin yarısı sanmak; yardımcı çizimi yarıda bırakmak.','zor',6,'ge-ik2-yardimci','Yardımcı çizimle uzunluk')
AB10,BC10,BD10,CE10=10,12,5,5; h10=sqrt(AB10**2-(BC10/2)**2); assert abs(h10-8)<1e-12
s10=.4; B10=(-6*s10,0); C10=(6*s10,0); A10=(0,8*s10); D10=lerp(B10,A10,BD10/AB10); E10=add(C10,mul(sub(C10,A10),CE10/AB10)); F10=kesis(D10,E10,B10,C10)
assert abs((F10[0]-B10[0])/s10-9)<1e-9 and abs(dist(D10,F10)-dist(F10,E10))<1e-9 and abs(dist(B10,D10)/s10-5)<1e-9 and abs(dist(C10,E10)/s10-5)<1e-9
f=F(); f.poly([A10,B10,C10]); f.line(C10,E10,'dashed'); f.line(D10,E10)
ic=cen([A10,B10,C10]); f.sl('$15$',A10,D10,C10,.35) if False else None
dim(f,B10,A10,'$10$',(-.8,.6),.8); f.sl('$5$',B10,D10,(-9,0),.3); f.sl('$5$',C10,E10,B10,.3); f.node((0,-.35),'$12$')
vlabs(f,[('A',A10),('B',B10),('C',C10)],ic); f.vl('D',D10,(1,.3),.3); f.vl('E',E10,(1,-.4),.3); f.vl('F',F10,(-.3,1),.3)
SK=f.svg()
assert sorted([3,6,9,10,12])==sorted([BC10-9,BC10//2,9,AB10,BC10])
q('0010',tipId='ge-ik2-yardimci',tip='Yardımcı çizimle uzunluk',z='zor',alt='Uzantı ve Kesen',kaz='İkizkenar üçgende yardımcı paralel ve eş üçgenlerle taban üzerindeki bir uzaklığı bulur.',
 kart='K-GIKI-10 (eşit uzunluklu uzantı)',
 metin='ABC üçgeninde |AB| = |AC| = 10 cm ve |BC| = 12 cm dir. D noktası [AB] üzerinde, E noktası ise [AC] kenarının C yönündeki uzantısı üzerindedir ve |BD| = |CE| = 5 cm dir. [DE] doğru parçası [BC] yi F noktasında kesmektedir. Şekil ölçekli değildir.\nBuna göre, |BF| kaç cm’dir?',
 dogru=9,yan=[(3,'|BF| yerine |FC| = 3 cm yi bulmuş.','dikkat'),(6,'F noktasını [BC] nin orta noktası sanmış.','bilgi'),(10,'|BF| = |AB| yazmış.','bilgi'),(12,'|BF| yerine |BC| yi vermiş.','dikkat')],
 istenen='|BF| uzunluğu (cm).',
 ip=['Eşit olan |BD| ve |CE| uzunluklarını bir paralel yardımıyla yan yana getirebilir misin?'],
 bilgi=[IKIZ,PAR,ESLIK],
 ad=[A('Yardımcı paralel çiz','D’den [AC] ye paralel çizilen doğru [BC] yi G’de kessin.','[DG] // [AC]'),A('BDG üçgenini incele','Yöndeş açılar eşit olduğundan BDG, ABC ye benzer ve ikizkenardır.','|BG| / 12 = 5 / 10 → |BG| = 6 ve |DG| = |BD| = 5'),A('Eş üçgenleri bul','[DG] // [CE] olduğundan ters açılar eşittir; F deki karşı açılar eşittir; |DG| = |CE| = 5.','DGF ≅ ECF'),A('GF yi bul','Eş üçgenlerde karşılıklı kenarlar eşittir.','|GF| = |FC| ve |GC| = 12 − 6 = 6 → |GF| = 3'),A('|BF| yi yaz','|BF| = |BG| + |GF|.','|BF| = 6 + 3 = 9')],
 puf='Yardımcı çizim sonrası ortaya çıkan eşit uzunlukları ve eşit açıları şekle işleyip hangi üçgenlerin eş ya da benzer olduğuna bak.',sekil=SK)
bitir_geo('ikizkenariki','İkizkenar Üçgen')
