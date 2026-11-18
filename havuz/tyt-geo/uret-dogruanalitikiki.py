"""TYT Geometri · Doğrunun Analitiği (hafif mod; kardeş yok, ipucu 1). Koordinatlar Python'da hesaplanır, TikZ gövdesi aynı değerlerden üretilir; her cevap ve çeldirici değeri assert edilir."""
import sys,os,math,json
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
from math import sin,cos,tan,radians,degrees,atan2,sqrt,pi
from fractions import Fraction as Fr
ONEK='dogruanalitikiki'
P=Parti(ONEK,'Doğrunun Analitiği','geo|Doğrunun Analitiği',ders='TYT Geometri',idon='tytgeo')
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
    P.yaz(os.path.join(GD,ONEK+'-1.json'),os.path.join('/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/ai_dk','bos-'+ONEK+'.json'))
    tipler={}
    for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=TIPK[c['tipId']]))['kartlar'].append(c['id'])
    json.dump(dict(konu=P.konu_adi,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 TYT Geometri çıkmış soruları (yalnız mantık), MEB 9–10. sınıf geometri müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar',ONEK+'.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler),'soru',len(P.ANA))
# ---- ek yardımcılar: sınırlara kırpılmış doğru, koordinat etiketi ----
def _clip(s,a,b):
    dx,dy=b[0]-a[0],b[1]-a[1]; ts=[]
    if dx: ts+= [(s.x0-a[0])/dx,(s.x1-a[0])/dx]
    if dy: ts+= [(s.y0-a[1])/dy,(s.y1-a[1])/dy]
    ok=[t for t in ts if s.x0-1e-9<=a[0]+t*dx<=s.x1+1e-9 and s.y0-1e-9<=a[1]+t*dy<=s.y1+1e-9]
    t0,t1=min(ok),max(ok); return (a[0]+t0*dx,a[1]+t0*dy),(a[0]+t1*dx,a[1]+t1*dy)
def _dogru(s,a,b,st='thick'):
    p,q_=_clip(s,a,b); s.line(s.c(*p),s.c(*q_),st); return p,q_
def _tag(s,t,x,y,dx,dy,anc):
    p=s.c(x,y); s.node((p[0]+dx,p[1]+dy),t,f'anchor={anc}')
Pl.dogru=_dogru; Pl.tag=_tag
EGIM=B('Doğrunun eğimi','A(x₁, y₁) ve B(x₂, y₂) noktalarından geçen doğrunun eğimi m = (y₂ − y₁) / (x₂ − x₁) dir. Örnek: (0, 5) ve (2, 1) noktalarından geçen doğrunun eğimi (1 − 5) / (2 − 0) = −2’dir')
DNK=B('Doğru denklemi ve noktalar','ax + by + c = 0 biçimindeki denklem, doğru üzerindeki her noktanın koordinatlarının sağladığı ilişkidir; denklemi sağlayan nokta doğrunun üzerindedir. Örnek: x + y − 5 = 0 için (2, 3) doğru üzerindedir, çünkü 2 + 3 − 5 = 0’dır')
NE=B('Nokta-eğim denklemi','eğimi m olan ve (x₁, y₁) noktasından geçen doğrunun denklemi y − y₁ = m(x − x₁) dir. Örnek: eğimi −1 ve (4, 0) noktasından geçen doğru y = −(x − 4), yani x + y − 4 = 0 dır')
UZK=B('Noktanın doğruya uzaklığı','P(x₀, y₀) noktasının ax + by + c = 0 doğrusuna uzaklığı |ax₀ + by₀ + c| / √(a² + b²) dir. Örnek: O(0, 0) noktasının 6x + 8y − 20 = 0 doğrusuna uzaklığı 20 / 10 = 2’dir')
PD=B('Paralel ve dik doğrular','ax + by + c = 0 doğrusunun eğimi −a/b dir. Paralel doğruların eğimleri eşit, dik doğruların eğimlerinin çarpımı −1 dir. Örnek: eğimi 3/5 olan doğruya dik doğrunun eğimi −5/3 tür')
KES=B('İki doğrunun kesişimi','iki doğrunun kesişim noktası, denklemlerinin ortak çözümüdür. Üç doğru aynı noktada kesişiyorsa bu nokta üçünün de denklemini sağlar. Örnek: y = 2x ve x + y = 9 doğruları için 3x = 9, x = 3 ve y = 6; kesişim (3, 6) dır')
ALN=B('Izgarada alan hesabı','köşeleri ızgara noktalarında olan şekillerin alanı, birim kareler ve dik üçgenler gibi alanı bilinen parçalarla hesaplanır. Örnek: köşeleri O(0, 0), P(6, 0), R(2, 4) olan üçgenin alanı 12 dir')
ODK=B('Orta nokta ve orta dikme','A(x₁, y₁) ve B(x₂, y₂) için orta nokta ((x₁ + x₂)/2, (y₁ + y₂)/2) dir. Bir doğru parçasının orta dikmesi, orta noktasından geçen ve doğru parçasına dik olan doğrudur. Örnek: A(0, 1) ve B(6, 1) için orta nokta (3, 1) dir')
EKS=B('Eksenleri kestiği noktalar','x eksenini kestiği noktada y = 0, y eksenini kestiği noktada x = 0 dır. Örnek: 2x + 5y − 10 = 0 doğrusu x eksenini (5, 0), y eksenini (0, 2) noktasında keser')
konu('geo|Doğrunun Analitiği','Doğrunun Analitiği')
def egim(a,b): return Fr(b[1]-a[1],b[0]-a[0])
def gec(eq,p): return eq[0]*p[0]+eq[1]*p[1]+eq[2]==0
def uzk(eq,p): return Fr(abs(eq[0]*p[0]+eq[1]*p[1]+eq[2]))

# ===== 01 kolay · eğimi bilinen doğruda bilinmeyen ordinat =====
kartla('K-GDQ-01','Eğimden bilinmeyen koordinat','Eğim, iki nokta arasındaki dikey farkın yatay farka oranıdır; eğim ve yatay fark biliniyorsa dikey fark bulunur.','Dikey farkı eğime eşitlemek; ilk noktanın ordinatını eklemeyi unutmak; işareti karıştırmak.','kolay',3,'ge-di-egim','Eğimden bilinmeyen koordinat')
A1=(1,-1); B1x=4; m1=2; a1=A1[1]+m1*(B1x-A1[0]); assert a1==5 and egim(A1,(B1x,a1))==m1
assert m1*(B1x-A1[0])==6 and A1[1]+m1==1 and m1*B1x-A1[1]==9 and A1[1]+(-m1)*(B1x-A1[0])==-7
pl=Pl(-2,6,-3,7,.5,grid=False,ticks=False); pl.dogru(A1,(B1x,3.6)); pl.dot(*A1); pl.dot(B1x,3.6)
pl.tag('$A(1,-1)$',*A1,.1,-.12,'north west'); pl.tag('$B(4,a)$',B1x,3.6,-.1,.12,'south east'); pl.lab('d',2.7,2.2,1,-.3,.34)
SK1=pl.svg()
q('0001',tipId='ge-di-egim',tip='Eğimden bilinmeyen koordinat',z='kolay',alt='Eğimden Ordinat',kaz='Eğimi ve bir noktası bilinen doğru üzerindeki noktanın bilinmeyen koordinatını bulur.',
 kart='K-GDQ-01 (eğimden bilinmeyen koordinat) · m = 2, A(1, −1), B(4, a)',
 metin='Şekilde, analitik düzlemde eğimi 2 olan bir d doğrusu ve bu doğru üzerinde bulunan A(1, −1) ile B(4, a) noktaları verilmiştir. B noktasının ordinatı a olarak adlandırılmıştır. Şekil ölçekli değildir.\nBuna göre, a kaçtır?',
 dogru=5,yan=[(6,'Dikey farkı yatay fark ile eğimin çarpımına eşitleyip A’nın ordinatını eklememiş: a = 2 × 3.','dikkat'),(1,'Dikey farkı eğime eşit alıp (a − (−1) = 2) yatay farkı hesaba katmamış.','bilgi'),(9,'Başlangıçta y = 2x + 1 yazmış: a = 2 × 4 + 1 = 9.','islem'),(-7,'Eğimi −2 almış (işaret hatası): a = −1 + (−2) × 3.','bilgi')],
 istenen='a değeri.',
 ip=['A ve B noktalarının koordinat farkları ile eğim arasındaki ilişkiyi yaz; bilinmeyen tek terim kalsın.'],
 bilgi=[EGIM],
 ad=[A('Eğim bağıntısını yaz','Eğim, ordinat farkının apsis farkına oranıdır.','2 = (a − (−1)) / (4 − 1)'),A('Paydayı hesapla','Apsis farkını bul.','4 − 1 = 3 → a + 1 = 6'),A('a’yı bul','Eşitliği çöz.','a = 5')],
 puf='Bilinmeyen koordinatı, eğim bağıntısında iki nokta arasındaki farklarla birlikte yaz.',sekil=SK1)

# ===== 02 kolay · denklemi verilen doğru üzerindeki nokta =====
kartla('K-GDQ-02','Denklemi sağlayan nokta','Doğru üzerindeki her noktanın koordinatları doğrunun denklemini sağlar; bilinen koordinat yerine konunca bilinmeyen kalır.','Ordinatın işaretini düşürmek; sabit terimin işaretini değiştirmek; koordinatları yer değiştirmek.','kolay',3,'ge-di-nokta','Doğru üzerindeki nokta')
d2=(2,-1,-3); k2=-1; assert gec(d2,(k2,-5)) and gec(d2,(1,-1)) and gec(d2,(2,1))
assert (2*4-5-3==0) and (2*(-4)+5+3==0) and (2*(-5)-(-13)-3==0) and Fr(-5,2)*1==Fr(-5,2) and 2*Fr(-5,2)+5==0
pl=Pl(-4,4,-7,3,.5,grid=False,ticks=False); pl.dogru((1,-1),(2,1)); pl.dot(-1.7,-6.4); pl.tag('$A(k,-5)$',-1.7,-6.4,-.1,.1,'south east'); pl.lab('d',2.35,1.9,1,0,.32)
SK2=pl.svg()
q('0002',tipId='ge-di-nokta',tip='Doğru üzerindeki nokta',z='kolay',alt='Doğru Üzerindeki Nokta',kaz='Denklemi verilen doğru üzerindeki bir noktanın bilinmeyen koordinatını bulur.',
 kart='K-GDQ-02 (doğru üzerindeki nokta) · 2x − y − 3 = 0, A(k, −5)',
 metin='Şekilde, analitik düzlemde denklemi 2x − y − 3 = 0 olan d doğrusu ve bu doğru üzerinde bulunan A(k, −5) noktası gösterilmiştir. A noktasının apsisi k olarak adlandırılmıştır. Şekil ölçekli değildir.\nBuna göre, k kaçtır?',
 dogru=-1,yan=[(-13,'Koordinatları yer değiştirerek x = −5 ve y = k yazmış.','dikkat'),(-4,'Sabit terimin işaretini değiştirip 2k + 5 + 3 = 0 yazmış.','islem'),(-2.5,'Sabit terimi unutup 2k + 5 = 0 çözmüş.','islem'),(4,'−5’i yerine yazarken işaretini düşürmüş: 2k − 5 − 3 = 0.','bilgi')],
 istenen='k değeri.',
 ip=['Doğru üzerindeki bir nokta ile doğrunun denklemi arasında nasıl bir bağ vardır?'],
 bilgi=[DNK],
 ad=[A('Koordinatları yerine yaz','A doğru üzerinde olduğundan x = k ve y = −5 denklemi sağlar.','2k − (−5) − 3 = 0'),A('Düzenle','Parantezi aç ve sabitleri topla.','2k + 5 − 3 = 0 → 2k + 2 = 0'),A('k’yi bul','Eşitliği çöz.','k = −1')],
 puf='Bir koordinatı bilinen noktayı denklemde yerine koyarken parantez kullanıp işaretleri dikkatle taşı.',sekil=SK2)

# ===== 03 orta · hikâyeli · noktanın doğruya uzaklığı =====
kartla('K-GDQ-03','Noktanın doğruya uzaklığı','Noktanın koordinatları doğrunun denkleminin sol tarafında yerine yazılır; mutlak değer, katsayıların karelerinin toplamının karekökü ile bölünür.','Paydayı karekök almadan yazmak; paydada yalnız x katsayısını kullanmak; koordinatın işaretini düşürmek.','orta',3,'ge-di-uzaklik','Noktanın doğruya uzaklığı','hikâyeli')
d3=(4,-3,-1); P3=(2,-1); assert gec(d3,(-2,-3)) and gec(d3,(1,1)) and gec(d3,(4,5))
assert uzk(d3,P3)/5==2 and abs(d3[0]**2+d3[1]**2)==25
assert Fr(10,25)==Fr(2,5) and Fr(10,4)==Fr(5,2) and Fr(abs(4*2-3*1-1),5)==Fr(4,5)
pl=Pl(-4,6,-5,7,.55); pl.dogru((-2,-3),(4,5)); pl.dot(*P3); pl.lab('P',*P3,1,-.5,.3); pl.lab('d',3.55,5.9,-1,.2,.34)
SK3=pl.svg()
q('0003',tipId='ge-di-uzaklik',tip='Noktanın doğruya uzaklığı',z='orta',alt='Noktanın Doğruya Uzaklığı',kaz='Bir noktanın verilen doğruya en kısa uzaklığını hesaplar.',kalip='hikâyeli',
 kart='K-GDQ-03 (noktanın doğruya uzaklığı) · P(2, −1), 4x − 3y − 1 = 0',
 metin='Bir kanalın kıyısı, bir karesinin kenarı 1 birim olan kareli planda denklemi 4x − 3y − 1 = 0 olan d doğrusuyla gösterilmiştir. Kıyıdan uzakta bulunan P noktasındaki kulübeden kanala en kısa yoldan gidilecektir.\nBuna göre, kulübenin kanala en kısa uzaklığı kaç birimdir?',
 dogru=2,yan=[(10,'Payı hesaplamış ama paydadaki √(4² + (−3)²) = 5 ile bölmeyi unutmuş.','islem'),(0.4,'Paydaya karekök almadan katsayıların kareleri toplamını (25) yazmış.','bilgi'),(2.5,'Paydada yalnız x’in katsayısını (4) kullanmış.','bilgi'),(0.8,'y = −1 yerine y = 1 yazarak payı 4 bulmuş.','dikkat')],
 istenen='Kulübenin kanala en kısa uzaklığı (birim).',
 ip=['Bir noktanın bir doğruya en kısa uzaklığını veren bağıntıyı düşün; P’nin koordinatlarını ızgaradan okuyarak denklemde kullan.'],
 bilgi=[UZK],
 ad=[A('P’nin koordinatlarını oku','Izgaradan kulübenin konumunu bul.','P(2, −1)'),A('Payı hesapla','Koordinatları doğrunun denkleminin sol tarafında yerine yaz.','|4 × 2 − 3 × (−1) − 1| = |8 + 3 − 1| = 10'),A('Paydayı hesapla','Katsayıların kareleri toplamının karekökünü al.','√(4² + 3²) = 5'),A('Uzaklığı bul','Payı paydaya böl.','10 / 5 = 2')],
 puf='Uzaklık sorularında önce noktanın koordinatlarını güvenle oku, sonra payı ve paydayı ayrı ayrı hesapla.',sekil=SK3)

# ===== 04 orta · üç doğrunun ortak noktası =====
kartla('K-GDQ-04','Üç doğrunun ortak noktası','Grafikle verilen doğrunun denklemi yazılır; ikinci doğruyla kesişim bulunur ve üçüncü doğrunun denklemi bu noktada sağlatılır.','Kesişimin bir koordinatını almak; koordinatları yer değiştirmek; kesişim yerine eksen kesim noktasını kullanmak.','orta',4,'ge-di-kesisim','Üç doğrunun ortak noktası')
P4=(3,4); assert Fr(2,3)*P4[0]+2==P4[1] and gec((1,1,-7),P4) and gec((2,3,-18),P4)
sol=[m for m in range(-30,31) if m*3+3*4-18==0]; assert sol==[2]
assert Fr(9,4)==Fr(18-9,4) and 3*6-18==0 and 3*4+6-18==0 and 3*(-10)+12+18==0
pl=Pl(-5,7,-1,7,.52); pl.dogru((-3,0),(3,4)); pl.dot(-3,0); pl.dot(0,2); pl.lab('d_1',5.2,5.45,-1,.3,.36)
SK4=pl.svg()
q('0004',tipId='ge-di-kesisim',tip='Üç doğrunun ortak noktası',z='orta',alt='Ortak Nokta',kaz='İki doğrunun kesişim noktasından geçen üçüncü doğrunun denklemindeki bilinmeyeni bulur.',
 kart='K-GDQ-04 (üç doğru bir noktada) · d₁ grafikten, x + y − 7 = 0 ve mx + 3y − 18 = 0',
 metin='Şekilde, bir karesinin kenarı 1 birim olan kareli düzlemde d₁ doğrusu verilmiştir. Denklemleri x + y − 7 = 0 ve mx + 3y − 18 = 0 olan d₂ ve d₃ doğruları ile d₁ doğrusu aynı noktada kesişmektedir.\nBuna göre, m kaçtır?',
 dogru=2,yan=[(-10,'Kesişim noktasını doğru bulmuş ama d₃’te sabit terimin işaretini değiştirmiş: 3m + 12 + 18 = 0.','islem'),(2.25,'Koordinatları yer değiştirmiş: x = 4 ve y = 3 alıp 4m + 9 − 18 = 0 çözmüş.','dikkat'),(4,'Ordinat olarak d₁’in y eksenini kestiği 2’yi almış: 3m + 6 − 18 = 0.','dikkat'),(6,'Kesişim noktasının yalnız apsisini kullanmış (y = 0 almış): 3m − 18 = 0.','bilgi')],
 istenen='m değeri.',
 ip=['Üç doğru aynı noktadan geçiyorsa bu nokta hepsinin denklemini sağlar. Önce d₁’in denklemini ızgaradan yaz.'],
 bilgi=[KES,NE],
 ad=[A('d₁’in denklemini yaz','Izgaradan (−3, 0) ve (0, 2) noktalarını oku; eğim ve y eksenini kestiği nokta bulunur.','m₁ = 2/3 → y = 2x/3 + 2'),A('d₁ ile d₂’yi kesiştir','d₂’den y = 7 − x çekip d₁’de yerine koy.','2x/3 + 2 = 7 − x → 5x/3 = 5 → x = 3 , y = 4'),A('Ortak nokta d₃ üzerindedir','K(3, 4) noktasını d₃’ün denkleminde yerine yaz.','3m + 3 × 4 − 18 = 0'),A('m’yi bul','Eşitliği çöz.','3m = 6 → m = 2')],
 puf='Ortak noktayı bulduktan sonra üçüncü doğrunun denklemini bu noktayla sağlat.',sekil=SK4)

# ===== 05 orta · hikâyeli · ızgarada üçgenin alanı =====
kartla('K-GDQ-05','Koordinatlı üçgenin alanı','Üçgeni içine alan dikdörtgenden köşelerdeki dik üçgenler çıkarılarak alan bulunur.','Dikdörtgenin alanını sonuç sanmak; köşe üçgenlerinden birini unutmak; yarıya bölmeyi atlamak.','orta',4,'ge-di-ucgen-alan','Koordinatlı üçgenin alanı','hikâyeli')
A5=(1,1); B5=(7,3); C5=(3,6)
al=Fr(abs(A5[0]*(B5[1]-C5[1])+B5[0]*(C5[1]-A5[1])+C5[0]*(A5[1]-B5[1])),2); assert al==13
bb=(7-1)*(6-1); t1=(7-1)*(3-1)//2; t2=(7-3)*(6-3)//2; t3=(3-1)*(6-1)//2; assert (bb,t1,t2,t3)==(30,6,6,5) and bb-t1-t2-t3==13 and t1+t2+t3==17 and bb-t1-t2==18 and 2*13==26
pl=Pl(-1,9,-1,8,.55); pl.raw('\\draw[thick] '+' -- '.join(pt(pl.c(*p)) for p in (A5,B5,C5))+' -- cycle;')
for p in (A5,B5,C5): pl.dot(*p)
pl.lab('A',*A5,-1,-.6,.3); pl.lab('B',*B5,1,-.4,.3); pl.lab('C',*C5,0,1,.3)
SK5=pl.svg()
q('0005',tipId='ge-di-ucgen-alan',tip='Koordinatlı üçgenin alanı',z='orta',alt='Izgarada Üçgen Alanı',kaz='Izgara noktalarında köşeleri bulunan üçgenin alanını hesaplar.',kalip='hikâyeli',
 kart='K-GDQ-05 (koordinatlı üçgenin alanı) · A(1, 1), B(7, 3), C(3, 6)',
 metin='Üçgen biçimli bir parsel, bir karesinin kenarı 1 metre olan kareli planda şekildeki gibi gösterilmiştir. Parselin köşe noktaları A, B ve C dir.\nBuna göre, parselin alanı kaç m²’dir?',
 dogru=13,yan=[(26,'Alanı hesaplarken ikiye bölmeyi unutmuş (taban × yükseklik gibi bir çarpım almış).','islem'),(17,'Dikdörtgenden köşe üçgenlerini çıkarmak yerine bu üç üçgenin alanlarını toplamış.','dikkat'),(18,'Üç köşe üçgeninden yalnız ikisini çıkarmış.','dikkat'),(30,'Üçgeni içine alan dikdörtgenin alanını üçgenin alanı sanmış.','dikkat')],
 istenen='Parselin alanı (m²).',
 ip=['Üçgenin eksenlere paralel bir kenarı var mı? Alanı hangi parçalara ayırarak ifade edebilirsin?'],
 bilgi=[ALN],
 ad=[A('Dikdörtgeni kur','Köşelerin en küçük ve en büyük apsis–ordinatlarıyla dikdörtgen çiz.','x: 1 → 7 , y: 1 → 6 → 6 × 5 = 30'),A('Köşe üçgenlerini bul','Dikdörtgende üçgenin dışında kalan üç dik üçgenin alanlarını hesapla.','6 × 2 ÷ 2 = 6 · 4 × 3 ÷ 2 = 6 · 2 × 5 ÷ 2 = 5'),A('Toplamı çıkar','Üç dik üçgenin alanı toplamını dikdörtgenden çıkar.','6 + 6 + 5 = 17'),A('Alanı yaz','Fark üçgenin alanıdır.','30 − 17 = 13')],
 puf='Alanı bilinen parçalarla ifade edebileceğin bir yol ara; her parçanın ölçülerini ızgaradan oku.',sekil=SK5)

# ===== 06 orta · hikâyeli · dik doğrunun y eksenini kestiği nokta =====
kartla('K-GDQ-06','Noktadan geçen dik doğru','Verilen doğrunun eğiminden dik doğrunun eğimi bulunur; nokta-eğim denkleminde x = 0 yazılarak y eksenini kestiği nokta elde edilir.','Dik yerine paralel eğimi almak; eğimin işaretini değiştirmemek; eğimi ters çevirmemek; kesim noktası yerine noktanın ordinatını vermek.','orta',4,'ge-di-dik','Noktadan geçen dik doğru','hikâyeli')
A6=(-3,-1); B6=(3,3); P6=(2,5); m6=egim(A6,B6); mp=-1/m6; assert m6==Fr(2,3) and mp==Fr(-3,2)
yk=lambda m: P6[1]-m*P6[0]
assert yk(mp)==8 and yk(Fr(3,2))==2 and yk(m6)==Fr(11,3) and yk(Fr(-2,3))==Fr(19,3) and P6[1]==5
pl=Pl(-5,6,-3,9,.5); pl.dogru(A6,B6); pl.dot(*A6); pl.dot(*B6); pl.dot(*P6)
pl.lab('A',*A6,1,-1.1,.3); pl.lab('B',*B6,1,-.5,.3); pl.lab('P',*P6,-1,.4,.3); pl.lab('d_1',4.6,4.4,-1,.3,.36)
SK6=pl.svg()
q('0006',tipId='ge-di-dik',tip='Noktadan geçen dik doğru',z='orta',alt='Dik Cadde',kaz='Bir doğruya dik olan ve verilen noktadan geçen doğrunun y eksenini kestiği noktayı bulur.',kalip='hikâyeli',
 kart='K-GDQ-06 (dik doğru, y ekseni) · d₁ grafikten, P(2, 5)',
 metin='Bir şehrin kareli planında, bir karesinin kenarı 1 birimdir. Şekilde d₁ caddesi ile P noktasındaki okul gösterilmiştir. P noktasından geçen ve d₁ caddesine dik olan yeni bir cadde açılacak, bu cadde y eksenini bir noktada kesecektir.\nBuna göre, yeni caddenin y eksenini kestiği noktanın ordinatı kaçtır?',
 dogru='8',yan=[('2','Dik doğrunun eğimini +3/2 almış (işaret hatası): y = 5 + 3/2 (x − 2).','bilgi'),('11/3','Dik yerine paralel doğruyu almış: eğim 2/3 olup y = 5 + 2/3 (x − 2).','dikkat'),('5','P’nin ordinatını y eksenini kestiği nokta sanmış.','dikkat'),('19/3','Eğimi ters çevirip işaretini değiştirmemiş: −2/3 alarak y = 5 − 2/3 (x − 2) yazmış.','bilgi')],
 sira=['2','11/3','5','19/3','8'],
 istenen='Yeni caddenin y eksenini kestiği noktanın ordinatı.',
 ip=['d₁’in eğimini ızgaradaki iki noktadan bul; bu eğimle dikliğin eğimler arasında kurduğu ilişkiyi kullan.'],
 bilgi=[PD,NE],
 ad=[A('d₁’in eğimini bul','A(−3, −1) ve B(3, 3) noktalarını oku.','m₁ = (3 − (−1)) / (3 − (−3)) = 4/6 = 2/3'),A('Dik doğrunun eğimini yaz','Eğimlerin çarpımı −1 olmalıdır.','m₂ = −3/2'),A('Denklemi yaz','P(2, 5) noktasından geçen doğrunun denklemini nokta-eğim biçiminde yaz.','y − 5 = −3/2 (x − 2)'),A('x = 0 yaz','y eksenini kestiği noktayı bul.','y = 5 + 3 = 8')],
 puf='Dik doğrunun eğimini bulduktan sonra, istenen eksen kesimini nokta-eğim denkleminde x = 0 yazarak elde et.',sekil=SK6)

# ===== 07 orta · orta dikme =====
kartla('K-GDQ-07','Orta dikmenin eksen kesimi','Orta nokta ve doğru parçasının eğimi bulunur; dik eğimle orta noktadan geçen doğrunun denkleminde y = 0 yazılır.','Orta dikme yerine doğru parçasının kendisini ya da paralelini almak; eğimin işaretini karıştırmak; orta noktanın apsisini cevap sanmak.','orta',4,'ge-di-ortadikme','Doğru parçasının orta dikmesi','hikâyeli')
A7=(-1,1); B7=(5,5); M7=((A7[0]+B7[0])//2,(A7[1]+B7[1])//2); assert M7==(2,3) and egim(A7,B7)==Fr(2,3)
od=(3,2,-12); assert gec(od,M7) and Fr(-od[0],od[1])==Fr(-3,2)
xk=lambda m: M7[0]-Fr(M7[1])/m   # y=0: -M_y = m(x-M_x)
assert xk(Fr(-3,2))==4 and xk(Fr(3,2))==0 and xk(Fr(2,3))==Fr(-5,2) and xk(Fr(-2,3))==Fr(13,2) and M7[0]==2
pl=Pl(-2,7,-1,7,.55); pl.seg(A7,B7); pl.dot(*A7); pl.dot(*B7); pl.lab('A',*A7,-1,.5,.3); pl.lab('B',*B7,1,-.3,.3)
SK7=pl.svg()
q('0007',tipId='ge-di-ortadikme',tip='Doğru parçasının orta dikmesi',z='orta',alt='Orta Dikme',kaz='Doğru parçasının orta dikmesinin eksenle kesim noktasını bulur.',
 kart='K-GDQ-07 (orta dikme) · A(−1, 1), B(5, 5)',kalip='hikâyeli',
 metin='Bir parkta iki heykel, bir karesinin kenarı 1 birim olan kareli planda A ve B noktalarına yerleştirilmiştir. Heykellere eşit uzaklıkta olan noktalardan geçen yürüyüş yolu, [AB] nin orta dikmesi boyunca uzanmakta ve x eksenini bir kapıda kesmektedir.\nBuna göre, kapının apsisi kaçtır?',
 dogru=4,yan=[(-2.5,'Orta dikme yerine [AB] nin bulunduğu doğruyu (ya da ona paralel olanı) kullanmış.','dikkat'),(0,'Dik doğrunun eğimini +3/2 almış (işaret hatası) ve orta noktadan geçirmiş.','bilgi'),(2,'Orta noktanın apsisini (2) kesim noktası sanmış.','dikkat'),(6.5,'Dik eğimi ters çevirmeden yalnız işaretini değiştirmiş (−2/3).','bilgi')],
 istenen='Orta dikmenin x eksenini kestiği noktanın apsisi.',
 ip=['Orta dikme [AB] nin hangi noktasından geçer ve [AB] ile nasıl bir açı yapar? Bu iki bilgiyle denklemi kur.'],
 bilgi=[ODK,PD],
 ad=[A('Orta noktayı bul','Uç noktaların koordinatlarının ortalamasını al.','M((−1 + 5)/2, (1 + 5)/2) = (2, 3)'),A('[AB] nin eğimini bul','Dikey farkı yatay farka böl.','m = (5 − 1)/(5 − (−1)) = 2/3'),A('Orta dikmenin denklemi','Eğimi −3/2 olan ve M den geçen doğru.','y − 3 = −3/2 (x − 2) → 3x + 2y − 12 = 0'),A('y = 0 yaz','x eksenini kestiği noktayı bul.','3x = 12 → x = 4')],
 puf='Orta dikme sorularında hem orta noktayı hem de dik eğimi bulmadan denklem yazma.',sekil=SK7)

# ===== 08 zor · orijine en yakın nokta =====
kartla('K-GDQ-08','Doğru üzerinde orijine en yakın nokta','En yakın nokta, orijinden doğruya inilen dikmenin ayağıdır; dik doğru ile verilen doğru kesiştirilir.','Dik yerine paralel doğruyu almak; eksen kesim noktalarını ya da orta noktasını en yakın nokta sanmak; koordinatları toplamak yerine çarpmak.','orta',5,'ge-di-enyakin','Doğru üzerinde en yakın nokta')
d8=(1,2,-10); H8=(2,4); assert gec(d8,H8) and Fr(-d8[0],d8[1])==Fr(-1,2) and 2*Fr(-1,2)==-1 and H8[1]==2*H8[0] and sum(H8)==6
assert [(x,y) for x in range(-20,21) for y in range(-20,21) if y==2*x and gec(d8,(x,y))]==[H8]
assert 2*Fr(5,2)==5 and Fr(5)+Fr(5,2)==Fr(15,2) and sum((0,5))==5 and sum((10,0))==10 and H8[0]*H8[1]==8
pl=Pl(-1,11,-1,7,.4,grid=False); pl.dogru((0,5),(10,0)); pl.lab('d',9.1,0.45,1,1,.34)
SK8=pl.svg()
q('0008',tipId='ge-di-enyakin',tip='Doğru üzerinde en yakın nokta',z='orta',alt='Orijine En Yakın Nokta',kaz='Doğru üzerinde orijine en yakın noktayı dik doğru yardımıyla bulur.',
 kart='K-GDQ-08 (en yakın nokta) · x + 2y − 10 = 0, O(0, 0)',
 metin='Şekilde, analitik düzlemde denklemi x + 2y − 10 = 0 olan d doğrusu ve O başlangıç noktası gösterilmiştir. d doğrusu üzerindeki noktalar arasında O noktasına uzaklığı en küçük olan nokta H(a, b) dir. Şekil ölçekli değildir.\nBuna göre, a + b toplamı kaçtır?',
 dogru=6,yan=[(5,'Doğrunun y eksenini kestiği noktanın ordinatını (5) en yakın nokta sanmış.','dikkat'),(7.5,'Dik yerine eğimi 1/2 olan doğruyu çizmiş: H(5, 5/2).','bilgi'),(8,'En yakın noktayı doğru bulmuş (H(2, 4)) ama koordinatları toplamak yerine çarpmış.','islem'),(10,'Doğrunun x eksenini kestiği noktanın apsisini (10) en yakın nokta sanmış.','dikkat')],
 istenen='a + b toplamı.',
 ip=['Uzaklığın en küçük olduğu konumda [OH] ile d doğrusu arasındaki ilişkiyi düşün.'],
 bilgi=[PD,KES],
 ad=[A('d’nin eğimini bul','x + 2y − 10 = 0 için eğim −a/b dir.','m = −1/2'),A('Dikmenin eğimi','O’dan geçen dikmenin eğimi −1/m dir.','m′ = 2 → y = 2x'),A('Kesişimi bul','y = 2x i d’de yerine yaz.','x + 4x − 10 = 0 → x = 2 , y = 4'),A('Toplamı yaz','H(2, 4) için a + b.','2 + 4 = 6')],
 puf='“En yakın” ifadesi görünce dik doğruyu düşün; bulduğun noktanın verilen doğruyu sağladığını kontrol et.',sekil=SK8)

# ===== 09 zor · iki doğru ve y ekseninin sınırladığı üçgen =====
kartla('K-GDQ-09','İki doğru ve y ekseninin üçgeni','Grafikten bir doğrunun denklemi yazılır; ikinci doğruyla kesişim ve y eksenindeki kesimler bulunur; taban y ekseni üzerinde, yükseklik kesişimin apsisidir.','Yüksekliği kesişimin ordinatı almak; tabanı eksen kesimlerinden birinden almak; yarıya bölmeyi unutmak ya da iki kez bölmek.','zor',5,'ge-di-ucgen-alan','Koordinatlı üçgenin alanı')
d1_=(2,-1,-2); d2_=(1,1,-10); K9=(4,6); assert gec(d1_,K9) and gec(d2_,K9) and gec(d1_,(0,-2)) and gec(d1_,(2,2)) and gec(d2_,(0,10))
taban=10-(-2); h9=K9[0]; al9=Fr(taban*h9,2); assert al9==24
assert taban==12 and Fr(10*4,2)==20 and Fr((6+2)*4,2)==16 and Fr(4*4,2)==8
pl=Pl(-2,6,-4,9,.5); pl.dogru((0,-2),(2,2)); pl.dot(0,-2); pl.dot(2,2); pl.lab('d_1',3.5,4.8,-1,.3,.36)
SK9=pl.svg()
q('0009',tipId='ge-di-ucgen-alan',tip='Koordinatlı üçgenin alanı',z='zor',alt='İki Doğru ve Eksen',kaz='İki doğru ile y ekseninin sınırladığı üçgenin alanını doğruların denklemlerinden bulur.',
 kart='K-GDQ-09 (iki doğru ve y ekseni) · d₁ grafikten, x + y − 10 = 0',
 metin='Şekilde, bir karesinin kenarı 1 birim olan kareli düzlemde d₁ doğrusu verilmiştir. Denklemi x + y − 10 = 0 olan d₂ doğrusu şekilde gösterilmemiştir. d₁ doğrusu, d₂ doğrusu ve y ekseni bir üçgen oluşturmaktadır.\nBuna göre, bu üçgenin alanı kaç birimkaredir?',
 dogru=24,yan=[(8,'Kesişim noktasının koordinatlarını taban ve yükseklik sanmış: 4 × 4 ÷ 2.','bilgi'),(12,'Üçgenin yalnız tabanının uzunluğunu (y eksenindeki parça) vermiş.','dikkat'),(16,'Tabanı −2 ile 6 arasında (8 birim) almış: 8 × 4 ÷ 2.','bilgi'),(20,'d₂’nin y eksenini kestiği 10’u taban sanıp 10 × 4 ÷ 2 işlemini yapmış.','dikkat')],
 istenen='Üçgenin alanı (birimkare).',
 ip=['Önce d₁’in denklemini yaz, sonra iki doğrunun ortak noktasını bul; üçgenin köşelerinden ikisi y ekseni üzerindedir.'],
 bilgi=[KES,NE,EKS],
 ad=[A('d₁’in denklemini yaz','Izgaradan (0, −2) ve (2, 2) noktalarını oku.','m = 4/2 = 2 → y = 2x − 2'),A('Kesişimi bul','d₂’den y = 10 − x yazıp d₁’de yerine koy.','2x − 2 = 10 − x → x = 4 , y = 6'),A('y eksenindeki köşeleri bul','d₁ için x = 0, d₂ için x = 0.','(0, −2) ve (0, 10) → taban = 12'),A('Yüksekliği belirle','Kesişim noktasının y eksenine uzaklığı yüksekliktir.','h = 4'),A('Alanı hesapla','Taban × yükseklik ÷ 2.','12 × 4 ÷ 2 = 24')],
 puf='Alanı istenen üçgenin köşelerini ayrı ayrı belirle; bir kenarı eksen üzerindeyse onu taban al.',sekil=SK9)

# ===== 10 zor · yükseklik uzunluğu =====
kartla('K-GDQ-10','Köşeden karşı kenara uzaklık','Karşı kenarın doğru denklemi iki köşeden yazılır; üçüncü köşenin bu doğruya uzaklığı yüksekliği verir.','Payı hesaplayıp paydayı atlamak; alanı yükseklik sanmak; taban uzunluğunu yükseklik sanmak.','orta',4,'ge-di-uzaklik','Noktanın doğruya uzaklığı')
A10=(1,6); B10=(0,-1); C10=(6,7); bc=(4,-3,-3); assert gec(bc,B10) and gec(bc,C10) and egim(B10,C10)==Fr(4,3)
h10=uzk(bc,A10)/5; assert h10==Fr(17,5)
al10=Fr(abs(A10[0]*(B10[1]-C10[1])+B10[0]*(C10[1]-A10[1])+C10[0]*(A10[1]-B10[1])),2); BCu=dist(B10,C10); assert al10==17 and abs(BCu-10)<1e-9 and Fr(2*17,10)==h10
assert Fr(2*17,5)==Fr(34,5) and uzk(bc,A10)==17 and Fr(abs(4*1-3*6+3),5)==Fr(11,5) and 2*17==34
pl=Pl(-2,8,-3,9,.5,o=(-.3,.25)); pl.raw('\\draw[thick] '+' -- '.join(pt(pl.c(*p)) for p in (A10,B10,C10))+' -- cycle;')
for p in (A10,B10,C10): pl.dot(*p)
pl.lab('A',*A10,-1,.5,.3); pl.lab('B',*B10,1,-.9,.32); pl.lab('C',*C10,1,.3,.3)
SK10=pl.svg()
q('0010',tipId='ge-di-uzaklik',tip='Noktanın doğruya uzaklığı',z='orta',alt='Üçgende Yükseklik',kaz='Köşegen koordinatları verilen üçgende bir köşeden karşı kenara olan uzaklığı hesaplar.',
 kart='K-GDQ-10 (köşeden karşı kenara uzaklık) · A(1, 6), B(0, −1), C(6, 7)',
 metin='Şekilde, bir karesinin kenarı 1 birim olan kareli düzlemde köşeleri A, B ve C olan bir üçgen verilmiştir. A köşesinden [BC] kenarına bir dikme indirilecektir.\nBuna göre, A köşesinden [BC] kenarına inen yüksekliğin uzunluğu kaç birimdir?',
 dogru=3.4,yan=[(6.8,'İki alanı (34) |BC| yerine denklem katsayılarından bulduğu 5 ile bölmüş.','islem'),(10,'|BC| uzunluğunu yükseklik sanmış.','dikkat'),(17,'Uzaklık formülünde payı (17) bulmuş ama paydadaki 5 ile bölmemiş.','islem'),(34,'Üçgenin alanının iki katını (34) yükseklik olarak vermiş.','dikkat')],
 istenen='Yüksekliğin uzunluğu (birim).',
 ip=['A noktasından [BC] ye olan uzaklığı ifade etmek için hangi bilgiye ihtiyacın var?'],
 bilgi=[UZK,NE],
 ad=[A('[BC] nin eğimini bul','B(0, −1) ve C(6, 7) noktalarını oku.','m = (7 − (−1)) / (6 − 0) = 4/3'),A('BC doğrusunun denklemi','B(0, −1) den geçen doğru y = 4x/3 − 1.','4x − 3y − 3 = 0'),A('A’nın uzaklığını yaz','A(1, 6) için pay ve paydayı hesapla.','|4 × 1 − 3 × 6 − 3| = 17 , √(4² + 3²) = 5'),A('Yüksekliği bul','Payı paydaya böl.','17 / 5 = 3,4')],
 puf='Koordinatlı üçgende uzunluk isteniyorsa, ızgaradan okunabilen ve hesaplanması gereken ölçüleri ayır.',sekil=SK10)

kayit_yaz()
