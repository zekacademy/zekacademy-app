"""TYT Geometri · İkizkenar Üçgen (hafif mod; kardeş yok, ipucu 1). Koordinatlar hesaplanır, TikZ aynı değerlerden; her cevap/çeldirici assert."""
import sys,os,math,json
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
HV=os.path.join(GD,'..')
from math import sin,cos,tan,radians,degrees,atan2,sqrt,pi
P=Parti('ikizkenar','İkizkenar Üçgen','geo|İkizkenar Üçgen',ders='TYT Geometri',idon='tytgeo')
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
    P.yaz(os.path.join(GD,'ikizkenar-1.json'),'/tmp/bos-ikizkenar.json')
    tipler={}
    for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=TIPK[c['tipId']]))['kartlar'].append(c['id'])
    json.dump(dict(konu='İkizkenar Üçgen',surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 TYT Geometri çıkmış soruları (yalnız mantık), MEB 9–10. sınıf geometri müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar','ikizkenar.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler))

IKIZ=B('İkizkenar üçgen','eşit kenarların karşısındaki taban açıları eşittir; iç açıların toplamı 180°’dir. Tepeden tabana inen dikme aynı zamanda açıortay ve kenarortaydır. Örnek: tepe açısı 50° ise taban açıları (180° − 50°) ÷ 2 = 65°’dir')
YUK=B('Tepeden inen yükseklik','ikizkenar üçgende tepeden tabana inen dikme tabanı iki eşit parçaya böler; yarım taban, yükseklik ve eş kenar dik üçgen oluşturur. Örnek: eş kenarı 13, tabanı 10 olan üçgende yükseklik √(13² − 5²) = 12’dir')
ALANTOP=B('Alanı parçalara ayırma','bir üçgenin alanı, içinden bir köşeye birleştirilen parçaların alanları toplamına eşittir; kenar × o kenara inen yükseklik ÷ 2 ile hesaplanır. Örnek: tabanı 8 ve yüksekliği 5 olan üçgenin alanı 20’dir')
DIS=B('Dış açı','üçgenin bir dış açısı, kendisine komşu olmayan iki iç açının toplamına eşittir ve komşu iç açıyla toplamı 180°’dir. Örnek: iç açıları 30° ve 50° olan üçgende üçüncü açının dış açısı 80°’dir')
KY='ÖSYM 2018–2026 TYT Geometri soruları (yalnız mantık) · MEB 9–10. sınıf geometri'

# =================== 01 · taban açıları · kolay ===================
konu('geo|İkizkenar Üçgen','İkizkenar Üçgen')
kartla('K-GIK-01','Taban açıları ve cebirsel açı','Taban açıları eşit ve iç açılar toplamı 180° olduğundan x için bir denklem kurulur; sonra istenen açı hesaplanır.','x’i bulup bırakmak; taban açısını tepe açısı sanmak; iki taban açısını tek açı almak.','kolay',3,'ge-ik-taban','İkizkenar üçgende taban açıları')
xx=32; Bb=2*xx+5; Aa=xx+10; assert Bb==69 and Aa==42 and 2*Bb+Aa==180 and 5*xx+20==180
assert xx==32 and Bb==69 and 2*Bb==138 and 180-Bb==111
h2=radians(Aa/2); Lk=4.2; B1=(-Lk*sin(h2),0); C1=(Lk*sin(h2),0); A1=(0,Lk*cos(h2))
assert abs(dist(A1,B1)-dist(A1,C1))<1e-9 and abs(ang(A1,B1,C1)-42)<1e-9 and abs(ang(B1,A1,C1)-69)<1e-9
f=F(); f.poly([A1,B1,C1]); f.tick(A1,B1); f.tick(A1,C1)
f.arc(A1,B1,C1,.8,'',1); f.node((0,A1[1]-2.2),'$(x+10)^\\circ$'); f.arc(B1,C1,A1,.7,'',1); f.node(add(B1,(1.55,.4)),'$(2x+5)^\\circ$')
f.vl('A',A1,(0,1),.3); f.vl('B',B1,(-1,-.6),.3); f.vl('C',C1,(1,-.6),.3)
SK1=f.svg()
q('0001',tipId='ge-ik-taban',tip='İkizkenar üçgende taban açıları',z='kolay',alt='Cebirsel Taban Açısı',kaz='İkizkenar üçgende taban açılarının eşitliğinden ve iç açılar toplamından x’i bulup tepe açısını hesaplar.',
 kart='K-GIK-01 (taban açıları) · m(B) = 2x + 5, m(A) = x + 10',
 metin='Şekilde, |AB| = |AC| olan bir ABC üçgeni verilmiştir. Üçgenin B köşesindeki iç açısının ölçüsü (2x + 5)°, A köşesindeki iç açısının ölçüsü ise (x + 10)° dir (x bir gerçek sayıdır). Şekil ölçekli değildir.\nBuna göre, m(BAC) kaç derecedir?',
 dogru=42,yan=[(32,'x = 32’yi bulup istenen açıyı hesaplamadan bırakmış.','dikkat'),(69,'B köşesindeki taban açısını (2x + 5 = 69°) bulup tepe açısını hesaplamamış.','dikkat'),(111,'Taban açısının bütünleyenini (180° − 69°) yazmış.','bilgi'),(138,'İki taban açısının toplamını (69° + 69°) yazmış.','dikkat')],
 istenen='m(BAC) açısının ölçüsü.',
 ip=['Eşit kenarların karşısındaki açılar hakkında ne söyleyebilirsin? İç açılar toplamına bir denklem kur.'],
 bilgi=[IKIZ],
 ad=[A('Taban açılarını eşitle','|AB| = |AC| olduğundan m(ABC) = m(ACB) = (2x + 5)° olur.','m(B) = m(C) = 2x + 5'),A('Denklemi kur ve çöz','İç açıların toplamı 180°’dir.','2(2x + 5) + (x + 10) = 180 → 5x + 20 = 180 → x = 32'),A('Tepe açısını hesapla','İstenen açı A köşesindeki açıdır.','m(BAC) = 32 + 10 = 42°'),A('Kontrol et','Üç açı toplamı 180° etmeli.','69° + 69° + 42° = 180°')],
 puf='İkizkenar üçgende taban açıları eşit olduğundan iç açılar toplamından tek bilinmeyenli denklem elde edilir; sonunda istenen açının hangisi olduğuna bak.',sekil=SK1)

# =================== 02 · çadır, yükseklik · kolay · hikâyeli ===================
kartla('K-GIK-02','Tepe yüksekliği','Tepeden tabana inen yükseklik tabanı ortalar; yarım taban, yükseklik ve eş kenar dik üçgen oluşturur (6-8-10).','Yüksekliği eş kenar ya da yarım taban sanmak; tabanı bölmeyi unutmak.','kolay',3,'ge-ik-yukseklik','İkizkenar üçgende yükseklik ve alan',kalip='hikâyeli')
a2,b2=10,12; h2_=8; assert (b2//2)**2+h2_**2==a2**2
s=.4; Bq=(-b2/2*s,0); Cq=(b2/2*s,0); Aq=(0,h2_*s); Dq=(0,0)
assert abs(dist(Aq,Bq)/s-10)<1e-9 and abs(dist(Aq,Cq)/s-10)<1e-9 and abs(ang(Dq,Aq,Cq)-90)<1e-9
assert 10-6==4 and b2//2==6 and a2==10 and b2==12
f=F(); f.poly([Aq,Bq,Cq]); f.line(Aq,Dq,'dashed'); f.dik(Dq,Aq,Cq); f.tick(Aq,Bq); f.tick(Aq,Cq)
f.sl('$10$',Aq,Bq,Cq,.3); f.sl('$12$',Bq,Cq,Aq,.3); f.node((.28,h2_*s/2),'$x$')
f.vl('A',Aq,(0,1),.3); f.vl('B',Bq,(-1,-.6),.3); f.vl('C',Cq,(1,-.6),.3); f.vl('D',Dq,(-.9,.7),.3)
SK2=f.svg()
q('0002',tipId='ge-ik-yukseklik',tip='İkizkenar üçgende yükseklik ve alan',z='kolay',alt='Çadır Direği',kaz='İkizkenar üçgende tepeden tabana inen yüksekliğin tabanı ortaladığını kullanıp Pisagor ile yüksekliği bulur.',kalip='hikâyeli',
 kart='K-GIK-02 (yükseklik) · 10-10-12 üçgeni',
 metin='Cepheden bakıldığında ikizkenar üçgen biçiminde görünen bir çadırın eşit kenarları ile taban uzunluğu şekilde metre cinsinden verilmiştir. Çadırı ortadan taşıyan [AD] direği yere diktir ve D noktası taban üzerindedir. Şekil ölçekli değildir.\nBuna göre, direğin uzunluğu olan x kaç metredir?',
 dogru=8,yan=[(4,'Yarım tabanı (6) eş kenardan çıkarmış: 10 − 6 = 4.','bilgi'),(6,'Yarım tabanı (6 m) direk uzunluğu sanmış.','dikkat'),(10,'Eş kenarın uzunluğunu direk sanmış.','dikkat'),(5,'Eş kenarın yarısını (10 ÷ 2 = 5 m) direk uzunluğu sanmış.','bilgi')],
 istenen='Direğin uzunluğu x (m).',
 ip=['Tepeden tabana inen dikme tabanı nasıl böler? Oluşan dik üçgenin kenarlarını yaz.'],
 bilgi=[YUK,IKIZ],
 ad=[A('Tabanı böl','İkizkenar üçgende tepeden tabana inen dikme tabanı ortalar.','|BD| = |DC| = 12 ÷ 2 = 6'),A('Dik üçgeni kur','ADC dik üçgeninde eş kenar hipotenüstür.','x² + 6² = 10²'),A('Pisagor ile hesapla','Kareleri çıkar ve karekökü al.','x² = 100 − 36 = 64 → x = 8')],
 puf='İkizkenar üçgende tepeden inen yükseklik tabanı ikiye böler; yarım taban, yükseklik ve eş kenar bir dik üçgendir (6-8-10, 5-12-13 gibi).',sekil=SK2)

# =================== 03 · levha, yan kenara inen yükseklik · orta · hikâyeli ===================
kartla('K-GIK-03','Eş kenara inen yükseklik','Tepe yüksekliği Pisagorla bulunur, alan iki farklı tabanla yazılıp eş kenara inen yükseklik çıkarılır.','Tepe yüksekliğini (8) istenen sanmak; alanı ikiye bölmeyi unutmak; yarım tabanı yükseklik sanmak.','orta',4,'ge-ik-yukseklik','İkizkenar üçgende yükseklik ve alan',kalip='hikâyeli')
ab3,bc3=10,12; hA3=8; assert (bc3//2)**2+hA3**2==ab3**2; al3=bc3*hA3//2; assert al3==48
bh3=2*al3/ab3; assert abs(bh3-9.6)<1e-12 and 48/10==4.8
s=.42; B3=(-6*s,0); C3=(6*s,0); A3=(0,8*s)
def ayak(P,V,W):
    u=un(sub(W,V)); t_=(P[0]-V[0])*u[0]+(P[1]-V[1])*u[1]; return add(V,mul(u,t_))
H3=ayak(B3,A3,C3); assert abs(dist(B3,H3)/s-9.6)<1e-9 and abs(dist(A3,B3)/s-10)<1e-9
f=F(); f.poly([A3,B3,C3]); f.line(B3,H3); f.dik(H3,B3,A3,.15); f.tick(A3,B3); f.tick(A3,C3)
f.sl('$10$',A3,B3,C3,.3); f.sl('$12$',B3,C3,A3,.4); f.node(add(mid(B3,H3),(-.18,-.22)),'$x$')
f.vl('A',A3,(0,1),.3); f.vl('B',B3,(-1,-.6),.3); f.vl('C',C3,(1,-.6),.3); f.vl('H',H3,(1,.5),.3)
SK3=f.svg()
q('0003',tipId='ge-ik-yukseklik',tip='İkizkenar üçgende yükseklik ve alan',z='orta',alt='Levhada Dik Kesim',kaz='İkizkenar üçgenin alanını iki farklı tabanla yazarak eş kenara inen yüksekliği bulur.',kalip='hikâyeli',
 kart='K-GIK-03 (alan, yükseklik) · 10-10-12 üçgeni, BH ⊥ AC',
 metin='İkizkenar üçgen biçimindeki ABC ahşap levhasının eşit kenarları ile taban uzunluğu şekilde desimetre cinsinden verilmiştir. Marangoz, B köşesinden [AC] kenarına dik bir doğru parçası boyunca kesim yapacak ve kesim, [AC] kenarını H noktasında bitirecektir. Şekil ölçekli değildir.\nBuna göre, kesimin uzunluğu olan x kaç desimetredir?',
 dogru=9.6,yan=[(4.8,'Alanı (48) eş kenara bölmüş ama 2 ile çarpmayı unutmuş: 48 ÷ 10 = 4,8.','islem'),(6,'Yarım tabanı (6) kesim uzunluğu sanmış.','dikkat'),(8,'Tepeden tabana inen yüksekliği (8) bulup bırakmış.','dikkat'),(12,'Taban uzunluğunu kesim sanmış.','dikkat')],
 istenen='Kesim uzunluğu x (dm).',
 ip=['Üçgenin alanını iki ayrı taban-yükseklik çiftiyle yazabilirsin; önce hangi yükseklik kolay bulunur?'],
 bilgi=[YUK,ALANTOP],
 ad=[A('Tepe yüksekliğini bul','Tepeden tabana inen dikme tabanı ortalar; yarım taban 6, eş kenar 10.','h² = 10² − 6² = 64 → h = 8'),A('Alanı hesapla','Taban 12, yükseklik 8.','Alan = 12 × 8 ÷ 2 = 48'),A('Alanı [AC] tabanıyla yaz','[AC] tabanına ait yükseklik [BH] = x’tir.','10 × x ÷ 2 = 48'),A('x’i bul','Denklemi çöz.','x = 96 ÷ 10 = 9,6')],
 puf='Aynı üçgenin alanı farklı taban-yükseklik çiftleriyle yazılabilir; biri kolay bulunuyorsa diğer yükseklik denklemden çıkar.',sekil=SK3)

# =================== 04 · art arda ikizkenar · orta ===================
kartla('K-GIK-04','Art arda ikizkenar üçgenler (açı zinciri)','|AD| = |DC| ve |AB| = |AD| eşitlikleri açıları zincirleme x cinsinden yazdırır: C = x, DAC = x, ADB = 2x, ABD = 2x.','Dış açıyı (2x) görememek; ABC’yi ikizkenar sanmak; 4x yerine 3x yazmak.','orta',4,'ge-ik-zincir','Art arda ikizkenar üçgenler (açı zinciri)')
xa=28; BAC4=96; assert 3*xa==180-BAC4 and xa==28
Dp=(0,0); L4=2.8; Cp=(L4,0); Ap=(L4*cos(radians(124)),L4*sin(radians(124))); Bp=(2*Ap[0],0)
assert abs(dist(Ap,Dp)-L4)<1e-9 and abs(dist(Ap,Bp)-L4)<1e-9 and abs(dist(Dp,Cp)-L4)<1e-9
assert abs(ang(Ap,Bp,Cp)-96)<1e-9 and abs(ang(Cp,Ap,Dp)-28)<1e-9 and abs(ang(Bp,Ap,Cp)-56)<1e-9 and abs(ang(Dp,Ap,Bp)-56)<1e-9 and abs(ang(Ap,Bp,Dp)-68)<1e-9
assert (180-96)//4==21 and (180-96)//2==42 and 2*xa==56 and 180-96==84
f=F(); f.poly([Ap,Bp,Cp]); f.line(Ap,Dp); f.tick(Ap,Bp); f.tick(Ap,Dp); f.tick(Dp,Cp)
f.arc(Ap,Bp,Cp,.55,'$96^\\circ$',1.12) if False else None
f.arc(Cp,Dp,Ap,.8,'$x$',1.2)
f.vl('A',Ap,(0,1),.3); f.vl('B',Bp,(-1,-.6),.3); f.vl('C',Cp,(1,-.6),.3); f.vl('D',Dp,(.15,-1),.3)
f.arc(Ap,Bp,Cp,.5,None); f.node(add(Ap,(.12,-.95)),'$96^\\circ$')
SK4=f.svg()
q('0004',tipId='ge-ik-zincir',tip='Art arda ikizkenar üçgenler (açı zinciri)',z='orta',alt='Açı Zinciri',kaz='Art arda ikizkenar üçgenlerde dış açı ve taban açılarını zincirleme x cinsinden yazıp açıyı bulur.',
 kart='K-GIK-04 (açı zinciri) · AB = AD = DC, m(BAC) = 96°',
 metin='Şekilde ABC üçgeninin [BC] kenarı üzerinde bir D noktası alınmıştır ve |AB| = |AD| = |DC| dir (eşit çentikli doğru parçalarının uzunlukları eşittir). Şekil ölçekli değildir. m(BAC) = 96° olduğuna göre, x = m(ACB) kaç derecedir?',
 dogru=28,yan=[(21,'ABC’yi 4x paylaşımı sanmış: 84° ÷ 4 = 21°.','bilgi'),(42,'ABC üçgeninin ikizkenar olduğunu sanıp (180° − 96°) ÷ 2 = 42° bulmuş.','bilgi'),(56,'ADB dış açısını (2x) bulup x yerine bunu yazmış.','dikkat'),(84,'180° − 96° = 84° farkını bulup bırakmış.','dikkat')],
 istenen='x = m(ACB) açısının ölçüsü.',
 ip=['|DA| = |DC| olduğuna göre ADC üçgeninde hangi açılar eşittir? Bir açıya x diyerek başla.'],
 bilgi=[IKIZ,DIS],
 ad=[A('x ile başla','|DA| = |DC| olduğundan DAC ve DCA açıları eşittir.','m(DAC) = m(DCA) = x'),A('Dış açıyı yaz','ADB, ADC üçgeninin dış açısıdır; uzak iki iç açının toplamına eşittir.','m(ADB) = x + x = 2x'),A('ABD üçgenini çöz','|AB| = |AD| olduğundan ABD ve ADB açıları eşittir; ABD’nin açıları toplamından BAD bulunur.','m(ABD) = 2x · m(BAD) = 180° − 4x'),A('Büyük üçgeni kur','BAC = BAD + DAC = 96°.','(180° − 4x) + x = 96° → 3x = 84° → x = 28°')],
 puf='Art arda ikizkenar üçgenlerde bir açıya x deyip dış açı ve taban açılarıyla her açıyı x cinsinden yaz; sonunda büyük üçgenin bir açısından denklemi kur.',sekil=SK4)

# =================== 05 · BD = BC, açı zinciri · orta ===================
kartla('K-GIK-05','Eş kenarın karşı kenara oturan ikizkenar üçgen','Tepe açısından taban açıları bulunur; küçük ikizkenar üçgende (|BD| = |BC|) açılar yazılarak ABD açısı fark olarak çıkar.','BD’yi açıortay sanmak; BDC yerine BCD’yi unutmak; 70° − 40° farkını alamamak.','orta',4,'ge-ik-zincir','Art arda ikizkenar üçgenler (açı zinciri)')
A5=40; Bt=(180-A5)//2; assert Bt==70; DBC5=180-2*70; ABD5=Bt-DBC5; assert DBC5==40 and ABD5==30 and 180-70==110 and Bt//2==35
L5=4.2; h5=radians(A5/2); Ac=(0,L5*cos(h5)); Bc=(-L5*sin(h5),0); Cc=(L5*sin(h5),0)
BCl=dist(Bc,Cc); CD5=2*BCl*cos(radians(70)); Dc=add(Cc,mul(un(sub(Ac,Cc)),CD5))
assert abs(dist(Bc,Dc)-BCl)<1e-9 and abs(ang(Bc,Ac,Dc)-30)<1e-9 and abs(ang(Dc,Bc,Cc)-70)<1e-9 and abs(ang(Bc,Ac,Cc)-70)<1e-9 and abs(ang(Ac,Bc,Cc)-40)<1e-9 and abs(ang(Bc,Dc,Cc)-40)<1e-9
f=F(); f.poly([Ac,Bc,Cc]); f.line(Bc,Dc); f.tick(Ac,Bc); f.tick(Ac,Cc); f.tick(Bc,Cc,2); f.tick(Bc,Dc,2)
f.arc(Ac,Bc,Cc,.8,'$40^\\circ$',1.25); f.arc(Bc,Ac,Dc,.8,'$x$',1.1)
f.vl('A',Ac,(0,1),.3); f.vl('B',Bc,(-1,-.6),.3); f.vl('C',Cc,(1,-.6),.3); f.vl('D',Dc,(1,.45),.3)
SK5=f.svg()
q('0005',tipId='ge-ik-zincir',tip='Art arda ikizkenar üçgenler (açı zinciri)',z='orta',alt='İkizkenar İçinde İkizkenar',kaz='İkizkenar üçgenin içindeki ikinci ikizkenar üçgenin açılarını kullanarak bir açıyı fark olarak bulur.',
 kart='K-GIK-05 (açı zinciri) · |AB| = |AC|, |BD| = |BC|, m(BAC) = 40°',
 metin='Şekilde ABC üçgeninde |AB| = |AC| dir. D noktası [AC] kenarı üzerinde alınmış ve |BD| = |BC| olacak biçimde [BD] doğru parçası çizilmiştir. Şekil ölçekli değildir. m(BAC) = 40° olduğuna göre, x = m(ABD) kaç derecedir?',
 dogru=30,yan=[(35,'[BD]’nin ABC açısını ikiye böldüğünü sanmış: 70° ÷ 2 = 35°.','bilgi'),(40,'x açısını A köşesindeki açıya eşit sanmış.','bilgi'),(70,'ABC taban açısını (70°) bulup bırakmış.','dikkat'),(110,'ADB açısının bütünleyenini (180° − 70°) yazmış.','bilgi')],
 istenen='x = m(ABD) açısının ölçüsü.',
 ip=['ABC üçgeninde taban açıları kaç derece? BCD üçgeninde eşit olan kenarların karşısındaki açılara bak.'],
 bilgi=[IKIZ],
 ad=[A('Büyük üçgenin taban açıları','|AB| = |AC| olduğundan B ve C eşittir.','m(ABC) = m(ACB) = (180° − 40°) ÷ 2 = 70°'),A('BCD üçgenini çöz','|BD| = |BC| olduğundan D ve C köşelerindeki açılar eşittir (70°); üçüncü açı DBC’dir.','m(DBC) = 180° − 70° − 70° = 40°'),A('Farkı al','x = ABC açısının DBC kısmı dışında kalan parçasıdır.','x = 70° − 40° = 30°')],
 puf='İçteki ikizkenar üçgenin tepe açısını bulup, büyük üçgenin taban açısından çıkararak aradığın açıya ulaş.',sekil=SK5)

# =================== 06 · uzatılmış kenar, dış açı · zor ===================
kartla('K-GIK-06','İkizkenar üçgen ve uzatılan taban','|AB| = |AC| ve |CA| = |CD| iki ikizkenar üçgen kurar; ACD üçgeninin dış açısı x cinsinden yazılarak tepe açısı bulunur.','D açısını taban açısı sanmak; dış açıyı iç açıyla karıştırmak; 4 adımlık zinciri yarıda bırakmak.','orta',5,'ge-ik-dis','İkizkenar üçgenler ve dış açı')
xb=34; D6=17; Ap6=180-2*xb; assert D6*2==xb and Ap6==112 and 2*xb==68 and 180-2*17==146 and 180-17==163
L6=2.3; Bq6=(0,0); Cq6=(2*L6*cos(radians(xb)),0); Aq6=(L6*cos(radians(xb)),L6*sin(radians(xb))); Dq6=(Cq6[0]+L6,0)
assert abs(dist(Aq6,Bq6)-dist(Aq6,Cq6))<1e-9 and abs(dist(Cq6,Dq6)-dist(Cq6,Aq6))<1e-9
assert abs(ang(Dq6,Aq6,Bq6)-17)<1e-9 and abs(ang(Bq6,Aq6,Cq6)-34)<1e-9 and abs(ang(Aq6,Bq6,Cq6)-112)<1e-9 and abs(ang(Cq6,Aq6,Bq6)-34)<1e-9
f=F(); f.poly([Aq6,Bq6,Cq6]); f.line(Cq6,Dq6); f.line(Aq6,Dq6); f.tick(Aq6,Bq6); f.tick(Aq6,Cq6); f.tick(Cq6,Dq6)
f.arc(Dq6,Aq6,Bq6,1.5,'$17^\\circ$',1.95)
f.vl('A',Aq6,(0,1),.3); f.vl('B',Bq6,(-1,-.6),.3); f.vl('C',Cq6,(0,-1),.3); f.vl('D',Dq6,(1,-.5),.3)
SK6=f.svg()
q('0006',tipId='ge-ik-dis',tip='İkizkenar üçgenler ve dış açı',z='orta',alt='Uzatılan Kenar ve Dış Açı',kaz='İki ikizkenar üçgende taban açıları ve dış açı ilişkisiyle tepe açısını bulur.',
 kart='K-GIK-06 (dış açı) · |AB| = |AC| = |CD|, m(ADB) = 17°',
 metin='Şekilde B, C ve D noktaları doğrusaldır ve C noktası [BD] doğru parçası üzerindedir. A noktası bu doğrunun dışında olup |AB| = |AC| = |CD| dir. Şekil ölçekli değildir. m(ADB) = 17° olduğuna göre, m(BAC) kaç derecedir?',
 dogru=112,yan=[(34,'Tepe açısını değil taban açısını (34°) bulup bırakmış.','dikkat'),(68,'İki taban açısının toplamını (68°) tepe açısı yazmış.','dikkat'),(146,'ADB açısını taban açısı sanıp 180° − 2 × 17° = 146° bulmuş.','bilgi'),(163,'180° − 17° işlemini yapıp tepe açısı yazmış.','bilgi')],
 istenen='m(BAC) açısının ölçüsü.',
 ip=['|CA| = |CD| olduğuna göre ACD üçgeninin hangi açıları eşit? ACB açısı bu üçgen için nasıl bir açı?'],
 bilgi=[IKIZ,DIS],
 ad=[A('ACD üçgenini çöz','|CA| = |CD| olduğundan CAD ve CDA açıları eşittir.','m(CAD) = m(CDA) = 17°'),A('Dış açıyı yaz','ACB, ACD üçgeninin dış açısıdır; uzak iki iç açının toplamına eşittir.','m(ACB) = 17° + 17° = 34°'),A('Taban açısını bul','|AB| = |AC| olduğundan B ve C köşelerindeki açılar eşittir.','m(ABC) = m(ACB) = 34°'),A('Tepe açısını hesapla','ABC üçgeninin iç açıları toplamı 180°’dir.','m(BAC) = 180° − 34° − 34° = 112°')],
 puf='Uzatılan taban kenarı oluşan ikinci ikizkenar üçgenin dış açısını verir: dış açı, eşit iki taban açısının toplamıdır.',sekil=SK6)

bitir_geo()
