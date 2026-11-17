"""TYT Kimya · Asitler, Bazlar ve Tuzlar · 3. ek paket (asitbazuc): 10 soru, kardeş yok, ipucu 1.
Şekil koordinatları, tanecik sayıları, mol hesapları ve öncül doğrulukları Python'da hesaplanır; TikZ bu değerlerden üretilir.
Öncüllerin doğru/yanlış değeri tek yerde (d sözlüğü) tanımlanır; anahtar, adım ve çeldirici açıklamaları oradan üretilir."""
import sys,os,math,random,re,itertools
from fractions import Fraction as Fr
GD=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,GD)
import _hafif_kim2 as H
from _hafif_kim2 import *
from _hafif_kim import onc as _onc_eski, tek
KONU_='Asitler, Bazlar ve Tuzlar'; UK='kim|Asitler, Bazlar ve Tuzlar'
H.KONU=KONU_
P=Parti('asitbazuc',KONU_,UK,ders='TYT Kimya',idon='tytkim')
KY='ÖSYM 2018–2026 TYT Kimya (yalnız mantık) · MEB 10. sınıf Asitler, Bazlar ve Tuzlar'
MAP={}
for _n,_t in [(('01','08'),('indikator','İndikatörler ve renk değişimleri')),(('02',),('metal','Asit ve bazların metallerle tepkimesi')),
              (('04',),('notr','Nötralleşme: tanecik modeli')),(('03',),('tuz','Tuz oluşumu')),(('06',),('ph','pH grafiği ve nötralleşme')),(('10',),('sinif','Asit, baz ve tuz çözeltilerini ayırt etme')),
              (('05','07','09'),('gunluk','Günlük hayatta asit–baz ve güvenlik'))]:
    for _x in _n: MAP[_x]=_t
assert len(MAP)==10
def kartla(n,alt,fikir,tuzak,z,kalip,adim):
    a,b=MAP[n]; kart(f'K-KMAB3-{n}',alt,fikir,tuzak,z,kalip,adim,f'km-ab3-{a}',b,KY)
def q(no,ad,**k):
    assert len(k['ip'])==1
    k['tipId']='km-ab3-'+MAP[no[-2:]][0]; k['tip']=MAP[no[-2:]][1]
    ne=k.pop('ne'); k['kart']=f"K-KMAB3-{no[-2:]} ({MAP[no[-2:]][1].lower()}) · {ne}"
    mk(P,no,ad=ad,adim=len(ad),**k)
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
ARR='-{Stealth[length=2mm,width=1.8mm]}'
def tk(g): return tikz_svg(HEAD+g+TAIL)

# ---------- öncüllü ve tekli yardımcılar ----------
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
def sonuc(d,r): return A('Sonucu yaz','Doğru olan öncüller bir arada yazılır.',oy(d)+' · Sonuç: '+r['dogru'])

# ---------- tanecik ve çizim yardımcıları ----------
def uzak(p,L,m): return all((p[0]-a)**2+(p[1]-b)**2>=m*m for a,b in L)
def rastgele(n,x1,x2,y1,y2,m,seed):
    rng=random.Random(seed)
    for deneme in range(3000):
        L=[]
        for _ in range(6000):
            p=(rng.uniform(x1,x2),rng.uniform(y1,y2))
            if uzak(p,L,m): L.append(p)
            if len(L)==n: return L
    raise RuntimeError('yerlesmedi')
ION={'H':('H$^+$',True),'Cl':('Cl$^-$',False),'Na':('Na$^+$',True),'OH':('OH$^-$',False),'K':('K$^+$',True)}
def iyon(x,y,k):
    t,kat=ION[k]
    st='thick,vurgu' if kat else 'thin'
    return f'\\draw[{st}] ({x:.2f},{y:.2f}) circle (.33); \\node[font=\\footnotesize] at ({x:.2f},{y:.2f}) {{{t}}};'
def beher(x0,W,Hh,lv):
    return f'\\draw[thick] ({x0},{Hh}) -- ({x0},0) -- ({x0+W},0) -- ({x0+W},{Hh}); \\draw[vurgu,thick] ({x0+.03},{lv}) -- ({x0+W-.03},{lv});'
def iyonlar(x0,W,lv,sayilar,seed):
    toplam=sum(sayilar.values()); pts=rastgele(toplam,x0+.42,x0+W-.42,.42,lv-.42,.78,seed)
    order=[k for k,n in sayilar.items() for _ in range(n)]
    return ''.join(iyon(p[0],p[1],k) for p,k in zip(pts,order))
def tup(x,metal,gaz,top=2.4,lvl=1.75):
    l,r=x-.36,x+.36
    s=f'\\fill[vurgu!15] ({l},{lvl}) -- ({l},.36) arc (180:360:.36) -- ({r},{lvl}) -- cycle;'
    s+=f'\\draw[thick] ({l},{top}) -- ({l},.36) arc (180:360:.36) -- ({r},{top});'
    s+=f'\\draw[thin] ({l},{lvl}) -- ({r},{lvl});'
    s+=f'\\fill[gray!60] ({x-.21},.1) rectangle ({x+.21},.46);'
    if gaz:
        for bx,by in [(-.1,.8),(.13,1.05),(-.12,1.3),(.09,1.52),(-.02,1.68)]:
            s+=f'\\draw[thin,fill=white] ({x+bx:.2f},{by:.2f}) circle (.075);'
    if metal: s+=f'\\node[below,font=\\small\\bfseries] at ({x},-.02) {{{metal}}};'
    return s
def eksen(xm,ym,xl,yl,sx,sy,xt=(),yt=()):
    s=f'\\draw[thick,{ARR}] (0,0) -- ({xm*sx+.3:.2f},0);\\draw[thick,{ARR}] (0,0) -- (0,{ym*sy+.3:.2f});'
    for t,lab in xt: s+=f'\\draw ({t*sx:.2f},0) -- ({t*sx:.2f},-.08) node[below,font=\\small] {{{lab}}};'
    for t in yt: s+=f'\\draw (0,{t*sy:.2f}) -- (-.08,{t*sy:.2f}) node[left,font=\\small] {{{t}}};'
    s+=f'\\node[font=\\small,anchor=north west] at ({xm*sx*.35:.2f},-.55) {{{xl}}};\\node[font=\\small,anchor=south] at (0,{ym*sy+.35:.2f}) {{{yl}}};'
    return s

# ============================================================ KARTLAR
kartla('01','Evrensel indikatör renk kartı','Evrensel indikatörün rengi pH aralığını verir; pH < 7 asidik, 7 nötr, > 7 bazik; kırmızıya yakın renk küçük pH’ı, mora yakın renk büyük pH’ı gösterir.','Renk adından pH’ı tahmin edip sarıyı bazik, maviyi asidik saymak.','kolay','tablo',3)
kartla('02','Gaz toplama düzeneği','Aktif metal asitle H₂ çıkarır; H₂ suda çok az çözündüğünden suyun yerini değiştirerek toplanır; soy metal asitle tepkime vermez.','Her metalin asitten gaz çıkardığını sanmak; hafif gazın açık kapta toplanabileceğini düşünmek.','orta','şekilli',3)
kartla('03','Tuz oluşturan tepkimeler','Asit–baz (nötralleşme), asit–aktif metal, asit–karbonat tepkimeleri tuz verir; asidik oksit + su asit verir, tuz vermez.','Her ürünü tuz sanmak; NH₃ + HCl tepkimesinin tuz vermediğini düşünmek.','kolay','düz',3)
kartla('04','Karışım sonrası iyon sayımı','Önce H⁺ ve OH⁻ eşit sayıda su olur; artan iyon ve seyirci iyonlar kapta kalır; su iyon sayılmaz.','Suyu iyon saymak; seyirci iyonları atlamak; artan iyonu unutmak.','orta','şekilli',4)
kartla('05','Toprak pH’ı ve kireçleme','Bitkilerin uygun pH aralıkları vardır; bazik kireç toprağın asitliğini azaltarak pH’ı yükseltir.','Kirecin toprağı daha asidik yaptığını sanmak; aralık sınırlarını yanlış okumak.','orta','öncüllü',3)
kartla('06','Nötralleşme pH grafiği','Asit çözeltisine baz eklenirken pH yükselir; eşdeğerlik noktasında ortam nötrdür ve yalnız tuzun iyonları kalır; sonrasında artan baz ortamı bazik yapar.','Nötr noktada çözeltide iyon kalmadığını sanmak; baz eklemeye devam edince tuzun artacağını düşünmek.','zor','grafik',4)
kartla('07','Antasit etkisi','Antasit bazik maddeler içerir; mide asidini nötrleştirir ve pH’ı yükseltir; son pH ortamın türünü ve indikatör rengini belirler.','Antasit ekleyince pH’ın azalacağını sanmak; pH 7’yi geçen ortamı nötr saymak.','orta','grafik',3)
kartla('08','İki indikatörlü sınıflama','Fenolftalein bazda pembe, asit ve nötrde renksiz; metil oranj asitte kırmızı, nötr ve bazda sarıdır; iki gözlem birlikte yorumlanır.','Tek indikatörün sonucunu yeterli sanmak; bazın mavi turnusolu etkileyeceğini düşünmek.','orta','tablo',3)
kartla('09','Laboratuvar güvenlik kuralları','Asit suya yavaş yavaş eklenir; maddeler tadılmaz; cilde sıçrayan madde bol suyla yıkanır, ters etkili madde dökülmez.','Nötralleşme için cilde bazik çözelti dökmek; maddelerin tadına bakılabileceğini sanmak.','kolay','öncüllü',3)
kartla('10','Asit, baz ve tuz çözeltisini ayırt etme','Turnusol, Mg ile gaz çıkışı ve iletkenlik gözlemleri birlikte yorumlanır: asit gaz verir ve turnusolu kırmızıya çevirir, baz maviye çevirir, tuz çözeltisi nötrdür ve iletir, şekerli su iletmez.','Nötr ve iletken çözeltiyi saf su ya da şekerli su sanmak.','orta','tablo',3)

# ============================================================ 01 · evrensel indikatör (kolay, öncüllü, tablo)
GOZ=[('K','Sarı'),('L','Mavi'),('M','Yeşil'),('N','Kırmızı'),('P','Mor')]
PH={'Kırmızı':(1,3),'Turuncu':(4,4),'Sarı':(5,6),'Yeşil':(7,7),'Mavi':(8,10),'Mor':(11,14)}
orta_ph={k:Fr(PH[r][0]+PH[r][1],2) for k,r in GOZ}
assert PH['Sarı'][1]<7 and PH['Mavi'][0]>7 and PH['Yeşil']==(7,7) and PH['Kırmızı'][1]<PH['Mor'][0]
SK1=tablo_svg(['Çözelti','Evrensel indikatörde gözlenen renk'],[[a,b] for a,b in GOZ])
d={'I':(True,'sarı renk pH 5–6’ya (asidik), mavi renk pH 8–10’a (bazik) karşılık gelir'),
   'II':(True,'yeşil renk pH 7’yi gösterir; nötr çözelti turnusol kâğıtlarının rengini değiştirmez'),
   'III':(False,'kırmızı renk pH 1–3, mor renk pH 11–14 aralığındadır; N’nin pH değeri P’ninkinden küçüktür')}
r=onc_t(d,1)
q('0001',ad=[A('Renkleri pH’a çevir','Kart: kırmızı 1–3, turuncu 4, sarı 5–6, yeşil 7, mavi 8–10, mor 11–14.','K: 5–6 · L: 8–10 · M: 7 · N: 1–3 · P: 11–14'),adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),A('Sonucu yaz','Doğru olan öncüller bir arada yazılır.',oy(d)+' · Sonuç: '+r['dogru'])],
 alt='İndikatörler',z='kolay',kaz='Evrensel indikatör renklerinden çözeltilerin asidik, bazik veya nötr olduğunu belirler.',kalip='öncüllü',ne='K, L, M, N, P renk tablosu',
 metin='Evrensel indikatör, çözeltinin pH değerine göre renk değiştirir: pH 1–3’te kırmızı, 4’te turuncu, 5–6’da sarı, 7’de yeşil, 8–10’da mavi, 11–14’te mor renk verir. Bir öğrenci, beş farklı çözeltiye bu indikatörden birkaç damla damlatmış ve oluşan renkleri tablodaki gibi kaydetmiştir.\nI. K çözeltisi asidiktir, L çözeltisi baziktir.\nII. M çözeltisi mavi turnusol kâğıdının rengini değiştirmez.\nIII. N çözeltisinin pH değeri P çözeltisinin pH değerinden büyüktür.\nBuna göre hangileri doğrudur?',
 sekil=SK1,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan öncüller.',
 ip=['Her rengin hangi pH aralığına karşılık geldiğini bul; 7’nin altı ve üstü ortamın türünü verir.'],
 bilgi=[B('pH ve ortam','pH < 7 olan çözelti asidik, pH = 7 nötr, pH > 7 baziktir. pH küçüldükçe asitlik, büyüdükçe baziklik artar. Örnek: pH 2 olan çözelti pH 5 olandan daha asidiktir')],
 puf='Renkten pH aralığını bul; 7’nin altı asidik, üstü bazik, tam 7 nötrdür.')

# ============================================================ 02 · gaz toplama düzeneği (orta, öncüllü, şekil)
g='\\draw[thick] (1.0,3.4) -- (1.0,2.5) -- (.1,.3) -- (2.5,.3) -- (1.6,2.5) -- (1.6,3.4);'
g+='\\fill[vurgu!15] (.12,.32) -- (2.48,.32) -- (2.05,1.4) -- (.55,1.4) -- cycle; \\draw (.55,1.4) -- (2.05,1.4);'
for x0 in (.6,1.15,1.7): g+=f'\\fill[black!45] ({x0},.34) rectangle ({x0+.4},.5);'
for x,y in [(.8,.9),(1.4,1.1),(1.75,.8),(1.1,1.25)]: g+=f'\\draw[thin,fill=white] ({x},{y}) circle (.06);'
g+='\\draw[thick,fill=gray!30] (.95,3.4) rectangle (1.65,3.75);'
g+='\\draw[thick] (2.4,2.4) -- (2.4,0) -- (7.4,0) -- (7.4,2.4); \\fill[vurgu!15] (2.42,.02) rectangle (7.38,1.8); \\draw (2.4,1.8) -- (7.4,1.8);'
g+='\\draw[line width=1.3pt] (1.3,1.9) -- (1.3,4.1) -- (3.0,4.1) -- (3.0,.45) -- (5.6,.45) -- (5.6,.95);'
g+='\\fill[vurgu!15] (5.0,.7) rectangle (6.2,2.9); \\draw[thick] (5.0,.7) -- (5.0,3.4) -- (6.2,3.4) -- (6.2,.7); \\draw (5.0,2.9) -- (6.2,2.9);'
for x,y in [(5.6,1.15),(5.5,1.55),(5.7,2.0)]: g+=f'\\draw[thin,fill=white] ({x},{y}) circle (.07);'
g+='\\node[font=\\footnotesize] at (6.9,1.0) {su}; \\node[below,font=\\footnotesize,align=center] at (1.3,.2) {Zn parçaları ve\\\\seyreltik HCl çözeltisi};'
SK2=tk(g)
d={'I':(True,'çinko aktif bir metaldir, asitten H₂ çıkarır ve H₂ yanan çırayla hafif patlama sesiyle yanar'),
   'II':(False,'H₂ havadan hafif olduğundan açık kapta yukarı kaçar; bu yüzden suyun yerini değiştirerek ya da ağzı aşağı tutularak toplanır'),
   'III':(True,'bakır soy bir metaldir ve seyreltik HCl ile tepkime vermez')}
r=onc_t(d,3)
q('0002',ad=[A('Düzeneği ve gözlemi yorumla','Metal parçaları asitle gaz verir; gaz yanan çırayla hafif patlama sesi çıkarır.','Gaz: H₂ (Zn + 2HCl → ZnCl₂ + H₂)'),adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),A('Sonucu yaz','Doğru olan öncüller bir arada yazılır.',oy(d)+' · Sonuç: '+r['dogru'])],
 alt='Metal–Asit Tepkimesi',z='orta',kaz='Metal–asit tepkimesinde gaz toplama düzeneğini ve gazın özelliklerini yorumlar.',kalip='öncüllü',ne='çinko–HCl, suyun yerini değiştirerek gaz toplama',
 metin='Bir öğrenci, çinko (Zn) parçalarını seyreltik HCl çözeltisi içeren erlene atıyor ve oluşan gazı şekildeki düzenekle su dolu bir tüpte topluyor. Tüp gazla dolunca ağzını su içinde kapatıp çıkarıyor; ağzı aşağıya bakacak biçimde tutarak yanan bir çıra yaklaştırıyor ve gazın hafif bir patlama sesiyle yandığını gözlüyor.\nI. Toplanan gaz H₂’dir.\nII. Gaz havadan hafif olduğu için ağzı yukarı bakan açık bir kapta da biriktirilebilirdi.\nIII. Çinko yerine bakır parçaları kullanılsaydı aynı gaz çıkışı gözlenmezdi.\nBuna göre hangileri doğrudur?',
 sekil=SK2,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan öncüller.',
 ip=['Aktif ve soy metallerin seyreltik asitle davranışını, ayrıca hafif bir gazın açık kapta nasıl davrandığını düşün.'],
 bilgi=[B('Metal ve asit','Mg, Zn, Al gibi aktif metaller asitle tuz ve H₂ gazı oluşturur; Cu, Ag, Au gibi soy metaller seyreltik asitlerle tepkime vermez. H₂ yanıcıdır ve yanan çırayla hafif patlama sesi çıkarır. Örnek: Mg + 2HCl → MgCl₂ + H₂')],
 puf='Aktif metal + asit → tuz + H₂; soy metal tepkime vermez; H₂ suyun yerini değiştirerek toplanır.')

# ============================================================ 03 · tuz oluşmaz (kolay, düz, olumsuz kök)
EQ=[('Zn + H₂SO₄ → ZnSO₄ + H₂','ZnSO₄ tuzdur; aktif metal ile asit tepkimesinde tuz ve H₂ oluşur.'),
    ('Mg(OH)₂ + 2HNO₃ → Mg(NO₃)₂ + 2H₂O','Mg(NO₃)₂ tuzdur; nötralleşmede tuz ve su oluşur.'),
    ('CaCO₃ + 2HCl → CaCl₂ + H₂O + CO₂','CaCl₂ tuzdur; karbonat asitle tuz, su ve CO₂ verir.'),
    ('NH₃ + HCl → NH₄Cl','NH₄Cl, amonyum ve klorür iyonlarından oluşan tuzdur; OH⁻ içermeyen NH₃ de asitle tuz verir.'),
    ('CO₂ + H₂O → H₂CO₃','')]
dogru3=EQ[4][0]
q('0003',ad=[A('Tuzu tanımla','Tuz, bazdan ya da metalden gelen pozitif iyon ile asitten gelen negatif iyonun oluşturduğu iyonik bileşiktir.','Katyon (metal/NH₄⁺) + anyon (asit kökü)'),A('Ürünleri tek tek incele','Her tepkimenin ürünlerinde pozitif ve negatif iyondan oluşan bileşik aranır.','ZnSO₄ · Mg(NO₃)₂ · CaCl₂ · NH₄Cl tuz'),A('Asit ürünü ayır','H₂CO₃ bir asittir; metal ya da NH₄⁺ içermez.','CO₂ + H₂O → H₂CO₃: tuz yok'),A('Sonucu yaz','Ürünü tuz olmayan tepkime aranan cevaptır.','Tuz oluşmayan tepkime: CO₂ + H₂O → H₂CO₃')],
 alt='Tuz Oluşumu',z='kolay',kaz='Tepkime denklemlerinin ürünlerinde tuz olup olmadığını belirler.',kalip='düz',ne='beş tepkime denklemi',
 metin='Bir kimya öğretmeni, tuzun tanımını (bir bazdan ya da metalden gelen pozitif iyon ile bir asitten gelen negatif iyonun oluşturduğu iyonik bileşik) verip öğrencilerinden beş tepkimeyi incelemelerini istiyor. Denklemlerde sol taraf girenleri, sağ taraf ürünleri göstermektedir.\nBuna göre aşağıdaki tepkimelerin hangisinde ürünler arasında tuz bulunmaz?',
 dogru=dogru3,sira=[e[0] for e in EQ],yan=[(e[0],'Bu tepkimede tuz oluşmadığını sanmış. '+e[1],'bilgi') for e in EQ[:4]],
 istenen='Tuz oluşmayan tepkime.',ip=['Her ürünün metal ya da NH₄⁺ gibi pozitif iyon ile asit kökünden oluşup oluşmadığına bak.'],
 bilgi=[B('Tuz oluşumu','Nötralleşme, asit–aktif metal ve asit–karbonat tepkimeleri tuz oluşturur. Tuz, pozitif iyon (metal ya da NH₄⁺) ile asit kökü anyonundan oluşan iyonik bileşiktir. Örnek: NaOH + HBr → NaBr + H₂O tepkimesinde NaBr tuzdur')],
 puf='Tuz, metal (ya da NH₄⁺) ile asit kökünden oluşan iyonik bileşiktir; asit tek başına tuz değildir.')

# ============================================================ 04 · H₂SO₄ + KOH tanecik modeli (orta, şekil)
random.seed(7)
def iyon2(x,y,t,r,kat): return f'\\draw[{"thick,vurgu" if kat else "thin"}] ({x:.2f},{y:.2f}) circle ({r}); \\node[font=\\scriptsize] at ({x:.2f},{y:.2f}) {{{t}}};'
TIP={'H':('H$^+$',.3,True),'SO4':('SO$_4^{2-}$',.42,False),'K':('K$^+$',.3,True),'OH':('OH$^-$',.33,False)}
def doldur(x0,W,sayilar,kol,satir,dx,dy,y0,seed):
    liste=[k for k,n in sayilar.items() for _ in range(n)]; assert len(liste)==kol*satir
    random.Random(seed).shuffle(liste); s=''; i=0
    for r_ in range(satir):
        for c in range(kol):
            t,rad,kat=TIP[liste[i]]; i+=1
            s+=iyon2(x0+W/2+(c-(kol-1)/2)*dx,y0+r_*dy,t,rad,kat)
    return s
NA={'H':6,'SO4':3}; NB={'K':8,'OH':8}
W4=4.2
g='\\draw[thick] (0,3.9) -- (0,0) -- (4.2,0) -- (4.2,3.9); \\draw[thick] (5.2,3.9) -- (5.2,0) -- (9.4,0) -- (9.4,3.9);'
g+=doldur(0,W4,NA,3,3,1.15,1.15,.75,3)+doldur(5.2,W4,NB,4,4,.95,.9,.65,4)
g+='\\node[font=\\Large] at (4.7,1.9) {+}; \\node[below] at (2.1,-.1) {\\ce{H2SO4} çözeltisi}; \\node[below] at (7.3,-.1) {KOH çözeltisi};'
SK4=tk(g)
nH,nS,nK,nO=NA['H'],NA['SO4'],NB['K'],NB['OH']
assert nH==2*nS and nK==nO
su=min(nH,nO); kalanOH=nO-su; kalanH=nH-su
assert (su,kalanOH,kalanH)==(6,2,0)
toplam=nK+nS+kalanOH+kalanH; assert toplam==13
hata={5:kalanOH+nS,11:nK+nS,19:toplam+su,25:nH+nS+nK+nO}
assert hata=={5:5,11:11,19:19,25:25}
q('0004',ad=[A('İyonları say','Şekildeki modelden her çözeltideki iyonlar sayılır.','H₂SO₄: 6 H⁺, 3 SO₄²⁻ · KOH: 8 K⁺, 8 OH⁻'),A('Su oluşumunu bul','H⁺ ve OH⁻ bire bir birleşir; az olan iyon tükenir.','6 H⁺ + 6 OH⁻ → 6 H₂O'),A('Kalan iyonları yaz','Artan OH⁻ ve seyirci iyonlar kapta kalır; su iyon sayılmaz.','OH⁻: 2 · K⁺: 8 · SO₄²⁻: 3'),A('Toplamı bul','Kalan iyonların sayısı toplanır.','2 + 8 + 3 = 13')],
 alt='Nötralleşme',z='orta',kaz='Nötralleşme tanecik modelinde tepkime sonrası kalan iyonları sayar.',kalip='şekilli',ne='6 H⁺, 3 SO₄²⁻ ve 8 K⁺, 8 OH⁻ içeren iki çözelti',
 metin='Bir öğrenci, H₂SO₄ ve KOH çözeltilerindeki iyonları şekildeki gibi modelliyor (su molekülleri gösterilmemiştir). İki çözeltiyi bir kapta karıştırıyor ve tepkime tamamlanıyor. H⁺ ve OH⁻ iyonları birleşerek su oluşturmaktadır; diğer iyonlar çözeltide serbest kalmakta, katı tuz çökmemektedir.\nBuna göre tepkime sonunda kapta bulunan toplam iyon sayısı kaçtır?',
 sekil=SK4,dogru=13,yan=[(5,'Yalnız artan OH⁻ ile SO₄²⁻ iyonlarını saymış (2 + 3); K⁺ iyonlarını tepkimeye girmiş sanıp dışarıda bırakmış.','dikkat'),(11,'K⁺ (8) ve SO₄²⁻ (3) iyonlarını saymış; artan 2 OH⁻ iyonunu unutmuş.','dikkat'),(19,'Oluşan 6 su molekülünü de iyon sayıp toplama katmış (13 + 6).','bilgi'),(25,'Tepkimeyi hiç dikkate almamış; karıştırmadan önceki bütün iyonları (9 + 16) saymış.','bilgi')],
 istenen='Tepkime sonundaki toplam iyon sayısı.',ip=['Hangi iyonun sayıca az olduğunu bul; su oluşturan iyonlar kaptan iyon olarak çıkar.'],
 bilgi=[B('Nötralleşme ve iyonlar','Asitten gelen H⁺ ile bazdan gelen OH⁻ bire bir birleşip su oluşturur. Tepkimeye girmeyen seyirci iyonlar ve artan iyon çözeltide kalır; su iyon değildir. Örnek: 5 H⁺ ile 3 OH⁻ karışırsa 3 su oluşur, 2 H⁺ artar')],
 puf='Önce H⁺ ile OH⁻ eşleştirilir; artan iyon ve seyirci iyonlar sayılır, suyu sayma.')

# ============================================================ 05 · toprak pH’ı ve kireçleme (orta, öncüllü, şekil)
BAR={'K':(4.5,5.5),'L':(6.0,7.0),'M':(7.0,8.0)}
X5=lambda p:(p-4)*1.4
g=''
for p in [4+.5*i for i in range(11)]:
    g+=f'\\draw[black!{12 if abs(p-round(p))>0 else 22}] ({X5(p):.2f},0) -- ({X5(p):.2f},3.1);'
g+=f'\\draw[thick,{ARR}] (0,0) -- (7.4,0);'
for p in range(4,10): g+=f'\\draw[thick] ({X5(p):.2f},0) -- ({X5(p):.2f},-.08) node[below,font=\\small] {{{p}}};'
g+='\\node[font=\\small] at (3.5,-.75) {Toprak pH değeri};'
for (nm,(a,b)),y in zip(BAR.items(),[2.4,1.55,.7]):
    g+=f'\\draw[thick,fill=vurgu!30] ({X5(a):.2f},{y-.22}) rectangle ({X5(b):.2f},{y+.22}); \\node[left,font=\\small\\bfseries] at (-.15,{y}) {{{nm} bitkisi}};'
SK5=tk(g)
ilk,son=Fr(5),Fr(13,2)
aralik=lambda n:BAR[n][0]<=son<=BAR[n][1]
assert BAR['K'][0]<=ilk<=BAR['K'][1] and not (BAR['L'][0]<=ilk<=BAR['L'][1]) and BAR['L'][0]<=son<=BAR['L'][1] and not (BAR['M'][0]<=son<=BAR['M'][1]) and son>ilk
d={'I':(False,'başlangıçta pH 5,0’dır; L’nin aralığı 6,0–7,0 olduğundan toprak L için uygun değildir (K için uygundur)'),
   'II':(True,'6,5 değeri, L’nin uygun aralığı olan 6,0–7,0 içindedir'),
   'III':(True,'toprağın pH değeri 5,0’dan 6,5’e yükselmiştir; pH arttıkça asitlik azalır')}
r=onc_t(d,4)
q('0005',ad=[A('Aralıkları oku','Her bitkinin uygun pH aralığı şekilden okunur.','K: 4,5–5,5 · L: 6,0–7,0 · M: 7,0–8,0'),adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),A('Sonucu yaz','Doğru olan öncüller bir arada yazılır.',oy(d)+' · Sonuç: '+r['dogru'])],
 alt='Günlük Hayatta pH',z='orta',kaz='Toprak pH’ını bitkilerin uygun pH aralıklarıyla karşılaştırıp kireçlemenin etkisini yorumlar.',kalip='öncüllü',ne='K, L, M bitkilerinin pH aralıkları; toprak pH 5,0 → 6,5',
 metin='Bir çiftçi, tarlasının toprağının pH değerini 5,0 olarak ölçmüştür. Şekilde K, L ve M bitkilerinin sağlıklı geliştiği toprak pH aralıkları verilmiştir. Çiftçi, toprağa sönmüş kireç [Ca(OH)₂] ekleyerek pH değerini 6,5’e çıkarmıştır.\nI. Başlangıçta toprak, L bitkisinin yetişmesi için uygundur.\nII. Kireç eklendikten sonra toprak, L bitkisinin yetişmesi için uygundur.\nIII. Kireç, toprağın asitliğini azaltmıştır.\nBuna göre hangileri doğrudur?',
 sekil=SK5,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan öncüller.',
 ip=['Toprağın pH değerini aralıklarla karşılaştır; pH’ın artmasının ortamın asitliğine etkisini düşün.'],
 bilgi=[B('pH ve asitlik','pH değeri küçüldükçe ortamın asitliği artar, büyüdükçe azalır. Bazik bir madde katılınca asidik ortamın pH değeri yükselir. Örnek: pH 4 olan çözeltiye bazik madde katılıp pH 6’ya çıkarılırsa çözelti hâlâ asidiktir ama daha az asidiktir')],
 puf='Bazik madde asidik ortamın pH’ını yükseltir; aralıklara bak, sınırdaki değerleri ayrıca kontrol et.')

# ============================================================ 06 · nötralleşme pH grafiği (zor, grafik)
Sx6=.09; Sy6=.27
pts=[(0,1),(10,3),(17,5),(19,6),(20,7),(21,9),(24,10.5),(30,11),(40,12)]
g=''.join(f'\\draw[black!15] (0,{v*Sy6:.2f}) -- ({40*Sx6:.2f},{v*Sy6:.2f});' for v in (1,3,5,7,9,11))+''.join(f'\\draw[black!15] ({v*Sx6:.2f},0) -- ({v*Sx6:.2f},{13*Sy6:.2f});' for v in (10,20,30,40))
g+=eksen(40,13,'Eklenen NaOH çözeltisi (mL)','pH',Sx6,Sy6,[(10,'10'),(20,'20'),(30,'30'),(40,'40')],[1,3,5,7,9,11,13])
g+='\\draw[thick,vurgu] plot[smooth,tension=.5] coordinates {'+' '.join(f'({a_*Sx6:.2f},{b_*Sy6:.2f})' for a_,b_ in pts)+'};'
for nm,(a_,b_) in {'P':(10,3),'R':(20,7),'S':(30,11)}.items():
    g+=f'\\fill ({a_*Sx6:.2f},{b_*Sy6:.2f}) circle (.07); \\node[font=\\small\\bfseries,anchor=north west] at ({a_*Sx6+.08:.2f},{b_*Sy6-.05:.2f}) {{{nm}}};'
SK6=tk(g)
PHN={'P':3,'R':7,'S':11}
assert PHN['P']<7 and PHN['R']==7 and PHN['S']>7
dg=('R noktasında çözeltide yalnız Na⁺ ve Cl⁻ iyonları vardır ve fenolftalein renksizdir.','R’de pH 7’dir: HCl ile NaOH tam nötrleşmiş, çözeltide tuzun iyonları (Na⁺, Cl⁻) kalmıştır; nötr ortamda fenolftalein renksizdir')
yl=[('P noktasında çözeltide H⁺ iyonu bulunmaz.','P’de pH 3’tür; NaOH henüz bütün HCl’yi nötrleştirmemiş, çözeltide artan H⁺ iyonları vardır'),
    ('R noktasında çözelti hiç iyon içermez.','nötr noktada da çözeltide tuzun Na⁺ ve Cl⁻ iyonları bulunur; çözelti elektriği iletir'),
    ('S noktasında metil oranj kırmızı renktedir.','S’de pH 11’dir; çözelti baziktir ve metil oranj bazik ortamda sarıdır'),
    ('R noktasından S noktasına giderken çözeltideki tuz miktarı artmaya devam eder.','R’de HCl tükenmiştir; sonra eklenen NaOH tuz oluşturmaz, çözeltide artan OH⁻ olarak kalır')]
r=tek_t(dg,yl,3,True)
q('0006',ad=[A('Grafiği oku','P, R ve S noktalarının pH değerleri okunur.','P: 3 · R: 7 · S: 11'),A('Ortamları belirle','pH < 7 asidik, 7 nötr, > 7 bazik.','P: asidik · R: nötr · S: bazik'),A('İyonları yorumla','Nötr noktada HCl tükenmiştir; bazik bölgede artan OH⁻ vardır.','P: H⁺ fazla · R: yalnız Na⁺, Cl⁻ · S: OH⁻ fazla'),A('Yargıları sına','İyon ve indikatör rengi birlikte değerlendirilir.','R: Na⁺, Cl⁻ + fenolftalein renksiz')],
 alt='pH ve Nötralleşme',z='zor',kaz='Nötralleşme pH grafiğinden ortamın türünü, çözeltideki iyonları ve indikatör renklerini yorumlar.',kalip='grafik',ne='HCl çözeltisine NaOH ekleme grafiği, P, R, S noktaları',
 metin='Bir öğrenci, HCl çözeltisine aynı sıcaklıkta NaOH çözeltisini damla damla ekliyor ve çözeltinin pH değerini ölçüyor. Sonuçlar şekildeki grafikte verilmiştir; P, R ve S ölçümün farklı anlarını göstermektedir. Tuz çökmemekte ve hacim değişimi ihmal edilmektedir.\nBuna göre aşağıdakilerden hangisi doğrudur?',
 sekil=SK6,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargı.',
 ip=['Her noktanın pH değerine bakıp ortamın türünü belirle; sonra hangi iyonun fazla kaldığını düşün.'],
 bilgi=[B('Nötralleşme ve pH','Asite baz eklendikçe H⁺ iyonları OH⁻ ile su olur ve pH yükselir. Tam nötrleşmede pH 7’dir ve çözeltide yalnız tuzun iyonları kalır. Daha fazla baz eklenirse artan OH⁻ çözeltiyi bazik yapar')],
 puf='pH 7 noktasında asit tükenmiştir; öncesinde H⁺, sonrasında OH⁻ fazladır.')

# ============================================================ 07 · antasit pH–zaman (orta, grafik)
Sx7=.65; Sy7=.38
CUR={'K':[(0,1),(1,2.2),(2,2.8),(3,3),(6,3)],'L':[(0,1),(1,4),(2,6),(3,6.8),(4,7),(6,7)],'M':[(0,1),(1,5),(2,8),(3,8.8),(4,9),(6,9)]}
g=''.join(f'\\draw[black!15] (0,{v*Sy7:.2f}) -- ({6*Sx7:.2f},{v*Sy7:.2f});' for v in (1,3,5,7,9))+''.join(f'\\draw[black!15] ({v*Sx7:.2f},0) -- ({v*Sx7:.2f},{10*Sy7:.2f});' for v in (2,4,6))
g+=eksen(6,10,'Zaman (dk)','pH',Sx7,Sy7,[(2,'2'),(4,'4'),(6,'6')],[1,3,5,7,9])
for nm,pt in CUR.items():
    g+='\\draw[thick,vurgu] plot[smooth,tension=.6] coordinates {'+' '.join(f'({a*Sx7:.2f},{b*Sy7:.2f})' for a,b in pt)+'};'
    g+=f'\\node[right,font=\\small\\bfseries] at ({6*Sx7+.05:.2f},{pt[-1][1]*Sy7:.2f}) {{{nm}}};'
SK7=tk(g)
SON={k:v[-1][1] for k,v in CUR.items()}
assert SON=={'K':3,'L':7,'M':9} and all(v[0][1]==1 for v in CUR.values())
dg=('L tabletinin eklendiği çözelti, sonunda nötr hâle gelmiştir.','L eğrisi pH 7’de yataylaşmıştır; pH 7 nötr ortamı gösterir')
yl=[('K tabletinin eklendiği çözelti, sonunda mavi turnusol kâğıdının rengini kırmızıya çevirmez.','K’nın son pH değeri 3’tür; asidik çözelti mavi turnusolu kırmızıya çevirir'),
    ('M tabletinin eklendiği çözeltide fenolftalein renksiz kalır.','M’nin son pH değeri 9’dur; çözelti baziktir ve fenolftalein bazik ortamda pembe renk verir'),
    ('Üç tablet de çözeltinin asitliğini artırmıştır.','üç eğri de pH 1’den yükselmiştir; pH’ın artması asitliğin azaldığını gösterir'),
    ('K tableti, mide asidinin L tabletinden daha büyük bölümünü nötrleştirmiştir.','pH’ı L daha çok yükseltmiştir; K’nın son pH değeri 3, L’ninki 7’dir')]
r=tek_t(dg,yl,0,True)
q('0007',ad=[A('Eğrileri oku','Her tablet için başlangıç ve son pH değeri grafikten okunur.','Başlangıç: 1 · K: 3 · L: 7 · M: 9'),A('Ortamları belirle','pH < 7 asidik, 7 nötr, > 7 bazik.','K: asidik · L: nötr · M: bazik'),A('Yargıları sına','İndikatör renkleri ve pH değişimi ortam türüne göre yorumlanır.','Mavi turnusol: K’da kırmızıya döner · Fenolftalein: M’de pembe olur'),A('Sonucu yaz','Grafikle uyumlu tek yargı aranır.','Doğru yargı: L ile nötr ortam')],
 alt='Günlük Hayatta Asit–Baz',z='orta',kaz='Antasit tabletlerinin pH–zaman grafiğini yorumlayarak ortamın türünü belirler.',kalip='grafik',ne='K, L, M tabletleri, başlangıç pH 1',
 metin='Bir ilaç firması, pH değeri 1 olan eşit hacimdeki yapay mide özsuyuna (seyreltik HCl çözeltisi) aynı kütlede K, L ve M antasit tabletlerini ayrı ayrı atıyor. Çözeltilerin pH değerlerinin zamanla değişimi şekildeki grafikte verilmiştir. Antasitler, mide asidini nötrleştiren bazik karakterli maddeler içerir.\nBuna göre aşağıdakilerden hangisi doğrudur?',
 sekil=SK7,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargı.',
 ip=['Her eğrinin son pH değerini oku ve bu değerin hangi ortama karşılık geldiğini belirle.'],
 bilgi=[B('Antasit','Antasitler mide asidini nötrleştiren bazik maddeler içerir; ortama katıldıklarında pH değeri yükselir. pH 7’nin üstüne çıkan ortam bazik olur. Örnek: pH 2 olan bir çözeltiye bazik madde katılıp pH 6’ya çıkarılırsa çözelti hâlâ asidiktir')],
 puf='Bazik madde katılınca pH artar; son pH değerinin 7’ye göre durumu ortamın türünü verir.')

# ============================================================ 08 · iki indikatör tablosu (orta, tablo)
OBS=[('K','Renksiz','Kırmızı'),('L','Renksiz','Sarı'),('M','Pembe','Sarı'),('N','Renksiz','Kırmızı'),('P','Pembe','Sarı')]
def ortam(f,m):
    if f=='Pembe': assert m=='Sarı'; return 'bazik'
    return 'asidik' if m=='Kırmızı' else 'nötr'
ORT={k:ortam(f,m) for k,f,m in OBS}
assert ORT=={'K':'asidik','L':'nötr','M':'bazik','N':'asidik','P':'bazik'}
SK8=tablo_svg(['Çözelti','Fenolftalein','Metil oranj'],[list(o) for o in OBS])
dg=('K ve N çözeltileri asidiktir.','K ve N’de fenolftalein renksiz, metil oranj kırmızıdır; metil oranjın kırmızı olması yalnız asidik ortamda görülür')
yl=[('L çözeltisi baziktir.','L’de fenolftalein renksizdir; bazik olsaydı pembe olurdu. Renksiz fenolftalein ve sarı metil oranj nötr ortamı gösterir'),
    ('M çözeltisi nötrdür.','M’de fenolftalein pembedir; bu yalnız bazik ortamda görülür'),
    ('M çözeltisi mavi turnusol kâğıdını kırmızıya çevirir.','bazik çözelti mavi turnusolun rengini değiştirmez, kırmızı turnusolu maviye çevirir'),
    ('N çözeltisi kırmızı turnusol kâğıdını maviye çevirir.','N asidiktir; asidik çözelti kırmızı turnusolun rengini değiştirmez')]
r=tek_t(dg,yl,1,True)
q('0008',ad=[A('Renk kurallarını yaz','Fenolftalein yalnız bazda pembe; metil oranj yalnız asitte kırmızıdır.','Pembe → baz · Kırmızı → asit'),A('Çözeltileri sınıfla','Her çözelti için iki gözlem birlikte yorumlanır.','K, N: asidik · L: nötr · M, P: bazik'),A('Yargıları sına','Turnusol kâğıtlarının davranışı da ortam türünden bulunur.','Bazik çözelti mavi turnusolu değiştirmez'),A('Sonucu yaz','Sınıflamayla uyumlu tek yargı seçilir.','Doğru yargı: K ve N asidik')],
 alt='İndikatörler',z='orta',kaz='İki indikatörün renklerinden çözeltilerin asidik, nötr veya bazik olduğunu belirler.',kalip='tablo',ne='K, L, M, N, P için fenolftalein ve metil oranj renkleri',
 metin='Bir öğrenci, etiketleri silinmiş beş çözeltiyi (K, L, M, N ve P) ayırt etmek için her birine fenolftalein ve metil oranj indikatörlerini ayrı ayrı damlatıyor. Fenolftalein asidik ve nötr ortamda renksiz, bazik ortamda pembe; metil oranj asidik ortamda kırmızı, nötr ve bazik ortamda sarı renk vermektedir. Öğrencinin gözlemleri tabloda verilmiştir.\nBuna göre aşağıdakilerden hangisi doğrudur?',
 sekil=SK8,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargı.',
 ip=['İki indikatörün renklerini birlikte düşün: hangi renk çifti yalnız tek bir ortamda görülür?'],
 bilgi=[B('İndikatörler','Fenolftalein bazik ortamda pembe, asidik ve nötr ortamda renksizdir. Metil oranj asidik ortamda kırmızı, nötr ve bazik ortamda sarıdır. Mavi turnusol asitte kırmızıya, kırmızı turnusol bazda maviye döner. Örnek: kırmızı turnusol bazik çözeltide maviye döner')],
 puf='İki indikatörün renk çiftini birlikte oku; tek indikatör asidi nötrden ya da nötrü bazdan ayıramayabilir.')

# ============================================================ 09 · laboratuvar güvenliği (kolay, öncüllü)
d={'I':(True,'asit suya yavaş yavaş akıtılırsa açığa çıkan ısı kontrol altında kalır ve sıçrama riski azalır'),
   'II':(False,'laboratuvarda hiçbir madde tadılmaz; asit ve baz ayırt etmek için indikatör kullanılır'),
   'III':(False,'cildin üzerine bazik çözelti dökmek yanığı artırır; cilt bol su ile yıkanır')}
r=onc_t(d,0)
q('0009',ad=[A('Kuralları tanı','Asit–baz güvenliğinde ana ilke: ters etkili madde dökmemek ve tatmamak.','Seyreltme: asit suya · Tatma yok · Bol suyla yıkama'),adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),A('Sonucu yaz','Doğru olan öncüller bir arada yazılır.',oy(d)+' · Sonuç: '+r['dogru'])],
 alt='Laboratuvar Güvenliği',z='kolay',kaz='Asit ve bazlarla çalışırken uyulması gereken güvenlik kurallarını ayırt eder.',kalip='öncüllü',ne='üç laboratuvar kuralı',
 metin='Bir okulun kimya laboratuvarında öğrencilere asit ve bazlarla çalışırken uyulacak güvenlik kuralları anlatılıyor. Öğretmen, verilen kuralların bazılarının yanlış olduğunu belirtip doğru olanları buldurmak istiyor.\nI. Derişik bir asit seyreltilirken asit, suya yavaş yavaş ve karıştırılarak eklenir.\nII. Etiketi okunamayan bir çözeltinin asit mi baz mı olduğu, tadına bakılarak anlaşılır.\nIII. Cilde asit sıçrarsa hemen üzerine bazik bir çözelti dökülerek nötralleştirilir.\nBuna göre hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan öncüller.',
 ip=['Her kuralı “bu davranış tehlikeyi artırır mı azaltır mı?” diye sına.'],
 bilgi=[B('Güvenlik kuralları','Laboratuvar güvenlik kuralları kazaları ve zehirlenmeleri önlemek için konmuştur; her kural, belirli bir tehlikeyi azaltmaya yöneliktir')],
 puf='Bir davranışın tehlikeyi artırıp artırmadığına bakarak güvenlik kuralını sına.')

# ============================================================ 10 · asit–baz–tuz çözeltisini ayırt etme (orta, tablo)
TAB=[('K','Mavi → kırmızı','Gaz çıkışı var','Yanar'),('L','Kırmızı → mavi','Gaz çıkışı yok','Yanar'),('M','Değişmez','Gaz çıkışı yok','Yanar'),('N','Değişmez','Gaz çıkışı yok','Yanmaz')]
SK10=tablo_svg(['Çözelti','Turnusol kâğıdı','Mg şeridi','Ampul'],[list(t) for t in TAB])
dg=('M çözeltisi nötr olup iyon içeren bir tuz çözeltisi olabilir.','M turnusolu değiştirmediği için nötrdür, ampulü yaktığı için iyon içerir; bu özellikler tuz çözeltisine uyar')
yl=[('K çözeltisinin pH değeri 7’den büyüktür.','K mavi turnusolu kırmızıya çevirir ve Mg ile gaz verir; bu asidik çözeltidir, pH değeri 7’den küçüktür'),
    ('L çözeltisi Mg ile tepkime verir.','L bazik çözeltidir; Mg şeridinde gaz çıkışı gözlenmemiştir'),
    ('N çözeltisi elektriği iletir.','N’de ampul yanmamıştır; çözeltide serbest iyon yoktur (ör. şekerli su)'),
    ('K ve M çözeltileri karıştırılınca nötralleşme tepkimesi olur.','nötralleşme asit ile baz arasında olur; M nötrdür, bir tuz çözeltisi olabilir')]
r=tek_t(dg,yl,2,True)
q('0010',ad=[A('Gözlemleri sınıfla','Turnusol rengi ortamı, Mg ile gaz asidi, ampul iyon varlığını gösterir.','K: asit · L: baz'),A('M’yi yorumla','Turnusolu değiştirmeyen iyonlu çözelti nötr bir tuz çözeltisi olabilir.','M: nötr, iyonlu'),A('N’yi yorumla','Ampul yanmıyorsa çözeltide iyon yoktur.','N: iyonsuz çözelti'),A('Yargıları sına','Her yargı bu sınıflamayla karşılaştırılır.','Doğru yargı: M nötr tuz çözeltisi olabilir')],
 alt='Asit, Baz ve Tuz Çözeltileri',z='orta',kaz='Turnusol, metal ve iletkenlik gözlemlerinden asit, baz, tuz ve iyonsuz çözeltileri ayırt eder.',kalip='tablo',ne='K, L, M, N çözeltileri için üç deney',
 metin='Bir öğrenci, etiketleri silinmiş K, L, M ve N çözeltilerinin her birine mavi ve kırmızı turnusol kâğıdı batırıyor, bir parça magnezyum (Mg) şeridi atıyor ve iletkenlik düzeneğinde ampulün yanıp yanmadığına bakıyor. Gözlemler tabloda verilmiştir; çözeltilerin hiçbiri bu maddelerden başkasını içermemektedir.\nBuna göre aşağıdakilerden hangisi doğrudur?',
 sekil=SK10,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargı.',
 ip=['Her deneyin neyi gösterdiğini düşün: turnusol ortamı, Mg asidi, ampul iyon varlığını gösterir.'],
 bilgi=[B('Çözeltileri ayırt etme','Asit mavi turnusolu kırmızıya çevirir ve aktif metalle gaz verir; baz kırmızı turnusolu maviye çevirir. Nötr tuz çözeltisi turnusolu değiştirmez ama iyon içerdiğinden elektriği iletir. Şekerli su iyon içermediği için iletmez')],
 puf='Turnusol ortamı, Mg ile gaz asidi, ampul iyon varlığını gösterir; üçünü birlikte oku.')

bitir(P,'asitbazuc',UK)
