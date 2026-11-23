"""AYT Fizik · İtme ve Momentum · 20 soruluk paket (3 kolay / 11 orta / 6 zor). Kardeş yok, ipucu 1.
Şekil verileri ve her cevap/çeldirici değeri Python'da (Fraction) hesaplanıp assert edilir; TikZ gövdeleri aynı verilerden üretilir."""
import sys,os,json,math
ADIR=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(ADIR,'..')
sys.path.insert(0,os.path.join(HV,'tyt-fiz')); sys.path.insert(0,HV)
import _hafif as H
from _hafif import *
from cizim import tikz_svg
from fractions import Fraction as Fr
H.KONU='İtme ve Momentum'
UK='afiz|İtme ve Momentum'
P=Parti('momentum','İtme ve Momentum',UK,ders='AYT Fizik',idon='aytfiz')
KY='ÖSYM 2018–2025 AYT Fizik (İtme ve Çizgisel Momentum: itme–momentum değişimi, esnek/esnek olmayan çarpışma, ayrılma; yalnız mantık) · 345 AYT Fizik · Bilgi Sarmal AYT Fizik denemeleri · MEB 11. sınıf'
g=10
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)
def dist(v,e): assert len({v,*[x[0] for x in e]})==len(e)+1,(v,e)
def sec(dogru,cands,hedef):
    r='ABCDE'.index(hedef); vs=[c[0] for c in cands]; assert dogru not in vs and len(set(vs))==len(vs),(dogru,vs)
    sm=sorted([c for c in cands if c[0]<dogru],key=lambda c:c[0]); lg=sorted([c for c in cands if c[0]>dogru],key=lambda c:c[0])
    assert len(sm)>=r and len(lg)>=4-r,(dogru,hedef,vs)
    return (sm[len(sm)-r:] if r else [])+lg[:4-r]
def alan(pts):
    s=Fr(0)
    for (x0,y0),(x1,y1) in zip(pts,pts[1:]): s+=Fr(x1-x0)*Fr(y0+y1)/2
    return s
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
ARR='-{Stealth[length=2mm,width=1.8mm]}'
def fig(body): return tikz_svg(HEAD+body+TAIL)
def zem(x0,x1,y=0,kaba=False):
    col='gray!70' if kaba else 'gray!30'
    return f'\\fill[{col}] ({x0},{y-.2}) rectangle ({x1},{y}); \\draw[thick] ({x0},{y}) -- ({x1},{y});'
def blok(cx,w,h,lab,y=0,fill='gray!25',fs='\\small'):
    return f'\\draw[thick,fill={fill}] ({cx-w/2:.3f},{y}) rectangle ({cx+w/2:.3f},{y+h}); \\node[font={fs}] at ({cx:.3f},{y+h/2:.3f}) {{{lab}}};'
def vk(x1,y1,x2,y2,lab='',pos='above',col='vurgu'):
    s=f'\\draw[{col},very thick,{ARR}] ({x1:.3f},{y1:.3f}) -- ({x2:.3f},{y2:.3f});'
    if lab: s+=f' \\node[{col}!70!black,{pos},inner sep=2pt] at ({(x1+x2)/2:.3f},{(y1+y2)/2:.3f}) {{{lab}}};'
    return s
def axis_opts(xl,yl,xmax,ymin,ymax,xt,yt,w='7cm',h='5cm'):
    return (f'\\begin{{axis}}[width={w},height={h},xmin=0,xmax={xmax},ymin={ymin},ymax={ymax},xtick={{{xt}}},ytick={{{yt}}},grid=both,major grid style={{gray!55,thin}},'
            f'tick label style={{font=\\scriptsize}},axis lines=middle,xlabel={{{xl}}},ylabel={{{yl}}},xlabel style={{font=\\small,at={{(ticklabel* cs:1)}},anchor=west}},ylabel style={{font=\\small,at={{(ticklabel* cs:1)}},anchor=south}}]')
SIR=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
def sirala(*s):
    assert [x for x in SIR if x in s]==list(s) and len(s)==5,s
    return list(s)

# ---------- bilgi kutuları (örnekler soruların sayılarından farklı) ----------
BP=B('Çizgisel momentum','p = m·v; vektörel bir niceliktir, yönü hızın yönündedir, birimi kg·m/s’dir. Zıt yönlü hızlar eksi işaretle yazılır. Örnek: 5 kg’lık cisim doğuya 3 m/s ile giderken p = 15 kg·m/s (doğu), batıya 3 m/s ile giderken p = −15 kg·m/s’dir')
BI=B('İtme ve momentum değişimi','İtme I = F·Δt = Δp = m·(v₂ − v₁) (birimi N·s). Kuvvet değişiyorsa itme, F–t grafiğinin altındaki işaretli alandır. Örnek: 6 N’luk sabit kuvvet 5 s etki ederse itme 30 N·s’dir')
BO=B('Ortalama kuvvet','F_ort = Δp ÷ Δt. Hız yön değiştiriyorsa Δp = m·(v₁ + v₂) olur (büyüklükler toplanır). Örnek: 2 kg’lık cisim 5 m/s ile gelip aynı büyüklükle geri dönüyorsa Δp = 20 kg·m/s; 0,1 s’de 200 N ortalama kuvvet uygulanır')
BK=B('Momentumun korunumu','Sisteme dışarıdan net kuvvet etki etmiyorsa (çarpışma süresince önemsiz ise) toplam momentum sabit kalır: Σp(önce) = Σp(sonra). Doğrultu ve yönler işaretle yazılır. Örnek: 5 kg ve 15 kg’lık cisimler 8 m/s ve 0 hızla gelip kenetlenirse ortak hız (5 × 8) ÷ 20 = 2 m/s’dir')
BE=B('Esnek çarpışma','Momentum ve kinetik enerji birlikte korunur; yaklaşma hızı ayrılma hızına eşittir: v₁ − v₂ = v₂′ − v₁′. Eşit kütleli cisimler merkezî esnek çarpışmada hızlarını değiş tokuş eder. Örnek: 4 kg’lık cisim 6 m/s ile durgun özdeş cisme çarparsa durur, diğeri 6 m/s ile gider')
BY=B('Esnek olmayan çarpışma','Cisimler birlikte hareket ediyorsa (kenetlenme) yalnız momentum korunur; kinetik enerjinin bir kısmı ısı ve sese dönüşür, kinetik enerji azalır. Örnek: 10 kg ve 30 kg’lık cisimler 4 m/s ve 0 hızla kenetlenirse ortak hız 1 m/s olur; enerji 80 J’den 20 J’e düşer')
BPA=B('Patlama ve ayrılma','Durgun bir cisim iç kuvvetlerle parçalara ayrılırsa toplam momentum sıfır kalır; parçaların momentum vektörlerinin toplamı sıfırdır. Kinetik enerji artar (depolu enerji açığa çıkar). Örnek: durgun 5 kg’lık cisim 2 kg ve 3 kg’lık parçalara ayrılıp 2 kg’lık parça 6 m/s ile giderse 3 kg’lık parça ters yönde 4 m/s ile gider')
BEK=B('Momentum ve kinetik enerji','Ek = ½mv² = p² ÷ (2m) olduğundan p = √(2m·Ek) ve v = √(2Ek ÷ m) yazılır. Aynı Ek için kütlesi büyük cismin momentumu büyük, hızı küçüktür. Örnek: 9 kg ve 1 kg’lık cisimlerin kinetik enerjileri eşitse momentumları oranı 3 : 1’dir')
BVE=B('Vektörel toplam','Birbirine dik doğrultulu momentumlar vektör olarak toplanır; bileşke büyüklük p = √(p₁² + p₂²) bulunur (3–4–5 ve 5–12–13 gibi). Örnek: 6 ve 8 kg·m/s’lik dik momentumların bileşkesi 10 kg·m/s’dir')
BG=B('Grafik yorumu','p–t grafiğinin eğimi net kuvveti (F = Δp ÷ Δt), v–t grafiğinin eğimi ivmeyi, x–t grafiğinin eğimi hızı verir. Örnek: p–t grafiğinde 3 s’de 12 kg·m/s artış gösteren doğru 4 N’luk net kuvvet demektir')
BMK=B('Kütle merkezi','Sisteme dış kuvvet etki etmiyorsa ve ilk anda durgunsa kütle merkezi yer değiştirmez: Σ m·Δx = 0. Örnek: 30 kg ve 10 kg’lık iki cisim ip üzerinden birbirine yaklaşırsa 10 kg’lık cismin yer değiştirmesi 30 kg’lık cismin üç katı olur')
BAT=B('Yatay atış ve eğik atış','Hava direnci yoksa yatay hız sabittir, düşey hareket g ile ivmelenir. Tepe noktasında yalnız yatay hız vardır. Yükseklik h = ½gt² ile süre bulunur. Örnek: 45 m yükseklikten yatay atılan cisim 3 s sonra yere düşer')
BSA=B('Kinetik sürtünme ve yavaşlama','Kinetik sürtünme kuvveti f = μ·N, yatay zeminde ivme büyüklüğü a = μ·g’dir; durma yolu için v² = 2·a·d yazılır. Örnek: μ = 0,5 için a = 5 m/s² ve 10 m/s’lik hızla giden cisim 10 m’de durur')
BYU=B('Yükseklik ve hız','Sürtünmesiz rayda mekanik enerji korunur: m·g·h = ½mv². Böylece v = √(2gh) ve h = v² ÷ (2g) olur. Örnek: 20 m/s’lik hızla yükselen cisim en çok 20 m yüksekliğe çıkar (g = 10 m/s²)')

# ---------- kartlar ----------
kartla('K-AFMOM-01','F–t grafiğinden itme ve hız','F–t grafiğinin altındaki alan itmedir; itme momentum değişimine eşittir, durgun cisimde hız = alan ÷ kütle.','Üçgen alanında ½ çarpanını unutmak; itmeyi hız sanmak; grafiğin tepe değerini hız sanmak.','kolay','grafik',3,'mo-ft','F–t grafiği ve itme')
kartla('K-AFMOM-02','Duvardan geri dönen top','Hız yön değiştirince Δp = m(v₁ + v₂); ortalama kuvvet Δp ÷ Δt.','Hız farkını (v₁ − v₂) almak; geri dönüşü saymamak; kütleyi unutmak.','kolay','şekilli',3,'mo-itme','İtme, momentum değişimi ve ortalama kuvvet')
kartla('K-AFMOM-03','Eşit kinetik enerjili cisimlerin momentumu','p = √(2mEk): eşit Ek’de momentum kütlenin karekökü ile, hız kütlenin karekökü ile ters orantılı değişir.','Eşit Ek’yi eşit momentum sanmak; kütle oranını karekök almadan kullanmak.','kolay','öncüllü',3,'mo-kinetik','Momentum ile kinetik enerji ilişkisi')
kartla('K-AFMOM-04','Merkezî esnek çarpışma (sayısal)','Momentum korunumu ve yaklaşma hızı = ayrılma hızı birlikte kullanılır; hızlar işaretle yazılır.','Eşit kütleli özel durumu (hız değiş tokuşu) genellemek; yönleri işaretsiz toplamak.','orta','şekilli',4,'mo-esnek','Merkezî esnek çarpışma')
kartla('K-AFMOM-05','Kenetlenme ve sürtünmeli yavaşlama','Çarpışmada momentum korunur (kinetik enerji korunmaz); ortak hızla sürtünmeli yolda durma yolu hesaplanır.','Çarpışmada kinetik enerjiyi korumak; ortak hızı yanlış kütleyle bulmak; durma yolunda ½ çarpanı.','orta','şekilli',5,'mo-yapisik','Kenetlenme ve sürtünmeli yavaşlama')
kartla('K-AFMOM-06','Patlamada parçaların nicelikleri','Ayrılan parçaların momentum, hız ve kinetik enerjileri kütleleriyle ilişkilendirilir.','Momentum ile kinetik enerjiyi karıştırmak.','orta','öncüllü',4,'mo-patlama','Ayrılma ve patlama')
kartla('K-AFMOM-07','İki boyutlu patlama','Parçaların momentum vektörleri arasındaki ilişki toplam momentumdan yararlanılarak kurulur.','Momentumları skaler toplamak; kütleyi hesaba katmamak.','orta','şekilli',4,'mo-patlama','Ayrılma ve patlama')
kartla('K-AFMOM-08','Delip geçen ok ve sarkaç','Momentum korunumu ile torbanın hızı, ardından enerji korunumu ile yükseklik bulunur.','Çarpışma ile yükselmede korunan büyüklükleri karıştırmak; okun çıkış momentumunu yanlış işaretlemek.','zor','şekilli',5,'mo-balistik','Balistik sarkaç')
kartla('K-AFMOM-09','v–t grafiğinden çarpışma yorumu','Çarpışma anındaki hız sıçramalarından momentum korunumu ile kütle oranı, kinetik enerji karşılaştırmasıyla çarpışma türü belirlenir.','Kütle oranını ters yazmak; enerji kaybını gözden kaçırmak.','orta','grafik',5,'mo-grafik','Grafik yorumu ve çarpışma türü')
kartla('K-AFMOM-10','p–t grafiği yorumu','p–t grafiğinin eğimi ve işareti yorumlanır.','Eğim ile p değerini karıştırmak; işaretin anlamını göz ardı etmek.','orta','grafik',4,'mo-grafik','Grafik yorumu ve çarpışma türü')
kartla('K-AFMOM-11','Dik doğrultulu çarpışmada kenetlenme','Momentum vektörel toplanır; bileşke momentum toplam kütleye bölünür.','Momentumları skaler toplamak; yalnız bir cismin kütlesine bölmek.','orta','şekilli',4,'mo-yapisik','Kenetlenme ve sürtünmeli yavaşlama')
kartla('K-AFMOM-12','Eşit bölmeli zeminde kütle oranı','Konum değişimlerinden hızlar okunur; kenetlenmede momentum korunumundan kütle oranı bulunur.','Hızları yönsüz toplamak; kütle oranını ters yazmak.','orta','şekilli',5,'mo-yapisik','Kenetlenme ve sürtünmeli yavaşlama')
kartla('K-AFMOM-13','Yayla ayrılan cisimler','Ayrılan cisimlerin hızları momentum korunumundan, yayda depolanan enerji toplam kinetik enerjiden bulunur.','Yalnız bir cismin enerjisini yazmak; ½ çarpanını unutmak; iki cismi aynı hızda almak.','orta','şekilli',4,'mo-patlama','Ayrılma ve patlama')
kartla('K-AFMOM-14','İşaretli alanlı F–t grafiği','İtme işaretli alandır; başlangıç momentumu işaretiyle eklenir.','Negatif alanı atlamak ya da pozitif saymak; ilk hızın yönünü yok saymak.','orta','grafik',5,'mo-ft','F–t grafiği ve itme')
kartla('K-AFMOM-15','Eğik atışın tepesinde patlama','Tepe noktasında hız yataydır; patlamada yatay momentum korunur; parçaların sonraki hareketi yatay atış gibidir.','Patlamadan sonra hızı değişmemiş saymak; yükseklik ve süreyi karıştırmak.','zor','şekilli',6,'mo-patlama','Ayrılma ve patlama')
kartla('K-AFMOM-16','Yere çarpıp yükselen top','Hızlar enerji korunumundan bulunur; zeminin kuvveti Δp ÷ Δt ile ağırlığın toplamıdır.','Ağırlığı unutmak; hız farkı almak; geri dönüş hızını eşit sanmak.','orta','şekilli',5,'mo-itme','İtme, momentum değişimi ve ortalama kuvvet')
kartla('K-AFMOM-17','Düşey boşalan kum','Yatay doğrultuda dış kuvvet bulunmayan sistemde hangi niceliklerin korunduğu belirlenir.','Momentum ve enerji korunumunu karıştırmak; kumun kütlesini unutmak.','orta','öncüllü',4,'mo-yapisik','Kenetlenme ve sürtünmeli yavaşlama')
kartla('K-AFMOM-18','Esnek çarpışma ve rampa','Rampada enerji korunumuyla çarpışma hızı, esnek çarpışmayla L’nin hızı, yine enerji korunumuyla yükseklik bulunur.','Eşit kütle formülünü uygulamak; kütleleri formülde ters yazmak.','zor','şekilli',6,'mo-esnek','Merkezî esnek çarpışma')
kartla('K-AFMOM-19','Kayıkta yürüyen kişi','Dış kuvvet yokken toplam momentum sıfır kalır; göreli hız yere göre hızlara ayrılır.','Göreli hızı yere göre hız sanmak; süreyi yere göre hızla hesaplamak.','zor','öncüllü',5,'mo-kutlemerkezi','Kütle merkezi ve momentum')
kartla('K-AFMOM-20','x–t grafiğinden esnek çarpışma','x–t eğimleri hızları verir; momentum ve enerji karşılaştırmasıyla kütle oranı ve çarpışma türü belirlenir.','Esnek çarpışmada enerji kaybı aramak; momentum değişimlerini farklı sanmak.','zor','grafik',6,'mo-grafik','Grafik yorumu ve çarpışma türü')

# ================= 01 kolay · F–t grafiği (üçgen) =================
m1=4; pts1=[(0,0),(2,12),(6,0)]; I1=alan(pts1); v1=I1/m1
assert I1==36 and v1==9
e1=[(Fr(9,2),'Hızı I ÷ (2m) = 36 ÷ 8 diye hesaplamış; itme Δp = m·Δv olduğundan hız I ÷ m ile bulunur.','islem'),
    (12,'Grafikteki en büyük kuvvet değerini (12) hız sanmış.','dikkat'),
    (18,'Üçgenin alanını ½ çarpanı olmadan almış (6 · 12 = 72 N·s): 72 ÷ 4 = 18 m/s.','islem'),
    (36,'İtmeyi (36 N·s) doğrudan hız olarak yazmış; kütleye bölmemiş.','bilgi')]
assert Fr(36,8)==Fr(9,2) and 72//4==18
for c in e1: dist(v1,e1)
SK=fig(axis_opts('$t$ (s)','$F$ (N)',6.6,0,14,'0,1,2,3,4,5,6','0,4,8,12')+
 '\n\\addplot[thick,vurgu,mark=*,mark size=1.5pt] coordinates {'+' '.join(f'({a},{b})' for a,b in pts1)+'};\n\\end{axis}')
q('0001',tipId='mo-ft',tip='F–t grafiği ve itme',z='kolay',alt='İtme',kaz='Kuvvet–zaman grafiğinin altındaki alandan itmeyi, itmeden de cismin hızını bulur.',
 kart='K-AFMOM-01 (F–t grafiği, üçgen alan) · m = 4 kg, tepe değeri 12 N, süre 6 s',kalip='grafik',
 metin='Sürtünmesiz yatay düzlemde durmakta olan 4 kg kütleli bir cisme, yatay doğrultulu bir kuvvet uygulanıyor. Kuvvetin büyüklüğünün zamanla değişimi şekildeki grafikte verilmiştir.\nBuna göre, cismin t = 6 s anındaki hızının büyüklüğü kaç m/s’dir?',
 dogru=v1,yan=sec(v1,e1,'B'),istenen='Cismin t = 6 s anındaki hızının büyüklüğü (m/s).',ip=['Kuvvetin cisme uyguladığı itmeyi grafikle ilişkilendir; itme momentumdaki değişimi verir.'],bilgi=[BI,BP],sekil=SK,
 ad=[A('İtmeyi grafikten bul','F–t grafiğinin altındaki alan itmeye eşittir; grafik bir üçgendir.','I = ½ · 6 · 12 = 36 N·s'),
     A('Momentum değişimine eşitle','İtme momentumdaki değişime eşittir; cisim durgun başlamıştır.','I = m·v − 0 → 36 = 4 · v'),
     A('Hızı hesapla','Denklemi hız için çöz.','v = 36 ÷ 4 = 9 m/s')],
 puf='F–t grafiğinde alan itmedir; durgun cisimde hız = alan ÷ kütle.')

# ================= 02 kolay · duvardan geri dönen top =================
m2=Fr(1,2); va,vb=8,4; dt2=Fr(2,100)
dp2=m2*(va+vb); F2=dp2/dt2
assert dp2==6 and F2==300
e2=[(m2*(va-vb)/dt2,'Momentum değişimini hız farkıyla (8 − 4 = 4 m/s) hesaplamış: Δp = 0,5 · 4 = 2 kg·m/s, F = 2 ÷ 0,02 = 100 N.','islem'),
    (m2*va/dt2,'Yalnız çarpmadan önceki momentumu (0,5 · 8 = 4) kullanmış: F = 4 ÷ 0,02 = 200 N; geri dönüşteki momentumu katmamış.','dikkat'),
    (m2*(va+va)/dt2,'Geri dönüş hızını da 8 m/s almış: Δp = 0,5 · 16 = 8 kg·m/s, F = 8 ÷ 0,02 = 400 N.','dikkat'),
    ((va+vb)/dt2,'Kütleyi hesaba katmamış: Δv = 12 m/s, F = 12 ÷ 0,02 = 600 N.','bilgi')]
assert [c[0] for c in e2]==[100,200,400,600]
u=.28
def duvar(y0): return f'\\fill[gray!30] (8.4,{y0}) rectangle (8.8,{y0+1.4}); \\draw[very thick] (8.4,{y0}) -- (8.4,{y0+1.4});'
body=zem(-.2,8.8,0)+'\n'+duvar(0)+'\n'+zem(-.2,8.8,2.6)+'\n'+duvar(2.6)+'\n'
body+='\\fill[gray!35] (1.0,2.88) circle (.28); \\draw[thick] (1.0,2.88) circle (.28); \\node[font=\\small] at (1.0,3.6) {0,5 kg};\n'+vk(1.35,2.88,1.35+va*u,2.88,'8 m/s','above')+'\n'
body+='\\node[font=\\small] at (4.6,3.6) {çarpışmadan önce};\n'
body+='\\fill[gray!35] (7.7,.28) circle (.28); \\draw[thick] (7.7,.28) circle (.28);\n'+vk(7.7-.35,.28,7.7-.35-vb*u,.28,'4 m/s','above','blue')+'\n'
body+='\\node[font=\\small] at (3.2,.95) {çarpışmadan sonra};\n'
SK=fig(body)
q('0002',tipId='mo-itme',tip='İtme, momentum değişimi ve ortalama kuvvet',z='kolay',alt='İtme',kaz='Yön değiştiren bir cismin momentum değişimini ve duvarın uyguladığı ortalama kuvveti hesaplar.',
 kart='K-AFMOM-02 (duvardan dönen top) · m = 0,5 kg, 8 m/s ve 4 m/s, Δt = 0,02 s',kalip='şekilli',
 metin='Kütlesi 0,5 kg olan bir top, sürtünmesiz yatay zeminde duvara dik olarak çarpıp geri dönüyor. Topun hız büyüklükleri çarpışmadan hemen önce ve hemen sonra şekilde gösterilmiştir. Top, duvarla 0,02 s süre etkileşmektedir.\n(Etkileşme süresince topa etki eden diğer kuvvetler önemsizdir.)\nBuna göre, duvarın topa uyguladığı ortalama kuvvetin büyüklüğü kaç N’dur?',
 dogru=F2,yan=sec(F2,e2,'C'),istenen='Duvarın topa uyguladığı ortalama kuvvetin büyüklüğü (N).',ip=['Top geri döndüğünde momentum değişiminin hangi işaretlerle hesaplanması gerektiğini düşün.'],bilgi=[BO,BP],sekil=SK,
 ad=[A('Yönleri belirle','Geliş yönünü + al; geri dönüşte hız ters yönlüdür.','v₁ = +8 m/s, v₂ = −4 m/s'),
     A('Momentum değişimini bul','Δp = m·(v₂ − v₁).','Δp = 0,5 · (−4 − 8) = −6 kg·m/s'),
     A('Ortalama kuvveti yaz','İtme = F·Δt ve itme momentum değişimine eşittir.','F = 6 ÷ 0,02 = 300 N')],
 puf='Yön değiştiren cismin momentum değişiminde büyüklükler toplanır.')

# ================= 03 kolay · eşit kinetik enerjili cisimler (öncüllü) =================
mK,mL=1,4; # E eşit
import math as _m
vr=Fr(_m.isqrt(mL),_m.isqrt(mK)); pr=Fr(_m.isqrt(mL),_m.isqrt(mK))
assert _m.isqrt(mL)**2==mL and vr==2 and pr==2          # vK/vL = √(mL/mK) = 2 ; pL/pK = √(mL/mK) = 2
E_=Fr(8); vK=_m.sqrt(2*E_/mK); vL=_m.sqrt(2*E_/mL); assert abs(vK/vL-2)<1e-12 and abs(mL*vL/(mK*vK)-2)<1e-12
tr={'I':True,'II':True,'III':False}
u=.45
body=zem(-.3,8.3)+'\n'
body+=blok(1.6,.8,.8,'K')+'\n'+blok(5.6,1.6,.8,'L')+'\n'
body+=vk(2.05,.4,3.05,.4,'$\\vec v_K$','above')+'\n'+vk(6.5,.4,7.5,.4,'$\\vec v_L$','above')+'\n'
body+='\\node[font=\\small] at (1.6,1.3) {$m$}; \\node[font=\\small] at (5.6,1.3) {$4m$};\n'
SK=fig(body)
sir=sirala('Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III')
q('0003',tipId='mo-kinetik',tip='Momentum ile kinetik enerji ilişkisi',z='kolay',alt='Çizgisel Momentum',kaz='Eşit kinetik enerjili cisimlerin hız ve momentum büyüklüklerini kütlelerine göre karşılaştırır.',
 kart='K-AFMOM-03 (p = √(2mEk)) · kütleler m ve 4m, Ek eşit',kalip='öncüllü',
 metin='Sürtünmesiz yatay düzlemde aynı doğrultuda hareket eden K ve L cisimlerinin kütleleri sırasıyla m ve 4m’dir. Cisimlerin kinetik enerjileri birbirine eşittir.\nBuna göre,\nI. K’nin hızının büyüklüğü, L’ninkinin 2 katıdır.\nII. L’nin momentumunun büyüklüğü, K’ninkinin 2 katıdır.\nIII. K ve L’nin momentumlarının büyüklükleri eşittir.\nyargılarından hangileri doğrudur?',
 dogru='I ve II',yan=[('Yalnız I','II’nin de doğru olduğunu görmemiş: p = √(2mEk) olduğundan kütlesi 4 kat olan L’nin momentumu 2 kat büyüktür.','bilgi'),
  ('Yalnız II','I’in de doğru olduğunu görmemiş: v = √(2Ek ÷ m) olduğundan kütlesi küçük olan K’nin hızı L’ninkinin 2 katıdır.','bilgi'),
  ('Yalnız III','Eşit kinetik enerjiyi eşit momentum sanmış; Ek = p² ÷ 2m olduğundan kütleleri farklı cisimlerin momentumları farklıdır.','bilgi'),
  ('I ve III','III’ü doğru sanmış: Ek eşit olsa da momentum kütlenin karekökü ile orantılı olduğundan momentumlar eşit değildir.','bilgi')],sira=sir,
 istenen='Doğru olan yargılar.',ip=['Kinetik enerjiyi momentum cinsinden yazıp eşit enerjili iki cismi karşılaştır.'],bilgi=[BEK,BP],sekil=SK,
 ad=[A('Ek’yi hız cinsinden yaz','Ek eşitliğinden hız oranı bulunur.','½·m·vK² = ½·4m·vL² → vK = 2·vL → I doğru'),
     A('Ek’yi momentum cinsinden yaz','Ek = p² ÷ 2m olduğundan p² ∝ m.','pL² ÷ pK² = 4 → pL = 2·pK → II doğru'),
     A('III’ü değerlendir','Momentumlar eşit değildir.','pK ≠ pL → III yanlış'),
     A('Sonucu yaz','Doğru olanlar I ve II’dir.','I ve II')],
 puf='Eşit kinetik enerjide kütlesi büyük cismin momentumu büyük, hızı küçüktür.')

# ================= 04 orta · merkezî esnek çarpışma (sayısal) =================
mK4,vK4,mL4,vL4=3,5,1,-3
vK4p=Fr((mK4-mL4)*vK4+2*mL4*vL4,mK4+mL4); vL4p=Fr((mL4-mK4)*vL4+2*mK4*vK4,mK4+mL4)
assert (vK4p,vL4p)==(1,9) and mK4*vK4+mL4*vL4==mK4*vK4p+mL4*vL4p and Fr(1,2)*(mK4*vK4**2+mL4*vL4**2)==Fr(1,2)*(mK4*vK4p**2+mL4*vL4p**2) and vK4-vL4==vL4p-vK4p
e4=[(1,'K’nin çarpışma sonrası hızını (1 m/s) L’nin hızı sanmış.','dikkat'),
    (3,'L’nin hızının büyüklüğünün değişmediğini düşünmüş; esnek çarpışmada hızlar değişir.','bilgi'),
    (5,'Eşit kütleli cisimlerdeki hız değiş tokuşunu uygulamış: L, K’nin ilk hızını (5 m/s) almış sanmış.','bilgi'),
    (8,'Yaklaşma hızını (5 + 3 = 8 m/s) L’nin hızı sanmış; momentum korunumunu kullanmamış.','islem')]
u=.3
body=zem(-.3,8.3)+'\n'+blok(1.2,1.0,.8,'3 kg')+'\n'+blok(6.4,.7,.8,'1 kg')+'\n'
body+=vk(1.7,.4,1.7+vK4*u,.4,'5 m/s','above')+'\n'+vk(6.05,.4,6.05+vL4*u,.4,'3 m/s','above','blue')+'\n'
body+='\\node[font=\\small] at (1.2,1.25) {K}; \\node[font=\\small] at (6.4,1.25) {L};\n'
SK=fig(body)
q('0004',tipId='mo-esnek',tip='Merkezî esnek çarpışma',z='orta',alt='Esnek Çarpışma',kaz='Merkezî esnek çarpışmada momentum korunumu ve yaklaşma–ayrılma hızı eşitliğiyle çarpışma sonrası hızları bulur.',
 kart='K-AFMOM-04 (esnek, zıt yönlü) · 3 kg · 5 m/s ve 1 kg · 3 m/s',kalip='şekilli',
 metin='Sürtünmesiz yatay düzlemde, aynı doğrultuda ve zıt yönlerde hareket eden K ve L cisimlerinin kütleleri ve hız büyüklükleri şekilde verilmiştir. Cisimler merkezî ve esnek çarpışma yapıyor.\nBuna göre, çarpışmadan hemen sonra L cisminin hızının büyüklüğü kaç m/s’dir?',
 dogru=vL4p,yan=sec(vL4p,e4,'E'),istenen='Çarpışmadan hemen sonra L’nin hızının büyüklüğü (m/s).',ip=['Esnek çarpışmada korunan iki büyüklüğü yaz; hızları aynı yöne göre işaretle.'],bilgi=[BE,BK],sekil=SK,
 ad=[A('Yönleri işaretle','K’nin yönünü + al; L zıt yönlüdür.','vK = +5, vL = −3 m/s'),
     A('Momentum korunumu','Toplam momentum çarpışmadan önce ve sonra aynıdır.','3 · 5 + 1 · (−3) = 3·vK′ + vL′ → 12 = 3·vK′ + vL′'),
     A('Esneklik koşulu','Yaklaşma hızı ayrılma hızına eşittir.','5 − (−3) = vL′ − vK′ → vL′ − vK′ = 8'),
     A('Denklemleri çöz','İki denklemi taraf tarafa topla.','4·vK′ = 4 → vK′ = 1 m/s ve vL′ = 9 m/s')],
 puf='Esnek çarpışmada iki denklem vardır: momentum korunumu ve yaklaşma hızı = ayrılma hızı.')

# ================= 05 zor · kenetlenme + sürtünmeli bölge =================
mK5,vK5,mL5,mu5=2,12,4,Fr(2,5)
v5=Fr(mK5*vK5,mK5+mL5); a5=mu5*g; d5=v5**2/(2*a5)
assert v5==4 and a5==4 and d5==2
e5=[(v5**2/a5,'Yavaşlamada ½ çarpanını unutmuş: d = v² ÷ (μg) = 16 ÷ 4 = 4 m.','islem'),
    (Fr((mK5*vK5)**2,mL5**2)/(2*a5),'Momentumu (24) yalnız L’nin kütlesine (4 kg) bölüp ortak hızı 6 m/s bulmuş: d = 36 ÷ 8 = 4,5 m.','bilgi'),
    (Fr(1,2)*mK5*vK5**2/(mu5*(mK5+mL5)*g),'Çarpışmada kinetik enerji korunur sanıp 144 J’ü sürtünme işine eşitlemiş: 144 = 24·d → d = 6 m.','bilgi'),
    (Fr(vK5**2,2)/a5,'Çarpışma sonrası hızı K’nin ilk hızı (12 m/s) sanmış: d = 144 ÷ 8 = 18 m.','dikkat')]
assert [c[0] for c in e5]==[4,Fr(9,2),6,18]
u=.2
body=zem(-.3,5.6)+'\n'+zem(5.6,9.2,kaba=True)+'\n'
body+=blok(1.0,.8,.7,'K')+blok(3.8,1.1,.7,'L')+'\n'+vk(1.4,.35,1.4+vK5*u*.7,.35,'12 m/s','above')+'\n'
body+='\\node[font=\\small] at (1.0,1.05) {2 kg}; \\node[font=\\small] at (3.8,1.05) {4 kg};\n'
body+='\\node[font=\\small,align=center] at (7.4,1.1) {sürtünmeli bölge\\\\$\\mu_k=0{,}4$}; \\node[font=\\small] at (2.6,-.55) {sürtünmesiz bölge}; \\draw[dashed] (5.6,0) -- (5.6,.7);\n'
SK=fig(body)
q('0005',tipId='mo-yapisik',tip='Kenetlenme ve sürtünmeli yavaşlama',z='orta',alt='Esnek Olmayan Çarpışma',kaz='Esnek olmayan çarpışmadan sonraki ortak hızı momentum korunumuyla, durma yolunu sürtünme ivmesiyle bulur.',
 kart='K-AFMOM-05 (kenetlenme + sürtünme) · 2 kg · 12 m/s, 4 kg, μ = 0,4',kalip='şekilli',
 metin='Şekildeki düzenekte yatay zeminin sol bölümü sürtünmesiz, sağ bölümü kinetik sürtünme katsayısı 0,4 olan sürtünmeli bölgedir. 2 kg kütleli K cismi 12 m/s hızla, durmakta olan 4 kg kütleli L cismine çarpıp ona kenetleniyor ve birlikte sürtünmeli bölgeye giriyor.\n(g = 10 m/s²; çarpışma sürtünmesiz bölgede gerçekleşmektedir.)\nBuna göre, cisimler sürtünmeli bölgede durana kadar kaç m yol alır?',
 dogru=d5,yan=sec(d5,e5,'A'),istenen='Cisimlerin sürtünmeli bölgede aldığı yol (m).',ip=['Çarpışma sırasında hangi büyüklüğün korunduğunu belirleyip kenetlenmiş cisimlerin hızını önce bul.'],bilgi=[BY,BSA],sekil=SK,
 ad=[A('Ortak hızı bul','Kenetlenmede momentum korunur.','2 · 12 = (2 + 4) · v → v = 4 m/s'),
     A('Yavaşlamayı bul','Sürtünme kuvveti toplam kütleye etki eder; a = μ·g.','a = 0,4 · 10 = 4 m/s²'),
     A('Durma yolunu yaz','Hız–yol bağıntısı ya da iş–enerji teoremi kullanılır.','0 = 4² − 2 · 4 · d'),
     A('Yolu hesapla','Denklemi d için çöz.','d = 16 ÷ 8 = 2 m')],
 puf='Çarpışma sırasında momentum, sürtünmeli yolda ise iş–enerji ilişkisi kullanılır; kinetik enerji çarpışmada korunmaz.')

# ================= 06 orta · patlama (öncüllü) =================
mK6,mL6=3,1; vK6,vL6=1,3; assert mK6*vK6==mL6*vL6
EK6=Fr(1,2)*mK6*vK6**2; EL6=Fr(1,2)*mL6*vL6**2; assert EL6==3*EK6
u=.5
yy=0
body=zem(-.3,9.2,y=2.8)+'\n'+blok(1.6,1.6,.8,'$4m$',y=2.8)+'\n\\node[font=\\small] at (5.0,3.2) {patlamadan önce (durgun)};\n'
body+=zem(-.3,9.2,y=yy)+'\n'+blok(3.6,1.2,.8,'$3m$',y=yy)+'\n'+blok(6.6,.6,.8,'$m$',y=yy)+'\n'
body+=vk(3.0,yy+.4,2.0,yy+.4,'','above')+'\n'+vk(6.9,yy+.4,7.9,yy+.4,'','above','blue')+'\n'
body+=f'\\node[font=\\small] at (2.1,{yy+.75}) {{$\\vec v_K$}}; \\node[font=\\small] at (7.9,{yy+.75}) {{$\\vec v_L$}};\n'
body+=f'\\node[font=\\small] at (3.6,{yy+1.15}) {{K}}; \\node[font=\\small] at (6.6,{yy+1.15}) {{L}}; \\node[font=\\small] at (5.0,{yy+1.75}) {{patlamadan hemen sonra}};\n'
SK=fig(body)
sir=sirala('Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III')
q('0006',tipId='mo-patlama',tip='Ayrılma ve patlama',z='orta',alt='Patlama ve Ayrılma',kaz='Durgun bir cismin iç kuvvetlerle ayrılmasında parçaların momentum, hız ve kinetik enerjilerini karşılaştırır.',
 kart='K-AFMOM-06 (patlama, nitel) · 4m → 3m ve m, zıt yönlü ayrılma',kalip='öncüllü',
 metin='Sürtünmesiz yatay zeminde durmakta olan 4m kütleli bir cisim, içindeki sıkıştırılmış yayın açığa çıkması sonucu 3m kütleli K ve m kütleli L parçalarına ayrılıyor. Parçalar şekildeki gibi zıt yönlerde hareket etmektedir.\nBuna göre, ayrılmadan hemen sonra,\nI. K ve L’nin momentumlarının büyüklükleri eşittir.\nII. K ve L’nin kinetik enerjileri eşittir.\nIII. K’nin kinetik enerjisi, L’ninkinin 3 katıdır.\nyargılarından hangileri doğrudur?',
 dogru='Yalnız I',yan=[('Yalnız II','Momentum büyüklüklerinin eşit olduğunu fark etmemiş; kinetik enerjileri de eşit sanmış, oysa Ek = p² ÷ 2m kütleyle ters orantılıdır.','bilgi'),
  ('Yalnız III','Kütlesi büyük olan parçanın enerjisinin de büyük olacağını düşünmüş; momentumlar eşitken kütlesi küçük olan L’nin enerjisi 3 kat büyüktür.','bilgi'),
  ('I ve II','I’i doğru bulmuş, ancak kinetik enerjilerin de eşit olacağını sanmış; momentum eşitliği enerji eşitliği değildir.','bilgi'),
  ('I ve III','I’i doğru bulmuş, III’te oranı ters yazmış: Ek ∝ 1 ÷ m olduğundan K’nin enerjisi L’ninkinin 1/3’üdür.','islem')],sira=sir,
 istenen='Doğru olan yargılar.',ip=['Ayrılma öncesi toplam momentumun değerini düşün; ardından kinetik enerjiyi momentum cinsinden yaz.'],bilgi=[BPA,BEK],sekil=SK,
 ad=[A('Momentumları karşılaştır','Cisim durgun olduğundan toplam momentum sıfırdır; parçaların momentumları eşit büyüklükte, zıt yönlüdür.','pK = pL → I doğru'),
     A('Hızları bul','p = m·v olduğundan kütle büyüdükçe hız küçülür.','3m · vK = m · vL → vL = 3·vK'),
     A('Kinetik enerjileri karşılaştır','Ek = p² ÷ 2m ve p eşittir.','EK ÷ EL = m ÷ 3m = 1/3 → II ve III yanlış'),
     A('Sonucu yaz','Yalnız I doğrudur.','Yalnız I')],
 puf='Ayrılmada momentum büyüklükleri eşit, kinetik enerjiler kütleyle ters orantılıdır.')

# ================= 07 orta · iki boyutlu patlama =================
mKa,vKa,mLa,vLa,mMa=1,5,2,6,1
px,py=mKa*vKa,mLa*vLa; pM=math.hypot(px,py); vM=Fr(int(pM),mMa); assert pM==13 and mKa+mLa+mMa==4 and vM==13
e7=[(Fr(py-px,mMa),'Momentumları çıkarmış: (12 − 5) ÷ 1 = 7 m/s; dik doğrultulu momentumlar vektörel olarak Pisagor ile birleşir.','islem'),
    (Fr(px,mMa),'Yalnız K’nin momentumunu (5) M’nin kütlesine bölmüş: 5 ÷ 1 = 5 m/s.','dikkat'),
    (Fr(py,mMa),'Yalnız L’nin momentumunu (12) M’nin kütlesine bölmüş: 12 ÷ 1 = 12 m/s.','dikkat'),
    (Fr(px+py,mMa),'Momentumları skaler toplamış: (5 + 12) ÷ 1 = 17 m/s.','islem')]
assert [c[0] for c in e7]==[7,5,12,17]
u=.2
body='\\fill[gray!30] (0,0) circle (.2); \\draw[thick] (0,0) circle (.2);\n'
body+=vk(.2,0,.2+vKa*u,0,'5 m/s','below')+'\n'+vk(0,.2,0,.2+vLa*u,'6 m/s','right','blue')+'\n'
body+=f'\\node[font=\\small,right] at ({.2+vKa*u+.05:.2f},0) {{K, 1 kg}}; \\node[font=\\small,above] at (0,{.2+vLa*u:.2f}) {{L, 2 kg}}; \\node[font=\\small] at (-1.3,-.95) {{M, 1 kg}};\n'
body+='\\node[font=\\small] at (2.3,1.35) {kuzey $\\uparrow$}; \\node[font=\\small] at (2.3,.9) {doğu $\\rightarrow$};\n'
SK=fig(body)
q('0007',tipId='mo-patlama',tip='Ayrılma ve patlama',z='orta',alt='Patlama ve Ayrılma',kaz='Durgun bir cismin üç parçaya ayrılmasında momentum vektörlerinin toplamının sıfır olduğunu kullanarak bilinmeyen parçanın hızını bulur.',
 kart='K-AFMOM-07 (2 boyutlu patlama) · 1 kg · 5 m/s doğu, 2 kg · 6 m/s kuzey, M: 1 kg',kalip='şekilli',
 metin='Uzayda durmakta olan 4 kg kütleli bir cisim, iç patlama sonucu K, L ve M parçalarına ayrılıyor. Kütleleri sırasıyla 1 kg ve 2 kg olan K ve L parçalarının patlamadan hemen sonraki hız büyüklükleri ve yönleri (kuşbakışı) şekilde verilmiştir.\nBuna göre, 1 kg kütleli M parçasının hızının büyüklüğü kaç m/s’dir?',
 dogru=vM,yan=sec(vM,e7,'D'),istenen='M parçasının hızının büyüklüğü (m/s).',ip=['Patlamadan önceki toplam momentumun değerini düşün.'],bilgi=[BPA,BVE],sekil=SK,
 ad=[A('K ve L’nin momentumlarını bul','Her parçanın momentumu p = m·v ile hesaplanır.','pK = 1 × 5 = 5 kg·m/s (doğu), pL = 2 × 6 = 12 kg·m/s (kuzey)'),
     A('Bileşkeyi bul','Birbirine dik iki momentum vektörü Pisagor ile birleşir.','p = √(5² + 12²) = 13 kg·m/s'),
     A('Korunumu uygula','Toplam momentum sıfır olduğundan M’nin momentumu bileşkeye eşit büyüklükte, zıt yönlüdür.','pM = 13 kg·m/s'),
     A('M’nin hızını bul','Hız = momentum ÷ kütle.','vM = 13 ÷ 1 = 13 m/s')],
 puf='Durgun sistemin parçalarında momentum vektörlerinin toplamı sıfırdır; dik bileşenleri Pisagor ile birleştir.')

# ================= 08 zor · balistik sarkaç =================
mo8,vo8,vex8,Mb8=Fr(1,10),100,50,Fr(5,2)
V8=mo8*(vo8-vex8)/Mb8; h8=V8**2/(2*g); h8cm=h8*100
assert V8==2 and h8==Fr(1,5) and h8cm==20
Vb=mo8*vo8/Mb8; Vc=mo8*(vo8+vex8)/Mb8; assert (Vb,Vc)==(4,6)
e8=[(V8/(2*g)*100,'Yüksekliği h = V ÷ 2g diye (hızın karesini almadan) yazmış: 2 ÷ 20 = 0,1 m = 10 cm.','islem'),
    (V8**2/g*100,'Enerji korunumunda ½ çarpanını unutmuş: h = V² ÷ g = 4 ÷ 10 = 0,4 m = 40 cm.','islem'),
    (Vb**2/(2*g)*100,'Okun çıkış momentumunu hesaba katmamış: V = 0,1 × 100 ÷ 2,5 = 4 m/s, h = 16 ÷ 20 = 0,8 m = 80 cm.','dikkat'),
    (Vc**2/(2*g)*100,'Okun çıkış momentumunu ters işaretle eklemiş: V = 0,1 × 150 ÷ 2,5 = 6 m/s, h = 36 ÷ 20 = 1,8 m = 180 cm.','islem')]
assert [c[0] for c in e8]==[10,40,80,180]
L8=3.0; h_cm=h8*100
import math as M_
ang=M_.acos(1-float(h8)/1.0)   # çizimde ip uzunluğu 1 birim; h (çizim) = .22 birim
th=M_.radians(38); R=2.6
px0,py0=1.6,3.6
def sark(cx,th_,lab_masses=''):
    bx=cx+R*M_.sin(th_); by=py0-R*M_.cos(th_)
    return bx,by
bx0,by0=sark(px0,0)
bx1,by1=sark(px0,th)
body='\\draw[very thick] (%.2f,%.2f) -- (%.2f,%.2f); \\draw[thick] (%.2f,%.2f) -- (%.2f,%.2f);\n'%(px0-1.0,py0,px0+3.2,py0,px0-1.0,py0,px0-.7,py0+.3)
body+=f'\\fill[gray!30] ({px0-1.0},{py0}) rectangle ({px0+3.2},{py0+.18});\n'
body=f'\\fill[gray!30] ({px0-.9},{py0}) rectangle ({px0+3.5},{py0+.2}); \\draw[very thick] ({px0-.9},{py0}) -- ({px0+3.5},{py0});\n'
body+=f'\\draw[thick] ({px0},{py0}) -- ({bx0:.3f},{by0+.5:.3f}); \\draw[thick,fill=gray!30] ({bx0-.5:.3f},{by0-.2:.3f}) rectangle ({bx0+.5:.3f},{by0+.5:.3f}); \\node[font=\\small] at ({bx0:.3f},{by0+.15:.3f}) {{2,5 kg}};\n'
body+=vk(bx0-2.9,by0+.15,bx0-.55,by0+.15,'100 m/s','above')+'\n'
body+=f'\\draw[thick] (-1.4,{by0+.15:.3f}) -- (-1.1,{by0+.15:.3f}); \\fill[gray!60] (-1.45,{by0+.15:.3f}) circle (.12); \\node[font=\\small] at (-1.45,{by0-.35:.3f}) {{ok, 0,1 kg}};\n'
body=body.replace(f'\\draw[thick] (-1.4,{by0+.15:.3f}) -- (-1.1,{by0+.15:.3f}); ','')
# kaldırılmış konum (kesikli)
body+=f'\\draw[dashed] ({px0},{py0}) -- ({bx1:.3f},{by1+.5*M_.cos(th):.3f}); \\draw[dashed,rotate around={{{M_.degrees(-th):.1f}:({bx1:.3f},{by1:.3f})}}] ({bx1-.5:.3f},{by1-.2:.3f}) rectangle ({bx1+.5:.3f},{by1+.5:.3f});\n'
body+=f'\\draw[dotted] ({bx1+.9:.3f},{by0:.3f}) -- ({bx1+.9:.3f},{by1:.3f}); \\draw[dotted] ({bx0+.5:.3f},{by0:.3f}) -- ({bx1+1.1:.3f},{by0:.3f});\n'
body+=f'\\draw[<->,thin] ({bx1+.9:.3f},{by0:.3f}) -- ({bx1+.9:.3f},{by1:.3f}); \\node[font=\\small,right] at ({bx1+.95:.3f},{(by0+by1)/2:.3f}) {{$h$}};\n'
SK=fig(body)
q('0008',tipId='mo-balistik',tip='Balistik sarkaç',z='zor',alt='Esnek Olmayan Çarpışma',kaz='Saplanmalı çarpışmada momentum korunumunu, sonrasındaki yükselmede enerji korunumunu birlikte kullanarak yüksekliği bulur.',
 kart='K-AFMOM-08 (delip geçen ok) · 0,1 kg ok · 100 m/s → 50 m/s, 2,5 kg torba',kalip='şekilli',
 metin='Şekildeki düzenekte tavana iple asılı, durgun 2,5 kg kütleli kum torbasına yatay doğrultuda 100 m/s hızla gelen 0,1 kg kütleli bir ok, torbayı çok kısa sürede delip 50 m/s hızla çıkıyor (kum kaybı önemsizdir). Torba, ip gergin kalacak biçimde yükseliyor ve h kadar yükseklikte anlık durup geri dönüyor.\n(Hava direnci ve ip kütlesi önemsiz, g = 10 m/s²)\nBuna göre, h yüksekliği kaç cm’dir?',
 dogru=h8cm,yan=sec(h8cm,e8,'B'),istenen='Torbanın çıktığı en büyük h yüksekliği (cm).',ip=['Her aşamada hangi büyüklüğün korunduğunu sorgula.'],bilgi=[BK,BYU],sekil=SK,
ad=[A('Delme anını yaz','Çok kısa sürede dış itme önemsiz; sistemin momentumu korunur.','0,1 × 100 = 0,1 × 50 + 2,5 × V'),
     A('Torbanın hızını bul','Denklemi V için çöz.','2,5 × V = 5 → V = 2 m/s'),
     A('Yükselmede enerji korunumu','Delme bittikten sonra mekanik enerji korunur: kinetik enerji potansiyel enerjiye dönüşür.','½ × V² = g × h'),
     A('Yüksekliği hesapla','Değerleri yerine koy.','h = 4 ÷ 20 = 0,2 m = 20 cm')],
  puf='Çok kısa süren etkileşmede momentum, sonraki yükselmede mekanik enerji korunur; ikisini karıştırma.')

# ================= 09 orta · v–t grafiği (öncüllü) =================
mK9,mL9=1,2; vKb,vLb,vKa,vLa=8,1,2,4
assert mK9*vKb+mL9*vLb==mK9*vKa+mL9*vLa==10
Eb=Fr(1,2)*(mK9*vKb**2+mL9*vLb**2); Ea=Fr(1,2)*(mK9*vKa**2+mL9*vLa**2); assert (Eb,Ea)==(33,18) and Ea<Eb
assert (mK9*vKa-mK9*vKb)==-(mL9*vLa-mL9*vLb)==-6
ax=axis_opts('$t$ (s)','$v$ (m/s)',4.6,0,9.5,'0,1,2,3,4','0,2,4,6,8',w='6.6cm',h='5cm')
gr=ax+'\n\\addplot[thick,vurgu] coordinates {(0,8) (2,8) (2,2) (4,2)};\n\\addplot[thick,blue!70!black,dashed] coordinates {(0,1) (2,1) (2,4) (4,4)};\n'
gr+='\\node[vurgu!70!black,above] at (axis cs:1,8) {K}; \\node[blue!70!black,above] at (axis cs:3,4) {L};\n\\end{axis}'
SK=fig(gr)
sir=sirala('Yalnız II','Yalnız III','I ve II','I ve III','II ve III')
q('0009',tipId='mo-grafik',tip='Grafik yorumu ve çarpışma türü',z='orta',alt='Çarpışma Türleri',kaz='Hız–zaman grafiğinden çarpışmadaki momentum ve enerji değişimini yorumlar.',
 kart='K-AFMOM-09 (v–t, çarpışma) · mL = 2mK, enerji azalır',kalip='grafik',
 metin='Bir tren oyuncağı düzeneğinde, sürtünmesiz düz raylar üzerinde aynı yönde giden K ve L vagonlarının hızlarının zamanla değişimi grafikte verilmiştir. Arkadaki vagon öndekine t = 2 s anında yetişip çok kısa süren bir çarpışma yapmıştır.\nGrafiğe göre,\nI. K’nin kütlesi, L’ninkinin 2 katıdır.\nII. çarpışmada mekanik enerji kaybı olmuştur.\nIII. K’nin kaybettiği momentum, L’nin kazandığı momentuma eşittir.\nyargılarından hangileri doğrudur?',
 dogru='II ve III',yan=[('Yalnız II','III’ün de doğru olduğunu görmemiş: sistemin toplam momentumu korunduğundan bir cismin kaybı diğerinin kazancına eşittir.','bilgi'),
  ('Yalnız III','II’nin de doğru olduğunu görmemiş: kinetik enerji 33mK’dan 18mK’ya düşmüştür.','dikkat'),
  ('I ve II','Kütle oranını ters yazmış: momentum korunumu 8mK + mL = 2mK + 4mL → mL = 2mK bulunur, K’nin kütlesi L’ninkinin yarısıdır.','islem'),
  ('I ve III','Kütle oranını ters yazmış (I doğru sanmış) ve kinetik enerji kaybını fark etmemiş.','islem')],sira=sir,
 istenen='Doğru olan yargılar.',ip=['Grafikten çarpışmadan önceki ve sonraki hızları oku; momentum korunumunu kütle oranını bulmak için kullan.'],bilgi=[BK,BY],sekil=SK,
 ad=[A('Hızları oku','Grafikte hız sıçraması çarpışma anını gösterir.','Önce: vK = 8, vL = 1 m/s · Sonra: vK′ = 2, vL′ = 4 m/s'),
     A('Kütle oranını bul','Momentum korunumu yaz.','mK · 8 + mL · 1 = mK · 2 + mL · 4 → mL = 2mK → I yanlış'),
     A('Kinetik enerjiyi karşılaştır','Çarpışma öncesi ve sonrası toplam Ek hesapla.','önce: 33mK, sonra: 18mK → azalmış → II doğru'),
     A('Momentum değişimlerini karşıla','Toplam momentum sabittir.','ΔpK = −6mK, ΔpL = +6mK → III doğru'),
     A('Sonucu yaz','Doğru olanlar II ve III’tür.','II ve III')],
 puf='v–t grafiğindeki sıçrama noktasında momentum korunumunu yaz; enerji için önce ve sonra Ek’yi karşılaştır.')

# ================= 10 orta · p–t grafiği (öncüllü) =================
pts10=[(0,0),(2,8),(5,8),(7,-4)]
assert Fr(8-0,2-0)==4 and pts10[2][1]==pts10[1][1]==8 and pts10[3][1]<0
ax=axis_opts('$t$ (s)','$p$ (kg·m/s)',7.6,-6,10,'0,1,2,3,4,5,6,7','-4,0,4,8',w='7cm',h='5.2cm').replace('axis lines=middle','axis lines=middle,xticklabel pos=lower')
gr=ax+'\n\\addplot[thick,vurgu,mark=*,mark size=1.5pt] coordinates {'+' '.join(f'({a},{b})' for a,b in pts10)+'};\n\\end{axis}'
SK=fig(gr)
sir=sirala('Yalnız I','Yalnız III','I ve II','I ve III','II ve III')
q('0010',tipId='mo-grafik',tip='Grafik yorumu ve çarpışma türü',z='orta',alt='İtme ve Net Kuvvet',kaz='Momentum–zaman grafiğinin eğiminden net kuvveti, işaretinden hareketin yönünü yorumlar.',
 kart='K-AFMOM-10 (p–t grafiği) · (0,0), (2,8), (5,8), (7,−4)',kalip='grafik',
 metin='Doğrusal bir yolda hareket eden bir cismin çizgisel momentumunun zamanla değişimi şekildeki grafikte verilmiştir; momentumun + işareti cismin başlangıçtaki hareket yönünü göstermektedir.\nBuna göre,\nI. 0–2 s aralığında cisme etki eden net kuvvetin büyüklüğü 4 N’dur.\nII. 2–5 s aralığında cisim durmaktadır.\nIII. t = 7 s anında cisim, t = 2 s anındaki hareket yönünün tersi yönde hareket etmektedir.\nyargılarından hangileri doğrudur?',
 dogru='I ve III',yan=[('Yalnız I','III’ü de görememiş: p = −4 kg·m/s olduğundan 7. saniyede hız ters yöndedir.','dikkat'),
  ('Yalnız III','I’i de bulamamış: eğim (8 − 0) ÷ 2 = 4 kg·m/s², yani 4 N’dur.','islem'),
  ('I ve II','II’yi doğru sanmış: momentum sabitse hız sabittir; cisim durmaz, sabit hızla gider (p ≠ 0).','bilgi'),
  ('II ve III','I’i yanlış bulmuş, II’yi doğru sanmış: p–t eğimi net kuvvettir, 0–2 s’de 4 N’dur; 2–5 s’de cisim durmaz.','bilgi')],sira=sir,
 istenen='Doğru olan yargılar.',ip=['p–t grafiğinde eğimin fiziksel anlamını, momentumun işaretinin de yönü ifade ettiğini düşün.'],bilgi=[BG,BP],sekil=SK,
 ad=[A('0–2 s aralığını incele','Eğim net kuvvettir.','F = Δp ÷ Δt = 8 ÷ 2 = 4 N → I doğru'),
     A('2–5 s aralığını incele','Momentum sabit ve sıfırdan farklıdır; hız sabit, cisim hareket halindedir.','p = 8 kg·m/s ≠ 0 → II yanlış'),
     A('t = 7 s anını incele','Momentum negatiftir; hızın yönü momentumun yönündedir.','p = −4 kg·m/s → ters yön → III doğru'),
     A('Sonucu yaz','Doğru olanlar I ve III’tür.','I ve III')],
 puf='p–t grafiğinde eğim net kuvveti, p’nin işareti hareketin yönünü verir; sabit p durma değildir.')

# ================= 11 orta · dik doğrultulu kenetlenme =================
mK11,vK11,mL11,vL11=3,4,2,8
px,py=mK11*vK11,mL11*vL11; pt_=math.hypot(px,py); v11=Fr(int(pt_),mK11+mL11)
assert (px,py,pt_)==(12,16,20) and v11==4
e11=[(Fr(abs(py-px),mK11+mL11),'Momentumları çıkarmış: (16 − 12) ÷ 5 = 0,8 m/s; dik doğrultulu momentumlar vektörel toplanır.','islem'),
     (Fr(px,mK11+mL11),'Yalnız K’nin momentumunu (12) toplam kütleye bölmüş: 12 ÷ 5 = 2,4 m/s.','dikkat'),
     (Fr(int(pt_),mK11),'Bileşke momentumu (20) yalnız K’nin kütlesine (3 kg) bölmüş: 20 ÷ 3 yerine… ','bilgi'),
     (Fr(px+py,mK11+mL11),'Momentumları skaler toplamış: (12 + 16) ÷ 5 = 5,6 m/s.','islem')]
# doğru: 20/5 = 4 m/s; çeldirici seti: 0,8 · 2,4 · 4 · 5 · 5,6  → 5: 20 ÷ 4 (L'nin kütlesine)
e11[2]=(Fr(int(pt_),mL11*2),'Bileşke momentumu (20) yalnız L’nin kütlesinin iki katına (4 kg) bölmüş: 20 ÷ 4 = 5 m/s; toplam kütle 5 kg’dır.','islem')
assert [c[0] for c in e11]==[Fr(4,5),Fr(12,5),5,Fr(28,5)]
u=.3
body='\\fill[gray!30] (0,0) circle (.12);\\node[font=\\small,above right] at (0,0) {O};\n'
body+=blok(-2.9,.9,.8,'K',y=-.4)+'\n'+vk(-2.4,0,-.2,0,'','above')+'\n'
body=body.replace(vk(-2.4,0,-.2,0,'','above')+'\n','')
# K: batıdan O'ya doğru (sağa), L: güneyden O'ya doğru (yukarı); ok boyları hız ile orantılı
body='\\fill[gray!30] (0,0) circle (.1); \\node[font=\\small,above right,inner sep=2pt] at (.1,.05) {O};\n'
body+='\\draw[thick,fill=gray!25] (-3.3,-.35) rectangle (-2.4,.35); \\node[font=\\small] at (-2.85,0) {K};\n'
body+=vk(-2.35,0,-2.35+vK11*u,0,'4 m/s','above')+'\n'
body+='\\draw[thick,fill=gray!25] (-.35,-3.35) rectangle (.35,-2.65); \\node[font=\\small] at (0,-3) {L};\n'
body+=vk(0,-2.6,0,-2.6+vL11*u,'8 m/s','right','blue')+'\n'
body+='\\draw[dotted] (-1.1,0) -- (-.14,0);\n'
body+='\\node[font=\\small] at (-2.85,-.7) {3 kg}; \\node[font=\\small] at (.95,-3.0) {2 kg};\n'
body+='\\node[font=\\small] at (2.1,1.0) {kuzey $\\uparrow$}; \\node[font=\\small] at (2.1,.55) {doğu $\\rightarrow$};\n'
SK=fig(body)
q('0011',tipId='mo-yapisik',tip='Kenetlenme ve sürtünmeli yavaşlama',z='orta',alt='Esnek Olmayan Çarpışma',kaz='Birbirine dik doğrultularda hareket eden cisimlerin kenetlenmesinde momentum korunumunu vektörel uygular.',
 kart='K-AFMOM-11 (dik kenetlenme) · 3 kg · 4 m/s doğu, 2 kg · 8 m/s kuzey',kalip='şekilli',
 metin='Sürtünmesiz yatay düzlemde kütleleri 3 kg ve 2 kg olan K ve L cisimleri, kuşbakışı şekilde gösterildiği gibi birbirine dik doğrultularda hareket edip O noktasında çarpışarak kenetleniyor.\nBuna göre, kenetlenen cisimlerin çarpışmadan hemen sonraki hızının büyüklüğü kaç m/s’dir?',
 dogru=v11,yan=sec(v11,e11,'C'),istenen='Kenetlenmiş cisimlerin hızının büyüklüğü (m/s).',ip=['Çarpışma öncesi toplam momentumu doğrultularıyla birlikte düşün.'],bilgi=[BVE,BK],sekil=SK,
 ad=[A('Momentumları yaz','Her cismin momentumu kendi doğrultusundadır.','pK = 3 · 4 = 12 (doğu), pL = 2 · 8 = 16 (kuzey)'),
     A('Bileşkeyi bul','Dik momentumlar Pisagor ile birleşir.','p = √(12² + 16²) = 20 kg·m/s'),
     A('Momentum korunumu','Kenetlenmiş cismin kütlesi 5 kg’dır.','20 = (3 + 2) · v'),
     A('Hızı hesapla','Denklemi çöz.','v = 20 ÷ 5 = 4 m/s')],
 puf='Dik doğrultulu çarpışmalarda momentumlar bileşenlerine ayrılır, Pisagor ile birleştirilir; hız toplam kütleye bölünerek bulunur.')

# ================= 12 orta · eşit bölmeli zeminde kütle oranı =================
xK,xL,D=-4,2,2
vK12,vL12=Fr(-xK),Fr(-xL)         # bölme/t (K sağa +, L sola −)
vL12=-vL12*1
# çarpışmada O'da; sonra t sürede D bölme
# mK*vK + mL*vL = (mK+mL)*D  → mK*(4−D) = mL*(D+2)  → mL/mK
vK12=4; vL12=-2
oran=Fr(vK12-D,D-vL12); assert oran==Fr(1,2)             # mL/mK
mKk,mLk=2,1; assert mKk*vK12+mLk*vL12==(mKk+mLk)*D
def mr_(Dx): return Fr(vK12-Dx,Dx-vL12)
e12=[(mr_(3),'Kenetlenmiş cismin O’dan 3 bölme sağda bulunduğunu okumuş (D = 3): (4 − 3) ÷ (3 + 2) = 1/5.','dikkat'),
     (mr_(1),'Kenetlenmiş cismin O’dan yalnız 1 bölme uzakta olduğunu okumuş (D = 1): (4 − 1) ÷ (1 + 2) = 1.','dikkat'),
     (Fr(2),'Kütle oranını ters yazmış (mK ÷ mL = 2 bulup mL ÷ mK yerine yazmış).','islem'),
     (Fr(4),'Hızlar oranının karesini (4) kütle oranı sanmış.','bilgi')]
assert [c[0] for c in e12]==[Fr(1,5),1,2,4]
def sf(x): x=Fr(x); return str(x.numerator) if x.denominator==1 else f'{x.numerator}/{x.denominator}'
sir12=[sf(x) for x in sorted([oran]+[c[0] for c in e12])]
def seritli(y0,n=15,xs=-6,ek=''):
    s=''
    for i in range(n):
        x=xs+i
        s+=f'\\draw[thick,fill={"gray!35" if i%2==0 else "white"}] ({x},{y0}) rectangle ({x+1},{y0+.35});'
    return s
cen=lambda c:c+.5
body=''
for i in range(14):
    x=-7.5+i
    body+=f'\\fill[{"gray!35" if i%2==0 else "white"}] ({x},-.35) rectangle ({x+1},0); \\draw[thick] ({x},-.35) rectangle ({x+1},0);'
    body+=f'\\fill[{"gray!35" if i%2==0 else "white"}] ({x},-2.95) rectangle ({x+1},-2.6); \\draw[thick] ({x},-2.95) rectangle ({x+1},-2.6);'
body+='\n\\node[font=\\small,anchor=west] at (-7,.55) {Şekil I};\\node[font=\\small,anchor=west] at (-7,-2.15) {Şekil II};\n'
body+=f'\\fill (0,-.175) circle (1.6pt); \\node[font=\\small] at (0,-.62) {{O}}; \\fill (0,-2.775) circle (1.6pt); \\node[font=\\small] at (0,-3.2) {{O}};\n'
body=body.replace('\\fill (0,-.175) circle (1.6pt); \\node[font=\\small] at (0,-.62) {O}; ','')
body+='\\fill (0,-.175) circle (1.6pt); \\node[font=\\small] at (0,-.62) {O};\n'
body+=f'\\draw[thick,fill=gray!25] ({xK-.45:.2f},0) rectangle ({xK+.45:.2f},.7); \\node[font=\\small] at ({xK:.2f},.35) {{K}}; '+vk(xK+.5,.35,xK+1.5,.35,'','above')+'\n'
body+=f'\\draw[thick,fill=gray!25] ({xL-.45:.2f},0) rectangle ({xL+.45:.2f},.7); \\node[font=\\small] at ({xL:.2f},.35) {{L}}; '+vk(xL-.5,.35,xL-1.0,.35,'','above','blue')+'\n'
body+=f'\\draw[thick,fill=gray!25] ({D-.6:.2f},-2.6) rectangle ({D+.6:.2f},-1.85); \\node[font=\\small] at ({D:.2f},-2.22) {{K+L}};\n'
SK=fig(body)
q('0012',tipId='mo-yapisik',tip='Kenetlenme ve sürtünmeli yavaşlama',z='orta',alt='Esnek Olmayan Çarpışma',kaz='Eşit bölmeli düzlemde konumlardan hızları okuyup kenetlenmeli çarpışmada kütle oranını bulur.',
 kart='K-AFMOM-12 (eşit bölmeli, kenetlenme) · vK = 4, vL = 2 bölme/t, D = 2',kalip='şekilli',
 metin='Sürtünmesiz ve eşit bölmeli yatay düzlemde K ve L cisimleri Şekil I’deki konumlardan aynı anda sabit hızlarla geçtikten t süre sonra O noktasında çarpışıp kenetleniyor. Kenetlenmiş cisimler çarpışmadan t süre sonra Şekil II’deki konumda bulunuyor.\nBuna göre, L cisminin kütlesinin K cisminin kütlesine oranı mL ÷ mK kaçtır?',
 dogru=sf(oran),yan=[(sf(c[0]),c[1],c[2]) for c in e12],sira=sir12,istenen='mL ÷ mK oranı.',ip=['Konum değişimlerini aynı t süresi için karşılaştırıp hızları “bölme/t” cinsinden yaz.'],bilgi=[BK,BY],sekil=SK,
 ad=[A('Hızları oku','Çarpışmaya kadar geçen süre t’dir; K 4 bölme, L 2 bölme gider.','vK = +4, vL = −2 (bölme/t)'),
     A('Ortak hızı oku','Çarpışmadan sonra t sürede 2 bölme sağa gidilmiştir.','V = +2 bölme/t'),
     A('Momentum korunumunu yaz','Sağ yönü + al.','mK · 4 + mL · (−2) = (mK + mL) · 2'),
     A('Oranı bul','Denklemi sadeleştir.','2·mK = 4·mL → mK = 2·mL'),
     A('İstenen oranı yaz','mL ÷ mK değeri sorulmaktadır.','mL ÷ mK = 1/2')],
 puf='Eşit bölmeli zeminde konum değişimleri aynı sürede hızları orantılı verir; kütle oranını momentum korunumu belirler.')

# ================= 13 orta · yayla ayrılma =================
mK13,mL13,vK13=2,6,6
vL13=Fr(mK13*vK13,mL13); Ey=Fr(1,2)*mK13*vK13**2+Fr(1,2)*mL13*vL13**2
assert vL13==2 and Ey==48
e13=[(Fr(1,2)*mK13*vK13**2,'Yalnız K’nin kinetik enerjisini (36 J) yay enerjisi sanmış; L’nin enerjisini katmamış.','dikkat'),
     (mK13*vK13**2,'K’nin kinetik enerjisini ½ çarpanı olmadan (2 · 36 = 72 J) yazmış ve L’nin enerjisini katmamış.','islem'),
     (2*Ey,'İki parçanın enerjilerini ayrı ayrı hesaplayıp çarpanı iki katına çıkarmış: 2 · 48 = 96 J.','islem'),
     (Fr(1,2)*(mK13+mL13)*vK13**2,'L’nin de 6 m/s ile gittiğini sanmış: ½ · 8 · 36 = 144 J.','bilgi')]
assert [c[0] for c in e13]==[36,72,96,144]
u=.3
body=zem(-.3,8.3)+'\n'+blok(2.2,.9,.8,'K')+'\n'+blok(5.3,1.5,.8,'L')+'\n'
body+='\\draw[thick,decorate,decoration={zigzag,segment length=2.5pt,amplitude=2pt}] (2.65,.4) -- (4.55,.4);\n'
body+=vk(1.75,.4,1.75-vK13*u*.6,.4,'6 m/s','above')+'\n'
body+='\\node[font=\\small] at (2.2,1.25) {2 kg}; \\node[font=\\small] at (5.3,1.25) {6 kg};\n'
SK=fig(body)
q('0013',tipId='mo-patlama',tip='Ayrılma ve patlama',z='orta',alt='Patlama ve Ayrılma',kaz='Yayla ayrılan cisimlerde momentum korunumundan hızları, hızlardan yayda depolanan enerjiyi bulur.',
 kart='K-AFMOM-13 (yaylı ayrılma) · 2 kg, 6 kg, vK = 6 m/s',kalip='şekilli',
 metin='Sürtünmesiz yatay düzlemde duran K ve L cisimlerinin arasına, cisimlere bağlı olmayan hafif bir yay sıkıştırılarak şekildeki gibi yerleştirilmiştir. Cisimler serbest bırakıldığında yay cisimlerden ayrılıyor; K cismi 6 m/s büyüklüğünde hızla şekildeki yönde hareket ediyor.\nBuna göre, serbest bırakılmadan önce yayda depolanan potansiyel enerji kaç J’dür?',
 dogru=Ey,yan=sec(Ey,e13,'B'),istenen='Yayda depolanan potansiyel enerji (J).',ip=['L’nin kinetik enerjisi için önce neyi bilmen gerekir?'],bilgi=[BPA,BK],sekil=SK,
 ad=[A('L’nin hızını bul','Başlangıçta toplam momentum sıfırdır.','0 = 2 · 6 − 6 · vL → vL = 2 m/s'),
     A('K’nin kinetik enerjisi','Ek = ½·m·v²','EK = ½ · 2 · 6² = 36 J'),
     A('L’nin kinetik enerjisi','Aynı bağıntıyı L için yaz.','EL = ½ · 6 · 2² = 12 J'),
     A('Enerjiyi yaz','Yayın potansiyel enerjisi iki cismin kinetik enerji toplamına dönüşür.','Ey = 36 + 12 = 48 J')],
 puf='Yayla ayrılan cisimlerde önce momentum korunumuyla hızı, sonra toplam kinetik enerjiyi bul.')

# ================= 14 orta · işaretli alanlı F–t grafiği =================
m14,v014=4,2; pts14=[(0,0),(2,10),(4,10),(6,0),(8,-4)]
I14=alan(pts14); v14=v014+I14/m14
assert I14==36 and v14==11
pos=alan(pts14[:4]); neg=alan(pts14[3:]); assert (pos,neg)==(40,-4)
e14=[(-v014+I14/m14,'İlk hızı ters işaretli almış: −2 + 9 = 7 m/s; ilk hız da +x yönündedir.','islem'),
     (I14/m14,'İlk hızı hesaba katmamış: yalnız Δv = 36 ÷ 4 = 9 m/s.','dikkat'),
     (v014+pos/m14,'Grafiğin negatif bölümünü (6–8 s) hesaba katmamış: 2 + 40 ÷ 4 = 12 m/s.','dikkat'),
     (v014+(pos-neg)/m14,'6–8 s aralığındaki alanı da pozitif sayıp toplamış: 2 + 44 ÷ 4 = 13 m/s.','islem')]
assert [c[0] for c in e14]==[7,9,12,13]
ax=axis_opts('$t$ (s)','$F$ (N)',8.7,-6,12,'0,1,2,3,4,5,6,7,8','-4,0,5,10',w='7cm',h='5.2cm').replace('axis lines=middle','axis lines=middle,xticklabel pos=lower')
gr=ax+'\n\\addplot[thick,vurgu,mark=*,mark size=1.5pt] coordinates {'+' '.join(f'({a},{b})' for a,b in pts14)+'};\n\\end{axis}'
SK=fig(gr)
q('0014',tipId='mo-ft',tip='F–t grafiği ve itme',z='orta',alt='İtme',kaz='İşaretli F–t alanından itmeyi bulur ve ilk momentumla birleştirerek son hızı hesaplar.',
 kart='K-AFMOM-14 (F–t, işaretli alan) · m = 4 kg, v₀ = 2 m/s, alan = 36 N·s',kalip='grafik',
 metin='Sürtünmesiz yatay düzlemde, t = 0 anında +x yönünde 2 m/s hızla giden 4 kg kütleli cisme x doğrultusunda etki eden net kuvvetin zamana bağlı grafiği şekildeki gibidir; kuvvetin + işareti +x yönünü göstermektedir.\nBuna göre, cismin t = 8 s anındaki hızının büyüklüğü kaç m/s’dir?',
 dogru=v14,yan=sec(v14,e14,'C'),istenen='Cismin t = 8 s anındaki hızının büyüklüğü (m/s).',ip=['Grafiğin ekseninin altında kalan bölümün itmeye katkısının işaretini unutma.'],bilgi=[BI,BP],sekil=SK,
 ad=[A('Pozitif alanı bul','0–6 s aralığı yamuk ve üçgenlerden oluşur.','½ · 2 · 10 + 2 · 10 + ½ · 2 · 10 = 40 N·s'),
     A('Negatif alanı bul','6–8 s aralığında kuvvet −x yönündedir.','½ · 2 · (−4) = −4 N·s'),
     A('Toplam itmeyi yaz','İşaretli alanlar toplanır.','I = 40 − 4 = 36 N·s'),
     A('Momentum değişimine eşitle','İtme Δp = m·(v − v₀) değerine eşittir.','36 = 4 · (v − 2) → v = 11 m/s')],
 puf='F–t grafiğinde eksenin altındaki alan negatif itmedir; son hız için ilk hızı işaretiyle ekle.')

# ================= 15 zor · eğik atışın tepesinde patlama =================
vx15,vy15,m15=10,20,2
tt=Fr(vy15,g); xp=vx15*tt; hp=Fr(vy15**2,2*g); assert (tt,xp,hp)==(2,20,20)
vsec=Fr(m15*vx15,1); assert vsec==20                      # 1 kg · v = 2 kg · 10 → v = 20 m/s (diğer parça durgun düşer)
td=math.sqrt(2*float(hp)/g); assert td==2
x15=xp+vsec*2; assert x15==60
e15=[(xp,'Diğer parçanın da durgun kaldığını (aynı noktaya düştüğünü) düşünmüş: patlama noktasının izdüşümü, 20 m.','dikkat'),
     (xp+vx15*2,'Patlamadan sonra yatay hızın değişmediğini sanmış: 20 + 10 · 2 = 40 m.','bilgi'),
     (vsec*4,'Düşme süresini toplam uçuş süresi 4 s alıp patlama noktasının x değerini (20 m) eklememiş: 20 × 4 = 80 m.','islem'),
     (xp+vsec*4,'Düşme süresini 4 s (toplam uçuş süresi) alarak 20 + 20 · 4 = 100 m bulmuş.','islem')]
assert [c[0] for c in e15]==[20,40,80,100]
# tek ölçek: 1 m = .06 cm ; yörünge y = x(…)  → parabol: y = vy/vx·x − g x²/(2 vx²)
sc=.1
pts=' '.join(f'({x*sc:.3f},{(vy15/vx15*x-g*x*x/(2*vx15**2))*sc:.3f})' for x in range(0,41,2))
body=zem(-.4,5.3)+'\n'
body+=f'\\draw[thick,dashed] plot[smooth] coordinates {{{pts}}};\n'
body=body.replace('\\draw[thick,dashed] plot[smooth] coordinates {'+pts+'};\n','')
pts=' '.join(f'({x*sc:.3f},{(vy15/vx15*x-g*x*x/(2*vx15**2))*sc:.3f})' for x in range(0,21,2))
body+=f'\\draw[thick,dashed] plot[smooth] coordinates {{{pts}}};\n'
body+='\\fill (0,0) circle (1.8pt); \\node[font=\\small,left] at (-.08,-.25) {O};\n'
body+=f'\\fill ({xp*sc:.3f},{hp*sc:.3f}) circle (2.2pt); \\node[font=\\small,above] at ({xp*sc:.3f},{hp*sc+.05:.3f}) {{T}};\n'
body+=vk(0,0,vx15*.06,0,'')+' \\node[font=\\small,right,inner sep=2pt] at (%.2f,.12) {$10$ m/s}; '%(vx15*.06)+vk(0,0,0,vy15*.06,'$20$ m/s','left','blue')+'\n'
body+=f'\\draw[dotted] ({xp*sc:.3f},0) -- ({xp*sc:.3f},{hp*sc:.3f});\n'
SK=fig(body)
q('0015',tipId='mo-patlama',tip='Ayrılma ve patlama',z='zor',alt='Patlama ve Ayrılma',kaz='Eğik atışın tepe noktasındaki patlamada yatay momentumun korunumunu, parçaların sonraki hareketini yatay atış gibi inceleyerek uygular.',
 kart='K-AFMOM-15 (eğik atış + patlama) · vx = 10, vy = 20 m/s, 2 kg → 1 kg + 1 kg',kalip='şekilli',
 metin='Düz yatay zeminin O noktasından, kütlesi 2 kg olan bir cisim, hız bileşenleri şekilde verilen biçimde eğik atılıyor. Cisim yörüngesinin en yüksek T noktasında iç patlamayla kütleleri 1 kg olan iki parçaya ayrılıyor. Patlamadan hemen sonra parçalardan birinin hızı sıfır oluyor, parçalar aynı düşey düzlemde hareket ediyor.\n(Hava direnci önemsiz, g = 10 m/s²)\nBuna göre, hızı sıfır olmayan parça yere O noktasından kaç m uzağa düşer?',
 dogru=x15,yan=sec(x15,e15,'C'),istenen='Diğer parçanın yere düştüğü yerin O’ya uzaklığı (m).',ip=['Tepe noktasında cismin hızını ve yüksekliğini bul; patlamada yatay momentumun korunduğunu kullan.'],bilgi=[BAT,BPA],sekil=SK,
 ad=[A('Tepe noktasını bul','Düşey hız sıfır olunca tepe noktasına ulaşılır.','t = 20 ÷ 10 = 2 s → x = 10 · 2 = 20 m, h = ½·10·2² = 20 m'),
     A('Patlamadan önceki momentum','Tepede yalnızca yatay hız vardır.','p = 2 · 10 = 20 kg·m/s (yatay)'),
     A('Patlamadan sonraki hız','Bir parça durduğundan momentum diğerinde toplanır.','20 = 1 · v → v = 20 m/s'),
     A('Düşme süresini bul','Parça T noktasından yatay atılmış gibi hareket eder.','20 = ½ · 10 · t² → t = 2 s'),
     A('Yatay yolu hesapla','Yatay hız sabittir.','Δx = 20 · 2 = 40 m'),
     A('O’ya olan uzaklığı yaz','T’nin izdüşümüne ekle.','x = 20 + 40 = 60 m')],
 puf='Patlamada yatay momentum korunur; sonrasında her parça yatay atış gibi hareket eder.')

# ================= 16 orta · yere çarpıp yükselen top =================
mb,hb,hr,dtb=Fr(1,2),Fr(5,4),Fr(9,20),Fr(4,100)
vb1=math.sqrt(2*g*float(hb)); vb2=math.sqrt(2*g*float(hr)); assert abs(vb1-5)<1e-9 and abs(vb2-3)<1e-9
vb1,vb2=5,3
dpb=mb*(vb1+vb2); Fnet=dpb/dtb; Nb=Fnet+mb*g
assert dpb==4 and Fnet==100 and Nb==105
e16=[(mb*(vb1-vb2)/dtb,'Hız değişimini fark olarak (5 − 3 = 2 m/s) almış: Δp = 1 kg·m/s, F = 1 ÷ 0,04 = 25 N.','islem'),
     (mb*vb2/dtb,'Yalnız çıkış hızını (3 m/s) kullanmış: 0,5 · 3 ÷ 0,04 = 37,5 N.','dikkat'),
     (mb*vb1/dtb,'Yalnız çarpma hızını (5 m/s) kullanmış: 0,5 · 5 ÷ 0,04 = 62,5 N.','dikkat'),
     (Fnet,'Zeminin kuvvetini Δp ÷ Δt = 100 N almış; topun ağırlığını (5 N) hesaba katmamış.','bilgi')]
assert [c[0] for c in e16]==[25,Fr(75,2),Fr(125,2),100]
s2=1.3
body=zem(-.3,6.9)+'\n'
body+=f'\\draw[dashed] (.5,{hb*s2:.3f}) -- (2.9,{hb*s2:.3f}); \\fill[gray!35] (1.2,{hb*s2+.2:.3f}) circle (.2); \\draw[thick] (1.2,{hb*s2+.2:.3f}) circle (.2);\n'
body+=f'\\draw[<->,thin] (2.7,0) -- (2.7,{hb*s2:.3f}); \\node[font=\\small,right] at (2.7,{hb*s2/2:.3f}) {{$1{{,}}25$ m}};\n'
body+=f'\\draw[dashed] (4.1,{hr*s2:.3f}) -- (6.0,{hr*s2:.3f}); \\fill[gray!35] (4.8,{hr*s2+.2:.3f}) circle (.2); \\draw[thick] (4.8,{hr*s2+.2:.3f}) circle (.2);\n'
body+=f'\\draw[<->,thin] (6.0,0) -- (6.0,{hr*s2:.3f}); \\node[font=\\small,right] at (6.0,{hr*s2/2:.3f}) {{$0{{,}}45$ m}};\n'
body+=f'\\draw[blue!70!black,very thick,{ARR}] (1.2,{hb*s2-.05:.3f}) -- (1.2,.2); \\draw[blue!70!black,very thick,{ARR}] (4.8,.05) -- (4.8,{hr*s2-.1:.3f});\n'
body+=f'\\node[font=\\small] at (1.2,-.55) {{serbest bırakma}}; \\node[font=\\small] at (4.8,-.55) {{yükselme}};\n'
SK=fig(body)
q('0016',tipId='mo-itme',tip='İtme, momentum değişimi ve ortalama kuvvet',z='orta',alt='İtme',kaz='Enerji korunumundan çarpma ve çıkış hızlarını bulur, zeminin ortalama kuvvetini ağırlığı da katarak hesaplar.',
 kart='K-AFMOM-16 (top, zemin tepkisi) · 0,5 kg, 1,25 m → 0,45 m, 0,04 s',kalip='şekilli',
 metin='Kütlesi 0,5 kg olan bir top, yerden 1,25 m yükseklikten serbest bırakılıyor. Top yere çarpıp düşey olarak yükseliyor ve en çok 0,45 m yüksekliğe çıkıyor. Topun yerle teması 0,04 s sürmüştür.\n(Hava direnci önemsiz, g = 10 m/s²)\nBuna göre, temas süresince zeminin topa uyguladığı ortalama kuvvetin büyüklüğü kaç N’dur?',
 dogru=Nb,yan=sec(Nb,e16,'E'),istenen='Zeminin topa uyguladığı ortalama kuvvetin büyüklüğü (N).',ip=['Temas süresince topa etkiyen kuvvetleri çiz; net kuvvet ile momentum değişimini ilişkilendir.'],bilgi=[BO,BYU],sekil=SK,
 ad=[A('Çarpma hızını bul','Düşmede enerji korunur.','v₁ = √(2 · 10 · 1,25) = 5 m/s (aşağı)'),
     A('Ayrılma hızını bul','Yükselmede de enerji korunur.','v₂ = √(2 · 10 · 0,45) = 3 m/s (yukarı)'),
     A('Momentum değişimini yaz','Yön değiştirdiğinden büyüklükler toplanır.','Δp = 0,5 · (5 + 3) = 4 kg·m/s'),
     A('Net kuvveti bul','Net kuvvet Δp ÷ Δt’dir; zeminin kuvveti N, ağırlık aşağıdadır.','N − mg = 4 ÷ 0,04 = 100 N'),
     A('Zeminin kuvvetini yaz','Ağırlığı (5 N) ekle.','N = 100 + 5 = 105 N')],
 puf='Temas süresince topa hem zeminin kuvveti hem ağırlık etki eder; net kuvvet Δp ÷ Δt’dir.')

# ================= 17 orta · düşey boşalan kum (öncüllü) =================
mv,vv,mk_=3000,6,1000
V17=Fr(mv*vv,mv+mk_); assert V17==Fr(9,2)
Ek1=Fr(1,2)*mv*vv**2; Ek2=Fr(1,2)*(mv+mk_)*V17**2; assert (Ek1,Ek2)==(54000,40500) and Ek2<Ek1
body=zem(-.3,9.2)+'\n'
body+='\\draw[thick,fill=gray!25] (1.2,.25) rectangle (5.2,1.3); \\draw[thick] (1.2,.25) circle (0pt);\n'
body=body.replace('\\draw[thick] (1.2,.25) circle (0pt);\n','\n')
body+='\\fill (1.9,.25) circle (.2); \\fill (4.5,.25) circle (.2); \\draw[thick] (1.9,.05) circle (.2) (4.5,.05) circle (.2);\n'
body=body.replace('\\fill (1.9,.25) circle (.2); \\fill (4.5,.25) circle (.2); \\draw[thick] (1.9,.05) circle (.2) (4.5,.05) circle (.2);\n','')
body+='\\node[font=\\small] at (3.2,.78) {vagon, 3000 kg}; \\fill[gray!60] (1.9,.2) circle (.2); \\fill[gray!60] (4.5,.2) circle (.2);\n'
body+=vk(5.3,.78,5.3+vv*.3,.78,'6 m/s','above')+'\n'
body+='\\draw[thick,fill=gray!15] (2.5,3.8) -- (4.1,3.8) -- (3.5,3.0) -- (3.1,3.0) -- cycle; \\node[font=\\small] at (3.3,4.25) {silo (1000 kg kum)};\n'
body+='\\foreach \\yy in {2.7,2.3,1.9,1.5} {\\fill[gray!70] (3.3,\\yy) circle (.07);}\n'
body+=vk(3.3,2.95,3.3,1.4,'','right')+'\n'
SK=fig(body)
sir=sirala('Yalnız I','I ve II','I ve III','II ve III','I, II ve III')
q('0017',tipId='mo-yapisik',tip='Kenetlenme ve sürtünmeli yavaşlama',z='orta',alt='Esnek Olmayan Çarpışma',kaz='Hareketli vagona düşey boşalan kumda yatay momentumun korunumunu ve kinetik enerjinin azaldığını yorumlar.',
 kart='K-AFMOM-17 (vagona kum boşalması) · 3000 kg · 6 m/s, 1000 kg kum',kalip='öncüllü',
 metin='Sürtünmesiz yatay raylarda 6 m/s hızla giden 3000 kg kütleli açık vagonun üzerine, durmakta olan bir siloda bulunan 1000 kg kütleli kum düşey doğrultuda boşalıyor ve kumun tamamı vagonda kalıyor. Hava direnci önemsizdir.\nBuna göre,\nI. Kum boşaldıktan sonra vagonun hızı 4,5 m/s olur.\nII. Vagon–kum sisteminin yatay momentumu korunur.\nIII. Vagon–kum sisteminin kinetik enerjisi korunur.\nyargılarından hangileri doğrudur?',
 dogru='I ve II',yan=[('Yalnız I','II’yi doğru bulmamış: dış yatay kuvvet olmadığından sistemin yatay momentumu korunur; hızın 4,5 m/s çıkması bu korunumdan gelir.','bilgi'),
  ('I ve III','III’ü doğru sanmış: vagon kuma yatay kuvvet uygulayıp onu hızlandırırken yapışma ve sürtünmeyle kinetik enerjinin bir kısmı ısıya dönüşür; Ek 54000 J’den 40500 J’e düşer.','bilgi'),
  ('II ve III','I’i yanlış bulmuş, III’ü doğru sanmış: momentum korunumundan v = 3000 · 6 ÷ 4000 = 4,5 m/s’dir ve kinetik enerji azalır.','islem'),
  ('I, II ve III','III’ü de doğru sanmış; momentum korunması kinetik enerjinin de korunacağı anlamına gelmez, kum vagona yapışarak hızlanırken enerji kaybı olur.','bilgi')],sira=sir,
 istenen='Doğru olan yargılar.',ip=['Vagon ve kumdan oluşan sisteme yatay doğrultuda dışarıdan etki eden kuvvet olup olmadığına bak.'],bilgi=[BK,BY],sekil=SK,
 ad=[A('Yatay kuvvetleri incele','Sürtünme yok; kumun düşey boşalması yatay dış kuvvet oluşturmaz.','Yatay momentum korunur → II doğru'),
     A('Son hızı bul','Kum başlangıçta yatayda durgundur.','3000 · 6 = 4000 · V → V = 4,5 m/s → I doğru'),
     A('Kinetik enerjiyi karşılaştır','Önce ve sonra Ek hesapla.','Ek önce = 54000 J, Ek sonra = 40500 J → III yanlış'),
     A('Sonucu yaz','Doğru olanlar I ve II’dir.','I ve II')],
 puf='Kumun kütlesi sisteme katılırken yatay momentum korunur, kinetik enerji korunmaz.')

# ================= 18 zor · esnek çarpışma + rampa =================
h18,mK18,mL18=Fr(9,5),1,2
vK18=math.sqrt(2*g*float(h18)); assert abs(vK18-6)<1e-12; vK18=6
vL18=Fr(2*mK18*vK18,mK18+mL18); vK18p=Fr((mK18-mL18)*vK18,mK18+mL18)
hL=vL18**2/(2*g); hK=vK18p**2/(2*g)
assert (vL18,vK18p,hL,hK)==(4,-2,Fr(4,5),Fr(1,5))
assert mK18*vK18==mK18*vK18p+mL18*vL18 and vK18-0==vL18-vK18p
e18=[(Fr(vK18**2,2*g),'Eşit kütleli cisimlerdeki hız değiş tokuşunu uygulamış: L’nin hızını 6 m/s sanıp h = 36 ÷ 20 = 1,8 m bulmuş.','bilgi'),
     (Fr(2*mL18*vK18,mK18+mL18)**2/(2*g),'Kütleleri formülde ters yazmış: vL′ = 2 · 2 · 6 ÷ 3 = 8 m/s, h = 64 ÷ 20 = 3,2 m.','islem'),
     (Fr(vK18+vL18)**2/(2*g),'L’nin hızını K’nin hızı ile çarpışma sonrası değeri toplayarak (6 + 4 = 10 m/s) bulmuş: h = 100 ÷ 20 = 5 m.','islem'),
     (Fr(2*vK18)**2/(2*g),'Esnek çarpışmada L’nin hızını 2v = 12 m/s sanmış: h = 144 ÷ 20 = 7,2 m.','bilgi')]
assert [c[0] for c in e18]==[Fr(9,5),Fr(16,5),5,Fr(36,5)]
sh=.8
H1=float(h18)*sh
body=f'\\draw[thick] (-.6,{H1:.2f}) -- (.9,{H1:.2f}) -- (2.4,0) -- (5.6,0) -- (7.4,2.6);\n'
body+=f'\\draw[thick,fill=gray!25] (-.1,{H1:.2f}) rectangle (.5,{H1+.45:.2f}); \\node[font=\\small] at (.2,{H1+.22:.2f}) {{K}}; \\node[font=\\small] at (.2,{H1+.8:.2f}) {{A}}; \\node[font=\\small] at (1.3,{H1+.5:.2f}) {{1 kg}};\n'
body+=f'\\draw[dashed] (-.9,0) -- (2.4,0); \\draw[<->,thin] (-.9,0) -- (-.9,{H1:.2f}); \\draw[dashed] (-.9,{H1:.2f}) -- (-.6,{H1:.2f}); \\node[font=\\small,left] at (-.9,{H1/2:.2f}) {{$1{{,}}8$ m}};\n'
body+='\\draw[thick,fill=gray!25] (3.6,0) rectangle (4.4,.5); \\node[font=\\small] at (4.0,.25) {L}; \\node[font=\\small] at (4.0,.85) {2 kg};\n'
SK=fig(body)
q('0018',tipId='mo-esnek',tip='Merkezî esnek çarpışma',z='zor',alt='Esnek Çarpışma',kaz='Rampadan inen cismin esnek çarpışmayla durgun cisme verdiği hızı bulur ve çıkabileceği yüksekliği enerji korunumuyla hesaplar.',
 kart='K-AFMOM-18 (rampa + esnek çarpışma) · 1 kg, 2 kg, h = 1,8 m',kalip='şekilli',
 metin='Şekildeki sürtünmesiz rayda, yatay kısmın 1,8 m yüksekliğindeki A noktasında durgun olan 1 kg kütleli K cismi serbest bırakılıyor. K cismi, yatay kısımda durmakta olan 2 kg kütleli L cismiyle merkezî ve esnek çarpışma yapıyor. Çarpışmadan sonra L cismi sağdaki rampadan yükselmektedir.\n(g = 10 m/s²)\nBuna göre, L cisminin sağdaki rampada ilk çıkışında ulaştığı en büyük yükseklik kaç m’dir?',
 dogru=hL,yan=sec(hL,e18,'A'),istenen='L cisminin çıkabildiği en büyük yükseklik (m).',ip=['Olayı üç aşamada düşün: iniş, çarpışma, yükseliş; her aşamada korunan büyüklük farklıdır.'],bilgi=[BE,BYU],sekil=SK,
 ad=[A('K’nin çarpma hızını bul','İnişte mekanik enerji korunur.','½·v² = g·h → v = √(2 · 10 · 1,8) = 6 m/s'),
     A('Momentum korunumunu yaz','K’nin yönü + alınır.','1 · 6 = 1 · vK′ + 2 · vL′'),
     A('Esneklik koşulunu yaz','Yaklaşma hızı ayrılma hızına eşittir.','6 − 0 = vL′ − vK′'),
     A('L’nin hızını bul','İki denklemi çöz.','3·vL′ = 12 → vL′ = 4 m/s (vK′ = −2 m/s)'),
     A('Yüksekliği hesapla','L’nin yükselişinde enerji korunur.','h = vL′² ÷ (2g) = 16 ÷ 20 = 0,8 m')],
 puf='Esnek çarpışmada önce çarpma hızını enerjiden, çarpışma sonrası hızları momentum ve esneklikten, yüksekliği yine enerjiden bul.')

# ================= 19 zor · kayıkta yürüyen kişi (öncüllü) =================
mp,mk2,Lk=60,120,6
xk=Fr(mp*Lk,mp+mk2); xpk=Lk-xk
assert xk==2 and xpk==4 and mp*xpk==mk2*xk
u=.62
body='\\fill[blue!8] (-.5,-.55) rectangle (8.9,0); \\draw[blue!60!black,thin] (-.5,0) -- (8.9,0);\n'
body+=f'\\draw[thick,fill=gray!20] (1.3,0) -- (1.3,.35) -- (1.3+{Lk*u:.2f},.35) -- (1.3+{Lk*u:.2f},0) -- (1.0+{Lk*u:.2f}+.3,-.0) -- cycle;\n'
body=body.replace(f'\\draw[thick,fill=gray!20] (1.3,0) -- (1.3,.35) -- (1.3+{Lk*u:.2f},.35) -- (1.3+{Lk*u:.2f},0) -- (1.0+{Lk*u:.2f}+.3,-.0) -- cycle;\n','')
body+=f'\\draw[thick,fill=gray!20] (1.3,.35) -- (1.0,.35) -- (1.5,-.35) -- ({1.3+Lk*u-.2:.2f},-.35) -- ({1.3+Lk*u+.3:.2f},.35) -- cycle;\n'
body=body.replace(f'\\draw[thick,fill=gray!20] (1.3,.35) -- (1.0,.35) -- (1.5,-.35) -- ({1.3+Lk*u-.2:.2f},-.35) -- ({1.3+Lk*u+.3:.2f},.35) -- cycle;\n',f'\\draw[thick,fill=gray!20] (1.0,.4) -- (1.4,-.1) -- ({1.3+Lk*u-.1:.2f},-.1) -- ({1.3+Lk*u+.3:.2f},.4) -- cycle;\n')
body+=f'\\draw[thick,fill=gray!50] (1.55,.7) circle (.14); \\draw[thick] (1.55,.56) -- (1.55,.15) (1.55,.15) -- (1.4,-.0) (1.55,.15) -- (1.7,-.0) (1.35,.4) -- (1.75,.4);\n'
body=body.replace('(1.55,.15) -- (1.4,-.0) (1.55,.15) -- (1.7,-.0) (1.35,.4) -- (1.75,.4);','(1.55,.15) -- (1.45,.0) (1.55,.15) -- (1.65,.0);')
body+=f'\\node[font=\\small,left] at (1.25,.75) {{kişi, 60 kg}}; \\node[font=\\small] at ({1.3+Lk*u/2:.2f},-.8) {{kayık, 120 kg}};\n'
body+=f'\\draw[<->,thin] (1.0,1.85) -- ({1.3+Lk*u+.3:.2f},1.85); \\node[font=\\small,above] at ({1.15+Lk*u/2+.15:.2f},1.85) {{$6$ m}}; '+vk(1.8,.95,2.9,.95,'1,5 m/s','above','blue')+'\n'
body+='\\node[font=\\small,blue!70!black] at (4.3,.95) {kayığa göre hız};\n'
SK=fig(body)
sir=sirala('Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III')
vrel=Fr(3,2); vk_=mp*vrel/(mp+mk2); vp_=vrel-vk_; tt19=Fr(Lk)/vrel
assert vk_==Fr(1,2) and vp_==1 and tt19==4 and mp*vp_==mk2*vk_
q('0019',tipId='mo-kutlemerkezi',tip='Kütle merkezi ve momentum',z='zor',alt='Çizgisel Momentum Korunumu',kaz='Dış kuvvetsiz sistemde göreli hızdan yere göre hızları ve süreyi bulur.',
 kart='K-AFMOM-19 (kayık ve kişi, göreli hız) · 60 kg, 120 kg, 6 m, 1,5 m/s',kalip='öncüllü',
 metin='Durgun suda, kıyıya bağlı olmayan 6 m uzunluğundaki 120 kg kütleli bir kayığın bir ucunda 60 kg kütleli bir kişi durmaktadır. Kişi, kayığa göre sabit 1,5 m/s büyüklüğündeki hızla yürüyerek diğer ucuna geçiyor. Suyun kayığa sürtünmesi ve hava direnci önemsizdir.\nBuna göre kişi yürürken,\nI. kayığın yere göre hızının büyüklüğü 0,5 m/s’dir.\nII. kişinin diğer uca ulaşması 4 s sürer.\nIII. kişinin yere göre hızının büyüklüğü 1,5 m/s’dir.\nyargılarından hangileri doğrudur?',
 dogru='I ve II',yan=[('Yalnız I','II’yi doğru bulmamış: kişi kayığa göre 1,5 m/s ile 6 m yürüdüğünden süre 6 ÷ 1,5 = 4 s’dir.','dikkat'),
  ('Yalnız II','I’i de doğru bulamamış: kişinin yere göre hızı v, kayığın hızı w ise 60·v = 120·w ve v + w = 1,5’tir; w = 0,5 m/s bulunur.','islem'),
  ('Yalnız III','Kişinin yere göre hızını kayığa göre hızına (1,5 m/s) eşit sanmış; kayık ters yöne gittiğinden yere göre hız 1,5 − 0,5 = 1 m/s’dir. I ve II de doğrudur.','bilgi'),
  ('I ve III','III’ü doğru sanmış: kişinin yere göre hızı, kayığa göre hızından kayığın geri hızı çıkarılarak 1,5 − 0,5 = 1 m/s bulunur.','bilgi')],sira=sir,
 istenen='Doğru olan yargılar.',ip=['Kişinin ve kayığın yere göre hızlarını, kişinin kayığa göre hızıyla ilişkilendir.'],bilgi=[BK,BP],sekil=SK,
 ad=[A('Yere göre hızları tanımla','Kişinin yere göre hızı v, kayığın ters yöndeki hızı w olsun; kişinin kayığa göre hızı v + w kadardır.','v + w = 1,5'),
     A('Momentum korunumunu yaz','Başlangıçta sistem durgundur, toplam momentum sıfır kalır.','60 × v = 120 × w → v = 2w'),
     A('Hızları bul','İki denklemi birlikte çöz.','3w = 1,5 → w = 0,5 m/s ve v = 1 m/s → I doğru, III yanlış'),
     A('Süreyi bul','Kişi kayığa göre 6 m yürür; kayığa göre hız 1,5 m/s’dir.','t = 6 ÷ 1,5 = 4 s → II doğru'),
     A('Sonucu yaz','Doğru olanlar I ve II’dir.','I ve II')],
 puf='Dış kuvvet yokken toplam momentum sıfırdır; kişinin kayığa göre hızı, yere göre hızlarının toplamıdır.')

# ================= 20 zor · x–t grafiği, esnek çarpışma (öncüllü) =================
mK20,mL20=1,3; xs=[((0,0),(2,10),(4,2)),((0,12),(2,10),(4,14))]
vK20b,vK20a=5,-4; vL20b,vL20a=-1,2
assert (10-0)/2==vK20b and (2-10)/2==vK20a and (10-12)/2==vL20b and (14-10)/2==vL20a
assert mK20*vK20b+mL20*vL20b==mK20*vK20a+mL20*vL20a==2
E20b=Fr(1,2)*(mK20*vK20b**2+mL20*vL20b**2); E20a=Fr(1,2)*(mK20*vK20a**2+mL20*vL20a**2); assert E20b==E20a==14
assert vK20b-vL20b==vL20a-vK20a==6
ax=axis_opts('$t$ (s)','$x$ (m)',4.6,0,15,'0,1,2,3,4','0,2,4,6,8,10,12,14',w='6.6cm',h='5.6cm')
gr=ax+'\n\\addplot[thick,vurgu] coordinates {(0,0) (2,10) (4,2)};\n\\addplot[thick,blue!70!black,dashed] coordinates {(0,12) (2,10) (4,14)};\n'
gr+='\\node[vurgu!70!black,left] at (axis cs:1.1,5) {K}; \\node[blue!70!black,above] at (axis cs:3.2,13.2) {L};\n\\end{axis}'
SK=fig(gr)
sir=sirala('Yalnız I','Yalnız III','I ve III','II ve III','I, II ve III')
q('0020',tipId='mo-grafik',tip='Grafik yorumu ve çarpışma türü',z='zor',alt='Çarpışma Türleri',kaz='Konum–zaman grafiğinin eğimlerinden hızları okuyup kütle oranını ve çarpışma türünü belirler.',
 kart='K-AFMOM-20 (x–t, esnek) · mL = 3mK, vK: 5 → −4, vL: −1 → 2',kalip='grafik',
 metin='Aynı doğru boyunca ve karşılıklı gelen K ve L bilyelerinin, sürtünmesiz bir olukta konumlarının zamanla değişimi şekildeki grafiklerle verilmiştir. Bilyeler t = 2 s anında karşılaşıp çarpışmaktadır.\nBuna göre, çarpışma için,\nI. L’nin kütlesi, K’ninkinin 3 katıdır.\nII. çarpışmadan sonraki toplam kinetik enerji, çarpışmadan öncekinden küçüktür.\nIII. K ve L’nin momentum değişimlerinin büyüklükleri birbirine eşittir.\nyargılarından hangileri doğrudur?',
 dogru='I ve III',yan=[('Yalnız I','III’ü de doğru olduğunu görmemiş: dış kuvvet olmadığından momentum değişimlerinin büyüklükleri eşittir (ΔpK = −9mK, ΔpL = +9mK).','dikkat'),
  ('Yalnız III','I’i de bulamamış: momentum korunumundan mK · 5 − mL · 1 = −mK · 4 + mL · 2 → mL = 3mK’dır.','islem'),
  ('II ve III','I’i yanlış, II’yi doğru bulmuş: kütle oranı 3’tür ve kinetik enerji 14mK’dan 14mK’ya sabittir (yaklaşma ve ayrılma hızları eşittir).','bilgi'),
  ('I, II ve III','II’yi de doğru bulmuş: grafikteki hızlar esnek çarpışmayı gösterir; kinetik enerji 14mK kadar sabit kalır, azalmaz.','bilgi')],sira=sir,
 istenen='Doğru olan yargılar.',ip=['Grafiklerin eğimlerinden çarpışmadan önceki ve sonraki hızları oku; sonra korunan büyüklükleri sına.'],bilgi=[BG,BE],sekil=SK,
 ad=[A('Hızları oku','x–t eğimi hızdır; hızlar çarpışma anında değişir.','K: +5 → −4 m/s, L: −1 → +2 m/s'),
     A('Kütle oranını bul','Momentum korunumunu yaz.','5·mK − mL = −4·mK + 2·mL → 9·mK = 3·mL → mL = 3mK → I doğru'),
     A('Kinetik enerjiyi karşılaştır','Önce ve sonra toplam Ek hesapla.','önce: 12,5mK + 1,5mK = 14mK, sonra: 8mK + 6mK = 14mK → II yanlış (esnek)'),
     A('Momentum değişimlerini karşılaştır','Toplam momentum sabit olduğundan değişimler zıt, eşit büyüklüktedir.','ΔpK = −9mK, ΔpL = +9mK → III doğru'),
     A('Sonucu yaz','Doğru olanlar I ve III’tür.','I ve III')],
 puf='x–t grafiğinde eğim hızı verir; momentum ve kinetik enerji karşılaştırmasıyla kütle oranı ve çarpışma türü belirlenir.')

# ---------- bitir ----------
for q_ in P.ANA: q_['kardes']=None
SCR='/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/mom/bos.json'
P.yaz(os.path.join(ADIR,'momentum-1.json'),SCR)
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=UK))['kartlar'].append(c['id'])
json.dump(dict(konu=P.konu_adi,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2025 AYT Fizik çıkmış soruları ve yayın soru bankaları (yalnız mantık), MEB 11. sınıf fizik müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','afmomentum.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
