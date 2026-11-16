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
P=Parti('deltoid','Deltoid','geo|Deltoid',ders='TYT Geometri',idon='tytgeo')
DEL=B('Deltoid','iki çift komşu kenarı eşit olan dörtgendir (|AB| = |AD|, |CB| = |CD|). Eşit kenarlı köşeleri birleştiren köşegen simetri eksenidir: diğer köşegeni dik keser ve ortalar. Alan = köşegenler çarpımı ÷ 2. Örnek: köşegenleri 10 ve 7 ise alan 35')
DAC=B('Deltoidde açılar','simetri ekseni üzerindeki köşelerdeki açıyı köşegen ikiye böler; eksenin dışındaki iki köşedeki açılar eşittir. Dörtgenin iç açıları toplamı 360°’dir. Örnek: eksendeki açılar 100° ve 60°, diğerleri eşit ise her biri (360° − 160°) ÷ 2 = 100°’dir')
PIS=B('Pisagor bağıntısı','dik üçgende dik kenarların kareleri toplamı hipotenüsün karesine eşittir. Örnek: 3, 4, 5 üçgeni için 3² + 4² = 5²')
CEV=B('Çevre','dörtgenin çevresi tüm kenar uzunlukları toplamıdır. Deltoidde iki çift kenar eşit olduğundan çevre = 2 × (bir kenar + diğer çift kenardan biri) dir. Örnek: kenarlar 5, 5, 8, 8 ise çevre 26')
def dlt(ao,bo,co,s=1,bo2=None):
    return [(0,ao*s),(-bo*s,0),(0,-co*s),(bo*s,0)]
O=(0,0)
def sl2(f,t,p,q_,ic,d=.3,fr=.3):
    m=lerp(p,q_,fr); e=un(sub(q_,p)); n=(-e[1],e[0])
    if n[0]*(m[0]-ic[0])+n[1]*(m[1]-ic[1])<0: n=(-n[0],-n[1])
    f.node(add(m,mul(n,d)),t)
konu('geo|Deltoid','Deltoid')
# ---- 01 alan · kolay
kartla('K-GDL-01','Köşegenlerden alan','Deltoidde köşegenler dik; simetri ekseni diğer köşegeni ortalar. Alan köşegenler çarpımının yarısıdır.','Alanı köşegenler çarpımı sanmak (÷ 2 unutmak); yalnız bir üçgenin alanını bulmak.','kolay',3,'ge-dl-alan','Köşegenlerden alan')
ao,bo,co=9,4,5; AC=ao+co; BD=2*bo; al=AC*BD/2; assert al==56
assert .5*ao*BD==36 and .5*co*BD==20 and ao*BD==72 and AC*BD==112
s=.3; Pt=dlt(ao,bo,co,s)
f=F(); f.poly(Pt); f.line(Pt[0],Pt[2]); f.line(Pt[1],Pt[3]); f.dik(O,Pt[3],Pt[0],.2); f.tick(Pt[1],O); f.tick(O,Pt[3])
vtx(f,'ABCD',Pt,O,.3); f.node((-.2,-.2),'$O$')
f.node((.22,ao*s/2),'$9$'); f.node((.22,-co*s/2),'$5$'); dimout(f,Pt[1],Pt[3],(0,-1),co*s+.6,'$8$')
SK=f.svg()
q('0001',tipId='ge-dl-alan',tip='Köşegenlerden alan',z='kolay',alt='Köşegenlerle Alan',kaz='Deltoidin köşegen uzunluklarından alanını hesaplar.',kalip='hikâyeli',
 kart='K-GDL-01 (köşegenlerden alan) · AO = 9, OC = 5, BD = 8',
 metin='Bir tasarımcı, şekildeki gibi deltoid biçiminde bir cam süs yapıyor. ABCD deltoidinde |AB| = |AD| ve |CB| = |CD| olup köşegenler O noktasında dik kesişmektedir. |AO| = 9 cm, |OC| = 5 cm ve |BD| = 8 cm dir. Cam, yüzey alanına göre fiyatlandırılacaktır.\nBuna göre, camın yüzey alanı kaç cm² dir?',
 dogru=56,yan=[(20,'Yalnız BCD üçgeninin alanını bulmuş (5 × 8 ÷ 2).','dikkat'),(36,'Yalnız ABD üçgeninin alanını bulmuş (9 × 8 ÷ 2).','dikkat'),(72,'Yalnız |AO| ile |BD| yi çarpmış (9 × 8); |AC| = 14 olmalı.','islem'),(112,'Köşegenleri çarpıp 2’ye bölmeyi unutmuş (14 × 8).','islem')],
 istenen='Deltoid biçimli camın alanı (cm²).',
 ip=['Alan için iki köşegenin uzunluğuna ihtiyaç var; |AC| nin tamamını nasıl bulursun?'],
 bilgi=[DEL],
 ad=[A('Köşegenleri belirle','|AC| = |AO| + |OC|, |BD| = 8 cm.','|AC| = 9 + 5 = 14'),A('Alan formülünü yaz','Köşegenleri dik kesişen dörtgenin alanı köşegenler çarpımının yarısıdır.','Alan = |AC| × |BD| ÷ 2'),A('Hesapla','Değerleri yerine koy.','14 × 8 ÷ 2 = 56 cm²')],
 puf='Köşegenleri dik kesişen dörtgenlerde (deltoid, eşkenar dörtgen) alan köşegenler çarpımının yarısıdır.',sekil=SK)

# ---- 02 çevre + alan (kenar bilgisi) · orta
kartla('K-GDL-02','Kenarlardan alan','Kenar ve BD ile iki dik üçgende Pisagor, simetri eksenini verir; alan köşegenler çarpımının yarısıdır.','Yalnız bir üçgenin alanını almak; kenarlar çarpımını alan saymak.','orta',4,'ge-dl-alan-kenar','Kenarlardan alan')
AB,CB,BDl=13,15,24; bo=12; ao=sqrt(AB**2-bo**2); co=sqrt(CB**2-bo**2); assert ao==5 and co==9; AC=14; al=AC*BDl/2; assert al==168
assert .5*ao*BDl==60 and AB*CB==195 and AB*BDl==312 and AC*BDl==336 and 2*(AB+CB)==56
s=.22; Pt=dlt(ao,bo,co,s)
assert abs(dist(Pt[0],Pt[1])/s-13)<1e-9 and abs(dist(Pt[2],Pt[1])/s-15)<1e-9
f=F(); f.poly(Pt); f.line(Pt[0],Pt[2],'dashed'); f.line(Pt[1],Pt[3],'dashed'); f.tick(Pt[0],Pt[1]); f.tick(Pt[0],Pt[3]); f.tick(Pt[2],Pt[1],2); f.tick(Pt[2],Pt[3],2)
vtx(f,'ABCD',Pt,O,.3); ic=cen(Pt); dimout(f,Pt[1],Pt[3],(0,-1),co*s+.6,'$24$')
sl2(f,'$13$',Pt[0],Pt[1],ic,.3,.28); sl2(f,'$15$',Pt[2],Pt[1],ic,.3,.28)
SK=f.svg()
q('0002',tipId='ge-dl-alan-kenar',tip='Kenarlardan alan',z='orta',alt='Kenarlarla Alan',kaz='Kenar ve köşegen uzunluklarından Pisagorla diğer köşegeni bulup deltoidin alanını hesaplar.',
 kart='K-GDL-02 (kenarlardan alan) · 13, 15, |BD| = 24',
 metin='Şekildeki ABCD deltoidinde |AB| = |AD| = 13 cm, |CB| = |CD| = 15 cm ve |BD| = 24 cm dir (şekil ölçekli değildir).\nBuna göre, ABCD deltoidinin alanı kaç cm² dir?',
 dogru=168,yan=[(60,'Yalnız ABD üçgeninin alanını bulmuş (24 × 5 ÷ 2).','dikkat'),(195,'Komşu kenarları çarpıp alan saymış (13 × 15).','bilgi'),(312,'|AB| ile |BD| yi çarpmış (13 × 24); köşegenler çarpımının yarısı gerekir.','bilgi'),(336,'|AC| = 14 ü doğru bulmuş ama köşegenler çarpımını 2’ye bölmeyi unutmuş.','islem')],
 istenen='ABCD deltoidinin alanı (cm²).',
 ip=['[AC] köşegeni [BD] yi dik ortalar; oluşan dik üçgenlerde |AO| ve |OC| yi ayrı ayrı bul.'],
 bilgi=[DEL,PIS],
 ad=[A('BD yi ortala','Simetri ekseni [BD] yi dik ortalar.','|BO| = 24 ÷ 2 = 12'),A('|AO| yu bul','ABO dik üçgeninde hipotenüs 13’tür.','|AO|² = 13² − 12² = 25 → |AO| = 5'),A('|OC| yi bul','CBO dik üçgeninde hipotenüs 15’tir.','|OC|² = 15² − 12² = 81 → |OC| = 9'),A('Alanı hesapla','|AC| = 5 + 9 = 14; alan köşegenler çarpımının yarısıdır.','14 × 24 ÷ 2 = 168 cm²')],
 puf='Deltoidin alanı için eksik köşegen parçaları, eşit kenarlardan kurulan iki dik üçgende Pisagor ile bulunur.',sekil=SK)

# ---- 03 uçurtma bağlamı · orta
kartla('K-GDL-03','Uçurtma iskeleti','Kenar çıtalar ve kısa çıtadan Pisagorla uzun çıta bulunur; toplam çıta uzunluğu kenarlar ve köşegenlerin toplamıdır.','Uzun çıtayı unutmak ya da kısa çıtayı iki kez saymak; çevreyi toplam sanmak.','orta',4,'ge-dl-ucurtma','Uçurtma iskeleti ve çıta uzunluğu')
AB,CB,BDl=20,34,32; bo=16; ao=sqrt(AB**2-bo**2); co=sqrt(CB**2-bo**2); assert ao==12 and co==30; AC=42
top=2*(AB+CB)+AC+BDl; assert top==182 and 2*(AB+CB)==108 and 2*(AB+CB)+BDl==140 and 2*(AB+CB)+AC==150 and 2*(AB+CB)+2*BDl==172
s=.1; Pt=dlt(ao,bo,co,s)
f=F(); f.poly(Pt); f.line(Pt[0],Pt[2]); f.line(Pt[1],Pt[3]); f.dik(O,Pt[3],Pt[0],.18); f.tick(Pt[0],Pt[1]); f.tick(Pt[0],Pt[3]); f.tick(Pt[2],Pt[1],2); f.tick(Pt[2],Pt[3],2)
vtx(f,'ABCD',Pt,O,.3); f.node((-.2,-.2),'$O$'); ic=cen(Pt)
sl2(f,'$20$',Pt[0],Pt[1],ic,.3,.28); sl2(f,'$34$',Pt[2],Pt[1],ic,.3,.28); dimout(f,Pt[1],Pt[3],(0,-1),co*s+.6,'$32$')
SK=f.svg()
q('0003',tipId='ge-dl-ucurtma',tip='Uçurtma iskeleti ve çıta uzunluğu',z='orta',alt='Uçurtma İskeleti',kaz='Deltoid biçimli uçurtmanın kenar uzunluklarından köşegen çıtayı bulup toplam çıta uzunluğunu hesaplar.',kalip='hikâyeli',
 kart='K-GDL-03 (uçurtma iskeleti) · 20, 34, |BD| = 32',
 metin='Deniz, şekildeki gibi deltoid biçiminde bir uçurtma yapıyor. İskeleti dört kenar çıtası ile iki köşegen çıtasından oluşuyor: kenar çıtalarının uzunlukları şekilde cm cinsinden verilmiştir, [BD] çıtasının uzunluğu şekilde verilmiştir ve [AC] çıtası [BD] ye dik olup onu ortalamaktadır; şekil ölçekli değildir. Çıtaların uçları birbirine eklenmeyecek, kesilmeden kullanılacaktır.\nBuna göre, uçurtma için toplam kaç cm çıta gerekir?',
 dogru=182,yan=[(108,'Yalnız kenar çıtalarını toplamış (2 × (20 + 34)); köşegen çıtalarını katmamış.','dikkat'),(140,'[AC] çıtasını unutmuş: 108 + 32 = 140.','dikkat'),(150,'[BD] çıtasını unutmuş: 108 + 42 = 150.','dikkat'),(172,'[AC] yerine [BD] yi iki kez saymış: 108 + 32 + 32 = 172.','dikkat')],
 istenen='Toplam çıta uzunluğu (cm).',
 ip=['Köşegen çıtasının uzunluğunu bulmak için eşit kenarlı üçgenlerden birini dik üçgen olarak düşün; hangi parçaları bulman gerekiyor?'],
 bilgi=[DEL,PIS,CEV],
 ad=[A('Kısa çıtanın yarısı','[AC], [BD] yi ortalar.','|BO| = 32 ÷ 2 = 16'),A('Uzun çıtanın parçaları','ABO ve CBO dik üçgenlerinde Pisagor uygula.','|AO|² = 20² − 16² = 144 → 12 · |OC|² = 34² − 16² = 900 → 30'),A('[AC] çıtasını bul','Parçaları topla.','|AC| = 12 + 30 = 42'),A('Toplamı hesapla','Kenar çıtaları: 20 + 20 + 34 + 34 = 108.','108 + 42 + 32 = 182 cm')],
 puf='Çıta, tel, ip gibi toplam uzunluk sorularında hangi parçaların kullanıldığını tek tek yazıp her parçayı bir kez say.',sekil=SK)

# ---- 04 açılar · orta
kartla('K-GDL-04','Deltoidde açılar','Eksen dışındaki iki açı eşittir; dörtgenin iç açıları toplamı 360°; köşegen eksendeki açıyı ikiye böler.','Köşegenin açıyı yarıladığını unutmak; B ve D açılarının eşit olduğunu görmemek.','orta',4,'ge-dl-aci','Deltoidde açılar')
A4,B4=80,115; C4=360-A4-2*B4; x4=C4/2; assert C4==50 and x4==25 and 25*2==50
assert A4/2==40 and 180-B4==65
ab=3; hA=radians(A4/2); Ap=(0,0); Bp=(-ab*sin(hA),-ab*cos(hA)); Dp=(ab*sin(hA),-ab*cos(hA))
ACl=ab*sin(radians(B4))/sin(radians(x4)); Cp=(0,-ACl)
assert abs(ang(Bp,Ap,Cp)-B4)<1e-9 and abs(ang(Cp,Bp,Dp)-C4)<1e-9 and abs(ang(Ap,Bp,Dp)-A4)<1e-9 and abs(ang(Cp,Ap,Bp)-x4)<1e-9
sc=1.0; Pt=[Ap,Bp,Cp,Dp]; M=(0,-ACl/2)
f=F(); f.poly(Pt); f.line(Ap,Cp); f.tick(Ap,Bp); f.tick(Ap,Dp); f.tick(Cp,Bp,2); f.tick(Cp,Dp,2)
f.arc(Ap,Bp,Dp,.7); f.node((.5,-1.1),'$80^\\circ$')
bd=un(add(un(sub(Ap,Bp)),un(sub(Cp,Bp)))); f.arc(Bp,Ap,Cp,.5); f.node(add(Bp,mul(bd,1.15)),'$115^\\circ$','fill=white,inner sep=1pt')
f.arc(Cp,Ap,Bp,1.0); f.node((-1.5*sin(radians(12.5)),Cp[1]+1.5*cos(radians(12.5))),'$x$')
f.vl('A',Ap,(0,1),.3); f.vl('B',Bp,(-1,0),.3); f.vl('C',Cp,(0,-1),.3); f.vl('D',Dp,(1,0),.3)
SK=f.svg()
q('0004',tipId='ge-dl-aci',tip='Deltoidde açılar',z='orta',alt='Açılar ve Simetri',kaz='Deltoidde eksen dışındaki açıların eşitliğinden ve iç açı toplamından köşegenle oluşan açıyı bulur.',
 kart='K-GDL-04 (açılar) · m(A) = 80°, m(B) = 115°',
 metin='Şekildeki ABCD deltoidinde |AB| = |AD|, |CB| = |CD|, m(BAD) = 80° ve m(ABC) = 115° dir. [AC] köşegeni çizilmiştir. Şekil ölçekli değildir.\nBuna göre, x = m(ACB) kaç derecedir?',
 dogru=25,yan=[(40,'[AC] nin A açısını ikiye böldüğünü bulmuş (m(BAC) = 40°) ama bunu x sanmış.','dikkat'),(50,'C köşesindeki açının tamamını (m(BCD) = 50°) x olarak almış; [AC] bu açıyı ikiye böler.','dikkat'),(65,'B açısının bütünlerini (180° − 115°) almış.','bilgi'),(80,'A köşesindeki açıyı x sanmış.','dikkat')],
 istenen='x = m(ACB) açısının ölçüsü.',
 ip=['Eşit kenarların karşısındaki iki açı hakkında ne biliyorsun? Dörtgenin iç açıları toplamını kullanıp C köşesindeki açıyı bul.'],
 bilgi=[DAC],
 ad=[A('D açısını yaz','|AB| = |AD| ve |CB| = |CD| olduğundan B ve D açıları eşittir.','m(ADC) = m(ABC) = 115°'),A('C açısını bul','İç açılar toplamı 360°’dir.','m(BCD) = 360° − 80° − 115° − 115° = 50°'),A('Köşegenle böl','[AC] simetri eksenidir; C açısını ikiye böler.','x = 50° ÷ 2 = 25°')],
 puf='Deltoidde simetri ekseni, üzerindeki köşelerdeki açıları ortalar; diğer iki açı eşittir.',sekil=SK)

# ---- 05 simetri / katlama · kolay
kartla('K-GDL-05','Katlama ve kenar eşitliği','Köşegen boyunca katlanınca çakışan kenarlar eşittir; cebirsel ifadeler eşitlenir ve çevre bulunur.','Yanlış kenar çiftlerini eşitlemek; çevrede bir kenarı eksik saymak; deltoidi eşkenar dörtgen sanmak.','kolay',3,'ge-dl-simetri','Simetri ve çevre')
x=5; AB5=2*x+1; AD5=x+6; CB5=3*x-2; CD5=x+8; assert AB5==AD5==11 and CB5==CD5==13 and 2*(AB5+CB5)==48
cev=2*(AB5+CB5); assert cev==48 and AB5+CB5==24 and 7+9+7+11==34 and 11+13+13==37 and 4*13==52
xw=3; assert (2*xw+1,xw+6,3*xw-2,xw+8)==(7,9,7,11)
bo5=5.5; ao5=sqrt(AB5**2-bo5**2); co5=sqrt(CB5**2-bo5**2); s=.3; Pt=dlt(ao5,bo5,co5,s)
assert abs(dist(Pt[0],Pt[1])/s-11)<1e-9 and abs(dist(Pt[2],Pt[3])/s-13)<1e-9
f=F(); f.poly(Pt); f.line(Pt[0],Pt[2],'dashed'); f.tick(Pt[0],Pt[1]); f.tick(Pt[0],Pt[3]); f.tick(Pt[2],Pt[1],2); f.tick(Pt[2],Pt[3],2)
vtx(f,'ABCD',Pt,O,.3); ic=cen(Pt)
sl2(f,'$2x+1$',Pt[0],Pt[1],ic,.5,.28); sl2(f,'$x+6$',Pt[0],Pt[3],ic,.45,.28); sl2(f,'$3x-2$',Pt[2],Pt[1],ic,.5,.28); sl2(f,'$x+8$',Pt[2],Pt[3],ic,.45,.28)
SK=f.svg()
q('0005',tipId='ge-dl-simetri',tip='Simetri ve çevre',z='kolay',alt='Katlama ve Çevre',kaz='Deltoidde köşegen boyunca çakışan kenarları eşitleyip x değerini ve çevreyi bulur.',kalip='hikâyeli',
 kart='K-GDL-05 (simetri, çevre) · 2x+1 = x+6, 3x−2 = x+8',
 metin='Zeynep, deltoid biçimli bir kâğıdı [AC] köşegeni boyunca katlayınca B ve D köşelerinin üst üste geldiğini görüyor. Kâğıdın kenar uzunlukları şekilde santimetre cinsinden verilmiştir. Zeynep, kâğıdın kenarlarına yapıştırmak için bir bant kullanacaktır.\nBuna göre, kenarlara yapıştırılacak bandın uzunluğu kaç cm dir?',
 dogru=48,yan=[(24,'Yalnız dört kenardan ikisini (11 + 13) toplayıp yarım çevreyi bulmuş.','dikkat'),(34,'|AB| = |CB| ve |AD| = |CD| gibi yanlış kenar çiftlerini eşitleyip x = 3 bulmuş: 7 + 9 + 7 + 11.','bilgi'),(37,'Çevrede |AB| yi bir kez sayıp |AD| yi katmamış (11 + 13 + 13).','dikkat'),(52,'Deltoidi eşkenar dörtgen sanıp 4 × 13 yazmış.','bilgi')],
 istenen='Dörtgenin çevresi (cm).',
 ip=['Katlanınca üst üste gelen kenarlar hangileri? Bunları eşitleyip x i bul.'],
 bilgi=[DEL,CEV],
 ad=[A('Eşit kenarları yaz','[AC] boyunca katlanınca B ile D çakışır; |AB| = |AD| ve |CB| = |CD| olur.','2x + 1 = x + 6 · 3x − 2 = x + 8'),A('x i bul','İlk denklemden x = 5 çıkar; ikinci denklem de x = 5 ile sağlanır.','x = 5 → |AB| = |AD| = 11 · |CB| = |CD| = 13'),A('Çevreyi hesapla','Dört kenarı topla.','11 + 11 + 13 + 13 = 48 cm')],
 puf='Katlanınca çakışan kenarlar eşittir; iki denklemin aynı x i vermesi çözümü doğrular.',sekil=SK)

# ---- 06 alan oranı · zor
kartla('K-GDL-06','Köşegenin böldüğü üçgenlerin alanları','BD ortak taban olduğundan ABD ve CBD üçgenlerinin alanları yükseklikleri |AO| ve |OC| ile orantılıdır.','Oranı ters yazmak; iki üçgeni eş sanmak; yalnız bir üçgenin alanını sonuç saymak.','zor',4,'ge-dl-karma','Alan oranı ve köşegen parçaları')
r1,r2=2,3; sABD=30; sCBD=sABD*r2/r1; assert sCBD==45 and sABD+sCBD==75
assert sABD*r1/r2==20 and sABD+sABD*r1/r2==50 and 2*sABD==60 and sABD*r2==90
bo6=5; ao6=2*3; co6=3*3
s=.3; Pt=dlt(6,5,9,s)
assert abs(alan([Pt[0],Pt[1],Pt[3]])/alan([Pt[2],Pt[1],Pt[3]])-2/3)<1e-9
f=F(); f.poly(Pt); f.line(Pt[0],Pt[2],'dashed'); f.line(Pt[1],Pt[3],'dashed'); f.dik(O,Pt[3],Pt[0],.2); f.tick(Pt[0],Pt[1]); f.tick(Pt[0],Pt[3]); f.tick(Pt[2],Pt[1],2); f.tick(Pt[2],Pt[3],2)
vtx(f,'ABCD',Pt,O,.3); f.node((-.2,-.22),'$O$'); f.node((.3,6*s/2),'$2k$'); f.node((.3,-9*s/2),'$3k$')
SK=f.svg()
q('0006',tipId='ge-dl-karma',tip='Alan oranı ve köşegen parçaları',z='zor',alt='Alan Oranı',kaz='Köşegen parçalarının oranından ortak tabanlı üçgenlerin alanlarını karşılaştırıp deltoidin alanını bulur.',
 kart='K-GDL-06 (alan oranı) · |AO| : |OC| = 2 : 3, A(ABD) = 30',
 metin='Şekildeki ABCD deltoidinde |AB| = |AD|, |CB| = |CD| dir ve köşegenler O noktasında dik kesişmektedir. |AO| : |OC| = 2 : 3 olup ABD üçgeninin alanı 30 cm² dir (şekil ölçekli değildir).\nBuna göre, ABCD deltoidinin alanı kaç cm² dir?',
 dogru=75,yan=[(45,'Yalnız BCD üçgeninin alanını bulmuş; deltoid iki üçgenden oluşur.','dikkat'),(50,'Oranı ters yazıp BCD nin alanını 30 × 2 ÷ 3 = 20 bulmuş.','bilgi'),(60,'ABD ve CBD üçgenlerini eş sanıp 2 × 30 yazmış.','bilgi'),(90,'Alanı oranın payıyla değil paydasıyla çarpmış: 30 × 3.','islem')],
 istenen='ABCD deltoidinin alanı (cm²).',
 ip=['ABD ve CBD üçgenlerinin ortak kenarı hangisi? Bu kenara ait yükseklikler hangi uzunluklar?'],
 bilgi=[DEL],
 ad=[A('Ortak tabanı bul','ABD ve CBD üçgenlerinin ortak kenarı [BD] dir; yükseklikleri |AO| ve |OC| dir.','h₁ = |AO| · h₂ = |OC|'),A('Alanları orantıla','Tabanı ortak üçgenlerde alanlar yüksekliklerle orantılıdır.','A(ABD) / A(CBD) = 2 / 3'),A('CBD nin alanı','Oranı yerine koy.','30 / A(CBD) = 2 / 3 → A(CBD) = 45'),A('Toplamı al','Deltoid iki üçgenin birleşimidir.','30 + 45 = 75 cm²')],
 puf='Tabanı ortak üçgenlerin alanları yükseklikleriyle orantılıdır; deltoidde bu yükseklikler köşegen parçalarıdır.',sekil=SK)
bitir_geo('deltoid','Deltoid')
