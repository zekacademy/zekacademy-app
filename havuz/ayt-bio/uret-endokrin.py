"""AYT Biyoloji · Endokrin Sistem · 20 soru (kardeş yok, ipucu 1). Şekil verileri Python'da hesaplanır; öncüllerin doğru/yanlış değeri tek yerde (onc) tanımlanır."""
import sys,os,math,json
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-bio')); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
import _hafif_bio as H
from _hafif_bio import *
from cizim import tikz_svg
H.KONU='Endokrin Sistem'
KONU_K='abio|Endokrin Sistem'
P=Parti('endokrin','Endokrin Sistem',KONU_K,ders='AYT Biyoloji',idon='aytbio')
KY='ÖSYM AYT 2018–2026 Biyoloji (Endokrin Sistem; yalnız mantık) · MEB 12. sınıf biyoloji'
TIPLER={'en-bez':'Endokrin bezler ve hormonların görevleri','en-genel':'Hormonların genel özellikleri ve etkileşimi','en-hipo':'Hipotalamus–hipofiz ilişkisi ve su dengesi',
 'en-geri':'Geri bildirim mekanizmaları','en-glikoz':'Kan glikoz düzeyinin düzenlenmesi','en-ca':'Kan kalsiyum düzeyi ve tiroit–paratiroit'}
CARD={}
def card(no,alt,fikir,tuzak,z,kalip,adim,tipId,ozet):
    kart(f'K-ABEN-{no:02d}',alt,fikir,tuzak,z,kalip,adim,tipId,TIPLER[tipId],KY); CARD[no]=ozet
def q(no,cn,ad,**k):
    mk(P,no,ad=ad,adim=len(ad),kart=f'K-ABEN-{cn:02d} ('+CARD[cn]+')',tip=TIPLER[k['tipId']],**k)
SIR=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
SETS={'Yalnız I':{'I'},'Yalnız II':{'II'},'Yalnız III':{'III'},'I ve II':{'I','II'},'I ve III':{'I','III'},'II ve III':{'II','III'},'I, II ve III':{'I','II','III'}}
def onc(truth,why,pos,neg=False):
    nm=['I','II','III']; C={n for n,t in zip(nm,truth) if (not t if neg else t)}
    dogru=[s for s in SIR if SETS[s]==C][0]; p=SIR.index(dogru)
    cand=[s for s in SIR if s!=dogru]
    key=lambda s:(len(SETS[s]^C),abs(SIR.index(s)-p))
    bef=sorted([s for s in cand if SIR.index(s)<p],key=key)[:pos]; aft=sorted([s for s in cand if SIR.index(s)>p],key=key)[:4-pos]
    assert len(bef)==pos and len(aft)==4-pos,(dogru,pos)
    sec=bef+aft; yan=[]
    for s in sec:
        ex=sorted(SETS[s]-C,key=nm.index); ms=sorted(C-SETS[s],key=nm.index); parts=[]
        for n in ex: parts.append(f'{n}. yargıyı da doğru sanmış; oysa {why[nm.index(n)]}.')
        for n in ms: parts.append(f'{n}. yargının doğru olduğunu görememiş; {why[nm.index(n)]}.')
        yan.append((s,' '.join(parts),'bilgi' if ex else 'dikkat'))
    sira=sorted(sec+[dogru],key=SIR.index); assert sira.index(dogru)==pos
    return dict(dogru=dogru,sira=sira,yan=yan)
def tek(opts,hedef,pos):
    """opts: [(metin,bool,olgu)] 5 adet; hedef: aranan doğruluk değeri; pos: doğru şıkkın sırası."""
    assert len(opts)==5
    h=[o for o in opts if o[1]==hedef]; assert len(h)==1
    dg=h[0]; yn=[o for o in opts if o[1]!=hedef]
    sira=yn[:pos]+[dg]+yn[pos:]
    return dict(dogru=dg[0],sira=[x[0] for x in sira],yan=[(o[0],o[2],'bilgi') for o in yn])

# ---------------- çizim yardımcıları
def tk(body,scale=1.0): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small,scale=%s]\n%s\n\\end{tikzpicture}'%(scale,body))
OK='-{Stealth[length=2.3mm,width=1.9mm]}'
def ck(knots,n=12):
    """knots: [(t,y)] — kosinüs yumuşatmalı parçalı eğri (düğümlerde teğet yatay)"""
    pts=[]
    for (t0,y0),(t1,y1) in zip(knots,knots[1:]):
        for i in range(n+ (1 if (t1,y1)==knots[-1] else 0)):
            u=i/n; pts.append((t0+(t1-t0)*u,y0+(y1-y0)*(1-math.cos(math.pi*u))/2))
    return pts
def co(pts): return ' '.join(f'({x:.3f},{y:.3f})' for x,y in pts)
def pg(opts,body):
    return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n\\begin{axis}['+opts+']\n'+body+'\n\\end{axis}\n\\end{tikzpicture}')
AXO='axis lines=left,label style={font=\\small},tick label style={font=\\small}'

# ---------------- bilgi kutuları (örnekler soruların maddelerini/sonuçlarını söylemez)
BEZ=B('Endokrin bezler ve hormonlar','endokrin bezler salgılarını (hormon) kanalsız olarak doğrudan kana verir; hormonlar kanla taşınır ve yalnız kendilerine özgü reseptörü bulunan hedef hücrelerde etki eder. Başlıca endokrin yapılar hipotalamus, hipofiz, epifiz, tiroit, paratiroit, böbreküstü, pankreas (Langerhans adacıkları) ve eşey bezleridir. Örnek: epifiz bezi melatonin hormonunu salgılar')
ORT=B('Sinirsel ve hormonal düzenleme','iç dengeyi sinir sistemi ile endokrin sistem birlikte sağlar; sinirsel uyarı nöronlar boyunca iletilir, hormonlar ise kan dolaşımıyla taşınır. Hedef hücreler, hormona özgü reseptörü taşıyorsa yanıt verir. Örnek: bir hormonun reseptörü olmayan hücre o hormonu algılayamaz')
HIP=B('Hipotalamus ve hipofiz','hipofiz, beyinde hipotalamusun altında yer alan ve ön lob ile arka lobdan oluşan endokrin bir bezdir. Hipotalamus sinir sistemini endokrin sisteme bağlayan merkezdir; salgıladığı bazı hormonlar hipofize ulaşır. Örnek: hipofizin ön lobu ve arka lobu farklı hormonlar salgılar')
GER=B('Geri bildirim','negatif geri bildirimde bir hormonun etkisi o hormonun salgısını azaltır, böylece değer dar sınırlar içinde kalır; pozitif geri bildirimde etki, salgıyı daha da artırır ve olay tamamlanınca sona erer. Örnek: vücut sıcaklığı yükselince terlemenin başlaması ve sıcaklığın normale dönmesi negatif geri bildirimdir')
TIR=B('Tiroit bezi','tiroit bezi boyunda bulunur ve tiroksin salgılar; tiroksinin yapısına iyot katılır. Ön hipofiz, tiroit uyarıcı hormon (TSH) salgılayarak tiroit bezinin çalışmasını denetler. Örnek: vücuda yeterli iyot alınmazsa tiroksin sentezi aksar')
GLK=B('Kan glikozu','kan glikoz düzeyi pankreas ve böbreküstü bezi hormonlarıyla dar sınırlar içinde tutulur; fazla glikoz karaciğer ve kaslarda glikojen olarak depolanabilir. Pankreasın Langerhans adacıklarında iki tür hormon salgılayan hücre bulunur. Örnek: glikojen, çok sayıda glikoz biriminden oluşan depo polisakkarittir')
GLK2=B('Hormon–etki ilişkisi','bir hormon, hedef hücrelerdeki reseptörüne bağlanarak etki eder; hormonun salgısı, düzenlediği değerin değişimine bağlı olarak artar ya da azalır. Grafik ve tablolarda önce değişimin yönü okunur, sonra bu değişimi yapabilecek hormon düşünülür. Örnek: bir değer artınca salgısı artan hormon o değeri geri azaltıyorsa bu negatif geri bildirimdir')
CAL=B('Kan kalsiyum düzeyi','kalsiyum iyonları kemik dokuda depolanır ve kan kalsiyum düzeyi dar sınırlar içinde tutulur; bu düzenleme tiroit ve paratiroit bezlerinin hormonlarıyla yapılır. Paratiroit bezleri tiroit bezinin arka yüzünde yer alır. Örnek: kalsiyum, kas kasılmasında da görevli bir iyondur')
OZM=B('Kanın ozmotik derişimi','kan plazmasının ozmotik derişimi, çözünmüş madde yoğunluğunun ölçüsüdür; su kaybı derişimi artırır, fazla su alımı azaltır. Hipotalamustaki ozmoreseptörler bu derişimi algılar. Örnek: tuzlu yiyecek yedikten sonra kanın ozmotik derişimi geçici olarak artabilir')
BOB=B('Böbreküstü bezi','böbreküstü bezi iki bölümden oluşur: iç kısım medulla (öz), dış kısım korteks (kabuk). Medulla, sinir sisteminden gelen uyarıyla hızlı yanıt veren hormon salgılar; korteks ise başka hormonlar üretir. Örnek: her iki böbreğin üstünde birer böbreküstü bezi bulunur')
GH=B('Büyüme hormonu','büyüme hormonu ön hipofizden salgılanır ve kemik ile kas gibi dokuların büyümesini uyarır; uzun kemiklerin boyuna uzaması büyüme çağında epifiz kıkırdağının açık olmasına bağlıdır. Örnek: uzun kemiklerin uç kısımlarında büyüme plakları yer alır')
DEN=B('Deney tasarımı','kontrol grubu, uygulanan işlemin dışındaki bütün koşulları aynı tutan gruptur; sahte ameliyat grubu ameliyatın kendi etkisini ayırt etmek için kullanılır. Bağımsız değişken denenen uygulamadır, bağımlı değişken ölçülen sonuçtur. Örnek: ilaç denemesinde ilaç verilmeyen gruba plasebo verilir')
DIY=B('Diyabet','diyabet, kan glikoz düzeyinin uzun süre yüksek kalmasıyla görülen bir hastalıktır. Glikoz tolerans testinde kişi glikoz çözeltisi içer ve kan glikozunun nasıl değiştiği izlenir. Örnek: açlık kan glikozunun sağlıklı bireylere göre belirgin yüksek olması dikkat çeken bir bulgudur')

# ================ 01 · kolay · bez konumları, öncüllü
card(1,'Bez konumları ve görevleri','Şekildeki bezler konumlarından tanınır; her bezin salgıladığı hormon ve görevi eşleştirilir.','Hipofizi yalnız büyüme ile ilişkilendirmek; böbreküstü bezini yalnız böbrek işleviyle karıştırmak.','kolay','öncüllü',3,'en-bez','numaralı bezler ve hormonları')
b=[]
b.append('\\draw[line width=1.1pt] (0,5.2) circle (.55);')
b.append('\\draw[line width=1.1pt] (-.2,4.67)--(-.2,4.3) (.2,4.67)--(.2,4.3);')
b.append('\\draw[line width=1.1pt,rounded corners=10pt] (-.2,4.3)--(-1.3,4.05)--(-1.15,.9)--(1.15,.9)--(1.3,4.05)--(.2,4.3);')
b.append('\\draw[line width=.9pt,fill=black,fill opacity=.12] (-.1,2.0) ellipse (.2 and .36); \\draw[line width=.9pt,fill=black,fill opacity=.12] (.1,2.0) ellipse (.2 and .36);')
b.append('\\draw[line width=.9pt] (-.1,2.0) ellipse (.2 and .36); \\draw[line width=.9pt] (.1,2.0) ellipse (.2 and .36);')
b[-2]='\\draw[line width=.9pt,fill=black,fill opacity=.12] (-.6,1.9) ellipse (.2 and .36); \\draw[line width=.9pt,fill=black,fill opacity=.12] (.6,1.9) ellipse (.2 and .36);'
b[-1]='\\draw[line width=.9pt] (-.6,1.9) ellipse (.2 and .36); \\draw[line width=.9pt] (.6,1.9) ellipse (.2 and .36);'
b.append('\\fill (-.6,2.32) ellipse (.17 and .07); \\fill (.6,2.32) ellipse (.17 and .07);')   # böbreküstü
b.append('\\fill (0,5.0) ellipse (.13 and .09);')   # hipofiz
b.append('\\fill (-.13,4.45) ellipse (.1 and .17); \\fill (.13,4.45) ellipse (.1 and .17); \\fill (0,4.43) rectangle (.001,4.44);')   # tiroit
def etk(n,x,y,x1,y1,x2,y2): return f'\\node[draw,circle,inner sep=1.6pt,font=\\small\\bfseries] at ({x},{y}) {{{n}}};\\draw[line width=.8pt] ({x1},{y1})--({x2},{y2});'
b.append(etk(1,2.3,5.0,2.05,5.0,.16,5.0)); b.append(etk(2,2.3,4.45,2.05,4.45,.24,4.45)); b.append(etk(3,2.3,2.32,2.05,2.32,.78,2.32))
SK=tk('\n'.join(b))
w1=onc([True,True,True],['1 numaralı bez hipofizdir; tiroit, böbreküstü ve eşey bezleri gibi bezlerin çalışmasını uyaran hormonlar salgılar','2 numaralı bez tiroit bezidir; salgıladığı tiroksin bazal metabolizma hızını artırır','3 numaralı bez böbreküstü bezidir; adrenalin ve kortizol gibi stres durumunda etkili hormonlar salgılar'],4)
q('0001',1,[A('Bezleri tanı','Şekildeki konumlara bak: baştaki bez hipofiz, boyundaki bez tiroit, böbreklerin üstündeki bez böbreküstü bezidir.','1: hipofiz · 2: tiroit · 3: böbreküstü'),
   A('I. yargıyı değerlendir','Hipofiz, birçok endokrin bezin çalışmasını uyaran hormonlar salgılar.','I: doğru'),
   A('II. yargıyı değerlendir','Tiroit bezinin hormonu tiroksin, hücrelerin metabolizma hızını yükseltir.','II: doğru'),
   A('III. yargıyı değerlendir','Böbreküstü bezi, stres durumunda etkili hormonları salgılar.','III: doğru'),
   A('Sonuç','Üç yargı da doğrudur.','I, II ve III')],
 tipId='en-bez',z='kolay',alt='Bezler ve Hormonlar',kaz='Şematik gövde çiziminde hipofiz, tiroit ve böbreküstü bezlerini tanır; salgıladıkları hormonların görevlerini ilişkilendirir.',kalip='öncüllü',
 metin='Şekilde insan vücudundaki bazı endokrin bezler 1, 2 ve 3 ile numaralandırılmıştır.\nBuna göre,\nI. 1 numaralı bez, diğer bazı endokrin bezlerin çalışmasını uyaran hormonlar salgılar.\nII. 2 numaralı bez, salgıladığı hormonla bazal metabolizma hızını artırır.\nIII. 3 numaralı bez, stres durumunda etkili olan hormonlar salgılar.\nyargılarından hangileri doğrudur?',
 sekil=SK,dogru=w1['dogru'],yan=w1['yan'],sira=w1['sira'],istenen='Şekildeki bezlerle ilgili doğru yargılar.',
 ip=['Her bezi vücuttaki konumundan tanı, sonra yargıdaki göreviyle o bezin hormonlarını karşılaştır.'],bilgi=[BEZ],
 puf='Bezi konumundan tanı, sonra salgıladığı hormonu ve görevini eşleştir.')

# ================ 02 · kolay · tablo, öncüllü
card(2,'Hormon–bez–etki tablosu','Tabloda her satırın üç bilgisi (hormon, salgılayan yapı, etki) ayrı ayrı doğrulanır; bir bilgi yanlışsa satır yanlıştır.','Satırdaki etkiyi doğru bulup salgılayan yapıyı kontrol etmemek.','kolay','tablo',3,'en-bez','tabloda hormon–bez–etki eşleştirmesi')
SK=tablo_svg(['Hormon','Salgılayan yapı','Etkisi'],[['I. Glukagon','Pankreas','Karaciğerde glikojen yıkımını artırır'],['II. Tiroksin','Hipofiz','Metabolizma hızını artırır'],['III. Kalsitonin','Paratiroit bezi','Kan kalsiyum düzeyini artırır']])
w2=onc([True,False,False],['glukagon pankreastan salgılanır ve karaciğerde glikojen yıkımını artırarak kan glikozunu yükseltir','tiroksini hipofiz değil, tiroit bezi salgılar','kalsitonini tiroit bezi salgılar ve kan kalsiyum düzeyini düşürür; paratiroit bezi parathormon salgılar'],0)
q('0002',2,[A('Satırları ayrı ayrı oku','Her satırdaki hormonu, salgılayan yapıyı ve etkiyi tek tek sına.','I, II, III satırları'),
   A('I. satırı değerlendir','Glukagon pankreasın α hücrelerinden salgılanır ve karaciğerde glikojeni yıkar.','I: doğru'),
   A('II. satırı değerlendir','Etki doğrudur ama tiroksini salgılayan yapı hipofiz değil tiroit bezidir.','II: yanlış'),
   A('III. satırı değerlendir','Hem salgılayan yapı hem etki hatalıdır: kalsitonin tiroit bezinden salgılanır ve kalsiyumu düşürür.','III: yanlış'),
   A('Sonuç','Yalnız I. satırdaki bilgilerin tümü doğrudur.','Yalnız I')],
 tipId='en-bez',z='kolay',alt='Bezler ve Hormonlar',kaz='Tabloda verilen hormon, salgılayan bez ve etki eşleştirmelerinin doğruluğunu değerlendirir.',kalip='tablo',
 metin='Bir biyoloji öğretmeni öğrencilerden bazı hormonları, bu hormonları salgılayan yapıları ve hormonların etkilerini içeren bir tablo hazırlamalarını istiyor. Bir öğrencinin hazırladığı tablo şekilde verilmiştir.\nBuna göre, tablodaki satırlardan hangilerinde yazılan bilgilerin tümü doğrudur?',
 sekil=SK,dogru=w2['dogru'],yan=w2['yan'],sira=w2['sira'],istenen='Bilgilerin tümü doğru olan satırlar.',
 ip=['Her satırda üç bilgiyi (hormon, salgılayan yapı, etki) ayrı ayrı sına; birinin hatası bile satırı yanlış yapar.'],bilgi=[BEZ],
 puf='Bir satırın doğru sayılması için hormon–bez–etki üçlüsünün hepsi doğru olmalıdır.')

# ================ 03 · kolay · olumsuz · hormonların genel özellikleri
card(3,'Hormonların ortak özellikleri','Hormonlar kanalsız bezlerden kana verilir, kanla taşınır, yalnız reseptörü olan hücreleri etkiler; sinirsel etkiye göre daha yavaş ve uzun sürelidir.','Hormonların özel kanallarla taşındığını sanmak.','kolay','düz',3,'en-genel','hormonların genel özellikleri (olumsuz kök)')
o3=[('Endokrin bezlerin salgıları kanalsız olarak doğrudan kana verilir.',True,'Doğru bir bilgiyi yanlış sanmış; endokrin bezler kanalsızdır ve salgılarını doğrudan kana verir.'),
    ('Hormonlar çok küçük miktarlarda bile hedef hücrelerde etki oluşturabilir.',True,'Doğru bir bilgiyi yanlış sanmış; hormonlar çok az miktarda etkilidir.'),
    ('Bir hormon yalnız kendisine özgü reseptörü taşıyan hücreleri etkiler.',True,'Doğru bir bilgiyi yanlış sanmış; hormonun etkisi hedef hücredeki özgün reseptöre bağlıdır.'),
    ('Hormonların etkisi, sinirsel etkiye göre genellikle daha yavaş başlar ve daha uzun sürer.',True,'Doğru bir bilgiyi yanlış sanmış; hormonlar kanla taşındığı için etkileri sinirsel uyarıdan geç başlar.'),
    ('Hormonlar, salgılandıkları bezden hedef organa özel kanallarla taşınır.',False,'')]
w3=tek(o3,False,4)
q('0003',3,[A('Kökü yorumla','Soru yanlış olan ifadeyi arıyor; bu yüzden doğru ifadeleri eleyeceğiz.','Aranan: yanlış ifade'),
   A('Salgı ve taşınmayı hatırla','Endokrin bezler kanalsızdır; hormonlar kana geçer ve kanla taşınır.','Kanalsız bez → kan'),
   A('Etki özelliklerini sına','Hormon az miktarda etkilidir, yalnız reseptörlü hücreleri etkiler, sinirsel etkiye göre yavaştır.','Dört ifade doğru'),
   A('Yanlış ifadeyi bul','Hormonların özel kanallarla taşınması dış salgı bezlerinin özelliğidir; hormonlar kanla taşınır.','Bu ifade yanlış')],
 tipId='en-genel',z='kolay',alt='Hormonların Genel Özellikleri',kaz='Hormonların salgılanma, taşınma ve etki özelliklerine ilişkin yanlış ifadeyi belirler.',kalip='düz',
 metin='İnsanda hormonlar, vücuttaki iç dengenin korunmasında görev alan kimyasal haberci moleküllerdir. Bu moleküller endokrin bezlerden salgılanır ve vücudun çeşitli bölgelerindeki hücreleri etkiler.\nHormonların özellikleri ve etki biçimleriyle ilgili aşağıdakilerden hangisi yanlıştır?',
 dogru=w3['dogru'],yan=w3['yan'],sira=w3['sira'],istenen='Yanlış olan ifade.',
 ip=['Her ifadeyi hormonların bez–kan–hedef yolculuğuyla karşılaştır.'],bilgi=[BEZ],
 puf='Hormonların bezden hedefe yolculuğunu adım adım düşün.')

# ================ 04 · orta · grafik · kan glikozu · öncüllü
card(4,'Glikoz–hormon grafiği','Glikoz yükselince artan, sonra glikozu azaltan hormon insülindir; bu bir negatif geri bildirimdir.','Glikozu düşüren hormonun karaciğerde glikojeni yıkacağını sanmak; geri bildirimin yönünü karıştırmak.','orta','grafik',4,'en-glikoz','glikoz–hormon grafiğini yorumlama')
g1=ck([(0,4),(0.3,4),(1.5,8),(4.8,4),(8,4)]); x1=ck([(0,1),(0.8,1),(2.5,6),(6.2,1),(8,1)])
SK=pg(f'width=6.6cm,height=5cm,{AXO},xmin=0,xmax=8,ymin=0,ymax=10,xtick={{0,1.5}},xticklabels={{0,$t_1$}},ytick=\\empty,xlabel={{Zaman (yemekten sonra)}},ylabel={{Derişim (göreli)}}',
 f'\\addplot[thick,smooth,no marks] coordinates {{{co(g1)}}};\n\\addplot[thick,dashed,smooth,no marks] coordinates {{{co(x1)}}};\n\\draw[gray,dotted] (axis cs:1.5,0) -- (axis cs:1.5,8);\n\\node[anchor=west] at (axis cs:2.3,8.4) {{Kan glikozu}};\n\\node[anchor=west] at (axis cs:3.6,5.8) {{X hormonu}};')
w4=onc([False,True,False],['X hormonu, glikoz yükselince salgılanıp glikozu azaltan insülindir ve karaciğerde glikojen yıkımını değil sentezini artırır','X hormonunun derişimi, glikoz derişimi yükseldikten sonra artmış ve glikoz azaldıkça düşmüştür','glikozun yükselmesi insülin salgısını artırıp glikozu azaltır; bu, değişimi geri çeviren negatif geri bildirimdir'],1)
q('0004',4,[A('Grafiği oku','Glikoz öğünden sonra yükselmiş, X hormonu da ardından artmış; sonra glikoz azalmıştır.','Glikoz ↑ → X ↑ → glikoz ↓'),
   A('X hormonunu belirle','Glikozu düşürmek üzere salgılanan hormon insülindir; insülin glikojen yıkımını değil sentezini artırır.','X = insülin → I: yanlış'),
   A('II. yargıyı değerlendir','X derişimi glikozun değişimini izlemiştir.','II: doğru'),
   A('III. yargıyı değerlendir','Değişimi azaltan etki negatif geri bildirimdir; pozitif değildir.','III: yanlış'),
   A('Sonuç','Yalnız II yargısı doğrudur.','Yalnız II')],
 tipId='en-glikoz',z='orta',alt='Kan Glikoz Düzeyi',kaz='Kan glikozu ve hormon derişiminin zamanla değişimini yorumlayarak hormonun kimliğini, etkisini ve geri bildirim türünü belirler.',kalip='grafik',
 metin='Sağlıklı bir birey karbonhidrattan zengin bir öğün yedikten sonra alınan kan örneklerinde, kan glikoz derişimi ile pankreastan salgılanan X hormonunun derişimi ölçülüyor. Ölçüm sonuçları grafikte gösterilmiştir.\nBuna göre,\nI. X hormonu, karaciğerde glikojenin yıkımını hızlandırır.\nII. X hormonunun derişimindeki değişim, kan glikoz düzeyindeki değişime bağlı olarak gerçekleşmiştir.\nIII. t₁ anından sonra kan glikozunun azalmasında pozitif geri bildirim rol oynamıştır.\nyargılarından hangileri doğrudur?',
 sekil=SK,dogru=w4['dogru'],yan=w4['yan'],sira=w4['sira'],istenen='Grafiğe göre doğru olan yargılar.',
 ip=['Hangi eğrinin değişimden önce, hangisinin sonra gerçekleştiğine bak; sonra değişimi geri çeviren yönü düşün.'],bilgi=[GLK,GER],
 puf='Grafikte önce hangi eğrinin değiştiğine, sonra diğerinin nasıl yanıt verdiğine bak.')

# ================ 05 · orta · olumsuz · geri bildirim şeması
card(5,'Hipotalamus–hipofiz–tiroit ekseni','Hipotalamus ön hipofizi, ön hipofiz tiroit bezini uyarır; tiroksin artınca ikisini de baskılar (negatif geri bildirim).','Geri dönen oklarda salgının artacağını sanmak; tiroksinin metabolizmayı azalttığını düşünmek.','orta','şekilli',4,'en-geri','tiroit ekseninde numaralı yollar')
b=['\\tikzset{box/.style={draw,rounded corners=3pt,minimum width=2.2cm,minimum height=.9cm,align=center,line width=.9pt},num/.style={draw,circle,fill=white,inner sep=1.4pt,font=\\small\\bfseries}}',
   '\\node[box] (hy) at (0,0) {Hipotalamus};\\node[box] (hf) at (3.4,0) {Ön hipofiz};\\node[box] (ti) at (6.8,0) {Tiroit bezi};\\node[box] (hh) at (10.2,0) {Hedef hücreler};']
for a_,b_,n in (('hy','hf',1),('hf','ti',2),('ti','hh',3)): b.append(f'\\draw[{OK},line width=.9pt] ({a_}.east)--node[num]{{{n}}}({b_}.west);')
b.append(f'\\draw[{OK},line width=.9pt,dashed] (6.4,-.45)--(6.4,-1.15)--(3.4,-1.15)--(3.4,-.45);\\node[num] at (4.9,-1.15) {{4}};')
b.append(f'\\draw[{OK},line width=.9pt,dashed] (7.2,-.45)--(7.2,-1.95)--(0,-1.95)--(0,-.45);\\node[num] at (3.6,-1.95) {{5}};')
SK=tk('\n'.join(b))
o5=[('1 numaralı yoldaki etki, ön hipofizin hormon salgısını denetler.',True,'Doğru bir ifadeyi yanlış sanmış; hipotalamus ön hipofizin salgısını hormonlarla denetler.'),
    ('2 numaralı yoldaki hormon, tiroit bezinin hormon salgısını artırır.',True,'Doğru bir ifadeyi yanlış sanmış; ön hipofizin TSH hormonu tiroit bezini uyarır.'),
    ('3 numaralı yoldaki hormon, hedef hücrelerde bazal metabolizma hızını azaltır.',False,''),
    ('4 numaralı yoldaki etki, ön hipofizin TSH salgısını azaltır.',True,'Doğru bir ifadeyi yanlış sanmış; tiroksin artınca ön hipofizin salgısı negatif geri bildirimle baskılanır.'),
    ('5 numaralı yoldaki etki, hipotalamusun salgısını azaltır.',True,'Doğru bir ifadeyi yanlış sanmış; tiroksin hipotalamus üzerinde de baskılayıcı etki gösterir.')]
w5=tek(o5,False,2)
q('0005',5,[A('Şemayı oku','Düz oklar uyarı yolunu, kesikli oklar tiroit bezinden geri dönen etkileri gösterir.','1, 2, 3: ileri yol · 4, 5: geri dönüş'),
   A('İleri yolu yorumla','Hipotalamus ön hipofizi, ön hipofiz TSH ile tiroit bezini uyarır.','1 ve 2: doğru'),
   A('Hedef etkiyi hatırla','3 numaralı yoldaki hormon tiroksindir; hücrelerde metabolizma hızını artırır.','3: azaltır → yanlış'),
   A('Geri dönüşü yorumla','Tiroksin artınca ön hipofiz ve hipotalamus salgısı baskılanır.','4 ve 5: doğru'),
   A('Sonuç','Yanlış olan ifade 3 numaralı yolla ilgilidir.','3 numaralı yol')],
 tipId='en-geri',z='orta',alt='Negatif Geri Bildirim',kaz='Hipotalamus–hipofiz–tiroit eksenini ve negatif geri bildirim yollarını şema üzerinde yorumlar.',kalip='şekilli',
 metin='Şekilde, insanda tiroit bezinin çalışmasının hipotalamus ve ön hipofiz tarafından düzenlenmesi şematik olarak gösterilmiştir. Düz oklar uyarı yolunu, kesikli oklar ise tiroit bezi salgısının geri dönen etkilerini göstermektedir.\nBuna göre, numaralı yollarla ilgili aşağıdakilerden hangisi yanlıştır?',
 sekil=SK,dogru=w5['dogru'],yan=w5['yan'],sira=w5['sira'],istenen='Yanlış olan ifade.',
 ip=['Düz oklarla kesikli okları ayrı ayrı yorumla; tiroit bezinin hormonunun hem hedef hücrelerdeki hem de geri dönüş yollarındaki etkisini düşün.'],bilgi=[TIR,GER],
 puf='Düz ve kesikli okları ayrı ayrı yorumla.')

# ================ 06 · orta · şekilli · kan glikozu hormonları
card(6,'Glikoz düzenleyici hormonları ayırt etme','Kan glikozu yükselince azaltan, düşünce artıran ve stres hormonu ayrı hormonlardır; etkinin yönü hormonu belirler.','İnsülin ile glukagonun yönlerini ters yazmak; adrenalini pankreas hormonu sanmak.','orta','şekilli',3,'en-glikoz','kan glikozunu değiştiren üç durumda hormon belirleme')
b=['\\tikzset{box/.style={draw,rounded corners=3pt,minimum height=.95cm,align=center,line width=.9pt,text width=2.5cm},bx/.style={box,minimum width=2.6cm},hr/.style={font=\\small\\bfseries}}']
rows=[('Kan glikoz düzeyi artar','Pankreas','K','Kan glikoz düzeyi azalır'),('Kan glikoz düzeyi azalır','Pankreas','L','Kan glikoz düzeyi artar'),('Heyecan ve korku','Böbreküstü bezi','M','Kan glikoz düzeyi artar')]
for i,(a_,g_,h_,r_) in enumerate(rows):
    y=-1.75*i
    b.append(f'\\node[bx] (a{i}) at (0,{y}) {{{a_}}};\\node[bx,minimum width=2.2cm,text width=2.0cm] (g{i}) at (4.6,{y}) {{{g_}}};\\node[bx] (r{i}) at (9.4,{y}) {{{r_}}};')
    b.append(f'\\draw[{OK},line width=.9pt] (a{i}.east)--(g{i}.west);\\draw[{OK},line width=.9pt] (g{i}.east)--node[above,hr]{{{h_}}}(r{i}.west);')
SK=tk('\n'.join(b))
HN={'ins':'insülin','glu':'glukagon','adr':'adrenalin'}
def trio(a_,b_,c_): return f'{HN[a_]} – {HN[b_]} – {HN[c_]}'
dg6=trio('ins','glu','adr')
y6=[(trio('glu','ins','adr'),'Glikozu azaltan K hormonunu glukagon, artıran L hormonunu insülin sanmış; oysa glikozu azaltan insülin, artıran glukagondur.','bilgi'),
    (trio('ins','adr','glu'),'L hormonunu pankreastan salgılanan glukagon yerine adrenalin, M hormonunu böbreküstü bezi yerine glukagon sanmış.','bilgi'),
    (trio('adr','glu','ins'),'Glikozu azaltan K hormonunu adrenalin, M hormonunu insülin sanmış; oysa M böbreküstü bezinden salgılanan adrenalindir.','bilgi'),
    (trio('glu','adr','ins'),'Glikozu azaltan K hormonunu glukagon sanmış ve glikoz azalınca pankreastan salgılanan L hormonunu adrenalin sanmış.','bilgi')]
sr6=[dg6]+[y[0] for y in y6]
q('0006',6,[A('Şemayı oku','Her satırda bir durum, onu yöneten bez ve sonuç verilmiştir.','3 satır: K, L, M'),
   A('K hormonunu bul','Glikoz artınca pankreastan salgılanan ve glikozu azaltan hormon insülindir.','K = insülin'),
   A('L hormonunu bul','Glikoz azalınca pankreastan salgılanan ve glikozu artıran hormon glukagondur.','L = glukagon'),
   A('M hormonunu bul','Heyecan ve korkuda böbreküstü bezinden salgılanan, glikozu artıran hormon adrenalindir.','M = adrenalin'),
   A('Sonuç','Sıra insülin, glukagon, adrenalindir.','insülin – glukagon – adrenalin')],
 tipId='en-glikoz',z='orta',alt='Kan Glikoz Düzeyi',kaz='Kan glikoz düzeyini değiştiren durumları ve sonuçlarını inceleyerek insülin, glukagon ve adrenalini ayırt eder.',kalip='şekilli',
 metin='Şekilde, sağlıklı bir bireyde kan glikoz düzeyini değiştiren üç farklı durum ve bu durumlarda salgılanan K, L ve M hormonları gösterilmiştir. Oklar, hormonu salgılayan yapıyı ve hormonun kan glikoz düzeyi üzerindeki sonucunu belirtmektedir.\nBuna göre, K, L ve M hormonları sırasıyla aşağıdakilerden hangisinde doğru verilmiştir?',
 sekil=SK,dogru=dg6,yan=y6,sira=sr6,istenen='K, L ve M hormonlarının sırasıyla adları.',
 ip=['Her satırda tetikleyici durumla sonucu karşılaştır ve hormonu salgılayan bezin hangisi olduğuna bak.'],bilgi=[GLK],
 puf='Önce hormonun kan glikozunu hangi yönde değiştirdiğine, sonra hangi bezden salgılandığına bak.')

# ================ 07 · orta · sütun grafik · deney
card(7,'Pankreas çıkarma deneyi','Pankreassız grup, sahte ameliyat grubuyla ve özüt verilen grupla karşılaştırılır; yalnız grafikten çıkarılabilen sonuç seçilir.','Deneyin göstermediği mekanizmayı (glikojen yıkımı) sonuç sanmak; ameliyatın etkisini ayırmamak.','orta','grafik',4,'en-glikoz','pankreas deneyinde sonuç çıkarma')
d7=[('K',90),('L',270),('M',100)]
SK=pg('ybar,width=6.4cm,height=5cm,'+AXO+',ymin=0,ymax=300,ytick distance=50,symbolic x coords={K,L,M},xtick=data,bar width=22pt,enlarge x limits=0.3,xlabel={Grup},ylabel={Kan glikozu (mg/100 mL)},ymajorgrids,major grid style={gray!40,thin}',
 '\\addplot[fill=black,fill opacity=.2,draw=black] coordinates {'+' '.join(f'({k},{v})' for k,v in d7)+'};')
o7=[('Pankreas bezi, kan glikoz düzeyini yükselten bir hormon salgılar.',False,'L grubunda pankreas çıkarılınca glikoz yükselmiştir; bu, pankreasın glikozu artıran değil düşüren bir madde salgıladığını gösterir.'),
    ('Ameliyat işleminin kendisi kan glikoz düzeyini artırmıştır.',False,'Sahte ameliyat uygulanan K grubunda glikoz düşük kalmıştır; bu yüzden artış ameliyata değil pankreasın çıkarılmasına bağlıdır.'),
    ('Pankreas bulunmadığında da kan glikoz düzeyi sabit tutulur.',False,'L grubunda glikoz belirgin biçimde yükselmiştir; pankreas olmadan düzen bozulmuştur.'),
    ('Pankreas özütü, karaciğerde glikojen yıkımını hızlandırarak etki eder.',False,'Deney etki mekanizmasını göstermez; özüt glikozu düşürmüştür, glikojen yıkımı ise glikozu artırırdı.'),
    ('Pankreas özütündeki madde, pankreasın yokluğunda yükselen kan glikozunu düşürür.',True,'')]
w7=tek(o7,True,4)
q('0007',7,[A('Grupları tanı','K sahte ameliyatlı kontrol grubudur; L pankreassız, M pankreassız ve özüt almıştır.','K: kontrol · L: pankreas yok · M: pankreas yok + özüt'),
   A('K ile L’yi karşılaştır','Pankreas çıkarılınca glikoz çok yükselmiştir; ameliyat tek başına etki etmemiştir.','90 → 270 mg/100 mL'),
   A('L ile M’yi karşılaştır','Özüt verilen grupta glikoz yeniden normale yakındır.','270 → 100 mg/100 mL'),
   A('Şıkları sına','Yalnız bu üç grup karşılaştırmasıyla desteklenen ifade seçilir; mekanizma bilgisi deneyden çıkmaz.','Desteklenen: özütteki madde glikozu düşürür'),
   A('Sonuç','Özütteki madde, yükselen glikozu düşürmüştür.','Pankreas özütü etkisi')],
 tipId='en-glikoz',z='orta',alt='Deney Yorumlama',kaz='Pankreas çıkarma ve özüt verme deneyinin sonuçlarını kontrol grubuyla karşılaştırarak yorumlar.',kalip='grafik',
 metin='Aynı türden, eşit kütleli ve aynı yaştaki hayvanlar üç gruba ayrılıyor. K grubuna sahte ameliyat uygulanıyor (pankreas yerinde bırakılıyor). L grubunun pankreası çıkarılıyor. M grubunun pankreası çıkarılıyor ve bu gruba her gün pankreas adacıklarından hazırlanmış özüt enjekte ediliyor. Bütün gruplar aynı koşullarda beslendikten beş gün sonra ölçülen kan glikoz düzeyleri grafikte verilmiştir.\nBuna göre, deneyin sonuçlarıyla ilgili aşağıdakilerden hangisi söylenebilir?',
 sekil=SK,dogru=w7['dogru'],yan=w7['yan'],sira=w7['sira'],istenen='Deney sonuçlarından çıkarılabilecek sonuç.',
 ip=['Her iddiayı grafikteki iki grubun karşılaştırmasıyla destekleyip destekleyemediğine bak.'],bilgi=[DEN],
 puf='Deneyden yalnız karşılaştırılan gruplardaki farkın gösterdiği sonuç çıkarılır; mekanizma bilgisi deneyden gelmez.')

# ================ 08 · orta · hipotalamus–hipofiz şeması · öncüllü
card(8,'Hipotalamus–hipofiz bağlantıları','Hipotalamus ön hipofizi hormonlarla, arka hipofizi sinir uzantılarıyla bağlar; arka hipofizin hormonları hipotalamusta sentezlenir.','Arka hipofizin hormonlarını kendi hücrelerinde sentezlediğini sanmak.','orta','öncüllü',5,'en-hipo','hipotalamus–hipofiz şemasında yolları yorumlama')
b=['\\draw[line width=1.1pt,fill=black,fill opacity=.08] (0,3.3) ellipse (1.6 and .6); \\draw[line width=1.1pt] (0,3.3) ellipse (1.6 and .6);',
   '\\node at (0,3.3) {Hipotalamus};',
   '\\draw[line width=1.1pt,fill=black,fill opacity=.08] (-.85,1.35) ellipse (.85 and .6); \\draw[line width=1.1pt] (-.85,1.35) ellipse (.85 and .6);',
   '\\draw[line width=1.1pt,fill=black,fill opacity=.08] (.55,1.35) ellipse (.5 and .52); \\draw[line width=1.1pt] (.55,1.35) ellipse (.5 and .52);',
   f'\\draw[{OK},line width=.9pt] (-1.0,2.72)--node[left,font=\\small\\bfseries]{{a}}(-1.0,1.97);',
   f'\\draw[{OK},line width=.9pt,dashed] (.75,2.72)--node[right,font=\\small\\bfseries]{{b}}(.75,1.85);',
   f'\\node[draw,rounded corners=3pt,minimum width=2.1cm,minimum height=.8cm,line width=.9pt] (ti) at (-1.7,-.6) {{Tiroit bezi}};\\node[draw,rounded corners=3pt,minimum width=2.4cm,minimum height=.8cm,line width=.9pt] (bo) at (1.9,-.6) {{Böbrek tüpleri}};',
   f'\\draw[{OK},line width=.9pt] (-1.2,.75)--node[left,font=\\small\\bfseries]{{c}}(-1.5,-.2);\\draw[{OK},line width=.9pt] (.7,.83)--node[right,font=\\small\\bfseries]{{d}}(1.6,-.2);',
   '\\node[draw,circle,inner sep=1.6pt,font=\\small\\bfseries] at (-3.1,3.3) {1};\\draw[line width=.8pt] (-2.85,3.3)--(-1.6,3.3);',
   '\\node[draw,circle,inner sep=1.6pt,font=\\small\\bfseries] at (-3.1,1.35) {2};\\draw[line width=.8pt] (-2.85,1.35)--(-1.7,1.35);\\node[anchor=east,font=\\small] at (-3.4,1.35) {Ön hipofiz};',
   '\\node[draw,circle,inner sep=1.6pt,font=\\small\\bfseries] at (2.5,1.35) {3};\\draw[line width=.8pt] (2.25,1.35)--(1.05,1.35);\\node[anchor=west,font=\\small] at (2.85,1.35) {Arka hipofiz};']
SK=tk('\n'.join(b))
w8=onc([True,True,False],['a yolu ile hipotalamustan ön hipofize ulaşan hormonlar, ön hipofizin hormon salgısını düzenler','c yolundaki hormon TSH’dir ve tiroit bezinin tiroksin salgısını uyarır','d yolundaki hormon ADH’dir; ADH arka hipofizde depolanıp salgılanır, ancak hipotalamusta sentezlenir'],2)
q('0008',8,[A('Şemayı oku','a ve b hipotalamusun hipofiz lobları ile bağlantılarıdır; c ve d lobların hedeflerine giden hormon yollarıdır.','a, b: hipotalamus çıkışı · c, d: hedefe giden hormon'),
   A('I. yargıyı değerlendir','Hipotalamus, ön hipofizin hormon salgısını hormonlarla denetler.','I: doğru'),
   A('II. yargıyı değerlendir','Ön hipofizden tiroit bezine giden hormon TSH’dir ve tiroksin salgısını uyarır.','II: doğru'),
   A('III. yargıyı değerlendir','Böbrek tüplerine giden hormon ADH’dir; arka hipofiz onu depolar, sentez hipotalamusta olur.','III: yanlış'),
   A('Sonuç','I ve II yargıları doğrudur.','I ve II')],
 tipId='en-hipo',z='orta',alt='Hipotalamus ve Hipofiz',kaz='Hipotalamus–hipofiz şemasında hormon yollarını ve hormonların sentez yerlerini yorumlar.',kalip='öncüllü',
 metin='Şekilde, insanda hipotalamus ile hipofizin iki lobu ve bu yapıların hormonlarıyla etkilediği bazı hedefler şematik olarak gösterilmiştir.\nBuna göre,\nI. a yolu ile hipotalamustan gelen hormonlar, 2 numaralı yapının hormon salgısını düzenler.\nII. c yolu ile taşınan hormon, tiroit bezinin hormon salgısını uyarır.\nIII. d yolu ile taşınan hormon, 3 numaralı yapının hücrelerinde sentezlenir.\nyargılarından hangileri doğrudur?',
 sekil=SK,dogru=w8['dogru'],yan=w8['yan'],sira=w8['sira'],istenen='Şemaya göre doğru olan yargılar.',
 ip=['Her yolun hedefine bak ve oraya ulaşan hormonun hangisi olduğunu, nerede sentezlenip nerede salgılandığını düşün.'],bilgi=[HIP],
 puf='Her yolun hedefini ve taşıdığı hormonun kimliğini belirleyip yargıyla karşılaştır.')

# ================ 09 · orta · sinirsel ve hormonal düzenleme · öncüllü
card(9,'Sinirsel ve hormonal düzenleme','Hormonlar kanla taşındığından etkileri geç başlar ve uzun sürer; hipotalamus nöron yapısında olduğu hâlde hormon salgılar; hedef hücre reseptöre bağlıdır.','Hipotalamusun hormon salgılayamayacağını sanmak; hormonların her hücreyi etkilediğini düşünmek.','orta','öncüllü',3,'en-genel','sinirsel–hormonal düzenleme karşılaştırması')
w9=onc([True,False,True],['hormonlar kanla taşındığı için vücudun birçok bölgesindeki hedef hücrelere aynı anda ulaşabilir','hipotalamus sinir sisteminin bir parçası olmakla birlikte hormon salgılar ve endokrin sistemi sinir sistemine bağlar','bir hormonun yalnız belirli hücreleri etkilemesi, o hücrelerde hormona özgü reseptörlerin bulunmasına bağlıdır'],3)
q('0009',9,[A('I. yargıyı değerlendir','Hormonlar kanla taşındığı için birçok bölgedeki hedef hücrelere aynı anda ulaşabilir.','I: doğru'),
   A('II. yargıyı değerlendir','Hipotalamus hem sinir sistemine ait hem de hormon salgılayan bir yapıdır.','II: yanlış'),
   A('III. yargıyı değerlendir','Hormon yalnız özgün reseptörü olan hücrelerde etki eder.','III: doğru'),
   A('Sonuç','I ve III yargıları doğrudur.','I ve III')],
 tipId='en-genel',z='orta',alt='Sinirsel ve Hormonal Düzenleme',kaz='Sinir sistemi ile hormonal sistemin çalışma özelliklerini karşılaştırır ve hormon–reseptör ilişkisini yorumlar.',kalip='öncüllü',
 metin='İnsanda iç dengenin korunması, sinir sistemi ile hormonal sistemin birlikte çalışmasıyla sağlanır. Bu iki sistemin çalışma biçimleriyle ilgili,\nI. Bir hormon, kan yoluyla vücudun birçok bölgesindeki hedef hücreleri aynı anda etkileyebilir.\nII. Hipotalamus, sinir sisteminin bir parçası olduğu için hormon salgılayamaz.\nIII. Bir hormonun yalnız belirli hücreleri etkilemesi, o hücrelerde hormona özgü reseptörlerin bulunmasına bağlıdır.\nyargılarından hangileri doğrudur?',
 dogru=w9['dogru'],yan=w9['yan'],sira=w9['sira'],istenen='Doğru olan yargılar.',
 ip=['Her yargıyı, hormonların taşınma yolu ve hedef hücrelerdeki etkisi açısından ayrı ayrı sına.'],bilgi=[ORT],
 puf='Her yargıyı ayrı ayrı sına; iki sistemin çalışma biçimini karşılaştır.')

# ================ 10 · orta · olumsuz · adrenalin
card(10,'Adrenalinin etkileri','Adrenalin stres anında kalp ve solunum hızını artırır, karaciğerde glikojen yıkımını hızlandırarak kan glikozunu yükseltir.','Adrenalinin glikoz depolayacağını sanmak; glikojen sentezi ile yıkımını karıştırmak.','orta','hikâyeli',3,'en-bez','adrenalinin etkileri (beklenmeyen)')
o10=[('Kalp atış hızının artması',True,'Beklenen bir etkiyi beklenmeyen sanmış; adrenalin kalp atış hızını artırır.'),
     ('Solunum hızının artması',True,'Beklenen bir etkiyi beklenmeyen sanmış; adrenalin solunum hızını da artırır.'),
     ('Karaciğerde glikojenin glikoza dönüşümünün hızlanması',True,'Beklenen bir etkiyi beklenmeyen sanmış; adrenalin glikojen yıkımını hızlandırır.'),
     ('Karaciğerde glikozun glikojene dönüşümünün hızlanması',False,''),
     ('Kan glikoz düzeyinin yükselmesi',True,'Beklenen bir etkiyi beklenmeyen sanmış; glikojen yıkımı sonucu kan glikozu yükselir.')]
w10=tek(o10,False,3)
q('0010',10,[A('Durumu yorumla','Sınav heyecanı sinirsel uyarıyla böbreküstü medullasından adrenalin salgısını artırır.','Adrenalin ↑'),
   A('Adrenalinin etkilerini hatırla','Adrenalin kalp ve solunum hızını artırır, karaciğerde glikojeni glikoza çevirir.','Kalp ↑ · solunum ↑ · glikojen yıkımı ↑'),
   A('Sonucu çıkar','Glikojen yıkımı hızlanınca kan glikozu yükselir.','Kan glikozu ↑'),
   A('Beklenmeyeni bul','Glikozun glikojene dönüşümü insülinin etkisidir; adrenalin bunun tersini yapar.','Beklenmez: glikojen sentezi')],
 tipId='en-bez',z='orta',alt='Adrenalin',kaz='Adrenalin salgısı arttığında vücutta beklenen ve beklenmeyen değişiklikleri ayırt eder.',kalip='hikâyeli',
 metin='Önemli bir sınava girmeden önce çok heyecanlanan sağlıklı bir bireyde, sinirsel uyarı sonucu böbreküstü bezinin medullasından adrenalin salgısı artıyor.\nBu bireyle ilgili aşağıdakilerden hangisinin gerçekleşmesi beklenmez?',
 dogru=w10['dogru'],yan=w10['yan'],sira=w10['sira'],istenen='Gerçekleşmesi beklenmeyen değişiklik.',
 ip=['Adrenalinin kalp, solunum ve karaciğerdeki etkilerini düşün; hangi seçeneğin karaciğerde ters yönde bir olay olduğuna bak.'],bilgi=[BOB],
 puf='Adrenalinin karaciğerdeki etkisini düşün.')

# ================ 11 · orta · ADH
card(11,'Terleme ve ADH','Kanın ozmotik derişimi artınca ozmoreseptörler uyarılır, ADH salgısı artar, böbrek tüplerinde su geri emilimi artar, idrar derişik ve az olur.','ADH’yi böbreküstü bezinden sanmak; ADH artınca idrarın seyreleceğini düşünmek.','orta','hikâyeli',4,'en-hipo','terleme sonrası ADH ve idrar')
o11=[('Arka hipofizden ADH salgısı artar ve böbrek tüplerinde su geri emilimi artar.',True,''),
     ('Hipotalamus uyarılır ve böbrek tüplerinde su geri emilimi azalır.',False,'Hipotalamusun uyarıldığını doğru bulmuş; ancak ADH artınca su geri emilimi azalmaz, artar.'),
     ('ADH salgısı azalır ve oluşan idrar seyrelir.',False,'Derişim arttığında ADH salgısının azalacağını sanmış; oysa su tutulması gerektiğinden ADH artar.'),
     ('Böbreküstü bezinden ADH salgısı artar ve idrar miktarı artar.',False,'ADH’yi böbreküstü bezine bağlamış; ADH böbreküstü bezinden değil, arka hipofizden salgılanır.'),
     ('Arka hipofizden ADH salgısı azalır ve idrarın ozmotik derişimi artar.',False,'ADH azalınca idrarın derişik olmayacağını gözden kaçırmış; ADH azalırsa su kaybı artar ve idrar seyrelir.')]
w11=tek(o11,True,0)
q('0011',11,[A('Durumu yorumla','Terleme su kaybettirir; kanın ozmotik derişimi artar.','Ozmotik derişim ↑'),
   A('Algılayıcıları düşün','Hipotalamustaki ozmoreseptörler uyarılır ve arka hipofizden ADH salgısı artar.','ADH ↑'),
   A('Böbrek etkisini bul','ADH, böbrek tüplerinden suyun geri emilimini artırır; vücut su tutar.','Su geri emilimi ↑'),
   A('İdrarı yorumla','Su tutulduğu için idrar miktarı azalır ve derişik hâle gelir.','İdrar az ve derişik'),
   A('Sonuç','Arka hipofizden ADH artar, su geri emilimi artar.','ADH ↑ · su geri emilimi ↑')],
 tipId='en-hipo',z='orta',alt='ADH ve Su Dengesi',kaz='Kanın ozmotik derişimi arttığında ADH salgısındaki ve böbrek tüplerindeki değişimleri yorumlar.',kalip='hikâyeli',
 metin='Sıcak bir günde uzun süre su içmeden spor yapan sağlıklı bir bireyde terleme nedeniyle kanın ozmotik derişimi artıyor.\nBu bireyin vücudunda gerçekleşen değişikliklerle ilgili aşağıdakilerden hangisi doğrudur?',
 dogru=w11['dogru'],yan=w11['yan'],sira=w11['sira'],istenen='Doğru olan ifade.',
 ip=['Ozmotik derişimin artması hangi algılayıcıları uyarır; vücut su kaybını azaltmak için hangi hormonu ve hangi yapıyı kullanır?'],bilgi=[OZM],
 puf='Ozmotik derişimdeki değişimin hangi algılayıcıyı ve hormonu devreye soktuğunu sırayla izle.')

# ================ 12 · orta · büyüme hormonu
card(12,'Yetişkinde büyüme hormonu fazlalığı','Büyüme çağı bittikten sonra büyüme hormonu fazlalığında boy uzamaz; el, ayak ve çene gibi kemikler kalınlaşıp büyür (akromegali).','Fazlalığı her yaşta devlikle özdeşleştirmek.','orta','hikâyeli',3,'en-bez','büyüme hormonu fazlalığının sonucu')
o12=[('Boy uzunluğunda belirgin artış',False,'Çocukluktaki fazlalığın sonucunu (devlik) yetişkine uygulamış; büyüme çağı bittiğinden uzun kemikler boyuna uzamaz.'),
     ('El, ayak ve çene kemiklerinde kalınlaşma ve büyüme',True,''),
     ('Bazal metabolizma hızında belirgin azalma',False,'Büyüme hormonunu tiroksinle karıştırmış; metabolizma hızını düzenleyen hormon tiroksindir.'),
     ('Böbreklerde su geri emiliminin artması ve idrarın derişmesi',False,'Büyüme hormonunu ADH ile karıştırmış; su geri emilimini düzenleyen hormon ADH’dir.'),
     ('Vücut oranları korunarak cüce kalma',False,'Cüceliği hormonun fazlalığı sanmış; oysa cücelik çocuklukta büyüme hormonunun yetersizliğinde görülür.')]
w12=tek(o12,True,1)
q('0012',12,[A('Durumu yorumla','Birey yetişkindir; büyüme çağı tamamlanmış ve uzun kemiklerin büyüme plakları kapanmıştır.','Yetişkin + fazla hormon'),
   A('Boy artışını ele','Plaklar kapandığı için kemikler boyuna uzamaz; devlik çocukluk dönemi durumudur.','Boy artışı: beklenmez'),
   A('Diğer hormonları ayır','Metabolizma hızı tiroksinle, su geri emilimi ADH ile ilgilidir.','Tiroksin ve ADH dışı'),
   A('Kemik etkisini bul','Büyüme hormonu el, ayak ve çene gibi kemiklerde kalınlaşma ve büyümeye yol açar.','Akromegali'),
   A('Sonuç','Beklenen sonuç, el, ayak ve çene kemiklerinin büyümesidir.','El, ayak, çene')],
 tipId='en-bez',z='orta',alt='Büyüme Hormonu',kaz='Büyüme çağı sonrasında büyüme hormonu fazlalığının sonuçlarını belirler.',kalip='hikâyeli',
 metin='Büyüme çağını tamamlamış sağlıklı bir yetişkinde, ön hipofizdeki bir tümör nedeniyle büyüme hormonu salgısı uzun süre normalin üzerinde kalıyor.\nBu bireyde aşağıdakilerden hangisinin görülmesi beklenir?',
 dogru=w12['dogru'],yan=w12['yan'],sira=w12['sira'],istenen='Bireyde beklenen sonuç.',
 ip=['Bireyin yaşını ve büyüme çağını tamamlamış olmasını düşün; hangi dokular hormona hâlâ yanıt verebilir?'],bilgi=[GH],
 puf='Hormonun etkisini bireyin büyüme durumuyla birlikte değerlendir.')

# ================ 13 · orta · pozitif geri bildirim şeması · öncüllü
card(13,'Doğumda oksitosin döngüsü','Döngüdeki her adımın bir sonrakini nasıl etkilediği okunarak geri bildirimin türü belirlenir.','Her geri bildirimi negatif sanmak.','orta','şekilli',3,'en-geri','oksitosinde pozitif geri bildirim şeması')
b=['\\tikzset{box/.style={draw,rounded corners=3pt,minimum height=1.0cm,align=center,line width=.9pt,text width=3.7cm}}',
   '\\node[box] (a) at (0,0) {Bebeğin baskısıyla rahim ağzı gerilir};\\node[box] (b) at (5.6,0) {Sinirsel uyarı\\\\hipotalamusa iletilir};',
   '\\node[box] (c) at (5.6,-2.3) {Arka hipofizden kana oksitosin verilir};\\node[box] (d) at (0,-2.3) {Rahim kasları kasılır};',
   f'\\draw[{OK},line width=.9pt] (a.east)--(b.west);\\draw[{OK},line width=.9pt] (b.south)--(c.north);\\draw[{OK},line width=.9pt] (c.west)--(d.east);\\draw[{OK},line width=.9pt] (d.north)--(a.south);']
SK=tk('\n'.join(b))
w13=onc([False,False,True],['şekildeki mekanizmada kasılmanın artması gerilmeyi, gerilme de oksitosin salgısını artırır; bu, pozitif geri bildirimdir','oksitosin hormondur ve rahim kaslarına sinir uzantılarıyla değil, kan yoluyla ulaşır','oksitosin salgısı arttıkça rahim kaslarının kasılması da artar'],1)
q('0013',13,[A('Şemayı oku','Gerilme sinirsel uyarıya, uyarı oksitosin salgısına, oksitosin kasılmaya, kasılma yeniden gerilmeye yol açar.','Gerilme → oksitosin → kasılma → gerilme'),
   A('I. yargıyı değerlendir','Döngü, değişimi azaltmaz; artırır. Bu pozitif geri bildirimdir, negatif değil.','I: yanlış'),
   A('II. yargıyı değerlendir','Oksitosin bir hormondur; kana verilir ve kanla rahim kaslarına taşınır.','II: yanlış'),
   A('III. yargıyı değerlendir','Şemada oksitosin kası kasıyor; salgı arttıkça kasılma da artar.','III: doğru'),
   A('Sonuç','Yalnız III yargısı doğrudur.','Yalnız III')],
 tipId='en-geri',z='orta',alt='Pozitif Geri Bildirim',kaz='Doğumda oksitosin döngüsünü şemadan yorumlayarak geri bildirimin türünü ve hormonun taşınma yolunu belirler.',kalip='öncüllü',
 metin='Şekilde, doğum eyleminde rahim kaslarının kasılmasını düzenleyen mekanizma şematik olarak gösterilmiştir.\nBuna göre,\nI. Şekildeki mekanizma negatif geri bildirime örnektir.\nII. Oksitosin, rahim kaslarına sinir uzantıları aracılığıyla ulaşır.\nIII. Oksitosin salgısı arttıkça rahim kaslarının kasılması da artar.\nyargılarından hangileri doğrudur?',
 sekil=SK,dogru=w13['dogru'],yan=w13['yan'],sira=w13['sira'],istenen='Şemaya göre doğru olan yargılar.',
 ip=['Oklarla halkayı tamamla ve her adımın bir önceki adımın etkisini artırıp azalttığına bak.'],bilgi=[GER],
 puf='Oklarla halkayı tamamlayıp her adımın etkisinin yönünü izle.')

# ================ 14 · orta · antagonist çift
card(14,'Zıt etkili hormon çiftleri','Antagonist hormonlar aynı kan değerini birbirine zıt yönde değiştirir.','Aynı yönde etkili hormonları zıt sanmak.','orta','düz',3,'en-genel','antagonist hormon çifti')
o14=[('Adrenalin – glukagon',False,'Her iki hormon da kan glikozunu artırır; aynı yönde etkili hormonlar birbirine zıt değildir.'),
     ('Büyüme hormonu – tiroksin',False,'İkisi de büyüme ve gelişmeyi destekler; farklı değerleri etkilediklerinden zıt çift sayılmaz.'),
     ('Kalsitonin – parathormon',True,''),
     ('Adrenalin – tiroksin',False,'İkisi de kalp atışını ve metabolizmayı hızlandırır; aynı yönde etkilidirler.'),
     ('ADH – oksitosin',False,'İkisi de arka hipofizden salgılanır ve farklı görevleri vardır; aynı değer üzerinde zıt etki göstermezler.')]
w14=tek(o14,True,2)
q('0014',14,[A('Zıt etkiyi tanımla','Zıt (antagonist) hormonlar aynı kan değerini birbirine ters yönde değiştirir.','Aynı değer, ters yön'),
   A('Aynı yönlüleri ele','Adrenalin–glukagon glikozu, adrenalin–tiroksin kalp hızını artırır; büyüme hormonu–tiroksin ve ADH–oksitosin farklı değerlerle ilgilidir.','Bu çiftler eleniyor'),
   A('Kalan çifti sına','Kalsitonin kan kalsiyumunu azaltır, parathormon artırır.','Kalsiyum: ↓ ve ↑'),
   A('Sonuç','Zıt etkili çift kalsitonin ve parathormondur.','Kalsitonin – parathormon')],
 tipId='en-genel',z='orta',alt='Zıt Etkili Hormonlar',kaz='Aynı değeri zıt yönde etkileyen hormon çiftini belirler.',kalip='düz',
 metin='Vücutta bazı hormon çiftleri, kanda ölçülen aynı değeri birbirine zıt yönde değiştirerek iç dengenin korunmasını sağlar. Bu çiftlerde bir hormon değeri artırırken diğeri aynı değeri azaltır.\nAşağıdaki hormon çiftlerinden hangisi birbirine zıt etki gösterir?',
 dogru=w14['dogru'],yan=w14['yan'],sira=w14['sira'],istenen='Zıt etkili hormon çifti.',
 ip=['Her çiftte iki hormonun etkilediği kan değerini ve etki yönünü ayrı ayrı yaz, sonra karşılaştır.'],bilgi=[CAL],
 puf='Zıt hormonları bulmak için ikisinin etkilediği ortak değeri ve yönünü karşılaştır.')

# ================ 15 · zor · grafik · geri bildirim · öncüllü
card(15,'Tiroksin ilacı ve TSH','Dışarıdan tiroksin verilince TSH salgısı baskılanır, tiroit etkinliği azalır; ilaç bırakılınca TSH artar ve tiroit yeniden çalışır.','Dışarıdan hormon verilince salgının artacağını sanmak; ilaç sonrası toparlanmayı atlamak.','zor','grafik',5,'en-geri','tiroksin ilacı sırasında TSH–tiroksin grafiği')
tk_=ck([(0,4),(1,4),(1.7,10),(5,10),(5.8,2.5),(7.3,4),(9,4)]); ts_=ck([(0,6),(1,6),(2.2,2),(5,2),(6.0,8),(7.6,6),(9,6)])
SK=pg(f'width=6.8cm,height=5.2cm,{AXO},xmin=0,xmax=9,ymin=0,ymax=12.5,xtick={{1,2.2,5,7.6}},xticklabels={{$t_1$,$t_2$,$t_3$,$t_4$}},ytick=\\empty,xlabel={{Zaman}},ylabel={{Derişim (göreli)}}',
 f'\\addplot[thick,smooth,no marks] coordinates {{{co(tk_)}}};\n\\addplot[thick,dashed,smooth,no marks] coordinates {{{co(ts_)}}};\n\\node[anchor=south] at (axis cs:3.5,10.3) {{Tiroksin}};\n\\node[anchor=north] at (axis cs:3.5,1.8) {{TSH}};')
w15=onc([False,True,True],['t₁–t₃ aralığında TSH derişimi düşmüştür; yani ön hipofizin TSH salgısı artmamış, azalmıştır','t₃ anından sonra TSH artmış ve tiroksin yeniden yükselmiştir; bu, tiroit bezinin etkinliğinin artmasını gösterir','tiroksin artınca TSH azalmış, tiroksin azalınca TSH artmıştır; bu, negatif geri bildirimle açıklanır'],3)
q('0015',15,[A('Grafiği oku','Tiroksin ilaçla yükselince TSH düşmüş; ilaç bırakılınca tiroksin düşmüş ve TSH yükselmiştir.','İlaç: tiroksin ↑, TSH ↓ · bırakınca: TSH ↑'),
   A('I. yargıyı değerlendir','t₁–t₃ arasında TSH azalmıştır; salgısı artmamıştır.','I: yanlış'),
   A('II. yargıyı değerlendir','t₃ sonrasında artan TSH tiroit bezini uyarır; tiroksin yeniden normale yükselir.','II: doğru'),
   A('III. yargıyı değerlendir','Tiroksin artınca TSH baskılanması negatif geri bildirimdir.','III: doğru'),
   A('Sonuç','II ve III yargıları doğrudur.','II ve III')],
 tipId='en-geri',z='zor',alt='Negatif Geri Bildirim',kaz='Dışarıdan tiroksin verilmesi ve kesilmesi sırasında tiroksin ve TSH derişimlerini negatif geri bildirimle yorumlar.',kalip='grafik',
 metin='Sağlıklı bir bireye t₁ anında dışarıdan tiroksin içeren bir ilaç verilmeye başlanıyor ve ilaç t₃ anında bırakılıyor. Bireyin kanındaki tiroksin ve TSH derişimlerinin zamanla değişimi grafikte verilmiştir.\nBuna göre,\nI. t₁–t₃ aralığında ön hipofizin TSH salgısı artmıştır.\nII. t₃ anından sonra tiroit bezinin etkinliği artmıştır.\nIII. Grafikteki değişimler negatif geri bildirim mekanizmasıyla açıklanabilir.\nyargılarından hangileri doğrudur?',
 sekil=SK,dogru=w15['dogru'],yan=w15['yan'],sira=w15['sira'],istenen='Grafiğe göre doğru olan yargılar.',
 ip=['İlaç alınırken ve bırakıldıktan sonra iki eğrinin zıt yönlü değişimini ayrı ayrı yorumla.'],bilgi=[TIR,GER],
 puf='Önce iki eğrinin yönünü oku, sonra yargıyı sına.')

# ================ 16 · zor · olumsuz · kalsiyum grafiği
card(16,'Kalsiyum yüklemesi ve iki hormon','Kan kalsiyumu artınca kalsitonin artar, parathormon azalır; beklenmeyen sonuç kemikten kana kalsiyum geçişinin artmasıdır.','Hormonları grafikten ayırt edememek; parathormonun etkisini kalsitoninle karıştırmak.','zor','grafik',5,'en-ca','kalsiyum yüklemesinde hormon grafiği (olumsuz)')
k_=ck([(0,9),(1,9),(1.4,12),(2.6,12),(5.2,9),(7,9)]); x_=ck([(0,2),(1,2),(2.5,6),(5,2),(7,2)]); y_=ck([(0,6),(1,6),(2.5,2),(5,6),(7,6)])
SK=pg(f'width=6.8cm,height=5.2cm,{AXO},xmin=0,xmax=8,ymin=0,ymax=13.5,xtick={{1,5}},xticklabels={{$t_1$,$t_3$}},ytick=\\empty,xlabel={{Zaman}},ylabel={{Derişim (göreli)}}',
 f'\\addplot[thick,smooth,no marks] coordinates {{{co(k_)}}};\n\\addplot[thick,dashed,smooth,no marks] coordinates {{{co(x_)}}};\n\\addplot[thick,dotted,smooth,no marks] coordinates {{{co(y_)}}};\n\\node[anchor=south west] at (axis cs:2.9,12.1) {{Kan kalsiyumu}};\n\\node[anchor=west] at (axis cs:7.05,2) {{X}};\n\\node[anchor=west] at (axis cs:7.05,6) {{Y}};')
o16=[('Kemik dokusundan kana kalsiyum geçişi artar.',False,''),
     ('Kemik dokusunda kalsiyum depolanması artar.',True,'Beklenen bir değişimi beklenmeyen sanmış; kalsiyum yükselince kalsitonin kalsiyumun kemikte depolanmasını artırır.'),
     ('Paratiroit bezlerinin salgısı azalır.',True,'Beklenen bir değişimi beklenmeyen sanmış; kan kalsiyumu yükselince parathormon salgısı azalır.'),
     ('Böbrek tüplerinde kalsiyumun geri emilimi azalır.',True,'Beklenen bir değişimi beklenmeyen sanmış; parathormon azalınca kalsiyumun geri emilimi de azalır.'),
     ('Kan kalsiyum düzeyi, tiroit bezinin salgısı artarak düşürülür.',True,'Beklenen bir değişimi beklenmeyen sanmış; yükselen kalsiyumu kalsitonin düşürür.')]
w16=tek(o16,False,0)
q('0016',16,[A('Grafiği oku','Kalsiyum t₁’de yükselmiş ve sonra normale dönmüştür; X artmış, Y azalmıştır.','Ca ↑ · X ↑ · Y ↓'),
   A('Hormonları belirle','Kalsiyum artınca artan X kalsiyumu düşüren kalsitonindir (tiroit); azalan Y parathormondur (paratiroit).','X = kalsitonin · Y = parathormon'),
   A('Beklenenleri çıkar','Kalsitonin artınca kemikte depolanma artar; parathormon azalınca kemikten kana geçiş ve böbrekte geri emilim azalır.','Depolama ↑ · kana geçiş ↓ · geri emilim ↓'),
   A('Beklenmeyeni bul','Kemikten kana kalsiyum geçişinin artması parathormonun etkisidir; Y azaldığı için bu beklenmez.','Beklenmez: kemikten kana geçiş ↑'),
   A('Sonuç','Gerçekleşmesi beklenmeyen olay kemikten kana kalsiyum geçişinin artmasıdır.','Kemikten kana geçiş')],
 tipId='en-ca',z='zor',alt='Kan Kalsiyum Düzeyi',kaz='Kalsiyum yüklemesi sonrası kalsitonin ve parathormon değişimlerini grafikten belirleyerek beklenmeyen sonucu bulur.',kalip='grafik',
 metin='Sağlıklı bir bireyin damarına t₁ anında hızlı biçimde kalsiyum çözeltisi veriliyor. Bireyin kan kalsiyum derişimi ile iki hormonun (X ve Y) kandaki derişimlerinin zamanla değişimi grafikte gösterilmiştir. Bu hormonlardan biri tiroit bezi, diğeri paratiroit bezi tarafından salgılanmaktadır.\nBuna göre, t₁–t₃ aralığında aşağıdakilerden hangisinin gerçekleşmesi beklenmez?',
 sekil=SK,dogru=w16['dogru'],yan=w16['yan'],sira=w16['sira'],istenen='Gerçekleşmesi beklenmeyen olay.',
 ip=['Kalsiyum yükseldikten sonra hangi eğrinin arttığına, hangisinin azaldığına bakarak hormonları ayır; ardından her olayı o hormonun etkisiyle karşılaştır.'],bilgi=[CAL],
 puf='Önce eğrilerin yönünü oku, sonra hormonları kimlikle eşleştir.')

# ================ 17 · zor · tablo · hipofiz çıkarma deneyi · öncüllü
card(17,'Hipofiz çıkarma ve TSH verme deneyi','Hipofizsiz grup, kontrol ve TSH verilen grupla karşılaştırılarak tiroit bezinin hipofiz hormonuna bağımlılığı yorumlanır.','Tiroksinin tiroit bezini uyardığını sanmak; ölçümleri gruplar arası karşılaştırmadan yorumlamak.','zor','tablo',5,'en-geri','hipofiz deneyinde tablo yorumlama')
SK=tablo_svg(['Grup','Uygulama','Tiroit kütlesi (mg)','Kan tiroksini'],[['K','Sahte ameliyat','20','8'],['L','Hipofiz çıkarıldı','8','2'],['M','Hipofiz çıkarıldı + TSH','20','8']])
w17=onc([True,False,True],['hipofizi çıkarılan L grubunda kan tiroksini azalmış, TSH verilen M grubunda ise K grubu düzeyine dönmüştür','tiroit bezini uyaran hormon tiroksin değil, hipofizden salgılanan TSH’dir; M grubundaki yanıt TSH’nin etkisini gösterir','L grubunda tiroit kütlesinin azalması, tiroit bezinin çalışması için hipofiz hormonuna gereksinim olduğunu gösterir'],2)
q('0017',17,[A('Grupları tanı','K sahte ameliyatlı, L hipofizsiz, M hipofizsiz ve TSH verilen gruptur.','K: hipofiz var · L: hipofiz yok · M: hipofiz yok + TSH'),
   A('I. yargıyı değerlendir','Hipofiz çıkarılınca kan tiroksini düşmüş; TSH ile K düzeyine dönmüştür.','I: doğru'),
   A('II. yargıyı değerlendir','M grubundaki yanıt, tiroit bezini uyaran hormonun tiroksin değil TSH olduğunu gösterir.','II: yanlış'),
   A('III. yargıyı değerlendir','Hipofizsiz grupta tiroit küçülmüş; bezin işlevi hipofiz hormonuna bağlıdır.','III: doğru'),
   A('Sonuç','I ve III yargıları doğrudur.','I ve III')],
 tipId='en-geri',z='zor',alt='Deney Yorumlama',kaz='Hipofiz çıkarma ve TSH verme deneyinin sonuçlarını tablodan yorumlayarak hipofiz–tiroit ilişkisini değerlendirir.',kalip='tablo',
 metin='Aynı yaş ve kütledeki fareler üç gruba ayrılıyor. K grubuna sahte ameliyat uygulanıyor (hipofiz yerinde bırakılıyor). L grubunun hipofizi çıkarılıyor. M grubunun hipofizi çıkarılıyor ve bu gruba her gün ön hipofiz hormonu olan TSH enjekte ediliyor. Bütün gruplar aynı koşullarda beslendikten dört hafta sonra yapılan ölçümler tabloda verilmiştir.\nBuna göre,\nI. Hipofizin çıkarılması kandaki tiroksin düzeyini azaltmıştır.\nII. M grubundaki sonuç, tiroksinin tiroit bezini uyardığını gösterir.\nIII. L grubundaki tiroit küçülmesi, tiroit bezinin çalışması için hipofiz hormonuna gereksinim olduğunu gösterir.\nyargılarından hangileri doğrudur?',
 sekil=SK,dogru=w17['dogru'],yan=w17['yan'],sira=w17['sira'],istenen='Deney sonuçlarına göre doğru olan yargılar.',
 ip=['Üç grubu ikişer ikişer karşılaştır; hangi uygulamanın hangi ölçümü değiştirdiğine bak.'],bilgi=[TIR],
 puf='Bir hormonun etkisi, hormonsuz grupla hormon verilen grubun karşılaştırılmasıyla anlaşılır.')

# ================ 18 · zor · tablo · diyabet
card(18,'Glikoz tolerans testi','İnsülin düzeyi çok düşük + glikoz yüksek: insülin üreten hücreler tahrip; insülin yüksek + glikoz yüksek: hedef hücre duyarlılığı azalmış.','Yüksek glikozu her durumda insülin yetersizliği sanmak.','zor','tablo',5,'en-glikoz','diyabet türlerini tablodan ayırt etme')
SK=tablo_svg(['Kişi','Açlık glikozu','Açlık insülini','2. saat glikozu'],[['K','85','8','105'],['L','230','1','380'],['M','180','40','300']])
S_,T_,D_='Sağlıklı','İnsülin üreten hücreleri tahrip olmuş','Duyarlılığı azalmış'
def tr(a_,b_,c_): return f'{a_} – {b_} – {c_}'
dg18=tr(S_,T_,D_)
y18=[(tr(S_,D_,T_),'L ve M’nin durumlarını ters yazmış; insülin düzeyi çok düşük olan L’nin insülin üretememesi, insülin düzeyi yüksek olan M’nin ise duyarlılığının azalması beklenir.','bilgi'),
     (tr(T_,S_,D_),'Glikozu normal ve 2 saat sonra normale dönen K’yi hasta sanmış; oysa K’nin değerleri sağlıklı bir bireye aittir.','dikkat'),
     (tr(D_,S_,T_),'K’yi duyarlılığı azalmış, L’yi sağlıklı sanmış; oysa L’nin glikozu çok yüksektir.','dikkat'),
     (tr(D_,T_,S_),'M’yi sağlıklı sanmış; oysa M’nin glikozu yüksek ve insülini yüksektir, bu duyarlılık azalmasını gösterir.','bilgi')]
sr18=[y18[0][0],dg18]+[y[0] for y in y18[1:]]
q('0018',18,[A('Tabloyu oku','K’nin değerleri normal; L’de glikoz çok yüksek, insülin çok düşük; M’de glikoz yüksek, insülin de yüksektir.','K normal · L: glikoz ↑, insülin ↓ · M: ikisi de ↑'),
   A('K’yi belirle','Normal açlık glikozu ve glikoz sonrası normale dönüş sağlıklı bir bireye aittir.','K = sağlıklı'),
   A('L’yi belirle','İnsülin neredeyse yok; insülin üreten hücreler tahrip olmuştur.','L = insülin üretimi yok'),
   A('M’yi belirle','İnsülin yüksek olduğu hâlde glikoz yüksektir; hedef hücreler insüline yanıt vermemektedir.','M = duyarlılığı azalmış'),
   A('Sonuç','Sıra sağlıklı, hücreleri tahrip olmuş, duyarlılığı azalmıştır.','Sağlıklı – tahrip – duyarlılık azalması')],
 tipId='en-glikoz',z='zor',alt='Diyabet',kaz='Glikoz ve insülin düzeylerini içeren tablodan sağlıklı, insülin üretemeyen ve insüline duyarlılığı azalmış bireyleri ayırt eder.',kalip='tablo',
 metin='Yaş ve beden kütlesi benzer K, L ve M yetişkinlerinden biri sağlıklı, birinin pankreasında insülin üreten hücreler tahrip olmuş, birinde ise hedef hücrelerin insüline duyarlılığı azalmıştır. Bu kişilerin açlık kan glikoz ve insülin düzeyleri ile glikoz içtikten iki saat sonraki kan glikoz düzeyleri tabloda verilmiştir (glikoz mg/100 mL, insülin göreli birimdir).\nBuna göre, K, L ve M kişilerinin durumları sırasıyla aşağıdakilerden hangisinde doğru verilmiştir?',
 sekil=SK,dogru=dg18,yan=y18,sira=sr18,istenen='K, L ve M kişilerinin sırasıyla durumları.',
 ip=['Her kişinin açlık ve 2. saat glikozunu insülin düzeyiyle birlikte oku.'],bilgi=[DIY,GLK2],
 puf='Tablodaki iki ölçümü birlikte yorumla.')

# ================ 19 · zor · olumsuz · ADH yokluğu
card(19,'ADH salgılayamayan birey','ADH yoksa su geri emilimi azalır; idrar çok ve seyrek olur, kan ozmotik derişimi artma eğilimi gösterir; ADH salgısı artırılamaz.','Ozmotik derişim artınca hastanın ADH salgılayabileceğini sanmak.','orta','hikâyeli',5,'en-hipo','ADH yetersizliğinde beklenen/beklenmeyen sonuçlar (olumsuz)')
o19=[('Günlük idrar miktarı sağlıklı bir bireye göre fazladır.',True,'Doğru bir ifadeyi yanlış sanmış; ADH olmadığı için su geri emilimi azalır ve idrar miktarı artar.'),
     ('İdrarın ozmotik derişimi sağlıklı bir bireye göre düşüktür.',True,'Doğru bir ifadeyi yanlış sanmış; su geri emilmediği için idrar seyrek olur.'),
     ('Böbrek tüplerinde suyun geri emilimi sağlıklı bir bireye göre azalmıştır.',True,'Doğru bir ifadeyi yanlış sanmış; ADH suyun geri emilimini artırır, yokluğunda azalır.'),
     ('Su kaybı arttığında kan plazmasının ozmotik derişimi yükselme eğilimi gösterir.',True,'Doğru bir ifadeyi yanlış sanmış; fazla su kaybı kanı derişikleştirir.'),
     ('Kanın ozmotik derişimi arttığında hipofizden salınan ADH, idrar miktarını azaltır.',False,'')]
w19=tek(o19,False,4)
q('0019',19,[A('Durumu yorumla','Arka hipofiz hasarlı olduğundan ADH salgılanamaz; ADH’nin görevi böbrek tüplerinde su geri emilimini artırmaktır.','ADH yok'),
   A('Böbrekteki sonucu çıkar','Su geri emilimi azalır; idrar miktarı artar ve idrar seyrelir.','İdrar çok ve seyrek'),
   A('Kana etkiyi çıkar','Su kaybı arttığı için kan plazmasının ozmotik derişimi yükselme eğilimi gösterir.','Ozmotik derişim ↑ eğilimi'),
   A('Telafiyi sına','Hasar nedeniyle ADH salgılanamaz; derişim artsa da ADH ile idrar azaltılamaz.','ADH yok → idrar azalmaz'),
   A('Sonuç','ADH’nin idrar miktarını azalttığını söyleyen ifade bu hasta için söylenemez.','ADH ile idrar azalması: söylenemez')],
 tipId='en-hipo',z='orta',alt='ADH ve Su Dengesi',kaz='ADH salgılayamayan bir bireyde idrar, kan ve böbrek tüpleriyle ilgili söylenemeyecek ifadeyi belirler.',kalip='hikâyeli',
 metin='Bir kaza sonucunda hipofizin arka lobu hasar gören ve bu nedenle ADH salgılayamayan sağlıklı bir yetişkin, günlük su gereksinimini karşılayacak kadar su içmektedir.\nBu bireyle ilgili aşağıdakilerden hangisi söylenemez?',
 dogru=w19['dogru'],yan=w19['yan'],sira=w19['sira'],istenen='Bu bireyle ilgili söylenemeyecek ifade.',
 ip=['Hormon salgılanamıyorsa hangi böbrek işleminin değişeceğini ve vücudun bunu telafi edip edemeyeceğini düşün.'],bilgi=[OZM],
 puf='Eksik hormonun görevlerini ve vücudun bunu telafi edip edemeyeceğini düşün.')

# ================ 20 · zor · tiroit çıkarılması
card(20,'Tiroidektomi sonrası değişimler','Tiroit çıkarılınca tiroksin azalır, TSH artar, metabolizma hızı düşer; paratiroit korunduğundan kan kalsiyumu parathormonla düzenlenir.','Kalsitonin yokluğunda kalsiyum düzenin tamamen bozulacağını sanmak; TSH’nin azalacağını düşünmek.','zor','hikâyeli',5,'en-ca','tiroit çıkarıldığında TSH, metabolizma ve kalsiyum')
d20='TSH artar, bazal metabolizma hızı azalır ve kan kalsiyum düzeyi paratiroit hormonuyla düzenlenmeye devam eder.'
y20=[('TSH azalır, bazal metabolizma hızı artar ve kan kalsiyum düzeyi paratiroit hormonuyla düzenlenmeye devam eder.','Tiroksin yokluğunda hipofiz baskısının kalkacağını görememiş; bu yüzden TSH’nin azaldığını ve metabolizmanın arttığını sanmış.','bilgi'),
     ('TSH artar, bazal metabolizma hızı azalır ve kan kalsiyum düzeyi düzenlenemez hâle gelir.','Kalsitonin yokluğunda kalsiyum düzeninin tümüyle bozulacağını sanmış; oysa paratiroit korunmuştur ve parathormon düzenlemeyi sürdürür.','bilgi'),
     ('TSH değişmez, bazal metabolizma hızı azalır ve kan kalsiyum düzeyi paratiroit hormonuyla düzenlenmeye devam eder.','Tiroksin azalınca hipofizin baskısının kalkacağını unutmuş; TSH’nin değişmeyeceğini sanmış.','bilgi'),
     ('TSH artar, bazal metabolizma hızı artar ve kan kalsiyum düzeyi düzenlenemez hâle gelir.','Tiroksinsiz bir bireyde metabolizma hızının artacağını ve kalsiyumun düzenlenemeyeceğini sanmış; iki bilgi de yanlıştır.','bilgi')]
sr20=[y20[0][0],y20[1][0],y20[2][0],d20,y20[3][0]]
q('0020',20,[A('Tiroksini ele al','Tiroit çıkarılınca tiroksin salgılanamaz; hücrelerde metabolizma hızı düşer.','Tiroksin ↓ → bazal metabolizma hızı ↓'),
   A('Geri bildirimi uygula','Tiroksin azalınca hipofiz üzerindeki baskı kalkar; TSH salgısı artar.','TSH ↑'),
   A('Kalsiyumu değerlendir','Kalsitonin tiroitten gelir ama paratiroit bezleri korunmuştur.','Parathormon var'),
   A('Kalsiyum düzenini yorumla','Parathormon kemikten kana kalsiyum geçişini artırarak düzeni sürdürür; düzen çökmez.','Kalsiyum düzenlenmeye devam'),
   A('Sonuç','TSH artar, metabolizma azalır, kalsiyum düzeni sürer.','TSH ↑ · BMH ↓ · Ca düzenli')],
 tipId='en-ca',z='zor',alt='Tiroit ve Paratiroit',kaz='Tiroit bezi çıkarılmış bir bireyde TSH, bazal metabolizma hızı ve kan kalsiyum düzenindeki değişimleri birlikte yorumlar.',kalip='hikâyeli',
 metin='Tiroit kanseri nedeniyle tiroit bezi tamamen çıkarılan ancak paratiroit bezleri korunan bir hastaya, ameliyattan sonra herhangi bir hormon tedavisi uygulanmıyor.\nBu hastada ameliyattan bir süre sonra yapılan ölçümlerle ilgili aşağıdakilerden hangisi beklenir?',
 dogru=d20,yan=y20,sira=sr20,istenen='Hastada beklenen değişimler.',
 ip=['Tiroksinin hipofiz üzerindeki etkisini, tiroit bezinin kalsiyum düzenlemesindeki payını ve paratiroit bezlerinin işlevini ayrı ayrı düşün.'],bilgi=[TIR,CAL],
 puf='Bir bez alınınca onun hormonunun etkisi ve hipofizdeki geri bildirimi birlikte değerlendirilir.')

# ---------------- yaz
for qq in P.ANA: qq['kardes']=None
SC='/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/endokrin'; os.makedirs(SC,exist_ok=True)
P.yaz(os.path.join(GD,'endokrin-1.json'),os.path.join(SC,'bos-endokrin.json'))
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=KONU_K))['kartlar'].append(c['id'])
json.dump(dict(konu='Endokrin Sistem',surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2018–2026 Biyoloji (yalnız mantık), MEB 12. sınıf biyoloji.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','abendokrin.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
