"""TYT Geometri · Dairede Çevre ve Alan (2. paket) · 10 şekilli soru (kardeş yok, ipucu 1). Şekiller hesaplanan koordinatlarla çizilir; her cevap ve çeldirici değer Python da assert edilir (π = 3 ya da π cinsinden simgesel)."""
import sys,os,math,json
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
from math import sin,cos,tan,radians,degrees,atan2,sqrt,pi
TIPK={}
def kartla(id,alt,fikir,tuzak,z,adim,tipId,tip,kalip='şekilli',kaynak=None):
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
    u=sub(a,V); v=sub(b,V); return degrees(math.acos(max(-1,min(1,(u[0]*v[0]+u[1]*v[1])/(ln(u)*ln(v))))))
def alan(ps): return abs(sum(ps[i][0]*ps[(i+1)%len(ps)][1]-ps[(i+1)%len(ps)][0]*ps[i][1] for i in range(len(ps))))/2
def pc(O,r,d): return (O[0]+r*cos(radians(d)),O[1]+r*sin(radians(d)))
def inter(p1,p2,p3,p4):
    x1,y1=p1;x2,y2=p2;x3,y3=p3;x4,y4=p4
    den=(x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
    a=x1*y2-y1*x2; b=x3*y4-y3*x4
    return ((a*(x3-x4)-(x1-x2)*b)/den,(a*(y3-y4)-(y1-y2)*b)/den)
class F:
    def __init__(s): s.o=[]
    def raw(s,t): s.o.append(t)
    def line(s,p,q_,st=''): s.o.append(f'\\draw[{st}] {pt(p)} -- {pt(q_)};')
    def poly(s,ps,st=''): s.o.append(f'\\draw[{st}] '+' -- '.join(map(pt,ps))+' -- cycle;')
    def fill(s,ps,st='fill=vurgu!25'): s.o.append(f'\\fill[{st}] '+' -- '.join(map(pt,ps))+' -- cycle;')
    def circ(s,c,r,st=''): s.o.append(f'\\draw[{st}] {pt(c)} circle ({r:.3f});')
    def dot(s,p): s.o.append(f'\\fill {pt(p)} circle (1.2pt);')
    def oarc(s,O,r,d1,d2,st=''):
        a=(d2-d1)%360
        s.o.append(f'\\draw[{st}] {pt(pc(O,r,d1))} arc[start angle={d1:.3f},delta angle={a:.3f},radius={r:.3f}];')
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
    def par(s,p,q_):
        m=mid(p,q_); e=un(sub(q_,p)); s.o.append(f'\\draw[-{{Stealth[length=1.9mm,width=1.7mm]}}] {pt(sub(m,mul(e,.07)))} -- {pt(add(m,mul(e,.07)))};')
    def body(s): return '\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'+'\n'.join(s.o)+'\n\\end{tikzpicture}'
    def svg(s): return tikz_svg(s.body())
def bitir_geo(onek,konuad):
    for qq in P.ANA: qq['kardes']=None
    P.yaz(os.path.join(GD,onek+'-1.json'),'/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/ciiki/bos-'+onek+'.json')
    tipler={}
    for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=TIPK[c['tipId']]))['kartlar'].append(c['id'])
    json.dump(dict(konu=konuad,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 TYT Geometri çıkmış soruları (yalnız mantık), MEB 9–10. sınıf geometri müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar',onek+'.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler))
P=Parti('daireiki','Dairede Çevre ve Alan','geo|Dairede Çevre ve Alan',ders='TYT Geometri',idon='tytgeo')
P.k='geo|Dairede Çevre ve Alan'; H.KONU='Dairede Çevre ve Alan'
def ok(a,b,t=1e-6): assert abs(a-b)<t,(a,b)
def V(x): return x[0]*pi+x[1]          # (p,c) = pπ + c
def S2(x):
    p,c=x
    if p==0: return str(c).replace('-','−')
    ps=('' if p==1 else str(p))+'π'
    if c==0: return ps
    return f'{c} + {ps}' if c>0 else f'{ps} − {-c}'
def sira(*xs): return [S2(x) for x in sorted(xs,key=V)]
def grid(inside,x0,x1,y0,y1,n=900):
    hx=(x1-x0)/n; hy=(y1-y0)/n; c=0
    for i in range(n):
        x=x0+(i+.5)*hx
        for j in range(n):
            if inside(x,y0+(j+.5)*hy): c+=1
    return c*hx*hy
DCA=B('Çember ve daire','yarıçapı r olan çemberin çevresi 2πr, dairenin alanı πr² dir (çap = 2r). Örnek: r = 5 için çevre 10π, alan 25π')
DIL=B('Daire dilimi','merkez açısı α olan dilimin yay uzunluğu 2πr × α/360, alanı πr² × α/360 dır; dilimin çevresi yay uzunluğu ile iki yarıçapın toplamıdır. Örnek: r = 9 ve α = 40° ise yay uzunluğu 2π × 9 × 40/360 = 2π dir')
YAR=B('Yarım daire','çapı d olan yarım dairenin alanı πd²/8, yayının uzunluğu πd/2 dir. Örnek: d = 10 için alan 25π/2, yay uzunluğu 5π')
TAR=B('Taralı alan','taralı bölgenin alanı, bildiğin şekillerin (kare, üçgen, daire, dilim) alanlarını toplayıp çıkararak bulunur. Örnek: kenarı 4 olan karenin içindeki yarıçapı 2 olan dairenin dışında kalan alan 16 − 4π dir')
KAY=B('Kuşak ve bant uzunluğu','çemberlere teğet düz parçalar ve çember yayları birleştirilerek oluşan kapalı çizginin uzunluğu, parçaların uzunlukları toplanarak bulunur. Örnek: yarıçapı 3 olan tek bir çemberin çevresi 6π dir')
KUD=B('Kare ve çember','bir karenin içine ya da dışına çizilen çemberlerin yarıçapları, karenin kenarı ve köşegeniyle ilişkilidir; halkanın alanı iki dairenin alanının farkıdır. Örnek: yarıçapı 4 ve 3 olan eş merkezli çemberler arasındaki halkanın alanı 7π dir')
PI3='π yerine 3 alınız.'
GEN1='Şekildeki bölgeyi alanı ya da uzunluğu bildiğin parçalara ayırmayı dene.'
GENP='Şekildeki bölgeyi bildiğin parçalara ayır; her parçanın ölçüsünü ayrı hesapla, sonra toplayıp çıkararak birleştir.'

# ===== 01 · pist çevresi · kolay, hikâyeli =====
kartla('K-GDV-01','Birleşik şeklin çevresi','Dikdörtgen ve yarım dairelerden oluşan kapalı bir şeklin çevresi, düz kenarların ve yay uzunluklarının toplamıdır.','Birleştirme yerlerini de çevreye katmak; yarım dairenin yayı yerine tam çevresini yazmak; çapı yarıçap sanmak.','kolay',3,'ge-di-birlesik','Birleşik şeklin çevresi ve alanı','hikâyeli')
L1,W1=36,14; assert 2*L1+3*W1==114 and 2*L1==72 and 72+3*W1//2==93 and 2*L1+2*W1==100 and 3*W1==42
s=.1; l=L1*s; w=W1*s; h=w/2
f=F(); f.raw(f'\\draw (0,0) -- ({l},0) arc[start angle=-90,end angle=90,radius={h}] -- (0,{w}) arc[start angle=90,end angle=270,radius={h}] -- cycle;')
f.raw(f'\\draw[<->] (0,{w+.45}) -- ({l},{w+.45}); \\draw[dashed,thin] (0,{w}) -- (0,{w+.55}); \\draw[dashed,thin] ({l},{w}) -- ({l},{w+.55});')
f.node((l/2,w+.75),'$36\\ \\mathrm{m}$')
f.raw(f'\\draw[dashed,thin] (0,0) -- (0,{w}); \\draw[<->] (.0,.06) -- (0,{w-.06});') 
f.node((.55,h),'$14\\ \\mathrm{m}$')
SK1=f.svg()
q('0001',tipId='ge-di-birlesik',tip='Birleşik şeklin çevresi ve alanı',z='kolay',alt='Pist Çevresi',kaz='Dikdörtgen ve iki yarım daireden oluşan şeklin çevresini hesaplar.',kalip='hikâyeli',
 kart='K-GDV-01 (pist çevresi) · 36 m, 14 m',
 metin='Şekilde, bir dikdörtgen ile onun iki kısa kenarına çizilmiş iki yarım daireden oluşan bir koşu pistinin ölçüleri verilmiştir. Bir sporcu, pistin dış çizgisi boyunca bir tam tur koşmuştur. '+PI3+'\nBuna göre, sporcunun koştuğu yol kaç m dir?',
 dogru=114,yan=[(42,'Yalnız yayların uzunluğunu (3 × 14) yazmış; düz kenarları katmamış.','dikkat'),(72,'Yalnız iki düz kenarı (2 × 36) toplamış; yayları katmamış.','dikkat'),(93,'Yalnız bir yarım dairenin yayını (3 × 14 ÷ 2 = 21) eklemiş.','dikkat'),(100,'Dikdörtgenin çevresini (2 × 36 + 2 × 14) yazmış; yaylar yerine kısa kenarları almış.','bilgi')],
 istenen='Sporcunun koştuğu yol (m).',
 ip=['Sınırı oluşturan çizgileri tek tek say.'],
 bilgi=[DCA,YAR],
 ad=[A('Düz kısımları bul','Pistin iki düz kenarı 36 m dir.','2 × 36 = 72'),A('Yayları bul','İki yarım daire birleşince çapı 14 olan bir çember eder.','3 × 14 = 42'),A('Toplamı yaz','Düz kısımlar ile yaylar toplanır.','72 + 42 = 114')],
 puf='Her çizginin uzunluğunu ayrı hesapla.',sekil=SK1)

# ===== 02 · yarım dairenin çevresi · kolay, hikâyeli =====
kartla('K-GDV-02','Yarım dairenin çevresi','Yarım dairenin çevresi, yayı ile çapının toplamıdır.','Yalnız yayı ya da yalnız çapı yazmak; yarım yay yerine tam çemberi almak.','kolay',3,'ge-di-dilim','Dilim: yay, açı, alan','hikâyeli')
d2=8; assert d2==8 and V((4,8))>V((4,4))
s=.3; R2_=d2*s/2
f=F(); f.raw(f'\\draw (0,0) -- ({2*R2_},0) arc[start angle=0,end angle=180,radius={R2_}] -- cycle;')
f.raw(f'\\draw[<->] (0,-.4) -- ({2*R2_},-.4);'); f.node((R2_,-.7),'$8\\ \\mathrm{cm}$')
SK2=f.svg()
q('0002',tipId='ge-di-dilim',tip='Dilim: yay, açı, alan',z='kolay',alt='Yarım Dairenin Çevresi',kaz='Yarım daire biçimli bir şeklin çevresini π cinsinden bulur.',kalip='hikâyeli',
 kart='K-GDV-02 (yarım daire çevresi) · çap 8',
 metin='Bir terzi, çapı şekilde verilen yarım daire biçimli bir kumaş parçasının bütün kenarına şerit biye dikecektir. Şerit, kumaşın kenarını hiç boşluk ve bindirme bırakmadan tamamen çevreleyecektir. Sonuç π cinsinden yazılacaktır.\nBuna göre, gereken şerit kaç cm dir?',
 dogru='8 + 4π',sira=sira((0,8),(4,0),(4,4),(4,8),(8,8)),
 yan=[('8','Yalnız çapın uzunluğunu yazmış.','dikkat'),('4π','Yalnız yayın uzunluğunu yazmış.','dikkat'),('4 + 4π','Çap yerine yarıçapı (4) eklemiş.','bilgi'),('8 + 8π','Yarım yay yerine tam çemberin uzunluğunu (π × 8) almış.','dikkat')],
 istenen='Gereken şeridin uzunluğu (cm, π cinsinden).',
 ip=['Kumaşın kenarını oluşturan çizgileri tek tek say.'],
 bilgi=[YAR,DCA],
 ad=[A('Yayın uzunluğunu bul','Çap 8 olduğundan yarıçap 4 tür; yarım çemberin uzunluğu π × r dir.','π × 4 = 4π'),A('Çapı ekle','Kapalı kenara düz kısım da girer.','8'),A('Toplamı yaz','Yay ile çap toplanır.','8 + 4π')],
 puf='Çevre sorularında sınırdaki her çizgiyi bir kez hesaba kat.',sekil=SK2)

# ===== 03 · yay uzunluğundan alan · orta =====
kartla('K-GDV-03','Yay uzunluğundan dilim alanı','Yay uzunluğu ve yarıçap verilen dilimde merkez açı bulunur; açı ile dilimin alanı hesaplanır.','Yay uzunluğunu alan sanmak; açı oranını 180 ile kurmak; tam çemberin uzunluğunu ya da tam dairenin alanını yazmak.','orta',3,'ge-di-dilim','Dilim: yay, açı, alan')
r3,yay3=12,(5,0); al3=75; assert 2*r3*al3/360==5 and r3**2*al3/360==30 and 5*r3/2==30
assert 24*(75/180)==10 and 2*r3==24
s=.2; R3=r3*s; a1,a2_=-37.5,37.5; P1=pc((0,0),R3,a1); P2=pc((0,0),R3,a2_)
f=F(); f.line((0,0),P1); f.line((0,0),P2); f.oarc((0,0),R3,a1,a2_); f.dot((0,0))
f.arc((0,0),P1,P2,.7,'$\\alpha$',1.1); f.sl('$12$',(0,0),P1,P2,.3); f.node(pc((0,0),R3+.6,0),'$5\\pi\\ \\mathrm{cm}$'); f.node((-.25,0),'$O$')
SK3=f.svg()
q('0003',tipId='ge-di-dilim',tip='Dilim: yay, açı, alan',z='orta',alt='Yay Uzunluğundan Alan',kaz='Yay uzunluğu ve yarıçapı verilen daire diliminin alanını π cinsinden bulur.',
 kart='K-GDV-03 (yay → alan) · r = 12, yay 5π',
 metin='Şekilde O merkezli bir daire diliminin yarıçapı (cm cinsinden) ile yayının uzunluğu verilmiştir. Merkez açının ölçüsü α ile gösterilmiştir. Şekil ölçekli değildir. Sonuç π cinsinden yazılacaktır.\nBuna göre, dilimin alanı kaç cm² dir?',
 dogru='30π',sira=sira((5,0),(15,0),(24,0),(30,0),(60,0)),
 yan=[('5π','Yay uzunluğunu alan sanmış.','dikkat'),('15π','Açı oranını 180 ile kurup α = 37,5° bulmuş.','bilgi'),('24π','Tam çemberin uzunluğunu (2π × 12) yazmış.','dikkat'),('60π','Alanı yay × yarıçap olarak almış; 2 ye bölmeyi unutmuş.','islem')],
 istenen='Dilimin alanı (cm², π cinsinden).',
 ip=['Yay uzunluğu hangi büyüklükleri birbirine bağlıyor?'],
 bilgi=[DIL,DCA],
 ad=[A('Merkez açıyı bul','Yay uzunluğu 2π × 12 × α/360 dır.','24π × α/360 = 5π → α = 75°'),A('Alan formülünü yaz','Dilimin alanı, tam dairenin α/360 ıdır.','π × 12² × 75/360'),A('Hesapla','Sadeleştirilir.','144π × 5/24 = 30π')],
 puf='Dilimin hangi büyüklüklerini bildiğini yaz.',sekil=SK3)

# ===== 04 · çeyrek daire eksi üçgen · orta =====
kartla('K-GDV-04','Daire kesmesi','Bir yay ile kirişin sınırladığı bölgenin alanı, dilimin alanı ile üçgenin alanının farkıdır.','Yalnız dilimi ya da yalnız üçgeni yazmak; farkı almak yerine toplamak; yarıçap yerine çap almak.','orta',3,'ge-di-taral','Taralı alanlar')
r4=10; assert r4*r4//2==50 and (25,-50)==(r4*r4//4,-(r4*r4)//2)
s=.25; R4=r4*s
f=F(); f.raw(f'\\fill[fill=vurgu!25] ({R4},0) arc[start angle=0,end angle=90,radius={R4}] -- cycle;')
f.line((0,0),(R4,0)); f.line((0,0),(0,R4)); f.line((R4,0),(0,R4)); f.oarc((0,0),R4,0,90); f.dik((0,0),(R4,0),(0,R4),.22)
f.node((R4/2,-.28),'$10$'); f.node((-.3,R4/2),'$10$'); f.node((-.2,-.2),'$O$'); f.vl('A',(R4,0),(1,-.4),.3); f.vl('B',(0,R4),(-.4,1),.3)
SK4=f.svg()
q('0004',tipId='ge-di-taral',tip='Taralı alanlar',z='orta',alt='Daire Kesmesi',kaz='Çeyrek daire ile üçgenin alan farkından taralı bölgenin alanını π cinsinden bulur.',
 kart='K-GDV-04 (kesme) · r = 10',
 metin='Şekilde O merkezli, yarıçapı 10 cm olan bir çeyrek daire ile uç noktaları A ve B olan [AB] doğru parçası çizilmiştir. Çeyrek daire yayı ile [AB] arasında kalan bölge taranmıştır. Sonuç π cinsinden yazılacaktır.\nBuna göre, taralı bölgenin alanı kaç cm² dir?',
 dogru='25π − 50',sira=sira((25,-50),(0,50),(25,0),(50,-50),(25,50)),
 yan=[('50','Yalnız OAB üçgeninin alanını yazmış.','dikkat'),('25π','Yalnız çeyrek dairenin alanını yazmış.','dikkat'),('50π − 50','Çeyrek daire yerine yarım dairenin alanını kullanmış.','bilgi'),('50 + 25π','Üçgenin alanını çıkarmak yerine eklemiş.','islem')],
 istenen='Taralı bölgenin alanı (cm², π cinsinden).',
 ip=['Taralı bölgenin sınırını hangi iki çizgi oluşturuyor?'],
 bilgi=[DIL,TAR],
 ad=[A('Çeyrek dairenin alanı','90° lik dilim, tam dairenin dörtte biridir.','π × 10² ÷ 4 = 25π'),A('Üçgenin alanını bul','O köşesindeki açı diktir; dik kenarlar 10 cm dir.','10 × 10 ÷ 2 = 50'),A('Farkı al','Taralı bölge, çeyrek daireden üçgenin çıkarılmasıyla kalır.','25π − 50')],
 puf='Önce bildiğin şekillerin ölçülerini bul.',sekil=SK4)

# ===== 05 · bant uzunluğu · orta, hikâyeli =====
kartla('K-GDV-05','Boruları saran bant','Özdeş çemberleri saran kapalı çizgi, çemberlere teğet düz parçalar ile yaylardan oluşur; düz parçalar çapa, yaylar çembere bağlıdır.','Düz parçaları yalnız bir çap uzunluğunda saymak; yayları unutmak; üç çemberin çevresini toplamak.','orta',3,'ge-di-bant','Çemberleri saran bant','hikâyeli')
r5=5; assert 8*r5==40 and 2*3*r5==30 and 8*r5+30==70 and 6*r5+30==60 and 4*r5+30==50 and 3*2*3*r5==90
s=.18; R5=r5*s; cs=[(R5+2*R5*i,0) for i in range(3)]
f=F()
for c in cs: f.circ(c,R5,'thin')
xl=cs[0][0]; xr=cs[2][0]
f.raw(f'\\draw[very thick,vurgu] ({xl},{R5}) -- ({xr},{R5}) arc[start angle=90,end angle=-90,radius={R5}] -- ({xl},{-R5}) arc[start angle=270,end angle=90,radius={R5}];')
for c in cs: f.dot(c)
rp_=pc(cs[1],R5,50); f.line(cs[1],rp_); f.node(pc(cs[1],.42,105),'$5$')
SK5=f.svg()
q('0005',tipId='ge-di-bant',tip='Çemberleri saran bant',z='orta',alt='Boru Bandı',kaz='Yan yana dizilmiş özdeş çemberleri saran bandın uzunluğunu hesaplar.',kalip='hikâyeli',
 kart='K-GDV-05 (borular, bant) · r = 5',
 metin='Yarıçapı şekilde cm cinsinden verilen üç özdeş boru, düz bir hat üzerinde birbirine teğet olacak biçimde yan yana dizilmiştir. Boruların çevresine kalın çizgiyle gösterilen bant, hiç bindirme yapılmadan sıkıca sarılmıştır. '+PI3+'\nBuna göre, bandın uzunluğu kaç cm dir?',
 dogru=70,yan=[(30,'Yalnız yayları (uçtaki iki yarım çember = bir tam çember, 3 × 10) yazmış; düz parçaları katmamış.','dikkat'),(40,'Yalnız düz parçaları (8r) yazmış; yayları katmamış.','dikkat'),(50,'Düz parçalardan yalnız üstteki 4r = 20 yi alıp 20 + 30 yazmış.','islem'),(60,'Düz parçaları 6r almış; borular üçgen biçiminde dizilmiş gibi düşünmüş.','bilgi')],
 sira=[30,40,50,60,70],
 istenen='Bandın uzunluğu (cm).',
 ip=['Bandın hangi parçalardan oluştuğunu ayır.'],
 bilgi=[KAY,DCA],
 ad=[A('Düz parçaları bul','Alttaki ve üstteki düz parçaların her biri, en soldaki ve en sağdaki merkezlerin arasındaki uzaklığa eşittir (4 yarıçap).','2 × 4 × 5 = 40'),A('Yayları bul','Soldaki ve sağdaki yarım çemberlerin toplamı bir tam çember eder.','2 × 3 × 5 = 30'),A('Toplamı yaz','Düz parçalar ve yaylar toplanır.','40 + 30 = 70')],
 puf='Düz ve yay parçalarını ayrı ayrı say.',sekil=SK5)

# ===== 06 · halka dilimi · orta, hikâyeli =====
kartla('K-GDV-06','Halka dilimi','Eş merkezli iki dilimin farkı olan bölgenin alanı, iki yarıçap ve merkez açıdan bulunur.','Halkanın tamamının alanını yazmak; yalnız dış ya da iç dilimi almak; yarıçapların farkının karesini kullanmak.','orta',3,'ge-di-dilim','Dilim: yay, açı, alan','hikâyeli')
ri,wd,al6=6,3,120; Ro=ri+wd; assert (Ro**2-ri**2)*al6//360==15 and 3*45==135 and Ro**2*al6//360==27 and ri**2*al6//360==12 and wd**2*al6//360==3 and Ro**2-ri**2==45
s=.22; Ri=ri*s; Rop=Ro*s; a1,a2_=30,150; PA=pc((0,0),Rop,a2_); PB=pc((0,0),Ri,a2_)
f=F(); f.raw(f'\\path[fill=vurgu!25] {pt(pc((0,0),Ri,a1))} arc[start angle={a1},end angle={a2_},radius={Ri}] -- {pt(pc((0,0),Rop,a2_))} arc[start angle={a2_},end angle={a1},radius={Rop}] -- cycle;')
f.line((0,0),pc((0,0),Rop,a1)); f.line((0,0),pc((0,0),Rop,a2_)); f.oarc((0,0),Ri,a1,a2_); f.oarc((0,0),Rop,a1,a2_); f.dot((0,0)); f.node((.3,-.12),'$O$')
f.arc((0,0),pc((0,0),1,a1),pc((0,0),1,a2_),.45,'$120^\\circ$',.8)
nv=(cos(radians(a2_+90)),sin(radians(a2_+90)))
off=mul(nv,.3)
f.raw(f'\\draw[<->] {pt(add((0,0),off))} -- {pt(add(PB,off))}; \\draw[<->] {pt(add(PB,off))} -- {pt(add(PA,off))};')
f.node(add(mul(PB,.5),mul(nv,.62)),'$6$'); f.node(add(mul(add(PB,PA),.5),mul(nv,.62)),'$3$')
SK6=f.svg()
q('0006',tipId='ge-di-dilim',tip='Dilim: yay, açı, alan',z='orta',alt='Halka Dilimi',kaz='Eş merkezli iki yay ve iki yarıçapın sınırladığı halka diliminin alanını π cinsinden bulur.',kalip='hikâyeli',
 kart='K-GDV-06 (halka dilimi) · 6 + 3, 120°',
 metin='Bir amfi tiyatronun oturma bölümü, merkezi O olan iki yay ile iki doğru parçasının sınırladığı taralı bölgedir. Sahnenin merkezi O dan oturma bölümünün başlangıcına kadar olan uzaklık ile bölümün derinliği (m cinsinden) ve yan kenarlar arasındaki açı şekilde verilmiştir. Sonuç π cinsinden yazılacaktır.\nBuna göre, oturma bölümünün alanı kaç m² dir?',
 dogru='15π',sira=sira((3,0),(12,0),(15,0),(27,0),(45,0)),
 yan=[('3π','Derinliğin (3) karesini alıp dilim oranıyla çarpmış: π × 3² × 1/3.','bilgi'),('12π','Yalnız iç dilimin alanını (π × 6² × 1/3) yazmış.','dikkat'),('27π','Yalnız dış dilimin alanını (π × 9² × 1/3) yazmış.','dikkat'),('45π','Halkanın tamamının alanını yazmış; 120° lik dilim oranını uygulamamış.','dikkat')],
 istenen='Oturma bölümünün alanı (m², π cinsinden).',
 ip=['Taralı bölgenin sınırını oluşturan iki yarıçap ve onları ayıran uzaklık nedir?'],
 bilgi=[DIL],
 ad=[A('Büyük yarıçapı bul','Dış yayın yarıçapı, iç yarıçap ile derinliğin toplamıdır.','R = 6 + 3 = 9'),A('Halkanın alanı','Dış ve iç dairelerin alanlarının farkı alınır.','π × 9² − π × 6² = 45π'),A('Dilim oranını uygula','120° lik bölüm, tam halkanın 120/360 = 1/3 üdür.','45π ÷ 3 = 15π')],
 puf='Halkayı iki yarıçapla düşün; dilim oranını sonda uygula.',sekil=SK6)

# ===== 07 · arbelos · orta =====
kartla('K-GDV-07','Yarım daireler arası bölge','Çapı bir doğru parçası üzerinde bölünmüş yarım dairelerde taralı bölge, büyük yarım daireden küçük yarım dairelerin çıkarılmasıyla bulunur.','Yalnız bir küçük yarım daireyi çıkarmak; küçük yarım daireleri eklemek; çapı yarıçap sanmak.','orta',4,'ge-di-taral','Taralı alanlar')
AC,CB=16,8; AB=AC+CB; big=(AB//2)**2/2; sm=((AC//2)**2+(CB//2)**2)/2; assert big==72 and sm==40 and big-sm==32 and 72-32==40 and 72-8==64 and 72+40==112
s=.12; xa=0; xc=AC*s; xb=AB*s
f=F(); f.raw(f'\\path[fill=vurgu!25,even odd rule] (0,0) arc[start angle=180,end angle=0,radius={AB*s/2}] -- cycle ({xc},0) arc[start angle=0,end angle=180,radius={AC*s/2}] -- cycle ({xb},0) arc[start angle=0,end angle=180,radius={CB*s/2}] -- cycle;')
f.raw(f'\\draw (0,0) -- ({xb},0); \\draw (0,0) arc[start angle=180,end angle=0,radius={AB*s/2}]; \\draw ({xc},0) arc[start angle=0,end angle=180,radius={AC*s/2}]; \\draw ({xb},0) arc[start angle=0,end angle=180,radius={CB*s/2}];')
f.raw(f'\\draw[<->] (0,-.62) -- ({xc},-.62); \\draw[<->] ({xc},-.62) -- ({xb},-.62);'); f.node((xc/2,-.95),'$16$'); f.node(((xc+xb)/2,-.95),'$8$')
f.node((0,-.28),'$A$'); f.node((xc,-.28),'$C$'); f.node((xb,-.28),'$B$')
SK7=f.svg()
q('0007',tipId='ge-di-taral',tip='Taralı alanlar',z='orta',alt='Yarım Daireler',kaz='Çapı bölünmüş yarım dairelerde taralı bölgenin alanını π cinsinden bulur.',
 kart='K-GDV-07 (yarım daireler) · 16 ve 8',
 metin='Şekilde, C noktası [AB] üzerinde olmak üzere AB, AC ve CB çaplı üç yarım daire aynı tarafa çizilmiştir. |AC| ve |CB| uzunlukları (cm cinsinden) şekilde verilmiştir. Taralı bölge, AB çaplı yarım dairenin içinde olup diğer iki yarım dairenin dışında kalan bölgedir. Sonuç π cinsinden yazılacaktır.\nBuna göre, taralı bölgenin alanı kaç cm² dir?',
 dogru='32π',sira=sira((32,0),(40,0),(64,0),(72,0),(112,0)),
 yan=[('40π','İki küçük yarım dairenin alanları toplamını (32π + 8π) cevap yazmış.','dikkat'),('64π','Yalnız küçük olan yarım daireyi (8π) çıkarmış: 72π − 8π.','dikkat'),('72π','Yalnız büyük yarım dairenin alanını yazmış.','dikkat'),('112π','Büyük yarım daireye küçük yarım daireleri eklemiş.','islem')],
 istenen='Taralı bölgenin alanı (cm², π cinsinden).',
 ip=['Taralı bölgenin sınırındaki üç yarım daireyi ayrı ayrı düşün.'],
 bilgi=[YAR,TAR],
 ad=[A('Büyük yarım daireyi bul','AB = 16 + 8 = 24 cm olduğundan yarıçap 12 dir.','π × 12² ÷ 2 = 72π'),A('Küçük yarım daireleri bul','Yarıçaplar 8 ve 4 tür.','π × 8² ÷ 2 = 32π · π × 4² ÷ 2 = 8π'),A('Farkı al','Taralı bölge = büyük yarım daire − iki küçük yarım daire.','72π − 32π − 8π = 32π')],
 puf='Yarım dairelerin çaplarını şekilden oku.',sekil=SK7)

# ===== 08 · Hipokrat ayçıkları · zor =====
kartla('K-GDV-08','Kenarlar üzerinde yarım daireler','Dik üçgenin kenarları üzerine çizilen yarım daireler arasındaki bölgelerin alanı, yarım dairelerin alanlarını ve üçgenin alanını birleştirerek bulunur.','Yarım dairelerin alanlarını π = 3 ile hesaplamaya çalışmak; hipotenüs üzerindeki yarım daireyi katmamak; üçgenin alanında 2 ye bölmeyi unutmak.','zor',4,'ge-di-taral','Taralı alanlar')
a8,b8=9,12; c8=15; assert a8*a8+b8*b8==c8*c8
Ls=a8*b8/2; assert Ls==54 and a8*b8==108 and Ls/2==27 and a8+b8+c8==36 and c8*b8/2==90
s=.2; Aa=(0,0); Bb=(a8*s,0); Cc=(0,b8*s); M=((a8*s)/2,(b8*s)/2); Rh=c8*s/2
sx=(a8*s)/2; sy=(b8*s)/2
def inside(x,y):
    in1=((x-sx)**2+y**2<=sx**2 and y<=0); in2=(x**2+(y-sy)**2<=sy**2 and x<=0)
    outh=((x-M[0])**2+(y-M[1])**2>Rh**2)
    return (in1 or in2) and outh
ar=grid(inside,-sy-.01,Bb[0]+.01,-sx-.01,Cc[1]+.01,700)/s/s
assert abs(ar-54)<.5,ar
f=F()
f.raw(f'\\begin{{scope}}\\clip ({sx},0) circle ({sx}); \\clip (-5,-5) rectangle (6,0); \\fill[even odd rule,fill=vurgu!25] (-5,-5) rectangle (6,6) {pt(M)} circle ({Rh:.4f}); \\end{{scope}}')
f.raw(f'\\begin{{scope}}\\clip (0,{sy}) circle ({sy}); \\clip (-5,-5) rectangle (0,6); \\fill[even odd rule,fill=vurgu!25] (-5,-5) rectangle (6,6) {pt(M)} circle ({Rh:.4f}); \\end{{scope}}')
f.poly([Aa,Bb,Cc])
f.oarc((sx,0),sx,180,360); f.oarc((0,sy),sy,90,270)
d0=degrees(atan2(Cc[1]-M[1],Cc[0]-M[0])); d1=degrees(atan2(Bb[1]-M[1],Bb[0]-M[0]))
f.oarc(M,Rh,d0,d1+360)
f.dik(Aa,Bb,Cc,.2)
f.node((a8*s/2,.28),'$9$'); f.node((.3,b8*s/2),'$12$')
f.vl('A',Aa,(-1,-1),.28); f.vl('B',Bb,(1,-.5),.3); f.vl('C',Cc,(.5,1),.3)
SK8=f.svg()
q('0008',tipId='ge-di-taral',tip='Taralı alanlar',z='zor',alt='Yarım Daireli Dik Üçgen',kaz='Dik üçgenin kenarları üzerindeki yarım daireler arasında kalan bölgelerin alanını bulur.',
 kart='K-GDV-08 (dik üçgen, yarım daireler) · 9 ve 12',
 metin='Şekilde A köşesinde dik açı bulunan ABC üçgeninin dik kenarlarının uzunlukları (cm cinsinden) verilmiştir. Dik kenarlar üzerine, üçgenin dışına doğru birer yarım daire; [BC] çaplı bir yarım daire de A köşesinden geçecek biçimde çizilmiştir. Taralı bölgeler, dik kenarlar üzerindeki yarım dairelerin [BC] çaplı yarım dairenin dışında kalan kısımlarıdır. Şekil ölçekli değildir.\nBuna göre, taralı bölgelerin alanları toplamı kaç cm² dir?',
 dogru=54,yan=[(27,'Üçgenin alanını bulurken 2 ye bir kez daha bölmüş.','islem'),(36,'Alan yerine üçgenin çevresini (9 + 12 + 15) yazmış.','dikkat'),(90,'Üçgenin alanını hipotenüs ile bir dik kenarın çarpımının yarısı (15 × 12 ÷ 2) almış.','bilgi'),(108,'Dik kenarların çarpımını (9 × 12) alan sanmış; 2 ye bölmeyi unutmuş.','islem')],
 istenen='Taralı bölgelerin alanları toplamı (cm²).',
 ip=['Taralı alanı doğrudan hesaplayamıyorsan, hangi şekillerin alanlarını toplayıp çıkarırsın?'],
 bilgi=[YAR,TAR],
 ad=[A('Hipotenüsü bul','Dik üçgende Pisagor bağıntısı kullanılır.','|BC|² = 9² + 12² = 225 → |BC| = 15'),A('Yarım daireleri karşılaştır','Dik kenarlar üzerindeki yarım dairelerin alanları toplamı, çapları 9 ve 12 olduğundan π(81 + 144)/8 dir; [BC] çaplı yarım daire de π · 225/8 dir. İkisi eşittir.','π(9² + 12²)/8 = π · 15²/8'),A('Taralı alanı yaz','Taralı bölgeler = iki küçük yarım daire + üçgen − [BC] çaplı yarım daire.','taralı = üçgenin alanı'),A('Hesapla','Üçgenin alanı dik kenarların çarpımının yarısıdır.','9 × 12 ÷ 2 = 54')],
 puf='Hangi şekillerin alanları taralı bölgeyle ilişkili, bak.',sekil=SK8)

# ===== 09 · içe doğru dört yarım daire · zor =====
kartla('K-GDV-09','Kare içindeki yarım daireler','Karenin kenarları üzerinde içe doğru çizilen yarım daireler karenin tamamını örter ve üst üste biner; üst üste binen bölgenin alanı toplam alandan kare çıkarılarak bulunur.','Yarım daireleri tam daire saymak; üst üste binen bölgeyi karenin alanı sanmak; yalnız iki yarım daireyi almak.','zor',3,'ge-di-yaprak','Kare içinde yarım daireler')
a9=12; r9=a9//2; yap=(72,-144); assert 4*(r9**2)==a9**2 and 2*r9**2==72 and V(yap)>0 and 4*r9**2==144
# sayısal doğrulama: iki yarım dairenin üst üste bindiği bölge (komşu çiftler) ~ 72π − 144
def cov(x,y):
    c=0
    for (cx,cy) in [(a9/2,0),(0,a9/2),(a9,a9/2),(a9/2,a9)]:
        if (x-cx)**2+(y-cy)**2<=r9*r9: c+=1
    return c
n=700; hx=a9/n; tot=0
for i in range(n):
    x=(i+.5)*hx
    for j in range(n):
        if cov(x,(j+.5)*hx)>=2: tot+=1
assert abs(tot*hx*hx-(72*pi-144))<.5,tot*hx*hx
s=.28; L9=a9*s; h9=L9/2
f=F()
cs9=dict(b=(h9,0),l=(0,h9),r=(L9,h9),t=(h9,L9))
for u,v in [('b','l'),('b','r'),('t','l'),('t','r')]:
    f.raw(f'\\begin{{scope}}\\clip {pt(cs9[u])} circle ({h9:.4f}); \\clip (0,0) rectangle ({L9:.4f},{L9:.4f}); \\fill[fill=vurgu!25] {pt(cs9[v])} circle ({h9:.4f}); \\end{{scope}}')
f.raw(f'\\draw (0,0) rectangle ({L9},{L9});')
f.raw(f'\\draw (0,0) arc[start angle=180,end angle=0,radius={h9}]; \\draw (0,{L9}) arc[start angle=90,end angle=-90,radius={h9}]; \\draw ({L9},0) arc[start angle=-90,end angle=-270,radius={h9}]; \\draw ({L9},{L9}) arc[start angle=0,end angle=-180,radius={h9}];')
f.raw(f'\\draw[<->] (0,-.4) -- ({L9},-.4);'); f.node((h9,-.7),'$12\\ \\mathrm{cm}$')
SK9=f.svg()
q('0009',tipId='ge-di-yaprak',tip='Kare içinde yarım daireler',z='zor',alt='İçe Doğru Yarım Daireler',kaz='Kare içine çizilen yarım dairelerin üst üste bindiği bölgenin alanını π cinsinden bulur.',
 kart='K-GDV-09 (kare, dört yarım daire) · kenar 12',
 metin='Şekilde kenar uzunluğu verilen bir karenin her kenarı çap kabul edilerek karenin içine doğru dört yarım daire çizilmiştir. Taralı bölgeler, komşu iki yarım dairenin ortak olarak örttüğü bölgelerdir. Sonuç π cinsinden yazılacaktır.\nBuna göre, taralı bölgelerin alanları toplamı kaç cm² dir?',
 dogru='72π − 144',sira=sira((72,-144),(36,-72),(0,144),(72,0),(36,0)),
 yan=[('36π − 72','Dört bölge yerine yalnız ikisinin alanını (36π − 72) yazmış.','dikkat'),('144','Karenin alanını yazmış.','dikkat'),('72π','Dört yarım dairenin alanları toplamını cevap yazmış; karenin alanını çıkarmamış.','dikkat'),('36π','İki yarım dairenin alanı toplamını yazmış.','dikkat')],
 istenen='Taralı bölgelerin alanları toplamı (cm², π cinsinden).',
 ip=['Taralı bölgelerin hangi yarım dairelerin ortak kısmı olduğuna bak.'],
 bilgi=[YAR,TAR],
 ad=[A('Yarıçapı bul','Her yarım daire karenin bir kenarını çap alır.','r = 12 ÷ 2 = 6'),A('Dört yarım dairenin toplamı','Her birinin alanı π × 6² ÷ 2 = 18π dir.','4 × 18π = 72π'),A('Örtülmeyi yorumla','Yarım daireler kareyi tam kaplar; taralı bölgeler iki kez örtülür. Toplam alan, karenin alanı ile bu bölgelerin alanlarının toplamıdır.','72π = 12² + taralı'),A('Taralı alanı bul','Eşitlikten taralı alan çekilir.','72π − 144')],
 puf='Her alanı ayrı hesaplayıp ilişkiyi yaz.',sekil=SK9)

# ===== 10 · kare, iç ve dış çember · zor =====
kartla('K-GDV-10','Karenin iç ve dış çemberi','Kare ile çemberler arasındaki uzunluk ilişkilerinden yarıçaplar bulunur; halkanın alanı iki dairenin alan farkıdır.','Dış çemberin yarıçapını kenara eşit almak; yalnız dış daireyi yazmak; iç daire yerine kareyi çıkarmak.','orta',4,'ge-di-kuad','Kare ve çember')
a10=6; Ri_=a10/2; R2=a10*a10/2; assert Ri_**2==9 and R2==18 and R2-Ri_**2==9 and 36-9==27 and 2*R2-a10*a10==0
s=.45; L10=a10*s; ctr=(L10/2,L10/2); Rin=L10/2; Rout=L10/sqrt(2)
ok(dist((0,0),ctr),Rout)
f=F(); f.raw(f'\\path[fill=vurgu!25,even odd rule] {pt(ctr)} circle ({Rout:.4f}) {pt(ctr)} circle ({Rin:.4f});')
f.raw(f'\\draw {pt(ctr)} circle ({Rout:.4f}); \\draw {pt(ctr)} circle ({Rin:.4f}); \\draw (0,0) rectangle ({L10},{L10});')
f.raw(f'\\draw[<->] (0,{-Rout+ctr[1]-.45}) -- ({L10},{-Rout+ctr[1]-.45});') if False else None
f.node((L10/2,-.0),'') if False else None
f.vl('A',(0,0),(-1,-1),.3); f.vl('B',(L10,0),(1,-1),.3); f.vl('C',(L10,L10),(1,1),.3); f.vl('D',(0,L10),(-1,1),.3)
yb=ctr[1]-Rout-.35
f.raw(f'\\draw[dashed,thin] (0,0) -- (0,{yb-.1}); \\draw[dashed,thin] ({L10},0) -- ({L10},{yb-.1}); \\draw[<->] (0,{yb}) -- ({L10},{yb});'); f.node((L10/2,yb-.3),'$6\\ \\mathrm{cm}$')
SK10=f.svg()
q('0010',tipId='ge-di-kuad',tip='Kare ve çember',z='orta',alt='Kare ve İki Çember',kaz='Karenin köşelerinden geçen ve kenarlarına teğet çemberler arasındaki halkanın alanını π cinsinden bulur.',
 kart='K-GDV-10 (kare, iki çember) · kenar 6',
 metin='Şekilde kenar uzunluğu verilen ABCD karesi, köşelerinden geçen bir çember ile dört kenarına da teğet olan başka bir çemberin arasında yer almaktadır. İki çemberin arasında kalan taralı bölgenin alanı soruluyor. Sonuç π cinsinden yazılacaktır.\nBuna göre, taralı bölgenin alanı kaç cm² dir?',
 dogru='9π',sira=sira((18,-36),(9,0),(18,0),(27,0),(36,0)),
 yan=[('18π − 36','İç daire yerine karenin alanını çıkarmış: 18π − 36.','bilgi'),('18π','Yalnız dış dairenin alanını yazmış.','dikkat'),('27π','Dış çemberin yarıçapını kenara (6) eşit alıp π(36 − 9) bulmuş.','bilgi'),('36π','Yalnız dış çemberin alanını, yarıçapı kenara eşit alarak (π × 6²) yazmış.','bilgi')],
 istenen='Taralı bölgenin alanı (cm², π cinsinden).',
 ip=['Kare ile çemberlerin yarıçapları arasındaki uzunluk ilişkilerini yaz.'],
 bilgi=[KUD,DCA],
 ad=[A('İç çemberin yarıçapını bul','İç çember karenin kenarlarına teğettir; çapı kenar uzunluğuna eşittir.','r = 6 ÷ 2 = 3 → r² = 9'),A('Dış çemberin yarıçapının karesini bul','Dış çemberin yarıçapı, karenin köşegeninin yarısıdır; köşegen uzunluğunun karesi 6² + 6² dir.','köşegen² = 72 → R² = 72 ÷ 4 = 18'),A('Halkanın alanını yaz','Halka, dış daire ile iç dairenin farkıdır.','π × 18 − π × 9 = 9π')],
 puf='Yarıçapları kenar uzunluğundan türet.',sekil=SK10)

bitir_geo('daireiki','Dairede Çevre ve Alan')
