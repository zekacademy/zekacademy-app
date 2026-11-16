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

TIPK={}
def konu(k,ad): P.k=k; P.konu_adi=ad; H.KONU=ad
def kartla(id,alt,fikir,tuzak,z,adim,tipId,tip,kalip='şekilli'):
    kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,'ÖSYM 2018–2026 TYT Geometri soruları (yalnız mantık) · MEB 9–10. sınıf geometri'); TIPK[tipId]=P.k
def q(no,ad,kalip='şekilli',**k): mk(P,no,ad=ad,adim=len(ad),kalip=kalip,**k)
def bitir_geo(onek,adi):
    for qq in P.ANA: qq['kardes']=None
    P.yaz(os.path.join(GD,f'{onek}-1.json'),f'/tmp/bos-{onek}.json')
    tipler={}
    for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=TIPK[c['tipId']]))['kartlar'].append(c['id'])
    json.dump(dict(konu=adi,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 TYT Geometri çıkmış soruları (yalnız mantık), MEB 9–10. sınıf geometri müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar',f'{onek}.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler))
P=Parti('yamuk','Yamuk','geo|Yamuk',ders='TYT Geometri',idon='tytgeo')
YAC=B('Yamukta açılar','AB // DC ise aynı yan kenarın uçlarındaki açılar bütünlerdir: m(A) + m(D) = 180° ve m(B) + m(C) = 180°. Örnek: bir yan kenar boyunca açılardan biri 50° ise diğeri 130°’dir')
ORTAT=B('Orta taban','yan kenarların orta noktalarını birleştiren doğru parçası tabanlara paraleldir ve uzunluğu tabanlar toplamının yarısıdır: |EF| = (a + c) ÷ 2. Örnek: tabanlar 10 ve 18 ise orta taban 14’tür')
IKIZ=B('İkizkenar yamuk ve iç ters açılar','yan kenarları eşit olan yamukta taban açıları ikişer ikişer eşittir. Paralel doğruların oluşturduğu iç ters açılar eşittir: AB // DC ise m(BAC) = m(ACD). Eşit kenarlı üçgende karşıdaki açılar eşittir')
DIKY=B('Yamuğun alanı','alan = (taban + taban) ÷ 2 × yükseklik. Dik yamukta dik yan kenar yüksekliktir; eğik yan kenar, yükseklik ve taban farkıyla Pisagordan bulunur. Örnek: tabanlar 4 ve 10, yükseklik 3 ise alan 7 × 3 = 21’dir')
OTALAN=B('Orta tabanın ayırdığı yamuklar','orta taban yamuğu yükseklikleri eşit iki yamuğa ayırır; her yamuğun alanı kendi tabanlarının toplamıyla orantılıdır. Örnek: tabanlar 2 ve 6 ise orta taban 4’tür; üst yamuk ile alt yamuğun alanları (2 + 4) : (4 + 6) = 3 : 5 oranındadır')
KEL=B('Köşegenlerin oluşturduğu üçgenler','AB // DC olan yamukta köşegenler E’de kesişirse ABE ve CDE benzerdir ve |AE| : |EC| = |BE| : |ED| = |AB| : |DC| olur. Köşeleri ortak, tabanları aynı doğru üzerinde üçgenlerde alanlar taban oranındadır; AED ile BEC üçgenlerinin alanları eşittir. Örnek: |AB| : |DC| = 1 : 2 ise ABE : AED = 1 : 2’dir')
PAR=B('Köşegen kesişiminden geçen paralel','köşegenlerin kesişim noktasından tabanlara çizilen paralel doğru, yan kenarlarla benzer üçgenler kurar: EK // DC ise EK / DC = AK / AC dir. Örnek: tabanlar 3 ve 6 ise AK : AC = 3 : 9 = 1 : 3 olur ve DC = 6 için EK = 2’dir')
UZANTI=B('Yan kenarları uzatma','yamuğun yan kenarları uzatılınca oluşan küçük ve büyük üçgenler benzerdir: EAB ~ EDC ise |EA| / |ED| = |AB| / |DC|. Örnek: |AB| = 3, |DC| = 5, |EA| = 6 ise |ED| = 10’dur')

# ===== 01 · açılar · kolay =====
konu('geo|Yamuk','Yamuk')
kartla('K-GYM-01','Yamukta yan kenar açıları','Yan kenarın iki ucundaki açılar bütünlerdir; önce bilinmeyen x bir yan kenardan bulunur, sonra diğer yan kenara geçilir.','Karşı köşedeki açıyı eşit sanmak; aynı taban üzerindeki açıları eşit ya da bütünler sanmak.','kolay',3,'ge-ym-aci','Yamukta açıları bulma')
x1=40; A1=2*x1+20; D1=x1+40; C1=x1+25; B1=180-C1; assert A1+D1==180 and (A1,D1,C1,B1)==(100,80,65,115)
assert 2*20+20==20+40 and 180-(20+25)==135 and 2*40+20==100
h1=2.4; Dd=(0,0); Cd=(5.3,0); Ad=(h1/tan(radians(D1)),h1); b1=h1/sin(radians(C1)); Bd=(Cd[0]+b1*cos(radians(180-C1)),h1)
assert abs(ang(Dd,Ad,Cd)-D1)<1e-9 and abs(ang(Ad,Dd,Bd)-A1)<1e-9 and abs(ang(Cd,Dd,Bd)-C1)<1e-9 and abs(ang(Bd,Ad,Cd)-B1)<1e-9
f=F(); f.poly([Ad,Bd,Cd,Dd]); f.par(Ad,Bd); f.par(Dd,Cd)
f.arc(Ad,Bd,Dd,.4,'$2x+20^\\circ$',1.15); f.arc(Dd,Ad,Cd,.4,'$x+40^\\circ$',1.1); f.arc(Cd,Bd,Dd,.5,'$x+25^\\circ$',1.15)
f.vl('A',Ad,(-1,1),.3); f.vl('B',Bd,(1,1),.3); f.vl('C',Cd,(1,-1),.3); f.vl('D',Dd,(-1,-1),.3)
SK1=f.svg()
q('0001',tipId='ge-ym-aci',tip='Yamukta açıları bulma',z='kolay',alt='Yamukta Açılar',kaz='Yamukta yan kenar açılarının bütünler olduğunu kullanarak bilinmeyen açıyı bulur.',
 kart='K-GYM-01 (yamukta açılar) · iki yan kenar, x cebirsel',
 metin='Şekildeki ABCD yamuğunda [AB] // [DC] dir ve bazı açıların ölçüleri x cinsinden verilmiştir.\nŞekil ölçekli değildir.\nBuna göre, m(ABC) kaç derecedir?',
 dogru=115,yan=[(65,'B açısını C açısına eşit sanmış.','bilgi'),(80,'m(ABC) açısını m(ADC) ile eşit alıp 80° yazmış.','bilgi'),(100,'Üst tabanın iki ucundaki açıları (A ve B) eşit sanmış.','bilgi'),(135,'A ile D açılarını eşitleyip x = 20 bulmuş; C = 45°, B = 135° çıkarmış.','bilgi')],
 istenen='m(ABC) açısının ölçüsü (derece).',
 ip=['Hangi iki açı aynı yan kenarın uçlarındadır? Bu açıların toplamı hangi değere eşittir; böylece x’i bulabilirsin.'],
 bilgi=[YAC],
 ad=[A('x’i bul','[AD] yan kenarının uçlarındaki A ve D açıları bütünlerdir.','(2x + 20) + (x + 40) = 180 → 3x = 120 → x = 40'),A('C açısını hesapla','x yerine 40 yazılır.','m(BCD) = 40 + 25 = 65°'),A('B açısını bul','[BC] yan kenarının uçlarındaki B ve C açıları da bütünlerdir.','m(ABC) = 180° − 65° = 115°')],
 puf='Yamukta her yan kenarın iki ucundaki açılar bütünlerdir; aynı tabandaki açılar ise genelde eşit değildir.',sekil=SK1)

# ===== 02 · orta taban · kolay =====
kartla('K-GYM-02','Orta taban','Orta taban tabanların aritmetik ortalamasıdır; verilen cebirsel ifadelerle denklem kurulup x bulunur, sonra istenen taban hesaplanır.','Orta tabanı iki tabanın toplamına eşit almak; x’i cevap sanmak; alt taban yerine üst tabanı yazmak.','kolay',3,'ge-ym-orta','Orta taban uzunluğu')
x2=6; AB2=2*x2-3; DC2=3*x2+5; EF2=(AB2+DC2)/2; assert (AB2,DC2,EF2)==(9,23,16)
s=.2; D2=(0,0); C2=(DC2*s,0); A2=(.9,2.2); B2=(.9+AB2*s,2.2); E2=mid(A2,D2); F2=mid(B2,C2)
assert abs(dist(E2,F2)/s-EF2)<1e-9 and abs(E2[1]-F2[1])<1e-9
assert AB2+DC2==32 and x2==6
f=F(); f.poly([A2,B2,C2,D2]); f.par(A2,B2); f.par(D2,C2); f.line(E2,F2,'dashed'); f.tick(A2,E2); f.tick(E2,D2); f.tick(B2,F2); f.tick(F2,C2)
f.sl('$2x-3$',A2,B2,cen([A2,B2,C2,D2]),.3); f.sl('$3x+5$',D2,C2,cen([A2,B2,C2,D2]),.3)
f.node(add(mid(E2,F2),(0,.22)),'$16$')
f.vl('A',A2,(-1,1),.3); f.vl('B',B2,(1,1),.3); f.vl('C',C2,(1,-1),.3); f.vl('D',D2,(-1,-1),.3); f.vl('E',E2,(-1,0),.3); f.vl('F',F2,(1,0),.3)
SK2=f.svg()
q('0002',tipId='ge-ym-orta',tip='Orta taban uzunluğu',z='kolay',alt='Orta Taban',kaz='Orta taban bağıntısıyla cebirsel tabanlardan x’i bulup istenen taban uzunluğunu hesaplar.',
 kart='K-GYM-02 (orta taban) · AB = 2x − 3, DC = 3x + 5, EF = 16',
 metin='Şekilde yamuk biçimli bir arsanın krokisi verilmiştir. [AB] // [DC] dir, E ve F noktaları yan kenarların orta noktalarıdır ve uzunluklar metre cinsindendir. Şekil ölçekli değildir.\nBuna göre, |DC| kaç metredir?',
 dogru=23,yan=[(6,'x değerini bulup |DC| sanmış.','dikkat'),(9,'x = 6 ile |AB| = 9’u bulup cevap olarak yazmış; istenen alt tabandır.','dikkat'),(16,'Orta tabanı (|EF| = 16) alt taban sanmış.','dikkat'),(32,'|AB| + |DC| toplamını bulup cevap yazmış.','dikkat')],
 istenen='|DC| uzunluğu (m).',
 ip=['E ve F yan kenarların orta noktaları olduğuna göre |EF| ile iki taban arasında nasıl bir bağıntı vardır?'],
 bilgi=[ORTAT],
 ad=[A('Orta taban bağıntısını yaz','|EF| = (|AB| + |DC|) ÷ 2.','16 = ((2x − 3) + (3x + 5)) ÷ 2'),A('x’i bul','Önce 2 ile çarp, sonra sadeleştir.','32 = 5x + 2 → 5x = 30 → x = 6'),A('|DC|’yi hesapla','x yerine 6 yazılır.','|DC| = 3 × 6 + 5 = 23')],
 puf='Orta tabanın uzunluğu tabanların aritmetik ortalamasıdır; üç uzunluktan ikisi biliniyorsa üçüncüsü bulunur.',sekil=SK2)

# ===== 03 · ikizkenar yamuk · orta =====
kartla('K-GYM-03','İkizkenar yamukta iç ters açı','Eşit kenarlardan ikizkenar üçgen, paralel kenarlardan iç ters açı bulunur; köşegen bir taban açısını ikiye böler.','Köşegeni açıortay sanıp 70°’yi ikiye bölmeden kullanmak; yamukta açıları 180° sanmak.','orta',4,'ge-ym-ikiz','İkizkenar yamukta köşegenle oluşan açı')
sd=2.6; D3=(0,0); DC3=sd*(1+2*cos(radians(70))); C3=(DC3,0); A3=(sd*cos(radians(70)),sd*sin(radians(70))); B3=(A3[0]+sd,A3[1])
assert abs(dist(A3,D3)-sd)<1e-9 and abs(dist(B3,C3)-sd)<1e-9 and abs(ang(D3,A3,C3)-70)<1e-9 and abs(ang(C3,B3,D3)-70)<1e-9
assert abs(ang(A3,D3,C3)-75)<1e-9 and abs(ang(C3,A3,D3)-35)<1e-9 and abs(ang(A3,C3,B3)-35)<1e-9
assert 180-70-35==75 and 180-70-70==40 and 180-70==110 and 180-35==145
f=F(); f.poly([A3,B3,C3,D3]); f.line(A3,C3); f.tick(A3,B3); f.tick(A3,D3); f.tick(B3,C3)
f.arc(D3,C3,A3,.55,'$70^\\circ$',1.05); f.arc(A3,D3,C3,.5,'$x$',.95)
f.vl('A',A3,(-1,1),.3); f.vl('B',B3,(1,1),.3); f.vl('C',C3,(1,-1),.3); f.vl('D',D3,(-1,-1),.3)
SK3=f.svg()
q('0003',tipId='ge-ym-ikiz',tip='İkizkenar yamukta köşegenle oluşan açı',z='orta',alt='İkizkenar Yamuk',kaz='İkizkenar yamukta eşit kenarlar ve iç ters açıları birlikte kullanarak köşegenin oluşturduğu açıyı bulur.',
 kart='K-GYM-03 (ikizkenar yamuk) · AB = AD = BC, m(D) = 70°, köşegen AC',
 metin='Şekildeki ABCD ikizkenar yamuğunda [AB] // [DC] dir ve eşit işaretli kenarlar aynı uzunluktadır. [AC] köşegeni çizilmiştir. Şekil ölçekli değildir.\nBuna göre, x = m(DAC) kaç derecedir?',
 dogru=75,yan=[(35,'Köşegenle oluşan 35°’lik açıyı bulup x sanmış.','dikkat'),(40,'m(ACD) = 70° alıp üçgende x = 180° − 70° − 70° = 40° bulmuş.','bilgi'),(110,'x yerine A köşesindeki tüm açıyı (m(DAB) = 110°) yazmış.','dikkat'),(145,'180° − 35° işlemini yapıp 145° bulmuş (ACD yerine bütünler açıyı kullanmış).','islem')],
 istenen='x = m(DAC) açısının ölçüsü.',
 ip=['|AB| = |BC| olduğundan ABC üçgeninde hangi açılar eşittir? Paralellikten bu açının bir eşi taban üzerinde de bulunur.'],
 bilgi=[IKIZ],
 ad=[A('Taban açısını bul','İkizkenar yamukta m(C) = m(D) = 70°; ABC üçgeninde 70° ile bütünler olan B açısı 110°’dir.','m(ABC) = 180° − 70° = 110°'),A('ABC üçgenini çöz','|AB| = |BC| olduğundan A ve C açıları eşittir.','m(BAC) = (180° − 110°) ÷ 2 = 35°'),A('İç ters açıyı yaz','[AB] // [DC] olduğundan m(ACD) = m(BAC).','m(ACD) = 35°'),A('ADC üçgeninde x’i bul','Üçgenin iç açıları toplamı 180°’dir.','x = 180° − 70° − 35° = 75°')],
 puf='Köşegen çizilen ikizkenar yamukta paralel kenarlar iç ters açıları, eşit kenarlar ikizkenar üçgeni verir; ikisini birlikte kullan.',sekil=SK3)

# ===== 04 · dik yamuk alan · orta =====
kartla('K-GYM-04','Dik yamukta alan','Eğik yan kenar ile taban farkından yükseklik Pisagorla bulunur; alan tabanlar toplamının yarısı çarpı yüksekliktir.','Eğik kenarı yükseklik sanmak; tabanlar toplamını yarılamamak; üst tabanı unutmak.','orta',3,'ge-ym-alan','Yamuğun alanı')
a4,c4,e4=6,14,10; hh4=sqrt(e4**2-(c4-a4)**2); assert hh4==6; al4=(a4+c4)/2*hh4; assert al4==60
assert c4*hh4==84 and (a4+c4)/2*e4==100 and (a4+c4)*hh4==120 and c4*e4==140
s=.3; D4=(0,0); C4=(c4*s,0); A4=(0,hh4*s); B4=(a4*s,hh4*s)
assert abs(dist(B4,C4)/s-e4)<1e-9 and abs(alan([A4,B4,C4,D4])/s**2-60)<1e-9
f=F(); f.poly([A4,B4,C4,D4]); f.dik(A4,B4,D4); f.dik(D4,A4,C4); f.par(A4,B4); f.par(D4,C4)
ic=cen([A4,B4,C4,D4]); f.sl('$6$',A4,B4,ic,.28); f.sl('$14$',D4,C4,ic,.28); f.sl('$10$',B4,C4,ic,.28)
f.vl('A',A4,(-1,1),.3); f.vl('B',B4,(1,1),.3); f.vl('C',C4,(1,-1),.3); f.vl('D',D4,(-1,-1),.3)
SK4=f.svg()
q('0004',tipId='ge-ym-alan',tip='Yamuğun alanı',z='orta',alt='Yamuğun Alanı',kaz='Dik yamukta Pisagor bağıntısıyla yüksekliği bulup alanı hesaplar.',
 kart='K-GYM-04 (dik yamuk alanı) · AB = 6, DC = 14, BC = 10',
 metin='Bir bahçenin dik yamuk biçimli ABCD planı çizilmiştir. Şekil ölçekli değildir. Plandaki [AB] // [DC] dir, m(DAB) = m(ADC) = 90° dir ve uzunluklar metre cinsindendir.\nBuna göre, bahçenin alanı kaç m²’dir?',
 dogru=60,yan=[(84,'Alt tabanı (14) ile yüksekliği (6) çarpıp yamuk alanını bulduğunu sanmış.','bilgi'),(100,'Eğik kenarı (10) yükseklik alıp orta tabanla çarpmış: 10 × 10.','bilgi'),(120,'Tabanlar toplamını yüksekliğle çarpıp 2’ye bölmeyi unutmuş: 20 × 6.','islem'),(140,'Alt taban ile eğik kenarı çarpmış: 14 × 10.','bilgi')],
 istenen='Yamuk biçimli bahçenin alanı (m²).',
 ip=['Alan formülü için yüksekliğe ihtiyacın var; dik yamukta B köşesinden alt tabana indirilen dikme hangi dik üçgeni oluşturur?'],
 bilgi=[DIKY],
 ad=[A('Dik üçgeni kur','B’den [DC]’ye indirilen dikme, yüksekliği ve taban farkını dik kenar yapar.','dik kenarlar: 14 − 6 = 8 ve h · hipotenüs: 10'),A('Yüksekliği bul','Pisagor bağıntısını uygula.','h² = 10² − 8² = 36 → h = 6'),A('Alanı hesapla','Alan = (üst taban + alt taban) ÷ 2 × yükseklik.','(6 + 14) ÷ 2 × 6 = 60')],
 puf='Dik yamukta eğik kenarın taban farkı ve yükseklikle kurduğu dik üçgen, yüksekliği verir (burada 6-8-10).',sekil=SK4)

# ===== 05 · orta tabanla bölünen alan · orta =====
kartla('K-GYM-05','Orta tabanın böldüğü alanlar','Orta taban yamuğu eşit yüksekli iki yamuğa böler; alanlar kendi taban toplamlarıyla orantılıdır, toplam alandan parça bulunur.','Alanı yarı yarıya bölmek; alanı yalnız üst tabanla orantılamak; orta tabanı toplam saymak.','orta',4,'ge-ym-alan','Yamuğun alanı')
a5,c5,S5=8,16,168; e5=(a5+c5)/2; k5=S5/((a5+c5)/2); assert k5==14 and e5==12
up=(a5+e5)/2*(k5/2); lo=(e5+c5)/2*(k5/2); assert up==70 and lo==98 and up+lo==S5
assert S5*a5/(a5+c5)==56 and S5/2==84 and S5*c5/(a5+c5)==112
D5=(0,0); C5=(4.4,0); A5=(1.0,2.3); B5=(1.0+2.2,2.3); E5=mid(A5,D5); F5=mid(B5,C5)
f=F(); f.fill([A5,B5,F5,E5]); f.poly([A5,B5,C5,D5]); f.line(E5,F5); f.par(A5,B5); f.par(D5,C5); f.tick(A5,E5); f.tick(E5,D5); f.tick(B5,F5); f.tick(F5,C5)
ic=cen([A5,B5,C5,D5]); f.sl('$8$',A5,B5,ic,.28); f.sl('$16$',D5,C5,ic,.28)
f.vl('A',A5,(-1,1),.3); f.vl('B',B5,(1,1),.3); f.vl('C',C5,(1,-1),.3); f.vl('D',D5,(-1,-1),.3); f.vl('E',E5,(-1,0),.3); f.vl('F',F5,(1,0),.3)
f.node((2.2,-.75),'Alan$(ABCD)=168\\ \\mathrm{cm}^2$')
SK5=f.svg()
q('0005',tipId='ge-ym-alan',tip='Yamuğun alanı',z='orta',alt='Orta Tabanla Alan',kaz='Orta taban uzunluğunu bulup yamuğu iki yamuğa ayırarak taralı bölgenin alanını hesaplar.',
 kart='K-GYM-05 (orta taban ve alan) · AB = 8, DC = 16, alan(ABCD) = 168',
 metin='Şekildeki ABCD yamuğunda [AB] // [DC] dir. E ve F noktaları yan kenarların orta noktalarıdır ve şekil ölçekli değildir.\nBuna göre, taralı ABFE yamuğunun alanı kaç cm²’dir?',
 dogru=70,yan=[(56,'Alanın tabanlarla orantılı bölündüğünü sanıp 168 × 8 ÷ 24 = 56 bulmuş.','bilgi'),(84,'Orta tabanın yamuğu iki eşit alana böldüğünü sanmış.','bilgi'),(98,'Alt yamuğun (EFCD) alanını bulmuş.','dikkat'),(112,'Alanı 16 : 8 oranında paylaştırıp alt tabana düşen payı yazmış.','bilgi')],
 istenen='Taralı ABFE yamuğunun alanı (cm²).',
 ip=['Orta tabanın uzunluğu kaçtır ve yükseklik orta tabanla nasıl bölünür? Yükseklik toplam alandan bulunabilir.'],
 bilgi=[ORTAT,OTALAN],
 ad=[A('Orta tabanı bul','Orta taban, üst ve alt tabanın ortalamasıdır.','|EF| = (8 + 16) ÷ 2 = 12'),A('Toplam yüksekliği bul','Yamuk alanı = tabanların ortalaması × yükseklik.','168 = 12 × h → h = 14'),A('Üst yamuğun yüksekliği','Orta taban yüksekliği ikiye böler.','h₁ = 14 ÷ 2 = 7'),A('ABFE’nin alanını hesapla','Tabanlar 8 ve 12, yükseklik 7.','(8 + 12) ÷ 2 × 7 = 70')],
 puf='Orta taban yüksekliği de ikiye böler; iki yamuğun alanı birbirine eşit değildir, tabanlarının toplamıyla orantılıdır.',sekil=SK5)

# ===== 06 · kelebek · zor =====
kartla('K-GYM-06','Yamukta köşegen üçgenleri','Taban oranı köşegen parçalarının oranını verir; verilen yan üçgenden başlayarak ortak köşeli üçgenlerde alan oranıyla diğer üçgenler bulunur.','Yan üçgenleri farklı sanmak; benzerlik oranının karesini ortak yükseklikli üçgenlere uygulamak; yalnız bir üçgeni hesaplamak.','zor',4,'ge-ym-kelebek','Yamukta köşegenlerin oluşturduğu üçgenlerin alanları')
a6,c6,AED=4,6,12; ABE=AED*a6/c6; CDE=AED*c6/a6; BEC=AED; assert (ABE,CDE,ABE+CDE)==(8,18,26)
assert AED==12 and CDE==18 and ABE+AED==20 and AED+BEC==24 and ABE+CDE+AED+BEC==50
s=.8; D6=(0,0); C6=(c6*s,0); A6=(.5,2.6); B6=(.5+a6*s,2.6); E6=lerp(A6,C6,a6/(a6+c6)); assert abs(E6[0]-lerp(B6,D6,a6/(a6+c6))[0])<1e-9
assert abs(alan([A6,B6,E6])/alan([A6,E6,D6])-ABE/AED)<1e-9 and abs(alan([C6,D6,E6])/alan([A6,E6,D6])-CDE/AED)<1e-9
f=F(); f.fill([A6,B6,E6]); f.fill([C6,D6,E6]); f.poly([A6,B6,C6,D6]); f.line(A6,C6); f.line(B6,D6); f.par(A6,B6); f.par(D6,C6)
ic=cen([A6,B6,C6,D6]); f.sl('$4$',A6,B6,ic,.28); f.sl('$6$',D6,C6,ic,.28)
f.node(cen([A6,E6,D6]),'\\footnotesize$12$')
f.vl('A',A6,(-1,1),.3); f.vl('B',B6,(1,1),.3); f.vl('C',C6,(1,-1),.3); f.vl('D',D6,(-1,-1),.3); f.node(add(E6,(.0,.3)),'$E$')
SK6=f.svg()
q('0006',tipId='ge-ym-kelebek',tip='Yamukta köşegenlerin oluşturduğu üçgenlerin alanları',z='zor',alt='Köşegenlerle Oluşan Üçgenler',kaz='Yamukta köşegenlerle oluşan üçgenlerin alanlarını taban oranları üzerinden bulup taralı bölgelerin alan toplamını hesaplar.',
 kart='K-GYM-06 (köşegen üçgenleri) · AB = 4, DC = 6, alan(AED) = 12; taralı ABE + CDE',
 metin='Yamuk biçimli bir tarlada [AB] // [DC] dir. Tarlanın iki köşegen yolu E noktasında kesişir ve tarlayı dört parçaya ayırır. Kenar uzunlukları metre, AED parçasının alanı 12 m² dir. Taralı iki parça ayrı ayrı ekilecektir.\nBuna göre, taralı ABE ve CDE parçalarının alanları toplamı kaç m²’dir?',
 dogru=26,yan=[(12,'Yalnız verilen AED üçgeninin alanını yazmış.','dikkat'),(18,'Yalnız CDE üçgeninin alanını (12 × 3/2) bulup ABE’yi eklememiş.','dikkat'),(20,'ABE ile AED’yi toplamış: 8 + 12; CDE yerine yan üçgeni almış.','dikkat'),(24,'Taralı yerine iki yan üçgenin alanını (12 + 12) toplamış.','dikkat')],
 istenen='Taralı ABE ve CDE üçgenlerinin alanları toplamı (m²).',
 ip=['Taban uzunluklarının oranı, köşegen parçalarının oranını verir. Hangi iki üçgenin tabanları aynı doğru üzerinde ve köşeleri ortaktır?'],
 bilgi=[KEL],
 ad=[A('Köşegen oranını bul','ABE ve CDE benzerdir; oran taban oranıdır.','|BE| : |ED| = |AE| : |EC| = 4 : 6 = 2 : 3'),A('ABE’yi bul','ABE ve AED üçgenlerinin A köşesinden inen yüksekliği ortaktır; tabanları [BE] ve [ED]’dir.','alan(ABE) = 12 × 2 ÷ 3 = 8'),A('CDE’yi bul','AED ve CDE üçgenlerinin D köşesinden inen yüksekliği ortaktır; tabanları [AE] ve [EC]’dir.','alan(CDE) = 12 × 3 ÷ 2 = 18'),A('Toplamı yaz','Taralı iki üçgenin alanı toplanır.','8 + 18 = 26')],
 puf='Yamukta köşegenlerle oluşan üçgenlerde yan üçgenler eşit alanlıdır; üst ve alt üçgenler yan üçgenle taban oranında ilişkilidir.',sekil=SK6)

# ===== 07 · benzerlik: köşegen kesişimi · zor =====
kartla('K-GYM-07','Köşegen kesişiminden geçen paralel','Köşegen kesişim noktasında tabanlara paralel çizilen doğrunun yan kenarlardaki parçası, benzer üçgenlerle bulunur; tamamı iki eş parçanın toplamıdır.','Orta tabanı (aritmetik ortalama) kullanmak; yalnız bir parçayı cevap sanmak; oranı ters kurmak.','zor',4,'ge-ym-benzer','Yamukta benzerlik')
a7,c7=4,12; r7=a7/(a7+c7); EK=c7*r7; EF7=2*EK; assert EK==3 and EF7==6 and (a7+c7)/2==8 and c7*(1-r7)==9 and 2*9==18
s=.4; D7=(0,0); C7=(c7*s,0); A7=(.7,2.4); B7=(.7+a7*s,2.4); K7=lerp(A7,C7,a7/(a7+c7)); E7=lerp(A7,D7,r7); F7=lerp(B7,C7,r7)
assert abs(E7[1]-K7[1])<1e-9 and abs(F7[1]-K7[1])<1e-9 and abs(dist(E7,F7)/s-6)<1e-9 and abs(K7[0]-lerp(B7,D7,a7/(a7+c7))[0])<1e-9
f=F(); f.poly([A7,B7,C7,D7]); f.line(A7,C7); f.line(B7,D7); f.line(E7,F7,'dashed'); f.par(A7,B7); f.par(D7,C7)
ic=cen([A7,B7,C7,D7]); f.sl('$4$',A7,B7,ic,.28); f.sl('$12$',D7,C7,ic,.28)
f.vl('A',A7,(-1,1),.3); f.vl('B',B7,(1,1),.3); f.vl('C',C7,(1,-1),.3); f.vl('D',D7,(-1,-1),.3); f.vl('E',E7,(-1,0),.3); f.vl('F',F7,(1,0),.3); f.node(add(K7,(.0,-.28)),'$K$')
SK7=f.svg()
q('0007',tipId='ge-ym-benzer',tip='Yamukta benzerlik',z='zor',alt='Yamukta Benzerlik',kaz='Yamukta köşegenlerin kesişim noktasından tabanlara paralel çizilen doğru parçasının uzunluğunu benzerlikle bulur.',
 kart='K-GYM-07 (yamukta benzerlik) · AB = 4, DC = 12, EF // DC, K köşegen kesişimi',
 metin='Şekildeki ABCD yamuğunda [AB] // [DC] dir ve köşegenler K noktasında kesişmektedir. K noktasından tabanlara paralel çizilen doğru, [AD] kenarını E’de, [BC] kenarını F’de kesmektedir. Uzunluklar cm cinsindendir. Şekil ölçekli değildir.\nBuna göre, |EF| kaç cm’dir?',
 dogru=6,yan=[(8,'|EF|’yi orta taban sanıp (4 + 12) ÷ 2 = 8 yazmış.','bilgi'),(9,'Oranı ters kurup (3/4) |EK| = 9 bulmuş ve bunu cevap yazmış.','islem'),(12,'Alt tabanın uzunluğunu (|DC| = 12) cevap sanmış.','dikkat'),(18,'Oranı ters kurup |EK| = 9 bulmuş, iki parçayı toplayıp 18 yazmış.','islem')],
 istenen='|EF| uzunluğu (cm).',
 ip=['Şekilde hangi üçgen çiftleri benzerdir? Benzerlik oranını hangi uzunluklardan yazabilirsin?'],
 bilgi=[KEL,PAR],
 ad=[A('Benzerliği kur','ABK ile CDK üçgenleri benzerdir; oran tabanların oranıdır.','|AK| : |KC| = 4 : 12 = 1 : 3 → |AK| : |AC| = 1 : 4'),A('|EK|’yi bul','ADC üçgeninde [EK] // [DC] olduğundan AEK ile ADC benzerdir.','|EK| ÷ 12 = 1 ÷ 4 → |EK| = 3'),A('|KF|’yi bul','Aynı benzerlik B köşesinden bakılınca da geçerlidir: |BK| : |BD| = 1 : 4 olduğundan |KF| de |DC|’nin dörtte biridir.','|KF| = 12 ÷ 4 = 3'),A('|EF|’yi yaz','İki parçayı topla.','|EF| = 3 + 3 = 6')],
 puf='Yamukta köşegenlerin kesişiminden tabanlara çizilen paralelin tamamı 2ac ÷ (a + c) uzunluğundadır; kesişim noktası onu tam ortalar.',sekil=SK7)

# ===== 08 · benzerlik: yan kenar uzantısı · orta =====
kartla('K-GYM-08','Yan kenarların uzantılarıyla benzerlik','Yan kenarlar uzatılınca oluşan büyük ve küçük üçgenler benzerdir; oran tabanlardan kurulur, tüm kenardan parça çıkarılır.','Oranı parça/parça yerine parça/bütün kurmak; ters oran; |EA| ile |ED|’yi karıştırmak.','orta',4,'ge-ym-benzer','Yamukta benzerlik')
AB8,DC8,AD8=6,10,6; EA8=AB8*AD8/(DC8-AB8); ED8=EA8+AD8; assert EA8==9 and ED8==15 and abs(EA8/ED8-AB8/DC8)<1e-9
assert abs(AD8*AB8/DC8-3.6)<1e-9 and DC8-AB8==4 and AD8*DC8/AB8==10
s=.25; D8=(0,0); C8=(DC8*s,0); E8=(3.5*s,sqrt(ED8**2-3.5**2)*s); A8=lerp(E8,D8,EA8/ED8); B8=lerp(E8,C8,EA8/ED8)
assert abs(dist(A8,B8)/s-6)<1e-9 and abs(dist(A8,D8)/s-6)<1e-9 and abs(A8[1]-B8[1])<1e-9
f=F(); f.poly([E8,A8,B8]) ; f.poly([A8,B8,C8,D8]); f.par(A8,B8); f.par(D8,C8)
ic=cen([A8,B8,C8,D8]); f.sl('$6$',A8,B8,ic,.28); f.sl('$10$',D8,C8,ic,.28); f.sl('$6$',A8,D8,cen([A8,B8,C8,D8]),.28)
f.vl('E',E8,(0,1),.3); f.vl('A',A8,(-1,.3),.3); f.vl('B',B8,(1,.3),.3); f.vl('C',C8,(1,-1),.3); f.vl('D',D8,(-1,-1),.3)
SK8=f.svg()
q('0008',tipId='ge-ym-benzer',tip='Yamukta benzerlik',z='orta',alt='Yan Kenar Uzantısı',kaz='Yamuğun yan kenarlarının uzantılarıyla oluşan benzer üçgenlerde orantı kurup istenen uzunluğu bulur.',
 kart='K-GYM-08 (yan kenar uzantısı) · AB = 6, DC = 10, AD = 6',
 metin='Şekilde ABCD yamuğunun [AD] ve [BC] kenarları uzatılmış, uzantılar E noktasında kesişmiştir. [AB] // [DC] dir ve uzunluklar cm cinsindendir. Şekil ölçekli değildir.\nBuna göre, |EA| kaç cm’dir?',
 dogru=9,yan=[(3.6,'|EA| / |AD| = |AB| / |DC| yazmış: |EA| = 6 × 6 ÷ 10 = 3,6 (oran parça/parça kurulmaz).','bilgi'),(4,'Tabanların farkını (10 − 6) |EA| sanmış.','bilgi'),(10,'Oranı ters kurup |EA| = 6 × 10 ÷ 6 = 10 bulmuş.','islem'),(15,'|EA| = 9’u bulup |AD| = 6’yı ekleyerek |ED| = 15’i cevap yazmış.','dikkat')],
 istenen='|EA| uzunluğu (cm).',
 ip=['EAB ve EDC üçgenleri arasında hangi oran vardır?'],
 bilgi=[UZANTI],
 ad=[A('Benzerliği yaz','[AB] // [DC] olduğundan EAB ile EDC üçgenleri benzerdir; oran 6 : 10 = 3 : 5.','|EA| / |ED| = |AB| / |DC| = 3 / 5'),A('|ED|’yi |EA| ile yaz','A noktası [ED] üzerindedir.','|ED| = |EA| + 6'),A('Denklemi çöz','İçler dışlar çarpımı yap.','5 × |EA| = 3 × (|EA| + 6) → 2 × |EA| = 18'),A('Sonucu yaz','|EA| bulunur.','|EA| = 9')],
 puf='Uzantı sorularında oran parça ÷ bütün kurulur: |EA| / |ED| = |AB| / |DC|; ardından |ED| = |EA| + |AD| yazılır.',sekil=SK8)
bitir_geo('yamuk','Yamuk')
