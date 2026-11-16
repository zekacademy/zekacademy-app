"""TYT Geometri · x · şekilli sorular (kardeş yok, ipucu 1). Koordinatlar hesaplanır; cevap ve çeldirici değerleri assert edilir."""
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
def kartla(id,alt,fikir,tuzak,z,adim,tipId,tip,kalip='şekilli'):
    kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY); TIPK[tipId]=P.k
def q(no,ad,kalip='şekilli',**k): mk(P,no,ad=ad,adim=len(ad),kalip=kalip,**k)
def pol(deg,r,o=(0,0)): return (o[0]+r*cos(radians(deg)),o[1]+r*sin(radians(deg)))
def inter(p,d,q_,e):
    # p+t*d = q_+s*e
    det=d[0]*(-e[1])-d[1]*(-e[0]); t=((q_[0]-p[0])*(-e[1])-(q_[1]-p[1])*(-e[0]))/det
    return (p[0]+t*d[0],p[1]+t*d[1])
def bit(onek,adi,konukey):
    for qq in P.ANA: qq['kardes']=None
    P.yaz(os.path.join(GD,f'{onek}-1.json'),f'/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/bos-{onek}.json')
    tipler={}
    for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=TIPK[c['tipId']]))['kartlar'].append(c['id'])
    json.dump(dict(konu=adi,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 TYT Geometri çıkmış soruları (yalnız mantık), MEB 9–10. sınıf geometri müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar',f'{onek}.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler),'soru',len(P.ANA))
def tri(a,b,c,L):
    """A,B,C köşe açıları (derece); BC tabanı yatay, uzunluk L. (A,B,C) döndürür."""
    assert abs(a+b+c-180)<1e-9
    AB=L*sin(radians(c))/sin(radians(a)); return (AB*cos(radians(b)),AB*sin(radians(b))),(0.0,0.0),(float(L),0.0)
def bis(V,P1,P2):
    u=un(sub(P1,V)); v=un(sub(P2,V)); return un(add(u,v))
P=Parti('acikenar','Açı Kenar Bağıntıları','geo|Açı Kenar Bağıntıları',ders='TYT Geometri',idon='tytgeo')
UES=B('Üçgen eşitsizliği','bir üçgenin herhangi iki kenarının farkı üçüncü kenardan küçük, toplamı üçüncü kenardan büyüktür: |b − c| < a < b + c. Örnek: kenarları 3 ve 8 olan üçgende üçüncü kenar 5’ten büyük 11’den küçüktür')
AKB=B('Açı–kenar bağıntısı','üçgende büyük açının karşısındaki kenar büyük, küçük açının karşısındaki kenar küçüktür; eşit açıların karşısındaki kenarlar eşittir. Örnek: m(A) > m(B) ise |BC| > |AC| dir')
PIS=B('Kenarlara göre açı türü','en uzun kenar c olsun: a² + b² = c² ise dik, a² + b² > c² ise dar, a² + b² < c² ise geniş açılı üçgendir (üçgen eşitsizliği de sağlanmalıdır). Örnek: kenarları 4, 5, 7 olan üçgende 16 + 25 < 49 olduğundan üçgen geniş açılıdır')
IC=B('Üçgenin iç açıları','iç açıların toplamı 180°’dir. Örnek: iki açısı 50° ve 60° olan üçgenin üçüncü açısı 70°’dir')
def nokta(f,*ps):
    for p_ in ps: f.raw(f'\\fill {pt(p_)} circle (1.6pt);')

# ============ 01 · Üçgen eşitsizliği, çevre · kolay (hikâyeli) ============
konu('geo|Açı Kenar Bağıntıları','Açı Kenar Bağıntıları')
kartla('K-GAK-01','Üçüncü kenarın sınırları','İki kenarın farkı < üçüncü kenar < toplamı kuralıyla tam sayı x’in en büyük değeri bulunur ve çevre hesaplanır.','Sınırları dahil saymak (x = 19); farkı ve toplamı karıştırmak.','kolay',3,'ge-ak-esitsizlik','Üçüncü kenarın alabileceği değerler',kalip='hikâyeli')
xs=[v for v in range(1,40) if 12-7<v<12+7]
assert xs[0]==6 and xs[-1]==18 and 7+12+xs[-1]==37 and 7+12==19 and 7+12+4==23 and 7+12+12==31 and 7+12+19==38
B1,C1=(0.0,0.0),(5.2,0.0); A1=(1.5,3.3)
f=F(); f.poly([A1,B1,C1]); nokta(f,A1,B1,C1); ic=cen([A1,B1,C1])
f.sl('$7$ m',A1,B1,ic,.42); f.sl('$12$ m',A1,C1,ic,.42); f.sl('$x$ m',B1,C1,ic,.3)
f.vl('A',A1,(0,1),.3); f.vl('B',B1,(-1,-.6),.3); f.vl('C',C1,(1,-.6),.3)
SK=f.svg()
q('0001',tipId='ge-ak-esitsizlik',tip='Üçüncü kenarın alabileceği değerler',z='kolay',alt='Üçgen Eşitsizliği',kaz='Üçgen eşitsizliğiyle üçüncü kenarın sınırlarını bulup tam sayı değerli en büyük çevreyi hesaplar.',kalip='hikâyeli',
 kart='K-GAK-01 (üçgen eşitsizliği) · iki kenar verilir, en büyük çevre istenir',
 metin='Üçgen biçimli bir arsanın çevresine tel çekilecektir. Arsanın kenar uzunlukları şekilde gösterilmiştir: |AB| = 7 m ve |AC| = 12 m olup |BC| = x m uzunluğu tam sayıdır. Tel yalnızca arsanın çevresi boyunca çekilecek, başka hiçbir yere ekleme yapılmayacaktır.\nŞekil ölçekli değildir.\nBuna göre, çekilecek telin uzunluğu en çok kaç metre olabilir?',
 dogru=37,yan=[(19,'Yalnız bilinen iki kenarı (7 + 12) toplayıp x’i hiç katmamış.','dikkat'),(23,'Farkı üst sınır sanıp x < 12 − 7 = 5 almış; x = 4 ile çevre 23 bulmuş.','bilgi'),(31,'x’i en büyük kenar olan |AC| = 12 alıp 7 + 12 + 12 = 31 yazmış.','bilgi'),(38,'x < 19 sınırını dahil edip x = 19 almış (7 + 12 = 19 olunca üçgen oluşmaz).','bilgi')],
 istenen='Arsanın çevresinin alabileceği en büyük değer (m).',
 ip=['|BC| uzunluğu için hem alt hem üst sınır var. Bu sınırları iki kenarın toplamı ve farkıyla ilişkilendir; uçlar dahil mi, değil mi?'],
 bilgi=[UES],
 ad=[A('x’in sınırlarını bul','Üçüncü kenar, diğer iki kenarın farkından büyük, toplamından küçüktür.','12 − 7 < x < 12 + 7 · 5 < x < 19'),A('En büyük tam sayıyı seç','Uçlar dahil olmadığından x = 19 olamaz.','x ≤ 18'),A('Çevreyi hesapla','En büyük x ile üç kenarı topla.','7 + 12 + 18 = 37 m')],
 puf='Üçüncü kenar daima “fark < kenar < toplam” aralığındadır; uç değerler dahil değildir.',sekil=SK)

# ============ 02 · Açılardan kenar sıralaması · kolay ============
kartla('K-GAK-02','Büyük açı karşısında büyük kenar','Her açının karşısındaki kenar belirlenir; açılar küçükten büyüğe sıralanıp kenarlar aynı sırayla yazılır.','Kenarı komşu açıyla eşlemek; sıralamayı ters yazmak.','kolay',3,'ge-ak-siralama','Açılara göre kenar sıralaması')
Av,Bv,Cv=48,70,62; assert Av+Bv+Cv==180
karsi={'A':'|BC|','B':'|AC|','C':'|AB|'}
sirali=[karsi[k] for k,_ in sorted(zip('ABC',[Av,Bv,Cv]),key=lambda t:t[1])]
assert sirali==['|BC|','|AB|','|AC|']
dog='|BC| < |AB| < |AC|'
A2,B2,C2=tri(48,70,62,5.4)
f=F(); f.poly([A2,B2,C2])
f.arc(A2,B2,C2,.8,'$48^\\circ$',1.6); f.arc(B2,C2,A2,.8,'$70^\\circ$',1.55); f.arc(C2,A2,B2,.8,'$62^\\circ$',1.55)
f.vl('A',A2,(0,1),.3); f.vl('B',B2,(-1,-.6),.3); f.vl('C',C2,(1,-.6),.3)
SK=f.svg()
q('0002',tipId='ge-ak-siralama',tip='Açılara göre kenar sıralaması',z='kolay',alt='Açı–Kenar Sıralaması',kaz='Üçgende büyük açının karşısında büyük kenar bulunduğunu kullanarak kenarları sıralar.',
 kart='K-GAK-02 (açı–kenar sıralaması) · üç açı verilir, kenar sıralaması istenir',
 metin='Şekildeki ABC üçgeni, bir çatı kirişinin yandan görünüşüdür. Üçgenin köşelerindeki açıların ölçüleri m(BAC) = 48°, m(ABC) = 70° ve m(ACB) = 62° dir.\nŞekil ölçekli değildir.\nBuna göre, kirişin kenar uzunlukları arasındaki sıralama aşağıdakilerden hangisidir?',
 dogru=dog,sira=[dog,'|AB| < |AC| < |BC|','|AC| < |AB| < |BC|','|AB| < |BC| < |AC|','|BC| < |AC| < |AB|'],
 yan=[('|AB| < |AC| < |BC|','Her kenarı komşu açıyla eşleyip (A→AB, B→BC, C→CA) sıralamış.','bilgi'),('|AC| < |AB| < |BC|','Büyük açının karşısındaki kenarı küçük sanıp sıralamayı ters yazmış.','bilgi'),('|AB| < |BC| < |AC|','En büyük açıyı (B) doğru eşleyip kalan iki kenarı yanlış sırada koymuş.','dikkat'),('|BC| < |AC| < |AB|','AB kenarını B açısının, AC kenarını C açısının karşısında sanmış.','dikkat')],
 istenen='Üçgenin kenar uzunluklarının doğru sıralaması.',
 ip=['Her açının karşısındaki kenarı belirle, sonra açıları küçükten büyüğe sırala.'],
 bilgi=[AKB],
 ad=[A('Karşı kenarları bul','Bir açının karşısındaki kenar, o açının köşesini içermeyen kenardır.','A ↔ |BC| · B ↔ |AC| · C ↔ |AB|'),A('Açıları sırala','Açıları küçükten büyüğe diz.','48° < 62° < 70°'),A('Kenarları yaz','Büyük açının karşısındaki kenar büyüktür; aynı sırayı uygula.','|BC| < |AB| < |AC|')],
 puf='Önce her açının karşısındaki kenarı yaz, sonra açı sırasını kenarlara aynen aktar.',sekil=SK)

# ============ 03 · Tam sayı kenar + ikizkenar koşulu · orta (hikâyeli) ============
kartla('K-GAK-03','İkizkenar koşulu ve üçgen eşitsizliği','Hangi kenarın diğerine eşit olabileceği üçgen eşitsizliğiyle sınanır; geçerli durumda çevre hesaplanır.','Eşitlikte geçersiz durumu (5, 5, 11) seçmek; çevreyi eksik hesaplamak.','orta',4,'ge-ak-sayi','İkizkenar koşuluyla kenar ve çevre',kalip='hikâyeli')
adaylar=[v for v in range(1,40) if (v==5 or v==11) and 11-5<v<11+5]
assert adaylar==[11] and 5+11+11==27 and 5+5+11==21 and 5+11==16 and 11*2==22
Ap,Bp,Cp=(0.0,2.6),(0.0,0.0),(6.0,1.5)
f=F(); f.line(Ap,Bp); f.line(Ap,Cp); f.line(Bp,Cp); nokta(f,Ap,Bp,Cp); ic=cen([Ap,Bp,Cp])
f.sl('$5$ km',Ap,Bp,ic,.55); f.sl('$11$ km',Ap,Cp,ic,.45); f.sl('$x$ km',Bp,Cp,ic,.4)
f.vl('A',Ap,(-1,.6),.3); f.vl('B',Bp,(-1,-.6),.3); f.vl('C',Cp,(1,0),.3)
SK=f.svg()
q('0003',tipId='ge-ak-sayi',tip='İkizkenar koşuluyla kenar ve çevre',z='orta',alt='İkizkenar Koşulu',kaz='Üçgen eşitsizliğini kullanarak ikizkenar koşulunu sağlayan kenarı belirler ve çevreyi hesaplar.',kalip='hikâyeli',
 kart='K-GAK-03 (ikizkenar koşulu) · iki yol verilir, üçüncü yol ikizkenar yapar',
 metin='A, B ve C köylerini ikişer ikişer birleştiren üç düz yol, şekildeki gibi bir üçgen oluşturmaktadır. A ile B arasındaki yol 5 km, A ile C arasındaki yol 11 km, B ile C arasındaki yol ise uzunluğu tam sayı olan x km’dir. Köylerin her birinden diğerine uzaklıkların üçgeni ikizkenar yaptığı, yani üç yoldan ikisinin uzunluğunun eşit olduğu bilinmektedir.\nŞekil ölçekli değildir.\nBuna göre, üç yolun toplam uzunluğu kaç km’dir?',
 dogru=27,yan=[(11,'Yalnız x = 11’i bulup toplam uzunluğu hesaplamadan bırakmış.','dikkat'),(16,'Bilinen iki yolu (5 + 11) toplayıp x’i katmamış.','dikkat'),(21,'x = 5 alıp 5 + 5 + 11 = 21 bulmuş (5, 5, 11 ile üçgen oluşmaz).','bilgi'),(22,'Eşit iki yolu (11 + 11) toplayıp 5 km’lik yolu katmamış.','dikkat')],
 istenen='Üç yolun toplam uzunluğu (km).',
 ip=['İkizkenar olması için x hangi iki değerden biri olabilir? Bu değerlerin hangisi üçgen eşitsizliğini sağlıyor?'],
 bilgi=[UES],
 ad=[A('Adayları yaz','İki kenar eşit olacağından x, 5 ya da 11’e eşit olmalıdır.','x = 5 veya x = 11'),A('Üçgen eşitsizliğini sına','x, 11 − 5 ile 11 + 5 arasında olmalıdır.','6 < x < 16 · x = 5 olamaz · x = 11'),A('Çevreyi hesapla','Kenarlar 5, 11, 11 km.','5 + 11 + 11 = 27 km')],
 puf='İkizkenar gibi bir koşul gelince eşitlik adaylarını yaz, her adayı üçgen eşitsizliğiyle sına.',sekil=SK)

# ============ 04 · İki üçgende sıralama · orta ============
kartla('K-GAK-04','Köşegenle bölünen dörtgende en uzun kenar','Her üçgende açılardan kenar sıralaması yapılır; ortak [AC] kenarı iki sıralamayı birbirine bağlar.','Yalnız bir üçgene bakmak; ortak kenarı gözden kaçırmak.','orta',4,'ge-ak-siralama','Açılara göre kenar sıralaması')
tA=dict(BAC=40,ABC=80); tA['BCA']=180-40-80; tB=dict(CAD=55,ACD=65); tB['ADC']=180-55-65
assert tA['BCA']==60 and tB['ADC']==60
# ABC: karşı kenarlar: BC~BAC, AC~ABC, AB~BCA ; ACD: CD~CAD, AD~ACD, AC~ADC
assert tA['BAC']<tA['BCA']<tA['ABC'] and tB['CAD']<tB['ADC']<tB['ACD']   # BC<AB<AC ; CD<AC<AD
L4=5.0; Ab,Cb=(0.0,0.0),(L4,0.0)
Bb=inter(Ab,(cos(radians(-40)),sin(radians(-40))),Cb,(cos(radians(240)),sin(radians(240))))
Db=inter(Ab,(cos(radians(55)),sin(radians(55))),Cb,(cos(radians(115)),sin(radians(115))))
assert abs(ang(Ab,Bb,Cb)-40)<1e-9 and abs(ang(Bb,Ab,Cb)-80)<1e-9 and abs(ang(Ab,Cb,Db)-55)<1e-9 and abs(ang(Cb,Ab,Db)-65)<1e-9
ln_={k:dist(*v) for k,v in dict(AB=(Ab,Bb),AC=(Ab,Cb),AD=(Ab,Db),BC=(Bb,Cb),CD=(Cb,Db)).items()}
assert max(ln_,key=ln_.get)=='AD'
f=F(); f.poly([Ab,Bb,Cb,Db]); f.line(Ab,Cb)
f.arc(Ab,Bb,Cb,.7,'$40^\\circ$',1.3); f.arc(Bb,Ab,Cb,.6,'$80^\\circ$',1.2)
f.arc(Ab,Cb,Db,.7,'$55^\\circ$',1.3); f.arc(Cb,Db,Ab,.6,'$65^\\circ$',1.2)
f.vl('A',Ab,(-1,0),.3); f.vl('B',Bb,(0,-1),.3); f.vl('C',Cb,(1,0),.3); f.vl('D',Db,(0,1),.3)
SK=f.svg()
q('0004',tipId='ge-ak-siralama',tip='Açılara göre kenar sıralaması',z='orta',alt='İki Üçgende Sıralama',kaz='Köşegenle ayrılan iki üçgende açı–kenar bağıntısını birleştirerek en uzun doğru parçasını belirler.',
 kart='K-GAK-04 (iki üçgen, ortak kenar) · en uzun parça istenir',
 metin='Şekildeki ABCD dörtgeninin [AC] köşegeni çizilmiştir. m(BAC) = 40°, m(ABC) = 80°, m(CAD) = 55° ve m(ACD) = 65° dir.\nŞekil ölçekli değildir.\nBuna göre, |AB|, |AC|, |AD|, |BC| ve |CD| uzunluklarından hangisi en büyüktür?',
 dogru='|AD|',sira=['|AB|','|AC|','|AD|','|BC|','|CD|'],
 yan=[('|AB|','ABC üçgeninde 80°’lik açıya komşu AB kenarını en büyük sanmış.','bilgi'),('|AC|','Yalnız ABC üçgenine bakıp |AC|’yi en büyük bulmuş; ACD üçgeninde |AD| > |AC| olduğunu görmemiş.','dikkat'),('|BC|','En küçük açının (40°) karşısındaki kenarı en büyük sanmış.','bilgi'),('|CD|','En küçük açının (55°) karşısındaki |CD|’yi seçmiş; büyük–küçük sıralamasını ters kullanmış.','bilgi')],
 istenen='En uzun doğru parçası.',
 ip=['Her üçgende üçüncü açıyı bulup kenar sıralamasını yaz; iki üçgende ortak olan kenarı kullanarak sıralamaları birleştir.'],
 bilgi=[AKB,IC],
 ad=[A('ABC üçgenini incele','Üçüncü açıyı bul, kenarları açılara göre sırala.','m(BCA) = 60° · 40° < 60° < 80° → |BC| < |AB| < |AC|'),A('ACD üçgenini incele','Aynı işlemi ACD için yap.','m(ADC) = 60° · 55° < 60° < 65° → |CD| < |AC| < |AD|'),A('Sıralamaları birleştir','|AC| iki üçgende ortaktır; |AD| onun üstünde, |AB| ve |BC| altındadır.','|BC| < |AB| < |AC| < |AD|'),A('En büyüğü seç','|AD| tüm diğerlerinden büyüktür.','En büyük: |AD|')],
 puf='Ortak kenarı iki sıralamanın köprüsü yap: biri onun altına, diğeri üstüne yerleşir.',sekil=SK)

# ============ 05 · Geniş açılı üçgen, tam sayı kenar sayısı · zor (hikâyeli) ============
kartla('K-GAK-05','Geniş açılı üçgende kenar sayısı','Üçgen eşitsizliği aralığı bulunur; x en uzun ya da en uzun değil durumlarında a² + b² < c² koşulu ayrı ayrı yazılıp değerler sayılır.','Yalnız x’in en uzun olduğu durumu saymak; üçgen eşitsizliği aralığını unutmak.','zor',5,'ge-ak-pisagor','Geniş açılı üçgende kenar sayısı',kalip='hikâyeli')
gecerli=[v for v in range(1,40) if 9-6<v<9+6]; genis=[v for v in gecerli if (v*v>36+81) or (v*v+36<81)]; dar=[v for v in gecerli if 36+81>v*v and v*v+36>81 and v*v+81>36]
assert gecerli==list(range(4,15)) and len(gecerli)==11 and genis==[4,5,6,11,12,13,14] and len(genis)==7 and dar==[7,8,9,10] and len(dar)==4
assert len(range(3,16))==13 and len(range(1,15))==14 and len([v for v in gecerli if v*v>117])==4 and all(v*v!=117 and v*v!=45 for v in gecerli)
sc5=.45; xa=(36-81+144)/24; Ap,Bp,Cp=(xa*sc5*1.0*(12/12)*1.0,sqrt(36-xa*xa)*sc5),(0.0,0.0),(12*sc5,0.0)
Ap=(xa*sc5,sqrt(36-xa*xa)*sc5); Bp,Cp=(0.0,0.0),(12*sc5,0.0)
assert abs(dist(Ap,Bp)/sc5-6)<1e-9 and abs(dist(Ap,Cp)/sc5-9)<1e-9 and ang(Ap,Bp,Cp)>90
f=F(); f.poly([Ap,Bp,Cp]); ic=cen([Ap,Bp,Cp])
f.sl('$6$ cm',Ap,Bp,ic,.5); f.sl('$9$ cm',Ap,Cp,ic,.5); f.sl('$x$ cm',Bp,Cp,ic,.3)
f.vl('A',Ap,(0,1),.3); f.vl('B',Bp,(-1,-.6),.3); f.vl('C',Cp,(1,-.6),.3)
SK=f.svg()
q('0005',tipId='ge-ak-pisagor',tip='Geniş açılı üçgende kenar sayısı',z='zor',alt='Geniş Açılı Üçgen',kaz='Pisagor eşitsizliği ile üçgen eşitsizliğini birleştirerek geniş açılı üçgen oluşturan tam sayı kenarları sayar.',kalip='hikâyeli',
 kart='K-GAK-05 (geniş açılı üçgen) · kenarlar 6, 9 ve x',
 metin='Bir marangoz, uzunlukları 6 cm ve 9 cm olan iki çubuğu ve uzunluğu tam sayı olan x cm’lik üçüncü bir çubuğu uçlarından birleştirerek şekildeki gibi bir üçgen çerçeve yapacaktır. Çerçevenin geniş açılı bir üçgen olması isteniyor.\nŞekil ölçekli değildir.\nBuna göre, x kaç farklı tam sayı değeri alabilir?',
 dogru=7,yan=[(4,'x’in en uzun kenar olduğu durumu (x² > 117 → 11, 12, 13, 14) sayıp diğer durumu atlamış.','dikkat'),(11,'Geniş açı koşulunu uygulamadan üçgen oluşturan bütün tam sayıları (4’ten 14’e) saymış.','dikkat'),(13,'Üçgen eşitsizliğinde uç değerleri de alıp x = 3, 4, …, 15 değerlerini saymış.','bilgi'),(14,'Alt sınırı (x > 3) unutup x = 1, 2, …, 14 demiş.','bilgi')],
 istenen='x’in alabileceği tam sayı değerlerinin sayısı.',
 ip=['Üçgenin oluşması için x hangi aralıkta olmalı? Geniş açı üçgenin hangi kenarının karşısında yer alır?'],
 bilgi=[PIS,UES],
 ad=[A('Üçgen oluşma aralığı','Üçgen eşitsizliği: 9 − 6 < x < 9 + 6.','3 < x < 15 · x = 4, 5, …, 14'),A('x en uzun kenar olsun','Geniş açı: en uzun kenarın karesi diğerlerinin kareleri toplamından büyük.','x² > 6² + 9² = 117 · x = 11, 12, 13, 14'),A('9 en uzun kenar olsun','x kısa kalır; 9’un karesi 6² ve x² toplamından büyük olmalı.','81 > 36 + x² · x² < 45 · x = 4, 5, 6'),A('Sayıyı bul','İki durumun değerlerini topla.','4 + 3 = 7 değer')],
 puf='Geniş açı koşulu en uzun kenar için yazılır; bilinmeyen kenarın hem en uzun hem en uzun olmama durumunu ayrı ayrı incele.',sekil=SK)

# ============ 06 · Açı sıralaması + kenar ifadeleri · orta ============
kartla('K-GAK-06','Açı sıralamasından kenar eşitsizliği','Açı sıralaması karşıdaki kenar sıralamasına çevrilir, ifadelerle eşitsizlikler kurulur ve üçgen eşitsizliğiyle ortak çözüm sayılır.','Sıralamayı ters çevirmek; üçgen eşitsizliğini atlamak.','orta',5,'ge-ak-aci-kenar','Açı sıralamasından kenar ifadelerine',kalip='şekilli')
def say(f_): return [v for v in range(1,60) if f_(v)]
dog_=say(lambda v: 2*v+3>v+8>12 and 2*v+3<v+8+12 and v+8<2*v+3+12 and 12<2*v+3+v+8)
ters=say(lambda v: 2*v+3<v+8<12 and 2*v+3<v+8+12 and v+8<2*v+3+12 and 12<2*v+3+v+8)
assert dog_==list(range(6,17)) and len(dog_)==11 and ters==[1,2,3] and len(ters)==3
assert len(range(5,18))==13 and len(range(5,17))==12 and len(range(6,16))==10 and len(range(4,17))==13
Ap,Bp,Cp=(1.0,2.8),(0.0,0.0),(4.8,0.0)
f=F(); f.poly([Ap,Bp,Cp]); ic=cen([Ap,Bp,Cp])
f.sl('$12$',Ap,Bp,ic,.35); f.sl('$(x+8)$',Ap,Cp,ic,.55); f.sl('$(2x+3)$',Bp,Cp,ic,.4)
f.vl('A',Ap,(0,1),.3); f.vl('B',Bp,(-1,-.6),.3); f.vl('C',Cp,(1,-.6),.3)
SK=f.svg()
q('0006',tipId='ge-ak-aci-kenar',tip='Açı sıralamasından kenar ifadelerine',z='orta',alt='Açı Sıralaması ve Kenar İfadeleri',kaz='Açı sıralamasını kenar sıralamasına çevirip üçgen eşitsizliğiyle birleştirerek x’in tam sayı değerlerini sayar.',
 kart='K-GAK-06 (açı sıralaması, kenar ifadeleri) · |AB| = 12, |AC| = x + 8, |BC| = 2x + 3',
 metin='Şekildeki ABC üçgeninde |AB| = 12 cm, |AC| = (x + 8) cm ve |BC| = (2x + 3) cm dir. Üçgenin açıları arasında m(BAC) > m(ABC) > m(ACB) ilişkisi vardır.\nŞekil ölçekli değildir.\nBuna göre, x kaç farklı tam sayı değeri alabilir?',
 dogru=11,yan=[(3,'Açı sıralamasını ters (m(A) < m(B) < m(C)) uygulayıp 2x + 3 < x + 8 < 12 koşuluyla x = 1, 2, 3 bulmuş.','bilgi'),(10,'Üçgen eşitsizliğinde x < 17 yerine x < 16 alıp x = 6, …, 15 saymış.','islem'),(12,'Yalnız x + 8 > 12 koşulunu alıp x = 5, 6, …, 16 saymış (2x + 3 > x + 8 koşulunu atlamış).','dikkat'),(13,'Eşitsizlik uçlarını dahil edip x = 5, …, 17 değerlerini saymış.','bilgi')],
 istenen='x’in alabileceği tam sayı değerlerinin sayısı.',
 ip=['Büyük açının karşısındaki kenar büyük olduğuna göre, açı sıralaması kenarlar için hangi sıralamayı verir? Üçgenin var olması için gereken koşulu da ekle.'],
 bilgi=[AKB,UES],
 ad=[A('Açı sıralamasını kenara çevir','A’nın karşısı |BC|, B’nin karşısı |AC|, C’nin karşısı |AB|’dir.','|BC| > |AC| > |AB|'),A('Eşitsizlikleri kur','Kenar ifadelerini yerine yaz.','2x + 3 > x + 8 · x > 5  ve  x + 8 > 12 · x > 4'),A('Üçgen eşitsizliğini ekle','En uzun kenar diğer ikisinin toplamından küçük olmalı.','2x + 3 < (x + 8) + 12 · x < 17'),A('Değerleri say','Ortak çözüm 5 < x < 17.','x = 6, 7, …, 16 · 11 değer')],
 puf='Açı sıralaması kenar sıralamasına çevrilir; ardından üçgen eşitsizliği ek bir aralık verir, ikisinin ortak çözümü sayılır.',sekil=SK)

bit('acikenar','Açı Kenar Bağıntıları','geo|Açı Kenar Bağıntıları')
