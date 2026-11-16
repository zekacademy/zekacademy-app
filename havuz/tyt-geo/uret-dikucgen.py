"""TYT Geometri · Dik Üçgen (hafif mod; kardeş yok, ipucu 1). Koordinatlar hesaplanır, TikZ aynı değerlerden; her cevap/çeldirici assert."""
import sys,os,math,json
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
HV=os.path.join(GD,'..')
from math import sin,cos,tan,radians,degrees,atan2,sqrt,pi
P=Parti('dikucgen','Dik Üçgen','geo|Dik Üçgen',ders='TYT Geometri',idon='tytgeo')
TIPK={}   # tipId -> uygulama konu anahtarı
def konu(k,ad): P.k=k; P.konu_adi=ad; H.KONU=ad
def kartla(id,alt,fikir,tuzak,z,adim,tipId,tip,kaynak=None,kalip='şekilli'):
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


def rk(a,b=1):
    """a√b biçimi (tam sayı çifti); b kareden arınmış olmalı. -> (metin, değer)"""
    assert a>0 and b>0 and all(b%(d*d) for d in range(2,int(b**.5)+2) if d*d<=b),(a,b)
    return (str(a) if b==1 else (f'{a}√{b}' if a!=1 else f'√{b}')), a*math.sqrt(b)
def kare_esit(a,b,n,d=1):
    """(a√b)² = a²b == n/d (tam sayı/Fraction kanıtı)"""
    from fractions import Fraction as Fr
    assert Fr(a*a*b)==Fr(n,d),(a,b,n,d)
def qk(no,ad,dogru,yan,**k):
    """kök içeren şıklı soru: dogru=(a,b), yan=[((a,b),cel,tur)]; şıklar değere göre sıralanır"""
    D=rk(*dogru); Y=[(rk(*v),c,t) for v,c,t in yan]
    vals=[D[1]]+[y[0][1] for y in Y]; assert len(set(round(v,9) for v in vals))==5
    sira=[s for s,_ in sorted([D]+[y[0] for y in Y],key=lambda x:x[1])]
    q(no,ad,dogru=D[0],yan=[(y[0][0],y[1],y[2]) for y in Y],sira=sira,**k)
def bitir_geo():
    for qq in P.ANA: qq['kardes']=None
    P.yaz(os.path.join(GD,'dikucgen-1.json'),'/tmp/bos-dikucgen.json')
    tipler={}
    for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=TIPK[c['tipId']]))['kartlar'].append(c['id'])
    json.dump(dict(konu='Dik Üçgen',surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 TYT Geometri çıkmış soruları (yalnız mantık), MEB 9–10. sınıf geometri müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar','dikucgen.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler))

PIS=B('Pisagor bağıntısı','dik üçgende dik kenarların kareleri toplamı hipotenüsün karesine eşittir. Örnek: dik kenarları 8 ve 15 olan üçgende hipotenüs √(64 + 225) = 17’dir. Sık kullanılan üçlüler: 3-4-5, 5-12-13, 8-15-17, 7-24-25 ve katları')
OZEL=B('Özel dik üçgenler','30°-60°-90° üçgende kenarlar 1 : √3 : 2 oranındadır (en kısa kenar 30°’nin karşısındadır); 45°-45°-90° üçgende kenarlar 1 : 1 : √2 oranındadır. Örnek: hipotenüsü 8 olan 30°-60°-90° üçgende kenarlar 4, 4√3 ve 8’dir')
OKLID=B('Öklid bağıntıları','dik üçgende hipotenüse indirilen yükseklik hipotenüsü p ve k parçalarına ayırırsa h² = p × k, a² = p × c (a, p’ye komşu dik kenar, c hipotenüs) olur. Örnek: p = 2, k = 8 ise h = 4 ve komşu dik kenar için a² = 2 × 10 = 20')
KORT=B('Hipotenüse ait kenarortay','dik üçgende hipotenüse ait kenarortayın uzunluğu hipotenüsün yarısına eşittir; yani hipotenüsün orta noktası üç köşeye de eşit uzaklıktadır. Örnek: hipotenüsü 14 olan dik üçgende bu kenarortay 7’dir')
ALD=B('Dik üçgenin alanı','dik kenarların çarpımının yarısıdır; hipotenüs ve ona ait yükseklikle de hesaplanır: Alan = (a × b) ÷ 2 = (c × h) ÷ 2. Örnek: dik kenarları 5 ve 12 olan üçgenin alanı 30’dur')
KAT=B('Katlama (simetri)','katlanınca üst üste gelen noktalardan birbirine uzaklıklar eşit olur; kat izi, çakışan iki noktayı birleştiren doğru parçasının orta dikmesidir. Örnek: P noktası Q’ya gelirse kat izi üzerindeki her noktanın P’ye ve Q’ya uzaklığı eşittir')
RAMP=B('Eğim ve açı','yere göre α açısı yapan rampada karşı dik kenar yüksekliği, komşu dik kenar yatay uzaklığı gösterir. 30°’nin karşısındaki kenar hipotenüsün yarısıdır; 45° ise iki dik kenar eşittir')
KY='ÖSYM 2018–2026 TYT Geometri soruları (yalnız mantık) · MEB 9–10. sınıf geometri'

# =================== 01 · merdiven · kolay · hikâyeli ===================
konu('geo|Dik Üçgen','Dik Üçgen')
kartla('K-GDU-01','Duvara dayalı merdiven','Duvar, zemin ve merdiven dik üçgen oluşturur; merdiven hipotenüstür. Pisagor üçlüsü (5-12-13) tanınırsa işlem kısalır.','Hipotenüsü dik kenar sanıp toplama ya da çıkarma yapmak; karekök almayı unutmak.','kolay',3,'ge-du-pisagor','Pisagor bağıntısı ve üçlüleri',kalip='hikâyeli')
s=.32; Ld,Ba=13,5; Hh=12; assert Ba**2+Hh**2==Ld**2
A1=(0,0); B1=(Ba*s,0); C1=(0,Hh*s)
assert abs(ang(A1,B1,C1)-90)<1e-9 and abs(dist(B1,C1)/s-Ld)<1e-9
assert 13*5==65 and 13+5==18 and 13**2==169 and 13**2-5**2==144 and Hh==12
f=F(); f.line((0,0),(0,Hh*s+.25),'very thick'); f.line((-.35,0),(B1[0]+.35,0),'very thick'); f.line(B1,C1,'thick'); f.dik(A1,B1,C1)
f.sl('$13$',B1,C1,A1,.3); f.sl('$5$',A1,B1,C1,.3); f.sl('$x$',A1,C1,B1,.3)
SK1=f.svg()
q('0001',tipId='ge-du-pisagor',tip='Pisagor bağıntısı ve üçlüleri',z='kolay',alt='Merdiven Problemi',kaz='Duvara dayalı merdivenin oluşturduğu dik üçgende Pisagor bağıntısıyla yüksekliği bulur.',kalip='hikâyeli',
 kart='K-GDU-01 (merdiven) · 5-12-13 üçlüsü ile duvar yüksekliği',
 metin='Bir itfaiye eri, boyu ve alt ucunun duvara uzaklığı şekilde metre cinsinden verilen merdiveni, yere dik bir duvara şekildeki gibi dayıyor. Zemin düzdür ve merdiven duvara tam olarak dayanmaktadır. Şekil ölçekli değildir.\nBuna göre, merdivenin üst ucunun yerden yüksekliği olan x kaç metredir?',
 dogru=12,yan=[(65,'İki uzunluğu çarpmış: 13 × 5 = 65.','bilgi'),(18,'Merdivenin boyu ile alt uzaklığı toplamış: 13 + 5 = 18.','bilgi'),(144,'13² − 5² = 144 işlemini yapıp karekökünü almayı unutmuş.','islem'),(169,'Hipotenüsün karesini (13² = 169) yazıp bırakmış.','dikkat')],
 istenen='Merdivenin üst ucunun yerden yüksekliği x (m).',
 ip=['Duvar, zemin ve merdiven birlikte nasıl bir üçgen oluşturuyor? Verilen uzunluklar bu üçgenin hangi kenarları?'],
 bilgi=[PIS],
 ad=[A('Dik üçgeni belirle','Duvar zemine diktir; duvar, zemin ve merdiven dik üçgendir. Merdiven dik açının karşısında, yani hipotenüstür.','hipotenüs = 13 · bir dik kenar = 5'),A('Pisagor’u yaz','Hipotenüsün karesi, dik kenarların kareleri toplamına eşittir.','13² = 5² + x² → x² = 169 − 25 = 144'),A('Karekökü al','Uzunluk pozitif olduğundan x pozitif kökle bulunur.','x = 12')],
 puf='Merdiven, duvar ve zemin dik üçgendir; merdiven hipotenüstür. 5-12-13 gibi üçlüleri ezberlemek işlemi kısaltır.',sekil=SK1)

# =================== 02 · 30-60-90 · kolay ===================
kartla('K-GDU-02','30°-60°-90° üçgende kenar','Hipotenüs verilince 30°’nin karşısı yarısı, 60°’nin karşısı bunun √3 katıdır.','Karşı kenarları karıştırmak (60°’nin karşısına 30° kuralını uygulamak); √2 ile √3’ü karıştırmak.','kolay',3,'ge-du-ozel','Özel dik üçgenler')
H2=12; sh=H2//2; assert sh*2==H2
kare_esit(6,3,H2*H2*3,4)    # (6√3)² = 108 = 12²·3/4
s=.38; A2=(0,0); B2=(6*sqrt(3)*s,0); C2=(0,6*s)
assert abs(ang(A2,B2,C2)-90)<1e-9 and abs(ang(B2,A2,C2)-30)<1e-9 and abs(ang(C2,A2,B2)-60)<1e-9 and abs(dist(B2,C2)/s-12)<1e-9
f=F(); f.poly([A2,B2,C2]); f.dik(A2,B2,C2); f.arc(B2,A2,C2,.7,'$30^\\circ$',1.35)
f.sl('$12$',B2,C2,A2,.3); f.sl('$x$',A2,B2,C2,.3)
f.vl('A',A2,(-1,-1),.3); f.vl('B',B2,(1,-.5),.3); f.vl('C',C2,(-.3,1),.3)
SK2=f.svg()
qk('0002',[A('Kenarın yerini bul','m(ABC) = 30° olduğundan m(ACB) = 60° dir. x = |AB|, 60°’nin karşısındaki kenardır.','m(C) = 180° − 90° − 30° = 60°'),A('Oranları yaz','30°-60°-90° üçgende kenarlar 1 : √3 : 2 oranındadır; hipotenüs 2 birimdir.','|AC| : |AB| : |BC| = 1 : √3 : 2'),A('Hesapla','Hipotenüs 12 ise bir birim 6’dır; 60°’nin karşısı 6√3’tür.','x = 6√3')],
 (6,3),[((6,1),'En kısa kenarı (30°’nin karşısı, hipotenüsün yarısı) bulmuş; x ise 60°’nin karşısındadır.','dikkat'),((4,3),'|AB| = 12 ÷ √3 = 4√3 yazmış; hipotenüsü √3’e bölmüş.','bilgi'),((6,2),'45°-45°-90° kuralını (√2) uygulamış: 6√2.','bilgi'),((3,3),'Hipotenüsün yarısını iki kez alıp (12 ÷ 4 = 3) √3 ile çarpmış: 3√3.','islem')],
 tipId='ge-du-ozel',tip='Özel dik üçgenler',z='kolay',alt='30-60-90 Üçgeni',kaz='30°-60°-90° üçgende kenar oranlarını kullanarak bir dik kenarı bulur.',
 kart='K-GDU-02 (özel üçgen) · hipotenüs 12, 30°’nin karşısındaki dışındaki dik kenar',
 metin='Şekilde, A köşesindeki açısı dik olan bir ABC üçgeni verilmiştir. Üçgenin B köşesindeki açısının ölçüsü 30° dir ve B ile C köşelerini birleştiren [BC] kenarının uzunluğu 12 cm’dir. [AB] kenarının uzunluğu x ile gösterilmiştir. Şekil ölçekli değildir.\nBuna göre, x kaç cm’dir?',
 istenen='x = |AB| uzunluğu (cm).',
 ip=['Üçgenin üç açısını yaz; bu açılar kenarlar arasında nasıl bir bağlantı kurar?'],
 bilgi=[OZEL],
 puf='30°-60°-90° üçgende kenarlar 1 : √3 : 2’dir; önce hangi kenarın hangi açının karşısında olduğunu belirle.',sekil=SK2)

# =================== 03 · Öklid · orta ===================
kartla('K-GDU-03','Hipotenüse inen yükseklik ve Öklid','Yükseklik ve bir parça verilince Öklid’den öbür parça, sonra dik kenar bulunur; kök a√b biçiminde kalır.','Öklid’i yanlış parçayla kurmak; AC² = AD × BC gibi yanlış çarpım; komşu olmayan parçayı kullanmak.','orta',4,'ge-du-oklid','Öklid bağıntıları ile dik kenar')
AD3,BD3=6,3; DC3=AD3**2//BD3; assert BD3*DC3==AD3**2 and DC3==12
BC3=BD3+DC3; assert BC3==15 and DC3*BC3==180 and 180==6**2*5
kare_esit(6,5,DC3*BC3); kare_esit(3,5,AD3**2+BD3**2); kare_esit(3,10,AD3*BC3)
s=.3; B3=(0,0); D3=(BD3*s,0); C3=(BC3*s,0); A3=(BD3*s,AD3*s)
assert abs(ang(A3,B3,C3)-90)<1e-9 and abs(dist(A3,C3)/s-sqrt(180))<1e-9
f=F(); f.poly([A3,B3,C3]); f.line(A3,D3); f.dik(A3,B3,C3); f.dik(D3,A3,C3)
f.sl('$6$',A3,D3,B3,.28); f.node((BD3*s/2,-.3),'$3$')
f.vl('A',A3,(0,1),.3); f.vl('B',B3,(-1,-.5),.3); f.vl('C',C3,(1,-.5),.3); f.vl('D',D3,(.1,-1),.3)
SK3=f.svg()
qk('0003',[A('Diğer parçayı bul','Yükseklik hipotenüsü iki parçaya ayırır: h² = |BD| × |DC|.','6² = 3 × |DC| → |DC| = 12'),A('Hipotenüsü hesapla','Parçaların toplamı hipotenüsü verir.','|BC| = 3 + 12 = 15'),A('Öklid ile |AC|’yi bul','|AC| dik kenarının karesi, kendisine komşu parça ile hipotenüsün çarpımıdır.','|AC|² = |DC| × |BC| = 12 × 15 = 180'),A('Kökü sadeleştir','180 = 36 × 5 olduğundan karekök 6√5 olur.','|AC| = 6√5')],
 (6,5),[((3,5),'|AC|² = |AD|² + |BD|² yazmış; bu |AB|² değeridir (3√5).','bilgi'),((3,10),'|AC|² = |AD| × |BC| = 90 yazmış (yükseklik × hipotenüs); bağıntı yanlış.','bilgi'),((12,1),'Yalnız |DC| = 12’yi bulup bırakmış; |AC| ile |DC| aynı uzunluk değildir.','dikkat'),((15,1),'|BC| = 15’i bulup bunu |AC| sanmış.','dikkat')],
 tipId='ge-du-oklid',tip='Öklid bağıntıları ile dik kenar',z='orta',alt='Öklid Bağıntıları',kaz='Hipotenüse indirilen yükseklik ve parçalarla Öklid bağıntısını kullanıp dik kenarı bulur.',
 kart='K-GDU-03 (Öklid) · AD = 6, BD = 3, AC isteniyor',
 metin='Şekilde, A köşesindeki açısı dik olan bir ABC üçgeni çizilmiştir. A köşesinden [BC] kenarına indirilen dikmenin ayağı olan D noktası, [BC] kenarının üzerindedir. |AD| = 6 cm ve |BD| = 3 cm’dir. Şekil ölçekli değildir.\nBuna göre, [AC] kenarının uzunluğu kaç cm’dir?',
 istenen='|AC| uzunluğu (cm).',
 ip=['Dik üçgende hipotenüse inen yükseklik, hipotenüsün parçalarıyla bir bağıntı kurar; önce eksik parçayı bul.'],
 bilgi=[OKLID],
 puf='Öklid: h² = p × k; dik kenar² = komşu parça × hipotenüs. Köklü sonuçlarda önce kareyi tam kare çarpanlara ayır.',sekil=SK3)

# =================== 04 · arsa, hipotenüse kenarortay · orta · hikâyeli ===================
kartla('K-GDU-04','Hipotenüse ait kenarortay','Hipotenüse ait kenarortay hipotenüsün yarısıdır; ADC üçgeninde |AD| = |DC| olur ve çevre kolayca yazılır.','Kenarortayı dik kenarlardan biri sanmak; yanlış üçgenin çevresini almak; hipotenüsü Pisagor’la bulmayı atlamak.','orta',3,'ge-du-kenarortay','Hipotenüse ait kenarortay',kalip='hikâyeli')
AB4,AC4=6,8; BC4=10; assert AB4**2+AC4**2==BC4**2; AD4=BC4//2; assert AD4==5
cev4=AD4+AD4+AC4; assert cev4==18 and AC4+AD4==13 and AB4+AC4==14 and AB4+AD4+AD4==16 and AB4+AC4+BC4==24
s=.5; A4=(0,0); B4=(0,AB4*s); C4=(AC4*s,0); D4=mid(B4,C4)
assert abs(dist(A4,D4)/s-AD4)<1e-9
f=F(); f.poly([A4,B4,C4]); f.line(A4,D4,'thick'); f.dik(A4,B4,C4); f.tick(B4,D4,1); f.tick(D4,C4,1)
f.sl('$6$',A4,B4,C4,.3); f.sl('$8$',A4,C4,B4,.3)
f.vl('A',A4,(-1,-1),.3); f.vl('B',B4,(-.3,1),.3); f.vl('C',C4,(1,-.5),.3); f.vl('D',D4,(1,.6),.3)
SK4=f.svg()
q('0004',tipId='ge-du-kenarortay',tip='Hipotenüse ait kenarortay',z='orta',alt='Arsada Çit Çevresi',kaz='Hipotenüse ait kenarortayın yarısına eşitliğini kullanıp bir üçgenin çevresini hesaplar.',kalip='hikâyeli',
 kart='K-GDU-04 (kenarortay) · AB = 6, AC = 8, D orta nokta, çevre(ADC)',
 metin='Dik üçgen biçimli ABC arsasının dik köşesi A’dır; dik kenarların uzunlukları şekilde metre cinsinden verilmiştir. A köşesinden, karşısındaki [BC] kenarının orta noktası olan D noktasına düz bir çit çekilerek arsa iki bölüme ayrılıyor.\nBuna göre, ADC bölümünün çevresini tamamen telle çevirmek için kaç metre tel gerekir?',
 dogru=18,yan=[(13,'Çevreye |DC| kenarını katmamış: 8 + 5 = 13.','dikkat'),(14,'Dik kenarları toplamış: 6 + 8 = 14.','dikkat'),(16,'ABD bölümünün çevresini bulmuş: 6 + 5 + 5 = 16.','dikkat'),(24,'Tüm ABC arsasının çevresini (6 + 8 + 10) bulmuş.','dikkat')],
 istenen='ADC bölümünün çevresi (m).',
 ip=['D noktası hipotenüsün orta noktasıysa A, B ve C köşelerine uzaklıkları arasında nasıl bir ilişki vardır?'],
 bilgi=[KORT,PIS],
 ad=[A('Hipotenüsü bul','Pisagor ile |BC| bulunur.','|BC|² = 6² + 8² = 100 → |BC| = 10'),A('Kenarortayı bul','Hipotenüse ait kenarortay hipotenüsün yarısıdır; ayrıca |DC| = |BC| ÷ 2.','|AD| = |DC| = 10 ÷ 2 = 5'),A('Çevreyi yaz','ADC üçgeninin üç kenarını topla.','5 + 5 + 8 = 18')],
 puf='Dik üçgende hipotenüsün orta noktası, üç köşeye de eşit uzaklıktadır: kenarortay = hipotenüs ÷ 2.',sekil=SK4)

# =================== 05 · 3:4:5 çevre ve alan · orta ===================
kartla('K-GDU-05','Kenar oranı 3:4:5 ve alan','Çevreden k bulunur, dik kenarlardan alan hesaplanır; dik kenarlar yerine hipotenüs kullanılmaz.','Alanda yarıyı unutmak; hipotenüsü dik kenar sanmak; çevreyi alan sanmak.','kolay',3,'ge-du-pisagor','Pisagor bağıntısı ve üçlüleri')
k5=60//12; assert 12*k5==60 and 3*k5==15 and 4*k5==20 and 5*k5==25
al5=15*20//2; assert al5==150 and 15*20==300 and 20*25//2==250 and 15*25==375
assert (3*k5)**2+(4*k5)**2==(5*k5)**2
s=.17; A5=(0,0); B5=(0,15*s); C5=(20*s,0)
assert abs(ang(A5,B5,C5)-90)<1e-9
f=F(); f.poly([A5,B5,C5]); f.dik(A5,B5,C5)
f.sl('$3k$',A5,B5,C5,.35); f.sl('$4k$',A5,C5,B5,.35); f.sl('$5k$',B5,C5,A5,.35)
f.vl('A',A5,(-1,-1),.3); f.vl('B',B5,(-.3,1),.3); f.vl('C',C5,(1,-.5),.3)
SK5=f.svg()
q('0005',tipId='ge-du-pisagor',tip='Pisagor bağıntısı ve üçlüleri',z='kolay',alt='Çevreden Alana',kaz='Kenarları orantılı verilen dik üçgenin çevresinden k’yı bulup alanı hesaplar.',
 kart='K-GDU-05 (3-4-5) · çevre 60, alan isteniyor',
 metin='Şekildeki ABC üçgeninde m(BAC) = 90°, |AB| = 3k, |AC| = 4k ve |BC| = 5k dir (k > 0). k pozitif bir gerçek sayıdır ve üçgenin çevresi 60 cm’dir. Şekil ölçekli değildir.\nBuna göre, ABC üçgeninin alanı kaç cm²’dir?',
 dogru=150,yan=[(60,'Üçgenin çevresini alan sanıp 60 yazmış.','dikkat'),(250,'Hipotenüsü ve bir dik kenarı kullanmış: 20 × 25 ÷ 2 = 250.','bilgi'),(300,'Dik kenarları çarpıp ikiye bölmeyi unutmuş: 15 × 20 = 300.','islem'),(375,'Dik kenar yerine hipotenüsle çarpmış: 15 × 25 = 375.','bilgi')],
 istenen='ABC üçgeninin alanı (cm²).',
 ip=['Çevre bilgisi k için bir denklem verir; alan formülünde hangi iki kenar çarpılır?'],
 bilgi=[ALD],
 ad=[A('k değerini bul','Üç kenar toplamı çevreyi verir.','3k + 4k + 5k = 60 → 12k = 60 → k = 5'),A('Dik kenarları bul','k = 5 ile kenarlar hesaplanır.','|AB| = 15 · |AC| = 20 · |BC| = 25'),A('Alanı hesapla','Dik kenarlar taban ve yüksekliktir.','(15 × 20) ÷ 2 = 150')],
 puf='Oranlı kenarlarda önce çevre ya da başka bir veriyle oran sabitini bul, sonra kenarlarla alanı yaz.',sekil=SK5)

# =================== 06 · kâğıt katlama · zor · hikâyeli ===================
kartla('K-GDU-06','Dik üçgen kâğıdı köşeden katlama','C köşesi B’ye gelince kat izi [BC]’nin orta dikmesidir; E noktasında |EB| = |EC| olur ve ABE üçgeninin çevresi |AB| + |AC|’ye eşit çıkar.','|EB| ile |EC|’yi eşitlemeyi görememek; kat izinin uzunluğunu sormak sanmak; çevreye yanlış kenarı katmak.','zor',4,'ge-du-katlama','Dik üçgen kâğıdı köşeden katlama',kalip='hikâyeli')
AB6,AC6=3,9; AE6=(AC6**2-AB6**2)//(2*AC6); assert AE6*2*AC6==AC6**2-AB6**2 and AE6==4
EC6=AC6-AE6; BE6=5; assert AB6**2+AE6**2==BE6**2 and EC6==BE6
cev6=AB6+AE6+BE6; assert cev6==12==AB6+AC6 and AB6+AE6==7 and AE6+BE6==9 and AB6+EC6+EC6==13 and AB6+2*AC6==21
s=.55; A6=(0,0); B6=(0,AB6*s); C6=(AC6*s,0); E6=(AE6*s,0); D6=mid(B6,C6)
assert abs(dist(E6,B6)-dist(E6,C6))<1e-9 and abs((D6[0]-E6[0])*(C6[0]-B6[0])+(D6[1]-E6[1])*(C6[1]-B6[1]))<1e-9
f=F(); f.poly([A6,B6,C6]); f.line(D6,E6,'dashed'); f.dik(A6,B6,C6)
f.sl('$3$',A6,B6,C6,.3); f.sl('$9$',A6,C6,B6,.3)
f.vl('A',A6,(-1,-1),.3); f.vl('B',B6,(-.3,1),.3); f.vl('C',C6,(1,-.5),.3); f.vl('D',D6,(.5,1),.3); f.vl('E',E6,(-.7,1),.3)
SK6=f.svg()
q('0006',tipId='ge-du-katlama',tip='Dik üçgen kâğıdı köşeden katlama',z='zor',alt='Üçgen Kâğıdı Katlama',kaz='Katlamada eşit kalan uzunlukları belirleyip oluşan üçgenin çevresini bulur.',kalip='hikâyeli',
 kart='K-GDU-06 (katlama) · AB = 3, AC = 9, C köşesi B’ye',
 metin='Dik üçgen biçimli bir kâğıtta m(BAC) = 90° olup dik kenarların uzunlukları şekilde cm cinsinden verilmiştir. Kâğıt, C köşesi B köşesinin üzerine gelecek biçimde katlanıyor; kat izi [DE] dir (D ∈ [BC], E ∈ [AC]).\nBuna göre, ABE üçgeninin çevresi kaç cm’dir?',
 dogru=12,yan=[(7,'|BE| kenarını katmamış: |AB| + |AE| = 3 + 4 = 7.','dikkat'),(9,'|AE| + |BE| = 4 + 5 = 9 almış; |AB| kenarını çevreye katmamış.','dikkat'),(13,'|AE| yerine |EC| = 5 yazmış: 3 + 5 + 5 = 13.','bilgi'),(21,'|AB| + 2 × |AC| = 3 + 18 = 21 yazmış; eşit parçaları yanlış yorumlamış.','bilgi')],
 istenen='ABE üçgeninin çevresi (cm).',
 ip=['C köşesi B’ye geldiğinde E noktasının B ve C’ye uzaklıkları hakkında ne söyleyebilirsin?'],
 bilgi=[KAT,PIS],
 ad=[A('Eşit uzunlukları yaz','Katlamada C, B’ye geldiği için kat izi üzerindeki E noktası B’ye ve C’ye eşit uzaklıktadır.','|EB| = |EC|'),A('|AE| = a al','|AE| = a ise |EC| = 9 − a ve |EB| = 9 − a olur; ABE dik üçgenine Pisagor uygula.','3² + a² = (9 − a)² → 9 = 81 − 18a → a = 4'),A('Kenarları hesapla','a = 4 ile |EB| = 5 bulunur; 3-4-5 üçlüsü olur.','|AB| = 3 · |AE| = 4 · |EB| = 5'),A('Çevreyi topla','ABE üçgeninin üç kenarı toplanır.','3 + 4 + 5 = 12')],
 kisa='|EB| = |EC| olduğundan ABE üçgeninin çevresi |AB| + |AE| + |EC| = |AB| + |AC| = 3 + 9 = 12 olur; Pisagor’a gerek kalmaz.',
 puf='Katlamada çakışan iki nokta kat izi üzerindeki her noktaya eşit uzaklıktadır; çevrede eşit parçalar birbirine eklenerek tüm kenar elde edilir.',sekil=SK6)

# =================== 07 · kenarortay ve yükseklik · zor ===================
kartla('K-GDU-07','Yükseklik, kenarortay ve alan','AH ve HM’den AM Pisagorla bulunur; AM = BC/2 olduğundan BC iki katıdır ve alan hipotenüs × yükseklik ÷ 2 ile bulunur.','AM’yi hipotenüs sanmak; alanda yükseklik yerine HM’yi kullanmak; yarıyı unutmak.','orta',4,'ge-du-kenarortay','Hipotenüse ait kenarortay')
AH7,HM7=12,5; AM7=13; assert AH7**2+HM7**2==AM7**2; BC7=2*AM7; al7=BC7*AH7//2; assert BC7==26 and al7==156 and 60==AH7*HM7 and 13*12//2==78 and BC7*HM7==130 and AH7**2==144
s=.2; M7=(0,0); B7=(-13*s,0); C7=(13*s,0); H7=(-5*s,0); A7=(-5*s,12*s)
assert abs(ang(A7,B7,C7)-90)<1e-9 and abs(dist(A7,M7)/s-13)<1e-9 and abs(alan([A7,B7,C7])/s**2-156)<1e-9
f=F(); f.poly([A7,B7,C7]); f.line(A7,H7); f.line(A7,M7); f.dik(A7,B7,C7,.13); f.dik(H7,A7,C7); f.tick(B7,M7,1); f.tick(M7,C7,1)
f.sl('$12$',A7,H7,M7,.3); f.sl('$5$',H7,M7,A7,.3)
f.vl('A',A7,(-.2,1),.3); f.vl('B',B7,(-1,-.5),.3); f.vl('C',C7,(1,-.5),.3); f.vl('H',H7,(-.3,-1),.3); f.vl('M',M7,(.3,-1),.3)
SK7=f.svg()
q('0007',tipId='ge-du-kenarortay',tip='Hipotenüse ait kenarortay',z='orta',alt='Kenarortay ve Yükseklik',kaz='Yükseklik ve hipotenüse ait kenarortayın özelliğinden hipotenüsü bulup alanı hesaplar.',
 kart='K-GDU-07 (kenarortay, yükseklik) · AH = 12, HM = 5, alan',
 metin='Şekilde, A köşesindeki açısı dik olan bir ABC üçgeni verilmiştir. A köşesinden [BC] kenarına indirilen dikmenin ayağı H, [BC] kenarının orta noktası ise M noktasıdır; H ile M noktaları farklıdır. |AH| = 12 cm ve |HM| = 5 cm’dir. Şekil ölçekli değildir.\nBuna göre, ABC üçgeninin alanı kaç cm²’dir?',
 dogru=156,yan=[(60,'|AH| × |HM| = 12 × 5 = 60 işlemini yapmış; bu alan değil.','bilgi'),(78,'|AM| = 13’ü hipotenüs sanmış: 13 × 12 ÷ 2 = 78.','bilgi'),(130,'Yükseklik yerine |HM| = 5 alıp ikiye bölmeyi unutmuş: 26 × 5 = 130.','dikkat'),(144,'Yüksekliğin karesini (12² = 144) alan sanmış.','bilgi')],
 istenen='ABC üçgeninin alanı (cm²).',
 ip=['AHM üçgeninden hangi uzunluğu bulabilirsin? Bu uzunluk büyük üçgenin hangi kenarıyla ilgili?'],
 bilgi=[KORT,ALD],
 ad=[A('|AM|’yi bul','AHM dik üçgeninde Pisagor uygula (5-12-13 üçlüsü).','|AM|² = 12² + 5² = 169 → |AM| = 13'),A('Hipotenüsü bul','M, hipotenüsün orta noktasıdır; kenarortay hipotenüsün yarısıdır.','|BC| = 2 × 13 = 26'),A('Alanı yaz','Hipotenüs ve ona ait yükseklikle alan hesaplanır.','Alan = (26 × 12) ÷ 2 = 156')],
 puf='Hipotenüse ait kenarortayı bulursan hipotenüs onun iki katıdır; alanı hipotenüs × yükseklik ÷ 2 ile yaz.',sekil=SK7)

# =================== 08 · kayan merdiven · zor · hikâyeli ===================
kartla('K-GDU-08','Kayan merdiven','Merdiven boyu sabit; iki konumda 7-24-25 ve 15-20-25 üçgenleri oluşur. Alt ucun kayması yeni ve eski uzaklığın farkıdır.','Eşit kayma sanmak; yeni uzaklığı kayma sanmak; yüksekliği kayma sanmak.','zor',4,'ge-du-pisagor','Pisagor bağıntısı ve üçlüleri',kalip='hikâyeli')
L8=25; b0=7; h0=24; assert b0**2+h0**2==L8**2; h1=h0-4; b1=15; assert h1==20 and b1**2+h1**2==L8**2; x8=b1-b0; assert x8==8
assert 4==h0-h1 and 15==b1 and 20==h1 and 24==h0
s=.17; P8=(b0*s,0); T8=(0,h0*s); Q8=(b1*s,0); U8=(0,h1*s)
assert abs(dist(P8,T8)/s-25)<1e-9 and abs(dist(Q8,U8)/s-25)<1e-9
f=F(); f.line((0,0),(0,h0*s+.25),'very thick'); f.line((-.35,0),(Q8[0]+.4,0),'very thick'); f.line(P8,T8,'dashed'); f.line(Q8,U8,'thick'); f.dik((0,0),P8,T8)
f.node(add(mid(Q8,U8),mul(un((U8[1]-Q8[1],Q8[0]-U8[0])),.3)),'$25$','rotate=%.1f'%degrees(atan2(U8[1]-Q8[1],U8[0]-Q8[0])-pi)); f.sl('$7$',(0,0),P8,T8,.3); f.sl('$4$',U8,T8,P8,.3); f.node((mid(P8,Q8)[0],-.3),'$x$')
SK8=f.svg()
q('0008',tipId='ge-du-pisagor',tip='Pisagor bağıntısı ve üçlüleri',z='zor',alt='Merdiven Kayıyor',kaz='Merdivenin iki konumunda oluşan dik üçgenlerde Pisagor bağıntısıyla alt ucun kaymasını bulur.',kalip='hikâyeli',
 kart='K-GDU-08 (kayan merdiven) · 25 m merdiven, 7 m, üst uç 4 m iner',
 metin='Yere dik bir duvara dayalı olan merdivenin boyu ve ilk konumda alt ucunun duvara uzaklığı şekilde metre cinsinden verilmiştir. Merdiven duvar boyunca aşağı kayıyor; üst ucu 4 m inince duruyor. Merdivenin boyu değişmemektedir (kesikli çizgi ilk konumunu gösterir) ve zemin düzdür. Şekil ölçekli değildir.\nBuna göre, merdivenin alt ucu duvardan uzaklaşma yönünde kaç metre kaymıştır?',
 dogru=8,yan=[(4,'Alt ucun da üst uç kadar (4 m) kaydığını sanmış.','bilgi'),(15,'Yeni uzaklığı (15 m) bulup ilk uzaklığı çıkarmamış.','dikkat'),(20,'İkinci konumdaki yüksekliği (20 m) kayma sanmış.','dikkat'),(24,'İlk konumdaki yüksekliği (24 m) kayma olarak yazmış.','dikkat')],
 istenen='Merdivenin alt ucunun kayma miktarı x (m).',
 ip=['Merdivenin ilk ve son konumunda oluşan iki dik üçgeni ayrı ayrı çöz; sabit kalan uzunluk hangisi?'],
 bilgi=[PIS],
 ad=[A('İlk konumun yüksekliği','Merdiven 25 m ve alt uzaklık 7 m olan dik üçgende Pisagor uygula.','h² = 25² − 7² = 576 → h = 24'),A('Yeni yükseklik','Üst uç 4 m indiğine göre yeni yükseklik hesaplanır.','24 − 4 = 20'),A('Yeni alt uzaklık','Merdiven yine 25 m; yeni dik üçgende Pisagor uygula.','b² = 25² − 20² = 225 → b = 15'),A('Kaymayı bul','Alt ucun yeni ve eski uzaklığı farkı kaymadır.','x = 15 − 7 = 8')],
 puf='Merdiven boyu sabit olduğundan her konum ayrı bir dik üçgendir; iki üçgeni ayrı çöz, sonra farkı al.',sekil=SK8)

# =================== 09 · dikdörtgen tarla, kestirme · orta · hikâyeli ===================
kartla('K-GDU-09','Dikdörtgenin köşegeni ve kestirme yol','Köşegen dik üçgenin hipotenüsüdür (9-40-41); kenar boyunca yürümek ile köşegen arasında 49 − 41 fark vardır.','İki kenarı toplayıp köşegen sanmak; kenar farkını almak; köşegenin 2 × uzun kenar olduğunu sanmak.','orta',3,'ge-du-pisagor','Pisagor bağıntısı ve üçlüleri',kalip='hikâyeli')
k9,u9=9,40; d9=41; assert k9**2+u9**2==d9**2 and k9+u9==49 and u9-k9==31 and 2*u9==80
s=.1; A9=(0,0); B9=(u9*s,0); C9=(u9*s,k9*s); D9=(0,k9*s)
assert abs(dist(A9,C9)/s-41)<1e-9
f=F(); f.poly([A9,B9,C9,D9]); f.line(A9,C9,'dashed'); f.dik(B9,A9,C9,.2)
f.sl('$40$',A9,B9,D9,.3); f.sl('$9$',B9,C9,A9,.3)
f.vl('A',A9,(-1,-1),.3); f.vl('B',B9,(1,-1),.3); f.vl('C',C9,(1,1),.3); f.vl('D',D9,(-1,1),.3)
SK9=f.svg()
q('0009',tipId='ge-du-pisagor',tip='Pisagor bağıntısı ve üçlüleri',z='orta',alt='Tarlada Kestirme Yol',kaz='Dikdörtgenin köşegenini Pisagor ile bulup kestirme yolun uzunluğunu hesaplar.',kalip='hikâyeli',
 kart='K-GDU-09 (dikdörtgen köşegeni) · 40 × 9 tarla, kestirme yol',
 metin='Dikdörtgen biçimli ABCD tarlasının kenar uzunlukları şekilde metre cinsinden verilmiştir. Bir çiftçi, A köşesinden C köşesine tarlanın içinden kesikli çizgiyle gösterilen düz yoldan gidiyor. Tarla düzdür. Şekil ölçekli değildir.\nBuna göre, çiftçinin yürüdüğü yol kaç metredir?',
 dogru=41,yan=[(9,'Yalnız kısa kenarı yol uzunluğu sanmış.','dikkat'),(31,'İki kenarın farkını (40 − 9) almış.','bilgi'),(49,'Kenarları toplamış: 40 + 9; bu, kenarlardan giden yoldur.','bilgi'),(80,'Köşegeni uzun kenarın iki katı sanmış.','bilgi')],
 istenen='Kesikli çizgiyle gösterilen yolun uzunluğu (m).',
 ip=['A, B ve C noktaları hangi üçgeni oluşturuyor? Yol bu üçgenin hangi kenarı?'],
 bilgi=[PIS],
 ad=[A('Dik üçgeni belirle','Dikdörtgenin köşesi dik açıdır; ABC dik üçgeninde yol hipotenüstür.','dik kenarlar 40 ve 9'),A('Pisagor’u yaz','Hipotenüsün karesi dik kenarların kareleri toplamıdır.','|AC|² = 40² + 9² = 1600 + 81 = 1681'),A('Karekökü al','41² = 1681 olduğundan yol 41 m’dir.','|AC| = 41')],
 puf='Dikdörtgenin köşegeni, kenarlarıyla dik üçgen oluşturur; köşegen = √(a² + b²).',sekil=SK9)

# =================== 10 · ikizkenar dik üçgen · orta ===================
kartla('K-GDU-10','İkizkenar dik üçgende yükseklik','45°-45°-90° üçgende hipotenüs dik kenarın √2 katıdır; hipotenüse inen yükseklik aynı zamanda kenarortaydır, hipotenüsün yarısıdır.','Hipotenüsü dik kenar sanmak; yüksekliği dik kenarın yarısı sanmak; √2 yerine √3 kullanmak.','orta',3,'ge-du-ozel','Özel dik üçgenler')
Lg=6; hy=(6,2); kare_esit(6,2,Lg*Lg*2); h10=(3,2); kare_esit(3,2,Lg*Lg,2)    # (3√2)²=18=36/2
s=.5; D10=(0,0); B10=(-3*sqrt(2)*s,0); C10=(3*sqrt(2)*s,0); A10=(0,3*sqrt(2)*s)
assert abs(ang(A10,B10,C10)-90)<1e-9 and abs(dist(A10,B10)/s-6)<1e-9 and abs(dist(A10,D10)/s-3*sqrt(2))<1e-9
f=F(); f.poly([A10,B10,C10]); f.line(A10,D10); f.dik(A10,B10,C10); f.dik(D10,A10,C10); f.tick(A10,B10,1); f.tick(A10,C10,1)
f.sl('$6$',A10,B10,C10,.3)
f.vl('A',A10,(0,1),.3); f.vl('B',B10,(-1,-.5),.3); f.vl('C',C10,(1,-.5),.3); f.vl('D',D10,(0,-1),.3)
SK10=f.svg()
qk('0010',[A('Hipotenüsü bul','45°-45°-90° üçgende hipotenüs, dik kenarın √2 katıdır.','|BC| = 6√2'),A('Kenarortayı belirle','[AD] hipotenüse inen yüksekliktir; ikizkenarda aynı zamanda kenarortaydır ve hipotenüsün yarısına eşittir.','|AD| = |BC| ÷ 2'),A('Hesapla','Hipotenüsün yarısı alınır.','|AD| = 6√2 ÷ 2 = 3√2')],
 (3,2),[((6,3),'Hipotenüsü 6√3 sanıp (√3 kuralı) yarısını almadan bırakmış.','bilgi'),((3,3),'Hipotenüsü 6√3 alıp yarısını bulmuş (√3 kuralını uygulamış).','bilgi'),((6,1),'Dik kenarı yükseklik sanmış.','dikkat'),((6,2),'Hipotenüsü (6√2) bulup yüksekliğin yarısını almayı unutmuş.','dikkat')],
 tipId='ge-du-ozel',tip='Özel dik üçgenler',z='orta',alt='İkizkenar Dik Üçgen',kaz='İkizkenar dik üçgende hipotenüse inen yüksekliği özel üçgen oranı ve kenarortay özelliğiyle bulur.',
 kart='K-GDU-10 (45-45-90) · dik kenar 6, hipotenüse inen yükseklik',
 metin='Şekilde, A köşesindeki açısı dik olan bir ABC üçgeninin dik kenarları eşit uzunluktadır: |AB| = |AC| = 6 cm. A köşesinden hipotenüs olan [BC] kenarına indirilen dikmenin ayağı D noktasıdır. Şekil ölçekli değildir.\nBuna göre, |AD| kaç cm’dir?',
 istenen='|AD| uzunluğu (cm).',
 ip=['Üçgenin açılarını bul; hipotenüsün uzunluğunu dik kenar cinsinden yazmanın bir yolu var mı?'],
 bilgi=[OZEL,KORT],
 puf='İkizkenar dik üçgende hipotenüs = dik kenar × √2 ve hipotenüse inen yükseklik = hipotenüsün yarısıdır.',sekil=SK10)

bitir_geo()
