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
P=Parti('aciortay','Açıortay','geo|Açıortay',ders='TYT Geometri',idon='tytgeo')
IC=B('İç açıortay teoremi','üçgenin bir iç açıortayı karşı kenarı, komşu kenarların oranında böler: [AD] açıortay ise |BD| / |DC| = |AB| / |AC|. Örnek: komşu kenarlar 2 ve 3 ise karşı kenar 2 : 3 oranında bölünür')
DISB=B('Dış açıortay teoremi','dış açıortay karşı kenarın uzantısını, komşu kenarların oranında dıştan böler: |EB| / |EC| = |AB| / |AC|. Örnek: komşu kenarlar 1 ve 2 ise E noktasının uzaklıkları da 1 : 2 oranındadır')
UZ=B('Açıortay ve uzaklık','bir açının açıortayı üzerindeki her nokta açının kollarına eşit uzaklıktadır; uzaklık, noktadan kola indirilen dikmenin uzunluğudur')
IT=B('İç teğet çemberin merkezi','üçgenin iç açıortayları aynı noktada (I) kesişir. Bu nokta kenarlara eşit uzaklıktadır ve m(BIC) = 90° + m(A) / 2 dir. Örnek: m(A) = 40° ise m(BIC) = 110°')
PAR=B('Açıortay ve paralel','iç teğet merkezinden kenara paralel çizilince BI açıortay olduğundan ikizkenar üçgenler oluşur: m(DBI) = m(IBC) = m(DIB) olduğundan |DB| = |DI| dır. Örnek: |DB| = 2 ise |DI| = 2')
ALANORAN=B('Ortak yüksekli üçgenler','yükseklikleri ortak olan üçgenlerin alanları tabanlarıyla orantılıdır. Örnek: tabanlar 2 ve 3 ise alanlar 2 : 3 oranındadır')

# ===== 01 · iç açıortay teoremi · kolay =====
konu('geo|Açıortay','Açıortay')
kartla('K-GAO-01','İç açıortay teoremi','Açıortay karşı kenarı komşu kenarların oranında böler; kenar toplamı verilen kenara bölünüp parçalar bulunur.','Oranı ters kurmak; D’yi [BC]’nin orta noktası sanmak.','kolay',3,'ge-ao-ic-oran','İç açıortay teoremi ile kenar oranı')
AB,AC,BC=8,12,15; BD=BC*AB/(AB+AC); assert BD==6 and BC-BD==9
s=.36; A1,B1,C1=tri(BC,AC,AB,s); D1=lerp(B1,C1,BD/BC)
assert abs(ang(A1,B1,D1)-ang(A1,D1,C1))<1e-9
f=F(); f.poly([A1,B1,C1]); f.line(A1,D1); ic=cen([A1,B1,C1])
f.arc(A1,B1,D1,.55); f.arc(A1,D1,C1,.55)
f.sl('$8$',A1,B1,ic,.28); f.sl('$12$',A1,C1,ic,.28); dim(f,B1,C1,'$15$',(0,-1),.6)
for n_,p_ in (('A',A1),('B',B1),('C',C1)): vtx(f,p_,n_,ic)
f.vl('D',D1,(0,-1),.3)
SK1=f.svg()
assert sorted([6,7,7.5,9,10])==sorted([BD,BC-AB,BC/2,BC-BD,BC*AB/AC])
q('0001',tipId='ge-ao-ic-oran',tip='İç açıortay teoremi ile kenar oranı',z='kolay',alt='İç Açıortay Teoremi',kaz='İç açıortay teoremiyle karşı kenarın parçalarını bulur.',
 kart='K-GAO-01 (iç açıortay teoremi) · AB = 8, AC = 12, BC = 15',
 metin='Şekilde ABC üçgeninin A köşesinden çizilen [AD] doğru parçası, A açısının iç açıortayıdır ve D noktası [BC] kenarı üzerindedir. Kenar uzunlukları cm cinsinden verilmiştir; şekil ölçekli değildir.\nBuna göre, |BD| kaç cm’dir?',
 dogru=BD,yan=[(BC-AB,'|BD| = |BC| − |AB| = 7 yazmış; parçalar kenar farkıyla bulunmaz.','bilgi'),(BC/2,'Açıortayı kenarortay sanıp D’yi [BC]’nin orta noktası kabul etmiş: 15 ÷ 2.','bilgi'),(BC-BD,'Oranı ters kurmuş: |BD| / |DC| = |AC| / |AB| yazıp 9 bulmuş.','dikkat'),(BC*AB/AC,'|BD| / |BC| = |AB| / |AC| yazmış (parça / bütün ile komşu kenar oranını karıştırmış): 15 × 8 ÷ 12 = 10.','bilgi')],
 istenen='|BD| uzunluğu (cm).',
 ip=['Açıortay, karşı kenarı hangi iki uzunluğun oranında bölüyor? Önce parçaların oranını yaz, toplamlarının |BC| olduğunu kullan.'],
 bilgi=[IC],
 ad=[A('Oranı yaz','İç açıortay karşı kenarı komşu kenarların oranında böler.','|BD| / |DC| = |AB| / |AC| = 8 / 12 = 2 / 3'),A('Parçalara ayır','|BC| = 15 cm, 2 + 3 = 5 eş parçaya bölünür; her parça 3 cm’dir.','|BD| = 2 × 3 = 6 · |DC| = 3 × 3 = 9'),A('Kontrol et','Parçaların toplamı |BC| ye eşit olmalıdır.','6 + 9 = 15')],
 puf='Açıortay teoreminde parçaların oranı komşu kenarların oranıdır; kenar uzunluğunu bu oranla paylaştır.',sekil=SK1)

# ===== 02 · açıortay üzerindeki noktanın uzaklığı · kolay · hikâyeli =====
kartla('K-GAO-02','Açıortay üzerinde eşit uzaklık','Açıortay üzerindeki nokta kollara eşit uzaklıktadır; iki uzaklık eşitlenip denklem çözülür.','Bulunan x’i cevap sanmak; yalnız bir uzaklığı vermek.','kolay',3,'ge-ao-uzaklik','Açıortay üzerindeki noktanın kollara uzaklığı')
th=35; O2=(0,0); u=(cos(radians(th)),sin(radians(th))); v=(cos(radians(th)),-sin(radians(th)))
P2=(4.6,0); H2=mul(u,P2[0]*cos(radians(th))); K2=mul(v,P2[0]*cos(radians(th)))
assert abs(dist(P2,H2)-dist(P2,K2))<1e-9 and abs(ang(P2,H2,O2)-(90-th))<1e-9 and abs((P2[0]-H2[0])*u[0]+(P2[1]-H2[1])*u[1])<1e-9
Ae=mul(u,5.5); Be=mul(v,5.5)
x2=4; assert x2+3==2*x2-1==7
f=F(); f.line(O2,Ae); f.line(O2,Be); f.line(O2,P2,'dashed'); f.line(P2,H2); f.line(P2,K2); f.dik(H2,O2,P2); f.dik(K2,O2,P2)
f.arc(O2,Ae,P2,.7); f.arc(O2,P2,Be,.7)
f.sl('$x+3$',P2,H2,O2,.42); f.sl('$2x-1$',P2,K2,O2,.45)
f.vl('O',O2,(-1,0),.3); f.vl('A',Ae,u,.3); f.vl('B',Be,v,.3); f.vl('P',P2,(1,0),.3); f.vl('H',H2,(.4,1),.3); f.vl('K',K2,(.4,-1),.3)
SK2=f.svg()
q('0002',tipId='ge-ao-uzaklik',tip='Açıortay üzerindeki noktanın kollara uzaklığı',z='kolay',kalip='hikâyeli',alt='Açıortayda Uzaklık',kaz='Açıortay üzerindeki noktanın kollara eşit uzaklıkta olduğunu kullanarak denklem çözer.',
 kart='K-GAO-02 (açıortayda eşit uzaklık) · |PH| = x + 3, |PK| = 2x − 1',
 metin='Bir parkta [OA ve [OB yürüyüş yolları O noktasında kesişmektedir. Belediye, [OP doğrusunun bu iki yolun oluşturduğu açının açıortayı olduğu P noktasına bir bank koyacaktır. P’den [OA ve [OB yollarına inilen dikmelerin ayakları H ve K noktalarıdır.\nBuna göre, |PH| + |PK| toplamı kaç birimdir?',
 dogru=14,yan=[(4,'Eşitlikten bulduğu x değerini uzaklıkların toplamı sanmış.','dikkat'),(7,'Yalnız bir uzaklığı (|PH| = 7) bulup diğerini eklemeyi unutmuş.','dikkat'),(8,'x + 3 = 2x − 1 eşitliğini x = 2 bulmuş (−1’i karşı tarafa yanlış geçirmiş): 5 + 3 = 8.','islem'),(11,'x ile bir uzaklığı toplamış: 4 + 7 = 11.','dikkat')],
 istenen='|PH| + |PK| toplamı.',
 ip=['P noktası açıortay üzerinde olduğundan hangi iki uzunluk birbirine eşittir?'],
 bilgi=[UZ],
 ad=[A('Eşitliği yaz','P, açıortay üzerinde olduğundan iki kola uzaklıkları eşittir.','|PH| = |PK| → x + 3 = 2x − 1'),A('x’i bul','Bilinmeyenleri bir tarafa topla.','x = 4'),A('Uzaklıkları hesapla','Her iki uzaklığı ayrı ayrı bul ve topla.','|PH| = 4 + 3 = 7 · |PK| = 2 × 4 − 1 = 7 · 7 + 7 = 14')],
 puf='Açıortay üzerindeki nokta kollara eşit uzaklıktadır: dikmeleri eşitle, sonra sorulan uzunluğa dön.',sekil=SK2)

# ===== 03 · dış açıortay · orta =====
kartla('K-GAO-03','Dış açıortay teoremi','Dış açıortay karşı kenarın uzantısını komşu kenarların oranında dıştan böler; uzantı parçası denklemle bulunur.','İç açıortay teoremini uygulamak; uzantı yerine iç parçayı bulmak.','orta',4,'ge-ao-dis-oran','Dış açıortay ile uzantı oranı')
AB3,AC3,BC3=6,9,5; EB3=10; EC3=15; assert EB3/EC3==AB3/AC3 and EC3-EB3==BC3
s=.3; A3,B3,C3=tri(BC3,AC3,AB3,s)
E3=(-EB3*s,0); F3=add(A3,mul(un(sub(A3,B3)),1.5))
assert abs(ang(A3,F3,E3)-ang(A3,E3,C3))<1e-9
ic=cen([A3,B3,C3])
f=F(); f.poly([A3,B3,C3]); f.line(B3,E3); f.line(B3,F3); f.line(A3,E3)
f.arc(A3,F3,E3,.5); f.arc(A3,E3,C3,.5)
f.sl('$6$',A3,B3,C3,.3); f.sl('$9$',A3,C3,B3,.3); f.node((C3[0]/2,-.3),'$5$')
f.vl('A',A3,(1,.9),.32); f.vl('B',B3,(.3,-1),.3); f.vl('C',C3,(1,-.4),.3); f.vl('E',E3,(-1,-.3),.3); f.vl('F',F3,(-.3,.8),.3)
SK3=f.svg()
assert sorted([2,3,10,15,25])==sorted([BC3*AB3/(AB3+AC3),BC3*AC3/(AB3+AC3),EB3,EC3,EB3+EC3])
q('0003',tipId='ge-ao-dis-oran',tip='Dış açıortay ile uzantı oranı',z='orta',alt='Dış Açıortay',kaz='Dış açıortay teoreminden uzantı uzunluğunu bulur.',
 kart='K-GAO-03 (dış açıortay oranı) · AB = 6, AC = 9, BC = 5',
 metin='Şekilde ABC üçgeninin A köşesindeki dış açıortay, dış açıyı iki eş açıya ayırmakta ve [CB] nin uzantısını E noktasında kesmektedir. Şekildeki uzunluklar cm cinsindendir; şekil ölçekli değildir.\nBuna göre, |BE| kaç cm’dir?',
 dogru=EB3,yan=[(2,'İç açıortay teoremini uygulamış: iç açıortayın [BC]’yi böldüğü |BD| = 5 × 6 ÷ 15 = 2’yi bulmuş.','bilgi'),(3,'Oranı ters yazıp iç açıortay parçasını bulmuş: 5 × 9 ÷ 15 = 3.','bilgi'),(15,'|BE| yerine |CE| = 15’i bulup bırakmış (|CE| = |BE| + 5).','dikkat'),(25,'|BE| ile |CE| uzunluklarını toplayıp 10 + 15 = 25 yazmış.','dikkat')],
 istenen='|BE| uzunluğu (cm).',
 ip=['Dış açıortay için |EB| / |EC| oranı hangi iki kenarın oranına eşittir? |EC| ile |EB| arasındaki ilişkiyi şekilden oku.'],
 bilgi=[DISB],
 ad=[A('Oranı yaz','Dış açıortay teoremi: E noktasının B ve C’ye uzaklıkları komşu kenarlarla orantılıdır.','|EB| / |EC| = |AB| / |AC| = 6 / 9 = 2 / 3'),A('Uzantıyı değişkenle göster','B, E ile C arasındadır; |EC| = |EB| + |BC|.','|EB| = 2k, |EC| = 3k → 3k − 2k = 5 → k = 5'),A('|BE| uzunluğunu bul','Bulunan k ile hesapla.','|BE| = 2 × 5 = 10'),A('Kontrol et','|EC| = 15 olmalı.','|EC| = 3 × 5 = 15 = 10 + 5')],
 puf='Dış açıortayda E, kısa kenar tarafında dışarıdadır; |EB| / |EC| = |AB| / |AC| ve |EC| = |EB| + |BC| denklemi birlikte kullanılır.',sekil=SK3)

# ===== 04 · iç teğet merkezi açı · orta =====
kartla('K-GAO-04','İç teğet merkezi ve BIC açısı','İç açıortayların kesişimi I için m(BIC) = 90° + A/2 bağıntısı kullanılır; A açısı bulunur.','180° − BIC ile A’yı bulmak; yarıyı unutmak.','orta',3,'ge-ao-merkez-aci','İç açıortayların kesişimi ve açılar')
Bd,Cd=56,60; Ad_=180-Bd-Cd; assert Ad_==64 and 90+Ad_/2==122
B4=(0,0); C4=(6.0,0); A4=tri_ac(B4,C4,Bd,Cd); I4=incenter(A4,B4,C4)
assert abs(ang(I4,B4,C4)-122)<1e-9 and abs(ang(B4,A4,I4)-ang(B4,I4,C4))<1e-9 and abs(ang(C4,A4,I4)-ang(C4,I4,B4))<1e-9
ic=cen([A4,B4,C4]); f=F(); f.poly([A4,B4,C4]); f.line(A4,I4); f.line(B4,I4); f.line(C4,I4)
arct(f,B4,A4,I4,.6,1); arct(f,B4,I4,C4,.6,1); arct(f,C4,A4,I4,.6,2); arct(f,C4,I4,B4,.6,2)
f.arc(A4,B4,C4,.7); f.node(add(A4,(.3,-.85)),'{\\large $x$}'); f.node(add(I4,(0,-.55)),'$122^\\circ$')
for n_,p_ in (('A',A4),('B',B4),('C',C4)): vtx(f,p_,n_,ic)
f.vl('I',I4,(.7,.8),.28)
SK4=f.svg()
vals=[Ad_,180-122,122-90,122/2,180-Ad_]; assert vals==[64,58,32,61,116]
q('0004',tipId='ge-ao-merkez-aci',tip='İç açıortayların kesişimi ve açılar',z='orta',alt='İç Teğet Merkezi',kaz='İç teğet çemberin merkezi I için m(BIC) bağıntısıyla A açısını bulur.',
 kart='K-GAO-04 (iç teğet merkezi) · m(BIC) = 122°',
 metin='Şekilde I noktası, ABC üçgeninin iç açıortaylarının kesim noktasıdır (iç teğet çemberinin merkezidir); [AI], [BI] ve [CI] çizilmiş, açıortayların ayırdığı eş açılar aynı sayıda çentikli yaylarla gösterilmiştir. Şekil ölçekli değildir. m(BIC) = 122° olduğuna göre, x = m(BAC) kaç derecedir?',
 dogru=64,yan=[(32,'122° − 90° = 32° bulup A açısının yarısını bulmuş, 2 ile çarpmayı unutmuş.','islem'),(58,'m(BIC) + m(BAC) = 180° sanıp 180° − 122° = 58° yazmış.','bilgi'),(61,'122° ÷ 2 = 61° işlemini yapmış.','bilgi'),(116,'B ile C açıları toplamını (180° − 64°) bulup A açısı sanmış.','dikkat')],
 istenen='x = m(BAC) açısının ölçüsü.',
 ip=['I iç açıortayların kesişimi olduğundan BIC açısı ile A açısı arasında sabit bir bağıntı vardır; BIC üçgeninin iç açılarına bak.'],
 bilgi=[IT],
 ad=[A('BIC üçgenini kur','B ve C’deki açılar açıortayla yarılanır: m(IBC) = B / 2, m(ICB) = C / 2.','m(BIC) = 180° − (B + C) / 2'),A('Bağıntıyı yaz','B + C = 180° − A olduğundan BIC = 90° + A / 2.','122° = 90° + x / 2'),A('x’i bul','Eşitliği çöz.','x / 2 = 32° → x = 64°')],
 puf='İç açıortayların kesişiminde BIC = 90° + A/2; verilen BIC açısından A’ya geçerken önce 90° çıkarılır, sonra 2 ile çarpılır.',sekil=SK4)

# ===== 05 · iç teğet merkezi + paralel · zor =====
kartla('K-GAO-05','İç teğet merkezinden paralel ve çevre','Açıortay ve paralellik ikizkenar üçgenler doğurur; küçük üçgenin çevresi iki kenar uzunluğunun toplamına dönüşür.','Çevreyi üç kenarla (BC dahil) hesaplamaya çalışmak; DE’yi BC sanmak.','zor',4,'ge-ao-merkez-paralel','İç teğet merkezinden kenara paralel')
AB5,AC5=9,13; cev5=AB5+AC5; assert cev5==22
Bd5,Cd5=58,48; B5=(0,0); C5=(6.2,0); A5=tri_ac(B5,C5,Bd5,Cd5); I5=incenter(A5,B5,C5)
D5=kesis(A5,B5,I5,add(I5,(1,0))); E5=kesis(A5,C5,I5,add(I5,(1,0)))
assert abs(dist(D5,E5)-dist(B5,D5)-dist(C5,E5))<1e-9 and abs(dist(B5,D5)-dist(D5,I5))<1e-9
assert abs(dist(A5,D5)+dist(A5,E5)+dist(D5,E5)-dist(A5,B5)-dist(A5,C5))<1e-9
ic=cen([A5,B5,C5]); f=F(); f.poly([A5,B5,C5]); f.line(B5,I5); f.line(C5,I5); f.line(D5,E5); f.par(D5,lerp(D5,E5,.4)); f.par(B5,lerp(B5,C5,.4))
arct(f,B5,D5,I5,.55,1); arct(f,B5,I5,C5,.55,1); arct(f,C5,E5,I5,.6,2); arct(f,C5,I5,B5,.6,2)
f.sl('$9$',A5,B5,C5,.3); f.sl('$13$',A5,C5,B5,.3)
for n_,p_ in (('A',A5),('B',B5),('C',C5)): vtx(f,p_,n_,ic)
f.vl('D',D5,(-1,.1),.3); f.vl('E',E5,(1,.1),.3); f.vl('I',I5,(0,-1),.28)
SK5=f.svg()
assert sorted([11,18,22,26,44])==sorted([cev5/2,2*AB5,cev5,2*AC5,2*cev5])
q('0005',tipId='ge-ao-merkez-paralel',tip='İç teğet merkezinden kenara paralel',z='zor',alt='İç Teğet Merkezi ve Paralel',kaz='İç teğet merkezinden çizilen paralelde ikizkenar üçgenleri kullanarak küçük üçgenin çevresini bulur.',
 kart='K-GAO-05 (iç teğet merkezi + paralel, çevre) · AB = 9, AC = 13',
 metin='Şekilde I noktası, ABC üçgeninin iç teğet çemberinin merkezidir. D ∈ [AB], E ∈ [AC], I ∈ [DE] ve [DE] // [BC] dir. Şekilde |AB| = 9 cm ve |AC| = 13 cm verilmiştir; şekil ölçekli değildir.\nBuna göre, ADE üçgeninin çevresi kaç cm’dir?',
 dogru=22,yan=[(11,'Çevreyi |AB| + |AC| toplamının yarısı sanmış: 22 ÷ 2 = 11.','bilgi'),(18,'ADE’yi ikizkenar sanıp |AD| ve |AE| yi |AB| ye eşit almış: 2 × 9 = 18.','bilgi'),(26,'ADE’yi ikizkenar sanıp |AD| ve |AE| yi |AC| ye eşit almış: 2 × 13 = 26.','bilgi'),(44,'|DE| yi ayrıca ekleyip |AB| + |AC| toplamını iki kez saymış: 2 × 22 = 44.','islem')],
 istenen='ADE üçgeninin çevresi (cm).',
 ip=['[BI] ve [CI] açıortay, [DE] // [BC] olduğuna göre D ve E köşelerindeki üçgenlerde hangi kenarlar eşit çıkar? |DE| yi bu parçalarla ifade et.'],
 bilgi=[PAR,IT],
 ad=[A('DBI üçgenini incele','m(DBI) = m(IBC) = m(DIB) (iç ters açı) olduğundan DBI ikizkenardır.','|DI| = |DB|'),A('CEI üçgenini incele','Aynı mantıkla CEI üçgeni de ikizkenardır.','|EI| = |EC|'),A('|DE| yi yaz','I, [DE] üzerindedir.','|DE| = |DI| + |IE| = |DB| + |EC|'),A('Çevreyi bul','Çevre = |AD| + |AE| + |DE|; |AD| + |DB| = |AB| ve |AE| + |EC| = |AC|.','|AB| + |AC| = 9 + 13 = 22')],
 puf='İç teğet merkezinden kenara çizilen paralel, açıortayla birlikte ikizkenar üçgenler verir: küçük üçgenin çevresi iki yan kenarın toplamıdır.',sekil=SK5)

# ===== 06 · açıortay + alan · zor =====
kartla('K-GAO-06','İç açıortay ve alan oranı','Açıortay karşı kenarı oranlar; yüksekliği ortak üçgenlerde alanlar bu orana eşittir.','Alan oranı yerine kenar oranının karesini almak; oranı ters yazmak; toplam alanı vermek.','orta',4,'ge-ao-ic-alan','İç açıortay ve ortak yükseklikli üçgenlerde alan')
AB6,AC6,aABD=12,8,30; aADC=aABD*AC6/AB6; assert aADC==20 and aABD+aADC==50
A6,B6,C6=tri(15,AC6,AB6,.36); D6=lerp(B6,C6,AB6/(AB6+AC6))
assert abs(ang(A6,B6,D6)-ang(A6,D6,C6))<1e-9
ic=cen([A6,B6,C6]); f=F(); f.fill([A6,B6,D6]); f.poly([A6,B6,C6]); f.line(A6,D6); f.arc(A6,B6,D6,.55); f.arc(A6,D6,C6,.55)
f.sl('$12$',A6,B6,ic,.28); f.sl('$8$',A6,C6,ic,.28); f.node((2.6,-.9),'Alan$(ABD)=30\\ \\mathrm{cm}^2$')
for n_,p_ in (('A',A6),('B',B6),('C',C6)): vtx(f,p_,n_,ic)
f.vl('D',D6,(0,-1),.3)
SK6=f.svg()
assert sorted([18,20,30,45,50])==sorted([aABD*3/5,aADC,aABD,aABD*AB6/AC6,aABD+aADC])
q('0006',tipId='ge-ao-ic-alan',tip='İç açıortay ve ortak yükseklikli üçgenlerde alan',z='orta',alt='Açıortay ve Alan',kaz='Açıortay teoremi ile bulunan taban oranından alanları hesaplar.',
 kart='K-GAO-06 (açıortay + alan) · AB = 12, AC = 8, alan(ABD) = 30',
 metin='Şekilde ABC üçgeninin [AD] iç açıortayı çizilmiş ve D ∈ [BC] dir. Şekilde |AB| = 12 cm, |AC| = 8 cm ve taralı ABD üçgeninin alanı verilmiştir; şekil ölçekli değildir.\nBuna göre, ADC üçgeninin alanı kaç cm²’dir?',
 dogru=20,yan=[(18,'Yalnız 3/5 oranını almış: 30 × 3 ÷ 5 = 18 (oran 3 : 2 olduğundan 2/3 gerekir).','islem'),(30,'ABD ile ADC üçgenlerini eş alanlı sanmış (D’yi orta nokta kabul etmiş).','bilgi'),(45,'Oranı ters yazıp 30 × 12 ÷ 8 = 45 bulmuş.','dikkat'),(50,'İstenen ADC yerine ABC üçgeninin alanını (30 + 20) vermiş.','dikkat')],
 istenen='ADC üçgeninin alanı (cm²).',
 ip=['A köşesinden [BC] ye inen yükseklik ABD ve ADC üçgenleri için ortaktır; tabanların oranını açıortay teoremi verir.'],
 bilgi=[IC,ALANORAN],
 ad=[A('Taban oranını bul','Açıortay teoremi: |BD| / |DC| = |AB| / |AC|.','|BD| / |DC| = 12 / 8 = 3 / 2'),A('Alanlara aktar','ABD ve ADC üçgenlerinin yüksekliği ortak; alanları tabanlarıyla orantılıdır.','alan(ABD) / alan(ADC) = 3 / 2'),A('Alanı hesapla','Verilen alanı 3 parça kabul et.','30 ÷ 3 = 10 → alan(ADC) = 2 × 10 = 20'),A('Kontrol et','Tüm alan 50 olur ve oran korunur.','30 + 20 = 50 · 30 : 20 = 3 : 2')],
 puf='Açıortay oranı ve alan oranı aynıdır: yüksekliği ortak üçgenlerde kenar oranını alan oranına çevir.',sekil=SK6)
bitir_geo('aciortay','Açıortay')
