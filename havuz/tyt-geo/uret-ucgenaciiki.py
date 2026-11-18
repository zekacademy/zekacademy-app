"""TYT Geometri · Üçgende Açılar · ikinci paket (kardeş yok, ipucu 1). Koordinatlar hesaplanır; cevap ve çeldirici değerleri assert edilir."""
import sys,os,math,json
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
HV=os.path.join(GD,'..')
from math import sin,cos,tan,radians,degrees,atan2,sqrt,pi
TIPK={}   # tipId -> uygulama konu anahtarı
def konu(k,ad): P.k=k; P.konu_adi=ad; H.KONU=ad

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
    def arc(s,V,a,b,r,lab=None,lr=None,st='',lt=.5):
        a1=degrees(atan2(a[1]-V[1],a[0]-V[0])); a2=degrees(atan2(b[1]-V[1],b[0]-V[0])); d=(a2-a1+180)%360-180
        s.o.append(f'\\draw[{st}] ({V[0]+r*cos(radians(a1)):.3f},{V[1]+r*sin(radians(a1)):.3f}) arc[start angle={a1:.2f},delta angle={d:.2f},radius={r}];')
        if lab: m=radians(a1+d*lt); s.node((V[0]+lr*cos(m),V[1]+lr*sin(m)),lab)
    def dik(s,V,a,b,z=.22): u=un(sub(a,V)); v=un(sub(b,V)); s.o.append(f'\\draw {pt(add(V,mul(u,z)))} -- {pt(add(add(V,mul(u,z)),mul(v,z)))} -- {pt(add(V,mul(v,z)))};')
    def tick(s,p,q_,n=1,h=.09):
        m=mid(p,q_); e=un(sub(q_,p)); nn=(-e[1],e[0])
        for i in range(n):
            c=add(m,mul(e,(i-(n-1)/2)*.1)); s.line(add(c,mul(nn,h)),sub(c,mul(nn,h)))
    def par(s,p,q_):
        m=mid(p,q_); e=un(sub(q_,p)); s.o.append(f'\\draw[-{{Stealth[length=1.9mm,width=1.7mm]}}] {pt(sub(m,mul(e,.07)))} -- {pt(add(m,mul(e,.07)))};')

    def olcu(s,p,q_,t,off=.4,g=None,st='thin'):
        e=un(sub(q_,p)); n=(-e[1],e[0]); sg=1 if off>0 else -1
        P1=add(p,mul(n,off)); Q1=add(q_,mul(n,off)); M=mid(P1,Q1)
        w=.115*len(t.replace('$','').replace('\\','').replace('^','').replace('{','').replace('}',''))+.12
        if g is None: g=.5*(w*abs(e[0])+.32*abs(e[1]))+.07
        L=dist(p,q_); g=min(g,L/2-.1); ar='{Stealth[length=1.7mm,width=1.4mm]}'
        s.o.append(f'\\draw[-{ar},{st}] {pt(sub(M,mul(e,g)))} -- {pt(P1)};')
        s.o.append(f'\\draw[-{ar},{st}] {pt(add(M,mul(e,g)))} -- {pt(Q1)};')
        s.node(M,t)
    def eslik(s,V,a,b,r,n=1,lab=None,lr=None,lt=.5):
        """yay + (n) eş açı çentiği; lab verilirse etiket (lt: yay boyunca konum 0..1)"""
        a1=degrees(atan2(a[1]-V[1],a[0]-V[0])); a2=degrees(atan2(b[1]-V[1],b[0]-V[0])); d=(a2-a1+180)%360-180
        s.o.append(f'\\draw ({V[0]+r*cos(radians(a1)):.3f},{V[1]+r*sin(radians(a1)):.3f}) arc[start angle={a1:.2f},delta angle={d:.2f},radius={r}];')
        m=radians(a1+d/2); u=(cos(m),sin(m)); tg=(-u[1],u[0])
        for i in range(n):
            c=add((V[0]+r*u[0],V[1]+r*u[1]),mul(tg,(i-(n-1)/2)*.1)); s.line(add(c,mul(u,.09)),sub(c,mul(u,.09)))
        if lab: mm=radians(a1+d*lt); s.node((V[0]+lr*cos(mm),V[1]+lr*sin(mm)),lab)
    def body(s): return '\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'+'\n'.join(s.o)+'\n\\end{tikzpicture}'
    def svg(s): return tikz_svg(s.body())
KY='ÖSYM 2018–2026 TYT Geometri soruları (yalnız mantık) · MEB 9–10. sınıf geometri'
def kartla(id,alt,fikir,tuzak,z,adim,tipId,tip,kalip='şekilli'):
    kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY); TIPK[tipId]=P.k
def q(no,ad,kalip='şekilli',**k): mk(P,no,ad=ad,adim=len(ad),kalip=kalip,**k)
def pol(deg,r,o=(0,0)): return (o[0]+r*cos(radians(deg)),o[1]+r*sin(radians(deg)))
def inter(p,d,q_,e):
    # p+t*d = q_+s*e
    det=d[0]*(-e[1])-d[1]*(-e[0]); t=((q_[0]-p[0])*(-e[1])-(q_[1]-p[1])*(-e[0]))/det
    return (p[0]+t*d[0],p[1]+t*d[1])
def bit(onek,adi,konukey):
    for qq in P.ANA: qq['kardes']=None
    P.yaz(os.path.join(GD,f'{onek}-1.json'),f'/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/ucgiki/bos-{onek}.json')
    tipler={}
    for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=TIPK[c['tipId']]))['kartlar'].append(c['id'])
    json.dump(dict(konu=adi,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 TYT Geometri çıkmış soruları (yalnız mantık), MEB 9–10. sınıf geometri müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar',f'{onek}.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler),'soru',len(P.ANA))
def tri(a,b,c,L):
    """A,B,C köşe açıları (derece); BC tabanı yatay, uzunluk L. (A,B,C) döndürür."""
    assert abs(a+b+c-180)<1e-9
    AB=L*sin(radians(c))/sin(radians(a)); return (AB*cos(radians(b)),AB*sin(radians(b))),(0.0,0.0),(float(L),0.0)
def bis(V,P1,P2):
    u=un(sub(P1,V)); v=un(sub(P2,V)); return un(add(u,v))
P=Parti('ucgenaciiki','Üçgende Açılar','geo|Üçgende Açılar',ders='TYT Geometri',idon='tytgeo')
IC=B('Üçgenin iç açıları','bir üçgenin iç açılarının ölçüleri toplamı 180°’dir. Örnek: iki açısı 35° ve 85° olan üçgenin üçüncü açısı 60°’dir')
DIS=B('Dış açı','üçgenin bir dış açısı, kendisine komşu olmayan iki iç açının toplamına eşittir; komşu iç açıyla toplamı 180° dir. Örnek: iç açıları 45° ve 65° olan iki köşenin karşısındaki dış açı 110° dir')
AOR=B('Açıortay','bir açıyı iki eş açıya ayıran ışındır. Örnek: 70° lik bir açının açıortayı onu 35° + 35° ye ayırır')
def foot(p,a,b):
    e=un(sub(b,a)); t=(p[0]-a[0])*e[0]+(p[1]-a[1])*e[1]; return add(a,mul(e,t))
def ray_hit(V,d,a,b):
    """V+t*d ile (a,b) doğrusunun kesişimi"""
    return inter(V,d,a,sub(b,a))
KENAR=B('Açı–kenar bağıntısı','bir üçgende büyük açının karşısındaki kenar büyüktür, eşit açıların karşısındaki kenarlar eşittir. Örnek: açıları 30°, 50° ve 100° olan üçgende en uzun kenar 100° lik açının karşısındadır')
PAR=B('Paralel doğrular ve kesen','iki paralel doğruyu bir kesen kesince ters açılar (iç ters ve dış ters) eşit olur. Örnek: d₁ // d₂ ve kesenin d₁ ile yaptığı sol alt açı 40° ise d₂ ile yaptığı sağ üst açı da 40° dir')
YUK=B('Yükseklik ve açıortay','yükseklik bir köşeden karşı kenara inen dikmedir, kenarla 90° lik açı yapar; açıortay köşedeki açıyı iki eş açıya ayırır. Örnek: 80° lik açının açıortayı onu 40° + 40° ye ayırır, yüksekliği ise bir dik üçgen oluşturur')
DISTOP=B('Dış açıların toplamı','bir üçgenin her köşesinde bir dış açı alındığında (kenarlar aynı yönde uzatılarak) üç dış açının toplamı 360° dir; her dış açı komşu iç açıyla 180° e tamamlanır. Örnek: dış açıları 100°, 120° ve 140° olan üçgenin iç açıları 80°, 60° ve 40° dır')
EKIZ=B('Eşkenar ve ikizkenar üçgen','eşkenar üçgenin üç açısı 60° dir; ikizkenar üçgende eşit kenarların karşısındaki açılar eşittir. Örnek: tepe açısı 100° olan ikizkenar üçgenin taban açıları 40° ar derecedir')
KATL2=B('Katlama (simetri)','katlanınca çakışan noktalar kat izine göre simetriktir; katlama açıları ve uzunlukları değiştirmez. Örnek: katlanınca çakışan iki açının ölçüleri eşittir')
DIKL=B('Dörtgenin açıları','dörtgenin iç açılarının toplamı 360° dir; iki karşılıklı köşesi dik olan dörtgenin diğer iki açısının toplamı 180° dir. Örnek: üç açısı 90°, 80° ve 100° olan dörtgenin dördüncü açısı 90° dir')
GEN='Şekil ölçekli değildir.'

# =================== 01 · açı–kenar sıralaması · kolay · hikâyeli ===================
konu('geo|Üçgende Açılar','Üçgende Açılar')
kartla('K-GUZ-01','Açılardan kenar sıralaması','Verilen iki açıdan üçüncü bulunur; açıların büyüklük sırası karşılarındaki kenarların büyüklük sırasını verir.','Üçüncü açıyı hesaplamadan sıralama yapmak; kenarı komşu açıyla eşleştirmek.','kolay',3,'ge-ui-kenar','Açı–kenar bağıntısı',kalip='hikâyeli')
A1,B1,C1=tri(60,50,70,5.4)
assert abs(ang(A1,B1,C1)-60)<1e-9 and abs(ang(B1,A1,C1)-50)<1e-9 and abs(ang(C1,A1,B1)-70)<1e-9
assert dist(A1,C1)<dist(B1,C1)<dist(A1,B1)
f=F(); f.poly([A1,B1,C1]); f.arc(B1,C1,A1,.8,'$50^\\circ$',1.45); f.arc(C1,A1,B1,.8,'$70^\\circ$',1.45)
f.vl('A',A1,(0,1),.3); f.vl('B',B1,(-1,-.6),.3); f.vl('C',C1,(1,-.6),.3)
SK=f.svg()
S1=['|AB| < |AC| < |BC|','|BC| < |AC| < |AB|','|AC| < |AB| < |BC|','|BC| < |AB| < |AC|','|AC| < |BC| < |AB|']
q('0001',tipId='ge-ui-kenar',tip='Açı–kenar bağıntısı',z='kolay',alt='Açı–Kenar Sıralaması',kaz='Üçgenin açılarını bulup karşılarındaki kenarların uzunluk sıralamasını belirler.',kalip='hikâyeli',
 kart='K-GUZ-01 (açı–kenar) · B = 50°, C = 70°, kenar sıralaması',
 metin='Üçgen biçimli bir parkın A, B ve C köşelerindeki açılardan ikisinin ölçüsü şekilde verilmiştir: m(ABC) = 50° ve m(ACB) = 70° dir. Parkın kenarlarına kısadan uzuna doğru ayrı ayrı yürüyüş parkuru yapılacaktır. '+GEN+'\nBuna göre, parkın kenar uzunlukları arasındaki sıralama aşağıdakilerden hangisidir?',
 dogru=S1[4],yan=[(S1[0],'Her açıya karşısındaki yerine komşu kenarı eşlemiş (B→[AB], A→[AC], C→[BC]).','dikkat'),(S1[1],'A açısının ölçüsünü hesaplamadan A’yı en küçük açı sanmış.','dikkat'),(S1[2],'A açısını en büyük sanıp onun karşısındaki |BC| yi en uzun yazmış.','dikkat'),(S1[3],'Komşu kenarı öbür yönde eşlemiş (B→[BC], A→[AB], C→[CA]).','dikkat')],
 sira=S1,
 istenen='Kenar uzunluklarının kısadan uzuna sıralaması.',ip=['Üçgenin üç açısını yazdın mı? Hangi açı hangi kenarın karşısında?'],bilgi=[IC,KENAR],
 ad=[A('Üçüncü açıyı bul','İç açıların toplamı 180° olduğundan A açısı hesaplanır.','m(BAC) = 180° − 50° − 70° = 60°'),A('Açıları sırala','Açıların küçükten büyüğe sıralaması bulunur.','50° < 60° < 70° → B < A < C'),A('Karşı kenarlara geç','Her açının karşısındaki kenar yazılır: B nin karşısı [AC], A nın karşısı [BC], C nin karşısı [AB].','|AC| < |BC| < |AB|')],
 puf='Önce üçüncü açıyı bul, sonra her açının karşısındaki kenarı eşleştir.',sekil=SK)

# =================== 02 · paralel doğrular arası üçgen · kolay ===================
kartla('K-GUZ-02','Paralel doğrular arasında üçgen','Paralel doğrular ve kesenlerle ters açılar eşit olur; üçgenin iki açısı belli olunca üçüncüsü iç açı toplamıyla bulunur.','Ters açıları yanlış eşleştirmek; verilen açıları üçgenin iç açısı sanıp 180° ten çıkarmamak.','kolay',3,'ge-ui-paralel','Paralel doğrular arasında üçgen ve kırık çizgi')
Hh=2.6; A2=(2.2,Hh); B2=(A2[0]-Hh/tan(radians(52)),0); C2=(A2[0]+Hh/tan(radians(63)),0)
assert abs(ang(B2,A2,C2)-52)<1e-9 and abs(ang(C2,A2,B2)-63)<1e-9 and abs(ang(A2,B2,C2)-65)<1e-9
f=F(); f.line((-1.2,Hh),(5.2,Hh)); f.line((-1.2,0),(5.2,0)); f.line(A2,B2); f.line(A2,C2)
f.par((4.5,Hh),(4.9,Hh)); f.par((4.5,0),(4.9,0))
f.arc(A2,(A2[0]-1,Hh),B2,.55,'$52^\\circ$',1.15,lt=.5); f.arc(A2,(A2[0]+1,Hh),C2,.55,'$63^\\circ$',1.15)
f.arc(A2,B2,C2,.45,'$x$',.95)
f.node((-1.55,Hh),'$d_1$'); f.node((-1.55,0),'$d_2$')
f.vl('A',A2,(0,1),.3); f.vl('B',B2,(-1,-.5),.3); f.vl('C',C2,(1,-.5),.3)
SK=f.svg()
q('0002',tipId='ge-ui-paralel',tip='Paralel doğrular arasında üçgen ve kırık çizgi',z='kolay',alt='Paralel Doğrular Arası Üçgen',kaz='Paralel doğrular arasındaki ters açıları kullanarak üçgenin bilinmeyen açısını bulur.',
 kart='K-GUZ-02 (paralel) · 52° ve 63°, tepe açısı',
 metin='Şekilde d₁ // d₂, A noktası d₁ üzerinde, B ve C noktaları d₂ üzerindedir. [AB] ile d₁ nin sol yönü arasındaki açı 52°, [AC] ile d₁ nin sağ yönü arasındaki açı 63° dir. '+GEN+'\nBuna göre, m(BAC) = x kaç derecedir?',
 dogru=65,yan=[(52,'Yalnız B köşesindeki ters açıyı (52°) yazıp bırakmış.','dikkat'),(63,'Yalnız C köşesindeki ters açıyı (63°) yazıp bırakmış.','dikkat'),(115,'Verilen iki açının toplamını (52° + 63°) x sanmış.','bilgi'),(117,'180° − 63° işlemini yapıp 52° yi kullanmamış.','dikkat')],
 istenen='m(BAC) = x.',ip=['Paralel doğrularda hangi açı çiftleri eşittir?'],bilgi=[PAR,IC],
 ad=[A('Ters açıları yaz','d₁ // d₂ olduğundan A daki açılar, kesenler boyunca B ve C köşelerindeki iç açılara ters açı olarak eşittir.','m(ABC) = 52° · m(ACB) = 63°'),A('İç açı toplamını kullan','ABC üçgeninin iç açılarının toplamı 180° dir.','x + 52° + 63° = 180°'),A('x i bul','115° 180° den çıkarılır.','x = 65°')],
 puf='Paralel doğruların kesenleriyle oluşan eşit açıları üçgenin köşelerine taşı; sonra üçgenin iç açılarını topla.',sekil=SK)

# =================== 03 · yükseklik ve açıortay arası · orta ===================
kartla('K-GUZ-03','Yükseklik ile iç açıortay arasındaki açı','Yükseklik B ve C ile dik üçgen kurar; BAH ve BAD açıları bulunup farkı alınır.','H ile D’nin sırasını karıştırmak; açıortay yerine yüksekliğin açısını vermek; B + C yerine farkı almamak.','orta',4,'ge-ui-yukseklik','Yükseklik ve açıortay',)
B3,C3,A3a=76,44,60
A3,Bp,Cp=tri(A3a,B3,C3,6.6); B3p=Bp; C3p=Cp
H3=foot(A3,B3p,C3p); d3=bis(A3,B3p,C3p); D3=ray_hit(A3,d3,B3p,C3p)
assert abs(ang(A3,B3p,H3)-14)<1e-6 and abs(ang(A3,B3p,D3)-30)<1e-6 and abs(ang(A3,H3,D3)-16)<1e-6 and abs(ang(A3,D3,C3p)-30)<1e-6
assert B3p[0]<H3[0]<D3[0]<C3p[0]
f=F(); f.poly([A3,B3p,C3p]); f.line(A3,H3); f.line(A3,D3); f.dik(H3,A3,C3p,.2)
f.arc(B3p,C3p,A3,.6,'$76^\\circ$',1.1); f.arc(C3p,A3,B3p,.8,'$44^\\circ$',1.4)
f.eslik(A3,B3p,D3,.75,1); f.eslik(A3,D3,C3p,.75,1)
f.arc(A3,H3,D3,1.15,'$x$',2.1)
f.vl('A',A3,(0,1),.3); f.vl('B',B3p,(-1,-.6),.3); f.vl('C',C3p,(1,-.6),.3); f.vl('H',H3,(-.5,-1),.3); f.vl('D',D3,(.6,-1),.3)
SK=f.svg()
q('0003',tipId='ge-ui-yukseklik',tip='Yükseklik ve açıortay',z='orta',alt='Yükseklik ve Açıortay',kaz='Aynı köşeden çizilen yükseklik ve açıortay arasındaki açıyı üçgenin diğer iki açısından hesaplar.',
 kart='K-GUZ-03 (yükseklik–açıortay) · B = 76°, C = 44°, HAD',
 metin='Şekildeki ABC üçgeninde m(ABC) = 76° ve m(ACB) = 44° dir. [AH] ⊥ [BC] olup [AD], BAC açısının açıortayıdır (H, D ∈ [BC]). '+GEN+'\nBuna göre, m(HAD) = x kaç derecedir?',
 dogru=16,yan=[(14,'Yalnız m(BAH) = 90° − 76° = 14° yi bulup bırakmış.','dikkat'),(30,'Açıortayın oluşturduğu açılardan birini (BAD = 30°) x sanmış.','dikkat'),(32,'İki açının farkını (76° − 44°) alıp ikiye bölmeyi unutmuş.','islem'),(46,'m(HAC) = 90° − 44° = 46° yi x sanmış.','dikkat')],
 istenen='m(HAD) = x.',ip=['BAC açısı kaç derece? [AD] bu açıyı hangi iki açıya ayırıyor ve [AH] hangi açıyı oluşturuyor?'],bilgi=[YUK,IC],
 ad=[A('A açısını bul','İç açıların toplamından m(BAC) hesaplanır.','m(BAC) = 180° − 76° − 44° = 60°'),A('Açıortay açısını yaz','[AD] açıortay olduğundan BAC açısını ikiye böler.','m(BAD) = 60° ÷ 2 = 30°'),A('Yükseklikle oluşan açıyı yaz','ABH dik üçgeninde diğer dar açı 90° ye tamamlanır.','m(BAH) = 90° − 76° = 14°'),A('Farkı al','H, B ile D arasında olduğundan x açıları farkıdır.','x = 30° − 14° = 16°')],
 puf='Aynı köşeden çıkan iki doğrunun B kenarıyla yaptığı açıları ayrı ayrı bul; aradaki açı bunların farkıdır.',sekil=SK)

# =================== 04 · diklik merkezi · orta ===================
kartla('K-GUZ-04','İki yüksekliğin kesişimi','C açısı bulunur; D ve E köşelerinde dik açılı CDHE dörtgeninden DHE, ters açıyla AHB bulunur.','180° − A ya da 180° − B yazmak; dörtgenin açı toplamını 180° almak; ters açıyı unutmak.','orta',4,'ge-ui-diklik','İki yüksekliğin kesişimi')
a4,b4=54,66; c4=180-a4-b4; assert c4==60
A4,B4,C4=tri(a4,b4,c4,6.4)
D4=foot(A4,B4,C4); E4=foot(B4,A4,C4)
# kesişim H
H4=inter(A4,sub(D4,A4),B4,sub(E4,B4))
assert abs(ang(H4,A4,B4)-120)<1e-6 and abs((D4[0]-A4[0])*(C4[0]-B4[0])+(D4[1]-A4[1])*(C4[1]-B4[1]))<1e-9
assert dist(D4,B4)>0 and 0<(D4[0]-B4[0])<(C4[0]-B4[0])
f=F(); f.poly([A4,B4,C4]); f.line(A4,D4); f.line(B4,E4); f.dik(D4,A4,C4,.2); f.dik(E4,B4,C4,.2)
f.arc(A4,B4,C4,.7,'$54^\\circ$',1.0,lt=.75); f.arc(B4,C4,A4,.8,'$66^\\circ$',1.5,lt=.8)
f.arc(H4,A4,B4,.4,'$x$',.8)
f.vl('A',A4,(0,1),.3); f.vl('B',B4,(-1,-.6),.3); f.vl('C',C4,(1,-.6),.3); f.vl('D',D4,(0,-1),.3); f.vl('E',E4,(1,.5),.3); f.vl('H',H4,(.9,-.3),.3)
SK=f.svg()
q('0004',tipId='ge-ui-diklik',tip='İki yüksekliğin kesişimi',z='orta',alt='Yüksekliklerin Kesişimi',kaz='Bir üçgende iki yüksekliğin kesişimiyle oluşan açıyı üçgenin açılarından hesaplar.',
 kart='K-GUZ-04 (yükseklikler) · A = 54°, B = 66°, AHB',
 metin='Şekilde ABC üçgeninin [AD] ve [BE] yükseklikleri H noktasında kesişmektedir (D ∈ [BC], E ∈ [AC]). m(BAC) = 54° ve m(ABC) = 66° dir. '+GEN+'\nBuna göre, m(AHB) = x kaç derecedir?',
 dogru=120,yan=[(54,'m(BAC) = 54° yi x sanmış.','dikkat'),(60,'Yalnız C açısını (60°) bulup bırakmış.','dikkat'),(114,'180° − 66° işlemini yapmış.','bilgi'),(126,'180° − 54° işlemini yapmış.','bilgi')],
 istenen='m(AHB) = x.',ip=['C köşesindeki açı kaç derece? CDHE dörtgeninin açılarından hangileri biliniyor?'],bilgi=[IC,DIKL],
 ad=[A('C açısını bul','İç açıların toplamından C hesaplanır.','m(ACB) = 180° − 54° − 66° = 60°'),A('CDHE dörtgenini yaz','D ve E köşelerindeki açılar diktir; dörtgenin iç açıları toplamı 360° dir.','m(DHE) = 360° − 90° − 90° − 60° = 120°'),A('Ters açıyı kullan','AHB ve DHE açıları karşılıklı (ters) açılardır.','x = m(DHE) = 120°')],
 puf='Dik açıları kullanarak oluşan bir dörtgeni bul; ters açıların eşitliğini unutma.',sekil=SK)

# =================== 05 · eşkenar + ikizkenar · orta ===================
kartla('K-GUZ-05','Eşkenar üçgen ve uzantıda ikizkenar','C’deki dış açı 120° olur; ACD ikizkenar üçgeninin taban açıları eşit ve toplamı 60° dir.','Dış açıyı 60° sanmak; tepe açısını ikizkenarın taban açısı yapmak; 180° − 30° yazmak.','orta',3,'ge-ui-ikizkenar','Eşkenar ve ikizkenar üçgen')
Ls=4.0; B5=(0,0); C5=(Ls,0); A5=(Ls/2,Ls*sqrt(3)/2); D5=(2*Ls,0)
assert abs(ang(B5,A5,C5)-60)<1e-9 and abs(dist(C5,D5)-dist(C5,A5))<1e-9 and abs(ang(D5,A5,C5)-30)<1e-6 and abs(ang(C5,A5,D5)-120)<1e-6
f=F(); f.poly([A5,B5,C5]); f.line(C5,D5); f.line(A5,D5)
for p_,q_ in [(A5,B5),(B5,C5),(C5,A5),(C5,D5)]: f.tick(p_,q_,1)
f.arc(D5,A5,C5,.9,'$x$',1.75)
f.vl('A',A5,(0,1),.3); f.vl('B',B5,(-1,-.6),.3); f.vl('C',C5,(.3,-1),.3); f.vl('D',D5,(1,-.6),.3)
SK=f.svg()
q('0005',tipId='ge-ui-ikizkenar',tip='Eşkenar ve ikizkenar üçgen',z='orta',alt='Eşkenar ve İkizkenar Birleşimi',kaz='Eşkenar üçgenin uzantısında oluşan ikizkenar üçgende dış açıyı kullanarak taban açısını bulur.',
 kart='K-GUZ-05 (eşkenar + ikizkenar) · CD = CA, ADC',
 metin='Şekilde ABC bir eşkenar üçgendir. [BC] kenarı C noktasından D noktasına kadar uzatılmış ve |CD| = |CA| olmuştur. Eşit uzunluktaki kenarlar aynı işaretle gösterilmiştir. '+GEN+'\nBuna göre, m(ADC) = x kaç derecedir?',
 dogru=30,yan=[(60,'Eşkenar üçgenin açısını (60°) x sanmış.','dikkat'),(90,'m(BAD) = 60° + 30° = 90° yi x sanmış.','dikkat'),(120,'m(ACD) = 120° dış açısını x sanmış.','dikkat'),(150,'30° yerine 180° − 30° = 150° yazmış.','dikkat')],
 istenen='m(ADC) = x.',ip=['ACD üçgeninde C köşesindeki açı kaç derece ve eşit kenarlar hangi açıların karşısında?'],bilgi=[EKIZ,DIS],
 ad=[A('Dış açıyı bul','ABC eşkenar olduğundan m(ACB) = 60° dir; B, C, D doğrusal olduğundan ACD açısı bunun bütünlerdir.','m(ACD) = 180° − 60° = 120°'),A('İkizkenarı kullan','|CA| = |CD| olduğundan ACD üçgeninde taban açıları eşittir.','m(CAD) = m(ADC) = x'),A('Denklemi kur','ACD üçgeninin iç açıları toplamı 180° dir.','x + x + 120° = 180° → 2x = 60°'),A('x i bul','60° ikiye bölünür.','x = 30°')],
 puf='Doğrusal noktalarda bütünler açıları bul; eşit kenarların karşısındaki açıları eşitle.',sekil=SK)

# =================== 06 · ikizkenar çatı ve açıortay · orta · hikâyeli ===================
kartla('K-GUZ-06','İkizkenar üçgende taban açıortayı','Taban açıları eşittir; açıortay B’yi ikiye böler; BDC üçgeninden B açısı, oradan tepe açısı bulunur.','Taban açılarını eşit saymamak; açıortayın açıyı yarıya bölmesini unutmak; B yerine tepe açısını vermek.','orta',4,'ge-ui-ikizkenar','Eşkenar ve ikizkenar üçgen',kalip='hikâyeli')
A6,B6,C6=tri(84,48,48,5.8)
assert abs(dist(A6,B6)-dist(A6,C6))<1e-9
d6=(cos(radians(24)),sin(radians(24))); D6=ray_hit(B6,d6,A6,C6)
assert abs(ang(D6,B6,C6)-108)<1e-6 and abs(ang(B6,A6,D6)-24)<1e-6 and abs(ang(B6,D6,C6)-24)<1e-6
f=F(); f.poly([A6,B6,C6]); f.line(B6,D6); f.tick(A6,lerp(A6,B6,.6),1); f.tick(A6,lerp(A6,C6,.6),1)
f.eslik(B6,A6,D6,.8,1); f.eslik(B6,D6,C6,.8,1)
f.arc(D6,B6,C6,.5,'$108^\\circ$',1.15,lt=.5)
f.arc(A6,B6,C6,.7,'$x$',1.25)
f.vl('A',A6,(0,1),.3); f.vl('B',B6,(-1,-.6),.3); f.vl('C',C6,(1,-.6),.3); f.vl('D',D6,(1,.5),.3)
SK=f.svg()
q('0006',tipId='ge-ui-ikizkenar',tip='Eşkenar ve ikizkenar üçgen',z='orta',alt='İkizkenar Köprü Kirişi',kaz='İkizkenar üçgende iç açıortayın oluşturduğu açıdan tepe açısını bulur.',kalip='hikâyeli',
 kart='K-GUZ-06 (ikizkenar + açıortay) · BDC = 108°, tepe açısı',
 metin='Bir köprünün çelik kafes sisteminde ABC üçgeni biçimindeki bölümün |AB| = |AC| olup [BD], ABC açısının açıortayıdır (D ∈ [AC]). Mühendisin ölçtüğü m(BDC) = 108° dir. Eşit uzunluktaki kenarlar aynı işaretle gösterilmiştir. '+GEN+'\nBuna göre, köprü bölümünün tepe noktasındaki m(BAC) = x kaç derecedir?',
 dogru=84,yan=[(24,'Yarım taban açısını (ABD) x sanmış.','dikkat'),(48,'Taban açısını (B = C = 48°) x sanmış.','dikkat'),(96,'180° − 84° = 96° yi x sanmış.','dikkat'),(108,'Verilen m(BDC) = 108° yi x sanmış.','dikkat')],
 istenen='m(BAC) = x.',ip=['B ve C açıları arasında nasıl bir ilişki var? BDC üçgeninin açıları B cinsinden nasıl yazılır?'],bilgi=[EKIZ,AOR],
 ad=[A('Taban açılarını yaz','|AB| = |AC| olduğundan taban açıları eşittir; m(ABC) = m(ACB) = 2a olsun. [BD] açıortay olduğundan m(DBC) = a olur.','m(ABC) = m(ACB) = 2a · m(DBC) = a'),A('BDC üçgenini yaz','BDC üçgeninin iç açıları toplamı 180° dir.','a + 2a + 108° = 180°'),A('a yı bul','72° 3 e bölünür.','3a = 72° → a = 24°'),A('Tepe açısını bul','Taban açıları 48° olduğundan A açısı kalan kadardır.','x = 180° − 48° − 48° = 84°')],
 puf='Eşit açılara aynı harfi ver; sonra açıortayın yarıya böldüğü açıyı yarısıyla yaz ve bir üçgenin açılarını topla.',sekil=SK)

# =================== 07 · dış açıların toplamı · orta · hikâyeli ===================
kartla('K-GUZ-07','Dış açılar toplamı 360°','Üç dış açının toplamından x bulunur; istenen köşenin iç açısı 180° den çıkarılarak yazılır.','İç açıyı sormak yerine dış açıyı vermek; toplamı 180° almak; x’i bulup bırakmak.','orta',4,'ge-ui-dis-toplam','Dış açıların toplamı',kalip='hikâyeli')
xx=55; eA,eB,eC=2*xx,xx+60,3*xx-30; assert eA+eB+eC==360 and (eA,eB,eC)==(110,115,135)
iA,iB,iC=180-eA,180-eB,180-eC; assert (iA,iB,iC)==(70,65,45) and 6*xx+30==360
A7,B7,C7=tri(iA,iB,iC,5.2)
rb=un(sub(B7,A7)); rc=un(sub(C7,B7)); ra=un(sub(A7,C7))
Be=add(B7,mul(rb,1.2)); Ce=add(C7,mul(rc,1.1)); Ae=add(A7,mul(ra,1.2))
assert abs(ang(B7,Be,C7)-eB)<1e-6 and abs(ang(C7,Ce,A7)-eC)<1e-6 and abs(ang(A7,Ae,B7)-eA)<1e-6
f=F(); f.poly([A7,B7,C7]); f.line(B7,Be); f.line(C7,Ce); f.line(A7,Ae)
f.arc(B7,Be,C7,.6,'$(x+60)^\\circ$',1.45); f.arc(C7,Ce,A7,.6,'$(3x-30)^\\circ$',1.35); f.arc(A7,Ae,B7,.6,'$(2x)^\\circ$',1.2)
f.vl('A',A7,(1,.25),.35); f.vl('B',B7,(.8,.8),.34); f.vl('C',C7,(.3,-1),.32)
SK=f.svg()
q('0007',tipId='ge-ui-dis-toplam',tip='Dış açıların toplamı',z='orta',alt='Dış Açılar Toplamı',kaz='Üçgenin dış açıları toplamının 360° olduğunu kullanıp bir köşenin iç açısını bulur.',kalip='hikâyeli',
 kart='K-GUZ-07 (dış açılar) · (2x), (x+60), (3x−30)',
 metin='Üçgen biçimli bir yarış pistinde araçlar A → B → C → A yönünde ilerlemektedir. Her köşede araç, geldiği kenarın doğrultusunu uzatarak dönmesi gereken açı şekilde gösterilmiştir: A köşesinde (2x)°, B köşesinde (x + 60)°, C köşesinde (3x − 30)°. '+GEN+'\nBuna göre, pistin B köşesindeki iç açının ölçüsü m(ABC) kaç derecedir?',
 dogru=65,yan=[(45,'İstenen B yerine C köşesinin iç açısını (180° − 135°) bulmuş.','dikkat'),(70,'İstenen B yerine A köşesinin iç açısını (180° − 110°) bulmuş.','dikkat'),(115,'B köşesinin dış açısını (x + 60 = 115°) iç açı sanmış.','dikkat'),(135,'C köşesinin dış açısını (3x − 30 = 135°) yazmış.','dikkat')],
 istenen='m(ABC) iç açısı (derece).',ip=['Verilen açılar iç açı mı, dış açı mı? Üç dış açının toplamı hakkında ne biliyorsun?'],bilgi=[DISTOP,DIS],
 ad=[A('Toplamı yaz','Her kenar aynı yönde uzatıldığından üç dış açının toplamı 360° dir.','(2x) + (x + 60) + (3x − 30) = 360'),A('x i bul','Benzer terimleri topla.','6x + 30 = 360 → x = 55'),A('B nin dış açısını hesapla','B köşesindeki dış açı x + 60 ifadesidir.','x + 60 = 115°'),A('İç açıyı bul','İç ve dış açı birbirini 180° ye tamamlar.','m(ABC) = 180° − 115° = 65°')],
 puf='Dış açılar toplamı sabittir; önce x i bul, sonra iç–dış açıların birbirini 180° ye tamamladığını kullan.',sekil=SK)

# =================== 08 · iki paralel arası kırık patika · zor · hikâyeli ===================
kartla('K-GUZ-08','Paralel doğrular arasında kırık çizgi','Köşelerden d₁ ve d₂ ye paraleller çizilerek ters açılar eşitlenir; bir yöne bakan açıların toplamı karşı yöne bakanların toplamına eşit olur.','Kırık çizgi açılarını doğrudan toplamak; paralel çizmeden sonuç yazmak; bütünler açıyı karıştırmak.','zor',5,'ge-ui-paralel','Paralel doğrular arasında üçgen ve kırık çizgi',kalip='hikâyeli')
Hd=0; dirs=[-50,240,-40]; ls=[2.2,1.8,2.0]
P8=(0.0,0.0); pts=[P8]
for dg,l in zip(dirs,ls): pts.append((pts[-1][0]+l*cos(radians(dg)),pts[-1][1]+l*sin(radians(dg))))
Hd=-pts[-1][1]; P8,E8,F8,Q8=[(p[0],p[1]+Hd) for p in pts]
assert abs(P8[1]-Hd)<1e-9 and abs(Q8[1])<1e-9 and E8[1]>F8[1]>0
assert abs(ang(P8,(P8[0]+1,P8[1]),E8)-50)<1e-6 and abs(ang(E8,P8,F8)-110)<1e-6 and abs(ang(F8,E8,Q8)-100)<1e-6 and abs(ang(Q8,(Q8[0]-1,Q8[1]),F8)-40)<1e-6
assert 50+100==110+40
f=F(); f.line((-1.2,Hd),(3.8,Hd)); f.line((-1.2,0),(3.8,0)); f.line(P8,E8); f.line(E8,F8); f.line(F8,Q8)
f.par((3.2,Hd),(3.6,Hd)); f.par((3.2,0),(3.6,0)); f.node((-1.65,Hd),'$d_1$'); f.node((-1.65,0),'$d_2$')
f.arc(P8,(P8[0]+1,P8[1]),E8,.55,'$50^\\circ$',1.15); f.arc(E8,P8,F8,.5,'$110^\\circ$',1.05); f.arc(F8,E8,Q8,.5,'$x$',1.0); f.arc(Q8,(Q8[0]-1,Q8[1]),F8,.6,'$40^\\circ$',1.25)
f.vl('A',P8,(-.2,1),.3); f.vl('B',E8,(.8,.7),.32); f.vl('C',F8,(-.9,-.3),.32); f.vl('D',Q8,(.4,-1),.3)
SK=f.svg()
q('0008',tipId='ge-ui-paralel',tip='Paralel doğrular arasında üçgen ve kırık çizgi',z='zor',alt='Paralel Yollar ve Patika',kaz='İki paralel doğru arasındaki kırık çizgide yardımcı paraleller çizerek bilinmeyen açıyı bulur.',kalip='hikâyeli',
 kart='K-GUZ-08 (kırık patika) · 50°, 110°, 40°',
 metin='Birbirine paralel d₁ ve d₂ yollarını, A ∈ d₁ ve D ∈ d₂ olmak üzere [AB], [BC] ve [CD] doğru parçalarından oluşan kırık bir patika birleştirmektedir. Şekilde, [AB] ile d₁ nin sağ yönü arasındaki açı 50°, [DC] ile d₂ nin sol yönü arasındaki açı 40° ve m(ABC) = 110° olarak verilmiştir. '+GEN+'\nBuna göre, m(BCD) = x kaç derecedir?',
 dogru=100,yan=[(60,'Açıları doğrudan işleme sokmuş: 110° − 50° = 60°.','bilgi'),(70,'110° − 40° işlemini yapmış.','bilgi'),(80,'C deki iki parçanın ikisini de 40° alıp toplamış: 40° + 40° = 80°.','dikkat'),(90,'50° + 40° = 90° yi x sanmış.','bilgi')],
 istenen='m(BCD) = x.',ip=['Kırık çizginin köşelerinden geçen paraleller hangi açıları eşitler?'],bilgi=[PAR,IC],
 ad=[A('B den paralel çiz','B den d₁ e paralel çizilen doğru ile [BA] arasındaki açı, ters açı olarak 50° dir. Böylece ABC açısının kalan kısmı bulunur.','110° − 50° = 60° (paralel ile [BC] arasındaki açı)'),A('C den paralel çiz','C den de d₁ e paralel çizilir; bu doğru ile [CB] arasındaki açı, B deki 60° ile ters açı olarak eşittir.','60°'),A('D deki açıyı kullan','Aynı paralel ile [CD] arasındaki açı, d₂ ile [DC] arasındaki 40° ye ters açı olarak eşittir.','40°'),A('Toplam','BCD açısı bu iki açının toplamıdır.','x = 60° + 40° = 100°')],
 puf='Kırık çizginin her köşesinden paralel çizerek açıları iki parçaya ayır; ters açıları eşitle ve parçaları topla.',sekil=SK)

# =================== 09 · B köşesi A'ya katlama · zor ===================
kartla('K-GUZ-09','Köşeden köşeye katlama','B köşesi A’ya geldiği için kat izi [AB] nin orta dikmesidir; E noktasında |EA| = |EB| olur ve EAB = ABC bulunur.','|EA| = |EB| eşitliğini görmemek; E noktasındaki açıyı yanlış bölmek; A açısını tamamen EAC sanmak.','orta',4,'ge-ui-katlama','Köşeden köşeye katlama')
B9o,C9o=56,40; A9a=180-B9o-C9o; assert A9a==84 and A9a-B9o==28
A9,Bq,Cq=tri(A9a,B9o,C9o,6.6); B9=Bq; C9=Cq
D9=mid(A9,B9); u=sub(B9,A9); E9=inter(D9,(-u[1],u[0]),B9,sub(C9,B9))
assert abs(dist(E9,A9)-dist(E9,B9))<1e-9 and abs(ang(B9,A9,E9)-56)<1e-6 and abs(ang(A9,B9,E9)-56)<1e-6 and abs(ang(E9,A9,B9)-68)<1e-6
xv=ang(A9,E9,C9); assert abs(xv-28)<1e-6,xv
f=F(); f.poly([A9,B9,C9]); f.line(D9,E9,'dashed'); f.line(A9,E9)
f.arc(B9,C9,A9,.9,'$56^\\circ$',1.6); f.arc(C9,A9,B9,.8,'$40^\\circ$',1.5)
f.arc(A9,E9,C9,.95,'$x$',1.6)
f.vl('A',A9,(0,1),.3); f.vl('B',B9,(-1,-.6),.3); f.vl('C',C9,(1,-.6),.3); f.vl('D',D9,(-1,.4),.3); f.vl('E',E9,(0,-1),.3)
SK=f.svg()
q('0009',tipId='ge-ui-katlama',tip='Köşeden köşeye katlama',z='orta',alt='Üçgen Kâğıdı Katlama',kaz='B köşesi A köşesine gelecek biçimde katlanan üçgende kat izinin orta dikme olduğunu kullanarak açıyı bulur.',kalip='hikâyeli',
 kart='K-GUZ-09 (katlama) · B = 56°, C = 40°, EAC',
 metin='ABC üçgeni biçimindeki bir kâğıt, B köşesi A köşesinin üzerine gelecek biçimde katlanıyor; kat izi [DE] dir (D ∈ [AB], E ∈ [BC]) ve kesikli çizgiyle gösterilmiştir. Kâğıdın B köşesindeki açısı 56°, C köşesindeki açısı 40° dir. [AE] doğru parçası da çizilmiştir. '+GEN+'\nBuna göre, m(EAC) = x kaç derecedir?',
 dogru=28,yan=[(40,'m(ACB) = 40° yi x sanmış.','dikkat'),(56,'m(EAB) = m(ABC) = 56° yi x sanmış.','dikkat'),(84,'Üçüncü açıyı (m(BAC) = 84°) bulup E nin açıyı bölmesini hesaba katmamış.','dikkat'),(112,'m(AEC) = 2 · 56° = 112° yi x sanmış.','dikkat')],
 istenen='m(EAC) = x.',ip=['Kat izi [AB] ye göre nasıl bir doğru?'],bilgi=[KATL2,EKIZ],
 ad=[A('A açısını bul','İç açıların toplamından m(BAC) hesaplanır.','m(BAC) = 180° − 56° − 40° = 84°'),A('Eşit uzaklıkları yaz','Kat izi üzerindeki E noktası A ya ve B ye eşit uzaklıktadır; AEB üçgeni ikizkenardır ve taban açıları eşittir.','|EA| = |EB| → m(EAB) = m(EBA) = 56°'),A('Açıyı çıkar','EAB açısı, BAC açısının bir parçasıdır.','x = 84° − 56° = 28°')],
 puf='Katlamada çakışan noktalara eşit uzaklıktaki noktaları işaretle; ortaya çıkan ikizkenar üçgenin açılarını yaz.',sekil=SK)

# =================== 10 · yükseklik ve açıortay kesişimi · zor ===================
kartla('K-GUZ-10','Yükseklik ile açıortayın kesişimi','F noktasındaki ters açıdan B bulunur; C ile birlikte A hesaplanır.','AFE yi doğrudan B sanmak; 90° − B yazıp A’ya geçmemek; açıortayı yükseklik sanmak.','zor',4,'ge-ui-yukseklik','Yükseklik ve açıortay')
B10o,C10o=52,70; A10a=58; assert 90-B10o//2==64 and 180-B10o-C10o==A10a
A10,Bq,Cq=tri(A10a,B10o,C10o,6.4); B10=Bq; C10=Cq
D10=foot(A10,B10,C10); d10=bis(B10,A10,C10); E10=ray_hit(B10,d10,A10,C10)
F10=inter(A10,sub(D10,A10),B10,sub(E10,B10))
assert abs(ang(F10,A10,E10)-64)<1e-6 and abs(ang(B10,A10,E10)-26)<1e-6 and abs((D10[0]-A10[0])*(C10[0]-B10[0])+(D10[1]-A10[1])*(C10[1]-B10[1]))<1e-9
f=F(); f.poly([A10,B10,C10]); f.line(A10,D10); f.line(B10,E10); f.dik(D10,A10,C10,.2)
f.eslik(B10,A10,E10,.75,1); f.eslik(B10,E10,C10,.75,1)
f.arc(F10,A10,E10,.45,'$64^\\circ$',1.15,lt=.5); f.arc(C10,A10,B10,.8,'$70^\\circ$',1.5)
f.arc(A10,B10,C10,.95,'$x$',.75,lt=.3)
f.vl('A',A10,(0,1),.3); f.vl('B',B10,(-1,-.6),.3); f.vl('C',C10,(1,-.6),.3); f.vl('D',D10,(0,-1),.3); f.vl('E',E10,(1,.5),.3); f.vl('F',F10,(-1,.45),.32)
SK=f.svg()
q('0010',tipId='ge-ui-yukseklik',tip='Yükseklik ve açıortay',z='zor',alt='Yükseklik ve Açıortay Kesişimi',kaz='Yükseklik ile iç açıortayın kesişiminde oluşan açıdan B açısını, oradan A açısını bulur.',
 kart='K-GUZ-10 (yükseklik–açıortay) · AFE = 64°, C = 70°',
 metin='Şekilde ABC üçgeninin [AD] yüksekliği ile [BE] açıortayı F noktasında kesişmektedir (D ∈ [BC], E ∈ [AC]). m(AFE) = 64° ve m(ACB) = 70° dir. Eşit açılar aynı işaretle gösterilmiştir. '+GEN+'\nBuna göre, m(BAC) = x kaç derecedir?',
 dogru=58,yan=[(26,'Yalnız m(ABE) = 26° yi bulup bırakmış.','dikkat'),(38,'Yarım B açısı yerine 90° − 52° = 38° yi x sanmış.','dikkat'),(52,'Yalnız m(ABC) = 52° yi bulup bırakmış.','dikkat'),(64,'Verilen m(AFE) = 64° yi x sanmış.','dikkat')],
 istenen='m(BAC) = x.',ip=['AFE açısıyla eşit olan karşılıklı (ters) açı hangisi? Hangi dik üçgenden B nin yarısı bulunur?'],bilgi=[YUK,IC],
 ad=[A('Ters açıyı yaz','AFE ve BFD açıları ters açılardır.','m(BFD) = 64°'),A('Dik üçgenden B yi bul','BFD üçgeninde D köşesi diktir; B nin yarısı (açıortay) hesaplanır.','m(FBD) = 90° − 64° = 26° → m(ABC) = 2 · 26° = 52°'),A('A yı bul','İç açıların toplamı 180° dir.','x = 180° − 52° − 70° = 58°')],
 puf='Önce ters açıyı belirle; dik açılı üçgenden açıortay açısını bul ve B yi iki katına çıkar.',sekil=SK)

bit('ucgenaciiki','Üçgende Açılar','geo|Üçgende Açılar')
