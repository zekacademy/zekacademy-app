"""TYT Geometri · Doğruda · şekilli sorular (kardeş yok, ipucu 1). Koordinatlar hesaplanır; cevap ve çeldirici değerleri assert edilir."""
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
    P.yaz(os.path.join(GD,f'{onek}-1.json'),f'/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/bos-{onek}.json')
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
P=Parti('dogruaci','Doğruda Açılar','geo|Doğruda Açılar',ders='TYT Geometri',idon='tytgeo')
TUM=B('Tümler ve bütünler açılar','ölçüleri toplamı 90° olan iki açı tümler, 180° olan iki açı bütünlerdir. Bir doğru üzerindeki bitişik açıların toplamı 180°’dir. Örnek: 35° açının tümleri 55°, bütünleri 145°’dir')
PAR=B('Paralel iki doğru ve kesen','paralel iki doğruyu bir kesen kesince ters açılar (iç ters, dış ters) ile yöndeş açılar eşit, kesenin aynı yanındaki iç (ya da dış) açılar bütünlerdir. Örnek: iç ters açılardan biri 70° ise diğeri de 70°’dir')
MKUR=B('Zigzag (M) kuralı','paralel iki doğru arasındaki kırık çizgide, bir yöne bakan açıların toplamı ters yöne bakan açıların toplamına eşittir. Örnek: bir yönde 40° ve 90° varsa, öbür yönde 130° vardır')
ACIORTAY=B('Açıortay','bir açıyı iki eş açıya ayıran ışındır. Örnek: 80° lik bir açının açıortayı onu 40° + 40° ye ayırır')
SAAT=B('Saat ve açı','saatte tam tur 360°’dir: akrep dakikada 0,5°, yelkovan dakikada 6° döner; iki rakam arası 30°’dir. Örnek: 15:00’te yelkovan 12’de, akrep 3’tedir ve aralarında 90° vardır')
KAT=B('Katlanmış şerit','katlayınca üst üste gelen parçaların açıları eşit kalır; kat doğrusu bu eşliğin simetri doğrusudur. Doğru üzerinde bitişik açıların toplamı 180°’dir. Örnek: kenar ile kat doğrusu arasında 100° olan bir köşe katlanınca, kat doğrusuyla yine 100° yapar')

# ============ 01 · Tümler / bütünler / dik açı · kolay ============
konu('geo|Doğruda Açılar','Doğruda Açılar')
kartla('K-GDA-01','Doğru üzerinde bitişik açılar','Doğru üzerindeki bitişik açıların toplamı 180°’dir; dik açı 90° verir. Denklem kurup x bulunur, sonra istenen açı hesaplanır.','x değerini bulup durmak; istenen açının ifadesine geri yazmayı unutmak.','kolay',3,'ge-da-bitisik','Doğru üzerinde bitişik açılar')
x=30; AOC=x+10; COD=90; DOB=2*x-10
assert AOC+COD+DOB==180 and DOB==50 and 3*x+90==180 and x-10==20 and AOC==40 and (AOC+DOB)//2==45
O=(0,0); R=3.3
Ap=(-R,0); Bp=(R,0); Cp=pol(180-55,R); Dp=pol(35,R)
assert abs(ang(O,Cp,Dp)-90)<1e-9
f=F(); f.line(Ap,Bp); f.line(O,Cp); f.line(O,Dp)
f.dik(O,Cp,Dp,.25)
f.arc(O,Ap,Cp,.6,'$(x+10)^\\circ$',1.95); f.arc(O,Dp,Bp,.6,'$(2x-10)^\\circ$',2.05)
f.vl('A',Ap,(-1,-.3),.3); f.vl('B',Bp,(1,-.3),.3); f.vl('C',Cp,(-.5,1),.3); f.vl('D',Dp,(.5,1),.3); f.vl('O',O,(0,-1),.3)
SK=f.svg()
q('0001',tipId='ge-da-bitisik',tip='Doğru üzerinde bitişik açılar',z='kolay',alt='Bitişik Açılar',kaz='Doğru üzerindeki bitişik açıların toplamının 180° olduğunu kullanarak bilinmeyeni ve istenen açıyı bulur.',
 kart='K-GDA-01 (doğru üzerinde bitişik açılar) · dik açı ve iki cebirsel açı',
 metin='Şekilde A, O, B noktaları doğrusaldır, [OC] ⊥ [OD], m(AOC) = (x + 10)° ve m(DOB) = (2x − 10)° dir.\nŞekil ölçekli değildir.\nBuna göre, m(DOB) kaç derecedir?',
 dogru=50,yan=[(20,'2x − 10 ifadesinde 2 katsayısını atlayıp x − 10 = 20 bulmuş.','islem'),(30,'Denklemden yalnız x = 30’u bulup sorulan açıyı hesaplamadan bırakmış.','dikkat'),(40,'İstenen açı yerine m(AOC) = x + 10 = 40’ı hesaplamış.','dikkat'),(45,'AOC ve DOB açılarının toplamı 90° olduğundan ikisini eşit sanıp 90° ÷ 2 = 45° bulmuş.','bilgi')],
 istenen='m(DOB) açısının ölçüsü.',
 ip=['Doğru üzerindeki üç açının toplamı kaç derecedir? Dik açıyı da unutma.'],
 bilgi=[TUM],
 ad=[A('Denklemi kur','A, O, B doğrusal olduğundan üç açının toplamı 180°’dir; dik açı 90°’dir.','(x + 10) + 90 + (2x − 10) = 180'),A('x’i bul','Benzer terimleri toplayıp çöz.','3x + 90 = 180 · x = 30'),A('İstenen açıyı yaz','x yerine 30 koy.','m(DOB) = 2 × 30 − 10 = 50°')],
 puf='Doğru üzerindeki bitişik açıların toplamı 180°’dir; x’i bulduktan sonra mutlaka sorulan açıya dön.',sekil=SK)

# ============ 02 · Paralel doğrular ve kesen · orta ============
kartla('K-GDA-02','Ters açılar, bütünler yan açı','İç ters açıların eşitliğinden x bulunur; kesenin aynı noktasındaki yan açı 180°’ye tamamlanır.','Ters açıları bütünler sanmak; x bulup bırakmak.','orta',3,'ge-da-paralel','Paralel iki doğru ve kesen')
x=30; a_=3*x-5; b_=2*x+25; yv=180-b_
assert a_==b_==85 and yv==95 and 5*32+20==180 and 180-(2*32+25)==91 and 180-x==150
d1y=3.1; th=65; Ak=(0.5,d1y); dirk=(cos(radians(-th)),sin(radians(-th)))
Bk=(Ak[0]+d1y/ sin(radians(th))*cos(radians(-th)),0)
f=F()
f.line((-2.6,d1y),(3.8,d1y)); f.line((-2.6,0),(3.8,0)); f.par((2.9,d1y),(3.3,d1y)); f.par((2.9,0),(3.3,0))
f.line(add(Ak,mul(dirk,-1.1)),add(Bk,mul(dirk,1.1)))
f.node((-2.95,d1y),'$d_1$'); f.node((-2.95,0),'$d_2$')
f.arc(Ak,add(Ak,(1,0)),Bk,.5,'$(3x-5)^\\circ$',1.45)
f.arc(Bk,add(Bk,(-1,0)),Ak,.5,'$(2x+25)^\\circ$',1.75)
f.arc(Bk,add(Bk,(1,0)),Ak,.9,'$y$',1.2)
f.vl('A',Ak,(-1,.8),.3); f.vl('B',Bk,(.3,-1),.3)
SK=f.svg()
q('0002',tipId='ge-da-paralel',tip='Paralel iki doğru ve kesen',z='orta',alt='Paralel Doğrular ve Kesen',kaz='Paralel iki doğruyu kesen doğruda iç ters açıların eşitliğiyle x’i, bütünler açıyla y’yi bulur.',
 kart='K-GDA-02 (iç ters + bütünler) · cebirsel ters açılar, y istenir',
 metin='Şekilde d₁ // d₂ olup bir kesen doğru bu doğruları A ve B noktalarında kesmektedir. A noktasında d₁ ile kesen arasındaki açı (3x − 5)°, B noktasında d₂ ile kesen arasındaki açı (2x + 25)° ve bu açının yanındaki açı y° dir.\nŞekil ölçekli değildir.\nBuna göre, y kaçtır?',
 dogru=95,yan=[(30,'Denklemi çözüp bulduğu x = 30’u y sanmış.','dikkat'),(85,'y açısını eşit olan ters açıyla karıştırıp 85° yazmış.','dikkat'),(91,'Ters açılar yerine toplamlarını 180° alıp x = 32 bulmuş; y = 180 − 89 = 91.','bilgi'),(150,'x = 30’u bulup y = 180 − x demiş.','islem')],
 istenen='y açısının ölçüsü (derece).',
 ip=['İşaretli iki açı kesenin hangi yanlarında ve doğrulara göre nerede? Aralarındaki ilişki eşitlik mi, toplam mı?'],
 bilgi=[PAR],
 ad=[A('İlişkiyi bul','A’daki açı ile B’deki açı kesenin zıt yanlarında, iki doğrunun arasında kaldığından iç ters açılardır; eşittir.','3x − 5 = 2x + 25'),A('x’i çöz','Bilinmeyenleri tek tarafa topla.','x = 30 · 3x − 5 = 85°'),A('y’yi hesapla','B’deki iki açı doğru üzerinde yan yanadır; toplamları 180°’dir.','y = 180° − 85° = 95°')],
 puf='Ters açılar eşit, yan yana bitişik açılar bütünlerdir; iki ilişkiyi ayrı ayrı sorgula.',sekil=SK)

# ============ 03 · Zigzag (M kuralı) · orta ============
kartla('K-GDA-03','Zigzag kuralı','Paralel doğrular arasındaki kırık çizgide açılar açıldıkları yöne göre gruplanır ve gruplar arasında denklem kurulur.','Hangi açıların aynı yöne baktığını karıştırmak; x’i tek bir açıya eşitlemek.','orta',4,'ge-da-zigzag','Paralel doğrular arasında zigzag')
x=30; a1=x+5; a3=2*x-20; Bv=110; Cv=105
assert a1==35 and a3==40 and Bv+a1==Cv+a3
assert 110+(x+5)==105+(2*x-20) and (65+5)+(2*65-20)==180 and 2*x-20==40 and x+5==35 and 180-x==150
al=45; a2=25; a3d=50
assert al+Bv+a2==180 and a2+Cv+a3d==180 and Bv+al==Cv+a3d
sc3=1.3; A3=(0.26,3.0*sc3); B3=add(A3,mul((cos(radians(-al)),sin(radians(-al))),1.5*sc3/sin(radians(al))))
C3=add(B3,mul((cos(radians(a2)),sin(radians(a2))),.8*sc3/sin(radians(a2)))); D3=add(C3,mul((cos(radians(-a3d)),sin(radians(-a3d))),C3[1]/sin(radians(a3d))))
assert abs(D3[1])<1e-9 and abs(ang(B3,A3,C3)-Bv)<1e-9 and abs(ang(C3,B3,D3)-Cv)<1e-9
f=F()
f.line((-0.9,3*sc3),(7.2,3*sc3)); f.line((-0.9,0),(7.2,0)); f.par((5.0,3*sc3),(5.4,3*sc3)); f.par((1.0,0),(1.4,0))
f.node((-1.35,3*sc3),'$d_1$'); f.node((-1.35,0),'$d_2$')
f.line(A3,B3); f.line(B3,C3); f.line(C3,D3)
f.arc(A3,add(A3,(1,0)),B3,.65); f.node(add(A3,pol(-16,1.65)),'$(x+5)^\\circ$')
f.arc(D3,add(D3,(-1,0)),C3,.65,'$(2x-20)^\\circ$',2.2)
f.arc(B3,A3,C3,.45,'$110^\\circ$',.85); f.arc(C3,B3,D3,.5,'$105^\\circ$',1.05)
f.vl('A',A3,(-1,1),.3); f.vl('B',B3,(0,-1),.3); f.vl('C',C3,(0,1),.3); f.vl('D',D3,(1,-1),.3)
SK=f.svg()
q('0003',tipId='ge-da-zigzag',tip='Paralel doğrular arasında zigzag',z='orta',alt='Zigzag (M) Kuralı',kaz='Paralel doğrular arasındaki kırık çizgide zigzag kuralıyla denklem kurup bilinmeyeni bulur.',
 kart='K-GDA-03 (M kuralı) · iki köşeli kırık çizgi, iki cebirsel açı',
 metin='Şekilde d₁ // d₂ dir. A noktası d₁ üzerinde, D noktası d₂ üzerinde olup A, B, C, D noktaları kırık çizgiyi oluşturmaktadır. m(ABC) = 110°, m(BCD) = 105°, d₁ ile [AB] arasındaki açı (x + 5)° ve d₂ ile [DC] arasındaki açı (2x − 20)° dir.\nŞekil ölçekli değildir.\nBuna göre, x kaçtır?',
 dogru=30,yan=[(35,'x yerine d₁ ile [AB] arasındaki açının ölçüsünü (x + 5 = 35) yazmış.','dikkat'),(40,'x yerine d₂ ile [DC] arasındaki açının ölçüsünü (2x − 20 = 40) yazmış.','dikkat'),(65,'Uçtaki iki açıyı bütünler sanıp (x + 5) + (2x − 20) = 180 yazmış.','bilgi'),(150,'x = 30’u bulduktan sonra x’i bir açı sanıp bütünlerini (180° − 30°) vermiş.','dikkat')],
 istenen='x’in değeri.',
 ip=['Kırık çizginin köşelerindeki açılar hangi doğruya doğru açılıyor? Açıları açıldıkları yöne göre ayırarak başla.'],
 bilgi=[MKUR],
 ad=[A('Yönleri ayır','Kırık çizginin B köşesindeki açı yukarı, C köşesindeki açı aşağı açılır; uçlardaki açılar da sırasıyla aşağı ve yukarı bakar.','Yukarı: B ile (x + 5) · Aşağı: C ile (2x − 20)'),A('Zigzag kuralını yaz','Bir yöne bakan açılar toplamı eşit olmalıdır.','110 + (x + 5) = 105 + (2x − 20)'),A('Çöz','Benzer terimleri topla.','115 + x = 85 + 2x · x = 30'),A('Kontrol et','Açıları hesaplayıp denklemi doğrula.','35 + 110 = 145 · 40 + 105 = 145')],
 puf='Zigzagda açıları “yukarı bakanlar” ve “aşağı bakanlar” diye iki gruba ayır, iki grubun toplamını eşitle.',sekil=SK)

# ============ 04 · Açıortaylar arası açı · orta ============
kartla('K-GDA-04','İki açıortay arasındaki açı','Açıortay açıyı iki eş açıya ayırır; açıortaylarla oluşan açı verilerle ilişkilendirilip denklem kurulur.','Yarıyı unutmak; istenen açı yerine x ya da toplam açıyı vermek.','orta',4,'ge-da-aciortay','Ardışık açıların açıortayları')
x=25; AOB=3*x+10; BOC=x+50; MON=(AOB+BOC)/2
assert AOB==85 and BOC==75 and MON==80 and 4*x+60==160 and 4*5+60==80 and 5+50==55 and 2*x+30==80
f=F(); Rr=3.6
Ao,Mo,Bo,No,Co=0,35,70,115,160
f.line(O,pol(Ao,Rr)); f.line(O,pol(Bo,Rr)); f.line(O,pol(Co,Rr)); f.line(O,pol(Mo,2.1)); f.line(O,pol(No,2.1))
for g in (Ao,Mo,Bo,No,Co): pass
f.arc(O,pol(Ao,1),pol(Mo,1),.8); f.arc(O,pol(Mo,1),pol(Bo,1),.8)
f.arc(O,pol(Bo,1),pol(No,1),.8); f.arc(O,pol(Bo,1),pol(No,1),.95); f.arc(O,pol(No,1),pol(Co,1),.8); f.arc(O,pol(No,1),pol(Co,1),.95)
f.arc(O,pol(Ao,1),pol(Bo,1),2.5,'$(3x+10)^\\circ$',3.2)
f.arc(O,pol(Bo,1),pol(Co,1),2.95,'$(x+50)^\\circ$',3.75)
f.arc(O,pol(Mo,1),pol(No,1),1.4); f.node(pol(100,1.62),'$80^\\circ$')
f.vl('A',pol(Ao,Rr),(1,0),.3); f.vl('B',pol(Bo,Rr),pol(Bo,1),.3); f.vl('C',pol(Co,Rr),(-1,0),.3); f.vl('M',pol(Mo,2.1),pol(Mo,1),.3); f.vl('N',pol(No,2.1),pol(No,1),.3); f.vl('O',O,(0,-1),.3)
SK=f.svg()
q('0004',tipId='ge-da-aciortay',tip='Ardışık açıların açıortayları',z='orta',alt='Açıortaylar Arası Açı',kaz='Ardışık iki açının açıortayları arasındaki açının toplam açının yarısı olduğunu kullanarak cebirsel açıyı bulur.',
 kart='K-GDA-04 (açıortaylar arası açı) · m(MON) verilir, m(BOC) istenir',
 metin='Şekilde O noktasından çıkan [OA, [OB, [OC ışınları için [OM, AOB açısının; [ON ise BOC açısının açıortayıdır. m(AOB) = (3x + 10)°, m(BOC) = (x + 50)° ve m(MON) = 80° dir.\nŞekil ölçekli değildir.\nBuna göre, m(BOC) kaç derecedir?',
 dogru=75,yan=[(25,'Denklemi çözüp bulduğu x = 25’i açının ölçüsü sanmış.','dikkat'),(80,'Verilen m(MON) = 80°’yi istenen açı sanmış.','dikkat'),(85,'Sorulan BOC yerine m(AOB) = 3x + 10 = 85° değerini bulmuş.','dikkat'),(160,'Toplam açıyı (AOC = 2 × 80 = 160°) BOC sanmış.','dikkat')],
 istenen='m(BOC) açısının ölçüsü.',
 ip=['m(MON) açısı hangi küçük açılardan oluşuyor? Açıortay AOB ve BOC açılarının her birini kaça böler?'],
 bilgi=[ACIORTAY],
 ad=[A('MON açısını ayrıştır','[OM açıortay olduğundan MOB, AOB’nin yarısıdır; [ON açıortay olduğundan BON, BOC’nin yarısıdır.','m(MON) = m(MOB) + m(BON) = (m(AOB) + m(BOC)) ÷ 2'),A('Denklemi kur','Verilen ifadeleri yerine yaz.','((3x + 10) + (x + 50)) ÷ 2 = 80'),A('x’i bul','Önce 2 ile çarp, sonra çöz.','4x + 60 = 160 · x = 25'),A('Sorulan açıyı yaz','BOC için x değerini kullan.','m(BOC) = 25 + 50 = 75°')],
 puf='İki ardışık açının açıortayları arasındaki açı, bu iki açının toplamının yarısıdır.',sekil=SK)

# ============ 05 · Saat ve açı · orta (hikâyeli) ============
kartla('K-GDA-05','Saatte akrep-yelkovan açısı','Akrebin dakikada 0,5°, yelkovanın 6° döndüğü bilgisiyle iki kolun konumu derece cinsinden yazılıp fark alınır; akrebin saat içindeki ilerlemesi unutulmaz.','Akrebi tam saat rakamında sanmak; 180°’den büyük açıyı vermek.','orta',4,'ge-da-saat','Saatte akrep ve yelkovan açısı',kalip='hikâyeli')
sa,dk=2,40; ak=sa*30+dk*.5; ye=dk*6; fark=ye-ak
assert ak==80 and ye==240 and fark==160 and 360-fark==200
assert abs(240-60)==180 and abs(240-90)==150 and abs(240-(60+40))==140
f=F(); Rc_=2.15
f.raw(f'\\draw ({0},{0}) circle ({Rc_});')
for h in range(1,13):
    ca=90-30*h; f.node(pol(ca,1.8),str(h),'font=\\small')
    f.line(pol(ca,Rc_),pol(ca,Rc_-.13))
hi=pol(90-ak,0.95); mi=pol(90-ye,1.38)
f.raw(f'\\draw[line width=2.2pt] (0,0) -- {pt(hi)};'); f.raw(f'\\draw[line width=1.1pt] (0,0) -- {pt(mi)};'); f.raw('\\fill (0,0) circle (.06);')
SK=f.svg()
q('0005',tipId='ge-da-saat',tip='Saatte akrep ve yelkovan açısı',z='orta',alt='Saat ve Açı',kaz='Akrep ve yelkovanın dönme hızlarından kolların konumunu bulup aralarındaki açıyı hesaplar.',kalip='hikâyeli',
 kart='K-GDA-05 (saat ve açı) · yelkovan 8’de, akrep 2 ile 3 arasında',
 metin='Selin ders çalışırken şekildeki duvar saatine bakıyor. Saat doğru çalışmaktadır; kısa kol akrep, uzun kol yelkovandır.\nAkrebin dakikada 0,5°, yelkovanın dakikada 6° döndüğü bilindiğine göre, bu anda akrep ile yelkovan arasındaki 180°’den küçük açı kaç derecedir?',
 dogru=160,yan=[(140,'Akrebi dakikada 1° döndürüp konumunu 60° + 40° = 100° almış; 240° − 100° = 140°.','bilgi'),(150,'Akrebi 3 rakamında (90°) sanıp 240° − 90° = 150° bulmuş.','dikkat'),(180,'Akrebin 40 dakikada ilerlediğini unutup tam 2’de (60°) sanmış: 240° − 60° = 180°.','dikkat'),(200,'Aradaki açıyı doğru bulup 360° − 160° = 200°’yi (180°’den büyük açıyı) yazmış.','dikkat')],
 istenen='Akrep ile yelkovan arasındaki 180°’den küçük açı (derece).',
 ip=['Önce saatin kaçı gösterdiğini bul. Akrep tam rakamda mı, yoksa ilerlemiş mi?'],
 bilgi=[SAAT],
 ad=[A('Saati oku','Yelkovan 8 rakamında, yani 40. dakikada; akrep 2 ile 3 arasında. Saat 2.40’tır.','Saat = 2.40'),A('Akrebin konumu','12’den itibaren 2 saat için 30° × 2, 40 dakika için 0,5° × 40.','60° + 20° = 80°'),A('Yelkovanın konumu','40 dakika için 6° × 40.','240°'),A('Açıyı bul','İki konumun farkı 180°’den küçük mü diye bak.','240° − 80° = 160°')],
 puf='Saat sorularında akrebi dakikayla da ilerlet: konumu 30° × saat + 0,5° × dakika’dır.',sekil=SK)

# ============ 06 · Katlanmış şerit · zor (hikâyeli) ============
kartla('K-GDA-06','Katlanmış şeritte açı','Katlayınca açılar korunur: katlanan kenar ile kat doğrusu arasındaki açı 180° − α dır ve bu açı aynı zamanda (katlanan açı + α) toplamına eşittir.','Katlanan açıyı kat doğrusundaki açıya eşitlemek; x bulup sorulan açıya dönmemek.','zor',5,'ge-da-serit','Katlanmış kâğıt şerit',kalip='hikâyeli')
x=30; al=2*x-5; fl=3*x-20
assert al==55 and fl==70 and 180-2*al==fl and 2*15-5==25 and 3*15-20==25 and 180-al==125
H_=2.8; psi=180+al; dE=(cos(radians(psi)),sin(radians(psi)))
E6=(0,H_); F6=add(E6,mul(dE,H_/abs(dE[1])))
assert abs(F6[1])<1e-9
dfl=(cos(radians(2*psi)),sin(radians(2*psi)))     # katlanan kenar yönü (yansıma)
assert abs(degrees(atan2(dfl[1],dfl[0]))%360-110)<1e-9 and abs(ang(E6,add(E6,dfl),(-1,H_))-fl)<1e-9
Ll=3.6; G1=add(E6,mul(dfl,Ll)); G2=add(F6,mul(dfl,Ll)); XL=-6.0
f=F()
f.fill([(XL,H_),E6,F6,(XL,0)],'fill=vurgu!6')
f.line((XL,0),F6)
f.fill([E6,F6,G2,G1],'fill=vurgu!30'); f.poly([E6,F6,G2,G1])
f.line((XL,H_),E6); f.line(E6,F6)
f.arc(E6,(-1,H_),F6,.6,'$(2x-5)^\\circ$',1.7)
f.arc(E6,(-1,H_),G1,.95,'$(3x-20)^\\circ$',1.9)
f.vl('E',E6,(1,1),.3); f.vl('F',F6,(.5,-1),.3); f.vl('A',(XL,H_),(-1,0),.3)
SK=f.svg()
q('0006',tipId='ge-da-serit',tip='Katlanmış kâğıt şerit',z='zor',alt='Katlanmış Şerit',kaz='Katlanmış şeritte kat doğrusu ve kenar arasındaki açıların eşitliğiyle cebirsel denklem kurup açıyı bulur.',kalip='hikâyeli',
 kart='K-GDA-06 (katlanmış şerit) · iki cebirsel açıdan x',
 metin='Ayşe, kenarları paralel olan şerit biçimli bir kâğıdı hediye paketi için hazırlıyor. Şeridin sağ ucunu, üst kenarındaki E noktasından alt kenarındaki F noktasına giden doğru boyunca şekildeki gibi katlıyor. Katlanan kısım, E noktasında üst kenarın sol parçasıyla (3x − 20)° lik açı yapmaktadır. Ayrıca m(AEF) = (2x − 5)° dir.\nŞekil ölçekli değildir.\nBuna göre, m(AEF) kaç derecedir?',
 dogru=55,yan=[(25,'Katlanan açıyı AEF’ye eşit sanıp 2x − 5 = 3x − 20 yazmış; x = 15 ve açı 25° çıkmış.','bilgi'),(90,'3x değerini (3 × 30) açı sanıp “− 20” kısmını atlamış.','islem'),(70,'m(AEF) yerine katlanan kısmın açısını (3x − 20 = 70°) yazmış.','dikkat'),(125,'AEF’nin bütünleri olan açıyı (180° − 55°) bulmuş.','dikkat')],
 istenen='m(AEF) açısının ölçüsü (derece).',
 ip=['Katlanmadan önce üst kenarın sağ parçası ile EF arasındaki açı kaç derece idi? Katlayınca bu açı nereye gidiyor?'],
 bilgi=[KAT],
 ad=[A('Katlanan kenarın açısını bul','Katlanmadan önce üst kenarın sağ parçası ile EF arasındaki açı 180° − α idi (α = m(AEF)). Katlayınca bu açı korunur.','Katlanan kenar ile EF arasında 180° − α'),A('Aynı açıyı bir de parçalarla yaz','Aynı açı, (3x − 20) ile α’nın toplamıdır; çünkü [EA, bu iki kenarın arasında kalır.','(3x − 20) + α = 180° − α'),A('Denklemi çöz','α yerine 2x − 5 yaz.','3x − 20 + 2x − 5 = 180 − 2x + 5 · 7x = 210 · x = 30'),A('Sorulan açıyı hesapla','x yerine 30 koy.','m(AEF) = 2 × 30 − 5 = 55°')],
 puf='Katlamada açılar korunur; katlanan kenarın kat doğrusuyla yaptığı açıyı iki farklı biçimde yazıp eşitle.',sekil=SK)

bit('dogruaci','Doğruda Açılar','geo|Doğruda Açılar')
