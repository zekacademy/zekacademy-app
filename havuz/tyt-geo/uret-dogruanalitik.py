"""TYT Geometri · Doğrunun Analitiği (hafif mod; kardeş yok, ipucu 1). Koordinatlar Python'da hesaplanır, TikZ gövdesi aynı değerlerden üretilir; her cevap ve çeldirici değeri assert edilir."""
import sys,os,math,json
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
from math import sin,cos,tan,radians,degrees,atan2,sqrt,pi
from fractions import Fraction as Fr
ONEK='dogruanalitik'
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
    P.yaz(os.path.join(GD,ONEK+'-1.json'),os.path.join('/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/hn_analitik','bos-'+ONEK+'.json'))
    tipler={}
    for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=TIPK[c['tipId']]))['kartlar'].append(c['id'])
    json.dump(dict(konu=P.konu_adi,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 TYT Geometri çıkmış soruları (yalnız mantık), MEB 9–10. sınıf geometri müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar',ONEK+'.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler),'soru',len(P.ANA))
EGIM=B('Doğrunun eğimi','A(x₁, y₁) ve B(x₂, y₂) noktalarından geçen doğrunun eğimi m = (y₂ − y₁) / (x₂ − x₁) dir; sağa doğru yükselen doğrunun eğimi pozitif, alçalanın negatiftir. Örnek: (1, 2) ve (4, 8) noktalarından geçen doğrunun eğimi 6/3 = 2’dir')
ACI=B('Eğim ve açı','doğrunun x ekseninin pozitif yönüyle yaptığı açı α ise eğim m = tan α dır. tan 30° = √3/3, tan 45° = 1, tan 60° = √3 tür; geniş açıda eğim negatiftir ve dar açı karşılığının değerinin eksilisidir. Örnek: α = 150° için m = −√3/3')
DENK=B('Doğru denklemi','eğimi m olan ve (x₁, y₁) noktasından geçen doğrunun denklemi y − y₁ = m(x − x₁) dir. Örnek: eğimi 3 ve (1, 2) noktasından geçen doğru y − 2 = 3(x − 1), yani 3x − y − 1 = 0 dır')
EKS=B('Eksenleri kestiği noktalar','x eksenini kestiği nokta için y = 0, y eksenini kestiği nokta için x = 0 yazılır. Örnek: x + 2y − 6 = 0 doğrusu x eksenini (6, 0), y eksenini (0, 3) noktasında keser')
PD=B('Paralel ve dik doğrular','paralel doğruların eğimleri eşittir (m₁ = m₂); dik doğruların eğimlerinin çarpımı −1 dir (m₁ × m₂ = −1). ax + by + c = 0 doğrusunun eğimi −a/b dir. Örnek: 2x + y − 5 = 0 doğrusunun eğimi −2, ona dik doğrunun eğimi 1/2’dir')
KES=B('İki doğrunun kesişimi','kesişim noktasının koordinatları iki doğru denkleminin ortak çözümüdür; denklemler birlikte çözülür. Örnek: y = x + 1 ve x + y = 5 için x + 1 + x = 5 → x = 2 ve y = 3, kesişim noktası (2, 3)’tür')
GRF=B('Grafikten denklem okuma','doğrunun üzerindeki ızgara noktalarından eksenleri kestiği noktalar okunur; (a, 0) ve (0, b) noktalarından geçen doğru x/a + y/b = 1 dir. Örnek: (3, 0) ve (0, 2) noktalarından geçen doğru x/3 + y/2 = 1, yani 2x + 3y − 6 = 0 dır')
konu('geo|Doğrunun Analitiği','Doğrunun Analitiği')
def egim(a,b): return Fr(b[1]-a[1],b[0]-a[0])
def gec(eq,p): return eq[0]*p[0]+eq[1]*p[1]+eq[2]==0

# ===== 01 eğim (iki noktadan) · kolay =====
kartla('K-GDO-01','İki noktadan eğim','Izgaradan okunan iki noktanın dikey farkı yatay farkına bölünür; işaret doğrunun yönünden belirlenir.','Oranı ters yazmak; işareti atlamak; farkları çıkarmak.','kolay',3,'ge-do-egim','Eğim (iki noktadan ve açıdan)')
A1=(-3,-2); B1=(3,7); m1=egim(A1,B1); assert m1==Fr(3,2) and egim(B1,A1)==m1
assert Fr(6,9)==Fr(2,3) and -m1==Fr(-3,2) and B1[1]-A1[1]-(B1[0]-A1[0])==3
pl=Pl(-4,5,-3,8,.5); pl.lin(A1,B1,-.08,1.08); pl.dot(*A1); pl.dot(*B1); pl.lab('A',*A1,-1,-.3,.28); pl.lab('B',*B1,1,.3,.28)
SK1=pl.svg()
q('0001',tipId='ge-do-egim',tip='Eğim (iki noktadan ve açıdan)',z='kolay',alt='İki Noktadan Eğim',kaz='Izgarada iki noktası verilen doğrunun eğimini hesaplar.',
 kart='K-GDO-01 (eğim) · ızgaradan okunan iki nokta',
 metin='Şekilde, bir karesinin kenarı 1 birim olan kareli düzlemde bir d doğrusu ile bu doğru üzerindeki A ve B noktaları verilmiştir.\nBuna göre, d doğrusunun eğimi kaçtır?',
 dogru='3/2',sira=['−3/2','−2/3','2/3','3/2','3'],
 yan=[('2/3','Yatay farkı dikey farka bölmüş (6/9); eğim dikey farkın yatay farka oranıdır.','bilgi'),('−3/2','Doğrunun sağa doğru yükseldiğini (eğimin pozitif olduğunu) görmeden işaret koymuş.','dikkat'),('−2/3','Hem oranı ters yazmış hem de negatif işaret koymuş.','bilgi'),('3','Dikey farktan yatay farkı çıkarmış (9 − 6).','bilgi')],
 istenen='d doğrusunun eğimi.',
 ip=['A ve B’nin koordinatlarını oku; dikey fark ile yatay farkın oranına bak.'],
 bilgi=[EGIM],
 ad=[A('Koordinatları oku','Izgaradan iki noktayı oku.','A(−3, −2) · B(3, 7)'),A('Farkları bul','Dikey fark pay, yatay fark paydadır.','Δy = 7 − (−2) = 9 · Δx = 3 − (−3) = 6'),A('Eğimi yaz','Doğru sağa doğru yükseldiği için eğim pozitiftir.','m = 9/6 = 3/2')],
 puf='Eğim = dikey fark ÷ yatay fark; yükselen doğrunun eğimi pozitiftir.',sekil=SK1)

# ===== 02 eğim (açıdan) · kolay =====
kartla('K-GDO-02','Açıdan eğim','Eğim, doğrunun x ekseninin pozitif yönüyle yaptığı açının tanjantıdır; geniş açıda tanjant negatiftir.','İşareti atlamak; 30° ile 60° değerlerini karıştırmak; kosinüsü eğim sanmak.','kolay',2,'ge-do-egim','Eğim (iki noktadan ve açıdan)')
t=radians(135); mm=tan(t); assert abs(mm+1)<1e-9 and abs(tan(radians(45))-1)<1e-9 and abs(tan(radians(60))-sqrt(3))<1e-9 and abs(tan(radians(30))-sqrt(3)/3)<1e-9
f=Pl(-3,5,-3,3,.7,grid=False,ticks=False)
Pc=(1.4,0); dr=(cos(t),sin(t)); top=add(Pc,mul(dr,2.3)); bot=sub(Pc,mul(dr,2.1))
f.line(bot,top,'thick'); f.raw(f'\\fill {pt(Pc)} circle (.06);')
f.arc(Pc,(Pc[0]+1,0),add(Pc,dr),.55,'$135^\\circ$',1.0); f.node((bot[0]+.3,bot[1]-.1),'$d$')
SK2=f.svg(); assert abs(ang(Pc,(Pc[0]+1,0),add(Pc,dr))-135)<1e-9
q('0002',tipId='ge-do-egim',tip='Eğim (iki noktadan ve açıdan)',z='kolay',alt='Açıdan Eğim',kaz='Doğrunun x ekseniyle yaptığı açıdan eğimini bulur.',
 kart='K-GDO-02 (açıdan eğim) · 135° için eğim',
 metin='Şekilde, analitik düzlemde bir d doğrusu ve bu doğrunun x ekseninin pozitif yönüyle yaptığı açı gösterilmiştir. Şekil ölçekli değildir.\nBuna göre, d doğrusunun eğimi kaçtır?',
 dogru='−1',sira=['−√3','−1','−√3/3','1','√3'],
 yan=[('1','tan 135° = tan 45° yazmış; geniş açının eğiminin negatif olduğunu atlamış.','bilgi'),('−√3','Dar açı karşılığını 60° bulup tan 60° = √3 değerinin eksilisini almış.','bilgi'),('−√3/3','Dar açı karşılığını 30° bulup tan 30° = √3/3 değerinin eksilisini almış.','bilgi'),('√3','Dar açı karşılığını 60° sanmış ve işareti de atlamış.','bilgi')],
 istenen='d doğrusunun eğimi.',
 ip=['Eğim ile doğrunun x ekseniyle yaptığı açı arasındaki ilişkiyi düşün. Açı dar mı geniş mi, eğimin işareti ne olur?'],
 bilgi=[ACI],
 ad=[A('Açıyı oku','Şekilde x ekseninin pozitif yönüyle doğru arasındaki açı verilmiş.','α = 135°'),A('Eğimi yaz','Eğim m = tan α dır.','m = tan 135°'),A('Dar açıya getir','135° geniş açıdır; eğim negatiftir ve dar açı karşılığı 180° − 135° = 45° dir.','tan 135° = −tan 45° = −1')],
 puf='Doğru x eksenine göre geniş açı yapıyorsa eğim negatiftir; dar açı karşılığıyla bulunur.',sekil=SK2)

# ===== 03 doğru denklemi · orta · hikâyeli =====
kartla('K-GDO-03','İki noktadan doğru denklemi','Izgaradan iki nokta okunur, eğim bulunur ve nokta-eğim denklemi düzenlenir.','Eğimin işaretini ya da oranını yanlış yazmak; sabit terimi yanlış noktadan almak.','orta',4,'ge-do-denklem','İki noktası verilen doğrunun denklemi','hikâyeli')
A3=(-2,3); B3=(2,-5); m3=egim(A3,B3); assert m3==-2
dog3=(2,1,1); assert gec(dog3,A3) and gec(dog3,B3)       # 2x + y + 1 = 0
ters=(1,2,-4); assert gec(ters,A3) and Fr(-ters[0],ters[1])==Fr(-1,2) and not gec(ters,B3)
isr=(2,-1,7); assert gec(isr,A3) and Fr(-isr[0],isr[1])==2        # eğim +2 : y-3=2(x+2)
sab=(2,1,-3); assert Fr(-sab[0],sab[1])==-2 and gec(sab,(0,3)) and not gec(sab,A3)
kar=(2,1,9); assert Fr(-kar[0],kar[1])==-2 and gec(kar,(-2,-5)) and not gec(kar,B3)   # y+5=-2(x+2)
pl=Pl(-4,4,-6,4,.5,o=(.22,.22)); pl.lin(A3,B3,-.1,1.1); pl.dot(*A3); pl.dot(*B3); pl.lab('A',*A3,-1,.4,.28); pl.lab('B',*B3,1,-.4,.28)
SK3=pl.svg()
q('0003',tipId='ge-do-denklem',tip='İki noktası verilen doğrunun denklemi',z='orta',alt='Doğru Denklemi',kaz='Izgaradan okunan iki noktadan geçen doğrunun denklemini yazar.',kalip='hikâyeli',
 kart='K-GDO-03 (doğru denklemi) · A(−2, 3), B(2, −5)',
 metin='Bir şehrin kareli planında, A ve B durakları arasında düz bir tramvay hattı kurulmuştur. Şekilde hattın bu iki durağı gösterilmiştir; planda bir karenin kenarı 1 birimdir ve hat, durakların üzerinden geçen doğru boyunca uzanmaktadır.\nBuna göre, hattın üzerinde bulunduğu doğrunun denklemi aşağıdakilerden hangisidir?',
 dogru='2x + y + 1 = 0',sira=['x + 2y − 4 = 0','2x − y + 7 = 0','2x + y + 1 = 0','2x + y − 3 = 0','2x + y + 9 = 0'],
 yan=[('x + 2y − 4 = 0','Eğimi ters yazmış (−1/2): y − 3 = −1/2 (x + 2) düzenlenince x + 2y − 4 = 0 bulmuş.','bilgi'),('2x − y + 7 = 0','Eğimin işaretini yanlış bulmuş (+2): y − 3 = 2(x + 2) yazıp 2x − y + 7 = 0 çıkarmış.','bilgi'),('2x + y − 3 = 0','Eğimi doğru (−2) bulmuş ama A’nın ordinatı olan 3’ü y eksenini kestiği nokta sanıp y = −2x + 3 yazmış.','dikkat'),('2x + y + 9 = 0','Noktaları karıştırıp y + 5 = −2(x + 2) yazmış (B’nin ordinatı ile A’nın apsisini birlikte kullanmış).','dikkat')],
 istenen='Doğrunun denklemi.',
 ip=['İki noktadan geçen doğrunun eğimini bul; sonra bu eğimle noktalardan birini kullanarak denklemi yaz ve ikisinin de denklemi sağladığını kontrol et.'],
 bilgi=[DENK,EGIM],
 ad=[A('Noktaları oku','Izgaradan iki durağı oku.','A(−2, 3) · B(2, −5)'),A('Eğimi bul','Dikey farkı yatay farka böl.','m = (−5 − 3) ÷ (2 − (−2)) = −8/4 = −2'),A('Denklemi yaz','A noktası ve eğimle nokta-eğim denklemi kurulur.','y − 3 = −2(x + 2) → y = −2x − 1'),A('Düzenle ve kontrol et','Tüm terimleri bir tarafa topla; B(2, −5) denklemi sağlamalı.','2x + y + 1 = 0 · 2 × 2 + (−5) + 1 = 0')],
 puf='Doğru denklemi için önce eğimi bul, sonra nokta-eğim denklemini yaz; sonucu diğer noktayla kontrol et.',sekil=SK3)

# ===== 04 eksenlerle üçgen · orta · hikâyeli =====
kartla('K-GDO-04','Eksenleri kestiği noktalar ve üçgen alanı','x=0 ve y=0 yazılarak kesim noktaları bulunur; dik kenarlar kesim noktalarının eksen üzerindeki uzaklıklarıdır.','Alanı yarıya bölmemek; hipotenüs uzunluğunu almak; kesim noktalarını toplamak.','kolay',3,'ge-do-eksen','Doğru ile eksenlerin sınırladığı üçgen','hikâyeli')
a4,b4=8,6; assert 3*a4+4*0-24==0 and 3*0+4*b4-24==0 and a4*b4//2==24 and a4*b4==48 and a4+b4==14 and a4*a4+b4*b4==100 and 3*4//2==6
pl=Pl(-1,9,-1,7,.5,grid=False,ticks=False); pl.pfill([(0,0),(a4,0),(0,b4)],'fill=vurgu!20'); pl.seg((a4,0),(0,b4)); pl.lab('d',6.0,2.2,1,.8,.3)
SK4=pl.svg()
q('0004',tipId='ge-do-eksen',tip='Doğru ile eksenlerin sınırladığı üçgen',z='kolay',alt='Eksenlerle Üçgen',kaz='Doğrunun eksenleri kestiği noktaları bulup oluşan üçgenin alanını hesaplar.',kalip='hikâyeli',
 kart='K-GDO-04 (eksenlerle üçgen) · 3x + 4y − 24 = 0',
 metin='Bir çiftçi, tarlasının sınırını koordinat düzleminde 3x + 4y − 24 = 0 doğrusuyla modellemiştir. Bu doğru ile koordinat eksenleri arasında kalan ve şekilde boyalı olarak gösterilen üçgen biçimindeki bölgeye buğday ekilecektir. Şekil ölçekli değildir; uzunluklar metre cinsindendir.\nBuna göre, buğday ekilecek bölgenin alanı kaç m²’dir?',
 dogru=24,yan=[(6,'3 ve 4 katsayılarını dik kenar sanıp 3 × 4 ÷ 2 = 6 bulmuş.','bilgi'),(10,'Alan yerine üçgenin hipotenüs uzunluğunu (√(8² + 6²) = 10) bulmuş.','dikkat'),(14,'Dik kenarların uzunluklarını toplamış (8 + 6) ve alan hesaplamamış.','dikkat'),(48,'Dik kenarları çarpmış (8 × 6) ama ikiye bölmeyi unutmuş.','islem')],
 istenen='Boyalı bölgenin alanı (m²).',
 ip=['Doğrunun x eksenini ve y eksenini kestiği noktaları bulmak için denklemde sırayla y = 0 ve x = 0 yaz.'],
 bilgi=[EKS],
 ad=[A('x eksenini kestiği nokta','Denklemde y = 0 yazılır.','3x − 24 = 0 → x = 8 → (8, 0)'),A('y eksenini kestiği nokta','Denklemde x = 0 yazılır.','4y − 24 = 0 → y = 6 → (0, 6)'),A('Dik üçgenin alanı','Dik kenarlar 8 ve 6 birimdir; alan çarpımın yarısıdır.','8 × 6 ÷ 2 = 24')],
 puf='Doğrunun eksenlerle oluşturduğu üçgenin alanı, kesim noktalarının mutlak değerlerinin çarpımının yarısıdır.',sekil=SK4)

# ===== 05 paralel doğrular · orta =====
kartla('K-GDO-05','Paralel doğrular','Grafikten okunan doğrunun eğimi bulunur; paralel doğrunun denklemindeki eğim ifadesi (−a/b) buna eşitlenir.','Eğimi a/b almak (işaret); paralel yerine dik koşulu kullanmak; m − 1 değerini m sanmak.','orta',4,'ge-do-paralel-dik','Paralel ve dik doğrular')
A5=(-1,-1); B5=(2,5); m5=egim(A5,B5); assert m5==2
# d2: (m-1)x + 2y - 7 = 0  -> eğim -(m-1)/2
sol=[m for m in range(-20,21) if Fr(-(m-1),2)==m5]; assert sol==[-3]
assert [m for m in range(-20,21) if Fr(m-1,2)==m5]==[5]                  # işaret hatası
assert [m for m in range(-20,21) if m!=1 and Fr(-2,(m-1))==m5]==[0]      # ters oran
assert [m for m in range(-20,21) if Fr(-(m-1),2)==Fr(-1,2)]==[2]          # dik koşulu
assert -3-1==-4
pl=Pl(-3,4,-4,6,.5,o=(.25,-.22)); pl.lin(A5,B5,-.3,1.15); pl.dot(*A5); pl.dot(*B5); pl.lab('A',*A5,1,-.5,.28); pl.lab('B',*B5,1,-.5,.28); pl.lab('d_1',1.3,5.2,-1,.2,.38)
SK5=pl.svg()
q('0005',tipId='ge-do-paralel-dik',tip='Paralel ve dik doğrular',z='orta',alt='Paralel Doğrular',kaz='Grafikten okunan doğrunun eğimini kullanarak paralel doğrunun denklemindeki bilinmeyeni bulur.',
 kart='K-GDO-05 (paralel doğrular) · d₁ grafikten, d₂: (m − 1)x + 2y − 7 = 0',
 metin='Şekilde, bir karesinin kenarı 1 birim olan kareli düzlemde d₁ doğrusu verilmiştir. Denklemi (m − 1)x + 2y − 7 = 0 olan d₂ doğrusu, d₁ doğrusuna paraleldir.\nBuna göre, m kaçtır?',
 dogru=-3,yan=[(-4,'Eğim eşitliğinden m − 1 = −4 bulmuş ve 1 eklemeyi unutup bunu m sanmış.','islem'),(0,'Eğimi −2/(m − 1) yazmış (katsayıları ters almış): −2/(m − 1) = 2 → m = 0.','bilgi'),(2,'Paralellik yerine dikliği kullanmış: eğimler çarpımını −1 yapıp m = 2 bulmuş.','bilgi'),(5,'ax + by + c = 0 doğrusunun eğimini a/b almış (işareti atlamış): (m − 1)/2 = 2 → m = 5.','bilgi')],
 istenen='m değeri.',
 ip=['d₁’in eğimini ızgara noktalarından bul; d₂’nin eğimini katsayılardan yazıp ikisini eşitle.'],
 bilgi=[PD,EGIM],
 ad=[A('d₁’in eğimini bul','Izgaradan iki noktayı oku ve eğimi hesapla.','A(−1, −1) · B(2, 5) → m₁ = 6/3 = 2'),A('d₂’nin eğimini yaz','ax + by + c = 0 için eğim −a/b dir.','m₂ = −(m − 1)/2'),A('Paralellik koşulunu yaz','Paralel doğruların eğimleri eşittir.','−(m − 1)/2 = 2 → m − 1 = −4'),A('m’yi bul','Her iki tarafa 1 ekle.','m = −3')],
 puf='ax + by + c = 0 doğrusunun eğimi −a/b dir; paralellikte eğimler eşit, dikte çarpım −1 olur.',sekil=SK5)

# ===== 06 kesişim · orta · hikâyeli =====
kartla('K-GDO-06','İki doğrunun kesişimi','Grafikten bir doğrunun denklemi yazılır; ikinci denklemle birlikte çözülüp kesişim noktası bulunur.','Yalnız bir koordinatı vermek; koordinatları toplamak ya da çıkarmak; ordinatı apsis sanmak.','orta',4,'ge-do-kesisim','İki doğrunun kesişim noktası','hikâyeli')
A6=(0,-3); B6=(2,1); m6=egim(A6,B6); assert m6==2
# d1: y = 2x - 3 ; d2: x + 2y - 14 = 0
sol6=[(x,y) for x in range(-30,31) for y in range(-30,31) if y==2*x-3 and x+2*y-14==0]; assert sol6==[(4,5)]
a6,b6=4,5; assert a6*b6==20 and a6+b6==9 and b6-a6==1
pl=Pl(-2,8,-4,8,.45); pl.lin(A6,B6,-.3,2.2); pl.dot(*A6); pl.dot(*B6); pl.lab('d_1',3.6,4.3,-1,.2,.38); pl.lab('A',*A6,1,-.5,.28); pl.lab('B',*B6,1,-.4,.28)
SK6=pl.svg()
q('0006',tipId='ge-do-kesisim',tip='İki doğrunun kesişim noktası',z='orta',alt='Kesişim Noktası',kaz='Biri grafikle, diğeri denklemle verilen iki doğrunun kesişim noktasını bulur.',kalip='hikâyeli',
 kart='K-GDO-06 (kesişim) · d₁ grafikten, d₂: x + 2y − 14 = 0',
 metin='Bir şehrin kareli planında iki cadde birer doğru olarak modellenmiştir; bir karenin kenarı 1 birimdir. d₁ caddesi şekilde gösterilmiştir, d₂ caddesinin denklemi x + 2y − 14 = 0 dır. İki caddenin kesiştiği kavşak K(a, b) noktasıdır.\nBuna göre, a · b çarpımı kaçtır?',
 dogru=20,yan=[(1,'Koordinatları çarpmak yerine ordinattan apsisi çıkarmış (5 − 4).','dikkat'),(4,'Yalnız kavşağın apsisini (a = 4) bulup cevap vermiş.','dikkat'),(5,'Yalnız kavşağın ordinatını (b = 5) bulup cevap vermiş.','dikkat'),(9,'Koordinatları çarpmak yerine toplamış (4 + 5).','dikkat')],
 istenen='a · b çarpımı.',
 ip=['d₁’in denklemini ızgaradaki iki noktadan yaz; sonra iki denklemi birlikte çöz.'],
 bilgi=[KES,DENK],
 ad=[A('d₁’in denklemini yaz','Eğimi ve y eksenini kestiği noktayı ızgaradan oku.','(0, −3) ve (2, 1) → m = 2 → y = 2x − 3'),A('Yerine koy','d₁’deki y ifadesini d₂’de yerine yaz.','x + 2(2x − 3) − 14 = 0 → 5x = 20 → x = 4'),A('Ordinatı bul','x = 4’ü d₁’de yerine koy.','y = 2 × 4 − 3 = 5 → K(4, 5)'),A('Çarpımı yaz','Apsis ile ordinatı çarp.','4 × 5 = 20')],
 puf='Kesişim noktası iki denklemin ortak çözümüdür: birinde y’yi (ya da x’i) çekip öbüründe yerine yaz.',sekil=SK6)

# ===== 07 dik doğru ve alan · zor =====
kartla('K-GDO-07','Dik doğru ve eksenlerle üçgen','Verilen doğrunun eğiminden dik doğrunun eğimi bulunur; noktadan geçen dik doğrunun denklemi ve eksenleri kestiği noktalar bulunup alan hesaplanır.','Dik doğru yerine paralel eğimi almak; işareti atlamak; sabit terimi yanlış noktadan almak; alanı yarıya bölmemek.','zor',5,'ge-do-paralel-dik','Paralel ve dik doğrular')
d7=(3,-2,6); md=Fr(-d7[0],d7[1]); assert md==Fr(3,2) and gec(d7,(-2,0)) and gec(d7,(0,3))
A7=(3,4); mp=Fr(-1)/md; assert mp==Fr(-2,3)
dik7=(2,3,-18); assert gec(dik7,A7) and Fr(-dik7[0],dik7[1])==mp
x7=Fr(18,2); y7=Fr(18,3); assert (x7,y7)==(9,6) and x7*y7/2==27 and x7*y7==54
# eğim 2/3 : y-4=2/3(x-3) -> 2x-3y+6=0
isr7=(2,-3,6); assert gec(isr7,A7) and Fr(-isr7[0],isr7[1])==Fr(2,3); a_=Fr(-isr7[2],isr7[0]); b_=Fr(-isr7[2],isr7[1]); assert (abs(a_),abs(b_))==(3,2) and abs(a_)*abs(b_)/2==3
# y-kesim 4 sanma: y=-2x/3+4 -> kesimler 6 ve 4
assert Fr(4)/Fr(2,3)==6 and 6*4//2==12
assert (3+4)==7 and Fr(49,2)==Fr(49,2)*1 and float(Fr(49,2))==24.5
# iki kesim de 9: eğim -1
pl=Pl(-3,10,-1,7,.42); pl.lin((-2,0),(0,3),-.4,2.3); pl.dot(*A7); pl.lab('A',*A7,.4,1,.28); pl.lab('d',2.3,6.3,1,0,.35)
SK7=pl.svg()
q('0007',tipId='ge-do-paralel-dik',tip='Paralel ve dik doğrular',z='zor',alt='Dik Doğru ve Alan',kaz='Verilen doğruya dik olan doğrunun denklemini yazıp eksenlerle oluşturduğu üçgenin alanını hesaplar.',
 kart='K-GDO-07 (dik doğru) · d: 3x − 2y + 6 = 0, A(3, 4)',
 metin='Şekilde, bir karesinin kenarı 1 birim olan kareli düzlemde A noktası ve denklemi 3x − 2y + 6 = 0 olan d doğrusu gösterilmiştir. A noktasından geçen ve d doğrusuna dik olan bir doğru çizilecektir.\nBuna göre, bu doğrunun koordinat eksenleriyle sınırladığı üçgenin alanı kaç birimkaredir?',
 dogru=27,yan=[(3,'Dik doğrunun eğimini 2/3 almış (ters çevirmiş ama işaret değiştirmemiş); kesim noktaları −3 ve 2 çıkıp alan 3 bulunmuş.','bilgi'),(12,'Eğimi doğru (−2/3) bulmuş ama sabit terim olarak A’nın ordinatı 4’ü y eksenini kestiği nokta sanmış: kesim noktaları 6 ve 4.','dikkat'),(24.5,'Dik doğrunun eğimini −1 sanmış: A(3, 4) ten geçen doğru x + y − 7 = 0, kesim noktaları 7 ve 7, alan 7 × 7 ÷ 2.','bilgi'),(54,'Kesim noktalarını doğru bulmuş (9 ve 6) ama alanı ikiye bölmemiş.','islem')],
 istenen='Üçgenin alanı (birimkare).',
 ip=['d doğrusunun eğimini bul; dik doğrunun eğimi için çarpımın −1 olduğunu kullan.'],
 bilgi=[PD,DENK,EKS],
 ad=[A('d’nin eğimi','3x − 2y + 6 = 0 için eğim −a/b dir.','m = −3/(−2) = 3/2'),A('Dik doğrunun eğimi','Eğimlerin çarpımı −1 olmalıdır.','m′ = −2/3'),A('Denklemi yaz','A(3, 4) noktasından geçen doğrunun denklemini nokta-eğim biçiminde yaz.','y − 4 = −2/3 (x − 3) → 2x + 3y − 18 = 0'),A('Kesim noktaları','Sırayla y = 0 ve x = 0 yaz.','x = 9 → (9, 0) · y = 6 → (0, 6)'),A('Alanı hesapla','Dik kenarlar 9 ve 6’dır.','9 × 6 ÷ 2 = 27')],
 puf='Dik doğrunun eğimi, verilen eğimin ters çevrilip işareti değiştirilmişidir; eksenlerle üçgen için kesim noktalarını bul.',sekil=SK7)

# ===== 08 grafikten denklem okuma · zor =====
kartla('K-GDO-08','Grafikten denklem okuma','Izgaradan eksenleri kestiği noktalar okunur; denklem yazılıp bir noktanın doğru üzerinde olma koşuluyla bilinmeyen bulunur.','Eğimi ters ya da ters işaretli almak; sabit terimi atlamak; kesim noktasının işaretini yanlış okumak.','zor',4,'ge-do-grafik','Grafikten doğru denklemi okuma')
P8=(6,0); Q8=(0,-4); m8=egim(P8,Q8); assert m8==Fr(2,3)
d8=(2,-3,-12); assert gec(d8,P8) and gec(d8,Q8)
k8=[k for k in range(-40,41) if gec(d8,(k,8))]; assert k8==[18]
assert [k for k in range(-60,61) if Fr(2,3)*k-4==8][0]==18
assert [k for k in range(-60,61) if Fr(-2,3)*k+4==8]==[-6]          # y-kesimini +4 okumuş
assert [k for k in range(-60,61) if Fr(2*k+12,3)==8]==[6]           # sabit terim işareti: 2k - 24 + 12 = 0
assert [k for k in range(-60,61) if Fr(3,2)*k-4==8]==[8]            # eğim ters
assert [k for k in range(-60,61) if Fr(2,3)*k==8]==[12]             # sabit terim unutulmuş
pl=Pl(-2,8,-6,3,.5); pl.lin(P8,Q8,-.3,1.3); pl.dot(*P8); pl.dot(*Q8); pl.lab('d',7.2,1.9,0,1,.3)
SK8=pl.svg()
q('0008',tipId='ge-do-grafik',tip='Grafikten doğru denklemi okuma',z='zor',alt='Grafikten Denklem',kaz='Grafikten okuduğu eksen kesim noktalarıyla doğrunun denklemini yazar ve bir noktanın koşulundan bilinmeyeni bulur.',
 kart='K-GDO-08 (grafikten denklem) · (6, 0) ve (0, −4), A(k, 8)',
 metin='Şekilde, bir karesinin kenarı 1 birim olan kareli düzlemde d doğrusu ve bu doğrunun eksenleri kestiği noktalar gösterilmiştir. Koordinatları (k, 8) olan A noktası d doğrusu üzerindedir; A şekilde gösterilmemiştir.\nBuna göre, k kaçtır?',
 dogru=18,yan=[(-6,'Doğrunun y eksenini +4’te kestiğini okuyup eğimi −2/3 almış: −2k/3 + 4 = 8.','dikkat'),(6,'Denklemde sabit terimin işaretini yanlış yazmış: 2k − 3 × 8 + 12 = 0 → k = 6.','islem'),(8,'Eğimi ters (3/2) almış: 3k/2 − 4 = 8 → k = 8.','bilgi'),(12,'Denklemde sabit terimi (−12) unutmuş: 2k − 24 = 0 → k = 12.','islem')],
 istenen='k değeri.',
 ip=['Doğrunun eksenleri kestiği noktalardan eğimi ve y eksenini kestiği noktayı oku, denklemi yaz; sonra (k, 8) noktasını denklemde yerine koy.'],
 bilgi=[GRF,DENK],
 ad=[A('Noktaları oku','Izgaradan eksenleri kestiği noktaları oku.','(6, 0) ve (0, −4)'),A('Eğimi bul','Dikey farkı yatay farka böl.','m = (−4 − 0) ÷ (0 − 6) = 2/3'),A('Denklemi yaz','y eksenini kestiği nokta −4 olduğundan y = mx + n biçiminde yaz.','y = 2x/3 − 4 → 2x − 3y − 12 = 0'),A('A noktasını yerine koy','(k, 8) noktası d üzerinde olduğundan denklemi sağlar.','2k − 3 × 8 − 12 = 0'),A('k’yi bul','Denklemi çöz.','2k = 36 → k = 18')],
 puf='Grafikten denklem için önce eksenleri kestiği noktaları oku; sonra bilinen noktayı denklemde yerine koyarak bilinmeyeni bul.',sekil=SK8)

kayit_yaz()
