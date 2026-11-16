"""TYT Fizik · Sıvıların Kaldırma Kuvveti (2. paket, hafif mod) · 16 soru, kardeş yok, ipucu 1.
Şekiller TikZ (cizim.tikz_svg); koordinatlar ve sayılar Python'da hesaplanır, her cevap/çeldirici assert edilir.
Öncüllü sorularda her öncülün doğru/yanlış değeri TEK yerde (ONC listesi) tanımlanır; anahtar, adımlar ve çeldirici açıklamaları oradan üretilir."""
import sys,os,json
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,GD)
import _hafif as H
from _hafif import *
from cizim import tikz_svg
P=Parti('kaldirmaiki','Sıvıların Kaldırma Kuvveti','fiz|Sıvıların Kaldırma Kuvveti',ders='TYT Fizik',idon='tytfiz')
H.KONU='Sıvıların Kaldırma Kuvveti'
KY='ÖSYM 2018–2026 TYT Fizik soruları (yalnız mantık) · MEB 10. sınıf fizik'
ALT='Kaldırma Kuvveti'
def kartla(n,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(f'K-FZKK2-{n:02d}',alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)
def q(no,ad,**k):
    assert len(k['ip'])==1
    mk(P,no,ad=ad,adim=len(ad),alt=ALT,**k)
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
def fig(*parts): return tikz_svg(HEAD+'\n'.join(parts)+TAIL)
# ---------- çizim yardımcıları (cm) ----------
SIV='vurgu!15'
def kap(x,w,h,lv,col=SIV,tas=None):
    """Kap; tas=(boy) verilirse sağ duvar sıvı seviyesinde biter ve boru çıkar."""
    s=f'\\fill[{col}] ({x},0) rectangle ({x+w},{lv});\n'
    if tas: s+=f'\\draw[thick] ({x},{h}) -- ({x},0) -- ({x+w},0) -- ({x+w},{lv}) -- ({x+w+tas},{lv-.25});'
    else: s+=f'\\draw[thick] ({x},{h}) -- ({x},0) -- ({x+w},0) -- ({x+w},{h});'
    return s
def blk(x,y,w,h,t='',fill='gray!40'):
    s=f'\\draw[thick,fill={fill}] ({x},{y}) rectangle ({x+w},{y+h});'
    if t: s+=f'\\node at ({x+w/2},{y+h/2}) {{{t}}};'
    return s
def lvl(x1,x2,y): return f'\\draw[densely dashed] ({x1},{y}) -- ({x2},{y});'
def dino(x,yt,oku):
    return (f'\\draw[thick,fill=white] ({x-.2},{yt-1.4}) rectangle ({x+.2},{yt});\\draw ({x},{yt}) -- ({x},{yt+.3});\\draw ({x},{yt+.4}) circle (.1);'
            f'\\draw ({x},{yt-1.4}) -- ({x},{yt-1.75});\\node[right] at ({x+.28},{yt-.7}) {{{oku}}};')
def yay(x,yt,yb,n=7,w=.28):
    pts=[(x,yt)]
    for i in range(1,2*n+1): pts.append((x+(w if i%2 else -w),yt-(yt-yb)*i/(2*n+1)))
    pts.append((x,yb))
    return '\\draw[thick] '+' -- '.join(f'({a:.3f},{b:.3f})' for a,b in pts)+';'
def olc(x,y1,y2,t,sol=True):
    """dikey ölçü oku"""
    return (f'\\draw[<->,thin] ({x},{y1}) -- ({x},{y2});\\node[{"left" if sol else "right"}] at ({x},{(y1+y2)/2}) {{{t}}};')
def zemin(x1,x2,y=0): return f'\\fill[pattern=north east lines,pattern color=gray] ({x1},{y-.2}) rectangle ({x2},{y});\\draw ({x1},{y}) -- ({x2},{y});'
# ---------- öncüllü üretici ----------
ROM=['I','II','III']
SETN={(0,):'Yalnız I',(1,):'Yalnız II',(2,):'Yalnız III',(0,1):'I ve II',(0,2):'I ve III',(1,2):'II ve III',(0,1,2):'I, II ve III'}
def onc(giris,ifadeler,sira,kok):
    """ifadeler: [(metin, dogru_mu, aciklama, yanilgi)]; yanilgi: o öncülü ters değerlendiren öğrencinin düşüncesi.
    sira: beş şık (alışılmış sırada, SETN değerleri). Döner: (metin, dogru, yan, adimlar)"""
    tr=tuple(i for i,x in enumerate(ifadeler) if x[1]); dog=SETN[tr]; assert dog in sira and len(sira)==5
    inv={v:k for k,v in SETN.items()}
    metin=giris+'\n'+'\n'.join(f'{ROM[i]}. {x[0]}' for i,x in enumerate(ifadeler))+'\n'+kok
    yan=[]
    for s in sira:
        if s==dog: continue
        k=set(inv[s]); parca=[]
        for i in sorted(k-set(tr)): parca.append(f'{ROM[i]}. öncülünü doğru sanmış: {ifadeler[i][3]}')
        for i in sorted(set(tr)-k): parca.append(f'{ROM[i]}. öncülünü yanlış sanmış: {ifadeler[i][3]}')
        yan.append((s,' '.join(parca),'bilgi'))
    adim=[A(f'{ROM[i]}. öncülü',x[2],f'{ROM[i]}: {"doğru" if x[1] else "yanlış"}') for i,x in enumerate(ifadeler)]
    return metin,dog,yan,adim
KAL=B('Kaldırma kuvveti','F = d_sıvı × V_batan × g; cismin yerini tuttuğu sıvının ağırlığına eşittir. Örnek: suya (1000 kg/m³) 1 × 10⁻³ m³ batan cisme 1000 × 1 × 10⁻³ × 10 = 10 N etki eder')
YUZ=B('Yüzme–askıda kalma–batma','d_cisim < d_sıvı ise cisim yüzer, d_cisim = d_sıvı ise askıda kalır, d_cisim > d_sıvı ise batar. Yüzen ve askıdaki cisimde kaldırma kuvveti cismin ağırlığına eşittir')
DEN=B('Denge','Durgun cisimde yukarı yönlü kuvvetlerin toplamı aşağı yönlülerin toplamına eşittir. Örnek: iple asılı 5 N’luk cisme ip 5 N’luk kuvvet uygular')

# ============ 01 · taşırma kabı + dinamometre · kolay ============
kartla(1,'Taşırma kabı','Taşan sıvının hacmi batan hacme eşittir; kaldırma kuvveti taşan sıvının ağırlığıdır, ip gerilmesi ağırlıktan bu kadar azalır.','Taşan suyun kütlesini ya da hacmini N olarak okumaya çalışmak; okuma farkını atlamak.','kolay','şekilli',3,'fz-kk2-tasirma','Taşırma kabı ve ip gerilmesi')
V1=Fr(250,10**6); F1=1000*V1*10; G1=Fr(13,2); R1=G1-F1
assert F1==Fr(5,2) and R1==4 and G1==Fr(13,2) and Fr(65,10)-Fr(25,100)==Fr(25,4) and G1+F1==9
a=['\\draw[very thick] (-.4,5) -- (1.6,5);','\\draw[thick] (.6,5) -- (.6,2.75);','\\node[right] at (.8,4.2) {$G=6{,}5$ N};',blk(.2,2.05,.8,.7,'taş'),'\\node at (.6,1.2) {(a) havada}; ',
   kap(3.4,2.4,2.8,2.0,tas=.6),'\\draw[very thick] (3.6,5) -- (5.6,5);','\\draw[thick] (4.6,5) -- (4.6,1.15);','\\node[right] at (4.8,4.2) {$T=\\,?$};',blk(4.25,.45,.7,.7,'taş'),'\\node at (4.6,-.5) {(b) suda};',
   kap(5.95,.9,1.5,.55),'\\node[right] at (6.95,.55) {$250$ cm$^3$};','\\draw[->,thin] (6.4,1.75) -- (6.4,.75);']
a.append(f'\\node[right] at (6.95,1.5) {{taşan su}};')
q('0001',tipId='fz-kk2-tasirma',tip='Taşırma kabı ve ip gerilmesi',z='kolay',kaz='Taşan suyun hacminden kaldırma kuvvetini bulup ip gerilmesini hesaplar.',
 kart='K-FZKK2-01 (taşırma kabı) · taş, taşan su ve ip gerilmesi',kalip='şekilli',sekil=fig(*a),
 metin='Fen laboratuvarında bir öğrenci, bir taş parçasını önce şekil (a)’daki gibi havada ince bir iple tavana asıyor. Sonra ağzına kadar su dolu bir taşırma kabına, taşı şekil (b)’deki gibi iple sarkıtarak tamamen batırıyor ve hareketsiz tutuyor. Kabın borusundan taşan suyun tamamı ölçü kabında toplanıyor. Taş kabın tabanına ve duvarlarına değmiyor.\nSuyun özkütlesi 1000 kg/m³ ve g = 10 m/s² olduğuna göre, (b) durumunda ipteki gerilme kuvveti kaç N’dur?',
 dogru=R1,yan=[(Fr(5,2),'Kaldırma kuvvetini (2,5 N) ip gerilmesi sanmış; taşın ağırlığından çıkarmamış.','dikkat'),(Fr(25,4),'Taşan suyun kütlesini (0,25 kg) kaldırma kuvveti sanıp 6,5 − 0,25 = 6,25 bulmuş; kütleyi ağırlığa çevirmeyi (× g) atlamış.','islem'),(Fr(13,2),'İp gerilmesinin suda da değişmeyeceğini sanmış.','bilgi'),(9,'Kaldırma kuvvetini taşın ağırlığına eklemiş (6,5 + 2,5).','dikkat')],
 istenen='Taş suya batırıldığında ipteki gerilme kuvveti (N).',
 ip=['Taşırma kabından taşan su ile taşın suya giren kısmı arasında nasıl bir ilişki olduğunu düşün.'],
 bilgi=[KAL,B('İp gerilmesi','taş iple hareketsiz tutuluyorsa T + F = G’dir, yani T = G − F. Örnek: ağırlığı 8 N, kaldırma kuvveti 3 N olan cisimde ip 5 N’luk kuvvet uygular')],
 ad=[A('Taşın hacmi','Tamamen batan taş, kendi hacmi kadar suyu taşırır.','V = 250 cm³ = 2,5 × 10⁻⁴ m³'),A('Kaldırma kuvveti','Taşan suyun ağırlığı kaldırma kuvvetine eşittir.','F = 1000 × 2,5 × 10⁻⁴ × 10 = 2,5 N'),A('İp gerilmesi','Taş dengede: yukarı yönlü T ve F, aşağı yönlü G vardır.','T = G − F = 6,5 − 2,5 = 4 N')],
 puf='Taşırma kabında taşan sıvının hacmi cismin batan hacmidir; kaldırma kuvveti de taşan sıvının ağırlığıdır.')

# ============ 02 · üç cisim, eşit hacim · kolay · öncüllü ============
kartla(2,'Yüzme–askıda–batma','Aynı sıvıda yüzen cismin özkütlesi sıvınınkinden küçük, askıdaki eşit, batanınki büyüktür; eşit hacimli tamamen batık cisimlere eşit kaldırma kuvveti etki eder.','Batan cisme en büyük, yüzen cisme en küçük ağırlık sanmak; kaldırma kuvvetini özkütleyle orantılı saymak.','kolay','öncüllü',3,'fz-kk2-uc-cisim','Aynı sıvıda yüzen, askıdaki ve batan cisimler')
ONC2=[('Özkütleleri arasında d_X < d_Y < d_Z ilişkisi vardır.',True,'X yüzdüğü için d_X < d_sıvı; Y askıda olduğu için d_Y = d_sıvı; Z battığı için d_Z > d_sıvı. Böylece d_X < d_Y < d_Z olur.','özkütlenin cismin kütlesinden bağımsız olduğunu, yani eşit hacimli cisimlerin özkütlece sıralanamayacağını düşünmüş.'),
      ('Y’ye etki eden kaldırma kuvveti X’e etki edenden büyüktür.',True,'Y tamamen batıktır, X’in ise yalnız bir kısmı batıktır; Y daha çok sıvı yer değiştirir (eşit hacim) ve F = d × V_batan × g büyük olur. Y ile Z’nin kaldırma kuvvetleri eşittir.','yüzen cismin kaldırma kuvvetinin daha büyük olduğunu sanmış.'),
      ('Z’ye etki eden kaldırma kuvveti Y’ye etki edenden büyüktür.',False,'Y ve Z eşit hacimlidir ve ikisi de tamamen batıktır; aynı sıvıda eşit sıvı hacmi yer değiştirirler. Kaldırma kuvvetleri eşittir.','dipteki cismin daha büyük kaldırma kuvveti aldığını (daha “ağır” olduğu için) sanmış.')]
m,dg,yn,ad=onc('Eşit hacimli X, Y ve Z cisimleri, aynı sıvının bulunduğu bir kapta şekildeki konumlarda dengededir: X yüzmekte, Y sıvının içinde askıda kalmakta, Z ise kabın tabanında durmaktadır. Bir fen öğretmeni bu düzeneği kullanarak öğrencilerinden cisimlerin özkütleleri ve üzerlerine etki eden kaldırma kuvvetleri hakkında yorum yapmalarını istiyor.',ONC2,['Yalnız III','I ve II','I ve III','II ve III','I, II ve III'],'Buna göre, yukarıdaki yargılardan hangileri doğrudur?')
assert dg=='I ve II'
s2=[kap(0,6.2,3.9,3.3),blk(.5,2.8,.9,.9,'X'),'\\draw[thick,fill=gray!40] (.5,2.8) rectangle (1.4,3.7);' if False else '',
    blk(.5,2.8,.9,.9,'X'),blk(2.6,1.2,.9,.9,'Y'),blk(4.6,0,.9,.9,'Z'),lvl(0,6.2,3.3)]
# X yarı batık: üst kenarı 3.3+.45; alt kenarı 2.85 → blk(.5,2.85,..)
s2=[kap(0,6.2,3.9,3.3),blk(.5,2.85,.9,.9,'X'),blk(2.6,1.2,.9,.9,'Y'),blk(4.6,0,.9,.9,'Z')]
s2[1]=blk(.5,2.85,.9,.9,'X')
q('0002',tipId='fz-kk2-uc-cisim',tip='Aynı sıvıda yüzen, askıdaki ve batan cisimler',z='kolay',kaz='Yüzen, askıda kalan ve batan cisimlerin özkütle ve kaldırma kuvveti ilişkilerini yorumlar.',
 kart='K-FZKK2-02 (üç cisim) · eşit hacimli X, Y, Z',kalip='öncüllü',sekil=fig(*s2),metin=m,
 dogru=dg,sira=['Yalnız III','I ve II','I ve III','II ve III','I, II ve III'],yan=yn,
 istenen='Doğru olan yargıların hangileri olduğu.',
 ip=['Her cismin konumundan sıvıya göre özkütlesini, tamamen batıp batmadığından da batan hacmini belirle.'],
 bilgi=[YUZ,KAL],ad=ad,puf='Eşit hacimli cisimlerde kaldırma kuvveti yalnız batan hacme bağlıdır; tamamen batık olanlara eşit kaldırma kuvveti etki eder.')

# ============ 03 · prizma yağda yüzüyor · kolay ============
kartla(3,'Yüzen cismin ağırlığı','Yüzen cismin ağırlığı kaldırma kuvvetine eşittir; kaldırma kuvveti yalnız batan hacimle hesaplanır.','Toplam hacmi kullanmak; cm² ve cm³’ü m’ye çevirirken üs hatası yapmak; sıvıyı su sanmak.','kolay','şekilli',3,'fz-kk2-kisa-prizma','Yüzen prizmanın ağırlığı')
A3=Fr(20,10**4); h3=Fr(12,100); F3=800*A3*h3*10
assert F3==Fr(48,25) and 800*A3*Fr(30,100)*10==Fr(24,5) and 1000*A3*h3*10==Fr(12,5) and 800*Fr(20,10**3)*h3*10==Fr(96,5) and 800*A3*Fr(12,1000)*10==Fr(48,250)
s3=[kap(0,4.2,4.2,3.4,col='yellow!25'),blk(1.3,.2+0,1.6,3.0,'','gray!30'),'']
# prizma: 30 cm = 3 cm çizim; batan 12 cm = 1.2 cm → alt kenar = 3.4-1.2 = 2.2
s3=[kap(0,5.2,4.4,3.4,col='yellow!25'),blk(1.6,2.2,2.2,3.0,'$A=20$ cm$^2$','gray!30'),olc(4.1,2.2,3.4,'$12$ cm',sol=False),
    olc(1.3,2.2,5.2,'$30$ cm'),'\\node[below] at (2.6,-.05) {yağ: $0{,}8$ g/cm$^3$};']
q('0003',tipId='fz-kk2-kisa-prizma',tip='Yüzen prizmanın ağırlığı',z='kolay',kaz='Yüzen prizmanın batan hacminden kaldırma kuvvetini, dolayısıyla ağırlığını hesaplar.',
 kart='K-FZKK2-03 (yüzen cismin ağırlığı) · yağda yüzen prizma',kalip='şekilli',sekil=fig(*s3),
 metin='Bir öğrenci, düzgün dikdörtgen prizma biçimli bir tahta çubuğu şekildeki gibi bir yağ dolu kaba bırakıyor ve çubuk dengede yüzüyor. Çubuğun kesit alanı, boyu, sıvının içindeki kısmının boyu ve yağın özkütlesi şekilde verilmiştir. Çubuk kabın tabanına ve yan duvarlarına değmemektedir.\ng = 10 m/s² olduğuna göre, çubuğun ağırlığı kaç N’dur?',
 dogru=F3,yan=[(Fr(48,250),'240 cm³ = 2,4 × 10⁻⁵ m³ yazmış (cm³ → m³ çevirisinde üs hatası); sonuç 10 kat küçük çıkmış.','islem'),(Fr(12,5),'Yağı su sanıp 1000 kg/m³ özkütle kullanmış.','dikkat'),(Fr(24,5),'Batan hacim yerine çubuğun tüm hacmini (600 cm³) kullanmış.','dikkat'),(Fr(96,5),'20 cm² = 2 × 10⁻² m² yazmış (cm² → m² çevirisinde üs hatası); sonuç 10 kat büyük çıkmış.','islem')],
 istenen='Çubuğun ağırlığı (N).',
 ip=['Çubuğun ağırlığı hangi kuvvetle dengelenir? Bu kuvvet için hangi hacmi kullanmalısın?'],
 bilgi=[YUZ,KAL],
 ad=[A('Batan hacim','Kesit alanı ile sıvıdaki boy çarpılır.','V = 20 × 12 = 240 cm³ = 2,4 × 10⁻⁴ m³'),A('Kaldırma kuvveti','Yağın özkütlesi 800 kg/m³ alınır.','F = 800 × 2,4 × 10⁻⁴ × 10 = 1,92 N'),A('Ağırlık','Yüzen cismin ağırlığı kaldırma kuvvetine eşittir.','G = F = 1,92 N')],
 puf='Yüzen cismin ağırlığını bulmak için tüm hacmi değil, yalnız sıvıdaki (batan) hacmi kullan.')

# ============ 04 · tuz eklenince tabana bağlı cisim · orta · öncüllü ============
kartla(4,'İp gerilmesi (nitel)','Tabana bağlı batık cisimde T = F − G; sıvının özkütlesi artarsa F artar, G değişmediği için ip gerilmesi artar.','Cismin ağırlığının da değiştiğini sanmak; ip gerilmesinin sabit kaldığını düşünmek.','orta','öncüllü',3,'fz-kk2-ip-tuz','Tabana bağlı cisim, tuz ekleme ve ip gerilmesi')
ONC4=[('Cisme etki eden kaldırma kuvveti artar.',True,'Cismin hacmi değişmez ve tamamen batıktır; sıvının özkütlesi arttığı için F = d × V × g artar.','kaldırma kuvvetinin yalnız cismin hacmine bağlı olduğunu, sıvının cinsinden etkilenmediğini sanmış.'),
      ('İpteki gerilme kuvveti artar.',True,'Cisim dengede kalır ve T = F − G’dir; G sabit, F arttığı için ip gerilmesi de artar.','ipin yalnız cismin ağırlığıyla ilgili olduğunu ve değişmeyeceğini sanmış.'),
      ('Cismin ağırlığı artar.',False,'Ağırlık cismin kütlesine bağlıdır; sıvıya tuz eklemek cismin kütlesini değiştirmez.','sıvı özkütlesi arttığı için cismin de “ağırlaştığını” sanmış.')]
m,dg,yn,ad=onc('Bir öğrenci, içinde su bulunan bir kabın tabanına hafif bir iple bağladığı küçük plastik bir cismi şekildeki gibi tamamen suyun içinde dengede tutuyor. Cismin özkütlesi suyunkinden küçüktür ve ip gergindir. Öğrenci daha sonra suya tuz ekleyip karıştırıyor; böylece sıvının özkütlesi artıyor, cisim ise yine aynı yerde ve tamamen batık olarak dengede kalıyor. Sıvı taşmıyor.',ONC4,['Yalnız I','Yalnız III','I ve II','I ve III','I, II ve III'],'Buna göre, tuz eklendikten sonra yukarıdaki yargılardan hangileri doğrudur?')
assert dg=='I ve II'
s4=[kap(0,3.4,3.8,3.0),blk(1.2,1.1,1.0,.9,'','gray!40'),'\\draw[thick] (1.7,0) -- (1.7,1.1);','\\fill (1.7,0) circle (.06);','\\node[below] at (2.7,-.05) {su};',
    '\\draw[thick] (4.4,3.3) -- (5.2,3.7) -- (5.4,3.45) -- (4.7,3.0) -- cycle;','\\draw[->,thick,vurgu] (4.7,3.1) -- (3.2,2.6);','\\node[right] at (4.4,3.8) {tuz};']
q('0004',tipId='fz-kk2-ip-tuz',tip='Tabana bağlı cisim, tuz ekleme ve ip gerilmesi',z='orta',kaz='Sıvı özkütlesi değişince tabana bağlı cisme etkiyen kaldırma kuvvetini ve ip gerilmesini nitel olarak yorumlar.',
 kart='K-FZKK2-04 (ip gerilmesi, nitel) · tuz eklenmesi',kalip='öncüllü',sekil=fig(*s4),metin=m,
 dogru=dg,sira=['Yalnız I','Yalnız III','I ve II','I ve III','I, II ve III'],yan=yn,
 istenen='Doğru olan yargıların hangileri olduğu.',
 ip=['Cismin hacmi ve kütlesi değişmiyor; kaldırma kuvvetinin hangi niceliğe bağlı olduğunu ve ip gerilmesiyle ilişkisini düşün.'],
 bilgi=[KAL,B('Tabana bağlı cisim','Tamamen batık ve tabana bağlı cisimde yukarı yönlü kaldırma kuvveti, aşağı yönlü ağırlık ve ip gerilmesinin toplamına eşittir: F = G + T')],ad=ad,
 puf='Tabana bağlı batık cisimde sıvının özkütlesi artarsa kaldırma kuvveti ve ip gerilmesi artar; cismin ağırlığı değişmez.')

# ============ 05 · yaya asılı cisim · orta ============
kartla(5,'Yaya asılı cisim','Yay uzaması kuvvetle orantılıdır; sıvıdaki uzama azalması kaldırma kuvvetini verir; F/G = (d_sıvı)/(d_cisim) ile cismin özkütlesi bulunur.','Sudaki uzamayı ağırlık sanmak; oranı ters kurmak; uzamaların toplamını almak.','orta','şekilli',3,'fz-kk2-yay','Yaya asılı cismin özkütlesi')
x_h,x_s=8,6; ds=Fr(1); dc=ds*x_h/(x_h-x_s)
assert dc==4 and ds*(x_h-x_s)/x_h==Fr(1,4) and ds*x_s/(x_h-x_s)==3 and ds*(x_h+x_s)/(x_h-x_s)==7
sc=.35  # 1 cm uzama = .35 cm çizim
y0=5.0
s5=['\\draw[very thick] (-.8,%.2f) -- (5.4,%.2f);'%(y0+.0,y0+.0),
    yay(.6,y0,y0-1.3-0,n=5),'\\draw[dashed] (.1,%.2f) -- (1.1,%.2f);'%(y0-1.3,y0-1.3)]
yb1=y0-1.3-x_h*sc*.0
# gerilmemiş boy 1.3 cm; uzama 8 cm→ 2.8 çizim; 6 cm → 2.1 çizim
yay_boy=1.3
ya=y0-yay_boy-x_h*sc; yb=y0-yay_boy-x_s*sc
s5=['\\draw[very thick] (-.8,%.2f) -- (5.6,%.2f);'%(y0,y0),
    yay(.6,y0,ya),yay(4.2,y0,yb),
    '\\draw[dashed] (.0,%.2f) -- (1.3,%.2f);'%(y0-yay_boy,y0-yay_boy),'\\draw[dashed] (3.6,%.2f) -- (4.9,%.2f);'%(y0-yay_boy,y0-yay_boy),
    olc(1.2,y0-yay_boy,ya,'$8$ cm',sol=False),olc(4.8,y0-yay_boy,yb,'$6$ cm',sol=False),
    blk(.15,ya-.9,.9,.9,'cisim'),blk(3.75,yb-.9,.9,.9,'cisim'),
    kap(3.1,2.4,1.6,1.7),'\\node at (.6,-.9) {(a) havada};','\\node at (4.3,-.9) {(b) suda};']
# kap içinde cisim: cisim su içinde olmalı → kabı cismin etrafına çiz (kabın tabanı y=yb-.9-.4)
kb=yb-.9-.4; hh=1.9
s5=[f'\\begin{{scope}}[shift={{(0,{kb})}}]'+kap(3.2,3.4,hh+.5,hh)+'\\end{scope}',
    '\\draw[very thick] (-.8,%.2f) -- (6.9,%.2f);'%(y0,y0),yay(.6,y0,ya),yay(4.6,y0,yb),
    '\\draw[dashed] (.0,%.2f) -- (1.3,%.2f);'%(y0-yay_boy,y0-yay_boy),'\\draw[dashed] (4.0,%.2f) -- (5.3,%.2f);'%(y0-yay_boy,y0-yay_boy),
    olc(1.2,y0-yay_boy,ya,'$8$ cm',sol=False),olc(5.2,y0-yay_boy,yb,'$6$ cm',sol=False),
    blk(.15,ya-.9,.9,.9,'cisim'),blk(4.15,yb-.9,.9,.9,'cisim'),
    f'\\node at (.6,{ya-1.4}) {{(a) havada}};',f'\\node at (4.6,{kb-.5}) {{(b) suda}};']
# kabın su seviyesi cismin üstünde olmalı
assert kb+hh>yb-.9+.9 and kb<yb-.9
q('0005',tipId='fz-kk2-yay',tip='Yaya asılı cismin özkütlesi',z='orta',kaz='Yayın havada ve sıvıdaki uzamalarından cismin özkütlesini bulur.',
 kart='K-FZKK2-05 (yaya asılı cisim) · uzama oranından özkütle',kalip='şekilli',sekil=fig(*s5),
 metin='Hafif ve esnek bir yaya asılan bir metal cisim, şekil (a)’daki gibi havada yayı belirli bir miktar uzatıyor. Cisim, aynı yay ile şekil (b)’deki gibi tamamen suya batırıldığında yaydaki uzama azalıyor. Şekilde kesikli çizgi yayın serbest (gerilmemiş) ucunu, oklar ise yayın uzamasını gösterir. Yay Hooke yasasına uygundur (uzama kuvvetle doğru orantılıdır) ve cisim kabın tabanına değmemektedir.\nSuyun özkütlesi 1 g/cm³ olduğuna göre, cismin özkütlesi kaç g/cm³’tür?',
 dogru=dc,yan=[(Fr(1,4),'Oranı ters kurup d_cisim = d_su × F ÷ G = 1 × 2 ÷ 8 hesaplamış.','islem'),(1,'Suyun özkütlesini cismin özkütlesi sanmış.','dikkat'),(3,'Sudaki uzamayı (6 cm) cismin ağırlığıyla orantılı sanmış: d = 6 ÷ (8 − 6).','dikkat'),(2,'Uzamaların farkını (8 − 6 = 2 cm) özkütle sayısı olarak almış.','dikkat')],
 istenen='Cismin özkütlesi (g/cm³).',
 ip=['Yayın uzaması yayı çeken kuvvetle orantılıdır; iki durumdaki uzama farkı hangi kuvvete karşılık gelir?'],
 bilgi=[B('Hooke yasası','yayı çeken kuvvet, yayın uzamasıyla doğru orantılıdır (F = k × x). Örnek: 5 cm uzayan yay 3 N’luk kuvvetle çekiliyorsa 10 cm uzaması için 6 N gerekir'),KAL],
 ad=[A('Uzamaları kuvvetle eşleştir','Havadaki uzama ağırlığa (G), sudaki uzama ağırlık ile kaldırma kuvveti farkına (G − F) karşılık gelir.','G ↔ 8 cm · G − F ↔ 6 cm'),A('Kaldırma kuvveti','Uzamadaki azalma kaldırma kuvvetini gösterir.','F ↔ 8 − 6 = 2 cm → F ÷ G = 2 ÷ 8 = 1/4'),A('Özkütleyi bul','Tamamen batık cisimde F ÷ G = d_su ÷ d_cisim olur.','1/4 = 1 ÷ d_cisim → d_cisim = 4 g/cm³')],
 puf='Tamamen batık cisimde F ÷ G = d_sıvı ÷ d_cisim; yayın uzama azalması F’yi, havadaki uzama G’yi temsil eder.')

# ============ 06 · terazi · orta ============
kartla(6,'Terazi okuması','İple tutulan batık cisim, sıvıya kaldırma kuvvetinin tepkisini uygular; terazi okuması bu kuvvetin kütle karşılığı kadar artar.','Cismin tüm kütlesini terazi okumasına eklemek; hacmi de kütleye eklemek; okumanın değişmediğini sanmak.','orta','şekilli',3,'fz-kk2-terazi','Terazi okuması ve batırılan cisim')
mt=300; Vt=100; Ft=1000*Fr(Vt,10**6)*10; rt=Ft/10*1000
assert Ft==1 and rt==100 and 2000+rt==2100 and 2000+mt==2300 and 2000+mt-rt==2200 and 2000-rt==1900
s6=['\\draw[thick,fill=gray!15] (-.2,-.5) rectangle (3.6,0);','\\node at (1.7,-.25) {\\small $2000$ g};',kap(.2,3.0,2.6,1.9),
    '\\draw[thick] (-.5,4.6) -- (3.9,4.6);','\\draw[thick] (1.7,4.6) -- (1.7,1.35);','\\draw[thick] (1.7,1.35) -- (1.7,1.4);',
    blk(1.25,.75,.9,.6,'','gray!40'),'\\node[right,align=left] at (3.9,2.9) {$m=300$ g\\\\$V=100$ cm$^3$};',
    '\\draw[->,thin] (3.9,2.4) -- (2.2,1.2);']
s6[3]='\\draw[thick] (-.5,4.6) -- (3.9,4.6);'
s6=['\\draw[thick,fill=gray!15] (-.2,-.5) rectangle (3.6,0);',kap(.2,3.0,2.6,1.9),
    '\\draw[thick] (-.5,4.4) -- (4.0,4.4);','\\draw[thick] (1.7,4.4) -- (1.7,1.35);',blk(1.25,.75,.9,.6,'','gray!40'),
    '\\node[right,align=left] at (3.5,3.3) {cisim:\\\\$m=300$ g\\\\$V=100$ cm$^3$};','\\draw[->,thin] (3.5,3.1) -- (2.3,1.2);',
    '\\node at (1.7,-.25) {$2000$ g};','\\node[below] at (1.7,-.6) {kap + su (cisim yokken)};']
q('0006',tipId='fz-kk2-terazi',tip='Terazi okuması ve batırılan cisim',z='orta',kaz='İple tutulan batık cismin terazi okumasını nasıl değiştirdiğini hesaplar.',
 kart='K-FZKK2-06 (terazi) · iple tutulan cisim, terazi okuması',kalip='şekilli',sekil=fig(*s6),
 metin='Bir terazinin üzerine su dolu bir kap konuyor; kap ve içindeki su birlikte şekilde gösterilen değeri okutuyor. Bir öğrenci, şekilde verilen bilgileri taşıyan metal bir cismi ince bir iple tutarak suyun içine, kabın tabanına ve duvarlarına değmeyecek biçimde tamamen daldırıyor; cismi tutmayı bırakmıyor. Kaptan su taşmıyor.\nSuyun özkütlesi 1000 kg/m³ ve g = 10 m/s² olduğuna göre, cisim bu durumdayken terazi kaç g gösterir?',
 dogru=2100,yan=[(1900,'Kaldırma kuvvetinin kütle karşılığını okumadan çıkarmış.','dikkat'),(2000,'Cismi iple tuttuğu için terazi okumasının hiç değişmeyeceğini sanmış.','bilgi'),(2300,'Cismin tüm kütlesini (300 g) okumaya eklemiş; cisim dipte durmuş gibi düşünmüş.','bilgi'),(2200,'İpin taşıdığı yükü (300 − 100 = 200 g karşılığı) okumaya eklemiş; kaldırma kuvvetinin tepkisini değil, ipteki yükü saymış.','bilgi')],
 istenen='Terazinin gösterdiği değer (g).',
 ip=['Su cisme yukarı doğru kuvvet uyguluyorsa, su, kap ve terazi tarafında ne olur?'],
 bilgi=[KAL,B('Etki–tepki','Su cisme yukarı doğru F kadar kuvvet uygularsa cisim de suya aşağı doğru F kadar kuvvet uygular. Örnek: 2 N’luk kuvvet, terazide 200 g’lık kütle gibi okunur (g = 10 m/s²)')],
 ad=[A('Kaldırma kuvveti','Cisim tamamen batıktır; hacmi 100 cm³ = 10⁻⁴ m³.','F = 1000 × 10⁻⁴ × 10 = 1 N'),A('Tepki kuvveti','Cisim suya, kaldırma kuvvetine eşit büyüklükte aşağı yönlü kuvvet uygular; terazi bunu da taşır.','Ek yük = 1 N ↔ 100 g'),A('Terazi okuması','Kap ve su kütlesine eklenir.','2000 + 100 = 2100 g')],
 puf='İple tutulan batık cisim, terazi okumasını kaldırma kuvvetinin kütle karşılığı kadar artırır; cismin kütlesi okumaya girmez.')

# ============ 07 · karışmayan iki sıvıda denge · zor ============
kartla(7,'Karışmayan iki sıvı','Ara yüzeyde dengedeki cismin ağırlığı iki sıvının kaldırma kuvvetlerinin toplamına eşittir: d_cisim × V = d₁ × V₁ + d₂ × V₂.','Cismi tek bir sıvıda yüzüyormuş gibi düşünmek; oranları ters yazmak; iki özkütlenin basit ortalamasını almak.','orta','şekilli',4,'fz-kk2-iki-sivi','Karışmayan iki sıvıda dengedeki cisim')
dy,dsu=Fr(8,10),Fr(1); hy,hs=2,3; d7=(dy*hy+dsu*hs)/(hy+hs)
assert d7==Fr(23,25) and (dy*hs+dsu*hy)/5==Fr(22,25) and (dy+dsu)/2==Fr(9,10) and d7==Fr('0.92')
s7=[kap(0,4.0,4.6,3.8,col='yellow!25'),f'\\fill[{SIV}] (0,0) rectangle (4,2.3);','\\draw[thick] (0,4.6) -- (0,0) -- (4,0) -- (4,4.6);','\\draw[densely dashed] (0,2.3) -- (4,2.3);',
    blk(1.5,.8+.0,1.0,1.0,'',''),]
# cisim yüksekliği 5 cm → 2.5 çizim (1 cm = .5): 2 cm yağda (1.0), 3 cm suda (1.5); ara yüzey y=2.3
hc=2.5; yb7=2.3-1.5
s7=[f'\\fill[yellow!25] (0,2.3) rectangle (5,3.8);',f'\\fill[{SIV}] (0,0) rectangle (5,2.3);','\\draw[thick] (0,4.6) -- (0,0) -- (5,0) -- (5,4.6);','\\draw[densely dashed] (0,2.3) -- (5,2.3);',
    blk(1.3,yb7,1.4,hc,'','gray!45'),olc(3.3,2.3,2.3+1.0,'$2$ cm',sol=False),olc(3.3,yb7,2.3,'$3$ cm',sol=False),
    '\\node[right] at (5.15,3.4) {yağ: $0{,}8$ g/cm$^3$};','\\node[right] at (5.15,1.2) {su: $1$ g/cm$^3$};']
q('0007',tipId='fz-kk2-iki-sivi',tip='Karışmayan iki sıvıda dengedeki cisim',z='orta',kaz='Karışmayan iki sıvının ara yüzeyinde dengedeki cismin özkütlesini hesaplar.',
 kart='K-FZKK2-07 (karışmayan iki sıvı) · ara yüzeyde dengedeki cisim',kalip='şekilli',sekil=fig(*s7),
 metin='Bir kapta, birbirine karışmayan iki sıvı üst üste durmaktadır: üstte yağ, altta su. Düzgün dikdörtgen prizma biçimli homojen bir cisim, şekildeki gibi iki sıvının sınırında, kabın tabanına değmeden ve hareketsiz kalarak dengededir. Cismin üst yüzü yağın içinde, alt yüzü suyun içindedir; yan yüzleri ise iki sıvıyla da temas etmektedir.\nBuna göre, cismin özkütlesi kaç g/cm³’tür?',
 dogru=d7,yan=[(Fr(4,5),'Cismi yalnız yağda yüzüyormuş gibi düşünüp yağın özkütlesini almış.','bilgi'),(Fr(22,25),'Boyları ters eşleştirmiş: yağa 3 cm, suya 2 cm demiş (0,8 × 3 + 1 × 2) ÷ 5.','dikkat'),(Fr(9,10),'İki sıvının özkütlelerinin basit ortalamasını (0,8 + 1) ÷ 2 almış; batan boyları hesaba katmamış.','islem'),(1,'Cismin suda yüzeye yakın olduğu için özkütlesini suyunkine eşit sanmış.','bilgi')],
 istenen='Cismin özkütlesi (g/cm³).',
 ip=['Cismin ağırlığını hangi kuvvetler dengeliyor?'],
 bilgi=[KAL,B('Birden çok sıvıda kaldırma','cisim iki sıvıya birden batıksa her sıvı, cismin kendi içindeki kısmına ayrı bir kaldırma kuvveti uygular. Örnek: yağdaki kısım 1 N, sudaki kısım 2 N’luk kuvvet doğuruyorsa bunlar aynı yönlüdür')],
 ad=[A('Kuvvetleri tanımla','Cismin kesiti A olsun; yağdaki boy 2 cm, sudaki boy 3 cm, toplam boy 5 cm’dir.','V_yağ = 2A · V_su = 3A · V = 5A'),A('Denge koşulu','Cismin ağırlığı iki kaldırma kuvvetinin toplamına eşittir.','d × 5A × g = 0,8 × 2A × g + 1 × 3A × g'),A('Sadeleştir','A ve g sadeleşir.','5d = 1,6 + 3 = 4,6'),A('Özkütle','Her iki yanı 5’e böl.','d = 0,92 g/cm³')],
 puf='İki sıvının sınırında dengedeki cismin özkütlesi, boy (hacim) ağırlıklı ortalamadır: d = (d₁h₁ + d₂h₂) ÷ (h₁ + h₂).')

# ============ 08 · yumurta ve tuz · orta · öncüllü ============
kartla(8,'Sıvı değiştirme/tuz','Dipteki cisimde F < G; yüzünce F = G olur ve batan hacim toplam hacimden küçüktür; yüzen cisim için sıvı özkütlesi cismin özkütlesinden büyüktür.','Yüzen cismin özkütlesinin sıvıyla eşit olduğunu sanmak; kaldırma kuvvetinin yüzünce azaldığını düşünmek.','orta','öncüllü',4,'fz-kk2-yumurta','Yumurta ve tuzlu su')
ONC8=[('Cisim dipteyken ona etki eden kaldırma kuvveti ağırlığına eşittir.',False,'Cisim dipte duruyorsa yukarı yönlü kaldırma kuvveti tek başına ağırlığı dengelemez; zemin de cisme yukarı doğru tepki uygular. Kaldırma kuvveti ağırlıktan küçüktür.','kaldırma kuvvetinin her denge durumunda ağırlığa eşit olması gerektiğini sanmış.'),
      ('Cisim yüzdüğünde batan hacmi, toplam hacminden küçüktür.',True,'Tuzlu su cisimden daha yoğundur; yüzen cisimde batan hacim oranı d_cisim ÷ d_sıvı < 1 olur.','yüzen cismin tamamen sıvının içinde kalması gerektiğini sanmış.'),
      ('Cisim bu son durumda yüzerken, özkütlesi tuzlu suyun özkütlesine eşittir.',False,'Yüzen cismin özkütlesi sıvınınkinden küçüktür; eşitlik yalnız askıda kalmada geçerlidir.','yüzmenin ve askıda kalmanın aynı şey olduğunu sanmış.')]
m,dg,yn,ad=onc('Özkütlesi 1,05 g/cm³ olan bir yumurta, saf su dolu bir bardağa bırakıldığında şekildeki gibi bardağın tabanında durmaktadır. Bir öğrenci suya tuz ekleyip karıştırdıkça sıvının özkütlesi artıyor; tuz eklemeyi sürdürdüğünde yumurta yükseliyor ve sonunda bir kısmı sıvının dışında kalacak biçimde yüzeyde dengede yüzüyor. Öğrenci, bu gözlemi arkadaşlarına açıklamak için yargılar yazıyor.',ONC8,['Yalnız II','Yalnız III','I ve II','I ve III','II ve III'],'Buna göre, yukarıdaki yargılardan hangileri doğrudur?')
assert dg=='Yalnız II'
s8=[kap(0,3.2,3.8,3.0),blk(.9,0,1.0,.75,'','gray!40') if False else '\\draw[thick,fill=gray!40] (1.5,.65) ellipse (.45 and .6);','\\node[below] at (1.6,-.05) {saf su};',
    '\\draw[->,thick] (3.8,1.9) -- (4.9,1.9);','\\node[above] at (4.35,1.95) {tuz ekle};',
    kap(5.3,3.2,3.8,3.0,col='vurgu!25'),'\\draw[thick,fill=gray!40] (6.9,2.55) ellipse (.45 and .6);','\\node[below] at (6.9,-.05) {tuzlu su};']
q('0008',tipId='fz-kk2-yumurta',tip='Yumurta ve tuzlu su',z='orta',kaz='Sıvının özkütlesi artınca dipteki cismin yüzmesini ve kuvvet–hacim ilişkilerini yorumlar.',
 kart='K-FZKK2-08 (sıvı değiştirme/tuz) · yumurta saf suda dipte, tuzlu suda yüzer',kalip='öncüllü',sekil=fig(*s8),metin=m,
 dogru=dg,sira=['Yalnız II','Yalnız III','I ve II','I ve III','II ve III'],yan=yn,
 istenen='Doğru olan yargıların hangileri olduğu.',
 ip=['Yumurta dipteyken ve yüzerken, sıvının özkütlesiyle yumurtanınkini karşılaştırıp ağırlık ile kaldırma kuvveti ilişkisini yaz.'],
 bilgi=[YUZ,B('Batan hacim oranı','yüzen cisimde V_batan ÷ V = d_cisim ÷ d_sıvı’dır. Örnek: d_cisim sıvınınkinin yarısı ise cismin yarısı batar')],ad=ad,
 puf='Yüzen cismin özkütlesi sıvınınkinden küçüktür ve batan hacmi toplam hacmin d_cisim ÷ d_sıvı katıdır.')

# ============ 09 · aynı cisim iki sıvıda dinamometre · zor ============
kartla(9,'Farklı sıvılarda aynı cisim','Aynı cisim iki sıvıda tamamen batıksa hacim aynıdır: suda kaldırma kuvvetinden hacim, Y’de kaldırma kuvvetinden özkütle bulunur.','Sıvıdaki okumayı kaldırma kuvveti sanmak; g ya da hacim adımını atlamak.','zor','şekilli',4,'fz-kk2-dino-iki-sivi','Aynı cismin iki sıvıdaki dinamometre okumaları')
G9,RX,RY=60,35,36; FX,FY=G9-RX,G9-RY; V9=Fr(FX,1000*10); dY=Fr(FY)/(V9*10); dc9=Fr(G9,10)/V9
assert FX==25 and FY==24 and V9==Fr(25,10000) and dY==960 and dc9==2400 and Fr(RY)/(V9*10)==1440 and Fr(FY)/V9==9600 and RX<G9 and RY<G9
s9=[dino(.6,5,'$60$ N'),'\\draw (.6,3.25) -- (.6,2.85);',blk(.15,2.15,.9,.7,'cisim'),'\\node at (.6,1.4) {havada};',
    kap(2.2,2.2,2.8,2.1),dino(3.3,5,'$35$ N'),'\\draw (3.3,3.25) -- (3.3,1.25);',blk(2.85,.55,.9,.7,'cisim'),'\\node[below] at (3.3,-.05) {X: su};',
    kap(5.6,2.2,2.8,2.1,col='orange!25'),dino(6.7,5,'$36$ N'),'\\draw (6.7,3.25) -- (6.7,1.25);',blk(6.25,.55,.9,.7,'cisim'),'\\node[below] at (6.7,-.05) {Y};']
q('0009',tipId='fz-kk2-dino-iki-sivi',tip='Aynı cismin iki sıvıdaki dinamometre okumaları',z='zor',kaz='Aynı cismin suda ve bilinmeyen Y sıvısındaki dinamometre okumalarından Y sıvısının özkütlesini bulur.',
 kart='K-FZKK2-09 (farklı sıvılarda aynı cisim) · suda hacim, Y’de özkütle',kalip='şekilli',sekil=fig(*s9),
 metin='Bir öğrenci, aynı metal cismi dinamometreye asarak önce havada, sonra suyun (X sıvısı) içinde, daha sonra özkütlesi bilinmeyen Y sıvısının içinde tamamen batırarak ölçüyor. Dinamometrenin üç durumdaki okuması şekilde gösterilmiştir. Cisim her iki sıvıda da kabın tabanına değmemektedir.\nSuyun özkütlesi 1000 kg/m³ ve g = 10 m/s² olduğuna göre, Y sıvısının özkütlesi kaç kg/m³’tür?',
 dogru=960,yan=[(1000,'Y sıvısını da su gibi düşünüp özkütlesini 1000 kg/m³ almış.','bilgi'),(1440,'Y’deki okumayı (36 N) kaldırma kuvveti sanmış: 36 ÷ (2,5 × 10⁻³ × 10).','dikkat'),(2400,'Cismin özkütlesini (6 kg ÷ 2,5 × 10⁻³ m³) bulup Y sıvısının özkütlesi sanmış.','dikkat'),(9600,'Y’deki kaldırma kuvvetini hacme bölerken g’ye bölmeyi atlamış (24 ÷ 2,5 × 10⁻³).','islem')],
 istenen='Y sıvısının özkütlesi (kg/m³).',
 ip=['Tamamen batık cisimde kaldırma kuvvetinin dinamometre okumalarından nasıl bulunduğunu düşün.'],
 bilgi=[KAL,B('Dinamometre','sıvıdaki okuma = havadaki okuma − kaldırma kuvveti. Örnek: havada 8 N, kaldırma kuvveti 3 N ise sıvıda 5 N okunur')],
 ad=[A('Sudaki kaldırma kuvveti','Havadaki okuma ile sudaki okuma farkı alınır.','F_X = 60 − 35 = 25 N'),A('Cismin hacmi','Cisim tamamen batıktır; hacim sudaki kaldırma kuvvetinden bulunur.','25 = 1000 × V × 10 → V = 2,5 × 10⁻³ m³'),A('Y’deki kaldırma kuvveti','Aynı cisim Y’de de tamamen batıktır.','F_Y = 60 − 36 = 24 N'),A('Y’nin özkütlesi','Aynı hacim, aynı g ile.','24 = d_Y × 2,5 × 10⁻³ × 10 → d_Y = 960 kg/m³')],
 puf='Aynı cisim farklı sıvılarda tamamen batıksa hacmi aynıdır; hacmi bilinen sıvıdan bulup bilinmeyen sıvıya taşı.')

# ============ 10 · gemi · orta · öncüllü ============
kartla(10,'Gemi','Gemi yüzerken kaldırma kuvveti ağırlığına eşittir; özkütlesi büyük sıvıda daha az batar, kaldırma kuvveti değişmez.','Daha yoğun sıvıda kaldırma kuvvetinin arttığını ya da geminin ağırlığının değiştiğini sanmak.','orta','öncüllü',3,'fz-kk2-gemi','Gemi, nehir ve deniz suyu')
ONC10=[('Gemiye etki eden kaldırma kuvveti, geminin ağırlığına eşittir.',True,'Gemi dengede yüzdüğü için yukarı yönlü kaldırma kuvveti aşağı yönlü ağırlığa eşittir; bu durum her iki sıvıda da geçerlidir.','kaldırma kuvvetinin sıvı özkütlesiyle birlikte arttığını ve ağırlıktan farklı olduğunu sanmış.'),
       ('Gemi denize geçince, suyun içinde kalan kısmının hacmi nehirdekine göre daha büyük olur.',False,'Kaldırma kuvveti aynı kalır; deniz suyunun özkütlesi büyük olduğu için aynı kuvveti sağlamak üzere daha az hacim batması yeter. Batan hacim azalır.','yoğun sıvıda gemiyi taşımanın daha çok hacim gerektirdiğini sanmış.'),
       ('Gemi denize geçince ağırlığı artar.',False,'Ağırlık geminin kütlesine bağlıdır; bulunduğu sıvı değişince kütle değişmez.','sıvı yoğunlaşınca gemiye daha fazla yük bindiğini sanmış.')]
m,dg,yn,ad=onc('Yüklü bir yük gemisi nehirde şekildeki gibi yüzmektedir. Gemi, yükünü değiştirmeden nehirden açılıp özkütlesi nehir suyundan büyük olan deniz suyuna geçiyor ve orada da dengede yüzüyor. Bir denizcilik öğrencisi bu geçişte geminin durumuyla ilgili yargılar yazıyor.',ONC10,['Yalnız I','Yalnız II','Yalnız III','I ve II','II ve III'],'Buna göre, yukarıdaki yargılardan hangileri doğrudur?')
assert dg=='Yalnız I'
s10=[f'\\fill[{SIV}] (-.8,0) rectangle (6.6,1.4);','\\draw[thick] (-.8,1.4) -- (6.6,1.4);',
     '\\draw[thick,fill=gray!35] (0,2.2) -- (5.8,2.2) -- (5.2,.6) -- (.6,.6) -- cycle;','\\draw[thick,fill=white] (3.6,2.2) rectangle (4.8,3.2);','\\draw[thick,fill=white] (4.0,3.2) rectangle (4.4,3.6);',
    blk(.6,2.2,.7,.5,'','gray!60'),blk(1.4,2.2,.7,.5,'','gray!60'),blk(2.2,2.2,.7,.5,'','gray!60'),blk(1.0,2.7,.7,.5,'','gray!60'),blk(1.8,2.7,.7,.5,'','gray!60'),
    '\\node[below] at (2.9,-.05) {nehir};']
q('0010',tipId='fz-kk2-gemi',tip='Gemi, nehir ve deniz suyu',z='orta',kaz='Gemi örneğinde ağırlık, kaldırma kuvveti ve batan hacim ilişkisini sıvı özkütlesine göre yorumlar.',
 kart='K-FZKK2-10 (gemi) · nehirden denize geçiş',kalip='öncüllü',sekil=fig(*s10),metin=m,
 dogru=dg,sira=['Yalnız I','Yalnız II','Yalnız III','I ve II','II ve III'],yan=yn,
 istenen='Doğru olan yargıların hangileri olduğu.',
 ip=['Gemi iki sıvıda da yüzüyor: dengedeki bir cisimde kaldırma kuvveti ile ağırlık arasındaki ilişkiyi yaz, sonra sıvı özkütlesi değişince batan hacmin ne olacağını düşün.'],
 bilgi=[YUZ,KAL],ad=ad,
 puf='Yüzen geminin kaldırma kuvveti hep ağırlığına eşittir; özkütlesi büyük sıvıda gemi daha az batar.')

# ============ 11 · denizaltı · orta · öncüllü ============
kartla(11,'Denizaltı','Denizaltı balast tankına su alınca ağırlığı artar, hacmi (dolayısıyla kaldırma kuvveti) değişmez; net kuvvet aşağı yönlü olur ve batar.','Kaldırma kuvvetinin ağırlıkla birlikte arttığını sanmak; batan hacmin arttığını düşünmek.','orta','öncüllü',3,'fz-kk2-denizalti','Denizaltı ve balast tankı')
ONC11=[('Denizaltıya etki eden kaldırma kuvveti artar.',False,'Kaldırma kuvveti F = d_deniz × V_batan × g’dir; denizaltı zaten tamamen batık ve hacmi sabit olduğundan değişmez.','denizaltı ağırlaşınca kaldırma kuvvetinin de arttığını sanmış.'),
       ('Denizaltının ağırlığı artar.',True,'Balast tanklarına giren deniz suyu denizaltının toplam kütlesini artırır; ağırlık artar.','tanktaki suyun denizaltının ağırlığına katkı yapmadığını sanmış.'),
       ('Denizaltıya etki eden bileşke kuvvet aşağı yönlü olur ve denizaltı alçalmaya başlar.',True,'Kaldırma kuvveti sabit, ağırlık büyüdüğü için ağırlık kaldırma kuvvetini aşar; bileşke kuvvet aşağı yönlüdür.','denizaltının askıda kalmaya devam edeceğini sanmış.')]
m,dg,yn,ad=onc('Deniz suyunun içinde, şekildeki konumda hareketsiz (askıda) duran bir denizaltı, balast tanklarına deniz suyu alıyor. Tanklara su girerken denizaltının dış hacmi değişmemekte ve denizaltı deniz suyunun içinde tamamen batık kalmaktadır. Deniz suyunun özkütlesi her derinlikte aynı kabul ediliyor.',ONC11,['Yalnız I','Yalnız II','I ve II','II ve III','I, II ve III'],'Buna göre, tanklara su alınmaya başlandıktan sonra yukarıdaki yargılardan hangileri doğrudur?')
assert dg=='II ve III'
s11=[f'\\fill[{SIV}] (-.8,-.6) rectangle (7.4,3.6);','\\draw[thick] (-.8,3.6) -- (7.4,3.6);',
     '\\draw[thick,fill=gray!30] (0,1.2) .. controls (0,2.3) .. (1.2,2.3) -- (5.2,2.3) .. controls (6.4,2.3) .. (6.4,1.2) .. controls (6.4,.1) .. (5.2,.1) -- (1.2,.1) .. controls (0,.1) .. (0,1.2);',
     '\\draw[thick,fill=gray!30] (2.4,2.3) rectangle (3.6,2.95);','\\draw[thick] (3.0,2.95) -- (3.0,3.4);',
     '\\draw[thick,fill=white] (1.4,.45) rectangle (2.4,1.45);','\\node at (1.9,.95) {\\scriptsize tank};','\\draw[thick,fill=white] (4.0,.45) rectangle (5.0,1.45);','\\node at (4.5,.95) {\\scriptsize tank};',
     '\\draw[thick,fill=white] (6.4,1.2) -- (7.0,1.5) -- (7.0,.9) -- cycle;','\\draw[->,thick,vurgu] (1.9,-.4) -- (1.9,.4);','\\draw[->,thick,vurgu] (4.5,-.4) -- (4.5,.4);']
q('0011',tipId='fz-kk2-denizalti',tip='Denizaltı ve balast tankı',z='orta',kaz='Balast tankına su alan denizaltının ağırlık, kaldırma kuvveti ve hareketini yorumlar.',
 kart='K-FZKK2-11 (denizaltı) · balast tankına su alma',kalip='öncüllü',sekil=fig(*s11),metin=m,
 dogru=dg,sira=['Yalnız I','Yalnız II','I ve II','II ve III','I, II ve III'],yan=yn,
 istenen='Doğru olan yargıların hangileri olduğu.',
 ip=['Tanklara su girince denizaltının hangi özelliği değişir, hangisi değişmez?'],
 bilgi=[KAL,DEN],ad=ad,
 puf='Denizaltı derinliği, kaldırma kuvveti sabitken ağırlığı (balast suyuyla) değiştirerek ayarlanır.')

# ============ 12 · sıcak hava balonu · orta · öncüllü ============
kartla(12,'Gazların kaldırma kuvveti','Gazlar da kaldırma kuvveti uygular: F = d_hava × V × g; balon, ağırlığı kaldırma kuvvetinden küçükse yükselir, yükseldikçe hava seyreldiğinden F azalır.','Kaldırma kuvvetinin yalnız sıvılarda olduğunu sanmak; ısıtınca dış havanın kaldırma kuvvetinin arttığını düşünmek.','orta','öncüllü',3,'fz-kk2-balon','Sıcak hava balonu')
ONC12=[('Balona havanın uyguladığı kaldırma kuvveti, balonun yer değiştirdiği havanın ağırlığına eşittir.',True,'Gazlar da akışkandır; balon hacmi kadar havanın yerini tutar ve F = d_hava × V × g olur.','kaldırma kuvvetinin yalnızca sıvılarda oluştuğunu sanmış.'),
       ('Balonun içindeki hava ısıtıldığında balona etki eden kaldırma kuvveti artar.',False,'Kaldırma kuvveti, balonun yerini tuttuğu dış havanın ağırlığıdır; hacim ve dış havanın özkütlesi değişmediğinden artmaz. Isıtma, balonun içinde kalan havanın kütlesini (ağırlığını) azaltır.','ısıtılan hava yükseldiği için kaldırma kuvvetinin de arttığını sanmış.'),
       ('Balon yükseldikçe, hava seyreldiği için kaldırma kuvveti azalır.',True,'Yükseklikle havanın özkütlesi azalır; hacim sabitse F = d_hava × V × g azalır ve balon, kaldırma kuvveti ağırlığına eşit olunca dengeye gelir.','atmosferin her yükseklikte aynı özkütleye sahip olduğunu sanmış.')]
m,dg,yn,ad=onc('Şekildeki sıcak hava balonunun alt ağzı açıktır. İçindeki hava, altındaki ısıtıcı ile ısıtıldıkça genleşir ve bir kısmı alt ağızdan dışarı çıkar; balonun hacmi ise değişmez. Isıtma sürdükçe balon zeminden kalkıp yükselmeye başlıyor.',ONC12,['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III'],'Buna göre, yukarıdaki yargılardan hangileri doğrudur?')
assert dg=='I ve III'
s12=['\\draw[thick,fill=orange!20] (2.0,3.2) .. controls (0,4.2) and (0,6.8) .. (2.0,7.0) .. controls (4.0,6.8) and (4.0,4.2) .. (2.0,3.2);',
     '\\draw[thick] (1.1,3.7) -- (1.6,1.9);','\\draw[thick] (2.9,3.7) -- (2.4,1.9);','\\draw[thick,fill=brown!30] (1.4,1.1) rectangle (2.6,1.9);',
     '\\draw[thick,vurgu,fill=orange!60] (2.0,2.3) .. controls (1.8,2.7) .. (2.0,3.2) .. controls (2.2,2.7) .. (2.0,2.3);','\\node[right] at (3.3,2.6) {ısıtıcı};','\\draw[->,thin] (3.25,2.6) -- (2.2,2.5);','\\node at (2.0,5.1) {sıcak hava};',
     zemin(-.5,4.5,0.0) if False else '\\draw (-.5,1.1) -- (4.5,1.1);']
q('0012',tipId='fz-kk2-balon',tip='Sıcak hava balonu',z='orta',kaz='Gazlarda kaldırma kuvvetini ve sıcak hava balonunun yükselmesini nitel olarak yorumlar.',
 kart='K-FZKK2-12 (gazların kaldırma kuvveti) · sıcak hava balonu',kalip='öncüllü',sekil=fig(*s12),metin=m,
 dogru=dg,sira=['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III'],yan=yn,
 istenen='Doğru olan yargıların hangileri olduğu.',
 ip=['Kaldırma kuvvetinin hangi akışkanın özkütlesine ve hangi hacme bağlı olduğunu düşün; ısıtma bu niceliklerden hangisini değiştirir?'],
 bilgi=[B('Gazlarda kaldırma kuvveti','hava gibi gazlar da cisimlere kaldırma kuvveti uygular: F = d_hava × V × g. Örnek: 1 m³ hacimli bir cisme, özkütlesi 1,2 kg/m³ olan havada 12 N’luk kaldırma kuvveti etki eder (g = 10 m/s²)'),YUZ],ad=ad,
 puf='Gazlarda da F = d_akışkan × V × g; balon, içindeki gazı ısıtarak ağırlığını azaltır, kaldırma kuvvetini değil.')

# ============ 13 · areometre · orta ============
kartla(13,'Areometre','Areometrede ağırlık sabit olduğundan kaldırma kuvveti de sabittir: d × h sabit; batan boy ile sıvı özkütlesi ters orantılıdır.','Doğru orantı kurmak; batan boyun farkını özkütle farkı sanmak.','orta','şekilli',3,'fz-kk2-areometre','Areometre ile sıvı özkütlesi')
hsu,hX,hY=12,10,15; dX=Fr(1)*hsu/hX; dY=Fr(1)*hsu/hY
assert dX==Fr(6,5) and dY==Fr(4,5) and dX-dY==Fr(2,5) and dX-1==Fr(1,5) and Fr(hY-hX,hX)==Fr(1,2) and dX+dY==2
def areo(x,hb,sivlv=3.8,col=SIV):
    # kap + areometre: batan boy hb cm (1 cm = .22 çizim); alt uca küçük yük
    s=kap(x-1.2,3.0,4.6,sivlv,col=col)
    yb=sivlv-hb*.22; assert yb>.3
    s+=f'\\draw[thick,fill=white] ({x-.12},{yb}) rectangle ({x+.12},4.4);\\draw[thick,fill=gray!60] ({x-.12},{yb}) rectangle ({x+.12},{yb+.15});'
    s+=olc(x+.45,yb,sivlv,f'${hb}$ cm',sol=False)
    return s
s13=[areo(1.4,hsu),areo(5.0,hX,col='orange!25'),areo(8.6,hY,col='blue!12'),'\\node[below] at (1.7,-.05) {su};','\\node[below] at (5.3,-.05) {X};','\\node[below] at (8.9,-.05) {Y};']
q('0013',tipId='fz-kk2-areometre',tip='Areometre ile sıvı özkütlesi',z='orta',kaz='Areometrenin batan boylarından sıvıların özkütlelerini karşılaştırarak özkütle farkını bulur.',
 kart='K-FZKK2-13 (areometre) · su, X ve Y sıvıları',kalip='şekilli',sekil=fig(*s13),
 metin='Düzgün silindir biçimli ince bir çubuğun alt ucuna, hacmi ihmal edilebilecek kadar küçük bir yük yapıştırılarak basit bir areometre hazırlanıyor. Areometre, özkütlesi 1 g/cm³ olan suda, X sıvısında ve Y sıvısında sırayla yüzdürülüyor ve her seferinde dik ve dengede kalıyor. Areometrenin her sıvıda batan boyu şekilde gösterilmiştir; çubuğun üst ucu sıvıdan hep dışarıdadır.\nBuna göre, X sıvısının özkütlesi ile Y sıvısının özkütlesi arasındaki fark (d_X − d_Y) kaç g/cm³’tür?',
 dogru=Fr(2,5),yan=[(Fr(1,5),'Yalnız X’in özkütlesini suyla karşılaştırmış (d_X − d_su = 1,2 − 1).','dikkat'),(Fr(1,2),'Batan boylar farkını X’in boyuna oranlamış: (15 − 10) ÷ 10.','islem'),(Fr(6,5),'Yalnız X’in özkütlesini bulup farkı almamış.','dikkat'),(2,'Özkütleleri toplamış (1,2 + 0,8).','islem')],
 istenen='X ve Y sıvılarının özkütlelerinin farkı, d_X − d_Y (g/cm³).',
 ip=['Areometre her sıvıda yüzdüğüne göre kaldırma kuvveti hep aynı; kesit sabit olduğundan batan boy ile sıvı özkütlesi arasındaki bağıntıyı kur.'],
 bilgi=[YUZ,B('Areometre','düzgün silindir gövdeli areometrede ağırlık sabit olduğundan kaldırma kuvveti de sabittir: d × h sabittir. Örnek: bir sıvıda 6 cm batan areometre, özkütlesi bunun 2 katı olan sıvıda 3 cm batar')],
 ad=[A('Sabit çarpım','Kesit alanı A olsun; kaldırma kuvveti her sıvıda ağırlığa eşittir.','d × A × h × g = G → d × h = sabit'),A('X sıvısı','Su ile X’i eşitle.','1 × 12 = d_X × 10 → d_X = 1,2 g/cm³'),A('Y sıvısı','Su ile Y’yi eşitle.','1 × 12 = d_Y × 15 → d_Y = 0,8 g/cm³'),A('Fark','İki özkütlenin farkı alınır.','1,2 − 0,8 = 0,4 g/cm³')],
 puf='Areometrede batan boy sıvı özkütlesiyle ters orantılıdır: özkütlesi büyük sıvıda areometre daha az batar.')

# ============ 14 · X'te yüzen, Y'de dinamometreli · zor ============
kartla(14,'Farklı sıvılarda aynı cisim','Aynı cisim X’te yüzüyorsa d_X × V_batan = G; Y’de tamamen batık ve tabanda duruyorsa F_Y = G − N; iki bağıntıdan sıvıların özkütle oranı bulunur.','Yüzen cisimde batan oranı kullanmamak; tabanın tepki kuvvetini kaldırma kuvveti sanmak.','zor','şekilli',5,'fz-kk2-yuzen-dino','Biri yüzen biri tabanda duran iki sıvı durumu')
G14,N14,fx=60,20,Fr(3,4); FY14=G14-N14; r14=(Fr(G14)/fx)/FY14
assert FY14==40 and r14==2 and Fr(G14,FY14)==Fr(3,2) and Fr(G14,N14)==3 and Fr(G14)/(fx*N14)==4 and FY14/(Fr(G14)/fx)==Fr(1,2)
# cisim her yerde 1,2 × 1,2 cm; X'te 3/4'ü batık (0,9 cm)
CB=1.2
s14=[blk(.2,.3,CB,CB,'cisim'),'\\draw[->,thick,vurgu] (.8,.9) -- (.8,-.4);','\\node[right] at (.95,-.15) {$60$ N};','\\node[below] at (.8,-.95) {(a)};',
     kap(2.4,2.8,3.0,2.2),blk(3.1,2.2-.75*CB,CB,CB,'cisim'),'\\node[below] at (3.8,-.05) {X sıvısı};',
     f'\\draw[<->,thin] (5.6,{2.2-.75*CB:.2f}) -- (5.6,2.2);','\\node[right] at (5.6,1.75) {\\small $3/4$ batık};',
     kap(7.9,2.8,3.0,2.2,col='orange!25'),blk(8.6,0,CB,CB,'cisim'),'\\draw[->,thick,vurgu] (9.2,-.6) -- (9.2,0);','\\node[right] at (9.3,-.3) {$20$ N};','\\node[below] at (9.3,-1.0) {Y sıvısı};']
q('0014',tipId='fz-kk2-yuzen-dino',tip='Biri yüzen biri tabanda duran iki sıvı durumu',z='zor',kaz='X’te yüzen, Y’de tabanda duran aynı cismin sıvılarının özkütle oranını bulur.',
 kart='K-FZKK2-14 (farklı sıvılarda aynı cisim) · X’te yüzme, Y’de tabanın tepkisi',kalip='şekilli',sekil=fig(*s14),
 metin='Aynı homojen cisim üç ayrı durumda gösterilmiştir: (a) cismin ağırlığı, X sıvısında yüzerken ve Y sıvısında kabın tabanında hareketsiz dururken. Şekilde cismin ağırlığı, X sıvısındaki batan oranı ve Y sıvısında kabın tabanının cisme uyguladığı tepki kuvveti (yeşil oklar) verilmiştir. Cisim Y sıvısında tamamen batıktır.\nBuna göre, d_X ÷ d_Y oranı kaçtır?',
 dogru=2,yan=[(Fr(1,2),'Oranı ters kurmuş: d_Y ÷ d_X hesaplamış.','islem'),(Fr(3,2),'X’teki batan oranı kullanmayı atlamış; G ÷ F_Y hesaplamış.','dikkat'),(3,'Tabanın tepkisini (20 N) kaldırma kuvveti sanmış; batan oranı da hesaba katmamış (60 ÷ 20).','dikkat'),(4,'Tabanın tepkisini kaldırma kuvveti sanmış (F_Y = 20 N): 60 ÷ (3/4 × 20).','dikkat')],
 istenen='X ve Y sıvılarının özkütle oranı (d_X ÷ d_Y).',
 ip=['Cisim her iki kapta da durgun: cisme etkiyen kuvvetleri belirleyip her kap için denge koşulunu yaz.'],
 bilgi=[YUZ,KAL,DEN],
 ad=[A('X sıvısında denge','Cisim yüzdüğü için kaldırma kuvveti ağırlığına eşittir.','F_X = G = 60 N'),A('V cinsinden yaz','Batan hacim, hacmin 3/4’üdür.','d_X × (3V ÷ 4) × g = 60 → d_X × V × g = 80 N'),A('Y sıvısında kaldırma kuvveti','Tamamen batık cisimde kaldırma kuvveti ile tabanın tepkisi birlikte ağırlığı dengeler.','F_Y + 20 = 60 → F_Y = 40 N → d_Y × V × g = 40 N'),A('Oranla','İki bağıntıyı birbirine böl; V ve g sadeleşir.','d_X ÷ d_Y = 80 ÷ 40 = 2')],
 puf='Yüzen cisimde önce tamamen batık olsaydı kaldırma kuvvetinin ne olacağını (d × V × g) bul; böylece farklı sıvılar aynı ölçekte karşılaştırılır.')

# ============ 15 · iple bağlı iki cisim · zor · öncüllü ============
kartla(15,'İple bağlı cisimler','Birbirine iple bağlı, biri kısmen biri tamamen batık eşit hacimli cisimlerde toplam kaldırma kuvveti toplam ağırlığa eşittir; ip gerildiği için üstteki cisim sıvıdan hafif (yarısından bile), alttaki ise sıvıdan yoğundur.','İpin gerildiğini hesaba katmamak; her cismi ayrı yüzüyormuş gibi düşünmek.','zor','öncüllü',4,'fz-kk2-bagli-cisimler','İple bağlı iki cismin dengesi')
ONC15=[('X cisminin özkütlesi, sıvının özkütlesinin yarısından büyüktür.',False,'X için F_X = d_sıvı × (V ÷ 2) × g ve G_X = F_X − T’dir (T > 0). Buradan G_X < d_sıvı × V × g ÷ 2 olur; yani d_X < d_sıvı ÷ 2’dir. Öncül I yanlıştır.','ip olsa da X’in tek başına yüzüyormuş gibi batan oranının özkütle oranına eşit olacağını sanmış.'),
       ('Y cisminin özkütlesi, sıvının özkütlesinden büyüktür.',True,'Y’de F_Y + T = G_Y ve T > 0 olduğundan G_Y > F_Y yani d_Y > d_sıvı’dır.','alttaki cismin tamamen batık olduğu için sıvıdan daha az yoğun olması gerektiğini sanmış.'),
       ('İp kesilirse X cisminin sıvıdaki batan hacmi azalır.',True,'İp gerilmesi X’i aşağı çekiyordu; ip kesilince X yalnız d_X ÷ d_sıvı oranı kadar batar. Bu oran 1/2’den küçük olduğundan batan hacim azalır.','ipin kesilmesinin X’in batan hacmini etkilemeyeceğini sanmış.')]
# sayısal sağlama: örnek değerler  d=1000, V=1: X batan 1/2, Y tam. Denge: F_X+F_Y = G_X+G_Y → d_X+d_Y = 1,5 d
d_s=1000; dX15=300; dY15=1200; assert dX15+dY15==Fr(3,2)*d_s
T15=Fr(dY15-d_s,1); assert T15>0 and d_s*Fr(1,2)-dX15==T15 and dX15<d_s/2 and dY15>d_s
yeni_oran=Fr(dX15,d_s); assert yeni_oran<Fr(1,2)
m,dg,yn,ad=onc('Eşit hacimli X ve Y cisimleri hafif bir iple birbirine bağlanıp bir sıvıya bırakılıyor. Cisimler şekildeki gibi dengede kalıyor: X cisminin hacminin yarısı sıvının içinde, Y cismi ise sıvının içinde tamamen batıktır ve ip gergindir. İp esnemez ve kütlesi ihmal edilir; cisimler kabın tabanına değmemektedir.',ONC15,['Yalnız I','Yalnız III','I ve II','I ve III','II ve III'],'Buna göre, yukarıdaki yargılardan hangileri doğrudur?')
assert dg=='II ve III'
s15=[kap(0,3.6,4.6,3.9),blk(1.0,3.05,1.2,.0+1.2,'X'),blk(1.0,.9,1.2,1.2,'Y'),'\\draw[thick] (1.6,2.1) -- (1.6,3.05);','\\node[right] at (1.75,2.6) {ip};']
s15[1]=blk(1.0,3.0,1.2,1.2,'X')
# X: yarısı batık → alt kenarı su seviyesi (3.9) − 0.6 = 3.3
s15[1]=blk(1.0,3.3,1.2,1.2,'X')
s15[3]='\\draw[thick] (1.6,2.1) -- (1.6,3.3);'
s15[4]='\\node[right] at (1.75,2.7) {ip};'
q('0015',tipId='fz-kk2-bagli-cisimler',tip='İple bağlı iki cismin dengesi',z='zor',kaz='Biri kısmen biri tamamen batık, iple bağlı iki cismin özkütle ve kuvvet ilişkilerini yorumlar.',
 kart='K-FZKK2-15 (iple bağlı cisimler) · X kısmen, Y tamamen batık',kalip='öncüllü',sekil=fig(*s15),metin=m,
 dogru=dg,sira=['Yalnız I','Yalnız III','I ve II','I ve III','II ve III'],yan=yn,
 istenen='Doğru olan yargıların hangileri olduğu.',
 ip=['Her cisim için kuvvet dengesini ayrı yaz: ip X’i aşağı, Y’yi yukarı çeker; ip gerilmesinin sıfırdan büyük olduğunu da kullan.'],
 bilgi=[KAL,DEN,YUZ],ad=ad,
 puf='İple bağlı cisimlerde ip gerilmesi sıfırdan büyükse üstteki cisim kendi kaldırma kuvvetinden hafiftir, alttaki cisim ise kendi kaldırma kuvvetinden ağırdır.')

# ============ 16 · taşırma kabı + yağ · kolay ============
kartla(16,'Taşırma kabı','Batan cisim kendi hacmi kadar sıvıyı taşırır; taşan sıvının kütlesi, hacmi ile sıvının özkütlesinin çarpımıdır, cismin kütlesi değil.','Taşan sıvının kütlesini cismin kütlesine eşit sanmak; hacmi özkütleye bölmek.','kolay','şekilli',3,'fz-kk2-tasirma-yag','Taşan sıvının kütlesi')
m16,V16,dy16=360,300,Fr(8,10); dbl=Fr(m16,V16); tasan=dy16*V16
assert dbl==Fr(6,5)>dy16 and tasan==240 and Fr(V16,1)/dy16==375 and Fr(m16)/dy16==450
s16=[kap(0,2.6,2.8,2.2,col='yellow!25',tas=.6),blk(.8,0,1.0,.8,'','gray!45'),'\\node[right] at (-.2,3.6) {blok: $m=360$ g, $V=300$ cm$^3$};','\\draw[->,thin] (1.3,3.35) -- (1.3,1.3);',
     kap(2.75,.9,1.5,.4,col='yellow!25'),'\\draw[->,thin] (3.2,1.95) -- (3.2,.55);','\\node[below] at (1.3,-.05) {yağ: $0{,}8$ g/cm$^3$};','\\node[right] at (3.8,.6) {ölçü kabı};']
q('0016',tipId='fz-kk2-tasirma-yag',tip='Taşan sıvının kütlesi',z='kolay',kaz='Taşırma kabına bırakılan cismin yerini aldığı sıvının kütlesini hesaplar.',
 kart='K-FZKK2-16 (taşırma kabı, yağ) · taşan yağın kütlesi',kalip='şekilli',sekil=fig(*s16),
 metin='Bir laboratuvar çalışmasında ağzına kadar yağ dolu bir taşırma kabının borusunun ucuna boş bir ölçü kabı yerleştiriliyor. Kütlesi ve hacmi ile yağın özkütlesi şekilde verilen homojen bir blok, kaba yavaşça bırakılıyor ve bloğun kabın tabanına inip orada durduğu görülüyor. Kabın borusundan akan yağın tamamı ölçü kabında toplanıyor ve hiçbir sıvı başka yere gitmiyor.\nBuna göre, ölçü kabında biriken yağın kütlesi kaç g’dır?',
 dogru=240,yan=[(300,'Taşan yağın hacminin (300 cm³) sayısal değerini kütle sanmış; özkütle ile çarpmayı atlamış.','dikkat'),(360,'Bloğun yüzdüğünü sanıp taşan sıvının kütlesini bloğun kütlesine eşit almış.','bilgi'),(375,'Taşan hacmi yağın özkütlesine bölmüş (300 ÷ 0,8).','islem'),(450,'Bloğun kütlesini yağın özkütlesine bölmüş (360 ÷ 0,8).','islem')],
 istenen='Ölçü kabında biriken yağın kütlesi (g).',
 ip=['Blok tabana battığına göre taşan yağın hacmi hangi niceliğe eşittir; bu hacimdeki yağın kütlesi nasıl bulunur?'],
 bilgi=[B('Özkütle','d = m ÷ V; kütle m = d × V. Örnek: özkütlesi 2 g/cm³ olan 10 cm³ maddenin kütlesi 20 g’dır'),KAL],
 ad=[A('Blok yüzer mi?','Bloğun özkütlesi yağınkiyle karşılaştırılır; blok tabanda durduğuna göre tamamen batıktır.','d_blok = 360 ÷ 300 = 1,2 > 0,8 g/cm³'),A('Taşan hacim','Tamamen batan blok kendi hacmi kadar yağı taşırır.','V_taşan = 300 cm³'),A('Taşan yağın kütlesi','Kütle, özkütle ile hacmin çarpımıdır.','m = 0,8 × 300 = 240 g')],
 puf='Tamamen batan cisim kendi hacmi kadar sıvı taşırır; taşan sıvının kütlesi hacim × sıvının özkütlesidir, cismin kütlesi değildir.')

bitir(P,'kaldirmaiki','fiz|Sıvıların Kaldırma Kuvveti')
