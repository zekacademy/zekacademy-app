"""TYT Kimya · Periyodik Sistem · 3. ek paket (periyodikuc): 10 soru, kardeş yok, ipucu 1.
Şekil verileri Python'da hesaplanır; TikZ bu değerlerden üretilir. Öncüllerin doğru/yanlış değeri tek yerde (d sözlüğü) tanımlanır."""
import sys,os,math,random,itertools
from fractions import Fraction as Fr
GD=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,GD)
import _hafif_kim2 as H
from _hafif_kim2 import *
from _hafif_kim import onc as _onc_eski, tek
KONU_='Periyodik Sistem'; UK='kim|Periyodik Sistem'
H.KONU=KONU_
P=Parti('periyodikuc',KONU_,UK,ders='TYT Kimya',idon='tytkim')
KY='ÖSYM 2018–2026 TYT Kimya (yalnız mantık) · MEB 9. sınıf Periyodik Sistem'
MAP={}
for _n,_t in [(('01','02'),('sinif','Elementlerin sınıflandırılması')),(('03','05'),('eneg','Elektronegatiflik ve metalik karakter')),(('06',),('grup','Grup içi eğilimler')),(('07','08'),('iyon','İyon yarıçapı ve iyonlaşma enerjisi')),(('04','09','10'),('konum','Tablodaki konumdan element belirleme'))]:
    for _x in _n: MAP[_x]=_t
assert len(MAP)==10
def kartla(n,alt,fikir,tuzak,z,kalip,adim):
    a,b=MAP[n]; kart(f'K-KMPR3-{n}',alt,fikir,tuzak,z,kalip,adim,f'km-pr3-{a}',b,KY)
def q(no,ad,**k):
    assert len(k['ip'])==1
    k['tipId']='km-pr3-'+MAP[no[-2:]][0]; k['tip']=MAP[no[-2:]][1]
    ne=k.pop('ne'); k['kart']=f"K-KMPR3-{no[-2:]} ({MAP[no[-2:]][1].lower()}) · {ne}"
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
kartla('01','Metal, yarı metal ve ametal','Periyodik sistemde metaller sol ve ortada, ametaller sağ üstte yer alır; yarı metaller (B, Si, Ge, As, Sb, Te) bu iki bölgenin sınırındadır ve iletkenlikleri ikisinin arasındadır.','Yarı metalleri ametal ya da metal saymak; her ametalin gaz olduğunu sanmak.','kolay','şekilli',3)
kartla('02','A grubu elementlerinin adları','1A alkali metaller, 2A toprak alkali metaller, 3A toprak metalleri, 7A halojenler, 8A soy gazlardır; A grubu numarası değerlik elektron sayısını verir.','Grup adlarını birbirine karıştırmak; elementin grubunu atom numarasından bulmayı atlamak.','kolay','tablo',3)
kartla('03','Periyotta elektronegatiflik','Aynı periyotta soldan sağa atom yarıçapı azalır, elektronegatiflik ve ametalik karakter artar; soy gazlar bu karşılaştırmaya katılmaz.','Elektronegatifliği metalik karakterle aynı yönde değiştiğini sanmak.','orta','grafik',3)
kartla('04','Uzun periyodik tabloda konum','1A–2A ile 3A–8A arasında B grubu (geçiş) elementleri bulunur; 4. periyottan itibaren B grubu başlar; her periyot soy gazla biter.','B grubu elementlerinin değerlik elektron sayısını grup numarasından çıkarmak.','orta','öncüllü',4)
kartla('05','Grup içinde metalik karakter','Aynı grupta yukarıdan aşağı inildikçe atom yarıçapı artar, iyonlaşma enerjisi azalır, değerlik elektronu daha kolay verilir ve metalik karakter artar.','Aşağıdaki elementin elektron sayısı arttığı için elektronu daha zor verdiğini sanmak.','orta','hikâyeli',3)
kartla('06','Grup içinde atom yarıçapı ve iyonlaşma enerjisi','Veri tablosundaki grup içi eğilim, sonraki elemente de uzatılabilir: yarıçap aşağı doğru artar, birinci iyonlaşma enerjisi azalır.','Değerlik elektron sayısının grup içinde arttığını düşünmek.','orta','öncüllü',4)
kartla('07','İzoelektronik iyonların yarıçapı','Elektron sayısı eşit taneciklerde proton sayısı arttıkça çekirdeğin çekimi artar ve yarıçap küçülür.','Yarıçapı yalnız elektron sayısına bağlamak; katyon yarıçapını atomuyla karıştırmak.','zor','grafik',4)
kartla('08','Ardışık iyonlaşma enerjileri','Ardışık iyonlaşma enerjisinde ani sıçrama, değerlik elektronlarının bittiğini ve bir sonraki elektronun iç katmandan koptuğunu gösterir.','Sıçramanın hangi elektrondan sonra olduğunu yanlış okumak; ardışık değerleri birbirinden çıkarmak.','zor','tablo',4)
kartla('09','İyon dizilimlerinden elementleri bulma','İyonun elektron sayısından atom numarası bulunur; verilen konum ilişkilerinden (aynı grup, aynı periyot) diğer elementler belirlenir.','Konum ilişkilerini birbirine karıştırmak (aynı grup yerine aynı periyot almak).','zor','öncüllü',5)
kartla('10','Tabloda komşu elementlerin karşılaştırılması','Periyotta sağa gidildikçe, grupta aşağı inildikçe periyodik özellikler zıt yönlerde değişir; iyonların yarıçapı da aynı kuralı izler.','Atom yarıçapı eğilimini iyonlaşma enerjisine de aynen uygulamak.','zor','öncüllü',4)

# ============================================================ 01 · metal–yarı metal–ametal (kolay, şekil)
SINIF={}
for c in range(8):
    SINIF[(2,c+1)]='M' if c<2 else ('Y' if c==2 else 'A')
    SINIF[(3,c+1)]='M' if c<3 else ('Y' if c==3 else 'A')
POS1={'X':(3,1),'Y':(2,3),'Z':(3,6),'T':(3,3)}
assert SINIF[POS1['X']]=='M' and SINIF[POS1['Y']]=='Y' and SINIF[POS1['Z']]=='A' and SINIF[POS1['T']]=='M'
g=''
for c in range(8): g+=f'\\node[font=\\footnotesize] at ({c*.85+.42:.2f},1.95) {{{c+1}A}};'
for rr,(per,y0) in enumerate([(2,.95),(3,.1)]):
    g+=f'\\node[font=\\footnotesize,anchor=east] at (-.1,{y0+.42:.2f}) {{{per}. periyot}};'
    for c in range(8):
        f={'M':'vurgu!35','Y':'black!25','A':'white'}[SINIF[(per,c+1)]]
        g+=f'\\draw[fill={f}] ({c*.85:.2f},{y0}) rectangle ({c*.85+.85:.2f},{y0+.85});'
for nm,(per,grp) in POS1.items():
    y0={2:.95,3:.1}[per]; g+=f'\\node[font=\\bfseries] at ({(grp-1)*.85+.42:.2f},{y0+.42:.2f}) {{{nm}}};'
g+='\\draw[fill=vurgu!35] (0,-.75) rectangle (.3,-.45); \\node[right,font=\\footnotesize] at (.35,-.6) {Metal}; \\draw[fill=black!25] (1.9,-.75) rectangle (2.2,-.45); \\node[right,font=\\footnotesize] at (2.25,-.6) {Yarı metal}; \\draw[fill=white] (4.3,-.75) rectangle (4.6,-.45); \\node[right,font=\\footnotesize] at (4.65,-.6) {Ametal};'
SK1=tk(g)
dg=('Y yarı metaldir; elektrik iletkenliği metallerle ametaller arasındadır.','şekilde Y yarı metal bölgesindedir; yarı metaller yarı iletkendir')
yl=[('Z metaldir ve tel ya da levha hâline getirilebilir.','Z ametal bölgesindedir; ametaller genellikle kırılgandır, işlenemez'),
    ('X ametaldir; bileşiklerinde elektron almaya yatkındır.','X metal bölgesindedir; metaller elektron vermeye yatkındır'),
    ('T yarı metaldir; ısıyı ve elektriği hiç iletmez.','T metal bölgesindedir; metaller ısıyı ve elektriği iyi iletir'),
    ('Z yarı metaldir; yarı iletken özelliği gösterir.','Z ametal bölgesindedir, yarı metal değildir')]
r=tek_t(dg,yl,0,True)
q('0001',ad=[A('Bölgeleri oku','Şekildeki renklere göre her elementin sınıfı belirlenir.','X, T: metal; Y: yarı metal; Z: ametal'),A('Özellikleri eşleştir','Metaller iyi iletken, ametaller kötü iletken, yarı metaller yarı iletkendir.','Y: yarı iletken'),A('Yargıları sına','Her yargı bu bilgilerle karşılaştırılır.','Doğru yargı: yarı metal Y')],
 alt='Elementlerin Sınıfları',z='kolay',kaz='Periyodik sistemdeki konumdan elementin metal, yarı metal ya da ametal olduğunu ve özelliklerini belirler.',kalip='şekilli',ne='metal, yarı metal, ametal bölgeleri ve X, Y, Z, T',
 metin='Şekilde periyodik sistemin 2. ve 3. periyotlarındaki elementler metal, yarı metal ve ametal olarak renklendirilmiştir; X, Y, Z ve T elementlerinin yerleri harflerle gösterilmiştir (harfler gerçek element sembolü değildir).\nBuna göre aşağıdakilerden hangisi doğrudur?',
 sekil=SK1,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargı.',
 ip=['Her harfin hangi renkli bölgede olduğuna bak.'],
 bilgi=[B('Elementlerin sınıfları','Metaller parlak, işlenebilir ve iyi iletkendir; ametaller genellikle kırılgan ve kötü iletkendir; yarı metaller iletkenlik bakımından bu ikisinin arasındadır')],
 puf='Önce renklere göre her elementin sınıfını belirle.')

# ============================================================ 02 · A grubu adları tablosu (kolay, tablo, olumsuz)
GT=[('1A','Alkali metaller','1','Li'),('2A','Toprak alkali metaller','2','Na'),('5A','Azot grubu','5','P'),('7A','Halojenler','7','Cl'),('8A','Soy gazlar','8','Ne')]
SK2=tablo_svg(['Grup','Grup adı','Değerlik elektronu','Örnek element'],[list(t) for t in GT])
grp_ok={'Li':'1A','Na':'1A','P':'5A','Cl':'7A','Ne':'8A'}
yanlis=[a for a,b,c,e in GT if grp_ok[e]!=a]; assert yanlis==['2A']
dg=('Toprak alkali metaller','Na elementi 1A grubundadır (11 elektronlu, dizilimi 2, 8, 1); 2A grubuna ait örnek Mg gibi bir elementtir')
yl=[('Alkali metaller','Li 1A grubundadır, değerlik elektron sayısı 1’dir; satır doğrudur'),('Azot grubu','P 5A grubundadır (2, 8, 5), değerlik elektron sayısı 5’tir; satır doğrudur'),('Halojenler','Cl 7A grubundadır (2, 8, 7); satır doğrudur'),('Soy gazlar','Ne 8A grubundadır (2, 8); satır doğrudur')]
r=tek_t(dg,yl,2,False)
q('0002',ad=[A('Tabloyu incele','Her satırda grup, ad, değerlik elektronu ve örnek element vardır.','5 satır'),A('Örnekleri sına','Örnek elementin elektron diziliminden grubu bulunur.','Li: 1; Na: 1; P: 5; Cl: 7; Ne: 8'),A('Satırı belirle','Grubuyla uyuşmayan örneğin satırı yanlıştır.','Na ≠ 2A')],
 alt='Elementlerin Sınıfları',z='kolay',kaz='A grubu adlarını ve örnek elementlerin gruplarını eşleştirir.',kalip='tablo',ne='beş A grubu satırı',
 metin='Bir öğrenci, periyodik sistemin beş A grubuna ait grup adlarını, değerlik elektron sayılarını ve birer örnek elementi tabloda göstermiştir (atom numaraları: Li: 3, Na: 11, P: 15, Cl: 17, Ne: 10). Tabloda yalnız bir satırdaki bilgi yanlıştır.\nBuna göre hangi grup için yazılan bilgi yanlıştır?',
 sekil=SK2,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Bilgisi yanlış olan grup.',
 ip=['Örnek elementlerin elektron dizilimini yazıp grubunu bul.'],
 bilgi=[B('Grup adları','A grubu numarası değerlik elektron sayısını verir. Örnek: 6A grubundaki bir elementin dış katmanında 6 elektron bulunur')],
 puf='Örnek elementin dizilimindeki son katman elektronu grup numarasını verir.')

# ============================================================ 03 · 3. periyot elektronegatifliği (orta, grafik)
EN3=[('Na',0.9),('Mg',1.3),('Al',1.6),('Si',1.9),('P',2.2),('S',2.6),('Cl',3.2)]
Sy3=1.05; Sx3=.9
g=eksen(len(EN3)+.2,3.5,Sx3,Sy3,[],[0,1,2,3],'','Elektronegatiflik',xtik=False)
for i,(nm,v) in enumerate(EN3):
    x=.7+i*Sx3
    g+=f'\\draw[fill=vurgu!30,thick] ({x-.3:.2f},0) rectangle ({x+.3:.2f},{v*Sy3:.3f}); \\node[font=\\small\\bfseries] at ({x:.2f},-.35) {{{nm}}}; \\node[above,font=\\footnotesize] at ({x:.2f},{v*Sy3:.3f}) {{{str(v).replace(".","{,}")}}};'
SK3=tk(g)
dg=('Na ile Mg arasındaki elektronegatiflik farkı, S ile Cl arasındakinden küçüktür.','grafiğe göre Na–Mg farkı 1,3 − 0,9 = 0,4; S–Cl farkı 3,2 − 2,6 = 0,6’dır')
yl=[('Cl, bu periyotta en düşük elektronegatifliğe sahip olduğundan elektronu en kolay verir.','Cl en yüksek elektronegatifliğe sahiptir; elektron vermeye değil, almaya yatkındır'),
    ('Elektronegatifliğin artmasıyla elementlerin metalik karakteri de artar.','elektronegatiflik arttıkça ametalik karakter artar, metalik karakter azalır'),
    ('Al ile Si arasındaki elektronegatiflik farkı, Mg ile Al arasındakinden büyüktür.','grafikte Al–Si farkı 1,9 − 1,6 = 0,3; Mg–Al farkı 1,6 − 1,3 = 0,3’tür; eşittir, büyük değildir'),
    ('P’nin elektronegatifliği Si’ninkinden küçüktür.','grafiğe göre P (2,2), Si’den (1,9) büyüktür')]
r=tek_t(dg,yl,3,True)
q('0003',ad=[A('Grafiği oku','Her çubuğun üzerindeki değer elektronegatifliktir.','Na 0,9 → Cl 3,2: artıyor'),A('Farkları hesapla','İki elementin değerleri çıkarılır.','Na–Mg: 0,4; S–Cl: 0,6'),A('Yargıları sına','Her yargı grafikteki değerler ve bu farklarla karşılaştırılır.','Doğru yargı: 0,4 < 0,6')],
 alt='Elektronegatiflik',z='orta',kaz='Periyotta elektronegatiflik grafiğini atom yarıçapı ve metalik karakterle ilişkilendirir.',kalip='grafik',ne='3. periyot elementlerinin elektronegatiflik grafiği',
 metin='3. periyotta yer alan ve soy gaz olmayan elementlerin elektronegatiflik değerleri grafikte verilmiştir.\nBuna göre aşağıdakilerden hangisi doğrudur?',
 sekil=SK3,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargı.',
 ip=['Her seçenekte grafiğe mi, bir kurala mı bakman gerektiğini ayır.'],
 bilgi=[B('Elektronegatiflik','Elektronegatiflik, bir atomun bağ elektronlarını çekme eğilimidir. Aynı grupta yukarı çıkıldıkça artar. Örnek: 2. periyotta F’nin elektronegatifliği Li’ninkinden büyüktür')],
 puf='Değer karşılaştıran yargıları grafikten, eğilim yargılarını periyodik kuraldan değerlendir.')

# ============================================================ 04 · uzun tablo kesiti (orta, öncüllü, şekil)
CW=.46
def hucre(per,col): return (col-1)*CW,(4-per)*CW
g=''
for per in (1,2,3,4):
    g+=f'\\node[font=\\footnotesize,anchor=east] at (-.1,{(4-per)*CW+CW/2:.2f}) {{{per}}};'
    for col in range(1,19):
        if per==1 and col not in (1,18): continue
        if per in (2,3) and col in range(3,13): continue
        x,y=hucre(per,col); g+=f'\\draw ({x:.2f},{y:.2f}) rectangle ({x+CW:.2f},{y+CW:.2f});'
for lab,col in (('1A',1),('2A',2),('3A',13),('4A',14),('5A',15),('6A',16),('7A',17),('8A',18)):
    g+=f'\\node[font=\\scriptsize] at ({(col-1)*CW+CW/2:.2f},{4*CW+.18:.2f}) {{{lab}}};'
g+=f'\\node[font=\\footnotesize,anchor=east] at (-.1,{4*CW+.18:.2f}) {{periyot}};'
POS4={'X':(4,2),'Y':(4,8),'Z':(3,17),'T':(4,18)}
for nm,(per,col) in POS4.items():
    x,y=hucre(per,col); g+=f'\\node[font=\\footnotesize\\bfseries] at ({x+CW/2:.2f},{y+CW/2:.2f}) {{{nm}}};'
SK4=tk(g)
d={'I':(True,'Y, 4. periyotta ve 3. ile 12. sütunlar arasındadır; bunlar B grubu (geçiş) elementleridir'),
   'II':(False,'X 2A grubunda, Z ise 7A grubundadır; aynı grupta değillerdir'),
   'III':(True,'T, 4. periyodun son elementi olan soy gazdır (8A)')}
r=onc_t(d,4)
q('0004',ad=[A('Konumları oku','Üstteki grup etiketlerine ve periyot numaralarına bakılır.','X: 4. per., 2A; Y: 4. per., B grubu; Z: 3. per., 7A; T: 4. per., 8A'),adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),A('Sonucu yaz','Doğru olan öncüller bir arada yazılır.',oy(d)+' · Sonuç: '+r['dogru'])],
 alt='Tabloda Konum',z='orta',kaz='Uzun periyodik sistem kesitinden elementlerin periyot, grup ve sınıfını belirler.',kalip='öncüllü',ne='4 periyotluk kesitte X, Y, Z, T',
 metin='Şekilde periyodik sistemin ilk dört periyodunu gösteren bir kesitte X, Y, Z ve T elementlerinin yerleri işaretlenmiştir (harfler gerçek element sembolü değildir). A grubu numaraları üstte verilmiştir.\nI. Y bir geçiş (B grubu) elementidir.\nII. X ve Z aynı gruptadır.\nIII. T bir soy gazdır.\nBuna göre hangileri doğrudur?',
 sekil=SK4,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan öncüller.',
 ip=['Her elementin sütununu üstteki A grubu etiketleriyle karşılaştır.'],
 bilgi=[B('Uzun periyodik tablo','1A ve 2A gruplarının yanında, 4. periyottan başlayarak B grubu (geçiş) elementleri bulunur. Her periyot bir soy gazla biter. Örnek: 2. periyot Ne ile biter')],
 puf='Etiketsiz sütunların B grubuna ait olduğunu unutma; her periyodun son sütunu soy gazdır.')

# ============================================================ 05 · alkali metallerin suyla tepkimesi (orta, hikâyeli)
dg=('Aynı grupta yukarıdan aşağı inildikçe atom yarıçapı artar ve iyonlaşma enerjisi azalır; değerlik elektronu daha kolay verilir.','K, Na’dan büyük yarıçaplıdır; dış elektron çekirdekten uzak, zayıf bağlıdır ve kolay kaybedilir')
yl=[('Aynı grupta yukarıdan aşağı inildikçe atom yarıçapı azalır ve elektronlar çekirdeğe daha sıkı bağlanır.','aşağı doğru katman sayısı artar; yarıçap artar, elektron zayıf bağlıdır'),
    ('K’nin değerlik elektron sayısı, Li ve Na’nınkinden fazla olduğu için elektron vermesi kolaydır.','Li, Na ve K’nin üçü de 1A’dadır; değerlik elektron sayıları 1’dir'),
    ('Aynı grupta aşağı inildikçe elektronegatiflik artar; bu yüzden K elektronu daha kolay verir.','aşağı inildikçe elektronegatiflik azalır, bu yüzden elektron verme eğilimi artar'),
    ('Li’nin atom yarıçapı K’ninkinden büyüktür; bu yüzden Li elektronunu daha kolay verir.','Li küçüktür, elektronunu daha zor verir; yarıçap Li < Na < K’dır')]
r=tek_t(dg,yl,4,True)
q('0005',ad=[A('Gözlemi yorumla','Tepkime hızı K > Na > Li sırasıdır; hızlı tepkime kolay elektron verme demektir.','Elektron verme: K > Na > Li'),A('Grup eğilimini bul','Aşağı inildikçe yarıçap artar, çekirdeğin dış elektronu tutması zayıflar.','Yarıçap ↑, iyonlaşma enerjisi ↓'),A('Yargıları sına','Her açıklama bu eğilimle karşılaştırılır.','Doğru açıklama: yarıçap artar, enerji azalır')],
 alt='Metalik Karakter',z='orta',kaz='Aynı gruptaki elementlerin tepkimeye girme eğilimini yarıçap ve iyonlaşma enerjisiyle açıklar.',kalip='hikâyeli',ne='Li, Na, K’nin suyla tepkime hızı',
 metin='Kimya laboratuvarında Cenk, eşit kütleli Li, Na ve K parçalarını ayrı ayrı su dolu kaplara atıyor. Tepkimenin K’de en hızlı, Li’de en yavaş gerçekleştiğini gözlemliyor. Bu üç element periyodik sistemin 1A grubunda yer alır.\nBuna göre Cenk’in gözlemini açıklayan aşağıdakilerden hangisi doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Gözlemi açıklayan doğru ifade.',
 ip=['Aşağı doğru inildikçe atomun yarıçapının ve elektronu tutuşun nasıl değiştiğini düşün.'],
 bilgi=[B('Grup içi eğilimler','Aynı grupta yukarıdan aşağı inildikçe katman sayısı artar. Katman sayısı, çekirdek ile dış elektron arasındaki uzaklığı etkiler. Örnek: 7A grubunda F’den I’a doğru atom yarıçapı büyür')],
 puf='Aşağı doğru katman sayısı ve yarıçap artarken değerlik elektron sayısının aynı kaldığını hatırla.')

# ============================================================ 06 · 1A grubu veri tablosu (orta, öncüllü, tablo)
AK=[('Li','2','152','520'),('Na','3','186','496'),('K','4','227','419')]
SK6=tablo_svg(['Element','Periyot','Atom yarıçapı (pm)','Birinci iyonlaşma enerjisi (kJ/mol)'],[list(t) for t in AK])
d={'I':(True,'Li, Na, K sırasında yarıçap 152, 186, 227 pm olarak artıyor; grupta aşağıdaki Rb’nin yarıçapı K’ninkinden de büyüktür'),
   'II':(True,'iyonlaşma enerjisi 520, 496, 419 kJ/mol olarak azalıyor; Rb’nin enerjisi K’ninkinden de küçüktür'),
   'III':(False,'üç element de 1A grubunda olduğundan hepsinin değerlik elektron sayısı 1’dir; farklı değildir')}
r=onc_t(d,1)
q('0006',ad=[A('Eğilimleri bul','Tablodaki değerlerin grupta aşağı doğru değişimine bakılır.','Yarıçap: 152 → 227 artar; enerji: 520 → 419 azalır'),adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),A('Sonucu yaz','Doğru olan öncüller bir arada yazılır.',oy(d)+' · Sonuç: '+r['dogru'])],
 alt='Grup İçi Eğilimler',z='orta',kaz='Grup içi veri tablosundaki eğilimi, tabloda verilmeyen bir elemente uygular.',kalip='öncüllü',ne='Li, Na, K atom yarıçapı ve iyonlaşma enerjisi tablosu',
 metin='1A grubundaki Li, Na ve K elementlerinin bazı özellikleri tabloda verilmiştir. Aynı grubun 5. periyotta yer alan elementi Rb’dir.\nI. Rb’nin atom yarıçapı 227 pm’den büyüktür.\nII. Rb’nin birinci iyonlaşma enerjisi 419 kJ/mol’den küçüktür.\nIII. Tablodaki elementlerin değerlik elektron sayıları birbirinden farklıdır.\nBuna göre hangileri doğrudur?',
 sekil=SK6,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan öncüller.',
 ip=['Tablodaki sütunların grupta aşağı doğru nasıl değiştiğine bak ve eğilimi bir sonraki elemente uygula.'],
 bilgi=[B('Grupta periyodik eğilim','Aynı grupta aşağı doğru atom yarıçapı artar ve iyonlaşma enerjisi azalır. Değerlik elektron sayısı ise grup içinde değişmez. Örnek: 7A grubunda atom yarıçapı F < Cl < Br sırasındadır')],
 puf='Eğilimi tablodan çıkar; verilmeyen element de aynı eğilimi sürdürür.')

# ============================================================ 07 · izoelektronik iyon yarıçapı (zor, grafik)
IY=[('K','2-',140),('L','-',133),('M','+',102),('T','2+',72)]
Sy7=.025; Sx7=1.1
g=eksen(4.6,160,1,Sy7,[],[0,40,80,120,160],'','İyon yarıçapı (pm)',xtik=False)
for i,(nm,yk_,v) in enumerate(IY):
    x=.9+i*Sx7
    g+=f'\\draw[fill=vurgu!30,thick] ({x-.35:.2f},0) rectangle ({x+.35:.2f},{v*Sy7:.3f}); \\node[font=\\small\\bfseries] at ({x:.2f},-.4) {{{nm}$^{{{yk_}}}$}}; \\node[above,font=\\footnotesize] at ({x:.2f},{v*Sy7:.3f}) {{{v}}};'
SK7=tk(g)
dg=('Atom numaraları K < L < M < T şeklindedir; elektron sayısı eşit olduğundan proton sayısı arttıkça yarıçap küçülür.','10 elektronlu bu iyonlarda yarıçap K’den T’ye küçüldüğüne göre proton sayısı artmaktadır')
yl=[('Atom numaraları T < M < L < K şeklindedir; çünkü proton sayısı arttıkça çekirdeğin çekimi azalır.','proton sayısı arttıkça çekim artar ve yarıçap küçülür'),
    ('K²⁻ ve L⁻ iyonlarının yarıçapları, katman sayıları farklı olduğu için farklıdır.','dört iyon da aynı elektron dizilimine (2, 8) sahiptir; katman sayıları eşittir'),
    ('İyonların yarıçapları arasındaki fark, elektron sayılarının farklı olmasından kaynaklanır.','dört iyonun elektron sayısı eşittir (10); fark proton sayısındadır'),
    ('M⁺ ve T²⁺ iyonlarının yarıçapları, kendi atomlarının yarıçaplarından büyüktür.','katyonlar atomlarından küçüktür; elektron kaybı çekirdek çekimini artırır')]
r=tek_t(dg,yl,0,True)
q('0007',ad=[A('Elektron sayısını bul','Dört iyonun da aynı dizilime sahip olduğu söylenmiştir.','Hepsi 10 elektronlu (2, 8)'),A('Yarıçapı yorumla','Elektron sayısı eşitken yarıçap, proton sayısı arttıkça küçülür.','Yarıçap: K > L > M > T'),A('Atom numarasını sırala','Yarıçap küçüldükçe proton sayısı artar.','Z: K < L < M < T'),A('Yargıları sına','Her yargı bu sonuçla karşılaştırılır.','Doğru yargı: K < L < M < T')],
 alt='İyon Yarıçapı',z='zor',kaz='Elektron sayısı eşit iyonların yarıçap sıralamasından atom numaralarını çıkarır.',kalip='grafik',ne='dört iyonun yarıçap çubuk grafiği',
 metin='K²⁻, L⁻, M⁺ ve T²⁺ iyonlarının elektron dizilimleri aynıdır (2, 8). İyonların yarıçapları grafikte verilmiştir (K, L, M ve T gerçek element sembolü değildir).\nBuna göre aşağıdakilerden hangisi doğrudur?',
 sekil=SK7,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargı.',
 ip=['Elektron sayısı eşit olan iyonlarda yarıçapı değiştiren etkenin ne olduğunu düşün.'],
 bilgi=[B('İyon yarıçapı','Katyon, atomundan küçük; anyon, atomundan büyüktür. Elektron sayıları eşit iyonlarda çekirdek yükü arttıkça elektronlar daha sıkı çekilir. Örnek: Li⁺ iyonunun yarıçapı Li atomununkinden küçüktür')],
 puf='Elektron sayısı eşitse karşılaştırmayı proton sayısına dayandır.')

# ============================================================ 08 · ardışık iyonlaşma enerjileri (zor, tablo)
IE=[('X','496','4562','6910','9544'),('Y','738','1451','7733','10543'),('Z','578','1817','2745','11577')]
SK8=tablo_svg(['Element','İE₁','İE₂','İE₃','İE₄'],[list(t) for t in IE])
dg=('X, Y ve Z aynı periyotta olduğundan atom yarıçapları X > Y > Z’dir; değerlik elektron sayıları sırasıyla 1, 2 ve 3’tür.','İE sıçramaları X’te 1’den sonra, Y’de 2’den sonra, Z’de 3’ten sonradır; aynı periyotta soldan sağa yarıçap azalır')
yl=[('Y’nin değerlik elektron sayısı 3’tür; çünkü İE₃ değeri çok büyüktür.','Y’de büyük sıçrama İE₂’den İE₃’e olmuştur; değerlik elektronu 2’dir'),
    ('X, 2A grubundadır; çünkü İE₂ değeri İE₁’den çok büyüktür.','X’te sıçrama 1. elektrondan sonra olduğundan değerlik elektronu 1’dir, X 1A grubundadır'),
    ('Aynı periyotta olduklarından Z’nin atom yarıçapı X’inkinden büyüktür.','aynı periyotta soldan sağa yarıçap azalır; Z, X’in sağındadır ve daha küçüktür'),
    ('Z’nin değerlik elektron sayısı 4’tür; çünkü tabloda dört değer verilmiştir.','Z’de büyük sıçrama İE₃’ten İE₄’e olduğundan değerlik elektronu 3’tür')]
r=tek_t(dg,yl,1,True)
q('0008',ad=[A('Sıçramaları bul','Ardışık enerjiler arasındaki en büyük artışa bakılır.','X: 1→2; Y: 2→3; Z: 3→4'),A('Grupları belirle','Sıçramadan önceki elektron sayısı değerlik elektron sayısıdır.','X: 1A; Y: 2A; Z: 3A'),A('Yarıçapı karşılaştır','Aynı periyotta soldan sağa atom yarıçapı azalır.','X > Y > Z'),A('Yargıları sına','Her yargı bulunan sonuçlarla karşılaştırılır.','Doğru yargı: 1, 2, 3 ve X > Y > Z')],
 alt='İyonlaşma Enerjisi',z='zor',kaz='Ardışık iyonlaşma enerjilerinden grubu bulup periyodik eğilimle birleştirir.',kalip='tablo',ne='X, Y, Z’nin ardışık iyonlaşma enerjileri',
 metin='Aynı periyotta bulunan X, Y ve Z elementlerinin ardışık iyonlaşma enerjileri (kJ/mol) tabloda verilmiştir (harfler gerçek element sembolü değildir).\nBuna göre aşağıdakilerden hangisi doğrudur?',
 sekil=SK8,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargı.',
 ip=['Her elementte iyonlaşma enerjisinin hangi basamaktan sonra birden sıçradığına bak.'],
 bilgi=[B('Ardışık iyonlaşma enerjisi','Bir atomdan elektronlar sırayla koparılırken her elektron için gereken enerji artar. Değerlik elektronları bittiğinde, iç katmandan elektron koparmak için gereken enerji aniden çok büyür. Örnek: 3 değerlik elektronlu bir elementte büyük sıçrama İE₃’ten İE₄’e olur')],
 puf='Büyük sıçramanın hemen öncesindeki basamak sayısı değerlik elektron sayısını verir.')

# ============================================================ 09 · iyonlardan elementleri bulma (zor, öncüllü, hikâyeli)
E9={'Ca':20,'F':9,'Br':35}
ex=18+2; ey=10-1
assert ex==20 and ey==9
d={'I':(True,'X, 4. periyot 2A’dır; Z (4. periyot 7A) aynı periyotta sağdadır; soldaki X’in atom yarıçapı Z’ninkinden büyüktür'),
   'II':(True,'Y ve Z aynı grupta (7A); aşağıya inildikçe iyonlaşma enerjisi azalır, üstteki Y’nin enerjisi Z’ninkinden büyüktür'),
   'III':(False,'Y ametal (7A), X metaldir (2A); elektronegatifliği büyük olan Y’dir, X değil')}
r=onc_t(d,2)
q('0009',ad=[A('X’i bul','X²⁺ iyonunda 18 elektron vardır; atomun elektronu 18 + 2 = 20’dir.','X: atom numarası 20 → 4. periyot 2A'),A('Y’yi bul','Y⁻ iyonunda 10 elektron vardır; atom 9 elektronludur.','Y: atom numarası 9 → 2. periyot 7A'),A('Z’yi yerleştir','Z, Y ile aynı grupta (7A), X ile aynı periyotta (4.) yer alır.','Z: 4. periyot 7A'),adim_onc(d,['I','II']),adim_onc(d,['III']),A('Sonucu yaz','Doğru olan öncüller bir arada yazılır.',oy(d)+' · Sonuç: '+r['dogru'])],
 alt='Konumdan Element Belirleme',z='zor',kaz='İyon dizilimlerinden elementleri bulup tablodaki konumlarına göre periyodik özellikleri karşılaştırır.',kalip='öncüllü',ne='X²⁺ ve Y⁻ dizilimleri, Z’nin konumu',
 metin='X²⁺ iyonunun elektron dizilimi 2, 8, 8; Y⁻ iyonunun elektron dizilimi 2, 8’dir. Z elementi, Y ile aynı grupta, X ile aynı periyotta yer alır (harfler gerçek element sembolü değildir).\nI. X’in atom yarıçapı Z’ninkinden büyüktür.\nII. Y’nin birinci iyonlaşma enerjisi Z’ninkinden büyüktür.\nIII. X’in elektronegatifliği Y’ninkinden büyüktür.\nBuna göre hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan öncüller.',
 ip=['Önce iyonların elektron sayısından X ve Y’nin atom numaralarını bul.'],
 bilgi=[B('İyondan atoma','Katyonun elektron sayısına yük eklenerek, anyonun elektron sayısından yük çıkarılarak atomun elektron sayısı bulunur. Örnek: Na⁺ iyonunda 10 elektron varsa Na atomunda 11 elektron bulunur')],
 puf='Konumları bulduktan sonra periyot ve grup eğilimlerini ayrı ayrı uygula.')

# ============================================================ 10 · 2×2 komşu elementler (zor, öncüllü, şekil)
g=''
CWd=1.0
for (r_,c_),nm in {(0,0):'X',(0,1):'Y',(1,0):'Z',(1,1):'T'}.items():
    x=c_*CWd; y=(1-r_)*CWd
    g+=f'\\draw[fill=white] ({x},{y}) rectangle ({x+CWd},{y+CWd}); \\node[font=\\bfseries] at ({x+CWd/2},{y+CWd/2}) {{{nm}}};'
g+='\\node[font=\\footnotesize,anchor=east] at (-.1,1.5) {3. periyot}; \\node[font=\\footnotesize,anchor=east] at (-.1,.5) {4. periyot}; \\node[font=\\footnotesize] at (.5,2.2) {1A}; \\node[font=\\footnotesize] at (1.5,2.2) {2A};'
SK10=tk(g)
d={'I':(False,'Z 4. periyotta 1A, Y 3. periyotta 2A’dır; Z hem bir katman fazladır hem de Y’nin solundadır; bu yüzden Z’nin yarıçapı Y’ninkinden büyüktür, küçük değildir'),
   'II':(True,'T, Z’nin hemen sağındadır; aynı periyotta sağa gidildikçe birinci iyonlaşma enerjisi artar, T’ninki Z’ninkinden büyüktür'),
   'III':(True,'Y ve T aynı grupta (2A); T aşağıdadır, katman sayısı fazladır; T²⁺ iyonunun yarıçapı Y²⁺ iyonununkinden büyüktür')}
r=onc_t(d,3)
q('0010',ad=[A('Konumları oku','X ve Y 3. periyotta, Z ve T 4. periyottadır; X, Z 1A; Y, T 2A grubundadır.','X: 3. per. 1A; Y: 3. per. 2A; Z: 4. per. 1A; T: 4. per. 2A'),adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),A('Sonucu yaz','Doğru olan öncüller bir arada yazılır.',oy(d)+' · Sonuç: '+r['dogru'])],
 alt='Tabloda Komşu Elementler',z='zor',kaz='Tabloda yan yana ve alt alta komşu elementlerin atom yarıçapı, iyonlaşma enerjisi ve iyon yarıçapını karşılaştırır.',kalip='öncüllü',ne='2×2 komşu element kesiti',
 metin='Periyodik sistemde yan yana ve alt alta bulunan X, Y, Z ve T elementlerinin yerleri şekilde gösterilmiştir (harfler gerçek element sembolü değildir).\nI. Z’nin atom yarıçapı Y’ninkinden küçüktür.\nII. T’nin birinci iyonlaşma enerjisi Z’ninkinden büyüktür.\nIII. T²⁺ iyonunun yarıçapı Y²⁺ iyonununkinden büyüktür.\nBuna göre hangileri doğrudur?',
 sekil=SK10,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan öncüller.',
 ip=['Her öncülde karşılaştırılan iki elementin aynı grupta mı, aynı periyotta mı olduğunu belirle.'],
 bilgi=[B('Periyodik eğilimler','Aynı periyotta sağa gidildikçe atom yarıçapı azalır, iyonlaşma enerjisi artar. Aynı grupta aşağı inildikçe atom yarıçapı artar, iyonlaşma enerjisi azalır. Örnek: 2. periyotta N’nin atom yarıçapı O’nunkinden büyüktür')],
 puf='Her karşılaştırmada önce iki elementin tablodaki konum ilişkisini belirle.')

bitir(P,'periyodikuc',UK)
