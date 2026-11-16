"""TYT Kimya · Kimya Her Yerde · ek paket (heryerdeiki): 14 soru, kardeş yok, ipucu 1.
Şekil verileri Python'da hesaplanır; TikZ bu değerlerden üretilir. Öncüllerin doğruluğu betikte TEK yerde (durum sözlüğü) tanımlanır."""
import sys,os,math
GD=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,GD)
import _hafif_kim2 as H
from _hafif_kim2 import *
from _hafif_kim import onc,tek,etk
KONU_='Kimya Her Yerde'; UK='kim|Kimya Her Yerde'
H.KONU=KONU_
P=Parti('heryerdeiki',KONU_,UK,ders='TYT Kimya',idon='tytkim')
KY='ÖSYM 2018–2026 TYT Kimya (yalnız mantık) · MEB 10. sınıf Kimya Her Yerde'
TIPAD={'sabun':'Sabun molekülü ve temizleme','polimer':'Polimerler: yapı ve kullanım','geridon':'Geri dönüşüm ve sürdürülebilirlik','gida':'Gıda katkı ve saklama','kozmetik':'Kozmetik ve ilaçlar','temizlik':'Temizlik maddelerinin güvenli kullanımı'}
def S(no,alt,tp,z,kalip,fikir,tuzak,kaz,oz,deg,ad,**k):
    kart(f'K-KMHY2-{no[-2:]}',alt,fikir,tuzak,z,kalip,len(ad),f'km-hy2-{tp}',TIPAD[tp],KY)
    if 'yan' in k: k['yan']=[(a,b.replace('..','.'),c) for a,b,c in k['yan']]
    mk(P,no,ad=ad,adim=len(ad),tipId=f'km-hy2-{tp}',tip=TIPAD[tp],z=z,alt=alt,kaz=kaz,kalip=kalip,kart=f'K-KMHY2-{no[-2:]} ({oz}) · {deg}',**k)
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
ARR='-{Stealth[length=2mm,width=1.8mm]}'
def tk(g): return tikz_svg(HEAD+g+TAIL)
def oncadim(durum,sonuc):
    """durum sözlüğünden adım listesi (tek kaynak)"""
    ad=[A(f'{k} öncülünü değerlendir',(('İ' if v[1][0]=='i' else v[1][0].upper()))+v[1][1:],f'{k}: '+('doğru' if v[0] else 'yanlış')) for k,v in durum.items()]
    ad.append(A('Sonuç','Doğru öncüller bir arada okunur.',sonuc)); return ad
# ============ 01 · sabun molekülü şeması · orta · öncüllü ============
d1={'I':(True,'iyonik uç polar olduğundan su molekülleriyle etkileşir.'),
    'II':(False,'hidrokarbon zinciri apolardır; polar su moleküllerinde iyi çözünmez.'),
    'III':(True,'apolar hidrokarbon zinciri, yağ gibi apolar maddelerle etkileşir.')}
r1=onc(d1,[('I',),('II',),('III',),('I','II'),('I','III')])
assert r1['dogru']=='I ve III'
g='\\draw[thick,fill=vurgu!15] (0,0) circle (.62); \\node at (0,0) {\\ce{COO^-}};\\node at (-.2,-.9) {\\ce{Na+}};'
pts=[(.62+0.0,0)]
x=.62; y=0
zig=[(.62,0)]
for i in range(1,10): zig.append((.62+i*.42,.26 if i%2 else 0))
g+='\\draw[thick] '+' -- '.join(f'({a:.2f},{b:.2f})' for a,b in zig)+';'
g+='\\node at (0,1.1) {\\textbf{I}}; \\draw[thick] (0,.72) -- (0,.9); \\node at (2.5,1.0) {\\textbf{II}}; \\draw[thick] (2.5,.6) -- (2.5,.82);'
g+='\\draw[thick,decorate,decoration={brace,amplitude=4pt,mirror}] (.7,-.35) -- (4.4,-.35);'
SK1=tk(g)
S('0001','Sabun ve Deterjanlar','sabun','orta','öncüllü','Sabun molekülünün iyonik (polar) ucu su ile, apolar zinciri yağ ile etkileşir; temizleme bu iki yönlü yapıya dayanır.','Hidrokarbon zincirinin de polar ve suda çözünür sanılması.','Sabun molekülünün iki kısmının özelliklerini şemadan yorumlar.','sabun molekülü şeması','üç öncül, zincirin apolarlığı',
 oncadim(d1,'I ve III'),sekil=SK1,
 metin='Bir kimya öğretmeni, sabunun yağlı kirleri neden temizleyebildiğini anlatmak için sabun molekülünün yapısını şekildeki gibi şematik olarak çizmiştir. Moleküldeki iki farklı kısım I ve II ile gösterilmiştir. Öğrencilerden bu kısımların özelliklerini yorumlamaları istenmiştir.\nI. I ile gösterilen iyonik uç, su molekülleriyle etkileşebilir.\nII. II ile gösterilen zincir kısmı polar olduğundan suda iyi çözünür.\nIII. II ile gösterilen zincir kısmı, yağ gibi apolar maddelerle etkileşebilir.\nBuna göre bu ifadelerden hangileri doğrudur?',
 istenen='Doğru ifadelerin belirlenmesi.',ip=['Şekilde iyonik grup ile uzun hidrokarbon zinciri birbirinden farklı özelliktedir; hangisinin hangi madde türüyle uyumlu olduğunu düşün.'],
 bilgi=[B('Polar ve apolar kısımlar','benzer benzeri çözer: polar maddeler polar maddelerle, apolar maddeler apolar maddelerle etkileşir. Örnek: sofra tuzu suda çözünür, bal mumu çözünmez')],
 puf='Benzer benzeri çözer: iyonik uç suyu, hidrokarbon zinciri yağı sever.',**r1)

# ============ 02 · mizel şeması · orta · şekilli ============
N=12; ry,rt,rh=1.0,2.1,2.3
g=f'\\draw[thick,fill=orange!25] (0,0) circle ({ry});'
for i in range(N):
    a=math.radians(i*360/N+15); c,s=math.cos(a),math.sin(a)
    g+=f'\\draw[thick] ({ry*c:.3f},{ry*s:.3f}) -- ({rt*c:.3f},{rt*s:.3f});\\draw[thick,fill=vurgu!30] ({rh*c:.3f},{rh*s:.3f}) circle (.17);'
a=math.radians(15+30*1); c,s=math.cos(a),math.sin(a)     # K: baş (i=1)
g+=f'\\draw[thin] ({2.5*c:.3f},{2.5*s:.3f}) -- ({3.2*c:.3f},{3.2*s:.3f}); \\node at ({3.45*c:.3f},{3.45*s:.3f}) {{\\textbf{{K}}}};'
a2=math.radians(15+30*8+15); c2,s2=math.cos(a2),math.sin(a2)   # L: zincir (i=8) için ok, işaret iki molekül arasından
a8=math.radians(15+30*8); c8,s8=math.cos(a8),math.sin(a8)
g+=f'\\draw[thin] ({1.6*c8:.3f},{1.6*s8:.3f}) -- ({3.2*c2:.3f},{3.2*s2:.3f}); \\node at ({3.45*c2:.3f},{3.45*s2:.3f}) {{\\textbf{{L}}}};'
SK2=tk(g)
yan2=[('K uçları yağ damlasıyla, L kısımları ise su molekülleriyle etkileşir.',False,'iyonik uç polar olduğundan suyla, apolar zincir yağla etkileşir.'),
 ('Yağ damlası apolar olduğu için sabun moleküllerinin iyonik uçlarına tutunmuştur.',False,'apolar yağ, iyonik uca değil apolar zincire tutunur.'),
 ('L kısımları su molekülleriyle hidrojen bağı yaparak yağ damlasını çözmüştür.',False,'apolar zincir su ile hidrojen bağı yapamaz.'),
 ('K uçları suyla, L kısımları yağ damlasıyla etkileştiğinden damla su içinde dağılmış kalmıştır.',True,''),
 ('Sabun, yağ damlasını başka bir maddeye dönüştürerek ortamdan kaldırmıştır.',False,'temizleme, yağın başka maddeye dönüşmesiyle değil fiziksel etkileşimlerle gerçekleşir.')]
def kon(r,harf):
    """tek() sonucunda doğru şıkkı verilen harfe taşır, öteki sıra korunur"""
    sr=[x for x in r['sira'] if x!=r['dogru']]; sr.insert('ABCDE'.index(harf),r['dogru']); r['sira']=sr; return r
r2=kon(tek(yan2,True),'A')
S('0002','Sabun ve Deterjanlar','sabun','orta','şekilli','Sabun molekülleri apolar zincirleriyle yağ damlasını sararken iyonik uçlarını suya yöneltir; böylece yağ su içinde asılı kalır.','Yağ ile iyonik ucu, su ile hidrokarbon zincirini eşleştirmek.','Yağ damlasının çevresindeki sabun moleküllerinin dizilişini yorumlar.','temizleme şeması','yağ damlası çevresinde sabun molekülleri',
 [A('Yağ damlasının yapısı','Yağ apolar bir maddedir; apolar kısımlarla etkileşir.','yağ: apolar'),A('Şekildeki dizilişi oku','Damlaya bakan L kısımları zincirlerdir; suya bakan K kısımları iyonik uçlardır.','L: zincir · K: iyonik uç'),A('Etkileşimleri eşle','Apolar zincir yağla, polar uç suyla etkileşir.','L–yağ · K–su'),A('İfadeyi seç','Bu eşleşmeyi doğru anlatan ifade damlanın neden suda dağıldığını da açıklar.','sonuç: K suyla, L yağla')],sekil=SK2,
 metin='Yağlı bir kumaşa sabunlu su uygulanıp ovulunca yağ lekesi küçük damlalar hâlinde kumaştan ayrılmış ve suda dağılmıştır. Şekilde, bu damlalardan birinin çevresinde sabun moleküllerinin dizilişi şematik olarak gösterilmiştir. Sabun moleküllerinin K ile gösterilen uçları ile L ile gösterilen zincir kısımları farklı özelliktedir.\nBuna göre, şekil ve verilen bilgilere göre aşağıdakilerden hangisi söylenebilir?',
 istenen='Şekle uygun olan ifadenin belirlenmesi.',ip=['Damlanın iç yanında yağ, dış yanında su vardır; her bölgeye hangi tür ucun döndüğünü düşün.'],
 bilgi=[B('Polar ve apolar etkileşim','polar uç polar su moleküllerine, apolar zincir apolar maddelere çekilir; benzer benzeri çözer. Örnek: tuz suda çözünür, bal mumu çözünmez')],
 puf='İçe dönen apolar zincirler yağı, dışa dönen polar uçlar suyu tutar.',**r2)


# ============ 03 · teflon zinciri atom sayısı · orta · şekilli ============
nb=150; n_C,n_F=2,4
assert nb*(n_C+n_F)==900 and nb*n_C==300 and nb*3==450 and nb*n_F==600 and nb*5==750
g='\\draw[thick] (-2.1,.4) -- (-.9,-.3) -- (-.1,.2) -- (1.1,-.5); \\draw[dashed] (-2.1,.4) -- (-2.6,.7); \\draw[dashed] (1.1,-.5) -- (1.6,-.8);'
for xc,yc,up in [(-.9,-.3,-1),(-.1,.2,1)]:
    for dx in (-.35,.35):
        g+=f'\\draw[thick] ({xc},{yc}) -- ({xc+dx},{yc+up*.55}); \\node at ({xc+dx*1.25},{yc+up*.8}) {{F}};'
for xc,yc in [(-.9,-.3),(-.1,.2)]:
    g+=f'\\node[fill=white,inner sep=1pt] at ({xc},{yc}) {{C}};'
g+='\\draw[thick] (-1.35,-1.25) -- (-1.5,-1.25) -- (-1.5,1.25) -- (-1.35,1.25); \\draw[thick] (.35,-1.25) -- (.5,-1.25) -- (.5,1.25) -- (.35,1.25);\\node at (.75,-1.15) {$n$};'
SK3=tk(g)
S('0003','Polimerler','polimer','kolay','şekilli','Polimer, monomerlerin zincir hâlinde birleşmesiyle oluşur; tekrar eden birimdeki atom sayısı zincirdeki toplam atom sayısını belirler.','Tekrar eden birimdeki atomları eksik ya da fazla saymak.','Tekrar eden birimi verilen polimerin zincirindeki atom sayısını hesaplar.','teflon zinciri','tekrar birimi ve n sayısı',
 [A('Birimi oku','Köşeli parantez içindeki parça tekrar eden birimdir; atomlarını tek tek say.','2 C + 4 F'),A('Birimdeki atom sayısı','Karbon ve flor atomları toplanır.','2 + 4 = 6 atom'),A('Zincire uygula','Zincirde 150 tekrar birimi bulunur; uç grupları ihmal edilir.','150 × 6'),A('Sonuç','Toplam atom sayısı hesaplanır.','900 atom')],sekil=SK3,
 metin='Yüzey kaplamalarında kullanılan teflon, tek tür küçük molekülün çok sayıda birleşmesiyle oluşan bir polimerdir. Şekilde bu polimerin zincirinden bir parça ve köşeli parantezle gösterilen tekrar eden birim ve zincirin uçlarındaki bağlar verilmiştir. Bir araştırmacı, uç grupları ihmal edilecek biçimde 150 tekrar biriminden oluşan tek bir teflon zincirini incelemiştir.\nBuna göre bu zincirdeki toplam atom sayısı kaçtır?',
 dogru=nb*(n_C+n_F),yan=[(nb*n_C,'Yalnız karbon atomlarını saymış: 150 × 2 = 300.','dikkat'),(nb*3,'Birimi CF₂ gibi üç atomlu sanmış: 150 × 3 = 450.','bilgi'),(nb*n_F,'Yalnız flor atomlarını saymış: 150 × 4 = 600.','dikkat'),(nb*5,'Birimde beş atom saymış: 150 × 5 = 750.','islem')],
 istenen='Zincirdeki toplam atom sayısı.',ip=['Önce köşeli parantez içindeki bir tekrar biriminde kaç atom bulunduğunu say.'],
 bilgi=[B('Monomer ve polimer','monomer, polimeri oluşturan küçük moleküldür; polimerde monomerden gelen birim tekrar eder. Örnek: polietilen, etilen (CH₂=CH₂) monomerlerinin art arda birleşmesiyle oluşur')],
 puf='Zincirdeki atom sayısı = tekrar birimindeki atom sayısı × birim sayısı.')

# ============ 04 · PVC zinciri · zor · şekilli ============
# zincir: -CH2-CHCl-CH2-CHCl-  (4 karbon)
sub=[('H','H'),('H','Cl'),('H','H'),('H','Cl')]
xs=[i*1.0 for i in range(4)]; ys=[0 if i%2==0 else .5 for i in range(4)]
g='\\draw[dashed] (-.7,.25) -- (-.0,0); \\draw[thick] '+' -- '.join(f'({x},{y})' for x,y in zip(xs,ys))+'; \\draw[dashed] (3.0,.5) -- (3.7,.25);'
for i,(x,y) in enumerate(zip(xs,ys)):
    up=1 if i%2 else -1
    for dx,lab in zip((-.32,.32),sub[i]):
        g+=f'\\draw[thick] ({x},{y}) -- ({x+dx},{y+up*.5}); \\node at ({x+dx*1.45},{y+up*.78}) {{{lab}}};'
    g+=f'\\node[fill=white,inner sep=1pt] at ({x},{y}) {{C}};'
SK4=tk(g)
s4=['Etilen (CH₂=CH₂) · market poşeti','Etilen (CH₂=CH₂) · su borusu','Vinil klorür (CH₂=CHCl) · içecek şişesi','Vinil klorür (CH₂=CHCl) · su borusu','Tetrafloroeten (CF₂=CF₂) · yapışmaz tava kaplaması']
S('0004','Polimerler','polimer','orta','şekilli','Zincirdeki yan atomlardan monomer bulunur; polimerin kullanım alanı bilinen plastik türüyle eşleşir.','Yalnız monomeri ya da yalnız kullanım alanını doğru eşleştirip öteki bilgiyi karıştırmak.','Yapısı verilen polimerin monomerini ve kullanım alanını belirler.','polimer zinciri','klor atomlu zincir',
 [A('Zinciri incele','Karbon iskeleti üzerinde H ve Cl atomları bulunur; F atomu yoktur.','C, H, Cl'),A('Monomeri bul','Tekrar eden birim –CH₂–CHCl– biçimindedir; monomer çift bağlı CH₂=CHCl’dir.','CH₂=CHCl'),A('Polimeri tanı','Klor içeren bu zincir PVC (polivinil klorür) polimeridir.','PVC'),A('Kullanımı eşle','PVC sert ve dayanıklı olduğundan su ve atık su borularında kullanılır.','vinil klorür + su borusu')],sekil=SK4,
 metin='Bir laboratuvarda, atık plastik yığınından alınan bir parçanın hangi polimer olduğu belirlenmeye çalışılmıştır. Analiz sonucunda parçanın zincir yapılı bir polimer olduğu anlaşılmış ve zincirden bir bölüm şekildeki gibi çizilmiştir. Karbon atomları zincirin iskeletini oluşturmakta, her karbona bağlı atomlar şekilde gösterilmektedir.\nBuna göre bu polimerin monomeri ile kullanım alanı aşağıdakilerden hangisinde doğru verilmiştir?',
 dogru=s4[3],sira=[s4[0],s4[3],s4[1],s4[2],s4[4]],yan=[(s4[0],'Zincirdeki Cl atomlarını görmemiş; etilenden oluşan polietilenle karıştırmış.','dikkat'),(s4[1],'Monomeri etilen sanmış ve polimerin kullanımını boruyla eşlemiş; Cl atomları etilende bulunmaz.','bilgi'),(s4[2],'Monomeri doğru bulmuş ama kullanım alanını PET’le karıştırmış.','bilgi'),(s4[4],'Zincirdeki Cl atomlarını F sanmış; teflonun yapısıyla karıştırmış.','dikkat')],
 istenen='Monomer ve kullanım alanı.',ip=['Zincirde hangi element atomlarının bulunduğuna bak; monomerde de aynı atomlar bulunur.'],
 bilgi=[B('Monomer–polimer ilişkisi','polimerin monomeri, zincirdeki tekrar eden birimden çift bağın açılmış hâli olarak bulunur. Örnek: etilen (CH₂=CH₂) monomerinden polietilen elde edilir')],
 puf='Zincirdeki yan atomlar monomeri verir; monomerden polimerin adı ve kullanımı bulunur.')

# ============ 05 · polimer–kullanım tablosu · orta · öncüllü ============
d5={'I':(True,'PVC, sert ve dayanıklı olduğundan su ve kanalizasyon borularında kullanılır.'),
    'II':(False,'plastik içecek şişeleri PET’ten üretilir; teflon yapışmaz kaplamada kullanılır.'),
    'III':(True,'polietilen (PE) market poşeti gibi ince ve esnek ürünlerde kullanılır.'),
    'IV':(False,'yapışmaz tava kaplaması teflondur; PET içecek şişelerinde kullanılır.')}
r5=onc(d5,[('I',),('I','II'),('I','III'),('II','IV'),('I','III','IV')])
assert r5['dogru']=='I ve III'
SK5=tablo_svg(['No','Kullanım alanı','Polimer'],[['I','Su ve kanalizasyon boruları','PVC'],['II','Plastik içecek şişesi','Teflon'],['III','Market poşeti','PE'],['IV','Yapışmaz tava kaplaması','PET']])
S('0005','Polimerler','polimer','orta','öncüllü','Yaygın polimerlerin kullanım alanları: PE poşet, PVC boru, PET içecek şişesi, teflon yapışmaz kaplama.','PET ile teflonu birbirine karıştırmak.','Yaygın polimerlerin kullanım alanlarını eşleştirir.','polimer–kullanım tablosu','dört satırlı tablo, iki yanlış',
 oncadim(d5,'I ve III'),sekil=SK5,
 metin='Bir okulun kimya kulübü, günlük hayattaki plastik ürünlerin yapıldığı polimerleri araştırmıştır. Öğrenciler buldukları bilgileri aşağıdaki tabloda her satıra bir numara vererek özetlemiştir. Kulüp danışmanı tabloyu kontrol ederek hatalı satırların bulunup bulunmadığını sormuştur.\nBuna göre tablodaki hangi satırlarda kullanım alanı ile polimer doğru eşleştirilmiştir?',
 istenen='Doğru eşleştirilmiş satırlar.',ip=['Her satırdaki ürünü düşün: ürünün esnek, sert ya da ısıya dayanıklı olması hangi polimerle uyuşur?'],
 bilgi=[B('Polimerlerin kullanımı','polimerler, zincirin yapısına göre farklı özellik gösterir; bu özellik kullanım alanını belirler. Örnek: polistiren köpük tabaklar ve ambalaj dolgusu yapımında kullanılır')],
 puf='PE esnek poşet, PET içecek şişesi, PVC boru, teflon yapışmaz kaplama demektir.',**r5)

# ============ 06 · geri dönüşüm kodları tablosu · kolay · tablo ============
SK6=tablo_svg(['Kod','Plastik türü','Örnek ürün'],[['1','PET','Meşrubat şişesi'],['2','PE-HD','Deterjan şişesi'],['3','PVC','Pencere profili'],['4','PE-LD','Streç film'],['5','PP','Yoğurt kabı'],['6','PS','Köpük tabak']])
s6=['Yoğurt kabı ve köpük tabak','Yoğurt kabı ve deterjan şişesi','Deterjan şişesi ve streç film','Köpük tabak ve streç film','Yoğurt kabı, deterjan şişesi ve streç film']
S('0006','Geri Dönüşüm','geridon','kolay','tablo','Ambalajlardaki geri dönüşüm kodu plastik türünü belirler; atıklar türüne göre ayrılır.','Ürünü ilk bildiği plastik türüyle eşleştirip tablodaki kodu okumamak.','Geri dönüşüm kodlarına göre plastik atıkları ayrıştırır.','geri dönüşüm kodu','kod tablosu, PE türleri',
 [A('Tabloyu oku','Her ürünün altında yer alan plastik türünü tablodan bul.','yoğurt kabı: PP · deterjan şişesi: PE-HD · köpük tabak: PS · streç film: PE-LD'),A('Hedef türü belirle','Kutuya yalnız PE türleri (PE-HD ve PE-LD) konacaktır.','PE-HD, PE-LD'),A('Ürünleri seç','Bu türde olan iki ürün ayrılır.','deterjan şişesi, streç film')],sekil=SK6,
 metin='Bir apartman yönetimi, plastik atıkları ambalajların altındaki geri dönüşüm koduna göre ayırmaktadır. Yönetimin kullandığı kod listesi tabloda verilmiştir. Apartmanda oturan bir aile, yoğurt kabı, deterjan şişesi, köpük tabak ve streç filmi toplamıştır. Yönetim, polietilen (PE) türlerini tek bir kutuda toplamaktadır.\nBuna göre aile, bu kutuya hangi ambalajları atmalıdır?',
 dogru=s6[2],sira=[s6[0],s6[1],s6[3],s6[2],s6[4]],yan=[(s6[0],'Kodları okumadan yoğurt kabıyla köpük tabağı polietilenden sanmış; bunlar PP ve PS’tir.','dikkat'),(s6[1],'Yoğurt kabını PE türü sanmış; yoğurt kabı PP’dir.','bilgi'),(s6[3],'Köpük tabağı PE-LD sanmış; köpük tabak PS’tir.','bilgi'),(s6[4],'Yoğurt kabını da PE türü saymış; yoğurt kabı PP’dir.','bilgi')],
 istenen='Kutuya atılacak ambalajlar.',ip=['Önce her ambalajın tablodaki türünü bul.'],
 bilgi=[B('Geri dönüşüm kodu','plastik ambalajların altındaki sayı ve kısaltma, plastiğin türünü belirtir; farklı plastikler karıştırılmadan geri dönüştürülür. Örnek: ambalajın altındaki “1” sayısı ve PET yazısı, plastiğin türünü belirtir')],
 puf='Önce ambalajın kodunu tablodan bul, sonra kutunun plastik türüyle karşılaştır.')

# ============ 07 · geri dönüşüm simgesi · kolay · şekilli ============
R_=1.5
v=[(R_*math.cos(math.radians(a)),R_*math.sin(math.radians(a))) for a in (90,210,330)]
g=''
for i in range(3):
    (x1,y1),(x2,y2)=v[i],v[(i+1)%3]
    g+=f'\\draw[line width=2pt,{ARR}] ({x1+(x2-x1)*.12:.3f},{y1+(y2-y1)*.12:.3f}) -- ({x1+(x2-x1)*.88:.3f},{y1+(y2-y1)*.88:.3f});'
g+='\\node at (0,0) {\\huge\\textbf{1}}; \\node at (0,-1.4) {\\large\\textbf{PET}};'
SK7=tk(g)
yan7=[('İşaretteki 1 sayısı, ambalajın bir kez geri dönüştürüldüğünü gösterir.',False,'sayı plastik türünü belirtir, geri dönüşüm sayısını değil.'),
 ('PET kısaltması, şişenin camdan yapıldığını gösterir.',False,'PET bir plastik türüdür.'),
 ('İşaret, şişenin doğada kısa sürede kendiliğinden çözündüğünü gösterir.',False,'işaret çözünürlük bilgisi değil, plastik türü ve geri dönüşüm bilgisi verir.'),
 ('İşaret, şişenin PET plastikten üretildiğini ve ayrıştırılarak geri dönüştürülebileceğini gösterir.',True,''),
 ('İşaret, şişenin tüm plastiklerle aynı kutuya atılması gerektiğini gösterir.',False,'plastikler türüne göre ayrı geri dönüştürülür.')]
r7=kon(tek(yan7,True),'A')
S('0007','Geri Dönüşüm','geridon','kolay','şekilli','Geri dönüşüm simgesindeki sayı ve kısaltma plastik türünü bildirir; ambalaj ayrıştırılarak geri dönüştürülebilir.','Simgedeki sayıyı geri dönüşüm sayısı sanmak.','Geri dönüşüm simgesinin anlamını yorumlar.','geri dönüşüm simgesi','üç oklu simge',
 [A('Simgeyi oku','Üçgen oklar geri dönüşümü, ortadaki sayı ile altındaki harfler plastik türünü gösterir.','1 · PET'),A('Anlamları eşle','Sayı kaç kez geri dönüştürüldüğünü değil, plastik türünü belirtir.','sayı = tür kodu'),A('İfadeyi seç','Plastik türünü ve geri dönüşüme uygunluğu doğru anlatan ifade seçilir.','doğru ifade seçildi')],sekil=SK7,
 metin='Bir gazoz şişesinin altında şekildeki işaret bulunmaktadır. Atıkları ayıran bir öğrenci ile arkadaşları işaretle ilgili yorumlarını paylaşmış ve hangi yorumun doğru olduğunu tartışmışlardır.\nBuna göre aşağıdakilerden hangisi doğrudur?',
 istenen='Doğru yorumun belirlenmesi.',ip=['Simgenin üç parçasını ayrı ayrı düşün: ok biçimi, ortadaki sayı ve alttaki yazı.'],
 bilgi=[B('Geri dönüşüm işareti','üçgen biçimli oklar, ambalajın geri dönüşüme uygun olduğunu; sayı ve kısaltma ise malzemenin türünü belirtir. Örnek: cam ve metal ambalajlarda da farklı geri dönüşüm işaretleri kullanılır')],
 puf='Simgedeki sayı ve harfler malzemenin türünü bildirir.',**r7)

# ============ 08 · haftalık atık grafiği · zor · grafik ============
ATIK={'Cam':6,'Kâğıt':12,'Plastik':8,'Metal':4,'Organik':20}
kirli=Fr(1,4); hafta=4
pvc=Fr(1,4); gd=ATIK['Cam']+ATIK['Metal']+ATIK['Plastik']*(1-pvc)+ATIK['Kâğıt']*(1-kirli); assert gd==25
cevap8=gd*hafta; assert cevap8==100
assert (gd+ATIK['Kâğıt']*0)*hafta==100 and 27*hafta==108 and 30*hafta==120 and ATIK['Organik']*hafta==80 and gd!=100
g='\\draw[->,thick] (0,0) -- (0,5.1) node[above] {\\small kg}; \\draw[thick] (0,0) -- (6.3,0);'
for yv in range(0,21,2):
    yy=yv*.24
    g+=f'\\draw[thin,gray!40] (0,{yy}) -- (6.2,{yy}); \\draw[thick] (-.06,{yy}) -- (.06,{yy}); \\node[left] at (-.08,{yy}) {{\\footnotesize {yv}}};'
for i,(k,vv) in enumerate(ATIK.items()):
    x0=.35+i*1.2
    g+=f'\\draw[thick,fill=vurgu!35] ({x0},0) rectangle ({x0+.8},{vv*.24}); \\node[below] at ({x0+.4},-.05) {{\\footnotesize {k}}};'
SK8=tk(g)
S('0008','Geri Dönüşüm','geridon','zor','grafik','Grafikten okunan atık miktarları ile geri dönüşüm koşullarından (kirlilik, PVC içeriği) kutuya girecek atık bulunur.','Plastiğin PVC içeren kısmını ya da kirli kâğıdı kutuya dahil etmek.','Geri dönüşüm koşullarına göre atık grafiğinden geri dönüştürülebilir miktarı bulur.','atık grafiği','çubuk grafik, iki koşul',
 [A('Grafiği oku','Her çubuğun yüksekliğinden haftalık atık miktarı (kg) okunur.','cam 6 · kâğıt 12 · plastik 8 · metal 4 · organik 20'),A('Kutuya girecek türleri seç','Organik atık kompost alanına gider; cam, kâğıt, plastik ve metal kutuya gider.','organik hariç'),A('Kâğıt koşulu','Kâğıdın dörtte biri kirli olduğundan kutuya konmaz.','12 − 3 = 9 kg'),A('Plastik koşulu','Plastiğin dörtte biri PVC içerdiğinden kutuya konmaz.','8 − 2 = 6 kg'),A('Haftalık toplam','Kutuya giren atıklar toplanır.','6 + 9 + 6 + 4 = 25 kg'),A('Dört haftaya yay','Miktar her hafta aynıdır.','25 × 4 = 100 kg')],sekil=SK8,
 metin='Bir sitenin yönetimi, haftalık atık miktarlarını grafikteki gibi belirlemiştir. Yönetim cam, kâğıt, plastik ve metal atıkları geri dönüşüm kutularına, organik atıkları ise mikroorganizmaların ayrıştırması için kompost alanına yönlendirmektedir. Kâğıt atıklarının dörtte biri yağ ve yiyecek artıklarıyla kirlendiğinden, plastik atıklarının dörtte biri ise PVC içerdiğinden anlaşmalı tesiste geri dönüştürülememekte ve kutuya konmamaktadır. Atık miktarlarının dört hafta boyunca grafikteki gibi kaldığı kabul edilmiştir.\nBuna göre dört haftada geri dönüşüm kutularında toplanacak atık kaç kg’dır?',
 dogru=cevap8,yan=[(gd,'Yalnız bir haftalık miktarı hesaplamış: 25 kg.','dikkat'),(ATIK['Organik']*hafta,'Kutuya giren atık yerine organik atığı almış: 20 × 4 = 80.','dikkat'),(108,'Plastikteki PVC payını çıkarmamış: 27 × 4 = 108.','bilgi'),(120,'Kâğıt ve plastik koşullarının ikisini de atlamış: 30 × 4 = 120.','bilgi')],
 istenen='Dört haftada kutularda toplanacak atık (kg).',ip=['Önce hangi atık türlerinin kutuya gireceğini, sonra bunlardan hangilerinin miktarının koşullarla azaldığını belirle.'],
 bilgi=[B('Atık yönetimi','atıklar türüne göre ayrılır: kâğıt, cam, plastik ve metal geri dönüştürülür; organik atık kompost yapılır. Kirli ya da farklı plastik türleriyle karışmış atıklar geri dönüşümü zorlaştırır')],
 puf='Önce kutuya girecek atık türlerini ve koşulları belirle, sonra haftalık miktarı süreyle çarp.')

# ============ 09 · gıda saklama tablosu · orta · tablo · olumsuz kök ============
SK9=tablo_svg(['Yöntem','Gıda örneği','Temel ilke'],[['Konserve','Domates','Isıtılıp hava almayacak kapatılır'],['Kurutma','Kayısı','Su giderilir, çoğalma engellenir'],['Dondurma','Biber','Çok düşük sıcaklıkta mikroorganizmalar ölür'],['Tuzlama','Zeytin','Tuz suyu çeker, çoğalma engellenir'],['Sirkeleme','Salatalık','Asidik ortamda çoğalma engellenir']])
yan9=[('Konserve',True,'konservede gıda ısıtılarak mikroorganizmalar öldürülür ve kapak hava girmeyecek biçimde kapatılır.'),
 ('Kurutma',True,'mikroorganizmalar çoğalmak için suya gereksinim duyar; sudan arındırılan gıdada çoğalamazlar.'),
 ('Dondurma',False,'çok düşük sıcaklıkta mikroorganizmalar genellikle ölmez; yalnız çoğalmaları ve tepkimeleri yavaşlar ya da durur.'),
 ('Tuzlama',True,'tuz gıdadan suyu çeker ve mikroorganizmaların çoğalmasını engeller.'),
 ('Sirkeleme',True,'sirkedeki asetik asit ortamı asidik yapar ve mikroorganizmaların çoğalmasını engeller.')]
r9=kon(tek(yan9,False),'A')
S('0009','Gıdalar','gida','orta','tablo','Gıda saklama yöntemleri mikroorganizmaların çoğalmasını engeller ya da yavaşlatır; dondurma onları yok etmez, yalnız etkinliğini durdurur.','Dondurmayı mikroorganizmaları öldüren bir yöntem sanmak.','Gıda saklama yöntemlerinin ilkelerini değerlendirir.','gıda saklama yöntemleri','beş yöntemden biri hatalı',
 [A('Tabloyu oku','Her yöntemin ilkesini tablodan ve bilgilerden değerlendir.','5 yöntem'),A('Mikroorganizma etkisini düşün','Mikroorganizmaların çoğalması için su, uygun sıcaklık ve uygun ortam gerekir.','su · sıcaklık · ortam'),A('Hatalı ilkeyi bul','Çok düşük sıcaklık mikroorganizmaları genellikle öldürmez, etkinliklerini yavaşlatır ya da durdurur.','dondurma: ilke hatalı')],sekil=SK9,
 metin='Bir aile, kış hazırlığı için yaz boyunca topladığı sebze ve meyveleri farklı yöntemlerle saklamayı planlamıştır. Ailenin araştırdığı yöntemler ile bu yöntemlerin temel ilkeleri tabloda özetlenmiştir. Ancak tabloyu hazırlayan kişi, ilkelerden birini hatalı yazmıştır.\nBuna göre tabloda ilkesi yanlış yazılmış olan yöntem aşağıdakilerden hangisidir?',
 istenen='İlkesi yanlış yazılan yöntemin bulunması.',ip=['Her ilkenin, mikroorganizmanın çoğalma koşullarından hangisini engellediğini düşün.'],
 bilgi=[B('Gıda saklama ilkesi','mikroorganizmaların çoğalmasını engellemek ya da yavaşlatmak gıdanın bozulmasını geciktirir. Örnek: bal, yüksek şeker oranı nedeniyle uzun süre bozulmadan saklanabilir')],
 puf='Gıda saklamanın amacı mikroorganizmaları yok etmek ya da çoğalmasını engellemektir; soğuk onları öldürmez.',**r9)

# ============ 10 · E kodları · orta · öncüllü + tablo ============
d10={'I':(True,'E100–E199 aralığı renklendiricilerdir; E102 ürüne renk vermek için kullanılır.'),
     'II':(True,'E200–E299 aralığı koruyuculardır; E211 bozulmayı geciktirir.'),
     'III':(False,'E330, E300–E399 aralığındaki antioksidan ve asitlik düzenleyiciler grubundadır; kıvam artırıcı değildir.'),
     'IV':(False,'E407, E400–E499 aralığında olup kıvam artırıcı ve emülgatör grubundadır.')}
r10=onc(d10,[('I',),('I','II'),('I','III'),('II','III'),('I','II','IV')])
assert r10['dogru']=='I ve II'
SK10=tablo_svg(['Kod aralığı','Katkı maddesi grubu'],[['E100–E199','Renklendirici'],['E200–E299','Koruyucu'],['E300–E399','Antioksidan ve asitlik düzenleyici'],['E400–E499','Kıvam artırıcı ve emülgatör']])
S('0010','Gıdalar','gida','orta','öncüllü','E kodu, katkı maddesinin grubunu belirtir; kod aralığı maddenin gıdadaki işlevini gösterir.','Kodun aralığını okumadan maddenin işlevini tahmin etmek.','Gıda ambalajındaki E kodlarını işlevleriyle eşleştirir.','E kodu tablosu','dört öncül, iki doğru',
 oncadim(d10,'I ve II'),sekil=SK10,
 metin='Bir meyveli içeceğin ambalajında içindekiler bölümünde şu ifade yazmaktadır: “Su, şeker, meyve suyu konsantresi, E102, E211, E330, E407”. Gıda katkı maddelerinin kod aralıklarına göre grupları tabloda verilmiştir. Bir öğrenci, her kodun ürüne hangi amaçla eklendiğini yorumlamıştır.\nI. E102, ürüne renk vermek için eklenmiştir.\nII. E211, ürünün bozulmasını geciktirmek için eklenmiştir.\nIII. E330, ürünün kıvamını artırmak için eklenmiştir.\nIV. E407, ürünün havayla tepkimeye girerek bozulmasını önlemek için eklenmiştir.\nBuna göre bu yorumlardan hangileri doğrudur?',
 istenen='Doğru yorumların belirlenmesi.',ip=['Her kodun hangi 100’lük aralığa girdiğine bak ve o aralığın grubunu tablodan oku.'],
 bilgi=[B('Katkı maddesi kodları','E harfi, katkı maddesinin Avrupa’da kullanım izni olduğunu; sayı ise maddenin grubunu belirtir. Örnek: E600’lü kodlar çoğunlukla tat ve koku artırıcılardır')],
 puf='Önce kodun yüzler basamağına bak; hangi grubun aralığında olduğu işlevi verir.',**r10)

# ============ 11 · sprey uyarı simgeleri · orta · öncüllü ============
def elmas(cx,cy,h=.5):
    return f'\\draw[thick,rotate around={{45:({cx},{cy})}}] ({cx-h},{cy-h}) rectangle ({cx+h},{cy+h});'
g='\\draw[thick,rounded corners=4pt] (-.5,0) rectangle (.5,2.6); \\draw[thick] (-.24,2.6) rectangle (.24,2.9); \\draw[thick] (-.1,2.9) rectangle (.1,3.1); \\draw[thick] (-.5,.8) -- (.5,.8);'
# alev (yerel koordinat, merkez 2.1,1.5)
g+=elmas(2.1,1.5)+'\\begin{scope}[shift={(2.1,1.45)},scale=.85]\\fill (0,-.32) .. controls (-.38,-.3) and (-.34,.05) .. (-.12,.25) .. controls (-.1,.1) and (-.05,.05) .. (0,0) .. controls (.02,.25) and (.1,.35) .. (.12,.5) .. controls (.4,.25) and (.4,-.3) .. (0,-.32);\\end{scope}'
# gaz tüpü
g+=elmas(3.55,1.5)+'\\fill[rounded corners=3pt] (3.4,1.15) rectangle (3.7,1.8); \\fill (3.48,1.8) rectangle (3.62,1.95);'
# ünlem
g+=elmas(5.0,1.5)+'\\node at (5.0,1.5) {\\huge\\textbf{!}};'
SK11=tk(g)
d11={'I':(True,'alev işareti ürünün yanıcı olduğunu bildirir; ateş kaynaklarından uzak tutulmalıdır.'),
     'II':(False,'basınçlı kap ısınınca patlayabileceğinden güneş alan araçta bırakılmaz.'),
     'III':(False,'basınçlı kap boşalsa da ateşe yaklaştırılmaz; patlama tehlikesi sürer.'),
     'IV':(True,'ünlem işareti ürünün tahriş edici ya da zararlı olabileceğini bildirir; göz ve cilt gibi bölgelerle temasından kaçınılmalıdır.')}
r11=onc(d11,[('I',),('I','II'),('I','IV'),('II','III'),('I','III','IV')])
assert r11['dogru']=='I ve IV'
S('0011','Kozmetik Malzemeler','kozmetik','zor','öncüllü','Kozmetik spreylerin üzerindeki uyarı işaretleri (yanıcı, basınçlı kap, dikkat) güvenli kullanım kuralını gösterir.','Basınçlı kabı boşaldığında tehlikesiz sanmak.','Ambalajdaki uyarı işaretlerine göre güvenli kullanımı değerlendirir.','uyarı işaretleri','dört öncül, üç işaret',
 oncadim(d11,'I ve IV'),sekil=SK11,
 metin='Bir market zincirinde çalışan satış görevlisi, sprey deodorantların ambalajında şekildeki üç uyarı işaretini görmüştür. Görevli, müşterilere ürünün güvenli kullanımını bu işaretlere dayanarak anlatacaktır. Ürünün nasıl saklanıp kullanılması gerektiği konusunda şu ifadeleri hazırlamıştır.\nI. Ürün alev ve kıvılcım gibi ateş kaynaklarından uzak tutulmalıdır.\nII. Ürün, doğrudan güneş alan bir aracın içinde bırakılabilir.\nIII. Boşalan kutu, ateşe atılarak yok edilebilir.\nIV. Ürünün göz ve cilt gibi bölgelerle temas etmemesine dikkat edilmelidir.\nBuna göre bu ifadelerden hangileri doğrudur?',
 istenen='Doğru ifadelerin belirlenmesi.',ip=['Üç işaretin her biri farklı bir tehlikeyi bildirir; ifadelerin hangi tehlikeyle ilgili olduğunu eşle.'],
 bilgi=[B('Güvenlik işaretleri','ambalajlardaki simgeler ürünün taşıdığı tehlikeyi (yanıcı, basınçlı, aşındırıcı vb.) kısaca bildirir. Örnek: kafatası işareti zehirli maddeyi belirtir')],
 puf='Uyarı simgesi tehlike türünü bildirir; kuralı simgeden çıkar.',**r11)

# ============ 12 · ilaç · kolay · öncüllü ============
d12={'I':(True,'antibiyotikler bakterilerin neden olduğu enfeksiyonlarda kullanılan ilaçlardır.'),
     'II':(False,'grip virüslerin neden olduğu bir hastalıktır; antibiyotikler virüslere etkili değildir.'),
     'III':(True,'son kullanma tarihi geçen ilaç etkisini yitirebilir ya da zararlı olabilir; kullanılmamalıdır.')}
r12=onc(d12,[('II',),('III',),('I','II'),('I','III'),('I','II','III')])
assert r12['dogru']=='I ve III'
S('0012','İlaçlar','kozmetik','kolay','öncüllü','Antibiyotikler yalnız bakteriyel enfeksiyonlarda kullanılır; ilaçlar doktor önerisine ve son kullanma tarihine göre kullanılır.','Antibiyotiğin virüslere de etkili olduğunu sanmak.','İlaçların bilinçli kullanımını değerlendirir.','ilaçlar','üç öncül',
 oncadim(d12,'I ve III'),
 metin='Gribe yakalanan Selim, birkaç ay önce bir hastalık için doktorun yazdığı ve evde kalan antibiyotiği içmeyi düşünmektedir. Annesi ilaçların bilinçli kullanılması gerektiğini söyleyerek ona ilaçlarla ilgili bilgi vermiştir. Annesinin açıklamaları şöyledir:\nI. Antibiyotikler, bakterilerin neden olduğu hastalıklarda kullanılır.\nII. Antibiyotikler, gribe neden olan virüslere karşı da etkilidir.\nIII. Son kullanma tarihi geçmiş ilaçlar kullanılmamalıdır.\nBuna göre annesinin açıklamalarından hangileri doğrudur?',
 istenen='Doğru açıklamaların belirlenmesi.',ip=['Her ifadenin hangi hastalık nedeniyle ve hangi kullanım kuralıyla ilgili olduğunu düşün.'],
 bilgi=[B('İlaçların kullanımı','ilaçlar etken madde içerir; yalnız doktor ya da eczacı önerisiyle, belirtilen dozda ve sürede kullanılmalıdır. Örnek: ağrı kesici ilaçlar ağrıyı gidermek için kullanılır')],
 puf='İlaç doktor önerisi, doğru doz ve geçerli son kullanma tarihiyle kullanılır.',**r12)

# ============ 13 · tuz ruhu güvenli kullanım · kolay · hikâyeli · olumsuz kök ============
yan13=[('Ürünün etiketindeki kullanım uyarılarını okur.',True,'etiket okumak güvenli kullanım için gereklidir.'),
 ('Pencereyi açarak ortamın havalanmasını sağlar.',True,'havalandırma, ürünün buharının solunmasını azaltır.'),
 ('Eldiven ve koruyucu gözlük takarak çalışır.',True,'koruyucu ekipman, aşındırıcı çözeltinin cilde ve göze temasını önler.'),
 ('Artan çözeltiyi boş bir meşrubat şişesine koyup mutfak dolabında saklar.',False,'Meşrubat şişesi gibi bir kapta saklanan asit çözeltisi, yanlışlıkla içilebilir; ürün kendi ambalajında saklanmalıdır.'),
 ('Cildine sıçrayan çözeltiyi bol suyla yıkar.',True,'bol suyla yıkamak, asidin cilde etkisini azaltır.')]
r13=kon(tek(yan13,False),'B')
S('0013','Yaygın Günlük Hayat Kimyasalları','temizlik','kolay','hikâyeli','Temizlik kimyasalları kendi ambalajında saklanır; kullanırken etiket okunur, ortam havalandırılır, eldiven ve gözlük takılır.','Artan ürünü başka bir kaba boşaltmanın zararsız olduğunu düşünmek.','Temizlik kimyasallarının güvenli kullanım kurallarını değerlendirir.','tuz ruhu','güvenli kullanım, olumsuz kök',
 [A('Kuralları hatırla','Aşındırıcı temizlik kimyasalları etiket bilgisine ve koruyucu önlemlere uygun kullanılır.','etiket · havalandırma · koruyucu ekipman'),A('Şıkları değerlendir','Üç davranış önlem içerir; cilde sıçrayan ürünün suyla yıkanması da doğrudur.','4 davranış uygun'),A('Hatalı davranışı bul','Ürünü yiyecek ve içecek kabında saklamak, yanlışlıkla içilmesine yol açabilir.','meşrubat şişesi: yanlış')],
 metin='Eda, banyodaki kireç lekelerini temizlemek için içinde hidroklorik asit bulunan bir temizlik ürününü (tuz ruhu) kullanacaktır. Ürünün aşındırıcı bir madde olduğunu bilen Eda, işe başlamadan önce güvenlik önlemlerini düşünmüştür. Temizlik bittikten sonra ürünün bir kısmı artmıştır.\nBuna göre Eda’nın aşağıdaki davranışlarından hangisi güvenlik açısından yanlıştır?',
 istenen='Güvenlik açısından yanlış davranışın bulunması.',ip=['Her davranışın, aşındırıcı bir maddenin yanlışlıkla ya da kazayla zarar vermesini önleyip önlemediğini düşün.'],
 bilgi=[B('Güvenli kullanım','temizlik kimyasalları kendi orijinal ambalajında, çocukların ulaşamayacağı yerde saklanır. Örnek: ilaçlar da çocukların ulaşamayacağı yerde saklanır')],
 puf='Kimyasalı asla yiyecek ve içecek kabına boşaltma; etiketi okuyup önlem al.',**r13)

# ============ 14 · sürdürülebilirlik · orta · öncüllü ============
d14={'I':(True,'atık kâğıdın geri dönüştürülmesi yeni kâğıt için gereken ağaç miktarını azaltır.'),
     'II':(False,'petrol esaslı plastik poşetler toprakta uzun yıllar çözünmeden kalır.'),
     'III':(True,'cam ambalajlar geri dönüştürülerek yeniden cam üretiminde kullanılabilir.'),
     'IV':(True,'sürdürülebilirlik ilkesi, önce atığı azaltmayı, sonra yeniden kullanmayı, en sonda geri dönüştürmeyi önerir.')}
r14=onc(d14,[('I',),('I','II'),('I','III'),('I','III','IV'),('II','III','IV')])
assert r14['dogru']=='I, III ve IV'
S('0014','Geri Dönüşüm','geridon','orta','öncüllü','Geri dönüşüm hammadde tasarrufu sağlar; plastik uzun süre doğada kalır; önce azaltma, sonra yeniden kullanma gelir.','Plastiklerin toprakta kısa sürede çözündüğünü sanmak.','Geri dönüşüm ve sürdürülebilirlik ilkelerini değerlendirir.','sürdürülebilirlik','dört öncül, üç doğru',
 oncadim(d14,'I, III ve IV'),
 metin='Bir belediye, çocukların çevre bilincini artırmak amacıyla ilkokul öğrencilerine atık yönetimi konusunda bir sunum hazırlamıştır. Sunumda geri dönüşüm ve sürdürülebilirlik ile ilgili şu ifadeler yer almaktadır:\nI. Atık kâğıtların geri dönüştürülmesi, kullanılan ağaç miktarını azaltır.\nII. Petrol esaslı plastik poşetler toprakta birkaç hafta içinde tamamen çözünür.\nIII. Cam ambalajlar geri dönüştürülerek yeniden cam üretiminde kullanılabilir.\nIV. Önce atık miktarını azaltmak, sonra ürünleri yeniden kullanmak, en sonda geri dönüştürmek tercih edilir.\nBuna göre bu ifadelerden hangileri doğrudur?',
 istenen='Doğru ifadelerin belirlenmesi.',ip=['Plastik ve cam gibi malzemelerin doğada ne kadar süre kaldığını ve yeniden üretimde kullanılıp kullanılamadığını düşün.'],
 bilgi=[B('Sürdürülebilirlik','kaynaklar gelecek kuşakları da düşünerek kullanılır; atığın azaltılması, yeniden kullanılması ve geri dönüştürülmesi doğal kaynak tüketimini düşürür. Örnek: kullanılmış kumaşlardan temizlik bezi yapmak yeniden kullanma, kumaşı eritip yeni elyaf üretmek geri dönüşümdür')],
 puf='Atığı önce azalt, sonra yeniden kullan, en sonda geri dönüştür.',**r14)

bitir(P,'heryerdeiki',UK)
