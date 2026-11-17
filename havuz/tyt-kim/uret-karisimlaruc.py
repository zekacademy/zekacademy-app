"""TYT Kimya · Karışımlar · 3. ek paket (karisimlaruc): 10 soru, kardeş yok, ipucu 1.
Şekil koordinatları ve veriler Python'da hesaplanır; TikZ bu değerlerden üretilir. Öncüllerin doğru/yanlış değeri tek yerde (d sözlüğü) tanımlanır.
Her sayısal cevap ve çeldirici değer assert edilir."""
import sys,os,math,random,itertools
from fractions import Fraction as Fr
GD=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,GD)
import _hafif_kim2 as H
from _hafif_kim2 import *
from _hafif_kim import onc as _onc_eski, tek
H.KONU='Karışımlar'
UK='kim|Karışımlar'
P=Parti('karisimlaruc','Karışımlar',UK,ders='TYT Kimya',idon='tytkim')
KY='ÖSYM 2018–2026 TYT Kimya (yalnız mantık) · MEB 10. sınıf Karışımlar'
MAP={}
for _n,_t in [(('01','04'),('ayirma','Karışımların ayrılması: süzme ve kromatografi')),(('02','06','09'),('derisim','Derişim: ppm, kütlece yüzde ve karıştırma')),
              (('03','08','10'),('cozunurluk','Çözünürlük, doygunluk ve kristallendirme')),(('05',),('tanecik','Çözelti türleri ve tanecik modeli')),
              (('07',),('sinif','Saf madde ve karışım ayrımı'))]:
    for _x in _n: MAP[_x]=_t
assert len(MAP)==10
def kartla(n,alt,fikir,tuzak,z,kalip,adim):
    a,b=MAP[n]; kart(f'K-KMKR3-{n}',alt,fikir,tuzak,z,kalip,adim,f'km-kr3-{a}',b,KY)
def q(no,ad,**k):
    assert len(k['ip'])==1
    k['tipId']='km-kr3-'+MAP[no[-2:]][0]; k['tip']=MAP[no[-2:]][1]
    ne=k.pop('ne'); k['kart']=f"K-KMKR3-{no[-2:]} ({MAP[no[-2:]][1].lower()}) · {ne}"
    mk(P,no,ad=ad,adim=len(ad),**k)
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
ARR='-{Stealth[length=1.9mm,width=1.7mm]}'
def tk(g): return tikz_svg(HEAD+g+TAIL)
DC='$^\\circ$C'

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
kartla('01','Süzme düzeneği','Süzmede katı taneler süzgeç kâğıdında kalır, çözünmüş madde sıvıyla birlikte geçer; süzüntü homojen bir karışımdır.','Çözünmüş maddenin süzgeç kâğıdında kaldığını sanmak; süzüntüyü saf su saymak.','kolay','öncüllü',3)
kartla('02','ppm ve kütlece yüzde dönüşümü','1 ppm = 1 mg/kg = 10⁻⁶ oran; kütlece % = 10⁻² oran; 1 % = 10 000 ppm. Madde kütlesi = ppm × çözelti kütlesi (kg) mg olarak bulunur.','Yüzdeyi ppm’e çevirirken ondalık basamağı kaydırmak; ppm değerini toplam kütleyle çarpmamak.','kolay','hikâyeli',3)
kartla('03','Çözünürlük grafiğinden doygunluk yorumu','Çözünürlük g/100 g su cinsindendir; çözeltideki su kütlesiyle ölçeklenir; ısıtma çözünen ve çözelti kütlesini değiştirmediğinden kütlece derişim değişmez, ama doymamış hâle getirir.','Isıtınca derişimin arttığını sanmak; 100 g su değerini toplam suya ölçeklememek.','orta','öncüllü',4)
kartla('04','Kâğıt kromatografisi','Daha az tutunan boya çözücüyle daha yükseğe çıkar; karışımın şeridindeki lekeler bilinen boyalarla aynı yükseklikteyse o boyaları içerir.','Yukarı çıkan boyanın kâğıda daha çok tutunduğunu sanmak; her şeritteki lekeyi aynı maddeye bağlamak.','orta','şekilli',3)
kartla('05','Doymamış ve doygun çözelti tanecik modeli','Dipte çözünmemiş katı bulunan çözelti doygundur; dipte katı yoksa doymamıştır ve aynı sıcaklıkta daha fazla katı çözebilir; çözünmüş tanecik sayısı çok olan çözelti daha derişiktir.','Dipteki katıyı çözeltideki tanecikle karıştırmak; dipte katı olmayan her çözeltiyi doygun saymak.','orta','öncüllü',3)
kartla('06','Su ve çözünen kütlesinden derişim','Su kütlesi–çözünen kütlesi doğrusundan çözelti kütlesi ve kütlece derişim bulunur; karışımda çözünenler toplanır; seyreltmede çözünen kütlesi sabittir.','Su kütlesini çözelti kütlesi saymak; derişimleri ortalamak.','zor','grafik',5)
kartla('07','Isıtma grafiğinde saf madde–karışım','Saf madde erirken sıcaklık sabit kalır; karışımlar erirken sıcaklık değişir ve belirli bir erime noktası yoktur.','Erime sırasında sıcaklığın artmasını saf madde özelliği saymak; platoyu hâl değişimi dışında yorumlamak.','orta','grafik',3)
kartla('08','Çözünürlük farkıyla ayırma','Soğutmada her katının çökeni, eklenen miktar ile düşük sıcaklıktaki çözünürlüğün farkıdır; çözünürlüğü sıcaklıkla çok değişen katı çok, az değişen katı az çöker.','Eklenen katının tamamının çöktüğünü sanmak; çözünürlük değerini çöken miktar saymak.','zor','tablo',4)
kartla('09','Çözeltiyi paylaştırma ve seyreltme','Homojen çözeltiyi bölünce derişim değişmez; su ekleyince çözünen kütlesi sabit kalır, derişim azalır.','Bölünen çözeltideki şeker kütlesinin değişmediğini sanmak; seyrelmede derişimin sabit kaldığını düşünmek.','kolay','öncüllü',3)
kartla('10','Doygunluk grafiği','Çözünen kütle ilk bölümde eklenenle birlikte artar, doygunluktan sonra sabit kalır; fazlası dipte katı olarak birikir.','Yatay bölgede çözünen kütlenin eklenenle arttığını sanmak; derişimi suya göre hesaplamak.','orta','grafik',4)

# ============================================================ 01 · süzme düzeneği (kolay, öncüllü, şekil)
g='\\draw[thick] (0,4.9) -- (0,3.3) -- (1.5,3.3) -- (1.5,4.9); \\fill[vurgu!15] (.02,3.32) rectangle (1.48,4.4); \\draw (0,4.4) -- (1.5,4.4);'
for x,y in [(.25,3.42),(.5,3.4),(.75,3.44),(1.0,3.41),(1.25,3.43),(.4,3.55),(.9,3.56)]: g+=f'\\fill ({x},{y}) circle (.06);'
g+=f'\\draw[{ARR}] (1.75,4.5) to[bend left=25] (2.95,3.75);'
g+='\\draw[thick] (2.9,3.6) -- (3.8,2.5) -- (3.8,1.7) -- (4.2,1.7) -- (4.2,2.5) -- (5.1,3.6);'
g+='\\draw[dashed,thick,vurgu] (3.05,3.5) -- (4.0,2.55) -- (4.95,3.5);'
g+='\\draw[thick] (3.0,1.4) -- (3.0,0) -- (5.0,0) -- (5.0,1.4); \\fill[vurgu!15] (3.02,.02) rectangle (4.98,.55); \\draw (3.0,.55) -- (5.0,.55);'
g+='\\fill (4.0,1.5) circle (.05); \\fill (4.0,1.05) circle (.05);'
def no(x,y,s): return f'\\node[circle,draw,inner sep=1.6pt,font=\\small\\bfseries,fill=white] at ({x},{y}) {{{s}}};'
g+=no(.75,2.95,1)+'\\draw (5.75,3.0) -- (4.5,3.05);'+no(6.0,3.0,2)+no(4.0,-.45,3)
SK1=tk(g)
d={'I':(True,'kum taneleri süzgeç kâğıdının gözeneklerinden geçemeyecek kadar büyüktür ve kâğıtta kalır'),
   'II':(False,'süzüntüde çözünmüş şeker de bulunur; bu nedenle sıvı saf su değil, homojen bir karışımdır'),
   'III':(False,'çözünmüş şeker taneciği çok küçüktür ve süzgeç kâğıdının gözeneklerinden suyla birlikte geçer')}
r=onc_t(d,0)
q('0001',ad=[A('Düzeneği tanı','Karışım 1 numaralı kaptan huniye boşaltılıyor; huniye süzgeç kâğıdı (2) yerleştirilmiş, sıvı 3 numaralı kapta toplanıyor.','1: karışım kabı · 2: süzgeç kâğıdı · 3: süzüntü kabı'),adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),A('Sonucu yaz','Doğru olan öncüller bir arada yazılır.',oy(d)+' · Sonuç: '+r['dogru'])],
 alt='Karışımların Ayrılması',z='kolay',kaz='Süzme düzeneğinde katı ve çözünmüş maddenin hangi bölümde bulunduğunu belirler.',kalip='öncüllü',
 ne='kumlu şekerli su, huni ve iki beher',
 metin='Bir öğrenci, içinde kum bulunan şekerli su karışımını, numaralandırılmış kısımları şekilde gösterilen düzenekle ayırmaya çalışıyor. Karışımı karıştırarak huniye boşaltıyor ve sıvı akıp bitene kadar bekliyor. Süzgeç kâğıdı ince gözeneklidir; şeker tamamen çözünmüş durumdadır.\nI. 2 numaralı kısımda kum kalır.\nII. 3 numaralı kapta toplanan sıvı saf sudur.\nIII. Şeker de 2 numaralı kısımda tutulur.\nBuna göre hangileri doğrudur?',
 sekil=SK1,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan öncüller.',
 ip=['Süzgeç kâğıdından hangi taneciklerin geçebildiğini, hangilerinin geçemediğini düşün.'],
 bilgi=[B('Süzme','Süzme, katı–sıvı heterojen karışımlarını tanecik boyutu farkıyla ayırır; büyük katı taneler süzgeç kâğıdında kalır, çözünmüş maddeler sıvıyla geçer. Örnek: çay süzgeci çay yapraklarını tutar, demlenmiş çay süzgeçten geçer')],
 puf='Süzmede çözünmemiş katı kâğıtta kalır; çözünmüş madde süzüntüyle birlikte geçer.')

# ============================================================ 02 · ppm (kolay, hikâyeli)
yuzde=Fr(4,10000); m_kg=5
ppm=yuzde/100*10**6; mg=ppm*m_kg
assert ppm==4 and mg==20
assert yuzde/100*m_kg*1000==Fr(2,100)            # g cinsinden 0,02
assert ppm*m_kg==20 and (yuzde*10**5)*m_kg==200 and (yuzde*10**6)*m_kg==2000
q('0002',ad=[A('Yüzdeyi ppm’e çevir','Kütlece %0,0004, yüz gramda 0,0004 g demektir; 1 ppm ise milyon gramda 1 g.','%0,0004 = 4 × 10⁻⁶ = 4 ppm'),A('ppm’i anlamlandır','1 ppm = 1 mg madde / 1 kg çözelti.','4 ppm = 4 mg / kg'),A('Kütleyle çarp','Numune 5 kg olduğundan madde kütlesi bulunur.','4 × 5 = 20 mg')],
 alt='Derişim',z='kolay',kaz='Kütlece yüzdeyi ppm’e çevirerek madde kütlesini bulur.',kalip='hikâyeli',ne='kütlece %0,0004 nitrat, 5 kg numune',
 metin='Bir içme suyu numunesinde çözünmüş nitrat derişimi kütlece %0,0004 olarak ölçülmüştür. Laboratuvar, çözünmüş madde miktarını ppm cinsinden de raporlamaktadır (1 ppm: 1 kg çözeltide 1 mg çözünmüş madde; 1 g = 1000 mg). Numune 5 kg’lık bir kaptan alınmıştır ve kapta başka çözünmüş madde bulunmadığı varsayılmaktadır.\nBuna göre kaptaki suda bulunan nitrat kaç mg’dır?',
 dogru=20,yan=[(Fr(2,100),'Kütlece yüzdeyi doğrudan gramla hesaplamış (5000 g × 0,0004/100 = 0,02 g) ve sonucu mg’a çevirmeden yazmış.','islem'),
 (4,'%0,0004’ü 4 ppm’e doğru çevirmiş ama 5 kg ile çarpmayı unutmuş.','dikkat'),
 (200,'Yüzdeyi ppm’e çevirirken 10⁵ ile çarpmış (40 ppm); 40 × 5 = 200.','islem'),
 (2000,'Yüzdeyi 100’e bölmeyi unutup 10⁶ ile çarpmış (400 ppm); 400 × 5 = 2000.','islem')],
 istenen='Kaptaki nitrat kütlesi (mg).',ip=['Önce kütlece yüzdeyi ppm cinsinden yaz; ppm’in kaç mg/kg olduğunu hatırla.'],
 bilgi=[B('ppm ve yüzde','Kütlece % değeri, 100 g çözeltideki madde gramıdır; ppm ise 10⁶ g (1 ton) çözeltideki madde gramıdır, yani 1 % = 10 000 ppm. Örnek: kütlece %0,01 = 100 ppm = 100 mg/kg')],
 puf='Yüzdeyi ppm yapmak için 10 000 ile çarp; ppm değeri mg/kg’dır.')

# ============================================================ 03 · çözünürlük grafiği (orta, öncüllü + grafik)
Sx=.045; Sy=.028
pts3=[(20,25),(40,50),(60,100),(80,150)]
g=eksen(100,150,Sx,Sy,[20,40,60,80,100],[25,50,75,100,125,150],'Sıcaklık (°C)','g X / 100 g su')
g+=egri(pts3,Sx,Sy,'thick,vurgu')+''.join(f'\\fill ({x*Sx:.3f},{y*Sy:.3f}) circle (.06);' for x,y in pts3)
g+=f'\\node[font=\\footnotesize,anchor=south east] at ({80*Sx+.5:.2f},{150*Sy+.05:.2f}) {{X}};'
SK3=tk(g)
S3={20:Fr(25),40:Fr(50),60:Fr(100),80:Fr(150)}
cozelti=300; yuz=Fr(20,100); x_k=cozelti*yuz; su=cozelti-x_k
assert x_k==60 and su==240
assert su*S3[20]/100==x_k            # 20 °C doygun
assert x_k/cozelti==yuz              # ısıtma derişimi değiştirmez
cap60=su*S3[60]/100; assert cap60==240 and x_k+200>cap60 and x_k+150<=cap60
d={'I':(True,'20 °C’de çözünürlük 25 g/100 g sudur; 240 g suda en çok 60 g X çözünür ve çözelti tam bu miktarı içerir'),
   'II':(True,'ısıtma çözünen ve çözelti kütlesini değiştirmediğinden derişim %20 olarak kalır'),
   'III':(False,'60 °C’de 240 g su en çok 240 g X çözer; toplam 260 g X olacağından 20 g X dipte kalır')}
r=onc_t(d,3)
q('0003',ad=[A('Su ve X kütlesini bul','300 g çözeltinin %20’si X’tir; kalanı sudur.','X: 60 g · su: 240 g'),adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),A('Sonucu yaz','Doğru olan öncüller bir arada yazılır.',oy(d)+' · Sonuç: '+r['dogru'])],
 alt='Çözünürlük',z='orta',kaz='Çözünürlük grafiğini su kütlesine ölçekleyerek doygunluk ve derişim yorumu yapar.',kalip='öncüllü',ne='X çözünürlük eğrisi, %20’lik 300 g çözelti',
 metin='Şekildeki grafik, X katısının sudaki çözünürlüğünün sıcaklıkla değişimini 20–80 °C aralığında göstermektedir. Kütlece %20’lik 300 g X sulu çözeltisi 20 °C’de hazırlanmıştır; çözeltide çözünmemiş X yoktur ve ısıtma sırasında su buharlaşmamaktadır.\nI. Çözelti 20 °C’de doygundur.\nII. Çözelti 40 °C’ye ısıtılırsa kütlece derişimi %20 olarak kalır.\nIII. Çözelti 60 °C’ye ısıtılıp üzerine 200 g daha X eklenirse X’in tamamı çözünür.\nBuna göre hangileri doğrudur?',
 sekil=SK3,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan öncüller.',
 ip=['Grafikteki değerler 100 g su içindir; çözeltideki gerçek su kütlesine göre ölçekle.'],
 bilgi=[B('Çözünürlük','Çözünürlük, belirli sıcaklıkta 100 g suda çözünebilen en çok madde kütlesidir. Su kütlesi katlanırsa çözünebilen miktar da aynı katla artar. Örnek: 10 g/100 g su çözünürlüklü maddeden 300 g suda en çok 30 g çözünür')],
 puf='Çözünürlük değerini her zaman çözeltideki su kütlesine ölçekle; ısıtma derişimi değil doygunluk durumunu değiştirir.')

# ============================================================ 04 · kâğıt kromatografisi (orta, şekilli, olumsuz kök)
def yy(h): return .6+.5*h
g='\\draw[thick] (1.0,.2) rectangle (5.7,5.0);'
g+=f'\\draw[dashed] (1.0,{yy(0)}) -- (5.7,{yy(0)}); \\draw[dashed] (1.0,{yy(8)}) -- (5.7,{yy(8)});'
g+=f'\\node[font=\\footnotesize,anchor=west] at (1.1,{yy(0)-.18}) {{başlangıç çizgisi}}; \\node[font=\\footnotesize,anchor=west] at (1.1,{yy(8)+.2}) {{çözücü cephesi}};'
g+='\\draw[thick] (.6,.6) -- (.6,4.6);'
for h in range(0,9): g+=f'\\draw (.6,{yy(h)}) -- (.45,{yy(h)}) node[left,font=\\footnotesize] {{{h}}};'
g+='\\node[font=\\footnotesize,anchor=south] at (.2,4.75) {cm};'
LANE={'K':(1.9,[2]),'L':(3.0,[4]),'M':(4.1,[6]),'X':(5.2,[2,6])}
for nm,(x,hs) in LANE.items():
    g+=f'\\node[font=\\small\\bfseries] at ({x},-.15) {{{nm}}};'
    for h in hs: g+=f'\\draw[fill=black!35] ({x},{yy(h)}) ellipse (.26 and .15);'
    g+=f'\\fill ({x},{yy(0)}) circle (.035);'
SK4=tk(g)
HS={'K':[2],'L':[4],'M':[6],'X':[2,6]}
assert set(HS['X'])==set(HS['K'])|set(HS['M']) and HS['L'][0] not in HS['X']
assert HS['K'][0]<HS['M'][0] and HS['L'][0]>HS['K'][0]
dg=('L boyası, K boyasına göre kâğıda daha fazla tutunur.','L lekesi K lekesinden yukarıdadır; çözücüyle daha kolay ilerleyen boya kâğıda daha az tutunur, yani L daha az tutunur')
yl=[('X mürekkebi, K ve M boyalarını içerir.','X şeridindeki iki leke K ve M lekeleriyle aynı yüksekliktedir'),
    ('X mürekkebi, iki farklı boyanın karışımıdır.','X şeridinde iki ayrı leke oluşmuştur'),
    ('K boyası, M boyasına göre kâğıda daha fazla tutunur.','K lekesi M lekesinden aşağıda kalmıştır; daha az yükselen boya kâğıda daha çok tutunur'),
    ('M boyası, üç boya içinde kâğıda en az tutunandır.','M lekesi en yükseğe çıkmıştır')]
r=tek_t(dg,yl,1,False)
q('0004',ad=[A('Şekli oku','Her şeritteki lekelerin başlangıç çizgisinden yükseklikleri cm olarak okunur.','K: 2 · L: 4 · M: 6 · X: 2 ve 6'),A('X’i yorumla','X’in lekeleri K ve M ile aynı yüksekliktedir; L ile eşleşen leke yoktur.','X = K + M'),A('Tutunmayı karşılaştır','Çözücüyle daha yükseğe çıkan boya kâğıda daha az tutunur.','Yükselme: M > L > K'),A('Yanlış yargıyı bul','Her yargı bu okumalara göre sınanır; kâğıda tutunma sırası ile çelişen yargı yanlıştır.','L, K’den yukarıda → L, K’den daha az tutunur')],
 alt='Karışımların Ayrılması',z='orta',kaz='Kâğıt kromatografisi sonucundan boyaların tutunma sırasını ve karışımın bileşimini yorumlar.',kalip='şekilli',ne='K, L, M ve X şeritleri',
 metin='Bir öğrenci, her biri tek bir boyadan oluşan K, L ve M mürekkeplerini ve bilinmeyen X mürekkebini kâğıt kromatografisi düzeneğinde ayrı şeritlere damlatıyor. Çözücü kâğıtta yükselirken boyaları da farklı mesafelere taşıyor ve öğrenci kâğıdı çözücü cephesi çizgiye ulaşınca çıkarıp kurutuyor. Şekilde kâğıt ve lekelerin yerleri verilmiştir.\nBuna göre aşağıdaki yargılardan hangisi yanlıştır?',
 sekil=SK4,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Yanlış olan yargı.',
 ip=['Çözücü ile daha yükseğe çıkan boyanın kâğıda ne kadar tutunduğunu düşün.'],
 bilgi=[B('Kâğıt kromatografisi','Karışımdaki boyalar, kâğıda tutunma ve çözücüde çözünme farkına göre farklı yüksekliklere çıkar. Kâğıda az tutunan çözücüyle daha yükseğe ilerler. Örnek: aynı yükseklikte duran iki leke aynı boyaya aittir')],
 puf='Kromatografide lekenin yüksekliği, boyanın kâğıda tutunmasıyla ters ilişkilidir; aynı yükseklikteki lekeler aynı boyayı gösterir.')

# ============================================================ 05 · doymamış–doygun tanecik modeli (orta, öncüllü, şekil)
SAY={'K':(4,0),'L':(8,4),'M':(6,0)}
W5=2.7; xs5=[0,3.3,6.6]
g=''
for (nm,(n,kat)),x0 in zip(SAY.items(),xs5):
    g+=beher(x0,2.3,W5,2.6)
    for k in range(kat): g+=f'\\fill[black!70] ({x0+.35+k*.55:.2f},.1) rectangle ({x0+.65+k*.55:.2f},.4);'
    g+=''.join(disc(x,y,.11,'white') .replace('fill=white','fill=white') for x,y in rastgele(n,x0+.25,x0+W5-.25,.75,2.05,.42,seed=61+n))
    g+=f'\\node[font=\\small\\bfseries] at ({x0+W5/2},-.35) {{{nm}}};'
g+='\\draw[thin,fill=white] (0,-1.0) circle (.11); \\node[right,font=\\footnotesize] at (.2,-1.0) {: çözünmüş tanecik}; \\fill[black!70] (3.4,-1.12) rectangle (3.7,-.88); \\node[right,font=\\footnotesize] at (3.85,-1.0) {: dipteki katı (su molekülleri gösterilmedi)};'
SK5=tk(g)
assert SAY['K'][1]==0 and SAY['L'][1]>0 and SAY['M'][0]>SAY['K'][0]
d={'I':(True,'dipte çözünmemiş katı bulunması, çözeltinin o sıcaklıkta daha fazla katı çözemediğini, yani doygun olduğunu gösterir'),
   'II':(False,'M’de 6, K’de 4 çözünmüş tanecik vardır; su kütlesi eşit olduğundan M, K’dan daha derişiktir'),
   'III':(True,'K’de dipte katı yoktur; çözelti doymamıştır ve aynı sıcaklıkta daha fazla katı çözebilir')}
r=onc_t(d,4)
q('0005',ad=[A('Kapları incele','Çözünmüş tanecik sayısı ve dipteki katı her kapta ayrı sayılır.','K: 4 çözünmüş · L: 8 çözünmüş + dipte katı · M: 6 çözünmüş'),adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),A('Sonucu yaz','Doğru olan öncüller bir arada yazılır.',oy(d)+' · Sonuç: '+r['dogru'])],
 alt='Çözünürlük ve Doygunluk',z='orta',kaz='Tanecik modelinden doymamış ve doygun çözeltiyi ayırt eder, derişimleri karşılaştırır.',kalip='öncüllü',ne='K, L, M kaplarında çözünmüş tanecikler ve dipteki katı',
 metin='Aynı sıcaklıkta, özdeş üç kapta bulunan eşit kütlede suya aynı katıdan farklı miktarlarda eklenmiş ve karıştırılmıştır. Bir süre beklendikten sonra kaplardaki çözünmüş taneciklerin ve dipte kalan katının durumu şekildeki gibi modellenmiştir. Sıcaklık değişmemiş, su buharlaşmamıştır.\nI. L çözeltisi doygundur.\nII. M çözeltisi, K çözeltisinden daha seyreltiktir.\nIII. K çözeltisine aynı sıcaklıkta bir miktar daha aynı katı eklenirse katı çözünebilir.\nBuna göre hangileri doğrudur?',
 sekil=SK5,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan öncüller.',
 ip=['Dipte katı kalıp kalmadığına ve çözünmüş tanecik sayısına ayrı ayrı bak.'],
 bilgi=[B('Doymamış ve doygun çözelti','Belirli sıcaklıkta daha fazla madde çözemeyen çözelti doygundur; fazla katı dipte kalır. Daha fazla çözebilen çözelti doymamıştır. Su miktarı eşitse çözünmüş madde miktarı çok olan çözelti daha derişiktir')],
 puf='Dipte katı varsa çözelti doygundur; yoksa doymamış olabilir ve daha fazla katı çözer.')

# ============================================================ 06 · su–çözünen kütlesi grafiği (zor, grafik)
Sx6=.11; Sy6=.03
g=eksen(40,160,Sx6,Sy6,[10,20,30,40],[20,40,60,80,100,120,140,160],'Çözünen şeker kütlesi (g)','Su kütlesi (g)')
g+=f'\\draw[thick,vurgu] (0,0) -- ({40*Sx6},{160*Sy6}); \\draw[thick] (0,0) -- ({40*Sx6},{60*Sy6});'
g+=f'\\fill ({20*Sx6},{80*Sy6}) circle (.06); \\fill ({40*Sx6},{60*Sy6}) circle (.06);'
g+=f'\\node[right,font=\\small\\bfseries] at ({40*Sx6+.1},{160*Sy6}) {{K}}; \\node[right,font=\\small\\bfseries] at ({40*Sx6+.1},{60*Sy6}) {{L}};'
SK6=tk(g)
oK=Fr(20,100); oL=Fr(40,100)
assert Fr(20)/(20+80)==oK and Fr(40)/(40+60)==oL
mK,mL=300,200; sol=mK*oK+mL*oL; son=sol/oK; eklenen=son-(mK+mL)
assert sol==140 and son==700 and eklenen==200
ort=(oK+oL)/2; h1=((mK+mL)*ort)/oK-(mK+mL); assert ort==Fr(3,10) and h1==250
tersK,tersL=oL,oK; sol_t=mK*tersK+mL*tersL; h2=sol_t/oK-(mK+mL); assert sol_t==160 and h2==300
h3=son-mK; assert h3==400
q('0006',ad=[A('Derişimleri bul','Grafikteki bir noktadan çözelti kütlesi (şeker + su) ve kütlece derişim hesaplanır.','K: 20 g şeker + 80 g su → %20 · L: 40 g şeker + 60 g su → %40'),A('Şeker kütlelerini bul','Her çözeltideki şeker, çözelti kütlesi × derişimdir.','K: 300 × 0,2 = 60 g; L: 200 × 0,4 = 80 g'),A('Toplam şekeri hesapla','Karışıma yalnız su eklendiğinden şeker kütlesi sabit kalır.','60 + 80 = 140 g'),A('Hedef çözelti kütlesi','Şekerin %20 olduğu çözeltinin kütlesi bulunur.','140 ÷ 0,2 = 700 g'),A('Eklenecek suyu bul','Karışımın kütlesi 300 + 200 = 500 g’dır.','700 − 500 = 200 g')],
 alt='Derişim',z='zor',kaz='Su–çözünen kütlesi grafiğinden derişimleri bulup karışım ve seyreltme hesabı yapar.',kalip='grafik',ne='K ve L doğruları, 300 g K + 200 g L',
 metin='Şekildeki grafikte, kütlece derişimleri farklı K ve L şekerli su çözeltilerini hazırlamak için kullanılan şeker ve su kütleleri arasındaki ilişki doğrularla gösterilmiştir. Bir öğrenci, K çözeltisinden 300 g ile L çözeltisinden 200 g alıp temiz bir kapta karıştırıyor; karışımın üzerine, kütlece %20’lik şekerli su elde edene kadar saf su ekliyor.\nBuna göre eklenen saf su kaç gramdır?',
 sekil=SK6,dogru=200,yan=[(140,'Karışımdaki toplam şeker kütlesini (60 + 80 = 140 g) eklenecek su kütlesi sanmış.','dikkat'),(250,'Karışımın derişimini iki derişimin ortalaması (%30) almış: 500 × 0,3 = 150 g şeker, 150 ÷ 0,2 = 750 g çözelti, 750 − 500 = 250 g.','islem'),(400,'Hedef çözelti kütlesinden (700 g) yalnız K çözeltisinin kütlesini (300 g) çıkarmış; L’nin 200 g’ını unutmuş.','dikkat'),(700,'Yeni çözelti kütlesini (700 g) eklenecek su kütlesi sanmış.','dikkat')],
 istenen='Eklenen saf su kütlesi (g).',ip=['Önce grafikteki noktalardan her çözeltinin şeker kütlesinin toplam kütleye oranını bul.'],
 bilgi=[B('Kütlece derişim','Kütlece derişim = çözünen kütlesi ÷ çözelti kütlesi × 100’dür; çözelti kütlesi çözünen ile çözücünün toplamıdır. Su eklemekle çözünen kütlesi değişmez. Örnek: 10 g şeker + 40 g su içeren çözelti kütlece %20’liktir')],
 puf='Derişim işlemlerinde su eklenince değişmeyen çözünen kütlesini anahtar yap; çözelti kütlesi çözünen + su’dur.')

# ============================================================ 07 · ısıtma grafiği, saf madde–karışım (orta, grafik)
Sx7=.2; Sy7=.032
KRV={'K':[(0,20),(4,60),(8,60),(12,100)],'L':[(0,20),(4,60),(8,80),(10,100)],'M':[(0,20),(4,80),(8,80),(10,100)]}
g=''
for i,(nm,pt) in enumerate(KRV.items()):
    g+=f'\\begin{{scope}}[xshift={i*3.7}cm]'+eksen(12,100,Sx7,Sy7,[4,8,12],[20,40,60,80,100],'Zaman (dk)','°C')
    g+=f'\\node[font=\\small\\bfseries] at ({6*Sx7},{100*Sy7+1.0}) {{{nm}}};'
    g+='\\draw[thick,vurgu] '+' -- '.join(f'({x*Sx7:.2f},{y*Sy7:.2f})' for x,y in pt)+';\\end{scope}'
SK7=tk(g)
def plato(pt): return any(pt[i][1]==pt[i+1][1] for i in range(len(pt)-1))
assert plato(KRV['K']) and plato(KRV['M']) and not plato(KRV['L'])
assert [p for p in KRV['K'] if p[1]==60][0][1]==60 and KRV['M'][1][1]==80
dg=('L saf madde değildir.','L’nin sıcaklığı erime bölgesinde (4–8 dakika) artmaya devam etmiştir; saf madde erirken sıcaklık sabit kalır, karışım erirken artar')
yl=[('K saf madde, M karışımdır.','M erirken sıcaklığı 80 °C’de sabit kalmıştır; bu saf madde özelliğidir'),
    ('K ve M aynı saf maddedir.','K’nın erime sıcaklığı 60 °C, M’ninki 80 °C’dir; aynı saf maddenin erime noktası tek bir değerdir'),
    ('M’nin erime sıcaklığı 60 °C’dir.','M’nin sabit sıcaklık bölgesi 80 °C’dedir; 60 °C K’nın erime sıcaklığıdır'),
    ('L’nin sıcaklığı erime sırasında sabit kalmıştır.','L’nin sıcaklığı 4–8 dakika arasında 60 °C’den 80 °C’ye çıkmıştır; sabit kalanlar K ve M’dir')]
r=tek_t(dg,yl,0,True)
q('0007',ad=[A('Eğrileri incele','Erime sırasında sıcaklığın sabit kalıp kalmadığına bakılır.','K: 60 °C’de sabit · M: 80 °C’de sabit · L: sabit bölge yok'),A('Saf maddeyi belirle','Saf madde belirli sıcaklıkta erir ve erirken sıcaklık sabit kalır.','K ve M: saf madde özelliği'),A('L’yi yorumla','Erime sırasında sıcaklığı artan örnek karışımdır.','L: karışım'),A('Yargıları sına','Erime noktaları: K 60 °C, M 80 °C; K ile M aynı madde olamaz.','Doğru yargı: L saf madde değildir')],
 alt='Saf Madde ve Karışım',z='orta',kaz='Isıtma grafiğinde erime sırasındaki sıcaklık değişiminden saf madde ve karışımı ayırt eder.',kalip='grafik',ne='K, L ve M için sıcaklık–zaman grafikleri',
 metin='Aynı ısıtıcıyla, eşit hızda ısıtılan K, L ve M katı örneklerinin sıcaklıkları zamanla ölçülmüş ve sıcaklık–zaman grafikleri şekildeki gibi çizilmiştir. Örneklerin her biri ya tek bir saf maddedir ya da karışımdır; üçü de ısıtma sırasında erimiş, başka bir değişikliğe uğramamıştır.\nBuna göre aşağıdakilerden hangisi doğrudur?',
 sekil=SK7,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargı.',
 ip=['Erime sırasında grafiğin yatay kalıp kalmadığını her örnek için ayrı ayrı incele.'],
 bilgi=[B('Saf madde ve karışım','Saf maddenin erime noktası sabittir; erirken sıcaklık değişmez. Karışımların belirli bir erime noktası yoktur, erime boyunca sıcaklık değişir. Örnek: buz 0 °C’de erirken sıcaklık sabit kalır')],
 puf='Erirken sıcaklık sabitse saf madde, artıyorsa karışım düşün.')

# ============================================================ 08 · kristallendirme (zor, tablo)
SXY={20:(38,30),80:(40,180)}
xe,ye=40,138
assert xe<=SXY[80][0] and ye<=SXY[80][1]
cx=xe-SXY[20][0]; cy=ye-SXY[20][1]; toplam=cx+cy
assert (cx,cy,toplam)==(2,108,110)
assert SXY[20][0]+SXY[20][1]==68 and xe+ye==178 and (SXY[80][1]-SXY[20][1])+cx==152
SK8=tablo_svg(['Sıcaklık (°C)','X (g / 100 g su)','Y (g / 100 g su)'],[[str(t),str(a),str(b)] for t,(a,b) in SXY.items()])
q('0008',ad=[A('80 °C’de çözülenleri kontrol et','Eklenen miktarlar 80 °C’deki çözünürlükleri aşmamalıdır.','X: 40 ≤ 40 · Y: 138 ≤ 180 → tamamı çözünür'),A('X’in çökenini bul','20 °C’de 100 g suda en çok 38 g X çözünür.','40 − 38 = 2 g'),A('Y’nin çökenini bul','20 °C’de 100 g suda en çok 30 g Y çözünür.','138 − 30 = 108 g'),A('Toplamı yaz','Süzülen katı, çöken X ve Y’nin toplamıdır.','2 + 108 = 110 g')],
 alt='Çözünürlük',z='zor',kaz='İki katının çözünürlük tablosundan soğutmada çöken toplam kütleyi hesaplar.',kalip='tablo',ne='X ve Y çözünürlük tablosu, 100 g su',
 metin='X ve Y katılarının sudaki çözünürlükleri iki sıcaklık için tabloda verilmiştir. Bir öğrenci, 100 g su içeren bir kapta 80 °C’de 40 g X ile 138 g Y katısını tamamen çözmüş, ardından çözeltiyi su kaybı olmadan 20 °C’ye soğutup dipte biriken katıları süzmüştür. X ve Y birbirinin çözünürlüğünü etkilememektedir.\nBuna göre süzülen katıların toplam kütlesi kaç gramdır?',
 sekil=SK8,dogru=110,yan=[(68,'Soğutmadan sonra çözeltide kalan miktarları (38 + 30 = 68 g) çökmüş sanmış.','dikkat'),(108,'Yalnız Y’nin çöktüğünü düşünmüş; X’in de 2 g çöktüğünü hesaba katmamış.','dikkat'),(152,'Y’nin çözünürlük farkını (180 − 30 = 150) ve X’in 2 g’ını toplamış; çöken Y, eklenen miktara bağlıdır.','islem'),(178,'Çözünürlüğe bakmadan eklenen bütün katının (40 + 138 = 178 g) çöktüğünü sanmış.','bilgi')],
 istenen='Süzülen katıların toplam kütlesi (g).',ip=['Her katı için, eklenen miktardan 20 °C’de çözeltide kalabilecek miktarı çıkar.'],
 bilgi=[B('Soğutarak ayırma','Soğutmada çözeltide kalabilen madde azalır; fazlası dipte katı olarak birikir. Çöken miktar = çözünmüş miktar − düşük sıcaklıktaki çözünürlük (aynı su kütlesi için). Örnek: 100 g suda 50 g çözünmüşken çözünürlük 30 g’a inerse 20 g çöker')],
 puf='Çöken miktar, çözünmüş miktar ile düşük sıcaklıktaki çözünürlüğün farkıdır; her katı için ayrı hesapla.')

# ============================================================ 09 · çözeltiyi paylaştırma (kolay, öncüllü)
tum=400; ok_=Fr(20,100); sk=Fr(tum,2)*ok_; sL=sk; cL=200+100
assert sk==40 and sL/cL<ok_ and Fr(sL,cL)==Fr(2,15) and sk/Fr(tum,2)==ok_
d={'I':(False,'çözelti eşit parçalara ayrılınca homojen yapı korunur; her parçanın derişimi yine %20’dir'),
   'II':(True,'L’deki şeker 200 × 0,20 = 40 g’dır ve saf su eklemek şeker miktarını değiştirmez'),
   'III':(True,'şeker 40 g’da kalırken çözelti 300 g’a çıktığından derişim yaklaşık %13’e düşer')}
r=onc_t(d,4)
q('0009',ad=[A('Kaplardaki şekeri bul','400 g çözelti yarıya bölünüyor; her yarı aynı derişimde kalır.','Her kap: 200 g çözelti, %20 → 40 g şeker'),adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),A('Sonucu yaz','Doğru olan öncüller bir arada yazılır.',oy(d)+' · Sonuç: '+r['dogru'])],
 alt='Derişim',z='kolay',kaz='Çözeltiyi bölme ve su ekleme sonrasında çözünen kütlesi ile derişimin nasıl değiştiğini yorumlar.',kalip='öncüllü',ne='%20’lik 400 g çözelti, iki kap, 100 g su',
 metin='Kütlece %20’lik 400 g şekerli su çözeltisi, iki özdeş kaba 200’er g olacak biçimde paylaştırılıyor (K ve L kapları). Daha sonra L kabındaki çözeltiye 100 g saf su ekleniyor ve karıştırılıyor. Çözeltilerden su buharlaşması ya da şeker çökmesi olmamaktadır.\nI. K kabındaki çözeltinin kütlece derişimi %10’dur.\nII. L kabındaki çözeltide 40 g şeker bulunur.\nIII. L kabındaki çözeltinin kütlece derişimi %20’nin altındadır.\nBuna göre hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan öncüller.',
 ip=['Çözeltiyi bölmenin ve saf su eklemenin şeker kütlesini ve çözelti kütlesini nasıl etkilediğini ayrı ayrı düşün.'],
 bilgi=[B('Bölme ve seyreltme','Homojen çözeltiden alınan her parçanın derişimi aynıdır. Saf su eklenince çözünen kütlesi değişmez, çözelti kütlesi artar, derişim azalır. Örnek: kütlece %10’luk 100 g çözeltiye 100 g su eklenince çözünen 10 g kalır, derişim %5 olur')],
 puf='Bölünen çözeltinin derişimi değişmez; su eklenince çözünen kütlesi sabit, derişim azalır.')

# ============================================================ 10 · doygunluk grafiği (orta, grafik)
Sx10=.034; Sy10=.055
g=eksen(125,60,Sx10,Sy10,[25,50,75,100,125],[25,50],'Eklenen X kütlesi (g)','Çözünen X (g)')
g+=f'\\draw[thick,vurgu] (0,0) -- ({50*Sx10:.3f},{50*Sy10:.3f}) -- ({125*Sx10:.3f},{50*Sy10:.3f}); \\fill ({50*Sx10:.3f},{50*Sy10:.3f}) circle (.06);'
SK10=tk(g)
cozunen=lambda e:min(e,50); su10=200
assert cozunen(25)==25 and cozunen(50)==50
assert 50-cozunen(50)==0 and Fr(cozunen(80),su10+cozunen(80))==Fr(1,5) and Fr(50,200)==Fr(1,4) and 100-cozunen(100)==50 and cozunen(125)==50
dg=('100 g X eklendiğinde dipte 50 g X kalır.','grafik 50 g’dan sonra yataydır; 100 g’ın 50 g’ı çözünür, geri kalan 50 g dipte birikir')
yl=[('25 g X eklendiğinde çözelti doygundur.','25 g eklenince çözünen de 25 g’dır; eğri hâlâ yükselmektedir, çözelti doymamıştır'),
    ('50 g X eklendiğinde dipte çözünmemiş X kalır.','50 g X’in tamamı çözünür; doygunluk tam bu noktadadır ve dipte katı kalmaz'),
    ('80 g X eklendiğinde çözeltinin kütlece derişimi %25’tir.','çözelti 200 + 50 = 250 g, çözünen 50 g olduğundan derişim %20’dir; %25 değeri 50 g’ın 200 g suya bölünmesiyle bulunur'),
    ('125 g X eklendiğinde çözünen X kütlesi 125 g olur.','çözünen kütle 50 g’da sabitlenir; fazlası çözünmez')]
r=tek_t(dg,yl,3,True)
q('0010',ad=[A('Doygunluk noktasını oku','Grafik 50 g’a kadar doğrusal artar, sonra yataydır.','200 g suda en çok 50 g X çözünür'),A('Küçük miktarları incele','50 g’dan az X eklenince tamamı çözünür.','25 g → doymamış · 50 g → tam doygun, dipte katı yok'),A('Büyük miktarları incele','Doygunluktan sonra eklenen fazlası çözünmez.','100 g → 50 g dipte · 125 g → 75 g dipte'),A('Derişimi sına','Çözelti kütlesi su + çözünen X’tir.','80 g eklenince: 50 ÷ (200 + 50) = %20')],
 alt='Çözünürlük',z='orta',kaz='Çözünen kütle–eklenen kütle grafiğinden doygunluğu, dipteki katıyı ve derişimi yorumlar.',kalip='grafik',ne='200 g suya X ekleme grafiği',
 metin='25 °C’de 200 g saf suya, karıştırılarak azar azar X katısı ekleniyor. Eklenen toplam X kütlesine karşılık çözeltide çözünmüş hâlde bulunan X kütlesi ölçülüyor ve sonuçlar şekildeki grafikte gösteriliyor. İşlem boyunca su buharlaşmamaktadır.\nBuna göre aşağıdakilerden hangisi doğrudur?',
 sekil=SK10,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargı.',
 ip=['Grafiğin hangi noktadan sonra yatay olduğunu belirle; eklenenle çözünenin farkı dipteki katıdır.'],
 bilgi=[B('Doygunluk','Doygun çözeltide çözünen madde miktarı en büyük değerindedir; daha fazla katı eklenirse çözünmeden dipte kalır. Örnek: 100 g suda en çok 20 g çözünen madde için 30 g eklenirse 10 g dipte kalır')],
 puf='Yatay bölge doygunluğu gösterir; dipteki katı, eklenen ile çözünenin farkıdır.')

bitir(P,'karisimlaruc',UK)
