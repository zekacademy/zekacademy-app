"""TYT Geometri · Noktanın Analitiği (hafif mod; kardeş yok, ipucu 1). Koordinatlar Python'da hesaplanır, TikZ gövdesi aynı değerlerden üretilir; her cevap ve çeldirici değeri assert edilir."""
import sys,os,math,json
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
from math import sin,cos,tan,radians,degrees,atan2,sqrt,pi
from fractions import Fraction as Fr
ONEK='noktaanalitik'
P=Parti(ONEK,'Noktanın Analitiği','geo|Noktanın Analitiği',ders='TYT Geometri',idon='tytgeo')
TIPK={}
def konu(k,ad): P.k=k; P.konu_adi=ad; H.KONU=ad
KY='ÖSYM 2018–2026 TYT Geometri soruları (yalnız mantık) · MEB 9–10. sınıf geometri'
def kartla(id,alt,fikir,tuzak,z,adim,tipId,tip,kalip='şekilli'):
    kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY); TIPK[tipId]=P.k
def q(no,ad,**k):
    kl=k.pop('kalip','şekilli'); mk(P,no,ad=ad,adim=len(ad),kalip=kl,**k)
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
    def vl(s,t,p,dv,d=.3): s.node(add(p,mul(un(dv),d)),f'${t}$')
    def arc(s,V,a,b,r,lab=None,lr=None,st=''):
        a1=degrees(atan2(a[1]-V[1],a[0]-V[0])); a2=degrees(atan2(b[1]-V[1],b[0]-V[0])); d=(a2-a1+180)%360-180
        s.o.append(f'\\draw[{st}] ({V[0]+r*cos(radians(a1)):.3f},{V[1]+r*sin(radians(a1)):.3f}) arc[start angle={a1:.2f},delta angle={d:.2f},radius={r}];')
        if lab: m=radians(a1+d/2); s.node((V[0]+lr*cos(m),V[1]+lr*sin(m)),lab)
    def body(s): return '\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'+'\n'.join(s.o)+'\n\\end{tikzpicture}'
    def svg(s): return tikz_svg(s.body())
class Pl(F):
    """Koordinat düzlemi: x0..x1, y0..y1 tamsayı ızgara; u = bir birimin cm karşılığı. Sayılar ızgaranın dış kenarında (çizgiye değmez)."""
    def __init__(s,x0,x1,y0,y1,u=.5,grid=True,ticks=True,step=None,o=(-.2,-.22)):
        F.__init__(s); s.u=u; s.x0,s.x1,s.y0,s.y1=x0,x1,y0,y1
        if step is None: step=1 if max(x1-x0,y1-y0)<=13 else 2
        if grid:
            for x in range(x0,x1+1): s.line((x*u,y0*u),(x*u,y1*u),'gray!55,thin')
            for y in range(y0,y1+1): s.line((x0*u,y*u),(x1*u,y*u),'gray!55,thin')
        s.raw(f'\\draw[-{{Stealth[length=2mm]}},thick] ({x0*u-.1:.3f},0) -- ({x1*u+.3:.3f},0);')
        s.raw(f'\\draw[-{{Stealth[length=2mm]}},thick] (0,{y0*u-.1:.3f}) -- (0,{y1*u+.3:.3f});')
        s.node((x1*u+.6,0),'$x$'); s.node((0,y1*u+.58),'$y$'); s.node(o,'\\footnotesize$O$')
        if ticks:
            for x in range(x0,x1+1):
                if x%step==0 and x!=0: s.node((x*u,y0*u-.3),f'\\footnotesize${x}$')
            for y in range(y0,y1+1):
                if y%step==0 and y!=0: s.node((x0*u-.33,y*u),f'\\footnotesize${y}$')
    def c(s,x,y): return (x*s.u,y*s.u)
    def dot(s,x,y,r=.075): s.raw(f'\\fill {pt(s.c(x,y))} circle ({r});')
    def lab(s,t,x,y,dx,dy,d=.3): s.vl(t,s.c(x,y),(dx,dy),d)
    def seg(s,a,b,st='thick'): s.line(s.c(*a),s.c(*b),st)
    def lin(s,a,b,t0=-1,t1=2,st='thick'):
        s.line(s.c(a[0]+t0*(b[0]-a[0]),a[1]+t0*(b[1]-a[1])),s.c(a[0]+t1*(b[0]-a[0]),a[1]+t1*(b[1]-a[1])),st)
    def pfill(s,ps,st='fill=vurgu!25'): s.fill([s.c(*p) for p in ps],st)
def kayit_yaz():
    for qq in P.ANA: qq['kardes']=None
    P.yaz(os.path.join(GD,ONEK+'-1.json'),os.path.join('/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/hn_analitik','bos-'+ONEK+'.json'))
    tipler={}
    for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=TIPK[c['tipId']]))['kartlar'].append(c['id'])
    json.dump(dict(konu=P.konu_adi,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 TYT Geometri çıkmış soruları (yalnız mantık), MEB 9–10. sınıf geometri müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar',ONEK+'.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler),'soru',len(P.ANA))
UZ=B('İki nokta arası uzaklık','A(x₁, y₁) ve B(x₂, y₂) için |AB| = √[(x₂ − x₁)² + (y₂ − y₁)²] dir. Örnek: (0, 1) ve (5, 13) noktaları arasındaki uzaklık √(25 + 144) = 13’tür')
ORTA=B('Orta nokta','A(x₁, y₁) ve B(x₂, y₂) noktalarını birleştiren doğru parçasının orta noktası ((x₁ + x₂)/2 , (y₁ + y₂)/2) dir. Örnek: (1, 0) ve (7, 10) noktalarının orta noktası (4, 5)’tir')
BOLEN=B('Doğru parçasını oranında bölen nokta','P ∈ [AB] ve |AP| : |PB| = m : n ise P = (n·A + m·B) / (m + n) dir (koordinatlar ayrı ayrı hesaplanır). Örnek: A(0, 0), B(10, 5) ve oran 2 : 3 ise P(4, 2)’dir')
AGIR=B('Ağırlık merkezi','köşeleri (x₁, y₁), (x₂, y₂), (x₃, y₃) olan üçgenin ağırlık merkezi ((x₁ + x₂ + x₃)/3 , (y₁ + y₂ + y₃)/3) dür. Örnek: köşeleri (0, 0), (9, 3), (3, 6) olan üçgenin ağırlık merkezi (4, 3)’tür')
ALAN=B('Alan hesabı','kareli zeminde çokgeni içine alan dikdörtgenden dışarıda kalan üçgenler çıkarılarak ya da köşe koordinatlarıyla alan formülü uygulanarak alan bulunur. Örnek: (0, 0), (4, 0), (0, 3) köşeli üçgenin alanı, 4 × 3 dikdörtgeninin yarısı olan 6’dır')
BOLGE=B('Dört bölge ve işaretler','analitik düzlem 1. bölge (+, +), 2. bölge (−, +), 3. bölge (−, −), 4. bölge (+, −) olmak üzere dört bölgeye ayrılır. Çarpımın ve farkın işareti, sayıların işaretinden bulunur. Örnek: (−2, 4) noktası 2. bölgededir ve (−2) × 4 = −8 < 0’dır')
PAR=B('Paralelkenarın köşegenleri','paralelkenarın köşegenleri birbirini ortalar; karşılıklı köşelerin koordinat toplamları eşittir: A + C = B + D. Örnek: ABCD paralelkenarında köşegenlerin kesişim noktası (3, 2) ve A(1, 1) ise C(5, 3)’tür')
konu('geo|Noktanın Analitiği','Noktanın Analitiği')

# ===== 01 uzaklık · kolay =====
kartla('K-GNA-01','İki nokta arası uzaklık','Izgaradan okunan iki noktanın yatay ve dikey farkları bulunur; uzaklık formülüyle (ya da 3-4-5 benzeri dik üçgenle) |AB| hesaplanır.','Farkları toplamak; karekökü almamak; yalnız dikey farkı vermek.','kolay',3,'ge-na-uzaklik','İki nokta arası uzaklık')
A1=(-3,-1); B1=(3,7); dx,dy=B1[0]-A1[0],B1[1]-A1[1]
assert (dx,dy)==(6,8) and dx*dx+dy*dy==100 and math.isqrt(100)==10 and dx+dy==14 and dy==8 and dx*dy==48
pl=Pl(-4,5,-2,8,.5); pl.seg(A1,B1); pl.dot(*A1); pl.dot(*B1); pl.lab('A',*A1,-1,-.5,.28); pl.lab('B',*B1,1,.5,.28)
SK1=pl.svg()
q('0001',tipId='ge-na-uzaklik',tip='İki nokta arası uzaklık',z='kolay',alt='Uzaklık Formülü',kaz='Koordinat düzleminde verilen iki nokta arasındaki uzaklığı hesaplar.',
 kart='K-GNA-01 (uzaklık) · ızgaradan okunan iki nokta',
 metin='Şekildeki ızgara, bir karesinin kenarı 1 birim olan bir analitik düzlemdir. Bu düzlemde A ve B noktaları işaretlenmiş ve [AB] doğru parçası çizilmiştir.\nBuna göre, |AB| kaç birimdir?',
 dogru=10,yan=[(14,'Yatay ve dikey farkları toplamış (6 + 8) ve uzaklık formülünü uygulamamış.','bilgi'),(100,'Farkların karelerini toplamış (36 + 64) ama karekökü almayı unutmuş.','islem'),(8,'Yalnız dikey farkı (|AB| nin y yönündeki izdüşümü) cevap vermiş.','dikkat'),(48,'Koordinat farklarını çarpmış (6 × 8) ve uzaklık formülünü kullanmamış.','bilgi')],
 istenen='|AB| uzaklığı (birim).',
 ip=['A ve B’nin koordinatlarını ızgaradan oku; x’ler arası ve y’ler arası farklarla bir dik üçgen kur.'],
 bilgi=[UZ],
 ad=[A('Koordinatları oku','Izgaradan iki noktanın koordinatlarını oku.','A(−3, −1) · B(3, 7)'),A('Farkları bul','Yatay ve dikey farklar dik üçgenin dik kenarlarıdır.','Δx = 3 − (−3) = 6 · Δy = 7 − (−1) = 8'),A('Uzaklığı hesapla','Pisagor bağıntısı ile hipotenüs bulunur.','|AB| = √(6² + 8²) = √100 = 10')],
 puf='Uzaklık sorularında koordinat farklarını bulup Pisagor uygula; farkları toplamak uzaklık vermez.',sekil=SK1)

# ===== 02 orta nokta · kolay · hikâyeli =====
kartla('K-GNA-02','Orta nokta','İki ucun koordinatları ızgaradan okunup ayrı ayrı toplanır ve ikiye bölünür.','Bölmeyi unutmak; farkı ikiye bölmek; bir koordinatta toplama, ötekinde çıkarma yapmak.','kolay',2,'ge-na-orta','Orta nokta koordinatları','hikâyeli')
A2=(-4,3); B2=(6,-1); M2=((A2[0]+B2[0])//2,(A2[1]+B2[1])//2); assert M2==(1,1) and (A2[0]+B2[0])%2==0
assert (A2[0]+B2[0],A2[1]+B2[1])==(2,2) and ((B2[0]-A2[0])//2,(B2[1]-A2[1])//2)==(5,-2) and (B2[0]-A2[0],B2[1]-A2[1])==(10,-4) and (M2[0],(A2[1]-B2[1])//2)==(1,2)
pl=Pl(-5,7,-2,4,.5); pl.seg(A2,B2); pl.dot(*A2); pl.dot(*B2); pl.lab('A',*A2,-1,.5,.28); pl.lab('B',*B2,1,-.5,.28)
SK2=pl.svg()
q('0002',tipId='ge-na-orta',tip='Orta nokta koordinatları',z='kolay',alt='Orta Nokta',kaz='İki noktanın koordinatlarından orta noktanın koordinatlarını bulur.',kalip='hikâyeli',
 kart='K-GNA-02 (orta nokta) · iki liman arasında şamandıra',
 metin='Şekildeki kareli zeminde A ve B limanları gösterilmiştir. İki liman arasında, bir karesinin kenarı 1 km olan haritada düz bir feribot hattı vardır. Hattın tam ortasına, M noktasına bir şamandıra bırakılacaktır.\nBuna göre, M noktasının koordinatları aşağıdakilerden hangisidir?',
 dogru='(1, 1)',sira=['(1, 1)','(1, 2)','(2, 2)','(5, −2)','(10, −4)'],
 yan=[('(2, 2)','Koordinatları ayrı ayrı toplamış (−4 + 6 ve 3 + (−1)) ama ikiye bölmemiş.','islem'),('(5, −2)','Orta nokta yerine koordinat farklarının yarısını (B − A) ÷ 2 almış.','bilgi'),('(10, −4)','Orta nokta yerine koordinat farklarını (B − A) almış, ikiye bölmemiş.','bilgi'),('(1, 2)','Apsislerde toplayıp ikiye bölmüş (1) ama ordinatlarda 3 − (−1) = 4 çıkarıp 2 bulmuş.','islem')],
 istenen='M noktasının koordinatları.',
 ip=['A ve B’nin koordinatlarını ızgaradan oku; iki noktanın tam ortası için her koordinatın ortalamasını düşün.'],
 bilgi=[ORTA],
 ad=[A('Koordinatları oku','Izgaradan iki liman noktasını oku.','A(−4, 3) · B(6, −1)'),A('Apsisin ortalaması','Orta noktanın apsisi iki apsisin ortalamasıdır.','(−4 + 6) ÷ 2 = 1'),A('Ordinatın ortalaması','Aynı işlemi ordinatlar için yap.','(3 + (−1)) ÷ 2 = 1 → M(1, 1)')],
 puf='Orta nokta, koordinatların ayrı ayrı ortalamasıdır; farkı değil toplamı yarıya böl.',sekil=SK2)

# ===== 03 bölen nokta · orta =====
kartla('K-GNA-03','Doğru parçasını bölen nokta','Verilen oran, parçayı kaç eş parçaya bölündüğünü gösterir; başlangıç noktasına toplam parçaya göre kesirle gidilir.','Oranı ters kullanmak; orta nokta almak; yalnız vektör farkını eklemek, başlangıç noktasını unutmak.','orta',3,'ge-na-bolen','Oranla bölen nokta','hikâyeli')
A3=(-2,-1); B3=(10,11); m3,n3=2,1
P3=((n3*A3[0]+m3*B3[0])//(m3+n3),(n3*A3[1]+m3*B3[1])//(m3+n3)); assert P3==(6,7) and (n3*A3[0]+m3*B3[0])%3==0 and (n3*A3[1]+m3*B3[1])%3==0
assert sum(P3)==13 and P3[0]==6
Pi3=((m3*A3[0]+n3*B3[0])//3,(m3*A3[1]+n3*B3[1])//3); assert Pi3==(2,3) and sum(Pi3)==5
Mo3=((A3[0]+B3[0])//2,(A3[1]+B3[1])//2); assert Mo3==(4,5) and sum(Mo3)==9
V3=((B3[0]-A3[0])*2//3,(B3[1]-A3[1])*2//3); assert V3==(8,8) and sum(V3)==16
assert abs(dist(P3,A3)/dist(B3,P3)-2)<1e-9
pl=Pl(-3,11,-2,12,.42); pl.seg(A3,B3); pl.dot(*A3); pl.dot(*B3); pl.lab('A',*A3,-1,-.4,.28); pl.lab('B',*B3,1,.4,.28)
SK3=pl.svg()
q('0003',tipId='ge-na-bolen',tip='Oranla bölen nokta',z='orta',alt='Bölen Nokta',kaz='Bir doğru parçasını verilen oranda bölen noktanın koordinatlarını bulur.',kalip='hikâyeli',
 kart='K-GNA-03 (bölen nokta) · |AP| : |PB| = 2 : 1, A(−2, −1), B(10, 11)',
 metin='Şekilde, bir doğa yürüyüşü parkurunun başlangıç noktası A ve bitiş noktası B gösterilmiştir; parkur A’dan B’ye düz bir çizgi boyunca uzanmaktadır. Parkur üzerine, |AP| : |PB| = 2 : 1 olacak biçimde bir mola noktası P kurulacaktır.\nP noktasının koordinatları (a, b) olduğuna göre, a + b kaçtır?',
 dogru=13,yan=[(5,'Oranı ters kullanmış (|AP| : |PB| = 1 : 2 gibi): P = (2, 3) → 5.','bilgi'),(6,'Yalnız P’nin apsisini (a = 6) hesaplayıp cevap vermiş; ordinatı eklememiş.','dikkat'),(9,'P’yi orta nokta almış: (4, 5) → 9.','bilgi'),(16,'A’dan B’ye koordinat farkının 2/3’ünü (8, 8) bulmuş, A’nın koordinatlarını eklemeyi unutmuş: 8 + 8 = 16.','islem')],
 istenen='a + b toplamı.',
 ip=['|AP| : |PB| = 2 : 1 ise [AB] kaç eş parçaya bölünmüş olur ve P, A’dan kaç parça uzaktadır?'],
 bilgi=[BOLEN],
 ad=[A('Koordinatları oku','Izgaradan A ve B’yi oku.','A(−2, −1) · B(10, 11)'),A('Parça sayısı','Oran 2 : 1 olduğundan [AB] 3 eş parçaya bölünür; |AP| iki parçadır.','|AP| = |AB| × 2/3'),A('P noktasını bul','A’dan B’ye gidişin üçte ikisi alınır.','P = ((1 × (−2) + 2 × 10) ÷ 3 , (1 × (−1) + 2 × 11) ÷ 3) = (6, 7)'),A('Toplamı yaz','a ile b’yi topla.','6 + 7 = 13')],
 puf='Oran m : n ise doğru parçası m + n eş parçaya ayrılır; başlangıçtan m parça ilerlenir. Başlangıç noktasını eklemeyi unutma.',sekil=SK3)

# ===== 04 ağırlık merkezi · orta =====
kartla('K-GNA-04','Ağırlık merkezi','Köşelerin koordinatları ızgaradan okunur; apsis ve ordinatlar ayrı ayrı toplanıp üçe bölünür.','Üçe bölmemek; ikiye bölmek; yalnız bir koordinatı vermek.','orta',3,'ge-na-agirlik','Üçgenin ağırlık merkezi','hikâyeli')
A4=(-2,0); B4=(6,1); C4=(2,8); G4=((A4[0]+B4[0]+C4[0])//3,(A4[1]+B4[1]+C4[1])//3)
assert (A4[0]+B4[0]+C4[0])%3==0 and (A4[1]+B4[1]+C4[1])%3==0 and G4==(2,3) and sum(G4)==5
assert (A4[0]+B4[0]+C4[0]+A4[1]+B4[1]+C4[1])==15 and Fr(15,2)==Fr(15,2) and alan([A4,B4,C4])>0
pl=Pl(-3,7,-1,9,.5); pl.poly if False else None
pl.raw('\\draw[thick] '+' -- '.join(pt(pl.c(*p)) for p in [A4,B4,C4])+' -- cycle;')
for p in (A4,B4,C4): pl.dot(*p)
pl.lab('A',*A4,-1,.8,.3); pl.lab('B',*B4,1,-.3,.28); pl.lab('C',*C4,0,1,.28)
SK4=pl.svg()
q('0004',tipId='ge-na-agirlik',tip='Üçgenin ağırlık merkezi',z='orta',alt='Ağırlık Merkezi',kaz='Köşeleri verilen üçgenin ağırlık merkezinin koordinatlarını bulur.',kalip='hikâyeli',
 kart='K-GNA-04 (ağırlık merkezi) · A(−2, 0), B(6, 1), C(2, 8)',
 metin='Kareli bir planda ABC üçgeni biçimindeki bir arsa gösterilmiştir. Arsanın ağırlık merkezine bir su kuyusu açılacaktır. Kuyunun bulunacağı G noktasının koordinatları (a, b) dir.\nBuna göre, a + b kaçtır?',
 dogru=5,yan=[(2,'Yalnız apsisi (a = 2) bulup ordinatı hesaplamamış.','dikkat'),(3,'Yalnız ordinatı (b = 3) bulup apsisi hesaplamamış.','dikkat'),(7.5,'Köşe koordinatlarını toplayıp 3 yerine 2’ye bölmüş: 15 ÷ 2 = 7,5.','bilgi'),(15,'Apsisleri ve ordinatları toplamış (6 + 9) ama üçe bölmemiş.','islem')],
 istenen='a + b toplamı.',
 ip=['Köşelerin koordinatlarını ızgaradan oku. Ağırlık merkezi üç köşenin “ortalaması”dır.'],
 bilgi=[AGIR],
 ad=[A('Köşeleri oku','Izgaradan üç köşenin koordinatlarını oku.','A(−2, 0) · B(6, 1) · C(2, 8)'),A('Apsisin ortalaması','Üç apsisin toplamını 3’e böl.','a = (−2 + 6 + 2) ÷ 3 = 2'),A('Ordinatın ortalaması','Üç ordinatın toplamını 3’e böl.','b = (0 + 1 + 8) ÷ 3 = 3'),A('Toplamı yaz','a ile b’yi topla.','2 + 3 = 5')],
 puf='Ağırlık merkezi, üç köşenin koordinatlarının ayrı ayrı aritmetik ortalamasıdır; ikiye değil üçe böl.',sekil=SK4)

# ===== 05 alan · orta · hikâyeli =====
kartla('K-GNA-05','Dörtgenin alanı (kareli zemin)','Köşeleri ızgaradan okunan dörtgenin alanı, dikdörtgenden köşe üçgenleri çıkarılarak ya da köşegen formülüyle bulunur.','Dörtgeni saran dikdörtgenin alanını vermek; yarıya bölmeyi unutmak; yalnız bir üçgenin alanını vermek.','orta',4,'ge-na-alan','Köşeleri verilen çokgenin alanı','hikâyeli')
A5=(4,1); B5=(8,4); C5=(5,6); D5=(1,5)
S5=[A5,B5,C5,D5]; al5=alan(S5); assert al5==18
def cr(o,a,b): return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
assert all(cr(S5[i],S5[(i+1)%4],S5[(i+2)%4])>0 for i in range(4))
bb=(max(p[0] for p in S5)-min(p[0] for p in S5))*(max(p[1] for p in S5)-min(p[1] for p in S5)); assert bb==35
kt=[alan([A5,(8,1),B5]),alan([B5,(8,6),C5]),alan([C5,(1,6),D5]),alan([D5,(1,1),A5])]; assert kt==[6,3,2,6] and sum(kt)==17 and bb-sum(kt)==al5
assert bb-(sum(kt)-6)==24 and 2*al5==36
pl=Pl(0,9,0,7,.5); pl.pfill(S5,'fill=vurgu!20'); pl.raw('\\draw[thick] '+' -- '.join(pt(pl.c(*p)) for p in S5)+' -- cycle;')
for p in S5: pl.dot(*p)
pl.lab('A',*A5,.3,-1,.28); pl.lab('B',*B5,1,-.3,.28); pl.lab('C',*C5,.3,1,.28); pl.lab('D',*D5,-1,.3,.28)
SK5=pl.svg()
q('0005',tipId='ge-na-alan',tip='Köşeleri verilen çokgenin alanı',z='orta',alt='Dörtgenin Alanı',kaz='Köşe koordinatları verilen dörtgenin alanını kareli zeminde hesaplar.',kalip='hikâyeli',
 kart='K-GNA-05 (alan, kareli zemin) · köşeleri saran dikdörtgen ve dört köşe üçgeni',
 metin='Şekildeki kareli zeminin her karesinin kenarı 1 m dir. Bir belediye, köşeleri A, B, C ve D olan dörtgen biçimindeki bu alana çim ekecektir. Çim ekilecek bölge şekilde boyalı olarak gösterilmiştir.\nBuna göre, çim ekilecek bölgenin alanı kaç m²’dir?',
 dogru=18,yan=[(17,'Köşelerde kalan dört üçgenin alanları toplamını (6 + 3 + 2 + 6) cevap sanmış; dikdörtgenden çıkarmamış.','dikkat'),(24,'Dikdörtgenden dört üçgenden yalnız üçünü çıkarmış (35 − 11), 6 m² lik bir köşe üçgenini atlamış.','dikkat'),(35,'Dörtgenin köşelerini saran dikdörtgenin alanını (7 × 5) cevap vermiş.','bilgi'),(36,'Çapraz çarpımları toplayıp ikiye bölmeyi unutmuş (alan formülünde 1/2 katsayısı).','islem')],
 istenen='Dörtgenin alanı (m²).',
 ip=['Dörtgeni bir köşegenle iki üçgene ayırabilir ya da köşeleri saran bir dikdörtgenden köşelerdeki üçgenleri çıkarabilirsin.'],
 bilgi=[ALAN],
 ad=[A('Köşeleri oku','Izgaradan köşe koordinatlarını oku.','A(4, 1) · B(8, 4) · C(5, 6) · D(1, 5)'),A('Saran dikdörtgen','Dörtgeni içine alan dikdörtgenin boyutları köşelerin en küçük ve en büyük koordinatlarından bulunur.','x: 1 → 8 = 7 · y: 1 → 6 = 5 · alan 7 × 5 = 35'),A('Köşe üçgenlerini bul','Dört köşede dik üçgenler kalır; dik kenarlarından alanlarını hesapla.','4 × 3 ÷ 2 = 6 · 2 × 3 ÷ 2 = 3 · 4 × 1 ÷ 2 = 2 · 4 × 3 ÷ 2 = 6 → toplam 17'),A('Farkı al','Dikdörtgenin alanından bu üçgenleri çıkar.','35 − 17 = 18')],
 puf='Kareli zeminde dörtgenin alanı için önce saran dikdörtgeni, sonra köşelerde kalan üçgenleri bul.',sekil=SK5)

# ===== 06 bölgeler · öncüllü · orta =====
kartla('K-GNA-06','Bölgeler ve işaretler','A noktasının bölgesinden a ve b’nin işareti çıkarılır; her öncüldeki yeni noktanın iki koordinatının işareti ayrı ayrı belirlenir.','Koordinatları yer değiştirince bölgenin değişmediğini sanmak; çarpım ve farkın işaretini yanlış bulmak.','orta',4,'ge-na-bolge','Bölgeler ve koordinat işaretleri','öncüllü')
a6,b6=3,-2   # IV. bölge (a>0, b<0)
def bolge(x,y): return 1 if x>0 and y>0 else 2 if x<0 and y>0 else 3 if x<0 and y<0 else 4 if x>0 and y<0 else 0
assert bolge(a6,b6)==4
o1=bolge(-a6,b6); o2=bolge(b6,a6); o3=bolge(a6*b6,b6-a6); assert (o1,o2,o3)==(3,2,3)
assert bolge(a6*b6,a6-b6)==2 and bolge(b6,a6)!=4 and bolge(-a6,b6)==3
f=Pl(-3,3,-3,3,.8,grid=False,ticks=False)
for t,(x,y) in {'1. bölge':(1.2,2.05),'2. bölge':(-1.2,2.05),'3. bölge':(-1.2,-2.05),'4. bölge':(1.2,-2.05)}.items(): f.node((x,y),'\\footnotesize '+t)
Ac=(1.35,-1.15); f.raw(f'\\fill {pt(Ac)} circle (.075);'); f.vl('A',Ac,(1,-.5),.3)
SK6=f.svg()
q('0006',tipId='ge-na-bolge',tip='Bölgeler ve koordinat işaretleri',z='orta',alt='Bölgeler',kaz='Bir noktanın bulunduğu bölgeden koordinat işaretlerini çıkarıp yeni noktaların bölgelerini belirler.',kalip='öncüllü',
 kart='K-GNA-06 (bölgeler) · A(a, b) 4. bölgede; (−a, b), (b, a), (a·b, b − a)',
 metin='Şekilde analitik düzlemin dört bölgesi numaralandırılmış ve koordinatları (a, b) olan A noktası gösterilmiştir.\nBuna göre,\nI. B(−a, b) noktası 3. bölgededir.\nII. C(b, a) noktası 2. bölgededir.\nIII. D(a·b, b − a) noktası 3. bölgededir.\nifadelerinden hangileri doğrudur?',
 dogru='I, II ve III',sira=['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III'],
 yan=[('Yalnız I','C(b, a) için koordinatları yer değiştirmenin bölgeyi değiştirmediğini sanmış; D’de b − a’yı pozitif bulmuş.','bilgi'),('Yalnız II','B(−a, b) için −a’yı pozitif sanmış; D’de de b − a’yı pozitif bulmuş.','bilgi'),('I ve II','D(a·b, b − a) için b − a’nın pozitif olduğunu sanmış (b negatif, a pozitif ise b − a negatiftir).','bilgi'),('I ve III','C(b, a) için koordinatları yer değiştirmenin bölgeyi değiştirmediğini, C’nin de 4. bölgede kaldığını sanmış.','bilgi')],
 istenen='Doğru olan öncüller.',
 ip=['A noktası 4. bölgede olduğuna göre a ve b’nin işaretlerini yaz; sonra her öncüldeki noktanın apsis ve ordinatının işaretini ayrı ayrı belirle.'],
 bilgi=[BOLGE],
 ad=[A('İşaretleri bul','A 4. bölgede olduğundan apsisi pozitif, ordinatı negatiftir.','a > 0 · b < 0'),A('I. öncülü incele','−a negatif, b negatiftir; iki koordinat da negatiftir.','B(−, −) → 3. bölge · doğru'),A('II. öncülü incele','Yeni apsis b negatif, yeni ordinat a pozitiftir.','C(−, +) → 2. bölge · doğru'),A('III. öncülü incele','a·b negatiftir; b − a ise negatif sayıdan pozitif sayı çıkarmaktır, negatiftir.','D(−, −) → 3. bölge · doğru'),A('Sonucu yaz','Üç öncül de doğrudur.','I, II ve III')],
 puf='Bölge sorularında önce a ve b’nin işaretini yaz; her yeni koordinatın işaretini (çarpım, fark, ters işaret) ayrı ayrı belirle.',sekil=SK6)

# ===== 07 eşit uzaklık · zor · hikâyeli =====
kartla('K-GNA-07','Eksen üzerinde eşit uzaklıkta nokta','x ekseni üzerindeki C(a, 0) noktası için |AC|² = |BC|² denklemi kurulur; a bulunur ve uzaklık hesaplanır.','C’yi orta noktanın izdüşümü sanmak; |AC|² yerine |AC| vermek; a’yı cevap sanmak.','zor',5,'ge-na-uzaklik','İki nokta arası uzaklık','hikâyeli')
A7=(1,4); B7=(7,2); a7=None
# (a-1)^2+16=(a-7)^2+4  ->  -2a+17 = -14a+53  -> a=3
cands=[a for a in range(-20,21) if (a-A7[0])**2+A7[1]**2==(a-B7[0])**2+B7[1]**2]; assert cands==[3]; a7=3
d2=(a7-A7[0])**2+A7[1]**2; assert d2==20 and d2==(a7-B7[0])**2+B7[1]**2 and 2*2*5==20 and (2*math.sqrt(5)-math.sqrt(d2))<1e-9
C7=(a7,0)
mo=((A7[0]+B7[0])//2); assert mo==4 and (mo-A7[0])**2+A7[1]**2==25 and ((A7[0]-B7[0])**2+(A7[1]-B7[1])**2)==40
assert abs(math.sqrt(40)/2-math.sqrt(10))<1e-9 and 3<math.sqrt(10)<5
pl=Pl(-1,9,-1,6,.55); pl.dot(*A7); pl.dot(*B7); pl.lab('A',*A7,-.5,1,.28); pl.lab('B',*B7,.6,1,.28)
SK7=pl.svg()
q('0007',tipId='ge-na-uzaklik',tip='İki nokta arası uzaklık',z='zor',alt='Eşit Uzaklık',kaz='Eksen üzerinde iki noktaya eşit uzaklıktaki noktayı bulup uzaklığı hesaplar.',kalip='hikâyeli',
 kart='K-GNA-07 (eşit uzaklık) · A(1, 4), B(7, 2), C ∈ x ekseni',
 metin='Şekilde, bir kasabanın haritası kareli zemine çizilmiştir; her karenin kenarı 1 km dir. Düz bir yol x ekseni boyunca uzanmaktadır. A ve B köyleri yolun aynı tarafındadır. Yol üzerine, her iki köye de eşit uzaklıkta bir C istasyonu kurulacaktır.\nBuna göre, |AC| kaç km dir?',
 dogru='2√5',sira=['3','√10','2√5','5','20'],
 yan=[('3','C(a, 0) noktasının apsisini (a = 3) bulup uzaklık yerine bunu cevap vermiş.','dikkat'),('√10','|AB| = √40’ın yarısını almış: √40 ÷ 2 = √10.','bilgi'),('5','C’yi A ile B’nin orta noktasının x eksenindeki izdüşümü (4, 0) almış: |AC| = √(9 + 16) = 5.','bilgi'),('20','|AC|² = 20 bulmuş ama karekökü almayı unutmuş.','islem')],
 istenen='|AC| uzaklığı (km).',
 ip=['C, x ekseni üzerinde olduğuna göre koordinatları (a, 0) biçimindedir; |AC| = |BC| eşitliğinin iki tarafının karesini yaz.'],
 bilgi=[UZ],
 ad=[A('Koordinatları oku','Izgaradan A ve B’yi oku; C(a, 0) al.','A(1, 4) · B(7, 2)'),A('Eşitliği kur','|AC| = |BC| olduğundan kareleri de eşittir.','(a − 1)² + 4² = (a − 7)² + 2²'),A('a’yı bul','Parantezleri aç ve sadeleştir.','a² − 2a + 17 = a² − 14a + 53 → 12a = 36 → a = 3'),A('|AC|’yi hesapla','C(3, 0) için uzaklık formülünü uygula.','|AC| = √[(3 − 1)² + 4²] = √20 = 2√5')],
 puf='Bir eksen üzerindeki noktaya koordinat vererek (a, 0) ya da (0, b) yaz; eşit uzaklıkta uzaklıkların kareleri eşitlenir, kök işlemi sona kalır.',sekil=SK7)

# ===== 08 paralelkenar alanı · zor =====
kartla('K-GNA-08','Paralelkenarın dördüncü köşesi ve alanı','Köşegenlerin orta noktası ortaktır: D = A + C − B bulunur; sonra köşe koordinatlarıyla ya da saran dikdörtgenle alan hesaplanır.','D’yi yanlış bulmak; ABC üçgeninin alanını vermek; saran dikdörtgenin alanını vermek; taban × yükseklikte eğik kenarı hesaba katmamak.','zor',5,'ge-na-alan','Köşeleri verilen çokgenin alanı')
A8=(-2,1); B8=(4,-1); C8=(8,3); D8=(A8[0]+C8[0]-B8[0],A8[1]+C8[1]-B8[1]); assert D8==(2,5)
S8=[A8,B8,C8,D8]; al8=alan(S8); assert al8==32 and alan([A8,B8,C8])==16 and 2*al8==64
assert mid(A8,C8)==mid(B8,D8)
bb8=(max(p[0] for p in S8)-min(p[0] for p in S8))*(max(p[1] for p in S8)-min(p[1] for p in S8)); assert bb8==60
AB8=sub(B8,A8); AD8=sub(D8,A8); assert AB8[0]*AD8[1]==24 and abs(AB8[0]*AD8[1]-AB8[1]*AD8[0])==32
pl=Pl(-3,9,-2,6,.5); pl.seg(A8,B8); pl.seg(B8,C8)
for p in (A8,B8,C8): pl.dot(*p)
pl.lab('A',*A8,-1,0,.28); pl.lab('B',*B8,0,-1,.28); pl.lab('C',*C8,1,0,.28)
SK8=pl.svg()
q('0008',tipId='ge-na-alan',tip='Köşeleri verilen çokgenin alanı',z='zor',alt='Paralelkenarın Alanı',kaz='Paralelkenarın eksik köşesini köşegenlerin orta noktasından bulup alanını hesaplar.',
 kart='K-GNA-08 (paralelkenar) · A(−2, 1), B(4, −1), C(8, 3); D = A + C − B',
 metin='Şekilde, bir karesinin kenarı 1 birim olan kareli düzlemde A, B ve C noktaları ile [AB] ve [BC] doğru parçaları verilmiştir. Köşeleri A, B, C ve D sırasıyla adlandırılan ABCD paralelkenarı oluşturulacaktır.\nBuna göre, ABCD paralelkenarının alanı kaç birimkaredir?',
 dogru=32,yan=[(16,'Yalnız ABC üçgeninin alanını bulup paralelkenar için ikiye katlamayı unutmuş.','dikkat'),(24,'6 × 4 hesaplamış (|AB| nin yatay uzunluğu 6, |AD| nin düşey uzunluğu 4); |AD| nin 4 birimlik yatay kaymasını hesaba katmamış.','bilgi'),(60,'Dört köşeyi saran dikdörtgenin alanını (10 × 6) cevap vermiş.','bilgi'),(64,'Çapraz çarpımları hesaplayıp ikiye bölmeyi unutmuş.','islem')],
 istenen='ABCD paralelkenarının alanı (birimkare).',
 ip=['Paralelkenarın köşegenleri hakkında ne biliyorsun? Bu bilgi eksik köşeyi bulmana yardım eder.'],
 bilgi=[PAR,ALAN],
 ad=[A('Koordinatları oku','Izgaradan üç köşeyi oku.','A(−2, 1) · B(4, −1) · C(8, 3)'),A('D’yi bul','Köşegenlerin orta noktaları aynıdır: A + C = B + D.','D = (−2 + 8 − 4 , 1 + 3 − (−1)) = (2, 5)'),A('ABC üçgeninin alanı','Köşe koordinatlarıyla alan hesapla (ya da saran dikdörtgenden köşe üçgenlerini çıkar).','|(−2)(−1) − 4·1 + 4·3 − 8·(−1) + 8·1 − (−2)·3| ÷ 2 = 32 ÷ 2 = 16'),A('Paralelkenarın alanı','Köşegen paralelkenarı eş iki üçgene böler.','2 × 16 = 32')],
 puf='Paralelkenarın eksik köşesi için karşılıklı köşelerin koordinat toplamlarını eşitle; köşegen alanı iki eş üçgene böler.',sekil=SK8)

kayit_yaz()
