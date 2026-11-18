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
P=Parti('paralelkenariki','Paralelkenar','geo|Paralelkenar',ders='TYT Geometri',idon='tytgeo')
def vls(f,names,pts):
    c=cen(pts)
    for n,p in zip(names,pts): f.vl(n,p,sub(p,c),.3)
def rot(ps,deg):
    t=radians(deg); return [(p[0]*cos(t)-p[1]*sin(t),p[0]*sin(t)+p[1]*cos(t)) for p in ps]
def foot(P_,Q,R): # P'nin QR doğrusu üzerindeki dik ayağı
    d=sub(R,Q); t=((P_[0]-Q[0])*d[0]+(P_[1]-Q[1])*d[1])/(d[0]**2+d[1]**2); return add(Q,mul(d,t))
def inter(p1,p2,p3,p4):
    d1=sub(p2,p1); d2=sub(p4,p3); den=d1[0]*d2[1]-d1[1]*d2[0]; t=((p3[0]-p1[0])*d2[1]-(p3[1]-p1[1])*d2[0])/den; return add(p1,mul(d1,t))
PAC=B('Paralelkenarda açılar','karşılıklı açılar eşit, komşu açılar bütünlerdir. Üçgenin iç açıları toplamı 180°’dir. Örnek: bir köşesi 72° olan paralelkenarın komşu açısı 108°’dir')
PALN=B('Paralelkenarın alanı','alan = taban × o tabana ait yükseklik; yükseklik tabana dik uzaklıktır. Örnek: tabanı 9, yüksekliği 4 olan paralelkenarın alanı 36’dır')
PPIS=B('Pisagor bağıntısı','dik üçgende dik kenarların kareleri toplamı hipotenüsün karesine eşittir. Örnek: dik kenarlar 9 ve 12 ise hipotenüs 15’tir')
PYUK=B('Paralelkenarın çevresi','çevre iki komşu kenarın toplamının iki katıdır. Örnek: kenarlar 5 ve 8, çevre 26’dır')
PUZ=B('Uzantı ve ikizkenar üçgen','bir kenarın uzantısı ile yan kenar arasında kalan açı, o köşedeki iç açının bütünleridir; ikizkenar üçgende taban açıları eşittir. Örnek: tepe açısı 50° olan ikizkenar üçgende taban açıları 65°’dir')
PKOS=B('Köşegenler ve çevre','paralelkenarın köşegenleri birbirini ortalar; karşılıklı kenarlar eşittir. Örnek: köşegenlerin kesim noktasına olan uzaklıklar 3 ve 5 ise köşegenler 6 ve 10’dur')
PDIK=B('Dik üçgende alan','dik üçgenin alanı dik kenarların çarpımının yarısıdır; Pisagor ile eksik dik kenar bulunur. Örnek: dik kenarlar 6 ve 8 ise hipotenüs 10’dur')
PORT=B('Orta noktalar ve alan','orta noktadan geçen doğrular ve bir köşegen paralelkenarı eş alanlı parçalara ayırır; aynı yüksekliğe sahip üçgenlerde alanlar tabanlarla orantılıdır. Örnek: yüksekliği ortak, tabanları 2 ve 3 olan üçgenlerin alanları 2 : 3 oranındadır')
PBEN=B('Benzer üçgenler','iki paralel doğru ve iki kesenle oluşan üçgenler benzerdir; karşılıklı kenarların oranı sabittir. Örnek: benzerlik oranı 1 : 3 ise karşılıklı kenarlar 2 ve 6’dır; alanlar 1 : 9 oranındadır')
konu('geo|Paralelkenar','Paralelkenar')

# ===== 01 · dik köşegen ve açı · kolay =====
kartla('K-GPL-01','Dik köşegenli paralelkenarda açı','Üçgende iki açıdan üçüncüsü bulunur; paralelkenarda karşılıklı açılar eşittir.','Karşıdaki açıyı komşu açı gibi bütünlemek; 34° ya da 90° yazmak.','kolay',3,'ge-pl-aci','Paralelkenarda açıları bulma')
h1=3.0; w1=h1*tan(radians(34)); A=(w1,h1); B_=(2*w1,h1); C=(w1,0); D=(0,0)
assert abs(ang(C,A,D)-90)<1e-9 and abs(ang(A,D,C)-34)<1e-9 and abs(ang(D,A,C)-56)<1e-9 and abs(ang(B_,A,C)-56)<1e-9
assert 180-90-34==56 and 180-56==124 and 180-34==146
f=F(); f.poly([A,B_,C,D]); f.line(A,C); f.dik(C,A,D,.22); f.par(A,B_); f.par(D,C)
f.arc(A,D,C,.5,'$34^\\circ$',.95); f.arc(B_,C,A,.5,'$x$',.9); vls(f,'ABCD',[A,B_,C,D])
SK=f.svg()
q('0001',tipId='ge-pl-aci',tip='Paralelkenarda açıları bulma',z='kolay',alt='Dik Köşegenli Paralelkenar',kaz='Paralelkenarda köşegenle oluşan dik üçgenden açıyı bulup karşılıklı açı eşitliğini kullanır.',
 kart='K-GPL-01 (dik köşegen ve açı) · AC ⊥ DC, m(DAC) = 34°, x = m(ABC)',
 metin='Bir tasarımcı, kâğıttan paralelkenar biçiminde bir ABCD kartı kesmiş ve karta [AC] köşegenini çizmiştir. Şekilde [AC] ⊥ [DC] ve m(DAC) = 34° dir. Şekil ölçekli değildir.\nBuna göre, x = m(ABC) kaç derecedir?',
 dogru=56,yan=[(34,'Verilen açıyı x’e eşit almış.','dikkat'),(90,'Dik açıyı cevap sanmış.','dikkat'),(124,'m(ADC) = 56° bulup bütünleyerek 124° yazmış.','islem'),(146,'180° − 34° işlemini yapmış.','islem')],
 istenen='x = m(ABC) açısının ölçüsü (derece).',ip=['ACD üçgeninde iki açı biliniyor; üçüncü açı hangi köşeye aittir ve B köşesinin karşısındaki köşe hangisidir?'],bilgi=[PAC],
 ad=[STEP('ACD üçgenini incele','[AC] ⊥ [DC] olduğundan C köşesinde dik açı vardır.','m(ACD) = 90°, m(DAC) = 34°'),STEP('Üçüncü açıyı bul','Üçgenin iç açıları toplamı 180°’dir.','m(ADC) = 180° − 90° − 34° = 56°'),STEP('Karşılıklı açı','B köşesi D köşesinin karşısındadır; karşılıklı açılar eşittir.','m(ABC) = m(ADC) = 56°')],
 puf='Paralelkenarda açı sorularında önce üçgenden bir köşe açısını bulup karşılıklı eşitliği kullan.',sekil=SK)

# ===== 02 · alan · kolay =====
kartla('K-GPL-02','Paralelkenarda alan','Alan taban çarpı o tabana ait yüksekliktir; yan kenarlar alana girmez.','Taban ile yan kenarı çarpmak; çevre ile karıştırmak; 2’ye bölmek.','kolay',2,'ge-pl-alan','Paralelkenarın alanı')
a2,h2=9,12; assert a2*h2==108 and a2+h2==21 and 2*(a2+h2)==42 and a2*h2/2==54 and a2*a2==81
s=.25; Pp=[(0,0),(a2*s,0),(a2*s+4*s,h2*s*.5),(4*s,h2*s*.5)]
# yükseklik 12 şeklin ölçeğini bozmasın: ölçek .15
s=.21; A_=(0,0); B2=(a2*s,0); D2=(5*s,h2*s); C2=(a2*s+5*s,h2*s); E=(D2[0],0)
assert abs(alan([A_,B2,C2,D2])/s**2-108)<1e-9
f=F(); f.poly([A_,B2,C2,D2]); f.line(D2,E,'dashed'); f.dik(E,D2,B2,.18); f.par(A_,B2); f.par(D2,C2)
f.raw(f'\\draw[<->] {pt((A_[0],-.4))} -- {pt((B2[0],-.4))};'); f.node((mid(A_,B2)[0],-.65),'$9$'); f.node(add(mid(D2,E),(.22,0)),'$12$'); vls(f,'ABCD',[A_,B2,C2,D2]); f.node(add(E,(-.24,.4)),'$E$')
SK=f.svg()
q('0002',tipId='ge-pl-alan',tip='Paralelkenarın alanı',z='kolay',alt='Paralelkenarın Alanı',kaz='Paralelkenarın taban uzunluğu ve yüksekliğini kullanarak alanını hesaplar.',
 kart='K-GPL-02 (paralelkenarın alanı) · AB = 9, DE = 12, DE ⊥ AB',
 metin='Şekilde paralelkenar biçimli bir tarlanın ABCD krokisi verilmiştir. Tarlanın bir kenarı yol boyunca uzanmakta, [DE] ⊥ [AB] olacak biçimde bir sulama kanalı çekilmiştir. Uzunluklar metre cinsindendir. Şekil ölçekli değildir.\nBuna göre, tarlanın alanı kaç m² dir?',
 dogru=108,yan=[(21,'|AB| ile |DE| uzunluklarını toplamış.','dikkat'),(42,'Verilenleri toplayıp 2 ile çarparak çevre mantığıyla hesaplamış.','bilgi'),(54,'Üçgen alanı gibi 2’ye bölmüş.','bilgi'),(81,'Taban uzunluğunun karesini (9 × 9) hesaplamış.','bilgi')],
 istenen='Tarlanın alanı (m²).',ip=['Paralelkenarın alanı için hangi iki uzunluk birbirine dik olmalıdır? Verilenler bunu sağlıyor mu?'],bilgi=[PALN],
 ad=[STEP('Tabanı belirle','[DE] doğru parçası [AB] kenarına diktir; bu kenar taban olur.','taban = |AB| = 9'),STEP('Yüksekliği belirle','Tabana inen dikme yüksekliktir.','yükseklik = |DE| = 12'),STEP('Alanı hesapla','Alan = taban × yükseklik.','9 × 12 = 108')],
 puf='Alanda taban ile o tabana dik yüksekliği çarp; verilen yan kenarı yükseklik sanma.',sekil=SK)

# ===== 03 · Pisagor, kenar · orta =====
kartla('K-GPL-03','Yükseklikle oluşan dik üçgenler','Yükseklikle iki dik üçgen oluşur; ikisinde de Pisagor uygulanıp taban parçaları bulunur ve toplanır.','Yalnız bir parçayı cevap sanmak; yüksekliği taban sanmak; kenarları toplamak.','orta',3,'ge-pl-pisagor','Paralelkenarda Pisagor')
AD3,DE3,BD3=10,8,17; AE3=sqrt(AD3**2-DE3**2); EB3=sqrt(BD3**2-DE3**2); assert AE3==6 and EB3==15 and AE3+EB3==21 and AD3+BD3==27 and AD3+EB3==25 and AD3+DE3+EB3==33 and AD3+DE3+BD3==35
A_=(0,0); B2=(21,0); D2=(6,8); C2=(27,8); s=.2; Pq=[mul(p,s) for p in (A_,B2,C2,D2)]; A_,B2,C2,D2=Pq; E=(D2[0],0)
assert abs(dist(A_,D2)/s-10)<1e-9 and abs(dist(B2,D2)/s-17)<1e-9
f=F(); f.poly([A_,B2,C2,D2]); f.line(D2,E,'dashed'); f.line(B2,D2); f.dik(E,D2,B2,.18); f.par(A_,B2); f.par(D2,C2); ic=cen(Pq)
f.sl('$10$',A_,D2,ic,.3); f.node(add(mid(D2,E),(-.24,0)),'$8$'); f.sl('$17$',B2,D2,(B2[0]+1,D2[1]*.2),.28); vls(f,'ABCD',Pq); f.vl('E',E,(0,-1),.3)
SK=f.svg()
q('0003',tipId='ge-pl-pisagor',tip='Paralelkenarda Pisagor',z='orta',alt='Yükseklik ve Köşegen',kaz='Paralelkenarda yükseklikle oluşan dik üçgenlerde Pisagor bağıntısını kullanarak taban uzunluğunu bulur.',
 kart='K-GPL-03 (yükseklik ve köşegenle Pisagor) · AD = 10, DE = 8, BD = 17',
 metin='Paralelkenar biçimli bir tarlanın ABCD krokisinde köşegen yolu [BD] ile D köşesinden [AB] kenarına inen dik patika [DE] çizilmiştir. [DE] ⊥ [AB] dir. |AD| = 10 cm, |DE| = 8 cm ve |BD| = 17 cm dir. Şekil ölçekli değildir.\nBuna göre, |AB| kaç cm dir?',
 dogru=21,yan=[(25,'|AD| ile |EB| = 15 uzunluklarını toplamış.','islem'),(27,'|AD| ile |BD| uzunluklarını toplamış.','islem'),(33,'|AD| + |DE| + |EB| toplamını yazmış.','islem'),(35,'Verilen üç uzunluğu toplamış: 10 + 8 + 17.','islem')],
 istenen='|AB| uzunluğu (cm).',ip=['Hangi iki dik üçgende iki kenar biliniyor? [AB] bu üçgenlerin kenarlarından hangileriyle ilişkilidir?'],bilgi=[PPIS],
 ad=[STEP('AED üçgeni','[DE] ⊥ [AB] olduğundan AED dik üçgendir.','|AE|² = 10² − 8² = 36 → |AE| = 6'),STEP('EBD üçgeni','EBD dik üçgeninde hipotenüs |BD| = 17’dir.','|EB|² = 17² − 8² = 225 → |EB| = 15'),STEP('Tabanı bul','E noktası [AB] üzerindedir.','|AB| = 6 + 15 = 21')],
 puf='Yükseklik çizilmiş şekillerde oluşan dik üçgenlerin her birine ayrı ayrı Pisagor uygulanır.',sekil=SK)

# ===== 04 · orta noktalarla alan · zor =====
kartla('K-GPL-04','Kenar orta noktalarının oluşturduğu üçgen','Paralelkenardan, köşe ve orta noktalarla çevrelenen üç üçgen çıkarılarak taralı üçgenin alanı bulunur; üçgenlerin alanları tabanlarla orantılıdır.','Alanı yarıya ya da çeyreğe bölmek; üç üçgenden yalnızca ikisini çıkarmak; CEF üçgenini çeyrek almak.','orta',4,'ge-pl-alanoran','Paralelkenarda orta noktalarla oluşan alan')
S4=96; assert S4*3/8==36 and S4/4==24 and S4/2==48 and S4/8==12 and S4*5/8==60
A_=(0,0); B2=(4.6,0); D2=(1.5,2.3); C2=add(B2,D2); E=mid(B2,C2); Fp=mid(C2,D2)
S_=alan([A_,B2,C2,D2]); assert abs(alan([A_,E,Fp])/S_-3/8)<1e-9 and abs(alan([A_,B2,E])/S_-1/4)<1e-9 and abs(alan([A_,D2,Fp])/S_-1/4)<1e-9 and abs(alan([E,C2,Fp])/S_-1/8)<1e-9
f=F(); f.fill([A_,E,Fp]); f.poly([A_,B2,C2,D2]); f.line(A_,E); f.line(A_,Fp); f.line(E,Fp); f.tick(B2,E); f.tick(E,C2); f.tick(C2,Fp,2); f.tick(Fp,D2,2); vls(f,'ABCD',[A_,B2,C2,D2]); f.vl('E',E,(1,0),.3); f.vl('F',Fp,(0,1),.3)
SK=f.svg()
q('0004',tipId='ge-pl-alanoran',tip='Paralelkenarda orta noktalarla oluşan alan',z='orta',alt='Orta Noktalardan Oluşan Üçgen',kaz='Paralelkenarda orta noktalarla oluşan üç köşe üçgeninin alanlarını tabanlarla orantılayarak taralı üçgenin alanını bulur.',
 kart='K-GPL-04 (orta noktalarla oluşan üçgen) · alan(ABCD) = 96, E ∈ BC ve F ∈ DC orta noktalar, taralı AEF',
 metin='Paralelkenar biçimli bir kumaş parçasının ABCD şeklinde alanı 96 cm² dir. E noktası [BC] nin, F noktası [DC] nin orta noktasıdır. Şekil ölçekli değildir.\nBuna göre, taralı AEF üçgeninin alanı kaç cm² dir?',
 dogru=36,yan=[(12,'Alanın sekizde birini (CEF üçgeninin alanını) cevap sanmış.','dikkat'),(24,'Alanın dörtte birini cevap sanmış.','bilgi'),(48,'Alanın yarısını cevap sanmış.','bilgi'),(60,'Taralı olmayan üç üçgenin alanları toplamını (24 + 24 + 12) cevap sanmış.','islem')],
 istenen='Taralı AEF üçgeninin alanı (cm²).',ip=['Taralı bölgeyi çevreleyen parçalar hangi şekillerdir?'],bilgi=[PORT,PALN],
 ad=[STEP('ABE üçgeni','|BE| = |BC| ÷ 2 olduğundan, [AB] tabanlı ve E’den inen yükseklik paralelkenarın yüksekliğinin yarısı olan üçgenin alanı bulunur.','alan(ABE) = 96 ÷ 4 = 24'),STEP('ADF üçgeni','|DF| = |DC| ÷ 2 olduğundan, [AD] ile F’den inen yükseklik düşünülerek aynı oran bulunur.','alan(ADF) = 96 ÷ 4 = 24'),STEP('CEF üçgeni','CBD üçgeninin alanı 48’dir; CEF üçgeninin iki kenarı CBD üçgeninin kenarlarının yarısıdır.','alan(CEF) = 48 ÷ 4 = 12'),STEP('Taralı alan','Paralelkenardan üç üçgen çıkarılır.','alan(AEF) = 96 − 24 − 24 − 12 = 36')],
 puf='Orta noktalar verilince kenar uzunlukları yarıya iner; alanların nasıl değiştiğini düşün.',sekil=SK)

# ===== 05 · çevre ve iki yükseklik · orta =====
kartla('K-GPL-05','İki yükseklik ve çevre','Aynı alanı iki farklı taban-yükseklik çiftiyle yaz; kenarlar oranını bul, çevreyle kenarları belirle ve alanı hesapla.','Yükseklikleri kenar sanmak; oranı ters kurmak; çevreyi alan sanmak.','orta',4,'ge-pl-yukseklik','İki yükseklik ve çevre')
AB5,AD5,DE5,BF5=20,15,12,16; assert AB5*DE5==AD5*BF5==240 and 2*(AB5+AD5)==70 and AD5*DE5==180 and DE5*BF5==192 and AD5*AD5==225 and 240/2==120
A_=(0,0); B2=(20,0); D2=(9,12); C2=add(B2,D2); E=(9,0); Fq=foot(B2,A_,D2); assert abs(dist(B2,Fq)-16)<1e-9 and abs(dist(A_,Fq)-12)<1e-9 and abs(dist(D2,E)-12)<1e-9
s=.15; Pq=[mul(p,s) for p in (A_,B2,C2,D2)]; A_,B2,C2,D2=Pq; E=mul(E,s); Fq=mul(Fq,s)
f=F(); f.poly([A_,B2,C2,D2]); f.line(D2,E,'dashed'); f.line(B2,Fq,'dashed'); f.dik(E,D2,B2,.18); f.dik(Fq,B2,D2,.18); f.par(A_,B2); f.par(D2,C2)
f.node(add(mid(D2,E),(-.25,0)),'$12$'); f.node(add(mid(B2,Fq),(.28,.1)),'$16$'); vls(f,'ABCD',Pq); f.vl('E',E,(0,-1),.3); f.vl('F',Fq,(-1,-.2),.32)
SK=f.svg()
q('0005',tipId='ge-pl-yukseklik',tip='İki yükseklik ve çevre',z='orta',alt='İki Yükseklik ve Çevre',kaz='Paralelkenarda iki yükseklikten kenarlar oranını kurup çevreyle kenarları bulur ve alanı hesaplar.',
 kart='K-GPL-05 (iki yükseklik ve çevre) · DE = 12, BF = 16, çevre 70',
 metin='Paralelkenar biçimli bir arsanın ABCD krokisinde, [DE] ⊥ [AB] ve [BF] ⊥ [AD] olacak biçimde iki dik yol çizilmiştir. |DE| = 12 cm, |BF| = 16 cm ve paralelkenarın çevresi 70 cm dir. Şekil ölçekli değildir.\nBuna göre, ABCD paralelkenarının alanı kaç cm² dir?',
 dogru=240,yan=[(192,'İki yüksekliği çarpmış: 12 × 16.','bilgi'),(225,'Yan kenarın karesini (15 × 15) hesaplamış.','bilgi'),(120,'Alanı üçgen alanı gibi 2’ye bölmüş: 20 × 12 ÷ 2.','islem'),(180,'|AD| × |DE| çarpımını (15 × 12) hesaplamış.','bilgi')],
 istenen='Paralelkenarın alanı (cm²).',ip=['Aynı paralelkenarın alanını iki farklı yolla yazabilir misin? Hangi çarpımlar birbirine eşittir?'],bilgi=[PYUK,PALN],
 ad=[STEP('Alanı iki biçimde yaz','Alan = |AB| · |DE| = |AD| · |BF|.','12·|AB| = 16·|AD| → |AB| : |AD| = 4 : 3'),STEP('Kenarları bul','Çevre 2·(|AB| + |AD|) = 70 → |AB| + |AD| = 35.','|AB| = 20, |AD| = 15'),STEP('Alanı hesapla','Taban |AB| ve yükseklik |DE|.','Alan = 20 × 12 = 240')],
 puf='Bilinmeyen kenarlar varsa verilen her uzunluğun hangi kenara ait olduğunu belirleyip ilişki kur.',sekil=SK)

# ===== 06 · uzantı ve ikizkenar · orta =====
kartla('K-GPL-06','Kenar uzantısı ve ikizkenar üçgen','Uzatılan kenar ile paralelkenarın köşe açısı bütünlerdir; ikizkenar üçgenin taban açıları bulunup açılar toplanır.','Dış açıyı iç açıya eşitlemek; tepe açısını 110° almak; yalnız taban açısını cevap yapmak.','orta',4,'ge-pl-aci','Paralelkenarda açıları bulma')
A_=(0,0); B2=(4.2,0); l6=2.4; D2=(l6*cos(radians(70)),l6*sin(radians(70))); C2=add(B2,D2); E=(B2[0]+l6,0)
assert abs(dist(B2,E)-dist(B2,C2))<1e-9 and abs(ang(A_,B2,D2)-70)<1e-9 and abs(ang(C2,D2,E)-125)<1e-9 and abs(ang(C2,B2,E)-55)<1e-9 and abs(ang(B2,C2,E)-70)<1e-9
assert 180-70==110 and (180-70)/2==55 and 70+55==125 and 70+70==140
f=F(); f.poly([A_,B2,C2,D2]); f.line(B2,E); f.line(C2,E); f.tick(B2,C2); f.tick(B2,E); f.par(A_,B2); f.par(D2,C2)
f.arc(A_,B2,D2,.5,'$70^\\circ$',.9); f.arc(C2,D2,E,.5); f.node(add(C2,mul((cos(radians(212)),sin(radians(212))),.85)),'$x$'); vls(f,'ABCD',[A_,B2,C2,D2]); f.vl('E',E,(1,0),.3)
SK=f.svg()
q('0006',tipId='ge-pl-aci',tip='Paralelkenarda açıları bulma',z='orta',alt='Uzatılan Kenar',kaz='Paralelkenarın bir kenarını uzatıp oluşan ikizkenar üçgenden yararlanarak istenen açıyı bulur.',
 kart='K-GPL-06 (kenar uzantısı) · BE = BC, m(DAB) = 70°, x = m(DCE)',
 metin='Paralelkenar biçimli bir çerçevenin ABCD şeklinde, [AB] kenarı B noktasından E noktasına kadar uzatılmıştır. |BE| = |BC| ve m(DAB) = 70° dir. Şekil ölçekli değildir.\nBuna göre, x = m(DCE) kaç derecedir?',
 dogru=125,yan=[(55,'Yalnız BCE üçgeninin taban açısını bulup x sanmış.','dikkat'),(70,'m(DCB) = 70° açısını x’e eşit almış.','dikkat'),(110,'m(ABC) = 110° açısını cevap sanmış.','dikkat'),(140,'Taban açısı yerine 70° almış: 70° + 70°.','islem')],
 istenen='x = m(DCE) açısının ölçüsü (derece).',ip=['E köşesinden C’ye çizilen doğru parçası hangi üçgeni kurar? x açısı hangi iki açının toplamıdır?'],bilgi=[PAC,PUZ],
 ad=[STEP('Karşılıklı açı','C köşesi A köşesinin karşısındadır.','m(DCB) = m(DAB) = 70°'),STEP('Uzantıdaki açı','A, B, E doğrusal olduğundan m(CBE) = 180° − m(ABC); m(ABC) = 180° − 70° = 110° olduğundan m(CBE) = 70°.','m(CBE) = 70°'),STEP('İkizkenar üçgen','|BE| = |BC| olduğundan BCE ikizkenardır, taban açıları eşittir.','m(BCE) = (180° − 70°) ÷ 2 = 55°'),STEP('x’i bul','x açısı iki açıdan oluşur.','x = 70° + 55° = 125°')],
 puf='Uzatılan kenar görünce doğrusal ve bütünler açıları yaz, sonra ikizkenar üçgeni ara.',sekil=SK)

# ===== 07 · çevre farkı · orta =====
kartla('K-GPL-07','Köşegenin oluşturduğu üçgenlerin çevreleri','Köşegenler birbirini ortaladığından iki komşu üçgenin çevre farkı iki komşu kenarın farkına eşittir; çevreyle birlikte kenarlar bulunur.','Çevre farkını kenar sanmak; toplamı kenar sanmak; AB ile BC’yi karıştırmak.','orta',3,'ge-pl-kosegen','Köşegenlerle oluşan üçgenlerin çevreleri')
a7,b7=8,12; S7=104; p7=7+sqrt(3); q7=7-sqrt(3); assert abs(p7**2+q7**2-S7)<1e-9 and abs(p7+q7-14)<1e-9
th=degrees(math.acos((p7**2+q7**2-a7**2)/(2*p7*q7)))
Oo=(0,0); Aa=(-p7,0); Cc=(p7,0); Bb=(q7*cos(radians(180-th)),q7*sin(radians(180-th))); Dd=mul(Bb,-1)
assert abs(dist(Aa,Bb)-8)<1e-9 and abs(dist(Bb,Cc)-12)<1e-9 and abs(dist(Aa,Bb)+dist(Aa,Oo)+dist(Bb,Oo)-22)<1e-9 and abs(dist(Bb,Cc)+dist(Bb,Oo)+dist(Cc,Oo)-26)<1e-9
assert 2*(8+12)==40 and (8+12)/2==10 and 12-8==4
sc=.28; Pq=[mul(p,sc) for p in (Aa,Bb,Cc,Dd)]; A_,B2,C2,D2=Pq; O_=(0,0)
f=F(); f.poly([A_,B2,C2,D2]); f.line(A_,C2); f.line(B2,D2); f.tick(A_,O_); f.tick(O_,C2); f.tick(B2,O_,2); f.tick(O_,D2,2); vls(f,'ABCD',Pq); f.node(add(O_,(.0,-.28)),'$O$')
SK=f.svg()
q('0007',tipId='ge-pl-kosegen',tip='Köşegenlerle oluşan üçgenlerin çevreleri',z='orta',alt='Köşegen Üçgenlerinin Çevreleri',kaz='Köşegenlerin birbirini ortalaması ve çevre farkıyla paralelkenarın komşu kenarlarını bulur.',
 kart='K-GPL-07 (köşegen üçgenlerinin çevreleri) · çevre(AOB) = 22, çevre(BOC) = 26, çevre(ABCD) = 40',
 metin='Paralelkenar biçimli bir uçurtmanın ABCD iskeletinde köşegen çıtaları O noktasında kesişmektedir. AOB üçgeninin çevresi 22 cm, BOC üçgeninin çevresi 26 cm ve ABCD paralelkenarının çevresi 40 cm dir. Şekil ölçekli değildir.\nBuna göre, |AB| kaç cm dir?',
 dogru=8,yan=[(4,'Çevreler farkını (26 − 22) cevap sanmış.','dikkat'),(10,'|AB| + |BC| = 20 toplamının yarısını almış.','islem'),(12,'|BC| uzunluğunu cevap sanmış.','dikkat'),(14,'|OA| + |OB| = 14 toplamını cevap sanmış.','dikkat')],
 istenen='|AB| uzunluğu (cm).',ip=['İki üçgenin çevresini yazıp birbirinden çıkarırsan hangi parçalar sadeleşir?'],bilgi=[PKOS],
 ad=[STEP('Çevre farkı','|OA| = |OC| ve [OB] ortaktır; üçgenlerin çevrelerinin farkında yalnız |BC| ile |AB| kalır.','|BC| − |AB| = 26 − 22 = 4'),STEP('Çevreden toplam','Paralelkenarın çevresi iki komşu kenarın toplamının iki katıdır.','|AB| + |BC| = 20'),STEP('Kenarı bul','İki bağıntı birlikte çözülür.','2·|AB| = 20 − 4 → |AB| = 8')],
 puf='Ortak ve eşit parçalar içeren iki çevre karşılaştırılırken sadeleşen parçaları yaz.',sekil=SK)

# ===== 08 · dik köşegen-kenar, alan · orta =====
kartla('K-GPL-08','Kenara dik köşegenli paralelkenar','Dik üçgende Pisagorla köşegen bulunur; köşegen kenara dik olduğundan yükseklik görevi görür.','Üçgen alanını paralelkenar alanı sanmak; yanlış kenarla çarpmak; Pisagorda hipotenüsü karıştırmak.','orta',3,'ge-pl-alan','Paralelkenarın alanı')
AD8,AB8=6,10; BD8=sqrt(AB8**2-AD8**2); assert BD8==8 and AD8*BD8==48 and AD8*BD8/2==24 and AD8*AB8==60 and AB8*BD8==80 and AD8*AB8/2==30
Dd=(0,0); Aa=(0,6); Bb=(8,0); Cc=add(Bb,sub(Dd,Aa)); assert abs(dist(A_,A_))==0
tt=-20; Pq=rot([Aa,Bb,Cc,Dd],tt); sc=.3; Pq=[mul(p,sc) for p in Pq]; A_,B2,C2,D2=Pq
assert abs(dist(A_,D2)/sc-6)<1e-9 and abs(dist(A_,B2)/sc-10)<1e-9 and abs(ang(D2,A_,B2)-90)<1e-9 and abs(alan(Pq)/sc**2-48)<1e-9
f=F(); f.poly([A_,B2,C2,D2]); f.line(B2,D2); f.dik(D2,A_,B2,.2); f.par(A_,B2); f.par(D2,C2); ic=cen(Pq)
f.sl('$6$',A_,D2,ic,.3); f.sl('$10$',A_,B2,ic,.35); vls(f,'ABCD',Pq)
SK=f.svg()
q('0008',tipId='ge-pl-alan',tip='Paralelkenarın alanı',z='orta',alt='Köşegeni Kenara Dik Paralelkenar',kaz='Köşegenin kenara dik olduğu paralelkenarda Pisagorla uzunluğu bulup alanı hesaplar.',
 kart='K-GPL-08 (köşegeni kenara dik paralelkenar) · AD = 6, AB = 10, BD ⊥ AD',
 metin='Paralelkenar biçimli bir bahçenin ABCD planında [BD] ⊥ [AD] dir, |AD| = 6 cm ve |AB| = 10 cm dir. Şekil ölçekli değildir.\nBuna göre, ABCD paralelkenarının alanı kaç cm² dir?',
 dogru=48,yan=[(24,'ABD üçgeninin alanını (6 × 8 ÷ 2) cevap sanmış.','bilgi'),(30,'|AD| · |AB| çarpımını 2’ye bölmüş.','islem'),(60,'|AD| · |AB| = 6 × 10 hesaplamış.','bilgi'),(80,'|AB| · |BD| = 10 × 8 hesaplamış.','bilgi')],
 istenen='Paralelkenarın alanı (cm²).',ip=['ABD üçgeninde iki kenar biliniyor; [BD] bu üçgenin hangi tür kenarıdır? [BD] ile [AD] arasındaki dik açı alan hesabında ne işe yarar?'],bilgi=[PALN,PDIK],
 ad=[STEP('|BD|’yi bul','ABD dik üçgeninde |AB| hipotenüstür.','|BD|² = 10² − 6² = 64 → |BD| = 8'),STEP('Yüksekliği tanı','[BD] ⊥ [AD] olduğundan, [AD] tabanına ait yükseklik [BD] dir.','taban = 6, yükseklik = 8'),STEP('Alanı hesapla','Alan = taban × yükseklik.','6 × 8 = 48')],
 puf='Bir köşegen bir kenara dikse, o köşegen o kenara ait yüksekliktir.',sekil=SK)

# ===== 09 · benzerlik ve alan · zor =====
kartla('K-GPL-09','Kesişen doğrularla oluşan küçük üçgenin alanı','Karşılıklı paralel kenarlar benzerlik kurar; oran köşegen üzerindeki parçayı verir; ortak köşeli üçgenlerde alan oranı kenar oranlarının çarpımıdır.','Alanı yalnız kenar oranıyla çarpmak; oranı ters kurmak; paralelkenar alanını doğrudan kullanmak.','zor',4,'ge-pl-benzer','Paralelkenarda benzerlik ve alan')
S9=120; BE9=1/3; BF9=1/4; ans9=S9/2*BE9*BF9; assert ans9==5 and S9/2*BE9==20 and S9/8*BF9*0==0 and S9/2*BE9*(1/2)==10 and S9/2*BF9==15 and S9/4==30
A_=(0,0); B2=(5.0,0); D2=(1.4,2.5); C2=add(B2,D2); E=lerp(B2,C2,1/3); Fp=inter(A_,E,B2,D2)
assert abs(dist(B2,Fp)/dist(B2,D2)-.25)<1e-9; S_=alan([A_,B2,C2,D2]); assert abs(alan([B2,E,Fp])/S_-5/120)<1e-9
f=F(); f.fill([B2,E,Fp]); f.poly([A_,B2,C2,D2]); f.line(A_,E); f.line(B2,D2); vls(f,'ABCD',[A_,B2,C2,D2]); f.vl('E',E,(1,0),.3); f.node(add(Fp,(-.05,-.28)),'$F$')
SK=f.svg()
q('0009',tipId='ge-pl-benzer',tip='Paralelkenarda benzerlik ve alan',z='zor',alt='Köşegen ve Kesen',kaz='Paralelkenarda köşegen ve bir doğru parçasının oluşturduğu benzer üçgenlerden oran kurup küçük üçgenin alanını bulur.',
 kart='K-GPL-09 (benzerlik ve alan) · alan(ABCD) = 120, BE : EC = 1 : 2, BEF alanı',
 metin='Paralelkenar biçimli bir halının ABCD şeklinde alanı 120 cm² dir. Halıya [AE] ve [BD] çizgileri işlenmiştir; E noktası [BC] üzerinde, |BE| : |EC| = 1 : 2 olacak biçimdedir. [AE] doğru parçası [BD] köşegenini F noktasında kesmektedir. Şekil ölçekli değildir.\nBuna göre, taralı BEF üçgeninin alanı kaç cm² dir?',
 dogru=5,yan=[(10,'F’yi [BD]’nin ortası sanıp 60 × 1/3 × 1/2 hesaplamış.','bilgi'),(15,'ABF üçgeninin alanını (60 × 1/4) cevap sanmış.','dikkat'),(20,'Yalnız BE : BC = 1 : 3 oranını uygulayıp 60 ÷ 3 hesaplamış.','bilgi'),(30,'Paralelkenarın alanının dörtte birini cevap sanmış.','bilgi')],
 istenen='Taralı BEF üçgeninin alanı (cm²).',ip=['[BC] // [AD] olduğundan hangi iki üçgen benzerdir? Benzerlik oranından F’nin [BD] üzerindeki yeri bulunabilir mi?'],bilgi=[PBEN,PORT],
 ad=[STEP('Benzerlik','[BE] // [AD] olduğundan BEF ile DAF benzerdir; |AD| = |BC| = 3k ve |BE| = k.','|BF| : |FD| = 1 : 3 → |BF| = |BD| ÷ 4'),STEP('BCD üçgeninin alanı','Köşegen paralelkenarı iki eş üçgene böler.','alan(BCD) = 120 ÷ 2 = 60'),STEP('BEF’yi oranla','BCD ve BEF üçgenlerinde B köşesi ortak; kenarlar [BC] üzerinde 1/3, [BD] üzerinde 1/4 oranında.','alan(BEF) = 60 × (1/3) × (1/4) = 5')],
 puf='Bir köşeyi ortak olan iki üçgenin alanları, o köşeden çıkan kenarların oranlarının çarpımıyla orantılıdır.',sekil=SK)

# ===== 10 · orta noktalarla dörtgen alanı · orta =====
kartla('K-GPL-10','Orta noktaların kestiği köşe üçgeni','İki komşu kenarın orta noktaları bir köşe üçgeni keser; kesilen üçgenin alanı oranla bulunur ve bütün üçgenden çıkarılır.','Kesilen üçgeni yarı almak; paralelkenar alanını doğrudan kullanmak; üçgenin alanı yerine paralelkenarın alanını bölmek.','orta',3,'ge-pl-alanoran','Paralelkenarda orta noktalarla oluşan alan')
S10=120; assert S10/2==60 and 60/4==15 and 60-15==45 and S10/4==30 and S10/3==40
A_=(0,0); B2=(5.0,0); D2=(1.4,2.5); C2=add(B2,D2); E=mid(A_,B2); Fp=mid(B2,C2)
S_=alan([A_,B2,C2,D2]); assert abs(alan([A_,E,Fp,C2])/S_-45/120)<1e-9 and abs(alan([E,B2,Fp])/S_-15/120)<1e-9
f=F(); f.fill([A_,E,Fp,C2]); f.poly([A_,B2,C2,D2]); f.line(A_,C2); f.line(E,Fp); f.tick(A_,E); f.tick(E,B2); f.tick(B2,Fp,2); f.tick(Fp,C2,2); vls(f,'ABCD',[A_,B2,C2,D2]); f.vl('E',E,(0,-1),.3); f.vl('F',Fp,(1,0),.3)
SK=f.svg()
q('0010',tipId='ge-pl-alanoran',tip='Paralelkenarda orta noktalarla oluşan alan',z='orta',alt='Köşeden Kesilen Üçgen',kaz='Paralelkenarda iki kenarın orta noktasıyla kesilen köşe üçgeninin alanını bulup taralı dörtgenin alanını hesaplar.',
 kart='K-GPL-10 (köşe üçgeni) · alan(ABCD) = 120, E ve F orta noktalar, taralı AEFC',
 metin='Paralelkenar biçimli bir bahçenin ABCD planında alanı 120 m² dir. E ve F noktaları sırasıyla [AB] ve [BC] kenarlarının orta noktalarıdır. Bahçenin taralı AEFC bölümüne çiçek ekilecektir. Şekil ölçekli değildir.\nBuna göre, çiçek ekilecek alan kaç m² dir?',
 dogru=45,yan=[(15,'Yalnız kesilen BEF üçgeninin alanını cevap sanmış.','dikkat'),(30,'Paralelkenarın alanının dörtte birini cevap sanmış.','bilgi'),(40,'Paralelkenarın alanının üçte birini cevap sanmış.','bilgi'),(60,'ABC üçgeninin alanını cevap sanmış.','dikkat')],
 istenen='Taralı AEFC bölgesinin alanı (m²).',ip=['Taralı olmayan bölgeler hangi şekillerdir ve alanları paralelkenarın alanıyla nasıl ilişkilidir?'],bilgi=[PORT,PALN],
 ad=[STEP('ABC üçgeninin alanı','Köşegen paralelkenarı iki eş üçgene böler.','alan(ABC) = 120 ÷ 2 = 60'),STEP('BEF üçgeninin alanı','|BE| = |BA| ÷ 2 ve |BF| = |BC| ÷ 2 olduğundan BEF’nin alanı ABC’nin dörtte biridir.','alan(BEF) = 60 ÷ 4 = 15'),STEP('Taralı alan','ABC üçgeninden BEF üçgeni çıkarılır.','60 − 15 = 45')],
 puf='Orta noktalar verilince kenar uzunlukları yarıya iner; alanların nasıl değiştiğini düşün.',sekil=SK)
bitir_geo('paralelkenariki','Paralelkenar')
