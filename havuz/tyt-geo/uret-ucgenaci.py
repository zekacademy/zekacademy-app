"""TYT Geometri · Üçgende · şekilli sorular (kardeş yok, ipucu 1). Koordinatlar hesaplanır; cevap ve çeldirici değerleri assert edilir."""
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
P=Parti('ucgenaci','Üçgende Açılar','geo|Üçgende Açılar',ders='TYT Geometri',idon='tytgeo')
IC=B('Üçgenin iç açıları','bir üçgenin iç açılarının ölçüleri toplamı 180°’dir. Örnek: iki açısı 50° ve 60° olan üçgenin üçüncü açısı 70°’dir')
DIS=B('Dış açı','üçgenin bir dış açısı, kendisine komşu olmayan iki iç açının toplamına eşittir. Örnek: iç açıları 30° ve 80° olan iki köşenin karşısındaki dış açı 110°’dir')
AOR=B('Açıortay','bir açıyı iki eş açıya ayıran ışındır; iç açıortay iç açıyı, dış açıortay dış açıyı ikiye böler. Örnek: 80° lik bir açının açıortayı onu 40° + 40° ye ayırır')
KEL=B('Kelebek (ters açılar)','iki doğru parçası kesişince karşılıklı açılar eşit olur; bu yüzden oluşan iki üçgenden birinin iki açısının toplamı, diğerinin ilgili iki açısının toplamına eşittir. Örnek: bir üçgende 30° ve 40° varsa karşısındaki üçgende de iki açının toplamı 70°’dir')
OK=B('Ok (kırık) dörtgeni','D noktası ABC üçgeninin içindeyse BDC açısı, A açısı ile ABD ve ACD açılarının toplamına eşittir: m(BDC) = m(A) + m(ABD) + m(ACD). Örnek: 30°, 20° ve 40° ise BDC = 90°’dir')
KATL=B('Katlama (simetri)','kâğıt katlanınca üst üste gelen açılar ve kenarlar eşit olur; bir köşe kat doğrusu boyunca katlanınca o köşedeki açı kat doğrusu tarafından iki eşit açıya ayrılır. Örnek: kat doğrusunun iki yanındaki açılar 40° ve 40°’dir')
IKIZ=B('İkizkenar üçgen','eşit kenarların karşısındaki açılar da eşittir. Örnek: tepe açısı 40° ise taban açıları 70°’er derecedir')
DORT=B('Dörtgenin açıları','bir dörtgenin iç açılarının toplamı 360°’dir. Örnek: üç açısı 80°, 90° ve 100° olan dörtgenin dördüncü açısı 90°’dir')
def dots(f): pass

# ================= 01 · İç açılar · kolay (hikâyeli) =================
konu('geo|Üçgende Açılar','Üçgende Açılar')
kartla('K-GUA-01','İç açılar toplamı','İç açıların toplamı 180° denklemi kurulur; x bulunur ve istenen köşenin açısı yazılır.','x’i bulup bırakmak; yanlış köşenin açısını vermek.','kolay',3,'ge-ua-ic','Üçgenin iç açıları toplamı',kalip='hikâyeli')
x=25; Av=2*x+10; Bv=3*x-5; Cv=x+25
assert Av+Bv+Cv==180 and (Av,Bv,Cv)==(60,70,50) and 180-Cv==130 and 6*x+30==180
A1,B1,C1=tri(60,70,50,5.6)
f=F(); f.poly([A1,B1,C1])
f.arc(A1,B1,C1,.7,'$(2x+10)^\\circ$',1.7); f.arc(B1,C1,A1,.7,'$(3x-5)^\\circ$',1.75); f.arc(C1,A1,B1,.7,'$(x+25)^\\circ$',1.75)
f.vl('A',A1,(0,1),.3); f.vl('B',B1,(-1,-.6),.3); f.vl('C',C1,(1,-.6),.3)
SK=f.svg()
q('0001',tipId='ge-ua-ic',tip='Üçgenin iç açıları toplamı',z='kolay',alt='İç Açılar Toplamı',kaz='Üçgenin iç açıları toplamının 180° olduğunu kullanarak cebirsel açıları bulur.',kalip='hikâyeli',
 kart='K-GUA-01 (iç açılar) · üç cebirsel açı, bir köşe istenir',
 metin='Üçgen biçimli bir bahçenin köşe noktaları A, B ve C dir. Bahçenin köşelerindeki açıların ölçüleri şekilde gösterildiği gibi m(BAC) = (2x + 10)°, m(ABC) = (3x − 5)° ve m(ACB) = (x + 25)° dir.\nŞekil ölçekli değildir.\nBuna göre, bahçenin C köşesindeki açının ölçüsü kaç derecedir?',
 dogru=50,yan=[(25,'Denklemden yalnız x = 25’i bulup sorulan açıyı hesaplamamış.','dikkat'),(60,'İstenen C köşesi yerine A köşesinin açısını (2x + 10 = 60°) hesaplamış.','dikkat'),(70,'İstenen C köşesi yerine B köşesinin açısını (3x − 5 = 70°) hesaplamış.','dikkat'),(130,'C açısının yerine onun bütünlerini (180° − 50°) yazmış.','dikkat')],
 istenen='m(ACB) açısının ölçüsü.',
 ip=['Üçgenin üç iç açısı arasında nasıl bir toplam ilişkisi var? Denklemi kurup çözdükten sonra sorulan köşeye dön.'],
 bilgi=[IC],
 ad=[A('Denklemi kur','Üçgenin iç açılarının toplamı 180°’dir.','(2x + 10) + (3x − 5) + (x + 25) = 180'),A('x’i bul','Benzer terimleri topla.','6x + 30 = 180 · x = 25'),A('C açısını yaz','x yerine 25 koy.','m(ACB) = 25 + 25 = 50°')],
 puf='İç açılar toplamı 180°’dir; x bulunduktan sonra sorulan köşenin ifadesine geri yaz.',sekil=SK)

# ================= 02 · Dış açı · kolay =================
kartla('K-GUA-02','Dış açı kuralı','Dış açı, komşu olmayan iki iç açının toplamına eşittir; cebirsel dış açıyla denklem kurulur.','Dış açıyı iç açı sanıp 180° toplamıyla denklem kurmak.','kolay',3,'ge-ua-dis','Üçgende dış açı')
x=40; Av=x+20; Bv=50; Dv=3*x-10
assert Av+Bv==Dv==110 and 180-Dv==70 and 4*30+60==180 and 3*30-10==80
A2,B2,C2=tri(60,50,70,5.0); D2=(C2[0]+2.0,0)
assert abs(ang(C2,D2,A2)-110)<1e-9
f=F(); f.poly([A2,B2,C2]); f.line(C2,D2)
f.arc(A2,B2,C2,.7,'$(x+20)^\\circ$',1.7); f.arc(B2,C2,A2,.7,'$50^\\circ$',1.45); f.arc(C2,D2,A2,.6,'$(3x-10)^\\circ$',1.55)
f.vl('A',A2,(0,1),.3); f.vl('B',B2,(-1,-.6),.3); f.vl('C',C2,(0,-1),.3); f.vl('D',D2,(1,-.5),.3)
SK=f.svg()
q('0002',tipId='ge-ua-dis',tip='Üçgende dış açı',z='kolay',alt='Dış Açı',kaz='Üçgende dış açının komşu olmayan iki iç açının toplamına eşit olduğunu kullanıp bilinmeyeni bulur.',
 kart='K-GUA-02 (dış açı) · cebirsel dış açı',
 metin='Şekilde ABC üçgeninin [BC] kenarı C noktasından D noktasına kadar uzatılmıştır. m(BAC) = (x + 20)°, m(ABC) = 50° ve m(ACD) = (3x − 10)° dir.\nŞekil ölçekli değildir.\nBuna göre, m(ACD) kaç derecedir?',
 dogru=110,yan=[(40,'Denklemden yalnız x = 40’ı bulup sorulan açıyı hesaplamamış.','dikkat'),(60,'İstenen dış açı yerine A köşesinin açısını (x + 20 = 60°) yazmış.','dikkat'),(70,'Dış açı yerine C köşesindeki iç açıyı (180° − 110°) yazmış.','dikkat'),(80,'Dış açıyı iç açı sanıp (x + 20) + 50 + (3x − 10) = 180 yazmış; x = 30 ve açı 80° çıkmış.','bilgi')],
 istenen='m(ACD) dış açısının ölçüsü.',
 ip=['ACD açısı üçgenin iç açısı mı? Komşu olmayan iki iç açıyla arasındaki ilişkiyi hatırla.'],
 bilgi=[DIS],
 ad=[A('Dış açı kuralını yaz','ACD dış açısı, C’ye komşu olmayan A ve B iç açılarının toplamına eşittir.','3x − 10 = (x + 20) + 50'),A('x’i bul','Bilinmeyenleri bir tarafa topla.','2x = 80 · x = 40'),A('Dış açıyı hesapla','x yerine 40 koy.','m(ACD) = 3 × 40 − 10 = 110°')],
 puf='Dış açı = komşu olmayan iki iç açının toplamıdır; iç açılar toplamı denklemiyle karıştırma.',sekil=SK)

# ================= 03 · İç açıortaylar · orta =================
kartla('K-GUA-03','İki iç açıortayın kesişimi','Açıortaylar B ve C açılarını yarıya böler; BIC üçgeni ve ABC üçgeninin iç açı toplamları birlikte kullanılır.','Yarıyı unutmak; 90° eklemek yerine 180°’den çıkarmak.','orta',3,'ge-ua-aciortay-ic','İç açıortayların kesişimi')
Av=56; BIC=90+Av//2
assert BIC==118 and 2*(118-90)==56 and 118-90==28 and 118//2==59 and 180-118==62 and 2*(180-118)==124
A3,B3,C3=tri(56,70,54,5.6)
a_=dist(B3,C3); b_=dist(A3,C3); c_=dist(A3,B3); I3=((a_*A3[0]+b_*B3[0]+c_*C3[0])/(a_+b_+c_),(a_*A3[1]+b_*B3[1]+c_*C3[1])/(a_+b_+c_))
assert abs(ang(I3,B3,C3)-118)<1e-9 and abs(ang(B3,A3,I3)-ang(B3,I3,C3))<1e-9
f=F(); f.poly([A3,B3,C3]); f.line(B3,I3); f.line(C3,I3)
f.arc(B3,A3,I3,.7); f.arc(B3,I3,C3,.7); f.arc(C3,A3,I3,.7); f.arc(C3,A3,I3,.82); f.arc(C3,I3,B3,.7); f.arc(C3,I3,B3,.82)
f.arc(A3,B3,C3,.6,'$x$',1.0)
f.arc(I3,B3,C3,.5,'$118^\\circ$',1.0)
f.vl('A',A3,(0,1),.3); f.vl('B',B3,(-1,-.6),.3); f.vl('C',C3,(1,-.6),.3); f.vl('I',I3,(0,1),.3)
SK=f.svg()
q('0003',tipId='ge-ua-aciortay-ic',tip='İç açıortayların kesişimi',z='orta',alt='İç Açıortaylar',kaz='İki iç açıortayın oluşturduğu açı ile üçüncü köşenin açısı arasındaki bağıntıyı kullanır.',
 kart='K-GUA-03 (iç açıortaylar) · m(BIC) verilir, A istenir',
 metin='Şekilde ABC üçgeninin B ve C köşelerindeki iç açıların açıortayları [BI] ve [CI] olup I noktasında kesişmektedir. m(BIC) = 118° dir.\nŞekil ölçekli değildir.\nBuna göre, m(BAC) = x kaç derecedir?',
 dogru=56,yan=[(28,'Bağıntıyı m(BIC) = 90° + m(A) alıp m(A) = 118° − 90° = 28° bulmuş (yarıyı unutmuş).','bilgi'),(59,'m(BIC)’in yarısını (118° ÷ 2) A açısı sanmış.','bilgi'),(62,'A açısını 180° − 118° olarak yazmış.','bilgi'),(124,'B ve C açılarının toplamını (2 × 62 = 124°) bulup sorulan A açısına geçmemiş.','dikkat')],
 istenen='m(BAC) açısının ölçüsü.',
 ip=['BIC üçgeninde B ve C’nin yarı açıları var. Bu yarı açıların toplamı ile A arasında nasıl bir bağ kurabilirsin?'],
 bilgi=[AOR,IC],
 ad=[A('BIC üçgenini yaz','Açıortaylar B ve C açılarını ikiye böler; BIC üçgeninin iç açıları toplamı 180°’dir.','(B ÷ 2) + (C ÷ 2) + 118 = 180'),A('B + C’yi bul','Önce yarı açıların toplamını, sonra B + C’yi hesapla.','(B + C) ÷ 2 = 62 · B + C = 124°'),A('A açısını bul','ABC üçgeninin iç açıları toplamını kullan.','m(A) = 180° − 124° = 56°')],
 puf='İki iç açıortay arasındaki açı BIC = 90° + A ÷ 2 dir; A bulunurken önce yarıyı çıkarıp sonra 2 ile çarp.',sekil=SK)

# ================= 04 · İç + dış açıortay · orta =================
kartla('K-GUA-04','İç ve dış açıortayın kesişimi','İç açıortay ve dış açı tanımlarıyla BCD üçgeninin açıları x cinsinden yazılır.','Yarıyı unutmak; iç–dış açıortay bağıntısını iki iç açıortayınkiyle (90° + A/2) karıştırmak.','orta',4,'ge-ua-aciortay-dis','Dış açıortaylı kesişimler')
Bd,Cd=48,56; Ad=180-Bd-Cd; assert Ad==76 and Ad//2==38
A4,B4,C4=tri(76,48,56,5.0); F4=(C4[0]+1.9,0)
dB=(cos(radians(Bd/2)),sin(radians(Bd/2))); dC=(cos(radians((180-Cd)/2)),sin(radians((180-Cd)/2)))
D4=inter(B4,dB,C4,dC)
assert abs(ang(D4,B4,C4)-38)<1e-9 and abs(ang(C4,A4,D4)-ang(C4,D4,F4))<1e-9 and abs(ang(B4,A4,D4)-ang(B4,D4,C4))<1e-9
assert 2*(90-38)==104 and 90-38==52 and 180-38==142 and 180-76==104
f=F(); f.poly([A4,B4,C4]); f.line(C4,F4); f.line(B4,D4); f.line(C4,D4)
f.arc(B4,A4,D4,.7); f.arc(B4,D4,C4,.7); f.arc(C4,A4,D4,.6); f.arc(C4,A4,D4,.72); f.arc(C4,D4,F4,.6); f.arc(C4,D4,F4,.72)
f.arc(D4,B4,C4,.6,'$38^\\circ$',1.15); f.arc(A4,B4,C4,.6,'$x$',1.0)
f.vl('A',A4,(-.5,1),.3); f.vl('B',B4,(-1,-.6),.3); f.vl('C',C4,(.2,-1),.3); f.vl('F',F4,(1,-.4),.3); f.vl('D',D4,(.6,1),.3)
SK=f.svg()
q('0004',tipId='ge-ua-aciortay-dis',tip='Dış açıortaylı kesişimler',z='orta',alt='İç ve Dış Açıortay',kaz='Bir iç ve bir dış açıortayın oluşturduğu açı ile üçüncü köşe açısı arasındaki bağıntıyı kullanır.',
 kart='K-GUA-04 (iç + dış açıortay) · m(BDC) verilir, A istenir',
 metin='Şekilde ABC üçgeninin [BC] kenarı C noktasından F noktasına kadar uzatılmıştır. [BD], ABC açısının; [CD] ise ACF dış açısının açıortayıdır. m(BDC) = 38° dir.\nŞekil ölçekli değildir.\nBuna göre, m(BAC) = x kaç derecedir?',
 dogru=76,yan=[(38,'Verilen m(BDC) = 38°’yi A açısı sanmış.','dikkat'),(52,'m(A) = 90° − m(BDC) = 52° bağıntısını uygulamış.','bilgi'),(104,'İki iç açıortay bağıntısını (BDC = 90° − A ÷ 2 gibi) kullanıp A = 2 × (90° − 38°) = 104° bulmuş.','bilgi'),(142,'BDC açısının bütünleri olan 180° − 38°’yi yazmış.','dikkat')],
 istenen='m(BAC) açısının ölçüsü.',
 ip=['BCD üçgeninde D’deki açıyı, B ve C köşelerindeki açıların yarılarıyla ilişkilendir; dış açıyı unutma.'],
 bilgi=[AOR,DIS],
 ad=[A('Açıları adlandır','ABC üçgeninde B ve C iç açılarına b ve c diyelim. [BD] açıortay olduğundan DBC = b ÷ 2.','m(DBC) = b ÷ 2'),A('DCB açısını yaz','ACF dış açısı b + A ya da 180° − c’dir; [CD] onu ikiye böler. DCB = c + (180° − c) ÷ 2.','m(DCB) = 90° + c ÷ 2'),A('BCD üçgeninin açıları toplamı','180° üzerinden D açısını çıkar.','38 + b ÷ 2 + 90 + c ÷ 2 = 180 · (b + c) ÷ 2 = 52'),A('A açısını bul','b + c = 104°; ABC üçgeninde A’yı hesapla.','m(BAC) = 180° − 104° = 76°')],
 puf='Bir iç ve bir dış açıortayın kesişiminde oluşan açı, o iki köşeye komşu olmayan köşe açısının yarısıdır.',sekil=SK)

# ================= 05 · Kelebek · orta =================
kartla('K-GUA-05','Kelebek (ters açı) bağıntısı','İki doğru parçası kesişince karşılıklı iki üçgende ters açılar eşittir; üstteki iki açının toplamı alttaki iki açının toplamına eşittir.','Dörtgen açıları toplamını (360°) kelebeğe uygulamak; toplamı istenen açı sanmak.','orta',3,'ge-ua-kelebek','Kelebek (iki üçgen, ters açılar)')
x=30; EAB=x+10; EBA=2*x+20; ECD=65; EDC=55
assert EAB+EBA==ECD+EDC==120 and EAB==40 and EBA==80 and 180-EBA==100 and 140==180-EAB
assert 3*x+30==120
A5,B5=(-3.0,2.3),(3.0,2.3); C5=mul(A5,-1.1); D5=mul(B5,-1.45); E5=(0,0)
f=F(); f.line(A5,C5); f.line(B5,D5); f.line(A5,B5); f.line(C5,D5)
f.arc(A5,B5,E5,.9,'$(x+10)^\\circ$',1.9); f.arc(B5,E5,A5,.9,'$(2x+20)^\\circ$',1.95)
f.arc(C5,E5,D5,.8,'$65^\\circ$',1.5); f.arc(D5,C5,E5,.8,'$55^\\circ$',1.5)
f.vl('A',A5,(-1,.7),.3); f.vl('B',B5,(1,.7),.3); f.vl('C',C5,(1,-.7),.3); f.vl('D',D5,(-1,-.7),.3); f.node((.32,0),'$E$')
SK=f.svg()
q('0005',tipId='ge-ua-kelebek',tip='Kelebek (iki üçgen, ters açılar)',z='orta',alt='Kelebek Şekli',kaz='Kelebek şeklinde karşılıklı iki üçgenin açıları arasındaki ilişkiyi kullanarak cebirsel açıyı bulur.',
 kart='K-GUA-05 (kelebek) · iki cebirsel açı, ters açı eşitliği',
 metin='Şekilde [AC] ile [BD] doğru parçaları E noktasında kesişmektedir. m(EAB) = (x + 10)°, m(EBA) = (2x + 20)°, m(ECD) = 65° ve m(EDC) = 55° dir.\nŞekil ölçekli değildir.\nBuna göre, m(EAB) kaç derecedir?',
 dogru=40,yan=[(80,'İstenen EAB yerine m(EBA) = 2x + 20 = 80° değerini yazmış.','dikkat'),(100,'EAB yerine EBA’nın bütünlerini (180° − 80°) almış.','dikkat'),(120,'Alttaki iki açının toplamını (65° + 55°) istenen açı sanmış.','dikkat'),(140,'EAB’nin bütünlerini (180° − 40°) yazmış.','dikkat')],
 istenen='m(EAB) açısının ölçüsü.',
 ip=['E noktasında oluşan açılara bak: iki üçgenin açıları arasında hangi ortak ilişki var?'],
 bilgi=[KEL,IC],
 ad=[A('Ters açıları eşitle','AEB ve CED ters açılar olduğundan eşittir; iki üçgende kalan iki açının toplamı da eşit olur.','m(EAB) + m(EBA) = m(ECD) + m(EDC)'),A('Denklemi kur','Verilen değerleri yaz.','(x + 10) + (2x + 20) = 65 + 55'),A('x’i bul','Benzer terimleri topla.','3x + 30 = 120 · x = 30'),A('Sorulan açıyı yaz','x yerine 30 koy.','m(EAB) = 30 + 10 = 40°')],
 puf='Kelebekte kesişen iki üçgenin ters açıları eşit olduğundan, üstteki iki açının toplamı alttaki iki açının toplamına eşittir.',sekil=SK)

# ================= 06 · Ok biçimli dörtgen · orta (hikâyeli) =================
kartla('K-GUA-06','Ok (kırık) dörtgen','Dörtgenin içe doğru kırık köşesindeki açı, karşı köşe açısı ile iki yan açının toplamına eşittir.','Dörtgen açıları toplamını (360°) kullanmak; x bulup bırakmak.','orta',4,'ge-ua-dortgen','Dörtgende açılar',kalip='hikâyeli')
x=30; BAC=40; ABD=x+5; ACD=2*x-5
assert BAC+ABD+ACD==130 and ACD==55 and ABD==35 and 180-130==50 and 130-BAC==90
Ab,Bb,Cb=tri(50,65,65,6.4)
# D: ABD=35 -> DBC=65-35=30 ; ACD=55 -> DCB=75-55=20
dB=(cos(radians(25)),sin(radians(25))); dC=(cos(radians(180-25)),sin(radians(180-25)))
Db=inter(Bb,dB,Cb,dC)
assert abs(ang(Bb,Ab,Db)-40)<1e-9 and abs(ang(Cb,Ab,Db)-40)<1e-9 and abs(ang(Db,Bb,Cb)-130)<1e-9
f=F(); f.poly([Ab,Bb,Db,Cb])
f.arc(Ab,Bb,Cb,.8,'$40^\\circ$',1.7); f.arc(Bb,Ab,Db,.9,'$(x+5)^\\circ$',2.4); f.arc(Cb,Ab,Db,.9,'$(2x-5)^\\circ$',2.5)
f.arc(Db,Bb,Cb,.55,'$130^\\circ$',1.1)
f.vl('A',Ab,(0,1),.3); f.vl('B',Bb,(-1,-.6),.3); f.vl('C',Cb,(1,-.6),.3); f.vl('D',Db,(0,1),.32)
SK=f.svg()
q('0006',tipId='ge-ua-dortgen',tip='Dörtgende açılar',z='orta',alt='Ok Biçimli Dörtgen',kaz='Ok biçimli dörtgende kırık köşedeki açının diğer üç açının toplamına eşitliğini kullanarak cebirsel açıyı bulur.',kalip='hikâyeli',
 kart='K-GUA-06 (ok dörtgeni) · BDC verilir, ACD istenir',
 metin='Bir reklam panosunun ok biçimli levhası, şekildeki ABDC dörtgeniyle gösterilmiştir. Levhanın A köşesindeki açı m(BAC) = 40°, B köşesinde m(ABD) = (x + 5)° ve C köşesinde m(ACD) = (2x − 5)° dir. D noktasındaki çentik açısı m(BDC) = 130° dir.\nŞekil ölçekli değildir.\nBuna göre, m(ACD) kaç derecedir?',
 dogru=55,yan=[(30,'Denklemden yalnız x = 30’u bulup sorulan açıyı hesaplamamış.','dikkat'),(35,'İstenen C açısı yerine B köşesindeki ABD açısını (x + 5 = 35°) hesaplamış.','dikkat'),(50,'D noktasındaki açıyı 180° − 130° = 50° alıp onu kullanmaya çalışmış; bulduğu değeri açı sanmış.','bilgi'),(90,'130° − 40° = 90° bulup bu toplamı (ABD + ACD) istenen açı sanmış.','dikkat')],
 istenen='m(ACD) açısının ölçüsü.',
 ip=['D’deki 130°’lik açı ile diğer üç açı arasında nasıl bir toplam ilişkisi var? [AD] doğrusunu çizip iki üçgene bakmayı dene.'],
 bilgi=[OK],
 ad=[A('Bağıntıyı yaz','ok biçimli dörtgende BDC açısı A, ABD ve ACD açılarının toplamıdır.','m(BDC) = m(A) + m(ABD) + m(ACD)'),A('Denklemi kur','Verilen ifadeleri yerine yaz.','40 + (x + 5) + (2x − 5) = 130'),A('x’i bul','Benzer terimleri topla.','3x + 40 = 130 · x = 30'),A('Sorulan açıyı yaz','x yerine 30 koy.','m(ACD) = 2 × 30 − 5 = 55°')],
 puf='İçbükey (ok) dörtgende kırık köşedeki açı, karşısındaki köşe ile yan iki açının toplamına eşittir.',sekil=SK)

# ================= 07 · Katlama · zor (hikâyeli) =================
kartla('K-GUA-07','Üçgen kâğıdı katlama','Katlanan köşe, kat doğrusu tarafından iki eş açıya ayrılır; iki köşede doğru üzerindeki açılardan ADE ve AED bulunup A hesaplanır.','Katlanan açıyı (BDF) ADE ile karıştırmak; ADE yerine BDF/2 almak.','zor',4,'ge-ua-katlama','Üçgen kâğıdı katlama',kalip='hikâyeli')
BDF,CEF=70,50; ADE=(180-BDF)//2; AED=(180-CEF)//2; Aa=180-ADE-AED
assert (ADE,AED,Aa)==(55,65,60) and BDF+CEF==120 and 180-BDF==110 and 180-CEF==130
Bq,Cq=64,56; t=3.2
BDl=t*sin(radians(180-Bq-BDF))/sin(radians(BDF)); DFl=t*sin(radians(Bq))/sin(radians(BDF))
D7=pol(Bq,BDl); A7=pol(Bq,BDl+DFl); B7=(0.0,0.0); F7=(t,0.0); C7=(A7[0]+A7[1]/tan(radians(Cq)),0.0)
# E: AC ile AF'nin orta dikmesinin kesişimi
M=mid(A7,F7); nAF=sub(F7,A7); dAC=sub(C7,A7); perp=(-nAF[1],nAF[0])
E7=inter(M,perp,A7,dAC)
assert abs(dist(D7,A7)-dist(D7,F7))<1e-9 and abs(dist(E7,A7)-dist(E7,F7))<1e-9
assert abs(ang(D7,B7,F7)-70)<1e-9 and abs(ang(E7,C7,F7)-50)<1e-9 and abs(ang(A7,B7,C7)-60)<1e-9
f=F(); f.poly([A7,B7,C7]); f.fill([D7,F7,E7],'fill=vurgu!25'); f.poly([D7,F7,E7]); f.line(D7,E7)
f.arc(D7,B7,F7,.55,'$70^\\circ$',1.1); f.arc(E7,F7,C7,.55,'$50^\\circ$',1.05); f.arc(A7,B7,C7,.55,'$x$',1.0)
f.vl('A',A7,(0,1),.3); f.vl('B',B7,(-1,-.6),.3); f.vl('C',C7,(1,-.6),.3); f.vl('D',D7,(-1,.2),.3); f.vl('E',E7,(1,.2),.3); f.vl('F',F7,(0,-1),.3)
SK=f.svg()
q('0007',tipId='ge-ua-katlama',tip='Üçgen kâğıdı katlama',z='zor',alt='Katlama',kaz='Katlamada eş açıları kullanarak katlanan köşenin açısını bulur.',kalip='hikâyeli',
 kart='K-GUA-07 (katlama) · BDF ve CEF verilir, A istenir',
 metin='Üçgen biçimli bir kâğıt, ABC üçgeniyle gösterilmiştir. D ∈ [AB] ve E ∈ [AC] olmak üzere [DE] doğrusu boyunca katlanarak A köşesi, [BC] kenarı üzerindeki F noktasına getirilmiştir. Katlama sonunda m(BDF) = 70° ve m(CEF) = 50° olmuştur.\nŞekil ölçekli değildir.\nBuna göre, kâğıdın A köşesindeki açının ölçüsü m(BAC) = x kaç derecedir?',
 dogru=60,yan=[(70,'Verilen m(BDF) = 70°’yi istenen A açısı sanmış.','dikkat'),(110,'BDF’nin bütünleri olan ADF açısını (180° − 70°) A açısı sanmış.','dikkat'),(120,'Verilen iki açıyı toplayıp (70° + 50°) A açısı sanmış.','dikkat'),(130,'CEF’nin bütünleri olan AEF açısını (180° − 50°) A açısı sanmış.','dikkat')],
 istenen='m(BAC) açısının ölçüsü.',
 ip=['D ve E köşelerinde doğru üzerindeki açılara bak: katlanınca eşit olan iki açı hangileri?'],
 bilgi=[KATL,IC],
 ad=[A('D köşesindeki açıyı bul','Katlanınca ADE ile FDE eşittir; A, D, B doğrusal olduğundan ADE + FDE + BDF = 180°.','2 × m(ADE) + 70 = 180 · m(ADE) = 55°'),A('E köşesindeki açıyı bul','Aynı mantıkla AED ile FED eşittir; A, E, C doğrusaldır.','2 × m(AED) + 50 = 180 · m(AED) = 65°'),A('A açısını hesapla','ADE üçgeninde iç açıların toplamı 180°’dir.','x = 180° − 55° − 65° = 60°')],
 puf='Katlamada köşe, kat doğrusuyla iki eş açıya ayrılır: doğru üzerindeki iki köşede “180° − verilen” değerini ikiye böl.',sekil=SK)

# ================= 08 · İkizkenar + eşit kenarlar · zor =================
kartla('K-GUA-08','Eş kenarlı üç ikizkenar üçgen','Eşit kenarlardan taban açıları eşitlenir; dış açı kuralıyla bir x cinsinden denklem kurulur.','Dış açı yerine iç açıyı yazıp x’i yanlış bulmak.','zor',5,'ge-ua-ikizkenar','Birden çok ikizkenar üçgen ve dış açı')
x=36; assert x==180-4*x+0 or 5*x==180
Bx=36; BAD=36; ADC=2*Bx; DAC=2*Bx; Cx=180-4*Bx; BAC=BAD+DAC
assert Cx==Bx==36 and BAC==108 and ADC==72 and DAC==72 and 3*60==180 and 60+60==120 and 4*36==144
L8=6.0; A8,B8,C8=tri(108,36,36,L8)
cl=dist(C8,A8); D8=(C8[0]-cl,0.0)
assert abs(dist(A8,D8)-dist(B8,D8))<1e-9 and abs(dist(C8,D8)-dist(C8,A8))<1e-9 and abs(dist(A8,B8)-dist(A8,C8))<1e-9 and abs(ang(A8,B8,D8)-36)<1e-9
f=F(); f.poly([A8,B8,C8]); f.line(A8,D8)
f.tick(A8,B8,2); f.tick(A8,C8,2); f.tick(C8,D8,2); f.tick(A8,D8,1); f.tick(B8,D8,1)
f.vl('A',A8,(0,1),.3); f.vl('B',B8,(-1,-.6),.3); f.vl('C',C8,(1,-.6),.3); f.vl('D',D8,(0,-1),.3)
SK=f.svg()
q('0008',tipId='ge-ua-ikizkenar',tip='Birden çok ikizkenar üçgen ve dış açı',z='zor',alt='İkizkenar Üçgenler Zinciri',kaz='Eşit kenarlardan taban açılarını x cinsinden yazıp dış açı kuralıyla denklem kurar.',
 kart='K-GUA-08 (üç ikizkenar) · AB = AC, AD = BD, CD = CA',
 metin='Şekilde ABC bir üçgendir ve D noktası [BC] üzerindedir. Bu üçgende |AB| = |AC|, |AD| = |BD| ve |CD| = |CA| dir. Eşit uzunluktaki kenarlar aynı işaretle gösterilmiştir.\nŞekil ölçekli değildir.\nBuna göre, m(BAC) kaç derecedir?',
 dogru=108,yan=[(36,'Bulduğu x = m(ABC) = 36°’yi istenen A açısı sanmış.','dikkat'),(72,'A açısı yerine m(DAC) = m(ADC) = 72° değerini yazmış.','dikkat'),(120,'ADC’yi dış açı kuralıyla değil m(ADC) = x alıp x = 60° bulmuş; A = 60° + 60° = 120°.','bilgi'),(144,'Bulduğu 4x = 144° değerini (x = m(ABC) iken) A açısı sanmış.','dikkat')],
 istenen='m(BAC) açısının ölçüsü.',
 ip=['m(ABC) = x deyip ABD ve ADC üçgenlerinde eşit kenarlara karşılık gelen açıları x cinsinden yaz.'],
 bilgi=[IKIZ,DIS],
 ad=[A('B açısını x al','|AB| = |AC| olduğundan m(B) = m(C) = x. |AD| = |BD| olduğundan m(BAD) = x.','m(B) = m(C) = m(BAD) = x'),A('ADC dış açısını yaz','ADC, ABD üçgeninin dış açısıdır: komşu olmayan B ve BAD açılarının toplamı.','m(ADC) = x + x = 2x'),A('Üçgen ADC’yi incele','|CD| = |CA| olduğundan m(DAC) = m(ADC) = 2x; ADC üçgeninde C açısı x’tir.','x + 2x + 2x = 180 · x = 36'),A('A açısını bul','A açısı BAD ve DAC’nin toplamıdır.','m(BAC) = x + 2x = 3x = 108°')],
 puf='Eşit kenarlı üçgen zincirlerinde bir açıya x de; eşit kenarlar ve dış açı kuralıyla diğer açıları x cinsinden yaz.',sekil=SK)

# ================= 09 · Dış açıortaylar · zor =================
kartla('K-GUA-09','Dış açıortaylı kesişimler','Dış açıların yarıları BEC üçgeninde kullanılır; verilen ifadelerle denklem kurulup A bulunur.','Bağıntıyı iç açıortayınkiyle (90° + A/2) karıştırmak; yarıyı unutmak.','zor',4,'ge-ua-aciortay-dis','Dış açıortaylı kesişimler')
x=20; Aa=4*x; BEC=x+30
assert Aa==80 and BEC==50==90-Aa//2
assert 90-4*12==12+30 and 4*12==48 and 2*30==30+30 and 4*30==120
A9,B9,C9=tri(80,55,45,5.0)
Pp=add(B9,mul(un(sub(B9,A9)),1.9)); Qq=add(C9,mul(un(sub(C9,A9)),1.9))
dBc=bis(B9,C9,Pp); dCc=bis(C9,B9,Qq); E9=inter(B9,dBc,C9,dCc)
assert abs(ang(E9,B9,C9)-50)<1e-9 and abs(ang(B9,C9,E9)-ang(B9,E9,Pp))<1e-9
f=F(); f.poly([A9,B9,C9]); f.line(B9,Pp); f.line(C9,Qq); f.line(B9,E9); f.line(C9,E9)
f.arc(B9,C9,E9,.6); f.arc(B9,E9,Pp,.6); f.arc(C9,B9,E9,.6); f.arc(C9,B9,E9,.72); f.arc(C9,E9,Qq,.6); f.arc(C9,E9,Qq,.72)
f.arc(A9,B9,C9,.7,'$4x^\\circ$',1.25); f.arc(E9,B9,C9,.55,'$(x+30)^\\circ$',1.45)
f.vl('A',A9,(0,1),.3); f.vl('B',B9,(-1,-.3),.3); f.vl('C',C9,(1,-.3),.3); f.vl('P',Pp,(-1,-.5),.3); f.vl('Q',Qq,(1,-.5),.3); f.vl('E',E9,(0,-1),.3)
SK=f.svg()
q('0009',tipId='ge-ua-aciortay-dis',tip='Dış açıortaylı kesişimler',z='zor',alt='İki Dış Açıortay',kaz='İki dış açıortayın oluşturduğu açı ile karşı köşenin açısı arasındaki bağıntıyı cebirsel açılarla kullanır.',
 kart='K-GUA-09 (iki dış açıortay) · 4x ve x + 30',
 metin='Şekilde ABC üçgeninin [AB] ve [AC] kenarları, B ve C noktalarının ötesinde sırasıyla P ve Q noktalarına kadar uzatılmıştır. [BE], CBP açısının; [CE] ise BCQ açısının açıortayıdır. m(BAC) = (4x)° ve m(BEC) = (x + 30)° dir.\nŞekil ölçekli değildir.\nBuna göre, m(BAC) kaç derecedir?',
 dogru=80,yan=[(20,'Denklemden yalnız x = 20’yi bulup sorulan açıyı hesaplamamış.','dikkat'),(48,'Bağıntıyı BEC = 90° − A yazıp (yarıyı unutarak) 90 − 4x = x + 30 çözmüş; x = 12, A = 48°.','bilgi'),(50,'İstenen A açısı yerine m(BEC) = x + 30 = 50° değerini yazmış.','dikkat'),(120,'BEC = A ÷ 2 alıp 2x = x + 30 çözmüş; x = 30 ve A = 120° bulmuş.','bilgi')],
 istenen='m(BAC) açısının ölçüsü.',
 ip=['BEC üçgeninde B ve C köşelerindeki açılar dış açıların yarılarıdır. Bu yarıları A cinsinden yazmayı dene.'],
 bilgi=[AOR,DIS],
 ad=[A('B ve C’deki yarı açılar','Dış açılar 180° − b ve 180° − c; açıortaylar bunları ikiye böler.','m(EBC) = 90° − b ÷ 2 · m(ECB) = 90° − c ÷ 2'),A('BEC açısını yaz','BEC üçgeninin iç açıları toplamı 180°’dir; b + c = 180° − A.','m(BEC) = 180° − (180° − (b + c) ÷ 2) = 90° − A ÷ 2'),A('Denklemi kur','A = 4x ve BEC = x + 30 yerine yaz.','x + 30 = 90 − 2x · 3x = 60 · x = 20'),A('Sorulan açıyı yaz','x yerine 20 koy.','m(BAC) = 4 × 20 = 80°')],
 puf='İki dış açıortay arasındaki açı 90° − A ÷ 2, iki iç açıortay arasındaki açı ise 90° + A ÷ 2 dir.',sekil=SK)

# ================= 10 · Dörtgende iç açıortaylar · orta =================
kartla('K-GUA-10','Dörtgende iki iç açıortay','BEC üçgeninden B + C bulunur, dörtgenin açı toplamıyla A + D ve x belirlenir.','Yarıyı unutmak; B + C yerine A + D’yi vermek.','orta',4,'ge-ua-dortgen','Dörtgende açılar')
x=46; Aq=2*x+30; Dq=x+40; BECq=104
assert Aq==122 and Dq==86 and (Aq+Dq)//2==BECq and 360-(Aq+Dq)==152 and 3*x+70==208 and 2*37+30==104 and x==46
Bq,Cq=80,72; Bq0=(0.0,0.0); Cq0=(6.0,0.0)
def dort(lD):
    A_=pol(Bq,3.0); D_=add(Cq0,pol(180-Cq,lD)); return A_,D_
lo,hi=3.0,6.0
for _ in range(80):
    mdl=(lo+hi)/2; A_,D_=dort(mdl); aa=ang(A_,Bq0,D_)
    if aa<Aq: lo=mdl
    else: hi=mdl
Aq0,Dq0=dort((lo+hi)/2)
assert abs(ang(Aq0,Bq0,Dq0)-122)<1e-6 and abs(ang(Dq0,Aq0,Cq0)-86)<1e-6 and abs(ang(Bq0,Aq0,Dq0)+0-ang(Bq0,Aq0,Dq0))<1e-9
dB_=(cos(radians(Bq/2)),sin(radians(Bq/2))); dC_=(cos(radians(180-Cq/2)),sin(radians(180-Cq/2)))
E10=inter(Bq0,dB_,Cq0,dC_)
assert abs(ang(E10,Bq0,Cq0)-104)<1e-9
f=F(); f.poly([Bq0,Cq0,Dq0,Aq0]); f.line(Bq0,E10); f.line(Cq0,E10)
f.arc(Bq0,Aq0,E10,.7); f.arc(Bq0,E10,Cq0,.7); f.arc(Cq0,Dq0,E10,.7); f.arc(Cq0,Dq0,E10,.82); f.arc(Cq0,E10,Bq0,.7); f.arc(Cq0,E10,Bq0,.82)
f.arc(Aq0,Dq0,Bq0,.5,'$(2x+30)^\\circ$',1.1); f.arc(Dq0,Cq0,Aq0,.5,'$(x+40)^\\circ$',1.45); f.arc(E10,Bq0,Cq0,.5,'$104^\\circ$',1.0)
f.vl('A',Aq0,(-1,.5),.3); f.vl('B',Bq0,(-1,-.6),.3); f.vl('C',Cq0,(1,-.6),.3); f.vl('D',Dq0,(.4,1),.3); f.vl('E',E10,(0,1),.3)
SK=f.svg()
q('0010',tipId='ge-ua-dortgen',tip='Dörtgende açılar',z='orta',alt='Dörtgende Açıortaylar',kaz='Dörtgende iki iç açıortayın oluşturduğu açıdan B + C’yi, sonra dörtgen açı toplamından x’i bulur.',
 kart='K-GUA-10 (dörtgen, açıortaylar) · BEC verilir, x istenir',
 metin='Şekilde ABCD dörtgeninin B ve C köşelerindeki iç açıların açıortayları [BE] ve [CE] olup E noktasında kesişmektedir. m(DAB) = (2x + 30)°, m(CDA) = (x + 40)° ve m(BEC) = 104° dir.\nŞekil ölçekli değildir.\nBuna göre, x kaçtır?',
 dogru=46,yan=[(37,'BEC açısını A açısına eşitleyip 2x + 30 = 104 çözmüş.','bilgi'),(86,'x yerine D köşesinin açısını (x + 40 = 86°) yazmış.','dikkat'),(122,'x yerine A köşesinin açısını (2x + 30 = 122°) yazmış.','dikkat'),(152,'B + C = 152° bulup A + D denklemine geçmemiş.','dikkat')],
 istenen='x’in değeri.',
 ip=['BEC üçgeninin açılarından B ile C’yi ilişkilendir; sonra dörtgenin iç açılar toplamını kullan.'],
 bilgi=[DORT,AOR],
 ad=[A('BEC üçgenini yaz','Açıortaylar B ve C açılarını ikiye böler; BEC üçgeninde iç açıların toplamı 180°’dir.','(B ÷ 2) + (C ÷ 2) + 104 = 180'),A('B + C’yi bul','Yarı açıların toplamını iki katına çıkar.','(B + C) ÷ 2 = 76 · B + C = 152°'),A('A + D’yi bul','Dörtgenin iç açıları toplamı 360°’dir.','A + D = 360° − 152° = 208°'),A('x’i çöz','Verilen ifadeleri yerine yaz.','(2x + 30) + (x + 40) = 208 · 3x = 138 · x = 46')],
 puf='Dörtgende iki iç açıortayın oluşturduğu açıdan B + C bulunur; sonra 360° − (B + C) ile A + D’ye geçilir.',sekil=SK)

bit('ucgenaci','Üçgende Açılar','geo|Üçgende Açılar')
