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
P=Parti('paralelkenar','Paralelkenar','geo|Paralelkenar',ders='TYT Geometri',idon='tytgeo')
PARA=B('Paralelkenarda açılar ve kenarlar','karşılıklı kenarlar paralel ve eşit, karşılıklı açılar eşittir; komşu açıların toplamı 180°’dir. Örnek: bir açısı 65° olan paralelkenarın komşu açısı 115°, karşısındaki açı 65°’dir')
PKOS=B('Paralelkenarda köşegenler','köşegenler birbirini ortalar: kesim noktası E ise |AE| = |EC| ve |BE| = |ED|. Bir köşegen paralelkenarı eş alanlı iki üçgene, iki köşegen dört eş alanlı üçgene böler. Örnek: |AE| = 7 ise |AC| = 14’tür')
PALAN=B('Paralelkenarın alanı','alan = taban × o tabana ait yükseklik. 45°–45°–90° üçgeninde hipotenüs, dik kenarın √2 katıdır. Örnek: dik kenar 3 ise hipotenüs 3√2’dir')
ORAN=B('Taban oranı ve alan oranı','yüksekliği ortak üçgenlerde alanlar tabanlarla orantılıdır. Bir köşegen paralelkenarı eş alanlı iki üçgene böler; köşegenlerin kesim noktası köşegenin orta noktasıdır. Örnek: yüksekliği ortak, tabanları 1 ve 3 olan üçgenlerin alanları 1 : 3 oranındadır')
PACIO=B('Paralelkenarda açıortay','bir köşedeki açının açıortayı karşı kenarı keserse iç ters açılar eşit olduğundan ikizkenar üçgen oluşur. Örnek: |AD| = 5 ise A’nın açıortayı [DC]’yi, D’den başlayarak |DE| = 5 olacak biçimde keser')
PIC=B('İçteki noktadan köşelere çizilen doğrular','paralelkenarın içindeki bir nokta dört köşeye birleştirilirse paralelkenar dört üçgene ayrılır; bu dört üçgenin alanları toplamı paralelkenarın alanına eşittir')
OTAD=B('Köşegenlerin kesim noktasından geçen doğru','paralelkenarın köşegenlerinin kesim noktasından geçen doğru, paralelkenarı iki eş parçaya ayırır ve kesim noktası bu doğrunun üzerinde kalan parçayı ortalar. Örnek: O noktası [KL]’nin orta noktasıysa |KL| = 2 × |OK|’dır; ayrıca |AK| = |CL| olur')
_A=A; _B=B
def pgram(w,d,h): A_=(0,0); B_=(w,0); D_=(d,h); C_=(w+d,h); return A_,B_,C_,D_

# ===== 01 · açılar · kolay =====
konu('geo|Paralelkenar','Paralelkenar')
kartla('K-GPK-01','Karşılıklı ve komşu açılar','Komşu açılar bütünlerdir; x bulunur, karşılıklı açı komşu açının bütünleri (ya da köşenin kendisi) olarak yazılır.','Komşu açıları eşit sanmak; x’i cevap sanmak; karşılıklı açıyı komşu açının bütünleri yerine kendisine eşitlemek.','kolay',3,'ge-pk-aci','Paralelkenarda açıları bulma')
x1=40; A1=2*x1-10; B1=x1+70; assert A1+B1==180 and (A1,B1)==(70,110)
assert 2*80-10==150 and 180-40==140
A,B,C,D=pgram(4.4,2.2*cos(radians(70)),2.2*sin(radians(70)))
assert abs(ang(A,B,D)-70)<1e-9 and abs(ang(B,A,C)-110)<1e-9 and abs(ang(C,B,D)-70)<1e-9
f=F(); f.poly([A,B,C,D]); f.par(A,B); f.par(D,C)
f.arc(A,B,D,.55,'$2x-10^\\circ$',1.35); f.arc(B,C,A,.45,'$x+70^\\circ$',1.15)
f.vl('A',A,(-1,-1),.3); f.vl('B',B,(1,-1),.3); f.vl('C',C,(1,1),.3); f.vl('D',D,(-1,1),.3)
SK1=f.svg(); A=_A; B=_B
q('0001',tipId='ge-pk-aci',tip='Paralelkenarda açıları bulma',z='kolay',alt='Karşılıklı ve Komşu Açılar',kaz='Paralelkenarda komşu açıların bütünler, karşılıklı açıların eşit olduğunu kullanarak açıyı bulur.',
 kart='K-GPK-01 (paralelkenarda açılar) · A = 2x − 10, B = x + 70',
 metin='ABCD paralelkenarında A ve B köşelerindeki iç açıların ölçüleri şekilde x cinsinden verilmiştir.\nŞekil ölçekli değildir.\nBuna göre, m(BCD) kaç derecedir?',
 dogru=70,yan=[(40,'x değerini bulup açı sanmış.','dikkat'),(110,'m(BCD) yerine komşu açıyı, B açısını (110°) yazmış.','dikkat'),(140,'180° − x işlemini yapıp 140° bulmuş.','islem'),(150,'A ile B açılarını eşitleyip x = 80 bulmuş: A = 150°, karşıdaki C de 150° çıkmış.','bilgi')],
 istenen='m(BCD) açısının ölçüsü (derece).',
 ip=['Komşu iki açı arasında nasıl bir bağıntı vardır? C köşesi hangi köşenin karşısındadır?'],
 bilgi=[PARA],
 ad=[A('x’i bul','A ve B komşu açılardır; toplamları 180°’dir.','(2x − 10) + (x + 70) = 180 → 3x = 120 → x = 40'),A('A açısını hesapla','x yerine 40 yazılır.','m(A) = 2 × 40 − 10 = 70°'),A('Karşılıklı açıyı yaz','C köşesi A’nın karşısındadır; karşılıklı açılar eşittir.','m(BCD) = m(A) = 70°')],
 puf='Paralelkenarda komşu açılar bütünler, karşılıklı açılar eşittir; önce x’i komşu açılardan bul.',sekil=SK1)

# ===== 02 · kenar ve çevre · kolay =====
kartla('K-GPK-02','Karşılıklı kenarlar ve çevre','Karşılıklı kenarlar eşit olduğundan x denklemden bulunur; çevre iki komşu kenarın toplamının iki katıdır.','Çevreyi yalnız iki kenar toplamı almak; karşılıklı kenarları farklı sanmak; x yerine kenar yazmak.','kolay',3,'ge-pk-cevre','Paralelkenarın çevresi')
x2=5; AB2=3*x2-2; DC2=x2+8; AD2=2*x2+1; assert AB2==DC2==13 and AD2==11 and 2*(AB2+AD2)==48 and 2*AD2==22 and AB2+AD2==24 and 2*AB2==26
A,B,C,D=pgram(4.4,1.0,2.2)
f=F(); f.poly([A,B,C,D]); f.par(A,B); f.par(D,C)
ic=cen([A,B,C,D]); f.sl('$3x-2$',A,B,ic,.3); f.sl('$x+8$',D,C,ic,.3); f.sl('$2x+1$',A,D,ic,.6)
f.vl('A',A,(-1,-1),.3); f.vl('B',B,(1,-1),.3); f.vl('C',C,(1,1),.3); f.vl('D',D,(-1,1),.3)
SK2=f.svg(); A=_A; B=_B
q('0002',tipId='ge-pk-cevre',tip='Paralelkenarın çevresi',z='kolay',alt='Kenarlar ve Çevre',kaz='Paralelkenarın karşılıklı kenarlarının eşitliğinden x’i bulup çevreyi hesaplar.',
 kart='K-GPK-02 (kenarlar ve çevre) · AB = 3x − 2, DC = x + 8, AD = 2x + 1',
 metin='Paralelkenar biçimli bir bahçenin etrafı, bir sıra tel çekilerek çevrilecektir. Bahçenin ABCD krokisinde kenar uzunlukları metre cinsinden x cinsinden verilmiştir.\nBuna göre, gereken tel uzunluğu kaç metredir?',
 dogru=48,yan=[(13,'Yalnız |AB| uzunluğunu bulup cevap yazmış.','dikkat'),(22,'Çevre olarak iki |AD| kenarının toplamını almış.','dikkat'),(24,'Yarı çevreyi (13 + 11) cevap sanmış.','dikkat'),(26,'Çevre olarak iki |AB| kenarının toplamını almış.','dikkat')],
 istenen='Bahçenin çevresi (m).',
 ip=['Karşılıklı kenarlar arasında nasıl bir ilişki var? Önce x’i bulmak için bunu kullan.'],
 bilgi=[PARA],
 ad=[A('x’i bul','Karşılıklı kenarlar eşittir: |AB| = |DC|.','3x − 2 = x + 8 → 2x = 10 → x = 5'),A('Kenarları hesapla','x yerine 5 yazılır.','|AB| = 13 · |AD| = 2 × 5 + 1 = 11'),A('Çevreyi yaz','Çevre, komşu iki kenarın toplamının iki katıdır.','2 × (13 + 11) = 48')],
 puf='Paralelkenarın çevresi 2 × (komşu iki kenar toplamı)’dır; x’i karşılıklı kenarların eşitliğinden bul.',sekil=SK2)

# ===== 03 · köşegenler · orta =====
kartla('K-GPK-03','Köşegenler birbirini ortalar','Köşegenler birbirini ortaladığından |AE| = |EC| denklemiyle x bulunur; iki köşegenin uzunluğu yarıların iki katıdır.','Yalnız yarım köşegenleri toplamak; BD’yi AC’ye eşit sanmak; iki köşegeni karıştırmak.','orta',4,'ge-pk-kosegen','Köşegenler birbirini ortalar')
x3=5; AE3=2*x3+1; EC3=3*x3-4; BE3=x3+3; assert AE3==EC3==11 and 2*AE3==22 and 2*BE3==16 and 22+16==38
assert AE3+BE3==19 and 22+BE3==30 and 22+22==44 and 2*38==76
A,B,C,D=pgram(4.6,1.0,2.4); E=mid(A,C); assert abs(dist(E,mid(B,D)))<1e-9
f=F(); f.poly([A,B,C,D]); f.line(A,C); f.line(B,D); f.par(A,B); f.par(D,C)
f.sl('$2x+1$',A,E,B,.3); f.sl('$3x-4$',E,C,B,.3); f.sl('$x+3$',B,E,A,.3)
f.vl('A',A,(-1,-1),.3); f.vl('B',B,(1,-1),.3); f.vl('C',C,(1,1),.3); f.vl('D',D,(-1,1),.3); f.node(add(E,(.0,-.25)),'$E$')
SK3=f.svg(); A=_A; B=_B
q('0003',tipId='ge-pk-kosegen',tip='Köşegenler birbirini ortalar',z='orta',alt='Köşegenler',kaz='Paralelkenarda köşegenlerin birbirini ortaladığını kullanarak x’i bulup köşegenlerin toplam uzunluğunu hesaplar.',
 kart='K-GPK-03 (köşegenler) · AE = 2x + 1, EC = 3x − 4, BE = x + 3',
 metin='Şekildeki ABCD paralelkenarında köşegenler E noktasında kesişmektedir ve parçaların uzunlukları cm cinsinden x cinsinden verilmiştir.\nBuna göre, |AC| + |BD| toplamı kaç cm’dir?',
 dogru=38,yan=[(19,'Yalnız yarım köşegenleri toplamış: |AE| + |BE| = 11 + 8.','dikkat'),(30,'|AC| = 22 ile yarım köşegen |BE| = 8’i toplamış.','dikkat'),(44,'|BD|’yi de |AC| gibi 22 almış.','bilgi'),(76,'İki köşegenin toplamını bulduktan sonra yarım parçaları da ekleyerek iki katına çıkarmış.','islem')],
 istenen='|AC| + |BD| toplamı (cm).',
 ip=['Köşegenler E noktasında nasıl bölünür? Önce hangi iki parçayı eşitleyerek x’i bulabilirsin?'],
 bilgi=[PKOS],
 ad=[A('x’i bul','Köşegenler birbirini ortalar: |AE| = |EC|.','2x + 1 = 3x − 4 → x = 5'),A('|AC|’yi bul','|AC|, iki yarım parçanın toplamıdır.','|AE| = 11 → |AC| = 22'),A('|BD|’yi bul','|BE| = x + 3 = 8 ve |BD| = 2 × |BE|.','|BD| = 16'),A('Toplamı yaz','İki köşegenin toplamı.','22 + 16 = 38')],
 puf='Paralelkenarda köşegenler birbirini ortaladığı için her köşegen kendi yarısının iki katıdır.',sekil=SK3)

# ===== 04 · alan · orta =====
kartla('K-GPK-04','Alan: taban × yükseklik','Yan kenar ve 45° açıdan ikizkenar dik üçgenle yükseklik bulunur; alan taban çarpı yüksekliktir.','Yan kenarı yükseklik sanmak; 30° kuralını 45°’ye uygulamak; alanı yarılamak.','orta',3,'ge-pk-alan','Paralelkenarın alanı')
s=.35; DC4=12; h4=6; AD4=6*sqrt(2); assert abs(AD4*sin(radians(45))-h4)<1e-9; al4=DC4*h4; assert al4==72
assert DC4*h4/2==36 and abs(DC4*AD4/2*sin(radians(45))*0+DC4*3*sqrt(2)-36*sqrt(2))<1e-9 and abs(DC4*AD4-72*sqrt(2))<1e-9 and DC4*DC4==144
assert 36<36*sqrt(2)<72<72*sqrt(2)<144
Dd=(0,0); Cd=(DC4*s,0); Ad=(h4*s,h4*s); Bd=add(Ad,(DC4*s,0))
assert abs(alan([Ad,Bd,Cd,Dd])/s**2-72)<1e-9 and abs(ang(Dd,Ad,Cd)-45)<1e-9 and abs(dist(Dd,Ad)/s-AD4)<1e-9
f=F(); f.poly([Ad,Bd,Cd,Dd]); f.par(Ad,Bd); f.par(Dd,Cd)
f.arc(Dd,Cd,Ad,.8,'$45^\\circ$',1.5)
ic=cen([Ad,Bd,Cd,Dd]); f.sl('$12$',Dd,Cd,ic,.3); f.sl('$6\\sqrt{2}$',Dd,Ad,ic,.4)
f.vl('A',Ad,(-1,1),.3); f.vl('B',Bd,(1,1),.3); f.vl('C',Cd,(1,-1),.3); f.vl('D',Dd,(-1,-1),.3)
SK4=f.svg(); A=_A; B=_B
q('0004',tipId='ge-pk-alan',tip='Paralelkenarın alanı',z='orta',alt='Paralelkenarın Alanı',kaz='Paralelkenarda 45° açıdan yüksekliği bulup alanı taban çarpı yükseklik ile hesaplar.',
 kart='K-GPK-04 (alan) · DC = 12, AD = 6√2, m(D) = 45°',
 metin='Bir kâğıt şeridinden kesilen ABCD paralelkenarının kenar uzunlukları cm cinsinden ve D köşesindeki açısı şekilde verilmiştir. Şekil ölçekli değildir.\nBuna göre, paralelkenarın alanı kaç cm²’dir?',
 dogru='72',sira=['36','36√2','72','72√2','144'],
 yan=[('36','Alanı yarılamış (üçgen alanı gibi): 12 × 6 ÷ 2.','bilgi'),('36√2','30° kuralını uygulayıp yüksekliği yan kenarın yarısı (3√2) almış: 12 × 3√2.','bilgi'),('72√2','Yükseklik yerine yan kenarı alıp 12 × 6√2 yazmış.','bilgi'),('144','Yüksekliği 12 bulmuş (yan kenarı √2 ile çarpmış): 12 × 12.','islem')],
 istenen='Paralelkenarın alanı (cm²).',
 ip=['Alan formülü için hangi tabana ait yüksekliğe ihtiyacın var? A köşesinden [DC]’ye indirilen dikme hangi özel dik üçgeni oluşturur?'],
 bilgi=[PALAN],
 ad=[A('Dik üçgeni kur','A’dan [DC]’ye dikme indirilir; D açısı 45° olan dik üçgen oluşur. Hipotenüs |AD| = 6√2 cm’dir.','45°–45°–90° üçgeni: hipotenüs = dik kenar × √2'),A('Yüksekliği bul','Dik kenar, hipotenüsün √2’ye bölümüdür.','h = 6√2 ÷ √2 = 6'),A('Alanı hesapla','Alan = taban × yükseklik.','12 × 6 = 72')],
 puf='Yan kenar ve aradaki açı verilince yükseklik, özel dik üçgenin kenar oranlarından bulunur; alan taban × yüksekliktir.',sekil=SK4)

# ===== 05 · alan oranı · orta =====
kartla('K-GPK-05','Köşegenle bölünen alanlar','Köşegen alanı ikiye böler; köşegenin orta noktasıyla ve taban oranıyla ardışık oranlar uygulanarak taralı üçgenin alanı bulunur.','Oranı ters kurmak; yalnız bir oranı uygulamak; köşegen yarısını atlamak.','orta',4,'ge-pk-alan','Paralelkenarın alanı')
S5=96; ABC5=S5/2; AFC5=ABC5*3/4; AEF5=AFC5/2; assert AEF5==18 and ABC5*1/4==12 and S5/4==24 and AFC5==36 and ABC5==48
w=4.4; d5=1.2; h5=2.6; A5,B5,C5,D5=pgram(w,d5,h5); E5=mid(A5,C5); F5=lerp(B5,C5,.25)
assert abs(alan([A5,E5,F5])/alan([A5,B5,C5,D5])-18/96)<1e-9
f=F(); f.fill([A5,E5,F5]); f.poly([A5,B5,C5,D5]); f.line(A5,C5); f.line(A5,F5); f.par(A5,B5); f.par(D5,C5)
f.sl('$a$',B5,F5,A5,.3); f.sl('$3a$',F5,C5,A5,.3)
f.vl('A',A5,(-1,-1),.3); f.vl('B',B5,(1,-1),.3); f.vl('C',C5,(1,1),.3); f.vl('D',D5,(-1,1),.3); f.vl('E',E5,(-1,.5),.3); f.vl('F',F5,(1,0),.3)
f.node((2.9,-.7),'Alan$(ABCD)=96\\ \\mathrm{cm}^2$')
SK5=f.svg(); A=_A; B=_B
q('0005',tipId='ge-pk-alan',tip='Paralelkenarın alanı',z='orta',alt='Köşegenle Bölünen Alanlar',kaz='Paralelkenarda köşegenin alanı ikiye böldüğünü ve taban oranlarını kullanarak taralı üçgenin alanını bulur.',
 kart='K-GPK-05 (köşegen ve alan oranı) · alan(ABCD) = 96, BF : FC = 1 : 3',
 metin='Şekildeki ABCD paralelkenarında E noktası köşegenlerin kesim noktası, F noktası ise [BC] üzerinde bir noktadır. |BF| = a ve |FC| = 3a dır.\nBuna göre, taralı AEF üçgeninin alanı kaç cm²’dir?',
 dogru=18,yan=[(12,'ABF üçgeninin alanını (48 × 1/4) bulup taralı alan sanmış.','dikkat'),(24,'ABE üçgeninin alanını (96 ÷ 4) taralı alan sanmış.','dikkat'),(36,'AFC üçgeninin alanını bulmuş, E’nin [AC]’yi ortaladığını (yarı almayı) unutmuş.','dikkat'),(48,'ABC üçgeninin alanını (96 ÷ 2) yazmış.','dikkat')],
 istenen='Taralı AEF üçgeninin alanı (cm²).',
 ip=['[AC] köşegeni paralelkenarı nasıl böler? AFC üçgeninin alanı ABC’nin hangi kesri? E noktası [AC] üzerinde nerededir?'],
 bilgi=[PKOS,ORAN],
 ad=[A('ABC üçgenini bul','Köşegen paralelkenarı eş iki üçgene böler.','alan(ABC) = 96 ÷ 2 = 48'),A('AFC üçgenini bul','ABC ve AFC üçgenlerinin A’dan inen yüksekliği ortaktır; tabanları |BC| ve |FC|’dir (|FC| = 3a, |BC| = 4a).','alan(AFC) = 48 × 3/4 = 36'),A('AEF üçgenini bul','E, [AC]’nin orta noktasıdır; AEF ve EFC üçgenlerinin F’den inen yüksekliği ortak, tabanları eşittir.','alan(AEF) = 36 ÷ 2 = 18')],
 puf='Alan sorularında önce köşegenle yarıya, sonra taban oranlarıyla ilgili parçaya in; her adımda ortak yükseklik ara.',sekil=SK5)

# ===== 06 · açıortay · zor =====
kartla('K-GPK-06','Açıortay ve ikizkenar üçgen','Paralelkenarda iki köşenin açıortayı karşı kenarda ikizkenar üçgenler oluşturur; kesişince parçaların toplamı taban uzunluğunu aşar.','Kesişmeyi görmeyip DE + CF toplamını EF sanmak; yan kenar yerine taban almak; EF yerine DE’yi yazmak.','zor',4,'ge-pk-aciortay','Açıortayların karşı kenarda ayırdığı parça')
AB6,AD6=12,9; EF6=2*AD6-AB6; assert EF6==6 and AB6-AD6==3 and AB6+AD6==21 and 2*AD6==18
s=.4; al=65; Ap=(0,0); Bp=(AB6*s,0); Dp=(AD6*s*cos(radians(al)),AD6*s*sin(radians(al))); Cp=add(Bp,Dp); hh=Dp[1]
ta=hh/sin(radians(al/2)); Ep=(ta*cos(radians(al/2)),hh); tb=hh/sin(radians((180-al)/2)); Fp=(Bp[0]+tb*cos(radians(180-(180-al)/2)),hh)
assert abs(dist(Dp,Ep)-AD6*s)<1e-9 and abs(dist(Cp,Fp)-AD6*s)<1e-9 and abs(dist(Ep,Fp)/s-6)<1e-9
f=F(); f.poly([Ap,Bp,Cp,Dp]); f.line(Ap,Ep); f.line(Bp,Fp); f.par(Ap,Bp); f.par(Dp,Cp)
f.arc(Ap,Bp,Ep,.55); f.arc(Ap,Ep,Dp,.55); f.arc(Bp,Fp,Ap,.55); f.arc(Bp,Cp,Fp,.55)
ic=cen([Ap,Bp,Cp,Dp]); f.sl('$12$',Ap,Bp,ic,.3); f.sl('$9$',Ap,Dp,ic,.3)
f.vl('A',Ap,(-1,-1),.3); f.vl('B',Bp,(1,-1),.3); f.vl('C',Cp,(1,1),.3); f.vl('D',Dp,(-1,1),.3); f.vl('E',Ep,(0,1),.3); f.vl('F',Fp,(0,1),.3)
SK6=f.svg(); A=_A; B=_B
q('0006',tipId='ge-pk-aciortay',tip='Açıortayların karşı kenarda ayırdığı parça',z='zor',alt='Paralelkenarda Açıortay',kaz='Paralelkenarda açıortayların oluşturduğu ikizkenar üçgenleri kullanarak karşı kenardaki parçanın uzunluğunu bulur.',
 kart='K-GPK-06 (açıortay) · AB = 12, AD = 9, A ve B açıortayları',
 metin='Şekildeki ABCD paralelkenarında [AE] ve [BF] sırasıyla A ve B köşelerindeki açıların açıortaylarıdır; E ve F noktaları [DC] kenarı üzerindedir. Kenar uzunlukları cm cinsindendir. Şekil ölçekli değildir.\nBuna göre, |EF| kaç cm’dir?',
 dogru=6,yan=[(9,'Yalnız |DE| = |AD| = 9’u bulup cevap yazmış.','dikkat'),(12,'|EF| yerine |DC| = |AB| = 12’yi yazmış.','dikkat'),(18,'|DE| + |CF| = 18’i |EF| sanmış; açıortaylar karşı kenarda kesişen parçalar oluşturur ve toplam |DC|’yi aşar.','dikkat'),(21,'|AB| + |AD| toplamını yazmış.','bilgi')],
 istenen='|EF| uzunluğu (cm).',
 ip=['[AE] açıortayı olduğunda hangi iki açı eşit olur? ADE üçgeni nasıl bir üçgendir? Aynı akıl yürütmeyi B köşesi için de yap.'],
 bilgi=[PACIO],
 ad=[A('|DE|’yi bul','[AB] // [DC] olduğundan m(EAB) = m(AED); [AE] açıortay olduğundan m(DAE) = m(EAB). ADE ikizkenardır.','|DE| = |AD| = 9'),A('|CF|’yi bul','Aynı biçimde B köşesinden: BCF ikizkenar üçgendir.','|CF| = |BC| = 9'),A('Noktaların yerini belirle','|DC| = 12 olduğundan |DF| = 12 − 9 = 3 ve |DE| = 9; E noktası F’nin sağındadır.','D — F — E — C sıralaması'),A('|EF|’yi hesapla','Parçalar kesişir.','|EF| = |DE| − |DF| = 9 − 3 = 6')],
 puf='Paralelkenarda açıortay karşı kenarı keserken ikizkenar üçgen oluşturur; iki açıortay kesişiyorsa |EF| = |DE| + |CF| − |DC| olur.',sekil=SK6)

# ===== 07 · içteki nokta · orta =====
kartla('K-GPK-07','İçteki noktanın oluşturduğu üçgenler','İçteki bir noktadan karşılıklı üçgen çiftlerinin alanları toplamı paralelkenar alanının yarısıdır; iki çiftten eşitlik kurulup bilinmeyen bulunur.','Karşılıklı üçgenleri eşit sanmak; dört alanı toplayıp cevap yazmak; paralelkenarın alanını sormak.','orta',3,'ge-pk-ic','İçteki noktanın oluşturduğu üçgenlerin alanları')
PAB,PBC,PCD=14,20,22; PAD=PAB+PCD-PBC; S7=2*(PAB+PCD); assert PAD==16 and S7==72 and PAB+PCD==36 and PAB+PBC+PCD==56 and PBC==20
w=4.8; d7=1.1; h7=3.0; A7,B7,C7,D7=pgram(w,d7,h7)
py=h7*PAB*2/S7  # PAB = w*py/2 , S = w*h
# PBC = 1/2*|d*py - h*(px-w)| = PBC/S * w*h
px=w-( (PBC/S7)*2*w*h7 - d7*py )/h7
P7=(px,py)
assert abs(alan([P7,A7,B7])/(w*h7)-PAB/S7)<1e-9 and abs(alan([P7,B7,C7])/(w*h7)-PBC/S7)<1e-9 and abs(alan([P7,C7,D7])/(w*h7)-PCD/S7)<1e-9 and abs(alan([P7,D7,A7])/(w*h7)-PAD/S7)<1e-9
f=F(); f.poly([A7,B7,C7,D7]); [f.line(P7,v) for v in (A7,B7,C7,D7)]; f.par(A7,B7); f.par(D7,C7); f.raw(f'\\fill {pt(P7)} circle (1.2pt);')
f.node(cen([P7,A7,B7]),'$14$'); f.node(cen([P7,B7,C7]),'$20$'); f.node(cen([P7,C7,D7]),'$22$'); f.node(cen([P7,D7,A7]),'$x$')
f.vl('A',A7,(-1,-1),.3); f.vl('B',B7,(1,-1),.3); f.vl('C',C7,(1,1),.3); f.vl('D',D7,(-1,1),.3); f.node(add(P7,(.0,.26)),'$P$')
SK7=f.svg(); A=_A; B=_B
q('0007',tipId='ge-pk-ic',tip='İçteki noktanın oluşturduğu üçgenlerin alanları',z='orta',alt='İçteki Nokta',kaz='Paralelkenar içindeki bir noktanın karşılıklı üçgen alanları toplamının eşitliğini kullanarak bilinmeyen alanı bulur.',
 kart='K-GPK-07 (içteki nokta) · PAB = 14, PBC = 20, PCD = 22',
 metin='Şekilde ABCD paralelkenarının içindeki P noktası köşelere birleştirilmiş, oluşan üçgenlerden üçünün alanı cm² cinsinden yazılmıştır. Alanı x ile gösterilen üçgen PAD üçgenidir. Şekil ölçekli değildir.\nBuna göre, x kaçtır?',
 dogru=16,yan=[(20,'Karşılıklı üçgenleri (PAD ve PBC) eşit alanlı sanmış: x = 20.','bilgi'),(36,'Karşılıklı çiftin toplamını (14 + 22) bulup x yerine yazmış.','dikkat'),(56,'Verilen üç alanı toplayıp cevap yazmış.','dikkat'),(72,'Dört üçgenin değil, paralelkenarın alanını (2 × 36) cevap sanmış.','dikkat')],
 istenen='x = alan(PAD) (cm²).',
 ip=['P noktasıyla karşılıklı iki kenardan oluşan üçgenlerin alanları toplamı paralelkenarın alanının kaçta kaçıdır? Aynı toplamı diğer çift için de yaz.'],
 bilgi=[PIC],
 ad=[A('İlk çifti topla','PAB ve PCD üçgenlerinin yükseklikleri toplamı paralelkenarın yüksekliğidir; alanları toplamı paralelkenar alanının yarısıdır.','14 + 22 = 36 = S ÷ 2'),A('İkinci çifte yaz','PAD ve PBC üçgenlerinin toplamı da S ÷ 2’dir.','x + 20 = 36'),A('x’i bul','Denklemi çöz.','x = 16')],
 puf='Paralelkenarın içindeki bir noktadan köşelere çizilen doğrularda karşılıklı üçgenlerin alanları toplamı daima paralelkenar alanının yarısıdır.',sekil=SK7)

# ===== 08 · orta noktadan geçen doğru · zor =====
kartla('K-GPK-08','Köşegen kesiminden geçen doğru','Kesim noktasından geçen doğru paralelkenarı iki eş parçaya ayırır; |CL| = |AK| ve |LK| = 2 · |OK| olur, bir parçanın çevresi bunlarla yazılır.','|LK| yerine |OK| kullanmak; KB yerine AK almak; paralelkenarın çevresini cevap sanmak.','zor',5,'ge-pk-kosegen','Köşegenler birbirini ortalar')
AB8,BC8,AK8,OK8=12,10,9,4; KB8=AB8-AK8; CL8=AK8; LK8=2*OK8; cev8=KB8+BC8+CL8+LK8; assert (KB8,CL8,LK8,cev8)==(3,9,8,30)
assert KB8+BC8+CL8==22 and KB8+BC8+CL8+OK8==26 and AK8+BC8+CL8+LK8==36 and 2*(AB8+BC8)==44
s=.28; A8=(0,0); B8=(12*s,0); D8=(6*s,8*s); C8=(18*s,8*s); O8=mid(A8,C8); K8=(9*s,0); L8=sub(mul(O8,2),K8)
assert abs(dist(A8,D8)/s-10)<1e-9 and abs(dist(B8,C8)/s-10)<1e-9 and abs(dist(O8,K8)/s-4)<1e-9 and abs(dist(A8,K8)/s-9)<1e-9 and abs(dist(C8,L8)/s-9)<1e-9 and abs(L8[1]-D8[1])<1e-9 and abs(dist(K8,L8)/s-8)<1e-9
Pq=[K8,B8,C8,L8]; assert abs(sum(dist(Pq[i],Pq[(i+1)%4]) for i in range(4))/s-30)<1e-9
f=F(); f.poly([A8,B8,C8,D8]); f.line(A8,C8); f.line(B8,D8); f.line(K8,L8); f.par(A8,B8); f.par(D8,C8)
f.sl('$9$',A8,K8,(2,1),.3); f.sl('$10$',B8,C8,(2,1),.3)
f.raw(f'\\draw[<->] ({A8[0]:.3f},{-.75:.3f}) -- ({B8[0]:.3f},{-.75:.3f});'); f.node((6*s,-1.0),'$12$')
f.node(add(mid(O8,K8),(-.23,0)),'$4$')
f.vl('A',A8,(-1,-1),.3); f.vl('B',B8,(1,-1),.3); f.vl('C',C8,(1,1),.3); f.vl('D',D8,(-1,1),.3); f.vl('K',K8,(0,-1),.3); f.vl('L',L8,(0,1),.3); f.node(add(O8,(.3,-.13)),'$O$')
SK8=f.svg(); A=_A; B=_B
q('0008',tipId='ge-pk-kosegen',tip='Köşegenler birbirini ortalar',z='zor',alt='Orta Noktadan Geçen Doğru',kaz='Paralelkenarın köşegenlerinin kesim noktasından geçen doğrunun eşit parçalar oluşturduğunu kullanarak bir parçanın çevresini hesaplar.',
 kart='K-GPK-08 (köşegen kesiminden geçen doğru) · AB = 12, BC = 10, AK = 9, OK = 4',
 metin='Şekildeki ABCD paralelkenarında köşegenler O noktasında kesişmektedir. O’dan geçen doğru, [AB] kenarını K noktasında, [DC] kenarını L noktasında kesmektedir. Uzunluklar cm cinsindendir. K ve L noktaları O noktasına göre simetriktir (O, [KL]’nin orta noktasıdır). Şekil ölçekli değildir.\nBuna göre, KBCL dörtgeninin çevresi kaç cm’dir?',
 dogru=30,yan=[(22,'|LK| kenarını çevreye katmayı unutmuş: 3 + 10 + 9.','dikkat'),(26,'|LK| yerine |OK| = 4’ü almış: 3 + 10 + 9 + 4.','bilgi'),(36,'|KB| yerine |AK| = 9’u yazmış: 9 + 10 + 9 + 8.','bilgi'),(44,'Paralelkenarın çevresini (2 × (12 + 10)) cevap sanmış.','dikkat')],
 istenen='KBCL dörtgeninin çevresi (cm).',
 ip=['O noktası köşegenlerin kesim noktası olduğuna göre [KL] doğru parçasının O ile ilişkisi nedir? |CL| ile |AK| arasında hangi ilişki kurulabilir?'],
 bilgi=[PKOS,OTAD],
 ad=[A('|KB|’yi bul','K noktası [AB] üzerindedir.','|KB| = 12 − 9 = 3'),A('|CL|’yi bul','AOK ve COL üçgenleri eştir (|AO| = |OC|, karşıt açılar ve iç ters açılar eşit); bu yüzden |CL| = |AK|.','|CL| = 9'),A('|LK|’yi bul','O noktası [KL]’nin orta noktasıdır.','|LK| = 2 × 4 = 8'),A('|BC|’yi yaz ve topla','Dörtgenin kenarları |KB|, |BC|, |CL|, |LK|’dir.','3 + 10 + 9 + 8 = 30')],
 puf='Paralelkenarın köşegenlerinin kesim noktasından geçen her doğru, iki eş parça oluşturur; bu yüzden |AK| = |CL| ve |OK| = |OL| olur.',sekil=SK8)
bitir_geo('paralelkenar','Paralelkenar')
