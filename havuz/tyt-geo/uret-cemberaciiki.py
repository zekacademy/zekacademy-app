"""TYT Geometri · Çemberde Açı (2. paket) · 10 şekilli soru (kardeş yok, ipucu 1). Şekil koordinatları açılardan hesaplanır; her cevap ve çeldirici koordinattan ölçülen açıyla assert edilir."""
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
    P.yaz(os.path.join(GD,onek+'-1.json'),'/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/ciiki/bos-'+onek+'.json')
    tipler={}
    for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=TIPK[c['tipId']]))['kartlar'].append(c['id'])
    json.dump(dict(konu=konuad,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 TYT Geometri çıkmış soruları (yalnız mantık), MEB 9–10. sınıf geometri müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar',onek+'.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler))
P=Parti('cemberaciiki','Çemberde Açı','geo|Çemberde Açı',ders='TYT Geometri',idon='tytgeo')
P.k='geo|Çemberde Açı'; H.KONU='Çemberde Açı'
def ok(a,b,t=1e-6): assert abs(a-b)<t,(a,b)
r=1.9; O=(0,0)
def vlab(f,t,p,d=.3): f.vl(t,p,sub(p,O),d)
def dt(u,v): return u[0]*v[0]+u[1]*v[1]
TEGB=B('Dış noktadan çizilen teğetler','bir dış noktadan çembere çizilen iki teğetin değme noktasına kadar uzunlukları eşittir ve teğet, değme noktasındaki yarıçapa diktir. Örnek: P den çizilen teğetlerin değme noktaları T ve S ise |PT| = |PS| dir')
CEV=B('Çevre açı ve yay','bir çevre açının ölçüsü gördüğü yayın yarısıdır; aynı yayı gören çevre açılar eşittir. Örnek: 70° lik yayı gören her çevre açı 35° dir')
ICD=B('Kirişlerin ve kesenlerin açıları','çemberin içinde kesişen iki kirişin açısı gördüğü iki yayın toplamının yarısı, dışında kesişen iki doğrunun (kesen ya da teğet) açısı gördüğü büyük yay ile küçük yayın farkının yarısıdır. Örnek: yaylar 100° ve 30° olan dış açı 35° dir')
ESY=B('Eşit kiriş, eşit yay','çemberde eşit kirişler eşit yayları, eşit yaylar eşit çevre açıları görür; paralel iki kirişin arasında kalan yaylar eşittir. Örnek: |PQ| = |QR| ise PQ ve QR yayları eşittir')
KIR=B('Kirişler dörtgeni','köşeleri çember üzerinde olan dörtgende karşılıklı açıların toplamı 180° dir. Örnek: bir köşesi 95° ise karşısındaki köşe 85° dir')
DUZ=B('Düzgün çokgen ve çember','çember üzerindeki n köşe eşit aralıklıysa her yay 360° ÷ n dir. Örnek: eşit aralıklı 9 köşede her yay 40° dir')
CEVR=B('Çevrel çember','bir üçgenin üç köşesinden geçen çemberin merkezi, köşelere eşit uzaklıktadır; merkezi köşelere bağlayan yarıçaplar ikizkenar üçgenler oluşturur. Örnek: merkez açı 80° ise taban açıları 50° dir')
TEGK=B('Teğet–kiriş açısı','teğet ile kiriş arasındaki açı gördüğü yayın yarısıdır; aynı yayı gören çevre açıya eşittir. Örnek: gördüğü yay 90° ise açı 45° dir')
GEN1='Verilen bilgilerle önce hangi açıyı ya da yayı hesaplayabileceğini bul.'
GENP='Şekildeki her veriyi bir açıya ya da yaya çevir; sorulan açıya hangi bilgilerin bağlandığını adım adım yaz.'

# ===== 01 · iki teğet (kolay, hikâyeli) =====
kartla('K-GCI-01','Dış noktadan iki teğet','İki teğetin yaptığı açı ile değme noktalarını birleştiren yay ya da merkez açı arasında bir bağıntı vardır; çevre açı da bu yayla bağlıdır.','Çevre açıyı merkez açıya eşit almak; köşenin hangi yayda olduğuna bakmadan yarılamak; teğet açısını cevap sanmak.','kolay',3,'ge-ci-iki-teget','İki teğet ve çember','hikâyeli')
r1=1.5; hp=25; d1=r1/sin(radians(hp)); P1=(-d1,0)
A1=pc(O,r1,180-(90-hp)); B1=pc(O,r1,180+(90-hp)); C1=pc(O,r1,0)
ok(dt(sub(P1,A1),sub(O,A1)),0); ok(dt(sub(P1,B1),sub(O,B1)),0)
ok(ang(P1,A1,B1),50); ok(ang(O,A1,B1),130); ok(ang(C1,A1,B1),65)
assert 130//2==65 and 50//2==25 and 180-65==115 and 130==360-90-90-50
f=F(); f.circ(O,r1); f.line(P1,A1); f.line(P1,B1); f.line(C1,A1); f.line(C1,B1)
f.arc(P1,A1,B1,.8,'$50^\\circ$',1.3); f.arc(C1,A1,B1,.4,'$x$',.72)
f.vl('P',P1,(-1,0),.3); vlab(f,'A',A1); vlab(f,'B',B1); vlab(f,'C',C1)
SK1=f.svg()
q('0001',tipId='ge-ci-iki-teget',tip='İki teğet ve çember',z='kolay',alt='İki Teğet',kaz='Dış noktadan çizilen iki teğetin açısından yay ve çevre açıyı hesaplar.',kalip='hikâyeli',
 kart='K-GCI-01 (iki teğet) · P açısı 50°',
 metin='Dairesel bir havuzun dışındaki P noktasından havuza iki düz çit çekilmiştir; çitler havuza A ve B noktalarında teğettir. P noktasındaki açı şekilde verilmiştir. Havuz kenarındaki C noktası, A ile B arasındaki büyük yay üzerindedir ve C noktasından A ile B ye birer ip gerilmiştir. Şekil ölçekli değildir.\nBuna göre, x = m(ACB) kaç derecedir?',
 dogru=65,yan=[(25,'P açısının yarısını almış (25°); iki teğetin açısı ile çevre açı arasında bu ilişki yoktur.','bilgi'),(90,'Teğetin yarıçapa dik olduğunu görüp 90° yazmış.','dikkat'),(115,'C nin küçük yayda olduğunu varsayıp 180° − 65° = 115° bulmuş; C büyük yay üzerindedir.','dikkat'),(130,'Merkez açıyı (130°) bulup çevre açıya geçmemiş.','dikkat')],
 istenen='x = m(ACB) çevre açısının ölçüsü.',
 ip=['P deki açıyı kullanarak hangi dörtgeni kurabileceğini düşün.'],
 bilgi=[TEGB,CEV],
 ad=[A('Merkez açıyı bul','Teğetler değme noktalarındaki yarıçaplara diktir; çemberin merkezi O, A, P, B köşeli dörtgenin iç açılarını tamamlar.','m(AOB) = 360° − 90° − 90° − 50° = 130°'),A('Gördüğü yayı belirle','C büyük yay üzerinde olduğundan ACB açısı, ölçüsü merkez açıya eşit olan küçük AB yayını görür.','küçük yay AB = 130°'),A('Çevre açıyı yaz','Çevre açı, gördüğü yayın yarısıdır.','x = 130° ÷ 2 = 65°')],
 puf='Aradığın açıya ulaşmak için ara açıları sırayla yaz.',sekil=SK1)

# ===== 02 · aynı yayı gören açılar · orta =====
kartla('K-GCI-02','Köşegenler ve aynı yayı gören açılar','Çemberde aynı yayı gören çevre açılar eşit olduğundan, köşegenlerin oluşturduğu üçgenlerde açılar bir yerden başka yere taşınır.','Açıyı yayın kendisi sanmak; komşu (bütünler) açıyı vermek; açıları birbirinden çıkarmak.','orta',3,'ge-ci-ayni-yay','Aynı yayı gören açılar','hikâyeli')
A2=pc(O,r,150); B2=pc(O,r,80); C2=pc(O,r,0); D2=pc(O,r,260); E2=inter(A2,C2,B2,D2)
ok(ang(D2,A2,B2),35); ok(ang(A2,C2,D2),50); ok(ang(A2,B2,C2),40); ok(ang(B2,C2,D2),50)
ok(ang(E2,B2,C2),95); ok(ang(E2,A2,B2),85); ok(ang(C2,A2,B2),35)
assert 180-50-35==95 and 180-95==85 and 50-35==15 and 2*35==70 and 2*50==100
f=F(); f.circ(O,r); f.poly([A2,B2,C2,D2]); f.line(A2,C2); f.line(B2,D2)
f.arc(D2,A2,B2,.55,'$35^\\circ$',1.0); f.arc(A2,C2,D2,.5,'$50^\\circ$',.95); f.arc(E2,B2,C2,.3,'$x$',.58)
vlab(f,'A',A2); vlab(f,'B',B2); vlab(f,'C',C2); vlab(f,'D',D2); f.node(add(E2,(-.1,-.3)),'$E$')
SK2=f.svg()
q('0002',tipId='ge-ci-ayni-yay',tip='Aynı yayı gören açılar',z='orta',alt='Köşegenler',kaz='Aynı yayı gören çevre açıların eşitliğiyle köşegenlerin kesişim açısını hesaplar.',kalip='hikâyeli',
 kart='K-GCI-02 (köşegenler, aynı yay) · ADB = 35°, CAD = 50°',
 metin='Dairesel bir meydanın kenarına A, B, C ve D noktalarında dört direk dikilmiş, direkler birbirine teller ile bağlanmıştır. Köşegen teller [AC] ve [BD] E noktasında kesişmektedir. Tellerin A ve D direklerindeki ADB ve CAD açılarının ölçüleri şekilde verilmiştir. Şekil ölçekli değildir.\nBuna göre, x = m(BEC) kaç derecedir?',
 dogru=95,yan=[(15,'İki açının farkını almış (50° − 35°).','islem'),(70,'35° lik açıyı iki katına çıkarmış; açı yerine yayı yazmış.','islem'),(85,'Komşu açıyı (AEB) bulmuş; x onun bütünleyenidir.','dikkat'),(100,'50° lik açıyı iki katına çıkarıp yay ölçüsünü (100°) yazmış.','islem')],
 istenen='x = m(BEC) açısının ölçüsü.',
 ip=['BEC üçgeninin diğer iki açısına ulaşmaya çalış.'],
 bilgi=[CEV],
 ad=[A('Açıları taşı','DBC ile DAC açıları DC yayını, ACB ile ADB açıları AB yayını görür; aynı yayı gören açılar eşittir.','m(EBC) = 50° · m(ECB) = 35°'),A('BEC üçgenini yaz','Üçgenin iç açıları toplamı 180° dir.','x = 180° − 50° − 35° = 95°'),A('Kontrol et','AEB açısı, BEC açısını 180° e tamamlar ve gördüğü yaylar AB ile CD nin toplamının yarısıdır.','(70° + 100°) ÷ 2 = 85° · 85° + 95° = 180°')],
 puf='Her yeni bulduğun açıyı şekle işle; sonraki adımda onu kullan.',sekil=SK2)

# ===== 03 · paralel kirişler · zor =====
kartla('K-GCI-03','Paralel kirişler, yaylar','Paralel iki kirişin arasında kalan yaylar eşittir; çevre açılardan yaylar bulunup istenen açı yeniden çevre açı olarak yazılır.','Paralel kirişlerin yaylarını eşit saymamak; açıyı gördüğü yaya göre değil bir köşedeki açılara göre toplamak; yayı açı sanmak.','zor',5,'ge-ci-esit-yay','Eşit kiriş, eşit yay')
r3=2.3; A3=pc(O,r3,165); B3=pc(O,r3,15); C3=pc(O,r3,-65); D3=pc(O,r3,245)
ok(A3[1],B3[1]); ok(C3[1],D3[1])
ok(ang(D3,A3,B3),75); ok(ang(A3,C3,D3),25); ok(ang(A3,B3,C3),40); ok(ang(B3,A3,C3),65)
assert 150+80+50+80==360 and 80+50==130 and 130//2==65 and 2*75==150 and 2*25==50
f=F(); f.circ(O,r3); f.poly([A3,B3,C3,D3]); f.line(A3,C3); f.line(B3,D3); f.par(A3,B3); f.par(D3,C3)
f.arc(D3,A3,B3,.6,'$75^\\circ$',1.05); f.arc(A3,C3,D3,1.0,'$25^\\circ$',1.4); f.arc(B3,A3,C3,1.3,'$x$',1.7)
vlab(f,'A',A3); vlab(f,'B',B3); vlab(f,'C',C3); vlab(f,'D',D3)
SK3=f.svg()
q('0003',tipId='ge-ci-esit-yay',tip='Eşit kiriş, eşit yay',z='zor',alt='Paralel Kirişler',kaz='Paralel kirişler arasındaki eşit yayları ve çevre açıları kullanarak bir açıyı hesaplar.',
 kart='K-GCI-03 (paralel kirişler) · ADB = 75°, CAD = 25°',
 metin='Köşeleri bir çemberin üzerinde olan ABCD yamuğunda [AB] // [DC] dir. Yamuğun köşegenleri çizilmiş; D ve A köşelerindeki ADB ve CAD açılarının ölçüleri şekilde verilmiştir. Şekil ölçekli değildir.\nBuna göre, x = m(ABC) kaç derecedir?',
 dogru=65,yan=[(25,'Verilen m(CAD) = 25° yi x ile eşit sanmış.','dikkat'),(40,'BC yayını (80°) bulup yarılamış: m(BAC) = 40°; x başka bir yayı görür.','dikkat'),(75,'Verilen m(ADB) = 75° yi x ile eşit sanmış.','dikkat'),(130,'ADC yayının ölçüsünü (130°) bulup çevre açıya geçmemiş.','dikkat')],
 istenen='x = m(ABC) açısının ölçüsü.',
 ip=['Verilen iki açıdan hangi yayların ölçüsünü bulabilirsin?'],
 bilgi=[CEV,ESY],
 ad=[A('AB yayını bul','ADB açısı AB yayını görür; çevre açı yayın yarısıdır.','AB yayı = 2 × 75° = 150°'),A('CD yayını bul','CAD açısı CD yayını görür.','CD yayı = 2 × 25° = 50°'),A('Eşit yayları kullan','Paralel kirişlerin arasında kalan BC ve DA yayları eşittir; çemberin tamamı 360° dir.','BC = DA = (360° − 150° − 50°) ÷ 2 = 80°'),A('x değerini yaz','ABC açısı, B yi içermeyen ADC yayını görür.','x = (80° + 50°) ÷ 2 = 65°')],
 puf='Önce yayları, sonra yayları gören açıları yaz.',sekil=SK3)

# ===== 04 · teğet–kesen · orta =====
kartla('K-GCI-04','Teğet ve kesen','Dışarıdaki bir noktadan çizilen teğet ve kesenin açısı yaylarla bağlıdır; yaylar bulunduktan sonra çevre ya da teğet–kiriş açıları yazılır.','Büyük ve küçük yayı karıştırmak; farkı almadan toplamak; yayı açı sanmak.','orta',3,'ge-ci-teget-kesen','Teğet–kesen açısı')
r4=1.7; T4=pc(O,r4,90); A4=pc(O,r4,0); B4=pc(O,r4,260)
P4=inter(A4,B4,T4,add(T4,(-sin(radians(90)),cos(radians(90)))))
assert dist(P4,A4)<dist(P4,B4) and ln(P4)>r4 and dt(sub(P4,T4),T4)==dt(sub(P4,T4),T4) and abs(dt(sub(P4,T4),sub(T4,O)))<1e-9
ok(ang(P4,T4,A4),40); ok(ang(A4,T4,B4),85); ok(ang(T4,A4,B4),50); ok(ang(B4,T4,A4),45)
assert 2*40+90==170 and 360-90-170==100 and 100//2==50 and 170//2==85 and 90//2==45
f=F(); f.circ(O,r4); f.line(P4,T4); f.line(P4,B4); f.line(T4,A4); f.line(T4,B4); f.oarc(O,r4,0,90,'very thick,vurgu')
f.node(pc(O,1.45,45),'$90^\\circ$'); f.arc(P4,T4,A4,.9,'$40^\\circ$',1.3); f.arc(T4,A4,B4,.5,'$x$',1.2)
vlab(f,'T',T4); vlab(f,'A',A4); vlab(f,'B',B4); f.vl('P',P4,(1,.3),.3)
SK4=f.svg()
q('0004',tipId='ge-ci-teget-kesen',tip='Teğet–kesen açısı',z='orta',alt='Teğet ve Kesen',kaz='Teğet ile kesenin açısından yayları bulup bir çevre açıyı hesaplar.',
 kart='K-GCI-04 (teğet ve kesen) · P = 40°, TA yayı 90°',
 metin='Şekilde P noktasından çizilen [PT], çembere T noktasında teğettir. P den çizilen diğer doğru çemberi, P ye yakın olan A noktasında ve B noktasında kesmektedir. Kalın gösterilen TA yayının ölçüsü ile P noktasındaki açının ölçüsü şekilde verilmiştir. Şekil ölçekli değildir.\nBuna göre, x = m(ATB) kaç derecedir?',
 dogru=50,yan=[(40,'Verilen m(TPA) = 40° yi x ile eşit sanmış.','dikkat'),(45,'m(TBA) = 90° ÷ 2 = 45° yi bulup x yerine yazmış.','dikkat'),(85,'m(TAB) = 170° ÷ 2 = 85° yi bulup x yerine yazmış.','dikkat'),(90,'TA yayının ölçüsünü (90°) açı sanmış.','dikkat')],
 istenen='x = m(ATB) açısının ölçüsü.',
 ip=['Önce çember üzerindeki yaylardan hangilerini bulabileceğine bak.'],
 bilgi=[ICD,TEGK],
 ad=[A('BT yayını bul','Dış açı, uzak yay ile yakın yayın farkının yarısıdır.','40° = (BT − 90°) ÷ 2 → BT = 170°'),A('AB yayını bul','Üç yay çemberi tamamlar.','AB = 360° − 90° − 170° = 100°'),A('x değerini yaz','ATB çevre açısı, T yi içermeyen AB yayını görür.','x = 100° ÷ 2 = 50°')],
 puf='Hangi yayın bilindiğini, hangisinin bilinmediğini ayrı ayrı yaz.',sekil=SK4)

# ===== 05 · düzgün beşgen · kolay, hikâyeli =====
kartla('K-GCI-05','Eşit aralıklı noktalar','Çember üzerinde eşit aralıklı noktalar çemberi eşit yaylara böler; bir yaydan çevre açı bulunur.','Yay sayısını yanlış saymak; yayı açı sanmak; çokgenin iç açısıyla karıştırmak.','kolay',3,'ge-ci-duzgun','Düzgün çokgen ve çember','hikâyeli')
V5=[pc(O,r,90-72*k) for k in range(5)]; A5,B5,C5,D5,E5=V5
ok(ang(A5,C5,D5),36)
assert 360//5==72 and 72//2==36 and 2*36==72 and 108==3*36 and 2*72==144
f=F(); f.circ(O,r); f.line(A5,C5); f.line(A5,D5)
for p in V5: f.dot(p)
f.arc(A5,C5,D5,.75,'$x$',1.1)
vlab(f,'A',A5); vlab(f,'B',B5); vlab(f,'C',C5); vlab(f,'D',D5); vlab(f,'E',E5)
SK5=f.svg()
q('0005',tipId='ge-ci-duzgun',tip='Düzgün çokgen ve çember',z='kolay',alt='Eşit Aralıklı Noktalar',kaz='Eşit aralıklı noktalarla bölünmüş çemberde yay sayısından bir çevre açıyı bulur.',kalip='hikâyeli',
 kart='K-GCI-05 (eşit aralıklı 5 nokta) · CAD açısı',
 metin='Yuvarlak bir bahçenin kenarına, birbirine eşit aralıklarla A, B, C, D ve E ile adlandırılan beş ışıklı direk dikilmiştir. A direğinden C ve D direklerine birer tel gerilmiş, bu iki telin arasındaki açı x ile gösterilmiştir. Şekil ölçekli değildir.\nBuna göre, x kaç derecedir?',
 dogru=36,yan=[(18,'Yayı iki kez yarılamış (72° ÷ 4).','islem'),(72,'Bir aralığın yayını (72°) x sanmış; çevre açı yayın yarısıdır.','dikkat'),(108,'Düzgün beşgenin iç açısını (108°) yazmış.','bilgi'),(144,'İki aralığın yayını (144°) açı sanmış.','dikkat')],
 istenen='x açısının ölçüsü.',
 ip=['Direkler arasındaki her bir yay kaç derecedir?'],
 bilgi=[DUZ,CEV],
 ad=[A('Bir yayı bul','Beş eşit yay çemberi tamamlar.','360° ÷ 5 = 72°'),A('x in gördüğü yayı belirle','C ile D arasında tek bir aralık vardır.','CD yayı = 72°'),A('Çevre açıyı yaz','Çevre açı, gördüğü yayın yarısıdır.','x = 72° ÷ 2 = 36°')],
 puf='Sorulan açıyı parçalara ayırıp her parçayı ayrı bul.',sekil=SK5)

# ===== 06 · eşit kirişler, dörtgen · orta =====
kartla('K-GCI-06','Eşit kirişli dörtgen','Eşit kirişlerin kurduğu ikizkenar üçgenden ve aynı yayı gören açılardan, kirişler dörtgeninin bir köşesi bulunur.','İkizkenar üçgenin taban açısı yerine tepe açısını almak; karşı köşeyi vermek; ara açıları toplamamak.','orta',4,'ge-ci-esit-yay','Eşit kiriş, eşit yay')
A6=pc(O,r,200); B6=pc(O,r,280); C6=pc(O,r,0); D6=pc(O,r,90)
ok(ang(B6,A6,D6),55); ok(ang(B6,D6,C6),45); ok(ang(B6,A6,C6),100); ok(dist(A6,B6),dist(B6,C6))
ok(ang(C6,B6,A6),40); ok(ang(C6,A6,D6),55); ok(ang(C6,B6,D6),95); ok(ang(A6,B6,D6),85)
assert 55+45==100 and (180-100)//2==40 and 40+55==95 and 180-95==85
f=F(); f.circ(O,r); f.poly([A6,B6,C6,D6]); f.line(B6,D6); f.tick(A6,B6); f.tick(B6,C6)
f.arc(B6,A6,D6,.55,'$55^\\circ$',.95); f.arc(B6,D6,C6,.7,'$45^\\circ$',1.1); f.arc(C6,B6,D6,.4,'$x$',.7)
vlab(f,'A',A6); vlab(f,'B',B6); vlab(f,'C',C6); vlab(f,'D',D6)
SK6=f.svg()
q('0006',tipId='ge-ci-esit-yay',tip='Eşit kiriş, eşit yay',z='orta',alt='Eşit Kirişli Dörtgen',kaz='Eşit kirişlerden oluşan ikizkenar üçgen ve aynı yayı gören açılarla bir dörtgenin açısını bulur.',
 kart='K-GCI-06 (eşit kirişler, dörtgen) · ABD = 55°, DBC = 45°',
 metin='Şekilde ABCD dörtgeninin köşeleri bir çemberin üzerindedir ve |AB| = |BC| dir. [BD] köşegeni çizilmiş, ABD ve DBC açılarının ölçüleri şekilde verilmiştir. Şekil ölçekli değildir.\nBuna göre, x = m(BCD) kaç derecedir?',
 dogru=95,yan=[(40,'Yalnız ikizkenar üçgenin taban açısını (40°) bulup bırakmış.','dikkat'),(55,'m(ACD) = 55° yi bulup x yerine yazmış; x, iki açının toplamıdır.','dikkat'),(85,'Karşıt köşedeki m(BAD) = 85° yi bulmuş; x onun bütünleyenidir.','dikkat'),(100,'m(ABC) = 100° yi x sanmış.','dikkat')],
 istenen='x = m(BCD) açısının ölçüsü.',
 ip=['x i oluşturan açıların her birini ayrı ayrı bulmayı dene.'],
 bilgi=[ESY,KIR,CEV],
 ad=[A('B köşesindeki açıyı bul','BD, ABC açısının içinden geçer.','m(ABC) = 55° + 45° = 100°'),A('Taban açısını bul','|AB| = |BC| olduğundan ABC üçgeninin taban açıları eşittir.','m(BCA) = (180° − 100°) ÷ 2 = 40°'),A('Aynı yayı gören açıyı kullan','ACD ve ABD açıları AD yayını görür.','m(ACD) = 55°'),A('x değerini bul','BCA ve ACD açıları BCD açısını oluşturur.','x = 40° + 55° = 95°'),A('Kontrol et','Kirişler dörtgeninde karşılıklı açılar bütünlerdir.','m(BAD) = 85° · 85° + 95° = 180°')],
 puf='Eşit olan doğru parçalarını ve açıları belirleyerek başla.',sekil=SK6)

# ===== 07 · iki teğet ve çap · zor =====
kartla('K-GCI-07','Teğetler ve çap','İki teğetin eşitliği, teğet–kiriş açısı ve teğetin çapa dikliği birleştirilerek bir üçgenin bilinmeyen açısı bulunur.','Teğetlerden oluşan üçgeni ikizkenar saymamak; teğet–kiriş açısını çevre açıyla eşlememek; dik açıyı unutmak.','zor',4,'ge-ci-iki-teget','İki teğet ve çember')
r7=1.25; A7=(-r7,0); B7=(r7,0); C7=pc(O,r7,110)
tC=(-sin(radians(110)),cos(radians(110)))
E7=inter(C7,add(C7,tC),B7,(r7,1)); D7=inter(A7,C7,B7,(r7,1))
ok(dist(E7,B7),dist(E7,C7)); ok(ang(E7,B7,C7),70); ok(ang(D7,A7,B7),35); ok(E7[1],D7[1]/2); assert E7[1]>0 and D7[1]>E7[1]
ok(ang(A7,B7,C7),55)
assert (180-70)//2==55 and 90-55==35 and 90-70==20 and 180-55==125
f=F(); f.circ(O,r7); f.line(A7,D7); f.line(B7,D7); f.line(E7,C7); f.line(A7,B7); f.dot(O)
f.arc(E7,B7,C7,.32,'$70^\\circ$',.6); f.arc(D7,A7,B7,1.1,'$x$',1.5)
f.vl('A',A7,(-1,-.4),.3); f.vl('B',B7,(1,-1),.3); vlab(f,'C',C7); f.vl('E',E7,(1,0),.3); f.vl('D',D7,(.4,1),.3)
SK7=f.svg()
q('0007',tipId='ge-ci-iki-teget',tip='İki teğet ve çember',z='zor',alt='Teğetler ve Çap',kaz='Aynı noktadan çizilen teğetlerin eşitliği, teğet–kiriş açısı ve çapa dik teğetle bir üçgenin açısını bulur.',
 kart='K-GCI-07 (teğetler, çap) · E açısı 70°',
 metin='Şekilde [AB] çemberin çapıdır. E noktasından çizilen [EB] ve [EC], çembere sırasıyla B ve C noktalarında teğettir. A ve C noktalarından geçen doğru, B noktasındaki teğeti D noktasında kesmektedir. E noktasındaki açının ölçüsü şekilde verilmiştir. Şekil ölçekli değildir.\nBuna göre, x = m(ADB) kaç derecedir?',
 dogru=35,yan=[(90,'B deki dik açıyı (90°) x sanmış.','dikkat'),(55,'m(BAC) = 55° yi bulup x yerine yazmış; x, ABD üçgeninin üçüncü açısıdır.','dikkat'),(70,'Verilen m(BEC) = 70° yi x sanmış.','dikkat'),(125,'55° yi 180° e tamamlayıp 125° bulmuş.','islem')],
 istenen='x = m(ADB) açısının ölçüsü.',
 ip=['E noktasından çıkan iki doğru parçasının uzunlukları arasında bir ilişki var mı?'],
 bilgi=[TEGB,TEGK],
 ad=[A('EBC üçgenini çöz','E dan çizilen teğetler eşittir: |EB| = |EC|. Taban açıları eşit olduğundan','m(EBC) = (180° − 70°) ÷ 2 = 55°'),A('A daki açıyı bul','EBC teğet–kiriş açısı ile BAC çevre açısı aynı BC yayını görür.','m(BAD) = m(BAC) = 55°'),A('B deki dik açıyı yaz','B deki teğet, çapa diktir.','m(ABD) = 90°'),A('x değerini bul','ABD üçgeninde iç açılar toplamı 180° dir.','x = 180° − 90° − 55° = 35°')],
 puf='Köşelerden yarıçaplara bakıp eşit uzunlukları bul.',sekil=SK7)

# ===== 08 · yay oranları · orta =====
kartla('K-GCI-08','Oranlı yaylar','Yaylar oranla verildiğinde önce çemberin tamamından oran birimi bulunur; yaylar bilinince kirişlerin kesişim açısı yaylardan hesaplanır.','Oran birimini (k) bulmadan işlem yapmak; yayları toplamak yerine farkını almak; açıyı yayın kendisi sanmak.','orta',3,'ge-ci-oran','Oranlı yaylar')
k8=20; Y8=[3*k8,5*k8,4*k8,6*k8]; assert sum(Y8)==360
a_=[150,150+Y8[0]]; a_.append(a_[1]+Y8[1]); a_.append(a_[2]+Y8[2])
A8,B8,C8,D8=[pc(O,r,x_) for x_ in a_]; assert abs((a_[3]+Y8[3])%360-a_[0]%360)<1e-9
E8=inter(A8,C8,B8,D8)
ok(ang(E8,A8,D8),110); ok(ang(E8,A8,B8),70)
assert (120+100)//2==110 and (60+80)//2==70 and 120+100==220 and 220//4==55 and 120-100==20
f=F(); f.circ(O,r); f.poly([A8,B8,C8,D8]); f.line(A8,C8); f.line(B8,D8)
for i,(t,p1,p2) in enumerate([('3k',a_[0],a_[1]),('5k',a_[1],a_[2]),('4k',a_[2],a_[3]),('6k',a_[3],a_[3]+Y8[3])]):
    f.node(pc(O,r+.62,(p1+p2)/2),f'${t}$')
f.arc(E8,A8,D8,.28,'$x$',.5)
vlab(f,'A',A8,.3); vlab(f,'B',B8,.3); vlab(f,'C',C8,.3); vlab(f,'D',D8,.3); f.node(add(E8,(.28,-.1)),'$E$')
SK8=f.svg()
q('0008',tipId='ge-ci-oran',tip='Oranlı yaylar',z='orta',alt='Oranlı Yaylar',kaz='Oranla verilen yaylardan yay ölçülerini bulup köşegenlerin kesişim açısını hesaplar.',
 kart='K-GCI-08 (oranlı yaylar) · AB, BC, CD, DA = 3k, 5k, 4k, 6k',
 metin='Şekilde A, B, C ve D noktaları bir çemberin üzerindedir. AB, BC, CD ve DA yaylarının ölçüleri şekilde k türünden verilmiştir. [AC] ve [BD] köşegenleri E noktasında kesişmektedir. Şekil ölçekli değildir.\nBuna göre, x = m(AED) kaç derecedir?',
 dogru=110,yan=[(20,'Yayların farkını (120° − 100°) almış.','islem'),(55,'Yayların toplamını ikiye bölüp bir kez daha yarılamış.','islem'),(70,'Komşu açıyı (AEB) bulmuş; x onun bütünleyenidir.','dikkat'),(100,'BC yayının ölçüsünü (100°) açı sanmış.','dikkat')],
 istenen='x = m(AED) açısının ölçüsü.',
 ip=['Yayların ölçüleri k cinsinden verilmiş; k yı nasıl bulabilirsin?'],
 bilgi=[ICD],
 ad=[A('k yı bul','Dört yay çemberi tamamlar.','3k + 5k + 4k + 6k = 360° → 18k = 360° → k = 20°'),A('Gerekli yayları yaz','AED açısının gördüğü yaylar DA ve BC dir.','DA = 6 × 20° = 120° · BC = 5 × 20° = 100°'),A('x değerini bul','İç açı, gördüğü iki yayın toplamının yarısıdır.','x = (120° + 100°) ÷ 2 = 110°')],
 puf='İki ayrı üçgenden iki ayrı eşitlik kurup birlikte çöz.',sekil=SK8)

# ===== 09 · çevrel çember · orta, hikâyeli =====
kartla('K-GCI-09','Çevrel çemberin merkezi','Üçgenin köşelerinden geçen çemberin merkezi köşelere eşit uzaklıktadır; merkez açı çevre açıdan, ikizkenar üçgen ise taban açısından bulunur.','Merkez açıyı çevre açıya eşit almak; ikizkenar üçgende tepe açısı ile taban açısını karıştırmak; verilen çevre açıyı cevap sanmak.','orta',3,'ge-ci-cevrel','Çevrel çember')
A9=pc(O,r,90); B9=pc(O,r,190); C9=pc(O,r,310)
ok(ang(B9,A9,C9),70); ok(ang(C9,A9,B9),50); ok(ang(A9,B9,C9),60)
ok(ang(O,A9,B9),100); ok(ang(B9,A9,O),40); ok(ang(B9,A9,C9),70); ok(ang(A9,B9,O),40)
assert 2*50==100 and (180-100)//2==40 and 90-70==20 and 90-50==40 and 40+20==60
f=F(); f.circ(O,r); f.poly([A9,B9,C9]); f.line(O,A9); f.dot(O)
f.arc(B9,A9,C9,.5,'$70^\\circ$',.95); f.arc(C9,A9,B9,.55,'$50^\\circ$',1.0); f.arc(A9,B9,O,.65,'$x$',1.05)
vlab(f,'A',A9); vlab(f,'B',B9); vlab(f,'C',C9); f.node((.2,-.2),'$O$')
SK9=f.svg()
q('0009',tipId='ge-ci-cevrel',tip='Çevrel çember',z='orta',alt='Çevrel Çember',kaz='Üçgenin çevrel çemberinin merkezini kullanarak merkez açıdan ikizkenar üçgenin taban açısına geçer.',kalip='hikâyeli',
 kart='K-GCI-09 (çevrel çember) · B = 70°, C = 50°',
 metin='Üçgen biçimli bir arsanın A, B ve C köşelerinden geçen dairesel bir çit çevrilmiştir. Çitin merkezi olan O noktasındaki çeşme, köşelere birer boruyla bağlanacaktır; şekilde yalnız A köşesine giden boru çizilmiştir. Arsanın B ve C köşelerindeki açıları şekilde verilmiştir. Şekil ölçekli değildir.\nBuna göre, x = m(OAB) kaç derecedir?',
 dogru=40,yan=[(70,'Verilen m(ABC) = 70° yi x ile eşit sanmış.','dikkat'),(50,'Verilen m(ACB) = 50° yi x ile eşit sanmış.','dikkat'),(60,'A köşesindeki açıyı (60°) bulup x yerine yazmış.','dikkat'),(100,'Merkez açıyı (100°) bulup ikizkenar üçgenin taban açısına geçmemiş.','dikkat')],
 istenen='x = m(OAB) açısının ölçüsü.',
 ip=['O noktasını köşelere bağlayan doğru parçalarının oluşturduğu üçgenlere bak.'],
 bilgi=[CEVR,CEV],
 ad=[A('Merkez açıyı bul','ACB çevre açısı AB yayını görür; merkez açı bu yayın ölçüsüne eşittir.','m(AOB) = 2 × 50° = 100°'),A('İkizkenar üçgene bak','OA ve OB yarıçaptır; OAB üçgeninin taban açıları eşittir.','x = (180° − 100°) ÷ 2 = 40°'),A('Kontrol et','Aynı yolla OAC açısı bulunur; ikisi A köşesindeki açıyı oluşturur.','m(OAC) = 90° − 70° = 20° · 40° + 20° = 60° = 180° − 70° − 50°')],
 puf='Her yayın kaç derece olduğunu ilk iş olarak bul.',sekil=SK9)

# ===== 10 · kirişler dörtgeninin uzantıları · zor =====
kartla('K-GCI-10','Dörtgenin kenar uzantıları','Kenar uzantılarının kesiştiği noktalardaki üçgenlerde, kirişler dörtgeninin karşılıklı açılarının bütünlüğü kullanılarak iki bilinmeyenli denklem kurulur.','Karşılıklı açıları eşit saymak; iki uzantı açısını toplayıp cevap yazmak; bir üçgeni kurup diğerini unutmak.','zor',4,'ge-ci-uzanti','Kirişler dörtgeninin uzantıları')
a10=[210,360,400,470]  # A,B,C,D açıları: AB=150,BC=40,CD=70,DA=100
A10,B10,C10,D10=[pc(O,r,x_) for x_ in a10]
E10=inter(A10,D10,B10,C10); F10=inter(A10,B10,D10,C10)
ok(ang(E10,D10,C10),40); ok(ang(F10,B10,C10),30); ok(ang(B10,A10,C10),85); ok(ang(A10,B10,D10),55); ok(ang(C10,B10,D10),125)
ok(ang(A10,B10,D10)+ang(C10,B10,D10),180)

assert 180-40==140 and 140-85==55 and 85-55==30 and 40+30==70 and 85+55==140
assert dist(F10,A10)>dist(B10,A10) and dist(E10,A10)>dist(D10,A10) and dist(F10,D10)>dist(C10,D10) and dist(E10,B10)>dist(C10,B10)
print('E,F',E10,F10)
f=F(); f.circ(O,r); f.poly([A10,B10,C10,D10]); f.line(D10,E10); f.line(C10,E10); f.line(B10,F10); f.line(C10,F10)
f.arc(E10,D10,C10,.9,'$40^\\circ$',1.4); f.arc(F10,B10,C10,.9,'$30^\\circ$',1.4)
vlab(f,'A',A10); vlab(f,'B',B10); vlab(f,'C',C10); vlab(f,'D',D10)
f.vl('E',E10,sub(E10,O),.3); f.vl('F',F10,sub(F10,O),.3)
SK10=f.svg()
q('0010',tipId='ge-ci-uzanti',tip='Kirişler dörtgeninin uzantıları',z='zor',alt='Kenar Uzantıları',kaz='Kirişler dörtgeninin kenar uzantılarının açılarından iki bilinmeyenli denklem kurup bir iç açıyı bulur.',
 kart='K-GCI-10 (uzantılar) · E = 40°, F = 30°',
 metin='Şekilde köşeleri bir çemberin üzerinde olan ABCD dörtgeninin [AD] ile [BC] kenarlarının uzantıları E noktasında, [AB] ile [DC] kenarlarının uzantıları F noktasında kesişmektedir. E ve F noktalarındaki açıların ölçüleri şekilde verilmiştir. Şekil ölçekli değildir.\nBuna göre, m(ABC) kaç derecedir?',
 dogru=85,yan=[(30,'Verilen m(F) = 30° yi cevap yazmış.','dikkat'),(40,'Verilen m(E) = 40° yi cevap yazmış.','dikkat'),(55,'Karşıt köşedeki m(BAD) = 55° yi bulup bırakmış.','dikkat'),(70,'E ve F açılarını toplayıp (70°) cevap yazmış.','islem')],
 istenen='m(ABC) açısının ölçüsü (derece).',
 ip=['ECD ve FBC üçgenlerinin her birinden bir eşitlik yazmayı dene.'],
 bilgi=[KIR],
 ad=[A('İlk denklemi kur','ECD üçgeninde ECD açısı, BCD nin bütünleyeni olduğundan m(BAD) e eşittir; EDC açısı da m(ABC) ye eşittir. İç açılar toplamı 180° dir.','40° + m(BAD) + m(ABC) = 180° → m(ABC) + m(BAD) = 140°'),A('İkinci denklemi kur','FBC üçgeninde FBC açısı 180° − m(ABC), BCF açısı m(BAD) dir.','30° + (180° − m(ABC)) + m(BAD) = 180° → m(ABC) − m(BAD) = 30°'),A('Denklemi çöz','İki eşitlik taraf tarafa toplanır.','2 · m(ABC) = 170° → m(ABC) = 85°'),A('Kontrol et','Diğer açı 55° olur; üç değer de tutarlıdır.','85° + 55° = 140° · 85° − 55° = 30°')],
 puf='Önce çemberin tamamından oran birimini çıkar.',sekil=SK10)

bitir_geo('cemberaciiki','Çemberde Açı')
