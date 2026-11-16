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
TIPK={}   # tipId -> uygulama konu anahtarı
def konu(k,ad): P.k=k; P.konu_adi=ad; H.KONU=ad
def kartla(id,alt,fikir,tuzak,z,adim,tipId,tip,kaynak=None):
    kart(id,alt,fikir,tuzak,z,'şekilli',adim,tipId,tip,kaynak or 'ÖSYM 2018–2026 TYT Geometri soruları (yalnız mantık) · MEB 9–10. sınıf geometri'); TIPK[tipId]=P.k
def q(no,ad,**k):
    kl=k.pop('kalip','şekilli'); mk(P,no,ad=ad,adim=len(ad),kalip=kl,**k)

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

def vtx(f,names,pts,c=None,d=.3):
    c=c or cen(pts)
    for n,p in zip(names,pts): f.vl(n,p,sub(p,c),d)
def bitir_geo(onek,ad):
    for qq in P.ANA: qq['kardes']=None
    P.yaz(os.path.join(GD,f'{onek}-1.json'),f'/tmp/bos-{onek}.json')
    tipler={}
    for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=TIPK[c['tipId']]))['kartlar'].append(c['id'])
    json.dump(dict(konu=ad,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 TYT Geometri çıkmış soruları (yalnız mantık), MEB 9–10. sınıf geometri müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar',f'{onek}.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler),'soru',len(P.ANA))
def bitir_geo(onek,konuadi):
    for qq in P.ANA: qq['kardes']=None
    P.yaz(os.path.join(GD,f'{onek}-1.json'),f'/tmp/bos-{onek}.json')
    tipler={}
    for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=TIPK[c['tipId']]))['kartlar'].append(c['id'])
    json.dump(dict(konu=konuadi,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 TYT Geometri çıkmış soruları (yalnız mantık), MEB 9–10. sınıf geometri müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar',f'{onek}.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler))
def dimout(f,p,q_,dv,dist,t,tl=.27):
    d=un(dv); p2=add(p,mul(d,dist)); q2=add(q_,mul(d,dist))
    f.line(p,add(p,mul(d,dist+.1)),'dotted'); f.line(q_,add(q_,mul(d,dist+.1)),'dotted')
    f.raw(f'\\draw[<->] {pt(p2)} -- {pt(q2)};'); f.node(add(mid(p2,q2),mul(d,tl)),t)
P=Parti('kare','Kare','geo|Kare',ders='TYT Geometri',idon='tytgeo')
KRE=B('Kare','dört kenarı eşit, dört açısı 90° olan dörtgendir. Kenarı a olan karenin çevresi 4a, alanı a², köşegeni a√2 dir; köşegenler eşit, birbirini dik ortalar ve köşe açılarını 45° ye böler. Örnek: kenarı 5 olan karenin köşegeni 5√2, alanı 25')
PIS=B('Pisagor bağıntısı','dik üçgende dik kenarların kareleri toplamı hipotenüsün karesine eşittir. Örnek: 3, 4, 5 üçgeni için 3² + 4² = 5²')
ICICE=B('Orta noktaları birleştirme','karenin kenar orta noktaları birleştirilince köşelerde dört eş dik üçgen kalır ve ortada yeni bir kare oluşur. Karenin alanı kenarının karesidir')
IKIZ=B('İkizkenar üçgen','eşit kenarların karşısındaki açılar eşittir; iç açıların toplamı 180°’dir. Örnek: tepe açısı 40° ise taban açıları 70° dir. Eşkenar üçgenin her açısı 60° dir')
ALANB=B('Alan bölüştürme','karenin içinde kalan üçgenlerin alanı, karenin alanından köşelerde kalan dik üçgenlerin alanları çıkarılarak bulunur. Dik üçgenin alanı dik kenarların çarpımının yarısıdır. Örnek: dik kenarları 4 ve 6 ise alan 12')
KARO=B('Karo sayma','eş karolarla boşluksuz döşenen karenin bir kenarındaki karo sayısı n ise kenar uzunluğu n × karo kenarıdır; toplam karo sayısı n² dir. Örnek: kenarı 5 karo olan döşemede 25 karo vardır')
ARTIS=B('Tam kare açılımı','(a + d)² = a² + 2ad + d² dir. Örnek: (5 + 2)² = 25 + 20 + 4 = 49')
konu('geo|Kare','Kare')
# ---- 01 köşegen → alan · kolay
kartla('K-GKR-01','Köşegenden alan','Köşegen kenarın √2 katıdır; kenar bulunur, alan kenarın karesidir.','Köşegeni kenar sanmak; kenarı köşegen × √2 yazmak; alan yerine çevre vermek.','kolay',3,'ge-kr-kosegen','Köşegenden kenar ve alan')
d=7; kenar=7; assert 2*d*d==2*kenar*kenar and kenar*kenar==49 and abs((d*sqrt(2))**2-98)<1e-9
assert 4*kenar==28 and 7*7==49 and abs((7*sqrt(2)*sqrt(2))**2-196)<1e-9
s=.45; Pt=[(0,0),(kenar*s,0),(kenar*s,kenar*s),(0,kenar*s)]
f=F(); f.poly(Pt); f.line(Pt[0],Pt[2],'dashed'); f.dik(Pt[0],Pt[1],Pt[3],.2); vtx(f,'ABCD',Pt,cen(Pt),.3)
m=mid(Pt[0],Pt[2]); f.node((m[0]-.35,m[1]+.3),'$7\\sqrt{2}$')
SK=f.svg()
q('0001',tipId='ge-kr-kosegen',tip='Köşegenden kenar ve alan',z='kolay',alt='Köşegen ve Alan',kaz='Kare biçimli bir cismin köşegeninden kenarını bulup alanını hesaplar.',kalip='hikâyeli',
 kart='K-GKR-01 (köşegenden alan) · köşegen 7√2',
 metin='Kare biçimli ABCD sehpa örtüsünün [AC] köşegeni şekilde cm cinsinden verilmiştir. Örtünün tamamı bir dantelle kaplanacak, dantel ise alanı kadar ölçülerek alınacaktır.\nBuna göre, örtünün alanı kaç cm² dir?',
 dogru='49',yan=[('28','Çevreyi (4 × 7) hesaplamış; alan istenmiş.','dikkat'),('49√2','Alanı kenar × köşegen (7 × 7√2) sanmış.','bilgi'),('98','Köşegeni kenar sanıp (7√2)² = 98 yazmış.','bilgi'),('196','Kenarı köşegen × √2 = 14 bulmuş (a√2 bağıntısını ters kullanmış): 14² = 196.','bilgi')],
 sira=['28','49','49√2','98','196'],
 istenen='Karenin alanı (cm²).',
 ip=['Karenin köşegeni ile kenarı arasındaki orantıyı hatırla; önce kenarı bul.'],
 bilgi=[KRE],
 ad=[A('Kenarı bul','Köşegen = kenar × √2.','a√2 = 7√2 → a = 7 cm'),A('Alanı hesapla','Kare alanı = kenar × kenar.','7 × 7 = 49 cm²'),A('Kontrol et','Köşegenin karesi alanın iki katıdır.','(7√2)² = 98 = 2 × 49')],
 puf='Köşegeni a√2 biçiminde verilen karede kenar doğrudan a dır; alan a² ve köşegenin karesinin yarısıdır.',sekil=SK)

# ---- 02 karolar · kolay
kartla('K-GKR-02','Karolardan oluşan kare','Büyük kare eş karolarla oluşmuştur; kenar = karo sayısı × karo kenarı; alan kenarın karesi.','Karo sayısını kenar sanmak; çevre ile alanı karıştırmak; karo sayısını (36) karo kenarıyla çarpmak.','kolay',3,'ge-kr-karo','Karolarla döşenmiş kare')
n=6; kb=40; ken=n*kb; assert ken==240 and ken*ken==57600 and 4*ken==960 and n*n*kb==1440 and kb*kb==1600
s=.5; N=n; Pt=[(0,0),(N*s,0),(N*s,N*s),(0,N*s)]
f=F(); f.poly(Pt)
for i in range(1,n): f.line((i*s,0),(i*s,N*s),'thin'); f.line((0,i*s),(N*s,i*s),'thin')
vtx(f,'ABCD',Pt,cen(Pt),.3)
f.raw(f'\\draw[<->] ({s:.3f},-.12) -- ({2*s:.3f},-.12);'); f.node((1.5*s,-.34),'$40$')
SK=f.svg()
q('0002',tipId='ge-kr-karo',tip='Karolarla döşenmiş kare',z='kolay',alt='Karolar ve Alan',kaz='Eş karolarla oluşturulan büyük karenin kenarını ve alanını karo ölçülerinden hesaplar.',kalip='hikâyeli',
 kart='K-GKR-02 (karolar) · 6 × 6 karo, kenar 40 cm',
 metin='Bir usta, şekildeki gibi eş kare karoları boşluk bırakmadan yan yana dizerek ABCD karesi biçiminde bir mutfak zemini döşemiştir. Bir karonun kenar uzunluğu şekilde santimetre cinsinden verilmiştir.\nBuna göre, ABCD biçimindeki zeminin alanı kaç cm² dir?',
 dogru='57600',yan=[('240','Büyük karenin kenarını (6 × 40) bulup bırakmış.','dikkat'),('960','Alan yerine çevreyi (4 × 240) hesaplamış.','dikkat'),('1440','Karo sayısını (36) karo kenarıyla (40) çarpmış.','bilgi'),('1600','Yalnız bir karonun alanını (40 × 40) bulmuş.','dikkat')],
 sira=['240','960','1440','1600','57600'],
 istenen='ABCD biçimindeki zeminin alanı (cm²).',
 ip=['Bir kenar boyunca kaç karo olduğunu şekilden say; sonra kenar uzunluğunu bul.'],
 bilgi=[KARO,KRE],
 ad=[A('Karoları say','Bir kenar boyunca şekilde 6 karo vardır.','n = 6'),A('Kenarı bul','Kenar = karo sayısı × karo kenarı.','6 × 40 = 240 cm'),A('Alanı hesapla','Kare alanı = kenar × kenar.','240 × 240 = 57600 cm²'),A('Kontrol et','36 karonun alanı toplamı da aynı olmalıdır.','36 × 1600 = 57600')],
 puf='Karolu döşemede bir kenardaki karo sayısı n ise alan = n² × (bir karonun alanı).',sekil=SK)

# ---- 03 iç içe kareler · orta
kartla('K-GKR-03','İç içe kareler','Her adımda kenar orta noktaları birleştirilince alan yarıya iner; iki adımda dörtte birine.','Alanı yarıya değil kenarı yarıya bölmek; bir adım eksik kalmak; çevre ile alanı karıştırmak.','orta',3,'ge-kr-icice','Orta noktalarla iç içe kareler')
a3=24; A0=a3*a3; A1=A0/2; A2=A1/2; assert (A0,A1,A2)==(576,288,144)
side2=sqrt(A2); assert side2==12 and 4*side2==48 and A1==288 and A0==576
s=.17; Pt=[(0,0),(a3*s,0),(a3*s,a3*s),(0,a3*s)]
Q=[mid(Pt[i],Pt[(i+1)%4]) for i in range(4)]; R=[mid(Q[i],Q[(i+1)%4]) for i in range(4)]
assert abs(alan(Q)/s/s-288)<1e-9 and abs(alan(R)/s/s-144)<1e-9
f=F(); f.poly(Pt); f.poly(Q); f.poly(R); vtx(f,'ABCD',Pt,cen(Pt),.3); vtx(f,'EFGH',Q,cen(Pt),.25); vtx(f,'KLMN',R,cen(Pt),.22)
f.raw(f'\\draw[<->] (0,-.62) -- ({a3*s:.3f},-.62);'); f.node((a3*s/2,-.85),'$24$')
SK=f.svg()
q('0003',tipId='ge-kr-icice',tip='Orta noktalarla iç içe kareler',z='orta',alt='İç İçe Kareler',kaz='Kenar orta noktalarının birleştirilmesiyle oluşan iç içe karelerde alanın her adımda yarıya indiğini kullanarak en içteki karenin alanını bulur.',
 kart='K-GKR-03 (iç içe kareler) · kenar 24, iki adım',
 metin='Bir mimar, şekildeki ABCD kare levhasının kenarlarının orta noktalarını E, F, G, H olarak işaretleyip birleştirerek EFGH karesini elde ediyor. Daha sonra EFGH karesinin kenarlarının orta noktaları K, L, M, N birleştirilerek KLMN karesi çiziliyor. [AB] nin uzunluğu şekilde cm cinsinden verilmiştir.\nBuna göre, en içteki KLMN karesinin alanı kaç cm² dir?',
 dogru=144,yan=[(12,'KLMN karesinin kenarını bulup bırakmış (24 ÷ 2).','dikkat'),(48,'KLMN karesinin çevresini (4 × 12) hesaplamış.','dikkat'),(288,'Yalnız bir adım uygulayıp EFGH nin alanını bulmuş.','dikkat'),(576,'ABCD karesinin alanını yazmış; iç kareleri hesaba katmamış.','dikkat')],
 istenen='KLMN karesinin alanı (cm²).',
 ip=['ABCD nin alanı ile EFGH nin alanı arasında nasıl bir oran var? Aynı oran bir adım daha tekrar eder.'],
 bilgi=[ICICE],
 ad=[A('ABCD nin alanı','Kenar 24 cm.','24 × 24 = 576 cm²'),A('EFGH nin alanı','Orta noktalar birleşince köşelerde dört eş dik üçgen kalır; iç kare alanın yarısıdır.','576 ÷ 2 = 288 cm²'),A('KLMN nin alanı','Aynı işlem EFGH için tekrar edilir.','288 ÷ 2 = 144 cm²'),A('Kontrol et','İki adımda alan dörtte birine iner; kenar da yarıya iner.','576 ÷ 4 = 144 = 12²')],
 puf='Kenar orta noktalarını birleştirmek karenin alanını yarıya, kenarını ise √2 ye böler; iki adımda kenar yarıya iner.',sekil=SK)

# ---- 04 kare + eşkenar üçgen · zor
kartla('K-GKR-04','Karenin içinde eşkenar üçgen','AE = AB = AD olduğundan ADE ikizkenardır; köşeler çevresindeki açılar toplamı 360° dir.','60° ile 30° açılarını karıştırmak; ikizkenar üçgenin taban açılarını yarıya bölmemek.','zor',5,'ge-kr-ucgen-aci','Kare ve eşkenar üçgenle açı')
a4=5.2; E4=(a4/2,a4*sqrt(3)/2); A4,B4,C4,D4=(0,0),(a4,0),(a4,a4),(0,a4)
assert abs(dist(A4,E4)-a4)<1e-9 and abs(dist(B4,E4)-a4)<1e-9 and E4[1]<a4
x4=ang(E4,D4,C4); assert abs(x4-150)<1e-9 and abs(ang(E4,A4,D4)-75)<1e-9 and abs(ang(A4,E4,D4)*0+ang(D4,E4,A4)-75)<1e-9
assert abs(x4+60+75+75-360)<1e-9 and 180-60==120 and 180-15==165 and 90-60==30
s=1.0; Pt=[A4,B4,C4,D4]
f=F(); f.poly(Pt); f.line(A4,E4); f.line(B4,E4); f.line(D4,E4); f.line(C4,E4); f.tick(A4,B4); f.tick(A4,E4); f.tick(B4,E4)
f.arc(E4,D4,C4,.28,'$x$',.55)
vtx(f,'ABCD',Pt,cen(Pt),.3); f.node((E4[0],E4[1]-.3),'$E$')
SK=f.svg()
q('0004',tipId='ge-kr-ucgen-aci',tip='Kare ve eşkenar üçgenle açı',z='zor',alt='Karede Eşkenar Üçgen',kaz='Kare ve içindeki eşkenar üçgenden ikizkenar üçgenleri bulup E noktası çevresindeki açıyı hesaplar.',
 kart='K-GKR-04 (kare + eşkenar üçgen) · ABE eşkenar, m(DEC)',
 metin='Bir tasarımcı, şekildeki ABCD kare levhasının içine [AB] kenarı üzerinde ABE eşkenar üçgenini çizmiş, ardından [DE] ve [CE] doğru parçalarını da çizmiştir. Şekil ölçekli değildir.\nBuna göre, x = m(DEC) kaç derecedir?',
 dogru=150,yan=[(30,'Yalnız m(DAE) = 90° − 60° = 30° yi bulup x olarak yazmış.','dikkat'),(75,'ADE ikizkenar üçgeninin taban açısını (75°) x sanmış.','dikkat'),(120,'E noktasında 180° − 60° = 120° yazmış (A, E, C ni doğrusal sanmış).','bilgi'),(165,'m(EDC) = 15° yi bulup 180° − 15° yazmış.','bilgi')],
 istenen='x = m(DEC) açısının ölçüsü.',
 ip=['|AE| ile |AD| arasında nasıl bir ilişki var? ADE ve BCE üçgenlerinin açılarını bul, E noktasının çevresindeki açıları topla.'],
 bilgi=[KRE,IKIZ],
 ad=[A('Eşit kenarları yaz','ABE eşkenar olduğundan |AE| = |AB|; kare olduğundan |AB| = |AD|.','|AE| = |AD|'),A('A açısını böl','m(DAE) = m(DAB) − m(EAB).','90° − 60° = 30°'),A('Taban açısını bul','ADE ikizkenar: tepe açısı 30°.','m(AED) = (180° − 30°) ÷ 2 = 75°'),A('Simetriyi kullan','BCE üçgeni de aynıdır: m(BEC) = 75°.','m(BEC) = 75°'),A('x i bul','E çevresindeki açıların toplamı 360° dir.','x = 360° − 60° − 75° − 75° = 150°')],
 puf='Karenin kenarı eşkenar üçgenin kenarıyla çakışırsa karenin iki kenarı eşit olur ve ikizkenar üçgenler oluşur.',sekil=SK)

# ---- 05 alan bölüşümü · orta
kartla('K-GKR-05','Orta noktalarla kesilen üçgen','Karenin alanından köşelerde kalan üç dik üçgenin alanı çıkarılır.','Yalnız bir üçgeni çıkarmak; üç üçgenin toplamını sonuç sanmak; yarı kareyi almak.','orta',4,'ge-kr-alan-bolusum','Karede alan bölüşümü')
a5=12; Ax,Bx,Cx,Dx=(0,0),(a5,0),(a5,a5),(0,a5); Ex=(a5,a5/2); Fx=(a5/2,a5)
sABE=a5*(a5/2)/2; sADF=sABE; sECF=(a5/2)**2/2; sAEF=a5*a5-sABE-sADF-sECF
assert abs(alan([Ax,Ex,Fx])-sAEF)<1e-9 and sAEF==54 and sABE==36 and sECF==18 and 2*sABE+sECF==90 and a5*a5-sABE==108 and a5*a5/2==72 and a5*a5==144
s=.3; Pt=[Ax,Bx,Cx,Dx]; Ps=[mul(p,s) for p in Pt]; Es=mul(Ex,s); Fs=mul(Fx,s)
f=F(); f.poly(Ps); f.line(Ps[0],Es); f.line(Ps[0],Fs); f.line(Es,Fs); f.tick(Ps[1],Es); f.tick(Es,Ps[2]); f.tick(Ps[2],Fs,2); f.tick(Fs,Ps[3],2)
vtx(f,'ABCD',Ps,cen(Ps),.3); f.node((Es[0]+.3,Es[1]),'$E$'); f.node((Fs[0],Fs[1]+.3),'$F$'); f.sl('$12$',Ps[0],Ps[1],cen(Ps),.28)
SK=f.svg()
q('0005',tipId='ge-kr-alan-bolusum',tip='Karede alan bölüşümü',z='orta',alt='Orta Noktalarla Üçgen',kaz='Karenin kenar orta noktalarını köşeye bağlayan üçgenin alanını, köşelerde kalan dik üçgenleri çıkararak bulur.',
 kart='K-GKR-05 (alan bölüşümü) · kenar 12, E ve F orta nokta',
 metin='Bir kâğıt katlama etkinliğinde, şekilde kenar uzunluğu 12 cm olan ABCD kare kâğıdı üzerinde E noktası [BC] nin, F noktası [CD] nin orta noktasıdır. A, E ve F noktaları birleştirilerek AEF üçgeni oluşturulmuştur.\nBuna göre, AEF üçgeninin alanı kaç cm² dir?',
 dogru=54,yan=[(72,'AEF üçgeninin alanını karenin yarısı (144 ÷ 2) sanmış.','bilgi'),(90,'Köşelerde kalan üç üçgenin alanları toplamını (36 + 36 + 18) AEF nin alanı sanmış.','dikkat'),(108,'Yalnız ABE üçgenini çıkarmış: 144 − 36.','dikkat'),(144,'Karenin alanını yazmış.','dikkat')],
 istenen='AEF üçgeninin alanı (cm²).',
 ip=['AEF dışında kalan üç parçanın hepsi dik üçgendir; hangi kenarlar dik kenar?'],
 bilgi=[ALANB],
 ad=[A('Karenin alanını yaz','Kenar 12 cm.','12 × 12 = 144 cm²'),A('ABE ve ADF üçgenleri','Dik kenarları 12 ve 6 dır.','12 × 6 ÷ 2 = 36 cm² (her biri)'),A('ECF üçgeni','Dik kenarları 6 ve 6 dır.','6 × 6 ÷ 2 = 18 cm²'),A('Farkı al','Karenin alanından üç dik üçgeni çıkar.','144 − 36 − 36 − 18 = 54 cm²')],
 puf='Köşeleri kareye oturan üçgenin alanı = karenin alanı − köşelerde kalan dik üçgenlerin alanları toplamı.',sekil=SK)

# ---- 06 nokta, kenarlara uzaklık · orta
kartla('K-GKR-06','İç noktanın kenarlara uzaklığı','Karşılıklı iki kenara uzaklıkların toplamı kenar uzunluğudur; diğer uzaklık kenardan çıkarılır.','Karşılıklı kenar yerine komşu kenarın uzaklığını yükseklik almak; ÷ 2 yi unutmak.','orta',4,'ge-kr-alan-bolusum','Karede alan bölüşümü')
a6=12; Pp=(8,3); assert Pp[1]==3 and a6-Pp[1]==9 and a6-Pp[0]==4 and Pp[0]==8
al6=a6*Pp[0]/2; assert al6==48 and a6*(a6-Pp[0])/2==24 and a6*(a6-Pp[1])/2==54 and a6*a6/2==72 and a6*Pp[0]==96 and a6*a6==144
s=.3; Pt=[(0,0),(a6*s,0),(a6*s,a6*s),(0,a6*s)]; Ps=mul(Pp,s)
f=F(); f.poly(Pt); f.line(Pt[0],Ps); f.line(Pt[3],Ps)
f.line(Ps,(Ps[0],0),'dashed'); f.line(Ps,(a6*s,Ps[1]),'dashed'); f.line(Ps,(Ps[0],a6*s),'dashed')
f.raw(f'\\fill {pt(Ps)} circle (1pt);'); vtx(f,'ABCD',Pt,cen(Pt),.3); f.node((Ps[0]+.27,Ps[1]-.22),'$P$')
f.node((Ps[0]-.2,Ps[1]/2),'$3$'); f.node(((Ps[0]+a6*s)/2,Ps[1]+.2),'$4$'); f.node((Ps[0]-.2,(Ps[1]+a6*s)/2+.4),'$9$')
SK=f.svg()
q('0006',tipId='ge-kr-alan-bolusum',tip='Karede alan bölüşümü',z='orta',alt='Kenarlara Uzaklık',kaz='Karenin içindeki bir noktanın üç kenara uzaklığından kenar uzunluğunu ve APD üçgeninin yüksekliğini bulup alanı hesaplar.',
 kart='K-GKR-06 (kenarlara uzaklık) · 3, 4, 9',
 metin='Bir bahçıvan, ABCD karesi biçimindeki bahçenin içine P noktasına bir fidan dikmiştir. Fidanın [AB], [BC] ve [CD] kenarlarına olan uzaklıkları şekilde cm cinsinden verilmiştir (şekil ölçekli değildir).\nBuna göre, APD üçgeninin alanı kaç cm² dir?',
 dogru=48,yan=[(54,'|CD| ye olan uzaklığı (9) APD nin yüksekliği sanmış: 12 × 9 ÷ 2.','dikkat'),(72,'Üçgenin alanını karenin yarısı (144 ÷ 2) sanmış.','bilgi'),(96,'Doğru yüksekliği (8) bulmuş ama alanı ÷ 2 yapmayı unutmuş.','islem'),(144,'Karenin alanını yazmış.','dikkat')],
 istenen='APD üçgeninin alanı (cm²).',
 ip=['Karşılıklı iki kenara olan uzaklıklar toplamı karenin kenarı hakkında ne söyler? APD üçgeninin tabanı [AD] dir; yüksekliğini düşün.'],
 bilgi=[KRE,ALANB],
 ad=[A('Kenarı bul','P, [AB] ve [CD] arasındadır; uzaklıklar toplamı kenar uzunluğudur.','|AB| = 3 + 9 = 12 cm'),A('[AD] ye uzaklığı bul','[BC] ye uzaklık 4 ise [AD] ye uzaklık kenardan çıkarılır.','12 − 4 = 8 cm'),A('Alanı hesapla','Taban |AD| = 12 ve yükseklik 8.','12 × 8 ÷ 2 = 48 cm²')],
 puf='Karşılıklı kenarlara uzaklıklar toplamı kenara eşittir; üçgenin yüksekliği, P noktasının taban olarak alınan kenara olan uzaklığıdır.',sekil=SK)

# ---- 07 kare, dik ve benzerlik · zor
kartla('K-GKR-07','Karede dik üçgen benzerliği','Dik kesişen iki doğru, karenin köşelerinde benzer dik üçgenler oluşturur; oran kurulup bilinmeyen kenar bulunur.','Benzer üçgenlerde karşılıklı kenarları eşlememek; orta nokta bilgisini unutmak; DF yerine CF vermek.','zor',4,'ge-kr-benzerlik','Karede dik ve benzerlik')
a7=12; A7,B7,C7,D7=(0,0),(a7,0),(a7,a7),(0,a7); E7=(a7,a7/2); CF=3; F7=(a7-CF,a7)
assert abs(((E7[0]-A7[0])*(F7[0]-E7[0])+(E7[1]-A7[1])*(F7[1]-E7[1])))<1e-9
assert a7/(a7/2)==(a7/2)/CF and a7-CF==9 and a7/2==6 and 12==a7 and 8==a7*2//3
s=.3; Ps=[mul(p,s) for p in (A7,B7,C7,D7)]; Es=mul(E7,s); Fs=mul(F7,s)
f=F(); f.poly(Ps); f.line(Ps[0],Es); f.line(Es,Fs); f.dik(Es,Ps[0],Fs,.22); f.tick(Ps[1],Es); f.tick(Es,Ps[2])
vtx(f,'ABCD',Ps,cen(Ps),.3); f.node((Es[0]+.3,Es[1]),'$E$'); f.node((Fs[0],Fs[1]+.3),'$F$'); f.sl('$12$',Ps[0],Ps[1],cen(Ps),.28)
SK=f.svg()
q('0007',tipId='ge-kr-benzerlik',tip='Karede dik ve benzerlik',z='zor',alt='Kare ve Benzerlik',kaz='Karenin içinde dik kesişen doğru parçalarının oluşturduğu benzer dik üçgenlerden bilinmeyen kenarı bulur.',kalip='hikâyeli',
 kart='K-GKR-07 (kare, dik, benzerlik) · kenar 12, E orta nokta',
 metin='Kare biçimli bir kâğıt şeritten kesilen ABCD parçasının kenar uzunluğu şekilde cm cinsinden verilmiştir. E noktası [BC] kenarının orta noktasıdır. Kâğıdın üzerine bir cetvelle, A noktasından E noktasına ve E noktasından [CD] kenarı üzerindeki F noktasına, [AE] ⊥ [EF] olacak biçimde iki doğru parçası çizilmiştir. Şekil ölçekli değildir.\nBuna göre, |DF| kaç cm dir?',
 dogru=9,yan=[(3,'|CF| yi bulup bırakmış; istenen |DF| = |DC| − |CF|.','dikkat'),(6,'F yi [CD] nin orta noktası sanıp |DF| = 12 ÷ 2 yazmış.','bilgi'),(8,'Benzerlik oranını yanlış eşleyip |CF| = 4 bulmuş: |DF| = 12 − 4.','bilgi'),(12,'F yi D ile çakışık sanıp |DF| = |DC| yazmış.','bilgi')],
 istenen='|DF| uzunluğu (cm).',
 ip=['A, B, E köşeli üçgenle E, C, F köşeli üçgenin açılarını karşılaştır; dik açı nerede?'],
 bilgi=[KRE],
 ad=[A('Açıları karşılaştır','[AE] ⊥ [EF] olduğundan m(BEA) + m(CEF) = 90°; ABE ve ECF dik üçgenlerinde dar açılar birbirini tamamlar.','m(BAE) = m(CEF)'),A('Benzerliği yaz','ABE ~ ECF (B ve C dik açılı).','|AB| / |EC| = |BE| / |CF|'),A('|CF| yi bul','|EC| = |BE| = 6.','12 / 6 = 6 / |CF| → |CF| = 3'),A('|DF| yi hesapla','|DF| = |DC| − |CF|.','12 − 3 = 9 cm')],
 puf='Dik kesişen doğrular dik üçgenlerde dar açıları tamamlayıcı yapar; bu da benzerlik ve oran kurmayı sağlar.',sekil=SK)

# ---- 08 kenar uzatma · orta
kartla('K-GKR-08','Kenarları uzatılan kare','Yeni alan (a + 3)² dir; fark 6a + 9 olur; a bulunur, çevre 4a.','Fark ifadesindeki 3 × 3 = 9 u unutmak; yeni karenin çevresini vermek; kenarı çevre sanmak.','orta',4,'ge-kr-uzatma','Kenarı uzatılan kare')
a8=9; assert (a8+3)**2-a8**2==63 and 4*a8==36 and 63/6*4==42 and 4*(a8+3)==48 and a8+3==12
s=.3; ou=(a8+3)*s; ia=a8*s; Pt=[(0,0),(ia,0),(ia,ia),(0,ia)]; Bg=[(0,0),(ou,0),(ou,ou),(0,ou)]
f=F(); f.raw('\\fill[vurgu!20,even odd rule] '+' -- '.join(map(pt,Bg))+' -- cycle '+' -- '.join(map(pt,Pt))+' -- cycle;')
f.poly(Bg); f.poly(Pt)
f.raw(f'\\draw[<->] ({ia:.3f},-.14) -- ({ou:.3f},-.14);'); f.node(((ia+ou)/2,-.36),'$3$'); f.raw(f'\\draw[<->] (-.14,{ia:.3f}) -- (-.14,{ou:.3f});'); f.node((-.36,(ia+ou)/2),'$3$')
f.node((-.3,-.3),'$A$'); f.node((ia-.3,-.3),'$B$'); f.node((ia-.3,ia-.3),'$C$'); f.node((-.3,ia-.35),'$D$')
SK=f.svg()
q('0008',tipId='ge-kr-uzatma',tip='Kenarı uzatılan kare',z='orta',alt='Kenarı Uzatılan Kare',kaz='Komşu iki kenarı uzatılan karede alan artışından kenarı bulup çevreyi hesaplar.',kalip='hikâyeli',
 kart='K-GKR-08 (kenar uzatma) · artış 63, uzatma 3',
 metin='Kare biçimli ABCD bahçesinin birbirine komşu iki kenarı, şekildeki gibi 3 m genişletilerek yine kare biçimli, daha büyük bir bahçe elde ediliyor. Genişletme sonunda bahçenin alanı 63 m² artmıştır.\nBuna göre, ilk bahçenin çevresi kaç m dir?',
 dogru=36,yan=[(9,'Kenarı bulup çevre yerine kenarı yazmış.','dikkat'),(12,'Yeni bahçenin kenarını (9 + 3) yazmış.','dikkat'),(42,'Alan farkını 6a = 63 almış (3 × 3 = 9 u unutmuş): a = 10,5 ve çevre 42.','islem'),(48,'Yeni bahçenin çevresini (4 × 12) hesaplamış.','dikkat')],
 istenen='İlk bahçenin çevresi (m).',
 ip=['Genişleyen bölgeyi iki dikdörtgen ve bir küçük kareye ayır; alanlarını a cinsinden yaz.'],
 bilgi=[ARTIS,KRE],
 ad=[A('Artışı yaz','Yeni kenar a + 3 tür; artış = (a + 3)² − a².','6a + 9 = 63'),A('Kenarı bul','Denklemi çöz.','6a = 54 → a = 9 m'),A('Çevreyi hesapla','Çevre = 4 × kenar.','4 × 9 = 36 m')],
 puf='Komşu iki kenarı d kadar uzatılan karenin alan artışı 2ad + d² dir; d² (köşe karesi) unutulmamalıdır.',sekil=SK)
bitir_geo('kare','Kare')
