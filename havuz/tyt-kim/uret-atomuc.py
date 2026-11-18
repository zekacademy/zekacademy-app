"""TYT Kimya · Atom ve Yapısı · 3. ek paket (atomuc): 10 soru, kardeş yok, ipucu 1.
Şekil verileri Python'da hesaplanır; TikZ bu değerlerden üretilir. Öncüllerin doğru/yanlış değeri tek yerde (d sözlüğü) tanımlanır."""
import sys,os,math,random,itertools
from fractions import Fraction as Fr
GD=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,GD)
import _hafif_kim2 as H
from _hafif_kim2 import *
from _hafif_kim import onc as _onc_eski, tek
KONU_='Atom ve Yapısı'; UK='kim|Atom ve Yapısı'
H.KONU=KONU_
P=Parti('atomuc',KONU_,UK,ders='TYT Kimya',idon='tytkim')
KY='ÖSYM 2018–2026 TYT Kimya (yalnız mantık) · MEB 9. sınıf Atomun Yapısı'
MAP={}
for _n,_t in [(('01','05'),('model','Atom modelleri')),(('02','03','09'),('tanecik','Atom altı tanecikler ve izotoplar')),(('04','10'),('ortkut','Ortalama atom kütlesi ve izotop bolluğu')),(('06','08'),('iyon','İyonlar ve izoelektronik tanecikler')),(('07',),('bohr','Bohr modeli ve enerji geçişleri'))]:
    for _x in _n: MAP[_x]=_t
assert len(MAP)==10
def kartla(n,alt,fikir,tuzak,z,kalip,adim):
    a,b=MAP[n]; kart(f'K-KMAT3-{n}',alt,fikir,tuzak,z,kalip,adim,f'km-at3-{a}',b,KY)
def q(no,ad,**k):
    assert len(k['ip'])==1
    k['tipId']='km-at3-'+MAP[no[-2:]][0]; k['tip']=MAP[no[-2:]][1]
    ne=k.pop('ne'); k['kart']=f"K-KMAT3-{no[-2:]} ({MAP[no[-2:]][1].lower()}) · {ne}"
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
kartla('01','Katot ışını deneyi','Yüklü levhalar arasından geçen yüklü bir demet, zıt yüklü levhaya doğru sapar; sapma yönü demeti oluşturan taneciklerin yük işaretini gösterir.','Sapma yönünü yük işaretiyle ilişkilendirmeden yorumlamak; farklı atom modellerinin deneylerini birbirine karıştırmak.','kolay','şekilli',3)
kartla('02','Atom altı taneciklerin özellikleri','Proton ve nötron çekirdekte bulunur ve kütleleri yaklaşık eşittir; elektronun kütlesi bunlara göre çok küçüktür; proton +1, elektron −1 yüklüdür, nötron yüksüzdür.','Elektronun kütlesini protona yakın sanmak; nötronu yüklü saymak.','kolay','tablo',3)
kartla('03','İzotop atomların çekirdek modeli','İzotop atomların proton sayısı eşit, nötron sayısı farklıdır; proton sayısı elementin kimliğini ve nötr atomdaki elektron sayısını belirler.','İzotopların proton sayısının farklı olduğunu sanmak; kütle farkını kimyasal özellik farkı saymak.','orta','şekilli',4)
kartla('04','Ortalama atom kütlesi','Doğal bir elementin ortalama atom kütlesi, izotopların kütle numaralarının bolluk yüzdeleriyle ağırlıklandırılmış ortalamasıdır.','İzotopların kütlelerinin düz ortalamasını almak; bolluk yüzdelerini ters yazmak.','orta','grafik',3)
kartla('05','Dalton atom teorisi','Dalton atomu, kimyasal tepkimelerde değişmeyen, bölünemez ve katı bir küre olarak düşünmüş; tepkimeyi atomların yeniden düzenlenmesi saymıştır.','Daha sonraki modellerin yeniliklerini Dalton’a mal etmek.','kolay','hikâyeli',3)
kartla('06','İyonlu taneciklerde sayı bulma','Katman diyagramından elektron sayısı, yükten proton sayısı, kütle numarasından nötron sayısı bulunur; nötr atomun dizilimi için yük kadar elektron geri verilir ya da alınır.','Elektron sayısını proton sayısı sanmak; yükü ters işlemek.','zor','şekilli',4)
kartla('07','Enerji düzeyleri arasında geçiş','Elektron üst düzeye çıkarken enerji soğurur, alt düzeye inerken yayar; geçişteki enerji, iki düzeyin enerji farkına eşittir.','Enerji farkını düzeylerin sıra numaralarından çıkarmak; soğurma ile yayılmayı karıştırmak.','zor','öncüllü',4)
kartla('08','İzoelektronik tanecikler ve proton sayısı','Çok atomlu taneciklerde proton ve elektron sayısı atomların atom numaraları toplanarak bulunur; yük elektron sayısını değiştirir, proton sayısını değiştirmez.','Yükü proton sayısına eklemek; izoelektronik ile izoton kavramını karıştırmak.','zor','öncüllü',4)
kartla('09','İyonların elektron dizilimi','İyonun elektron sayısı atom numarası ile yükten bulunur; dizilim bu sayıdaki elektronun katmanlara 2, 8, 8 kuralıyla yerleşmesidir.','Dizilimi atomun elektron sayısına göre yazmak.','orta','tablo',3)
kartla('10','İyon, izotop ve ortalama kütle birlikte','Atom numarası aynı olan izotoplarda elektron sayısı eşittir; nötron sayısı kütle numarasından atom numarası çıkarılarak bulunur; ortalama kütle en bol izotopa yakındır.','Ortalama kütleyi izotopların düz ortalaması sanmak.','orta','öncüllü',4)

# ============================================================ 01 · katot ışını tüpü (kolay, şekil)
g='\\draw[thick] (0,-1.6) rectangle (7.6,1.6);'
g+='\\draw[thick,fill=black!30] (-.15,-.45) rectangle (.25,.45); \\node[font=\\footnotesize] at (.05,-1.0) {Katot};'
g+='\\draw[thick,fill=black!30] (1.6,-.45) rectangle (1.9,-.1); \\draw[thick,fill=black!30] (1.6,.1) rectangle (1.9,.45); \\node[font=\\footnotesize] at (1.75,-1.0) {Anot};'
g+='\\draw[thick,fill=black!15] (3.5,.75) rectangle (5.1,.95); \\node[font=\\footnotesize] at (4.3,1.2) {Levha (+)};'
g+='\\draw[thick,fill=black!15] (3.5,-.95) rectangle (5.1,-.75); \\node[font=\\footnotesize] at (4.3,-1.2) {Levha ($-$)};'
g+='\\draw[very thick,vurgu] (.25,0) -- (1.6,0) -- (3.5,0) .. controls (4.6,0) and (5.3,.35) .. (6.3,.95);'
g+='\\draw[thick] (7.6,-1.4) -- (7.6,1.4); \\node[font=\\footnotesize,rotate=90] at (7.85,0) {Ekran};'
SK1=tk(g)
dg=('Katot ışınları negatif yüklü taneciklerden oluşur.','ışın (+) levhaya doğru sapmıştır; zıt yükler çekişir, demet negatif yüklüdür')
yl=[('Katot ışınları pozitif yüklü taneciklerden oluşur.','pozitif yüklü demet (+) levhadan itilir, (−) levhaya doğru sapardı'),
    ('Işının sapması katot metalinin cinsine bağlıdır; her metalde farklı tanecikler gözlenir.','Thomson katot metalini değiştirdiğinde aynı özellikte tanecikler bulmuştur'),
    ('Bu deney, atomun merkezinde yoğun bir pozitif çekirdek bulunduğunu kanıtlamıştır.','çekirdeğin varlığı alfa saçılma deneyiyle (Rutherford) bulunmuştur'),
    ('Işının sapması, atomun parçalanamayan en küçük tanecik olduğunu gösterir.','ışının sapması atomdan daha küçük, yüklü taneciklerin varlığını gösterir')]
r=tek_t(dg,yl,0,True)
q('0001',ad=[A('Sapmayı oku','Işın üstteki (+) levhaya doğru sapmıştır.','Sapma: (+) levhaya doğru'),A('Yükü yorumla','Zıt yükler birbirini çeker; ışın (+) levhaya çekildiğine göre negatif yüklüdür.','Demet: negatif yüklü'),A('Yargıları sına','Her yargı bu sonuçla ve deneyin kime ait olduğuyla karşılaştırılır.','Doğru yargı: negatif yüklü tanecikler')],
 alt='Atom Modelleri',z='kolay',kaz='Katot ışını tüpündeki sapmadan taneciklerin yük işaretini ve deneyin sonucunu yorumlar.',kalip='şekilli',ne='katot ışını tüpü, yüklü levhalar',
 metin='Havası boşaltılmış bir cam tüpte katottan çıkan ışınlar, yüklü iki levha arasından geçirilerek ekrana ulaştırılıyor. Üstteki levha (+), alttaki levha (−) yüklüdür. Işının izlediği yol şekilde gösterilmiştir. Bu düzenek, Thomson’un yaptığı deneye benzemektedir.\nBuna göre aşağıdakilerden hangisi doğrudur?',
 sekil=SK1,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargı.',
 ip=['Işının hangi levhaya doğru sapıp hangisinden uzaklaştığına bak.'],
 bilgi=[B('Yükler arasındaki kuvvet','Zıt yükler birbirini çeker, aynı yükler birbirini iter. Yüklü bir demet, zıt yüklü levhaya doğru sapar')],
 puf='Sapma yönü, demetin yükünü gösterir.')

# ============================================================ 02 · atom altı tanecik tablosu (kolay, tablo)
SK2=tablo_svg(['Tanecik','Bulunduğu yer','Yük','Kütle (u)'],[['Proton','Çekirdek','+1','1'],['Nötron','Çekirdek','0','1'],['Elektron','Çekirdek dışı','−1','yaklaşık 0,0005']])
dg=('Atomun kütlesinin hemen hemen tamamı çekirdekte toplanmıştır.','proton ve nötron birer u kütlelidir, elektronun kütlesi ihmal edilebilecek kadar küçüktür')
yl=[('Elektronun kütlesi protona yakındır; bu yüzden kütle numarasına elektronlar da katılır.','elektronun kütlesi protonunkinin binde birinden azdır; kütle numarası proton + nötrondur'),
    ('Nötron yüklü olduğundan çekirdekteki toplam pozitif yükü artırır.','nötronun yükü sıfırdır; çekirdeğin yükünü yalnız protonlar belirler'),
    ('Her atomda proton sayısı nötron sayısına eşittir.','tablo bunu söylemez; ¹H atomunda nötron yoktur, çoğu atomda ise nötron sayısı protondan farklıdır'),
    ('Elektronlar çekirdekte, protonlarla birlikte bulunur.','tabloya göre elektronlar çekirdek dışında bulunur')]
r=tek_t(dg,yl,2,True)
q('0002',ad=[A('Tabloyu oku','Üç taneciğin yeri, yükü ve kütlesi karşılaştırılır.','Proton, nötron: çekirdek, 1 u; elektron: dışarıda, ≈ 0'),A('Kütleyi yorumla','Elektronun kütlesi çok küçük olduğundan atomun kütlesi çekirdekle belirlenir.','Kütle: çekirdekte'),A('Yargıları sına','Her yargı tablo ve bu sonuçla karşılaştırılır.','Doğru yargı: kütle çekirdekte')],
 alt='Atomun Yapısı',z='kolay',kaz='Atom altı taneciklerin yük, kütle ve konumunu karşılaştırır.',kalip='tablo',ne='proton, nötron, elektron tablosu',
 metin='Bir öğrenci, atomu oluşturan taneciklerin bazı özelliklerini tabloda göstermiştir.\nBuna göre aşağıdakilerden hangisi doğrudur?',
 sekil=SK2,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargı.',
 ip=['Tabloda her taneciğin yerine ve kütlesine bak.'],
 bilgi=[B('Atom altı tanecikler','Atomun çekirdeğinde proton ve nötron bulunur; elektronlar çekirdek çevresinde hareket eder. Kütle numarası, proton ve nötron sayılarının toplamıdır')],
 puf='Tablodaki yer, yük ve kütle bilgilerini birlikte değerlendir.')

# ============================================================ 03 · izotop çekirdek modeli (orta, öncüllü, şekil)
def cekirdek(x0,p,n,seed):
    s=f'\\draw[thick] ({x0},0) circle (1.05);'
    rng=random.Random(seed); L=[]
    while len(L)<p+n:
        x,y=rng.uniform(-.82,.82),rng.uniform(-.82,.82)
        if x*x+y*y<=.82**2 and all((x-a)**2+(y-b)**2>=.34**2 for a,b in L): L.append((x,y))
    for k,(x,y) in enumerate(L):
        s+=disc(x0+x,y,.13,'vurgu!50') if k<p else disc(x0+x,y,.13,'white')
    return s
g=''
for nm,x0,pp,nn,sd in (('X',0,6,6,21),('Y',3.0,6,7,22),('Z',6.0,6,8,23)): g+=cekirdek(x0,pp,nn,sd)+f'\\node[font=\\bfseries] at ({x0},-1.45) {{{nm}}};'
g+='\\draw[thin,fill=vurgu!50] (0.2,-2.25) circle (.13); \\node[right,font=\\footnotesize] at (.4,-2.25) {: proton}; \\draw[thin,fill=white] (2.4,-2.25) circle (.13); \\node[right,font=\\footnotesize] at (2.6,-2.25) {: nötron};'
SK3=tk(g)
d={'I':(False,'X, Y ve Z çekirdeklerinin her birinde 6 proton vardır; proton sayısı eşittir'),
   'II':(True,'proton sayısı eşit olduğundan nötr atomların elektron sayıları da eşittir (6)'),
   'III':(True,'proton sayıları eşit olan atomlar aynı elementin izotoplarıdır; kimyasal özellikleri benzerdir')}
r=onc_t(d,3)
q('0003',ad=[A('Çekirdekleri say','Yeşil daireler protonu, beyaz daireler nötronu gösterir.','X: 6 p, 6 n; Y: 6 p, 7 n; Z: 6 p, 8 n'),adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),A('Sonucu yaz','Doğru olan öncüller bir arada yazılır.',oy(d)+' · Sonuç: '+r['dogru'])],
 alt='İzotop Atomlar',z='orta',kaz='Çekirdek modellerinden proton ve nötron sayılarını okuyup izotop atomları yorumlar.',kalip='öncüllü',ne='X, Y, Z çekirdeklerinin proton ve nötron modelleri',
 metin='Şekilde X, Y ve Z atomlarının çekirdekleri modellenmiştir (harfler gerçek element sembolü değildir).\nI. Z atomunun proton sayısı X atomununkinden fazladır.\nII. Nötr hâldeki X, Y ve Z atomlarının elektron sayıları eşittir.\nIII. X, Y ve Z atomlarının kimyasal özellikleri benzerdir.\nBuna göre hangileri doğrudur?',
 sekil=SK3,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan öncüller.',
 ip=['Her çekirdekteki yeşil ve beyaz daireleri ayrı ayrı say.'],
 bilgi=[B('Proton sayısı','Proton sayısı, atomun hangi element olduğunu belirler. Nötr bir atomda elektron sayısı proton sayısına eşittir')],
 puf='Önce her çekirdekte proton ve nötron sayılarını ayrı ayrı say.')

# ============================================================ 04 · klor izotop bolluğu (orta, grafik, sayısal)
Sy4=.05
g=eksen(2.8,100,1,Sy4,[],[0,25,50,75,100],'','Doğadaki bolluk (\\%)',xtik=False)
for i,(nm,v) in enumerate((('³⁵Cl',75),('³⁷Cl',25))):
    x=.9+i*1.3
    g+=f'\\draw[fill=vurgu!30,thick] ({x-.4:.2f},0) rectangle ({x+.4:.2f},{v*Sy4:.3f}); \\node[font=\\small\\bfseries] at ({x:.2f},-.35) {{{"$^{35}$Cl" if i==0 else "$^{37}$Cl"}}};'
SK4=tk(g)
ort=Fr(35*75+37*25,100); assert ort==Fr(71,2)
r4=dict(dogru=35.5)
q('0004',ad=[A('Grafiği oku','Bolluk yüzdeleri çubuk yüksekliklerinden okunur.','³⁵Cl: %75; ³⁷Cl: %25'),A('Ağırlıklı ortalama','Her izotopun kütle numarası bolluk oranıyla çarpılıp toplanır.','(35 × 75 + 37 × 25) / 100'),A('Sonucu bul','Toplam 100’e bölünür.','3550 / 100 = 35,5')],
 alt='Ortalama Atom Kütlesi',z='orta',kaz='İzotop bolluk grafiğinden elementin ortalama atom kütlesini bulur.',kalip='grafik',ne='klorun iki izotopunun bolluk grafiği',
 metin='Doğal klor örneği, kütle numaraları 35 ve 37 olan iki izotoptan oluşmaktadır. İzotopların doğadaki bolluk yüzdeleri grafikte verilmiştir. Bir izotopun atom kütlesi yaklaşık olarak kütle numarasına eşit alınacaktır.\nBuna göre klorun ortalama atom kütlesi kaçtır?',
 sekil=SK4,dogru=35.5,yan=[(35.0,'En bol izotopun kütle numarasını ortalama sanmış.','bilgi'),(36.0,'İki kütle numarasının düz ortalamasını almış; bolluk yüzdelerini kullanmamış.','islem'),(36.5,'Bolluk yüzdelerini ters yazmış (³⁵Cl’yi %25, ³⁷Cl’yi %75 almış).','islem'),(37.0,'En ağır izotopun kütle numarasını ortalama sanmış.','bilgi')],
 istenen='Klorun ortalama atom kütlesi.',
 ip=['Her izotopun kütle numarasını kendi bolluk oranıyla çarpıp topla.'],
 bilgi=[B('Ortalama atom kütlesi','Ortalama atom kütlesi, izotopların kütlelerinin bolluk oranlarıyla çarpılıp toplanmasıyla bulunur. Örnek: iki izotopu eşit bollukta olan bir elementin ortalama kütlesi, iki kütlenin düz ortalamasıdır')],
 puf='Düz ortalama değil, bolluğa göre ağırlıklı ortalama al.')

# ============================================================ 05 · Dalton (orta, hikâyeli)
dg=('Atomlar tepkimelerde yok olmaz, yeni atom oluşmaz.','Dalton modelinde atomlar bölünemez, tepkimelerde değişmez; kütlenin korunumu bununla açıklanır')
yl=[('Dalton atomun içinde elektron denilen negatif yüklü taneciklerin bulunduğunu ileri sürmüştür.','elektronun varlığı Thomson’un deneylerinden sonra anlaşılmıştır; Dalton atomu bölünemez sanmıştır'),
    ('Dalton’a göre aynı elementin atomlarının kütleleri birbirinden farklı olabilir.','Dalton, aynı elementin bütün atomlarının özdeş (aynı kütleli) olduğunu kabul etmiştir; izotoplar sonradan bulunmuştur'),
    ('Dalton modelinde elektronlar çekirdek çevresindeki belirli enerji katmanlarında dolanır.','enerji katmanları fikri Bohr modeline aittir'),
    ('Dalton, atomun hacminin büyük kısmının boşluk olduğunu savunmuştur.','atomun büyük kısmının boş olduğu, alfa saçılma deneyiyle (Rutherford) anlaşılmıştır')]
r=tek_t(dg,yl,4,True)
q('0005',ad=[A('Dalton modelini hatırla','Atom bölünemez, tepkimelerde değişmeyen küredir; aynı elementin atomları özdeştir.','Dalton: katı, bölünmez küre'),A('Sonraki modelleri ayır','Elektron, çekirdek ve katman fikirleri Dalton’dan sonraki modellerde ortaya çıkmıştır.','Thomson, Rutherford, Bohr'),A('Yargıları sına','Her yargı bu ayrımla karşılaştırılır.','Doğru yargı: atomlar yok olmaz')],
 alt='Atom Modelleri',z='kolay',kaz='Dalton atom teorisinin ilkelerini sonraki modellerin yeniliklerinden ayırt eder.',kalip='hikâyeli',ne='kütlenin korunumu ve Dalton atom teorisi',
 metin='Fen kulübünde Nehir, kapalı bir kapta gerçekleşen bir tepkimede tepkimeden önceki ve sonraki toplam kütlenin değişmediğini gözlemliyor. Bunu, 1800’lerin başında atomu bölünemeyen, içi dolu bir küre olarak tasarlayan Dalton’un atom teorisiyle açıklamak istiyor.\nBuna göre aşağıdakilerden hangisi Dalton atom teorisinin ilkelerindendir?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Dalton atom teorisinin ilkesi.',
 ip=['Dalton’un atomu nasıl tasarladığını düşün.'],
 bilgi=[B('Atom modelleri','Dalton’dan sonra Thomson elektronu, Rutherford çekirdeği, Bohr enerji katmanlarını modele ekledi. Her model, önceki modelin açıklayamadığı gözlemleri açıklamak için geliştirildi')],
 puf='Önce Dalton modelinde neler olmadığını (elektron, çekirdek, katman) belirle.')

# ============================================================ 06 · iyon Bohr diyagramı (zor, şekil)
def bohr(x0,kat,etiket):
    s=f'\\draw[fill=white] ({x0},0) circle (.3);'
    for i,n in enumerate(kat):
        r_=.62+.32*i; s+=f'\\draw[black!50] ({x0},0) circle ({r_});'
        for k in range(n):
            a=2*math.pi*k/n+i*.5; s+=f'\\fill ({x0+r_*math.cos(a):.2f},{r_*math.sin(a):.2f}) circle (.055);'
    s+=f'\\node[font=\\bfseries] at ({x0},-1.9) {{{etiket}}};'
    return s
g=bohr(0,[2,8,8],'Z$^{3-}$')
SK6=tk(g)
p6=18-3; A6=31; n6=A6-p6; assert (p6,n6)==(15,16)
dg=('Z atomunun çekirdeğinde 16 nötron vardır ve Z atomunun 5 değerlik elektronu bulunur.','proton sayısı 18 − 3 = 15, nötron sayısı 31 − 15 = 16; nötr Z atomunun dizilimi 2, 8, 5’tir')
yl=[('Z³⁻ iyonunda 15 elektron bulunur.','şekilde 2 + 8 + 8 = 18 elektron vardır; 15 Z’nin proton sayısıdır'),
    ('Z atomunun elektron dizilimi 2, 8, 8’dir.','2, 8, 8 iyonun dizilimidir; nötr atom 3 elektron daha az taşır: 2, 8, 5'),
    ('Z³⁻ iyonu, atom numarası 18 olan bir atomla aynı sayıda protona sahiptir.','Z³⁻ iyonu 18 elektrona sahiptir (Ar ile izoelektronik), protonu ise 15’tir'),
    ('Z³⁻ iyonunun elektron katmanı sayısı, Z atomununkinden fazladır.','Z atomu da 3 katmana sahiptir; fazladan alınan 3 elektron aynı katmanlara yerleşir')]
r=tek_t(dg,yl,0,True)
q('0006',ad=[A('Elektron sayısını bul','Şekilde elektronlar sayılır; yük elektron fazlasını gösterir.','e = 2 + 8 + 8 = 18'),A('Proton ve nötron','Proton sayısı elektron sayısından yük kadar eksiktir; nötron = kütle numarası − proton.','p = 18 − 3 = 15; n = 31 − 15 = 16'),A('Nötr atomu yaz','Fazla 3 elektron çıkarılınca nötr atomun dizilimi bulunur.','Z: 2, 8, 5'),A('Yargıları sına','Bulunan değerler her yargıyla karşılaştırılır.','n = 16 ve değerlik e⁻ = 5')],
 alt='İyonlar',z='zor',kaz='Katman diyagramı, yük ve kütle numarasından proton, nötron ve nötr atomun dizilimini birlikte belirler.',kalip='şekilli',ne='Z³⁻ iyonunun katman diyagramı, kütle numarası 31',
 metin='Şekilde, kütle numarası 31 olan Z³⁻ iyonunun katman diyagramı verilmiştir; çekirdekteki proton sayısı gösterilmemiştir (Z gerçek element sembolü değildir).\nBuna göre aşağıdakilerden hangisi doğrudur?',
 sekil=SK6,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargı.',
 ip=['Önce şekilden elektron sayısını, sonra yükten proton sayısını bul.'],
 bilgi=[B('İyonda tanecik sayıları','Proton sayısı, iyon yükü eksi ise elektron sayısından yük kadar az, artı ise yük kadar fazladır. Nötron sayısı, kütle numarasından proton sayısı çıkarılarak bulunur. Örnek: O²⁻ iyonunda 10 elektron, 8 proton vardır')],
 puf='Sırayla elektron, proton, nötron sayılarını bul; sonra nötr atomun dizilimine geç.')

# ============================================================ 07 · enerji düzeyi geçişleri (zor, öncüllü, şekil)
LV=[('K',0,''),('L',1.5,''),('M',2.5,''),('N',3.2,'')]
g='\\draw[thick,'+ARR+'] (-1.6,-.2) -- (-1.6,4.1); \\node[above,font=\\footnotesize] at (-1.0,4.1) {Enerji};'
for nm,y,e in LV:
    g+=f'\\draw[thick] (0,{y}) -- (7,{y}); \\node[right,font=\\small\\bfseries] at (7.1,{y}) {{{nm}}}; \\node[left,font=\\footnotesize] at (-.1,{y}) {{{e}}};'
g+=f'\\draw[thick,vurgu,-{{Stealth[length=2mm]}}] (1.5,0) -- (1.5,1.5); \\node[above,font=\\small\\bfseries] at (1.5,1.55) {{1}};'
g+=f'\\draw[thick,vurgu,-{{Stealth[length=2mm]}}] (3.7,2.5) -- (3.7,0); \\node[above,font=\\small\\bfseries] at (3.7,2.55) {{2}};'
g+=f'\\draw[thick,vurgu,-{{Stealth[length=2mm]}}] (5.7,3.2) -- (5.7,1.5); \\node[above,font=\\small\\bfseries] at (5.7,3.25) {{3}};'
SK7=tk(g)
E={'K':0,'L':1.5,'M':2.5,'N':3.2}
e1=E['L']-E['K']; e2=E['M']-E['K']; e3=E['N']-E['L']
assert e1>0 and e2>e1 and e3>e1 and e3<e2
d={'I':(False,'1. geçiş K’den L’ye, yani alt düzeyden üst düzeye olduğundan atom enerji soğurur; ışıma yapmaz'),
   'II':(True,'2. geçiş K ile M arasındadır, 1. geçiş K ile L arasındadır; K–M aralığı K–L aralığından büyüktür, bu yüzden yayılan enerji soğurulandan büyüktür'),
   'III':(False,'3. geçiş N ile L arasındadır, 2. geçiş M ile K arasındadır; N–L aralığı M–K aralığından küçüktür, 3. geçişte yayılan enerji daha azdır')}
r=onc_t(d,1)
q('0007',ad=[A('Okların yönünü oku','Yukarı ok enerji soğurulduğunu, aşağı ok yayıldığını gösterir.','1: yukarı; 2, 3: aşağı'),A('Düzey aralıklarını karşılaştır','Geçişteki enerji, iki düzey arasındaki uzaklıkla orantılıdır.','K–M aralığı > K–L aralığı; N–L aralığı < K–M aralığı'),adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),A('Sonucu yaz','Doğru olan öncüller bir arada yazılır.',oy(d)+' · Sonuç: '+r['dogru'])],
 alt='Bohr Modeli',z='zor',kaz='Enerji düzeyi diyagramından geçişlerde enerji soğurulup yayıldığını ve enerji farklarını karşılaştırır.',kalip='öncüllü',ne='enerji düzeyi diyagramı ve 1, 2, 3 numaralı geçişler',
 metin='Şekilde, Bohr modeline göre bir atomun K, L, M ve N enerji düzeyleri verilmiştir; düzeyler arasındaki uzaklıklar enerji farkıyla orantılı çizilmiştir. Elektronun yaptığı üç geçiş 1, 2 ve 3 numaralı oklarla gösterilmiştir.\nI. 1. geçişte atom ışıma yapar.\nII. 2. geçişte yayılan enerji, 1. geçişte soğurulan enerjiden büyüktür.\nIII. 3. geçişte yayılan enerji, 2. geçişte yayılan enerjiden büyüktür.\nBuna göre hangileri doğrudur?',
 sekil=SK7,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan öncüller.',
 ip=['Okun yönüne bakarak enerjinin soğurulduğunu ya da yayıldığını belirle; sonra düzeyler arasındaki uzaklığa bak.'],
 bilgi=[B('Enerji düzeyleri','Elektron üst düzeye çıkarken enerji soğurur, alt düzeye inerken yayar. Geçişteki enerji, iki düzeyin enerji farkına eşittir. Örnek: birbirinden uzak iki düzey arasındaki geçişte, yakın iki düzey arasındakinden daha büyük enerji alışverişi olur')],
 puf='Önce her okun yönüne, sonra iki düzey arasındaki enerji farkına bak.')

# ============================================================ 08 · izoelektronik çok atomlu tanecikler (zor, öncüllü, hikâyeli)
Zat={'H':1,'N':7,'O':8}
def pe(f,q_):
    p=sum(Zat[a]*n for a,n in f.items()); return p,p-q_
NH3=pe({'N':1,'H':3},0); NH4=pe({'N':1,'H':4},1); H2O=pe({'H':2,'O':1},0); OH=pe({'O':1,'H':1},-1); H3O=pe({'H':3,'O':1},1)
assert NH3==(10,10) and NH4==(11,10) and H2O==(10,10) and OH==(9,10) and H3O==(11,10)
d={'I':(True,'NH₃ ve OH⁻ taneciklerinin ikisinde de 10 elektron vardır; izoelektroniktirler'),
   'II':(True,'NH₄⁺’da 7 + 4 = 11 proton, H₃O⁺’da 8 + 3 = 11 proton vardır; proton sayıları eşittir'),
   'III':(False,'H₂O’da 8 + 2 = 10 proton, OH⁻’da 8 + 1 = 9 proton vardır; eşit değildir')}
r=onc_t(d,2)
q('0008',ad=[A('Proton sayılarını bul','Atomların atom numaraları toplanır; yük proton sayısını değiştirmez.','NH₃: 10; NH₄⁺: 11; H₂O: 10; OH⁻: 9; H₃O⁺: 11'),A('Elektron sayılarını bul','Elektron sayısı = proton sayısı − yük.','NH₃: 10; NH₄⁺: 10; OH⁻: 10'),adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),A('Sonucu yaz','Doğru olan öncüller bir arada yazılır.',oy(d)+' · Sonuç: '+r['dogru'])],
 alt='İzoelektronik Tanecikler',z='zor',kaz='Çok atomlu taneciklerde proton ve elektron sayılarını bulup izoelektronik olanları belirler.',kalip='öncüllü',ne='NH₃, NH₄⁺, H₂O, OH⁻, H₃O⁺ taneciklerinin proton ve elektron sayıları',
 metin='Atom numaraları H: 1, N: 7 ve O: 8 olan elementlerden oluşan NH₃, NH₄⁺, H₂O, OH⁻ ve H₃O⁺ tanecikleri inceleniyor (aynı sayıda elektron taşıyan taneciklere izoelektronik denir).\nI. NH₃ ve OH⁻ izoelektroniktir.\nII. NH₄⁺ ve H₃O⁺ taneciklerinin proton sayıları eşittir.\nIII. H₂O ve OH⁻ taneciklerinin proton sayıları eşittir.\nBuna göre hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan öncüller.',
 ip=['Her taneciğin proton sayısını atom numaralarının toplamından, elektron sayısını yükten bul.'],
 bilgi=[B('Çok atomlu tanecikler','Çok atomlu bir taneciğin proton sayısı, atomlarının atom numaraları toplanarak bulunur. Elektron sayısı, proton sayısından yük çıkarılarak bulunur. Örnek: CH₄’te proton ve elektron sayısı 10’dur')],
 puf='Proton sayısı atomlardan, elektron sayısı protondan ve yükten bulunur.')

# ============================================================ 09 · iyon dizilimi tablosu (orta, tablo, olumsuz)
IT=[('Mg²⁺','12','2, 8'),('S²⁻','16','2, 8, 8'),('K⁺','19','2, 8, 8'),('Cl⁻','17','2, 8, 7'),('Al³⁺','13','2, 8')]
SK9=tablo_svg(['Tanecik','Atom numarası','Elektron dizilimi'],[list(t) for t in IT])
iyk={'Mg²⁺':(12,2),'S²⁻':(16,-2),'K⁺':(19,1),'Cl⁻':(17,-1),'Al³⁺':(13,3)}
def dizil(e):
    out=[]
    for c in (2,8,8):
        t=min(c,e); out.append(t); e-=t
        if e==0: break
    return ', '.join(map(str,out))
dog={k:dizil(a-y) for k,(a,y) in iyk.items()}
yanlis=[k for k,_,dz in IT if dog[k]!=dz]; assert yanlis==['Cl⁻']
dg=('Cl⁻','Cl⁻ iyonunun 17 + 1 = 18 elektronu vardır; dizilimi 2, 8, 8 olmalıdır (tabloda 2, 8, 7 yazılmış)')
yl=[('Mg²⁺','12 − 2 = 10 elektron; 2, 8 doğrudur'),('S²⁻','16 + 2 = 18 elektron; 2, 8, 8 doğrudur'),('K⁺','19 − 1 = 18 elektron; 2, 8, 8 doğrudur'),('Al³⁺','13 − 3 = 10 elektron; 2, 8 doğrudur')]
r=tek_t(dg,yl,3,False)
q('0009',ad=[A('Elektron sayılarını bul','Elektron sayısı atom numarası ile yükten bulunur.','Mg²⁺: 10; S²⁻: 18; K⁺: 18; Cl⁻: 18; Al³⁺: 10'),A('Dizilimleri yaz','Elektronlar katmanlara 2, 8, 8 sırasıyla yerleştirilir.','10 → 2, 8; 18 → 2, 8, 8'),A('Tabloyla karşılaştır','Tablodaki dizilim bulunanla eşleşmeyen satır yanlıştır.','Eşleşmeyen: Cl⁻')],
 alt='Elektron Dizilimi',z='orta',kaz='İyonların elektron sayısını bulup elektron dizilimlerini katmanlara yerleştirir.',kalip='tablo',ne='beş iyonun elektron dizilimi tablosu',
 metin='Bir öğrenci, beş iyonun atom numaralarını ve elektron dizilimlerini tabloda göstermiştir. Tabloda yalnız bir iyonun elektron dizilimi yanlış yazılmıştır.\nBuna göre hangi iyonun elektron dizilimi yanlıştır?',
 sekil=SK9,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Dizilimi yanlış yazılan iyon.',
 ip=['Her iyonun elektron sayısını atom numarası ve yükten bul.'],
 bilgi=[B('İyonun elektron dizilimi','İyondaki elektron sayısı, atom numarasından artı yük kadar eksik, eksi yük kadar fazladır. Elektronlar K, L, M katmanlarına sırayla 2, 8, 8 olacak şekilde yerleşir. Örnek: Li⁺ iyonunda 2 elektron vardır')],
 puf='Elektron sayısını bulmadan dizilimi atom numarasına göre yazma.')

# ============================================================ 10 · magnezyum izotopları (zor, öncüllü, grafik)
MG=[(24,79),(25,10),(26,11)]
Sy10=.04
g=eksen(4.2,100,1,Sy10,[],[0,20,40,60,80,100],'','Doğadaki bolluk (\\%)',xtik=False)
for i,(a,v) in enumerate(MG):
    x=.9+i*1.2
    g+=f'\\draw[fill=vurgu!30,thick] ({x-.4:.2f},0) rectangle ({x+.4:.2f},{v*Sy10:.3f}); \\node[font=\\small\\bfseries] at ({x:.2f},-.35) {{$^{{{a}}}$Mg}}; \\node[above,font=\\footnotesize] at ({x:.2f},{v*Sy10:.3f}) {{{v}}};'
SK10=tk(g)
ortMg=sum(a*v for a,v in MG)/100; assert 24<ortMg<25 and abs(ortMg-24.32)<1e-9
d={'I':(True,'²⁴Mg²⁺ iyonunda elektron sayısı 12 − 2 = 10, nötron sayısı 24 − 12 = 12’dir'),
   'II':(True,'²⁶Mg’de nötron sayısı 26 − 12 = 14, ²⁴Mg’de 12’dir; fark 2’dir'),
   'III':(True,'ortalama atom kütlesi (24×79 + 25×10 + 26×11)/100 = 24,32’dir; 24 ile 25 arasındadır')}
r=onc_t(d,4)
q('0010',ad=[A('Bollukları oku','Çubukların üzerindeki sayılar bolluk yüzdesidir.','²⁴Mg: 79; ²⁵Mg: 10; ²⁶Mg: 11'),adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),A('Sonucu yaz','Doğru olan öncüller bir arada yazılır.',oy(d)+' · Sonuç: '+r['dogru'])],
 alt='Ortalama Atom Kütlesi',z='orta',kaz='İyon, izotop ve ortalama atom kütlesi kavramlarını birlikte kullanarak yargıları değerlendirir.',kalip='öncüllü',ne='magnezyum izotoplarının bolluk grafiği',
 metin='Atom numarası 12 olan magnezyumun doğal örneği, kütle numaraları 24, 25 ve 26 olan üç izotoptan oluşmaktadır. İzotopların doğadaki bolluk yüzdeleri grafikte verilmiştir.\nI. ²⁴Mg²⁺ iyonunda 10 elektron ve 12 nötron vardır.\nII. ²⁶Mg atomunun nötron sayısı, ²⁴Mg atomununkinden 2 fazladır.\nIII. Magnezyumun ortalama atom kütlesi 24 ile 25 arasındadır.\nBuna göre hangileri doğrudur?',
 sekil=SK10,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan öncüller.',
 ip=['Her öncül için ilgili izotopun proton, nötron ve elektron sayısını ayrı ayrı bul.'],
 bilgi=[B('İzotop ve iyon','Bir elementin izotoplarında proton sayısı aynıdır; nötron sayısı kütle numarasından atom numarası çıkarılarak bulunur. İyonun elektron sayısı yüke göre değişir. Örnek: ²³Na atomunda 12 nötron vardır')],
 puf='Ortalama kütlenin hangi izotopa yakın olacağını bolluk oranlarından tahmin et.')

bitir(P,'atomuc',UK)
