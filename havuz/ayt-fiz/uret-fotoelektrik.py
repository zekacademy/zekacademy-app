"""AYT Fizik · Fotoelektrik Olay ve Compton Olayı · 20 soru (3 kolay / 11 orta / 6 zor; kardeş yok, ipucu 1). Şekil değerleri Python'da hesaplanır; her cevap ve çeldirici assert edilir."""
import sys,os,math,json
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-fiz')); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
import _hafif as H
from _hafif import *
from cizim import tikz_svg
from _hafif_mat import tablo_svg
from math import sin,cos,radians,sqrt,exp,atan2,degrees,pi
H.KONU='Fotoelektrik Olay ve Compton Olayı'
P=Parti('fotoelektrik','Fotoelektrik Olay ve Compton Olayı','afiz|Fotoelektrik Olay ve Compton Olayı',ders='AYT Fizik',idon='aytfiz')
KY='ÖSYM AYT 2018–2026 Fizik (Fotoelektrik Olayı, Compton Saçılması ve De Broglie; yalnız mantık) · 345 AYT Fizik s.331–392 · Bilgi Sarmal AYT Fizik · MEB 12. sınıf fizik'
TIPLER={'fe-esik':'Foton enerjisi ve eşik enerjisi','fe-grafik':'Ek–f ve Vs–f grafikleri','fe-durdurma':'Durdurma potansiyeli','fe-akim':'Akım–gerilim grafiği','fe-kavram':'Fotoelektrik olayın özellikleri',
 'fe-devre':'Fotoelektrik devresi','fe-foton':'Foton momentumu ve ışınım basıncı','fe-compton':'Compton saçılması','fe-debroglie':'De Broglie dalga boyu'}
CARD={}
def card(no,alt,fikir,tuzak,z,kalip,adim,tipId,ozet):
    kart(f'K-AFFOTO-{no:02d}',alt,fikir,tuzak,z,kalip,adim,tipId,TIPLER[tipId],KY); CARD[no]=ozet
def q(no,ad,**k):
    kn=int(no); mk(P,no,ad=ad,adim=len(ad),kart=f'K-AFFOTO-{kn:02d} ('+CARD[kn]+')',**k)
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
ARR='-{Stealth[length=2.2mm,width=1.9mm]}'
def N(x,y,t,o=''): return f'\\node[{o}] at ({x:.3f},{y:.3f}) {{{t}}};'
def D(a,b,o='thick'): return f'\\draw[{o}] ({a[0]:.3f},{a[1]:.3f}) -- ({b[0]:.3f},{b[1]:.3f});'
def AR(a,b,o='vurgu,very thick'): return f'\\draw[{o},{ARR}] ({a[0]:.3f},{a[1]:.3f}) -- ({b[0]:.3f},{b[1]:.3f});'
def DOT(p,r=1.8): return f'\\fill ({p[0]:.3f},{p[1]:.3f}) circle ({r}pt);'
def tikz(lines): return tikz_svg(HEAD+'\n'.join(lines)+TAIL)
def ptx(lines): return tikz_svg(HEAD+lines+TAIL)
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
        for n in ex: parts.append(f'{n}. yargıyı da doğru sanmış; gerçekte {why[nm.index(n)]}.')
        for n in ms: parts.append(f'{n}. yargının doğru olduğunu görememiş; {why[nm.index(n)]}.')
        yan.append((s,' '.join(parts),'bilgi' if ex else 'dikkat'))
    sira=sorted(sec+[dogru],key=SIR.index); assert sira.index(dogru)==pos
    return dict(dogru=dogru,sira=sira,yan=yan)
HC=12400  # eV·Å
# ---------- bilgi kutuları (örnekler soruların sayılarını kullanmaz)
FE=B('Foton enerjisi ve eşik enerjisi','foton enerjisi E = h·f = h·c ÷ λ; hc = 12400 eV·Å. Elektron sökülebilmesi için E > W (eşik enerjisi) olmalıdır ve Ek,maks = E − W. Örnek: λ = 8000 Å için E = 12400 ÷ 8000 = 1,55 eV')
EKF=B('Ek–f grafiği','Ek,maks = h·f − W doğrusunda f eksenini kestiği nokta eşik frekansı f₀, eğim ise metalden bağımsız Planck sabiti h’dır. Örnek: eğimi 0,5 eV/birim olan doğruda f₀’dan 6 birim büyük frekansta Ek = 3 eV’tur')
DUR=B('Durdurma potansiyeli','sökülen en hızlı elektronu durduran ters gerilim Vs için e·Vs = Ek,maks bağıntısı vardır. Ek,maks değeri eV cinsinden, Vs ise volt cinsinden aynı sayıdır. Örnek: Ek,maks = 1,2 eV ise Vs = 1,2 V')
VSF=B('Vs–f grafiği','Vs = (h ÷ e)·f − W ÷ e olduğundan doğrunun eğimi h ÷ e’dir; Vs = 0 olduğu frekans eşik frekansı f₀’dır ve W = h·f₀ = e × (eğim) × f₀. Örnek: eğim 0,5 V/birim ve f₀ = 6 birim ise W = 3 eV’tur')
AKIM=B('Akım–gerilim grafiği','akım, gerilim arttıkça artıp doygunluğa ulaşır. Doygunluk akımı birim zamanda sökülen elektron sayısıyla (ışığın şiddetiyle) orantılıdır. Akımın sıfır olduğu ters gerilim Vs ise Ek,maks ile belirlenir. Örnek: aynı frekansta şiddet yarıya inerse doygunluk akımı yarıya iner')
KAV=B('Işığın tanecik modeli','ışık, enerjisi h·f olan fotonlardan oluşur. Bir elektron enerjiyi yalnız bir fotondan ve bir defada alır. Işığın şiddeti birim zamanda gelen foton sayısını, frekansı ise her fotonun enerjisini belirler. Örnek: aynı frekansta iki kat şiddetli ışık iki kat fazla foton taşır')
DEV=B('Fotoelektrik devresi','ters bağlı üreteçte elektronlar anota doğru giderken e·V kadar enerji kaybeder; anota ulaşan elektronun kinetik enerjisi Ek,maks − e·V olur (e·V < Ek,maks ise akım geçer). Örnek: Ek,maks = 3 eV, ters gerilim 2 V ise anota en çok 1 eV ile çarpılır')
FOT=B('Foton momentumu','fotonun momentumu p = h ÷ λ = E ÷ c’dir. Işık gücü P ise birim zamanda gelen foton sayısı N = P ÷ E olur. Işığın yüzeye uyguladığı kuvvet, birim zamanda yüzeye aktarılan momentuma eşittir. Örnek: dalga boyu iki katına çıkan fotonun momentumu yarıya iner')
COM=B('Compton saçılması','X-ışını fotonu, durgun ve serbest kabul edilen elektronla esnek çarpışır; enerji ve (vektörel) momentum korunur. Saçılan fotonun dalga boyu λ′ = λ + (h ÷ m·c)(1 − cosθ) kadardır; θ, fotonun sapma açısıdır. Örnek: θ = 0° ise λ′ = λ olur')
DB=B('De Broglie dalga boyu','hareketli her parçacığa λ = h ÷ p dalga boyu eşlik eder. Kinetik enerjisi K olan parçacıkta p = √(2·m·K) olduğundan λ = h ÷ √(2mK) yazılır. Örnek: momentumu iki katına çıkan parçacığın dalga boyu yarıya iner')
HIZ=B('Elektrik alanda hızlanma','q yüklü bir parçacık durgun halden V potansiyel farkıyla hızlandırılırsa kazandığı kinetik enerji K = q·V olur. Örnek: yükü iki katına çıkan parçacık aynı gerilimde iki kat kinetik enerji kazanır')
# ---------- şekil yardımcıları
def tube(cx,cy,lab=True,r=1.0,light=None):
    o=[f'\\draw[thick] ({cx},{cy}) circle ({r});']
    o.append(f'\\draw[very thick] ({cx-.5:.2f},{cy-.5:.2f}) -- ({cx-.5:.2f},{cy+.5:.2f});')
    o.append(f'\\draw[very thick] ({cx+.5:.2f},{cy-.5:.2f}) -- ({cx+.5:.2f},{cy+.5:.2f});')
    if lab:
        o.append(N(cx-.5,cy+.78,'K','font=\\small')); o.append(N(cx+.5,cy+.78,'A','font=\\small'))
    return o
def plot_iv(Is,Vs,k=1.7,vmax=1.6,n=14):
    pts=[(-Vs,0.0)]
    for i in range(n+1):
        v=-Vs+(vmax+Vs)*i/n; pts.append((v,Is*(1-exp(-k*(v+Vs)))))
    pts=[(-4.0,0.0),(-Vs,0.0)]+pts[1:]
    return ' '.join(f'({x:.3f},{y:.3f})' for x,y in pts)
PGF='/pgf/number format/.cd,use comma,fixed,precision=1'
# ===== 01 kolay · eşik enerjisi sütun grafiği (öncüllü)
card(1,'Foton enerjisi ve eşik karşılaştırması','Foton enerjisi hc ÷ λ ile bulunur ve metalin eşik enerjisiyle karşılaştırılır; yalnız eşiği aşan durumda elektron sökülür.','Dalga boyunun büyük olmasını enerjinin büyük olması sanmak; eşik enerjisini kinetik enerji gibi hesaba katmak.','kolay','öncüllü',3,'fe-esik','ışık enerjisi ile üç metalin eşiği')
lam1=3100; E1=Fr(HC,lam1); assert E1==4
W1={'K':Fr(23,10),'L':Fr(43,10),'M':Fr(16,5)}; t1=[E1>W1[k] for k in 'KLM']; assert t1==[True,False,True] and all(E1!=w for w in W1.values())
bars=' '.join(f'({i+1},{float(W1[k])})' for i,k in enumerate('KLM'))
SK=ptx(f'\\begin{{axis}}[ybar,width=6.6cm,height=4.8cm,bar width=16pt,ymin=0,ymax=5,ytick={{0,1,2,3,4,5}},ymajorgrids,grid style={{gray!45}},xmin=.4,xmax=3.6,xtick={{1,2,3}},xticklabels={{K,L,M}},ylabel={{Eşik enerjisi (eV)}},label style={{font=\\small}},tick label style={{font=\\small}},/pgf/number format/.cd,use comma,fixed,precision=1,nodes near coords,every node near coord/.append style={{font=\\small}},axis lines=left]\n\\addplot[fill=vurgu!35,draw=black] coordinates {{{bars}}};\n\\end{{axis}}')
q('0001',tipId='fe-esik',tip=TIPLER['fe-esik'],z='kolay',alt='Eşik Enerjisi',kaz='Foton enerjisini dalga boyundan hesaplayıp metallerin eşik enerjileriyle karşılaştırarak fotoelektron sökülüp sökülmeyeceğini belirler.',kalip='öncüllü',
 metin='K, L ve M metal levhalarının eşik enerjileri şekildeki sütun grafiğinde verilmiştir. Dalga boyu 3100 Å olan tek renkli ışık, bu levhaların yüzeylerine ayrı ayrı gönderiliyor. (hc = 12400 eV·Å)\nBuna göre,\nI. K levhasından elektron sökülür.\nII. L levhasından elektron sökülür.\nIII. M levhasından elektron sökülür.\nyargılarından hangileri doğrudur?',
 sekil=SK,istenen='Fotoelektron sökülen levhalar.',
 ip=['Önce ışığın foton enerjisini eV cinsinden bul, sonra her levhanın eşik enerjisiyle karşılaştır.'],
 bilgi=[FE],
 ad=[A('Foton enerjisini hesapla','Enerji dalga boyuyla ters orantılıdır.','E = 12400 ÷ 3100 = 4 eV'),
     A('Eşiklerle karşılaştır','Elektron sökülmesi için foton enerjisi eşik enerjisinden büyük olmalıdır.','K: 4 > 2,3 · L: 4 < 4,3 · M: 4 > 3,2'),
     A('Yargıları değerlendir','Yalnız K ve M levhalarında koşul sağlanır.','I doğru · II yanlış · III doğru')],
 puf='Foton enerjisi eşik enerjisinden küçükse ışık ne kadar şiddetli olursa olsun elektron sökülmez.',
 **onc(t1,['foton enerjisi K’nin eşik enerjisinden büyüktür','foton enerjisi L’nin eşik enerjisinden küçüktür','foton enerjisi M’nin eşik enerjisinden büyüktür'],4))
# ===== 02 kolay · Ek–f grafiğinden okuma
card(2,'Ek–f grafiğinden okuma','Doğrusal Ek–f grafiğinde eğim bulunur ve eşik frekansından itibaren ilerleyerek istenen frekanstaki Ek,maks okunur.','Doğruyu orijinden geçen doğru sanıp orantı kurmak; eğimi eşik frekansından değil sıfırdan hesaplamak.','kolay','grafik',3,'fe-grafik','grafikten istenen frekansta Ek,maks')
f0_2,fA,EA,fq=4,8,Fr(8,5),10; sl2=Fr(EA,fA-f0_2); assert sl2==Fr(2,5); ans2=sl2*(fq-f0_2); assert ans2==Fr(12,5)
assert EA*Fr(fq,fA)==2 and sl2*fq==4 and sl2*(fq-fA)==Fr(4,5) and EA+(fq-fA)==Fr(18,5)
SK=ptx('\\begin{axis}[width=7.4cm,height=5.2cm,xmin=0,xmax=11,ymin=0,ymax=3.2,xtick={0,1,2,3,4,5,6,7,8,9,10,11},ytick={0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2},grid=both,major grid style={gray!50,thin},tick label style={font=\\scriptsize},axis lines=left,xlabel={$f$ ($10^{14}$ Hz)},ylabel={$E_{k,\\mathrm{maks}}$ (eV)},label style={font=\\small},'+PGF+']\n\\addplot[thick,vurgu] coordinates {(4,0) (8,1.6)};\n\\addplot[only marks,mark=*,mark size=1.8pt] coordinates {(4,0) (8,1.6)};\n\\end{axis}')
q('0002',tipId='fe-grafik',tip=TIPLER['fe-grafik'],z='kolay',alt='Ek–f Grafiği',kaz='Fotoelektrik olayda Ek,maks – frekans grafiğinden eğimi kullanarak başka bir frekans için kinetik enerjiyi bulur.',kalip='grafik',
 metin='Bir katot metaline gönderilen ışığın frekansı (f) ile sökülen elektronların maksimum kinetik enerjisi (Ek,maks) arasındaki değişim, deneysel olarak şekildeki doğru parçası biçiminde elde edilmiştir.\nBuna göre, aynı metale 10 × 10¹⁴ Hz frekanslı ışık gönderilirse sökülen elektronların maksimum kinetik enerjisi kaç eV olur?',
 sekil=SK,dogru=ans2,yan=[(Fr(4,5),'Grafikteki son noktadan sonraki artışı (10 − 8 = 2 birim) eğimle çarpıp yalnız bunu yazmış: 0,4 × 2, oysa son noktadaki 1,6 eV’u da eklemeliydi.','dikkat'),(2,'Doğruyu orijinden geçen doğru sanıp orantı kurmuş: 1,6 × 10 ÷ 8.','bilgi'),
  (Fr(18,5),'Frekanstaki artışı (10 − 8 = 2) doğrudan enerjiye eklemiş: 1,6 + 2.','islem'),(4,'Ek,maks = eğim × f yazıp eşik frekansını hesaba katmamış: 0,4 × 10.','bilgi')],
 istenen='10 × 10¹⁴ Hz için Ek,maks (eV).',
 ip=['Doğrunun eğimini f eksenini kestiği noktadan itibaren bul; frekansı o noktadan başlayarak ölç.'],
 bilgi=[EKF],
 ad=[A('Eşik frekansını oku','Doğru f eksenini kestiği yerde Ek,maks sıfırdır.','f₀ = 4 × 10¹⁴ Hz'),
     A('Eğimi hesapla','Eğim, Ek,maks değişiminin frekans değişimine oranıdır.','eğim = 1,6 ÷ (8 − 4) = 0,4 eV / 10¹⁴ Hz'),
     A('İstenen frekansı yerine koy','Ek,maks, f₀ değerinden itibaren eğimle orantılı artar.','Ek,maks = 0,4 × (10 − 4) = 2,4 eV')],
 puf='Ek–f doğrusu orijinden geçmez: önce eşik frekansını, sonra eşikten itibaren geçen frekans farkını kullan.')
# ===== 03 orta · iki metalin Ek–f doğruları (öncüllü)
card(3,'İki metalin Ek–f doğruları','Farklı metallerin Ek–f doğruları paraleldir (eğim h); eşik frekansı büyük olan metalin eşik enerjisi de büyüktür ve aynı ışıkta daha az Ek verir.','Eğimin metale bağlı olduğunu sanmak; Ek,maks farkının frekansla arttığını düşünmek.','orta','öncüllü',3,'fe-grafik','iki metalin grafiklerini karşılaştırma')
fX,fY,f1,sl3=4,6,8,Fr(2,5); EkX=sl3*(f1-fX); EkY=sl3*(f1-fY); assert EkX==Fr(8,5) and EkY==Fr(4,5) and fY>fX and EkX>EkY
t3=[True,True,False]
SK=ptx('\\begin{axis}[width=7cm,height=5cm,xmin=0,xmax=11.2,ymin=0,ymax=3.1,xtick={4,6,8},xticklabels={$f_X$,$f_Y$,$f_1$},ytick=\\empty,axis lines=left,xlabel={$f$},ylabel={$E_{k,\\mathrm{maks}}$},label style={font=\\small},tick label style={font=\\small}]\n'
 '\\addplot[thick,vurgu] coordinates {(4,0) (10,2.4)};\n\\addplot[thick,black] coordinates {(6,0) (10,1.6)};\n'
 '\\addplot[dashed,gray] coordinates {(8,0) (8,1.6)};\n\\addplot[only marks,mark=*,mark size=1.6pt] coordinates {(8,1.6) (8,0.8)};\n'
 '\\node[font=\\small,vurgu!70!black,anchor=south east] at (axis cs:10,2.4) {X};\n\\node[font=\\small,anchor=north west] at (axis cs:10,1.6) {Y};\n\\end{axis}')
q('0003',tipId='fe-grafik',tip=TIPLER['fe-grafik'],z='orta',alt='Ek–f Grafiği',kaz='İki farklı metalin Ek,maks – frekans doğrularını eğim, eşik frekansı ve kinetik enerji bakımından karşılaştırır.',kalip='öncüllü',
 metin='X ve Y metal levhaları üzerine ayrı ayrı gönderilen ışığın frekansı (f) ile sökülen elektronların maksimum kinetik enerjisi (Ek,maks) arasındaki değişim şekildeki grafikte verilmiştir. f₁ frekanslı ışık her iki levha için de eşik frekansından büyüktür.\nBuna göre,\nI. Doğruların eğimleri eşittir.\nII. Y levhasının eşik enerjisi X levhasınınkinden büyüktür.\nIII. f₁ frekanslı ışıkla Y’den sökülen elektronların maksimum kinetik enerjisi X’ten sökülenlerinkinden büyüktür.\nyargılarından hangileri doğrudur?',
 sekil=SK,istenen='Grafik için doğru yargılar.',
 ip=['Ek,maks = h·f − W ilişkisinde eğimin neyi, f eksenini kestiği noktanın neyi gösterdiğini düşün.'],
 bilgi=[EKF],
 ad=[A('Eğimleri karşılaştır','Eğim her metal için Planck sabiti h’dır; iki doğru paraleldir.','I doğru'),
     A('Eşik enerjilerini karşılaştır','Eşik frekansı büyük olanın eşik enerjisi W = h·f₀ de büyüktür.','f_Y > f_X → W_Y > W_X → II doğru'),
     A('f₁ için kinetik enerjileri karşılaştır','Aynı frekansta eşik enerjisi büyük olandan daha az kinetik enerjili elektron sökülür.','Ek,X > Ek,Y → III yanlış')],
 puf='Eğimin neyi, f eksenini kestiği noktanın neyi gösterdiğini ayır; her yargıyı grafikten ayrı oku.',
 **onc(t3,['iki doğru paraleldir; eğim her metalde h’dır','eşik frekansı büyük olan metalin eşik enerjisi de büyüktür','aynı frekansta eşik enerjisi küçük olan X’ten sökülen elektronlar daha büyük kinetik enerjiye sahiptir'],3))
# ===== 04 orta · durdurma potansiyeli
card(4,'Durdurma potansiyeli hesabı','Vs, foton enerjisinden eşik enerjisi çıkarılarak bulunan Ek,maks değerinin eV cinsinden sayısına eşittir.','Foton enerjisini ya da eşik enerjisini doğrudan gerilim sanmak; dalga boyu birimini yanlış dönüştürmek.','orta','hikâyeli',3,'fe-durdurma','ters gerilimle akımı sıfırlama')
lam4=2480; E4=Fr(HC,lam4); W4=Fr(14,5); Vs4=E4-W4; assert E4==5 and Vs4==Fr(11,5)
assert Fr(1240,lam4)<W4 and E4+W4==Fr(39,5)
q('0004',tipId='fe-durdurma',tip=TIPLER['fe-durdurma'],z='orta',alt='Durdurma Potansiyeli',kaz='Dalga boyu ve eşik enerjisi verilen bir fotoelektrik düzeneğinde akımı sıfırlayan ters gerilimi hesaplar.',kalip='hikâyeli',
 metin='Eşik enerjisi 2,8 eV olan bir katot metaline, dalga boyu 2480 Å olan tek renkli ışık gönderilerek fotoelektrik olay gerçekleştiriliyor. Katot ile anot arasına, anot katoda göre negatif olacak biçimde ayarlanabilir bir üreteç bağlanıyor. Üretecin gerilimi sıfırdan başlanarak yavaş yavaş artırılıyor. (hc = 12400 eV·Å)\nBuna göre, devreden geçen akımın ilk kez sıfır olduğu anda üretecin gerilimi kaç V’tur?',
 sekil=None,dogru=Vs4,yan=[(0,'hc değerini 1240 eV·Å alıp foton enerjisini 0,5 eV bulmuş; eşiğin altında kaldığı için hiç akım oluşmadığını ve gerilimin 0 olduğunu düşünmüş.','islem'),(Fr(14,5),'Eşik enerjisini durdurma potansiyeli sanmış.','bilgi'),(5,'Foton enerjisinin sayısını doğrudan ters gerilim olarak yazmış, eşik enerjisini çıkarmamış.','bilgi'),(Fr(39,5),'Eşik enerjisini foton enerjisinden çıkarmak yerine eklemiş: 5 + 2,8.','islem')],
 istenen='Akımı sıfırlayan ters gerilim (V).',
 ip=['Akımın sıfırlandığı anda ters gerilimin elektronlardan en hızlısına verdiği iş ile onun kinetik enerjisi arasındaki ilişkiyi kur.'],
 bilgi=[FE,DUR],
 ad=[A('Foton enerjisini bul','hc değeri Å cinsinden verildiği için dalga boyu Å alınır.','E = 12400 ÷ 2480 = 5 eV'),
     A('Maksimum kinetik enerjiyi bul','Foton enerjisinden eşik enerjisi çıkarılır.','Ek,maks = 5 − 2,8 = 2,2 eV'),
     A('Durdurma potansiyelini yaz','En hızlı elektronu durduran gerilimde e·Vs = Ek,maks olur.','Vs = 2,2 V')],
 puf='Ters gerilimle akım sıfırlanırken sayısal olarak Vs (V) = Ek,maks (eV) olur; hf − W değerini bulmak yeterlidir.')
# ===== 05 orta · iki ışık için akım–gerilim eğrileri (öncüllü)
card(5,'Şiddet ve akım–gerilim eğrisi','Aynı frekanslı ışıklarda durdurma potansiyeli eşittir; doygunluk akımı şiddetle orantılıdır.','Doygunluk akımı büyük olan ışığın hem frekansını hem kinetik enerjisini büyük sanmak.','orta','öncüllü',3,'fe-akim','iki ışığın akım–gerilim eğrileri')
c5=[(2,2),(1,2)]  # (Is, Vs)
assert c5[0][1]==c5[1][1] and c5[0][0]>c5[1][0]
t5=[True,False,False]
SK=ptx('\\begin{axis}[width=7cm,height=5.2cm,xmin=-3.4,xmax=3.4,ymin=0,ymax=2.5,xtick={-3,-2,-1,0,1,2,3},ytick={1,2},yticklabels={$I_0$,$2I_0$},axis x line=middle,axis y line=left,grid=both,major grid style={gray!40,thin},xlabel={$V$ (V)},ylabel={$I$},xlabel style={at={(1.01,0)},anchor=west},ylabel style={at={(0,1.02)},anchor=south},label style={font=\\small},tick label style={font=\\small}]\n'
 '\\addplot[thick,vurgu,smooth] coordinates {'+plot_iv(2,2)+'};\n\\addplot[thick,black,smooth] coordinates {'+plot_iv(1,2)+'};\n'
 '\\node[font=\\small\\bfseries,vurgu!70!black,anchor=south] at (axis cs:2.1,2.15) {1};\n\\node[font=\\small\\bfseries,anchor=south] at (axis cs:2.1,1.15) {2};\n\\end{axis}')
q('0005',tipId='fe-akim',tip=TIPLER['fe-akim'],z='orta',alt='Akım–Gerilim Grafiği',kaz='Fotoelektrik akım–gerilim eğrilerinden ışıkların şiddet ve frekanslarını karşılaştırır.',kalip='öncüllü',
 metin='Aynı katot metaliyle yapılan iki fotoelektrik deneyde, katot ile anot arasındaki gerilime bağlı olarak devreden geçen akımın değişimi şekildeki 1 ve 2 numaralı eğrilerle verilmiştir. Her deneyde tek renkli ışık kullanılmıştır. Gerilimin negatif değerleri, anodun katoda göre negatif olduğu durumları göstermektedir.\nBuna göre,\nI. 1 numaralı eğriyi veren ışığın şiddeti, 2 numaralı eğriyi verenden büyüktür.\nII. 2 numaralı eğriyi veren ışığın frekansı, 1 numaralı eğriyi verenden büyüktür.\nIII. 1 numaralı deneyde sökülen elektronların maksimum kinetik enerjisi, 2 numaralı deneydekilerden büyüktür.\nyargılarından hangileri doğrudur?',
 sekil=SK,istenen='Grafiklere göre doğru yargılar.',
 ip=['Akımın sıfır olduğu gerilimin hangi niceliği, doygunluk akımının hangi niceliği belirlediğini ayır.'],
 bilgi=[AKIM,DUR],
 ad=[A('Doygunluk akımlarını karşılaştır','Doygunluk akımı birim zamanda sökülen elektron sayısını, yani şiddeti gösterir.','I₁ = 2I₀ > I₂ = I₀ → I doğru'),
     A('Durdurma potansiyellerini karşılaştır','İki eğri akımı aynı ters gerilimde sıfırlıyor; bu, Ek,maks değerlerinin eşit olduğunu gösterir.','Vs₁ = Vs₂ = 2 V → III yanlış'),
     A('Frekansları karşılaştır','Aynı metalde Ek,maks eşitse foton enerjisi, dolayısıyla frekans da eşittir.','f₁ = f₂ → II yanlış')],
 puf='Doygunluk akımını ve akımın sıfırlandığı gerilimi ayrı ayrı yorumla.',
 **onc(t5,['doygunluk akımı büyük olan ışıkta birim zamanda daha çok foton gelir; şiddet daha büyüktür','durdurma potansiyelleri eşit olduğundan iki ışığın frekansları eşittir','durdurma potansiyelleri eşit olduğundan maksimum kinetik enerjiler de eşittir'],0))
# ===== 06 orta · iki frekans, iki durdurma potansiyeli → eşik enerjisi
card(6,'Eşik enerjisini iki ölçümden bulma','İki ışık için foton enerjileri W + e·Vs biçiminde yazılır; frekans oranı enerji oranına eşit olduğundan W çözülür.','Durdurma potansiyellerinin farkını ya da birini eşik enerjisi sanmak.','orta','hikâyeli',4,'fe-durdurma','iki ışıkta Vs farklı, frekans oranı bilinir')
Vs6a,Vs6b=Fr(3,2),5; W6=Vs6b-2*Vs6a; E6a=W6+Vs6a; E6b=W6+Vs6b
assert W6==2 and E6b==2*E6a and E6a==Fr(7,2) and W6>0 and Vs6b-Vs6a==Fr(7,2) and Vs6a+Vs6b==Fr(13,2)
q('0006',tipId='fe-durdurma',tip=TIPLER['fe-durdurma'],z='orta',alt='Durdurma Potansiyeli',kaz='Aynı metal için iki farklı frekansta ölçülen durdurma potansiyellerinden eşik enerjisini bulur.',kalip='hikâyeli',
 metin='Bir öğrenci, aynı katot metalini kullanarak iki ayrı fotoelektrik deney yapıyor. Birinci deneyde f frekanslı tek renkli ışık kullanıyor ve akımı sıfırlayan ters gerilimi 1,5 V ölçüyor. İkinci deneyde ise 2f frekanslı tek renkli ışık kullanıyor ve akımı sıfırlayan ters gerilimi 5 V ölçüyor.\nBuna göre, katot metalinin eşik enerjisi kaç eV’tur?',
 sekil=None,dogru=W6,yan=[(Fr(3,2),'Birinci deneydeki durdurma potansiyelini eşik enerjisi sanmış.','bilgi'),(Fr(7,2),'İki durdurma potansiyelinin farkını (5 − 1,5) eşik enerjisi olarak yazmış.','islem'),(5,'İkinci deneydeki durdurma potansiyelini eşik enerjisi sanmış.','bilgi'),(Fr(13,2),'İki durdurma potansiyelini toplamış: 1,5 + 5.','islem')],
 istenen='Katot metalinin eşik enerjisi (eV).',
 ip=['Her deney için foton enerjisini W ve Vs cinsinden yaz; frekanslar arasındaki oranın enerjiler arasında nasıl bir oran verdiğini kullan.'],
 bilgi=[FE,DUR],
 ad=[A('Foton enerjilerini yaz','Ek,maks = e·Vs olduğundan foton enerjisi W artı Vs’dir.','E₁ = W + 1,5 · E₂ = W + 5'),
     A('Frekans oranını kullan','Foton enerjisi frekansla doğru orantılıdır; f₂ = 2f₁ ise E₂ = 2E₁.','W + 5 = 2 × (W + 1,5)'),
     A('Denklemi çöz','Parantez açılıp W yalnız bırakılır.','W + 5 = 2W + 3 → W = 2 eV'),
     A('Kontrol et','Bulunan değer iki deneyle de tutarlıdır.','E₁ = 3,5 eV · E₂ = 7 eV = 2 × 3,5')],
 puf='Aynı metalde iki ışık verildiğinde her biri için “E = W + e·Vs” yaz; frekans oranı enerji oranını verir.')
# ===== 07 orta · eşik frekansı altındaki ışık (öncüllü, şekilsiz)
card(7,'Eşik frekansının altındaki ışık','Elektron enerjiyi tek fotondan alır; foton enerjisi yetersizse şiddet ve süre sonucu değiştirmez, frekans yeterli olunca söküm anidir.','Şiddet arttıkça ya da bekledikçe enerjinin birikeceğini düşünmek.','orta','öncüllü',3,'fe-kavram','eşik altı ışıkta şiddet, süre, frekans')
t7=[False,False,True]
q('0007',tipId='fe-kavram',tip=TIPLER['fe-kavram'],z='orta',alt='Işığın Tanecik Modeli',kaz='Fotoelektrik olayın temel özelliklerini ışığın şiddeti, süresi ve frekansıyla ilişkilendirerek yorumlar.',kalip='öncüllü',
 metin='Eşik frekansı f₀ olan bir katot metaline, frekansı f₀’dan küçük olan tek renkli bir ışık gönderiliyor ve metalden hiçbir elektron sökülmediği gözleniyor.\nBuna göre,\nI. Işığın şiddeti yeterince artırılırsa elektronlar sökülmeye başlar.\nII. Işık yüzeye yeterince uzun süre gönderilirse elektronlar enerji biriktirerek sökülmeye başlar.\nIII. Işığın frekansı f₀’dan büyük bir değere çıkarılırsa, şiddet çok az olsa bile elektronlar sökülmeye başlar.\nyargılarından hangileri doğrudur?',
 sekil=None,istenen='Doğru yargılar.',
 ip=['Bir elektronun enerjiyi kaç fotondan aldığını ve şiddetin hangi niceliği belirlediğini düşün.'],
 bilgi=[KAV],
 ad=[A('I. yargıyı sına','Şiddet foton sayısını artırır; her foton ise elektron sökmeye yetmeyecek enerjidedir.','I yanlış'),
     A('II. yargıyı sına','Elektron enerjiyi tek bir fotondan alır; farklı fotonların enerjileri birikmez.','II yanlış'),
     A('III. yargıyı sına','f > f₀ olunca tek foton bile elektronu söker; şiddet yalnız elektron sayısını belirler.','III doğru')],
 puf='Elektron enerjiyi kaç fotondan alır? Önce bunu belirle.',
 **onc(t7,['her fotonun enerjisi eşik enerjisinden küçük kaldığı için şiddet artsa da elektron sökülmez','elektron enerjiyi tek bir fotondan alır ve enerji birikmez','frekansı f₀’dan büyük ışığın her fotonu tek başına elektron sökebilir'],0))
# ===== 08 orta · ters gerilimli devrede anota ulaşan elektron
card(8,'Ters gerilimli devre','Ters bağlı üreteç elektrona e·V kadar iş yapar; anota ulaşan elektronun kinetik enerjisi Ek,maks − e·V olur.','Üretecin yönünü karıştırıp kinetik enerjiye eklemek; akımın kesildiğini varsaymak.','orta','şekilli',4,'fe-devre','ters bağlı üretecin anota ulaşan elektrona etkisi')
lam8=3100; E8=Fr(HC,lam8); W8=Fr(5,2); K8=E8-W8; V8=1; ans8=K8-V8
assert E8==4 and K8==Fr(3,2) and K8>V8 and ans8==Fr(1,2) and K8+V8==Fr(5,2)
def devre(cx=0,cy=0,V='1 V',pol=True):
    o=tube(cx,cy,lab=False)
    o.append(N(cx-.62,cy-1.3,'katot','font=\\small')); o.append(N(cx+.62,cy-1.3,'anot','font=\\small'))
    o.append(AR((cx-2.3,cy+1.25),(cx-.58,cy+.32),'thick,vurgu')); o.append(N(cx-2.05,cy+1.52,'ışık','font=\\small'))
    y=cy-2.1
    o.append(D((cx-.5,cy-.3),(cx-1.7,cy-.3))); o.append(D((cx-1.7,cy-.3),(cx-1.7,y))); o.append(D((cx-1.7,y),(cx-1.1,y)))
    o.append(f'\\draw[thick] ({cx-.8:.2f},{y:.2f}) circle (.3); '+N(cx-.8,y,'A','font=\\small'))
    o.append(D((cx-.5,y),(cx+.55,y)))
    o.append(D((cx+.55,y-.28),(cx+.55,y+.28),'very thick')); o.append(D((cx+.78,y-.15),(cx+.78,y+.15),'very thick'))
    o.append(D((cx+.78,y),(cx+1.7,y))); o.append(D((cx+1.7,y),(cx+1.7,cy-.3))); o.append(D((cx+1.7,cy-.3),(cx+.5,cy-.3)))
    o.append(N(cx+.42,y+.42,'+','font=\\small')); o.append(N(cx+.92,y+.42,'$-$','font=\\small')); o.append(N(cx+.68,y-.45,V,'font=\\small'))
    return o
SK=tikz(devre())
q('0008',tipId='fe-devre',tip=TIPLER['fe-devre'],z='orta',alt='Fotoelektrik Devre',kaz='Ters gerilim uygulanan fotoelektrik devresinde anota ulaşan elektronların maksimum kinetik enerjisini hesaplar.',kalip='şekilli',
 metin='Eşik enerjisi 2,5 eV olan katoda dalga boyu 3100 Å olan tek renkli ışık gönderiliyor. Katot ile anot arasına, şekildeki gibi gerilimi verilen bir üreteç bağlanmıştır. (hc = 12400 eV·Å)\nBuna göre, anoda ulaşan fotoelektronların sahip olabileceği maksimum kinetik enerji kaç eV’tur?',
 sekil=SK,dogru=ans8,yan=[(4,'Anoda ulaşan elektronun enerjisini foton enerjisine eşit almış; eşik enerjisini ve ters gerilimi hesaba katmamış.','dikkat'),(1,'Anoda ulaşan elektronun kinetik enerjisini ters gerilime (1 V) eşit almış.','bilgi'),(Fr(3,2),'Üretecin etkisini hesaba katmayıp katottan kopan elektronların kinetik enerjisini yazmış.','dikkat'),(Fr(5,2),'Ters bağlı üretecin elektrona kazandırdığını sanıp kinetik enerjiye eklemiş: 1,5 + 1.','bilgi')],
 istenen='Anoda ulaşan fotoelektronların maksimum kinetik enerjisi (eV).',
 ip=['Üretecin kutuplarına bakarak elektronun katottan anoda giderken enerjisinin nasıl değiştiğini belirle.'],
 bilgi=[FE,DEV],
 ad=[A('Foton enerjisini bul','Dalga boyu Å cinsinden olduğundan hc = 12400 eV·Å kullanılır.','E = 12400 ÷ 3100 = 4 eV'),
     A('Katottan kopan en hızlı elektron','Ek,maks, foton enerjisi eksi eşik enerjisidir.','Ek,maks = 4 − 2,5 = 1,5 eV'),
     A('Üretecin yönünü belirle','Uzun çubuk (+) katot tarafındadır; anot katoda göre negatiftir ve elektronlar yavaşlar.','Ters gerilim = 1 V'),
     A('Anottaki enerjiyi hesapla','Elektron e·V = 1 eV kaybeder; 1 < 1,5 olduğundan akım geçer.','1,5 − 1 = 0,5 eV')],
 puf='Ters bağlı üretecin gerilimi V ise anoda ulaşan en hızlı elektronun enerjisi Ek,maks − e·V’dir; üretecin yönünü pil sembolünden oku.')
# ===== 09 kolay · foton momentumu dalga sayısından
card(9,'Dalga biçiminden foton momentumu','Aynı uzunluktaki bölgede daha çok dalga varsa dalga boyu daha küçüktür; p = h ÷ λ olduğundan momentum büyür.','Momentumu dalga boyuyla doğru orantılı sanmak.','kolay','şekilli',3,'fe-foton','dalga sayısından momentum oranı')
nK,nM=2,5; r9=Fr(nM,nK); assert r9==Fr(5,2) and Fr(nK,nM)==Fr(2,5) and Fr(nM-nK,nK)==Fr(3,2) and r9**2==Fr(25,4)
def wave(y,n,L=6.0,A_=.32,o='thick,vurgu'):
    return f'\\draw[{o},domain=0:{L},samples=110,smooth,variable=\\x] plot ({{\\x}},{{{y}+{A_}*sin(360*\\x*{n}/{L})}});'
o=[wave(1.2,nK),wave(0,nM),N(-.45,1.2,'K','font=\\small\\bfseries'),N(-.45,0,'M','font=\\small\\bfseries')]
for x in (0,6): o.append(D((x,-.55),(x,1.95),'dashed,gray'))
o.append('\\draw[thin,{Stealth[length=1.8mm]}-{Stealth[length=1.8mm]}] (0,-.8) -- (6,-.8);'); o.append(N(3,-1.08,'aynı uzunluktaki bölge','font=\\scriptsize'))
SK=tikz(o)
q('0009',tipId='fe-foton',tip=TIPLER['fe-foton'],z='kolay',alt='Foton Momentumu',kaz='Dalga boyu ile foton momentumu arasındaki ters orantıyı kullanarak momentum oranını bulur.',kalip='şekilli',
 metin='Boşlukta yayılan K ve M ışınlarının aynı uzunluktaki bir bölgedeki dalga biçimleri şekilde verilmiştir.\nBuna göre, M ışınındaki bir fotonun momentumunun büyüklüğü, K ışınındaki bir fotonun momentumunun büyüklüğünün kaç katıdır?',
 sekil=SK,dogru=r9,yan=[(Fr(2,5),'Momentumu dalga boyuyla doğru orantılı sanıp oranı ters yazmış: 2 ÷ 5.','bilgi'),(Fr(3,2),'Dalga sayıları farkını K’nin dalga sayısına oranlamış: (5 − 2) ÷ 2.','islem'),(5,'M ışınındaki dalga sayısını oran olarak yazmış, K’nin sayısına bölmemiş.','dikkat'),(Fr(25,4),'Dalga sayısı oranının karesini almış (2,5²); momentumu enerji gibi karesiyle orantılı sanmış.','bilgi')],
 istenen='pM ÷ pK oranı.',
 ip=['Aynı uzunlukta kaç dalga olduğuna bakarak dalga boyları arasındaki oranı bul; momentum ile dalga boyu arasındaki ilişkiyi hatırla.'],
 bilgi=[FOT],
 ad=[A('Dalga boylarını karşılaştır','Aynı uzunlukta K’de 2, M’de 5 dalga vardır; dalga sayısı dalga boyuyla ters orantılıdır.','λK ÷ λM = 5 ÷ 2'),
     A('Momentum bağıntısını yaz','Foton momentumu dalga boyuyla ters orantılıdır.','p = h ÷ λ'),
     A('Oranı bul','Dalga boyu oranının tersi momentum oranını verir.','pM ÷ pK = λK ÷ λM = 2,5')],
 puf='Foton momentumu p = h ÷ λ olduğundan dalga boyu küçüldükçe momentum büyür: aynı uzunlukta daha çok dalga varsa momentum daha büyüktür.')
# ===== 10 orta · aynı güçlü iki ışık (öncüllü, şekilsiz)
card(10,'Eşit güçlü ışıklarda foton sayısı ve kuvvet','Güç eşitken dalga boyu büyük ışıkta foton enerjisi küçük, foton sayısı büyüktür; tam soğurmada kuvvet yalnız P ÷ c ile belirlenir.','Foton enerjisi küçük olan ışığın daha az kuvvet uyguladığını sanmak.','orta','öncüllü',3,'fe-foton','eşit güçlü iki ışıkta enerji, sayı, kuvvet')
lK,lL=1,2; EK10=Fr(1,lK); EL10=Fr(1,lL); NK=1/EK10; NL=1/EL10; assert EK10==2*EL10 and NL==2*NK and (EK10*NK==EL10*NL)
t10=[False,True,True]
q('0010',tipId='fe-foton',tip=TIPLER['fe-foton'],z='orta',alt='Foton Momentumu',kaz='Aynı güçlü iki ışık için foton enerjisi, foton sayısı ve ışınım kuvvetini karşılaştırır.',kalip='öncüllü',
 metin='Boşlukta yayılan, eşit güçte ve tek renkli K ve L ışık demetlerinden K’nin dalga boyu λ, L’nin dalga boyu 2λ’dır. Demetlerin her biri, kendisine dik duran aynı tam soğurucu yüzeye ayrı ayrı gönderiliyor ve ışığın tamamı yüzeye ulaşıyor.\nBuna göre,\nI. K ışığındaki bir fotonun enerjisi, L ışığındaki bir fotonun enerjisinin yarısıdır.\nII. Birim zamanda yüzeye çarpan foton sayısı L ışığında daha fazladır.\nIII. Demetlerin yüzeye uyguladığı kuvvetlerin büyüklükleri eşittir.\nyargılarından hangileri doğrudur?',
 sekil=None,istenen='Doğru yargılar.',
 ip=['Güç sabitken foton sayısının foton enerjisiyle, kuvvetin ise saniyede aktarılan momentumla nasıl ilişkili olduğunu düşün.'],
 bilgi=[FOT],
 ad=[A('Foton enerjilerini karşılaştır','Dalga boyu küçük olan ışığın fotonu daha enerjilidir.','E_K = 2E_L → I yanlış'),
     A('Foton sayılarını karşılaştır','N = P ÷ E ve P eşit olduğundan enerjisi küçük olan L’de foton sayısı iki kat büyüktür.','N_L = 2N_K → II doğru'),
     A('Kuvvetleri karşılaştır','Tam soğurulan ışıkta saniyede aktarılan toplam momentum P ÷ c’dir ve iki demette eşittir.','F_K = F_L = P ÷ c → III doğru')],
 puf='Güç eşitken foton sayısı ve saniyedeki momentum aktarımı neye bağlı olur?',
 **onc(t10,['K’nin fotonu L’ninkinden iki kat enerjilidir','güç eşit olduğundan fotonların enerjisi küçük olan L ışığında foton sayısı daha fazladır','tam soğurulan ışıkta saniyede aktarılan momentum P ÷ c olduğundan kuvvetler eşittir'],3))
# ===== 11 orta · Compton saçılması yargıları (öncüllü)
card(11,'Compton saçılması yargıları','Saçılan foton enerji kaybeder (λ′ > λ), elektron kinetik enerji kazanır; enerji ve vektörel momentum korunur.','Saçılan fotonun hızının da azaldığını düşünmek; enerji korunumunu Compton olayına uygulamamak.','orta','öncüllü',3,'fe-compton','saçılma sonrası nicelikler')
t11=[True,True,True]
q('0011',tipId='fe-compton',tip=TIPLER['fe-compton'],z='orta',alt='Compton Saçılması',kaz='Compton saçılmasında dalga boyu, enerji ve momentum korunumuna ilişkin yargıları değerlendirir.',kalip='öncüllü',
 metin='Dalga boyu λ olan bir X-ışını fotonu, durgun ve serbest kabul edilen bir elektronla çarpışıyor. Çarpışmadan sonra foton λ′ dalga boyuyla saçılıyor, elektron ise hareket etmeye başlıyor.\nBuna göre,\nI. λ′ > λ’dır.\nII. Gelen fotonun enerjisi, saçılan fotonun enerjisi ile elektronun kinetik enerjisinin toplamına eşittir.\nIII. Saçılan foton ile elektronun momentumlarının vektörel toplamı, gelen fotonun momentumuna eşittir.\nyargılarından hangileri doğrudur?',
 sekil=None,istenen='Doğru yargılar.',
 ip=['Çarpışmada hangi niceliklerin korunduğunu ve elektronun enerji kazanmasının fotonu nasıl etkilediğini düşün.'],
 bilgi=[COM],
 ad=[A('Dalga boyunu yorumla','Foton enerjisinin bir kısmını elektrona verir; enerjisi azalan fotonun dalga boyu büyür.','E′ < E → λ′ > λ → I doğru'),
     A('Enerji korunumunu yaz','Elektron başlangıçta durgun olduğundan başlangıçtaki enerji yalnız fotona aittir.','E = E′ + Ek,e → II doğru'),
     A('Momentum korunumunu yaz','Sisteme dış kuvvet etki etmediğinden toplam momentum vektörel olarak korunur.','p⃗ = p⃗′ + p⃗ₑ → III doğru')],
 puf='Çarpışmada hangi niceliklerin korunduğunu düşün.',
 **onc(t11,['saçılan fotonun enerjisi azaldığından dalga boyu büyür','foton enerjisinin bir kısmı elektronun kinetik enerjisine dönüşür ve toplam enerji korunur','dış kuvvet olmadığından toplam momentum vektörel olarak korunur'],4))
# ===== 12 orta · saçılma açısına göre dalga boyu sıralaması
card(12,'Saçılma açısı ve dalga boyu','Dalga boyu artışı saçılma açısına (1 − cosθ ile) bağlıdır; gelen foton yönünde (0°) saçılan fotonda artış sıfırdır.','Dalga boyu artışını sinθ ile ya da 1 + cosθ ile orantılı sanmak.','orta','şekilli',3,'fe-compton','farklı açılardaki dedektörler')
aK,aL,aM=120,0,60; dl=lambda a:1-cos(radians(a)); assert dl(aL)<dl(aM)<dl(aK)
assert abs(sin(radians(aK))-sin(radians(aM)))<1e-9 and sin(radians(aL))<sin(radians(aM))
e1=lambda a:1+cos(radians(a)); assert e1(aL)>e1(aM)>e1(aK)
c1=lambda a:abs(cos(radians(a))); assert c1(aL)>c1(aK) and abs(c1(aK)-c1(aM)) <1e-9 or True
assert abs(abs(cos(radians(aK)))-abs(cos(radians(aM))))<1e-9 and abs(cos(radians(aL)))>abs(cos(radians(aM)))
def comp12():
    o=[AR((-2.7,0),(-.12,0))]
    o.append(N(-1.45,.32,'gelen foton','font=\\small')); o.append(DOT((0,0),2.6)); o.append(N(.05,-.38,'hedef','font=\\small,anchor=north west'))
    for nm,a in (('K',aK),('L',aL),('M',aM)):
        x,y=2.2*cos(radians(a)),2.2*sin(radians(a))
        o.append(AR((0.12*cos(radians(a)),.12*sin(radians(a))),(1.78*cos(radians(a)),1.78*sin(radians(a))),'thick'))
        o.append(f'\\node[draw,rounded corners=2pt,inner sep=2pt,align=center,font=\\small] at ({x*1.12:.3f},{y*1.12:.3f}) {{{nm}\\\\[-1pt]\\scriptsize ${a}^\\circ$}};')
    return o
SK=tikz(comp12())
q('0012',tipId='fe-compton',tip=TIPLER['fe-compton'],z='orta',alt='Compton Saçılması',kaz='Compton saçılmasında saçılma açısı ile saçılan fotonun dalga boyu arasındaki ilişkiyi yorumlar.',kalip='şekilli',
 metin='Dalga boyu aynı olan X-ışını fotonları, durgun ve serbest kabul edilen elektronlardan oluşan bir hedefe gönderiliyor. Saçılan fotonlar, gelen fotonların doğrultusuyla şekilde verilen açıları yapan K, L ve M dedektörleriyle ayrı ayrı inceleniyor. Dedektörlere ulaşan fotonların dalga boyları sırasıyla λK, λL ve λM’dir.\nBuna göre, λK, λL ve λM arasındaki ilişki aşağıdakilerden hangisidir?',
 sekil=SK,dogru='λK > λM > λL',yan=[('λL > λM > λK','Dalga boyu artışını (1 + cosθ) ile orantılı sanmış; 0° için en büyük, 120° için en küçük değeri bulmuş.','bilgi'),('λK = λL = λM','Gelen fotonların dalga boyunun aynı olmasından saçılanların da aynı olacağını sanmış.','bilgi'),('λK = λM > λL','Dalga boyu artışını sinθ ile orantılı sanmış; 60° ve 120° için aynı, 0° için sıfır değerini bulmuş.','bilgi'),('λL > λK = λM','Dalga boyu artışını |cosθ| ile orantılı sanmış; 60° ve 120° için aynı, 0° için en büyük değeri bulmuş.','bilgi')],
 sira=['λK = λL = λM','λK = λM > λL','λL > λM > λK','λL > λK = λM','λK > λM > λL'],
 istenen='Saçılan fotonların dalga boyu sıralaması.',
 ip=['Dalga boyundaki artışın saçılma açısına nasıl bağlı olduğunu her dedektör için ayrı ayrı değerlendir.'],
 bilgi=[COM],
 ad=[A('Bağıntıyı yaz','Dalga boyu artışı (h ÷ m·c)(1 − cosθ) ile verilir; sabit çarpan aynıdır.','Δλ ∝ 1 − cosθ'),
     A('Üç açı için hesapla','Kosinüs değerleri yerine konur.','K: 1 − (−0,5) = 1,5 · L: 1 − 1 = 0 · M: 1 − 0,5 = 0,5'),
     A('Sırala','Gelen foton aynı olduğundan λ′ = λ + Δλ sıralaması Δλ sıralamasıyla aynıdır.','λK > λM > λL')],
 puf='Dalga boyundaki artışı saçılma açısıyla ilişkilendiren bağıntıyı her dedektör için ayrı değerlendir.')
# ===== 13 orta · Compton enerji korunumu
card(13,'Compton enerji aktarımı','Gelen ve saçılan fotonun enerjileri dalga boyundan bulunur; aradaki fark durgun elektronun kinetik enerjisidir.','Saçılan fotonun enerjisini elektrona vermek; dalga boyu farkından enerji hesaplamaya çalışmak.','orta','şekilli',4,'fe-compton','dalga boylarından elektronun kinetik enerjisi')
l13a,l13b=Fr(1,10),Fr(31,250); E13a=Fr(HC)/l13a; E13b=Fr(HC)/l13b; Ke13=(E13a-E13b)/1000
assert E13a==124000 and E13b==100000 and Ke13==24 and E13a/1000==124 and E13b/1000==100
pe=(1/float(l13a),-1/float(l13b)); sc13=.23
assert abs(float(l13b-l13a)-0.024)<1e-9 and abs((float(l13b-l13a))/0.02426-1)<0.02  # kabaca 90° saçılma
def comp13():
    o=[AR((-2.6,0),(-.12,0)),DOT((0,0),2.6)]
    o.append(N(-1.35,.62,'gelen foton','font=\\small')); o.append(N(-1.35,.32,'$\\lambda=0{,}1$ Å','font=\\small'))
    o.append(AR((0,.12),(0,.12+1/float(l13b)*sc13),'vurgu,very thick')); o.append(N(.12,1.45,'saçılan foton','font=\\small,anchor=west')); o.append(N(.12,1.15,'$\\lambda\'=0{,}124$ Å','font=\\small,anchor=west'))
    o.append(AR((.1,-.08),(.1+pe[0]*sc13,-.08+pe[1]*sc13),'thick')); o.append(N(2.0,-.7,'elektron','font=\\small,anchor=west'))
    o.append(N(-.2,-.5,'durgun elektron','font=\\small,anchor=north east'))
    return o
SK=tikz(comp13())
q('0013',tipId='fe-compton',tip=TIPLER['fe-compton'],z='orta',alt='Compton Saçılması',kaz='Compton saçılmasında foton enerjilerinin farkından elektronun kazandığı kinetik enerjiyi hesaplar.',kalip='şekilli',
 metin='Bir X-ışını fotonu, durgun ve serbest kabul edilen bir elektronla çarpışarak şekildeki gibi saçılıyor. Gelen ve saçılan fotonların dalga boyları şekilde verilmiştir. (hc = 12400 eV·Å)\nBuna göre, çarpışmada elektronun kazandığı kinetik enerji kaç keV’tur?',
 sekil=SK,dogru=24,yan=[(Fr(12,5),'Dalga boyunu keV’e çevirirken ondalık virgülü bir basamak kaydırmış: 24 yerine 2,4.','islem'),(100,'Saçılan fotonun enerjisini elektronun kinetik enerjisi sanmış.','bilgi'),(124,'Gelen fotonun enerjisinin tamamının elektrona aktarıldığını düşünmüş.','bilgi'),(224,'İki fotonun enerjisini toplamış: 124 + 100.','islem')],
 istenen='Elektronun kinetik enerjisi (keV).',
 ip=['Her fotonun enerjisini dalga boyundan bul; elektron başlangıçta durgun olduğuna göre enerji korunumunu yaz.'],
 bilgi=[FE,COM],
 ad=[A('Gelen fotonun enerjisi','E = hc ÷ λ; dalga boyu Å cinsinden alınır.','E = 12400 ÷ 0,1 = 124000 eV = 124 keV'),
     A('Saçılan fotonun enerjisi','Aynı bağıntı saçılan foton için de uygulanır.','E′ = 12400 ÷ 0,124 = 100000 eV = 100 keV'),
     A('Enerji korunumunu yaz','Elektron başlangıçta durgun olduğundan kinetik enerjisi fotonun kaybettiği enerjidir.','124 = 100 + Ek,e'),
     A('Elektronun enerjisini bul','Fark alınır.','Ek,e = 24 keV')],
 puf='Çarpışmada enerji korunur; elektron başlangıçta durgundur.')
# ===== 14 orta · de Broglie tablo (öncüllü)
card(14,'Momentum ve dalga boyu tablosu','De Broglie dalga boyu momentumla ters orantılıdır; momentumlar eşitse dalga boyları da eşittir, kinetik enerji ise p² ÷ 2m ile bulunur.','Kütle ya da hız tek başına büyük olan parçacığın dalga boyunu küçük sanmak.','orta','tablo',4,'fe-debroglie','farklı kütle ve hızlı parçacıklar')
mv={'K':(1,4),'L':(2,1),'M':(4,1)}; pp={k:m*v for k,(m,v) in mv.items()}; kk={k:Fr(m*v*v,2) for k,(m,v) in mv.items()}
assert pp['K']==pp['M']==4 and pp['L']==2 and Fr(pp['K'],pp['L'])==2 and kk['K']==8 and kk['M']==2 and kk['K']>kk['M']
t14=[False,True,False]
SK=tablo_svg(['Parçacık','Kütle','Hız'],[['K','m','4v'],['L','2m','v'],['M','4m','v']])
q('0014',tipId='fe-debroglie',tip=TIPLER['fe-debroglie'],z='orta',alt='De Broglie Dalga Boyu',kaz='Kütle ve hızı verilen parçacıkların de Broglie dalga boylarını ve kinetik enerjilerini karşılaştırır.',kalip='tablo',
 metin='Aşağıdaki tabloda K, L ve M parçacıklarının kütleleri ile hızları verilmiştir. Hızlar ışık hızından çok küçüktür.\nBuna göre,\nI. M’nin de Broglie dalga boyu, K’ninkinden büyüktür.\nII. L’nin de Broglie dalga boyu, K’ninkinin iki katıdır.\nIII. K’nin kinetik enerjisi, M’ninkinden küçüktür.\nyargılarından hangileri doğrudur?',
 sekil=SK,istenen='Doğru yargılar.',
 ip=['Her parçacığın momentumunu m·v çarpımından bul; dalga boyunu momentumla, kinetik enerjiyi ½·m·v² ile ilişkilendir.'],
 bilgi=[DB],
 ad=[A('Momentumları hesapla','p = m·v çarpımı tablodan okunur.','pK = 4mv · pL = 2mv · pM = 4mv'),
     A('Dalga boylarını karşılaştır','λ = h ÷ p olduğundan K ve M’nin dalga boyları eşittir, L’ninki momentumun yarısı nedeniyle iki kat büyüktür.','λM = λK → I yanlış · λL = 2λK → II doğru'),
     A('Kinetik enerjileri hesapla','Ek = ½·m·v² bağıntısı kullanılır.','EK = ½ × m × 16v² = 8mv² · EM = ½ × 4m × v² = 2mv²'),
     A('III. yargıyı değerlendir','K’nin kinetik enerjisi M’ninkinden büyüktür.','III yanlış')],
 puf='Dalga boyunu momentumla, kinetik enerjiyi kütle ve hızla ilişkilendir.',
 **onc(t14,['K ve M’nin momentumları eşit (4mv) olduğundan dalga boyları da eşittir','L’nin momentumu K’ninkinin yarısı olduğundan dalga boyu iki katıdır','K’nin kinetik enerjisi 8mv², M’ninki 2mv²’dir; K’ninki daha büyüktür'],1))
# ===== 15 zor · Vs–f grafiğinden eşik dalga boyu
card(15,'Vs–f grafiğinden eşik dalga boyu','Vs–f doğrusunun eğimi h ÷ e’dir; doğru Vs = 0’a uzatılarak eşik frekansı, W = h·f₀ ile eşik enerjisi ve hc ÷ W ile eşik dalga boyu bulunur.','Verilen noktadaki Vs, eğim ya da Vs farkını eşik enerjisi sanmak.','zor','grafik',5,'fe-grafik','Vs–f doğrusundan eşik dalga boyu')
fa,Va,fb,Vb=7,Fr(4,5),11,Fr(12,5); sl15=(Vb-Va)/(fb-fa); f0_15=fa-Va/sl15; W15=sl15*f0_15; L15=Fr(HC)/W15
assert sl15==Fr(2,5) and f0_15==5 and W15==2 and L15==6200
assert Fr(HC)/sl15==31000 and Fr(HC)/Va==15500 and Fr(HC)/f0_15==2480 and Fr(HC)/(Vb-Va)==7750
SK=ptx('\\begin{axis}[width=7.4cm,height=5.2cm,xmin=0,xmax=12,ymin=0,ymax=3.2,xtick={0,1,2,3,4,5,6,7,8,9,10,11,12},ytick={0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2},grid=both,major grid style={gray!50,thin},tick label style={font=\\scriptsize},axis lines=left,xlabel={$f$ ($10^{14}$ Hz)},ylabel={$V_s$ (V)},label style={font=\\small},'+PGF+']\n\\addplot[thick,vurgu] coordinates {(7,0.8) (11,2.4)};\n\\addplot[only marks,mark=*,mark size=1.8pt] coordinates {(7,0.8) (11,2.4)};\n\\end{axis}')
q('0015',tipId='fe-grafik',tip=TIPLER['fe-grafik'],z='zor',alt='Vs–f Grafiği',kaz='Durdurma potansiyeli – frekans doğrusundan metalin eşik enerjisini ve fotoelektron sökebilen en büyük dalga boyunu hesaplar.',kalip='grafik',
 metin='Bir katot metaline gönderilen tek renkli ışığın frekansı (f) ile bu frekanstaki fotoelektrik akımı sıfırlayan ters gerilimin (durdurma potansiyeli, Vs) değişimi deneysel olarak şekildeki doğru parçası biçiminde elde edilmiştir. (hc = 12400 eV·Å)\nBuna göre, bu metalden fotoelektron sökebilen ışığın dalga boyu en çok kaç Å olabilir?',
 sekil=SK,dogru=L15,yan=[(31000,'Doğrunun eğimini (0,4) eşik enerjisi alıp dalga boyunu 12400 ÷ 0,4 bulmuş.','bilgi'),(15500,'Grafikteki ilk noktanın durdurma potansiyelini (0,8) eşik enerjisi alıp 12400 ÷ 0,8 bulmuş.','bilgi'),(2480,'Doğruyu uzatıp bulduğu eşik frekansının sayısını (5) eV cinsinden eşik enerjisi alıp 12400 ÷ 5 bulmuş.','dikkat'),(7750,'İki noktadaki durdurma potansiyellerinin farkını (2,4 − 0,8 = 1,6) eşik enerjisi alıp 12400 ÷ 1,6 bulmuş.','islem')],
 istenen='Fotoelektron sökebilen en büyük dalga boyu (Å).',
 ip=['Doğrunun eğimini bul ve doğruyu Vs = 0 olduğu frekansa kadar uzat; eğimin h ÷ e olduğunu kullan.'],
 bilgi=[DUR,VSF],
 ad=[A('Eğimi hesapla','İki nokta arasındaki Vs değişiminin f değişimine oranıdır.','eğim = (2,4 − 0,8) ÷ (11 − 7) = 0,4 V ÷ 10¹⁴ Hz'),
     A('Eşik frekansını bul','Vs = 0 olduğu frekans eşik frekansıdır; ilk noktadan geriye gidilir.','f₀ = 7 − 0,8 ÷ 0,4 = 5 × 10¹⁴ Hz'),
     A('Eşik enerjisini hesapla','Eğim h ÷ e olduğundan W = h·f₀ = e × eğim × f₀ yazılır.','W = 0,4 × 5 = 2 eV'),
     A('Eşik dalga boyunu bul','Sökülebilmesi için foton enerjisi en az W olmalıdır; dalga boyu en çok hc ÷ W kadardır.','λ₀ = 12400 ÷ 2 = 6200 Å')],
 puf='Doğrunun eğiminin neyi gösterdiğini ve Vs = 0 noktasının neyi verdiğini düşün.')
# ===== 16 zor · iki dalga boyundaki Ek'ten eşik dalga boyu
card(16,'İki dalga boyundan eşik dalga boyu','E ve E′ = E ÷ 2 için Ek değerlerinden foton enerjisi ve W çözülür, eşik dalga boyu hc ÷ W ile λ cinsinden bulunur.','Eşik enerjisini Ek değerlerinin farkı ya da biri sanmak; dalga boyu oranını enerji oranıyla karıştırmak.','zor','tablo',5,'fe-esik','dalga boyu ve Ek tablosundan eşik dalga boyu')
Ea=Fr(6); Wd=2; Ka,Kb=4,1; assert Ea-Wd==Ka and Ea/2-Wd==Kb and Ea/Wd==3 and Ea/(Ka-Kb)==2 and Ea/Ka==Fr(3,2) and Ea/Kb==6 and Ea/Wd/3==1
SK=tablo_svg(['Işığın dalga boyu','Ek,maks (eV)'],[['λ','4'],['2λ','1']])
q('0016',tipId='fe-esik',tip=TIPLER['fe-esik'],z='zor',alt='Eşik Dalga Boyu',kaz='Farklı dalga boylarındaki Ek,maks değerlerinden eşik enerjisini ve eşik dalga boyunu bulur.',kalip='tablo',
 metin='Bir katot metaline dalga boyları λ ve 2λ olan tek renkli ışıklar ayrı ayrı gönderiliyor. Sökülen elektronların maksimum kinetik enerjileri aşağıdaki tabloda verilmiştir.\nBuna göre, bu metalin eşik dalga boyu λ’nın kaç katıdır?',
 sekil=SK,dogru=3,yan=[(1,'Gönderilen ışıklardan birinin dalga boyunu (λ) eşik dalga boyu sanmış.','dikkat'),(Fr(3,2),'Eşik enerjisini birinci ışıktaki kinetik enerji (4 eV) sanıp λ₀ = 6 ÷ 4 bulmuş.','bilgi'),(2,'Eşik enerjisini iki kinetik enerjinin farkı (3 eV) sanıp λ₀ = 6 ÷ 3 bulmuş.','bilgi'),(6,'Eşik enerjisini ikinci ışıktaki kinetik enerji (1 eV) sanıp λ₀ = 6 ÷ 1 bulmuş.','bilgi')],
 istenen='λ₀ ÷ λ oranı.',
 ip=['λ dalga boylu fotonun enerjisine E dersen 2λ dalga boylu fotonun enerjisinin ne olacağını yaz ve iki Ek değerini E cinsinden ifade et.'],
 bilgi=[FE],
 ad=[A('Foton enerjilerini ilişkilendir','Dalga boyu iki katına çıkınca foton enerjisi yarıya iner.','E₁ = E · E₂ = E ÷ 2'),
     A('İki denklem yaz','Her ışık için Ek,maks = E − W ilişkisi uygulanır.','E − W = 4 · E ÷ 2 − W = 1'),
     A('E ve W’yi bul','İki denklem taraf tarafa çıkarılır.','E ÷ 2 = 3 → E = 6 eV · W = 6 − 4 = 2 eV'),
     A('Eşik dalga boyunu bul','Dalga boyu enerjiyle ters orantılıdır; λ dalga boylu fotonun enerjisi eşik enerjisinin 3 katıdır.','λ₀ ÷ λ = E ÷ W = 6 ÷ 2 = 3')],
 puf='Dalga boyu ve enerji ters orantılı olduğundan eşik dalga boyu oranı λ₀ ÷ λ = E ÷ W olur; önce E ve W’yi iki denklemle bul.')
# ===== 17 zor · frekans artırılınca akım–gerilim grafiği
card(17,'Güç sabitken frekans artışı','Güç sabitken frekans artınca foton sayısı azalır (doygunluk akımı küçülür), foton enerjisi artar (durdurma potansiyeli büyür).','Yalnız enerjinin arttığını düşünüp akımı da artırmak ya da yalnız foton sayısına bakıp durdurma potansiyelini sabit bırakmak.','zor','grafik',4,'fe-akim','güç sabit, frekans artıyor')
orig=(2,2)  # (Is,Vs)
pan={'K':(3,3),'L':(1,2),'M':(3,1),'N':(2,3),'P':(Fr(3,2),3)}
fold=1; fnew=Fr(3,2); Pg=1; Nold=Pg/fold; Nnew=Pg/fnew; assert Nnew<Nold
ok={k:(v[0]<orig[0] and v[1]>orig[1]) for k,v in pan.items()}; assert [k for k,v in ok.items() if v]==['P']
def panel(nm,Is,Vs,x,y):
    return (f'\\begin{{axis}}[at={{({x}cm,{y}cm)}},anchor=south west,width=3.9cm,height=3.5cm,xmin=-4,xmax=1.6,ymin=0,ymax=3.6,xtick={{-3,-2,-1}},ytick={{1,1.5,2,3}},grid=both,major grid style={{gray!35,thin}},axis lines=middle,tick label style={{font=\\small}},title={{\\small {nm}}},title style={{yshift=-2pt}}]\n'
            f'\\addplot[thick,gray,dashed] coordinates {{{plot_iv(*orig)}}};\n\\addplot[thick,vurgu] coordinates {{{plot_iv(Is,Vs)}}};\n\\end{{axis}}')
pp17=[panel('K',*pan['K'],0,9.0),panel('L',*pan['L'],5.2,9.0),panel('M',*pan['M'],0,4.5),panel('N',*pan['N'],5.2,4.5),panel('P',*pan['P'],0,0)]
leg=('\\draw[thick,gray,dashed] (5.6,2.0) -- (6.4,2.0); \\node[anchor=west,font=\\small] at (6.5,2.0) {ilk deney};\n\\draw[thick,vurgu] (5.6,1.2) -- (6.4,1.2); \\node[anchor=west,font=\\small] at (6.5,1.2) {yeni deney};')
SK=ptx('\n'.join(pp17)+'\n'+leg)
q('0017',tipId='fe-akim',tip=TIPLER['fe-akim'],z='zor',alt='Akım–Gerilim Grafiği',kaz='Işığın gücü sabitken frekansı artırıldığında akım–gerilim grafiğinin nasıl değişeceğini foton sayısı ve foton enerjisiyle yorumlar.',kalip='grafik',
 metin='Bir fotoelektrik düzenekte tek renkli ışıkla yapılan ilk deneyin akım–gerilim grafiği kesikli çizgiyle gösterilmiştir. Daha sonra aynı katot kullanılarak ışığın gücü değiştirilmeden yalnız frekansı artırılıyor ve deney tekrarlanıyor. Gelen her foton en çok bir elektron söküyor, sökme verimi frekanstan bağımsızdır ve gerilim yeterince büyük olduğunda sökülen bütün elektronlar anoda ulaşıyor.\nHer panelde düşey eksen akımı, yatay eksen gerilimi (V) göstermektedir.\nBuna göre, yeni deneye ait akım–gerilim grafiği (sürekli çizgi) şekildeki panellerin hangisinde verilmiştir?',
 sekil=SK,dogru='P',yan=[('K','Frekans artınca hem durdurma potansiyelinin hem akımın artacağını düşünmüş; oysa güç sabitken fotonlar daha enerjili olduğundan sayıları azalır.','bilgi'),('L','Frekansın durdurma potansiyelini değiştirdiğini unutup yalnız foton sayısının azalmasını (doygunluk akımının küçülmesini) görmüş.','bilgi'),('M','Frekans artışını foton enerjisinin azalması sanıp durdurma potansiyelini küçültmüş ve akımı artırmış.','bilgi'),('N','Gücün sabit olmasından foton sayısının da sabit kaldığını düşünmüş; durdurma potansiyelinin arttığını doğru bulup doygunluk akımını değiştirmemiş.','bilgi')],
 sira=['K','L','M','N','P'],
 istenen='Yeni deneye ait grafiğin bulunduğu panel.',
 ip=['Güç sabitken fotonların enerjisi artarsa saniyede gelen foton sayısının nasıl değişeceğini düşün; sonra akımın sıfırlandığı gerilimin neye bağlı olduğunu hatırla.'],
 bilgi=[AKIM,FOT],
 ad=[A('Foton enerjisini yorumla','Frekans arttığı için her fotonun enerjisi artar; sökülen elektronların Ek,maks değeri büyür.','f ↑ → Ek,maks ↑ → Vs ↑'),
     A('Foton sayısını yorumla','Güç = (foton sayısı) × (foton enerjisi) sabittir; enerji arttığından saniyede gelen foton sayısı azalır.','N = P ÷ (h·f) ↓ → doygunluk akımı ↓'),
     A('Panelleri ele','Durdurma potansiyeli büyüyen ve doygunluk akımı küçülen panel aranır.','K: akım ↑ · L: Vs sabit · M: Vs ↓ · N: akım sabit · P: Vs ↑, akım ↓'),
     A('Sonuç','Yalnız P panelinde iki değişim birlikte doğrudur.','P')],
 puf='Güç sabitken frekans artarsa foton enerjisi artar (Vs büyür) ama foton sayısı azalır (doygunluk akımı küçülür).')
# ===== 18 zor · aynı gerilimde hızlandırılan parçacıkların de Broglie oranı
card(18,'Hızlandırılmış parçacıkların dalga boyu','Aynı V’de K = qV; p = √(2mK) = √(2mqV) olduğundan λ oranı √(m·q) çarpımının oranının tersidir.','Yalnız kütleyi ya da yalnız yükü hesaba katmak; karekökü unutmak.','zor','şekilli',4,'fe-debroglie','aynı V ile hızlandırılan iki parçacık')
mX,qX,mY,qY=1,1,4,4; KX=qX; KY=qY; pX=math.sqrt(2*mX*KX); pY=math.sqrt(2*mY*KY); lr=pY/pX
assert abs(lr-4)<1e-12 and mY*qY==16*mX*qX and mY/qY==1 and abs(math.sqrt(mY/mX)-2)<1e-12
def acc(y,nm,lab,mq):
    o=[D((0,y-.62),(0,y+.62),'very thick'),D((2.9,y-.62),(2.9,y+.62),'very thick'),N(0,y+.9,'$+$','font=\\small'),N(2.9,y+.9,'$-$','font=\\small')]
    o.append(f'\\draw[thick,fill=vurgu!30] (.32,{y:.2f}) circle (.17);'); o.append(AR((.6,y),(2.0,y),'thick,vurgu'))
    o.append(N(1.45,y+.42,mq,'font=\\small')); o.append(N(-.55,y,nm,'font=\\small\\bfseries'))
    o.append('\\draw[thin,{Stealth[length=1.8mm]}-{Stealth[length=1.8mm]}] (0,'+f'{y-.9:.2f}) -- (2.9,{y-.9:.2f});'); o.append(N(1.45,y-1.15,'$V$','font=\\small'))
    return o
SK=tikz(acc(1.9,'X','','$m,\\ +q$')+acc(-.4,'Y','','$4m,\\ +4q$'))
q('0018',tipId='fe-debroglie',tip=TIPLER['fe-debroglie'],z='zor',alt='De Broglie Dalga Boyu',kaz='Aynı potansiyel farkıyla hızlandırılan iki parçacığın de Broglie dalga boyları oranını kütle ve yükten hesaplar.',kalip='şekilli',
 metin='X ve Y parçacıkları, şekildeki gibi aynı V potansiyel farkı uygulanan levhalar arasında durgun halden hızlandırılıyor. Parçacıkların hızları ışık hızından çok küçüktür.\nBuna göre, levhalar arasından çıkan X ve Y parçacıklarının de Broglie dalga boyları oranı λX ÷ λY kaçtır?',
 sekil=SK,dogru=4,yan=[(Fr(1,4),'Oranı ters yazmış: λY ÷ λX bulmuş.','dikkat'),(1,'Kütlenin ve yükün aynı oranda arttığını görüp etkilerin birbirini götürdüğünü düşünmüş (m ÷ q = sabit).','bilgi'),(2,'Yükün kinetik enerjiyi de dört katına çıkardığını unutup yalnız kütleyi hesaba katmış: λ ∝ 1 ÷ √m.','bilgi'),(16,'Dalga boyunu m·q çarpımıyla ters orantılı alıp karekök almamış.','islem')],
 istenen='λX ÷ λY oranı.',
 ip=['Her parçacığın kazandığı kinetik enerjiyi levhalar arasındaki V cinsinden yaz, sonra momentumu kütle ve kinetik enerjiyle ilişkilendir.'],
 bilgi=[HIZ,DB],
 ad=[A('Kinetik enerjileri bul','Aynı V için kazanılan enerji yükle orantılıdır.','K_X = qV · K_Y = 4qV'),
     A('Momentumları oranla','p = √(2mK) olduğundan momentum √(m·K) ile orantılıdır.','pY ÷ pX = √(4m × 4qV) ÷ √(m × qV) = √16 = 4'),
     A('Dalga boylarını oranla','De Broglie dalga boyu momentumla ters orantılıdır.','λX ÷ λY = pY ÷ pX = 4')],
 puf='Kazanılan kinetik enerjiyi yük ve gerilimden bul, sonra momentuma geç.')
# ===== 19 zor · tam yansıtıcı yüzeye eğik gelen ışığın kuvveti
card(19,'Eğik yansıyan ışığın kuvveti','Birim zamanda gelen momentum P ÷ c; tam yansımada yüzeye dik bileşenin yönü değişir ve kuvvet 2·(P ÷ c)·cosθ olur.','Momentum değişimini p sanmak (2 çarpanı), dik bileşen için cos yerine sin ya da bölme kullanmak.','zor','şekilli',5,'fe-foton','eğik tam yansıma kuvveti')
Pw,cc=3,3*10**8; cs,sn=Fr(4,5),Fr(3,5); Pc=Fr(Pw,cc)*10**9; F19=2*Pc*cs
assert Pc==10 and F19==16 and Pc*cs==8 and 2*Pc*sn==12 and 2*Pc==20 and 2*Pc/cs==25
def yelken():
    s37,c37=sin(radians(37)),cos(radians(37)); o=[D((-2.6,0),(2.6,0),'very thick')]
    for i in range(-10,11): x=i*.25; o.append(D((x,0),(x-.18,-.22),'thin'))
    o.append(D((0,0),(0,2.7),'dashed,gray')); o.append(AR((-2.5*s37,2.5*c37),(-.06*s37,.06*c37),'thick,vurgu')); o.append(AR((.06*s37,.06*c37),(2.5*s37,2.5*c37),'thick,vurgu'))
    for sg in (-1,1):
        o.append(f'\\draw[thin] (0,.95) arc (90:{90+sg*37}:.95);'); o.append(N(sg*.38,1.2,'$37^\\circ$','font=\\scriptsize'))
    o.append(N(-2.2,2.3,'$P=3$ W','font=\\small')); o.append(N(1.55,-.62,'tam yansıtıcı yüzey','font=\\small'))
    return o
SK=tikz(yelken())
q('0019',tipId='fe-foton',tip=TIPLER['fe-foton'],z='zor',alt='Işınım Basıncı',kaz='Tam yansıtıcı yüzeye eğik gelen ışığın uyguladığı kuvveti foton momentumunun değişiminden hesaplar.',kalip='şekilli',
 metin='Boşlukta yayılan tek renkli bir ışık demeti, şekildeki gibi tam yansıtıcı düzlem bir yüzeye gelip aynı açıyla yansıyor. Demetin gücü şekilde verilmiştir. Işığın boşluktaki hızı 3 × 10⁸ m/s, sin37° = 0,6 ve cos37° = 0,8’dir (1 nN = 10⁻⁹ N).\nBuna göre, ışık demetinin yüzeye uyguladığı kuvvetin büyüklüğü kaç nN’dir?',
 sekil=SK,dogru=16,yan=[(8,'Yansımada momentum değişiminin 2p yerine p olduğunu sanmış: (P ÷ c) × cos37°.','bilgi'),(12,'Yüzeye dik bileşen için cos37° yerine sin37° kullanmış: 2 × (P ÷ c) × 0,6.','islem'),(20,'Dik bileşeni almayı unutup momentum değişimini 2P ÷ c olarak yazmış.','dikkat'),(25,'Dik bileşeni bulmak için cos37° ile çarpmak yerine bölmüş: 2 × (P ÷ c) ÷ 0,8.','islem')],
 istenen='Işığın yüzeye uyguladığı kuvvet (nN).',
 ip=['Saniyede gelen toplam momentumu güçten bul; yansımada hangi bileşenin değiştiğini düşün.'],
 bilgi=[FOT],
 ad=[A('Saniyedeki momentumu bul','Gelen ışığın saniyedeki momentumu P ÷ c’dir.','P ÷ c = 3 ÷ (3 × 10⁸) = 10⁻⁸ N = 10 nN'),
     A('Hangi bileşen değişir','Tam yansımada yüzeye paralel bileşen korunur, yüzeye dik bileşen yön değiştirir.','dik bileşen: (P ÷ c) × cos37° = 8 nN'),
     A('Momentum değişimini yaz','Dik bileşen +’dan −’ye döndüğü için değişim iki katıdır.','Δ(p dik) = 2 × 8 = 16 nN'),
     A('Kuvveti bul','Yüzeye uygulanan kuvvet, saniyedeki momentum değişimine eşittir.','F = 16 nN')],
 puf='Saniyedeki momentum değişiminin yüzeye dik bileşenine bak.')
# ===== 20 zor · fotoelektron ve de Broglie
card(20,'Fotoelektronun dalga boyu','Ek,maks = hf − W ile sökülen elektronun kinetik enerjisi bulunur; de Broglie dalga boyu λ = h ÷ √(2mEk) ile Ek’nın karekökü ile ters orantılıdır.','Elektronun dalga boyunu fotonun dalga boyuyla karıştırmak; karekökü unutmak.','orta','şekilli',4,'fe-debroglie','fotoelektronların de Broglie dalga boyları oranı')
E20a,E20b,W20=Fr(5,2),Fr(4),Fr(2); K20a=E20a-W20; K20b=E20b-W20
assert K20a==Fr(1,2) and K20b==2 and math.isqrt(int(K20b/K20a))**2==K20b/K20a and math.isqrt(int(K20b/K20a))==2 and E20b/E20a==Fr(8,5)
assert K20b/K20a==4 and K20a/K20b==Fr(1,4)
def ph(x,lab,ttl):
    o=tube(x,0)
    o.append(AR((x-2.1,1.25),(x-.58,.32),'thick,vurgu')); o.append(N(x-1.55,1.85,lab,'font=\\small,align=center')); o.append(N(x,-1.35,ttl,'font=\\small\\bfseries'))
    return o
SK=tikz(ph(0,'foton enerjisi\\\\$2{,}5$ eV','Deney I')+ph(4.4,'foton enerjisi\\\\$4$ eV','Deney II'))
q('0020',tipId='fe-debroglie',tip=TIPLER['fe-debroglie'],z='orta',alt='De Broglie Dalga Boyu',kaz='Fotoelektrik olayda sökülen elektronların maksimum kinetik enerjilerinden de Broglie dalga boyları oranını bulur.',kalip='şekilli',
 metin='Eşik enerjisi 2 eV olan bir katot levhasına, foton enerjileri şekilde verilen tek renkli ışıklarla iki ayrı deney yapılıyor. Her deneyde sökülen elektronlardan maksimum kinetik enerjili olanların de Broglie dalga boyları, Deney I’de λ₁, Deney II’de λ₂’dir. Elektronların hızları ışık hızından çok küçüktür.\nBuna göre, λ₁ ÷ λ₂ oranı kaçtır?',
 sekil=SK,dogru=2,yan=[(Fr(1,4),'Dalga boyunu kinetik enerjiyle doğru orantılı alarak λ₁ ÷ λ₂ = 0,5 ÷ 2 bulmuş.','bilgi'),(Fr(1,2),'Dalga boyunu √Ek ile doğru orantılı alıp oranı ters yazmış: √(0,5 ÷ 2).','dikkat'),(Fr(8,5),'Elektronların değil, fotonların dalga boyları oranını bulmuş: 4 ÷ 2,5.','bilgi'),(4,'Dalga boyunu Ek ile ters orantılı alıp karekök almamış: 2 ÷ 0,5.','islem')],
 istenen='λ₁ ÷ λ₂ oranı.',
 ip=['Her deney için sökülen en hızlı elektronun kinetik enerjisini bul; dalga boyunun kinetik enerjiyle ilişkisini momentum üzerinden kur.'],
 bilgi=[FE,DB],
 ad=[A('Kinetik enerjileri bul','Her deneyde foton enerjisinden eşik enerjisi çıkarılır.','Ek₁ = 2,5 − 2 = 0,5 eV · Ek₂ = 4 − 2 = 2 eV'),
     A('Dalga boyu bağıntısını yaz','Aynı parçacık (elektron) için λ ∝ 1 ÷ √Ek.','λ = h ÷ √(2mEk)'),
     A('Oranı kur','Kinetik enerjiler oranının karekökünün tersi alınır.','λ₁ ÷ λ₂ = √(Ek₂ ÷ Ek₁) = √(2 ÷ 0,5)'),
     A('Sonucu bul','Karekök içi 4’tür.','λ₁ ÷ λ₂ = 2')],
 puf='Aynı tür parçacıkta de Broglie dalga boyu, kinetik enerjinin karekökü ile ters orantılıdır; kinetik enerji dokuz katına çıkarsa dalga boyu üçte birine iner.')
# ===== yaz
for qq in P.ANA: qq['kardes']=None
SC='/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/fotoelektrik'
P.yaz(os.path.join(GD,'fotoelektrik-1.json'),os.path.join(SC,'bos-fotoelektrik.json'))
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu='afiz|Fotoelektrik Olay ve Compton Olayı'))['kartlar'].append(c['id'])
json.dump(dict(konu='Fotoelektrik Olay ve Compton Olayı',surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2018–2026 Fizik (yalnız mantık), 345 AYT Fizik, Bilgi Sarmal AYT Fizik, MEB 12. sınıf fizik.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','affotoelektrik.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
