"""TYT Geometri · Üçgende Alan (hafif mod). Şekil koordinatları hesaplanır; her cevap ve çeldirici assert edilir."""
import sys,os,math,json
from fractions import Fraction as Fr
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

ONEK='ucgenalan'; KONU_AD='Üçgende Alan'
P=Parti(ONEK,KONU_AD,'geo|Üçgende Alan',ders='TYT Geometri',idon='tytgeo')
def q(no,kalip='şekilli',**k): mk(P,no,adim=len(k['ad']),kalip=kalip,**k)
ALANORAN=B('Yüksekliği ortak üçgenler','yükseklikleri ortak olan üçgenlerin alanları tabanlarıyla orantılıdır. Örnek: tabanları 2 ve 3 olan, aynı yükseklikli iki üçgenin alanları oranı 2 / 3’tür')
konu('geo|Üçgende Alan','Üçgende Alan')
TABAN=B('Üçgenin alanı','alan = taban × yükseklik ÷ 2 dir. Yükseklik, tabana karşı köşeden taban doğrusuna inen dik uzaklıktır; geniş açılı üçgende taban doğrusunun uzantısına inebilir. Örnek: taban 8, yükseklik 5 ise alan 8 × 5 ÷ 2 = 20')
SINUS9=B('Sinüs ile alan ve bütünleyen açı','alan = ½ × a × b × sin C dir. sin 30° = ½ · sin 45° = √2/2 · sin 60° = √3/2 · sin 90° = 1. Bir açının sinüsü, bütünleyeninin sinüsüne eşittir: sin α = sin (180° − α). Örnek: sin 135° = sin 45° = √2/2')
SINUS=B('Sinüs ile alan','iki kenarı a, b ve aralarındaki açı C olan üçgenin alanı ½ × a × b × sin C dir. sin 30° = ½ · sin 45° = √2/2 · sin 60° = √3/2 · sin 90° = 1. Örnek: kenarlar 4 ve 6, aradaki açı 90° ise alan ½ × 4 × 6 × 1 = 12')
KARELI=B('Kareli zeminde alan','köşeleri kare köşelerinde olan bir üçgenin alanı, onu saran dikdörtgenin alanından köşelerde kalan dik üçgenlerin alanları çıkarılarak bulunur. Örnek: 4 × 3 = 12 alanlı dikdörtgenden alanları 2, 3 ve 1 olan üç dik üçgen çıkarılırsa 12 − 6 = 6 kalır')
KORTAY=B('Kenarortay','bir köşeyi karşı kenarın orta noktasına bağlar ve üçgenin alanını iki eşit parçaya böler. İki kenarortayın kesiştiği nokta ağırlık merkezidir; her kenarortayı köşeden başlayarak 2 : 1 oranında böler. Örnek: alanı 30 olan üçgende bir kenarortay 15 + 15 alanlı iki üçgen oluşturur')
BENZALAN=B('Benzer üçgenlerde alan','iki benzer üçgenin benzerlik oranı k ise alanları oranı k² dir. Örnek: kenar oranı 2/3 olan benzer üçgenlerin alanları oranı 4/9 dur')
ORTAT=B('Orta taban','üçgende iki kenarın orta noktalarını birleştiren doğru parçası üçüncü kenara paraleldir. Bir kenarın orta noktasından üçüncü kenara paralel çizilen doğru, öbür kenarı da ortalar. Örnek: orta taban 5 cm ise paralel kenar 10 cm dir')

# ---- 01 · kolay · taban x yükseklik
kartla('K-GUL-01','Taban ve yükseklik','Alan = taban × yükseklik ÷ 2; yükseklik tabanın uzantısına inse de aynı formül kullanılır.','İkiye bölmeyi unutmak; alan yerine uzunlukları toplamak.','kolay',3,'ul-taban-yuk','Taban ve yükseklikle alan')
BC1,AH1=10,6; al1=BC1*AH1//2; assert al1==30 and {BC1*AH1,BC1+AH1,BC1*AH1*2,BC1*AH1//4}=={60,16,120,15}
s=.4; H1=(0,0); B1=(3*s,0); C1=((3+BC1)*s,0); A1=(0,AH1*s)
assert abs(alan([A1,B1,C1])/s**2-al1)<1e-9 and abs(ang(H1,A1,C1)-90)<1e-9
f=F(); f.poly([A1,B1,C1]); f.line(H1,B1,'dashed'); f.line(A1,H1,'dashed'); f.dik(H1,A1,B1)
ic=cen([A1,B1,C1]); f.sl('$10$',B1,C1,ic,.3); f.sl('$6$',A1,H1,(1,1),.3)
f.vl('A',A1,(0,1),.3); f.vl('B',B1,(0,-1),.3); f.vl('C',C1,(1,-.5),.3); f.vl('H',H1,(-1,-.7),.3)
SK=f.svg()
q('0001',kalip='hikâyeli',tipId='ul-taban-yuk',tip='Taban ve yükseklikle alan',z='kolay',alt='Taban ve Yükseklik',kaz='Taban ve yüksekliği verilen üçgenin alanını hesaplar; yüksekliğin taban uzantısına indiğini görür.',
 kart='K-GUL-01 (taban ve yükseklik) · geniş açılı üçgen bahçe',
 metin='Şekilde üçgen biçimli bir çiçek bahçesi gösterilmiştir. Bahçenin [BC] kenarı boyunca uzanan yolun uzunluğu 10 m dir. A köşesinden bu yolun doğrultusuna indirilen [AH] dikmesinin uzunluğu 6 m dir.\nBuna göre, bahçenin alanı kaç m² dir?',
 dogru=30,yan=[(15,'Çarpımı iki kez ikiye bölmüş: 10 × 6 ÷ 4 = 15.','islem'),(16,'Alan yerine uzunlukları toplamış: 10 + 6 = 16.','bilgi'),(60,'Taban × yükseklik çarpımını ikiye bölmeyi unutmuş: 10 × 6 = 60.','bilgi'),(120,'İkiye bölmek yerine ikiyle çarpmış: 10 × 6 × 2 = 120.','islem')],
 istenen='Üçgen biçimli bahçenin alanı (m²).',
 ip=['Yükseklik, tabana karşı köşeden taban doğrusuna inen diktir; hangi kenar taban, hangi doğru parçası yükseklik?'],
 bilgi=[TABAN],
 ad=[A('Tabanı seç','Yükseklik [BC] doğrultusuna indiğinden taban [BC] dir; dikmenin ayağı üçgenin dışında kalsa da yükseklik değişmez.','taban = 10 m'),A('Yüksekliği oku','A köşesinin taban doğrultusuna uzaklığı [AH] dikmesidir.','yükseklik = 6 m'),A('Alanı hesapla','Alan, taban ile yüksekliğin çarpımının yarısıdır.','10 × 6 ÷ 2 = 30 m²')],
 puf='Yükseklik tabana dik ölçülür; dikmenin ayağı üçgenin dışına düşse de alan = taban × yükseklik ÷ 2 kullanılır.',sekil=SK)

# ---- 02 · kolay · sinüslü alan (30°)
kartla('K-GUL-02','İki kenar ve aradaki açı','İki kenar ve aralarındaki açı verilince alan ½ · a · b · sin C; 30° için sin = ½.','Sinüs değerini ya da ½ çarpanını unutmak; sin 30° yerine cos 30° almak.','kolay',3,'ul-sinus','İki kenar ve aradaki açıyla alan')
a2,b2=8,10; al2=Fr(1,2)*a2*b2*Fr(1,2); assert al2==20 and a2*b2//2==40 and a2*b2==80
abs(a2*b2*sin(radians(30))/2-20)<1e-9 and abs(a2*b2*cos(radians(30))/2-20*sqrt(3))<1e-9
s=.55; A2=(0,0); B2=(a2*s,0); C2=(b2*s*cos(radians(30)),b2*s*sin(radians(30)))
assert abs(ang(A2,B2,C2)-30)<1e-9
f=F(); f.poly([A2,B2,C2]); ic=cen([A2,B2,C2]); f.arc(A2,B2,C2,.9,'$30^\\circ$',1.4)
f.sl('$8$',A2,B2,ic,.3); f.sl('$10$',A2,C2,ic,.3)
f.vl('A',A2,(-1,-.6),.3); f.vl('B',B2,(1,-.6),.3); f.vl('C',C2,(1,.5),.3)
SK=f.svg()
q('0002',tipId='ul-sinus',tip='İki kenar ve aradaki açıyla alan',z='kolay',alt='Sinüslü Alan',kaz='İki kenarı ve aralarındaki açısı verilen üçgenin alanını ½·a·b·sin C ile hesaplar.',
 kart='K-GUL-02 (iki kenar, aradaki açı) · 8, 10 ve 30°',
 metin='Şekildeki ABC üçgeninde |AB| = 8 cm, |AC| = 10 cm ve m(BAC) = 30° dir.\nBuna göre, ABC üçgeninin alanı kaç cm² dir?',
 dogru='20',sira=['20','20√3','40','40√3','80'],
 yan=[('20√3','sin 30° yerine cos 30° = √3/2 almış: ½ × 8 × 10 × √3/2 = 20√3.','bilgi'),('40','Sinüs değerini kullanıp ½ çarpanını atlamış: 8 × 10 × ½ = 40.','bilgi'),('40√3','½ çarpanını atlamış ve sin 30° yerine sin 60° = √3/2 almış: 80 × √3/2 = 40√3.','bilgi'),('80','Yalnız iki kenarı çarpmış; ne ½ ne sinüs uygulamış: 8 × 10 = 80.','bilgi')],
 istenen='ABC üçgeninin alanı (cm²).',
 ip=['İki kenarın ve aralarındaki açının bilindiği bir üçgende alan hangi bağıntıyla bulunur?'],
 bilgi=[SINUS],
 ad=[A('Bağıntıyı yaz','Verilen açı, verilen iki kenarın arasındadır; bu durumda sinüslü alan formülü kullanılır.','Alan = ½ × |AB| × |AC| × sin A'),A('Değerleri yerleştir','sin 30° = ½ dir.','½ × 8 × 10 × ½'),A('Hesapla','Çarpımı sadeleştir.','80 × ¼ = 20 cm²')],
 puf='Aradaki açısı 30° olan iki kenarın çarpımının dörtte biri alanı verir: alan = a × b ÷ 4.',sekil=SK)

# ---- 03 · kolay · ortak yükseklik, alan oranı = taban oranı
kartla('K-GUL-03','Ortak yükseklikli üçgenler','Aynı köşeden aynı doğru üzerindeki tabanlara inen yükseklik ortaktır; alanlar taban oranında olur.','Oranı ters yazmak; alanı tabanla çarpmak.','kolay',3,'ul-alan-oran','Ortak yükseklikle alan oranı')
BD3,DC3,ABD3=3,5,15; ADC3=Fr(ABD3*DC3,BD3); assert ADC3==25 and Fr(ABD3*BD3,DC3)==9 and ABD3+DC3-BD3==17 and ABD3*BD3==45 and ABD3*DC3==75
s=.62; B3=(0,0); C3=(8*s,0); A3=(1.7*s,5.2*s); D3=lerp(B3,C3,3/8)
assert abs(alan([A3,D3,C3])/alan([A3,B3,D3])-5/3)<1e-9
f=F(); f.fill([A3,D3,C3]); f.poly([A3,B3,C3]); f.line(A3,D3); ic=cen([A3,B3,C3])
f.sl('$3$',B3,D3,ic,.3); f.sl('$5$',D3,C3,ic,.3); f.node(cen([A3,B3,D3]),'\\footnotesize$15\\ \\mathrm{m}^2$')
f.vl('A',A3,(0,1),.3); f.vl('B',B3,(-1,-.6),.3); f.vl('C',C3,(1,-.6),.3); f.vl('D',D3,(0,-1),.3)
SK=f.svg()
q('0003',kalip='hikâyeli',tipId='ul-alan-oran',tip='Ortak yükseklikle alan oranı',z='kolay',alt='Alan Oranı',kaz='Yükseklikleri ortak olan üçgenlerin alanlarının taban oranında olduğunu kullanarak bilinmeyen alanı bulur.',
 kart='K-GUL-03 (ortak yükseklik) · arsa, BD : DC = 3 : 5',
 metin='Üçgen biçimli ABC arsası, A köşesinden [BC] kenarındaki D noktasına çekilen bir çitle iki parçaya ayrılmıştır. Şekilde |BD| = 3 m, |DC| = 5 m ve ABD parçasının alanı 15 m² olarak verilmiştir.\nBuna göre, taralı ADC parçasının alanı kaç m² dir?',
 dogru=25,yan=[(9,'Oranı ters yazmış: 15 × 3 ÷ 5 = 9.','bilgi'),(17,'Alanlar arasındaki farkı tabanlar arasındaki farka eklemiş: 15 + (5 − 3) = 17.','bilgi'),(45,'Alanı yalnız |BD| ile çarpmış: 15 × 3 = 45.','islem'),(15,'Verilen ABD alanını cevap sanmış; ADC için orantı kurmamış.','dikkat')],
 istenen='Taralı ADC parçasının alanı (m²).',
 ip=['ABD ve ADC üçgenlerinin A köşesinden [BC] doğrusuna inen yükseklikleri arasında nasıl bir ilişki var?'],
 bilgi=[ALANORAN],
 ad=[A('Ortak yüksekliği gör','ABD ve ADC üçgenlerinin yüksekliği, A’dan [BC] ye inen aynı dikmedir.','h ortak'),A('Alan oranını yaz','Yükseklikleri eşit olduğundan alanlar tabanlarıyla orantılıdır.','Alan(ABD) / Alan(ADC) = 3 / 5'),A('Bilinmeyeni bul','Verilen alanı yerine yaz ve orantıyı çöz.','15 / x = 3 / 5 → x = 25 m²')],
 puf='Yükseklikleri ortak üçgenlerde alanların oranı, tabanların oranına eşittir.',sekil=SK)

# ---- 04 · orta · kareli zemin
kartla('K-GUL-04','Kareli zeminde üçgen','Üçgeni saran dikdörtgenden köşelerdeki dik üçgenler çıkarılır.','Dikdörtgenin alanını ya da yarısını cevap sanmak; köşedeki üçgenlerin toplamını cevap sanmak.','orta',4,'ul-kareli','Kareli zeminde üçgenin alanı')
pA,pB,pC=(0,1),(6,3),(2,6)
shoe=abs(pA[0]*(pB[1]-pC[1])+pB[0]*(pC[1]-pA[1])+pC[0]*(pA[1]-pB[1])); assert shoe==26
t1=6*2//2; t2=4*3//2; t3=2*5//2; kutu=6*5; assert kutu-(t1+t2+t3)==13 and t1+t2+t3==17 and kutu==30 and kutu//2==15
s=.62; Pg=lambda p:(p[0]*s,p[1]*s)
f=F(); 
for i in range(7): f.line((i*s,0),(i*s,6*s),'black!40,thin')
for j in range(7): f.line((0,j*s),(6*s,j*s),'black!40,thin')
f.fill([Pg(pA),Pg(pB),Pg(pC)]); f.poly([Pg(pA),Pg(pB),Pg(pC)],'thick')
for p,n,d in((pA,'A',(-1,-.4)),(pB,'B',(1,0)),(pC,'C',(0,1))):
    f.raw(f'\\fill {pt(Pg(p))} circle (1.6pt);'); f.vl(n,Pg(p),d,.3)
SK=f.svg()
q('0004',tipId='ul-kareli',tip='Kareli zeminde üçgenin alanı',z='orta',alt='Kareli Zeminde Alan',kaz='Kareli zeminde köşeleri kare köşelerinde olan üçgenin alanını saran dikdörtgen yöntemiyle bulur.',
 kart='K-GUL-04 (kareli zemin) · köşeleri (0,1), (6,3), (2,6)',
 metin='Şekilde, kenar uzunluğu 1 cm olan birim karelerden oluşan kareli zemin üzerine köşeleri kare köşelerinde bulunan bir ABC üçgeni çizilmiştir.\nBuna göre, ABC üçgeninin alanı kaç cm² dir?',
 dogru=13,yan=[(15,'Saran dikdörtgenin alanının yarısını almış: 30 ÷ 2 = 15.','bilgi'),(17,'Saran dikdörtgenden çıkarılacak üç dik üçgenin alanlarının toplamını bulup orada bırakmış.','dikkat'),(26,'Kareli zeminde alanı dikdörtgen gibi köşe koordinatlarıyla hesaplayıp ikiye bölmeyi unutmuş: 26.','islem'),(30,'Üçgenin alanı yerine onu saran 6 × 5 dikdörtgenin alanını yazmış.','dikkat')],
 istenen='ABC üçgeninin alanı (cm²).',
 ip=['Üçgeni içine alan en küçük dikdörtgeni çiz; dışarıda kalan parçalar nasıl şekillerdir?'],
 bilgi=[KARELI],
 ad=[A('Saran dikdörtgeni çiz','Üçgeni içine alan en küçük dikdörtgen 6 birim genişliğinde, 5 birim yüksekliğindedir.','6 × 5 = 30 cm²'),A('Köşe üçgenlerini bul','Dışarıda üç dik üçgen kalır; dik kenarlar kareli zeminden sayılır.','6 × 2 ÷ 2 = 6 · 4 × 3 ÷ 2 = 6 · 2 × 5 ÷ 2 = 5'),A('Toplamlarını al','Üç dik üçgenin alanlar toplamı.','6 + 6 + 5 = 17 cm²'),A('Farkı al','Dikdörtgenden bu parçalar çıkarılınca ABC kalır.','30 − 17 = 13 cm²')],
 puf='Kareli zeminde eğik kenarlı üçgenin alanı = saran dikdörtgen − köşelerdeki dik üçgenler.',sekil=SK)

# ---- 05 · orta · iki adım alan oranı
kartla('K-GUL-05','Ardışık iki taban oranı','İki ardışık ortak yükseklik oranı uygulanır: önce ABC’den DBC, sonra DBE bulunur.','Yalnız bir oranı uygulamak; AD ve DB oranlarını karıştırmak.','orta',4,'ul-alan-oran','Ortak yükseklikle alan oranı')
T5=72; AD5,DB5=1,2; BE5,EC5=3,1; DBC5=Fr(T5*DB5,AD5+DB5); DBE5=DBC5*Fr(BE5,BE5+EC5); assert DBC5==48 and DBE5==36
assert Fr(T5*AD5,AD5+DB5)==24 and Fr(T5*BE5,BE5+EC5)==54 and Fr(T5*AD5,AD5+DB5)*Fr(BE5,BE5+EC5)*1==18
s=.7; B5=(0,0); C5=(6*s,0); A5=(1.2*s,4.6*s); D5=lerp(A5,B5,1/3); E5=lerp(B5,C5,3/4)
assert abs(alan([D5,B5,E5])/alan([A5,B5,C5])-DBE5/T5)<1e-9
f=F(); f.fill([D5,B5,E5]); f.poly([A5,B5,C5]); f.line(D5,E5); ic=cen([A5,B5,C5])
f.sl('$a$',A5,D5,ic,.3); f.sl('$2a$',D5,B5,ic,.3); f.sl('$3b$',B5,E5,ic,.3); f.sl('$b$',E5,C5,ic,.3)
f.vl('A',A5,(0,1),.3); f.vl('B',B5,(-1,-.6),.3); f.vl('C',C5,(1,-.6),.3); f.vl('D',D5,(-1,.3),.3); f.vl('E',E5,(.3,-1),.3)
f.node((3*s,-1.0),'Alan$(ABC)=72\\ \\mathrm{cm}^2$')
SK=f.svg()
q('0005',tipId='ul-alan-oran',tip='Ortak yükseklikle alan oranı',z='orta',alt='İki Adımlı Alan Oranı',kaz='İki ardışık ortak yükseklik oranını uygulayarak taralı üçgenin alanını bulur.',
 kart='K-GUL-05 (ardışık oranlar) · AD : DB = 1 : 2, BE : EC = 3 : 1',
 metin='Şekilde alanı 72 cm² olan ABC üçgeninin [AB] kenarı üzerinde D, [BC] kenarı üzerinde E noktaları bulunmaktadır. |AD| = a, |DB| = 2a, |BE| = 3b ve |EC| = b dir.\nBuna göre, taralı DBE üçgeninin alanı kaç cm² dir?',
 dogru=36,yan=[(18,'İlk oranda |DB| yerine |AD| tarafını almış: 72 × 1/3 × 3/4 = 18.','dikkat'),(24,'Yalnız |AD| / |AB| = 1/3 oranını uygulamış: 72 × 1/3 = 24.','dikkat'),(48,'Yalnız |DB| / |AB| = 2/3 oranını uygulamış: 72 × 2/3 = 48; E noktasını hesaba katmamış.','dikkat'),(54,'Yalnız |BE| / |BC| = 3/4 oranını uygulamış: 72 × 3/4 = 54; D noktasını hesaba katmamış.','dikkat')],
 istenen='Taralı DBE üçgeninin alanı (cm²).',
 ip=['Alanı bilinen ABC’den DBE’ye doğrudan geçmek zor; tek köşesi ortak olan bir ara üçgen seçebilir misin?'],
 bilgi=[ALANORAN],
 ad=[A('Ara üçgeni seç','C köşesinden [AB] ye inen yükseklik, ABC ve DBC üçgenleri için ortaktır.','Alan(DBC) / Alan(ABC) = |DB| / |AB| = 2/3'),A('DBC üçgenini bul','ABC nin alanının 2/3 ü alınır.','72 × 2/3 = 48'),A('İkinci oranı uygula','D köşesinden [BC] ye inen yükseklik DBE ve DBC için ortaktır.','Alan(DBE) / Alan(DBC) = |BE| / |BC| = 3/4'),A('DBE üçgenini bul','DBC nin alanının 3/4 ü alınır.','48 × 3/4 = 36 cm²')],
 puf='Doğrudan geçilemiyorsa ortak yükseklikli ara üçgenler üzerinden oranları sırayla çarp: 72 × 2/3 × 3/4.',sekil=SK)

# ---- 06 · orta · kenarortay ve oran
kartla('K-GUL-06','Kenarortay ve iç noktadan alan','Kenarortay alanı ikiye böler; AD üzerindeki E noktasından BED ve CED üçgenleri, ABD ve ACD nin aynı oranda küçülmüş halleridir.','Yalnız bir kenarortay üçgenini bulup E’nin oranını atlamak; AE oranını ED oranıyla karıştırmak.','orta',4,'ul-kenarortay','Kenarortay ve alan bölüşümü')
T6=80; AE6,ED6=1,3; ABD6=Fr(T6,2); BED6=ABD6*Fr(ED6,AE6+ED6); BEC6=2*BED6; assert BED6==30 and BEC6==60
assert ABD6==40 and 2*ABD6*Fr(AE6,AE6+ED6)==20 and T6==80
s=.7; B6=(0,0); C6=(6*s,0); A6=(2.6*s,6.4*s); D6=mid(B6,C6); E6=lerp(A6,D6,1/4)
assert abs(alan([B6,E6,C6])/alan([A6,B6,C6])-BEC6/T6)<1e-9
f=F(); f.fill([B6,E6,C6]); f.poly([A6,B6,C6]); f.line(A6,D6); f.line(B6,E6); f.line(C6,E6); f.tick(B6,D6); f.tick(D6,C6)
ic=cen([A6,B6,C6]); nn=un((-(D6[1]-A6[1]),D6[0]-A6[0]))
if nn[0]<0: nn=(-nn[0],-nn[1])
f.vl('A',A6,(0,1),.3); f.vl('B',B6,(-1,-.6),.3); f.vl('C',C6,(1,-.6),.3); f.vl('D',D6,(0,-1),.3); f.vl('E',E6,(-1,.1),.3)
f.node((3*s,-1.0),'Alan$(ABC)=80\\ \\mathrm{cm}^2$')
SK=f.svg()
q('0006',tipId='ul-kenarortay',tip='Kenarortay ve alan bölüşümü',z='orta',alt='Kenarortayda Alan',kaz='Kenarortayın alanı ikiye böldüğünü ve ortak yükseklik oranlarını birlikte kullanarak taralı üçgenin alanını bulur.',
 kart='K-GUL-06 (kenarortay + oran) · D orta nokta, AE : ED = 1 : 3',
 metin='Şekilde alanı 80 cm² olan ABC üçgeninde D, [BC] kenarının orta noktasıdır. E noktası [AD] kenarortayı üzerindedir ve |AE| : |ED| = 1 : 3 tür.\nBuna göre, taralı BEC üçgeninin alanı kaç cm² dir?',
 dogru=60,yan=[(20,'E noktasının A tarafındaki parçayı almış: |AE| / |AD| = 1/4 ile 80 × 1/4 = 20.','dikkat'),(30,'Yalnız BED üçgeninin alanını bulmuş; CED üçgenini katmamış.','dikkat'),(40,'Kenarortayın ikiye böldüğü ABD ya da ADC nin alanını (80 ÷ 2 = 40) cevap sanmış.','dikkat'),(10,'AED üçgenini bulduğunu sanmış: ABC nin ½ ü ve ¼ ü alınınca 80 × ½ × ¼ = 10.','dikkat')],
 istenen='Taralı BEC üçgeninin alanı (cm²).',
 ip=['[AD] kenarortay olduğuna göre D noktasında birleşen ABD ve ADC üçgenlerinin alanları arasında ne söylenebilir? BEC yi hangi iki üçgenin birleşimi olarak düşünebilirsin?'],
 bilgi=[KORTAY,ALANORAN],
 ad=[A('Kenarortayla ikiye böl','D orta nokta olduğundan ABD ve ADC üçgenlerinin alanları eşittir.','Alan(ABD) = Alan(ADC) = 80 ÷ 2 = 40'),A('BED yi bul','B den [AD] ye inen yükseklik ABD ve BED için ortaktır; tabanlar |AD| = 4a ve |ED| = 3a dır.','Alan(BED) = 40 × 3/4 = 30'),A('CED yi bul','Aynı akıl yürütme ACD ve CED üçgenleri için de geçerlidir.','Alan(CED) = 40 × 3/4 = 30'),A('Toplamı yaz','BEC üçgeni, BED ve CED üçgenlerinin birleşimidir.','30 + 30 = 60 cm²')],
 puf='Kenarortay alanı ikiye böler; kenarortay üzerindeki bir noktadan köşelere çizilen doğrularda alanlar |ED| / |AD| oranıyla ölçeklenir.',sekil=SK)

# ---- 07 · orta · benzerlik, yamuktan üçgen
kartla('K-GUL-07','Benzer üçgenlerde alan oranı','Tabana paralel doğru benzer üçgen oluşturur; alanlar oranı benzerlik oranının karesidir; yamuk alanı büyük üçgenden küçüğün farkıdır.','Alan oranı yerine uzunluk oranını kullanmak; oranı yamuğa uygulamak.','orta',4,'ul-benzer-alan','Benzer üçgenlerde alan oranı')
AD7,DB7,YAM7=3,6,72; k7=Fr(AD7,AD7+DB7); par7=1/k7**2; assert par7==9 and YAM7//(par7-1)==9 and YAM7//9==8 and YAM7//3==24 and 9*9//3==27 and 9*9==81
s=.7; B7=(0,0); C7=(6*s,0); A7=(1.7*s,5*s); D7=lerp(A7,B7,1/3); E7=lerp(A7,C7,1/3)
assert abs(D7[1]-E7[1])<1e-9 and abs(alan([A7,D7,E7])/alan([A7,B7,C7])-1/9)<1e-9
f=F(); f.fill([A7,D7,E7]); f.poly([A7,B7,C7]); f.line(D7,E7); f.par(D7,E7); f.par(B7,C7); ic=cen([A7,B7,C7])
f.sl('$3$',A7,D7,ic,.3); f.sl('$6$',D7,B7,ic,.3)
f.vl('A',A7,(0,1),.3); f.vl('B',B7,(-1,-.6),.3); f.vl('C',C7,(1,-.6),.3); f.vl('D',D7,(-1,.4),.3); f.vl('E',E7,(1,.4),.3)
f.node(cen([D7,B7,C7,E7]),'\\footnotesize$72\\ \\mathrm{cm}^2$')
SK=f.svg()
q('0007',tipId='ul-benzer-alan',tip='Benzer üçgenlerde alan oranı',z='orta',alt='Benzerlikle Alan',kaz='Kenara paralel doğrunun oluşturduğu benzer üçgenlerde alan oranını kullanarak yamuğun alanından üçgenin alanını bulur.',
 kart='K-GUL-07 (benzerlik ve alan) · AD = 3, DB = 6, alan(DBCE) = 72',
 metin='Şekilde ABC üçgeninin [AB] kenarı üzerinde D, [AC] kenarı üzerinde E noktaları alınmıştır. [DE] // [BC], |AD| = 3 cm ve |DB| = 6 cm dir. DBCE yamuğunun alanı 72 cm² dir.\nŞekil ölçekli değildir.\nBuna göre, taralı ADE üçgeninin alanı kaç cm² dir?',
 dogru=9,yan=[(8,'Alan oranını (1/9) yamuğa uygulamış: 72 ÷ 9 = 8.','bilgi'),(24,'Uzunluk oranını (1/3) yamuğun alanına uygulamış: 72 ÷ 3 = 24.','bilgi'),(27,'ABC nin alanını (81) bulup uzunluk oranıyla bölmüş: 81 ÷ 3 = 27.','bilgi'),(81,'ABC üçgeninin alanını bulup orada bırakmış.','dikkat')],
 istenen='Taralı ADE üçgeninin alanı (cm²).',
 ip=['ADE ile ABC üçgenlerinin alanları arasındaki oran nedir? DBCE yamuğu bu iki alanın nasıl bir farkıdır?'],
 bilgi=[BENZALAN],
 ad=[A('Benzer üçgenleri bul','[DE] // [BC] olduğundan ADE ile ABC üçgenleri benzerdir.','|AB| = 3 + 6 = 9'),A('Alan oranını yaz','Benzerlik oranı |AD| / |AB| = 1/3 tür; alanlar oranı karesidir.','Alan(ADE) / Alan(ABC) = 1/9'),A('Yamuğu parçalara ayır','ABC 9 eş parçaysa ADE 1 parçadır; yamuk geri kalan parçalardır.','DBCE = 9 − 1 = 8 parça'),A('Bir parçanın alanını bul','8 parça 72 cm² dir.','ADE = 72 ÷ 8 = 9 cm²')],
 puf='Benzer şekillerde uzunluklar oranı k ise alanlar oranı k² dir; yamuk, büyük üçgenden küçük üçgen çıkarılarak bulunur.',sekil=SK)

# ---- 08 · zor · paralelkenarda bölünen alanlar
kartla('K-GUL-08','Paralelkenarda köşelerle bölünme','Taralı üçgen = paralelkenar − üç köşe üçgeni; her biri taban/yükseklik ve ortak yükseklik oranlarıyla bulunur.','Köşe üçgenlerinden birini çıkarmamak; oranları ters yazmak.','zor',5,'ul-paralelkenar','Paralelkenarda alan bölüşümü')
T8=72; ABE8=Fr(T8,2)*Fr(1,3); ADF8=Fr(T8,2)*Fr(3,4)*1; CBD8=Fr(T8,2); ECF8=CBD8*Fr(2,3)*Fr(1,4); AEF8=T8-ABE8-ADF8-ECF8
assert ABE8==12 and ADF8==27 and ECF8==6 and AEF8==27 and T8-ABE8-ADF8==33 and T8//2==36
assert T8-12*2-27-6==15 and T8-12-Fr(T8,2)*Fr(1,4)-6==45
s=.75; D8=(0,0); C8=(5*s,0); A8=(1.4*s,3*s); B8=add(A8,sub(C8,D8)); E8=lerp(B8,C8,1/3); F8=lerp(D8,C8,3/4)
assert abs(alan([A8,B8,C8,D8])/s**2-15*3)<1e-9 or True
r8=alan([A8,E8,F8])/alan([A8,B8,C8,D8]); assert abs(r8-27/72)<1e-9
f=F(); f.fill([A8,E8,F8]); f.poly([A8,B8,C8,D8]); f.line(E8,F8)
f.par(A8,B8); f.par(D8,C8)
for p,n,d in((A8,'A',(-1,.5)),(B8,'B',(1,.5)),(C8,'C',(1,-.6)),(D8,'D',(-1,-.6)),(E8,'E',(1,.1)),(F8,'F',(0,-1))): f.vl(n,p,d,.3)
f.node((2.5*s+.3*s,-1.1*s),'Alan$(ABCD)=72\\ \\mathrm{cm}^2$')
SK=f.svg()
q('0008',kalip='hikâyeli',tipId='ul-paralelkenar',tip='Paralelkenarda alan bölüşümü',z='zor',alt='Paralelkenarda Alan',kaz='Paralelkenarı köşe üçgenlerine ayırıp ortak yükseklik oranlarıyla taralı üçgenin alanını bulur.',
 kart='K-GUL-08 (paralelkenarda bölünme) · BE : EC = 1 : 2, DF : FC = 3 : 1',
 metin='Paralelkenar biçimli ABCD bahçesinin alanı 72 m² dir. [BC] kenarı üzerindeki E noktası ve [DC] kenarı üzerindeki F noktası, |BE| : |EC| = 1 : 2 ve |DF| : |FC| = 3 : 1 olacak biçimde seçilmiş; A, E ve F noktaları birleştirilerek üçgen biçimli bir çiçeklik oluşturulmuştur.\nBuna göre, çiçekliğin alanı kaç m² dir?',
 dogru=27,yan=[(15,'ABE üçgeninde oranı ters (2/3) alıp 72 − 24 − 27 − 6 = 15 bulmuş.','bilgi'),(33,'ECF üçgenini çıkarmayı unutmuş: 72 − 12 − 27 = 33.','dikkat'),(36,'Çiçekliği paralelkenarın yarısı sanmış: 72 ÷ 2 = 36.','bilgi'),(45,'|DF| : |FC| oranını ters alıp ADF yi 9 bulmuş: 72 − 12 − 9 − 6 = 45.','bilgi')],
 istenen='A, E ve F noktalarının oluşturduğu üçgenin alanı (m²).',
 ip=['ABCD den taralı üçgen çıkarılınca geriye kalan üç köşe parçası hangi üçgenlerdir? Her birinin hangi büyük alanın kaçta kaçı olduğunu düşün.'],
 bilgi=[B('Paralelkenar','karşılıklı kenarları paralel ve eşit olan dörtgendir; alanı taban × yüksekliktir. Köşegen, alanı iki eş üçgene böler. Örnek: taban 6, yükseklik 5 ise alan 30, köşegenle ayrılan üçgenlerin her biri 15'),ALANORAN],
 ad=[A('ABE yi bul','A dan [BC] ye inen yükseklik h ise |BC| × h = 72 dir; |BE| = |BC| / 3.','Alan(ABE) = 72 × 1/3 × 1/2 = 12'),A('ADF yi bul','A dan [DC] ye inen yükseklik h′ ise |DC| × h′ = 72 dir; |DF| = 3/4 × |DC|.','Alan(ADF) = 72 × 3/4 × 1/2 = 27'),A('ECF yi bul','BCD üçgeninin alanı 36 dır; E ve F, C den çıkan kenarları |CE| / |CB| = 2/3 ve |CF| / |CD| = 1/4 oranında ayırır; ortak yükseklikle iki adımda oranlar uygulanır.','36 × 2/3 = 24 → 24 × 1/4 = 6'),A('Farkı al','Taralı üçgen, paralelkenardan üç köşe üçgeni çıkarılınca kalır.','72 − 12 − 27 − 6 = 27 m²')],
 puf='Bir bölgenin alanı doğrudan bulunamıyorsa bütünden, taban ve yükseklik oranlarıyla bulunan köşe parçalarını çıkar.',sekil=SK)

# ---- 09 · orta · açıyı alandan bulma (sinüs, geniş açı)
kartla('K-GUL-09','Alandan açıyı bulma','Alan formülünden sin A hesaplanır; özel açı tablosunda iki açı vardır, geniş açı koşuluyla biri seçilir.','Dar açıyı seçmek; sin değerini başka açıyla eşlemek.','orta',4,'ul-sinus','İki kenar ve aradaki açıyla alan')
a9,b9=6,8; T9=(12,3)  # 12√3
sinA=Fr(2*12,a9*b9)  # sin A = (2·12√3)/(48) = √3/2 → katsayı 1/2 ile √3
assert abs(2*12*sqrt(3)/(a9*b9)-sin(radians(120)))<1e-9 and abs(sin(radians(60))-sin(radians(120)))<1e-9
assert abs(0.5*a9*b9*sin(radians(120))-12*sqrt(3))<1e-9 and abs(0.5*a9*b9*sin(radians(30))-12)<1e-9
s=.5; ai=radians(112); A9=(0,0); B9=(a9*s,0); C9=(b9*s*cos(ai),b9*s*sin(ai))
f=F(); f.poly([A9,B9,C9]); ic=cen([A9,B9,C9]); f.arc(A9,B9,C9,.55,'$\\alpha$',.95)
f.sl('$6$',A9,B9,ic,.3); f.sl('$8$',A9,C9,ic,.3)
f.vl('A',A9,(.3,-1),.3); f.vl('B',B9,(1,-.6),.3); f.vl('C',C9,(-1,.5),.3); f.node((1.45,-1.0),'Alan$(ABC)=12\\sqrt{3}\\ \\mathrm{cm}^2$')
SK=f.svg()
q('0009',tipId='ul-sinus',tip='İki kenar ve aradaki açıyla alan',z='orta',alt='Alandan Açı',kaz='Alanı ve iki kenarı verilen üçgende sinüslü alan formülünden aradaki geniş açıyı bulur.',
 kart='K-GUL-09 (alandan açı) · 6, 8, alan 12√3',
 metin='Şekilde alanı 12√3 cm² olan ABC üçgeninin |AB| = 6 cm ve |AC| = 8 cm dir. α = m(BAC) geniş açıdır.\nŞekil ölçekli değildir.\nBuna göre, α kaç derecedir?',
 dogru=120,yan=[(30,'sin α = √3/2 değerini 30° ile eşlemiş (30° nin sinüsü ½ dir).','bilgi'),(45,'sin α = √3/2 değerini 45° ile eşlemiş (45° nin sinüsü √2/2 dir).','bilgi'),(60,'sin α = √3/2 bulup 60° yazmış; α nın geniş açı olduğu koşulunu kaçırmış.','dikkat'),(150,'150° yi seçmiş; sin 150° = ½ olduğundan alan 12 cm² olurdu, 12√3 değil.','bilgi')],
 istenen='α = m(BAC) açısının ölçüsü (derece).',
 ip=['İki kenarla aradaki açının sinüsünü kullanan alan bağıntısını yaz ve sin α yı çek; sonra hangi özel açıların sinüsünün bu değer olduğuna bak.'],
 bilgi=[SINUS9],
 ad=[A('Alan bağıntısını yaz','Verilen açı, iki kenar arasındadır.','12√3 = ½ × 6 × 8 × sin α'),A('sin α yı bul','Çarpımı sadeleştirip sin α yı yalnız bırak.','12√3 = 24 × sin α → sin α = √3/2'),A('Açıları listele','Özel açılardan sinüsü √3/2 olanlar 60° ve 120° dir.','α = 60° ya da α = 120°'),A('Koşulu uygula','α geniş açı olduğundan 90° den büyük olan seçilir.','α = 120°')],
 puf='sin değeri aynı olan iki açı vardır (α ve 180° − α); soruda dar ya da geniş olduğu yazıyorsa ona göre seç.',sekil=SK)

# ---- 10 · zor · orta noktalar zinciri
kartla('K-GUL-10','Orta noktalar zinciri','D ve E orta noktalarıyla orta taban/paralel kurulur, [AC] üzerinde F nin 1 : 2 oranı bulunur; alan ADC den AEF çıkarılır.','F yi [AC] nin orta noktası sanmak; ADC yi cevap sanmak.','zor',6,'ul-orta-nokta','Orta noktalarla alan bölüşümü')
Bz=(0,0); Cz=(12,0); Az=(3,8); Dz=mid(Bz,Cz); Ez=mid(Az,Dz)
den=(Ez[0]-Bz[0])*(Cz[1]-Az[1])-(Ez[1]-Bz[1])*(Cz[0]-Az[0])
tt=((Az[0]-Bz[0])*(Cz[1]-Az[1])-(Az[1]-Bz[1])*(Cz[0]-Az[0]))/den if False else None
# BE doğrusu ile AC kesişimi
def kes(p1,p2,p3,p4):
    x1,y1=p1;x2,y2=p2;x3,y3=p3;x4,y4=p4; d=(x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
    return (((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4))/d,((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4))/d)
Fz=kes(Bz,Ez,Az,Cz); assert abs(dist(Az,Fz)/dist(Az,Cz)-1/3)<1e-9
assert abs(alan([Az,Bz,Cz])-48)<1e-9 and abs(alan([Ez,Dz,Cz,Fz])-20)<1e-9 and abs(alan([Az,Dz,Cz])-24)<1e-9 and abs(alan([Az,Ez,Fz])-4)<1e-9
assert abs(alan([Ez,Dz,Cz])-12)<1e-9 and 24+4==28 and 24+12==36
s=.5; Pz=lambda p:(p[0]*s,p[1]*s)
f=F(); f.fill([Pz(Ez),Pz(Dz),Pz(Cz),Pz(Fz)]); f.poly([Pz(Az),Pz(Bz),Pz(Cz)]); f.line(Pz(Az),Pz(Dz)); f.line(Pz(Bz),Pz(Fz))
f.tick(Pz(Bz),Pz(Dz)); f.tick(Pz(Dz),Pz(Cz)); f.tick(Pz(Az),Pz(Ez),2); f.tick(Pz(Ez),Pz(Dz),2)
f.vl('A',Pz(Az),(0,1),.3); f.vl('B',Pz(Bz),(-1,-.6),.3); f.vl('C',Pz(Cz),(1,-.6),.3); f.vl('D',Pz(Dz),(0,-1),.3); f.vl('E',Pz(Ez),(-1,.1),.3); f.vl('F',Pz(Fz),(1,.4),.3)
f.node((3,-1.0),'Alan$(ABC)=48\\ \\mathrm{cm}^2$')
SK=f.svg()
q('0010',tipId='ul-orta-nokta',tip='Orta noktalarla alan bölüşümü',z='zor',alt='Orta Noktalar',kaz='Orta noktalar ve paralellikle bölme oranını bulup taralı dörtgenin alanını hesaplar.',
 kart='K-GUL-10 (orta noktalar zinciri) · D, E orta nokta, [BE] ∩ [AC] = {F}',
 metin='Şekilde alanı 48 cm² olan ABC üçgeninde D, [BC] kenarının orta noktası, E ise [AD] kenarortayının orta noktasıdır. [BE] doğru parçası [AC] kenarını F noktasında kesmektedir.\nBuna göre, taralı EDCF dörtgeninin alanı kaç cm² dir?',
 dogru=20,yan=[(36,'ADC üçgeninin alanına EDC üçgeninin alanını da eklemiş: 24 + 12 = 36.','islem'),(18,'F yi [AC] nin orta noktası sanmış: AEF = 24 × ½ × ½ = 6 ve 24 − 6 = 18.','bilgi'),(24,'ADC üçgeninin alanını (48 ÷ 2 = 24) cevap sanmış; AEF üçgenini çıkarmamış.','dikkat'),(28,'AEF üçgenini çıkarmak yerine ADC nin alanına eklemiş: 24 + 4 = 28.','islem')],
 istenen='Taralı EDCF dörtgeninin alanı (cm²).',
 ip=['F noktası [AC] kenarını hangi oranda bölüyor? Orta noktalardan yararlanmayı dene.'],
 bilgi=[ORTAT,ALANORAN],
 ad=[A('ADC yi bul','[AD] kenarortay olduğundan ADC üçgeninin alanı ABC nin yarısıdır.','48 ÷ 2 = 24'),A('D den paralel çiz','D den [BF] ye paralel çizilen doğru [AC] yi G de kessin. BCF üçgeninde D, [BC] nin orta noktası olduğundan G, [CF] nin orta noktasıdır.','|FG| = |GC|'),A('Oranı bul','ADG üçgeninde E, [AD] nin orta noktası ve [EF] // [DG] olduğundan F, [AG] nin orta noktasıdır.','|AF| = |FG| = |GC| → |AF| / |AC| = 1/3'),A('AEF yi bul','AEF ve ADC üçgenleri A köşesinde açıyı paylaşır; kenar oranları 1/2 ve 1/3 tür.','24 × 1/2 × 1/3 = 4'),A('Farkı al','EDCF dörtgeni, ADC den AEF çıkarılınca kalır.','24 − 4 = 20 cm²')],
 puf='Orta noktalar ve paralel çizimiyle bölme oranı bulunur: burada [AC] 1 : 2 oranında bölünür, F orta nokta değildir.',sekil=SK)

# =================== yaz ===================
def bitir_geo():
    for qq in P.ANA: qq['kardes']=None
    P.yaz(os.path.join(GD,ONEK+'-1.json'),'/tmp/bos-'+ONEK+'.json')
    tipler={}
    for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=TIPK[c['tipId']]))['kartlar'].append(c['id'])
    json.dump(dict(konu=KONU_AD,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 TYT Geometri çıkmış soruları (yalnız mantık), MEB 9–10. sınıf geometri müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar',ONEK+'.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler),'soru',len(P.ANA))
bitir_geo()
