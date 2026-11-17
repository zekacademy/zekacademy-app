"""TYT Biyoloji · Hücre ve Organeller – Madde Geçişleri · 3. paket (hucreuc): 10 soru, kardeş yok, ipucu 1.
Grafik değerleri, küp hacimleri, ozmoz oranları ve öncül doğrulukları Python'da hesaplanır/assert edilir; şekiller aynı değerlerden çizilir.
Öncüllerin doğru/yanlış değeri tek yerde (d sözlüğü) tanımlanır; anahtar, adım ve çeldirici açıklamaları oradan üretilir."""
import sys,os,math
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_bio as H
from _hafif_bio3 import *
KONU_='Hücre ve Organeller – Madde Geçişleri'; UK='bio|'+KONU_; H.KONU=KONU_
P=Parti('hucreuc',KONU_,UK,ders='TYT Biyoloji',idon='tytbio')
KY='ÖSYM 2018–2026 TYT Biyoloji (yalnız mantık) · MEB 9. sınıf Hücre ve Organeller, Madde Geçişleri'
TIP={'salgi':('by-hc3-salgi','Radyoaktif işaretleme ve salgı yolu'),'organel':('by-hc3-organel','Organel çeşitleri ve işlevleri'),
     'deney':('by-hc3-deney','Madde geçişi deneyi ve değişkenler'),'yuzey':('by-hc3-yuzey','Yüzey/hacim oranı ve madde alışverişi'),
     'ozmoz':('by-hc3-ozmoz','Ozmoz ve günlük yaşam / canlı örnekleri'),'gecis':('by-hc3-gecis','Zardan madde geçişi grafiği')}
def kartla(n,tip,alt,fikir,tuzak,z,kalip,adim):
    kart(f'K-BYHC3-{n}',alt,fikir,tuzak,z,kalip,adim,TIP[tip][0],TIP[tip][1],KY)
def q(no,tip,ad,ne,**k):
    assert len(k['ip'])==1
    mk(P,no,ad=ad,adim=len(ad),tipId=TIP[tip][0],tip=TIP[tip][1],kart=f"K-BYHC3-{no[-2:]} ({TIP[tip][1].lower()}) · {ne}",**k)
def F(a,b=1): return Fr(a,b)
AX='tick label style={font=\\footnotesize},label style={font=\\small},axis lines=left,every axis plot/.append style={line width=1.5pt}'

# ============ 0001 · radyoaktif amino asit grafiği · orta ============
kartla('01','salgi','Salgı yolu – radyoaktivite–zaman grafiği','İşaretli amino asitle yapılan protein, sentez ve taşınma sırasında yapıları sırayla geçer: granüllü ER’de erken, Golgi’de sonra, salgı kesecikleri ve hücre dışında en geç yoğunlaşır. Grafikte tepe noktasının zamanı sırayı verir.','Tepe yüksekliğine bakarak sıra belirlemek; Golgi’yi ER’den önce sanmak.','orta','grafik',4)
def egri(t,tp,a): return a*(t/tp)*math.exp(1-t/tp)
TP={'ER':6,'Golgi':20,'Kesecik':45}; AA={'ER':100,'Golgi':85,'Kesecik':70}
assert TP['ER']<TP['Golgi']<TP['Kesecik'] and all(abs(max(egri(t/4,TP[k],AA[k]) for t in range(0,241))-AA[k])<1.5 for k in TP)
def cr(k): return ' '.join(f'({t/2:.1f},{egri(t/2,TP[k],AA[k]):.1f})' for t in range(0,121))
b=['\\begin{axis}[width=7.8cm,height=5.4cm,xmin=0,xmax=60,ymin=0,ymax=115,xtick={0,10,20,30,40,50,60},ytick=\\empty,xlabel={Zaman (dk)},ylabel={Radyoaktivite},'+AX+']',
   f'\\addplot[black] coordinates {{{cr("ER")}}};',f'\\addplot[black,densely dashed] coordinates {{{cr("Golgi")}}};',f'\\addplot[vurgu] coordinates {{{cr("Kesecik")}}};',
   '\\node[font=\\normalsize\\bfseries] at (axis cs:11,104) {I};\\node[font=\\normalsize\\bfseries] at (axis cs:26,89) {II};\\node[font=\\normalsize\\bfseries,vurgu] at (axis cs:45,79) {III};','\\end{axis}']
SK1=tk('\n'.join(b),1.0)
S1=['I: Granüllü endoplazmik retikulum, II: Golgi cisimciği, III: Salgı kesecikleri','I: Golgi cisimciği, II: Granüllü endoplazmik retikulum, III: Salgı kesecikleri',
    'I: Salgı kesecikleri, II: Golgi cisimciği, III: Granüllü endoplazmik retikulum','I: Granüllü endoplazmik retikulum, II: Salgı kesecikleri, III: Golgi cisimciği',
    'I: Golgi cisimciği, II: Salgı kesecikleri, III: Granüllü endoplazmik retikulum']
q('0001','salgi',[A('Deneyin mantığını kur','İşaretli amino asitle yapılan proteinler hücre içinde ilerledikçe radyoaktivite de aynı yapılara sırayla taşınır.','Radyoaktivite = protein'),
   A('Sırayı belirle','Protein ribozomlu granüllü ER’de sentezlenir, Golgi cisimciğinde paketlenir, kesecikle hücre dışına salgılanır.','Granüllü ER → Golgi → salgı kesecikleri'),
   A('Grafikle eşleştir','Tepe noktası en erken I’de, sonra II’de, en geç III’te görülür.','Tepe zamanı: I < II < III'),
   A('Şıkları ele','I = granüllü ER, II = Golgi cisimciği, III = salgı kesecikleri eşleşmesi tepe sırasına uyar.','Doğru: I–ER, II–Golgi, III–kesecik')],
 'pankreas hücresi, işaretli amino asit',z='orta',alt='Salgı Yolu',kaz='Radyoaktif işaretleme grafiğinden proteinin hücre içi yolunu ve organel sırasını belirler.',kalip='grafik',
 metin='Bir araştırmacı, sindirim enzimi salgılayan bir hücreye kısa süre radyoaktif işaretli amino asit veriyor, ardından hücreyi işaretsiz amino asitli ortama aktarıyor. Üç yapıdaki radyoaktivite zamanla ölçülüyor ve sonuçlar grafikte I, II, III ile gösteriliyor. Bu yapılar Golgi cisimciği, salgı kesecikleri ve granüllü endoplazmik retikulumdur.\nBuna göre, I, II ve III ile gösterilen yapılar aşağıdakilerin hangisinde doğru verilmiştir?',
 sekil=SK1,dogru=S1[0],sira=yer('B',S1[0],S1[1:]),
 yan=[(S1[1],'Golgi cisimciği ile granüllü ER sırası ters alınmış; protein önce ribozomlu ER’de yapılır, radyoaktivite ER’de ilk tepe noktasına ulaşır.','bilgi'),
      (S1[2],'Sırayı tamamen tersine çevirmiş; hücre dışına çıkan protein önce sentezlenmeli, en son kesecikte yoğunlaşmalıdır.','bilgi'),
      (S1[3],'Golgi ile kesecik yer değiştirmiş; kesecikler Golgi’den koptuğu için kesecikteki radyoaktivite Golgi’den sonra zirve yapar.','dikkat'),
      (S1[4],'ER’yi son sıraya koymuş; ER proteinin sentezlendiği ilk yapıdır ve radyoaktivite en erken orada görülür.','bilgi')],
 istenen='Grafikteki I, II ve III numaralı eğrilerin hangi yapılara ait olduğu.',
 ip=['Proteinin sentezlendiği yerden hücre dışına çıkana dek uğradığı yapıları sıraya diz ve eğrilerin tepe noktalarının zamanını karşılaştır.'],
 bilgi=[B('Salgı proteinlerinin yolu','Hücre dışına salgılanan proteinler ribozomlu yapıda sentezlenir ve kesecikler yoluyla zardan dışarı verilir')],
 puf='İşaretli maddenin geçtiği yapılar zamana göre sıralanır: tepe noktası ne kadar erkense yapı yoldaki ilk basamaklara o kadar yakındır.')

# ============ 0002 · plastit · kolay · olumsuz ============
kartla('02','organel','Plastit çeşitleri','Plastitler bitki hücrelerinde bulunan çift zarlı organellerdir: kloroplast klorofil içerir ve fotosentez yapar, kromoplast renkli pigment taşır, lökoplast renksizdir ve besin (nişasta, yağ) depolar.','Renksiz plastitlerin de fotosentez yaptığını sanmak; plastitleri yalnız kloroplast saymak.','kolay','düz',3)
S2=['Patates yumrusundaki renksiz plastitler ışık enerjisini kullanarak glikoz sentezler.','Yaprak hücrelerindeki yeşil plastitler klorofil taşır ve ışık enerjisini kimyasal enerjiye dönüştürür.',
    'Havuç kökündeki turuncu plastitler pigment içerir ve organa renk verir.','Patates yumrusundaki renksiz plastitler nişasta gibi besinleri depolar.','Yaprak, kök ve yumru hücrelerindeki plastitlerin hepsi çift zarla çevrilidir.']
q('0002','organel',[A('Plastit çeşitlerini tanı','Yeşil olan kloroplast, turuncu pigmentli olan kromoplast, renksiz olan lökoplasttır.','Yaprak: kloroplast · Havuç: kromoplast · Patates: lökoplast'),
   A('Görevleri eşleştir','Fotosentez yalnız klorofilli kloroplastta olur; lökoplast besin depolar.','Lökoplast: depolama'),
   A('Yanlış ifadeyi bul','Renksiz plastitin ışık enerjisiyle glikoz sentezlediğini söyleyen ifade yanlıştır.','Yanlış: lökoplast fotosentez yapar')],
 'yaprak, havuç kökü, patates yumrusu plastitleri',z='kolay',alt='Organeller',kaz='Plastit çeşitlerini ve işlevlerini ayırt eder.',kalip='hikâyeli',
 metin='Bitkilerde plastit denilen organeller, bulundukları dokuya göre farklı görünür ve farklı işlevler üstlenir. Bir bitki biyoloğu, bir bitkinin yaprağında yeşil, havuç kökünde turuncu, patates yumrusunda ise renksiz plastitler bulunduğunu mikroskopla görüyor.\nBu plastitlerle ilgili aşağıdakilerden hangisi yanlıştır?',
 dogru=S2[0],sira=yer('E',S2[0],S2[1:]),
 yan=[(S2[1],'Kloroplast klorofil taşır ve fotosentezle ışık enerjisini kimyasal enerjiye çevirir. Bu doğru bir ifadedir; “yeşil plastit” ifadesine takılıp yanlış sanılmış.','bilgi'),
      (S2[2],'Kromoplastlar karotenoit gibi renkli pigmentler taşır; havuç köküne rengini verir. İfade doğrudur.','bilgi'),
      (S2[3],'Lökoplastlar renksizdir ve nişasta gibi besinleri depolar; patates yumrusundaki nişasta lökoplastlarda birikir. İfade doğrudur.','bilgi'),
      (S2[4],'Tüm plastitler çift zarlı organellerdir. İfade doğrudur; kloroplast dışındaki plastitler yanlışlıkla zarsız sanılmış.','dikkat')],
 istenen='Plastitlerle ilgili yanlış olan ifade.',
 ip=['Her plastit türünün rengini ve hücrede üstlendiği görevi ayrı ayrı düşün; yalnız hangisinde klorofil bulunduğuna bak.'],
 bilgi=[B('Plastitler','Bitki hücrelerinde bulunan çift zarlı organellerdir · Kloroplast klorofil içerir, kromoplast renkli pigment taşır, lökoplast renksizdir ve besin depolar')],
 puf='Fotosentez klorofil gerektirir; klorofilsiz (renksiz) plastit ışıkla besin üretemez.')

# ============ 0003 · selofan kese tablosu · orta ============
kartla('03','deney','Selofan kese deneyi – değişkenler ve yorum','Aynı koşullarda yalnız kesedeki derişim değiştirilir (bağımsız değişken); kese kütlesindeki değişim ölçülür (bağımlı değişken). Su derişimi düşük (çözünen fazla) tarafa geçer, bu yüzden kütle artışı/azalışı yönü derişim karşılaştırmasından çıkar.','Su yönünü ters almak; sabit tutulan değişkenle bağımsız değişkeni karıştırmak; değişim olmayınca su geçişi yok sanmak.','orta','tablo',4)
beher=15; kese=[5,15,30]; kt0=40; kt=[kt0+x for x in (-3,0,4)]
for c,k in zip(kese,kt):
    yon='dışarı' if c<beher else ('yok' if c==beher else 'içeri')
    assert (k<kt0 and yon=='dışarı') or (k==kt0 and yon=='yok') or (k>kt0 and yon=='içeri')
S3=['Bağımsız değişken kesedeki şeker derişimidir; 1. kesede su dışarı çıktığı için kütle azalmıştır.','Bağımlı değişken kesedeki şeker derişimidir; 3. kesede su dışarı çıktığı için kütle artmıştır.',
    'Bağımsız değişken beherdeki çözeltinin derişimidir; 2. kesede kütle değişmediği için su geçişi olmamıştır.','Bağımlı değişken kese kütlesindeki değişimdir; 3. kesede şeker dışarı çıktığı için kütle artmıştır.',
    'Sabit tutulan değişken kesedeki şeker derişimidir; 1. kesede su içeri girdiği için kütle azalmıştır.']
q('0003','deney',[A('Değişkenleri belirle','Deneyci yalnız kesedeki derişimi değiştirmiştir; ölçülen kese kütlesindeki değişimdir; beher derişimi, kese boyutu ve süre sabittir.','Bağımsız: kesedeki derişim · Bağımlı: kütle değişimi'),
   A('Su yönünü bul','Kese derişimi beherdekinden (%15) düşük ise su dışarı, yüksek ise içeri geçer; eşitse net geçiş olmaz.','1. kese: dışarı · 2. kese: net yok · 3. kese: içeri'),
   A('Kütleyle eşleştir','Su kaybeden kese hafifler, su alan kese ağırlaşır.','1. kese: 40 → 37 g · 3. kese: 40 → 44 g'),
   A('Şıkları ele','Doğru şık, değişkenleri doğru adlandırıp 1. kesedeki su çıkışını doğru yorumlayan şıktır.','Doğru: A')],
 'üç selofan kese, %15’lik beher',z='orta',alt='Deney ve Ozmoz',kaz='Selofan kese deneyinde değişkenleri belirler ve kütle değişimini ozmozla yorumlar.',kalip='tablo',
 metin='Bir öğrenci, suyu ve küçük molekülleri geçiren aynı boyutlu üç selofan kesenin her birine eşit hacimde, derişimi farklı şeker çözeltisi dolduruyor. Şeker selofandan geçememektedir. Keseleri tartıp her birini, aynı hacimde %15’lik şeker çözeltisi bulunan ayrı beherlere batırıyor. Bir saat sonra keseleri yeniden tartıyor ve sonuçları aşağıdaki tabloda gösteriyor.\nBuna göre, aşağıdakilerden hangisi doğrudur?',
 sekil=tablo_svg(['Kese','Şeker (%)','İlk kütle (g)','Son kütle (g)'],[['1. kese','5','40','37'],['2. kese','15','40','40'],['3. kese','30','40','44']]),
 dogru=S3[0],sira=yer('A',S3[0],S3[1:]),
 yan=[(S3[1],'Kesedeki derişim deneyci tarafından değiştirilen (bağımsız) değişkendir; ölçülen kütledir. Ayrıca 3. kesede su içeri girmiş, kütle bu yüzden artmıştır.','dikkat'),
      (S3[2],'Beher derişimi tüm keselerde %15’tir, yani sabittir. 2. kesede kütle değişmemesi su geçişinin dengede olduğunu gösterir; su geçişi durmaz, net geçiş sıfırdır.','bilgi'),
      (S3[3],'Bağımlı değişken doğru; ancak 3. kesede şeker değil su içeri girmiştir (şeker selofandan geçemez), kütle bu yüzden artmıştır.','bilgi'),
      (S3[4],'Kesedeki derişim deneyde değiştirilen değişkendir, sabit tutulan değildir. 1. kesede su dışarı çıktığı için kütle azalmıştır, içeri girmemiştir.','bilgi')],
 istenen='Tablodaki deney sonuçlarına ve değişkenlere ilişkin doğru ifade.',
 ip=['Deneyde sınanan değişkenle ölçülen değişkeni ayır; sonra su geçişinin yönünü kese ile beherin derişimini karşılaştırarak belirle.'],
 bilgi=[B('Deneyde değişkenler','Bağımsız değişken deneyci tarafından değiştirilen, bağımlı değişken ölçülen, sabit tutulan değişken ise sonucu etkilememesi için aynı bırakılan koşuldur'),
        B('Ozmoz yönü','Su, yarı geçirgen zardan çözünen derişiminin düşük olduğu ortamdan yüksek olduğu ortama geçer')],
 puf='Değişkenleri “neyi değiştirdim, neyi ölçtüm, neyi sabit tuttum?” diye sor; su yönünü çözünen derişimi yüksek olan tarafa göre ver.')

# ============ 0004 · agar küp · zor · öncüllü ============
kartla('04','yuzey','Yüzey/hacim oranı – agar küp deneyi','Küp büyüdükçe hacim yüzey alanından hızlı artar; yüzey/hacim oranı azalır. Maddenin her yüzeyden sabit derinliğe işlemesi durumunda boyanan hacim, küpün iç bölgesi çıkarılarak hesaplanır.','Büyük küpte boyanan hacmin oranının da büyük olacağını sanmak; iç küpün kenarını yanlış hesaplamak.','zor','öncüllü',5)
def kup(a,d=1): return dict(a=a,hacim=a**3,yuzey=6*a*a,ic=max(a-2*d,0)**3)
K4=[kup(2),kup(4),kup(6)]
assert [k['ic'] for k in K4]==[0,8,64]
boy=[Fr(k['hacim']-k['ic'],k['hacim']) for k in K4]; assert boy==[F(1),F(7,8),F(19,27)]
yh=[Fr(k['yuzey'],k['hacim']) for k in K4]; assert yh==[3,F(3,2),1] and boy[0]>boy[1]>boy[2]
d4={'I':(True,'Kenar uzunluğu arttıkça yüzey alanı kenarın karesiyle, hacim kübüyle artar; yüzey alanı/hacim oranı 6/a olduğundan küp büyüdükçe azalır (3 → 1,5 → 1).'),
    'II':(False,'4 cm kenarlı küpte iç bölge 2 cm kenarlıdır (8 cm³); boyanan hacim 64 − 8 = 56 cm³’tür, yani toplam hacmin 7/8’i. Yarısı değildir.'),
    'III':(True,'6 cm kenarlı küpte iç bölge 6 − 2 = 4 cm kenarlıdır; boyanmayan bölgenin hacmi 4 × 4 × 4 = 64 cm³’tür.')}
r=onc(d4,True,'D')
def ci(x,a,s=.5):
    w=a*s; o=[f'\\draw[line width=1.2pt,fill=vurgu!25] ({x},0) rectangle ({x+w},{w});']
    if a>2: o.append(f'\\draw[line width=1.2pt,fill=white] ({x+s},{s}) rectangle ({x+w-s},{w-s});')
    o.append(f'\\node[font=\\small] at ({x+w/2},-.4) {{{a} cm}};')
    return '\n'.join(o)
SK4=tk(ci(0,2)+'\n'+ci(1.5,4)+'\n'+ci(4.5,6)+'\n\\draw[line width=.8pt] (1.5,2.05)--(1.5,2.3);\\draw[line width=.8pt] (2.0,2.05)--(2.0,2.3);\\draw[<->,line width=.8pt] (1.5,2.18)--(2.0,2.18);\\node[font=\\small] at (1.75,2.55) {1 cm};',1.0)
q('0004','yuzey',[A('Yüzey/hacim oranını hesapla','Kenarı a olan küpün yüzeyi 6a², hacmi a³’tür; oran 6/a.','2 cm: 3 · 4 cm: 1,5 · 6 cm: 1'),
   A('İç bölgeleri bul','Boya her yüzeyden 1 cm girdiği için iç küpün kenarı a − 2 cm’dir.','2 cm: 0 · 4 cm: 2 cm · 6 cm: 4 cm'),
   adim_onc(d4,'I'),adim_onc(d4,'II'),adim_onc(d4,'III'),sonuc(r,True)],
 'üç boyutta agar küp, kesit',z='zor',alt='Yüzey/Hacim Oranı',kaz='Küp modelinde yüzey/hacim oranı ve boyanan hacim hesabıyla hücre büyüklüğü–madde alışverişi ilişkisini yorumlar.',kalip='öncüllü',
 metin='Bir öğrenci, hücre büyüklüğü ile madde alışverişi arasındaki ilişkiyi göstermek için kenar uzunlukları farklı üç agar küpünü boya çözeltisine batırıyor. Boya, küpün her yüzeyinden eşit derinlikte içeri işlemektedir. Küpler ortadan kesiliyor; kesitler ve boyanan bölgeler (renkli) şekilde verilmiştir.\nBuna göre,\nI. Küp büyüdükçe yüzey alanının hacme oranı azalır.\nII. 4 cm kenarlı küpün boyanan hacmi, toplam hacminin yarısıdır.\nIII. 6 cm kenarlı küpte boyanmayan iç bölgenin hacmi 64 cm³’tür.\nyargılarından hangileri doğrudur?',
 sekil=SK4,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',
 ip=['Her küpün iç bölgesinin kenarını, boyanan kalınlığı çıkararak bul; sonra yüzey ve hacmi karşılaştır.'],
 bilgi=[B('Yüzey ve hacim','Küpün yüzey alanı kenarın karesiyle, hacmi kenarın küpüyle orantılıdır · Hücre büyüdükçe hacim, yüzeye göre hızlı artar; bu, madde alışverişinin yeterliliğini etkiler')],
 puf='Büyüyen cisimde hacim yüzeyden hızlı artar; yüzeyden giren maddenin ulaşamadığı iç bölge büyür.')

# ============ 0005 · günlük ozmoz · kolay · olumsuz ============
kartla('05','ozmoz','Günlük yaşamda ozmoz ve difüzyon ayrımı','Ozmoz suyun yarı geçirgen zardan geçişidir; tuz/şeker serpilince bitkisel dokudan su çıkması, kuru gıdanın suda şişmesi ve kökün su alması ozmozdur. Kokunun yayılması gibi gaz hareketleri difüzyondur.','Her madde hareketine ozmoz demek; tuzlu su içince susamayı ozmozla ilişkilendirmemek.','kolay','hikâyeli',3)
S5=['Odanın bir köşesine sıkılan parfümün kokusunun zamanla odaya yayılması','Tuz serpilen patlıcan dilimlerinin bir süre sonra su bırakması','Kuru üzümün suya konulunca şişmesi','Tuzlu suda bekletilen taze marulun sertliğini kaybedip solması','Bitki köklerinin topraktaki suyu kök tüyleriyle alması']
q('0005','ozmoz',[A('Ozmozu tanımla','Ozmoz, suyun yarı geçirgen zardan geçişidir.','Ozmoz = suyun geçişi'),
   A('Olayları tek tek sına','Patlıcan, üzüm, marul ve kök olaylarında hücre zarından su geçişi vardır.','Hepsi ozmoz'),
   A('Ozmoz olmayanı seç','Koku molekülleri gaz hâlinde yayılır; zar ve su geçişi yoktur.','Parfüm kokusu: difüzyon')],
 'patlıcan, üzüm, marul, kök, parfüm',z='kolay',alt='Ozmoz',kaz='Günlük yaşam örneklerinden ozmozla ilişkili olmayanı belirler.',kalip='hikâyeli',
 metin='Ozmoz, suyun yarı geçirgen bir zardan geçmesidir. Bir öğretmen, öğrencilerinden günlük yaşamda karşılaştıkları bazı olayları ozmozla ilişkilendirmelerini istiyor ve öğrenciler aşağıdaki olayları sıralıyor.\nBu olaylardan hangisinin ozmozla ilişkili olduğu söylenemez?',
 dogru=S5[0],sira=yer('C',S5[0],S5[1:]),
 yan=[(S5[1],'Tuz serpilince dilimlerin hücrelerinden su, daha derişik tuzlu ortama çıkar; ozmozla ilgilidir.','bilgi'),
      (S5[2],'Kuru üzümün hücrelerindeki derişim yüksektir; su hücrelere ozmozla girer ve üzüm şişer.','bilgi'),
      (S5[3],'Tuzlu su, marul hücrelerine göre derişiktir; hücrelerden su ozmozla çıkar ve marul solar.','dikkat'),
      (S5[4],'Köklerde su, derişimi düşük topraktan hücrelere ozmozla geçer.','bilgi')],
 istenen='Ozmozla ilişkisi olmayan olay.',
 ip=['Her olayda suyun yarı geçirgen bir zardan geçip geçmediğine bak.'],
 bilgi=[B('Ozmoz ve difüzyon','Ozmoz, suyun yarı geçirgen zardan geçişidir · Difüzyon ise madde taneciklerinin derişimin çok olduğu ortamdan az olduğu ortama yayılmasıdır; zar gerektirmeyebilir')],
 puf='Zar ve su geçişi varsa ozmoz; gaz ya da çözünen taneciklerin yayılması varsa difüzyon düşün.')

# ============ 0006 · derişim–zaman grafiği · orta · öncüllü ============
kartla('06','gecis','Zar iki maddeyi geçiriyorsa derişim–zaman grafiği','Zar X’i geçiriyorsa X derişim farkı yönünde yayılır ve iki bölmede derişim eşitlenince net geçiş durur; ancak taneciklerin iki yöndeki hareketi sürer (dinamik denge). Pasif taşıma enerji harcamaz.','Derişimler eşitlenince hareketin tamamen durduğunu sanmak; geçişi ATP’ye bağlamak.','orta','öncüllü',4)
def e6(t,c0,cs,tau=2.5): return cs+(c0-cs)*math.exp(-t/tau)
SOL6=lambda t:e6(t,8,5); SAG6=lambda t:e6(t,2,5)
assert abs(SOL6(0)-8)<1e-9 and abs(SAG6(0)-2)<1e-9 and abs(SOL6(10)-5)<0.1 and all(abs(SOL6(t)+SAG6(t)-10)<1e-9 for t in range(0,11))
cs=' '.join(f'({t/2:.1f},{SOL6(t/2):.2f})' for t in range(0,25)); cg=' '.join(f'({t/2:.1f},{SAG6(t/2):.2f})' for t in range(0,25))
b=['\\begin{axis}[width=7.6cm,height=5.4cm,xmin=0,xmax=12,ymin=0,ymax=9,xtick={0,2,4,6,8,10,12},ytick={0,2,4,6,8},xlabel={Zaman (dk)},ylabel={X derişimi (birim)},'+AX+']',
   f'\\addplot[black] coordinates {{{cs}}};',f'\\addplot[black,densely dashed] coordinates {{{cg}}};',
   '\\node[font=\\small\\bfseries,anchor=south] at (axis cs:8.5,5.5) {Sol bölme};\\node[font=\\small\\bfseries,anchor=north] at (axis cs:8.5,4.5) {Sağ bölme};','\\end{axis}']
SK6=tk('\n'.join(b),1.0)
d6={'I':(True,'X’in derişimi sol bölmede azalıp sağ bölmede arttığına göre X, derişimin çok olduğu sol bölmeden az olduğu sağ bölmeye difüzyonla geçmiştir.'),
    'II':(False,'Derişimler eşitlendikten sonra net geçiş sıfırdır; ancak X tanecikleri iki yönde hareketini sürdürür. Geçişin tamamen durduğu söylenemez.'),
    'III':(True,'Derişimler eşitlendikten sonra iki yöndeki geçiş hızları eşittir (dinamik denge); bu yüzden derişimler değişmez.')}
r=onc(d6,True,'D')
q('0006','gecis',[A('Grafiği oku','Sol bölmede X derişimi 8’den 5’e düşer, sağ bölmede 2’den 5’e çıkar ve 10. dakika civarında eşitlenir.','Sol: 8 → 5 · Sağ: 2 → 5'),
   adim_onc(d6,'I'),adim_onc(d6,'II'),adim_onc(d6,'III'),sonuc(r,True)],
 'iki bölme, X derişimleri eşitleniyor',z='orta',alt='Madde Geçişi',kaz='Derişim–zaman grafiğinden difüzyonun yönünü ve dinamik dengeyi yorumlar.',kalip='grafik',
 metin='Bir kap, X maddesini de suyu da geçiren bir zarla iki eşit bölmeye ayrılıyor. Sol bölmeye derişimi yüksek, sağ bölmeye derişimi düşük X çözeltisi konuluyor. Bölmelerdeki X derişimi zamanla ölçülüyor ve grafikte gösteriliyor; bölme hacimleri sabittir.\nBuna göre,\nI. X, sol bölmeden sağ bölmeye difüzyonla geçmiştir.\nII. 10. dakikadan sonra X taneciklerinin zardan geçişi tamamen durmuştur.\nIII. Derişimler eşitlendikten sonra X taneciklerinin iki yöndeki geçiş hızları birbirine eşittir.\nyargılarından hangileri doğrudur?',
 sekil=SK6,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',
 ip=['Grafikte iki eğrinin zamanla nasıl değiştiğine ve eşitlendikten sonra neler olduğuna bak.'],
 bilgi=[B('Difüzyon ve denge','Difüzyon, maddenin derişimi çok olan ortamdan az olan ortama geçişidir ve enerji gerektirmez')],
 puf='Eşit derişimde “net geçiş sıfır” demek “hareket yok” demek değildir.')

# ============ 0007 · nişasta–iyot düzeneği · orta · öncüllü ============
kartla('07','deney','Selofan kese: nişasta, glikoz ve iyot','Selofan küçük molekülleri geçirir: iyot ve glikoz geçer, büyük molekül nişasta geçemez. Kesenin içinin mavi-siyaha dönmesi iyodun içeri girdiğini, dışarıda Benedict pozitifliği glikozun dışarı çıktığını gösterir.','Mavi-siyah rengi nişastanın dışarı çıkması sanmak; glikozun geçemediğini düşünmek.','orta','öncüllü',4)
d7={'I':(True,'Kesenin içi mavi-siyaha dönmüştür; iyot nişastayla ancak iç ortamda buluşup bu rengi verebilir, yani iyot molekülleri selofandan içeri geçmiştir.'),
    'II':(True,'Beherdeki çözeltinin rengi sarı-kahverengi kalmıştır; nişasta dışarı geçseydi dış ortamda da mavi-siyah renk oluşurdu. Nişasta molekülleri selofandan geçememiştir.'),
    'III':(False,'Beherden alınan örnekte Benedict testi pozitiftir; bu, glikozun kesenin dışına geçtiğini gösterir. Glikoz selofandan geçmiştir.')}
r=onc(d7,True,'B')
b=['\\draw[line width=1.6pt] (0,0) -- (0,3.6) (4.2,0) -- (4.2,3.6);\\draw[line width=1.6pt] (0,0) -- (4.2,0);',
   '\\fill[vurgu,fill opacity=.15] (0.04,0.04) rectangle (4.16,2.8);\\draw[line width=.7pt] (0.04,2.8)--(4.16,2.8);',
   '\\draw[line width=1.2pt,dashed,rounded corners=10pt,fill=white] (.8,.5) rectangle (3.4,2.5);\\draw[line width=1.3pt] (2.1,2.5)--(2.1,3.9);',
   '\\node[font=\\small,align=center] at (2.1,1.5) {nişasta ve\\\\glikoz çözeltisi};',
   '\\node[font=\\small,align=center,anchor=south] at (2.1,3.95) {selofan kese};',
   '\\draw['+OKU+',line width=.8pt] (5.1,2.0)--(3.75,2.0);\\node[font=\\small,anchor=west,align=left] at (5.1,2.0) {iyot çözeltisi\\\\(sarı-kahverengi)};',
   '\\draw['+OKU+',line width=.8pt] (5.1,0.9)--(3.4,1.0);\\node[font=\\small,anchor=west] at (5.1,0.85) {selofan zar};']
SK7=tk('\n'.join(b),.95)
q('0007','deney',[A('Düzeneği kavra','Kese nişasta ve glikoz çözeltisiyle doludur; beherde iyot çözeltisi vardır. Selofan küçük molekülleri geçirir.','Geçebilir: iyot, glikoz · Geçemez: nişasta'),
   adim_onc(d7,'I'),adim_onc(d7,'II'),adim_onc(d7,'III'),sonuc(r,True)],
 'selofan kese, nişasta+glikoz içeride, iyot dışarıda',z='orta',alt='Madde Geçişi Deneyi',kaz='Selofan kese deneyinde renk değişimi ve Benedict sonucundan hangi maddelerin zardan geçtiğini çıkarır.',kalip='öncüllü',
 metin='Nişasta ve glikoz içeren çözeltiyle doldurulmuş selofan kese, şekildeki gibi iyot çözeltisi bulunan bir behere batırılıyor. Yarım saat sonra kesenin içindeki çözeltinin mavi-siyah renk aldığı, beherdeki çözeltinin sarı-kahverengi kaldığı görülüyor. Beherden alınan örneğe Benedict çözeltisi eklenip ısıtılınca tuğla kırmızısı çökelti oluşuyor.\nBuna göre,\nI. İyot molekülleri selofan zardan geçmiştir.\nII. Nişasta molekülleri selofan zardan geçememiştir.\nIII. Glikoz molekülleri selofan zardan geçememiştir.\nyargılarından hangileri doğrudur?',
 sekil=SK7,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',
 ip=['Her ayıracın hangi maddeyle hangi renk verdiğini ve bu rengin kesenin içinde mi dışında mı oluştuğunu düşün.'],
 bilgi=[B('Ayıraçlar','İyot nişastayla birleşince mavi-siyah renk verir · Benedict çözeltisi glikozlu ortamda ısıtılınca tuğla kırmızısı çökelti oluşturur · Selofan küçük molekülleri geçirir, büyük molekülleri tutar')],
 puf='Ayıracın rengi nerede oluştuysa, o ayıracın ve ilgili maddenin orada bulunduğunu gösterir: hangi madde zardan geçmiştir, buna göre kurgula.')

# ============ 0008 · kontraktil koful bar grafiği · orta · öncüllü ============
kartla('08','ozmoz','Kontraktil koful – dış ortam derişimi','Tatlı su protistlerinde hücre içi derişim ortamdan yüksektir; ozmozla giren fazla su kontraktil kofulla atılır. Ortamın derişimi artınca giren su azalır, atım sayısı düşer; eşit derişimde koful çalışmaz.','Atım sayısı azalınca suyun hücreden çıktığını sanmak; kontraktil kofulu depolama organeli sanmak.','orta','öncüllü',4)
TUZ=[0,0.3,0.6,0.9]; ATIM=[12,8,4,0]
assert all(ATIM[i]>ATIM[i+1] for i in range(3)) and ATIM[-1]==0
d8={'I':(True,'Ortamın derişimi arttıkça hücre içi ile ortam arasındaki derişim farkı azalır; ozmozla giren su azalır ve kofulun atım sayısı düşer.'),
    'II':(False,'%0,9’luk ortamda koful hiç çalışmamıştır ve hücre hacmi sabittir; net su girişi yoktur. Bu, hücre özsuyu derişiminin ortama eşit olduğunu gösterir, ortamdan yüksek olduğunu değil.'),
    'III':(True,'Kontraktil koful, ozmozla hücreye giren fazla suyu hücre dışına atar ve hücrenin su dengesini korur.')}
r=onc(d8,True,'C')
b=['\\begin{axis}[ybar,width=7.8cm,height=5.4cm,xmin=-0.2,xmax=1.1,xtick={0,0.3,0.6,0.9},ymin=0,ymax=15,ytick={0,4,8,12},xlabel={Ortamdaki tuz derişimi (\\%)},ylabel={Atım sayısı (dk$^{-1}$)},bar width=22pt,nodes near coords,every node near coord/.append style={font=\\small,text=black},'+AX.replace('every axis plot/.append style={line width=1.5pt}','every axis plot/.append style={fill=vurgu!35,draw=black,line width=1pt}')+']',
   '\\addplot[fill=vurgu!35,draw=black,line width=1pt] coordinates {'+' '.join(f'({t},{a})' for t,a in zip(['0','0.3','0.6','0.9'],ATIM))+'};','\\end{axis}']
SK8=tk('\n'.join(b),1.0)
q('0008','ozmoz',[A('Grafiği oku','Tuz derişimi arttıkça kontraktil kofulun dakikadaki atım sayısı 12’den 0’a düşer.','12 → 8 → 4 → 0'),
   adim_onc(d8,'I'),adim_onc(d8,'II'),adim_onc(d8,'III'),sonuc(r,True)],
 'tatlı su protisti, kontraktil koful atım sayısı',z='orta',alt='Organel İşlevi ve Ozmoz',kaz='Kontraktil koful atım grafiğinden ortam derişimi, ozmoz ve organel işlevini ilişkilendirir.',kalip='öncüllü',
 metin='Tatlı suda yaşayan tek hücreli bir canlı, farklı tuz derişimlerine sahip ortamlara aktarılıyor ve kontraktil kofulunun dakikadaki atım sayısı ölçülüyor. Sonuçlar grafikte verilmiştir. %0,9’luk tuz çözeltisinde kofulun hiç boşalmadığı ve hücre hacminin değişmediği görülmüştür.\nBuna göre,\nI. Ortamın tuz derişimi arttıkça hücreye ozmozla giren su miktarı azalmıştır.\nII. %0,9’luk ortamda hücrenin özsuyu derişimi ortamdan daha yüksektir.\nIII. Kontraktil koful, hücreye giren fazla suyun dışarı atılmasını sağlar.\nyargılarından hangileri doğrudur?',
 sekil=SK8,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',
 ip=['Grafikte tuz derişimi arttıkça atım sayısının nasıl değiştiğini, kofulun çalışmadığı ortamda hücre hacminin neden sabit kaldığını düşün.'],
 bilgi=[B('Kontraktil koful','Tatlı su protistlerinde bulunan, hücreye ozmozla giren fazla suyu toplayıp dışarı atan organeldir · Ortamla hücre özsuyu arasındaki derişim farkı arttıkça ozmozla giren su artar')],
 puf='Koful çalışmıyorsa net su girişi yok demektir; bu da hücre ile ortamın derişiminin eşit olduğunu gösterir.')

# ============ 0009 · radyoaktif timin · kolay · olumsuz ============
kartla('09','organel','İşaretli timin – DNA içeren yapılar','Timin yalnız DNA’da bulunan bir bazdır; DNA çekirdekte (kromozom), mitokondride ve kloroplastta bulunur. RNA ve protein içeren, DNA içermeyen yapılar (ribozom) timin almaz.','Ribozomu da DNA taşıyor sanmak; mitokondri ve kloroplastın DNA’sını unutmak.','kolay','hikâyeli',3)
S9=['Ribozom','Çekirdek','Mitokondri','Kloroplast','Kromozom']
q('0009','organel',[A('Timinin yerini bul','Timin, DNA nükleotitlerinde bulunur; hücre bölünürken DNA eşlenir ve işaretli nükleotit bu DNA’ya katılır.','Timin → DNA'),
   A('DNA içeren yapıları say','Bitki hücresinde DNA çekirdekte (kromozomlar), mitokondride ve kloroplastta bulunur.','Çekirdek, kromozom, mitokondri, kloroplast'),
   A('DNA içermeyeni seç','Ribozom rRNA ve proteinden oluşur; DNA içermez.','Ribozom: timin yok')],
 'bölünen bitki hücreleri, radyoaktif timin',z='kolay',alt='Organeller',kaz='DNA içeren ve içermeyen hücre yapılarını ayırt eder.',kalip='hikâyeli',
 metin='Bir araştırmacı, bölünebilen bitki hücrelerinin yetiştirildiği besi ortamına radyoaktif işaretli timin nükleotiti ekliyor. Hücreler birkaç kez bölündükten sonra hücrelerden bazı yapılar ayrılıyor ve bu yapılarda radyoaktivite ölçülüyor.\nBuna göre, aşağıdaki yapılardan hangisinde radyoaktivite beklenemez?',
 dogru=S9[0],sira=yer('A',S9[0],S9[1:]),
 yan=[(S9[1],'Çekirdekte DNA vardır; bölünme sırasında eşlenen DNA işaretli timin içerir. Radyoaktivite beklenir.','bilgi'),
      (S9[2],'Mitokondri kendi DNA’sını taşır ve eşler; işaretli timin bu DNA’ya katılır.','bilgi'),
      (S9[3],'Kloroplast da kendi DNA’sını taşır; işaretli timin bu DNA’ya katılabilir.','bilgi'),
      (S9[4],'Kromozomlar DNA ve proteinden oluşur; işaretli timin kromozomdaki DNA’da bulunur.','dikkat')],
 istenen='Radyoaktivite beklenmeyen yapı.',
 ip=['Hücre bölünürken hangi molekülün eşlendiğini ve bu yapının hücrenin neresinde bulunduğunu düşün.'],
 bilgi=[B('Nükleik asitler','DNA nükleotitlerinin bazları adenin, guanin, sitozin ve timindir')],
 puf='Timin = DNA; DNA’sı olmayan yapıda timin bulunmaz.')

# ============ 0010 · hacim–zaman grafiği (3 çözelti) · zor ============
kartla('10','ozmoz','Hayvan hücresi – ardışık çözeltilerde hacim','Hayvan hücresinde çözünen madde miktarı sabitken hücre hacmi derişimle ters orantılıdır: denge hacminden çözelti derişimleri oranlanır. Hacim artıyorsa çözelti, öncekinden seyreltiktir.','Oranı ters kurmak; bir önceki yerine ilk çözeltiye göre karşılaştırmak; hacim farkını oran sanmak.','zor','grafik',5)
V=[100,200,50]; T0=[0,10,30]; TS=[10,30,50]
assert F(V[0],V[1])==F(1,2) and F(V[0],V[2])==2 and F(V[1],V[2])==4
def hacim(t):
    if t<10: return V[0]
    if t<30: return V[1]+(V[0]-V[1])*math.exp(-(t-10)/2.2)
    return V[2]+(V[1]-V[2])*math.exp(-(t-30)/2.2)
assert abs(hacim(29.99)-200)<1 and abs(hacim(49.9)-50)<1
ch=' '.join(f'({t/2:.1f},{hacim(t/2):.1f})' for t in range(0,101))
b=['\\begin{axis}[width=7.8cm,height=5.4cm,xmin=0,xmax=50,ymin=0,ymax=230,xtick={0,10,20,30,40,50},ytick={0,50,100,150,200},xlabel={Zaman (dk)},ylabel={Hücre hacmi (birim)},'+AX+']',
   f'\\addplot[black] coordinates {{{ch}}};',
   '\\draw[dotted,line width=.9pt] (axis cs:10,0)--(axis cs:10,225);\\draw[dotted,line width=.9pt] (axis cs:30,0)--(axis cs:30,225);',
   '\\node[font=\\small\\bfseries] at (axis cs:5,218) {K};\\node[font=\\small\\bfseries] at (axis cs:20,218) {L};\\node[font=\\small\\bfseries] at (axis cs:40,218) {M};','\\end{axis}']
SK10=tk('\n'.join(b),1.0)
dg,yn,sr=kesirler(F(4),[(F(1,4),'Oranı ters kurmuş: L çözeltisinin derişiminin M çözeltisinin derişimine oranını (1/4) vermiş.','dikkat'),
  (F(2),'M çözeltisini L ile değil ilk (K) çözeltiyle karşılaştırmış: hacim 100’den 50’ye indiği için derişim 2 katına çıkmıştır; istenen L’ye göre karşılaştırmadır.','dikkat'),
  (F(3),'Hacim farkını (200 − 50 = 150) M’nin hacmine (50) bölmüş; derişim hacimle ters orantılıdır, fark değil oran alınır.','islem'),
  (F(1,2),'L’yi K’ye göre değerlendirmiş: hacim iki katına çıktığı için L çözeltisinin derişimi K’nin 1/2’sidir; istenen M ile L karşılaştırmasıdır.','dikkat')])
q('0010','ozmoz',[A('Ters orantıyı kur','Hücredeki çözünen madde miktarı sabit, hacim dengede olduğundan hücre içi derişim = çözelti derişimi ve derişim ∝ 1/hacim.','Derişim × hacim = sabit'),
   A('L çözeltisini K ile karşılaştır','Hacim 100’den 200’e çıkmıştır; derişim yarıya inmiştir.','L = K/2'),
   A('M çözeltisini K ile karşılaştır','Hacim 100’den 50’ye inmiştir; derişim iki katına çıkmıştır.','M = 2K'),
   A('M ve L’yi oranla','K cinsinden yazılan değerler oranlanır.','M / L = 2K / (K/2)'),
   A('Sonucu yaz','Oran 4’tür.','M, L’nin 4 katıdır')],
 'hayvan hücresi, K → L → M çözeltileri',z='zor',alt='Ozmoz',kaz='Hacim–zaman grafiğinden ardışık çözeltilerin derişim oranını hesaplar.',kalip='grafik',
 metin='Bir hayvan hücresi önce K çözeltisinde bekletiliyor; 10. dakikada L, 30. dakikada M çözeltisine aktarılıyor. Hücre hacminin zamanla değişimi grafikte gösterilmiştir. Çözünen maddeler zardan geçmemekte, hacim yalnızca su alışverişiyle değişmekte ve hücre her çözeltide dengeye ulaşmaktadır. Hücre içi derişim hücre hacmiyle ters orantılıdır.\nBuna göre, M çözeltisinin derişimi L çözeltisinin derişiminin kaç katıdır?',
 sekil=SK10,dogru=dg,yan=yn,sira=sr,istenen='M çözeltisinin derişiminin L çözeltisininkine oranı.',
 ip=['Her denge hacminde hücre içi derişimin çözelti derişimine eşit olduğunu kullan ve hacimle derişimin ters orantılı olduğunu yaz.'],
 bilgi=[B('Hayvan hücresinde ozmoz','Hayvan hücresinde hücre çeperi yoktur; hacim su alışverişiyle değişir · Hipotonik ortamda hücre su alıp şişer, hipertonik ortamda su kaybedip büzüşür')],
 puf='Hücredeki çözünen sabitse hacim × derişim sabittir; derişim oranı hacim oranının tersidir.')

bitir(P,'hucreuc',UK)
