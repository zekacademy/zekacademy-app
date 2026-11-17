"""TYT Kimya · Maddenin Halleri · 3. ek paket (halleruc): 10 soru, kardeş yok, ipucu 1.
Şekil verileri Python'da hesaplanır; TikZ bu değerlerden üretilir. Öncüllerin doğru/yanlış değeri tek yerde (d sözlüğü) tanımlanır."""
import sys,os,math,random,itertools
from fractions import Fraction as Fr
GD=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,GD)
import _hafif_kim2 as H
from _hafif_kim2 import *
from _hafif_kim import onc as _onc_eski, tek
KONU_='Maddenin Halleri'; UK='kim|Maddenin Halleri'
H.KONU=KONU_
P=Parti('halleruc',KONU_,UK,ders='TYT Kimya',idon='tytkim')
KY='ÖSYM 2018–2026 TYT Kimya (yalnız mantık) · MEB 9. sınıf Maddenin Hâlleri'
MAP={}
for _n,_t in [(('01',),('hal','Hâl değişim sıcaklıkları')),(('10',),('isitma','Isıtma eğrisi ve hâl değişimi')),
              (('02','03','08'),('gaz','Gazların özellikleri ve basıncı')),(('04','09'),('sivi','Sıvıların özellikleri')),
              (('05','06','07'),('buhar','Buhar basıncı ve kaynama'))]:
    for _x in _n: MAP[_x]=_t
assert len(MAP)==10
def kartla(n,alt,fikir,tuzak,z,kalip,adim):
    a,b=MAP[n]; kart(f'K-KMHL3-{n}',alt,fikir,tuzak,z,kalip,adim,f'km-hl3-{a}',b,KY)
def q(no,ad,**k):
    assert len(k['ip'])==1
    k['tipId']='km-hl3-'+MAP[no[-2:]][0]; k['tip']=MAP[no[-2:]][1]
    ne=k.pop('ne'); k['kart']=f"K-KMHL3-{no[-2:]} ({MAP[no[-2:]][1].lower()}) · {ne}"
    mk(P,no,ad=ad,adim=len(ad),**k)
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
ARR='-{Stealth[length=1.9mm,width=1.7mm]}'
def tk(g): return tikz_svg(HEAD+g+TAIL)

# ---------- öncüllü yardımcıları ----------
def _anah(s): return (len(s),tuple(s))
def onc_t(d,hedef):
    etiket=sorted(d,key=lambda x:['I','II','III','IV'].index(x))
    T=frozenset(k for k,v in d.items() if v[0])
    ad=lambda s:tuple(sorted(s,key=lambda x:['I','II','III','IV'].index(x)))
    adaylar=[]
    for n in range(1,min(3,len(etiket))+1):
        for c in itertools.combinations(etiket,n): adaylar.append(c)
    adaylar=sorted(adaylar,key=_anah); kt=_anah(ad(T))
    alt=[c for c in adaylar if _anah(c)<kt]; ust=[c for c in adaylar if _anah(c)>kt]
    assert hedef<=len(alt) and 4-hedef<=len(ust),('hedef uygun degil',T,hedef,len(alt),len(ust))
    uz=lambda c:len(frozenset(c)^T)
    sa=sorted(alt,key=lambda c:(uz(c),-adaylar.index(c)))[:hedef]
    su=sorted(ust,key=lambda c:(uz(c),adaylar.index(c)))[:4-hedef]
    ops=sorted(sa+[ad(T)]+su,key=_anah)
    assert ops.index(ad(T))==hedef
    return _onc_eski(d,ops)
def tek_t(dogru,yanlislar,hedef,hedef_bool=True):
    S=[(m,not hedef_bool,n) for m,n in yanlislar]
    S.insert(hedef,(dogru[0],hedef_bool,dogru[1]))
    return tek(S,hedef_bool)
def cap(s): return ('İ' if s[0]=='i' else s[0].upper())+s[1:]
def oy(d,anahtarlar=None):
    return ' · '.join(f'{k}: '+('doğru' if d[k][0] else 'yanlış') for k in (anahtarlar or d))
def adim_onc(d,keys,baslik=None):
    ac=' '.join(cap(d[k][1])+'.' for k in keys)
    return A(baslik or ('. '.join(keys)+'. öncül' if len(keys)==1 else ' ve '.join(keys)+'. öncüller'),ac,oy(d,keys))

# ---------- çizim yardımcıları ----------
def disc(x,y,r=.12,f='vurgu!25'): return f'\\draw[thin,fill={f}] ({x:.3f},{y:.3f}) circle ({r});'
def nokta(x,y,r=.06): return f'\\fill ({x:.3f},{y:.3f}) circle ({r});'
def uzak(p,L,m): return all((p[0]-a)**2+(p[1]-b)**2>=m*m for a,b in L)
def rastgele(n,x1,x2,y1,y2,m,seed,L0=()):
    rng=random.Random(seed)
    for deneme in range(2000):
        L=list(L0); new=[]
        for _ in range(4000):
            p=(rng.uniform(x1,x2),rng.uniform(y1,y2))
            if uzak(p,L,m): L.append(p); new.append(p)
            if len(new)==n: return new
    raise RuntimeError('yerlesmedi')
def kap(x0,W=2.4,Hh=2.2): return f'\\draw[thick] ({x0},{Hh}) -- ({x0},0) -- ({x0+W},0) -- ({x0+W},{Hh});'
def beher(x,lv,w=1.7,h=2.3,fill='vurgu!15'):
    return f'\\fill[{fill}] ({x},0) rectangle ({x+w},{lv});\\draw[thick] ({x},{h}) -- ({x},0) -- ({x+w},0) -- ({x+w},{h});'
def eksen(xm,ym,sx,sy,xt,yt,xl,yl,xtik=True,grid=True,xlpos=None):
    s=''
    if grid:
        for v in yt:
            if v!=0: s+=f'\\draw[black!15] (0,{v*sy:.3f}) -- ({xm*sx:.3f},{v*sy:.3f});'
        for v in xt:
            if v!=0: s+=f'\\draw[black!15] ({v*sx:.3f},0) -- ({v*sx:.3f},{ym*sy:.3f});'
    s+=f'\\draw[thick,{ARR}] (0,0) -- ({xm*sx+.35:.3f},0);\\draw[thick,{ARR}] (0,0) -- (0,{ym*sy+.35:.3f});'
    if xtik:
        for v in xt: s+=f'\\draw[thick] ({v*sx:.3f},0) -- ({v*sx:.3f},-.07) node[below,font=\\footnotesize] {{{v}}};'
    for v in yt: s+=f'\\draw[thick] (0,{v*sy:.3f}) -- (-.07,{v*sy:.3f}) node[left,font=\\footnotesize] {{{v if v>=0 else "$-$"+str(-v)}}};'
    s+=f'\\node[below,font=\\footnotesize] at ({xm*sx/2 if xlpos is None else xlpos:.3f},{-.55 if xtik else -.2}) {{{xl}}};'
    s+=f'\\node[above,font=\\footnotesize] at (0,{ym*sy+.4:.3f}) {{{yl}}};'
    return s
def egri(pts,sx,sy,stil='thick'):
    c=' '.join(f'({x*sx:.3f},{y*sy:.3f})' for x,y in pts)
    return f'\\draw[{stil}] plot[smooth,tension=.7] coordinates {{{c}}};'


# ============================================================ KARTLAR
kartla('01','Erime ve kaynama noktasından hâl belirleme','Sıcaklık erime noktasının altındaysa madde katı, erime ile kaynama noktası arasındaysa sıvı, kaynama noktasının üstündeyse gazdır.','Sıcaklığı yalnız kaynama noktasıyla karşılaştırmak; erime noktasının altındaki bir maddeyi sıvı saymak.','kolay','öncüllü',3)
kartla('02','Açık uçlu manometre ile gaz basıncı','Gaz tarafındaki sıvı yüzeyi daha alçaksa gaz basıncı dış basınçtan büyük, daha yüksekse küçüktür; fark kadar basınç eklenir ya da çıkarılır.','Seviyesi alçak olan tarafın basıncını küçük sanmak; seviye farkını basıncın kendisi sanmak.','kolay','şekilli',3)
kartla('03','Pistonlu kapta gaz basıncı ve tanecik modeli','Gaz basıncı, taneciklerin çeperlere çarpmasından oluşur; sabit sıcaklıkta hacim küçülünce çarpma sıklığı artar, sabit hacimde sıcaklık artınca çarpmalar hem sıklaşır hem şiddetlenir.','Hacim küçülünce taneciklerin ortalama hızının arttığını sanmak.','zor','öncüllü',4)
kartla('04','Kılcallık ve yapışma–birbirini çekme kuvvetleri','Sıvının tüp duvarına yapışma kuvveti kendi molekülleri arası çekimden büyükse sıvı tüpte yükselir (içbükey), küçükse çökmüş görünür (dışbükey).','Kılcal tüp kalınlaştıkça yükselmenin arttığını sanmak.','orta','şekilli',3)
kartla('05','Buhar basıncı–sıcaklık grafiği','Buhar basıncı sıcaklıkla artar; dış basınca eşitlendiği sıcaklık kaynama noktasıdır; aynı sıcaklıkta buhar basıncı büyük olan sıvıda moleküller arası çekim zayıftır.','Eğrinin eğimiyle buhar basıncının büyüklüğünü karıştırmak; kaynama noktası düşük sıvının çekim kuvvetini büyük sanmak.','orta','öncüllü',4)
kartla('06','Kapalı kapta sıvı–buhar dengesi','Denge hâlinde buharlaşma ve yoğunlaşma hızları eşittir; buhar basıncı yalnız sıcaklığa ve sıvının cinsine bağlıdır, sıvının miktarına ya da kabın hacmine bağlı değildir.','Hacim büyüyünce buhar basıncının düşeceğini sanmak.','orta','hikâyeli',3)
kartla('07','Uçuculuk ve moleküller arası çekim','Aynı koşulda daha çok buharlaşan sıvı daha uçucudur: buhar basıncı büyük, kaynama noktası düşük, moleküller arası çekimi zayıftır.','Uçucu olan sıvının kaynama noktasının yüksek olduğunu sanmak.','orta','grafik',3)
kartla('08','Gazların tanecik modeliyle açıklanması','Gaz taneciklerinin arasındaki çekim çok zayıf, boşluk çok büyüktür; tanecikler sürekli ve gelişigüzel hareket eder.','Gazların tanecikleri arasında da katılardaki gibi güçlü çekim olduğunu sanmak.','kolay','tablo',2)
kartla('09','Yüzey gerilimi ve sıvı yüzeyi','Yüzey gerilimi sıvı yüzeyindeki moleküllerin içeri çekilmesinden doğar; sıvıdaki molekül çekimi azaldıkça yüzey gerilimi düşer ve yüzeyde duran küçük cisimler batabilir.','Cismin batmasını yalnız yoğunluğuna bağlamak.','orta','şekilli',3)
kartla('10','Saf maddenin ısıtma eğrisi','Isıtma eğrisinde eğik bölümlerde sıcaklık artar (hâl aynı kalır); yatay bölümlerde hâl değişir, sıcaklık sabit kalır, verilen ısı taneciklerin potansiyel enerjisini artırır.','Yatay bölümde ısının kesildiğini ya da kinetik enerjinin arttığını sanmak.','orta','öncüllü',4)

# ============================================================ 01 · hâl tablosu (kolay, öncüllü, tablo)
HT=[('X',-90,-40),('Y',-20,90),('Z',60,280),('T',-5,60)]
def hal(m,t):
    e,k=[(a,b) for n,a,b in HT if n==m][0]
    return 'katı' if t<e else ('sıvı' if t<k else 'gaz')
SK1=tablo_svg(['Madde','Erime noktası (°C)','Kaynama noktası (°C)'],[[n,str(a),str(b)] for n,a,b in HT])
assert hal('Y',25)=='sıvı' and hal('T',25)=='sıvı' and hal('Z',100)=='sıvı' and hal('X',0)=='gaz'
d={'I':(True,'25 °C, Y için −20 ile 90 arasında, T için −5 ile 60 arasındadır; ikisi de sıvıdır'),
   'II':(False,'100 °C, Z’nin erime noktası (60 °C) ile kaynama noktası (280 °C) arasındadır; Z sıvıdır, katı değildir'),
   'III':(True,'0 °C, X’in kaynama noktasının (−40 °C) üstündedir; X gaz hâldedir')}
r=onc_t(d,2)
q('0001',ad=[A('Hâl aralıklarını yaz','Erime noktasının altı katı, iki nokta arası sıvı, kaynama noktasının üstü gazdır.','X: −90 ve −40; Y: −20 ve 90; Z: 60 ve 280; T: −5 ve 60'),adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),A('Sonucu yaz','Doğru olan öncüller bir arada yazılır.',oy(d)+' · Sonuç: '+r['dogru'])],
 alt='Hâl Değişimi',z='kolay',kaz='Erime ve kaynama noktalarını kullanarak verilen sıcaklıkta maddenin hâlini belirler.',kalip='öncüllü',ne='dört maddenin erime ve kaynama noktası tablosu',
 metin='X, Y, Z ve T saf maddelerinin 1 atm basınçtaki erime ve kaynama noktaları tabloda verilmiştir.\nI. 25 °C’ta Y ve T sıvı hâldedir.\nII. 100 °C’ta Z katı hâldedir.\nIII. 0 °C’ta X gaz hâldedir.\nBuna göre hangileri doğrudur?',
 sekil=SK1,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan öncüller.',
 ip=['Her yargıdaki sıcaklığı ilgili maddenin iki hâl değişim sıcaklığıyla karşılaştır.'],
 bilgi=[B('Hâl ve sıcaklık','Sıcaklık erime noktasının altındaysa madde katı, erime ve kaynama noktaları arasındaysa sıvı, kaynama noktasının üstündeyse gazdır. Örnek: erime noktası 0 °C, kaynama noktası 100 °C olan bir maddenin 50 °C’ta sıvı olması gerekir')],
 puf='Sıcaklığı hem erime hem kaynama noktasıyla karşılaştır; iki sınırın arasında madde sıvıdır.')

# ============================================================ 02 · manometre (kolay, şekil)
def manom(xo,yl,yr,ad,h,seed):
    yt=3.0; yb=.2
    s=f'\\begin{{scope}}[xshift={xo}cm]'
    s+=f'\\fill[black!35] (2.6,{yb}) rectangle (3.0,{yl}); \\fill[black!35] (2.6,{yb}) rectangle (3.8,{yb+.4}); \\fill[black!35] (3.4,{yb}) rectangle (3.8,{yr});'
    s+=f'\\draw[thick] (2.6,{yt+.4}) -- (2.6,{yb}) -- (3.8,{yb}) -- (3.8,{yt}); \\draw[thick] (3.0,{yt+.4}) -- (3.0,{yb+.4}) -- (3.4,{yb+.4}) -- (3.4,{yt});'
    s+=f'\\draw[thick] (2.6,{yt+.4}) -- (1.8,{yt+.4}) -- (1.8,{yt+1.7}) -- (3.8,{yt+1.7}) -- (3.8,{yt+.4}) -- (3.0,{yt+.4});'
    for x,y in rastgele(6,2.05,3.55,yt+.6,yt+1.5,.38,seed): s+=disc(x,y,.07,'black!20')
    s+=f'\\draw[dashed,black!50] (3.0,{yl}) -- (4.35,{yl}); \\draw[dashed,black!50] (3.8,{yr}) -- (4.35,{yr});'
    s+=f'\\draw[{{Stealth[length=1.6mm]}}-{{Stealth[length=1.6mm]}}] (4.25,{yl}) -- (4.25,{yr});'
    s+=f'\\node[anchor=west,font=\\footnotesize] at (4.35,{(yl+yr)/2}) {{$h={h}$ cm}};'
    s+=f'\\node[font=\\bfseries] at (3.2,-.35) {{{ad}}};'
    return s+'\\end{scope}'
g=manom(0,1.5,2.1,'K',4,3)+manom(6.6,2.25,1.95,'L',2,5)
SK2=tk(g)
dg=('K’deki gazın basıncı dış basınçtan büyük, L’deki gazın basıncı dış basınçtan küçüktür.','gaz tarafındaki cıva K’de alçak, L’de yüksektir; K’de gaz cıvayı aşağı iter, L’de dış basınç cıvayı gaza doğru iter')
yl=[('K’deki gazın basıncı 72 cmHg’dir.','gaz tarafındaki cıva daha alçak olduğundan basınç 76 cmHg’den büyüktür: 76 + 4 = 80 cmHg'),
    ('L’deki gazın basıncı 78 cmHg’dir.','L’de gaz tarafındaki cıva daha yüksektir; basınç 76 − 2 = 74 cmHg’dir'),
    ('İki kaptaki gazın basıncı da dış basınca eşittir; seviye farkı kap şeklinden kaynaklanır.','seviye farkı, gaz basıncının dış basınçtan farklı olduğunu gösterir'),
    ('L’deki gazın basıncı K’dekinden büyüktür.','K’de 80, L’de 74 cmHg; K’deki gazın basıncı daha büyüktür')]
r=tek_t(dg,yl,0,True)
q('0002',ad=[A('Seviyeleri karşılaştır','Gaz tarafındaki cıva alçaksa gaz basıncı dış basınçtan büyüktür.','K: gaz tarafı alçak; L: gaz tarafı yüksek'),A('Basınçları hesapla','Basınç, dış basınca seviye farkı eklenerek ya da çıkarılarak bulunur.','K: 76 + 4 = 80; L: 76 − 2 = 74'),A('Yargıları sına','Bulunan değerler her yargıyla karşılaştırılır.','K > 76 ve L < 76')],
 alt='Gazlar',z='kolay',kaz='Açık uçlu manometre şeklinden gaz basıncını dış basınçla karşılaştırır.',kalip='şekilli',ne='K ve L kaplarına bağlı manometreler, h = 4 ve 2 cm',
 metin='Dış basıncın 76 cmHg olduğu bir ortamda, K ve L kaplarındaki gazlar açık uçlu cıvalı manometrelere şekildeki gibi bağlanmıştır. Manometrelerdeki cıva seviyeleri arasındaki fark K’de 4 cm, L’de 2 cm olarak ölçülmüştür.\nBuna göre aşağıdakilerden hangisi doğrudur?',
 sekil=SK2,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargı.',
 ip=['Gaz tarafındaki cıvanın dış basınç tarafına göre alçak mı yüksek mi olduğuna bak.'],
 bilgi=[B('Açık uçlu manometre','Gaz basıncı, açık uçtaki dış basınca cıva sütunu farkının eklenmesi ya da çıkarılmasıyla bulunur. Örnek: gaz tarafı daha yüksek olan bir manometrede gaz basıncı dış basınçtan küçüktür')],
 puf='Gaz tarafındaki sıvı alçaksa gaz basıncı dış basınçtan büyüktür; farkı ekle ya da çıkar.')

# ============================================================ 03 · piston ve tanecik modeli (orta, öncüllü, şekil)
def silin(x0,p,n,ad,seed):
    s=f'\\draw[thick] ({x0},3.7) -- ({x0},0) -- ({x0+2},0) -- ({x0+2},3.7);'
    s+=f'\\draw[thick,fill=black!30] ({x0+.03},{p}) rectangle ({x0+1.97},{p+.14}); \\draw[thick] ({x0+1},{p+.14}) -- ({x0+1},{p+.85}); \\draw[thick] ({x0+.65},{p+.85}) -- ({x0+1.35},{p+.85});'
    for x,y in rastgele(n,x0+.22,x0+1.78,.2,p-.2,.42,seed): s+=disc(x,y,.08,'vurgu!25')
    s+=f'\\node[font=\\bfseries] at ({x0+1},-.4) {{{ad}}};'
    return s
g=silin(0,3.0,8,'K: 25 $^\\circ$C',11)+silin(3.4,1.5,8,'L: 25 $^\\circ$C',12)+silin(6.8,1.5,8,'M: 75 $^\\circ$C',13)
SK3=tk(g)
d={'I':(False,'K ve L’nin sıcaklığı aynıdır (25 °C); taneciklerin ortalama hızı değişmez, hacmin küçülmesi hızı artırmaz'),
   'II':(True,'tanecik sayısı aynı, hacim yarıya inmiştir; gaz çeperlere daha sık çarpar, basınç büyür'),
   'III':(True,'M’nin hacmi L ile aynı, sıcaklığı yüksektir; tanecikler hızlanır, çeperlere daha sık ve daha şiddetli çarpar, basınç büyür')}
r=onc_t(d,3)
q('0003',ad=[A('Durumları karşılaştır','K’den L’ye yalnız hacim, L’den M’ye yalnız sıcaklık değişir.','K→L: V küçülür; L→M: T artar'),adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),A('Sonucu yaz','Doğru olan öncüller bir arada yazılır.',oy(d)+' · Sonuç: '+r['dogru'])],
 alt='Gazlar',z='orta',kaz='Pistonlu kaptaki gazın basıncını tanecik modeliyle hacim ve sıcaklık değişimleri için yorumlar.',kalip='öncüllü',ne='K, L ve M pistonlu kaplar, tanecik modeli, 25 ve 75 °C',
 metin='Sürtünmesiz pistonlu bir kapta bulunan sabit miktardaki gaz, şekilde K durumundan L durumuna sıcaklığı sabit tutularak sıkıştırılıyor; L durumundaki gaz, pistonu sabitleyip ısıtılınca M durumuna getiriliyor.\nI. K’den L’ye geçerken gaz taneciklerinin ortalama hızı artar.\nII. L’deki gazın basıncı K’dekinden büyüktür.\nIII. M’deki gazın basıncı L’dekinden büyüktür.\nBuna göre hangileri doğrudur?',
 sekil=SK3,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan öncüller.',
 ip=['Her geçişte yalnız hangi niceliğin (hacim ya da sıcaklık) değiştiğini belirle.'],
 bilgi=[B('Gaz basıncının kaynağı','Gaz basıncı, tanecikler kap çeperine çarptıkça oluşur. Çarpma sıklığı arttıkça basınç büyür. Örnek: sabit hacimli kapalı bir kapta tanecik sayısı artırılırsa çarpma sayısı artar ve basınç yükselir')],
 puf='Her geçişte hangi niceliğin değiştiğini, hangisinin sabit kaldığını belirleyip basınçla ilişkilendir.')

# ============================================================ 04 · kılcal tüp (orta, şekil)
def kilcal(x0,lv,tl,renk,ad,egik):
    s=f'\\fill[{renk}] ({x0},0) rectangle ({x0+2.4},{lv}); \\draw[thick] ({x0},3.2) -- ({x0},0) -- ({x0+2.4},0) -- ({x0+2.4},3.2);'
    cx=x0+1.2
    s+=f'\\fill[{renk}] ({cx-.15},.55) rectangle ({cx+.15},{tl});'
    s+=f'\\draw[thick] ({cx-.15},3.4) -- ({cx-.15},.55); \\draw[thick] ({cx+.15},3.4) -- ({cx+.15},.55);'
    e=.09
    if egik: s+=f'\\draw[thick] ({cx-.15},{tl+e}) .. controls ({cx-.1},{tl-.02}) and ({cx+.1},{tl-.02}) .. ({cx+.15},{tl+e});'
    else: s+=f'\\draw[thick] ({cx-.15},{tl-e}) .. controls ({cx-.1},{tl+.04}) and ({cx+.1},{tl+.04}) .. ({cx+.15},{tl-e});'
    s+=f'\\draw[dashed,black!50] ({x0+.1},{lv}) -- ({cx-.3},{lv});'
    s+=f'\\node[font=\\bfseries] at ({cx},-.4) {{{ad}}};'
    return s
g=kilcal(0,1.5,2.4,'vurgu!20','K: su',True)+kilcal(3.8,1.5,1.0,'black!40','L: cıva',False)
SK4=tk(g)
dg=('Suyun cama çekimi kendi molekülleri arasındaki çekimden büyüktür; cıvada bunun tersi geçerlidir.','su tüp duvarına yapışıp yükselir (içbükey), cıva kendi içinde birbirini daha çok çeker ve çöker (dışbükey)')
yl=[('Cıva moleküllerinin cama çekimi kendi aralarındaki çekimden büyüktür; bu yüzden cıva tüpte yükselmiştir.','cıva tüpte kabın seviyesinin altında kalmıştır; yani kendi molekülleri arasındaki çekim cama çekimden büyüktür'),
    ('Tüpler kalınlaştırılırsa sıvı seviyesi daha çok yükselir.','kılcal tüp inceldikçe yükselme artar; kalınlaşınca azalır'),
    ('İki sıvıda da kendi molekülleri arası çekim cama çekimden büyüktür; seviye farkı sıvı miktarından kaynaklanır.','su cama yapışmaktadır ve yükselmiştir; seviye farkı çekim kuvvetlerinin farkındandır'),
    ('Sıvının tüpte yükselebilmesi için yüzey geriliminin sıfır olması gerekir.','yükselmenin nedeni yapışma kuvvetidir; sıvıların yüzey gerilimi sıfır olmaz')]
r=tek_t(dg,yl,1,True)
q('0004',ad=[A('Seviyeleri karşılaştır','Kaptaki seviyeye göre K’de sıvı yükselmiş, L’de çökmüştür.','K: kabın üstünde; L: kabın altında'),A('Sonucu yorumla','Yükselme, cama çekimin kendi aralarındaki çekimden büyük olduğunu gösterir.','K: yapışma büyük; L: kendi çekimi büyük'),A('Yargıları sına','Her yargı bu sonuçla karşılaştırılır.','Doğru yargı: K ve L zıt')],
 alt='Sıvılar',z='orta',kaz='Kılcal tüpteki sıvı seviyesinden yapışma ve birbirini çekme kuvvetlerini karşılaştırır.',kalip='şekilli',ne='su ve cıvanın kılcal tüplerdeki seviyeleri',
 metin='Aynı kalınlıktaki iki özdeş kılcal tüp, içinde eşit yükseklikte sıvı bulunan K ve L kaplarına şekildeki gibi daldırılıyor. K kabında su, L kabında cıva vardır. Tüplerdeki sıvı seviyeleri, kaplardaki seviyelerle birlikte şekilde gösterilmiştir.\nBuna göre aşağıdakilerden hangisi doğrudur?',
 sekil=SK4,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargı.',
 ip=['Tüpteki seviyenin kaptaki seviyeye göre yüksek ya da alçak olmasının hangi çekim kuvvetinin baskın olduğunu gösterdiğini düşün.'],
 bilgi=[B('Yapışma ve kendi çekimi','Sıvı ile tüp cidarı arasındaki çekime yapışma, sıvının kendi molekülleri arasındaki çekime birbirini çekme kuvveti denir. Yapışma baskınsa sıvı kılcal tüpte yükselir. Örnek: bitki köklerinden alınan suyun ince borucuklarda yükselmesi')],
 puf='Seviyenin kaba göre konumu, hangi çekimin baskın olduğunu gösterir.')

# ============================================================ 05 · buhar basıncı grafiği (zor, öncüllü, grafik)
def Pb(T,Tb,a): return 760*math.exp(a*(1/(Tb+273.15)-1/(T+273.15)))
SIV={'K':(40,4000),'L':(80,4600),'M':(100,5000)}
for T in range(0,101,5): assert Pb(T,40,4000)>Pb(T,80,4600)>Pb(T,100,5000)
Sx5=.07; Sy5=.005
g=eksen(100,800,Sx5,Sy5,[0,20,40,60,80,100],[0,200,400,600,760],'Sıcaklık ($^\\circ$C)','Buhar basıncı (mmHg)')
g+=f'\\draw[dashed,black!60] (0,{760*Sy5:.3f}) -- ({7.5:.2f},{760*Sy5:.3f});'
for tb in (40,80,100): g+=f'\\draw[dotted,black!60] ({tb*Sx5:.3f},0) -- ({tb*Sx5:.3f},{760*Sy5:.3f}); \\fill ({tb*Sx5:.3f},{760*Sy5:.3f}) circle (.06);'
for nm,(tb,a) in SIV.items():
    pts=[]
    T=0
    while T<=100:
        p=Pb(T,tb,a)
        if p>800:
            Tprev=T-2; pp=Pb(Tprev,tb,a); f=(800-pp)/(p-pp); pts.append((Tprev+2*f,800)); break
        pts.append((T,p)); T+=2
    g+=egri(pts,Sx5,Sy5,'very thick,vurgu' if nm=='M' else ('very thick,black!70' if nm=='L' else 'very thick'))
    xe,ye=pts[-1]; g+=f'\\node[font=\\bfseries,anchor=south west] at ({xe*Sx5:.3f},{ye*Sy5:.3f}) {{{nm}}};'
SK5=tk(g)
d={'I':(False,'30 °C’ta eğrilerin yüksekliği K > L > M sıralamasındadır; buhar basıncı en büyük olan K’dir, M en küçüğüdür'),
   'II':(True,'760 mmHg’ye M’nin eğrisi en yüksek sıcaklıkta (100 °C) ulaşır; kaynama noktası en yüksek olan M’nin moleküller arası çekimi en güçlüdür, K’nin en zayıftır'),
   'III':(True,'K 40 °C’ta, L ise 80 °C’ta 760 mmHg’ye ulaşır; bu değerler eşittir')}
r=onc_t(d,3)
q('0005',ad=[A('Eğrileri oku','760 mmHg çizgisine eğriler farklı sıcaklıklarda ulaşır.','K: 40; L: 80; M: 100 (°C)'),adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),A('Sonucu yaz','Doğru olan öncüller bir arada yazılır.',oy(d)+' · Sonuç: '+r['dogru'])],
 alt='Buhar Basıncı',z='orta',kaz='Buhar basıncı–sıcaklık grafiğinden kaynama noktası ve moleküller arası çekim kuvveti karşılaştırması yapar.',kalip='öncüllü',ne='K, L, M için buhar basıncı–sıcaklık grafiği',
 metin='Saf K, L ve M sıvılarının buhar basıncının sıcaklıkla değişimi grafikte verilmiştir. Kesikli çizgi, deniz seviyesindeki dış basıncı (760 mmHg) göstermektedir; eğrilerin bu çizgiyle kesiştiği noktalar işaretlenmiştir.\nI. 30 °C’ta buhar basıncı en büyük olan sıvı M’dir.\nII. Moleküller arası çekim kuvveti en büyük olan M, en küçük olan K’dir.\nIII. K’nin 40 °C’taki buhar basıncı, L’nin 80 °C’taki buhar basıncına eşittir.\nBuna göre hangileri doğrudur?',
 sekil=SK5,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan öncüller.',
 ip=['Her sıcaklıkta hangi eğrinin daha yukarıda olduğuna ve eğrilerin 760 mmHg çizgisini kestiği sıcaklıklara bak.'],
 bilgi=[B('Buhar basıncı ve kaynama','Sıvının buhar basıncı dış basınca eşit olunca sıvı kaynar. Aynı sıcaklıkta buhar basıncı büyük olan sıvı daha uçucudur ve moleküller arası çekimi daha zayıftır. Örnek: kaynama noktası düşük olan bir sıvı oda sıcaklığında daha çabuk buharlaşır')],
 puf='Aynı sıcaklıkta eğrisi üstte olan sıvı uçucudur; 760 mmHg çizgisini kestiği sıcaklık kaynama noktasıdır.')

# ============================================================ 06 · sıvı–buhar dengesi, piston (orta, hikâyeli)
dg=('Piston çekilince sıvının bir kısmı buharlaşır ve yeniden denge kurulduğunda buhar basıncı ilk değerine eşit olur.','sabit sıcaklıkta buhar basıncı yalnız sıvının cinsine ve sıcaklığa bağlıdır; sıvı bir miktar buharlaşarak basıncı eski değerine getirir')
yl=[('Hacim büyüdüğü için buhar basıncı düşer ve yeni dengede ilk basınçtan küçük kalır.','sıvı olduğu sürece buhar basıncı değişmez; buharlaşarak eksik basıncı tamamlar'),
    ('Piston çekilirken buharlaşma durur, çünkü sıvı–buhar dengesi bozulmuştur.','buharlaşma durmaz; yoğunlaşma yavaş kalır, net buharlaşma olur ve yeni denge kurulur'),
    ('Dengeye ulaşıldığında kaptaki sıvı miktarı ilk hâlindekiyle aynıdır.','hacim büyüdüğü için buhar miktarı artmıştır; sıvı miktarı azalmıştır'),
    ('Sıcaklık sabit olsa da buhar basıncı hacimle ters orantılı olarak değişir.','buhar basıncı hacme bağlı değildir; yalnız sıcaklığa ve sıvının cinsine bağlıdır')]
r=tek_t(dg,yl,1,True)
q('0006',ad=[A('Dengeyi anla','Denge hâlinde buharlaşma ve yoğunlaşma hızları eşittir.','Piston çekilir → buhar seyrelir'),A('Yeni durumu yorumla','Net buharlaşma, buhar basıncı eski değere dönene kadar sürer.','Sıcaklık sabit → basınç eski değer'),A('Yargıları sına','Her yargı bu sonuçla karşılaştırılır.','Doğru yargı: basınç ilk değerine döner')],
 alt='Buhar Basıncı',z='orta',kaz='Kapalı kapta sıvı–buhar dengesi bozulduğunda buhar basıncı ve sıvı miktarındaki değişimi yorumlar.',kalip='hikâyeli',ne='pistonlu kapta sıvı–buhar dengesi, hacim artırma',
 metin='Fen kulübünde Elif, sıcaklığı 25 °C’ta sabit tutulan pistonlu ve kapalı bir kaba az miktarda saf su koyuyor. Bir süre sonra kapta sıvı su ile su buharı dengeye ulaşıyor. Sonra Elif pistonu sabit sıcaklıkta yavaşça yukarı çekiyor; kapta hâlâ sıvı su kalıyor ve yeniden denge kuruluyor.\nBuna göre aşağıdakilerden hangisi doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargı.',
 ip=['Buhar basıncının hangi niceliklere bağlı olduğunu düşün.'],
 bilgi=[B('Sıvı–buhar dengesi','Kapalı kapta buharlaşma hızı yoğunlaşma hızına eşit olunca denge kurulur. Dengedeki buhar basıncı, sıcaklık sabit kaldıkça değişmez. Örnek: aynı sıcaklıkta eterin buhar basıncı suyunkinden büyüktür')],
 puf='Buhar basıncının hangi niceliklere bağlı olduğunu hatırla.')

# ============================================================ 07 · uçuculuk çubuk grafiği (orta, grafik)
KV=[('K',10),('L',30),('M',40)]
Sy7=.08
g=eksen(3.4,50,1,Sy7,[],[0,10,20,30,40,50],'','Kalan hacim (mL)',xtik=False)
g+=f'\\draw[dashed,black!60] (0,{50*Sy7}) -- (4.4,{50*Sy7}); \\node[anchor=west,font=\\footnotesize] at (4.4,{50*Sy7}) {{başlangıç}};'
for i,(nm,v) in enumerate(KV):
    x=.9+i*1.1
    g+=f'\\draw[fill=vurgu!30,thick] ({x-.35:.2f},0) rectangle ({x+.35:.2f},{v*Sy7:.3f}); \\node[font=\\small\\bfseries] at ({x:.2f},-.35) {{{nm}}};'
SK7=tk(g)
dg=('K sıvısının aynı sıcaklıktaki buhar basıncı en büyüktür; kaynama noktası en düşüktür.','en çok buharlaşan K en uçucudur: buhar basıncı büyük, moleküller arası çekimi zayıf, kaynama noktası düşüktür')
yl=[('M sıvısı en uçucu olduğu için kaynama noktası en düşüktür.','en az buharlaşan M en az uçucudur; kaynama noktası en yüksektir'),
    ('Kalan hacmi en fazla olan sıvının buharlaşma hızı en büyüktür.','kalan hacmi en fazla olan sıvı en az buharlaşmıştır; hızı en küçüktür'),
    ('Üç sıvının buhar basıncı eşittir; kalan hacim farkı kap şeklinden kaynaklanır.','kaplar özdeştir; kalan hacim farkı buhar basınçlarının farklı olmasındandır'),
    ('L sıvısı K sıvısından daha çok buharlaşmıştır.','K’nin kalan hacmi daha azdır; K daha çok buharlaşmıştır')]
r=tek_t(dg,yl,4,True)
q('0007',ad=[A('Grafiği oku','Başlangıç hacmi 50 mL’dir; buharlaşan hacim 50 − kalan hacimdir.','K: 40; L: 20; M: 10 mL buharlaşmış'),A('Uçuculuğu sırala','Çok buharlaşan sıvı daha uçucudur.','K > L > M'),A('Yargıları sına','Uçuculuk sıralaması her yargıyla karşılaştırılır.','Doğru yargı: K en uçucu')],
 alt='Buhar Basıncı',z='orta',kaz='Buharlaşan miktardan sıvıların uçuculuğunu, buhar basıncını ve kaynama noktasını karşılaştırır.',kalip='grafik',ne='üç sıvının kalan hacim çubuk grafiği',
 metin='Özdeş açık kapların her birine 50 mL olacak biçimde saf K, L ve M sıvıları konuyor. Kaplar aynı odada, aynı sıcaklıkta bir gün bekletildikten sonra sıvıların kalan hacimleri ölçülüyor ve sonuçlar grafikte verilmiştir.\nBuna göre aşağıdakilerden hangisi doğrudur?',
 sekil=SK7,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargı.',
 ip=['Her sıvının ne kadarının buharlaştığını bulup sıralamaya bak.'],
 bilgi=[B('Uçuculuk','Aynı koşulda hızlı buharlaşan sıvı uçucudur; buhar basıncı büyük, kaynama noktası düşüktür. Örnek: açık bir tabaktaki bir sıvının zamanla azalması buharlaşmanın göstergesidir')],
 puf='Çok buharlaşan sıvı: buhar basıncı büyük, çekim zayıf, kaynama noktası düşüktür.')

# ============================================================ 08 · gaz modeli tablosu (kolay, tablo, olumsuz)
GS=[('Gaz, kabı tamamen doldurur','Çekim çok zayıf, tanecikler serbest',True),
    ('Gazlar kolayca sıkıştırılabilir','Tanecikler arası boşluk çok büyük',True),
    ('Gazların belirli bir şekli yoktur','Tanecikler güçlü çekimle bağlı',False),
    ('Kapalı kapta gaz basıncı oluşur','Tanecikler çeperlere çarpar',True),
    ('İki gaz kısa sürede karışır','Tanecikler sürekli hareket eder',True)]
SK8=tablo_svg(['Gözlem','Tanecik modeline göre açıklama'],[[a,b] for a,b,_ in GS])
yan_=[x for x in GS if not x[2]][0]
dg=(yan_[0],'gaz tanecikleri arasındaki çekim çok zayıftır; şekil belirsizliği bu yüzdendir')
nedenler={'Gaz, kabı tamamen doldurur':'tanecikler serbestçe hareket eder','Gazlar kolayca sıkıştırılabilir':'tanecikler arasındaki boşluk çok büyüktür','Kapalı kapta gaz basıncı oluşur':'tanecikler çeperlere çarpar','İki gaz kısa sürede karışır':'tanecikler sürekli hareket eder'}
yl=[(a,nedenler[a]) for a,b,c in GS if c]
r=tek_t(dg,yl,2,False)
q('0008',ad=[A('Tabloyu incele','Her satırda bir gözlem ve onun tanecik modeline göre açıklaması vardır.','5 gözlem, 5 açıklama'),A('Açıklamaları sına','Gaz taneciklerinin çekimi çok zayıf, boşluğu büyük, hareketi sürekli ve gelişigüzeldir.','Bir açıklama bu modelle çelişir'),A('Satırı belirle','Modelle çelişen açıklamanın gözlemi bulunur.','Çelişen: güçlü çekim')],
 alt='Gazlar',z='kolay',kaz='Gazların özelliklerini tanecik modeliyle eşleştirir.',kalip='tablo',ne='gaz gözlemleri ve tanecik açıklamaları tablosu',
 metin='Öğretmen, gazların bazı gözlemlenebilir özelliklerini ve bu özelliklerin tanecik modeline göre açıklamalarını tabloda vermiştir. Tabloda yalnız bir satırdaki açıklama hatalıdır.\nBuna göre hangi gözlem için verilen açıklama yanlıştır?',
 sekil=SK8,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Açıklaması yanlış olan gözlem.',
 ip=['Gaz taneciklerinin birbirini çekme düzeyini ve aralarındaki boşluğu hatırla.'],
 bilgi=[B('Gazlarda tanecik modeli','Gaz taneciklerinin arasındaki çekim çok zayıf, aralarındaki boşluk çok büyüktür; tanecikler sürekli, hızlı ve gelişigüzel hareket eder. Örnek: bir balona üflenen havanın balonun her yerine yayılması')],
 puf='Gazda çekim çok zayıf, boşluk büyük, hareket sürekli ve gelişigüzeldir.')

# ============================================================ 09 · yüzey gerilimi, ataç (orta, şekil)
def atac(x0,lv,tip_,ad,altyazi):
    s=f'\\fill[vurgu!15] ({x0},0) rectangle ({x0+2.2},{lv}); \\draw[thick] ({x0},2.5) -- ({x0},0) -- ({x0+2.2},0) -- ({x0+2.2},2.5);'
    cx=x0+1.1
    if tip_=='yuzer': s+=f'\\draw[thick,fill=black!50] ({cx-.35},{lv-.02}) rectangle ({cx+.35},{lv+.07}); \\draw[black!60] ({cx-.55},{lv}) .. controls ({cx-.4},{lv-.08}) and ({cx-.35},{lv-.08}) .. ({cx-.3},{lv-.04}); \\draw[black!60] ({cx+.55},{lv}) .. controls ({cx+.4},{lv-.08}) and ({cx+.35},{lv-.08}) .. ({cx+.3},{lv-.04});'
    else: s+=f'\\draw[thick,fill=black!50] ({cx-.35},.05) rectangle ({cx+.35},.14);'
    s+=f'\\node[font=\\bfseries,align=center] at ({cx},-.45) {{{ad}}};'
    return s
g=atac(0,1.7,'yuzer',  'K: su','')+atac(3.4,1.7,'bat','L: su + deterjan','')+atac(6.8,1.7,'bat','M: etanol','')
SK9=tk(g)
dg=('Suyun yüzey gerilimi, hem deterjanlı suyunkinden hem de etanolünkinden büyüktür.','ataç yalnız suyun yüzeyinde kalabildiğine göre su yüzeyi cismi taşıyacak kadar gerilmiştir; L ve M’de gerilim bundan küçüktür')
yl=[('L’de deterjan yüzey gerilimini artırdığı için ataç batmıştır.','deterjan yüzey gerilimini azaltır; gerilim azalınca ataç batar'),
    ('K’de ataç yüzdüğüne göre ataç suyun özkütlesinden küçük bir maddeden yapılmıştır.','ataç metaldir ve sudan yoğundur; yüzmesi yüzey geriliminden kaynaklanır'),
    ('M’de ataç battığı için etanolün yüzey gerilimi sudan büyüktür.','etanolün yüzey gerilimi sudan küçüktür; ataç bu yüzden batar'),
    ('Üç sıvının yüzey gerilimi eşittir; atacın durumu yalnız sıvının derinliğine bağlıdır.','yüzeyde kalma, yüzey gerilimi farkından kaynaklanır; derinlikle ilgisi yoktur')]
r=tek_t(dg,yl,4,True)
q('0009',ad=[A('Gözlemleri yaz','Ataç yalnız K’de yüzeyde kalmış, L ve M’de batmıştır.','K: yüzer; L, M: batar'),A('Gerilimi yorumla','Cismi yüzeyde tutan, yüzey gerilimidir.','Gerilim: K > L ve K > M'),A('Yargıları sına','Her yargı bu sonuçla karşılaştırılır.','Doğru yargı: K’nin gerilimi en büyük')],
 alt='Sıvılar',z='orta',kaz='Yüzeydeki cismin yüzme ya da batma durumundan sıvıların yüzey gerilimlerini karşılaştırır.',kalip='şekilli',ne='su, deterjanlı su ve etanolde ataç',
 metin='Aynı sıcaklıkta K, L ve M kaplarına eşit yükseklikte sıvı konuyor. K’de saf su, L’de saf su ile birkaç damla deterjan, M’de etanol bulunmaktadır. Özdeş metal ataçlar sıvıların yüzeyine dikkatle bırakılıyor; sonuç şekilde verilmiştir.\nBuna göre aşağıdakilerden hangisi doğrudur?',
 sekil=SK9,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargı.',
 ip=['Atacı yüzeyde tutan kuvvetin ne olduğunu ve hangi sıvılarda bunun yetmediğini düşün.'],
 bilgi=[B('Yüzey gerilimi','Sıvı yüzeyindeki moleküller içeri doğru çekilir; bu, yüzeyi gerili bir zar gibi davranmaya iter. Moleküller arası çekim azaldıkça yüzey gerilimi düşer. Örnek: bazı böceklerin su üstünde yürüyebilmesi')],
 puf='Yüzeyde kalma ile yüzey gerilimi arasındaki ilişkiyi düşün.')

# ============================================================ 10 · ısıtma eğrisi (zor, öncüllü, grafik)
Sx10=.31; Sy10=.025
g=eksen(22,160,Sx10,Sy10,list(range(0,23,2)),[0,40,80,120,160],'Zaman (dk)','Sıcaklık ($^\\circ$C)')
Ptl=[(0,0),(2,40),(6,40),(14,120),(20,120),(22,160)]
g+='\\draw[very thick,vurgu] '+' -- '.join(f'({t*Sx10:.3f},{T*Sy10:.3f})' for t,T in Ptl)+';'
def Tz(t):
    for (t1,T1),(t2,T2) in zip(Ptl,Ptl[1:]):
        if t1<=t<=t2: return T1+(T2-T1)*(t-t1)/(t2-t1)
for nm,t,pos in (('K',1,'below right'),('L',4,'above'),('M',10,'below right'),('N',17,'above')):
    g+=f'\\fill ({t*Sx10:.3f},{Tz(t)*Sy10:.3f}) circle (.07); \\node[font=\\bfseries,{pos}] at ({t*Sx10:.3f},{Tz(t)*Sy10:.3f}) {{{nm}}};'
SK10=tk(g)
assert Tz(4)==40 and Tz(17)==120 and Tz(10)==80
d={'I':(True,'L, 40 °C’lik yatay (erime) bölümdedir; madde hem katı hem sıvı hâldedir'),
   'II':(False,'N, 120 °C’lik yatay (kaynama) bölümdedir; madde hem sıvı hem gaz hâldedir, yalnız gaz değildir'),
   'III':(False,'K’den L’ye giderken önce sıcaklık artar (kinetik enerji artar), sonra erime sırasında verilen ısı potansiyel enerjiyi artırır; yalnız kinetik enerji artmaz')}
r=onc_t(d,0)
q('0010',ad=[A('Bölümleri belirle','Eğik bölümlerde sıcaklık artar; yatay bölümlerde hâl değişir.','0–2: katı ısınır; 2–6: erime; 6–14: sıvı ısınır; 14–20: kaynama'),adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),A('Sonucu yaz','Doğru olan öncüller bir arada yazılır.',oy(d)+' · Sonuç: '+r['dogru'])],
 alt='Hâl Değişimi',z='orta',kaz='Isıtma eğrisinin eğik ve yatay bölümlerini hâl ve enerji türü açısından yorumlar.',kalip='öncüllü',ne='saf X maddesinin sıcaklık–zaman grafiği, K, L, M, N noktaları',
 metin='Katı hâldeki saf bir X maddesi, sabit güçlü bir ısıtıcıyla kesintisiz ısıtılıyor. Sıcaklığın zamanla değişimi ve işaretlenen K, L, M, N noktaları grafikte gösterilmiştir.\nI. L noktasında madde hem katı hem sıvı hâldedir.\nII. N noktasında madde yalnız gaz hâldedir.\nIII. K noktasından L noktasına geçerken verilen ısı, yalnızca taneciklerin ortalama kinetik enerjisini artırır.\nBuna göre hangileri doğrudur?',
 sekil=SK10,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan öncüller.',
 ip=['Her işaretli noktanın hangi bölümde olduğuna ve orada sıcaklığın değişip değişmediğine bak.'],
 bilgi=[B('Isıtma eğrisi','Eğik bölümlerde ısı, taneciklerin ortalama kinetik enerjisini (sıcaklığı) artırır. Yatay bölümlerde sıcaklık sabittir; ısı, taneciklerin birbirinden uzaklaşmasına, yani potansiyel enerjiye harcanır. Örnek: kaynayan bir sıvının sıcaklığı kaynama bitene kadar sabit kalır')],
 puf='Yatay bölüm hâl değişimidir (iki hâl birlikte, ısı potansiyel enerjiye); eğik bölümde sıcaklık artar.')

bitir(P,'halleruc',UK)
