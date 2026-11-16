import sys,os,math,json
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
from math import sin,cos,tan,radians,degrees,atan2,sqrt,pi
TIPK={}
KY='ÖSYM 2018–2026 TYT Geometri soruları (yalnız mantık) · MEB 9–10. sınıf geometri'
def konu(k,ad): P.k=k; P.konu_adi=ad; H.KONU=ad
def kartla(id,alt,fikir,tuzak,z,adim,tipId,tip,kalip='şekilli',kaynak=None):
    kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,kaynak or KY); TIPK[tipId]=P.k
def q(no,ad,kalip='şekilli',**k): mk(P,no,ad=ad,adim=len(ad),kalip=kalip,**k)
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
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def ang(V,a,b):
    u=sub(a,V); v=sub(b,V); return degrees(math.acos(dot(u,v)/(ln(u)*ln(v))))
def alan(ps): return abs(sum(ps[i][0]*ps[(i+1)%len(ps)][1]-ps[(i+1)%len(ps)][0]*ps[i][1] for i in range(len(ps))))/2
class F:
    def __init__(s): s.o=[]
    def raw(s,t): s.o.append(t)
    def line(s,p,q_,st=''): s.o.append(f'\\draw[{st}] {pt(p)} -- {pt(q_)};')
    def poly(s,ps,st=''): s.o.append(f'\\draw[{st}] '+' -- '.join(map(pt,ps))+' -- cycle;')
    def fill(s,ps,st='fill=vurgu!25'): s.o.append(f'\\fill[{st}] '+' -- '.join(map(pt,ps))+' -- cycle;')
    def node(s,p,t,st=''): s.o.append(f'\\node[{st}] at {pt(p)} {{{t}}};')
    def dot(s,p,r=1.2): s.o.append(f'\\fill {pt(p)} circle ({r}pt);')
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
    def ell(s,c,rx,ry,st='',a0=None,a1=None):
        if a0 is None: s.o.append(f'\\draw[{st}] {pt(c)} ellipse [x radius={rx:.3f},y radius={ry:.3f}];')
        else: s.o.append(f'\\draw[{st}] ({c[0]+rx*cos(radians(a0)):.3f},{c[1]+ry*sin(radians(a0)):.3f}) arc[start angle={a0},end angle={a1},x radius={rx:.3f},y radius={ry:.3f}];')
    def body(s): return '\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'+'\n'.join(s.o)+'\n\\end{tikzpicture}'
    def svg(s): return tikz_svg(s.body())
KP=.5; AL=radians(40); CAM=(KP*cos(AL),-1,KP*sin(AL))
def pr(p): return (p[0]+KP*p[1]*cos(AL),p[2]+KP*p[1]*sin(AL))
def katı(V,faces):
    c=cen(list(V.values())); vis={}; adj={}
    for fc in faces:
        ps=[V[k] for k in fc]; n=cross(sub(ps[1],ps[0]),sub(ps[2],ps[0]))
        if dot(n,sub(cen(ps),c))<0: n=mul(n,-1)
        vis[fc]=dot(n,CAM)>1e-9
        for i in range(len(fc)):
            e=frozenset((fc[i],fc[(i+1)%len(fc)])); adj.setdefault(e,[]).append(fc)
    hidden={e for e,fs in adj.items() if not any(vis[x] for x in fs)}
    return vis,hidden,list(adj.keys())
def ciz_kati(f,V,faces,sc):
    vis,hidden,edges=katı(V,faces); Q={k:mul(pr(v),sc) for k,v in V.items()}
    for e in edges:
        a,b=sorted(e); f.line(Q[a],Q[b],'dashed' if e in hidden else '')
    return Q,vis,hidden
def izgara(f,x0,x1,y0,y1,s,eksen=True,sayi=True,adim=1):
    f.raw(f'\\draw[black!20,very thin] ({x0*s:.3f},{y0*s:.3f}) grid[step={s*adim:.3f}] ({x1*s:.3f},{y1*s:.3f});')
    if eksen:
        f.raw(f'\\draw[-{{Stealth[length=2mm]}},thick] ({x0*s-.15:.3f},0) -- ({x1*s+.25:.3f},0);')
        f.raw(f'\\draw[-{{Stealth[length=2mm]}},thick] (0,{y0*s-.15:.3f}) -- (0,{y1*s+.25:.3f});')
        f.node((x1*s+.45,-.2),'$x$'); f.node((.22,y1*s+.42),'$y$'); f.node((.17,-.22),'$O$')
        if sayi:
            for i in range(x0,x1+1):
                if i not in (0,-1): f.node((i*s,-.26),f'\\footnotesize ${i}$')
            for j in range(y0,y1+1):
                if j not in (0,-1): f.node((-.3 if j>0 else -.34,j*s),f'\\footnotesize ${j}$')
def bitir_geo(onek,konuadi):
    for qq in P.ANA: qq['kardes']=None
    P.yaz(os.path.join(GD,f'{onek}-1.json'),f'/tmp/bos-{onek}.json')
    tipler={}
    for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=TIPK[c['tipId']]))['kartlar'].append(c['id'])
    json.dump(dict(konu=konuadi,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 TYT Geometri çıkmış soruları (yalnız mantık), MEB 9–10. sınıf geometri müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar',f'{onek}.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler))
"""TYT Geometri · Küre (6 soru; kardeş yok, ipucu 1). Koordinatlar hesaplanır, TikZ aynı değerlerden; her cevap/çeldirici assert edilir."""
P=Parti('kure','Küre','geo|Küre',ders='TYT Geometri',idon='tytgeo')
EL=radians(24)
KHAC=B('Kürenin hacmi','V = 4 × π × r³ ÷ 3 tür (r yarıçap). Örnek: r = 3 için V = 4 × π × 27 ÷ 3 = 36π')
KYUZ=B('Kürenin yüzey alanı','A = 4 × π × r² dir. Yarım kürenin eğri yüzeyi, tam küre yüzeyinin yarısıdır. Örnek: r = 2 için küre yüzeyi 16π')
KSIL=B('Silindir ve küre','yarıçapı r ve yüksekliği h olan silindirin hacmi π × r² × h dir. Kürenin hacmi 4πr³ ÷ 3 tür. Örnek: r = 2 ve h = 4 için silindirin hacmi 16π, yarıçapı 2 olan kürenin hacmi 32π ÷ 3')
KKES=B('Kürenin kesiti','bir düzlemin küreyi kestiği bölge dairedir. Merkezin düzleme uzaklığı d, kürenin yarıçapı R ise kesit dairenin yarıçapı r için R² = r² + d² dir. Örnek: R = 5, d = 3 ise r = 4')
PIS=B('Pisagor bağıntısı','dik üçgende dik kenarların kareleri toplamı hipotenüsün karesine eşittir. Örnek: 6, 8, 10 üçgeni için 6² + 8² = 10²')
def kure(f,R,merkez=(0,0),ekv=True):
    f.ell(merkez,R,R,'')
    if ekv:
        ry=R*sin(EL); f.ell(merkez,R,ry,'',180,360); f.ell(merkez,R,ry,'dashed',0,180)
konu('geo|Küre','Küre')
# =================== 01 · hacim · kolay ===================
kartla('K-GKU-01','Kürenin hacmi','V = 4πr³ ÷ 3; yarıçap şekilden okunur.','Yüzey alanı formülüyle karıştırmak; 1/3 çarpanını unutmak; yarıçap yerine çap kullanmak.','kolay',3,'ge-ku-hacim','Kürenin hacmi')
r1=6; assert 4*r1**3//3==288 and 4*r1**2==144 and 4*r1**3==864 and 4*(2*r1)**3//3==2304 and 4*(2*r1)**3==6912 and 4*r1**3%3==0
f=F(); sc=.42; R=r1*sc; kure(f,R)
f.line((0,0),(R,0),'dashed'); f.dot((0,0),1.1)
f.node((-.2,-.22),'$O$'); f.node((R+.25,0),'$A$'); f.node((R/2,-.27),'$6$')
SK1=f.svg()
q('0001',tipId='ge-ku-hacim',tip='Kürenin hacmi',z='kolay',alt='Hacim',kaz='Yarıçapı verilen kürenin hacmini π cinsinden hesaplar.',
 kart='K-GKU-01 (hacim) · r = 6',
 metin='Şekilde merkezi O noktası olan bir kürenin yarıçapı cm cinsinden verilmiştir. A noktası küre üzerindedir ve küre yüzeyindeki bütün noktalar merkeze eşit uzaklıktadır; kürenin ekvator çemberinin görünmeyen kısmı kesikli çizgiyle gösterilmiştir.\nBuna göre, bu kürenin hacmi kaç cm³ tür?',
 dogru='288π',sira=['144π','288π','864π','2304π','6912π'],yan=[('144π','Hacim yerine yüzey alanı formülünü (4 × π × 6²) kullanmış.','bilgi'),('864π','Hacim formülündeki 1/3 çarpanını unutmuş: 4 × π × 6³ = 864π.','bilgi'),('2304π','Yarıçap yerine çapı (12) alıp 4 × π × 12³ ÷ 3 = 2304π bulmuş.','dikkat'),('6912π','Hem çapı (12) almış hem de 1/3 çarpanını unutmuş: 4 × π × 12³ = 6912π.','bilgi')],
 istenen='Kürenin hacmi (cm³).',
 ip=['Şekilde verilen uzunluk kürenin yarıçapı mı, çapı mı? Hacim formülünde hangisi kullanılır?'],
 bilgi=[KHAC],
 ad=[A('Yarıçapı oku','|OA| kürenin merkezinden yüzeyine uzaklıktır.','r = 6 cm'),A('Küpünü al','Hacim formülü r³ içerir.','6³ = 216'),A('Hacmi hesapla','4 × π × r³ ÷ 3 işlemini yap.','4 × π × 216 ÷ 3 = 288π cm³')],
 puf='Kürenin hacmi 4πr³ ÷ 3, yüzey alanı 4πr² dir; r yarıçaptır, çap değil.',sekil=SK1)
# =================== 02 · yüzeyden hacme · orta ===================
kartla('K-GKU-02','Yüzey alanından hacme','Yüzey alanı 4πr² ile yarıçap bulunur, sonra hacim hesaplanır.','Yarıçap yerine r² değerini kullanmak; yarım küre formülüyle karıştırmak; 1/3 çarpanını unutmak.','orta',4,'ge-ku-yuzey','Yüzey alanından hacme geçiş')
S2=324; r2=int(sqrt(S2/4)); assert r2==9 and 4*r2*r2==S2
V2=4*r2**3//3; assert V2==972 and r2**3//3==243 and 2*r2**3//3==486 and 4*r2**3==2916 and 4*r2**3%3==0
f=F(); sc=.17; R=r2*sc; kure(f,R)
f.line((0,0),(R,0),'dashed'); f.dot((0,0),1.1)
f.node((-.2,-.22),'$O$'); f.node((R/2,-.25),'$r$')
SK2=f.svg()
q('0002',tipId='ge-ku-yuzey',tip='Yüzey alanından hacme geçiş',z='orta',alt='Yüzey Alanından Hacim',kaz='Yüzey alanı verilen kürenin yarıçapını bulup hacmini hesaplar.',
 kart='K-GKU-02 (yüzey → hacim) · yüzey alanı 324π',
 metin='Merkezi O olan şekildeki küre biçimli bir su balonunun yarıçapı r ile gösterilmiştir. Balonun yüzeyinin alanı 324π cm² dir ve balonun lastik kalınlığı ihmal edilmektedir; balon tamamen şişirildiğinde küre biçimini almıştır.\nBuna göre, balonun hacmi kaç cm³ tür?',
 dogru='972π',sira=['243π','324π','486π','972π','2916π'],yan=[('243π','Hacim formülünde 4 çarpanını unutmuş: π × 9³ ÷ 3 = 243π.','bilgi'),('324π','Hacim yerine verilen yüzey alanını işaretlemiş.','dikkat'),('486π','Yarım küre formülünü kullanmış: 2 × π × 9³ ÷ 3 = 486π.','bilgi'),('2916π','Hacim formülündeki 1/3 çarpanını unutmuş: 4 × π × 9³ = 2916π.','bilgi')],
 istenen='Balonun hacmi (cm³).',
 ip=['Hacim için önce hangi büyüklüğü bulmalısın? Yüzey alanı formülü bunu veriyor mu?'],
 bilgi=[KYUZ,KHAC],
 ad=[A('Yüzey alanı formülünü yaz','Küre yüzeyi 4πr² dir.','4 × π × r² = 324π'),A('Yarıçapı bul','Her iki yanı 4π ye böl, sonra karekök al.','r² = 81 → r = 9 cm'),A('Hacim formülünü yaz','Hacim 4πr³ ÷ 3 tür.','V = 4 × π × 9³ ÷ 3'),A('Hesapla','9³ = 729.','4 × 729 ÷ 3 = 972 → 972π cm³')],
 puf='Küre sorularında yarıçap ana anahtardır: yüzey ya da hacimden r bulunur, istenen değer r ile hesaplanır.',sekil=SK2)
# =================== 03 · küre–silindir · orta ===================
kartla('K-GKU-03','Silindirin içindeki küre','Silindir 2πr³, küre 4πr³ ÷ 3; küre silindirin üçte ikisidir.','Oranı ters yazmak (3/2); 1/3 ya da 1/2 almak; silindir hacmini cevap sanmak.','orta',4,'ge-ku-silindir','Silindire teğet küre hacmi')
V3c=54; r3=3; assert pi*r3**2*(2*r3)==54*pi and 2*r3**3==54
V3=4*r3**3//3; assert V3==36 and V3*3==2*V3c and V3c//3==18 and V3c//2==27 and 4*r3**2*1//3==12 and r3**2==9
R=1.35; ry=R*sin(EL); f=F()
f.ell((0,0),R,ry,'',180,360); f.ell((0,0),R,ry,'dashed',0,180); f.ell((0,2*R),R,ry,'')
f.line((-R,0),(-R,2*R)); f.line((R,0),(R,2*R))
f.ell((0,R),R,R,''); f.ell((0,R),R,ry,'',180,360); f.ell((0,R),R,ry,'dashed',0,180)
f.dot((0,0),1.2); f.dot((0,2*R),1.2); f.dot((0,R),1.2)
f.line((0,R),(R,R),'dashed'); f.node((R/2,R+.24),'$r$')
f.node((-.25,R-.05),'$O$')
SK3=f.svg()
q('0003',tipId='ge-ku-silindir',tip='Silindire teğet küre hacmi',z='orta',alt='Silindir ve Küre',kaz='Silindirin içine tam yerleşen kürenin hacmini silindirin hacminden bulur.',
 kart='K-GKU-03 (silindir–küre) · silindir hacmi 54π',
 metin='Şekilde, taban yarıçapı r olan bir dik silindirin içine bir küre yerleştirilmiştir. Küre, silindirin iki tabanına ve yan yüzeyine teğettir; yani silindirin yüksekliği kürenin çapına eşittir. Silindirin hacmi 54π cm³ tür. Şekilde kürenin tabanlara değdiği noktalar işaretlenmiştir.\nBuna göre, kürenin hacmi kaç cm³ tür?',
 dogru='36π',sira=['9π','12π','18π','27π','36π'],yan=[('9π','Hacim yerine taban dairesinin alanını (π × 3²) bulmuş.','dikkat'),('12π','Hacim formülünde r³ yerine r² kullanmış: 4 × π × 9 ÷ 3 = 12π.','bilgi'),('18π','Küre hacmini silindirin 1/3 ü sanmış (koniyle karıştırmış): 54π ÷ 3 = 18π.','bilgi'),('27π','Küreyi silindirin yarısı sanmış: 54π ÷ 2 = 27π.','bilgi')],
 istenen='Kürenin hacmi (cm³).',
 ip=['Silindirin yüksekliğini r cinsinden yaz; hacim ifadesinde r³ çıkıyor mu?'],
 bilgi=[KSIL],
 ad=[A('Silindirin yüksekliğini yaz','Küre iki tabana teğet olduğundan yükseklik çapa eşittir.','h = 2r'),A('Silindirin hacmini r ile yaz','Hacim = taban alanı × yükseklik.','π × r² × 2r = 2πr³ = 54π → r³ = 27 → r = 3'),A('Kürenin hacmini yaz','Hacim formülüne r = 3 yaz.','4 × π × 27 ÷ 3'),A('Hesapla','Bölme ve çarpmayı yap.','36π cm³')],
 puf='Silindire tam yerleşen kürenin hacmi silindirin hacminin 2/3 üdür (2πr³ ve 4πr³ ÷ 3).',sekil=SK3)
# =================== 04 · kesit · orta ===================
kartla('K-GKU-04','Kürenin düzlemle kesiti','Kesit dairenin yarıçapı R² = r² + d² ile bulunur; sonra alan hesaplanır.','Yarıçaptan uzaklığı çıkarmak (R − d); büyük dairenin alanını almak; çapı yarıçap sanmak.','orta',3,'ge-ku-kesit','Kürenin kesit dairesinin alanı')
R4,d4=13,5; rk=int(sqrt(R4**2-d4**2)); assert rk==12 and rk*rk==144 and (R4-d4)**2==64 and R4**2==169 and (R4+d4)**2==324 and (2*rk)**2==576
s=.2; Rr=R4*s; zc=d4*s; rkk=rk*s; ry=rkk*sin(radians(11)); f=F()
f.ell((0,0),Rr,Rr,'')
f.ell((0,zc),rkk,ry,'',180,360); f.ell((0,zc),rkk,ry,'dashed',0,180)
Op=(0,0); O2=(0,zc); Ap=(rkk,zc)
assert abs(dist(Op,Ap)-Rr)<1e-9
f.line(Op,O2,'dashed'); f.line(Op,Ap,'dashed'); f.dot(Op,1.1); f.dot(O2,1.1)
f.node((-.22,-.22),'$O$'); f.node((-.27,zc+.12),'$O\'$'); f.node((Ap[0]+.25,Ap[1]+.1),'$A$')
f.node((-.3,zc*.25),'$5$'); f.node((rkk*.62,zc*.31-.24),'$13$')
SK4=f.svg()
q('0004',tipId='ge-ku-kesit',tip='Kürenin kesit dairesinin alanı',z='orta',alt='Kesit Dairesi',kaz='Küreyi merkezinden uzakta kesen düzlemin oluşturduğu dairenin alanını hesaplar.',
 kart='K-GKU-04 (kesit) · R = 13, d = 5',
 metin='Şekilde merkezi O olan bir küre, merkezine uzaklığı |OO\'| olan yatay bir düzlemle kesilmiştir. O\' noktası kesit dairenin merkezi, A noktası ise kesit çemberi üzerindeki bir noktadır. Kesit düzlemi küreyi merkezi dışında kesmektedir ve şekildeki uzunluklar cm cinsindendir.\nBuna göre, kesit dairesinin alanı kaç cm² dir?',
 dogru='144π',sira=['64π','144π','169π','324π','576π'],yan=[('64π','Kesit yarıçapını 13 − 5 = 8 bulmuş: π × 8² = 64π.','bilgi'),('169π','Kesit yerine kürenin büyük dairesinin alanını (π × 13²) hesaplamış.','dikkat'),('324π','Kesit yarıçapını 13 + 5 = 18 bulmuş: π × 18² = 324π.','bilgi'),('576π','Kesit yarıçapını 12 doğru bulmuş ama π × (2 × 12)² = 576π hesaplamış (çapı yarıçap sanmış).','islem')],
 istenen='Kesit dairesinin alanı (cm²).',
 ip=['O, O\' ve A noktalarını birleştirince hangi özel üçgen oluşuyor? Kesit dairenin yarıçapı bu üçgenin hangi kenarı?'],
 bilgi=[KKES,PIS],
 ad=[A('Dik üçgeni belirle','[OO\'] kesit düzlemine diktir; OO\'A üçgeninin O\' köşesi diktir ve |OA| kürenin yarıçapıdır (hipotenüs).','|OA| = 13, |OO\'| = 5'),A('Kesit yarıçapını bul','Pisagor bağıntısını uygula.','|O\'A|² = 13² − 5² = 144 → 12 cm'),A('Alanı hesapla','Kesit, yarıçapı 12 olan bir dairedir.','π × 12² = 144π cm²')],
 puf='Küreyi düzlemle kestiğinde kesit dairedir; yarıçapı R² − d² nin kareköküdür.',sekil=SK4)
# =================== 05 · toplar / kutu · zor · hikâyeli ===================
kartla('K-GKU-05','Kutudaki toplar','Kutu hacminden topların hacmi çıkarılır; boş kalan hacim bulunur.','Çapı yarıçap sanmak; yalnız kutuyu ya da yalnız topları hesaplamak; topu da kutuya eklemek.','zor',5,'ge-ku-toplar','Kutuda boş kalan hacim','hikâyeli')
d5=4; r5=2; n5=3; Hc5=n5*d5; Vk=pi*r5**2*Hc5; Vt=n5*4*pi*r5**3/3; bos=Vk-Vt
assert abs(Vk-48*pi)<1e-9 and abs(Vt-32*pi)<1e-9 and abs(bos-16*pi)<1e-9
assert abs(pi*d5**2*(2*Hc5)-384*pi)<1e-9 and abs(3*4*pi*d5**3/3-256*pi)<1e-9 and 384-256==128 and 48+32==80
sc5=.5; R=r5*sc5; ry=R*sin(EL); HT=Hc5*sc5; f=F()
f.ell((0,HT),R,ry,''); f.ell((0,0),R,ry,'',180,360); f.ell((0,0),R,ry,'dashed',0,180)
f.line((-R,0),(-R,HT)); f.line((R,0),(R,HT))
for i in range(n5): f.ell((0,R+2*R*i),R,R,'')
SK5=f.svg()
q('0005',tipId='ge-ku-toplar',tip='Kutuda boş kalan hacim',z='zor',alt='Toplar ve Kutu',kaz='Silindir kutuya yerleştirilen topların hacmini kutunun hacminden çıkararak boş hacmi bulur.',kalip='hikâyeli',
 kart='K-GKU-05 (toplar/kutu) · çapı 4 cm üç top',
 metin='Bir spor mağazasında çapı 4 cm olan üç özdeş pinpon topu, şekildeki gibi üst üste dizilerek taban çapı da 4 cm olan ve toplara tam sığan yükseklikte, silindir biçimli saydam bir kutuya konmuştur. Toplar ile kutunun kapağı ve yan yüzeyleri arasında hiçbir boşluk bırakılmamıştır (toplar kutuya teğettir).\nBuna göre, kutunun içinde topların kaplamadığı boşluğun hacmi kaç cm³ tür?',
 dogru='16π',sira=['16π','32π','48π','80π','128π'],yan=[('32π','Boş hacim yerine topların toplam hacmini (3 × 32π ÷ 3) bulmuş.','dikkat'),('48π','Boş hacim yerine kutunun tamamının hacmini (π × 2² × 12) bulmuş.','dikkat'),('80π','Topların hacmini kutunun hacmine eklemiş: 48π + 32π = 80π.','bilgi'),('128π','Çapı (4) yarıçap sanmış: kutu 384π, toplar 256π; 384π − 256π = 128π.','dikkat')],
 istenen='Kutuda topların kaplamadığı boşluğun hacmi (cm³).',
 ip=['Kutunun yüksekliği kaç top çapına eşit? Hangi iki hacmin farkı isteniyor?'],
 bilgi=[KSIL,KHAC],
 ad=[A('Kutunun boyutlarını bul','Taban çapı 4 cm → yarıçap 2 cm. Üç top üst üste: yükseklik 3 × 4 cm.','r = 2, h = 12'),A('Kutunun hacmini bul','Silindirin hacmi π r² h.','π × 4 × 12 = 48π cm³'),A('Topların hacmini bul','Bir topun hacmi 4πr³ ÷ 3; üç top var.','3 × (4 × π × 8 ÷ 3) = 32π cm³'),A('Farkı al','Boşluk = kutu − toplar.','48π − 32π = 16π cm³')],
 puf='Kutuya tam sığan toplarda boşluk = silindirin hacmi − toplamda topların hacmi; çap verilmişse önce yarıçapa geç.',sekil=SK5)
# =================== 06 · yarım küre · kolay · hikâyeli ===================
kartla('K-GKU-06','Yarım kürenin tüm yüzeyi','Yarım kürenin yüzeyi eğri yüzey (2πr²) + taban dairesi (πr²) = 3πr².','Tam küre yüzeyini almak; tabanı unutmak; tam küre yüzeyine tabanı eklemek.','kolay',3,'ge-ku-yarim','Yarım kürenin tüm yüzey alanı','hikâyeli')
r6=6; S6=3*r6**2; assert S6==108 and r6**2==36 and 2*r6**2==72 and 4*r6**2==144 and 4*r6**2+r6**2==180
sc6=.42; R=r6*sc6; ry=R*sin(EL); f=F()
f.ell((0,0),R,ry,'')
f.ell((0,0),R,R,'',180,360)
f.line((0,0),(R,0),'dashed'); f.dot((0,0),1.1); f.node((R/2,.24),'$6$'); f.node((-.2,-.22),'$O$')
SK6=f.svg()
q('0006',tipId='ge-ku-yarim',tip='Yarım kürenin tüm yüzey alanı',z='kolay',alt='Yarım Küre',kaz='Yarım küre biçimli cismin taban dairesi dahil tüm yüzey alanını hesaplar.',kalip='hikâyeli',
 kart='K-GKU-06 (yarım küre) · r = 6',
 metin='Bir çömlekçi, şekildeki gibi yarım küre biçiminde, üstü açık bir kase yapıyor. Kasenin ağzındaki dairesel açıklığın merkezi O ve yarıçapı cm cinsinden şekilde verilmiştir. Kase, ağzına tam oturan düz bir kapakla kapatılacak ve kapağın dış yüzü de dâhil olmak üzere kasenin kapalı yüzeyinin tamamı sırlanacaktır.\nBuna göre, sırlanacak yüzeyin alanı kaç cm² dir?',
 dogru='108π',sira=['36π','72π','108π','144π','180π'],yan=[('36π','Yalnızca kapağı (taban dairesi) hesaplamış: π × 6².','dikkat'),('72π','Yalnızca eğri yüzeyi (2πr²) hesaplamış, kapağı eklememiş.','dikkat'),('144π','Yarım küre yerine tam kürenin yüzey alanını (4πr²) almış.','bilgi'),('180π','Tam küre yüzeyine kapağı da eklemiş: 144π + 36π.','bilgi')],
 istenen='Sırlanacak yüzeyin alanı (cm²).',
 ip=['Kapak dâhil olunca yüzeyi hangi iki parçaya ayırabilirsin? Yarım kürenin eğri yüzeyi tam kürenin kaçta kaçı?'],
 bilgi=[KYUZ],
 ad=[A('Eğri yüzeyi bul','Yarım kürenin eğri yüzeyi tam küre yüzeyinin yarısıdır.','4π × 6² ÷ 2 = 72π'),A('Kapağı bul','Kapak, yarıçapı 6 olan dairedir.','π × 6² = 36π'),A('Topla','Kapak dâhil toplam yüzey.','72π + 36π = 108π cm²')],
 puf='Yarım kürenin tüm yüzeyi, eğri yüzey ile taban dairesinin toplamıdır: 3πr².',sekil=SK6)
bitir_geo('kure','Küre')
