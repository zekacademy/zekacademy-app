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
"""TYT Geometri · Koni (6 soru; kardeş yok, ipucu 1). Koordinatlar hesaplanır, TikZ aynı değerlerden; her cevap/çeldirici assert edilir."""
P=Parti('koni','Koni','geo|Koni',ders='TYT Geometri',idon='tytgeo')
EL=radians(24)
KHAC=B('Koninin hacmi','V = (π × r² × h) ÷ 3. Aynı taban ve yükseklikli silindirin hacminin üçte biridir. Örnek: r = 2, h = 6 için V = π × 4 × 6 ÷ 3 = 8π')
KPIS=B('Ana doğru','koninin tepesinden taban çemberi üzerindeki bir noktaya uzaklığıdır; yarıçap, yükseklik ve ana doğru dik üçgen oluşturur: ℓ² = r² + h². Örnek: r = 5, h = 12 için ℓ = 13')
KYAN=B('Yanal alan','koninin yan yüzeyinin alanı π × r × ℓ dir (ℓ ana doğru). Tüm alan = taban + yanal = π × r² + π × r × ℓ. Örnek: r = 2, ℓ = 5 için yanal alan 10π')
KACI=B('Koninin açınımı','yan yüzey, yarıçapı ana doğru ℓ olan bir daire dilimidir. Dilimin yay uzunluğu taban çemberinin uzunluğuna (2πr) eşittir; bu yüzden dilimin merkez açısı, tam çemberin hangi kesri olduğuna göre bulunur. Örnek: yay, yarıçapı 8 olan çemberin çevresinin 1/4 ü ise merkez açı 90° dir')
def kone(f,r,h,sc,tam_arka=True):
    rx=r*sc; ry=rx*sin(EL); HT=h*sc
    f.ell((0,0),rx,ry,'',180,360); f.ell((0,0),rx,ry,'dashed',0,180)
    f.line((-rx,0),(0,HT)); f.line((rx,0),(0,HT))
    return rx,ry,HT
konu('geo|Koni','Koni')
# =================== 01 · hacim · kolay ===================
kartla('K-GKN-01','Koninin hacmi','Hacim = π r² h ÷ 3; yarıçap ve yükseklik şekilden okunur.','1/3 çarpanını unutmak; ana doğruyu yükseklik sanmak; yarıçap yerine çap kullanmak.','kolay',3,'ge-kn-hacim','Koninin hacmi')
r1,h1=3,4; l1=5; assert r1*r1+h1*h1==l1*l1
assert r1*r1*h1//3==12 and r1*r1*l1//3==15 and r1*r1*h1==36 and (2*r1)**2*h1//3==48 and (2*r1)**2*h1==144 and r1*r1*h1%3==0
f=F(); rx,ry,HT=kone(f,r1,h1,.7)
f.line((0,HT),(0,0),'dashed'); f.line((0,0),(rx,0),'dashed'); f.dot((0,0),1)
f.node((0,HT+.28),'$V$'); f.node((rx+.28,0),'$A$'); f.node((-.2,-.2),'$O$')
f.node((-.22,HT*.45),'$4$'); f.node((rx/2,-.24),'$3$')
SK1=f.svg()
q('0001',tipId='ge-kn-hacim',tip='Koninin hacmi',z='kolay',alt='Hacim',kaz='Koninin hacmini yarıçap ve yükseklikten π cinsinden hesaplar.',
 kart='K-GKN-01 (hacim) · r = 3, h = 4',
 metin='Şekildeki dik dairesel koninin tepe noktası V, taban merkezi O dur. [VO] doğru parçası tabana diktir; [OA] taban yarıçapıdır. Yarıçap ve yükseklik cm cinsinden şekilde verilmiştir. Koni, bir dik üçgenin dik kenarlarından biri etrafında döndürülmesiyle oluşmuştur. Görünmeyen kısımlar kesikli çizgiyle gösterilmiştir.\nBuna göre, koninin hacmi kaç cm³ tür?',
 dogru='12π',sira=['12π','15π','36π','48π','144π'],
 yan=[('15π','Yüksekliği değil ana doğruyu (|VA| = 5) kullanmış: π × 9 × 5 ÷ 3 = 15π.','bilgi'),('36π','Hacim formülündeki 1/3 çarpanını unutmuş: π × 9 × 4 = 36π.','bilgi'),('48π','Yarıçap yerine çapı (6) alıp π × 36 × 4 ÷ 3 = 48π bulmuş.','dikkat'),('144π','Hem çapı (6) almış hem de 1/3 çarpanını unutmuş: π × 36 × 4 = 144π.','bilgi')],
 istenen='Koninin hacmi (cm³).',
 ip=['Hacim formülüne girecek taban alanını ve yüksekliği şekilden oku; hangisi yarıçap, hangisi yükseklik?'],
 bilgi=[KHAC],
 ad=[A('Verileri oku','Yarıçap |OA| = 3 cm, yükseklik |VO| = 4 cm dir.','r = 3, h = 4'),A('Taban alanını bul','Taban, yarıçapı 3 olan bir dairedir.','π × 3² = 9π'),A('Hacmi hesapla','Koninin hacmi taban alanı × yükseklik ÷ 3 tür.','9π × 4 ÷ 3 = 12π cm³')],
 puf='Koninin hacminde yükseklik tabana dik olan |VO| dur; ana doğruyu kullanma ve 1/3 çarpanını unutma.',sekil=SK1)
# =================== 02 · ana doğru · kolay ===================
kartla('K-GKN-02','Ana doğru (Pisagor)','Yarıçap, yükseklik ve ana doğru dik üçgen oluşturur; ana doğru hipotenüstür.','Toplama ya da çıkarma yapmak; karekökü unutmak; hipotenüs yerine dik kenarı bulmak.','kolay',3,'ge-kn-anadogru','Koninin ana doğrusu')
r2,h2=9,12; l2=int(sqrt(r2**2+h2**2)); assert l2==15 and r2+h2==21 and r2**2+h2**2==225 and r2*h2==108 and h2**2-r2**2==63
f=F(); rx,ry,HT=kone(f,r2,h2,.25)
f.line((0,HT),(0,0),'dashed'); f.line((0,0),(rx,0),'dashed'); f.dot((0,0),1)
f.node((0,HT+.28),'$V$'); f.node((rx+.28,0),'$A$'); f.node((-.2,-.22),'$O$')
f.node((-.24,HT*.45),'$12$'); f.node((rx/2,-.24),'$9$')
SK2=f.svg()
q('0002',tipId='ge-kn-anadogru',tip='Koninin ana doğrusu',z='kolay',alt='Ana Doğru',kaz='Koninin yarıçapı ve yüksekliğinden ana doğrusunu Pisagor bağıntısıyla bulur.',
 kart='K-GKN-02 (ana doğru) · r = 9, h = 12',
 metin='Şekildeki dik dairesel koninin tepe noktası V, taban merkezi O dur ve [VO] doğru parçası tabana diktir. A noktası taban çemberi üzerindedir ve [VA] doğru parçası koninin bir ana doğrusudur. Koninin yarıçapı ile yüksekliği cm cinsinden şekilde verilmiştir.\nBuna göre, koninin ana doğrusu olan |VA| kaç cm dir?',
 dogru='15',sira=['3','3√7','9','12','15'],yan=[('3','Pisagor yerine çıkarma yapmış: 12 − 9 = 3.','bilgi'),('3√7','Hipotenüsü yanlış belirlemiş: |VO|² − |OA|² = 144 − 81 = 63 işlemini yapmış.','bilgi'),('9','Yarıçapı (|OA| = 9) ana doğru sanmış.','dikkat'),('12','Yüksekliği (|VO| = 12) ana doğru sanmış.','dikkat')],
 istenen='|VA| ana doğrusunun uzunluğu (cm).',
 ip=['V, O ve A noktalarını birleştirince oluşan üçgen hangi türdendir? Hangi kenar hipotenüs?'],
 bilgi=[KPIS],
 ad=[A('Dik üçgeni bul','[VO] tabana dik olduğundan VOA üçgeninin O köşesi diktir; |VA| hipotenüstür.','|OA| = 9, |VO| = 12'),A('Pisagor yaz','Dik kenarların kareleri toplamı hipotenüsün karesidir.','|VA|² = 9² + 12² = 81 + 144 = 225'),A('Karekökü al','Uzunluk pozitiftir.','|VA| = 15 cm')],
 puf='Ana doğru, koni için hipotenüstür: ℓ = √(r² + h²). 9-12-15, 3-4-5 üçgeninin 3 katıdır.',sekil=SK2)
# =================== 03 · yanal alan · orta ===================
kartla('K-GKN-03','Yanal alan π r ℓ','Önce ana doğru Pisagorla bulunur, sonra yanal alan π × r × ℓ hesaplanır.','Yanal alan yerine tüm alan ya da taban alanı; ℓ yerine h kullanmak; 2π r ℓ.','orta',3,'ge-kn-yanal','Koninin yanal alanı')
r3,h3=6,8; l3=int(sqrt(r3**2+h3**2)); assert l3==10
assert r3*l3==60 and r3*r3==36 and r3*h3==48 and r3*r3+r3*l3==96 and 2*r3*l3==120
f=F(); rx,ry,HT=kone(f,r3,h3,.3)
f.line((0,HT),(0,0),'dashed'); f.line((0,0),(rx,0),'dashed'); f.dot((0,0),1)
f.node((0,HT+.28),'$V$'); f.node((rx+.28,0),'$A$'); f.node((-.2,-.22),'$O$')
f.node((-.24,HT*.45),'$8$'); f.node((rx/2,-.24),'$6$')
SK3=f.svg()
q('0003',tipId='ge-kn-yanal',tip='Koninin yanal alanı',z='orta',alt='Yanal Alan',kaz='Ana doğruyu bulup koninin yanal alanını π cinsinden hesaplar.',
 kart='K-GKN-03 (yanal alan) · r = 6, h = 8',
 metin='Şekilde tepe noktası V, taban merkezi O olan bir dik dairesel koni gösterilmiştir. [VO] tabana diktir. Koninin taban yarıçapı ile yüksekliği cm cinsinden verilmiştir. Koninin açınımında yan yüzey, bir daire dilimi biçimindedir.\nBuna göre, bu koninin yan yüzeyinin (yanal alanının) ölçüsü kaç cm² dir?',
 dogru='60π',sira=['36π','48π','60π','96π','120π'],yan=[('36π','Yanal alan yerine taban alanını (π × 6²) hesaplamış.','dikkat'),('48π','Ana doğru yerine yüksekliği kullanmış: π × 6 × 8 = 48π.','bilgi'),('96π','Yanal alana tabanı da eklemiş: 36π + 60π = 96π.','dikkat'),('120π','Yanal alan formülünü 2 × π × r × ℓ sanmış (çemberin çevresiyle karıştırmış).','bilgi')],
 istenen='Koninin yanal alanı (cm²).',
 ip=['Yanal alan formülünde hangi uzunluk yer alıyor? Şekilde verilmiş mi, yoksa hesaplamak mı gerekiyor?'],
 bilgi=[KPIS,KYAN],
 ad=[A('Ana doğruyu bul','Yarıçap 6, yükseklik 8 olan dik üçgende Pisagor uygula.','ℓ² = 6² + 8² = 100 → ℓ = 10'),A('Formülü yaz','Yanal alan = π × r × ℓ.','π × 6 × 10'),A('Hesapla','Çarpımı yap.','60π cm²')],
 puf='Yanal alan π r ℓ dir ve ℓ ana doğrudur; yükseklik verilmişse önce ℓ = √(r² + h²) bulunur.',sekil=SK3)
# =================== 04 · açınımda daire dilimi · orta ===================
kartla('K-GKN-04','Açınımda daire dilimi açısı','Dilimin yay uzunluğu taban çemberine eşittir: α = 360° × r ÷ ℓ.','Çap kullanmak; r yerine yükseklik ya da ℓ − r almak; 360° ÷ ℓ yapmak.','orta',3,'ge-kn-acinim','Koni açınımı: daire dilimi açısı')
r4,l4=6,10; h4=int(sqrt(l4**2-r4**2)); al4=360*r4/l4
assert h4==8 and al4==216 and 360/l4==36 and al4/2==108 and 360*(l4-r4)/l4==144 and 360*h4/l4==288
a0=270-205/2; a1=270+205/2; s=.28; R=l4*s; rc=r4*s
f=F(); C0=(0,0)
f.line(C0,(R*cos(radians(a0)),R*sin(radians(a0)))); f.line(C0,(R*cos(radians(a1)),R*sin(radians(a1))))
f.o.append(f'\\draw ({R*cos(radians(a0)):.3f},{R*sin(radians(a0)):.3f}) arc[start angle={a0:.2f},end angle={a1:.2f},radius={R:.3f}];')
pm=(R*cos(radians(a1)),R*sin(radians(a1)))
nrm=(-sin(radians(a1)),cos(radians(a1))); f.node((R*cos(radians(a1))/2+.3*nrm[0],R*sin(radians(a1))/2+.3*nrm[1]),'$10$')
f.o.append(f'\\draw ({.55*cos(radians(a0)):.3f},{.55*sin(radians(a0)):.3f}) arc[start angle={a0:.2f},end angle={a1:.2f},radius=.55];')
f.node((0,-.95),'$\\alpha$')
Cc=(R+rc+.6,-R*.15); f.ell(Cc,rc,rc,''); f.line(Cc,add(Cc,(rc,0)),'dashed'); f.dot(Cc,1); f.node((Cc[0]+rc/2,Cc[1]-.24),'$6$')
SK4=f.svg()
q('0004',tipId='ge-kn-acinim',tip='Koni açınımı: daire dilimi açısı',z='orta',alt='Açınım ve Merkez Açı',kaz='Koninin yan yüzeyi olan daire diliminin merkez açısını taban yarıçapı ve ana doğrudan bulur.',
 kart='K-GKN-04 (açınım) · r = 6, ℓ = 10',
 metin='Şekilde bir dik dairesel koninin açınımı verilmiştir: yan yüzeyi, yarıçapı ana doğruya eşit olan bir daire dilimidir ve tabanı bir dairedir; koni, dilimin iki yarıçapı üst üste getirilip yapıştırılarak oluşturulur. Dilimin yarıçapı ile taban dairesinin yarıçapı cm cinsinden gösterilmiştir.\nŞekil ölçekli değildir.\nBuna göre, daire diliminin merkez açısı α kaç derecedir?',
 dogru=216,yan=[(36,'Yay uzunluğu eşitliğini kurmadan 360° ÷ 10 = 36° bulmuş.','bilgi'),(108,'Taban yarıçapı yerine yarısını (3) alıp 360° × 3 ÷ 10 = 108° bulmuş.','bilgi'),(144,'Yarıçap yerine ℓ − r = 4 almış: 360° × 4 ÷ 10 = 144°.','bilgi'),(288,'Yarıçap yerine yüksekliği (8) almış: 360° × 8 ÷ 10 = 288°.','bilgi')],
 istenen='Daire diliminin merkez açısı α (derece).',
 ip=['Koni kurulunca dilimin yayı neye dönüşüyor? İki uzunluğu karşılaştır.'],
 bilgi=[KACI],
 ad=[A('Uzunlukları oku','Dilimin yarıçapı ℓ = 10, taban yarıçapı r = 6.','ℓ = 10, r = 6'),A('Yay uzunluğunu eşitle','Dilimin yayı, taban çemberine dönüşür.','α ÷ 360° × 2π × 10 = 2π × 6'),A('Açıyı çöz','Her iki taraftaki 2π sadeleşir.','α = 360° × 6 ÷ 10 = 216°')],
 puf='Koni açınımında dilimin açısı 360° × r ÷ ℓ dir; r taban yarıçapı, ℓ dilimin yarıçapıdır (yükseklik değil).',sekil=SK4)
# =================== 05 · dondurma külahı · zor · hikâyeli ===================
kartla('K-GKN-05','Daire diliminden külah','Dilimin yarıçapı ana doğru, yayı taban çemberi olur; r bulunur, h Pisagorla, hacim hesaplanır.','Dilimin yarıçapını koninin yarıçapı sanmak; yüksekliği ana doğru almak; 1/3 unutmak.','zor',5,'ge-kn-kulah','Daire diliminden külah hacmi','hikâyeli')
L5=10; al5=288; r5=L5*al5/360; h5=sqrt(L5**2-r5**2); V5=pi*r5**2*h5/3
assert r5==8 and h5==6 and abs(V5-128*pi)<1e-9 and r5*r5*h5/3*3/pi==r5*r5*h5/pi
assert 6*6*8//3==96 and 64*6//2==192 and 64*6==384 and abs(64*10/3-640/3)<1e-9
a0=270-al5/2; a1=270+al5/2; s=.3; R=L5*s; f=F(); C0=(0,0)
f.line(C0,(R*cos(radians(a0)),R*sin(radians(a0)))); f.line(C0,(R*cos(radians(a1)),R*sin(radians(a1))))
f.o.append(f'\\draw ({R*cos(radians(a0)):.3f},{R*sin(radians(a0)):.3f}) arc[start angle={a0:.2f},end angle={a1:.2f},radius={R:.3f}];')
nrm=(-sin(radians(a1)),cos(radians(a1))); f.node((R*cos(radians(a1))/2-.62*nrm[0],R*sin(radians(a1))/2-.62*nrm[1]),'$10$ cm')
f.o.append(f'\\draw ({.5*cos(radians(a0)):.3f},{.5*sin(radians(a0)):.3f}) arc[start angle={a0:.2f},end angle={a1:.2f},radius=.5];')
f.node((0,-.85),'$288^\\circ$')
SK5=f.svg()
q('0005',tipId='ge-kn-kulah',tip='Daire diliminden külah hacmi',z='zor',alt='Külah Hacmi',kaz='Daire diliminden yapılan koninin yarıçapını ve yüksekliğini bulup hacmini hesaplar.',kalip='hikâyeli',
 kart='K-GKN-05 (külah) · dilim yarıçapı 10, merkez açı 288°',
 metin='Bir dondurmacı, şekildeki gibi yarıçapı ve merkez açısı verilen bir daire dilimi biçiminde kesilmiş gofret yaprağının kenarlarını üst üste getirip yapıştırarak koni biçiminde bir külah yapıyor. Yapıştırma payı ve boşluk yoktur. Külah ağzına kadar dondurmayla doldurulacaktır.\nBuna göre, külahın alabileceği dondurmanın hacmi kaç cm³ tür?',
 dogru='128π',sira=['96π','128π','192π','640π/3','384π'],yan=[('96π','Yarıçap ile yüksekliği karıştırmış: r = 6, h = 8 alıp π × 36 × 8 ÷ 3 = 96π bulmuş.','bilgi'),('192π','Hacimde 1/3 yerine 1/2 kullanmış: π × 64 × 6 ÷ 2 = 192π.','bilgi'),('384π','1/3 çarpanını unutmuş: π × 64 × 6 = 384π.','bilgi'),('640π/3','Ana doğruyu (10) yükseklik sanmış: π × 64 × 10 ÷ 3 = 640π/3.','bilgi')],
 istenen='Külahın hacmi (cm³).',
 ip=['Külah yapılınca dilimin yayı neye dönüşür? Bundan külahın yarıçapını bulabilir misin?'],
 bilgi=[KACI,KPIS,KHAC],
 ad=[A('Taban çevresini yay ile eşitle','Dilimin yayı, taban çemberinin uzunluğu olur.','2π × r = 288 ÷ 360 × 2π × 10'),A('Yarıçapı bul','Sadeleştir.','r = 10 × 288 ÷ 360 = 8 cm'),A('Yüksekliği bul','Dilimin yarıçapı ana doğrudur (ℓ = 10).','h² = 10² − 8² = 36 → h = 6 cm'),A('Hacmi hesapla','Koninin hacmi π r² h ÷ 3 tür.','π × 64 × 6 ÷ 3 = 128π cm³')],
 puf='Daire diliminden koni yaparken: dilimin yarıçapı ℓ, yay uzunluğu taban çevresidir; sonra h = √(ℓ² − r²).',sekil=SK5)
# =================== 06 · huni · orta · hikâyeli ===================
kartla('K-GKN-06','Huniden silindire su aktarma','Koni hacmi = silindirdeki su hacmi; yükseklik bulunur.','Koni hacminde 1/3 unutmak; silindirde π r² yerine π r kullanmak; yüksekliği aynı sanmak.','orta',4,'ge-kn-huni','Huniden silindire su aktarma','hikâyeli')
rh,hh,rs=6,12,4; Vh=rh*rh*hh//3; hs=Vh/(rs*rs); assert Vh==144 and hs==9 and 3*Vh/(rs*rs)==27 and Vh/rs==36 and Vh/(2*rs)==18 and hh==12
f=F(); sc=.25; rx=rh*sc; ry=rx*sin(EL); HT=hh*sc
f.ell((0,HT),rx,ry,'')
f.line((-rx,HT),(0,0)); f.line((rx,HT),(0,0)); f.line((0,HT),(0,0),'dashed'); f.line((0,HT),(rx,HT),'dashed'); f.dot((0,HT),1)
f.node((-.22,HT*.5),'$12$'); f.node((rx/2,HT+.27),'$6$')
x0=rx+1.1; rr=rs*sc; ryy=rr*sin(EL); Hc=3.4; hw=hs*sc*1.2
f.ell((x0,Hc),rr,ryy,''); f.ell((x0,0),rr,ryy,'',180,360); f.ell((x0,0),rr,ryy,'dashed',0,180)
f.line((x0-rr,0),(x0-rr,Hc)); f.line((x0+rr,0),(x0+rr,Hc))
f.ell((x0,hw),rr,ryy,'vurgu',180,360); f.ell((x0,hw),rr,ryy,'vurgu,dashed',0,180)
f.line((x0,0),(x0+rr,0),'dashed'); f.dot((x0,0),1); f.node((x0,-.5),'$r=4$')
f.line((x0+rr+.25,0),(x0+rr+.25,hw),'{Stealth[length=1.6mm]}-{Stealth[length=1.6mm]}'); f.node((x0+rr+.5,hw/2),'$h$')
SK6=f.svg()
q('0006',tipId='ge-kn-huni',tip='Huniden silindire su aktarma',z='orta',alt='Huni ve Silindir',kaz='Koni biçimli huninin içindeki suyun hacmini silindirde yüksekliğe çevirir.',kalip='hikâyeli',
 kart='K-GKN-06 (huni) · koni r = 6, h = 12; silindir r = 4',
 metin='Bir laboratuvarda koni biçimli bir huni ağzına kadar suyla doludur. Huninin ağız yarıçapı ile derinliği, ayrıca altındaki silindir biçimli boş kabın taban yarıçapı cm cinsinden şekilde verilmiştir. Hunideki suyun tamamı bu kaba aktarılıyor; su taşmıyor ve kaybolmuyor. Şekil ölçekli değildir.\nBuna göre, kaptaki suyun yüksekliği olan h kaç cm dir?',
 dogru=9,yan=[(12,'Suyun yüksekliğini huninin derinliğiyle aynı sanmış.','dikkat'),(18,'Silindirin taban alanı yerine taban çevresini (2π × 4 = 8π) kullanmış: 144π ÷ 8π = 18.','bilgi'),(27,'Koninin hacmini 1/3 ile çarpmayı unutmuş: 432π ÷ 16π = 27.','bilgi'),(36,'Silindirin taban alanı yerine π r (4π) alıp 144π ÷ 4π = 36 bulmuş.','bilgi')],
 istenen='Kaptaki suyun yüksekliği h (cm).',
 ip=['Aktarma sırasında hangi büyüklük değişmiyor? İki kabın o büyüklüğünü ayrı ayrı yaz.'],
 bilgi=[KHAC,B('Silindirin hacmi','V = π × r² × h, yani taban alanı × yükseklik. Örnek: r = 3, h = 5 için V = π × 9 × 5 = 45π')],
 ad=[A('Suyun hacmini bul','Hunideki su, koninin tamamını doldurur.','V = π × 6² × 12 ÷ 3 = 144π cm³'),A('Silindirde hacmi yaz','Aynı su silindirde π r² h hacmini kaplar.','π × 4² × h = 16π × h'),A('Eşitle','Hacim korunur.','16π × h = 144π'),A('Yüksekliği çöz','Her iki yanı 16π ye böl.','h = 9 cm')],
 puf='Su aktarma sorularında hacim korunur: önce bir kaptaki hacmi bul, sonra diğer kabın taban alanına böl.',sekil=SK6)
bitir_geo('koni','Koni')
