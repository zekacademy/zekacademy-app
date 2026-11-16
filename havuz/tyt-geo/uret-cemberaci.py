"""TYT Geometri · Çemberde Açı · 10 şekilli soru (kardeş yok, ipucu 1). Şekil koordinatları açılardan hesaplanır; her cevap ölçülen açıyla assert edilir."""
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
P=Parti('cemberaci','Çemberde Açı','geo|Çemberde Açı',ders='TYT Geometri',idon='tytgeo')
P.k='geo|Çemberde Açı'; H.KONU='Çemberde Açı'
def ok(a,b,t=1e-6): assert abs(a-b)<t,(a,b)
MERK=B('Merkez açı ve çevre açı','merkez açının ölçüsü gördüğü yayın ölçüsüne eşittir; çevre açı ise gördüğü yayın yarısıdır. Örnek: 80° lik yayı gören çevre açı 40° dir')
CAP=B('Çapı gören çevre açı','çap, çemberi 180° lik iki yaya böler; bu yüzden çapı gören çevre açı dik açıdır')
TEGK=B('Teğet–kiriş açısı','teğet ile kiriş arasındaki açı gördüğü yayın yarısıdır; yani aynı yayı gören çevre açıya eşittir. Örnek: gördüğü yay 90° ise teğet–kiriş açısı 45° dir')
TEGY=B('Teğet ve yarıçap','teğet, değme noktasındaki yarıçapa diktir. Örnek: O merkezli çembere A noktasında teğet olan doğru için OA ⊥ doğru')
ICA=B('İç açı (kirişlerin kesişmesi)','çemberin içinde kesişen iki kirişin yaptığı açı, gördüğü iki yayın toplamının yarısıdır. Örnek: yaylar 20° ve 100° ise açı 60° dir')
DISA=B('Dış açı (kesenlerin kesişmesi)','çemberin dışında kesişen iki kesenin yaptığı açı, gördüğü büyük yayla küçük yayın farkının yarısıdır. Örnek: yaylar 150° ve 90° ise açı 30° dir')
DORT=B('Kirişler dörtgeni','köşeleri çember üzerinde olan dörtgende karşılıklı açıların toplamı 180° dir; tamamlayıcı (doğrusal) açılar 180° e tamamlanır. Örnek: bir açısı 100° ise karşısındaki açı 80° dir')
IKIZ=B('Yarıçapların oluşturduğu ikizkenar üçgen','merkezi köşe alan, kenarları yarıçap olan üçgen ikizkenardır; taban açıları eşittir. Örnek: tepe açısı 100° ise taban açıları 40° dir')
r=1.9; O=(0,0)
def cemb(f,r_=r,pts=()):
    f.circ(O,r_)
def vlab(f,t,p,d=.3): f.vl(t,p,sub(p,O),d)

# ===== 01 · merkez açı ve çevre açı (küçük yayda çevre açı) · orta =====
kartla('K-GCA-01','Merkez açı – çevre açı','Çevre açı, gördüğü yayın yarısıdır; köşe küçük yay üzerindeyse gördüğü yay büyük yaydır.','Merkez açının yarısını almak (köşenin hangi yayda olduğuna bakmamak); merkez açıyı çevre açı sanmak.','orta',3,'ge-ca-merkez-cevre','Merkez açı ve çevre açı')
r1=2.2; A1=pc(O,r1,235); B1=pc(O,r1,305); C1=pc(O,r1,270)
ok(ang(O,A1,B1),70); ok(ang(C1,A1,B1),145); assert 180-35==145 and 2*70==140 and 180-70==110
f=F(); f.circ(O,r1); f.line(O,A1); f.line(O,B1); f.line(C1,A1); f.line(C1,B1); f.dot(O)
f.arc(O,A1,B1,.5,'$70^\\circ$',.85); f.arc(C1,A1,B1,.3,'$x$',.62)
vlab(f,'A',A1); vlab(f,'B',B1); vlab(f,'C',C1,.32); f.node((0,.27),'$O$')
SK1=f.svg()
q('0001',tipId='ge-ca-merkez-cevre',tip='Merkez açı ve çevre açı',z='orta',alt='Merkez ve Çevre Açı',kaz='Merkez açıdan, köşesi küçük yayda olan çevre açıyı hesaplar.',
 kart='K-GCA-01 (merkez/çevre açı) · köşe küçük yayda',
 metin='Şekilde O merkezli çemberin üzerinde A, B ve C noktaları verilmiştir. C noktası, A ile B arasındaki küçük yay üzerindedir ve [OA], [OB] çemberin yarıçaplarıdır. Şekil ölçekli değildir.\nBuna göre, x = m(ACB) kaç derecedir?',
 dogru=145,yan=[(35,'Çevre açıyı merkez açının yarısı (35°) almış; C’nin küçük yayda olduğunu, bu yüzden büyük yayı gördüğünü kaçırmış.','dikkat'),(70,'x açısını merkez açıya eşit sanmış.','bilgi'),(110,'Merkez açıyı 180° den çıkarıp 110° bulmuş; bu, çevre açı ile merkez açı arasındaki ilişki değildir.','bilgi'),(140,'Çevre açıyı merkez açının iki katı (140°) almış; ilişkiyi ters kurmuş.','bilgi')],
 istenen='x = m(ACB) çevre açısının ölçüsü.',
 ip=['Küçük yayın ölçüsünü merkez açıdan bul; C noktasının bu yaya göre hangi tarafta olduğuna dikkat et.'],
 bilgi=[MERK],
 ad=[A('Büyük yayı bul','Merkez açı küçük yaya eşittir; C küçük yayın üzerinde olduğundan x, büyük yayı görür.','küçük yay = 70° → büyük yay = 360° − 70° = 290°'),A('Çevre açıyı yaz','Çevre açı gördüğü yayın yarısıdır.','x = 290° ÷ 2 = 145°'),A('Kontrol et','Aynı yayı gören iki çevre açıdan biri küçük, biri büyük yaydadır; toplamları 180° olur.','35° + 145° = 180°')],
 puf='Çevre açının köşesi gördüğü yayın karşı tarafındaysa yay yarısı alınır; köşe o yayın üzerindeyse diğer (büyük) yayın yarısı alınır.',sekil=SK1)

# ===== 02 · çapı gören açı · kolay =====
kartla('K-GCA-02','Çapı gören çevre açı','Çap uçlarını bir çember noktasına bağlayan üçgende, çapı gören açı 90° olduğundan diğer iki açının toplamı 90° dir.','90° yi unutup iç açıları 180° e tamamlamak; verilen açıyı aranan sanmak.','kolay',2,'ge-ca-cap','Çapı gören çevre açı','hikâyeli')
A2=pc(O,r,180); B2=pc(O,r,0); C2=pc(O,r,68)
ok(ang(A2,B2,C2),34); ok(ang(B2,A2,C2),56); ok(ang(C2,A2,B2),90)
assert 90-34==56 and 90+34==124 and 180-34==146
f=F(); f.circ(O,r); f.line(A2,B2); f.line(A2,C2); f.line(B2,C2); f.dot(O)
f.arc(A2,B2,C2,.95,'$34^\\circ$',1.5); f.arc(B2,A2,C2,.5,'$x$',.82)
f.vl('A',A2,(-1,-.3),.3); f.vl('B',B2,(1,-.3),.3); vlab(f,'C',C2); f.node((0,-.27),'$O$')
SK2=f.svg()
q('0002',tipId='ge-ca-cap',tip='Çapı gören çevre açı',z='kolay',alt='Çapı Gören Açı',kaz='Çapı gören çevre açının 90° olduğunu kullanarak üçgenin bir açısını bulur.',kalip='hikâyeli',
 kart='K-GCA-02 (çapı gören açı) · yuvarlak havuz kenarında halat',
 metin='Dairesel bir havuzun merkezi O noktasıdır. Havuzun merkezinden geçen bir halatın uçları havuz kenarındaki A ve B noktalarına bağlanmıştır. Havuz kenarındaki C noktasındaki bir kişi, A ve B noktalarına birer ip gererek ABC üçgenini oluşturmuştur. Şekil ölçekli değildir.\nBuna göre, x = m(ABC) kaç derecedir?',
 dogru=56,yan=[(34,'Verilen 34° lik açıyı x ile eşit sanmış.','dikkat'),(90,'Çapı gören açının 90° olduğunu bilip bunu x sanmış; x, B köşesindeki açıdır.','dikkat'),(124,'90° ile 34° yi toplamış; üçgende iki açının toplamı yerine fark gerekir.','islem'),(146,'Açıyı 180° − 34° olarak almış; C açısının 90° olduğunu kullanmamış.','bilgi')],
 istenen='x = m(ABC) açısının ölçüsü.',
 ip=['Üçgenin köşelerinden biri çemberin neresine bakıyor?'],
 bilgi=[CAP],
 ad=[A('Dik açıyı bul','Halat havuzun merkezinden geçtiği için [AB] çaptır; çapı gören C açısı 90° dir.','m(ACB) = 90°'),A('Üçgenin açılarını yaz','Üçgenin iç açıları toplamı 180° dir.','34° + x + 90° = 180°'),A('x değerini bul','Eşitlikten x çekilir.','x = 180° − 124° = 56°')],
 puf='Çap görünce çevre açıyı 90° al; üçgende kalan iki açının toplamı 90° olur.',sekil=SK2)

# ===== 03 · teğet–kiriş açısı · orta =====
kartla('K-GCA-03','Teğet–kiriş açısı','Teğet–kiriş açısı aynı yayı gören çevre açıya eşittir; bir doğru açısı 180° den tamamlanarak diğer teğet–kiriş açısı bulunur.','Teğet–kiriş açısını yayın kendisi sanmak; 180° tamamlamasını yanlış açıyla yapmak.','orta',3,'ge-ca-teget','Teğet–kiriş açısı ve teğet')
A3=(0,-r); T3=(-2.8,-r); D3=(2.8,-r)
B3=add(A3,mul((cos(radians(130)),sin(radians(130))),2*r*sin(radians(130)))); C3=add(A3,mul((cos(radians(70)),sin(radians(70))),2*r*sin(radians(70))))
ok(ln(B3),r); ok(ln(C3),r)
ok(ang(A3,T3,B3),50); ok(ang(A3,B3,C3),60); ok(ang(B3,A3,C3),70); ok(ang(C3,A3,B3),50)
assert 180-70==110 and 50+70==120
f=F(); f.circ(O,r); f.line(T3,D3); f.line(A3,B3); f.line(A3,C3); f.line(B3,C3)
f.arc(A3,T3,B3,.6,'$50^\\circ$',1.02); f.arc(A3,B3,C3,.4,'$60^\\circ$',.78); f.arc(B3,A3,C3,.5,'$x$',.8)
f.vl('T',T3,(-1,0),.3); f.vl('D',D3,(1,0),.3); f.vl('A',A3,(0,-1),.3); f.vl('B',B3,sub(B3,O),.3); f.vl('C',C3,sub(C3,O),.3)
SK3=f.svg()
q('0003',tipId='ge-ca-teget',tip='Teğet–kiriş açısı ve teğet',z='orta',alt='Teğet–Kiriş Açısı',kaz='Teğet–kiriş açısını çevre açıya eşitleyerek bir üçgenin açısını bulur.',
 kart='K-GCA-03 (teğet–kiriş) · TAB = 50°, BAC = 60°',
 metin='Şekilde [TD], çembere A noktasında teğet olan doğrudur. B ve C noktaları çember üzerindedir ve ABC bir üçgendir. Teğet ile kenarların yaptığı açılar şekilde gösterilmiştir. Şekil ölçekli değildir.\nBuna göre, x = m(ABC) kaç derecedir?',
 dogru=70,yan=[(50,'Teğet ile kiriş arasındaki 50° lik açıyı x ile eşit sanmış.','bilgi'),(60,'x yerine verilen m(BAC) = 60° açısını yazmış.','dikkat'),(110,'DAC açısını (70°) bulmuş ama x’i onun bütünleri (180° − 70°) sanmış.','bilgi'),(120,'50° ile 70° yi toplayıp 120° bulmuş; x in tek bir teğet–kiriş açısına eşit olduğunu bilmemiş.','bilgi')],
 istenen='x = m(ABC) açısının ölçüsü.',
 ip=['T, A, D doğrusal olduğundan A köşesindeki üç açının toplamı kaç derecedir? Kalan açı hangi yayı görüyor?'],
 bilgi=[TEGK],
 ad=[A('Kalan açıyı bul','T, A ve D doğrusal olduğundan A noktasındaki üç açının toplamı 180° dir.','m(DAC) = 180° − 50° − 60° = 70°'),A('Aynı yayı gören açıyı bul','DAC teğet–kiriş açısı ile ABC çevre açısı aynı AC yayını görür.','m(ABC) = m(DAC)'),A('x değerini yaz','Teğet–kiriş açısı çevre açıya eşittir.','x = 70°')],
 puf='Teğet–kiriş açısı gördüğü yayı gören çevre açıya eşittir; teğet doğrusunda açılar 180° e tamamlanır.',sekil=SK3)

# ===== 04 · iç açı · kolay =====
kartla('K-GCA-04','İç açı (kirişler)','İki kirişin kesişimindeki açı, gördüğü iki yayın toplamının yarısıdır; bilinen açıdan eksik yay geriye doğru bulunur.','Yayları toplamak yerine çıkarmak; açıyı iki katına çıkarmayı unutmak; eksik yaya toplamı eklemek.','kolay',3,'ge-ca-ic-dis','İç ve dış açı (yaylar)')
A4=pc(O,r,90); C4=pc(O,r,180); B4=pc(O,r,280); D4=pc(O,r,330); E4=inter(A4,B4,C4,D4)
ok(ang(E4,A4,C4),70); assert (90+50)//2==70 and 2*70-90==50 and 90-70==20 and 2*70==140 and 2*70+90==230
f=F(); f.circ(O,r); f.line(A4,B4); f.line(C4,D4); f.oarc(O,r,90,180,'very thick,vurgu'); f.oarc(O,r,280,330,'very thick,vurgu')
f.node(pc(O,r-.5,135),'$90^\\circ$'); f.node(pc(O,r-.45,305),'$y$')
f.arc(E4,A4,C4,.3,'$70^\\circ$',.85)
vlab(f,'A',A4); vlab(f,'B',B4); vlab(f,'C',C4); vlab(f,'D',D4); f.node(add(E4,(.3,.12)),'$E$')
SK4=f.svg()
q('0004',tipId='ge-ca-ic-dis',tip='İç ve dış açı (yaylar)',z='kolay',alt='İç Açı',kaz='Çemberin içinde kesişen kirişlerin açısı ile bir yay verildiğinde eksik yayı bulur.',
 kart='K-GCA-04 (iç açı) · AEC = 70°, AC = 90°, BD yayı sorulur',
 metin='Şekilde bir çemberin [AB] ve [CD] kirişleri E noktasında kesişmektedir. Kalın gösterilen AC yayının ölçüsü ile AEC açısının ölçüsü şekilde verilmiş, kalın gösterilen BD yayının ölçüsü y ile gösterilmiştir. Şekil ölçekli değildir.\nBuna göre, y kaç derecedir?',
 dogru=50,yan=[(20,'Açıyı yaydan çıkarıp 90° − 70° = 20° bulmuş; iç açı kuralını (yayların toplamı) uygulamamış.','bilgi'),(70,'Açının ölçüsünü doğrudan BD yayı sanmış.','bilgi'),(140,'Yalnız açıyı iki katına çıkarıp (140°) AC yayını çıkarmayı unutmuş.','islem'),(230,'Eşitlikte AC yayını çıkarmak yerine eklemiş: 140° + 90° = 230°.','islem')],
 istenen='BD yayının ölçüsü y (derece).',
 ip=['AEC açısı hangi iki yayı görüyor? Bu açı ile yaylar arasındaki bağıntıyı yazıp y yi çekmeye çalış.'],
 bilgi=[ICA],
 ad=[A('Bağıntıyı yaz','AEC açısı AC ve BD yaylarını görür; açı, iki yayın toplamının yarısıdır.','70° = (90° + y) ÷ 2'),A('Yayların toplamını bul','Eşitliğin iki yanını 2 ile çarp.','90° + y = 140°'),A('y değerini bul','AC yayını çıkar.','y = 140° − 90° = 50°')],
 puf='İç açıda açı ile yaylar arasındaki bağıntıyı yaz; bilinmeyen yayı eşitlikten çek.',sekil=SK4)

# ===== 05 · dış açı · orta =====
kartla('K-GCA-05','Dış açı (iki kesen)','Çemberin dışında iki kesenin yaptığı açı, büyük yay ile küçük yayın farkının yarısıdır.','Yayları toplamak; yalnız büyük yayı yarılamak; farkı yarılamayı unutmak.','orta',3,'ge-ca-ic-dis','İç ve dış açı (yaylar)')
rr=1.5
A5=pc(O,rr,30); B5=pc(O,rr,140); C5=pc(O,rr,-10); D5=pc(O,rr,250); P5=inter(A5,B5,C5,D5)
assert dist(P5,A5)<dist(P5,B5) and dist(P5,C5)<dist(P5,D5) and ln(P5)>rr
ok(ang(P5,A5,C5),35); assert (110-40)//2==35 and 110//2==55 and 110-40==70 and (110+40)//2==75
f=F(); f.circ(O,rr); f.line(P5,B5); f.line(P5,D5); f.oarc(O,rr,-10,30,'very thick,vurgu'); f.oarc(O,rr,140,250,'very thick,vurgu')
f.node(pc(O,rr-.5,10),'$40^\\circ$'); f.node(pc(O,rr-.5,195),'$110^\\circ$')
f.arc(P5,A5,C5,.8,'$x$',1.25)
vlab(f,'A',A5); vlab(f,'B',B5); vlab(f,'C',C5); vlab(f,'D',D5); f.node(add(P5,(.3,0)),'$P$')
SK5=f.svg()
q('0005',tipId='ge-ca-ic-dis',tip='İç ve dış açı (yaylar)',z='orta',alt='Dış Açı',kaz='Çemberin dışında kesişen iki kesenin açısını gördüğü yaylardan hesaplar.',
 kart='K-GCA-05 (dış açı) · yaylar 110° ve 40°',
 metin='Şekilde P noktasından çıkan iki kesen, çemberi A, B ve C, D noktalarında kesmektedir. P ye yakın olan AC yayı ile uzak olan BD yayının ölçüleri şekilde gösterilmiştir. Şekil ölçekli değildir.\nBuna göre, x = m(APC) kaç derecedir?',
 dogru=35,yan=[(55,'Yalnız büyük yayı yarılamış: 110° ÷ 2 = 55°.','dikkat'),(70,'Yayların farkını almış ama ikiye bölmeyi unutmuş.','islem'),(75,'Dış açıda yayları toplamış: (110° + 40°) ÷ 2 = 75°; bu, iç açı kuralıdır.','bilgi'),(150,'İki yayı toplayıp ikiye bölmeyi de unutmuş.','islem')],
 istenen='x = m(APC) açısının ölçüsü.',
 ip=['Köşe çemberin dışında olunca açı hangi yaylara bağlı?'],
 bilgi=[DISA],
 ad=[A('Yayları belirle','Açının gördüğü büyük yay BD, küçük yay AC dir.','BD = 110°, AC = 40°'),A('Farkı al','Dış açı, iki yayın farkının yarısıdır.','x = (110° − 40°) ÷ 2'),A('Hesapla','Fark 70°, yarısı 35° dir.','x = 35°')],
 puf='Açının köşesi çemberin dışındaysa büyük yaydan küçük yay çıkarılır ve ikiye bölünür.',sekil=SK5)

# ===== 06 · kirişler dörtgeni · orta =====
kartla('K-GCA-06','Kirişler dörtgeni, dış açı','Karşılıklı açılar bütünler olduğundan x bulunur; bir köşenin dış açısı, karşısındaki iç açıya eşittir.','Karşılıklı açıları eşit sanmak; dış açı yerine iç açıyı vermek; x değerini verip bırakmak.','orta',4,'ge-ca-dortgen','Kirişler dörtgeni')
A6=pc(O,r,200); B6=pc(O,r,270); C6=pc(O,r,20); D6=pc(O,r,130)
x6=25; assert (4*x6+10)+(2*x6+20)==180
ok(ang(A6,B6,D6),110); ok(ang(C6,B6,D6),70)
E6=add(C6,mul(un(sub(C6,D6)),1.0)); ok(ang(C6,B6,E6),110)
assert 4*5+10==30 and 180-30==150 and 2*x6+20==70
f=F(); f.circ(O,r); f.poly([A6,B6,C6,D6]); f.line(C6,E6)
f.arc(A6,B6,D6,.45,'$(4x+10)^\\circ$',1.15); f.arc(C6,B6,D6,.5,'$(2x+20)^\\circ$',1.3)
vlab(f,'A',A6); vlab(f,'B',B6); vlab(f,'D',D6); f.vl('C',C6,(.3,-1),.3); f.node(add(E6,(.3,-.1)),'$E$')
SK6=f.svg()
q('0006',tipId='ge-ca-dortgen',tip='Kirişler dörtgeni',z='orta',alt='Kirişler Dörtgeni',kaz='Kirişler dörtgeninde karşılıklı açıların bütünlüğünden bilinmeyeni bulup dış açıyı hesaplar.',
 kart='K-GCA-06 (kirişler dörtgeni) · (4x+10)° ve (2x+20)°',
 metin='Şekilde köşeleri çember üzerinde olan ABCD dörtgeni verilmiştir. [DC] doğru parçası C noktasından sonra E noktasına kadar uzatılmıştır. A ve C köşelerindeki iç açıların ölçüleri şekilde x türünden verilmiştir. Şekil ölçekli değildir.\nBuna göre, m(BCE) kaç derecedir?',
 dogru=110,yan=[(25,'x değerini bulup soruyu orada bırakmış; istenen m(BCE) dir.','dikkat'),(30,'Karşılıklı açıları eşit sanıp 4x + 10 = 2x + 20 → x = 5 bulmuş, m(BCE) = 4x + 10 = 30 yazmış.','bilgi'),(70,'m(BCD) = 2x + 20 = 70° iç açısını bulup dış açı olan m(BCE) ye geçmemiş.','dikkat'),(150,'Hatalı x = 5 ile 180° − 30° = 150° bulmuş.','bilgi')],
 istenen='m(BCE) dış açısının ölçüsü.',
 ip=['Kirişler dörtgeninde karşılıklı açılar arasındaki ilişkiyi yaz.'],
 bilgi=[DORT],
 ad=[A('x değerini bul','Karşılıklı A ve C açılarının toplamı 180° dir.','4x + 10 + 2x + 20 = 180 → 6x = 150 → x = 25'),A('İç açıları yaz','x = 25 yerine konur.','m(BAD) = 110° · m(BCD) = 70°'),A('Dış açıya geç','D, C, E doğrusal olduğundan BCE açısı BCD nin bütünleridir.','m(BCE) = 180° − 70° = 110°')],
 puf='Kirişler dörtgeninde karşılıklı açıları 180° e tamamla; doğrusal açıları da 180° e tamamlamayı unutma.',sekil=SK6)

# ===== 07 · merkez, ikizkenar, çevre açı · zor =====
kartla('K-GCA-07','Yarıçaplar ve merkez açı','OA = OB = OC olduğundan her yarıçap çifti ikizkenar üçgen kurar; taban açılarından ABC bulunur, merkez açı onun iki katıdır.','Taban açısıyla tepe açısını karıştırmak; çevre açıyı merkez açıya eşit almak; ters (dış) merkez açıyı vermek.','zor',4,'ge-ca-merkez-cevre','Merkez açı ve çevre açı')
A7=pc(O,r,200); B7=pc(O,r,300); C7=pc(O,r,50)
ok(ang(O,A7,B7),100); ok(ang(O,B7,C7),110); ok(ang(O,A7,C7),150)
ok(ang(A7,O,B7),40); ok(ang(C7,O,B7),35); ok(ang(B7,A7,C7),75)
assert 40+35==75 and 2*75==150 and 360-150==210
f=F(); f.circ(O,r); f.line(O,A7); f.line(O,B7); f.line(O,C7); f.line(A7,B7); f.line(C7,B7); f.dot(O)
f.arc(A7,O,B7,.75,'$40^\\circ$',1.25); f.arc(C7,O,B7,.7,'$35^\\circ$',1.2); f.arc(O,A7,C7,.4,'$x$',.7)
vlab(f,'A',A7); vlab(f,'B',B7); vlab(f,'C',C7); f.node((-.1,-.3),'$O$')
SK7=f.svg()
q('0007',tipId='ge-ca-merkez-cevre',tip='Merkez açı ve çevre açı',z='zor',alt='Merkez Açı',kaz='Yarıçapların ikizkenar üçgenlerinden ABC açısını bulup aynı yayı gören merkez açıya geçer.',
 kart='K-GCA-07 (yarıçaplar, merkez açı) · OAB = 40°, OCB = 35°',
 metin='Şekilde O merkezli çemberin üzerinde A, B ve C noktaları ile O noktasını bu noktalara bağlayan yarıçaplar verilmiştir. [AB] ve [CB] kirişleri çizilmiş, O noktası ABC üçgeninin içindedir. Şekil ölçekli değildir.\nBuna göre, x = m(AOC) kaç derecedir?',
 dogru=150,yan=[(75,'m(ABC) = 75° yi bulmuş ama aynı yayı gören merkez açıyı iki kat almayı unutmuş.','dikkat'),(100,'Yalnız m(AOB) = 180° − 2 × 40° = 100° yi bulup bırakmış.','dikkat'),(110,'Yalnız m(BOC) = 180° − 2 × 35° = 110° yi bulup bırakmış.','dikkat'),(210,'Merkez açıyı doğru bulup (150°) ardından 360° ye tamamlayarak ters yayı vermiş.','dikkat')],
 istenen='x = m(AOC) merkez açısının ölçüsü.',
 ip=['Yarıçaplarla hangi ikizkenar üçgenler oluşuyor?'],
 bilgi=[IKIZ,MERK],
 ad=[A('Taban açılarını yaz','OA = OB olduğundan OBA açısı 40°, OC = OB olduğundan OBC açısı 35° dir.','m(OBA) = 40° · m(OBC) = 35°'),A('ABC açısını bul','OB ışını B köşesindeki açıyı iki parçaya ayırır.','m(ABC) = 40° + 35° = 75°'),A('Merkez açıya geç','AC yayını gören merkez açı, çevre açının iki katıdır.','x = 2 × 75° = 150°'),A('Kontrol et','Üç merkez açının toplamı 360° olmalıdır.','100° + 110° + 150° = 360°')],
 puf='Merkezi köşe alan ve kenarları yarıçap olan üçgen ikizkenardır; taban açılarından çevre açıyı kurup iki katını al.',sekil=SK7)

# ===== 08 · saat kadranı, kirişler dörtgeni · orta =====
kartla('K-GCA-08','Eşit yaylı çemberde dörtgen','Çember eşit yaylara bölündüğünde her yay aynı ölçüdür; dörtgenin açısı karşısındaki yayın yarısıdır.','Yay sayısını yanlış saymak; açıyı yayın kendisi almak; karşı köşenin açısını vermek.','orta',3,'ge-ca-dortgen','Kirişler dörtgeni','hikâyeli')
def sa(h): return pc(O,r,90-30*h)
V8={h:sa(h) for h in (12,2,5,9)}
ok(ang(V8[5],V8[2],V8[9]),75); ok(ang(V8[12],V8[2],V8[9]),105); ok(ang(V8[2],V8[12],V8[5]),105); ok(ang(V8[9],V8[12],V8[5]),75)
assert 5*30+0==150 and 2*30==60 and 7*30==210
f=F(); f.circ(O,r); f.poly([V8[12],V8[2],V8[5],V8[9]])
for h in range(1,13):
    f.node(pc(O,r+.3,90-30*h),f'\\small {h}')
for h in V8: f.dot(V8[h])
f.arc(V8[5],V8[2],V8[9],.4,'$x$',.7)
SK8=f.svg()
q('0008',tipId='ge-ca-dortgen',tip='Kirişler dörtgeni',z='orta',alt='Eşit Yaylı Çember',kaz='Eşit yaylara bölünmüş çemberde yay sayısından kirişler dörtgeninin bir açısını bulur.',kalip='hikâyeli',
 kart='K-GCA-08 (saat kadranı, dörtgen) · 12, 2, 5, 9',
 metin='Dairesel bir duvar saatinin kadranında rakamlar eşit aralıklarla dizilmiştir. Bir tasarımcı, 12, 2, 5 ve 9 rakamlarının bulunduğu noktaları sırayla birleştirerek kadranın içine bir dörtgen çizmiştir. Şekilde dörtgenin 5 rakamındaki köşesinin açısı x ile gösterilmiştir.\nBuna göre, x kaç derecedir?',
 dogru=75,yan=[(60,'12 ile 2 arasındaki yayı (60°) bulup bu yayı x sanmış; x başka bir yayı görür.','dikkat'),(105,'Karşı köşedeki (2 rakamındaki) açıyı bulmuş: gördüğü yay 210° idi.','dikkat'),(150,'x açısının gördüğü yayı (150°) bulup yarılamayı unutmuş.','islem'),(210,'Karşı yayın (7 aralık × 30°) ölçüsünü yazmış; açı bu yayın yarısıdır.','islem')],
 istenen='x açısının ölçüsü.',
 ip=['Saat kadranında iki rakam arasındaki yay kaç derecedir? x açısı hangi yayı görüyor ve bu yay hangi köşelerden geçmiyor?'],
 bilgi=[DORT,MERK],
 ad=[A('Bir aralığın yayını bul','Kadranda 12 eşit aralık vardır; tam çember 360° dir.','360° ÷ 12 = 30°'),A('x in gördüğü yayı bul','5 rakamındaki köşe, 9 → 12 → 2 yayını görür (bu yay 5 i içermez): 9 dan 12 ye 3 aralık, 12 den 2 ye 2 aralık.','5 aralık × 30° = 150°'),A('Çevre açıyı hesapla','Çevre açı gördüğü yayın yarısıdır.','x = 150° ÷ 2 = 75°')],
 puf='Eşit bölünmüş çemberde önce bir aralığın derecesini bul; çevre açı, karşısındaki aralıkların toplamının yarısıdır.',sekil=SK8)

# ===== 09 · teğet, yarıçap, doğrusallık · zor =====
kartla('K-GCA-09','Teğet ve merkezden geçen kesen','Teğet yarıçapa diktir; dik üçgenden merkez açı, ikizkenar üçgenden taban açısı bulunur.','Teğet–yarıçap dikliğini görmemek; ikizkenar üçgenin taban açısı yerine tepe açısını vermek; merkez açıyı x sanmak.','zor',4,'ge-ca-teget','Teğet–kiriş açısı ve teğet','hikâyeli')
r9=1.7; d9=r9/sin(radians(28)); P9=(-d9,0); B9=(-r9,0); C9=(r9,0); A9=pc(O,r9,118)
ok(ang(P9,A9,C9),28); assert abs((A9[0]-P9[0])*A9[0]+(A9[1]-P9[1])*A9[1])<1e-9
ok(ang(O,P9,A9),62); ok(ang(B9,A9,C9),59); assert (180-62)//2==59 and 62//2==31 and 180-62==118 and 90-31==59
f=F(); f.circ(O,r9); f.line(P9,C9); f.line(P9,A9); f.line(O,A9); f.line(A9,B9); f.dot(O)
f.arc(P9,A9,C9,1.0,'$28^\\circ$',1.6); f.arc(B9,A9,C9,.5,'$x$',.85)
f.vl('P',P9,(-1,0),.3); f.vl('A',A9,sub(A9,O),.3); f.vl('B',B9,(-1,-.5),.3); f.vl('C',C9,(1,0),.3); f.node((.18,-.27),'$O$')
SK9=f.svg()
q('0009',tipId='ge-ca-teget',tip='Teğet–kiriş açısı ve teğet',z='zor',alt='Teğet ve Yarıçap',kaz='Teğet–yarıçap dikliğinden merkez açıyı, ikizkenar üçgenden taban açısını bulur.',kalip='hikâyeli',
 kart='K-GCA-09 (teğet, merkezden geçen kesen) · APB = 28°',
 metin='Dairesel bir göletin merkezi O dur. Gölün dışındaki P noktasından başlayan bir patika, gölün kıyısında A noktasına dokunacak biçimde teğet geçmektedir. P den başlayan ikinci bir kanal, gölün kıyısındaki B noktasında göle girip merkezden geçerek C noktasında çıkar. Şekil ölçekli değildir.\nBuna göre, x = m(ABC) kaç derecedir?',
 dogru=59,yan=[(28,'Verilen m(APB) = 28° yi x ile eşit sanmış.','dikkat'),(31,'m(ACB) = 31° çevre açısını bulup x yerine yazmış.','dikkat'),(62,'m(AOB) = 62° merkez açısını bulup x yerine yazmış.','dikkat'),(118,'İkizkenar üçgenin tepe açısının bütünlerini (180° − 62°) alıp 2 ye bölmeyi unutmuş.','islem')],
 istenen='x = m(ABC) açısının ölçüsü.',
 ip=['O’yu A ile birleştiren yarıçap teğetle hangi açıyı yapıyor? Sonra OAB üçgeninin kenarlarına bak.'],
 bilgi=[TEGY,IKIZ],
 ad=[A('Dik açıyı bul','Teğet, değme noktasındaki yarıçapa diktir: OA ⊥ PA. POA dik üçgenindeki P açısı 28° dir.','m(AOP) = 90° − 28° = 62°'),A('Merkez açıyı yaz','P, B, O doğrusal olduğundan AOB açısı da 62° dir (B, P ile O arasındadır).','m(AOB) = 62°'),A('İkizkenar üçgene bak','OA = OB yarıçaptır; OAB üçgeninin taban açıları eşittir.','2x + 62° = 180°'),A('x değerini bul','Eşitlikten x çekilir.','x = 118° ÷ 2 = 59°')],
 puf='Teğet görünce yarıçapla dik açı kur; yarıçap ikizkenar üçgenleri taban açısı sorusuna çevirir.',sekil=SK9)

# ===== 10 · çapı gören + kirişler dörtgeni · orta =====
kartla('K-GCA-10','Çap ve kirişler dörtgeni','Karşılıklı açıların bütünlüğünden ABC bulunur; çapı gören açı 90° olduğundan ABC üçgeninden CAB hesaplanır.','Karşılıklı açıları eşit almak; 90° yi kullanmamak; ara açıyı (65°) cevap sanmak.','orta',3,'ge-ca-cap','Çapı gören çevre açı')
A10=pc(O,r,180); B10=pc(O,r,0); C10=pc(O,r,50); D10=pc(O,r,120)
ok(ang(A10,B10,C10),25); ok(ang(C10,A10,B10),90); ok(ang(B10,A10,C10),65); ok(ang(D10,A10,C10),115)
assert 180-115==65 and 90-65==25 and 115-65==50
f=F(); f.circ(O,r); f.poly([A10,B10,C10,D10]); f.line(A10,C10); f.dot(O)
f.arc(D10,A10,C10,.3,'$115^\\circ$',.62); f.arc(A10,B10,C10,.9,'$x$',1.4)
f.vl('A',A10,(-1,-.3),.3); f.vl('B',B10,(1,-.3),.3); vlab(f,'C',C10); vlab(f,'D',D10); f.node((0,-.27),'$O$')
SK10=f.svg()
q('0010',tipId='ge-ca-cap',tip='Çapı gören çevre açı',z='orta',alt='Çap ve Dörtgen',kaz='Kirişler dörtgeninin karşılıklı açısından ABC yi, çapı gören açıdan CAB yi bulur.',
 kart='K-GCA-10 (çap, kirişler dörtgeni) · ADC = 115°',
 metin='Şekilde O merkezli çemberde [AB] çaptır; C ve D noktaları çember üzerindedir. ABCD dörtgeninin köşegenlerinden yalnız [AC] çizilmiştir. Şekil ölçekli değildir.\nBuna göre, x = m(CAB) kaç derecedir?',
 dogru=25,yan=[(50,'m(ADC) − m(ABC) = 115° − 65° = 50° işlemini yapmış; fark almanın bir anlamı yok.','islem'),(65,'m(ABC) = 65° yi bulup bırakmış; x, A köşesindeki açıdır.','dikkat'),(90,'Çapı gören açıyı (C köşesinde, 90°) x sanmış.','dikkat'),(115,'Verilen m(ADC) = 115° yi x ile eşit sanmış.','bilgi')],
 istenen='x = m(CAB) açısının ölçüsü.',
 ip=['ADC açısının karşısındaki köşeyi bul. Sonra ABC üçgeninde çap hangi özel açıyı oluşturuyor?'],
 bilgi=[CAP,DORT],
 ad=[A('Karşılıklı açıyı bul','ABCD kirişler dörtgeninde karşılıklı D ve B açıları bütünlerdir.','m(ABC) = 180° − 115° = 65°'),A('Dik açıyı yaz','[AB] çap olduğundan çapı gören ACB açısı 90° dir.','m(ACB) = 90°'),A('x değerini bul','ABC üçgeninde iç açılar toplamı 180° dir.','x = 180° − 90° − 65° = 25°')],
 puf='Kirişler dörtgeninde karşılıklı açıyı 180° e tamamla; çap varsa 90° lik bir üçgen kur ve kalan açıyı bul.',sekil=SK10)

bitir_geo('cemberaci','Çemberde Açı')
