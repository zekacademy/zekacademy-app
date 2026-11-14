"""TYT Geometri PİLOT · 10 şekilli soru (kardeş yok, ipucu 1). Şekil koordinatları hesaplanır, TikZ gövdesi bu değerlerden üretilir (cizim.tikz_svg).
Her cevap ve çeldirici değer koordinat/Python hesabından assert edilir."""
import sys,os,math,json
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
HV=os.path.join(GD,'..')
from math import sin,cos,tan,radians,degrees,atan2,sqrt,pi
P=Parti('geopilot','Geometri','geo|Üçgende Açılar',ders='TYT Geometri',idon='tytgeo')
TIPK={}   # tipId -> uygulama konu anahtarı
def konu(k,ad): P.k=k; P.konu_adi=ad; H.KONU=ad
def kartla(id,alt,fikir,tuzak,z,adim,tipId,tip,kaynak=None):
    kart(id,alt,fikir,tuzak,z,'şekilli',adim,tipId,tip,kaynak or 'ÖSYM 2018–2026 TYT Geometri soruları (yalnız mantık) · MEB 9–10. sınıf geometri'); TIPK[tipId]=P.k
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),kalip='şekilli',**k)

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
IKIZ=B('İkizkenar üçgen','eşit kenarların karşısındaki açılar da eşittir; iç açıların toplamı 180°’dir. Örnek: tepe açısı 40° ise taban açıları (180° − 40°) ÷ 2 = 70°’dir')
DIS=B('Dış açı','üçgenin bir dış açısı, kendisine komşu olmayan iki iç açının toplamına eşittir (ya da 180° − komşu iç açı). Örnek: iç açıları 40° ve 70° olan üçgende üçüncü iç açının dış açısı 110°’dir')
PIS=B('Pisagor bağıntısı','dik üçgende dik kenarların kareleri toplamı hipotenüsün karesine eşittir. Örnek: 3, 4, 5 üçgeni için 3² + 4² = 5²')
OKLID=B('Öklid bağıntısı','dik üçgende hipotenüse indirilen yüksekliğin karesi, hipotenüsü ayırdığı iki parçanın çarpımına eşittir: h² = p × k. Örnek: p = 4, k = 9 ise h² = 36 ve h = 6')
BENZ=B('Temel benzerlik','bir üçgende bir kenara paralel çizilen doğru, diğer iki kenarı orantılı böler: DE // BC ise AD/AB = AE/AC = DE/BC. Örnek: AD/AB = 1/3 ise DE = BC’nin üçte biridir')
ALANORAN=B('Yüksekliği ortak üçgenler','yükseklikleri ortak olan üçgenlerin alanları tabanlarıyla orantılıdır. Örnek: tabanları 2 ve 3 olan, aynı yükseklikli iki üçgenin alanları oranı 2 / 3’tür')
YAMUK=B('Yamukta köşegenler','AB // DC ise köşegenlerin oluşturduğu ABE ve CDE üçgenleri benzerdir; alanlarının oranı benzerlik oranının karesidir. Diğer iki üçgenin (AED ve BEC) alanları birbirine eşittir. Örnek: oran 1/2 ise alan oranı 1/4’tür')
KATLAMA=B('Katlama (simetri)','katlanınca üst üste gelen parçaların uzunlukları ve açıları eşittir; kat izi, birbirine karşılık gelen noktaları birleştiren doğru parçasının orta dikmesidir. Örnek: B köşesi E’ye gelirse |AB| = |AE| ve |FB| = |FE|')
CEMBER=B('Çemberde açılar','çevre açı, gördüğü yayın ölçüsünün yarısıdır ve aynı yayı gören merkez açının yarısına eşittir. Teğet, değme noktasındaki yarıçapa diktir. Örnek: merkez açı 100° ise aynı yayı gören çevre açı 50°’dir')
DAIRE=B('Daire alanı','yarıçapı r olan dairenin alanı π × r²’dir. Teğet iki çemberin merkezleri arası uzaklık yarıçaplar toplamıdır. Örnek: r = 3 için alan 9π')
KOSEGEN=B('Cisim köşegeni','kenar uzunlukları a, b, c olan dikdörtgenler prizmasının cisim köşegeni √(a² + b² + c²) dir. Örnek: 2, 3, 6 kenarlı prizmada köşegen √49 = 7’dir')
YUZEY=B('Prizmanın yüzey alanı','tüm yüzey alanı = 2 × taban alanı + yanal alandır; yanal alan taban çevresi × yüksekliktir. Örnek: kenarı 2 ve yüksekliği 5 olan kare prizmada 2 × 4 + 8 × 5 = 48')
SIL=B('Silindir ve koni hacmi','silindirin hacmi π × r² × h, aynı taban ve yükseklikli koninin hacmi bunun üçte biridir. Koninin ana doğrusu l için l² = r² + h² dir. Örnek: r = 3, h = 4 için koninin ana doğrusu 5’tir')

# =================== 01 · Üçgende Açılar · kolay ===================
konu('geo|Üçgende Açılar','Üçgende Açılar')
kartla('K-GEOP-01','İç ve dış açı, ikizkenar','İkizkenar üçgende taban açıları tepe açısından bulunur; dış açı komşu iç açının bütünleri ya da uzak iki iç açının toplamıdır.','Verilen 50° açısını taban açısı sanmak; dış açı yerine iç açıyı yazmak.','kolay',3,'gep-ucgen-aci','İkizkenar üçgende iç ve dış açı')
Ad=50; Bb=(180-Ad)/2; xx=180-Bb; assert Bb==65 and xx==115 and xx==Ad+Bb
Lh=4.3; hs=radians(Ad/2)
A1=(Lh*sin(hs),Lh*cos(hs)); B1=(0,0); C1=(2*Lh*sin(hs),0); D1=(C1[0]+1.7,0)
assert abs(dist(A1,B1)-dist(A1,C1))<1e-9 and abs(ang(A1,B1,C1)-Ad)<1e-9 and abs(ang(C1,A1,D1)-xx)<1e-9
f=F(); f.poly([A1,B1,C1]); f.line(C1,D1); f.tick(A1,B1); f.tick(A1,C1)
f.arc(A1,B1,C1,.6,'$50^\\circ$',1.35); f.arc(C1,D1,A1,.6,'$x$',.98)
f.vl('A',A1,(0,1),.3); f.vl('B',B1,(-1,-1),.3); f.vl('C',C1,(.2,-1),.3); f.vl('D',D1,(1,-.6),.3)
SK1=f.svg()
q('0001',tipId='gep-ucgen-aci',tip='İkizkenar üçgende iç ve dış açı',z='kolay',alt='İç ve Dış Açı',kaz='İkizkenar üçgende tepe açısından taban açılarını bulup dış açıyı hesaplar.',
 kart='K-GEOP-01 (iç/dış açı) · ikizkenar üçgende dış açı',
 metin='Şekildeki ABC üçgeninde |AB| = |AC| ve m(BAC) = 50° dir. [BC] kenarı, C noktasından D noktasına kadar uzatılmıştır.\nBuna göre, x = m(ACD) kaç derecedir?',
 dogru=115,yan=[(65,'Dış açıyı değil C köşesindeki iç açıyı (taban açısı) bulup bırakmış.','dikkat'),(100,'Dış açı = iki iç açının toplamı kuralında A ile B’yi aynı sanıp 50° + 50° = 100° yazmış.','bilgi'),(130,'50°’yi taban açısı sanıp C’nin iç açısını 50°, dış açıyı 180° − 50° = 130° bulmuş.','bilgi'),(155,'Taban açılarını 50° ÷ 2 = 25° almış, dış açıyı 180° − 25° = 155° bulmuş.','islem')],
 istenen='x = m(ACD) açısının ölçüsü.',
 ip=['Önce ABC üçgeninin iç açılarının neler olduğunu bul; eşit kenarlar hangi açılar hakkında bilgi veriyor?'],
 bilgi=[IKIZ,DIS],
 ad=[A('Taban açılarını bul','|AB| = |AC| olduğundan B ve C açıları eşittir; iç açılar toplamı 180°’dir.','m(B) = m(C) = (180° − 50°) ÷ 2 = 65°'),A('Dış açıya geç','x açısı C köşesindeki iç açıyla doğrusal çifttir.','x = 180° − 65° = 115°'),A('Kontrol et','Dış açı, uzak iki iç açının toplamına eşit olmalıdır.','50° + 65° = 115°')],
 puf='Verilen açı tepe açısıysa taban açıları (180° − tepe) ÷ 2 ile bulunur; dış açı komşu iç açının bütünleridir.',sekil=SK1)

# =================== 02 · Dik Üçgen · orta ===================
konu('geo|Dik Üçgen','Dik Üçgen')
kartla('K-GEOP-02','Hipotenüse inen yükseklik','Hipotenüse indirilen yükseklikle oluşan iki küçük dik üçgende Öklid ve Pisagor birlikte kullanılır; bulunan kenarlarla çevre toplanır.','Yüksekliği çevreye katmak; yalnız küçük üçgenin çevresini almak; hipotenüsü unutmak.','orta',4,'gep-dik-yukseklik','Hipotenüse indirilen yükseklikli dik üçgen')
s=.24; BD,DC=9,16; AD=sqrt(BD*DC); assert AD==12
B2=(0,0); C2=((BD+DC)*s,0); D2=(BD*s,0); A2=(BD*s,AD*s)
AB=dist(A2,B2)/s; AC=dist(A2,C2)/s; BC2=BD+DC
assert abs(AB-15)<1e-9 and abs(AC-20)<1e-9 and abs(ang(A2,B2,C2)-90)<1e-9
cev=AB+AC+BC2; assert cev==60
assert 12==AD and 35==AB+AC and 37==BD+DC+AD and 48==DC+AD+AC and cev+AD==72 and (BD+AD+AB)+(DC+AD+AC)==84 and sorted([12,35,37,48,60])==[12,35,37,48,60]
f=F(); f.poly([A2,B2,C2]); f.line(A2,D2); f.dik(A2,B2,C2); f.dik(D2,A2,C2)
f.vl('A',A2,(0,1),.36); f.vl('B',B2,(-1,-.6),.3); f.vl('C',C2,(1,-.6),.3); f.vl('D',D2,(0,-1),.3)
f.node((BD*s/2,-.3),'$9$'); f.node(((BD+DC/2)*s,-.3),'$16$')
SK2=f.svg()
q('0002',tipId='gep-dik-yukseklik',tip='Hipotenüse indirilen yükseklikli dik üçgen',z='orta',alt='Hipotenüse İnen Yükseklik',kaz='Hipotenüse indirilen yükseklik ve parçalardan dik kenarları bulup üçgenin çevresini hesaplar.',
 kart='K-GEOP-02 (hipotenüse inen yükseklik) · BD = 9, DC = 16 ile çevre',
 metin='Şekildeki ABC üçgeninde m(BAC) = 90°, [AD] ⊥ [BC], |BD| = 9 cm ve |DC| = 16 cm’dir.\nBuna göre, ABC üçgeninin çevresi kaç cm’dir?',
 dogru=60,yan=[(12,'Yalnız |AD| yüksekliğini bulup soruyu orada bırakmış; çevre için kenarlar gerekir.','dikkat'),(35,'|AB| = 15 ve |AC| = 20’yi bulmuş ama |BC| = 25’i çevreye katmamış.','dikkat'),(37,'Çevreyi |BD| + |DC| + |AD| = 9 + 16 + 12 olarak almış; |AD| bir kenar değildir.','bilgi'),(48,'Yalnız ADC üçgeninin çevresini hesaplamış: 16 + 12 + 20 = 48.','dikkat')],
 istenen='ABC üçgeninin çevresi (cm).',
 ip=['|AD| ile |BD|, |DC| arasında bir bağıntı ara; sonra bulduğun uzunluklarla dik kenarları hesapla.'],
 bilgi=[OKLID,PIS],
 ad=[A('Yüksekliği bul','Hipotenüse indirilen yükseklik için Öklid bağıntısını yaz.','|AD|² = 9 × 16 = 144 → |AD| = 12'),A('|AB| kenarını bul','ABD dik üçgeninde Pisagor uygula.','|AB|² = 9² + 12² = 225 → |AB| = 15'),A('|AC| kenarını bul','ADC dik üçgeninde Pisagor uygula.','|AC|² = 16² + 12² = 400 → |AC| = 20'),A('Çevreyi topla','|BC| = 9 + 16 = 25 cm.','15 + 20 + 25 = 60')],
 puf='Hipotenüse inen yükseklikte önce h² = p × k ile yüksekliği bul, sonra Pisagor ile dik kenarlara geç.',sekil=SK2)

# =================== 03 · Üçgende Benzerlik · orta ===================
konu('geo|Üçgende Benzerlik','Üçgende Benzerlik')
kartla('K-GEOP-03','Paralel doğruyla benzerlik','Kenara paralel doğru oranı AD/AB = AE/AC = DE/BC verir; hangi parçanın hangi bütüne oranlandığına dikkat edilip iki uzunluk bulunur.','AD/DB ile AD/AB oranını karıştırmak; EC yerine AC ya da AE almak.','orta',4,'gep-benzer-paralel','Kenara paralel doğruyla temel benzerlik')
AD3,DB3,AE3,BC3=6,4,9,20; AB3=AD3+DB3; AC3=AE3*AB3/AD3; assert AC3==15
DE3=BC3*AD3/AB3; EC3=AC3-AE3; assert DE3==12 and EC3==6 and DE3+EC3==18
sol=18
assert BC3*AD3/DB3+EC3==36 and DE3+AE3*AB3/AD3==27 and AE3+DE3==21 and DE3==12
# koordinat
x=(AB3**2-AC3**2+BC3**2)/(2*BC3); y=sqrt(AB3**2-x**2); s=.3
B3=(0,0); C3=(BC3*s,0); A3=(x*s,y*s); D3=lerp(A3,B3,AD3/AB3); E3=lerp(A3,C3,AE3/AC3)
assert abs(dist(A3,B3)/s-AB3)<1e-9 and abs(dist(A3,C3)/s-AC3)<1e-9 and abs(dist(D3,E3)/s-DE3)<1e-9
assert abs((E3[1]-D3[1]))<1e-9
f=F(); f.poly([A3,B3,C3]); f.line(D3,E3); f.par(D3,E3); f.par(B3,C3)
ic=cen([A3,B3,C3])
f.sl('$6$',A3,D3,ic,.28); f.sl('$4$',D3,B3,ic,.28); f.sl('$9$',A3,E3,ic,.28); f.sl('$20$',B3,C3,ic,.28)
f.vl('A',A3,(0,1),.3); f.vl('B',B3,(-1,-.6),.3); f.vl('C',C3,(1,-.6),.3); f.vl('D',D3,(-1,.55),.3); f.vl('E',E3,(1,.55),.3)
SK3=f.svg()
q('0003',tipId='gep-benzer-paralel',tip='Kenara paralel doğruyla temel benzerlik',z='orta',alt='Paralel Doğruyla Benzerlik',kaz='Kenara paralel doğrunun oluşturduğu benzer üçgenlerde orantı kurarak iki uzunluğu bulur.',
 kart='K-GEOP-03 (paralel doğruyla benzerlik) · AD = 6, DB = 4, AE = 9, BC = 20',
 metin='Şekildeki ABC üçgeninde D ∈ [AB], E ∈ [AC], [DE] // [BC], |AD| = 6 cm, |DB| = 4 cm, |AE| = 9 cm ve |BC| = 20 cm’dir.\nBuna göre, |DE| + |EC| toplamı kaç cm’dir?',
 dogru=18,yan=[(12,'Yalnız |DE| uzunluğunu bulup |EC|’yi eklemeyi unutmuş.','dikkat'),(21,'|EC| yerine |AE| = 9’u alıp 12 + 9 = 21 yazmış.','dikkat'),(27,'|AE| / |EC| = |AD| / |AB| yazıp |EC| = 9 × 10 ÷ 6 = 15 bulmuş (|AC| bulunur, |EC| değil); 12 + 15 = 27.','islem'),(36,'|DE| = 20 × 6 ÷ 4 = 30 bulmuş (|AD| / |DB| oranını kullanmış); |EC| = 6 ile 36.','bilgi')],
 istenen='|DE| + |EC| toplamı (cm).',
 ip=['Paralel doğru hangi benzer üçgenleri oluşturdu? Orantıyı kurarken pay ve paydadaki kenarların aynı üçgenden gelmesine dikkat et.'],
 bilgi=[BENZ],
 ad=[A('Benzerliği kur','[DE] // [BC] olduğundan ADE ve ABC üçgenleri benzerdir.','|AB| = 6 + 4 = 10 · |AD| / |AB| = |AE| / |AC| = |DE| / |BC|'),A('|DE| uzunluğunu bul','Benzerlik oranı 6/10’dur; |BC| = 20 ile çarp.','|DE| = 20 × 6 ÷ 10 = 12'),A('|AC| ve |EC| uzunluğunu bul','9 / |AC| = 6 / 10 oranından |AC| bulunur, |AE| çıkarılır.','|AC| = 15 → |EC| = 15 − 9 = 6'),A('Toplamı yaz','İstenen toplam.','12 + 6 = 18')],
 puf='Paralel doğru çizilince oranlar parça ÷ bütün olarak kurulur: AD/AB ve AE/AC.',sekil=SK3)

# =================== 04 · Üçgende Alan · orta ===================
konu('geo|Üçgende Alan','Üçgende Alan')
kartla('K-GEOP-04','Ortak yükseklikle alan oranı','Aynı köşeden çizilen tabanlar üzerinde alanlar tabanlarla orantılıdır; iki ardışık oranla büyük alandan istenen üçgene inilir.','Oranları ters yazmak; yalnız bir oranı uygulamak; taralı alan yerine komşu üçgenin alanını vermek.','orta',3,'gep-alan-oran','Ortak yükseklikle alan oranı')
T4=60; BD4,DC4=3,2; AE4,ED4=1,2
ADC4=T4*DC4/(BD4+DC4); CDE4=ADC4*ED4/(AE4+ED4); assert ADC4==24 and CDE4==16
assert T4/3==20 and ADC4==24 and T4*BD4/5==36 and T4*2/3==40
B4=(0,0); C4=(6,0); A4=(1.6,3.6); D4=lerp(B4,C4,BD4/5); E4=lerp(A4,D4,AE4/3)
assert abs(alan([C4,D4,E4])/alan([A4,B4,C4])-CDE4/T4)<1e-9
f=F(); f.fill([C4,D4,E4]); f.poly([A4,B4,C4]); f.line(A4,D4); f.line(E4,C4)
ic=cen([A4,B4,C4])
f.sl('$3a$',B4,D4,ic,.28); f.sl('$2a$',D4,C4,ic,.28)
mAE=mid(A4,E4); mED=mid(E4,D4); nn=un((-(D4[1]-A4[1]),D4[0]-A4[0]))  # AD'ye dik (sağa doğru)
if nn[0]<0: nn=(-nn[0],-nn[1])
f.node(sub(mAE,mul(nn,.25)),'$b$'); f.node(sub(mED,mul(nn,.3)),'$2b$')
f.vl('A',A4,(0,1),.3); f.vl('B',B4,(-1,-.6),.3); f.vl('C',C4,(1,-.6),.3); f.vl('D',D4,(.0,-1),.3); f.vl('E',E4,(-1,.2),.3)
f.node((3,-1.05),'Alan$(ABC)=60\\ \\mathrm{cm}^2$')
SK4=f.svg()
q('0004',tipId='gep-alan-oran',tip='Ortak yükseklikle alan oranı',z='orta',alt='Alan Oranları',kaz='Yükseklikleri ortak üçgenlerde alan oranını taban oranına eşitleyerek taralı üçgenin alanını bulur.',
 kart='K-GEOP-04 (alan oranı) · BD:DC = 3:2, AE:ED = 1:2, alan(ABC) = 60',
 metin='Şekilde ABC üçgeninin alanı 60 cm², D ∈ [BC], E ∈ [AD], |BD| : |DC| = 3 : 2 ve |AE| : |ED| = 1 : 2 dir.\nBuna göre, taralı CDE üçgeninin alanı kaç cm²’dir?',
 dogru=16,yan=[(20,'Yalnız E noktasının oranını uygulamış: 60 × (1/3) = 20 (D’nin oranını atlamış).','dikkat'),(24,'ADC üçgeninin alanını (24) bulup E noktasının oranını uygulamayı unutmuş.','dikkat'),(36,'|BD| / |BC| = 3/5 oranını almış (ABD üçgeni): 60 × 3 ÷ 5 = 36.','dikkat'),(40,'Yalnız |ED| / |AD| = 2/3 oranını uygulamış: 60 × 2 ÷ 3 = 40 (D oranını atlamış).','dikkat')],
 istenen='Taralı CDE üçgeninin alanı (cm²).',
 ip=['Alanı verilen ABC’den CDE’ye hangi ara üçgenle gidebilirsin? Ortak köşe ve aynı doğru üzerindeki tabanlara bak.'],
 bilgi=[ALANORAN],
 ad=[A('ADC üçgenini bul','A köşesinden BC’ye inen yükseklik ortaktır; alanlar tabanlarla orantılıdır.','Alan(ADC) = 60 × 2/5 = 24'),A('CDE üçgenine in','C köşesinden AD’ye inen yükseklik ortaktır; ACD ve CDE üçgenlerinin tabanları |AD| ve |ED|’dir.','|ED| / |AD| = 2/3'),A('Hesapla','ADC’nin alanının 2/3’ü alınır.','24 × 2/3 = 16')],
 puf='Alan sorularında önce ortak yüksekliği olan üçgen çiftlerini bul; her adımda bir taban oranı uygula.',sekil=SK4)

# =================== 05 · Yamuk · orta ===================
konu('geo|Yamuk','Yamuk')
kartla('K-GEOP-05','Yamukta köşegenlerle alan','Köşegenler iki benzer üçgen ve eş alanlı iki yan üçgen oluşturur; benzerlik oranının karesi alan oranını verir.','Alan oranı yerine uzunluk oranını kullanmak; yan üçgenleri ABE ya da CDE’ye eşit sanmak; bir yan üçgeni saymamak.','orta',4,'gep-yamuk-kosegen','Yamukta köşegenlerin oluşturduğu üçgenlerin alanları')
AB5,DC5=6,10; ABE5=9; CDE5=ABE5*DC5**2/AB5**2; assert abs(CDE5-25)<1e-9
yan5=sqrt(ABE5*CDE5); assert abs(yan5-15)<1e-9; tum5=ABE5+CDE5+2*yan5; assert abs(tum5-64)<1e-9
assert ABE5+CDE5==34 and ABE5+CDE5+yan5==49 and ABE5+CDE5+2*ABE5==52 and ABE5+3*CDE5==84
s=.5; D5=(0,0); C5=(DC5*s,0); h5=8*s; A5=(1.5*s,h5); B5=(1.5*s+AB5*s,h5)
E5=lerp(A5,C5,AB5/(AB5+DC5)); assert abs(E5[0]-lerp(B5,D5,AB5/(AB5+DC5))[0])<1e-9
alanyamuk=alan([A5,B5,C5,D5])/s**2; assert abs(alanyamuk-tum5)<1e-9 and abs(alan([A5,B5,E5])/s**2-9)<1e-9
f=F(); f.fill([A5,B5,E5]); f.poly([A5,B5,C5,D5]); f.line(A5,C5); f.line(B5,D5); f.par(A5,B5); f.par(D5,C5)
ic=cen([A5,B5,C5,D5])
f.sl('$6$',A5,B5,ic,.28); f.sl('$10$',D5,C5,ic,.28)
f.vl('A',A5,(-1,.7),.3); f.vl('B',B5,(1,.7),.3); f.vl('C',C5,(1,-.7),.3); f.vl('D',D5,(-1,-.7),.3)
f.node(add(cen([A5,B5,E5]),(0,.1)),'\\footnotesize$9\\ \\mathrm{cm}^2$')
SK5=f.svg()
q('0005',tipId='gep-yamuk-kosegen',tip='Yamukta köşegenlerin oluşturduğu üçgenlerin alanları',z='orta',alt='Yamukta Alan',kaz='Yamukta köşegenlerin oluşturduğu benzer üçgenlerin alan oranından yamuğun alanını bulur.',
 kart='K-GEOP-05 (yamuk, köşegenler) · AB = 6, DC = 10, alan(ABE) = 9',
 metin='Şekildeki ABCD yamuğunda [AB] // [DC], |AB| = 6 cm ve |DC| = 10 cm’dir. Köşegenler E noktasında kesişmektedir. Taralı ABE üçgeninin alanı 9 cm² dir.\nBuna göre, ABCD yamuğunun alanı kaç cm²’dir?',
 dogru=64,yan=[(34,'Yalnız ABE ve CDE üçgenlerinin alanlarını toplamış: 9 + 25 = 34; yan üçgenleri saymamış.','dikkat'),(49,'9 + 25 + 15 yazmış; iki yan üçgenden yalnız birini saymış.','dikkat'),(52,'Yan üçgenleri ABE’ye eşit alıp 9 + 25 + 9 + 9 = 52 bulmuş.','bilgi'),(84,'Yan üçgenleri CDE’ye eşit alıp 9 + 25 + 25 + 25 = 84 bulmuş.','bilgi')],
 istenen='ABCD yamuğunun alanı (cm²).',
 ip=['[AB] // [DC] olduğundan köşegenlerin oluşturduğu hangi iki üçgen benzerdir? Diğer iki üçgenin alanlarını nasıl bulursun?'],
 bilgi=[YAMUK],
 ad=[A('Benzer üçgenleri bul','AB // DC olduğundan ABE ile CDE üçgenleri benzerdir.','benzerlik oranı = 6 / 10 = 3 / 5'),A('CDE’nin alanını bul','Alanlar oranı, benzerlik oranının karesidir.','Alan(CDE) = 9 × (5/3)² = 25'),A('Yan üçgenleri bul','AED ve BEC üçgenleri eş alanlıdır; her biri, alanları çarpımının kareköküdür.','√(9 × 25) = 15'),A('Toplamı yaz','Dört üçgenin alanını topla.','9 + 25 + 15 + 15 = 64')],
 puf='Yamukta köşegenlerle oluşan dört üçgenin alanları a, b ve iki tane √(a × b) biçimindedir; toplamı (√a + √b)² dir.',sekil=SK5)

# =================== 06 · Dikdörtgen · zor ===================
konu('geo|Dikdörtgen','Dikdörtgen')
kartla('K-GEOP-06','Katlama','Katlanan köşe E’ye gelince |AE| = |AB| ve |FE| = |FB| olur; DE ve EC Pisagorla bulunur, ECF dik üçgeninde Pisagor yeniden uygulanır.','Katlanan uzunlukların eşitliğini görememek; BF ile FC’yi karıştırmak; DE yerine EC’yi vermek.','zor',5,'gep-katlama','Dikdörtgen kâğıdı köşeden katlama')
AB6,BC6=10,8; AE6=AB6; DE6=sqrt(AE6**2-BC6**2); EC6=AB6-DE6; assert DE6==6 and EC6==4
# FB=x: x^2 = EC^2 + (BC-x)^2
x6=(EC6**2+BC6**2)/(2*BC6); FC6=BC6-x6; assert x6==5 and FC6==3
assert abs(FC6-EC6*DE6/BC6)<1e-9      # ADE ~ ECF ile ikinci yol
assert (EC6,x6,DE6,BC6-DE6)==(4,5,6,2)
s=.6; A6=(0,0); B6=(AB6*s,0); C6=(AB6*s,BC6*s); D6=(0,BC6*s); E6=(DE6*s,BC6*s); F6=(AB6*s,x6*s)
assert abs(dist(A6,E6)/s-10)<1e-9 and abs(dist(E6,F6)-dist(B6,F6))<1e-9
f=F(); f.fill([A6,E6,F6]); f.poly([A6,B6,C6,D6]); f.line(A6,F6,'very thick'); f.line(A6,E6,'dashed'); f.line(E6,F6,'dashed')
ic=cen([A6,B6,C6,D6])
f.sl('$10$',A6,B6,ic,.28)
f.raw(f'\\draw[<->,thin] ({B6[0]+.75:.3f},{B6[1]:.3f}) -- ({C6[0]+.75:.3f},{C6[1]:.3f});'); f.node((B6[0]+1.05,mid(B6,C6)[1]),'$8$')
f.vl('A',A6,(-1,-1),.3); f.vl('B',B6,(1,-1),.3); f.vl('C',C6,(1,1),.3); f.vl('D',D6,(-1,1),.3); f.vl('E',E6,(0,1),.3); f.vl('F',F6,(1,.0),.3)
SK6=f.svg()
q('0006',tipId='gep-katlama',tip='Dikdörtgen kâğıdı köşeden katlama',z='zor',alt='Katlama Problemleri',kaz='Katlamada eşit kalan uzunlukları belirleyip Pisagor bağıntısıyla kenar uzunluğunu bulur.',
 kart='K-GEOP-06 (katlama) · AB = 10, BC = 8, B köşesi DC üzerine',
 metin='Şekildeki ABCD dikdörtgeni biçimindeki kâğıtta |AB| = 10 cm ve |BC| = 8 cm’dir. Bu kâğıt, B köşesi [DC] kenarı üzerindeki E noktasına gelecek biçimde [AF] boyunca katlanıyor (F ∈ [BC]). Katlanmış B köşesinin yeri şekilde E olarak gösterilmiştir.\nBuna göre, |FC| kaç cm’dir?',
 dogru=3,yan=[(2,'|FC| = |BC| − |DE| = 8 − 6 = 2 yazmış; |DE| ile |FC| arasında böyle bir ilişki yoktur.','bilgi'),(4,'|EC| = 4’ü bulup bunu |FC| sanmış.','dikkat'),(5,'|BF| = |FE| = 5’i bulup |FC| = |BC| − |BF| işlemini yapmamış.','dikkat'),(6,'|DE| = 6’yı bulup cevap olarak yazmış; |DE|, |FC|’den farklı bir uzunluktur.','dikkat')],
 istenen='|FC| uzunluğu (cm).',
 ip=['|AB| kenarının katlandıktan sonra hangi doğru parçasına dönüştüğünü bul; bu parça hangi dik üçgenin kenarı oluyor?'],
 bilgi=[KATLAMA,PIS],
 ad=[A('Katlamadan eşitleri yaz','B köşesi E’ye geldiğinden |AE| = |AB| ve |FE| = |FB| olur.','|AE| = 10'),A('DE ve EC’yi bul','ADE dik üçgeninde Pisagor uygula; |DC| = 10’dan |DE| çıkar.','|DE|² = 10² − 8² = 36 → |DE| = 6 · |EC| = 4'),A('FC’yi bilinmeyenle yaz','|BF| = x alınırsa |FE| = x ve |FC| = 8 − x olur.','ECF dik üçgeni: kenarlar 4, 8 − x, x'),A('Pisagor uygula','ECF üçgeninde hipotenüs |FE| = x’tir.','x² = 4² + (8 − x)² → 16x = 80 → x = 5'),A('FC’yi hesapla','|FC| = |BC| − |BF|.','8 − 5 = 3')],
 puf='Katlama sorularında önce eşit kalan uzunlukları yaz; sonra oluşan dik üçgende Pisagor’u bilinmeyenle kur.',sekil=SK6)

# =================== 07 · Çemberde Açı · orta ===================
konu('geo|Çemberde Açı','Çemberde Açı')
kartla('K-GEOP-07','Teğetler ve çevre açı','İki teğetin yaptığı açıdan merkez açı (360° − 90° − 90° − P) bulunur, çevre açı bunun yarısıdır.','Merkez açıyı çevre açı sanmak; çevre açıyı küçük yaydan görmek; P açısını doğrudan yazmak.','orta',3,'gep-cember-teget','İki teğet ve çevre açı')
P7=50; AOB7=180-P7; C7a=AOB7/2; assert AOB7==130 and C7a==65 and 180-C7a==115 and P7/2==25
r7=1.8; d7=r7/sin(radians(P7/2)); th=degrees(math.acos(r7/d7)); assert abs(th-(90-P7/2))<1e-9
O7=(0,0); Pp=(d7,0); A7=(r7*cos(radians(th)),r7*sin(radians(th))); B7=(A7[0],-A7[1]); C7=(r7*cos(radians(200)),r7*sin(radians(200)))
assert abs(ang(Pp,A7,B7)-50)<1e-9 and abs(ang(O7,A7,B7)-130)<1e-9 and abs(ang(C7,A7,B7)-65)<1e-9
assert abs((A7[0]-Pp[0])*A7[0]+(A7[1]-Pp[1])*A7[1])<1e-9      # PA ⟂ OA
f=F(); f.raw(f'\\draw (0,0) circle ({r7});'); f.line(Pp,A7); f.line(Pp,B7); f.line(O7,A7); f.line(O7,B7); f.line(C7,A7); f.line(C7,B7)
f.raw('\\fill (0,0) circle (1pt);')
f.arc(Pp,A7,B7,.9,'$50^\\circ$',1.55); f.arc(C7,A7,B7,.55,'$x$',.9)
f.vl('A',A7,sub(A7,O7),.3); f.vl('B',B7,sub(B7,O7),.3); f.vl('P',Pp,(1,0),.3); f.vl('C',C7,sub(C7,O7),.3); f.node((-.25,-.22),'$O$')
SK7=f.svg()
q('0007',tipId='gep-cember-teget',tip='İki teğet ve çevre açı',z='orta',alt='Teğet ve Çevre Açı',kaz='Teğetlerin yaptığı açıdan merkez açıyı, ondan da çevre açıyı bulur.',
 kart='K-GEOP-07 (çemberde açı) · m(APB) = 50°, C büyük yayda',
 metin='Şekilde O merkezli çembere A ve B noktalarında teğet olan [PA] ve [PB] doğru parçaları verilmiştir. C noktası, [AB] kirişinin P noktasının bulunmadığı tarafında çember üzerindedir ve m(APB) = 50° dir.\nBuna göre, x = m(ACB) kaç derecedir?',
 dogru=65,yan=[(25,'Çevre açıyı P açısının yarısı sanmış: 50° ÷ 2 = 25°.','bilgi'),(50,'x açısını P açısına eşit sanmış.','bilgi'),(115,'Merkez açıyı (130°) bulmuş, ama C’yi küçük yay üzerinde sanıp 180° − 65° = 115° yazmış.','dikkat'),(130,'m(AOB) = 130° merkez açısını bulup bırakmış; x çevre açıdır, yarısıdır.','dikkat')],
 istenen='x = m(ACB) çevre açısının ölçüsü.',
 ip=['O’yu A ve B’ye birleştiren yarıçapların teğetlerle yaptığı açılara bak; hangi dörtgen oluşuyor?'],
 bilgi=[CEMBER],
 ad=[A('Dik açıları yaz','Teğet, değme noktasındaki yarıçapa diktir: OA ⊥ PA ve OB ⊥ PB.','m(OAP) = m(OBP) = 90°'),A('Merkez açıyı bul','OAPB dörtgeninin iç açıları toplamı 360°’dir.','m(AOB) = 360° − 90° − 90° − 50° = 130°'),A('Çevre açıyı bul','C büyük yayda olduğundan, AB yayını gören çevre açı merkez açının yarısıdır.','x = 130° ÷ 2 = 65°')],
 puf='İki teğet sorusunda önce merkez açıyı (180° − teğetler arası açı) bul; çevre açı bunun yarısıdır (C büyük yayda ise).',sekil=SK7)

# =================== 08 · Dairede Çevre ve Alan · kolay ===================
konu('geo|Dairede Çevre ve Alan','Dairede Çevre ve Alan')
kartla('K-GEOP-08','Teğet çemberler ve taralı alan','Eş teğet çemberlerin yarıçapı kenar uzunluğundan bulunur; taralı alan dikdörtgenden dairelerin alanları çıkarılarak π cinsinden yazılır.','Daire alanı yerine çevre formülü; daire sayısını yanlış almak; yarıçapı yanlış bölmek.','kolay',4,'gep-daire-taralı','Teğet daireler ve taralı alan')
AB8=24; r8=AB8/6; BC8=2*r8; assert r8==4 and BC8==8
dik8=AB8*BC8; tar_c=dik8-3*r8**2   # katsayı: 3*16=48
assert dik8==192 and 3*r8**2==48 and 2*r8**2==32 and 3*2*r8*1==24 and r8**2==16 and 3*(AB8/12)**2==12
s=.25; f=F()
f.raw(f'\\path[fill=vurgu!25,even odd rule] (0,0) rectangle ({AB8*s},{BC8*s}) '+' '.join(f'({(2*i+1)*r8*s},{r8*s}) circle ({r8*s})' for i in range(3))+';')
f.raw(f'\\draw (0,0) rectangle ({AB8*s},{BC8*s});')
for i in range(3): f.raw(f'\\draw ({(2*i+1)*r8*s},{r8*s}) circle ({r8*s});')
A8=(0,0);B8=(AB8*s,0);C8=(AB8*s,BC8*s);D8=(0,BC8*s)
f.sl('$24$',A8,B8,(3,1),.3)
f.vl('A',A8,(-1,-1),.3); f.vl('B',B8,(1,-1),.3); f.vl('C',C8,(1,1),.3); f.vl('D',D8,(-1,1),.3)
SK8=f.svg()
S8=['192 − 48π','192 − 32π','192 − 24π','192 − 16π','192 − 12π']
q('0008',tipId='gep-daire-taralı',tip='Teğet daireler ve taralı alan',z='kolay',alt='Taralı Alan',kaz='Teğet eş dairelerin yarıçapını bulup taralı bölgenin alanını π cinsinden hesaplar.',
 kart='K-GEOP-08 (daire alanı) · dikdörtgen içinde üç eş daire, AB = 24',
 metin='Şekilde ABCD dikdörtgeninin içinde üç eş çember bulunmaktadır. Çemberler birbirine ve dikdörtgenin kenarlarına şekildeki gibi teğettir. |AB| = 24 cm dir.\nBuna göre, taralı bölgenin alanı kaç cm²’dir?',
 dogru='192 − 48π',sira=['192 − 48π','192 − 32π','192 − 24π','192 − 16π','192 − 12π'],
 yan=[('192 − 32π','Çember sayısını iki sanıp 2 × 16π = 32π çıkarmış.','dikkat'),('192 − 24π','Daire alanı yerine çevre formülünü (2πr = 8π) kullanıp 3 × 8π = 24π çıkarmış.','bilgi'),('192 − 16π','Yalnız bir dairenin alanını (16π) çıkarmış.','dikkat'),('192 − 12π','|AB| = 24’ü 12 parçaya bölüp yarıçapı 2 almış: 3 × 4π = 12π.','islem')],
 istenen='Taralı bölgenin alanı (cm²).',
 ip=['|AB| uzunluğu, üç çemberin yan yana dizilişinde kaç yarıçapa karşılık geliyor? Dikdörtgenin diğer kenarını da şekilden bul.'],
 bilgi=[DAIRE],
 ad=[A('Yarıçapı bul','Üç çember yan yana teğet olduğundan |AB| altı yarıçap uzunluğundadır.','6r = 24 → r = 4'),A('Dikdörtgenin alanını bul','Çemberler üst ve alt kenara teğet olduğundan |BC| = 2r = 8 cm.','24 × 8 = 192'),A('Dairelerin alanı','Üç dairenin alanı toplamı.','3 × π × 4² = 48π'),A('Farkı al','Taralı alan, dikdörtgen eksi daireler.','192 − 48π')],
 puf='Teğet çemberlerde uzunluk, yarıçapların katı olarak yazılır; taralı alan = bütün alan − çıkarılan alan.',sekil=SK8)

# =================== 09 · Katı Cisimler · zor ===================
konu('geo|Katı Cisimler','Katı Cisimler')
kartla('K-GEOP-09','Cisim köşegeni ve yüzey alanı','Cisim köşegeninden yükseklik √(d² − 2a²) ile bulunur; tüm yüzey alanı iki taban + dört yan yüzdür.','Yanal alanı ya da yalnız bir tabanı saymak; hacimle karıştırmak; yan yüzleri iki tane saymak.','zor',4,'gep-prizma-yuzey','Kare dik prizmada cisim köşegeni ve yüzey alanı')
a9=6; d9=11; h9=sqrt(d9**2-2*a9**2); assert h9==7
SA9=2*a9**2+4*a9*h9; assert SA9==240 and a9**2*h9==252 and 4*a9*h9==168 and a9**2+4*a9*h9==204 and 2*a9**2+2*a9*h9==156
AZ,EL=-35,22
def proj(p,k=.5,al=radians(40)): return (p[0]+k*p[1]*cos(al),p[2]+k*p[1]*sin(al))   # kabine (eğik) izdüşüm: ön yüz gerçek oranda
def gorunen(c): return c
sc=.4
V9={'A':(0,0,0),'B':(a9,0,0),'C':(a9,a9,0),'D':(0,a9,0),'E':(0,0,h9),'F':(a9,0,h9),'G':(a9,a9,h9),'H':(0,a9,h9)}
cam=(0.3,-1,0.6)   # ön (y=0), sağ (x=a) ve üst yüz görünür
YUZ={'taban':('ABCD',(0,0,-1)),'ust':('EFGH',(0,0,1)),'on':('ABFE',(0,-1,0)),'arka':('DCGH',(0,1,0)),'sol':('ADHE',(-1,0,0)),'sag':('BCGF',(1,0,0))}
gor={k:sum(n[i]*cam[i] for i in range(3))>0 for k,(v,n) in YUZ.items()}
assert gor=={'taban':False,'ust':True,'on':True,'arka':False,'sol':False,'sag':True}
KEN=['AB','BC','CD','DA','EF','FG','GH','HE','AE','BF','CG','DH']
def gizli(e): return not any(gor[k] for k,(v,n) in YUZ.items() if e[0] in v and e[1] in v)
assert sorted(e for e in KEN if gizli(e))==['CD','DA','DH']
Q9={k:mul(proj(v),sc) for k,v in V9.items()}
f=F()
for e in KEN: f.line(Q9[e[0]],Q9[e[1]],'dashed' if gizli(e) else '')
f.line(Q9['A'],Q9['G'],'dashed')
ic=cen(list(Q9.values()))
f.vl('A',Q9['A'],(-1,-.5),.3); f.vl('B',Q9['B'],(.5,-1),.3); f.vl('C',Q9['C'],(1,-.4),.3); f.vl('D',Q9['D'],(-.2,-1),.3)
f.vl('E',Q9['E'],(-1,.5),.3); f.vl('F',Q9['F'],(.3,1),.3); f.vl('G',Q9['G'],(1,.5),.3); f.vl('H',Q9['H'],(-.2,1),.3)
f.sl('$6$',Q9['A'],Q9['B'],ic,.28)
mA=lerp(Q9['A'],Q9['G'],.5); eA=un(sub(Q9['G'],Q9['A'])); nA=(-eA[1],eA[0])
f.node(add(mA,mul(nA,.28)),'$11$')
SK9=f.svg()
q('0009',tipId='gep-prizma-yuzey',tip='Kare dik prizmada cisim köşegeni ve yüzey alanı',z='zor',alt='Cisim Köşegeni',kaz='Cisim köşegeninden prizmanın yüksekliğini bulup tüm yüzey alanını hesaplar.',
 kart='K-GEOP-09 (prizma) · taban kenarı 6, cisim köşegeni 11',
 metin='Şekildeki ABCDEFGH kare dik prizmasının taban kenarı |AB| = 6 cm ve cisim köşegeni |AG| = 11 cm dir. Görünmeyen kenarlar kesikli çizgiyle gösterilmiştir.\nBuna göre, bu prizmanın tüm yüzey alanı kaç cm²’dir?',
 dogru=240,yan=[(156,'Yan yüzeyleri iki tane saymış: 2 × 36 + 2 × 6 × 7 = 156 (yan yüz dört tanedir).','dikkat'),(168,'Yalnız yanal alanı (4 × 6 × 7) bulup tabanları eklememiş.','dikkat'),(204,'Tabanlardan yalnız birini saymış: 36 + 168 = 204.','dikkat'),(252,'Yüzey alanı yerine hacmi (36 × 7) hesaplamış.','bilgi')],
 istenen='Prizmanın tüm yüzey alanı (cm²).',
 ip=['Yüzey alanı için hangi uzunluk eksik? Cisim köşegeni, tabanın köşegeni ve yükseklikle hangi dik üçgeni oluşturuyor?'],
 bilgi=[KOSEGEN,YUZEY,PIS],
 ad=[A('Taban köşegenini bul','Tabanı kare olan prizmada taban köşegeni kenarın √2 katıdır.','|AC|² = 6² + 6² = 72'),A('Yüksekliği bul','AC, CG ve AG bir dik üçgen oluşturur (AG hipotenüs).','|CG|² = 11² − 72 = 49 → h = 7'),A('Yanal alanı bul','Dört yan yüz 6 × 7 dikdörtgenidir.','4 × 6 × 7 = 168'),A('Tabanları ekle','İki taban kare, her biri 6 × 6.','2 × 36 + 168 = 240')],
 puf='Cisim köşegeni d² = a² + b² + h² ile yüksekliği verir; tüm yüzey alanı = iki taban + yanal alandır.',sekil=SK9)

# =================== 10 · Silindir · zor ===================
konu('geo|Silindir','Silindir')
kartla('K-GEOP-10','Silindir içinde koni','Ana doğrudan koninin yüksekliği Pisagorla bulunur; silindir ve koni hacimleri farkı π cinsinden yazılır.','Yüksekliği yerine ana doğruyu kullanmak; koni hacmindeki 1/3 katsayısını unutmak; yalnız koni ya da silindiri hesaplamak.','zor',4,'gep-silindir-koni','Silindir içine yerleştirilmiş koni')
r10=3; l10=5; h10=sqrt(l10**2-r10**2); assert h10==4
Vc=pi*r10**2*h10; Vk=Vc/3; assert abs((Vc-Vk)/pi-24)<1e-9
cl=lambda v,w: abs(v/pi-w)<1e-9
assert cl(Vk,12) and cl(Vc-pi*r10**2*l10/3,21) and cl(pi*r10**2*l10-pi*r10**2*l10/3,30) and cl(Vc,36)
sc=.7; el=radians(22); R=r10*sc; ry=R*sin(el); Hs=h10*sc*cos(el)
f=F()
f.raw(f'\\draw (0,{Hs:.3f}) ellipse [x radius={R:.3f},y radius={ry:.3f}];')
f.line((-R,0),(-R,Hs)); f.line((R,0),(R,Hs))
f.raw(f'\\draw (-{R:.3f},0) arc[start angle=180,end angle=360,x radius={R:.3f},y radius={ry:.3f}];')
f.raw(f'\\draw[dashed] (-{R:.3f},0) arc[start angle=180,end angle=0,x radius={R:.3f},y radius={ry:.3f}];')
V10=(0,Hs); Ar=(R,0); Al=(-R,0); O10=(0,0)
f.line(V10,Ar,'dashed'); f.line(V10,Al,'dashed'); f.line(O10,Ar,'dashed')
f.raw(f'\\fill {pt(V10)} circle (1pt); \\fill (0,0) circle (1pt);')
f.node((0,Hs+.27),'$V$'); f.node((R+.28,-.1),'$A$'); f.node((0,-.27),'$O$')
f.node((R/2,.21),'$3$')
mm=mid(V10,Ar); nn=un((Hs,R)); f.node(add(mm,mul(nn,.3)),'$5$')
SK10=f.svg()
q('0010',tipId='gep-silindir-koni',tip='Silindir içine yerleştirilmiş koni',z='zor',alt='Silindir ve Koni',kaz='Koninin ana doğrusundan yüksekliği bulup silindir ile koninin hacim farkını π cinsinden hesaplar.',
 kart='K-GEOP-10 (silindir, koni) · r = 3, ana doğru 5',
 metin='Şekilde taban yarıçapı |OA| = 3 cm olan bir dik silindirin içine, tabanı silindirin alt tabanıyla aynı olan ve tepe noktası V, silindirin üst tabanının merkezinde bulunan bir dik koni yerleştirilmiştir. Koninin ana doğrusu |VA| = 5 cm dir.\nBuna göre, silindirin içinde koninin dışında kalan bölgenin hacmi kaç cm³’tür?',
 dogru='24π',sira=['12π','21π','24π','30π','36π'],
 yan=[('12π','Yalnız koninin hacmini (⅓ × π × 9 × 4) bulup silindirden çıkarmamış.','dikkat'),('21π','Silindirde h = 4, konide ana doğruyu (5) yükseklik alıp 36π − 15π = 21π bulmuş.','bilgi'),('30π','Silindirin yüksekliğini de 5 alıp 45π − 15π = 30π bulmuş (ana doğru yükseklik değildir).','bilgi'),('36π','Yalnız silindirin hacmini (π × 9 × 4) hesaplamış.','dikkat')],
 istenen='Silindirin içinde koninin dışında kalan bölgenin hacmi (cm³).',
 ip=['Silindirin yüksekliğini bulmak için |OA|, |VA| ve |VO| hangi üçgeni oluşturuyor? Sonra iki hacmi karşılaştır.'],
 bilgi=[SIL,PIS],
 ad=[A('Yüksekliği bul','V’den tabana inen |VO| yüksekliği, |OA| = 3 ve |VA| = 5 ile dik üçgen oluşturur.','h² = 5² − 3² = 16 → h = 4'),A('Silindirin hacmi','Silindirin tabanı yarıçapı 3, yüksekliği 4.','π × 3² × 4 = 36π'),A('Koninin hacmi','Aynı taban ve yükseklikte koni silindirin üçte biridir.','36π ÷ 3 = 12π'),A('Farkı al','Koninin dışında kalan hacim.','36π − 12π = 24π')],
 puf='Koninin yüksekliği ana doğru değildir: h = √(l² − r²). Aynı taban ve yükseklikte koni silindirin hacminin 1/3’üdür.',sekil=SK10)

# =================== yaz ===================
def bitir_geo():
    for qq in P.ANA: qq['kardes']=None
    P.yaz(os.path.join(GD,'geopilot-1.json'),'/tmp/bos-geopilot.json')
    tipler={}
    for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=TIPK[c['tipId']]))['kartlar'].append(c['id'])
    json.dump(dict(konu='Geometri (pilot)',surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 TYT Geometri çıkmış soruları (yalnız mantık), MEB 9–10. sınıf geometri müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar','geopilot.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler))
bitir_geo()
