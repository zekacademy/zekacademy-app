"""TYT Geometri · Küp (kardeş yok, ipucu 1). Şekil koordinatları hesaplanır; TikZ gövdesi aynı değerlerden üretilir (cizim.tikz_svg).
3B şekiller eğik görünümle (ön yüz gerçek oran, derinlik yarı kısaltılmış) çizilir; gizli kenarlar yüz görünürlüğünden hesaplanıp kesikli çizilir.
Her cevap ve çeldirici değer Python hesabıyla assert edilir."""
import sys,os,math,json
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
from math import sin,cos,tan,radians,degrees,atan2,sqrt,pi
TIPK={}
def konu(k,ad): P.k=k; P.konu_adi=ad; H.KONU=ad
def kartla(id,alt,fikir,tuzak,z,adim,tipId,tip,kaynak=None):
    kart(id,alt,fikir,tuzak,z,'şekilli',adim,tipId,tip,kaynak or 'ÖSYM 2018–2026 TYT Geometri soruları (yalnız mantık) · MEB 9–10. sınıf geometri'); TIPK[tipId]=P.k
def q(no,ad,kalip='şekilli',**k): mk(P,no,ad=ad,adim=len(ad),kalip=kalip,**k)
# ---------------- çizim yardımcıları (cm cinsinden koordinatlar) ----------------
def add(p,q_): return tuple(a+b for a,b in zip(p,q_))
def sub(p,q_): return tuple(a-b for a,b in zip(p,q_))
def mul(p,s): return tuple(a*s for a in p)
def ln(p): return math.sqrt(sum(a*a for a in p))
def un(p): n=ln(p); return tuple(a/n for a in p)
def mid(p,q_): return tuple((a+b)/2 for a,b in zip(p,q_))
def lerp(p,q_,t): return tuple(a+(b-a)*t for a,b in zip(p,q_))
def dist(p,q_): return ln(sub(p,q_))
def cen(ps): return tuple(sum(p[i] for p in ps)/len(ps) for i in range(len(ps[0])))
def pt(p): return f'({p[0]:.3f},{p[1]:.3f})'
def ang(V,a,b):
    u=sub(a,V); v=sub(b,V); return degrees(math.acos(sum(x*y for x,y in zip(u,v))/(ln(u)*ln(v))))
def alan(ps): return abs(sum(ps[i][0]*ps[(i+1)%len(ps)][1]-ps[(i+1)%len(ps)][0]*ps[i][1] for i in range(len(ps))))/2
class F:
    def __init__(s): s.o=[]
    def raw(s,t): s.o.append(t)
    def line(s,p,q_,st=''): s.o.append(f'\\draw[{st}] {pt(p)} -- {pt(q_)};')
    def poly(s,ps,st=''): s.o.append(f'\\draw[{st}] '+' -- '.join(map(pt,ps))+' -- cycle;')
    def fill(s,ps,st='fill=vurgu!25'): s.o.append(f'\\fill[{st}] '+' -- '.join(map(pt,ps))+' -- cycle;')
    def node(s,p,t,st=''): s.o.append(f'\\node[{st}] at {pt(p)} {{{t}}};')
    def vl(s,t,p,dv,d=.3): s.node(add(p,mul(un(dv),d)),f'${t}$')
    def sl(s,t,p,q_,ic,d=.3):
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
    def body(s): return '\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'+'\n'.join(s.o)+'\n\\end{tikzpicture}'
    def svg(s): return tikz_svg(s.body())
# ---- 3B: eğik görünüm (x sağ, y derinlik, z yukarı); ön yüz (y sabit) gerçek oranda, derinlik yarı kısaltılmış ----
KA=radians(40); KK=.5
def proj(p,k=KK,al=KA): return (p[0]+k*p[1]*cos(al),p[2]+k*p[1]*sin(al))
W=(KK*cos(KA),-1,KK*sin(KA))      # gözlemciye doğru yön: ön, sağ ve üst yüzler görünür
class Solid:
    """V: ad->3B nokta; faces: ad->(köşe adları sırayla, DIŞ normal). Gizli kenar = komşu yüzlerin hiçbiri görünür değil."""
    def __init__(s,V,faces,sc=.4):
        s.V=V; s.faces=faces; s.sc=sc
        s.vis={k:sum(n[i]*W[i] for i in range(3))>1e-9 for k,(vs,n) in faces.items()}
        ed={}
        for k,(vs,n) in faces.items():
            for i in range(len(vs)):
                e=tuple(sorted((vs[i],vs[(i+1)%len(vs)]))); ed.setdefault(e,[]).append(k)
        for e,fs in ed.items(): assert len(fs)==2,('kenar iki yüze ait olmalı',e,fs)
        s.edges=ed; s.Q={k:mul(proj(v),sc) for k,v in V.items()}
    def hidden(s,e): return not any(s.vis[k] for k in s.edges[tuple(sorted(e))])
    def hid_list(s): return sorted(''.join(e) for e in s.edges if s.hidden(e))
    def draw(s,f,st='',gst='dashed'):
        for e in s.edges: f.line(s.Q[e[0]],s.Q[e[1]],gst if s.hidden(e) else st)
    def fillface(s,f,name,st='fill=vurgu!25'): f.fill([s.Q[v] for v in s.faces[name][0]],st)
def kutu(a,b,c,sc=.4,o=(0,0,0)):
    """a (x), b (derinlik y), c (yükseklik z) ayrıtlı dikdörtgenler prizması; köşe adları A B C D (taban) E F G H (üst)."""
    x,y,z=o
    V={'A':(x,y,z),'B':(x+a,y,z),'C':(x+a,y+b,z),'D':(x,y+b,z),'E':(x,y,z+c),'F':(x+a,y,z+c),'G':(x+a,y+b,z+c),'H':(x,y+b,z+c)}
    FC={'taban':('ADCB',(0,0,-1)),'ust':('EFGH',(0,0,1)),'on':('ABFE',(0,-1,0)),'arka':('DHGC',(0,1,0)),'sol':('ADHE',(-1,0,0)),'sag':('BCGF',(1,0,0))}
    return Solid(V,FC,sc)
RV={}
def Rd(k,r):
    """k√r biçimli metin (RV'ye değeri kaydedilir)."""
    s=(str(k) if r==1 else ('' if k==1 else str(k))+'√'+str(r)) if k!=0 else '0'; RV[s]=k*sqrt(r); return s
def Pm(a,b):
    s=f'{a} − {b}π' if b!=1 else f'{a} − π'; RV[s]=a-b*pi; return s
def Pk(k):
    s=f'{k}π' if k!=1 else 'π'; RV[s]=k*pi; return s
def Rp(a,k,r):
    s=f'{a} + {Rd(k,r)}'; RV[s]=a+k*sqrt(r); return s
def sirala(*ss): return sorted(ss,key=lambda t:RV[t])
def say(s): return s
P=Parti('kup','Küp','geo|Küp',ders='TYT Geometri',idon='tytgeo')
def lbl(f,S,p,q_,t,off): f.node(add(mid(S.Q[p],S.Q[q_]),off),t)
def Nn(x): s=str(x); RV[s]=float(x); return s
def izgara(f,S,a,n,st='thin,gray'):
    sc=S.sc; c=a/n
    for i in range(1,n):
        t=i*c
        for (p,q_) in [((t,0,0),(t,0,a)),((0,0,t),(a,0,t)),((a,t,0),(a,t,a)),((a,0,t),(a,a,t)),((t,0,a),(t,a,a)),((0,t,a),(a,t,a))]:
            f.line(mul(proj(p),sc),mul(proj(q_),sc),st)
KOSEGEN=B('Küpün köşegenleri','ayrıtı a olan küpün yüz köşegeni a√2, cisim köşegeni a√3 tür; küpün 12 ayrıtı, 6 yüzü ve 8 köşesi vardır. Örnek: ayrıtı 4 olan küpün yüz köşegeni 4√2, cisim köşegeni 4√3 tür')
KUPALAN=B('Küpün alanı ve hacmi','ayrıtı a olan küpün bir yüzünün alanı a², tüm yüzey alanı 6a², hacmi a³ tür. Örnek: a = 3 için yüzey alanı 54, hacim 27’dir')
ESKENAR=B('Eşkenar üçgenin alanı','kenarı a olan eşkenar üçgenin alanı (a² × √3) ÷ 4 tür. Örnek: kenarı 4 olan eşkenar üçgenin alanı 16√3 ÷ 4 = 4√3 tür')
BOYAK=B('Boyanıp bölünen küp','dış yüzü boyanıp küçük küplere bölünen büyük küpte küçük küpler konumlarına göre ayrılır: köşelerdekilerin 3, ayrıtlar üzerindekilerin (köşeler hariç) 2, yüzlerin içindekilerin 1 yüzü boyalıdır; tam içte kalanların hiç yüzü boyalı değildir')
ACINIM=B('Küpün açınımı ve en kısa yol','yüzey üzerindeki en kısa yol, yüzler aynı düzleme serilince iki nokta arasındaki doğru parçasıdır. Örnek: ayrıtı 3 olan küpte, yan yana serilmiş iki kare 3 × 6 lık dikdörtgen oluşturur; köşegeni √(9 + 36) = 3√5 tir')
PIS=B('Pisagor bağıntısı','dik üçgende dik kenarların kareleri toplamı hipotenüsün karesine eşittir. Örnek: dik kenarları 6 ve 8 olan üçgende hipotenüs 10’dur')
KALAN=B('Köşesi kesilen küpün yüzey alanı','köşeyi kesen düzlem üç yüzden dik üçgenler götürür ve yerine yeni bir üçgen yüz ekler; kalan alan = 6a² − götürülen üçgenler + yeni üçgen. Örnek: köşeden ayrıtlar üzerinde 1 birim uzaklıktan kesilirse üç yüzden 1/2 şer birimkare gider')

# =================== 01 · Cisim köşegeni · kolay ===================
konu('geo|Küp','Küp')
kartla('K-GKP-01','Cisim köşegeninden ayrıt','Cisim köşegeni a√3 olduğundan ayrıt köşegenin √3’e bölümüyle bulunur; küpün 12 ayrıtı vardır.','Cisim köşegenini ayrıt sanmak; ayrıt sayısını 8 ya da 6 almak; hacim hesaplamak.','kolay',3,'ge-kp-kosegen','Küpte yüz ve cisim köşegeni')
a1=6; assert sqrt(3*a1**2)==a1*sqrt(3) and 12*a1==72 and 4*a1==24 and 6*a1==36 and 8*a1==48 and a1**3==216
K1=kutu(a1,a1,a1,sc=.4); f=F(); K1.draw(f); Q=K1.Q
f.line(Q['E'],Q['C'],'dashed'); assert K1.hid_list()==['AD','CD','DH']
mAG=mid(Q['E'],Q['C']); eA=un(sub(Q['C'],Q['E'])); nA=(-eA[1],eA[0])
f.node(add(mAG,mul(nA,.38)),'$6\\sqrt{3}$')
for k,dv in dict(A=(-1,-1),B=(.4,-1),C=(1,-.2),D=(-.4,-1),E=(-1,.5),F=(.2,1),G=(1,.5),H=(-.2,1)).items(): f.vl(k,Q[k],dv,.3)
SK1=f.svg()
q('0001',tipId='ge-kp-kosegen',tip='Küpte yüz ve cisim köşegeni',z='kolay',alt='Cisim Köşegeni',kaz='Küpün cisim köşegeninden ayrıtını bulup tüm ayrıtlarının uzunluğunu hesaplar.',kalip='hikâyeli',
 kart='K-GKP-01 (cisim köşegeni) · |EC| = 6√3, ayrıt toplamı',
 metin='Bir oyuncak firması, şekildeki gibi küp biçiminde ahşap bloklar üretmektedir. Blokların köşegeninin ([EC] doğru parçasının) uzunluğu şekilde cm cinsinden verilmiştir. Her blok, bütün ayrıtları boyunca ince bir renkli şeritle kaplanacaktır; şeridin kalınlığı ve birleşim payı hesaba katılmayacaktır.\nBuna göre, bir blok için kullanılacak şeridin toplam uzunluğu kaç cm dir?',
 dogru=72,yan=[(24,'Yalnız bir yüzün çevresini (4 × 6) bulmuş.','dikkat'),(36,'Küpün 6 ayrıtı olduğunu sanıp 6 × 6 = 36 bulmuş.','bilgi'),(48,'Küpün 8 ayrıtı olduğunu sanıp 8 × 6 = 48 bulmuş (8 köşe sayısıdır).','bilgi'),(216,'Şerit uzunluğu yerine küpün hacmini (6³) hesaplamış.','dikkat')],
 istenen='Şeridin toplam uzunluğu (cm).',
 ip=['Köşegenin hangi iki köşeyi birleştirdiğine bak; istenen uzunluğun hangi ayrıtlardan oluştuğunu düşün.'],
 bilgi=[KOSEGEN],
 ad=[A('Ayrıtı bul','[EC] küpün karşılıklı iki köşesini birleştirdiğinden cisim köşegenidir; ayrıtın √3 katıdır.','a√3 = 6√3 → a = 6 cm'),A('Ayrıt sayısını yaz','Küpün tabanında 4, üst yüzünde 4 ve yan ayrıt olarak 4 ayrıt vardır.','4 + 4 + 4 = 12 ayrıt'),A('Toplam uzunluğu bul','Ayrıt sayısı ile ayrıt uzunluğunu çarp.','12 × 6 = 72')],
 puf='Küpte cisim köşegeni a√3 ise ayrıt a’dır; küpün 12 ayrıtı olduğundan ayrıtların toplamı 12a dır.',sekil=SK1)

# =================== 02 · Yüzey alanından yüz köşegeni · kolay ===================
kartla('K-GKP-02','Yüzey alanından yüz köşegeni','Yüzey alanı 6a² olduğundan ayrıt bulunur; yüz köşegeni ayrıtın √2 katıdır.','Yüz köşegenini ayrıt ya da cisim köşegeni sanmak; yüzey alanını bir yüzün alanı sanmak.','kolay',3,'ge-kp-kosegen','Küpte yüz ve cisim köşegeni')
a2=5; assert 6*a2**2==150 and sqrt(2*a2**2)==a2*sqrt(2) and a2**2==25
K2=kutu(a2,a2,a2,sc=.4); f=F(); K2.draw(f); Q=K2.Q
f.line(Q['B'],Q['E'],''); assert K2.hid_list()==['AD','CD','DH']
mEG=mid(Q['B'],Q['E']); f.node(add(mEG,(.4,.25)),'$x$')
for k_,dv in dict(A=(-1,-1),B=(.4,-1),C=(1,-.2),D=(-.4,-1),E=(-1,.5),F=(1,-.3),G=(1,.5),H=(-.2,1)).items(): f.vl(k_,Q[k_],dv,.3 if k_!='F' else .38)
SK2=f.svg()
q('0002',tipId='ge-kp-kosegen',tip='Küpte yüz ve cisim köşegeni',z='kolay',alt='Yüz Köşegeni',kaz='Küpün yüzey alanından ayrıtını bulup yüz köşegeninin uzunluğunu hesaplar.',kalip='hikâyeli',
 kart='K-GKP-02 (yüzey alanından yüz köşegeni) · yüzey alanı 150',
 metin='Küp biçiminde bir hediye kutusunun altı yüzünü kaplamak için tam 150 cm² kâğıt kullanılmış, kâğıttan hiç artmamış ve üst üste binen yer olmamıştır. Kutunun ön yüzünde [BE] köşegeni şekildeki gibi çizilmiş ve uzunluğu x ile gösterilmiştir. Şekil ölçekli değildir.\nBuna göre, x kaç cm dir?',
 dogru=Rd(5,2),sira=sirala(Nn(5),Rd(5,2),Rd(5,3),Nn(10),Nn(25)),
 yan=[(Nn(5),'Köşegeni ayrıta eşit sanıp 5 bulmuş.','dikkat'),(Rd(5,3),'Yüz köşegeni yerine cisim köşegenini (a√3) yazmış.','bilgi'),(Nn(10),'Köşegeni iki ayrıt uzunluğu (5 + 5) sanmış.','dikkat'),(Nn(25),'150’yi 6’ya bölüp bir yüzün alanını (25) bulmuş ve bunu uzunluk sanmış.','dikkat')],
 istenen='Ön yüzdeki köşegenin uzunluğu (cm).',
 ip=['Önce yüzey alanından ayrıtı bul; köşegenin hangi şeklin köşegeni olduğuna bak.'],
 bilgi=[KOSEGEN,KUPALAN],
 ad=[A('Bir yüzün alanını bul','Küpün altı eş kare yüzü vardır.','150 ÷ 6 = 25'),A('Ayrıtı bul','Karenin alanı kenarın karesidir.','a² = 25 → a = 5 cm'),A('Köşegeni hesapla','Ön yüz bir kare olduğundan köşegeni kenarın √2 katıdır.','x = 5√2')],
 puf='Yüzey alanı verilen küpte önce ayrıtı bul; yüz köşegeni a√2 ile hesaplanır.',sekil=SK2)

# =================== 03 · ACF üçgeni · orta ===================
kartla('K-GKP-03','Yüz köşegenleriyle oluşan eşkenar üçgen','Küpün bir köşesinden çıkan üç yüz köşegeni eşit olduğundan ACF eşkenar üçgendir; kenarı a√2, alanı (a√2)²√3/4 tür.','Kenarı ayrıt sanmak; eşkenar üçgen alanında 4’e bölmeyi unutmak; ACF’yi dik üçgen sanmak.','orta',4,'ge-kp-ucgen','Küpte köşelerle oluşan eşkenar üçgen')
a3=6; ks=a3*sqrt(2); al=ks**2*sqrt(3)/4; assert abs(al-18*sqrt(3))<1e-9 and abs(a3**2*sqrt(3)/4-9*sqrt(3))<1e-9 and a3*a3/2==18 and a3**2==36 and abs(ks**2*sqrt(3)/2-36*sqrt(3))<1e-9
A_,C_,F_=(0,0,0),(a3,a3,0),(a3,0,a3)
assert abs(dist(A_,C_)-ks)<1e-9 and abs(dist(C_,F_)-ks)<1e-9 and abs(dist(A_,F_)-ks)<1e-9
K3=kutu(a3,a3,a3,sc=.4); Q=K3.Q; f=F()
f.fill([Q['A'],Q['C'],Q['F']],'fill=vurgu!25'); K3.draw(f); f.line(Q['A'],Q['C'],'dashed')
f.line(Q['A'],Q['F'],''); f.line(Q['C'],Q['F'],'')
lbl(f,K3,'A','B','$6$',(0,-.3))
for k,dv in dict(A=(-1,-1),B=(.4,-1),C=(1,-.2),D=(-.4,-1),E=(-1,.5),F=(.2,1),G=(1,.5),H=(-.2,1)).items(): f.vl(k,Q[k],dv,.3)
SK3=f.svg()
q('0003',tipId='ge-kp-ucgen',tip='Küpte köşelerle oluşan eşkenar üçgen',z='orta',alt='Köşegenlerle Oluşan Üçgen',kaz='Küpün yüz köşegenlerinden oluşan eşkenar üçgenin alanını hesaplar.',kalip='hikâyeli',
 kart='K-GKP-03 (ACF eşkenar üçgeni) · ayrıt 6',
 metin='Cam bir küp biçimindeki vitrinin A, C ve F köşeleri arasına ince birer tel gerilerek şekildeki ACF üçgeni oluşturuluyor. Vitrinin ayrıtı şekilde cm cinsinden verilmiştir; görünmeyen kenarlar kesikli çizgiyle gösterilmiştir.\nBuna göre, taralı ACF üçgeninin alanı kaç cm² dir?',
 dogru=Rd(18,3),sira=sirala(Rd(9,3),Rd(18,1),Rd(18,3),Rd(36,1),Rd(36,3)),
 yan=[(Rd(9,3),'ACF üçgeninin kenarını ayrıt (6) sanıp 6² × √3 ÷ 4 = 9√3 bulmuş.','bilgi'),(Rd(18,1),'Üçgeni dik üçgen sanıp 6 × 6 ÷ 2 = 18 bulmuş.','bilgi'),(Rd(36,1),'Bir yüzün alanını (6 × 6) vermiş.','dikkat'),(Rd(36,3),'Eşkenar üçgenin alanında 4 yerine 2’ye bölmüş: 72 × √3 ÷ 2 = 36√3.','islem')],
 istenen='ACF üçgeninin alanı (cm²).',
 ip=['ACF üçgeninin kenarları küpün hangi doğru parçalarıdır? Üç kenarın uzunluklarını karşılaştır.'],
 bilgi=[KOSEGEN,ESKENAR],
 ad=[A('Kenarları belirle','|AC|, |CF| ve |AF| birer yüz köşegenidir.','|AC| = |CF| = |AF| = 6√2'),A('Üçgenin türünü bul','Üç kenar eşit olduğundan ACF eşkenar üçgendir.','kenar a = 6√2'),A('Alanı hesapla','Eşkenar üçgenin alanı (a² × √3) ÷ 4 tür.','(72 × √3) ÷ 4 = 18√3')],
 puf='Küpün bir köşesinden çıkan üç yüz köşegeninin uçları eşkenar üçgen oluşturur; kenarı a√2 dir.',sekil=SK3)

# =================== 04 · Boyama ve bölme · orta ===================
kartla('K-GKP-04','Boyanıp küçük küplere bölünen küp','İki yüzü boyalı küçük küpler yalnız ayrıtların üzerinde, köşelerin dışındadır; her ayrıtta n − 2 tane vardır.','Köşe küplerini de saymak; yüz içi küpleri saymak; boyasız küplerle karıştırmak.','orta',3,'ge-kp-boya','Boyanıp küçük küplere bölünen küp')
n4=5
def boyali(n,boyali_yuzler):
    from collections import Counter
    c=Counter()
    for x in range(n):
        for y in range(n):
            for z in range(n):
                k=0
                if 'x0' in boyali_yuzler and x==0: k+=1
                if 'x1' in boyali_yuzler and x==n-1: k+=1
                if 'y0' in boyali_yuzler and y==0: k+=1
                if 'y1' in boyali_yuzler and y==n-1: k+=1
                if 'z0' in boyali_yuzler and z==0: k+=1
                if 'z1' in boyali_yuzler and z==n-1: k+=1
                c[k]+=1
    return c
c4=boyali(5,{'x0','x1','y0','y1','z0','z1'}); assert c4[2]==36==12*(n4-2) and c4[3]==8 and c4[1]==54 and c4[0]==27 and 125-c4[0]==98 and 12*5==60
K4=kutu(5,5,5,sc=.5); f=F()
for nm,st in (('on','fill=vurgu!10'),('sag','fill=vurgu!10'),('ust','fill=vurgu!10')): K4.fillface(f,nm,st)
izgara(f,K4,5,5); K4.draw(f); Q=K4.Q
lbl(f,K4,'A','B','$5$',(0,-.3))
SK4=f.svg()
q('0004',tipId='ge-kp-boya',tip='Boyanıp küçük küplere bölünen küp',z='orta',alt='Boyama ve Bölme',kaz='Boyanıp birim küplere bölünen küpte tam iki yüzü boyalı küp sayısını bulur.',kalip='hikâyeli',
 kart='K-GKP-04 (boyama, bölme) · ayrıt 5, iki yüzü boyalı',
 metin='Bir oyuncak yapımcısı, ayrıtı şekilde cm cinsinden verilen küp biçimli bir tahta bloğun dış yüzeyinin tamamını kırmızıya boyamıştır. Boya kuruyunca bloğu, şekildeki çizgiler boyunca yüzlere paralel düzlemlerle keserek ayrıtı 1 cm olan özdeş küçük küpler elde etmiştir.\nBuna göre, bu küçük küplerden kaç tanesinin tam iki yüzü kırmızıdır?',
 dogru=36,yan=[(54,'Tam bir yüzü boyalı olanları (6 × 3 × 3) saymış.','dikkat'),(60,'Her ayrıttaki köşe küplerini de sayıp 12 × 5 = 60 bulmuş.','dikkat'),(98,'Boyalı yüzü olan bütün küçük küpleri saymış: 125 − 27 = 98.','dikkat'),(125,'Küçük küplerin tümünü saymış.','dikkat')],
 istenen='Tam iki yüzü boyalı küçük küp sayısı.',
 ip=['Tam iki yüzü boyalı küpler küpün hangi bölgesinde bulunur? Köşelerdeki küpleri neden saymamalısın?'],
 bilgi=[BOYAK],
 ad=[A('Konumu belirle','İki yüzü boyalı küçük küpler ayrıtların üzerinde, köşelerin dışında yer alır.','12 ayrıt'),A('Bir ayrıttaki sayıyı bul','Her ayrıtta 5 küp vardır; iki ucundaki köşe küpleri çıkarılır.','5 − 2 = 3'),A('Toplamı yaz','Her ayrıtta 3 küp bulunan 12 ayrıt vardır.','12 × 3 = 36')],
 puf='Küçük küpleri konumuna göre (köşe, ayrıt, yüz içi, iç) sınıflandır ve istenen sınıfı say.',sekil=SK4)

# =================== 05 · Alt yüzü boyanmayan küp · zor ===================
kartla('K-GKP-05','Beş yüzü boyanan küpte boyasız küpler','Alt yüz boyanmadığından boyasız küpler yalnız yan ve üst yüzlerin içinde kalanlardır; alt katman boyasız sayılır.','Altı yüzün de boyalı olduğunu sanıp (n − 2)³ almak; alt katmanı unutmak; boyalı küp sayısını vermek.','zor',4,'ge-kp-boya','Boyanıp küçük küplere bölünen küp')
n5=6; c5=boyali(6,{'x0','x1','y0','y1','z1'}); assert c5[0]==80==4*4*5 and (n5-2)**3==64 and 4*4*6==96 and 5*5*4==100 and 216-80==136
K5=kutu(6,6,6,sc=.45); f=F()
for nm in ('on','sag','ust'): K5.fillface(f,nm,'fill=vurgu!10')
izgara(f,K5,6,6); K5.draw(f)
lbl(f,K5,'A','B','$6$',(0,-.3))
SK5=f.svg()
q('0005',tipId='ge-kp-boya',tip='Boyanıp küçük küplere bölünen küp',z='zor',alt='Alt Yüzü Boyanmayan Küp',kaz='Beş yüzü boyanıp bölünen küpte hiçbir yüzü boyalı olmayan küçük küp sayısını bulur.',kalip='hikâyeli',
 kart='K-GKP-05 (beş yüzü boyalı) · ayrıt 6, boyasız küpler',
 metin='Bir mermer ustası, ayrıtı şekilde cm cinsinden verilen küp biçimli bir mermer bloğu masaya koyup masaya değmeyen beş yüzüne koruyucu cila sürmüştür. Cila kuruyunca blok, çizgiler boyunca kesilip 1 cm ayrıtlı minik küpçüklere bölünmüştür; hiçbir küpçük kesim sırasında eksilmemiştir.\nBuna göre, minik küpçüklerin kaçının yüzlerinin hiçbirinde cila yoktur?',
 dogru=80,yan=[(64,'Altı yüzün de boyalı olduğunu sanıp (6 − 2)³ = 64 bulmuş.','bilgi'),(96,'Yükseklik boyunca hiç katman çıkarmamış: 4 × 4 × 6 = 96.','dikkat'),(100,'Yatay yönlerde 1 sıra, düşey yönde 2 sıra çıkarıp 5 × 5 × 4 = 100 bulmuş.','islem'),(136,'Boyalı küçük küp sayısını (216 − 80) vermiş.','dikkat')],
 istenen='Hiçbir yüzü boyalı olmayan küçük küp sayısı.',
 ip=['Hangi yüzler boyalı? Hiçbir yüzü boyalı olmayan küpler büyük küpün neresinde kalır?'],
 bilgi=[BOYAK],
 ad=[A('Boyasız küplerin konumu','Boyalı yüzler dört yan yüz ve üst yüzdür; boyasız küpler bunların içinde kalır, alt yüz boyasızdır.','yan ve üst yüzlerin içi'),A('Yatay yönler','Dört yan yüz yüzünden iki yönde de 2 sıra (her uçtan 1) dışarıda kalır.','6 − 2 = 4 → 4 × 4'),A('Düşey yön','Yalnız üst katman boyalı; alt katman boyasızdır ve sayılır.','6 − 1 = 5 kat'),A('Toplamı bul','Yatay tabaka sayısı ile kat sayısını çarp.','4 × 4 × 5 = 80')],
 puf='Boyanan yüzlere göre her yönde boyalı katmanları çıkar; boyanmayan yüze bakan katman boyasız sayılır.',sekil=SK5)

# =================== 06 · A'dan G'ye en kısa yol · orta ===================
kartla('K-GKP-06','Zıt köşeye yüzeyden en kısa yol','İki komşu yüz aynı düzleme serilince A ve G, ayrıtı ve iki katı dik kenar olan dikdörtgenin zıt köşeleri olur; en kısa yol a√5 tir.','Cisim köşegenini (a√3) yüzeyden yürünebilir sanmak; yan yana ayrıtları toplamak; yüz köşegeni artı ayrıt almak.','orta',3,'ge-kp-yol','Küp yüzeyinde en kısa yol')
a6=6; yol=sqrt(a6**2+(2*a6)**2); assert abs(yol-6*sqrt(5))<1e-9 and abs(6*sqrt(3)-10.392)<1e-3 and 12==2*a6 and 18==3*a6 and 6*sqrt(5)<6+6*sqrt(2)<18
assert 6*sqrt(3)<12<6*sqrt(5)<6+6*sqrt(2)
K6=kutu(6,6,6,sc=.4); Q=K6.Q; f=F(); K6.draw(f)
f.raw(f'\\fill {pt(Q["A"])} circle (1.5pt); \\fill {pt(Q["G"])} circle (1.5pt);')
lbl(f,K6,'A','B','$6$',(0,-.3))
for k,dv in dict(A=(-1,-1),B=(.4,-1),C=(1,-.2),D=(-.4,-1),E=(-1,.5),F=(.2,1),G=(1,.5),H=(-.2,1)).items(): f.vl(k,Q[k],dv,.3)
SK6=f.svg()
# açınım (ön yüz + üst yüz)
g=F(); s=.35
g.raw(f'\\draw ({0},{0}) rectangle ({6*s},{6*s}); \\draw ({0},{6*s}) rectangle ({6*s},{12*s});')
g.raw(f'\\draw[thick,vurgu] (0,0) -- ({6*s},{12*s});'); g.raw('\\fill (0,0) circle (1.4pt); '+f'\\fill ({6*s},{12*s}) circle (1.4pt);')
g.node((-.28,-.12),'$A$'); g.node((6*s+.3,12*s+.12),'$G$'); g.node((3*s,-.3),'$6$'); g.node((-.28,3*s),'$6$'); g.node((-.28,9*s),'$6$')
GR6=g.svg()
q('0006',tipId='ge-kp-yol',tip='Küp yüzeyinde en kısa yol',z='orta',alt='En Kısa Yol',kaz='Küp yüzeyinde zıt köşeler arasındaki en kısa yolu açınımdan bulur.',kalip='hikâyeli',
 kart='K-GKP-06 (en kısa yol) · A’dan G’ye, ayrıt 6',
 metin='Ayrıtı şekilde cm cinsinden verilen küp biçimli bir kutunun A köşesinde bir karınca vardır. Karınca, kutunun yüzeyi üzerinden yürüyerek karşı köşe olan G noktasına gidecektir; kutunun içinden geçemez ve yüzeyden ayrılamaz.\nBuna göre, karıncanın gidebileceği en kısa yolun uzunluğu kaç cm dir?',
 dogru=Rd(6,5),sira=sirala(Rd(6,3),Nn(12),Rd(6,5),Rp(6,6,2),Nn(18)),
 yan=[(Rd(6,3),'Cisim köşegenini (6√3) yol sanmış; karınca küpün içinden geçemez.','bilgi'),(Nn(12),'Yalnız iki ayrıt boyunca yürüyüp 6 + 6 = 12 bulmuş; iki ayrıt G’ye ulaştırmaz.','dikkat'),(Rp(6,6,2),'Bir yüz köşegeni ve bir ayrıt boyunca yürümeyi en kısa sanmış: 6√2 + 6.','islem'),(Nn(18),'Üç ayrıt boyunca yürümüş: 6 + 6 + 6 = 18.','dikkat')],
 istenen='En kısa yolun uzunluğu (cm).',
 ip=['Karıncanın geçeceği iki komşu yüzü aynı düzleme serersen yol nasıl bir çizgi olur?'],
 bilgi=[ACINIM,PIS],
 ad=[A('Yüzleri düzleme ser','Karıncanın geçtiği ön ve üst yüzleri alt alta aç; A ve G dikdörtgenin zıt köşeleri olur.','6 × 12 dikdörtgen',GR6),A('Dik üçgen kur','En kısa yol dikdörtgenin köşegenidir; dik kenarlar 6 ve 12’dir.','yol² = 6² + 12²'),A('Uzunluğu hesapla','Pisagor bağıntısıyla yolun karesini bul.','36 + 144 = 180 → yol = 6√5')],
 puf='Küpte zıt köşeler arasındaki yüzey yolu, ayrıtı ve iki katı dik kenar olan dikdörtgenin köşegenidir: a√5.',sekil=SK6)

# =================== 07 · A'dan M'ye en kısa yol · orta ===================
kartla('K-GKP-07','Üst ayrıt orta noktasına en kısa yol','Ön ve üst yüz açılınca M noktası ayrıtı yatay, 1,5 katı düşey kenar olan dikdörtgenin köşesine düşer; farklı açınımlar karşılaştırılır.','Yalnız tek açınımı denemek; M’yi köşe sanmak; yatay uzaklığı yarım almak.','orta',4,'ge-kp-yol','Küp yüzeyinde en kısa yol')
a7=8; cands={'on-ust':sqrt(a7**2+(1.5*a7)**2),'sol-ust':sqrt((a7/2)**2+(2*a7)**2),'taban-sag':sqrt((2*a7)**2+(a7/2)**2),'on-sag':sqrt((1.5*a7)**2+a7**2)}
mn=min(cands.values()); assert abs(mn-4*sqrt(13))<1e-9 and abs(cands['sol-ust']-4*sqrt(17))<1e-9 and abs(sqrt(16+144)-4*sqrt(10))<1e-9 and 8+12==20 and abs(a7*sqrt(5)-8*sqrt(5))<1e-9
M7=(a7,a7/2,a7)
K7=kutu(a7,a7,a7,sc=.4); Q=K7.Q; f=F(); K7.draw(f)
M7q=mul(proj(M7),K7.sc)
f.raw(f'\\fill {pt(Q["A"])} circle (1.5pt); \\fill {pt(M7q)} circle (1.5pt);')
lbl(f,K7,'A','B','$8$',(0,-.3))
for k,dv in dict(A=(-1,-1),B=(.4,-1),C=(1,-.2),D=(-.4,-1),E=(-1,.5),F=(.2,1),G=(1,.5),H=(-.2,1)).items(): f.vl(k,Q[k],dv,.3)
f.node(add(M7q,(.1,.33)),'$M$')
SK7=f.svg()
g=F(); s=.28
g.raw(f'\\draw (0,0) rectangle ({8*s},{8*s}); \\draw (0,{8*s}) rectangle ({8*s},{16*s});')
g.raw(f'\\draw[thick,vurgu] (0,0) -- ({8*s},{12*s});'); g.raw(f'\\fill (0,0) circle (1.4pt); \\fill ({8*s},{12*s}) circle (1.4pt);')
g.node((-.28,-.12),'$A$'); g.node((8*s+.3,12*s),'$M$'); g.node((4*s,-.3),'$8$'); g.node((8*s+.3,4*s),'$8$'); g.node((8*s+.3,14*s),'$4$'); g.node((8*s+.3,9.7*s),'$4$') if False else None
GR7=g.svg()
q('0007',tipId='ge-kp-yol',tip='Küp yüzeyinde en kısa yol',z='orta',alt='En Kısa Yol',kaz='Küp yüzeyinde bir köşeden bir ayrıt orta noktasına en kısa yolu açınımlardan bulur.',kalip='hikâyeli',
 kart='K-GKP-07 (en kısa yol, orta nokta) · A’dan [FG] orta noktası M’ye, ayrıt 8',
 metin='Ayrıtı şekilde cm cinsinden verilen ABCDEFGH küpünün A köşesinde duran bir karınca, [FG] ayrıtının orta noktası olan M noktasına, küpün yüzeyi üzerinden yürüyerek gidecektir. Karınca küpün içinden geçemez ve yüzeyden ayrılamaz.\nBuna göre, karıncanın gidebileceği en kısa yolun uzunluğu kaç cm dir?',
 dogru=Rd(4,13),sira=sirala(Rd(4,10),Rd(4,13),Rd(4,17),Rd(8,5),Nn(20)),
 yan=[(Rd(4,10),'Yatay uzaklığı 8 yerine 4 alıp √(4² + 12²) = 4√10 bulmuş.','islem'),(Rd(4,17),'Sol ve üst yüzü açıp √(4² + 16²) = 4√17 bulmuş; bu yol daha uzundur.','dikkat'),(Rd(8,5),'M’yi G köşesi sanıp zıt köşeye giden yolu (8√5) bulmuş.','dikkat'),(Nn(20),'Ayrıtlar boyunca yürüyüp 8 + 8 + 4 = 20 bulmuş.','dikkat')],
 istenen='En kısa yolun uzunluğu (cm).',
 ip=['Karıncanın geçebileceği yüz çiftlerinden birini aynı düzleme ser ve M’nin yeni yerini bul; başka bir açınım daha kısa yol verir mi?'],
 bilgi=[ACINIM,PIS],
 ad=[A('Ön ve üst yüzü aç','A ön yüzün köşesi, M üst yüzün [FG] kenarının orta noktasıdır; iki yüz alt alta serilir.','yatay: 8 · düşey: 8 + 4 = 12',GR7),A('Yolu hesapla','Pisagor bağıntısı uygula.','yol² = 8² + 12² = 208 → 4√13'),A('Diğer açınımı dene','Sol ve üst yüzü açınca yatay 4, düşey 16 olur; bu yol daha uzundur.','√(4² + 16²) = 4√17 > 4√13'),A('En kısasını seç','Ön–sağ açınımı da 4√13 verir; en kısa yol bulunmuştur.','4√13')],
 puf='Yüzeyde en kısa yol sorularında birden fazla açınım dene; en küçük uzunluk cevaptır.',sekil=SK7)

# =================== 08 · Köşesi kesilen küpün yüzey alanı · zor ===================
kartla('K-GKP-08','Orta noktalardan köşe kesme','Kesilen köşede üç yüzden dik üçgenler gider, yerine eşkenar üçgen yüz gelir; yüzey alanı bu üç değişimle hesaplanır.','Yeni üçgen yüzü saymamak; kaybolan üçgenleri çıkarmamak; kayıp üçgenin alanını yanlış hesaplamak.','zor',4,'ge-kp-kose','Küpte köşe kesme ve yüzey alanı')
a8=8; kay=(a8/2)**2/2; eny=(a8/2*sqrt(2))**2*sqrt(3)/4; T8=6*a8**2-3*kay+eny
assert kay==8 and abs(eny-8*sqrt(3))<1e-9 and abs(T8-(360+8*sqrt(3)))<1e-9 and 6*a8**2==384 and 6*a8**2-3*kay==360 and abs(6*a8**2-3*16+8*sqrt(3)-(336+8*sqrt(3)))<1e-9 and 3*4*4==48
V8={'A':(0,0,0),'M':(4,0,0),'N':(8,4,0),'C':(8,8,0),'D':(0,8,0),'E':(0,0,8),'F':(8,0,8),'G':(8,8,8),'H':(0,8,8),'K':(8,0,4)}
s3=1/sqrt(3)
FC8={'taban':(['A','M','N','C','D'],(0,0,-1)),'on':(['A','M','K','F','E'],(0,-1,0)),'sag':(['N','C','G','F','K'],(1,0,0)),'ust':(list('EFGH'),(0,0,1)),'arka':(list('DHGC'),(0,1,0)),'sol':(list('ADHE'),(-1,0,0)),'yeni':(['M','N','K'],(s3,-s3,-s3))}
S8=Solid(V8,FC8,sc=.4); Q=S8.Q; f=F(); S8.fillface(f,'yeni','fill=vurgu!25'); S8.draw(f)
Bq=mul(proj((8,0,0)),.4)
for p in 'MNK': f.line(Bq,Q[p],'dotted')
print('Q8 gizli',S8.hid_list())
f.node(add(mid(Q['A'],Q['E']),(-.3,0)),'$8$')
for k,dv in dict(A=(-1,-1),D=(-.4,-1),C=(1,-.2),E=(-1,.5),F=(.2,1),G=(1,.5),H=(-.2,1)).items(): f.vl(k,Q[k] if k in Q else Bq,dv,.3)
f.vl('B',Bq,(.4,-1),.3); f.vl('M',Q['M'],(-.2,-1),.3); f.vl('N',Q['N'],(1,-.5),.3); f.vl('K',Q['K'],(1,.1),.3)
SK8=f.svg()
q('0008',tipId='ge-kp-kose',tip='Küpte köşe kesme ve yüzey alanı',z='zor',alt='Köşe Kesme',kaz='Küpün bir köşesi ayrıt orta noktalarından geçen düzlemle kesilince kalan cismin yüzey alanını hesaplar.',kalip='hikâyeli',
 kart='K-GKP-08 (köşe kesme, yüzey alanı) · ayrıt 8, orta noktalar',
 metin='Küp biçimindeki bir sabun kalıbının ayrıtı şekilde cm cinsinden verilmiştir. Kalıbın B köşesi, [AB], [BC] ve [BF] ayrıtlarının orta noktaları olan M, N ve K noktalarından geçen düzlemle kesilip atılıyor. Kesilen parçanın kenarları noktalı çizgiyle gösterilmiştir. Kalan cismin bütün yüzeyi (kesit yüzü dahil) parlatılacaktır.\nBuna göre, parlatılacak yüzeyin alanı kaç cm² dir?',
 dogru=Rp(360,8,3),sira=sirala(Rp(336,8,3),Nn(360),Rp(360,4,3),Rp(360,8,3),Nn(384)),
 yan=[(Rp(336,8,3),'Kaybolan dik üçgenlerin alanını 4 × 4 = 16 alıp 384 − 48 + 8√3 = 336 + 8√3 bulmuş (1/2 çarpanını unutmuş).','islem'),(Nn(360),'Yeni oluşan MNK yüzünü eklemeyi unutmuş: 384 − 24 = 360.','dikkat'),(Nn(384),'Küpün alanını (6 × 64) vermiş; kesilen köşenin etkisini hesaba katmamış.','dikkat'),(Rp(360,4,3),'MNK üçgeninin kenarını 4 sanıp alanını (16 × √3) ÷ 4 = 4√3 bulmuş: 360 + 4√3.','bilgi')],
 istenen='Kalan cismin yüzey alanı (cm²).',
 ip=['Kesme işlemi küpün yüzlerinden hangi parçaları götürüyor ve yerine hangi yeni yüzü getiriyor? Yeni yüzün kenarı nedir?'],
 bilgi=[KALAN,ESKENAR],
 ad=[A('Küpün alanını yaz','Kesmeden önce altı eş kare yüz vardır.','6 × 8² = 384'),A('Giden üçgenleri çıkar','B köşesindeki üç yüzden, dik kenarları 4 cm olan birer dik üçgen gider.','3 × (4 × 4 ÷ 2) = 24 → 384 − 24 = 360'),A('Yeni yüzün kenarını bul','MNK üçgeninin kenarları, dik kenarı 4 olan üçgenlerin hipotenüsleridir.','4√2'),A('Yeni yüzün alanını ekle','Kenarı 4√2 olan eşkenar üçgenin alanı (a² × √3) ÷ 4 tür.','(32 × √3) ÷ 4 = 8√3 → 360 + 8√3')],
 puf='Köşe kesilince yüzey alanı = küpün alanı − üç dik üçgen + yeni eşkenar üçgen; üç etkiyi ayrı ayrı yaz.',sekil=SK8)

# =================== yaz ===================
def bitir_geo(onek):
    for qq in P.ANA: qq['kardes']=None
    P.yaz(os.path.join(GD,f'{onek}-1.json'),f'/tmp/bos-{onek}.json')
    tipler={}
    for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=TIPK[c['tipId']]))['kartlar'].append(c['id'])
    json.dump(dict(konu=P.konu_adi,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 TYT Geometri çıkmış soruları (yalnız mantık), MEB 9–10. sınıf geometri müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar',f'{onek}.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler))
bitir_geo('kup')
