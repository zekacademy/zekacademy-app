"""TYT Biyoloji · Canlıların Temel Bileşenleri · 3. paket (bilesenleruc): 10 soru, kardeş yok, ipucu 1.
Enerji hesabı, peptit bağı sayımı, deney/grafik değerleri ve öncül doğrulukları Python'da hesaplanır/assert edilir; şekiller aynı değerlerden çizilir."""
import sys,os,math
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_bio as H
from _hafif_bio3 import *
KONU_='Canlıların Temel Bileşenleri'; UK='bio|Canlıların Temel Bileşenleri'; H.KONU=KONU_
P=Parti('bilesenleruc',KONU_,UK,ders='TYT Biyoloji',idon='tytbio')
KY='ÖSYM 2018–2026 TYT Biyoloji (yalnız mantık) · MEB 9. sınıf Canlıların Temel Bileşenleri'
TIP={'enerji':('by-bu3-enerji','Besin enerjisi hesabı'),'mineral':('by-bu3-mineral','Minerallerin görevleri ve eksikliği'),'test':('by-bu3-test','Besin deneyleri ve ayraçlar'),
     'peptit':('by-bu3-peptit','Peptit bağı ve hidroliz sayımı'),'depo':('by-bu3-depo','Enerji depolarının kullanım sırası'),'su':('by-bu3-su','Suyun kohezyon ve adhezyon özelliği'),
     'enzimgraf':('by-bu3-enzimgraf','Enzimli tepkimede ürün–zaman grafiği'),'enzimdeney':('by-bu3-enzimdeney','Enzim deneyi yorumu')}
def kartla(n,tip,alt,fikir,tuzak,z,kalip,adim):
    kart(f'K-BYBS3-{n}',alt,fikir,tuzak,z,kalip,adim,TIP[tip][0],TIP[tip][1],KY)
def q(no,tip,ad,ne,**k):
    assert len(k['ip'])==1
    mk(P,no,ad=ad,adim=len(ad),tipId=TIP[tip][0],tip=TIP[tip][1],kart=f"K-BYBS3-{no[-2:]} ({TIP[tip][1].lower()}) · {ne}",**k)
AX='tick label style={font=\\footnotesize},label style={font=\\small},axis lines=left,every axis plot/.append style={line width=1.5pt}'

# ============ 0001 · besin etiketi enerji · kolay · hikâyeli ============
kartla('01','enerji','Besin etiketinden enerji hesabı','Karbonhidrat ve proteinin 1 gramı yaklaşık 4 kcal, yağın 1 gramı yaklaşık 9 kcal enerji verir; toplam enerji, her bileşiğin kütlesi birim enerjisiyle çarpılıp toplanarak bulunur.','Yağın birim enerjisini diğerleriyle aynı almak; bir bileşiği toplama katmamak.','kolay','hikâyeli',3)
KH,YG,PR=60,20,10
E1=KH*4+YG*9+PR*4; assert E1==460
q('0001','enerji',[A('Birim enerjileri yaz','Karbonhidrat ve proteinin gramı 4 kcal, yağın gramı 9 kcal verir.','KH, protein: 4 · yağ: 9 kcal/g'),
   A('Her bileşiğin enerjisini bul','Her kütle kendi birim enerjisiyle çarpılır.','60·4 = 240 · 20·9 = 180 · 10·4 = 40'),
   A('Toplamı bul','Üç değer toplanır; su ve mineral enerji vermez.','240 + 180 + 40 = 460 kcal')],
 'bisküvi etiketi, 100 gramdan enerji',z='kolay',alt='Organik Bileşikler',kaz='Besin içeriğindeki organik bileşiklerin kütlesinden toplam enerjiyi hesaplar.',kalip='hikâyeli',
 metin='Bir bisküvi paketinin etiketinde 100 gramında 60 g karbonhidrat, 20 g yağ ve 10 g protein bulunduğu, kalanın su ve mineral olduğu yazmaktadır. Karbonhidrat ve proteinin 1 gramı yaklaşık 4 kcal, yağın 1 gramı yaklaşık 9 kcal enerji vermektedir.\nBuna göre, bu bisküvinin 100 gramı yaklaşık kaç kcal enerji sağlar?',
 dogru=460,yan=[(360,'Yağı da gram başına 4 kcal almış: 90 g × 4 = 360.','islem'),(420,'Proteinin enerjisini toplama katmamış: 240 + 180 = 420.','dikkat'),
                (510,'Proteini yağ gibi 9 kcal almış: 240 + 180 + 90 = 510.','islem'),(90,'Enerji yerine yalnız besin kütlelerini toplamış: 60 + 20 + 10 = 90.','bilgi')],
 istenen='100 gram bisküvinin sağladığı yaklaşık enerji (kcal).',
 ip=['Her organik bileşiğin gram başına verdiği enerjiyi ayrı ayrı düşün.'],
 bilgi=[B('Besinlerin enerji değeri','Karbonhidrat, yağ ve proteinler oksitlendiğinde enerji verir · Su ve mineraller enerji kaynağı değildir')],
 puf='Her bileşiğin kütlesini kendi birim enerjisiyle çarp, sonra topla.')

# ============ 0002 · mineral eksikliği · kolay · olumsuz ============
kartla('02','mineral','Mineral eksikliklerinin sonuçları','Mineraller canlıda yapıya katılır ve düzenleyici görev üstlenir: kalsiyum kemik–dişte, demir hemoglobinde, iyot tiroksinde, magnezyum klorofilde bulunur.','Bir mineralin görevini başka bir mineralle karıştırmak.','kolay','hikâyeli',3)
S2=['Demir eksikliğinde hemoglobin yapımı azalır ve kansızlık görülebilir.','İyot eksikliğinde tiroksin yapımı azalır ve guatr görülebilir.','Kalsiyum eksikliğinde kemik ve dişlerde zayıflama görülebilir.','Magnezyum eksikliğinde bitkilerde klorofil yapımı azalır ve yapraklar sararabilir.','Sodyum eksikliğinde hemoglobin yapımı azalır ve kansızlık görülür.']
q('0002','mineral',[A('Bilgiyi hatırla','Demir hemoglobinin, iyot tiroksinin, magnezyum klorofilin, kalsiyum kemiğin yapısında bulunur.','Fe–Hb · I–tiroksin · Mg–klorofil · Ca–kemik'),
   A('İfadeleri sına','Demir, iyot, kalsiyum ve magnezyum için verilen sonuçlar bu görevlerle uyumludur.','4 ifade doğru'),
   A('Yanlışı seç','Hemoglobin yapımı sodyuma değil demire bağlıdır.','Yanlış: sodyum–hemoglobin')],
 'sağlık broşürü, mineral eksiklikleri',z='kolay',alt='Mineraller',kaz='Minerallerin canlı yapısındaki görevlerini ve eksikliklerinde görülen sonuçları eşleştirir.',kalip='hikâyeli',
 metin='Bir sağlık broşüründe, bazı minerallerin eksikliğinde canlılarda görülebilen durumlar aşağıdaki gibi sıralanmıştır. Broşürü hazırlayan kişi, ifadelerden birini yazarken yanlış bir eşleştirme yapmıştır.\nBuna göre, aşağıdaki ifadelerden hangisi yanlıştır?',
 dogru=S2[4],sira=yer('A',S2[4],S2[:4]),
 yan=[(S2[0],'Hemoglobin demir içerir; ifade doğrudur.','bilgi'),(S2[1],'Tiroksin iyot içerir; eksikliğinde guatr görülebilir; ifade doğrudur.','bilgi'),
      (S2[2],'Kalsiyum kemik ve diş yapısında bulunur; ifade doğrudur.','dikkat'),(S2[3],'Magnezyum klorofilin yapısına katılır; ifade doğrudur.','bilgi')],
 istenen='Yanlış olan ifade.',
 ip=['Her mineralin yapıya katıldığı molekülü düşün.'],
 bilgi=[B('Mineraller','Mineraller enerji vermez; yapıya katılır ve düzenleyici görev yapar · Her mineralin canlıdaki görevi farklıdır')],
 puf='Eksikliği verilen molekülün hangi mineralle ilişkili olduğunu kontrol et.')

# ============ 0003 · besin testi tablosu · orta · öncüllü ============
kartla('03','test','Besin ayraçlarının sonuç tablosu','Her ayraç belirli bir bileşiği gösterir; sonuç yorumlanırken testin kapsamı gözetilir.','Testin kapsamı dışındaki bileşikler için karar vermek.','orta','öncüllü',4)
TST=['Lugol','Biüret','Sudan III','Benedict']
SON={'K':'+−−−','L':'−++−','M':'−−−+','N':'++−+'}
sn=lambda b,t:SON[b][TST.index(t)]=='+'
d3={'I':(True,'N’de Lugol ve biüret testleri olumludur; nişasta ve protein birlikte bulunur.'),
    'II':(True,'K’de Sudan III testi olumsuzdur; K’de yağ bulunmaz.'),
    'III':(False,'L’de Lugol ve Benedict olumsuzdur; bu yalnız nişasta ve basit şeker bulunmadığını gösterir, bu testlerle gösterilemeyen şekerler bulunabilir.')}
assert sn('N','Lugol') and sn('N','Biüret') and not sn('K','Sudan III') and not sn('L','Lugol') and not sn('L','Benedict')
r=onc(d3,True,'B')
q('0003','test',[A('Ayraçların ne gösterdiğini yaz','Lugol nişasta, biüret protein, Sudan III yağ, Benedict basit şeker gösterir.','4 ayraç · 4 madde'),
   adim_onc(d3,'I'),adim_onc(d3,'II'),adim_onc(d3,'III'),sonuc(r,True)],
 'K, L, M, N besinlerinin dört ayraçla testi',z='orta',alt='Besin Deneyleri',kaz='Ayraç sonuçlarından besin içeriği hakkında geçerli çıkarım yapar.',kalip='öncüllü',
 metin='Bir öğrenci, K, L, M ve N besinlerini dört ayraçla test ediyor. Lugol nişastayı, biüret proteini, Sudan III yağı, Benedict ise glikoz gibi basit şekerleri gösterir. Sonuçlar tabloda “+” (olumlu) ve “−” (olumsuz) ile verilmiştir.\nBuna göre,\nI. N besininde nişasta ve protein birlikte bulunur.\nII. K besininde yağ bulunmaz.\nIII. L besininde hiçbir karbonhidrat bulunmaz.\nyargılarından hangileri doğrudur?',
 sekil=tablo_dar(['Besin']+TST,[[b]+[('+' if c=='+' else '−') for c in SON[b]] for b in 'KLMN']),
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',
 ip=['Her yargının hangi ayraç sütununa dayandığına bak.'],
 bilgi=[B('Besin ayraçları','Lugol nişasta ile mavi-mor, biüret protein ile mor, Sudan III yağ ile kırmızımsı renk verir · Benedict ayracı, ısıtmayla basit şekerlerin varlığında renk değiştirir')],
 puf='Olumsuz sonuç, yalnız o testle gösterilen maddenin yokluğunu bildirir.')

# ============ 0004 · polipeptit hidrolizi · orta ============
kartla('04','peptit','Hidrolizde kalan peptit bağı','Amino asitler peptit bağıyla bağlanır; hidrolizde bağlar kopar.','Bağ sayısı ile amino asit sayısını karıştırmak.','kolay','şekilli',4)
NA,KES=14,[3,6,9]
bag=NA-1; kal=bag-len(KES); parca=len(KES)+1
assert (bag,kal,parca)==(13,10,4)
b=[]
for i in range(NA):
    x=.7*i; b.append(f'\\draw[line width=1.2pt] ({x:.2f},0) circle (.27);')
    if i<NA-1: b.append(f'\\draw[line width=1.2pt] ({x+.27:.2f},0)--({x+.43:.2f},0);')
for k,c in zip('XYZ',KES):
    x=.7*(c-1)+.35+0.0; x=.7*(c-1)+.35
    b.append(f'\\draw[{OKU},vurgu,line width=1.4pt] ({x:.2f},1.05)--({x:.2f},.4);\\node[font=\\normalsize\\bfseries,vurgu] at ({x:.2f},1.35) {{{k}}};')
SK4=tk('\n'.join(b),.72)
q('0004','peptit',[A('Başlangıç bağlarını say','14 amino asitli tek zincirde 13 peptit bağı vardır.','14 − 1 = 13 bağ'),
   A('Kesimleri uygula','Üç noktada kesim yapılır; her kesimde bir bağ hidrolizle kopar.','3 bağ kopar · 4 parça'),
   A('Kalan bağları bul','Başlangıçtaki bağlardan kopanlar çıkarılır.','13 − 3 = 10 bağ')],
 'on dört amino asitli zincirin üç noktadan kesilmesi',z='kolay',alt='Proteinler',kaz='Polipeptit hidrolizinde kopan ve kalan peptit bağı sayısını hesaplar.',kalip='şekilli',
 metin='Şekilde, 14 amino asitten oluşan tek zincirli bir polipeptit ve bu zinciri hidrolizle parçalayan bir enzimin etki ettiği X, Y ve Z noktaları gösterilmiştir. Enzim üç noktada da etkisini tamamladığında zincir parçalara ayrılmaktadır.\nBuna göre, oluşan parçalarda toplam kaç peptit bağı kalmıştır?',
 sekil=SK4,dogru=kal,yan=[(13,'Başlangıçtaki bağ sayısını vermiş; kopan bağları çıkarmamıştır.','dikkat'),(11,'Amino asit sayısından kesim sayısını çıkarmış: 14 − 3 = 11; bağ sayısı amino asit sayısından bir eksiktir.','islem'),
                          (4,'Parça sayısını bağ sayısı sanmış.','bilgi'),(3,'Kopan bağ sayısını kalan bağ sanmış.','bilgi')],
 istenen='Parçalarda kalan toplam peptit bağı sayısı.',
 ip=['Amino asitler arasında kaç bağ bulunduğunu düşün.'],
 bilgi=[B('Peptit bağı ve hidroliz','Amino asitler peptit bağıyla bağlanır · Hidrolizde su kullanılarak bağ kopar')],
 puf='Önce toplam bağ sayısını yaz; her kesimde bağ sayısı bir azalır.')

# ============ 0005 · açlık depo grafiği · orta · öncüllü · olumsuz ============
kartla('05','depo','Açlıkta depoların kullanım sırası','Enerji gereksinimi farklı bileşiklerin depolarından karşılanır; azalış hızı ve zamanı bileşiğe göre değişir.','Eğrileri depo türleriyle eşleştirirken azalış zamanını gözden kaçırmak.','orta','öncüllü',4)
def s(t,t0,w): return 1/(1+math.exp(-(t-t0)/w))
KK=lambda t:100*math.exp(-t/.8); LL=lambda t:max(5,100-3.1*t); MM=lambda t:100-.15*t-88*s(t,35,1.4)
assert KK(10)<1 and LL(10)>60 and MM(10)>98 and MM(27)>94 and LL(30)<10
ts=[i/2 for i in range(0,81)]
def cr(f): return ' '.join(f'({t:.1f},{f(t):.1f})' for t in ts)
b=['\\begin{axis}[width=7.8cm,height=5.4cm,xmin=0,xmax=40,ymin=0,ymax=120,xtick={0,10,20,30,40},ytick={0,50,100},xlabel={Açlık süresi (gün)},ylabel={Depo miktarı (\\%)},'+AX+']',
   f'\\addplot[black] coordinates {{{cr(KK)}}};',f'\\addplot[vurgu] coordinates {{{cr(LL)}}};',f'\\addplot[black,densely dashed] coordinates {{{cr(MM)}}};',
   '\\node[font=\\normalsize\\bfseries] at (axis cs:3,48) {K};\\node[font=\\normalsize\\bfseries,vurgu] at (axis cs:14,66) {L};\\node[font=\\normalsize\\bfseries] at (axis cs:15,110) {M};','\\end{axis}']
SK5=tk('\n'.join(b),1.0)
d5={'I':(True,'K eğrisi ilk günlerde hızla sıfıra iner; enerji için ilk kullanılan karbonhidrat depolarıdır.'),
    'II':(False,'10. günde K tükenmiş, M çok az azalmıştır; belirgin azalan L’dir. Enerji için o sırada en çok yağ depoları kullanılır, protein kullanılmaz.'),
    'III':(False,'M eğrisi yaklaşık 30. günden sonra düşmeye başlar; o sırada L eğrisi başlangıç değerinin %10’una yakındır, yağ depoları neredeyse tükenmiştir; “yarısında” demek yanlıştır.')}
r=onc(d5,True,'A')
q('0005','depo',[A('Eğrileri tanı','En önce azalan K karbonhidrat, yavaş ve düzenli azalan L yağ, en son azalan M proteindir.','K: karbonhidrat · L: yağ · M: protein'),
   adim_onc(d5,'I'),adim_onc(d5,'II'),adim_onc(d5,'III'),sonuc(r,True)],
 'uzun açlıkta K, L, M depoları',z='orta',alt='Organik Bileşikler',kaz='Depo grafiğinden enerji kaynaklarının kullanım sırasını yorumlar.',kalip='öncüllü',
 metin='Uzun süre aç kalan bir canlıda karbonhidrat, yağ ve protein depolarının miktarındaki değişim, başlangıç değeri %100 alınarak grafikte K, L ve M eğrileriyle gösterilmiştir. Eğrilerin hangi depoya ait olduğu belirtilmemiştir.\nBuna göre,\nI. K eğrisi karbonhidrat depolarını göstermektedir.\nII. 10. günde enerji için en çok protein depoları kullanılmaktadır.\nIII. M eğrisi düşmeye başladığında yağ depoları hâlâ başlangıç değerinin yaklaşık yarısındadır.\nyargılarından hangileri doğrudur?',
 sekil=SK5,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',
 ip=['Hangi eğrinin ne zaman ve ne hızla azaldığına bakarak enerji kaynağı sırasını belirle.'],
 bilgi=[B('Enerji kaynakları','Hücre enerji gereksinimini karbonhidrat, yağ ve proteinlerden karşılayabilir · Kullanım sırası ve depo miktarları bileşiğe göre farklıdır')],
 puf='Önce eğrilerin düşmeye başlama sırasını yaz, sonra yargıları bu sıraya göre değerlendir.')

# ============ 0006 · kılcal tüp deneyi · orta · olumsuz ============
kartla('06','su','Dar tüpte suyun yükselmesi','Su molekülleri birbirine ve yüzeylere tutunur; dar tüplerde bu etki suyun yükselmesini etkiler.','Yükselmeyi yalnız tek bir çekim türüne bağlamak.','orta','şekilli',4)
DH={1:30,2:15,4:7.5}
assert all(abs(d*h-30)<1e-9 for d,h in DH.items()) and abs(30/4-7.5)<1e-9
b=['\\draw[line width=1.2pt] (-.4,-1.7)--(-.4,-.1)--(-.4,-1.7)--(10.2,-1.7)--(10.2,-.1);','\\draw[densely dashed,line width=.9pt] (-.4,0)--(10.2,0);','\\fill[vurgu,opacity=.18] (-.4,-1.7) rectangle (10.2,0);']
for x,d in zip([1.6,5.0,8.4],[1,2,4]):
    w=.09*d; h=DH[d]/10
    b.append(f'\\fill[vurgu,opacity=.55] ({x-w},-1.2) rectangle ({x+w},{h});')
    b.append(f'\\draw[line width=1.1pt] ({x-w},-1.2)--({x-w},4)\\space ;'.replace('\\space ',''))
    b.append(f'\\draw[line width=1.1pt] ({x+w},-1.2)--({x+w},4);')
    b.append(f'\\draw[{{Stealth[length=2.3mm,width=1.9mm]}}-{{Stealth[length=2.3mm,width=1.9mm]}},line width=.9pt] ({x+w+.5},0)--({x+w+.5},{h});')
    b.append(f'\\node[font=\\small,anchor=west] at ({x+w+.6},{h/2+.0}) {{{str(DH[d]).replace(".0","").replace(".",",")} mm}};')
    b.append(f'\\node[font=\\small] at ({x},-2.1) {{$d={d}$ mm}};')
SK6=tk('\n'.join(b),.9)
S6=['Tüp çapı küçüldükçe sudaki yükselme artmaktadır.','Yükselme ile çap ters orantılıdır; çapı 1 mm ile 4 mm arasında olan bir tüpte yükselme 7,5 mm ile 30 mm arasında olur.','Suyun cam yüzeye tutunması yükselmeye katkı sağlar.','Yükselme yalnız su moleküllerinin birbirini çekmesiyle açıklanır, cam yüzeyin etkisi yoktur.','Benzer bir etki, bitkilerde suyun ince iletim borularında yukarı taşınmasına katkı sağlar.']
q('0006','su',[A('Verileri oku','Çap 1, 2, 4 mm iken yükselme 30, 15, 7,5 mm’dir.','Çap × yükselme = 30'),
   A('İfadeleri sına','Çap küçüldükçe yükselme artar; çarpım sabit olduğundan ara çaplarda yükselme 7,5–30 mm arasındadır; adhezyon ve kohezyon birlikte etkilidir.','4 ifade deneyle ve bilgiyle uyumlu'),
   A('Desteklenmeyeni seç','Cam yüzeyin etkisi olmadığını söyleyen ifade, suyun cama tutunmasıyla çelişir.','Yalnız kohezyon: desteklenmez')],
 'çapları farklı üç cam tüpte su yükselmesi',z='orta',alt='İnorganik Bileşikler',kaz='Dar tüp deneyi verilerinden suyun kohezyon ve adhezyon özelliğini yorumlar.',kalip='şekilli',
 metin='Şekildeki düzenekte, iç çapları 1, 2 ve 4 mm olan üç ince cam tüp aynı kaptaki suya dik biçimde daldırılmıştır. Tüplerde suyun kap seviyesinin üzerine çıktığı yükseklikler şekilde gösterilmiştir; ortam koşulları ve sıcaklık aynıdır.\nBu deneye ve suyun özelliklerine göre aşağıdakilerden hangisi söylenemez?',
 sekil=SK6,dogru=S6[3],sira=yer('B',S6[3],[S6[0],S6[1],S6[2],S6[4]]),
 yan=[(S6[0],'30 mm, 15 mm ve 7,5 mm değerleri çap küçüldükçe yükselmenin arttığını gösterir.','bilgi'),(S6[1],'Çap × yükselme = 30 sabittir; 1 mm ile 4 mm arasındaki çaplarda yükselme 30 mm ile 7,5 mm arasındadır.','islem'),
      (S6[2],'Adhezyon, suyun cam yüzeye tutunmasıdır ve yükselmeye katkı sağlar.','bilgi'),(S6[4],'Kohezyon ve adhezyon, bitkilerde suyun yukarı taşınmasına katkı sağlar.','dikkat')],
 istenen='Deney sonuçlarıyla desteklenmeyen ya da yanlış olan ifade.',
 ip=['Tüp çapı ile yükselme arasındaki ilişkiyi ve suyun hangi yüzeylere tutunabildiğini düşün.'],
 bilgi=[B('Suyun yapışma özellikleri','Su molekülleri hem birbirine hem de başka maddelere tutunabilir · Bu özellik suyun ince borularda hareketini etkiler')],
 puf='Verilerden bir bağıntı çıkar, sonra seçeneklerde bu bağıntıyla çelişeni ara.')

# ============ 0007 · enzim ürün–zaman grafiği · zor · öncüllü ============
kartla('07','enzimgraf','Ürün–zaman grafiğinde enzim miktarı ve sıcaklık','Ürün–zaman grafiğinde eğimin değişimi hızı, eğrinin ulaştığı değer toplam ürünü gösterir.','Eğrilerin hangi özelliğinin neyi gösterdiğini karıştırmak.','zor','öncüllü',5)
KP=lambda t:80*(1-math.exp(-t/5)); LP=lambda t:80*(1-math.exp(-t/2.5)); MP=lambda t:20*(1-math.exp(-t/1.2))
for t in [1,2,3,5,7]: assert abs(LP(t/2)-KP(t))<1e-9
assert abs(KP(20)-80)<2 and abs(MP(20)-20)<.1
hiz=lambda t:16*math.exp(-t/5); assert hiz(4)>hiz(10)
tz=[i/4 for i in range(0,81)]
def cp(f): return ' '.join(f'({t:.2f},{f(t):.1f})' for t in tz)
b=['\\begin{axis}[width=7.8cm,height=5.4cm,xmin=0,xmax=20,ymin=0,ymax=95,xtick={0,2,4,6,8,10,12,14,16,18,20},ytick={0,10,20,30,40,50,60,70,80,90},grid=major,grid style={gray!35},xlabel={Zaman (dakika)},ylabel={Oluşan ürün (birim)},'+AX+']',
   f'\\addplot[black] coordinates {{{cp(KP)}}};',f'\\addplot[vurgu] coordinates {{{cp(LP)}}};',f'\\addplot[black,densely dashed] coordinates {{{cp(MP)}}};',
   '\\node[font=\\normalsize\\bfseries] at (axis cs:12,70) {K};\\node[font=\\normalsize\\bfseries,vurgu] at (axis cs:5.8,86) {L};\\node[font=\\normalsize\\bfseries] at (axis cs:6,28) {M};','\\end{axis}']
SK7=tk('\n'.join(b),1.0)
d7={'I':(True,'40 birim ürüne K tüpünde yaklaşık 3,5 dakikada, L tüpünde yaklaşık 1,7 dakikada ulaşılır; L’de süre yaklaşık yarıdır.'),
    'II':(False,'M tüpünde ürün 20 birimde durmuştur; aynı miktarda substrat bulunan K ve L tüplerinde 80 birime ulaşıldığından substrat bitmemiştir, enzim 65 °C’ta bozulmuştur.'),
    'III':(True,'K eğrisi başlangıçta daha diktir; eğim zamanla azalır. 4. dakikadaki hız 10. dakikadakinden büyüktür.')}
r=onc(d7,True,'E')
q('0007','enzimgraf',[A('Tüpleri karşılaştır','K ile L yalnız enzim miktarında, K ile M yalnız sıcaklıkta farklıdır.','L: 2 kat enzim · M: 65 °C'),
   adim_onc(d7,'I'),adim_onc(d7,'II'),adim_onc(d7,'III'),sonuc(r,True)],
 'üç tüpte ürün–zaman grafiği',z='zor',alt='Enzimler',kaz='Ürün–zaman grafiğinden enzim miktarı ve sıcaklığın tepkimeye etkisini yorumlar.',kalip='öncüllü',
 metin='Eşit miktarda substrat içeren üç özdeş tüpten K ve L’ye sırasıyla 1 ve 2 birim enzim konup 37 °C’ta, M’ye 1 birim aynı enzim konup 65 °C’ta tutuluyor. Ürün miktarının zamanla değişimi grafikte verilmiştir.\nBuna göre,\nI. L tüpünde 40 birim ürüne ulaşma süresi, K tüpündekinin yaklaşık yarısıdır.\nII. M tüpünde ürün artışının durması, substratın tükenmesinden kaynaklanmıştır.\nIII. K tüpünde tepkime hızı 4. dakikada, 10. dakikadakinden büyüktür.\nyargılarından hangileri doğrudur?',
 sekil=SK7,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',
 ip=['Eğrilerin ulaştığı en yüksek değerleri, eğimlerini ve tüpler arasındaki tek farkı karşılaştır.'],
 bilgi=[B('Enzimlerin etkisi','Enzimler tepkimeyi hızlandırır ve harcanmaz · Sıcaklık yükselince yapıları bozulabilir')],
 puf='Önce tüpler arasındaki farkı belirle, sonra her yargıyı eğrilerin hangi özelliğiyle ilgili olduğuna bağla.')

# ============ 0008 · amilaz tüp deneyi · zor · olumsuz ============
kartla('08','enzimdeney','Tükürük–nişasta deney tüpleri','Kontrollü deneyde tek bir etken değiştirilerek tüpler karşılaştırılır.','Kontrol grubunu yanlış belirlemek; veride olmayan sonuç çıkarmak.','zor','tablo',5)
TUP=[('1','N + T','37 °C','Sarı-kahve'),('2','N + kaynamış T','37 °C','Mavi-mor'),('3','N + T','0 °C','Mavi-mor'),('4','N + T + HCl','37 °C','Mavi-mor'),('5','N + su','37 °C','Mavi-mor')]
S8=['1 ve 5 numaralı tüplerin karşılaştırılması, tükürükte nişastayı parçalayan bir madde bulunduğunu gösterir.','1 ve 2 numaralı tüplerin karşılaştırılması, nişastayı parçalayan maddenin kaynatılınca etkinliğini yitirdiğini gösterir.','3 numaralı tüpte, düşük sıcaklık nedeniyle tükürükteki maddenin yapısı kalıcı olarak bozulmuştur.','1 ve 4 numaralı tüplerin karşılaştırılması, asidik ortamın nişasta parçalanmasını engellediğini gösterir.','2 numaralı tüpte nişasta parçalanmamıştır.']
q('0008','enzimdeney',[A('Kontrol ve deneyi ayır','5 numaralı tüp tükürüksüz kontrol, 1 numaralı tüp koşulları uygun deney tüpüdür.','Tek farklı etken: tükürük'),
   A('Tüpleri ikişer ikişer karşılaştır','1–5: tükürük; 1–2: kaynatma; 1–4: asit; 1–3: soğuk karşılaştırılır.','Her karşılaştırmada tek etken farklı'),
   A('Sonucu doğrula','Soğukta nişasta parçalanmamıştır ancak bu, enzimin bozulduğu değil yavaşladığı ya da durduğu anlamına gelir; kalıcı bozulma deneyle gösterilmemiştir.','Desteklenmeyen: 3. tüp')],
 'amilaz deneyi, Lugol sonuçları',z='zor',alt='Enzimler',kaz='Kontrollü enzim deneyinde tüpleri karşılaştırarak geçerli ve geçersiz çıkarımları ayırır.',kalip='tablo',
 metin='Bir öğrenci, beş tüpte nişasta çözeltisine (N) tükürük (T) ve başka maddeler ekleyip koşulları değiştiriyor. 30 dakika sonra her tüpe Lugol damlatıyor; mavi-mor renk nişastanın hâlâ bulunduğunu gösteriyor. Tüplerin içeriği ve sonuçlar tabloda verilmiştir.\nBu deneye göre aşağıdakilerden hangisi söylenemez?',
 sekil=tablo_dar(['Tüp','İçerik','Ortam','Lugol sonucu'],[list(t) for t in TUP]),
 dogru=S8[2],sira=yer('C',S8[2],[S8[0],S8[1],S8[3],S8[4]]),
 yan=[(S8[0],'Yalnız 1. tüpte nişasta kalmamıştır; 5. tüpte tükürük yoktur ve nişasta duruyor; ifade doğrudur.','bilgi'),(S8[1],'Kaynatılmış tükürüklü 2. tüpte nişasta kalmıştır; ifade doğrudur.','dikkat'),
      (S8[3],'HCl eklenen 4. tüpte nişasta kalmıştır; ifade doğrudur.','bilgi'),(S8[4],'Mavi-mor renk nişastanın durduğunu gösterir; ifade doğrudur.','bilgi')],
 istenen='Deney verileriyle desteklenmeyen ifade.',
 ip=['Her karşılaştırmada hangi etkenin tek başına değiştiğine bak ve sonucun neyi gösterip neyi göstermediğini ayır.'],
 bilgi=[B('Kontrollü deney','Bir deneyde yalnız bir etken değiştirilir, diğerleri sabit tutulur · Enzim etkinliği sıcaklık ve pH gibi koşullardan etkilenir')],
 puf='Sonucu doğrudan veriden okunanlarla ve yorumla eklenenlerle ayır.')

# ============ 0009 · enzim özgüllüğü tablosu · zor ============
kartla('09','enzimdeney','Enzim özgüllüğünden molekül sayısı','Her enzim yalnız belirli bir substrata etki eder; deney tablosundan hangi enzimin hangi disakkariti parçaladığı çıkarılır, parçalanan her disakkarit iki monosakkarit verir.','Her enzimin her disakkariti parçaladığını sanmak; parçalanmayan molekülleri sayıma katmamak.','zor','tablo',5)
OZ=[('1','K','E1','Monosakkarit oluştu'),('2','K','E2','Değişim yok'),('3','L','E2','Monosakkarit oluştu'),('4','L','E3','Değişim yok'),('5','M','E3','Monosakkarit oluştu'),('6','M','E1','Değişim yok')]
EN={'E1':'K','E2':'L','E3':'M'}
for t,sub,en,so in OZ: assert (so!='Değişim yok')==(EN[en]==sub)
n={'K':30,'L':20,'M':10}; son=0
for sub,c in n.items():
    son+= 2*c if sub in ('K','M') else c
assert son==100 and 2*sum(n.values())==120 and 2*30+20+10==90 and 2*(30+10)==80
q('0009','enzimdeney',[A('Özgüllüğü çıkar','Parçalanma gözlenen tüpler: K–E1, L–E2, M–E3.','E1: K · E2: L · E3: M'),
   A('Kullanılan enzimleri uygula','Yalnız E1 ve E3 vardır; K ve M parçalanır, L aynı kalır.','K: 30 → 60 · M: 10 → 20 · L: 20'),
   A('Toplam karbonhidrat molekülünü bul','Parçalanan her disakkarit iki monosakkarit verir; L molekülleri disakkarit olarak kalır.','60 + 20 + 20 = 100')],
 'üç enzimin üç disakkaritteki etkisi',z='zor',alt='Enzimler',kaz='Deney tablosundan enzim özgüllüğünü çıkarıp ürün molekülü sayısını hesaplar.',kalip='tablo',
 metin='K, L ve M disakkaritleri ile E1, E2 ve E3 enzimleriyle yapılan deneylerin sonuçları tabloda verilmiştir. Her enzim, tablodaki substratlardan en çok birini parçalamaktadır. Ortamda 30 K, 20 L ve 10 M molekülü bulunmakta ve yalnızca E1 ile E3 eklenmektedir.\nBuna göre, tepkimeler bittiğinde ortamdaki toplam karbonhidrat (di- ve monosakkarit) molekülü sayısı kaçtır?',
 sekil=tablo_dar(['Tüp','Substrat','Enzim','Sonuç'],[list(t) for t in OZ]),
 dogru=100,yan=[(120,'Üç disakkaritin de parçalandığını sanmış: 60 × 2 = 120.','dikkat'),(90,'Yalnız K’nin parçalandığını hesaplamış: 60 + 20 + 10 = 90; M’yi atlamıştır.','islem'),
                (80,'Yalnız oluşan monosakkaritleri saymış: 60 + 20 = 80; L moleküllerini katmamıştır.','islem'),(60,'Tepkimeyle molekül sayısının değiştiğini görmeyip başlangıç sayısını vermiştir.','bilgi')],
 istenen='Tepkimeler bittiğinde ortamdaki toplam karbonhidrat molekülü sayısı.',
 ip=['Tablodan hangi enzimin hangi molekülü parçaladığını bul, sonra yalnız eklenen enzimlerin etkisini hesapla.'],
 bilgi=[B('Enzim özgüllüğü','Her enzim yalnız belirli bir substrata bağlanır · Disakkarit hidrolizle iki monosakkarite ayrılır')],
 puf='Önce enzim–substrat eşleşmelerini yaz, sonra yalnız eşleşen moleküllerin sayısını değiştir.')

# ============ 0010 · mineral saksı deneyi · zor · öncüllü ============
kartla('10','mineral','Mineral eksikliği saksı deneyi','Deneyde bir etken değiştirilerek sonuçlar karşılaştırılır; ölçülen özellik bağımlı değişkendir.','Gruplar arasındaki farkı yanlış etkene bağlamak.','orta','öncüllü',5)
SK10=[('1','Tam besin',22,'g'),('2','Mg yok',15,'y'),('3','N yok',6,'p')]
b=[]
for i,(no,ad,h,c) in enumerate(SK10):
    x=2.8*i; hh=h/6
    fill={'g':'green!60!black','y':'yellow!85!orange','p':'yellow!60!lime'}[c]
    b.append(f'\\draw[line width=1.1pt] ({x-.6},0)--({x-.45},-.9)--({x+.45},-.9)--({x+.6},0)--cycle;')
    b.append(f'\\draw[line width=1.4pt] ({x},0)--({x},{hh});')
    for k,(dx,dy) in enumerate([(-.45,.45),(.45,.62),(-.4,.9),(.4,.95)]):
        yy=hh*dy; 
        if hh<1.2 and k>1: continue
        b.append(f'\\filldraw[{fill},draw=black,line width=.7pt] ({x+dx},{yy}) ellipse (.36 and .17);')
    b.append(f'\\node[font=\\small] at ({x},-1.3) {{{no}. {ad}}};\\node[font=\\small] at ({x},-1.75) {{Boy: {h} cm}};')
    b.append(f'\\node[font=\\small] at ({x},-2.2) {{Yaprak: '+{'g':'yeşil','y':'sarı','p':'soluk sarı'}[c]+'};')
SK10F=tk('\n'.join(b),.82)
d10={'I':(False,'Kontrol grubu, yalnız ölçülen etkenin uygulanmadığı tam besinli 1 numaralı saksıdır; 2 numaralı saksı deney grubudur.'),
     'II':(True,'Mg eksikliğinde boy 22’den 15 cm’ye, N eksikliğinde 6 cm’ye iner; Mg eksikliğinin etkisi daha azdır.'),
     'III':(True,'Azot, amino asit ve protein yapımında gerekli bir elementtir; 3. saksıdaki cüceliğin nedeni bu şekilde açıklanabilir.')}
assert 22-15<22-6
r=onc(d10,True,'E')
q('0010','mineral',[A('Deney düzenini çöz','1. saksı tam besinli, 2. saksı Mg’siz, 3. saksı N’suz çözeltiyle sulanmıştır; ölçülen boy ve yaprak rengidir.','Kontrol: 1 · Bağımsız: mineral · Bağımlı: boy, renk'),
   adim_onc(d10,'I'),adim_onc(d10,'II'),adim_onc(d10,'III'),sonuc(r,True)],
 'tam, Mg’siz ve N’suz çözeltili üç fide',z='orta',alt='Mineraller',kaz='Mineral eksikliği deneyinde kontrol grubunu belirler ve sonuçtan geçerli çıkarım yapar.',kalip='öncüllü',
 metin='Aynı türden ve yaşta üç fide, aynı ışık ve sıcaklıkta eşit miktarda çözeltiyle sulanıyor: 1. saksıda tüm mineralleri içeren, 2. saksıda yalnız magnezyum içermeyen, 3. saksıda yalnız azot içermeyen çözelti. Üç hafta sonraki sonuçlar şekildedir.\nBuna göre,\nI. 2 numaralı saksı kontrol grubudur.\nII. Magnezyum eksikliğinin boy uzamasına etkisi, azot eksikliğinden daha azdır.\nIII. 3 numaralı saksıdaki gelişme geriliği, azotun protein yapımında gerekli olmasıyla açıklanabilir.\nyargılarından hangileri doğrudur?',
 sekil=SK10F,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',
 ip=['Hangi saksıda hangi etkenin eksik olduğuna ve boydaki kayba bak; kontrol grubunun tanımını düşün.'],
 bilgi=[B('Bitkilerde mineraller','Mineraller bitkilerin organik moleküllerinin yapısına katılır · Eksiklikleri büyüme ve yaprak renginde değişim yapabilir')],
 puf='Önce hangi etkenin tek başına değiştiğini belirle; kontrol, hiçbir eksikliği olmayan gruptur.')

bitir(P,'bilesenleruc',UK)
