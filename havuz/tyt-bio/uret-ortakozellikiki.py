"""TYT Biyoloji · Canlıların Ortak Özellikleri · ek paket (ortakozellikiki): 18 soru, kardeş yok, ipucu 1.
Grafik/tablo verileri, deney düzeneği karşılaştırmaları ve öncül doğrulukları Python'da tek yerde tanımlanır;
şekiller TikZ/pgfplots ile bu değerlerden çizilir; anahtar, adım ve çeldirici açıklamaları aynı veriden üretilir."""
import sys,os,json,math
BD=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,BD)
import _hafif_bio as H
from _hafif_bio import *
KONU_='Canlıların Ortak Özellikleri'; UK='bio|Canlıların Ortak Özellikleri'
H.KONU=KONU_
P=Parti('ortakozellikiki',KONU_,UK,ders='TYT Biyoloji',idon='tytbio')
KY='ÖSYM 2018–2026 TYT Biyoloji dağılımı (yalnız mantık) · MEB 9. sınıf Biyolojinin Doğası ve Canlıların Ortak Özellikleri'
TIPK={}
def kartla(n,alt,fikir,tuzak,z,kalip,adim,tipId,tip):
    kart(f'K-BYOO2-{n}',alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY); TIPK[n]=(tipId,tip)
def q(no,ad,**k):
    n=no[-2:]; tipId,tip=TIPK[n]; ne=k.pop('ne'); ozet=k.pop('ozet')
    mk(P,no,ad=ad,adim=len(ad),tipId=tipId,tip=tip,kart=f'K-BYOO2-{n} ({ozet}) · {ne}',**k)
def yer(harf,dogru,yanlar):
    sira=[None]*5; sira['ABCDE'.index(harf)]=dogru; it=iter(yanlar)
    for i in range(5):
        if sira[i] is None: sira[i]=next(it)
    assert sorted(sira)==sorted([dogru]+list(yanlar)) and len(set(sira))==5; return sira
def tk(body,scale=1.0): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small,scale=%s]\n%s\n\\end{tikzpicture}'%(scale,body))
def ax(body,w,h,xmin,xmax,ymin,ymax,xt,yt,xl,yl,extra=''):
    return tikz_svg('\\begin{tikzpicture}[font=\\small]\n\\begin{axis}[width=%scm,height=%scm,xmin=%s,xmax=%s,ymin=%s,ymax=%s,xtick={%s},ytick={%s},axis lines=left,'
      'xlabel={%s},ylabel={%s},tick label style={font=\\footnotesize},label style={font=\\small},ymajorgrids=true,grid style={dashed,black!25},%s]\n%s\n\\end{axis}\n\\end{tikzpicture}'%(w,h,xmin,xmax,ymin,ymax,xt,yt,xl,yl,extra,body))
ORD=['I','II','III']
def adS(s): return ('Yalnız '+s[0]) if len(s)==1 else (' ve '.join(s) if len(s)==2 else ', '.join(s[:-1])+' ve '+s[-1])
def onc(d,ops,olumsuz=False):
    """d: {'I':(bool,doğru bilgi cümlesi)}; olumsuz=True: anahtar yanlış öncüllerin kümesi."""
    T=frozenset(k for k,v in d.items() if v[0]!=olumsuz)
    ops=[tuple(o) for o in ops]; assert len(ops)==5 and len(set(ops))==5
    eş=[o for o in ops if frozenset(o)==T]; assert len(eş)==1,(T,ops)
    yan=[]
    for o in ops:
        W=frozenset(o)
        if W==T: continue
        p=[]
        for x in sorted(W-T,key=ORD.index):
            p.append(f'{x} öncülünü '+('yanlış' if olumsuz else 'doğru')+' sanmış; oysa '+('doğrudur: ' if olumsuz else 'yanlıştır: ')+d[x][1] if True else '')
        for x in sorted(T-W,key=ORD.index):
            p.append(f'{x} öncülünü '+('doğru' if olumsuz else 'yanlış')+' sanmış; oysa '+('yanlıştır: ' if olumsuz else 'doğrudur: ')+d[x][1])
        yan.append((adS(o),' '.join(p),'bilgi'))
    return dict(dogru=adS(eş[0]),yan=yan,sira=[adS(o) for o in ops])
def oad(d,olumsuz=False):
    s=[A(f'{k}. öncülü değerlendir',v[1],f'{k}: '+('doğru' if v[0] else 'yanlış')) for k,v in d.items()]
    T=[k for k,v in d.items() if v[0]!=olumsuz]
    s.append(A('Sonucu yaz','İstenen türdeki öncüller bir arada yazılır.',('Yanlış olanlar: ' if olumsuz else 'Doğru olanlar: ')+adS(T)))
    return s
def tek(sec,hedef,tur='bilgi'):
    """sec: [(metin,bool,açıklama)]; hedef True: tek doğru, False: tek yanlış aranır. Açıklama o ifadenin gerçek değerini söyler."""
    assert len(sec)==5; h=[s for s in sec if s[1]==hedef]; assert len(h)==1,[s[0] for s in h]
    yan=[]
    for m,b,n in sec:
        if b==hedef: continue
        yan.append((m,('Bu ifadeyi doğru sanmış; oysa yanlıştır: ' if hedef else 'Bu ifadeyi yanlış sanmış; oysa doğrudur: ')+n,tur))
    return h[0][0],yan
def harf(sira,d): return 'ABCDE'[sira.index(d)]

# =================== bilgi kutuları ===================
YON=B('Bilimsel yöntemin basamakları','gözlem → problem → hipotez (sınanabilir tahmin) → kontrollü deney → veri toplama ve yorumlama → sonuç; sonuç hipotezi destekler ya da desteklemez · Örnek: “Yağmurlu günlerde salyangozlar daha çok görülüyor” bir gözlemdir')
DEG=B('Deneyde değişkenler','bağımsız değişken: araştırmacının değiştirdiği etken · bağımlı değişken: ölçülen sonuç · kontrol (sabit) değişkenler: bütün gruplarda eşit tutulan koşullar · kontrol grubu: denenen etkenin uygulanmadığı gruptur')
TEO=B('Hipotez, teori ve kanun','hipotez: sınanabilen geçici açıklama · teori: gözlem ve deneylerle desteklenmiş açıklama · kanun: doğada gözlenen düzenlilik')
OZ=B('Canlıların ortak özellikleri','hücresel yapı · beslenme · solunum · boşaltım · metabolizma · homeostazi · uyarılara tepki · hareket · büyüme ve gelişme · üreme · uyum (adaptasyon) · Örnek: balığın yüzgeçleriyle suda hareket etmesi hareket özelliğidir')
BES=B('Beslenme çeşitleri','ototrof: inorganik maddelerden organik madde sentezler (fotosentez, kemosentez) · heterotrof: organik besini dışarıdan hazır alır · Örnek: yosun ototrof, tavşan heterotroftur')
MET=B('Metabolizma','anabolizma: küçük moleküllerden büyük molekül sentezi, enerji harcanır · katabolizma: büyük molekülün yıkılması, enerji açığa çıkar · Örnek: nişastanın glikoza yıkılması katabolizmadır')
HOM=B('Homeostazi, tepki ve uyum','homeostazi: iç ortamın uygun sınırlar içinde tutulması (kısa sürede, fizyolojik) · uyarılara tepki: dış ya da iç etkiye karşılık verme · adaptasyon: popülasyonun uzun sürede kazandığı kalıtsal uyum')
EVR=B('Doğal seçilim ve adaptasyon','popülasyonda zaten bulunan farklı özellikler arasından ortama uygun olanlar daha çok hayatta kalıp çoğalır; böylece özellik sonraki nesillerde yaygınlaşır · Bireyin yaşamı boyunca kazandığı özellikler döl yoluyla aktarılmaz')
VIR=B('Virüslerin canlılık durumu','virüsler hücresel yapıda değildir ve canlıların ortak özelliklerinin yalnız bir kısmını gösterir · Örnek: bakteriler hücresel yapıdadır')
ENZ=B('Enzimler ve sıcaklık','metabolizmayı yürüten enzimlerin etkinliği sıcaklığa duyarlıdır; optimum sıcaklıkta en yüksektir ve çok yüksek sıcaklıkta enzimlerin yapısı bozulur')
CAN=B('Canlı ve cansız ayrımı','canlılar hücresel yapıdadır, metabolizma yapar, iç ortamını korur, uyarılara tepki verir, üreyip büyür ve gelişir · Cansızlar bu özelliklerin hiçbirini göstermez · Örnek: taş ve buz kristali cansız; mantar canlıdır')

# =================== 01 · hipotez basamağı · kolay ===================
kartla('01','Bilimsel yöntem basamakları','Verilen ifadenin bilimsel yöntemin hangi basamağı olduğunu belirlemek; sınanmamış tahmin hipotezdir.','Tahmini gözlem ya da sonuçla karıştırmak.','kolay','düz',3,'by-oo2-yontem','Bilimsel yöntem ve bilimsel bilgi')
H01='Hipotez'
q('0001',[A('İfadeyi çöz','Araştırmacı balık sayısının azalmasını tahmini bir nedenle açıklıyor; bu tahmini henüz sınamamış.','sınanmamış tahmin'),
 A('Basamakları ele','Gözlem, olayı fark etmektir; deney ve sonuç sınama sonrasındadır; teori çok sayıda deneyle desteklenmiş bilgidir.','4 basamak uymuyor'),
 A('Sonucu yaz','Sınanabilir geçici açıklama hipotezdir.','Hipotez')],
 z='kolay',alt='Bilimsel yöntem',kaz='Verilen ifadeyi bilimsel yöntemin basamaklarından biriyle eşleştirir.',kalip='düz',ozet='hipotez basamağı',ne='göl ve fabrika atığı',
 metin='Bir gölde yaşayan balıkların sayısının son iki yılda belirgin biçimde azaldığını gözlemleyen bir araştırmacı, azalmanın nedenini şöyle tahmin etmiştir: “Göle karışan fabrika atıkları balıkların üremesini engelliyor olabilir.” Araştırmacı bu tahminini sınamak için henüz herhangi bir deney yapmamıştır.\nBuna göre araştırmacının bu tahmini, bilimsel yöntemin aşağıdaki basamaklarından hangisine karşılık gelir?',
 dogru='Hipotez',sira=['Gözlem','Kontrollü deney','Hipotez','Sonuç','Teori'],
 yan=[('Gözlem','Balık sayısının azaldığını fark etmek gözlemdir; nedeni tahmin eden ifade ise gözlem değildir.','bilgi'),
      ('Kontrollü deney','Araştırmacı henüz deney yapmamıştır; tahmin deneyin kendisi değil, deneyle sınanacak düşüncedir.','dikkat'),
      ('Sonuç','Sonuç, deney verileri yorumlandıktan sonra yazılır; burada henüz veri yoktur.','bilgi'),
      ('Teori','Teori çok sayıda gözlem ve deneyle desteklenmiş açıklamadır; sınanmamış bir tahmin teori olamaz.','bilgi')],
 istenen='Tahmin ifadesinin bilimsel yöntemdeki basamağı.',ip=['İfade deneyle sınanmış mı, yoksa sınanmayı bekleyen bir açıklama mı?'],bilgi=[YON,TEO],
 puf='Sınanmamış, deneyle sınanabilir tahmin hipotezdir; nedeni açıklayan ama kanıtlanmamış cümleyi arıyorsan hipotez de.')

# =================== 02 · canlı–cansız tablosu · kolay ===================
kartla('02','Canlı–cansız ayrımı tablosu','Tabloda her özelliği taşıyan madde canlı, hiçbirini taşımayan madde cansızdır.','Hücresel yapıyı tek ölçüt sanmak ya da tabloya dayanmadan yorum yapmak.','kolay','tablo',3,'by-oo2-canli','Canlı–cansız ayrımı ve virüsler')
T02=[['Hücresel yapı','Var','Yok','Var'],['Metabolizma','Var','Yok','Var'],['İç dengeyi koruma','Var','Yok','Var'],['Uyarılara tepki','Var','Yok','Var'],['Üreme','Var','Yok','Var']]
S02=tablo_svg(['Özellik','Madde X','Madde Y','Madde Z'],T02)
dog2='X ve Z canlı, Y cansızdır.'
q('0002',[A('Tabloyu oku','X ve Z’de bütün özellikler var; Y’de hiçbiri yok.','X, Z: 5/5 · Y: 0/5'),
 A('Ölçütü uygula','Canlı, hücresel yapı, metabolizma, iç dengeyi koruma, tepki ve üremeyi birlikte gösterir; cansız bunları göstermez.','X ve Z canlı; Y cansız'),
 A('Sonucu yaz','Doğru ifade X ve Z’yi canlı, Y’yi cansız sayan ifadedir.',dog2)],
 z='kolay',alt='Canlı–cansız ayrımı',kaz='Tablodaki canlılık özelliklerinden maddelerin canlı ya da cansız olduğunu çıkarır.',kalip='tablo',ozet='canlı–cansız tablosu',ne='X, Y, Z maddeleri',sekil=S02,
 metin='Bir öğrenci, laboratuvarda incelediği X, Y ve Z maddelerinde bazı canlılık özelliklerini araştırmış ve bulduğu sonuçları tabloda göstermiştir.\nBuna göre bu maddelerle ilgili aşağıdakilerden hangisi söylenebilir?',
 dogru=dog2,sira=yer('A',dog2,['Yalnız X canlıdır; Z’nin özellikleri canlı olması için yeterli değildir.','Y, hiçbir özellik göstermemesine rağmen canlıdır.','X, Y ve Z’nin üçü de canlıdır.','Y canlı, X ve Z cansızdır.']),
 yan=[('Yalnız X canlıdır; Z’nin özellikleri canlı olması için yeterli değildir.','Z’de X’teki bütün özellikler var; X canlıysa Z de canlıdır.','dikkat'),
      ('Y, hiçbir özellik göstermemesine rağmen canlıdır.','Canlılık özelliklerinden hiçbirini göstermeyen madde cansızdır.','bilgi'),
      ('X, Y ve Z’nin üçü de canlıdır.','Y tabloda hiçbir canlılık özelliği göstermemiştir; bu yüzden canlı değildir.','dikkat'),
      ('Y canlı, X ve Z cansızdır.','Canlı–cansız ayrımını ters kurmuş; özellikleri gösteren X ve Z canlıdır.','bilgi')],
 istenen='Tabloya göre maddelerin canlı ya da cansız olması.',ip=['Her sütunda kaç özelliğin “Var” yazdığına bak.'],bilgi=[CAN],
 puf='Tabloda canlılık özelliklerinin hepsi varsa canlı, hiçbiri yoksa cansızdır; sütunu özellik özellik oku.')

# =================== 03 · saksı deneyi · orta ===================
kartla('03','Gübre deneyi: değişken ve kontrol grubu','Saksı düzeneğinde yalnız gübre farklıdır; bağımsız, bağımlı, sabit değişken ve kontrol grubu ayrılır; deneyin başında sonuç kesin bilinmez.','Sonucu deney bitmeden kesinmiş gibi söylemek.','orta','şekilli',4,'by-oo2-deney','Deney düzeneği, değişkenler ve kontrol grubu')
G03=[0,5,10]
def pot(x0,n,etiket,alt):
    b=f'\\draw[line width=1.3pt] ({x0+.25},0)--({x0+1.75},0)--({x0+2},1.3)--({x0},1.3)--cycle;'
    b+=f'\\draw[line width=1.3pt] ({x0-.08},1.3)--({x0+2.08},1.3)--({x0+2.08},1.5)--({x0-.08},1.5)--cycle;'
    b+=f'\\draw[line width=1.5pt] ({x0+1},1.5)--({x0+1},2.9);'
    b+=f'\\draw[fill=vurgu!15,line width=1pt] ({x0+1},2.3) ellipse (.5 and .2); \\draw[fill=vurgu!15,line width=1pt] ({x0+1},2.7) ellipse (.5 and .2);'
    pts=[(.55,.35),(1.0,.5),(1.45,.35),(.7,.85),(1.3,.8),(.4,1.05),(1.0,1.05),(1.6,1.05),(.85,.2),(1.2,.2)]
    for i in range(n): b+=f'\\fill ({x0+pts[i][0]:.2f},{pts[i][1]:.2f}) circle (.07);'
    b+=f'\\node[font=\\normalsize\\bfseries] at ({x0+1},3.55) {{{etiket}}};\\node[font=\\small] at ({x0+1},-.5) {{{alt}}};'
    return b
SK3=tk('\n'.join(pot(i*3.0,n,e,f'Gübre: {n} g') for i,(n,e) in enumerate(zip(G03,ORD))),.95)
assert G03[0]==0
sec3=[('Kontrol grubu I numaralı saksıdır.',True,'Gübre eklenmeyen I numaralı saksı kontrol grubudur.'),
      ('Bağımsız değişken gübre miktarıdır.',True,'Araştırmacının değiştirdiği etken gübre miktarıdır.'),
      ('Bağımlı değişken fidelerin boy uzamasıdır.',True,'Ay sonunda ölçülecek sonuç boy uzamasıdır.'),
      ('Sulama miktarı ve ışık koşulları sabit tutulan değişkenlerdendir.',True,'Hepsi 20 mL su almış ve aynı pencerede bekletilmiştir.'),
      ('Deney bitmeden, gübre miktarı arttıkça boy uzamasının arttığı kesin olarak söylenebilir.',False,'Sonuçlar ölçülmeden etkinin yönü kesin bilinemez; bu bir hipotezdir.')]
d3,y3=tek(sec3,False)
q('0003',[A('Değişkenleri belirle','Yalnız gübre miktarı farklıdır: bağımsız değişken gübre; ölçülecek sonuç boy uzaması, yani bağımlı değişkendir.','bağımsız: gübre · bağımlı: boy'),
 A('Sabit koşulları bul','Fide türü, toprak miktarı, su ve ışık bütün saksılarda eşittir.','sabit: tür, toprak, su, ışık'),
 A('Kontrol grubunu bul','Denenen etkenin (gübre) uygulanmadığı saksı kontrol grubudur.','Kontrol: 0 g gübreli saksı'),
 A('Yanlış ifadeyi seç','Sonuç ölçülmeden etki kesinmiş gibi söylenemez; ifade yalnız bir tahmindir.','Yanlış ifade: kesin sonuç iddiası')],
 z='orta',alt='Deney düzeneği',kaz='Deney düzeneğinde bağımsız, bağımlı, sabit değişkeni ve kontrol grubunu ayırt eder.',kalip='şekilli',ozet='saksı düzeneği',ne='gübre miktarına göre üç saksı',sekil=SK3,
 metin='Bir öğrenci, gübrenin fidelerin boy uzamasına etkisini araştırmak için aynı türden, aynı yaşta ve aynı boydaki fideleri eşit miktarda toprak içeren üç saksıya dikmiştir. Saksılara şekilde gösterilen miktarlarda gübre eklemiş, her saksıyı günde 20 mL su ile sulamış ve hepsini aynı pencere önünde bir ay bekletmiştir. Ay sonunda fidelerin boylarını ölçecektir.\nBuna göre bu deneyle ilgili aşağıdakilerden hangisi söylenemez?',
 dogru=d3,sira=[s[0] for s in sec3],yan=y3,istenen='Deney düzeneğine göre doğru olmayan ifade.',
 ip=['Her ifadenin deney düzeneğinden doğrudan okunup okunmadığına bak.'],bilgi=[DEG],
 puf='Deney bitmeden sonuç kesinleşmez; kontrol grubu etken uygulanmayan gruptur, geri kalan koşullar eşit tutulur.')

# =================== 04 · boşaltım · kolay ===================
kartla('04','Ortak özellik: boşaltım örneği','Metabolizma atıklarının hücreden uzaklaştırılması boşaltımdır.','Boşaltımı solunum ya da homeostazi ile karıştırmak.','kolay','düz',3,'by-oo2-ozellik','Ortak özelliklerin tanınması')
d4='Boşaltım'
q('0004',[A('Olayı çöz','Kas hücresinde besinlerin yıkımıyla oluşan atıklar hücrenin dışına verilir.','atık → hücre dışı'),
 A('Özelliği eşleştir','Metabolizma atıklarının vücuttan uzaklaştırılması boşaltımdır.','boşaltım'),
 A('Diğerlerini ele','Üreme, büyüme, adaptasyon ve tepki verme atık uzaklaştırmayı anlatmaz.','4 özellik elenir')],
 z='kolay',alt='Ortak özellikler',kaz='Metabolizma atıklarının atılmasını boşaltım olarak tanır.',kalip='düz',ozet='atık maddelerin atılması',ne='kas hücresi',
 metin='Bir kas hücresinde besinlerin yıkılmasıyla oluşan karbondioksit ve diğer atık maddeler, hücre zarından geçerek hücre dışına verilir. Bu atıklar hücrede birikirse hücrenin faaliyetleri olumsuz etkilenir.\nBuna göre bu olay canlıların aşağıdaki ortak özelliklerinden hangisine örnektir?',
 dogru=d4,sira=yer('B',d4,['Üreme','Büyüme ve gelişme','Adaptasyon','Uyarılara tepki verme']),
 yan=[('Üreme','Olayda yeni birey ya da hücre oluşmuyor; atık verilmesi çoğalma değildir.','bilgi'),
      ('Büyüme ve gelişme','Olayda boy ya da kütle artışı yok; atıkların atılması büyüme sayılmaz.','bilgi'),
      ('Adaptasyon','Adaptasyon uzun sürede kazanılan kalıtsal uyumdur; atık atma her hücrede süren bir olaydır.','bilgi'),
      ('Uyarılara tepki verme','Olayda dışarıdan gelen bir uyarıya karşılık verme yok; atıklar metabolizmanın doğal sonucudur.','bilgi')],
 istenen='Olayın karşılık geldiği ortak özellik.',ip=['Hücrenin metabolizma sonucu oluşan maddelerle ne yapması gerekir?'],bilgi=[OZ],
 puf='Metabolizma atığının hücre ya da vücuttan uzaklaştırılması boşaltımdır.')

# =================== 05 · tuz deneyi · orta · öncüllü + grafik ===================
kartla('05','Tuz deneyi: çimlenme grafiği','Sütun grafiğinden kontrol grubu, bağımlı değişken ve etki yorumu öncüllerle sınanır.','Azalmayı etkinin olmadığı sanmak; bağımlı ile bağımsız değişkeni karıştırmak.','orta','öncüllü',4,'by-oo2-sonuc','Deney sonuçlarını yorumlama')
TZ=[0,1,3,6]; CIM=[46,44,31,9]
assert all(CIM[i]>CIM[i+1] for i in range(3)) and CIM[0]>=45
G5=['K','A','B','C']
bars='\\addplot[ybar,bar width=20pt,fill=vurgu!25,draw=black,line width=1pt] coordinates {'+' '.join(f'({g},{c})' for g,c in zip(G5,CIM))+'};'
SK5=ax(bars,6.6,5.0,'','',0,55,'','0,10,20,30,40,50','Grup (tuz: K 0 g, A 1 g, B 3 g, C 6 g)','Çimlenen tohum sayısı','symbolic x coords={K,A,B,C},xtick=data,enlarge x limits=.18,nodes near coords,every node near coord/.append style={font=\\footnotesize}')
d5={'I':(True,'K grubuna tuz eklenmemiştir; denenen etkenin uygulanmadığı grup kontrol grubudur.'),
    'II':(False,'6 g tuzlu grupta çimlenmenin 46’dan 9’a düşmesi tuzun çimlenmeyi etkilediğini gösterir; etkisiz olduğunu değil.'),
    'III':(True,'Ölçülen sonuç çimlenen tohum sayısıdır; bağımlı değişken odur.')}
assert CIM[0]>CIM[3]
r5=onc(d5,[('I',),('I','II'),('I','III'),('II','III'),('I','II','III')])
q('0005',oad(d5),
 z='orta',alt='Deney sonuçları',kaz='Sütun grafiğiyle verilen deneyde kontrol grubunu, bağımlı değişkeni ve etkiyi yorumlar.',kalip='öncüllü',ozet='tuz ve çimlenme',ne='sütun grafiği',sekil=SK5,
 metin='Bir araştırmacı, tuzun tohumların çimlenmesine etkisini incelemek için aynı türden 50’şer tohumu aynı sıcaklıkta, eşit miktarda su içeren dört kapta çimlendirmiştir. Kaplara eklenen tuz miktarı grafikte belirtilmiştir. Sonuçlar bir hafta sonra grafikte gösterilmiştir.\nBuna göre,\nI. K grubu kontrol grubudur.\nII. 6 g tuzlu ortamda çimlenmenin azalması, tuzun çimlenmeyi etkilemediğini gösterir.\nIII. Deneyde bağımlı değişken çimlenen tohum sayısıdır.\nifadelerinden hangileri doğrudur?',
 dogru=r5['dogru'],sira=r5['sira'],yan=r5['yan'],istenen='Doğru olan öncüller.',
 ip=['Her öncülde sorulan kavramı (kontrol grubu, bağımlı değişken) ayrı ayrı tanımla.'],bilgi=[DEG],
 puf='Kontrol grubu etken uygulanmayan gruptur; ölçülen sonuç bağımlı değişkendir; sonuçta fark varsa etken etkilidir.')

# =================== 06 · teori–kanun · orta · öncüllü · olumsuz ===================
kartla('06','Hipotez, teori ve kanun','Bilimsel bilgi türlerinin niteliği: sınanabilirlik, teorilerin değişebilmesi, teori–kanun farkı.','Teorinin kanıtlanınca kanun olacağını sanmak.','orta','öncüllü',3,'by-oo2-yontem','Bilimsel yöntem ve bilimsel bilgi')
d6={'I':(True,'Hipotez deney ya da gözlemle sınanabilen bir açıklama olmalıdır.'),
    'II':(True,'Teoriler yeni bulgular ışığında değiştirilebilir ya da geliştirilebilir.'),
    'III':(False,'Teori kanuna dönüşmez; teori olayları açıklar, kanun ise doğada değişmeden gözlenen düzenliliği belirtir.')}
r6=onc(d6,[('III',),('I','II'),('I','III'),('II','III'),('I','II','III')],olumsuz=True)
q('0006',oad(d6,True),
 z='orta',alt='Bilimsel bilgi',kaz='Hipotez, teori ve kanun kavramlarını ayırt eder.',kalip='öncüllü',ozet='teori–kanun',ne='üç ifade',
 metin='Biyoloji öğretmeni, bilimsel bilginin niteliğini anlatırken öğrencilerden aşağıdaki ifadelerin doğruluğunu değerlendirmelerini istemiştir.\nBilimsel bilgiyle ilgili,\nI. Bir hipotez, deney ya da gözlemle sınanabilir olmalıdır.\nII. Bir teori, yeni bulgular karşısında değiştirilebilir ya da geliştirilebilir.\nIII. Bir teori yeterince kanıtlandığında kanuna dönüşür.\nifadelerinden hangileri yanlıştır?',
 dogru=r6['dogru'],sira=r6['sira'],yan=r6['yan'],istenen='Yanlış olan öncüller.',
 ip=['Teori ile kanun aynı bilgi türü müdür, öncülleri bu açıdan değerlendir.'],bilgi=[TEO],
 puf='Teori kanuna dönüşmez; teori açıklar, kanun düzenliliği bildirir; ikisi de yeni bulgularla sınanabilir.')

# =================== 07 · metabolizma hızı–sıcaklık grafiği · orta ===================
kartla('07','Metabolizma hızı–sıcaklık grafiği','Çizgi grafiğinden hız değişimi okunur; yüksek sıcaklıkta hızın düşmesi enzim yapısının bozulmasıyla açıklanır.','Sıcaklık arttıkça hızın sürekli arttığını sanmak.','orta','grafik',4,'by-oo2-metab','Metabolizma ve grafik yorumlama')
TS=[0,10,20,30,40,50]; HZ=[2,5,10,15,20,2]
assert HZ[1]<HZ[2] and HZ[2]==2*HZ[1] and HZ[5]<HZ[4] and HZ[0]>0 and HZ[3]==3*HZ[1]
SK7=ax('\\addplot[vurgu,line width=1.5pt,mark=*] coordinates {'+' '.join(f'({t},{h})' for t,h in zip(TS,HZ))+'};',7.0,4.8,-2,52,0,23,'0,10,20,30,40,50','0,5,10,15,20','Sıcaklık ($^\\circ$C)','CO$_2$ miktarı (mL/saat)','')
sec7=[('10 °C ile 20 °C arasında metabolizma hızı azalmıştır.',False,'Grafikte 10 °C’tan 20 °C’a hız 5’ten 10’a çıkmıştır; azalmamıştır.'),
      ('Sıcaklık arttıkça metabolizma hızı her sıcaklıkta artar.',False,'50 °C’ta hız 20’den 2’ye düşmüştür; artış sürekli değildir.'),
      ('10 °C’taki metabolizma hızı, 20 °C’takinin iki katıdır.',False,'10 °C’ta hız 5, 20 °C’ta 10’dur; 20 °C’takinin yarısıdır.'),
      ('40 °C ile 50 °C arasında hızın azalması, enzimlerin yapısının bozulmasıyla açıklanabilir.',True,'Yüksek sıcaklıkta enzimler denatüre olur ve metabolizma hızı düşer.'),
      ('0 °C’ta maya hücrelerinde metabolizma tamamen durmuştur.',False,'0 °C’ta hız 2’dir; sıfır olmadığı için metabolizma tamamen durmamıştır.')]
d7,y7=tek(sec7,True)
q('0007',[A('Grafiği oku','Hız 0 °C’ta 2, 20 °C’ta 10, 40 °C’ta 20 ve 50 °C’ta 2’dir.','0:2 · 20:10 · 40:20 · 50:2'),
 A('Düşük sıcaklığı değerlendir','10 °C’tan 20 °C’a hız artmıştır; 0 °C’ta hız sıfır olmadığından metabolizma durmamıştır.','artış var; 0 °C’ta hız 2'),
 A('Yüksek sıcaklığı değerlendir','50 °C’ta hız düşmüştür; yüksek sıcaklık enzim yapısını bozar.','50 °C: denatürasyon'),
 A('İfadeyi seç','Grafikle ve enzim bilgisiyle uyumlu tek ifade seçilir.','Doğru: yüksek sıcaklıkta enzim bozulması')],
 z='orta',alt='Metabolizma',kaz='Sıcaklık–metabolizma hızı grafiğini yorumlar.',kalip='grafik',ozet='sıcaklık ve metabolizma hızı',ne='maya hücreleri',sekil=SK7,
 metin='Bir araştırmacı, aynı sayıda maya hücresi ve aynı derişimde glikoz çözeltisi içeren altı düzeneği farklı sıcaklıklarda bir saat bekletmiştir. Hücrelerin metabolizma hızının göstergesi olarak, her düzenekte bir saatte açığa çıkan karbondioksit miktarını ölçmüştür. Sonuçlar grafikte verilmiştir.\nBuna göre aşağıdakilerden hangisi söylenebilir?',
 dogru=d7,sira=yer('D',d7,[s[0] for s in sec7 if s[0]!=d7]),yan=[(m,c,t) for (m,c,t) in y7],istenen='Grafiğe göre doğru olan ifade.',
 ip=['Hız değerlerini 0, 10, 20, 40 ve 50 °C için ayrı ayrı okuyup her ifadeyi bu değerlerle karşılaştır.'],bilgi=[ENZ],
 puf='Metabolizma hızı optimuma kadar sıcaklıkla artar, yüksek sıcaklıkta enzimler bozulduğu için düşer.')

# =================== 08 · beslenme · orta · öncüllü ===================
kartla('08','Beslenme çeşitleri','Ototrof ve heterotrof canlıların ayrımı; kemosentez de ototrofluktur.','Mantarı ototrof saymak.','orta','öncüllü',4,'by-oo2-ozellik','Ortak özelliklerin tanınması')
d8={'I':(False,'Mantarlar heterotrofturlar; organik besini dışarıdan hazır alırlar.'),
    'II':(True,'Kemosentez yapan bakteriler inorganik maddelerden organik madde sentezledikleri için ototroftur.'),
    'III':(True,'Hayvanlar organik besini dışarıdan hazır aldıkları için heterotroftur.')}
r8=onc(d8,[('I',),('III',),('I','II'),('II','III'),('I','II','III')])
q('0008',oad(d8),
 z='orta',alt='Beslenme',kaz='Ototrof ve heterotrof canlıları ayırt eder.',kalip='öncüllü',ozet='ototrof–heterotrof',ne='mantar, kemosentetik bakteri, hayvan',
 metin='Canlılar, enerji ve organik madde ihtiyaçlarını karşılama biçimlerine göre ototrof ve heterotrof olarak gruplandırılır.\nBu gruplamayla ilgili,\nI. Mantarlar ototrof canlılardır.\nII. Kemosentez yapan bakteriler ototrof canlılardır.\nIII. Hayvanlar organik besinleri dışarıdan hazır alan canlılardır.\nifadelerinden hangileri doğrudur?',
 dogru=r8['dogru'],sira=r8['sira'],yan=r8['yan'],istenen='Doğru olan öncüller.',
 ip=['Ototrofluğun ölçütü, organik maddeyi kendisinin yapıp yapmamasıdır.'],bilgi=[BES],
 puf='Organik maddeyi kendisi yapan ototrof, dışarıdan hazır alan heterotroftur; mantar ve hayvanlar heterotroftur.')

# =================== 09 · virüs tablosu · orta · öncüllü · olumsuz ===================
kartla('09','Virüslerin canlılık durumu tablosu','Tablodaki özelliklerden virüsün canlılara ve cansızlara benzer yönleri ayrılır.','Virüsü hücresel yapıda ya da konak dışında çoğalan sanmak.','orta','tablo',4,'by-oo2-canli','Canlı–cansız ayrımı ve virüsler')
T09=[['Hücresel yapı','Yok','Var'],['Genetik materyal (DNA ya da RNA)','Var','Var'],['Kendi enzimleriyle metabolizma','Yok','Var'],['Konak hücre dışında çoğalma','Yok','Var'],['Kristal hâline geçebilme','Var','Yok']]
S09=tablo_svg(['Özellik','Virüsler','Bakteriler'],T09)
d9={'I':(True,'Virüsler DNA ya da RNA taşır; genetik materyal taşımak canlıların ortak özelliklerindendir.'),
    'II':(False,'Tabloda virüsler konak hücre dışında çoğalamaz; bakteriler gibi tek başlarına çoğalamazlar.'),
    'III':(True,'Kristal hâline geçebilmek cansız maddelere benzeyen bir özelliktir.')}
r9=onc(d9,[('I',),('II',),('III',),('I','II'),('I','III')],olumsuz=True)
q('0009',oad(d9,True),
 z='orta',alt='Virüsler',kaz='Virüslerin canlı ve cansızlara benzer özelliklerini tablodan yorumlar.',kalip='tablo',ozet='virüs–bakteri tablosu',ne='virüs ve bakteri karşılaştırması',sekil=S09,
 metin='Bir biyoloji öğrencisi, virüsleri ve bakterileri bazı özellikler bakımından karşılaştırmış ve sonuçları tabloya işlemiştir.\nBuna göre virüslerle ilgili,\nI. Genetik materyal taşımaları, canlılara benzeyen bir yönleridir.\nII. Bakteriler gibi konak hücre olmadan çoğalabilirler.\nIII. Kristal hâline geçebilmeleri, cansızlara benzeyen bir yönleridir.\nifadelerinden hangileri yanlıştır?',
 dogru=r9['dogru'],sira=r9['sira'],yan=r9['yan'],istenen='Tabloya göre yanlış olan öncüller.',
 ip=['Her öncülü tablodaki ilgili satırla karşılaştır.'],bilgi=[VIR],
 puf='Virüsler genetik materyal taşır ama hücresel yapıda değildir; yalnız konak hücre içinde çoğalır, bu yüzden canlı sayılmazlar.')

# =================== 10 · kan glikozu · orta · grafik · homeostazi ===================
kartla('10','Homeostazi grafiği: kan glikozu','Zaman–derişim grafiğinde değerin yükselip yeniden başlangıç düzeyine dönmesi homeostaziyi gösterir.','Yükselmeyi kalıcı sanmak ya da en yüksek değerin zamanını yanlış okumak.','orta','grafik',3,'by-oo2-uyum','Uyum, adaptasyon ve homeostazi')
ZG=[0,1,2,3,4,5,6]; GL=[90,90,140,115,95,90,90]
assert max(GL)==GL[2] and GL[4]>GL[0] and GL[5]==GL[0] and GL[1]==GL[0]
SK10=ax('\\addplot[vurgu,line width=1.5pt,mark=*] coordinates {'+' '.join(f'({t},{g})' for t,g in zip(ZG,GL))+'};',7.0,4.8,0,6.4,70,150,'0,1,2,3,4,5,6','80,100,120,140','Zaman (saat)','Kan glikozu (mg/100 mL)','')
sec10=[('Glikoz düzeyi yemekten sonra ölçüm boyunca sürekli artmıştır.',False,'Glikoz 2. saatten sonra azalmıştır; artış sürekli değildir.'),
       ('Yemekten sonra yükselen glikoz düzeyi, zamanla yemekten önceki değere yakın düzeye dönmüştür.',True,'Glikoz 140’a çıktıktan sonra 5. saatte yeniden 90’a inmiştir; bu iç dengenin korunmasıdır.'),
       ('En yüksek glikoz düzeyi 3. saatte ölçülmüştür.',False,'En yüksek değer 2. saatteki 140’tır; 3. saatte 115’tir.'),
       ('4. saatte glikoz düzeyi, yemekten önceki değerin altına düşmüştür.',False,'4. saatte düzey 95’tir; ilk değer olan 90’ın üzerindedir.'),
       ('Glikoz düzeyi 1. ve 2. saat arasında değişmemiştir.',False,'Bu aralıkta düzey 90’dan 140’a çıkmıştır.')]
d10,y10=tek(sec10,True)
q('0010',[A('Grafiği oku','Glikoz 1. saate kadar 90’da kalmış, 2. saatte 140’a çıkmış, sonra azalarak 5. saatte yeniden 90 olmuştur.','90 → 140 → 90'),
 A('İfadeleri sına','Artış 2. saatte son bulur; en yüksek değer 2. saattedir; 4. saatte düzey ilk değerin üzerindedir.','çoğu ifade grafiğe uymuyor'),
 A('Sonucu yaz','Yükselen glikozun başlangıç düzeyine dönmesi iç ortamın dengede tutulduğunu gösterir.','Doğru: başlangıç değerine dönüş')],
 z='orta',alt='Homeostazi',kaz='Kan glikozu grafiğini okuyup iç dengenin korunmasını yorumlar.',kalip='grafik',ozet='yemek sonrası glikoz',ne='zaman–glikoz grafiği',sekil=SK10,
 metin='Sağlıklı bir kişi sabah aç karnına kan örneği verdikten bir saat sonra karbonhidratlı bir yemeği, 1. saat ölçümünden hemen sonra yemiş ve sonraki saatlerde de belirli aralıklarla kan örneği vermiştir. Bu örneklerde ölçülen kan glikozu düzeyi grafikte gösterilmiştir.\nBuna göre aşağıdakilerden hangisi söylenebilir?',
 dogru=d10,sira=yer('B',d10,[s[0] for s in sec10 if s[0]!=d10]),yan=y10,istenen='Grafiğe göre doğru olan ifade.',
 ip=['Her ifadeyi grafikteki değerlerle tek tek karşılaştır.'],bilgi=[HOM],
 puf='İç ortamdaki bir değer değişip yeniden uygun düzeye dönüyorsa homeostazi vardır.')

# =================== 11 · adaptasyon örneği · kolay ===================
kartla('11','Adaptasyon örneği','Kalıtsal ve uzun sürede oluşan uyum adaptasyondur; tepki ve homeostazi kısa süreli olaylardır.','Kısa süreli tepkiyi adaptasyon sanmak.','kolay','düz',3,'by-oo2-uyum','Uyum, adaptasyon ve homeostazi')
d11='Ağaçkakanın gagasının, ağaç kabuğunu delmeye uygun yapıda olması'
q('0011',[A('Ölçütü hatırla','Adaptasyon, popülasyonun uzun sürede kazandığı kalıtsal yapı ve davranış uyumudur.','kalıtsal + uzun süre'),
 A('Şıkları ele','Işığa dönme ve geri çekilme uyarıya tepkidir; terleme ve kan şekerinin dengelenmesi homeostazidir.','4 şık tepki/homeostazi'),
 A('Sonucu yaz','Gaganın yapısı ortama uygun kalıtsal özelliktir.','Adaptasyon: gaga yapısı')],
 z='kolay',alt='Adaptasyon',kaz='Adaptasyon örneğini tepki ve homeostazi örneklerinden ayırır.',kalip='düz',ozet='adaptasyon–tepki–homeostazi',ne='beş canlı örneği',
 metin='Canlılar yaşadıkları ortama uygun yapı ve davranışlar geliştirmiştir.\nBuna göre aşağıdakilerden hangisi adaptasyona örnektir?',
 dogru=d11,sira=yer('E',d11,['Işıklı yöne getirilen bir bitkinin yapraklarını ışığa doğru döndürmesi','Sıcak havada bir insanın terleyerek vücut sıcaklığını dengede tutması','Dokunulan bir kaplumbağanın başını kabuğuna çekmesi','Soğuk havada bir insanın titreyerek vücut sıcaklığını dengede tutması']),
 yan=[('Işıklı yöne getirilen bir bitkinin yapraklarını ışığa doğru döndürmesi','Bu kısa sürede verilen bir yanıttır, yani uyarıya tepkidir; kalıtsal ve uzun süreli bir uyum değildir.','bilgi'),
      ('Sıcak havada bir insanın terleyerek vücut sıcaklığını dengede tutması','Terleme iç ortamı koruyan homeostazi örneğidir; uzun sürede oluşan kalıtsal uyum değildir.','bilgi'),
      ('Dokunulan bir kaplumbağanın başını kabuğuna çekmesi','Başını çekmek anlık bir uyarıya tepkidir; adaptasyon değildir.','bilgi'),
      ('Soğuk havada bir insanın titreyerek vücut sıcaklığını dengede tutması','Titreyerek vücut sıcaklığının dengelenmesi homeostazidir; adaptasyon uzun sürede kalıtımla kazanılır.','bilgi')],
 istenen='Adaptasyona örnek olan durum.',ip=['Her seçeneğin kısa sürede mi, uzun sürede mi ortaya çıktığına bak.'],bilgi=[OZ],
 puf='Kısa sürede verilen yanıt tepki ya da homeostazi, uzun sürede kalıtsal olarak yerleşen uyum adaptasyondur.')

# =================== 12 · tepkime şeması · orta · öncüllü ===================
kartla('12','Anabolizma–katabolizma şeması','Üç tepkimenin girenleri, ürünleri ve enerji durumuna göre anabolik ya da katabolik olduğu belirlenir.','Işık enerjisi alan tepkimeyi enerji açığa çıkarıyor sanmak.','orta','öncüllü',4,'by-oo2-metab','Metabolizma ve grafik yorumlama')
def satir(y,e,sol,sag,ust):
    return (f'\\node[font=\\small\\bfseries] at (0,{y}) {{{e}}};\\node[draw,rounded corners=3pt,minimum width=2.6cm,minimum height=.9cm,line width=1pt] (a{e}) at (2.2,{y}) {{{sol}}};'
            f'\\node[draw,rounded corners=3pt,minimum width=2.6cm,minimum height=.9cm,line width=1pt] (b{e}) at (8.6,{y}) {{{sag}}};'
            f'\\draw[-{{Stealth[length=2.4mm]}},line width=1.2pt] (a{e}.east)--(b{e}.west);\\node[font=\\small,above] at (5.4,{y}) {{{ust}}};')
SK12=tk(satir(2.4,'X','Amino asitler','Protein','ATP harcanır')+satir(1.2,'Y','Glikoz + O$_2$','CO$_2$ + H$_2$O','ATP üretilir')+satir(0,'Z','CO$_2$ + H$_2$O','Glikoz + O$_2$','Işık enerjisi alınır'),.9)
d12={'I':(True,'X’te amino asitlerden protein yapılır; küçük moleküllerden büyük molekül sentezi anabolizmadır.'),
     'II':(True,'Y’de glikoz yıkılır ve ATP üretilir; büyük molekülün yıkımı katabolizmadır.'),
     'III':(True,'Z’de alınan ışık enerjisi glikozun kimyasal bağlarında depolanır.')}
r12=onc(d12,[('II',),('III',),('I','III'),('II','III'),('I','II','III')])
q('0012',oad(d12),
 z='orta',alt='Metabolizma',kaz='Tepkimeleri girenler, ürünler ve enerji durumuna göre anabolik ya da katabolik olarak sınıflar.',kalip='şekilli',ozet='üç tepkime şeması',ne='protein yapımı, glikoz yıkımı, glikoz yapımı',sekil=SK12,
 metin='Şekilde, bir hücrede gerçekleşen X, Y ve Z tepkimelerinin girenleri, ürünleri ve enerji durumları gösterilmiştir.\nBuna göre,\nI. X tepkimesi anabolizmaya örnektir.\nII. Y tepkimesi katabolizmaya örnektir.\nIII. Z tepkimesinde alınan enerji ürünlerin kimyasal bağlarında depolanır.\nifadelerinden hangileri doğrudur?',
 dogru=r12['dogru'],sira=r12['sira'],yan=r12['yan'],istenen='Şekle göre doğru olan öncüller.',
 ip=['Her tepkimede girenlerin büyük mü küçük mü ürünlere dönüştüğüne ve enerjinin harcanıp açığa çıktığına bak.'],bilgi=[MET],
 puf='Küçükten büyüğe sentez anabolizma (enerji harcanır ya da depolanır), büyükten küçüğe yıkım katabolizmadır (ATP üretilir).')

# =================== 13 · çimlenme düzenekleri · zor · öncüllü ===================
kartla('13','Çimlenme düzenekleri: hangi iki düzenek karşılaştırılır','Dört düzenekte su, ışık ve sıcaklık farklarına bakılarak karşılaştırma çifti seçilir.','İki etkenin birlikte değiştiği düzenekleri karşılaştırıp sonuç çıkarmak.','orta','öncüllü',4,'by-oo2-karsilastir','Hangi düzenekler karşılaştırılır')
DZ=[dict(ad='I',su=True,isik=True,sic=25,cim=90),dict(ad='II',su=True,isik=False,sic=25,cim=90),dict(ad='III',su=False,isik=True,sic=25,cim=0),dict(ad='IV',su=True,isik=True,sic=5,cim=10)]
def fark(a,b): return {k for k in ('su','isik','sic') if DZ[a][k]!=DZ[b][k]}
assert fark(0,1)=={'isik'} and fark(0,2)=={'su'} and fark(1,3)=={'isik','sic'} and fark(0,3)=={'sic'}
def jar(x0,dz):
    b=f'\\draw[line width=1.3pt] ({x0},0) rectangle ({x0+1.8},2.0);'
    if dz['su']: b+=f'\\draw[fill=vurgu!18,line width=.8pt] ({x0+.05},.05) rectangle ({x0+1.75},1.0);'
    for sx in (.4,.9,1.4): b+=f'\\draw[line width=.8pt] ({x0+sx},.35) ellipse (.17 and .09);'
    cx,cy=x0+.9,3.0
    if dz['isik']:
        b+=f'\\draw[line width=1pt] ({cx},{cy}) circle (.22);'
        for a in range(0,360,60): b+=f'\\draw[line width=1pt] ({cx+.32*math.cos(math.radians(a)):.2f},{cy+.32*math.sin(math.radians(a)):.2f})--({cx+.5*math.cos(math.radians(a)):.2f},{cy+.5*math.sin(math.radians(a)):.2f});'
    else:
        b+=f'\\node[draw,line width=1pt,inner sep=3pt] at ({cx},{cy}) {{Karanlık}};'
    b+=f'\\node[font=\\small\\bfseries] at ({x0+.9},3.9) {{{dz["ad"]}}};'
    b+=f'\\node[font=\\small] at ({x0+.9},-.45) {{{dz["sic"]} °C}};\\node[font=\\small] at ({x0+.9},-1.05) {{\\%{dz["cim"]}}};\\node[font=\\small] at ({x0+.9},-1.65) {{{"var" if dz["su"] else "yok"}}};'
    return b
SK13=tk('\n'.join(jar(i*2.35,dz) for i,dz in enumerate(DZ))+'\\node[font=\\small,anchor=east] at (-.2,-1.05) {Çimlenme:};\\node[font=\\small,anchor=east] at (-.2,-1.65) {Su:};',.78)
d13={'I':(True,'I ve II’de yalnız ışık farklıdır; ışığın etkisi bu iki düzenek karşılaştırılarak anlaşılır.'),
     'II':(True,'I ve III’te yalnız su farklıdır; suyun etkisi bu iki düzenek karşılaştırılarak anlaşılır.'),
     'III':(False,'II ve IV’te ışık ve sıcaklık birlikte farklıdır; fark hangisinden doğduğu ayırt edilemez.')}
r13=onc(d13,[('I',),('I','II'),('I','III'),('II','III'),('I','II','III')])
q('0013',oad(d13),
 z='orta',alt='Deney düzeneği',kaz='Çimlenme deneyinde hangi düzeneklerin karşılaştırılarak hangi etkenin etkisinin anlaşılabileceğini belirler.',kalip='öncüllü',ozet='dört çimlenme düzeneği',ne='su, ışık, sıcaklık',sekil=SK13,
 metin='Bir araştırmacı, çimlenmeyi etkileyen etkenleri belirlemek için aynı türden 100’er tohum içeren dört düzenek kurmuştur. Düzeneklerde su, ışık ve sıcaklık koşulları şekilde gösterilmiş; bir hafta sonunda çimlenen tohumların yüzdeleri de belirtilmiştir.\nBu verilere göre,\nI. Işığın çimlenmeye etkisi I ve II numaralı düzenekler karşılaştırılarak anlaşılır.\nII. Suyun çimlenmeye etkisi I ve III numaralı düzenekler karşılaştırılarak anlaşılır.\nIII. Sıcaklığın çimlenmeye etkisi II ve IV numaralı düzenekler karşılaştırılarak anlaşılır.\nifadelerinden hangileri doğrudur?',
 dogru=r13['dogru'],sira=r13['sira'],yan=r13['yan'],istenen='Doğru olan öncüller.',
 ip=['Her öncüldeki iki düzeneği karşılaştır.'],bilgi=[DEG],
 puf='Bir etkenin etkisi, yalnız o etkenin farklı olduğu düzenekler karşılaştırılarak yorumlanır.')

# =================== 14 · adaptasyon ifadeleri · orta · olumsuz ===================
kartla('14','Adaptasyon ile ilgili yanlış ifade','Adaptasyon kalıtsal ve uzun sürede gelişen, ortama uyum sağlayan özelliktir; kısa sürede oluşan değişim adaptasyon değildir.','Adaptasyonu kısa sürede verilen yanıtla karıştırmak.','orta','düz',3,'by-oo2-uyum','Uyum, adaptasyon ve homeostazi')
d14='Adaptasyon, bir canlının bir gün içinde ortama uyum sağlamasıdır.'
sec14=[(d14,False,'Adaptasyon uzun sürede gelişen kalıtsal bir uyumdur; bir günde oluşmaz.'),
       ('Çöl bitkilerinde yaprakların dikene dönüşmesi, su kaybını azaltan bir adaptasyondur.',True,'Yaprağın dikene dönüşmesi çöl ortamına uygun kalıtsal bir yapıdır.'),
       ('Adaptasyon, canlının yaşadığı ortamda hayatta kalma ve üreme şansını artırır.',True,'Ortama uygun özellikler canlının yaşamını sürdürmesini kolaylaştırır.'),
       ('Aynı ortamda yaşayan farklı canlı türleri farklı adaptasyonlar gösterebilir.',True,'Her tür ortama kendine özgü yapı ve davranışlarla uyum sağlayabilir.'),
       ('Kutup ayısının kalın yağ tabakasına sahip olması soğuk ortama bir adaptasyondur.',True,'Kalın yağ tabakası soğuktan korunmayı sağlayan kalıtsal bir özelliktir.')]
dd14,y14=tek(sec14,False)
q('0014',[A('Kavramı hatırla','Adaptasyon, canlının yaşadığı ortama uygun, kalıtsal ve uzun sürede gelişen özelliğidir.','kalıtsal + uzun süre'),
 A('Doğru ifadeleri ayır','Dikene dönüşmüş yaprak ve yağ tabakası ortama uyumdur; hayatta kalma şansını artırır; farklı türler farklı uyumlar gösterebilir.','4 ifade doğru'),
 A('Yanlışı bul','Adaptasyon bir günde gerçekleşmez; bu ifade yanlıştır.','Yanlış: bir günde oluşma')],
 z='orta',alt='Adaptasyon',kaz='Adaptasyonun niteliğini ve örneklerini doğru değerlendirir.',kalip='düz',ozet='adaptasyon ifadeleri',ne='beş ifade',
 metin='Canlılar yaşadıkları ortamın koşullarına uygun yapı, işlev ve davranışlara sahiptir. Bu uygunluk, canlıların ortak özelliklerinden biri olan uyum (adaptasyon) ile açıklanır.\nBuna göre adaptasyonla ilgili aşağıdakilerden hangisi yanlıştır?',
 dogru=d14,sira=yer('A',d14,[s[0] for s in sec14 if s[0]!=d14]),yan=y14,istenen='Adaptasyonla ilgili yanlış ifade.',
 ip=['Her ifadenin ortaya çıkış süresiyle ilgili ne söylediğine bak.'],bilgi=[OZ],
 puf='Adaptasyon bir olay değil, uzun sürede gelişen kalıtsal bir uyumdur.')

# =================== 15 · adaptasyon, homeostazi, tepki · orta · öncüllü ===================
kartla('15','Adaptasyon, homeostazi ve tepki öncülleri','Üç kavramın niteliği: kalıtsal uyum, iç denge ve uyarılara tepkinin kapsamı.','Homeostaziyi yalnız çok hücrelilere ait sanmak; tepkiyi hayvanlara özgü sanmak.','orta','öncüllü',4,'by-oo2-uyum','Uyum, adaptasyon ve homeostazi')
d15={'I':(True,'Adaptasyon, popülasyonda uzun süre içinde ortaya çıkan kalıtsal bir uyumdur.'),
     'II':(False,'Homeostazi tek hücreli canlılarda da görülür; örneğin bazı tek hücrelilerde fazla suyun kofullarla atılması iç ortamı dengede tutar.'),
     'III':(False,'Bitkiler de uyarılara tepki verir; örneğin yaprakların ışığa yönelmesi bir tepkidir.')}
r15=onc(d15,[('I',),('II',),('III',),('I','II'),('I','III')])
q('0015',oad(d15),
 z='orta',alt='Uyum ve homeostazi',kaz='Adaptasyon, homeostazi ve uyarılara tepki kavramlarını doğru tanımlar.',kalip='öncüllü',ozet='üç kavram',ne='kalıtsal uyum, iç denge, tepki',
 metin='Bir öğrenci, canlıların ortak özelliklerinden olan uyum, iç denge ve tepkiyle ilgili aşağıdaki ifadeleri yazmıştır.\nI. Adaptasyon, popülasyonda uzun süre içinde ortaya çıkan kalıtsal bir uyumdur.\nII. Homeostazi yalnız çok hücreli canlılarda görülür.\nIII. Uyarılara tepki yalnız hareketli canlılarda görülür.\nBuna göre bu ifadelerden hangileri doğrudur?',
 dogru=r15['dogru'],sira=r15['sira'],yan=r15['yan'],istenen='Doğru olan öncüller.',
 ip=['“Yalnız” sözcüğü geçen ifadeler için bir karşı örnek bulmaya çalış.'],bilgi=[OZ],
 puf='“Yalnız … canlılarda” diyen ifadeler için karşı örnek ara; tepki ve homeostazi tek hücrelilerde de bitkilerde de görülür.')

# =================== 16 · solunum · kolay · olumsuz ===================
kartla('16','Solunum ile ilgili yanlış ifade','Solunum her canlıda, hücrede gerçekleşen katabolik bir olaydır; akciğerli olmak şart değildir.','Solunumu yalnız akciğerle yapılan gaz alışverişi sanmak.','kolay','düz',3,'by-oo2-ozellik','Ortak özelliklerin tanınması')
d16='Solunum yalnız akciğeri olan canlılarda gerçekleşir.'
sec16=[('Hücresel solunumda organik maddelerin yıkılmasıyla ATP üretilir.',True,'Solunum, organik maddelerin yıkılıp ATP üretildiği olaydır.'),
       ('Oksijen kullanmadan enerji elde eden canlılar da vardır.',True,'Oksijensiz solunum yapan canlılar bulunur.'),
       ('Bitki hücreleri hem fotosentez hem de solunum yapabilir.',True,'Bitkiler de canlı olduğu için hücrelerinde solunum yapar.'),
       (d16,False,'Solunum hücrelerde gerçekleşir; akciğeri olmayan canlılar da solunum yapar.'),
       ('Solunum katabolik bir metabolizma olayıdır.',True,'Büyük molekülün yıkılıp enerji açığa çıkması katabolizmadır.')]
dd16,y16=tek(sec16,False)
q('0016',[A('Solunumu hatırla','Solunum, besinlerdeki enerjinin ATP olarak elde edildiği hücresel bir olaydır.','hücrede ATP üretimi'),
 A('Doğru ifadeleri ayır','Organik maddelerin yıkımı, oksijensiz solunum, bitkilerde solunum ve katabolizma bilgileri doğrudur.','4 ifade doğru'),
 A('Yanlışı bul','Akciğeri olmayan canlılar da solunum yaptığı için “yalnız akciğerli canlılarda” ifadesi yanlıştır.','Yanlış: akciğer şartı')],
 z='kolay',alt='Solunum',kaz='Solunumun her canlıda gerçekleşen hücresel bir olay olduğunu bilir.',kalip='düz',ozet='solunum ifadeleri',ne='akciğer yanılgısı',
 metin='Solunum, canlıların ortak özelliklerinden biridir. Canlılar bu olay sayesinde besinlerinde depolanmış enerjiyi hücrelerinin kullanabileceği biçime dönüştürür.\nBuna göre solunumla ilgili aşağıdakilerden hangisi yanlıştır?',
 dogru=d16,sira=yer('D',d16,[s[0] for s in sec16 if s[0]!=d16]),yan=y16,istenen='Solunumla ilgili yanlış ifade.',
 ip=['“Yalnız” gibi sınırlayıcı sözcük içeren ifade var mı, varsa karşı örnek ara.'],bilgi=[OZ,MET],
 puf='Solunum akciğerle değil hücrede gerçekleşir; akciğer yalnız gaz alışverişi yapan bir organdır.')

# =================== 17 · vitamin deneyi tablosu · zor ===================
kartla('17','Vitamin deneyi: iki değişken birlikte değişince yorum','Tabloda gruplar arasındaki besin ve vitamin farkları birlikte değerlendirilerek ifadeler sınanır.','D3’ü vitaminin tek başına etkisini gösteriyor sanmak.','zor','tablo',5,'by-oo2-karsilastir','Hangi düzenekler karşılaştırılır')
GR=[['K','Standart',0,6],['D1','Standart',1,9],['D2','Standart',2,12],['D3','Yüksek proteinli',2,16]]
assert GR[0][3]<GR[1][3]<GR[2][3] and GR[3][1]!=GR[2][1] and GR[3][2]==GR[2][2]
S17=tablo_svg(['Grup','Besin türü','Vitamin (mg/gün)','Kütle artışı (g)'],[[g,b,str(v),str(k)] for g,b,v,k in GR])
d17='K, D1 ve D2 grupları karşılaştırıldığında, vitamin miktarı arttıkça kütle artışının arttığı söylenebilir.'
sec17=[('D3 grubundaki kütle artışı yalnız vitamin miktarına bağlıdır.',False,'D3’te besin türü de farklıdır; artış vitaminden mi proteinden mi doğduğu ayırt edilemez.'),
       ('D1, D2 ve D3 gruplarındaki farklar yalnız vitamin miktarından kaynaklanır.',False,'D3’te vitamin D2 ile aynıdır ama besin türü farklıdır; farklar yalnız vitaminden kaynaklanmaz.'),
       (d17,True,'K, D1 ve D2’de besin aynıdır, yalnız vitamin farklıdır; kütle artışı 6, 9, 12 g olarak artmıştır.'),
       ('Bu deneyde kontrol grubu D3 grubudur.',False,'Kontrol grubu, denenen etkenin (vitamin) uygulanmadığı K grubudur.'),
       ('K grubundaki fareler hiç kütle kazanmamıştır.',False,'K grubunda kütle artışı 6 g’dır; vitamin verilmese de fareler kütle kazanmıştır.')]
dd17,y17=tek(sec17,True)
q('0017',[A('Tabloyu oku','K, D1, D2’de besin aynı; vitamin 0, 1, 2 mg; kütle artışı 6, 9, 12 g. D3’te vitamin D2 ile aynı ama besin farklı.','K–D1–D2: yalnız vitamin farklı'),
 A('Kontrol grubunu bul','Vitamin verilmeyen K grubu kontrol grubudur.','Kontrol: K'),
 A('D3’ü değerlendir','D3’te besin türü ve kütle artışı farklıdır; vitaminin tek başına etkisi için kullanılamaz.','D3: iki etken birden farklı'),
 A('İfadeleri ele','D3’e dayanan ve K’nin hiç kütle almadığını söyleyen ifadeler tabloya uymaz.','4 ifade yanlış'),
 A('Doğruyu seç','Yalnız vitamin farklıyken oluşan artışı söyleyen ifade doğrudur.','K, D1, D2 karşılaştırması')],
 z='zor',alt='Deney sonuçları',kaz='Tabloda yalnız bir etkenin farklı olduğu grupları belirleyip doğru çıkarım yapar.',kalip='tablo',ozet='vitamin ve besin türü',ne='dört fare grubu',sekil=S17,
 metin='Bir araştırmacı, yeni geliştirilen bir vitamin takviyesinin farelerin kütle artışına etkisini incelemek için aynı türden, aynı yaşta ve başlangıç kütleleri eşit olan fareleri dört gruba ayırmıştır. Her grupta 10 fare bulunmaktadır. Grupların besin türü ve günlük vitamin miktarı ile dört hafta sonundaki ortalama kütle artışları tabloda verilmiştir.\nBuna göre aşağıdakilerden hangisi söylenebilir?',
 dogru=d17,sira=yer('C',d17,[s[0] for s in sec17 if s[0]!=d17]),yan=y17,istenen='Tabloya göre doğru olan ifade.',
 ip=['Her ifadede hangi grupların karşılaştırıldığına bak.'],bilgi=[DEG],
 puf='Gruplar arasında hangi etkenlerin farklı olduğunu belirlemeden yorum yapma.')

# =================== 18 · bilimsel yöntem sırası · zor ===================
kartla('18','Bilimsel yöntem adımlarının sırası','Karışık verilen beş işlem: gözlem → hipotez → deney düzeneği → veri kaydı → sonuca karar.','Hipotezi gözlemden önce ya da veri kaydını deney kurmadan önce koymak.','orta','düz',5,'by-oo2-yontem','Bilimsel yöntem ve bilimsel bilgi')
OL={'I':'Gruplardaki fidelerin eğilme açılarının ölçülüp kaydedilmesi','II':'“Fideler ışığın geldiği yöne doğru büyür.” düşüncesinin ortaya atılması','III':'Pencere kenarındaki fidelerin pencereye doğru eğildiğinin fark edilmesi','IV':'Verilere bakılarak düşüncenin desteklenip desteklenmediğine karar verilmesi','V':'Fidelerin bir bölümünün tek yönlü, bir bölümünün her yönden ışık alacağı düzeneklerin kurulması'}
DOGS=['III','II','V','I','IV']
fmt=lambda s:' – '.join(s)
d18=fmt(DOGS)
yan18=[('II – III – V – I – IV','Hipotezi gözlemden önce yazmış; oysa tahmin, olayın fark edilmesinden sonra gelir.','bilgi'),
       ('III – II – I – V – IV','Verileri düzeneği kurmadan önce kaydetmiş; oysa ölçüm, deney düzeneği kurulduktan sonra yapılır.','dikkat'),
       ('III – II – V – IV – I','Karar vermeyi ölçüm yapmadan önce koymuş; oysa karar, kaydedilen verilere göre verilir.','dikkat'),
       ('III – V – II – I – IV','Düzeneği hipotezden önce kurmuş; oysa deney, sınanacak düşünce belli olduktan sonra tasarlanır.','bilgi')]
sira18=sorted([d18]+[y[0] for y in yan18]); assert len(set(sira18))==5
q('0018',[A('Gözlemi bul','Olay önce fark edilir: pencere kenarındaki fidelerin eğilmesi.','ilk: III'),
 A('Hipotezi yerleştir','Gözlemden sonra olası açıklama (hipotez) ortaya atılır.','ikinci: II'),
 A('Deneyi sırala','Hipotez sınanmak için düzenek kurulur, sonra ölçümler yapılıp kaydedilir.','III. ve IV. sıra: V, I'),
 A('Sonucu yerleştir','En son, veriler yorumlanarak hipotezin desteklenip desteklenmediğine karar verilir.','son: IV'),
 A('Sırayı yaz','Gözlem, hipotez, deney düzeneği, veri kaydı, karar.',d18)],
 z='orta',alt='Bilimsel yöntem',kaz='Bilimsel yöntemin basamaklarını doğru sıraya koyar.',kalip='düz',ozet='fide eğilmesi araştırması',ne='beş işlem sıralaması',
 metin='Bir araştırmacının, fidelerin ışığa karşı davranışını araştırırken yaptığı çalışmada gerçekleştirdiği işlemler aşağıda karışık sırayla verilmiştir.\nI. '+OL['I']+'\nII. '+OL['II']+'\nIII. '+OL['III']+'\nIV. '+OL['IV']+'\nV. '+OL['V']+'\nBuna göre bu işlemler gerçekleştirilme sırasına göre aşağıdakilerden hangisi gibi olmalıdır?',
 dogru=d18,sira=sira18,yan=yan18,istenen='İşlemlerin doğru gerçekleşme sırası.',
 ip=['Hangi işlem diğerlerinin dayanağı olarak önce gelir?'],bilgi=[YON],
 puf='Bilimsel yöntem sırası: gözlem, hipotez, deney düzeneği, veri kaydı, sonuç; karar her zaman verilerden sonra gelir.')

# =================== yaz ===================
print({q_['id'][-4:]:q_['cevap']['sik'] for q_ in P.ANA})
bitir(P,'ortakozellikiki',UK)
