"""AYT Kimya · Kimyasal Tepkimelerde Hız · 2. dalga (hiziki) · 10 soru. Her değer Python'da hesaplanıp assert edilir."""
import sys,os,math,json
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-kim')); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
import _hafif_kim2 as H
from _hafif_kim2 import *
from cizim import tikz_svg
H.KONU='Kimyasal Tepkimelerde Hız'
P=Parti('hiziki','Kimyasal Tepkimelerde Hız','akim|Kimyasal Tepkimelerde Hız',ders='AYT Kimya',idon='aytkim')
KY='ÖSYM AYT 2018–2026 Kimya (Tepkime Hızı; yalnız mantık) · MEB 11. sınıf Kimyasal Tepkimelerde Hız'
TIPLER={'hz-ifade':'Hız ifadesi ve ortalama hız','hz-denklem':'Hız denklemi ve hız sabiti','hz-mekanizma':'Mekanizma ve hızı belirleyen basamak','hz-enerji':'Aktivasyon enerjisi ve enerji diyagramı','hz-katalizor':'Katalizör ve aktivasyon enerjisi','hz-faktor':'Hızı etkileyen faktörler'}
CARD={}
def card(no,alt,fikir,tuzak,z,kalip,adim,tipId,ozet):
    kart(f'K-AKHIZ2-{no:02d}',alt,fikir,tuzak,z,kalip,adim,tipId,TIPLER[tipId],KY); CARD[no]=ozet
def q(no,cn,ad,**k):
    mk(P,no,ad=ad,adim=len(ad),kart=f'K-AKHIZ2-{cn:02d} ('+CARD[cn]+')',tip=TIPLER[k['tipId']],**k)
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
def tikz(lines): return tikz_svg(HEAD+'\n'.join(lines)+TAIL)
def pg(opts,body):
    return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n\\begin{axis}['+opts+']\n'+body+'\n\\end{axis}\n\\end{tikzpicture}')
def co(pts): return ' '.join(f'({x:.3f},{y:.4f})' for x,y in pts)
SIR=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
SETS={'Yalnız I':{'I'},'Yalnız II':{'II'},'Yalnız III':{'III'},'I ve II':{'I','II'},'I ve III':{'I','III'},'II ve III':{'II','III'},'I, II ve III':{'I','II','III'}}
def onc(truth,why,pos):
    nm=['I','II','III']; C={n for n,t in zip(nm,truth) if t}
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
    h=[o for o in opts if o[1]==hedef]; assert len(h)==1
    dg=h[0]; yn=[o for o in opts if o[1]!=hedef]
    sira=yn[:pos]+[dg]+yn[pos:]
    return dict(dogru=dg[0],sira=[x[0] for x in sira],yan=[(o[0],o[2],'bilgi') for o in yn])
def pe(curves,ticks,ymax,leg,sc=0.03):
    """curves: [(Ereaktif,Etepe,Eurun,stil,renk)]; ticks: kJ değerleri; leg: [(etiket,stil,renk)]"""
    o=[f'\\draw[->,thick] (0,0) -- (0,{ymax*sc+0.35:.2f});',f'\\draw[->,thick] (0,0) -- (6.8,0);',
       f'\\node[anchor=north] at (3.4,-.1) {{Tepkime koordinatı}};',f'\\node[rotate=90,anchor=south] at (-1.15,{ymax*sc/2:.2f}) {{Potansiyel enerji (kJ)}};']
    for t in ticks: o.append(f'\\draw (0,{t*sc:.3f}) -- (-.08,{t*sc:.3f}); \\node[anchor=east] at (-.1,{t*sc:.3f}) {{{t}}};')
    for (R,Hh,Pr,stl,col) in curves:
        r,h,p=R*sc,Hh*sc,Pr*sc
        o.append(f'\\draw[gray,dotted] (0,{h:.3f}) -- (3,{h:.3f});')
        o.append(f'\\draw[thick,{stl},{col}] (0,{r:.3f}) -- (1,{r:.3f}) .. controls (2,{r:.3f}) and (2.2,{h:.3f}) .. (3,{h:.3f}) .. controls (3.8,{h:.3f}) and (4,{p:.3f}) .. (5,{p:.3f}) -- (6,{p:.3f});')
    base=curves[0]
    o.append(f'\\draw[gray,dotted] (0,{base[0]*sc:.3f}) -- (1,{base[0]*sc:.3f}); \\draw[gray,dotted] (0,{base[2]*sc:.3f}) -- (5,{base[2]*sc:.3f});')
    y=ymax*sc-0.1
    for (et,stl,col) in leg:
        o.append(f'\\draw[thick,{stl},{col}] (4.4,{y:.2f}) -- (5.1,{y:.2f}); \\node[anchor=west] at (5.2,{y:.2f}) {{{et}}};'); y-=0.45
    return tikz(o)
BLK='black'; BLU='blue!70!black'; RED='red!70!black'

TAB=B('Tanecik modelinde derişim','derişim, tanecik sayısının hacme bölümüdür; aynı tanecik sayısı daha küçük hacimde daha büyük derişim demektir. Hız denklemi verilmişse iki kaptaki hız oranı, derişimlerin üslü çarpımlarının oranıdır. Örnek: r = k[P]² iken derişim 3 katına çıkarsa hız 9 katına çıkar')
KATB=B('İki yolun karşılaştırılması','aynı tepkimenin farklı yollarında girenler ve ürünler aynı düzeydedir; yollar yalnız tepe noktalarıyla ayrılır. Tepesi daha düşük yolun aktivasyon enerjisi küçüktür ve hızı büyüktür. Örnek: tepeleri 90 ve 70 kJ olan iki yolda, girenleri 30 kJ’de olan tepkimenin ileri Eₐ’ları 60 ve 40 kJ’dir')
# ---------- bilgi kutuları (örnekler soruların madde ve sayılarını kullanmaz)
ORTB=B('Ortalama hız','ortalama hız, derişim değişiminin süreye oranıdır (mol/L·s). Maddelerin hızları katsayılarıyla orantılıdır; tepkime hızı bir maddenin hızının kendi katsayısına bölünmesiyle bulunur. Hacim hesaba katılmadığında hız mol/s olarak da verilebilir. Örnek: 2P → 3R tepkimesinde R’nin oluşma hızı, P’nin harcanma hızının 3/2 katıdır')
ETB=B('Hızı etkileyen etkenler','derişim, yüzey alanı, sıcaklık ve katalizör hızı değiştirir. Bir etkenin hızı değiştirmesi için derişimi, temas yüzeyini, çarpışma enerjisini ya da tepkime yolunu gerçekten değiştirmesi gerekir. Örnek: katalizör, aynı tepkimeyi daha düşük aktivasyon enerjili bir yoldan yürütür')
MEB=B('Mekanizma','tepkime basamaklarının toplamı net tepkimeyi verir; yalnız ara basamaklarda görünen madde ara üründür. Hız denklemini en yavaş basamak belirler: o basamaktaki girenlerin katsayıları üs olur. Örnek: yavaş basamak P + 2Q → … ise r = k[P][Q]²')
KUB=B('Hız sabitinin birimi','r = k[A]ᵐ[B]ⁿ ise k’nın birimi (mol/L·s) ÷ (mol/L)ᵐ⁺ⁿ ile bulunur; toplam derece 2 ise L/mol·s, 3 ise L²/mol²·s olur. Örnek: toplam derecesi 1 olan tepkimede k’nın birimi 1/s’dir')
DEB=B('Deney tablosundan hız denklemi','bir derişimi sabit tutup diğerini değiştirdiğin iki deneyi karşılaştır: derişim a kat olunca hız aⁿ kat oluyorsa o maddeye göre derece n’dir. Hızı değişmeyen maddenin derecesi sıfırdır ve denklemde yer almaz. Örnek: derişim 2 katına çıkınca hız 8 katına çıkıyorsa derece 3’tür')
GRB=B('Derişim–zaman grafiği','girenlerin eğrisi iner, ürünlerin eğrisi çıkar; aynı sürede derişim değişimleri katsayılarla orantılıdır. Eğri yataylaşınca hız sıfıra yaklaşır; eğimi ne kadar dik ise o aralıkta hız o kadar büyüktür. Örnek: bir aralıkta 0,2 ve 0,6 mol/L değişen iki maddenin katsayıları 1 : 3 oranındadır')
PEB=B('Enerji diyagramı','ileri tepkimenin Eₐ’sı tepe noktası ile girenler arasındaki, geri tepkimenin Eₐ’sı tepe noktası ile ürünler arasındaki enerji farkıdır. Katalizör tepe noktasını indirir; ileri ve geri Eₐ’yı aynı miktarda azaltır, ΔH’ı değiştirmez. Örnek: girenler 20, tepe 60, ürünler 30 kJ ise ileri Eₐ = 40, geri Eₐ = 30 kJ’dir')
GZB=B('Gaz tepkimesinde basınç','sabit hacim ve sıcaklıkta toplam mol sayısı toplam basınçla orantılıdır (PV = nRT). Başlangıçtaki ve sonraki toplam mol sayısı farkından, tepkimede ilerleyen miktar katsayılarla bulunur. Örnek: 2P → 4R için 1 birim ilerlemede toplam mol 2 artar')
KTB=B('Kütle kaybından hız','açık kapta gaz çıkan tepkimede kütledeki azalma, çıkan gazın kütlesidir. Gazın kütlesi molüne çevrilir, katsayı oranıyla başka maddenin molüne geçilir ve süreye bölünür. Örnek: 1 mol gaz çıkışına karşılık 3 mol bir giren harcanıyorsa 0,2 mol gaz çıkışında giren 0,6 mol azalmıştır')

# ================ kartlar
card(1,'Katsayı oranıyla ortalama hız','Tablodan bir maddenin mol değişimi bulunur, hacme ve süreye bölünür; başka madde için katsayı oranı uygulanır.','Katsayıyı mol sayısı sanmak; hacme bölmeyi unutmak.','kolay','tablo',3,'hz-ifade','tablodan ortalama oluşma hızı')
card(2,'Hızı etkileyen etkenleri yorumlama','Her etken derişimi, yüzeyi, çarpışma enerjisini ya da yolu değiştirir; her açıklamada ileri sürülen neden gerçekten bu niceliklerden birini değiştirmelidir.','Etkeni, ileri sürülen nedeni sorgulamadan kabul etmek.','kolay','düz',3,'hz-faktor','hız etkenlerinde yanlış açıklamayı bulma')
card(3,'Mekanizmada ara ürün ve hız denklemi','Yavaş basamak hız denklemini verir; yalnız ara basamaklarda görünen tür ara üründür; k’nın birimi toplam dereceden çıkar.','Hız denklemini net tepkime katsayılarından yazmak.','orta','tablo',4,'hz-mekanizma','mekanizma tablosunu yorumlama')
card(4,'Katalizörlü yolda geri tepkime Eₐ’sı','Katalizör tepe noktasını indirir; geri Eₐ’yı da ileri Eₐ ile aynı miktarda azaltır.','Katalizörü yalnız ileri tepkimeye etkili saymak.','orta','şekilli',3,'hz-enerji','enerji diyagramından geri Eₐ okuma')
card(5,'Üç maddeli deney tablosu','Her maddenin derecesi ayrı deney çiftlerinden bulunur; sıfırıncı dereceli madde denklemde yer almaz.','Hızı değişmeyen maddeyi de denkleme katmak.','orta','tablo',4,'hz-denklem','deney tablosundan k hesabı')
card(6,'Derişim–zaman grafiğinden denklem ve hız','Derişim değişimlerinin oranı katsayıları, eğimin dikliği hızın büyüklüğünü verir.','Eğri yataylaşınca hızın arttığını sanmak.','orta','grafik',4,'hz-ifade','grafikten katsayı ve ortalama hız')
card(7,'Tanecik modelinde hız oranı','Taneciklerin sayıları hacme bölünerek derişim bulunur, hız denklemine yazılır ve iki kap oranlanır.','Hacim farkını göz ardı edip sayılarla oranlamak.','orta','şekilli',4,'hz-denklem','tanecik modelinden hız oranı')
card(8,'Toplam basınçtan hız','Toplam mol sayısı artışı ilerleme miktarını verir; ilerleme katsayılarla ürün miktarına çevrilir.','Toplam mol artışını doğrudan bir ürünün miktarı sanmak.','zor','grafik',5,'hz-ifade','basınç–zaman grafiğinden oluşma hızı')
card(9,'Kütle kaybı ve katsayı oranı','Kütle azalması çıkan gazın kütlesidir; molüne ve katsayı oranıyla öteki maddenin molüne çevrilip süreye bölünür.','Katsayı oranını uygulamamak; yanlış aralığı okumak.','zor','grafik',5,'hz-faktor','kütle–zaman grafiğinden hız karşılaştırma')
card(10,'İki katalizörlü enerji diyagramı','Her yolun Eₐ’sı tepeden girenlere ve ürünlere göre ayrı bulunur; ΔH tüm yollarda aynıdır, daha düşük tepe daha hızlı yoldur.','Katalizörün ΔH’ı değiştirdiğini sanmak.','zor','şekilli',5,'hz-katalizor','iki katalizörlü diyagramı yorumlama')

# ================ 01 · kolay · tablo, NO₂ oluşma hızı
V1=5; n1=[Fr(3),Fr(2),Fr(7,5)]
dN=n1[0]-n1[1]; rate_N=dN/V1/25; rate_NO2=rate_N*2; assert (rate_N,rate_NO2)==(Fr(8,1000),Fr(16,1000))
d1=(rate_N, Fr(4)/V1/25, dN/25, 2*dN/25); assert d1==(Fr(8,1000),Fr(32,1000),Fr(40,1000),Fr(80,1000))
SK=tablo_svg(['Zaman (s)','N₂O₅ mol sayısı'],[['0','3'],['25','2'],['50','1,4']])
q('0001',1,[A('Mol değişimini bul','İlk 25 saniyede N₂O₅ 3 − 2 = 1 mol azalır.','Δn(N₂O₅) = 1 mol'),
   A('N₂O₅’in hızı','Hacim 5 L ve süre 25 s olduğundan harcanma hızı 1 ÷ 5 ÷ 25 = 0,008 mol/L·s bulunur.','0,008 mol/L·s'),
   A('Katsayı oranını uygula','NO₂’nin katsayısı 4, N₂O₅’inki 2’dir; NO₂’nin hızı 0,008 × 4/2 = 0,016 mol/L·s olur.','0,016 mol/L·s')],
 tipId='hz-ifade',z='kolay',alt='Ortalama Hız',kaz='Tablodaki mol verisinden bir maddenin ortalama hızını bulup katsayı oranıyla başka maddenin hızına geçer.',kalip='tablo',
 metin='Hacmi 5 L olan sabit hacimli kapalı bir kapta, sabit sıcaklıkta\n2N₂O₅(g) → 4NO₂(g) + O₂(g)\ntepkimesi gerçekleştiriliyor. Kaptaki N₂O₅ gazının mol sayısının zamanla değişimi tabloda verilmiştir.\nBuna göre tepkimenin ilk 25 saniyesinde NO₂ gazının ortalama oluşma hızı kaç mol/L·s’dir?',
 sekil=SK,dogru=rate_NO2,yan=[(d1[0],'N₂O₅’in harcanma hızını (0,008) NO₂’nin hızı sanmış; katsayı oranı olan 4/2 = 2 ile çarpmayı unutmuştur.','dikkat'),
  (d1[1],'N₂O₅’in 1 mol azalmasına karşılık 4 mol NO₂ oluştuğunu sanmış (katsayıyı mol saymış): 4 ÷ 5 ÷ 25 = 0,032.','bilgi'),
  (d1[2],'N₂O₅’in mol değişimini (1 mol) doğrudan süreye bölmüş (1 ÷ 25); hacmi ve katsayı oranını hesaba katmamıştır.','islem'),
  (d1[3],'Oluşan NO₂ mol sayısını (2 mol) doğru bulmuş ama hacme bölmeden süreye bölmüştür: 2 ÷ 25 = 0,08.','islem')],
 istenen='NO₂ gazının ilk 25 saniyedeki ortalama oluşma hızı.',ip=['Tabloda hangi maddenin verisi var, hangi maddenin hızı isteniyor?'],bilgi=[ORTB],
 puf='Hız, derişim değişiminin süreye oranıdır; maddelerin hızları katsayılarıyla orantılıdır.')

# ================ 02 · kolay · olumsuz kök, metin
o2=[('Magnezyum şerit yerine magnezyum tozu kullanıldığında temas yüzeyi arttığı için HCl çözeltisiyle tepkime daha hızlı gerçekleşir.',True,'Bu açıklama doğrudur: katı girenin yüzeyi büyüdükçe etkin çarpışma sayısı artar. Bu şıkkı seçen öğrenci doğru bir açıklamayı yanlış sanmıştır.'),
    ('Gaz fazındaki bir tepkimenin gerçekleştiği kabın hacmi küçültülünce girenlerin derişimi artar ve tepkime hızlanır.',True,'Bu açıklama doğrudur: hacim küçülünce birim hacimdeki tanecik sayısı artar. Bu şıkkı seçen öğrenci doğru bir açıklamayı yanlış sanmıştır.'),
    ('Sabit hacimli bir kapta gaz fazında gerçekleşen tepkimeye tepkimeye girmeyen bir asal gaz eklenince girenlerin derişimi azalır ve tepkime yavaşlar.',False,'Sabit hacimde asal gaz eklenince girenlerin mol sayısı da hacim de değişmez; derişim ve hız aynı kalır.'),
    ('Sıcaklık artırılınca aktivasyon enerjisini aşan tanecik oranı arttığından etkin çarpışma sayısı artar ve tepkime hızlanır.',True,'Bu açıklama doğrudur: sıcaklık arttıkça eşik enerjisini aşan tanecik oranı büyür. Bu şıkkı seçen öğrenci doğru bir açıklamayı yanlış sanmıştır.'),
    ('Katalizör, tepkimenin daha düşük aktivasyon enerjili bir yoldan gerçekleşmesini sağlayarak tepkimeyi hızlandırır.',True,'Bu açıklama doğrudur: katalizör alternatif ve daha düşük enerjili bir yol sunar. Bu şıkkı seçen öğrenci doğru bir açıklamayı yanlış sanmıştır.')]
r2=tek(o2,False,4)
q('0002',2,[A('Her açıklamayı sına','Yüzey alanı, hacim, sıcaklık ve katalizör açıklamaları ders kitabı bilgisiyle uyumludur.','Dört açıklama doğru'),
   A('Asal gazı değerlendir','Sabit hacimde tepkimeye girmeyen gaz eklenince girenlerin derişimi değişmez.','Derişim ve hız aynı kalır'),
   A('Sonuç','Yanlış açıklama asal gazın hızı azalttığını söyleyen açıklamadır.','Asal gaz açıklaması yanlış')],
 tipId='hz-faktor',z='kolay',alt='Hızı Etkileyen Faktörler',kaz='Tepkime hızını etkileyen etkenlere ilişkin açıklamaların doğruluğunu değerlendirir.',kalip='düz',
 metin='Bir kimya öğretmeni, tepkime hızını etkileyen etkenleri anlatmak için laboratuvardan ve günlük yaşamdan örnekler veriyor. Öğrencilerden, her örnekte verilen açıklamanın bilimsel olarak doğru olup olmadığını değerlendirmelerini istiyor. Öğretmenin verdiği açıklamalar aşağıda sıralanmıştır.\nBuna göre bu açıklamalardan hangisi yanlıştır?',
 sekil=None,dogru=r2['dogru'],yan=r2['yan'],sira=r2['sira'],istenen='Yanlış olan açıklama.',
 ip=['Her açıklamada ileri sürülen nedenin derişimi, yüzeyi ya da enerjiyi gerçekten değiştirip değiştirmediğini düşün.'],bilgi=[ETB],
 puf='İleri sürülen nedenin derişimi, yüzeyi ya da enerjiyi gerçekten değiştirip değiştirmediğine bak.')

# ================ 03 · orta · mekanizma tablosu, öncüllü
SK=tablo_svg(['Basamak','Tepkime','Hız'],[['1','2NO(g) + H₂(g) → N₂(g) + H₂O₂(g)','Yavaş'],['2','H₂O₂(g) + H₂(g) → 2H₂O(g)','Hızlı']])
w3=onc([True,False,True],['H₂O₂ 1. basamakta oluşup 2. basamakta tükendiği için net tepkimede yer almaz ve ara üründür',
   'hız denklemini yavaş olan 1. basamak belirler; bu basamakta 2 NO ve 1 H₂ girdiğinden denklem r = k[NO]²[H₂]’dir, H₂’nin üssü 1’dir',
   'hız denklemi r = k[NO]²[H₂] olduğundan toplam derece 3’tür ve k’nın birimi L²/mol²·s olur'],4)
q('0003',3,[A('Ara ürünü bul','H₂O₂ yalnız 1. basamakta oluşur, 2. basamakta tükenir; net tepkimede görünmez.','I: doğru'),
   A('Hız denklemini yaz','Yavaş basamak 1. basamaktır: r = k[NO]²[H₂].','II: yanlış'),
   A('k’nın birimini bul','Toplam derece 2 + 1 = 3 olduğundan birim L²/mol²·s’dir.','III: doğru'),
   A('Sonuç','I ve III doğrudur.','I ve III')],
 tipId='hz-mekanizma',z='orta',alt='Tepkime Mekanizması',kaz='İki basamaklı bir mekanizmada ara ürünü, hız denklemini ve hız sabitinin birimini belirler.',kalip='tablo',
 metin='Sabit sıcaklıkta gerçekleşen\n2NO(g) + 2H₂(g) → N₂(g) + 2H₂O(g)\ntepkimesinin mekanizması, basamakları ve bu basamakların hızları ile birlikte tabloda verilmiştir.\nI. H₂O₂ ara üründür.\nII. Tepkimenin hız denklemi r = k[NO]²[H₂]²’dir.\nIII. Hız sabitinin (k) birimi L²/mol²·s’dir.\nBuna göre yukarıdaki yargılardan hangileri doğrudur?',
 sekil=SK,dogru=w3['dogru'],yan=w3['yan'],sira=w3['sira'],istenen='Doğru olan yargılar.',
 ip=['Hız denklemini yazarken hangi basamağın hızı belirlediğine bak, k’nın birimini de bu denklemden çıkar.'],bilgi=[MEB,KUB],
 puf='Her yargıyı basamak tablosundaki bilgilerle ayrı ayrı sına.')

# ================ 04 · orta · enerji diyagramı, katalizörlü yolda geri Ea
R4,T4,P4,TK4=40,130,10,105
assert (T4-R4,T4-P4,TK4-R4,TK4-P4)==(90,120,65,95) and T4-TK4==25
SK=pe([(R4,T4,P4,'solid',BLK),(R4,TK4,P4,'dashed',BLU)],[P4,R4,TK4,T4],T4,[('Katalizörsüz','solid',BLK),('Katalizörlü','dashed',BLU)])
d4=(TK4-R4,TK4,T4-P4,T4-P4+(T4-TK4)); assert d4==(65,105,120,145)
q('0004',4,[A('Katalizörlü yolu oku','Katalizörlü yolun tepe noktasının enerjisi grafikte okunur.','Tepe: 105 kJ'),
   A('Ürünlerin enerjisini oku','Ürünlerin potansiyel enerjisi 10 kJ’dir.','Ürünler: 10 kJ'),
   A('Geri Eₐ’yı hesapla','Geri tepkimenin Eₐ’sı tepe noktası ile ürünler arasındaki farktır.','Eₐ(geri) = 105 − 10 = 95 kJ')],
 tipId='hz-enerji',z='orta',alt='Enerji Diyagramı',kaz='Katalizörlü yola ait enerji diyagramından geri tepkimenin aktivasyon enerjisini bulur.',kalip='şekilli',
 metin='Tek basamakta gerçekleşen bir tepkimenin katalizörsüz ve katalizörlü yollara ait potansiyel enerji–tepkime koordinatı grafiği şekilde verilmiştir.\nBuna göre katalizörlü yolda geri tepkimenin aktivasyon enerjisi kaç kJ’dir?',
 sekil=SK,dogru=95,yan=[(d4[0],'Katalizörlü yoldaki ileri tepkimenin Eₐ’sını (105 − 40 = 65) vermiş; istenen geri tepkimenin Eₐ’sıdır.','dikkat'),
  (d4[1],'Katalizörlü yolun tepe noktasının enerjisini (105 kJ) Eₐ sanmış; Eₐ tepe ile ilgili başlangıç düzeyi arasındaki farktır.','bilgi'),
  (d4[2],'Katalizörsüz yoldaki geri Eₐ’yı (130 − 10 = 120) vermiş; katalizörün geri tepkimenin Eₐ’sını da azalttığını unutmuştur.','dikkat'),
  (d4[3],'Katalizörün tepeyi indirdiği 25 kJ’yi geri Eₐ’ya eklemiş: 120 + 25 = 145; katalizör Eₐ’yı azaltır.','islem')],
 istenen='Katalizörlü yolda geri tepkimenin aktivasyon enerjisi.',ip=['Geri tepkimenin Eₐ’sının hangi iki enerji düzeyi arasındaki fark olduğunu düşün.'],bilgi=[PEB],
 puf='Aktivasyon enerjisi yöne bağlıdır; hangi yönün ve hangi yolun istendiğine dikkat et.')

# ================ 05 · orta · üç maddeli deney tablosu, k
exps=[(Fr(1,10),Fr(1,10),Fr(1,10),Fr(2,1000)),(Fr(2,10),Fr(1,10),Fr(1,10),Fr(4,1000)),(Fr(1,10),Fr(2,10),Fr(1,10),Fr(8,1000)),(Fr(1,10),Fr(1,10),Fr(2,10),Fr(2,1000))]
assert exps[1][3]/exps[0][3]==2 and exps[2][3]/exps[0][3]==4 and exps[3][3]/exps[0][3]==1
k5=exps[0][3]/(exps[0][0]*exps[0][1]**2); assert k5==2
for e in exps: assert e[3]==k5*e[0]*e[1]**2
e0=exps[0]
d5=(e0[3], e0[3]/(e0[0]*e0[1]), e0[3]/(e0[0]*e0[1]**2*e0[2]), e0[3]/(e0[0]*e0[1]**2*e0[2]**2)); assert d5==(Fr(2,1000),Fr(2,10),20,200)
SK=tablo_svg(['Deney','[X] (mol/L)','[Y] (mol/L)','[Z] (mol/L)','Hız (mol/L·s)'],[[str(i+1)]+[fm(v) for v in e] for i,e in enumerate(exps)])
q('0005',5,[A('X’in derecesini bul','1. ve 2. deneyde yalnız [X] 2 katına çıkmış, hız 2 katına çıkmıştır.','X’e göre 1. derece'),
   A('Y ve Z’yi bul','1. ve 3. deneyde hız 4 katına çıkar (2. derece); 1. ve 4. deneyde hız değişmez (0. derece).','Y’ye göre 2. derece · Z’ye göre 0. derece'),
   A('k’yı hesapla','r = k[X][Y]² denkleminde 1. deneyin değerleri yazılır.','0,002 = k × 0,1 × 0,01 → k = 2')],
 tipId='hz-denklem',z='orta',alt='Hız Denklemi',kaz='Üç girenli bir tepkimenin deney tablosundan hız denklemini bulup hız sabitinin değerini hesaplar.',kalip='tablo',
 metin='X(g) + Y(g) + Z(g) → ürünler\ntepkimesi için sabit sıcaklıkta yapılan dört deneyin başlangıç derişimleri ve başlangıç hızları tabloda verilmiştir.\nBuna göre bu sıcaklıkta tepkimenin hız sabiti (k) kaç L²/mol²·s’dir?',
 sekil=SK,dogru=2,yan=[(d5[0],'Hız denkleminde k’yı bulmak yerine ilk deneyin hız değerini (0,002) k sanmıştır.','dikkat'),
  (d5[1],'Hız denklemini r = k[X][Y] almış (Y’yi 1. derece saymış): 0,002 ÷ 0,01 = 0,2.','bilgi'),
  (d5[2],'Hız hiç değişmediği hâlde Z’yi 1. dereceden denkleme katmış: 0,002 ÷ (0,1 × 0,01 × 0,1) = 20.','bilgi'),
  (d5[3],'Z’yi 2. dereceden denkleme katmış: 0,002 ÷ (0,1 × 0,01 × 0,01) = 200.','bilgi')],
 istenen='Hız sabitinin (k) değeri.',ip=['Her maddenin derecesini, yalnız o maddenin derişiminin değiştiği deney çiftinden bul.'],bilgi=[DEB],
 puf='Önce her maddenin derecesini ayrı deney çiftlerinden bul, sonra k’yı hesapla.')

# ================ 06 · orta · derişim–zaman grafiği, öncüllü
def Aa(t): return Fr(6,5)*(1-Fr(t,20))**2
def Bb(t): return (Fr(6,5)-Aa(t))/2
def Cc(t): return 3*(Fr(6,5)-Aa(t))/2
assert (Aa(0),Aa(20),Bb(20),Cc(20))==(Fr(6,5),0,Fr(3,5),Fr(9,5)) and (Aa(10),Bb(10),Cc(10))==(Fr(3,10),Fr(9,20),Fr(27,20))
dA1=Aa(0)-Aa(10); dA2=Aa(10)-Aa(20); assert dA1>dA2 and (dA1,dA2)==(Fr(9,10),Fr(3,10))
assert Bb(20)/20==Fr(3,100)
ts=[i*20/24 for i in range(25)]
pa=[(t,float(Aa(Fr(t).limit_denominator(1000)))) for t in ts]; pb=[(t,float(Bb(Fr(t).limit_denominator(1000)))) for t in ts]; pc=[(t,float(Cc(Fr(t).limit_denominator(1000)))) for t in ts]
SK=pg('width=7cm,height=5.4cm,axis lines=left,xmin=0,xmax=22,ymin=0,ymax=2.1,xtick={0,10,20},ytick distance=0.3,yticklabel={\\pgfmathprintnumber[fixed,fixed zerofill,precision=1,use comma]{\\tick}},grid=major,major grid style={gray!45,thin},xlabel={Zaman (s)},ylabel={Derişim (mol/L)},label style={font=\\small},tick label style={font=\\small}',
 f'\\addplot[thick,color=blue!70!black] coordinates {{{co(pa)}}};\n\\addplot[thick,dashed,color=red!70!black] coordinates {{{co(pb)}}};\n\\addplot[thick,dotted,color=black] coordinates {{{co(pc)}}};\n\\node[anchor=west,font=\\small] at (axis cs:9,1.65) {{C}};\n\\node[anchor=south west,font=\\small] at (axis cs:1.2,1.0) {{A}};\n\\node[anchor=center,font=\\small] at (axis cs:16.5,0.4) {{B}};')
w6=onc([True,False,False],['A’dan 1,2, B’den 0,6 ve C’den 1,8 mol/L’lik derişim değişimi 2 : 1 : 3 oranında olduğundan tepkime 2A → B + 3C’dir',
   'A’nın derişimi 0–10 s aralığında 0,9, 10–20 s aralığında 0,3 mol/L azaldığından ilk aralıktaki ortalama hız daha büyüktür',
   'B’nin derişimi 20 s’de 0,6 mol/L arttığından ortalama oluşma hızı 0,6 ÷ 20 = 0,03 mol/L·s’dir'],0)
q('0006',6,[A('Katsayıları bul','A 1,2 mol/L azalırken B 0,6, C 1,8 mol/L artmıştır; oran 2 : 1 : 3.','I: doğru'),
   A('Aralıkları kıyasla','A’da 0–10 s aralığında 1,2 → 0,3 (0,9 azalma), 10–20 s aralığında 0,3 → 0 (0,3 azalma).','II: yanlış'),
   A('B’nin hızını hesapla','0,6 ÷ 20 = 0,03 mol/L·s.','III: yanlış'),
   A('Sonuç','Yalnız I doğrudur.','Yalnız I')],
 tipId='hz-ifade',z='orta',alt='Derişim–Zaman Grafiği',kaz='Derişim–zaman grafiğinden tepkime denklemini ve ortalama hızları yorumlar.',kalip='grafik',
 metin='Sabit hacimli kapalı bir kapta, sabit sıcaklıkta yalnız A gazı ile başlayan bir tepkimede A, B ve C gazlarının derişimlerinin zamanla değişimi grafikte verilmiştir. A tamamen tükendiğinde tepkime sona ermiştir.\nI. Tepkime denklemi 2A(g) → B(g) + 3C(g) şeklindedir.\nII. 0–10 s aralığında A’nın ortalama harcanma hızı, 10–20 s aralığındakinden küçüktür.\nIII. 0–20 s aralığında B’nin ortalama oluşma hızı 0,06 mol/L·s’dir.\nBuna göre yukarıdaki yargılardan hangileri doğrudur?',
 sekil=SK,dogru=w6['dogru'],yan=w6['yan'],sira=w6['sira'],istenen='Grafiğe göre doğru olan yargılar.',
 ip=['Her yargıyı grafikteki derişim değişimlerinden ayrı ayrı sına.'],bilgi=[GRB,ORTB],
 puf='Derişim değişimlerinin oranı katsayıları verir; eğrinin dikliği hızın büyüklüğünü gösterir.')

# ================ 07 · orta · tanecik modeli, hız oranı
A1,B1,A2,B2=4,1,3,4   # Kap I: V hacminde; Kap II: V/2 hacminde
cA1,cB1,cA2,cB2=Fr(A1),Fr(B1),Fr(A2*2),Fr(B2*2)
r1=cA1**2*cB1; r2=cA2**2*cB2; assert (r1,r2,r2/r1)==(16,288,18)
d7=(Fr(A2**2*B2)/Fr(A1**2*B1), Fr(A2*2)**2*B2/r1, cA2*cB2/(cA1*cB1), cA2*cB2**2/(cA1*cB1**2)); assert d7==(Fr(9,4),9,12,96)
def kap(ox,w,ttl,hh,na,nb,posA,posB):
    o=[f'\\draw[thick] ({ox},0) rectangle ({ox+w},2.4);',f'\\node[anchor=south] at ({ox+w/2},2.45) {{{ttl}}};',f'\\node[anchor=north] at ({ox+w/2},-.05) {{{hh}}};']
    assert len(posA)==na and len(posB)==nb
    for (x,y) in posA: o.append(f'\\draw[fill=gray!45] ({ox+x},{y}) circle (.13);')
    for (x,y) in posB: o.append(f'\\draw[fill=white] ({ox+x},{y}) circle (.13);')
    return o
o=kap(0,2.4,'Kap I','Hacim: V',4,1,[(.5,.5),(1.7,.6),(1.0,1.5),(1.9,1.8)],[(.6,1.9)])
o+=kap(3.6,1.2,'Kap II','Hacim: V/2',3,4,[(.35,.4),(.85,1.0),(.35,1.6)],[(.85,.4),(.35,1.0),(.85,1.6),(.6,2.1)])
o+=['\\draw[fill=gray!45] (5.4,1.6) circle (.13); \\node[anchor=west] at (5.6,1.6) {A};','\\draw[fill=white] (5.4,1.0) circle (.13); \\node[anchor=west] at (5.6,1.0) {B};']
SK=tikz(o)
q('0007',7,[A('Derişimleri yaz','Kap I’de [A] = 4/V, [B] = 1/V; Kap II’de hacim V/2 olduğundan [A] = 3 ÷ (V/2) = 6/V, [B] = 4 ÷ (V/2) = 8/V.','I: 4 ve 1 · II: 6 ve 8 (1/V cinsinden)'),
   A('Hızları hesapla','r = k[A]²[B] denkleminde Kap I için 4² × 1 = 16, Kap II için 6² × 8 = 288.','16 · 288'),
   A('Oranla','288 ÷ 16 = 18.','r(II) ÷ r(I) = 18')],
 tipId='hz-denklem',z='orta',alt='Tanecik Modeli ve Hız',kaz='Farklı hacimli kaplardaki tanecik sayılarından derişimleri bulup hız denklemiyle başlangıç hızlarını oranlar.',kalip='şekilli',
 metin='Aynı sıcaklıkta iki ayrı kapta\n2A(g) + B(g) → C(g)\ntepkimesi başlatılıyor. Tepkimenin hız denklemi r = k[A]²[B]’dir. Kapların başlangıçtaki durumu şekilde verilmiştir; her tanecik aynı mol sayısını temsil etmektedir.\nBuna göre Kap II’deki başlangıç hızı, Kap I’dekinin kaç katıdır?',
 sekil=SK,dogru=18,yan=[(d7[0],'Hacim farkını göz ardı edip tanecik sayılarını doğrudan derişim almış: (3² × 4) ÷ (4² × 1) = 2,25.','dikkat'),
  (d7[1],'[A]’yı hacme göre düzeltmiş ama [B]’yi sayı olarak bırakmıştır: (6² × 4) ÷ 16 = 9.','islem'),
  (d7[2],'A’nın üssünü 1 almış: (6 × 8) ÷ (4 × 1) = 12; denklemde [A] ikinci kuvvettedir.','bilgi'),
  (d7[3],'Üsleri ters almış (r = k[A][B]²): (6 × 8²) ÷ (4 × 1²) = 96.','bilgi')],
 istenen='Kap II’deki başlangıç hızının Kap I’dekine oranı.',ip=['Kapların hacimleri farklıdır; bu, derişimleri nasıl etkiler?'],bilgi=[TAB],
 puf='Derişim, tanecik sayısının hacme bölümüdür; hızı denklemdeki üslerle hesapla.')

# ================ 08 · zor · basınç–zaman, C'nin oluşma hızı
V8=Fr(246,10); R8=Fr(82,1000); T8=300; assert R8*T8==V8
Pt={0:Fr(1),20:Fr(6,5),40:Fr(33,25),60:Fr(7,5),80:Fr(29,20)}
nn=lambda p:p*V8/(R8*T8); xx=lambda p:(nn(p)-1)/2
assert [xx(Pt[t]) for t in (0,20,40,60)]==[0,Fr(1,10),Fr(4,25),Fr(1,5)] and 3*xx(Pt[80])<1
C20,C40=4*xx(Pt[20]),4*xx(Pt[40]); rC=(C40-C20)/20; assert rC==Fr(3,250)
d8=(C20/20, C40/40, 4*(Pt[40]-Pt[20])/20, C40/20)
assert d8==(Fr(1,50),Fr(2,125),Fr(3,125),Fr(4,125)) and len({rC,*d8})==5
SK=pg('width=7.2cm,height=5.4cm,axis lines=left,xmin=0,xmax=90,ymin=0.9,ymax=1.6,xtick={0,20,40,60,80},ytick={1.0,1.2,1.32,1.4},yticklabel={\\pgfmathprintnumber[fixed,fixed zerofill,precision=2,use comma]{\\tick}},grid=major,major grid style={gray!45,thin},xlabel={Zaman (s)},ylabel={Toplam basınç (atm)},label style={font=\\small},tick label style={font=\\small}',
 f'\\addplot[thick,color=blue!70!black,smooth,mark=*,mark size=1.6pt] coordinates {{{co([(t,float(p)) for t,p in Pt.items()])}}};')
q('0008',8,[A('Toplam molü bul','PV = nRT ve V = 24,6 L, RT = 0,082 × 300 = 24,6 olduğundan n = P (mol); toplam mol 20 s’de 1,20, 40 s’de 1,32’dir.','n = 1,20 ve 1,32 mol'),
   A('İlerlemeyi bul','3A → B + 4C’de bir ilerlemede toplam mol 2 artar: x(20) = 0,10, x(40) = 0,16 mol.','Δn = 2x'),
   A('C’nin molünü bul','C’nin mol sayısı 4x’tir: 0,40 mol ve 0,64 mol.','Δn(C) = 0,64 − 0,40 = 0,24 mol'),
   A('Hızı hesapla','0,24 mol ÷ 20 s = 0,012 mol/s.','0,012 mol/s')],
 tipId='hz-ifade',z='zor',alt='Basınçtan Hız',kaz='Toplam basınç–zaman grafiğinden gaz hâlindeki bir ürünün ortalama oluşma hızını hesaplar.',kalip='grafik',
 metin='Hacmi 24,6 L olan sabit hacimli bir kaba yalnız A gazı konularak 300 K sabit sıcaklıkta\n3A(g) → B(g) + 4C(g)\ntepkimesi gerçekleştiriliyor. Kaptaki toplam basıncın zamanla değişimi grafikte verilmiştir. (R = 0,082 L·atm/mol·K)\nBuna göre tepkimenin 20–40 saniye aralığında C gazının ortalama oluşma hızı kaç mol/s’dir?',
 sekil=SK,dogru=rC,yan=[(d8[1],'0–40 s aralığındaki oluşumu (0,64 mol) 40 s’ye bölmüş: 0,64 ÷ 40 = 0,016; istenen aralık 20–40 s’dir.','dikkat'),
  (d8[0],'0–20 s aralığındaki oluşumu almış: 0,40 ÷ 20 = 0,02; istenen aralık 20–40 s’dir.','dikkat'),
  (d8[2],'Toplam basınç artışını (0,12 atm = 0,12 mol) doğrudan 4 ile çarpmış: 0,48 ÷ 20 = 0,024; toplam mol artışı ilerlemenin 2 katıdır.','islem'),
  (d8[3],'C’nin 0–40 s aralığındaki oluşumunu (0,64 mol) 20 s’ye bölmüş: 0,64 ÷ 20 = 0,032.','islem')],
 istenen='C gazının 20–40 s aralığındaki ortalama oluşma hızı.',ip=['Basınç değerlerini önce mol sayısına çevir, sonra ilerleme miktarını katsayılarla ilişkilendir.'],bilgi=[GZB,ORTB],
 puf='Toplam mol artışı ilerlemenin kaç katıdır, bunu denklemin katsayılarından bul.')

# ================ 09 · zor · kütle–zaman, iki deney
mCO2=Fr(44)
I_pts=[(0,Fr(0)),(10,Fr(11,5)),(20,Fr(33,10)),(30,Fr(198,50)),(40,Fr(22,5))]
II_pts=[(0,Fr(0)),(5,Fr(11,5)),(10,Fr(33,10)),(15,Fr(198,50)),(20,Fr(22,5))]
assert I_pts[-1][1]/mCO2==Fr(1,10)==Fr(10,100)
rI=(I_pts[2][1]-I_pts[1][1])/mCO2*2/10; rII=(II_pts[1][1]-II_pts[0][1])/mCO2/5
assert (rI,rII,rII/rI)==(Fr(1,200),Fr(1,100),2)
r_wrong=(II_pts[2][1]-II_pts[0][1])/mCO2/10; assert r_wrong/rI==Fr(3,2)
d9=(rII/(rI/2), rII*2/(rI/2), rI/rII, r_wrong/rI); assert d9==(4,8,Fr(1,2),Fr(3,2))
def kf(pts): return [(t,float(v)) for t,v in pts]
SK=pg('width=7cm,height=5.4cm,axis lines=left,xmin=0,xmax=44,ymin=0,ymax=5.3,xtick={0,5,10,15,20,25,30,35,40},ytick={0,1.1,2.2,3.3,4.4},yticklabel={\\pgfmathprintnumber[fixed,fixed zerofill,precision=1,use comma]{\\tick}},grid=major,major grid style={gray!45,thin},xlabel={Zaman (s)},ylabel={Kütle azalması (g)},label style={font=\\small},tick label style={font=\\small}',
 f'\\addplot[thick,color=blue!70!black,smooth,mark=*,mark size=1.6pt] coordinates {{{co(kf(I_pts))}}};\n\\addplot[thick,dashed,color=red!70!black,smooth,mark=square*,mark size=1.6pt] coordinates {{{co(kf(II_pts))}}};\n\\node[anchor=west,font=\\small] at (axis cs:31,2.7) {{Deney I}};\n\\node[anchor=west,font=\\small] at (axis cs:21.5,4.4) {{Deney II}};')
q('0009',9,[A('CO₂ miktarlarını bul','Deney I’de 10–20 s aralığında kütle 2,2 → 3,3 g azalır: 1,1 g CO₂ = 0,025 mol.','Δn(CO₂) = 0,025 mol'),
   A('I’de HCl’nin hızı','1 CO₂’ye karşılık 2 HCl harcanır: 0,05 mol ÷ 10 s = 0,005 mol/s.','0,005 mol/s'),
   A('II’de CaCO₃’ün hızı','0–5 s aralığında 2,2 g CO₂ = 0,05 mol; CaCO₃ da 0,05 mol azalır: 0,05 ÷ 5 = 0,01 mol/s.','0,01 mol/s'),
   A('Oranla','0,01 ÷ 0,005 = 2.','Oran = 2')],
 tipId='hz-faktor',z='zor',alt='Kütle Kaybıyla Hız',kaz='Kütle–zaman grafiğinden gaz çıkışını molüne çevirip farklı maddelerin ortalama hızlarını karşılaştırır.',kalip='grafik',
 metin='Aşırı miktarda HCl çözeltisi bulunan iki özdeş açık kaba, 10 gram CaCO₃ içeren iki ayrı örnek atılıyor (Deney I ve Deney II; örneklerin yüzey alanı farklıdır).\nCaCO₃(k) + 2HCl(suda) → CaCl₂(suda) + H₂O(s) + CO₂(g)\nKapların toplam kütlesindeki azalmanın zamanla değişimi grafikte verilmiştir. (CO₂: 44 g/mol)\nBuna göre Deney II’de 0–5 s aralığında CaCO₃’ün ortalama harcanma hızı, Deney I’de 10–20 s aralığında HCl’nin ortalama harcanma hızının kaç katıdır?',
 sekil=SK,dogru=2,yan=[(d9[3],'Deney II’de 0–5 s yerine 0–10 s aralığını almış: 0,0075 ÷ 0,005 = 1,5.','dikkat'),
  (d9[2],'Oranı ters kurmuş: 0,005 ÷ 0,01 = 0,5; istenen Deney II’deki hızın Deney I’dekine oranıdır.','dikkat'),
  (d9[0],'HCl’nin hızını CO₂ ile 1 : 1 saymış (0,0025): 0,01 ÷ 0,0025 = 4; HCl’nin katsayısı 2’dir.','bilgi'),
  (d9[1],'HCl’nin katsayısını (2) CaCO₃’e de uygulamış ve HCl’yi CO₂ ile 1 : 1 saymış: 0,02 ÷ 0,0025 = 8; CaCO₃’ün katsayısı 1’dir.','islem')],
 istenen='İki hızın birbirine oranı.',ip=['Grafikteki kütle azalması hangi maddenin kütlesine karşılık gelir?'],bilgi=[KTB],
 puf='Her aralık için hangi maddenin değişimi sorulduğuna ve katsayılara dikkat et.')

# ================ 10 · zor · iki katalizörlü diyagram, öncüllü
R10,P10,T0,T1,T2=50,20,140,110,95
assert (T0-R10,T0-P10,T1-R10,T1-P10,T2-R10,T2-P10)==(90,120,60,90,45,75)
assert (T2-P10)==(T0-R10)-15 and T2>R10 and T2<T1<T0 and P10-R10==-30
SK=pe([(R10,T0,P10,'solid',BLK),(R10,T1,P10,'dashed',BLU),(R10,T2,P10,'dotted',RED)],[P10,R10,T2,T1,T0],T0,[('Katalizörsüz','solid',BLK),('$K_1$','dashed',BLU),('$K_2$','dotted',RED)])
w10=onc([False,True,True],['ΔH girenlerle ürünlerin enerji farkıdır ve katalizör ΔH’ı değiştirmediğinden her iki yolda da −30 kJ’dir',
  'K₂’li yolun tepe noktası K₁’li yoldakinden düşüktür; Eₐ’sı küçük olan yol daha hızlıdır',
  'K₂’li yolda geri Eₐ = 95 − 20 = 75 kJ, katalizörsüz yolda ileri Eₐ = 140 − 50 = 90 kJ’dir; fark 15 kJ’dir'],3)
q('0010',10,[A('Enerjileri oku','Girenler 50, ürünler 20 kJ; tepeler 140 (katalizörsüz), 110 (K₁), 95 kJ (K₂).','Düzeyler okundu'),
   A('I’i değerlendir','ΔH = 20 − 50 = −30 kJ her yolda aynıdır; K₂ için de K₁ için de değişmez.','I: yanlış'),
   A('II’yi değerlendir','K₂’de ileri Eₐ = 45 kJ, K₁’de 60 kJ; tepe daha düşük olduğu için K₂’li yol daha hızlıdır.','II: doğru'),
   A('III’ü değerlendir','K₂’li yolda geri Eₐ = 95 − 20 = 75; katalizörsüz ileri Eₐ = 140 − 50 = 90; fark 15 kJ.','III: doğru'),
   A('Sonuç','II ve III doğrudur.','II ve III')],
 tipId='hz-katalizor',z='zor',alt='Katalizörlü Yollar',kaz='İki farklı katalizörlü yola ait enerji diyagramından ΔH, hız ve aktivasyon enerjilerini karşılaştırır.',kalip='şekilli',
 metin='Aynı tepkime için katalizörsüz yol ile K₁ ve K₂ katalizörlerinin kullanıldığı iki yola ait potansiyel enerji–tepkime koordinatı grafiği şekilde verilmiştir.\nI. K₂ kullanılan yolda tepkime entalpisi (ΔH), K₁ kullanılan yoldakinden küçüktür.\nII. Aynı sıcaklıkta tepkime hızı K₂ varlığında K₁ varlığındakinden büyüktür.\nIII. K₂ kullanılan yolda geri tepkimenin aktivasyon enerjisi, katalizörsüz yolda ileri tepkimenin aktivasyon enerjisinden 15 kJ küçüktür.\nBuna göre yukarıdaki yargılardan hangileri doğrudur?',
 sekil=SK,dogru=w10['dogru'],yan=w10['yan'],sira=w10['sira'],istenen='Şekle göre doğru olan yargılar.',
 ip=['Her yargı için ilgili enerji düzeylerini grafikten okuyup farkları ayrı ayrı hesapla.'],bilgi=[KATB],
 puf='Aktivasyon enerjisi, tepe noktası ile ilgili yönün başlangıç düzeyi arasındaki farktır.')

# ================ yaz
for qq in P.ANA: qq['kardes']=None
SC='/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/hiziki'; os.makedirs(SC,exist_ok=True)
P.yaz(os.path.join(GD,'hiziki-1.json'),os.path.join(SC,'bos-hiziki.json'))
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu='akim|Kimyasal Tepkimelerde Hız'))['kartlar'].append(c['id'])
json.dump(dict(konu='Kimyasal Tepkimelerde Hız',surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2018–2026 Kimya (yalnız mantık), MEB 11. sınıf kimya.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','akhiziki.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
