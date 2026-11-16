"""TYT Kimya · Asitler, Bazlar ve Tuzlar · ek paket (asitbaziki): 22 soru, kardeş yok, ipucu 1.
Şekil koordinatları, tanecik sayıları, denklem dengeleri ve öncül doğrulukları Python'da hesaplanır; TikZ bu değerlerden üretilir.
Öncüllerin doğru/yanlış değeri tek yerde (d sözlüğü) tanımlanır; anahtar, adım ve çeldirici açıklamaları oradan üretilir."""
import sys,os,math,random,re,itertools
GD=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,GD)
import _hafif_kim2 as H
from _hafif_kim2 import *
from _hafif_kim import onc as _onc_eski, tek
KONU_='Asitler, Bazlar ve Tuzlar'; UK='kim|Asitler, Bazlar ve Tuzlar'
H.KONU=KONU_
P=Parti('asitbaziki',KONU_,UK,ders='TYT Kimya',idon='tytkim')
KY='ÖSYM 2018–2026 TYT Kimya (yalnız mantık) · MEB 10. sınıf Asitler, Bazlar ve Tuzlar'
MAP={}
for _n,_t in [(('01','02','03'),('ozellik','Asit ve bazların genel özellikleri')),(('04','05'),('ph','pH ölçeği ve yorumlanması')),
              (('06','07','18'),('indikator','İndikatörler ve renk değişimleri')),(('08','09','19'),('metal','Asit ve bazların metallerle tepkimesi')),
              (('10','11','12','22'),('notr','Nötralleşme ve tuz oluşumu')),(('13','14','17','20'),('gunluk','Günlük hayatta asitler, bazlar ve tuzlar')),
              (('15','16','21'),('yagmur','Asit yağmurları ve asit–tuz etkileşimi'))]:
    for _x in _n: MAP[_x]=_t
assert len(MAP)==22
def kartla(n,alt,fikir,tuzak,z,kalip,adim):
    a,b=MAP[n]; kart(f'K-KMAB2-{n}',alt,fikir,tuzak,z,kalip,adim,f'km-ab2-{a}',b,KY)
def q(no,ad,**k):
    assert len(k['ip'])==1
    k['tipId']='km-ab2-'+MAP[no[-2:]][0]; k['tip']=MAP[no[-2:]][1]
    ne=k.pop('ne'); k['kart']=f"K-KMAB2-{no[-2:]} ({MAP[no[-2:]][1].lower()}) · {ne}"
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
kartla('01','Asit–baz genel özellikleri','Asit ve baz çözeltileri iyon içerdiğinden akım iletir; asit mavi, baz kırmızı turnusolun rengini değiştirir; fenolftalein yalnız bazda pembe olur.','Fenolftaleinin asitte de renk değiştirdiğini sanmak.','kolay','öncüllü',3)
kartla('02','İletkenlik düzeneği','Ampulün yanması çözeltide serbest iyon bulunduğunu gösterir; katı iyonik bileşik iletmez, çözeltisi iletir; şekerli su iyon içermez.','İletkenliği yalnız asitlere özgü sanmak; ampul yanmayınca “baz” demek.','kolay','öncüllü',3)
kartla('03','Arrhenius tanımı','Arrhenius’a göre suda H⁺ veren asit, OH⁻ veren bazdır; ikisini de vermeyen iyonik bileşik tuzdur.','Cl⁻ içeren her bileşiği asit, Na⁺ içereni baz saymak.','kolay','tablo',2)
kartla('04','pH çizelgesi','pH < 7 asidik, 7 nötr, > 7 bazik; pH küçüldükçe asitlik artar.','Kahve gibi hafif asidik maddeyi bazik saymak; küçük pH’ı bazik sanmak.','kolay','şekilli',2)
kartla('05','Seyreltme ve pH','Asidik çözelti seyrelince pH artarak 7’ye yaklaşır, bazik çözelti seyrelince azalarak 7’ye yaklaşır; 7’yi geçmez.','Seyreltmeyle asidin bazik olabileceğini sanmak.','orta','grafik',3)
kartla('06','Ayıraç tablosu','Turnusol ve fenolftalein renklerinden asit, baz ve nötr ayrılır; nötr ve asitte fenolftalein renksizdir.','Renksiz fenolftaleini nötr ya da asit için ayırt edici saymak.','orta','tablo',3)
kartla('07','Doğal indikatör','Kırmızı lahana suyunun renk–ortam eşleşmesinden çözeltinin asit ya da baz olduğu çıkarılır ve turnusol davranışına aktarılır.','Mor rengi (nötr) de turnusolu değiştirir sanmak.','orta','tablo',3)
kartla('08','Metal–asit deneyi','Aktif metaller asitten H₂ çıkarır; soy metaller (Cu, Ag, Au) seyreltik asitle tepkime vermez; metal kütlesi azalır.','Cu’nun da asitten gaz çıkardığını sanmak; gazın O₂ olduğunu düşünmek.','orta','öncüllü',3)
kartla('09','Metallerin asit ve baz tepkimesi','Tüpteki gaz çıkışı gözlemlerinden metallerin asit ve bazla davranışı (hem ikisi, yalnız asit, hiçbiri) çıkarılır.','Her aktif metalin bazla da tepkimeye girdiğini sanmak.','orta','şekilli',4)
kartla('10','Nötralleşme tanecik modeli','Ardışık nötralleşmede önce artan iyon bulunur, sonra eklenen asit ya da bazla yeniden birleşir; ortam en son artan iyona göre belirlenir.','Tuz oluştuğu için ortamın hep nötr olduğunu sanmak.','zor','şekilli',5)
kartla('11','Nötralleşme sonrası tanecik çizimi','Tepkime sonrası çizimde kalan iyon türü ortamı belirler; başlangıç taneciklerine dönülerek sayılar yorumlanır.','Artan H⁺ varken ortamı bazik saymak.','orta','öncüllü',3)
kartla('12','Nötralleşme denklemi','Fosforik asit gibi çok protonlu asitle Ca(OH)₂ tepkimesinde atom sayıları eşitlenir; H₂O katsayısı toplam H’tan bulunur.','Katsayıları indislerle karıştırmak.','zor','düz',4)
kartla('13','Günlük hayatta asit–baz','Günlük maddelerin asidik ya da bazik olması kullanım amaçlarıyla ilişkilidir; ifadeler bilimsel gerçekle sınanır.','Antasit ilaçlarını asidik sanmak.','orta','düz',3)
kartla('14','Tuzların kullanımı','Günlük hayatta kullanılan tuzların formülleri kullanım alanlarıyla eşleştirilir.','Kabartma tozu ile sofra tuzunu karıştırmak.','kolay','hikâyeli',2)
kartla('15','Asit yağmuru grafiği','SO₂ ve NO₂ gazları yağmur suyunda çözünerek asit oluşturur; göl suyunda pH azalması asitliğin artması demektir.','pH azalmasını bazikliğin artması sanmak.','orta','grafik',3)
kartla('16','Asit yağmuru etkileri','Asit yağmurunun yapılara, canlılara ve çevreye etkileri asidik niteliğiyle ilişkilendirilir.','Toprağın bazikleştiğini sanmak.','orta','düz',3)
kartla('17','Temizlik ürünleri uyarısı','Temizlik ürünleri etiket uyarılarına göre ayrı ayrı kullanılır, birbirine karıştırılmaz; ortam havalandırılır.','“Karıştırınca daha etkili olur” yanılgısı.','kolay','öncüllü',3)
kartla('18','Fenolftalein kullanımı','Fenolftalein renksizse çözelti asit ya da nötrdür; ayırt etmek için mavi turnusol kullanılır.','Kırmızı turnusolun asidi nötrden ayırdığını sanmak.','kolay','hikâyeli',2)
kartla('19','Tepkime denklemi seçimi','Mg + 2HCl → MgCl₂ + H₂; Cu tepkime vermez; formüller yük dengesiyle, denklem atom sayısıyla doğrulanır.','Gazı O₂ yazmak; yük dengesini gözetmemek.','orta','hikâyeli',3)
kartla('20','Tuzların kullanım alanı','Poster bilgilerinden doğru olanlar tuzların formül ve kullanım alanı eşleşmesiyle belirlenir.','NaCl’yi kuru pil tuzu saymak.','orta','öncüllü',3)
kartla('21','Karbonatlı tuz ve asit','Mermer–asit deneyinde çıkan gazın türü giren maddelere göre belirlenir; asit yağmuru mermeri benzer tepkimeyle aşındırır.','Her asit tepkimesinde H₂ çıktığını sanmak.','orta','öncüllü',3)
kartla('22','Tanecik sayımı','Tepkimeden sonra kalan ve seyirci iyonlar sayılır, su iyon sayılmaz; sayıca az olan iyon tükenir.','Suyu iyon saymak ya da seyirci iyonları atlamak.','zor','düz',4)

# ======================= 0001 · genel özellikler · kolay · öncüllü =======================
d={'I':(True,'asitlerin sulu çözeltilerinde serbest iyonlar bulunduğu için elektrik akımını iletirler'),
   'II':(True,'baz çözeltileri kırmızı turnusol kâğıdını maviye çevirir'),
   'III':(False,'asit çözeltileri fenolftaleinin rengini değiştirmez, renksiz bırakır; fenolftalein yalnız bazlarda pembe olur')}
r=onc_t(d,2)
q('0001',ad=[adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),sonuc(d,r)],
 ne='asit ve bazların genel özellikleri',z='kolay',alt='Asit ve Bazların Genel Özellikleri',kaz='Asit ve bazların genel özelliklerini ayırt eder.',kalip='öncüllü',
 metin='Bir öğrenci, evdeki mutfak ve temizlik maddelerini inceleyip limon suyu, sirke gibi asitler ile sabunlu su, kireç çözücü gibi bazlar hakkında defterine notlar alıyor. Öğretmeni, notların birkaçının bilimsel olarak doğru olduğunu söylüyor.\nI. Asitlerin sulu çözeltileri elektrik akımını iletir.\nII. Baz çözeltileri kırmızı turnusol kâğıdını maviye çevirir.\nIII. Asit çözeltileri fenolftalein damlatılınca pembe renk verir.\nBuna göre öğrencinin notlarından hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan notlar.',
 ip=['Her notu, çözeltide iyon bulunup bulunmamasına ve ayıraçların hangi ortamda renk değiştirdiğine bakarak değerlendir.'],
 bilgi=[B('İletkenlik ve iyon','Elektrik akımını, çözeltide serbest hareket eden iyonlar iletir. Örnek: sofra tuzunun sulu çözeltisi iyon içerdiği için iletir, şekerli su iyon içermediği için iletmez'),
        B('Ayıraç (indikatör)','Ortamın asit ya da baz olduğunu renk değiştirerek gösteren maddelerdir. Örnek: kırmızı lahana suyu ortama göre kırmızı, mor ya da yeşil olur')],
 puf='Fenolftalein yalnız bazik ortamda pembe olur; asitte ve nötr ortamda renksizdir.')

# ======================= 0002 · iletkenlik düzeneği · kolay · öncüllü + şekil =======================
def duzenek(x0,etiket,yanik,katı=False):
    s=f'\\draw[thick] ({x0},2.0) -- ({x0},0) -- ({x0+2.4},0) -- ({x0+2.4},2.0);'
    if katı:
        for i in range(7): s+=f'\\draw[thin,fill=gray!25] ({x0+.35+i*.26:.2f},.04) rectangle ({x0+.35+i*.26+.2:.2f},.24);'
    else:
        s+=f'\\fill[vurgu!15] ({x0+.02},0.02) rectangle ({x0+2.38},1.2); \\draw[thin] ({x0+.02},1.2) -- ({x0+2.38},1.2);'
    for ex in (x0+.6,x0+1.8): s+=f'\\draw[very thick] ({ex},3.2) -- ({ex},{.3 if not katı else .26});'
    s+=f'\\draw[thick] ({x0+.6},3.2) -- ({x0+.73},3.2); \\draw[thick] ({x0+1.27},3.2) -- ({x0+1.45},3.2); \\draw[thick] ({x0+1.58},3.2) -- ({x0+1.8},3.2);'
    s+=f'\\draw[thick] ({x0+1.45},3.0) -- ({x0+1.45},3.4); \\draw[very thick] ({x0+1.58},3.1) -- ({x0+1.58},3.3);'
    s+=f'\\draw[thick{",fill=vurgu!40" if yanik else ""}] ({x0+1.0},3.2) circle (.27);\\draw[thick] ({x0+.83},3.03) -- ({x0+1.17},3.37);\\draw[thick] ({x0+.83},3.37) -- ({x0+1.17},3.03);'
    if yanik:
        for a in range(0,360,45): s+=f'\\draw[thick,vurgu] ({x0+1.0+.38*math.cos(math.radians(a+22)):.2f},{3.2+.38*math.sin(math.radians(a+22)):.2f}) -- ({x0+1.0+.58*math.cos(math.radians(a+22)):.2f},{3.2+.58*math.sin(math.radians(a+22)):.2f});'
    s+=f'\\node[below,align=center] at ({x0+1.2},-.08) {{{etiket}}};'
    return s
g=duzenek(0,'\\textbf{K}\\\\katı NaOH',False,True)+duzenek(3.7,'\\textbf{L}\\\\NaOH çözeltisi',True)+duzenek(7.4,'\\textbf{M}\\\\şeker çözeltisi',False)
SK=tk(g)
d={'I':(True,'katı NaOH’ta iyonlar yerlerinde sabittir ve serbestçe hareket edemez; bu yüzden katı hâlde akım iletilmez, suda çözününce iyonlar serbest kalır'),
   'II':(False,'şeker suda iyon vermez, molekül hâlinde çözünür; çözeltisi asit de baz da değildir, bazlar ise sulu çözeltide OH⁻ verip akım iletir'),
   'III':(False,'NaOH suda Na⁺ ve OH⁻ iyonlarına ayrışır; ampulün yanması çözeltide iyon bulunduğunu gösterir, H⁺ iyonu bulunduğunu değil')}
r=onc_t(d,0)
q('0002',ad=[adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),sonuc(d,r)],
 ne='üç kaptaki iletkenlik gözlemi',z='kolay',alt='Asit ve Bazların Genel Özellikleri',kaz='İletkenlik deney sonuçlarından maddelerin suda iyon verip vermediğini yorumlar.',kalip='öncüllü',sekil=SK,
 metin='İletkenlik deney düzeneği (pil, ampul ve iki elektrot) kurulan bir laboratuvarda elektrotlar sırasıyla şekildeki üç kaba (K, L ve M) daldırılıyor. Kapların içindeki maddeler şekilde yazılıdır; çözeltiler saf suyla hazırlanmıştır ve ampullerin yanma durumu şekilde gösterilmiştir.\nI. Katı NaOH’ta iyonlar sabit olduğundan K kabındaki ampul yanmaz.\nII. M kabındaki ampulün yanmaması, şekerin bir baz olduğunu gösterir.\nIII. L kabındaki ampulün yanması, çözeltide H⁺ iyonları bulunduğunu gösterir.\nBuna göre bu yargılardan hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',
 ip=['Ampulün yanması çözeltide serbest iyon bulunduğunu gösterir; hangi iyonların oluştuğunu maddenin formülünden çıkar.'],
 bilgi=[B('Katı ve çözeltide iletkenlik','İyonik bir katıda iyonlar yerinde sabittir; suda çözününce ya da erince hareket serbest olur ve akım iletilir. Örnek: KCl katı hâlde iletmez, sulu çözeltisi iletir')],
 puf='Ampul yanıyorsa çözeltide iyon vardır; yanmıyorsa iyon yoktur ve madde asit ya da baz değildir.')

# ======================= 0003 · Arrhenius tablosu · kolay · tablo =======================
tab=[['X','H⁺ ve Cl⁻'],['Y','Na⁺ ve OH⁻'],['Z','Na⁺ ve Cl⁻'],['T','H⁺ ve SO₄²⁻'],['U','Ca²⁺ ve OH⁻']]
SK=tablo_svg(['Suda çözünen madde','Çözeltide bulunan iyonlar'],tab)
ASIT=[r_[0] for r_ in tab if 'H⁺' in r_[1]]; BAZ=[r_[0] for r_ in tab if 'OH⁻' in r_[1]]; TUZ=[r_[0] for r_ in tab if r_[0] not in ASIT+BAZ]
assert ASIT==['X','T'] and BAZ==['Y','U'] and TUZ==['Z']
S3=lambda a,b,t:f'Asit: {a} · Baz: {b} · Tuz: {t}'
dg=S3('X, T','Y, U','Z')
d3=tek_t((dg,''),[
 (S3('X, Z','Y, U','T'),'Cl⁻ iyonu içeren her maddeyi asit sanmak yanlıştır: Z suda H⁺ vermediği için asit değildir; H⁺ veren T ise asittir'),
 (S3('X, T','Y','Z, U'),'U suda OH⁻ verdiği için baz sayılır; Ca²⁺ içermesi onu tuz yapmaz'),
 (S3('X','Y, U','Z, T'),'T suda H⁺ verdiği için SO₄²⁻ iyonuna rağmen asittir, tuz değildir'),
 (S3('X, T','Y, Z, U','yok'),'Na⁺ içeren her madde baz değildir; Z suda OH⁻ vermediği için baz değil, tuzdur')],3)
q('0003',ad=[A('Asitleri belirle','Arrhenius’a göre suda H⁺ veren madde asittir.','X ve T: H⁺ verir → asit'),A('Bazları belirle','Suda OH⁻ veren madde bazdır.','Y ve U: OH⁻ verir → baz'),A('Kalanı sınıfla','H⁺ ya da OH⁻ vermeyen, metal ve asit kalıntısı iyonlarından oluşan madde tuzdur.','Z: Na⁺ ve Cl⁻ → tuz'),A('Sonucu karşılaştır','Üç sınıflandırmayı birden doğru veren şık seçilir.',S3('X, T','Y, U','Z'))],
 ne='X, T, Y, U ve Z’nin sınıfları',z='kolay',alt='Asit ve Bazların Genel Özellikleri',kaz='Arrhenius tanımına göre madde ve iyonlardan asit, baz ve tuzu ayırt eder.',kalip='tablo',sekil=SK,
 metin='Bir öğrenci, suda çözünen beş maddenin her biri için çözeltide bulunan iyonları belirleyip aşağıdaki tabloya yazıyor. Daha sonra öğretmeninin verdiği Arrhenius asit–baz tanımına göre bu maddeleri asit, baz ve tuz olarak sınıflandırmak istiyor.\nBuna göre öğrencinin sınıflandırması aşağıdakilerden hangisinde doğru verilmiştir?',
 dogru=d3['dogru'],yan=d3['yan'],sira=d3['sira'],istenen='Maddelerin asit, baz ve tuz olarak doğru sınıflandırması.',
 ip=['Her maddenin çözeltisinde H⁺ ya da OH⁻ iyonu bulunup bulunmadığına bak.'],
 bilgi=[B('Arrhenius tanımı','Suda H⁺ iyonu veren maddeler asit, OH⁻ iyonu veren maddeler bazdır. Metal (ya da NH₄⁺) ile asit kalıntısından oluşan, H⁺ ya da OH⁻ vermeyen iyonik bileşikler tuzdur. Örnek: HNO₃ asit, KOH baz, KNO₃ tuzdur')],
 puf='Arrhenius’ta ayırıcı iyonlar H⁺ (asit) ve OH⁻ (baz)’dır; ikisini de vermeyen iyonik madde tuzdur.')

# ======================= 0004 · pH çizelgesi · kolay · şekilli =======================
U_=.72
pHm=[('mide özsuyu',1,1),('sirke',3,2),('kahve',5,1),('saf su',7,2),('sabunlu su',10,1),('çamaşır suyu',12,2)]
g=f'\\draw[thick] (0,0) -- ({14*U_},0);'
for t in range(15): g+=f'\\draw[thick] ({t*U_},-.12) -- ({t*U_},.12) node[below,font=\\small] {{{t}}};'
for ad_,v,lv in pHm:
    y=.9 if lv==1 else 1.75
    g+=f'\\fill[vurgu] ({v*U_},0) circle (.09); \\draw[thin] ({v*U_},.1) -- ({v*U_},{y}); \\node[above,font=\\normalsize,align=center] at ({v*U_},{y-.02}) {{{ad_}}};'
g+=f'\\node[below,font=\\normalsize] at ({7*U_},-.7) {{pH}};'
SK=tk(g)
S=[('Mide özsuyu, sirkeden daha az asidiktir.',False,'pH değeri küçük olan daha asidiktir; mide özsuyunun pH’ı sirkeninkinden küçüktür'),
   ('Sirke ve mide özsuyu asidik, sabunlu su ile çamaşır suyu baziktir.',True,''),
   ('Saf su ile kahve aynı ortam türündedir.',False,'saf su pH 7’de nötrdür, kahve ise pH 7’den küçük olduğu için asidiktir'),
   ('Ölçekteki maddeler arasında en bazik olan sabunlu sudur.',False,'pH değeri en büyük olan çamaşır suyudur; sabunlu suyun pH’ı ondan küçüktür'),
   ('Sabunlu suya asit eklenirse pH değeri artar.',False,'asit eklenince baziklik azalır ve pH küçülür')]
d4=tek_t((S[1][0],''),[(s[0],s[2]) for i,s in enumerate(S) if i!=1],1)
q('0004',ad=[A('Ortam türlerini ayır','pH 7’den küçükse asidik, 7 ise nötr, 7’den büyükse bazik ortam vardır.','sirke: 3 · mide özsuyu: 1 → asidik'),A('Bazik olanları bul','pH’ı 7’den büyük olan maddeler baziktir.','sabunlu su: 10 · çamaşır suyu: 12 → bazik'),A('Karşılaştırma yap','pH küçüldükçe asitlik, büyüdükçe baziklik artar.','en asidik: mide özsuyu · en bazik: çamaşır suyu'),A('Şıkları sına','Ölçekle çelişmeyen tek yargı seçilir.','Sirke ve mide özsuyu asidik; sabunlu su ile çamaşır suyu bazik')],
 ne='pH çizelgesine göre doğru yargı',z='kolay',alt='pH Ölçeği',kaz='Günlük hayattaki maddelerin pH değerlerine göre asit–baz özelliğini yorumlar.',kalip='şekilli',sekil=SK,
 metin='Kimya öğretmeni, günlük hayatta karşılaşılan bazı maddelerin yaklaşık pH değerlerini gösteren bir pH ölçeği hazırlayıp tahtaya asıyor ve öğrencilerden ölçeği yorumlamalarını istiyor. Ölçekteki maddelerin hepsi sulu çözelti ya da sıvı hâldedir ve aynı sıcaklıktadır.\nBuna göre pH ölçeğiyle ilgili aşağıdaki yargılardan hangisi doğrudur?',
 dogru=d4['dogru'],yan=d4['yan'],sira=d4['sira'],istenen='Ölçekle uyumlu doğru yargı.',
 ip=['Her yargıyı, ilgili iki maddenin pH değerlerini 7 ile karşılaştırarak sına.'],
 bilgi=[B('pH ölçeği','pH, çözeltinin asitlik ya da baziklik derecesini 0–14 arasında gösterir: 7’den küçük asidik, 7 nötr, 7’den büyük baziktir. Örnek: pH 2 olan çözelti, pH 6 olandan daha asidiktir')],
 puf='pH 7’nin altında asidik, üstünde bazik; 7’den uzaklaştıkça asitlik ya da baziklik artar.')

# ======================= 0005 · seyreltme grafiği · orta · öncüllü + grafik =======================
sx,sy=.55,.30
def pxa(t): return 7-5*(.55**t)
def pyb(t): return 7+5*(.55**t)
ts=[0,.5,1,1.5,2,3,4,5,6,8]
assert pxa(0)==2 and pyb(0)==12 and all(pxa(t)<7 for t in ts) and all(pyb(t)>7 for t in ts)
assert all(pxa(a)<pxa(b) for a,b in zip(ts,ts[1:])) and all(pyb(a)>pyb(b) for a,b in zip(ts,ts[1:]))
g=eksen(8,14,'Eklenen saf su miktarı','pH',sx,sy,xt=[(0,'0')],yt=[2,7,12])
g+=f'\\draw[dashed] (0,{7*sy}) -- ({8*sx+.1},{7*sy});'
g+='\\draw[very thick,vurgu] plot[smooth] coordinates {'+' '.join(f'({t*sx:.2f},{pxa(t)*sy:.2f})' for t in ts)+'};'
g+='\\draw[very thick] plot[smooth] coordinates {'+' '.join(f'({t*sx:.2f},{pyb(t)*sy:.2f})' for t in ts)+'};'
g+=f'\\node[vurgu,font=\\small\\bfseries,above] at ({7*sx:.2f},{pxa(7)*sy-.55:.2f}) {{X}};\\node[font=\\small\\bfseries,above] at ({7*sx:.2f},{pyb(7)*sy+.05:.2f}) {{Y}};'
SK=tk(g)
d={'I':(True,'asidik bir çözeltiye su eklenince H⁺ derişimi azalır, asitlik azalır ve pH değeri 7’ye doğru artar'),
   'II':(False,'bazik çözelti seyrelince pH değeri 7’ye yaklaşır ama 7’yi geçmez; asidik çözeltiye dönüşmez'),
   'III':(True,'pH değeri 7’den büyük olan çözelti baziktir ve kırmızı turnusol kâğıdını maviye çevirir')}
r=onc_t(d,4)
q('0005',ad=[adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),sonuc(d,r)],
 ne='seyreltme sırasında X ve Y’nin pH değişimi',z='orta',alt='pH Ölçeği',kaz='Asit ve baz çözeltilerinin seyreltilmesiyle pH değişimini yorumlar.',kalip='grafik',sekil=SK,
 metin='Aynı sıcaklıkta hazırlanmış X ve Y çözeltilerine ayrı ayrı sürekli saf su ekleniyor ve karışımların pH değerleri ölçülüyor. Elde edilen değişim grafikte gösterilmiştir.\nI. X çözeltisine su eklendikçe asitliği azalır.\nII. Y çözeltisine yeterince su eklenirse çözelti asidik hâle geçer.\nIII. Y çözeltisi, kırmızı turnusol kâğıdını maviye çevirir.\nBuna göre bu yargılardan hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Grafikle uyumlu doğru yargılar.',
 ip=['Başlangıç pH değerlerine bakarak çözeltilerin türünü belirle; eğrilerin 7 çizgisine göre nasıl davrandığını izle.'],
 bilgi=[B('Seyrelme ve pH','Çözeltiye saf su katılınca iyon derişimi azalır. Asidik çözeltilerin pH’ı artarak, bazik çözeltilerin pH’ı azalarak 7’ye yaklaşır; saf su 7 değerindedir. Örnek: pH 3 olan çözelti seyrelince 4, 5 gibi değerlere gelir ama 7’yi aşmaz')],
 puf='Seyreltme pH’ı 7’ye yaklaştırır ama asidi baza ya da bazı aside dönüştürmez.')

# ======================= 0006 · ayıraç tablosu · orta · tablo =======================
tab=[['K','kırmızı','kırmızı','renksiz'],['L','mavi','mavi','pembe'],['M','mavi','kırmızı','renksiz']]
def tur(m,k,f):
    if m=='kırmızı' and f=='renksiz': return 'asit'
    if k=='mavi' and f=='pembe': return 'baz'
    if m=='mavi' and k=='kırmızı' and f=='renksiz': return 'nötr'
TURLER=[tur(r_[1],r_[2],r_[3]) for r_ in tab]; assert TURLER==['asit','baz','nötr']
SK=tablo_svg(['Çözelti','Mavi turnusol','Kırmızı turnusol','Fenolftalein'],tab)
S6=lambda a,b,c:f'K: {a} · L: {b} · M: {c}'
d6=tek_t((S6('limon suyu','sabunlu su','saf su'),''),[
 (S6('sabunlu su','limon suyu','saf su'),'K çözeltisi mavi turnusolu kırmızıya çevirdiği için asittir; sabunlu su baz olduğundan K olamaz'),
 (S6('limon suyu','saf su','sabunlu su'),'L çözeltisi fenolftaleini pembe yaptığı için bazdır; nötr olan saf su L olamaz'),
 (S6('saf su','sabunlu su','limon suyu'),'K asit olduğu için saf su (nötr) olamaz; nötr çözelti M’dir'),
 (S6('sabunlu su','saf su','limon suyu'),'K çözeltisi asit olduğundan sabunlu su olamaz; M çözeltisi hiçbir kâğıdın rengini değiştirmediğinden limon suyu olamaz')],1)
q('0006',ad=[A('Asidi ve bazı bul','Mavi turnusolu kırmızıya çeviren çözelti asittir; kırmızı turnusolu maviye çeviren ve fenolftaleini pembe yapan çözelti bazdır.','K: asit · L: baz'),A('Nötrü bul','Hiçbir kâğıdın rengini değiştirmeyen ve fenolftaleini renksiz bırakan çözelti nötrdür.','M: nötr'),A('Günlük maddelere eşle','Limon suyu asit, sabunlu su baz, saf su nötrdür.','K → limon suyu · L → sabunlu su · M → saf su'),A('Şıkları karşılaştır','Üç çözeltiyi birden doğru eşleştiren şık seçilir.',S6('limon suyu','sabunlu su','saf su'))],
 ne='K, L ve M çözeltilerinin olabileceği maddeler',z='orta',alt='İndikatörler',kaz='Turnusol ve fenolftalein renk değişimlerinden çözeltilerin türünü belirler.',kalip='tablo',sekil=SK,
 metin='Bir öğrenci, mutfaktan aldığı üç çözeltinin (K, L ve M) her birine ayrı ayrı mavi ve kırmızı turnusol kâğıtları batırıyor, ayrıca her birine birkaç damla fenolftalein damlatıyor. Turnusol kâğıtlarının çözeltiden sonraki renkleri ile fenolftaleinin rengi tabloda gösterilmiştir. Çözeltiler limon suyu, sabunlu su ve saf sudan oluşmaktadır.\nBuna göre K, L ve M çözeltileri sırasıyla aşağıdakilerden hangisi olabilir?',
 dogru=d6['dogru'],yan=d6['yan'],sira=d6['sira'],istenen='K, L ve M çözeltilerinin sırasıyla olabileceği maddeler.',
 ip=['Önce her satırın renklerinden çözeltinin türünü bul, sonra günlük maddelerle eşleştir.'],
 bilgi=[B('Turnusol ve fenolftalein','Turnusol kâğıdı mavi ve kırmızı olmak üzere iki türlüdür; fenolftalein renksiz bir sıvıdır. Bu ayıraçlar ortamın türüne göre farklı renkler verir. Örnek: saf su nötr bir çözeltidir')],
 puf='Renk tablosunda önce fenolftaleini pembe yapan çözeltiyi, sonra turnusolu kırmızıya çeviren çözeltiyi bul; kalanı nötr olarak ayır.')

# ======================= 0007 · kırmızı lahana · orta · tablo =======================
tab=[['X','kırmızı'],['Y','yeşil'],['Z','mor'],['T','kırmızı'],['U','yeşil']]
ASITL=[r_[0] for r_ in tab if r_[1]=='kırmızı']; assert ASITL==['X','T']
SK=tablo_svg(['Çözelti','Kırmızı lahana suyunun verdiği renk'],tab)
d7=tek_t(('X ve T',''),[
 ('Y ve U','bu çözeltiler yeşil renk verdiği için bazdır; baz mavi turnusolu kırmızıya değil, kırmızı turnusolu maviye çevirir'),
 ('X, Z ve T','Z mor renk verdiği için nötrdür; nötr çözelti mavi turnusolun rengini değiştirmez'),
 ('Yalnız Z','nötr çözelti mavi turnusolun rengini değiştirmez'),
 ('Y, Z ve U','bazlar ve nötr çözelti mavi turnusolu kırmızıya çevirmez')],0)
q('0007',ad=[A('Renk–ortam eşleşmesi','Kırmızı lahana suyu asitte kırmızı, nötr ortamda mor, bazda yeşil olur.','kırmızı: asit · mor: nötr · yeşil: baz'),A('Tabloyu yorumla','X ve T kırmızı, Z mor, Y ve U yeşil renk vermiştir.','X, T: asit · Z: nötr · Y, U: baz'),A('Turnusola aktar','Mavi turnusol kâğıdını yalnızca asit çözeltileri kırmızıya çevirir.','X ve T')],
 ne='mavi turnusolu kırmızıya çeviren çözeltiler',z='orta',alt='İndikatörler',kaz='Doğal indikatörlerin renk değişiminden çözeltinin asit ya da baz olduğunu çıkarır.',kalip='tablo',sekil=SK,
 metin='Kırmızı lahana suyu doğal bir indikatördür: asidik çözeltilerde kırmızı, nötr çözeltilerde mor, bazik çözeltilerde yeşil renk verir. Bir öğrenci, evdeki beş farklı sulu çözeltiyi (X, Y, Z, T ve U) eşit miktarda lahana suyu içeren beş ayrı bardağa damlatıyor ve oluşan renkleri tabloya yazıyor.\nBuna göre mavi turnusol kâğıdı bu çözeltilerden hangilerine batırıldığında kırmızıya dönmesi beklenir?',
 dogru=d7['dogru'],yan=d7['yan'],sira=d7['sira'],istenen='Mavi turnusolu kırmızıya çeviren çözeltiler.',
 ip=['Lahana suyunun verdiği renkten çözelti türünü bul; sonra mavi turnusolun hangi türde değiştiğini hatırla.'],
 bilgi=[B('Doğal indikatörler','Bazı bitki özleri ortamın asit ya da baz oluşuna göre renk değiştirir. Çay ve kırmızı lahana suyu bunlara örnektir. Her indikatör kendi renk tablosuna göre okunur')],
 puf='Önce indikatör renginden çözelti türünü bul, sonra ikinci indikatörün davranışını o türe göre yorumla.')

# ======================= 0008 · metal + HCl tüpleri · orta · öncüllü + şekil =======================
MET=[('Mg',True),('Cu',False),('Zn',True),('Ag',False)]
g=''.join(tup(i*1.5,m,gz) for i,(m,gz) in enumerate(MET))
g+=f'\\node[font=\\small,anchor=west] at (-.3,2.95) {{Her tüpte seyreltik HCl çözeltisi vardır}};'
SK=tk(g)
d={'I':(True,'aktif metaller asitle tepkimeye girip hidrojen (H₂) gazı oluşturur; gaz oksijen değildir'),
   'II':(True,'Cu ve Ag soy metallerdir, seyreltik HCl ile tepkimeye girmez ve H₂ oluşturmaz'),
   'III':(False,'Mg asitle tepkimeye girince Mg²⁺ iyonuna dönüşüp çözeltiye geçer; parçanın kütlesi azalır')}
r=onc_t(d,3)
q('0008',ad=[adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),sonuc(d,r)],
 ne='dört tüpteki metal–asit gözlemleri',z='orta',alt='Asit ve Bazların Metallerle Tepkimesi',kaz='Asitlerin metallerle tepkimesini gözlem ve denklemlerle yorumlar.',kalip='öncüllü',sekil=SK,
 metin='Bir öğrenci, eşit hacimde ve aynı derişimde seyreltik HCl çözeltisi içeren dört deney tüpüne eşit büyüklükte Mg, Cu, Zn ve Ag parçaları atıyor ve bir süre sonra gözlemlerini şekildeki gibi çiziyor.\nI. Gaz çıkışı gözlenen tüplerde çıkan gaz hidrojendir.\nII. Cu ve Ag tüplerinde gaz çıkmaması, bu metallerin seyreltik HCl ile tepkime vermemesindendir.\nIII. Mg tüpünde tepkime sonunda Mg parçasının kütlesi artar.\nBuna göre bu yargılardan hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',
 ip=['Hangi tüplerde gaz kabarcığı olduğuna bak; metalin asit içinde zamanla ne olduğunu düşün.'],
 bilgi=[B('Metallerin asitlerle tepkimesi','Bir metal asitle tepkimeye girerse metal atomları iyon hâline geçip çözeltiye karışır ve tepkime sırasında gaz oluşabilir. Örnek: Fe + 2HCl → FeCl₂ + H₂')],
 puf='Gözlemi yorumlarken hangi tüplerde tepkime olduğunu, metalin ve gazın ne olduğunu ayrı ayrı sorgula.')

# ======================= 0009 · amfoter metaller · zor · şekilli =======================
kolon=[('X',True,True),('Y',True,False),('Z',False,False)]  # HCl gazı, NaOH gazı
AMF=lambda h,n: 'amfoter' if h and n else ('aktif, bazla vermez' if h else 'soy')
assert [AMF(h,n) for _,h,n in kolon]==['amfoter','aktif, bazla vermez','soy']
g=''
for j,(nm,h,n) in enumerate(kolon):
    g+=tup(2.2+j*1.5,'',h)
    g+=f'\\begin{{scope}}[yshift=-3.1cm]'+tup(2.2+j*1.5,nm,n)+'\\end{scope}'
g+='\\node[font=\\small,anchor=east,align=right] at (1.55,1.0) {HCl\\\\çözeltisi}; \\node[font=\\small,anchor=east,align=right] at (1.55,-2.1) {NaOH\\\\çözeltisi};'
SK=tk(g)
S9=lambda a,b,c:f'X: {a} · Y: {b} · Z: {c}'
d9=tek_t((S9('Al','Mg','Cu'),''),[
 (S9('Mg','Al','Cu'),'X metali NaOH ile de gaz verdiği için amfoterdir (Al); yalnız asitle gaz veren Mg, Y olmalıdır'),
 (S9('Cu','Al','Mg'),'Z hiçbir çözeltide gaz vermediği için soy metaldir (Cu); Mg asitle gaz verdiğinden Z olamaz'),
 (S9('Zn','Cu','Mg'),'Y asitle gaz verdiği için Cu olamaz; Cu seyreltik asitle tepkime vermez'),
 (S9('Al','Zn','Ag'),'Zn de amfoter olduğu için NaOH’la gaz verirdi; Y yalnız asitle gaz verdiğinden Zn olamaz')],2)
q('0009',ad=[A('X’i değerlendir','Hem asitte hem bazda gaz çıkaran metal amfoterdir.','X: Al ya da Zn'),A('Y’yi değerlendir','Yalnız asitle gaz veren metal aktiftir ama amfoter değildir.','Y: Mg ya da Fe'),A('Z’yi değerlendir','Her iki çözeltide de değişmeyen metal soy metaldir.','Z: Cu, Ag ya da Au'),A('Şıkları sına','Üç koşulu birden sağlayan şık seçilir; amfoter metallerin bazla da H₂ verdiği unutulmaz.',S9('Al','Mg','Cu'))],
 ne='X, Y ve Z metalleri',z='orta',alt='Asit ve Bazların Metallerle Tepkimesi',kaz='Amfoter, aktif ve soy metallerin asit ve bazlarla davranışını ayırt eder.',kalip='şekilli',sekil=SK,
 metin='Bir öğrenci, X, Y ve Z metallerinin her birinden ikişer parçayı alıp birini HCl çözeltisi, diğerini NaOH çözeltisi içeren tüplere atıyor ve bir süre bekliyor. Tüplerdeki gaz kabarcıklarının görünümü şekilde verilmiştir; tüplerdeki çözeltilerin derişimleri aynıdır.\nBuna göre X, Y ve Z metalleri sırasıyla aşağıdakilerden hangisi olabilir?',
 dogru=d9['dogru'],yan=d9['yan'],sira=d9['sira'],istenen='X, Y ve Z metalleri.',
 ip=['Hem asitte hem bazda gaz veren, yalnız asitte gaz veren ve hiçbirinde gaz vermeyen metalleri ayrı gruplara koy.'],
 bilgi=[B('Metallerin asit ve bazlarla tepkimesi','Metaller asit ya da bazlarla tepkimeye girdiğinde gaz kabarcığı çıkışı gözlenebilir. Bazı metaller yalnız bir çözeltiyle, bazıları her ikisiyle, bazıları hiçbiriyle tepkime verir')],
 puf='Her metal için iki tüpün gözlemini birlikte oku; önce tepkime veren çözeltileri belirle.')

# ======================= 0010 · nötralleşme tanecik modeli · zor · şekilli =======================
A_={'H':4,'Cl':4}; B_={'Na':6,'OH':6}
kal_OH=B_['OH']-A_['H']; su=min(A_['H'],B_['OH'])
assert kal_OH==2 and su==4 and B_['Na']+kal_OH*(-1)==B_['Na']-kal_OH and (B_['Na']-A_['Cl']-kal_OH)==0
g=beher(0,4.0,3.4,3.0)+iyonlar(0,4.0,3.0,A_,13)+beher(5.0,4.0,3.4,3.0)+iyonlar(5.0,4.0,3.0,B_,29)
g+='\\node[below,align=center] at (2.0,-.1) {HCl çözeltisi}; \\node[below,align=center] at (7.0,-.1) {NaOH çözeltisi};\\node[font=\\Large] at (4.5,1.5) {+};'
SK=tk(g)
SS=['Bazik · 4','Bazik · 6','Nötr · 6','Asidik · 8','Asidik · 6']
ek=A_['H']; kal2=ek-kal_OH; su_top=su+kal_OH
assert kal2==2 and su_top==6 and su+ek==8
y10=[('Bazik · 4','Yalnız ilk karışımın sonucunu yazmış; eklenen ikinci HCl çözeltisini hesaba katmamıştır.','dikkat'),
     ('Bazik · 6','Su sayısını doğru bulmuş ama ortamı yine bazik sanmış; oysa 4 H⁺ iyonu, kalan 2 OH⁻ iyonunu tüketip H⁺ fazlası bırakır.','bilgi'),
     ('Nötr · 6','Ek H⁺ iyonlarının kalan OH⁻ iyonlarını tam götüreceğini düşünmüş; oysa 2 OH⁻ için 2 H⁺ yeter, 2 H⁺ artar.','islem'),
     ('Asidik · 8','Ortamı doğru bulmuş ama ikinci aşamada 4 H⁺’nın hepsinin su oluşturduğunu sanıp 4 + 4 = 8 yazmış; oysa yalnız 2 OH⁻ kalmıştı.','islem')]
q('0010',ad=[A('İlk karışımı çöz','HCl çözeltisinde 4 H⁺, NaOH çözeltisinde 6 OH⁻ vardır; sayısı az olan H⁺ tükenir.','4 H₂O oluşur · 6 − 4 = 2 OH⁻ kalır'),A('İkinci HCl eklenir','Eklenen çözeltide yine 4 H⁺ vardır ve bunlar kalan OH⁻ ile birleşir.','2 H⁺ + 2 OH⁻ → 2 H₂O'),A('Toplam suyu say','İlk aşamadaki ve ikinci aşamadaki su molekülleri toplanır.','4 + 2 = 6 H₂O'),A('Artanı bul','OH⁻ tükenmiştir, eklenen H⁺’lardan kalır.','4 − 2 = 2 H⁺ artar'),A('Ortamı yorumla','Artan iyon H⁺ olduğundan ortam asidiktir.','Sonuç: asidik ortam, 6 H₂O')],
 ne='iki aşamalı nötralleşmede ortam ve toplam su sayısı',z='zor',alt='Nötralleşme ve Tuz Oluşumu',kaz='Nötralleşmeyi tanecik modeliyle yorumlar; oluşan su ve artan iyondan ortamı belirler.',kalip='şekilli',sekil=SK,
 metin='Bir öğrenci, HCl ve NaOH çözeltilerinin taneciklerini şekildeki gibi modelleyip karıştırmadan önceki durumlarını çiziyor. İki çözelti karıştırılıp tam olarak tepkimeye bırakılıyor. Ardından bu karışıma, şekildeki HCl çözeltisinin aynısından (4 H⁺ ve 4 Cl⁻ içeren) bir kap daha ekleniyor ve yine tam tepkime gerçekleşiyor. H⁺ ve OH⁻ iyonları yalnızca su oluşturmak üzere harcanıyor; su molekülleri şekilde gösterilmemiştir.\nBuna göre son karışımın ortam türü ve toplam oluşan H₂O molekülü sayısı aşağıdakilerden hangisinde doğru verilmiştir?',
 dogru='Asidik · 6',yan=y10,sira=SS,istenen='Son karışımın ortam türü ve toplam H₂O sayısı.',
 ip=['Önce ilk karışımda hangi iyonun tükendiğini bul; ikinci ekleme bu artanı nasıl değiştirir, ona bak.'],
 bilgi=[B('Nötralleşmenin iyon modeli','Asitten gelen H⁺ ile bazdan gelen OH⁻ 1:1 oranında birleşip H₂O verir: H⁺ + OH⁻ → H₂O. Tepkimeye girmeyen metal ve asit kalıntısı iyonları çözeltide kalır')],
 puf='Her aşamada sayıca az olan iyon tükenir; artan iyon bir sonraki aşamanın başlangıcı olur.')

# ======================= 0011 · tepkime sonrası iyonlar · orta · öncüllü + şekil =======================
SON={'K':3,'Cl':5,'H':2}
assert SON['K']+SON['H']==SON['Cl']   # yük dengesi
g=beher(0,4.2,3.4,3.0)+iyonlar(0,4.2,3.0,SON,7)+'\\node[below,align=center] at (2.1,-.1) {Karışım (su molekülleri gösterilmemiştir)};'
SK=tk(g)
d={'I':(True,'karışımda tepkimeye girmeden kalan H⁺ iyonları vardır; ortam asidiktir'),
   'II':(False,'karışımdaki 3 tane K⁺ iyonu, KOH çözeltisinde 3 tane OH⁻ iyonu bulunduğunu gösterir; OH⁻ sayısı K⁺ sayısına eşittir, 5 değildir'),
   'III':(True,'asidik ortamda mavi turnusol kâğıdı kırmızıya döner')}
r=onc_t(d,2)
q('0011',ad=[adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),sonuc(d,r)],
 ne='nötralleşme sonrasındaki iyon dağılımı',z='orta',alt='Nötralleşme ve Tuz Oluşumu',kaz='Nötralleşme sonrası tanecik çiziminden ortamı ve başlangıç taneciklerini yorumlar.',kalip='öncüllü',sekil=SK,
 metin='KOH çözeltisi ile HCl çözeltisi bir kapta karıştırılıp tepkimenin tamamlanması bekleniyor. Tepkime sonunda kapta bulunan iyonların taneciklerle modellenmiş hâli şekilde verilmiştir; oluşan su molekülleri çizilmemiştir.\nI. Karışımın ortamı asidiktir.\nII. Karıştırılan KOH çözeltisinde 5 tane OH⁻ iyonu vardır.\nIII. Karışıma mavi turnusol kâğıdı batırılırsa kâğıt kırmızıya döner.\nBuna göre bu yargılardan hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',
 ip=['Şekildeki iyon türlerine bak: tepkimeye girmeden kalan H⁺ ya da OH⁻ iyonu var mı?'],
 bilgi=[B('Katyon ve anyon sayıları','Bir bazın çözeltisinde OH⁻ sayısı, metal katyonunun yüküyle çarpılan katyon sayısına eşittir. Örnek: Mg(OH)₂ çözeltisinde 1 tane Mg²⁺ ile 2 tane OH⁻ vardır')],
 puf='Nötralleşmeden sonra şekilde H⁺ kalmışsa ortam asidik, OH⁻ kalmışsa baziktir.')

# ======================= 0012 · denkleştirme · zor · düz =======================
def say(f):
    return {e:int(n or 1) for e,n in re.findall(r'([A-Z][a-z]?)(\d*)',f)}
def topla(terim):
    top={}
    for kat,form in terim:
        for e,n in form.items(): top[e]=top.get(e,0)+kat*n
    return top
CaOH2={'Ca':1,'O':2,'H':2}; H3PO4={'H':3,'P':1,'O':4}; CaP={'Ca':3,'P':2,'O':8}; H2O={'H':2,'O':1}
sol=[(a,b,c,e) for a in range(1,7) for b in range(1,7) for c in range(1,4) for e in range(1,13) if topla([(a,CaOH2),(b,H3PO4)])==topla([(c,CaP),(e,H2O)])]
assert sol and sol[0]==(3,2,1,6),sol[:3]
mk(P,'0012',tipId='km-ab2-notr',tip='Nötralleşme ve tuz oluşumu',z='zor',alt='Nötralleşme ve Tuz Oluşumu',kaz='Nötralleşme tepkimelerinin denklemini yazar ve denkleştirir.',kalip='düz',adim=4,
 kart='K-KMAB2-12 (nötralleşme denklemi) · Ca(OH)₂ + H₃PO₄',
 metin='Bir laboratuvarda kalsiyum hidroksit [Ca(OH)₂] çözeltisi ile fosforik asit (H₃PO₄) çözeltisi tam nötralleşecek biçimde karıştırılıyor. Tepkimede kalsiyum fosfat [Ca₃(PO₄)₂] tuzu ve su oluşuyor. Tepkime denklemi en küçük tam sayılarla denkleştirilecektir.\nCa(OH)₂ + H₃PO₄ → Ca₃(PO₄)₂ + H₂O\nBuna göre denkleştirilmiş denklemde H₂O’nun katsayısı kaçtır?',
 dogru=6,yan=[(2,'H₃PO₄’ün katsayısını (2) H₂O’nun katsayısı sanmış.','dikkat'),(3,'Ca(OH)₂’nin katsayısını (3) H₂O’nun katsayısı sanmış.','dikkat'),(5,'Ca(OH)₂ ve H₃PO₄ katsayılarını toplamış (3 + 2).','islem'),(12,'Sol taraftaki toplam H atomu sayısını (12) suyun katsayısı almış; suda iki H olduğunu hesaba katmamış.','islem')],
 ad=[A('Ca ve P sayılarını eşitle','Tuzda 3 Ca ve 2 P vardır; bu yüzden Ca(OH)₂’nin katsayısı 3, H₃PO₄’ün katsayısı 2 olur.','3Ca(OH)₂ + 2H₃PO₄ → Ca₃(PO₄)₂ + ?H₂O'),A('Hidrojenleri say','Sol tarafta 3 × 2 + 2 × 3 H vardır.','6 + 6 = 12 H'),A('Suyun katsayısını bul','Her H₂O’da 2 hidrojen vardır.','12 ÷ 2 = 6 → H₂O katsayısı 6'),A('Oksijenle kontrol et','Soldaki O sayısı sağdakine eşit olmalıdır.','3 × 2 + 2 × 4 = 14 · 8 + 6 = 14')],
 istenen='Denkleştirilmiş denklemde H₂O’nun katsayısı.',
 ip=['Önce tuzdaki Ca ve P sayılarını eşitleyerek asit ve bazın katsayılarını bul.'],
 bilgi=[B('Denkleştirme','Tepkimede atom cinsi ve sayısı girenlerde ve ürünlerde eşit olmalıdır; katsayılar formülün önüne yazılır, indisler değiştirilmez. Örnek: 2H₂ + O₂ → 2H₂O')],
 puf='Önce tuzdaki iyon sayılarına göre asit ve bazın katsayılarını, sonra H ve O’yu eşitleyerek suyun katsayısını bul.')
assert 3*2+2*4==14 and 8+6==14

# ======================= 0013 · günlük hayat · orta · olumsuz kök =======================
d13=tek_t(('Mide ekşimesinde kullanılan antasit ilaçlar asidik özelliktedir ve mide özsuyunu nötrleştirmek için bu özellikten yararlanılır.',''),[
 ('Sabunlu suyun pH değeri 7’den büyüktür.','sabunlar bazik özellik gösterir ve pH değerleri 7’den büyüktür'),
 ('Limon suyu ve sirke asidik maddelerdir ve sulu çözeltileri elektrik akımını iletir.','asitler suda iyon verdiği için sulu çözeltileri akım iletir'),
 ('Mide özsuyunda hidroklorik asit (HCl) bulunur.','mide özsuyundaki HCl, besinlerin sindirimine yardım eden bir asittir'),
 ('Sirkenin pH değeri 7’den küçüktür.','sirke asetik asit içerir ve asidik olduğundan pH değeri 7’den küçüktür')],0,False)
q('0013',ad=[A('Maddelerin türünü hatırla','Limon suyu, sirke ve mide özsuyu asidik; sabun ve antasit bazik özelliktedir.','asidik: limon, sirke, mide özsuyu · bazik: sabun, antasit'),A('İfadeleri sına','Her ifadenin bilimsel gerçekle uyumuna bak.','sabun, limon, sirke, HCl ifadeleri doğru'),A('Antasidi çöz','Mide asidini azaltacak madde asidi nötrleştirir; bunu ancak baz yapar.','antasit: bazik'),A('Yanlış ifadeyi seç','Antasit asidik denilen ifade bilimsel olarak yanlıştır.','yanlış olan: antasit için verilen ifade')],
 ne='bilimsel olarak yanlış olan ifade',z='orta',alt='Günlük Hayatta Asitler ve Bazlar',kaz='Günlük hayattaki asit ve bazların özelliklerini ve kullanımını açıklar.',kalip='hikâyeli',
 metin='Bir ev ekonomisi dersinde mutfak ve banyoda kullanılan maddelerin asit–baz özellikleri tartışılıyor. Öğrenciler; limon suyu, sirke, sabun ve mide ilaçları üzerine kendi araştırmalarında bulduklarını sırayla paylaşıyor ve öğretmen her ifadeyi bilimsel doğruluğuna göre değerlendiriyor.\nBuna göre aşağıdaki ifadelerden hangisi yanlıştır?',
 dogru=d13['dogru'],yan=d13['yan'],sira=d13['sira'],istenen='Yanlış olan ifade.',
 ip=['Her ifadeyi, maddenin türü ile kullanım amacının birbirine uyup uymadığı açısından sına.'],
 bilgi=[B('Günlük hayatta asit ve bazlar','Günlük hayatta kullanılan birçok madde asidik ya da bazik özellik gösterir; asidik maddelerin pH’ı 7’den küçük, bazik maddelerin 7’den büyüktür. Örnek: saf su 7 olduğundan nötrdür')],
 puf='Olumsuz kökte doğru ifadeleri tek tek elemek, bilimsel gerçekle çelişeni bulmanın en güvenli yoludur.')

# ======================= 0014 · tuzların kullanımı · kolay · hikâyeli =======================
S14=lambda a,b,c:f'X: {a} · Y: {b} · Z: {c}'
d14=tek_t((S14('NaCl','NaHCO₃','Na₂CO₃'),''),[
 (S14('NaHCO₃','NaCl','Na₂CO₃'),'yemeklere tat veren ve gıda saklamada kullanılan tuz NaCl’dir; kabartma tozu NaHCO₃ olduğundan X ile Y’nin yeri karışmıştır'),
 (S14('Na₂CO₃','NaHCO₃','NaCl'),'cam ve deterjan yapımında kullanılan Na₂CO₃’tür, yemek tuzu NaCl olduğundan X ile Z’nin yeri karışmıştır'),
 (S14('NaCl','Na₂CO₃','NaHCO₃'),'hamur işlerinde kabartıcı olan NaHCO₃’tür; Na₂CO₃ ile NaHCO₃ formülleri birbirine karıştırılmıştır'),
 (S14('NaHCO₃','Na₂CO₃','NaCl'),'X yemek tuzu, Y kabartma tozu, Z çamaşır sodasıdır; verilen sıralamada üç madde de yanlış yerdedir')],1)
q('0014',ad=[A('X’i tanı','Yemeklerde tat vermek ve et, balık gibi gıdaları saklamak için sofra tuzu kullanılır.','X: NaCl'),A('Y’yi tanı','Hamur işlerini kabartan ve mide ekşimesinde kullanılan tuz sodyum bikarbonattır.','Y: NaHCO₃'),A('Z’yi tanı','Cam ve deterjan yapımında kullanılan, çamaşır sodası olarak bilinen tuz sodyum karbonattır.','Z: Na₂CO₃'),A('Şıkları karşılaştır','Üç eşleştirmeyi birden doğru veren şık seçilir.',S14('NaCl','NaHCO₃','Na₂CO₃'))],
 ne='X, Y ve Z tuzlarının formülleri',z='kolay',alt='Tuzların Kullanım Alanları',kaz='Günlük hayatta kullanılan tuzları ve kullanım alanlarını eşleştirir.',kalip='hikâyeli',
 metin='Bir aşçı, mutfakta kullandığı üç tuzu inceliyor. X tuzunu yemeklere tat vermek ve balık gibi gıdaları saklamak için, Y tuzunu hamur işlerini kabartmak ve mide ekşimesini gidermek için kullanıyor. Z tuzu ise cam ve deterjan yapımında ve su yumuşatmada kullanılan, çamaşır sodası olarak da bilinen bir tuzdur.\nBuna göre X, Y ve Z tuzlarının formülleri aşağıdakilerden hangisinde doğru verilmiştir?',
 dogru=d14['dogru'],yan=d14['yan'],sira=d14['sira'],istenen='X, Y ve Z tuzlarının formülleri.',
 ip=['Her tuzun kullanım alanını bilinen formülle eşleştir.'],
 bilgi=[B('Tuzların kullanım alanları','Tuzlar günlük hayatta, sanayide ve tarımda kullanılır. Örnek: KNO₃ gübre ve barut yapımında, CaSO₄ (alçı) sıva ve alçıpanda kullanılır')],
 puf='Tuzları formülleriyle kullanım alanlarını birlikte öğren: formül benzer olsa da kullanım farklı olabilir.')

# ======================= 0015 · göl pH grafiği · orta · öncüllü + grafik =======================
yil=[2000,2005,2010,2015,2020]; pHg=[7,7,6,5,4]
assert pHg[0]==7 and all(a>=b for a,b in zip(pHg,pHg[1:])) and pHg[1]-pHg[-1]==3
sx,sy=.3,.8
def Y_(p): return (p-3)*sy
g=f'\\draw[thick,{ARR}] (0,0) -- ({20*sx+.5:.2f},0);\\draw[thick,{ARR}] (0,0) -- (0,{Y_(8):.2f});'
for y_ in yil: g+=f'\\draw ({(y_-2000)*sx:.2f},0) -- ({(y_-2000)*sx:.2f},-.08) node[below,font=\\small] {{{y_}}};'
for t in (4,5,6,7): g+=f'\\draw[dotted] (0,{Y_(t):.2f}) -- ({20*sx:.2f},{Y_(t):.2f}); \\draw (0,{Y_(t):.2f}) -- (-.08,{Y_(t):.2f}) node[left,font=\\small] {{{t}}};'
g+='\\draw[very thick,vurgu] '+' -- '.join(f'({(a-2000)*sx:.2f},{Y_(b):.2f})' for a,b in zip(yil,pHg))+';'
g+=''.join(f'\\fill[vurgu] ({(a-2000)*sx:.2f},{Y_(b):.2f}) circle (.07);' for a,b in zip(yil,pHg))
g+=f'\\node[font=\\small,anchor=south] at (0,{Y_(8)+.1:.2f}) {{Göl suyunun pH değeri}};\\node[font=\\small,anchor=north] at ({10*sx:.2f},-.55) {{Yıl}};'
SK=tk(g)
d={'I':(False,'2005 yılından önce göl suyunun pH değeri 7’dir; bu değer nötr ortamı gösterir, asidik özelliği değil'),
   'II':(True,'2005–2020 arasında pH değeri 7’den 4’e düşmüştür; pH azaldıkça asitlik artar'),
   'III':(True,'fabrika gazlarındaki SO₂ ve NO₂ yağmur suyunda çözünerek asitleri oluşturabilir ve bu asit yağmuru gölün asitliğini artırabilir')}
r=onc_t(d,3)
q('0015',ad=[adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),sonuc(d,r)],
 ne='göl suyunun pH değerinin yıllara göre değişimi',z='orta',alt='Asit Yağmurları',kaz='Asit yağmurlarının oluşumunu ve çevreye etkisini grafik verisiyle yorumlar.',kalip='grafik',sekil=SK,
 metin='Bir fabrika, 2005 yılında bir gölün yakınında üretime başlamıştır. Fabrikanın bacasından çıkan gazlar arasında kükürt dioksit (SO₂) ve azot dioksit (NO₂) da bulunmaktadır. Göl suyunun pH değeri beş yılda bir ölçülmüş ve sonuçlar grafikte gösterilmiştir.\nI. 2005 yılından önce göl suyu asidik özellikteydi.\nII. 2005–2020 arasında göl suyunun asitliği artmıştır.\nIII. Gölün pH değerindeki değişimde fabrika gazlarının yağmur suyunda çözünüp asit oluşturması etkili olabilir.\nBuna göre bu yargılardan hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',
 ip=['pH değerinin 7’ye göre durumuna ve zamanla yönüne bak; SO₂ ve NO₂ gazlarının suda çözününce ne oluşturduğunu düşün.'],
 bilgi=[B('Asit yağmurları','Fosil yakıtlardan açığa çıkan SO₂ ve NO₂ gibi gazlar atmosferde yağmur suyunda çözünerek asitler oluşturur ve asit yağmuru olarak yeryüzüne iner. Örnek: baca gazı filtreleri bu gazları azaltarak asit yağmurunu önlemeye yardım eder')],
 puf='pH azalıyorsa ortam daha asidik olur; kükürt ve azot oksitleri asit yağmurunun başlıca kaynağıdır.')

# ======================= 0016 · asit yağmuru etkileri · orta · olumsuz kök =======================
d16=tek_t(('Toprağın pH değerini artırarak toprağın bazikleşmesine neden olur.',''),[
 ('Mermer heykel ve binalarda aşınmaya neden olur.','mermerin ana bileşeni CaCO₃ asitle tepkimeye girerek aşınır'),
 ('Göl ve akarsuların pH değerini düşürerek canlı yaşamını olumsuz etkiler.','asit yağmuru suların asitliğini artırır ve pH değerini düşürür'),
 ('Demir ve çelik gibi metallerin daha hızlı aşınmasına yol açar.','asitler metallerle tepkimeye girerek korozyonu hızlandırır'),
 ('Ormanlardaki bazı ağaçların yapraklarına zarar verir.','asit yağmuru bitkilerin yapraklarına ve köklerine zarar verir')],4,False)
q('0016',ad=[A('Asit yağmurunun niteliği','Asit yağmuru asidik olduğundan yağdığı yerde asitliği artırır.','pH azalır → asitlik artar'),A('Etkileri sırala','Mermeri ve metalleri aşındırır; göl, toprak ve ormana zarar verir.','mermer, metal, göl, orman: etkilenir'),A('Toprağı değerlendir','Asidik yağış toprağın pH’ını düşürür, yükseltmez.','toprak: asitleşir'),A('Sonucu belirle','Toprağın bazikleşmesi asit yağmurunun sonucu olamaz.','Söylenemeyen: toprağın bazikleşmesi')],
 ne='asit yağmurunun sonucu olarak söylenemeyen ifade',z='orta',alt='Asit Yağmurları',kaz='Asit yağmurlarının çevreye ve yapılara etkilerini açıklar.',kalip='düz',
 metin='Sanayi bölgelerinden ve yoğun trafikli şehirlerden atmosfere salınan kükürt dioksit ve azot dioksit gazları, yağmur suyunda çözünerek asitleri oluşturur ve yağışla yeryüzüne iner. Bir çevre kulübü, bu yağışların yapılara ve doğaya etkilerini araştırıp afiş hazırlıyor.\nBuna göre aşağıdakilerden hangisi asit yağmurlarının sonucu olarak söylenemez?',
 dogru=d16['dogru'],yan=d16['yan'],sira=d16['sira'],istenen='Asit yağmurunun sonucu olmayan durum.',
 ip=['Yağışın asidik olduğunu düşünerek toprak ve su ortamında pH’ın hangi yönde değişeceğini bul.'],
 bilgi=[B('Asit yağmurlarının etkileri','Asit yağmuru ormanlara zarar verir, metallerin korozyonunu hızlandırır ve CaCO₃ içeren mermer, kireçtaşı yapıları aşındırır. Örnek: tarihî kireçtaşı heykellerde yüzeyin dökülmesi')],
 puf='Olumsuz kökte her şıkkı, yağışın asidik niteliğiyle çelişip çelişmediğine bakarak sına.')

# ======================= 0017 · temizlik ürünleri · orta · öncüllü =======================
d={'I':(False,'farklı temizlik ürünlerini birbirine karıştırmak temizliği artırmaz; ürünler birbiriyle tepkimeye girip sağlığa zararlı gazlar oluşturabilir'),
   'II':(True,'temizlik ürünleri ambalajlarındaki uyarılara uygun ve birbirine karıştırılmadan ayrı ayrı kullanılmalıdır'),
   'III':(False,'rahatsızlık hissedilirse ortamdan uzaklaşılıp temiz havaya çıkılmalıdır; kokunun geçmesini beklemek tehlikelidir')}
r=onc_t(d,1)
q('0017',ad=[adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),sonuc(d,r)],
 ne='temizlik ürünlerinin güvenli kullanımı',z='kolay',alt='Günlük Hayatta Asitler ve Bazlar',kaz='Asit ve baz içeren temizlik ürünlerinin güvenli kullanımını açıklar.',kalip='öncüllü',
 metin='Bir okulda temizlik görevlileri için kimya öğretmeni bir bilgilendirme yapıyor. Öğretmen, asidik ve bazik özellikli temizlik ürünlerinin güvenli kullanımı hakkında üç öneri yazıyor ve öğrencilerden hangilerinin doğru olduğunu işaretlemelerini istiyor.\nI. Farklı temizlik ürünlerini birbirine karıştırmak temizliği güçlendirir.\nII. Ürünler, ambalajlarındaki uyarılara göre ayrı ayrı kullanılmalıdır.\nIII. Ortamda rahatsız edici bir koku hissedilirse koku geçene kadar orada beklenmelidir.\nBuna göre bu önerilerden hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan öneriler.',
 ip=['Etiketlerdeki uyarıların neden yazıldığını ve rahatsızlık hâlinde en güvenli davranışın ne olduğunu düşün.'],
 bilgi=[B('Temizlik maddelerinin güvenli kullanımı','Temizlik ürünlerinin birçoğu asit ya da baz içerir ve ciltte, gözde, solunumda zarara yol açabilir. Etiketteki uyarılara uyulur, ürünler birbirine karıştırılmaz, ortam havalandırılır. Örnek: eldiven ve koruyucu gözlük kullanmak')],
 puf='Temizlik ürünleri ayrı ayrı, etiket uyarılarına uygun ve havalandırılan ortamda kullanılır; birbirine karıştırılmaz.')

# ======================= 0018 · fenolftalein · kolay · hikâyeli =======================
d18=tek_t(('Mavi turnusol kâğıdı batırılır; kırmızıya dönen asittir.',''),[
 ('Kırmızı turnusol kâğıdı batırılır; değişmeyen çözelti asittir.','kırmızı turnusol yalnız bazda maviye döner; hem asit hem nötr çözeltide kırmızı kalır, ikisini ayıramaz'),
 ('Aynı çözeltilere biraz daha fenolftalein damlatılır.','fenolftalein asit ve nötr çözeltide renksiz kalır; fazla damlatmak ikisini ayırt etmeye yaramaz'),
 ('Çözeltiler karıştırılıp fenolftalein tekrar damlatılır.','karıştırma çözeltilerin türünü belirlemez; üstelik fenolftalein yine renksiz kalabilir'),
 ('Kırmızı turnusol kâğıdı ile fenolftalein birlikte kullanılır.','kırmızı turnusol asitte ve nötrde kırmızı kalır, fenolftalein ikisinde de renksizdir; ikisi de asit ile nötrü ayırmaz')],0)
q('0018',ad=[A('Pembe çözeltiyi yorumla','Fenolftalein yalnız bazik ortamda pembe olur.','pembe → baz'),A('Renksizleri değerlendir','Fenolftalein asitte ve nötr ortamda renksizdir; bu nedenle ikisi ayırt edilemez.','renksiz → asit ya da nötr'),A('Ayıraç seç','Asidi nötrden ayırmak için asidin rengini değiştirdiği bir kâğıt gerekir.','mavi turnusol: asitte kırmızıya döner'),A('Sonucu yaz','Mavi turnusol kullanılırsa iki çözelti birbirinden ayrılır.','kırmızıya dönen: asit · değişmeyen: nötr')],
 ne='asit ile nötr çözeltiyi ayırt edecek işlem',z='kolay',alt='İndikatörler',kaz='İndikatörler kullanarak asit, baz ve nötr çözeltileri ayırt eder.',kalip='hikâyeli',
 metin='Bir öğrenci, etiketleri silinmiş üç kaptaki renksiz çözeltilerden (X, Y ve Z) birinin baz, birinin asit, birinin nötr olduğunu biliyor. Üçüne de fenolftalein damlatınca yalnızca X çözeltisi pembe oluyor; Y ve Z çözeltileri renksiz kalıyor. Öğrenci, Y ve Z çözeltilerinden hangisinin asit, hangisinin nötr olduğunu belirlemek istiyor.\nBuna göre öğrenci aşağıdakilerden hangisini yaparsa Y ve Z çözeltilerini birbirinden ayırt edebilir?',
 dogru=d18['dogru'],yan=d18['yan'],sira=d18['sira'],istenen='Y ve Z’yi ayıracak işlem.',
 ip=['Asit ile nötr çözeltiyi hangi ayıracın farklı renkle gösterdiğini düşün.'],
 bilgi=[B('Ayıraçların kullanımı','Her ayıraç her ortamda renk değiştirmez; bir ayıraçla elde edilen sonuç, ancak o ayıracın renk değiştirdiği ortamlar için bilgi verir. Örnek: kırmızı lahana suyu asit, nötr ve bazda üç ayrı renk verir')],
 puf='Bir ayıraç renk değiştirmiyorsa, elde ettiğin bilginin sınırını sorgula ve renk değiştirebileceği başka bir ayıraç seç.')

# ======================= 0019 · tepkime denklemi seçimi · orta · hikâyeli =======================
def parse(f):
    sub=str.maketrans('₀₁₂₃₄₅₆₇₈₉','0123456789'); f=f.translate(sub)
    return {e:int(n or 1) for e,n in re.findall(r'([A-Z][a-z]?)(\d*)',f)}
def dengeli(sol_,sag):
    a={};b={}
    for k,f in sol_:
        for e,n in parse(f).items(): a[e]=a.get(e,0)+k*n
    for k,f in sag:
        for e,n in parse(f).items(): b[e]=b.get(e,0)+k*n
    return a==b
dogruD=dengeli([(1,'Mg'),(2,'HCl')],[(1,'MgCl₂'),(1,'H₂')]); assert dogruD
assert dengeli([(1,'Cu'),(2,'HCl')],[(1,'CuCl₂'),(1,'H₂')])        # denk ama Cu gerçekleşmez
assert not dengeli([(1,'Zn'),(1,'HCl')],[(1,'ZnCl'),(1,'H₂')])
assert not dengeli([(1,'Al'),(3,'HCl')],[(1,'AlCl₃'),(1,'H₂')])
assert not dengeli([(1,'Mg'),(2,'HCl')],[(1,'MgCl₂'),(1,'O₂')])
d19=tek_t(('Mg + 2HCl → MgCl₂ + H₂',''),[
 ('Cu + 2HCl → CuCl₂ + H₂','denklem dengelidir ama Cu soy metaldir ve seyreltik HCl ile tepkime vermez'),
 ('Zn + HCl → ZnCl + H₂','çinko Zn²⁺ iyonu oluşturur, formül ZnCl₂ olmalıdır; denklem atom sayısı bakımından da dengeli değildir'),
 ('Al + 3HCl → AlCl₃ + H₂','denklem dengeli değildir: hidrojen sayısı sol tarafta 3, sağ tarafta 2’dir (2Al + 6HCl → 2AlCl₃ + 3H₂ olmalıdır)'),
 ('Mg + 2HCl → MgCl₂ + O₂','asit–metal tepkimesinde açığa çıkan gaz hidrojendir; ayrıca tepkimeye giren maddelerde oksijen yoktur')],0)
q('0019',ad=[A('Gazı belirle','Aktif metal asitle tuz ve H₂ gazı oluşturur; asitte oksijen yoktur.','ürün gazı: H₂'),A('Soy metali ele','Cu seyreltik HCl ile tepkime vermez; yazılan denklem gerçekleşemez.','Cu denklemi elenir'),A('Formül ve denge kontrolü','Zn²⁺ için tuz ZnCl₂’dir; Al denkleminde hidrojen sayıları eşit değildir.','Zn ve Al denklemleri elenir'),A('Doğru denklemi seç','Mg²⁺ için tuz MgCl₂’dir ve denklem dengelidir.','Mg: 1 · Cl: 2 · H: 2 → sol = sağ')],
 ne='dengeli ve gerçekleşen tepkime denklemi',z='orta',alt='Asit ve Bazların Metallerle Tepkimesi',kaz='Asit–metal tepkimelerinin denklemlerini yazar.',kalip='hikâyeli',
 metin='Bir öğrenci, seyreltik hidroklorik asit (HCl) çözeltisine magnezyum, bakır, çinko ve alüminyum parçalarını ayrı ayrı atıp gözlemleyeceği tepkimelerin denklemlerini deney öncesinde yazıyor. Öğretmeni, yazdığı denklemlerin yalnızca birinin hem dengeli hem de gerçekten gerçekleşen bir tepkimeyi gösterdiğini söylüyor.\nBuna göre aşağıdaki denklemlerden hangisi bu tepkimedir?',
 dogru=d19['dogru'],yan=d19['yan'],sira=d19['sira'],istenen='Dengeli ve gerçekleşen tepkime denklemi.',
 ip=['Her denklemde önce atom sayılarını, sonra metalin seyreltik asitle tepkime verip vermediğini kontrol et.'],
 bilgi=[B('Asit–metal denklemi','Aktif metal + asit → tuz + H₂. Tuzun formülü metalin iyon yükünden bulunur: Na⁺ için NaCl, Ca²⁺ için CaCl₂. Denklem atom sayısı bakımından dengelenir. Örnek: Zn + H₂SO₄ → ZnSO₄ + H₂')],
 puf='Önce metalin aktif olduğundan emin ol, sonra tuzun formülünü yükten yaz ve atom sayılarını eşitle.')

# ======================= 0020 · tuz kullanım alanları · orta · öncüllü =======================
d={'I':(False,'kuru pillerde kullanılan tuz NaCl değil NH₄Cl’dir; NaCl yemeklik tuz olarak ve gıda saklamada kullanılır'),
   'II':(True,'NH₄Cl (nişadır) kuru pillerde kullanılan bir tuzdur'),
   'III':(True,'CaCO₃ kireç taşı ve mermerin bileşenidir; çimento ve kireç eldesinde hammadde olarak kullanılır')}
r=onc_t(d,4)
q('0020',ad=[adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),sonuc(d,r)],
 ne='tuzların kullanım alanları',z='orta',alt='Tuzların Kullanım Alanları',kaz='Tuzların kullanım alanlarını açıklar.',kalip='öncüllü',
 metin='Bir kimya kulübünde öğrenciler, günlük hayatta ve sanayide kullanılan tuzlarla ilgili bir poster hazırlıyor. Poster için aşağıdaki bilgileri yazıp doğru olanların poster metnine alınmasını istiyorlar.\nI. NaCl, kuru pillerde kullanılan başlıca tuzdur.\nII. NH₄Cl, kuru pillerde kullanılır.\nIII. CaCO₃, çimento ve kireç elde etmede hammadde olarak kullanılır.\nBuna göre posterde hangi bilgilere yer verilmelidir?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Poster metnine alınabilecek doğru bilgiler.',
 ip=['Tuzların formüllerini kullanım alanlarıyla birlikte hatırla; kuru pillerde kullanılan tuzun formülüne dikkat et.'],
 bilgi=[B('Tuzlar','Metal (ya da NH₄⁺) iyonu ile asit kalıntısı iyonundan oluşan iyonik bileşiklere tuz denir. Tuzlar günlük hayatta, tarımda ve sanayide çok çeşitli alanlarda kullanılır. Örnek: KNO₃ gübrelerde bulunur')],
 puf='Her tuzun formülünü, kullanıldığı alanla birlikte eşleştirerek öğren.')

# ======================= 0021 · mermer + asit · zor · öncüllü =======================
mu=lambda: None
assert dengeli([(1,'CaCO₃'),(2,'HCl')],[(1,'CaCl₂'),(1,'H₂O'),(1,'CO₂')])
d={'I':(True,'CaCO₃ asitle tepkimeye girince tuz (CaCl₂), su ve CO₂ gazı oluşur'),
   'II':(False,'kireç suyunu bulandıran gaz CO₂’dir; asit–metal tepkimesindeki H₂ değildir ve CaCO₃ bir metal değil tuzdur'),
   'III':(True,'asit yağmurları da mermer ve kireçtaşı yapılardaki CaCO₃ ile benzer biçimde tepkimeye girerek bu yapıları aşındırır')}
r=onc_t(d,3)
q('0021',ad=[adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),sonuc(d,r)],
 ne='mermer üzerine asit damlatma deneyi',z='orta',alt='Asit Yağmurları',kaz='Asit yağmurlarının mermer ve kireçtaşı yapılara etkisini tepkime üzerinden açıklar.',kalip='öncüllü',
 metin='Bir öğrenci, mermer (CaCO₃) parçasının üzerine seyreltik HCl çözeltisi damlatıyor ve gaz kabarcıkları çıktığını görüyor. Çıkan gazı kireç suyundan geçirdiğinde kireç suyunun bulandığını gözlüyor. Öğrenci, bu deneyi asit yağmurlarının mermer heykellere verdiği zararla ilişkilendiriyor.\nI. Tepkimede CaCl₂, H₂O ve CO₂ oluşur.\nII. Kabarcıklar hidrojen gazıdır.\nIII. Asit yağmurları mermer yapıları benzer bir tepkimeyle aşındırır.\nBuna göre bu yargılardan hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',
 ip=['Mermerin metal mi tuz mu olduğunu ve kireç suyunu bulandıran gazın hangisi olduğunu hatırla.'],
 bilgi=[B('Tuzların asitlerle tepkimesi','Bir tuz asitle tepkimeye girerek yeni bir tuz ve başka ürünler oluşturabilir. Açığa çıkan gazın türü tepkimeye giren maddelere bağlıdır; her asit tepkimesi aynı gazı vermez')],
 puf='Ürünleri tahmin ederken girenlerin türüne bak: metal mi, tuz mu?')

# ======================= 0022 · tanecik sayımı · zor · düz =======================
Ca=2; OH=2*Ca; Hh=7; Cl=Hh
su22=min(Hh,OH); kalH=Hh-su22; son=Ca+kalH+Cl
assert OH==4 and su22==4 and kalH==3 and son==12 and Ca*2+kalH-Cl==0
assert OH+Ca+Hh+Cl==20 and son+su22==16 and Ca+kalH==5 and Ca+Cl==9
q('0022',ad=[A('Başlangıç iyonlarını yaz','Ca(OH)₂ çözeltisinde Ca²⁺ sayısının iki katı kadar OH⁻, HCl çözeltisinde H⁺ kadar Cl⁻ vardır.','Ca²⁺: 2 · OH⁻: 4 · H⁺: 7 · Cl⁻: 7'),A('Su oluşumunu hesapla','H⁺ ve OH⁻ birer birer harcanır; sayısı az olan tükenir.','4 OH⁻ + 4 H⁺ → 4 H₂O'),A('Kalan iyonları bul','H⁺’tan 7 − 4 kalır; Ca²⁺ ve Cl⁻ seyirci olarak durur.','Ca²⁺: 2 · H⁺: 3 · Cl⁻: 7'),A('Toplamı yaz','Su molekülleri iyon sayılmaz.','2 + 3 + 7 = 12')],
 ne='karışımdaki toplam iyon sayısı',z='zor',alt='Nötralleşme ve Tuz Oluşumu',kaz='Nötralleşme sonrası karışımdaki iyonları tanecik sayısıyla belirler.',kalip='hikâyeli',
 metin='Bir öğrenci, Ca(OH)₂ ve HCl çözeltilerinin tepkimesini tanecik düzeyinde modelliyor. Ca(OH)₂ çözeltisinde 2 tane Ca²⁺ iyonu ile bunlarla birlikte bulunan OH⁻ iyonları, HCl çözeltisinde ise 7 tane H⁺ iyonu ile bunlarla birlikte bulunan Cl⁻ iyonları vardır. Çözeltiler karıştırılıyor ve tam tepkime gerçekleşiyor; H⁺ ve OH⁻ iyonları yalnızca H₂O oluşturmak üzere harcanıyor.\nOluşan su molekülleri iyon olarak sayılmadığına göre karışımdaki toplam iyon sayısı kaçtır?',
 dogru=son,yan=[(5,'Cl⁻ iyonlarını da tepkimede harcanmış saymış; yalnız Ca²⁺ ve artan H⁺ iyonlarını saymış (2 + 3).','bilgi'),(9,'Artan H⁺ iyonlarını unutup yalnız Ca²⁺ ve Cl⁻ iyonlarını saymış (2 + 7).','dikkat'),(16,'Oluşan 4 H₂O molekülünü de iyon sayıp 12’ye eklemiş.','bilgi'),(20,'Tepkimeyi hesaba katmayıp başlangıçtaki bütün iyonları saymış (2 + 4 + 7 + 7).','dikkat')],
 istenen='Karışımdaki toplam iyon sayısı.',
 ip=['Sayısı az olan iyon tükenir; tükenmeyen ve tepkimeye girmeyen iyonları birlikte say.'],
 bilgi=[B('İyon sayısı ve formül','Bileşiğin formülündeki indis, çözeltideki iyon sayı oranını verir. Örnek: Mg(OH)₂ çözeltisinde 1 tane Mg²⁺ ile 2 tane OH⁻ vardır')],
 puf='Önce iyonları yaz, H⁺ ile OH⁻’ı eşit sayıda azalt, kalan ve seyirci iyonları topla; suyu sayma.')

bitir(P,'asitbaziki',UK)
