"""TYT Geometri · Dairede Çevre ve Alan · 10 şekilli soru (kardeş yok, ipucu 1). Şekiller hesaplanan koordinatlarla çizilir; her cevap ve çeldirici değer Python'da assert edilir (π = 3 ya da π cinsinden)."""
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
    P.yaz(os.path.join(GD,onek+'-1.json'),f'/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/gcb/bos-{onek}.json')
    tipler={}
    for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=TIPK[c['tipId']]))['kartlar'].append(c['id'])
    json.dump(dict(konu=konuad,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 TYT Geometri çıkmış soruları (yalnız mantık), MEB 9–10. sınıf geometri müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar',onek+'.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler))
P=Parti('daire','Dairede Çevre ve Alan','geo|Dairede Çevre ve Alan',ders='TYT Geometri',idon='tytgeo')
P.k='geo|Dairede Çevre ve Alan'; H.KONU='Dairede Çevre ve Alan'
def ok(a,b,t=1e-6): assert abs(a-b)<t,(a,b)
DCA=B('Çember ve daire','yarıçapı r olan çemberin çevresi 2πr, dairenin alanı πr² dir (çap = 2r). Örnek: r = 5 için çevre 10π, alan 25π')
DIL=B('Daire dilimi','merkez açısı α olan dilimin yay uzunluğu 2πr × α/360, alanı πr² × α/360 dır; dilimin çevresi yay uzunluğu ile iki yarıçapın toplamıdır. Örnek: r = 9 ve α = 40° ise yay uzunluğu 2π × 9 × 40/360 = 2π dir')
HAL=B('Halka','eş merkezli iki çemberin arasında kalan bölgeye halka denir; halkanın alanı, çemberlerin sınırladığı dairelerin alanları kullanılarak bulunur')
TAR=B('Taralı alan','taralı bölgenin alanı, bildiğin şekillerin (kare, daire, dilim) alanlarını toplayıp çıkararak bulunur. Örnek: kenarı 4 olan karenin içindeki yarıçapı 2 olan dairenin dışında kalan alan 16 − 4π dir')
TEK=B('Tekerlek dönüşü','çevresi C olan tekerlek kaymadan bir tam turda C kadar yol alır; tur sayısı = yol ÷ çevre. Örnek: çevresi 50 cm olan tekerlek 400 cm yolu 8 turda alır')
PI3='π yerine 3 alınız.'

# ===== 01 · çevreden alan · kolay · hikâyeli =====
kartla('K-GDC-01','Çevreden yarıçap, alan','Çevre 2πr den yarıçap bulunur; alan πr² ile hesaplanır.','Çevre formülünü πr almak; alan yerine r² ya da πr yazmak; yarıçapı bulmadan çevreyi alana katmak.','kolay',3,'ge-dc-cevre-alan','Çevre ve alan hesabı','hikâyeli')
r1=6; assert 2*3*r1==36 and 3*r1**2==108 and 3*r1==18 and r1**2==36 and 36*r1==216 and 3*12**2==432
s=.25; f=F(); f.circ((0,0),r1*s); f.dot((0,0)); f.node((0,.28),'$O$'); f.node((0,-r1*s-.4),'Çevre $=36\\ \\mathrm{m}$')
SK1=f.svg()
q('0001',tipId='ge-dc-cevre-alan',tip='Çevre ve alan hesabı',z='kolay',alt='Çevre ve Alan',kaz='Dairenin çevresinden yarıçapını, yarıçaptan alanını hesaplar.',kalip='hikâyeli',
 kart='K-GDC-01 (çevre, alan) · çevre 36',
 metin='Bir belediye, dairesel biçimli bir parkın tamamına çim serecektir. Parkın çevresi şekilde verilmiştir. Çim, metrekaresi aynı fiyatla satılmaktadır ve parkın alanı kadar çim alınacaktır. '+PI3+'\nBuna göre, alınacak çim kaç m² dir?',
 dogru=108,yan=[(18,'Alan yerine π × r = 3 × 6 = 18 hesaplamış.','bilgi'),(36,'Alanı r² = 36 olarak almış; π çarpanını unutmuş.','bilgi'),(216,'Alanı çevre × r = 36 × 6 olarak almış; 2 ye bölmeyi unutmuş.','islem'),(432,'Çevreyi π × r sanıp r = 12 bulmuş, alanı 3 × 12² = 432 hesaplamış.','bilgi')],
 istenen='Alınacak çimin alanı (m²).',
 ip=['Önce çevre formülünden yarıçapı bul; alan için yarıçapın karesi gerekir.'],
 bilgi=[DCA],
 ad=[A('Yarıçapı bul','Çevre 2πr dir; π = 3 alınır.','2 × 3 × r = 36 → r = 6'),A('Alanı yaz','Alan, π × r² dir.','3 × 6² = 3 × 36'),A('Hesapla','Çarpma yapılır.','108')],
 puf='Çevre verilince önce yarıçapı bul (C = 2πr); alan için yarıçapın karesi gerekir.',sekil=SK1)

# ===== 02 · dilimin çevresi · orta =====
kartla('K-GDC-02','Daire diliminin çevresi','Yay uzunluğu 2πr × α/360 dır; dilimin çevresi yay ile iki yarıçapın toplamıdır.','Yalnız yay uzunluğunu almak; açı oranını 180 ile kurmak; tam çemberi cevap yazmak.','orta',3,'ge-dc-dilim','Daire dilimi: yay ve alan')
r2=6; al2=60; yay2=2*3*r2*al2/360; assert yay2==6 and yay2+2*r2==18
assert 2*3*r2*al2/180==12 and 12+12==24 and 2*3*r2==36 and 36+6==42
s=.35; R2=r2*s; a1,a2=15,75; P1=pc((0,0),R2,a1); P2=pc((0,0),R2,a2)
f=F(); f.fill([(0,0),P1]+[pc((0,0),R2,a1+i*(a2-a1)/20) for i in range(21)]+[P2]); f.line((0,0),P1); f.line((0,0),P2); f.oarc((0,0),R2,a1,a2)
f.arc((0,0),P1,P2,.55,'$60^\\circ$',.95); f.sl('$6$',(0,0),P1,P2,.26); f.node((-.2,-.1),'$O$')
SK2=f.svg()
q('0002',tipId='ge-dc-dilim',tip='Daire dilimi: yay ve alan',z='orta',alt='Dilimin Çevresi',kaz='Merkez açısı ve yarıçapı verilen daire diliminin çevresini hesaplar.',
 kart='K-GDC-02 (dilim çevresi) · r = 6, 60°',
 metin='Şekilde merkezi O olan bir daire diliminin yarıçapı (cm cinsinden) ve merkez açısı gösterilmiştir. Dilimin çevresi, yay uzunluğu ile iki yarıçapın toplamına eşittir. '+PI3+'\nBuna göre, bu dilimin çevresi kaç cm dir?',
 dogru=18,yan=[(6,'Yalnız yay uzunluğunu bulup iki yarıçapı eklememiş.','dikkat'),(24,'Açı oranını 60/180 almış: yay 12, çevre 12 + 12 = 24.','bilgi'),(36,'Dilim yerine tam çemberin uzunluğunu (2 × 3 × 6) yazmış.','dikkat'),(42,'Tam çember uzunluğuna yayı eklemiş: 36 + 6.','islem')],
 istenen='Dilimin çevresi (cm).',
 ip=['Dilimin çevresi hangi üç parçadan oluşuyor? Yay uzunluğu, tam çemberin kaçta kaçı?'],
 bilgi=[DIL],
 ad=[A('Yay uzunluğunu bul','60° lik açı, tam çemberin 60/360 = 1/6 sidir.','2 × 3 × 6 × 1/6 = 6'),A('Yarıçapları ekle','Çevreye iki yarıçap da katılır.','2 × 6 = 12'),A('Çevreyi yaz','Yay ve yarıçaplar toplanır.','6 + 12 = 18')],
 puf='Dilimin çevresi sorulduğunda yay uzunluğuna iki yarıçapı eklemeyi unutma.',sekil=SK2)

# ===== 03 · pizza dilimi alanı · orta · hikâyeli =====
kartla('K-GDC-03','Daire diliminin alanı','Çaptan yarıçap bulunur; dilimin alanı tam dairenin α/360 ıdır.','Çapı yarıçap sanmak; açı oranını 180 ile kurmak; tam dairenin alanını cevap yazmak.','orta',3,'ge-dc-dilim','Daire dilimi: yay ve alan','hikâyeli')
r3=12; al3=120; tam3=3*r3**2; assert tam3==432 and tam3*al3/360==144
assert 2*3*r3*al3/360==24 and tam3*al3/180==288 and 3*24**2*al3/360==576 and tam3*60/360==72
s=.16; R3=r3*s; a1,a2=30,150
f=F(); f.circ((0,0),R3); f.fill([(0,0),pc((0,0),R3,a1)]+[pc((0,0),R3,a1+i*(a2-a1)/20) for i in range(21)]+[pc((0,0),R3,a2)]); f.line((0,0),pc((0,0),R3,a1)); f.line((0,0),pc((0,0),R3,a2)); f.oarc((0,0),R3,a1,a2)
f.line((-R3,0),(R3,0)); f.arc((0,0),pc((0,0),1,a1),pc((0,0),1,a2),.5,'$120^\\circ$',.95); f.node((0,-.3),'$24\\ \\mathrm{cm}$'); f.dot((0,0))
SK3=f.svg()
q('0003',tipId='ge-dc-dilim',tip='Daire dilimi: yay ve alan',z='orta',alt='Dilimin Alanı',kaz='Çapı verilen dairede merkez açısı bilinen dilimin alanını hesaplar.',kalip='hikâyeli',
 kart='K-GDC-03 (dilim alanı) · çap 24, 120°',
 metin='Bir pizzacı, çapı şekilde verilen dairesel bir pizzayı keserken taralı dilimi 120° lik merkez açısıyla ayırmıştır. Müşteri, bu dilimin alanı kadar peynir ücreti ödeyecektir. '+PI3+'\nBuna göre, taralı dilimin alanı kaç cm² dir?',
 dogru=144,yan=[(24,'Alan yerine yay uzunluğunu (2 × 3 × 12 × 1/3) hesaplamış.','bilgi'),(72,'Açı oranını 60/360 = 1/6 almış: 432 ÷ 6.','islem'),(288,'Açı oranını 120/180 almış: 432 × 2/3.','bilgi'),(432,'Tam dairenin alanını cevap yazmış; dilimin oranını uygulamamış.','dikkat')],
 istenen='Taralı dilimin alanı (cm²).',
 ip=['Şekildeki 24 cm uzunluğu yarıçap mı çap mı? Dilim, tam dairenin kaçta kaçıdır?'],
 bilgi=[DIL],
 ad=[A('Yarıçapı bul','Şekildeki doğru parçası daireyi ortadan bölen çaptır.','r = 24 ÷ 2 = 12'),A('Tam dairenin alanı','Alan π × r² dir.','3 × 12² = 432'),A('Dilimin payını al','120° lik dilim tam dairenin 120/360 = 1/3 üdür.','432 × 1/3 = 144')],
 puf='Dilim alanı = tam daire alanı × (merkez açı ÷ 360); önce şekildeki uzunluğun çap mı yarıçap mı olduğuna bak.',sekil=SK3)

# ===== 04 · halka alanı (π cinsinden) · orta =====
kartla('K-GDC-04','Halka alanı','Halkanın alanı iki dairenin alanları kullanılarak bulunur; sonuç π cinsinden yazılır.','Yarıçapların farkının karesini almak; yalnız bir dairenin alanını yazmak; alanları toplamak.','kolay',3,'ge-dc-halka','Halka alanı')
Rh,rh=10,8; assert Rh**2-rh**2==36 and (Rh-rh)**2==4 and rh**2==64 and Rh**2==100 and Rh**2+rh**2==164
s=.2; f=F(); f.raw(f'\\path[fill=vurgu!25,even odd rule] (0,0) circle ({Rh*s}) (0,0) circle ({rh*s});'); f.circ((0,0),Rh*s); f.circ((0,0),rh*s); f.dot((0,0))
p1=pc((0,0),rh*s,30); p2=pc((0,0),Rh*s,150); f.line((0,0),p1); f.line((0,0),p2)
f.sl('$8$',(0,0),p1,p2,.24); f.sl('$10$',(0,0),p2,p1,.27); f.node((.02,-.27),'$O$')
SK4=f.svg()
q('0004',tipId='ge-dc-halka',tip='Halka alanı',z='kolay',alt='Halka Alanı',kaz='Eş merkezli iki çemberin oluşturduğu halkanın alanını π cinsinden bulur.',
 kart='K-GDC-04 (halka) · R = 10, r = 8',
 metin='Şekilde O merkezli iç içe iki çemberin yarıçapları (cm cinsinden) gösterilmiştir. İki çember arasında kalan taralı bölgeye halka denir. Sonuç π cinsinden yazılacaktır.\nBuna göre, taralı halkanın alanı kaç cm² dir?',
 dogru='36π',sira=['4π','36π','64π','100π','164π'],
 yan=[('4π','Yarıçapların farkının karesini alıp π ile çarpmış: π × (10 − 8)².','bilgi'),('64π','Yalnız iç dairenin alanını (π × 8²) yazmış.','dikkat'),('100π','Yalnız dış dairenin alanını (π × 10²) yazmış.','dikkat'),('164π','İki dairenin alanlarını toplamış; halka için çıkarmak gerekir.','bilgi')],
 istenen='Halkanın alanı (cm², π cinsinden).',
 ip=['Taralı bölgenin sınırını oluşturan iki çembere ve yarıçaplarına bak.'],
 bilgi=[HAL],
 ad=[A('Dış dairenin alanı','Büyük yarıçap 10 dur.','π × 10² = 100π'),A('İç dairenin alanı','Küçük yarıçap 8 dir.','π × 8² = 64π'),A('Farkı al','Halka = dış daire − iç daire.','100π − 64π = 36π')],
 puf='Halka alanı iki dairenin farkıdır: π(R² − r²); yarıçapların farkının karesi değildir.',sekil=SK4)

# ===== 05 · kare içinde daire · kolay =====
kartla('K-GDC-05','Kare içinde daire','Kenara teğet dairenin yarıçapı kenarın yarısıdır; taralı alan kare eksi daire alanıdır.','Daire alanı yerine πr almak; çapı yarıçap sanmak; yalnız kare ya da yalnız daireyi yazmak.','kolay',3,'ge-dc-taral','Taralı alanlar')
a5=12; assert a5**2-3*(a5//2)**2==36 and 3*(a5//2)**2==108 and a5**2-3*(a5//2)==126 and a5**2==144 and 144+108==252
s=.2; L5=a5*s
f=F(); f.raw(f'\\path[fill=vurgu!25,even odd rule] (0,0) rectangle ({L5},{L5}) ({L5/2},{L5/2}) circle ({L5/2});'); f.raw(f'\\draw (0,0) rectangle ({L5},{L5}); \\draw ({L5/2},{L5/2}) circle ({L5/2});')
f.node((L5/2,-.3),'$12\\ \\mathrm{cm}$')
SK5=f.svg()
q('0005',tipId='ge-dc-taral',tip='Taralı alanlar',z='kolay',alt='Kare ve Daire',kaz='Kareye teğet dairenin yarıçapını bulup taralı bölgenin alanını hesaplar.',
 kart='K-GDC-05 (kare, daire, taralı) · kenar 12',
 metin='Şekilde kenar uzunluğu verilen bir karenin içine, dört kenarına da teğet olan bir daire çizilmiştir. '+PI3+'\nBuna göre, karenin içinde daire dışında kalan taralı bölgelerin alanları toplamı kaç cm² dir?',
 dogru=36,yan=[(108,'Taralı bölge yerine dairenin alanını (3 × 6²) bulmuş.','dikkat'),(126,'Daire alanı yerine π × r = 18 çıkarmış: 144 − 18.','bilgi'),(144,'Yalnız karenin alanını yazmış.','dikkat'),(252,'Daireyi çıkarmak yerine karenin alanına eklemiş: 144 + 108.','islem')],
 istenen='Taralı bölgelerin alanları toplamı (cm²).',
 ip=['Dairenin yarıçapı karenin kenarıyla nasıl ilişkili?'],
 bilgi=[TAR,DCA],
 ad=[A('Yarıçapı bul','Daire karenin karşılıklı kenarlarına teğettir; çapı kenar uzunluğuna eşittir.','r = 12 ÷ 2 = 6'),A('Alanları yaz','Kare ve daire alanları ayrı ayrı bulunur.','kare 12² = 144 · daire 3 × 6² = 108'),A('Farkı al','Taralı bölge = kare − daire.','144 − 108 = 36')],
 puf='Teğet daire kenarın yarısı kadar yarıçapa sahiptir; taralı alan = kare − daire.',sekil=SK5)

# ===== 06 · köşelerde çeyrek daireler · orta =====
kartla('K-GDC-06','Köşelerde çeyrek daireler','Köşelerdeki dört çeyrek daire birlikte bir tam dairenin alanını verir; taralı alan kare eksi bu alandır.','Dört çeyreği bir daire yerine dört daire saymak; yalnız bir ya da iki çeyrek çıkarmak; karenin alanını yazmak.','orta',3,'ge-dc-taral','Taralı alanlar')
a6=8; assert 4*(3*(a6//2)**2/4)==48 and a6**2-48==16 and a6**2-2*(3*16/4)==40 and a6**2-3*16/4==52
s=.3; L6=a6*s; h=L6/2
f=F(); f.raw(f'\\path[fill=vurgu!25,even odd rule] (0,0) rectangle ({L6},{L6}) (0,0) -- ({h},0) arc[start angle=0,end angle=90,radius={h}] -- cycle ({L6},0) -- ({L6},{h}) arc[start angle=90,end angle=180,radius={h}] -- cycle ({L6},{L6}) -- ({h},{L6}) arc[start angle=180,end angle=270,radius={h}] -- cycle (0,{L6}) -- (0,{h}) arc[start angle=270,end angle=360,radius={h}] -- cycle;')
f.raw(f'\\draw (0,0) rectangle ({L6},{L6}); \\draw ({h},0) arc[start angle=0,end angle=90,radius={h}]; \\draw ({L6},{h}) arc[start angle=90,end angle=180,radius={h}]; \\draw ({h},{L6}) arc[start angle=180,end angle=270,radius={h}]; \\draw (0,{h}) arc[start angle=270,end angle=360,radius={h}];')
f.node((h,-.3),'$8\\ \\mathrm{cm}$')
SK6=f.svg()
q('0006',tipId='ge-dc-taral',tip='Taralı alanlar',z='orta',alt='Çeyrek Daireler',kaz='Köşelerdeki çeyrek dairelerin alanı toplamını kareden çıkararak taralı bölgenin alanını bulur.',
 kart='K-GDC-06 (çeyrek daireler) · kenar 8',
 metin='Şekilde kenar uzunluğu verilen bir karenin her köşesi merkez olacak biçimde, yarıçapı kenarın yarısı olan dört çeyrek daire çizilmiştir. Çeyrek daireler birbirine yalnız kenarların orta noktalarında değmektedir. '+PI3+'\nBuna göre, taralı bölgenin alanı kaç cm² dir?',
 dogru=16,yan=[(40,'Çeyrek dairelerden yalnız ikisini çıkarmış: 64 − 24.','dikkat'),(48,'Çeyrek dairelerin toplam alanını (48) taralı alan sanmış.','dikkat'),(52,'Yalnız bir çeyrek dairenin alanını çıkarmış: 64 − 12.','dikkat'),(64,'Karenin alanını cevap yazmış.','dikkat')],
 istenen='Taralı bölgenin alanı (cm²).',
 ip=['Çeyrek dairelerin yarıçapı karenin kenarıyla ilişkili mi? Birleştirsen ne olur?'],
 bilgi=[TAR,DCA],
 ad=[A('Yarıçapı bul','Yarıçap kenarın yarısıdır.','r = 8 ÷ 2 = 4'),A('Çeyreklerin toplamı','Dört çeyrek daire bir tam daire eder.','3 × 4² = 48'),A('Farkı al','Taralı bölge = kare − dört çeyrek.','8² − 48 = 64 − 48 = 16')],
 puf='Taralı alan sorularında parçaları birleştirip bildiğin şekle dönüştürmeyi dene.',sekil=SK6)

# ===== 07 · tekerlek dönüşü · orta · hikâyeli =====
kartla('K-GDC-07','Tekerlek dönüşü','Bir turda alınan yol çevreye eşittir; tur sayısı yolun çevreye bölümüdür; birimler aynı yapılır.','Çapı yarıçap sanmak; çevre yerine alan ya da πr almak; metreyi santimetreye çevirmemek.','orta',3,'ge-dc-teker','Tekerlek dönüşü','hikâyeli')
d7=60; C7=3*d7; yol=108*100; assert C7==180 and yol//C7==60 and yol%C7==0
assert yol//(3*30**2)==4 and (yol*10)//(10*C7)==60 and 108*10//C7==6 and yol//(2*3*60)==30 and yol//(3*30)==120
f=F(); R7=1.1; f.circ((0,R7),R7); f.line((-R7,R7),(R7,R7)); f.node((0,R7-.3),'$60\\ \\mathrm{cm}$'); f.dot((0,R7))
f.line((-1.5,0),(6,0)); xe=5.2
f.raw(f'\\draw[dashed,thin] (0,0) -- (0,-.55); \\draw[dashed,thin] ({xe},0) -- ({xe},-.55); \\draw[<->] (0,-.4) -- ({xe},-.4);'); f.node((xe/2,-.7),'$108\\ \\mathrm{m}$')
SK7=f.svg()
q('0007',tipId='ge-dc-teker',tip='Tekerlek dönüşü',z='orta',alt='Tekerlek Dönüşü',kaz='Tekerleğin çevresinden, belirli bir yolu kaç turda aldığını hesaplar.',kalip='hikâyeli',
 kart='K-GDC-07 (tekerlek) · çap 60 cm, yol 108 m',
 metin='Bir kurye, çapı şekilde verilen tekerlekli bir el arabasını düz bir yolda kaymadan sürerek şekilde gösterilen uzunluktaki yolu alacaktır. Tekerleğin her turda aldığı yol, çevresine eşittir. '+PI3+'\nBuna göre, tekerlek bu yolu kaç tam turda alır?',
 dogru=60,yan=[(4,'Çevre yerine dairenin alanını (3 × 30² = 2700 cm²) kullanıp 10800 ÷ 2700 = 4 bulmuş.','bilgi'),(6,'Yolu 108 m = 1080 cm alarak 1080 ÷ 180 = 6 bulmuş; metreyi santimetreye yanlış çevirmiş.','islem'),(30,'Çapı yarıçap sanıp çevreyi 2 × 3 × 60 = 360 cm almış: 10800 ÷ 360 = 30.','bilgi'),(120,'Çevreyi π × r = 90 cm almış: 10800 ÷ 90 = 120.','bilgi')],
 istenen='Tekerleğin attığı tam tur sayısı.',
 ip=['Tekerlek bir turda ne kadar yol alır? Yolu ve çevreyi aynı birimde yaz.'],
 bilgi=[TEK],
 ad=[A('Çevreyi bul','Çap 60 cm olduğundan çevre π × çap dır.','3 × 60 = 180 cm'),A('Yolu aynı birime çevir','1 m = 100 cm.','108 m = 10 800 cm'),A('Tur sayısını bul','Yol, çevreye bölünür.','10 800 ÷ 180 = 60')],
 puf='Tekerlek sorularında yolu ve çevreyi aynı birime getir; tur sayısı = yol ÷ (π × çap).',sekil=SK7)

# ===== 08 · iki tekerlekte tur oranı · orta · hikâyeli =====
kartla('K-GDC-08','İki tekerlek, tur oranı','Aynı yolu alan iki tekerlekte tur sayısı çevreyle ters orantılıdır; çap oranı yeterlidir.','Oranı ters kurmak; alan oranını (karesini) kullanmak; farkı eklemek.','orta',3,'ge-dc-teker','Tekerlek dönüşü','hikâyeli')
da,dn,na=80,60,36; nn_=na*da//dn; assert nn_==48 and na*da%dn==0
assert na*dn//da==27 and na*da*da//(dn*dn)==64 and na+(da-dn)==56
f=F(); ra,rn=1.12,.84; ca=(0,ra); cn=(4.1,rn)
f.circ(ca,ra); f.circ(cn,rn); f.line((-1.4,0),(5.4,0)); f.line(ca,cn,'thick'); f.dot(ca); f.dot(cn)
f.line((ca[0]-ra,ca[1]),(ca[0]+ra,ca[1])); f.line((cn[0]-rn,cn[1]),(cn[0]+rn,cn[1]))
f.node((ca[0],ca[1]+ra+.28),'\\small arka'); f.node((cn[0],cn[1]+rn+.28),'\\small ön'); f.node((ca[0],ca[1]-.27),'$80\\ \\mathrm{cm}$'); f.node((cn[0],cn[1]-.27),'$60\\ \\mathrm{cm}$')
SK8=f.svg()
q('0008',tipId='ge-dc-teker',tip='Tekerlek dönüşü',z='orta',alt='İki Tekerlek',kaz='Çapları farklı iki tekerleğin aynı yolda attığı tur sayılarını çevre oranıyla karşılaştırır.',kalip='hikâyeli',
 kart='K-GDC-08 (iki tekerlek) · çaplar 80 ve 60, 36 tur',
 metin='Şekildeki bisikletin arka tekerleği büyük, ön tekerleği küçük olup tekerleklerin çapları gösterilmiştir. Bisiklet düz bir yolda ilerlerken tekerlekler kaymamaktadır. Arka tekerlek 36 tur attığı sürede bisiklet, ön tekerleğin de aynı uzunlukta yol almasını sağlar.\nBuna göre, bu sürede ön tekerlek kaç tur atmıştır?',
 dogru=48,yan=[(27,'Oranı ters kurmuş: 36 × 60 ÷ 80 = 27.','bilgi'),(36,'İki tekerleğin tur sayısını aynı sanmış.','bilgi'),(56,'Çaplar farkını (20) tur sayısına eklemiş.','islem'),(64,'Çap oranının karesini kullanmış: 36 × (80/60)² = 64; çevre çapla doğru orantılıdır, alan değil.','bilgi')],
 istenen='Ön tekerleğin attığı tur sayısı.',
 ip=['Aynı yolu alan iki tekerlekten çevresi küçük olan daha mı çok, daha mı az dönmelidir?'],
 bilgi=[TEK],
 ad=[A('Alınan yolu çevreyle yaz','Aynı yol: tur sayısı × çevre iki tekerlekte eşittir; çevre = 3 × çap.','36 × 3 × 80 = n × 3 × 60'),A('Sadeleştir','Ortak 3 çarpanı sadeleşir.','36 × 80 = n × 60'),A('n yi bul','Eşitlikten n çekilir.','n = 2880 ÷ 60 = 48')],
 puf='Aynı yolu alan tekerleklerde tur × çap sabittir; küçük çaplı tekerlek daha çok döner.',sekil=SK8)

# ===== 09 · yalnız birinin içinde kalan bölgeler · zor =====
kartla('K-GDC-09','Üst üste binen çeyrek daireler','İki çeyrek dairenin ortak bölgesi alanlar toplamından kare çıkarılarak bulunur; yalnız birinin içinde kalan bölge toplamdan ortak bölgenin iki katı çıkarılarak elde edilir.','Ortak bölgeyi taralı sanmak; ortak bölgeyi bir kez çıkarmak; bir çeyrek daireyi ya da kareyi yazmak.','zor',4,'ge-dc-taral','Taralı alanlar')
a9=6; ceyrek=3*a9**2/4; yap=2*ceyrek-a9**2; tek=2*ceyrek-2*yap; assert ceyrek==27 and yap==18 and tek==18
assert 2*ceyrek==54 and a9**2==36 and ceyrek-yap==9
import random
random.seed(1); n=200000; ic=0; bir=0
for _ in range(n):
    x=random.random()*a9; y=random.random()*a9
    u=x*x+y*y<=a9*a9; v=(x-a9)**2+(y-a9)**2<=a9*a9
    ic+= (u and v); bir+= (u!=v)
assert abs(ic/n*a9*a9-a9*a9*(pi/2-1))<.25 and abs(bir/n*a9*a9-(2*a9*a9-pi*a9*a9/2))<.3
s=.4; L9=a9*s
f=F(); f.raw(f'\\path[fill=vurgu!25,even odd rule] (0,0) -- ({L9},0) arc[start angle=0,end angle=90,radius={L9}] -- cycle ({L9},{L9}) -- (0,{L9}) arc[start angle=180,end angle=270,radius={L9}] -- cycle;')
f.raw(f'\\draw (0,0) rectangle ({L9},{L9}); \\draw ({L9},0) arc[start angle=0,end angle=90,radius={L9}]; \\draw (0,{L9}) arc[start angle=180,end angle=270,radius={L9}];')
f.node((L9/2,-.3),'$6\\ \\mathrm{cm}$'); f.vl('A',(0,0),(-1,-1),.28); f.vl('B',(L9,0),(1,-1),.28); f.vl('C',(L9,L9),(1,1),.28); f.vl('D',(0,L9),(-1,1),.28)
SK9=f.svg()
q('0009',tipId='ge-dc-taral',tip='Taralı alanlar',z='zor',alt='Üst Üste Binen Yaylar',kaz='İki çeyrek dairenin yalnız birinin içinde kalan bölgelerinin alanlarını bulur.',
 kart='K-GDC-09 (iki çeyrek daire) · kenar 6',
 metin='Şekilde ABCD karesinin kenar uzunluğu verilmiştir. A merkezli ve C merkezli, yarıçapı kenara eşit iki çeyrek daire yayı çizilmiştir; her yay B ile D noktalarından geçer. Taralı bölgeler, iki çeyrek dairenin yalnız birinin içinde kalan bölgelerdir. '+PI3+'\nBuna göre, taralı bölgelerin alanları toplamı kaç cm² dir?',
 dogru=18,yan=[(9,'Taralı bölgelerden yalnız birinin alanını (27 − 18) bulup bırakmış.','dikkat'),(27,'Yalnız bir çeyrek dairenin alanını (3 × 6² ÷ 4) yazmış.','dikkat'),(36,'Karenin alanını cevap yazmış.','dikkat'),(54,'İki çeyrek dairenin alanlarını toplayıp üst üste binen bölgeyi çıkarmamış.','dikkat')],
 istenen='Taralı bölgelerin alanları toplamı (cm²).',
 ip=['İki çeyrek daire üst üste biniyor mu? Binen bölgeyi nasıl bulursun?'],
 bilgi=[TAR],
 ad=[A('Çeyrek dairenin alanı','Yarıçap 6 cm olan çeyrek dairenin alanı daire alanının dörtte biridir.','3 × 6² ÷ 4 = 27'),A('Ortak bölgeyi bul','İki çeyrek daire kareyi örter; üst üste binen bölge iki kez sayılmıştır.','27 + 27 − 36 = 18'),A('Yalnız birindekileri bul','Her çeyrek dairenin yalnız kendine ait kısmı, çeyrek daire eksi ortak bölgedir.','27 − 18 = 9'),A('Toplamı yaz','İki çeyrek dairenin yalnız kendine ait kısımları toplanır.','9 + 9 = 18')],
 puf='İki şekil üst üste biniyorsa: alanlar toplamı = bütün + ortak bölge; yalnız birinde kalan kısım = toplam − 2 × ortak bölge.',sekil=SK9)

# ===== 10 · alandan yarıçap, dilimin çevresi · zor =====
kartla('K-GDC-10','Dilim alanından çevreye','Alandan yarıçap bulunur; yay uzunluğu ve iki yarıçap toplanarak çevre bulunur.','Yarıçapı cevap yazmak; yalnız yayı vermek; iki yarıçapı unutmak ya da yayı eklemeyi unutmak.','orta',4,'ge-dc-dilim','Daire dilimi: yay ve alan')
al10=90; A10=27; r10=sqrt(A10*360/(3*al10)); assert r10==6
yay10=2*3*r10*al10/360; assert yay10==9 and yay10+2*r10==21 and yay10+r10==15 and 2*r10==12
s=.3; R10=r10*s; P1=(R10,0); P2=(0,R10)
f=F(); f.fill([(0,0)]+[pc((0,0),R10,i*90/20) for i in range(21)]); f.line((0,0),P1); f.line((0,0),P2); f.oarc((0,0),R10,0,90); f.dik((0,0),P1,P2,.3)
f.node((.7,.7),'\\small$27\\ \\mathrm{cm}^2$'); f.node((-.2,-.2),'$O$')
SK10=f.svg()
q('0010',tipId='ge-dc-dilim',tip='Daire dilimi: yay ve alan',z='orta',alt='Alandan Çevreye',kaz='Alanı ve merkez açısı verilen dilimin yarıçapını, ardından çevresini hesaplar.',
 kart='K-GDC-10 (dilim, alan → çevre) · 90°, alan 27',
 metin='Şekildeki çeyrek daire biçimli taralı bölgenin alanı verilmiştir. Bu bölgenin sınırı, bir yay ile iki doğru parçasından oluşur. '+PI3+'\nBuna göre, bölgenin sınırının toplam uzunluğu kaç cm dir?',
 dogru=21,yan=[(6,'Yarıçapı (6) bulup bırakmış.','dikkat'),(9,'Yalnız yay uzunluğunu bulup yarıçapları eklememiş.','dikkat'),(12,'Yalnız iki yarıçapın toplamını (2 × 6) yazmış.','dikkat'),(15,'Çevreye yalnız bir yarıçap eklemiş: 9 + 6.','dikkat')],
 istenen='Bölgenin sınırının toplam uzunluğu (cm).',
 ip=['Önce yarıçapı bul.'],
 bilgi=[DIL],
 ad=[A('Yarıçapı bul','90° lik dilimin alanı tam dairenin dörtte biridir.','3 × r² ÷ 4 = 27 → r² = 36 → r = 6'),A('Yay uzunluğunu bul','Yay, tam çemberin dörtte biridir.','2 × 3 × 6 ÷ 4 = 9'),A('Çevreyi yaz','Yay ile iki yarıçap toplanır.','9 + 6 + 6 = 21')],
 puf='Alan ya da yay verilince önce yarıçapı çöz; dilimin çevresinde yaya iki yarıçapı eklemeyi unutma.',sekil=SK10)

bitir_geo('daire','Dairede Çevre ve Alan')
