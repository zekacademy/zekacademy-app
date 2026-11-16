"""TYT Geometri · Prizmalar (kardeş yok, ipucu 1). Şekil koordinatları hesaplanır; TikZ gövdesi aynı değerlerden üretilir (cizim.tikz_svg).
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
P=Parti('prizma','Prizmalar','geo|Prizmalar',ders='TYT Geometri',idon='tytgeo')
def lbl(f,S,p,q_,t,off): f.node(add(mid(S.Q[p],S.Q[q_]),off),t)
def okdim(f,S,p,q_,t,dx,dl=.3):
    a=S.Q[p]; b=S.Q[q_]; f.raw(f'\\draw[<->,thin] {pt((a[0]+dx,a[1]))} -- {pt((b[0]+dx,b[1]))};'); f.node(((a[0]+b[0])/2+dx-dl,(a[1]+b[1])/2),t)
def shift(S,dx,dy): S.Q={k:(p[0]+dx,p[1]+dy) for k,p in S.Q.items()}
def sudolu(f,S,st='fill=vurgu!18'):
    for nm in ('on','sag','ust'): S.fillface(f,nm,st)
YUZEY=B('Prizmanın yüzey alanı','tüm yüzey alanı = 2 × taban alanı + taban çevresi × yükseklik. Dikdörtgenler prizmasında 2 × (ab + bc + ca) dır. Örnek: ayrıtları 2, 3 ve 7 olan prizmada 2 × (6 + 21 + 14) = 82')
HACIM=B('Prizmanın hacmi','V = taban alanı × yükseklik; dikdörtgenler prizmasında V = a × b × c. Örnek: ayrıtları 2, 5 ve 6 olan prizmanın hacmi 60’tır')
PIS=B('Pisagor bağıntısı','dik üçgende dik kenarların kareleri toplamı hipotenüsün karesine eşittir. Örnek: dik kenarları 5 ve 12 olan üçgende hipotenüs 13’tür')
UCGEN=B('Dik üçgenin alanı','dik kenar uzunlukları a ve b olan üçgenin alanı a × b ÷ 2 dir. Örnek: dik kenarları 6 ve 7 olan üçgenin alanı 21’dir')
LITRE=B('Hacim ve litre','1 litre = 1000 cm³ tür. Örnek: 5000 cm³ hacmindeki su 5 litredir')
KESIM=B('Köşeden prizma kesilince alan','bir köşeden dikdörtgenler prizması biçiminde parça çıkarılırsa, üç yüzden aynı alan kadar kesilir ve çukurun üç iç yüzü kadar yüz eklenir; bu iki alan eşit olduğundan yüzey alanı değişmez. Hacim ise çıkarılan parçanın hacmi kadar azalır. Örnek: ayrıtı 4 olan küpün bir köşesinden 1 × 1 × 1 lik küp çıkarılırsa yüzey alanı yine 96, hacim 64 − 1 = 63 olur')
YERLES=B('Prizmaya prizma yerleştirme','her ayrıt boyunca sığan kutu sayısı, koli ayrıtının kutu ayrıtına bölümünün tam kısmıdır; toplam sayı üç sayının çarpımıdır. Örnek: 20 × 10 × 6 lık koliye 4 × 3 × 2 lik kutular aynı yönde 5 × 3 × 3 = 45 tane sığar')
SUBOS=B('Su yüksekliği','tabanı S olan prizma biçimli kapta V hacmindeki suyun yüksekliği h = V ÷ S dir. Örnek: tabanı 50 cm², hacmi 400 cm³ olan suyun yüksekliği 8 cm’dir')

# =================== 01 · Dikdörtgenler prizması yüzey alanı · kolay ===================
konu('geo|Prizmalar','Prizmalar')
kartla('K-GPR-01','Dikdörtgenler prizmasının yüzey alanı','Altı yüz üç çift eş dikdörtgendir; yüzey alanı 2(ab + bc + ca) ile bulunur.','Yüz çiftlerinden yalnız birer yüzü saymak; tabanları unutmak; hacimle karıştırmak.','kolay',3,'ge-pr-dik','Dikdörtgenler prizmasının yüzey alanı')
a1,b1,c1=10,6,4; S1=2*(a1*b1+b1*c1+c1*a1); assert S1==248 and a1*b1+b1*c1+c1*a1==124 and 2*(a1+b1)*c1==128 and S1-a1*b1==188 and a1*b1*c1==240
K1=kutu(a1,b1,c1,sc=.3); f=F(); K1.draw(f); Q=K1.Q
assert K1.hid_list()==['AD','CD','DH']
lbl(f,K1,'A','B','$10$',(0,-.3)); lbl(f,K1,'B','C','$6$',(.28,-.12)); lbl(f,K1,'A','E','$4$',(-.28,0))
SK1=f.svg()
q('0001',tipId='ge-pr-dik',tip='Dikdörtgenler prizmasının yüzey alanı',z='kolay',alt='Yüzey Alanı',kaz='Dikdörtgenler prizmasının tüm yüzey alanını ayrıtlarından hesaplar.',kalip='hikâyeli',
 kart='K-GPR-01 (yüzey alanı) · 10 × 6 × 4 hediye kutusu',
 metin='Bir mağazada, ölçüleri şekilde verilen dikdörtgenler prizması biçimindeki hediye kutularının tüm dış yüzü renkli kâğıtla kaplanacaktır. Kâğıt, kutunun altı yüzünü de örtecek, kâğıdın kalınlığı ve birleşim payı hesaba katılmayacaktır.\nBuna göre, bir kutuyu kaplamak için en az kaç cm² kâğıt gerekir?',
 dogru=248,yan=[(124,'Üç yüz çiftinden yalnız birer yüzün alanını toplamış: 60 + 24 + 40 = 124.','dikkat'),(128,'Yalnız yan yüzleri (2 × (10 + 6) × 4) hesaplamış; alt ve üst yüzü unutmuş.','dikkat'),(188,'Yüzlerden yalnız birini (10 × 6 = 60) çıkarmış; kutunun altı yüzü de kaplanacaktır.','dikkat'),(240,'Yüzey alanı yerine hacmi (10 × 6 × 4) bulmuş.','bilgi')],
 istenen='Kutunun tüm yüzey alanı (cm²).',
 ip=['Kutunun yüzlerini eş çiftler hâlinde düşün; her çiftin yüz ölçüleri hangi iki ayrıttan oluşuyor?'],
 bilgi=[YUZEY],
 ad=[A('Yüz çiftlerini ayır','Karşılıklı yüzler eştir: alt-üst, ön-arka, sol-sağ.','alt-üst: 10 × 6 · ön-arka: 10 × 4 · yan: 6 × 4'),A('Bir çiftin alanlarını yaz','Üç farklı yüzün alanları hesaplanır.','60 + 40 + 24 = 124'),A('Çiftlerle çarp','Her yüzden iki tane olduğundan toplam ikiyle çarpılır.','2 × 124 = 248')],
 puf='Dikdörtgenler prizmasının yüzey alanı, üç farklı yüzün alanları toplamının iki katıdır.',sekil=SK1)

# =================== 02 · Dik üçgen prizma · orta ===================
kartla('K-GPR-02','Üçgen prizmanın yüzey alanı','Taban dik üçgenin alanı ve çevresi bulunur; yanal alan çevre × yükseklik, tüm alan iki taban ile yanal alanın toplamıdır.','Üçgenin alanında 1/2 çarpanını unutmak; hipotenüsü yan yüzlerde saymamak; yalnız yanal alanı vermek.','orta',4,'ge-pr-ucgen','Üçgen prizmanın yüzey alanı')
L2=5; ta=8*15/2; cev=8+15+17; assert ta==60 and cev==40 and 2*ta+cev*L2==320 and cev*L2==200 and 2*ta+(8+15)*L2==235 and ta+cev*L2==260 and 2*(8*15)+cev*L2==440 and 8**2+15**2==17**2
V2={'A':(0,0,0),'B':(15,0,0),'C':(0,0,8),'D':(0,L2,0),'E':(15,L2,0),'F':(0,L2,8)}
nn=un((8,0,15))
FC2={'on':(list('ABC'),(0,-1,0)),'arka':(list('DEF'),(0,1,0)),'taban':(list('ABED'),(0,0,-1)),'sol':(list('ACFD'),(-1,0,0)),'egik':(list('BCFE'),nn)}
S2=Solid(V2,FC2,sc=.22); f=F(); S2.draw(f); Q=S2.Q
assert S2.hid_list()==['AD','DE','DF'],S2.hid_list()
f.dik(Q['A'],Q['B'],Q['C'],.2)
lbl(f,S2,'A','B','$15$',(0,-.28)); lbl(f,S2,'A','C','$8$',(-.25,0)); lbl(f,S2,'F','E','$17$',(.2,.3)); lbl(f,S2,'B','E','$5$',(.28,-.12))
SK2=f.svg()
q('0002',tipId='ge-pr-ucgen',tip='Üçgen prizmanın yüzey alanı',z='orta',alt='Üçgen Prizma',kaz='Tabanı dik üçgen olan prizmanın tüm yüzey alanını hesaplar.',kalip='hikâyeli',
 kart='K-GPR-02 (üçgen prizma alan) · 8-15-17 tabanlı, yükseklik 5',
 metin='Bir yapı marketi, şekilde ölçüleri verilen dik üçgen prizma biçimindeki beton blokların her yüzünü yağmura dayanıklı boyayla kaplayacaktır. Blokların tabanı dik üçgendir; yan yüzler dikdörtgen biçimindedir ve boyanacak yüzeyin kalınlığı ihmal edilecektir.\nBuna göre, bir bloğun boyanacak toplam yüzeyi kaç cm² dir?',
 dogru=320,yan=[(200,'Yalnız yanal alanı (40 × 5) bulup iki tabanı eklememiş.','dikkat'),(235,'Hipotenüs yüzünü (17 × 5) saymadan 2 × 60 + (8 + 15) × 5 = 235 bulmuş.','dikkat'),(260,'Tabanlardan yalnız birini eklemiş: 60 + 200 = 260.','dikkat'),(440,'Üçgenin alanını 1/2 ile çarpmadan 8 × 15 = 120 almış: 2 × 120 + 200 = 440.','bilgi')],
 istenen='Bloğun tüm yüzey alanı (cm²).',
 ip=['Prizmanın yüzlerini iki üçgen taban ve üç dikdörtgen yan yüz olarak ayır; yan yüzlerin bir kenarı hangi uzunluk?'],
 bilgi=[YUZEY,UCGEN],
 ad=[A('Taban alanını bul','Taban dik kenarları 8 ve 15 olan dik üçgendir.','8 × 15 ÷ 2 = 60'),A('Taban çevresini bul','Üçgenin üç kenarı toplanır; hipotenüs 17 olarak verilmiştir.','8 + 15 + 17 = 40'),A('Yanal alanı bul','Üç yan yüz, tabanın kenarları ile yüksekliğin oluşturduğu dikdörtgenlerdir.','40 × 5 = 200'),A('Tüm yüzeyi topla','İki taban ve yanal alan toplanır.','2 × 60 + 200 = 320')],
 puf='Prizmanın tüm yüzey alanı = 2 × taban alanı + taban çevresi × yükseklik; dik üçgende alan için 1/2’yi unutma.',sekil=SK2)

# =================== 03 · Köşeden prizma kesme · orta ===================
kartla('K-GPR-03','Köşeden parça çıkarılan prizma','Köşeden dikdörtgenler prizması biçiminde parça çıkarılınca alan kaybı ile çukurun iç yüzleri eşittir; yüzey alanı değişmez.','Çıkarılan parçanın yüzlerini toplam alandan çıkarmak ya da eklemek; hacmi alan sanmak.','zor',3,'ge-pr-kesme','Prizmadan parça kesme ve yüzey alanı')
a3,b3,c3,p3,q3,r3=10,8,6,4,3,2
S3v=2*(a3*b3+b3*c3+c3*a3); vol=a3*b3*c3-p3*q3*r3; nt=p3*q3+p3*r3+q3*r3
assert S3v==376 and nt==26 and S3v-nt==350 and S3v-p3*q3==364 and S3v+nt==402 and vol==456
Vb={'A':(0,0,0),'B':(a3,0,0),'C':(a3,b3,0),'D':(0,b3,0),'E':(0,0,c3),'H':(0,b3,c3),'G':(a3,b3,c3),
    'P1':(a3-p3,0,c3),'P2':(a3-p3,q3,c3),'P3':(a3,q3,c3),'Q1':(a3-p3,0,c3-r3),'Q2':(a3-p3,q3,c3-r3),'Q3':(a3,q3,c3-r3),'Q4':(a3,0,c3-r3)}
FC3={'taban':(list('ADCB'),(0,0,-1)),'arka':(list('DHGC'),(0,1,0)),'sol':(list('ADHE'),(-1,0,0)),
     'on':(['A','B','Q4','Q1','P1','E'],(0,-1,0)),'sag':(['B','C','G','P3','Q3','Q4'],(1,0,0)),'ust':(['E','P1','P2','P3','G','H'],(0,0,1)),
     'zemin':(['Q1','Q4','Q3','Q2'],(0,0,1)),'duvx':(['P1','P2','Q2','Q1'],(1,0,0)),'duvy':(['P2','P3','Q3','Q2'],(0,-1,0))}
S3=Solid(Vb,FC3,sc=.28); f=F(); S3.fillface(f,'zemin','fill=vurgu!18'); S3.draw(f); Q=S3.Q
assert S3.hid_list()==['AD','CD','DH'],S3.hid_list()
lbl(f,S3,'A','B','$10$',(0,-.28)); lbl(f,S3,'B','C','$8$',(.28,-.12)); lbl(f,S3,'A','E','$6$',(-.25,0))
lbl(f,S3,'P2','P3','$4$',(0,.2)); lbl(f,S3,'P1','P2','$3$',(-.22,.08)); lbl(f,S3,'P3','Q3','$2$',(.22,0))
SK3=f.svg()
q('0003',tipId='ge-pr-kesme',tip='Prizmadan parça kesme ve yüzey alanı',z='zor',alt='Prizmadan Prizma Kesme',kaz='Köşesinden prizma kesilen cismin yüzey alanının değişmediğini görerek alanı hesaplar.',kalip='hikâyeli',
 kart='K-GPR-03 (köşe kesme, yüzey alanı) · 10 × 8 × 6 bloktan 4 × 3 × 2 parça',
 metin='Bir marangoz, ölçüleri şekilde verilen dikdörtgenler prizması biçimindeki ahşap bir bloğun bir köşesinden, yine dikdörtgenler prizması biçiminde bir parçayı kesip çıkarıyor. Çıkarılan parçanın ölçüleri şekilde gösterilmiştir. Daha sonra bloğun bütün dış yüzeyi (çukurun içi dahil) vernikleniyor.\nBuna göre, vernik sürülen yüzeyin alanı kaç cm² dir?',
 dogru=376,yan=[(350,'Çıkarılan parçanın üç yüzünün alanını (12 + 8 + 6 = 26) toplam alandan çıkarıp çukurun iç yüzlerini eklemeyi unutmuş.','dikkat'),(364,'Yalnız üst yüzden çıkarılan 4 × 3 = 12 cm² yi çıkarmış.','dikkat'),(402,'Çukurun üç iç yüzünü ekleyip dış yüzlerden eksilen alanı çıkarmayı unutmuş: 376 + 26 = 402.','dikkat'),(456,'Yüzey alanı yerine kalan cismin hacmini (480 − 24) bulmuş.','bilgi')],
 istenen='Vernik sürülen toplam yüzeyin alanı (cm²).',
 ip=['Kesilince hangi yüzler kısalıyor, hangi yeni yüzler ortaya çıkıyor?'],
 bilgi=[YUZEY],
 ad=[A('Bütün bloğun alanı','Kesmeden önceki dikdörtgenler prizmasının yüzey alanını bul.','2 × (10 × 8 + 8 × 6 + 6 × 10) = 376'),A('Kesilen yüzleri incele','Köşeden alınan parça, bloğun üç yüzünden 4 × 3, 4 × 2 ve 3 × 2 lik dikdörtgenleri götürür.','12 + 8 + 6 = 26 cm² azalır'),A('Çukurun iç yüzleri','Çukurun üç iç yüzü, yok olan dikdörtgenlerle aynı ölçüdedir.','26 cm² artar'),A('Sonucu yaz','Azalan ve artan alan eşit olduğundan yüzey alanı değişmez.','376 − 26 + 26 = 376')],
 puf='Parça çıkarılan cisimlerde yüzeyden giden ve ortaya çıkan yüzleri ayrı ayrı hesaplayıp karşılaştır.',sekil=SK3)

# =================== 04 · Su dolumu · ön görünüş · kolay ===================
kartla('K-GPR-04','Dikdörtgen prizma kapta su dolumu','Su hacmi taban alanı × su yüksekliğidir; cm³ litreye çevrilip musluğun debisine bölünür.','Kabın tüm yüksekliğini kullanmak; litre–cm³ dönüşümünü yanlış yapmak; hacmi debiye bölmemek.','kolay',3,'ge-pr-su','Prizma biçimli kapta su doldurma, aktarma ve boşaltma')
h4,H4,a4,b4,deb=25,30,60,40,12; V4=a4*b4*h4; assert V4==60000 and V4/1000==60 and V4/1000/deb==5 and a4*b4*H4/1000/deb==6 and 60000/100/deb==50 and 60==V4/1000 and V4/deb==5000
s=.05; f=F()
f.fill([(0,0),(a4*s,0),(a4*s,h4*s),(0,h4*s)],'fill=vurgu!20'); f.raw(f'\\draw (0,0) rectangle ({a4*s},{H4*s});')
f.raw(f'\\draw[dashed] (0,{h4*s}) -- ({a4*s},{h4*s});')
f.node((a4*s/2,-.3),'$60$'); f.node((a4*s+.3,H4*s/2),'$30$'); f.node((-.3,h4*s/2),'$25$')
f.raw(f'\\draw[<->,thin] (-.62,0) -- (-.62,{h4*s});') if False else None
f.node((a4*s/2,H4*s+.3),'ön görünüş')
SK4=f.svg()
q('0004',tipId='ge-pr-su',tip='Prizma biçimli kapta su doldurma, aktarma ve boşaltma',z='kolay',alt='Su Doldurma',kaz='Dikdörtgenler prizması biçimli kapta belirli yüksekliğe kadar dolma süresini hesaplar.',kalip='hikâyeli',
 kart='K-GPR-04 (su dolumu) · 60 × 40 × 30 akvaryum, 25 cm su',
 metin='İç tabanı 60 cm × 40 cm olan dikdörtgenler prizması biçimli bir akvaryumun, ön yüzünden görünüşü şekilde verilmiştir. Boş akvaryum, dakikada 12 litre su akıtan bir musluk ile doldurulacak ve su seviyesi şekilde gösterilen yüksekliğe ulaşınca musluk kapatılacaktır. 1 litre = 1000 cm³ tür.\nBuna göre, musluk kaç dakika açık kalmalıdır?',
 dogru=5,yan=[(6,'Su seviyesi yerine akvaryumun tüm yüksekliğini (30 cm) alıp 72 ÷ 12 = 6 bulmuş.','dikkat'),(50,'1 litreyi 100 cm³ sanıp 60000 ÷ 100 = 600 litre bulmuş; 600 ÷ 12 = 50.','bilgi'),(60,'Hacmi 60 litre bulup musluğun debisine bölmeyi unutmuş.','dikkat'),(5000,'Hacmi cm³ cinsinden 60000 bulup litreye çevirmeden 12’ye bölmüş.','islem')],
 istenen='Musluğun açık kalacağı süre (dakika).',
 ip=['Önce suyun kaplayacağı prizmanın hacmini bul; musluk litre ile verildiğinden birimi dönüştürmen gerekiyor.'],
 bilgi=[HACIM,LITRE],
 ad=[A('Suyun hacmini bul','Su, tabanı 60 × 40 ve yüksekliği 25 cm olan prizma biçimindedir.','60 × 40 × 25 = 60 000 cm³'),A('Litreye çevir','1 litre 1000 cm³ olduğundan hacim 1000’e bölünür.','60 000 ÷ 1000 = 60 litre'),A('Süreyi hesapla','Toplam su miktarı, dakikada akan miktara bölünür.','60 ÷ 12 = 5 dakika')],
 puf='Doldurma süresi = suyun hacmi (litre) ÷ musluğun debisi (litre/dakika); önce cm³ → litre dönüşümünü yap.',sekil=SK4)

# =================== 05 · Su aktarma · zor ===================
kartla('K-GPR-05','İki kap arasında su aktarma','A kabındaki suyun hacmi B kabındaki suya eklenir; toplam hacim B’nin taban alanına bölünerek yeni su yüksekliği bulunur.','Yükseklikleri toplamak; A’nın taban alanına bölmek; B’deki ilk suyu unutmak.','orta',4,'ge-pr-su','Prizma biçimli kapta su doldurma, aktarma ve boşaltma')
VA=20*18*25; VB0=30*20*6; Vt=VA+VB0; hh=Vt/(30*20); assert VA==9000 and VB0==3600 and hh==21 and hh<=40 and VA/(30*20)==15 and 6+25==31 and Vt/(20*18)==35 and Vt/(30*30)==14
scl=.07; GAP=48
KA_=kutu(20,18,25,sc=scl); KB_=kutu(30,20,40,sc=scl,o=(GAP,0,0)); WA=kutu(20,18,25,sc=scl); WB=kutu(30,20,6,sc=scl,o=(GAP,0,0))
f=F(); sudolu(f,WA); sudolu(f,WB)
for S in (KA_,KB_): S.draw(f)
WB.draw(f,'','dashed') if False else None
for nm in ('A','B','C'): pass
assert KA_.hid_list()==['AD','CD','DH'] and KB_.hid_list()==['AD','CD','DH']
lbl(f,KA_,'A','B','$20$',(0,-.28)); lbl(f,KA_,'B','C','$18$',(.3,-.1)); okdim(f,KA_,'A','E','$25$',-.12)
lbl(f,KB_,'A','B','$30$',(0,-.28)); lbl(f,KB_,'B','C','$20$',(.3,-.1)); okdim(f,KB_,'A','E','$40$',-.7)
f.raw(f'\\draw[<->,thin] {pt((WB.Q["A"][0]-.12,WB.Q["A"][1]))} -- {pt((WB.Q["E"][0]-.12,WB.Q["E"][1]))};'); f.node((WB.Q['A'][0]-.4,mid(WB.Q['A'],WB.Q['E'])[1]),'$6$')
f.node((mid(KA_.Q['E'],KA_.Q['G'])[0],KA_.Q['G'][1]+.3),'A kabı'); f.node((mid(KB_.Q['E'],KB_.Q['G'])[0],KB_.Q['G'][1]+.3),'B kabı')
SK5=f.svg()
q('0005',tipId='ge-pr-su',tip='Prizma biçimli kapta su doldurma, aktarma ve boşaltma',z='orta',alt='Su Aktarma',kaz='İki dikdörtgen prizma kap arasında su aktarılınca yeni su yüksekliğini hacim üzerinden hesaplar.',kalip='hikâyeli',
 kart='K-GPR-05 (su aktarma) · A dolu, B kabında 6 cm su',
 metin='İç ölçüleri şekilde verilen A ve B kapları dikdörtgenler prizması biçimindedir. A kabı ağzına kadar suyla doludur; B kabında ise şekilde gösterilen yüksekliğe kadar su vardır. Bir öğrenci A kabındaki suyun tamamını, hiç dökmeden B kabına boşaltıyor.\nBuna göre, B kabındaki suyun yüksekliği kaç cm olur?',
 dogru=21,yan=[(14,'B kabının tabanını 30 × 30 sanıp 12600 ÷ 900 = 14 bulmuş.','islem'),(15,'Yalnız A kabındaki suyu hesaba katmış: 9000 ÷ 600 = 15; B’deki ilk suyu unutmuş.','dikkat'),(31,'Su yüksekliklerini doğrudan toplamış: 6 + 25 = 31.','bilgi'),(35,'Toplam hacmi A kabının taban alanına (20 × 18) bölmüş: 12600 ÷ 360 = 35.','dikkat')],
 istenen='B kabındaki suyun son yüksekliği (cm).',
 ip=['Su, bir kaptan diğerine geçerken hangi nicelik korunur? Sonra bu niceliği hangi kabın tabanına bölmelisin?'],
 bilgi=[HACIM,SUBOS],
 ad=[A('A kabındaki suyu bul','A kabı ağzına kadar dolu olduğundan su hacmi kabın hacmine eşittir.','20 × 18 × 25 = 9000 cm³'),A('B kabındaki ilk su','B’de tabanı 30 × 20 olan, yüksekliği 6 cm olan su vardır.','30 × 20 × 6 = 3600 cm³'),A('Toplam hacmi yaz','Su aktarılınca hacimler toplanır.','9000 + 3600 = 12600 cm³'),A('Yüksekliği hesapla','Toplam hacim B’nin taban alanına bölünür; B’nin yüksekliği 40 cm olduğundan taşma olmaz.','12600 ÷ (30 × 20) = 21 cm')],
 puf='Su aktarmada hacim korunur; yeni yükseklik = toplam hacim ÷ suyun bulunduğu kabın taban alanı.',sekil=SK5)

# =================== 06 · Köşegen düzlemle bölme · orta ===================
kartla('K-GPR-06','Prizmayı köşegen düzlemle ikiye bölme','Taban köşegeni Pisagorla bulunur; üçgen prizmanın alanı iki üçgen taban, üç dikdörtgen yan yüz ve kesit yüzünden oluşur.','Kesit yüzünü saymamak; tabanlardan birini unutmak; yarım prizma alanını bütünün yarısı sanmak.','orta',4,'ge-pr-kesme','Prizmadan parça kesme ve yüzey alanı')
a6,b6,c6=9,12,4; d6=sqrt(a6**2+b6**2); assert d6==15
At=a6*b6/2; yan6=(a6+b6+15)*c6; T6=2*At+yan6; assert At==54 and yan6==144 and T6==252 and 2*At+(a6+b6)*c6==192 and At+yan6==198 and T6+15*c6==312
V6={'A':(0,0,0),'B':(a6,0,0),'C':(a6,b6,0),'E':(0,0,c6),'F':(a6,0,c6),'G':(a6,b6,c6)}
nk=un((-b6,a6,0))
FC6={'taban':(list('ABC'),(0,0,-1)),'ust':(list('EFG'),(0,0,1)),'on':(list('ABFE'),(0,-1,0)),'sag':(list('BCGF'),(1,0,0)),'kes':(list('ACGE'),nk)}
S6=Solid(V6,FC6,sc=.25); f=F(); S6.draw(f); Q=S6.Q
assert S6.hid_list()==['AC'],S6.hid_list()
lbl(f,S6,'A','B','$9$',(0,-.28)); lbl(f,S6,'B','C','$12$',(.32,-.12)); lbl(f,S6,'B','F','$4$',(.28,0))
SK6=f.svg()
q('0006',tipId='ge-pr-kesme',tip='Prizmadan parça kesme ve yüzey alanı',z='orta',alt='Prizmayı Bölme',kaz='Dikdörtgenler prizmasının köşegen düzlemle ayrılan parçasının tüm yüzey alanını hesaplar.',kalip='hikâyeli',
 kart='K-GPR-06 (köşegen düzlemle bölme) · 9 × 12 × 4 bloğun yarısı',
 metin='Şekildeki üçgen prizma, dikdörtgenler prizması biçimindeki bir tahta bloğun, tabanının bir köşegenini içeren ve tabana dik olan düzlemle ikiye ayrılmasıyla elde edilen parçalardan biridir. Görünmeyen kenar kesikli çizgiyle gösterilmiştir. Bu parçanın kesit yüzü de dahil bütün yüzleri boyanacaktır.\nBuna göre, boyanacak yüzeyin alanı kaç cm² dir?',
 dogru=252,yan=[(144,'Yalnız yanal alanı (9 + 12 + 15) × 4 hesaplayıp tabanları eklememiş.','dikkat'),(192,'Kesit yüzünü (15 × 4) saymamış: 2 × 54 + (9 + 12) × 4 = 192.','dikkat'),(198,'Tabanlardan yalnız birini eklemiş: 54 + 144 = 198.','dikkat'),(312,'Kesit yüzünü iki kez saymış: 252 + 60 = 312.','dikkat')],
 istenen='Parçanın tüm yüzey alanı (cm²).',
 ip=['Parçanın hangi yüzleri bloğun yüzleridir, hangisi yeni oluşmuştur? Yeni yüzün kenar uzunluklarını nasıl bulursun?'],
 bilgi=[YUZEY,PIS],
 ad=[A('Taban köşegenini bul','Kesit, tabanın köşegeni boyunca olur; üçgen tabanın hipotenüsü köşegendir.','|AC|² = 9² + 12² = 225 → 15'),A('Taban alanını bul','Taban, dik kenarları 9 ve 12 olan dik üçgendir.','9 × 12 ÷ 2 = 54'),A('Yanal alanı bul','Üç yan yüzün kenarları 9, 12 ve 15; yükseklik 4’tür (15 × 4 kesit yüzüdür).','(9 + 12 + 15) × 4 = 144'),A('Tüm alanı yaz','İki taban ile yanal alan toplanır.','2 × 54 + 144 = 252')],
 puf='Prizmayı köşegen düzlemle bölünce yeni oluşan kesit yüzünü iki parçanın alanına da ekle; yarım prizmanın alanı bütünün yarısı değildir.',sekil=SK6)

# =================== 07 · Koliye kutu yerleştirme · orta ===================
kartla('K-GPR-07','Koliye kutu yerleştirme','Her ayrıt boyunca sığan kutu sayısı bölümün tam kısmıdır; üç sayı çarpılır. Yönler yanlış eşleştirilirse sayı değişir.','Kutuyu yanlış yönde dizmek; hacim oranını alıp tam sayıya bakmamak; üç sayıyı toplamak.','orta',4,'ge-pr-yerles','Koliye kutu yerleştirme')
Lk=(60,45,30); Lb=(12,9,5); n7=[Lk[i]//Lb[i] for i in range(3)]; assert n7==[5,5,6] and n7[0]*n7[1]*n7[2]==150 and 60*45*30/(12*9*5)==150 and sum(n7)==16
import itertools
perm={}
for pm in itertools.permutations(range(3)): perm[pm]=1; 
def sg(pm): 
    r=1
    for i in range(3): r*=Lk[i]//Lb[pm[i]]
    return r
assert sg((0,1,2))==150 and sg((0,2,1))==135 and sg((1,0,2))==108 and sg((2,1,0))==120 and sg((2,0,1))==108 and sg((1,2,0))==108
K7=kutu(60,45,30,sc=.07); k7=kutu(12,9,5,sc=.19); shift(k7,6.2,.15)
f=F(); K7.draw(f); k7.draw(f); k7.fillface(f,'ust','fill=vurgu!18')
lbl(f,K7,'A','B','$60$',(0,-.28)); lbl(f,K7,'B','C','$45$',(.28,-.1)); lbl(f,K7,'A','E','$30$',(-.3,0))
lbl(f,k7,'A','B','$12$',(0,-.25)); lbl(f,k7,'B','C','$9$',(.22,-.1)); lbl(f,k7,'A','E','$5$',(-.22,0))
f.node((mid(k7.Q['E'],k7.Q['G'])[0],k7.Q['G'][1]+.3),'kutu')
f.node((mid(K7.Q['E'],K7.Q['G'])[0],K7.Q['G'][1]+.3),'koli')
SK7=f.svg()
q('0007',tipId='ge-pr-yerles',tip='Koliye kutu yerleştirme',z='orta',alt='Koliye Kutu Dizme',kaz='Dikdörtgenler prizması biçimli koliye prizma biçimli kutuların kaç tanesinin sığdığını bulur.',kalip='hikâyeli',
 kart='K-GPR-07 (yerleştirme) · 60 × 45 × 30 koliye 12 × 9 × 5 kutu',
 metin='Bir depoda, şekilde ölçüleri verilen dikdörtgenler prizması biçimli kutular, yine dikdörtgenler prizması biçimli bir koliye dizilecektir. Kutular döndürülmeden, hepsi aynı yönde ve en uzun ayrıtları kolinin en uzun ayrıtına, en kısa ayrıtları kolinin en kısa ayrıtına paralel olacak biçimde sıralanacaktır. Şekil ölçekli değildir.\nBuna göre, koliye en çok kaç kutu sığar?',
 dogru=150,yan=[(16,'Her ayrıt boyunca sığan kutu sayılarını çarpmak yerine toplamış: 5 + 5 + 6 = 16.','bilgi'),(108,'9 cm’lik ayrıtı 60 cm’lik ayrıta koyup 6 × 3 × 6 = 108 bulmuş (yön eşleştirmesi yanlış).','dikkat'),(120,'5 cm’lik ayrıtı 60 cm’lik ayrıta, 12 cm’lik ayrıtı 30 cm’lik ayrıta koymuş: 12 × 5 × 2 = 120.','dikkat'),(135,'5 cm’lik ayrıtı 45 cm’lik, 9 cm’lik ayrıtı 30 cm’lik ayrıta koymuş: 5 × 9 × 3 = 135.','dikkat')],
 istenen='Koliye sığan en çok kutu sayısı.',
 ip=['Her ayrıt doğrultusunda kaç kutunun yan yana dizilebileceğini ayrı ayrı bul; hangi kutu ayrıtı hangi koli ayrıtına paralel?'],
 bilgi=[YERLES],
 ad=[A('Ayrıtları eşleştir','En uzun, orta ve en kısa ayrıtlar birbirine karşılık gelir.','60 ↔ 12 · 45 ↔ 9 · 30 ↔ 5'),A('Her yönde say','Koli ayrıtı kutu ayrıtına bölünür; bölümler tam sayı çıkar.','60 ÷ 12 = 5 · 45 ÷ 9 = 5 · 30 ÷ 5 = 6'),A('Çarp','Üç yöndeki sayılar çarpılır.','5 × 5 × 6 = 150'),A('Hacimle kontrol et','Koli hacmi kutu hacmine tam bölünür.','81000 ÷ 540 = 150')],
 puf='Yerleştirme sorularında kutu sayısı, her ayrıt doğrultusunda sığan sayıların çarpımıdır; yön eşleşmesini önce belirle.',sekil=SK7)

# =================== 08 · Depoya su dolumu ve tahliye · zor ===================
kartla('K-GPR-08','Dolum ve tahliye birlikte','Depo hacmi litreye çevrilir; kalan boş hacmi, dolum ile boşaltma hızı farkı olan net hıza bölmek süreyi verir.','Başlangıçtaki suyu unutmak; hızları toplamak; yalnız dolum ya da boşaltma hızıyla hesap yapmak.','zor',5,'ge-pr-su','Prizma biçimli kapta su doldurma, aktarma ve boşaltma')
a8,b8,c8,h8=150,100,80,20; cap=a8*b8*c8/1000; w0=a8*b8*h8/1000; dol,bos=45,30
assert cap==1200 and w0==300 and (cap-w0)/(dol-bos)==60 and (cap-w0)/dol==20 and cap/(dol-bos)==80 and (cap-w0)/(dol+bos)==12 and (cap-w0)/bos==30 and (cap-w0)%(dol-bos)==0
K8=kutu(a8,b8,c8,sc=.032); W8=kutu(a8,b8,h8,sc=.032)
f=F(); sudolu(f,W8); K8.draw(f); W8.draw(f,'','dashed')
assert K8.hid_list()==['AD','CD','DH']
lbl(f,K8,'A','B','$150$',(0,-.3)); lbl(f,K8,'B','C','$100$',(.38,-.1)); okdim(f,K8,'A','E','$80$',-.95,.3)
f.node(add(mid(W8.Q['B'],W8.Q['F']),(.28,0)),'$20$') if False else None
okdim(f,W8,'A','E','$20$',-.2,.3)
SK8=f.svg()
q('0008',tipId='ge-pr-su',tip='Prizma biçimli kapta su doldurma, aktarma ve boşaltma',z='zor',alt='Dolum ve Boşaltma',kaz='Dikdörtgenler prizması biçimli depoda dolum ve boşaltma hızlarının farkıyla dolma süresini hesaplar.',kalip='hikâyeli',
 kart='K-GPR-08 (dolum-tahliye) · 150 × 100 × 80 depo, 20 cm su',
 metin='İç ölçüleri şekilde verilen dikdörtgenler prizması biçimli su deposunun iç yüksekliği (dıştaki ok) ve içindeki suyun yüksekliği (içteki ok) şekilde gösterilmiştir. Depoyu dolduran musluk dakikada 45 litre su akıtırken, aynı anda açık olan tahliye borusu dakikada 30 litre su boşaltmaktadır. Her iki akış da sabit hızla sürmektedir. 1 litre = 1000 cm³ tür.\nBuna göre, ikisi aynı anda açıldığında depo ağzına kadar kaç dakikada dolar?',
 dogru=60,yan=[(12,'Hızları toplayıp 900 ÷ (45 + 30) = 12 bulmuş.','bilgi'),(20,'Boşaltmayı dikkate almayıp yalnız dolum hızıyla 900 ÷ 45 = 20 bulmuş.','dikkat'),(30,'Yalnız tahliye hızıyla 900 ÷ 30 = 30 bulmuş.','dikkat'),(80,'Başlangıçtaki suyu hesaba katmayıp 1200 ÷ 15 = 80 bulmuş.','dikkat')],
 istenen='Deponun dolma süresi (dakika).',
 ip=['Depoda başlangıçta ne kadar su olduğunu ve bir dakikada depoda gerçekte kaç litre su biriktiğini bul.'],
 bilgi=[HACIM,LITRE],
 ad=[A('Deponun hacmini bul','Depo, 150 × 100 × 80 cm ölçülerinde bir prizmadır.','150 × 100 × 80 = 1 200 000 cm³ = 1200 L'),A('Başlangıçtaki suyu bul','Suyun yüksekliği 20 cm olduğundan hacmi hesapla.','150 × 100 × 20 = 300 000 cm³ = 300 L'),A('Boş hacmi bul','Depo dolana kadar eklenecek su.','1200 − 300 = 900 L'),A('Net hızı hesapla','Dolum ve boşaltma birlikte açıkken depoda biriken su.','45 − 30 = 15 L/dk'),A('Süreyi bul','Boş hacim net hıza bölünür.','900 ÷ 15 = 60 dakika')],
 puf='Dolum ve tahliye birlikteyse dakikadaki net su miktarı hızların farkıdır; süre = boş hacim ÷ net hız.',sekil=SK8)

# =================== yaz ===================
def bitir_geo(onek):
    for qq in P.ANA: qq['kardes']=None
    P.yaz(os.path.join(GD,f'{onek}-1.json'),f'/tmp/bos-{onek}.json')
    tipler={}
    for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=TIPK[c['tipId']]))['kartlar'].append(c['id'])
    json.dump(dict(konu=P.konu_adi,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 TYT Geometri çıkmış soruları (yalnız mantık), MEB 9–10. sınıf geometri müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar',f'{onek}.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler))
bitir_geo('prizma')
