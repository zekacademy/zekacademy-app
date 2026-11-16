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
"""TYT Geometri · Dönüşüm Geometrisi (6 soru; kardeş yok, ipucu 1). Koordinatlar hesaplanır, TikZ aynı değerlerden; her cevap/çeldirici assert edilir."""
P=Parti('donusum','Dönüşüm Geometrisi','geo|Dönüşüm Geometrisi',ders='TYT Geometri',idon='tytgeo')
OTE=B('Öteleme','bir şeklin her noktası aynı yönde ve aynı uzaklıkta kaydırılır. (a, b) kadar ötelemede P(x, y) noktası P\'(x + a, y + b) olur; a sağa (+) ya da sola (−), b yukarı (+) ya da aşağı (−) birim sayısıdır. Örnek: (2, −1) kadar ötelemeyle P(3, 4) → P\'(5, 3)')
YAN=B('Yansıma','x eksenine göre yansımada (x, y) → (x, −y); y eksenine göre (x, y) → (−x, y); y = x doğrusuna göre (x, y) → (y, x); orijine göre (x, y) → (−x, −y) olur. Yansıma uzunlukları korur. Örnek: P(2, 7) için x eksenine göre (2, −7), y = x e göre (7, 2)')
DON=B('Orijin etrafında dönme','saat yönünün tersine 90° dönmede (x, y) → (−y, x); saat yönünde 90° dönmede (x, y) → (y, −x); 180° dönmede (x, y) → (−x, −y) olur. Örnek: P(3, 1) saat yönünde 90° dönünce (1, −3), saatin tersine 90° dönünce (−1, 3) olur')
DONN=B('Bir nokta etrafında dönme','dönme merkezi M ise önce M den P ye gidiş (yatay ve dikey fark, (u, v)) alınır, bu gidiş istenen açıyla döndürülür ve sonuç M nin koordinatlarına eklenir. Saat yönünde 90° dönmede (u, v) farkı (v, −u) olur. Dönme uzunlukları korur: |MP| = |MP\'| dür')
SIM=B('Simetri ekseni','bir şekli, katlayınca üst üste çakışan iki parçaya ayıran doğrudur. Düzgün n kenarlı çokgenin n simetri ekseni vardır (eşkenar üçgenin 3 ü gibi). Kenarları eşit olmayan bir paralelkenarın simetri ekseni yoktur. Örnek: kare 4 simetri eksenine sahiptir')
PIS=B('Pisagor bağıntısı','dik üçgende dik kenarların kareleri toplamı hipotenüsün karesine eşittir. İki nokta arasındaki uzaklık dikey ve yatay farktan Pisagorla bulunur. Örnek: farklar 6 ve 8 ise uzaklık 10')
konu('geo|Dönüşüm Geometrisi','Dönüşüm Geometrisi')
def noktalar(f,pts,s,off):
    for k,(p,dv) in pts.items():
        f.dot(G2(p,s),1.3); f.vl(k,G2(p,s),dv,off)
def G2(p,s): return (p[0]*s,p[1]*s)
def gzemin(f,x1,y1,s):
    f.raw(f'\\draw[black!25,very thin] (0,0) grid[step={s:.3f}] ({x1*s:.3f},{y1*s:.3f});')
    f.raw(f'\\draw[black!40] (0,0) rectangle ({x1*s:.3f},{y1*s:.3f});')
# =================== 01 · öteleme · kolay · hikâyeli ===================
kartla('K-GDN-01','Öteleme miktarı','Karşılık gelen iki noktanın koordinat (kare) farkından öteleme miktarı okunur; işaretler yöne göre verilir.','Yön işaretini unutmak; a·b yerine a + b ya da |a| + |b| almak.','kolay',3,'ge-dn-otele','Kareli zeminde öteleme miktarı','hikâyeli')
v1=(-4,3); T1=[(7,1),(11,1),(9,3)]; Ti=[(p[0]+v1[0],p[1]+v1[1]) for p in T1]
assert v1[0]*v1[1]==-12 and v1[0]+v1[1]==-1 and abs(v1[0])+abs(v1[1])==7 and v1[0]-v1[1]==-7
s=.5; f=F(); gzemin(f,12,8,s)
f.fill([G2(p,s) for p in T1],'fill=black!10'); f.poly([G2(p,s) for p in T1],'thick')
f.fill([G2(p,s) for p in Ti],'fill=vurgu!22'); f.poly([G2(p,s) for p in Ti],'thick')
for k,p,dv in [('A',T1[0],(-1,-1)),('B',T1[1],(1,-1)),('C',T1[2],(0,1))]: f.vl(k,G2(p,s),dv,.3); f.dot(G2(p,s),1.4)
for k,p,dv in [("A'",Ti[0],(-1,-1)),("B'",Ti[1],(1,-.6)),("C'",Ti[2],(0,1))]: f.vl(k,G2(p,s),dv,.34); f.dot(G2(p,s),1.4)
SK1=f.svg()
q('0001',tipId='ge-dn-otele',tip='Kareli zeminde öteleme miktarı',z='kolay',alt='Öteleme',kaz='Kareli zeminde ötelenen şeklin karşılık gelen köşelerinden öteleme miktarını okur.',kalip='hikâyeli',
 kart='K-GDN-01 (öteleme) · (−4, 3) kadar öteleme',
 metin='Bir grafik tasarımcı, kareli zemine çizdiği ABC üçgeni biçimindeki logoyu, tasarım programında bir kaydırma komutuyla A\'B\'C\' konumuna taşımıştır. Kareli zeminde her karenin kenarı 1 birimdir. Bu taşıma, (a, b) kadar bir ötelemedir: a sağa doğru, b yukarı doğru birim sayısını gösterir; sola ve aşağı yönler negatif sayılarla ifade edilir.\nBuna göre, a × b çarpımı kaçtır?',
 dogru=-12,yan=[(-7,'Vektörün bileşenlerini çıkarmış: a − b = −4 − 3 = −7.','islem'),(-1,'Çarpım yerine toplamı (−4 + 3) hesaplamış.','dikkat'),(7,'Yönleri dikkate almadan |a| + |b| = 4 + 3 = 7 bulmuş.','dikkat'),(12,'Sola gitmenin negatif olduğunu unutup a = 4 almış; 4 × 3 = 12.','bilgi')],
 istenen='a × b çarpımı.',
 ip=['ABC üçgeninin bir köşesini ve onun karşılığını seç; kaç kare sağa/sola, kaç kare yukarı/aşağı gidilmiş?'],
 bilgi=[OTE],
 ad=[A('Karşılık gelen köşeleri seç','Öteleme tüm köşeleri aynı miktarda kaydırır; A ile A\' yeterlidir.','A → A\''),A('Yatay hareketi say','A noktasından A\' noktasına 4 kare sola gidilmiştir; sola negatiftir.','a = −4'),A('Dikey hareketi say','3 kare yukarı gidilmiştir; yukarı pozitiftir.','b = 3'),A('Çarpımı bul','İşaretlere dikkat et.','a × b = (−4) × 3 = −12')],
 puf='Ötelemede (a, b), bir köşeden karşılığına giden yatay (sağ +) ve dikey (yukarı +) birim sayısıdır; işaretleri unutma.',sekil=SK1)
# =================== 02 · iki yansıma · orta · hikâyeli ===================
kartla('K-GDN-02','Eksenlere göre ardışık yansıma','Önce x eksenine, sonra y eksenine yansıma orijine göre yansımadır: (x, y) → (−x, −y); uzaklık Pisagorla bulunur.','Yalnız tek yansımayı uygulamak; iki nokta arası uzaklıkta yalnız bir farkı almak ya da farkları toplamak.','orta',4,'ge-dn-yansima','Eksenlere göre ardışık yansıma','hikâyeli')
A2=(-3,4); B2=(A2[0],-A2[1]); C2=(-B2[0],B2[1]); assert B2==(-3,-4) and C2==(3,-4) and C2==(-A2[0],-A2[1])
d2=sqrt((A2[0]-C2[0])**2+(A2[1]-C2[1])**2); assert d2==10 and abs(A2[0]-C2[0])==6 and abs(A2[1]-C2[1])==8 and abs(A2[0])+abs(A2[1])==7 and sqrt(A2[0]**2+A2[1]**2)==5
s=.5; f=F(); izgara(f,-5,5,-5,5,s)
f.dot(G2(A2,s),1.6); f.vl('A',G2(A2,s),(-1,.5),.3)
SK2=f.svg()
q('0002',tipId='ge-dn-yansima',tip='Eksenlere göre ardışık yansıma',z='orta',alt='Ardışık Yansıma',kaz='Bir noktanın iki eksene göre ardışık yansımasını bulup iki nokta arasındaki uzaklığı hesaplar.',kalip='hikâyeli',
 kart='K-GDN-02 (ardışık yansıma) · A(−3, 4)',
 metin='Bir bilgisayar oyununda ekran, orijini O olan bir koordinat düzlemi olarak modellenmiştir ve eksenler üzerindeki her bölme 1 birimdir. Şekilde A noktasında bulunan karakter, önce x eksenine göre yansıtılarak B noktasına, ardından B noktasındaki karakter y eksenine göre yansıtılarak C noktasına gönderiliyor.\nBuna göre, |AC| kaç birimdir?',
 dogru=10,yan=[(5,'Yalnız |OA| uzaklığını (karakterin orijine uzaklığı) bulmuş.','dikkat'),(6,'Yalnız apsis farkını (|−3 − 3| = 6) almış.','dikkat'),(7,'A noktasının koordinatlarının mutlak değerlerini toplamış: 3 + 4 = 7.','dikkat'),(8,'Yalnız ordinat farkını (|4 − (−4)| = 8) almış.','dikkat')],
 istenen='|AC| uzunluğu (birim).',
 ip=['A noktasının koordinatlarını şekilden oku. İki yansımayı sırayla uygulayınca C noktası A noktasına göre nerede olur?'],
 bilgi=[YAN,PIS],
 ad=[A('A noktasını oku','Şekilde A, x = −3 ve y = 4 noktasındadır.','A(−3, 4)'),A('x eksenine göre yansı','Ordinatın işareti değişir.','B(−3, −4)'),A('y eksenine göre yansı','Apsisin işareti değişir.','C(3, −4)'),A('Uzaklığı hesapla','Apsis farkı 6, ordinat farkı 8; Pisagor uygula.','|AC|² = 6² + 8² = 100 → |AC| = 10')],
 puf='x ekseni ve ardından y eksenine yansıma, orijine göre yansımadır: (x, y) → (−x, −y). Bu durumda |AC| = 2 × |OA|.',sekil=SK2)
# =================== 03 · y=x yansıma · kolay ===================
kartla('K-GDN-03','y = x doğrusuna göre yansıma','y = x doğrusuna göre yansımada koordinatlar yer değiştirir: (x, y) → (y, x).','Koordinatları yer değiştirmemek; x eksenine ya da y eksenine göre yansıma yapmak; y = −x ile karıştırmak.','kolay',3,'ge-dn-yansima-yx','y = x doğrusuna göre yansıma')
T3=[(1,5),(1,2),(5,2)]; T3i=[(p[1],p[0]) for p in T3]; C3=T3[2]; C3i=T3i[2]
assert C3i==(2,5) and C3i[0]-C3i[1]==-3 and C3[0]-C3[1]==3 and (C3[0]-(-C3[1]))==7 and (-C3[0])-C3[1]==-7 and C3i[0]*C3i[1]==10
s=.5; f=F(); izgara(f,-1,7,-1,7,s)
f.line(G2((-.7,-.7),s),G2((6.8,6.8),s),'dashed'); f.node(G2((5.3,6.3),s),'$y=x$')
f.fill([G2(p,s) for p in T3],'fill=vurgu!20'); f.poly([G2(p,s) for p in T3],'thick')
for k,p,dv in [('A',T3[0],(-1,.5)),('B',T3[1],(-1,-1)),('C',T3[2],(1,-.6))]: f.vl(k,G2(p,s),dv,.3); f.dot(G2(p,s),1.4)
SK3=f.svg()
q('0003',tipId='ge-dn-yansima-yx',tip='y = x doğrusuna göre yansıma',z='kolay',alt='y = x Yansıması',kaz='Bir noktanın y = x doğrusuna göre yansımasının koordinatlarını bulur.',
 kart='K-GDN-03 (y = x yansıması) · C(5, 2)',
 metin='Şekilde köşeleri koordinat düzleminin ızgara noktalarında olan ABC üçgeni ve y = x doğrusu verilmiştir. ABC üçgeninin y = x doğrusuna göre yansıması olan üçgen A\'B\'C\' dür. C\' noktasının koordinatları (m, n) ile gösterilmektedir. Üçgenin köşelerinin koordinatları, ızgara çizgilerinden okunabilir.\nBuna göre, m − n farkı kaçtır?',
 dogru=-3,yan=[(-7,'y eksenine göre yansıtmış: C\'(−5, 2) için m − n = −7.','bilgi'),(3,'Yansımayı uygulamamış: C(5, 2) için 5 − 2 = 3.','dikkat'),(7,'x eksenine göre yansıtmış: C\'(5, −2) için m − n = 7.','bilgi'),(10,'m − n yerine çarpımı (m × n = 2 × 5) hesaplamış.','dikkat')],
 istenen='m − n farkı.',
 ip=['C noktasının koordinatlarını oku. y = x doğrusuna göre yansımada koordinatlara ne olur?'],
 bilgi=[YAN],
 ad=[A('C noktasını oku','Şekilde C noktası x = 5, y = 2 dedir.','C(5, 2)'),A('Yansımayı uygula','y = x doğrusuna göre yansımada apsis ve ordinat yer değiştirir.','(5, 2) → (2, 5), C\'(2, 5)'),A('Farkı bul','m = 2, n = 5.','m − n = 2 − 5 = −3')],
 puf='y = x doğrusuna göre yansımada noktanın koordinatları yer değiştirir; sonuç, şekilde doğrunun öte yanındaki simetriğidir.',sekil=SK3)
# =================== 04 · orijin etrafında dönme · orta ===================
kartla('K-GDN-04','Orijin etrafında 90° dönme','Saat yönünde 90° dönmede (x, y) → (y, −x); köşelerin yeni koordinatlarından orta nokta bulunur.','Dönme yönünü karıştırmak (saatin tersi); 180° almak; döndürmeden hesaplamak.','orta',4,'ge-dn-donme','Orijin etrafında 90° dönme')
A4,B4,C4=(1,2),(5,2),(5,6); rot=lambda p:(p[1],-p[0]); A4i,B4i,C4i=rot(A4),rot(B4),rot(C4)
M4=((A4i[0]+C4i[0])/2,(A4i[1]+C4i[1])/2); assert A4i==(2,-1) and C4i==(6,-5) and M4==(4,-3) and M4[0]+M4[1]==1
ccw=lambda p:(-p[1],p[0]); Mc=((ccw(A4)[0]+ccw(C4)[0])/2,(ccw(A4)[1]+ccw(C4)[1])/2); assert Mc==(-4,3) and sum(Mc)==-1
M180=((-A4[0]-C4[0])/2,(-A4[1]-C4[1])/2); assert M180==(-3,-4) and sum(M180)==-7
M0=((A4[0]+C4[0])/2,(A4[1]+C4[1])/2); assert M0==(3,4) and sum(M0)==7 and M4[0]==4
s=.45; f=F(); izgara(f,-2,7,-2,7,s)
f.fill([G2(p,s) for p in (A4,B4,C4)],'fill=vurgu!20'); f.poly([G2(p,s) for p in (A4,B4,C4)],'thick')
for k,p,dv in [('A',A4,(-1,-.6)),('B',B4,(1,-.6)),('C',C4,(0,1))]: f.vl(k,G2(p,s),dv,.3); f.dot(G2(p,s),1.4)
SK4=f.svg()
q('0004',tipId='ge-dn-donme',tip='Orijin etrafında 90° dönme',z='orta',alt='90° Dönme',kaz='Bir üçgeni orijin etrafında 90° döndürüp köşelerin yeni koordinatlarıyla orta nokta hesaplar.',
 kart='K-GDN-04 (orijin etrafında dönme) · saat yönünde 90°',
 metin='Şekilde köşeleri ızgara noktalarında olan ABC üçgeni verilmiştir. Bu üçgen, orijin etrafında saat yönünde 90° döndürüldüğünde A\'B\'C\' üçgeni elde ediliyor. [A\'C\'] doğru parçasının orta noktası M(p, r) dir. Üçgenin köşelerinin koordinatları, eksenlerdeki bölmelerden okunabilir.\nBuna göre, p + r toplamı kaçtır?',
 dogru=1,yan=[(-7,'180° dönmüş: M(−3, −4) için p + r = −7.','dikkat'),(-1,'Saatin tersi yönünde döndürmüş: M(−4, 3) için p + r = −1.','dikkat'),(4,'Yalnız apsisi (p = 4) almış, r yi eklememiş.','dikkat'),(7,'Dönme uygulamamış: orta nokta (3, 4) için 3 + 4 = 7.','dikkat')],
 istenen='p + r toplamı.',
 ip=['A ve C noktalarının koordinatlarını oku. Saat yönünde 90° dönmede bir noktanın koordinatları nasıl değişir?'],
 bilgi=[DON],
 ad=[A('A ve C yi oku','Şekilde A(1, 2) ve C(5, 6) dır.','A(1, 2), C(5, 6)'),A('Saat yönünde 90° döndür','(x, y) → (y, −x) kuralını uygula.','A\'(2, −1), C\'(6, −5)'),A('Orta noktayı bul','Koordinatların ortalamasını al.','M((2 + 6) ÷ 2, (−1 − 5) ÷ 2) = (4, −3)'),A('Toplamı hesapla','p = 4, r = −3.','p + r = 1')],
 puf='Saat yönünde 90° dönme: (x, y) → (y, −x); saatin tersi yönünde: (x, y) → (−y, x). Yönü şekilde kontrol et.',sekil=SK4)
# =================== 05 · simetri ekseni · orta ===================
kartla('K-GDN-05','Simetri ekseni sayısı','Dikdörtgenin 2, ikizkenar yamuğun 1, düzgün altıgenin 6 simetri ekseni vardır.','Dikdörtgene 4 eksen vermek; yamuğa 0 ya da 2 eksen vermek; altıgene 3 eksen vermek.','orta',3,'ge-dn-simetri','Şekillerin simetri ekseni sayısı')
SE={'dikdörtgen':2,'ikizkenar yamuk':1,'düzgün altıgen':6}; assert sum(SE.values())==9
assert 2+1+3==6 and 4+1+6==11 and 2+0+6==8 and 2+2+3==7
f=F()
# I dikdörtgen
w,h=2.6,1.7; R1=[(0,0),(w,0),(w,h),(0,h)]
f.poly(R1,'thick'); [f.dik(R1[i],R1[(i+1)%4],R1[(i-1)%4],.2) for i in range(4)]
f.node((w/2,-.4),'I')
# II düzgün altıgen
cx=w+1.5; rr=1.05; HX=[(cx+rr*cos(radians(60*i)),h/2+rr*sin(radians(60*i))) for i in range(6)]
for i in range(6): assert abs(dist(HX[i],HX[(i+1)%6])-rr)<1e-9
f.poly(HX,'thick'); [f.tick(HX[i],HX[(i+1)%6]) for i in range(6)]
f.node((cx,-.4),'II')
# III ikizkenar yamuk
x0=cx+rr+1.0; bb,tt,hh=2.7,1.5,1.5; TZ=[(x0,0),(x0+bb,0),(x0+bb-(bb-tt)/2,hh),(x0+(bb-tt)/2,hh)]
assert abs(dist(TZ[1],TZ[2])-dist(TZ[0],TZ[3]))<1e-9
f.poly(TZ,'thick'); f.tick(TZ[1],TZ[2]); f.tick(TZ[0],TZ[3]); f.par(TZ[0],TZ[1]); f.par(TZ[3],TZ[2])
f.node((x0+bb/2,-.4),'III')
SK5=f.svg()
q('0005',tipId='ge-dn-simetri',tip='Şekillerin simetri ekseni sayısı',z='orta',alt='Simetri Ekseni',kaz='Dikdörtgen, düzgün altıgen ve ikizkenar yamuğun simetri eksenlerini sayarak toplar.',
 kart='K-GDN-05 (simetri ekseni) · dikdörtgen, ikizkenar yamuk, düzgün altıgen',
 metin='Şekilde birer dikdörtgen (kare değildir), düzgün altıgen ve ikizkenar yamuk çizilmiştir. Şekillerdeki dik açı, eşit kenar ve paralel kenar işaretleri doğrudur. Bir şeklin simetri ekseni, şekli katlayınca iki yarısı birbiriyle tam çakışan doğrudur.\nBuna göre, I, II ve III numaralı şekillerin simetri eksenlerinin sayıları toplamı kaçtır?',
 dogru=9,yan=[(6,'Altıgene yalnız 3 eksen vermiş (köşegen eksenleri ya da kenar orta dikmeleri); toplam 2 + 3 + 1 = 6.','bilgi'),(7,'Altıgene 3, yamuğa 2 eksen vermiş: 2 + 3 + 2 = 7.','bilgi'),(8,'İkizkenar yamuğun simetri ekseni olmadığını sanmış: 2 + 6 + 0 = 8.','bilgi'),(11,'Dikdörtgene köşegenlerini de eksen sayıp 4 eksen vermiş: 4 + 6 + 1 = 11.','bilgi')],
 istenen='Simetri eksenlerinin sayıları toplamı.',
 ip=['Her şekli ayrı ayrı düşün: hangi doğrular boyunca katlayınca iki yarım üst üste çakışır? Köşegenler eksen olur mu?'],
 bilgi=[SIM],
 ad=[A('I numaralı şekli incele','Dikdörtgenin yalnızca karşılıklı kenarların orta dikmeleri eksendir; köşegenleri eksen değildir.','2 eksen'),A('II numaralı şekli incele','Düzgün altıgende 3 eksen köşelerden, 3 eksen kenar orta noktalarından geçer.','6 eksen'),A('III numaralı şekli incele','İkizkenar yamukta yalnız tabanların orta noktalarını birleştiren doğru eksendir.','1 eksen'),A('Topla','Üçünün toplamı.','2 + 6 + 1 = 9')],
 puf='Düzgün n-genin n ekseni vardır; dikdörtgenin 2, ikizkenar yamuğun 1 ekseni vardır; paralelkenarın (eşkenar değilse) hiç yoktur.',sekil=SK5)
# =================== 06 · bir nokta etrafında dönme · zor ===================
kartla('K-GDN-06','Bir nokta etrafında dönme','Dönme merkezine göre yer farkı döndürülür; dönmede merkeze uzaklık korunur, iki nokta arası uzaklık Pisagorla bulunur.','Dönme merkezini orijin sanmak; yönü karıştırmak; 180° almak; dik kenarları toplamak.','zor',5,'ge-dn-donme-nokta','Bir nokta etrafında 90° dönme ve uzaklık')
A6,B6,C6,D6=(4,4),(8,7),(7,5),(3,2)
assert (B6[0]-A6[0],B6[1]-A6[1])==(D6[0]-C6[0],D6[1]-C6[1])*1 or (B6[0]-A6[0],B6[1]-A6[1])==(-(D6[0]-C6[0]),-(D6[1]-C6[1])) and (A6[0]-D6[0],A6[1]-D6[1])==(B6[0]-C6[0],B6[1]-C6[1])
v=(D6[0]-C6[0],D6[1]-C6[1]); assert v==(-4,-3) and ln(v)==5
vr=(v[1],-v[0]); assert vr==(-3,4); D6r=(C6[0]+vr[0],C6[1]+vr[1]); assert D6r==(4,9)
dd=sqrt((D6r[0]-D6[0])**2+(D6r[1]-D6[1])**2); assert abs(dd-5*sqrt(2))<1e-9 and abs(dd*dd-50)<1e-9 and D6r[1]-D6[1]==7
assert abs(dist(C6,D6)-5)<1e-9 and 4+3==7 and 2*5==10
s=.5; f=F(); gzemin(f,10,9,s)
f.fill([G2(p,s) for p in (A6,B6,C6,D6)],'fill=vurgu!18'); f.poly([G2(p,s) for p in (A6,B6,C6,D6)],'thick')
for k,p,dv in [('A',A6,(-1,.6)),('B',B6,(1,.6)),('C',C6,(1,-.4)),('D',D6,(-1,-.6))]: f.vl(k,G2(p,s),dv,.3); f.dot(G2(p,s),1.4)
SK6=f.svg()
q('0006',tipId='ge-dn-donme-nokta',tip='Bir nokta etrafında 90° dönme ve uzaklık',z='zor',alt='Merkezli Dönme',kaz='Bir noktayı başka bir nokta etrafında 90° döndürüp ilk ve son konumları arasındaki uzaklığı hesaplar.',
 kart='K-GDN-06 (merkezli dönme) · C merkez, D\' = D nin dönmüşü',
 metin='Kareli zeminde (her karenin kenarı 1 birimdir) şekildeki ABCD paralelkenarı çiziliyor. Bu paralelkenar, C köşesi etrafında saat yönünde 90° döndürülerek A\'B\'C\'D\' paralelkenarı elde ediliyor; D\', D köşesinin dönmüş hâlidir. Paralelkenarın köşeleri, kareli zeminin çizgilerinin kesiştiği noktalardadır ve dönme sırasında şeklin ölçüleri değişmez.\nBuna göre, |DD\'| kaç birimdir?',
 dogru='5√2',sira=['5','7','5√2','10','50'],yan=[('5','Dönme sonrası uzaklığı, merkeze uzaklığa eşit sanmış: |DD\'| yerine |CD| = 5.','dikkat'),('7','D\' noktasının D ye göre yalnızca dikey farkını (7 birim) uzaklık sanmış.','dikkat'),('10','180° döndürmüş gibi |DD\'| = 2 × |CD| = 10 almış.','dikkat'),('50','Pisagorda karekökü almayı unutmuş: |DD\'|² = 50.','islem')],
 istenen='|DD\'| uzunluğu (birim).',
 ip=['C merkezli dönmede D ile D\' noktaları için neler söylenebilir? Önce D nin C ye göre yerini kareli zeminden say.'],
 bilgi=[DONN,PIS],
 ad=[A('C den D ye gidişi bul','C den D ye gidiş: 4 kare sola, 3 kare aşağı.','C → D = (−4, −3), |CD| = 5'),A('Gidişi döndür','Saat yönünde 90° dönmede (u, v) → (v, −u) olur.','(−4, −3) → (−3, 4)'),A('D\' nün yerini bul','Dönmüş gidişi C nin koordinatlarına ekle: D\' noktası D den yatayda 1 kare sağda, dikeyde 7 kare yukarıdadır.','Δx = 1, Δy = 7'),A('Uzaklığı hesapla','Pisagor bağıntısı.','|DD\'|² = 1² + 7² = 50 → |DD\'| = 5√2')],
 puf='Merkezli dönmede önce noktanın merkeze göre yerini say, döndür, sonra merkeze ekle; uzaklık için Pisagoru unutma.',sekil=SK6)
bitir_geo('donusum','Dönüşüm Geometrisi')
