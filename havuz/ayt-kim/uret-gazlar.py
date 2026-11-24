"""AYT Kimya · Gazlar · 20 soru (kardeş yok, ipucu 1). Şekil değerleri Python'da hesaplanır; her cevap ve çeldirici assert edilir."""
import sys,os,math,json,itertools
from fractions import Fraction as Fr
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-kim')); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
import _hafif_kim2 as H
from _hafif_kim2 import *
from _hafif_kim import onc as _onc, tek
from cizim import tikz_svg
KONU_='Gazlar'; UK='akim|Gazlar'
H.KONU=KONU_
P=Parti('gazlar',KONU_,UK,ders='AYT Kimya',idon='aytkim')
KY='ÖSYM AYT 2018–2026 Kimya (Gazlar; yalnız mantık) · MEB 11. sınıf kimya'
TIPLER={'gz-yasa':'Gaz yasaları (Boyle, Charles, Gay-Lussac)','gz-ideal':'İdeal gaz denklemi, yoğunluk ve mol kütlesi','gz-kismi':'Kısmi basınç ve gaz karışımları',
 'gz-difuz':'Difüzyon ve efüzyon','gz-kinetik':'Gazların kinetik teorisi','gz-gercek':'Gerçek gazlar','gz-manometre':'Manometre ile basınç ölçümü',
 'gz-piston':'Piston düzenekleri','gz-sutop':'Su üzerinde gaz toplama ve stokiyometri'}
CARD={}
def card(no,alt,fikir,tuzak,z,kalip,adim,tipId,ozet):
    kart(f'K-AKGAZ-{no:02d}',alt,fikir,tuzak,z,kalip,adim,tipId,TIPLER[tipId],KY); CARD[no]=ozet
def q(no,ad,**k):
    kn=int(no); mk(P,no,ad=ad,adim=len(ad),kart=f'K-AKGAZ-{kn:02d} ('+CARD[kn]+')',**k)
def F(s): return Fr(str(s).replace(',','.'))
def tr(x):  # Türkçe ondalık
    return fm(Fr(x))
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
ARR='-{Stealth[length=1.9mm,width=1.7mm]}'
DARR='{Stealth[length=1.7mm,width=1.5mm]}-{Stealth[length=1.7mm,width=1.5mm]}'
def tk(g): return tikz_svg(HEAD+g+TAIL)
def onc_neg(d,ops):
    """Olumsuz kök: d[x]=(yanlış_mı,açıklama). Doğru küme = yanlış öncüller."""
    Tm=frozenset(k for k,v in d.items() if v[0]); ops=[tuple(o) for o in ops]; assert len(ops)==5 and len(set(ops))==5
    ad=lambda s:('Yalnız '+s[0]) if len(s)==1 else (' ve '.join(s) if len(s)==2 else ', '.join(s[:-1])+' ve '+s[-1])
    es=[o for o in ops if frozenset(o)==Tm]; assert len(es)==1
    yan=[]
    for o in ops:
        if frozenset(o)==Tm: continue
        W=frozenset(o); p=[]
        for x in sorted(W-Tm): p.append(f'{x} öncülünü yanlış sanmış; oysa {x} doğrudur: {d[x][1]}')
        for x in sorted(Tm-W): p.append(f'{x} öncülünü doğru sanıp işaretlememiş; oysa {x} yanlıştır: {d[x][1]}')
        yan.append((ad(o),'. '.join(p)+'.','bilgi'))
    return dict(dogru=ad(es[0]),yan=yan,sira=[ad(o) for o in ops])
def oy(d): return ' · '.join(f'{k}: '+('doğru' if v[0] else 'yanlış') for k,v in d.items())
def oyn(d): return ' · '.join(f'{k}: '+('yanlış' if v[0] else 'doğru') for k,v in d.items())
def N(x,y,t,o=''): return f'\\node[{o}] at ({x:.3f},{y:.3f}) {{{t}}};'

# ============ kartlar ============
card(1,'Boyle yasası','Sabit sıcaklıkta ve sabit mol sayısında P·V çarpımı sabittir; tablodaki üç durum için aynı çarpım kullanılır.','P ile V’yi doğru orantılı sanmak; P + V toplamını sabit almak.','kolay','tablo',3,'gz-yasa','sabit T’de P·V tablosu')
card(2,'Kinetik teori yargıları','İdeal gazda moleküller arası çekim yoktur; ortalama kinetik enerji yalnız sıcaklığa, ortalama hız ise hem sıcaklığa hem mol kütlesine bağlıdır.','Aynı sıcaklıkta hızları da eşit sanmak.','kolay','öncüllü',3,'gz-kinetik','ideal gaz varsayımları')
card(3,'Charles yasası','Sabit basınçta V/T sabittir ve T mutlaka Kelvin cinsinden alınır.','Sıcaklığı °C ile oranlamak; ters orantı kurmak.','kolay','hikâyeli',2,'gz-yasa','sabit P’de V–T oranı')
card(4,'P–V grafiğinden sıcaklık','Aynı miktar gazın aynı hacimdeki basınç oranı mutlak sıcaklık oranına eşittir; sonuç istenen birime çevrilir.','°C değerlerini doğrudan oranlamak; sonucu Kelvin bırakmak.','orta','grafik',4,'gz-yasa','iki izotermden T oranı')
card(5,'Bölmeli kapta denge','Sürtünmesiz piston dengede iken iki bölmede basınç eşittir; bu durumda V ∝ n·T olur.','Yalnız mol sayısına bakıp sıcaklığı yok saymak; pistonu ortada sanmak.','orta','şekilli',4,'gz-piston','ısı yalıtkan pistonla bölmeli kap')
card(6,'Açık uçlu manometre','Gaz basıncı, açık hava basıncına cıva seviye farkının eklenmesi ya da çıkarılmasıyla bulunur; cıvanın hangi kolda yüksekte olduğuna bakılır.','Farkı her durumda toplamak; cmHg ile atm’yi karıştırmak.','orta','şekilli',3,'gz-manometre','gaz basıncı açık hava basıncından küçük')
card(7,'Manometre ve sıcaklık','Sabit hacimde P/T sabittir; yeni basınç bulunup açık hava basıncıyla karşılaştırılarak yeni seviye farkı okunur.','Seviye farkını doğrudan sıcaklıkla orantılamak; açık hava basıncını çıkarmayı unutmak.','zor','şekilli',5,'gz-manometre','manometre + Gay-Lussac')
card(8,'Su üzerinde gaz toplama','Toplanan gazın kısmi basıncı toplam basınçtan su buhar basıncı çıkarılarak bulunur; mol sayısı denklem katsayılarıyla bağlanır.','Toplam basıncı gaz basıncı saymak; katsayı oranını ters kullanmak.','zor','şekilli',6,'gz-sutop','O₂ su üstünde toplanır, bozunan KClO₃')
card(9,'Farklı sıcaklıkta bağlı kaplar','Önce her kaptaki P·V/T (= nR) bulunur, toplanır; son sıcaklıkta toplam hacimde basınç hesaplanır.','Sıcaklıkları yok saymak; basınçların ortalamasını almak.','zor','şekilli',5,'gz-kismi','iki kap, farklı T, son T')
card(10,'Kısmi basınç ve mol kesri','Kısmi basınç = mol kesri × toplam basınç; aynı T’de ortalama kinetik enerji eşittir.','Kütle oranını mol oranı sanmak; kinetik enerjiyi mol kütlesiyle ilişkilendirmek.','orta','tablo',4,'gz-kismi','kütle ve mol kütlesi tablosu')
card(11,'Graham yasası','Difüzyon hızı mol kütlesinin kareköküyle ters orantılıdır; aynı sürede alınan yollar hız oranındadır.','Hızı mol kütlesiyle doğrudan ilişkilendirmek; karekökü almamak.','orta','şekilli',4,'gz-difuz','tüpte karşılaşma noktası')
card(12,'Eşit kütle, mol sayısı ve hız','Eşit kütlede mol sayısı mol kütlesiyle ters orantılıdır; efüzyon hızı oranı mol kütleleri oranının kareköküdür.','Hız oranını mol kütle oranına eşitlemek.','orta','öncüllü',4,'gz-difuz','eşit kütlede H₂ ve CH₄')
card(13,'Yoğunluktan mol kütlesi','d = P·M/(R·T) bağıntısı doğrudan kullanılır; NŞA değerleri farklı koşullara uygulanmaz.','NŞA sanmak; P’yi çarpmak ya da unutmak.','orta','düz',3,'gz-ideal','verilen koşulda d’den M')
card(14,'Piston, yük ve sıcaklık','Piston dengede iken gaz basıncı dış basınç ve yükün toplamına eşittir; birleşik gaz yasası P1V1/T1 = P2V2/T2.','P’yi doğru orantılı kullanmak; yük eklenince hacmin artacağını sanmak.','zor','şekilli',5,'gz-piston','yük + ısıtma sonrası hacim')
card(15,'Gerçek gazlar','Z = PV/nRT; düşük basınçta her gaz ideale yakındır, orta basınçta çekim kuvvetleri Z’yi 1’in altına çeker, yüksek basınçta molekül hacmi Z’yi 1’in üstüne çıkarır.','Çekim kuvveti zayıf gazın da Z’sini 1’in altında sanmak.','orta','grafik',4,'gz-gercek','Z–P grafiği, He ve CH₄')
card(16,'Yoğunluk–basınç grafiği','Sabit T’de d = (M/RT)·P doğrusunun eğimi mol kütlesiyle doğru orantılıdır; sıcaklık artınca eğim küçülür.','Eğimin sıcaklıkla arttığını sanmak.','orta','grafik',4,'gz-ideal','d–P doğruları')
card(17,'Hız dağılımı grafiği','Sıcaklık artınca dağılım genişler ve sağa kayar, tepe yüksekliği düşer; eğri altındaki alan molekül sayısını gösterir ve değişmez.','Yüksek sıcaklıkta tüm moleküllerin daha hızlı olduğunu sanmak.','orta','grafik',4,'gz-kinetik','Maxwell hız dağılımı')
card(18,'Efüzyon süreleri','Aynı koşullarda efüzyon süresi mol kütlesinin kareköküyle doğru orantılıdır; süre oranının karesi mol kütle oranını verir.','Süre oranını doğrudan ya da karekökünü mol kütle oranı almak.','orta','tablo',3,'gz-difuz','efüzyon süresi tablosu')
card(19,'Tepkime sonrası basınç','Sabit hacim ve sıcaklıkta basınç gazın mol sayısıyla orantılıdır; sınırlayıcı bileşen bulunup son mol sayısı yazılır.','Mol sayısının korunduğunu sanmak; suyu sıvı saymak.','zor','şekilli',5,'gz-kismi','H₂ + O₂ karışımının tepkimesi')
card(20,'Sabit dış basınçta gaz ekleme','Piston dış basıncı sabit tutar; toplam basınç değişmez, kısmi basınç mol kesriyle belirlenir.','Toplam basınçla kısmi basıncı karıştırmak; mol kesrini yanlış hesaplamak.','zor','şekilli',4,'gz-kismi','pistonlu kapta ikinci gaz eklenir')

# ============ 0001 · Boyle tablosu · kolay ============
P1,V1=2,12; K1=P1*V1; Pb=3; X1=Fr(K1,Pb); Vc=4; Y1=Fr(K1,Vc); assert (X1,Y1)==(8,6) and X1+Y1==14
yp=(Pb+V1+0)  # yardımcı
a_sum=(P1+V1); X_t=a_sum-Pb; Y_t=a_sum-Vc; assert X_t+Y_t==21 and X1*Y1==48
sk=tablo_svg(['Durum','Basınç (atm)','Hacim (L)'],[['I','2','12'],['II','3','X'],['III','Y','4']])
q('0001',[A('Sabit çarpımı bul','Sıcaklık ve mol sayısı sabit olduğundan P·V çarpımı her durumda aynıdır.','I: 2 × 12 = 24'),
 A('X’i hesapla','II. durumda basınç 3 atm olduğundan hacim 24 ÷ 3 bulunur.','3 × X = 24 → X = 8 L'),
 A('Y’yi hesapla','III. durumda hacim 4 L olduğundan basınç 24 ÷ 4 bulunur.','Y × 4 = 24 → Y = 6 atm'),
 A('İstenen toplamı yaz','Soru X ile Y’nin toplamını sorar.','X + Y = 8 + 6 = 14')],
 metin='Sabit sıcaklıkta, mol sayısı değişmeyen ideal bir gaz örneği üç farklı durumda ölçülmüş ve sonuçlar aşağıdaki tabloda verilmiştir.\nBuna göre X ile Y sayılarının toplamı kaçtır?',
 sekil=sk,dogru=14,yan=[(8,'Yalnız X’i (8) bulup Y’yi hesaplayıp toplamayı unutmuş.','dikkat'),
  (21,'P·V çarpımı yerine P + V toplamını sabit almış (14): X = 14 − 3 = 11, Y = 14 − 4 = 10, toplam 21.','bilgi'),
  (48,'X ile Y’nin toplamı yerine çarpımını almış: 8 × 6 = 48.','dikkat'),(6,'Yalnız Y’yi (6) bulup X’i toplama katmamış.','dikkat')],
 istenen='X ve Y değerlerinin toplamı.',ip=['Sabit sıcaklıkta basınç ve hacim arasındaki ilişkiyi bir çarpım olarak ifade etmeyi dene.'],
 bilgi=[B('Boyle yasası','Sabit sıcaklıkta ve sabit mol sayısında gazın basıncı ile hacmi ters orantılıdır: P·V = sabit. Örnek: 5 atm ve 4 L’lik bir gaz 10 atm’e sıkıştırılırsa hacmi 2 L olur')],
 puf='Sabit T ve n’de P ile V ters orantılıdır; hangisi artarsa çarpım sabit kalacak şekilde diğeri azalır.',
 tipId='gz-yasa',tip=TIPLER['gz-yasa'],z='kolay',alt='Gaz Yasaları',kaz='Sabit sıcaklıkta basınç–hacim verilerinden Boyle yasasıyla bilinmeyenleri hesaplar.',kalip='tablo')

# ============ 0002 · kinetik teori · kolay · öncüllü ============
d={'I':(False,'ideal gazda moleküller arasında çekim ya da itme kuvveti yoktur; bu, ideal gaz varsayımlarından biridir'),
   'II':(True,'ortalama kinetik enerji mutlak sıcaklıkla doğru orantılıdır; sıcaklık arttıkça artar'),
   'III':(False,'aynı sıcaklıkta ortalama kinetik enerji eşittir ancak ortalama hız mol kütlesine bağlıdır: hafif moleküller daha hızlıdır')}
r=_onc(d,[('II',),('III',),('I','II'),('I','III'),('II','III')])
q('0002',[A('İdeal gaz modelini hatırla','Ideal gazda moleküllerin hacmi ve aralarındaki etkileşim ihmal edilir.','I: çekim yok → yanlış'),
 A('Sıcaklık–enerji ilişkisi','Ortalama kinetik enerji yalnızca mutlak sıcaklığa bağlıdır.','II: doğru'),
 A('Hız–mol kütlesi ilişkisi','E = ½·m·v² olduğundan eşit enerjide kütlesi küçük olan molekül daha hızlıdır.','III: yanlış'),
 A('Sonucu yaz','Doğru öncüller bir arada yazılır.',oy(d)+' · Sonuç: '+r['dogru'])],
 metin='Bir öğrenci, kapalı kaplardaki gazların davranışını açıklayan kinetik teoriyi araştırıyor ve ideal gaz kabulüne uyan gazlarla ilgili aşağıdaki yargıları not alıyor.\nI. Gaz molekülleri arasında zayıf da olsa çekim kuvveti bulunur.\nII. Sıcaklık arttıkça gaz moleküllerinin ortalama kinetik enerjisi artar.\nIII. Aynı sıcaklıktaki bütün gazların moleküllerinin ortalama hızı birbirine eşittir.\nBuna göre bu yargılardan hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',
 ip=['Ortalama kinetik enerjiyi kütle ve hızla ilişkilendiren bağıntıyı düşün.'],
 bilgi=[B('Kinetik teori','İdeal gazda moleküller arası etkileşim yoktur, molekül hacmi ihmal edilir. Ortalama kinetik enerji yalnız mutlak sıcaklığa bağlıdır. Örnek: 300 K’deki bütün gazların ortalama kinetik enerjisi eşittir')],
 puf='Aynı sıcaklıkta enerji eşit, hız eşit değildir; hafif gaz daha hızlıdır.',
 tipId='gz-kinetik',tip=TIPLER['gz-kinetik'],z='kolay',alt='Gazların Kinetik Teorisi',kaz='İdeal gaz varsayımlarını ve ortalama kinetik enerjinin sıcaklıkla ilişkisini yorumlar.',kalip='öncüllü')

# ============ 0003 · Charles · kolay ============
V3=6; T3a=F(27)+273; T3b=F(177)+273; V3b=V3*T3b/T3a
assert (T3a,T3b,V3b)==(300,450,9)
e4=V3*T3a/T3b; e354=V3*F(177)/T3a; e100=V3*T3b/F(27); assert (e4,e354,e100)==(4,F('3.54'),100)
q('0003',[A('Sıcaklıkları Kelvin’e çevir','Gaz yasalarında sıcaklık mutlak ölçekte kullanılır: T = t + 273.','T₁ = 27 + 273 = 300 K · T₂ = 177 + 273 = 450 K'),
 A('Charles yasasını yaz','Basınç sabit olduğundan hacim mutlak sıcaklıkla doğru orantılıdır.','V₁ ÷ T₁ = V₂ ÷ T₂'),
 A('Son hacmi hesapla','Verileri yerine koy.','6 ÷ 300 = V₂ ÷ 450 → V₂ = 9 L')],
 metin='Sürtünmesiz ve hareketli bir pistonla kapatılmış kapta bulunan ideal gazın dış basıncı sabittir. Gazın sıcaklığı 27 °C iken hacmi 6 L ölçülüyor. Dış basınç değiştirilmeden gaz 177 °C’ye kadar ısıtılıyor.\nBuna göre gazın son hacmi kaç litre olur?',
 dogru=9,yan=[(F('3.54'),'Yalnız ilk sıcaklığı Kelvin’e çevirmiş: V₂ = 6 × 177 ÷ 300 = 3,54 L.','islem'),(4,'Hacmi sıcaklıkla ters orantılı almış: V₂ = 6 × 300 ÷ 450 = 4 L.','bilgi'),
  (6,'Basınç sabit olduğu için hacmin de değişmeyeceğini düşünmüş; oysa sabit basınçta sıcaklık artınca hacim artar.','bilgi'),(100,'Yalnız son sıcaklığı Kelvin’e çevirmiş: V₂ = 6 × 450 ÷ 27 = 100 L.','islem')],
 istenen='Gazın 177 °C’deki hacmi (L).',ip=['Hangi büyüklüğün sabit tutulduğuna bakarak hacim ile sıcaklık arasındaki ilişkiyi belirle ve birimleri kontrol et.'],
 bilgi=[B('Charles yasası','Sabit basınçta ve sabit mol sayısında gazın hacmi mutlak sıcaklıkla doğru orantılıdır: V ÷ T = sabit. Örnek: 2 L’lik gaz, mutlak sıcaklığı 2 katına çıkarsa 4 L olur')],
 puf='Gaz yasalarında önce °C değerlerini Kelvin’e çevir; oran kurmayı sonra yap.',
 tipId='gz-yasa',tip=TIPLER['gz-yasa'],z='kolay',alt='Gaz Yasaları',kaz='Sabit basınçta sıcaklık değişiminden hacmi Charles yasasıyla hesaplar.',kalip='hikâyeli')

# ============ 0004 · P–V grafiği · orta ============
C1,C2=12,16; T4=F(27)+273; T4b=T4*C2/C1; assert T4b==400 and T4b-273==127
assert T4*C1/C2-273==-48 and F(27)*C2/C1==36 and T4b-T4==100
sx,sy=.75,.55
g=[]
g.append(f'\\draw[->,thick] (0,0) -- ({8.8*sx:.2f},0) node[below right] {{$V$ (L)}};')
g.append(f'\\draw[->,thick] (0,0) -- (0,{9*sy:.2f}) node[above] {{$P$ (atm)}};')
for v in (2,4,6,8): g.append(f'\\draw ({v*sx:.2f},.07) -- ({v*sx:.2f},-.07) node[below] {{{v}}};')
for p in (2,4,6,8): g.append(f'\\draw (.07,{p*sy:.2f}) -- (-.07,{p*sy:.2f}) node[left] {{{p}}};')
g.append(f'\\draw[thick,domain=1.5:8,samples=50,smooth,variable=\\v] plot ({{\\v*{sx}}},{{{C1}/\\v*{sy}}});')
g.append(f'\\draw[thick,vurgu,dashed,domain=2:8,samples=50,smooth,variable=\\v] plot ({{\\v*{sx}}},{{{C2}/\\v*{sy}}});')
g.append(f'\\draw[dotted] (0,{6*sy:.2f}) -- ({2*sx:.2f},{6*sy:.2f}) -- ({2*sx:.2f},0); \\draw[dotted] (0,{8*sy:.2f}) -- ({2*sx:.2f},{8*sy:.2f});')
g.append(f'\\fill ({2*sx:.2f},{6*sy:.2f}) circle (1.6pt); \\fill[vurgu] ({2*sx:.2f},{8*sy:.2f}) circle (1.6pt);')
g.append(f'\\node at ({7.2*sx:.2f},{C1/7.2*sy-.38:.2f}) {{$T_1$}}; \\node[vurgu] at ({6.6*sx:.2f},{C2/6.6*sy+.45:.2f}) {{$T_2$}};')
SK4=tk('\n'.join(g))
q('0004',[A('İzotermleri oku','Aynı hacimde (2 L) iki eğrinin basınçları grafikten okunur.','T₁: 6 atm · T₂: 8 atm'),
 A('Oranı yaz','Aynı n ve V için P ÷ T sabittir; T₁ mutlak sıcaklığa çevrilir.','T₁ = 27 + 273 = 300 K · 6 ÷ 300 = 8 ÷ T₂'),
 A('T₂’yi bul','Eşitliği çöz.','T₂ = 400 K'),
 A('Birimi dönüştür','İstenen sıcaklık °C cinsindendir.','t = 400 − 273 = 127 °C')],
 metin='Aynı miktardaki ideal bir gaz örneğinin iki farklı sıcaklıktaki basınç–hacim grafiği şekilde verilmiştir. Gazın T₁ sıcaklığı 27 °C’dir.\nBuna göre gazın T₂ sıcaklığı kaç °C’dir?',
 sekil=SK4,dogru=127,yan=[(-48,'P ile T’yi ters orantılı almış: T₂ = 300 × 6 ÷ 8 = 225 K = −48 °C.','bilgi'),(36,'Sıcaklıkları Kelvin’e çevirmeden °C ile oranlamış: 27 × 8 ÷ 6 = 36.','islem'),
  (100,'Sıcaklık farkını (400 − 300 = 100) T₂ olarak yazmış.','dikkat'),(400,'T₂’yi doğru bulmuş ancak Kelvin cinsinden bırakıp °C’ye çevirmemiş.','dikkat')],
 istenen='T₂ sıcaklığının °C cinsinden değeri.',ip=['Aynı hacimdeki iki noktayı karşılaştır ve hangi iki büyüklüğün oranının sabit kaldığını düşün.'],
 bilgi=[B('P–V grafiği','Sabit sıcaklıkta P·V sabittir ve grafik bir hiperbol (izoterm) olur. Aynı n için daha yukarıdaki eğri daha yüksek sıcaklığa aittir. Örnek: aynı hacimde basıncı 2 katı olan eğrinin mutlak sıcaklığı 2 katıdır')],
 puf='Grafikte aynı hacimde dikey çizgi çiz; basınçlar oranı mutlak sıcaklıklar oranını verir.',
 tipId='gz-yasa',tip=TIPLER['gz-yasa'],z='orta',alt='Gaz Yasaları',kaz='P–V grafiğindeki iki izotermden sıcaklık oranını bulur ve sıcaklık birimlerini dönüştürür.',kalip='grafik')

# ============ 0005 · bölmeli kap · orta ============
nL,TL,nR,TR=2,300,1,400; tot=15; wl=nL*TL; wr=nR*TR; VL=Fr(tot*wl,wl+wr); assert (wl,wr,VL)==(600,400,9)
e6=tot-VL; e75=Fr(tot,2); e10=Fr(tot*nL,nL+nR); e5=Fr(tot*nR,nL+nR); assert (e6,e75,e10,e5)==(6,F('7.5'),10,5)
g=[]
g.append('\\draw[thick] (0,0) rectangle (7,1.6);')
g.append('\\fill[gray!45] (3.42,0.03) rectangle (3.58,1.57); \\draw[thick] (3.42,0) rectangle (3.58,1.6);')
g.append(N(1.7,.8,'He\\\\$2$ mol\\\\$300$ K','align=center'))
g.append(N(5.3,.8,'Ne\\\\$1$ mol\\\\$400$ K','align=center'))
g.append(f'\\draw[{DARR}] (0,-.5) -- (7,-.5); '+N(3.5,-.95,'toplam hacim: $15$ L (şekil ölçekli değildir)','font=\\small'))
SK5=tk('\n'.join(g))
q('0005',[A('Denge koşulunu yaz','Sürtünmesiz piston dengede iken iki bölmedeki basınç eşittir; P·V = nRT’den V ∝ n·T.','V₁ ÷ V₂ = (n₁T₁) ÷ (n₂T₂)'),
 A('n·T değerlerini hesapla','He ve Ne için çarpımları bul.','He: 2 × 300 = 600 · Ne: 1 × 400 = 400'),
 A('Hacim oranını yaz','Oran toplam hacmi 600 : 400 = 3 : 2 oranında paylaştırır.','V(He) : V(Ne) = 3 : 2'),
 A('Sol bölmeyi bul','Toplam 15 L olduğundan He bölmesi 3/5’ini kaplar.','V(He) = 15 × 3 ÷ 5 = 9 L')],
 metin='Isı geçirmeyen, sürtünmesiz ve serbestçe hareket edebilen bir pistonla iki bölmeye ayrılmış kapta He ve Ne gazları şekildeki mol sayısı ve sıcaklıklarda bulunmaktadır. Piston dengede durmaktadır ve gazlar ideal davranmaktadır.\nBuna göre He gazının kapladığı hacim kaç litredir?',
 sekil=SK5,dogru=9,yan=[(6,'Hesabı doğru yapıp Ne’un hacmini (15 − 9) He’un hacmi olarak yazmış.','dikkat'),(F('7.5'),'Piston şekilde ortada çizildiği için hacimleri eşit (15 ÷ 2) sanmış.','dikkat'),
  (10,'Sıcaklıkları dikkate almamış; yalnız mol oranıyla (2 : 1) bölmüş: 15 × 2 ÷ 3 = 10 L.','bilgi'),(5,'Hacmi mol sayısıyla ters orantılı almış: 15 × 1 ÷ 3 = 5 L.','bilgi')],
 istenen='He bölmesinin hacmi (L).',ip=['Piston dengedeyken iki taraftaki basınçlar arasındaki ilişkiyi kur ve P·V = nRT bağıntısını her bölme için yaz.'],
 bilgi=[B('İdeal gaz denklemi','P·V = n·R·T. Basınç eşitse V ÷ (n·T) oranı her iki bölmede aynıdır. Örnek: aynı basınçta ve sıcaklıkta mol sayısı 3 kat olan gaz 3 kat hacim kaplar')],
 puf='Basınç eşitse hacimler n·T çarpımıyla orantılıdır; yalnız mol sayısına bakma.',
 tipId='gz-piston',tip=TIPLER['gz-piston'],z='orta',alt='Piston Düzenekleri',kaz='Bölmeli kapta piston dengesinden hacimleri mol sayısı ve sıcaklıkla ilişkilendirir.',kalip='şekilli')

# ============ manometre çizimi ============
def manometre(yL,yR,hl,gaz='Gaz'):
    g=[]
    g.append(f'\\fill[gray!40] (2.5,{yL:.3f}) -- (2.5,.5) arc[start angle=180,end angle=360,radius=.7] -- (3.9,{yR:.3f}) -- (3.5,{yR:.3f}) -- (3.5,.5) arc[start angle=360,end angle=180,radius=.3] -- (2.9,.5) -- (2.9,{yL:.3f}) -- cycle;')
    g.append('\\draw[thick] (2.5,3.4) -- (2.5,.5) arc[start angle=180,end angle=360,radius=.7] -- (3.9,3.1);')
    g.append('\\draw[thick] (2.9,3.4) -- (2.9,.5) arc[start angle=180,end angle=360,radius=.3] -- (3.5,3.1);')
    g.append('\\draw[thick] (1.4,3.4) -- (2.5,3.4); \\draw[thick] (2.9,3.4) -- (3.1,3.4) -- (3.1,4.6) -- (1.4,4.6) -- (1.4,3.4);')
    g.append(N(2.25,4.0,gaz,'align=center')); g.append(N(3.7,3.45,'açık uç','font=\\small'))
    g.append(f'\\draw[dashed] (2.9,{yL:.3f}) -- (4.75,{yL:.3f}); \\draw[dashed] (3.9,{yR:.3f}) -- (4.75,{yR:.3f});')
    g.append(f'\\draw[{DARR}] (4.5,{yL:.3f}) -- (4.5,{yR:.3f}); '+N(5.15,(yL+yR)/2,hl,'anchor=west'))
    g.append(N(3.2,-.4,'Hg'))
    return '\n'.join(g)

# ============ 0006 · açık uçlu manometre · orta ============
h6=19; Pa=76; Pg=Pa-h6; assert Fr(Pg,Pa)==F('0.75')
assert (Fr(Pa+h6,Pa),Fr(h6,Pa),Fr(Pa,h6))==(F('1.25'),F('0.25'),4)
SK6=tk(manometre(2.2,2.2-h6*.06,'$19$ cm'))
q('0006',[A('Seviye farkını yorumla','Gaz tarafındaki cıva açık koldakinden 19 cm yüksektedir; yani gaz basıncı açık hava basıncından küçüktür.','P(gaz) < P(açık hava)'),
 A('Gaz basıncını cmHg ile yaz','Açık hava basıncından seviye farkı çıkarılır.','P = 76 − 19 = 57 cmHg'),
 A('Atmosfere çevir','76 cmHg = 1 atm olduğundan oran alınır.','P = 57 ÷ 76 = 0,75 atm')],
 metin='Cıva (Hg) ile doldurulmuş açık uçlu bir manometre, içinde ideal gaz bulunan kaba şekildeki gibi bağlanmıştır. Açık hava basıncı 76 cmHg (1 atm) değerindedir.\nBuna göre kaptaki gazın basıncı kaç atm’dir?',
 sekil=SK6,dogru=F('0.75'),yan=[(F('0.25'),'Yalnız seviye farkını (19 cmHg) atm’ye çevirmiş: 19 ÷ 76 = 0,25 atm.','dikkat'),(1,'Seviye farkını hiç hesaba katmamış; gaz basıncını açık hava basıncına eşit almış.','dikkat'),
  (F('1.25'),'Gaz tarafındaki cıva yüksekte olmasına rağmen farkı eklemiş: (76 + 19) ÷ 76 = 1,25 atm.','bilgi'),(4,'cmHg ile atm’yi karıştırıp 76 ÷ 19 oranını almış.','islem')],
 istenen='Gazın basıncı (atm).',ip=['Cıvanın hangi kolda daha yüksekte olduğu, gazın basıncının açık hava basıncından büyük mü küçük mü olduğunu gösterir.'],
 bilgi=[B('Açık uçlu manometre','Gaz basıncı açık hava basıncına eşitlenir ve cıva seviye farkı kadar sapar: gaz tarafında cıva alçaksa P = Pₐ + h, yüksekse P = Pₐ − h. Örnek: Pₐ = 76 cmHg iken gaz tarafı 10 cm yüksekse P = 66 cmHg')],
 puf='Cıva hangi tarafta alçaksa basınç o tarafta büyüktür.',
 tipId='gz-manometre',tip=TIPLER['gz-manometre'],z='orta',alt='Manometre',kaz='Açık uçlu manometredeki seviye farkından gaz basıncını hesaplar.',kalip='şekilli')

# ============ 0007 · manometre + sıcaklık · zor ============
h7=4; P7=Pa+h7; T7a,T7b=240,300; P7b=Fr(P7*T7b,T7a); h7b=P7b-Pa
assert (P7,P7b,h7b)==(80,100,24)
assert Fr(h7*T7b,T7a)==5 and abs(Pa-Fr(P7*T7a,T7b))==12 and P7b-P7==20
SK7=tk(manometre(1.3,1.3+h7*.1,'$4$ cm','Gaz\\\\$240$ K'))
q('0007',[A('Başlangıç basıncını bul','Gaz tarafında cıva alçakta olduğundan gaz basıncı açık hava basıncından büyüktür.','P₁ = 76 + 4 = 80 cmHg'),
 A('Sabit hacimde yasayı kur','Hacim sabit olduğundan basınç mutlak sıcaklıkla doğru orantılıdır.','P₁ ÷ T₁ = P₂ ÷ T₂'),
 A('Yeni basıncı hesapla','Verileri yerine koy.','80 ÷ 240 = P₂ ÷ 300 → P₂ = 100 cmHg'),
 A('Yeni seviye farkını bul','Gaz basıncı açık hava basıncından büyük kalır; fark bu iki basıncın farkıdır.','h₂ = 100 − 76 = 24 cm')],
 metin='Sabit hacimli bir kaba bağlı, cıva (Hg) dolu açık uçlu manometrede 240 K sıcaklıkta cıva seviyeleri şekildeki gibidir. Açık hava basıncı 76 cmHg’dir. Kaptaki ideal gaz 300 K’e kadar ısıtılıyor; kabın hacmine göre manometredeki cıvanın yer değiştirmesi ihmal edilecektir.\nBuna göre ısıtma sonunda iki koldaki cıva seviyeleri arasındaki fark kaç cm olur?',
 sekil=SK7,dogru=24,yan=[(5,'Seviye farkını doğrudan sıcaklıkla orantılamış: 4 × 300 ÷ 240 = 5 cm.','bilgi'),(12,'Basıncı sıcaklıkla ters orantılı almış: P₂ = 80 × 240 ÷ 300 = 64 cmHg; 76 − 64 = 12 cm.','bilgi'),
  (20,'Basınçtaki artışı (100 − 80 = 20 cmHg) seviye farkı sanmış.','dikkat'),(100,'Yeni gaz basıncını (100 cmHg) bulup açık hava basıncını çıkarmayı unutmuş.','dikkat')],
 istenen='Isıtma sonunda cıva seviyeleri arasındaki fark (cm).',ip=['Önce gazın basıncını cmHg cinsinden bulmayı dene; sonra sıcaklığın basıncı nasıl değiştirdiğini düşün.'],
 bilgi=[B('Gay-Lussac yasası','Sabit hacimde ve sabit mol sayısında basınç mutlak sıcaklıkla doğru orantılıdır: P ÷ T = sabit. Örnek: mutlak sıcaklığı 1,5 katına çıkan sabit hacimli gazın basıncı da 1,5 katına çıkar')],
 puf='Seviye farkı basıncın kendisi değil, gaz basıncı ile açık hava basıncı arasındaki farktır.',
 tipId='gz-manometre',tip=TIPLER['gz-manometre'],z='zor',alt='Manometre',kaz='Manometredeki gaz basıncının sıcaklıkla değişimini Gay-Lussac yasasıyla yorumlayıp yeni seviye farkını bulur.',kalip='şekilli')

# ============ 0008 · su üzerinde gaz toplama · zor ============
R8=F('0.082'); T8=300; Pt=F('1.04'); Pw=F('0.04'); V8=F('7.38'); M8=F('122.5')
Po=Pt-Pw; nO=Po*V8/(R8*T8); nK=nO*2/3; mK=nK*M8
assert (Po,nO,nK,mK)==(1,F('0.3'),F('0.2'),F('24.5'))
e_tot=Pt*V8/(R8*T8)*Fr(2,3)*M8; e_ters=nO*Fr(3,2)*M8; e_bir=nO*M8; e_uc=nO/3*M8
assert (e_tot,e_ters,e_bir,e_uc)==(F('25.48'),F('55.125'),F('36.75'),F('12.25'))
g=[]
g.append('\\draw[thick,rounded corners=3pt] (0,.6) rectangle (2.2,1.5); \\draw[thick,fill=gray!50] (2.2,.85) rectangle (2.45,1.25);')
g.append('\\fill[gray!35] (.08,.68) rectangle (1.0,1.42); '+N(.55,1.05,'\\small\\ce{KClO3}','font=\\scriptsize'))
g.append('\\draw[thick] (.45,.1) -- (.65,.5) -- (.25,.5) -- cycle; '+N(.45,-.25,'ısıtıcı','font=\\small'))
g.append('\\fill[vurgu!18] (2.72,-2.28) rectangle (7.58,-1.45); \\draw[thick] (2.7,-1.1) -- (2.7,-2.3) -- (7.6,-2.3) -- (7.6,-1.1);')
g.append('\\fill[vurgu!8] (4.42,-1.45) rectangle (6.18,.88); \\draw[thick] (4.4,-1.9) -- (4.4,.9) -- (6.2,.9) -- (6.2,-1.9);')
g.append('\\draw[thick] (2.45,1.05) -- (3.5,1.05) -- (3.5,-2.1) -- (5.3,-2.1) -- (5.3,-.5);')
g.append(N(5.3,.3,'\\ce{O2}(g)\\\\$+$\\\\\\ce{H2O}(g)','align=center,font=\\small'))
g.append(N(6.4,-.55,'$V=7{,}38$ L\\\\$27\\,^\\circ$C','align=left,anchor=west,font=\\small'))
g.append(N(7.0,-1.95,'su','font=\\small'))
SK8=tk('\n'.join(g))
q('0008',[A('Gazın kısmi basıncını bul','Kapta O₂ ile birlikte su buharı vardır; toplam basınç kısmi basınçların toplamıdır.','P(O₂) = 1,04 − 0,04 = 1,00 atm'),
 A('O₂ mol sayısını hesapla','İdeal gaz denkleminde yalnız O₂’nin kısmi basıncı kullanılır; T = 27 + 273 = 300 K.','n = P·V ÷ (R·T) = 1 × 7,38 ÷ (0,082 × 300) = 0,3 mol'),
 A('Denklemden oran kur','2 mol KClO₃ bozunduğunda 3 mol O₂ oluşur.','n(KClO₃) = 0,3 × 2 ÷ 3 = 0,2 mol'),
 A('Kütleye çevir','Mol sayısı mol kütlesiyle çarpılır.','m = 0,2 × 122,5 = 24,5 g')],
 metin='Potasyum klorat (KClO₃) katısı ısıtıldığında potasyum klorür (KCl) katısı ve oksijen gazı oluşur.\n2KClO₃(k) → 2KCl(k) + 3O₂(g)\nTepkimede açığa çıkan gaz, şekildeki düzenekte 27 °C’de su üzerinde toplanmıştır. Kabın toplam basıncı 1,04 atm’dir ve 27 °C’de suyun buhar basıncı 0,04 atm alınacaktır. O₂ gazı suda çözünmemektedir. (KClO₃ = 122,5 g/mol, R = 0,082 L·atm/mol·K; gazlar ideal davranmaktadır.)\nBuna göre bozunan KClO₃ kaç gramdır?',
 sekil=SK8,dogru=F('24.5'),yan=[(F('12.25'),'Denklemde O₂ katsayısını (3) KClO₃’ın mol sayısına bölmüş: 0,3 ÷ 3 = 0,1 mol → 12,25 g.','islem'),(F('25.48'),'Toplam basıncı (1,04 atm) O₂ basıncı sanmış: n = 1,04 × 7,38 ÷ 24,6 = 0,312 mol → 0,208 mol KClO₃ → 25,48 g.','bilgi'),
  (F('36.75'),'Mol oranını 1 : 1 almış: n(KClO₃) = n(O₂) = 0,3 mol → 36,75 g.','bilgi'),(F('55.125'),'Katsayı oranını ters kullanmış: 0,3 × 3 ÷ 2 = 0,45 mol → 55,125 g.','islem')],
 istenen='Bozunan KClO₃ kütlesi (g).',ip=['Su üzerinde toplanan gazın tamamının O₂ olmadığını göz önüne alarak ideal gaz denklemine hangi basınç değerini yazman gerektiğini düşün.'],
 bilgi=[B('Su üzerinde gaz toplama','Toplanan karışımın toplam basıncı, gazın kısmi basıncı ile suyun buhar basıncının toplamıdır: P_toplam = P_gaz + P_buhar. Örnek: toplam 0,95 atm ve buhar basıncı 0,05 atm ise gazın kısmi basıncı 0,90 atm’dir'),
        B('Denklem katsayıları','Katsayılar mol oranını verir. Örnek: 2A → 3B tepkimesinde 4 mol A’dan 6 mol B oluşur')],
 puf='Su üzerinde toplanan gazın mol sayısını bulurken toplam basıncı değil, buhar basıncı çıkarılmış kısmi basıncı kullan.',
 tipId='gz-sutop',tip=TIPLER['gz-sutop'],z='zor',alt='Gaz Karışımları',kaz='Su üzerinde toplanan gazın kısmi basıncından mol sayısını, tepkime denkleminden de tepkimeye giren madde miktarını hesaplar.',kalip='şekilli')

# ============ 0009 · farklı sıcaklıkta bağlı kaplar · zor ============
VA,PA,TA=2,6,300; VB,PB,TB=6,1,600; Tf=400
nRA=Fr(PA*VA,TA); nRB=Fr(PB*VB,TB); Pf=(nRA+nRB)*Tf/(VA+VB); assert (nRA,nRB,Pf)==(F('0.04'),F('0.01'),F('2.5'))
e_ts=Fr(PA*VA+PB*VB,VA+VB); e_t300=(nRA+nRB)*300/(VA+VB); e_or=Fr(PA+PB,2); e_top=PA+PB
assert (e_ts,e_t300,e_or,e_top)==(F('2.25'),F('1.875'),F('3.5'),7)
g=[]
g.append('\\draw[thick] (0,0) rectangle (1.6,1.7); \\draw[thick] (2.8,0) rectangle (6.4,1.7);')
g.append('\\draw[thick] (1.6,.85) -- (2.8,.85); \\draw[thick] (2.0,.6) -- (2.4,1.1) -- (2.4,.6) -- (2.0,1.1) -- cycle; \\draw[thick] (2.2,.85) -- (2.2,1.45); \\draw[thick] (2.0,1.45) -- (2.4,1.45);')
g.append(N(2.2,1.8,'musluk','anchor=south,font=\\small'))
g.append(N(.8,.85,'He\\\\$2$ L\\\\$6$ atm\\\\$300$ K','align=center'))
g.append(N(4.6,.85,'Ne\\\\$6$ L\\\\$1$ atm\\\\$600$ K','align=center'))
SK9=tk('\n'.join(g))
q('0009',[A('Her kapta P·V ÷ T hesapla','P·V ÷ T = n·R olduğundan farklı sıcaklıktaki kapların mol miktarları buradan karşılaştırılır.','He: 6 × 2 ÷ 300 = 0,04 · Ne: 1 × 6 ÷ 600 = 0,01'),
 A('Toplam n·R değerini bul','Musluk açılınca mol sayıları toplanır.','n·R = 0,04 + 0,01 = 0,05'),
 A('Toplam hacmi yaz','İki kabın hacmi birleşir.','V = 2 + 6 = 8 L'),
 A('Son basıncı hesapla','Sistem 400 K’e getirildiğinde P = (n·R)·T ÷ V.','P = 0,05 × 400 ÷ 8 = 2,5 atm')],
 metin='Şekildeki kaplarda ideal davranan He ve Ne gazları farklı sıcaklıklardadır. Musluk açıldığında gazlar karışıyor ve sistem 400 K sıcaklığa getirilerek dengeye ulaşıyor. Musluk ve bağlantı borusunun hacmi ihmal edilecektir.\nBuna göre son durumda gaz karışımının toplam basıncı kaç atm olur?',
 sekil=SK9,dogru=F('2.5'),yan=[(F('1.875'),'Son sıcaklık olarak 400 K yerine 300 K almış: P = 0,05 × 300 ÷ 8 = 1,875 atm.','dikkat'),(F('2.25'),'Sıcaklıkları dikkate almamış: (6 × 2 + 1 × 6) ÷ 8 = 2,25 atm.','bilgi'),
  (F('3.5'),'Basınçların aritmetik ortalamasını almış: (6 + 1) ÷ 2 = 3,5 atm.','bilgi'),(7,'Başlangıç basınçlarını toplamış: 6 + 1 = 7 atm.','bilgi')],
 istenen='Son durumdaki toplam basınç (atm).',ip=['Her kaptaki gazın P·V ÷ T değerinin neyi gösterdiğini düşün.'],
 bilgi=[B('İdeal gaz denklemi','P·V = n·R·T olduğundan P·V ÷ T = n·R’dir ve mol sayısıyla doğru orantılıdır. Örnek: 2 atm × 3 L ÷ 300 K değeri, 1 atm × 6 L ÷ 300 K değerine eşit olduğundan iki örnekteki mol sayıları eşittir')],
 puf='Gazlar karışırken P ya da V’yi değil, mol sayısını (P·V ÷ T) topla.',
 tipId='gz-kismi',tip=TIPLER['gz-kismi'],z='zor',alt='Gaz Karışımları',kaz='Farklı sıcaklıklardaki gazların karışımının son basıncını mol sayılarını toplayarak hesaplar.',kalip='şekilli')

# ============ 0010 · kısmi basınç · öncüllü tablo · orta ============
mHe,MHe,mCH,MCH=8,4,16,16; nHe=Fr(mHe,MHe); nCH=Fr(mCH,MCH); nT=nHe+nCH; Pt10=3
PHe=Pt10*nHe/nT; xCH=nCH/nT; assert (nHe,nCH,PHe,xCH)==(2,1,2,Fr(1,3))
d={'I':(True,'He’un mol kesri 2/3 olduğundan kısmi basıncı 3 × 2/3 = 2 atm’dir'),
   'II':(False,'aynı sıcaklıkta bütün gazların ortalama kinetik enerjisi eşittir; He’un enerjisi CH₄’ünkinden büyük değildir'),
   'III':(True,'CH₄’ün mol kesri 1 ÷ (2 + 1) = 1/3’tür')}
r=_onc(d,[('I',),('II',),('I','II'),('I','III'),('II','III')])
sk=tablo_svg(['Gaz','Kütle (g)','Mol kütlesi (g/mol)'],[['He','8','4'],['CH₄','16','16']])
q('0010',[A('Mol sayılarını bul','n = kütle ÷ mol kütlesi.','n(He) = 8 ÷ 4 = 2 · n(CH₄) = 16 ÷ 16 = 1'),
 A('Mol kesirlerini yaz','Toplam mol sayısı 3’tür.','X(He) = 2/3 · X(CH₄) = 1/3'),
 A('Kısmi basınçları hesapla','Kısmi basınç = mol kesri × toplam basınç.','P(He) = 2 atm · P(CH₄) = 1 atm'),
 A('Öncülleri yorumla','Enerji karşılaştırması mol kütlesine değil sıcaklığa bağlıdır.',oy(d)+' · Sonuç: '+r['dogru'])],
 metin='Sabit sıcaklıktaki rijit bir kapta, kütleleri ve mol kütleleri aşağıdaki tabloda verilen He ve CH₄ gazları karıştırılmıştır. Gazlar ideal davranmakta ve karışımın toplam basıncı 3 atm olmaktadır.\nI. He gazının kısmi basıncı 2 atm’dir.\nII. He atomlarının ortalama kinetik enerjisi CH₄ moleküllerininkinden büyüktür.\nIII. CH₄ gazının mol kesri 1/3’tür.\nBuna göre hangileri doğrudur?',
 sekil=sk,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan öncüller.',
 ip=['Kütleden mol sayısına geçmeden kısmi basınç ya da mol kesri hakkında yorum yapma.'],
 bilgi=[B('Dalton yasası','Kısmi basınç = mol kesri × toplam basınç; mol kesri = bileşenin mol sayısı ÷ toplam mol sayısı. Örnek: 1 mol X ile 3 mol Y karışımında Y’nin mol kesri 3/4’tür')],
 puf='Kısmi basınç kütleyle değil mol sayısıyla belirlenir.',
 tipId='gz-kismi',tip=TIPLER['gz-kismi'],z='orta',alt='Gaz Karışımları',kaz='Kütle ve mol kütlesi verilen gaz karışımında mol kesri ve kısmi basıncı yorumlar.',kalip='öncüllü')

# ============ 0011 · difüzyon tüpü · öncüllü · orta ============
Lt=60; dCH=40; dSO=Lt-dCH; assert Fr(dCH,dSO)==2==math.isqrt(64//16)
d={'I':(True,'karşılaşma noktasına kadar alınan yol hızla orantılıdır; 40 ÷ 20 = 2 ve Graham yasasına göre √(64 ÷ 16) = 2 olduğundan CH₄ iki kat hızlıdır'),
   'II':(True,'√(32 ÷ 16) ≈ 1,41 < 2 olduğundan hız oranı 2’den küçük olur ve karşılaşma noktası 40 cm’den CH₄ ucuna daha yakın olur'),
   'III':(False,'aynı sıcaklıkta bütün gazların ortalama kinetik enerjisi eşittir')}
assert math.sqrt(2)<2
r=_onc(d,[('III',),('I','II'),('I','III'),('II','III'),('I','II','III')])
g=[]
g.append('\\draw[thick] (.2,0) circle (.6); \\draw[thick] (7.4,0) circle (.6);')
g.append(N(.2,0,'\\ce{CH4}')); g.append(N(7.4,0,'\\ce{SO2}'))
g.append('\\draw[thick] (.8,.2) -- (6.8,.2); \\draw[thick] (.8,-.2) -- (6.8,-.2);')
g.append('\\draw[dashed,vurgu,thick] (4.8,-.55) -- (4.8,.55); \\draw['+ARR+'] (4.8,1.25) -- (4.8,.6); '+N(4.8,1.5,'karşılaşma noktası','font=\\small'))
g.append(f'\\draw[{DARR}] (.8,-1.0) -- (4.8,-1.0); '+N(2.8,-1.35,'$40$ cm','font=\\small'))
g.append(f'\\draw[{DARR}] (.8,-1.9) -- (6.8,-1.9); '+N(3.8,-2.25,'$60$ cm','font=\\small'))
SK11=tk('\n'.join(g))
q('0011',[A('Şekilden yolları oku','Toplam uzunluk 60 cm ve karşılaşma noktası CH₄ ucundan 40 cm uzaktadır.','CH₄: 40 cm · SO₂: 60 − 40 = 20 cm'),
 A('I. öncülü incele','Aynı sürede alınan yollar hızlarla orantılıdır; Graham yasasıyla karşılaştır.','40 ÷ 20 = 2 = √(64 ÷ 16)'),
 A('II. öncülü incele','Mol kütlesi daha küçük bir gazla hız oranı küçülür.','√(32 ÷ 16) ≈ 1,41'),
 A('III. öncülü incele','Sıcaklık aynıysa ortalama kinetik enerji gazdan bağımsızdır.','III: yanlış'),
 A('Sonucu yaz','Doğru öncüller bir arada yazılır.',oy(d)+' · Sonuç: '+r['dogru'])],
 metin='Aynı sıcaklık ve basınçtaki CH₄ ve SO₂ gazları, ayrı balonlardan aynı anda, 60 cm uzunluğundaki bir cam borunun iki ucundan boruya salınıyor. Gazlar şekilde gösterilen noktada karşılaşıyor. (H = 1, C = 12, O = 16, S = 32 g/mol; gazlar ideal davranmaktadır.)\nI. Karşılaşma noktası, CH₄’ün difüzyon hızının SO₂’ninkinin 2 katı olduğunu gösterir.\nII. SO₂ yerine O₂ kullanılsaydı karşılaşma noktası CH₄ balonuna daha yakın olurdu.\nIII. CH₄ moleküllerinin ortalama kinetik enerjisi SO₂ moleküllerinkinden büyüktür.\nBuna göre hangileri doğrudur?',
 sekil=SK11,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan öncüller.',
 ip=['Aynı sürede alınan yollar ile hızlar arasındaki ilişkiyi mol kütleleriyle bağdaştır.'],
 bilgi=[B('Graham yasası','Aynı sıcaklık ve basınçta difüzyon hızı mol kütlesinin kareköküyle ters orantılıdır: v₁ ÷ v₂ = √(M₂ ÷ M₁). Örnek: mol kütlesi 4 kat büyük olan gaz 2 kat yavaştır')],
 puf='Hız oranı mol kütle oranının karekökü kadardır; yol oranı da hız oranına eşittir.',
 tipId='gz-difuz',tip=TIPLER['gz-difuz'],z='orta',alt='Difüzyon ve Efüzyon',kaz='Difüzyon tüpündeki karşılaşma noktasından Graham yasasını yorumlar.',kalip='şekilli')

# ============ 0012 · olumsuz kök · eşit kütle H2/CH4 · orta ============
d={'I':(False,'eşit kütlede mol sayısı mol kütlesiyle ters orantılıdır: n(H₂) ÷ n(CH₄) = 16 ÷ 2 = 8 olduğundan molekül sayısı 8 katıdır'),
   'II':(False,'aynı sıcaklıkta bütün gazların ortalama kinetik enerjisi eşittir'),
   'III':(True,'efüzyon hızı oranı √(16 ÷ 2) = √8 ≈ 2,8’dir; 8 kat değildir')}
assert Fr(16,2)==8 and math.sqrt(8)!=8
r=onc_neg(d,[('III',),('I','II'),('I','III'),('II','III'),('I','II','III')])
q('0012',[A('Mol sayılarını karşılaştır','Eşit kütlede mol sayısı = kütle ÷ mol kütlesi.','n(H₂) ÷ n(CH₄) = 16 ÷ 2 = 8 → I doğru'),
 A('Kinetik enerjiyi karşılaştır','Sıcaklık aynıysa ortalama kinetik enerji de aynıdır.','II doğru'),
 A('Efüzyon hızını karşılaştır','Hızlar oranı mol kütlelerinin oranının kareköküdür.','v(H₂) ÷ v(CH₄) = √(16 ÷ 2) = √8 ≈ 2,8 → III yanlış'),
 A('Sonucu yaz','Soru yanlış olan yargıları sorar.',oyn(d)+' · Sonuç: '+r['dogru'])],
 metin='Aynı sıcaklıkta, eşit kütlelerde alınan H₂ ve CH₄ gazlarıyla ilgili bir öğrencinin yazdığı yargılar aşağıda verilmiştir. (H = 1, C = 12 g/mol; gazlar ideal davranmaktadır.)\nI. H₂ gazının molekül sayısı CH₄ gazınınkinin 8 katıdır.\nII. İki gazın moleküllerinin ortalama kinetik enerjileri eşittir.\nIII. Aynı koşullarda küçük bir delikten efüzyon hızı H₂ gazının CH₄ gazınınkinin 8 katıdır.\nBuna göre bu yargılardan hangileri yanlıştır?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Yanlış olan yargılar.',
 ip=['Her yargıda kütle, mol sayısı, enerji ve hız kavramlarından hangisinin sorulduğunu ayırarak incele.'],
 bilgi=[B('Mol sayısı ve efüzyon','Eşit kütlede mol sayısı mol kütlesiyle ters orantılıdır. Efüzyon hızı mol kütlesinin kareköküyle ters orantılıdır. Örnek: mol kütlesi 9 kat büyük gaz 3 kat yavaş efüze olur')],
 puf='Mol sayısı oranı mol kütlesiyle ters, hız oranı ise onun karekökü kadardır.',
 tipId='gz-difuz',tip=TIPLER['gz-difuz'],z='orta',alt='Difüzyon ve Efüzyon',kaz='Eşit kütleli gazlarda mol sayısı, kinetik enerji ve efüzyon hızı arasındaki ilişkileri yorumlar.',kalip='öncüllü')

# ============ 0013 · yoğunluktan mol kütlesi · orta ============
R13=Fr(224,10)/273; T13=819; P13=2; d13=F('1.25'); M13=d13*R13*T13/P13
assert M13==42 and d13*R13*273/P13==14 and d13*R13*T13==84 and d13*R13*T13*P13==168 and d13*22.4==28
q('0013',[A('Bağıntıyı yaz','Yoğunluk d = m ÷ V ve P·V = (m ÷ M)·R·T olduğundan P·M = d·R·T.','M = d·R·T ÷ P'),
 A('R·T değerini hesapla','R = 22,4 ÷ 273 olduğundan T = 819 K = 3 × 273 için R·T = 22,4 × 3.','R·T = 67,2 L·atm/mol'),
 A('Mol kütlesini bul','Değerleri yerine koy.','M = 1,25 × 67,2 ÷ 2 = 42 g/mol')],
 metin='Sıcaklığı 819 K ve basıncı 2 atm olan ideal bir gaz örneğinin yoğunluğu 1,25 g/L olarak ölçülmüştür. İdeal gaz sabiti R = 22,4/273 L·atm/mol·K’dir.\nBuna göre gazın mol kütlesi kaç g/mol’dür?',
 dogru=42,yan=[(14,'Sıcaklık olarak 273 K kullanmış: M = 1,25 × 22,4 ÷ 2 = 14 g/mol.','dikkat'),(28,'Koşulları NŞA sanıp 1 mol gazın 22,4 L hacim kapladığını varsaymış: M = 1,25 × 22,4 = 28 g/mol.','bilgi'),
  (84,'Basınca bölmeyi unutmuş: M = 1,25 × 67,2 = 84 g/mol.','islem'),(168,'Basınçla bölmek yerine çarpmış: M = 1,25 × 67,2 × 2 = 168 g/mol.','islem')],
 istenen='Gazın mol kütlesi (g/mol).',ip=['Yoğunluğu ideal gaz denkleminde kütle ve hacim yerine yazarak mol kütlesini yoğunlukla ilişkilendir.'],
 bilgi=[B('Yoğunluk ve mol kütlesi','İdeal gazlarda P·M = d·R·T bağıntısı geçerlidir. Örnek: aynı P ve T’de mol kütlesi 2 kat büyük olan gazın yoğunluğu 2 kat büyüktür')],
 puf='22,4 L/mol değeri yalnız normal şartlarda (0 °C, 1 atm) geçerlidir.',
 tipId='gz-ideal',tip=TIPLER['gz-ideal'],z='orta',alt='İdeal Gaz Denklemi',kaz='Verilen koşuldaki yoğunluktan gazın mol kütlesini ideal gaz denklemiyle hesaplar.',kalip='düz')

# ============ 0014 · piston + yük + ısıtma · zor ============
V14,P14,T14=6,1,300; P14b=F('1.5'); T14b=600; V14b=Fr(V14*P14*T14b,1)/(T14*P14b); assert V14b==8
assert (V14*T14b/T14/1,V14*P14/P14b,V14*P14b*T14b/T14,V14*P14/P14b*T14/T14b)==(12,4,18,Fr(3,2)*Fr(4,3)*0+2) or True
e12=Fr(V14*T14b,T14); e4=Fr(V14*P14,1)/P14b; e18=V14*P14b*Fr(T14b,T14); e2=Fr(V14*P14,1)/P14b*Fr(T14,T14b)
assert (e12,e4,e18,e2)==(12,4,18,2)
cy=lambda x0,hh,yazi,ek=None:(f'\\draw[thick] ({x0},3.4) -- ({x0},0) -- ({x0+1.6},0) -- ({x0+1.6},3.4); \\fill[vurgu!12] ({x0+.02},.02) rectangle ({x0+1.58},{hh}); \\fill[gray!45] ({x0+.02},{hh}) rectangle ({x0+1.58},{hh+.18}); \\draw[thick] ({x0},{hh}) rectangle ({x0+1.6},{hh+.18});'
 +(f'\\draw[thick,fill=gray!20] ({x0+.3},{hh+.18}) rectangle ({x0+1.3},{hh+.78}); '+N(x0+.8,hh+.48,'yük','font=\\small') if ek else '')+N(x0+.8,hh/2,yazi,'align=center'))
g=[cy(0,2.1,'$6$ L\\\\$300$ K'),cy(4.6,2.1,'$V$ = ?\\\\$600$ K',True)]
g.append(f'\\draw[{ARR}] (2.0,1.3) -- (4.3,1.3); '+N(3.15,1.65,'ısıtma ve yük','font=\\small'))
g.append(N(.8,3.75,'dış basınç: $1$ atm','font=\\small')); g.append(N(5.4,3.75,'dış basınç: $1$ atm','font=\\small'))
g.append(N(3.2,-.6,'(piston konumu şematiktir)','font=\\small'))
SK14=tk('\n'.join(g))
q('0014',[A('Son gaz basıncını bul','Piston dengede iken gaz basıncı dış basınç ile yükün oluşturduğu basıncın toplamıdır.','P₂ = 1 + 0,5 = 1,5 atm'),
 A('Birleşik gaz yasasını yaz','Mol sayısı sabit olduğundan P·V ÷ T değişmez.','P₁V₁ ÷ T₁ = P₂V₂ ÷ T₂'),
 A('Değerleri yerine koy','İlk ve son durumun verileri yazılır.','1 × 6 ÷ 300 = 1,5 × V₂ ÷ 600'),
 A('Son hacmi bul','Eşitliği V₂ için çöz.','V₂ = 6 × 600 ÷ (300 × 1,5) = 8 L')],
 metin='Ağırlığı ve sürtünmesi ihmal edilen bir pistonla kapatılmış kapta bulunan ideal gaz, şekildeki başlangıç durumundadır. Pistonun üzerine, gaz üzerinde 0,5 atm ek basınç oluşturan bir yük konuluyor ve gaz şekildeki son sıcaklığa kadar ısıtılarak yeniden dengeye ulaşması sağlanıyor. Dış basınç değişmemektedir.\nBuna göre gazın son hacmi kaç litredir?',
 sekil=SK14,dogru=8,yan=[(2,'Hem basıncı hem sıcaklığı ters orantılı almış: V₂ = 6 × 1 ÷ 1,5 × 300 ÷ 600 = 2 L.','bilgi'),(4,'Sıcaklık değişimini hesaba katmamış: V₂ = 6 × 1 ÷ 1,5 = 4 L.','dikkat'),
  (12,'Yükün oluşturduğu basıncı hesaba katmamış: V₂ = 6 × 600 ÷ 300 = 12 L.','dikkat'),(18,'Hacmi basınçla doğru orantılı almış: V₂ = 6 × 1,5 × 600 ÷ 300 = 18 L.','bilgi')],
 istenen='Gazın son hacmi (L).',ip=['Yük konulduktan sonra gaza uygulanan toplam dış basıncın ne olduğunu belirle.'],
 bilgi=[B('Birleşik gaz yasası','Mol sayısı sabitken P·V ÷ T sabittir. Örnek: basıncı 2 katına çıkıp mutlak sıcaklığı 2 katına çıkan gazın hacmi değişmez')],
 puf='Pistonlu kapta denge: gaz basıncı = dış basınç + yükün basıncı.',
 tipId='gz-piston',tip=TIPLER['gz-piston'],z='zor',alt='Piston Düzenekleri',kaz='Piston üzerine yük konulup sıcaklık değiştirildiğinde birleşik gaz yasasıyla son hacmi bulur.',kalip='şekilli')

# ============ 0015 · gerçek gazlar Z–P · orta ============
zHe=lambda p:1+0.0005*p; zCH=lambda p:1-0.0024*p+0.000006*p*p
assert zHe(300)>1 and zCH(200)<1 and zCH(100)<1 and zHe(450)>zCH(450)>1 and all(zHe(p)>1 for p in range(10,451,10))
sxz,syz=.011,5.5; Zy=lambda z:(z-.6)*syz
g=[]
g.append(f'\\draw[->,thick] (0,0) -- ({470*sxz:.2f},0) node[below right] {{$P$ (atm)}};')
g.append(f'\\draw[->,thick] (0,0) -- (0,{Zy(1.45):.2f}) node[above] {{$Z=\\dfrac{{PV}}{{nRT}}$}};')
for p in (100,200,300,400): g.append(f'\\draw ({p*sxz:.2f},.07) -- ({p*sxz:.2f},-.07) node[below] {{{p}}};')
for z,t in ((.8,'0{,}8'),(1.0,'1{,}0'),(1.2,'1{,}2'),(1.4,'1{,}4')): g.append(f'\\draw (.07,{Zy(z):.2f}) -- (-.07,{Zy(z):.2f}) node[left] {{${t}$}};')
g.append(f'\\draw[dashed] (0,{Zy(1):.2f}) -- ({450*sxz:.2f},{Zy(1):.2f}); '+N(450*sxz+.1,Zy(1)-.28,'ideal gaz','anchor=west,font=\\small'))
ptsHe=' '.join(f'({p*sxz:.3f},{Zy(zHe(p)):.3f})' for p in range(0,451,15)); ptsCH=' '.join(f'({p*sxz:.3f},{Zy(zCH(p)):.3f})' for p in range(0,451,15))
g.append(f'\\draw[thick] plot[smooth] coordinates {{{ptsHe}}}; \\draw[thick,vurgu,densely dashed] plot[smooth] coordinates {{{ptsCH}}};')
g.append(N(450*sxz+.2,Zy(zHe(450)),'$1$','anchor=west')); g.append(N(450*sxz+.2,Zy(zCH(450))+.05,'$2$','anchor=west,text=vurgu'))
SK15=tk('\n'.join(g))
d={'I':(False,'Z değeri 1’in üstünde kalan 1 numaralı eğri, çekim kuvvetleri çok zayıf olan He gazına aittir; CH₄ gazının eğrisi Z = 1’in altına iner'),
   'II':(True,'düşük basınçta moleküller birbirinden uzaktır; molekül hacmi ve çekim kuvvetleri ihmal edilir, Z ≈ 1 olur'),
   'III':(True,'orta basınçlarda moleküller arası çekim kuvvetleri gaz hacmini küçülterek Z’yi 1’in altına indirir')}
r=_onc(d,[('I',),('II',),('I','II'),('I','III'),('II','III')])
q('0015',[A('Eğrileri gazlara eşle','Çekim kuvvetleri zayıf olan He’un Z değeri her basınçta 1’in üstündedir; CH₄’ün eğrisi ise Z = 1’in altına iner.','1: He · 2: CH₄ → I yanlış'),
 A('Düşük basınçta davranış','Basınç sıfıra giderken iki eğri de Z = 1’e yaklaşır.','II doğru'),
 A('2 numaralı eğriyi yorumla','Z < 1 olması, gazın ideale göre daha çok sıkışabildiğini yani çekim kuvvetlerinin etkin olduğunu gösterir.','III doğru'),
 A('Sonucu yaz','Doğru öncüller bir arada yazılır.',oy(d)+' · Sonuç: '+r['dogru'])],
 metin='273 K sıcaklıkta He ve CH₄ gazlarının farklı basınçlardaki Z = PV/nRT değerleri şekildeki 1 ve 2 numaralı eğrilerle gösterilmiştir. Eğrilerden biri He’a, diğeri CH₄’a aittir.\nI. 1 numaralı eğri CH₄ gazına aittir.\nII. Düşük basınçlarda her iki gaz da ideal gaza yakın davranır.\nIII. 2 numaralı gazın Z değerinin 1’in altına inmesi, moleküller arası çekim kuvvetlerinin etkisiyle açıklanır.\nBuna göre hangileri doğrudur?',
 sekil=SK15,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan öncüller.',
 ip=['Z değerinin 1’in altında ya da üstünde olmasının moleküller arası etkileşimlerle nasıl ilişkili olduğunu düşün.'],
 bilgi=[B('Gerçek gazlar','Z = PV ÷ nRT; ideal gazda Z = 1’dir. Çekim kuvvetleri etkinse Z < 1, molekül hacmi etkinse Z > 1 olur. Örnek: çok yüksek basınçta molekül hacmi hacim ayrılmasına yol açtığından Z 1’in üstüne çıkar')],
 puf='Z < 1 çekim kuvvetinin, Z > 1 molekül hacminin baskın olduğunu gösterir.',
 tipId='gz-gercek',tip=TIPLER['gz-gercek'],z='orta',alt='Gerçek Gazlar',kaz='Z–P grafiğinden gerçek gazların ideal davranıştan sapmasını yorumlar.',kalip='grafik')

# ============ 0016 · d–P grafiği · orta ============
sA,sB=F('0.8'),F('1.6'); assert sB/sA==2 and sB*4==F('6.4') and sA*1==F('0.8') and sB*2==F('3.2')
sxd,syd=1.5,.75
g=[]
g.append(f'\\draw[->,thick] (0,0) -- ({4.5*sxd:.2f},0) node[below right] {{$P$ (atm)}};')
g.append(f'\\draw[->,thick] (0,0) -- (0,{7*syd:.2f}) node[above] {{$d$ (g/L)}};')
for p in (1,2,3,4): g.append(f'\\draw ({p*sxd:.2f},.07) -- ({p*sxd:.2f},-.07) node[below] {{{p}}};')
for dv,t in ((0.8,'0{,}8'),(3.2,'3{,}2'),(6.4,'6{,}4')): g.append(f'\\draw (.07,{dv*syd:.2f}) -- (-.07,{dv*syd:.2f}) node[left] {{${t}$}};')
g.append(f'\\draw[thick] (0,0) -- ({4*sxd:.2f},{3.2*syd:.2f}); \\draw[thick,vurgu,densely dashed] (0,0) -- ({4*sxd:.2f},{6.4*syd:.2f});')
g.append(f'\\draw[dotted] (0,{.8*syd:.2f}) -- ({1*sxd:.2f},{.8*syd:.2f}) -- ({1*sxd:.2f},0); \\draw[dotted] (0,{3.2*syd:.2f}) -- ({2*sxd:.2f},{3.2*syd:.2f}) -- ({2*sxd:.2f},0);')
g.append(f'\\fill ({1*sxd:.2f},{.8*syd:.2f}) circle (1.6pt); \\fill[vurgu] ({2*sxd:.2f},{3.2*syd:.2f}) circle (1.6pt);')
g.append(N(4*sxd+.2,3.2*syd,'A','anchor=west')); g.append(N(4*sxd+.2,6.4*syd,'B','anchor=west,text=vurgu'))
SK16=tk('\n'.join(g))
d={'I':(True,'aynı sıcaklıkta d ÷ P = M ÷ (R·T) olduğundan eğim mol kütlesiyle orantılıdır; B’nin eğimi (1,6) A’nın eğiminin (0,8) 2 katıdır'),
   'II':(False,'B doğrusu orijinden geçtiğinden P = 4 atm’de yoğunluğu 1,6 × 4 = 6,4 g/L’dir'),
   'III':(False,'d = P·M ÷ (R·T) olduğundan sıcaklık artınca eğim (M ÷ RT) azalır')}
r=_onc(d,[('I',),('II',),('III',),('I','II'),('II','III')])
q('0016',[A('Eğimleri oku','Doğruların eğimi d ÷ P oranıdır; işaretli noktalardan hesaplanır.','A: 0,8 ÷ 1 = 0,8 · B: 3,2 ÷ 2 = 1,6'),
 A('I. öncülü incele','Aynı T’de eğim M ile orantılıdır.','1,6 ÷ 0,8 = 2 → I doğru'),
 A('II. öncülü incele','B doğrusu orijinden geçer; 4 atm’de yoğunluk eğimle çarpılarak bulunur.','1,6 × 4 = 6,4 g/L → II yanlış'),
 A('III. öncülü incele','Eğim M ÷ (R·T) olduğundan sıcaklık artınca küçülür.','III yanlış'),
 A('Sonucu yaz','Doğru öncüller bir arada yazılır.',oy(d)+' · Sonuç: '+r['dogru'])],
 metin='Aynı sıcaklıkta bulunan, ideal davranan A ve B gazlarının yoğunluklarının basınçla değişimi şekilde verilmiştir.\nI. B gazının mol kütlesi A gazınınkinin 2 katıdır.\nII. B gazının 4 atm basınçtaki yoğunluğu 3,2 g/L’dir.\nIII. Sıcaklık artırılırsa A gazının doğrusunun eğimi artar.\nBuna göre hangileri doğrudur?',
 sekil=SK16,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan öncüller.',
 ip=['Yoğunluk bağıntısında basınçla orantılı olan terimlerin dışındaki büyüklükleri doğrunun eğimi olarak düşün.'],
 bilgi=[B('Yoğunluk–basınç ilişkisi','İdeal gazda d = P·M ÷ (R·T) olduğundan sabit sıcaklıkta d ile P doğru orantılıdır ve eğim M ÷ (R·T) değerine eşittir. Örnek: aynı T’de mol kütlesi 3 kat büyük gazın doğrusunun eğimi 3 kat büyüktür')],
 puf='Sabit T’de d–P doğrusunun eğimi mol kütlesiyle doğru, sıcaklıkla ters orantılıdır.',
 tipId='gz-ideal',tip=TIPLER['gz-ideal'],z='orta',alt='İdeal Gaz Denklemi',kaz='d–P grafiğindeki doğruların eğimini mol kütlesi ve sıcaklıkla ilişkilendirir.',kalip='grafik')

# ============ 0017 · Maxwell dağılımı · olumsuz kök · orta ============
def fmx(v,s): return math.sqrt(2/math.pi)*v*v/s**3*math.exp(-v*v/(2*s*s))
s1,s2=1.0,1.7
# alanlar eşit (sayısal integral)
a1=sum(fmx(i*.01,s1)*.01 for i in range(1,1500)); a2=sum(fmx(i*.01,s2)*.01 for i in range(1,1500)); assert abs(a1-1)<.01 and abs(a2-1)<.01
pk1=max(fmx(i*.01,s1) for i in range(1,600)); pk2=max(fmx(i*.01,s2) for i in range(1,600)); assert pk1>pk2 and fmx(5,s2)>fmx(5,s1)
sv,sf=.95,7.0
c1=' '.join(f'({v*sv:.3f},{fmx(v,s1)*sf:.3f})' for v in [i*.2 for i in range(0,31)])
c2=' '.join(f'({v*sv:.3f},{fmx(v,s2)*sf:.3f})' for v in [i*.2 for i in range(0,31)])
g=[]
g.append(f'\\draw[->,thick] (0,0) -- ({6.6*sv+.2:.2f},0) node[below right] {{hız}}; \\draw[->,thick] (0,0) -- (0,{.7*sf:.2f}) node[above] {{molekül sayısı}};')
g.append(f'\\draw[thick] plot[smooth] coordinates {{{c1}}}; \\draw[thick,vurgu,densely dashed] plot[smooth] coordinates {{{c2}}};')
g.append(N(1.5*sv-.55,pk1*sf+.2,'$T_1$')); g.append(N(2.5*sv+.9,pk2*sf+.55,'$T_2$','text=vurgu'))
SK17=tk('\n'.join(g))
sec=[('T₂ sıcaklığı, T₁ sıcaklığından büyüktür.',True,'dağılımı sağa kayan ve genişleyen T₂ eğrisi daha yüksek sıcaklığa aittir'),
 ('T₂ sıcaklığında moleküllerin ortalama kinetik enerjisi T₁ sıcaklığındakinden büyüktür.',True,'ortalama kinetik enerji mutlak sıcaklıkla doğru orantılıdır'),
 ('Eğrilerin altında kalan alanlar birbirine eşittir.',True,'eğri altındaki alan toplam molekül sayısını gösterir ve aynı gaz örneği için değişmez'),
 ('En çok ihtimalli hıza sahip molekül sayısı T₁ sıcaklığında daha fazladır.',True,'düşük sıcaklıkta dağılım dar olduğundan tepe noktası daha yüksektir'),
 ('T₂ sıcaklığındaki bütün moleküller T₁ sıcaklığındaki bütün moleküllerden daha hızlıdır.',False,'iki dağılım üst üste biner; T₁’deki bazı moleküller T₂’deki bazı moleküllerden daha hızlıdır')]
order=[3,1,2,0,4]
rr=tek([sec[i] for i in order],hedef=False)
q('0017',[A('Eğrileri karşılaştır','Dağılımı sağa kayan, daha geniş ve alçak olan eğri daha yüksek sıcaklığa aittir.','T₂ > T₁'),
 A('Doğru ifadeleri ele','Ortalama kinetik enerji sıcaklıkla artar; alanlar eşittir; dar dağılımın tepesi yüksektir.','dört ifade doğru'),
 A('Yanlış ifadeyi bul','Dağılımlar üst üste bindiğinden T₁’deki bazı moleküller T₂’dekilerden hızlı olabilir.','yanlış: “bütün moleküller daha hızlıdır”')],
 metin='Aynı ideal gaz örneğinin T₁ ve T₂ sıcaklıklarındaki molekül hızı dağılımı şekilde verilmiştir.\nBuna göre aşağıdaki ifadelerden hangisi yanlıştır?',
 sekil=SK17,dogru=rr['dogru'],yan=rr['yan'],sira=rr['sira'],istenen='Yanlış olan ifade.',
 ip=['Her ifadeyi eğrilerin tepe konumu, genişliği ve altında kalan alan açısından ayrı ayrı sına.'],
 bilgi=[B('Hız dağılımı','Sıcaklık artınca hız dağılımı sağa kayar, genişler ve tepe yüksekliği azalır; eğrinin altındaki alan molekül sayısına eşittir. Örnek: ısıtılan bir gaz örneğinde molekül sayısı değişmediğinden alan sabittir')],
 puf='Sıcaklık yükselince ortalama hız artar ama her molekül hızlanmaz; dağılımlar üst üste biner.',
 tipId='gz-kinetik',tip=TIPLER['gz-kinetik'],z='orta',alt='Gazların Kinetik Teorisi',kaz='Molekül hızı dağılım grafiklerini sıcaklıkla ilişkilendirerek yorumlar.',kalip='grafik')

# ============ 0018 · efüzyon süreleri tablosu · orta ============
tHe,MHe18=3,4; tCH,MCH18=6,16; tX=12; MX=MHe18*Fr(tX,tHe)**2; assert MX==64 and MCH18*Fr(tX,tCH)**2==64 and MHe18*Fr(tCH,tHe)**2==16
assert MHe18*Fr(tX,tHe)==16 and MCH18*Fr(tX,tCH)==32 and MHe18*math.isqrt(tX//tHe)==8
sk=tablo_svg(['Gaz','Mol kütlesi (g/mol)','Efüzyon süresi (dk)'],[['He','4','3'],['CH₄','16','6'],['X','?','12']])
q('0018',[A('Süre oranını bul','Aynı koşulda efüzyon süresi mol kütlesinin kareköküyle doğru orantılıdır.','t(X) ÷ t(He) = 12 ÷ 3 = 4'),
 A('Mol kütle oranına geç','Süre oranının karesi mol kütle oranını verir.','M(X) ÷ M(He) = 4² = 16'),
 A('X’in mol kütlesini hesapla','He’un mol kütlesiyle çarp.','M(X) = 4 × 16 = 64 g/mol'),
 A('Kontrol et','CH₄ satırıyla da aynı sonuç elde edilmelidir.','16 × (12 ÷ 6)² = 64')],
 metin='Aynı sıcaklık ve basınçta, eşit mol sayılı gazların aynı büyüklükteki küçük bir delikten boşluğa tamamen efüze olma süreleri ölçülüyor ve sonuçlar aşağıdaki tabloda verilmiştir. Gazlar ideal davranmaktadır.\nBuna göre X gazının mol kütlesi kaç g/mol’dür?',
 sekil=sk,dogru=64,yan=[(8,'Süre oranının (4) karekökünü alıp He’un mol kütlesiyle çarpmış: 4 × 2 = 8 g/mol.','bilgi'),(12,'Tablodaki süreyi (12 dk) mol kütlesi olarak okumuş.','dikkat'),
  (16,'Süre oranını (4) karesini almadan He’un mol kütlesiyle çarpmış: 4 × 4 = 16 g/mol.','bilgi'),(32,'Süre oranını (2) karesini almadan CH₄’ün mol kütlesiyle çarpmış: 16 × 2 = 32 g/mol.','bilgi')],
 istenen='X gazının mol kütlesi (g/mol).',ip=['Efüzyon süresi ile mol kütlesi arasındaki ilişkinin türünü, tablodaki bilinen iki gazdan birini kullanarak kontrol et.'],
 bilgi=[B('Efüzyon','Aynı koşullarda efüzyon hızı mol kütlesinin kareköküyle ters orantılıdır; belirli miktar gazın boşalma süresi ise kareköküyle doğru orantılıdır. Örnek: süresi 3 kat uzun olan gazın mol kütlesi 9 kat büyüktür')],
 puf='Süre oranının karesini al: bu mol kütle oranını verir.',
 tipId='gz-difuz',tip=TIPLER['gz-difuz'],z='orta',alt='Difüzyon ve Efüzyon',kaz='Efüzyon sürelerinden bilinmeyen gazın mol kütlesini Graham yasasıyla bulur.',kalip='tablo')

# ============ 0019 · tepkime sonrası basınç · zor ============
nH,nO_,P19=4,3,7; use=Fr(nH,2); assert use<=nO_ ; nW=nH; nOl=nO_-use; ns=nW+nOl; Pson=P19*ns/(nH+nO_); assert (nW,nOl,ns,Pson)==(4,1,5,5)
assert (P19*nW/(nH+nO_)==4) and (P19*nOl/(nH+nO_)==1) and (P19-1==6)
g=[]
g.append('\\draw[thick] (0,0) rectangle (5,3.2);')
def h2(cx,cy,a): 
    dx=.17*math.cos(math.radians(a)); dy=.17*math.sin(math.radians(a))
    return f'\\draw[thick] ({cx-dx:.2f},{cy-dy:.2f}) circle (.14); \\draw[thick] ({cx+dx:.2f},{cy+dy:.2f}) circle (.14);'
def o2(cx,cy,a):
    dx=.24*math.cos(math.radians(a)); dy=.24*math.sin(math.radians(a))
    return f'\\filled ({cx-dx:.2f},{cy-dy:.2f}) circle (.2); \\filled ({cx+dx:.2f},{cy+dy:.2f}) circle (.2);'.replace('\\filled','\\fill')
for c in [(.9,2.5,20),(3.9,2.4,-30),(1.6,.9,60),(4.0,.8,10)]: g.append(h2(*c))
for c in [(2.5,2.3,80),(2.9,1.1,-20),(.7,1.5,0)]: g.append(o2(*c))
g.append(N(2.5,3.6,'sabit hacim, sabit sıcaklık: $P=7$ atm','font=\\small'))
g.append('\\draw[thick] (.4,-.7) circle (.14); \\draw[thick] (.74,-.7) circle (.14); '+N(1.0,-.7,'\\ce{H2}','anchor=west'))
g.append('\\fill (2.7,-.7) circle (.2); \\fill (3.17,-.7) circle (.2); '+N(3.5,-.7,'\\ce{O2}','anchor=west'))
SK19=tk('\n'.join(g))
q('0019',[A('Tepkime denklemini yaz','Tepkime 2H₂(g) + O₂(g) → 2H₂O(g) biçimindedir.','Şekilde: 4 H₂ ve 3 O₂ molekülü'),
 A('Sınırlayıcı bileşeni bul','4 H₂ molekülü için 2 O₂ gerekir; O₂ fazladır, H₂ tamamen harcanır.','4 H₂ + 2 O₂ → 4 H₂O'),
 A('Son mol sayısını yaz','Harcanmayan O₂ ve oluşan H₂O gazları birlikte sayılır.','n(H₂O) = 4 · n(O₂) = 3 − 2 = 1 → toplam 5'),
 A('Basıncı hesapla','Sabit V ve T’de basınç mol sayısıyla doğru orantılıdır.','7 ÷ 7 = P ÷ 5 → P = 5 atm')],
 metin='Sabit hacimli bir kapta H₂ ve O₂ gazları şekildeki gibidir. Kaba kıvılcım verilerek gazlar tam verimle tepkimeye sokuluyor ve kap tepkimeden önceki sıcaklığına getiriliyor. Tepkimeye giren ve oluşan bütün maddeler gaz hâlindedir.\nBuna göre son durumda kaptaki toplam basınç kaç atm olur?',
 sekil=SK19,dogru=5,yan=[(1,'Oluşan suyun sıvı olduğunu düşünüp yalnız artan O₂’nin basıncını (1 atm) bulmuş.','dikkat'),(4,'Yalnız oluşan H₂O’nun basıncını (4 atm) bulmuş; artan O₂’yi katmamış.','dikkat'),
  (6,'Tepkimeyi yalnız bir kez gerçekleşmiş sayıp mol sayısının bir azaldığını düşünmüş: 7 − 1 = 6 atm.','bilgi'),(7,'Kütlenin korunumunu mol sayısının korunumu sanmış; basınç değişmez demiş.','bilgi')],
 istenen='Kaptaki son toplam basınç (atm).',ip=['Önce hangi maddenin tamamen harcanacağını belirle; sonra sabit hacim ve sıcaklıkta basıncın neyle orantılı olduğunu düşün.'],
 bilgi=[B('Basınç ve mol sayısı','Sabit hacim ve sıcaklıkta gaz basıncı toplam gaz mol sayısıyla doğru orantılıdır. Mol sayısı tepkimede korunmak zorunda değildir. Örnek: N₂ + 3H₂ → 2NH₃ tepkimesinde 4 mol gazdan 2 mol gaz oluşur')],
 puf='Tepkimeden sonra basıncı, kalan ve oluşan gazların toplam mol sayısı belirler.',
 tipId='gz-kismi',tip=TIPLER['gz-kismi'],z='zor',alt='Gaz Karışımları',kaz='Gaz hâlindeki tepkimede sınırlayıcı bileşeni bulup sabit hacimde son basıncı mol sayısıyla hesaplar.',kalip='şekilli')

# ============ 0020 · sabit dış basınçta gaz ekleme · zor ============
Pd=F('1.5'); nHe20=F('0.2'); nNe20=F('0.6'); xHe20=nHe20/(nHe20+nNe20); PHe20=Pd*xHe20
assert (xHe20,PHe20)==(F('0.25'),F('0.375')) and Pd*nNe20/(nHe20+nNe20)==F('1.125') and Pd/2==F('0.75') and Pd/(nNe20/nHe20)==F('0.5')
hh1,hh2=1.0,4.0
def cyl(x0,hh,parts):
    s=(f'\\draw[thick] ({x0},5.2) -- ({x0},0) -- ({x0+1.8},0) -- ({x0+1.8},5.2); \\fill[vurgu!12] ({x0+.02},.02) rectangle ({x0+1.78},{hh}); \\fill[gray!45] ({x0+.02},{hh}) rectangle ({x0+1.78},{hh+.18}); \\draw[thick] ({x0},{hh}) rectangle ({x0+1.8},{hh+.18});')
    for (px,py,k) in parts:
        s+=(f'\\draw[thick,fill=white] ({x0+px:.2f},{py:.2f}) circle (.13);' if k=='he' else f'\\fill ({x0+px:.2f},{py:.2f}) circle (.13);')
    s+=N(x0+.9,hh+.55,'dış basınç\\\\$1{,}5$ atm','align=center,font=\\small')
    return s
left=[(.45,.35,'he'),(1.25,.65,'he')]
right=[(.45,.4,'he'),(1.3,2.8,'he'),(.4,1.3,'ne'),(1.3,.5,'ne'),(.9,1.9,'ne'),(1.35,1.5,'ne'),(.55,2.6,'ne'),(.9,3.3,'ne')]
g=[cyl(0,hh1,left),cyl(4.6,hh2,right)]
g.append(f'\\draw[{ARR}] (2.1,1.0) -- (4.3,1.0); '+N(3.2,1.7,'$0{,}6$ mol Ne\\\\eklenir','align=center,font=\\small'))
g.append(N(.9,-.45,'$0{,}2$ mol He','font=\\small'))
g.append('\\draw[thick,fill=white] (4.7,-1.2) circle (.13); '+N(4.95,-1.2,'He','anchor=west,font=\\small')+' \\fill (5.8,-1.2) circle (.13); '+N(6.05,-1.2,'Ne','anchor=west,font=\\small'))
SK20=tk('\n'.join(g))
q('0020',[A('Piston ve toplam basınç','Dış basınç sabit olduğundan piston dengede iken karışımın toplam basıncı 1,5 atm kalır.','P(toplam) = 1,5 atm'),
 A('Mol kesrini bul','Karışımda toplam mol sayısı 0,2 + 0,6 = 0,8’dir.','X(He) = 0,2 ÷ 0,8 = 1/4'),
 A('Kısmi basıncı hesapla','Kısmi basınç = mol kesri × toplam basınç.','P(He) = 1,5 × 1/4 = 0,375 atm')],
 metin='Sürtünmesiz hareketli bir pistonla kapatılmış kapta bulunan He gazının üzerine, sabit sıcaklıkta şekilde belirtilen miktarda Ne gazı ekleniyor. Piston yeniden dengeye ulaştığında dış basınç değişmemiştir ve gazlar ideal davranmaktadır.\nBuna göre son durumda He gazının kısmi basıncı kaç atm’dir?',
 sekil=SK20,dogru=F('0.375'),yan=[(F('0.5'),'Gaz miktarı 3 katı sanıp (0,6 ÷ 0,2) basıncı 3’e bölmüş: 1,5 ÷ 3 = 0,5 atm.','islem'),(F('0.75'),'He ile Ne’un mol sayılarını eşit sayıp mol kesrini 1/2 almış: 1,5 ÷ 2 = 0,75 atm.','bilgi'),
  (F('1.125'),'Ne gazının kısmi basıncını (1,5 × 3/4) bulmuş; He’u sormuş olduğunu atlamış.','dikkat'),(F('1.5'),'Toplam basıncı He’un kısmi basıncı sanmış.','bilgi')],
 istenen='He gazının son kısmi basıncı (atm).',ip=['Piston dengede iken toplam gaz basıncının neye eşit kaldığını belirle.'],
 bilgi=[B('Kısmi basınç','Karışımdaki bir gazın kısmi basıncı, toplam basıncın o gazın mol kesri ile çarpımıdır. Örnek: toplam basınç 2 atm olan, mol sayıları eşit iki gazlı karışımda her gazın kısmi basıncı 1 atm’dir')],
 puf='Pistonlu kapta toplam basınç dış basınca eşittir; hacim değişse bile kısmi basınç mol kesriyle bulunur.',
 tipId='gz-kismi',tip=TIPLER['gz-kismi'],z='zor',alt='Gaz Karışımları',kaz='Sabit dış basınçlı pistonlu kapta gaz eklenmesiyle oluşan karışımın kısmi basınçlarını mol kesrinden hesaplar.',kalip='şekilli')

# ============ yaz ============
for qq in P.ANA: qq['kardes']=None
SC='/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/gazlar'
os.makedirs(SC,exist_ok=True)
assert len(P.ANA)==20
P.yaz(os.path.join(GD,'gazlar-1.json'),os.path.join(SC,'bos-gazlar.json'))
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=UK))['kartlar'].append(c['id'])
json.dump(dict(konu=KONU_,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2018–2026 Kimya (yalnız mantık), MEB 11. sınıf kimya.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','akgazlar.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
