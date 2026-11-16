"""TYT Kimya · Karışımlar · ek paket (karisimlariki): 22 soru, kardeş yok, ipucu 1.
Şekil koordinatları ve veriler Python'da hesaplanır; TikZ bu değerlerden üretilir. Öncüllerin doğru/yanlış değeri tek yerde (d sözlüğü) tanımlanır.
Her sayısal cevap ve çeldirici değer assert edilir."""
import sys,os,math,random,itertools
GD=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,GD)
import _hafif_kim2 as H
from _hafif_kim2 import *
from _hafif_kim import onc as _onc_eski, tek
H.KONU='Karışımlar'
UK='kim|Karışımlar'
P=Parti('karisimlariki','Karışımlar',UK,ders='TYT Kimya',idon='tytkim')
KY='ÖSYM 2018–2026 TYT Kimya (yalnız mantık) · MEB 10. sınıf Karışımlar'
MAP={}
for _n,_t in [(('01','02','03'),('sinif','Karışım türleri ve sınıflandırma')),(('04','05','06'),('cozunme','Çözünme süreci ve çözünme hızı')),
              (('07','08','09'),('derisim','Kütlece ve hacimce yüzde, ppm')),(('10','11','12','13'),('seyrelt','Seyreltme, derişikleştirme ve karıştırma')),
              (('14','15','16','17'),('cozunurluk','Çözünürlük ve doygunluk')),(('18','19'),('koligatif','Koligatif özellikler')),
              (('20','21','22'),('ayirma','Karışımların ayrılması'))]:
    for _x in _n: MAP[_x]=_t
def kartla(n,alt,fikir,tuzak,z,kalip,adim):
    a,b=MAP[n]; kart(f'K-KMKR2-{n}',alt,fikir,tuzak,z,kalip,adim,f'km-kr2-{a}',b,KY)
def q(no,ad,**k):
    assert len(k['ip'])==1
    k['tipId']='km-kr2-'+MAP[no[-2:]][0]; k['tip']=MAP[no[-2:]][1]
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
kartla('01','Homojen–heterojen ve saf madde modeli','Tek tür tanecik saf maddedir; iki tür tanecik her yerde düzgün karışmışsa homojen, ayrı bölgelerde toplanmışsa heterojen karışımdır.','Karışımı tanecik sayısına ya da renge göre sınıflamak; iki katmanlı görüntüyü homojen saymak.','kolay','şekilli',3)
kartla('02','Çözelti, kolloit, süspansiyon ayrımı','Işığı saçma, süzgeçten geçme ve bekletince çökme gözlemlerinden çözelti, kolloit ve süspansiyon ayırt edilir.','Kolloidi çözelti ya da süspansiyonla karıştırmak; süspansiyonun süzgeçten geçtiğini sanmak.','orta','tablo',3)
kartla('03','Günlük hayatta karışım türleri','Sis ve duman aerosol, süt ve mayonez emülsiyon, çamurlu su süspansiyon, kolonya ve alaşım çözeltidir.','Aerosolü yalnız gaz içinde katı sanmak; çözeltiyi heterojen saymak.','kolay','öncüllü',3)
kartla('04','Çözünme ve tanecik modeli','Molekülsel katılar moleküller hâlinde, iyonik katılar iyonlarına ayrışarak çözünür; yalnız iyonlu çözelti elektriği iletir.','Şekeri de iyonlarına ayrışıyor saymak; çözünmeyi kimyasal bağların kopması sanmak.','orta','şekilli',4)
kartla('05','Benzer benzeri çözer','Polar madde polar çözücüde, apolar madde apolar çözücüde çözünür; iyonik bileşikler polar çözücüde çözünür.','Çözünmeyi yalnız kütleyle ilişkilendirmek; polar ve apolar maddenin karışmayacağını yorumlayamamak.','orta','tablo',3)
kartla('06','Çözünme hızını etkileyen etmenler','Çözünme hızı tanecik boyutu küçüldükçe, sıcaklık arttıkça ve karıştırdıkça artar; deneyde yalnız bir değişken farklı olmalıdır.','Birden çok değişkeni aynı anda farklı olan iki deneyi karşılaştırmak.','orta','tablo',3)
kartla('07','Hacimce yüzde','Hacimce yüzde derişim = çözünen hacmi ÷ çözelti hacmi × 100; çözücü hacmi çözelti hacminden çıkarılarak bulunur.','Yüzde değerini mL sanmak; çözünen yerine çözücü hacmini vermek.','kolay','şekilli',2)
kartla('08','ppm derişimi','1 ppm = 1 mg madde / 1 kg çözelti; karışımda toplam madde kütlesi toplam çözelti kütlesine bölünür.','ppm değerlerinin ortalamasını almak; mg ile kg’ı karıştırmak.','orta','tablo',3)
kartla('09','Katı ekleyerek derişim ayarlama','Katı eklenince hem çözünen hem çözelti kütlesi artar; denklem (çözünen + x) ÷ (çözelti + x) olarak kurulur.','Eklenen katıyı yalnız çözünen kütlesine eklemek.','zor','hikâyeli',4)
kartla('10','Su ekleyerek seyreltme','Seyreltmede çözünen kütlesi sabittir; yeni çözelti kütlesi çözünen ÷ yeni derişim ile bulunur.','Yüzde farkını doğrudan gram saymak; yeni çözelti kütlesini eklenen su sanmak.','kolay','hikâyeli',3)
kartla('11','Derişim–su grafiği','Su eklenirse derişim hiperbolik azalır; grafikten ilk çözelti ve çözünen kütlesi bulunur, sonra yeni hedef hesaplanır.','Derişimin su kütlesiyle doğrusal azaldığını sanmak.','zor','grafik',4)
kartla('12','Karıştırma ve buharlaştırma','İki çözeltinin çözünen kütleleri toplanır; buharlaşan yalnız su olduğundan çözelti kütlesi azalır.','Derişimlerin ortalamasını almak; buharlaşan kütleyi çözünenden düşmek.','zor','şekilli',4)
kartla('13','Derişimi artıran işlemler','Derişim; çözücü azaltılarak, çözünen eklenerek ya da daha derişik çözelti katılarak artar; aynı derişimli çözelti değiştirmez.','Aynı derişimli çözeltiyi eklemenin etkisini yanlış yorumlamak.','kolay','öncüllü',3)
kartla('14','Çözünürlük–sıcaklık grafiği','Katıların çözünürlüğü çoğunlukla sıcaklıkla artar, bazıları azalır; kesişim noktasında çözünürlükler eşittir.','Eğrinin eğimini her maddede aynı sanmak; eşit çözünürlüğü sıcaklık eşitliğiyle karıştırmak.','orta','grafik',3)
kartla('15','Doymamış ve doygun çözelti','Eğrinin altındaki miktar tamamen çözünür (doymamış); eğri üzeri doygun, eğrinin üstündeki fazla miktar dipte katı kalır.','Eğrinin üstündeki noktayı tamamen çözünmüş saymak.','orta','grafik',3)
kartla('16','Soğutmada çöken madde','Çözelti kütlesinden çözünen ve su kütlesi bulunur; soğutmada çöken miktar su kütlesi başına iki çözünürlük farkıyla hesaplanır.','Çözelti kütlesini su kütlesi sanmak; 100 g su farkını ölçeklememek.','zor','grafik',5)
kartla('17','Gaz çözünürlüğü','Gazların sudaki çözünürlüğü sıcaklık arttıkça azalır, basınç arttıkça artar; katı ve sıvıların çözünürlüğü basınçla belirgin değişmez.','Gaz çözünürlüğünü katı gibi sıcaklıkla artıyor saymak; basınç etkisini ters yorumlamak.','orta','düz',3)
kartla('18','Donma noktası alçalması','Çözünen madde donma noktasını düşürür; çözeltide donma sırasında sıcaklık sabit kalmaz; derişim arttıkça etki artar.','Tuzun donma noktasını yükselttiğini sanmak; saf madde ile çözeltinin grafiğini karıştırmak.','kolay','grafik',3)
kartla('19','Koligatif özelliklerin günlük örnekleri','Buzlanmayı önlemek için tuz, antifriz, deniz suyunun geç donması koligatiftir; yağ lekesinin benzinle çıkması çözünme polarlığıdır.','Her çözünme olayını koligatif özellik saymak.','orta','hikâyeli',3)
kartla('20','Basit damıtma düzeneği','Damıtmada kaynama noktası düşük bileşen önce buharlaşır, soğutucuda yoğuşur; termometre buharın sıcaklığını ölçer.','Termometreyi sıvıya daldırmak; ayırma hunisi ile damıtmayı karıştırmak.','orta','şekilli',3)
kartla('21','Ayırma hunisi ve özkütle','Karışmayan iki sıvıda özkütlesi büyük olan altta kalır; alt katman musluktan alınır, kütle hacim × özkütledir.','Üst ve alt katmanı özkütleye bakmadan atamak; yükseklikten hacmi bulmamak.','orta','şekilli',4)
kartla('22','Ayırma yöntemi seçimi','Yöntem, bileşenlerin farkına dayanır: mıknatıslanma, çözünürlük, kaynama noktası, özkütle ve karışmama.','Homojen sıvı karışımını ayırma hunisiyle ayrılabilir saymak.','orta','tablo',3)

# ============================================================ 01 · tanecik modeli, homojen/heterojen
W1=2.2; xs1=[0,2.8,5.6]
g=''
for x0 in xs1: g+=kap(x0,W1,2.1)
pt_x=rastgele(5,xs1[0]+.25,xs1[0]+W1-.25,.25,1.85,.5,seed=41)
pt_y=rastgele(5,xs1[0]+.25,xs1[0]+W1-.25,.25,1.85,.5,seed=42,L0=pt_x)
g+=''.join(disc(x,y,.13) for x,y in pt_x)+''.join(nokta(x,y,.07) for x,y in pt_y)
g+=''.join(disc(x,y,.13) for x,y in rastgele(8,xs1[1]+.25,xs1[1]+W1-.25,.25,1.85,.5,seed=43))
Mx=rastgele(5,xs1[2]+.25,xs1[2]+W1-.25,.25,.85,.5,seed=44)
My=rastgele(5,xs1[2]+.25,xs1[2]+W1-.25,1.25,1.85,.5,seed=45)
g+=f'\\draw[thick] ({xs1[2]},1.05) -- ({xs1[2]+W1},1.05);'
g+=''.join(disc(x,y,.13) for x,y in Mx)+''.join(nokta(x,y,.07) for x,y in My)
for ad_,x0 in zip('KLM',xs1): g+=f'\\node at ({x0+W1/2},-.35) {{\\textbf{{{ad_}}}}};'
g+='\\draw[thin,fill=vurgu!25] (.3,-1.05) circle (.13);\\node[right,font=\\footnotesize] at (.5,-1.05) {X taneciği};'
g+='\\fill (2.9,-1.05) circle (.07);\\node[right,font=\\footnotesize] at (3.05,-1.05) {Y taneciği};'
SK1=tk(g)
d={'I':(True,'iki tür tanecik kabın her yerinde düzgün karıştığından tek faz görülür ve karışım homojendir'),
   'II':(True,'yalnız bir tür taneciğin bulunduğu madde saf maddedir'),
   'III':(False,'iki tür tanecik ayrı bölgelerde toplanmıştır; arada sınır bulunduğundan karışım heterojendir')}
r=onc_t(d,1)
q('0001',ad=[A('Kaplardaki taneciklere bak','Her kapta kaç tür tanecik olduğuna ve nasıl dağıldığına bakılır.','K: iki tür, düzgün dağılmış · L: tek tür · M: iki tür, iki bölge'),adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),A('Sonucu yaz','Doğru olan öncüller bir arada yazılır.',oy(d)+' · Sonuç: I ve II')],
 alt='Homojen ve Heterojen Karışımlar',z='kolay',kaz='Tanecik modelinden saf madde, homojen ve heterojen karışımı ayırt eder.',kalip='şekilli',
 kart='K-KMKR2-01 (homojen–heterojen, saf madde modeli) · K, L, M kapları',
 metin='Aynı sıcaklıktaki özdeş üç kapta bulunan sıvı maddelerin tanecik modelleri şekilde verilmiştir. Çizimlerde iki ayrı saf maddeye ait X ve Y tanecikleri gösterilmiş, tanecik dağılımları kaplardaki gerçek durumu yansıtacak biçimde çizilmiştir.\nI. K kabındaki madde homojen karışımdır.\nII. L kabındaki madde saf maddedir.\nIII. M kabındaki madde homojen karışımdır.\nBuna göre hangileri doğrudur?',
 sekil=SK1,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan öncüller.',
 ip=['Önce her kapta kaç tür tanecik bulunduğunu, sonra bu taneciklerin kabın içinde nasıl dağıldığını incele.'],
 bilgi=[B('Saf madde ve karışım','Saf madde tek tür tanecikten oluşur. Karışımda en az iki tür tanecik vardır; her yerde aynı dağılım varsa homojen, bölgelere ayrılmışsa heterojendir. Örnek: şekerli su homojen, yağ–su karışımı heterojendir')],
 puf='Tek tür tanecik saf maddeyi; iki tür taneciğin her yerde düzgün karışması homojen, ayrı bölgelerde toplanması heterojen karışımı gösterir.')

# ============================================================ 02 · kolloit tablo
TAB2=[('X','hayır','evet','hayır'),('Y','evet','evet','hayır'),('Z','evet','hayır','evet')]
SK2=tablo_svg(['Karışım','Işığı saçar mı?','Süzgeçten geçer mi?','Bekletince çöker mi?'],[list(s) for s in TAB2])
def s2(a,b,c): return f'X: {a}, Y: {b}, Z: {c}'
d2=tek_t((s2('çözelti','kolloit','süspansiyon'),''),[
 (s2('kolloit','çözelti','süspansiyon'),'çözelti ışık demetini saçmaz; ışığı saçan Y çözelti olamaz, ışığı saçmayan X ise kolloit değildir'),
 (s2('çözelti','süspansiyon','kolloit'),'süspansiyon süzgeç kâğıdından geçemez ve bekletilince çöker; bu özellikler Z’ye aittir, Y ise bekletilince çökmediği için süspansiyon olamaz'),
 (s2('süspansiyon','kolloit','çözelti'),'süzgeçten geçen ve bekletilince çökmeyen X süspansiyon değildir; çökeni ve süzgeçte kalanı Z’dir, bu da çözelti olamaz'),
 (s2('kolloit','süspansiyon','çözelti'),'bekletince çökmeyen Y süspansiyon olamaz; ışığı hiç saçmayan X de kolloit olamaz')],0)
q('0002',ad=[A('Işığı saçmayanı bul','Çözelti ışık demetini saçmaz, tanecikleri çok küçüktür.','X: ışığı saçmıyor → çözelti'),A('Kolloidi ayır','Kolloit ışığı saçar, süzgeçten geçer ve bekletilince çökmez.','Y: saçar, geçer, çökmez → kolloit'),A('Süspansiyonu ayır','Süspansiyon iri tanecikli olduğundan süzgeçte kalır ve zamanla çöker.','Z: geçmez, çöker → süspansiyon'),A('Şıkları karşılaştır','Üç sonucu birlikte veren şık seçilir.','X: çözelti · Y: kolloit · Z: süspansiyon')],
 alt='Homojen ve Heterojen Karışımlar',z='orta',kaz='Gözlem sonuçlarından çözelti, kolloit ve süspansiyonu ayırt eder.',kalip='tablo',
 kart='K-KMKR2-02 (çözelti–kolloit–süspansiyon) · X, Y, Z gözlem tablosu',
 metin='Bir laboratuvarda X, Y ve Z karışımları ayrı ayrı hazırlanmış; her biri, aynı koşullarda ışık demetinden geçirilmiş, süzgeç kâğıdından süzülmüş ve uzun süre hareketsiz bekletilmiştir. Üç karışımın da çözelti, kolloit ya da süspansiyon olduğu bilinmekte, gözlem sonuçları tabloda verilmektedir.\nBuna göre X, Y ve Z karışımları aşağıdakilerden hangisinde doğru sınıflandırılmıştır?',
 sekil=SK2,dogru=d2['dogru'],yan=d2['yan'],sira=d2['sira'],istenen='X, Y ve Z karışımlarının türleri.',
 ip=['Üç gözlemin her biri hangi karışım türünü diğerlerinden ayırıyor, önce bunu düşün.'],
 bilgi=[B('Çözelti, kolloit, süspansiyon','Çözelti ışığı saçmaz, süzgeçten geçer, çökmez (şekerli su). Kolloit ışığı saçar, süzgeçten geçer, çökmez (jelatin çözeltisi). Süspansiyon ışığı saçar, süzgeçte kalır, bekletilince çöker (kireçli su)')],
 puf='Işığı saçmayan çözelti; saçıp süzgeçten geçen ve çökmeyen kolloit; süzgeçte kalıp çöken süspansiyondur.')

# ============================================================ 03 · günlük karışımlar
d={'I':(True,'sis, gaz ortamında dağılmış sıvı damlacıklarından oluşan bir aerosoldür'),
   'II':(False,'kolonya, etil alkolün suda ve diğer maddelerde tamamen çözünmesiyle oluşan tek fazlı homojen karışımdır (çözeltidir)'),
   'III':(True,'zeytinyağı ile su çalkalanınca küçük damlacıklar oluşur, bu emülsiyon bekletilince katmanlara ayrılır')}
r=onc_t(d,2)
q('0003',ad=[adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),A('Sonucu yaz','Doğru olan öncüller bir arada yazılır.',oy(d)+' · Sonuç: I ve III')],
 alt='Homojen ve Heterojen Karışımlar',z='kolay',kaz='Günlük hayattaki karışımları türlerine göre sınıflandırır.',kalip='öncüllü',
 kart='K-KMKR2-03 (günlük karışım türleri) · sis, kolonya, zeytinyağı–su',
 metin='Fen bilimleri öğretmeni, öğrencilerinden günlük hayatta karşılaştıkları karışımların türleri hakkında yorum yapmalarını istiyor. Öğrenciler sabah yoğun sis görmüş, evlerinde kolonya kullanmış ve salata sosu hazırlarken zeytinyağı ile suyu çalkalamıştır.\nI. Sis, gaz içinde dağılmış sıvı damlacıklarından oluşan bir aerosoldür.\nII. Kolonya, heterojen bir karışımdır.\nIII. Çalkalanan zeytinyağı–su karışımı, bekletilince katmanlara ayrılan bir emülsiyondur.\nBuna göre hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan öncüller.',
 ip=['Her örnekte dağılan maddenin ve içinde dağıldığı ortamın hâlini düşün; tek fazlı olup olmadığına bak.'],
 bilgi=[B('Karışım türleri','Aerosol: gaz içinde katı ya da sıvı taneciklerin dağılması (deodorant spreyi). Emülsiyon: birbirinde çözünmeyen iki sıvının karışımı (süt). Süspansiyon: sıvı içinde bekletince çöken katı (kum–su). Çözelti: tek fazlı, homojen karışım (limonata)')],
 puf='Gaz içinde dağılan sıvı ya da katı aerosol, karışmayan iki sıvı emülsiyon, tek fazlı karışım çözeltidir.')

# ============================================================ 04 · çözünme tanecik modeli
W4=2.4; xs4=[0,3.2]
g=kap(xs4[0],W4,2.1)+kap(xs4[1],W4,2.1)
sek=rastgele(5,xs4[0]+.3,xs4[0]+W4-.3,.3,1.8,.6,seed=51)
for x,y in sek: g+=f'\\draw[thin,fill=vurgu!25] ({x:.3f},{y:.3f}) circle (.2);\\node[font=\\scriptsize] at ({x:.3f},{y:.3f}) {{Ş}};'
iy=rastgele(8,xs4[1]+.3,xs4[1]+W4-.3,.3,1.8,.5,seed=52)
for i,(x,y) in enumerate(iy):
    g+=f'\\draw[thin,fill=vurgu!25] ({x:.3f},{y:.3f}) circle (.17);\\node[font=\\scriptsize] at ({x:.3f},{y:.3f}) {{{"+" if i%2==0 else "$-$"}}};'
g+=f'\\node at ({xs4[0]+W4/2},-.35) {{\\textbf{{K}}}};\\node at ({xs4[1]+W4/2},-.35) {{\\textbf{{L}}}};'
g+='\\node[right,font=\\footnotesize,align=left] at (6.0,1.55) {Ş: şeker molekülü\\\\ $+$, $-$: iyonlar\\\\ (su molekülleri\\\\ çizilmemiştir)};'
SK4=tk(g)
d={'I':(False,'şeker molekülleri çözünürken yapıları bozulmadan birbirinden ayrılarak suda dağılır, iyonlarına ayrışmaz'),
   'II':(True,'L çözeltisinde serbest hareket eden yüklü iyonlar bulunduğundan çözelti elektrik akımını iletir'),
   'III':(True,'K çözeltisinde yüksüz moleküller bulunur; yük taşıyıcı olmadığından elektrik akımı iletilmez')}
r=onc_t(d,4)
q('0004',ad=[A('Modelleri tanı','K kabında yüksüz Ş molekülleri, L kabında + ve − iyonlar çizilmiştir.','K: moleküler çözünme · L: iyonlarına ayrışma'),adim_onc(d,['I']),adim_onc(d,['II','III'],'II ve III. öncüller'),A('Sonucu yaz','Doğru olan öncüller bir arada yazılır.',oy(d)+' · Sonuç: II ve III')],
 alt='Çözünme Süreci',z='orta',kaz='Moleküler ve iyonik maddelerin çözünme modellerini ve iletkenliklerini yorumlar.',kalip='şekilli',
 kart='K-KMKR2-04 (çözünme ve tanecik modeli) · şekerli su, tuzlu su',
 metin='Aynı sıcaklıkta, eşit hacimli sudan oluşan K ve L kaplarından birine şeker, diğerine yemek tuzu atılmış; maddeler tamamen çözünmüştür. Çözeltilerdeki çözünen taneciklerin görünümü şekildeki gibidir. Elektrik iletkenliği deneyiyle iki çözelti ayrı ayrı denenecektir.\nI. K kabında şeker çözünürken Ş molekülleri iyonlarına ayrışmıştır.\nII. L çözeltisi elektrik akımını iletir.\nIII. K çözeltisinin akımı iletmemesinin nedeni, çözünen taneciklerin yüksüz olmasıdır.\nBuna göre hangileri doğrudur?',
 sekil=SK4,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan öncüller.',
 ip=['Çözünen taneciklerin yüklü olup olmadığına bak; elektrik akımını yüklü tanecikler taşır.'],
 bilgi=[B('Çözünme ve iletkenlik','Moleküler maddeler çözününce molekülleri bozulmadan dağılır; çözelti yüksüz taneciklerden oluşur ve iletmez (alkol–su). İyonik bileşikler çözününce iyonlarına ayrışır; serbest iyonlar akımı iletir (kireç tuzu çözeltisi)')],
 puf='İyonik madde çözününce serbest iyonlar oluşur ve çözelti iletir; moleküler madde çözününce yüksüz moleküller dağılır, çözelti iletmez.')

# ============================================================ 05 · polar–apolar tablo
d={'I':(False,'suda çözünüp apolar hekzanda çözünmeyen madde apolar olamaz; polar ya da iyonik yapılıdır'),
   'II':(True,'hekzanda çözünüp suda çözünmeyen madde “benzer benzeri çözer” ilkesine göre apolar yapılıdır'),
   'III':(False,'su polar, X de polar ya da iyonik olduğundan X’in sudaki karışımı tek fazlı homojendir; heterojen değildir')}
r=onc_t(d,0)
q('0005',ad=[A('Gözlemi yorumla','X suda, Y hekzanda çözünüyor.','X: polar çözücüde · Y: apolar çözücüde'),adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),A('Sonucu yaz','Doğru olan öncüller bir arada yazılır.',oy(d)+' · Sonuç: Yalnız II')],
 alt='Çözünme Süreci',z='orta',kaz='Çözünme gözlemlerinden maddelerin polar ya da apolar yapısını belirler.',kalip='öncüllü',
 kart='K-KMKR2-05 (benzer benzeri çözer) · X, Y katıları; su ve hekzan',
 metin='Öğrenciler, X ve Y katılarından 1’er gram alıp her birini 20 mL su ve 20 mL hekzan ile ayrı ayrı karıştırmıştır. X suda çözünmüş, hekzanda çözünmemiş; Y ise suda çözünmemiş, hekzanda çözünmüştür. Su polar, hekzan apolar çözücüdür; maddelerin hiçbiri çözücüyle tepkime vermemiştir.\nI. X apolar yapılıdır.\nII. Y apolar yapılıdır.\nIII. X’in su ile karışımı heterojendir.\nBuna göre hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan öncüller.',
 ip=['Çözücünün polar mı apolar mı olduğuna bakarak maddenin hangi çözücüde çözündüğünü yorumla.'],
 bilgi=[B('Benzer benzeri çözer','Polar maddeler ve iyonik bileşikler polar çözücülerde (su), apolar maddeler apolar çözücülerde (benzin) çözünür. Örnek: naftalin benzende çözünür, suda çözünmez')],
 puf='Polar madde polar çözücüde, apolar madde apolar çözücüde çözünür; çözünmeyen karışım heterojendir.')

# ============================================================ 06 · çözünme hızı deney tablosu
TAB6=[('1','küp','20','yok','240'),('2','toz','20','yok','90'),('3','toz','20','var','30'),('4','toz','40','var','15')]
assert sum(1 for a,b in itertools.combinations(TAB6,2) if sum(x!=y for x,y in zip(a[1:4],b[1:4]))==1)==3
SK6=tablo_svg(['Deney','Şeker biçimi','Su sıcaklığı (°C)','Karıştırma','Çözünme süresi (s)'],[list(s) for s in TAB6])
pair=lambda i,j:f'{i} ve {j}'
d6=tek_t((pair(2,3),''),[
 (pair(1,3),'bu iki deneyde hem şeker biçimi hem karıştırma farklıdır; süre farkı yalnız karıştırmaya bağlanamaz'),
 (pair(1,4),'bu iki deneyde şeker biçimi, sıcaklık ve karıştırma birlikte değişmiştir'),
 (pair(2,4),'bu iki deneyde sıcaklık ve karıştırma birlikte farklıdır; karıştırmanın etkisi sıcaklıktan ayrılamaz'),
 (pair(3,4),'bu iki deney arasında yalnız su sıcaklığı farklıdır; karıştırma ikisinde de vardır')],2)
q('0006',ad=[A('Değişkenleri incele','Her deneyde şeker biçimi, sıcaklık ve karıştırma değerleri okunur.','1: küp, 20, yok · 2: toz, 20, yok · 3: toz, 20, var · 4: toz, 40, var'),A('Koşulu belirle','Karıştırmanın etkisi için yalnız karıştırma farklı, diğerleri aynı olmalıdır.','karıştırma: yok ve var'),A('Çiftleri ele','Her çiftte kaç etmenin değiştiğine bakılır.','1-2: biçim · 3-4: sıcaklık · 1-3, 1-4, 2-4: birden çok etmen'),A('Sonucu yaz','Yalnız karıştırmanın değiştiği çifti veren şık seçilir.','2 ve 3')],
 alt='Çözünme Süreci',z='orta',kaz='Çözünme hızını etkileyen etmenleri kontrollü deney verisinden yorumlar.',kalip='tablo',
 kart='K-KMKR2-06 (çözünme hızı) · küp/toz şeker, sıcaklık, karıştırma',
 metin='Bir öğrenci, eşit kütlede şekerin 100 mL suda tamamen çözünme süresini, farklı koşullarda dört ayrı deneyde ölçmüştür. Deneylerde şekerin biçimi, suyun sıcaklığı ve karıştırma değiştirilmiş, diğer koşullar aynı tutulmuştur; sonuçlar tabloda verilmiştir.\nÖğrenci, karıştırmanın çözünme hızına etkisini yalnız bu tablodan yararlanarak incelemek istiyor.\nBuna göre hangi iki deneyin sonuçlarını karşılaştırmalıdır?',
 sekil=SK6,dogru=d6['dogru'],yan=d6['yan'],sira=d6['sira'],istenen='Karıştırmanın etkisini gösteren deney çifti.',
 ip=['Bir etkiyi incelemek için karşılaştırılan iki deneyde yalnız o etmen farklı olmalıdır.'],
 bilgi=[B('Çözünme hızı','Çözünme hızı; tanecikler küçüldükçe, sıcaklık arttıkça ve karıştırdıkça artar. Kontrollü deneyde yalnız bir etmen değişir. Örnek: toz tuz, aynı koşullarda kaya tuzundan hızlı çözünür')],
 puf='Bir etmenin etkisini görmek için yalnız o etmeni farklı, diğerlerini aynı olan iki deneyi karşılaştır.')

# ============================================================ 07 · hacimce yüzde etiket
g=('\\draw[thick,rounded corners=3pt] (0,0) rectangle (2.6,3.2);\\draw[thick] (.8,3.2) -- (.8,3.7) -- (1.8,3.7) -- (1.8,3.2);'
   '\\draw[thick,fill=white] (.7,3.7) rectangle (1.9,3.95);'
   '\\draw[thick] (.2,.5) rectangle (2.4,2.7);'
   '\\node[align=center,font=\\small] at (1.3,2.12) {\\textbf{ANTİSEPTİK}};\\draw (.35,1.85) -- (2.25,1.85);'
   '\\node[align=center,font=\\footnotesize] at (1.3,1.45) {Hacimce \\%70\'lik\\\\ etil alkol–su};'
   '\\node[align=center,font=\\small] at (1.3,.88) {\\textbf{250 mL}};')
SK7=tk(g)
v,yz=250,70; alk=Fr(v*yz,100); su=v-alk
assert alk==175 and su==75 and yz==70 and v-yz==180 and 100-yz==30
q('0007',ad=[A('Etiketi oku','Şişedeki çözeltinin toplam hacmi ve hacimce yüzde derişimi etikette yazılıdır.','çözelti: 250 mL · derişim: hacimce %70 alkol'),A('Alkol hacmini bul','Hacimce yüzde, alkolün çözelti hacmine oranıdır.','alkol = 250 × 70 ÷ 100 = 175 mL'),A('Su hacmini bul','Çözeltinin geri kalanı sudur.','su = 250 − 175 = 75 mL')],
 tipId=None,alt='Derişim Birimleri',z='kolay',kaz='Hacimce yüzde derişimden çözücü hacmini hesaplar.',kalip='şekilli',
 kart='K-KMKR2-07 (hacimce yüzde) · antiseptik şişesi etiketi',
 metin='Bir eczanede satılan antiseptik çözeltinin şişesindeki etiket şekilde görülmektedir. Alkol ve suyun hacimlerinin karışırken toplanabildiği varsayılmaktadır.\nBuna göre şişedeki çözeltide kaç mL su vardır?',
 sekil=SK7,dogru=75,yan=[(30,'Suyun yüzdesini (%30) hacim olarak mL yazmış.','dikkat'),(70,'Alkolün yüzde değerini mL sanmış.','dikkat'),(175,'Sorulan suyun yerine alkolün hacmini bulmuş.','dikkat'),(180,'Toplam hacimden yüzde değerini (70) çıkarmış.','islem')],
 istenen='Şişedeki suyun hacmi (mL).',
 ip=['Etikette verilen yüzde, alkolün çözeltinin tamamına oranını gösterir; sorulan ise alkol değildir.'],
 bilgi=[B('Hacimce yüzde','Hacimce yüzde derişim = çözünen hacmi ÷ çözelti hacmi × 100. Örnek: hacimce %40’lık 500 mL çözeltide 200 mL çözünen vardır')],
 puf='Yüzde değeri çözünenin çözeltiye oranıdır; çözücü hacmi çözelti hacminden çözünen hacmi çıkarılarak bulunur.')

# ============================================================ 08 · ppm tablosu
kK,mK=400,8; kL,mL_=600,42
ppK=Fr(mK,kK); ppL=Fr(mL_,kL); top=Fr(mK+mL_,kK+kL)
assert ppK==Fr(2,100) and ppL==Fr(7,100) and top==Fr(5,100) and (ppK+ppL)/2==Fr(45,1000) and ppK+ppL==Fr(9,100) and Fr(mK+mL_,1)==50 and Fr((mK+mL_)*1,1)/Fr(1,1)==50
assert Fr(mK+mL_,kK+kL)*1000==50 # 1 kg yerine 1 g sanma: 50 mg / 1000 g ... 50 ppm
q('0008',ad=[A('Toplamları bul','İki numune karışınca kurşun kütleleri ve çözelti kütleleri ayrı ayrı toplanır.','kurşun: 8 + 42 = 50 mg · çözelti: 400 + 600 = 1000 kg'),A('ppm tanımını uygula','1 ppm, 1 kg çözeltide 1 mg çözünen demektir.','ppm = 50 mg ÷ 1000 kg'),A('Sonucu hesapla','Bölme işlemi yapılır.','50 ÷ 1000 = 0,05 ppm')],
 alt='Derişim Birimleri',z='orta',kaz='Karışımın ppm derişimini toplam kütlelerden hesaplar.',kalip='hikâyeli',
 kart='K-KMKR2-08 (ppm) · iki su numunesi karıştırılıyor',
 metin='Bir çevre mühendisi, iki farklı kuyudan su numuneleri almıştır: K numunesi 400 kg olup 8 mg, L numunesi 600 kg olup 42 mg çözünmüş kurşun içermektedir. Numuneler bir depoda tamamen karıştırılacak, başka madde eklenmeyecek ve kayıp olmayacaktır.\nBuna göre depodaki karışımın kurşun derişimi kaç ppm’dir?',
 dogru=Fr(5,100),yan=[(Fr(45,1000),'İki numunenin ppm değerlerinin aritmetik ortalamasını almış; kütleleri hesaba katmamış.','bilgi'),(Fr(7,100),'Yalnız L numunesinin ppm değerini vermiş.','dikkat'),(Fr(9,100),'İki numunenin ppm değerlerini toplamış.','islem'),(50,'Toplam kurşun kütlesini (50 mg) ppm olarak yazmış; çözelti kütlesine bölmeyi unutmuş.','islem')],
 istenen='Karışımın kurşun derişimi (ppm).',
 ip=['Önce karışımdaki toplam kurşun miktarını ve toplam çözelti kütlesini bul; ppm bunların oranıdır.'],
 bilgi=[B('ppm','ppm “milyonda bir kısım” demektir; sulu çözeltilerde 1 ppm = 1 mg çözünen / 1 kg çözelti. Örnek: 2 kg çözeltide 6 mg madde varsa derişim 3 ppm’dir')],
 puf='ppm hesabında çözünen madde kütlesini mg, çözelti kütlesini kg olarak al; karışımda iki toplamı ayrı ayrı bul.')

# ============================================================ 09 · katı ekleme (zor)
m0,c0,c1=200,10,28
x=Fr(c1*m0-c0*m0,100-c1); sol=Fr(c0*m0,100)
assert x==50 and (sol+x)/(m0+x)==Fr(c1,100)
assert Fr(c1*m0,100)-sol==36 and c1-c0==18 and Fr((c1-c0)*m0,100-c0)==40 and Fr(c1*m0,100)==56
q('0009',ad=[A('Başlangıç durumunu yaz','İlk çözeltideki şeker kütlesi bulunur.','şeker = 200 × 10 ÷ 100 = 20 g'),A('Denklemi kur','x gram eklenince şeker de çözelti de x kadar artar.','(20 + x) ÷ (200 + x) = 28 ÷ 100'),A('Çöz','İçler dışlar çarpımıyla x yalnız bırakılır.','100 × (20 + x) = 28 × (200 + x) → 2000 + 100x = 5600 + 28x'),A('Sonucu bul','x terimleri bir tarafta toplanır.','72x = 3600 → x = 50 g')],
 alt='Derişim Birimleri',z='zor',kaz='Çözeltiye katı eklenerek istenen kütlece yüzde derişime ulaşmak için gereken miktarı hesaplar.',kalip='hikâyeli',
 kart='K-KMKR2-09 (katı ekleme ile derişim) · %10’luk 200 g şerbete şeker ekleme',
 metin='Bir tatlıcı, kütlece %10’luk 200 g şekerli su çözeltisine bir miktar daha şeker ekleyip karıştırarak kütlece %28’lik şerbet elde etmek istiyor. Eklenen şekerin tamamı çözünecek, çözeltiden su ayrılmayacak ve başka madde eklenmeyecektir.\nBuna göre tatlıcının çözeltiye kaç gram şeker eklemesi gerekir?',
 dogru=50,yan=[(18,'Yüzde farkını (28 − 10) gram sanmış.','dikkat'),(36,'Eklenen şekerin çözelti kütlesini de artırdığını unutarak 200 × 28 ÷ 100 − 20 işlemini yapmış.','bilgi'),(40,'Denklemde paydaya 100 − 28 yerine 100 − 10 yazmış.','islem'),(56,'Yeni çözeltideki 56 g şekerin tamamını eklenen miktar sanmış.','dikkat')],
 istenen='Eklenmesi gereken şeker kütlesi (g).',
 ip=['Eklenen şeker, çözünen kütlesini ve çözelti kütlesini nasıl değiştirir?'],
 bilgi=[B('Kütlece yüzde','Kütlece yüzde = çözünen kütlesi ÷ çözelti kütlesi × 100. Örnek: %15’lik 80 g çözeltide 12 g çözünen vardır')],
 puf='Çözünen eklenince çözünen ve çözelti kütlesi aynı miktarda artar; denklemi (çözünen + x) ÷ (çözelti + x) olarak kur.')

# ============================================================ 10 · seyreltme (kolay)
m,c1,c2=240,30,24
tz=Fr(m*c1,100); yeni=tz*100/c2; ek=yeni-m
assert tz==72 and yeni==300 and ek==60 and c1-c2==6 and Fr(m*(c1-c2),c1)==48
q('0010',ad=[A('Şeker kütlesini bul','Su eklenince şeker miktarı değişmez.','şeker = 240 × 30 ÷ 100 = 72 g'),A('Yeni çözelti kütlesi','Aynı şeker, %24’lük çözeltide kaç gram çözelti yapar?','72 ÷ 24 × 100 = 300 g'),A('Eklenen suyu bul','Yeni ve eski çözelti kütlelerinin farkı eklenen sudur.','300 − 240 = 60 g')],
 alt='Seyreltme ve Derişikleştirme',z='kolay',kaz='Kütlece yüzde derişimi bilinen çözeltiyi seyrelterek eklenecek su kütlesini hesaplar.',kalip='hikâyeli',
 kart='K-KMKR2-10 (seyreltme) · %30’luk 240 g şekerli su, %24’e seyreltme',
 metin='Bir lokumcuda şerbet yapımında kullanılan kütlece %30’luk 240 g şekerli su çözeltisi, üzerine saf su eklenerek kütlece %24’lük hâle getirilecektir. Eklenen su dışında bir madde karışmayacak ve buharlaşma olmayacaktır.\nBuna göre çözeltiye kaç gram saf su eklenmelidir?',
 dogru=60,yan=[(6,'İki derişim arasındaki yüzde farkını gram saymış.','dikkat'),(48,'Seyreltme oranını ters kurarak 240 × (30 − 24) ÷ 30 işlemini yapmış.','islem'),(72,'Çözeltideki şeker kütlesini eklenecek su sanmış.','dikkat'),(300,'Seyrelmiş çözeltinin kütlesini eklenen su kütlesi sanmış.','dikkat')],
 istenen='Eklenmesi gereken saf su kütlesi (g).',
 ip=['Su eklenince değişmeyen nicelik hangisi? Onunla yeni çözeltinin kütlesini bul.'],
 bilgi=[B('Seyreltme','Seyreltmede çözünen kütlesi değişmez, çözelti kütlesi artar, derişim azalır. Örnek: %50’lik 100 g çözeltideki 50 g çözünen, 100 g su eklenince %25’lik 200 g çözeltide yine 50 g kalır')],
 puf='Seyreltmede çözünen kütlesi sabittir; yeni çözelti kütlesini çözünen ÷ yeni derişim ile bul.')

# ============================================================ 11 · derişim–su grafiği (zor)
mm=200; tz=60; cx=lambda s: Fr(tz*100,mm+s)
assert cx(0)==30 and cx(100)==20 and cx(300)==12 and 30*mm==20*(mm+100)
hedef=10; top_=Fr(tz*100,hedef); ekl=top_-mm
assert top_==600 and ekl==400 and top_==600 and Fr(30,hedef)*100==300 and top_-100==500
sx,sy=.016,.11
pts=[(s,float(cx(s))) for s in range(0,301,25)]
g=eksen(300,32,sx,sy,[0,100,200,300],[10,20,30],'Eklenen su kütlesi (g)','Kütlece yüzde derişim (\\%)',xlpos=300*sx/2)
g+=egri(pts,sx,sy,'very thick,vurgu')
for s,c in [(0,30),(100,20)]:
    g+=f'\\draw[dashed] ({s*sx},0) -- ({s*sx},{c*sy}) -- (0,{c*sy});\\fill ({s*sx},{c*sy}) circle (.07);'
SK11=tk(g)
q('0011',ad=[A('Grafikten veri oku','Hiç su eklenmeden derişim 30, 100 g su eklenince 20 okunur.','30 ve 20'),A('İlk çözelti kütlesini bul','Çözünen kütlesi sabit olduğundan iki durum eşitlenir.','m × 30 = (m + 100) × 20 → m = 200 g'),A('Çözünen kütlesi','İlk çözeltideki çözünen hesaplanır.','200 × 30 ÷ 100 = 60 g'),A('Hedef çözelti kütlesi','%10’luk çözeltide 60 g çözünen kaç g çözelti yapar?','60 ÷ 10 × 100 = 600 g'),A('Eklenecek su','Hedef kütle ile ilk çözelti kütlesinin farkı alınır.','600 − 200 = 400 g')],
 alt='Seyreltme ve Derişikleştirme',z='zor',kaz='Derişim–eklenen su grafiğinden çözelti kütlesini bulup yeni derişim için gereken suyu hesaplar.',kalip='grafik',
 kart='K-KMKR2-11 (derişim–su grafiği) · şekerli su çözeltisine su ekleme',
 metin='Bir öğrenci, kütlece derişimi bilinmeyen miktarda şekerli su çözeltisine saf su ekleyerek her aşamada çözeltinin kütlece yüzde derişimini hesaplamış ve sonuçları şekildeki grafikte göstermiştir. İşlem boyunca şeker kaybı ve buharlaşma olmamıştır.\nÖğrenci aynı çözeltiyi kütlece %10’luk hâle getirmek istediğine göre, hiç su eklenmemiş başlangıç durumuna göre toplam kaç gram saf su eklemelidir?',
 sekil=SK11,dogru=400,yan=[(200,'Grafikte 100 g suyun derişimi 10 puan düşürdüğünü doğrusal sanıp %10 için 200 g su bulmuş.','bilgi'),(300,'Grafikte 300 g su eklenince okunan derişimin (yaklaşık %12) %10’a yakın olduğunu düşünerek 300 g demiş.','dikkat'),(500,'%10’luk çözeltinin 600 g olduğunu bulmuş, fakat grafikte okunan 100 g suyu da çıkarmış.','islem'),(600,'Hedef çözeltinin kütlesini eklenecek su kütlesi sanmış.','dikkat')],
 istenen='Toplam eklenmesi gereken saf su kütlesi (g).',
 ip=['Grafikteki iki noktadan ilk çözeltinin kütlesi hakkında ne öğrenebileceğini düşün.'],
 bilgi=[B('Seyreltme ve derişim','Su eklenince derişim doğrusal değil, çözelti kütlesiyle ters orantılı azalır. Örnek: %40’lık çözeltiye ilk kütlesi kadar su eklenirse derişim yarıya iner, %20 olur')],
 puf='Çözünen kütlesi sabit; derişim × çözelti kütlesi her durumda aynı değeri verir.')

# ============================================================ 12 · karıştırma + buharlaştırma (zor)
mK_,cK_,mL2,cL2,buh=150,20,250,36,80
tK=Fr(mK_*cK_,100); tL=Fr(mL2*cL2,100); T_=tK+tL; M_=mK_+mL2-buh
son=T_/M_*100
assert tK==30 and tL==90 and T_==120 and M_==320 and son==Fr(75,2)
assert T_/(mK_+mL2)*100==30 and Fr(cK_+cL2,2)==28 and Fr(28*(mK_+mL2),100)/M_*100==35 and (T_-buh)/M_*100==Fr(25,2) and T_/(mK_+mL2-T_-buh)*100==60
g=beher(0,1.5)+beher(2.5,1.9)+beher(5.5,0,w=2.0,h=2.6)
g+=f'\\node[align=center,font=\\footnotesize] at (.85,2.75) {{K\\\\ {mK_} g\\\\ \\%{cK_}}};\\node[align=center,font=\\footnotesize] at (3.35,2.75) {{L\\\\ {mL2} g\\\\ \\%{cL2}}};'
g+='\\node[font=\\Large] at (2.1,1.1) {$+$};\\draw['+ARR+'] (4.45,1.1) -- (5.3,1.1);\\node[align=center,font=\\footnotesize] at (6.5,2.95) {karışım};'
g+='\\node at (6.5,-.4) {M};'
SK12=tk(g)
q('0012',ad=[A('Şeker kütleleri','Her çözeltideki şeker kütlesi hesaplanır.','K: 150 × 20 ÷ 100 = 30 g şeker · L: 250 × 36 ÷ 100 = 90 g şeker'),A('Karışımın toplamları','Şeker ve çözelti kütleleri ayrı ayrı toplanır.','şeker = 30 + 90 = 120 g · çözelti = 150 + 250 = 400 g'),A('Buharlaşmayı uygula','Yalnız su gittiği için çözelti kütlesi azalır, şeker değişmez.','çözelti = 400 − 80 = 320 g'),A('Yeni derişim','Şeker kütlesi son çözelti kütlesine bölünür.','120 ÷ 320 × 100 = %37,5')],
 alt='Seyreltme ve Derişikleştirme',z='zor',kaz='İki çözeltinin karışımından buharlaştırma yapıldığında oluşan derişimi hesaplar.',kalip='şekilli',
 kart='K-KMKR2-12 (karıştırma ve buharlaştırma) · K ve L şekerli su çözeltileri',
 metin='Bir şekerleme atölyesinde, kütleleri ve kütlece derişimleri şekilde verilen K ve L şekerli su çözeltileri boş bir M kabında tamamen karıştırılıyor. Ardından M kabını ısıtan ustalar, karışımdan 80 g su buharlaştırıyor. Şeker buharlaşmıyor ve başka madde eklenmiyor.\nBuna göre son çözeltinin kütlece yüzde derişimi kaçtır?',
 sekil=SK12,dogru=Fr(75,2),yan=[(Fr(25,2),'Buharlaşan 80 g’ı çözünen şeker kütlesinden çıkarmış.','bilgi'),(30,'Buharlaşmayı hesaba katmadan karışımın derişimini bulmuş.','dikkat'),(35,'İki derişimin ortalamasıyla (%28) çözelti kütlesi hesaplamış, ortalama almanın kütleye bağlı olduğunu görmemiş.','bilgi'),(60,'Şeker kütlesini yalnız su kütlesine (200 g) bölmüş.','islem')],
 istenen='Son çözeltinin kütlece yüzde derişimi (%).',
 ip=['Karıştırmada şeker kütleleri toplanır; buharlaşmada değişen nicelik şeker değil, çözelti kütlesidir.'],
 bilgi=[B('Çözelti karıştırma','İki çözeltiyi karıştırınca derişimler değil, çözünen kütleleri ve çözelti kütleleri toplanır. Örnek: %10’luk 100 g ile %30’luk 100 g çözelti karışınca 40 g çözünen, 200 g çözelti olur')],
 puf='Önce çözünen kütlelerini topla; buharlaşma yalnız çözelti kütlesini azaltır.')

# ============================================================ 13 · derişimi artıran işlemler
d={'I':(True,'çözünen kütlesi sabit kalıp çözelti kütlesi azalınca derişim artar'),
   'II':(True,'daha derişik bir çözelti katılınca karışımın derişimi ilk derişimden büyük olur'),
   'III':(True,'eklenen şeker tamamen çözününce hem çözünen kütlesi hem çözelti kütlesi artar ve derişim büyür')}
r=onc_t(d,4)
q('0013',ad=[adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),A('Sonucu yaz','Üç işlem de derişimi artırır.',oy(d)+' · Sonuç: I, II ve III')],
 alt='Seyreltme ve Derişikleştirme',z='kolay',kaz='Çözelti derişimini artıran işlemleri belirler.',kalip='öncüllü',
 kart='K-KMKR2-13 (derişimi artıran işlemler) · kütlece %20’lik şekerli su',
 metin='Bir öğrencinin hazırladığı kütlece %20’lik şekerli su çözeltisinin derişimi artırılmak isteniyor. Her işlem ayrı ayrı uygulanacak; sıcaklık sabit tutulacak ve çözeltideki şeker çözünürlük sınırını aşmayacaktır.\nI. Bir miktar suyun buharlaştırılması\nII. Kütlece %35’lik şekerli su çözeltisinden bir miktar eklenmesi\nIII. Bir miktar şekerin eklenip tamamen çözülmesi\nBuna göre hangileri çözeltinin derişimini artırır?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Derişimi artıran işlemler.',
 ip=['Her işlemde çözünen kütlesinin ve çözelti kütlesinin nasıl değiştiğine bak.'],
 bilgi=[B('Derişikleştirme','Derişim; çözücü azaltılarak, çözünen eklenerek ya da daha derişik çözelti katılarak artırılır. Örnek: %5’lik çözelti, %12’lik bir çözelti ile karıştırılınca derişimi %5’ten büyük, %12’den küçük olur')],
 puf='Çözünen oranını artıran her işlem derişimi artırır; daha derişik çözelti eklemek de bunlardandır.')

# ============================================================ 14 · çözünürlük grafiği
TT=[20,40,60,80]
Kd=[20,34,50,70]; Ld=[40,46,50,52]; Md=[30,20,12,6]
assert Kd[2]==Ld[2]==50 and Ld[0]>Md[0]>Kd[0] and Md[0]>Md[1]>Md[2]>Md[3] and all(a<b for a,b in zip(Kd,Kd[1:])) and all(a<b for a,b in zip(Ld,Ld[1:]))
sx,sy=.065,.045
g=eksen(80,80,sx,sy,[20,40,60,80],[10,20,30,40,50,60,70,80],f'Sıcaklık ({DC})','Çözünürlük (g / 100 g su)',xlpos=40*sx)
for nm,dt,st,yy in [('K',Kd,'very thick,vurgu',0),('L',Ld,'very thick,dashed',0),('M',Md,'very thick,dash dot',0)]:
    g+=egri(list(zip(TT,dt)),sx,sy,st)
g+=f'\\node[right,font=\\footnotesize] at ({80*sx+.05},{Kd[3]*sy}) {{K}};\\node[right,font=\\footnotesize] at ({80*sx+.05},{Ld[3]*sy}) {{L}};\\node[right,font=\\footnotesize] at ({80*sx+.05},{Md[3]*sy+.1}) {{M}};'
g+=f'\\fill ({60*sx},{50*sy}) circle (.06);'
SK14=tk(g)
d={'I':(True,'K ve L eğrileri 60 °C’de kesiştiği için bu sıcaklıkta çözünürlükleri eşittir'),
   'II':(False,'20 °C’de en çok çözünen madde, eğrisi en yukarıda olan L’dir; K’nin çözünürlüğü üçünün en küçüğüdür'),
   'III':(False,'M’nin çözünürlüğü sıcaklıkla azaldığından doygun çözeltisi ısıtılınca fazla madde çözünemez ve dipte katı birikir')}
r=onc_t(d,0)
q('0014',ad=[A('Eğrileri tanı','K ve L’nin çözünürlüğü sıcaklıkla artar, M’ninki azalır.','K, L: artan · M: azalan'),adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),A('Sonucu yaz','Doğru olan öncül belirlenir.',oy(d)+' · Sonuç: Yalnız I')],
 alt='Çözünürlük',z='orta',kaz='Çözünürlük–sıcaklık grafiğinden maddelerin çözünürlüklerini karşılaştırır.',kalip='grafik',
 kart='K-KMKR2-14 (çözünürlük–sıcaklık grafiği) · K, L, M katıları',
 metin='K, L ve M katılarının sudaki çözünürlüklerinin sıcaklıkla değişimi şekildeki grafikte verilmiştir. Katıların hiçbiri suyla tepkime vermemekte ve doygun çözeltiler dipte çözünmemiş katı bulunmayacak biçimde hazırlanmaktadır.\nI. 60 °C’de K ve L’nin çözünürlükleri eşittir.\nII. 20 °C’de en çok çözünen madde K’dir.\nIII. M’nin doygun çözeltisi ısıtılırsa dipte katı birikmez.\nBuna göre hangileri doğrudur?',
 sekil=SK14,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan öncüller.',
 ip=['Eğrilerin kesiştiği nokta ve her eğrinin sıcaklıkla yükselip alçalması öncüllerin dayanağıdır.'],
 bilgi=[B('Çözünürlük–sıcaklık grafiği','Çözünürlük, 100 g suda çözünebilen en çok madde kütlesidir. Eğri sıcaklıkla yükseliyorsa madde ısınınca daha çok çözünür; kesişen iki eğri o sıcaklıkta eşit çözünürlük demektir')],
 puf='Eğrinin yüksekliği çözünürlüğü, eğimi sıcaklıkla değişimini; kesişme noktası eşit çözünürlüğü gösterir.')

# ============================================================ 15 · doymamış / doygun
Xd=[(0,22),(20,30),(40,40),(60,52),(80,66)]
assert Xd[2]==(40,40)
sx,sy=.065,.04
g=eksen(80,80,sx,sy,[20,40,60,80],[20,40,60,80],f'Sıcaklık ({DC})','100 g suya katılan X (g)',xlpos=40*sx)
g+=egri(Xd,sx,sy,'very thick,vurgu')
for nm,yv in [('P',20),('R',40),('S',60)]:
    g+=f'\\fill ({40*sx},{yv*sy}) circle (.07);\\node[right,font=\\small] at ({40*sx+.1},{yv*sy-.12}) {{\\textbf{{{nm}}}}};'
SK15=tk(g)
d={'I':(False,'P’de 40 °C’de çözünebilecek 40 g’ın yarısı katılmıştır; çözelti daha fazla X çözebilir, yani doymamıştır'),
   'II':(False,'R’de katılan miktar tam olarak 40 °C’deki çözünürlüğe eşittir; çözelti doygundur'),
   'III':(True,'S’de 60 g katılmış, en çok 40 g çözünebildiğinden 20 g katı dipte kalır; çözelti doygundur')}
r=onc_t(d,0)
q('0015',ad=[A('Noktaları yorumla','Eğrinin altındaki miktar tamamen çözünür; eğri üzeri doygun çözelti ve dipte katı demektir.','P: eğrinin altı · R: eğri üzerinde · S: eğrinin üstü'),adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),A('Sonucu yaz','Doğru olan öncül belirlenir.',oy(d)+' · Sonuç: Yalnız III')],
 alt='Çözünürlük',z='orta',kaz='Çözünürlük eğrisine göre çözeltilerin doymamış ya da doygun olduğunu ve dipte katı bulunup bulunmadığını belirler.',kalip='grafik',
 kart='K-KMKR2-15 (doymamış–doygun) · P, R, S noktaları',
 metin='Şekildeki eğri, X katısının sudaki çözünürlüğünün sıcaklıkla değişimini göstermektedir. P, R ve S noktaları, her biri 100 g su içeren üç kapta, 40 °C’de karıştırılarak hazırlanan çözeltilere katılan X miktarını temsil etmektedir. Üç kapta da karışım dengeye gelmiş, sıcaklık 40 °C’de sabit tutulmuştur.\nI. P kabındaki çözelti doygundur.\nII. R kabındaki çözelti doymamıştır.\nIII. S kabındaki çözelti doygundur ve dibinde katı X bulunur.\nBuna göre hangileri doğrudur?',
 sekil=SK15,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan öncüller.',
 ip=['Her noktadaki X miktarını 40 °C’de 100 g suyun çözebileceği en çok miktarla karşılaştır.'],
 bilgi=[B('Doymamış ve doygun çözelti','Doymamış çözelti aynı sıcaklıkta daha fazla madde çözebilir. Doygun çözelti çözebileceği en çok maddeyi içerir; fazlası çözünmeden dipte kalır')],
 puf='Katılan miktar çözünürlükten azsa çözelti doymamış, eşitse tam doygun, fazlaysa doygun ve dipte katı vardır.')

# ============================================================ 16 · soğutmada çöken (zor)
c80,c20=60,20; m80=320
su_=Fr(m80*100,100+c80); cz=su_*c80/100; cok=cz-su_*c20/100
assert su_==200 and cz==120 and cok==80 and c80-c20==40 and Fr(m80*(c80-c20),100)==128 and su_*c20/100==40
sx,sy=.06,.06
a=Fr(0); # c(T)=a0+b T+c T^2 ; (20,20),(80,60) ; c2=.002
c2=.002; b=(60-20-c2*(80**2-20**2))/60; a0=20-20*b-c2*400
Cf=lambda T:a0+b*T+c2*T*T
pts=[(T,Cf(T)) for T in range(10,101,10)]
assert abs(Cf(20)-20)<1e-9 and abs(Cf(80)-60)<1e-9 and 0<Cf(10) and Cf(100)<85
g=eksen(100,80,sx,sy,[20,40,60,80,100],[20,40,60,80],f'Sıcaklık ({DC})','Çözünürlük (g X / 100 g su)',xlpos=50*sx)
g+=egri(pts,sx,sy,'very thick,vurgu')
for T,c in [(20,20),(80,60)]:
    g+=f'\\draw[dashed] ({T*sx},0) -- ({T*sx},{c*sy}) -- (0,{c*sy});\\fill ({T*sx},{c*sy}) circle (.07);'
SK16=tk(g)
q('0016',ad=[A('Grafikten çözünürlükleri oku','80 °C’de 60, 20 °C’de 20 g X çözünür (100 g suda).','80 °C: 60 · 20 °C: 20'),A('Su kütlesini bul','100 g su + 60 g X = 160 g doygun çözelti demektir.','320 ÷ 160 = 2 → su = 200 g'),A('Çözünen X kütleleri','200 g su için iki sıcaklıktaki çözünen hesaplanır.','80 °C: 120 g · 20 °C: 40 g'),A('Çöken miktar','Fark soğutmada katı olarak çöker.','120 − 40 = 80 g')],
 alt='Çözünürlük',z='zor',kaz='Çözünürlük grafiğinden ve doygun çözelti kütlesinden soğutmada çöken madde miktarını hesaplar.',kalip='grafik',
 kart='K-KMKR2-16 (soğutmada çöken madde) · 80 °C’de doygun 320 g çözelti 20 °C’ye soğutuluyor',
 metin='Şekildeki grafik, X katısının sudaki çözünürlüğünün sıcaklıkla değişimini göstermektedir. 80 °C’de hazırlanan 320 g’lık doygun X çözeltisi, çözücü kaybı olmadan 20 °C’ye kadar soğutuluyor ve dipte katı X birikiyor.\nBuna göre dipte biriken katı X kaç gramdır?',
 sekil=SK16,dogru=80,yan=[(40,'Çözünürlük farkını (60 − 20) 100 g suya göre bulmuş, çözeltideki su kütlesine ölçeklememiş.','dikkat'),(120,'80 °C’de çözünmüş toplam X kütlesini çöken miktar sanmış.','dikkat'),(128,'320 g çözeltiyi su kütlesi sanıp 40 g farkını 3,2 ile çarpmış.','bilgi'),(200,'Çözeltideki su kütlesini çöken katı kütlesi sanmış.','dikkat')],
 istenen='Dipte biriken katı X kütlesi (g).',
 ip=['Çözünürlüğün hangi su kütlesine göre verildiğine dikkat et.'],
 bilgi=[B('Soğutmada çökme','Çözünürlük sıcaklıkla azalırsa doygun çözelti soğutulunca fazla madde çöker. Örnek: 100 g suda çözünürlük 45 g ise doygun çözeltinin 145 g’ında 100 g su, 45 g çözünen vardır')],
 puf='Önce çözeltiden su kütlesini bul, sonra iki sıcaklıktaki çözünürlüğü o su kütlesine göre hesaplayıp farkı al.')

# ============================================================ 17 · gaz çözünürlüğü
d17=tek_t(('Gazlı içeceğin kapağı açılınca basınç düşer, CO₂’nin çözünürlüğü azalır ve kabarcıklar çıkar.',''),[
 ('Gazlı içecek ısıtıldığında CO₂’nin çözünürlüğü artar, bu yüzden daha fazla gaz çözünür.','gazların sudaki çözünürlüğü sıcaklık arttıkça azalır; ısıtılan içecekten gaz çıkar'),
 ('Katı bir maddenin sudaki çözünürlüğü, çözeltinin üzerindeki basınç artırılınca belirgin biçimde artar.','katıların ve sıvıların çözünürlüğü basınçtan belirgin biçimde etkilenmez; basınç etkisi gazlar için geçerlidir'),
 ('Sıcaklık artınca bütün katıların sudaki çözünürlüğü azalır.','katıların çoğunun çözünürlüğü sıcaklıkla artar; azalan katılar istisnadır'),
 ('Gazların sudaki çözünürlüğü, üzerlerindeki basınç azaldıkça artar.','gazların çözünürlüğü basınç arttıkça artar, azaldıkça azalır')],3)
q('0017',ad=[A('Gazın özelliğini hatırla','Gaz çözünürlüğü basınçla artar, sıcaklıkla azalır.','basınç ↑ → çözünürlük ↑ · sıcaklık ↑ → çözünürlük ↓'),A('Gaz içeceğe uygula','Kapak açılınca basınç düşer, gaz çözünürlüğü azalır.','kabarcıklar çıkar'),A('Diğer ifadeleri ele','Isıtma, basınç ve katı çözünürlüğüyle ilgili diğer ifadeler bu kurala ters düşer.','diğer dört ifade: yanlış')],
 alt='Çözünürlük',z='orta',kaz='Gaz ve katıların çözünürlüğüne sıcaklık ve basıncın etkisini yorumlar.',kalip='hikâyeli',
 kart='K-KMKR2-17 (gaz çözünürlüğü) · gazlı içecek şişesi',
 metin='Yaz günü bir pikniğe giden aile, soğutucu çantadaki gazlı içecek şişelerinden birinin kapağını açıyor ve içecekte hemen kabarcıklar oluştuğunu görüyor. Sonra şişenin bir bölümünü güneşte unutuyor; bir süre sonra o şişedeki içecek bayatlıyor. Bu gözlemler çözünürlük kavramıyla yorumlanacaktır.\nBuna göre aşağıdakilerden hangisi doğrudur?',
 dogru=d17['dogru'],yan=d17['yan'],sira=d17['sira'],istenen='Doğru olan ifade.',
 ip=['Gazların çözünürlüğünün sıcaklık ve basınçla nasıl değiştiğini katılarla karşılaştırarak düşün.'],
 bilgi=[B('Çözünürlüğü etkileyen etmenler','Gazların çözünürlüğü sıcaklık arttıkça azalır, basınç arttıkça artar. Katıların çözünürlüğü çoğunlukla sıcaklıkla artar, basınçtan belirgin etkilenmez. Örnek: soğuk su, ılık sudan daha çok oksijen çözer')],
 puf='Gaz çözünürlüğü basınçla artar, sıcaklıkla azalır; katıların çözünürlüğü basınçtan belirgin etkilenmez.')

# ============================================================ 18 · donma noktası alçalması (grafik)
Kc=[(0,20),(8,0),(16,0),(24,-10)]
Lc=[(0,20),(10,-5),(22,-7),(24.4,-10)]
sx,sy=.2,.09
def Y(v): return (v+12)*sy
YT=[-10,-5,0,5,10,15,20]
g=''
for v in YT: g+=f'\\draw[black!15] (0,{Y(v):.3f}) -- ({26*sx:.3f},{Y(v):.3f});'
g+=f'\\draw[thick,{ARR}] (0,0) -- ({26*sx+.35:.3f},0);\\draw[thick,{ARR}] (0,0) -- (0,{Y(20)+.45:.3f});'
for v in YT: g+=f'\\draw[thick] (0,{Y(v):.3f}) -- (-.07,{Y(v):.3f}) node[left,font=\\footnotesize] {{{v if v>=0 else "$-$"+str(-v)}}};'
g+=f'\\node[below,font=\\footnotesize] at ({13*sx:.3f},-.1) {{Zaman}};\\node[above,font=\\footnotesize] at (0,{Y(20)+.45:.3f}) {{Sıcaklık ({DC})}};'
g+='\\draw[very thick,vurgu] '+' -- '.join(f'({x*sx:.3f},{Y(y):.3f})' for x,y in Kc)+';'
g+='\\draw[very thick,dashed] '+' -- '.join(f'({x*sx:.3f},{Y(y):.3f})' for x,y in Lc)+';'
g+=f'\\node[font=\\footnotesize] at ({12*sx:.3f},{Y(0)+.28:.3f}) {{K}};\\node[font=\\footnotesize] at ({16*sx:.3f},{Y(-6)-.3:.3f}) {{L}};'
SK18=tk(g)
assert Kc[1][1]==Kc[2][1]==0 and Lc[1][1]==-5 and Lc[2][1]<Lc[1][1]
d={'I':(True,'tuzlu su, saf sudan düşük sıcaklıkta donmaya başlar; grafikte donmanın daha düşük sıcaklıkta başladığı L eğrisi tuzlu suya aittir'),
   'II':(False,'çözünen madde (tuz) suyun donma noktasını yükseltmez, düşürür'),
   'III':(True,'çözünen miktarı arttıkça donma noktası daha çok düşer; L’ye tuz eklenirse donma başlangıç sıcaklığı daha da düşer')}
r=onc_t(d,4)
q('0018',ad=[A('Grafiği oku','K’de donma 0 °C’de sabit sıcaklıkta; L’de daha düşük sıcaklıkta ve sıcaklık hafif düşerek gerçekleşir.','K: saf su · L: tuzlu su'),adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),A('Sonucu yaz','Doğru olan öncüller bir arada yazılır.',oy(d)+' · Sonuç: I ve III')],
 alt='Koligatif Özellikler',z='kolay',kaz='Soğutma grafiğinden çözünen maddenin donma noktasını düşürdüğünü yorumlar.',kalip='grafik',
 kart='K-KMKR2-18 (donma noktası alçalması) · saf su ve tuzlu su soğutma grafiği',
 metin='Biri saf su, diğeri yemek tuzunun suda çözünmesiyle hazırlanmış tuzlu su olan iki sıvı, aynı soğutucuda eşit hızla soğutulmuş ve sıcaklıkları zamanla ölçülerek grafikte K ve L eğrileri olarak gösterilmiştir. Hangi eğrinin hangi sıvıya ait olduğu belirtilmemiştir.\nI. L eğrisi tuzlu suya aittir.\nII. Tuz çözünmesi suyun donma noktasını yükseltir.\nIII. L’deki çözeltiye bir miktar daha tuz çözülürse donmanın başladığı sıcaklık daha da düşer.\nBuna göre hangileri doğrudur?',
 sekil=SK18,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan öncüller.',
 ip=['Saf maddenin donma sırasında sıcaklığının nasıl davrandığını, çözeltininkiyle karşılaştır.'],
 bilgi=[B('Donma noktası alçalması','Bir sıvıda uçucu olmayan madde çözününce donma noktası düşer; çözünen miktarı arttıkça düşüş artar. Örnek: şekerli su, saf sudan daha düşük sıcaklıkta donar')],
 puf='Çözünen madde donma noktasını düşürür, miktarı arttıkça düşüş büyür; saf madde donarken sıcaklık sabit kalır.')

# ============================================================ 19 · koligatif günlük örnekler (olumsuz kök)
d19=tek_t(('Yağlı bir yemek lekesinin benzinle silinerek çıkarılması',''),[
 ('Buzlanma tehlikesi olan yollara kış aylarında tuz serpilmesi','tuz buzun erimesini sağlar; çözelti saf sudan düşük sıcaklıkta donar, bu donma noktası alçalmasıdır'),
 ('Araç radyatörüne antifriz katılarak suyun kış aylarında donmasının önlenmesi','antifriz suyun donma noktasını düşürür, kaynama noktasını da yükseltir; bu koligatif özelliktir'),
 ('Deniz suyunun, akarsu suyundan daha düşük sıcaklıkta donması','tuzlu deniz suyunun donma noktası saf sudan düşüktür; bu koligatif özelliktir'),
 ('Kaynayan suya tuz eklenince çözeltinin kaynama noktasının saf sudan yüksek olması','çözünen madde kaynama noktasını yükseltir; bu da koligatif bir özelliktir')],0,False)
q('0019',ad=[A('Koligatif özelliği hatırla','Çözünen maddenin çözücünün donma ve kaynama noktasını değiştirmesidir.','donma noktası ↓ · kaynama noktası ↑'),A('Örnekleri ele','Tuz serpme, antifriz, deniz suyu ve tuzlu su kaynaması bu özellikle açıklanır.','4 örnek: koligatif'),A('Farklı olanı bul','Yağ lekesinin benzinle çıkması çözünme türüyle, “benzer benzeri çözer” ilkesiyle ilgilidir.','yağ lekesi: koligatif değil')],
 alt='Koligatif Özellikler',z='orta',kaz='Günlük yaşam örneklerinden hangilerinin koligatif özellikle açıklandığını belirler.',kalip='hikâyeli',
 kart='K-KMKR2-19 (koligatif günlük örnekler) · yola tuz, antifriz, deniz suyu, benzinle leke',
 metin='Fen bilimleri dersinde öğretmen, günlük hayattan çeşitli uygulamaları koligatif özellikler yönünden incelemelerini istiyor. Koligatif özellikler, çözünen maddenin türüne değil çözeltideki tanecik miktarına bağlı olarak çözücünün donma ve kaynama noktasının değişmesidir.\nBuna göre aşağıdaki uygulamalardan hangisinin nedeni koligatif özellik değildir?',
 dogru=d19['dogru'],yan=d19['yan'],sira=d19['sira'],istenen='Nedeni koligatif özellik olmayan uygulama.',
 ip=['Her uygulamada donma ya da kaynama noktasının mı değiştiğine, yoksa maddenin çözünüp çözünmediğine mi bakıldığını ayırt et.'],
 bilgi=[B('Koligatif özellikler','Çözeltide donma noktası düşer, kaynama noktası yükselir; etki çözünen tanecik miktarına bağlıdır. Örnek: yemek tuzu ve şeker çözeltisinin ikisi de saf sudan düşük sıcaklıkta donar')],
 puf='Donma ya da kaynama noktasının değişmesiyle açıklanan olaylar koligatiftir; çözünme uyumu başka bir konudur.')

# ============================================================ 20 · damıtma düzeneği
th=math.degrees(math.asin(.22/.9)); a1=90+th; a2=90-th+360
xl_,yl_=.9*math.cos(math.radians(a1)),.9*math.sin(math.radians(a1))
al=-20
g=''
g+=f'\\begin{{scope}}\\clip (0,0) circle (.9);\\fill[vurgu!15] (-1,-1) rectangle (1,.1);\\end{{scope}}'
g+=f'\\draw[thick] (-.22,1.75) -- ({xl_:.3f},{yl_:.3f}) arc[start angle={a1:.2f},end angle={a2:.2f},radius=.9] -- (.22,1.75);'
g+='\\draw[thick,fill=white] (-.3,1.75) rectangle (.3,1.98);'
g+='\\draw[thick,fill=white] (-.05,1.98) rectangle (.05,3.0);\\draw[thick,fill=white] (0,1.15) circle (.08);\\draw[thick] (-.05,1.15) -- (-.05,1.98);'
g+='\\draw[thick] (.22,1.5) -- (1.25,1.15);\\draw[thick] (.22,1.28) -- (1.25,.95);'
g+='\\draw[thick] (-.7,-1.15) rectangle (.7,-1.4);\\foreach \\x in {-.35,0,.35}{\\draw[thick,'+ARR+'] (\\x,-1.1) -- (\\x,-.95);}'
g+=f'\\begin{{scope}}[shift={{(1.3,1.05)}},rotate={al}]\\draw[thick] (0,-.3) rectangle (3,.3);\\draw[thick] (0,-.08) -- (3.35,-.08);\\draw[thick] (0,.08) -- (3.35,.08);'
g+=f'\\draw[thick,{ARR}] (2.5,-.95) -- (2.5,-.3);\\draw[thick,{ARR}] (.5,.3) -- (.5,.95);\\end{{scope}}'
ex=1.3+3.35*math.cos(math.radians(-al)); ey=1.05-3.35*math.sin(math.radians(-al))
g+=f'\\draw[thick] ({ex:.3f},{ey:.3f}) -- ({ex+.12:.3f},-1.0);'
rx=ex+.1
g+=f'\\draw[thick] ({rx-.65:.3f},-2.35) -- ({rx-.25:.3f},-1.2) -- ({rx+.25:.3f},-1.2) -- ({rx+.65:.3f},-2.35) -- cycle;\\fill[vurgu!15] ({rx-.6:.3f},-2.3) -- ({rx-.5:.3f},-2.0) -- ({rx+.5:.3f},-2.0) -- ({rx+.6:.3f},-2.3) -- cycle;'
lab=lambda n,x,y:f'\\node[circle,draw,inner sep=1.2pt,font=\\footnotesize] at ({x},{y}) {{{n}}};'
g+=lab(1,-1.3,.2)+lab(2,.65,2.6)+lab(3,3.0,1.45)+lab(4,rx+1.1,-1.7)
SK20=tk(g)
d={'I':(True,'kaynama noktası düşük olan bileşen önce buharlaşır, soğutucuda yoğuşarak toplama kabında birikir'),
   'II':(True,'soğutucuda buhar, soğuk yüzeyle temas edip yoğuşarak sıvıya dönüşür'),
   'III':(False,'termometre balondaki sıvıya değil, yan koldan çıkan buharın sıcaklığını ölçmek için kolun hizasında durur; sıvıya daldırılmaz')}
r=onc_t(d,1)
q('0020',ad=[A('Düzeneği tanı','Balon ısıtılır, buhar yan kola geçer, soğutucuda yoğuşur, toplama kabında birikir.','1: balon · 2: termometre · 3: soğutucu · 4: toplama kabı'),adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),A('Sonucu yaz','Doğru olan öncüller bir arada yazılır.',oy(d)+' · Sonuç: I ve II')],
 alt='Karışımların Ayrılması',z='orta',kaz='Basit damıtma düzeneğinin bölümlerini ve işleyişini yorumlar.',kalip='şekilli',
 kart='K-KMKR2-20 (basit damıtma düzeneği) · 1, 2, 3, 4 numaralı kısımlar',
 metin='Kaynama noktaları farklı iki sıvıdan oluşan homojen bir karışımı ayırmak için şekildeki düzenek kurulmuştur. Balon sabit kuvvetli bir ısıtıcıyla ısıtılmakta; sıvılardan biri diğerinden çok daha düşük sıcaklıkta kaynamaktadır. Düzenekte numaralanan kısımlar gösterilmiştir.\nI. Kaynama noktası düşük olan sıvı, 1 numaralı balondan ilk olarak ayrılıp 4 numaralı kapta toplanır.\nII. 3 numaralı kısımda buhar yoğuşur.\nIII. 2 numaralı termometrenin haznesi balondaki sıvıya daldırılmalıdır.\nBuna göre hangileri doğrudur?',
 sekil=SK20,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan öncüller.',
 ip=['Damıtmada buharın izlediği yolu balondan toplama kabına kadar takip et; ölçülen sıcaklığın neyin sıcaklığı olduğunu düşün.'],
 bilgi=[B('Basit damıtma','Basit damıtma, bileşenlerin kaynama noktalarının farklı olmasına dayanır. Örnek: deniz suyundan saf su elde etmek')],
 puf='Damıtmada kaynama noktası düşük sıvı önce buharlaşır, soğutucuda yoğuşup toplanır; termometre buhar sıcaklığını ölçer.')

# ============================================================ 21 · ayırma hunisi
hy,hs=4,6; al_,doy_y,doy_s=20,Fr(8,10),1
V_s=hs*al_; m_s=V_s*doy_s; m_y=hy*al_*doy_y
assert m_s==120 and m_y==64 and hy*al_==80 and hs*al_*doy_y==96 and m_s+m_y==184
sc=.45
g=(f'\\fill[vurgu!15] (0,0) rectangle (1.8,{hs*sc});\\fill[black!8] (0,{hs*sc}) rectangle (1.8,{(hs+hy)*sc});'
   f'\\draw[thick] (0,{(hs+hy)*sc+.35}) -- (0,0) -- (1.8,0) -- (1.8,{(hs+hy)*sc+.35});'
   f'\\draw[thick] (0,{hs*sc}) -- (1.8,{hs*sc});'
   f'\\draw[thick,fill=white] (.5,{(hs+hy)*sc+.35}) rectangle (1.3,{(hs+hy)*sc+.6});'
   '\\draw[thick] (.9,0) -- (.9,-.3);\\draw[thick,fill=white] (.65,-.3) rectangle (1.15,-.5);\\draw[thick] (1.15,-.4) -- (1.75,-.4);'
   '\\draw[thick] (.9,-.5) -- (.9,-.85);')
g+=f'\\draw[{ARR}] (2.3,{hs*sc+(hy*sc)/2}) -- (2.3,{hs*sc});\\draw[{ARR}] (2.3,{hs*sc+(hy*sc)/2}) -- (2.3,{(hs+hy)*sc});\\node[right,font=\\small] at (2.4,{hs*sc+(hy*sc)/2}) {{{hy} cm}};'
g+=f'\\draw[{ARR}] (2.3,{hs*sc/2}) -- (2.3,0);\\draw[{ARR}] (2.3,{hs*sc/2}) -- (2.3,{hs*sc});\\node[right,font=\\small] at (2.4,{hs*sc/2}) {{{hs} cm}};'
SK21=tk(g)
q('0021',ad=[A('Katmanları ayır','Özkütlesi büyük sıvı altta, küçük sıvı üstte toplanır.','alt katman: su (1,0) · üst katman: yağ (0,8)'),A('Alt katman hacmi','Silindirik gövdede hacim kesit alanı × yükseklik.','V = 20 × 6 = 120 cm³'),A('Kütleyi hesapla','Kütle özkütle ile hacmin çarpımıdır.','m = 1,0 × 120 = 120 g')],
 alt='Karışımların Ayrılması',z='orta',kaz='Ayırma hunisindeki karışmayan sıvıları özkütlelerine göre ayırarak alt katmanın kütlesini hesaplar.',kalip='şekilli',
 kart='K-KMKR2-21 (ayırma hunisi ve özkütle) · su–yağ, iki katman',
 metin='Biri su, diğeri yağ olan, birbirine karışmayan iki sıvı silindirik gövdeli bir ayırma hunisine konulmuş ve beklenmiştir; katmanların yükseklikleri şekilde verilmiştir. Suyun özkütlesi 1,0 g/cm³, yağın özkütlesi 0,8 g/cm³’tür. Hunin iç kesit alanı her yükseklikte 20 cm²’dir. Musluk açılarak alt katmanın tamamı boş bir kaba aktarılmaktadır.\nBuna göre boş kaba aktarılan sıvının kütlesi kaç gramdır?',
 sekil=SK21,dogru=120,yan=[(64,'Üst katmanı alta aktarılan sanıp yağın kütlesini hesaplamış.','dikkat'),(80,'Üst katmanın hacmini (4 × 20) kütle olarak yazmış.','dikkat'),(96,'Alt katmanın hacmine 0,8 g/cm³ özkütlesini uygulamış; hangi katmanın su olduğunu bulamamış.','bilgi'),(184,'Su ve yağın kütlelerini toplamış.','islem')],
 istenen='Boş kaba aktarılan sıvının kütlesi (g).',
 ip=['Katmanların konumunu belirleyen özelliği düşün; şekildeki uzunlukları hacme çevirmen gerekecek.'],
 bilgi=[B('Özkütle ve ayırma hunisi','Karışmayan sıvılardan özkütlesi büyük olan altta kalır, musluktan önce alt katman alınır. Kütle = özkütle × hacim. Örnek: özkütlesi 1,2 g/cm³ olan 50 cm³ sıvının kütlesi 60 g’dır')],
 puf='Özkütlesi büyük sıvı altta kalır; alt katmanın kütlesi hacim ile özkütlenin çarpımıdır.')

# ============================================================ 22 · ayırma yöntemi seçimi tablosu (olumsuz)
dogruSat=[('Demir tozu – kum','mıknatıslanma farkı','mıknatıs kullanma'),
          ('Zeytinyağı – su','karışmama, özkütle farkı','ayırma hunisi'),
          ('Kum – tuz','çözünürlük farkı','çözme–süzme–buharlaştırma'),
          ('Tuzlu su','kaynama noktası farkı','basit damıtma')]
yanlisSat=('Etil alkol – su','özkütle farkı','ayırma hunisi')
hed22=4
sat22=list(dogruSat); sat22.insert(hed22,yanlisSat)
harf22=['K','L','M','N','P']
# tablodaki satır etiketleri: karışım adının başına harf
SK22=tablo_svg(['','Karışım','Ayırmaya dayanak özellik','Yöntem'],[[h,a,b,c] for h,(a,b,c) in zip(harf22,sat22)])
# metinler düzgün Türkçe: nedenleri elle yaz
nedenler={'K':'mıknatıs demir tozunu çeker, kuma etki etmez; eşleştirme doğrudur','L':'zeytinyağı ile su karışmaz ve özkütleleri farklıdır; ayırma hunisiyle ayrılır, eşleştirme doğrudur','M':'tuz suda çözünür, kum çözünmez; çözme–süzme–buharlaştırma uygundur','N':'tuz buharlaşmaz, su damıtmayla ayrılır; eşleştirme doğrudur'}
yan22=[]
for i in range(5):
    if i==hed22: continue
    h=harf22[i]
    nd={'Demir tozu – kum':nedenler['K'],'Zeytinyağı – su':nedenler['L'],'Kum – tuz':nedenler['M'],'Tuzlu su':nedenler['N']}[sat22[i][0]]
    yan22.append((h,f'Bu satırı yanlış sanmış; oysa {nd}.','bilgi'))
dd=dict(dogru=harf22[hed22],yan=yan22,sira=harf22)
q('0022',ad=[A('Satırları tanı','Her karışım için ayırmaya dayanan özellik ve uygulanan yöntem verilmiştir.','5 karışım · 5 yöntem'),A('Doğru eşleşmeleri ele','Mıknatıs, ayırma hunisi, çözme–süzme ve damıtma sırasıyla uygun satırlarda kullanılmıştır.','4 satır: doğru'),A('Hatalı satırı bul','Etil alkol ve su birbiri içinde çözünür; tek fazlıdır, ayırma hunisiyle ayrılamaz.','etil alkol – su: kaynama noktası farkı → damıtma'),A('Sonucu yaz','Hatalı eşleşmeyi içeren satırın harfi seçilir.',f'{harf22[hed22]}')],
 alt='Karışımların Ayrılması',z='orta',kaz='Karışımlar için uygun ayırma yöntemini ayırt edici özelliğe göre seçer.',kalip='tablo',
 kart='K-KMKR2-22 (ayırma yöntemi seçimi) · beş karışım ve yöntem tablosu',
 metin='Bir öğrenci, karışımları ayırmada kullanılan yöntemleri tablodaki gibi özetlemiş: her satırda karışımı, ayrılmasına dayanak olan özelliği ve uygulanacak yöntemi yazmıştır. Öğretmeni, satırların birinde karışım için yazılan yöntemin o karışıma uygulanamayacağını söylemiştir.\nBuna göre hangi satırdaki eşleştirme yanlıştır?',
 sekil=SK22,dogru=dd['dogru'],yan=dd['yan'],sira=dd['sira'],istenen='Yanlış eşleştirme içeren satır.',
 ip=['Her satırda yöntemin dayandığı özellik, karışımda gerçekten var mı?'],
 bilgi=[B('Ayırma yöntemleri','Ayırma yöntemi seçilirken bileşenlerin hâli, çözünürlüğü, mıknatıslanması, kaynama noktası ve özkütlesi karşılaştırılır; yöntem karışımın türüne uygun olmalıdır. Örnek: kükürt–talaş karışımı suya atılınca özkütle farkıyla ayrılır')],
 puf='Ayırma hunisi yalnız birbirine karışmayan sıvılar içindir; birbiri içinde çözünen sıvılar damıtılır.')

bitir(P,'karisimlariki',UK)
