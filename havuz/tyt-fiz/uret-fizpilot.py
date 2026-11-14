"""TYT Fizik PİLOT · 6 şekilli soru (kardeş yok, ipucu 1). Şekil koordinatları Python'da hesaplanır; TikZ (circuitikz, pgfplots) gövdesi bu değerlerden üretilir (cizim.tikz_svg).
Her cevap ve çeldirici değer Python'da assert edilir."""
import sys,os,math,json
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,GD)
import _hafif as H
from _hafif import *
from cizim import tikz_svg
from math import sin,cos,tan,radians,degrees,atan2,sqrt,pi
P=Parti('fizpilot','Dinamik','fiz|Dinamik',ders='TYT Fizik',idon='tytfiz')
TIPK={}
def konu(k,ad): P.k=k; P.konu_adi=ad; H.KONU=ad
def kartla(id,alt,fikir,tuzak,z,adim,tipId,tip,kaynak=None):
    kart(id,alt,fikir,tuzak,z,'şekilli',adim,tipId,tip,kaynak or 'ÖSYM 2018–2026 TYT Fizik soruları (yalnız mantık) · MEB 9–10. sınıf fizik'); TIPK[tipId]=P.k
def q(no,ad,**k):
    assert len(k['ip'])==1
    mk(P,no,ad=ad,adim=len(ad),**k)
def pt(p): return f'({p[0]:.3f},{p[1]:.3f})'
def add(p,q_): return (p[0]+q_[0],p[1]+q_[1])
def mul(p,s): return (p[0]*s,p[1]*s)
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
ARR='-{Stealth[length=1.9mm,width=1.7mm]}'
def orta_ok(renk='vurgu',w='thick'):
    return f'{renk},{w},postaction={{decorate,decoration={{markings,mark=at position .55 with {{\\arrow{{Stealth[length=1.9mm,width=1.7mm]}}}}}}}}'

# =================== 01 · Dinamik · eğik düzlem + makara · zor ===================
konu('fiz|Dinamik','Dinamik')
kartla('K-FZP-01','Eğik düzlemde sürtünmeli makara sistemi','Her cisim için hareket denklemi yazılır: eğik düzlemdeki cisme düzleme paralel bileşen ve kinetik sürtünme, asılı cisme ağırlık etki eder; ortak ivmeden ipteki gerilme bulunur.','Sürtünmeyi unutmak; ağırlığın eğik düzleme paralel bileşenini (mg·sinθ) atlamak; gerilmeyi asılı cismin ağırlığına eşit almak; gerilme denkleminde işaret hatası yapmak.','zor',5,'fzp-dinamik-egik','Eğik düzlem ve makaralı iki cisim sisteminde ip gerilmesi')
g=10; th=radians(37); s37,c37=0.6,0.8; assert abs(sin(th)-s37)<0.002 and abs(cos(th)-c37)<0.002
m1=5; m2=5; mu=0.25
fk=mu*m1*g*c37; a1=(m2*g-m1*g*s37-fk)/(m1+m2); T1=m2*(g-a1)
assert fk==10 and a1==1 and T1==45 and abs(T1-(m1*g*s37+fk+m1*a1))<1e-9
assert m2*g>m1*g*s37+fk                                           # hareket m2 aşağı yönde
d30=m2*(g-(m2*g-fk)/(m1+m2)); assert d30==30                      # eğik düzlem bileşeni unutulmuş
assert (m2*g-m1*g*s37)/(m1+m2)==2 and m2*(g-2)==40                # sürtünmesiz
d50=m2*g; assert d50==50
d55=m2*(g+a1); assert d55==55                                     # T − m2g = m2a yazılmış
Lb=3.7; Ht=Lb*tan(th); Tc=(Lb,Ht); u=(cos(th),sin(th)); n=(-sin(th),cos(th))
bw,bh=.9,.7; hb=bh/2; r=.22; sp=.6
def on_surface(s): return mul(u,s)
def blok1(sc):
    S=on_surface(sc); c=[add(add(S,mul(u,-bw/2)),mul(n,0)),add(add(S,mul(u,bw/2)),mul(n,0)),add(add(S,mul(u,bw/2)),mul(n,bh)),add(add(S,mul(u,-bw/2)),mul(n,bh))]
    return S,c
sc1=1.9; S1,c1=blok1(sc1)
face1=add(add(S1,mul(u,bw/2)),mul(n,hb))                           # ipin bağlandığı nokta
C=add(add(Tc,mul(n,hb-r)),mul(u,sp)); Tp=add(C,mul(n,r)); Vx=C[0]+r
b2c=(Vx,C[1]-1.1-bh/2)                                             # asılı cismin merkezi
assert b2c[0]-bw/2>Lb+.1 and b2c[1]-bh/2>.5
def seg(a,b,st=''): return f'\\draw[{st}] {pt(a)} -- {pt(b)};'
o=[]
o.append(f'\\fill[pattern=north east lines,pattern color=gray] (-.5,-.22) rectangle (5.4,0);')
o.append(f'\\draw (-.5,0) -- (5.4,0);')
o.append(f'\\draw[thick] (0,0) -- {pt(Tc)} -- ({Lb:.3f},0) -- cycle;')
# bloklar
o.append('\\draw[thick,fill=gray!25] '+' -- '.join(map(pt,c1))+' -- cycle;')
o.append(f'\\node[rotate={degrees(th):.2f}] at {pt(add(S1,mul(n,hb)))} {{$5$ kg}};')
o.append(f'\\draw[thick,fill=gray!25] ({b2c[0]-bw/2:.3f},{b2c[1]-bh/2:.3f}) rectangle ({b2c[0]+bw/2:.3f},{b2c[1]+bh/2:.3f});')
o.append(f'\\node at {pt(b2c)} {{$5$ kg}};')
# makara ve ip
o.append(f'\\draw[thick] {pt(Tc)} -- {pt(add(C,(0,0)))};')
o.append(f'\\draw[thick,fill=white] {pt(C)} circle ({r});')
o.append(f'\\fill {pt(C)} circle (1.2pt);')
o.append(seg(face1,Tp,'thick'))
o.append(f'\\draw[thick] ({Vx:.3f},{C[1]:.3f}) -- ({Vx:.3f},{b2c[1]+bh/2:.3f});')
# gerilme okları (ipin cisme uyguladığı kuvvet)
Ta=add(face1,mul(u,.75)); o.append(f'\\draw[vurgu,very thick,{ARR}] {pt(face1)} -- {pt(Ta)};')
o.append(f'\\node[vurgu] at {pt(add(add(face1,mul(u,.42)),mul(n,.22)))} {{$T$}};')
Tb0=(Vx,b2c[1]+bh/2); Tb1=(Vx,b2c[1]+bh/2+.7); o.append(f'\\draw[vurgu,very thick,{ARR}] {pt(Tb0)} -- {pt(Tb1)};')
o.append(f'\\node[vurgu] at ({Vx+.25:.3f},{b2c[1]+bh/2+.42:.3f}) {{$T$}};')
# açı, sürtünme katsayısı
o.append(f'\\draw (.95,0) arc[start angle=0,end angle={degrees(th):.2f},radius=.95];')
o.append(f'\\node at ({1.25*cos(th/2)+.12:.3f},{1.25*sin(th/2):.3f}) {{$37^\\circ$}};')
o.append(f'\\node at (2.55,.62) {{$\\mu_k=0{{,}}25$}};')
SK1=HEAD+'\n'.join(x for x in o if x)+TAIL
SK1=tikz_svg(SK1)
q('0001',tipId='fzp-dinamik-egik',tip='Eğik düzlem ve makaralı iki cisim sisteminde ip gerilmesi',z='zor',alt='Sürtünme Kuvveti',kaz='Eğik düzlem üzerindeki ve asılı cisimden oluşan sistemde ortak ivmeyi ve ip gerilmesini sürtünmeyi de katarak hesaplar.',
 kart='K-FZP-01 (eğik düzlem + makara) · m₁ = m₂ = 5 kg, μ = 0,25, 37°',kalip='şekilli',
 metin='Şekildeki sistemde 37° eğimli eğik düzlem üzerindeki 5 kg kütleli cisim ile asılı duran 5 kg kütleli cisim, hafif ve esnemez bir iple birbirine bağlanmıştır. Makara hafif ve sürtünmesizdir; eğik düzlem ile cisim arasındaki kinetik sürtünme katsayısı 0,25’tir. Sistem serbest bırakılıyor.\n(g = 10 m/s², sin 37° = 0,6, cos 37° = 0,8)\nBuna göre, cisimler hareket ederken ipteki gerilme kuvveti T kaç N’dur?',
 dogru=45,yan=[(30,'Ağırlığın eğik düzleme paralel bileşenini (m₁·g·sin37° = 30 N) hiç hesaba katmamış: a = (50 − 10) ÷ 10 = 4 m/s², T = 5 · (10 − 4) = 30 N.','dikkat'),
  (40,'Sürtünmeyi yok saymış: a = (50 − 30) ÷ 10 = 2 m/s², T = 5 · (10 − 2) = 40 N.','dikkat'),
  (50,'İpin gerilmesini asılı cismin ağırlığına (5 · 10 = 50 N) eşit almış; cisimler ivmeli hareket ettiği için T < m₂g’dir.','bilgi'),
  (55,'Asılı cisim için denklemi T − m₂g = m₂a biçiminde yazmış (işaret hatası): T = 50 + 5 · 1 = 55 N.','islem')],
 istenen='Hareket sırasında ipteki gerilme kuvvetinin büyüklüğü (N).',
 ip=['Sistemi hareket ettiren ve hareketi engelleyen kuvvetleri ayrı ayrı belirleyip önce ortak ivmeyi bulmayı dene.'],
 bilgi=[B('Newton’ın ikinci yasası','bileşke kuvvet = kütle × ivme (ΣF = m·a). İpe bağlı cisimler aynı büyüklükte ivmeyle hareket eder. Örnek: 10 N’luk net kuvvet 2 kg’lık cisme 5 m/s² ivme verir'),
        B('Kinetik sürtünme','f = μ · N; eğik düzlemde N = m·g·cosθ’dır ve f hareket yönünün tersinedir. Ağırlığın düzleme paralel bileşeni m·g·sinθ’dır. Örnek: 2 kg, μ = 0,5, θ = 37° için N = 16 N, f = 8 N')],
 ad=[A('Sürtünme kuvvetini bul','Normal kuvvet N = m₁·g·cos37° ve f = μ·N; cisim eğik düzlemde yukarı hareket edeceğinden f aşağı yönlüdür.','N = 5 · 10 · 0,8 = 40 N → f = 0,25 · 40 = 10 N'),
     A('Hareketin yönünü belirle','Asılı cismin ağırlığı ile eğik düzlem boyunca aşağı yönlü kuvvetleri karşılaştır.','m₂g = 50 N > m₁g·sin37° + f = 30 + 10 = 40 N → m₂ aşağı iner'),
     A('Ortak ivmeyi bul','Tüm sistem için ΣF = (m₁ + m₂)·a yaz.','50 − 30 − 10 = (5 + 5)·a → a = 1 m/s²'),
     A('Asılı cisme uygula','Asılı cisim için aşağı yönlü ağırlık ve yukarı yönlü gerilme.','m₂g − T = m₂a → 50 − T = 5 → T = 45 N'),
     A('Kontrol et','Eğik düzlemdeki cisim için aynı gerilme değerini doğrula.','T − 30 − 10 = 5 · 1 → T = 45 N')],
 puf='İvmeli harekette ip gerilmesi asılı cismin ağırlığına eşit değildir; önce sistemin ortak ivmesini bul, sonra tek bir cisme uygula.',sekil=SK1)

# =================== 02 · Elektrik · devre · orta ===================
konu('fiz|Elektrik','Elektrik')
kartla('K-FZP-02','Seri–paralel devrede ölçü aletleri','Paralel kolların uçları arasındaki gerilim ortaktır; kol akımları toplanıp ana kol akımı bulunur ve seri direnç üzerindeki gerilim eklenerek üretecin gerilimi elde edilir.','Ampermetrenin gösterdiği akımı ana kol akımı sanmak; paralel kol gerilimlerini toplamak; paralel kolları seri gibi toplamak.','orta',5,'fzp-devre-olcu','Ampermetre ve voltmetreli seri–paralel devre')
R1,R2,R3=2,6,3; IA=2
Vp=IA*R2; I3=Vp/R3; It=IA+I3; V1=It*R1; E=Vp+V1
assert (Vp,I3,It,V1,E)==(12,4,6,12,24) and E==It*(R1+R2*R3/(R2+R3))
e8=IA*(R1+R2*R3/(R2+R3)); e12=Vp; e16=Vp+IA*R1; e22=IA*(R1+R2+R3)
assert (e8,e12,e16,e22)==(8,12,16,22)
f=[]
f.append('\\draw (0,0) to[battery1] (0,4);')
f.append('\\draw (0,4) to[R,l=$2\\,\\Omega$] (2.6,4) -- (4,4);')
f.append('\\node[draw,circle,minimum size=.72cm,inner sep=0pt] (A) at (4,1.5) {A};')
f.append('\\draw (4,4) to[R,l_=$6\\,\\Omega$] (4,2.7) -- (A.north);')
f.append('\\draw (A.south) -- (4,0);')
f.append('\\node[left=.05cm of A] {$2$ A};')
f.append('\\draw (4,4) -- (6,4) to[R,l^=$3\\,\\Omega$] (6,0);')
f.append('\\draw (0,0) -- (6,0);')
f.append('\\node[draw,circle,minimum size=.72cm,inner sep=0pt] (V) at (-1.7,2) {V};')
f.append('\\draw (0,4) -- (-1.7,4) -- (V.north); \\draw (V.south) -- (-1.7,0) -- (0,0);')
f.append('\\fill (4,4) circle (1.6pt) (4,0) circle (1.6pt) (0,4) circle (1.6pt) (0,0) circle (1.6pt);')
SK2=tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small,circuitikz/bipoles/length=1.1cm]\n'+'\n'.join(f)+TAIL)
q('0002',tipId='fzp-devre-olcu',tip='Ampermetre ve voltmetreli seri–paralel devre',z='orta',alt='Elektrik Devreleri',kaz='Paralel koldaki ampermetre okumasından kol gerilimini, ana akımı ve üretecin gerilimini bulur.',
 kart='K-FZP-02 (devre, ölçü aletleri) · R₁ = 2 Ω, R₂ = 6 Ω, R₃ = 3 Ω, I = 2 A',kalip='şekilli',
 metin='Şekildeki devrede üreteç, ampermetre ve voltmetre idealdir. Dirençler R₁ = 2 Ω, R₂ = 6 Ω ve R₃ = 3 Ω’dur; ampermetre 2 A’i göstermektedir. Voltmetre üretecin uçlarına bağlıdır.\nBuna göre, voltmetre kaç V’u gösterir?',
 dogru=24,yan=[(8,'Ampermetrenin gösterdiği 2 A’i devrenin ana kol akımı sanmış: V = 2 · (2 + 2) = 8 V (eşdeğer direnç 4 Ω).','dikkat'),
  (12,'Yalnız paralel kolların uçları arasındaki gerilimi (2 · 6 = 12 V) bulmuş; R₁ üzerindeki gerilimi eklememiş.','dikkat'),
  (16,'R₁’den de 2 A geçtiğini sanmış: V = 2 · 6 + 2 · 2 = 16 V; R₃ koluna giden akımı toplamamış.','bilgi'),
  (22,'R₂ ve R₃’ü seri toplayıp (2 + 6 + 3 = 11 Ω) ana kol akımını 2 A almış: V = 2 · 11 = 22 V.','islem')],
 istenen='Voltmetrenin gösterdiği değer (V).',
 ip=['Ampermetrenin hangi koldan geçen akımı ölçtüğüne bak; bu akımla önce paralel kolların ortak gerilimini bulabilirsin.'],
 bilgi=[B('Paralel bağlama','paralel kolların uçları arasındaki gerilim aynıdır; ana koldaki akım, kol akımlarının toplamıdır. Örnek: 12 V altında 4 Ω ve 6 Ω’luk kollardan 3 A ve 2 A, ana koldan 5 A geçer'),
        B('Ohm yasası','V = I · R. Seri bağlı elemanların gerilimleri toplanır; ideal üretecin uçlarındaki gerilim, üretecin emk’sına eşittir. Örnek: 2 A akım 3 Ω’luk dirençte 6 V’luk gerilim düşürür')],
 ad=[A('R₂ koluna uygula','Ampermetre R₂ ile seri olduğundan R₂ koluna ait akımı ölçer.','V_paralel = 2 · 6 = 12 V'),
     A('R₃ koluna uygula','Paralel kolların gerilimi ortaktır.','I₃ = 12 ÷ 3 = 4 A'),
     A('Ana kol akımını bul','Kol akımları toplanır.','I = 2 + 4 = 6 A'),
     A('R₁ üzerindeki gerilim','R₁ ana kolda olduğundan ana kol akımı geçer.','V₁ = 6 · 2 = 12 V'),
     A('Üreteç gerilimi','Voltmetre üretecin uçlarında, R₁ ile paralel koldaki gerilimlerin toplamını ölçer.','V = 12 + 12 = 24 V')],
 puf='Ampermetre hangi koldaysa o kolun akımını verir; ana kol akımı için kol akımlarını toplamayı unutma.',sekil=SK2)

# =================== 03 · Optik · ince kenarlı mercek · orta ===================
konu('fiz|Optik','Optik')
kartla('K-FZP-03','İnce kenarlı merceğin görüntü boyu','Odak uzaklığı ve cisim uzaklığıyla görüntü uzaklığı mercek denkleminden bulunur; büyütme görüntü ve cisim uzaklıklarının oranıdır.','Büyütmeyi yanlış oranla almak (d/f, v/f gibi); cismi 2F ile F arasında sanıp görüntüyü aynı boyda varsaymak.','orta',4,'fzp-mercek-goruntu','İnce kenarlı mercekte görüntü boyu')
f_,d_,h_=10,15,4
v_=1/(1/f_-1/d_); m_=v_/d_; hi=m_*h_
assert abs(v_-30)<1e-9 and abs(m_-2)<1e-9 and abs(hi-8)<1e-9 and f_<d_<2*f_
assert h_*(d_-f_)/f_==2 and h_*d_/f_==6 and h_*d_/(d_-f_)==12 and h_*1==4
sc=.2; Xo=-d_*sc; Xf=f_*sc; Ho=h_*sc; Xe=4.6
assert abs(Xo+3)<1e-9 and abs(Ho-.8)<1e-9
sl2=(0-Ho)/(Xf-0)                                                   # asal eksene paralel ışının kırıldıktan sonraki eğimi (F'den geçer)
sl3=(0-Ho)/(0-Xo)                                                   # merkezden geçen ışının eğimi
ya=Ho+sl2*Xe; yb=0+sl3*Xe
# iki ışın x = v*sc noktasında kesişir (görüntü); çizim alanı bunun öncesinde biter
assert abs((Ho+sl2*(v_*sc))-(sl3*(v_*sc)))<1e-9 and Xe<v_*sc
fo=[]
fo.append(f'\\draw[{ARR}] (-3.9,0) -- (5.0,0);')
fo.append('\\draw[{Stealth[length=2.2mm,width=2mm]}-{Stealth[length=2.2mm,width=2mm]},thick] (0,-1.75) -- (0,1.75);')
fo.append(f'\\draw[very thick,{ARR}] ({Xo:.3f},0) -- ({Xo:.3f},{Ho:.3f});')
fo.append(f'\\fill ({Xf:.3f},0) circle (1.4pt) ({-Xf:.3f},0) circle (1.4pt);')
fo.append(f'\\node[anchor=south west,inner sep=1pt] at ({Xf+.1:.3f},.07) {{$F$}}; \\node[above,inner sep=1pt] at ({-Xf:.3f},.05) {{$F$}};')
fo.append(f'\\draw[{orta_ok()}] ({Xo:.3f},{Ho:.3f}) -- (0,{Ho:.3f});')
fo.append(f'\\draw[{orta_ok()}] (0,{Ho:.3f}) -- ({Xe:.3f},{ya:.3f});')
fo.append(f'\\draw[{orta_ok()}] ({Xo:.3f},{Ho:.3f}) -- (0,0);')
fo.append(f'\\draw[{orta_ok()}] (0,0) -- ({Xe:.3f},{yb:.3f});')
# ölçüler (eksenin altında)
yd=-.85
fo.append(f'\\draw[<->,thin] ({Xo:.3f},{yd}) -- (0,{yd}); \\node[below] at ({Xo/2:.3f},{yd}) {{$15$ cm}};')
fo.append(f'\\draw[<->,thin] (0,{yd}) -- ({Xf:.3f},{yd}); \\node[below] at ({Xf/2:.3f},{yd}) {{$10$ cm}};')
fo.append(f'\\draw[dotted] ({Xo:.3f},0) -- ({Xo:.3f},{yd-.1}); \\draw[dotted] ({Xf:.3f},0) -- ({Xf:.3f},{yd-.1});')
fo.append(f'\\node[left] at ({Xo-.04:.3f},{Ho/2:.3f}) {{$4$ cm}};')
SK3=tikz_svg(HEAD+'\n'.join(fo)+TAIL)
q('0003',tipId='fzp-mercek-goruntu',tip='İnce kenarlı mercekte görüntü boyu',z='orta',alt='Mercekler',kaz='İnce kenarlı merceğin önündeki cismin görüntü uzaklığını ve boyunu odak uzaklığından yararlanarak bulur.',
 kart='K-FZP-03 (mercek) · f = 10 cm, d = 15 cm, h = 4 cm',kalip='şekilli',
 metin='Şekilde odak uzaklığı 10 cm olan ince kenarlı merceğin önünde, mercekten 15 cm uzaklıkta, optik eksene dik duran 4 cm boyunda bir cisim gösterilmiştir. Cisimden çıkan iki özel ışının mercekle karşılaştıktan sonraki yolları da çizilmiştir.\nBuna göre, cismin görüntüsünün boyu kaç cm’dir?',
 dogru=8,yan=[(2,'Büyütmeyi (d − f) ÷ f = 0,5 almış (oranı ters yazmış): 4 · 0,5 = 2 cm.','islem'),
  (4,'Cismin 2F’de olduğunu sanıp görüntünün cisimle aynı boyda (4 cm) olduğunu düşünmüş; oysa cisim F ile 2F arasındadır.','dikkat'),
  (6,'Büyütmeyi d ÷ f = 1,5 almış: 4 · 1,5 = 6 cm.','bilgi'),
  (12,'Büyütmeyi d ÷ (d − f) = 3 almış (pay yerine cisim uzaklığını yazmış): 4 · 3 = 12 cm.','islem')],
 istenen='Görüntünün boyu (cm).',
 ip=['Cismin F ve 2F noktalarına göre konumuna bak; görüntünün mercekten ne kadar uzakta oluştuğunu bulduğunda boyu da bulabilirsin.'],
 bilgi=[B('Mercek denklemi','1/f = 1/d + 1/v (gerçek görüntüde d ve v pozitif). Örnek: f = 6 cm, d = 12 cm ise 1/v = 1/6 − 1/12 → v = 12 cm'),
        B('Büyütme','m = h′/h = v/d. Örnek: d = 20 cm, v = 40 cm ise görüntü cismin 2 katı boydadır ve ters oluşur')],
 ad=[A('Cismin konumunu belirle','Cisim, merceğin F ve 2F noktaları arasındadır; gerçek ve ters görüntü oluşur.','f = 10 cm < d = 15 cm < 2f = 20 cm'),
     A('Görüntü uzaklığını bul','Mercek denklemini uygula.','1/v = 1/10 − 1/15 = 1/30 → v = 30 cm'),
     A('Büyütmeyi bul','Büyütme görüntü uzaklığının cisim uzaklığına oranıdır.','m = 30 ÷ 15 = 2'),
     A('Görüntü boyunu bul','Görüntü boyu = büyütme × cisim boyu.','h′ = 2 · 4 = 8 cm')],
 puf='Önce görüntü uzaklığını mercek denklemiyle bul, büyütmeyi v ÷ d olarak yaz.',sekil=SK3)

# =================== 04 · Sıvıların kaldırma kuvveti · zor ===================
konu('fiz|Sıvıların Kaldırma Kuvveti','Sıvıların Kaldırma Kuvveti')
kartla('K-FZP-04','Yüzen ve batan cisimlerde sıvı seviyesi ve taban basıncı','Yüzen cisim kendi ağırlığı kadar sıvıyı yer değiştirir (batan hacim = ağırlık ÷ sıvı özkütlesi), batan cisim kendi hacmi kadar; toplam yer değiştiren hacim kesit alanına bölünüp seviye artışı ve basınç bulunur.','Yüzen cismin tüm hacmini sıvıya katmak; yalnız batan cismi ya da yalnız yüzeni saymak; seviye artışını hesaplayıp ilk seviyeyi unutmak.','zor',5,'fzp-sivi-seviye','Yüzen ve batan cisimlerle sıvı seviyesi ve taban basıncı')
dsu=1; Ac=60; h0=20; VK,dK=300,.6; VL,dL=120,2
batK=VK*dK/dsu; assert dK<dsu and dL>dsu and batK==180 and VL==120
dh=(batK+VL)/Ac; h1=h0+dh; assert dh==5 and h1==25
Pt=1000*g*h1/100; assert Pt==2500
p2000=1000*g*h0/100; p2200=1000*g*(h0+VL/Ac)/100; p2300=1000*g*(h0+batK/Ac)/100; p2700=1000*g*(h0+(VK+VL)/Ac)/100
assert (p2000,p2200,p2300,p2700)==(2000,2200,2300,2700)
sy=.2     # tek ölçek: 1 cm = 0.2 çizim cm'i (yatay ve düşey)
Wc,Dc=10,6; assert Wc*Dc==Ac                                         # kap önden 10 cm genişlik, 6 cm derinlik
Kwc,Khc=5,10; Lwc,Lhc=4,5; assert Kwc*Dc*Khc==VK and Lwc*Dc*Lhc==VL and Kwc+Lwc<=Wc
kapW,kapH=Wc*sy,32*sy; KW,KH=Kwc*sy,Khc*sy; LW,LH=Lwc*sy,Lhc*sy
Kbat=KH*dK/dsu; assert abs(Kbat/sy-6)<1e-9; yK=h1*sy-Kbat                                       # K'nin alt yüzü
assert abs(Kbat/KH-.6)<1e-9 and yK>LH
def kap(x0,seviye,fo,ust):
    fo.append(f'\\fill[fill=vurgu!15] ({x0},0) rectangle ({x0+kapW},{seviye*sy:.3f});')
    fo.append(f'\\draw[line width=1.1pt] ({x0},{kapH}) -- ({x0},0) -- ({x0+kapW},0) -- ({x0+kapW},{kapH});')
    fo.append(f'\\draw ({x0},{seviye*sy:.3f}) -- ({x0+kapW},{seviye*sy:.3f});')
    fo.append(f'\\node at ({x0+kapW/2},{kapH+.35}) {{{ust}}};')
fq=[]
kap(0,h0,fq,'İlk durum'); xr=3.8; kap(xr,h1,fq,'Son durum')
fq.append(f'\\draw[<->,thin] (-.3,0) -- (-.3,{h0*sy:.3f}); \\node[left] at (-.3,{h0*sy/2:.3f}) {{$20$ cm}};')
kx=xr+.1; fq.append(f'\\draw[thick,fill=gray!35] ({kx},{yK:.3f}) rectangle ({kx+KW},{yK+KH:.3f}); \\node at ({kx+KW/2},{yK+KH/2:.3f}) {{K}};')
lx=xr+kapW-LW-.1; fq.append(f'\\draw[thick,pattern=north east lines,pattern color=gray] ({lx:.3f},0) rectangle ({lx+LW:.3f},{LH}); \\node[fill=white,inner sep=1pt] at ({lx+LW/2:.3f},{LH/2}) {{L}};')
fq.append(f'\\node[below,align=left] at ({kapW/2},-.1) {{su: $1$ g/cm$^3$\\\\kesit alanı: $60$ cm$^2$}};')
fq.append(f'\\node[below,align=left] at ({xr+kapW/2},-.1) {{K: $300$ cm$^3$, $0{{,}}6$ g/cm$^3$\\\\L: $120$ cm$^3$, $2$ g/cm$^3$}};')
SK4=tikz_svg(HEAD+'\n'.join(fq)+TAIL)
q('0004',tipId='fzp-sivi-seviye',tip='Yüzen ve batan cisimlerle sıvı seviyesi ve taban basıncı',z='zor',alt='Kaldırma Kuvveti',kaz='Yüzen ve batan cisimlerin yer değiştirdiği sıvı hacminden seviye artışını ve kap tabanındaki sıvı basıncını hesaplar.',
 kart='K-FZP-04 (kaldırma, seviye, basınç) · A = 60 cm², K yüzer, L batar',kalip='şekilli',
 metin='Şekildeki dikdörtgen prizma biçimli kapta, kesit alanı 60 cm² olan kabın içinde özkütlesi 1 g/cm³ olan su 20 cm yüksekliğe kadar doludur. Suya hacmi 300 cm³, özkütlesi 0,6 g/cm³ olan K cismi ile hacmi 120 cm³, özkütlesi 2 g/cm³ olan L cismi bırakılıyor; K yüzmekte, L ise kabın tabanında durmaktadır. Su kaptan taşmamıştır.\n(Suyun özkütlesi 1000 kg/m³, g = 10 m/s²)\nBuna göre, son durumda kabın tabanındaki sıvı basıncı kaç Pa’dır?',
 dogru=2500,yan=[(2000,'Cisimlerin seviyeyi yükselttiğini hesaba katmamış; ilk seviyedeki basıncı (1000 · 10 · 0,20) yazmış.','dikkat'),
  (2200,'Yalnız batan L cisminin hacmini (120 cm³) saymış; yüzen K’nin batan kısmını atlamış: h = 22 cm.','dikkat'),
  (2300,'Yalnız K’nin batan kısmını (180 cm³) saymış; L’nin hacmini atlamış: h = 23 cm.','dikkat'),
  (2700,'Yüzen K’nin hacminin tamamını (300 cm³) sıvıya batmış saymış: (300 + 120) ÷ 60 = 7 cm artış, h = 27 cm.','bilgi')],
 istenen='Son durumda kabın tabanındaki sıvı basıncı (Pa).',
 ip=['Sıvı seviyesinin ne kadar yükseldiğini bulmak için her cismin sıvıdan yer değiştirdiği hacmi ayrı ayrı düşün.'],
 bilgi=[B('Yüzen cisim','yüzen cismin ağırlığı kaldırma kuvvetine eşittir; batan hacim = cismin kütlesi ÷ sıvı özkütlesi. Örnek: 200 g’lık cisim suda yüzerse 200 cm³ su yer değiştirir'),
        B('Sıvı basıncı','P = h · d · g (h: sıvı yüksekliği). Seviye artışı = yer değiştiren hacim ÷ kesit alanı. Örnek: 30 cm² kesitli kapta 90 cm³ yer değiştiren hacim seviyeyi 3 cm yükseltir')],
 ad=[A('K’nin batan hacmini bul','Yüzen cismin ağırlığı kadar sıvı yer değiştirir; özkütle oranı batan hacim oranını verir.','V_batan = 300 · 0,6 = 180 cm³'),
     A('L’nin yer değiştirdiği hacmi bul','Tabanda duran L tamamen batmıştır.','V = 120 cm³'),
     A('Seviye artışını bul','Toplam yer değiştiren hacmi kesit alanına böl.','Δh = (180 + 120) ÷ 60 = 5 cm'),
     A('Yeni seviyeyi yaz','İlk seviyeye artışı ekle.','h = 20 + 5 = 25 cm = 0,25 m'),
     A('Basıncı hesapla','Sıvı basıncı P = h · d · g.','P = 0,25 · 1000 · 10 = 2500 Pa')],
 puf='Yüzen cisim kendi ağırlığı kadar sıvıyı, batan cisim kendi hacmi kadar sıvıyı yer değiştirir; seviye artışı toplam hacimden bulunur.',sekil=SK4)

# =================== 05 · Hareket · konum–zaman grafiği · orta ===================
konu('fiz|Hareket ve Kuvvet','Hareket ve Kuvvet')
kartla('K-FZP-05','Konum–zaman grafiğinde ortalama hız','Ortalama hız yer değiştirmenin geçen süreye oranıdır; grafikten başlangıç ve bitiş konumları okunur, yol ile yer değiştirme karıştırılmaz.','Ortalama hız yerine ortalama sürati (toplam yol ÷ süre) bulmak; yer değiştirmeyi süreye bölmemek; durma süresini katmamak.','orta',3,'fzp-xt-hiz','Konum–zaman grafiğinden ortalama hız')
pts=[(0,0),(3,15),(5,15),(10,-10)]
dx=pts[-1][1]-pts[0][1]; yol=sum(abs(pts[i+1][1]-pts[i][1]) for i in range(3)); T5=10
assert dx==-10 and yol==40 and abs(dx)/T5==1 and yol/T5==4
assert dx/T5!=0 and abs(dx)==10 and yol/8==5 and (15+10)/T5==2.5
gx=['\\begin{axis}[width=6.6cm,height=5.2cm,xmin=0,xmax=10,ymin=-10,ymax=15,xtick distance=1,ytick={-10,-5,0,5,10,15},grid=both,major grid style={gray!55,thin},tick label style={font=\\scriptsize},axis lines=left,xlabel={$t$ (s)},ylabel={$x$ (m)},xlabel style={font=\\small},ylabel style={font=\\small}]',
    '\\addplot[gray,thin] coordinates {(0,0) (10,0)};',
    '\\addplot[thick,vurgu,mark=*,mark size=1.5pt] coordinates {(0,0) (3,15) (5,15) (10,-10)};',
    '\\end{axis}']
SK5=tikz_svg(HEAD+'\n'.join(gx)+TAIL)
q('0005',tipId='fzp-xt-hiz',tip='Konum–zaman grafiğinden ortalama hız',z='orta',alt='Hareket',kaz='Konum–zaman grafiğinden yer değiştirmeyi okuyup ortalama hızın büyüklüğünü bulur.',
 kart='K-FZP-05 (konum–zaman) · (0,0), (3,15), (5,15), (10,−10)',kalip='grafik',
 metin='Doğrusal bir yolda hareket eden bir aracın konum–zaman grafiği şekildeki gibidir.\nBuna göre, aracın 0–10 s aralığındaki ortalama hızının büyüklüğü kaç m/s’dir?',
 dogru=1,yan=[(10,'Yer değiştirmenin büyüklüğünü (10 m) süreye bölmeyi unutmuş.','islem'),
  (2.5,'Yolu, ulaşılan en uzak konum 15 m ile son konumun büyüklüğü 10 m’nin toplamı olarak (25 m) almış: 25 ÷ 10 = 2,5 m/s.','bilgi'),
  (4,'Toplam yolu (15 + 25 = 40 m) süreye bölüp ortalama sürati bulmuş; ortalama hız yer değiştirmeyle bulunur.','bilgi'),
  (5,'Yalnız araç hareket ederken (8 s) geçen süreyi kullanmış: 40 ÷ 8 = 5 m/s; duraksadığı 2 s de toplam süredir.','dikkat')],
 istenen='0–10 s aralığında ortalama hızın büyüklüğü (m/s).',
 ip=['Ortalama hızı yer değiştirmeyle ilişkilendir: aracın başlangıç ve bitiş konumlarını grafikten oku.'],
 bilgi=[B('Ortalama hız','ortalama hız = yer değiştirme ÷ geçen süre; yer değiştirme son konum − ilk konumdur. Örnek: 5 m’den 20 m’ye 3 s’de giden aracın ortalama hızı 15 ÷ 3 = 5 m/s’dir'),
        B('Yol ve yer değiştirme','yol, konumdaki toplam değişimin mutlak değerlerinin toplamıdır; gidiş–dönüşlü harekette yol ile yer değiştirmenin büyüklüğü farklı olur')],
 ad=[A('Konumları oku','Grafikten t = 0 ve t = 10 s anlarındaki konumları bul.','x₀ = 0 m, x₁₀ = −10 m'),
     A('Yer değiştirmeyi bul','Yer değiştirme = son konum − ilk konum.','Δx = −10 − 0 = −10 m'),
     A('Ortalama hızı hesapla','Süre 10 s; büyüklük istendiğinden mutlak değer alınır.','|v_ort| = 10 ÷ 10 = 1 m/s')],
 puf='Ortalama hız için araya giren hareketlerin önemi yoktur; yalnız ilk ve son konumlara bak, süreyi 0–10 s olarak al.',sekil=SK5)

# =================== 06 · İş, güç ve enerji · ray · kolay ===================
konu('fiz|İş, Güç ve Enerji','İş, Güç ve Enerji')
kartla('K-FZP-06','Sürtünmesiz rayda mekanik enerjinin korunumu','Sürtünmesiz rayda mekanik enerji korunur; iki nokta arasında kinetik enerji artışı yükseklik farkından kaybedilen potansiyel enerjiye eşittir.','Potansiyel enerjiyi (m·g·h_L) ya da toplam enerjiyi (m·g·h_K) kinetik enerji sanmak; yükseklik farkı yerine yükseklikleri toplamak.','kolay',3,'fzp-enerji-ray','Sürtünmesiz rayda iki nokta arasındaki kinetik enerji')
mm=2; hK,hL=1.8,1.0
EkL=mm*g*(hK-hL); assert abs(EkL-16)<1e-9
assert abs(mm*g*hK-36)<1e-9 and abs(mm*g*hL-20)<1e-9 and abs(mm*g*(hK+hL)-56)<1e-9 and abs(.5*mm*g*(hK-hL)-8)<1e-9
sx=.85
keys=[(0.5,1.8),(2.4,0),(4.0,1.0),(5.5,0)]
def prof(xx):
    if xx<=keys[0][0]: return keys[0][1]
    if xx>=keys[-1][0]: return keys[-1][1]
    for (xa,ya_),(xb,yb_) in zip(keys,keys[1:]):
        if xa<=xx<=xb:
            uu=(xx-xa)/(xb-xa); return yb_+(ya_-yb_)*(1+cos(pi*uu))/2
xs=[-.5+i*.05 for i in range(0,int((6.7+.5)/.05)+1)]
curve=' '.join(pt((xx,prof(xx))) for xx in xs)
assert abs(prof(0.5)-hK)<1e-9 and abs(prof(4.0)-hL)<1e-9 and abs(prof(2.4))<1e-9
fr=[]
fr.append(f'\\fill[pattern=north east lines,pattern color=gray] ({xs[0]:.3f},-.3) -- ({xs[0]:.3f},{prof(xs[0]):.3f}) -- plot[smooth,tension=0] coordinates {{{curve}}} -- ({xs[-1]:.3f},-.3) -- cycle;')
fr.append(f'\\draw[thick] plot[smooth,tension=0] coordinates {{{curve}}};')
fr.append(f'\\draw[thick] ({xs[0]:.3f},-.3) -- ({xs[0]:.3f},{prof(xs[0]):.3f}); \\draw[thick] ({xs[0]:.3f},-.3) -- ({xs[-1]:.3f},-.3) -- ({xs[-1]:.3f},0);')
bw6,bh6=.7,.5
fr.append(f'\\draw[thick,fill=gray!25] ({.5-bw6/2:.3f},{hK}) rectangle ({.5+bw6/2:.3f},{hK+bh6}); \\node[font=\\scriptsize] at (.5,{hK+bh6/2:.3f}) {{$2$ kg}};')
fr.append(f'\\node at (.5,{hK+bh6+.28:.3f}) {{K}}; \\node at (4.0,{hL+.3:.3f}) {{L}};')
fr.append(f'\\fill (4.0,{hL}) circle (1.3pt);')
fr.append(f'\\draw[dashed,thin] (-.5,{hK}) -- (-1.0,{hK}); \\draw[dashed,thin] (-.5,0) -- (-1.0,0);')
fr.append(f'\\draw[<->,thin] (-.9,0) -- (-.9,{hK}); \\node[left] at (-.9,{hK/2}) {{$1{{,}}8$ m}};')
fr.append(f'\\draw[dashed,thin] (4.0,{hL}) -- (6.9,{hL}); \\draw[dashed,thin] (5.5,0) -- (6.9,0);')
fr.append(f'\\draw[<->,thin] (6.8,0) -- (6.8,{hL}); \\node[right] at (6.8,{hL/2}) {{$1$ m}};')
SK6=tikz_svg(HEAD+'\n'.join(fr)+TAIL)
q('0006',tipId='fzp-enerji-ray',tip='Sürtünmesiz rayda iki nokta arasındaki kinetik enerji',z='kolay',alt='Mekanik Enerji',kaz='Sürtünmesiz rayda yükseklik farkından kinetik enerji değişimini hesaplar.',
 kart='K-FZP-06 (mekanik enerji) · m = 2 kg, h_K = 1,8 m, h_L = 1 m',kalip='şekilli',
 metin='Şekildeki sürtünmesiz rayda K noktasında durgun olan 2 kg kütleli bir cisim serbest bırakılıyor. Cisim ray boyunca hareket ederek L noktasındaki tepeden geçiyor. K ve L noktalarının yatay zeminden yükseklikleri şekilde verilmiştir.\n(g = 10 m/s²)\nBuna göre, cismin L noktasından geçerken kinetik enerjisi kaç J’dür?',
 dogru=16,yan=[(8,'Yükseklik farkından gelen enerjiye de ½ çarpanını uygulamış: ½ · 2 · 10 · 0,8 = 8 J.','islem'),
  (20,'L noktasındaki potansiyel enerjiyi (2 · 10 · 1) kinetik enerji sanmış.','bilgi'),
  (36,'K noktasındaki toplam enerjiyi (2 · 10 · 1,8) L’deki kinetik enerji sanmış; L’de enerjinin bir kısmı potansiyeldir.','dikkat'),
  (56,'Yükseklikleri toplamış: 2 · 10 · (1,8 + 1) = 56 J; kinetik enerji yükseklik farkıyla bulunur.','islem')],
 istenen='Cismin L noktasındaki kinetik enerjisi (J).',
 ip=['Sürtünme olmadığında hangi enerji türünün toplamı korunur? K ve L noktalarında bu enerjiyi karşılaştır.'],
 bilgi=[B('Mekanik enerjinin korunumu','sürtünmesiz ortamda kinetik ve potansiyel enerjinin toplamı sabittir: E_K + E_P = sabit; potansiyel enerji E_P = m·g·h. Örnek: 1 kg’lık cisim 5 m alçalırsa 50 J kinetik enerji kazanır')],
 ad=[A('K’deki enerjiyi yaz','Cisim durgun olduğundan K’de yalnızca potansiyel enerjisi vardır.','E_K = 2 · 10 · 1,8 = 36 J'),
     A('L’deki potansiyel enerjiyi yaz','L noktası 1 m yüksekliktedir.','E_P(L) = 2 · 10 · 1 = 20 J'),
     A('Korunumu uygula','Toplam mekanik enerji sabit kalır; kalan kısım kinetik enerjidir.','E_k(L) = 36 − 20 = 16 J')],
 puf='Sürtünmesiz rayda kinetik enerji artışı, kaybedilen yükseklik farkı × m·g kadardır.',sekil=SK6)

# =================== yaz ===================
def bitir_fiz():
    for qq in P.ANA: qq['kardes']=None
    P.yaz(os.path.join(GD,'fizpilot-1.json'),'/tmp/bos-fizpilot.json')
    tipler={}
    for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=TIPK[c['tipId']]))['kartlar'].append(c['id'])
    json.dump(dict(konu='Fizik (pilot)',surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 TYT Fizik çıkmış soruları (yalnız mantık), MEB 9–10. sınıf fizik müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar','fizpilot.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler))
bitir_fiz()
