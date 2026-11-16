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
"""TYT Geometri · Piramit (6 soru; kardeş yok, ipucu 1). Koordinatlar hesaplanır, TikZ aynı değerlerden; her cevap/çeldirici assert edilir."""
P=Parti('piramit','Piramit','geo|Piramit',ders='TYT Geometri',idon='tytgeo')
HAC=B('Piramidin hacmi','V = (taban alanı × yükseklik) ÷ 3. Yükseklik, tepe noktasından tabana inen dik uzunluktur. Örnek: taban alanı 12, yükseklik 5 olan piramidin hacmi 12 × 5 ÷ 3 = 20')
PIS=B('Pisagor bağıntısı','dik üçgende dik kenarların kareleri toplamı hipotenüsün karesine eşittir. Örnek: 3, 4, 5 üçgeni için 3² + 4² = 5²')
YYY=B('Yan yüz yüksekliği','kare dik piramitte tepeden taban kenarının orta noktasına inen doğru parçasıdır; bir yan yüz, tabanı taban kenarı olan ikizkenar üçgendir')
ALANT=B('Yüzey alanı','piramidin tüm yüzey alanı = taban alanı + yan yüzlerin alanları toplamıdır. Üçgenin alanı = taban × yükseklik ÷ 2. Örnek: kenarı 4, yan yüz yüksekliği 6 olan kare piramitte 16 + 4 × (4 × 6 ÷ 2) = 64')
ESKEN=B('Eşkenar üçgenin alanı','kenarı a olan eşkenar üçgenin alanı (a² × √3) ÷ 4 tür. Düzgün dörtyüzlünün 4 yüzü, 6 ayrıtı vardır ve tüm ayrıtları eşittir. Örnek: a = 4 için alan 4√3')
ACIN=B('Açınım','kare dik piramidin açınımı bir kare ile onun dört kenarına yapışık dört eş ikizkenar üçgenden oluşur; üçgenin tabana ait yüksekliği yan yüz yüksekliğidir. Örnek: kare kenarı 8 ise üçgenlerin tabanı 8 dir')
def piram(a,h,sc,etiket,gizli_ho=True,M=False,etik_h=True,ek=''):
    V={'A':(0,0,0),'B':(a,0,0),'C':(a,a,0),'D':(0,a,0),'T':(a/2,a/2,h)}
    faces=[('A','B','C','D'),('A','B','T'),('B','C','T'),('C','D','T'),('D','A','T')]
    f=F(); Q,vis,hid=ciz_kati(f,V,faces,sc)
    assert frozenset('CD') in hid,hid
    O=mul(pr((a/2,a/2,0)),sc); T=Q['T']
    f.line(T,O,'dashed'); f.dot(O,1)
    ic=cen(list(Q.values()))
    f.vl('A',Q['A'],(-1,-.6),.3); f.vl('B',Q['B'],(1,-.6),.3); f.vl('C',Q['C'],(1,.3),.3); f.vl('D',Q['D'],(-1,.5),.36); f.vl('T',T,(0,1),.3)
    f.node((O[0]+.2,O[1]-.2),'$O$')
    return f,Q,O,T,ic
# =================== 01 · hacim · kolay ===================
konu('geo|Piramit','Piramit')
kartla('K-GPM-01','Kare dik piramidin hacmi','Hacim = taban alanı × yükseklik ÷ 3; taban kare olduğundan taban alanı kenarın karesidir.','1/3 çarpanını unutmak; taban alanı yerine çevre ya da kenar kullanmak.','kolay',2,'ge-pm-hacim','Kare dik piramidin hacmi')
a1,h1=6,10; V1=a1*a1*h1//3; assert V1==120 and a1*a1*h1==360 and a1*a1*h1/2==180 and 4*a1*h1//3==80 and a1*h1//3==20
f,Q,O,T,ic=piram(a1,h1,.34,None)
f.sl('$6$',Q['A'],Q['B'],ic,.3)
f.node((T[0]+.28,O[1]+(T[1]-O[1])*.3),'$10$')
SK1=f.svg()
q('0001',tipId='ge-pm-hacim',tip='Kare dik piramidin hacmi',z='kolay',alt='Hacim',kaz='Kare dik piramidin hacmini taban alanı ve yükseklikten hesaplar.',
 kart='K-GPM-01 (hacim) · taban kenarı ve yükseklikten hacim',
 metin='Şekildeki T tepeli ABCD kare dik piramidinde O noktası, tabanın köşegenlerinin kesişim noktasıdır ve [TO] doğru parçası tabana diktir. Taban kenarı ile piramidin yüksekliği cm cinsinden şekilde verilmiştir. Görünmeyen kenarlar kesikli çizgiyle gösterilmiştir.\nBuna göre, bu piramidin hacmi kaç cm³ tür?',
 dogru=120,yan=[(20,'Taban alanı yerine taban kenarını (6) alıp 6 × 10 ÷ 3 = 20 bulmuş.','bilgi'),(80,'Taban alanı yerine tabanın çevresini (24) alıp 24 × 10 ÷ 3 = 80 bulmuş.','bilgi'),(180,'Üçe değil ikiye bölmüş: 36 × 10 ÷ 2 = 180.','bilgi'),(360,'Hacim formülündeki 1/3 çarpanını unutmuş: 36 × 10 = 360.','bilgi')],
 istenen='Piramidin hacmi (cm³).',
 ip=['Hacim formülüne girecek iki büyüklük nedir? Tabanın kare olduğunu kullanarak birini bul.'],
 bilgi=[HAC],
 ad=[A('Verileri oku','Taban kenarı 6 cm, yükseklik |TO| = 10 cm dir.','a = 6, h = 10'),A('Taban alanını bul','Taban kare olduğundan alanı kenarın karesidir.','6 × 6 = 36 cm²'),A('Hacmi hesapla','Piramitte hacim, taban alanı ile yüksekliğin çarpımının üçte biridir.','36 × 10 ÷ 3 = 120 cm³')],
 puf='Piramitte hacim her zaman taban alanı × yükseklik ÷ 3 tür; yükseklik tabana dik olan |TO| dur.',sekil=SK1)
# =================== 02 · tabana paralel kesit · kolay ===================
kartla('K-GPM-02','Tabana paralel kesit','Yüksekliğin ortasından tabana paralel kesit, tabana benzerdir: kenar oranı 1/2, alan oranı 1/4.','Alan oranı yerine kenar oranını almak (1/2); taban alanını yazmak; çevreyle karıştırmak.','kolay',3,'ge-pm-kesit','Tabana paralel kesitin alanı')
a2,h2=12,10; ke=a2//2; assert ke*ke==36 and a2*a2//2==72 and a2*a2==144 and 4*ke==24 and a2*a2//3==48 and a2*a2*2//3==96 and ke==6
V2={'A':(0,0,0),'B':(a2,0,0),'C':(a2,a2,0),'D':(0,a2,0),'T':(a2/2,a2/2,h2)}
f=F(); Q,vis,hid=ciz_kati(f,V2,[('A','B','C','D'),('A','B','T'),('B','C','T'),('C','D','T'),('D','A','T')],.3)
assert frozenset('CD') in hid
Kp={k:lerp(V2[k],V2['T'],.5) for k in 'ABCD'}
for k in 'ABCD': assert abs(Kp[k][2]-h2/2)<1e-9
assert abs(dist(Kp['A'],Kp['B'])-ke)<1e-9
KQ={k:mul(pr(Kp[k]),.3) for k in 'ABCD'}
f.o.insert(0,'\\fill[fill=vurgu!25] '+' -- '.join(pt(KQ[k]) for k in 'ABCD')+' -- cycle;')
f.line(KQ['A'],KQ['B'],'thick'); f.line(KQ['B'],KQ['C'],'thick'); f.line(KQ['C'],KQ['D'],'thick,dashed'); f.line(KQ['D'],KQ['A'],'thick,dashed')
O=mul(pr((a2/2,a2/2,0)),.3); T=Q['T']; f.line(T,O,'dashed'); f.dot(O,1)
ic=cen(list(Q.values()))
f.vl('A',Q['A'],(-1,-.6),.3); f.vl('B',Q['B'],(1,-.6),.3); f.vl('C',Q['C'],(1,.3),.3); f.vl('D',Q['D'],(-1,.5),.36); f.vl('T',T,(0,1),.3)
f.node((O[0]+.22,O[1]-.2),'$O$')
f.sl('$12$',Q['A'],Q['B'],ic,.3)
SK2=f.svg()
q('0002',tipId='ge-pm-kesit',tip='Tabana paralel kesitin alanı',z='kolay',alt='Paralel Kesit',kaz='Yüksekliğin orta noktasından tabana paralel kesilen piramitte kesit alanını benzerlikle bulur.',
 kart='K-GPM-02 (paralel kesit) · taban kenarı 12, kesit yüksekliğin ortasında',
 metin='Şekildeki T tepeli ABCD kare dik piramidinin taban kenarı cm cinsinden verilmiştir. Piramit, [TO] yüksekliğinin orta noktasından geçen ve tabana paralel olan bir düzlemle kesilmiştir. Oluşan kesit, şekilde taralı olarak gösterilmiştir; görünmeyen kenarlar kesikli çizgiyle gösterilmiştir.\nBuna göre, taralı kesitin alanı kaç cm² dir?',
 dogru=36,yan=[(48,'Alan oranını 1/3 almış: 144 ÷ 3 = 48.','bilgi'),(72,'Alan oranını kenar oranıyla (1/2) aynı sanmış: 144 ÷ 2 = 72.','bilgi'),(96,'Kenar oranını 2/3 sanıp alanı 144 × 2 ÷ 3 = 96 bulmuş.','bilgi'),(144,'Kesit yerine taban alanını (12 × 12) işaretlemiş.','dikkat')],
 istenen='Taralı kesitin alanı (cm²).',
 ip=['Kesit düzlemi tabana paralel olduğuna göre kesit ile tabanın şekilleri arasında nasıl bir ilişki vardır? Kenarlar hangi oranda küçülür?'],
 bilgi=[B('Paralel kesit','piramidi tabana paralel bir düzlemle keserseniz kesit tabana benzer olur; benzerlik oranı, tepeden olan uzaklıkların oranıdır ve alanlar oranı benzerlik oranının karesidir. Örnek: oran 1/3 ise alan oranı 1/9 dur')],
 ad=[A('Benzerlik oranını bul','Kesit, tepeden yüksekliğin yarısı kadar uzaklıktadır.','Kenar oranı = 1/2'),A('Kesit kenarını bul','Kesit de bir karedir.','12 × 1/2 = 6 cm'),A('Alanı hesapla','Kare alanı kenarın karesidir.','6 × 6 = 36 cm²')],
 puf='Tabana paralel kesitte kenarlar benzerlik oranıyla, alanlar oranın karesiyle değişir.',sekil=SK2)
# =================== 03 · yüzey alanı · orta · hikâyeli ===================
kartla('K-GPM-03','Yüzey alanı (çadır)','Tüm yüzey = taban + 4 eş üçgen; yan yüz yüksekliği verilmiştir.','Yalnız yanal alanı ya da bir yan yüzü saymak; zemini eklemeyi unutmak.','orta',3,'ge-pm-yuzey','Kare dik piramidin yüzey alanı','hikâyeli')
a3,ap3=6,5; S3=a3*a3+4*a3*ap3//2
assert S3==96 and 4*a3*ap3//2==60 and a3*a3==36 and a3*a3+a3*ap3//2==51 and a3*a3+2*a3*ap3//2==66
f,Q,O,T,ic=piram(a3,4,.55,None)
M=mid(Q['A'],Q['B']); f.line(T,M); f.dot(M,1); f.node((M[0]-.05,M[1]-.3),'$M$')
f.node(add(lerp(Q['A'],Q['B'],.82),(0,-.3)),'$6$')
f.node(add(lerp(T,M,.72),(.2,-.02)),'$5$')
SK3=f.svg()
q('0003',tipId='ge-pm-yuzey',tip='Kare dik piramidin yüzey alanı',z='orta',alt='Yüzey Alanı',kaz='Yan yüz yüksekliği verilen kare dik piramidin tüm yüzey alanını hesaplar.',kalip='hikâyeli',
 kart='K-GPM-03 (yüzey alanı) · çadır, taban 6 m, yan yüz yüksekliği 5 m',
 metin='Bir kamp çadırı, şekildeki gibi kare dik piramit biçimindedir. M noktası [AB] kenarının orta noktasıdır; taban kenarı ile ABT yan yüzünün tabana ait yüksekliği olan [TM] metre cinsinden şekilde verilmiştir. Çadırın zemini dâhil bütün yüzeyleri bezle kaplanacaktır ve dikişlerden dolayı bez payı hesaba katılmayacaktır. Bezin her yüzeye eksiksiz ve kesintisiz serileceği varsayılmaktadır.\nBuna göre, çadırın yapımında kaç m² bez kullanılır?',
 dogru=96,yan=[(36,'Yalnız zemini (taban alanını) hesaplamış.','dikkat'),(51,'Zemine yalnız bir yan yüzü eklemiş: 36 + 15 = 51.','dikkat'),(60,'Yalnız dört yan yüzü hesaplamış, zemini eklememiş.','dikkat'),(66,'Zemine yalnız iki yan yüzü eklemiş: 36 + 30 = 66.','dikkat')],
 istenen='Kullanılacak bezin alanı (m²).',
 ip=['Çadırın yüzeyi hangi parçalardan oluşuyor? Her parçanın alanı için gereken uzunluklar şekilde verilmiş mi?'],
 bilgi=[ALANT],
 ad=[A('Bir yan yüzün alanı','Yan yüz, tabanı 6 ve tabana ait yüksekliği 5 olan üçgendir.','6 × 5 ÷ 2 = 15 m²'),A('Yanal alanı bul','Dört eş yan yüz vardır.','4 × 15 = 60 m²'),A('Zemini ekle','Zemin kare, kenarı 6 m.','36 + 60 = 96 m²')],
 puf='Yüzey alanı = taban + yan yüzler; çadır sorularında zemin dâhil mi değil mi dikkat et.',sekil=SK3)
# =================== 04 · düzgün dörtyüzlü · orta ===================
kartla('K-GPM-04','Düzgün dörtyüzlü','Yüzün alanından eşkenar üçgenin kenarı bulunur; dörtyüzlünün 6 ayrıtı eşittir.','Ayrıt sayısını 12 ya da 9 almak; yalnız bir yüzün çevresini hesaplamak; kenarı bulmadan kareyi vermek.','orta',3,'ge-pm-dortyuzlu','Düzgün dörtyüzlünün ayrıtları')
a4=6; assert a4*a4*3==9*3*4 and a4**2==36
# a^2 sqrt3/4 = 9 sqrt3 -> a^2=36
t=a4*sqrt(2/3); cx4,cy4=a4/2,a4*sqrt(3)/6; th=radians(-25)
def rot4(p): x,y=p[0]-cx4,p[1]-cy4; return (cx4+cos(th)*x-sin(th)*y,cy4+sin(th)*x+cos(th)*y,p[2])
V4={k:rot4(v) for k,v in {'A':(0,0,0),'B':(a4,0,0),'C':(a4/2,a4*sqrt(3)/2,0),'D':(a4/2,a4*sqrt(3)/6,t)}.items()}
fc4=[('A','B','C'),('A','B','D'),('B','C','D'),('A','C','D')]
for (x,y) in [('A','B'),('A','C'),('A','D'),('B','C'),('B','D'),('C','D')]: assert abs(dist(V4[x],V4[y])-a4)<1e-9
sc=.62
f=F(); vis,hid,_=katı(V4,fc4)
Q,vis,hid=ciz_kati(f,V4,fc4,sc)
gor=[fc for fc,v in vis.items() if v]; assert sorted(gor)==[('A','B','D'),('B','C','D')],gor; assert sorted(''.join(sorted(e)) for e in hid)==['AC']
tara=('A','B','D')
f.o.insert(0,'\\fill[fill=vurgu!22] '+' -- '.join(pt(Q[k]) for k in tara)+' -- cycle;')
ic=cen(list(Q.values()))
for k,dv in {'A':(-1,-.5),'B':(1,-.5),'C':(1,.3),'D':(0,1)}.items(): f.vl(k,Q[k],dv,.3)
f.node(add(cen([Q[k] for k in tara]),(-.1,-.1)),'$9\\sqrt{3}$')
SK4=f.svg()
q('0004',tipId='ge-pm-dortyuzlu',tip='Düzgün dörtyüzlünün ayrıtları',z='orta',alt='Düzgün Dörtyüzlü',kaz='Bir yüzünün alanı verilen düzgün dörtyüzlünün ayrıt uzunluğunu bulup tüm ayrıtlarının toplamını hesaplar.',
 kart='K-GPM-04 (düzgün dörtyüzlü) · yüz alanı 9√3, ayrıt toplamı',
 metin='Şekildeki ABCD düzgün dörtyüzlüsünün (tüm yüzleri eş eşkenar üçgendir) taralı yüzünün alanı cm² cinsinden gösterilmiştir. Düzgün dörtyüzlünün her ayrıtı birbirine eşittir ve görünmeyen kenar kesikli çizgiyle gösterilmiştir. Şekil, dörtyüzlünün eğik görünümüdür; bu yüzden uzunluklar şekil üzerinde birebir ölçülemez.\nBuna göre, bu dörtyüzlünün bütün ayrıtlarının uzunlukları toplamı kaç cm dir?',
 dogru=36,yan=[(18,'Yalnız taralı yüzün çevresini (3 × 6) bulmuş.','dikkat'),(54,'Dörtyüzlüyü üçgen prizma gibi düşünüp 9 ayrıt saymış: 9 × 6 = 54.','bilgi'),(72,'Dörtyüzlünün 12 ayrıtı olduğunu sanmış (küp ile karıştırmış): 12 × 6 = 72.','bilgi'),(216,'Kenar yerine a² = 36 değerini kullanıp 6 × 36 = 216 bulmuş.','islem')],
 istenen='Tüm ayrıtların uzunlukları toplamı (cm).',
 ip=['Bir yüz eşkenar üçgendir; alan formülünden ayrıtın uzunluğunu bulabilir misin? Dörtyüzlünün kaç ayrıtı var?'],
 bilgi=[ESKEN],
 ad=[A('Ayrıt uzunluğunu bul','Yüzler eşkenar üçgendir; alan formülünü verilen alana eşitle.','a² × √3 ÷ 4 = 9√3 → a² = 36 → a = 6 cm'),A('Ayrıt sayısını belirle','Düzgün dörtyüzlünün 4 köşesi vardır; her iki köşe bir ayrıtla birleşir.','4 köşe → 6 ayrıt'),A('Toplamı hesapla','Tüm ayrıtlar eşit uzunluktadır.','6 × 6 = 36 cm')],
 puf='Düzgün dörtyüzlünün 4 yüzü, 6 ayrıtı, 4 köşesi vardır; ayrıt uzunluğu yüz alanından bulunur.',sekil=SK4)
# =================== 05 · açınım · zor ===================
kartla('K-GPM-05','Piramit açınımı','Açınımdan taban kenarı ve yan yüz yüksekliği okunur; yükseklik Pisagorla bulunup hacim hesaplanır.','Yan yüz yüksekliğini piramidin yüksekliği sanmak; 1/3 çarpanını unutmak.','zor',4,'ge-pm-acinim','Kare dik piramidin açınımı ve hacmi')
a5,ap5=12,10; h5=int(sqrt(ap5**2-(a5/2)**2)); V5=a5*a5*h5//3
assert h5==8 and a5*a5*(a5//2)//3==288 and V5==384 and a5*a5*ap5//3==480 and a5*a5*h5==1152 and a5*a5*h5//2==576 and a5*a5*(ap5-a5//2)//3==192 and a5*a5==144
s5=.2; f=F()
Aa=(0,0); Bb=(a5*s5,0); Cc=(a5*s5,a5*s5); Dd=(0,a5*s5)
T1=(a5*s5/2,-ap5*s5); T2=(a5*s5+ap5*s5,a5*s5/2); T3=(a5*s5/2,a5*s5+ap5*s5); T4=(-ap5*s5,a5*s5/2)
f.poly([Aa,Bb,Cc,Dd])
for (u,v,Tt) in [(Aa,Bb,T1),(Bb,Cc,T2),(Cc,Dd,T3),(Dd,Aa,T4)]:
    f.line(u,Tt); f.line(v,Tt); f.tick(u,Tt); f.tick(v,Tt)
    assert abs(dist(u,Tt)-dist(v,Tt))<1e-9
Mr=mid(Bb,Cc); f.line(Mr,T2,'dashed'); f.dik(Mr,T2,Cc,.2)
assert abs(dist(Mr,T2)/s5-ap5)<1e-9
f.vl('A',Aa,(-1,-1),.3); f.vl('B',Bb,(1,-1),.3); f.vl('C',Cc,(1,1),.3); f.vl('D',Dd,(-1,1),.3)
for Tt,dv in [(T1,(0,-1)),(T2,(1,0)),(T3,(0,1)),(T4,(-1,0))]: f.vl('T',Tt,dv,.3)
f.node((a5*s5/2,.28),'$12$ cm'); f.node((a5*s5+ap5*s5/2,a5*s5/2+.27),'$10$ cm')
SK5=f.svg()
q('0005',tipId='ge-pm-acinim',tip='Kare dik piramidin açınımı ve hacmi',z='zor',alt='Piramit Açınımı',kaz='Açınımdan taban kenarı ve yan yüz yüksekliğini okuyup piramidin hacmini hesaplar.',
 kart='K-GPM-05 (açınım) · taban 12, yan yüz yüksekliği 10',
 metin='Şekilde, tabanı ABCD karesi olan bir kare dik piramidin açınımı verilmiştir. Dört yan yüz birbirine eş ikizkenar üçgenlerdir; karenin bir kenarı ile bir yan yüzün tabana ait yüksekliği cm cinsinden gösterilmiştir. Açınımda T ile gösterilen köşeler, piramit kurulunca tepe noktasında birleşir.\nBuna göre, bu piramidin hacmi kaç cm³ tür?',
 dogru=384,yan=[(144,'Hacim yerine taban alanını (12 × 12) işaretlemiş.','dikkat'),(192,'Yüksekliği 10 − 6 = 4 bularak 144 × 4 ÷ 3 = 192 hesaplamış.','bilgi'),(288,'Tabanın yarı kenarını (6) piramidin yüksekliği sanıp 144 × 6 ÷ 3 = 288 bulmuş.','bilgi'),(480,'Yan yüz yüksekliğini (10) piramidin yüksekliği sanıp 144 × 10 ÷ 3 = 480 bulmuş.','bilgi')],
 istenen='Piramidin hacmi (cm³).',
 ip=['Açınımdaki 10 cm hangi doğru parçasının uzunluğu: piramidin yüksekliği mi, yan yüz yüksekliği mi?'],
 bilgi=[ACIN,YYY,HAC],
 ad=[A('Açınımı oku','Karenin kenarı 12 cm; yan yüzün tabana ait yüksekliği 10 cm, yani yan yüz yüksekliğidir.','a = 12, yan yüz yüksekliği = 10'),A('Yüksekliği bul','Piramidin yüksekliği, yarı kenar 6 ve yan yüz yüksekliği 10 ile dik üçgen oluşturur.','h² = 10² − 6² = 64 → h = 8 cm'),A('Taban alanını bul','Taban kare.','12 × 12 = 144 cm²'),A('Hacmi hesapla','Taban alanı × yükseklik ÷ 3.','144 × 8 ÷ 3 = 384 cm³')],
 puf='Açınımdaki üçgenin yüksekliği, piramidin yüksekliği değil yan yüz yüksekliğidir; yüksekliği Pisagorla bul.',sekil=SK5)
# =================== 06 · yanal alan · zor · hikâyeli ===================
kartla('K-GPM-06','Hacimden yüksekliğe, yanal alan','Hacimden yükseklik bulunur, yükseklikten yan yüz yüksekliği, ondan yanal alan.','Yan yüz yüksekliği yerine yüksekliği kullanmak; hacim formülünde 3 ile çarpmayı unutmak.','zor',5,'ge-pm-yanal','Hacimden yanal alana','hikâyeli')
a6=9; V6=162; h6=3*V6//(a6*a6); ap6=sqrt(h6**2+(a6/2)**2); Y6=4*a6*ap6/2
assert h6==6 and ap6==7.5 and Y6==135 and 4*a6*h6/2==108 and 4*a6*ap6==270 and a6*a6+Y6==216 and V6==162
f,Q,O,T,ic=piram(a6,h6,.4,None)
f.sl('$9$',Q['A'],Q['B'],ic,.3)
SK6=f.svg()
q('0006',tipId='ge-pm-yanal',tip='Hacimden yanal alana',z='zor',alt='Yanal Alan',kaz='Hacminden piramidin yüksekliğini, ondan yan yüz yüksekliğini bulup yanal alanı hesaplar.',kalip='hikâyeli',
 kart='K-GPM-06 (yanal alan) · hacim 162 m³, taban kenarı 9 m',
 metin='Bir köy evinin çatı katı, şekildeki gibi tabanı kare olan bir dik piramit biçimindedir. Çatı katının hacmi 162 m³ tür ve taban kenarı metre cinsinden şekilde verilmiştir. Yalnızca dört yan yüzey kiremitle kaplanacaktır; taban kaplanmayacaktır.\nBuna göre, kaplanacak yüzeyin alanı kaç m² dir?',
 dogru=135,yan=[(216,'Tabanı da eklemiş: 81 + 135 = 216 (taban kaplanmayacak).','dikkat'),(108,'Yan yüz yüksekliği yerine piramidin yüksekliğini (6) kullanmış: 4 × 9 × 6 ÷ 2 = 108.','bilgi'),(162,'Yüzey alanı yerine verilen hacim değerini işaretlemiş.','dikkat'),(270,'Üçgenin alanındaki ikiye bölmeyi unutmuş: 4 × 9 × 7,5 = 270.','bilgi')],
 istenen='Kiremitle kaplanacak yüzeyin alanı (m²).',
 ip=['Yanal alan için önce eksik uzunlukları bulmalısın. Hacim formülünde bilinmeyen hangisi?'],
 bilgi=[HAC,YYY,ALANT],
 ad=[A('Yüksekliği bul','Hacim formülünü yüksekliği bilinmeyen olarak yaz.','162 = 9 × 9 × h ÷ 3 → h = 6 m'),A('Yan yüz yüksekliğini bul','Yükseklik 6, yarı kenar 4,5 olan dik üçgende Pisagor.','h’² = 6² + 4,5² = 56,25 → 7,5 m'),A('Bir yan yüzün alanı','Tabanı 9, yüksekliği 7,5 olan üçgen.','9 × 7,5 ÷ 2 = 33,75 m²'),A('Dört yüzü topla','Taban kaplanmayacağı için yalnız yan yüzler.','4 × 33,75 = 135 m²')],
 puf='Hacmi verilip yanal alan sorulursa sıra: yükseklik → yan yüz yüksekliği → yanal alan.',sekil=SK6)
bitir_geo('piramit','Piramit')
