"""TYT Kimya · Maddenin Halleri · ek paket (halleriki): 20 soru, kardeş yok, ipucu 1.
Şekil koordinatları ve veriler Python'da hesaplanır; TikZ bu değerlerden üretilir. Öncüllerin doğru/yanlış değeri tek yerde (d sözlüğü) tanımlanır."""
import sys,os,math,random
GD=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,GD)
import _hafif_kim2 as H
from _hafif_kim2 import *
from _hafif_kim import onc as _onc_eski, tek
H.KONU='Maddenin Halleri'
UK='kim|Maddenin Halleri'
P=Parti('halleriki','Maddenin Halleri',UK,ders='TYT Kimya',idon='tytkim')
KY='ÖSYM 2018–2026 TYT Kimya (yalnız mantık) · MEB 9. sınıf Maddenin Halleri'
MAP={}
for _n,_t in [(('01','02','17'),('tanecik','Hâllerin tanecik modeli ve plazma')),(('03','04','05','20'),('kati','Katı türleri ve özellikleri')),(('06','07','08','10'),('buhar','Buharlaşma, buhar basıncı ve kaynama')),(('11','12','15'),('gaz','Gazların özellikleri')),(('09','13','14','19'),('hal','Hâl değişimleri ve grafikleri')),(('16','18'),('sivi','Sıvıların özellikleri'))]:
    for _x in _n: MAP[_x]=_t
def kartla(n,alt,fikir,tuzak,z,kalip,adim,tipad,tip):
    a,b=MAP[n]; kart(f'K-KMHL2-{n}',alt,fikir,tuzak,z,kalip,adim,f'km-hl2-{a}',b,KY)
def q(no,ad,**k):
    assert len(k['ip'])==1
    k['tipId']='km-hl2-'+MAP[no[-2:]][0]; k['tip']=MAP[no[-2:]][1]
    mk(P,no,ad=ad,adim=len(ad),**k)
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
ARR='-{Stealth[length=1.9mm,width=1.7mm]}'
def tk(g): return tikz_svg(HEAD+g+TAIL)

# ---------- öncüllü yardımcıları: şık kümeleri hedef harfe göre seçilir ----------
def _anah(s): return (len(s),tuple(s))
def onc_t(d,hedef):
    etiket=sorted(d,key=lambda x:['I','II','III','IV'].index(x))
    import itertools
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
    """dogru: (metin,neden); yanlislar: [(metin,neden)]; hedef_bool True: tek doğru ifade; False: tek yanlış ifade aranır."""
    S=[(m,not hedef_bool,n) for m,n in yanlislar]
    S.insert(hedef,(dogru[0],hedef_bool,dogru[1]))
    return tek(S,hedef_bool)
def cap(s): return ('İ' if s[0]=='i' else s[0].upper())+s[1:]
def oy(d,anahtarlar=None):
    return ' · '.join(f'{k}: '+('doğru' if d[k][0] else 'yanlış') for k in (anahtarlar or d))
def adim_onc(d,keys,baslik=None):
    """d'deki öncüllerden ikisini/birini tek adımda anlatır (doğru kavram, çeldirici dili yok)."""
    ac=' '.join(cap(d[k][1])+'.' for k in keys)
    return A(baslik or ('. '.join(keys)+'. öncül' if len(keys)==1 else ' ve '.join(keys)+'. öncüller'),ac,oy(d,keys))

# ---------- tanecik çizimleri ----------
def disc(x,y,r=.11,f='vurgu!25'): return f'\\draw[thin,fill={f}] ({x:.3f},{y:.3f}) circle ({r});'
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
def kati_p(x0,W=2.4,cols=4,rows=2,sp=.3):
    xs=x0+(W-(cols-1)*sp-.15)/2
    return [(xs+i*sp+(.15 if j%2 else 0),.14+j*.26) for j in range(rows) for i in range(cols)]
def sivi_p(x0,W=2.4,n=8,seed=3): return rastgele(n,x0+.2,x0+W-.2,.13,.68,.25,seed)
def gaz_p(x0,W=2.4,Hh=2.2,n=8,seed=5): return rastgele(n,x0+.2,x0+W-.2,.2,Hh-.2,.8,seed)
def parcacik(pts): return '\n'.join(disc(x,y) for x,y in pts)
def etiket(x,y,s,ek=''): return f'\\node{ek} at ({x:.3f},{y:.3f}) {{{s}}};'

# ============================================================ KARTLAR
kartla('01','Katı, sıvı, gaz modelleri','Katıda tanecikler düzenli ve sıkı, sıvıda düzensiz ama birbirine yakın, gazda birbirinden çok uzak ve kabın tamamına dağılmıştır.','Düzenli dizilimi sıvıya, düzensiz yakın dizilimi katıya yormak.','kolay','şekilli',2,'tanecik','Kapta tanecik modeliyle hâl belirleme')
kartla('02','Plazma ve hâl modelleri','Plazma, serbest iyon ve elektron içeren iyonlaşmış gazdır; yüklü olduğundan iletkendir. Hâl değişimleri ısı alışverişiyle olur.','Plazmayı yüksüz gaz sanmak; gaz–plazma dönüşümünü ısı veren saymak.','orta','öncüllü',4,'plazmahal','Dört hâlin tanecik modeli ve plazma')
kartla('03','Katı sınıflandırması','Erime noktası, katı ve sıvı hâldeki iletkenlik ve çözünme gözleminden iyonik, metalik, kovalent ağ ve moleküler katı ayırt edilir.','Yüksek erime noktasını tek başına iyonik saymak; kovalent ağ ile molekülerik katıyı karıştırmak.','orta','tablo',3,'katisinif','Deney verilerinden katı türünü belirleme')
kartla('04','Katı türleri ve örnekleri','Amorf katıların belirli erime noktası yoktur; iyonik katılar katıda iletmez; elmas kovalent ağ katısıdır.','Camı kristal sanmak; iyonik katıyı katı hâlde iletken saymak; elması moleküler sanmak.','kolay','öncüllü',3,'katiornek','Katı türleri ve örnekleri')
kartla('05','Kristal ve amorf katı','Kristal katı belirli sıcaklıkta erirken sıcaklık sabit kalır; amorf katı geniş aralıkta yumuşar ve sıcaklığı sürekli artar.','Sıcaklığı artan katıyı saf kristal sanmak; sabit sıcaklıkta ısı alınmadığını düşünmek.','orta','grafik',3,'amorf','Isıtma grafiğinde kristal ve amorf katı')
kartla('06','Buharlaşma hızı','Buharlaşma hızı sıcaklık ve yüzey alanı arttıkça artar; ortamdaki buhar derişimi azaldıkça artar.','Yüzey alanının etkisini ters yorumlamak; sıcaklığı yok saymak.','kolay','şekilli',2,'buharlasma','Buharlaşma hızını etkileyen etmenler')
kartla('07','Buharlaşma ve kaynama farkı','Buharlaşma her sıcaklıkta ve yüzeyde, kaynama belirli sıcaklıkta ve sıvının her yerinde olur; ikisi de ısı alır.','Buharlaşmayı ısı veren saymak; kaynamayı yalnız kabarcık olayı sanmak.','orta','hikâyeli',3,'buharkaynama','Buharlaşma ile kaynamanın karşılaştırılması')
kartla('08','Kapalı kapta buhar basıncı','Kapalı kapta buharlaşma ve yoğuşma sürerken buhar basıncı sabitlenir; sıcaklık artınca artar, sıvı miktarına bağlı değildir.','Sabit basınçta yoğuşmanın durduğunu sanmak; sıvı eklenince basıncın arttığını düşünmek.','orta','grafik',4,'buharbasinci','Kapalı kapta buhar basıncı–zaman grafiği')
kartla('09','Isıtma grafiği ve tanecik modeli','Eğimli aralıkta madde tek hâlde, yatay aralıkta iki hâlin karışımı hâlindedir; her an uygun tanecik modeliyle eşleştirilir.','Erime aralığını yalnız sıvı, kaynama aralığını yalnız gaz sanmak.','zor','grafik',4,'hal','x')
kartla('10','Düdüklü tencere','Kapalı kapta basınç artınca kaynama noktası yükselir; grafikte yatay basınç doğrusunun eğriyi kestiği sıcaklık okunur.','Dış basınç değişse de 100 °C okumak; eğri üzerinde yanlış basınç değerine bakmak.','orta','grafik',4,'kaynamagrafik','Buhar basıncı eğrisinden kaynama noktası farkı')
kartla('11','Gazların sıkıştırılabilirliği','Gazlarda tanecikler arası boşluk büyüktür; sıkıştırınca taneciklerin kendisi değil aralarındaki uzaklık azalır. Sıvılar zor sıkıştırılır.','Taneciklerin küçüldüğünü sanmak.','kolay','şekilli',3,'gaz','Enjektörde gaz ve sıvının sıkıştırılması')
kartla('12','Difüzyon','Gaz tanecikleri sürekli hareket eder; sıcaklık arttıkça difüzyon hızlanır; sıvılarda da gerçekleşir.','Soğukta hareketin durduğunu sanmak; difüzyonu yalnız gaza özgü saymak.','kolay','tablo',3,'difuzyon','Sıcaklığa göre difüzyon süresi')
kartla('13','Saf madde ve karışım ısıtma grafiği','Saf maddede hâl değişimi sırasında sıcaklık sabit kalır; karışımda hâl değişimi sırasında sıcaklık değişir.','Sıcaklığı artan her aralığı tek hâl sanmak; karışımı saf madde saymak.','zor','grafik',4,'egri','Saf madde ve karışımın ısıtma grafiğini karşılaştırma')
kartla('14','Soğutma grafiği','Soğutmada yatay bölgeler yoğuşma ve donmadır; yalnız sıvı hâl, bu iki yatay bölge arasındaki süredir.','Yoğuşma ya da donma süresini sıvı süresine katmak.','orta','grafik',3,'sogutma','Soğutma grafiğinden hâl süresi okuma')
kartla('15','Gaz basıncı','Gaz basıncı tanecik çarpmalarından doğar; kapalı kapta sıcaklık artınca taneciklerin hızı ve basınç artar.','Tanecik sayısının ya da boyunun arttığını sanmak.','kolay','tablo',3,'gaz','x')
kartla('16','Viskozite','Bilyenin geç indiği sıvının viskozitesi büyüktür; sıcaklık arttıkça viskozite azalır, etkileşim arttıkça artar.','Viskozite ile akışkanlığı karıştırmak; sıcaklıkla arttığını sanmak.','zor','tablo',4,'viskozite','Bilye düşme deneyiyle viskozite')
kartla('17','Plazma örnekleri','Plazma iyonlaşmış gazdır; neon tabelası, floresan lamba, şimşek ve yıldızlarda bulunur; elektriği iletir.','Plazmayı yüksüz sanmak; yoğuşmuş buharı plazma saymak.','kolay','öncüllü',2,'plazma','Plazma hâli ve örnekleri')
kartla('18','Yüzey gerilimi','Yüzeydeki molekül yalnız içeriye ve yanlara çekilir; net kuvvet içedir. Sıcaklık ve deterjan yüzey gerilimini azaltır.','Yüzeydeki molekülü dışarı çekilen sanmak; deterjanın artırdığını düşünmek.','orta','öncüllü',4,'yuzey','Yüzey gerilimi ve molekül çekimleri')
kartla('19','Hâl değişimleri şeması','Katı→sıvı, sıvı→gaz ve katı→gaz ısı alır; ters yönler ısı verir.','Kırağılaşmayı ısı alan saymak.','kolay','şekilli',3,'hal','Hâl değişimi şemasında ısı alışverişi')
kartla('20','Katı türlerinin tanecik modelleri','Model, katı türünü; tür de iletkenlik, dövülebilirlik ve erime noktası özelliklerini belirler.','Kovalent ağ ile moleküler katıyı, iyonik ile metalik katıyı karıştırmak.','zor','şekilli',4,'kati','x')

# ============================================================ 01 · tanecik modelleri
kaplar=[('K',0,'gaz'),('L',3.2,'katı'),('M',6.4,'sıvı')]
g=kap(0)+parcacik(gaz_p(0,seed=11))+kap(3.2)+parcacik(kati_p(3.2))+kap(6.4)+parcacik(sivi_p(6.4,seed=7))
for ad_,x0,_ in kaplar: g+=etiket(x0+1.2,-.4,f'\\textbf{{{ad_}}}')
SK1=tk(g)
def sk(a,b,c): return f'K: {a}, L: {b}, M: {c}'
d1=tek_t((sk('gaz','katı','sıvı'),''),[
 (sk('gaz','sıvı','katı'),'taneciklerin düzenli dizilip yerinde titreştiği L kabı katıdır; M’deki düzensiz ama birbirine yakın dizilim sıvıya aittir'),
 (sk('sıvı','katı','gaz'),'taneciklerin birbirinden çok uzak olduğu ve kabın tamamına dağıldığı K kabı gazdır; M’deki yakın taneciklerin bulunduğu hâl sıvıdır'),
 (sk('katı','sıvı','gaz'),'K’deki birbirinden çok uzak tanecikler katıya değil gaza aittir; düzenli ve sıkı dizilim L’de olup katıyı gösterir'),
 (sk('katı','gaz','sıvı'),'L’deki taneciklerin düzenli ve sıkı dizilişi gazı değil katıyı gösterir; gaz taneciklerinin aralarındaki uzaklık en büyüktür')],0)
q('0001',ad=[A('Kaplara bak','Gazda tanecikler birbirinden çok uzak ve kabın tamamına dağılmıştır.','K: tanecikler uzak ve dağınık → gaz'),A('Yakın dizilimleri ayır','Katıda tanecikler düzenli ve sıkı; sıvıda düzensiz ama birbirine yakındır.','L: düzenli → katı · M: düzensiz, yakın → sıvı'),A('Sonucu yaz','Her kabın hâli sırayla yazılır.','K: gaz, L: katı, M: sıvı')],
 tipId='km-hl2-tanecik',tip='Kapta tanecik modeliyle hâl belirleme',z='kolay',alt='Tanecik Modelleri',kaz='Katı, sıvı ve gaz hâllerinin tanecik modellerini ayırt eder.',kalip='şekilli',
 kart='K-KMHL2-01 (katı, sıvı, gaz modelleri) · üç kapta tanecik çizimi',
 metin='Ağzı kapalı ve özdeş üç kapta, aynı sayıda tanecik içeren saf bir maddenin katı, sıvı ve gaz hâllerine ait tanecik modelleri şekildeki gibi çizilmiştir. Çizimlerde taneciklerin dizilişi, birbirine uzaklığı ve kabı doldurma durumu kaptan kaba farklılık göstermektedir.\nBuna göre K, L ve M kaplarındaki hâller aşağıdakilerden hangisinde doğru verilmiştir?',
 dogru=d1['dogru'],yan=d1['yan'],sira=d1['sira'],istenen='K, L ve M kaplarındaki hâller.',
 ip=['Taneciklerin dizilişine ve birbirlerine uzaklığına bakarak kapları ayır.'],
 bilgi=[B('Tanecik modelleri','Katıda tanecikler düzenli ve sıkı dizilir, yerinde titreşir. Sıvıda düzensiz ama birbirine yakındır, birbiri üzerinde kayar. Gazda birbirinden çok uzaktır ve kabın tamamına yayılır. Örnek: buzda, suda ve su buharında aynı su molekülleri farklı dizilir')],
 puf='Düzenli ve sıkı dizilim katıyı, düzensiz ama yakın dizilim sıvıyı, çok uzak dağınık dizilim gazı gösterir.',sekil=SK1)

# ============================================================ 02 · dört hâl + plazma
W2=2.2; xs2=[0,2.7,5.4,8.1]
g=''
pl=rastgele(8,.25,W2-.25,.25,1.95,.55,seed=21)
g+=kap(xs2[0],W2)+parcacik(sivi_p(xs2[0],W2,seed=4))       # K sıvı
g+=kap(xs2[1],W2)
for i,(x,y) in enumerate(rastgele(8,xs2[1]+.25,xs2[1]+W2-.25,.25,1.95,.55,seed=23)):
    g+=(f'\\draw[thin,fill=vurgu!25] ({x:.3f},{y:.3f}) circle (.13);\\node[font=\\tiny] at ({x:.3f},{y:.3f}) {{+}};' if i%2==0 else f'\\fill ({x:.3f},{y:.3f}) circle (.05);')   # L plazma
g+=kap(xs2[2],W2)+parcacik(kati_p(xs2[2],W2))           # M katı
g+=kap(xs2[3],W2)+parcacik(gaz_p(xs2[3],W2,seed=31))    # N gaz
for ad_,x0 in zip('KLMN',xs2): g+=etiket(x0+W2/2,-.4,f'\\textbf{{{ad_}}}')
g+='\\draw[thin,fill=vurgu!25] (0.2,-1.15) circle (.13);\\node[font=\\tiny] at (0.2,-1.15) {+};\\node[right,font=\\footnotesize] at (.4,-1.15) {iyon};'
g+='\\fill (2.1,-1.15) circle (.05);\\node[right,font=\\footnotesize] at (2.3,-1.15) {serbest elektron};'
g+='\\draw[thin,fill=vurgu!25] (5.2,-1.15) circle (.11);\\node[right,font=\\footnotesize] at (5.4,-1.15) {yüksüz atom/molekül};'
SK2=tk(g)
d={'I':(True,'plazma serbest iyon ve elektronlar içerdiğinden elektrik akımını iletir'),
   'II':(True,'katının sıvıya dönüşmesi (erime) ısı alarak gerçekleşir'),
   'III':(False,'sıvılarda tanecikler birbiri üzerinde kayarak yer değiştirebilir, yalnız titreşmez'),
   'IV':(False,'gazın plazmaya dönüşmesi için ortamdan enerji alınması gerekir, ısı verilmez')}
r=onc_t(d,3)
q('0002',ad=[A('Modelleri tanı','L serbest iyon ve elektron içerir, plazmadır; M katı, K sıvı, N gazdır.','K: sıvı · L: plazma · M: katı · N: gaz'),adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III','IV'],'III ve IV. öncüller'),A('Sonucu yaz','Doğru olan öncüller bir arada yazılır.',oy(d)+' · Sonuç: I ve II')],
 tipId='km-hl2-plazmahal',tip='Dört hâlin tanecik modeli ve plazma',z='orta',alt='Plazma',kaz='Katı, sıvı, gaz ve plazma hâllerinin tanecik modellerini ve hâl değişimlerindeki ısı alışverişini değerlendirir.',kalip='öncüllü',
 kart='K-KMHL2-02 (plazma ve hâl modelleri) · K sıvı, L plazma, M katı, N gaz',
 metin='Aynı maddenin dört farklı hâlinin kapalı kaplardaki tanecik modeli şekilde verilmiştir. Şekildeki sembollerin anlamı çizimin altında açıklanmıştır. Madde, ısı alıp vererek bu hâller arasında birbirine dönüşebilmektedir.\nI. L kabındaki madde elektrik akımını iletir.\nII. M kabındaki maddenin K kabındaki maddeye dönüşmesi ısı alarak gerçekleşir.\nIII. K kabındaki tanecikler bulundukları yerde titreşir, yer değiştirmez.\nIV. N kabındaki maddenin L kabındaki maddeye dönüşmesi ortama ısı vererek gerçekleşir.\nBuna göre hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan öncüller.',
 ip=['Önce her kaptaki hâli tanecik dizilişinden ve yüklü taneciklerden bul; sonra öncülleri tek tek değerlendir.'],
 bilgi=[B('Plazma','plazma, iyonlaşmış gazdır; serbest iyon ve elektronlar içerdiği için elektrik akımını iletir. Örnek: şimşek kanalında hava kısa süre plazma hâline geçer'),B('Hâl değişimi ve ısı','erime ve buharlaşma gibi tanecikleri birbirinden uzaklaştıran değişimler ısı alır; ters yöndekiler ısı verir')],
 puf='Plazma yüklü taneciklerden oluşur ve iletkendir; taneciklerin birbirinden uzaklaştığı her hâl değişimi ısı alır.',sekil=SK2)

# ============================================================ 03 · katı türleri tablosu
tab=[('X','801','iletmez','iletir','çözünür'),('Y','1085','iletir','iletir','çözünmez'),('Z','1710','iletmez','iletmez','çözünmez'),('T','115','iletmez','iletmez','çözünmez')]
TUR={'X':'iyonik','Y':'metalik','Z':'kovalent ağ','T':'moleküler'}
SK3=tablo_svg(['Katı','Erime sıc. (°C)','Katıda iletkenlik','Sıvıda iletkenlik','Suda çözünme'],[list(s) for s in tab])
def s3(a,b,c,t): return f'X: {a}, Y: {b}, Z: {c}, T: {t}'
d3=tek_t((s3('iyonik','metalik','kovalent ağ','moleküler'),''),[
 (s3('metalik','iyonik','kovalent ağ','moleküler'),'katı hâlde elektrik akımını yalnız metalik katılar iletir; X katı hâlde iletmez, sıvı hâlde ilettiği için iyoniktir'),
 (s3('iyonik','metalik','moleküler','kovalent ağ'),'çok yüksek erime noktası ve hiçbir hâlde iletkenlik göstermemesi kovalent ağ katısını; düşük erime noktası moleküler katıyı gösterir'),
 (s3('kovalent ağ','metalik','iyonik','moleküler'),'sıvı hâlde de iletmeyen ve suda çözünmeyen Z iyonik olamaz; X sıvı hâlde iletir ve suda çözünür, bu nedenle iyoniktir'),
 (s3('iyonik','kovalent ağ','metalik','moleküler'),'katı hâlde elektrik iletkenliği metalik katıya özgüdür; Y iletken olduğundan metaliktir, Z ise iletmediği için metalik olamaz')],4)
q('0003',ad=[A('Katı hâlde iletkenliğe bak','Katı hâlde yalnız metalik katılar iletir.','Y: metalik'),A('Sıvı hâlde ve çözünmede ayır','Katıda iletmeyen ama sıvıda ileten, suda çözünen katı iyoniktir.','X: iyonik'),A('Erime noktasıyla ayır','Hiçbir hâlde iletmeyenlerden çok yüksek erime noktalısı kovalent ağ, düşük olanı moleküler katıdır.','Z (1710 °C): kovalent ağ · T (115 °C): moleküler'),A('Şıkları karşılaştır','Dört sonucu veren şık seçilir.','E')],
 tipId='km-hl2-katisinif',tip='Deney verilerinden katı türünü belirleme',z='orta',alt='Katılar',kaz='Katıların bazı özelliklerinden iyonik, metalik, kovalent ağ ve moleküler katı olduklarını belirler.',kalip='tablo',
 kart='K-KMHL2-03 (katı sınıflandırması) · X iyonik, Y metalik, Z kovalent ağ, T moleküler',
 metin='Bir laboratuvarda X, Y, Z ve T katılarının erime noktaları, katı ve sıvı hâldeki elektrik iletkenlikleri ile suda çözünme durumları incelenmiş ve sonuçlar tabloda verilmiştir. Sıvı hâl iletkenliği, erime noktasının hemen üstündeki sıcaklıkta ölçülmüştür.\nBuna göre bu katıların türleri aşağıdakilerden hangisinde doğru verilmiştir?',
 sekil=SK3,dogru=d3['dogru'],yan=d3['yan'],sira=d3['sira'],istenen='X, Y, Z ve T katılarının türleri.',
 ip=['Katı hâlde iletkenlik, sıvı hâlde iletkenlik ve erime noktası birlikte hangi katı türüne işaret ediyor?'],
 bilgi=[B('Katı türleri','İyonik katı: katıda iletmez, sıvıda ve çözeltide iletir (NaCl). Metalik katı: katıda da sıvıda da iletir (Cu). Kovalent ağ katısı: çok yüksek erime noktalı, iletmez (elmas, kuvars). Moleküler katı: düşük erime noktalı, iletmez (iyot, buz)')],
 puf='Katı hâlde iletiyorsa metalik; yalnız sıvıda iletiyorsa iyonik; hiç iletmeyip erime noktası çok yüksekse kovalent ağ, düşükse moleküler katıdır.')

# ============================================================ 04 · amorf, iyonik, elmas
d={'I':(True,'cam gibi amorf katıların tanecikleri düzensiz dizilir ve belirli bir erime noktaları yoktur'),
   'II':(False,'iyonik katılarda iyonlar yerlerinde sabit olduğundan katı hâlde elektrik akımı iletilmez (sıvı hâlde ve çözeltide iletilir)'),
   'III':(False,'elmas, atomları kovalent bağlarla birbirine bağlı ağ yapılı bir katıdır ve erime noktası çok yüksektir')}
r=onc_t(d,0)
q('0004',ad=[adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),A('Sonucu yaz','Doğru olan öncüller bir arada yazılır.',oy(d)+' · Sonuç: Yalnız I')],
 tipId='km-hl2-katiornek',tip='Katı türleri ve örnekleri',z='kolay',alt='Katılar',kaz='Amorf, iyonik ve kovalent ağ katıların genel özelliklerini ayırt eder.',kalip='öncüllü',
 kart='K-KMHL2-04 (katı türleri) · cam, sofra tuzu, elmas',
 metin='Katıların yapısını ve özelliklerini inceleyen bir öğrenci, defterine şu notları alıyor.\nI. Cam gibi amorf katıların belirli bir erime noktası yoktur.\nII. Sofra tuzu gibi iyonik katılar, katı hâlde elektrik akımını iletir.\nIII. Elmas, tanecikleri arasında zayıf etkileşimler bulunan moleküler bir katıdır.\nÖğretmeni, bu notların yalnız bir kısmının doğru olduğunu söylüyor.\nBuna göre öğrencinin notlarından hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan notlar.',
 ip=['Her notu, ilgili katı türünün temel özelliğiyle karşılaştır.'],
 bilgi=[B('Amorf ve kristal katı','kristal katıların tanecikleri düzenli dizilir ve belirli erime noktaları vardır (NaCl, buz). Amorf katıların tanecikleri düzensizdir ve belirli erime noktaları yoktur (cam, plastik)')],
 puf='Amorf katıda belirli erime noktası yoktur; iyonik katı yalnız sıvıda ve çözeltide iletir; elmas kovalent ağ katısıdır.')

# ============================================================ 05 · kristal / amorf grafik
def eksen(xm,ym,xt,yt,xl,yl,sx,sy,ek=''):
    s=f'\\draw[thick,{ARR}] (0,0) -- ({xm*sx+.3:.2f},0);\\draw[thick,{ARR}] (0,0) -- (0,{ym*sy+.3:.2f});'
    for t in xt: s+=f'\\draw ({t*sx:.2f},0) -- ({t*sx:.2f},-.07) node[below,font=\\footnotesize] {{{t}}};'
    for t in yt: s+=f'\\draw (0,{t*sy:.2f}) -- (-.07,{t*sy:.2f}) node[left,font=\\footnotesize] {{{t}}};'
    s+=f'\\node[font=\\footnotesize,anchor=west] at ({xm*sx+.35:.2f},0) {{{xl}}};\\node[font=\\footnotesize,anchor=south] at (0,{ym*sy+.35:.2f}) {{{yl}}};'
    return s+ek
def egri(pts,sx,sy,st='thick',sm=False):
    return f'\\draw[{st}{",smooth" if sm else ""}] '+' -- '.join(f'({x*sx:.2f},{(y)*sy:.2f})' for x,y in pts)+';' if not sm else f'\\draw[{st},smooth] plot coordinates {{'+' '.join(f'({x*sx:.2f},{y*sy:.2f})' for x,y in pts)+'};'
sx,sy=.52,.036
X5=[(0,20),(2,60),(6,60),(8,100)]; Y5=[(0,20),(1,35),(2,48),(4,64),(6,76),(8,86),(10,93)]
def seviye(S,t):
    for (a,b),(c,e) in zip(S,S[1:]):
        if a<=t<=c: return b+(e-b)*(t-a)/(c-a)
assert seviye(X5,3)==60==seviye(X5,5) and seviye(Y5,10)==93
g=eksen(10,110,range(0,11,2),[20,60,100],'Zaman (dk)','Sıcaklık (°C)',sx,sy)
g+=egri(X5,sx,sy,'vurgu,very thick')+egri(Y5,sx,sy,'thick',True)
g+=f'\\node[vurgu,font=\\small\\bfseries] at ({8*sx+.3:.2f},{100*sy:.2f}) {{X}};\\node[font=\\small\\bfseries] at ({10*sx+.3:.2f},{93*sy+.05:.2f}) {{Y}};'
SK5=tk(g)
d5=tek_t(('X’in erime sıcaklığı 60 °C’dir ve 2–6. dakikalar arasında X hem katı hem sıvı hâlde bulunur.',''),[
 ('Y’nin belirli bir erime sıcaklığı vardır ve bu sıcaklık 64 °C’dir.','amorf katıların belirli bir erime sıcaklığı yoktur; Y’nin sıcaklığı yumuşarken sürekli artar'),
 ('2–6. dakikalar arasında X’e verilen ısı, X’in sıcaklığını yükseltmek için kullanılır.','2–6. dakikalarda sıcaklık sabittir; verilen ısı katının sıvıya dönüşmesi için harcanır'),
 ('Y’nin tanecikleri, X’in tanecikleri gibi düzenli bir kristal örgüde dizilmiştir.','amorf katıların tanecikleri düzensiz dizilir; düzenli dizilim kristal katılara özgüdür'),
 ('X ve Y’nin erime sıcaklıkları aynıdır.','X 60 °C’de erirken Y belirli bir sıcaklıkta erimez; ikisinin erime sıcaklığı karşılaştırılamaz')],3)
q('0005',ad=[A('X’in eğrisini oku','Yatay aralık hâl değişimini gösterir; X’te 2–6. dakikada sıcaklık sabittir.','X: 60 °C’de erir · katı + sıvı birlikte'),A('Y’nin eğrisini oku','Y’nin sıcaklığı yatay kalmadan, giderek yavaşlayarak artar.','Y: belirli erime noktası yok → amorf'),A('Şıkları sına','Sabit sıcaklıkta verilen ısı hâl değişimine harcanır; amorf katı düzensizdir.','A, B, C, E yanlış'),A('Sonucu yaz','Doğru ifadeyi veren şık seçilir.','D')],
 tipId='km-hl2-amorf',tip='Isıtma grafiğinde kristal ve amorf katı',z='orta',alt='Katılar',kaz='Kristal ve amorf katıların ısıtma grafiğini yorumlar.',kalip='grafik',
 kart='K-KMHL2-05 (kristal ve amorf katı) · X kristal, Y amorf ısıtma grafiği',
 metin='Eşit kütlelerde, kristal yapılı X katısı ile camsı (amorf) yapılı Y katısı, aynı güçteki ısıtıcılarla ısıtılıyor. Isıtma sırasında katıların kaptan buharlaşma yoluyla kütle kaybetmediği kabul edilmektedir. Sıcaklıklarının zamanla değişimi şekildeki grafikte verilmiştir.\nBuna göre aşağıdakilerden hangisi söylenebilir?',
 sekil=SK5,dogru=d5['dogru'],yan=d5['yan'],sira=d5['sira'],istenen='Grafikten söylenebilecek doğru ifade.',
 ip=['Sıcaklığın sabit kaldığı aralık varsa o aralıkta ne olduğunu, yoksa katının nasıl bir katı olduğunu düşün.'],
 bilgi=[B('Erime ve katı türü','kristal katı belirli bir sıcaklıkta erir ve erirken sıcaklığı sabit kalır. Amorf katı belirli bir sıcaklıkta erimez; ısıtılınca giderek yumuşar ve sıcaklığı sürekli artar. Örnek: buz 0 °C’de erir, cam yumuşayarak akar')],
 puf='Isıtma grafiğinde yatay aralık kristal katının erimesini gösterir; yatay aralığı olmayan sürekli yükselen eğri amorf katıya uyar.')

# ============================================================ 06 · buharlaşma hızı kapları
def kab(x,w,h,lv,sic,ad_):
    s=f'\\fill[vurgu!15] ({x},0) rectangle ({x+w},{lv});\\draw[thick] ({x},{h}) -- ({x},0) -- ({x+w},0) -- ({x+w},{h});'
    s+=f'\\node at ({x+w/2},-.4) {{\\textbf{{{ad_}}}}};\\node[font=\\footnotesize] at ({x+w/2},-.9) {{{sic} °C}};'
    return s
V=1.5
g=kab(0,3,1.4,V/3,25,'K')+kab(3.8,1,2.4,V/1.0,25,'L')+kab(5.6,3,1.4,V/3,40,'M')
assert abs(1*(V/1.0)-3*(V/3))<1e-9
SK6=tk(g)
yan6=[('K > M > L','yüzey alanı büyük olan kapta suyun daha geç buharlaştığını düşünmüş (yüzey alanı etkisini ters yorumlamış)','bilgi'),
      ('L > M > K','yüzey alanının etkisini doğru yorumlayıp L’yi en yavaş almış; ancak sıcak kapta buharlaşmanın daha yavaş olduğunu düşünerek M’yi K’den sonra sıralamış','bilgi'),
      ('M > K > L','hem yüzey alanının hem sıcaklığın etkisini ters yorumlamış; oysa ikisi de arttıkça buharlaşma hızlanır','bilgi'),
      ('M > L > K','sıcaklık farkını belirleyici sayıp ters yorumlayarak M’yi en yavaş almış; kalan iki kapta yüzey alanı büyük olan K’yi daha hızlı sıralamış','bilgi')]
q('0006',ad=[A('Etmenleri belirle','Kaplarda yüzey alanı ve sıcaklık farklıdır; sıvı ve miktar aynıdır.','K ile M: geniş yüzey · L: dar yüzey · M: 40 °C'),A('Hızı yorumla','Yüzey alanı ve sıcaklık arttıkça buharlaşma hızı artar.','M en hızlı · K ikinci · L en yavaş'),A('Süreye çevir','Hız büyük olan kapta tamamen buharlaşma süresi kısadır.','süre: L > K > M')],
 tipId='km-hl2-buharlasma',tip='Buharlaşma hızını etkileyen etmenler',z='kolay',alt='Buharlaşma',kaz='Buharlaşma hızını etkileyen etmenleri yorumlar.',kalip='şekilli',
 kart='K-KMHL2-06 (buharlaşma hızı) · geniş ve dar kaplarda su, 25 ve 40 °C',
 dogru='L > K > M',yan=yan6,sira=['L > K > M','K > M > L','L > M > K','M > K > L','M > L > K'],
 metin='Bir öğrenci, aynı odadaki üç farklı kaba ağızları açık olacak biçimde eşit miktarda saf su koyuyor. K ve M kapları aynı genişlikte sığ tabaklar, L kabı dar ve derin bir kaptır; suların sıcaklıkları şekilde verilmiştir. Ortamda hava akımı yoktur ve kaplardaki suyun tamamının buharlaşması için geçen süreler karşılaştırılacaktır.\nBuna göre süreler arasındaki ilişki aşağıdakilerden hangisidir?',
 istenen='Tamamen buharlaşma sürelerinin büyükten küçüğe sıralanması.',
 ip=['Kaplar arasında hangi nicelikler farklı, hangileri aynı?'],
 bilgi=[B('Buharlaşma hızı','buharlaşma hızı sıvının sıcaklığı ve yüzey alanı arttıkça artar, ortamdaki buhar derişimi azaldıkça da artar. Örnek: ıslak çamaşır, sıcak havada ve asılıp yayıldığında daha çabuk kurur')],
 puf='Sıcaklığı ve yüzey alanı büyük olan sıvı daha çabuk buharlaşır; süre ile hız ters yönde sıralanır.',sekil=SK6)

# ============================================================ 07 · buharlaşma / kaynama farkı
d7=tek_t(('Buharlaşma ısı alan, kaynama ise ısı veren bir olaydır.','buharlaşma da kaynama da sıvı tanecikleri gaz hâline geçirdiği için ısı alan olaylardır'),[
 ('Buharlaşma her sıcaklıkta gerçekleşir, kaynama ise yalnız belirli bir sıcaklıkta (kaynama noktasında) gerçekleşir.','buharlaşma her sıcaklıkta olur; kaynama yalnız kaynama noktasında gerçekleşir'),
 ('Buharlaşma yalnız sıvının yüzeyinde, kaynama ise sıvının her yerinde gerçekleşir.','buharlaşma yüzeyde, kaynama sıvının her yerinde olur'),
 ('Kaynama sırasında sıvının içinde buhar kabarcıkları oluşur, buharlaşmada oluşmaz.','kaynamada sıvının içinde buhar kabarcıkları oluşur; buharlaşmada olmaz'),
 ('Dış basınç değişirse sıvının kaynama noktası da değişir.','dış basınç azalırsa kaynama noktası düşer, artarsa yükselir')],2,False)
q('0007',ad=[A('Gözlemleri çevir','Yüzeyden yavaşça buhar çıkması buharlaşmayı, her yerde kabarcık oluşması kaynamayı gösterir.','yüzey: buharlaşma · her yer: kaynama'),A('İfadeleri sına','Her ifade, iki olayın bilinen özellikleriyle karşılaştırılır.','A, B, D, E doğru'),A('Hatalı ifadeyi bul','İkisi de sıvıyı gaz hâline getirdiği için ısı alır.','C: yanlış')],
 tipId='km-hl2-buharkaynama',tip='Buharlaşma ile kaynamanın karşılaştırılması',z='orta',alt='Buharlaşma ve Kaynama',kaz='Buharlaşma ve kaynama olaylarını karşılaştırır.',kalip='hikâyeli',
 kart='K-KMHL2-07 (buharlaşma ve kaynama farkı) · açık kapta su ısıtma gözlemi',
 metin='Fen laboratuvarında öğretmen, açık bir beherdeki suyu oda sıcaklığından başlayarak ısıtıyor. Öğrenciler, ısıtma boyunca su yüzeyinden çok az miktarda buhar çıktığını, suyun sıcaklığı kaynama noktasına ulaşınca ise sıvının her yerinde kabarcıklar oluşup hızla buhara dönüştüğünü ve sıcaklığın sabit kaldığını not ediyorlar.\nBuna göre buharlaşma ve kaynama ile ilgili aşağıdakilerden hangisi yanlıştır?',
 dogru=d7['dogru'],yan=d7['yan'],sira=d7['sira'],istenen='Yanlış olan ifade.',
 ip=['İki olayı sıcaklık, gerçekleştiği yer ve gözlenen olay bakımından ayrı ayrı değerlendir.'],
 bilgi=[B('Buharlaşma ve kaynama','buharlaşma her sıcaklıkta, yalnız sıvı yüzeyinde olur. Kaynama belirli bir sıcaklıkta ve sıvının her yerinde olur; kabarcıklar oluşur. İkisi de ısı alır. Örnek: çamaşırın kuruması buharlaşma, çaydanlıktaki suyun fokurdaması kaynamadır')],
 puf='Buharlaşma da kaynama da ısı alan olaylardır; fark sıcaklık, bölge ve kabarcık oluşumundadır.')

# ============================================================ 08 · kapalı kapta buhar basıncı–zaman
sx,sy=.5,.022
P8=[(0,0),(1,28),(2,42),(3,48),(4,50),(5,50),(6,50),(7,50),(8,50),(8.5,58),(9,76),(10,91),(11,98),(12,100),(13,100),(14,100)]
g=eksen(14,110,range(0,15,2),[50,100],'Zaman (dk)','Buhar basıncı (mmHg)',sx,sy)
g+=egri(P8,sx,sy,'vurgu,very thick,tension=.35',True)
SK8=tk(g)
assert P8[4][1]==P8[7][1]==50 and P8[-1][1]==100
d={'I':(True,'kapta başlangıçta buhar yokken buharlaşma yoğuşmadan hızlıdır; basınç sabitlenene kadar buharlaşma hızı yoğuşma hızından büyüktür'),
   'II':(True,'buhar basıncı sabit kaldığı aralıkta sıvıdan buhara geçen ve buhardan sıvıya dönen tanecik sayıları eşittir; olay durmaz'),
   'III':(True,'buhar basıncı yalnız sıcaklığa bağlıdır ve sıcaklık arttıkça artar; basıncın yeniden yükselmesi sıcaklığın artırıldığını gösterir'),
   'IV':(False,'buhar basıncı sıvının miktarına bağlı değildir; kaba daha fazla sıvı eklenmesi basıncı değiştirmez')}
r=onc_t(d,3)
q('0008',ad=[A('Grafiği oku','Basınç önce artıyor, 4–8. dakikada sabit kalıyor, 8. dakikadan sonra yeniden artıp yine sabitleniyor.','0–4: artış · 4–8: 50 mmHg · 8–12: artış · 12–14: 100 mmHg'),adim_onc(d,['I','II'],'I ve II. öncüller'),adim_onc(d,['III']),adim_onc(d,['IV']),A('Sonucu yaz','Doğru olan öncüller bir arada yazılır.',oy(d)+' · Sonuç: I, II ve III')],
 tipId='km-hl2-buharbasinci',tip='Kapalı kapta buhar basıncı–zaman grafiği',z='orta',alt='Buhar Basıncı',kaz='Kapalı kapta buhar basıncının zamanla değişimini buharlaşma, yoğuşma ve sıcaklık açısından yorumlar.',kalip='grafik',
 kart='K-KMHL2-08 (kapalı kapta buhar basıncı) · basınç–zaman, sıcaklığın bir kez artırılması',
 metin='Havası boşaltılmış, kapalı ve sabit hacimli bir kaba bir miktar saf X sıvısı konuyor. Kaptaki buhar basıncının zamanla değişimi şekildeki grafikte verilmiştir. Sıcaklık, deney süresince yalnız bir kez değiştirilmiştir.\nI. 0–2. dakikalar arasında X’in buharlaşma hızı, yoğuşma hızından büyüktür.\nII. 5–7. dakikalar arasında sıvıdan buhara geçen tanecik sayısı, buhardan sıvıya dönen tanecik sayısına eşittir.\nIII. Sıcaklık 8. dakikadan itibaren artırılmıştır.\nIV. 12. dakikada kaba bir miktar daha X sıvısı eklenirse buhar basıncı 100 mmHg’den büyük olur.\nBuna göre hangileri doğrudur?',
 sekil=SK8,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Grafiğe göre doğru olan öncüller.',
 ip=['Basıncın arttığı ve sabit kaldığı aralıklarda buharlaşma ile yoğuşma hızlarının nasıl olduğunu düşün; buhar basıncının neye bağlı olduğunu hatırla.'],
 bilgi=[B('Kapalı kapta buhar basıncı','kapalı kapta sıvı buharlaşırken buhar da yoğuşur. Buharlaşma hızı yoğuşma hızına eşit olunca buhar basıncı sabitlenir; olay durmaz. Buhar basıncı sıcaklık arttıkça artar, sıvı miktarına ve kap hacmine bağlı değildir')],
 puf='Basıncın sabit kaldığı aralıkta buharlaşma ve yoğuşma sürer; buhar basıncını yalnız sıcaklık ve sıvı türü değiştirir.')

# ============================================================ 09 · ısıtma grafiği + tanecik modelleri (K,L,M,N)
sx,sy=.42,.036
X9=[(0,10),(2,40),(6,40),(9,80),(13,80)]
zam={'I':1,'II':4,'III':7,'IV':11}
assert seviye(X9,1)==25 and seviye(X9,4)==40 and 40<seviye(X9,7)<80 and seviye(X9,11)==80
g=f'\\draw[thick,{ARR}] (0,0) -- ({14*sx+.3:.2f},0);\\draw[thick,{ARR}] (0,0) -- (0,{95*sy:.2f});'
for t in range(0,15): g+=f'\\draw ({t*sx:.2f},0) -- ({t*sx:.2f},-.07)'+(f' node[below,font=\\footnotesize] {{{t}}};' if t%2==0 else ';')
for t in (10,40,80): g+=f'\\draw (0,{t*sy:.2f}) -- (-.07,{t*sy:.2f}) node[left,font=\\footnotesize] {{{t}}};'
g+=f'\\node[font=\\footnotesize,anchor=west] at ({14*sx+.35:.2f},0) {{Zaman (dk)}};\\node[font=\\footnotesize,anchor=south] at (0,{95*sy+.03:.2f}) {{Sıcaklık (°C)}};'
g+=egri(X9,sx,sy,'vurgu,very thick')
for k,t in zam.items():
    yy=seviye(X9,t); g+=f'\\draw[dashed,gray] ({t*sx:.2f},0) -- ({t*sx:.2f},{yy*sy:.2f});\\fill ({t*sx:.2f},{yy*sy:.2f}) circle (.05);\\node[font=\\small\\bfseries] at ({t*sx:.2f},{yy*sy+.3:.2f}) {{{k}}};'
SK9=tk(g)
HAL=lambda *a:' · '.join(a)
d9=tek_t((HAL('katı','katı + sıvı','sıvı','sıvı + gaz'),''),[
 (HAL('katı','sıvı','sıvı','gaz'),'sıcaklığın sabit kaldığı aralıklarda tek hâl değil iki hâl birlikte bulunur: erimede katı + sıvı, kaynamada sıvı + gaz'),
 (HAL('katı','katı + sıvı','sıvı + gaz','sıvı + gaz'),'sıcaklığın arttığı eğimli aralıkta madde tek hâldedir; III. anda X yalnız sıvıdır'),
 (HAL('katı','sıvı','sıvı','sıvı + gaz'),'erime aralığında (II) madde yalnız sıvı değildir, katı ve sıvı birlikte bulunur'),
 (HAL('katı','katı + sıvı','sıvı','gaz'),'kaynama aralığında (IV) madde yalnız gaz değildir, sıvı ve gaz birlikte bulunur')],1)
q('0009',ad=[A('Aralıkları belirle','Eğimli aralıkta madde tek hâldedir; yatay aralıkta iki hâl birlikte bulunur.','I: eğimli · II: yatay (40 °C) · III: eğimli · IV: yatay (80 °C)'),A('İlk yatay aralık','40 °C’de sıcaklık sabittir; bu aralık erimedir.','II: katı + sıvı'),A('Eğimli aralıklar','Katı ısınırken yalnız katı, erime bitince sıvı ısınırken yalnız sıvı bulunur.','I: katı · III: sıvı'),A('İkinci yatay aralık','80 °C’de sıcaklık sabittir; bu aralık kaynamadır.','IV: sıvı + gaz'),A('Sonucu yaz','Hâlleri sırasıyla veren şık seçilir.',HAL('katı','katı + sıvı','sıvı','sıvı + gaz').replace(' · ',' ; '))],
 tipId='km-hl2-hal',tip='Hâl değişimleri ve grafikleri',z='zor',alt='Hâl Değişimleri',kaz='Isıtma grafiğindeki anlarda maddenin bulunduğu hâlleri belirler.',kalip='grafik',
 kart='K-KMHL2-09 (ısıtma grafiğinde hâller) · I–IV anları',
 metin='Katı hâldeki saf X maddesi, kapalı bir kapta sabit güçlü bir ısıtıcıyla ısıtılıyor ve sıcaklığının zamanla değişimi şekildeki grafikte veriliyor. Grafikte I, II, III ve IV ile bazı anlar işaretlenmiştir.\nBuna göre I, II, III ve IV anlarında X’in bulunduğu hâller sırasıyla aşağıdakilerden hangisinde doğru verilmiştir?',
 sekil=SK9,dogru=d9['dogru'],yan=d9['yan'],sira=d9['sira'],istenen='I–IV anlarında X’in bulunduğu hâller.',
 ip=['Her anın grafikte eğimli mi yatay mı bir aralığa denk geldiğine bak ve o aralıkta kaç hâlin bulunabileceğini düşün.'],
 bilgi=[B('Isıtma grafiği ve hâller','saf maddede sıcaklık artarken madde tek hâldedir; sıcaklığın sabit kaldığı aralıkta (erime, kaynama) iki hâl birlikte bulunur. Örnek: suyun tamamen buz olduğu an ile buzun erimekte olduğu an farklı hâl bilgisi verir')],
 puf='Eğimli aralık tek hâli, yatay aralık iki hâlin bir arada bulunduğu hâl değişimini gösterir.')

# ============================================================ 10 · düdüklü tencere, buhar basıncı eğrisi (su)
sx,sy=.075,1.45
P10=[(70,.3),(80,.5),(90,.7),(100,1.0),(110,1.4),(120,2.0),(130,2.7)]
rd=dict((p,t) for t,p in P10)
Tdag=rd[.7]; Tdud=rd[2.0]; assert (Tdag,Tdud)==(90,120)
g=f'\\draw[thick,{ARR}] (0,0) -- ({(130-65)*sx+.3:.2f},0);\\draw[thick,{ARR}] (0,0) -- (0,{3.1*sy:.2f});'
for t in range(70,131,10): g+=f'\\draw[gray!40,thin] ({(t-65)*sx:.2f},0) -- ({(t-65)*sx:.2f},{3*sy:.2f});\\draw ({(t-65)*sx:.2f},0) -- ({(t-65)*sx:.2f},-.07) node[below,font=\\footnotesize] {{{t}}};'
for p,lab in [(.5,'0,5'),(.7,'0,7'),(1,'1'),(1.5,'1,5'),(2,'2'),(2.5,'2,5'),(3,'3')]: g+=f'\\draw[gray!40,thin] (0,{p*sy:.2f}) -- ({(130-65)*sx:.2f},{p*sy:.2f});\\draw (0,{p*sy:.2f}) -- (-.07,{p*sy:.2f}) node[left,font=\\footnotesize] {{{lab}}};'
g+=f'\\node[font=\\footnotesize,anchor=west] at ({(130-65)*sx+.35:.2f},0) {{Sıcaklık (°C)}};\\node[font=\\footnotesize,anchor=south] at (0,{3.1*sy+.05:.2f}) {{Buhar basıncı (atm)}};'
g+='\\draw[vurgu,very thick,smooth] plot coordinates {'+' '.join(f'({(t-65)*sx:.2f},{p*sy:.2f})' for t,p in P10)+'};'
SK10=tk(g)
dogru10=Tdud-Tdag; assert dogru10==30
assert 100-Tdag==10 and Tdud-100==20 and 130-Tdag==40 and 130-80==50 and rd[2.7]==130 and rd[.5]==80
q('0010',ad=[A('Dağ evi için oku','Kaynama noktası, buhar basıncının dış basınca eşit olduğu sıcaklıktır; 0,7 atm düzeyinden eğriye bakılır.','0,7 atm → 90 °C'),A('Düdüklü tencere için oku','Tencerenin içindeki basınç 2 atm olduğundan 2 atm düzeyinden eğriye bakılır.','2 atm → 120 °C'),A('Farkı bul','İki kaynama sıcaklığı birbirinden çıkarılır.','120 − 90 = 30 °C')],
 tipId='km-hl2-kaynamagrafik',tip='Buhar basıncı eğrisinden kaynama noktası farkı',z='orta',alt='Kaynama Noktası ve Dış Basınç',kaz='Buhar basıncı–sıcaklık eğrisinden farklı dış basınçlardaki kaynama noktalarını okuyup karşılaştırır.',kalip='grafik',
 kart='K-KMHL2-10 (düdüklü tencere) · su, 0,7 atm ve 2 atm',
 dogru=30,yan=[(10,'Düdüklü tencere için 2 atm yerine 1 atm düzeyinden 100 °C okumuş: 100 − 90 = 10 °C.','dikkat'),
  (20,'Düdüklü tencerenin kaynama sıcaklığını (120 °C), dağ evi yerine 1 atm’deki 100 °C ile karşılaştırmış: 120 − 100 = 20 °C.','dikkat'),
  (40,'2 atm düzeyi yerine 2,7 atm düzeyinden okumuş: 130 − 90 = 40 °C.','islem'),
  (50,'Hem 2,7 atm düzeyinden (130 °C) hem 0,5 atm düzeyinden (80 °C) okumuş: 130 − 80 = 50 °C.','islem')],
 metin='Dağ evinde kamp yapan bir grup, suyu açık kapta kaynatırken dış basıncı 0,7 atm olarak ölçüyor. Eve döndüklerinde ise aynı suyu, içindeki toplam basınç 2 atm’e ulaşan, kapağı kapalı bir düdüklü tencerede kaynatıyorlar. Suyun buhar basıncının sıcaklıkla değişimi şekildeki grafikte verilmiştir.\nBuna göre suyun düdüklü tencerede ve dağ evinde kaynama sıcaklıkları arasındaki fark kaç °C’dir?',
 sekil=SK10,istenen='İki kaynama sıcaklığı arasındaki fark (°C).',
 ip=['Her ortam için, dış basıncı gösteren düzeyden eğriye giderek suyun kaynama sıcaklığını ayrı ayrı oku.'],
 bilgi=[B('Kaynama noktası ve basınç','bir sıvı, buhar basıncı dış basınca eşit olunca kaynar; grafikte dış basınç düzeyinden eğriye gidilip sıcaklık okunur. Dış basınç büyüdükçe kaynama noktası yükselir. Örnek: düdüklü tencerede su 100 °C’nin üstünde kaynar')],
 puf='Kaynama sıcaklığını bulmak için önce dış basıncı belirle, o basınç düzeyinden eğriye git ve sıcaklığı oku.')

# ============================================================ 11 · enjektör
def enj(y0,gaz,seed):
    s=f'\\draw[thick] (0,{y0}) rectangle (2.4,{y0+.9});\\draw[thick] (-.45,{y0+.3}) rectangle (0,{y0+.6});\\fill (-.45,{y0+.3}) rectangle (-.35,{y0+.6});'
    s+=f'\\draw[thick,fill=gray!30] (2.4,{y0+.05}) rectangle (2.55,{y0+.85});\\draw[thick] (2.55,{y0+.45}) -- (3.6,{y0+.45});\\draw[thick] (3.6,{y0+.15}) -- (3.6,{y0+.75});'
    if gaz: pts=rastgele(6,.2,2.2,y0+.15,y0+.75,.5,seed)
    else:
        pts=[(.17+i*.3+(.15 if j%2 else 0)+random.Random(seed+i+9*j).uniform(-.05,.05),y0+.14+j*.26+random.Random(seed+7*i+j).uniform(-.04,.04)) for j in range(3) for i in range(7)]
    return s+'\n'.join(disc(x,y,.095) for x,y in pts)
SK11=tk(enj(1.4,True,41)+enj(0,False,5)+'\\node[font=\\small\\bfseries,anchor=east] at (-.6,1.85) {X};\\node[font=\\small\\bfseries,anchor=east] at (-.6,.45) {Y};')
d={'I':(True,'gaz tanecikleri arasındaki boşluk çok büyüktür; bu yüzden gaz kolay sıkıştırılabilir'),
   'II':(False,'gaz sıkıştırılınca taneciklerin kendisi küçülmez; yalnız aralarındaki uzaklık azalır'),
   'III':(True,'sıvı tanecikleri birbirine çok yakındır; aralarındaki boşluk çok az olduğundan sıvılar neredeyse sıkıştırılamaz')}
r=onc_t(d,2)
q('0011',ad=[A('Şekli yorumla','X’te tanecikler seyrek ve uzak, Y’de sıkı ve birbirine çok yakın çizilmiştir.','X: gaz · Y: sıvı'),adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),A('Sonucu yaz','Doğru olan öncüller bir arada yazılır.',oy(d)+' · Sonuç: I ve III')],
 tipId='km-hl2-gaz',tip='Enjektörde gaz ve sıvının sıkıştırılması',z='kolay',alt='Gazlar',kaz='Gaz ve sıvıların sıkıştırılabilirliğini tanecik modeliyle açıklar.',kalip='şekilli',
 kart='K-KMHL2-11 (gazların sıkıştırılabilirliği) · iki enjektör, gaz ve sıvı',
 metin='Özdeş iki enjektörün ağzı kapatılıyor; X enjektörünün içinde bir gaz, Y enjektörünün içinde bir sıvı bulunmaktadır. Şekilde tanecik modelleri gösterilmiştir. Her iki enjektörün pistonu, aynı büyüklükte kuvvetle içeri doğru itiliyor; X’teki piston belirgin biçimde ilerlerken Y’deki piston neredeyse hiç ilerlemiyor.\nI. Gaz tanecikleri arasındaki boşluk çok büyük olduğundan X’teki gaz kolay sıkıştırılır.\nII. X’teki gaz sıkıştırılırken gaz taneciklerinin kendisi küçülür.\nIII. Y’deki sıvının tanecikleri birbirine çok yakın olduğundan sıvı neredeyse sıkıştırılamaz.\nBuna göre hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan öncüller.',
 ip=['Pistonlar içeri itilirken her enjektörde hacmi neyin azaltabileceğini düşün.'],
 bilgi=[B('Sıkıştırılabilirlik','gazlarda tanecikler arası boşluk çok büyüktür; gaz kolay sıkıştırılır ve bu sırada yalnız tanecikler arası uzaklık azalır. Sıvı ve katılarda tanecikler birbirine yakındır; bunlar çok zor sıkıştırılır. Örnek: bisiklet pompasındaki hava sıkıştırılır')],
 puf='Gaz sıkıştırılınca taneciklerin boyu değişmez, aralarındaki uzaklık azalır; sıvı ve katı bu boşluğun azlığı nedeniyle sıkıştırılamaz.',sekil=SK11)

# ============================================================ 12 · difüzyon tablosu
tb12=[('K','10','90'),('L','25','75'),('M','40','60')]
SK12=tablo_svg(['Oda','Sıcaklık (°C)','Kokunun öğrenciye ulaşma süresi (s)'],[list(s) for s in tb12])
assert [int(s[2]) for s in tb12]==sorted([int(s[2]) for s in tb12],reverse=True)
d12=tek_t(('Sıcaklık arttıkça gaz tanecikleri daha hızlı hareket ettiğinden difüzyon hızlanır.',''),[
 ('Soğuk odada gaz tanecikleri hareketsiz kaldığı için koku geç yayılmıştır.','gaz tanecikleri her sıcaklıkta sürekli hareket eder; soğukta yalnızca daha yavaş hareket ederler'),
 ('Difüzyon yalnız gazlarda gerçekleşir, sıvılarda gerçekleşmez.','difüzyon sıvılarda da gerçekleşir; yalnız gazlardakinden daha yavaştır'),
 ('M odasında koku daha çabuk ulaşmıştır çünkü bu odada gaz tanecikleri arasındaki boşluk daha azdır.','odaların hacmi aynıdır; süre farkı taneciklerin hızı farkından kaynaklanır'),
 ('Gaz tanecikleri soğuk odada daha büyük olduğu için koku daha geç ulaşmıştır.','gaz taneciklerinin büyüklüğü sıcaklıkla değişmez; süre farkı taneciklerin hız farkından kaynaklanır')],0)
q('0012',ad=[A('Tabloyu oku','Sıcaklık arttıkça kokunun ulaşma süresi kısalıyor.','10 °C: 90 s · 25 °C: 75 s · 40 °C: 60 s'),A('Nedeni bul','Sıcak gazın tanecikleri daha hızlı hareket eder ve daha çabuk yayılır.','sıcaklık ↑ → hız ↑ → süre ↓'),A('İfadeleri ele','Soğukta hareketin durmadığı ve odaların aynı olduğu unutulmaz.','B, C, D, E yanlış'),A('Sonucu yaz','Doğru ifadeyi veren şık seçilir.','A')],
 tipId='km-hl2-difuzyon',tip='Sıcaklığa göre difüzyon süresi',z='kolay',alt='Gazlar',kaz='Gazlarda difüzyonun sıcaklıkla ilişkisini yorumlar.',kalip='tablo',
 kart='K-KMHL2-12 (difüzyon) · üç odada koku yayılma süresi',
 metin='Rüzgârsız ve hacimleri eşit üç kapalı odanın sıcaklıkları birbirinden farklıdır. Her odada, bir noktadan aynı miktarda kokulu bir gaz bırakılıyor ve bu noktadan aynı uzaklıkta duran öğrencinin kokuyu ilk fark etme süresi ölçülüyor. Sonuçlar tabloda verilmiştir.\nBuna göre aşağıdakilerden hangisi söylenebilir?',
 sekil=SK12,dogru=d12['dogru'],yan=d12['yan'],sira=d12['sira'],istenen='Tablodan söylenebilecek doğru ifade.',
 ip=['Gaz taneciklerinin hareketinin sıcaklıkla nasıl değiştiğini düşün.'],
 bilgi=[B('Difüzyon','difüzyon, taneciklerin sürekli hareketi sonucu kendiliğinden yayılmasıdır. Gazlarda ve sıvılarda gerçekleşir; sıcaklık arttıkça hızlanır. Örnek: sıcak odada parfüm kokusu daha çabuk yayılır')],
 puf='Gaz tanecikleri her sıcaklıkta hareket eder; sıcaklık arttıkça hızlanır ve difüzyon hızlanır.')

# ============================================================ 13 · saf madde ve karışım ısıtma grafiği
sx,sy=.5,.034
X13=[(0,20),(2,50),(6,50),(9,80),(13,80),(15,95)]
Y13=[(0,20),(2,40),(7,62),(10,86),(14,98),(15,102)]
assert seviye(X13,4)==50 and seviye(X13,11)==80
g=eksen(15,110,range(0,16,2),[20,40,60,80,100],'Zaman (dk)','Sıcaklık (°C)',sx,sy)
g+=egri(X13,sx,sy,'vurgu,very thick')+egri(Y13,sx,sy,'thick')
g+=f'\\node[vurgu,font=\\small\\bfseries] at ({15*sx+.25:.2f},{95*sy-.12:.2f}) {{X}};\\node[font=\\small\\bfseries] at ({15*sx+.25:.2f},{102*sy+.12:.2f}) {{Y}};'
SK13=tk(g)
d={'I':(True,'saf maddede hâl değişimi sırasında sıcaklık sabit kalır; X’in sıcaklığı 2–6. ve 9–13. dakikalarda sabittir'),
   'II':(False,'Y’de hâl değişimi sırasında sıcaklık sabit kalmadığından Y’nin erime sıcaklığı tek bir değer değildir; sıcaklık 40 °C’den 62 °C’ye kadar değişir'),
   'III':(True,'4. dakika X’in sabit sıcaklıkta eridiği aralıktadır; bu aralıkta X hem katı hem sıvı hâldedir'),
   'IV':(True,'karışımlarda kaynama sırasında sıcaklık sabit kalmaz, artar; Y’nin 10–14. dakikalarda yükselmesi bunu gösterir')}
r=onc_t(d,4)
q('0013',ad=[A('Maddeleri tanı','Saf madde hâl değişiminde sabit sıcaklık gösterir; karışım göstermez.','X: yatay aralıklar var → saf · Y: yok → karışım'),adim_onc(d,['I','III'],'I ve III. öncüller'),adim_onc(d,['II']),adim_onc(d,['IV']),A('Sonucu yaz','Doğru olan öncüller bir arada yazılır.',oy(d)+' · Sonuç: I, III ve IV')],
 tipId='km-hl2-egri',tip='Saf madde ve karışımın ısıtma grafiğini karşılaştırma',z='zor',alt='Hâl Değişimleri',kaz='Saf madde ve karışımın ısıtma grafiğini hâl değişimi açısından karşılaştırır.',kalip='grafik',
 kart='K-KMHL2-13 (saf madde ve karışım grafiği) · X saf, Y karışım',
 metin='Katı hâldeki X ve Y maddelerinden biri saf madde, diğeri ise homojen bir katı karışımdır. Eşit kütlelerdeki X ve Y, aynı güçteki ısıtıcılarla ısıtılıyor ve sıcaklıklarının zamanla değişimi şekildeki grafikte veriliyor. Isıtma sırasında maddelerin tepkime vermediği ve kütle kaybetmediği kabul edilecektir.\nI. X saf maddedir.\nII. Y’nin erime sıcaklığı 40 °C’dir.\nIII. 4. dakikada X hem katı hem sıvı hâldedir.\nIV. Y’nin 10–14. dakikalar arasında kaynadığı varsayılırsa bu aralıkta sıcaklığının artması Y’nin karışım olduğunu gösterir.\nBuna göre hangileri doğrudur?',
 sekil=SK13,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Grafiğe göre doğru olan öncüller.',
 ip=['Hangi maddenin hâl değişimi sırasında sıcaklığının sabit kaldığına bak.'],
 bilgi=[B('Saf madde ve karışım','saf madde hâl değiştirirken sıcaklığı sabit kalır. Karışım hâl değiştirirken sıcaklığı sabit kalmaz; erime ve kaynama bir sıcaklık aralığında gerçekleşir. Örnek: buz 0 °C’de erirken sıcaklık sabittir, tuzlu su kaynarken sıcaklığı yavaşça artar')],
 puf='Hâl değişimi sırasında sıcaklık sabit kalıyorsa madde saftır; sıcaklık değişiyorsa karışımdır.')

# ============================================================ 14 · soğutma grafiği, yalnız sıvı süresi
sx,sy=.5,.034
S14=[(0,110),(3,80),(7,80),(12,20),(17,20),(20,5)]
assert seviye(S14,5)==80 and seviye(S14,15)==20
yog=(3,7); sivi=(7,12); don=(12,17)
dogru14=sivi[1]-sivi[0]; assert dogru14==5
assert yog[1]-yog[0]==4 and sivi[1]-yog[0]==9 and don[1]-sivi[0]==10 and don[1]-yog[0]==14
g=eksen(20,115,range(0,21),[20,80,110],'Zaman (dk)','Sıcaklık (°C)',sx,sy)+egri(S14,sx,sy,'vurgu,very thick')
for _t in (3,7,12,17): g+=f'\\draw[dashed,gray] ({_t*sx:.2f},0) -- ({_t*sx:.2f},{seviye(S14,_t)*sy:.2f});'
SK14=tk(g)
q('0014',ad=[A('Yatay bölgeleri bul','Soğutmada sıcaklığın sabit kaldığı aralıklar hâl değişimidir.','3–7. dk: yoğuşma (80 °C) · 12–17. dk: donma (20 °C)'),A('Yalnız sıvı aralığı','Yoğuşma bitince madde tamamen sıvıdır; donma başlayınca sıvı ile katı birlikte bulunur.','sıvı: 7–12. dk'),A('Süreyi hesapla','Aralığın uzunluğu bulunur.','12 − 7 = 5 dk')],
 tipId='km-hl2-sogutma',tip='Soğutma grafiğinden hâl süresi okuma',z='orta',alt='Hâl Değişimleri',kaz='Saf maddenin soğutma grafiğinde hâlleri ve hâl değişimi aralıklarını belirler.',kalip='grafik',
 kart='K-KMHL2-14 (soğutma grafiği) · gazdan katıya soğutma, yalnız sıvı süresi',
 dogru=5,yan=[(4,'Yoğuşma aralığının (3–7. dk) uzunluğunu sıvı hâlde kalma süresi sanmış.','dikkat'),(9,'Yoğuşma başladığı andan (3. dk) donmanın başladığı ana (12. dk) kadar olan süreyi almış; yoğuşma sırasında gazın da bulunduğunu görmemiş.','bilgi'),(10,'Yoğuşmanın bittiği andan (7. dk) donmanın bittiği ana (17. dk) kadar sürenin tamamını almış; donma sırasında katının da bulunduğunu görmemiş.','bilgi'),(14,'Yoğuşmanın başladığı andan donmanın bittiği ana kadar olan süreyi (3–17. dk) almış.','islem')],
 metin='Gaz hâldeki saf X maddesi, kapalı bir kapta sabit güçlü bir soğutucuyla soğutuluyor ve sıcaklığının zamanla değişimi şekildeki grafikte veriliyor. Soğutma boyunca maddenin kaptan kaybolmadığı ve kapta başka bir madde bulunmadığı kabul edilmektedir. Grafikteki yatay aralıklarda madde iki hâlde birlikte bulunmaktadır.\nBuna göre X maddesi kaç dakika boyunca yalnız sıvı hâldedir?',
 sekil=SK14,istenen='X’in yalnız sıvı hâlde bulunduğu süre (dk).',
 ip=['Sıcaklığın sabit kaldığı iki aralığın hangi hâl değişimlerine karşılık geldiğini belirle.'],
 bilgi=[B('Soğutma grafiği','saf maddede hâl değişimi sırasında sıcaklık sabit kalır. Gazın soğutulmasında ilk yatay aralık yoğuşma, ikincisi donmadır. Yoğuşma sırasında gaz ve sıvı, donma sırasında sıvı ve katı birlikte bulunur')],
 puf='Yalnız tek hâl, iki yatay (hâl değişimi) aralığı arasında kalan eğimli kısımdır.')

# ============================================================ 15 · gaz basıncı (nitel)
tb15=[('27','100'),('77','117'),('127','133')]
SK15=tablo_svg(['Sıcaklık (°C)','Gaz basıncı (kPa)'],[list(s) for s in tb15])
assert [int(b) for _,b in tb15]==sorted(int(b) for _,b in tb15)
d15=tek_t(('Gaz tanecikleri ısınınca genleşip büyüdüğünden gazın basıncı artmıştır.','gaz taneciklerinin kendisi ısınmayla büyümez; basıncı artıran, taneciklerin daha hızlı hareket etmesidir'),[
 ('Sıcaklık arttıkça gaz tanecikleri kabın duvarına daha sık ve daha şiddetli çarpar.','ısınan gaz tanecikleri hızlanır ve duvara daha sık, daha şiddetli çarpar'),
 ('Kap kapalı ve sızdırmaz olduğundan gaz taneciklerinin sayısı ısıtma boyunca değişmez.','kap kapalı olduğundan tanecik sayısı sabittir'),
 ('Gaz basıncı, taneciklerin kabın duvarına çarpmasıyla oluşur.','gaz basıncı tanecik çarpmalarından kaynaklanır'),
 ('Bu kapta gazın basıncı, 27 °C’den 127 °C’ye ısıtıldığında artmıştır.','tabloda 27 °C’de 100 kPa olan basınç, 127 °C’de 133 kPa olmuştur')],2,False)
q('0015',ad=[A('Tabloyu oku','Hacim sabitken sıcaklık arttıkça basınç da artıyor.','27 °C: 100 kPa · 77 °C: 117 kPa · 127 °C: 133 kPa'),A('Nedeni bul','Basınç, taneciklerin duvara çarpmasıyla oluşur; ısınan tanecikler hızlanır.','sıcaklık ↑ → hız ↑ → çarpma ↑ → basınç ↑'),A('İfadeleri ele','Kap kapalı olduğundan tanecik sayısı sabittir ve taneciklerin boyu ısınmayla değişmez.','sayı sabit · boy sabit · hız artıyor'),A('Hatalı ifadeyi bul','Taneciklerin büyüdüğünü söyleyen ifade yanlıştır.','büyüme ifadesi: yanlış')],
 tipId='km-hl2-gaz',tip='Gazların özellikleri',z='kolay',alt='Gazların Genel Özellikleri',kaz='Gaz basıncının oluşumunu ve sıcaklıkla değişimini tanecik modeliyle açıklar.',kalip='tablo',
 kart='K-KMHL2-15 (gaz basıncı) · kapalı kapta ısıtılan gaz',
 metin='Hacmi değişmeyen, kapalı ve sızdırmaz bir kapta sabit miktarda gaz bulunmaktadır. Kap yavaşça ısıtılırken gazın basıncı bir manometre ile üç farklı sıcaklıkta ölçülüyor ve sonuçlar tabloda veriliyor.\nBu sonuçlara göre ve gaz tanecik modeline göre aşağıdakilerden hangisi söylenemez?',
 sekil=SK15,dogru=d15['dogru'],yan=d15['yan'],sira=d15['sira'],istenen='Söylenemeyecek ifade.',
 ip=['Kap kapalı olduğuna göre ısınırken nelerin değiştiğini, nelerin sabit kaldığını ayır.'],
 bilgi=[B('Gaz basıncı','gaz tanecikleri sürekli hareket eder ve kabın duvarlarına çarpar; bu çarpmalar gaz basıncını oluşturur. Tanecikler ne kadar hızlıysa çarpmalar o kadar sık ve şiddetlidir. Örnek: bisiklet lastiğinin içindeki hava, lastiğin iç yüzeyine sürekli çarpar')],
 puf='Gaz basıncı, tanecik çarpmalarından doğar; kapalı kapta sıcaklık artınca yalnız taneciklerin hızı artar.')

# ============================================================ 16 · viskozite bilye düşme tablosu
tb16=[('X','4','3'),('Y','12','7'),('Z','30','16')]
SK16=tablo_svg(['Sıvı','20 °C’de düşme süresi (s)','40 °C’de düşme süresi (s)'],[list(s) for s in tb16])
assert all(int(a)>int(b) for _,a,b in tb16) and max(tb16,key=lambda s:int(s[1]))[0]=='Z' and int(tb16[0][2])<int(tb16[1][2])
d={'I':(True,'bilyenin en geç indiği sıvı, akmaya karşı direnci (viskozitesi) en büyük olan sıvıdır; 20 °C’de bu sıvı Z’dir'),
   'II':(False,'sıcaklık arttıkça sıvıların viskozitesi azalır, akışkanlıkları artar; üç sıvıda da düşme süresi kısalmıştır'),
   'III':(True,'viskozitesi küçük olan sıvı daha akıcıdır; 40 °C’de X’te bilye 3 s, Y’de 7 s sürede inmiştir'),
   'IV':(False,'aynı sıcaklıkta viskozitesi büyük olan sıvıda tanecikler arası etkileşim daha kuvvetlidir; Z’nin viskozitesi X’inkinden büyüktür')}
r=onc_t(d,4)
q('0016',ad=[A('Tabloyu oku','Bilye geç iniyorsa sıvı akmaya karşı daha dirençlidir.','20 °C ve 40 °C’de düşme süresi: Z > Y > X'),adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),adim_onc(d,['IV']),A('Sonucu yaz','Doğru olan öncüller bir arada yazılır.',oy(d)+' · Sonuç: I ve III')],
 tipId='km-hl2-viskozite',tip='Bilye düşme deneyiyle viskozite',z='zor',alt='Viskozite',kaz='Sıvıların viskozitesini sıcaklık ve tanecikler arası etkileşimle ilişkilendirir.',kalip='tablo',
 kart='K-KMHL2-16 (viskozite) · bilye düşme süreleri, 20 ve 40 °C',
 metin='Aynı boyut ve kütledeki özdeş çelik bilyeler, özdeş uzun silindirlerdeki eşit hacimli X, Y ve Z sıvılarına bırakılıyor ve bilyelerin silindirdeki aynı mesafeyi inme süreleri iki ayrı sıcaklıkta ölçülüyor. Bilye ne kadar geç iniyorsa sıvının akmaya karşı direnci o kadar büyüktür. Sonuçlar tabloda verilmiştir.\nI. 20 °C’de akmaya karşı direnci en büyük sıvı Z’dir.\nII. Sıcaklık arttıkça üç sıvının da akışkanlığı azalmıştır.\nIII. 40 °C’de X sıvısının akışkanlığı Y sıvısınınkinden büyüktür.\nIV. Z sıvısının tanecikleri arasındaki etkileşim, X sıvısınınkinden daha zayıftır.\nBuna göre hangileri doğrudur?',
 sekil=SK16,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Tabloya göre doğru olan öncüller.',
 ip=['Düşme süresi ile viskozite ve akışkanlık arasındaki ilişkiyi kur; sonra sıcaklığın etkisine bak.'],
 bilgi=[B('Viskozite','viskozite, bir sıvının akmaya karşı direncidir. Tanecikler arası etkileşim arttıkça artar, sıcaklık arttıkça azalır. Akışkanlık viskozitenin tersidir. Örnek: bal, soğukken sıcağa göre daha yavaş akar')],
 puf='Bilye geç iniyorsa viskozite büyüktür; sıcaklık artınca viskozite azalır, akışkanlık artar.')

# ============================================================ 17 · plazma örnekleri
d={'I':(False,'plazma doğada da bulunur; yıldızlar, şimşek ve kutup ışıkları plazma hâlindedir'),
   'II':(True,'neon tabelalarında ve floresan lambalarda ışık yayan iyonlaşmış gaz plazma hâlindedir'),
   'III':(False,'soğuk yüzeyde oluşan su damlacıkları sıvı hâldedir; plazma, iyonlaşmış bir gazdır')}
r=onc_t(d,1)
q('0017',ad=[adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),A('Sonucu yaz','Doğru olan öncüller bir arada yazılır.',oy(d)+' · Sonuç: Yalnız II')],
 tipId='km-hl2-plazma',tip='Plazma hâli ve örnekleri',z='kolay',alt='Plazma',kaz='Plazma hâlini ve günlük hayattaki örneklerini tanır.',kalip='öncüllü',
 kart='K-KMHL2-17 (plazma örnekleri) · neon tabelası, floresan lamba',
 metin='Bir öğrenci, evrendeki görünür maddenin büyük bölümünün plazma hâlinde bulunduğunu okuyor ve plazma ile ilgili günlük hayattan örnekler araştırıyor. Çalışmasında şu ifadeleri kullanıyor.\nI. Plazma hâlindeki madde yalnız laboratuvarda elde edilebilir, doğada bulunmaz.\nII. Neon tabelalarındaki ışık yayan gaz plazma hâlindedir.\nIII. Soğuk bir bardağın dış yüzeyinde oluşan su damlacıkları plazma hâlindedir.\nBuna göre hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan ifadeler.',
 ip=['Plazma hâlini oluşturan taneciklerin özelliğini ve günlük hayattaki yerini her öncül için ayrı ayrı sorgula.'],
 bilgi=[B('Plazma','plazma, iyonlaşmış gazdır; iyonlar ve serbest elektronlar içerir, elektriği iletir ve ışık yayabilir. Örnek: yıldızlar, şimşek, neon tabelası, floresan lamba')],
 puf='Plazma yüklü taneciklerden oluşan iletken bir hâldir; ışık yayan neon ve floresan lambalarda bulunur.')

# ============================================================ 18 · yüzey gerilimi
ARR2='-{Stealth[length=3mm,width=2.6mm]}'
def ok_(x,y,ang,L=.7,r=.17):
    a=math.radians(ang); return f'\\draw[vurgu,thick,{ARR2}] ({x+r*math.cos(a):.3f},{y+r*math.sin(a):.3f}) -- ({x+(r+L)*math.cos(a):.3f},{y+(r+L)*math.sin(a):.3f});'
Ax,Ay=1.7,1.5; Bx,By=4.4,2.95
gg='\\draw[thick] (0,4.3) -- (0,0) -- (6,0) -- (6,4.3);\\draw[thick,dashed] (0,3.7) -- (6,3.7);'
gg+='\\node[font=\\normalsize\\bfseries] at (3,.5) {sıvı};\\node[font=\\normalsize\\bfseries] at (3,4.0) {gaz (hava)};'
Aang=[0,60,120,180,240,300]; Bang=[0,180,225,270,315]
for a in Aang:
    gg+=ok_(Ax,Ay,a)+disc(Ax+.95*math.cos(math.radians(a)),Ay+.95*math.sin(math.radians(a)),.17,'gray!25')
for a in Bang:
    gg+=ok_(Bx,By,a)+disc(Bx+.95*math.cos(math.radians(a)),By+.95*math.sin(math.radians(a)),.17,'gray!25')
gg=gg.replace('gray!25','gray!25')
gg+=disc(Ax,Ay,.17,'vurgu!45')+disc(Bx,By,.17,'vurgu!45')
gg+=f'\\node[font=\\small\\bfseries] at ({Ax-.55*math.sqrt(3)/2*1.0:.2f},{Ay+.3:.2f}) {{A}};\\node[font=\\small\\bfseries] at ({Bx},{By+.47}) {{B}};'
assert all(math.sin(math.radians(a))<=0 for a in Bang if a not in (0,180)) and (Bx,By)[1]<3.7
SK18=tk(gg)
d={'I':(False,'sıvının iç kısmındaki molekülü her yönden eşit sayıda molekül çeker; bu nedenle A’ya etki eden net çekim kuvveti sıfırdır'),
   'II':(True,'yüzeydeki molekülü üstten çeken sıvı molekülü yoktur; B’ye etki eden net çekim kuvveti sıvının iç kısmına doğrudur'),
   'III':(True,'sıcaklık arttıkça moleküller arası çekim etkisi azalır ve sıvının yüzey gerilimi azalır'),
   'IV':(False,'deterjan ve sabun gibi maddeler suyun yüzey gerilimini azaltır, artırmaz')}
r=onc_t(d,4)
q('0018',ad=[A('Oklara bak','A’ya her yönden, B’ye yalnız yanlardan ve aşağıdan çekim uygulanıyor.','A: oklar dengeli · B: yukarıdan çekim yok'),adim_onc(d,['I','II'],'I ve II. öncüller'),adim_onc(d,['III']),adim_onc(d,['IV']),A('Sonucu yaz','Doğru olan öncüller bir arada yazılır.',oy(d)+' · Sonuç: II ve III')],
 tipId='km-hl2-yuzey',tip='Yüzey gerilimi ve molekül çekimleri',z='orta',alt='Yüzey Gerilimi',kaz='Yüzey geriliminin moleküller arası çekimlerle ilişkisini açıklar.',kalip='öncüllü',
 kart='K-KMHL2-18 (yüzey gerilimi) · iç ve yüzey molekülü çekim okları',
 metin='Şekilde bir sıvının iç kısmındaki A molekülü ile sıvı–gaz ara yüzeyindeki B molekülüne, çevresindeki sıvı moleküllerinin uyguladığı çekim kuvvetleri eşit uzunlukta oklarla gösterilmiştir. Sıvı yüzeyinin gerilmiş bir zar gibi davranmasına yüzey gerilimi denir.\nI. A molekülüne etki eden net çekim kuvveti sıvının iç kısmına doğrudur.\nII. B molekülüne etki eden net çekim kuvveti sıvının iç kısmına doğrudur.\nIII. Sıcaklık arttıkça sıvının yüzey gerilimi azalır.\nIV. Su yüzeyine deterjan eklenmesi suyun yüzey gerilimini artırır.\nBuna göre hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan öncüller.',
 ip=['Her molekülün çevresindeki oklara bak: çekimler dengeleniyor mu, yoksa bir yöne mi net kuvvet kalıyor?'],
 bilgi=[B('Yüzey gerilimi','sıvının iç kısmındaki molekülü her yönden komşu moleküller çeker, net kuvvet sıfırdır. Yüzeydeki molekül ise yalnız yanlardan ve içeriden çekilir; net kuvvet içeri doğrudur. Bu yüzden yüzey küçülmeye çalışır. Sıcaklık arttıkça yüzey gerilimi azalır. Örnek: su damlası küre biçimini almaya çalışır')],
 puf='Yüzeydeki molekül içe doğru net kuvvetle çekilir; sıcaklık ve deterjan yüzey gerilimini azaltır.',sekil=SK18)

# ============================================================ 19 · hâl değişimi şeması
num={'1':('sıvı','gaz'),'2':('katı','sıvı'),'3':('gaz','sıvı'),'4':('sıvı','katı'),'5':('gaz','katı'),'6':('katı','gaz')}
sira_h={'katı':0,'sıvı':1,'gaz':2}
alir={k for k,(a,b) in num.items() if sira_h[b]>sira_h[a]}
assert alir=={'1','2','6'}
g='\\node[draw,thick,rounded corners,minimum width=1.7cm,minimum height=.8cm] (K) at (0,0) {Katı};\\node[draw,thick,rounded corners,minimum width=1.7cm,minimum height=.8cm] (S) at (4,0) {Sıvı};\\node[draw,thick,rounded corners,minimum width=1.7cm,minimum height=.8cm] (G) at (8,0) {Gaz};'
g+=f'\\draw[{ARR},thick] (.95,.17) -- node[above] {{2}} (3.05,.17);\\draw[{ARR},thick] (3.05,-.17) -- node[below] {{4}} (.95,-.17);'
g+=f'\\draw[{ARR},thick] (4.95,.17) -- node[above] {{1}} (7.05,.17);\\draw[{ARR},thick] (7.05,-.17) -- node[below] {{3}} (4.95,-.17);'
g+=f'\\draw[{ARR},thick] (0,.5) to[out=60,in=120] node[above] {{6}} (8,.5);\\draw[{ARR},thick] (8,-.5) to[out=-120,in=-60] node[below] {{5}} (0,-.5);'
SK19=tk(g)
d19=tek_t(('1, 2 ve 6','1: sıvı→gaz (buharlaşma), 2: katı→sıvı (erime) ve 6: katı→gaz (süblimleşme) ısı alarak gerçekleşir'),[
 ('1, 3 ve 6','3 numaralı değişim gaz→sıvı (yoğuşma) olup ısı vererek gerçekleşir'),
 ('1, 2 ve 5','5 numaralı değişim gaz→katı (kırağılaşma) olup ısı vererek gerçekleşir; ısı alan üçüncü değişim 6’dır'),
 ('2, 4 ve 5','4 numaralı sıvı→katı (donma) ve 5 numaralı gaz→katı (kırağılaşma) değişimleri ısı vererek gerçekleşir'),
 ('3, 4 ve 5','3, 4 ve 5 numaralı değişimler (yoğuşma, donma, kırağılaşma) ısı vererek gerçekleşir; ısı alan değişimler 1, 2 ve 6’dır')],1)
q('0019',ad=[A('Okları adlandır','Okun yönüne göre hangi hâlden hangi hâle geçildiği belirlenir.','1: buharlaşma · 2: erime · 3: yoğuşma · 4: donma · 5: kırağılaşma · 6: süblimleşme'),A('Isı alışverişini ayır','Tanecikleri birbirinden uzaklaştıran değişimler ısı alır.','ısı alan: katı→sıvı, sıvı→gaz, katı→gaz'),A('Numaraları yaz','Isı alan değişimlerin numaraları yazılır.','1, 2 ve 6')],
 tipId='km-hl2-hal',tip='Hâl değişimi şemasında ısı alışverişi',z='kolay',alt='Hâl Değişimleri',kaz='Hâl değişimlerini ısı alan ve ısı veren olarak sınıflandırır.',kalip='şekilli',
 kart='K-KMHL2-19 (hâl değişimleri şeması) · numaralı oklarla altı hâl değişimi',
 metin='Şekilde bir saf maddenin katı, sıvı ve gaz hâlleri arasındaki dönüşümler, numaralı oklarla gösterilmiştir. Bu dönüşümlerin hepsi maddenin ortamla ısı alışverişi yapmasıyla gerçekleşmektedir. Oklar, dönüşümün yönünü göstermektedir.\nBuna göre ısı alarak gerçekleşen hâl değişimlerinin numaraları aşağıdakilerden hangisinde doğru verilmiştir?',
 dogru=d19['dogru'],yan=d19['yan'],sira=d19['sira'],istenen='Isı alarak gerçekleşen hâl değişimlerinin numaraları.',
 ip=['Her okun hangi hâlden hangi hâle gittiğini yaz.'],
 bilgi=[B('Hâl değişimleri ve ısı','erime, buharlaşma ve süblimleşme ısı alır; donma, yoğuşma ve kırağılaşma ısı verir. Örnek: buz erirken çevresinden ısı alır, çamaşırın kuruması buharlaşmadır')],
 puf='Tanecikleri birbirinden uzaklaştıran (katı→sıvı→gaz yönündeki) her hâl değişimi ısı alır.',sekil=SK19)

# ============================================================ 20 · katı tanecik modelleri
def plus(x,y,r=.15,s='+',f='vurgu!25'): return f'\\draw[thin,fill={f}] ({x:.3f},{y:.3f}) circle ({r});\\node[font=\\tiny] at ({x:.3f},{y:.3f}) {{{s}}};'
def kutu(x0,Wb=2.0,Hb=1.8): return f'\\draw[thick] ({x0},0) rectangle ({x0+Wb},{Hb});'
xs20={'K':0,'L':2.5,'M':5.0,'N':7.5}; Wb=2.0; Hb=1.8
g=''
for ad_ in xs20: g+=kutu(xs20[ad_])
# K: metalik
x0=xs20['K']
for i in range(3):
    for j in range(3): g+=plus(x0+.4+i*.6,.35+j*.55)
rng=random.Random(5)
for (x,y) in rastgele(8,x0+.2,x0+Wb-.2,.2,Hb-.2,.28,seed=3,L0=[(x0+.4+i*.6,.35+j*.55) for i in range(3) for j in range(3)]): g+=f'\\fill ({x:.3f},{y:.3f}) circle (.04);'
# L: iyonik
x0=xs20['L']
for i in range(4):
    for j in range(3): g+=(plus(x0+.35+i*.43,.35+j*.5,.17,'+') if (i+j)%2==0 else plus(x0+.35+i*.43,.35+j*.5,.17,'$-$','gray!25'))
# M: moleküler
x0=xs20['M']
for (cx,cy) in [(.5,1.35),(1.35,1.3),(.55,.45),(1.4,.5)]:
    g+=f'\\draw[thick] ({x0+cx-.12:.2f},{cy:.2f}) -- ({x0+cx+.12:.2f},{cy:.2f});'+disc(x0+cx-.12,cy,.12)+disc(x0+cx+.12,cy,.12)
# N: kovalent ağ
x0=xs20['N']
for i in range(4):
    for j in range(3):
        px,py=x0+.35+i*.43,.35+j*.55
        if i<3: g+=f'\\draw[thick] ({px:.2f},{py:.2f}) -- ({px+.43:.2f},{py:.2f});'
        if j<2: g+=f'\\draw[thick] ({px:.2f},{py:.2f}) -- ({px:.2f},{py+.55:.2f});'
for i in range(4):
    for j in range(3): g+=disc(x0+.35+i*.43,.35+j*.55,.11)
mp={'K':'1085','L':'801','M':'115','N':'1710'}
for ad_ in xs20: g+=etiket(xs20[ad_]+Wb/2,-.35,f'\\textbf{{{ad_}}}')+etiket(xs20[ad_]+Wb/2,-.8,f'{mp[ad_]} °C','[font=\\footnotesize]')
g+=etiket(4.75,-1.35,'Erime noktaları kapların altında verilmiştir. $+$ ve $-$ : zıt yüklü iyonlar, • : serbest elektron','[font=\\footnotesize]')
SK20=tk(g)
d20=tek_t(('K katı hâlde de sıvı hâlde de elektrik akımını iletir; L ise yalnız sıvı hâlde iletir.','K’de serbest elektronlar, L’de ise yalnız erimiş hâldeki serbest iyonlar iletkenlik sağlar'),[
 ('L’nin katı hâlde elektrik akımını iletmesinin nedeni, iyonlarının serbestçe hareket edebilmesidir.','L’de iyonlar katı hâlde yerlerinde sabittir; iyonlar ancak sıvı hâlde ya da çözeltide hareket edebilir'),
 ('K da L de çekiçle dövüldüğünde şekil değiştirir, kırılmaz.','K (metalik katı) dövülebilir; L (iyonik katı) ise kırılgandır ve dövülünce parçalanır'),
 ('M’nin erime noktasının N’ninkinden düşük olması, M’deki tanecikler arasındaki bağların N’dekilerden daha güçlü olmasından kaynaklanır.','M’de moleküller arasında zayıf etkileşimler, N’de atomlar arasında güçlü kovalent bağlar vardır; bu yüzden M’nin erime noktası düşüktür'),
 ('N’nin erime noktasının yüksek olması, tanecikleri arasındaki zayıf etkileşimlerin çokluğundan kaynaklanır.','N’de atomlar birbirine güçlü kovalent bağlarla bağlanmış ağ yapı oluşturur; erime noktasının yüksek olması bundandır')],3)
q('0020',ad=[A('Modelleri tanı','Serbest elektronlu pozitif örgü metalik, zıt yüklü iyon örgüsü iyonik, bağlı atom ağı kovalent ağ, ayrık atom çiftleri moleküler katıdır.','K: metalik · L: iyonik · M: moleküler · N: kovalent ağ'),A('Elektrik iletkenliğini yorumla','Metalik katı her hâlde iletir; iyonik katı yalnız iyonlar hareket ederken, yani sıvı hâlde iletir.','K: katıda ve sıvıda iletir · L: yalnız sıvıda iletir'),A('Bağ ve erime noktası','Güçlü kovalent bağlı ağ çok yüksek, zayıf etkileşimli moleküler katı düşük erime noktalıdır.','N’nin erime noktası M’ninkinden çok yüksektir'),A('İfadeleri sına','Her ifade modelle ve verilen erime noktasıyla karşılaştırılır.','doğru olanı veren ifade seçilir')],
 tipId='km-hl2-kati',tip='Katı türleri ve özellikleri',z='zor',alt='Katılar',kaz='Katı türlerinin tanecik modellerini tanıyıp özelliklerini birlikte yorumlar.',kalip='şekilli',
 kart='K-KMHL2-20 (katı türleri modelleri) · metalik, iyonik, moleküler, kovalent ağ',
 metin='Şekilde dört farklı katının tanecik modelleri, her katının erime noktasıyla birlikte gösterilmiştir. K, L, M ve N katılarının her biri farklı bir katı türüne (iyonik, metalik, kovalent ağ, moleküler) aittir. Modellerde tanecikler arasındaki bağlar ve yükler çizimde belirtilmiştir.\nBu katılarla ilgili aşağıdakilerden hangisi doğrudur?',
 sekil=SK20,dogru=d20['dogru'],yan=d20['yan'],sira=d20['sira'],istenen='Doğru olan ifade.',
 ip=['Önce her modeli hangi katı türüne ait olduğunu belirleyerek adlandır.'],
 bilgi=[B('Katı türleri','Metalik katıda pozitif yüklü atom kalıntıları serbest elektron denizi içindedir; iletken ve dövülebilirdir. İyonik katıda zıt yüklü iyonlar yerinde sabittir; katıda iletmez, sıvıda iletir, kırılgandır. Kovalent ağ katısında atomlar kovalent bağlarla bağlıdır; erime noktası çok yüksektir. Moleküler katıda zayıf etkileşimler vardır; erime noktası düşüktür')],
 puf='Önce modelden katı türünü bul; sonra o türün iletkenlik, dövülebilirlik ve erime noktası özelliklerini ifadeyle karşılaştır.')

bitir(P,'halleriki',UK)
