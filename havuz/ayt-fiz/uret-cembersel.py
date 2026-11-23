"""AYT Fizik · Düzgün Çembersel Hareket · 20 soru (kardeş yok, ipucu 1). Şekiller TikZ/pgfplots; sayılar Python'da hesaplanıp assert edilir."""
import sys,os,json
import math
from math import radians,sin,cos,tan,atan2,asin,sqrt,degrees
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-fiz'))
import _hafif as H
from _hafif import *
from cizim import tikz_svg
from fractions import Fraction as Fr
KONUAD='Düzgün Çembersel Hareket'; KK='afiz|Düzgün Çembersel Hareket'
P=Parti('cembersel',KONUAD,KK,ders='AYT Fizik',idon='aytfiz'); H.KONU=KONUAD
g=10
def kartla(n,alt,fikir,tuzak,z,kalip,adim,tipId,tip):
    kart(f'K-AFCEM-{n:02d}',alt,fikir,tuzak,z,kalip,adim,tipId,tip,'ÖSYM AYT 2018–2025 Fizik (yalnız mantık) · 345 AYT Fizik SB · MEB 11. sınıf')
KN={}
def q(no,n,z,alt,kalip,tipId,tip,kaz,ad,**k):
    assert len(k['ip'])==1 and 3<=len(ad)<=6
    mk(P,f'{no:04d}',ad=ad,adim=len(ad),z=z,alt=alt,kalip=kalip,tipId=tipId,tip=tip,kaz=kaz,kart=f'K-AFCEM-{n:02d} ({alt})',**k)
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'; TAIL='\n\\end{tikzpicture}'
def FIG(s): return tikz_svg(HEAD+s+TAIL)
FR='red!70!black'
def AX(body,xmax,ymin,ymax,xt,yt,yl,xl,w=6.4,h=4.6):
    xs=','.join(map(str,xt)); ys=','.join(map(str,yt))
    opt=(r'width=%scm,height=%scm,xmin=0,xmax=%s,ymin=%s,ymax=%s,xtick={%s},ytick={%s},grid=both,major grid style={gray!55,thin},'
         r'tick label style={font=\footnotesize},axis lines=left,xlabel={%s},ylabel={%s},xlabel style={font=\small},ylabel style={font=\small}')%(w,h,xmax,ymin,ymax,xs,ys,xl,yl)
    if ymin<0: body+='\\addplot[black,thin] coordinates {(0,0) (%s,0)};\n'%xmax
    return tikz_svg(HEAD+'\\begin{axis}['+opt+']\n'+body+'\n\\end{axis}'+TAIL)
def pl(pts,st='thick,vurgu'): return f'\\addplot[{st}] coordinates {{'+' '.join(f'({a},{b})' for a,b in pts)+'};\n'
ROM=['I','II','III']
ADLAR=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
KUME={'Yalnız I':{0},'Yalnız II':{1},'Yalnız III':{2},'I ve II':{0,1},'I ve III':{0,2},'II ve III':{1,2},'I, II ve III':{0,1,2}}
def onc(no,n,z,alt,tipId,tip,kaz,kok,items,sec,sekil=None,**k):
    """items: (yargı metni, doğru mu, gerekçe cümlesi). Doğru küme, anahtar, çeldirici açıklamaları ve adımlar BU listeden üretilir."""
    T={i for i,it in enumerate(items) if it[1]}
    dogru=[a for a in ADLAR if KUME[a]==T][0]; assert dogru in sec and len(sec)==5 and len(set(sec))==5
    sira=[a for a in ADLAR if a in sec]
    yan=[]
    for a in sira:
        if a==dogru: continue
        S=KUME[a]; c=[]
        for i in sorted(S-T): c.append(f'{ROM[i]}. yargıyı doğru sanmış; oysa {items[i][2]}')
        for i in sorted(T-S): c.append(f'{ROM[i]}. yargıyı yanlış sanmış; oysa {items[i][2]}')
        yan.append((a,' '.join(c),'bilgi'))
    metin=kok+'\n'+'\n'.join(f'{ROM[i]}. {it[0]}' for i,it in enumerate(items))+'\nyargılarından hangileri doğrudur?'
    ad=[A(f'{ROM[i]}. yargıyı incele',it[2][0].upper()+it[2][1:],f'{ROM[i]}: {"doğru" if it[1] else "yanlış"}') for i,it in enumerate(items)]+[A('Sonucu belirle','Doğru yargıların kümesi yanıttır.',dogru)]
    q(no,n,z,alt,'öncüllü',tipId,tip,kaz,ad,metin=metin,dogru=dogru,yan=yan,sira=sira,sekil=sekil,istenen='Doğru olan yargılar.',**k)
    return dogru
def sq(v):
    v=Fr(v); n,d=v.numerator,v.denominator; rn,rd=round(sqrt(n)),round(sqrt(d)); assert rn*rn==n and rd*rd==d,v
    return Fr(rn,rd)

TP=dict(te=('cem-temel','Çizgisel ve açısal nicelikler'),di=('cem-disk','Dönen disk ve merkezcil kuvvet'),vi=('cem-viraj','Viraj problemleri'),
        du=('cem-dusey','Düşey düzlemde çembersel hareket'),ko=('cem-konik','Konik sarkaç ve koni yüzeyi'),ro=('cem-rotor','Dönen silindir (rotor)'),
        gr=('cem-grafik','Grafik yorumu'),zi=('cem-zincir','Birbirine bağlı cisimler'))
kartla(1,'Çizgisel ve açısal nicelikler','Aynı kayışla veya aynı eksende bağlı çarklarda ya çizgisel sürat ya da açısal hız ortaktır; v = ωr ve F = mv²/r ilişkileriyle diğeri bulunur.','Merkezcil kuvvete ayrı bir kuvvet gibi davranmak; v = ωr ilişkisinde ortak büyüklüğü karıştırmak.','kolay','şekilli',3,*TP['te'])
kartla(2,'Dönen disk','Dönen yüzeyde duran cismi merkeze çeken kuvvet sürtünmedir; kayma sınırında sürtünme kuvveti en büyük değerindedir ve merkezcil kuvvete eşittir.','Kuvvetin kütleye bağlı olduğunu sanmak; karekökü unutmak; yarıçapı metreye çevirmemek.','orta','şekilli',3,*TP['di'])
kartla(3,'Viraj problemleri','Yatay virajda merkezcil kuvveti sürtünme, eğimli virajda yol tepkisinin yatay bileşeni (ve gerekirse sürtünme) sağlar; bileşenler düşey ve yatayda ayrı ayrı yazılır.','Eğimli virajda tepkiyi ağırlığa eşit almak; tan, sin ve cos bileşenlerini karıştırmak.','orta','şekilli',4,*TP['vi'])
kartla(4,'Düşey düzlemde çembersel hareket','Her konumda yarıçap doğrultusundaki bileşke kuvvet merkezcil kuvvettir; konumlar arası sürat değişimi enerji korunumundan bulunur.','Merkezcil kuvvete ağırlığı hep eklemek; yükseklik farkını yanlış almak.','zor','şekilli',5,*TP['du'])
kartla(5,'Konik sarkaç ve koni yüzeyi','Gerilme veya tepkinin düşey bileşeni ağırlığı dengeler, yatay bileşeni merkezcil kuvveti oluşturur; yarıçap, ip boyu ve açıdan bulunur.','İp boyunu yörünge yarıçapı sanmak; açıyı yataya göre almak; gerilmeyi ağırlığa eşitlemek.','orta','şekilli',4,*TP['ko'])
kartla(6,'Dönen silindir','Duvara yapışan cismi düşmekten sürtünme, merkezcil kuvveti duvarın dik tepkisi sağlar; denge koşulları ayrı yazılır.','Sürtünme kuvvetini dik tepkiyle karıştırmak; kütlenin sonucu etkilediğini sanmak.','orta','öncüllü',3,*TP['ro'])
kartla(7,'Grafik yorumu','Grafikteki doğrunun eğimi ve kesim noktası, bağıntıdaki sabit niceliklerden okunur; bağıntı önce yazılır.','Eksen değişkenini karıştırmak; eğimi yarıçap sanmak.','orta','grafik',4,*TP['gr'])
kartla(8,'Birbirine bağlı cisimler','Aynı eksen etrafında dönen bağlı cisimlerde açısal hız ortaktır; her ipin gerilmesi, ipin dışında kalan cisimlerin merkezcil kuvvetleri farkından bulunur.','Her ipe yalnız bir cismi yazmak; gerilmeleri toplamak.','zor','şekilli',4,*TP['zi'])
B_MER=B('Merkezcil kuvvet','düzgün çembersel harekette cisme etki eden net kuvvet çemberin merkezine yöneliktir ve büyüklüğü F = mv²/r = mω²r’dir. Merkezcil kuvvet ayrı bir kuvvet değil, gerçek kuvvetlerin merkeze doğru bileşkesidir. Örnek: 1 kg’lık cisim 1 m yarıçaplı çemberde 2 m/s ile dönerse F = 4 N')
B_VW=B('Çizgisel sürat ve açısal hız','v = ω·r ve T = 2π/ω ilişkileri geçerlidir; dönen cisimlerde hangi büyüklüğün ortak, hangisinin yarıçapa bağlı olduğu bağıntıdan çıkarılır. Örnek: ω = 3 rad/s ve r = 2 m olan nokta 6 m/s ile hareket eder')
B_DUS=B('Düşey çember','çemberin her noktasında yarıçap doğrultusundaki kuvvetlerin bileşkesi merkezcil kuvvete eşittir; ağırlığın yarıçap doğrultusundaki bileşeni konuma göre değişir. Sürtünmesiz ortamda iki nokta arasındaki sürat değişimi mgh = ½mΔ(v²) ile bulunur')

# ===================== 01 · kolay · merkezcil kuvvet =====================
m1,r1,v1=2,Fr(1,2),3
F1=Fr(m1)*v1**2/r1; assert F1==36
assert Fr(m1)*v1**2*r1==9 and Fr(m1)*v1/r1==12 and m1*v1**2==18 and F1+m1*g==56
SK=FIG(r'''\draw[gray,dashed] (0,0) circle (1.5);
\fill (0,0) circle (.06); \node[below left] at (0,0) {O};
\draw[thick] (0,0) -- (1.5,0); \node[below] at (.75,0) {ip, $0{,}5$ m};
\draw[thick,fill=gray!40] (1.5,0) circle (.17); \node[below right] at (1.5,-.15) {$m=2$ kg};
\draw[vurgu,very thick,-{Stealth[length=2.4mm]}] (1.5,.3) -- (1.5,1.3); \node[right] at (1.5,.85) {$v=3$ m/s};''')
q(1,1,'kolay','Merkezcil kuvvet','şekilli',*TP['te'],'Düzgün çembersel hareketteki cisim için ip gerilmesini merkezcil kuvvet bağıntısından bulur.',
 metin='Sürtünmesi önemsiz yatay bir masa üzerinde, bir ucu O noktasına bağlı ağırlıksız iple tutulan cisim, şekildeki gibi düzgün çembersel hareket yapmaktadır.\nBuna göre, ipteki gerilme kuvvetinin büyüklüğü kaç N’dur?',
 dogru=36,yan=[(9,'Merkezcil kuvveti mv²·r diye yazıp yarıçapla çarpmış: 2 · 9 · 0,5 = 9 N.','islem'),(12,'v² yerine v almış: 2 · 3 ÷ 0,5 = 12 N.','islem'),(18,'Yarıçapa bölmeyi unutmuş: 2 · 3² = 18 N.','dikkat'),(56,'Yatay masada ağırlığı da ipe eklemiş: 36 + 20 = 56 N.','bilgi')],
 istenen='İpteki gerilme kuvvetinin büyüklüğü (N).',ip=['Cismin hareketini sürdüren kuvvetin yönünü belirle; bu kuvvet hangi bağıntıyla hesaplanır?'],
 bilgi=[B_MER],
 ad=[A('Veriyi oku','Şekilden kütle, yarıçap ve sürat okunur.','m = 2 kg, r = 0,5 m, v = 3 m/s'),A('Merkezcil kuvveti belirle','Yatay masada merkeze yönelen tek yatay kuvvet ip gerilmesidir.','T = mv²/r'),A('Hesapla','Değerleri yerine koy.','T = 2 × 9 ÷ 0,5 = 36 N')],
 puf='Yatay düzlemde ağırlık ile tepki birbirini dengeler; merkeze doğru net kuvveti ip sağlar.',sekil=SK)

# ===================== 02 · kolay · kayışla bağlı kasnaklar =====================
rK,rL,wK=10,40,8
wL=Fr(wK*rK,rL); assert wL==2
assert wK*rL//rK==32 and Fr(wK*rK**2,rL**2)==Fr(1,2) and wK*rK==80
c1,c2,d=0.0,4.2,4.2; R1,R2=0.6,2.4
ph=asin((R2-R1)/d); nx,ny=-sin(ph),cos(ph)
p1=(R1*nx,R1*ny); p2=(c2+R2*nx,R2*ny)
SK=FIG(rf'''\draw[thick,fill=gray!25] (0,0) circle ({R1}); \draw[thick,fill=gray!25] ({c2},0) circle ({R2});
\fill (0,0) circle (.05); \fill ({c2},0) circle (.05);
\draw[thick] ({p1[0]:.3f},{p1[1]:.3f}) -- ({p2[0]:.3f},{p2[1]:.3f}); \draw[thick] ({p1[0]:.3f},{-p1[1]:.3f}) -- ({p2[0]:.3f},{-p2[1]:.3f});
\node at (0,-.2) {{K}}; \node at ({c2},.45) {{L}};
\node[below] at (-.2,-.85) {{$r_K=10$ cm}}; \node[below] at ({c2},-1.0) {{$r_L=40$ cm}};
\draw[vurgu,very thick,-{{Stealth[length=2mm]}}] (-.65,.9) arc[start angle=140,end angle=40,radius=1.0];
\node[above,font=\small] at (0,1.5) {{$\omega_K=8$ rad/s}};''')
q(2,1,'kolay','Kayışla bağlı kasnaklar','şekilli',*TP['te'],'Kaymadan dönen kayışla bağlı kasnaklarda çizgisel sürat eşitliğinden açısal hızı bulur.',
 metin='Yarıçapları şekilde verilen K ve L kasnakları bir kayışla birbirine bağlanmıştır. Kayış kasnaklar üzerinde kaymadan dönmektedir ve K kasnağı şekildeki açısal hızla dönmektedir.\nBuna göre, L kasnağının açısal hızı kaç rad/s’dir?',
 dogru=2,yan=[(Fr(1,2),'Yarıçap oranını iki kez uygulamış: 8 · (10 ÷ 40)² = 0,5 rad/s.','islem'),(8,'Kasnakların açısal hızlarını eşit sanmış.','bilgi'),(32,'Açısal hızı yarıçapla doğru orantılı sanmış: 8 · 40 ÷ 10 = 32 rad/s.','bilgi'),(80,'K’nin çizgisel süratini (8 · 10 = 80 cm/s) L’nin açısal hızı sanmış.','dikkat')],
 istenen='L kasnağının açısal hızı (rad/s).',ip=['Kayışın üzerindeki noktaların hareketini karşılaştır; hangi büyüklük iki kasnak için ortaktır?'],
 bilgi=[B_VW],
 ad=[A('Ortak büyüklüğü bul','Kayış kaymadığı için iki kasnağın kenarındaki noktaların çizgisel sürati eşittir.','v_K = v_L'),A('Bağıntıyı yaz','Her kasnak için v = ωr.','ω_K · r_K = ω_L · r_L'),A('Çöz','Değerleri yerine koy.','8 × 10 = ω_L × 40 → ω_L = 2 rad/s')],
 puf='Kayışın üzerindeki noktalar için hangi büyüklük iki kasnakta ortak olabilir?',sekil=SK)

# ===================== 03 · kolay · öncüllü kavram =====================
onc(3,1,'kolay','Düzgün çembersel hareketin özellikleri','cem-temel',TP['te'][1],'Düzgün çembersel hareketin vektörel ve skaler niteliklerini ayırt eder.',
 'Sürtünmesiz yatay bir düzlemde, ipin ucuna bağlı bir cisim düzgün çembersel hareket yapmaktadır.\nBuna göre, cisimle ilgili;',
 [('Çizgisel süratinin büyüklüğü sabittir.',True,'düzgün çembersel harekette hızın yalnız yönü değişir, büyüklüğü (sürat) sabit kalır.'),
  ('Hız vektörü sabittir.',False,'hız vektörünün yönü her an değiştiği için hız vektörü sabit değildir.'),
  ('Merkezcil ivmesi her an çemberin merkezine yönelir.',True,'merkezcil ivme her konumda çemberin merkezine doğrudur ve cismi çembersel yörüngede tutar.')],
 ['Yalnız I','Yalnız II','I ve II','I ve III','II ve III'],
 ip=['Hızın bir vektör olduğunu, vektörün hem büyüklüğü hem yönü olduğunu hatırla.'],bilgi=[B_MER],puf='Bir vektörün hangi özellikleri değişebilir?')

# ===================== 04 · orta · disk, sürtünme =====================
k4=Fr(1,2); r4=Fr(20,100); w4=sq(k4*g/r4); assert w4==5
assert k4*g/r4==25 and sq(k4*g*r4)==1 and sq(g/(k4*r4))==10 and sq(k4*g/20)==Fr(1,2)
SK=FIG(r'''\draw[thick,fill=gray!15] (0,0) circle (2.2);
\fill (0,0) circle (.06); \node[above left] at (0,0) {O};
\draw[thick,fill=gray!50] (.85,-.15) rectangle (1.15,.15);
\draw[<->] (0,-.45) -- (1,-.45) node[midway,below] {$20$ cm};
\draw[vurgu,very thick,-{Stealth[length=2.4mm]}] (1.0,.25) -- (1.0,1.2);
\draw[thick,-{Stealth[length=2mm]}] (-1.75,-1.15) arc[start angle=213,end angle=245,radius=2.1]; \node at (-1.0,-1.75) {$\omega$};
\draw[dashed,gray] (0,0) circle (1.0);''')
q(4,2,'orta','Dönen disk','şekilli',*TP['di'],'Kayma sınırında sürtünme kuvvetini merkezcil kuvvete eşitleyerek açısal hızı bulur.',
 metin='Düşey eksen etrafında dönebilen yatay bir diskin üzerine, eksenden şekildeki uzaklıkta bir cisim konulmuştur. Cisim ile disk arasındaki sürtünme katsayısı 0,5’tir. Diskin açısal hızı sıfırdan başlayarak çok yavaş artırılıyor.\n(g = 10 m/s²)\nBuna göre, cisim diskin üzerinde kaymaya başladığı anda diskin açısal hızı kaç rad/s’dir?',
 dogru=5,yan=[(Fr(1,2),'Yarıçapı 20 cm yerine 20 almış: √(0,5 · 10 ÷ 20) = 0,5 rad/s.','dikkat'),(1,'Merkezcil kuvvet eşitliğinde yarıçapa bölmek yerine çarpmış: √(0,5 · 10 · 0,2) = 1 rad/s.','islem'),(10,'Sürtünme katsayısını paydaya yazmış: √(10 ÷ (0,5 · 0,2)) = 10 rad/s.','islem'),(25,'Karekök almayı unutup ω² değerini (25) yazmış.','dikkat')],
 istenen='Kayma anındaki açısal hız (rad/s).',ip=['Cismi çembersel yörüngede tutan kuvvetin kaynağını belirle ve bu kuvvetin alabileceği en büyük değeri düşün.'],
 bilgi=[B_MER,B('Sürtünme kuvveti','yatay yüzeyde en büyük (kayma sınırındaki) sürtünme kuvveti f = k·N’dir; yatay düzlemde N cismin ağırlığına eşittir. Örnek: k = 0,2 ve m = 3 kg ise f en çok 6 N olur')],
 ad=[A('Merkezcil kuvveti sağlayanı bul','Diskte cismi merkeze çeken kuvvet sürtünmedir.','f = mω²r'),A('Kayma sınırında sürtünme','En büyük sürtünme kuvveti k·m·g’dir.','f = k·m·g'),A('Eşitle','Kütle sadeleşir.','mω²r = kmg → ω² = kg/r = 0,5 · 10 ÷ 0,2 = 25'),A('Karekök al','Açısal hız ω² değerinin kareköküdür.','ω = 5 rad/s')],
 puf='Kayma sınırında sürtünme kuvveti en büyük değerindedir; merkezcil kuvvet eşitliğinde kütle sadeleşir.',sekil=SK)

# ===================== 05 · orta · öncüllü disk K, L =====================
SK=FIG(r'''\draw[thick,fill=gray!15] (0,0) circle (2.7);
\fill (0,0) circle (.06); \node[above left] at (0,0) {O};
\draw[thick,fill=gray!55] (.95,-.15) rectangle (1.25,.15); \node[above] at (1.1,.15) {K};
\draw[thick,fill=gray!55] (2.0,-.15) rectangle (2.3,.15); \node[above left] at (2.15,.15) {L};
\draw[<->] (0,-.5) -- (1.1,-.5) node[midway,below] {$r$}; \draw[<->] (0,-1.15) -- (2.15,-1.15) node[midway,below] {$2r$};
\draw[thick,-{Stealth[length=2mm]}] (-1.9,-1.35) arc[start angle=215,end angle=250,radius=2.3]; \node at (-1.0,-2.0) {$\omega$};''')
d5=onc(5,2,'orta','Dönen disk','cem-disk',TP['di'][1],'Aynı eksende dönen cisimlerin periyot, sürat ve merkezcil kuvvetlerini yarıçapa göre karşılaştırır.',
 'Düşey eksen etrafında sabit açısal hızla dönen yatay bir diskin üzerine, şekildeki gibi özdeş K ve L cisimleri konulmuştur. Cisimler disk üzerinde kaymadan dönmektedir.\nBuna göre, K ve L cisimleri için;',
 [('Periyotları eşittir.',True,'aynı disk üzerinde olduklarından ω ve dolayısıyla T = 2π/ω eşittir.'),
  ('Çizgisel süratleri eşittir.',False,'v = ωr olduğundan yarıçapı büyük olan L’nin sürati K’ninkinin iki katıdır.'),
  ('Merkezcil kuvvetlerinin büyüklükleri eşittir.',False,'F = mω²r olduğundan kütleleri ve ω eşitken yarıçapı büyük olan L’nin merkezcil kuvveti daha büyüktür.')],
 ['Yalnız I','Yalnız II','I ve II','I ve III','II ve III'],sekil=SK,
 ip=['Cisimlerin disk üzerinde kaymadığını göz önünde bulundurarak hangi büyüklüklerin ortak, hangilerinin yarıçapa bağlı olduğunu ayır.'],bilgi=[B_VW],
 puf='Aynı disk üzerindeki iki cismin ortak büyüklükleri hangileridir?')
assert d5=='Yalnız I'

# ===================== 06 · orta · düz viraj =====================
R6=100; k6=Fr(1,10); v6=sq(k6*g*R6); assert v6==10; kmh=v6*Fr(36,10); assert kmh==36
assert v6==10 and k6*g*R6==100 and kmh*Fr(36,10)==Fr(1296,10) and v6*36==360
a=-0.0
import math
cx,cy=0,0; Rin,Rout=3.0,4.4; Rm=3.7; th=48
def pol(r,a): return (r*cos(radians(a)),r*sin(radians(a)))
cp=pol(Rm,th)
SK=FIG(rf'''\fill[gray!25] (0:{Rin}) arc[start angle=0,end angle=90,radius={Rin}] -- (90:{Rout}) arc[start angle=90,end angle=0,radius={Rout}] -- cycle;
\draw[thick] (0:{Rin}) arc[start angle=0,end angle=90,radius={Rin}]; \draw[thick] (0:{Rout}) arc[start angle=0,end angle=90,radius={Rout}];
\draw[dashed,gray] (90:{Rm}) arc[start angle=90,end angle=0,radius={Rm}];
\fill (0,0) circle (.06); \node[below left] at (0,0) {{O}};
\draw[thick] (0,0) -- ({cp[0]:.3f},{cp[1]:.3f}); \node[above left] at ({cp[0]*.5:.3f},{cp[1]*.5:.3f}) {{$R=100$ m}};
\begin{{scope}}[shift={{({cp[0]:.3f},{cp[1]:.3f})}},rotate={th+90}]
\draw[thick,fill=white] (-.38,-.2) rectangle (.38,.2); \draw[thick] (.1,-.2) -- (.1,.2); \draw[thick] (-.2,-.2) -- (-.2,.2);
\end{{scope}}
\draw[vurgu,very thick,-{{Stealth[length=2.4mm]}}] ({cp[0]-0.55*sin(radians(th)):.3f},{cp[1]+0.55*cos(radians(th)):.3f}) -- ({cp[0]-1.35*sin(radians(th)):.3f},{cp[1]+1.35*cos(radians(th)):.3f});''')
q(6,3,'orta','Yatay viraj','şekilli',*TP['vi'],'Yatay virajda en büyük sürati sürtünme katsayısı ve yarıçaptan hesaplar ve birim çevirir.',
 metin='Yatay ve düz bir yolun şekildeki virajını, yol ile lastikler arasındaki sürtünme katsayısı 0,1 olan yağışlı havada dönen bir otomobil, savrulmadan hareket etmektedir.\n(g = 10 m/s²)\nBuna göre, otomobilin virajı savrulmadan dönebileceği en büyük sürat kaç km/h’tir?',
 dogru=36,yan=[(10,'En büyük sürati doğru bulmuş (10 m/s) ancak km/h’ye çevirmemiş.','dikkat'),(100,'Karekök almayı unutup v² = 100 değerini yazmış.','dikkat'),(Fr(1296,10),'m/s değerini km/h’ye çevirirken 3,6 ile iki kez çarpmış: 10 · 3,6 · 3,6 = 129,6.','islem'),(360,'m/s değerini 36 ile çarparak km/h’ye çevirmiş.','islem')],
 istenen='Virajı dönebileceği en büyük sürat (km/h).',ip=['Viraj yatay olduğuna göre aracı çembersel yörüngede tutan kuvvetin ne olduğunu ve alabileceği en büyük değeri belirle.'],
 bilgi=[B_MER,B('Birim çevirme','1 m/s = 3,6 km/h’tir. Örnek: 5 m/s = 18 km/h')],
 ad=[A('Merkezcil kuvvetin kaynağı','Yatay virajda merkeze yönelen tek yatay kuvvet sürtünmedir.','f = mv²/R'),A('En büyük sürtünme','Savrulma sınırında f = k·mg.','mv²/R = kmg'),A('Sürati bul','Kütle sadeleşir.','v² = kgR = 0,1 · 10 · 100 = 100 → v = 10 m/s'),A('Birimi çevir','m/s değeri 3,6 ile çarpılır.','10 × 3,6 = 36 km/h')],
 puf='Yatay virajda en büyük sürat yalnız sürtünme katsayısı ile viraj yarıçapına bağlıdır; araç kütlesi sonucu etkilemez.',sekil=SK)

# ===================== 07 · orta · eğimli viraj, tanθ =====================
def banked(th,thlab,Rlab,Rtxt=None):
    c_,s_=cos(radians(th)),sin(radians(th)); L=4.6
    px,py=2.7*c_,2.7*s_
    return FIG(rf'''\fill[gray!30] (0,0) -- ({L*c_:.3f},{L*s_:.3f}) -- ({L*c_:.3f},-.35) -- (0,-.35) -- cycle; \draw[very thick] (0,0) -- ({L*c_:.3f},{L*s_:.3f});
\draw[dotted] (0,0) -- ({L*c_:.3f},0); \draw (1.3,0) arc[start angle=0,end angle={th},radius=1.3]; \node[right] at ({1.35*cos(radians(th/2)):.3f},{1.3*sin(radians(th/2)):.3f}) {{{thlab}}};
\begin{{scope}}[shift={{({px:.3f},{py:.3f})}},rotate={th}]
\draw[thick,fill=white] (-.6,0) rectangle (.6,.48); \draw[thick,fill=gray!40] (-.3,.48) rectangle (.3,.8); \draw[thick,fill=gray!70] (-.35,.0) circle (.1); \draw[thick,fill=gray!70] (.35,.0) circle (.1);
\end{{scope}}
\draw[dashed] (-.7,-.35) -- (-.7,{py+1.4:.3f}); \node[above] at (-.7,{py+1.4:.3f}) {{eksen}};
\draw[<->] (-.7,{py+1.15:.3f}) -- ({px:.3f},{py+1.15:.3f}); \node[above] at ({(px-.7)/2:.3f},{py+1.15:.3f}) {{{Rlab}}};
\draw[dashed,gray] ({px:.3f},{py+.5:.3f}) -- ({px:.3f},{py+1.15:.3f});''')
v7=20; R7=80; tan7=Fr(v7**2,g*R7); assert tan7==Fr(1,2)
assert Fr(v7**2,2*g*R7)==Fr(1,4) and Fr(g*R7,v7**2)==2 and Fr(72**2,g*R7)==Fr(648,100) and Fr(v7**2,g*(R7//2))==1
SK=banked(degrees(atan2(1,2)),r'$\theta$',r'$R=80$ m')
q(7,3,'orta','Eğimli viraj','şekilli',*TP['vi'],'Sürtünmesiz eğimli virajda tepkinin bileşenlerini yazarak eğim açısının tanjantını bulur.',
 metin='Yatayla θ açısı yapan eğimli bir yolun virajı, şekildeki gibi yarıçaplı çembersel bir yörüngedir. Sürtünmenin önemsiz olduğu bu virajı 72 km/h sabit süratle dönen bir otomobil, yol üzerinde yanal yönde kaymadan hareket etmektedir.\n(g = 10 m/s²)\nBuna göre, tanθ değeri kaçtır?',
 dogru=Fr(1,2),yan=[(Fr(1,4),'Paydada 2gR yazmış: 400 ÷ (2 · 10 · 80) = 0,25.','islem'),(1,'Şekildeki R değerini çap sanıp yarıya indirmiş: 400 ÷ (10 · 40) = 1.','dikkat'),(2,'Bağıntıyı ters yazmış: gR ÷ v² = 800 ÷ 400 = 2.','islem'),(Fr(648,100),'72 km/h değerini m/s’ye çevirmeden yerine koymuş: 72² ÷ (10 · 80) = 6,48.','dikkat')],
 istenen='Eğim açısının tanjantı (tanθ).',ip=['Otomobile etki eden kuvvetleri çiz; kuvvetleri düşey ve yatay doğrultularda bileşenlerine ayır.'],
 bilgi=[B_MER,B('Birim çevirme','1 km/h = 1 ÷ 3,6 m/s’dir. Örnek: 36 km/h = 10 m/s')],
 ad=[A('Sürati çevir','72 km/h değeri m/s’ye çevrilir.','v = 72 ÷ 3,6 = 20 m/s'),A('Kuvvetleri yaz','Sürtünme yoksa yol tepkisi N’nin düşey bileşeni ağırlığı, yatay bileşeni merkezcil kuvveti sağlar.','N cosθ = mg · N sinθ = mv²/R'),A('Oranla','Taraf tarafa bölününce kütle sadeleşir.','tanθ = v²/(gR)'),A('Hesapla','Değerleri yerine koy.','tanθ = 400 ÷ (10 · 80) = 0,5')],
 puf='Yol tepkisi yola diktir; bileşenlerini ayrı ayrı yazıp oranlarsan bilinmeyen sayısı azalır.',sekil=SK)

# ===================== 08 · orta · öncüllü, viraj değişkenleri =====================
v_ = lambda k,R: sq(k*g*R)
kk,RR=Fr(36,100),10; assert v_(4*kk,RR)==2*v_(kk,RR)   # k 4 katı -> v 2 katı
assert Fr(sqrt(1/2))!=Fr(1,2)  # R yarıya inince v/√2 (yarıya inmez)
d8=onc(8,3,'orta','Yatay viraj','cem-viraj',TP['vi'][1],'Yatay virajda en büyük sürat bağıntısının değişkenlere bağımlılığını yorumlar.',
 'Yatay ve düz bir virajı, yol ile lastikler arasındaki sürtünme kuvvetinin yardımıyla dönen bir otomobilin, virajı savrulmadan dönebileceği en büyük sürati v’dir.\nBuna göre, v ile ilgili;',
 [('Otomobilin kütlesi artırılırsa v artar.',False,'v = √(kgR) bağıntısında kütle yoktur; en büyük sürat kütleye bağlı değildir.'),
  ('Sürtünme katsayısı 4 katına çıkarılırsa v 2 katına çıkar.',True,'v, √k ile orantılıdır; k dört katına çıkınca v iki katına çıkar.'),
  ('Viraj yarıçapı yarıya indirilirse v yarıya iner.',False,'v, √R ile orantılıdır; R yarıya inince v yarıya değil, 1/√2 katına iner.')],
 ['Yalnız II','Yalnız III','I ve II','I ve III','II ve III'],
 ip=['En büyük sürati veren bağıntıyı kuvvet eşitliğinden çıkar, her niceliğin bağıntıda yer alıp almadığına bak.'],bilgi=[B_MER],
 puf='Bağıntıyı yazdıktan sonra değişken sadeleşiyorsa sonuç o değişkenden bağımsızdır; kareköklü ilişkilere dikkat et.')
assert d8=='Yalnız II'

# ===================== 09 · orta · köprü =====================
m9,v9,R9=1000,10,50; N9=m9*(Fr(g)-Fr(v9**2,R9)); assert N9==8000
assert m9*Fr(v9**2,R9)==2000 and m9*g==10000 and m9*(g+Fr(v9**2,R9))==12000 and m9*(g-g)==0
SK=FIG(r'''\begin{scope}[shift={(0,-4)}]
\draw[very thick] (53.13:5) arc[start angle=53.13,end angle=126.87,radius=5];
\fill[gray!25] (53.13:5) arc[start angle=53.13,end angle=126.87,radius=5] -- (126.87:4.4) arc[start angle=126.87,end angle=53.13,radius=4.4] -- cycle;
\fill (0,0) circle (.06); \draw[dashed] (0,0) -- (0,5); \node[left] at (0,2.3) {$R=50$ m};
\end{scope}
\draw[thick,fill=white] (-.6,1.0) rectangle (.6,1.5); \draw[thick,fill=gray!40] (-.3,1.5) rectangle (.3,1.8);
\draw[thick,fill=gray!70] (-.35,1.0) circle (.1); \draw[thick,fill=gray!70] (.35,1.0) circle (.1);
\draw[vurgu,very thick,-{Stealth[length=2.4mm]}] (.8,1.25) -- (1.8,1.25); \node[above] at (1.5,1.25) {$v$};''')
q(9,4,'orta','Tümsek köprü','şekilli',*TP['du'],'Tümsek bir köprünün tepe noktasında merkezcil kuvvet ile ağırlık ve tepkiyi ilişkilendirir.',
 metin='Kütlesi 1000 kg olan bir otomobil, yüzeyi şekildeki gibi çembersel bir yay olan tümsek bir köprünün en yüksek noktasından 10 m/s sabit süratle geçmektedir.\n(g = 10 m/s²)\nBuna göre, otomobil bu noktadan geçerken yolun otomobile uyguladığı tepki kuvvetinin büyüklüğü kaç N’dur?',
 dogru=8000,yan=[(0,'Merkezcil ivmenin g’ye eşit olduğunu sanıp m(g − g) = 0 bulmuş.','bilgi'),(2000,'Merkezcil kuvveti (mv²/R = 2000 N) tepki sanmış.','bilgi'),(10000,'Tepkiyi ağırlığa eşit almış: mg = 10000 N.','bilgi'),(12000,'Merkezcil kuvveti ağırlığa eklemiş (çukur yoldaki gibi): 10000 + 2000 = 12000 N.','dikkat')],
 istenen='Yolun otomobile uyguladığı tepki kuvveti (N).',ip=['Otomobile etki eden iki kuvveti çembersel yörüngenin yarıçapı doğrultusunda ayır; merkeze doğru olanı belirle.'],
 bilgi=[B_DUS],
 ad=[A('Kuvvetleri belirle','Tepe noktasında merkez aşağıdadır; ağırlık merkeze doğru, tepki dışarı doğrudur.','mg − N = mv²/R'),A('Merkezcil kuvveti hesapla','Değerleri yerine koy.','mv²/R = 1000 × 100 ÷ 50 = 2000 N'),A('Tepkiyi bul','Ağırlıktan merkezcil kuvvet çıkarılır.','N = 10000 − 2000 = 8000 N')],
 puf='Merkez aşağıda olduğundan merkeze doğru bileşke, ağırlık ile tepkinin farkıdır.',sekil=SK)

# ===================== 10 · orta · konik sarkaç, sürat =====================
L10,th10=2,37; r10=Fr(L10)*Fr(6,10); t10=Fr(3,4); v10=sq(g*r10*t10); assert r10==Fr(6,5) and v10==3
w10=Fr(25,10); assert w10*r10==3 and w10*L10==5 and sq(g*r10*Fr(4,3))==4 and g*r10*t10==9 and w10**2*r10==Fr(15,2)
sx,sy=3.4*sin(radians(37)),-3.4*cos(radians(37))
SK=FIG(rf'''\fill[gray!35] (-1.2,0) rectangle (3.2,.2); \draw[thick] (-1.2,0) -- (3.2,0);
\draw[dashed] (0,0) -- (0,{sy-.6:.3f});
\draw[thick] (0,0) -- ({sx:.3f},{sy:.3f}); \node[above right] at ({sx/2:.3f},{sy/2:.3f}) {{$\ell=2$ m}};
\draw[dashed,gray] ({sx:.3f},{sy:.3f}) ellipse ({sx:.3f} and .45); \draw[dashed,gray] (0,{sy:.3f}) -- ({sx:.3f},{sy:.3f});
\draw (0,-1.2) arc[start angle=-90,end angle=-53,radius=1.2]; \node at (.35,-1.5) {{$37^\circ$}};
\draw[thick,fill=gray!45] ({sx:.3f},{sy:.3f}) circle (.2); \node[above right] at ({sx+.1:.3f},{sy+.15:.3f}) {{$m=400$ g}};''')
q(10,5,'orta','Konik sarkaç','şekilli',*TP['ko'],'Konik sarkaçta ipin düşeyle yaptığı açıdan çizgisel sürati hesaplar.',
 metin='Bir ucu tavana bağlı ağırlıksız ipin ucundaki cisim, şekildeki gibi yatay düzlemde düzgün çembersel hareket yapmaktadır. Hava direnci önemsizdir.\n(g = 10 m/s²; sin37° = 0,6; cos37° = 0,8)\nBuna göre, cismin çizgisel süratinin büyüklüğü kaç m/s’dir?',
 dogru=3,yan=[(4,'Açıyı yataya göre almış: v² = g · r · tan53° = 16 → v = 4 m/s.','dikkat'),(5,'Yörünge yarıçapı yerine ip boyunu kullanıp v = ωℓ = 2,5 · 2 = 5 m/s bulmuş.','dikkat'),(Fr(15,2),'Sürati ω²r = 7,5 değeriyle karıştırmış (merkezcil ivme).','bilgi'),(9,'Karekök almayı unutup v² = 9 değerini yazmış.','dikkat')],
 istenen='Cismin çizgisel süratinin büyüklüğü (m/s).',ip=['Yörünge yarıçapını ip boyu ve açıdan hesapla; cisme etki eden iki kuvveti düşey ve yatay bileşenlerine ayır.'],
 bilgi=[B_MER,B('Konik sarkaç','ip düşeyle θ açısı yapıyorsa yörünge yarıçapı r = ℓ sinθ’dır; gerilmenin düşey bileşeni ağırlığı dengeler, yatay bileşeni merkezcil kuvvettir')],
 ad=[A('Yarıçapı bul','Yörünge yarıçapı ip boyunun yatay izdüşümüdür.','r = ℓ sin37° = 2 × 0,6 = 1,2 m'),A('Kuvvet dengesi','Düşeyde T cosθ = mg, yatayda T sinθ = mv²/r.','tanθ = v²/(g r)'),A('Sürati hesapla','Değerleri yerine koy.','v² = 10 × 1,2 × 0,75 = 9'),A('Karekök al','Sürat v² değerinin kareköküdür.','v = 3 m/s')],
 puf='İpin gerilmesi eğik olduğundan düşey bileşeni ağırlığı dengeler; yatay bileşen merkezcil kuvveti oluşturur.',sekil=SK)

# ===================== 11 · orta · öncüllü, rotor =====================
SK=FIG(r'''\draw[thick] (0,0) -- (0,3.4); \draw[thick] (3,0) -- (3,3.4); \draw[thick] (-.15,3.4) -- (3.15,3.4); \draw[thick,fill=gray!30] (-.15,0) rectangle (0,3.4); \draw[thick,fill=gray!30] (3,0) rectangle (3.15,3.4);
\draw[dashed] (1.5,-.3) -- (1.5,3.9); \draw[thick,fill=gray!55] (2.65,1.4) rectangle (3,1.9); \node[left] at (2.6,1.65) {m};
\draw[<->] (1.5,1.0) -- (3,1.0) node[midway,below] {$r$};
\draw[thick,-{Stealth[length=2mm]}] (.9,3.75) arc[start angle=200,end angle=340,x radius=.65,y radius=.2]; \node[above] at (1.5,3.95) {$\omega$};''')
d11=onc(11,6,'orta','Dönen silindir','cem-rotor',TP['ro'][1],'Dönen silindirde duvara yapışan cismin kuvvetlerini ve kütleden bağımsızlığı yorumlar.',
 'Şekildeki silindirin iç yüzeyine yapışan m kütleli cisim, silindir düşey eksen etrafında sabit açısal hızla dönerken düşmeden silindirle birlikte dönmektedir. Silindir ile cisim arasındaki sürtünme katsayısı k’dir.\nBuna göre;',
 [('Cisme etki eden sürtünme kuvvetinin büyüklüğü, cismin ağırlığına eşittir.',True,'cisim düşeyde dengede olduğundan sürtünme kuvveti ağırlığa eşittir.'),
  ('Silindirin açısal hızı artırılırsa, silindirin cisme uyguladığı dik tepki kuvvetinin büyüklüğü artar.',True,'dik tepki merkezcil kuvvet olduğundan N = mω²r bağıntısına göre ω ile artar.'),
  ('Cismin kütlesi artırılırsa, cismin düşmeden dönebilmesi için gereken en küçük açısal hız artar.',False,'kmω²r = mg eşitliğinde kütle sadeleşir; gereken en küçük açısal hız kütleye bağlı değildir.')],
 ['Yalnız I','Yalnız III','I ve II','I ve III','II ve III'],sekil=SK,
 ip=['Cisme etki eden kuvvetleri çiz; hangi kuvvetin düşeyde, hangisinin yatayda etkili olduğunu ayır.'],bilgi=[B_MER],
 puf='Düşey ve yatay doğrultularda hangi kuvvetler dengeyi, hangisi merkezcil kuvveti belirler?')
assert d11=='I ve II'

# ===================== 12 · orta · F–v² grafiği =====================
m12=2; sl=Fr(1,2); r12=Fr(m12)/sl; assert r12==4 and 16*sl==8
assert Fr(16,8)==2 and Fr(8,m12*16)==Fr(1,4) and Fr(m12*8,16)==1 and r12!=8
SK=AX(pl([(0,0),(32,16)]),32,0,16,range(0,33,8),range(0,17,4),'$F$ (N)','$v^2$ (m$^2$/s$^2$)')
q(12,7,'orta','Merkezcil kuvvet–sürat grafiği','grafik',*TP['gr'],'F–v² grafiğinin eğiminden çember yarıçapını bulur.',
 metin='Kütlesi 2 kg olan bir cisim, sürtünmesiz yatay düzlemde bir ipin ucunda sabit yarıçaplı çembersel yörüngede farklı süratlerle döndürülüyor. Cisme etki eden merkezcil kuvvetin büyüklüğü (F) ile cismin süratinin karesi (v²) arasındaki ilişki grafikte verilmiştir.\nBuna göre, çembersel yörüngenin yarıçapı kaç m’dir?',
 dogru=4,yan=[(Fr(1,4),'Bağıntıyı r = F ÷ (m·v²) biçiminde ters yazmış: 8 ÷ (2 · 16) = 0,25 m.','islem'),(1,'r = m·F ÷ v² yazmış: 2 · 8 ÷ 16 = 1 m.','islem'),(2,'Kütleyi hesaba katmamış: r = v² ÷ F = 16 ÷ 8 = 2 m.','dikkat'),(8,'Grafikten okuduğu F değerini (8 N) yarıçap sanmış.','dikkat')],
 istenen='Çembersel yörüngenin yarıçapı (m).',ip=['Merkezcil kuvvet bağıntısını v² cinsinden yaz ve doğrunun eğiminin neye karşılık geldiğini bul.'],
 bilgi=[B_MER],
 ad=[A('Bağıntıyı yaz','F, v² ile doğru orantılıdır.','F = (m/r) · v²'),A('Eğimi oku','Grafikte v² = 16 için F = 8 N.','eğim = 8 ÷ 16 = 0,5 kg/m'),A('Yarıçapı bul','Eğim m/r değerine eşittir.','m/r = 0,5 → r = 2 ÷ 0,5 = 4 m')],
 puf='Doğrusal grafikte eğim, bağıntıdaki sabit çarpandır; hangi niceliklerden oluştuğunu bağıntıdan çıkar.',sekil=SK)

# ===================== 13 · orta · öncüllü, dönme dolap =====================
SK=FIG(r'''\draw[thick] (0,0) circle (1.7);
\foreach \a in {0,45,...,315} {\draw (0,0) -- (\a:1.7);}
\draw[thick] (0,0) -- (-1.4,-3.1); \draw[thick] (0,0) -- (1.4,-3.1); \draw[thick] (-1.8,-3.1) -- (1.8,-3.1);
\foreach \a/\n in {90/A,0/B,270/C,180/D} {\draw[thick,fill=gray!30] (\a:1.95) circle (.26); }
\node at (0,2.45) {A}; \node at (2.5,0) {B}; \node at (-2.5,0) {D}; \node[right] at (.3,-2.15) {C};
\fill (0,0) circle (.07);
\draw[thick,-{Stealth[length=2mm]}] (-.75,.6) arc[start angle=140,end angle=40,radius=.95]; \node at (0,1.15) {$\omega$};''')
d13=onc(13,4,'orta','Dönme dolap','cem-dusey',TP['du'][1],'Düşey düzlemde sabit açısal hızla dönen cismin farklı konumlarında net kuvvet ve tepkiyi karşılaştırır.',
 'Şekildeki dönme dolap, düşey düzlemde sabit açısal hızla dönmektedir. Kabinlerden birinde oturan Aleyna’nın kütle merkezinin dönme eksenine uzaklığı sabittir ve Aleyna her an koltukla temas hâlindedir. A ve C noktaları sırasıyla dolabın en üst ve en alt noktalarıdır.\nBuna göre, Aleyna için;',
 [('A ve C noktalarında net kuvvetin büyüklüğü eşittir.',True,'sürat ve yarıçap sabit olduğundan net kuvvet her noktada mω²r büyüklüğündedir.'),
  ('C noktasında koltuğun Aleyna’ya uyguladığı kuvvet, Aleyna’nın ağırlığından büyüktür.',True,'C’de merkez yukarıda olduğundan N − mg = mω²r ve N = mg + mω²r > mg olur.'),
  ('A noktasında koltuğun Aleyna’ya uyguladığı kuvvet, Aleyna’nın ağırlığından küçüktür.',True,'A’da merkez aşağıda olduğundan mg − N = mω²r ve N = mg − mω²r < mg olur.')],
 ['I ve II','I ve III','II ve III','I, II ve III','Yalnız II'],sekil=SK,
 ip=['Her konumda net kuvvetin yönünü ve büyüklüğünü belirle; hangi kuvvetin merkeze doğru olduğuna bak.'],bilgi=[B_DUS],
 puf='A ve C noktalarında Aleyna’ya etki eden kuvvetleri çizip net kuvvetin yönüne bak.')
assert d13=='I, II ve III'

# ===================== 14 · orta · öncüllü, koni =====================
al=55; ta=tan(radians(al))
def kx(h): return h/ta
SK=FIG(rf'''\fill[gray!30] (-2.8,0) rectangle (2.8,-.2); \draw[thick] (-2.8,0) -- (2.8,0);
\draw[very thick] (0,0) -- ({kx(3.2):.3f},3.2); \draw[very thick] (0,0) -- ({-kx(3.2):.3f},3.2);
\draw[thick] ({kx(3.2):.3f},3.2) arc[start angle=0,end angle=-180,x radius={kx(3.2):.3f},y radius=.4]; \draw[thick,dashed] ({kx(3.2):.3f},3.2) arc[start angle=0,end angle=180,x radius={kx(3.2):.3f},y radius=.4];
\draw[dashed] (0,-.1) -- (0,3.9);
\draw[dashed,gray] (0,1.1) -- ({kx(1.1):.3f},1.1); \draw[dashed,gray] (0,2.4) -- ({kx(2.4):.3f},2.4);
\draw[thick,fill=gray!55] ({kx(1.1):.3f},1.1) circle (.17); \node[right] at ({kx(1.1)+.2:.3f},1.1) {{K}};
\draw[thick,fill=gray!55] ({kx(2.4):.3f},2.4) circle (.17); \node[right] at ({kx(2.4)+.2:.3f},2.4) {{L}};
\draw (1.0,0) arc[start angle=0,end angle={al},radius=1.0]; \node[right] at (1.05,.3) {{$\alpha$}};
\draw[thick,-{{Stealth[length=2mm]}}] (-.55,3.95) arc[start angle=200,end angle=340,x radius=.55,y radius=.2]; \node[above] at (0,4.05) {{$\omega$}};''')
d14=onc(14,5,'orta','Koni iç yüzeyi','cem-konik',TP['ko'][1],'Sürtünmesiz koni yüzeyinde çembersel hareket yapan cisimlerin tepki, ivme ve açısal hızını karşılaştırır.',
 'Yatay düzlemle α açısı yapan sürtünmesiz bir koninin iç yüzeyinde, özdeş K ve L cisimleri şekildeki yüksekliklerde düşey eksen etrafında düzgün çembersel hareket yapmaktadır.\nBuna göre, K ve L cisimleri için;',
 [('Açısal hızları eşittir.',False,'ω² = g tanα ÷ r olduğundan yarıçapı büyük olan L’nin açısal hızı K’ninkinden küçüktür.'),
  ('Yüzeyin uyguladığı tepki kuvvetlerinin büyüklükleri eşittir.',True,'tepkinin düşey bileşeni ağırlığı dengelediğinden N = mg/cosα her ikisi için aynıdır.'),
  ('Merkezcil ivmelerinin büyüklükleri eşittir.',True,'merkezcil ivme a = g tanα bağıntısından konumdan bağımsızdır, her ikisi için aynıdır.')],
 ['Yalnız I','Yalnız II','I ve II','I ve III','II ve III'],sekil=SK,
 ip=['Cisimlerden birine etki eden kuvvetleri düşey ve yatay doğrultularda yaz; bulduğun bağıntılarda yarıçapın bulunup bulunmadığına bak.'],bilgi=[B_MER],
 puf='Bulduğun bağıntılarda yarıçap r görünüyor mu?')
assert d14=='II ve III'

# ===================== 15 · zor · düşey çember, yatay nokta =====================
m15,r15,vB=Fr(1,2),1,6; vC2=vB**2-2*g*r15; T15=m15*vC2/r15; assert T15==8 and vC2==16
assert m15*(vC2/r15-g)==3 and T15+m15*g==Fr(26,2) and m15*vB**2/r15==18 and m15*(g+vB**2/r15)==23
SK=FIG(r'''\draw[gray,dashed] (0,0) circle (1.7);
\fill (0,0) circle (.06); \node[above left] at (0,0) {O};
\draw[thick] (0,0) -- (1.7,0); \draw[thick,fill=white] (1.7,0) circle (.17); \node[above right] at (1.75,.1) {C};
\draw[thick,fill=gray!45] (0,-1.7) circle (.17); \node[below] at (0,-1.95) {B};
\draw[vurgu,very thick,-{Stealth[length=2.4mm]}] (.3,-1.7) -- (1.3,-1.7); \node[below] at (1.0,-1.75) {$v_B=6$ m/s};
\node[right] at (0,-.8) {$\ell=1$ m}; \draw[thick] (0,0) -- (0,-1.7); \node[left] at (-.2,-1.7) {$m=500$ g};''')
q(15,4,'zor','Düşey çember, yatay konum','şekilli',*TP['du'],'Enerji korunumu ile düşey çemberin yatay konumundaki süratini bulup ip gerilmesini hesaplar.',
 metin='Ağırlıksız bir ipin ucuna bağlı bilye, düşey düzlemde O noktası etrafında hava direnci önemsenmeden çembersel hareket yapmaktadır. Bilye, çemberin en alt noktası olan B noktasından şekildeki sürat ile geçmektedir.\n(g = 10 m/s²)\nBuna göre, bilye ipin yatay olduğu C noktasından geçerken ipteki gerilme kuvveti kaç N’dur?',
 dogru=8,yan=[(3,'C noktasında merkezcil kuvvet eşitliğine ağırlığı da katmış: T = m(v²/r − g) = 3 N.','dikkat'),(13,'Ağırlığı gerilmeye eklemiş: 8 + 5 = 13 N.','bilgi'),(18,'B noktasındaki sürati C noktasında da aynı sanmış: 0,5 · 36 ÷ 1 = 18 N.','dikkat'),(23,'B noktasındaki gerilmeyi bulmuş: 0,5 · (10 + 36) = 23 N.','dikkat')],
 istenen='C noktasında ipteki gerilme kuvveti (N).',ip=['Önce bilyenin C noktasındaki süratini bulmak için B ile C arasında enerjiye bak; sonra C’de yarıçap doğrultusundaki kuvvetleri yaz.'],
 bilgi=[B_DUS],
 ad=[A('Yükseklik farkı','B’den C’ye çıkış, çemberin yarıçapı kadardır.','h = r = 1 m'),A('Enerji korunumu','Ağırlığın işi kinetik enerjiyi azaltır.','v_C² = v_B² − 2gh = 36 − 20 = 16'),A('C’de kuvvet','C’de ağırlık yatay doğrultuya diktir; merkeze doğru tek kuvvet gerilmedir.','T = mv_C²/r'),A('Hesapla','Değerleri yerine koy.','T = 0,5 × 16 ÷ 1 = 8 N')],
 puf='İpin yatay olduğu konumda ağırlığın yarıçap doğrultusundaki bileşeni nedir?',sekil=SK)

# ===================== 16 · zor · eğimli viraj, sürtünmeli =====================
th16=37; R16=45; v16=30; t16=Fr(3,4); kmin=(Fr(v16**2,g*R16)-t16)/(1+t16*Fr(v16**2,g*R16)); assert kmin==Fr(1,2)
s_,c_=Fr(3,5),Fr(4,5); X=Fr(v16**2,g*R16); assert (s_+kmin*c_)/(c_-kmin*s_)==X
assert (X*c_-s_)==1 and (Fr(g)/c_)*(s_+1)==Fr(g)/c_*s_+Fr(g)/c_ and X-t16==Fr(5,4) and t16==Fr(3,4) and X==2
SK=banked(37,r'$37^\circ$',r'$R=45$ m')
q(16,3,'zor','Eğimli viraj, sürtünmeli','şekilli',*TP['vi'],'Sürtünmeli eğimli virajda düşey ve yatay denge denklemlerini birlikte çözerek en küçük sürtünme katsayısını bulur.',
 metin='Yatayla şekildeki açıyı yapan eğimli bir yolun virajı, şekilde verilen yarıçaplı çembersel bir yörüngedir. Bu virajı 30 m/s sabit süratle dönen bir otomobil, ideal sürati aştığı için yol ile lastikler arasındaki sürtünme kuvvetinin yardımıyla yol üzerinde savrulmadan (yamaçtan dışarı kaymadan) hareket etmektedir.\n(g = 10 m/s²; sin37° = 0,6; cos37° = 0,8)\nBuna göre, yol ile lastikler arasındaki sürtünme katsayısı en az kaç olmalıdır?',
 dogru=Fr(1,2),yan=[(1,'Sürtünmeyi yamaç boyunca değil yatay almış: N cosθ = mg ve N sinθ + kN = mv²/R → 0,6 + k = 1,6 → k = 1.','islem'),(Fr(3,4),'Sürtünme katsayısını tanθ’ya eşit almış: k = 0,75.','bilgi'),(Fr(5,4),'Paydadaki 1 + k·tanθ terimini unutmuş: 2 − 0,75 = 1,25.','islem'),(2,'Yalnız v² ÷ (gR) oranını (2) katsayı sanmış.','bilgi')],
 istenen='En küçük sürtünme katsayısı (k).',ip=['Sürtünme kuvvetinin yönünü belirle (araç dışarı kayma eğiliminde); kuvvetleri düşey ve yatay doğrultularda bileşenlerine ayır.'],
 bilgi=[B_MER,B('Eğik düzlemde bileşenler','yatayla θ açısı yapan yüzeyde yüzeye dik kuvvet N’nin düşey bileşeni N cosθ, yatay bileşeni N sinθ’dır; yüzey boyunca f kuvvetinin düşey bileşeni f sinθ, yatay bileşeni f cosθ’dır')],
 ad=[A('Kuvvetleri yaz','Araç yamaçtan dışarı kayacağı için sürtünme yol boyunca aşağı yönündedir (f = kN).','Düşey: N cosθ = mg + f sinθ'),A('Yatay denklem','Merkezcil kuvvet N ile f’nin yatay bileşenlerinin toplamıdır.','Yatay: N sinθ + f cosθ = mv²/R'),A('Oranla','Taraf tarafa bölüp f = kN yazılır; kütle sadeleşir.','(sinθ + k cosθ) ÷ (cosθ − k sinθ) = v²/(gR) = 2'),A('k’yi çöz','sin37° = 0,6 ve cos37° = 0,8 yerine konur.','0,6 + 0,8k = 1,6 − 1,2k → k = 0,5')],
 puf='Aracın kayma eğilimini düşün ve sürtünme kuvvetinin yönünü kendin belirle.',sekil=SK)

# ===================== 17 · zor · ipli zincir =====================
m17,w17,l1,l2=1,2,Fr(1,2),Fr(1,2)
T2=m17*w17**2*(l1+l2); T1=T2+m17*w17**2*l1; assert T2==4 and T1==6
assert m17*w17**2*l1==2 and T2+m17*w17**2*(l1+l2)==8 and T1+T2==10
SK=FIG(r'''\fill (0,0) circle (.07); \node[below left] at (0,0) {O};
\draw[thick] (0,0) -- (2.2,0); \draw[thick] (2.2,0) -- (4.4,0);
\draw[thick,fill=gray!45] (2.2,0) circle (.17); \node[below] at (2.2,-.2) {K}; \draw[thick,fill=gray!45] (4.4,0) circle (.17); \node[below] at (4.4,-.2) {L};
\node[below] at (1.1,-.05) {ip$_1$, $0{,}5$ m}; \node[below] at (3.3,-.05) {ip$_2$, $0{,}5$ m};
\node[below] at (2.2,-.9) {$m_K=1$ kg}; \node[below] at (4.4,-.9) {$m_L=1$ kg};
\draw[vurgu,very thick,-{Stealth[length=2.4mm]}] (2.2,.3) -- (2.2,.9); \draw[vurgu,very thick,-{Stealth[length=2.4mm]}] (4.4,.3) -- (4.4,1.5);''')
q(17,8,'zor','Ardışık iplerle bağlı cisimler','şekilli',*TP['zi'],'Ardışık iplerde gerilmeleri dışta kalan cisimlerin merkezcil kuvvetlerinden hesaplar.',
 metin='Sürtünmesiz yatay bir masa üzerinde, kütleleri ve ip boyları şekilde verilen K ve L cisimleri, ağırlıksız iplerle O noktasına ve birbirine bağlanmıştır. Cisimler O noktası etrafında 2 rad/s sabit açısal hızla ve O, K, L her an doğrusal kalacak biçimde düzgün çembersel hareket yapmaktadır.\nBuna göre, O ile K arasındaki ip₁’deki gerilme kuvveti kaç N’dur?',
 dogru=6,yan=[(2,'Yalnız K’nin merkezcil kuvvetini (mω²r = 2 N) gerilme sanmış.','dikkat'),(4,'Yalnız L’nin merkezcil kuvvetini (ip₂ gerilmesini) bulmuş.','dikkat'),(8,'K’yi de O’dan 1 m uzakta sanıp iki cismin merkezcil kuvvetlerini toplamış: 4 + 4 = 8 N.','islem'),(10,'İki ipin gerilmelerini toplamış: 4 + 6 = 10 N.','bilgi')],
 istenen='O–K arasındaki ipteki gerilme kuvveti (N).',ip=['Önce en dıştaki cismi, sonra içteki cismi ayrı ayrı çiz; her cisme etki eden ip kuvvetlerinin yönünü belirle.'],
 bilgi=[B_MER,B('Net kuvvet','cisme etki eden kuvvetlerin merkeze doğru bileşkesi merkezcil kuvvete eşittir; her cisim için ayrı yazılır')],
 ad=[A('L cismi','L’ye yalnız ip₂ etki eder; L, O’dan 1 m uzaktadır.','T₂ = mω²·(1) = 1 × 4 × 1 = 4 N'),A('K cismi','K’ye ip₁ merkeze, ip₂ dışarı doğru çeker; K, O’dan 0,5 m uzaktadır.','T₁ − T₂ = mω²·(0,5) = 2 N'),A('ip₁ gerilmesi','İkinci denklemden T₁ bulunur.','T₁ = 4 + 2 = 6 N')],
 puf='Her cisim için kuvvetleri ayrı çiz ve merkeze doğru net kuvveti yaz.',sekil=SK)

# ===================== 18 · zor · looping =====================
r18=Fr(4,5); h18=3*r18; assert h18==Fr(12,5)
vt2=2*g*r18; assert g*h18==g*2*r18+vt2/2
for nm,vt2x,hh in [('2r',0,2*r18),('2,5r',g*r18,Fr(5,2)*r18),('3,5r',3*g*r18,Fr(7,2)*r18),('4r',2*g*r18,4*r18)]:
    pass
assert 2*r18+Fr(0)/2/g==Fr(8,5) and 2*r18+g*r18/2/g==2 and 2*r18+3*g*r18/2/g==Fr(14,5) and 2*r18+2*g*r18/g==Fr(16,5)
SK=FIG(r'''\draw[thick] (-.4,0) -- (7,0); \fill[gray!30] (-.4,0) rectangle (7,-.2);
\draw[very thick] (.3,2.6) .. controls (1.4,.5) .. (2.3,0);
\draw[very thick] (2.3,0) -- (3.2,0);
\draw[very thick] (3.2,0) arc[start angle=-90,end angle=270,radius=1.0] ; \draw[very thick] (3.2,0) -- (6.5,0);
\draw[thick,fill=gray!45] (.3,2.75) circle (.15); \node[right] at (.5,2.8) {A};
\draw[<->] (-.15,0) -- (-.15,2.6); \node[left] at (-.15,1.3) {$h$};
\fill (3.2,1.0) circle (.05); \draw[<->] (3.2,1.0) -- (4.2,1.0); \node[right] at (4.3,1.0) {$r=0{,}8$ m}; \node[above] at (3.2,2.05) {T};''')
q(18,4,'zor','Düşey çemberli ray (looping)','şekilli',*TP['du'],'Enerji korunumu ile tepe noktasındaki merkezcil kuvvet koşulunu birleştirerek bırakılma yüksekliğini bulur.',
 metin='Sürtünmesiz şekildeki rayın A noktasından serbest bırakılan cisim, yarıçapı şekilde verilen düşey çembersel halkanın en üst noktası T’den geçerken raya, ağırlığına eşit büyüklükte bir kuvvet uygulamaktadır.\n(g = 10 m/s²; cismin boyutları önemsizdir ve şekil ölçekli değildir.)\nBuna göre, A noktasının yerden yüksekliği h kaç m’dir?',
 dogru=Fr(12,5),yan=[(Fr(8,5),'Tepede N − mg = mv²/r yazıp v = 0 bulmuş: h = 2r = 1,6 m.','islem'),(2,'Merkezcil kuvvet eşitliğine ağırlığı katmamış: N = mv²/r → v² = gr ve h = 2r + r/2 = 2 m.','dikkat'),(Fr(14,5),'Tepkiyi 2mg alıp v² = 3gr bulmuş: h = 2r + 1,5r = 2,8 m.','islem'),(Fr(16,5),'Enerji eşitliğinde ½ katsayısını unutmuş: gh = 2gr + v² → h = 4r = 3,2 m.','islem')],
 istenen='A noktasının yerden yüksekliği h (m).',ip=['Tepe noktasında cisme etki eden kuvvetlerin yönünü belirle; sonra A ile T arasında enerjiyi karşılaştır.'],
 bilgi=[B_DUS],
 ad=[A('Tepe noktasında kuvvetler','Ray cisme aşağı yönde tepki uygular; merkez aşağıdadır.','N + mg = mv²/r'),A('Tepe süratini bul','N = mg verildiğinden 2mg = mv²/r.','v² = 2gr = 2 × 10 × 0,8 = 16'),A('Enerji korunumu','A’dan T’ye: potansiyel enerji kaybı = kinetik enerji + çıkılan yükseklik.','mgh = mg·2r + ½mv²'),A('h’yi bul','Değerleri yerine koy.','10h = 10 · 1,6 + 8 → h = 2,4 m')],
 puf='Tepede merkez hangi yöndedir ve hangi kuvvetler o yöndedir?',sekil=SK)

# ===================== 19 · zor · konik sarkaç, iki cisim =====================
m19=Fr(2,10); TK=m19*g/Fr(4,5); assert TK==Fr(5,2); cL=Fr(4,5)/2; TL=m19*g/cL; assert TL==5==2*TK
assert TK/2==Fr(5,4) and m19*g==2 and 4*TK==10
la=37; lb=degrees(math.acos(0.4)); lenK=2.0; lenL=4.0
kx_,ky_=lenK*sin(radians(la)),-lenK*cos(radians(la)); lx_,ly_=lenL*sin(radians(lb)),-lenL*cos(radians(lb))
SK=FIG(rf'''\fill[gray!35] (-.8,0) rectangle (4.6,.2); \draw[thick] (-.8,0) -- (4.6,0);
\fill (0.3,0) circle (.04); \fill (2.8,0) circle (.04);
\begin{{scope}}[shift={{(0.3,0)}}]
\draw[dashed] (0,0) -- (0,-2.6); \draw[thick] (0,0) -- ({kx_:.3f},{ky_:.3f}); \draw[thick,fill=gray!45] ({kx_:.3f},{ky_:.3f}) circle (.15);
\node[right] at ({kx_/2:.3f},{ky_/2+.1:.3f}) {{$\ell$}}; \draw (0,-.8) arc[start angle=-90,end angle=-53,radius=.8]; \node at (.6,-1.0) {{$37^\circ$}}; \node[below] at ({kx_:.3f},{ky_-.15:.3f}) {{K}};
\end{{scope}}
\begin{{scope}}[shift={{(2.8,0)}}]
\draw[dashed] (0,0) -- (0,-4.3); \draw[thick] (0,0) -- ({lx_:.3f},{ly_:.3f}); \draw[thick,fill=gray!45] ({lx_:.3f},{ly_:.3f}) circle (.15);
\node[left] at ({lx_/2:.3f},{ly_/2:.3f}) {{$2\ell$}}; \node[below] at ({lx_:.3f},{ly_-.15:.3f}) {{L}};
\end{{scope}}''')
q(19,5,'zor','Konik sarkaç, iki cisim','şekilli',*TP['ko'],'Aynı açısal hızla dönen farklı boydaki konik sarkaçlarda gerilmeyi ip boyu ve açıyla ilişkilendirir.',
 metin='Kütleleri 200 g olan özdeş K ve L cisimleri, ağırlıksız ipler ile aynı tavana şekildeki gibi bağlanmış ve aynı sabit açısal hızla yatay düzlemlerde düzgün çembersel hareket yapmaktadır. K’nin ipi düşeyle şekildeki açıyı yapmaktadır.\n(g = 10 m/s²; cos37° = 0,8)\nBuna göre, L’nin bağlı olduğu ipteki gerilme kuvveti kaç N’dur?',
 dogru=5,yan=[(Fr(5,4),'Gerilmeyi ip boyuyla ters orantılı sanmış: T_L = T_K ÷ 2 = 1,25 N.','dikkat'),(2,'İpin yalnız ağırlığı taşıdığını düşünüp T = mg = 2 N yazmış.','bilgi'),(Fr(5,2),'L için de K ile aynı gerilmeyi bulmuş (açıları aynı sanmış).','bilgi'),(10,'Gerilmeyi ip boyunun karesiyle orantılı sanmış: 4 · 2,5 = 10 N.','islem')],
 istenen='L cismini taşıyan ipteki gerilme kuvveti (N).',ip=['Her sarkaçta gerilmenin düşey ve yatay bileşenlerini ayrı yaz; ortak büyüklüğün hangisi olduğuna bak.'],
 bilgi=[B_MER,B('Konik sarkaç','ip düşeyle θ açısı yapıyorsa T cosθ = mg ve T sinθ = mω²r’dir; r = ℓ sinθ olduğundan gerilme T = mω²ℓ biçiminde de yazılır')],
 ad=[A('K’nin gerilmesi','K’de düşey denge.','T_K cos37° = mg → T_K = 2 ÷ 0,8 = 2,5 N'),A('Gerilmeyi ip boyuyla yaz','T = mω²ℓ olduğundan aynı m ve ω için gerilme ip boyuyla doğru orantılıdır.','T_L ÷ T_K = 2ℓ ÷ ℓ = 2'),A('L’nin gerilmesi','İki katı alınır.','T_L = 2 × 2,5 = 5 N'),A('Kontrol','L’nin açısı cosθ_L = mg/T_L ile uyumludur.','cosθ_L = 2 ÷ 5 = 0,4 (geçerli)')],
 puf='Yatay bileşeni yazarken yörünge yarıçapını r = ℓ sinθ ile ifade et.',sekil=SK)

# ===================== 20 · zor · T–v² grafiği, alt nokta =====================
m20=Fr(1,2); r20=Fr(4,5); sl20=m20/r20; assert sl20==Fr(5,8); T_A=sl20*16-m20*g; assert T_A==5
vA2=16; vB2=vA2+4*g*r20; T_B=m20*(g+vB2/r20); assert T_B==35 and T_B==T_A+6*m20*g
assert m20*g==5 and 6*m20*g==30 and T_A+2*m20*g==15
vB2x=vA2+2*g*r20; assert m20*(g+vB2x/r20)==25
assert m20*vB2/r20==30 and m20*(g+(vA2+6*g*r20)/r20)==45
SK=AX(pl([(8,0),(16,5),(24,10),(32,15)])+pl([(0,-5),(8,0)],'thick,vurgu,dashed'),32,-5,15,range(0,33,8),[-5,0,5,10,15],'$T$ (N)','$v^2$ (m$^2$/s$^2$)',h=5.0)
q(20,4,'zor','T–v² grafiği, düşey çember','grafik',*TP['du'],'Grafikten kütleyi ve üst noktadaki gerilmeyi okuyup enerji korunumuyla alt noktadaki gerilmeyi bulur.',
 metin='Ağırlıksız bir ipin ucuna bağlı bir cisim, düşey düzlemde hava direnci önemsenmeden çembersel hareket yapmaktadır (g = 10 m/s²). Cisim en üst noktadan geçerken ipteki gerilme kuvveti (T) ile cismin süratinin karesi (v²) arasındaki ilişki grafikte verilmiştir (kesikli çizgi grafiğin uzantısıdır).\nCisim en üst noktadan 4 m/s sürat ile geçtiğine göre, en alt noktadan geçerken ipteki gerilme kuvveti kaç N’dur?',
 dogru=35,yan=[(15,'Üstteki gerilmeye yalnız ağırlık farkını (2mg = 10 N) eklemiş: 5 + 10 = 15 N.','dikkat'),(25,'Yükseklik farkını r almış: v_B² = 16 + 2 · 10 · 0,8 = 32 ve T = 0,5 · (10 + 32 ÷ 0,8) = 25 N.','islem'),(30,'Alt noktada merkezcil kuvvete ağırlığı eklemeyi unutmuş: mv_B² ÷ r = 0,5 · 48 ÷ 0,8 = 30 N.','dikkat'),(45,'Yükseklik farkını 3r almış: v_B² = 16 + 6 · 10 · 0,8 = 64 ve T = 0,5 · (10 + 64 ÷ 0,8) = 45 N.','islem')],
 istenen='En alt noktadaki ip gerilmesi (N).',ip=['Grafikteki doğrunun v² = 0 değerindeki uzantısının neyi gösterdiğini düşün; sonra üst ve alt nokta arasında enerjiye bak.'],bilgi=[B_DUS],
 ad=[A('Kütleyi bul','v² = 0 için T = −mg olur; grafikte uzantı T ekseninin −5 N noktasını keser.','mg = 5 N → m = 0,5 kg'),A('Üst gerilmeyi oku','v² = 4² = 16 için grafikten T değeri okunur.','T_A = 5 N'),A('Üst sürat ve yarıçap','Üstte T + mg = mv²/r.','5 + 5 = 0,5 × 16 ÷ r → r = 0,8 m'),A('Alt süratı bul','Enerji korunumu, yükseklik farkı 2r.','v_B² = 16 + 4 · 10 · 0,8 = 48'),A('Alt gerilme','Altta T − mg = mv²/r.','T_B = 5 + 0,5 · 48 ÷ 0,8 = 35 N')],
 puf='Çemberin tepesinde ve dibinde gerilme farkı yalnız ağırlığa bağlıdır; farkı bulmak için kuvvet ve enerji eşitliklerini birleştir.',sekil=SK)

# ================= yaz =================
def bitir_af():
    for qq in P.ANA: qq['kardes']=None
    P.yaz(os.path.join(GD,'cembersel-1.json'),'/dev/null')
    tipler={}
    for c in KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=KK))['kartlar'].append(c['id'])
    json.dump(dict(konu=KONUAD,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2018–2025 Fizik (yalnız mantık), MEB 11. sınıf fizik müfredatı.',kartlar=KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar','afcembersel.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler))
bitir_af()
