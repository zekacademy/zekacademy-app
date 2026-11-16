"""TYT Geometri · Çemberin Analitiği (hafif mod; kardeş yok, ipucu 1). Koordinatlar Python'da hesaplanır, TikZ gövdesi aynı değerlerden üretilir; her cevap ve çeldirici değeri assert edilir."""
import sys,os,math,json
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
from math import sin,cos,tan,radians,degrees,atan2,sqrt,pi
from fractions import Fraction as Fr
ONEK='cemberanalitik'
P=Parti(ONEK,'Çemberin Analitiği','geo|Çemberin Analitiği',ders='TYT Geometri',idon='tytgeo')
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
CDEN=B('Çemberin denklemi','merkezi M(a, b) ve yarıçapı r olan çemberin denklemi (x − a)² + (y − b)² = r² dir; denklemde yazılan işaretler merkezin koordinatlarının ters işaretlisidir. Örnek: merkezi (1, −5), yarıçapı 2 olan çemberin denklemi (x − 1)² + (y + 5)² = 4 tür')
COKU=B('Denklemden merkez ve yarıçap','(x − a)² + (y − b)² = r² denkleminde merkez (a, b), yarıçap √(r²) = r dir; sağ taraf yarıçapın karesidir. Örnek: (x + 4)² + (y − 1)² = 36 çemberinin merkezi (−4, 1), yarıçapı 6’dır')
CTEG=B('Eksene teğet çember','bir doğruya teğet olan çemberin merkezinin o doğruya uzaklığı yarıçapa eşittir. Bir noktanın bir eksene uzaklığı, diğer koordinatın mutlak değeridir. Örnek: (−3, 6) noktasının x eksenine uzaklığı 6 dır')
CKON=B('Noktanın çembere göre konumu','merkezi M(a, b) ve yarıçapı r olan çember için P(x, y) noktasında (x − a)² + (y − b)² değeri r² den küçükse P çemberin içinde, r² ye eşitse çember üzerinde, büyükse dışındadır. Örnek: x² + y² = 9 çemberi için (1, 2) noktasında 1 + 4 = 5 < 9 olduğundan nokta içtedir')
konu('geo|Çemberin Analitiği','Çemberin Analitiği')

# ===== 01 merkez ve yarıçapı ızgaradan okuyup denklem yazma · kolay =====
kartla('K-GCN-01','Merkez ve yarıçaptan denklem','Merkez ve yarıçap ızgaradan okunur; (x − a)² + (y − b)² = r² biçiminde, işaretlere ve r² ye dikkat edilerek yazılır.','Merkezin işaretini aynen yazmak; r yerine r² yi yazmamak; yarıçap yerine çapı almak.','kolay',3,'ge-cn-denklem','Merkez ve yarıçaptan çember denklemi')
M1=(3,-2); r1=4
for p in [(7,-2),(-1,-2),(3,2),(3,-6)]: assert (p[0]-M1[0])**2+(p[1]-M1[1])**2==r1**2
assert r1**2==16 and 2*r1==8
pl=Pl(-2,8,-7,3,.45,o=(.25,.25)); pl.raw(f'\\draw[thick] {pt(pl.c(*M1))} circle ({r1*pl.u});'); pl.dot(*M1); pl.lab('M',*M1,1,.7,.3)
SK1=pl.svg()
q('0001',tipId='ge-cn-denklem',tip='Merkez ve yarıçaptan çember denklemi',z='kolay',alt='Çember Denklemi',kaz='Izgaradan okunan merkez ve yarıçapa göre çemberin denklemini yazar.',
 kart='K-GCN-01 (çember denklemi) · merkez (3, −2), r = 4',
 metin='Şekilde, bir karesinin kenarı 1 birim olan kareli düzlemde merkezi M olan bir çember verilmiştir. Çember, ızgaranın köşe noktalarından geçmektedir.\nBuna göre, bu çemberin denklemi aşağıdakilerden hangisidir?',
 dogru='(x − 3)² + (y + 2)² = 16',sira=['(x − 3)² + (y − 2)² = 16','(x − 3)² + (y + 2)² = 4','(x − 3)² + (y + 2)² = 8','(x + 3)² + (y − 2)² = 16','(x − 3)² + (y + 2)² = 16'],
 yan=[('(x − 3)² + (y − 2)² = 16','Merkezin apsisini doğru, ordinatını (−2) yanlış işaretle yazmış: (y − 2).','bilgi'),('(x − 3)² + (y + 2)² = 4','Sağ tarafa yarıçapın karesi yerine yarıçapın kendisini (4) yazmış.','bilgi'),('(x − 3)² + (y + 2)² = 8','Sağ tarafa yarıçap yerine çapı (8) yazmış.','dikkat'),('(x + 3)² + (y − 2)² = 16','Merkezin koordinatlarını işaretleriyle aynen yazmış: (x + 3) ve (y − 2).','bilgi')],
 istenen='Çemberin denklemi.',
 ip=['Merkezin koordinatlarını ve çemberin merkezden bir ızgara noktasına olan uzaklığını (yarıçapı) oku.'],
 bilgi=[CDEN],
 ad=[A('Merkezi oku','Izgaradan M noktasının koordinatlarını oku.','M(3, −2)'),A('Yarıçapı bul','Merkezden çember üzerindeki bir ızgara noktasına (7, −2) uzaklığı yarıçaptır.','r = 7 − 3 = 4'),A('Denklemi yaz','(x − a)² + (y − b)² = r² biçiminde yaz; −2 için (y − (−2)) = (y + 2) olur.','(x − 3)² + (y + 2)² = 16')],
 puf='Merkez (a, b) ise denklemde (x − a) ve (y − b) yazılır; sağ taraf r nin karesidir.',sekil=SK1)

# ===== 02 denklemden merkez/yarıçap okuma · orta · hikâyeli =====
kartla('K-GCN-02','Denklemden merkez ve yarıçap okuma','Standart denklemden merkez (ters işaretle) ve yarıçap (karekök) okunur; merkezin x eksenine uzaklığı ordinatın mutlak değeridir.','Merkezin işaretini aynen almak; r² yi yarıçap sanmak; x eksenine uzaklık yerine apsisi almak.','orta',4,'ge-cn-okuma','Denklemden merkez ve yarıçap okuma','hikâyeli')
a2,b2,r2=-2,5,7; M2=(a2,b2); H2=(a2,0); T2=(a2+r2,b2)
assert abs(b2)==5 and r2*r2==49 and abs(b2)+r2==12 and abs(a2)+r2==9 and abs(b2)+r2*r2==54 and abs(a2)+r2*r2==51 and r2-abs(b2)==2
u=.3; f=Pl(-10,6,-3,13,u,grid=False,ticks=False,o=(.25,.25))
f.raw(f'\\draw[thick] {pt(f.c(*M2))} circle ({r2*u});'); f.seg(M2,H2,'dashed'); f.seg(M2,T2)
f.dot(*M2); f.dot(*T2)
f.lab('M',*M2,-.8,.8,.3); f.lab('H',*H2,-.3,-1,.3); f.lab('T',*T2,1,.3,.3)
SK2=f.svg()
q('0002',tipId='ge-cn-okuma',tip='Denklemden merkez ve yarıçap okuma',z='orta',alt='Denklemden Merkez ve Yarıçap',kaz='Çemberin standart denkleminden merkezi ve yarıçapı okuyup uzaklık hesaplar.',kalip='hikâyeli',
 kart='K-GCN-02 (merkez, yarıçap okuma) · (x + 2)² + (y − 5)² = 49',
 metin='Bir parkta dairesel bir havuzun kenarı, kareli planda (x + 2)² + (y − 5)² = 49 denklemli çember olarak gösterilmektedir (birim: metre). Çemberin merkezi M, M noktasından x eksenine (kıyı çizgisine) indirilen dikmenin ayağı H ve çember üzerindeki bir nokta T ile gösterilmiştir.\nBuna göre, |MH| + |MT| toplamı kaç metredir?',
 dogru=12,yan=[(2,'Uzunlukları toplamak yerine yarıçaptan merkezin eksene uzaklığını çıkarmış (7 − 5).','dikkat'),(9,'Merkezin x eksenine uzaklığı yerine apsisinin mutlak değerini (2) almış: 2 + 7.','dikkat'),(51,'Apsisin mutlak değerini (2) almış ve yarıçap yerine sağ taraftaki 49’u kullanmış.','bilgi'),(54,'Merkezin eksene uzaklığını doğru (5) bulmuş ama yarıçap yerine sağ taraftaki 49’u yazmış.','bilgi')],
 istenen='|MH| + |MT| toplamı (m).',
 ip=['Denklemden merkezin koordinatlarını ve sağ taraftaki sayıyla yarıçapı bul; M’nin x eksenine uzaklığının hangi koordinatla bulunduğunu düşün.'],
 bilgi=[COKU],
 ad=[A('Merkezi bul','Denklemde (x + 2) ve (y − 5) ifadelerinden merkezin koordinatları ters işaretle okunur.','M(−2, 5)'),A('Yarıçapı bul','Sağ taraftaki sayı r² dir.','r² = 49 → r = |MT| = 7'),A('|MH| uzunluğunu bul','M’den x eksenine uzaklık ordinatın mutlak değeridir.','|MH| = |5| = 5'),A('Toplamı yaz','İki uzunluğu topla.','5 + 7 = 12')],
 puf='Standart denklemde merkez ters işaretle okunur, yarıçap sağ taraftaki sayının karekökü olur; eksene uzaklık ilgili koordinatın mutlak değeridir.',sekil=SK2)

# ===== 03 eksene teğet çember · orta =====
kartla('K-GCN-03','Eksene teğet çemberin denklemi','Merkez ızgaradan okunur; teğet olunan eksene uzaklık yarıçap olur ve denklem yazılır.','Yarıçap yerine diğer koordinatın mutlak değerini almak; r yi r² yerine yazmak; işareti aynen yazmak.','orta',3,'ge-cn-teget','Eksene teğet çember')
A3=(-5,4); r3=abs(A3[0]); assert r3==5 and r3**2==25 and abs(A3[1])**2==16 and 2*r3==10
pl=Pl(-8,3,-2,8,.45); pl.dot(*A3); pl.lab('A',*A3,-1,.5,.3)
SK3=pl.svg()
q('0003',tipId='ge-cn-teget',tip='Eksene teğet çember',z='orta',alt='Eksene Teğet Çember',kaz='Merkezi verilen ve bir eksene teğet olan çemberin denklemini yazar.',
 kart='K-GCN-03 (teğet çember) · merkez (−5, 4), y eksenine teğet',
 metin='Şekilde, bir karesinin kenarı 1 birim olan kareli düzlemde A noktası verilmiştir. Merkezi A noktası olan ve y eksenine teğet olan bir çember çizilecektir.\nBuna göre, bu çemberin denklemi aşağıdakilerden hangisidir?',
 dogru='(x + 5)² + (y − 4)² = 25',sira=['(x + 5)² + (y − 4)² = 5','(x + 5)² + (y − 4)² = 10','(x + 5)² + (y − 4)² = 16','(x + 5)² + (y − 4)² = 25','(x − 5)² + (y + 4)² = 25'],
 yan=[('(x + 5)² + (y − 4)² = 5','Yarıçapı 5 bulmuş ama sağ tarafa karesini değil kendisini yazmış.','bilgi'),('(x + 5)² + (y − 4)² = 10','Sağ tarafa yarıçap yerine çapı (10) yazmış.','dikkat'),('(x + 5)² + (y − 4)² = 16','y eksenine teğet olan çemberde yarıçapı ordinattan (4) almış; bu x eksenine teğet olma koşuludur.','bilgi'),('(x − 5)² + (y + 4)² = 25','Merkezi (5, −4) sanmış; (−5, 4) merkezli çemberde parantezlerin işaretlerinin (x + 5) ve (y − 4) olduğunu atlamış.','bilgi')],
 istenen='Çemberin denklemi.',
 ip=['Çember y eksenine teğetse merkezin y eksenine uzaklığı hangi uzunluğa eşit olur?'],
 bilgi=[CTEG,CDEN],
 ad=[A('Merkezi oku','Izgaradan A noktasının koordinatlarını oku.','A(−5, 4)'),A('Yarıçapı bul','y eksenine teğet çemberde yarıçap, merkezin y eksenine uzaklığıdır; bu uzaklık apsisin mutlak değeridir.','r = |−5| = 5'),A('Denklemi yaz','(x − a)² + (y − b)² = r² biçiminde yerine koy.','(x + 5)² + (y − 4)² = 25')],
 puf='y eksenine teğet çemberde r = |a|, x eksenine teğet çemberde r = |b| dir; merkez ters işaretle denkleme yazılır.',sekil=SK3)

# ===== 04 noktanın çembere göre konumu · zor · öncüllü =====
kartla('K-GCN-04','Noktanın çembere göre konumu','Her noktanın koordinatları (x − a)² + (y − b)² ifadesine yazılır ve r² ile karşılaştırılır.','Sonucu r ile kıyaslamak; işaret hatası; eşit olma durumunu (çember üzerinde) iç sanmak.','zor',4,'ge-cn-konum','Noktanın çembere göre konumu','öncüllü')
a4,b4,R4=2,-1,5
def konum(p):
    v=(p[0]-a4)**2+(p[1]-b4)**2; return v,('üzerinde' if v==R4**2 else 'içinde' if v<R4**2 else 'dışında')
Pa=(5,3); Pb=(0,1); Pc=(-3,0)
assert konum(Pa)==(25,'üzerinde') and konum(Pb)==(8,'içinde') and konum(Pc)==(26,'dışında')
tru=(konum(Pa)[1]=='üzerinde', konum(Pb)[1]=='dışında', konum(Pc)[1]=='içinde'); assert tru==(True,False,False)
assert 8>R4 and 26>R4**2 and (7**2+2**2)==53 and (0+2)**2+(1-1)**2==4 and (-3+2)**2+(0-1)**2==2
pl=Pl(-4,6,-2,4,.5); 
for p,n,d in [(Pa,'A',(.3,1)),(Pb,'B',(1,.5)),(Pc,'C',(-.3,1))]: pl.dot(*p); pl.lab(n,*p,d[0],d[1],.3)
SK4=pl.svg()
q('0004',tipId='ge-cn-konum',tip='Noktanın çembere göre konumu',z='zor',alt='Noktanın Konumu',kaz='Noktaların koordinatlarını çember denklemine yazarak çembere göre konumlarını belirler.',kalip='öncüllü',
 kart='K-GCN-04 (konum) · (x − 2)² + (y + 1)² = 25; A(5, 3), B(0, 1), C(−3, 0)',
 metin='Şekilde, bir karesinin kenarı 1 birim olan kareli düzlemde A, B ve C noktaları gösterilmiştir. Denklemi (x − 2)² + (y + 1)² = 25 olan çember şekilde çizilmemiştir.\nBuna göre,\nI. A noktası çember üzerindedir.\nII. B noktası çemberin dış bölgesindedir.\nIII. C noktası çemberin iç bölgesindedir.\nifadelerinden hangileri doğrudur?',
 dogru='Yalnız I',sira=['Yalnız I','Yalnız II','Yalnız III','I ve III','I, II ve III'],
 yan=[('Yalnız II','Hesapladığı değerleri r² = 25 ile değil r = 5 ile kıyaslamış: 25 > 5 ve 26 > 5 olduğundan A ve C’yi dışarıda, 8 > 5 olduğundan B’yi dışarıda saymış.','bilgi'),('Yalnız III','Merkezi (−2, 1) almış (işaretleri aynen yazmış): A için 53 (dışarıda), B için 4, C için 2 bulup yalnız C’yi içeride saymış.','bilgi'),('I ve III','C için 26 bulmuş ama 26’yı 25’e çok yakın görüp C’yi çemberin içinde saymış.','dikkat'),('I, II ve III','Kıyası ters yapmış: r² den küçük değeri dışarıda, büyük değeri içeride saymış (8 → dışarıda, 26 → içeride).','bilgi')],
 istenen='Doğru olan öncüller.',
 ip=['Çemberin merkezini ve r² değerini yaz; her noktanın koordinatlarını (x − 2)² + (y + 1)² ifadesinde yerine koyup sonucu r² ile karşılaştır.'],
 bilgi=[CKON],
 ad=[A('Merkez ve r²','Denklemden merkez ve yarıçapın karesi okunur.','M(2, −1) · r² = 25'),A('A noktası','Koordinatları (x − 2)² + (y + 1)² ifadesinde yerine koy.','(5 − 2)² + (3 + 1)² = 9 + 16 = 25 → çember üzerinde'),A('B noktası','Aynı işlemi B için yap.','(0 − 2)² + (1 + 1)² = 4 + 4 = 8 < 25 → çemberin içinde'),A('C noktası','Aynı işlemi C için yap.','(−3 − 2)² + (0 + 1)² = 25 + 1 = 26 > 25 → çemberin dışında'),A('Öncülleri değerlendir','Yalnız birinci öncül doğrudur; B içeride, C dışarıdadır.','I doğru · II yanlış · III yanlış')],
 puf='Konum için sonucu r² ile karşılaştır (r ile değil): küçükse iç, eşitse üzerinde, büyükse dış bölgededir.',sekil=SK4)

kayit_yaz()
