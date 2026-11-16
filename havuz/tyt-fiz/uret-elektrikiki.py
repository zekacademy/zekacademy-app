"""TYT Fizik · Elektrik (ikinci genişletme) · 26 soru: elektrostatik ≈ 10, akım ve devreler ≈ 16.
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
P=Parti('elektrikiki','Elektrik','fiz|Elektrik',ders='TYT Fizik',idon='tytfiz')
KAYNAK='ÖSYM 2018–2026 TYT Fizik soruları (yalnız mantık) · MEB 9–10. sınıf fizik'
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small,circuitikz/bipoles/length=1.1cm]\n'
TAIL='\n\\end{tikzpicture}'
def tk(body): return tikz_svg(HEAD+body+TAIL)
def nn(no): return f'{int(no):02d}'
def kartk(no,alt,fikir,tuzak,z,kalip,adim,tipId,tip):
    kart(f'K-FZEL2-{nn(no)}',alt,fikir,tuzak,z,kalip,adim,tipId,tip,KAYNAK)

# ---------- sayısal soru ----------
def N(no,tipId,tip,alt,z,kaz,fikir,tuzak,metin,dogru,yan,istenen,ip,bilgi,ad,puf,sekil=None,kalip=None,sira=None):
    kalip=kalip or ('şekilli' if sekil else 'düz')
    kartk(no,alt,fikir,tuzak,z,kalip,len(ad),tipId,tip)
    mk(P,no,metin=metin,dogru=dogru,yan=yan,istenen=istenen,ad=ad,sekil=sekil,ip=ip,bilgi=bilgi,puf=puf,tipId=tipId,tip=tip,z=z,alt=alt,kaz=kaz,
       kalip=kalip,adim=len(ad),kart=f'K-FZEL2-{nn(no)} ({alt}) · yeni kurgu, ÖSYM mantığı',kisa=None,sira=sira)

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
       kalip=kalip,adim=len(ad),kart=f'K-FZEL2-{nn(no)} ({alt}) · yeni kurgu, ÖSYM mantığı')

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

# =====================================================================
# ELEKTROSTATİK (10)
# =====================================================================
# ---- 01 · Elektroskopta etkiyle yük ayrışması · öncüllü · orta ----
# I doğru: pozitif çubuk serbest elektronları topuza çeker → topuz −, yapraklar +. II yanlış: dokunma yok, toplam yük 0. III doğru: çubuk gidince yükler yeniden dağılır.
sk=tk(elsk(0,28)+cubuk(1.6,2.55,'+',w=1.7)+'\\node[font=\\small] at (1.6,3.2) {cam çubuk};')
O('0001','fz-el2-elektroskop-etki','Elektroskopa yaklaştırılan yüklü çubuk (etkiyle yük ayrışması)','Elektriklenme türleri','orta',
 'Yüklü bir cisim nötr bir elektroskopa dokunmadan yaklaştırıldığında oluşan yük dağılımını ve yaprakların davranışını yorumlar.',
 'Dokunmadan yaklaştırılan yüklü çubuk, iletkendeki serbest elektronları yer değiştirir; toplam yük değişmez, yükler ayrışır ve çubuk gidince geri döner.',
 'Yük ayrışmasını toplam yük değişimi sanmak; çubuk uzaklaşınca yaprakların açık kalacağını düşünmek.',
 'Yalıtkan bir ayak üzerinde duran nötr bir elektroskopun topuzuna, ipek kumaşa sürtülerek pozitif yüklenmiş bir cam çubuk, dokunmadan şekildeki gibi yaklaştırılıyor. Çubuk yaklaştırılırken elektroskopun yapraklarının açıldığı gözleniyor. Çubuk ile elektroskop arasında yük geçişi olmamakta, ortamda başka yüklü cisim bulunmamaktadır.',
 [('Topuz ile yapraklar zıt işaretli yüklenmiştir.',True,'Pozitif çubuk, iletken elektroskoptaki serbest elektronları topuza çeker: topuz negatif, yapraklar pozitif olur ve yapraklar birbirini iter.','Yük ayrışmasını fark etmeyip bütün elektroskopun çubukla aynı işaretli olduğunu düşünmüş.'),
  ('Elektroskop toplam olarak pozitif yüklenmiştir.',False,'Dokunma olmadığından elektroskopa yük girmemiş, çıkmamıştır; toplam yük sıfır kalır, yalnızca yükler yer değiştirir.','Yaprakların pozitif olmasını elektroskopun toplam yükünün pozitif olması sanmış.'),
  ('Cam çubuk uzaklaştırılırsa yapraklar kapanır.',True,'Elektronlar çubuğun etkisiyle yer değiştirmişti; çubuk gidince yeniden dağılır, elektroskop nötr kalır ve yapraklar sarkar.','Yük ayrışmasının kalıcı olduğunu düşünüp yaprakların açık kalacağını sanmış.')],
 ['Yalnız I','Yalnız II','I ve II','II ve III','I ve III'],
 ('Düzenekte çubuk topuza değmez; yapraklar çubuk varken açılır.','Dokunma yok → yük alışverişi yok'),
 ['Çubuğun topuza değmediğini ve elektroskopun toplam yükünün ne olduğunu düşünerek her yargıyı ayrı ayrı sına.'],
 [B('Etki ile yüklenme','yüklü cisim iletkene dokunmadan yaklaşırsa iletkenin toplam yükü değişmez; serbest elektronlar çubuğa göre yer değiştirir. Örnek: negatif çubuk yaklaşınca elektronlar uzak uca itilir'),
  B('Elektroskop','yapraklar aynı işaretli yüklenince birbirini iter ve açılır; yük miktarı arttıkça açıklık artar')],
 'Dokunmadan yaklaştırma yalnızca yükleri ayrıştırır; toplam yük ancak dokunma veya topraklamayla değişir.',sekil=sk)

# ---- 02 · Üç özdeş iletken kürede ardışık yük paylaşımı · sayısal · orta ----
qX,qY,qZ=12,-4,0
a1=Fr(qX+qY,2); assert a1==4          # X–Y dokunması
z2=(a1+qZ)/Fr(2); assert z2==2         # Y–Z dokunması → Z
e1=Fr(qY+qZ,2); assert e1==-2         # ilk aşamayı atlayıp Y'nin ilk yükünü Z ile paylaştırmış
e2=a1; assert e2==4                    # Y'nin yükünün tamamını Z'ye geçirmiş
e3=Fr(qX+qZ,2); assert e3==6           # X ile Z'yi dokundurmuş
e4=qX+qY; assert e4==8                 # yükleri paylaştırmadan toplamış
sk=(kure(0,0,.55,'$X$')+ayak(0,0,.55)+kure(2.6,0,.55,'$Y$')+ayak(2.6,0,.55)+kure(5.2,0,.55,'$Z$')+ayak(5.2,0,.55)+
    '\\node at (0,1.0) {$+12q$}; \\node at (2.6,1.0) {$-4q$}; \\node at (5.2,1.0) {nötr};')
N('0002','fz-el2-yuk-paylasim-uc','Üç özdeş iletken kürede ardışık yük paylaşımı','İletken kürelerde yük paylaşımı','orta',
 'Özdeş iletken kürelerin ardışık dokundurulmasında toplam yükün korunumunu ve eşit paylaşımı kullanarak son yükü bulur.',
 'Özdeş iletken kürelerde dokunduktan sonra toplam yük eşit paylaşılır; her aşamada yalnızca dokunan küreler hesaba katılır.',
 'Aşamaların sırasını karıştırmak; yükleri paylaştırmak yerine toplamak; bir küreyi dokunmamış olmasına rağmen hesaba katmak.',
 'Yalıtkan ayaklar üzerinde duran özdeş X, Y ve Z iletken kürelerinin yükleri şekilde verilmiştir. Önce X ile Y küreleri birbirine dokundurulup ayrılıyor; ardından Y ile Z küreleri birbirine dokundurulup ayrılıyor. Dokundurma sırasında küreler ortamla ve toprakla yük alışverişi yapmamaktadır.\nBuna göre, işlemler bittiğinde Z küresinin yükü kaç q olur?',
 2,[(-2,'İlk aşamayı (X–Y) hiç yapmamış gibi davranıp Y’nin başlangıç yükünü (−4q) Z ile paylaştırmış: (−4 + 0) ÷ 2 = −2q.','dikkat'),
    (4,'Y’nin ilk dokundurmadan sonraki yükünü (+4q) Z ile paylaşmak yerine tamamen Z’ye aktarmış.','bilgi'),
    (6,'İkinci aşamada Y yerine X küresini (+12q) Z ile dokundurmuş sanmış: (12 + 0) ÷ 2 = 6q.','dikkat'),
    (8,'Yükleri eşit paylaştırmak yerine cebirsel toplamış: 12 − 4 = 8q ve bunu Z’ye vermiş.','islem')],
 'Z küresinin son yükü (q cinsinden).',
 ['Her dokundurmadan sonra yalnızca dokunan iki kürenin yükleri eşitlenir; sırayla ilerle.'],
 [B('Yük paylaşımı','özdeş iletken küreler dokundurulup ayrılınca toplam yük korunur ve eşit paylaşılır. Örnek: +6q ile 0 yüklü küreler ayrılınca ikisi de +3q olur'),
  B('Yük işareti','zıt işaretli yükler toplanırken birbirini götürür; toplam, işaretli sayıların toplamıdır')],
 [A('X–Y dokunması','Toplam yük (+12q) + (−4q) = +8q, iki özdeş küre arasında eşit paylaşılır.','(12 − 4) ÷ 2 = +4q → X = Y = +4q'),
  A('Y’nin yeni yükü','Y küresi ikinci dokundurmaya +4q ile girer; Z nötrdür.','Y = +4q, Z = 0'),
  A('Y–Z dokunması','Toplam +4q iki küre arasında eşit paylaşılır.','(4 + 0) ÷ 2 = +2q'),
  A('Sonuç','Z küresinin yükü Y ile eşitlenmiştir.','Z = +2q')],
 'Ardışık dokundurmalarda her aşamada yalnızca dokunan küreler eşit paylaşır; yükün işaretini unutma.',sekil=tk(sk))

# ---- 03 · Etkiyle yükleme + topraklama · öncüllü · zor ----
# I: negatif çubuk elektronları iter, topraklama teliyle toprağa gider → doğru. II: tel kalkınca küre elektron eksikliğiyle pozitif kalır → doğru.
# III: tel kaldırılmadan çubuk uzaklaştırılırsa elektronlar topraktan geri gelir, küre nötr → yargı yanlış.
sk=(kure(2.4,1.2,.65)+ayak(2.4,1.2,.65)+cubuk(.55,1.2,'−',w=1.9)+
    '\\draw[thick] (3.05,1.2) -- (4.2,1.2) -- (4.2,.55); \\draw (4.2,.55) node[ground]{}; \\node[font=\\footnotesize] at (5.05,.95) {toprak teli};')
O('0003','fz-el2-etki-topraklama','Etkiyle yükleme ve topraklama sırası','Topraklama','zor',
 'Etki ile yüklemede çubuğun yaklaştırılması, topraklama ve bağlantının kesilmesi sırasına göre küredeki yük akışını ve son yükü yorumlar.',
 'Çubuk yerindeyken topraklanan küre, çubukla zıt işaretli yüklü kalır; topraklama kesilmeden çubuk çekilirse yük toprağa geri döner.',
 'Elektronların akış yönünü ters düşünmek; işlemlerin sırasını (çubuk-tel) gözetmemek.',
 'Yalıtkan ayak üzerindeki nötr metal küreye, negatif yüklü bir çubuk dokundurulmadan şekildeki gibi yaklaştırılıyor. Çubuk yerindeyken küre iletken bir telle toprağa bağlanıyor, bir süre sonra tel kürenin üzerinden alınıyor ve ancak bundan sonra çubuk uzaklaştırılıyor. Küre ile çubuk hiçbir aşamada birbirine değmemiştir.',
 [('Topraklama sırasında elektronlar küreden toprağa akar.',True,'Negatif çubuk, küredeki serbest elektronları kendinden uzağa iter; bu elektronlar toprak teliyle toprağa geçer.','Topraklamada pozitif yüklerin toprağa aktığını düşünmüş.'),
  ('Çubuk uzaklaştırıldıktan sonra küre pozitif yüklüdür.',True,'Tel alındığında küre elektron kaybetmiş durumdadır; çubuk gidince geriye elektron eksikliği, yani pozitif yük kalır.','Çubuğun uzaklaşmasıyla kürenin yeniden nötr olacağını sanmış.'),
  ('Çubuk, tel küreye bağlıyken uzaklaştırılsaydı küre pozitif yüklü kalırdı.',False,'Tel bağlıyken çubuk gidince toprağa geçen elektronlar küreye geri döner; küre nötr kalır.','Topraklamanın kalıcı pozitif yük bıraktığını, telin ne zaman alındığının önemsiz olduğunu düşünmüş.')],
 ['Yalnız I','Yalnız II','I ve II','II ve III','I, II ve III'],
 ('Sıra: çubuk yaklaştırılır → küre topraklanır → tel alınır → çubuk uzaklaştırılır.','Yük akışı çubuğun işaretine göre'),
 ['Çubuk uzaklaşmadan önce telin alınıp alınmamasının elektronların nereye gideceğini nasıl değiştirdiğini düşün.'],
 [B('Topraklama','iletken bir cisim toprağa bağlanınca yük serbestçe toprağa ya da topraktan cisme akabilir. Örnek: pozitif yüklü cisim topraklanınca topraktan elektron alır'),
  B('Etki ile yükleme','topraklı iletken, yaklaşan çubuğun yüküyle zıt işaretli yüklenir; bağlantı çubuk varken kesilirse yük kalıcı olur')],
 'Etki ile yüklenen cisim, kendisine yaklaştırılan çubuğun yüküyle zıt işaretli olur ve toprak bağlantısı çubuk varken kesilmelidir.',sekil=tk(sk))

# ---- 04 · Sürtünmeyle yüklenme · öncüllü · kolay (şekilsiz) ----
O('0004','fz-el2-surtunme','Sürtünme ile yüklenme ve nötr cismin çekilmesi','Elektriklenme türleri','kolay',
 'Sürtünmeyle elektriklenmede yük aktarımını, yük korunumunu ve nötr cismin yüklü cisme çekilmesini yorumlar.',
 'Sürtünmede elektronlar bir cisimden diğerine geçer; iki cismin yükleri zıt işaretli ve eşit büyüklüktedir; nötr yalıtkan etkiyle çekilir.',
 'Yük aktarıcısının proton olduğunu sanmak; nötr cismin yüklü cisme çekilemeyeceğini düşünmek.',
 'Kuru bir kış gününde plastik bir tarak, yünlü bir kazağa birkaç kez sürtülüyor. Ardından tarak, masa üzerindeki nötr kâğıt parçalarına yaklaştırıldığında parçaların tarağa doğru sıçrayıp ona yapıştığı görülüyor. Sürtünmeden önce tarak ile kazağın nötr olduğu ve yük aktarımında yalnızca elektronların rol oynadığı kabul ediliyor.',
 [('Sürtünmeden sonra tarak ile kazağın yükleri eşit büyüklükte ve zıt işaretlidir.',True,'Elektronlar bir cisimden diğerine geçtiğinden toplam yük korunur: biri −Q, öbürü +Q olur.','Yüklerin yalnızca tarakta oluştuğunu, kazağın yüksüz kaldığını düşünmüş.'),
  ('Tarak, sürtünme sırasında protonlarının bir kısmını kazağa vermiştir.',False,'Yük aktarımını elektronlar sağlar; protonlar atom çekirdeğinde bulunduğundan cisimler arasında geçmez.','Pozitif yükün proton aktarımıyla oluştuğunu düşünmüş.'),
  ('Nötr kâğıt parçalarının çekilmesi, parçalardaki yüklerin tarağın etkisiyle yeniden dağılmasından kaynaklanır.',True,'Yüklü tarak kâğıttaki yükleri ayrıştırır; yakın uçta zıt işaretli yük oluşur ve çekim itmeden büyük olur.','Nötr cismin yüklü cisim tarafından çekilemeyeceğini düşünmüş.')],
 ['Yalnız I','Yalnız III','I ve II','I ve III','II ve III'],
 ('Tarak yünle sürtünerek yüklenir; kâğıtlar nötrdür.','Aktarılan parçacık: elektron'),
 ['Sürtünmede hangi parçacığın bir cisimden ötekine geçtiğini ve toplam yükün korunduğunu düşün.'],
 [B('Sürtünme ile yüklenme','iki cisim birbirine sürtülünce elektron geçişi olur; biri elektron kazanıp negatif, diğeri kaybedip pozitif yüklenir. Örnek: ebonit çubuk yüne sürtülünce negatif olur'),
  B('Yük korunumu','yalıtılmış sistemde toplam yük değişmez')],
 'Yük aktarımını elektronlar yapar; sürtünmede iki cismin yükü eşit büyüklükte, zıt işaretlidir.')

# ---- 05 · Coulomb kuvveti oranı · sayısal · kolay ----
cK,cL,cd=3,2,2
Fyeni=Fr(cK*cL,cd**2); assert Fyeni==Fr(3,2)
h1=Fr(cK*cL,cd); assert h1==3          # uzaklığın karesini almamış
h2=Fr(cK*cL); assert h2==6             # uzaklığı hiç hesaba katmamış
h5=Fr(cK,cd**2); assert h5==Fr(3,4)   # L'nin yükündeki artışı hesaba katmamış
h4=Fr(cK+cL,cd**2); assert h4==Fr(5,4) # çarpım yerine toplam
sk=(kure(0,0,.45)+'\\node[font=\\small] at (0,0) {$K$};'+kure(4.2,0,.45)+'\\node at (4.2,0) {$L$};'
    '\\node at (0,.95) {$+$}; \\node at (4.2,.95) {$-$};'
    '\\draw[<->] (0,-.85) -- (4.2,-.85); \\node[fill=white,inner sep=1pt] at (2.1,-.85) {$d$};'
    '\\draw[thick] (-.9,-.45) -- (5.1,-.45);')
N('0005','fz-el2-coulomb-oran','Coulomb kuvvetinin yük ve uzaklıkla değişimi','Coulomb kuvveti','kolay',
 'Coulomb kuvvetinin yüklerin çarpımıyla doğru, uzaklığın karesiyle ters orantılı olduğunu kullanarak kuvvetin değişimini oranlar.',
 'F, yüklerin çarpımıyla doğru, aralarındaki uzaklığın karesiyle ters orantılıdır; değişen büyüklükler oran olarak çarpılır.',
 'Uzaklığın karesini unutmak; yükleri çarpmak yerine toplamak; uzaklık artınca kuvvetin de arttığını sanmak.',
 'Yalıtkan bir ray üzerinde duran noktasal K ve L yüklü küreleri, şekildeki gibi birbirinden d kadar uzaktadır ve birbirini F büyüklüğünde bir kuvvetle çekmektedir. Bir öğrenci, K küresinin yükünü 3 katına, L küresinin yükünü 2 katına çıkarırken küreler arasındaki uzaklığı da 2 katına çıkarıyor. Başka yüklü cisim ve ortam değişikliği yoktur.\nBuna göre, küreler arasındaki yeni çekim kuvvetinin büyüklüğü kaç F olur?',
 Fyeni,[(h4,'Yüklerin çarpımı yerine toplamını almış: (3 + 2) ÷ 2² = 1,25 F.','bilgi'),
        (h1,'Uzaklığın karesini değil kendisini almış: (3 × 2) ÷ 2 = 3 F.','islem'),
        (h2,'Uzaklığın değişiminin kuvveti etkilemediğini düşünmüş: 3 × 2 = 6 F.','bilgi'),
        (h5,'L küresinin yükündeki artışı hesaba katmamış: 3 ÷ 2² = 0,75 F.','dikkat')],
 'Yeni çekim kuvvetinin büyüklüğü (F cinsinden).',
 ['Kuvvetin hangi büyüklüklerle doğru, hangileriyle ters orantılı olduğunu yazıp oranları ayrı ayrı çarp.'],
 [B('Coulomb yasası','F = k·q₁·q₂ ÷ d²; yüklerin çarpımıyla doğru, uzaklığın karesiyle ters orantılıdır. Örnek: uzaklık 3 katına çıkarsa kuvvet 9 katı azalır')],
 [A('Yük etkisi','Kuvvet yüklerin çarpımıyla doğru orantılıdır.','3 × 2 = 6 katına çıkar'),
  A('Uzaklık etkisi','Kuvvet uzaklığın karesiyle ters orantılıdır; uzaklık 2 katına çıkmıştır.','1 ÷ 2² = 1 ÷ 4'),
  A('Oranı birleştir','İki etkiyi çarp.','F′ = F × 6 ÷ 4 = 1,5 F')],
 'Oran sorularında önce her büyüklüğün çarpanını, sonra uzaklık için karesini uygula.',sekil=tk(sk))

# ---- 06 · İpe asılı küreler (kesinlikle doğru) · öncüllü · orta ----
# M(+) L'yi itiyor → L (+). K, L'yi çekiyor → K negatif ya da nötr: negatif olması kesin değil, pozitif olması imkânsız.
def asili(hx,ang,etiket,isaret=''):
    Ls=2.0; bx=hx+Ls*sin(radians(ang)); by=3.2-Ls*cos(radians(ang))
    s=f'\\draw[thick] ({hx},3.2) -- ({bx:.3f},{by:.3f}); \\fill ({hx},3.2) circle (1.6pt);\n'
    s+=f'\\draw[thick,fill=gray!15] ({bx:.3f},{by-.3:.3f}) circle (.3); \\node at ({bx:.3f},{by-.3:.3f}) {{${etiket}$}};\n'
    return s
sk=('\\draw[thick] (-.6,3.2) -- (5.4,3.2); \\fill[pattern=north east lines,pattern color=gray] (-.6,3.2) rectangle (5.4,3.45);\n'+
    asili(0,9,'K')+asili(2.4,-9,'L')+asili(4.8,6,'M')+'\\node at (5.7,.95) {$+$};')
O('0006','fz-el2-asili-kureler','İpe asılı kürelerin çekim–itme durumundan yük işareti çıkarma','Elektriklenme türleri','orta',
 'İtme ve çekme gözlemlerinden yüklerin işaretini çıkarır; çekmenin nötr cisimle de olabileceğini bilir.',
 'İtme yalnızca aynı işaretli yükler arasında olur; çekme zıt işaretli ya da nötr cisimle olabilir. Kesin sonuç yalnızca itmeden çıkar.',
 'Çekimin yalnızca zıt işaretli cisimler arasında olduğunu sanmak.',
 'Yalıtkan iplerle tavana asılı K, L ve M küreleri, şekildeki gibi dengede durmaktadır. M küresinin pozitif yüklü olduğu biliniyor; K ve L kürelerinden her biri yüklü ya da yüksüz (nötr) olabilir. Küreler arasındaki etkileşim yalnızca elektriksel kuvvetlerden oluşmakta, iplerin kütlesi ve yük taşıması önemsenmemektedir. Yalnızca birbirine komşu küreler arasındaki kuvvetler dikkate alınacak, uzaktaki kürenin etkisi ihmal edilecektir.',
 [('L küresi pozitif yüklüdür.',True,'L, pozitif yüklü M tarafından itiliyor; itme yalnızca aynı işaretli yükler arasında olduğundan L de pozitiftir.','İtme olayını yük işaretinden bağımsız saymış.'),
  ('K küresi negatif yüklüdür.',False,'K, pozitif L’yi çekiyor; bu ya K’nin negatif ya da nötr olduğunu gösterir. Negatif olması kesin değildir.','Çekmenin yalnızca zıt işaretli cisimler arasında olduğunu düşünmüş.'),
  ('K küresi pozitif yüklüdür.',False,'Pozitif K, pozitif L’yi çekemez, iterdi; dolayısıyla K pozitif olamaz.','K’nin L’yi çekmesinin yük işaretiyle ilgisini kuramamış.')],
 ['Yalnız I','Yalnız II','I ve II','I ve III','II ve III'],
 ('K–L çekiyor, L–M itiyor, M pozitif.','Kesin bilgi: yalnızca itmeden gelir'),
 ['Hangi gözlemin yük işareti için kesin bilgi verdiğini düşün: itme mi, çekme mi?'],
 [B('Elektriksel kuvvet','aynı işaretli yükler birbirini iter, zıt işaretli yükler çeker; nötr bir iletken ya da yalıtkan da yüklü cisim tarafından etkiyle çekilir. Örnek: yüklü tarak nötr kâğıdı çeker')],
 'İtme kesin bilgi verir (aynı işaret); çekme zıt işaretli olmayı değil, aynı işaretli olmamayı kanıtlar.',sekil=tk(sk),
 son='Buna göre, yukarıdaki yargılardan hangileri kesinlikle doğrudur?')

# ---- 07 · Pozitif yüklü elektroskopun topraklanması · öncüllü · orta ----
# I yanlış: elektronlar topraktan elektroskopa gelir. II doğru: nötrleşince yapraklar kapanır. III doğru: tel alınınca yük yok, nötr.
sk=elsk(0,48)+'\\draw[thick] (.25,2.55) -- (1.3,2.55) -- (1.3,1.7); \\draw (1.3,1.7) node[ground]{}; \\node[font=\\footnotesize] at (2.45,2.4) {toprak teli};'
O('0007','fz-el2-elektroskop-toprak','Yüklü elektroskopun topraklanması','Topraklama','orta',
 'Yüklü elektroskopun topraklanmasında elektron akış yönünü, yaprakların durumunu ve son yükü yorumlar.',
 'Pozitif yüklü iletken topraklanınca topraktan elektron gelir ve cisim nötrleşir; yapraklar kapanır.',
 'Elektron akış yönünü ters düşünmek; topraklamanın kalıcı yük bıraktığını sanmak.',
 'Yaprakları şekildeki gibi açık olan, pozitif yüklü bir elektroskopun topuzu iletken bir telle toprağa bağlanıyor. Bir süre beklendikten sonra tel topuzdan ayrılıyor. Elektroskop, bu süre içinde yalnızca toprakla yük alışverişi yapmaktadır; başka yüklü cisim ortamda bulunmamaktadır.',
 [('Elektronlar elektroskoptan toprağa akar.',False,'Pozitif yüklü elektroskopta elektron eksiği vardır; elektronlar topraktan elektroskopa geçer.','Topraklamada her zaman fazla yükün toprağa aktığını düşünmüş.'),
  ('Yapraklar kapanır.',True,'Elektron eksiği giderilince yapraklardaki pozitif yük kalmaz; yapraklar birbirini itmez ve sarkar.','Yaprakların toprağa bağlanınca açık kalacağını sanmış.'),
  ('Tel ayrıldıktan sonra elektroskop nötrdür.',True,'Elektronlar eksiği tam karşılayana dek geçer; elektroskopun yükü sıfırlanır ve tel çekilince de sıfır kalır.','Topraklamanın bir miktar pozitif yük bıraktığını düşünmüş.')],
 ['Yalnız I','Yalnız II','I ve II','I ve III','II ve III'],
 ('Pozitif elektroskop → topraklama → yapraklar açık başlar.','Elektron akışı eksik olan yöne'),
 ['Elektroskop toprağa bağlandığı anda yük akışının yönünü neyin belirlediğini düşün.'],
 [B('Topraklama','iletken cisim toprağa bağlanınca elektronlar toprak yönünde ya da topraktan cisme akarak cismi nötrler. Örnek: negatif cisimden toprağa elektron gider')],
 'Pozitif cisme topraktan elektron gelir; negatif cisimden toprağa elektron gider.',sekil=tk(sk))

# ---- 08 · Elektroskopta yaprak açıklığı artışı · tek doğru · kolay ----
sk=(elsk(0,22)+'\\node at (0,-.45) {(1)};'+
    elsk(4.6,42)+cubuk(6.1,2.55,'',w=1.7)+'\\node at (6.1,3.15) {$X$};'+'\\node at (4.6,-.45) {(2)};')
N('0008','fz-el2-yaprak-aciklik','Yaprak açıklığındaki değişimden yaklaşan yükün işareti','Elektroskop','kolay',
 'Yüklü elektroskoba yüklü cisim yaklaştırıldığında yaprak açıklığının artmasından cismin yük işaretini çıkarır.',
 'Yaprak açıklığı artıyorsa yapraklara elektronlar (aynı işaretli yük) gelmiştir; yaklaştırılan cisim elektroskopla aynı işaretlidir.',
 'Yaprakların açılmasını yüklü cisim ile çubuğun çekmesine bağlamak; açıklığın azalmasını artmasıyla karıştırmak.',
 'Negatif yüklü bir elektroskopun (1) yaprakları şekildeki gibi açıktır. Öğrenci, işaretini bilmediği yüklü bir X cismini elektroskopun topuzuna dokundurmadan yaklaştırıyor ve yaprakların (2) konumuna kadar daha çok açıldığını gözlüyor; yapraklar bu sırada hiç kapanmadan sürekli açılmaktadır. X cismi dışında hiçbir cisim yaklaştırılmamıştır ve elektroskopun toplam yükü değişmemiştir.\nBuna göre, X cismi için aşağıdakilerden hangisi söylenebilir?',
 'Negatif yüklüdür',[('Pozitif yüklüdür','Yaprak açıklığının artmasını, pozitif cismin elektronları topuza çekip yaprakları pozitif bırakması sanmış; oysa bu durumda yaprak açıklığı azalırdı.','bilgi'),
  ('Elektroskoptan daha çok yüklüdür, işareti önemsizdir','Yaprak açıklığını yalnızca yük miktarına bağlamış; oysa pozitif bir cisim yaklaşınca açıklık önce azalırdı, işaret belirleyicidir.','bilgi'),
  ('İşareti belirlenemez','Yaprak açıklığındaki değişimin işaret bilgisi vermediğini düşünmüş; oysa artış, yapraklara elektron gelmesine işaret eder.','bilgi'),
  ('Yalnızca iletken olabilir','Yaprak açıklığını cismin iletken ya da yalıtkan oluşuna bağlamış; yük işareti iletkenlikten bağımsızdır.','bilgi')],
 'X cismi hakkında doğru çıkarım.',
 ['Yaprak açıklığının artması için yapraklarda yük miktarının nasıl değişmesi gerektiğini ve elektronların hangi yöne itildiğini düşün.'],
 [B('Elektroskop','yaprakların açıklığı yük miktarıyla artar. Örnek: negatif yüklü elektroskopa negatif cisim yaklaşırsa elektronlar yapraklara itilir ve açıklık artar')],
 [A('Başlangıç durumu','Elektroskop negatif yüklüdür; yapraklar elektron fazlası nedeniyle açıktır.','(1): açıklık küçük'),
  A('Değişimi yorumla','Açıklık artmışsa yapraklardaki elektron fazlası artmıştır.','Elektronlar topuzdan yapraklara itilmiştir'),
  A('Yaklaşan cismin yükünü bul','Elektronları kendinden uzağa iten cisim negatif yüklüdür.','X: negatif')],
 'Yaprak açıklığı artıyorsa yaklaşan cisim elektroskopla aynı işaretlidir; azalıyorsa zıt işaretlidir.',sekil=tk(sk),
 sira=['Pozitif yüklüdür','Elektroskoptan daha çok yüklüdür, işareti önemsizdir','İşareti belirlenemez','Yalnızca iletken olabilir','Negatif yüklüdür'])

# ---- 09 · Elde tutulan / saplı metal çubuk · öncüllü · orta (şekilsiz) ----
O('0009','fz-el2-iletken-yalitkan','İletken ve yalıtkan çubuğun sürtünmeyle yüklenmesi','Elektriklenme türleri','kolay',
 'İletken cismin yük tutabilmesi için yalıtılmış olması gerektiğini, yalıtkanda yükün sürtünen bölgede kaldığını yorumlar.',
 'Elde tutulan iletken çubukta fazla yük, vücut aracılığıyla toprağa akar; yalıtılmış iletken yük tutar; yalıtkanda yük bulunduğu yerde kalır.',
 'Her cismin sürtünmeyle yüklenebileceğini, iletkenin elde de yük tutacağını sanmak; yalıtkanda yükün yayıldığını düşünmek.',
 'Bir öğretmen, sürtünmeyle yüklenmeyi göstermek için iki deney yapıyor. Birinci deneyde metal bir çubuğu doğrudan elinde tutarak yüne sürtüyor; ikinci deneyde aynı çubuğu plastik bir sapla tutarak sürtüyor. Çubuk her deneyde küçük kâğıt parçalarına yaklaştırılıyor ve yalnızca ikinci deneyde parçaların çubuğa çekildiği görülüyor.',
 [('Elde tutulan metal çubuk sürtünmeyle yüklenir ve yükünü korur.',False,'Metal iletkendir; elde tutulursa sürtünmeyle oluşan yük vücut yoluyla toprağa akar ve çubuk yüklü kalmaz.','Her sürtünmenin kalıcı yük bıraktığını, çubuğun metal olmasının önemsiz olduğunu düşünmüş.'),
  ('Plastik saplı metal çubuk sürtünme sonucunda yüklü kalabilir.',True,'Sap, çubuğu elden yalıtır; yük toprağa akamaz ve çubukta kalır, kâğıtları çekmesi bunun kanıtıdır.','Metalin hiçbir koşulda yüklenemeyeceğini düşünmüş.'),
  ('Yalıtkan bir cismin sürtünen bölgesindeki yük, cismin her yerine yayılır.',False,'Yalıtkanlarda yükler serbestçe hareket edemez; yük bulunduğu bölgede kalır.','Yükün her maddede serbestçe yayıldığını sanmış.')],
 ['Yalnız I','Yalnız II','I ve II','II ve III','I, II ve III'],
 ('Elde tutulan metal → yüklenmiyor; saplı metal → yükleniyor; cam → yük sürtünen yerde.','İletken yükü yayar/akıtır, yalıtkan tutar'),
 ['Yükün iletken bir cismin içinde ya da bir yalıtkanın üzerinde nasıl davrandığını karşılaştır ve elin rolünü düşün.'],
 [B('İletken–yalıtkan','iletkenlerde yükler serbestçe hareket eder, yalıtkanlarda hareket edemez. Örnek: bakır tel iletken, plastik yalıtkandır'),
  B('Yalıtılmış iletken','toprağa bağlantısı olmayan iletken, aldığı yükü üzerinde tutar')],
 'İletken yalnızca yalıtılmışsa yük tutar; yalıtkan yükü bulunduğu yerde saklar.')

# ---- 10 · Doğrusal üç yükte net Coulomb kuvveti · sayısal · zor ----
k_,q_,d_=1,1,1
FKL=Fr(k_*4*q_*q_,(2*d_)**2); FML=Fr(k_*q_*q_,d_**2); assert FKL==FML==1
net=FKL+FML; assert net==2                         # K iter (sağa), M çeker (sağa)
y0=FKL-FML; assert y0==0                           # M'yi iten sanmış → zıt yönde
y1=FKL; assert y1==1                               # M'yi unutmuş
y3=Fr(k_*4*q_*q_,2*d_)+Fr(k_*q_*q_,d_); assert y3==3  # uzaklığın karesini almamış (F biriminde)
y5=Fr(k_*4*q_*q_,d_**2)+FML; assert y5==5          # K–L uzaklığını d almış
sk=(kure(0,0,.5)+kure(3.6,0,.5)+kure(5.4,0,.5)+'\\node at (0,0) {$K$}; \\node at (3.6,0) {$L$}; \\node at (5.4,0) {$M$};'
    '\\node at (0,.95) {$+4q$}; \\node at (3.6,.95) {$+q$}; \\node at (5.4,.95) {$-q$};'
    '\\draw[<->] (.5,-.8) -- (3.1,-.8); \\node[fill=white,inner sep=1pt] at (1.8,-.8) {$2d$};'
    '\\draw[<->] (4.1,-.8) -- (4.9,-.8); \\node[fill=white,inner sep=1pt] at (4.5,-1.3) {$d$};'
    '\\draw[thick] (-.9,-.5) -- (6.3,-.5);')
N('0010','fz-el2-net-kuvvet','Doğru üzerinde üç noktasal yükte net Coulomb kuvveti','Coulomb kuvveti','orta',
 'Doğrusal dizilmiş noktasal yükler arasındaki kuvvetleri oranla bularak bir yüke etkiyen net kuvveti yön dikkate alarak hesaplar.',
 'Her yükün uyguladığı kuvvet ayrı ayrı oranlanır; aynı işaretli yük iter, zıt işaretli yük çeker; kuvvetler yönlerine göre toplanır.',
 'Yönleri gözetmeden mutlak değerleri toplamak ya da çıkarmak; uzaklığın karesini unutmak; yanlış uzaklık almak.',
 'Yalıtkan bir ray üzerinde sabit tutulan noktasal K, L ve M yükleri aynı doğru üzerinde, şekildeki gibi dizilmiştir. K yükünün L yüküne uyguladığı elektriksel kuvvetin büyüklüğü F olarak ölçülüyor. Yükler dışında etkileşen başka cisim yoktur ve ortam her yerde aynıdır.\nBuna göre, L yüküne etki eden net elektriksel kuvvetin büyüklüğü kaç F’tir?',
 net,[(y0,'M yükünün L’yi ittiğini düşünmüş; kuvvetler zıt yönlü kabul edilip F − F = 0 bulunmuş.','bilgi'),
      (y1,'M’nin L üzerindeki etkisini hesaba katmamış; yalnız K’nin uyguladığı F’yi almış.','dikkat'),
      (y3,'Uzaklığın karesini almamış: K–L kuvveti 4 ÷ 2 = 2 birim, M–L kuvveti 1 birim olup toplam 3F bulmuş.','islem'),
      (y5,'K–L arasındaki uzaklığı d almış: 4 + 1 = 5 F.','islem')],
 'L yüküne etki eden net kuvvetin büyüklüğü (F cinsinden).',
 ['Önce M’nin L’ye uyguladığı kuvvetin F ile ilişkisini kur, sonra iki kuvvetin yönlerini karşılaştır.'],
 [B('Net kuvvet','aynı doğru üzerindeki kuvvetler yönlerine göre toplanır; aynı yöndekiler toplanır, zıt yöndekiler çıkarılır'),
  B('Coulomb yasası','F = k·q₁·q₂ ÷ d²; aynı işaretli yükler iter, zıt işaretli yükler çeker')],
 [A('K’nin kuvveti','K ile L aynı işaretlidir; K, L’yi sağa iter.','F = k·4q·q ÷ (2d)² = k·q² ÷ d²'),
  A('M’nin kuvveti','M ile L zıt işaretlidir; M, L’yi kendisine, yani sağa çeker.','F_M = k·q·q ÷ d² = k·q² ÷ d² = F'),
  A('Yönleri karşılaştır','İki kuvvet de sağa doğrudur.','Aynı yönlü → toplanır'),
  A('Net kuvveti bul','Büyüklükler toplanır.','F_net = F + F = 2F')],
 'Doğrusal yük dizilerinde önce her kuvveti F cinsinden yaz, sonra yönlerine göre topla.',sekil=tk(sk))

# =====================================================================
# AKIM VE DEVRELER (16)
# =====================================================================
GR='width=6.6cm,height=5.4cm,grid=both,major grid style={gray!55,thin},tick label style={font=\\scriptsize},axis lines=left,xlabel style={font=\\small},ylabel style={font=\\small}'
# ---- 11 · V–I grafiğinden direnç, seri bağlama · sayısal · orta ----
RK,RL,Vk=4,8,24
assert RK*2==8 and RL*1==8 and RK*5==20 and RL*3==24     # grafikteki noktalar
Ik=Fr(Vk,RK+RL); assert Ik==2
ht=[Fr(Vk,RL),Fr(Vk,RK),Fr(Vk,Fr(RK+RL,2)),Fr(Vk)/(Fr(RK*RL,RK+RL))]; assert ht==[3,6,4,9]
gx=['\\begin{axis}['+GR+',xmin=0,xmax=5,ymin=0,ymax=26,xtick distance=1,ytick={0,4,8,12,16,20,24},xlabel={$I$ (A)},ylabel={$V$ (V)}]',
    '\\addplot[thick,vurgu,no marks] coordinates {(0,0)(5,20)}; \\node[above left,vurgu] at (axis cs:5,20) {$K$};',
    '\\addplot[thick,no marks] coordinates {(0,0)(3,24)}; \\node[above left] at (axis cs:3,24) {$L$};','\\end{axis}']
N('0011','fz-el2-vi-grafik','Gerilim–akım grafiğinden direnç okuma ve seri bağlama','Ohm yasası','orta',
 'Gerilim–akım grafiğinde eğimden direnci bulur, seri bağlı dirençlerin eşdeğerinden devre akımını hesaplar.',
 'Ohm yasasında V–I grafiğinin eğimi direnci verir; seri bağlı dirençlerin eşdeğeri toplamdır ve akım V ÷ R_eş ile bulunur.',
 'Grafiği I ÷ V olarak okumak; yalnız bir direnci hesaba katmak; seri yerine paralel eşdeğer almak; dirençlerin ortalamasını almak.',
 'Bir öğrenci laboratuvarda sıcaklığı sabit tutulan K ve L dirençlerinin uçlarına farklı gerilimler uygulayıp akımları ölçüyor ve sonuçları şekildeki gibi grafiğe geçiriyor. Daha sonra K ve L dirençlerini birbirine seri bağlıyor ve bu seri grubu gerilimi 24 V olan ideal bir üretecin uçlarına bağlıyor.\nBuna göre, devreden geçen akım kaç A’dır?',
 2,[(3,'Yalnız L direncini (8 Ω) hesaba katmış: 24 ÷ 8 = 3 A.','dikkat'),(4,'Dirençlerin ortalamasını (6 Ω) eşdeğer sanmış: 24 ÷ 6 = 4 A.','bilgi'),
    (6,'Yalnız K direncini (4 Ω) hesaba katmış: 24 ÷ 4 = 6 A.','dikkat'),(9,'Seri yerine paralel eşdeğeri (8/3 Ω) kullanmış: 24 ÷ (8/3) = 9 A.','bilgi')],
 'Seri devreden geçen akım (A).',
 ['Grafikteki bir noktadan her direncin değerini bulmaya başla; sonra bağlanma biçimine göre eşdeğerini yaz.'],
 [B('Ohm yasası','V = I · R; V–I grafiğinde doğrunun eğimi direnci verir. Örnek: (2 A, 10 V) noktasından geçen doğrunun direnci 5 Ω’dur'),
  B('Seri bağlama','eşdeğer direnç dirençlerin toplamıdır; seri kolda akım her dirençte aynıdır')],
 [A('K’nin direnci','Grafikte K, 2 A akımda 8 V gerilime sahiptir.','R_K = 8 ÷ 2 = 4 Ω'),
  A('L’nin direnci','Grafikte L, 1 A akımda 8 V gerilime sahiptir.','R_L = 8 ÷ 1 = 8 Ω'),
  A('Eşdeğer direnç','Seri bağlı dirençler toplanır.','R_eş = 4 + 8 = 12 Ω'),
  A('Akımı bul','Ohm yasasını eşdeğer dirence uygula.','I = 24 ÷ 12 = 2 A')],
 'V–I grafiğinde direnç, grafikten okunan herhangi bir noktadaki V ÷ I oranıdır.',sekil=tikz_svg(HEAD+'\n'.join(gx)+TAIL),kalip='grafik')

# ---- 12 · Direncin bağlı olduğu etkenler (tablo) · öncüllü · orta ----
Rn={'X':Fr(1,1),'Y':Fr(2,1)/1,'Z':Fr(1,2),'T':Fr(2,2)}        # R ∝ ℓ / A (aynı madde, aynı sıcaklık)
assert Rn['Z']<Rn['X'] and Rn['Y']==4*Rn['Z'] and Rn['T']==Rn['X']
sk=tablo_svg(['Tel','Uzunluk','Kesit alanı'],[['X','ℓ','A'],['Y','2ℓ','A'],['Z','ℓ','2A'],['T','2ℓ','2A']])
O('0012','fz-el2-direnc-tablo','Tellerin direncini karşılaştırma (uzunluk, kesit)','Direncin bağlı olduğu etkenler','orta',
 'Aynı maddeden yapılmış tellerin direncini uzunluk ve kesit alanına göre oranlayarak karşılaştırır.',
 'Telin direnci uzunluğuyla doğru, kesit alanıyla ters orantılıdır (R ∝ ℓ ÷ A); oranlar tablodan okunarak karşılaştırılır.',
 'Kesit alanının direnci artırdığını sanmak; uzunluk ve kesit değişimini birbirine karıştırmak.',
 'Bir atölyede aynı maddeden yapılmış, silindir biçimli X, Y, Z ve T tellerinin uzunlukları ile kesit alanları tabloda verilmiştir. Tellerin hepsi aynı sıcaklıktadır ve homojendir. Öğrenciler, tellerin dirençlerini karşılaştırarak hangi telin akıma karşı daha çok direnç gösterdiğini bulmaya çalışıyor.',
 [('Z telinin direnci, X telinin direncinden büyüktür.',False,'Kesit alanı arttıkça direnç azalır; Z’nin kesiti X’in 2 katı olduğundan R_Z = R_X ÷ 2’dir.','Kesit alanı büyük olan telin daha dirençli olduğunu sanmış.'),
  ('Y telinin direnci, Z telinin direncinin 4 katıdır.',True,'R_Y = 2·R_X (uzunluk iki kat), R_Z = R_X ÷ 2 (kesit iki kat); dolayısıyla R_Y ÷ R_Z = 4’tür.','Yalnız uzunluk etkisini (2 kat) ya da yalnız kesit etkisini (2 kat) görmüş.'),
  ('T telinin direnci, X telinin direncine eşittir.',True,'T’nin uzunluğu 2 katı, kesiti 2 katıdır; iki etki birbirini götürür ve R_T = R_X olur.','Uzunluk ve kesit artışının direnci mutlaka değiştireceğini düşünmüş.')],
 ['Yalnız I','Yalnız II','I ve III','II ve III','I, II ve III'],
 ('Aynı madde ve sıcaklık: R ∝ ℓ ÷ A.','X referans: R_X = R'),
 ['X telini referans alıp her telin uzunluk ve kesit çarpanını ayrı ayrı R ∝ ℓ ÷ A ilişkisine yerleştir.'],
 [B('Telin direnci','R = ρ·ℓ ÷ A; uzunlukla doğru, kesit alanıyla ters orantılıdır. Örnek: uzunluğu 3 katına çıkan telin direnci 3 katına çıkar'),
  B('Sabitler','maddenin cinsi ve sıcaklık aynıysa özdirenç ρ aynıdır ve oranlarda sadeleşir')],
 'Oranlarda önce uzunluk, sonra kesit çarpanını R ∝ ℓ ÷ A’ya yerleştir; sonra iki telin oranını al.',sekil=sk,kalip='tablo')

# ---- 13 · Seri–paralel karışık devre, direnç üzerindeki gerilim · sayısal · orta ----
V3,R31,R32,R33=12,4,2,4
Rk2=R32+R33; I2=Fr(V3,Rk2); V3d=I2*R33
assert Rk2==6 and I2==2 and V3d==8 and Fr(V3,R31)==3
assert I2*R32==4 and Fr(V3,2)==6 and V3==12
sk=('\\draw (0,0) to[battery1,l={$12$ V}] (0,3) -- (3,3); \\draw (3,3) to[R,l={$R_1=4\\,\\Omega$}] (3,0) -- (0,0);\n'
    '\\draw (3,3) -- (6.3,3) to[R,l={$R_2=2\\,\\Omega$}] (6.3,1.5) to[R,l={$R_3=4\\,\\Omega$}] (6.3,0) -- (3,0);\n'
    '\\fill (3,3) circle (1.7pt) (3,0) circle (1.7pt);')
N('0013','fz-el2-karisik-devre','Paralel kolların birinde seri direnç bulunan devre','Elektrik devreleri','orta',
 'Paralel bağlı kolların gerilimlerinin eşit olduğunu ve seri koldaki akımın aynı olduğunu kullanarak bir direnç üzerindeki gerilimi bulur.',
 'Paralel kollarda gerilim üreteç gerilimine eşittir; seri koldaki akım, kol eşdeğerine Ohm yasası uygulanarak bulunur ve gerilim V = I·R ile hesaplanır.',
 'Kolun gerilimini seri dirençlerden birine vermek; akımı gerilim sanmak; gerilimi eşit paylaştırmak.',
 'Şekilde ideal bir üreteç, üç direnç ve bağlantı telleri ile kurulmuş bir devre görülmektedir. Üretecin emk’sı ve direnç değerleri şekilde verilmiştir. Devre dengeye ulaştıktan sonra bir öğrenci, sağ koldaki R₃ direncinin uçları arasındaki gerilimi bulmak istiyor. Bağlantı tellerinin ve üretecin iç direnci ihmal edilmektedir.\nBuna göre, R₃ direncinin uçları arasındaki gerilim kaç V’tur?',
 8,[(2,'Sağ koldan geçen akımı (2 A) gerilim sanmış; akımı direnç ile çarpmayı unutmuş.','islem'),
    (4,'R₂ direncinin uçları arasındaki gerilimi (2 A × 2 Ω = 4 V) bulmuş; sorulan R₃’tür.','dikkat'),
    (6,'Üreteç gerilimini iki koldaki gerilime eşit paylaştırıp 12 ÷ 2 = 6 V bulmuş.','bilgi'),
    (12,'Paralel kolların gerilimi üretece eşit olduğundan R₃’ün de 12 V gerilim taşıdığını sanmış; R₃ ile R₂ seridir.','bilgi')],
 'R₃ direncinin uçları arasındaki gerilim (V).',
 ['Önce sağ koldaki iki direncin ortak akımını bulmak için bu kola uygulanan gerilimi belirle.'],
 [B('Paralel bağlama','kolların uçları arasındaki gerilim ortaktır ve üreteç gerilimine eşittir. Örnek: 9 V’a bağlı iki paralel kolun her birinde 9 V vardır'),
  B('Seri bağlama','aynı koldaki dirençlerden aynı akım geçer; gerilim dirençle orantılı paylaşılır')],
 [A('Sağ kolun gerilimi','Sağ kol, üretece paralel bağlıdır; R₂ ve R₃ seridir.','V_kol = 12 V, R_kol = 2 + 4 = 6 Ω'),
  A('Sağ kol akımı','Ohm yasasını kola uygula.','I = 12 ÷ 6 = 2 A'),
  A('R₃’ün gerilimi','R₃’ten kolun akımı geçer.','V₃ = 2 × 4 = 8 V')],
 'Önce hangi dirençlerin aynı akımı taşıdığını belirle; sonra V = I·R’yi yalnız o dirençlere uygula.',sekil=tk(sk))

# ---- 14 · Köprü (simetrik) devrede anahtar · öncüllü · orta ----
# K–L ve M–N özdeş seri kollar paralel: orta düğümler eşit potansiyelde → S'den akım geçmez; hiçbir lambanın parlaklığı değişmez; toplam akım aynı.
sk=('\\draw (0,0) to[battery1] (0,3) -- (6,3); \\draw (0,0) -- (6,0);\n'
    '\\draw (2.4,3) to[lamp,l={$K$}] (2.4,1.5) to[lamp,l={$L$}] (2.4,0);\n'
    '\\draw (6,3) to[lamp,l={$M$}] (6,1.5) to[lamp,l={$N$}] (6,0);\n'
    '\\draw (2.4,1.5) to[spst,l={$S$}] (6,1.5);\\fill (2.4,1.5) circle (1.7pt) (6,1.5) circle (1.7pt) (2.4,3) circle (1.7pt) (2.4,0) circle (1.7pt);')
O('0014','fz-el2-kopru-lamba','Simetrik devrede anahtarın kapatılması (lamba parlaklığı)','Anahtar açma ve kapama','orta',
 'Simetrik bağlı özdeş lambalarda orta düğümler arasına anahtar kapatıldığında akım ve parlaklık değişimini yorumlar.',
 'Özdeş ve simetrik kollarda orta düğümlerin potansiyeli eşittir; aralarına bağlanan anahtardan akım geçmez ve hiçbir şey değişmez.',
 'Kapalı anahtarın akım geçmesine ve eşdeğer direncin düşmesine yol açtığını sanmak.',
 'Dirençleri sabit ve özdeş K, L, M ve N lambaları ile ideal bir üreteç şekildeki gibi bağlanmıştır. S anahtarı açıkken lambalar bir süre yandıktan sonra devre dengeye ulaşıyor. Bağlantı telleri ve üreteç iç direnci ihmal edilmektedir. Öğrenci, S anahtarını kapatıp devre yeniden dengeye ulaştığında lambaların davranışını gözlemek istiyor.',
 [('K lambasının parlaklığı artar.',False,'Orta düğümler S’den önce de aynı potansiyeldedir; K’nin gerilimi ve akımı değişmez, parlaklığı aynı kalır.','Köprünün akımı yeniden dağıttığını, kapalı anahtarın kolları kısaltıp akımı artıracağını düşünmüş.'),
  ('S anahtarından akım geçmez.',True,'İki kolda da aynı iki özdeş lamba seri olduğundan orta düğümlerin potansiyelleri eşittir; S’nin uçları arasında gerilim yoktur.','Kapalı bir anahtardan her zaman akım geçeceğini düşünmüş.'),
  ('Üreteçten çekilen toplam akım değişmez.',True,'S’den akım geçmediğinden devre S’siz haliyle aynıdır; eşdeğer direnç ve toplam akım sabit kalır.','Anahtar kapanınca eşdeğer direncin azalacağını sanmış.')],
 ['Yalnız I','Yalnız II','I ve II','I ve III','II ve III'],
 ('İki kol özdeş: K–L ve M–N; S orta düğümleri bağlıyor.','Simetri: V_orta düğümler eşit'),
 ['Anahtarın iki ucu arasındaki gerilimi bulmaya çalış.'],
 [B('Düğüm potansiyeli','iki nokta arasında gerilim yoksa, o noktaları bağlayan iletkenden akım geçmez. Örnek: eşit direnç bölücüde iki orta nokta aynı potansiyeldedir'),
  B('Lamba parlaklığı','lambanın parlaklığı üzerindeki güçle (P = I²R) belirlenir; akım ve gerilim değişmezse parlaklık değişmez')],
 'Simetrik devrede orta düğümler eşit potansiyeldedir; bunları bağlayan anahtar devreyi değiştirmez.',sekil=tk(sk))

# ---- 15 · Seri devrede voltmetre okumasından emk · sayısal · kolay ----
R51,R52,R53=2,4,6; Vr=8
I5=Fr(Vr,R52); E5=I5*(R51+R52+R53)
assert I5==2 and E5==24 and Vr+I5*R51==12 and Vr+I5*R53==20 and Fr(Vr*12,R53)==16
sk=('\\draw (0,0) to[battery1] (0,3) to[R,l={$R_1=2\\,\\Omega$}] (2.4,3) to[R,l={$R_2=4\\,\\Omega$}] (4.8,3) to[R,l={$R_3=6\\,\\Omega$}] (7.2,3) -- (7.2,0) -- (0,0);\n'
    '\\node[draw,circle,minimum size=.7cm,inner sep=0pt] (V) at (3.6,4.5) {V};\n'
    '\\draw (2.4,3) |- (V.west); \\draw (4.8,3) |- (V.east); \\fill (2.4,3) circle (1.7pt) (4.8,3) circle (1.7pt);')
N('0015','fz-el2-seri-emk','Seri devrede voltmetre okumasından üreteç gerilimi','Ampermetre ve voltmetre','kolay',
 'Bir dirence bağlı voltmetre okumasından devre akımını, oradan da üretecin gerilimini bulur.',
 'Seri devrede akım her yerde aynıdır; voltmetre okuması ve direnç değeriyle akım bulunur, üreteç gerilimi toplam dirençle çarpılarak elde edilir.',
 'Voltmetre okumasını üreteç gerilimi sanmak; dirençlerden birini unutmak.',
 'Şekildeki devrede üreteç ve voltmetre idealdir; direnç değerleri şekilde verilmiştir. Voltmetre yalnızca R₂ direncine bağlıdır ve 8 V göstermektedir. Bağlantı tellerinin direnci ihmal edilmektedir. Devre sürekli akım durumundadır.\nBuna göre, üretecin emk’sı kaç V’tur?',
 24,[(8,'Voltmetrenin değerini doğrudan üreteç gerilimi almış; yalnız bir dirence bağlı olduğunu görmemiş.','dikkat'),
     (12,'R₃ direncini hesaba katmamış: 8 + 2 × 2 = 12 V.','dikkat'),(16,'Gerilim paylaşımında oran paydasına R₃’ü alıp 8 × 12 ÷ 6 = 16 V bulmuş.','bilgi'),
     (20,'R₁ direncini hesaba katmamış: 8 + 2 × 6 = 20 V.','dikkat')],
 'Üretecin emk’sı (V).',
 ['Voltmetrenin bağlı olduğu dirençten geçen akımı bularak başla; bu akım devrenin başka yerlerinde de aynı mıdır?'],
 [B('Voltmetre','ölçülecek elemana paralel bağlanır ve o elemanın uçları arasındaki gerilimi gösterir'),
  B('Seri devre','akım her elemanda aynıdır; üreteç gerilimi dirençlerdeki gerilimlerin toplamıdır')],
 [A('Devre akımını bul','Voltmetre R₂’nin gerilimini gösterir; Ohm yasası.','I = 8 ÷ 4 = 2 A'),
  A('Toplam direnci bul','Seri dirençler toplanır.','R = 2 + 4 + 6 = 12 Ω'),
  A('Üreteç gerilimini bul','Akım tüm devrede aynıdır.','ε = 2 × 12 = 24 V')],
 'Seri devrede tek bir dirençten akımı bulup tüm devreye taşı.',sekil=tk(sk))

# ---- 16 · Fatura hesabı (tablo) · sayısal · orta ----
cihaz=[('Ütü',1,2000,Fr(1,2)),('Saç kurutma makinesi',1,1000,Fr(1,2)),('LED lamba',8,10,5),('Televizyon',1,100,5)]
gun=sum(Fr(a*w,1000)*s for _,a,w,s in cihaz); assert gun==Fr(12,5)
fat=gun*30*3; assert fat==216
f1=sum(Fr(w,1000)*s for _,a,w,s in cihaz)*30*3; assert f1==Fr(369,2)     # lambaların adedini yok saymış
f2=gun*3; assert f2==Fr(36,5)                                          # 30 günü unutmuş
f3=sum(Fr(a*w,1000)*(1 if s==Fr(1,2) else s) for _,a,w,s in cihaz)*30*3; assert f3==351   # yarım saati 1 saat almış
f4=gun*30; assert f4==72                                               # fiyatı çarpmamış
sk=tablo_svg(['Cihaz','Adet','Güç (W)','Günlük süre (saat)'],[['Ütü','1','2000','0,5'],['Saç kurutma makinesi','1','1000','0,5'],['LED lamba','8','10','5'],['Televizyon','1','100','5']])
N('0016','fz-el2-fatura','Elektrik enerjisi tüketimi ve fatura hesabı (tablo)','Elektriksel enerji ve güç','orta',
 'Cihazların güç, adet ve süre verilerinden günlük enerji tüketimini kWh olarak bulur ve faturayı hesaplar.',
 'Enerji = güç × süre; adetle çarpılır, kW × saat = kWh olarak toplanır ve tüketim birim fiyatla çarpılır.',
 'Adedi unutmak; W–kW dönüşümünü yanlış yapmak; gün sayısını ya da birim fiyatı unutmak.',
 'Bir ailenin evde kullandığı bazı elektrikli aletlerin etiket güçleri, adetleri ve günlük kullanım süreleri tabloda verilmiştir. Aletler her gün tabloda belirtilen sürelerde ve etiket güçlerinde çalıştırılmakta; evde başka elektrik tüketen cihaz bulunmamaktadır. Elektrik şirketi 1 kWh enerji için 3 TL ücret almaktadır ve ay 30 gündür.\nBuna göre, ailenin bu aletler için bir ayda ödeyeceği elektrik ücreti kaç TL’dir?',
 216,[(Fr(36,5),'30 günü hesaba katmamış; yalnız bir günlük ücreti (2,4 × 3 = 7,2 TL) bulmuş.','dikkat'),(72,'Birim fiyatı (3 TL) ile çarpmayı unutmuş; yalnız aylık enerjiyi (72 kWh) bulmuş.','dikkat'),
      (Fr(369,2),'LED lamba adedini (8) hesaba katmamış; günlük tüketimi 2,05 kWh bulup 2,05 × 30 × 3 = 184,5 TL hesaplamış.','dikkat'),
      (351,'Yarım saatlik kullanımları (ütü ve saç kurutma makinesi) 1 saat okumuş.','dikkat')],
 'Aylık elektrik ücreti (TL).',
 ['Her cihazın günlük enerjisini kWh cinsinden ayrı ayrı bul; adet ve süre çarpanlarını unutma.'],
 [B('Elektriksel enerji','E = P · t; güç kW, süre saat alınırsa enerji kWh çıkar. Örnek: 2 kW’lık cihaz 3 saat çalışırsa 6 kWh tüketir'),
  B('Birim dönüşümü','1 kW = 1000 W; 100 W = 0,1 kW')],
 [A('Ütü','2 kW × 0,5 saat','1 × 2 × 0,5 = 1 kWh'),
  A('Diğer cihazlar','Saç kurutma: 1 kW × 0,5 saat; LED: 8 × 0,01 kW × 5 saat; TV: 0,1 kW × 5 saat.','0,5 + 0,4 + 0,5 = 1,4 kWh'),
  A('Günlük toplam','Tüm cihazların günlük enerjisi toplanır.','1 + 1,4 = 2,4 kWh'),
  A('Aylık ücret','30 günlük enerji birim fiyatla çarpılır.','2,4 × 30 × 3 = 216 TL')],
 'Fatura sorularında önce günlük kWh’yi, sonra gün sayısını ve birim fiyatı çarp.',sekil=sk,kalip='tablo')

# ---- 17 · Etiketli lambaların seri bağlanması · öncüllü · zor ----
Ra=Fr(220**2,100); Rb=Fr(220**2,25); assert Ra==484 and Rb==1936
Is=Fr(220)/(Ra+Rb); Pa=Is**2*Ra; Pb=Is**2*Rb; Va=Is*Ra; Vb=Is*Rb
assert Va==44 and Vb==176 and Pa==4 and Pb==16 and Pa+Pb==20 and Pb>Pa and 100+25!=Pa+Pb
sk=('\\draw (0,0) to[sV,l={$220$ V}] (0,3) to[lamp,l={$L_1$}] (3,3) to[lamp,l={$L_2$}] (6,3) -- (6,0) -- (0,0);\n'
    '\\node[font=\\footnotesize,align=center] at (1.5,2.0) {220 V – 100 W}; \\node[font=\\footnotesize,align=center] at (4.5,2.0) {220 V – 25 W};')
O('0017','fz-el2-etiket-seri','Üzerinde etiket bulunan lambaların seri bağlanması','Elektriksel enerji ve güç','orta',
 'Lamba etiketinden direnci bulup seri bağlamada gerilimin ve gücün dirençle orantılı paylaşıldığını yorumlar.',
 'Etiket değerleri direnci verir (R = V² ÷ P); seri bağlamada akım ortaktır, güç P = I²R olduğundan direnci büyük lamba daha parlak yanar.',
 'Gücü büyük lambanın her durumda daha parlak olduğunu sanmak; seri bağlamada güçleri toplamak.',
 'Üzerlerinde 220 V – 100 W ve 220 V – 25 W yazan L₁ ve L₂ lambaları, şekildeki gibi gerilimi 220 V olan şebekeye seri bağlanmıştır. Lambaların dirençleri sıcaklıkla değişmiyor, bağlantı telleri ve şebeke iç direnci ihmal edilmektedir. Öğrenci, lambaların her birini tek başına şebekeye bağladığındaki parlaklıkları ile seri bağlandığındaki parlaklıklarını karşılaştırıyor.',
 [('Lambalar tek başına 220 V’luk şebekeye bağlanırsa L₁ daha parlak yanar.',True,'Etiket gücü, anma geriliminde harcanan güçtür; P₁ = 100 W > P₂ = 25 W olduğundan L₁ daha parlaktır.','Etiketteki gücün parlaklıkla ilgisi olmadığını düşünmüş.'),
  ('Lambalar seri bağlandığında L₁’in uçları arasındaki gerilim, L₂’ninkinden büyüktür.',False,'R₁ = 484 Ω, R₂ = 1936 Ω’dur; seri kolda gerilim dirençle orantılı bölüşülür, V₁ = 44 V < V₂ = 176 V’tur.','Gücü büyük lambanın daha çok gerilim alacağını sanmış.'),
  ('Lambalar seri bağlandığında devrede harcanan toplam güç 125 W’tır.',False,'Seri bağlamada lambalar anma gerilimini alamaz; toplam güç 220² ÷ 2420 = 20 W’tır.','Güçlerin etiket değerlerinin toplanacağını düşünmüş.')],
 ['Yalnız I','Yalnız II','I ve II','I ve III','II ve III'],
 ('R = V² ÷ P ile her lambanın direnci bulunur; seri kolda akım ortaktır.','R₁ = 484 Ω, R₂ = 1936 Ω'),
 ['Etiket bilgisinden her lambanın direncini bul; seri kolda akımın ve gerilimin dirençle nasıl paylaşıldığını düşün.'],
 [B('Etiket değeri','220 V – 100 W, lambanın 220 V’ta 100 W güç harcadığını gösterir; direnci R = V² ÷ P ile bulunur. Örnek: 220 V – 55 W lambanın direnci 880 Ω’dur'),
  B('Seri bağlama','akım ortaktır, gerilim dirençle doğru orantılı bölüşülür; güç P = I²R ile hesaplanır')],
 'Etiket gücü yalnızca anma geriliminde geçerlidir; seri bağlamada gerilim ve güç dirençle paylaşılır.',sekil=tk(sk))

# ---- 18 · Paralel dirençlerde güç · sayısal · zor ----
Rp=[4,6,12]; Req=1/sum(Fr(1,r) for r in Rp); assert Req==2
Ip=6; Vp_=Ip*Req; assert Vp_==12
Pd=[Fr(Vp_**2,r) for r in Rp]; assert Pd==[36,24,12] and sum(Pd)==72==Vp_*Ip
assert Ip**2*6==216
sk=('\\draw (0,0) to[battery1] (0,3) -- (1.0,3); \\node[draw,circle,minimum size=.7cm,inner sep=0pt] (A) at (1.7,3) {A}; \\draw (A.east) -- (6.8,3);\n'
    '\\draw (0,0) -- (6.8,0);\n'
    '\\draw (3,3) to[R,l={$R_1=4\\,\\Omega$}] (3,0); \\draw (4.9,3) to[R,l={$R_2=6\\,\\Omega$}] (4.9,0); \\draw (6.8,3) to[R,l={$R_3=12\\,\\Omega$}] (6.8,0);\n'
    '\\fill (3,3) circle (1.7pt) (4.9,3) circle (1.7pt) (3,0) circle (1.7pt) (4.9,0) circle (1.7pt);')
N('0018','fz-el2-paralel-guc','Paralel dirençlerde bir dirençte harcanan güç','Elektriksel enerji ve güç','orta',
 'Ampermetre okumasıyla paralel dirençlerin eşdeğerinden üreteç gerilimini bulur ve belirli bir dirençteki gücü hesaplar.',
 'Paralel kollarda gerilim ortaktır; ana akım ve eşdeğer dirençle gerilim bulunur, güç P = V² ÷ R ile hesaplanır.',
 'Ana akımla tek dirençte güç hesaplamak; başka direnci okumak; toplam gücü vermek.',
 'Şekildeki devrede ideal bir üreteç, ideal bir ampermetre ve üç direnç bulunmaktadır. Direnç değerleri şekilde verilmiştir. Devre dengeye ulaştığında ampermetre 6 A göstermektedir. Bağlantı tellerinin direnci ihmal edilmektedir ve dirençlerin değeri sıcaklıkla değişmemektedir.\nBuna göre, R₂ direncinde harcanan elektriksel güç kaç W’tır?',
 24,[(12,'R₂ yerine R₃’ün (12 Ω) gücünü hesaplamış: 12² ÷ 12 = 12 W.','dikkat'),(36,'R₂ yerine R₁’in (4 Ω) gücünü hesaplamış: 12² ÷ 4 = 36 W.','dikkat'),
     (72,'Devrenin toplam gücünü (12 V × 6 A = 72 W) R₂’nin gücü sanmış.','dikkat'),(216,'Ana kol akımını (6 A) R₂’den geçiyormuş gibi alıp I² · R = 36 × 6 = 216 W bulmuş.','bilgi')],
 'R₂ direncinde harcanan güç (W).',
 ['Önce paralel kolların ortak gerilimini bulmak için ampermetrenin ölçtüğü akımla toplam dirençten yararlan.'],
 [B('Paralel eşdeğer direnç','1 ÷ R_eş = 1 ÷ R₁ + 1 ÷ R₂ + … Örnek: 6 Ω ve 3 Ω paralel bağlanınca R_eş = 2 Ω olur'),
  B('Elektriksel güç','P = V·I = V² ÷ R = I²R; paralel kollarda gerilim ortak olduğundan P = V² ÷ R kullanışlıdır')],
 [A('Eşdeğer direnç','Paralel kollar için 1/R_eş = 1/4 + 1/6 + 1/12.','R_eş = 2 Ω'),
  A('Ortak gerilim','Ampermetre ana kol akımını ölçer.','V = 6 × 2 = 12 V'),
  A('R₂’nin gücü','R₂ üzerindeki gerilim üreteç gerilimine eşittir.','P₂ = 12² ÷ 6 = 24 W'),
  A('Kontrol et','Kol akımlarının toplamı ana akımı vermeli.','12/4 + 12/6 + 12/12 = 3 + 2 + 1 = 6 A')],
 'Paralel kollarda gerilim ortaktır; güç sorularında P = V² ÷ R’yi kullan.',sekil=tk(sk))

# ---- 19 · Kısa devre, güç artışı · sayısal · zor ----
R91,R92,R93,V9=3,5,7,30
i_ac=Fr(V9,R91+R92+R93); i_kp=Fr(V9,R91+R93); assert i_ac==2 and i_kp==3
P_ac=i_ac**2*R93; P_kp=i_kp**2*R93; dP=P_kp-P_ac; assert (P_ac,P_kp,dP)==(28,63,35)
e1=(i_kp-i_ac)*R93; e2=V9*(i_kp-i_ac); assert (e1,e2)==(7,30)
sk=('\\draw (0,0) to[battery1,l={$30$ V}] (0,3) to[R,l={$R_1=3\\,\\Omega$}] (2.5,3) to[R,l={$R_2=5\\,\\Omega$}] (5.2,3) to[R,l={$R_3=7\\,\\Omega$}] (7.7,3) -- (7.7,0);\n'
    '\\node[draw,circle,minimum size=.7cm,inner sep=0pt] (A) at (3.8,0) {A}; \\draw (7.7,0) -- (A.east); \\draw (A.west) -- (0,0);\n'
    '\\draw (2.5,3) -- (2.5,4.4) to[spst,l=$S$] (5.2,4.4) -- (5.2,3); \\fill (2.5,3) circle (1.7pt) (5.2,3) circle (1.7pt);')
N('0019','fz-el2-kisa-devre','Anahtar kapatılınca bir direncin kısa devre olması ve güç değişimi','Kısa devre','zor',
 'Bir direnç koluna paralel bağlı anahtar kapatıldığında direncin devre dışı kaldığını fark ederek akımı ve başka bir dirençteki güç artışını hesaplar.',
 'Anahtar bir direnci kısa devre yaparsa akım dirençten değil telden geçer; eşdeğer direnç azalır, akım artar; güç P = I²R ile iki durumda ayrı bulunup farkı alınır.',
 'Kısa devre olan direnci değil başka direnci çıkarmak; yalnız son ya da ilk gücü vermek; gerilimle akım artışını çarpmak.',
 'Şekildeki devrede üreteç ve ampermetre idealdir; üretecin emk’sı ve direnç değerleri şekilde verilmiştir. S anahtarı açıkken devre dengeye ulaşmıştır. Anahtar R₂ direncinin uçlarına, direnci ihmal edilebilir bir tel gibi bağlanmaktadır. Bir öğrenci S anahtarını kapatıp devre yeniden dengeye ulaştığında R₃ direncinde harcanan gücün ne kadar değiştiğini ölçmek istiyor.\nBuna göre, S anahtarı kapatılınca R₃ direncinde harcanan güç kaç W artar?',
 35,[(7,'Akım artışını (1 A) R₃ ile çarpıp gerilim değişimini (7 V) güç sanmış.','islem'),(28,'S açıkken R₃’te harcanan gücü (2² × 7) bulmuş; sorulan artıştır.','dikkat'),
     (30,'Üreteç gerilimi ile akım artışını çarpmış: 30 × 1 = 30 W; oysa R₃’ün gücü I²R ile bulunur.','bilgi'),(63,'Yalnız anahtar kapalıyken R₃’te harcanan gücü (3² × 7) bulmuş; farkı almamış.','dikkat')],
 'S anahtarı kapatılınca R₃ direncinde harcanan gücün artışı (W).',
 ['Anahtarın iki konumu için devreyi ayrı ayrı çiz; her durumda R₃’ten geçen akımı bulduktan sonra gücü hesapla.'],
 [B('Kısa devre','bir elemanın uçları direnci ihmal edilebilir bir iletkenle birleştirilirse akım o elemandan geçmez. Örnek: bir lambaya paralel bağlı tel, lambayı söndürür'),
  B('Elektriksel güç','bir dirençte harcanan güç P = I²R’dir. Örnek: 2 A akım geçen 5 Ω’luk dirençte 20 W harcanır')],
 [A('S açıkken akım','Üç direnç seridir.','I = 30 ÷ (3 + 5 + 7) = 2 A'),
  A('S açıkken R₃’ün gücü','Güç P = I²R.','P = 2² × 7 = 28 W'),
  A('S kapalıyken akım','R₂ kısa devre olur; R₁ ve R₃ kalır.','I′ = 30 ÷ (3 + 7) = 3 A'),
  A('S kapalıyken R₃’ün gücü','Yeni akımla güç.','P′ = 3² × 7 = 63 W'),
  A('Artışı bul','Yeni ve eski güç farkı.','ΔP = 63 − 28 = 35 W')],
 'Kısa devre edilen eleman akım taşımaz; devreyi onsuz yeniden çiz ve her durumda gücü ayrı hesapla.',sekil=tk(sk))

# ---- 20 · Kısa devre ve sigorta · öncüllü · kolay ----
sk=('\\draw (0,0) to[sV,l={$220$ V}] (0,3) to[fuse,l=sigorta] (1.9,3) -- (7.6,3); \\draw (0,0) -- (7.6,0);\n'
    '\\draw (3.4,3) to[lamp,l={$L$}] (3.4,0); \\draw (5.1,3) to[R,l=ütü] (5.1,0); \\draw[thick] (7.6,3) -- (7.6,0); \\node[rotate=90,font=\\small] at (8.15,1.5) {birbirine değen teller};\n'
    '\\fill (3.4,3) circle (1.7pt) (5.1,3) circle (1.7pt) (3.4,0) circle (1.7pt) (5.1,0) circle (1.7pt) (7.6,3) circle (1.7pt) (7.6,0) circle (1.7pt);')
O('0020','fz-el2-sigorta-kisa','Kısa devrede akımın artması ve sigortanın görevi','Sigorta ve güvenlik','kolay',
 'Kısa devrede eşdeğer direncin çok azalmasıyla akımın arttığını ve sigortanın ana kola seri bağlanarak devreyi açtığını yorumlar.',
 'Kısa devrede direnç çok küçüldüğünden akım çok artar; sigorta ana koldaki seri elemandır ve aşırı akımda eriyerek bütün devreyi açar.',
 'Sigortayı paralel sanmak; kısa devrede akımın azaldığını düşünmek.',
 'Bir evin şebeke gerilimi 220 V’tur. Şekildeki ev devresinde sigorta, bir lamba ve bir ütü şebekeye bağlıdır. Evde eskiyen bir kablonun yalıtımı soyulunca iki teli birbirine değiyor ve lamba ile ütü çalışırken sigorta atıyor. Teknisyen devredeki akımın ve sigortanın görevini inceleyerek arızanın nedenini açıklıyor.',
 [('Birbirine değen teller, devrenin eşdeğer direncini çok küçültür ve ana koldaki akımı çok artırır.',True,'Teller arasında direnç yok denecek kadar azdır; paralel kolun direnci sıfıra yaklaşır, akım çok büyür.','Kısa devrenin akımı azaltacağını, direncin artacağını sanmış.'),
  ('Sigorta, ana koldaki akım sınır değeri aşınca eriyerek devreyi açar.',True,'Sigorta ana koldaki akımı taşır; aşırı akım teli ısıtıp eritir ve bütün devrenin akımı kesilir.','Sigortanın devreyi açacak biçimde çalışmadığını düşünmüş.'),
  ('Sigorta eridiğinde yalnızca kısa devre olan kolun akımı kesilir; lamba ve ütü çalışmaya devam eder.',False,'Sigorta tüm kollara giden akımı taşıyan ana kolda seridir; eriyince hiçbir koldan akım geçmez.','Sigortanın yalnızca arızalı kolu kapatacağını düşünmüş.')],
 ['Yalnız I','I ve II','I ve III','II ve III','I, II ve III'],
 ('Sigorta ana kolda, kısa devre paralel bir kol.','Akım ana koldan geçer'),
 ['Şekilde sigortanın ve birbirine değen tellerin devreye göre konumuna bak; her yargıyı bu konuma göre sına.'],
 [B('Kısa devre','akıma karşı direnci ihmal edilebilir bir yol açılırsa akım çok artar. Örnek: pilin iki ucunu tel ile birleştirmek')],
 'Sigorta ana koldaki seri elemandır; kısa devrede akım çok artar ve sigorta devreyi tamamen açar.',sekil=tk(sk))

# ---- 21 · Sigortanın atmaması için en çok lamba sayısı · sayısal · orta ----
Us,Isg,Pu,Pl=220,16,2000,100
Pmax=Us*Isg; assert Pmax==3520
n=(Pmax-Pu)//Pl; assert n==15 and Pmax-Pu-n*Pl>=0 and Pmax-Pu-(n+1)*Pl<0
n_up=-(-(Pmax-Pu)//Pl); assert n_up==16
n_no=Pmax//Pl; assert n_no==35
n_no_up=-(-Pmax//Pl); assert n_no_up==36
n_200=(200*Isg-Pu)//Pl; assert n_200==12
sk=('\\draw (0,0) to[sV,l={$220$ V}] (0,3) to[fuse,l={$16$ A}] (1.9,3) -- (6.9,3); \\draw (0,0) -- (6.9,0);\n'
    '\\draw (3.4,3) to[R,l_={$2000$ W}] (3.4,0); \\node at (3.4,3.5) {ütü};\n'
    '\\node[draw,dashed,align=center,font=\\footnotesize,inner sep=3pt] (LB) at (6.0,1.5) {özdeş lambalar\\\\her biri $100$ W}; \\draw (6.0,3) -- (LB.north); \\draw (LB.south) -- (6.0,0);\n'
    '\\fill (3.4,3) circle (1.7pt) (6.0,3) circle (1.7pt) (3.4,0) circle (1.7pt) (6.0,0) circle (1.7pt);')
N('0021','fz-el2-sigorta-sayi','Sigortanın atmaması için çalışabilecek cihaz sayısı','Sigorta ve güvenlik','orta',
 'Sigortanın anma akımından izin verilen toplam gücü bulur ve çalışan cihazın gücünü çıkararak en çok kaç özdeş cihaz eklenebileceğini bulur.',
 'Paralel bağlı cihazların güçleri toplanır; P = V·I ile sigortanın taşıyabileceği en büyük güç bulunur; kalan güç tek cihazın gücüne bölünüp tam sayıya (aşağı) yuvarlanır.',
 'Çalışan ütüyü hesaba katmamak; sayıyı yukarı yuvarlamak; gerilimi yanlış almak.',
 'Şekildeki ev devresinde şebeke gerilimi 220 V’tur ve ana koldaki sigorta, üzerinde yazan akım değerini aşınca devreyi açmaktadır. Ütü, etiketinde yazan güçle çalışmaktadır. Aynı şebekeye, şekilde belirtilen özdeş lambalardan birbirine paralel olarak eklenecek ve lambalar da etiket güçlerinde çalışacaktır. Evde başka cihaz yoktur; tellerin ve sigortanın direnci ihmal edilmektedir.\nBuna göre, sigortanın atmaması için ütü çalışırken devreye en çok kaç özdeş lamba eklenebilir?',
 n,[(n_200,'Şebeke gerilimini yaklaşık 200 V alıp 16 × 200 = 3200 W bulmuş: (3200 − 2000) ÷ 100 = 12.','dikkat'),
    (n_up,'Kalan gücü (1520 W) lamba gücüne bölüp 15,2’yi yukarı yuvarlayarak 16 bulmuş; 16. lamba sigortayı attırır.','islem'),
    (n_no,'Ütünün de çalıştığını unutmuş: 3520 ÷ 100 = 35,2 → 35.','dikkat'),
    (n_no_up,'Ütüyü hesaba katmamış ve sonucu yukarı yuvarlamış: 3520 ÷ 100 = 35,2 → 36.','dikkat')],
 'Sigortanın atmaması için eklenebilecek en çok lamba sayısı.',
 ['Sigorta atmadan önce devreden çekilebilecek en büyük akımı düşün.'],
 [B('Elektriksel güç','P = V·I. Örnek: 220 V şebekede 5 A akım çeken cihazın gücü 1100 W’tır'),
  B('Paralel bağlı cihazlar','toplam akım, kol akımlarının toplamıdır; toplam güç cihaz güçlerinin toplamıdır')],
 [A('En büyük toplam güç','Sigorta 16 A’de atar; sınır akımdaki güç hesaplanır.','P_en çok = 220 × 16 = 3520 W'),
  A('Ütünün payını çıkar','Ütü çalışırken lambalara kalan güç.','3520 − 2000 = 1520 W'),
  A('Lamba sayısını bul','Kalan güç, bir lambanın gücüne bölünür.','1520 ÷ 100 = 15,2'),
  A('Tam sayıya yuvarla','Lamba sayısı tam sayıdır ve sınırı aşmamalıdır.','15 lamba (16 lamba 3600 W eder)')],
 'Çalışabilecek cihaz sayısı sorularında sonucu daima aşağı yuvarla; çünkü sınır aşılırsa sigorta atar.',sekil=tk(sk))

# ---- 22 · Üreteçlerin seri ve paralel bağlanması · öncüllü · orta ----
# İdeal, özdeş 1,5 V pillerde: seri → 3 V; paralel → 1,5 V; paralelde her pil akımın yarısını verir.
sk=('\\draw (0,0) to[battery1,l_={$1{,}5$ V}] (0,1.5) to[battery1,l_={$1{,}5$ V}] (0,3) -- (.4,3) to[lamp,l={$L$}] (3.0,3) -- (3.4,3) -- (3.4,0) -- (0,0);\n'
    '\\node at (1.7,-.6) {(a)};\n'
    '\\draw (6.0,0) to[battery1,l_={$1{,}5$ V}] (6.0,3) -- (8.0,3); \\draw (8.0,0) to[battery1,l_={$1{,}5$ V}] (8.0,3); \\draw (6.0,0) -- (8.0,0);\n'
    '\\draw (8.0,3) -- (8.6,3) to[lamp,l=$L$] (11.0,3) -- (11.4,3) -- (11.4,0) -- (8.0,0);\n'
    '\\node at (9.0,-.6) {(b)};')
O('0022','fz-el2-ureteç-baglama','Özdeş üreteçlerin seri ve paralel bağlanması','Üreteçlerin bağlanması','orta',
 'Özdeş ideal pillerin seri bağlanınca gerilimlerinin toplandığını, paralel bağlanınca gerilimin değişmeyip akımın paylaşıldığını yorumlar.',
 'Seri bağlı özdeş üreteçlerde emk toplanır; paralel bağlı özdeş üreteçlerde emk tek üretecinkine eşittir ve akım üreteçlerce eşit paylaşılır.',
 'Paralel bağlamada da gerilimin toplandığını sanmak; seri bağlamada gerilimin değişmediğini düşünmek; akımın paylaşılmadığını düşünmek.',
 'Bir öğrenci, aynı türden özdeş lambaları iki farklı devreyle yakıyor. (a) devresinde iki özdeş pil seri, (b) devresinde ise iki özdeş pil paralel bağlanmıştır. Piller ideal kabul edilmekte, her pilin emk’sı şekilde verilmektedir ve devrelerdeki lambaların dirençleri sabittir. Bağlantı tellerinin direnci ihmal edilmektedir.',
 [('(a) devresinde lambanın uçları arasındaki gerilim 3 V’tur.',True,'Seri bağlı özdeş pillerin emk’ları toplanır: 1,5 + 1,5 = 3 V.','Seri bağlı pillerin gerilimlerinin toplanmadığını düşünmüş.'),
  ('(b) devresinde lambanın uçları arasındaki gerilim 1,5 V’tur.',True,'Paralel bağlı özdeş pillerin uçları arasındaki gerilim tek bir pilinkine eşittir.','Paralel bağlamada da pil gerilimlerinin toplandığını (3 V) sanmış.'),
  ('(b) devresinde her pilden geçen akım, lambadan geçen akımın yarısıdır.',True,'Özdeş pillerin her biri aynı gerilimi sağladığından lambanın akımını eşit paylaşırlar.','Lambanın akımının tek bir pilden geçtiğini ya da pillerin akım paylaşmadığını düşünmüş.')],
 ['Yalnız I','I ve II','I ve III','II ve III','I, II ve III'],
 ('(a): pil gerilimleri toplanır; (b): paralel → gerilim aynı.','V_a = 3 V, V_b = 1,5 V'),
 ['Her devrede lambaya uygulanan gerilimi pil bağlantısına göre belirle; paralelde akımın piller arasında nasıl dağıldığını düşün.'],
 [B('Üreteçlerin seri bağlanması','özdeş ideal üreteçlerin emk’ları toplanır. Örnek: 1,5 V’luk üç pil seri bağlanınca 4,5 V elde edilir'),
  B('Üreteçlerin paralel bağlanması','özdeş üreteçlerin emk’sı değişmez; devre akımı üreteçler arasında eşit paylaşılır, piller daha uzun süre dayanır')],
 'Seri bağlama gerilimi artırır; paralel bağlama gerilimi değiştirmez, yalnız her pilin yükünü azaltır.',sekil=tk(sk))

# ---- 23 · Akım–zaman grafiğinden yük · sayısal · kolay ----
Qg=2*10+4*5+1*5; assert Qg==45
g1=(2+4+1)*5; g2=2*10+4*5; g3=4*20; g4=2+4+1
assert (g1,g2,g3,g4)==(35,40,80,7)
gx=['\\begin{axis}['+GR+',xmin=0,xmax=20,ymin=0,ymax=5,xtick={0,5,10,15,20},ytick={0,1,2,3,4,5},xlabel={$t$ (s)},ylabel={$I$ (A)}]',
    '\\addplot[thick,vurgu,no marks] coordinates {(0,2)(10,2)(10,4)(15,4)(15,1)(20,1)};','\\end{axis}']
N('0023','fz-el2-akim-yuk','Akım–zaman grafiğinden geçen yük','Elektrik akımı','kolay',
 'Akım–zaman grafiğinde eğri altında kalan alanın geçen yükü verdiğini kullanarak toplam yükü hesaplar.',
 'Elektrik akımı birim zamanda geçen yüktür (Q = I·t); akım sabit aralıkların her birinde yük ayrı bulunup toplanır.',
 'Aralık sürelerini eşit almak; akımları toplamak; en büyük akımla bütün süreyi çarpmak; bir aralığı atlamak.',
 'Bir cep telefonu şarj edilirken şarj kablosundan geçen akım, ampermetreyle her an kaydedilmiş ve zamanla değişimi şekildeki grafiğe aktarılmıştır. Akım değişimleri her aralıkta ani olup aralıklarda akım sabit kalmıştır.\nBuna göre, kablonun kesitinden ilk 20 saniyede geçen toplam yük kaç C’dur?',
 Qg,[(g4,'Akım değerlerini (2 + 4 + 1) toplayıp süreyle çarpmayı unutmuş.','islem'),(g1,'Üç aralığı da 5 s alıp (2 + 4 + 1) × 5 = 35 C bulmuş; ilk aralığın 10 s olduğunu okumamış.','dikkat'),
     (g2,'Son aralığı (15–20 s) hesaba katmamış: 2 × 10 + 4 × 5 = 40 C.','dikkat'),(g3,'En büyük akımı (4 A) bütün süreyle (20 s) çarpmış: 80 C.','bilgi')],
 'İlk 20 saniyede kablodan geçen toplam yük (C).',
 ['Akımın sabit kaldığı aralıkları ayırıp her aralığın süresini ve akımını grafikten oku.'],
 [B('Elektrik yükü','Q = I · t. Örnek: 3 A akım 5 s sürerse kesitten 15 C yük geçer'),
  B('I–t grafiği','eğrinin altında kalan alan, geçen toplam yükü verir')],
 [A('0–10 s aralığı','Akım 2 A’dir.','Q₁ = 2 × 10 = 20 C'),
  A('10–15 s aralığı','Akım 4 A’dir.','Q₂ = 4 × 5 = 20 C'),
  A('15–20 s aralığı','Akım 1 A’dir.','Q₃ = 1 × 5 = 5 C'),
  A('Toplam yük','Üç aralığın yükleri toplanır.','Q = 20 + 20 + 5 = 45 C')],
 'Akımı sabit aralıklara böl; her aralık için I × t hesapla ve topla.',sekil=tikz_svg(HEAD+'\n'.join(gx)+TAIL),kalip='grafik')

# ---- 24 · Ölçü aletlerinin bağlanması · öncüllü · orta ----
# A, R2 koluna seri → R2 kol akımını ölçer (ana akım değil): I yanlış. R3 akımı R1'den (ana akım) küçük: II yanlış.
# V, R3'e paralel; R2 ile R3 paralel kollar → V aynı zamanda R2 gerilimini gösterir: III doğru.
sk=('\\draw (0,0) to[battery1,l={$\\varepsilon$}] (0,3) to[R,l={$R_1$}] (2.4,3) -- (6,3); \\draw (0,0) -- (7.6,0);\n'
    '\\draw (3.6,3) to[R,l={$R_2$}] (3.6,1.5); \\node[draw,circle,minimum size=.7cm,inner sep=0pt] (A) at (3.6,.7) {A}; \\draw (3.6,1.5) -- (A.north); \\draw (A.south) -- (3.6,0);\n'
    '\\draw (6,3) to[R,l={$R_3$}] (6,0); \\node[draw,circle,minimum size=.7cm,inner sep=0pt] (V) at (7.6,1.5) {V}; \\draw (6,3) -- (7.6,3) -- (V.north); \\draw (V.south) -- (7.6,0);\n'
    '\\fill (3.6,3) circle (1.7pt) (6,3) circle (1.7pt) (3.6,0) circle (1.7pt) (6,0) circle (1.7pt);')
O('0024','fz-el2-olcu-aletleri','Ampermetre ve voltmetrenin ölçtüğü büyüklükler','Ampermetre ve voltmetre','orta',
 'Ampermetrenin seri, voltmetrenin paralel bağlandığını kullanarak ölçü aletlerinin hangi akım ve gerilimi ölçtüğünü yorumlar.',
 'Ampermetre bağlı olduğu koldaki akımı ölçer; voltmetre paralel bağlandığı elemanın gerilimini gösterir; paralel kolların gerilimi ortaktır.',
 'Ampermetrenin ana kol akımını ölçtüğünü sanmak; voltmetrenin yalnızca paralel olduğu dirençte okuma yaptığını düşünmek.',
 'Şekildeki devrede üreteç, ampermetre ve voltmetre idealdir; R₁, R₂ ve R₃ dirençlerinin değerleri birbirinden farklı ve bilinmemektedir. Devre sürekli akım durumundadır ve bağlantı telleri ile ölçü aletlerinin bağlantı noktaları için direnç ihmal edilmektedir. Öğrenci, ölçü aletlerinin neyi ölçtüğünü yorumluyor.',
 [('A ampermetresi, üreteçten çekilen toplam akımı gösterir.',False,'A yalnız R₂ koluna seri bağlıdır; bu kolun akımını ölçer. Ana kol akımı R₃ koluna giden akımı da içerir.','Ampermetrenin her zaman ana kol akımını ölçtüğünü düşünmüş.'),
  ('R₃ direncinden geçen akım, R₁ direncinden geçen akımdan büyüktür.',False,'R₁ ana koldadır ve hem R₂ hem R₃ koluna giden akımı taşır; R₃’ten geçen akım bunun yalnızca bir kısmıdır.','Paralel bir kolun akımının ana kol akımından büyük olabileceğini düşünmüş.'),
  ('V voltmetresi, R₂ direncinin uçları arasındaki gerilimi de gösterir.',True,'V, R₃’e paraleldir; R₂ ile R₃ paralel kollar olduğundan uçları arasındaki gerilim ortaktır.','Voltmetrenin yalnızca bağlı olduğu dirençteki gerilimi gösterdiğini düşünmüş.')],
 ['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III'],
 ('A, R₂ koluna seri; V, R₃’e paralel; R₂ ve R₃ paralel kollar.','Paralel kollarda V ortak'),
 ['Her ölçü aletinin hangi eleman(lar)a seri ya da paralel bağlı olduğunu belirleyip akım ve gerilimin nerede ortak olduğunu düşün.'],
 [B('Ampermetre ve voltmetre','ampermetre ölçülecek koldaki elemana seri, voltmetre ise elemana paralel bağlanır'),
  B('Paralel kollar','kolların uçları arasındaki gerilim ortaktır; ana koldaki akım kol akımlarının toplamıdır')],
 'Ampermetre bağlı olduğu kolun, voltmetre paralel olduğu kolların ortak gerilimini gösterir.',sekil=tk(sk))

# ---- 25 · Elektrik güvenliği · öncüllü · kolay (şekilsiz) ----
O('0025','fz-el2-guvenlik','Elektrik güvenliği (topraklama, ıslak eller, sigorta)','Sigorta ve güvenlik','kolay',
 'Topraklı priz, ıslak elle dokunma ve sigorta kullanımının güvenlik açısından nedenlerini yorumlar.',
 'Topraklı priz kaçak akıma düşük dirençli yol sunar; ıslak deri direnci azaltır ve akımı artırır; sigorta yerine kalın tel takmak devre korumasını kaldırır.',
 'Islak elin direnci artırdığını sanmak; kalın telin sigortadan daha güvenli olduğunu düşünmek.',
 'Bir sitede elektrik tesisatı bakımı yapan teknisyen, apartman sakinlerine güvenlik konusunda bir konuşma yapıyor. Teknisyen; çamaşır makinesinin metal gövdesine kaçan akımın nasıl bir yol izlediğini, ıslak ellerle prize dokunmanın neden tehlikeli olduğunu ve atan bir sigortanın yerine ne takılması gerektiğini anlatıyor ve şu yargılarda bulunuyor.',
 [('Topraklı prizde cihaz gövdesine kaçan akım, topraklama hattıyla toprağa gider ve kullanıcının üzerinden çok az akım geçer.',True,'Topraklama hattı, insan vücuduna göre çok düşük dirençli bir yol sunar; kaçak akım büyük ölçüde bu hattan toprağa akar.','Topraklama hattının kaçak akımı çekmediğini, akımın hep kullanıcıdan geçtiğini düşünmüş.'),
  ('Islak ellerle elektrikli aletlere dokunmak, kuru ellere göre daha güvenlidir.',False,'Islak elin direnci kuru elden küçüktür; aynı gerilimde vücuttan geçen akım artar ve çarpılma tehlikesi büyür, yani ıslak elle dokunmak daha tehlikelidir.','Suyun direnci artırdığını, ıslak elin daha güvenli olduğunu düşünmüş.'),
  ('Sigorta yerine daha kalın bir tel takılırsa devre daha güvenli çalışır.',False,'Kalın tel, aşırı akımda erimez; sigortanın koruma görevi ortadan kalkar ve kablolar aşırı ısınıp yangına neden olabilir.','Telin kalın olmasını daha dayanıklı ve güvenli sanmış.')],
 ['Yalnız I','Yalnız III','I ve II','I ve III','II ve III'],
 ('Topraklama, ıslak el, sigorta yerine tel.','Güvenlik kuralları'),
 ['Her yargıda akımın hangi yoldan geçeceğini ve direncin nasıl değiştiğini düşün.'],
 [B('Topraklama','metal gövdeli cihazlarda kaçak akımı toprağa ileten düşük dirençli yoldur. Örnek: topraklı prizdeki üçüncü bağlantı ucu'),
  B('Sigorta','aşırı akımda eriyip devreyi açan, devreye seri bağlı koruma elemanıdır; yerine tel takılmaz')],
 'Güvenlik önlemleri akımı insan vücudundan uzak tutmak ve aşırı akımı kesmek içindir.')

# ---- 26 · Telin boyu ve çapı değişince direnç · sayısal · orta ----
R1w=8; R2w=R1w*Fr(3)/(Fr(2)**2); assert R2w==6
w1=R1w*Fr(3,2); assert w1==12            # çapın karesini almamış (kesit ∝ d²)
w2=R1w*3; assert w2==24                  # çapı hesaba katmamış
w3=R1w*3*2; assert w3==48                # kesit arttıkça direnç artar sanmış
w4=R1w*3*4; assert w4==96                # kesit etkisini ters uygulamış (4 ile çarpmış)
sk=('\\draw[thick,fill=gray!15] (0,.5) rectangle (3,1.0); \\draw[<->] (0,1.35) -- (3,1.35); \\node[fill=white,inner sep=1pt] at (1.5,1.35) {$\\ell$};'
    '\\draw[<->] (3.35,.5) -- (3.35,1.0); \\node[right] at (3.35,.75) {$d$}; \\node at (1.5,-.05) {1. tel: $R_1=8\\,\\Omega$};\n'
    '\\draw[thick,fill=gray!15] (0,-2.0) rectangle (9,-1.0); \\draw[<->] (0,-.7) -- (9,-.7); \\node[fill=white,inner sep=1pt] at (4.5,-.7) {$3\\ell$};'
    '\\draw[<->] (9.35,-2.0) -- (9.35,-1.0); \\node[right] at (9.35,-1.5) {$2d$}; \\node at (4.5,-2.5) {2. tel: $R_2=?$};')
N('0026','fz-el2-tel-cap','Telin boyu ve çapı değişince direncin değişimi','Direncin bağlı olduğu etkenler','orta',
 'Telin direncinin uzunlukla doğru, kesit alanıyla (çapın karesiyle) ters orantılı olduğunu kullanarak yeni direnci bulur.',
 'R = ρ·ℓ ÷ A ve kesit A ∝ d²; uzunluk 3 katına, çap 2 katına çıkarsa direnç 3 ÷ 2² = 3/4 katı olur.',
 'Kesit yerine çapı oranlamak; kesit arttığında direncin arttığını sanmak; çapı hesaba katmamak.',
 'Bir öğrenci, aynı maddeden yapılmış iki telin direncini karşılaştırıyor. Teller silindir biçimli, homojen ve dairesel kesitlidir; ikisi de aynı sıcaklıktadır. Tellerin boyları ile çapları ve birinci telin direnci şekilde verilmiştir.\nBuna göre, ikinci telin direnci R₂ kaç Ω’dur?',
 R2w,[(w1,'Kesit alanını çapla orantılı sanmış (çapın karesini almamış): 8 × 3 ÷ 2 = 12 Ω.','bilgi'),(w2,'Çap farkını hesaba katmamış; yalnız boyun 3 katına çıktığını görmüş: 8 × 3 = 24 Ω.','dikkat'),
      (w3,'Kesiti çapla orantılı alıp direnci de kesitle doğru orantılı sanmış: 8 × 3 × 2 = 48 Ω.','bilgi'),(w4,'Kesit alanının 4 katına çıkmasını direnci 4 katı artırıyormuş gibi uygulamış: 8 × 3 × 4 = 96 Ω.','bilgi')],
 'İkinci telin direnci (Ω).',
 ['Direnci belirleyen üç büyüklüğü ayrı ayrı yaz.'],
 [B('Telin direnci','R = ρ·ℓ ÷ A; dairesel kesitte A = π·d² ÷ 4 olduğundan A, çapın karesiyle orantılıdır. Örnek: çap yarıya inerse kesit dörtte birine düşer')],
 [A('Kesit değişimi','Dairesel kesitte alan çapın karesiyle orantılıdır; çap 2 katına çıkmıştır.','A₂ = 4 · A₁'),
  A('Uzunluk değişimi','Uzunluk 3 katına çıkmıştır.','ℓ₂ = 3 · ℓ₁'),
  A('Direnci oranla','Direnç uzunlukla doğru, kesitle ters orantılıdır.','R₂ = R₁ × 3 ÷ 4'),
  A('Sonuç','Birinci telin direnci 8 Ω’dur.','R₂ = 8 × 3 ÷ 4 = 6 Ω')],
 'Çap ya da yarıçap verilirse kesit alanını mutlaka karesiyle oranla.',sekil=tk(sk))

bitir(P,'elektrikiki','fiz|Elektrik')
