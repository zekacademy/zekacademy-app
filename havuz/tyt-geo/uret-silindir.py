"""TYT Geometri · Silindir (kardeş yok, ipucu 1). Şekil koordinatları hesaplanır; TikZ gövdesi aynı değerlerden üretilir (cizim.tikz_svg).
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
P=Parti('silindir','Silindir','geo|Silindir',ders='TYT Geometri',idon='tytgeo')
def cyl(f,cx,cy,R,Hc,ry,fillw=None):
    """Dik silindir (eksen dikey). Taban merkezi (cx,cy). Üst elips tam, alt ön yay düz, alt arka yay kesikli. fillw: su yüksekliği (şekil birimi)."""
    if fillw:
        f.raw(f'\\fill[fill=vurgu!18] ({cx-R:.3f},{cy:.3f}) rectangle ({cx+R:.3f},{cy+fillw:.3f});')
        f.raw(f'\\fill[fill=vurgu!18] ({cx-R:.3f},{cy:.3f}) arc[start angle=180,end angle=360,x radius={R:.3f},y radius={ry:.3f}] -- cycle;')
        f.raw(f'\\fill[fill=vurgu!18] ({cx:.3f},{cy+fillw:.3f}) ellipse [x radius={R:.3f},y radius={ry:.3f}];')
        f.raw(f'\\draw[thin] ({cx:.3f},{cy+fillw:.3f}) ellipse [x radius={R:.3f},y radius={ry:.3f}];')
    f.raw(f'\\draw ({cx:.3f},{cy+Hc:.3f}) ellipse [x radius={R:.3f},y radius={ry:.3f}];')
    f.line((cx-R,cy),(cx-R,cy+Hc)); f.line((cx+R,cy),(cx+R,cy+Hc))
    f.raw(f'\\draw ({cx-R:.3f},{cy:.3f}) arc[start angle=180,end angle=360,x radius={R:.3f},y radius={ry:.3f}];')
    f.raw(f'\\draw[dashed] ({cx-R:.3f},{cy:.3f}) arc[start angle=180,end angle=0,x radius={R:.3f},y radius={ry:.3f}];')
def yaricap(f,cx,cy,R,t,yuk=0,asag=False):
    f.raw(f'\\fill ({cx:.3f},{cy:.3f}) circle (1pt);'); f.line((cx,cy),(cx+R,cy)); f.node((cx+R+.24,cy),t)
HACIMS=B('Silindirin hacmi','taban alanı × yükseklik: V = π × r² × h. Örnek: r = 2 ve h = 5 olan silindirin hacmi π × 4 × 5 = 20π dir')
YANAL=B('Silindirin yüzey alanı','yanal alan = taban çevresi × yükseklik = 2π × r × h; tüm yüzey alanı = yanal alan + 2 × π × r² dir. Açınımda yan yüzey, kenarları 2πr ve h olan bir dikdörtgendir. Örnek: r = 3 ve h = 4 için yanal alan 24π, tüm yüzey alanı 24π + 18π = 42π dir')
BILYE=B('Cisim batınca su yüksekliği','batan cismin hacmi kadar su seviyesi yükselir: artış = cismin hacmi ÷ kabın taban alanı. Örnek: taban alanı 25π olan kaba hacmi 50π olan cisim batarsa su 2 cm yükselir')
KESIKB=B('Kesik silindirin hacmi','taban yarıçapı r olan silindir, tabana paralel olmayan düzlemle kesilirse hacim V = π × r² × (h₁ + h₂) ÷ 2 dir (en kısa ve en uzun ana doğruların ortalaması). Örnek: r = 2, h₁ = 3, h₂ = 5 için V = π × 4 × 4 = 16π dır')
BORUB=B('İçi boş silindir (boru)','boru, büyük bir silindirden içindeki silindirik boşluğun çıkarılmasıyla elde edilmiş gibi düşünülür; çap, yarıçapın iki katıdır. Örnek: hacmi 100π olan bir silindirden 40π lık bir parça çıkarılırsa 60π kalır')
YARIMB=B('Yarım silindir','bir silindir, ekseninden geçen düzlemle boyuna ikiye bölünürse her parça yarım silindirdir ve hacmi tam silindirin hacminin yarısıdır. Örnek: hacmi 40π olan silindirin yarım parçasının hacmi 20π dir')
CEVRE=B('Daire çevresi ve alanı','yarıçapı r olan dairenin çevresi 2πr, alanı πr² dir. Örnek: r = 5 için çevre 10π, alan 25π dir')

# =================== 01 · Hacim · kolay ===================
konu('geo|Silindir','Silindir')
kartla('K-GSL-01','Silindirin hacmi','Taban alanı πr² yükseklikle çarpılır; yarıçap ve yükseklik karıştırılmaz.','Çapı yarıçap sanmak; r² yerine r almak; yanal alanla karıştırmak.','kolay',3,'ge-sl-hacim','Silindirin hacmi')
r1,h1=3,10; assert pi*r1**2*h1/pi==90 and r1*h1==30 and 2*r1*h1==60 and r1*h1**2==300 and 2*pi*r1**2*h1/pi==180 and (r1*h1)**2==900
sc=.25; R=r1*sc; Hc=h1*sc; ry=R*.3
f=F(); cyl(f,0,0,R,Hc,ry); yaricap(f,0,Hc,R,'$3$'); f.node((R+.3,Hc/2),'$10$')
SK1=f.svg()
q('0001',tipId='ge-sl-hacim',tip='Silindirin hacmi',z='kolay',alt='Hacim',kaz='Silindirin taban yarıçapı ve yüksekliğinden hacmini hesaplar.',kalip='hikâyeli',
 kart='K-GSL-01 (silindirin hacmi) · r = 3, h = 10',
 metin='Bir konserve fabrikası, şekilde ölçüleri cm cinsinden verilen silindir biçimli teneke kutular üretmektedir. Kutular, ağzına kadar ürünle doldurulacak ve kutu cidarının kalınlığı ihmal edilecektir.\nBuna göre, bir kutuya konulan ürünün hacmi kaç cm³ tür?',
 dogru=Pk(90),sira=sirala(Pk(90),Pk(180),Pk(300),Pk(360),Pk(900)),
 yan=[(Pk(180),'Hacim formülünü 2 ile çarpıp 2 × π × 3² × 10 = 180π bulmuş (2πr²h değildir).','bilgi'),(Pk(300),'Yarıçap ile yüksekliği karıştırıp π × 3 × 10² = 300π bulmuş.','bilgi'),(Pk(360),'3 cm’yi yarıçap bilip çapı (6) yarıçap yerine kullanmış: π × 6² × 10 = 360π.','bilgi'),(Pk(900),'Yarıçapla yüksekliği çarpıp karesini almış: π × (3 × 10)² = 900π.','islem')],
 istenen='Kutunun hacmi (cm³).',
 ip=['Silindirin hacmi, tabanının alanı ile yüksekliğinin çarpımıdır; taban hangi şekil?'],
 bilgi=[HACIMS,CEVRE],
 ad=[A('Formülü yaz','Silindirin hacmi taban alanı ile yüksekliğin çarpımıdır.','V = π × r² × h'),A('Taban alanını bul','Taban, yarıçapı 3 cm olan bir dairedir.','π × 3² = 9π'),A('Hacmi hesapla','Taban alanını yükseklikle çarp.','9π × 10 = 90π')],
 puf='Silindirin hacmi için önce taban dairesinin alanını bul, sonra yükseklikle çarp.',sekil=SK1)

# =================== 02 · Yanal alan · kolay ===================
kartla('K-GSL-02','Silindirin yanal alanı','Yan yüzey açılınca kenarları taban çevresi ve yükseklik olan dikdörtgen olur: 2πrh.','Tüm yüzey alanıyla karıştırmak; πrh yazıp 2’yi unutmak; hacim hesaplamak.','kolay',3,'ge-sl-yanal','Silindirin yanal ve tüm yüzey alanı')
r2,h2=4,9; assert 2*r2*h2==72 and r2*h2==36 and 2*r2*h2+2*r2**2==104 and r2**2*h2==144 and 2*r2**2*h2==288
sc=.22; R=r2*sc; Hc=h2*sc; ry=R*.3
f=F(); cyl(f,0,0,R,Hc,ry); yaricap(f,0,Hc,R,'$4$'); f.node((R+.3,Hc/2),'$9$')
SK2=f.svg()
q('0002',tipId='ge-sl-yanal',tip='Silindirin yanal ve tüm yüzey alanı',z='kolay',alt='Yanal Alan',kaz='Silindirin yanal alanını yarıçap ve yüksekliğinden hesaplar.',kalip='hikâyeli',
 kart='K-GSL-02 (yanal alan) · r = 4, h = 9 peynir kutusu',
 metin='Silindir biçimli bir peynir kutusunun ölçüleri şekilde cm cinsinden verilmiştir. Kutunun yan yüzeyi (alt ve üst kapağı hariç), boydan boya ve kutunun yüksekliğince bir etiketle çevrelenecektir. Etiket kutuya tam oturacak, üst üste binmeyecektir.\nBuna göre, etiketin alanı kaç cm² dir?',
 dogru=Pk(72),sira=sirala(Pk(36),Pk(72),Pk(104),Pk(144),Pk(288)),
 yan=[(Pk(36),'Yanal alan formülünde 2 çarpanını unutup π × 4 × 9 = 36π bulmuş.','bilgi'),(Pk(104),'Tüm yüzey alanını (72π + 2 × 16π) hesaplamış; kapaklar etikete dahil değildir.','dikkat'),(Pk(144),'Yanal alan yerine hacmi (π × 4² × 9) bulmuş.','bilgi'),(Pk(288),'Yanal alanı 2 × π × r² × h olarak yazıp 2 × π × 16 × 9 = 288π bulmuş.','bilgi')],
 istenen='Etiketin alanı (cm²).',
 ip=['Etiket kutunun yan yüzeyine sarılıp açılırsa nasıl bir şekil olur? Kenarlarından biri taban çevresiyle ilişkili.'],
 bilgi=[YANAL],
 ad=[A('Açınımı düşün','Yan yüzey açılınca dikdörtgen olur; bir kenarı yükseklik, diğeri taban çevresidir.','kenarlar: 2πr ve h'),A('Taban çevresini bul','Taban yarıçapı 4 cm olan dairenin çevresi.','2 × π × 4 = 8π'),A('Alanı hesapla','Dikdörtgenin alanı kenarlarının çarpımıdır.','8π × 9 = 72π')],
 puf='Silindirin yanal alanı, taban çevresi ile yüksekliğin çarpımıdır: 2πrh.',sekil=SK2)

# =================== 03 · Açınım · orta ===================
kartla('K-GSL-03','Silindirin açınımı ve tüm yüzey alanı','Açınımdaki dikdörtgenin uzun kenarı taban çevresidir; yarıçap çevreden bulunur, iki taban ve yanal alan toplanır.','Yarıçapı çevre sanmak; tabanları saymamak; tek taban saymak.','orta',4,'ge-sl-acinim','Silindirin açınımı')
W3,H3=12,8; r3=W3/2; T3=2*pi*r3*H3/pi+2*r3**2; assert r3==6 and T3==168 and W3*H3==96 and 96+36==132 and 2*r3**2==72 and r3**2*H3==288
s=.115; w=W3*pi*s; hh=H3*s; rr=r3*s
f=F(); f.raw(f'\\draw (0,0) rectangle ({w:.3f},{hh:.3f});')
cx=w*.35
f.raw(f'\\draw ({cx:.3f},{-rr:.3f}) circle ({rr:.3f}); \\draw ({cx:.3f},{hh+rr:.3f}) circle ({rr:.3f});')
f.node((w/2,hh/2),'$8$'); f.node((w*.78,hh+.28),'$12\\pi$')
SK3=f.svg()
q('0003',tipId='ge-sl-acinim',tip='Silindirin açınımı',z='orta',alt='Açınım',kaz='Silindirin açınımındaki dikdörtgenden yarıçapı bulup tüm yüzey alanını hesaplar.',kalip='hikâyeli',
 kart='K-GSL-03 (açınım) · dikdörtgen 12π × 8',
 metin='Bir terzi, silindir biçimli bir kalem kutusu için şekilde cm cinsinden gösterilen açınımı kumaştan kesmiştir. Dikdörtgen kısım kutunun yan yüzeyini, iki daire kapaklarını oluşturmaktadır; her dairenin çevresi, dikdörtgenin uzun kenarına eşittir. Kumaşın birleşim payı hesaba katılmayacaktır.\nBuna göre, kutuyu kaplayan kumaşın toplam alanı kaç cm² dir?',
 dogru=Pk(168),sira=sirala(Pk(72),Pk(96),Pk(132),Pk(168),Pk(288)),
 yan=[(Pk(72),'Yalnız iki dairenin alanını (2 × 36π) bulmuş.','dikkat'),(Pk(96),'Yalnız dikdörtgenin alanını (12π × 8) bulup daireleri eklememiş.','dikkat'),(Pk(132),'Dairelerden yalnız birini eklemiş: 96π + 36π = 132π.','dikkat'),(Pk(288),'Toplam alan yerine hacmi (π × 36 × 8) hesaplamış.','bilgi')],
 istenen='Kumaşın toplam alanı (cm²).',
 ip=['Dairenin çevresi 12π ise yarıçapı kaçtır? Önce bunu bul, sonra üç parçanın alanlarını topla.'],
 bilgi=[YANAL,CEVRE],
 ad=[A('Yarıçapı bul','Dairenin çevresi, dikdörtgenin uzun kenarı olan 12π’ye eşittir.','2πr = 12π → r = 6'),A('Yanal alanı bul','Dikdörtgenin kenarları 12π ve 8’dir.','12π × 8 = 96π'),A('Tabanların alanı','Yarıçapı 6 olan iki daire vardır.','2 × π × 6² = 72π'),A('Toplamı yaz','Yanal alan ile iki tabanın alanı toplanır.','96π + 72π = 168π')],
 puf='Açınımda dikdörtgenin uzun kenarı taban çevresidir; yarıçapı buradan bul ve iki tabanı unutma.',sekil=SK3)

# =================== 04 · Su ve bilye · orta ===================
kartla('K-GSL-04','Silindirik kaba bilye bırakma','Batan bilyelerin toplam hacmi taban alanına bölünerek su seviyesindeki artış bulunur ve ilk yüksekliğe eklenir.','Yalnız artışı yanıt vermek; taban alanı yerine yarıçapa bölmek; bilye sayısını yanlış almak.','orta',4,'ge-sl-su','Silindirik kaba cisim bırakınca su yüksekliği')
rr4,hw4,vb,nb=6,10,36,3; art=nb*vb/rr4**2; assert art==3 and hw4+art==13 and nb*vb/rr4==18 and hw4+18==28 and hw4+2*vb/36*3==16
sc=.14; R=rr4*sc; Hc=16*sc; ry=R*.3
f=F(); cyl(f,0,0,R,Hc,ry,fillw=hw4*sc); yaricap(f,0,Hc,R,'$6$'); f.node((-R-.3,hw4*sc/2),'$10$')
for i,(x,y) in enumerate([(2.0,.18),(2.45,.18),(2.225,.52)]): f.raw(f'\\draw[fill=vurgu!45] ({x:.3f},{y:.3f}) circle (.2);')
f.node((2.2,.95),'bilyeler')
SK4=f.svg()
q('0004',tipId='ge-sl-su',tip='Silindirik kaba cisim bırakınca su yüksekliği',z='orta',alt='Su ve Bilye',kaz='Silindirik kaptaki suya bilye bırakıldığında su yüksekliğini hacim üzerinden hesaplar.',kalip='hikâyeli',
 kart='K-GSL-04 (su, bilye) · r = 6, su 10 cm, 3 bilye 36π',
 metin='Taban yarıçapı şekilde verilen silindir biçimli bir akvaryumda, şekilde gösterilen yüksekliğe kadar su vardır. Hacimleri 36π cm³ olan özdeş üç cam bilye, suyun içine tamamen batacak biçimde akvaryuma bırakılıyor; bilyelerin her biri tamamen suya batıyor ve akvaryumdan su taşmıyor.\nBuna göre, bilyeler bırakıldıktan sonra akvaryumdaki su yüksekliği kaç cm olur?',
 dogru=13,yan=[(3,'Yalnız su seviyesindeki artışı (108π ÷ 36π = 3) bulmuş; ilk yüksekliği eklememiş.','dikkat'),(16,'Bilye hacmini iki katı almış: artışı 6 bulup 10 + 6 = 16 yazmış.','islem'),(18,'Hacmi taban alanı yerine yarıçapa bölmüş: 108π ÷ 6π = 18.','bilgi'),(28,'Hacmi yarıçapa bölüp (18) ilk yüksekliğe eklemiş: 10 + 18 = 28.','bilgi')],
 istenen='Bilyeler bırakıldıktan sonra su yüksekliği (cm).',
 ip=['Suyun yükselmesine neden olan hacim ne kadar? Bu hacim hangi alana yayılarak yüksekliği artırır?'],
 bilgi=[BILYE,HACIMS],
 ad=[A('Bilyelerin toplam hacmi','Üç özdeş bilyenin hacimleri toplanır.','3 × 36π = 108π'),A('Taban alanını bul','Akvaryumun tabanı yarıçapı 6 cm olan dairedir.','π × 6² = 36π'),A('Yükselmeyi hesapla','Su seviyesindeki artış hacmin taban alanına bölümüdür.','108π ÷ 36π = 3 cm'),A('Yeni yüksekliği yaz','İlk yüksekliğe artışı ekle.','10 + 3 = 13')],
 puf='Suya cisim batınca yükselme = cismin hacmi ÷ kabın taban alanı; sonra ilk su yüksekliğine ekle.',sekil=SK4)

# =================== 05 · Yarım silindir oluk · orta ===================
kartla('K-GSL-05','Yarım silindir biçimli oluğun hacmi','Boyuna ikiye bölünmüş silindirin hacmi, tam silindirin hacminin yarısıdır.','Yarıyı unutmak; çapı yarıçap sanmak; yanal alanla karıştırmak.','orta',3,'ge-sl-yarim','Yarım silindirin hacmi')
r5,L5=10,30; assert pi*r5**2*L5/2/pi==1500 and r5**2*L5==3000 and r5**2*L5*4/2==6000 and 0.5*2*r5*L5==300 and r5**2/2==50
sc=.09; R=r5*sc; v=(L5*.5*cos(KA)*sc,L5*.5*sin(KA)*sc); phi=degrees(atan2(v[1],v[0]))
def pl(ps,st=''): return '\\draw['+st+'] '+' -- '.join(pt(p) for p in ps)+';'
f=F()
fr=[(R*cos(radians(t)),R*sin(radians(t))) for t in range(180,361,5)]
f.raw(pl(fr)); f.line((-R,0),(R,0))
f.line((-R,0),add((-R,0),v)); f.line((R,0),add((R,0),v)); f.line(add((-R,0),v),add((R,0),v))
t0=int(round(phi-90))
vis=[add(v,(R*cos(radians(t)),R*sin(radians(t)))) for t in range(t0,1,5)]
f.raw(pl(vis))
f.line((R*cos(radians(t0)),R*sin(radians(t0))),add((R*cos(radians(t0)),R*sin(radians(t0))),v))
hid=[add(v,(R*cos(radians(t)),R*sin(radians(t)))) for t in range(180,t0+361,5)]
f.raw(pl(hid,'dashed'))
f.raw('\\fill (0,0) circle (1pt);'); f.line((0,0),(-R,0),'dashed') if False else None
f.node((0,-.28),'$10$'); f.node((R+v[0]/2+.6,v[1]/2-.25),'$30$')
SK5=f.svg()
q('0005',tipId='ge-sl-yarim',tip='Yarım silindirin hacmi',z='orta',alt='Yarım Silindir',kaz='Boyuna ikiye bölünmüş silindir biçimli oluğun hacmini hesaplar.',kalip='hikâyeli',
 kart='K-GSL-05 (yarım silindir) · r = 10, uzunluk 30',
 metin='Bir çatı oluğu, silindir biçimli bir borunun boyuna tam ortadan ikiye bölünmesiyle yapılmıştır. Şekilde, oluğun kesit yarıçapı ve uzunluğu cm cinsinden verilmiştir. Oluk ağzına kadar suyla doldurulacaktır; oluğun iki ucu da kapalı, cidar kalınlığı ihmal edilecektir.\nBuna göre, oluğa en çok kaç cm³ su konabilir?',
 dogru=Pk(1500),sira=sirala(Pk(50),Pk(300),Pk(1500),Pk(3000),Pk(6000)),
 yan=[(Pk(50),'Uzunluğu hesaba katmadan yarım dairenin alanını (π × 100 ÷ 2) bulmuş.','dikkat'),(Pk(300),'Hacim yerine yanal alanın yarısını (½ × 2π × 10 × 30) hesaplamış.','bilgi'),(Pk(3000),'Oluğu tam silindir sanıp yarıyı almayı unutmuş: π × 10² × 30.','dikkat'),(Pk(6000),'10’u yarıçap yerine çap sanıp r = 20 almış: π × 20² × 30 ÷ 2 = 6000π.','bilgi')],
 istenen='Oluğun hacmi (cm³).',
 ip=['Oluğu, aynı ölçülerde tam bir silindirin parçası olarak düşün; bu parça silindirin ne kadarı?'],
 bilgi=[HACIMS,YARIMB],
 ad=[A('Tam silindirin hacmi','Önce aynı yarıçap ve uzunlukta tam silindir düşün.','π × 10² × 30 = 3000π'),A('Yarısını al','Oluğa karşılık gelen parça bu silindirin yarısıdır.','3000π ÷ 2'),A('Sonucu yaz','Yarı hacim.','1500π')],
 puf='Boyuna ikiye bölünen silindirin hacmi, tam silindirin hacminin yarısıdır.',sekil=SK5)

# =================== 06 · Bidon, bardak · orta ===================
kartla('K-GSL-06','Bidondaki suyu bardaklara paylaştırma','İki silindirin hacmi hesaplanıp oranlanır; oranda yarıçaplar karesiyle, yükseklikler birinci kuvvetle yer alır.','Yarıçap oranının karesini almamak; yalnız yükseklik oranını almak; litre değerini cevap sanmak.','orta',4,'ge-sl-hacim','Silindirin hacmi')
rb,hb,rc,hc=10,50,5,10; Vb=3*rb**2*hb; Vc=3*rc**2*hc; assert Vb==15000 and Vc==750 and Vb/Vc==20 and (rb/rc)*(hb/hc)==10 and hb/hc==5 and Vb/1000==15 and Vb/(3*rc**2*5)==40
f=F(); sc1=.05; sc2=.09
R1=rb*sc1; H1=hb*sc1; ry1=R1*.3
cyl(f,0,0,R1,H1,ry1); yaricap(f,0,H1,R1,'$10$'); f.node((R1+.3,H1/2),'$50$'); f.node((0,-.6),'bidon')
R2=rc*sc2; H2=hc*sc2; ry2=R2*.3; ox=2.6
cyl(f,ox,0,R2,H2,ry2); yaricap(f,ox,H2,R2,'$5$'); f.node((ox+R2+.3,H2/2),'$10$'); f.node((ox,-.6),'bardak')
SK6=f.svg()
q('0006',tipId='ge-sl-hacim',tip='Silindirin hacmi',z='orta',alt='Bidon ve Bardak',kaz='Silindir biçimli iki kabın hacimlerini oranlayarak kaç bardak dolacağını bulur.',kalip='hikâyeli',
 kart='K-GSL-06 (bidon, bardak) · π = 3, 15 litrelik bidon',
 metin='Şekilde ölçüleri cm cinsinden verilen silindir biçimli bidon, ağzına kadar suyla doludur. Bu suyun tamamı, yine şekilde ölçüleri verilen silindir biçimli bardaklara, her bardak ağzına kadar dolacak ve hiç su artmayacak biçimde paylaştırılıyor. Kapların cidar kalınlığı ihmal edilecek, π = 3 alınacaktır. Şekil ölçekli değildir.\nBuna göre, kaç bardak doldurulur?',
 dogru=20,yan=[(5,'Yalnız yüksekliklerin oranını (50 ÷ 10) almış.','bilgi'),(10,'Yarıçapların oranını karesiz alıp 2 × 5 = 10 bulmuş.','bilgi'),(15,'Bidonun hacmini litre olarak (15 L) bulup cevap yazmış.','dikkat'),(40,'Bardağın yüksekliğini 10 yerine 5 alıp 15000 ÷ 375 = 40 bulmuş.','dikkat')],
 istenen='Doldurulan bardak sayısı.',
 ip=['Bidonun ve bir bardağın hacmini ayrı ayrı bul; sonra birini diğerine böl.'],
 bilgi=[HACIMS],
 ad=[A('Bidonun hacmi','π = 3, r = 10 ve h = 50 ile hacmi yaz.','3 × 10² × 50 = 15 000 cm³'),A('Bardağın hacmi','π = 3, r = 5 ve h = 10 ile hacmi yaz.','3 × 5² × 10 = 750 cm³'),A('Bardak sayısı','Toplam su, bir bardağın hacmine bölünür.','15 000 ÷ 750 = 20')],
 puf='Paylaştırma sorularında iki hacmi ayrı hesaplayıp böl; oranda yarıçaplar karesiyle yer alır.',sekil=SK6)

# =================== 07 · Boru · zor ===================
kartla('K-GSL-07','İçi boş silindir (boru) hacmi','Çaplar yarıya bölünüp yarıçap yapılır; boru hacmi dış silindirin hacminden iç silindirin hacmi çıkarılarak bulunur.','Çapı yarıçap sanmak; yarıçap farkının karesini almak; yalnız taban halkasının alanını vermek.','zor',4,'ge-sl-boru','İçi boş silindir (boru) hacmi')
D7,d7,L7=12,8,10; R7,r7=D7/2,d7/2; V7=(R7**2-r7**2)*L7; assert V7==200 and (R7**2-r7**2)==20 and (R7-r7)**2*L7==40 and R7**2*L7==360 and r7**2*L7==160 and (D7**2-d7**2)*L7==800
sc=.17; Rr=R7*sc; rr=r7*sc; v=(L7*.5*cos(KA)*sc,L7*.5*sin(KA)*sc); phi=degrees(atan2(v[1],v[0])); nv=(-v[1]/ln(v),v[0]/ln(v)); P1=v
f=F()
f.raw(f'\\draw (0,0) circle ({Rr:.3f}); \\draw (0,0) circle ({rr:.3f});')
for sg in (1,-1): f.line((sg*nv[0]*Rr,sg*nv[1]*Rr),(P1[0]+sg*nv[0]*Rr,P1[1]+sg*nv[1]*Rr))
f.raw(f'\\draw ({P1[0]+nv[0]*Rr:.3f},{P1[1]+nv[1]*Rr:.3f}) arc[start angle={phi+90:.2f},end angle={phi-90:.2f},radius={Rr:.3f}];')
f.raw(f'\\draw[dashed] ({P1[0]:.3f},{P1[1]:.3f}) circle ({rr:.3f});')
f.raw(f'\\draw[<->,thin] ({-Rr:.3f},{-Rr-.3:.3f}) -- ({Rr:.3f},{-Rr-.3:.3f});'); f.node((0,-Rr-.6),'dış çap $12$')
f.node((-Rr-1.0,0),'iç çap $8$'); f.raw(f'\\draw[->,thin] ({-Rr-.38:.3f},0) -- ({-rr:.3f},0);')
f.node((P1[0]/2-nv[0]*(Rr+.3),P1[1]/2-nv[1]*(Rr+.3)),'$10$')
SK7=f.svg()
q('0007',tipId='ge-sl-boru',tip='İçi boş silindir (boru) hacmi',z='zor',alt='Boru',kaz='İçi boş silindir biçimli borunun malzeme hacmini dış ve iç çaplardan hesaplar.',kalip='hikâyeli',
 kart='K-GSL-07 (boru hacmi) · dış çap 12, iç çap 8, uzunluk 10',
 metin='Şekilde ölçüleri cm cinsinden verilen, silindir biçimli içi boş bir metal boru dökümle üretilmektedir. Borunun dış çapı ile iç çapı ve uzunluğu şekilde gösterilmiştir; borunun iç yüzeyi de silindir biçimlidir ve iki ucu açıktır. Döküm için gereken metal hacmi hesaplanacaktır.\nBuna göre, boruyu oluşturan metalin hacmi kaç cm³ tür?',
 dogru=Pk(200),sira=sirala(Pk(20),Pk(40),Pk(160),Pk(200),Pk(800)),
 yan=[(Pk(20),'Yalnız boru kesitindeki halkanın alanını (36π − 16π) bulmuş; uzunlukla çarpmamış.','dikkat'),(Pk(40),'Yarıçap farkının karesini almış: π × (6 − 4)² × 10 = 40π.','bilgi'),(Pk(160),'İçteki boşluğun hacmini (π × 4² × 10) bulmuş.','dikkat'),(Pk(800),'Çapları yarıçap sanıp π × (12² − 8²) × 10 = 800π bulmuş.','bilgi')],
 istenen='Boruyu oluşturan metalin hacmi (cm³).',
 ip=['Boru, büyük bir silindirden küçük bir silindirin çıkarılmasıyla oluşmuş gibidir; verilen uzunluklar çap mı yarıçap mı?'],
 bilgi=[BORUB,HACIMS],
 ad=[A('Yarıçapları bul','Çaplar yarıya bölünür.','dış: 12 ÷ 2 = 6 · iç: 8 ÷ 2 = 4'),A('Dış silindirin hacmi','Boru dolu bir silindir olsaydı hacmi.','π × 6² × 10 = 360π'),A('İç boşluğun hacmi','İçteki silindirik boşluğun hacmi.','π × 4² × 10 = 160π'),A('Farkı al','Metalin hacmi iki hacmin farkıdır.','360π − 160π = 200π')],
 puf='Boru sorularında çaplardan yarıçaplara geç; metalin hacmi = π (R² − r²) × uzunluk.',sekil=SK7)

# =================== 08 · Yanal alan ve hacimden tüm yüzey · zor ===================
kartla('K-GSL-08','Yanal alan ve hacimden yarıçap','Hacmin yanal alana bölümü r ÷ 2 verir; yarıçap ve yükseklik bulunup tüm yüzey alanı yazılır.','Yanal alanı tüm yüzey sanmak; yalnız bir taban eklemek; yanal alanı iki katı almak.','zor',4,'ge-sl-yanal','Silindirin yanal ve tüm yüzey alanı')
L8,V8=48,144; r8=2*V8/L8; h8=L8/(2*r8); T8=L8+2*r8**2; assert r8==6 and h8==4 and T8==120 and L8+r8**2==84 and 2*r8**2==72 and 2*L8==96 and pi*r8**2*h8/pi==144 and 2*r8*h8==48
sc=.22; R=1.0; Hc=1.3; ry=R*.3
f=F(); cyl(f,0,0,R,Hc,ry); yaricap(f,0,Hc,R,'$r$'); f.node((R+.28,Hc/2),'$h$')
SK8=f.svg()
q('0008',tipId='ge-sl-yanal',tip='Silindirin yanal ve tüm yüzey alanı',z='zor',alt='Yüzey Alanı',kaz='Silindirin yanal alanı ve hacminden yarıçapı ile yüksekliğini bulup tüm yüzey alanını hesaplar.',kalip='yeni nesil',
 kart='K-GSL-08 (yanal alan + hacim → tüm yüzey) · 48π ve 144π',
 metin='Şekildeki dik silindirin yanal alanı 48π cm², hacmi 144π cm³ tür. Silindirin taban yarıçapı r, yüksekliği h ile gösterilmiştir.\nBuna göre, bu silindirin alt ve üst tabanları dahil tüm yüzey alanı kaç cm² dir?',
 dogru=Pk(120),sira=sirala(Pk(48),Pk(72),Pk(84),Pk(96),Pk(120)),
 yan=[(Pk(48),'Yanal alanı tüm yüzey alanı sanmış.','dikkat'),(Pk(72),'Yalnız iki tabanın alanını (2 × 36π) bulmuş.','dikkat'),(Pk(84),'Tabanlardan yalnız birini yanal alana eklemiş: 48π + 36π.','dikkat'),(Pk(96),'Taban alanlarını da yanal alan kadar sanıp 2 × 48π = 96π bulmuş.','bilgi')],
 istenen='Silindirin tüm yüzey alanı (cm²).',
 ip=['İki veriyi birlikte kullanarak önce tek bir bilinmeyeni nasıl bulabilirsin?'],
 bilgi=[HACIMS,YANAL],
 ad=[A('Yarıçapı bul','Hacmin yanal alana oranında π, r ve h sadeleşir.','πr²h ÷ 2πrh = r ÷ 2 = 144π ÷ 48π = 3 → r = 6'),A('Yüksekliği bul','Yanal alan formülünde r yerine 6 yaz.','2π × 6 × h = 48π → h = 4'),A('Tabanların alanı','Yarıçapı 6 olan iki daire.','2 × π × 6² = 72π'),A('Toplamı yaz','Yanal alana iki tabanı ekle.','48π + 72π = 120π')],
 puf='Hacim ve yanal alan birlikte verilince iki veriyi oranlayıp önce yarıçapı bul; sonra yüksekliğe geç.',sekil=SK8)

# =================== yaz ===================
def bitir_geo(onek):
    for qq in P.ANA: qq['kardes']=None
    P.yaz(os.path.join(GD,f'{onek}-1.json'),f'/tmp/bos-{onek}.json')
    tipler={}
    for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=TIPK[c['tipId']]))['kartlar'].append(c['id'])
    json.dump(dict(konu=P.konu_adi,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 TYT Geometri çıkmış soruları (yalnız mantık), MEB 9–10. sınıf geometri müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar',f'{onek}.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler))
bitir_geo('silindir')
