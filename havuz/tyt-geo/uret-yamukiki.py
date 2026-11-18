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
STEP=A
P=Parti('yamukiki','Yamuk','geo|Yamuk',ders='TYT Geometri',idon='tytgeo')
def vls(f,names,pts,extra=None):
    c=cen(pts)
    for n,p in zip(names,pts): f.vl(n,p,sub(p,c),.3)
def ytab(D,C,a,h,x0): # D=(0,0) C=(c,0) A=(x0,h) B=(x0+a,h) (cm koordinat)
    return (x0,h),(x0+a,h),C,D
SRC='ÖSYM 2018–2026 TYT Geometri soruları (yalnız mantık) · MEB 9–10. sınıf geometri'
YALAN=B('Yamuğun alanı','alan = (taban + taban) ÷ 2 × yükseklik; yükseklik iki tabana dik olan uzaklıktır. Örnek: tabanları 6 ve 10, yüksekliği 4 olan yamuğun alanı 8 × 4 = 32’dir')
YCEV=B('Yamuğun çevresi','çevre dört kenarın toplamıdır. İkizkenar yamukta yan kenarlar birbirine eşittir. Örnek: tabanları 5 ve 9, yan kenarları 4 olan ikizkenar yamukta çevre 5 + 9 + 4 + 4 = 22’dir')
YORT=B('Orta taban','yamuğun yan kenarlarının orta noktalarını birleştiren doğru parçasıdır; tabanlara paraleldir ve uzunluğu tabanların aritmetik ortalamasıdır. Örnek: tabanlar 4 ve 12 ise orta taban 8’dir')
YIKIZ=B('İkizkenar yamuk','yan kenarları eşit olan yamuktur; aynı tabana ait açılar eşit, köşegenler eşittir. Örnek: bir taban açısı 65° ise diğer taban açısı da 65°, üst taban açıları 115°’dir')
YPAR=B('Paralel doğrularda açılar','iki paralel doğruyu bir kesen kesti, iç ters açıları eşit yapar. Örnek: d₁ // d₂ ve kesenle 40° yapan açının iç ters eşi de 40°’dir; aynı yan kenarın uçlarındaki açılar bütünlerdir')
YBEN=B('Benzer üçgenler ve paralel doğru','bir üçgende bir kenara paralel çizilen doğru, ayırdığı küçük üçgenle ilk üçgeni benzer yapar; kenarlar aynı oranda büyür. Örnek: iki benzer üçgende karşılıklı kenarlar 3 ve 9 ise oran 1 : 3’tür')
YPIS=B('Pisagor bağıntısı','dik üçgende dik kenarların kareleri toplamı hipotenüsün karesine eşittir: a² + b² = c². Örnek: dik kenarlar 5 ve 12 ise hipotenüs 13’tür')
YEU=B('İkizkenar üçgen','iki kenarı eşit olan üçgende karşılarındaki açılar eşittir. Örnek: bir ikizkenar üçgende tepe açısı 40° ise taban açıları 70°’dir')
YDIK=B('Dik üçgende yükseklik','dik üçgende hipotenüse inen yükseklik, hipotenüsü iki parçaya ayırır; yüksekliğin karesi bu iki parçanın çarpımına eşittir (Öklid bağıntısı). Örnek: parçalar 2 ve 8 ise yükseklik 4’tür')
YDKS=B('Orta noktaları birleştiren doğru','üçgende iki kenarın orta noktasını birleştiren doğru parçası üçüncü kenara paraleldir ve onun yarısı kadardır. Örnek: üçüncü kenar 10 ise orta noktalar doğrusu 5’tir')
konu('geo|Yamuk','Yamuk')

# ===== 01 · ikizkenar yamuk çevre · kolay =====
kartla('K-GYK-01','İkizkenar yamukta çevre','Yan kenarlar eşit olduğundan cebirsel ifadeler eşitlenir, x bulunur; çevre dört kenarın toplamıdır.','Yalnız bir yan kenarı eklemek; x’i yan kenar sanmak; tabanları unutmak.','kolay',3,'ge-yk-cevre','İkizkenar yamukta çevre')
a1,c1,x1=8,14,5; y1=2*x1-1; assert y1==x1+4==9 and a1+c1+2*y1==40 and a1+c1==22 and a1+c1+y1==31 and a1+c1+2*x1==32 and 40+9==49
s=.3; h=sqrt(y1**2-((c1-a1)/2)**2); D=(0,0); C=(c1*s,0); A=((c1-a1)/2*s,h*s); B_=((c1+a1)/2*s,h*s)
assert abs(dist(A,D)/s-9)<1e-9 and abs(dist(B_,C)/s-9)<1e-9
f=F(); f.poly([A,B_,C,D]); f.par(A,B_); f.par(D,C); f.tick(A,D); f.tick(B_,C); ic=cen([A,B_,C,D])
f.sl('$8$',A,B_,ic,.3); f.sl('$14$',D,C,ic,.3); f.sl('$2x-1$',A,D,ic,.55); f.sl('$x+4$',B_,C,ic,.55); vls(f,'ABCD',[A,B_,C,D])
SK=f.svg()
q('0001',tipId='ge-yk-cevre',tip='İkizkenar yamukta çevre',z='kolay',alt='İkizkenar Yamuk Çevresi',kaz='İkizkenar yamukta yan kenarları eşitleyip x’i bulur ve çevreyi hesaplar.',
 kart='K-GYK-01 (ikizkenar yamuk çevresi) · AB = 8, DC = 14, AD = 2x − 1, BC = x + 4',
 metin='Şekilde ikizkenar yamuk biçimli bir salonun ABCD zemin planı verilmiştir. [AB] // [DC] dir, |AD| = |BC| dir ve uzunluklar metre cinsindendir. Salonun bütün kenarları boyunca süpürgelik döşenecektir. Şekil ölçekli değildir.\nBuna göre, gereken süpürgelik uzunluğu kaç metredir?',
 dogru=40,yan=[(22,'Yalnız iki tabanın toplamını (8 + 14) yazmış.','dikkat'),(31,'Yan kenarlardan yalnız birini eklemiş: 8 + 14 + 9.','dikkat'),(32,'x = 5’i yan kenar sanıp 8 + 14 + 5 + 5 hesaplamış.','bilgi'),(49,'Yan kenarlardan birini iki kez sayıp 8 + 14 + 9 + 9 + 9 yazmış.','islem')],
 istenen='Yamuğun çevresi (m).',ip=['Hangi iki kenarın uzunluğu eşittir ve bu bilgiyle x’i nasıl bulabilirsin?'],bilgi=[YCEV],
 ad=[STEP('Yan kenarları eşitle','İkizkenar yamukta yan kenarlar eşittir.','2x − 1 = x + 4 → x = 5'),STEP('Yan kenarı bul','x yerine 5 yazılır.','|AD| = |BC| = 2·5 − 1 = 9'),STEP('Çevreyi topla','Dört kenarın uzunlukları toplanır.','8 + 14 + 9 + 9 = 40')],
 puf='Çevre sorularında önce bilinmeyen x’i bulmalı, sonra dört kenarın hepsini ayrı ayrı yazmalısın.',sekil=SK)

# ===== 02 · yamuk alan (yükseklik verilmiş) · kolay =====
kartla('K-GYK-02','Yamukta alan','Alan formülü: tabanların ortalaması çarpı yükseklik; dikmenin ayağı tabanın dışında/içinde olması fark etmez.','Tabanlardan yalnız birini kullanmak; 2’ye bölmeyi unutmak; çevre ile karıştırmak.','kolay',2,'ge-yk-alan','Yamuğun alanı')
a2,c2,h2=7,13,5; assert (a2+c2)/2*h2==50 and a2*h2==35 and c2*h2==65 and (a2+c2)*h2==100 and (a2+c2)==20
s=.3; D=(0,0); C=(c2*s,0); A=(2.5*s,h2*s); B_=(2.5*s+a2*s,h2*s); Hh=(A[0],0)
f=F(); f.poly([A,B_,C,D]); f.line(A,Hh,'dashed'); f.dik(Hh,A,C); f.par(A,B_); f.par(D,C); ic=cen([A,B_,C,D])
f.sl('$7$',A,B_,ic,.3); f.sl('$13$',D,C,ic,.3); f.node(add(mid(A,Hh),(.22,0)),'$5$'); vls(f,'ABCD',[A,B_,C,D]); f.vl('H',Hh,(0,-1),.3)
SK=f.svg()
q('0002',tipId='ge-yk-alan',tip='Yamuğun alanı',z='kolay',alt='Yamuğun Alanı',kaz='Yamuğun tabanlarını ve yüksekliğini kullanarak alanı hesaplar.',
 kart='K-GYK-02 (yamuk alanı) · AB = 7, DC = 13, AH = 5, AH ⊥ DC',
 metin='Şekilde yamuk biçimli bir cam levhanın ABCD krokisi verilmiştir. [AB] // [DC] dir, [AH] ⊥ [DC] dir ve uzunluklar cm cinsindendir. Şekil ölçekli değildir.\nBuna göre, levhanın bir yüzünün alanı kaç cm² dir?',
 dogru=50,yan=[(20,'İki tabanın toplamını (7 + 13) cevap sanmış.','dikkat'),(35,'Üst taban ile yüksekliği çarpmış: 7 × 5.','bilgi'),(65,'Alt taban ile yüksekliği çarpmış: 13 × 5.','bilgi'),(100,'Tabanlar toplamını yükseklikle çarpıp 2’ye bölmeyi unutmuş: 20 × 5.','islem')],
 istenen='Levhanın alanı (cm²).',ip=['Yamuğun alanı için hangi uzunluklar gerekir? Verilenlerden hangisi yüksekliktir?'],bilgi=[YALAN],
 ad=[STEP('Tabanları ve yüksekliği belirle','[AB] // [DC] olduğundan tabanlar bunlardır; [AH] tabana dik olduğundan yüksekliktir.','tabanlar 7 ve 13, yükseklik 5'),STEP('Tabanların ortalamasını bul','İki tabanın toplamı 2’ye bölünür.','(7 + 13) ÷ 2 = 10'),STEP('Yükseklikle çarp','Alan = ortalama taban × yükseklik.','10 × 5 = 50')],
 puf='Yamuk alanında iki tabanı da kullan ve toplamı 2’ye bölmeyi unutma.',sekil=SK)

# ===== 03 · orta taban ve köşegenler · orta =====
kartla('K-GYK-03','Orta taban ve köşegenler','Orta taban köşegenleri de ortalar; ABD ve ACD üçgenlerinde orta noktalar doğrusu özelliği ile parçalar bulunur, fark alınır.','Orta tabanı cevap sanmak; parçaları eşit üçe bölmek; yalnız bir parçayı yazmak.','orta',3,'ge-yk-orta','Orta taban ve köşegenler')
a3,c3=8,20; e3=(a3+c3)/2; eh=a3/2; gh=(c3-a3)/2; assert (e3,eh,gh)==(14,4,6) and e3==eh+gh+eh and c3/2==10 and c3-a3==12
s=.25; D=(0,0); C=(c3*s,0); A=(1.0,2.4); B_=(1.0+a3*s,2.4); E=mid(A,D); Fp=mid(B_,C); G=mid(A,C); Hq=mid(B_,D)
assert abs(dist(Hq,G)/s-6)<1e-9 and abs(dist(E,Hq)/s-4)<1e-9 and abs(dist(E,Fp)/s-14)<1e-9 and abs(E[1]-G[1])<1e-9
f=F(); f.poly([A,B_,C,D]); f.line(A,C); f.line(B_,D); f.line(E,Fp,'dashed'); f.par(A,B_); f.par(D,C); f.tick(A,E); f.tick(E,D); f.tick(B_,Fp); f.tick(Fp,C); ic=cen([A,B_,C,D])
f.sl('$8$',A,B_,ic,.3); f.sl('$20$',D,C,ic,.3)
vls(f,'ABCD',[A,B_,C,D]); f.vl('E',E,(-1,0),.3); f.vl('F',Fp,(1,0),.3); f.node(add(Hq,(-.1,.26)),'$H$'); f.node(add(G,(.2,-.24)),'$G$')
SK=f.svg()
q('0003',tipId='ge-yk-orta',tip='Orta taban ve köşegenler',z='orta',alt='Orta Taban ve Köşegenler',kaz='Yamukta orta tabanın köşegenlerle ayrılan parçalarından aradaki parçanın uzunluğunu bulur.',
 kart='K-GYK-03 (orta taban ve köşegenler) · AB = 8, DC = 20, E ve F orta nokta, EF ∩ BD = H, EF ∩ AC = G',
 metin='Şekildeki ABCD yamuğunda [AB] // [DC] dir, |AB| = 8 cm ve |DC| = 20 cm dir. E ve F noktaları yan kenarların orta noktalarıdır. [EF] orta tabanı, [BD] köşegenini H noktasında, [AC] köşegenini G noktasında kesmektedir. Şekil ölçekli değildir.\nBuna göre, |HG| kaç cm dir?',
 dogru=6,yan=[(4,'Yalnız |EH| = 8 ÷ 2 = 4 parçasını bulup cevap yazmış.','dikkat'),(10,'|DC| ÷ 2 = 10’u cevap sanmış.','bilgi'),(12,'|DC| − |AB| = 12 farkını yarılamadan yazmış.','islem'),(14,'Orta tabanın tamamını (|EF| = 14) cevap sanmış.','dikkat')],
 istenen='|HG| uzunluğu (cm).',ip=['ABD üçgeninde [EH] ile [AB] arasında nasıl bir ilişki vardır? ACD üçgeninde [EG] için aynı soruyu sor.'],bilgi=[YORT,YDKS],
 ad=[STEP('Orta tabanı bul','Orta taban tabanların ortalamasıdır.','|EF| = (8 + 20) ÷ 2 = 14'),STEP('|EH| ve |GF|’yi bul','ABD ve ABC üçgenlerinde E ile F orta noktalarını bir köşeye bağlayan doğru [AB]’nin yarısı uzunluğundadır.','|EH| = |GF| = 8 ÷ 2 = 4'),STEP('Ortadaki parçayı hesapla','Orta tabandan iki uç parça çıkarılır.','|HG| = 14 − 4 − 4 = 6')],
 puf='Orta tabanı üç parçaya ayıran köşegenleri görünce, uç parçaların hangi tabanın yarısı olduğunu düşün.',sekil=SK)

# ===== 04 · ikizkenar yamuk dik köşegen · zor =====
kartla('K-GYK-04','Köşegenleri dik ikizkenar yamuk','Köşegenlerden biri paralel kaydırılarak yamuk bir üçgene dönüştürülür; oluşan üçgenden yükseklik bulunur ve alan formülü uygulanır.','Alan formülünde yüksekliği tabanlardan biri sanmak; köşegen uzunluğu istemek; yamuğu iki eş üçgenin toplamı sanmak.','zor',4,'ge-yk-alan','Yamuğun alanı')
a4,c4=6,14; h4=(a4+c4)/2; al4=(a4+c4)/2*h4; assert h4==10 and al4==100 and a4*h4==60 and (a4+c4)/2*(c4/2)==70 and c4*a4==84 and al4/2==50
s=.28; D=(0,0); C=(c4*s,0); A=((c4-a4)/2*s,h4*s); B_=((c4+a4)/2*s,h4*s)
AC=sub(C,A); BD=sub(D,B_); assert abs(AC[0]*BD[0]+AC[1]*BD[1])<1e-9 and abs(dist(A,D)-dist(B_,C))<1e-9 and abs(alan([A,B_,C,D])/s**2-100)<1e-9
K=lerp(A,C,a4/(a4+c4))
f=F(); f.poly([A,B_,C,D]); f.line(A,C); f.line(B_,D); f.dik(K,A,B_,.2); f.tick(A,D); f.tick(B_,C); f.par(A,B_); f.par(D,C); ic=cen([A,B_,C,D])
f.sl('$6$',A,B_,ic,.3); f.sl('$14$',D,C,ic,.3); vls(f,'ABCD',[A,B_,C,D])
SK=f.svg()
q('0004',tipId='ge-yk-alan',tip='Yamuğun alanı',z='zor',alt='Köşegenleri Dik Yamuk',kaz='Köşegenleri dik olan ikizkenar yamukta köşegeni kaydırarak yüksekliği bulur ve alanı hesaplar.',
 kart='K-GYK-04 (köşegenleri dik ikizkenar yamuk) · AB = 6, DC = 14, AC ⊥ BD',
 metin='Şekildeki ABCD ikizkenar yamuğunda [AB] // [DC] dir, |AD| = |BC| dir ve köşegenler birbirine diktir. |AB| = 6 cm ve |DC| = 14 cm dir. Şekil ölçekli değildir.\nBuna göre, ABCD yamuğunun alanı kaç cm² dir?',
 dogru=100,yan=[(50,'Alanı 2’ye iki kez bölmüş: (6 + 14) ÷ 2 ÷ 2 × 10.','islem'),(60,'Üst taban ile yüksekliği (6 × 10) çarpmış.','bilgi'),(70,'Yüksekliği alt tabanın yarısı (7) sanıp 10 × 7 hesaplamış.','bilgi'),(84,'Yüksekliği üst taban (6) sanıp alt tabanla çarpmış: 14 × 6.','bilgi')],
 istenen='Yamuğun alanı (cm²).',ip=['Yükseklik verilmemiş. Köşegenlerin birbirine dik olması yüksekliği bulmak için nasıl kullanılabilir?'],bilgi=[YALAN,YIKIZ],
 ad=[STEP('Paralel çiz','B noktasından [AC]’ye paralel çizilip [DC] uzantısı E’de kesilsin; ABEC paralelkenar olur.','|CE| = |AB| = 6 → |DE| = 14 + 6 = 20 ve |BE| = |AC|'),STEP('Üçgeni tanı','İkizkenar yamukta köşegenler eşittir; [BE] // [AC] ve [AC] ⊥ [BD] olduğundan [BE] ⊥ [BD].','|BD| = |BE| ve m(DBE) = 90° → DBE dik ikizkenar üçgendir'),STEP('Yüksekliği bul','Dik ikizkenar üçgende hipotenüse inen yükseklik hipotenüsün yarısıdır; bu yükseklik yamuğun yüksekliğidir.','h = |DE| ÷ 2 = 10'),STEP('Alanı hesapla','Tabanlar 6 ve 14, yükseklik 10.','(6 + 14) ÷ 2 × 10 = 100')],
 puf='Yükseklik verilmemişse köşegen, yan kenar gibi verileri kullanarak yardımcı bir üçgen kurmaya çalış.',sekil=SK)

# ===== 05 · dik yamuk, AC ⊥ BC · zor =====
kartla('K-GYK-05','Dik yamukta dik köşegen-yan kenar','Eğik yan kenar ile köşegen dik olduğundan C’den indirilen dikme hipotenüse inen yüksekliktir; Öklid bağıntısıyla dik yan kenar bulunur.','Pisagorda hatalı kenarları seçmek; yüksekliği tabanlar farkı sanmak; ortalama almak.','zor',3,'ge-yk-dik','Dik yamukta yardımcı dikme')
a5,c5,h5=13,9,6; assert c5*(a5-c5)==h5**2 and a5-c5==4
s=.3; D=(0,0); C=(c5*s,0); A=(0,h5*s); B_=(a5*s,h5*s); AC=sub(C,A); BC=sub(C,B_); assert abs(AC[0]*BC[0]+AC[1]*BC[1])<1e-9
f=F(); f.poly([A,B_,C,D]); f.line(A,C); f.dik(D,A,C); f.dik(A,D,B_); f.dik(C,A,B_,.2); f.par(A,B_); f.par(D,C); ic=cen([A,B_,C,D])
f.sl('$13$',A,B_,ic,.3); f.sl('$9$',D,C,ic,.3); f.sl('$x$',A,D,ic,.3); vls(f,'ABCD',[A,B_,C,D])
SK=f.svg()
q('0005',tipId='ge-yk-dik',tip='Dik yamukta yardımcı dikme',z='zor',alt='Dik Yamukta Dik Köşegen',kaz='Dik yamukta yardımcı dikme çizip dik üçgende yükseklik bağıntısıyla dik yan kenarı bulur.',
 kart='K-GYK-05 (dik yamuk, AC ⊥ BC) · AB = 13, DC = 9, AD = x',
 metin='Şekildeki ABCD dik yamuğunda [AB] // [DC], [AD] ⊥ [DC] ve [AC] ⊥ [BC] dir. |AB| = 13 cm ve |DC| = 9 cm dir. Şekil ölçekli değildir.\nBuna göre, x = |AD| kaç cm dir?',
 dogru=6,yan=[(4,'Tabanların farkını (13 − 9) cevap sanmış.','bilgi'),(9,'|DC| uzunluğunu |AD| sanmış.','dikkat'),(11,'Tabanların ortalamasını (13 + 9) ÷ 2 almış.','bilgi'),(13,'|AB| uzunluğunu cevap sanmış.','dikkat')],
 istenen='|AD| uzunluğu (cm).',ip=['C noktasından [AB]’ye inilen dikme hangi uzunlukları belirler?'],bilgi=[YPIS],
 ad=[STEP('Dikme çiz','C’den [AB]’ye inilen dikmenin ayağı H olsun; ADCH dikdörtgen olur.','|AH| = |DC| = 9, |CH| = |AD| = x, |HB| = 13 − 9 = 4'),STEP('Yükseklik bağıntısı','ACB üçgeninde C açısı dik, [CH] hipotenüse inen yüksekliktir.','x² = |AH| · |HB| = 9 × 4 = 36'),STEP('x’i bul','Pozitif kök alınır.','x = 6')],
 puf='Dik üçgeni bulamadığında dik yamukta köşelerden tabana dikme indirmek çoğu zaman yeni bir dik üçgen kurar.',sekil=SK)

# ===== 06 · orta noktadan alan · orta =====
kartla('K-GYK-06','Yan kenarın orta noktası ve alan','Yan kenarın orta noktası ile karşı yan kenarın uçları birleştirilirse oluşan üçgenin alanı yamuk alanının sabit bir kesridir; alan önce hesaplanır.','Üçgenin alanını yamuk alanı sanmak; yarı yerine çeyrek almak; üçgen alanı formülünde yanlış taban seçmek.','orta',3,'ge-yk-alan','Yamuğun alanı')
a6,c6,h6=10,14,8; S6=(a6+c6)/2*h6; assert S6==96 and S6/2==48 and S6/4==24 and c6*h6/2==56 and a6*h6/2==40
s=.3; D=(0,0); C=(c6*s,0); A=(3.0*s,h6*s); B_=((3.0+a6)*s,h6*s); E=mid(A,D); Hh=(A[0],0)
assert abs(alan([B_,E,C])/s**2-48)<1e-9
f=F(); f.fill([B_,E,C]); f.poly([A,B_,C,D]); f.line(A,Hh,'dashed'); f.dik(Hh,A,C,.18); f.par(A,B_); f.par(D,C); f.tick(A,E); f.tick(E,D); ic=cen([A,B_,C,D])
f.sl('$10$',A,B_,ic,.3); f.sl('$14$',D,C,ic,.3); f.node(add(lerp(A,Hh,.78),(-.2,0)),'$8$'); vls(f,'ABCD',[A,B_,C,D]); f.vl('E',E,(-1,0),.3)
SK=f.svg()
q('0006',tipId='ge-yk-alan',tip='Yamuğun alanı',z='orta',alt='Orta Noktadan Oluşan Üçgen',kaz='Yamuğun alanını bulup yan kenarın orta noktasıyla oluşan taralı üçgenin alanını hesaplar.',
 kart='K-GYK-06 (yamuğun yarısı olan üçgen) · AB = 10, DC = 14, yükseklik 8, E orta nokta',
 metin='Şekildeki yamuk biçimli ABCD bahçesinde [AB] // [DC], [AH] ⊥ [DC] dir ve E noktası [AD] kenarının orta noktasıdır. Uzunluklar metre cinsindendir. Bahçenin taralı BEC bölümüne çim ekilecektir. Şekil ölçekli değildir.\nBuna göre, çim ekilecek alan kaç m² dir?',
 dogru=48,yan=[(24,'Taralı alanı yamuk alanının dörtte biri sanmış.','bilgi'),(40,'Taban olarak |AB|’yi, yükseklik olarak 8’i alıp 10 × 8 ÷ 2 hesaplamış.','bilgi'),(56,'Taban olarak |DC|’yi, yükseklik olarak 8’i alıp 14 × 8 ÷ 2 hesaplamış.','bilgi'),(96,'Bütün bahçenin alanını cevap sanmış.','dikkat')],
 istenen='Taralı BEC bölgesinin alanı (m²).',ip=['Önce bahçenin tamamının alanını bulabilir misin? Taralı üçgenin köşelerinden biri yan kenarın orta noktasında; bu üçgen ile yamuk arasındaki ilişkiyi bulmak için E’den tabanlara paralel çizmeyi dene.'],bilgi=[YALAN,YDKS],
 ad=[STEP('Yamuğun alanını bul','Tabanlar 10 ve 14, yükseklik 8.','Alan(ABCD) = (10 + 14) ÷ 2 × 8 = 96'),STEP('E’den orta taban çiz','E’den tabanlara çizilen paralel [BC]’yi F’de keser; F de [BC]’nin orta noktasıdır ve |EF| = (10 + 14) ÷ 2 = 12’dir.','|EF| = 12'),STEP('BEC’yi ikiye böl','BEC üçgeni, ortak tabanı [EF] olan BEF ve FEC üçgenlerinden oluşur; yükseklikleri toplamı 8’dir.','Alan(BEC) = 12 × 8 ÷ 2 = 48')],
 puf='Yan kenarın orta noktası verilince çoğu soruda orta tabanı çizmek işe yarar.',sekil=SK)

# ===== 07 · üç eşit kenar · orta =====
kartla('K-GYK-07','Yarım altıgen yamuk','Üç kenarı eşit yamukta alt taban iki katı ise orta noktadan paralelkenarlar ve eşkenar üçgenler kurulur; açı hesabı yapılır.','Köşegeni açıortay sanıp 60°’yi yazmak; yamuğun açıları bütünlerini karıştırmak.','orta',4,'ge-yk-ikiz','Eş kenarlı yamukta açı')
s7=6; h7=3*sqrt(3); A=(0,0); B_=(12*0.3,0); D=(3*.3,h7*.3); C=(9*.3,h7*.3)
A=(0,0);B_=(12,0);D=(3,h7);C=(9,h7); assert abs(dist(A,D)-6)<1e-9 and abs(dist(D,C)-6)<1e-9 and abs(dist(C,B_)-6)<1e-9
assert abs(ang(C,A,B_)-90)<1e-9 and abs(ang(D,A,C)-120)<1e-9
sc=.3; P_=[mul(p,sc) for p in (A,B_,C,D)]; A_,B2,C2,D2=P_
f=F(); f.poly([A_,B2,C2,D2]); f.line(A_,C2); f.par(A_,B2); f.par(D2,C2); f.tick(A_,D2); f.tick(D2,mid(D2,C2)); f.tick(C2,B2); ic=cen(P_)
f.sl('$12$',A_,B2,ic,.3); f.vl('A',A_,(-1,-1),.3); f.vl('B',B2,(1,-1),.3); f.vl('C',C2,(1,1),.3); f.vl('D',D2,(-1,1),.3); f.arc(C2,A_,B2,.45,'$x$',.8)
SK=f.svg()
q('0007',tipId='ge-yk-ikiz',tip='Eş kenarlı yamukta açı',z='orta',alt='Üç Kenarı Eşit Yamuk',kaz='Üç kenarı eşit olan ve tabanı iki katına çıkan yamukta orta nokta kurarak köşegenin oluşturduğu açıyı bulur.',
 kart='K-GYK-07 (üç eşit kenarlı yamuk) · AD = DC = CB, AB = 12, x = m(ACB)',
 metin='Şekildeki ABCD yamuğunda [AB] // [DC] dir, |AD| = |DC| = |CB| = 6 cm ve |AB| = 12 cm dir. Şekil ölçekli değildir.\nBuna göre, x = m(ACB) kaç derecedir?',
 dogru=90,yan=[(30,'m(CAB) açısını bulup x sanmış.','dikkat'),(45,'[AC]’yi m(DCB) açısının açıortayı sanıp 90° ÷ 2 almış.','bilgi'),(60,'Eşkenar üçgenin açısını (60°) cevap sanmış.','bilgi'),(75,'30° ile 45° açılarını toplamış.','islem')],
 istenen='x = m(ACB) açısının ölçüsü (derece).',ip=['|AD| = |DC| = |CB| eşitliği ve |AB| = 2·|DC| olması hangi özel şekilleri düşündürür?'],bilgi=[YEU,YPAR],
 ad=[STEP('Orta noktayı al','[AB]’nin orta noktası M olsun; |AM| = |DC| = 6 ve [AM] // [DC] olduğundan AMCD paralelkenardır.','|MC| = |AD| = 6'),STEP('Eşkenar üçgeni bul','|MB| = 6, |BC| = 6 ve |MC| = 6 olduğundan MBC eşkenar üçgendir.','m(CMB) = m(MBC) = 60°'),STEP('AMC üçgenini çöz','|MA| = |MC| = 6 ve m(AMC) = 180° − 60° = 120° olduğundan taban açıları eşittir.','m(MCA) = (180° − 120°) ÷ 2 = 30°'),STEP('x’i bul','Açılar toplanır.','x = 30° + 60° = 90°')],
 puf='Eşit kenarlı yamuklarda kenar uzunlukları arasındaki oranlara bakıp bildiğin özel şekilleri ara.',sekil=SK)

# ===== 08 · dik yamuk açı · orta =====
kartla('K-GYK-08','Dik yamukta eşit kenar ve açı','Eşit kenardan ikizkenar üçgen, paralellikten iç ters açı bulunur; köşegen C açısını ikiye böler; dik açıdan istenen açı bulunur.','Köşegeni açıortay olarak kullanıp 32° yerine 64° kullanmak; 90° − 64° yapmak.','orta',3,'ge-yk-aci','Dik yamukta açı')
c8=64; al8=c8/2; x8=90-al8; assert x8==58
b8=3; Cx=b8*(1+cos(radians(c8))); hh8=b8*sin(radians(c8)); D=(0,0); A=(0,hh8); B_=(b8,hh8); C=(Cx,0)
assert abs(dist(B_,C)-b8)<1e-9 and abs(ang(C,B_,D)-64)<1e-9 and abs(ang(A,D,C)-58)<1e-9 and abs(ang(C,A,B_)-32)<1e-9
f=F(); f.poly([A,B_,C,D]); f.line(A,C); f.dik(D,A,C); f.dik(A,D,B_); f.tick(A,mid(A,B_)); f.tick(B_,C); f.par(A,B_); f.par(D,C)
f.arc(C,B_,D,.45); f.node(add(C,mul((cos(radians(166)),sin(radians(166))),1.0)),'$64^\\circ$'); f.arc(A,D,C,.5,'$x$',.8); vls(f,'ABCD',[A,B_,C,D])
SK=f.svg()
q('0008',tipId='ge-yk-aci',tip='Dik yamukta açı',z='orta',alt='Dik Yamukta Açı',kaz='Dik yamukta eşit kenarlı üçgen ve iç ters açılarla köşegenin oluşturduğu açıyı bulur.',
 kart='K-GYK-08 (dik yamukta açı) · AB = BC, m(BCD) = 64°, x = m(DAC)',
 metin='Şekildeki ABCD dik yamuğunda [AB] // [DC], [AD] ⊥ [DC] ve |AB| = |BC| dir. m(BCD) = 64° dir. Şekil ölçekli değildir.\nBuna göre, x = m(DAC) kaç derecedir?',
 dogru=58,yan=[(26,'90° − 64° işlemini yapmış.','islem'),(32,'m(BAC) açısını bulup x sanmış.','dikkat'),(45,'Dik açıyı ikiye bölüp 45° bulmuş.','bilgi'),(64,'Verilen açıyı x’e eşit almış.','dikkat')],
 istenen='x = m(DAC) açısının ölçüsü (derece).',ip=['|AB| = |BC| olduğunda ABC üçgeninde hangi iki açı eşittir? [AB] // [DC] olduğundan bu açılardan biri başka hangi açıya eşittir?'],bilgi=[YEU,YPAR],
 ad=[STEP('İkizkenar üçgen','|AB| = |BC| olduğundan ABC üçgeninde karşılarındaki açılar eşittir.','m(BAC) = m(BCA) = α'),STEP('İç ters açı','[AB] // [DC] ve [AC] kesen olduğundan iç ters açılar eşittir.','m(ACD) = m(BAC) = α'),STEP('α’yı bul','C köşesindeki açı iki parçadan oluşur.','α + α = 64° → α = 32°'),STEP('x’i bul','A köşesi dik açıdır: m(DAB) = 90°.','x = 90° − 32° = 58°')],
 puf='Eşit kenar ve paralel doğrular birlikte verilince köşegen açıyı ikiye böler.',sekil=SK)

# ===== 09 · paralel doğru oranı · orta =====
kartla('K-GYK-09','Tabanlara paralel doğru','Yan kenar üzerinde verilen orana göre paralel doğrunun uzunluğu iki taban arasında aynı oranda ilerler; yardımcı paralel çizimle bulunur.','Orta taban formülünü uygulamak; oranı ters kurmak; yalnız farkın üçte birini yazmak.','orta',3,'ge-yk-paralel','Tabanlara paralel doğrunun uzunluğu')
a9,c9=8,14; e9=a9+(c9-a9)/3; assert e9==10 and (a9+c9)/2==11 and a9+(c9-a9)*2/3==12 and (c9-a9)/3==2 and c9-a9==6
s=.3; D=(0,0); C=(c9*s,0); A=(.9,2.4); B_=(.9+a9*s,2.4); E=lerp(A,D,1/3); Fp=lerp(B_,C,1/3)
assert abs(E[1]-Fp[1])<1e-9 and abs(dist(E,Fp)/s-10)<1e-9
f=F(); f.poly([A,B_,C,D]); f.line(E,Fp,'dashed'); f.par(A,B_); f.par(D,C); f.par(E,Fp); ic=cen([A,B_,C,D])
f.sl('$8$',A,B_,ic,.3); f.sl('$14$',D,C,ic,.3); vls(f,'ABCD',[A,B_,C,D]); f.vl('E',E,(-1,0),.3); f.vl('F',Fp,(1,0),.3)
SK=f.svg()
q('0009',tipId='ge-yk-paralel',tip='Tabanlara paralel doğrunun uzunluğu',z='orta',alt='Tabanlara Paralel Doğru',kaz='Yan kenar üzerindeki orana göre tabanlara paralel doğru parçasının uzunluğunu bulur.',
 kart='K-GYK-09 (tabanlara paralel doğru) · AB = 8, DC = 14, AE : ED = 1 : 2',
 metin='Şekildeki ABCD yamuğunda [AB] // [DC] dir. E noktası [AD] üzerinde, F noktası [BC] üzerindedir, [EF] // [AB] dir ve |AE| : |ED| = 1 : 2 dir. |AB| = 8 cm, |DC| = 14 cm dir. Şekil ölçekli değildir.\nBuna göre, |EF| kaç cm dir?',
 dogru=10,yan=[(11,'[EF]’yi orta taban sanıp (8 + 14) ÷ 2 yazmış.','bilgi'),(12,'Oranı ters kurup 8 + 6 × 2 ÷ 3 = 12 bulmuş.','islem'),(14,'Alt tabanın uzunluğunu (|DC| = 14) cevap sanmış.','dikkat'),(22,'İki tabanı toplayıp (8 + 14) cevap yazmış.','dikkat')],
 istenen='|EF| uzunluğu (cm).',ip=['A’dan [BC]’ye paralel çizip [EF] ve [DC] ile kesiştirsen hangi benzer üçgenler oluşur?'],bilgi=[YBEN],
 ad=[STEP('Paralel çiz','A’dan [BC]’ye paralel çizilip [EF] ile P’de, [DC] ile Q’da kesilsin; oluşan ABFP ve ABCQ paralelkenarlardır.','|PF| = 8 ve |QC| = 8 → |DQ| = 14 − 8 = 6'),STEP('Benzerliği yaz','APE ve AQD üçgenleri benzerdir; oran |AE| : |AD| = 1 : 3.','|EP| ÷ |DQ| = 1 ÷ 3 → |EP| = 6 ÷ 3 = 2'),STEP('|EF|’yi bul','Parçalar toplanır.','|EF| = |EP| + |PF| = 2 + 8 = 10')],
 puf='Paralel çizim yaparak yamuğu paralelkenar ve benzer üçgene ayırmak orantı kurmayı kolaylaştırır.',sekil=SK)

# ===== 10 · yardımcı çizim, alan · zor =====
kartla('K-GYK-10','Dört kenarı verilen yamuğun alanı','Yamuk, bir yan kenara paralel çizilerek paralelkenar ve kenarları bilinen üçgene ayrılır; üçgende yükseklik bulunur.','Yan kenarlardan birini yükseklik sanmak; taban farkını yükseklik yapmak; 2’ye bölmeyi unutmak.','zor',4,'ge-yk-alan','Yamuğun alanı')
a10,c10,l10,r10=6,20,13,15; d10=c10-a10; x10=(l10**2-r10**2+d10**2)/(2*d10); h10=sqrt(l10**2-x10**2); assert x10==5 and h10==12 and (a10+c10)/2*h10==156
assert 13*15==195 and d10*h10==168 and (a10+c10)/2*d10==182 and (a10+c10)*h10==312 and 156/2==78
s=.25; D=(0,0); C=(c10*s,0); A=(5*s,12*s); B_=(11*s,12*s)
assert abs(dist(A,D)/s-13)<1e-9 and abs(dist(B_,C)/s-15)<1e-9 and abs(alan([A,B_,C,D])/s**2-156)<1e-9
f=F(); f.poly([A,B_,C,D]); f.par(A,B_); f.par(D,C); ic=cen([A,B_,C,D])
f.sl('$6$',A,B_,ic,.3); f.sl('$20$',D,C,ic,.3); f.sl('$13$',A,D,ic,.4); f.sl('$15$',B_,C,ic,.4); vls(f,'ABCD',[A,B_,C,D])
SK=f.svg()
q('0010',tipId='ge-yk-alan',tip='Yamuğun alanı',z='zor',alt='Kenarları Verilen Yamuk',kaz='Dört kenarı verilen yamukta yardımcı paralel çizip yüksekliği bularak alanı hesaplar.',
 kart='K-GYK-10 (kenarları verilen yamuk) · AB = 6, DC = 20, AD = 13, BC = 15',
 metin='Şekildeki ABCD yamuğunda [AB] // [DC] dir ve kenar uzunlukları cm cinsinden verilmiştir. Şekil ölçekli değildir.\nBuna göre, ABCD yamuğunun alanı kaç cm² dir?',
 dogru=156,yan=[(168,'Yüksekliği 12 bulup tabanlar farkıyla çarpmış: 14 × 12.','bilgi'),(182,'Taban farkını (14) yükseklik sanıp ortalama tabanla çarpmış: 13 × 14.','bilgi'),(195,'Yan kenarları çarpıp 13 × 15 yazmış.','bilgi'),(312,'Tabanlar toplamını yükseklikle çarpıp 2’ye bölmeyi unutmuş.','islem')],
 istenen='Yamuğun alanı (cm²).',ip=['Yükseklik verilmemiş; yan kenarlardan birine paralel bir doğru çizip yamuğun içinde kenar uzunlukları bilinen bir üçgen elde etmeyi dene.'],bilgi=[YALAN,YPIS],
 ad=[STEP('Paralel çiz','B’den [AD]’ye paralel çizilip [DC]’yi E’de kessin; ABED paralelkenar olur.','|DE| = 6, |EB| = 13 → |EC| = 20 − 6 = 14'),STEP('Üçgenin kenarlarını yaz','EBC üçgeninin kenarları 13, 14 ve 15’tir; B’den [EC]’ye inilen dikmenin ayağı H olsun ve |EH| = t olsun.','13² − t² = 15² − (14 − t)²'),STEP('Yüksekliği bul','Denklemi çöz.','169 = 29 + 28t → t = 5 → h² = 169 − 25 = 144 → h = 12'),STEP('Alanı hesapla','Tabanlar 6 ve 20, yükseklik 12.','(6 + 20) ÷ 2 × 12 = 156')],
 puf='Kenarları bilinen ama yüksekliği verilmeyen şekillerde yan kenara paralel çizmek, bilinen kenarlı bir üçgen kurar.',sekil=SK)
bitir_geo('yamukiki','Yamuk')
