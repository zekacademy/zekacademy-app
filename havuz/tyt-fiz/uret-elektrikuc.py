"""TYT Fizik · Elektrik (üçüncü genişletme) · 10 soru.
Kardeş yok, ipucu 1. Devreler circuitikz (tikzpicture içinde, european), grafikler pgfplots; her sayı ve çeldirici değer Python'da assert edilir.
Öncüllü sorularda her öncülün doğruluğu yorumda gerekçelendirilir; yanlış şık metinleri öncül yanılgılarından üretilir."""
import sys,os,math,json
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,GD)
import _hafif as H
from _hafif import *
from cizim import tikz_svg
sys.path.insert(0,os.path.join(HV,'tyt-mat'))
from _hafif_mat import tablo_svg
from math import sin,cos,radians
KONU='Elektrik'; H.KONU=KONU
P=Parti('elektrikuc','Elektrik','fiz|Elektrik',ders='TYT Fizik',idon='tytfiz')
KAYNAK='ÖSYM 2018–2026 TYT Fizik soruları (yalnız mantık) · MEB 9–10. sınıf fizik'
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small,circuitikz/bipoles/length=1.1cm]\n'
TAIL='\n\\end{tikzpicture}'
def tk(body): return tikz_svg(HEAD+body+TAIL)
def nn(no): return f'{int(no):02d}'
def kartk(no,alt,fikir,tuzak,z,kalip,adim,tipId,tip):
    kart(f'K-FZEL3-{nn(no)}',alt,fikir,tuzak,z,kalip,adim,tipId,tip,KAYNAK)

# ---------- sayısal soru ----------
def N(no,tipId,tip,alt,z,kaz,fikir,tuzak,metin,dogru,yan,istenen,ip,bilgi,ad,puf,sekil=None,kalip=None,sira=None):
    kalip=kalip or ('şekilli' if sekil else 'düz')
    kartk(no,alt,fikir,tuzak,z,kalip,len(ad),tipId,tip)
    mk(P,no,metin=metin,dogru=dogru,yan=yan,istenen=istenen,ad=ad,sekil=sekil,ip=ip,bilgi=bilgi,puf=puf,tipId=tipId,tip=tip,z=z,alt=alt,kaz=kaz,
       kalip=kalip,adim=len(ad),kart=f'K-FZEL3-{nn(no)} ({alt}) · yeni kurgu, ÖSYM mantığı',kisa=None,sira=sira)

# ---------- öncüllü soru ----------
ROM=['I','II','III']
def secenek(S):
    S=sorted(S,key=ROM.index)
    return 'Yalnız '+S[0] if len(S)==1 else (' ve '.join(S) if len(S)==2 else 'I, II ve III')
def ayristir(s):
    if s.startswith('Yalnız'): return {s.split()[1]}
    if s=='I, II ve III': return set(ROM)
    return set(s.split(' ve '))
def O(no,tipId,tip,alt,z,kaz,fikir,tuzak,kok,stm,sira,oku,ip,bilgi,puf,sekil=None,son='Buna göre, yukarıdaki yargılardan hangileri doğrudur?',kalip=None):
    """stm: [(yargı, doğru_mu, doğru_gerekçe, yanılgı)] — yanılgı: yargıyı ters değerlendiren öğrencinin düşüncesi."""
    assert len(stm)==3 and len(sira)==5 and len(set(sira))==5
    S={ROM[i] for i,s in enumerate(stm) if s[1]}; dogru=secenek(S); assert dogru in sira,(no,dogru,sira)
    assert all(ayristir(o)!=S for o in sira if o!=dogru)
    def cel(o):
        K=ayristir(o); parts=[]
        for i,(t,v,w,m) in enumerate(stm):
            r=ROM[i]
            if r in K and not v: parts.append(f'{r}. yargıyı doğru sanmış: {m}')
            if r not in K and v: parts.append(f'{r}. yargıyı yanlış sanmış: {m}')
        assert parts,(no,o); return ' '.join(parts)
    yan=[(o,cel(o),'bilgi') for o in sira if o!=dogru]
    metin=kok+'\n'+'\n'.join(f'{ROM[i]}. {s[0]}' for i,s in enumerate(stm))+'\n'+son
    ad=[A('Verileri oku',oku[0],oku[1])]
    for i,(t,v,w,m) in enumerate(stm): ad.append(A(f'{ROM[i]}. yargıyı incele',w,f'{ROM[i]}: '+('doğru' if v else 'yanlış')))
    ad.append(A('Sonucu belirle','Doğru olan yargıları birleştir.',dogru))
    kalip=kalip or ('şekilli' if sekil else 'öncüllü')
    kartk(no,alt,fikir,tuzak,z,kalip,len(ad),tipId,tip)
    mk(P,no,metin=metin,dogru=dogru,yan=yan,istenen='Verilen yargılardan doğru olanlar.',ad=ad,sekil=sekil,sira=sira,ip=ip,bilgi=bilgi,puf=puf,tipId=tipId,tip=tip,z=z,alt=alt,kaz=kaz,
       kalip=kalip,adim=len(ad),kart=f'K-FZEL3-{nn(no)} ({alt}) · yeni kurgu, ÖSYM mantığı')

# ---------- elektrostatik çizim yardımcıları ----------
def elsk(ox,a,top=''):
    """Elektroskop: kutu, saplı topuz ve yapraklar (a = yaprağın düşeyle açısı, derece)."""
    L=.55; px,py=ox,1.0
    s=f'\\draw[thick] ({ox-.8},0) rectangle ({ox+.8},1.7);\n'
    s+=f'\\draw[thick] ({ox},{py}) -- ({ox},2.3); \\draw[thick,fill=gray!25] ({ox},2.55) circle (.25);\n'
    for sg in (-1,1):
        s+=f'\\draw[very thick] ({px},{py}) -- ({px+sg*L*sin(radians(a)):.3f},{py-L*cos(radians(a)):.3f});\n'
    return s
def cubuk(x,y,isaret,w=1.8,h=.38,ad='',ang=0):
    """Yatay çubuk (merkez x,y); isaret '+', '−' ya da ''."""
    s=f'\\begin{{scope}}[rotate around={{{ang}:({x},{y})}}]\\draw[thick,fill=gray!15] ({x-w/2},{y-h/2}) rectangle ({x+w/2},{y+h/2});\n'
    isaret=isaret.replace('−','-')
    if isaret:
        for k in range(3): s+=f'\\node[font=\\footnotesize] at ({x-w/3+k*w/3:.3f},{y}) {{${isaret}$}};\n'
    s+='\\end{scope}\n'
    return s
def kure(x,y,r=.5,et='',fill='gray!15'):
    return f'\\draw[thick,fill={fill}] ({x},{y}) circle ({r});\n'+(f'\\node at ({x},{y}) {{{et}}};\n' if et else '')
def ayak(x,y,r=.5):
    return f'\\draw[thick,fill=gray!40] ({x-.28},{y-r-.35}) rectangle ({x+.28},{y-r});\n\\draw[thick] ({x-.55},{y-r-.35}) -- ({x+.55},{y-r-.35});\n'
def zemin(x,y):
    return f'\\draw ({x},{y}) node[ground]{{}};\n'

# ---- 01 · Lamba kısa devre (anahtar) · öncüllü · kolay ----
# V=12, özdeş R=1. S açık: kol1 (K+L seri) 2R → I_K=I_L=6; kol2 M: I_M=12.  S kapalı: L kısa devre → I_K=12, I_L=0, I_M=12.
V=Fr(12); R=Fr(1)
Ik0=V/(2*R); Im0=V/R; Ik1=V/R; Il1=Fr(0); Im1=V/R
assert (Ik0,Im0,Ik1,Im1)==(6,12,12,12) and Ik1**2*R>Ik0**2*R and Im1==Im0    # I doğru, III yanlış; II doğru (L'den akım geçmez)
sk=('\\draw (0,0) to[battery1] (0,3) -- (2.5,3) to[lamp,l_={$K$}] (2.5,1.5) to[lamp,l_={$L$}] (2.5,0) -- (6,0) -- (0,0);\n'
    '\\draw (2.5,3) -- (6,3) to[lamp,l={$M$}] (6,0);\n'
    '\\draw (2.5,1.5) -- (3.8,1.5) to[spst,l={$S$}] (3.8,0);\n'
    '\\fill (2.5,3) circle (1.7pt) (2.5,1.5) circle (1.7pt) (2.5,0) circle (1.7pt) (3.8,0) circle (1.7pt);')
O('0001','fz-el3-lamba-kisa-devre','Anahtar kapatılınca bir lambanın kısa devre olması','Anahtar açma ve kapama','kolay',
 'Bir lambaya paralel bağlı anahtar kapatıldığında lambaların parlaklık değişimini, kısa devre ve paralel kol gerilimi kavramlarıyla yorumlar.',
 'Anahtar kapanınca L lambası kısa devre olur: akım anahtardan geçer. Kolun direnci azalacağından K’nin akımı artar; ideal üretecin uçlarına paralel bağlı M’nin gerilimi ve akımı ise değişmez.',
 'Kısa devre olan lambanın da yandığını sanmak; ideal üretece paralel kolun parlaklığının değiştiğini düşünmek.',
 'Şekildeki devrede K, L ve M lambaları özdeştir; lambaların dirençleri sabittir. Üreteç idealdir ve bağlantı telleri ihmal edilmektedir. S anahtarı açıkken devre dengeye ulaşmıştır. Öğrenci S anahtarını kapatıyor ve devre yeniden dengeye ulaşıyor.',
 [('K lambasının parlaklığı artar.',True,'Anahtar kapanınca L, kısa devre olur ve K’nin bulunduğu kolun direnci yarıya düşer; kolun gerilimi aynı kaldığından K’nin akımı ve parlaklığı artar.','Kısa devrenin K’nin akımını etkilemeyeceğini düşünmüş.'),
  ('L lambasından akım geçmez.',True,'Anahtar L’ye paralel olduğundan L’nin iki ucu aynı noktaya bağlanır; akım dirençsiz yoldan, yani anahtardan geçer.','Kapalı anahtarın L’yi daha parlak yaptığını sanmış.'),
  ('M lambasının parlaklığı artar.',False,'M, ideal üretecin uçlarına doğrudan bağlıdır; gerilimi de akımı da değişmez, parlaklığı aynı kalır.','Kısa devrenin devredeki bütün lambaları etkilediğini düşünmüş.')],
 ['Yalnız I','Yalnız II','I ve II','I ve III','II ve III'],
 ('K ve L aynı kolda seri; S yalnız L’ye paralel.','S kapalı → L kısa devre'),
 ['Anahtar kapandığında akımın L’den mi anahtardan mı geçeceğini düşün; ardından her kolun direncindeki değişime bak.'],
 [B('Kısa devre','bir elemanın uçları direnci ihmal edilen bir iletkenle birleştirilirse akım yalnızca bu iletkenden geçer, eleman çalışmaz. Örnek: pile bağlı bir lambanın uçlarına tel dokundurulursa lamba söner'),
  B('Lamba parlaklığı','lambanın parlaklığı üzerindeki güçle belirlenir; akım arttıkça parlaklık artar')],
 'Kısa devre yapılan eleman devre dışı kalır; geri kalan kolun toplam direnci düştüğü için o koldaki akım artar.',sekil=tk(sk))

# ---- 02 · Ampermetre ve voltmetre okumalarından kol akımı · sayısal · orta ----
R1,R2,R3=2,6,3; Vr=6
I=Fr(Vr,R1); Req=Fr(R2*R3,R2+R3); Vp=I*Req; I2=Vp/R2; I3=Vp/R3
assert (I,Req,Vp,I2,I3)==(3,2,6,1,2) and I2+I3==I
w1=I/2; assert w1==Fr(3,2)          # akımı iki kola eşit bölmüş
w2=I*R2/(R2+R3)*1; assert w2==2 and w2==I3   # ters oran = diğer kolun akımı
sk=('\\draw (0,0) to[battery1] (0,3) -- (0.5,3) to[R,l_={$R_1=2\\,\\Omega$}] (3,3);\n'
    '\\node[draw,circle,minimum size=.72cm,inner sep=0pt] (V) at (1.75,4.6) {V};\n'
    '\\draw (0.5,3) |- (V.west); \\draw (3,3) |- (V.east); \\fill (0.5,3) circle (1.7pt); \\node[above=.05cm of V] {$6$ V};\n'
    '\\draw (3,3) -- (7.4,3);\n'
    '\\draw (4.4,3) to[R,l_={$R_2=6\\,\\Omega$}] (4.4,1.6); \\node[draw,circle,minimum size=.72cm,inner sep=0pt] (A) at (4.4,.9) {A}; \\draw (4.4,1.6) -- (A.north); \\draw (A.south) -- (4.4,0);\n'
    '\\draw (7.4,3) to[R,l={$R_3=3\\,\\Omega$}] (7.4,0);\n'
    '\\draw (0,0) -- (7.4,0); \\fill (3,3) circle (1.7pt) (4.4,3) circle (1.7pt) (4.4,0) circle (1.7pt);')
N('0002','fz-el3-akim-bolunme','Voltmetre okumasından ana akım ve paralel koldaki ampermetre okuması','Ampermetre ve voltmetre','orta',
 'Voltmetre okumasından ana kol akımını bulur, akımın paralel kollara dirençleriyle ters orantılı paylaşıldığını kullanarak ampermetre okumasını hesaplar.',
 'Voltmetreden R₁ üzerindeki gerilimle devre akımı bulunur; paralel kolların gerilimi ortaktır, akım dirençle ters orantılı bölünür ve ampermetre yalnız bir koldan geçen akımı gösterir.',
 'Ampermetreyi ana kolda sanmak; akımı iki kola eşit bölmek; akım bölme oranını ters kurmak.',
 'Şekildeki devrede üreteç, ampermetre ve voltmetre idealdir; bağlantı telleri ihmal edilmektedir. Voltmetre R₁ direncinin uçlarına bağlıdır, gösterdiği değer şekilde verilmiştir ve devre dengeye ulaşmıştır.\nBuna göre, ampermetre kaç A’i gösterir?',
 1,[(Fr(3,2),'Ana kol akımını (3 A) iki paralel kola eşit bölmüş: 3 ÷ 2 = 1,5 A.','bilgi'),
    (2,'Akım bölme oranını ters kurmuş (daha büyük direncin koluna daha çok akım vermiş): 3 × 6 ÷ 9 = 2 A; bu değer R₃ kolunun akımıdır.','bilgi'),
    (3,'Ampermetrenin ana koldaki akımı gösterdiğini sanmış; yalnız R₁’in akımını (6 ÷ 2 = 3 A) yazmış.','dikkat'),
    (6,'Voltmetrenin gösterdiği 6 değerini ampermetre okuması sanmış; gerilimle akımı karıştırmış.','dikkat')],
 'Ampermetrenin gösterdiği akım (A).',
 ['R₁’den geçen akım ana koldan geçen akımdır; bu akım paralel kollara nasıl paylaşılır?'],
 [B('Paralel bağlama','paralel kolların uçları arasındaki gerilim aynıdır; akım dirençle ters orantılı paylaşılır. Örnek: 2 Ω ve 4 Ω’luk kollarda 4 Ω’luk koldan geçen akım, 2 Ω’luk koldakinin yarısıdır'),
  B('Ampermetre','bulunduğu koldan geçen akımı gösterir; devreye seri bağlanır')],
 [A('Ana kol akımını bul','Voltmetre R₁’in gerilimini gösterir; Ohm yasası.','I = 6 ÷ 2 = 3 A'),
  A('Paralel kolların gerilimini bul','Paralel kolların eşdeğer direnci ile ana akım çarpılır.','R_p = 6 × 3 ÷ 9 = 2 Ω · V_p = 3 × 2 = 6 V'),
  A('Ampermetre okumasını bul','Ampermetre R₂ kolundadır; kol gerilimi 6 V.','I₂ = 6 ÷ 6 = 1 A'),
  A('Kontrol et','Kol akımları toplamı ana akıma eşit olmalı.','1 + 6 ÷ 3 = 1 + 2 = 3 A')],
 'Önce ana kol akımını bul; paralel bölgede gerilim ortak, akım dirençle ters orantılıdır.',sekil=tk(sk))

# ---- 03 · Voltmetrenin yanlış (seri) bağlanması · öncüllü · kolay ----
# İdeal voltmetre: sonsuz direnç → devrede akım yok; lamba ışık vermez; voltmetre üretecin gerilimini gösterir. İdeal ampermetre (0 Ω) olsaydı lamba yanardı.
eps=Fr(6); RL=Fr(3); Rv=10**9
I_v=eps/(RL+Rv); assert I_v<Fr(1,10**8) and eps-I_v*RL>Fr(599,100)   # akım ≈ 0, voltmetre ≈ ε
I_a=eps/(RL+0); assert I_a==2
sk=('\\draw (0,0) to[battery1,l_={$6$ V}] (0,3) -- (1.3,3) to[lamp,l={$L$}] (4.0,3) -- (5.3,3);\n'
    '\\node[draw,circle,minimum size=.72cm,inner sep=0pt] (V) at (5.3,1.5) {V}; \\draw (5.3,3) -- (V.north); \\draw (V.south) -- (5.3,0) -- (0,0);')
O('0003','fz-el3-voltmetre-seri','Voltmetrenin lambaya seri bağlanması','Ampermetre ve voltmetre','kolay',
 'Voltmetrenin devreye yanlış (seri) bağlanmasının devre akımına, lamba ışığına ve voltmetre okumasına etkisini yorumlar.',
 'İdeal voltmetrenin direnci çok büyüktür; seri bağlanırsa devre akımı hemen hemen sıfır olur, lamba ışık vermez ve üretecin gerilimi voltmetre üzerinde ölçülür.',
 'Voltmetreyi her bağlantıda lambanın gerilimini ölçen alet saymak; seri bağlı voltmetreden akım geçeceğini düşünmek.',
 'Şekildeki devrede üreteç ve bağlantı telleri idealdir. Bir öğrenci, lambanın gerilimini ölçmek için voltmetreyi lambaya paralel yerine şekildeki gibi seri bağlamıştır. Voltmetrenin iç direnci, lambanın direncinin çok çok katıdır (ideal voltmetre).',
 [('Lamba ışık vermez.',True,'Voltmetrenin direnci çok büyük olduğundan devreden hemen hemen hiç akım geçmez; lamba çok az akımla ışık veremez.','Seri bağlı voltmetreden de lamba yanacak kadar akım geçeceğini düşünmüş.'),
  ('Voltmetre üretecin gerilimini gösterir.',True,'Akım ihmal edilecek kadar küçük olduğundan lambanın uçları arasında gerilim düşmez; üretecin gerilimi neredeyse tamamen voltmetrenin uçlarında görülür.','Voltmetrenin yalnız lambanın gerilimini (sıfıra yakın) gösterdiğini sanmış.'),
  ('Voltmetre yerine ideal ampermetre bağlansaydı lamba ışık verirdi.',True,'İdeal ampermetrenin direnci sıfırdır; seri bağlandığında devre tamamlanır, lambadan akım geçer.','Ampermetrenin de devreyi kestiğini düşünmüş.')],
 ['Yalnız I','I ve II','I ve III','II ve III','I, II ve III'],
 ('Voltmetre lambayla seri; ideal voltmetrenin direnci çok büyük.','Seri bağlı V → akım ≈ 0'),
 ['Seri devrede toplam direnç büyüdükçe devre akımına ne olur? Voltmetrenin direnci lambanınkinden çok büyük.'],
 [B('Voltmetre','ölçülecek elemana paralel bağlanır; iç direnci çok büyüktür, bu yüzden devreden neredeyse akım çekmez'),
  B('Ampermetre','devreye seri bağlanır; iç direnci çok küçüktür (ideal ampermetrede sıfır), akıma engel olmaz')],
 'Voltmetre paralel, ampermetre seri bağlanır; ters bağlanan voltmetre devreyi neredeyse açık devre yapar.',sekil=tk(sk))

# ---- 04 · Eşdeğer direnç: iki direncin aynı iki düğüm arasında olması · sayısal · orta ----
Ra,Rb,Rc=3,12,4
Rp=Fr(Rb*Rc,Rb+Rc); Re=Ra+Rp
assert (Rp,Re)==(3,6)
assert Ra+Rc==7 and Ra+Rb==15 and Ra+Rb+Rc==19 and Fr(1)/(Fr(1,Ra)+Fr(1,Rb)+Fr(1,Rc))==Fr(3,2)
sk=('\\draw (0,2) to[R,l={$3\\,\\Omega$}] (3,2) to[R,l={$12\\,\\Omega$}] (6,2) -- (6,0);\n'
    '\\draw (3,2) to[R,l_={$4\\,\\Omega$}] (3,0) -- (8,0);\n'
    '\\fill (3,2) circle (1.7pt) (6,0) circle (1.7pt); \\fill[white] (0,2) circle (2.4pt); \\draw (0,2) circle (2.4pt); \\fill[white] (8,0) circle (2.4pt); \\draw (8,0) circle (2.4pt);\n'
    '\\node[above] at (0,2.15) {$A$}; \\node[right] at (8.2,0) {$B$};')
N('0004','fz-el3-esdeger-tel','Aynı iki düğüm arasında kalan dirençlerin eşdeğeri','Eşdeğer direnç','orta',
 'Şekildeki bağlantı tellerinin hangi noktaları birleştirdiğini izleyerek paralel kalan dirençleri bulur ve A–B arasındaki eşdeğer direnci hesaplar.',
 'Bağlantı telinin birleştirdiği noktalar aynı düğümdür; 12 Ω ve 4 Ω’luk dirençlerin iki ucu da aynı düğümlere bağlı olduğundan paraleldir ve 3 Ω ile seri toplanır.',
 'Dirençlerin hepsini seri toplamak; teli yok sayıp bir direncin akım taşımadığını sanmak; hepsini paralel almak.',
 'Şekilde dirençler, bağlantı telleri ve A, B uçları görülmektedir. Bağlantı telleri idealdir.\nBuna göre, A ve B uçları arasındaki eşdeğer direnç kaç Ω’dur?',
 6,[(Fr(3,2),'Üç direncin üçünü de paralel bağlı saymış: 1/R = 1/3 + 1/12 + 1/4 → R = 1,5 Ω.','bilgi'),
    (7,'Teli yok sayarak 12 Ω’luk direncin ucunun boşta kaldığını, ondan akım geçmediğini düşünmüş: 3 + 4 = 7 Ω.','dikkat'),
    (15,'Tel 4 Ω’luk direnci kısa devre ediyor sanmış: 3 + 12 = 15 Ω.','dikkat'),
    (19,'Dirençleri yalnızca yan yana görüp hepsini seri toplamış: 3 + 12 + 4 = 19 Ω.','bilgi')],
 'A ile B arasındaki eşdeğer direnç (Ω).',
 ['Bağlantı telinin hangi noktaları aynı düğüm yaptığını bul; 12 Ω ve 4 Ω’luk dirençlerin uçlarını izle.'],
 [B('Eşdeğer direnç','iki ucu da aynı düğümlere bağlı dirençler paraleldir; paralel iki direnç R₁·R₂ ÷ (R₁ + R₂) ile bulunur. Örnek: 6 Ω ve 3 Ω paralel bağlanırsa 6·3 ÷ 9 = 2 Ω olur'),
  B('Düğüm','dirençsiz bir tel üzerindeki bütün noktalar aynı potansiyeldedir, tek bir nokta gibi düşünülebilir')],
 [A('Düğümleri belirle','Düşey tel, 12 Ω’luk direncin sağ ucunu alt hatta bağlar; 4 Ω’luk direncin alt ucu da aynı hattadır.','12 Ω ve 4 Ω: ortak iki düğüm arasında'),
  A('Paralel kolu çöz','İki direncin eşdeğeri çarpım bölü toplam.','12 × 4 ÷ 16 = 3 Ω'),
  A('Seri ekle','Bu eşdeğer, A’dan gelen 3 Ω ile seridir.','R_AB = 3 + 3 = 6 Ω')],
 'Bağlantı telleri düğümleri birleştirir; önce hangi dirençlerin aynı iki düğüm arasında kaldığını belirle.',sekil=tk(sk))

# ---- 05 · Lamba parlaklık sıralaması · nitel · zor ----
# K ana kol akımı I; L kolu R, M–N kolu 2R → I_L = 2I/3, I_M = I_N = I/3. P ∝ I²: K=1, L=4/9, M=N=1/9
I0=Fr(1); IL=I0*2/3; IM=I0/3
PK,PL,PM=I0**2,IL**2,IM**2
assert PK>PL>PM and PM==Fr(1,9) and PL==Fr(4,9) and IL+IM==I0
sk=('\\draw (0,0) to[battery1] (0,3) -- (1.2,3) to[lamp,l={$K$}] (3.6,3) -- (4.5,3);\n'
    '\\draw (4.5,3) to[lamp,l_={$L$}] (4.5,0);\n'
    '\\draw (4.5,3) -- (7.5,3) to[lamp,l={$M$}] (7.5,1.5) to[lamp,l={$N$}] (7.5,0);\n'
    '\\draw (0,0) -- (7.5,0); \\fill (4.5,3) circle (1.7pt) (4.5,0) circle (1.7pt);')
N('0005','fz-el3-parlaklik-siralama','Karışık bağlı özdeş lambaların parlaklık sıralaması','Lamba parlaklığı','zor',
 'Ana kol, tek lambalı kol ve iki lambalı seri kolun akımlarını karşılaştırarak özdeş lambaların parlaklık sıralamasını bulur.',
 'Ana koldaki akım, paralel kollara dirençleriyle ters orantılı bölünür: tek lambalı kol 2/3, iki lambalı kol 1/3 pay alır. Parlaklık P = I²R ile akımın karesiyle orantılıdır.',
 'Paralel kollara akımın eşit bölündüğünü sanmak; seri lambalarda akımın azaldığını düşünmek; paralel koldaki lambayı ana koldakinden parlak sanmak.',
 'Şekildeki devrede K, L, M ve N lambaları özdeştir; lambaların dirençleri sabit ve üreteç idealdir. Devre dengeye ulaşmıştır.\nBuna göre, lambaların parlaklıkları arasındaki ilişki aşağıdakilerden hangisidir?',
 'K > L > M = N',[('K > L = M = N','Paralel kollara akımın eşit paylaştığını düşünmüş; L’yi M ve N ile aynı sanmış.','bilgi'),
    ('K = L > M = N','Paralel iki kolun gerilimi eşit olduğundan K ile L’nin aynı parlaklıkta olacağını düşünmüş.','bilgi'),
    ('K > L > M > N','Seri bağlı M ve N’den akımın sırayla azaldığını, ilk lambanın daha parlak olduğunu sanmış.','bilgi'),
    ('L > K > M = N','Ana koldaki akımı bir koldan küçük sanıp K’yi L’den sönük saymış.','bilgi')],
 'Lambaların parlaklık sıralaması.',
 ['Önce ana koldan geçen akıma I de; bu akım L kolu ile M–N kolu arasında dirençlerin oranına göre nasıl paylaşılır?'],
 [B('Akım bölünmesi','paralel kollarda akım dirençle ters orantılı paylaşılır. Örnek: 1 Ω ve 2 Ω’luk kollara giren 6 A, 4 A ve 2 A olarak ayrılır'),
  B('Parlaklık','özdeş lambalarda parlaklık, üzerlerinden geçen akımın karesiyle orantılıdır (P = I²R)')],
 [A('Kol dirençlerini yaz','Lamba direnci R olsun; L kolu R, M–N kolu 2R.','R_L kolu = R · R_MN kolu = 2R'),
  A('Akımı paylaştır','K’den geçen I akımı ters orantılı bölünür.','I_L = 2I/3 · I_M = I_N = I/3'),
  A('Güçleri karşılaştır','Parlaklık akımın karesiyle orantılıdır.','P_K : P_L : P_M = 1 : 4/9 : 1/9'),
  A('Sırala','En parlak K, sonra L; M ile N aynı akımı taşır.','K > L > M = N')],
 'Özdeş lambalarda parlaklığı sıralarken önce kollardaki akımı bul; seri lambaların akımı eşittir.',sekil=tk(sk),
 sira=['K > L = M = N','K = L > M = N','K > L > M > N','L > K > M = N','K > L > M = N'])

# ---- 06 · Sayaç okuması ve kademeli tarife · sayısal · orta ----
o1,o2=12485,12735; tuk=o2-o1; assert tuk==250
ucret=200*2+(tuk-200)*3; assert ucret==550
d1=(tuk-200)*3; d2=tuk*2; d3=200*3+(tuk-200)*2; d4=tuk*3
assert (d1,d2,d3,d4)==(150,500,700,750) and len({ucret,d1,d2,d3,d4})==5
def sayac(x,y,sayi,et):
    s=f'\\node[font=\\small] at ({x+1.4},{y+1.05}) {{{et}}};\n'
    for k,ch in enumerate(f'{sayi:05d}'):
        s+=f'\\node[draw,thick,minimum width=.55cm,minimum height=.85cm,fill=gray!10,font=\\Large] at ({x+k*.6},{y}) {{{ch}}};\n'
    s+=f'\\node[font=\\small] at ({x+3.5},{y}) {{kWh}};\n'
    return s
sk=sayac(0,0,o1,'Önceki ay sonu')+sayac(5.4,0,o2,'Bu ay sonu')
N('0006','fz-el3-sayac-tarife','Elektrik sayacı okumasından kademeli tarifeyle fatura','Elektriksel enerji ve güç','orta',
 'İki sayaç okuması arasındaki farktan tüketilen elektrik enerjisini bulur ve kademeli tarifeye göre ödenecek ücreti hesaplar.',
 'Tüketim, iki sayaç okuması arasındaki farktır; kademeli tarifede her dilimin kWh’si kendi birim fiyatıyla çarpılıp toplanır.',
 'Son okumayı tüketim sanmak; tüm tüketimi tek fiyatla çarpmak; fiyat dilimlerini ters uygulamak.',
 'Bir evin elektrik sayacının önceki ay sonundaki ve bu ay sonundaki okumaları şekilde verilmiştir. Elektrik şirketi, ay boyunca tüketilen enerjinin ilk 200 kWh’si için kWh başına 2 TL, 200 kWh’yi aşan kısmı için kWh başına 3 TL ücret almaktadır. Sabit bedel ve vergi yoktur.\nBuna göre, bu ay için ödenecek elektrik ücreti kaç TL’dir?',
 550,[(150,'Yalnızca 200 kWh’yi aşan 50 kWh’yi 3 TL ile çarpmış; ilk dilimi hesaba katmamış.','dikkat'),
      (500,'Bütün tüketimi (250 kWh) 2 TL ile çarpmış; ikinci fiyat dilimini uygulamamış.','dikkat'),
      (700,'Fiyat dilimlerini ters uygulamış: ilk 200 kWh’ye 3 TL, kalan 50 kWh’ye 2 TL.','bilgi'),
      (750,'Bütün tüketimi (250 kWh) 3 TL ile çarpmış; ilk 200 kWh’nin daha ucuz olduğunu unutmuş.','bilgi')],
 'Ödenecek elektrik ücreti (TL).',
 ['Önce bu ay tüketilen enerjiyi iki okumanın farkından bul, sonra hangi kısmının hangi fiyattan ücretlendirildiğine bak.'],
 [B('Sayaç','elektrik enerjisini kWh cinsinden toplar; belli bir dönemdeki tüketim, son okuma ile ilk okumanın farkıdır. Örnek: 3200 ve 3290 kWh okumaları arasındaki tüketim 90 kWh’tir'),
  B('Kademeli tarife','her dilim kendi birim fiyatıyla ücretlendirilir ve sonuçlar toplanır')],
 [A('Tüketimi bul','Son okumadan ilk okumayı çıkar.','12735 − 12485 = 250 kWh'),
  A('Dilimlere ayır','İlk 200 kWh ve aşan kısım.','200 kWh + 50 kWh'),
  A('Ücretleri hesapla','Her dilim kendi fiyatıyla.','200 × 2 = 400 TL · 50 × 3 = 150 TL'),
  A('Topla','İki dilimin ücreti toplanır.','400 + 150 = 550 TL')],
 'Sayaç okumalarında tüketim farktan bulunur; kademeli tarifede dilimleri ayrı ayrı fiyatla.',sekil=tk(sk))

# ---- 07 · Yüklü ve nötr elektroskopların telle bağlanması · öncüllü · orta ----
# X (+q) ve Y (nötr) özdeş, yalıtkan ayaklı; iletken telle bağlanınca yük paylaşılır (q/2, q/2). I: Y'nin yaprakları açılır (doğru). II: X'in açıklığı azalır (yanlış: "değişmez" denmiş). III: tel kaldırılınca Y'nin yaprakları kapanır (yanlış: yük kalır).
qX,qY=Fr(8),Fr(0); sonra=(qX+qY)/2; assert sonra==4 and qX+qY==2*sonra
sk=(elsk(0,32)+elsk(4.2,0)+'\\draw[thick] (0,2.8) -- (0,3.4) -- (4.2,3.4) -- (4.2,2.8);\n'
    '\\node[font=\\small] at (2.1,3.75) {iletken tel};\n\\node at (0,-.4) {$X$}; \\node at (4.2,-.4) {$Y$};')
O('0007','fz-el3-iki-elektroskop','Yüklü ve nötr iki elektroskopun iletken telle bağlanması','Elektroskop','orta',
 'Özdeş iletken sistemlerin birbirine iletken telle bağlanmasında yükün paylaşılmasını elektroskop yapraklarının davranışıyla yorumlar.',
 'İletken telle bağlanan özdeş iletkenler arasında yük, potansiyeller eşitleninceye kadar geçer ve yarı yarıya paylaşılır; bağlantı kesilirse paylaşılan yükler kendi yerinde kalır.',
 'Yük paylaşımında yüklü cismin açıklığının değişmeyeceğini düşünmek; tel çekilince yükün geri döneceğini sanmak.',
 'Yalıtkan ayaklar üzerinde duran özdeş X ve Y elektroskoplarından X pozitif yüklüdür ve yaprakları açıktır; Y nötrdür ve yaprakları kapalıdır. Elektroskopların topuzları şekildeki gibi iletken bir telle birleştiriliyor ve sistem dengeye ulaşıyor; ardından tel, yalıtkan sapından tutularak kaldırılıyor. Ortamdan yük alışverişi olmamaktadır.',
 [('Y elektroskopunun yaprakları açılır.',True,'Tel üzerinden X’teki pozitif yükün bir kısmı Y’ye geçer; Y’nin yaprakları aynı cins yükle yüklenip birbirini iter ve açılır.','Yükün telden geçmeyeceğini, Y’nin kapalı kalacağını düşünmüş.'),
  ('X elektroskopunun yaprak açıklığı değişmez.',False,'X’in yükünün bir kısmı Y’ye geçtiğinden X’te kalan yük azalır; yapraklar arasındaki itme azalır ve açıklık küçülür.','Yük paylaşıldığında yüklü cismin açıklığının aynı kalacağını sanmış.'),
  ('Tel kaldırıldıktan sonra Y elektroskopunun yaprakları kapanır.',False,'Tel kaldırıldığında Y’de kalan yük yok olmaz; yalıtkan ayak yükün kaçmasını engeller, yaprakları açık kalır.','Telin çekilmesiyle yükün geri X’e döneceğini düşünmüş.')],
 ['Yalnız I','Yalnız II','I ve II','I ve III','II ve III'],
 ('X yüklü, Y nötr; tel iletken, ayaklar yalıtkan.','Toplam yük korunur'),
 ['İletken telin iki elektroskop arasındaki yük dağılımına etkisini düşün; ardından tel kaldırıldığında yüklerin nereye gideceğine bak.'],
 [B('Yük paylaşımı','iletkenler birbirine dokununca ya da iletken telle bağlanınca toplam yük, özdeş cisimler arasında eşit bölüşülür. Örnek: +6q ve nötr özdeş iki küre bağlanınca ikisi de +3q yüklü olur'),
  B('Elektroskop','yaprak açıklığı yük miktarının göstergesidir; aynı işaretli yük arttıkça yapraklar daha çok açılır')],
 'Telle bağlanan özdeş iletkenler yükü eşit paylaşır; bağlantı kesilince yükler olduğu yerde kalır.',sekil=tk(sk))

# ---- 08 · Etiketli lambanın seri dirençle çalıştırılması · sayısal · orta ----
Ve,Pe,eps8=6,18,15
Ie=Fr(Pe,Ve); R8=Fr(eps8-Ve)/Ie; RL8=Fr(Ve*Ve,Pe)
assert (Ie,R8,RL8)==(3,3,2)
y1=RL8; y2=Fr(eps8)/Ie; y3=Fr(eps8+Ve)/Ie; y4=Fr(eps8-Ve)/(Fr(Pe)/eps8)
assert (y1,y2,y3,y4)==(2,5,7,Fr(15,2))
sk=('\\draw (0,0) to[battery1,l_={$15$ V}] (0,3) -- (1.0,3) to[R,l={$R$}] (3.4,3) to[lamp,l={$6$ V – $18$ W}] (6.6,3) -- (7.4,3) -- (7.4,0) -- (0,0);')
N('0008','fz-el3-etiketli-lamba','Etiketli lambanın normal parlaklıkta çalışması için seri direnç','Elektriksel enerji ve güç','orta',
 'Lamba etiketinden normal çalışma akımını bulur; üreteç geriliminin lambada ve dirençte paylaşılmasından seri direnci hesaplar.',
 'Etiketteki gerilim ve güçten lambanın normal akımı (I = P ÷ V) bulunur; seri bağlı dirençten de aynı akım geçer ve gerilimin lambada düşmeyen kısmı bu dirençte düşer.',
 'Lamba direncini ya da üreteç gerilimini doğrudan seri dirence uygulamak; akımı yanlış gerilimle hesaplamak.',
 'Şekildeki devrede üreteç ve bağlantı telleri idealdir; lambanın etiketi şekilde verilmiştir. Lamba, etiketindeki gerilim ve güçle (normal parlaklıkta) çalışmaktadır.\nBuna göre, R direnci kaç Ω’dur?',
 3,[(2,'Direncin, lambanın direncine (V² ÷ P = 36 ÷ 18 = 2 Ω) eşit olduğunu düşünmüş.','bilgi'),
    (5,'Üretecin gerilimini (15 V) tamamen R’ye uygulamış: 15 ÷ 3 = 5 Ω.','dikkat'),
    (7,'Gerilimleri toplamış: (15 + 6) ÷ 3 = 7 Ω; R üzerindeki gerilim farkla bulunur.','islem'),
    (Fr(15,2),'Lambanın akımını üreteç gerilimiyle hesaplamış: I = 18 ÷ 15 = 1,2 A; R = 9 ÷ 1,2 = 7,5 Ω.','bilgi')],
 'R direncinin değeri (Ω).',
 ['Lamba normal çalışırken üzerindeki gerilim ve gücü kullanarak lambadan geçen akımı bul.'],
 [B('Lamba etiketi','etiket, lambanın normal çalıştığı gerilimi ve gücü gösterir; güç P = V × I olduğundan akım I = P ÷ V’dir. Örnek: 12 V – 24 W etiketli lambanın normal akımı 2 A’dir'),
  B('Seri devre','akım her elemanda aynıdır; üreteç gerilimi elemanların gerilimleri toplamına eşittir')],
 [A('Lambanın akımını bul','P = V · I.','I = 18 ÷ 6 = 3 A'),
  A('R’nin gerilimini bul','Seri devrede gerilimler toplanır: lambada 6 V düşer.','V_R = 15 − 6 = 9 V'),
  A('R’yi hesapla','Seri dirençten de 3 A geçer.','R = 9 ÷ 3 = 3 Ω')],
 'Seri bağlı etiketli lambada önce normal akımı bul; direnç, kalan gerilimin bu akıma oranıdır.',sekil=tk(sk))

# ---- 09 · Bir lambanın sökülmesi · öncüllü · zor ----
# N ana kolda; K ve L paralel. K söküldü: Req 1,5R → 2R. V=6,R=1: I: 4 → 3 (azalır); N gücü 16 → 9 (azalır); L akımı 2 → 3, gücü 4 → 9 (artar).
V9=Fr(6); R9=Fr(1)
Rea=R9+R9/2; Reb=R9+R9; Ia=V9/Rea; Ib=V9/Reb
assert (Ia,Ib)==(4,3) and Ib<Ia
PNa,PNb=Ia**2*R9,Ib**2*R9; PLa,PLb=(Ia/2)**2*R9,Ib**2*R9
assert (PNa,PNb)==(16,9) and (PLa,PLb)==(4,9) and PNb<PNa and PLb>PLa
sk=('\\draw (0,0) to[battery1] (0,3) -- (1.2,3) to[lamp,l={$N$}] (3.6,3) -- (4.6,3);\n'
    '\\draw (4.6,3) to[lamp,l_={$K$}] (4.6,0); \\draw (4.6,3) -- (7.6,3) to[lamp,l={$L$}] (7.6,0); \\draw (0,0) -- (7.6,0);\n'
    '\\fill (4.6,3) circle (1.7pt) (4.6,0) circle (1.7pt);')
O('0009','fz-el3-lamba-sokme','Paralel kollardan bir lambanın sökülmesi','Lamba parlaklığı','zor',
 'Bir lamba devreden çıkarıldığında eşdeğer direncin ve kol akımlarının değişimini yorumlayarak diğer lambaların parlaklık değişimini belirler.',
 'K söküldüğünde paralel bölümün direnci artar, toplam direnç büyür ve üreteçten çekilen akım azalır. N’nin akımı azaldığı için sönükleşir; L ise artık tüm akımı taşıdığından parlaklığı artar.',
 'Bir lamba sökülünce paralel koldaki lambanın etkilenmediğini düşünmek; ana koldaki lambanın parlaklığının arttığını sanmak.',
 'Şekildeki devrede K, L ve N lambaları özdeştir; lambaların dirençleri sabit ve üreteç idealdir. Devre dengeye ulaşmıştır. Daha sonra K lambası soketinden çıkarılıyor ve devre yeniden dengeye ulaşıyor.',
 [('N lambasının parlaklığı artar.',False,'K çıkarılınca eşdeğer direnç artar, ana koldaki akım azalır; N’nin gücü (P = I²R) azalır, lamba sönükleşir.','Bir lamba çıkınca kalan lambaların hepsinin daha parlak olacağını düşünmüş.'),
  ('L lambasının parlaklığı artar.',True,'Üreteç gerilimi V, lamba direnci R olsun. K varken toplam akım V ÷ 1,5R olup L bu akımın yarısını, yani V ÷ 3R’yi taşır; K çıkınca toplam akım V ÷ 2R olur ve tamamı L’den geçer. L’nin akımı V ÷ 3R’den V ÷ 2R’ye büyüdüğü için parlaklığı artar.','Paralel koldaki bir lambanın sökülmesinin diğer paralel lambayı etkilemediğini sanmış.'),
  ('Üreteçten çekilen akım azalır.',True,'K’nin kolu devreden çıkınca paralel bölümün direnci R/2’den R’ye çıkar; toplam direnç artar ve ideal üreteç aynı gerilimle daha az akım verir.','Bir kol azalınca üretecin daha çok akım vereceğini düşünmüş.')],
 ['Yalnız II','Yalnız III','I ve III','II ve III','I, II ve III'],
 ('N ana kolda, K ve L paralel.','K söküldü → paralel bölüm yalnız L'),
 ['K çıkarılınca paralel bölümün direnci ve devrenin toplam direnci nasıl değişir? Ona göre ana akıma bak.'],
 [B('Toplam direnç','paralel kollardan biri çıkarılırsa paralel bölümün eşdeğer direnci artar. Örnek: 2 Ω ve 2 Ω paralelken 1 Ω olan bölüm, bir kol çıkınca 2 Ω olur'),
  B('Parlaklık','özdeş lambalarda parlaklık akımın karesiyle değişir; akımı artan lamba daha parlak yanar')],
 'Bir paralel kol çıkarılınca toplam direnç artar, ana akım azalır; ama kalan paralel koldan geçen akım artabilir.',sekil=tk(sk))

# ---- 10 · Lamba türlerinin enerji tüketimi (tablo) · öncüllü · kolay ----
G10={'Akkor':60,'Kompakt flüoresan':15,'LED':10}
e1=Fr(G10['Akkor']-G10['LED'])*100/1000; assert e1==5                        # I doğru
assert Fr(G10['LED'],G10['Kompakt flüoresan'])==Fr(2,3)!=Fr(1,2)            # II yanlış (2/3, yarısı değil)
assert 2*G10['LED']>G10['Kompakt flüoresan']                                  # III doğru
sk=tablo_svg(['Lamba türü','Güç (W)'],[[k,str(v)] for k,v in G10.items()])
O('0010','fz-el3-lamba-turleri','Aynı ışığı veren lamba türlerinin enerji tüketimi','Elektriksel enerji ve güç','kolay',
 'Tabloda verilen güç değerlerinden belirli sürede harcanan enerjileri karşılaştırır ve yargıları değerlendirir.',
 'Enerji E = P·t’dir; aynı sürede güç büyük olan cihaz daha çok enerji harcar. Enerji farkı güç farkı ile süre çarpılarak, oran ise güç oranıyla bulunur.',
 'Güç oranını yanlış hesaplamak (ör. 10 W’ı 15 W’ın yarısı saymak); W ile kW’ı karıştırmak.',
 'Aynı odada aynı miktarda ışık veren üç farklı lamba türünün etiket güçleri tabloda verilmiştir. Lambalar etiket güçlerinde çalışmaktadır.',
 [('LED lamba 100 saat yandığında akkor lambadan 5 kWh daha az enerji harcar.',True,'Güç farkı 60 − 10 = 50 W = 0,05 kW’tır; 0,05 × 100 = 5 kWh.','W cinsinden bulduğu farkı kWh’ye çevirmeyi unutup sonucu yanlış bulmuş.'),
  ('Aynı süre yandıklarında LED lambanın harcadığı enerji, kompakt flüoresan lambanın harcadığı enerjinin yarısıdır.',False,'Aynı sürede enerji oranı güç oranına eşittir: 10 ÷ 15 = 2/3; yarısı değildir.','10 W’ı 15 W’ın yaklaşık yarısı sayıp oranı 1/2 almış.'),
  ('Aynı süre yanan iki LED lamba toplamda, bir kompakt flüoresan lambadan daha fazla enerji harcar.',True,'İki LED’in gücü 2 × 10 = 20 W, bir kompakt flüoresanın gücü 15 W’tır; aynı sürede 20 W olan daha çok enerji harcar.','Tek LED’in gücünü düşünüp iki lambanın gücünü toplamayı unutmuş.')],
 ['Yalnız I','Yalnız III','I ve II','I ve III','I, II ve III'],
 ('Güçler: akkor 60 W, kompakt flüoresan 15 W, LED 10 W.','E = P·t'),
 ['Her yargıda hangi iki lambanın gücünü hangi süreyle karşılaştırdığını bul; enerji = güç × süre.'],
 [B('Elektriksel enerji','E = P·t; güç kW, süre saat alınırsa enerji kWh olur. Örnek: 200 W’lık bir cihaz 5 saatte 1 kWh harcar'),
  B('Karşılaştırma','aynı sürede harcanan enerjiler, güçlerle aynı oranda olur')],
 'Aynı sürede enerji oranı güç oranına eşittir; farkları hesaplarken W’ı kW’a çevirmeyi unutma.',sekil=sk,kalip='tablo')

bitir(P,'elektrikuc','fiz|Elektrik')
