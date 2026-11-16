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
P=Parti('eslik','Eşlik ve Benzerlik','geo|Eşlik ve Benzerlik',ders='TYT Geometri',idon='tytgeo')
ESL=B('Eşlik','iki üçgen KAK, AKA ya da KKK koşullarından birini sağlarsa eştir; eş üçgenlerde karşılıklı kenarlar ve açılar eşittir. Köşelerin yazım sırası karşılıklı köşeleri gösterir: ABC ≅ DEF ise A↔D, B↔E, C↔F. Örnek: ABC ≅ DEF ise |AB| = |DE|')
BNZ=B('Benzerlik','iki üçgenin açıları (AA) ya da kenar oranları eşitse üçgenler benzerdir; karşılıklı kenarların oranı sabittir (benzerlik oranı), çevre de aynı oranda değişir. Örnek: oran 2 ise her kenar 2 katı, çevre de 2 katıdır')
OLC=B('Harita ölçeği','haritadaki uzunluk ile gerçek uzunluğun oranı her yerde aynıdır (ölçek). Örnek: haritada 2 cm gerçekte 10 km ise 1 cm = 5 km ve haritada 3 cm gerçekte 15 km’dir')
GOL=B('Gölge ve benzerlik','aynı anda güneş ışınları paraleldir; cisim, gölgesi ve ışın dik üçgenler oluşturur ve bu üçgenler benzerdir: boy / gölge oranı aynıdır. Örnek: 2 m’lik direğin gölgesi 3 m ise gölgesi 6 m olan cismin boyu 4 m’dir')
OKL=B('Öklid bağıntısı','dik üçgende hipotenüse inen yükseklik üçgeni benzer iki üçgene ayırır; dik kenarın karesi, hipotenüs ile o kenarın hipotenüs üzerindeki izdüşümünün çarpımına eşittir: c² = p × a. Örnek: c = 6, a = 10 ise p = 3,6')
PIS=B('Pisagor bağıntısı','dik üçgende dik kenarların kareleri toplamı hipotenüsün karesine eşittir. Örnek: 3, 4, 5 üçgeni için 3² + 4² = 5²')

# ===== 01 · eşlik, karşılıklı kenar · kolay =====
konu('geo|Eşlik ve Benzerlik','Eşlik ve Benzerlik')
kartla('K-GES-01','Eş üçgenlerde karşılıklı kenar','Eş üçgenlerin karşılıklı kenarları eşittir; eşleşme köşe sırasından okunur ve denklem kurulur.','Eşleşmeyi harf sırasına bakmadan kurmak; x’i cevap sanmak.','kolay',3,'ge-es-esit-eleman','Eş üçgenlerde karşılıklı elemanlar')
x1=7; assert 2*x1+1==x1+8==15
A1=(0,0); B1=(4.0,0); C1=(1.1,2.5); th=33; Dv=(5.7,.6)
D1=add(Dv,rot(A1,th)); E1=add(Dv,rot(B1,th)); F1=add(Dv,rot(C1,th))
assert abs(dist(A1,B1)-dist(D1,E1))<1e-9 and abs(ang(A1,B1,C1)-ang(D1,E1,F1))<1e-9
f=F(); f.poly([A1,B1,C1]); f.poly([D1,E1,F1]); i1=cen([A1,B1,C1]); i2=cen([D1,E1,F1])
f.tick(B1,C1); f.tick(E1,F1); f.tick(A1,C1,2); f.tick(D1,F1,2)
f.sl('$2x+1$',A1,B1,i1,.35); f.sl('$x+8$',D1,E1,i2,.35)
for n_,p_ in (('A',A1),('B',B1),('C',C1)): vtx(f,p_,n_,i1)
for n_,p_ in (('D',D1),('E',E1),('F',F1)): vtx(f,p_,n_,i2)
SK1=f.svg()
q('0001',tipId='ge-es-esit-eleman',tip='Eş üçgenlerde karşılıklı elemanlar',z='kolay',alt='Eş Üçgenler',kaz='Eş üçgenlerde karşılıklı kenarları eşitleyerek bilinmeyeni bulur.',
 kart='K-GES-01 (eş üçgen, karşılıklı kenar) · 2x + 1 = x + 8',
 metin='Şekilde ABC ve DEF üçgenleri, ABC ≅ DEF olacak biçimde çizilmiştir. Aynı sayıda çentik taşıyan kenarlar birbirine eşittir; uzunluklar aynı birimle verilmiştir. |AB| = 2x + 1 ve |DE| = x + 8 birimdir.\nBuna göre, |AB| kaç birimdir?',
 dogru=15,yan=[(7,'x değerini bulup |AB| yerine onu yazmış.','dikkat'),(17,'1’i karşı tarafa geçirmeyi unutup x = 8 bulmuş: 2 × 8 + 1 = 17.','islem'),(22,'x ile |AB| uzunluklarını toplamış: 7 + 15 = 22.','dikkat'),(30,'Eşit uzunlukları toplamış: 15 + 15 = 30.','dikkat')],
 istenen='|AB| uzunluğu.',
 ip=['ABC ≅ DEF yazımında hangi köşeler birbirine karşılık gelir? Buna göre hangi kenar |AB| ye eşittir?'],
 bilgi=[ESL],
 ad=[A('Karşılıklı kenarı bul','ABC ≅ DEF olduğundan A ↔ D ve B ↔ E karşılıklıdır; |AB| = |DE|.','2x + 1 = x + 8'),A('x’i bul','Bilinmeyenleri bir tarafa topla.','x = 7'),A('|AB| yi hesapla','Bulunan x ile uzunluğu yaz.','|AB| = 2 × 7 + 1 = 15')],
 puf='Eş üçgenlerde karşılıklı kenarları köşelerin yazım sırasından bul, sonra eşitle.',sekil=SK1)

# ===== 02 · eşlik koşulları · orta =====
kartla('K-GES-02','Eşlik koşulları','Verilen eşitliklerin KAK, AKA ya da KKK koşullarından birini oluşturup oluşturmadığına bakılır; KKA, AA ve AAA eşlik koşulu değildir.','KKA’yı eşlik koşulu saymak; AAA ya da AA’yı eşlik sanmak.','orta',4,'ge-es-kosul','Eşlik koşulları (KAK, AKA, KKK)')
A2_=(0,0); B2_=(4.2,0); C2_=(1.5,2.6)
D2_=(5.6,.3); E2_=add(D2_,(4.0,0)); F2_=add(D2_,(2.6,1.9))
f=F(); f.poly([A2_,B2_,C2_]); f.poly([D2_,E2_,F2_]); i1=cen([A2_,B2_,C2_]); i2=cen([D2_,E2_,F2_])
for n_,p_ in (('A',A2_),('B',B2_),('C',C2_)): vtx(f,p_,n_,i1)
for n_,p_ in (('D',D2_),('E',E2_),('F',F2_)): vtx(f,p_,n_,i2)
SK2=f.svg()
S_A='|AB| = |DE| ve |BC| = |EF|'; S_B='m(A) = m(D) ve m(B) = m(E)'; S_C='|AB| = |DE|, |AC| = |DF| ve m(A) = m(D)'
S_D='|AB| = |DE|, |BC| = |EF| ve m(A) = m(D)'; S_E='m(A) = m(D), m(B) = m(E) ve m(C) = m(F)'
q('0002',tipId='ge-es-kosul',tip='Eşlik koşulları (KAK, AKA, KKK)',z='orta',alt='Eşlik Koşulları',kaz='Verilen eşitliklerin eşlik koşulu oluşturup oluşturmadığını belirler.',
 kart='K-GES-02 (eşlik koşulları) · KAK doğru; KKA, AA, AAA eşlik koşulu değil',
 metin='Şekilde, köşeleri A, B, C ve D, E, F olan iki üçgen çizilmiştir; üçgenlerin kenar ve açıları hakkında şekil bilgi vermemektedir.\nAşağıdaki eşitlik gruplarından hangisi doğru ise ABC ve DEF üçgenlerinin eş olduğu kesinlikle söylenebilir?',
 dogru=S_C,sira=[S_A,S_B,S_C,S_D,S_E],yan=[(S_A,'İki kenar eşitliğini yeterli saymış; eşlik için bu kenarların arasındaki açı ya da üçüncü kenar da gerekir.','bilgi'),(S_B,'İki açı eşitliği benzerlik koşuludur (AA); eşlik için bir kenar eşitliği de gerekir.','bilgi'),(S_D,'Eşit açının, eşit iki kenarın arasında olmadığını fark etmemiş (KKA), eşlik koşulu sanmış.','dikkat'),(S_E,'Üç açı eşitliğini (AAA) eşlik sanmış; bu yalnız benzerlik verir.','bilgi')],
 istenen='Eşliği kesinlikle sağlayan eşitlik grubu.',
 ip=['Her grupta açıların, eşit olan kenarlara göre konumuna bak: açı iki eşit kenarın arasında mı, yoksa bir kenarın karşısında mı?'],
 bilgi=[ESL],
 ad=[A('Koşulları hatırla','Eşlik için KAK, AKA ya da KKK gerekir.','KAK · AKA · KKK'),A('Grupları ele','Yalnız kenar ya da yalnız açı grupları ya da açı kenarın karşısındaysa eşlik kesin olmaz.','Yalnız kenar (2): yetmez · yalnız açı (2 ya da 3): yetmez · KKA: yetmez'),A('Doğru grubu bul','|AB| = |DE| ve |AC| = |DF| kenarlarının arasındaki A ve D açıları eşit.','Kenar–Açı–Kenar → eş')],
 puf='Eşlikte açı, eşit iki kenarın arasında olmalıdır; kenarlar ve karşılarındaki açı (KKA) ya da yalnız açılar eşlik vermez.',sekil=SK2)

# ===== 03 · harita ölçeği, alan · orta · hikâyeli =====
kartla('K-GES-03','Harita ölçeği ve alan','Haritadaki bir uzunluğun gerçeği bilinirse ölçek bulunur; alan, uzunluk oranının karesiyle büyür.','Alanı uzunluk oranıyla çarpmak; dik kenarların çarpımını alan sanmak.','orta',4,'ge-es-harita','Harita ölçeği ile gerçek alan')
l1,l2=3,4; gerc=6; k3=gerc/l1; aharita=l1*l2/2; agercek=aharita*k3**2; assert agercek==24 and k3==2
Bm=(0,0); Cm_=(4*.7,0); Am=(0,3*.7)
f=F(); f.poly([Am,Bm,Cm_]); f.dik(Bm,Am,Cm_); ic=cen([Am,Bm,Cm_])
f.sl('$3$ cm',Am,Bm,ic,.45); f.sl('$4$ cm',Bm,Cm_,ic,.3)
f.node(Am,'$\\bullet$'); f.node(Bm,'$\\bullet$'); f.node(Cm_,'$\\bullet$')
f.vl('A',Am,(-.6,.8),.3); f.vl('B',Bm,(-1,-.7),.3); f.vl('C',Cm_,(1,-.6),.3)
SK3=f.svg()
assert sorted([6,12,14,24,48])==sorted([aharita,aharita*k3,gerc+8,agercek,gerc*8])
q('0003',tipId='ge-es-harita',tip='Harita ölçeği ile gerçek alan',z='orta',kalip='hikâyeli',alt='Harita ve Ölçek',kaz='Haritadaki uzunluk–gerçek uzunluk ilişkisinden ölçeği bulup gerçek alanı hesaplar.',
 kart='K-GES-03 (harita ölçeği, alan) · 3-4 cm dik üçgen, |AB| gerçekte 6 km',
 metin='Bir milli parkın üçgen biçimli ABC koruma alanı, haritada şekildeki gibi dik üçgen olarak gösterilmiştir. Haritada |AB| = 3 cm olan kenarın gerçek uzunluğu 6 km, haritada |BC| = 4 cm dir; haritanın her yerinde aynı ölçek kullanılmıştır.\nBuna göre, koruma alanının gerçek alanı kaç km²’dir?',
 dogru=24,yan=[(6,'Haritadaki alanı (6 cm²) ölçeği uygulamadan km² yazmış.','dikkat'),(12,'Alanı yalnız uzunluk oranıyla (2) çarpmış: 6 × 2 = 12 (oranın karesini almamış).','islem'),(14,'Gerçek dik kenarları (6 ve 8 km) toplamış: 6 + 8 = 14.','dikkat'),(48,'Gerçek dik kenarları çarpıp ikiye bölmeyi unutmuş: 6 × 8 = 48.','islem')],
 istenen='Gerçek alan (km²).',
 ip=['Önce haritadaki 1 cm’nin gerçekte kaç km olduğunu bul; sonra gerçek dik kenarları hesapla.'],
 bilgi=[OLC],
 ad=[A('Ölçeği bul','Haritada 3 cm gerçekte 6 km’dir.','1 cm = 2 km'),A('Gerçek kenarları bul','Dik üçgenin dik kenarları ölçekle büyür.','|AB| = 6 km · |BC| = 4 × 2 = 8 km'),A('Alanı hesapla','Dik üçgenin alanı dik kenarların çarpımının yarısıdır.','6 × 8 ÷ 2 = 24 km²'),A('Kontrol et','Haritadaki alan 6 cm²; alan oranı ölçeğin karesidir.','6 × 2² = 24')],
 puf='Uzunluk k kat büyürse alan k² kat büyür; alanı ölçekle doğrudan çarpma.',sekil=SK3)

# ===== 04 · gölge · orta · hikâyeli =====
kartla('K-GES-04','Gölge ve benzerlik','Aynı anda güneş ışınları paralel olduğundan boy ve gölge dik üçgenleri benzerdir.','Oranı ters kurmak; gölgeyi yükseklik sanmak.','kolay',3,'ge-es-golge','Gölge problemi')
hp,sp,sa=1.5,1,6; ha=hp/sp*sa; assert ha==9
sc4=.42; Pb=(0,0); Pt=(0,hp*sc4); Ps=(sp*sc4,0); Tb=(2.6,0); Tt=(2.6,ha*sc4); Ts=(2.6+sa*sc4,0)
assert abs((Pt[1]-Ps[1])/(Pt[0]-Ps[0])-(Tt[1]-Ts[1])/(Tt[0]-Ts[0]))<1e-9
f=F(); f.line((-.4,0),(2.6+sa*sc4+.5,0)); f.line(Pb,Pt,'line width=1.6pt'); f.line(Tb,Tt,'line width=1.6pt')
f.line(Pt,Ps,'dashed'); f.line(Tt,Ts,'dashed'); f.dik(Pb,Pt,Ps,.12); f.dik(Tb,Tt,Ts,.15)
f.node((Pb[0]-.55,hp*sc4/2),'$1{,}5$ m'); f.node((sp*sc4/2,-.32),'$1$ m'); f.node((2.6+sa*sc4/2,-.32),'$6$ m'); f.node((Tb[0]-.35,ha*sc4/2),'$h$')
f.node((Pb[0]+.1,hp*sc4+.35),'Kişi'); f.node((Tt[0],Tt[1]+.3),'Ağaç')
SK4=f.svg()
assert sorted([4,6,6.5,7.5,9])==sorted([sa*sp/hp,sa,hp+sa-sp,(sa-sp)*hp,ha])
q('0004',tipId='ge-es-golge',tip='Gölge problemi',z='kolay',kalip='hikâyeli',alt='Gölge Problemi',kaz='Aynı anda oluşan gölgelerden benzerlik oranıyla cisim boyunu bulur.',
 kart='K-GES-04 (gölge) · 1,5 m kişi, 1 m gölge, 6 m ağaç gölgesi',
 metin='Güneşli bir günde, aynı anda boyu 1,5 m olan bir kişinin gölgesi 1 m, bir ağacın gölgesi ise 6 m ölçülüyor. Kişi ve ağaç yere dik, zemin düzdür. Şekil ölçekli değildir.\nBuna göre, ağacın boyu h kaç metredir?',
 dogru=9,yan=[(4,'Oranı ters kurmuş: h = 6 × 1 ÷ 1,5 = 4.','dikkat'),(6,'Ağacın gölgesini boy sanmış.','dikkat'),(6.5,'Orantı yerine farkları kullanmış: 1,5 + (6 − 1) = 6,5.','islem'),(7.5,'Gölgelerin farkını kişi boyuyla çarpmış: (6 − 1) × 1,5 = 7,5.','islem')],
 istenen='Ağacın boyu h (m).',
 ip=['Güneş ışınları paralel olduğu için kişi ve ağaçla oluşan iki dik üçgen birbirine benzerdir; boy / gölge oranını eşitle.'],
 bilgi=[GOL],
 ad=[A('Benzer üçgenleri belirle','Kişi + gölgesi ve ağaç + gölgesi iki dik üçgendir; ışınlar paralel olduğundan açılar eşittir.','AA benzerliği'),A('Oranı kur','Boy / gölge oranı iki üçgende de aynıdır.','1,5 / 1 = h / 6'),A('h’yi bul','İçler dışlar çarpımı.','h = 1,5 × 6 = 9 m')],
 puf='Gölge sorularında aynı anda ölçüm yapıldığı için boy ÷ gölge oranı sabittir.',sekil=SK4)

# ===== 05 · eşlik KKK, deltoid · orta =====
kartla('K-GES-05','Köşegenle bölünen dörtgende eşlik','İki çift eşit kenar ve ortak köşegen KKK ile eş üçgenler verir; eş üçgenlerin karşılıklı açıları eşitlenip denklem kurulur.','Karşılıklı açıları yanlış eşleştirmek; x’i cevap sanmak; yalnız bir tarafın açısını ikiye katlamayı unutmak.','orta',4,'ge-es-kkk','KKK eşliği ve karşılıklı açılar')
x5=25; assert 2*x5+20==4*x5-30==70
L=4.2; th=radians(40); A5_=(0,0); C5_=(L,0); B5_=(L*cos(th),L*sin(th)); D5_=(L*cos(th),-L*sin(th))
assert abs(dist(A5_,B5_)-dist(A5_,D5_))<1e-9 and abs(dist(B5_,C5_)-dist(D5_,C5_))<1e-9
assert abs(ang(B5_,A5_,C5_)-70)<1e-9 and abs(ang(D5_,A5_,C5_)-70)<1e-9 and abs(ang(C5_,B5_,D5_)-140)<1e-9
f=F(); f.poly([A5_,B5_,C5_,D5_]); f.line(A5_,C5_); f.tick(A5_,B5_); f.tick(A5_,D5_); f.tick(B5_,C5_,2); f.tick(D5_,C5_,2)
f.node(add(B5_,(1.15,.1)),'$(2x+20)^\\circ$'); f.node(add(D5_,(1.15,-.1)),'$(4x-30)^\\circ$'); f.node((1.55,.5),'$40^\\circ$')
f.arc(B5_,A5_,C5_,.45); f.arc(D5_,A5_,C5_,.45); f.arc(A5_,B5_,C5_,.9)
f.vl('A',A5_,(-1,0),.3); f.vl('B',B5_,(0,1),.3); f.vl('C',C5_,(1,0),.3); f.vl('D',D5_,(0,-1),.3)
SK5=f.svg()
assert sorted([25,70,80,110,140])==sorted([x5,70,80,180-70,140])
q('0005',tipId='ge-es-kkk',tip='KKK eşliği ve karşılıklı açılar',z='orta',alt='KKK Eşliği',kaz='KKK ile eş üçgenleri bulup karşılıklı açıları eşitleyerek açı hesaplar.',
 kart='K-GES-05 (KKK, deltoid) · 2x + 20 = 4x − 30, BAC = 40°',
 metin='Şekildeki ABCD dörtgeninde çentikli kenarlar kendi aralarında eşittir: |AB| = |AD| ve |BC| = |DC|. m(BAC) = 40°, m(ABC) = (2x + 20)° ve m(ADC) = (4x − 30)° dir. Şekil ölçekli değildir.\nBuna göre, m(BCD) kaç derecedir?',
 dogru=140,yan=[(25,'Bulduğu x değerini açı olarak vermiş.','dikkat'),(70,'Yalnız m(ACB) = 70° açısını bulup m(BCD) için ikiye katlamamış.','dikkat'),(80,'Üçgenin tepe açısını (m(BAD) = 80°) istenen açı sanmış.','dikkat'),(110,'m(BCD) yerine 180° − 70° = 110° yazmış (dış açıyla karıştırmış).','bilgi')],
 istenen='m(BCD) açısının ölçüsü.',
 ip=['ABC ve ADC üçgenlerinin kenarlarına bak: hangi eşlik koşulu sağlanıyor? Eş üçgenlerde hangi açılar eşittir?'],
 bilgi=[ESL],
 ad=[A('Eşliği kur','|AB| = |AD|, |BC| = |DC| ve [AC] ortak olduğundan ABC ≅ ADC (KKK).','m(ABC) = m(ADC)'),A('x’i bul','Eş üçgenlerde karşılıklı açılar eşittir.','2x + 20 = 4x − 30 → x = 25 → m(ABC) = 70°'),A('m(ACB) yi bul','ABC üçgeninin iç açıları toplamı 180°.','m(ACB) = 180° − 40° − 70° = 70°'),A('m(BCD) yi yaz','Eş üçgenlerden m(ACD) = m(ACB).','m(BCD) = 70° + 70° = 140°')],
 puf='Köşegenle bölünen dörtgende iki çift eşit kenar ve ortak köşegen KKK’dır: karşılıklı açıları eşitle.',sekil=SK5)

# ===== 06 · kare içinde eş üçgenler · zor =====
kartla('K-GES-06','Kare içinde eşlik ve Öklid','Kare içinde eş üçgenlerden dik açı bulunur; dik üçgende yükseklik bağıntısıyla parçalar hesaplanır.','Eşliği fark etmeyip uzunlukları şekilden tahmin etmek; parçaları karıştırmak.','zor',5,'ge-es-kare-oklid','Kare içinde eş üçgenler ve Öklid')
a6,be6=20,15; AE6=25; AP6=a6*a6//AE6; assert AP6==16 and AE6-AP6==9 and a6**2+be6**2==AE6**2
BP6=a6*be6//AE6; assert BP6==12
s=.2; A6=(0,0); B6=(a6*s,0); C6=(a6*s,a6*s); D6=(0,a6*s); E6=(a6*s,be6*s); F6=((a6-be6)*s,a6*s)
P6=kesis(A6,E6,B6,F6)
assert abs(dist(P6,B6)/s-12)<1e-9 and abs(dist(A6,P6)/s-16)<1e-9 and abs(dist(P6,E6)/s-9)<1e-9 and abs(ang(P6,A6,B6)-90)<1e-9
f=F(); f.poly([A6,B6,C6,D6]); f.line(A6,E6); f.line(B6,F6)
f.tick(B6,E6); f.tick(C6,F6)
f.sl('$20$',A6,B6,C6,.3); f.sl('$15$',B6,E6,A6,.3)
for n_,p_ in (('A',A6),('B',B6),('C',C6),('D',D6)): vtx(f,p_,n_,cen([A6,B6,C6,D6]))
f.vl('E',E6,(1,.1),.3); f.vl('F',F6,(-.1,1),.3); f.vl('P',P6,(-1,-.05),.36)
SK6=f.svg()
assert sorted([9,12,15,16,25])==sorted([AE6-AP6,BP6,be6,AP6,AE6])
q('0006',tipId='ge-es-kare-oklid',tip='Kare içinde eş üçgenler ve Öklid',z='zor',alt='Kare İçinde Eşlik',kaz='Kare içinde eş üçgenleri bularak dik açıyı belirler ve Öklid ile uzunluk hesaplar.',
 kart='K-GES-06 (eş üçgen + Öklid) · AB = 20, BE = CF = 15',
 metin='Şekildeki ABCD karesinde E ∈ [BC], F ∈ [CD] dir. [AE] ile [BF] doğru parçaları P noktasında kesişmektedir. Çentikli kenarların uzunlukları eşittir; |AB| = 20 cm ve |BE| = 15 cm dir. Şekil ölçekli değildir.\nBuna göre, |PE| kaç cm’dir?',
 dogru=9,yan=[(12,'|PE| yerine |BP| = 12 uzunluğunu bulmuş.','dikkat'),(15,'Çentikli kenar uzunluğunu |PE| sanmış.','dikkat'),(16,'|PE| yerine |AP| = 16 uzunluğunu bulmuş.','dikkat'),(25,'|PE| yerine |AE| = 25 hipotenüsünü vermiş.','dikkat')],
 istenen='|PE| uzunluğu (cm).',
 ip=['ABE ve BCF üçgenlerinin eş olduğunu görürsen m(APB) açısı hakkında bir sonuca ulaşırsın; bu sonuç hangi üçgende yüksekliği verir?'],
 bilgi=[ESL,PIS,OKL],
 ad=[A('Eşliği kur','|AB| = |BC|, m(ABE) = m(BCF) = 90° ve |BE| = |CF| olduğundan ABE ≅ BCF (KAK).','m(BAE) = m(CBF)'),A('Dik açıyı bul','ABP üçgeninde m(BAP) + m(ABP) = m(CBF) + m(ABP) = 90° olur.','m(APB) = 90° → [BP] ⊥ [AE]'),A('|AE| yi bul','ABE dik üçgeninde Pisagor.','|AE|² = 20² + 15² = 625 → |AE| = 25'),A('Öklid uygula','ABE dik üçgeninde [BP] hipotenüse inen yüksekliktir: |AB|² = |AP| × |AE|.','400 = |AP| × 25 → |AP| = 16'),A('|PE| yi hesapla','Hipotenüs iki parçanın toplamıdır.','|PE| = 25 − 16 = 9')],
 puf='Karede eş üçgenler çoğu zaman dik kesişim verir; dik kesişim varsa Öklid bağıntısını dene.',sekil=SK6)
bitir_geo('eslik','Eşlik ve Benzerlik')
