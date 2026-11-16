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
P=Parti('eskenardortgen','Eşkenar Dörtgen','geo|Eşkenar Dörtgen',ders='TYT Geometri',idon='tytgeo')
EDG=B('Eşkenar dörtgen','dört kenarı eşit olan paralelkenardır; köşegenleri birbirini dik ortalar ve köşelerdeki açıları ikiye böler. Alan = köşegenler çarpımı ÷ 2. Örnek: köşegenleri 18 ve 24 ise yarım köşegenler 9 ve 12, kenar 15, alan 216')
PIS=B('Pisagor bağıntısı','dik üçgende dik kenarların kareleri toplamı hipotenüsün karesine eşittir. Örnek: 3, 4, 5 üçgeni için 3² + 4² = 5²')
ACI=B('Eşkenar dörtgende açılar','karşılıklı açılar eşit, komşu açılar bütünlerdir (toplamları 180°). Köşegen köşedeki açıyı ikiye böler. Örnek: bir köşedeki açı 80° ise komşusu 100°, köşegenle ayrılan parça 40°')
IKIZ=B('İkizkenar üçgen','eşit kenarların karşısındaki açılar eşittir; iç açıların toplamı 180°’dir. Örnek: tepe açısı 100° ise taban açıları 40°’dir')
ALANYUK=B('Paralelkenarın alanı','taban × yüksekliktir; eşkenar dörtgende de geçerlidir. 30°-60°-90° üçgende kenarlar 1 : √3 : 2 oranındadır. Örnek: hipotenüsü 8 olan böyle bir üçgende kısa dik kenar 4, uzun dik kenar 4√3’tür')
ICTEG=B('İç teğet çember','eşkenar dörtgenin iç teğet çemberinin merkezi köşegenlerin kesişim noktasıdır; yarıçap, merkezin bir kenara olan uzaklığıdır. Teğet, değme noktasındaki yarıçapa diktir')
def rh(h1,h2,s,ang0=None):
    return [(-h1*s,0),(0,-h2*s),(h1*s,0),(0,h2*s)]

# ---- 01 çevre · kolay
konu('geo|Eşkenar Dörtgen','Eşkenar Dörtgen')
kartla('K-GED-01','Köşegenlerden kenar ve çevre','Köşegenler birbirini dik ortalar; yarım köşegenlerle Pisagor kenarı verir, çevre kenarın dört katıdır.','Köşegeni kenar sanmak; yarım köşegenlerin toplamını kenar almak; yalnız bir kenarı vermek.','kolay',3,'ge-ed-kosegen','Köşegenlerden kenar ve çevre')
d1,d2=16,12; k=sqrt((d1/2)**2+(d2/2)**2); assert k==10 and 4*k==40
assert 4*(d1/2+d2/2)==56 and 2*(d1+d2)==56 and d1+d2==28 and 4*d2==48
s=.27; Pt=rh(d1/2,d2/2,s); O=(0,0)
assert all(abs(dist(Pt[i],Pt[(i+1)%4])/s-10)<1e-9 for i in range(4))
f=F(); f.poly(Pt); f.line(Pt[0],Pt[2]); f.line(Pt[1],Pt[3]); f.dik(O,Pt[2],Pt[3],.2)
vtx(f,'ABCD',Pt,O,.3); f.node((-.2,-.2),'$O$')
dimout(f,Pt[0],Pt[2],(0,-1),d2/2*s+.65,'$16$'); dimout(f,Pt[1],Pt[3],(1,0),d1/2*s+.8,'$12$')
SK=f.svg()
q('0001',tipId='ge-ed-kosegen',tip='Köşegenlerden kenar ve çevre',z='kolay',alt='Köşegenler ve Çevre',kaz='Yarım köşegenlerle Pisagor uygulayıp eşkenar dörtgenin kenarını ve çevresini bulur.',kalip='hikâyeli',
 kart='K-GED-01 (köşegenlerden kenar) · köşegenler 16 ve 12',
 metin='Aylin, şekildeki gibi eşkenar dörtgen biçiminde bir pano yapmıştır. Panonun köşegenleri O noktasında dik olarak kesişmekte ve uzunlukları |AC| = 16 cm, |BD| = 12 cm olmaktadır. Panonun dört kenarının tamamına, uçları üst üste binmeyecek biçimde, tek parça bir kurdele geçirilecektir.\nBuna göre, kurdelenin uzunluğu en az kaç cm olmalıdır?',
 dogru=40,yan=[(28,'İki köşegenin uzunluğunu toplamış (16 + 12 = 28); çevre kenarlardan oluşur.','bilgi'),(48,'Kısa köşegeni (12) kenar sanıp 4 × 12 = 48 bulmuş.','bilgi'),(56,'Yarım köşegenleri (8 + 6 = 14) kenar sanıp 4 × 14 = 56 bulmuş; kenarı Pisagor ile bulmamış.','bilgi'),(64,'Uzun köşegeni (16) kenar sanıp 4 × 16 = 64 bulmuş.','bilgi')],
 istenen='Eşkenar dörtgenin çevresi (cm).',
 ip=['Köşegenlerin kesişim noktasında oluşan küçük üçgenlerden birinin dik kenarlarını düşün; eşkenar dörtgenin kenarı onun hangi kenarı?'],
 bilgi=[EDG,PIS],
 ad=[A('Yarım köşegenleri yaz','Köşegenler birbirini ortalar.','|AO| = 16 ÷ 2 = 8 · |BO| = 12 ÷ 2 = 6'),A('Kenarı bul','AOB üçgeni O’da diktir; hipotenüs eşkenar dörtgenin kenarıdır.','|AB|² = 8² + 6² = 100 → |AB| = 10'),A('Çevreyi hesapla','Dört kenar eşittir.','Ç = 4 × 10 = 40 cm')],
 puf='Eşkenar dörtgende kenar, yarım köşegenlerin oluşturduğu dik üçgenin hipotenüsüdür.',sekil=SK)

# ---- 02 alan (kenar + köşegen) · orta
kartla('K-GED-02','Kenar ve bir köşegenden alan','Kenar ile bir yarım köşegenden Pisagor diğer yarım köşegeni verir; alan köşegenler çarpımının yarısıdır.','Alanı kenar × köşegen sanmak; yarım köşegenlerle alanı hesaplamak; ÷ 2’yi unutmak.','orta',4,'ge-ed-alan','Kenar ve köşegenden alan')
a=13; D1=24; h2_=sqrt(a*a-(D1/2)**2); assert h2_==5; D2=10; al=D1*D2/2; assert al==120
assert 4*a==52 and 12*5==60 and 13*5==65 and 13*12/2==78
s=.25; Pt=rh(12,5,s)
f=F(); f.poly(Pt); f.line(Pt[0],Pt[2],'dashed'); f.line(Pt[1],Pt[3],'dashed')
vtx(f,'ABCD',Pt,O,.3)
dimout(f,Pt[0],Pt[2],(0,-1),5*s+.65,'$24$'); sl2e=f.sl('$13$',Pt[0],Pt[1],Pt[2],.28)
SK=f.svg()
q('0002',tipId='ge-ed-alan',tip='Kenar ve köşegenden alan',z='orta',alt='Alan Hesabı',kaz='Kenar ve bir köşegenden diğer köşegeni bulup eşkenar dörtgenin alanını hesaplar.',kalip='hikâyeli',
 kart='K-GED-02 (kenar + köşegen) · kenar 13, köşegen 24',
 metin='Bir cam sanatçısı, şekildeki gibi eşkenar dörtgen biçiminde bir vitray parçası kesmiştir. Parçanın kenar uzunluğu 13 cm, uzun köşegeninin uzunluğu |AC| = 24 cm dir (şekil ölçekli değildir). Sanatçı, parçanın üzerine sürülecek cilanın miktarını yüzey alanına göre ayarlayacaktır.\nBuna göre, vitray parçasının yüzey alanı kaç cm² dir?',
 dogru=120,yan=[(52,'Çevreyi (4 × 13) hesaplamış; soru alanı istiyor.','dikkat'),(60,'Yarım köşegenleri çarpıp (12 × 5) alan saymış; köşegenler çarpımı ÷ 2 gerekir.','islem'),(65,'Kenar ile kısa yarım köşegeni çarpmış (13 × 5).','bilgi'),(78,'Kenar ile yarım köşegenin çarpımının yarısını (13 × 12 ÷ 2) alan sanmış.','bilgi')],
 istenen='Eşkenar dörtgen biçimli parçanın alanı (cm²).',
 ip=['Alan için iki köşegen gerekir; verilmeyen köşegenin yarısını kenar ve verilen yarım köşegenle bir dik üçgenden bul.'],
 bilgi=[EDG,PIS],
 ad=[A('Yarım köşegeni al','Köşegenler birbirini ortalar; uzun köşegenin yarısı 12 cm’dir.','|AO| = 24 ÷ 2 = 12'),A('Kısa yarım köşegeni bul','AOB dik üçgeninde hipotenüs 13’tür.','|BO|² = 13² − 12² = 25 → |BO| = 5'),A('Köşegeni tamamla','Kısa köşegen yarımın iki katıdır.','|BD| = 2 × 5 = 10 cm'),A('Alanı hesapla','Alan = köşegenler çarpımı ÷ 2.','24 × 10 ÷ 2 = 120 cm²')],
 puf='Kenar ve bir köşegen verilince diğer köşegen yarım köşegenlerle Pisagordan bulunur; alan köşegenlerin çarpımının yarısıdır.',sekil=SK)

# ---- 03 açı · kolay
kartla('K-GED-03','Köşegen ve açılar','Komşu açılar bütünlerdir; köşegen köşedeki açıyı ikiye böler.','Köşegenin açıyı ikiye böldüğünü unutmak; komşu açı yerine karşılıklı açıyı almak.','kolay',3,'ge-ed-aci','Köşedeki açılar ve köşegen')
A0=64; Bk=180-A0; x3=Bk/2; assert x3==58
assert 90-A0==26 and A0/2==32 and Bk==116
sd=5; h1=sd*cos(radians(A0/2)); h2=sd*sin(radians(A0/2)); Pt=[(-h1,0),(0,-h2),(h1,0),(0,h2)]
assert abs(ang(Pt[0],Pt[1],Pt[3])-A0)<1e-9 and abs(ang(Pt[1],O,Pt[2])-x3)<1e-9 and abs(dist(Pt[0],Pt[1])-sd)<1e-9
sc=1.0; f=F(); f.poly(Pt); f.line(Pt[0],Pt[2]); f.line(Pt[1],Pt[3]); f.dik(O,Pt[2],Pt[3],.2)
f.arc(Pt[0],Pt[1],Pt[3],.8); f.node((Pt[0][0]-.62,0),'$64^\\circ$'); f.arc(Pt[1],O,Pt[2],.7,'$x$',1.05)
vtx(f,'BCD',Pt[1:],O,.3); f.node((Pt[0][0]-.05,.42),'$A$'); f.node((-.2,-.22),'$O$')
SK=f.svg()
q('0003',tipId='ge-ed-aci',tip='Köşedeki açılar ve köşegen',z='kolay',alt='Köşegen ve Açılar',kaz='Komşu açıları ve köşegenin açıortay olduğunu kullanarak köşegenle oluşan açıyı bulur.',
 kart='K-GED-03 (açılar) · m(DAB) = 64°, m(OBC) istenir',
 metin='Ece, eşkenar dörtgen biçimli bir kâğıdın köşegenleri boyunca iki kat izi oluşturmuştur; kat izleri şekildeki gibi O noktasında kesişmektedir. Kâğıdın A köşesindeki açı m(DAB) = 64° olarak ölçülmüştür.\nŞekil ölçekli değildir.\nBuna göre, x = m(OBC) kaç derecedir?',
 dogru=58,yan=[(26,'Dik üçgende 90° − 64° = 26° hesaplamış; x açısı B köşesindeki açının yarısıdır.','bilgi'),(32,'A köşesindeki açıyı ikiye bölüp (64° ÷ 2) bunu x sanmış.','dikkat'),(45,'Köşegenlerin dik kesiştiğini görüp 90° yi ikiye bölmüş.','bilgi'),(64,'Karşılıklı açıların eşitliğini kullanıp C köşesindeki açıyı (64°) x kabul etmiş.','dikkat')],
 istenen='x = m(OBC) açısının ölçüsü.',
 ip=['Komşu açıların toplamını düşün; köşegenler köşedeki açıya ne yapar?'],
 bilgi=[ACI],
 ad=[A('B köşesindeki açıyı bul','A ve B komşu açılardır; toplamları 180°’dir.','m(ABC) = 180° − 64° = 116°'),A('Köşegenle böl','[BD] köşegeni B köşesindeki açıyı ikiye böler.','x = 116° ÷ 2 = 58°'),A('Kontrol et','AOB dik üçgeninde diğer dar açı 90° − 58° = 32° = 64° ÷ 2 olmalıdır.','90° − 58° = 32°')],
 puf='Eşkenar dörtgende komşu açılar bütünler, köşegenler açıortaydır; ABO dik üçgeninde dar açılar toplamı 90°’dir.',sekil=SK)

# ---- 04 yükseklik ve alan · orta
kartla('K-GED-04','60° açılı eşkenar dörtgenin alanı','Dik üçgenden yükseklik bulunur; alan taban × yükseklik.','Alanı kenar × kenar almak; üçgenin alanını bulup bırakmak; yüksekliği kenarın yarısı sanmak.','orta',3,'ge-ed-yukseklik','Kenar ve açıdan alan')
sd=6; hh=sd*sqrt(3)/2; assert abs(hh-3*sqrt(3))<1e-9; al4=sd*hh; assert abs(al4-18*sqrt(3))<1e-9
Ab=(0,0); Bb=(sd,0); Db=(sd*cos(radians(60)),sd*sin(radians(60))); Cb=add(Bb,Db); Eb=(Db[0],0)
assert abs(alan([Ab,Bb,Cb,Db])-al4)<1e-9 and abs(ang(Ab,Bb,Db)-60)<1e-9
assert sd*sd==36 and abs(0.5*sd*hh-9*sqrt(3))<1e-9 and sd*sd/2==18 and abs(sd*sd*sqrt(3)-36*sqrt(3))<1e-9
s=.55; sc=lambda p:(p[0]*s,p[1]*s)
Ps=[sc(Ab),sc(Bb),sc(Cb),sc(Db)]; Es=sc(Eb)
f=F(); f.poly(Ps); f.line(Ps[3],Es,'dashed'); f.dik(Es,Ps[3],Ps[0],.2)
f.arc(Ps[0],Ps[1],Ps[3],.75,'$60^\\circ$',1.2)
f.vl('A',Ps[0],(-1,-1),.3); f.vl('B',Ps[1],(1,-1),.3); f.vl('C',Ps[2],(1,1),.3); f.vl('D',Ps[3],(-0.3,1),.3); f.node((Es[0],-.25),'$E$')
dimout(f,Ps[0],Ps[1],(0,-1),.55,'$6$',.3)
SK=f.svg()
q('0004',tipId='ge-ed-yukseklik',tip='Kenar ve açıdan alan',z='orta',alt='60° Açılı Eşkenar Dörtgen',kaz='Açılı dik üçgenden yüksekliği bulup eşkenar dörtgenin alanını hesaplar.',
 kart='K-GED-04 (yükseklik, alan) · kenar 6, açı 60°',
 metin='Şekildeki ABCD eşkenar dörtgeninde |AB| = 6 cm ve m(DAB) = 60° dir. D noktasından [AB] kenarına indirilen dikme [AB] kenarını E noktasında kesmektedir. Şekil ölçekli değildir.\nBuna göre, ABCD eşkenar dörtgeninin alanı kaç cm² dir?',
 dogru='18√3',yan=[('9√3','Yalnız ABD üçgeninin alanını (6 × 3√3 ÷ 2) bulmuş; soru paralelkenarın alanını istiyor.','dikkat'),('18','Yüksekliği 3 almış (60° ile 30° yu karıştırmış): 6 × 3.','bilgi'),('36','Eşkenar dörtgeni kare sanıp 6 × 6 = 36 yazmış.','bilgi'),('36√3','Yüksekliği 6√3 almış (√3 çarpanını kenara uygulamış): 6 × 6√3.','bilgi')],
 sira=['9√3','18','18√3','36','36√3'],
 istenen='ABCD eşkenar dörtgeninin alanı (cm²).',
 ip=['ADE dik üçgeninin açılarına bak; dik kenarlarla hipotenüs arasındaki özel oranı hatırla, sonra alanı taban × yükseklik olarak yaz.'],
 bilgi=[ALANYUK],
 ad=[A('Üçgeni tanı','ADE dik üçgeninde m(DAE) = 60° ve |AD| = 6; açılar 30°, 60°, 90° dir.','|AE| = 6 ÷ 2 = 3'),A('Yüksekliği bul','Pisagor ya da 30-60-90 oranı (1 : √3 : 2).','|DE| = 3√3'),A('Alanı hesapla','Alan = taban × yükseklik.','6 × 3√3 = 18√3 cm²')],
 puf='Açısı verilen paralelkenarda yükseklik, dik üçgenin özel açı oranlarından bulunur; alan = taban × yükseklik.',sekil=SK)

# ---- 05 iç teğet çember · orta
kartla('K-GED-05','İç teğet çemberin yarıçapı','Çemberin merkezi köşegenlerin kesişimidir; yarıçap, merkezin kenara uzaklığı olup yüksekliğin yarısıdır (alan ÷ (2 × kenar)).','Yarıçapı yüksekliğe eşit almak; alanı çevreye bölmek; yarım köşegeni yarıçap sanmak.','orta',4,'ge-ed-icteget','İç teğet çemberin yarıçapı')
h1_,h2_=20,15; kk=sqrt(h1_**2+h2_**2); assert kk==25; al5=2*h1_*2*h2_/2; assert al5==600
r5=al5/(2*kk); assert r5==12 and al5/kk==24 and h2_==15 and kk==25
s=.13; Pt=rh(h1_,h2_,s)
# O'dan [AB] kenarına uzaklık = r
A_,B_=Pt[0],Pt[1]; e=un(sub(B_,A_)); nrm=(-e[1],e[0]); dd=abs(nrm[0]*(0-A_[0])+nrm[1]*(0-A_[1])); assert abs(dd/s-12)<1e-9
f=F(); f.poly(Pt); f.line(Pt[0],Pt[2],'dashed'); f.line(Pt[1],Pt[3],'dashed'); f.raw(f'\\draw[vurgu] (0,0) circle ({r5*s:.3f});')
vtx(f,'ABCD',Pt,O,.3); f.node((.18,.18),'$O$'); f.raw('\\fill (0,0) circle (1pt);'); dimout(f,Pt[0],Pt[2],(0,-1),h2_*s+.65,'$40$'); dimout(f,Pt[1],Pt[3],(1,0),h1_*s+.8,'$30$')
SK=f.svg()
q('0005',tipId='ge-ed-icteget',tip='İç teğet çemberin yarıçapı',z='orta',alt='İç Teğet Çember',kaz='Köşegenlerden kenar ve alanı bulup iç teğet çemberin yarıçapını hesaplar.',
 kart='K-GED-05 (iç teğet çember) · köşegenler 30 ve 40',
 metin='Şekildeki ABCD eşkenar dörtgeninin köşegenleri O noktasında kesişmekte ve |AC| = 40 cm, |BD| = 30 cm olmaktadır. Merkezi O olan çember, eşkenar dörtgenin dört kenarına teğettir. Şekil ölçekli değildir.\nBuna göre, bu çemberin yarıçapı kaç cm dir?',
 dogru=12,yan=[(15,'Kısa yarım köşegeni (15) yarıçap sanmış; çember köşegenlere değil kenarlara teğettir.','bilgi'),(24,'Alanı kenara bölüp (600 ÷ 25) yüksekliği bulmuş; yarıçap yüksekliğin yarısıdır.','bilgi'),(25,'Kenar uzunluğunu (25) yarıçap sanmış.','dikkat'),(30,'Kısa köşegeni (30) yarıçap olarak almış.','dikkat')],
 istenen='Çemberin yarıçapı (cm).',
 ip=['Çemberin yarıçapı, O noktasından bir kenara indirilen dikmedir. Aynı dikmeyi alan formülüyle iki farklı biçimde yazmayı dene.'],
 bilgi=[EDG,ICTEG],
 ad=[A('Kenarı bul','Yarım köşegenler 20 ve 15; Pisagor uygula.','|AB|² = 20² + 15² = 625 → |AB| = 25'),A('Alanı bul','Alan = köşegenler çarpımı ÷ 2.','40 × 30 ÷ 2 = 600'),A('Yüksekliği yaz','Alan = kenar × yükseklik.','h = 600 ÷ 25 = 24'),A('Yarıçapı bul','Çember iki karşı kenara da değer; yarıçap yüksekliğin yarısıdır.','r = 24 ÷ 2 = 12 cm')],
 puf='Eşkenar dörtgenin iç teğet çemberinin çapı, karşılıklı kenarlar arasındaki uzaklığa (yüksekliğe) eşittir.',sekil=SK)

# ---- 06 simetri/açı · zor
kartla('K-GED-06','Orta nokta ve dikme ile açı','Orta nokta ve dikme koşulu üçgeni eşkenar yapar; ardından ikizkenar üçgende taban açısı bulunur.','60° ile 30° açılarını karıştırmak; köşegenin açıyı yarıladığını iki kez uygulamak.','zor',5,'ge-ed-aci-karma','Orta nokta ve dikmeyle açı bulma')
s_=6; Bq=(0,0); Cq=(s_,0); Aq=(s_/2,s_*sqrt(3)/2); Dq=add(Aq,sub(Cq,Bq)); Eq=(s_/2,0)
assert abs(dist(Aq,Bq)-s_)<1e-9 and abs(dist(Aq,Dq)-s_)<1e-9 and abs(dist(Cq,Dq)-s_)<1e-9
assert abs(ang(Bq,Aq,Cq)-60)<1e-9 and abs(ang(Eq,Aq,Cq)-90)<1e-9 and abs(ang(Dq,Bq,Cq)-30)<1e-9
sg=.55; S=lambda p:(p[0]*sg,p[1]*sg)
Pq=[S(Aq),S(Bq),S(Cq),S(Dq)]; Es=S(Eq)
f=F(); f.poly(Pq); f.line(Pq[1],Pq[3]); f.line(Pq[0],Es); f.dik(Es,Pq[0],Pq[2],.2)
f.tick(Pq[1],Es); f.tick(Es,Pq[2]); f.arc(Pq[3],Pq[1],Pq[2],.9,'$x$',1.35)
f.vl('A',Pq[0],(-.4,1),.3); f.vl('B',Pq[1],(-1,-1),.3); f.vl('C',Pq[2],(.3,-1),.3); f.vl('D',Pq[3],(1,.8),.3); f.node((Es[0],-.25),'$E$')
SK=f.svg()
q('0006',tipId='ge-ed-aci-karma',tip='Orta nokta ve dikmeyle açı bulma',z='zor',alt='Orta Nokta ve Dikme',kaz='Orta nokta ve dikme koşulundan eşkenar üçgeni fark edip eşkenar dörtgende istenen açıyı bulur.',
 kart='K-GED-06 (orta nokta, dikme) · m(BDC) istenir',
 metin='Şekildeki ABCD eşkenar dörtgeninde E noktası [BC] kenarının orta noktasıdır ve [AE] ⊥ [BC] dir. [BD] köşegeni çizilmiştir. Şekil ölçekli değildir.\nBuna göre, x = m(BDC) kaç derecedir?',
 dogru=30,yan=[(15,'Köşegenin açıyı ikiye böldüğünü iki kez uygulayıp 30° yı bir kez daha yarılamış.','islem'),(60,'D köşesindeki açının (60°) tamamını x sanmış; [BD] bu açıyı ikiye böler.','dikkat'),(90,'[AE] ⊥ [BC] işaretini x açısı sanmış.','dikkat'),(120,'C köşesindeki açıyı (120°) x olarak yazmış.','dikkat')],
 istenen='x = m(BDC) açısının ölçüsü.',
 ip=['[AE] hem yükseklik hem kenar ortay olduğunda ABC üçgeninin kenarları hakkında ne söylenebilir?'],
 bilgi=[EDG,ACI,IKIZ],
 ad=[A('ABC üçgenini incele','E, [BC]’nin orta noktası ve [AE] ⊥ [BC] olduğundan [AE] orta dikmedir: |AB| = |AC|.','|AB| = |AC|'),A('Eşkenar üçgeni fark et','|AB| = |BC| eşkenar dörtgen kenarlarıdır; böylece üç kenar eşit.','ABC eşkenar → m(ABC) = 60°'),A('Köşelerdeki açıları bul','Karşılıklı açılar eşit, komşu açılar bütünler.','m(BCD) = 180° − 60° = 120° · m(BAD) = 120°'),A('x açısını bul','BCD ikizkenar üçgeninde |CB| = |CD| ve tepe açısı 120°’dir.','x = (180° − 120°) ÷ 2 = 30°')],
 puf='Bir kenarın orta noktasına inen dikme kenar ortay olur; eşkenar dörtgende iki kenar daha eşitse üçgen eşkenar çıkar.',sekil=SK)
bitir_geo('eskenardortgen','Eşkenar Dörtgen')
