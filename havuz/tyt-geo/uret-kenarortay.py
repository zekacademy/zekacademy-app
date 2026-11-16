"""TYT Geometri · hafif mod üretici. Şekil koordinatları hesaplanır, TikZ aynı değerlerden üretilir; her cevap ve çeldirici assert edilir."""
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
def vtx(f,P_,name,ic,d=.3): f.vl(name,P_,sub(P_,ic),d)
def tri(a,b,c,s):
    """BC=a, CA=b, AB=c → A,B,C (B orijin, BC yatay), s ölçek"""
    x=(c*c+a*a-b*b)/(2*a); y=sqrt(c*c-x*x); return (x*s,y*s),(0,0),(a*s,0)
def tri_ac(B_,C_,Bd,Cd):
    """B ve C açıları (derece) ile A (B,C yatay)"""
    a=dist(B_,C_); Ad=180-Bd-Cd; c=a*sin(radians(Cd))/sin(radians(Ad))
    return (B_[0]+c*cos(radians(Bd)),B_[1]+c*sin(radians(Bd)))
def incenter(A_,B_,C_):
    a=dist(B_,C_); b=dist(A_,C_); c=dist(A_,B_); w=a+b+c
    return ((a*A_[0]+b*B_[0]+c*C_[0])/w,(a*A_[1]+b*B_[1]+c*C_[1])/w)
def rot(p,t,o=(0,0)):
    t=radians(t); d=sub(p,o); return (o[0]+d[0]*cos(t)-d[1]*sin(t),o[1]+d[0]*sin(t)+d[1]*cos(t))
def kesis(p1,p2,p3,p4):
    x1,y1=p1;x2,y2=p2;x3,y3=p3;x4,y4=p4; d=(x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
    return (((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4))/d,((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4))/d)
TIPK={}
def konu(k,ad): P.k=k; P.konu_adi=ad; H.KONU=ad
def kartla(id,alt,fikir,tuzak,z,adim,tipId,tip):
    kart(id,alt,fikir,tuzak,z,'şekilli',adim,tipId,tip,'ÖSYM 2018–2026 TYT Geometri soruları (yalnız mantık) · MEB 9–10. sınıf geometri'); TIPK[tipId]=P.k
def q(no,ad,kalip='şekilli',**k): mk(P,no,ad=ad,adim=len(ad),kalip=kalip,**k)
def bitir_geo(onek,konuad):
    for qq in P.ANA: qq['kardes']=None
    P.yaz(os.path.join(GD,f'{onek}-1.json'),f'/tmp/bos-{onek}.json')
    tipler={}
    for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=TIPK[c['tipId']]))['kartlar'].append(c['id'])
    json.dump(dict(konu=konuad,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 TYT Geometri çıkmış soruları (yalnız mantık), MEB 9–10. sınıf geometri müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar',f'{onek}.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler))
def dim(f,p,q_,t,n,off=.6):
    """ölçü oku: p–q doğru parçasını n yönünde off kadar ötele, iki uçlu ok + ortada etiket"""
    n=un(n); p2=add(p,mul(n,off)); q2=add(q_,mul(n,off))
    f.line(p,add(p,mul(n,off+.12)),'thin'); f.line(q_,add(q_,mul(n,off+.12)),'thin')
    f.line(p2,q2,'{Stealth[length=1.6mm]}-{Stealth[length=1.6mm]}'); f.node(add(mid(p2,q2),mul(n,.24)),t)
def arct(f,V,a,b,r,n=1):
    """yay + n çentik (eş açı işareti)"""
    f.arc(V,a,b,r)
    a1=degrees(atan2(a[1]-V[1],a[0]-V[0])); a2=degrees(atan2(b[1]-V[1],b[0]-V[0])); d=(a2-a1+180)%360-180; m=radians(a1+d/2)
    e=(cos(m),sin(m)); tg=(-e[1],e[0])
    for i in range(n):
        c=add(V,mul(e,r)); c=add(c,mul(tg,(i-(n-1)/2)*.08))
        f.line(add(c,mul(e,-.07)),add(c,mul(e,.07)))
P=Parti('kenarortay','Kenarortay','geo|Kenarortay',ders='TYT Geometri',idon='tytgeo')
AGR=B('Ağırlık merkezi','üçgenin kenarortayları tek noktada (G) kesişir; G her kenarortayı köşeden başlayarak 2 : 1 oranında böler: |AG| = 2 × |GD|. Örnek: |GD| = 3 ise |AG| = 6 ve |AD| = 9')
ALAN6=B('Kenarortayların böldüğü alanlar','üç kenarortay üçgeni alanları eşit 6 küçük üçgene ayırır; her biri toplam alanın 1/6’sıdır. Bir kenarortay ise üçgeni alanları eşit iki parçaya böler')
HIP=B('Hipotenüs kenarortayı','dik üçgende hipotenüse ait kenarortay hipotenüsün yarısına eşittir; orta nokta üç köşeye eşit uzaklıktadır. Örnek: hipotenüs 10 ise kenarortay 5’tir')
PIS=B('Pisagor bağıntısı','dik üçgende dik kenarların kareleri toplamı hipotenüsün karesine eşittir. Örnek: 3, 4, 5 üçgeni için 3² + 4² = 5²')
BENZ=B('Temel benzerlik','bir kenara paralel çizilen doğru diğer kenarları orantılı böler; küçük üçgenin kenarları büyük üçgenin kenarlarıyla aynı oranda küçülür. Örnek: oran 1/2 ise paralel kenar da yarısı kadardır')

# ===== 01 · ağırlık merkezi 2:1 · kolay =====
konu('geo|Kenarortay','Kenarortay')
kartla('K-GKO-01','Ağırlık merkezinde 2:1','Kenarortay ağırlık merkezinde köşeden itibaren 2 : 1 bölünür; parçalardan tüm uzunluk bulunur.','Oranı ters yazmak; yalnız köşeye yakın parçayı vermek.','kolay',3,'ge-ko-agirlik','Ağırlık merkezinin kenarortayı bölme oranı')
GD1=6; AG1=2*GD1; AD1=3*GD1; assert AD1==18
B1=(0,0); C1=(5.6,0); A1=(1.5,4.0); D1=mid(B1,C1); E1=mid(A1,C1); G1=cen([A1,B1,C1])
assert abs(dist(A1,G1)-2*dist(G1,D1))<1e-9 and abs(kesis(A1,D1,B1,E1)[0]-G1[0])<1e-9
ic=G1; f=F(); f.poly([A1,B1,C1]); f.line(A1,D1); f.line(B1,E1); f.tick(B1,D1); f.tick(D1,C1); f.tick(A1,E1,2); f.tick(E1,C1,2)
f.sl('$6$',G1,D1,(0,0),.28) if False else None
f.node(add(mid(G1,D1),(.3,-.02)),'$6$')
for n_,p_ in (('A',A1),('B',B1),('C',C1)): vtx(f,p_,n_,cen([A1,B1,C1]))
f.vl('D',D1,(0,-1),.3); f.vl('E',E1,(1,.5),.3); f.vl('G',G1,(-1,0),.36)
SK1=f.svg()
q('0001',tipId='ge-ko-agirlik',tip='Ağırlık merkezinin kenarortayı bölme oranı',z='kolay',alt='Ağırlık Merkezi',kaz='Ağırlık merkezinin 2:1 oranını kullanarak kenarortay uzunluğunu bulur.',
 kart='K-GKO-01 (ağırlık merkezi 2:1) · |GD| = 6',
 metin='Şekilde G noktası, ABC üçgeninin ağırlık merkezidir ve D, E noktaları sırasıyla [BC] ile [AC] kenarlarının orta noktalarıdır. Şekilde gösterilen uzunluk cm cinsindendir; çentikli kenarların uzunlukları eşittir.\nBuna göre, |AD| kaç cm’dir?',
 dogru=AD1,yan=[(9,'Oranı ters kurmuş: |AG| = |GD| ÷ 2 = 3 ve |AD| = 3 + 6 = 9.','bilgi'),(12,'Yalnız |AG| = 2 × 6 = 12 uzunluğunu bulup |GD|’yi eklememiş.','dikkat'),(24,'|AD| = 2 × |AG| yazmış: 2 × 12 = 24.','bilgi'),(6,'Yalnız verilen |GD| = 6 uzunluğunu |AD| sanmış.','dikkat')],
 istenen='|AD| uzunluğu (cm).',
 ip=['G noktası [AD] kenarortayını hangi iki parçaya, hangi oranda ayırıyor? Hangi parça kısa?'],
 bilgi=[AGR],
 ad=[A('Oranı yaz','G, [AD] yi köşeden başlayarak 2 : 1 oranında böler.','|AG| : |GD| = 2 : 1'),A('|AG| uzunluğunu bul','Kısa parça |GD| = 6 olduğundan uzun parça iki katıdır.','|AG| = 2 × 6 = 12'),A('Toplam uzunluğu bul','Kenarortay iki parçanın toplamıdır.','|AD| = 12 + 6 = 18')],
 puf='Ağırlık merkezinde köşe tarafı uzun parçadır (2k), kenar tarafı kısa parçadır (k); kenarortay 3k’dır.',sekil=SK1)

# ===== 02 · alan: 6 eşit parça · kolay · hikâyeli =====
kartla('K-GKO-02','Kenarortay ve eşit alanlı parçalar','Üç kenarortay alanları eşit altı parça oluşturur; bir kenarortay da alanı ikiye böler. Taralı parçadan toplam alana, oradan istenen bölgeye gidilir.','Parça sayısını yanlış belirlemek; ABE’yi 1/3 ya da 1/4 sanmak.','kolay',3,'ge-ko-alan-alti','Kenarortayların oluşturduğu eşit alanlı parçalar')
g2=9; T2=g2*6; aABE=T2/2; assert T2==54 and aABE==27
A2=(1.4,3.9); B2=(0,0); C2=(5.8,0); D2=mid(B2,C2); E2=mid(A2,C2); F2=mid(A2,B2); G2=cen([A2,B2,C2])
assert abs(alan([G2,D2,C2])*6-alan([A2,B2,C2]))<1e-9 and abs(alan([A2,B2,E2])*2-alan([A2,B2,C2]))<1e-9
f=F(); f.fill([G2,D2,C2]); f.poly([A2,B2,C2]); f.line(A2,D2); f.line(B2,E2); f.line(C2,F2)
f.tick(B2,D2); f.tick(D2,C2); f.tick(A2,E2,2); f.tick(E2,C2,2)
for n_,p_ in (('A',A2),('B',B2),('C',C2)): vtx(f,p_,n_,G2)
f.vl('D',D2,(0,-1),.3); f.vl('E',E2,(1,.5),.3); f.vl('G',G2,(-1,0),.36)
f.node((2.9,-1.0),'Alan$(GDC)=9\\ \\mathrm{m}^2$')
SK2=f.svg()
assert sorted([9,18,27,36,54])==sorted([g2,g2*2,aABE,g2*4,T2])
q('0002',tipId='ge-ko-alan-alti',tip='Kenarortayların oluşturduğu eşit alanlı parçalar',z='kolay',kalip='hikâyeli',alt='Kenarortaylarla Alan',kaz='Kenarortayların böldüğü eşit alanlı parçalardan yararlanarak istenen bölgenin alanını bulur.',
 kart='K-GKO-02 (6 eşit parça, kenarortay alanı ikiye böler) · alan(GDC) = 9',
 metin='Üçgen biçimli ABC arsasında D ve E noktaları sırasıyla [BC] ve [AC] kenarlarının orta noktalarıdır; [AD], [BE] ve [CF] hatlarına çit çekilmiştir (F, [AB] nin orta noktasıdır). G, çitlerin kesim noktasıdır. Taralı GDC bölümünün alanı 9 m² olarak verilmiştir.\nBuna göre, ABE üçgeni biçimindeki bölümün alanı kaç m²’dir?',
 dogru=27,yan=[(9,'ABE’yi taralı bölüme eşit sanmış (tek parça).','dikkat'),(18,'ABE’yi 1/3 alan sanmış: 9 × 2 = 18.','bilgi'),(36,'ABE’yi 4 parçalık bölge sanmış: 9 × 4 = 36.','bilgi'),(54,'İstenen ABE yerine tüm arsanın alanını (9 × 6) vermiş.','dikkat')],
 istenen='ABE üçgeninin alanı (m²).',
 ip=['Üç kenarortayın ayırdığı bölgelerin alanları arasında nasıl bir ilişki var? [BE] kenarortayı ABC üçgenini nasıl böler?'],
 bilgi=[ALAN6],
 ad=[A('Tüm alanı bul','Üç kenarortay alanları eşit 6 üçgen oluşturur; taralı bölge bunlardan biridir.','alan(ABC) = 6 × 9 = 54'),A('ABE’yi yaz','[BE] kenarortayı ABC üçgenini alanları eşit iki parçaya böler.','alan(ABE) = 54 ÷ 2'),A('Hesapla','Sonuç.','alan(ABE) = 27 m²')],
 puf='Kenarortay üçgenin alanını ikiye böler; üç kenarortay ise altı eşit parça verir: bölgeleri parça sayısıyla ifade et.',sekil=SK2)

# ===== 03 · dik üçgende hipotenüs kenarortayı · kolay =====
kartla('K-GKO-03','Hipotenüs kenarortayı','Dik üçgende hipotenüsün orta noktası köşelere eşit uzaklıktadır; kenarortay hipotenüsün yarısıdır.','Kenarortayı hipotenüsün kendisi sanmak; katsayıyı iki ile çarpmak yerine yarılamak.','orta',3,'ge-ko-hipotenus','Dik üçgende hipotenüs kenarortayı')
x3=5; assert x3+2==2*x3-3==7 and 2*7==14
R3=7; A3=(-R3*.3,0); C3=(R3*.3,0)
th=radians(62); B3=(R3*.3*cos(th),R3*.3*sin(th)); D3=(0,0)
assert abs(ang(B3,A3,C3)-90)<1e-9 and abs(dist(B3,D3)-dist(A3,D3))<1e-9
f=F(); f.poly([A3,B3,C3]); f.line(B3,D3); f.dik(B3,A3,C3); f.tick(A3,D3); f.tick(D3,C3)
f.node(add(mid(B3,D3),(.45,.0)),'$x+2$'); f.node((-.95,-.3),'$2x-3$')
f.vl('A',A3,(-1,-.5),.3); f.vl('C',C3,(1,-.5),.3); f.vl('B',B3,(0,1),.3); f.vl('D',D3,(.1,-1),.3)
SK3=f.svg()
assert sorted([5,7,10.5,14,21])==sorted([x3,7,7*1.5,14,21])
q('0003',tipId='ge-ko-hipotenus',tip='Dik üçgende hipotenüs kenarortayı',z='orta',alt='Hipotenüs Kenarortayı',kaz='Dik üçgende hipotenüs kenarortayı özelliğini kullanarak denklem kurar.',
 kart='K-GKO-03 (hipotenüs kenarortayı) · BD = x + 2, AD = 2x − 3',
 metin='Şekildeki ABC üçgeninde m(ABC) = 90° ve D noktası [AC] hipotenüsünün orta noktasıdır. |BD| = x + 2 ve |AD| = 2x − 3 birimdir. Çentikli parçaların uzunlukları eşittir ve uzunluklar aynı birimle ölçülmüştür.\nBuna göre, |AC| kaç birimdir?',
 dogru=14,yan=[(5,'Bulduğu x değerini hipotenüs uzunluğu sanmış.','dikkat'),(7,'|BD| = |AD| = 7 bulup hipotenüsü değil kenarortayı vermiş.','dikkat'),(21,'|AC| = 3 × |BD| = 21 yazmış.','bilgi'),(10.5,'|AC| = 1,5 × |BD| = 10,5 yazmış (kenarortayın hipotenüsün yarısı olduğunu karıştırmış).','bilgi')],
 istenen='|AC| uzunluğu.',
 ip=['Dik üçgende hipotenüsün orta noktası, üç köşeye de aynı uzaklıktadır. Hangi iki uzunluk eşit olur?'],
 bilgi=[HIP],
 ad=[A('Eşitliği yaz','Hipotenüsün orta noktası köşelere eşit uzaklıktadır: |BD| = |AD| = |DC|.','x + 2 = 2x − 3'),A('x’i bul','Bilinmeyenleri bir tarafa topla.','x = 5 → |BD| = 7'),A('Hipotenüsü hesapla','|AC| = |AD| + |DC| = 2 × |BD|.','|AC| = 2 × 7 = 14')],
 puf='Dik üçgende hipotenüs kenarortayı hipotenüsün yarısıdır: kenarortay uzunluğunu bulunca ikiyle çarp.',sekil=SK3)

# ===== 04 · ağırlık merkezinden paralel · orta =====
kartla('K-GKO-04','Ağırlık merkezinden paralel','Ağırlık merkezi tabana 2/3 oranında yaklaşır; paralel doğru benzer küçük üçgen verir ve oran 2/3 olur.','1/3 ya da 1/2 oranını kullanmak; AG yerine GM oranını almak.','orta',3,'ge-ko-paralel','Ağırlık merkezinden tabana paralel')
BC4=18; A4=(2.0,3.6); B4=(0,0); C4=(5.4,0); M4=mid(B4,C4); G4=cen([A4,B4,C4])
D4=kesis(A4,B4,G4,add(G4,(1,0))); E4=kesis(A4,C4,G4,add(G4,(1,0)))
assert abs(dist(D4,E4)/dist(B4,C4)-2/3)<1e-9
ic=G4; f=F(); f.poly([A4,B4,C4]); f.line(A4,M4); f.line(D4,E4); f.tick(B4,M4); f.tick(M4,C4); f.par(D4,lerp(D4,E4,.5)); f.par(lerp(B4,C4,.85),C4)
dim(f,B4,C4,'$18$',(0,-1),.75)
f.vl('A',A4,(0,1),.3); f.vl('B',B4,(-1,-.5),.3); f.vl('C',C4,(1,-.5),.3); f.vl('M',M4,(.1,1),.3) if False else f.vl('M',M4,(0,-1),.3); f.vl('D',D4,(-1,.1),.3); f.vl('E',E4,(1,.1),.3); f.vl('G',G4,(.7,-.4),.28)
SK4=f.svg()
assert sorted([12,13.5,18,27,36])==sorted([BC4*2/3,BC4*3/4,BC4,BC4*3/2,BC4*2])
q('0004',tipId='ge-ko-paralel',tip='Ağırlık merkezinden tabana paralel',z='orta',alt='Ağırlık Merkezi ve Paralel',kaz='Ağırlık merkezinden tabana çizilen paralelin uzunluğunu benzerlikle bulur.',
 kart='K-GKO-04 (ağırlık merkezinden paralel) · |BC| = 18',
 metin='Şekilde G noktası, ABC üçgeninin ağırlık merkezidir ve M, [BC] nin orta noktasıdır. G noktasından [BC] kenarına çizilen paralel doğru [AB] yi D, [AC] yi E noktasında kesmektedir. Şekil ölçekli değildir; uzunluk cm cinsindendir.\nBuna göre, |DE| kaç cm’dir?',
 dogru=12,yan=[(27,'Oranı ters yazmış: |BC| × |AM| / |AG| = 18 × 3 ÷ 2 = 27.','dikkat'),(36,'Paralel doğru tabanın iki katı sanılmış: 2 × 18 = 36.','dikkat'),(13.5,'Oran olarak 3/4 almış: |DE| = 18 × 3 ÷ 4.','bilgi'),(18,'Paralel doğruyu tabana eşit sanmış: |DE| = |BC|.','dikkat')],
 istenen='|DE| uzunluğu (cm).',
 ip=['ADE ve ABC üçgenleri benzerdir. Benzerlik oranı, A köşesinden G’ye ve M’ye olan uzaklıkların oranıdır; ağırlık merkezi [AM] yi nasıl böler?'],
 bilgi=[AGR,BENZ],
 ad=[A('Benzerliği kur','[DE] // [BC] olduğundan ADE ve ABC üçgenleri benzerdir.','|DE| / |BC| = |AG| / |AM|'),A('Oranı bul','G, [AM] yi 2 : 1 böler; |AG| = 2k, |AM| = 3k.','|AG| / |AM| = 2 / 3'),A('Uzunluğu hesapla','Oranı |BC| ile çarp.','|DE| = 18 × 2 ÷ 3 = 12')],
 puf='Ağırlık merkezinden tabana çizilen paralel tabanın 2/3’ü kadardır (tepeden G’ye 2, G’den tabana 1 parça).',sekil=SK4)

# ===== 05 · iki kenarortayın oluşturduğu dörtgenin alanı · orta =====
kartla('K-GKO-05','Dörtgen bölgenin alanı','İki kenarortayın kesişiminde oluşan dörtgen, 6 eşit parçadan 2’sini kapsar; toplam alan oradan bulunur.','Dörtgeni 3 parçadan biri saymak; parça sayısını yanlış belirlemek.','orta',3,'ge-ko-alan-bolge','İki kenarortaydan oluşan bölgenin alanı')
AF5=14; T5=AF5*3; assert T5==42 and AF5==T5/3
A5=(1.6,4.0); B5=(0,0); C5=(5.7,0); E5=mid(A5,C5); F5=mid(A5,B5); G5=cen([A5,B5,C5])
assert abs(alan([A5,F5,G5,E5])*3-alan([A5,B5,C5]))<1e-9
f=F(); f.fill([A5,F5,G5,E5]); f.poly([A5,B5,C5]); f.line(B5,E5); f.line(C5,F5); f.tick(A5,F5); f.tick(F5,B5); f.tick(A5,E5,2); f.tick(E5,C5,2)
ic=cen([A5,B5,C5])
for n_,p_ in (('A',A5),('B',B5),('C',C5)): vtx(f,p_,n_,ic)
f.vl('F',F5,(-1,.3),.3); f.vl('E',E5,(1,.3),.3); f.vl('G',G5,(.1,-1),.28)
f.node((2.8,-.9),'Alan$(AFGE)=14\\ \\mathrm{cm}^2$')
SK5=f.svg()
assert sorted([7,14,21,28,42])==sorted([AF5/2,AF5,AF5*1.5,AF5*2,T5])
q('0005',tipId='ge-ko-alan-bolge',tip='İki kenarortaydan oluşan bölgenin alanı',z='orta',alt='Alan Bölgeleri',kaz='İki kenarortayın ayırdığı dörtgenin alanından üçgenin alanını bulur.',
 kart='K-GKO-05 (6 eşit parça, dörtgen bölge) · alan(AFGE) = 14',
 metin='Şekilde [BE] ve [CF] kenarortaylarının kesim noktası G, ABC üçgeninin ağırlık merkezidir. Taralı AFGE dörtgeninin alanı 14 cm² dir. |AF| = |FB| ve |AE| = |EC| olduğu çentiklerle gösterilmiştir. Buna göre, ABC üçgeninin alanı kaç cm²’dir?',
 dogru=42,yan=[(7,'Dörtgeni üçgenin parçası sanmayıp tersine 14 ÷ 2 = 7 işlemini yapmış.','dikkat'),(14,'Taralı dörtgenin alanını ABC üçgeninin alanı sanmış.','dikkat'),(21,'Dörtgeni toplam alanın 2/3’ü sanmış: 14 × 1,5 = 21.','bilgi'),(28,'Dörtgenin üçgenin yarısı olduğunu düşünüp 14 × 2 = 28 yazmış.','bilgi')],
 istenen='ABC üçgeninin alanı (cm²).',
 ip=['Ağırlık merkezinden köşelere çizilen doğrular üçgenin bölgelerinin alanlarını nasıl etkiler? Taralı bölgenin tüm alana oranını düşün.'],
 bilgi=[ALAN6],
 ad=[A('Altı parçayı düşün','AG doğrusu çizilince üçgen eşit alanlı 6 küçük üçgene bölünür; her biri toplamın 1/6’sıdır.','6 eş parça'),A('Taralı bölgeyi say','AFGE dörtgeni, AFG ve AGE üçgenlerinden oluşur.','AFGE = 2 parça = toplamın 2/6’sı = 1/3’ü'),A('Toplamı bul','Dörtgen toplam alanın 1/3’üne eşittir.','14 × 3 = 42')],
 puf='İki kenarortayın ayırdığı dörtgen, üçgenin tam 1/3’üdür (iki altılık parça).',sekil=SK5)

# ===== 06 · dik üçgen + ağırlık merkezi · zor =====
kartla('K-GKO-06','Dik üçgende ağırlık merkezi','Ağırlık merkezi 2:1 ile hipotenüs kenarortayı bulunur; hipotenüs 2 katıdır; Pisagor ile diğer dik kenar hesaplanır.','Kenarortayı hipotenüs sanmak; 2:1 oranını yanlış yönde uygulamak.','zor',4,'ge-ko-agirlik-hipotenus','Dik üçgende ağırlık merkezi ve Pisagor')
BG6=10; BD6=15; AC6=30; AB6=18; BC6=24; assert BD6==BG6*3//2 and AB6**2+BC6**2==AC6**2
s=.2; B6=(0,0); A6=(0,20*s); C6=(21*s,0); D6=mid(A6,C6); G6=lerp(B6,D6,2/3)   # şekil ölçekli değil (hafif bozuk)
assert abs(dist(B6,G6)/dist(B6,D6)-2/3)<1e-9
f=F(); f.poly([A6,B6,C6]); f.line(B6,D6); f.dik(B6,A6,C6); f.tick(A6,D6); f.tick(D6,C6)
f.sl('$18$',A6,B6,C6,.3); f.node(mid(B6,G6),'$10$','sloped,above,inner sep=2pt'); f.raw(f'\\fill {pt(G6)} circle (1.3pt);')
f.vl('A',A6,(-1,.5),.3); f.vl('B',B6,(-1,-1),.3); f.vl('C',C6,(1,-.5),.3); f.vl('D',D6,(1,.6),.3); f.vl('G',G6,(-.3,.9),.3)
SK6=f.svg()
assert sorted([12,15,24,30,48])==sorted([AC6-AB6,BD6,BC6,AC6,AB6+AC6])
q('0006',tipId='ge-ko-agirlik-hipotenus',tip='Dik üçgende ağırlık merkezi ve Pisagor',z='zor',alt='Dik Üçgende Kenarortay',kaz='Ağırlık merkezi ve hipotenüs kenarortayı bilgisini Pisagor ile birleştirir.',
 kart='K-GKO-06 (dik üçgende ağırlık merkezi) · BG = 10, AB = 18',
 metin='Şekildeki ABC dik üçgeninde m(ABC) = 90° dir. D, [AC] hipotenüsünün orta noktası, G ise ABC üçgeninin ağırlık merkezidir ve G noktası [BD] kenarortayı üzerindedir. Şekilde gösterilen uzunluklar cm cinsindendir; çentikli parçaların uzunlukları eşittir ve şekil ölçekli değildir.\nBuna göre, |BC| kaç cm’dir?',
 dogru=24,yan=[(12,'Hipotenüsle |AB| arasındaki farkı almış: 30 − 18 = 12.','bilgi'),(15,'Kenarortay uzunluğu |BD| = 15’i |BC| olarak vermiş.','dikkat'),(30,'|BC| yerine hipotenüsü (|AC| = 30) vermiş.','dikkat'),(48,'|AB| + |AC| = 18 + 30 = 48 yazmış.','bilgi')],
 istenen='|BC| uzunluğu (cm).',
 ip=['Önce |BD| uzunluğunu ağırlık merkezinin kenarortayı bölme oranından bul; sonra bu kenarortayın hipotenüsle ilişkisini kullan.'],
 bilgi=[AGR,HIP,PIS],
 ad=[A('Kenarortayı bul','G, [BD] yi 2 : 1 böler; |BG| = 10 uzun parçadır.','|GD| = 5 → |BD| = 15'),A('Hipotenüsü bul','Hipotenüs kenarortayı hipotenüsün yarısıdır.','|AC| = 2 × 15 = 30'),A('Pisagor uygula','ABC dik üçgeninde |AB| = 18 ve |AC| = 30.','|BC|² = 30² − 18² = 900 − 324 = 576'),A('Kökü al','Uzunluk pozitif olmalıdır.','|BC| = 24')],
 puf='Dik üçgende hipotenüs kenarortayı bulununca hipotenüs onun iki katıdır; sonra Pisagor ile eksik dik kenar bulunur.',sekil=SK6)
bitir_geo('kenarortay','Kenarortay')
