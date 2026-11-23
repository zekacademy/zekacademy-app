"""AYT Fizik · Enerji ve Hareket · 20 soru (kardeş yok, ipucu 1). Şekil değerleri Python'da hesaplanır; her cevap ve çeldirici assert edilir."""
import sys,os,math,json
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-fiz'))
import _hafif as H
from _hafif import *
from cizim import tikz_svg
from math import sin,cos,radians,degrees,atan2,sqrt,pi
from math import isqrt
H.KONU='Enerji ve Hareket'
P=Parti('enerji','Enerji ve Hareket','afiz|Enerji ve Hareket',ders='AYT Fizik',idon='aytfiz')
KY='ÖSYM AYT 2018–2026 Fizik (Enerji ve Hareket; yalnız mantık) · 345 AYT Fizik s.97–117 · MEB 11–12. sınıf fizik'
g=10
TIPLER={'en-kor':'Sürtünmesiz yolda mekanik enerjinin korunumu','en-fx':'Kuvvet–konum grafiğinden iş ve kinetik enerji','en-yay':'Yay potansiyel enerjisi',
 'en-yayhar':'Yay ve cismin hareketi','en-surt':'Sürtünmeli yollarda enerji','en-isteo':'İş–enerji teoremi','en-sistem':'Cisim sistemlerinde enerji','en-guc':'Güç ve verim'}
def kk(no,alt,fikir,tuzak,z,kalip,adim,tipId):
    kart(f'K-AFEN-{no:02d}',alt,fikir,tuzak,z,kalip,adim,tipId,TIPLER[tipId],KY)
def q(no,ad,**k):
    kn=int(no); mk(P,no,ad=ad,adim=len(ad),kart=f'K-AFEN-{kn:02d} ('+CARD[kn]+')',**k)
CARD={}
def card(no,alt,fikir,tuzak,z,kalip,adim,tipId,ozet):
    kk(no,alt,fikir,tuzak,z,kalip,adim,tipId); CARD[no]=ozet
# ---------- TikZ yardımcıları
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
ARR='-{Stealth[length=1.9mm,width=1.7mm]}'
DARR='{Stealth[length=1.7mm,width=1.5mm]}-{Stealth[length=1.7mm,width=1.5mm]}'
def N(x,y,t,o=''): return f'\\node[{o}] at ({x:.3f},{y:.3f}) {{{t}}};'
def D(a,b,o='thick'): return f'\\draw[{o}] ({a[0]:.3f},{a[1]:.3f}) -- ({b[0]:.3f},{b[1]:.3f});'
def AR(a,b,o='vurgu,very thick'): return f'\\draw[{o},{ARR}] ({a[0]:.3f},{a[1]:.3f}) -- ({b[0]:.3f},{b[1]:.3f});'
def DM(a,b,o='thin'): return f'\\draw[{o},{DARR}] ({a[0]:.3f},{a[1]:.3f}) -- ({b[0]:.3f},{b[1]:.3f});'
def ticks(p0,p1,n,dx=-.14,dy=-.14,o='thin'):
    seg=[]
    for k in range(n+1):
        t=k/n; x=p0[0]+(p1[0]-p0[0])*t; y=p0[1]+(p1[1]-p0[1])*t
        seg.append(f'({x:.3f},{y:.3f}) -- ({x+dx:.3f},{y+dy:.3f})')
    return f'\\draw[{o}] '+' ('.join(seg).replace(') -- (',') -- (')+';' if False else '\\draw[thin] '+' '.join(seg)+';'
def zemin(x0,x1,y=0): return D((x0,y),(x1,y),'thick')+ticks((x0+.15,y),(x1,y),int((x1-x0)/.22))
def tikz(lines): return tikz_svg(HEAD+'\n'.join(lines)+TAIL)
def yay(p,q_,n=8,amp=2.2):
    L=math.hypot(q_[0]-p[0],q_[1]-p[1])
    return f'\\draw[thick,decorate,decoration={{coil,aspect=.5,segment length={L/n:.3f}cm,amplitude={amp}mm}}] ({p[0]:.3f},{p[1]:.3f}) -- ({q_[0]:.3f},{q_[1]:.3f});'
def duvar(x,y0,y1,sol=True):
    dx=-.16 if sol else .16
    return D((x,y0),(x,y1),'thick')+ticks((x,y0+.12),(x,y1),max(2,int((y1-y0)/.2)),dx,-.12)
def blok(x,y,w,h,t='',fill='gray!25'):
    return f'\\draw[thick,fill={fill}] ({x:.3f},{y:.3f}) rectangle ({x+w:.3f},{y+h:.3f});'+(N(x+w/2,y+h/2,t,'font=\\scriptsize') if t else '')
def axis(plots,xmax,ymax,xt,yt,xl,yl,w=6.6,h=5.0,ymin=0):
    return ['\\begin{axis}['+f'width={w}cm,height={h}cm,xmin=0,xmax={xmax},ymin={ymin},ymax={ymax},xtick={{{xt}}},ytick={{{yt}}},grid=both,major grid style={{gray!55,thin}},tick label style={{font=\\scriptsize}},axis lines=left,xlabel={{{xl}}},ylabel={{{yl}}}]']+plots+['\\end{axis}']
# ---------- öncüllü yardımcısı
SIR=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
SETS={'Yalnız I':{'I'},'Yalnız II':{'II'},'Yalnız III':{'III'},'I ve II':{'I','II'},'I ve III':{'I','III'},'II ve III':{'II','III'},'I, II ve III':{'I','II','III'}}
def onc(truth,why,pos):
    nm=['I','II','III']; C={n for n,t in zip(nm,truth) if t}
    dogru=[s for s in SIR if SETS[s]==C][0]; p=SIR.index(dogru)
    cand=[s for s in SIR if s!=dogru]
    key=lambda s:(len(SETS[s]^C),abs(SIR.index(s)-p))
    bef=sorted([s for s in cand if SIR.index(s)<p],key=key)[:pos]; aft=sorted([s for s in cand if SIR.index(s)>p],key=key)[:4-pos]
    assert len(bef)==pos and len(aft)==4-pos,(dogru,pos)
    sec=bef+aft; yan=[]
    for s in sec:
        ex=sorted(SETS[s]-C,key=nm.index); ms=sorted(C-SETS[s],key=nm.index); parts=[]
        for n in ex: parts.append(f'{n}. yargıyı da doğru sanmış; {why[nm.index(n)]}.')
        for n in ms: parts.append(f'{n}. yargının doğru olduğunu görememiş; {why[nm.index(n)]}.')
        yan.append((s,' '.join(parts),'bilgi' if ex else 'dikkat'))
    sira=sorted(sec+[dogru],key=SIR.index); assert sira.index(dogru)==pos
    return dict(dogru=dogru,sira=sira,yan=yan)
EK=B('Kinetik ve potansiyel enerji','E_k = ½ × m × v², E_p = m × g × h. Sürtünmesiz yolda E_k + E_p sabit kalır. Örnek: 2 kg’lık cisim 3 m alçalırsa 2 × 10 × 3 = 60 J kinetik enerji kazanır')
IT=B('İş–enerji teoremi','cisme etkiyen tüm kuvvetlerin yaptığı işlerin toplamı kinetik enerji değişimine eşittir: W_net = ΔE_k. Örnek: 10 N’luk net kuvvet 3 m’de 30 J’lük kinetik enerji artışı sağlar')
SU=B('Sürtünme kuvvetinin işi','sürtünme kuvveti harekete zıt olduğundan negatif iş yapar; W_s = −f × yol ve bu enerji ısıya dönüşür. f = μ × N. Örnek: f = 4 N olan yolda 3 m yol alan cisimden 12 J enerji ısıya dönüşür')
YE=B('Yay potansiyel enerjisi','yayda depolanan enerji kuvvet–uzama grafiğinin altındaki alandır: E = ½ × F × x = ½ × k × x². Örnek: k = 100 N/m, x = 0,2 m ise E = ½ × 100 × 0,04 = 2 J')
FX=B('Kuvvet–konum grafiği','grafiğin altında kalan alan, kuvvetin yaptığı işi verir; alan üçgen, dikdörtgen ya da yamuğa ayrılarak bulunur. Örnek: 6 N’luk sabit kuvvet 5 m’de 30 J iş yapar')
VE=B('Verim','verim = yararlı güç (ya da enerji) ÷ harcanan güç (ya da enerji). Örnek: 200 W harcayıp 150 W yararlı güç veren sistemin verimi %75’tir')
# ---------- ortak raylı şekil
def zeminpoly(pts,ybot):
    pp=' -- '.join(f'({x:.3f},{y:.3f})' for x,y in pts)
    return f'\\fill[gray!15] {pp} -- ({pts[-1][0]:.3f},{ybot}) -- ({pts[0][0]:.3f},{ybot}) -- cycle;\n\\draw[thick] {pp};'
def rough(x0,x1,y): # sürtünmeli bölüm: kalın çizgi + kısa taramalar
    s=f'\\draw[line width=2.2pt,gray!60] ({x0:.3f},{y:.3f}) -- ({x1:.3f},{y:.3f});'
    n=int((x1-x0)/.18)
    for i in range(n+1):
        xx=x0+i*.18; s+=f'\\draw[thin] ({xx:.3f},{y:.3f}) -- ({xx-.07:.3f},{y-.11:.3f});'
    return s
CRD=[]
# ===== 01 kolay · sürtünmesiz ray · KE
card(1,'Sürtünmesiz rayda kinetik enerji','Mekanik enerji korunur: ilk kinetik enerji ile yükseklik farkından gelen potansiyel enerji azalması toplanır.','Başlangıçtaki kinetik enerjiyi unutmak; potansiyel enerjiyi (m·g·h_K) hesaba tam katmak.','kolay','şekilli',3,'en-kor','sürtünmesiz ray, v₀ ile atılış')
m1,v01,hK1,hL1=2,6,5,Fr(9,5)
dh1=hK1-hL1; EkL1=Fr(m1*v01**2,2)+m1*g*dh1; assert dh1==Fr(16,5) and EkL1==100
assert Fr(m1*v01**2,2)==36 and m1*g*dh1==64 and Fr(m1*v01**2,2)+m1*g*hK1==136 and m1*g*dh1+m1*g*dh1==128
s1=.36
keys=[(0.5,hK1*s1),(2.6,0),(4.4,float(hL1)*s1),(5.8,0)]
def prof(xx,keys):
    if xx<=keys[0][0]: return keys[0][1]
    if xx>=keys[-1][0]: return keys[-1][1]
    for (xa,ya),(xb,yb) in zip(keys,keys[1:]):
        if xa<=xx<=xb:
            uu=(xx-xa)/(xb-xa); return yb+(ya-yb)*(1+cos(pi*uu))/2
xs=[-.5+i*.05 for i in range(0,int((6.9+.5)/.05)+1)]
pts=[(x,prof(x,keys)) for x in xs]
o=[zeminpoly(pts,-.3)]
o.append(D((xs[0],-.3),(xs[0],pts[0][1]))+D((xs[0],-.3),(xs[-1],-.3))+D((xs[-1],-.3),(xs[-1],0)))
o.append(blok(.5-.4,hK1*s1,.8,.55,'$2$ kg')); o.append(N(.1,hK1*s1+.8,'K')); o.append(N(4.4,float(hL1)*s1+.3,'L'))
o.append(f'\\fill (4.4,{float(hL1)*s1:.3f}) circle (1.3pt);')
o.append(AR((1.0,hK1*s1+.27),(1.9,hK1*s1+.27),'vurgu,thick')); o.append(N(2.75,hK1*s1+.27,'$v_0=6$ m/s','vurgu,font=\\scriptsize'))
o.append(D((-.5,hK1*s1),(-1.1,hK1*s1),'thin,dashed')); o.append(D((-.5,0),(-1.1,0),'thin,dashed')); o.append(DM((-1.0,0),(-1.0,hK1*s1))); o.append(N(-1.0,hK1*s1/2,'$5$ m','left'))
o.append(D((4.4,float(hL1)*s1),(7.2,float(hL1)*s1),'thin,dashed')); o.append(D((5.8,0),(7.2,0),'thin,dashed')); o.append(DM((7.1,0),(7.1,float(hL1)*s1))); o.append(N(7.1,float(hL1)*s1/2,'$1{,}8$ m','right'))
SK=tikz(o)
q('0001',tipId='en-kor',tip=TIPLER['en-kor'],z='kolay',alt='Mekanik Enerji',kaz='Sürtünmesiz rayda ilk kinetik enerjiyi de katarak iki nokta arasındaki kinetik enerjiyi hesaplar.',kalip='şekilli',
 metin='Şekildeki sürtünmesiz rayın K noktasından 2 kg kütleli bir cisim, rayın doğrultusunda 6 m/s hızla geçmektedir. Cisim ray boyunca hareket ederek L noktasındaki tepeden de geçmektedir. K ve L noktalarının yatay zeminden yükseklikleri şekilde verilmiştir.\n(g = 10 m/s²)\nBuna göre, cismin L noktasından geçerken kinetik enerjisi kaç J’dür?',
 sekil=SK,dogru=100,yan=[(64,'K’deki kinetik enerjiyi (36 J) hesaba katmamış; yalnız yükseklik farkından gelen 64 J’ü almış.','dikkat'),
  (36,'Yükseklik farkını unutup kinetik enerjinin değişmediğini düşünmüş; oysa cisim 3,2 m alçalmıştır.','bilgi'),
  (128,'Yükseklik farkından gelen enerjiyi iki kez katmış: 64 + 64 = 128 J.','islem'),(136,'K’deki potansiyel enerjiyi (2 × 10 × 5 = 100 J) yükseklik farkı yerine kullanıp 36 + 100 = 136 J bulmuş.','islem')],
 istenen='Cismin L noktasındaki kinetik enerjisi (J).',
 ip=['Sürtünme olmadığında hangi enerji toplamı sabit kalır? K’deki iki enerji türünü de düşün.'],
 bilgi=[EK],
 ad=[A('K’deki kinetik enerji','Cisim K’den hızla geçtiği için kinetik enerjisi vardır.','E_k(K) = ½ × 2 × 6² = 36 J'),
     A('Yükseklik farkı','K ile L arasındaki yükseklik farkı kadar potansiyel enerji kinetik enerjiye dönüşür.','Δh = 5 − 1,8 = 3,2 m → m × g × Δh = 2 × 10 × 3,2 = 64 J'),
     A('L’deki kinetik enerji','Mekanik enerji korunur.','E_k(L) = 36 + 64 = 100 J')],
 puf='Mekanik enerjinin korunumunda başlangıç kinetik enerjisi unutulmaz: E_k(son) = E_k(ilk) + m × g × (düşen yükseklik).')
# ===== 02 kolay · F–x
card(2,'Kuvvet–konum grafiğinde iş','Grafiğin altındaki alan işi verir; üçgen ve dikdörtgen alanlar toplanır.','Üçgen alanda ½ çarpanını unutmak; yalnız tek bölgeyi hesaplamak.','kolay','grafik',2,'en-fx','F–x grafiğinde iş')
W2=Fr(20*4,2)+20*6; assert W2==160 and Fr(20*4,2)==40 and 20*4==80 and 20*6==120 and 20*10==200
pl=['\\addplot[thick,vurgu] coordinates {(0,0) (4,20) (10,20)};']
SK=tikz_svg(HEAD+'\n'.join(axis(pl,10,25,'0,1,2,3,4,5,6,7,8,9,10','0,5,10,15,20,25','$x$ (m)','$F$ (N)',w=7.0,h=5.2))+TAIL)
q('0002',tipId='en-fx',tip=TIPLER['en-fx'],z='kolay',alt='İş ve Kinetik Enerji',kaz='Kuvvet–konum grafiğinin altındaki alandan kuvvetin yaptığı işi hesaplar.',kalip='grafik',
 metin='Yatay bir yolda hareket edebilen bir cisme, yol doğrultusunda uygulanan F kuvvetinin cismin konumuna bağlı değişimi şekildeki grafikte verilmiştir.\nBuna göre, F kuvvetinin cisim x = 0 konumundan x = 10 m konumuna gelinceye kadar yaptığı iş kaç J’dür?',
 sekil=SK,dogru=160,yan=[(40,'Yalnız ilk 4 m’deki üçgen bölgenin işini almış; sabit kuvvetli bölgeyi katmamış.','dikkat'),(80,'Üçgenin alanında ½ çarpanını unutmuş (20 × 4 = 80 J), sabit bölgeyi de katmamış.','islem'),
  (120,'Yalnız sabit kuvvetli bölgeyi (20 × 6 = 120 J) hesaplamış; ilk 4 m’yi katmamış.','dikkat'),(200,'En büyük kuvveti bütün yol boyunca uygulanmış saymış: 20 × 10 = 200 J.','bilgi')],
 istenen='F kuvvetinin 0–10 m arasında yaptığı iş (J).',
 ip=['Grafiğin altındaki bölgeyi basit şekillere ayırıp alanlarını ayrı ayrı hesapla.'],
 bilgi=[FX],
 ad=[A('Bölgeleri ayır','Grafik 0–4 m arasında bir üçgen, 4–10 m arasında bir dikdörtgen oluşturur.','Üçgen: taban 4 m, yükseklik 20 N · Dikdörtgen: 6 m × 20 N'),
     A('Alanları hesapla','Her alan o bölgedeki işi verir.','W₁ = ½ × 4 × 20 = 40 J · W₂ = 6 × 20 = 120 J'),
     A('Toplam işi bul','Bölgelerdeki işler toplanır.','W = 40 + 120 = 160 J')],
 puf='F–x grafiğinde iş, eğrinin altındaki alandır; üçgende ½ çarpanını unutma.')
# ===== 03 kolay · yaylar
card(3,'Aynı kuvvetle sıkıştırılan yaylarda enerji','Aynı F kuvvetiyle sıkışan yayda x = F ÷ k ve E = ½·F·x = F² ÷ 2k; enerji k ile ters orantılıdır.','"Aynı kuvvet, aynı enerji" demek; k büyük olan yayda enerjinin de büyük olduğunu sanmak.','kolay','şekilli',3,'en-yay','aynı F, farklı k')
kK,kL=1,2; EK_=Fr(1,2*kK); EL_=Fr(1,2*kL); assert EK_/EL_==2 and Fr(kK,kL)==Fr(1,2) and Fr(kL,kK)**2==4 and Fr(kK,kL)**2==Fr(1,4)
o=[]
for yy,kt,L in ((1.9,'$k$',2.0),(0,'$2k$',3.0)):
    o.append(duvar(0,yy-.4,yy+.5)); o.append(yay((0,yy),(L,yy),8)); o.append(blok(L,yy-.4,.5,.8))
    o.append(AR((L+1.5,yy),(L+.5,yy),'vurgu,very thick')); o.append(N(L+1.0,yy+.35,'$F$','vurgu')); o.append(N(1.0,yy+.62,kt))
    o.append(D((-.3,yy-.4),(5.2,yy-.4),'thick'))
o.append(N(-.35,1.9,'K','left')); o.append(N(-.35,0,'L','left'))
SK=tikz(o)
q('0003',tipId='en-yay',tip=TIPLER['en-yay'],z='kolay',alt='Esneklik Potansiyel Enerjisi',kaz='Aynı kuvvetle sıkıştırılan, esneklik sabitleri farklı yaylarda depolanan enerjileri karşılaştırır.',kalip='şekilli',
 metin='Sürtünmesiz yatay bir zeminde, birer ucu duvara bağlı K ve L yaylarının esneklik sabitleri sırasıyla k ve 2k’dır. Yaylar şekildeki gibi, serbest uçlarına büyüklüğü F olan birer kuvvet uygulanarak sıkıştırılmış ve denge sağlanmıştır. Yaylar esneklik sınırını aşmamıştır.\nBuna göre, K yayında depolanan esneklik potansiyel enerjisinin L yayında depolananına oranı kaçtır?',
 sekil=SK,dogru=2,yan=[(Fr(1,2),'Oranı ters yazmış: enerjinin esneklik sabitiyle doğru orantılı olduğunu düşünmüş.','bilgi'),(1,'Kuvvetler eşit olduğu için enerjilerin de eşit olduğunu sanmış; sıkışma miktarları farklıdır.','dikkat'),
  (Fr(1,4),'Enerjiyi k ile doğru orantılı ve kareli sanmış: (k ÷ 2k)² = 1/4.','islem'),(4,'Sıkışma oranını (2) karesini alarak enerji oranı olarak yazmış; enerji F²/2k olduğundan oran 2’dir.','islem')],
 istenen='E_K ÷ E_L oranı.',
 ip=['Aynı kuvvetle sıkıştırılan iki yayın sıkışma miktarları esneklik sabitleriyle nasıl ilişkilidir?'],
 bilgi=[YE,B('Yay kuvveti','F = k × x. Aynı F için k büyükse sıkışma x küçüktür. Örnek: F = 20 N, k = 100 N/m ise x = 0,2 m')],
 ad=[A('Sıkışmaları yaz','F = k × x olduğundan x = F ÷ k.','x_K = F ÷ k · x_L = F ÷ 2k'),A('Enerjileri yaz','E = ½ × F × x.','E_K = F² ÷ 2k · E_L = F² ÷ 4k'),A('Oranı bul','İki enerji oranlanır.','E_K ÷ E_L = 2')],
 puf='Kuvvet sabitken yay enerjisi E = F² ÷ 2k’dır; esneklik sabiti büyük yaya daha az enerji depolanır.')
# ===== 04 orta · iş–enerji, eğik F, sürtünme (şekilsiz)
card(4,'Eğik kuvvetle çekilen cisimde iş–enerji','Kuvvet yatayla açı yapınca normal kuvvet azalır; sürtünme f = μ·N yeniden bulunur, net iş kinetik enerji değişimine eşittir.','Normal kuvveti m·g almak; F’nin tamamını yatay iş yapan kuvvet saymak.','orta','hikâyeli',5,'en-isteo','eğik F, μ, 4 m')
m4,F4,mu4,x4=5,50,Fr(1,2),4; s37,c37=Fr(3,5),Fr(4,5)
N4=m4*g-F4*s37; f4=mu4*N4; Fx4=F4*c37; net4=Fx4-f4; Ek4=net4*x4
assert (N4,f4,Fx4,net4,Ek4)==(20,10,40,30,120)
assert (Fx4-mu4*m4*g)*x4==60 and Fx4*x4==160 and F4*x4==200 and net4==30
q('0004',tipId='en-isteo',tip=TIPLER['en-isteo'],z='orta',alt='İş–Enerji Teoremi',kaz='Yatayla açı yapan kuvvetle çekilen cismin normal kuvvetini ve sürtünmesini bularak iş–enerji teoremiyle kinetik enerjisini hesaplar.',kalip='hikâyeli',
 metin='Kütlesi 5 kg olan bir sandık, kinetik sürtünme katsayısı 0,5 olan yatay bir zeminde durmaktadır. Sandık, yatayla 37° açı yapacak biçimde yukarı doğru uygulanan 50 N büyüklüğündeki sabit bir kuvvetle çekilerek 4 m ilerletiliyor. Sandık yerden kesilmemektedir.\n(g = 10 m/s², sin 37° = 0,6, cos 37° = 0,8)\nBuna göre, sandığın 4 m sonundaki kinetik enerjisi kaç J’dür?',
 sekil=None,dogru=120,yan=[(30,'Net kuvveti (30 N) yol ile çarpmamış; iş yerine kuvvet değerini kinetik enerji sanmış.','dikkat'),(60,'Normal kuvveti m·g = 50 N almış (f = 25 N); kuvvetin düşey bileşeninin normal kuvveti azalttığını unutmuş.','bilgi'),
  (160,'Sürtünme kuvvetinin yaptığı işi hesaba katmamış: 40 × 4 = 160 J.','dikkat'),(200,'F’nin tamamını yatay almış ve sürtünmeyi atlamış: 50 × 4 = 200 J.','bilgi')],
 istenen='Sandığın 4 m sonundaki kinetik enerjisi (J).',
 ip=['Sandığa etkiyen kuvvetleri yatay ve düşey doğrultuda ayrı ayrı yazıp başla.'],
 bilgi=[IT,B('Kinetik sürtünme','f = μ × N. Cisim yatay zeminde düşey kuvvetlerin dengesinden N bulunur. Örnek: N = 30 N, μ = 0,4 ise f = 12 N')],
 ad=[A('Normal kuvveti bul','Düşey dengede N + F × sin37° = m × g.','N = 50 − 50 × 0,6 = 20 N'),A('Sürtünme kuvvetini bul','f = μ × N.','f = 0,5 × 20 = 10 N'),
     A('Yatay bileşeni bul','İş yapan bileşen F × cos37°.','F_x = 50 × 0,8 = 40 N'),A('Net işi yaz','İş–enerji teoremi: W_net = ΔE_k; cisim durgun başlamıştır.','E_k = (40 − 10) × 4 = 120 J')],
 puf='Eğik kuvvet uygulandığında normal kuvvet değişir; önce N, sonra f, en sonda iş–enerji teoremi.')
# ===== 05 zor · F–x + sürtünme
card(5,'F–x grafiği ve sürtünmeli yolda hız','Grafikteki alan F’nin işidir; sürtünmenin işi f·x çıkarılır, kalan kinetik enerjiden hız bulunur.','Sürtünmeyi hesaba katmamak; üçgen bölgeyi atlamak; ½mv² yerine mv ya da mv² kullanmak.','zor','grafik',5,'en-fx','F–x, sürtünme, v')
m5,F05,a5,b5,f5=4,12,4,8,5
W5=F05*a5+Fr(F05*(b5-a5),2); Ek5=W5-f5*b5; v5=sqrt(2*Ek5/m5)
assert (W5,Ek5,v5)==(72,32,4.0) and sqrt(2*W5/m5)==6 and sqrt(2*(F05*a5-f5*b5)/m5)==2 and Ek5/m5==8 and 2*Ek5/m5==16
assert all(F05*a5-f5*x>0 for x in range(1,5)) and Ek5>0
pl=['\\addplot[thick,vurgu] coordinates {(0,12) (4,12) (8,0)};']
SK=tikz_svg(HEAD+'\n'.join(axis(pl,10,15,'0,1,2,3,4,5,6,7,8,9,10','0,3,6,9,12,15','$x$ (m)','$F$ (N)',w=7.0,h=5.2))+TAIL)
q('0005',tipId='en-fx',tip=TIPLER['en-fx'],z='zor',alt='İş ve Kinetik Enerji',kaz='Kuvvet–konum grafiğinden işi, sürtünme işini ve kinetik enerjiyi birleştirerek cismin hızını hesaplar.',kalip='grafik',
 metin='Kütlesi 4 kg olan bir cisim, sürtünme kuvvetinin büyüklüğü 5 N olan yatay bir yolun başlangıcında (x = 0) durgun hâlde iken, yol doğrultusunda uygulanan F kuvvetiyle harekete geçiriliyor. F kuvvetinin cismin konumuna bağlı değişimi şekildeki grafikte verilmiştir. Cisim hareketi boyunca duraksamamıştır.\nBuna göre, cismin x = 8 m konumundan geçerken hızının büyüklüğü kaç m/s’dir?',
 sekil=SK,dogru=4,yan=[(2,'Grafikteki üçgen bölgeyi hesaba katmamış: (48 − 40) = 8 J → v = 2 m/s.','dikkat'),(6,'Sürtünmeyi yok saymış: 72 J → v = 6 m/s.','dikkat'),(8,'Kinetik enerjiyi (32 J) kütleye bölüp hız saymış (½ ve karekök işlemlerini atlamış).','bilgi'),(16,'½·m·v² yerine ½·m·v yazmış (kareyi unutmuş): ½ × 4 × v = 32 → v = 16 m/s.','islem')],
 istenen='Cismin x = 8 m konumundaki hızının büyüklüğü (m/s).',
 ip=['Hem F’nin hem de sürtünmenin 0–8 m arasında yaptığı işi bulup net işi kinetik enerjiyle ilişkilendir.'],
 bilgi=[FX,IT],
 ad=[A('F’nin işini bul','0–4 m dikdörtgen, 4–8 m üçgen.','W_F = 12 × 4 + ½ × 4 × 12 = 48 + 24 = 72 J'),A('Sürtünmenin işini bul','Sürtünme 8 m boyunca harekete zıt etkir.','W_s = −5 × 8 = −40 J'),
     A('İş–enerji teoremi','Cisim durgun başladığından net iş son kinetik enerjidir.','E_k = 72 − 40 = 32 J'),A('Hızı bul','E_k = ½ × m × v².','32 = ½ × 4 × v² → v = 4 m/s')],
 puf='Grafiğin alanı yalnız F’nin işidir; net iş için sürtünmenin işini çıkarmayı unutma.')
# ===== 06 orta · sürtünmeli LM, ilk hızla giriş
card(6,'Sürtünmeli bölümden geçip rampaya çıkan cisim','Başlangıç kinetik enerjisinin bir kısmı sürtünmeli bölümde ısıya dönüşür; kalan enerji rampada potansiyel enerjiye dönüşür.','Sürtünmeyi unutmak; ½ çarpanını unutmak; ısı enerjisini eklemek.','orta','şekilli',4,'en-surt','LM sürtünmeli, v₀ ile rampaya çıkış')
v6,d6,mu6=5,1,Fr(1,2)
Ek6=Fr(v6**2,2); Q6=mu6*g*d6; h6=(Ek6-Q6)/g
assert Ek6==Fr(25,2) and Q6==5 and h6==Fr(3,4)
assert Ek6/g==Fr(5,4) and (Ek6-2*Q6)/g==Fr(1,4) and (Ek6+Q6)/g==Fr(7,4) and Fr(v6**2,g)==Fr(5,2)
o=[]
pts=[(-.8,0),(0,0),(1.6,0),(2.6,0),(4.1,1.9)]
o.append(zeminpoly([(-.8,0),(2.6,0),(4.1,1.9)],-.3)+D((-.8,-.3),(-.8,0))+D((-.8,-.3),(4.1,-.3))+D((4.1,-.3),(4.1,1.9)))
o.append(rough(1.6,2.6,0)); o.append(blok(-.5,0,.7,.45,'')); o.append(N(-.15,.22,'$m$','font=\\scriptsize')); o.append(AR((.3,.7),(1.3,.7),'vurgu,very thick')); o.append(N(.8,1.0,'$v_0=5$ m/s','vurgu,font=\\scriptsize'))
o.append(N(1.6,-.5,'L')); o.append(N(2.6,-.5,'M')); o.append(DM((1.6,-.85),(2.6,-.85))); o.append(N(2.1,-1.15,'$1$ m')); o.append(N(2.1,.35,'$\\mu=0{,}5$','font=\\scriptsize'))
SK=tikz(o)
q('0006',tipId='en-surt',tip=TIPLER['en-surt'],z='orta',alt='Sürtünmeli Yollar',kaz='Yalnız bir bölümü sürtünmeli olan yolda ilk kinetik enerjinin ısıya ve potansiyel enerjiye dönüşümünden cismin çıkabileceği yüksekliği hesaplar.',kalip='şekilli',
 metin='Şekildeki yolun yalnız LM yatay bölümü sürtünmelidir; yolun geri kalanı sürtünmesizdir ve sağdaki eğimli kısım yeterince yüksektir. Yolun sol ucundaki m kütleli cisim, 5 m/s hızla L noktasına doğru atılıyor ve LM bölümünden geçerek eğimli kısma çıkıyor. LM bölümünün uzunluğu 1 m, kinetik sürtünme katsayısı 0,5’tir.\n(g = 10 m/s²)\nBuna göre, cismin eğimli kısımda zeminden çıkabileceği en büyük yükseklik kaç m’dir?',
 sekil=SK,dogru=Fr(3,4),yan=[(Fr(1,4),'Sürtünmeden ısıya dönüşen enerjiyi iki kez çıkarmış: (12,5 − 10) ÷ 10 = 0,25 m.','islem'),(Fr(5,4),'Sürtünmeyi yok saymış: 12,5 ÷ 10 = 1,25 m.','dikkat'),(Fr(7,4),'Isıya dönüşen enerjiyi çıkarmak yerine eklemiş: (12,5 + 5) ÷ 10 = 1,75 m.','islem'),(Fr(5,2),'Kinetik enerjide ½ çarpanını unutmuş (v₀² ÷ g = 2,5 m) ve sürtünmeyi de hesaba katmamış.','bilgi')],
 istenen='Cismin eğimli kısımda çıkabileceği en büyük yükseklik (m).',
 ip=['Başlangıçtaki kinetik enerjinin nerelerde harcandığını sırayla düşün.'],
 bilgi=[SU,EK],
 ad=[A('Başlangıç enerjisi','Cisim hızla atıldığı için kinetik enerjisi var (m başına).','E ÷ m = ½ × 5² = 12,5 J/kg'),A('Sürtünmedeki kayıp','LM’den geçerken f × d kadar enerji ısıya dönüşür (m başına).','μ × g × d = 0,5 × 10 × 1 = 5 J/kg'),A('Kalan enerji','Rampanın dibine ulaşan enerji.','12,5 − 5 = 7,5 J/kg'),A('Yüksekliği bul','Kalan enerjinin tamamı potansiyel enerjiye dönüşür.','g × h = 7,5 → h = 0,75 m')],
 puf='Sürtünmeli bölümde kaybedilen enerjiyi ilk enerjiden çıkar; kalan enerji yükseklik verir.')
# ===== 07 orta öncüllü · yay m ve 2m
card(7,'Eşit sıkışmış yaylardan fırlayan farklı kütleler','Aynı sıkışmada depolanan enerji eşittir; enerji kinetik enerjiye dönüşür: büyük kütle daha yavaş, momentumu ise daha büyüktür.','Enerji eşit olunca hız ve momentumun da eşit olduğunu sanmak.','orta','şekilli',4,'en-yayhar','özdeş yaylar, m ve 2m')
mm=Fr(1,1); E7=Fr(1)
vP=sqrt(2*E7/ mm) if False else None
# P: m, R: 2m; aynı E: v ∝ 1/√m ; p = √(2mE)
import math as _m
vP=_m.sqrt(2*1/1); vR=_m.sqrt(2*1/2); pP=_m.sqrt(2*1*1); pR=_m.sqrt(2*2*1)
assert vP>vR and abs(vP/vR-_m.sqrt(2))<1e-9 and pR>pP and abs(pR/pP-_m.sqrt(2))<1e-9
o=[]
for yy,lab,mt,xb in ((1.9,'P','$m$',1.9),(0,'R','$2m$',1.9)):
    o.append(duvar(0,yy-.4,yy+.5)); o.append(yay((0,yy),(1.9,yy),8)); o.append(blok(1.9,yy-.4,.5 if mt=='$m$' else .8,.8,mt)); o.append(D((-.3,yy-.4),(5.4,yy-.4),'thick')); o.append(N(-.35,yy,lab,'left'))
    o.append(D((3.4,yy-.55),(3.4,yy+.55),'thin,dashed'))
o.append(DM((1.9+.0,2.95),(3.4,2.95))) if False else None
o=[x for x in o if x]
o.append(N(2.65,2.75,'$x$'))
o.append(DM((1.9,2.55),(3.4,2.55)))
o.append(N(2.65,-.85,'$x$')); o.append(DM((1.9,-.55),(3.4,-.55)))
SK=tikz(o)
q('0007',tipId='en-yayhar',tip=TIPLER['en-yayhar'],z='orta',alt='Yay Potansiyel Enerjisi',kaz='Aynı miktar sıkıştırılmış özdeş yaylardan fırlayan farklı kütleli cisimlerin enerji, hız ve momentumunu karşılaştırır.',kalip='şekilli',
 metin='Sürtünmesiz yatay bir zeminde, özdeş P ve R yaylarının birer ucu duvara bağlıdır. Yayların serbest uçlarına kütleleri sırasıyla m ve 2m olan cisimler şekildeki gibi aynı x miktarı sıkıştırılarak tutulmakta, cisimler yaylara bağlı değildir. Cisimler aynı anda serbest bırakılıyor ve yaylardan ayrılıyorlar.\nCisimler yaylardan ayrıldıkları anda,\nI. kinetik enerjileri eşittir,\nII. P’nin yanındaki cismin hızı diğerinin hızından büyüktür,\nIII. momentumlarının büyüklükleri eşittir\nyargılarından hangileri doğrudur?',
 sekil=SK,istenen='Doğru olan yargılar.',
 ip=['Yayda depolanan enerji ile ayrılma anındaki kinetik enerji arasındaki ilişkiyi, ardından kinetik enerjiyle hız ve momentum ilişkisini düşün.'],
 bilgi=[YE,B('Hız ve momentum','E_k = ½ × m × v² ve p = m × v. Aynı kinetik enerjide kütle büyüdükçe hız azalır, momentum artar. Örnek: E_k = 8 J için 1 kg’ın hızı 4 m/s, 4 kg’ın hızı 2 m/s’dir')],
 ad=[A('I. yargı','Yaylar özdeş ve sıkışma aynı olduğundan depolanan enerji eşittir; sürtünme yok.','E_P = E_R → I doğru'),A('II. yargı','Aynı kinetik enerjide kütlesi küçük olanın hızı büyüktür.','v = √(2E ÷ m) → v_P > v_R → II doğru'),
     A('III. yargı','Momentum p = √(2 × m × E); kütlesi büyük olanda daha büyüktür.','p_R = √2 × p_P → III yanlış')],
 puf='Eşit kinetik enerjide kütle büyük cismin hızı küçük, momentumu büyüktür.',
 **onc([True,True,False],['yaylar özdeş ve sıkışmalar eşit olduğundan depolanan enerji ve dolayısıyla kinetik enerji eşittir','kinetik enerji eşitken kütlesi küçük olanın hızı büyüktür (v = √(2E ÷ m))','p = √(2 × m × E) olduğundan kütlesi büyük olanın momentumu daha büyüktür; momentumlar eşit değildir'],3))
# ===== 08 orta · eğik düzlemde yay
card(8,'Eğik düzlemde dengedeki yaylı cisim','Denge: k·x = m·g·sinθ; yay enerjisi ½·F·x ya da F² ÷ 2k.','Ağırlığın tamamını (m·g) yay kuvveti almak; cosθ kullanmak; ½ çarpanını unutmak.','orta','şekilli',4,'en-yay','eğik düzlem, yay, denge')
m8,k8=5,200; Fy8=m8*g*s37; x8=Fy8/k8; E8=Fr(1,2)*Fy8*x8
assert Fy8==30 and x8==Fr(3,20) and E8==Fr(9,4) and E8==Fr(1,2)*k8*x8**2
assert Fr(1,2)*(m8*g*c37)**2/k8==4 and Fr(1,2)*(m8*g)**2/k8==Fr(25,4) and (Fy8*x8)==Fr(9,2) and Fr(1,2)*Fr(1,2)*Fy8*x8==Fr(9,8)
th=radians(37); u=(cos(th),sin(th)); nn=(-sin(th),cos(th)); Lr=5.0
Ar=(Lr*cos(th),Lr*sin(th)) ; 
def sp(s,t=0): return (s*u[0]+t*nn[0],s*u[1]+t*nn[1])
# eğik düzlem: tabandan (0,0) ile tepe (4.2,3.15); yay üstte duvara (üst uca) bağlı, cisim aşağıda
topS=4.9; blS=2.35; bw=.9; bh=.62
o=[]
o.append(f'\\fill[gray!15] (0,0) -- ({topS*u[0]:.3f},{topS*u[1]:.3f}) -- ({topS*u[0]:.3f},-.25) -- (0,-.25) -- cycle;')
o.append(D((0,0),sp(topS))+D((0,0),(topS*u[0]+.2,0)))
o.append(D((0,-.25),(topS*u[0]+.2,-.25),'thin') if False else '')
# üst duvar (eğik düzleme dik çubuk)
o.append(D(sp(topS),sp(topS,.9),'ultra thick'))
yp1=sp(topS,.0); 
o.append(yay(sp(blS+bw,bh/2),sp(topS,bh/2),9,2.0))
c=[sp(blS,0),sp(blS+bw,0),sp(blS+bw,bh),sp(blS,bh)]
o.append('\\draw[thick,fill=gray!25] '+' -- '.join(f'({x:.3f},{y:.3f})' for x,y in c)+' -- cycle;')
cx,cy=sp(blS+bw/2,bh/2); o.append(f'\\node[rotate=37,font=\\scriptsize] at ({cx:.3f},{cy:.3f}) {{$5$ kg}};')
o.append(f'\\draw (1.0,0) arc[start angle=0,end angle=37,radius=1.0]; \\node at (1.38,.28) {{$37^\\circ$}};')
mx,my=sp(2.9+blS/2+1.1,1.05); o.append(f'\\node[rotate=37,font=\\scriptsize] at ({sp(3.45,1.15)[0]:.3f},{sp(3.45,1.15)[1]:.3f}) {{$k=200$ N/m}};')
SK=tikz([x for x in o if x])
q('0008',tipId='en-yay',tip=TIPLER['en-yay'],z='orta',alt='Esneklik Potansiyel Enerjisi',kaz='Eğik düzlemde dengedeki yaylı cismin yaydaki uzamasını denge koşulundan bulup yayda depolanan enerjiyi hesaplar.',kalip='şekilli',
 metin='Şekildeki 37° eğimli sürtünmesiz eğik düzlemde, esneklik sabiti 200 N/m olan hafif bir yayın ucuna bağlı 5 kg kütleli cisim dengededir. Yayın diğer ucu eğik düzlemin üst ucundaki sabit çubuğa bağlıdır ve yay eğik düzleme paraleldir.\n(g = 10 m/s², sin 37° = 0,6, cos 37° = 0,8)\nBuna göre, yayda depolanan esneklik potansiyel enerjisi kaç J’dür?',
 sekil=SK,dogru=Fr(9,4),yan=[(Fr(9,8),'Yay enerjisinde ½ çarpanını iki kez uygulamış: ½ × ½ × F × x.','islem'),(4,'Yay kuvveti olarak ağırlığın eğik düzleme dik bileşenini (m·g·cos37° = 40 N) almış.','bilgi'),
  (Fr(9,2),'½ çarpanını unutup E = F × x yazmış (30 × 0,15 = 4,5 J).','islem'),(Fr(25,4),'Yay kuvvetini ağırlığın tamamı (50 N) almış; eğik düzlemde yalnız paralel bileşen yayı gerer.','dikkat')],
 istenen='Yayda depolanan esneklik potansiyel enerjisi (J).',
 ip=['Cismi dengede tutan yay kuvveti, ağırlığın hangi bileşenine eşittir?'],
 bilgi=[YE,B('Eğik düzlemde ağırlık','ağırlığın düzleme paralel bileşeni m × g × sinθ, dik bileşeni m × g × cosθ’dır. Örnek: 2 kg, θ = 30° için paralel bileşen 10 N’dur')],
 ad=[A('Yay kuvvetini bul','Sürtünme yok; denge için yay kuvveti ağırlığın paralel bileşenine eşit.','F = m × g × sin37° = 5 × 10 × 0,6 = 30 N'),A('Uzamayı bul','F = k × x.','x = 30 ÷ 200 = 0,15 m'),A('Enerjiyi yaz','E = ½ × F × x.','E = ½ × 30 × 0,15 = 2,25 J')],
 puf='Eğik düzlemde dengede yay kuvveti m·g·sinθ’dır; enerji ½·F·x ile bulunur.')
# ===== 09 orta · yay + rampa
card(9,'Yayın fırlattığı cismin çıkabileceği yükseklik','Yayda depolanan enerji önce kinetik, sonra potansiyel enerjiye dönüşür; sürtünmesizse m·g·h = ½·k·x².','Sıkışma miktarını yükseklik sanmak; ½ çarpanını unutmak.','orta','şekilli',4,'en-yayhar','yay → rampa')
k9,x9,m9=200,Fr(1,5),Fr(1,2); E9=Fr(1,2)*k9*x9**2; h9=E9/(m9*g); v9=sqrt(2*E9/m9)
assert E9==4 and h9==Fr(4,5) and v9==4 and Fr(1,2)*h9==Fr(2,5) and 2*h9==Fr(8,5) and E9==4 and x9==Fr(1,5)
o=[]
o.append(duvar(0,0,1.0)); o.append(yay((0,.42),(1.4,.42),7)); o.append(blok(1.4,0,.6,.5,'$0{,}5$ kg') if False else blok(1.4,0,.6,.5)); o.append(N(1.7,.25,'$m$','font=\\scriptsize'))
o.append(zeminpoly([(-.3,0),(4.6,0),(6.6,1.8)],-.25)+D((-.3,-.25),(-.3,0))+D((6.6,-.25),(6.6,1.8)))
o.append(D((2.0,.65),(2.0,1.1),'thin,dashed')+D((1.0,.65),(1.0,1.1),'thin,dashed')+DM((1.0,.95),(2.0,.95))) if False else None
o=[x for x in o if x]
o.append(N(2.0,1.35,'yay $0{,}2$ m sıkışmış','font=\\scriptsize')); o.append(N(1.2,-.45,'$k=200$ N/m','font=\\scriptsize'))
SK=tikz(o)
q('0009',tipId='en-yayhar',tip=TIPLER['en-yayhar'],z='orta',alt='Yay Potansiyel Enerjisi',kaz='Yayda depolanan enerjinin kinetik ve potansiyel enerjiye dönüşümünden cismin çıkabileceği yüksekliği hesaplar.',kalip='şekilli',
 metin='Şekildeki düzenekte esneklik sabiti 200 N/m olan hafif bir yay, birer ucu duvara bağlı iken 0,2 m sıkıştırılmış ve ucuna temas eden 0,5 kg kütleli cisimle birlikte tutulmaktadır. Yay serbest bırakıldığında cisim yayın doğal boyuna gelince yaydan ayrılıyor, sürtünmesiz yatay zemini kat ettikten sonra yeterince uzun, sürtünmesiz eğik düzleme çıkıyor.\n(g = 10 m/s²)\nBuna göre, cismin eğik düzlemde zeminden çıkabileceği en büyük yükseklik kaç m’dir?',
 sekil=SK,dogru=Fr(4,5),yan=[(Fr(1,5),'Yayın sıkışma miktarını (0,2 m) cismin çıkacağı yükseklik sanmış.','dikkat'),(Fr(2,5),'Yay enerjisinde ½ çarpanını iki kez kullanmış: E = 2 J → h = 0,4 m.','islem'),(Fr(8,5),'Yay enerjisini k × x² = 8 J (½ çarpanını unutarak) bulmuş: h = 8 ÷ 5 = 1,6 m.','islem'),(4,'Yay enerjisini (4 J) doğrudan yükseklik olarak yazmış; potansiyel enerjiyi m·g’ye bölmemiş.','bilgi')],
 istenen='Cismin ulaşabileceği en büyük yükseklik (m).',
 ip=['Yaydan ayrıldığı anda ve en yüksek noktada cismin hangi enerjilere sahip olduğunu karşılaştır.'],
 bilgi=[YE,EK],
 ad=[A('Yay enerjisi','Sıkışmış yayda depolanan enerji.','E = ½ × 200 × 0,2² = 4 J'),A('Enerjinin dönüşümü','Sürtünme yok; yay enerjisi önce kinetik, en yüksek noktada tamamen potansiyel enerji olur.','m × g × h = 4'),A('Yüksekliği bul','m = 0,5 kg.','h = 4 ÷ (0,5 × 10) = 0,8 m')],
 puf='Sürtünmesiz sistemde yay enerjisi doğrudan m·g·h’a eşitlenebilir.')
# ===== 10 zor öncüllü · seri/paralel yaylar
card(10,'Seri ve paralel yaylarda toplam enerji','Seri ve paralel bağlı yaylarda her yayın taşıdığı kuvvet belirlenir; uzama ve enerji ½·F·x ile karşılaştırılır.','Aynı yük asılı diye iki sistemde de enerjinin eşit olduğunu sanmak; paralel yayda uzamayı seri ile aynı almak.','zor','şekilli',6,'en-yay','seri–paralel yay')
xs_=Fr(1); xp_=Fr(1,2)
Es_=2*Fr(1,2)*xs_**2; Ep_=2*Fr(1,2)*xp_**2   # k=mg=1 birimlerinde
assert Es_/Ep_==4 and xs_/xp_==2 and Fr(1,2)*xs_**2/(Fr(1,2)*xp_**2)==4
o=[]
o.append(D((-.4,4.1),(7.0,4.1))+ticks((-.25,4.1),(7.0,4.1),33,.14,.14))
# sistem 1: seri, x=1.0
o.append(yay((1.0,4.1),(1.0,2.8),7)); o.append(yay((1.0,2.8),(1.0,1.5),7)); o.append(blok(.7,.8,.6,.7,'$m$')); o.append(N(1.0,4.6,'Sistem 1'))
o.append(N(1.55,3.45,'$k$')); o.append(N(1.55,2.15,'$k$'))
# sistem 2: paralel
o.append(yay((4.6,4.1),(4.6,2.6),7)); o.append(yay((5.8,4.1),(5.8,2.6),7)); o.append(D((4.35,2.6),(6.05,2.6),'very thick')); o.append(D((5.2,2.6),(5.2,1.5)))
o.append(blok(4.9,.8,.6,.7,'$m$')); o.append(N(5.2,4.6,'Sistem 2')); o.append(N(4.15,3.35,'$k$')); o.append(N(6.3,3.35,'$k$'))
SK=tikz(o)
q('0010',tipId='en-yay',tip=TIPLER['en-yay'],z='zor',alt='Yay Potansiyel Enerjisi',kaz='Seri ve paralel bağlı özdeş yaylarda aynı yük altındaki uzamaları ve depolanan toplam enerjiyi karşılaştırır.',kalip='şekilli',
 metin='Sistem 1’de özdeş ve hafif iki yay seri, Sistem 2’de aynı iki yay paralel bağlanarak şekildeki gibi tavana asılmıştır. Yayları ve Sistem 2’deki yatay çubuğu hafif kabul ediniz; her iki sistemde de yaylara kütlesi m olan birer cisim bağlanmış ve cisimler dengededir. Yaylar esneklik sınırını aşmamıştır.\nBuna göre,\nI. iki sistemde yaylarda depolanan toplam esneklik potansiyel enerjileri eşittir,\nII. Sistem 1’deki yaylarda depolanan toplam enerji, Sistem 2’dekinin 4 katıdır,\nIII. Sistem 1’deki bir yayın uzaması, Sistem 2’deki bir yayın uzamasının 4 katıdır\nyargılarından hangileri doğrudur?',
 sekil=SK,istenen='Doğru olan yargılar.',
 ip=['Her sistemde bir yayın taşıdığı kuvveti ve buna bağlı uzamayı ayrı ayrı bul; enerjiyi ½ × F × x ile hesapla.'],
 bilgi=[YE,B('Seri ve paralel yaylar','seri bağlı yaylarda her yaya aynı kuvvet (tüm yük) etki eder; paralel bağlı özdeş yaylarda yük eşit paylaşılır. Örnek: 40 N’luk yük paralel iki özdeş yayda 20 N’a bölünür')],
 ad=[A('Sistem 1’de bir yay','Seride her yay yükün tamamını taşır: F = m × g, x₁ = m × g ÷ k.','E₁ (iki yay) = 2 × (m × g)² ÷ 2k = (m × g)² ÷ k'),
     A('Sistem 2’de bir yay','Paralelde yük ikiye bölünür: F = m × g ÷ 2, x₂ = m × g ÷ 2k.','E₂ (iki yay) = 2 × (m × g ÷ 2)² ÷ 2k = (m × g)² ÷ 4k'),
     A('I. yargı','E₁ = 4 × E₂ olduğundan enerjiler eşit değildir.','I yanlış'),A('II. yargı','Oran 4’tür.','E₁ ÷ E₂ = 4 → II doğru'),A('III. yargı','Uzamalar oranı: x₁ ÷ x₂ = 2.','III yanlış (4 değil, 2)')],
 puf='Aynı yük altında seri bağlı yaylarda enerji paralelin 4 katıdır; ancak uzama oranı 2’dir, enerji ise uzamanın karesiyle orantılıdır.',
 **onc([False,True,False],['seri bağlı yaylarda enerji paralel bağlıdakinin 4 katı olduğundan enerjiler eşit değildir','toplam enerji oranı E₁ ÷ E₂ = 4’tür','tek yaydaki uzama oranı 4 değil 2’dir; 4 katı olan toplam enerjidir'],0))
# ===== 11 orta · Atwood, enerji
card(11,'Makaralı iki cisimli sistemde enerji','Sürtünmesiz sistemde potansiyel enerji azalması iki cismin toplam kinetik enerjisine eşittir; hızlar eşit büyüklüktedir.','Yalnız ağır cismin potansiyel enerjisini kullanmak; hafif cismin yükseldiğini unutmak; tüm kinetik enerjiyi tek cisme yazmak.','orta','şekilli',5,'en-sistem','Atwood, enerji korunumu')
m1_,m2_,h11=5,3,Fr(4,5)
dE=(m1_-m2_)*g*h11; v11=sqrt(2*dE/(m1_+m2_)); Ek1=Fr(1,2)*m1_*Fr(int(v11))**2
assert dE==16 and v11==2 and Ek1==10
assert Fr(1,2)*m2_*4==6 and m1_*g*h11==40 and m2_*g*h11==24 and dE==16
sc=1.6; hs=float(h11)*sc
o=[]
o.append(D((.6,3.9),(3.0,3.9))+ticks((.75,3.9),(3.0,3.9),11,.14,.14))
o.append(D((1.8,3.9),(1.8,3.6),'thick')); o.append('\\draw[thick,fill=white] (1.8,3.3) circle (.3);'); o.append('\\fill (1.8,3.3) circle (1.3pt);')
o.append(D((1.5,3.3),(1.5,hs+.6),'thick')); o.append(D((2.1,3.3),(2.1,.6),'thick'))
o.append(blok(1.1,hs,.8,.6,'$5$ kg')); o.append(blok(1.7,0,.8,.6,'$3$ kg'))
o.append(zemin(.4,3.2,0))
o.append(D((.6,hs),(1.1,hs),'thin,dashed')); o.append(DM((.7,0),(.7,hs))); o.append(N(.65,hs/2,'$0{,}8$ m','left'))
SK=tikz(o)
q('0011',tipId='en-sistem',tip=TIPLER['en-sistem'],z='orta',alt='Mekanik Enerji',kaz='Makaralı iki cisimli sistemde enerji korunumuyla cisimlerden birinin kinetik enerjisini hesaplar.',kalip='şekilli',
 metin='Şekildeki düzenekte kütleleri 5 kg ve 3 kg olan cisimler, hafif ve esnemez bir iple, sürtünmesiz ve hafif bir makaradan geçirilerek bağlanmıştır. 3 kg’lık cisim yere değmektedir; 5 kg’lık cisim ise yerden 0,8 m yüksekliktedir ve sistem durgun hâlden serbest bırakılıyor.\n(g = 10 m/s²)\nBuna göre, 5 kg’lık cisim yere çarpmadan hemen önce sahip olduğu kinetik enerji kaç J’dür?',
 sekil=SK,dogru=10,yan=[(6,'3 kg’lık cismin kinetik enerjisini hesaplamış; soruda 5 kg’lık cisim isteniyor.','dikkat'),(16,'Sistemin toplam kinetik enerjisini (iki cismin toplamı) tek cismin enerjisi saymış.','dikkat'),(24,'Yalnız hafif cismin kazandığı potansiyel enerjiyi (3 × 10 × 0,8) kinetik enerji sanmış.','bilgi'),(40,'5 kg’lık cismin kaybettiği potansiyel enerjiyi (5 × 10 × 0,8) kinetik enerjisi saymış; 3 kg’lık cismin enerji kazancını düşmemiş.','bilgi')],
 istenen='5 kg’lık cismin yere çarpmadan önceki kinetik enerjisi (J).',
 ip=['Potansiyel enerji azalması yalnız 5 kg’lık cismin kinetik enerjisine mi gider, yoksa başka bir cisim de enerji kazanır mı?'],
 bilgi=[EK,B('İple bağlı cisimler','esnemez ip ile bağlı cisimlerin hız büyüklükleri eşittir ve aynı yol alırlar; kinetik enerjileri kütleleriyle orantılıdır. Örnek: 2 kg ve 4 kg’lık cisimlerde enerji oranı 1 : 2’dir')],
 ad=[A('Potansiyel enerji değişimi','5 kg 0,8 m iner, 3 kg 0,8 m yükselir.','ΔE_p = 5 × 10 × 0,8 − 3 × 10 × 0,8 = 40 − 24 = 16 J'),A('Toplam kinetik enerji','Enerji korunur; bu enerji iki cismin kinetik enerjisidir.','½ × (5 + 3) × v² = 16 → v = 2 m/s'),A('5 kg’lık cismin enerjisi','Hız her iki cisim için 2 m/s’dir.','E_k = ½ × 5 × 2² = 10 J')],
 puf='Makaralı sistemlerde enerji kazancını iki cisim kütleleri oranında paylaşır; önce ortak hızı bul.')
# ===== 12 orta öncüllü · sabit hız, iş (şekilsiz)
card(12,'Sabit hızla çekilen cisimde iş ve enerji','Her kuvvetin işinin işareti ve toplam iş, hızın değişip değişmediğiyle birlikte değerlendirilir.','Hız değişimi ile işin işaretini karıştırmak.','kolay','öncüllü',3,'en-isteo','sabit hızlı çekme, iş işaretleri')
q('0012',tipId='en-isteo',tip=TIPLER['en-isteo'],z='kolay',alt='İş–Enerji Teoremi',kaz='Sabit hızla hareket eden cisimde kuvvetlerin yaptığı işlerin işaretlerini ve net işi yorumlar.',kalip='öncüllü',
 metin='Bir işçi, kinetik sürtünme katsayısı sabit olan yatay bir yolda duran bir sandığı yola paralel F kuvvetiyle çekmeye başlıyor. Sandık kısa sürede sabit hıza ulaşıyor ve işçi sandığı bu hızla belirli bir yol boyunca çekmeye devam ediyor.\nSandık sabit hızla hareket ederken bu yol boyunca,\nI. sandığın kinetik enerjisi artar,\nII. F kuvvetinin yaptığı iş pozitiftir,\nIII. sandığa etkiyen kuvvetlerin yaptığı işlerin toplamı sıfırdır\nyargılarından hangileri doğrudur?',
 sekil=None,istenen='Doğru olan yargılar.',
 ip=['Her kuvvetin işinin işaretini ayrı ayrı düşün.'],
 bilgi=[IT,B('İşin işareti','kuvvet yer değiştirmeyle aynı yönde ise iş pozitif, zıt yönde ise negatiftir; dik kuvvetler iş yapmaz. Örnek: sürtünme kuvveti hareketi geri çektiğinden negatif iş yapar')],
 ad=[A('I. yargı','Hız sabit olduğundan kinetik enerji değişmez.','ΔE_k = 0 → I yanlış'),A('II. yargı','F yer değiştirmeyle aynı yönlüdür.','W_F > 0 → II doğru'),A('III. yargı','Net kuvvet sıfır olduğundan net iş sıfırdır; iş–enerji teoremi ΔE_k = 0 verir.','W_F + W_s = 0 → III doğru')],
 puf='Sabit hızda ΔE_k = 0 olduğundan toplam iş sıfırdır; çeken kuvvetin işi sürtünmenin işini dengeler.',
 **onc([False,True,True],['sabit hızda kinetik enerji değişmez','F kuvveti yer değiştirmeyle aynı yönde olduğundan pozitif iş yapar','net kuvvet sıfır olduğundan işlerin toplamı da sıfırdır'],3))
# ===== 13 orta · çeyrek çember + sürtünmeli yatay
card(13,'Çeyrek çember rayda inip sürtünmeli yolda duran cisim','İnişte kaybedilen potansiyel enerji, sürtünmeli yolda ısıya dönüşen f·d enerjisine eşitlenir.','R yerine çapı almak; ½mv² = mgR yerine v² = gR kullanmak.','orta','şekilli',4,'en-surt','çeyrek çember + sürtünmeli yatay')
R13,mu13=Fr(6,5),Fr(2,5); d13=R13/mu13
assert d13==3 and mu13*R13==Fr(12,25) and R13/(2*mu13)==Fr(3,2) and 2*R13==Fr(12,5)
Rs=1.5*float(R13)
o=[]
cx,cy=Rs,Rs
o.append(ticks((.15,0),(Rs+4.2,0),int((Rs+4.2)/.22)))
o.append(f'\\draw[thick] (0,{Rs:.3f}) arc[start angle=180,end angle=270,radius={Rs:.3f}] -- ({Rs+4.2:.3f},0);')
o.append(D((0,Rs),(0,Rs+.5),'thick')) if False else None
o.append(D((0,-.25),(Rs+4.2,-.25),'thin')) if False else None
o.append(blok(0,Rs,.55,.45,'')); o.append(N(.28,Rs+.75,'K')); o.append(N(.28,Rs+.22,'$m$','font=\\scriptsize'))
o.append(f'\\draw[thin,dashed] ({Rs:.3f},{Rs:.3f}) -- (0,{Rs:.3f}); \\draw[thin,->] ({Rs:.3f},{Rs:.3f}) -- ({Rs-Rs*cos(pi/4):.3f},{Rs-Rs*sin(pi/4):.3f}); \\node at ({Rs*.62+.35:.3f},{Rs*.62-.2:.3f}) {{$R$}};')
o.append(rough(Rs,Rs+4.2,0)); o.append(N(Rs,-.45,'L')); o.append(N(Rs+2.1,.4,'$\\mu=0{,}4$')); o.append(N(Rs+2.1,-.55,'sürtünmeli yatay yol','font=\\scriptsize'))
o.append(D((0,0),(-.4,0),'thin,dashed')) if False else None
o.append(N(Rs/2+.1,Rs+1.05,'$R=1{,}2$ m','font=\\scriptsize')) if False else None
o=[x for x in o if x]
SK=tikz(o)
q('0013',tipId='en-surt',tip=TIPLER['en-surt'],z='orta',alt='Sürtünmeli Yollar',kaz='Sürtünmesiz çeyrek çember rayda inen cismin sürtünmeli yatay yolda durana kadar aldığı yolu enerji korunumuyla hesaplar.',kalip='şekilli',
 metin='Şekildeki yolun yarıçapı 1,2 m olan çeyrek çember biçimindeki bölümü sürtünmesizdir. Çeyrek çemberin K noktasında durgun olan m kütleli cisim serbest bırakılıyor ve cisim alt noktadaki L noktasından sonra kinetik sürtünme katsayısı 0,4 olan yatay yolda ilerleyerek duruyor.\n(g = 10 m/s²)\nBuna göre, cisim L noktasından itibaren yatay yolda kaç m ilerleyerek durur?',
 sekil=SK,dogru=3,yan=[(Fr(12,25),'Yolu R × μ olarak bulmuş; enerji denkleminde μ’nün paydada olduğunu görememiş.','islem'),(Fr(3,2),'L’deki hız için v² = g × R yazmış (v² = 2 × g × R olmalı); enerji korunumunu eksik uygulamış.','bilgi'),(Fr(6,5),'Cismin L’ye varınca durduğunu sanıp yolu R olarak yazmış.','dikkat'),(Fr(12,5),'Çeyrek çemberin çapını (2R = 2,4 m) yatay yolun uzunluğu sanmış.','dikkat')],
 istenen='Cismin yatay yolda aldığı yol (m).',
 ip=['K ile cismin durduğu nokta arasında kaybolan potansiyel enerjinin tamamı hangi işe dönüşür?'],
 bilgi=[SU,EK],
 ad=[A('Potansiyel enerji','K noktasında cisim durgundur; yükseklik R kadardır.','E_p = m × g × R = m × 10 × 1,2 = 12 m (J)'),A('Sürtünme işi','Durana kadar enerjinin tamamı ısıya dönüşür.','μ × m × g × d = 0,4 × 10 × m × d = 4 m × d'),A('Yolu bul','Enerjiyi eşitle.','4 m × d = 12 m → d = 3 m')],
 puf='Durana kadar kaybedilen mekanik enerji f × yol kadardır; kütle her iki yanda sadeleşir.')
# ===== 14 zor · halka
card(14,'Düşey halkadan geçmek için gerekli yükseklik','Tepe noktasında yoldan ayrılmama koşulu ile enerji korunumu birleştirilerek başlangıç yüksekliği bulunur.','Tepede hızı sıfır almak (h = 2r); v² = 2·g·r kullanmak; r yerine çap kullanmak.','zor','şekilli',5,'en-kor','düşey halka, en küçük yükseklik')
r14=Fr(2,5); h14=2*r14+r14/2
assert h14==1 and 2*r14==Fr(4,5) and 3*r14==Fr(6,5) and 4*r14==Fr(8,5)
assert Fr(9,10)==2*r14+r14/4
sc=2.8; rs=float(r14)*sc; hs=1.55*sc  # çizimde h ölçekli değil, h bilinmeyen
cxr=3.2
o=[]
o.append(ticks((.15,0),(cxr+rs+1.4,0),int((cxr+rs+1.4)/.22)))
o.append(f'\\draw[thick] (0.2,{hs:.3f}) -- ({cxr-rs-0.2:.3f},0.0) -- ({cxr:.3f},0);')
o.append(f'\\draw[thick] ({cxr:.3f},0) arc[start angle=-90,end angle=270,radius={rs:.3f}];')
o.append(f'\\draw[thick] ({cxr:.3f},0) -- ({cxr+rs+1.4:.3f},0);')
o.append(f'\\draw[thin,dashed] (-.4,{hs:.3f}) -- (.9,{hs:.3f}); \\draw[thin,dashed] (-.4,0) -- (0,0); \\draw[thin,<->] (-.3,0) -- (-.3,{hs:.3f}); \\node[left] at (-.3,{hs/2:.3f}) {{$h$}};')
o.append(f'\\fill ({0.2:.3f},{hs:.3f}) circle (3pt);')
o.append(f'\\draw[thin,->] ({cxr:.3f},{rs:.3f}) -- ({cxr+rs*cos(pi/4):.3f},{rs+rs*sin(pi/4):.3f}); \\node at ({cxr+.62:.3f},{rs+.12:.3f}) {{$r$}};')
o.append(N(cxr+rs+.7,-.45,'M') if False else '')
o.append(N(cxr,-.45,'L')); o.append(N(cxr,2*rs+.28,'T'))
o.append(N(.2,hs+.35,'K'))
SK=tikz([x for x in o if x])
q('0014',tipId='en-kor',tip=TIPLER['en-kor'],z='zor',alt='Mekanik Enerji',kaz='Düşey halkada tepe noktasından geçebilmenin koşulunu enerji korunumuyla birleştirip başlangıç yüksekliğini hesaplar.',kalip='şekilli',
 metin='Şekildeki sürtünmesiz yolun L noktasından sonraki bölümü, yarıçapı r = 0,4 m olan düşey bir halkadır. Boyutları önemsiz m kütleli bir cisim, K noktasından serbest bırakılıyor ve halkanın en üst noktası T’yi yoldan ayrılmadan geçiyor.\n(g = 10 m/s²)\nCismin halkayı bu şekilde tamamlayabilmesi için K noktasının yerden yüksekliği (h) en az kaç m olmalıdır?',
 sekil=SK,dogru=1,yan=[(Fr(4,5),'Cismin T noktasında durgun olduğunu (hızının sıfır olduğunu) varsayıp h = 2r = 0,8 m bulmuş.','bilgi'),(Fr(9,10),'T’deki kinetik enerjiyi ½ × m × v² = m × g × r ÷ 4 almış (½ çarpanını fazladan uygulamış).','islem'),(Fr(6,5),'T’deki hızı v² = 2 × g × r almış (merkezcil koşulu hatalı yazmış): h = 3r.','bilgi'),(Fr(8,5),'T’de v² = 4·g·r almış: h = 2r + 2r = 1,6 m.','bilgi')],
 istenen='K noktasının yerden en küçük yüksekliği (m).',
 ip=['T noktasında cismin yoldan ayrılmama koşulunu yaz.'],
 bilgi=[EK,B('Düşey halkada tepe noktası','tepe noktasında cismin halkaya uyguladığı basınç sıfır olduğunda en küçük hız elde edilir: m × g = m × v² ÷ r → v² = g × r. Örnek: r = 0,9 m için v = 3 m/s')],
 ad=[A('En küçük hız','T noktasında yalnız ağırlık merkezcil kuvvet olur.','m × g = m × v² ÷ r → v² = g × r = 10 × 0,4 = 4'),A('T’deki enerji','T noktasının yüksekliği 2r = 0,8 m.','E_k(T) = ½ × m × 4 = 2m · E_p(T) = m × 10 × 0,8 = 8m'),A('Toplam enerji','Enerji korunur: K’deki potansiyel enerji T’deki toplam enerjiye eşittir.','m × 10 × h = 2m + 8m'),A('Yüksekliği bul','Sadeleştir.','h = 1 m')],
 puf='Düşey halkayı tamamlamak için tepede v² = g·r olmalıdır; bu da başlangıç yüksekliğinin en az 2,5·r olması demektir.')
# ===== 15 zor · yaya çarpan cisim, sürtünmeli yol
card(15,'Sürtünmeli yolda yaya çarpan cisim','Yayın en çok sıkıştığı anda kinetik enerji sıfırdır: ½mv₀² = f·(d + x) + ½kx².','Yay sıkışırken sürtünmeyi unutmak; ½ çarpanını unutmak; x yerine d ya da d + x vermek.','zor','şekilli',5,'en-yayhar','sürtünmeli yol + yay')
m15,v15,f15,d15,k15=1,8,4,5,16
x15=Fr(1); assert Fr(m15*v15**2,2)==f15*(d15+x15)+Fr(1,2)*k15*x15**2 and f15*(d15+x15)+Fr(1,2)*k15*x15**2==32
assert Fr(1,2)*k15*Fr(2)**2==32                                    # sürtünmesiz → x=2
assert Fr(m15*v15**2,2)==f15*(d15+Fr(3,4))+k15*Fr(3,4)**2           # ½ unutuldu → x=3/4
assert d15+x15==6
o=[]
o.append(zemin(-.3,8.2,0)); o.append(rough(.6,6.4,0))
o.append(duvar(8.0,0,1.0,sol=False)); o.append(yay((6.4,.45),(8.0,.45),7))
o.append(blok(.2,0,.7,.55,'')); o.append(N(.55,.28,'$m$','font=\\scriptsize')); o.append(AR((.55,.9),(1.8,.9),'vurgu,very thick')); o.append(N(1.2,1.2,'$v_0$','vurgu'))
o.append(DM((.9,-.45),(6.4,-.45))); o.append(N(3.65,-.75,'$d=5$ m')); o.append(N(3.65,.4,'$f=4$ N','font=\\scriptsize')); o.append(N(7.2,1.0,'$k=16$ N/m','font=\\scriptsize'))
SK=tikz(o)
q('0015',tipId='en-yayhar',tip=TIPLER['en-yayhar'],z='zor',alt='Yay Potansiyel Enerjisi',kaz='Sürtünmeli yatay yolda yaya çarpan cismin yayı en çok ne kadar sıkıştıracağını iş–enerji teoremiyle hesaplar.',kalip='şekilli',
 metin='Şekildeki yatay yolun tamamı sürtünmelidir ve cisme etkiyen sürtünme kuvvetinin büyüklüğü her yerde 4 N’dur. Esneklik sabiti 16 N/m olan hafif yay, doğal boyunda iken bir ucundan duvara bağlıdır. 1 kg kütleli cisim yayın serbest ucundan 5 m uzaktan 8 m/s hızla yaya doğru atılıyor, yaya çarpıp onu sıkıştırdıktan sonra bir an durmaktadır. Cisim yaya bağlı değildir.\nBuna göre, yayın en büyük sıkışması kaç m’dir?',
 sekil=SK,dogru=1,yan=[(Fr(3,4),'Yay enerjisini k × x² olarak yazmış (½ çarpanını unutmuş).','islem'),(2,'Sürtünmeyi tamamen yok saymış: ½ × 1 × 8² = ½ × 16 × x² → x = 2 m.','dikkat'),(5,'Yayın sıkışması yerine cismin yaya kadar aldığı yolu (5 m) vermiş.','dikkat'),(6,'Cismin durana kadar aldığı toplam yolu (d + x = 6 m) yayın sıkışması saymış.','dikkat')],
 istenen='Yayın en büyük sıkışması (m).',
 ip=['Cisim yayı sıkıştırırken de sürtünme kuvveti iş yapmaya devam eder. Başlangıç kinetik enerjisi hangi üç kalemde harcanır?'],
 bilgi=[IT,SU,YE],
 ad=[A('Başlangıç enerjisi','Cisim ilk hızıyla kinetik enerjiye sahip.','E_k = ½ × 1 × 8² = 32 J'),A('Enerji denklemi','En büyük sıkışmada kinetik enerji sıfırdır; enerji ısıya ve yaya gider.','32 = 4 × (5 + x) + ½ × 16 × x²'),A('Sadeleştir','Terimleri düzenle.','8x² + 4x − 12 = 0 → 2x² + x − 3 = 0'),A('Kökü seç','Pozitif kök sıkışmadır.','(2x + 3)(x − 1) = 0 → x = 1 m')],
 puf='Yay sıkışırken de sürtünme iş yapar; enerji denklemine f·(d + x) yazılır.')
# ===== 16 zor · eğik düzlem yukarı-aşağı
card(16,'Sürtünmeli eğik düzlemde çıkış ve dönüş','Çıkışta mg·sinθ ve f birlikte yavaşlatır; dönüşte sürtünme harekete zıt olduğundan net kuvvet küçülür. İş–enerji teoremi iki yolda ayrı uygulanır.','Dönüşte sürtünmeyi unutmak; yalnız tek yönde ısı hesaplamak.','zor','şekilli',5,'en-isteo','eğik düzlem, çık-dön')
m16,v16,mu16=2,10,Fr(1,2); f16=mu16*m16*g*c37; Fs16=m16*g*s37
L16=Fr(m16*v16**2,2)/(Fs16+f16); Ekd=(Fs16-f16)*L16
assert f16==8 and Fs16==12 and L16==5 and Ekd==20 and L16*s37==3
assert f16*L16==40 and 2*f16*L16==80 and Fr(m16*v16**2,2)-f16*L16==60 and Fr(m16*v16**2,2)==100
o=[]
Hh=3.0; Bb=4.0
o.append(f'\\fill[gray!15] (0,0) -- ({Bb},0) -- ({Bb},{Hh}) -- cycle;')
o.append(f'\\draw[thick] (0,0) -- ({Bb},0) -- ({Bb},{Hh}) -- cycle;')
# blok alt uçta
bw,bh=.7,.45
c=[(.35*u[0],.35*u[1]),((.35+bw)*u[0],(.35+bw)*u[1])]
def sp2(s,t=0): return (s*u[0]+t*nn[0],s*u[1]+t*nn[1])
cc=[sp2(.35,0),sp2(.35+bw,0),sp2(.35+bw,bh),sp2(.35,bh)]
o.append('\\draw[thick,fill=gray!25] '+' -- '.join(f'({x:.3f},{y:.3f})' for x,y in cc)+' -- cycle;')
cx,cy=sp2(.35+bw/2,bh/2); o.append(f'\\node[rotate=37,font=\\scriptsize] at ({cx:.3f},{cy:.3f}) {{$2$ kg}};')
a0=sp2(.35+bw+.1,bh/2+.25); a1=sp2(.35+bw+1.2,bh/2+.25); o.append(AR(a0,a1,'vurgu,very thick')); t0=sp2(.35+bw+.7,bh/2+.6); o.append(f'\\node[vurgu,rotate=37] at ({t0[0]:.3f},{t0[1]:.3f}) {{$v_0=10$ m/s}};')
o.append(f'\\draw (1.0,0) arc[start angle=0,end angle=37,radius=1.0]; \\node at (1.38,.26) {{$37^\\circ$}};')
o.append(N(2.1,-.4,'$\\mu=0{,}5$ (eğik düzlem)','font=\\scriptsize')); o.append(N(.2,-.3,'L'))
SK=tikz(o)
q('0016',tipId='en-isteo',tip=TIPLER['en-isteo'],z='zor',alt='İş–Enerji Teoremi',kaz='Sürtünmeli eğik düzlemde çıkış ve dönüşü iş–enerji teoremiyle birlikte değerlendirip dönüşteki kinetik enerjiyi hesaplar.',kalip='şekilli',
 metin='Şekildeki 37° eğimli eğik düzlemin sürtünme katsayısı 0,5’tir. Düzlemin alt ucundaki L noktasından, düzleme paralel ve yukarı doğru 10 m/s hızla geçen 2 kg kütleli cisim, düzlem üzerinde bir miktar yükselip durduktan sonra geri dönmekte ve L noktasından tekrar geçmektedir.\n(g = 10 m/s², sin 37° = 0,6, cos 37° = 0,8)\nBuna göre, cismin L noktasından geri dönüşünde geçerken kinetik enerjisi kaç J’dür?',
 sekil=SK,dogru=20,yan=[(40,'Yalnız çıkışta ısıya dönüşen enerjiyi (f × L = 40 J) kinetik enerji sanmış.','dikkat'),(60,'Dönüşte yalnız sürtünmeyi düşünüp çıkıştaki kaybı bir kez katmış: 100 − 40 = 60 J.','islem'),(80,'Gidiş–dönüşte toplam ısıya dönüşen enerjiyi (2 × 40 = 80 J) kinetik enerji sanmış.','bilgi'),(100,'Sürtünmeyi yok sayıp mekanik enerjinin korunduğunu düşünmüş.','bilgi')],
 istenen='Cismin dönüşte L noktasındaki kinetik enerjisi (J).',
 ip=['Çıkışta ve dönüşte sürtünme kuvvetinin yönü nasıl değişir? Toplam yolu ve ısıya dönüşen enerjiyi bul.'],
 bilgi=[IT,SU,B('Eğik düzlemde kuvvetler','paralel bileşen m × g × sinθ, normal kuvvet N = m × g × cosθ’dır. Örnek: 1 kg, θ = 37° için paralel bileşen 6 N, N = 8 N’dur')],
 ad=[A('Sürtünme kuvveti','N = m × g × cos37°, f = μ × N.','f = 0,5 × 2 × 10 × 0,8 = 8 N'),A('Çıkış yolu','Çıkışta durana kadar ağırlığın bileşeni ve f birlikte iş yapar.','½ × 2 × 10² = (12 + 8) × L → L = 5 m'),A('Dönüşteki net kuvvet','Dönüşte f yukarı yönlüdür.','Net = 12 − 8 = 4 N'),A('Kinetik enerji','Dönüşte 5 m yol alır.','E_k = 4 × 5 = 20 J'),A('Kontrol','Toplam ısı 2 × 8 × 5 = 80 J.','100 − 80 = 20 J')],
 puf='Gidiş–dönüşte sürtünmeden toplam f × 2L enerji ısıya dönüşür; dönüş kinetik enerjisi E₀ − 2·f·L’dir.')
# ===== 17 zor öncüllü · sürtünmeli LM rampa
card(17,'Sürtünmeli bölümden tekrar geçen cismin yükseklikleri','Her LM geçişinde sabit enerji ısıya dönüşür; rampadaki yükseklikler kalan enerjiden, durma yeri toplam yoldan bulunur.','Dönüşte enerjinin korunduğunu (LM’de kayıp olmadığını) sanmak; durma noktasını M sanmak.','zor','şekilli',6,'en-surt','LM sürtünmeli, iki rampa')
m17,h17,Q17=1,2,8
E0=m17*g*h17; EM=E0-Q17; hr=Fr(EM,m17*g); EL=EM-Q17; hl=Fr(EL,m17*g); stop=Fr(E0,Q17)
assert (E0,EM,hr,EL,hl,stop)==(20,12,Fr(6,5),4,Fr(2,5),Fr(5,2))
assert stop-2==Fr(1,2)    # 2 tam geçiş sonra ortada durur
hs=h17*.9
o=[]
pts=[(-.8,hs),(0,hs),(.9,0),(2.0,0),(3.1,hs*1.25)]
o.append(zeminpoly(pts,-.3)+D((-.8,-.3),(-.8,hs))+D((-.8,-.3),(3.1,-.3))+D((3.1,-.3),(3.1,hs*1.25)))
o.append(rough(.9,2.0,0)); o.append(blok(-.7,hs,.7,.45,'')); o.append(N(-.35,hs+.22,'$m$','font=\\scriptsize')); o.append(N(-.35,hs+.7,'K'))
o.append(N(.9,-.5,'L')); o.append(N(2.0,-.5,'M')); o.append(N(1.45,.4,'$f=8$ N','font=\\scriptsize'))
o.append(D((-.8,hs),(-1.4,hs),'thin,dashed')); o.append(D((-.8,0),(-1.4,0),'thin,dashed')); o.append(DM((-1.3,0),(-1.3,hs))); o.append(N(-1.3,hs/2,'$2$ m','left'))
o.append(DM((.9,-.85),(2.0,-.85))); o.append(N(1.45,-1.15,'$1$ m'))
SK=tikz(o)
q('0017',tipId='en-surt',tip=TIPLER['en-surt'],z='zor',alt='Sürtünmeli Yollar',kaz='Sürtünmeli bölümden birden fazla geçen cismin rampalarda çıkabildiği yükseklikleri ve durma yerini enerji kaybından değerlendirir.',kalip='şekilli',
 metin='Şekildeki yolun yalnız LM yatay bölümü sürtünmelidir; yolun geri kalanı sürtünmesiz ve her iki yandaki eğimli kısımlar yeterince yüksektir. LM bölümünün uzunluğu 1 m, bu bölümde cisme etkiyen sürtünme kuvvetinin büyüklüğü 8 N’dur. K noktasında durgun olan 1 kg kütleli cisim serbest bırakılıyor ve cisim sonunda yolun bir noktasında duruyor.\n(g = 10 m/s²)\nBuna göre,\nI. cisim M noktasının sağındaki eğimli kısımda en çok 1,2 m yüksekliğe çıkar,\nII. cismin geri dönüp L noktasından ikinci geçişindeki kinetik enerjisi 8 J’dür,\nIII. cisim LM bölümünün ortasında durur\nyargılarından hangileri doğrudur?',
 sekil=SK,istenen='Doğru olan yargılar.',
 ip=['Cismin her LM geçişinde kaç J enerji kaybettiğini bul; sonra sırayla M, L ve bir sonraki geçişteki kalan enerjiyi hesapla.'],
 bilgi=[SU,EK],
 ad=[A('Başlangıç enerjisi','K noktasında cisim durgundur.','E = 1 × 10 × 2 = 20 J'),A('Birinci geçiş','LM’de f × d = 8 × 1 = 8 J ısıya dönüşür.','E_k(M) = 20 − 8 = 12 J → h = 12 ÷ 10 = 1,2 m'),A('İkinci geçiş','Geri dönüşte LM’den bir kez daha geçer.','E_k(L) = 12 − 8 = 4 J'),A('Sol rampa','Kalan 4 J ile yükselir.','h = 4 ÷ 10 = 0,4 m'),A('Durma noktası','Toplam yol = 20 ÷ 8 = 2,5 m; iki tam geçiş sonra L’den 0,5 m.','LM’nin ortasında durur → III doğru, II yanlış')],
 puf='Sürtünmeli bölümden her geçişte aynı enerji kaybolur; toplam enerjiyi bu kayba bölerek geçiş sayısını ve durma noktasını bul.',
 **onc([True,False,True],['M’de 12 J kinetik enerji kalır ve cisim 12 ÷ 10 = 1,2 m yükselir','L’den ikinci geçişte enerji 12 − 8 = 4 J’dür; 8 J değildir','toplam yol 20 ÷ 8 = 2,5 m; iki tam geçişten sonra kalan 0,5 m LM’nin ortasında biter'],4))
# ===== 18 orta · güç ve verim (şekilsiz)
card(18,'Eğik düzlemde sabit hızla çekme: güç ve verim','Sabit hızda çeken kuvvet m·g·sinθ + f; yararlı güç F·v; verimle bölünerek motorun harcadığı güç bulunur.','Sürtünmeyi unutmak; verimi çarpmak yerine bölmek ya da tersini yapmak.','orta','hikâyeli',5,'en-guc','çekme gücü, verim')
m18,v18,ver=50,2,Fr(4,5); Fc=m18*g*s37+Fr(1,4)*m18*g*c37; Pf=Fc*v18; Pin=Pf/ver
assert Fc==400 and Pf==800 and Pin==1000 and Pf*ver==640 and (m18*g*s37)*v18/ver==750 and (m18*g*s37)*v18==600
q('0018',tipId='en-guc',tip=TIPLER['en-guc'],z='orta',alt='Güç ve Verim',kaz='Eğik düzlemde sabit hızla çekilen yük için gerekli kuvveti, yararlı gücü ve verimli çalışan motorun harcadığı gücü hesaplar.',kalip='hikâyeli',
 metin='Bir inşaat alanında 50 kg kütleli bir yük, kinetik sürtünme katsayısı 0,25 olan 37° eğimli bir rampada, rampaya paralel bir halatla bir motor tarafından yukarı doğru sabit 2 m/s hızla çekilmektedir. Motorun verimi %80’dir ve çekme sırasında halat, makara vb. başka kayıp yoktur.\n(g = 10 m/s², sin 37° = 0,6, cos 37° = 0,8)\nBuna göre, motorun harcadığı güç kaç W’tır?',
 sekil=None,dogru=1000,yan=[(640,'Yararlı gücü verimle çarpmış (800 × 0,8); harcanan güç, yararlı gücün verime bölünmesiyle bulunur.','islem'),(750,'Sürtünmeyi hesaba katmadan yalnız ağırlığın paralel bileşenini (300 N) kullanıp 600 ÷ 0,8 = 750 W bulmuş.','dikkat'),(800,'Verimi hesaba katmamış; yalnız yararlı gücü (F × v = 800 W) vermiş.','dikkat'),(600,'Hem sürtünmeyi hem verimi hesaba katmamış: yalnız 300 × 2 = 600 W.','dikkat')],
 istenen='Motorun harcadığı güç (W).',
 ip=['Sabit hızda yükü çeken kuvvet hangi iki kuvvetin toplamına eşittir? Bu kuvvetle hızın çarpımı neyi verir?'],
 bilgi=[B('Güç','P = F × v (kuvvet ve hız aynı doğrultuda). Örnek: 30 N’luk kuvvetle 4 m/s hızla çekilen cismin gücü 120 W’tır'),VE,SU],
 ad=[A('Sürtünme kuvveti','N = m × g × cos37°.','f = 0,25 × 50 × 10 × 0,8 = 100 N'),A('Çekme kuvveti','Sabit hızda net kuvvet sıfır.','F = m × g × sin37° + f = 300 + 100 = 400 N'),A('Yararlı güç','P = F × v.','P_y = 400 × 2 = 800 W'),A('Harcanan güç','Verim = yararlı güç ÷ harcanan güç.','P = 800 ÷ 0,8 = 1000 W')],
 puf='Harcanan güç = yararlı güç ÷ verim; verim her zaman 1’den küçük olduğundan harcanan güç yararlı güçten büyük çıkar.')
# ===== 19 orta öncüllü · yaya çarpma, sürtünmesiz
card(19,'Yaya çarpan cismin en çok sıkıştığı an','Sürtünmesizde kinetik enerji yay enerjisine dönüşür; en büyük sıkışma anında cisme etkiyen kuvvetler ve enerjiler değerlendirilir.','Hız ve kuvvet kavramlarını karıştırmak.','kolay','şekilli',3,'en-yay','yaya çarpma, nitel')
o=[]
o.append(zemin(-.3,7.4,0)); o.append(duvar(7.2,0,1.0,sol=False)); o.append(yay((4.6,.45),(7.2,.45),8))
o.append(blok(.4,0,.8,.6,'$m$')); o.append(AR((.8,.9),(2.2,.9),'vurgu,very thick')); o.append(N(1.5,1.2,'$v_0$','vurgu'))
o.append(N(5.9,1.0,'$k$'))
SK=tikz(o)
q('0019',tipId='en-yay',tip=TIPLER['en-yay'],z='kolay',alt='Yay Potansiyel Enerjisi',kaz='Yaya çarpan cismin en büyük sıkışma anındaki kinetik enerji, net kuvvet ve yay enerjisini yorumlar.',kalip='şekilli',
 metin='Sürtünmesiz yatay bir zeminde, esneklik sabiti k olan hafif bir yayın bir ucu duvara bağlıdır. Kütlesi m olan cisim v₀ hızıyla yaya doğru gelip yaya çarpıyor, yayı sıkıştırıyor ve yayın en çok sıkıştığı anda bir an duruyor. Yay esneklik sınırını aşmamıştır; cisim yaya bağlı değildir.\nCismin yayı en çok sıkıştırdığı anda,\nI. cismin kinetik enerjisi sıfırdır,\nII. cisme etkiyen net kuvvet sıfırdır,\nIII. yayda depolanan enerji, cismin ilk kinetik enerjisinden büyüktür\nyargılarından hangileri doğrudur?',
 sekil=SK,istenen='Doğru olan yargılar.',
 ip=['En büyük sıkışma anında cisme etkiyen kuvvetleri say.'],
 bilgi=[YE,B('Net kuvvet','cismin hızının sıfır olması, net kuvvetin sıfır olduğu anlamına gelmez. Örnek: yukarı atılan cisim en üst noktada durur ama ağırlık kuvveti etki etmeye devam eder')],
 ad=[A('I. yargı','Cisim bir an durduğuna göre hızı sıfırdır.','E_k = 0 → I doğru'),A('II. yargı','Yay cismi en çok sıkışmış hâlde geri iter; net kuvvet k × x kadardır.','F_net = k × x_max ≠ 0 → II yanlış'),A('III. yargı','Sürtünme yok; yay enerjisi ilk kinetik enerjiye eşittir, ondan büyük olamaz.','E_yay = ½ × m × v₀² → III yanlış')],
 puf='Hızın sıfır olması net kuvvetin sıfır olması demek değildir; en büyük sıkışmada yay kuvveti en büyüktür.',
 **onc([True,False,False],['cisim bir an durduğundan kinetik enerjisi sıfırdır','yay cismi geri ittiğinden net kuvvet k × x kadardır, sıfır değildir','sürtünme olmadığından yay enerjisi ilk kinetik enerjiye eşittir; ondan büyük olamaz'],0))
# ===== 20 orta öncüllü · iki farklı eğimli sürtünmeli düzlem
card(20,'Aynı yükseklikten iki sürtünmeli eğik düzlemde kayma','Isıya dönüşen enerji Q = μ·m·g·h·cotθ ile bulunur; yer çekiminin işi yüksekliğe bağlıdır.','Sürtünmeli yolda da hızların eşit olduğunu sanmak; ısıyı eğimden bağımsız saymak.','orta','şekilli',4,'en-surt','iki eğik düzlem, aynı h')
mu20=Fr(1,2); cot53=Fr(3,4); cot37=Fr(4,3)
assert mu20<Fr(3,4)             # tan37 = 3/4 > 0,5: her iki düzlemde de kayar
QK=mu20*cot53; QL=mu20*cot37     # m·g·h birimi
assert QK<QL and 1-QK>1-QL and QK==Fr(3,8) and QL==Fr(2,3)
h20=3.0; bK=h20*.75; bL=h20*1.333
o=[]
o.append(f'\\fill[gray!15] ({-bK:.3f},0) -- ({bL:.3f},0) -- (0,{h20}) -- cycle;')
o.append(f'\\draw[thick] ({-bK:.3f},0) -- (0,{h20}) -- ({bL:.3f},0) -- cycle;')
th1=radians(53); th2=radians(37)
def blk(side,s,w=.7,hh=.42,t=''):
    # side=-1: sol eğik düzlem (yukarı yön sağa-yukarı u=(cos53,sin53) ters yön ile apex'e göre)
    if side<0:
        ang=th1; base=(0,h20); dirv=(-cos(th1),-sin(th1)); nv=(-sin(th1),cos(th1))
    else:
        ang=th2; base=(0,h20); dirv=(cos(th2),-sin(th2)); nv=(sin(th2),cos(th2))
    P0=(base[0]+dirv[0]*s,base[1]+dirv[1]*s)
    pts=[P0,(P0[0]+dirv[0]*w,P0[1]+dirv[1]*w),(P0[0]+dirv[0]*w+nv[0]*hh,P0[1]+dirv[1]*w+nv[1]*hh),(P0[0]+nv[0]*hh,P0[1]+nv[1]*hh)]
    cx=sum(p[0] for p in pts)/4; cy=sum(p[1] for p in pts)/4
    rot=0
    return '\\draw[thick,fill=gray!25] '+' -- '.join(f'({x:.3f},{y:.3f})' for x,y in pts)+' -- cycle;'+f'\\node[rotate={rot:.1f},font=\\scriptsize] at ({cx:.3f},{cy:.3f}) {{{t}}};'
o.append(blk(-1,.41,t='K')); o.append(blk(1,.55,t='L'))
o.append(f'\\draw ({-bK+.7:.3f},0) arc[start angle=0,end angle=53,radius=.7]; \\node at ({-bK+1.05:.3f},.3) {{$53^\\circ$}};')
o.append(f'\\draw ({bL-.8:.3f},0) arc[start angle=180,end angle=143,radius=.8]; \\node at ({bL-1.18:.3f},.27) {{$37^\\circ$}};')
o.append(D((-bK-.4,h20),(.6,h20),'thin,dashed')); o.append(D((-bK-.4,0),(-bK,0),'thin,dashed')); o.append(DM((-bK-.3,0),(-bK-.3,h20))); o.append(N(-bK-.35,h20/2,'$h$','left'))
o.append(N(0,-.5,'Her iki yüzeyde $\\mu=0{,}5$','font=\\scriptsize'))
SK=tikz(o)
q('0020',tipId='en-surt',tip=TIPLER['en-surt'],z='orta',alt='Sürtünmeli Yollar',kaz='Aynı yükseklikten sürtünmeli, farklı eğimli düzlemlerde kayan özdeş cisimlerin ısıya dönüşen enerjisini ve hızlarını karşılaştırır.',kalip='şekilli',
 metin='Şekildeki gibi aynı h yüksekliğine sahip, eğim açıları 53° ve 37° olan iki eğik düzlemin yüzeylerindeki kinetik sürtünme katsayısı 0,5’tir. Özdeş K ve L cisimleri, bu düzlemlerin üst uçlarından durgun hâlden serbest bırakılıyor ve düzlemlerin tabanına kadar kayıyor.\nCisimler tabana ulaşıncaya kadar,\nI. K’nin ısıya dönüşen enerjisi L’ninkinden küçüktür,\nII. K’nin tabana ulaştığı andaki kinetik enerjisi L’ninkinden büyüktür,\nIII. yer çekimi kuvvetinin yaptığı iş K’de ve L’de eşittir\nyargılarından hangileri doğrudur?',
 sekil=SK,istenen='Doğru olan yargılar.',
 ip=['Bir düzlemde sürtünme kuvveti ve alınan yolu eğim açısına göre yazıp ısıya dönüşen enerjiyi karşılaştır.'],
 bilgi=[SU,IT,B('Yer çekiminin işi','yer çekimi kuvvetinin işi yalnız yükseklik farkına bağlıdır: W = m × g × h; izlenen yol önemli değildir. Örnek: 2 kg, 3 m alçalırsa W = 60 J')],
 ad=[A('Isıya dönüşen enerji','f = μ × m × g × cosθ, yol = h ÷ sinθ.','Q = μ × m × g × h ÷ tanθ → Q_K = 0,375 m·g·h · Q_L = 0,667 m·g·h'),A('I. yargı','Dik düzlemde (53°) yol kısa, kayıp azdır.','Q_K < Q_L → I doğru'),A('II. yargı','Kinetik enerji = m·g·h − Q.','E_K = 0,625 m·g·h > E_L = 0,333 m·g·h → II doğru'),A('III. yargı','İş yalnız yüksekliğe bağlıdır.','W_K = W_L = m × g × h → III doğru')],
 puf='Sürtünmeli eğik düzlemde kayıp enerji μ·m·g·h ÷ tanθ’dır; yatık düzlemde kayıp büyük, tabandaki kinetik enerji küçüktür.',
 **onc([True,True,True],['dik düzlemde yol kısa olduğundan ısıya dönüşen enerji daha azdır','kinetik enerji = m·g·h − ısı olduğundan ısı azken kinetik enerji büyüktür','yer çekiminin işi yalnızca yükseklik farkına bağlıdır ve iki düzlemde de m × g × h’tır'],4))
# ===== yaz
for qq in P.ANA: qq['kardes']=None
SC='/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/en'
P.yaz(os.path.join(GD,'enerji-1.json'),os.path.join(SC,'bos-enerji.json'))
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu='afiz|Enerji ve Hareket'))['kartlar'].append(c['id'])
json.dump(dict(konu='Enerji ve Hareket',surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2018–2026 Fizik (yalnız mantık), 345 AYT Fizik, MEB 11–12. sınıf fizik.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','afenerji.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
