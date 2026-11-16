"""TYT Fizik · Madde ve Özellikleri · ek paket (maddeiki): 18 soru, kardeş yok, ipucu 1. Şekil verileri Python'da hesaplanır, TikZ bu değerlerden üretilir.
Her cevap ve çeldirici değer assert edilir; öncüllerin doğruluğu TEK yerde (ONC) tanımlanır, adımlar/çeldirici açıklamaları oradan üretilir."""
import sys,os,json,importlib.util
from math import sin,cos,radians,pi,atan2,degrees
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,GD)
import _hafif as H
from _hafif import *
from cizim import tikz_svg
spec=importlib.util.spec_from_file_location('hm',os.path.join(HV,'tyt-mat','_hafif_mat.py')); HM=importlib.util.module_from_spec(spec); spec.loader.exec_module(HM)
tablo_svg=HM.tablo_svg
KONU_='Madde ve Özellikleri'; UK='fiz|Madde ve Özellikleri'
H.KONU=KONU_
P=Parti('maddeiki',KONU_,UK,ders='TYT Fizik',idon='tytfiz')
KY='ÖSYM 2018–2026 TYT Fizik (yalnız mantık) · MEB 9. sınıf Madde ve Özellikleri'
def kartla(n,alt,fikir,tuzak,z,kalip,adim,tipad,tip):
    kart(f'K-FZMD2-{n}',alt,fikir,tuzak,z,kalip,adim,f'fz-md2-{tipad}',tip,KY)
def q(no,ad,**k):
    assert len(k['ip'])==1
    mk(P,no,ad=ad,adim=len(ad),**k)
HEAD='\\begin{tikzpicture}[scale=1.3,every node/.style={scale=1.2},line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
def tk(g): return tikz_svg(HEAD+g+TAIL)
ORD=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
KUME={'Yalnız I':{1},'Yalnız II':{2},'Yalnız III':{3},'I ve II':{1,2},'I ve III':{1,3},'II ve III':{2,3},'I, II ve III':{1,2,3}}
ROM={1:'I',2:'II',3:'III'}
def etiket(s): return [o for o in ORD if KUME[o]==set(s)][0]
def pick(dogru,t):
    """doğru küme ORD içinde t seçenek öne gelecek biçimde beş şık seç (harf dengesi için)."""
    ci=ORD.index(dogru); once=ORD[:ci]; sonra=ORD[ci+1:]
    assert len(once)>=t and len(sonra)>=4-t,(dogru,t)
    return (once[len(once)-t:] if t else [])+[dogru]+sonra[:4-t]
def onc(truth,kisa,yanl_dogru,yanl_yanlis):
    """truth: (bool,bool,bool). kisa: yargı başına doğru kavram açıklaması (adım). yanl_dogru[i]: yanlış yargıyı doğru sanma nedeni;
    yanl_yanlis[i]: doğru yargıyı yanlış sanma nedeni. Dönen: (dogru etiket, adımlar, cel fonksiyonu)"""
    d={i+1 for i,v in enumerate(truth) if v}; et=etiket(d)
    ad=[A(f'{ROM[i+1]}. yargıyı değerlendir',kisa[i],f'{ROM[i+1]}: '+('doğru' if truth[i] else 'yanlış')) for i in range(3)]
    ad.append(A('Sonuç','Doğru olan yargılar birleştirilir.',et))
    def cel(sec):
        ks=KUME[sec]; out=[]
        for i in sorted(ks-d): out.append(f'{ROM[i]} yargısını doğru saymış: '+yanl_dogru[i-1])
        for i in sorted(d-ks): out.append(f'{ROM[i]} yargısını yanlış saymış: '+yanl_yanlis[i-1])
        return ' '.join(out)
    return et,ad,cel
def oncq(no,truth,t,kisa,yd,yy,tur=None,**k):
    et,ad,cel=onc(truth,kisa,yd,yy)
    sira=pick(et,t); yan=[(s,cel(s),(tur or {}).get(s,'bilgi')) for s in sira if s!=et]
    q(no,ad,dogru=et,sira=sira,yan=yan,**k)
    return et

# ---------- çizim yardımcıları ----------
def silindir(x,level,ymax=100,hh=3.6,w=.8,blob=False,adim=10,lab=20,fill=True):
    u=hh/ymax; s=''
    if fill and level>0: s+=f'\\fill[vurgu!18] ({x},0) rectangle ({x+w},{level*u:.3f});'
    s+=f'\\draw[thick] ({x},{hh+.15:.3f}) -- ({x},0) -- ({x+w},0) -- ({x+w},{hh+.15:.3f});'
    if level>0: s+=f'\\draw[vurgu!60!black,thick] ({x},{level*u:.3f}) -- ({x+w},{level*u:.3f});'
    for t in range(adim,ymax+1,adim):
        L=.2 if t%lab==0 else .1
        s+=f'\\draw ({x+w},{t*u:.3f}) -- ({x+w-L},{t*u:.3f});'
        if t%lab==0: s+=f'\\node[right,font=\\scriptsize,inner sep=1pt] at ({x+w},{t*u:.3f}) {{{t}}};'
    if blob: s+=f'\\draw[fill=gray!55] ({x+.2},.03) .. controls ({x+.08},.4) and ({x+.5},.55) .. ({x+.6},.22) .. controls ({x+.66},.03) and ({x+.45},.0) .. cycle;'
    return s
def kutu(x,y,w,h,fill='gray!45'): return f'\\draw[thick,fill={fill}] ({x},{y}) rectangle ({x+w},{y+h});'
def mgraf(cizgiler,xt,yt,xmax=40,ymax=40,ux=.12,uy=.075):
    s=f'\\draw[-{{Stealth}},thick] (0,0) -- ({xmax*ux+.3:.2f},0) node[right] {{$V$ (cm$^3$)}};\\draw[-{{Stealth}},thick] (0,0) -- (0,{ymax*uy+.3:.2f}) node[above] {{$m$ (g)}};'
    for t in xt: s+=f'\\draw ({t*ux:.3f},0) -- ({t*ux:.3f},-.07) node[below,font=\\scriptsize,inner sep=2pt] {{{t}}};'
    for t in yt: s+=f'\\draw (0,{t*uy:.3f}) -- (-.07,{t*uy:.3f}) node[left,font=\\scriptsize,inner sep=2pt] {{{t}}};'
    for ad,(v,m) in cizgiler:
        sl=m/v; ev=min((ymax-3)/sl,xmax-2); em=ev*sl
        s+=f'\\draw[vurgu,very thick] (0,0) -- ({ev*ux:.3f},{em*uy:.3f}) node[above,vurgu!60!black] {{\\textbf{{{ad}}}}};'
        s+=f'\\draw[dashed,gray] (0,{m*uy:.3f}) -- ({v*ux:.3f},{m*uy:.3f}) -- ({v*ux:.3f},0);\\fill ({v*ux:.3f},{m*uy:.3f}) circle (1.6pt);'
    return s
def sekil_kap(x,adlar):  # basit beher
    return ''

# =================== 01 · dereceli silindir ile özkütle · kolay ===================
kartla('01','Dereceli silindirle hacim ve özkütle','Düzgün olmayan katının hacmi, dereceli silindirdeki seviye farkından okunur; özkütle d = m ÷ V ile bulunur.','Son seviyeyi ya da ilk seviyeyi hacim sanmak.','kolay','şekilli',3,'silindir','Dereceli silindirle özkütle')
m1,a1,b1=180,40,60; V1=b1-a1; d1=Fr(m1,V1)
assert V1==20 and d1==9 and Fr(m1,a1)==Fr(9,2) and Fr(m1,b1)==3 and Fr(m1,a1+b1)==Fr(9,5) and Fr(m1,10)==18
g=silindir(0,a1)+silindir(2.5,b1,blob=True)
g+='\\node[below] at (.4,-.05) {Önce}; \\node[below] at (2.9,-.05) {Sonra};'
q('0001',tipId='fz-md2-silindir',tip='Dereceli silindirle özkütle',z='kolay',alt='Kütle, Hacim ve Özkütle',kaz='Dereceli silindirdeki seviye farkından hacmi okuyup özkütleyi hesaplar.',kalip='şekilli',
 kart='K-FZMD2-01 (dereceli silindir, özkütle) · seviye farkı',sekil=tk(g),
 metin='Bir öğrenci, düzgün olmayan şekilli ve suda çözünmeyen bir metal parçanın özkütlesini bulmak istiyor. Önce parçayı hassas terazide tartıp kütlesini 180 g buluyor. Sonra içinde su bulunan dereceli silindire parçayı, tamamen suya batacak ve su dışarı taşmayacak biçimde yavaşça bırakıyor. Silindirdeki su seviyesinin parça bırakılmadan önceki ve bırakıldıktan sonraki durumu şekilde gösterilmiştir. Parça suyu emmemekte ve ölçümlerde hava kabarcığı kalmamaktadır.\nBuna göre metal parçanın özkütlesi kaç g/cm³’tür?',
 dogru=9,yan=[(Fr(9,5),'İki seviyeyi toplayıp (40 + 60 = 100 cm³) kütleyi buna bölmüş.','islem'),(3,'Son seviyeyi (60 cm³) parçanın hacmi sanmış; parçanın hacmi seviye farkıdır.','dikkat'),(Fr(9,2),'İlk seviyeyi (40 cm³) parçanın hacmi sanmış; parçanın hacmi seviye farkıdır.','dikkat'),(18,'Bölme aralığını (10 cm³) hacim sanmış; parçanın hacmi okunan seviyelerin farkıdır.','dikkat')],
 istenen='Metal parçanın özkütlesi (g/cm³).',ip=['Parçanın hacmini nasıl ölçebileceğini düşün: iki görünüm arasında silindirde ne değişti?'],
 bilgi=[B('Özkütle','d = m ÷ V (kütle ÷ hacim). Örnek: 120 g kütleli, 30 cm³ hacimli cismin özkütlesi 4 g/cm³'),B('Hacim ölçme','düzgün olmayan katı cismin hacmi, dereceli silindirde cisim bırakıldığında su seviyesinin yükselme miktarıdır. Örnek: seviye 50’den 65 cm³’e çıkıyorsa cismin hacmi 15 cm³’tür')],
 ad=[A('Seviyeleri oku','Silindirdeki ilk ve son seviye ölçek üzerinden okunur.','ilk = 40 cm³ · son = 60 cm³'),A('Hacmi bul','Yükselen su, cismin yer değiştirdiği hacme eşittir.','V = 60 − 40 = 20 cm³'),A('Özkütleyi hesapla','Kütle hacme bölünür.','d = 180 ÷ 20 = 9 g/cm³')],
 puf='Düzgün olmayan cismin hacmi için sonuç seviyesinden ilk seviyeyi çıkar; özkütleyi m ÷ V ile bul.')

# =================== 02 · m–V grafiği eğim · kolay · öncüllü ===================
kartla('02','m–V grafiğinde özkütle karşılaştırma','Orijinden geçen doğrunun eğimi özkütledir; eşit hacimde kütlesi büyük olan, eşit kütlede hacmi küçük olandır.','Hacmi büyük olana özkütlesi büyük demek.','kolay','grafik',3,'grafik','Kütle–hacim grafiğinden özkütle karşılaştırma')
dX,dY,dZ=Fr(30,10),Fr(30,20),Fr(30,30); assert (dX,dY,dZ)==(3,Fr(3,2),1) and dX>dY>dZ
# I: eşit hacimde m = d·V → kütlesi en büyük X (doğru). II: eşit kütlede V = m/d → hacmi en büyük Z (doğru). III: Y/Z = 3/2 (yanlış, 3 kat değil).
# II'yi YANLIŞ yapmak için "X" yazılır: eşit kütlede hacmi en büyük olan en küçük özkütleli Z'dir, X değil.
assert dY/dZ==Fr(3,2)
g=mgraf([('X',(10,30)),('Y',(20,30)),('Z',(30,30))],[10,20,30],[30,40])
oncq('0002',(True,False,False),0,
 ['Eşit hacimde m = d × V olduğundan eğimi (özkütlesi) en büyük olan X’in kütlesi en büyüktür.','Eşit kütlede V = m ÷ d; hacmi en büyük olan, özkütlesi en küçük olan Z’dir, X değil.','Eğimlerden dY = 30 ÷ 20 = 1,5 ve dZ = 30 ÷ 30 = 1 g/cm³ olur; oran 3 değil, 1,5’tir.'],
 ['','Eşit kütlede özkütlesi büyük olanın hacminin de büyük olacağını düşünmüş; V = m ÷ d bağıntısını kullanmamış.','Grafikte 30 g’da hacim oranı 30 ÷ 10 = 3 olan X–Z çiftini Y–Z ile karıştırmış (dX = 3, dZ = 1 g/cm³); oysa dY = 1,5 g/cm³’tür.'],
 ['Eşit hacimde kütle farkını, özkütlenin eğimle gösterildiğini bilmediği için görememiş.','','' ],
 tur={},
 kart='K-FZMD2-02 (m–V grafiği, özkütle) · üç doğru, öncüllü',kalip='grafik',tipId='fz-md2-grafik',tip='Kütle–hacim grafiğinden özkütle karşılaştırma',z='kolay',alt='Kütle, Hacim ve Özkütle',kaz='Kütle–hacim grafiğindeki doğruların eğiminden özkütleleri karşılaştırır.',sekil=tk(g),
 metin='Bir öğrenci, suda çözünmeyen ve içi dolu X, Y ve Z katı maddelerinden farklı büyüklükte parçalar alıp her parçanın kütlesini ve hacmini ölçüyor. Aynı maddeye ait ölçüm sonuçları kütle–hacim grafiğinde orijinden geçen bir doğru oluşturuyor; üç maddenin grafiği şekilde verilmiştir. Ölçümler aynı sıcaklıkta yapılmış ve bütün parçalar homojendir.\nI. Eşit hacimli parçalar alındığında kütlesi en büyük olan X’tir.\nII. Eşit kütleli parçalar alındığında hacmi en büyük olan X’tir.\nIII. Y’nin özkütlesi, Z’nin özkütlesinin 3 katıdır.\nBuna göre bu yargılardan hangileri doğrudur?',
 istenen='Doğru olan yargılar.',ip=['Doğruların birbirine göre dik ya da yatık olmasının hangi niceliği yansıttığını düşün.'],
 bilgi=[B('Kütle–hacim grafiği','m = d × V olduğundan orijinden geçen doğrunun eğimi özkütledir; doğru ne kadar dikse özkütle o kadar büyüktür. Örnek: (10 cm³, 20 g) noktasından geçen doğrunun özkütlesi 2 g/cm³’tür')],
 puf='m–V grafiğinde dik doğru büyük özkütle demektir; eşit kütlede hacim, özkütle ile ters değişir.')

# =================== 03 · ortak ve ayırt edici özellikler · kolay · tablo ===================
kartla('03','Ortak ve ayırt edici özellikler','Kütle ve hacim madde miktarına bağlı ortak özelliklerdir; özkütle maddeyi tanıtan ayırt edici özelliktir. Aynı maddeden yapılan cisimlerin özkütlesi eşittir.','Kütle ya da hacmi eşit olan cisimleri aynı maddeden sanmak.','kolay','tablo',3,'ortak','Ortak ve ayırt edici özellikler')
T3={'A':(54,20),'B':(54,30),'C':(135,50),'D':(40,20)}; ozk={k:Fr(m,v) for k,(m,v) in T3.items()}
assert ozk['A']==ozk['C']==Fr(27,10) and ozk['B']==Fr(9,5) and ozk['D']==2 and len(set(ozk.values()))==3
assert T3['A'][0]==T3['B'][0] and T3['A'][1]==T3['D'][1]
tb=tablo_svg(['Cisim','Kütle (g)','Hacim (cm³)'],[[k,str(m),str(v)] for k,(m,v) in T3.items()])
S3=['A ve B','A ve C','A ve D','B ve D','C ve D']
q('0003',tipId='fz-md2-ortak',tip='Ortak ve ayırt edici özellikler',z='kolay',alt='Ortak ve Ayırt Edici Özellikler',kaz='Kütle ve hacmin ortak, özkütlenin ayırt edici özellik olduğunu kullanarak aynı maddeden yapılmış cisimleri belirler.',kalip='tablo',
 kart='K-FZMD2-03 (ayırt edici özellik) · dört cisim tablosu',sekil=tb,
 metin='Bir laboratuvarda, her biri tek cins maddeden yapılmış, içi dolu ve homojen dört katı cisim bulunuyor. Cisimlerin kütleleri hassas terazide, hacimleri ise taşırma kabı ile ölçülmüş ve sonuçlar aşağıdaki tabloda verilmiştir. Öğretmen, öğrencilerden hangi cisimlerin aynı maddeden yapıldığını belirlemelerini istiyor.\nBuna göre bu cisimlerden hangi ikisi aynı maddeden yapılmış olabilir?',
 dogru='A ve C',sira=S3,yan=[('A ve B','Kütleleri eşit olan cisimleri aynı maddeden sanmış; kütle madde miktarına bağlı ortak bir özelliktir.','bilgi'),('A ve D','Hacimleri eşit olan cisimleri aynı maddeden sanmış; hacim de ortak özelliktir.','bilgi'),('B ve D','Özkütleleri birbirine yakın çıkan (1,8 ve 2 g/cm³) cisimleri aynı sanmış; özkütleler tam olarak eşit olmalıdır.','dikkat'),('C ve D','Özkütleyi hesaplamadan seçmiş; C’nin özkütlesi 2,7, D’ninki 2 g/cm³’tür.','islem')],
 istenen='Aynı maddeden yapılmış olabilecek cisim çifti.',ip=['Kütle ve hacim madde miktarıyla değişir; iki veriden maddeyi tanıtan başka bir nicelik türetmeyi dene.'],
 bilgi=[B('Ortak ve ayırt edici özellik','kütle, hacim ve eylemsizlik madde miktarına bağlı ortak özelliklerdir. Özkütle, erime ve kaynama sıcaklığı gibi özellikler maddeyi tanıtır. Örnek: 10 g ve 40 g kütleli iki demir parçanın kütleleri farklıdır, özkütleleri eşittir')],
 ad=[A('Özkütleleri bul','Ayırt edici özellik özkütledir; her cisim için d = m ÷ V.','A: 54 ÷ 20 = 2,7 · B: 54 ÷ 30 = 1,8'),A('Devam et','Aynı işlemi C ve D için uygula.','C: 135 ÷ 50 = 2,7 · D: 40 ÷ 20 = 2'),A('Eşitleri bul','Aynı maddenin özkütlesi aynıdır.','dA = dC = 2,7 g/cm³'),A('Elemeyi kontrol et','Kütlesi eşit (A, B) ya da hacmi eşit (A, D) olanların özkütlesi farklıdır.','A–B: 2,7 ≠ 1,8 · A–D: 2,7 ≠ 2')],
 puf='Aynı maddeyi bulmak için kütle ya da hacme değil, kütle ÷ hacim oranına (özkütleye) bak.')

# =================== 04 · menisküs · adezyon ve kohezyon · kolay · öncüllü ===================
kartla('04','Menisküs ve yapışma','Sıvı yüzeyinin cam tüpte çukur olması adezyonun, tümsek olması kohezyonun üstünlüğünü gösterir.','Su ile cıvanın camı aynı ölçüde ıslattığını sanmak.','kolay','şekilli',4,'yapisma','Menisküs, adezyon ve kohezyon')
def tup(x,tur,ylev=1.5):
    w=.9; s=f'\\draw[thick] ({x},2.6) -- ({x},0) -- ({x+w},0) -- ({x+w},2.6);'
    if tur=='su': s+=f'\\fill[vurgu!18] ({x},0) -- ({x},{ylev+.28}) .. controls ({x+.2},{ylev+.02}) and ({x+w-.2},{ylev+.02}) .. ({x+w},{ylev+.28}) -- ({x+w},0) -- cycle;'
    else: s+=f'\\fill[gray!50] ({x},0) -- ({x},{ylev}) .. controls ({x+.1},{ylev+.34}) and ({x+w-.1},{ylev+.34}) .. ({x+w},{ylev}) -- ({x+w},0) -- cycle;'
    return s
g=tup(0,'su')+tup(2,'cıva',1.5)+'\\node[below] at (.45,-.05) {K}; \\node[below] at (2.45,-.05) {L};'
ONC4=oncq('0004',(False,True,True),3,
 ['Suyun yüzeyinin çukur olması, cam ile su arasındaki çekimin (adezyon) su moleküllerinin birbirini çekmesinden (kohezyon) büyük olduğunu gösterir; yargı bunun tersini söylüyor.','Cıvanın yüzeyinin tümsek olması, cıva moleküllerinin birbirini çekmesinin cam ile arasındaki çekimden büyük olduğunu gösterir.','Su camı ıslatır (adezyon baskın), cıva camı ıslatmaz (kohezyon baskın).'],
 ['Çukur yüzeyi, kohezyonun adezyondan büyük olmasına bağlamış.','',''],
 ['','Tümsek yüzeyin cıvanın kendi molekülleri arasındaki çekimle ilgisini görememiş.','Camı ıslatma kavramını adezyonun baskın olmasıyla ilişkilendirememiş.'],
 kalip='şekilli',kart='K-FZMD2-04 (menisküs) · su ve cıva tüpleri, öncüllü',tipId='fz-md2-yapisma',tip='Menisküs, adezyon ve kohezyon',z='kolay',alt='Yapışma ve Birbirini Tutma',kaz='Menisküsün biçiminden adezyon ve kohezyon üstünlüğünü yorumlar.',sekil=tk(g),
 metin='Fizik laboratuvarında aynı cinsten, aynı çaplı iki temiz cam tüpün birine su, diğerine cıva konuluyor. Tüplerdeki sıvıların yüzeyleri cam çeperin yakınında şekilde görüldüğü gibi farklı biçimler alıyor. K tüpünde su, L tüpünde cıva bulunmaktadır ve ölçümler aynı sıcaklıkta yapılmıştır. Öğrenciler, bu görünümü sıvı moleküllerinin birbirini ve cam moleküllerini çekmesiyle ilişkilendiriyor.\nI. K tüpünde suyun yüzeyinin çukur olması, adezyonun kohezyondan küçük olduğunu gösterir.\nII. L tüpünde cıvanın yüzeyinin tümsek olması, kohezyonun adezyondan büyük olduğunu gösterir.\nIII. Su camı ıslatır, cıva camı ıslatmaz.\nBuna göre bu yargılardan hangileri doğrudur?',
 istenen='Doğru olan yargılar.',ip=['Sıvı yüzeylerinin cam çeperin yanında hangi yöne kıvrıldığına bak.'],
 bilgi=[B('Adezyon ve kohezyon','adezyon, farklı cins moleküller arasındaki çekimdir (su–cam); kohezyon, aynı cins moleküller arasındaki çekimdir (su–su). Adezyon baskınsa sıvı camı ıslatır ve yüzeyi çukur olur; kohezyon baskınsa yüzey tümsek olur. Örnek: cam tüpteki su çeperde yukarı tırmanır')],
 puf='Yüzey çukursa adezyon baskındır (ıslatır); tümsekse kohezyon baskındır (ıslatmaz).')

# =================== 05 · taşırma kabı · orta ===================
kartla('05','Taşırma kabı ve özkütle','Taşan su hacmi, batan cismin hacmine eşittir; ardışık eklemelerde hacim farkından ikinci cismin hacmi bulunur.','Toplam taşan hacmi ikinci cismin hacmi sanmak.','orta','şekilli',4,'silindir','Taşırma kabı ve ardışık hacim')
mX,mY=90,120; vX,vXY=30,50; vY=vXY-vX; dXk=Fr(mX,vX); dYk=Fr(mY,vY)
assert vY==20 and dXk==3 and dYk==6 and Fr(mY,vXY)==Fr(12,5) and Fr(mY,vX)==4 and Fr(mX+mY,vY)==Fr(21,2)
def tasirma(x,cis,seviye,ymax=60,hh=2.0):
    s=f'\\fill[vurgu!18] ({x},0) rectangle ({x+1.8},2.5);\\draw[thick] ({x},2.9) -- ({x},0) -- ({x+1.8},0) -- ({x+1.8},2.5) -- ({x+2.3},2.3);'
    cx=x+.2
    for ad,w in cis: s+=kutu(cx,.05,w,.5)+f'\\node[font=\\scriptsize] at ({cx+w/2},.3) {{{ad}}};'; cx+=w+.15
    sx=x+1.975
    s+=f'\\draw[dotted,thick] ({sx+.325:.3f},2.25) -- ({sx+.325:.3f},{seviye*hh/ymax+.05:.3f});'
    s+=silindir(sx,seviye,ymax=ymax,hh=hh,w=.65,adim=10,lab=10).replace('\\node[right,font=\\scriptsize,inner sep=1pt]','\\node[right,font=\\tiny,inner sep=1pt]')
    return s
g=tasirma(0,[('X',.7)],vX)+tasirma(4.0,[('X',.7),('Y',.5)],vXY)
g+='\\node[below] at (1.3,-.1) {X bırakıldığında}; \\node[below] at (5.3,-.1) {Y de bırakıldığında};'
q('0005',tipId='fz-md2-silindir',tip='Taşırma kabı ve ardışık hacim',z='orta',alt='Kütle, Hacim ve Özkütle',kaz='Taşırma kabında ardışık taşan su hacimlerinden cismin hacmini ve özkütlesini bulur.',kalip='şekilli',
 kart='K-FZMD2-05 (taşırma kabı) · ardışık iki cisim',sekil=tk(g),
 metin='Ağzına kadar su dolu bir taşırma kabında, ağızdaki oluktan taşan su altına konulan dereceli silindirde toplanıyor. Kaba önce kütlesi 90 g olan X cismi, ardından kütlesi 120 g olan Y cismi yavaşça bırakılıyor. İki cisim de suda çözünmüyor, suyu emmez ve tamamen suya batar. Silindirdeki su seviyesi X bırakıldıktan sonra ve Y de bırakıldıktan sonra şekilde gösterilmiştir; silindir bu sırada boşaltılmamıştır.\nBuna göre Y cisminin özkütlesi kaç g/cm³’tür?',
 dogru=6,yan=[(Fr(12,5),'Y’nin kütlesini toplam taşan hacme (50 cm³) bölmüş; Y’nin hacmi yalnız ikinci artıştır.','dikkat'),(3,'X’in özkütlesini (90 ÷ 30) Y’nin özkütlesi sanmış.','dikkat'),(4,'Y’nin kütlesini yalnız X’in hacmine (30 cm³) bölmüş.','dikkat'),(Fr(21,2),'Toplam kütleyi (210 g) Y’nin hacmine bölmüş; Y’nin kütlesi alınmalıdır.','islem')],
 istenen='Y cisminin özkütlesi (g/cm³).',ip=['Her cismin hacmini hangi okumalardan bulabileceğini düşün.'],
 bilgi=[B('Taşırma kabı','batan bir cismin taşırdığı su hacmi, cismin hacmine eşittir. Örnek: bir taşı kaba bırakınca 12 cm³ su taşıyorsa taşın hacmi 12 cm³’tür'),B('Özkütle','d = m ÷ V. Örnek: 45 g kütleli, 15 cm³ hacimli cismin özkütlesi 3 g/cm³’tür')],
 ad=[A('Seviyeleri oku','Silindirdeki ölçek her iki durumda okunur.','X: 30 cm³ · X ve Y: 50 cm³'),A('Y’nin hacmini bul','Y’nin taşırdığı su, ikinci artıştır.','V(Y) = 50 − 30 = 20 cm³'),A('Y’nin özkütlesi','Y’nin kütlesi kendi hacmine bölünür.','d = 120 ÷ 20 = 6 g/cm³'),A('Kontrol et','X’in özkütlesi de kendi hacmiyle hesaplanabilir.','dX = 90 ÷ 30 = 3 g/cm³')],
 puf='Ardışık eklemelerde her cismin hacmini kendi artışından bul; toplam hacmi tek bir cisme yazma.')

# =================== 06 · eşit hacim / eşit kütle karışımları · orta · öncüllü ===================
kartla('06','Eşit hacim ve eşit kütle karışımları','Eşit hacimde özkütlelerin ortalaması; eşit kütlede toplam kütle ÷ toplam hacim, ortalamanın altında kalır. Karışımın özkütlesi iki özkütlenin arasındadır.','Her karışımda özkütlelerin aritmetik ortalamasını almak.','orta','şekilli',4,'karisim','Eşit hacim ve eşit kütle karışımları')
dx,dy=Fr(4,5),Fr(6,5); Vh=100; mm_=120
kK=(dx*Vh+dy*Vh)/(2*Vh); kL=(2*mm_)/(Fr(mm_)/dx+Fr(mm_)/dy)
assert kK==1 and kL==Fr(24,25) and kL<kK and dx<kL<kK<dy
def beher(x,lv,etk,fill='vurgu!18',w=1.0,h=2.4):
    return f'\\fill[{fill}] ({x},0) rectangle ({x+w},{lv:.3f});\\draw[thick] ({x},{h}) -- ({x},0) -- ({x+w},0) -- ({x+w},{h});\\node[below,align=center,font=\\scriptsize] at ({x+w/2},-.05) {{{etk}}};'
u6=.0085
g=beher(0,100*u6,'X\\\\100 cm$^3$')+beher(1.5,100*u6,'Y\\\\100 cm$^3$','gray!50')
g+='\\draw[-{Stealth},thick] (2.7,1) -- (3.3,1);'+beher(3.5,200*u6,'K karışımı','vurgu!8')
g+=beher(6.0,float(Fr(mm_)/dx)*u6,'X\\\\120 g')+beher(7.5,float(Fr(mm_)/dy)*u6,'Y\\\\120 g','gray!50')
g+='\\draw[-{Stealth},thick] (8.7,1) -- (9.3,1);'+beher(9.5,float(Fr(mm_)/dx+Fr(mm_)/dy)*u6,'L karışımı','vurgu!8')
oncq('0006',(True,False,True),2,
 ['Eşit hacimde karışımın özkütlesi iki özkütlenin ortalamasıdır: (0,8 + 1,2) ÷ 2 = 1 g/cm³.','L’de toplam kütle 240 g, hacim 150 + 100 = 250 cm³’tür; özkütle 0,96 g/cm³ ile K’nınkinden (1 g/cm³) küçüktür.','Homojen karışımın özkütlesi, karışan sıvıların özkütleleri arasındadır; iki karışım da 0,8 ile 1,2 g/cm³ arasındadır.'],
 ['','Eşit kütlede de hacimlerin eşit olduğunu düşünerek L’nin özkütlesini de 1 g/cm³ almış; oysa hafif sıvının hacmi daha büyüktür.',''],
 ['Eşit hacimde özkütlelerin ortalaması alınacağını bilmemiş.','','Karışımın özkütlesinin bileşenlerin arasında kaldığını kavrayamamış.'],
 kart='K-FZMD2-06 (eşit hacim/kütle) · iki karışımın karşılaştırılması',tipId='fz-md2-karisim',tip='Eşit hacim ve eşit kütle karışımları',z='orta',alt='Karışımların Özkütlesi',kaz='Eşit hacimli ve eşit kütleli karışımların özkütlesini karşılaştırır.',kalip='şekilli',sekil=tk(g),
 metin='Özkütleleri X için 0,8 g/cm³ ve Y için 1,2 g/cm³ olan, birbiri içinde tamamen çözünen iki sıvıdan şekilde gösterilen miktarlarla iki ayrı homojen karışım hazırlanıyor. K karışımında sıvıların hacimleri, L karışımında ise kütleleri birbirine eşittir. Karışma sırasında hacim değişmiyor ve çevreyle madde alışverişi olmuyor.\nI. K karışımının özkütlesi 1 g/cm³’tür.\nII. L karışımının özkütlesi, K karışımının özkütlesinden büyüktür.\nIII. Her iki karışımın özkütlesi de X’inkinden büyük, Y’ninkinden küçüktür.\nBuna göre bu yargılardan hangileri doğrudur?',
 istenen='Doğru olan yargılar.',ip=['Her karışımın toplam kütlesini ve toplam hacmini ayrı ayrı bulmayı dene.'],
 bilgi=[B('Karışımın özkütlesi','d = toplam kütle ÷ toplam hacim. Örnek: 30 g ve 50 g kütleli sıvılar toplam 100 cm³ oluşturuyorsa d = 80 ÷ 100 = 0,8 g/cm³')],
 puf='Eşit kütlede karışımın özkütlesi, özkütlelerin ortalamasından küçük kalır; toplam kütleyi toplam hacme böl.')

# =================== 07 · üç sıvı tablosu · karışım · orta · tablo ===================
kartla('07','Tablodan en büyük ve en küçük özkütleli sıvıların karışımı','Önce her sıvının özkütlesi bulunur, uç değerli iki sıvı seçilir ve toplam kütle ÷ toplam hacim alınır.','Özkütlelerin ortalamasını ya da toplamını almak.','orta','tablo',4,'karisim','Tablodan seçilen sıvıların karışımı')
T7={'K':(100,80),'L':(150,180),'M':(200,180)}; oz7={k:Fr(m,v) for k,(v,m) in T7.items()}
assert oz7=={'K':Fr(4,5),'L':Fr(6,5),'M':Fr(9,10)}; mx_=max(oz7,key=oz7.get); mn_=min(oz7,key=oz7.get); assert (mx_,mn_)==('L','K')
dk7=Fr(T7['L'][1]+T7['K'][1],T7['L'][0]+T7['K'][0]); assert dk7==Fr(26,25)*1 or dk7==Fr(52,50)
assert dk7==Fr(26,25) and (oz7['L']+oz7['K'])/2==1 and oz7['L']+oz7['K']==2
assert (oz7['K']*T7['L'][0]+oz7['L']*T7['K'][0])/(T7['K'][0]+T7['L'][0])==Fr(24,25)
tb=tablo_svg(['Sıvı','Hacim (cm³)','Kütle (g)'],[[k,str(v),str(m)] for k,(v,m) in T7.items()])
q('0007',tipId='fz-md2-karisim',tip='Tablodan seçilen sıvıların karışımı',z='orta',alt='Karışımların Özkütlesi',kaz='Tablodaki verilerden özkütleleri bulup seçilen iki sıvının karışımının özkütlesini hesaplar.',kalip='tablo',
 kart='K-FZMD2-07 (tablodan karışım) · üç sıvı',sekil=tb,
 metin='Bir kimya laboratuvarında birbiri içinde tamamen çözünen K, L ve M sıvılarından birer örnek alınıyor; örneklerin hacimleri dereceli silindirle, kütleleri hassas terazide ölçülerek aşağıdaki tabloda gösteriliyor. Bir öğrenci, özkütlesi en büyük olan sıvı ile özkütlesi en küçük olan sıvının örneklerinin tamamını bir kapta karıştırıyor. Karışma sırasında toplam hacim değişmiyor.\nBuna göre bu karışımın özkütlesi kaç g/cm³’tür?',
 dogru=Fr(26,25),yan=[(Fr(24,25),'Hacimleri ters yerleştirmiş (özkütleleri hacimlerle çaprazlamış) ve 0,96 bulmuş.','dikkat'),(1,'İki özkütlenin aritmetik ortalamasını (1,2 ve 0,8) almış; hacimlerin farklı olduğunu görmemiş.','bilgi'),(Fr(6,5),'En büyük özkütleyi karışımın özkütlesi sanmış.','dikkat'),(2,'İki özkütleyi toplamış (1,2 + 0,8).','bilgi')],
 istenen='Karışımın özkütlesi (g/cm³).',ip=['Karışacak iki sıvıyı seçebilmek için önce sıvıları özkütleleri açısından sıralaman gerekir.'],
 bilgi=[B('Özkütle ve karışım','d = m ÷ V; karışımda d = toplam kütle ÷ toplam hacim. Örnek: 40 g ve 60 g kütleli, 50 cm³ ve 150 cm³ hacimli iki sıvının karışımı 100 ÷ 200 = 0,5 g/cm³’tür')],
 ad=[A('Özkütleleri bul','Her sıvı için kütle hacme bölünür.','K: 80 ÷ 100 = 0,8 · L: 180 ÷ 150 = 1,2 · M: 180 ÷ 200 = 0,9'),A('Uç sıvıları seç','En büyük L, en küçük K’dir.','L ve K karıştırılıyor'),A('Toplamları al','Kütle ve hacimler ayrı ayrı toplanır.','m = 180 + 80 = 260 g ; V = 150 + 100 = 250 cm³'),A('Karışımın özkütlesi','Toplam kütleyi toplam hacme böl.','d = 260 ÷ 250 = 1,04 g/cm³')],
 puf='Tablodaki verilerden önce özkütle bul, sonra toplam kütleyi toplam hacme böl.')

# =================== 08 · dayanıklılık · küpler · orta ===================
kartla('08','Dayanıklılık: kesit alanı / hacim','Dayanıklılık, kesit alanının hacme oranıyla doğru orantılıdır; küp büyüdükçe oran kenarla ters değişir.','Yalnız kesit alanına ya da yalnız hacme bakmak.','orta','şekilli',4,'dayaniklilik','Kesit alanı ve hacim oranı')
aK,aL=2,8; rK=Fr(aK**2,aK**3); rL=Fr(aL**2,aL**3); oran=rL/rK
assert rK==Fr(1,2) and rL==Fr(1,8) and oran==Fr(1,4) and Fr(aL**2,aK**2)==16 and Fr(aL**3,aK**3)==64 and Fr(aL,aK)==4
def kup(x,a,u,ad):
    s=a*u; return f'\\draw[thick,fill=gray!20] ({x},0) rectangle ({x+s:.3f},{s:.3f});\\draw[thick,fill=gray!35] ({x},{s:.3f}) -- ({x+s*.45:.3f},{s*1.35:.3f}) -- ({x+s*1.45:.3f},{s*1.35:.3f}) -- ({x+s:.3f},{s:.3f}) -- cycle;\\draw[thick,fill=gray!10] ({x+s:.3f},0) -- ({x+s*1.45:.3f},{s*.35:.3f}) -- ({x+s*1.45:.3f},{s*1.35:.3f}) -- ({x+s:.3f},{s:.3f}) -- cycle;\\node[below] at ({x+s/2:.3f},-.05) {{{ad}}};'
g=kup(0,aK,.32,'K: kenar 2 cm')+kup(2.1,aL,.32,'L: kenar 8 cm')
q('0008',tipId='fz-md2-dayaniklilik',tip='Kesit alanı ve hacim oranı',z='orta',alt='Dayanıklılık',kaz='Cisimlerin dayanıklılığını kesit alanı/hacim oranıyla karşılaştırır.',kalip='şekilli',
 kart='K-FZMD2-08 (dayanıklılık, küpler) · kenar oranı 4',sekil=tk(g),
 metin='Bir mühendislik atölyesinde aynı maddeden yapılmış, içi dolu iki küp model hazırlanıyor; şekilde K ve L küplerinin kenar uzunlukları verilmiştir. Atölyede, bir cismin dayanıklılığının kesit alanının hacmine oranı ile doğru orantılı olduğu kabul ediliyor. Küplerde kesit alanı olarak bir yüzün alanı alınıyor. Modellerde başka hiçbir malzeme ya da şekil farkı bulunmuyor.\nBuna göre L küpünün dayanıklılığı, K küpünün dayanıklılığının kaç katıdır?',
 dogru=Fr(1,4),yan=[(1,'Aynı maddeden yapıldıkları için dayanıklılıklarını eşit sanmış; boyut farkı oranı değiştirir.','bilgi'),(4,'Oranı ters kurmuş (K’nın L’ye oranı); sorulan L’nin K’ya oranıdır.','islem'),(16,'Yalnız kesit alanlarını (64 ÷ 4) kıyaslamış; hacmi hesaba katmamış.','bilgi'),(64,'Yalnız hacimlerin (512 ÷ 8) oranını almış; dayanıklılık hacimle ters orantılıdır.','bilgi')],
 istenen='L’nin dayanıklılığının K’ninkine oranı.',ip=['Dayanıklılığın hangi iki niceliğin oranına bağlı olduğunu metinden bul ve her küp için yaz.'],
 bilgi=[B('Dayanıklılık','dayanıklılık, kesit alanı ile doğru, hacim ile ters orantılıdır. Küpte kesit a², hacim a³ olduğundan oran 1 ÷ a’dır. Örnek: kenarı 5 cm olan küpte oran 25 ÷ 125 = 1 ÷ 5’tir')],
 ad=[A('K’nın oranı','Kesit alanı bir yüz, hacim kenarın küpüdür.','K: 2² ÷ 2³ = 4 ÷ 8 = 1/2'),A('L’nin oranı','Aynı işlem L için yapılır.','L: 8² ÷ 8³ = 64 ÷ 512 = 1/8'),A('Oranları kıyasla','L’nin dayanıklılığı K’ya bölünür.','(1/8) ÷ (1/2) = 1/4'),A('Yorumla','Küp büyüdükçe oran kenarla ters değişir; kenar 4 kat arttı.','dayanıklılık 4 kat azaldı')],
 puf='Dayanıklılık için kesit ÷ hacim oranına bak; benzer cisimler büyüdükçe bu oran küçülür, yani dayanıklılık azalır.')

# =================== 09 · yüzey gerilimi · orta · öncüllü ===================
kartla('09','Yüzey gerilimi ve deterjan','Sıvı yüzeyi, moleküller arası çekim yüzünden gergin bir zar gibi davranır; deterjan yüzey gerilimini azaltır.','Yüzeyde kalmayı özkütleyle açıklamak.','orta','şekilli',4,'yuzey','Yüzey gerilimi')
def bardak(x,su=1.8):
    return f'\\fill[vurgu!15] ({x},0) -- ({x+.1},0) -- ({x+1.6},0) -- ({x+1.7},{su}) -- ({x-.1},{su}) -- cycle;\\draw[thick] ({x-.15},2.3) -- ({x},0) -- ({x+1.6},0) -- ({x+1.75},2.3);'
def atac(x,y): return f'\\draw[thick,rounded corners=1pt] ({x},{y}) rectangle ({x+.55},{y+.2});'
g=bardak(0)+atac(.52,1.82)+'\\node[below] at (.8,-.1) {Önce};'
g+=bardak(3)+atac(3.52,.02)+'\\fill[gray!60] (3.78,2.75) circle (.09);\\draw[thick] (3.78,2.84) -- (3.78,3.3);\\node[right,font=\\scriptsize] at (3.9,2.95) {deterjan};\\draw[dotted] (3.78,2.65) -- (3.78,1.9);\\node[below] at (3.8,-.1) {Sonra};'
oncq('0009',(False,True,False),0,
 ['Çelik ataç suyun özkütlesinden büyük özkütleli olduğu hâlde batmamıştır; yüzeyde kalmasının nedeni özkütle değil, yüzey gerilimidir.','Deterjan, su molekülleri arasındaki çekimi zayıflatarak yüzey gerilimini azaltır; yüzey ataçı taşıyamayınca ataç batar.','Deterjan su moleküllerinin birbirini çekmesini (kohezyonu) zayıflatır, artırmaz.'],
 ['Ataçların yüzeyde kalmasını hafif olmalarına bağlamış; çelik suyun özkütlesinden büyük özkütleli olduğu için yüzeyde kalması özkütleyle açıklanamaz.','','Deterjanın moleküller arası çekimi artırdığını sanmış; yüzey gerilimini azalttığı için kohezyon zayıflar.'],
 ['','Deterjanın yüzey gerilimini azalttığını bilmemiş.',''],
 kalip='şekilli',kart='K-FZMD2-09 (yüzey gerilimi) · ataç ve deterjan',tipId='fz-md2-yuzey',tip='Yüzey gerilimi',z='orta',alt='Yüzey Gerilimi',kaz='Yüzey gerilimini sıvı molekülleri arasındaki çekimle açıklar ve deterjanın etkisini yorumlar.',sekil=tk(g),
 metin='Bir öğrenci, su dolu bardağın yüzeyine çelik bir ataçı çok yavaşça bırakıyor ve ataç batmadan yüzeyde kalıyor. Ardından suyun yüzeyine bir damla deterjan damlatıyor; kısa süre sonra ataç şekilde görüldüğü gibi dibe batıyor. Bardaktaki suyun miktarı ve sıcaklığı değişmemiştir.\nI. Ataç, suyun özkütlesinden küçük özkütleli olduğu için yüzeyde kalmıştır.\nII. Deterjan damlatıldığında suyun yüzey gerilimi azalmıştır.\nIII. Deterjan damlatıldığında su moleküllerinin birbirini çekmesi (kohezyon) artmıştır.\nBuna göre bu yargılardan hangileri doğrudur?',
 istenen='Doğru olan yargılar.',ip=['Ataç yüzeyde kalırken deterjan damlatılınca batıyor; deterjanın suyun yüzeyindeki çekimleri nasıl değiştirdiğini düşün.'],
 bilgi=[B('Yüzey gerilimi','sıvı yüzeyindeki moleküller, altlarındaki ve yanlarındaki moleküllerce çekildiği için yüzey gergin bir zar gibi davranır. Örnek: su örümceği ve yüzeye bırakılan iğne bu sayede batmaz; sabun ve deterjan yüzey gerilimini azaltır')],
 puf='Yüzeyde kalan yoğun cisim yüzey gerilimini gösterir; deterjan ve ısınma yüzey gerilimini azaltır.')

# =================== 10 · kılcallık · orta · öncüllü ===================
kartla('10','Kılcal borularda yükselme','Çap küçüldükçe sıvı daha çok yükselir; yükselme adezyon üstünlüğünün sonucudur, fitil ve havlu da bu olaya örnektir.','Yükselmeyi atmosfer basıncına bağlamak; cıvanın da yükseleceğini sanmak.','orta','şekilli',4,'kilcal','Kılcallık')
def kilcal(x,cap,hy):
    w=cap/2; return f'\\fill[vurgu!35] ({x-w},0.9) rectangle ({x+w},{.9+hy});\\draw[thick] ({x-w-.05},{.9+hy+.55}) -- ({x-w-.05},.35) ({x+w+.05},{.9+hy+.55}) -- ({x+w+.05},.35);'
# yükselme çapla ters orantılı çizilir (nitel): K en ince, M en kalın
kc=[('K',.12,1.9),('L',.3,.8),('M',.6,.35)]
g='\\fill[vurgu!18] (-.6,0) rectangle (4.2,.9);\\draw[thick] (-.6,2.9) -- (-.6,0) -- (4.2,0) -- (4.2,2.9);\\draw[vurgu!60!black,thick] (-.6,.9) -- (4.2,.9);'
xs=[.5,1.9,3.3]
for (ad,c,hy),x in zip(kc,xs): g+=kilcal(x,c,hy)+f'\\node[above] at ({x},{.9+hy+.55}) {{{ad}}};'
oncq('0010',(True,False,True),2,
 ['Aynı sıvıda çap küçüldükçe sıvı daha fazla yükselir; şekilde en ince boru K’de seviye en yüksektir.','Sıvıyı kılcal boruda yükselten, cam ile su arasındaki adezyonun kohezyondan büyük olmasıdır; atmosfer basıncı borunun içine ve dışına aynı etki eder. Cıva camı ıslatmadığı için borunun içinde dış seviyenin altında kalır.','Fitilin lifleri arasındaki dar boşluklarda sıvı adezyon etkisiyle yükselir; bu da kılcallıktır.'],
 ['','Cıvanın da suyun yaptığı gibi yükseleceğini sanmış; cıvada kohezyon baskın olduğundan borunun içinde dış seviyenin altında kalır.',''],
 ['Çap ile yükselme arasındaki ters ilişkiyi şekilden okuyamamış.','','Kılcallığın günlük hayattaki örneklerini tanıyamamış.'],
 kalip='şekilli',kart='K-FZMD2-10 (kılcallık) · üç borunun karşılaştırılması',tipId='fz-md2-kilcal',tip='Kılcallık',z='orta',alt='Kılcallık',kaz='Kılcal borulardaki yükselmeyi çapla ve günlük örneklerle ilişkilendirir.',sekil=tk(g),
 metin='Aynı cinsten camdan yapılmış, iç çapları farklı K, L ve M kılcal boruları şekildeki gibi geniş bir kaptaki suya dik olarak batırılıyor. Borulardaki su seviyeleri kaptaki serbest su seviyesine göre ölçülüyor ve şekilde gösteriliyor. Deneyin yapıldığı sıcaklık ve kaptaki su aynıdır; borular temizdir. Öğretmen, bu olayın günlük yaşamda görülen benzer örneklerini de öğrencilerden bulmalarını istiyor.\nI. Borunun çapı küçüldükçe borudaki su seviyesi artar.\nII. Boruları suyun yerine cıva dolu kaba batırsaydık cıva seviyesi de kaptaki seviyenin üstüne çıkardı.\nIII. Gaz lambasının fitilinde gaz yağının yukarı çıkması da kılcallıkla açıklanır.\nBuna göre bu yargılardan hangileri doğrudur?',
 istenen='Doğru olan yargılar.',ip=['Seviyelerin boruların çaplarıyla nasıl değiştiğine bak; sonra suyun cama, cıvanın cama nasıl davrandığını hatırla.'],
 bilgi=[B('Kılcallık','adezyonun kohezyondan büyük olduğu sıvılar dar borularda ve gözenekli maddelerde yükselir; boru inceldikçe yükselme artar. Örnek: kâğıt havlunun suyu emmesi, bitki köklerinin suyu çekmesi')],
 puf='İnce boruda sıvı daha çok yükselir; adezyon baskınsa yükselir, kohezyon baskınsa alçalır.')

# =================== 11 · damla biçimi · orta ===================
kartla('11','Damla biçimi ve ıslatma','Damlanın yüzeyde yayılması adezyonun, küreye yakın kalması kohezyonun baskın olduğunu gösterir.','Damla biçimini yüzey pürüzlülüğüne ya da sıcaklığa bağlamak.','orta','şekilli',3,'yapisma','Damla biçimi ve ıslatma')
from math import radians,sin,cos
def cap_hacim(R,th): c=cos(th); return pi*R**3/3*(2+c)*(1-c)**2
def R_bul(th,V0):
    lo,hi=.05,3.0
    for _ in range(80):
        mid=(lo+hi)/2
        if cap_hacim(mid,th)>V0: hi=mid
        else: lo=mid
    return (lo+hi)/2
V0=cap_hacim(.62/sin(radians(140)),radians(140))
def damla(x,tdeg):
    th=radians(tdeg); R=R_bul(th,V0); w=R*sin(th)
    return f'\\draw[thick,fill=vurgu!25] ({x+w:.3f},0) arc[start angle={90-tdeg},end angle={90+tdeg},radius={R:.3f}];\\draw[thick,fill=gray!30] ({x-1.45},-.18) rectangle ({x+1.45},0);\\draw[thick] ({x-1.45},0) -- ({x+1.45},0);'
th_list=[('K',25),('L',140),('M',160)]
g=''
for (ad,t),x in zip(th_list,[1.5,4.7,7.9]): g+=damla(x,t)+f'\\node[below] at ({x},-.2) {{{ad}}};'
S11=['K yüzeyinde adezyon kohezyondan büyüktür; M yüzeyinde kohezyon adezyondan büyüktür.','K yüzeyinde kohezyon adezyondan büyüktür; M yüzeyinde adezyon kohezyondan büyüktür.','L yüzeyinde adezyon ile kohezyon eşittir; K ve M yüzeylerinde bu eşitlik bozulmuştur.','Üç yüzeyde de adezyon kohezyondan büyüktür; damla biçimleri yalnız adezyonun şiddet farkından kaynaklanır.','Üç yüzeyde de kohezyon adezyondan büyüktür; damla biçimleri yalnız kohezyonun şiddet farkından kaynaklanır.']
q('0011',tipId='fz-md2-yapisma',tip='Damla biçimi ve ıslatma',z='orta',alt='Yapışma ve Birbirini Tutma',kaz='Su damlasının farklı yüzeylerdeki biçimini adezyon ve kohezyon ile açıklar.',kalip='şekilli',
 kart='K-FZMD2-11 (ıslatma, damla biçimi) · üç yüzey',sekil=tk(g),
 metin='Bir öğrenci, aynı sıcaklıktaki suyla doldurduğu damlalıkla, farklı maddelerden yapılmış, temiz ve yatay K, L ve M yüzeylerine eşit hacimde birer su damlası bırakıyor. Damlaların bir süre sonraki yandan görünümü şekilde gösterilmiştir. Su moleküllerinin birbirini çekmesi ile su moleküllerinin yüzey moleküllerini çekmesi arasındaki ilişki, damlanın yüzeyde yayılıp yayılmayacağını belirler. Sıcaklık, damla hacmi ve ortam aynıdır.\nBuna göre aşağıdakilerden hangisi doğrudur?',
 dogru=S11[0],sira=[S11[3],S11[1],S11[2],S11[4],S11[0]],yan=[(S11[1],'Adezyon ile kohezyonun etkisini ters yorumlamış; damla yayılan yüzeyde su–yüzey çekimi baskındır.','bilgi'),(S11[2],'L’deki damlanın K ve M arasında kaldığına bakıp adezyon ile kohezyonu eşit saymış; L’de damla küreye yakın olduğundan kohezyon baskındır.','dikkat'),(S11[3],'Her yüzeyde adezyonun baskın olduğunu sanmış; M’deki küresel damla kohezyonun baskın olduğunu gösterir.','bilgi'),(S11[4],'Her yüzeyde kohezyonun baskın olduğunu sanmış; K’deki yayılmış damla adezyonun baskın olduğunu gösterir.','dikkat')],
 istenen='Doğru olan ifade.',ip=['Damlaların yayılma ya da toparlak kalma biçimini iki çekim kuvvetinin göreli büyüklüğüyle ilişkilendir.'],
 bilgi=[B('Adezyon ve kohezyon','adezyon farklı cins moleküller arasındaki, kohezyon aynı cins moleküller arasındaki çekimdir. Adezyon baskınsa sıvı yüzeyi ıslatır ve yayılır; kohezyon baskınsa damla küreye yakın kalır. Örnek: temiz cam üzerindeki su yayılır, yaprak üzerindeki su boncuk gibi durur')],
 ad=[A('Damlaları incele','K’de damla yayılmış, M’de küreye yakın, L’de ikisi arasında.','K: yayılmış · M: küresel'),A('Çekimleri yorumla','Yayılma adezyonun, küreleşme kohezyonun baskın olduğunu gösterir.','K: adezyon > kohezyon · M: kohezyon > adezyon'),A('Seçenekleri ele','L’de damla yarım küreden belirgin biçimde fazla; kohezyon baskındır, eşitlik yok. Üç yüzeyde aynı sonuç da çıkmaz.','L: kohezyon > adezyon')],
 puf='Damla yayılıyorsa adezyon, küre gibi duruyorsa kohezyon baskındır.')

# =================== 12 · plazma · orta · öncüllü ===================
kartla('12','Plazma hâli','Isıtılan madde katı, sıvı, gaz ve plazma hâllerine geçer; plazma iyon ve serbest elektron içerir, elektriği iletir, şekli ve hacmi yoktur.','Plazmayı yalnız yapay ortamda var sanmak; plazmanın belirli şekli olduğunu düşünmek.','kolay','şekilli',4,'hal','Plazma ve maddenin hâlleri')
g=''
for i,(ad,x) in enumerate(zip(['Katı','Sıvı','Gaz','Plazma'],[0,2.1,4.2,6.3])):
    g+=f'\\node[draw,thick,rounded corners=2pt,minimum width=1.3cm,minimum height=.7cm] (n{i}) at ({x+.65},0) {{{ad}}};'
for i in range(3): g+=f'\\draw[-{{Stealth}},thick] (n{i}.east) -- node[above,font=\\scriptsize] {{({i+1})}} (n{i+1}.west);'
oncq('0012',(True,True,False),2,
 ['Gaz hâlinden plazma hâline geçişte atomlardan elektronlar kopar; serbest elektron ve iyonlar oluşur.','Plazmada serbest yüklü taneciklerin bulunması nedeniyle madde elektrik akımını iletir.','Plazma gaz gibi bulunduğu kabın hacmini doldurur; belirli şekli ve hacmi yoktur.'],
 ['','','Plazmanın katı gibi belirli şekli ve hacmi olduğunu düşünmüş.'],
 ['İyonlaşmanın yeni bir hâl oluşturduğunu bilmemiş.','Plazmadaki serbest yüklü taneciklerin elektriği iletmesini göz ardı etmiş.',''],
 kalip='şekilli',kart='K-FZMD2-12 (plazma) · hâl şeması, öncüllü',tipId='fz-md2-hal',tip='Plazma ve maddenin hâlleri',z='kolay',alt='Plazma ve Maddenin Hâlleri',kaz='Plazma hâlini ve maddenin hâlleri arasındaki geçişleri açıklar.',sekil=tk(g),
 metin='Bir fizik öğretmeni, yıldızları, şimşeği ve neon tabelaların içindeki parlayan gazı örnek vererek maddenin dördüncü hâlinden söz ediyor. Şemada, sürekli ısıtılan bir maddenin sıcaklığı arttıkça geçtiği hâller oklarla gösterilmiştir ve okların üzerinde geçişler numaralandırılmıştır. Isıtma sırasında maddenin kimyasal yapısı değişmemekte, yalnız sıcaklığı artmaktadır.\nI. (3) numaralı geçişte atomlardan elektronlar kopar ve iyonlar oluşur.\nII. Son hâldeki madde elektrik akımını iletir.\nIII. Son hâldeki maddenin belirli bir şekli ve hacmi vardır.\nBuna göre bu yargılardan hangileri doğrudur?',
 istenen='Doğru olan yargılar.',ip=['Son hâlde maddeyi oluşturan taneciklerin yüklü olup olmadığını ve bu hâlin bulunduğu kabı doldurup doldurmadığını düşün.'],
 bilgi=[B('Plazma','gazın daha da ısıtılmasıyla atomlardan elektronlar kopar; serbest elektron ve iyonlardan oluşan bu hâle plazma denir. Elektriği iletir, belirli şekli ve hacmi yoktur. Örnek: yıldızlar, şimşek, floresan lamba')],
 puf='Plazma, iyon ve serbest elektronlu bir gazdır: elektriği iletir, kabını doldurur.')

# =================== 13 · tanecik modeli · orta ===================
kartla('13','Tanecik modelinden hâl özellikleri','Katıda tanecikler düzenli ve sıkı, sıvıda sıkı fakat düzensiz, gazda birbirinden uzaktır; şekil, hacim ve sıkıştırılabilirlik buna bağlıdır.','Sıvıların sıkıştırılabildiğini sanmak.','kolay','şekilli',3,'hal','Taneciklerin dizilimi ve hâl özellikleri')
import random
rnd=random.Random(7)
def kapp(x,tur):
    s=f'\\draw[thick] ({x},1.9) -- ({x},0) -- ({x+1.6},0) -- ({x+1.6},1.9);'
    if tur=='K':
        for i in range(4):
            for j in range(3): s+=f'\\draw[fill=vurgu!30] ({x+.25+.38*i:.2f},{.18+.3*j:.2f}) circle (.12);'
    elif tur=='L':
        pts=[]
        while len(pts)<12:
            p=(x+.17+rnd.random()*1.26,.17+rnd.random()*.85)
            if all((p[0]-a_)**2+(p[1]-b_)**2>.27**2 for a_,b_ in pts): pts.append(p)
        for a_,b_ in pts: s+=f'\\draw[fill=vurgu!30] ({a_:.2f},{b_:.2f}) circle (.12);'
    else:
        pts=[]
        while len(pts)<12:
            p=(x+.2+rnd.random()*1.2,.2+rnd.random()*1.5)
            if all((p[0]-a)**2+(p[1]-b)**2>.3**2 for a,b in pts): pts.append(p)
        for a,b in pts: s+=f'\\draw[fill=vurgu!30] ({a:.2f},{b:.2f}) circle (.12);'
    return s+f'\\node[below] at ({x+.8},-.05) {{{tur}}};'
g=kapp(0,'K')+kapp(2.2,'L')+kapp(4.4,'M')
S13=['K’nin şekli ve hacmi sabittir; L’nin hacmi sabit, şekli kabına göre değişir; M, bulunduğu kabın tamamını doldurur.','K’nin hacmi sabit, şekli kabına göre değişir; L’nin şekli ve hacmi sabittir; M’nin hacmi sabittir.','K ve L kolayca sıkıştırılabilir; M’nin tanecikleri sıkı bağlı olduğundan sıkıştırılamaz.','L’nin tanecikleri K’ninkine göre daha az hareketlidir; M’nin tanecikleri yerlerinde titreşir.','K, L ve M’deki tanecikler arasındaki çekim kuvvetleri aynıdır; yalnız dizilimleri farklıdır.']
q('0013',tipId='fz-md2-hal',tip='Taneciklerin dizilimi ve hâl özellikleri',z='kolay',alt='Plazma ve Maddenin Hâlleri',kaz='Tanecik dizilimine bakarak katı, sıvı ve gazın şekil, hacim ve sıkıştırılabilirlik özelliklerini ayırt eder.',kalip='şekilli',
 kart='K-FZMD2-13 (tanecik modeli) · üç kap',sekil=tk(g),
 metin='Aynı saf maddenin farklı sıcaklıklardaki üç hâlini inceleyen bir öğrenci, her hâlden bir miktarı birbirinin aynısı olan K, L ve M kaplarına koyuyor ve taneciklerin dizilimini şekildeki gibi modelliyor. Kaplar kapalı ve aynı büyüklüktedir, tanecikler özdeştir. Öğrenci hâllerin şekil, hacim ve sıkıştırılabilme özelliklerini bu modelden yorumlayacaktır.\nBuna göre aşağıdakilerden hangisi doğrudur?',
 dogru=S13[0],sira=[S13[0],S13[1],S13[2],S13[3],S13[4]],yan=[(S13[1],'Katı ile sıvının özelliklerini karıştırmış; şekli sabit olan K’dir.','bilgi'),(S13[2],'Sıvıyı sıkıştırılabilir, gazı sıkıştırılamaz sanmış; durum tersidir.','bilgi'),(S13[3],'Tanecik hareketini yanlış hâllere yazmış; yerinde titreşen K’dir, M değil.','bilgi'),(S13[4],'Çekim kuvvetlerinin hâller arasında aynı olduğunu sanmış; tanecikler arası uzaklık arttıkça çekim zayıflar.','bilgi')],
 istenen='Doğru olan ifade.',ip=['Taneciklerin sıklığına ve düzenine göre hangi kabın hâlinin şekil ve hacmini kendisinin, hangisinin kabın belirlediğini düşün.'],
 bilgi=[B('Maddenin hâlleri','katıda tanecikler düzenli ve sıkıdır: şekli ve hacmi sabit. Sıvıda tanecikler sıkı fakat düzensizdir: hacmi sabit, şekli kabına bağlı. Gazda tanecikler uzaktır: bulunduğu kabı doldurur, kolay sıkıştırılır. Örnek: buz, su ve su buharı')],
 ad=[A('Dizilimi oku','K’de düzenli ve sıkı, L’de sıkı ama düzensiz, M’de seyrek tanecikler var.','K: katı · L: sıvı · M: gaz'),A('Özellikleri eşle','Katının şekli ve hacmi, sıvının yalnız hacmi sabittir; gaz kabını doldurur.','K: sabit şekil + hacim · L: sabit hacim · M: kap hacmi'),A('Seçenekleri tara','Yalnız A bu eşlemeyle uyumludur.','A')],
 puf='Tanecik dizilimini oku: düzenli ve sıkıysa katı, sıkı ve düzensizse sıvı, seyrekse gaz.')

# =================== 14 · kap, sıvı, terazi · orta ===================
kartla('14','Kütle farkından özkütle','Kabın kütlesi bilinmediğinde iki doluluk durumunun kütle ve hacim farkı, sıvının özkütlesini verir.','Kabın kütlesini sıvıya katarak toplam kütleyi hacme bölmek.','orta','şekilli',4,'silindir','Kütle ve hacim farkıyla özkütle')
(h1,k1),(h2,k2)=(50,140),(100,200); dsv=Fr(k2-k1,h2-h1); kap=k1-dsv*h1
assert dsv==Fr(6,5) and kap==80 and Fr(k2,h2)==2 and Fr(k1,h1)==Fr(14,5) and Fr(k2-k1,h2)==Fr(3,5) and Fr(k1+k2,h2)==Fr(17,5)
def terazi(x,lv,kt):
    h=3.2; u=h/120
    s=f'\\fill[vurgu!18] ({x},0) rectangle ({x+1.2},{lv*u:.3f});\\draw[thick] ({x},{h}) -- ({x},0) -- ({x+1.2},0) -- ({x+1.2},{h});\\draw[vurgu!60!black,thick] ({x},{lv*u:.3f}) -- ({x+1.2},{lv*u:.3f});'
    s+=f'\\node[font=\\small,fill=white,inner sep=1.5pt] at ({x+.6},{lv*u/2:.3f}) {{{lv} cm$^3$}};'
    s+=f'\\draw[thick,fill=gray!20] ({x-.35},-.4) rectangle ({x+1.55},-.05);\\node[draw,rounded corners=2pt,fill=white,minimum width=1.4cm,font=\\small] at ({x+.6},-.85) {{${kt}$ g}};'
    return s
g=terazi(0,h1,k1)+terazi(3.0,h2,k2)
q('0014',tipId='fz-md2-silindir',tip='Kütle ve hacim farkıyla özkütle',z='orta',alt='Kütle, Hacim ve Özkütle',kaz='Kütle ve hacim ölçümlerinin farkından kabın kütlesini katmadan sıvının özkütlesini bulur.',kalip='şekilli',
 kart='K-FZMD2-14 (terazi ve beher) · kap kütlesi bilinmiyor',sekil=tk(g),
 metin='Bir öğrenci, kütlesi bilinmeyen bir beheri dijital terazinin üzerine koyup içine önce belli bir miktar homojen sıvı dolduruyor, sonra aynı sıvıdan ekleyerek ikinci ölçümü yapıyor. İki durumda beherdeki sıvının hacmi ve beherle birlikte tartılan toplam kütle şekilde gösterilmiştir. Sıvı hiç dökülmemiş ve buharlaşmamıştır, ölçümler aynı sıcaklıkta yapılmıştır.\nBuna göre sıvının özkütlesi kaç g/cm³’tür?',
 dogru=Fr(6,5),yan=[(Fr(3,5),'Kütle farkını (60 g) ikinci hacme (100 cm³) bölmüş; hacim farkı 50 cm³’tür.','dikkat'),(2,'İkinci toplam kütleyi (200 g) sıvı hacmine bölmüş; kabın kütlesi de bu kütlenin içindedir.','dikkat'),(Fr(14,5),'İlk toplam kütleyi (140 g) ilk hacme bölmüş; kabın kütlesini sıvıdan ayırmamış.','dikkat'),(Fr(17,5),'İki toplam kütleyi toplayıp (340 g) son hacme bölmüş.','islem')],
 istenen='Sıvının özkütlesi (g/cm³).',ip=['Beherin kütlesini bilmesen de iki ölçümde ortak olan bir şey var; bunu ortadan kaldırmanın yolunu düşün.'],
 bilgi=[B('Kütle farkı','kabın kütlesi iki ölçümde de aynı kaldığı için toplam kütledeki artış yalnız eklenen sıvının kütlesidir. Örnek: toplam kütle 130 g’dan 190 g’a çıkarsa eklenen sıvı 60 g’dır'),B('Özkütle','d = m ÷ V. Örnek: 90 g kütleli, 60 cm³ hacimli sıvının özkütlesi 1,5 g/cm³’tür')],
 ad=[A('Kütle artışını bul','Beherin kütlesi sabit; artış eklenen sıvıdır.','Δm = 200 − 140 = 60 g'),A('Hacim artışını bul','Eklenen sıvının hacmi seviye farkıdır.','ΔV = 100 − 50 = 50 cm³'),A('Özkütleyi hesapla','Eklenen sıvının kütlesi hacmine bölünür.','d = 60 ÷ 50 = 1,2 g/cm³'),A('Kontrol et','Boş beherin kütlesi de tutarlı çıkar.','50 × 1,2 = 60 g → beher 140 − 60 = 80 g')],
 puf='Kabın kütlesi bilinmiyorsa iki ölçümün farkını al: kütle farkı ÷ hacim farkı özkütleyi verir.')

# =================== 15 · alaşım · zor · hikâyeli ===================
kartla('15','Alaşımda bileşen kütlesi','İki bileşenin hacimleri toplamı alaşımın hacmine eşit alınır; kütle–hacim denklem sistemiyle bileşenlerin kütlesi bulunur.','Bileşenleri eşit hacimde ya da eşit kütlede varsaymak.','zor','hikâyeli',5,'karisim','Alaşımda bileşen kütlesi')
dCu,dZn=9,7; mT,VT=660,80; mCu=Fr(dCu*dZn*VT-dCu*mT,dZn-dCu)  # x/9+(660-x)/7=80
mCu=Fr(dCu*(dZn*VT-mT),dZn-dCu)*-1 if False else None
# x/9 + (mT-x)/7 = VT → 7x + 9mT − 9x = 63 VT → x = (9mT − 63VT)/2
mCu=Fr(9*mT-63*VT,2); mZn=mT-mCu
assert mCu==450 and mZn==210 and Fr(mCu,dCu)+Fr(mZn,dZn)==VT==80 and Fr(mCu,dCu)==50 and Fr(mZn,dZn)==30
assert (mT//2)==330 and Fr(VT,2)*dCu==360 and dZn*50==350 and dCu*30==270
q('0015',tipId='fz-md2-karisim',tip='Alaşımda bileşen kütlesi',z='zor',alt='Karışımların Özkütlesi',kaz='İki bileşenli alaşımda toplam kütle ve hacimden bileşenlerin kütlesini hesaplar.',kalip='hikâyeli',
 kart='K-FZMD2-15 (alaşım) · iki bilinmeyenli kütle–hacim',
 metin='Bir döküm atölyesinde bakır (özkütlesi 9 g/cm³) ve çinko (özkütlesi 7 g/cm³) eritilip karıştırılarak homojen bir alaşım elde ediliyor. Katılaşan alaşım bloğunun kütlesi 660 g, hacmi 80 cm³ ölçülüyor. Bileşenler karışırken toplam hacmin değişmediği, alaşımda başka madde ve boşluk bulunmadığı biliniyor.\nBuna göre bu alaşımdaki bakırın kütlesi kaç g’dır?',
 dogru=450,yan=[(270,'Çinkonun hacmini (30 cm³) bakırın özkütlesiyle çarpmış.','islem'),(330,'Alaşımı yarı yarıya kütlece paylaştırmış.','bilgi'),(350,'Bakırın hacmini (50 cm³) çinkonun özkütlesiyle çarpmış.','islem'),(360,'Bakır ve çinkonun hacimlerini eşit (40 cm³) varsaymış.','bilgi')],
 istenen='Alaşımdaki bakırın kütlesi (g).',ip=['Bileşenlerin hacimlerini kütle ve özkütle cinsinden yazıp toplamı alaşımın hacmiyle karşılaştır.'],
 bilgi=[B('Hacim ve kütle ilişkisi','bir bileşenin hacmi V = m ÷ d’dir; homojen karışımda bileşenlerin hacimleri toplamı karışımın hacmine eşittir. Örnek: 24 g madde d = 8 g/cm³ ise 3 cm³ yer tutar')],
 ad=[A('Bilinmeyeni tanımla','Bakırın kütlesine x dersek çinkonunki kalan kütledir.','m(Cu) = x ; m(Zn) = 660 − x'),A('Hacimleri yaz','Her bileşenin hacmi kütlesinin özkütlesine oranıdır.','V(Cu) = x ÷ 9 ; V(Zn) = (660 − x) ÷ 7'),A('Toplam hacimden denklem kur','Hacimlerin toplamı 80 cm³’tür.','x ÷ 9 + (660 − x) ÷ 7 = 80'),A('Çöz','Paydaları eşitle (63 ile çarp).','7x + 5940 − 9x = 5040 → x = 450'),A('Kontrol et','Hacimler toplamı alaşımın hacmini vermelidir.','450 ÷ 9 + 210 ÷ 7 = 50 + 30 = 80 cm³')],
 puf='Alaşımda iki bilinmeyenli problemde bileşenlerin hacimlerini m ÷ d ile yaz ve toplamı alaşımın hacmine eşitle.')

# =================== 16 · m–V grafiği ile karışım · zor ===================
kartla('16','Grafikten karışımdaki hacim','Grafikten özkütleler okunur; karışımın kütle ve hacmiyle iki denklem kurulup bileşen hacmi çözülür.','Eşit hacim varsaymak; kütle ile hacmi karıştırmak.','zor','grafik',5,'grafik','Grafik ve karışımda bileşen hacmi')
gX,gY=(25,20),(10,12); dgX,dgY=Fr(gX[1],gX[0]),Fr(gY[1],gY[0]); mK,VK=66,60
Vx=Fr(dgY*VK-mK,dgY-dgX); Vy=VK-Vx
assert (dgX,dgY)==(Fr(4,5),Fr(6,5)) and Vx==15 and Vy==45 and dgX*Vx+dgY*Vy==mK and dgX*Vx==12 and dgY*Vy==54 and VK//2==30
g=mgraf([('X',gX),('Y',gY)],[10,25],[12,20,40])
q('0016',tipId='fz-md2-grafik',tip='Grafik ve karışımda bileşen hacmi',z='zor',alt='Karışımların Özkütlesi',kaz='Kütle–hacim grafiğinden özkütleleri okuyup karışımın bileşen hacmini hesaplar.',kalip='grafik',
 kart='K-FZMD2-16 (m–V grafiği + karışım) · bileşen hacmi',sekil=tk(g),
 metin='X ve Y sıvılarının kütle–hacim grafiği şekildeki gibidir. İki sıvı birbiri içinde tamamen çözünmekte ve karışırken toplam hacim korunmaktadır. Laboratuvarda bu sıvılardan homojen bir karışım hazırlanıyor ve karışımın kütlesi 66 g, hacmi 60 cm³ olarak ölçülüyor. Karışımda X ve Y dışında başka madde yoktur ve sıcaklık sabittir.\nBuna göre karışımı hazırlamak için kaç cm³ X sıvısı kullanılmıştır?',
 dogru=15,yan=[(12,'X’in kütlesini (12 g) hacim sanmış; sorulan hacimdir.','dikkat'),(30,'Karışımı eşit hacimli (30 + 30 cm³) varsaymış.','bilgi'),(45,'Y’nin hacmini sorulan X’in hacmi sanmış.','dikkat'),(54,'Y’nin kütlesini (54 g) X’in hacmi sanmış.','dikkat')],
 istenen='Kullanılan X sıvısının hacmi (cm³).',ip=['Önce grafikten iki sıvının özkütlesini bul; sonra toplam hacim ve toplam kütle için iki eşitlik yaz.'],
 bilgi=[B('Kütle–hacim grafiği','orijinden geçen doğruda d = m ÷ V okunan bir noktadan bulunur. Örnek: (20 cm³, 30 g) noktası 1,5 g/cm³ özkütle verir'),B('Karışımda hacim ve kütle','toplam hacim = V₁ + V₂, toplam kütle = d₁V₁ + d₂V₂. Örnek: d₁ = 2, d₂ = 3 olan sıvılardan 10 + 20 cm³ alınırsa kütle 20 + 60 = 80 g olur')],
 ad=[A('Özkütleleri oku','Grafikteki birer noktadan d = m ÷ V.','dX = 20 ÷ 25 = 0,8 · dY = 12 ÷ 10 = 1,2 g/cm³'),A('Denklemleri kur','X’in hacmine x diyelim; Y’nin hacmi 60 − x olur.','0,8x + 1,2(60 − x) = 66'),A('Çöz','Parantezi aç.','72 − 0,4x = 66 → x = 15 cm³'),A('Kontrol et','Y’nin hacmi 45 cm³; toplam kütle 66 g olmalı.','0,8 × 15 + 1,2 × 45 = 12 + 54 = 66 g')],
 puf='Grafikten özkütleleri okuyup “toplam hacim” ve “toplam kütle” denklemlerini yaz.',
 kisa='Karışımın özkütlesi 66 ÷ 60 = 1,1 g/cm³; 0,8 ile 1,2’ye uzaklıkları 0,3 ve 0,1 olduğundan X : Y hacimleri 1 : 3 çıkar; 60 cm³’ün dörtte biri 15 cm³’tür.')

# =================== 17 · dayanıklılık · silindirler · zor · öncüllü ===================
kartla('17','Silindirlerde kesit/hacim','Silindirde kesit alanı ÷ hacim = 1 ÷ yükseklik olduğundan dayanıklılık yarıçaptan bağımsız, yükseklikle ters orantılıdır.','Kalın olan daha dayanıklı demek.','orta','şekilli',5,'dayaniklilik','Silindirlerde dayanıklılık karşılaştırma')
cx={'X':(2,4),'Y':(4,4),'Z':(2,8)}  # çap, yükseklik (cm)
def oran(c): d,h=c; r=Fr(d,2); return (r*r)/(r*r*h)
ox,oy,oz=oran(cx['X']),oran(cx['Y']),oran(cx['Z'])
assert ox==oy==Fr(1,4) and oz==Fr(1,8) and oz*2==ox
vX_,vY_=Fr(cx['X'][0],2)**2*cx['X'][1],Fr(cx['Y'][0],2)**2*cx['Y'][1]; assert vY_==4*vX_
def silin(x,d,h,ad,u=.4):
    w=d*u; hh=h*u; return f'\\draw[thick,fill=gray!20] ({x},0) -- ({x},{hh}) arc[start angle=180,end angle=0,x radius={w/2:.3f},y radius=.12] -- ({x+w},0) arc[start angle=0,end angle=-180,x radius={w/2:.3f},y radius=.12];\\draw[thick] ({x},{hh}) arc[start angle=180,end angle=-180,x radius={w/2:.3f},y radius=.12];\\node[below] at ({x+w/2:.3f},-.18) {{{ad}}};\\node[left,font=\\scriptsize] at ({x-.03},{hh/2:.3f}) {{{h} cm}};\\node[above,font=\\scriptsize] at ({x+w/2:.3f},{hh+.12:.3f}) {{çap {d} cm}};'
g=silin(0.5,*cx['X'],'X')+silin(2.2,*cx['Y'],'Y')+silin(5.2,*cx['Z'],'Z')
oncq('0017',(True,True,True),4,
 ['Silindirde kesit ÷ hacim = (πr²) ÷ (πr²h) = 1 ÷ h’tır; X ve Y’nin yükseklikleri aynı (4 cm) olduğundan oranlar eşit, yani 1/4 cm⁻¹’dir.','Z’nin yüksekliği 8 cm olduğundan oranı 1/8 cm⁻¹; X’in oranının yarısıdır.','Çap iki katına çıkınca yarıçap iki, taban alanı dört, hacim de dört kat artar; Y’nin hacmi X’inkinin 4 katıdır.'],
 ['','',''],
 ['Kalın silindirin daha dayanıklı olacağını düşünerek oranların eşit çıktığını fark etmemiş.','Yüksekliğin iki katına çıkmasının oranı yarıya indirdiğini görememiş.','Çapın iki katı olmasının hacmi 2 değil 4 kat artırdığını kavrayamamış.'],
 kart='K-FZMD2-17 (silindirlerde dayanıklılık) · üç silindir, öncüllü',tipId='fz-md2-dayaniklilik',tip='Silindirlerde dayanıklılık karşılaştırma',z='orta',alt='Dayanıklılık',kaz='Silindirlerde kesit alanı ve hacim oranından dayanıklılığı karşılaştırır.',kalip='şekilli',sekil=tk(g),
 metin='Bir yapı laboratuvarında aynı maddeden yapılmış, içi dolu X, Y ve Z dik silindirik model sütunlar hazırlanıyor; sütunların çapları ve yükseklikleri şekilde verilmiştir. Laboratuvarda bir cismin dayanıklılığının, taban (kesit) alanının hacmine oranıyla doğru orantılı olduğu kabul ediliyor. Sütunlar arasında şekilde görülenler dışında bir fark yoktur.\nI. X ve Y’nin dayanıklılıkları eşittir.\nII. Z’nin dayanıklılığı X’inkinin yarısıdır.\nIII. Y’nin hacmi X’inkinin 4 katıdır.\nBuna göre bu yargılardan hangileri doğrudur?',
 istenen='Doğru olan yargılar.',ip=['Her silindir için kesit alanını ve hacmi ayrı ayrı yazıp oranlarını kıyasla.'],
 bilgi=[B('Dayanıklılık','dayanıklılık, kesit alanı ÷ hacim oranıyla doğru orantılıdır. Dik silindirde bu oran 1 ÷ yükseklik olur. Örnek: yüksekliği 5 cm olan silindirde oran 1/5 cm⁻¹’dir')],
 puf='Dik silindirde kesit ÷ hacim = 1 ÷ yükseklik; yarıçap sadeleşir, yükseklik belirleyicidir.')

# =================== 18 · kılcallık, iki etken · zor · öncüllü ===================
kartla('18','Kılcallıkta sıvı cinsi ve çap','Su camı ıslatır (yükselir), cıva ıslatmaz (alçalır); aynı sıvıda çap küçüldükçe sapma artar. İki etken birlikte değerlendirilir.','Çapı büyütünce sapmanın artacağını sanmak.','zor','şekilli',5,'kilcal','Kılcallıkta sıvı cinsi ve çap')
def kilcal2(x,cap,sapma,tur):
    w=cap/2; s=''
    if tur=='su': s+=f'\\fill[vurgu!18] (-.35,0) rectangle (1.65,.9);'
    else: s+=f'\\fill[gray!50] (-.35,0) rectangle (1.65,.9);'
    s+=f'\\draw[thick] (-.35,2.9) -- (-.35,0) -- (1.65,0) -- (1.65,2.9);\\draw[thick] (-.35,.9) -- ({x-w-.05},.9) ({x+w+.05},.9) -- (1.65,.9);'
    top=.9+sapma
    if tur=='su': s+=f'\\fill[vurgu!35] ({x-w},.9) rectangle ({x+w},{top});'
    else: s+=f'\\fill[white] ({x-w},{top}) rectangle ({x+w},.9);\\draw[thick] ({x-w},{top}) -- ({x+w},{top});'
    s+=f'\\draw[thick] ({x-w-.05},2.4) -- ({x-w-.05},{min(top,.9)-.25:.2f}) ({x+w+.05},2.4) -- ({x+w+.05},{min(top,.9)-.25:.2f});'
    return s
def panel(ox,cap,sap,tur,ad):
    return f'\\begin{{scope}}[xshift={ox}cm]'+kilcal2(.65,cap,sap,tur)+f'\\node[below] at (.65,-.05) {{{ad}}};\\end{{scope}}'
g=panel(0,.14,1.4,'su','K')+panel(2.4,.4,.55,'su','L')+panel(4.8,.14,-.6,'cıva','M')
oncq('0018',(True,True,False),1,
 ['K ve L’de su camı ıslatır (adezyon > kohezyon) ve yükselir; M’de cıva camı ıslatmaz (kohezyon > adezyon) ve dış seviyenin altında kalır.','K ve L’de aynı sıvı var; K’de yükselme daha fazla olduğundan K’nin iç çapı L’ninkinden küçüktür.','Cıva için de çap küçüldükçe alçalma artar; boru geniş (iç çapı büyük) olursa alçalma azalır.'],
 ['','','Çapın büyümesiyle cıvanın daha çok alçalacağını sanmış.'],
 ['Su ile cıvanın cama farklı davrandığını bilmemiş.','Aynı sıvıda yükselmenin çapla doğru orantılı olduğunu düşünmüş; oysa ince boruda yükselme daha fazladır.',''],
 tur={},
 kart='K-FZMD2-18 (kılcallık, sıvı cinsi ve çap) · üç boru, öncüllü',tipId='fz-md2-kilcal',tip='Kılcallıkta sıvı cinsi ve çap',z='zor',alt='Kılcallık',kaz='Sıvı cinsi ve boru çapının kılcallıktaki seviye değişimine etkisini birlikte yorumlar.',kalip='şekilli',sekil=tk(g),
 metin='Aynı cinsten camdan yapılmış temiz K, L ve M kılcal boruları, şekilde görüldüğü gibi ayrı kaplardaki sıvılara dik biçimde batırılıyor. K ve L borularının bulunduğu kaplarda su, M borusunun bulunduğu kapta cıva vardır. M borusunun iç çapı K borusunun iç çapı ile aynıdır. Borulardaki sıvı seviyeleri kaplardaki serbest seviyelere göre şekilde gösterilmiştir; sıcaklık ve sıvıların cinsi deney boyunca değişmemiştir.\nI. M borusunda cıva moleküllerinin birbirini çekmesi, cıva ile cam arasındaki çekimden büyüktür.\nII. K borusunun iç çapı L borusunun iç çapından küçüktür.\nIII. M borusu iç çapı daha büyük bir boruyla değiştirilirse cıva seviyesi serbest seviyeye göre daha çok alçalır.\nBuna göre bu yargılardan hangileri doğrudur?',
 istenen='Doğru olan yargılar.',ip=['Önce hangi sıvının camı ıslattığını seviyelere bakarak belirle; sonra aynı sıvıdaki iki boruyu çap açısından karşılaştır.'],
 bilgi=[B('Kılcallık','sıvı camı ıslatıyorsa (adezyon > kohezyon) kılcal boruda yükselir, ıslatmıyorsa (kohezyon > adezyon) dış seviyenin altında kalır. Sapma miktarı çap küçüldükçe artar. Örnek: ince boruda su yüksek, kalın boruda daha az yükselir')],
 puf='Önce sıvının camı ıslatıp ıslatmadığına, sonra boru çapına bak: çap küçüldükçe sapma artar.')

TIPAD={'silindir':'Hacim ölçümü ve özkütle','grafik':'Kütle–hacim grafiği','ortak':'Ortak ve ayırt edici özellikler','yapisma':'Yapışma ve birbirini tutma','karisim':'Karışımların özkütlesi','dayaniklilik':'Dayanıklılık','yuzey':'Yüzey gerilimi','kilcal':'Kılcallık','hal':'Plazma ve maddenin hâlleri'}
for x in P.ANA+H.KARTLAR: x['tip']=TIPAD[x['tipId'][7:]]
bitir(P,'maddeiki',UK)
