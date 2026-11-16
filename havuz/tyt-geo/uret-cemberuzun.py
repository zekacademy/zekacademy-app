"""TYT Geometri · Çemberde Uzun · 8 şekilli soru (kardeş yok, ipucu 1). Şekil koordinatları hesaplanır; her cevap koordinattan ölçülen uzunlukla assert edilir."""
import sys,os,math,json
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
from math import sin,cos,tan,radians,degrees,atan2,sqrt,pi
TIPK={}
def kartla(id,alt,fikir,tuzak,z,adim,tipId,tip,kalip='şekilli',kaynak=None):
    kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,kaynak or 'ÖSYM 2018–2026 TYT Geometri soruları (yalnız mantık) · MEB 9–10. sınıf geometri'); TIPK[tipId]=P.k
def q(no,ad,kalip='şekilli',**k): mk(P,no,ad=ad,adim=len(ad),kalip=kalip,**k)
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
    u=sub(a,V); v=sub(b,V); return degrees(math.acos(max(-1,min(1,(u[0]*v[0]+u[1]*v[1])/(ln(u)*ln(v))))))
def alan(ps): return abs(sum(ps[i][0]*ps[(i+1)%len(ps)][1]-ps[(i+1)%len(ps)][0]*ps[i][1] for i in range(len(ps))))/2
def pc(O,r,d): return (O[0]+r*cos(radians(d)),O[1]+r*sin(radians(d)))
def inter(p1,p2,p3,p4):
    x1,y1=p1;x2,y2=p2;x3,y3=p3;x4,y4=p4
    den=(x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
    a=x1*y2-y1*x2; b=x3*y4-y3*x4
    return ((a*(x3-x4)-(x1-x2)*b)/den,(a*(y3-y4)-(y1-y2)*b)/den)
class F:
    def __init__(s): s.o=[]
    def raw(s,t): s.o.append(t)
    def line(s,p,q_,st=''): s.o.append(f'\\draw[{st}] {pt(p)} -- {pt(q_)};')
    def poly(s,ps,st=''): s.o.append(f'\\draw[{st}] '+' -- '.join(map(pt,ps))+' -- cycle;')
    def fill(s,ps,st='fill=vurgu!25'): s.o.append(f'\\fill[{st}] '+' -- '.join(map(pt,ps))+' -- cycle;')
    def circ(s,c,r,st=''): s.o.append(f'\\draw[{st}] {pt(c)} circle ({r:.3f});')
    def dot(s,p): s.o.append(f'\\fill {pt(p)} circle (1.2pt);')
    def oarc(s,O,r,d1,d2,st=''):
        a=(d2-d1)%360
        s.o.append(f'\\draw[{st}] {pt(pc(O,r,d1))} arc[start angle={d1:.3f},delta angle={a:.3f},radius={r:.3f}];')
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
    def par(s,p,q_):
        m=mid(p,q_); e=un(sub(q_,p)); s.o.append(f'\\draw[-{{Stealth[length=1.9mm,width=1.7mm]}}] {pt(sub(m,mul(e,.07)))} -- {pt(add(m,mul(e,.07)))};')
    def body(s): return '\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'+'\n'.join(s.o)+'\n\\end{tikzpicture}'
    def svg(s): return tikz_svg(s.body())
def bitir_geo(onek,konuad):
    for qq in P.ANA: qq['kardes']=None
    P.yaz(os.path.join(GD,onek+'-1.json'),f'/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/gcb/bos-{onek}.json')
    tipler={}
    for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=TIPK[c['tipId']]))['kartlar'].append(c['id'])
    json.dump(dict(konu=konuad,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 TYT Geometri çıkmış soruları (yalnız mantık), MEB 9–10. sınıf geometri müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar',onek+'.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler))
P=Parti('cemberuzun','Çemberde Uzun','geo|Çemberde Uzun',ders='TYT Geometri',idon='tytgeo')
P.k='geo|Çemberde Uzun'; H.KONU='Çemberde Uzun'
def ok(a,b,t=1e-6): assert abs(a-b)<t,(a,b)
PIS=B('Pisagor bağıntısı','dik üçgende dik kenarların kareleri toplamı hipotenüsün karesine eşittir. Örnek: 6, 8, 10 üçgeni için 6² + 8² = 10²')
KIRD=B('Merkezden kirişe dikme','çemberin merkezinden bir kirişe indirilen dikme kirişi ortalar; yarıçap, yarım kiriş ve dikme bir dik üçgen oluşturur. Örnek: yarım kirişi 3 ve dikmesi 4 olan çemberin yarıçapı 5 tir')
TEGU=B('Teğet uzunlukları','dış bir noktadan çembere çizilen iki teğetin uzunlukları eşittir; teğet, değme noktasındaki yarıçapa diktir. Örnek: yarıçap 3 ve merkeze uzaklık 5 ise teğet uzunluğu 4 tür')
KUV=B('Kuvvet bağıntıları','çemberin içinde kesişen iki kirişin parçaları arasında ve dışarıdaki bir noktadan çizilen teğet ile kesenin uzunlukları arasında birer bağıntı vardır; bunlar parçaların çarpımlarıyla ilgilidir')
ORT=B('Ortak teğet','iki çemberin ortak teğetinin değme noktaları arasındaki uzunluk, merkezler arası uzaklık ve yarıçaplardan kurulan bir dik üçgenle bulunur; ortak iç ve ortak dış teğette yarıçaplar farklı biçimde birleşir. Dıştan teğet çemberlerde merkezler arası uzaklık yarıçaplar toplamıdır')
TDORT=B('Teğetler dörtgeni','dört kenarı da bir çembere teğet olan dörtgende her köşeden çembere çizilen iki teğet parçası eşittir; bu yüzden karşılıklı kenar uzunluklarının toplamları arasında bir ilişki vardır')
O=(0,0)
def vlab(f,t,p,c=O,d=.3): f.vl(t,p,sub(p,c),d)

# ===== 01 · merkezden kirişe dikme · kolay =====
kartla('K-GCU-01','Merkezden kirişe dikme','Dikme kirişi ortalar; yarıçap hipotenüs olan dik üçgende Pisagor ile dikme uzunluğu bulunur.','Yarım kirişi dikme sanmak; Pisagor sonunda kök almayı unutmak; yarıçap yerine çapı kullanmak.','kolay',3,'ge-cu-kiris-dikme','Merkezden kirişe dikme')
s=.14; AB1=24; R1=13; h1=sqrt(R1**2-(AB1/2)**2); assert h1==5
A1=(-12*s,-5*s); B1=(12*s,-5*s); H1=(0,-5*s)
ok(dist(A1,O),R1*s); ok(dist(B1,O),R1*s)
assert 12==AB1//2 and 25==R1**2-12**2 and 2*R1==26
f=F(); f.circ(O,R1*s); f.line(A1,B1); f.line(O,A1); f.line(O,H1); f.dik(H1,O,B1); f.dot(O)
f.sl('$13$',O,A1,B1,.26); f.sl('$24$',A1,B1,O,.28)
vlab(f,'A',A1); vlab(f,'B',B1); f.node((.28,-.22),'$H$'); f.node((0,.25),'$O$')
SK1=f.svg()
q('0001',tipId='ge-cu-kiris-dikme',tip='Merkezden kirişe dikme',z='kolay',alt='Merkezden Kirişe Dikme',kaz='Merkezden kirişe indirilen dikmenin kirişi ortaladığını kullanarak dikmenin uzunluğunu bulur.',
 kart='K-GCU-01 (merkezden kirişe dikme) · OA = 13, AB = 24',
 metin='Şekilde O merkezli çemberin [AB] kirişi çizilmiş ve O noktasından bu kirişe indirilen dikmenin ayağı H noktası olarak işaretlenmiştir. Şekilde verilen uzunluklar cm cinsindendir ve şekil ölçekli değildir.\nBuna göre, |OH| kaç cm’dir?',
 dogru=5,yan=[(12,'Merkezden inen dikmeyi değil, yarım kirişi (24 ÷ 2) cevap sanmış.','dikkat'),(13,'Yarıçapı cevap olarak yazmış.','dikkat'),(25,'Pisagorda |OH|² = 169 − 144 = 25 yi bulup kök almayı unutmuş.','islem'),(26,'Yarıçap yerine çapı (2 × 13) yazmış.','dikkat')],
 istenen='|OH| uzunluğu (cm).',
 ip=['Dikme kirişe indirilince kirişle ilgili ne olur? OHA üçgeninin hangi kenarlarını biliyorsun?'],
 bilgi=[KIRD,PIS],
 ad=[A('Yarım kirişi bul','Merkezden kirişe inen dikme kirişi ortalar.','|AH| = 24 ÷ 2 = 12'),A('Dik üçgen kur','OHA dik üçgeninde hipotenüs yarıçap olan |OA| = 13 tür.','|OH|² + 12² = 13²'),A('Dikmeyi hesapla','Pisagorla |OH|² bulunur, kök alınır.','|OH|² = 169 − 144 = 25 → |OH| = 5')],
 puf='Merkezden kirişe dikme görünce kirişi ikiye böl; yarıçap, yarım kiriş ve dikmeden Pisagorlu bir dik üçgen çıkar.',sekil=SK1)

# ===== 02 · iki paralel kiriş · zor =====
kartla('K-GCU-02','İki paralel kiriş arası uzaklık','Her kiriş için merkeze uzaklık Pisagorla bulunur; merkez kirişlerin arasındaysa uzaklıklar toplanır, aynı yandaysa çıkarılır.','Merkezin kirişlerin aynı yanında olduğunu varsaymak (çıkarmak); yalnız bir uzaklığı bulmak; çapı yazmak.','zor',4,'ge-cu-kiris-dikme','Merkezden kirişe dikme')
s=.15; R2=13
A2=(-12*s,5*s); B2=(12*s,5*s); C2=(-5*s,-12*s); D2=(5*s,-12*s)
for p in (A2,B2,C2,D2): ok(ln(p),R2*s)
d1=sqrt(R2**2-12**2); d2=sqrt(R2**2-5**2); assert d1==5 and d2==12 and d1+d2==17 and d2-d1==7 and 2*R2==26
xd=R2*s+.5
f=F(); f.circ(O,R2*s); f.line(A2,B2); f.line(C2,D2); f.line(O,A2); f.dot(O)
f.raw(f'\\draw[dashed,thin] ({B2[0]+.4:.3f},{B2[1]:.3f}) -- ({xd+.1:.3f},{B2[1]:.3f}); \\draw[dashed,thin] {pt(D2)} -- ({xd+.1:.3f},{D2[1]:.3f}); \\draw[<->] ({xd:.3f},{B2[1]:.3f}) -- ({xd:.3f},{D2[1]:.3f});')
f.node((xd+.3,(B2[1]+D2[1])/2),'$x$')
f.sl('$13$',O,A2,B2,.27); f.node((0,B2[1]+.28),'$24$'); f.node((0,D2[1]-.28),'$10$')
vlab(f,'A',A2); vlab(f,'B',B2); vlab(f,'C',C2); vlab(f,'D',D2); f.node((.22,-.24),'$O$')
SK2=f.svg()
q('0002',tipId='ge-cu-kiris-dikme',tip='Merkezden kirişe dikme',z='zor',alt='Paralel Kirişler',kaz='Merkezin iki yanındaki paralel kirişlerin merkeze uzaklıklarını bulup aralarındaki uzaklığı hesaplar.',
 kart='K-GCU-02 (paralel kirişler) · 24 ve 10, yarıçap 13',
 metin='Şekilde O merkezli çemberde [AB] // [CD] dir ve O noktası bu iki kirişin arasında kalmaktadır. Şekilde verilen uzunluklar cm cinsindendir ve şekil ölçekli değildir.\nBuna göre, paralel kirişler arasındaki uzaklık olan x kaç cm’dir?',
 dogru=17,yan=[(5,'Yalnız [AB] kirişinin merkeze uzaklığını bulup bırakmış.','dikkat'),(7,'Merkezin kirişlerin aynı yanında olduğunu sanıp uzaklıkları çıkarmış: 12 − 5 = 7.','dikkat'),(12,'Yalnız [CD] kirişinin merkeze uzaklığını bulup bırakmış.','dikkat'),(26,'Kirişler arası uzaklığı çapa (2 × 13) eşit sanmış.','bilgi')],
 istenen='Paralel kirişler arasındaki uzaklık x (cm).',
 ip=['Her kirişin merkeze olan uzaklığını ayrı ayrı bulmak için hangi dik üçgenleri kurarsın? O noktasının konumu, uzaklıkları toplamanı mı çıkarmanı mı gerektiriyor?'],
 bilgi=[KIRD,PIS],
 ad=[A('Yarım kirişleri bul','Merkezden kirişlere inen dikmeler kirişleri ortalar.','24 için 12 · 10 için 5'),A('Merkeze uzaklıkları bul','Her kiriş için yarıçap hipotenüs olan dik üçgende Pisagor uygula.','d₁ = √(13² − 12²) = 5 · d₂ = √(13² − 5²) = 12'),A('Konumu yorumla','O noktası kirişlerin arasında olduğundan merkeze uzaklıklar toplanır.','x = 5 + 12 = 17'),A('Kontrol et','Aynı yanda olsalardı fark 7 olurdu; ancak O kirişlerin arasındadır.','x = 17')],
 puf='Paralel kirişlerde merkezin konumuna bak: kirişlerin arasındaysa merkeze uzaklıklar toplanır, aynı yandaysa çıkarılır.',sekil=SK2)

# ===== 03 · teğet uzunluğu · kolay · hikâyeli =====
kartla('K-GCU-03','Teğet uzunluğu','Teğet yarıçapa diktir; merkez uzaklığı hipotenüs olan dik üçgende Pisagor ile teğet uzunluğu bulunur.','Teğet uzunluğunu uzaklık farkı ya da toplamı sanmak; hipotenüsü cevap yazmak.','kolay',3,'ge-cu-teget','Teğet uzunlukları','hikâyeli')
s=.3; r3=6; d3=10; th=degrees(math.acos(r3/d3)); P3=(d3*s,0); A3=pc(O,r3*s,th)
ok(dist(A3,P3)/s,8); assert abs((A3[0]-P3[0])*A3[0]+(A3[1]-P3[1])*A3[1])<1e-9
assert 10-6==4 and 10+6==16
f=F(); f.circ(O,r3*s); f.line(O,A3); f.line(A3,P3); f.line(O,P3); f.dik(A3,O,P3); f.dot(O)
f.sl('$6$',O,A3,P3,.26); f.node((1.15,-.27),'$10$')
f.vl('A',A3,sub(A3,O),.3); f.vl('P',P3,(1,0),.3); f.node((-.05,-.27),'$O$')
SK3=f.svg()
q('0003',tipId='ge-cu-teget',tip='Teğet uzunlukları',z='kolay',alt='Teğet Uzunluğu',kaz='Teğetin yarıçapa dik olduğunu kullanarak dış noktadan çembere çizilen teğetin uzunluğunu bulur.',kalip='hikâyeli',
 kart='K-GCU-03 (teğet uzunluğu) · OP = 10, r = 6',
 metin='Dairesel bir havuzun merkezi O noktasıdır. Havuzun dışındaki P noktasında duran bir bahçıvan, havuz kenarındaki A noktasına dokunacak biçimde düz bir hortum germiştir; hortum havuza teğettir. Şekilde verilen uzunluklar metre cinsindendir ve şekil ölçekli değildir.\nBuna göre, hortumun uzunluğu olan |PA| kaç metredir?',
 dogru=8,yan=[(4,'|PA| yerine uzaklıkların farkını (10 − 6) yazmış.','bilgi'),(6,'Yarıçapı cevap olarak yazmış.','dikkat'),(10,'Hipotenüs olan |OP| uzunluğunu cevap sanmış.','dikkat'),(16,'|PA| yerine uzaklıkların toplamını (10 + 6) yazmış.','bilgi')],
 istenen='|PA| uzunluğu (m).',
 ip=['Teğet, değme noktasındaki yarıçapla hangi açıyı yapar? OAP üçgeninin hangi kenarı hipotenüstür?'],
 bilgi=[TEGU,PIS],
 ad=[A('Dik açıyı bul','Teğet değme noktasındaki yarıçapa dik olduğundan OAP üçgeni A da diktir; hipotenüs |OP| = 10 dur.','|OA| = 6 · |OP| = 10'),A('Pisagoru yaz','Dik kenarların kareleri toplamı hipotenüsün karesine eşittir.','|PA|² + 6² = 10²'),A('Uzunluğu bul','Kök alınır.','|PA|² = 100 − 36 = 64 → |PA| = 8')],
 puf='Teğet uzunluğu sorularında merkezi değme noktasına ve dış noktaya bağla; dik üçgenin hipotenüsü merkeze uzaklıktır.',sekil=SK3)

# ===== 04 · iki kiriş kesişmesi · orta =====
kartla('K-GCU-04','Kesişen kirişler','Kesişen iki kirişte parçaların çarpımları eşittir; eksik parça bulunup kirişe eklenir.','Çarpmak yerine toplamak; eksik parçayı bulup kirişin tamamını eklemeyi unutmak; parçaları yanlış eşleştirmek.','orta',3,'ge-cu-kuvvet','Kesen–teğet ve kiriş bağıntısı')
s=.25; ph=radians(-55); uu=(cos(ph),sin(ph)); E4=(0,0); A4=(-4*s,0); B4=(9*s,0); C4=mul(uu,-3*s); D4=mul(uu,12*s)
kk=(-27*s*s-5*s*C4[0])/(2*C4[1]); cc=(2.5*s,kk); R4=dist(cc,A4)
for p in (A4,B4,C4,D4): ok(dist(cc,p),R4)
assert 4*9==3*12 and 4+9-3==10 and 3+12==15 and 3*9==27
f=F(); f.circ(cc,R4); f.line(A4,B4); f.line(C4,D4)
f.sl('$4$',A4,E4,cc,.24); f.sl('$9$',E4,B4,cc,.24); f.sl('$3$',C4,E4,cc,.24)
for t,p in (('A',A4),('B',B4),('C',C4),('D',D4)): vlab(f,t,p,cc)
f.node(add(E4,(-.12,-.26)),'$E$')
SK4=f.svg()
q('0004',tipId='ge-cu-kuvvet',tip='Kesen–teğet ve kiriş bağıntısı',z='orta',alt='Kesişen Kirişler',kaz='Kesişen iki kirişin parçalarının çarpımlarını eşitleyerek bir kirişin uzunluğunu bulur.',
 kart='K-GCU-04 (kesişen kirişler) · AE = 4, EB = 9, CE = 3',
 metin='Şekildeki çemberin [AB] ve [CD] kirişleri E noktasında kesişmektedir. Şekilde bazı parçaların uzunlukları cm cinsinden verilmiştir ve şekil ölçekli değildir.\nBuna göre, [CD] kirişinin uzunluğu kaç cm’dir?',
 dogru=15,yan=[(12,'Yalnız |ED| parçasını bulup |CE| yi eklememiş.','dikkat'),(13,'Çarpım yerine toplam kullanıp |ED| = 4 + 9 − 3 = 10 bulmuş, |CD| = 13 yazmış.','bilgi'),(27,'|CE| × |EB| = 27 çarpımını cevap sanmış; parçaları yanlış eşleştirmiş.','bilgi'),(36,'|AE| × |EB| = 36 çarpımını cevap olarak yazmış.','dikkat')],
 istenen='|CD| uzunluğu (cm).',
 ip=['Kesişen iki kirişin parçaları arasındaki ilişkiyi hatırla.'],
 bilgi=[KUV],
 ad=[A('Bağıntıyı yaz','Kesişen iki kirişte, bir kirişin parçalarının çarpımı diğerinin parçalarının çarpımına eşittir.','|AE| × |EB| = |CE| × |ED|'),A('|ED| yi bul','Bilinen değerler yerine konur.','4 × 9 = 3 × |ED| → |ED| = 12'),A('Kirişi tamamla','|CD| iki parçanın toplamıdır.','|CD| = 3 + 12 = 15')],
 puf='Kesişen kirişlerde parçalar arasındaki bağıntıyı yaz; sonda istenenin bir parça mı kirişin tamamı mı olduğuna bak.',sekil=SK4)

# ===== 05 · teğet–kesen · orta =====
kartla('K-GCU-05','Teğet–kesen bağıntısı','Dış noktadan teğet ve kesende teğetin karesi, kesenin dış parçası ile tamamının çarpımına eşittir; iç parça farktan bulunur.','|PB| yerine |AB| sanmak; çarpmak yerine toplamak; teğeti kesenin parçası saymak.','orta',3,'ge-cu-kuvvet','Kesen–teğet ve kiriş bağıntısı')
s=.22; r5=6; PT5=12; PA5=8; d5=sqrt(PT5**2+r5**2); PB5=PT5**2/PA5; assert PB5==18
P5=(d5*s,0); T5=(r5**2/d5*s,r5*sqrt(1-(r5/d5)**2)*s)
cps=(PA5+PB5)/(2*d5); psi=math.acos(cps); u5=(-cos(psi),-sin(psi))
A5=add(P5,mul(u5,PA5*s)); B5=add(P5,mul(u5,PB5*s))
ok(ln(A5),r5*s); ok(ln(B5),r5*s); ok(dist(P5,T5)/s,12); ok(dist(A5,B5)/s,10)
assert abs(T5[0]*(T5[0]-P5[0])+T5[1]*T5[1])<1e-9
assert 12-8==4 and 8+18==26
f=F(); f.circ(O,r5*s); f.line(P5,T5); f.line(P5,B5)
f.sl('$12$',P5,T5,O,.27); f.sl('$8$',P5,A5,T5,.27)
f.vl('P',P5,(1,0),.3); f.vl('T',T5,sub(T5,O),.3); f.vl('A',A5,sub(A5,O),.32); f.vl('B',B5,sub(B5,O),.3)
SK5=f.svg()
q('0005',tipId='ge-cu-kuvvet',tip='Kesen–teğet ve kiriş bağıntısı',z='orta',alt='Teğet ve Kesen',kaz='Teğet–kesen bağıntısıyla kesenin çember içinde kalan parçasının uzunluğunu bulur.',
 kart='K-GCU-05 (teğet–kesen) · PT = 12, PA = 8',
 metin='Şekilde P noktasından çembere çizilen [PT] doğru parçası T noktasında çembere teğettir. P noktasından geçen bir kesen çemberi önce A, sonra B noktasında kesmektedir. Şekilde verilen uzunluklar cm cinsindendir ve şekil ölçekli değildir.\nBuna göre, |AB| kaç cm’dir?',
 dogru=10,yan=[(4,'Uzunlukları çıkarıp |PT| − |PA| = 4 yazmış; teğet–kesen bağıntısını bilmiyor.','bilgi'),(12,'Teğetin uzunluğunu cevap sanmış.','dikkat'),(18,'|PB| = 18 i bulup |PA| yı çıkarmayı unutmuş.','dikkat'),(26,'|PA| + |PB| = 8 + 18 yi cevap sanmış.','islem')],
 istenen='|AB| uzunluğu (cm).',
 ip=['Teğet ile kesenin uzunlukları arasındaki ilişkiyi hatırla; kesenin hangi parçası isteniyor?'],
 bilgi=[KUV],
 ad=[A('Bağıntıyı yaz','Teğetin karesi, kesenin dış parçası ile tamamının çarpımına eşittir.','|PT|² = |PA| × |PB|'),A('|PB| yi bul','Bilinen değerler yerine konur.','144 = 8 × |PB| → |PB| = 18'),A('|AB| yi çıkar','Kesenin çember içinde kalan parçası tamamından dış parçanın farkıdır.','|AB| = 18 − 8 = 10')],
 puf='Teğet–kesen sorularında dış parça ile tamamını ayır; iç parçayı sonda bulursun.',sekil=SK5)

# ===== 06 · çapraz kayış (iç ortak teğet) · orta =====
kartla('K-GCU-06','İç ortak teğet','Merkezlerden birinden teğete paralel çizince yarıçapların toplamı bir dik kenar olur; hipotenüs merkezler arası uzaklıktır.','Dış teğet formülünü (fark) kullanmak; karekök almayı unutmak; merkezler arası uzaklığı cevap sanmak.','orta',3,'ge-cu-iki-cember','İki çemberin ortak teğeti','hikâyeli')
s=.3; r1,r2,d6=3,5,17; O1=(0,0); O2=(d6*s,0)
cph=(r1+r2)/d6; sph=sqrt(1-cph**2)
def nrm(sg): return (cph,sg*sph)
nn=nrm(1); T1=add(O1,mul(nn,r1*s)); T2=sub(O2,mul(nn,r2*s)); nm=nrm(-1); S1=add(O1,mul(nm,r1*s)); S2=sub(O2,mul(nm,r2*s))
ok(dist(T1,T2)/s,15)
# teğetlik: T1-T2 doğrusu her iki merkezden uzaklık r1, r2
def duzd(p,a,b): return abs((b[0]-a[0])*(a[1]-p[1])-(a[0]-p[0])*(b[1]-a[1]))/dist(a,b)
ok(duzd(O1,T1,T2),r1*s); ok(duzd(O2,T1,T2),r2*s)
assert 17-8==9 and 17+8==25 and 15**2==225
f=F(); f.circ(O1,r1*s); f.circ(O2,r2*s); f.line(T1,T2,'thick'); f.line(S1,S2,'thick'); f.line(O1,T1); f.line(O2,T2); f.dot(O1); f.dot(O2)
yd=-(r2*s+.4)
f.raw(f'\\draw[dashed,thin] {pt(O1)} -- ({O1[0]:.3f},{yd-.1:.3f}); \\draw[dashed,thin] {pt(O2)} -- ({O2[0]:.3f},{yd-.1:.3f}); \\draw[<->] ({O1[0]:.3f},{yd:.3f}) -- ({O2[0]:.3f},{yd:.3f});')
f.node((d6*s/2,yd-.25),'$17$')
f.node(add(lerp(T1,T2,.3),(.1,.3)),'$x$'); f.sl('$3$',O1,T1,O2,.24); f.sl('$5$',O2,T2,O1,.24)
f.node((.33,-.3),'$O_1$'); f.node((O2[0]+.35,-.32),'$O_2$')
f.node(add(T1,(-.3,.2)),'$T_1$'); f.node(add(T2,(.12,-.3)),'$T_2$')
SK6=f.svg()
q('0006',tipId='ge-cu-iki-cember',tip='İki çemberin ortak teğeti',z='orta',alt='Ortak İç Teğet',kaz='Merkezleri arası uzaklığı ve yarıçapları verilen iki çemberin ortak iç teğetinin uzunluğunu hesaplar.',kalip='hikâyeli',
 kart='K-GCU-06 (iç ortak teğet) · r = 3 ve 5, d = 17',
 metin='Bir atölyede iki makara, merkezleri O₁ ve O₂ olacak biçimde yerleştirilmiş ve üzerlerine bir kayış çaprazlama geçirilmiştir. Kayışın makaralara dokunmayan düz kısımları, makaraların ortak iç teğetleridir. Şekilde birimler cm dir ve şekil ölçekli değildir.\nBuna göre, kayışın [T₁T₂] düz kısmının uzunluğu olan x kaç cm’dir?',
 dogru=15,yan=[(9,'Merkezler arası uzaklıktan yarıçaplar toplamını çıkarıp 17 − 8 = 9 yazmış.','bilgi'),(17,'Merkezler arası uzaklığı teğet uzunluğu sanmış.','dikkat'),(25,'Merkezler arası uzaklıkla yarıçaplar toplamını toplamış: 17 + 8.','bilgi'),(225,'Pisagorda x² = 225 değerini bulup kök almayı unutmuş.','islem')],
 istenen='[T₁T₂] düz kısmının uzunluğu x (cm).',
 ip=['Yarıçaplar teğetle hangi açıyı yapar? Merkezler arası uzaklığı hipotenüs alan bir dik üçgen kurmayı dene.'],
 bilgi=[ORT,PIS],
 ad=[A('Dik üçgen kur','[O₂T₂] yarıçapı uzatılıp O₁ den [T₁T₂] ye paralel çizilirse hipotenüsü [O₁O₂], dik kenarları x ve r₁ + r₂ olan bir dik üçgen oluşur.','hipotenüs 17 · dik kenarlar: x ve 3 + 5 = 8'),A('Pisagoru yaz','Dik kenarların kareleri toplamı hipotenüsün karesidir.','x² + 8² = 17²'),A('x i bul','Eşitlikten x çekilir.','x² = 289 − 64 = 225 → x = 15')],
 puf='Ortak teğet sorularında merkezler arası uzaklığı hipotenüs alan bir dik üçgen kur; yarıçaplar hangi dik kenarı oluşturuyor diye bak.',sekil=SK6)

# ===== 07 · dıştan teğet çemberler · zor =====
kartla('K-GCU-07','Dış ortak teğetten yarıçap','Dıştan teğet çemberlerde merkezler arası uzaklık yarıçaplar toplamıdır; dış ortak teğetten oluşan dik üçgende Pisagor bilinmeyen yarıçapı verir.','Dış teğet için toplam yerine fark kullanmamak; r yerine merkezler arası uzaklığı vermek; verilen değeri cevap sanmak.','zor',4,'ge-cu-iki-cember','İki çemberin ortak teğeti')
s=.2; R7,r7,t7=9,4,12; d7=R7+r7; assert t7**2+(R7-r7)**2==d7**2
O1=(0,0); O2=(d7*s,0); cph=(R7-r7)/d7; nn=(cph,sqrt(1-cph**2))
T1=add(O1,mul(nn,R7*s)); T2=add(O2,mul(nn,r7*s)); ok(dist(T1,T2)/s,12)
ok(duzd(O1,T1,T2),R7*s); ok(duzd(O2,T1,T2),r7*s)
assert 9-4==5 and d7==13
f=F(); f.circ(O1,R7*s); f.circ(O2,r7*s); f.line(T1,T2,'thick'); f.line(O1,T1); f.dot(O1); f.dot(O2)
f.sl('$9$',O1,T1,O2,.24); f.sl('$12$',T1,T2,O1,.27)
f.node((-.12,-.25),'$O_1$'); f.node((O2[0]+.1,-.3),'$O_2$')
f.node(add(T1,(-.3,.25)),'$T_1$'); f.node(add(T2,(.2,.2)),'$T_2$')
SK7=f.svg()
q('0007',tipId='ge-cu-iki-cember',tip='İki çemberin ortak teğeti',z='zor',alt='Dıştan Teğet Çemberler',kaz='Dıştan teğet iki çemberin ortak dış teğetinden küçük yarıçapı ve merkezler arası uzaklığı bulur.',
 kart='K-GCU-07 (dış ortak teğet) · R = 9, T₁T₂ = 12',
 metin='Şekildeki O₁ ve O₂ merkezli çemberler birbirine dıştan teğettir. [T₁T₂], iki çembere T₁ ve T₂ noktalarında teğet olan ortak dış teğetin değme noktaları arasındaki parçadır. Şekilde verilen uzunluklar cm cinsindendir ve şekil ölçekli değildir.\nBuna göre, |O₁O₂| kaç cm’dir?',
 dogru=13,yan=[(4,'Küçük çemberin yarıçapını bulup merkezler arası uzaklığa geçmemiş.','dikkat'),(5,'Merkezler arası uzaklık yerine yarıçaplar farkını (9 − 4) yazmış.','dikkat'),(9,'Büyük çemberin yarıçapını cevap sanmış.','dikkat'),(12,'Verilen ortak teğet uzunluğunu cevap olarak yazmış.','dikkat')],
 istenen='|O₁O₂| uzunluğu (cm).',
 ip=['Küçük çemberin yarıçapına r deyip merkezler arası uzaklığı r cinsinden yaz. Merkezden teğete paralel çizersen nasıl bir dik üçgen oluşur?'],
 bilgi=[ORT,PIS],
 ad=[A('Uzaklığı r ile yaz','Küçük yarıçap r olsun; dıştan teğet çemberlerde merkezler arası uzaklık yarıçapların toplamıdır.','|O₁O₂| = 9 + r'),A('Dik üçgen kur','O₂ den [O₁T₁] ye dik çizilirse hipotenüs [O₁O₂], dik kenarlar 12 ve 9 − r olur.','(9 + r)² = 12² + (9 − r)²'),A('r yi çöz','Parantezler açılınca r² ler sadeleşir.','81 + 18r = 225 − 18r → 36r = 144 → r = 4'),A('Uzaklığı bul','r yerine 4 yazılır.','|O₁O₂| = 9 + 4 = 13')],
 puf='Dıştan teğet çemberlerde merkezler arası uzaklığı yarıçaplar toplamı yaz; teğetten dik üçgen kur, kareler sadeleşirse denklem doğrusal kalır.',sekil=SK7)

# ===== 08 · teğetler dörtgeni · orta · hikâyeli =====
kartla('K-GCU-08','Teğetler dörtgeni','Teğetler dörtgeninde karşılıklı kenar toplamları arasındaki ilişkiden eksik kenar bulunur; sonra çevre yazılır.','Karşılıklı kenarları eşit sanmak; eksik kenarı bulup çevreye katmamak; yalnız bir karşılıklı toplamı cevap yazmak.','orta',3,'ge-cu-dortgen','Teğetler dörtgeni','hikâyeli')
lens=[6,3,4,8]   # A,B,C,D teğet uzunlukları
def topl(r): return sum(math.atan(l/r) for l in lens)
lo,hi=1e-6,1e3
for _ in range(200):
    mdl=(lo+hi)/2
    if topl(mdl)>math.pi: lo=mdl
    else: hi=mdl
rq=(lo+hi)/2; assert abs(topl(rq)-math.pi)<1e-9
# ölçek: r ~ gerçek birim; çizim cm = birim * ss
ss=.22
a0=-90; vs={}; gap=[math.degrees(math.atan(l/rq)) for l in lens]
# sıra: TAB, B, TBC, C, TCD, D, TDA, A
ang_cur=a0; order=['B','C','D','A']; li={'A':6,'B':3,'C':4,'D':8}
for nme in order:
    g=math.degrees(math.atan(li[nme]/rq)); vs[nme]=pc(O,sqrt(rq**2+li[nme]**2)*ss,ang_cur+g); ang_cur+=2*g
ok(ang_cur,a0+360,1e-6)
for (p1,p2,L) in (('A','B',9),('B','C',7),('C','D',12),('D','A',14)): ok(dist(vs[p1],vs[p2])/ss,L,1e-6)
assert 9+12==7+14 and 9+7+12+14==42 and 9+7+12==28 and 9+12==21 and 9+7+12+7==35 and 2*28==56
f=F(); f.circ(O,rq*ss); f.poly([vs['A'],vs['B'],vs['C'],vs['D']])
icq=O
f.sl('$9$',vs['A'],vs['B'],icq,.27); f.sl('$7$',vs['B'],vs['C'],icq,.27); f.sl('$12$',vs['C'],vs['D'],icq,.27)
for t in 'ABCD': vlab(f,t,vs[t],O,.3)
SK8=f.svg()
q('0008',tipId='ge-cu-dortgen',tip='Teğetler dörtgeni',z='orta',alt='Teğetler Dörtgeni',kaz='Teğetler dörtgeninde karşılıklı kenar toplamlarını eşitleyerek eksik kenarı ve çevreyi bulur.',kalip='hikâyeli',
 kart='K-GCU-08 (teğetler dörtgeni) · AB = 9, BC = 7, CD = 12',
 metin='Dörtgen biçimli bir bahçenin dört kenarı, bahçenin içindeki dairesel süs havuzuna şekildeki gibi teğettir. Bahçenin üç kenarının uzunlukları metre cinsinden şekilde verilmiştir ve şekil ölçekli değildir.\nBuna göre, bahçenin çevresi kaç metredir?',
 dogru=42,yan=[(21,'Yalnız bir karşılıklı kenar çiftinin toplamını (9 + 12) cevap sanmış.','dikkat'),(28,'Bilinen üç kenarı toplayıp dördüncü kenarı eklememiş.','dikkat'),(35,'Karşılıklı kenarları eşit sanıp |AD| = |BC| = 7 almış: 9 + 7 + 12 + 7 = 35.','bilgi'),(56,'Üç kenarın toplamını (28) iki katına çıkarmış.','islem')],
 istenen='Bahçenin çevresi (m).',
 ip=['Çembere teğet iki doğru parçasının uzunlukları arasında ne var?'],
 bilgi=[TDORT],
 ad=[A('Kuralı yaz','Teğetler dörtgeninde karşılıklı kenarların toplamları eşittir.','|AB| + |CD| = |BC| + |AD|'),A('|AD| yi bul','Bilinen değerler yerine konur.','9 + 12 = 7 + |AD| → |AD| = 14'),A('Çevreyi topla','Dört kenarın toplamı.','9 + 7 + 12 + 14 = 42')],
 puf='Teğetler dörtgeninde eksik kenarı karşılıklı kenar toplamlarının ilişkisinden bul, sonra çevreyi yaz.',sekil=SK8)

bitir_geo('cemberuzun','Çemberde Uzun')
