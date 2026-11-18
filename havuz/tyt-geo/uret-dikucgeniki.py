"""TYT Geometri · Dik Üçgen · ikinci paket (hafif mod; kardeş yok, ipucu 1). Koordinatlar hesaplanır, TikZ aynı değerlerden; her cevap/çeldirici assert."""
import sys,os,math,json
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
HV=os.path.join(GD,'..')
from math import sin,cos,tan,radians,degrees,atan2,sqrt,pi
P=Parti('dikucgeniki','Dik Üçgen','geo|Dik Üçgen',ders='TYT Geometri',idon='tytgeo')
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

    def olcu(s,p,q_,t,off=.4,g=None,st='thin'):
        """ölçü oku: p-q parçasına off kadar paralel, ortada etiket boşluğu; off işareti normal yönünü seçer"""
        e=un(sub(q_,p)); n=(-e[1],e[0]); sg=1 if off>0 else -1; o=abs(off)
        P1=add(p,mul(n,off)); Q1=add(q_,mul(n,off)); M=mid(P1,Q1)
        w=.115*len(t.replace('$','').replace('\\','').replace('^','').replace('{','').replace('}',''))+.12
        if g is None: g=.5*(w*abs(e[0])+.32*abs(e[1]))+.07
        L=dist(p,q_); g=min(g,L/2-.1)
        ar='{Stealth[length=1.7mm,width=1.4mm]}'
        s.o.append(f'\\draw[-{ar},{st}] {pt(sub(M,mul(e,g)))} -- {pt(P1)};')
        s.o.append(f'\\draw[-{ar},{st}] {pt(add(M,mul(e,g)))} -- {pt(Q1)};')
        for a in (p,q_): s.o.append(f'\\draw[line width=.35pt] {pt(add(a,mul(n,sg*.05)))} -- {pt(add(a,mul(n,off+sg*.1)))};')
        s.node(M,t)

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
    P.yaz(os.path.join(GD,'dikucgeniki-1.json'),'/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/dikiki/bos.json')
    tipler={}
    for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=TIPK[c['tipId']]))['kartlar'].append(c['id'])
    json.dump(dict(konu='Dik Üçgen',surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 TYT Geometri çıkmış soruları (yalnız mantık), MEB 9–10. sınıf geometri müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar','dikucgeniki.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler))

def qm(no,ad,dogru,yan,**k):
    """karışık (tam sayı / ondalık / köklü) şıklı soru: dogru=(metin,değer); yan=[((metin,değer),cel,tur)]; değere göre sıralanır"""
    D=dogru; Y=[(v,c,t) for v,c,t in yan]
    vals=[D[1]]+[y[0][1] for y in Y]; assert len(set(round(v,9) for v in vals))==5,vals
    assert len(set([D[0]]+[y[0][0] for y in Y]))==5
    sira=[t for t,_ in sorted([D]+[y[0] for y in Y],key=lambda x:x[1])]
    q(no,ad,dogru=D[0],yan=[(y[0][0],y[1],y[2]) for y in Y],sira=sira,**k)
    RANK.append(sira.index(D[0]))
RANK=[]
KY='ÖSYM 2018–2026 TYT Geometri soruları (yalnız mantık) · MEB 9–10. sınıf geometri'

PIS=B('Pisagor bağıntısı','dik üçgende dik kenarların kareleri toplamı hipotenüsün karesine eşittir. Örnek: dik kenarları 6 ve 7 olan üçgende hipotenüs √(36 + 49) = √85’tir')
OZEL=B('Özel dik üçgenler','30°-60°-90° üçgende kenarlar, açıların karşısında sırasıyla 1 : √3 : 2 oranındadır; 45°-45°-90° üçgende 1 : 1 : √2 oranındadır. Örnek: dik kenarı 5 olan ikizkenar dik üçgenin hipotenüsü 5√2’dir')
OKLID=B('Öklid bağıntıları','dik üçgende hipotenüse indirilen yükseklik hipotenüsü p ve k parçalarına ayırırsa h² = p × k ve bir dik kenarın karesi, o kenarın hipotenüs üzerindeki izdüşümü ile hipotenüsün çarpımıdır. Örnek: dik kenarın hipotenüs üzerindeki izdüşümü 4, hipotenüs 20 ise o dik kenar √80 dir')
ALAN=B('Üçgenin alanı','taban uzunluğu ile bu tabana ait yüksekliğin çarpımının yarısıdır; dik üçgende iki dik kenar birbirinin yüksekliğidir. Örnek: taban 10, yükseklik 6 olan üçgenin alanı 30’dur')
YAMUK=B('Yamuğun alanı','paralel kenarların (tabanların) toplamı ile yüksekliğin çarpımının yarısıdır; yükseklik paralel kenarlar arasındaki dik uzaklıktır. Örnek: tabanları 4 ve 10, yüksekliği 5 olan yamuğun alanı 35’tir')
PRIZ=B('Dikdörtgenler prizması','bir köşesinde buluşan üç ayrıt birbirine diktir ve bütün yüzleri dikdörtgendir. Örnek: ayrıtları 2, 3 ve 4 olan prizmanın alt yüzünün alanı 6, ön yüzünün alanı 8’dir')
def DUZ(ad): pass
GEN='Şekil ölçekli değildir.'

# =================== 01 · direk ve gölge · kolay · hikâyeli ===================
konu('geo|Dik Üçgen','Dik Üçgen')
kartla('K-GDI-01','Gölge ve yükselme açısı','Direk, gölge ve güneş ışını dik üçgen oluşturur; 60° açının komşusu bilinirken karşı kenar √3 ile çarpılarak bulunur.','Karşı ve komşu kenarı karıştırıp √3 ile bölmek; 45° kuralını uygulamak; gölgeyi direk boyu sanmak.','kolay',3,'ge-di-ozel','Özel açılı dik üçgen',kalip='hikâyeli')
s=.25; B1=(0,0); C1=(12*s,0); A1=(0,12*sqrt(3)*s)
assert abs(ang(B1,A1,C1)-90)<1e-9 and abs(ang(C1,A1,B1)-60)<1e-9 and abs(dist(A1,B1)/dist(B1,C1)-sqrt(3))<1e-9
f=F(); f.line((-.6,0),(C1[0]+.7,0),'very thick'); f.line(B1,A1,'very thick'); f.line(A1,C1,'thick'); f.dik(B1,A1,C1)
f.arc(C1,A1,B1,.6,'$60^\\circ$',1.15)
f.olcu(B1,C1,'$12$',-.7); f.olcu(B1,A1,'$x$',.6)
f.vl('A',A1,(0,1),.32); f.vl('B',B1,(-1,-1),.34); f.vl('C',C1,(1,-1),.34)
SK1=f.svg()
v=12*sqrt(3)
qm('0001',[A('Dik üçgeni belirle','Direk zemine diktir; direk, gölge ve güneş ışını dik üçgendir. |BC| = 12 m, 60° lik açının komşu dik kenarıdır; x ise bu açının karşısındaki dik kenardır.','m(ACB) = 60° · |BC| = 12 (komşu) · x (karşı)'),A('Açılara bak','Üçgenin diğer dar açısı 30° dir; kenarlar 30°-60°-90° üçgeninin oranındadır.','m(BAC) = 180° − 90° − 60° = 30°'),A('Kenarı hesapla','30°nin karşısı 1 birim ise 60°nin karşısı √3 birimdir; 12 m, 30°nin karşısıdır.','x = 12 · √3 = 12√3')],
 rk(12,3),[(rk(4,3),'12’yi √3’e bölmüş: 12 ÷ √3 = 4√3 (karşı ve komşuyu ters kullanmış).','bilgi'),(rk(6,3),'Hipotenüsü 12 sanıp 60°nin karşısını (12 · √3 ÷ 2 = 6√3) hesaplamış.','bilgi'),(rk(12,1),'Gölgeyi direk boyu sanıp 12 bulmuş.','dikkat'),(rk(12,2),'45°-45°-90° kuralını (√2) uygulamış: 12√2.','bilgi')],
 tipId='ge-di-ozel',tip='Özel açılı dik üçgen',z='kolay',alt='Gölge ve Açı',kaz='60° lik açının komşu kenarı bilinen dik üçgende özel üçgen oranıyla karşı kenarı bulur.',kalip='hikâyeli',
 kart='K-GDI-01 (gölge) · 60° ışın açısı, gölge 12',
 metin='Zemine dik olarak dikilmiş AB direğinin gölgesi, güneş ışınlarının zeminle 60° lik açı yaptığı bir anda şekildeki gibi |BC| = 12 m dir. A noktası direğin üst ucu, C noktası gölgenin ucudur ve ışın [AC] doğrultusunda gelmektedir. Zemin düzdür. '+GEN+'\nBuna göre, direğin boyu olan x kaç metredir?',
 istenen='Direğin boyu x (m).',ip=['Direk, gölge ve ışın hangi üçgeni oluşturuyor? 60° lik açının hangi kenarı biliniyor?'],bilgi=[OZEL],
 puf='Verilen açıdan üçgenin üç açısını yaz; hangi kenarın hangi açının karşısında olduğunu işaretle.',sekil=SK1)

# =================== 02 · ikizkenar çatı · kolay · hikâyeli ===================
kartla('K-GDI-02','İkizkenar üçgende alan','Yan kenar ve taban verilince yükseklik Pisagorla bulunur (7-24-25); alan taban × yükseklik ÷ 2.','Yan kenarı yükseklik sanmak; tabanın tamamını Pisagorda kullanmak; alanda yarıyı unutmak.','kolay',3,'ge-di-pisagor','Pisagor bağıntısı ve üçlüleri',kalip='hikâyeli')
s=.2; A2=(0,24*s); B2=(-7*s,0); C2=(7*s,0); assert abs(dist(A2,B2)/s-25)<1e-9 and abs(dist(A2,C2)/s-25)<1e-9
assert 24**2+7**2==25**2 and 14*24//2==168 and 25*14//2==175 and 14*7==98 and 7*24//2==84 and 25+25+14==64
f=F(); f.poly([A2,B2,C2]); f.olcu(B2,A2,'$25$',.5); f.olcu(A2,C2,'$25$',.5); f.olcu(B2,C2,'$14$',-.6)
f.vl('A',A2,(0,1),.32); f.vl('B',B2,(-1,-1),.34); f.vl('C',C2,(1,-1),.34)
SK2=f.svg()
qm('0002',[A('Yüksekliği düşün','İkizkenar üçgende tepeden tabana inen dikme tabanı iki eşit parçaya ayırır; yarım taban 7 m ve yan kenar 25 m olan dik üçgen oluşur.','yarım taban = 14 ÷ 2 = 7'),A('Pisagor’u uygula','Yan kenar hipotenüstür; yükseklik h ise h² = 25² − 7².','h² = 625 − 49 = 576 → h = 24'),A('Alanı hesapla','Taban 14 m, yükseklik 24 m.','Alan = (14 × 24) ÷ 2 = 168')],
 ('168',168),[(('64',64),'Üçgenin çevresini (25 + 25 + 14) alan sanmış.','dikkat'),(('84',84),'Yarım tabanla yüksekliği çarpıp bir kez daha ikiye bölmüş: 7 × 24 ÷ 2.','islem'),(('98',98),'Taban ile yarım tabanı çarpmış: 14 × 7.','bilgi'),(('175',175),'Yan kenarı yükseklik sanmış: 14 × 25 ÷ 2.','bilgi')],
 tipId='ge-di-pisagor',tip='Pisagor bağıntısı ve üçlüleri',z='kolay',alt='Çadır Alanı',kaz='İkizkenar üçgenin yüksekliğini Pisagor ile bulup alanını hesaplar.',kalip='hikâyeli',
 kart='K-GDI-02 (ikizkenar çadır) · 25-25-14, alan',
 metin='Bir çadırın ön yüzü, şekilde gösterilen ikizkenar ABC üçgeni biçimindeki bir bezdir: |AB| = |AC| = 25 dm ve |BC| = 14 dm dir. Bu bezin tamamı su geçirmez bir boyayla boyanacaktır. '+GEN+'\nBuna göre, boyanacak bezin alanı kaç dm² dir?',
 istenen='ABC üçgeninin alanı (dm²).',ip=['Alan formülünde hangi uzunluğa ihtiyaç var ve şekilde bu uzunluk veriliyor mu?'],bilgi=[PIS,ALAN],
 puf='Alan için gereken uzunluğun verilenlerden nasıl elde edilebileceğini düşün.',sekil=SK2)

# =================== 03 · Öklid, yükseklik · orta ===================
kartla('K-GDI-03','Hipotenüs ve bir parça verilince yükseklik','Bir dik kenarın izdüşümü ve hipotenüs bilinirse öbür parça bulunur; yükseklik iki parçanın çarpımının kareköküdür.','Parçaları karıştırmak; h² = p × c yazmak; yüksekliği parçalardan biriyle karıştırmak.','orta',3,'ge-di-oklid','Öklid bağıntıları ile yükseklik')
BH3,BC3=8,18; HC3=BC3-BH3; assert HC3==10 and BH3*HC3==80 and 80==16*5 and BH3*BC3==144 and HC3*BC3==180
s=.3; B3=(0,0); C3=(BC3*s,0); H3=(BH3*s,0); A3=(BH3*s,sqrt(80)*s)
assert abs(ang(A3,B3,C3)-90)<1e-9 and abs(dist(A3,B3)/s-12)<1e-9
kare_esit(4,5,BH3*HC3)
f=F(); f.poly([A3,B3,C3]); f.line(A3,H3); f.dik(A3,B3,C3,.2); f.dik(H3,A3,C3,.2)
f.olcu(B3,H3,'$8$',-.55); f.olcu(B3,C3,'$18$',-1.15); f.node((H3[0]-.3,A3[1]/2),'$x$')
f.vl('A',A3,(0,1),.32); f.vl('B',B3,(-1,-1),.34); f.vl('C',C3,(1,-1),.34); f.node((H3[0]+.3,-.3),'$H$')
SK3=f.svg()
qm('0003',[A('Eksik parçayı bul','Hipotenüs 18 ve |BH| = 8 olduğundan [HC] parçası kalan uzunluktur.','|HC| = 18 − 8 = 10'),A('Öklid’i yaz','Hipotenüse inen yüksekliğin karesi, hipotenüsün parçalarının çarpımına eşittir.','x² = |BH| × |HC| = 8 × 10 = 80'),A('Kökü sadeleştir','80 = 16 × 5 olduğundan karekökü 4√5 olur.','x = 4√5')],
 rk(4,5),[(rk(8,1),'Yüksekliği |BH| = 8 ile karıştırmış.','dikkat'),(rk(10,1),'Yüksekliği |HC| = 10 ile karıştırmış.','dikkat'),(rk(12,1),'x² = |BH| × |BC| = 144 yazmış; bu |AB|² dir.','bilgi'),(rk(6,5),'x² = |HC| × |BC| = 180 yazmış; bu |AC|² dir.','bilgi')],
 tipId='ge-di-oklid',tip='Öklid bağıntıları ile yükseklik',z='orta',alt='Öklid ile Yükseklik',kaz='Hipotenüs ve bir parçası verilen dik üçgende Öklid bağıntısıyla yüksekliği bulur.',
 kart='K-GDI-03 (Öklid) · BH = 8, BC = 18, AH isteniyor',
 metin='Şekildeki ABC üçgeninde m(BAC) = 90° dir. Bu üçgenin tahtadan kesilmiş bir modelinde, A köşesinden hipotenüse inen [AH] dikmesi çizilmiştir. Hipotenüs üzerindeki [BH] parçası 8 cm, hipotenüsün tamamı ise 18 cm dir. '+GEN+'\nBuna göre, |AH| = x kaç cm dir?',
 istenen='|AH| = x (cm).',ip=['[AH] hangi iki küçük dik üçgenin ortak kenarı? Bu üçgenler büyük üçgenle nasıl ilişkili?'],bilgi=[OKLID],
 puf='Önce bilinmeyen parçanın uzunluğunu bul; sonuç kök içeriyorsa karekökün içini tam kare çarpanlarına ayır.',sekil=SK3)

# =================== 04 · x, x+7, x+9 · orta ===================
kartla('K-GDI-04','Cebirsel kenarlı dik üçgen','Kenarlar x cinsinden verildiğinde Pisagor ikinci derece denklem verir; kök bulunur, alan hesaplanır.','Denklemi kurarken hipotenüsü yanlış kenar seçmek; x’i bulup alan yerine çevre vermek; yarıyı unutmak.','orta',4,'ge-di-pisagor','Pisagor bağıntısı ve üçlüleri')
x4=8; assert x4**2+(x4+7)**2==(x4+9)**2 and x4*(x4+7)//2==60 and 2*60==120 and x4*(x4+9)//2==68 and (x4+7)*(x4+9)==255 and x4+x4+7+x4+9==40
assert 2*x4*x4+14*x4+49==x4*x4+18*x4+81 and x4*x4-4*x4-32==0 and (x4-8)*(x4+4)==0
s=.3; A4=(0,0); B4=(x4*s,0); C4=(0,(x4+7)*s)
assert abs(ang(A4,B4,C4)-90)<1e-9 and abs(dist(B4,C4)/s-17)<1e-9
f=F(); f.poly([A4,B4,C4]); f.dik(A4,B4,C4,.22)
f.olcu(A4,B4,'$x$',-.5); f.olcu(A4,C4,'$x+7$',.65); f.olcu(B4,C4,'$x+9$',-.7)
f.vl('A',A4,(-1,-1),.34); f.vl('B',B4,(1,-1),.34); f.vl('C',C4,(-.2,1),.34)
SK4=f.svg()
qm('0004',[A('Pisagor’u yaz','A köşesi dik olduğundan [BC] hipotenüstür.','x² + (x + 7)² = (x + 9)²'),A('Denklemi düzenle','Parantezleri aç, benzer terimleri topla.','2x² + 14x + 49 = x² + 18x + 81 → x² − 4x − 32 = 0'),A('x’i bul','Denklem (x − 8)(x + 4) = 0 biçiminde çarpanlara ayrılır; uzunluk pozitiftir.','x = 8'),A('Alanı hesapla','Dik kenarlar 8 ve 15’tir.','Alan = (8 × 15) ÷ 2 = 60')],
 ('60',60),[(('255',255),'Dik kenar ile hipotenüsü çarpıp ikiye bölmeyi unutmuş: 15 × 17.','islem'),(('68',68),'Bir dik kenar ile hipotenüsü çarpıp ikiye bölmüş: 8 × 17 ÷ 2.','bilgi'),(('120',120),'Alan formülünde ikiye bölmeyi unutmuş: 8 × 15.','islem'),(('127,5',127.5),'Diğer dik kenar ile hipotenüsü çarpıp ikiye bölmüş: 15 × 17 ÷ 2.','bilgi')],
 tipId='ge-di-pisagor',tip='Pisagor bağıntısı ve üçlüleri',z='orta',alt='Cebirsel Kenarlar',kaz='Kenar uzunlukları cebirsel verilen dik üçgende Pisagor denklemini kurup çözerek alanı bulur.',
 kart='K-GDI-04 (x, x+7, x+9) · alan',
 metin='Şekilde, A köşesindeki açısı dik olan bir ABC üçgeninin kenar uzunlukları cm cinsinden x cinsinden verilmiştir (x > 0). '+GEN+'\nBuna göre, ABC üçgeninin alanı kaç cm² dir?',
 istenen='ABC üçgeninin alanı (cm²).',ip=['Dik açının karşısındaki kenar hangisi? Üç kenar arasında hangi bağıntı kurulabilir?'],bilgi=[PIS,ALAN],
 puf='x’i bulduktan sonra istenenin alan olduğunu unutma; kenar uzunluklarını tek tek yazarak kontrol et.',sekil=SK4)

# =================== 05 · 30°-60° iki özel üçgen · orta ===================
kartla('K-GDI-05','İki özel üçgenin birleşimi','AB ortak dik kenardır; ABD ve ABC üçgenlerinde ayrı ayrı özel üçgen oranı kullanılır, parçalar farkla bulunur.','Yanlış açının karşısındaki kenarı almak; BD ile DC’yi karıştırmak; hipotenüsü dik kenar sanmak.','orta',4,'ge-di-ozel2','Birleşik özel dik üçgenler')
AB5=6; BD5=2*sqrt(3); BC5=6*sqrt(3); DC5=4*sqrt(3)
kare_esit(2,3,12); kare_esit(4,3,48); kare_esit(6,3,108)
s=.5; B5=(0,0); A5=(0,AB5*s); C5=(BC5*s,0); D5=(BD5*s,0)
assert abs(ang(B5,A5,C5)-90)<1e-9 and abs(ang(C5,A5,B5)-30)<1e-9 and abs(ang(D5,A5,B5)-60)<1e-9 and abs(dist(D5,C5)/s-DC5)<1e-9
f=F(); f.poly([A5,B5,C5]); f.line(A5,D5); f.dik(B5,A5,C5,.22)
f.arc(C5,A5,B5,1.15,'$30^\\circ$',1.75); f.arc(D5,A5,B5,.45,'$60^\\circ$',.85)
f.olcu(B5,A5,'$6$',.5)
f.vl('A',A5,(0,1),.32); f.vl('B',B5,(-1,-1),.34); f.vl('C',C5,(1,-1),.34); f.vl('D',D5,(.1,-1),.34)
SK5=f.svg()
qm('0005',[A('ABD üçgenini çöz','ABD üçgeninde m(ADB) = 60° olduğundan 30°-60°-90° üçgenidir; 60°nin karşısı |AB| = 6 dır.','|BD| = 6 ÷ √3 = 2√3'),A('ABC üçgenini çöz','ABC üçgeninde m(ACB) = 30° dir; |AB| 30°nin karşısı olduğundan |BC| = √3 · 6 dır.','|BC| = 6√3'),A('Farkı al','D noktası [BC] üzerinde olduğundan [DC] parçası, |BC| − |BD| dir.','|DC| = 6√3 − 2√3 = 4√3')],
 rk(4,3),[(rk(2,3),'Yalnız |BD| = 2√3’ü bulup bırakmış.','dikkat'),(rk(6,1),'|AB| = 6’yı |DC| sanmış.','dikkat'),(rk(6,3),'|BC| = 6√3’ü bulup |BD|’yi çıkarmamış.','dikkat'),(rk(12,1),'|AC| = 12’yi |DC| sanmış.','dikkat')],
 tipId='ge-di-ozel2',tip='Birleşik özel dik üçgenler',z='orta',alt='İki Özel Üçgen',kaz='Ortak dik kenarlı iki özel dik üçgende uzunlukları bulup fark alarak istenen parçayı hesaplar.',
 kart='K-GDI-05 (30°-60°) · AB = 6, DC isteniyor',
 metin='Şekilde, m(ABC) = 90° olan bir ABC üçgeninin [BC] kenarı üzerinde bir D noktası alınmıştır. m(ACB) = 30°, m(ADB) = 60° ve |AB| = 6 cm dir. '+GEN+'\nBuna göre, |DC| kaç cm dir?',
 istenen='|DC| (cm).',ip=['A noktasından bakınca iki ayrı dik üçgen görüyor musun? Her birinde hangi kenar biliniyor?'],bilgi=[OZEL],
 puf='Ortak kenarı iki üçgende de kullan; bulduğun uzunlukların şekildeki hangi parçalara ait olduğunu işaretle.',sekil=SK5)

# =================== 06 · iki direk · orta · hikâyeli ===================
kartla('K-GDI-06','İki direk arasındaki tel','Yükseklik farkı ve yatay uzaklık dik kenar olur; tel hipotenüstür (12-35-37).','Boyları toplamak; yatay uzaklığı tel sanmak; dik kenarları toplamak.','orta',3,'ge-di-pisagor','Pisagor bağıntısı ve üçlüleri',kalip='hikâyeli')
h1,h2,dd=5,40,12; assert (h2-h1)**2+dd**2==37**2 and h2-h1==35 and h1+h2==45 and 35+12==47
sx=.3; sy=.1; D6=(0,0); C6=(dd*sx,0); A6=(0,h1*sy); B6=(dd*sx,h2*sy)
f=F(); f.line((-.6,0),(C6[0]+.6,0),'very thick'); f.line(D6,A6,'very thick'); f.line(C6,B6,'very thick'); f.line(A6,B6,'thick')
f.node((-.4,h1*sy/2),'$5$'); f.olcu(C6,B6,'$40$',-.6); f.olcu(D6,C6,'$12$',-.7)
f.vl('A',A6,(-.5,1),.34); f.vl('B',B6,(.5,1),.34); f.vl('D',D6,(-1,-1),.34); f.vl('C',C6,(1,-1),.34)
SK6=f.svg()
qm('0006',[A('Dik üçgeni kur','A noktasından zemine paralel bir doğru çizilirse, bu doğru [CB] direğini keser; oluşan dik üçgende telin uzunluğu hipotenüstür.','yükseklik farkı = 40 − 5 = 35 · yatay uzaklık = 12'),A('Pisagor’u uygula','Tel, dik kenarları 35 ve 12 olan üçgenin hipotenüsüdür.','|AB|² = 35² + 12² = 1225 + 144 = 1369'),A('Kökü al','37² = 1369 olduğundan tel 37 m’dir.','|AB| = 37')],
 ('37',37),[(('12',12),'Yatay uzaklığı tel uzunluğu sanmış.','dikkat'),(('35',35),'Yalnız yükseklik farkını (40 − 5) tel uzunluğu sanmış.','dikkat'),(('45',45),'Direk boylarını toplamış: 5 + 40.','bilgi'),(('47',47),'Dik kenarları toplamış: 35 + 12.','bilgi')],
 tipId='ge-di-pisagor',tip='Pisagor bağıntısı ve üçlüleri',z='orta',alt='İki Direk Arası',kaz='Zemine dik iki direğin üst uçlarını birleştiren telin uzunluğunu dik üçgen kurarak bulur.',kalip='hikâyeli',
 kart='K-GDI-06 (iki direk) · 5 m ve 40 m, 12 m aralık',
 metin='Düz bir zeminde, birbirinden 12 m uzaklıkta, zemine dik iki direk dikilmiştir. [DA] direğinin boyu 5 m, [CB] direğinin boyu 40 m dir. Direklerin üst uçları A ve B, gergin bir telle birleştirilmiştir; telin sarkması ve kalınlığı önemsizdir. '+GEN+' (Yatay ve düşey uzunluklar farklı ölçeklerle çizilmiştir.)\nBuna göre, telin uzunluğu kaç metredir?',
 istenen='|AB| telinin uzunluğu (m).',ip=['Telin uçları hangi yükseklikte? Bu iki yükseklik arasındaki fark ve yatay uzaklık bir dik üçgenin hangi kenarlarını verir?'],bilgi=[PIS],
 puf='Şekle uygun bir yardımcı doğru çizip dik üçgeni ayrı çiz; kenarlarını ayrı ayrı yaz.',sekil=SK6)

# =================== 07 · ikizkenar dik üçgen halı · orta · hikâyeli ===================
kartla('K-GDI-07','İkizkenar dik üçgende hipotenüsten alan','Hipotenüsten dik kenar √2 ile bölünerek bulunur; alan dik kenarın karesinin yarısı, yani hipotenüs² ÷ 4.','Dik kenarı hipotenüse eşit almak; kareyi unutmak; √2 ile çarpmak.','orta',3,'ge-di-ozel','Özel açılı dik üçgen',kalip='hikâyeli')
l7=7*sqrt(2); assert abs(l7*l7/2-49)<1e-9 and 14*14//2==98 and 14*14==196
s=.3; B7=(-7*s,0); C7=(7*s,0); A7=(0,7*s)
assert abs(ang(A7,B7,C7)-90)<1e-9 and abs(dist(A7,B7)-dist(A7,C7))<1e-9 and abs(dist(B7,C7)/s-14)<1e-9
f=F(); f.poly([A7,B7,C7]); f.dik(A7,B7,C7,.25); f.tick(A7,B7,1); f.tick(A7,C7,1); f.olcu(B7,C7,'$14$',-.6)
f.vl('A',A7,(0,1),.32); f.vl('B',B7,(-1,-1),.34); f.vl('C',C7,(1,-1),.34)
SK7=f.svg()
qm('0007',[A('Dik kenarı bul','İkizkenar dik üçgende açılar 45°-45°-90° dir; hipotenüs dik kenarın √2 katıdır.','|AB| = |AC| = a → 14 = a√2 → a = 7√2'),A('Alanı yaz','Dik kenarlar taban ve yüksekliktir.','Alan = (7√2 · 7√2) ÷ 2 = 98 ÷ 2'),A('Hesapla','Karekökü olan çarpım tam sayıya dönüşür.','Alan = 49')],
 ('49',49),[(('98√2',98*sqrt(2)),'Hipotenüsü 14√2 ile karıştırıp (14 × 14√2 ÷ 2) hesaplamış.','bilgi'),(('49√2',49*sqrt(2)),'Hipotenüs ile bir dik kenarı çarpıp ikiye bölmüş: 14 × 7√2 ÷ 2.','bilgi'),(('98',98),'Dik kenarı 14 alıp (14 × 14 ÷ 2) hesaplamış.','bilgi'),(('196',196),'Hipotenüsün karesini (14²) alan sanmış.','dikkat')],
 tipId='ge-di-ozel',tip='Özel açılı dik üçgen',z='orta',alt='İkizkenar Dik Üçgen Alanı',kaz='İkizkenar dik üçgende hipotenüsten dik kenarı bulup alanı hesaplar.',kalip='hikâyeli',
 kart='K-GDI-07 (45°-45°-90°) · hipotenüs 14, alan',
 metin='Dik kenarları eşit uzunlukta olan, üçgen biçimli bir halının A köşesindeki açısı diktir ve hipotenüsü olan [BC] kenarı 14 dm dir. '+GEN+'\nBuna göre, halının alanı kaç dm² dir?',
 istenen='ABC üçgeninin alanı (dm²).',ip=['Üçgenin açılarını yaz; kenarlar arasında nasıl bir oran var?'],bilgi=[OZEL,ALAN],
 puf='Dik kenarı bulmadan alan formülüne geçme; sonucu kare kökü sadeleştirerek yaz.',sekil=SK7)

# =================== 08 · 15°-75°-90° · zor ===================
kartla('K-GDI-08','15°-75°-90° üçgende yükseklik','Hipotenüse ait kenarortay çizilir; oluşan 30° lik dış açıyla yarım yükseklik özel üçgeni elde edilir.','Yüksekliği hipotenüsün yarısı sanmak; 30°-60°-90° kuralını doğrudan uygulamak; yardımcı doğruyu çizmemek.','zor',4,'ge-di-ozel2','Birleşik özel dik üçgenler')
BC8=24; s=.3; B8=(0,0); C8=(BC8*s,0); ABl=BC8*cos(radians(15)); A8=(ABl*cos(radians(15))*s,ABl*sin(radians(15))*s); H8=(A8[0],0)
assert abs(ang(A8,B8,C8)-90)<1e-9 and abs(ang(B8,A8,C8)-15)<1e-9 and abs(dist(A8,H8)/s-6)<1e-9
M8=mid(B8,C8); assert abs(dist(A8,M8)/s-12)<1e-9 and abs(ang(M8,A8,B8)-150)<1e-6 and abs(ang(M8,A8,C8)-30)<1e-6
f=F(); f.poly([A8,B8,C8]); f.line(A8,H8); f.dik(A8,B8,C8,.2); f.dik(H8,A8,C8,.14)
f.arc(B8,C8,A8,1.1,'$15^\\circ$',2.3); f.olcu(B8,C8,'$24$',-.7); f.node((H8[0]-.28,A8[1]*.55),'$x$')
f.vl('A',A8,(0,1),.32); f.vl('B',B8,(-1,-1),.34); f.vl('C',C8,(1,-1),.34); f.node((H8[0]-.1,-.33),'$H$')
SK8=f.svg()
qm('0008',[A('Hipotenüsün orta noktasını al','[BC] nin orta noktası M olsun ve [AM] çizilsin; hipotenüse ait kenarortay hipotenüsün yarısıdır, dolayısıyla M, A, B ve C köşelerine eşit uzaklıktadır.','|MA| = |MB| = |MC| = 12'),A('Dış açıyı bul','MAB üçgeni ikizkenardır; taban açıları 15° dir ve AMC açısı bunun dış açısıdır.','m(AMC) = 15° + 15° = 30°'),A('Özel üçgeni kur','AHM dik üçgeninde 30° nin karşısındaki kenar, hipotenüsün yarısıdır.','x = |AH| = |AM| ÷ 2 = 12 ÷ 2'),A('Sonucu yaz','12 nin yarısı alınır.','x = 6')],
 rk(6,1),[(rk(3,1),'Hipotenüsün yarısını iki kez yarılamış: 24 ÷ 8.','islem'),(rk(8,1),'Yüksekliği hipotenüsün üçte biri almış.','bilgi'),(rk(6,3),'30°-60°-90° kuralını (12 · √3 ÷ 2) doğrudan uygulamış.','bilgi'),(rk(12,1),'Hipotenüse ait kenarortayı (12) yükseklik sanmış.','dikkat')],
 tipId='ge-di-ozel2',tip='Birleşik özel dik üçgenler',z='zor',alt='15°-75°-90° Üçgen',kaz='15° lik açı içeren dik üçgende yardımcı doğru çizerek hipotenüse ait yüksekliği bulur.',
 kart='K-GDI-08 (15°-75°-90°) · hipotenüs 24, yükseklik',
 metin='ABC bir dik üçgendir; dik açı A köşesindedir. Bir kâğıt şeritten kesilen bu üçgenin A köşesinden karşı kenara çizilen yükseklik [AH] ile gösterilmiştir (H ∈ [BC]). Üçgenin B köşesindeki açı 15° ve hipotenüsü 24 cm uzunluğundadır. '+GEN+'\nBuna göre, |AH| = x kaç cm dir?',
 istenen='|AH| = x (cm).',ip=['15° özel üçgenlerde yok; hipotenüsün uçlarından eşit uzaklıkta olan özel bir nokta var mı?'],bilgi=[OZEL,ALAN],
 puf='Doğrudan uygulanamayan açıyı, yardımcı doğruyla özel bir açıya çevirmeyi dene; yeni oluşan üçgenlerin açılarını yaz.',sekil=SK8)

# =================== 09 · dik yamuk · zor ===================
kartla('K-GDI-09','Dik yamukta alan','Eğik kenar ve taban farkından yükseklik Pisagorla bulunur (10-24-26); alan yamuk formülüyle hesaplanır.','Eğik kenarı yükseklik sanmak; taban farkını yükseklik sanmak; ortalama yerine toplam almak.','orta',4,'ge-di-yamuk','Dik yamukta Pisagor')
AB9,DC9,BC9=8,18,26; h9=24; assert (DC9-AB9)**2+h9**2==BC9**2 and (AB9+DC9)*h9//2==312
assert (AB9+DC9)*BC9//2==338 and (DC9-AB9)*h9//2==120 and AB9*h9==192 and (AB9+DC9)*10//2==130
s=.2; D9=(0,0); A9=(0,h9*s); B9=(AB9*s,h9*s); C9=(DC9*s,0)
assert abs(dist(B9,C9)/s-26)<1e-9
f=F(); f.poly([A9,B9,C9,D9]); f.dik(A9,B9,D9,.2); f.dik(D9,A9,C9,.2)
f.olcu(A9,B9,'$8$',.55); f.olcu(D9,C9,'$18$',-.55); f.olcu(B9,C9,'$26$',.6)
f.vl('A',A9,(-1,1),.34); f.vl('B',B9,(-.5,1),.36); f.vl('C',C9,(1,-1),.34); f.vl('D',D9,(-1,-1),.34)
SK9=f.svg()
qm('0009',[A('Yardımcı dikme çiz','B noktasından [DC] ye indirilen dikmenin ayağı E olsun; ABED dikdörtgen, BEC dik üçgen olur.','|DE| = |AB| = 8 → |EC| = 18 − 8 = 10'),A('Yüksekliği bul','BEC dik üçgeninde [BC] hipotenüstür.','|BE|² = 26² − 10² = 576 → |BE| = 24'),A('Alanı yaz','Yamuğun alanı tabanlar toplamının yarısı ile yüksekliğin çarpımıdır.','Alan = ((8 + 18) ÷ 2) · 24'),A('Hesapla','13 · 24 işlemi yapılır.','Alan = 312')],
 ('312',312),[(('120',120),'Taban toplamı yerine taban farkını (10) alıp 10 · 24 ÷ 2 işlemini yapmış.','bilgi'),(('130',130),'Yüksekliği 10 (taban farkı) alıp 13 · 10 işlemini yapmış.','dikkat'),(('192',192),'Üst taban ile yüksekliği çarpmış: 8 × 24.','bilgi'),(('338',338),'Eğik kenarı yükseklik sanmış: 13 · 26.','dikkat')],
 tipId='ge-di-yamuk',tip='Dik yamukta Pisagor',z='orta',alt='Dik Yamuk',kaz='Dik yamukta yükseklik bulunup Pisagor ile yamuğun alanı hesaplanır.',
 kart='K-GDI-09 (dik yamuk) · 8, 18, 26, alan',
 metin='Şekilde, [AB] // [DC] olan ABCD yamuğunda m(DAB) = m(ADC) = 90° dir. |AB| = 8 cm, |DC| = 18 cm ve |BC| = 26 cm dir. '+GEN+'\nBuna göre, ABCD yamuğunun alanı kaç cm² dir?',
 istenen='ABCD yamuğunun alanı (cm²).',ip=['Alan formülü için hangi uzunluk eksik?'],bilgi=[YAMUK,PIS],
 puf='Eksik uzunluğu bulmak için şekildeki bilinen dik üçgenleri ya da dik açıları ara; kenarlarını ayrı ayrı yaz.',sekil=SK9)

# =================== 10 · kutu köşegeni · zor · hikâyeli ===================
kartla('K-GDI-10','Prizmanın cisim köşegeni','Önce taban köşegeni, sonra yükseklikle ikinci dik üçgen kurulur; iki kez Pisagor uygulanır.','Yüz köşegenini cisim köşegeni sanmak; üç ayrıtı toplamak; yüz köşegeninde yüksekliği unutmak.','orta',4,'ge-di-uzay','Prizmada köşegen',kalip='hikâyeli')
a10,b10,c10=12,6,4; d10=14; assert a10**2+b10**2+c10**2==d10**2 and a10**2+b10**2==180 and 180+16==196
kare_esit(6,5,180); kare_esit(4,10,160); kare_esit(2,13,52); kare_esit(2,61,244)
s=.42; W=a10*s; Hh=c10*s; dp=b10*.5*s; dx=dp*cos(radians(45)); dy=dp*sin(radians(45)); dv=(dx,dy)
A10=(0,0); B10=(W,0); E10=(0,Hh); F10=(W,Hh); D10=add(A10,dv); C10=add(B10,dv); H10=add(E10,dv); G10=add(F10,dv)
f=F()
f.poly([A10,B10,F10,E10]); f.line(B10,C10); f.line(C10,G10); f.line(G10,F10); f.line(E10,H10); f.line(H10,G10)
f.line(A10,D10,'dashed'); f.line(D10,C10,'dashed'); f.line(D10,H10,'dashed'); f.line(A10,G10,'dashed,thick')
f.olcu(A10,B10,'$12$',-.5); f.olcu(A10,E10,'$4$',.7); f.olcu(B10,C10,'$6$',-.65)
f.vl('A',A10,(-1,-1),.3); f.vl('B',B10,(-.9,-.7),.34); f.vl('C',C10,(1.2,-.2),.45); f.vl('E',E10,(-.6,1),.3); f.vl('G',G10,(.6,1),.3); f.vl('D',D10,(-.8,.5),.3)
f.node((F10[0]-.3,F10[1]-.28),'$F$')
SK10=f.svg()
qm('0010',[A('Taban köşegenini çiz','ABCD tabanında [AC] köşegeni çizilir; ABC üçgeni B de diktir.','|AC|² = 12² + 6² = 180'),A('İkinci dik üçgeni bul','[CG] ayrıtı tabana diktir; ACG üçgeni C de dik üçgendir ve [AG] hipotenüstür.','|AG|² = |AC|² + |CG|² = 180 + 4²'),A('Hesapla','Toplam 196 dır.','|AG|² = 196'),A('Kökü al','Uzunluk pozitiftir.','|AG| = 14')],
 ('14',14),[(('2√13',2*sqrt(13)),'Yalnız |AE| ve |AD|’den oluşan yüz köşegenini (√(4² + 6²)) hesaplamış.','dikkat'),(('12',12),'En uzun ayrıtı (12) çubuk uzunluğu sanmış.','dikkat'),(('4√10',4*sqrt(10)),'|AB| ve |AE|’den oluşan yüz köşegenini (√(12² + 4²)) cisim köşegeni sanmış.','dikkat'),(('6√5',6*sqrt(5)),'Taban köşegenini (√(12² + 6²)) hesaplayıp yüksekliği katmamış.','dikkat')],
 tipId='ge-di-uzay',tip='Prizmada köşegen',z='orta',alt='Kutu Köşegeni',kaz='Dikdörtgenler prizmasında iki dik üçgenle cisim köşegeninin uzunluğunu hesaplar.',kalip='hikâyeli',
 kart='K-GDI-10 (kutu) · 12 × 6 × 4, cisim köşegeni',
 metin='Dikdörtgenler prizması biçimindeki bir kutunun taban ayrıtları |AB| = 12 cm, |BC| = 6 cm ve yüksekliği |AE| = 4 cm dir. Kutunun A köşesinden G köşesine, kutunun içinden geçen düz bir çubuk gerilmiştir (kesikli çizgi). '+GEN+'\nBuna göre, çubuğun uzunluğu kaç cm dir?',
 istenen='|AG| çubuğunun uzunluğu (cm).',ip=['Çubuk bir yüzün üzerinde mi? Çubuğu hipotenüs kabul eden bir dik üçgen kurmak için hangi yardımcı doğru parçasına ihtiyaç var?'],bilgi=[PIS,PRIZ],
 puf='Gerekirse şekle bir yüz köşegeni ekle; oluşan her dik üçgeni ayrı çizip kenarlarını yaz.',sekil=SK10)

import collections
print('rank',collections.Counter(RANK))
for q_ in P.ANA: assert q_['sekil'] and len(q_['sekil'])<=40000,(q_['id'],len(q_['sekil']))
bitir_geo()
