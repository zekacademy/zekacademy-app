"""AYT Matematik · Trigonometri · 20 soruluk paket (hafif mod; kardeş yok, ipucu 1).
Şekil, metin ve çeldirici değerleri aynı verilerden; her cevap ve çeldirici Fraction/math ile assert edilir."""
import sys,os,json,math
HD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(HD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
from ortak import *
from cizim import tikz_svg
from _hafif_mat import tablo_svg,mk
from fractions import Fraction as Fr
pi=math.pi; s2=math.sqrt(2); s3=math.sqrt(3)
def yak(a,b,t=1e-9): assert abs(a-b)<t,(a,b)
UK='amat|Trigonometri'
P=Parti('trigo','Trigonometri',UK,ders='AYT Matematik',idon='aytmat')
KY='ÖSYM AYT Matematik 2018–2026 (Trigonometri soruları; yalnız mantık) · yayın soru bankaları (yalnız mantık) · MEB 11. sınıf'
KART=[]; TIP={}
def kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip):
    KART.append(dict(id=id,konu='Trigonometri',alt=alt,fikir=fikir,tuzak=tuzak,zorluk=z,kalip=kalip,adim=adim,tipId=tipId,tip=tip,kaynak=KY)); TIP[tipId]=(tip,id)
def fs(v):
    v=Fr(v); n='−' if v<0 else ''; v=abs(v)
    return n+(str(v.numerator) if v.denominator==1 else f'{v.numerator}/{v.denominator}')
def Q(no,tipId,z,alt,kaz,kalip,metin,dogru,yan,istenen,ip,bilgi,ad,puf,kart_ozet,sekil=None,sira=None,kisa=None):
    """dogru=(şık metni, sayısal değer); yan=[(metin, değer, açıklama, tür)]. sira verilmezse sayısal değere göre küçükten büyüğe."""
    tip,kid=TIP[tipId]
    if sira is None:
        items=[dogru]+[(y[0],y[1]) for y in yan]; assert len({round(v,9) for _,v in items})==5,('esit sik',no,items)
        sira=[t for t,_ in sorted(items,key=lambda t:t[1])]
    d=dogru[0]; yy=[(y[0],y[2],y[3]) for y in yan]
    assert len(yy)==4 and len(set([d]+[y[0] for y in yy]))==5 and sorted(sira)==sorted([d]+[y[0] for y in yy]),(no,)
    mk(P,no,metin=metin,dogru=d,yan=yy,istenen=istenen,ad=ad,sekil=sekil,sira=sira,ip=ip,bilgi=bilgi,puf=puf,kisa=kisa,tipId=tipId,tip=tip,z=z,alt=alt,kaz=kaz,kalip=kalip,adim=len(ad),kart=f'{kid} ({kart_ozet})')
def fig(body,font='\\small'):
    return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font='+font+']\n'+body+'\n\\end{tikzpicture}')
MAVI='blue!70!black'; TUR='orange!90!black'; YES='green!50!black'; MOR='violet!80!black'

# ---------------- bilgi kutuları (tanım ve gösterim; örnekler soruların sayılarından farklı) ----------------
B_TNJ=B('Tanjant ve kotanjant','tanα = sinα / cosα ve cotα = cosα / sinα’dır; ikisi birbirinin çarpmaya göre tersidir. Örnek: sin 20° = a, cos 20° = b ise tan 20° = a/b ve cot 20° = b/a’dır')
B_ISR=B('Bölgelere göre işaretler','I. bölgede sin, cos ve tan pozitiftir; II. bölgede yalnız sin, III. bölgede yalnız tan, IV. bölgede yalnız cos pozitiftir. Örnek: 100° II. bölgededir; sin 100° > 0, cos 100° < 0, tan 100° < 0')
B_YAY=B('Yay uzunluğu ve daire dilimi','yarıçapı r olan bir çemberde radyan cinsinden θ merkez açısının gördüğü yay uzunluğu l = r·θ, daire diliminin alanı A = (1/2)·r²·θ’dır. Örnek: r = 4 ve θ = π/2 ise l = 2π ve A = 4π’dir')
B_IND=B('İndirgeme','açı, 180° ± a, 360° − a gibi yazılır; değerin işareti açının bulunduğu bölgeden, adı (sin, cos, tan) aynen kalarak gelir. Örnek: sin 160° = sin(180° − 20°) = sin 20°; cos 200° = −cos 20°; tan 340° = −tan 20°')
B_GRF=B('Sinüs grafiğinin ölçüleri','f(x) = a·sin(bx) + c grafiğinde en büyük değer c + |a|, en küçük değer c − |a|’dır; periyot 2π/|b|’dir. En büyük ile en küçük değerin ortası c’yi, farkın yarısı |a|’yı verir. Örnek: en büyük 5, en küçük 1 ise c = 3 ve |a| = 2’dir')
B_KES=B('Eğrilerin kesişimi','iki fonksiyonun grafiklerinin kesiştiği noktaların apsisleri f(x) = g(x) denkleminin çözümüdür; ordinatı, bulunan x değerini iki fonksiyondan birinde yerine yazarak elde edilir. Örnek: y = sin x ile y = 1/2 doğrusunun [0, π] aralığındaki kesişimleri sin x = 1/2 denkleminden gelir')
B_CEM=B('Birim çemberde koordinatlar','O merkezli birim çemberde pozitif x ekseniyle α açısı yapan ışının çemberi kestiği noktanın apsisi cosα, ordinatı sinαdır. Örnek: α = 45° için kesim noktası (√2/2, √2/2)’dir')
B_PER=B('Periyot','f(x + T) = f(x) eşitliğini sağlayan en küçük pozitif T sayısına periyot denir. f(x) = a·cos(bx) + c fonksiyonunun periyodu 2π/|b|’dir. Örnek: cos(3x) fonksiyonunun periyodu 2π/3’tür')
B_KOS=B('Kosinüs teoremi','bir üçgende a, b kenarları arasındaki açı C ise bu açının karşısındaki c kenarı için c² = a² + b² − 2ab·cosC’dir. Örnek: a = 2, b = 3, C = 60° ise c² = 4 + 9 − 2·2·3·(1/2) = 7’dir')
B_SIN=B('Sinüs teoremi','bir üçgende her kenarın uzunluğunun karşısındaki açının sinüsüne oranı sabittir: a/sinA = b/sinB = c/sinC = 2R (R çevrel çemberin yarıçapı). Örnek: A = 30°, a = 5 ise 2R = 5/(1/2) = 10’dur')
B_TOP=B('Toplam–fark formülleri','sin(a ± b) = sin a·cos b ± cos a·sin b, cos(a ± b) = cos a·cos b ∓ sin a·sin b, tan(a ± b) = (tan a ± tan b)/(1 ∓ tan a·tan b). Örnek: sin(30° + 45°) = (1/2)(√2/2) + (√3/2)(√2/2)')
B_IKI=B('İki kat açı formülleri','sin2x = 2·sinx·cosx, cos2x = cos²x − sin²x = 2cos²x − 1 = 1 − 2sin²x. Ayrıca sin²x + cos²x = 1’dir. Örnek: sin x = 1/3 ise cos2x = 1 − 2/9 = 7/9’dur')
B_DEN=B('Trigonometrik denklem','cos x = c denkleminde [0, 2π] aralığında c ≠ ±1 için iki kök vardır; c = 1 için x = 0 ve 2π, c = −1 için x = π’dir. Eşitliği tek bir fonksiyona (sin ya da cos) indirgeyip çarpanlarına ayırmak gerekir. Örnek: cos x = 1/2 için x = π/3 ve 5π/3’tür')
B_MOD=B('Dönel hareketin modeli','h(t) = a − b·cos(ct) kuralında a, en büyük ile en küçük değerin ortası; b, farkın yarısı; periyot 2π/c’dir. Örnek: en küçük 1, en büyük 7 ise a = 4 ve b = 3’tür')
B_TAB=B('Tablodan model kurma','h(t) = a + b·cos(ct) biçimindeki modelde tablodaki en büyük ve en küçük değerler a ile b’yi verir; c, periyottan 2π/c ile bulunur. Örnek: değerler 3 ile 9 arasında değişiyorsa a = 6, |b| = 3’tür')
B_TERS=B('Eş değer ifadeler','birim çember üzerinde ve dik üçgenlerde kenarların oranları açıyı belirler; çevrel çemberin yarıçapı R için a = 2R·sinA yazılır. Örnek: bir kenar 6, karşısındaki açı 30° ise R = 6')

# ---------------- kartlar ----------------
kart('K-ATR-01','Birim çemberde değer ve işaret','Birim çember üzerindeki noktanın koordinatları ve açının bulunduğu bölge, trigonometrik oranların değerini ve işaretini belirler; ifade bu değerlerden kurulur.','Bölge işaretini yanlış almak; tanjantın III. bölgede pozitif olduğunu unutmak; sin ile cos değerlerini yer değiştirmek.','kolay','şekilli',3,'trg-cember','Birim çemberde değer ve işaret')
kart('K-ATR-02','Yay uzunluğu ve daire dilimi','Radyan cinsinden merkez açı, yay uzunluğu ve yarıçap arasındaki l = rθ bağıntısıyla eksik büyüklük bulunur; dilim alanı yarıçap ve yaydan çıkar.','Alan formülündeki 1/2 çarpanını atmak; açıyı dereceyle radyan karıştırmak; dilim yerine daire alanı almak.','kolay','hikâyeli',3,'trg-yay','Yay uzunluğu ve daire dilimi')
kart('K-ATR-03','İndirgeme ile değer hesabı','Her açı 180° ya da 360° etrafında indirgenir; işaret bölgeden, değer 30°–45°–60° özel açılarından alınır.','İşareti bölgeye bakmadan almak; 180° ± a ile 90° ± a indirgemelerini karıştırmak.','kolay','düz',3,'trg-indirgeme','İndirgeme ile değer hesabı')
kart('K-ATR-04','Grafikten kural ve değer','Grafikteki en büyük, en küçük değer ve periyottan a, b, c bulunur; sorulan noktada fonksiyon değeri hesaplanır.','Genlik yerine uçlar farkını almak; periyodu yanlış okumak; c’nin işaretini ters almak.','orta','grafik',4,'trg-grafik','Grafikten kural ve değer')
kart('K-ATR-05','Dönel olayların modeli','Tablo ya da grafikten kosinüs modelinin a, b, c değerleri bulunur; istenen anda ya da koşulda model çözülür.','Periyodu yarım ya da iki kat almak; eşitsizliğin hangi aralığı verdiğini karıştırmak; işaret hatası.','orta','tablo',4,'trg-model','Dönel olayların modeli')
kart('K-ATR-06','Üçgende sinüs ve kosinüs teoremi','Verilen kenar ve açılara göre uygun teorem seçilir; kosinüs teoreminde işaret, sinüs teoreminde karşılıklı kenar–açı eşleşmesi korunur.','cos 120° işaretini yanlış almak; kenarı bitişik açıyla eşlemek; 2R yerine R yazmak.','orta','hikâyeli',4,'trg-ucgen','Üçgende sinüs ve kosinüs teoremi')
kart('K-ATR-07','Toplam–fark formülleri','Açılar bilinen özel açıların toplamı ya da farkı olarak yazılır; formüldeki işaret kuralı uygulanır, gerekirse tanjant ızgaradan okunur.','Tanjantta paydadaki işareti ters almak; toplam ile fark formüllerini karıştırmak.','orta','öncüllü',4,'trg-toplamfark','Toplam–fark formülleri')
kart('K-ATR-08','İki kat açı ve özdeşlikler','Verilen koşul sin²x + cos²x = 1 ve iki kat açı formülleriyle istenen ifadeye dönüştürülür; yardımcı bir ifadenin karesi alınır.','İki kat açıdaki 2 çarpanını unutmak; karesini alırken orta terimi atlamak; işareti ters çevirmek.','zor','düz',5,'trg-ikikat','İki kat açı ve özdeşlikler')
kart('K-ATR-09','Trigonometrik denklem ve kök toplamı','Denklem tek fonksiyona indirgenip çarpanlarına ayrılır; verilen aralıktaki tüm kökler (uç noktalar dahil) bulunup toplanır.','Uç noktaları atlamak; çarpan ayırmada işaret hatası; yalnız bir bölgedeki kökü almak.','zor','grafik',5,'trg-denklem','Trigonometrik denklem ve kök toplamı')

# ================= 01 kolay · birim çemberde değer (şekilli) =================
c1=Fr(-4,5); sn1=Fr(3,5); assert c1**2+sn1**2==1
tn1=sn1/c1; ct1=c1/sn1
v=tn1+ct1; assert v==Fr(-25,12)
e=[Fr(25,12),Fr(7,12),Fr(-7,12),Fr(-12,25)]
assert v==Fr(-25,12)
assert (-tn1)+(-ct1)==e[0] and Fr(-3,4)+Fr(4,3)==e[1] and Fr(3,4)+Fr(-4,3)==e[2] and sn1*c1==e[3]
ang=math.degrees(math.atan2(0.6,-0.8)); yak(ang,143.13010235,1e-6)
SK=fig(f'''\\fill[{TUR}!15] (0,0) -- (0.9,0) arc (0:{ang:.2f}:0.9) -- cycle;
\\draw[thick] (0,0) circle (2);
\\draw[-{{Stealth}}] (-2.5,0) -- (2.8,0) node[right] {{$x$}};
\\draw[-{{Stealth}}] (0,-2.4) -- (0,2.7) node[above] {{$y$}};
\\draw[very thick,{MAVI}] (0,0) -- (-1.6,1.2);
\\fill[{MAVI}] (-1.6,1.2) circle (2.4pt);
\\node[above left] at (-1.6,1.2) {{$P\\left(-\\dfrac45,\\ \\dfrac35\\right)$}};
\\draw[{TUR},thick,-{{Stealth}}] (0.9,0) arc (0:{ang:.2f}:0.9);
\\node[{TUR}!70!black] at ({1.3*math.cos(math.radians(72)):.2f},{1.3*math.sin(math.radians(72)):.2f}) {{$\\alpha$}};
\\node[below left] at (0,0) {{$O$}};
\\node[below right,font=\\footnotesize] at (2,0) {{$1$}}; \\node[above right,font=\\footnotesize] at (0,2) {{$1$}};''')
Q('0001','trg-cember','kolay','Birim Çemberde Değer','Birim çember üzerindeki noktanın koordinatlarından trigonometrik oranları bulup işaretini yorumlayarak işlem yapar.','şekilli',
 'Şekilde, O merkezli birim çember ile çember üzerindeki P noktası verilmiştir. OP ışınının pozitif x ekseniyle yaptığı yönlü açının ölçüsü α’dır.\nBuna göre, tanα + cotα toplamı kaçtır?',
 (fs(v),float(v)),
 [(fs(e[0]),float(e[0]),'II. bölgede tanjant ve kotanjantın pozitif olduğunu sanmış: 3/4 + 4/3 = 25/12.','bilgi'),
  (fs(e[1]),float(e[1]),'tanα = −3/4’ü doğru bulmuş fakat cotα’yı pozitif almış: −3/4 + 4/3 = 7/12.','islem'),
  (fs(e[2]),float(e[2]),'cotα = −4/3’ü doğru bulmuş fakat tanα’yı pozitif almış: 3/4 − 4/3 = −7/12.','islem'),
  (fs(e[3]),float(e[3]),'Toplam yerine çarpımı hesaplamış: sinα · cosα = 3/5 · (−4/5) = −12/25.','dikkat')],
 'tanα ile cotα’nın toplamı.',['Şekilde okuyabildiğin koordinatların hangi iki oranı doğrudan verdiğini düşün; sonra istenen oranları bunlardan kur.'],[B_TNJ],
 [A('Oranları belirle','P noktasının apsisi cosα, ordinatı sinαdır.','cosα = −4/5 · sinα = 3/5'),
  A('Tanjant ve kotanjant','tanα = sinα/cosα, cotα = cosα/sinα hesaplanır.','tanα = (3/5)/(−4/5) = −3/4 · cotα = −4/3'),
  A('Topla','İki değer toplanır.','−3/4 + (−4/3) = −9/12 − 16/12 = −25/12')],
 'Bir oranın işaretini önce bölgeden, değerini sonra koordinatlardan bul.','K-ATR-01; P(−4/5, 3/5) noktası, tanα + cotα',sekil=SK)

# ================= 02 kolay · bölge işaretleri (öncüllü, şekilli) =================
al,be,ga=130,250,320
R_=lambda d:math.radians(d)
I1=math.sin(R_(al))*math.cos(R_(be)); I2=math.tan(R_(be))*math.cos(R_(ga)); I3=math.tan(R_(al))*math.sin(R_(ga))
assert I1<0 and I2>0 and I3>0
SK2=[]
for d,nm,cl in ((al,'\\alpha',MAVI),(be,'\\beta',TUR),(ga,'\\gamma',YES)):
    ca,sa=math.cos(R_(d)),math.sin(R_(d))
    SK2.append(f'\\draw[very thick,{cl}] (0,0) -- ({2*ca:.3f},{2*sa:.3f}); \\fill[{cl}] ({2*ca:.3f},{2*sa:.3f}) circle (2.2pt);')
    r=0.55 if d==al else (0.75 if d==be else 0.95)
    SK2.append(f'\\draw[{cl},thick,-{{Stealth}}] ({r},0) arc (0:{d}:{r});')
    SK2.append(f'\\node[{cl}] at ({2.75*ca:.3f},{2.6*sa:.3f}) {{${nm}={d}^\\circ$}};')
SK2=fig(f'''\\draw[thick] (0,0) circle (2);
\\draw[-{{Stealth}}] (-2.5,0) -- (2.8,0) node[right] {{$x$}};
\\draw[-{{Stealth}}] (0,-2.5) -- (0,2.7) node[above] {{$y$}};
'''+'\n'.join(SK2)+'\n\\node[above right,font=\\footnotesize] at (0,0) {$O$};')
Q('0002','trg-cember','kolay','Bölgelere Göre İşaret','Yönlü açıların bulunduğu bölgeden sin, cos ve tan işaretlerini belirleyerek ifadelerin işaretini yorumlar.','öncüllü',
 'Şekilde, O merkezli birim çember ve pozitif x ekseniyle yönlü açılar yapan üç ışın gösterilmiştir.\nBuna göre,\nI. sinα · cosβ\nII. tanβ · cosγ\nIII. tanα · sinγ\nifadelerinden hangileri pozitiftir?',
 ('II ve III',3),
 [('Yalnız II',1,'sinγ’yı IV. bölgede pozitif almış: I negatif, II pozitif, III tanα(−)·sinγ(+) negatif kalır.','bilgi'),
  ('Yalnız III',2,'tanβ’yı III. bölgede negatif almış: I negatif, II negatif, III pozitif kalır.','bilgi'),
  ('I ve II',2.5,'cosβ’yı III. bölgede pozitif, tanα’yı II. bölgede pozitif almış: I ve II pozitif, III negatif kalır.','bilgi'),
  ('I, II ve III',4,'cosβ’yı III. bölgede pozitif sanmış; diğer işaretleri doğru almış: I da pozitif çıkar.','bilgi')],
 'Pozitif olan ifadelerin hangileri olduğu.',['Her açının hangi bölgede olduğuna bak; sonra ifadedeki her oranın o bölgedeki işaretini ayrı ayrı yaz.'],[B_ISR],
 [A('Bölgeleri bul','130° II., 250° III., 320° IV. bölgededir.','α: II. · β: III. · γ: IV.'),
  A('Oranların işaretleri','Her bölgede sin, cos, tan işaretleri ayrı bulunur.','sinα (+), tanα (−) · cosβ (−), tanβ (+) · cosγ (+), sinγ (−)'),
  A('Çarpımları değerlendir','İşaretler çarpılır.','I: (+)(−) = − · II: (+)(+) = + · III: (−)(−) = +'),
  A('Sonuç','Pozitif olanlar II ve III’tür.','II ve III')],
 'Üç oranın işaretini bölgeden ezberlemek yerine her açıyı önce bölgesine yerleştir.','K-ATR-01; üç yönlü açı, çarpım işaretleri',sekil=SK2,
 sira=['Yalnız II','Yalnız III','I ve II','II ve III','I, II ve III'])

# ================= 03 kolay · daire dilimi (hikâyeli, şekilli) =================
r3=9; l3=6   # yay = 6π; θ = l/r = 2π/3
alan3=Fr(1,2)*81*Fr(2,3); assert alan3==27 and Fr(1,2)*r3*l3==27
e3=[Fr(27,2),Fr(81,2),r3*l3,81]; assert e3==[Fr(27,2),Fr(81,2),54,81]
SK=fig(f'''\\fill[{TUR}!18] (0,0) -- ({2.4*math.cos(R_(30)):.3f},{2.4*math.sin(R_(30)):.3f}) arc (30:150:2.4) -- cycle;
\\draw[thick] ({2.4*math.cos(R_(150)):.3f},{2.4*math.sin(R_(150)):.3f}) -- (0,0) -- ({2.4*math.cos(R_(30)):.3f},{2.4*math.sin(R_(30)):.3f});
\\draw[thick] ({2.4*math.cos(R_(30)):.3f},{2.4*math.sin(R_(30)):.3f}) arc (30:150:2.4);
\\fill (0,0) circle (1.8pt); \\node[below] at (0,0) {{$O$}};
\\node[above=3pt] at (0,2.4) {{yay uzunluğu $6\\pi$ cm}};
\\node[below right,{MAVI}!80!black] at ({1.2*math.cos(R_(30)):.3f},{1.2*math.sin(R_(30)):.3f}) {{$9$ cm}};''')
Q('0003','trg-yay','kolay','Yay Uzunluğu ve Dilim Alanı','Yay uzunluğu ve yarıçaptan daire diliminin alanını hesaplar.','hikâyeli',
 'Bir pastacı, tabanı şekilde ölçüleri verilen daire dilimi biçiminde bir tart yapıyor. Tartın dilim biçimli üst yüzünün tamamı çikolata kaplamayla kaplanacak ve kaplamanın kalınlığı ihmal edilecektir.\nBuna göre kaplanacak yüzeyin alanı kaç cm² dir?',
 ('27π',27.0),
 [('27π/2',13.5,'Alan formülündeki 1/2 çarpanını iki kez uygulamış: (1/2)·(1/2)·9·6π.','islem'),
  ('81π/2',40.5,'Dilimi yarım daire sanmış: (1/2)·π·9².','bilgi'),
  ('54π',54.0,'Alan formülündeki 1/2 çarpanını unutmuş: 9 · 6π.','islem'),
  ('81π',81.0,'Dilim yerine tam dairenin alanını hesaplamış: π · 9².','dikkat')],
 'Daire diliminin alanı (cm²).',['Verilenlerin yarıçap ve yay uzunluğu olduğuna dikkat et; dilimin merkez açısını mı yoksa doğrudan alanı mı bulacağına karar ver.'],[B_YAY],
 [A('Merkez açıyı bul','l = r·θ bağıntısıyla θ bulunur.','6π = 9 × θ → θ = 2π/3'),
  A('Alan formülünü yaz','Dilim alanı (1/2)·r²·θ’dır.','A = (1/2) × 9² × 2π/3'),
  A('Hesapla','Sayılar çarpılır.','A = (1/2) × 81 × 2π/3 = 27π')],
 'Yarıçap ve yay uzunluğu bilinen dilimin alanına açıyı hiç bulmadan ulaşılabilir mi, dene.','K-ATR-02; r = 9, yay = 6π',sekil=SK,
 kisa='Dilimin alanı (1/2)·r·l olduğundan merkez açıyı hiç bulmadan (1/2) × 9 × 6π = 27π yazılabilir.')

# ================= 04 kolay · indirgeme (düz) =================
v4=Fr(1,2)+2*Fr(1,2)+4*1; assert v4==Fr(11,2)
yak(math.sin(R_(150))+2*math.cos(R_(300))+4*math.tan(R_(225)),5.5)
e4=[Fr(-11,2),Fr(-5,2),Fr(7,2),Fr(9,2)]
assert -Fr(1,2)-2*Fr(1,2)-4==e4[0] and Fr(1,2)+1-4==e4[1] and Fr(1,2)-1+4==e4[2] and -Fr(1,2)+1+4==e4[3]
Q('0004','trg-indirgeme','kolay','İndirgeme ve Özel Açılar','Büyük açıları indirgeyip bölge işaretiyle özel açı değerlerinden ifadenin değerini bulur.','düz',
 'sin150° + 2cos300° + 4tan225° işleminin sonucu kaçtır?',
 (fs(v4),float(v4)),
 [(fs(e4[0]),float(e4[0]),'Her üç terimin işaretini tersine almış: −1/2 − 1 − 4.','bilgi'),
  (fs(e4[1]),float(e4[1]),'III. bölgede tanjantı negatif almış: tan225° = −1 bulup 1/2 + 1 − 4 yazmış.','bilgi'),
  (fs(e4[2]),float(e4[2]),'IV. bölgede cos300°’yi negatif almış: 1/2 − 1 + 4.','bilgi'),
  (fs(e4[3]),float(e4[3]),'II. bölgede sin150°’yi negatif almış: −1/2 + 1 + 4.','bilgi')],
 'Üç trigonometrik terimin katlı toplamı.',['Her açıyı 180° ya da 360° etrafında 0°–90° arasında bir açıya indirge; işareti ayrı bir adımda bölgeden belirle.'],[B_IND],
 [A('sin150° değeri','150° II. bölgede, sin pozitiftir; 180° − 30° olarak yazılır.','sin150° = sin30° = 1/2'),
  A('cos300° değeri','300° IV. bölgede, cos pozitiftir; 360° − 60° olarak yazılır.','cos300° = cos60° = 1/2'),
  A('tan225° değeri','225° III. bölgede, tan pozitiftir; 180° + 45° olarak yazılır.','tan225° = tan45° = 1'),
  A('Sonucu yaz','Değerler yerine konur.','1/2 + 2 × 1/2 + 4 × 1 = 11/2')],
 'İndirgemede önce bölgeye bak: işaret oradan, değer ise 0°–90° arasındaki karşılığından gelir.','K-ATR-03; sin150°, cos300°, tan225° birleşimi')

# ================= 05 orta · grafikten kural (grafik) =================
a5,b5,c5=3,2,-1
f5=lambda x:a5*math.sin(b5*x)+c5
v5=Fr(1,2); yak(f5(5*pi/12),0.5)
e5=[Fr(5,2),2,0,Fr(-5,2)]
yak(a5*0.5-c5,2.5); yak(6*0.5+c5,2); yak(2*0.5+c5,0); yak(-a5*0.5+c5,-2.5)
kx=1.3; ky=0.52
def X(x): return x*kx
g=[]
for j in range(-4,3): g.append(f'\\draw[gray!35,thin] (0,{j*ky:.3f}) -- ({X(pi)+0.35:.3f},{j*ky:.3f});')
for i in range(1,5): g.append(f'\\draw[gray!35,thin] ({X(i*pi/4):.3f},{-4*ky:.3f}) -- ({X(i*pi/4):.3f},{2*ky:.3f});')
g.append(f'\\draw[-{{Stealth}},thick] (-0.1,0) -- ({X(pi)+0.75:.3f},0) node[right] {{$x$}};')
g.append(f'\\draw[-{{Stealth}},thick] (0,{-4*ky-0.35:.3f}) -- (0,{2*ky+0.6:.3f}) node[above] {{$y$}};')
for j in (-4,-3,-2,-1,1,2): g.append(f'\\node[left=2pt,font=\\footnotesize,fill=white,inner sep=0.5pt] at (0,{j*ky:.3f}) {{${j}$}};')
for i,t in ((1,'\\frac{\\pi}{4}'),(2,'\\frac{\\pi}{2}'),(3,'\\frac{3\\pi}{4}'),(4,'\\pi')): g.append(f'\\node[above=1pt,font=\\footnotesize,fill=white,inner sep=0.5pt] at ({X(i*pi/4):.3f},{-4*ky-0.02:.3f}) {{${t}$}};'.replace('above=1pt','below=1pt').replace(f'{-4*ky-0.02:.3f}','0'))
g.append(f'\\draw[{MAVI},very thick,smooth,domain=0:{pi:.4f},samples=60,variable=\\t] plot ({{\\t*{kx}}},{{({a5}*sin(2*\\t r)+({c5}))*{ky}}});')
g.append(f'\\fill[{TUR}] ({X(pi/4):.3f},{2*ky:.3f}) circle (2.4pt) node[above right,black] {{$\\left(\\frac{{\\pi}}{{4}},\\,2\\right)$}};')
g.append(f'\\fill[{TUR}] ({X(3*pi/4):.3f},{-4*ky:.3f}) circle (2.4pt) node[below left,black] {{$\\left(\\frac{{3\\pi}}{{4}},\\,-4\\right)$}};')
SK=fig('\n'.join(g))
# tik etiketleri x ekseninde: yukarıdaki replace ile 0 yüksekliğine alındı
Q('0005','trg-grafik','orta','Sinüs Grafiğinden Kural','Sinüs eğrisinin en büyük ve en küçük noktalarından a, b, c değerlerini bulup fonksiyon değerini hesaplar.','grafik',
 'Şekilde, a > 0 ve b > 0 olmak üzere f(x) = a·sin(bx) + c fonksiyonunun [0, π] aralığındaki grafiği ve grafiğin en büyük ile en küçük değeri aldığı noktalar gösterilmiştir.\nBuna göre f(5π/12) değeri kaçtır?',
 (fs(v5),float(v5)),
 [(fs(e5[0]),2.5,'c = −1 yerine +1 almış: 3 · (1/2) + 1.','islem'),
  (fs(e5[1]),2.0,'Genliği en büyük ile en küçük değerin farkı (6) sanmış: 6 · (1/2) − 1.','bilgi'),
  (fs(e5[2]),0.0,'Genliği en büyük değer olan 2 sanmış: 2 · (1/2) − 1.','dikkat'),
  (fs(e5[3]),-2.5,'sin(5π/6) değerini negatif almış: 3 · (−1/2) − 1.','islem')],
 'f(5π/12) değeri.',['Grafikteki iki işaretli noktanın ordinatlarından önce eğrinin orta çizgisini ve en büyük sapmasını bul; periyodu ise x eksenindeki konumlarından çıkar.'],[B_GRF],
 [A('a ve c’yi bul','En büyük 2, en küçük −4: farkın yarısı a, ortası c’dir.','a = (2 + 4)/2 = 3 · c = (2 − 4)/2 = −1'),
  A('b’yi bul','En büyük ile en küçük değer arası yarım periyottur: π/2. Periyot π olur.','2π/b = π → b = 2'),
  A('Değeri hesapla','x = 5π/12 yazılır.','f(5π/12) = 3 sin(5π/6) − 1'),
  A('Sonuç','sin(5π/6) = 1/2’dir.','3 × 1/2 − 1 = 1/2')],
 'Grafikten kural çıkarırken önce orta çizgiyi, sonra genliği, en son periyodu oku.','K-ATR-04; 3sin(2x) − 1 grafiği',sekil=SK)

# ================= 06 orta · iki grafik, kesişim uzunluğu (grafik) =================
xa,xb=pi/4,5*pi/4
yak(math.sin(xa),math.cos(xa)); yak(math.sin(xb),math.cos(xb))
v6=math.sqrt(pi**2+2); yak(math.hypot(xb-xa,math.sin(xb)-math.sin(xa)),v6)
e6=[(pi,'π'),(math.sqrt(pi**2+0.5),'√(π² + 1/2)'),(math.sqrt(pi**2+4),'√(π² + 4)'),(math.sqrt(pi**2/4+2),'√(π²/4 + 2)')]
yak(math.hypot(xb-xa,0),pi); yak(math.hypot(xb-xa,s2/2),e6[1][0]); yak(math.hypot(xb-xa,2),e6[2][0]); yak(math.hypot(pi/2,s2),e6[3][0])
kx6=0.92; ky6=1.15
def X6(x): return x*kx6
g=[f'\\draw[gray!35,thin] ({X6(i*pi/2):.3f},{-1.25*ky6:.3f}) -- ({X6(i*pi/2):.3f},{1.25*ky6:.3f});' for i in range(1,5)]
g+= [f'\\draw[gray!35,thin] (0,{j*ky6:.3f}) -- ({X6(2*pi)+0.2:.3f},{j*ky6:.3f});' for j in (-1,1)]
g.append(f'\\draw[-{{Stealth}},thick] (-0.1,0) -- ({X6(2*pi)+0.8:.3f},0) node[right] {{$x$}};')
g.append(f'\\draw[-{{Stealth}},thick] (0,{-1.35*ky6:.3f}) -- (0,{1.5*ky6:.3f}) node[above] {{$y$}};')
for i,t in ((1,'\\frac{\\pi}{2}'),(2,'\\pi'),(3,'\\frac{3\\pi}{2}'),(4,'2\\pi')): g.append(f'\\node[below=1pt,font=\\footnotesize] at ({X6(i*pi/2):.3f},{-1.25*ky6:.3f}) {{${t}$}};')
g.append(f'\\node[left=2pt,font=\\footnotesize] at (0,{ky6:.3f}) {{$1$}}; \\node[left=2pt,font=\\footnotesize] at (0,{-ky6:.3f}) {{$-1$}};')
g.append(f'\\draw[{MAVI},very thick,smooth,domain=0:{2*pi:.4f},samples=70,variable=\\t] plot ({{\\t*{kx6}}},{{sin(\\t r)*{ky6}}});')
g.append(f'\\draw[{TUR},very thick,smooth,domain=0:{2*pi:.4f},samples=70,variable=\\t] plot ({{\\t*{kx6}}},{{cos(\\t r)*{ky6}}});')
g.append(f'\\fill ({X6(xa):.3f},{math.sin(xa)*ky6:.3f}) circle (2.4pt) node[above=2pt] {{$A$}};')
g.append(f'\\fill ({X6(xb):.3f},{math.sin(xb)*ky6:.3f}) circle (2.4pt) node[below=2pt] {{$B$}};')
g.append(f'\\node[{MAVI}] at ({X6(2.2):.3f},{1.12*ky6:.3f}) {{$y=\\sin x$}}; \\node[{TUR}] at ({X6(5.35):.3f},{1.15*ky6:.3f}) {{$y=\\cos x$}};')
SK=fig('\n'.join(g))
Q('0006','trg-grafik','orta','Sinüs ve Kosinüs Grafiklerinin Kesişimi','İki trigonometrik fonksiyonun grafiklerinin kesişim noktalarını bulup noktalar arasındaki uzaklığı hesaplar.','grafik',
 'Şekilde, [0, 2π] aralığında y = sinx ve y = cosx fonksiyonlarının grafikleri ile bu grafiklerin kesiştiği A ve B noktaları gösterilmiştir.\nBuna göre |AB| uzunluğu kaç birimdir?',
 ('√(π² + 2)',v6),
 [(e6[0][1],e6[0][0],'A ve B’nin aynı yükseklikte olduğunu sanıp yalnız apsis farkını (π) almış.','dikkat'),
  (e6[1][1],e6[1][0],'Ordinat farkını √2/2 (yalnız bir ordinat) almış: √(π² + 1/2).','islem'),
  (e6[2][1],e6[2][0],'Ordinatları ±1 sanmış, ordinat farkını 2 almış: √(π² + 4).','bilgi'),
  (e6[3][1],e6[3][0],'Apsis farkını π/2 almış (π/4 ile 3π/4), ordinat farkını √2 bırakmış.','bilgi')],
 '|AB| uzunluğu.',['Kesişim noktalarının apsislerini bulmak için iki eğrinin eşit olduğu x değerlerini yaz; sonra iki noktanın koordinatlarından uzaklığı hesapla.'],[B_KES],
 [A('Apsisleri bul','sinx = cosx denkleminden tanx = 1 olur; [0, 2π] içindeki kökler yazılır.','x = π/4 ve x = 5π/4'),
  A('Ordinatları bul','Her kök sinx’te yerine yazılır.','A(π/4, √2/2) · B(5π/4, −√2/2)'),
  A('Farkları yaz','Yatay fark π, düşey fark √2’dir.','Δx = 5π/4 − π/4 = π · Δy = √2/2 + √2/2 = √2'),
  A('Uzaklığı hesapla','İki nokta arası uzaklık formülü uygulanır.','|AB| = √(π² + 2)')],
 'Kesişim noktasının koordinatlarında apsisi denklemden, ordinatı bulunan apsisi yerine yazarak bul.','K-ATR-04; sin x ve cos x kesişimleri',sekil=SK)

# ================= 07 orta · birim çemberde tanjant ekseni (şekilli) =================
sn7,cs7=Fr(3,5),Fr(4,5); assert Fr(1,2)*sn7*cs7==Fr(6,25) and sn7<cs7
v7=sn7/cs7; assert v7==Fr(3,4)
e7=[cs7/sn7,sn7,cs7,sn7*cs7]; assert e7==[Fr(4,3),Fr(3,5),Fr(4,5),Fr(12,25)]
R7=3.0; Px,Py=R7*0.8,R7*0.6; Ty=R7*0.75
SK=fig(f'''\\fill[{MAVI}!15] (0,0) -- ({Px:.2f},0) -- ({Px:.2f},{Py:.2f}) -- cycle;
\\draw[thick] (0,0) -- ({R7+0.3:.2f},0); \\draw[thick] (0,0) -- (0,{R7+0.3:.2f});
\\draw[thick] ({R7:.2f},0) arc (0:90:{R7});
\\draw[{TUR},very thick] ({R7:.2f},0) -- ({R7:.2f},{Ty:.2f});
\\draw[very thick] (0,0) -- ({R7:.2f},{Ty:.2f});
\\draw[{MAVI},very thick] ({Px:.2f},0) -- ({Px:.2f},{Py:.2f}) -- (0,0);
\\fill (0,0) circle (1.8pt); \\fill ({R7:.2f},0) circle (1.8pt); \\fill ({Px:.2f},0) circle (1.8pt); \\fill ({Px:.2f},{Py:.2f}) circle (1.8pt); \\fill ({R7:.2f},{Ty:.2f}) circle (1.8pt);
\\node[below left] at (0,0) {{$O$}}; \\node[below] at ({Px:.2f},0) {{$H$}}; \\node[below right] at ({R7:.2f},0) {{$A$}};
\\node[above left,font=\\small] at ({Px:.2f},{Py:.2f}) {{$P$}}; \\node[right] at ({R7:.2f},{Ty:.2f}) {{$T$}};
\\draw[{MAVI},thick,-{{Stealth}}] (0.75,0) arc (0:36.87:0.75); \\node[{MAVI}!80!black] at (1.05,0.28) {{$\\alpha$}};
\\node[{MAVI}!80!black,align=left,font=\\small] at (1.5,-0.95) {{Alan$(OHP)=\\dfrac{{6}}{{25}}$ br$^2$}};''')
Q('0007','trg-cember','orta','Birim Çemberde Tanjant Ekseni','Birim çember üzerindeki dik üçgenin alanından sinα ve cosα’yı bulup tanjant eksenindeki uzunluğu hesaplar.','şekilli',
 'Şekilde, O merkezli birim çember ile çember üzerinde P noktası, P’den x eksenine inilen dikme ayağı H, çemberin A(1, 0) noktasındaki teğet doğrusu ve OP ışınının bu teğeti kestiği T noktası gösterilmiştir. OHP üçgeninin alanı şekilde verilmiştir ve m(AOP) = α, 0 < α < π/4 dir.\nBuna göre |AT| uzunluğu kaç birimdir?',
 (fs(v7),float(v7)),
 [(fs(e7[0]),float(e7[0]),'α < π/4 koşulunu atlayıp sinα ile cosα’yı yer değiştirmiş: tanα = 4/3.','dikkat'),
  (fs(e7[1]),float(e7[1]),'|AT| uzunluğunu sinα sanmış.','bilgi'),
  (fs(e7[2]),float(e7[2]),'|AT| uzunluğunu cosα sanmış.','bilgi'),
  (fs(e7[3]),float(e7[3]),'sinα · cosα = 12/25 değerini bulup tanα sanmış.','dikkat')],
 '|AT| uzunluğu.',['OHP üçgeninin dik kenarlarını α cinsinden yaz; alan bilgisinden hangi ifade çıktığına bak, sonra |AT|’nin hangi orana karşılık geldiğini düşün.'],[B_CEM],
 [A('Dik kenarları yaz','Birim çemberde |OH| = cosα, |HP| = sinα’dır.','Alan = (1/2) · cosα · sinα'),
  A('Alandan denklem kur','Verilen alan yerine konur.','(1/2) · sinα · cosα = 6/25 → sinα · cosα = 12/25'),
  A('Değerleri belirle','sin²α + cos²α = 1 ve 0 < α < π/4 (sinα < cosα).','sinα = 3/5 · cosα = 4/5'),
  A('|AT| değerini bul','OAT dik üçgeninde |AT| = tanα’dır.','|AT| = (3/5)/(4/5) = 3/4')],
 '|AT| uzunluğunun OAT dik üçgeninde hangi orana karşılık geldiğini sor.','K-ATR-01; OHP alanı, tanjant ekseni',sekil=SK)

# ================= 08 orta · öncüllü, f(x)=1−2cos(πx/2) =================
f8=lambda x:1-2*math.cos(pi*x/2)
yak(f8(0),-1); yak(f8(1),1); yak(f8(2),3)
assert abs(f8(5)-f8(1))<1e-9
kok=[x/1000 for x in range(0,4001) if abs(f8(x/1000)-1)<1e-9]; assert kok==[1.0,3.0] and sum(kok)==4
Q('0008','trg-grafik','orta','Kosinüs Fonksiyonunun Özellikleri','Kosinüs türü bir fonksiyonun periyodunu, grafiğin eksen kesimini ve denklem köklerini yorumlar.','öncüllü',
 'f(x) = 1 − 2cos(πx/2) fonksiyonu için\nI. f fonksiyonunun periyodu 4 tür.\nII. f fonksiyonunun grafiği y eksenini (0, 3) noktasında keser.\nIII. [0, 4] aralığında f(x) = 1 denkleminin köklerinin toplamı 4 tür.\nifadelerinden hangileri doğrudur?',
 ('I ve III',5),
 [('Yalnız I',1,'III’te kökleri x = π/2, 3π/2 gibi π’li alıp toplamı 2π bulmuş; I’i doğru değerlendirmiş.','bilgi'),
  ('Yalnız III',2,'Periyodu 2π/π = 2 hesaplamış (b = π/2’yi π almış); II’yi ve III’ü doğru değerlendirmiş.','islem'),
  ('I ve II',3,'f(0) = 1 + 2 = 3 hesaplamış (cos0 = 1 iken işareti ters kullanmış) ve III’te π’li kök alıp toplamı 2π bulmuş.','islem'),
  ('II ve III',4,'Periyodu 2 bulmuş ve f(0) = 3 hesaplamış; III’ü doğru değerlendirmiş.','islem')],
 'Doğru olan ifadelerin hangileri olduğu.',['Üç ifadeyi ayrı ayrı sına: periyot için formülü, eksen kesimi için x = 0’ı, kökler için cos’un sıfır olduğu açıları kullan.'],[B_PER],
 [A('I’i incele','Periyot 2π/(π/2) ile bulunur.','T = 2π ÷ (π/2) = 4 → I doğru'),
  A('II’yi incele','x = 0 yazılır.','f(0) = 1 − 2cos0 = −1 → kesim (0, −1), II yanlış'),
  A('III’ü incele','1 − 2cos(πx/2) = 1 için cos(πx/2) = 0 olur.','πx/2 = π/2 + kπ → x = 1, 3'),
  A('Köklerin toplamı','[0, 4] içindeki kökler toplanır.','1 + 3 = 4 → III doğru')],
 'Öncüllü sorularda her ifadeyi ayrı bir mini soru gibi çöz; birini diğerine bağlama.','K-ATR-04; 1 − 2cos(πx/2) için üç yargı',
 sira=['Yalnız I','Yalnız III','I ve II','II ve III','I ve III'])

# ================= 09 orta · kosinüs teoremi (hikâyeli, şekilli) =================
a9,b9,t9=30,50,120
d9=math.sqrt(a9**2+b9**2-2*a9*b9*math.cos(R_(t9))); yak(d9,70)
yak(math.sqrt(900+2500-1500),math.sqrt(1900))
yak(math.sqrt(900+2500),10*math.sqrt(34))
# ölçek: 10 km = 0.6 cm
A9=(1.8,0); B9=(3.0*math.cos(R_(120)),3.0*math.sin(R_(120)))
SK=fig(f'''\\draw[{MAVI},very thick] (0,0) -- ({A9[0]:.3f},0); \\draw[{TUR},very thick] (0,0) -- ({B9[0]:.3f},{B9[1]:.3f});
\\draw[dashed,thick] ({A9[0]:.3f},0) -- ({B9[0]:.3f},{B9[1]:.3f});
\\fill (0,0) circle (2.2pt) node[below left] {{Liman}}; \\fill ({A9[0]:.3f},0) circle (2.2pt) node[below right] {{$A$}}; \\fill ({B9[0]:.3f},{B9[1]:.3f}) circle (2.2pt) node[above left] {{$B$}};
\\node[below,{MAVI}!80!black] at (0.9,0) {{$30$ km}};
\\node[left=2pt,{TUR}!70!black] at ({B9[0]/2:.3f},{B9[1]/2:.3f}) {{$50$ km}};
\\draw[thick,-{{Stealth}}] (0.45,0) arc (0:120:0.45); \\node at (0.0,0.95) {{$120^\\circ$}};''')
Q('0009','trg-ucgen','orta','Kosinüs Teoremi','Kosinüs teoremini rota problemine uygulayıp iki nokta arasındaki uzaklığı bulur.','hikâyeli',
 'Bir limandan aynı anda ayrılan iki gemi düz rotalarda ilerliyor. Şekilde, bir süre sonra gemilerin A ve B konumları, limandan alınan yollar ve rotalar arasındaki açı gösterilmiştir.\nBuna göre bu anda iki gemi arasındaki uzaklık kaç km dir?',
 ('70',70.0),
 [('20',20.0,'Uzaklığı alınan yolların farkı olarak almış: 50 − 30.','dikkat'),
  ('10√19',10*math.sqrt(19),'Kosinüs teoreminde cos120° yerine +1/2 kullanmış: √(900 + 2500 − 1500).','islem'),
  ('10√34',10*math.sqrt(34),'Açıyı 90° kabul edip Pisagor uygulamış: √(900 + 2500).','bilgi'),
  ('80',80.0,'Uzaklığı alınan yolların toplamı olarak almış: 30 + 50.','dikkat')],
 'İki gemi arasındaki uzaklık (km).',['Şekilde iki kenarı ve aralarındaki açıyı okuyabildiğin üçgenin hangi teoremle çözüleceğini düşün.'],[B_KOS],
 [A('Teoremi seç','İki kenar ve aralarındaki açı bilindiğinden kosinüs teoremi kullanılır.','|AB|² = 30² + 50² − 2 × 30 × 50 × cos120°'),
  A('cos120° değeri','120° II. bölgede, cos negatiftir.','cos120° = −1/2'),
  A('Hesapla','Sayılar yerine konur.','|AB|² = 900 + 2500 + 1500 = 4900'),
  A('Kökü al','Uzunluk pozitiftir.','|AB| = 70 km')],
 'Açının hangi bölgede olduğuna bak; işaret orada belirlenir.','K-ATR-06; 30 km, 50 km, 120°',sekil=SK)

# ================= 10 orta · sinüs teoremi (hikâyeli, şekilli) =================
AB=24; An,Bn=45,75; Cn=180-An-Bn; assert Cn==60
BC=AB*math.sin(R_(An))/math.sin(R_(Cn)); yak(BC,8*math.sqrt(6))
e10=[(18.0,'18'),(12*s3,'12√3'),(12*math.sqrt(6),'12√6'),(24*s2,'24√2')]
yak(AB*An/Cn,18); yak(AB*s3/2,12*s3); yak(AB*math.sin(R_(Cn))/math.sin(R_(An)),12*math.sqrt(6)); yak(AB*math.cos(R_(An))/math.cos(R_(Cn)),24*s2)
sc=0.2; Cx=AB*math.sin(R_(Bn))/math.sin(R_(Cn))*math.cos(R_(An))*sc; Cy=AB*math.sin(R_(Bn))/math.sin(R_(Cn))*math.sin(R_(An))*sc
SK=fig(f'''\\fill[{MAVI}!12] (0,0) -- ({AB*sc:.3f},0) -- ({Cx:.3f},{Cy:.3f}) -- cycle;
\\draw[very thick] (0,0) -- ({AB*sc:.3f},0) -- ({Cx:.3f},{Cy:.3f}) -- cycle;
\\fill (0,0) circle (2.2pt) node[below left] {{$A$}}; \\fill ({AB*sc:.3f},0) circle (2.2pt) node[below right] {{$B$}}; \\fill ({Cx:.3f},{Cy:.3f}) circle (2.2pt) node[above] {{$C$ (ada)}};
\\node[below] at ({AB*sc/2:.3f},0) {{$24$ m}};
\\draw[thick,-{{Stealth}}] (0.75,0) arc (0:45:0.75); \\node at (1.12,0.27) {{$45^\\circ$}};
\\draw[thick,-{{Stealth}}] ({AB*sc-0.7:.3f},0) arc (180:105:0.7); \\node at ({AB*sc-1.05:.3f},0.45) {{$75^\\circ$}};
\\node[right,{TUR}!70!black] at ({(AB*sc+Cx)/2:.3f},{Cy/2:.3f}) {{$|BC|=?$}};''')
Q('0010','trg-ucgen','orta','Sinüs Teoremi','Üçüncü açıyı bularak sinüs teoremiyle karşıdaki kenarın uzunluğunu hesaplar.','hikâyeli',
 'Bir göl kıyısındaki A ve B noktalarından, gölün içindeki küçük bir adada bulunan C noktası gözleniyor. Şekilde, A ve B arasındaki uzaklık ile bu noktalardan C’ye bakış açıları gösterilmiştir.\nBuna göre C noktasının B noktasına uzaklığı olan |BC| kaç metredir?',
 ('8√6',BC),
 [('18',18.0,'Kenarların açılarla doğru orantılı olduğunu sanmış: |BC| = 24 · 45/60.','bilgi'),
  ('12√3',12*s3,'Teorem yerine yalnız |AB| · sin60° çarpımını almış.','bilgi'),
  ('12√6',12*math.sqrt(6),'Oranı ters kurmuş: |AB| · sin60° / sin45°.','islem'),
  ('24√2',24*s2,'sin yerine cos kullanmış: 24 · cos45° / cos60°.','islem')],
 '|BC| uzunluğu (m).',['Bilinen kenarın karşısındaki açıyı önce bulman gerekebilir; sonra kenar–karşı açı eşleşmesini kur.'],[B_SIN],
 [A('Üçüncü açı','Üçgenin iç açıları toplamı 180°’dir.','C = 180° − 45° − 75° = 60°'),
  A('Eşleşmeyi kur','|AB| C’nin, |BC| A’nın karşısındadır.','|BC| / sin45° = 24 / sin60°'),
  A('Değerleri yaz','sin45° = √2/2, sin60° = √3/2.','|BC| = 24 × (√2/2) ÷ (√3/2) = 24√2/√3'),
  A('Sadeleştir','Payda √3 ile genişletilir.','|BC| = 24√6/3 = 8√6')],
 'Sinüs teoreminde kenarı kendi karşısındaki açıyla eşle; bilinen iki açı üçüncüyü verir.','K-ATR-06; A = 45°, B = 75°, |AB| = 24',sekil=SK)

# ================= 11 orta · öncüllü toplam–fark (düz) =================
t75=math.tan(R_(75)); t15=math.tan(R_(15))
yak(math.sin(R_(75)),math.cos(R_(15))); yak(math.sin(R_(15))*math.cos(R_(15)),0.25); assert abs(t75+t15-2*s3)>0.5; yak(t75+t15,4); yak(t75-t15,2*s3)
Q('0011','trg-toplamfark','orta','Toplam–Fark ve İki Kat Açı','Özel açılar üzerinde toplam–fark ve iki kat açı formüllerini kullanarak öncülleri değerlendirir.','öncüllü',
 'I. sin75° = cos15°\nII. sin15° · cos15° = 1/4\nIII. tan75° + tan15° = 2√3\nBu öncüllerden hangileri doğrudur?',
 ('I ve II',3),
 [('Yalnız I',1,'II’de sin15° · cos15° = sin30° = 1/2 almış (2 ile çarpmayı unutmuş); III’ü de yanlış bulmuş.','islem'),
  ('Yalnız II',2,'sin75° = sin15° sanıp I’i yanlış bulmuş; II’yi doğru, III’ü yanlış değerlendirmiş.','bilgi'),
  ('II ve III',4,'sin75° = sin15° sanıp I’i yanlış bulmuş ve tan75° − tan15° = 2√3 farkını toplam sanarak III’ü doğru bulmuş.','bilgi'),
  ('I, II ve III',5,'I ve II’yi doğru değerlendirmiş; tan75° − tan15° = 2√3 farkını toplam sanarak III’ü de doğru bulmuş.','islem')],
 'Doğru olan öncüllerin hangileri olduğu.',['Üç öncülü ayrı ayrı sına; 75° = 90° − 15° ve 15° gibi özel açılarla ilişkilendirilebilecek yolları dene.'],[B_TOP,B_IKI],
 [A('I’i incele','75° ile 15° birbirinin tümleyenidir.','sin75° = sin(90° − 15°) = cos15° → I doğru'),
  A('II’yi incele','sin2x = 2sinx·cosx formülü x = 15° için kullanılır.','sin15° · cos15° = sin30°/2 = 1/4 → II doğru'),
  A('III’ü incele','tan75° = 2 + √3, tan15° = 2 − √3.','tan75° + tan15° = 4 ≠ 2√3 → III yanlış'),
  A('Sonuç','Doğru olanlar I ve II’dir.','I ve II')],
 'Çarpım biçimindeki ifadeleri tek bir trigonometrik orana çevirmenin yolunu ara.','K-ATR-07; sin75°, sin15°·cos15°, tan75° + tan15°',
 sira=['Yalnız I','Yalnız II','I ve II','II ve III','I, II ve III'])

# ================= 12 orta · ızgarada tan(α−β) (şekilli) =================
Pq=(3,1); Qq=(2,1)
cross=Pq[0]*Qq[1]-Pq[1]*Qq[0]; dot=Pq[0]*Qq[0]+Pq[1]*Qq[1]; v12=Fr(abs(cross),dot); assert v12==Fr(1,7)
ta,tb=Fr(1,2),Fr(1,3); assert (ta-tb)/(1+ta*tb)==v12
e12=[ta-tb, (ta-tb)/(1-ta*tb), ta+tb, (ta+tb)/(1-ta*tb)]; assert e12==[Fr(1,6),Fr(1,5),Fr(5,6),Fr(1)]
g=['\\begin{scope}[scale=1.5]']
for i in range(0,5): g.append(f'\\draw[gray!45] ({i},0) -- ({i},2);')
for j in range(0,3): g.append(f'\\draw[gray!45] (0,{j}) -- (4,{j});')
aq,ap=math.degrees(math.atan(1/2)),math.degrees(math.atan(1/3))
g.append(f'\\fill[{TUR}!25] (0,0) -- ({2.0*math.cos(R_(ap)):.3f},{2.0*math.sin(R_(ap)):.3f}) arc ({ap:.2f}:{aq:.2f}:2.0) -- cycle;')
g.append(f'\\draw[{MAVI},very thick] (0,0) -- (2,1); \\draw[{TUR},very thick] (0,0) -- (3,1); \\draw[very thick] (0,0) -- (4,0);')
g.append(f'\\fill (0,0) circle (1.4pt) node[below left] {{$O$}}; \\fill (2,1) circle (1.5pt) node[above=1pt] {{$Q$}}; \\fill (3,1) circle (1.5pt) node[above right=0pt] {{$P$}};')
g.append(f'\\node[font=\\scriptsize] at ({1.5*math.cos(R_((ap+aq)/2)):.3f},{1.5*math.sin(R_((ap+aq)/2)):.3f}) {{$\\theta$}};')
g.append('\\end{scope}')
SK=fig('\n'.join(g)+'\n',font='\\footnotesize')
Q('0012','trg-toplamfark','orta','Izgarada Açı Farkının Tanjantı','Izgaradaki noktaların koordinatlarından iki açının tanjantını bulup fark formülünü uygular.','şekilli',
 'Şekilde, birim karelerden oluşan bir ızgara üzerinde O köşesinden çıkan OP ve OQ doğru parçaları çizilmiştir. P ve Q noktaları ızgara köşeleridir ve m(POQ) = θ dır.\nBuna göre tanθ değeri kaçtır?',
 (fs(v12),float(v12)),
 [(fs(e12[0]),float(e12[0]),'Fark formülünün paydasını atlayıp yalnız tanα − tanβ almış: 1/2 − 1/3.','bilgi'),
  (fs(e12[1]),float(e12[1]),'Paydada 1 − tanα·tanβ almış (işareti ters): (1/6) / (5/6).','islem'),
  (fs(e12[2]),float(e12[2]),'Fark yerine toplam almış: 1/2 + 1/3.','dikkat'),
  (fs(e12[3]),float(e12[3]),'tan(α + β) formülünü kullanmış: (5/6) / (5/6).','bilgi')],
 'tanθ değeri.',['OP ve OQ doğru parçalarının x ekseniyle yaptığı açıları ızgaradan okuyabildiğin dik üçgenlerle düşün; θ bu iki açının ilişkisi olarak yazılabilir.'],[B_TOP],
 [A('Açıları tanımla','OQ ve OP’nin x ekseniyle yaptığı açılar α ve β olsun; ızgaradan tanjantları okunur.','tanα = 1/2 (Q) · tanβ = 1/3 (P)'),
  A('θ’yı yaz','θ, iki açının farkıdır.','θ = α − β'),
  A('Fark formülünü uygula','tan(α − β) = (tanα − tanβ)/(1 + tanα·tanβ).','(1/2 − 1/3) / (1 + 1/6)'),
  A('Hesapla','Pay 1/6, payda 7/6’dır.','tanθ = (1/6) ÷ (7/6) = 1/7')],
 'θ’yı iki ışının x eksenine göre açılarıyla ilişkilendir.','K-ATR-07; ızgara üzerinde (3,1) ve (2,1)',sekil=SK)

# ================= 13 orta · sinx − cosx verilmiş, sin2x (düz) =================
v13=Fr(8,9); assert 1-2*Fr(4,9)==Fr(1,9) and 2*Fr(4,9)==v13
sol=[i/100000 for i in range(1,157079) if abs(math.sin(i/100000)-math.cos(i/100000)-1/3)<2e-5]; assert sol
yak(math.sin(2*sol[len(sol)//2]),8/9,2e-4)
e13=[Fr(-8,9),Fr(1,9),Fr(4,9),Fr(2,3)]
assert Fr(1,9)==1+e13[0] and Fr(1,9)==e13[1] and e13[2]==Fr(8,9)/2 and e13[3]==2*Fr(1,3)
Q('0013','trg-ikikat','orta','İki Kat Açı ve Özdeşlik','Verilen sinx − cosx değerinin karesinden iki kat açının sinüsünü hesaplar.','düz',
 '0 < x < π/2 olmak üzere, sinx − cosx = 1/3 olduğuna göre sin2x değeri kaçtır?',
 (fs(v13),float(v13)),
 [(fs(e13[0]),float(e13[0]),'(sinx − cosx)² açılımında −2sinx·cosx terimini +sin2x olarak yazmış: 1 + sin2x = 1/9.','islem'),
  (fs(e13[1]),float(e13[1]),'Eşitliğin karesi olan 1/9 değerini doğrudan sin2x sanmış.','dikkat'),
  (fs(e13[2]),float(e13[2]),'1 − 2sinx·cosx = 1/9 denkleminden sinx·cosx = 4/9’u bulup 2 ile çarpmayı unutmuş.','islem'),
  (fs(e13[3]),float(e13[3]),'sin2x = 2(sinx − cosx) = 2/3 yazmış.','bilgi')],
 'sin2x değeri.',['sinx − cosx ifadesi ile sin2x arasında nasıl bir köprü kurulabileceğini düşün.'],[B_IKI],
 [A('Karesini al','Her iki taraf kare alınır.','(sinx − cosx)² = 1/9'),
  A('Açılımı yaz','sin²x + cos²x = 1 ve 2sinx·cosx = sin2x kullanılır.','1 − 2sinx·cosx = 1/9 → 1 − sin2x = 1/9'),
  A('sin2x’i çöz','Eşitlik sin2x için çözülür.','sin2x = 1 − 1/9 = 8/9')],
 'Verilen ifade ile sin2x arasında nasıl bir köprü kurulabileceğini düşün.','K-ATR-08; sinx − cosx = 1/3, sin2x')

# ================= 14 orta · tablo, gelgit modeli (tablo) =================
h14=lambda t:6+2*math.cos(pi*t/6)
tab=[(0,8),(3,6),(6,4),(9,6),(12,8)]
for t,h in tab: yak(h14(t),h)
assert [t for t in range(1,13) if abs(h14(t)-7)<1e-9]==[2,10]
assert abs(math.cos(pi/3)-0.5)<1e-9 and abs(math.cos(2*pi/3)+0.5)<1e-9
SK=tablo_svg(['t (saat)','h (m)'],[[str(t),str(h)] for t,h in tab])
Q('0014','trg-model','orta','Gelgit Modeli','Tablodaki değerlerden kosinüs modelini kurup verilen yüksekliğe ulaşılan en erken zamanı trigonometrik denklemle bulur.','tablo',
 'Bir liman girişinde deniz tabanından su yüzeyine olan yükseklik, ölçümün başlamasından t saat sonra h(t) = a + b·cos(ct) metre kuralına göre değişiyor. Burada a, b ve c pozitif gerçel sayılardır ve değişim her 12 saatte bir kendini tekrarlamaktadır. Aşağıdaki tabloda bazı saatlerdeki h değerleri verilmiştir.\nBuna göre su yüksekliğinin ilk kez 7 metre olduğu an, ölçümün başlamasından kaç saat sonradır?',
 ('2',2.0),
 [('1',1.0,'cos(πt/6) = 1/2 için πt/6 = π/6 almış (30° ile 60°’yi karıştırmış): t = 1.','bilgi'),
  ('3',3.0,'Tabloda h = 6 olan t = 3 anını 7 metreye yakın bularak seçmiş.','dikkat'),
  ('4',4.0,'cos(πt/6) = 1/2 yerine −1/2 almış (işaret hatası): πt/6 = 2π/3.','islem'),
  ('6',6.0,'Tabloda en küçük değer olan t = 6 anını seçmiş.','dikkat')],
 'h değerinin ilk kez 7 olduğu t anı (saat).',['Tablodaki değerlerden sabitleri belirleyip kuralı yaz; sonra h = 7 eşitliğinin cos için ne dediğine bak.'],[B_TAB],
 [A('a ve b’yi bul','Değerler 4 ile 8 arasında değişir; ortası a, farkın yarısı b’dir.','a = (8 + 4)/2 = 6 · b = (8 − 4)/2 = 2'),
  A('c’yi bul','Periyot 12 saattir.','2π/c = 12 → c = π/6'),
  A('Denklemi kur','h(t) = 7 yazılır.','6 + 2cos(πt/6) = 7 → cos(πt/6) = 1/2'),
  A('En küçük pozitif kök','cosθ = 1/2 için en küçük pozitif θ = π/3’tür.','πt/6 = π/3 → t = 2')],
 'Model kurulunca tablo bir kenara bırakılır; istenen değer denklem olarak yazılır.','K-ATR-05; 6 + 2cos(πt/6), h = 7',sekil=SK)

# ================= 15 zor · yarım çemberde dikdörtgen (şekilli) =================
sn15,cs15=Fr(3,5),Fr(4,5); assert 2*sn15*cs15==Fr(24,25) and cs15**2*2-1==Fr(7,25)
v15=2*(2*cs15+sn15); assert v15==Fr(22,5)
e15=[2*(2*sn15+cs15), 2*cs15+sn15, 2*(cs15+sn15), 4*cs15+sn15*2*0+sn15]; assert e15==[4,Fr(11,5),Fr(14,5),Fr(19,5)]
yak(float(4*cs15+sn15),3.8)
R15=2.4; cx,cy=R15*0.8,R15*0.6
SK=fig(f'''\\draw[thick] ({R15:.2f},0) arc (0:180:{R15}); \\draw[thick] (-{R15:.2f},0) -- ({R15:.2f},0);
\\fill[{YES}!22] (-{cx:.3f},0) rectangle ({cx:.3f},{cy:.3f}); \\draw[{YES}!60!black,very thick] (-{cx:.3f},0) rectangle ({cx:.3f},{cy:.3f});
\\draw[thick] (0,0) -- ({cx:.3f},{cy:.3f});
\\fill ({cx:.3f},{cy:.3f}) circle (2.2pt) node[above right] {{$C$}}; \\fill (-{cx:.3f},{cy:.3f}) circle (2.2pt) node[above left] {{$D$}};
\\fill (-{cx:.3f},0) circle (2pt) node[below left] {{$A$}}; \\fill ({cx:.3f},0) circle (2pt) node[below right] {{$B$}}; \\fill (0,0) circle (2pt) node[below] {{$O$}};
\\draw[thick,-{{Stealth}}] (0.55,0) arc (0:36.87:0.55); \\node at (0.82,0.17) {{$x$}};
\\node[above,font=\\footnotesize] at (0,{R15+0.05:.2f}) {{Yarıçap $=1$ br}};
\\node[align=center,font=\\footnotesize] at (0,{cy/2:.3f}) {{Alan$(ABCD)$\\\\$=\\dfrac{{24}}{{25}}$ br$^2$}};''')
Q('0015','trg-ikikat','zor','Yarım Çemberde Dikdörtgen','Çember içine yerleşen dikdörtgenin kenarlarını sinx ve cosx ile ifade edip alandan çevreyi hesaplar.','şekilli',
 'Şekilde, O merkezli ve yarıçapı 1 birim olan yarım çember ile köşeleri A, B, C, D olan ABCD dikdörtgeni gösterilmiştir. A, O, B noktaları doğrusal, C ve D noktaları yarım çember üzerindedir, O noktası [AB] nin orta noktasıdır ve m(BOC) = x, 0 < x < π/4 tür. Dikdörtgenin alanı şekilde verilmiştir.\nBuna göre ABCD dikdörtgeninin çevresi kaç birimdir?',
 (fs(v15),float(v15)),
 [(fs(e15[1]),float(e15[1]),'Çevreyi kenarların toplamı olan 2cosx + sinx sanmış, sondaki 2 ile çarpmayı unutmuş.','islem'),
  (fs(e15[2]),float(e15[2]),'Uzun kenarı cosx almış (2cosx yerine): 2(4/5 + 3/5).','islem'),
  (fs(e15[3]),float(e15[3]),'Kısa kenarı bir kez sayıp 4cosx + sinx yazmış.','dikkat'),
  (fs(e15[0]),float(e15[0]),'0 < x < π/4 koşulunu atlamış, sinx = 4/5, cosx = 3/5 almış: 2(6/5 + 4/5).','dikkat')],
 'ABCD dikdörtgeninin çevresi.',['C noktasının koordinatlarını x cinsinden yazıp dikdörtgenin kenarlarını bu koordinatlarla ifade et; sonra alandan hangi iki kat açı ifadesi çıkacağını bak.'],[B_IKI],
 [A('Kenarları yaz','C(cosx, sinx) olduğundan genişlik 2cosx, yükseklik sinx’tir.','Alan = 2cosx · sinx = sin2x'),
  A('sin2x’ten cos2x’i bul','sin2x = 24/25 ve 2x < π/2 olduğundan cos2x pozitiftir.','cos2x = √(1 − 576/625) = 7/25'),
  A('cosx ve sinx’i bul','cos2x = 2cos²x − 1 ve 1 − 2sin²x kullanılır.','cosx = 4/5 · sinx = 3/5'),
  A('Çevreyi hesapla','Çevre = 2(2cosx + sinx).','2 × (8/5 + 3/5) = 22/5')],
 'Alan sin2x’e dönüşünce cos2x’ten tek tek sinx ve cosx’e geri dönmek gerekir; aralık koşulu hangisinin büyük olduğunu söyler.','K-ATR-08; yarım çemberde dikdörtgen, alan 24/25',sekil=SK,
 sira=None)

# ================= 16 zor · 2sin²x + cosx = 1, kesişim toplamı (grafik) =================
f16=lambda x:2*math.sin(x)**2+math.cos(x)
kok16=[0,2*pi/3,4*pi/3,2*pi]
for r in kok16: yak(f16(r),1)
assert all(abs(f16(i*2*pi/3000)-1)>1e-6 for i in range(1,3000) if abs(i*2*pi/3000-2*pi/3)>1e-3 and abs(i*2*pi/3000-4*pi/3)>1e-3)
yak(sum(kok16),4*pi)
e16=[('2π',2*pi),('3π',3*pi),('5π',5*pi),('6π',6*pi)]
yak(2*pi/3+4*pi/3,2*pi); yak(pi/3+5*pi/3+pi,3*pi); yak(pi+2*pi/3+4*pi/3+2*pi,5*pi); yak(2*pi+2*pi+2*pi/3+4*pi/3,6*pi)
kx16=0.88; ky16=0.8
def X16(x): return x*kx16
g=[f'\\draw[gray!35,thin] ({X16(i*pi/2):.3f},{-1.2*ky16:.3f}) -- ({X16(i*pi/2):.3f},{2.2*ky16:.3f});' for i in range(1,5)]
g+=[f'\\draw[gray!35,thin] (0,{j*ky16:.3f}) -- ({X16(2*pi)+0.2:.3f},{j*ky16:.3f});' for j in (-1,1,2)]
g.append(f'\\draw[-{{Stealth}},thick] (-0.1,0) -- ({X16(2*pi)+0.8:.3f},0) node[right] {{$x$}};')
g.append(f'\\draw[-{{Stealth}},thick] (0,{-1.35*ky16:.3f}) -- (0,{2.9*ky16:.3f}) node[above] {{$y$}};')
for j in (-1,1,2): g.append(f'\\node[left=2pt,font=\\footnotesize] at (0,{j*ky16:.3f}) {{${j}$}};')
for i,t in ((1,'\\frac{\\pi}{2}'),(2,'\\pi'),(3,'\\frac{3\\pi}{2}'),(4,'2\\pi')): g.append(f'\\node[below=1pt,font=\\scriptsize,fill=white,inner sep=0.3pt] at ({X16(i*pi/2):.3f},{-1.2*ky16:.3f}) {{${t}$}};')
g.append(f'\\draw[{TUR},very thick,dashed] (0,{ky16:.3f}) -- ({X16(2*pi)+0.35:.3f},{ky16:.3f}) node[right,{TUR}!70!black] {{$y=1$}};')
g.append(f'\\draw[{MAVI},very thick,smooth,domain=0:{2*pi:.4f},samples=90,variable=\\t] plot ({{\\t*{kx16}}},{{(2*(sin(\\t r))^2+cos(\\t r))*{ky16}}});')
for nm,r,pos in (('A',0,'above right'),('B',2*pi/3,'above'),('C',4*pi/3,'above'),('D',2*pi,'above left')):
    g.append(f'\\fill[{MOR}] ({X16(r):.3f},{ky16:.3f}) circle (2.4pt) node[{pos},black] {{$' + nm + '$};')
g.append(f'\\node[{MAVI}!80!black,above=1pt] at ({X16(1.318):.3f},{2.13*ky16:.3f}) {{$y=f(x)$}};')
SK=fig('\n'.join(g),font='\\footnotesize')
Q('0016','trg-denklem','zor','Trigonometrik Denklem ve Kök Toplamı','İkinci dereceden trigonometrik denklemi kosinüse indirgeyip verilen aralıktaki köklerin toplamını bulur.','grafik',
 'Şekilde, 0 ≤ x ≤ 2π için f(x) = 2sin²x + cosx fonksiyonunun grafiği ile y = 1 doğrusu ve bunların kesişim noktaları olan A, B, C, D noktaları gösterilmiştir.\nBuna göre A, B, C ve D noktalarının apsisleri toplamı kaçtır?',
 ('4π',4*pi),
 [(e16[0][0],e16[0][1],'cosx = 1 kökleri olan x = 0 ve x = 2π’yi atlayıp yalnız 2π/3 ve 4π/3’ü toplamış.','dikkat'),
  (e16[1][0],e16[1][1],'Çarpanlara ayırırken işareti hata yapıp 2cos²x + cosx − 1 = 0 çözmüş: x = π/3, 5π/3 ve π köklerini toplamış.','islem'),
  (e16[2][0],e16[2][1],'cosx = 1 denkleminin köklerini x = π ve 2π almış: π + 2π + 2π/3 + 4π/3.','bilgi'),
  (e16[3][0],e16[3][1],'x = 0 kökünü 2π ile aynı sayıp 2π’yi iki kez eklemiş: 2π + 2π + 2π/3 + 4π/3.','dikkat')],
 'Dört kesişim noktasının apsisleri toplamı.',['Grafik üzerindeki kesişimler denklemin kökleridir; sin²x yerine cos cinsinden bir ifade yazarak denklemi tek bir fonksiyona indirgemeyi dene.'],[B_DEN],
 [A('Denklemi kur','Kesişimlerde f(x) = 1 olur.','2sin²x + cosx = 1'),
  A('Kosinüse indirge','sin²x = 1 − cos²x yazılır.','2 − 2cos²x + cosx = 1 → 2cos²x − cosx − 1 = 0'),
  A('Çarpanlara ayır','Denklem iki çarpana ayrılır.','(2cosx + 1)(cosx − 1) = 0 → cosx = −1/2 ya da cosx = 1'),
  A('Kökleri bul','[0, 2π] aralığında kökler yazılır.','x = 2π/3, 4π/3 · x = 0, 2π'),
  A('Topla','Dört kök toplanır.','2π/3 + 4π/3 + 0 + 2π = 4π')],
 'Karma denklemde sin² görünce cos cinsine geç; kökleri toplarken aralığın uç noktalarını unutma.','K-ATR-09; 2sin²x + cosx = 1, [0, 2π]',sekil=SK)

# ================= 17 zor · iki dik üçgen, tan(α+β) (şekilli) =================
tA=Fr(3,4); tB=Fr(12,5); v17=(tA+tB)/(1-tA*tB); assert v17==Fr(-63,16)
e17=[Fr(-16,63),Fr(33,56),Fr(63,20),Fr(63,16)]
assert 1/v17==e17[0] and (tB-tA)/(1+tA*tB)==e17[1] and tA+tB==e17[2] and (tA+tB)/(tA*tB-1)==e17[3]
sc17=0.4
g=[]
# üçgen 1: yatay kenar 4, düşey 3, hipotenüs 5; α sol alt köşede (karşısı 3)
g.append(f'\\fill[{MAVI}!15] (0,0) -- ({4*sc17},0) -- ({4*sc17},{3*sc17}) -- cycle; \\draw[very thick,{MAVI}] (0,0) -- ({4*sc17},0) -- ({4*sc17},{3*sc17}) -- cycle;')
g.append(f'\\draw ({4*sc17-0.2},0) -- ({4*sc17-0.2},0.2) -- ({4*sc17},0.2);')
g.append(f'\\node[above left=-2pt] at ({2*sc17},{1.5*sc17}) {{$5$}}; \\node[right] at ({4*sc17},{1.5*sc17}) {{$3$}};')
g.append(f'\\draw[thick,-{{Stealth}}] (0.55,0) arc (0:36.87:0.55); \\node at (0.82,0.16) {{$\\alpha$}};')
ox=3.6
# üçgen 2: yatay kenar 5, düşey 12, hipotenüs 13; β sağ alt köşede... β yatay kenara komşu, yatay=5
g.append(f'\\fill[{TUR}!18] ({ox},0) -- ({ox+5*sc17},0) -- ({ox+5*sc17},{12*sc17}) -- cycle; \\draw[very thick,{TUR}] ({ox},0) -- ({ox+5*sc17},0) -- ({ox+5*sc17},{12*sc17}) -- cycle;')
g.append(f'\\draw ({ox+5*sc17-0.2},0) -- ({ox+5*sc17-0.2},0.2) -- ({ox+5*sc17},0.2);')
g.append(f'\\node[above left=-2pt] at ({ox+2.5*sc17},{6*sc17}) {{$13$}}; \\node[below] at ({ox+2.5*sc17},0) {{$5$}};')
g.append(f'\\draw[thick,-{{Stealth}}] ({ox+0.55},0) arc (0:67.38:0.55); \\node at ({ox+0.9},0.35) {{$\\beta$}};')
SK=fig('\n'.join(g))
Q('0017','trg-toplamfark','orta','İki Açının Toplamının Tanjantı','Dik üçgenlerden iki açının tanjantını bulup toplam formülüyle tan(α + β) değerini hesaplar.','şekilli',
 'Şekilde, iki dik üçgen ile bunların bazı kenar uzunlukları ve α, β dar açıları gösterilmiştir.\nBuna göre tan(α + β) değeri kaçtır?',
 (fs(v17),float(v17)),
 [(fs(e17[0]),float(e17[0]),'tan(α + β) yerine cot(α + β) değerini yani çarpmaya göre tersini almış.','dikkat'),
  (fs(e17[1]),float(e17[1]),'Toplam yerine fark formülünü uygulamış: tan(β − α).','bilgi'),
  (fs(e17[2]),float(e17[2]),'Yalnız payı (tanα + tanβ) hesaplayıp paydayı yazmamış.','bilgi'),
  (fs(e17[3]),float(e17[3]),'Paydayı tanα·tanβ − 1 olarak yazıp işareti ters çevirmiş.','islem')],
 'tan(α + β) değeri.',['Her dik üçgende bilinmeyen dik kenarı bulmak için hangi teoremin gerekeceğini düşün; sonra α ve β için hangi iki oranın lazım olduğuna karar ver.'],[B_TOP,B_TNJ],
 [A('Eksik kenarları bul','Pisagor teoremi iki üçgene ayrı uygulanır.','Üçgen 1: √(25 − 9) = 4 · Üçgen 2: √(169 − 25) = 12'),
  A('Tanjantları yaz','α’nın karşısı 3, komşusu 4; β’nın karşısı 12, komşusu 5.','tanα = 3/4 · tanβ = 12/5'),
  A('Toplam formülünü uygula','tan(α + β) = (tanα + tanβ)/(1 − tanα·tanβ).','(3/4 + 12/5) / (1 − 9/5)'),
  A('Hesapla','Pay 63/20, payda −16/20’dir.','tan(α + β) = (63/20) ÷ (−16/20) = −63/16')],
 'Toplam formülünde payda 1’den küçüklenirse sonuç negatif çıkar; bu, α + β’nın 90°’yi aştığını gösterir.','K-ATR-07; 3-4-5 ve 5-12-13 üçgenleri',sekil=SK)

# ================= 18 zor · dönme dolap modeli (grafik, hikâyeli) =================
h18=lambda t:10-8*math.cos(pi*t/15)
yak(h18(0),2); yak(h18(15),18); yak(h18(30),2)
ust=[t/1000 for t in range(0,30001) if h18(t/1000)>=14-1e-9]; assert abs((max(ust)-min(ust))-10)<1e-2 and abs(min(ust)-10)<1e-2 and abs(max(ust)-20)<1e-2
yak(10-8*math.cos(2*pi*5/15),14); yak(10-8*math.cos(pi*7.5/15),10);
e18=[('5',5.0),('15',15.0),('20',20.0),('25',25.0)]
kx18=0.19; ky18=0.22
g=[f'\\draw[gray!35,thin] ({i*5*kx18:.3f},0) -- ({i*5*kx18:.3f},{18*ky18:.3f});' for i in range(1,7)]
g+=[f'\\draw[gray!35,thin] (0,{j*ky18:.3f}) -- ({30*kx18+0.2:.3f},{j*ky18:.3f});' for j in (2,10,18)]
g.append(f'\\draw[-{{Stealth}},thick] (-0.1,0) -- ({30*kx18+0.85:.3f},0) node[right] {{$t$ (s)}};')
g.append(f'\\draw[-{{Stealth}},thick] (0,-0.1) -- (0,{19.5*ky18+0.3:.3f}) node[above] {{$h$ (m)}};')
for j in (2,10,18): g.append(f'\\node[left=2pt,font=\\footnotesize] at (0,{j*ky18:.3f}) {{${j}$}};')
for i in range(1,7): g.append(f'\\node[below=1pt,font=\\footnotesize] at ({i*5*kx18:.3f},0) {{${i*5}$}};')
g.append(f'\\draw[{MAVI},very thick,smooth,domain=0:30,samples=70,variable=\\t] plot ({{\\t*{kx18}}},{{(10-8*cos(\\t*pi/15 r))*{ky18}}});')
g.append(f'\\fill[{TUR}] (0,{2*ky18:.3f}) circle (2.4pt); \\fill[{TUR}] ({15*kx18:.3f},{18*ky18:.3f}) circle (2.4pt) node[above=2pt,black] {{$(15,\\,18)$}}; \\fill[{TUR}] ({30*kx18:.3f},{2*ky18:.3f}) circle (2.4pt);')
SK=fig('\n'.join(g),font='\\footnotesize')
Q('0018','trg-model','zor','Dönme Dolap Modeli','Grafikten kosinüs modelini kurup yüksekliğin belirli bir değerin üzerinde kaldığı süreyi trigonometrik eşitsizlikle bulur.','hikâyeli',
 'Bir lunaparktaki dönme dolap, sabit hızla ve aynı yönde dönmektedir. Dolabın bir kabininin yerden yüksekliği, hareketin başlamasından t saniye sonra h(t) metredir. Şekilde, ilk tam turdaki h(t) grafiği ve grafiğin bazı noktaları gösterilmiştir.\nBuna göre bu kabin, bir tam turda yerden en az 14 metre yükseklikte kaç saniye bulunur?',
 ('10',10.0),
 [(e18[0][0],e18[0][1],'Yarım turun süresini (15 s) periyot sanmış: cos(2πt/15) ≤ −1/2 için yalnızca 5 saniye bulmuş.','bilgi'),
  (e18[1][0],e18[1][1],'h ≥ 14 yerine h ≥ 10 (cos ≤ 0) koşulunu çözmüş.','dikkat'),
  (e18[2][0],e18[2][1],'En az 14 m yerine en çok 14 m koşulunun süresini bulmuş: 30 − 10.','dikkat'),
  (e18[3][0],e18[3][1],'Yarım periyodu kullanıp 5 saniyeyi bulmuş, sonra bir tur olan 30 saniyeden çıkarmış: 30 − 5.','islem')],
 'Kabinin bir turda en az 14 m yükseklikte kaldığı süre (s).',['Grafikteki en küçük, en büyük değer ve tur süresinden önce h(t) kuralını yaz; sonra 14 m eşitliğini sağlayan zamanlara bak.'],[B_MOD],
 [A('Modelin sabitleri','En küçük 2, en büyük 18; tur süresi 30 s.','a = (18 + 2)/2 = 10 · b = (18 − 2)/2 = 8 · c = 2π/30 = π/15'),
  A('Kuralı yaz','En küçük değer t = 0’da olduğundan kosinüs eksi işaretlidir.','h(t) = 10 − 8cos(πt/15)'),
  A('Eşitsizliği kur','h ≥ 14 koşulu cos için çözülür.','10 − 8cos(πt/15) ≥ 14 → cos(πt/15) ≤ −1/2'),
  A('Aralığı bul','[0, 2π] içinde cosθ ≤ −1/2 için θ aralığı 2π/3 ile 4π/3 arasıdır.','2π/3 ≤ πt/15 ≤ 4π/3 → 10 ≤ t ≤ 20'),
  A('Süreyi hesapla','Aralığın uzunluğu bulunur.','20 − 10 = 10 s')],
 'Dönel harekette “en az” ya da “en çok” koşulu cos eşitsizliği verir; eşitsizlik yönünü eksi işaretli modelde kontrol et.','K-ATR-05; 10 − 8cos(πt/15), h ≥ 14',sekil=SK)

# ================= 19 zor · çevrel çember (şekilli) =================
a19,b19,c19=5,7,8
cosA=Fr(b19*0+c19**2+a19**2-b19**2,2*a19*c19); assert cosA==Fr(1,2)
R19=7/(2*(s3/2)); yak(R19,7*s3/3)
yak(b19*c19*a19/(4*0.5*a19*c19*math.sin(R_(60))),7*s3/3)
e19=[(7*s3/2,'7√3/2'),(7.0,'7'),(14*s3/3,'14√3/3'),(14.0,'14')]
yak(7*s3/2,6.062177826); yak(7/(2*0.5),7); yak(7/(s3/2),14*s3/3); yak(7/0.5,14)
Ax,Bx=0,8*0.5; Cx=5*0.5*0.5; Cy=5*0.5*(s3/2)
SK=fig(f'''\\fill[{YES}!15] (0,0) -- ({Bx:.3f},0) -- ({Cx:.3f},{Cy:.3f}) -- cycle; \\draw[very thick] (0,0) -- ({Bx:.3f},0) -- ({Cx:.3f},{Cy:.3f}) -- cycle;
\\fill (0,0) circle (2.2pt) node[below left] {{$A$}}; \\fill ({Bx:.3f},0) circle (2.2pt) node[below right] {{$B$}}; \\fill ({Cx:.3f},{Cy:.3f}) circle (2.2pt) node[above] {{$C$}};
\\node[below] at ({Bx/2:.3f},0) {{$8$}}; \\node[above left=-1pt] at ({Cx/2:.3f},{Cy/2:.3f}) {{$5$}}; \\node[above right=-1pt] at ({(Bx+Cx)/2:.3f},{Cy/2:.3f}) {{$7$}};''')
Q('0019','trg-ucgen','orta','Çevrel Çemberin Yarıçapı','Kosinüs teoremiyle bir açıyı bulup sinüs teoremiyle çevrel çemberin yarıçapını hesaplar.','şekilli',
 'Şekilde, kenar uzunlukları birim cinsinden verilen bir ABC üçgeni gösterilmiştir.\nBuna göre ABC üçgeninin çevrel çemberinin yarıçapı kaç birimdir?',
 ('7√3/3',R19),
 [(e19[0][1],e19[0][0],'Sinüs teoreminde a/sinA = 2R yerine R = a·sinA yazmış: 7 · √3/2.','bilgi'),
  (e19[1][1],e19[1][0],'A açısının sinüsünü 1/2 almış (cos ile karıştırmış): R = 7 / (2 · 1/2).','bilgi'),
  (e19[2][1],e19[2][0],'a/sinA = 2R değerini R sanmış: 7 / (√3/2) = 14√3/3.','islem'),
  (e19[3][1],e19[3][0],'sinA = 1/2 almış ve 2R yerine R yazmış: 7 / (1/2).','bilgi')],
 'Çevrel çemberin yarıçapı.',['Üç kenarı bilinen üçgende elde edilebilecek büyüklükler ile çevrel çember arasındaki ilişkiyi düşün.'],[B_KOS,B_SIN],
 [A('Açıyı bul','Kosinüs teoremi 7 kenarının karşısındaki A açısına uygulanır.','7² = 5² + 8² − 2 × 5 × 8 × cosA → cosA = 1/2'),
  A('A’yı belirle','A açısı üçgenin iç açısıdır, 0° ile 180° arasındadır.','A = 60° → sinA = √3/2'),
  A('Sinüs teoremini yaz','a/sinA = 2R.','7 ÷ (√3/2) = 2R'),
  A('R’yi çöz','Her iki taraf 2’ye bölünür ve payda sadeleştirilir.','R = 7/√3 = 7√3/3')],
 'Üç kenar bilinince bulunabilen büyüklüklerle çevrel çemberin ilişkisini düşün.','K-ATR-06; kenarlar 5, 7, 8',sekil=SK)

# ================= 20 zor · tanx + cotx = 4, sin⁴x + cos⁴x (düz) =================
v20=Fr(7,8); sc20=Fr(1,4)
assert sc20+1/sc20*0==sc20 and 1/sc20==4 and 1-2*sc20**2==v20
x20=[i/100000 for i in range(1,157079) if abs(math.tan(i/100000)+1/math.tan(i/100000)-4)<3e-4]; assert x20
xm=x20[len(x20)//2]; yak(math.sin(xm)**4+math.cos(xm)**4,7/8,2e-3)
e20=[Fr(1,16),Fr(1,8),Fr(3,4),Fr(15,16)]
assert sc20**2==e20[0] and 2*sc20**2==e20[1] and 1-4*sc20**2==Fr(3,4) and 1-sc20**2==e20[3]
Q('0020','trg-ikikat','orta','Özdeşlik ve Dördüncü Kuvvet','tanx + cotx toplamından sinx·cosx değerini bulup sin⁴x + cos⁴x ifadesini iki kat açı ve özdeşliklerle hesaplar.','düz',
 '0 < x < π/2 olmak üzere, tanx + cotx = 4 olduğuna göre sin⁴x + cos⁴x ifadesinin değeri kaçtır?',
 (fs(v20),float(v20)),
 [(fs(e20[0]),float(e20[0]),'Çarpımı bulduktan sonra (sinx·cosx)² = 1/16 değerinde bırakmış.','dikkat'),
  (fs(e20[1]),float(e20[1]),'Eksik terimi 1’den çıkarmayı unutup yalnız 2sin²x·cos²x = 1/8 değerini almış.','dikkat'),
  (fs(e20[2]),float(e20[2]),'sin⁴x + cos⁴x = 1 − 4sin²x·cos²x yazmış (2 yerine 4 almış).','islem'),
  (fs(e20[3]),float(e20[3]),'sin⁴x + cos⁴x = 1 − sin²x·cos²x yazmış (2 çarpanını unutmuş).','islem')],
 'sin⁴x + cos⁴x ifadesinin değeri.',['tanx ve cotx’i sinx ile cosx cinsinden yaz, ortak paydada topla; sonra dördüncü kuvvetleri 1’i kullanarak karesi alınmış bir ifadeye bağla.'],[B_IKI,B_TNJ],
 [A('Toplamı sadeleştir','tanx + cotx ortak paydada toplanır.','(sin²x + cos²x)/(sinx·cosx) = 1/(sinx·cosx) = 4'),
  A('Çarpımı bul','Eşitlikten çarpım çıkar.','sinx · cosx = 1/4'),
  A('Dördüncü kuvveti dönüştür','(sin²x + cos²x)² = 1 açılır.','sin⁴x + cos⁴x = 1 − 2sin²x·cos²x'),
  A('Değeri yaz','Çarpımın karesi yerine konur.','1 − 2 × (1/4)² = 1 − 1/8 = 7/8')],
 'Dördüncü kuvvetleri 1’e bağlayacak bir kare ifadesi ara.','K-ATR-08; tanx + cotx = 4',
 )

#<<SON>>
# ---------------- yaz ----------------
for q_ in P.ANA: q_['kardes']=None
from collections import Counter
tipler={}
for k_ in KART: tipler.setdefault(k_['tipId'],dict(tipId=k_['tipId'],ad=k_['tip'],kartlar=[],uygulamaKonu=UK))['kartlar'].append(k_['id'])
if len(P.ANA)==20:
    json.dump(P.ANA,open(os.path.join(HD,'trigo-1.json'),'w'),ensure_ascii=False,indent=1)
    json.dump(dict(konu='Trigonometri',surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT Matematik 2018–2026 çıkmış soruları ve yayın soru bankaları (yalnız mantık), MEB 11–12. sınıf müfredatı.',kartlar=KART,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar','trigo.json'),'w'),ensure_ascii=False,indent=1)
print(len(P.ANA),'soru · harfler',dict(sorted(Counter(q['cevap']['sik'] for q in P.ANA).items())),'· zorluk',dict(Counter(q['zorluk'] for q in P.ANA)),'· şekilli',sum(1 for q in P.ANA if q.get('sekil')),'· tip',len(tipler))
