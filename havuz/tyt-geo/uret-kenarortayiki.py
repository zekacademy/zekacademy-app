"""TYT Geometri · Kenarortay ikinci paket (hafif mod). Şekil koordinatları hesaplanır, TikZ aynı değerlerden üretilir; her cevap ve çeldirici assert edilir."""
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
    P.yaz(os.path.join(GD,f'{onek}-1.json'),f'/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/ai_dk/bos-{onek}.json')
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
ONEK='kenarortayiki'
P=Parti(ONEK,'Kenarortay','geo|Kenarortay',ders='TYT Geometri',idon='tytgeo')
def kartla(id,alt,fikir,tuzak,z,adim,tipId,tip,kalip='şekilli'):
    kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,'ÖSYM 2018–2026 TYT Geometri soruları (yalnız mantık) · MEB 9–10. sınıf geometri'); TIPK[tipId]=P.k
def bestdir(p,hedefler,d=.3):
    ac=[degrees(atan2(h[1]-p[1],h[0]-p[0])) for h in hedefler]; best=None
    for a in range(0,360,10):
        m=min(abs((a-b+180)%360-180) for b in ac)
        if best is None or m>best[0]: best=(m,a)
    a=radians(best[1]); return (p[0]+d*cos(a),p[1]+d*sin(a))
AGR=B('Ağırlık merkezi','üçgenin üç kenarortayı tek bir noktada (G) kesişir; G, her kenarortayı köşe tarafından başlayarak 2 : 1 oranında böler. Örnek: bir kenarortayın uzunluğu 12 ise köşeye uzaklık 8, kenara uzaklık 4 tür')
IKZ0=B('İkizkenar üçgen ve kenarortay','ikizkenar üçgende tabana ait kenarortay tabanı dik olarak ortalar ve tepe açısını iki eşit açıya böler. Örnek: taban açıları 50° olan ikizkenar üçgende tepe açısı 80° dir ve tabana ait kenarortay onu 40° + 40° ye ayırır')
ESK=B('Eşkenar üçgenin yüksekliği','kenarı a olan eşkenar üçgende yükseklik (aynı zamanda kenarortay) h = a√3/2 dir. Örnek: kenarı 8 olan eşkenar üçgenin yüksekliği 4√3 tür')
KOR=B('Kenarortay','köşeyi karşı kenarın orta noktasına birleştiren doğru parçasıdır; orta nokta kenarı eşit iki parçaya ayırır. Örnek: |BC| = 14 ve D orta nokta ise |BD| = 7 dir')
PIS=B('Pisagor bağıntısı','dik üçgende dik kenarların kareleri toplamı hipotenüsün karesine eşittir. Örnek: dik kenarları 7 ve 24 olan üçgenin hipotenüsü 25 tir')
CEV=B('Üçgenin çevresi','üçgenin çevresi üç kenarının uzunlukları toplamıdır; orta nokta, bir kenarı eşit iki parçaya ayırır. Örnek: kenarları 5, 6 ve 7 olan üçgenin çevresi 18 dir')
PRK=B('Paralel doğrular ve benzerlik','iki paralel doğru arasında kesişen doğrular orantılı parçalar ayırır ve oluşan iki üçgen benzerdir. Örnek: köşegenleri kesişen bir yamukta paralel kenarların oranı 2 : 3 ise köşegenler kesim noktasında 2 : 3 oranında bölünür')
PAR=B('Paralelkenar','paralelkenarda karşılıklı kenarlar paralel ve eşittir. Örnek: |AB| = 7 ise |CD| = 7 dir')
ALN=B('Kenarortay ve alan','bir kenarortay üçgeni alanları eşit iki üçgene ayırır; aynı yüksekliğe sahip üçgenlerin alanları taban uzunlukları ile orantılıdır. Örnek: alanı 40 olan üçgenin bir kenarortayı onu 20 ve 20 alanlı iki parçaya böler')
ICA=B('İkizkenar üçgenin açıları','eşit kenarların karşısındaki açılar eşittir; üçgenin iç açılarının toplamı 180° dir. Örnek: tepe açısı 40° olan ikizkenar üçgenin taban açıları 70° er derecedir')
DEN=B('Denklem kurma','eşit olan iki ifade birbirine eşitlenir; bulunan değer iki ifadede de yerine konarak kontrol edilir. Örnek: 2m + 1 = m + 6 ise m = 5 tir ve her iki taraf 11 dir')
ORT=B('Orta taban','bir üçgende iki kenarın orta noktalarını birleştiren doğru parçası üçüncü kenara paraleldir ve onun yarısı uzunluğundadır. Örnek: orta tabanın uzunluğu 7 ise üçüncü kenar 14 tür')
konu('geo|Kenarortay','Kenarortay')
def deger(a,b): return abs(a-b)<1e-9

# ===== 01 kolay · ikizkenar üçgende taban kenarortayı =====
kartla('K-GKI-01','İkizkenar üçgende taban kenarortayı','Taban kenarortayı tabanı dik ortalar; orta noktadan yarı taban bulunur ve Pisagor uygulanır.','Kenarortayı yan kenara eşitlemek; yan kenardan yarı tabanı çıkarmak; yan kenarla yarı tabanı toplamak.','kolay',3,'ge-ki-ozel','Özel üçgenlerde kenarortay')
AB1=26; BC1=20; BD1=BC1//2; AD1=int(round(sqrt(AB1**2-BD1**2))); assert AD1==24 and AD1**2+BD1**2==AB1**2 and AB1-BD1==16 and AB1+BD1==36
s=.2; B1=(0,0); C1=(BC1*s,0); A1=(BC1*s/2,AD1*s); D1=mid(B1,C1); assert deger(dist(A1,B1),AB1*s) and deger(dist(A1,C1),AB1*s)
ic=cen([A1,B1,C1]); f=F(); f.poly([A1,B1,C1]); f.line(A1,D1)
f.tick(A1,B1,2); f.tick(A1,C1,2); f.tick(B1,D1); f.tick(D1,C1); f.sl('$26$',A1,B1,ic,.4); dim(f,B1,C1,'$20$',(0,-1),.75)
for n_,p_ in (('A',A1),('B',B1),('C',C1)): vtx(f,p_,n_,ic)
f.vl('D',D1,(0,1),.28) if False else f.node((D1[0]+.28,D1[1]+.25),'$D$')
SK1=f.svg()
q('0001',tipId='ge-ki-ozel',tip='Özel üçgenlerde kenarortay',z='kolay',alt='İkizkenar Kenarortay',kaz='İkizkenar üçgende taban kenarortayının uzunluğunu bulur.',
 kart='K-GKI-01 (ikizkenar taban kenarortayı) · |AB| = |AC| = 26, |BC| = 20',
 metin='Şekilde, uzunlukları cm cinsinden verilen ABC ikizkenar üçgeninde D noktası [BC] tabanının orta noktasıdır. Eşit çentikli kenarların uzunlukları eşittir ve şekil ölçekli değildir.\nBuna göre, |AD| kaç cm’dir?',
 dogru=AD1,yan=[(10,'Yalnız yarı tabanı (|BD| = 10) bulup |AD| olarak vermiş.','dikkat'),(16,'Yan kenardan yarı tabanı çıkarmış: 26 − 10.','bilgi'),(26,'Kenarortayı yan kenara eşit almış.','dikkat'),(36,'Yan kenarla yarı tabanı toplamış: 26 + 10.','bilgi')],
 istenen='|AD| uzunluğu (cm).',
 ip=['[AD] ile [BC] arasında özel bir ilişki var mı?'],
 bilgi=[KOR,PIS],
 ad=[A('Yarı tabanı bul','D, [BC] nin orta noktasıdır.','|BD| = 20 ÷ 2 = 10'),A('Dik üçgeni kur','İkizkenar üçgende taban kenarortayı tabana diktir; ABD üçgeni D de diktir.','|AD|² + |BD|² = |AB|²'),A('Hesapla','Değerleri yaz ve kökü al.','|AD|² = 26² − 10² = 676 − 100 = 576 → |AD| = 24')],
 puf='Kenarortay yardımıyla oluşan küçük üçgende, bilinen kenarları belirleyip uygun bağıntıyı seç.',sekil=SK1)

# ===== 02 kolay · eşkenar üçgende ağırlık merkezi =====
kartla('K-GKI-02','Eşkenar üçgende ağırlık merkezi','Eşkenar üçgenin yüksekliği hesaplanır; ağırlık merkezinin köşeye uzaklığı yüksekliğin 2/3 üdür; üç köşe aynı uzaklıktadır.','Yüksekliği cevap sanmak; yalnız bir uzaklığı vermek; 1/3 ile 2/3 ü karıştırmak.','kolay',3,'ge-ki-ozel','Özel üçgenlerde kenarortay')
a2=6; h2=a2*3//2*1; # a=6√3 ⇒ h = a√3/2 = 6*3/2
assert deger(6*sqrt(3)*sqrt(3)/2,9) and h2==9; AG2=2*9//3; GD2=9//3; assert (AG2,GD2)==(6,3) and 3*AG2==18 and 3*GD2==9 and 2*AG2==12 and 3*9==27
s=.42; a2c=6*sqrt(3)*s*0+4.4; B2=(0,0); C2=(a2c,0); A2=(a2c/2,a2c*sqrt(3)/2); G2=cen([A2,B2,C2]); D2=mid(B2,C2)
assert deger(dist(G2,A2),2*dist(G2,D2)) and deger(dist(G2,A2),dist(G2,B2)) and deger(dist(G2,B2),dist(G2,C2))
f=F(); f.poly([A2,B2,C2])
for p_ in (A2,B2,C2): f.line(G2,p_,'densely dashed')
f.tick(A2,B2); f.tick(B2,C2); f.tick(C2,A2); dim(f,B2,C2,'$6\\sqrt{3}$',(0,-1),.55)
ic=G2
for n_,p_ in (('A',A2),('B',B2),('C',C2)): vtx(f,p_,n_,G2)
f.node(bestdir(G2,[A2,B2,C2],.3),'$G$')
SK2=f.svg()
q('0002',tipId='ge-ki-ozel',tip='Özel üçgenlerde kenarortay',z='kolay',alt='Eşkenarda Ağırlık Merkezi',kaz='Eşkenar üçgende ağırlık merkezinin köşelere uzaklıkları toplamını bulur.',
 kart='K-GKI-02 (eşkenar üçgen, G nin uzaklıkları) · kenar 6√3',
 metin='Şekilde, kenar uzunluğu 6√3 cm olan ABC eşkenar üçgeni ve bu üçgenin ağırlık merkezi G verilmiştir. Şekil ölçekli değildir.\nBuna göre, G noktasının A, B ve C köşelerine olan uzaklıkları toplamı, yani |GA| + |GB| + |GC| kaç cm’dir?',
 dogru=18,yan=[(3,'G nin bir kenara uzaklığını (3) bulmuş.','dikkat'),(6,'Yalnız bir uzaklığı (|GA| = 6) bulup üçünü toplamayı unutmuş.','dikkat'),(9,'Üçgenin yüksekliğini (9) cevap olarak vermiş.','dikkat'),(12,'Üç uzaklık yerine iki uzaklığı toplamış: 6 + 6.','islem')],
 sira=None,
 istenen='|GA| + |GB| + |GC| toplamı (cm).',
 ip=['Eşkenar üçgenin köşelerinden ağırlık merkezine olan üç uzaklık arasında nasıl bir ilişki vardır? Birini bulmak için önce hangi uzunluk gerekir?'],
 bilgi=[ESK,AGR],
 ad=[A('Yüksekliği bul','Eşkenar üçgende yükseklik, aynı zamanda kenarortaydır.','h = 6√3 × √3 / 2 = 9'),A('Bir köşeye uzaklığı bul','G, kenarortayı köşeden başlayarak 2 : 1 böler.','|GA| = 2/3 × 9 = 6'),A('Üç uzaklığı topla','Eşkenar üçgende G üç köşeye eşit uzaklıktadır.','6 + 6 + 6 = 18')],
 puf='Önce tek bir kenarortay uzunluğunu bul; sonra ağırlık merkezinin bu kenarortaya göre konumunu kullan.',sekil=SK2)

# ===== 03 orta · çevre farkı ile denklem =====
kartla('K-GKI-03','Kenarortayın ayırdığı üçgenlerin çevreleri','İki üçgenin çevresi yazılır; ortak ve eşit parçalar sadeleşince kalan fark kenarlar arasındaki ilişkiyi verir; denklem çözülür.','Çevre farkını bir kenara eşitlemek; farkı iki katına çıkarmak; çıkarmayı ters yönde yapmak.','orta',4,'ge-ki-cevre','Kenarortaylı üçgenlerde çevre')
AB3=lambda x: 3*x-2; AC3=lambda x: 2*x+1
x3=[x for x in range(-20,40) if AB3(x)-AC3(x)==6]; assert x3==[9] and AB3(9)==25 and AC3(9)==19
assert [x for x in range(-30,40) if AB3(x)-AC3(x)==12]==[15] and AB3(15)==43 and [x for x in range(-30,40) if AB3(x)-AC3(x)==6 and False]==[] and AB3(3)==7
s=1; B3=(0,0); C3=(5.6,0); A3=(3.8,3.7); D3=mid(B3,C3); ic=cen([A3,B3,C3])
f=F(); f.poly([A3,B3,C3]); f.line(A3,D3); f.tick(B3,D3); f.tick(D3,C3); f.sl('$3x-2$',A3,B3,ic,.6); f.sl('$2x+1$',A3,C3,ic,.7)
for n_,p_ in (('A',A3),('B',B3),('C',C3)): vtx(f,p_,n_,ic)
f.vl('D',D3,(0,-1),.3)
SK3=f.svg()
q('0003',tipId='ge-ki-cevre',tip='Kenarortaylı üçgenlerde çevre',z='orta',alt='Çevre Farkı',kaz='Kenarortayın ayırdığı iki üçgenin çevre farkından bilinmeyen kenarı bulur.',
 kart='K-GKI-03 (çevre farkı) · |AB| = 3x − 2, |AC| = 2x + 1, fark 6',
 metin='Şekilde, kenar uzunlukları birim cinsinden verilen ABC üçgeninde D noktası [BC] nin orta noktasıdır. ABD üçgeninin çevresi, ADC üçgeninin çevresinden 6 birim fazladır. Şekil ölçekli değildir.\nBuna göre, |AB| kaç birimdir?',
 dogru=25,yan=[(7,'Farkı |AB| − |AC| yerine |AC| − |AB| sanıp x + 3 = 6 yazmış: x = 3, |AB| = 3 × 3 − 2 = 7.','islem'),(9,'x değerini bulup |AB| yi hesaplamadan cevap vermiş.','dikkat'),(19,'|AB| yerine |AC| = 2x + 1 değerini vermiş.','dikkat'),(43,'Çevre farkını 12 alarak x = 15 bulmuş (|BD| = |DC| nin etkisini iki kez saymış).','bilgi')],
 istenen='|AB| uzunluğu (birim).',
 ip=['İki üçgenin çevresini ayrı ayrı yazıp farkını bulmayı dene; hangi uzunluklar her iki çevrede de yer alıyor?'],
 bilgi=[CEV,DEN],
 ad=[A('Çevreleri yaz','D, [BC] nin orta noktası olduğundan |BD| = |DC| dir; [AD] ortaktır.','Ç(ABD) = |AB| + |BD| + |AD| · Ç(ADC) = |AC| + |DC| + |AD|'),A('Farkı yaz','Eşit ve ortak uzunluklar birbirini götürür.','Ç(ABD) − Ç(ADC) = |AB| − |AC| = 6'),A('Denklemi çöz','Verilen ifadeleri yerine yaz.','(3x − 2) − (2x + 1) = 6 → x − 3 = 6 → x = 9'),A('|AB| yi hesapla','x = 9 u yerine koy.','|AB| = 3 × 9 − 2 = 25')],
 puf='Çevre karşılaştırırken her iki çevrede bulunan uzunlukları ayıkla; kalanlar arasındaki ilişkiyi denklem yap.',sekil=SK3)

# ===== 04 orta · paralelkenarda köşegen bölünmesi =====
kartla('K-GKI-04','Paralelkenarda köşegenin bölünmesi','Paralel kenarlar sayesinde oluşan benzer üçgenlerden köşegenin parçalarının oranı bulunur; orta nokta oranı 1 : 2 verir.','Orta nokta nedeniyle oranı 1 : 1 sanmak; oranı ters kullanmak; parçayı bütünle karıştırmak.','orta',4,'ge-ki-paralelkenar','Paralelkenarda orta nokta ve köşegen')
BD4=18; A4=(1.4,2.8); B4=(0,0); C4=(5,0); D4=add(sub(A4,B4),C4); E4=mid(B4,C4); K4=kesis(A4,E4,B4,D4)
assert deger(dist(B4,K4)*3,dist(B4,D4)) and deger(dist(K4,D4),2*dist(B4,K4)); KD4=Fr(2*BD4,3); assert KD4==12
assert Fr(BD4,3)==6 and Fr(BD4,2)==9 and Fr(BD4,4)==Fr(9,2) and Fr(BD4,6)==3
ic=cen([A4,B4,C4,D4]); f=F(); f.poly([A4,B4,C4,D4]); f.line(B4,D4); f.line(A4,E4); f.tick(B4,E4); f.tick(E4,C4)
for n_,p_ in (('A',A4),('B',B4),('C',C4),('D',D4)): vtx(f,p_,n_,ic)
f.vl('E',E4,(0,-1),.3); f.vl('K',K4,(-1,.35),.3)
SK4=f.svg()
q('0004',tipId='ge-ki-paralelkenar',tip='Paralelkenarda orta nokta ve köşegen',z='orta',alt='Paralelkenarda Köşegen',kaz='Paralelkenarda bir kenarın orta noktasından çizilen doğrunun köşegeni bölme oranını kullanır.',
 kart='K-GKI-04 (paralelkenar, orta nokta) · |BD| = 18',
 metin='Şekildeki ABCD paralelkenarında E noktası [BC] kenarının orta noktasıdır. [AE] doğru parçası, [BD] köşegenini K noktasında kesmektedir. |BD| = 18 cm dir ve şekil ölçekli değildir.\nBuna göre, |KD| kaç cm’dir?',
 dogru=12,yan=[(3,'Köşegenin 1/6 sı kadar bir parça almış (oranı 1 : 5 sanmış).','bilgi'),(4.5,'Köşegenin 1/4 ü kadar bir parça almış (oranı 1 : 3 sanmış).','bilgi'),(6,'|BK| yı bulup |KD| yerine vermiş.','dikkat'),(9,'E orta nokta olduğundan K yı da [BD] nin orta noktası sanmış.','dikkat')],
 istenen='|KD| uzunluğu (cm).',
 ip=['[AD] ile [BE] paralel olduğuna göre K noktasında oluşan iki üçgen arasında nasıl bir ilişki vardır?'],
 bilgi=[PRK,PAR],
 ad=[A('Benzer üçgenleri bul','[AD] ∥ [BE] olduğundan BKE ve DKA üçgenleri benzerdir.','|BK| / |KD| = |BE| / |AD|'),A('Oranı yaz','|BE| = |BC| / 2 ve |AD| = |BC| dir.','|BK| / |KD| = 1 / 2'),A('Parçaları belirle','Köşegen 1 + 2 = 3 eşit parçaya ayrılır.','|KD| = 18 × 2 / 3 = 12')],
 puf='Paralel doğrular gördüğünde benzer üçgen ara; oranı kısa kenarlardan kurup bütünü paylaştır.',sekil=SK4)

# ===== 05 orta · hikâyeli · kenarortayın orta noktası ve alan =====
kartla('K-GKI-05','Kenarortayın orta noktasıyla alan','Kenarortay önce tüm alanı yarıya böler; oluşan üçgenin kenarortayı alanı bir kez daha yarıya böler.','Yalnız bir kez yarıya bölmek; alanı 1/3 ya da 3/4 almak; tüm alanı cevap sanmak.','orta',3,'ge-ki-alan','Kenarortay ve alan oranları','hikâyeli')
T5=48; ABD5=T5//2; BED5=ABD5//2; assert (ABD5,BED5)==(24,12)
A5=(1.6,4.0); B5=(0,0); C5=(5.8,0); D5=mid(B5,C5); E5=mid(A5,D5)
assert deger(alan([B5,E5,D5])*4,alan([A5,B5,C5])) and T5*Fr(1,3)==16 and T5*Fr(3,4)==36
ic=cen([A5,B5,C5]); f=F(); f.fill([B5,E5,D5]); f.poly([A5,B5,C5]); f.line(A5,D5); f.line(B5,E5); f.tick(B5,D5); f.tick(D5,C5); f.tick(A5,E5,2); f.tick(E5,D5,2)
for n_,p_ in (('A',A5),('B',B5),('C',C5)): vtx(f,p_,n_,ic)
f.vl('D',D5,(0,-1),.3); f.vl('E',E5,(1,.2),.28)
SK5=f.svg()
q('0005',tipId='ge-ki-alan',tip='Kenarortay ve alan oranları',z='orta',kalip='hikâyeli',alt='Kenarortay ve Alan',kaz='Kenarortayın ve onun orta noktasının ayırdığı bölgelerin alanlarını hesaplar.',
 kart='K-GKI-05 (kenarortay, orta nokta, alan) · alan(ABC) = 48',
 metin='Üçgen biçimli ABC bahçesinin alanı 48 m² dir. Şekilde D noktası [BC] nin, E noktası ise [AD] nin orta noktasıdır. B ile E arasına çit çekilmiş ve çitle çevrili, taralı BED bölümüne çiçek ekilecektir. Şekil ölçekli değildir.\nBuna göre, çiçek ekilecek bölümün alanı kaç m²’dir?',
 dogru=12,yan=[(16,'Alanı 1/3 almış: 48 ÷ 3.','bilgi'),(24,'Yalnız bir kez yarıya bölmüş (ABD alanı).','dikkat'),(36,'Alanı 3/4 almış: 48 × 3 ÷ 4.','bilgi'),(48,'Bahçenin tüm alanını vermiş.','dikkat')],
 istenen='BED bölümünün alanı (m²).',
 ip=['[AD] kenarortayı ABC üçgenini nasıl böler? BED üçgeni hangi üçgenin kenarortayıyla elde ediliyor?'],
 bilgi=[ALN],
 ad=[A('[AD] nin böldüğü alanı bul','D orta nokta olduğundan ABD ve ADC üçgenlerinin alanları eşittir.','alan(ABD) = 48 ÷ 2 = 24'),A('ABD içinde [BE] yi incele','E, [AD] nin orta noktasıdır; [BE], ABD üçgeninin kenarortayıdır.','alan(BED) = alan(ABD) ÷ 2'),A('Hesapla','Değeri yaz.','24 ÷ 2 = 12')],
 puf='Bölgeyi oluşturan her kenarortay için alanı yarıya bölerek ilerle; hangi üçgenin kenarortayı olduğunu her adımda belirle.',sekil=SK5)

# ===== 06 orta · orta noktaya eşit uzaklık ve açı =====
kartla('K-GKI-06','Orta noktaya eşit uzaklık ve açılar','Orta noktadan üç köşeye uzaklıklar eşit olunca oluşan ikizkenar üçgenlerin açıları toplanır; karşı açının 90° olduğu görülür ve açı toplamıyla denklem kurulur.','Taban açılarını eşit saymak; toplamı 180° almak; x yerine üç x li ifadenin değerini vermek.','orta',4,'ge-ki-aci','Orta noktaya eşit uzaklık ve açı')
x6=30; B6a=2*x6-4; C6a=x6+4; assert B6a+C6a==90 and (B6a,C6a)==(56,34)
assert [x for x in range(-10,100) if 2*x-4==x+4]==[8] and [x for x in range(0,200) if (2*x-4)+(x+4)==180]==[60] and [x for x in range(0,200) if (2*x-4)+(x+4)==135]==[45] and 3*x6==90
B6=(0,0); C6=(5.5,0); A6=tri_ac(B6,C6,B6a,C6a); D6=mid(B6,C6)
assert abs(ang(A6,B6,C6)-90)<1e-9 and deger(dist(A6,D6),dist(B6,D6))
ic=cen([A6,B6,C6]); f=F(); f.poly([A6,B6,C6]); f.line(A6,D6); f.tick(A6,D6); f.tick(B6,D6); f.tick(D6,C6)
f.arc(B6,A6,C6,.6,'$(2x-4)^\\circ$',1.55); f.arc(C6,B6,A6,.55,'$(x+4)^\\circ$',1.75)
for n_,p_ in (('A',A6),('B',B6),('C',C6)): vtx(f,p_,n_,ic)
f.vl('D',D6,(0,-1),.3)
SK6=f.svg()
q('0006',tipId='ge-ki-aci',tip='Orta noktaya eşit uzaklık ve açı',z='orta',alt='Açı ve Kenarortay',kaz='Orta noktanın köşelere eşit uzaklığından yararlanarak açı denklemini çözer.',
 kart='K-GKI-06 (|AD| = |BD| = |DC|, açı denklemi) · m(B) = 2x − 4, m(C) = x + 4',
 metin='Şekildeki ABC üçgeninde D noktası [BC] nin orta noktasıdır ve |AD| = |BD| dir. m(ABC) = (2x − 4)° ve m(ACB) = (x + 4)° olarak verilmiştir. Şekil ölçekli değildir.\nBuna göre, x kaçtır?',
 dogru=30,yan=[(8,'m(ABC) = m(ACB) sanıp 2x − 4 = x + 4 çözmüş.','bilgi'),(45,'A açısını 45° alıp 3x = 135 yazmış.','bilgi'),(60,'İki açının toplamını 180° alıp 3x = 180 yazmış.','bilgi'),(90,'3x = 90 eşitliğinden x yerine 3x in değerini (90) vermiş.','islem')],
 istenen='x değeri.',
 ip=['|AD| = |BD| = |DC| ise A, B ve C köşelerinin D ye göre durumu nedir? Hangi küçük üçgenler ikizkenardır?'],
 bilgi=[ICA,DEN],
 ad=[A('Eşit uzaklıkları yaz','D orta nokta olduğundan |BD| = |DC| dir; ayrıca |AD| = |BD|.','|AD| = |BD| = |DC|'),A('Açıları taşı','ABD ve ADC üçgenleri ikizkenardır; m(BAD) = m(ABC) ve m(DAC) = m(ACB) dir.','m(A) = m(B) + m(C)'),A('A açısını bul','İç açılar toplamı 180° olduğundan 2 × (m(B) + m(C)) = 180°.','m(B) + m(C) = 90°'),A('Denklemi çöz','İfadeleri yerine yaz.','(2x − 4) + (x + 4) = 90 → 3x = 90 → x = 30')],
 puf='Eşit uzunlukları gördüğünde oluşan ikizkenar üçgenleri belirle ve eşit açıları şekle taşı.',sekil=SK6)

# ===== 07 orta · alan denklemi ve dörtgen bölge =====
kartla('K-GKI-07','Alan denklemiyle dörtgen bölge','Kenarortay alanı ikiye böldüğünden iki alan ifadesi eşitlenir; bulunan değerle tüm alan ve altıda bir parçalar kullanılır.','Eşitlik yerine toplam kurmak; dörtgeni tek parça saymak; dörtgenin yarım üçgen olduğunu sanmak.','orta',4,'ge-ki-alan','Kenarortay ve alan oranları')
x7=[x for x in range(-20,40) if 3*x+3==6*x-9]; assert x7==[4]; ABD7=3*4+3; T7=2*ABD7; assert (ABD7,T7)==(15,30) and T7//6*2==10
assert T7//6==5 and T7//2==15 and T7*Fr(2,3)==20
A7=(1.7,4.1); B7=(0,0); C7=(5.8,0); D7=mid(B7,C7); E7=mid(A7,C7); F7=mid(A7,B7); G7=cen([A7,B7,C7])
assert deger(alan([B7,D7,G7,F7])*3,alan([A7,B7,C7]))
ic=G7; f=F(); f.fill([B7,D7,G7,F7]); f.poly([A7,B7,C7]); f.line(A7,D7); f.line(B7,E7); f.line(C7,F7)
f.tick(B7,D7); f.tick(D7,C7); f.tick(A7,E7,2); f.tick(E7,C7,2); f.tick(A7,F7,3); f.tick(F7,B7,3)
for n_,p_ in (('A',A7),('B',B7),('C',C7)): vtx(f,p_,n_,G7)
f.vl('D',D7,(0,-1),.3); f.vl('E',E7,(1,.4),.3); f.vl('F',F7,(-1,.4),.3); f.node(bestdir(G7,[A7,B7,C7,D7,E7,F7],.3),'$G$')
SK7=f.svg()
q('0007',tipId='ge-ki-alan',tip='Kenarortay ve alan oranları',z='orta',kalip='hikâyeli',alt='Alan Denklemi',kaz='Kenarortayın eşit alanlı böldüğü üçgenlerden denklem kurup dörtgen bölgenin alanını bulur.',
 kart='K-GKI-07 (alan ifadeleri, dörtgen bölge) · alan(ABD) = 3x + 3, alan(ADC) = 6x − 9',
 metin='Üçgen biçimli bir arsada [AD], [BE] ve [CF] hatları kenarortay olarak çizilmiş ve G noktası bu hatların kesim noktası olmuştur. ABD bölümünün alanı (3x + 3) m², ADC bölümünün alanı ise (6x − 9) m² dir. Şekil ölçekli değildir.\nBuna göre, taralı BDGF bölümünün alanı kaç m²’dir?',
 dogru=10,yan=[(5,'Taralı dörtgeni altı eş parçadan yalnız biri sanmış.','bilgi'),(15,'Taralı dörtgenin alanı yerine ABD bölümünün alanını vermiş.','dikkat'),(20,'Dörtgeni toplam alanın 2/3 ü sanmış.','bilgi'),(30,'Taralı bölgenin alanı yerine arsanın tüm alanını vermiş.','dikkat')],
 istenen='BDGF bölümünün alanı (m²).',
 ip=['[AD] kenarortayı ABC üçgenini nasıl böler? İki alan ifadesi arasındaki bu ilişkiyi denkleme dönüştür.'],
 bilgi=[ALN,DEN],
 ad=[A('Denklemi kur','[AD] kenarortayı alanı iki eşit parçaya böler.','3x + 3 = 6x − 9 → x = 4'),A('Tüm alanı bul','ABD bölümünün alanını hesaplayıp ikiyle çarp.','alan(ABD) = 15 → alan(ABC) = 30'),A('Altı eş parçayı kullan','Üç kenarortay alanı eşit 6 üçgene ayırır; her biri 30 ÷ 6 = 5 m² dir.','BDGF = GBD + GBF'),A('Dörtgenin alanı','Dörtgen iki küçük üçgenden oluşur.','2 × 5 = 10')],
 puf='Alan ifadeleri verildiğinde önce eşitlikten bilinmeyeni bul; sonra bölgeyi eş parçaların sayısıyla ifade et.',sekil=SK7)

# ===== 08 zor · dik kesişen kenarortaylar =====
kartla('K-GKI-08','Dik kesişen kenarortaylar','İki kenarortay uzunluğunun 2/3 ü ağırlık merkezine uzaklıkları verir; G de dik üçgen oluşur ve Pisagor ile kenar bulunur.','Tam kenarortay uzunluklarıyla Pisagor yapmak; 1/3 oranını kullanmak; ağırlık merkezi uzaklıklarını toplamak.','zor',4,'ge-ki-dikko','Dik kesişen kenarortaylar')
BE8=18; CF8=24; BG8=BE8*2//3; CG8=CF8*2//3; BC8=int(round(sqrt(BG8**2+CG8**2))); assert (BG8,CG8,BC8)==(12,16,20) and BG8**2+CG8**2==BC8**2
assert int(round(sqrt(BE8**2+CF8**2)))==30 and BE8*CF8>0 and int(round(sqrt((BE8//3)**2+(CF8//3)**2)))==10 and BG8+CG8==28
Gx=(0,0); Bx=(-12,0); Cx=(0,16); Ax=(12,-16); Ex=mid(Ax,Cx); Fx=mid(Ax,Bx); assert Ex==(6,0) and Fx==(0,-8) and cen([Ax,Bx,Cx])==(0,0)
sc=.17; th=-25; rr=lambda p:rot(mul(p,sc),th)
A8,B8,C8,E8,F8,G8=[rr(p) for p in (Ax,Bx,Cx,Ex,Fx,Gx)]
assert abs(ang(G8,B8,C8)-90)<1e-9 and abs(ang(G8,E8,F8)-90)<1e-9 and deger(dist(G8,B8)/dist(G8,E8),2)
ic=G8; f=F(); f.poly([A8,B8,C8]); f.line(B8,E8); f.line(C8,F8); f.dik(G8,B8,C8,.2); f.tick(A8,E8); f.tick(E8,C8); f.tick(A8,F8,2); f.tick(F8,B8,2)
for n_,p_ in (('A',A8),('B',B8),('C',C8)): vtx(f,p_,n_,G8)
f.vl('E',E8,sub(E8,G8),.3); f.vl('F',F8,sub(F8,G8),.3); f.node(bestdir(G8,[A8,B8,C8,E8,F8],.3),'$G$')
SK8=f.svg()
q('0008',tipId='ge-ki-dikko',tip='Dik kesişen kenarortaylar',z='zor',alt='Dik Kenarortaylar',kaz='Dik kesişen iki kenarortayın uzunluklarından kenar uzunluğunu bulur.',
 kart='K-GKI-08 (dik kesişen kenarortaylar) · |BE| = 18, |CF| = 24',
 metin='Şekilde, ABC üçgeninin [BE] ve [CF] kenarortayları ağırlık merkezi G de dik kesişmektedir. E ve F noktaları sırasıyla [AC] ve [AB] kenarlarının orta noktalarıdır. |BE| = 18 cm ve |CF| = 24 cm dir. Şekil ölçekli değildir.\nBuna göre, |BC| kaç cm’dir?',
 dogru=20,yan=[(10,'Ağırlık merkezine uzaklıkları 1/3 oranıyla bulmuş (6 ve 8).','bilgi'),(12,'|BG| yi bulup |BC| olarak vermiş.','dikkat'),(16,'|CG| yi bulup |BC| olarak vermiş.','dikkat'),(30,'Tam kenarortay uzunluklarıyla Pisagor uygulamış: √(18² + 24²).','bilgi')],
 sira=None,
 istenen='|BC| uzunluğu (cm).',
 ip=['G noktası kenarortayları hangi oranda böler? BGC üçgeninin kenarlarından hangileri bu sayede belli olur?'],
 bilgi=[AGR,PIS],
 ad=[A('|BG| yi bul','G, [BE] yi köşeden başlayarak 2 : 1 böler.','|BG| = 2/3 × 18 = 12'),A('|CG| yi bul','Aynı oran [CF] için de geçerlidir.','|CG| = 2/3 × 24 = 16'),A('BGC üçgenini incele','Kenarortaylar G de dik kesiştiğinden BGC üçgeni G de diktir.','|BC|² = |BG|² + |CG|²'),A('Hesapla','Değerleri yaz ve kökü al.','|BC|² = 144 + 256 = 400 → |BC| = 20')],
 puf='Dik kesişen iki doğrunun oluşturduğu üçgen hangisi?',sekil=SK8)

# ===== 09 zor · G, D, E üçgeninin çevresi =====
kartla('K-GKI-09','Orta taban ve ağırlık merkezinin parçaları','Orta taban üçüncü kenarın yarısıdır; ağırlık merkezi kenarortayın kenar tarafındaki 1/3 ünü ayırır; üç uzunluk toplanır.','Parça oranını 1/2 ya da 2/3 almak; orta tabanı üçüncü kenara eşit almak; yanlış üçgenin çevresini bulmak.','orta',4,'ge-ki-cevre','Kenarortaylı üçgenlerde çevre')
BC9=18; BE9=21; CD9=15; DE9=BC9//2; GD9=CD9//3; GE9=BE9//3; assert (DE9,GD9,GE9)==(9,5,7) and DE9+GD9+GE9==21
BG9=2*BE9//3; CG9=2*CD9//3; assert BG9+CG9>BC9 and BC9+CG9>BG9 and BC9+BG9>CG9 and BC9+BG9+CG9==42
assert Fr(CD9,2)+Fr(BE9,2)+DE9==27 and 18+5+7==30 and CG9+BG9//1*0+BG9+DE9==33
B9=(0,0); C9=(18,0); xg=(BG9**2+BC9**2-CG9**2)/(2*BC9); yg=sqrt(BG9**2-xg**2); G9r=(xg,yg); A9r=(3*G9r[0]-B9[0]-C9[0],3*G9r[1])
sc=.19; Bs,Cs,As,Gs=[mul(p,sc) for p in (B9,C9,A9r,G9r)]; D9=mid(As,Bs); E9=mid(As,Cs)
assert deger(dist(Bs,mid(As,Cs))/sc,BE9) and deger(dist(Cs,mid(As,Bs))/sc,CD9) and deger(dist(D9,E9)/sc,DE9) and deger(dist(Gs,D9)/sc,GD9) and deger(dist(Gs,E9)/sc,GE9)
ic=cen([As,Bs,Cs]); f=F(); f.fill([D9,Gs,E9]); f.poly([As,Bs,Cs]); f.line(Bs,E9); f.line(Cs,D9); f.line(D9,E9); f.tick(As,D9); f.tick(D9,Bs); f.tick(As,E9,2); f.tick(E9,Cs,2)
for n_,p_ in (('A',As),('B',Bs),('C',Cs)): vtx(f,p_,n_,ic)
f.vl('D',D9,sub(D9,Gs),.3); f.vl('E',E9,sub(E9,Gs),.3); f.node(bestdir(Gs,[Bs,Cs,D9,E9],.3),'$G$')
SK9=f.svg()
q('0009',tipId='ge-ki-cevre',tip='Kenarortaylı üçgenlerde çevre',z='orta',alt='Orta Taban ve G',kaz='Orta taban ve ağırlık merkezi oranlarını birlikte kullanarak üçgenin çevresini bulur.',
 kart='K-GKI-09 (orta taban + ağırlık merkezi) · |BC| = 18, |BE| = 21, |CD| = 15',
 metin='Şekilde, ABC üçgeninin [BE] ve [CD] kenarortayları G noktasında kesişmektedir (D, [AB] nin; E, [AC] nin orta noktasıdır). |BC| = 18 cm, |BE| = 21 cm ve |CD| = 15 cm dir. Şekil ölçekli değildir.\nBuna göre, taralı GDE üçgeninin çevresi kaç cm’dir?',
 dogru=21,yan=[(27,'G nin kenarortayları yarıya böldüğünü sanıp |GD| = 7,5 ve |GE| = 10,5 almış.','bilgi'),(30,'Orta tabanı |BC| ye eşit alıp 18 + 5 + 7 yazmış.','bilgi'),(33,'Parçaları 2/3 oranıyla almış: |GD| = 10, |GE| = 14.','bilgi'),(42,'GDE yerine GBC üçgeninin çevresini hesaplamış (14 + 10 + 18).','dikkat')],
 sira=None,
 istenen='GDE üçgeninin çevresi (cm).',
 ip=['DE doğru parçası ile [BC] arasında nasıl bir ilişki vardır? G, [BE] ve [CD] yi hangi oranlarda böler?'],
 bilgi=[ORT,AGR],
 ad=[A('|DE| yi bul','D ve E orta nokta olduğundan [DE] orta tabandır.','|DE| = 18 ÷ 2 = 9'),A('|GD| yi bul','G, [CD] yi köşeden 2 : 1 böler; kenar tarafındaki parça 1/3 tür.','|GD| = 15 ÷ 3 = 5'),A('|GE| yi bul','Aynı oran [BE] için geçerlidir.','|GE| = 21 ÷ 3 = 7'),A('Çevreyi hesapla','Üç kenarı topla.','9 + 5 + 7 = 21')],
 puf='Çevresi istenen üçgenin her kenarını ayrı bir bilgiyle (orta taban, ağırlık merkezi oranı) bul; sonra topla.',sekil=SK9)

# ===== 10 zor · ağırlık merkezi, orta nokta ve alan =====
kartla('K-GKI-10','İki orta noktalı alan hesabı','Kenarortay alanı yarıya böler; üçgenin bir kenarı üzerindeki nokta, tabanı oranlar; aynı köşeden tabanı oranlanan üçgenlerin alanı bu oranla bölünür.','K yerine G yi kullanmak; K yı [AD] nin orta noktası sanmak; oranı ters yazmak.','zor',5,'ge-ki-alan','Kenarortay ve alan oranları')
T10=72; ABD10=T10//2; AK_AD=Fr(1,3); KD_AD=1-AK_AD; assert KD_AD==Fr(2,3) and ABD10*KD_AD==24
assert ABD10*Fr(1,3)==12 and ABD10*Fr(1,2)==18 and ABD10*Fr(5,6)==30 and ABD10==36
A10=(1.5,4.2); B10=(0,0); C10=(5.6,0); D10=mid(B10,C10); G10=lerp(A10,D10,2/3); K10=mid(A10,G10)
assert deger(dist(K10,D10),2/3*dist(A10,D10)) and deger(alan([K10,B10,D10])*3,alan([A10,B10,D10])*2)
ic=cen([A10,B10,C10]); f=F(); f.fill([K10,B10,D10]); f.poly([A10,B10,C10]); f.line(A10,D10); f.line(B10,K10); f.tick(B10,D10); f.tick(D10,C10); f.tick(A10,K10,2); f.tick(K10,G10,2)
for n_,p_ in (('A',A10),('B',B10),('C',C10)): vtx(f,p_,n_,ic)
f.vl('D',D10,(0,-1),.3); f.vl('K',K10,(1,.15),.3); f.vl('G',G10,(1,.15),.3)
SK10=f.svg()
q('0010',tipId='ge-ki-alan',tip='Kenarortay ve alan oranları',z='zor',alt='İki Orta Noktalı Alan',kaz='Ağırlık merkezi ve bir orta nokta yardımıyla küçük üçgenin alanını oranlarla hesaplar.',
 kart='K-GKI-10 (G ve K orta nokta, alan) · alan(ABC) = 72',
 metin='Şekilde G, ABC üçgeninin ağırlık merkezidir. D noktası [BC] nin orta noktası, K noktası ise [AG] nin orta noktasıdır. Üçgenin alanı 72 cm² dir ve şekil ölçekli değildir.\nBuna göre, taralı KBD üçgeninin alanı kaç cm²’dir?',
 dogru=24,yan=[(12,'K yerine G yi kullanıp |GD| = |AD| / 3 almış: alan(GBD) = 36 ÷ 3.','dikkat'),(18,'K yı [AD] nin orta noktası sanmış: |KD| = |AD| / 2.','bilgi'),(30,'|AK| yı |AD| nin 1/6 sı almış: |KD| = 5/6 |AD|.','bilgi'),(36,'KBD yerine ABD üçgeninin alanını vermiş.','dikkat')],
 sira=None,
 istenen='KBD üçgeninin alanı (cm²).',
 ip=['KBD ve ABD üçgenlerinin B den [AD] ye inen yüksekliği aynıdır. Tabanları arasındaki oran ne olmalı?'],
 bilgi=[AGR,ALN],
 ad=[A('ABD nin alanını bul','D orta nokta olduğundan [AD] alanı yarıya böler.','alan(ABD) = 72 ÷ 2 = 36'),A('|AG| yi |AD| cinsinden yaz','G, [AD] yi 2 : 1 böler.','|AG| = 2/3 |AD|'),A('K nın konumunu bul','K, [AG] nin orta noktasıdır.','|AK| = 1/3 |AD| → |KD| = 2/3 |AD|'),A('Alanı oranla','ABD ve KBD üçgenleri B den aynı yüksekliğe sahiptir; alanlar tabanlarla orantılıdır.','alan(KBD) = 36 × 2/3'),A('Hesapla','Sonuç.','24')],
 puf='Aynı köşeden inen yükseklik ortaksa alan oranı taban oranına eşittir; tabanı oluşturan parçaları önce [AD] cinsinden yaz.',sekil=SK10)

bitir_geo(ONEK,'Kenarortay')
