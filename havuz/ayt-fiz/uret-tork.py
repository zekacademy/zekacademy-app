"""AYT Fizik · Tork Denge · 20 soru (kardeş yok, ipucu 1). Şekiller TikZ; koordinatlar ve her sayı Python'da hesaplanıp assert edilir."""
import sys,os,json
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-fiz'))
import _hafif as H
from _hafif import *
from cizim import tikz_svg
from math import radians,sin,cos,sqrt
P=Parti('tork','Tork Denge','afiz|Tork Denge',ders='AYT Fizik',idon='aytfiz')
H.KONU='Tork Denge'
ALT='Tork ve Denge'
KURS={}
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip):
    kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,'ÖSYM AYT 2018–2026 Fizik (yalnız mantık) · 345 AYT Fizik Soru Bankası · MEB 11. sınıf fizik')
    KURS[tipId]=id
def q(no,**k):
    assert len(k['ip'])==1
    mk(P,no,adim=len(k['ad']),ad=k.pop('ad'),**k)
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
ARR='-{Stealth[length=2mm,width=1.8mm]}'
CNT=[0]
def nid():
    CNT[0]+=1; return f'n{CNT[0]}'
# ---------- çizim yardımcıları (bar: merkez y, kalınlık .2) ----------
def bar(L,U,x0=0.0,y=0.0,fill='gray!20',ticks=True):
    s=f'\\draw[thick,fill={fill}] ({x0:.3f},{y-.1:.3f}) rectangle ({x0+L*U:.3f},{y+.1:.3f});'
    if ticks:
        for i in range(1,L): s+=f'\\draw[thin] ({x0+i*U:.3f},{y-.1:.3f}) -- ({x0+i*U:.3f},{y+.1:.3f});'
    return s
def wt(x,lab,drop=1.1,y=0.0,w=.9):
    n=nid()
    return (f'\\node[draw,thick,fill=gray!35,minimum width={w}cm,minimum height=.55cm,inner sep=1.5pt] ({n}) at ({x:.3f},{y-.1-drop:.3f}) {{{lab}}};'
            f'\\draw[thick] ({x:.3f},{y-.1:.3f}) -- ({n}.north);')
def tri(x,y=0.0,h=.55,w=.5,lab=None,fill='gray!55'):
    s=f'\\draw[thick,fill={fill}] ({x-w:.3f},{y-.1-h:.3f}) -- ({x+w:.3f},{y-.1-h:.3f}) -- ({x:.3f},{y-.1:.3f}) -- cycle;'
    s+=f'\\fill[gray!35] ({x-w-.35:.3f},{y-.1-h-.12:.3f}) rectangle ({x+w+.35:.3f},{y-.1-h:.3f}); \\draw[thick] ({x-w-.35:.3f},{y-.1-h:.3f}) -- ({x+w+.35:.3f},{y-.1-h:.3f});'
    if lab: s+=f'\\node[below] at ({x:.3f},{y-.1-h-.12:.3f}) {{{lab}}};'
    return s
def ceil(a,b,y,t=.2):
    return f'\\fill[gray!35] ({a:.3f},{y:.3f}) rectangle ({b:.3f},{y+t:.3f}); \\draw[thick] ({a:.3f},{y:.3f}) -- ({b:.3f},{y:.3f});'
def wall(x,y0,y1,t=.25):
    return f'\\fill[gray!35] ({x-t:.3f},{y0:.3f}) rectangle ({x:.3f},{y1:.3f}); \\draw[thick] ({x:.3f},{y0:.3f}) -- ({x:.3f},{y1:.3f});'
def floor(a,b,y,t=.2):
    return f'\\fill[gray!35] ({a:.3f},{y-t:.3f}) rectangle ({b:.3f},{y:.3f}); \\draw[thick] ({a:.3f},{y:.3f}) -- ({b:.3f},{y:.3f});'
def rope(x,y0,y1): return f'\\draw[thick] ({x:.3f},{y0:.3f}) -- ({x:.3f},{y1:.3f});'
def lab(x,y,t,pos='above'): return f'\\node[{pos}] at ({x:.3f},{y:.3f}) {{{t}}};'
def harf(x,y,t): return f'\\node[above] at ({x:.3f},{y:.3f}) {{{t}}};'
def hinge(x,y): return f'\\draw[thick,fill=white] ({x:.3f},{y:.3f}) circle (.09);'
def fig(*parts): return tikz_svg(HEAD+'\n'.join(parts)+TAIL)
def onc(truth,reasons,sira):
    """öncüllü: truth {'I':bool,..}; reasons {'I':'doğru olgu cümlesi'}; sira şık etiketleri → (dogru, yan[(etiket,cel,tur)], adimlar)"""
    def kume(l): return set(('I','II','III')) if l=='I, II ve III' else set(x for x in l.replace('Yalnız ','').replace(' ve ',' ').split())
    gercek={k for k,v in truth.items() if v}
    dog=[l for l in sira if kume(l)==gercek]; assert len(dog)==1,(sira,gercek)
    yan=[]
    for l in sira:
        if l==dog[0]: continue
        k=kume(l); c=[]
        for x in ('I','II','III'):
            if x in k and x not in gercek: c.append(f'{x}. öncülü doğru saymış, oysa yanlıştır: {reasons[x]}')
            if x in gercek and x not in k: c.append(f'{x}. öncülünü yanlış saymış, oysa doğrudur: {reasons[x]}')
        yan.append((l,' '.join(c),'bilgi'))
    ad=[A(f'{x}. öncülü incele',reasons[x],f'{x}: '+('doğru' if truth[x] else 'yanlış')) for x in ('I','II','III')]
    ad.append(A('Sonuca var','Doğru öncülleri birleştir.',f'Doğru: '+', '.join(x for x in ('I','II','III') if truth[x])))
    return dog[0],yan,ad
S5=['Yalnız I','Yalnız II','I ve II','I ve III','II ve III']
B_TORK=B('Tork','τ = F · d; d, kuvvetin dönme noktasına olan dik uzaklığıdır (kuvvet kolu). Dönme noktasından geçen kuvvetin torku sıfırdır. Örnek: 10 N’luk kuvvet dönme noktasından 3 m uzakta çubuğa dik uygulanırsa τ = 30 N·m')
B_DENGE=B('Denge şartları','Cisim dengede ise bileşke kuvvet sıfırdır (ΣF = 0) ve herhangi bir noktaya göre net tork sıfırdır (Στ = 0): saat yönündeki torkların toplamı, saat yönünün tersindeki torkların toplamına eşittir. Örnek: bir noktanın iki yanında 20 N · 1 m ile 10 N · 2 m dengelenir')
B_DUZGUN=B('Düzgün türdeş çubuk','ağırlığı tek bir kuvvet olarak geometrik merkezine etki eder; eşit bölmeli çubukta ağırlık, çubuğun orta noktasındadır. Örnek: 6 bölmeli çubukta ağırlık uçtan 3. bölmededir')
g=10
# ================= KARTLAR =================
kartla('K-AFTORK-01','Kaldıraç dengesi, destek tepkisi','Destek noktasına göre torklar eşitlenir; destek tepkisi çubuğa etki eden aşağı kuvvetlerin toplamına eşittir.','Kolları ters kullanmak; destek tepkisini yalnız bir ağırlığa eşit almak; çubuğun ağırlığını atlamak.','kolay','şekilli',3,'tork-kaldirac','Kaldıraç dengesi ve destek tepkisi')
kartla('K-AFTORK-02','İp gerilmeleri (iki ip, ağırlıklı çubuk)','Bir ipin bağlandığı noktaya göre tork alınır; çubuk ve cismin ağırlıkları kollarıyla çarpılır, diğer ip bulunur.','Çubuğun ağırlığını ihmal etmek; ağırlıkları iplere eşit paylaştırmak.','orta','şekilli',4,'tork-ip','Çubuk ve levhada ip gerilmeleri')
kartla('K-AFTORK-03','Menteşeli çubuk, ip gerilmesi ve menteşe tepkisi','Menteşeye göre tork alınır; eğik ipte yalnız çubuğa dik bileşen tork yapar; menteşe tepkisi kuvvet dengesinden bulunur.','Eğik ipin tamamını dik sanmak; tepkiyi ip gerilmesine eşitlemek; sin–cos karıştırmak.','zor','şekilli',5,'tork-mentese','Menteşeli çubukta gerilme ve tepki')
kartla('K-AFTORK-04','İki destekli çubuk, devrilme sınırı','Desteklerden biri için tepki sıfır olduğunda devrilme sınırıdır; diğer destekten tork alınır.','Devrilme sınırında iki tepkinin de sıfırdan farklı olduğunu sanmak; kolları karıştırmak.','zor','şekilli',4,'tork-destek','İki desteğe oturan çubuk, tepkiler ve devrilme')
kartla('K-AFTORK-05','Kavramsal tork–denge öncülleri','Cismin konumu veya ip değişince gerilme, tepki ve torkların nasıl değiştiği nicel ilişkilerden (τ = F·d) çıkarılır.','Net torkun dengede de sıfır olduğunu unutmak; tepkiyi gerilmeyle aynı yönde değiştirmek.','orta','öncüllü',3,'tork-kavram','Denge durumunda niceliklerin değişimi')
kartla('K-AFTORK-06','Düğüm noktasında kuvvet dengesi','Düğüme etki eden ip kuvvetleri bileşenlerine ayrılır; yatay ve düşeyde ayrı ayrı ΣF = 0 yazılır.','sin ve cos bileşenlerini karıştırmak; gerilmeyi ağırlığa eşitlemek.','orta','şekilli',3,'tork-dugum','Düğüm noktası ve ip gerilmeleri')
kartla('K-AFTORK-07','Merdiven dengesi','Sürtünmesiz duvara dayalı merdivende zemine göre tork alınarak duvar tepkisi bulunur; yatay dengeden zemin sürtünmesi duvar tepkisine eşittir.','Yatay kolları yerine merdiven boyunu kullanmak; üstteki kişinin konumunu yanlış almak.','zor','şekilli',5,'tork-merdiven','Duvara dayalı merdiven')
kartla('K-AFTORK-08','Tork grafiği (T–x)','Grafikten gerilme–konum ilişkisi okunur; ipin bağlandığı uçtaki değer cismin ağırlığını verir.','Gerilmeyi menteşe tepkisi sanmak; eğimi tepki saymak.','zor','grafik',4,'tork-grafik','Gerilme–konum grafiği')
kartla('K-AFTORK-09','Mobil (iç içe çubuklar)','Alttaki çubuğun toplam ağırlığı üsttekinin ucundaki tek kuvvet gibi alınır; çubuklar sırayla dengelenir.','Alt sistemi yok sayıp yalnız bir ağırlığı almak; gerilmeyi bölme olarak kullanmak.','zor','şekilli',4,'tork-mobil','İç içe çubuklardan oluşan mobil')

# ================= 01 · kolay · kaldıraç =================
U=.75; L=6
sk=fig(tri(2*U,y=0,h=.8,lab=None),bar(L,U),wt(0,'$30$ N',1.0),wt(L*U,'$P$',1.0),
       f'\\node[above] at ({2*U:.3f},.1) {{destek}};')
W1=30; a1,a2=2,4; Pw=Fr(W1*a1,a2); assert Pw==15 and a1+a2==L
q('0001',tipId='tork-kaldirac',tip='Kaldıraç dengesi ve destek tepkisi',z='kolay',alt=ALT,kaz='Ağırlıksız çubukta destek noktasına göre tork eşitliği yazarak bilinmeyen ağırlığı bulur.',
 kart='K-AFTORK-01 (kaldıraç) · 30 N, kollar 2 ve 4 bölme',kalip='şekilli',
 metin='Ağırlığı önemsiz, eşit bölmeli bir çubuk, şekildeki gibi bir destek üzerinde yatay dengededir. Çubuğun uçlarına ağırlıkları 30 N ve P olan cisimler ipler ile asılmıştır.\nBuna göre, P ağırlığı kaç N’dur?',
 dogru=15,yan=[(10,'Sağ kolu 6 bölme (tüm çubuk boyu) almış: 30 · 2 = P · 6 → P = 10 N.','dikkat'),(20,'Sağ kolu 3 bölme sanmış: 30 · 2 = P · 3 → P = 20 N.','dikkat'),(30,'İki ucu desteğe göre eşit uzak sanıp ağırlıkları eşitlemiş.','bilgi'),(60,'Kolları ters yazmış: P · 2 = 30 · 4 → P = 60 N.','islem')],
 istenen='Sağ uca asılı cismin ağırlığı P (N).',ip=['Destek noktasını dönme noktası al; her kuvvetin desteğe olan uzaklığını bölme sayarak belirle.'],
 bilgi=[B_TORK,B_DENGE],
 ad=[A('Kolları oku','Destekten sol uca 2, sağ uca 4 bölme vardır.','d₁ = 2, d₂ = 4'),A('Tork eşitliği yaz','Saat yönünün tersindeki ve saat yönündeki torklar eşittir.','30 × 2 = P × 4'),A('Çöz','Eşitliği P için çöz.','P = 60 ÷ 4 = 15 N')],
 puf='Dengedeki kaldıraçta ağırlık × kol çarpımı iki yanda eşittir; kuvvet büyükse kol küçüktür.',sekil=sk)

# ================= 02 · kolay · destek tepkisi =================
U=.8; L=5
sk=fig(tri(1*U,h=.5,w=.3),bar(L,U),wt(0,'$40$ N',1.25),wt(L*U,'$10$ N',1.25))
N2=40+10; assert 40*1==10*4 and N2==50
q('0002',tipId='tork-kaldirac',tip='Kaldıraç dengesi ve destek tepkisi',z='kolay',alt=ALT,kaz='Dengedeki çubukta kuvvet dengesinden destek tepkisini bulur.',
 kart='K-AFTORK-01 (destek tepkisi) · 40 N ve 10 N, kollar 1 ve 4 bölme',kalip='şekilli',
 metin='Ağırlığı önemsiz, eşit bölmeli bir çubuk, şekildeki gibi bir destek üzerinde yatay dengededir. Çubuğun uçlarına 40 N ve 10 N ağırlığında iki cisim asılmıştır.\nBuna göre, desteğin çubuğa uyguladığı tepki kuvvetinin büyüklüğü kaç N’dur?',
 dogru=50,yan=[(25,'İki ağırlığın ortalamasını almış: (40 + 10) ÷ 2 = 25 N.','bilgi'),(30,'Farkı alıp 30 N bulmuş; oysa tepki toplam ağırlığa eşittir.','bilgi'),(40,'Yalnız büyük ağırlığın tepkisini düşünmüş: 40 N.','dikkat'),(80,'Torkların toplamını tepki sanmış: 40 · 1 + 10 · 4 = 80.','islem')],
 istenen='Desteğin çubuğa uyguladığı tepki kuvveti (N).',ip=['Çubuk durgun olduğuna göre çubuğa yukarı ve aşağı yönde etki eden kuvvetleri karşılaştır.'],
 bilgi=[B_DENGE,B('Destek tepkisi','destek, çubuğa yukarı yönde tepki uygular; ağırlıksız çubukta tepki, asılı cisimlerin ağırlıkları toplamına eşittir. Örnek: 5 N ve 15 N asılıysa tepki 20 N’dur')],
 ad=[A('Torku kontrol et','Destekten uçlara olan uzaklıklar 1 ve 4 bölmedir.','40 × 1 = 10 × 4 = 40 → denge sağlanır'),A('Kuvvet dengesi yaz','Yukarı kuvvet (tepki), aşağı kuvvetlerin toplamına eşittir.','N = 40 + 10'),A('Sonucu bul','Toplamı hesapla.','N = 50 N')],
 puf='Düşeyde dengedeki çubuğa etki eden yukarı kuvvetlerin toplamı, aşağı kuvvetlerin toplamına eşittir.',sekil=sk)

# ================= 03 · kolay · öncüllü (şeksiz) =================
tr={'I':True,'II':True,'III':False}
rs={'I':'Dengedeki çubuk ivmelenmez; bileşke kuvvet sıfırdır.','II':'Dönmeyen (dengedeki) çubukta herhangi bir noktaya göre net tork sıfırdır.','III':'Tepki, çubuğun ağırlığı ile asılı cismin ağırlığının toplamına (G + P) eşittir; yalnız G’ye eşit değildir.'}
d,y,ad=onc(tr,rs,S5)
q('0003',tipId='tork-kavram',tip='Denge durumunda niceliklerin değişimi',z='kolay',alt=ALT,kaz='Denge şartlarını (net kuvvet ve net tork) kavramsal olarak yorumlar.',
 kart='K-AFTORK-05 (denge şartları) · düzgün çubuk + asılı cisim',kalip='öncüllü',
 metin='Ağırlığı G olan düzgün ve türdeş bir çubuk, bir ucuna ağırlığı P olan bir cisim asılı hâlde bir destek üzerinde yatay ve durgun biçimde dengededir.\nBuna göre;\nI. Çubuğa etki eden kuvvetlerin bileşkesi sıfırdır.\nII. Çubuğa etki eden net tork, her noktaya göre sıfırdır.\nIII. Desteğin çubuğa uyguladığı tepki kuvveti G’ye eşittir.\nyargılarından hangileri doğrudur?',
 dogru=d,yan=[(a,b,c) for a,b,c in y],sira=S5,istenen='Doğru olan yargılar.',ip=['Denge şartlarını (bileşke kuvvet ve net tork) ayrı ayrı değerlendir; desteğin çubuğa uyguladığı kuvvetin neyi dengelediğini düşün.'],
 bilgi=[B_DENGE],ad=ad,puf='Dengede hem bileşke kuvvet hem net tork sıfırdır.')

# ================= 04 · orta · iki ip, ağırlıklı çubuk =================
U=.65; L=6
sk=fig(ceil(-.3,L*U+.3,1.5),rope(0,.1,1.5),rope(L*U,.1,1.5),bar(L,U),wt(2*U,'$60$ N',1.1),
       f'\\node[left] at (-.1,.9) {{K}}; \\node[right] at ({L*U+.1:.3f},.9) {{L}};')
Wc,Wk=30,60; TL=Fr(Wk*2+Wc*3,6); TK=Wk+Wc-TL; assert TL==35 and TK==55
assert Fr(Wk*2,6)==20 and Fr(Wc*3,6)*1==Fr(15) and Fr(Wk+Wc,2)==45
q('0004',tipId='tork-ip',tip='Çubuk ve levhada ip gerilmeleri',z='orta',alt=ALT,kaz='Ağırlıklı çubuğun iki ucundaki ip gerilmelerini tork dengesiyle hesaplar.',
 kart='K-AFTORK-02 (iki ip) · çubuk 30 N, cisim 60 N, kollar 2 ve 3 bölme',kalip='şekilli',
 metin='Ağırlığı 30 N olan düzgün ve türdeş, eşit bölmeli bir çubuk, uçlarına bağlı K ve L düşey ipleri ile tavandan yatay olarak asılmıştır. Çubuğun K ucundan 2 bölme uzağa 60 N ağırlığında bir cisim asılarak sistem dengelenmiştir.\nBuna göre, L ipindeki gerilme kuvvetinin büyüklüğü kaç N’dur?',
 dogru=35,yan=[(15,'Yalnız çubuğun ağırlığının payını (30 · 3 ÷ 6) bulmuş; cismin etkisini katmamış.','dikkat'),(20,'Çubuğun ağırlığını hesaba katmamış: 60 · 2 ÷ 6 = 20 N.','dikkat'),(45,'Toplam ağırlığı (90 N) iki ipe eşit paylaştırmış.','bilgi'),(55,'K ipindeki gerilmeyi bulmuş: 90 − 35 = 55 N.','dikkat')],
 istenen='L ipindeki gerilme kuvveti (N).',ip=['K ucunu dönme noktası kabul edip L ipinin torkunu, çubuğun ve cismin ağırlık torklarıyla karşılaştır.'],
 bilgi=[B_TORK,B_DUZGUN],
 ad=[A('Dönme noktasını seç','K ucuna göre tork alınırsa K ipinin torku sıfır olur.','Στ(K) = 0'),A('Kolları belirle','Cisim K’dan 2, çubuğun ağırlığı 3, L ipi 6 bölme uzaktadır.','d = 2, 3, 6'),A('Tork eşitliği yaz','L ipinin torku, ağırlıkların torkuna eşittir.','T_L × 6 = 60 × 2 + 30 × 3 = 210'),A('Gerilmeyi bul','Eşitliği çöz.','T_L = 35 N')],
 puf='İp gerilmesini bulmak için diğer ipin bağlandığı noktadan tork al; böylece bilinmeyen sayısı azalır.',sekil=sk)

# ================= 05 · orta · menteşe, eğik ip =================
U=.65; L=6; ty=.75
wy=L*U*ty
sk=fig(wall(0,-.6,wy+.5),bar(L,U),hinge(0,0),wt(4*U,'$18$ N',1.0),
       f'\\draw[thick] ({L*U:.3f},0) -- (0,{wy:.3f});',
       f'\\draw ({L*U-1.1:.3f},0) arc[start angle=180,end angle=143.13,radius=1.1]; \\node at ({L*U-1.55:.3f},.45) {{$37^\\circ$}};',
       lab(L*U*.45,wy*.55+.1,'ip','above'))
Wr,Wk=36,18; Tt=Fr(Wr*3+Wk*4,6)/Fr(3,5); assert Tt==50
assert Fr(Wk*4,6)/Fr(3,5)==20 and Fr(Wr*3+Wk*4,6)==30 and Fr(180,4)==45 and Fr(180)/(Fr(4,5)*6)==Fr(75,2)
q('0005',tipId='tork-mentese',tip='Menteşeli çubukta gerilme ve tepki',z='orta',alt=ALT,kaz='Eğik ipin çubuğa dik bileşeniyle tork dengesi yazarak ip gerilmesini bulur.',
 kart='K-AFTORK-03 (menteşe, eğik ip) · çubuk 36 N, cisim 18 N, 37°',kalip='şekilli',
 metin='Ağırlığı 36 N olan 6 bölmeli düzgün ve türdeş çubuk, bir ucundan duvara menteşelenmiş, diğer ucundan duvara bağlı bir iple şekildeki gibi yatay olarak dengelenmiştir. Çubuğa menteşeden 4 bölme uzaktaki noktadan 18 N ağırlığında bir cisim asılmıştır.\n(sin37° = 0,6; cos37° = 0,8)\nBuna göre, ipteki gerilme kuvvetinin büyüklüğü kaç N’dur?',
 dogru=50,yan=[(20,'Çubuğun ağırlığını hesaba katmamış: 18 · 4 = T · 0,6 · 6 → T = 20 N.','dikkat'),(30,'İpi çubuğa dik sanmış, sin37° çarpanını kullanmamış: T · 6 = 36 · 3 + 18 · 4 → T = 30 N.','bilgi'),(Fr(75,2),'Tork denkleminde sin37° yerine cos37° kullanmış: T · 0,8 · 6 = 180 → T = 37,5 N.','islem'),(45,'İpi çubuğa dik sanıp kolunu 4 bölme almış: T · 4 = 180 → T = 45 N.','islem')],
 istenen='İpteki gerilme kuvvetinin büyüklüğü (N).',ip=['Menteşeye göre tork al; ipin çubukla yaptığı açıyı tork hesabında nasıl kullanacağını düşün.'],
 bilgi=[B_TORK,B('Kuvvetin bileşenleri','çubuğa θ açısıyla etki eden T kuvvetinin çubuğa dik bileşeni T·sinθ’dır ve tork yalnız bu bileşenden oluşur. Örnek: 10 N’luk kuvvet 37° açıyla uygulanırsa dik bileşeni 6 N’dur')],
 ad=[A('Dönme noktasını seç','Menteşeye göre tork al; menteşe tepkisinin torku sıfırdır.','Στ(O) = 0'),A('Ağırlık torkları','Çubuğun ağırlığı 3. bölmede, cisim 4. bölmededir.','36 × 3 + 18 × 4 = 180'),A('İpin torku','İpin çubuğa dik bileşeni T·sin37°, kolu 6 bölmedir.','T × 0,6 × 6 = 3,6 T'),A('Çöz','Torkları eşitle.','3,6 T = 180 → T = 50 N')],
 puf='Eğik ipin tork yapan kısmı, çubuğa dik bileşenidir; açı çubukla ip arasında ölçülüyorsa bileşen sin ile bulunur.',sekil=sk)

# ================= 06 · orta · menteşe tepkisi =================
U=.9; L=4
sk=fig(wall(0,-1.6,1.9),ceil(-.1,L*U+.5,1.7),bar(L,U),hinge(0,0),rope(L*U,.1,1.7),wt(3*U,'$20$ N',1.0))
Wr,Wk=40,20; T6=Fr(Wr*2+Wk*3,4); N6=Wr+Wk-T6; assert T6==35 and N6==25
assert Fr(Wr*4+Wk*3,4)==55 and Wr+Wk-55==5
q('0006',tipId='tork-mentese',tip='Menteşeli çubukta gerilme ve tepki',z='orta',alt=ALT,kaz='Menteşeli çubukta ip gerilmesini tork dengesiyle, menteşe tepkisini kuvvet dengesiyle bulur.',
 kart='K-AFTORK-03 (menteşe tepkisi) · çubuk 40 N, cisim 20 N',kalip='şekilli',
 metin='Ağırlığı 40 N olan 4 bölmeli düzgün ve türdeş çubuk, bir ucundan duvara menteşelenmiş, diğer ucundan düşey bir iple tavana bağlanarak yatay dengelenmiştir. Çubuğa menteşeden 3 bölme uzaktaki noktadan 20 N ağırlığında bir cisim asılmıştır.\nBuna göre, menteşenin çubuğa uyguladığı tepki kuvvetinin büyüklüğü kaç N’dur?',
 dogru=25,yan=[(5,'Çubuğun ağırlığını ucunda almış: T = (40 · 4 + 20 · 3) ÷ 4 = 55 N; tepki = 60 − 55 = 5 N.','islem'),(35,'İpteki gerilmeyi (35 N) menteşe tepkisi sanmış.','dikkat'),(40,'Tepkiyi çubuğun ağırlığına eşit almış.','bilgi'),(60,'Tepkiyi toplam ağırlığa (40 + 20) eşit almış; ip de yukarı kuvvet uygular.','bilgi')],
 istenen='Menteşenin çubuğa uyguladığı tepki kuvveti (N).',ip=['Önce menteşeye göre tork dengesiyle ipin gerilmesini, sonra düşey kuvvet dengesini kullan.'],
 bilgi=[B_TORK,B_DUZGUN],
 ad=[A('İp gerilmesini bul','Menteşeye göre tork al.','T × 4 = 40 × 2 + 20 × 3 = 140'),A('Gerilme sonucu','Eşitliği çöz.','T = 35 N'),A('Düşey dengeyi yaz','Yukarı kuvvetler (T ve tepki), aşağı kuvvetlerin toplamına eşit.','T + N = 40 + 20'),A('Tepkiyi bul','Değerleri yerine koy.','N = 60 − 35 = 25 N')],
 puf='Menteşe tepkisini, önce ipi bulup sonra düşey kuvvet dengesinden bul.',sekil=sk)

# ================= 07 · orta · öncüllü, cisim kaydırılıyor =================
U=.75; L=6
sk=fig(ceil(-.1,L*U+.4,1.5),tri(0,h=.8,lab=None,w=.45),bar(L,U),rope(L*U,.1,1.5),wt(2*U,'$P$',1.1),
       f'\\draw[vurgu,very thick,{ARR}] ({2*U-.2:.3f},-2.15) -- ({4*U:.3f},-2.15); \\node[below] at ({3*U:.3f},-2.15) {{kaydırma yönü}};',
       f'\\node[above] at (0,.1) {{K}}; \\node[above right] at ({L*U:.3f},1.1) {{L}};')
tr={'I':False,'II':True,'III':False}
rs={'I':'Cisim ipe yaklaşınca ipin kolu değil, cismin ipe olan uzaklığı azalır; K’ya göre T · d_ip = P · d eşitliğinde d artar; böylece T artar.','II':'Cisim K’dan uzaklaştığı için ipteki gerilme artar; kuvvet dengesinde N = P − T olduğundan K desteğinin tepkisi azalır.','III':'Çubuk her konumda dengededir; net tork her noktaya göre sıfırdır, artmaz.'}
rs['I']='Cisim K’dan uzaklaştıkça P’nin K’ya göre torku (P·d) artar; bunu dengeleyen ipin gerilmesi de artar, azalmaz.'
S5g=['Yalnız II','Yalnız III','I ve II','I ve III','II ve III']
d,y,ad=onc(tr,rs,S5g)
q('0007',tipId='tork-kavram',tip='Denge durumunda niceliklerin değişimi',z='orta',alt=ALT,kaz='Cismin konumu değişince ip gerilmesi, destek tepkisi ve net torkun değişimini yorumlar.',
 kart='K-AFTORK-05 (konum değişimi) · ağırlıksız çubuk, K desteği, L ipi',kalip='öncüllü',
 metin='Ağırlığı önemsiz bir çubuk, K ucundaki destek ve L ucuna bağlı düşey ip ile şekildeki gibi yatay dengededir. Çubuğa asılı P ağırlıklı cisim, çubuk yatay kalacak biçimde yavaşça ok yönünde kaydırılıyor.\nBuna göre cisim kaydırılırken;\nI. İpteki gerilme kuvveti azalır.\nII. Desteğin çubuğa uyguladığı tepki kuvveti azalır.\nIII. Çubuğa etki eden net tork artar.\nyargılarından hangileri doğrudur?',
 dogru=d,yan=y,sira=S5g,istenen='Doğru olan yargılar.',ip=['K ucuna göre tork dengesini yaz: cismin K’ya uzaklığı arttıkça ipin torku nasıl değişmelidir?'],
 bilgi=[B_TORK,B_DENGE],ad=ad,puf='Kuvvet dengesi için “ip + destek = ağırlık” yazılır; ip arttıkça destek azalır.',sekil=sk)

# ================= 08 · orta · masa kenarı =================
U=.6; L=8; kenar=5
sk=fig(f'\\draw[thick,fill=gray!40] (-1.2,-.1) rectangle ({kenar*U:.3f},-.55); \\draw[thick] (-.8,-.55) -- (-.8,-1.7) ({kenar*U-.4:.3f},-.55) -- ({kenar*U-.4:.3f},-1.7);',
       floor(-1.5,kenar*U+.6,-1.7),bar(L,U),wt(L*U,'$W$',.9),
       f'\\draw[dashed] ({kenar*U:.3f},-.55) -- ({kenar*U:.3f},.9); \\node[above] at ({kenar*U:.3f},.9) {{masa kenarı}};')
Wl=60; kol_cm=kenar-L//2; kol_w=L-kenar; Wm=Fr(Wl*kol_cm,kol_w); assert Wm==20 and kol_cm==1 and kol_w==3
assert Fr(Wl*2,3)==40 and Fr(Wl*4,3)==80 and Fr(Wl*3,1)==180
q('0008',tipId='tork-destek',tip='İki desteğe oturan çubuk, tepkiler ve devrilme',z='orta',alt=ALT,kaz='Masa kenarından taşan levhanın devrilme sınırını tork dengesiyle bulur.',
 kart='K-AFTORK-04 (levha, masa kenarı) · 60 N levha, 8 bölme, kenar 5. bölmede',kalip='şekilli',
 metin='Ağırlığı 60 N olan 8 bölmeli düzgün ve türdeş bir levha, bir ucu masadan taşacak biçimde şekildeki gibi yatay masaya yerleştirilmiştir. Levhanın masadan taşan ucuna W ağırlıklı bir cisim asılıyor. W ağırlığı artırıldığında levha, masanın kenarı etrafında dönmeye başlayacaktır.\nBuna göre, levhanın devrilmeden dengede kalabilmesi için W en çok kaç N olabilir?',
 dogru=20,yan=[(40,'Levhanın ağırlık merkezinin kenara uzaklığını 2 bölme almış: W · 3 = 60 · 2 → W = 40 N.','dikkat'),(60,'Levhanın ağırlığı ile cismin ağırlığını eşitlemiş.','bilgi'),(80,'Ağırlık merkezinin kenara uzaklığını 4 bölme (levhanın yarısı) almış: W · 3 = 60 · 4 → W = 80 N.','dikkat'),(180,'Kolları ters yazmış: W · 1 = 60 · 3 → W = 180 N.','islem')],
 istenen='Cismin en büyük ağırlığı W (N).',ip=['Devrilme anında levha yalnız masanın kenarına dayanır; torkları o noktaya göre yaz ve levhanın ağırlık merkezini bul.'],
 bilgi=[B_TORK,B_DUZGUN],
 ad=[A('Dönme noktasını seç','Devrilme sınırında levha masanın kenarı etrafında döner.','Dönme noktası: masa kenarı'),A('Kolları bul','Ağırlık merkezi 4. bölmededir, kenar 5. bölmededir; cisim 8. bölmededir.','d_levha = 5 − 4 = 1, d_W = 8 − 5 = 3'),A('Tork eşitliği yaz','Levhanın masa üstündeki torku W’nin torkunu dengeler.','60 × 1 = W × 3'),A('Çöz','Eşitliği çöz.','W = 20 N')],
 puf='Devrilme sınırında tepki yalnız dayanma noktasındadır; torkları o noktaya göre yaz.',sekil=sk)

# ================= 09 · orta · düğüm =================
ang=radians(37)
sk=fig(wall(-2.6,-1.9,.6),ceil(-2.6,2.6,1.8),
       f'\\draw[thick] (0,0) -- (-2.6,0); \\draw[thick] (0,0) -- (2.4,1.8);',
       f'\\draw[dashed,thin] (0,0) -- (1.5,0); \\draw (1.1,0) arc[start angle=0,end angle=36.87,radius=1.1]; \\node at (1.45,.3) {{$37^\\circ$}};',
       f'\\fill (0,0) circle (.06);',wt(0,'$30$ N',1.0,w=1.0).replace('(0.000,-0.100)','(0.000,0.000)'),
       lab(-1.3,0,'A','above'),lab(1.35,1.0,'B','above left'))
PB=Fr(30)/Fr(3,5); TA=PB*Fr(4,5); assert PB==50 and TA==40
q('0009',tipId='tork-dugum',tip='Düğüm noktası ve ip gerilmeleri',z='orta',alt=ALT,kaz='Düğüm noktasında yatay ve düşey kuvvet dengesini yazarak ip gerilmelerini bulur.',
 kart='K-AFTORK-06 (düğüm) · 30 N, 37°',kalip='şekilli',
 metin='Hafif ve esnemeyen A ve B iplerinin düğüm noktasından 30 N ağırlığında bir cisim asılmıştır. A ipi yatay ve duvara bağlıdır, B ipi yatayla 37° açı yaparak tavana bağlıdır. Sistem şekildeki gibi dengededir.\n(sin37° = 0,6; cos37° = 0,8)\nBuna göre, A ipindeki gerilme kuvvetinin büyüklüğü kaç N’dur?',
 dogru=40,yan=[(18,'A ipini ağırlığın sin37° ile çarpımı sanmış: 30 · 0,6 = 18 N.','islem'),(24,'A ipini ağırlığın cos37° ile çarpımı sanmış: 30 · 0,8 = 24 N.','islem'),(30,'A ipindeki gerilmeyi cismin ağırlığına eşit almış.','bilgi'),(50,'B ipinin gerilmesini (50 N) bulup A ipi için de aynı değeri vermiş.','dikkat')],
 istenen='A ipindeki gerilme kuvveti (N).',ip=['Düğüme etki eden üç kuvveti yatay ve düşey bileşenlerine ayırıp her doğrultuda bileşkeyi sıfır yaz.'],
 bilgi=[B_DENGE,B('Bileşenlere ayırma','yatayla θ açısı yapan T kuvvetinin düşey bileşeni T·sinθ, yatay bileşeni T·cosθ’dır. Örnek: 10 N’luk kuvvet 37° açıyla düşeyde 6 N, yatayda 8 N verir')],
 ad=[A('Düşey denge','B ipinin düşey bileşeni ağırlığı taşır.','T_B · sin37° = 30 → T_B = 50 N'),A('Yatay denge','B ipinin yatay bileşeni A ipinin gerilmesini dengeler.','T_A = T_B · cos37°'),A('Sonucu bul','Değerleri yerine koy.','T_A = 50 × 0,8 = 40 N')],
 puf='Düğüm dengesinde önce düşey doğrultuda eğik ipi, sonra yatayda diğer ipi bul.',sekil=sk)

# ================= 10 · orta · mil, çok kuvvet =================
U=.6; L=8
sk=fig(tri(3*U,h=.7,lab='P',w=.4),bar(L,U),
       f'\\draw[vurgu,very thick,{ARR}] (0,1.3) -- (0,.1); \\node[above] at (0,1.3) {{$30$ N}};',
       f'\\draw[vurgu,very thick,{ARR}] ({7*U:.3f},1.3) -- ({7*U:.3f},.1); \\node[above] at ({7*U:.3f},1.3) {{$30$ N}};',
       f'\\draw[vurgu,very thick,{ARR}] ({6*U:.3f},-1.3) -- ({6*U:.3f},-.1); \\node[below] at ({6*U:.3f},-1.3) {{$F$}};')
F10=Fr(30*4-30*3,3); N10=60-F10; assert F10==10 and N10==50
assert Fr(30*4,3)==40 and 60-40==20 and 60+10==70 and F10!=30
q('0010',tipId='tork-kaldirac',tip='Kaldıraç dengesi ve destek tepkisi',z='orta',alt=ALT,kaz='Birden çok kuvvet etkisindeki çubukta dönme noktasına göre tork dengesinden bilinmeyen kuvveti ve tepkiyi bulur.',
 kart='K-AFTORK-01 (çok kuvvet) · 30 N, 30 N, F',kalip='şekilli',
 metin='Ağırlığı önemsiz, eşit bölmeli bir çubuk, P noktasından geçen sürtünmesiz bir mil etrafında dönebilmektedir. Çubuğa, çubuğa dik doğrultuda şekildeki gibi iki ucuna yakın noktalardan 30 N’luk iki kuvvet ve F kuvveti uygulandığında çubuk yatay dengede kalmaktadır.\nBuna göre, milin çubuğa uyguladığı tepki kuvvetinin büyüklüğü kaç N’dur?',
 dogru=50,yan=[(20,'F’yi bulurken soldaki 30 N’un torkunu unutmuş (F = 120 ÷ 3 = 40 N) ve tepkiyi 60 − 40 = 20 N bulmuş.','dikkat'),(30,'Soldaki 30 N’un torkunu atlayıp F’nin kolunu 4 bölme almış: F = 120 ÷ 4 = 30 N; tepki = 60 − 30 = 30 N.','islem'),(60,'F kuvvetini hesaba katmadan yalnız iki 30 N’un toplamını tepki sanmış.','dikkat'),(70,'F kuvvetini de aşağı yönlü sanmış: 30 + 30 + 10 = 70 N.','bilgi')],
 istenen='Milin çubuğa uyguladığı tepki kuvveti (N).',ip=['P noktası dönme noktası olduğundan milin torku sıfırdır; önce F kuvvetini tork dengesinden bul, sonra yönlerine dikkat ederek kuvvetleri topla.'],
 bilgi=[B_TORK,B_DENGE],
 ad=[A('Torkları yaz','Soldaki 30 N ve F saat yönünün tersine, sağdaki 30 N saat yönünde döndürür (P’ye uzaklıklar 3, 3 ve 4 bölme).','30 × 3 + F × 3 = 30 × 4'),A('F’yi bul','Eşitliği çöz.','F = 10 N'),A('Kuvvet dengesi yaz','Aşağı kuvvetler = yukarı kuvvetler.','N + F = 30 + 30'),A('Tepkiyi bul','Değeri yerine koy.','N = 60 − 10 = 50 N')],
 puf='Birden çok kuvvet varsa dönme noktasına göre torkları yön yön yaz; tepkiyi kuvvet dengesinden bul.',sekil=sk)

# ================= 11 · orta · öncüllü, tahterevalli =================
U=.6; L=8
sk=fig(tri(3*U,h=.8,w=.5),bar(L,U),wt(0,'$30$ N',1.0),wt(L*U,'$Y$',1.0))
Wb=40; Yv=Fr(30*3-Wb*1,5); assert Yv==10 and 30+Wb+Yv==80
sol_ccw=30*3; sag_cw=Wb*1; assert sol_ccw>sag_cw
tr={'I':True,'II':False,'III':False}
rs={'I':'Destek noktasına göre: 30 · 3 = 40 · 1 + Y · 5 → Y = 10 N.','II':'Tepki, 30 + 40 + 10 = 80 N’dur; 70 N değildir.','III':'Y kaldırılırsa soldaki 30 N’un torku (90) çubuğun ağırlığının torkundan (40) büyük kalır; dönme sol ucu aşağı doğrudur, sağ uç aşağı inmez.'}
rs['II']='Destek tepkisi 30 + 40 + 10 = 80 N’dur; 70 N değildir.'
S5b=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III']
d,y,ad=onc(tr,rs,S5b)
q('0011',tipId='tork-kaldirac',tip='Kaldıraç dengesi ve destek tepkisi',z='orta',alt=ALT,kaz='Ağırlıklı çubukta tork dengesiyle bilinmeyen ağırlığı, destek tepkisini ve dönme eğilimini yorumlar.',
 kart='K-AFTORK-01 (ağırlıklı tahta) · 40 N tahta, 30 N ve Y',kalip='öncüllü',
 metin='Ağırlığı 40 N olan 8 bölmeli düzgün ve türdeş bir tahta, şekildeki gibi bir destek üzerinde yatay dengededir. Tahtanın sol ucuna 30 N, sağ ucuna Y ağırlığında birer cisim asılmıştır.\nBuna göre;\nI. Y ağırlığı 10 N’dur.\nII. Desteğin tahtaya uyguladığı tepki kuvveti 70 N’dur.\nIII. Y cismi kaldırılırsa tahtanın sağ ucu aşağı doğru döner.\nyargılarından hangileri doğrudur?',
 dogru=d,yan=y,sira=S5b,istenen='Doğru olan yargılar.',ip=['Destek noktasına göre torkları yazıp Y’yi bul; sonra her yargıyı bu değerle sına.'],
 bilgi=[B_TORK,B_DUZGUN],ad=ad,puf='Ağırlıklı tahtada tahtanın ağırlığını orta noktasından tek kuvvet olarak al ve destekten uzaklığıyla çarp.',sekil=sk)

# ================= 12 · orta · öncüllü, iki destek =================
U=.6; L=8
sk=fig(tri(1*U,h=.8,lab='K',w=.4),tri(7*U,h=.8,lab='L',w=.4),bar(L,U),
       f'\\node[draw,thick,fill=gray!35,minimum width=.9cm,minimum height=.55cm,anchor=south,inner sep=1.5pt] at ({2*U:.3f},.1) {{$30$ N}};')
NK=Fr(60*3+30*5,6); NL=90-NK; assert NK==55 and NL==35
tr={'I':True,'II':False,'III':False}
rs={'I':'L desteğine göre: N_K · 6 = 60 · 3 + 30 · 5 = 330 → N_K = 55 N.','II':'K desteğine göre: N_L · 6 = 60 · 3 + 30 · 1 = 210 → N_L = 35 N; 45 N değildir.','III':'Tepkilerin toplamı 55 + 35 = 90 N’dur (toplam ağırlık); 80 N değildir.'}
tr['III']=True; rs['III']='Tepkilerin toplamı toplam ağırlığa eşittir: 55 + 35 = 90 N.'
tr['II']=False
S5c=['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III']
d,y,ad=onc(tr,rs,S5c)
q('0012',tipId='tork-destek',tip='İki desteğe oturan çubuk, tepkiler ve devrilme',z='orta',alt=ALT,kaz='İki desteğe oturan çubukta destek tepkilerini tork ve kuvvet dengesiyle bulur.',
 kart='K-AFTORK-04 (iki destek) · çubuk 60 N, cisim 30 N',kalip='öncüllü',
 metin='Ağırlığı 60 N olan 8 bölmeli düzgün ve türdeş bir çubuk, şekildeki gibi K ve L destekleri üzerinde yatay dengededir. Çubuğun sol ucundan 2 bölme uzaktaki noktaya 30 N ağırlığında bir cisim yerleştirilmiştir. Desteklerin çubuğa uyguladığı tepki kuvvetleri N_K ve N_L’dir.\nBuna göre;\nI. N_K = 55 N’dur.\nII. N_L = 45 N’dur.\nIII. N_K + N_L = 90 N’dur.\nyargılarından hangileri doğrudur?',
 dogru=d,yan=y,sira=S5c,istenen='Doğru olan yargılar.',ip=['Bir desteği dönme noktası seçip diğer desteğin tepkisini bul; tepkilerin toplamını toplam ağırlıkla karşılaştır.'],
 bilgi=[B_TORK,B_DENGE],ad=ad,puf='İki destekli çubukta bir desteğe göre tork alıp diğer tepkiyi bul, kalanını kuvvet dengesinden çıkar.',sekil=sk)

# ================= 13 · orta · öncüllü, ip bağlantı noktası =================
U=.65; L=6; y1=L*U*.75; y2=L*U
sk=fig(wall(0,-.6,y2+.4),bar(L,U),hinge(0,0),wt(L*U,'$P$',1.0),
       f'\\draw[thick] ({L*U:.3f},0) -- (0,{y1:.3f}); \\draw[dashed,thick] ({L*U:.3f},0) -- (0,{y2:.3f});',
       f'\\fill (0,{y1:.3f}) circle (.06); \\fill (0,{y2:.3f}) circle (.06);',
       f'\\node[above right] at (.05,{y1:.3f}) {{K}}; \\node[above right] at (.05,{y2:.3f}) {{L}};')
from math import atan2,tan
th1=atan2(.75,1); th2=atan2(1,1)
tr={'I':False,'II':True,'III':True}
rs={'I':'T · sinθ = P olduğundan θ büyüyünce T azalır; artmaz (θ, ip ile çubuk arasındaki açıdır).','II':'Menteşe tepkisinin yatay bileşeni T · cosθ = P · cotθ’dır; θ büyüdükçe azalır.','III':'İpin menteşeye göre torku, cismin torkuna (P · çubuk boyu) eşit kalmalıdır; değişmez.'}
assert Fr(1)/tan(th2)<Fr(1)/tan(th1) if False else (1/tan(th2)<1/tan(th1)) and (1/sin(th2)<1/sin(th1))
S5d=['Yalnız I','Yalnız II','I ve II','II ve III','I, II ve III']
d,y,ad=onc(tr,rs,S5d)
q('0013',tipId='tork-mentese',tip='Menteşeli çubukta gerilme ve tepki',z='orta',alt=ALT,kaz='İpin bağlantı noktası değişince ip gerilmesi, menteşe tepkisi ve tork değişimini yorumlar.',
 kart='K-AFTORK-03 (açı değişimi) · ağırlıksız çubuk, menteşe, ip K → L',kalip='öncüllü',
 metin='Ağırlığı önemsiz bir çubuk, bir ucundan duvara menteşelenmiş, diğer ucundan duvardaki K noktasına bağlı bir iple şekildeki gibi yatay dengelenmiştir. Çubuğun ucuna P ağırlıklı cisim asılıdır. İpin duvardaki ucu K noktasından L noktasına çıkarılıyor; çubuk yine yatay dengededir.\nBuna göre, bu değişiklik sonunda;\nI. İpteki gerilme kuvveti artar.\nII. Menteşenin çubuğa uyguladığı tepkinin yatay bileşeni azalır.\nIII. İpin çubuğa menteşeye göre uyguladığı torkun büyüklüğü değişmez.\nyargılarından hangileri doğrudur?',
 dogru=d,yan=y,sira=S5d,istenen='Doğru olan yargılar.',ip=['İpin menteşeye göre torkunu cismin torkuyla eşitle; ipin çubukla yaptığı açı değişince bileşenlerin nasıl değiştiğine bak.'],
 bilgi=[B_TORK,B('Bileşenlere ayırma','ip çubukla θ açısı yapıyorsa T·sinθ çubuğa dik, T·cosθ çubuk boyunca etkir. Örnek: θ = 90° iken ip çubuğa diktir ve tüm gerilme tork yapar')],ad=ad,puf='İpin açısı büyüyünce aynı torku üretmek için gereken gerilme azalır; tork ise cismin torkuna eşit kaldığından değişmez.',sekil=sk)

# ================= 14 · orta · öncüllü, mobil çubuğu =================
U=.7; L=6
sk=fig(ceil(-.3,L*U+.3,1.6),rope(2*U,.1,1.6),bar(L,U),wt(0,'$X$',1.1),wt(3*U,'$20$ N',1.1),wt(L*U,'$10$ N',1.1))
Xw=Fr(20*1+10*4,2); Tk=Xw+20+10; assert Xw==30 and Tk==60 and 20*1*2==10*4
tr={'I':True,'II':False,'III':True}
rs={'I':'İpin bağlandığı noktaya göre: X · 2 = 20 · 1 + 10 · 4 → X = 30 N.','II':'İpteki gerilme toplam ağırlığa eşittir: 30 + 20 + 10 = 60 N; 50 N değildir.','III':'20 N’luk cismin torku 20 · 1 = 20, 10 N’luk cismin torku 10 · 4 = 40’tır; 20 N’luk cismin torku diğerinin yarısıdır.'}
S5e=['Yalnız I','I ve II','I ve III','II ve III','I, II ve III']
d,y,ad=onc(tr,rs,S5e)
q('0014',tipId='tork-kavram',tip='Denge durumunda niceliklerin değişimi',z='orta',alt=ALT,kaz='Birden çok cisim asılı ağırlıksız çubukta ağırlıkları, ip gerilmesini ve torkları yorumlar.',
 kart='K-AFTORK-05 (çok cisim) · X, 20 N, 10 N; kollar 2, 1, 4',kalip='öncüllü',
 metin='Ağırlığı önemsiz, 6 bölmeli bir çubuk, soldan 2. bölmeye bağlı düşey bir iple tavandan asılarak şekildeki gibi yatay dengelenmiştir. Çubuğa X, 20 N ve 10 N ağırlığında üç cisim asılmıştır.\nBuna göre;\nI. X cisminin ağırlığı 30 N’dur.\nII. İpteki gerilme kuvveti 50 N’dur.\nIII. 20 N’luk cismin ipin bağlandığı noktaya göre torku, 10 N’luk cismin torkunun yarısına eşittir.\nyargılarından hangileri doğrudur?',
 dogru=d,yan=y,sira=S5e,istenen='Doğru olan yargılar.',ip=['İpin bağlandığı noktayı dönme noktası seç; her cismin kolunu bölme sayarak bulup torkları karşılaştır.'],
 bilgi=[B_TORK,B_DENGE],ad=ad,puf='İp gerilmesi, ipe asılı bütün ağırlıkların toplamına eşittir.',sekil=sk)

# ================= 15 · zor · merdiven =================
Wl,Wp=60,30; H,Bs=3,4; fr=Fr(3,5); hx=Bs*fr
Nw=Fr(Wl*Fr(Bs,2)+Wp*hx,H); assert Nw==64 and hx==Fr(12,5)
assert Fr(Wl*2,3)==40 and Fr(192,4)==48 and Fr(Wl*2+Wp*Fr(8,5),3)==56 and Fr(Wl*2+Wp*2,3)==60
px,py=4-float(hx),float(fr*H)
sk=fig(wall(0,0,3.6),floor(-.4,5.0,0),
       '\\draw[ultra thick] (4,0) -- (0,3);',
       f'\\draw[vurgu,very thick,{ARR}] (2,1.5) -- (2,.5); \\node[below] at (2,.5) {{$60$ N}};',
       f'\\draw[vurgu,very thick,{ARR}] ({px:.3f},{py:.3f}) -- ({px:.3f},{py-.9:.3f}); \\node[left] at ({px:.3f},{py-.5:.3f}) {{$30$ N}};',
       f'\\node[draw,circle,fill=white,inner sep=1pt] at ({px:.3f},{py+.0:.3f}) {{}};',
       '\\draw[<->,thin] (-.55,0) -- (-.55,3); \\node[left] at (-.55,1.5) {$3$ m}; \\draw[<->,thin] (0,-.6) -- (4,-.6); \\node[below] at (2,-.6) {$4$ m};')
q('0015',tipId='tork-merdiven',tip='Duvara dayalı merdiven',z='zor',alt=ALT,kaz='Merdivenin dengesinde zemine göre tork dengesi ve yatay kuvvet dengesini birlikte kullanır.',
 kart='K-AFTORK-07 (merdiven) · 60 N merdiven, 30 N kişi, 3 m – 4 m',kalip='şekilli',
 metin='Ağırlığı 60 N olan düzgün ve türdeş bir merdiven, şekildeki gibi sürtünmesiz düşey bir duvara dayanmış hâlde, sürtünmeli yatay zeminde kaymadan dengededir. Ağırlığı 30 N olan bir kişi, merdivenin alt ucundan boyunun 3/5’i kadar yukarıdaki noktada durmaktadır.\nBuna göre, zeminin merdivene uyguladığı sürtünme kuvvetinin büyüklüğü kaç N’dur?',
 dogru=64,yan=[(40,'Kişinin ağırlığını hesaba katmamış: 60 · 2 ÷ 3 = 40 N.','dikkat'),(48,'Duvar tepkisinin kolunu 4 m almış: 192 ÷ 4 = 48 N.','islem'),(56,'Kişinin kolunu duvardan 1,6 m almış: (60 · 2 + 30 · 1,6) ÷ 3 = 56 N.','dikkat'),(60,'Kişiyi merdivenin orta noktasında sanmış: (60 · 2 + 30 · 2) ÷ 3 = 60 N.','dikkat')],
 istenen='Zeminin merdivene uyguladığı sürtünme kuvveti (N).',ip=['Zemin ile merdivenin temas noktasını dönme noktası al ve yatay kolları bul; duvar sürtünmesiz olduğundan duvar tepkisi yataydır.'],
 bilgi=[B_TORK,B_DUZGUN],
 ad=[A('Yatay kolları bul','Alt uçtan yatay uzaklıklar: merdivenin ağırlık merkezi 4 ÷ 2 = 2 m; kişi 4 · 3/5 = 2,4 m; duvar tepkisinin kolu 3 m’dir.','d₁ = 2, d₂ = 2,4, d₃ = 3'),A('Zemine göre tork yaz','Duvar tepkisinin torku, ağırlıkların torkuna eşittir.','N_duvar × 3 = 60 × 2 + 30 × 2,4 = 192'),A('Duvar tepkisini bul','Eşitliği çöz.','N_duvar = 64 N'),A('Yatay dengeyi yaz','Yatayda yalnız duvar tepkisi ve zemin sürtünmesi vardır.','f = N_duvar'),A('Sürtünmeyi bul','Sonucu yaz.','f = 64 N')],
 puf='Merdivende tork alırken kollar yatay uzaklıklardır; zemin temas noktası seçilirse zemin kuvvetleri tork yapmaz.',sekil=sk)

# ================= 16 · zor · eğik çubuk, yatay bileşen =================
U=.7; L=5; c,s=.8,.6
ex,ey=L*U*c,L*U*s
rx,ry=4*U*c,4*U*s; tt=rx/s; wx,wy=0.0,ry+c*tt
sk=fig(wall(0,-.5,wy+.4),
       f'\\begin{{scope}}[rotate=36.87]{bar(L,U)}\\end{{scope}}',hinge(0,0),
       f'\\draw[thick] ({rx:.3f},{ry:.3f}) -- (0,{wy:.3f});',
       f'\\draw ({rx+.25*(-s):.3f},{ry+.25*c:.3f}) -- ({rx+.25*(-s)+.25*c:.3f},{ry+.25*c+.25*s:.3f}) -- ({rx+.25*c:.3f},{ry+.25*s:.3f});',
       f'\\node[draw,thick,fill=gray!35,minimum width=.9cm,minimum height=.55cm,inner sep=1.5pt] (w) at ({ex:.3f},{ey-1.25:.3f}) {{$20$ N}}; \\draw[thick] ({ex:.3f},{ey:.3f}) -- (w.north);',
       f'\\draw (.9,0) arc[start angle=0,end angle=36.87,radius=.9]; \\node at (1.25,.25) {{$37^\\circ$}};',
       lab(rx*.45,(ry+wy)/2+.1,'ip','left'))
Wr,Wk=40,20; T16=Fr(Wr*Fr(5,2)*Fr(4,5)+Wk*5*Fr(4,5),4); H16=T16*Fr(3,5); V16=Wr+Wk-T16*Fr(4,5)
assert T16==40 and H16==24 and V16==28 and T16*Fr(4,5)==32
q('0016',tipId='tork-mentese',tip='Menteşeli çubukta gerilme ve tepki',z='zor',alt=ALT,kaz='Eğik çubukta ipin çubuğa dik olduğu durumda tork dengesinden gerilmeyi, kuvvet dengesinden menteşe tepkisinin bileşenini bulur.',
 kart='K-AFTORK-03 (eğik çubuk) · 40 N çubuk, 20 N cisim, 37°',kalip='şekilli',
 metin='Ağırlığı 40 N olan 5 bölmeli düzgün ve türdeş bir çubuk, alt ucundan duvara menteşelenmiş ve yatayla 37° açı yapacak biçimde şekildeki gibi dengelenmiştir. Çubuğun serbest ucuna 20 N ağırlığında bir cisim asılmıştır. Çubuğa menteşeden 4 bölme uzaktaki noktaya çubuğa dik doğrultuda bağlı bir ip, çubuğu duvara bağlamaktadır.\n(sin37° = 0,6; cos37° = 0,8)\nBuna göre, menteşenin çubuğa uyguladığı tepki kuvvetinin yatay bileşeni kaç N’dur?',
 dogru=24,yan=[(28,'Tepkinin düşey bileşenini (60 − 32 = 28 N) yatay bileşen sanmış.','dikkat'),(32,'İp gerilmesinin düşey bileşenini (40 · 0,8 = 32 N) yatay bileşen sanmış; ip çubuğa dik olduğundan yatay bileşeni T · sin37°’dir.','islem'),(40,'İpin gerilmesini (40 N) menteşe tepkisinin yatay bileşeni sanmış.','dikkat'),(60,'Toplam ağırlığı (40 + 20) yatay bileşen sanmış.','bilgi')],
 istenen='Menteşe tepkisinin yatay bileşeni (N).',ip=['Menteşeye göre tork alırken yatay uzaklıkları değil, çubuğa dik kolları kullan; ipin çubuğa dik olduğunu değerlendir.'],
 bilgi=[B_TORK,B('Dik ip','ip çubuğa dik ise ipin tamamı tork yapar ve gerilmenin yatay bileşeni T·sinθ (θ çubuğun yatayla açısı), düşey bileşeni T·cosθ’dır. Örnek: T = 10 N ve θ = 37° için yatay 6 N, düşey 8 N')],
 ad=[A('Ağırlıkların torkları','Çubuk ve cisim ağırlıkları çubuğa dik bileşenleriyle (G·cos37°) tork yapar; çubuğun ağırlığı 2,5, cisim 5 bölme uzaktadır.','40 × 2,5 × 0,8 + 20 × 5 × 0,8 = 160'),A('İpin torku','İp çubuğa diktir; kolu 4 bölmedir.','T × 4 = 160 → T = 40 N'),A('İpin bileşenleri','İp çubuğa dik olduğundan yatay bileşeni T·sin37°, düşey bileşeni T·cos37°’dır; ip duvara doğru çeker.','T_x = 40 × 0,6 = 24 N, T_y = 40 × 0,8 = 32 N'),A('Yatay dengeyi yaz','Yatayda yalnız ip ve menteşe tepkisi vardır.','H = T_x'),A('Sonucu bul','Değeri yerine koy.','H = 24 N')],
 puf='Çubuğa dik bağlı ip için torkta kuvvetin tamamı, kuvvet dengesinde ise bileşenleri kullanılır.',sekil=sk)

# ================= 17 · zor · mobil =================
U1=.8
sk=fig(ceil(-.6,4.2,3.7),
       rope(3*U1,.0+2.4+.1,3.7),
       bar(5,U1,0,2.4),
       f'\\draw[thick] (0,2.3) -- (0,.9+.1);',
       bar(4,U1,-U1,.9),
       f'\\node[draw,thick,fill=gray!35,minimum width=1.0cm,minimum height=.55cm,inner sep=1.5pt] (a) at ({-U1:.3f},-.55) {{$30$ N}}; \\draw[thick] ({-U1:.3f},.8) -- (a.north);',
       f'\\node[draw,thick,fill=gray!35,minimum width=.9cm,minimum height=.55cm,inner sep=1.5pt] (b) at ({-U1+4*U1:.3f},-.55) {{$B$}}; \\draw[thick] ({-U1+4*U1:.3f},.8) -- (b.north);',
       f'\\node[draw,thick,fill=gray!35,minimum width=.9cm,minimum height=.55cm,inner sep=1.5pt] (c) at ({5*U1:.3f},1.0) {{$C$}}; \\draw[thick] ({5*U1:.3f},2.3) -- (c.north);')
A_,Bv=30,Fr(30*1,3); tot=A_+Bv; Cv=Fr(tot*3,2); assert Bv==10 and tot==40 and Cv==60
assert Fr(A_*3,2)==45 and Fr(tot*3,5)==24 and A_==30
q('0017',tipId='tork-mobil',tip='İç içe çubuklardan oluşan mobil',z='zor',alt=ALT,kaz='İç içe iki çubuktan oluşan sistemde çubukları sırayla tork dengesiyle çözerek bilinmeyen ağırlığı bulur.',
 kart='K-AFTORK-09 (mobil) · 30 N, B, C; kollar 1:3 ve 3:2',kalip='şekilli',
 metin='Ağırlıkları önemsiz, eşit bölmeli iki çubuk ve ipler kullanılarak oluşturulan düzenek şekildeki gibi dengededir. Alttaki çubuğun ucuna 30 N ağırlığında A cismi, diğer ucuna B cismi asılmıştır. Alttaki çubuk, üstteki çubuğun sol ucundan asılmış, üstteki çubuğun sağ ucuna da C cismi asılmıştır. İplerin ağırlığı önemsizdir.\nBuna göre, C cisminin ağırlığı kaç N’dur?',
 dogru=60,yan=[(40,'C’nin ağırlığını alttaki sistemin toplam ağırlığına (40 N) eşit almış.','bilgi'),(24,'Üst çubukta C’nin kolunu 5 bölme (çubuğun tamamı) almış: C · 5 = 40 · 3 → C = 24 N.','islem'),(30,'C’yi A cisminin ağırlığına eşit almış.','bilgi'),(45,'Alt çubuğu atlayıp yalnız 30 N’luk cismi üst çubuğun ucunda sanmış: C · 2 = 30 · 3 → C = 45 N.','dikkat')],
 istenen='C cisminin ağırlığı (N).',ip=['Önce alttaki çubuğu kendi ipinin bağlandığı noktaya göre dengele; bu çubuk, üst çubuğa tek bir kuvvet olarak etki eder.'],
 bilgi=[B_TORK,B_DENGE],
 ad=[A('Alt çubuğu dengele','Alt çubuğun ipi, A’dan 1, B’den 3 bölme uzaktadır.','30 × 1 = B × 3 → B = 10 N'),A('Alt sistemin ağırlığını bul','Alt çubuğu taşıyan ip, A ve B’nin ağırlıkları toplamını çeker.','T_alt = 30 + 10 = 40 N'),A('Üst çubuğu dengele','Üst çubuğun ipi, alt iple 3 bölme, C ile 2 bölme uzaktadır.','40 × 3 = C × 2'),A('C’yi bul','Eşitliği çöz.','C = 60 N')],
 puf='Mobilde alttaki çubuk, ağırlıkları toplamına eşit tek bir kuvvet olarak üst çubuğa etki eder; çubukları aşağıdan yukarı sırayla çöz.',sekil=sk)

# ================= 18 · zor · düğüm + makara =================
sk=fig(ceil(-3.4,3.8,2.0),
       '\\draw[thick] (0,0) -- (-2.667,2.0); \\draw[thick] (0,0) -- (3.0,0);',
       '\\draw[thick] (3.0,-.25) -- (3.0,2.0); \\draw[thick,fill=white] (3.0,-.25) circle (.25); \\fill (3.0,-.25) circle (.05);',
       '\\draw[thick] (3.25,-.25) -- (3.25,-1.2); \\node[draw,thick,fill=gray!35,minimum width=1.0cm,minimum height=.55cm,inner sep=1.5pt] (m) at (3.25,-1.5) {$40$ N};',
       '\\fill (0,0) circle (.06); \\draw[dashed,thin] (0,0) -- (-1.6,0); \\draw (-1.1,0) arc[start angle=180,end angle=143.13,radius=1.1]; \\node at (-1.55,.3) {$37^\\circ$};',
       '\\draw[thick] (0,0) -- (0,-.95); \\node[draw,thick,fill=gray!35,minimum width=.9cm,minimum height=.55cm,inner sep=1.5pt] at (0,-1.2) {$P$};')
M18=40; T18=Fr(M18)/Fr(4,5); P18=T18*Fr(3,5); assert T18==50 and P18==30
assert M18*Fr(3,5)==24 and M18*Fr(4,5)==32
q('0018',tipId='tork-dugum',tip='Düğüm noktası ve ip gerilmeleri',z='orta',alt=ALT,kaz='Makaradan geçen ip ve eğik ip bulunan düğümde yatay ve düşey kuvvet dengesini birlikte kullanarak bilinmeyen ağırlığı bulur.',
 kart='K-AFTORK-06 (düğüm + makara) · 40 N, 37°',kalip='şekilli',
 metin='Hafif ve esnemeyen iplerle kurulan düzenekte sürtünmesiz makaradan geçen yatay ip, bir ucunda 40 N ağırlığında cisim taşımaktadır. İpin diğer ucu, düğüm noktasında yatayla 37° açı yapan başka bir ip ve P ağırlıklı cismi taşıyan ip ile birleşmiştir. Sistem şekildeki gibi dengededir.\n(sin37° = 0,6; cos37° = 0,8)\nBuna göre, P cisminin ağırlığı kaç N’dur?',
 dogru=30,yan=[(24,'Eğik ipin gerilmesini bulmadan P’yi 40 · sin37° = 24 N almış.','islem'),(32,'P’yi 40 · cos37° = 32 N almış; sin ve cos bileşenlerini karıştırmış.','islem'),(40,'P’yi makaradan geçen ipteki yükün ağırlığına eşit almış.','bilgi'),(50,'Eğik ipteki gerilmeyi (50 N) P’nin ağırlığı sanmış.','dikkat')],
 istenen='P cisminin ağırlığı (N).',ip=['Düğüme etki eden kuvvetleri yatay ve düşey bileşenlerine ayır.'],
 bilgi=[B_DENGE,B('İdeal makara','sürtünmesiz ve hafif makaradan geçen ipin gerilmesi her noktada aynıdır; yön değiştirir, büyüklüğü değiştirmez. Örnek: ucunda 20 N’luk cisim asılı ipte gerilme 20 N’dur')],
 ad=[A('Yatay ipin gerilmesi','Makaradan geçen ipte gerilme, asılı cismin ağırlığına eşittir.','T₁ = 40 N'),A('Yatay denge','Eğik ipin yatay bileşeni T₁’i dengeler.','T₂ · cos37° = 40 → T₂ = 50 N'),A('Düşey denge','Eğik ipin düşey bileşeni P’yi taşır.','P = T₂ · sin37°'),A('Sonucu bul','Değerleri yerine koy.','P = 50 × 0,6 = 30 N')],
 puf='Düğümde önce yatayda bilinen kuvvetle eğik ipin gerilmesini bul, sonra düşey bileşenden bilinmeyen ağırlığı çıkar.',sekil=sk)

# ================= 19 · zor · iki destek, devrilme sınırı =================
U=.6; L=8
sk=fig(tri(2*U,h=.8,lab='K',w=.4),tri(7*U,h=.8,lab='L',w=.4),bar(L,U),wt(0,'$W$',.55),
       f'\\node[draw,thick,fill=gray!35,minimum width=.9cm,minimum height=.55cm,anchor=south,inner sep=1.5pt] at ({3*U:.3f},.1) {{$30$ N}};')
Wl=60; Wmax=Fr(Wl*2+30*1,2); assert Wmax==Fr(75) and Fr(Wl*2,2)==60 and Fr(150,3)==50 and Fr(150,4)==Fr(75,2) and Fr(150,5)==30
assert (Wl*2+30-76*2)<0 and (Wl*2+30-74*2)>0
q('0019',tipId='tork-destek',tip='İki desteğe oturan çubuk, tepkiler ve devrilme',z='zor',alt=ALT,kaz='İki destekli çubukta, iki cisim etkisinde devrilme sınırını bir desteğin tepkisinin sıfır olduğu koşuldan bulur.',
 kart='K-AFTORK-04 (devrilme sınırı) · 60 N çubuk, 30 N cisim, W, K ve L destekleri',kalip='şekilli',
 metin='Ağırlığı 60 N olan 8 bölmeli düzgün ve türdeş bir çubuk, şekildeki gibi K ve L destekleri üzerinde yatay dengededir. Çubuğun sol ucundan W ağırlıklı bir cisim asılmış, sol ucundan 3 bölme uzaktaki noktaya da 30 N ağırlığında bir cisim yerleştirilmiştir. W artırılırken çubuk, L desteğinden ayrılıp K desteği etrafında dönmeye başlayabilir.\nBuna göre, çubuğun yatay dengesi bozulmadan W en çok kaç N olabilir?',
 dogru=75,yan=[(Fr(75,2),'W’nin kolunu 4 bölme almış: W · 4 = 60 · 2 + 30 · 1 → W = 37,5 N.','islem'),(30,'W’nin kolunu 5 bölme (L desteğine uzaklığı) almış: W · 5 = 150 → W = 30 N.','islem'),(50,'W’nin kolunu 3 bölme almış: W · 3 = 150 → W = 50 N.','islem'),(60,'30 N’luk cismin torkunu hesaba katmamış: W · 2 = 60 · 2 → W = 60 N.','dikkat')],
 istenen='Dengenin bozulmaması için W’nin en büyük değeri (N).',ip=['Dengenin bozulmak üzere olduğu sınır durumunu tanımla; torkları bu duruma uygun bir noktaya göre yaz.'],
 bilgi=[B_TORK,B_DUZGUN],
 ad=[A('Sınır koşulunu belirle','Çubuk L’den ayrılmak üzereyken yalnız K’ye dayanır; L’nin çubuğa uyguladığı tepki sıfırdır.','N_L = 0'),A('Kolları bul','K desteğine göre W’nin kolu 2 bölme (sol); 30 N’luk cismin kolu 1 bölme, çubuğun ağırlık merkezi 4. bölmede olduğundan kolu 2 bölmedir (sağ).','d_W = 2, d_30 = 1, d_G = 2'),A('Tork eşitliği yaz','W’nin torku, çubuğun ve 30 N’luk cismin torklarının toplamına eşittir.','W × 2 = 60 × 2 + 30 × 1 = 150'),A('Çöz','Eşitliği çöz.','W = 75 N')],
 puf='Devrilme sınırında uzaktaki desteğin tepkisi sıfırdır; torkları yakın desteğe göre yaz.',sekil=sk)

# ================= 20 · zor · grafik =================
gx=['\\begin{axis}[width=6.6cm,height=5.4cm,xmin=0,xmax=6,ymin=0,ymax=60,xtick distance=1,ytick={0,10,20,30,40,50,60},grid=both,major grid style={gray!55,thin},tick label style={font=\\small},axis lines=left,xlabel={$x$ (m)},ylabel={$T$ (N)},xlabel style={font=\\small},ylabel style={font=\\small}]',
    '\\addplot[thick,vurgu] coordinates {(0,0) (5,50)};','\\end{axis}']
sk=fig(*gx)
W20=60; sl=Fr(50,5); L20=W20/sl; x20=L20-2; T20=sl*x20; N20=W20-T20; assert sl==10 and L20==6 and x20==4 and T20==40 and N20==20
q('0020',tipId='tork-grafik',tip='Gerilme–konum grafiği',z='zor',alt=ALT,kaz='İp gerilmesi–konum grafiğinin eğiminden çubuğun boyunu çıkarıp menteşe tepkisini bulur.',
 kart='K-AFTORK-08 (T–x grafiği) · W = 60 N, eğim 10 N/m',kalip='grafik',
 metin='Boyu bilinmeyen, ağırlığı önemsiz bir çubuk, bir ucundan duvara menteşelenmiş, diğer ucundan düşey bir iple tavana bağlanarak yatay dengelenmiştir. Çubuğa, menteşeden x uzaklığındaki noktaya 60 N ağırlığında bir cisim asılıyor ve cismin konumu değiştirilerek ipteki gerilme kuvveti T ölçülüyor. T’nin x’e bağlı grafiği şekildeki gibidir.\nBuna göre, cisim ipin bağlandığı uçtan 2 m uzaktayken menteşenin çubuğa uyguladığı tepki kuvvetinin büyüklüğü kaç N’dur?',
 dogru=20,yan=[(10,'Grafiğin eğimini (10 N/m) tepki kuvveti sanmış.','bilgi'),(30,'Grafikten x = 3 m’deki gerilmeyi (30 N) tepki sanmış.','dikkat'),(40,'Cismin ipten 2 m uzakta olduğu konumda gerilmeyi (40 N) bulmuş, ancak tepkiyi ağırlıktan çıkarmamış.','dikkat'),(60,'Cismin ağırlığını (60 N) tepki sanmış; ip de ağırlığın bir kısmını taşır.','dikkat')],
 istenen='Menteşe tepkisi (N).',ip=['Eğimin hangi niceliklerin oranı olduğunu düşün; çubuğun boyunu nasıl bulabileceğini araştır.'],
 bilgi=[B_TORK,B_DENGE],
 ad=[A('Çubuğun boyunu bul','Menteşeye göre tork: T · L = W · x olduğundan T–x doğrusunun eğimi W ÷ L’dir.','10 = 60 ÷ L → L = 6 m'),A('Konumu belirle','Cisim ipin bağlandığı uçtan 2 m uzakta, menteşeden 6 − 2 kadar uzaktadır.','x = 4 m'),A('Gerilmeyi bul','Doğrusal ilişkiyi kullan.','T = 10 × 4 = 40 N'),A('Tepkiyi bul','Yukarı kuvvetler ağırlığa eşittir.','N = 60 − 40 = 20 N')],
 puf='T–x doğrusunun eğimi W ÷ L’dir; konum ve gerilme bulununca tepki, ağırlıkla gerilmenin farkıdır.',sekil=sk)

# ================= yaz =================
def bitir_af():
    for qq in P.ANA: qq['kardes']=None
    P.yaz(os.path.join(GD,'tork-1.json'),'/tmp/bos-tork.json')
    tipler={}
    for c in KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu='afiz|Tork Denge'))['kartlar'].append(c['id'])
    json.dump(dict(konu='Tork Denge',surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2018–2026 Fizik (yalnız mantık), MEB 11. sınıf fizik müfredatı.',kartlar=KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar','aftork.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler))
bitir_af()
