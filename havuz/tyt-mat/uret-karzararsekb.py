"""Kâr Zarar Problemleri · ŞEKİLLİ ek paket b (10 soru: 2 kolay / 4 orta / 4 zor): şekil/tablo çözüm verisini taşır; her doğru ve çeldirici değer assert'lidir. Kardeş yok, ipucu 1."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
H.KONU='Kâr Zarar Problemleri'
UK='prob|Kar Zarar Problemleri'
P=Parti('karzararsekb','Kâr Zarar Problemleri',UK)
KY='ÖSYM 2018–2026 TYT Matematik (şekilli/tablolu kâr-zarar soruları; yalnız mantık) · MEB 8–9. sınıf'
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)
def fig(body): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'+body.replace('%','\\%')+'\n\\end{tikzpicture}')
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)

KAR=B('Kâr ve zarar','kâr = satış fiyatı − alış fiyatı; kâr yüzdesi alış fiyatına göre hesaplanır: kâr yüzdesi = kâr ÷ alış × 100. Örnek: alış 80 TL, satış 100 TL ise kâr 20 TL, kâr yüzdesi %25')
ORN=B('Dilim ve oran','bir bütünün parçaları yüzdelerle verildiğinde, bilinen bir parçanın değerinden bütün ve diğer parçalar bulunur. Örnek: %20’si 50 olan bütün 250’dir')
KUT=B('Kutu modeli','eş kutular aynı değeri gösterir; toplam, eş kutuların toplamıdır. Örnek: alış 4 kutu, kâr 1 kutuysa satış fiyatı 5 kutudur')
YUZ=B('Yüzdeyle artış','alışa kâr yüzdesi eklenirken alış × (100 + kâr yüzdesi) ÷ 100, zararda alış × (100 − zarar yüzdesi) ÷ 100 hesaplanır. Örnek: alış 200 TL, %30 kârla satış 260 TL')
GRF=B('Gelir ve gider doğruları','gelir doğrusu ile gider doğrusunun farkı kârı verir; gider doğrusunun başlangıç değeri sabit giderdir. Örnek: adet başına 50 TL gelir, adet başına 30 TL gider ve 100 TL sabit gider varsa 10 adette kâr 10 × 50 − (100 + 10 × 30) = 100 TL’dir')
ZNC=B('Zincirleme kâr','her halka bir öncekinin satış fiyatını alış fiyatı sayar ve kendi kâr yüzdesini ekler; çarpanlar art arda çarpılır. Örnek: %10 ve %20 kârda çarpan 1,1 × 1,2 = 1,32 olur')

kartla('K-KZC-01','Kutu modelli kâr','Alış fiyatı eş kutularla gösterilir; kâr kutusundan kutu değeri, oradan satış fiyatı bulunur.','Kâr tutarını alış fiyatı sanmak; kutu sayısını yanlış saymak.','kolay','hikâyeli',3,'kzc-model','Kutu modeli ve oran')
kartla('K-KZC-02','Daire grafiği ve maliyet','Dilim yüzdelerinden bütün ve istenen dilim değeri bulunur.','Kâr dilimini toplam gelir sanmak; dilimleri toplamamak.','kolay','grafik',3,'kzc-dilim','Daire grafiği ve oran')
kartla('K-KZC-03','Sayı doğrusunda fiyatlar','Alış, satış ve etiket fiyatı arasındaki uzaklıklardan denklem kurulup fiyatlar bulunur.','Kâr yüzdesini satış fiyatına göre hesaplamak.','orta','yeni nesil',4,'kzc-dogru','Sayı doğrusunda fiyatlar')
kartla('K-KZC-04','Eş satış fiyatlı iki ürün','Eş satış fiyatında kâr ve zarar yüzdesi aynı olsa da alışlar farklıdır; ayrı ayrı alış bulunur.','Kâr ile zararı %20 diye birbirini götürüyor sanmak.','orta','yeni nesil',4,'kzc-karsilastir','İki ürünün karşılaştırması')
kartla('K-KZC-05','Maliyet tablosu','Gider kalemleri toplanıp ürün sayısına bölünür, sonra kâr yüzdesi eklenir.','Kâr yüzdesini satış fiyatına göre uygulamak; yanlış ürün sayısına bölmek.','orta','tablo',4,'kzc-maliyet','Maliyet tablosu')
kartla('K-KZC-06','Çay karışımı','Karışımın toplam alışı ve kilogramı bulunur; birim maliyetten kâr yüzdesi hesaplanır.','Fiyatların aritmetik ortalamasını almak.','orta','hikâyeli',4,'kzc-karisim','Karışım ve kâr')
kartla('K-KZC-07','Gelir–gider doğruları','İki doğrudan birim fiyat, değişken gider ve sabit gider okunur; verilen adetteki kâr hesaplanır.','Sabit gideri atlamak; değişken gideri hesaba katmamak.','zor','grafik',5,'kzc-basabas','Gelir–gider grafiği')
kartla('K-KZC-08','Daire grafiği ve fire','Dilimlerden her grubun kilogramı ve geliri bulunur; çürük için gelir yoktur, toplam kâr alışa oranlanır.','Çürük miktarı atlamak; fiyatları ortalamak.','zor','hikâyeli',5,'kzc-dilim','Daire grafiği ve oran')
kartla('K-KZC-09','Oranlı alış ve karşıt sonuç','Toplam alış orana göre iki mala bölünür; birinde kâr, diğerinde zarar hesaplanıp net sonuç bulunur.','Kâr ve zararı eşit pay saymak; orana göre bölmemek.','orta','hikâyeli',5,'kzc-model','Kutu modeli ve oran')
kartla('K-KZC-10','Zincirleme kâr','Ürün zincirde ilerlerken her halkanın kâr çarpanı bulunur; son fiyattan geriye doğru işlenir.','Kâr yüzdelerini toplayıp tek çarpan yapmak.','zor','hikâyeli',5,'kzc-zincir','Zincirleme kâr')

# 01 kolay · kutu modeli
ku=45; alis=4*ku; satis=alis+ku; assert (alis,satis)==(180,225)
e=[45,180,270,360]; assert len({satis,*e})==5 and 6*ku==270 and 8*ku==360
o=[]
for j in range(4): o.append(f'\\filldraw[fill=vurgu!25,draw=vurgu!80!black] ({j*1.1:.1f},0) rectangle ({(j+1)*1.1:.1f},0.8);')
o.append('\\filldraw[fill=white,draw=vurgu!80!black] (4.4,0) rectangle (5.5,0.8); \\node at (4.95,0.4) {45 TL};')
o.append('\\draw[<->] (0,1.2) -- (4.4,1.2); \\node[above=1pt] at (2.2,1.2) {alış fiyatı}; \\draw[<->] (4.4,1.2) -- (5.5,1.2); \\node[above=1pt] at (4.95,1.2) {kâr};')
o.append('\\draw[<->] (0,-0.4) -- (5.5,-0.4); \\node[below=1pt] at (2.75,-0.4) {satış fiyatı = ?};')
SK=fig('\n'.join(o))
q('0001',tipId='kzc-model',tip='Kutu modeli ve oran',z='kolay',alt='Kutu Modelli Kâr',kaz='Kutu modelinden kâr tutarına göre alış ve satış fiyatını bulur.',kalip='hikâyeli',
 kart='K-KZC-01 · alış = 4 kutu, kâr = 1 kutu = 45 TL; satış 225 TL',
 metin='Bir kırtasiyeci, aldığı bir defter setini hiçbir indirim yapmadan satmıştır. Şekilde setin alış fiyatı birbirine eş 4 kutuyla, bu satıştan elde ettiği kâr ise aynı büyüklükteki bir kutuyla gösterilmiştir. Kâr olan kutunun üzerinde yazan değer, kırtasiyecinin bu satıştan elde ettiği kârdır.\nBuna göre, defter seti kaç TL’ye satılmıştır?',
 dogru=satis,yan=[(45,'Kâr tutarını satış fiyatı sanmış.','dikkat'),(180,'Alış fiyatını satış fiyatı sanmış.','dikkat'),(270,'Kâr için iki kutu hesaplayıp 6 kutu almış.','dikkat'),(360,'Kâr kutusunu da 4 kutu sayıp 8 kutu almış.','dikkat')],
 istenen='Defter setinin satış fiyatı.',ip=['Kâr kutusu bir eş kutuya karşılık gelir; alış fiyatı kaç kutudur?'],bilgi=[KAR,KUT],sekil=SK,
 ad=[A('Kutu değeri','Kâr tek eş kutudur.','1 kutu = 45 TL'),A('Alış fiyatı','Alış 4 kutudur.','4 × 45 = 180 TL'),A('Satış fiyatı','Satış = alış + kâr.','180 + 45 = 225 TL')],
 puf='Satış fiyatı 5 kutudur.')

# 02 kolay · daire grafiği
kar=450; yk=15; top_=kar*100//yk; am=top_*65//100
assert top_==3000 and am==1950 and 65+20+15==100
e=[1350,2400,2550,3000]; assert len({am,*e})==5 and 2400==top_*80//100 and 2550==top_-kar and 1350==top_*45//100
import math
def dilim(a0,a1,fill): return f'\\fill[{fill},draw=white] (0,0) -- ({a0}:1.5) arc ({a0}:{a1}:1.5) -- cycle;'
o=[dilim(0,234,'vurgu!25'),dilim(234,306,'vurgu!10'),dilim(306,360,'vurgu!55')]
o.append('\\node[above] at (0,1.55) {alış maliyeti: %65}; \\node[below] at (270:1.5) {kira ve personel: %20}; \\node[right] at (1.55,-0.55) {kâr: %15};')
SK=fig('\n'.join(o))
q('0002',tipId='kzc-dilim',tip='Daire grafiği ve oran',z='kolay',alt='Daire Grafiği ve Maliyet',kaz='Daire grafiğindeki dilim yüzdelerinden bilinen bir dilimle istenen dilimin değerini bulur.',kalip='grafik',
 kart='K-KZC-02 · kâr %15 = 450 TL; alış maliyeti %65 = 1950 TL',
 metin='Bir pastanenin bir aydaki satış gelirinin dağılımı, aşağıdaki daire grafiğinde yüzdelerle gösterilmiştir. Pastane bu ay yalnızca grafikteki üç kalemi hesaplamış ve geliri tamamen bu kalemlere ayırmıştır. Kâr, gelirden alış maliyeti ile kira ve personel giderleri çıkarıldıktan sonra kalan tutardır; bu ayki kâr 450 TL olmuştur ve pastane başka bir gelir ya da gider kalemi hesaplamamıştır.\nBuna göre, pastanenin bu ayki alış maliyeti kaç TL’dir?',
 dogru=am,yan=[(1350,'%65 − %20 = %45’i hesaplamış: 3000 × 0,45.','dikkat'),(2400,'Alış maliyeti ile kira ve personel giderini toplamış (%80).','dikkat'),(2550,'Toplam gelirden yalnız kârı çıkarmış: 3000 − 450.','dikkat'),(3000,'Toplam geliri alış maliyeti sanmış.','dikkat')],
 istenen='Pastanenin alış maliyeti.',ip=['%15’lik kâr 450 TL ise %1’lik dilimin değeri kaç TL olur?'],bilgi=[ORN],sekil=SK,
 ad=[A('%1’in değeri','Kâr dilimi %15.','450 ÷ 15 = 30 TL'),A('Toplam gelir','%100.','30 × 100 = 3000 TL'),A('Alış maliyeti','%65’i hesaplanır.','30 × 65 = 1950 TL')],
 puf='%1’i bul, sonra %65 ile çarp.')

# 03 orta · sayı doğrusu
ab=400; sat=460; et=500
assert sat-ab==60 and et-sat==40 and et==ab*125//100
v=60*100//ab; assert v==15
e=[8,12,25,40]; assert len({v,*e})==5 and 40*100//et==8 and 60*100//et==12 and (et-ab)*100//ab==25 and et-sat==40
o=['\\draw[-{Stealth}] (-0.3,0) -- (5.8,0);',
 '\\foreach \\px/\\nm in {0.5/Alış,3.5/Satış,5.5/Etiket}{\\draw[thick] (\\px,-0.12) -- (\\px,0.12); \\node[below=3pt] at (\\px,-0.1) {\\nm};}',
 '\\draw[<->] (0.5,0.7) -- (3.5,0.7); \\node[above=1pt] at (2.0,0.7) {60 TL}; \\draw[<->] (3.5,0.7) -- (5.5,0.7); \\node[above=1pt] at (4.5,0.7) {40 TL};']
SK=fig('\n'.join(o))
q('0003',tipId='kzc-dogru',tip='Sayı doğrusunda fiyatlar',z='orta',alt='Sayı Doğrusunda Fiyatlar',kaz='Alış, satış ve etiket fiyatı arasındaki farklardan fiyatları bulup kâr yüzdesini hesaplar.',kalip='yeni nesil',
 kart='K-KZC-03 · alış 400, satış 460, etiket 500; kâr %15',
 metin='Bir ürünün alış fiyatı, satış fiyatı ve etiket fiyatı sayı doğrusu üzerinde gösterilmiştir; uzaklıklar TL cinsindendir. Ürünün etiket fiyatı, alış fiyatının %125’idir ve satış yapılırken etiket fiyatından yalnızca bir miktar indirim uygulanmıştır.\nBuna göre, ürün satış fiyatından satıldığında kâr yüzdesi kaçtır?',
 dogru=v,yan=[(8,'İndirim yüzdesini (40 ÷ 500) kâr yüzdesi sanmış.','dikkat'),(12,'60 TL’lik kârı etiket fiyatına oranlamış.','dikkat'),(25,'Etiket fiyatının alıştan yüzde artışını kâr yüzdesi sanmış.','dikkat'),(40,'İndirim tutarını kâr yüzdesi sanmış.','dikkat')],
 istenen='Kâr yüzdesi.',ip=['Şekildeki iki uzaklığı birlikte düşün; etiket fiyatı alışın %125’i olduğuna göre bu uzaklıklar alışın kaçta kaçıdır?'],bilgi=[KAR,YUZ],sekil=SK,
 ad=[A('Etiket ile alış','60 + 40 = 100 TL fark; etiket alışın %125’i.','%25 alış = 100 TL'),A('Alış','%25 alışa eşit.','alış = 400 TL'),A('Satış','Alış + 60.','400 + 60 = 460 TL'),A('Kâr yüzdesi','Alışa göre.','60 ÷ 400 = %15')],
 puf='Önce alış fiyatını bul.')

# 04 orta · iki ürün
sf=240; ka=sf*100//120; za=sf*100//80
assert ka==200 and za==300; v=(za-sf)-(sf-ka); assert v==20
e=[0,40,60,100]; assert len({v,*e})==5 and sf-ka==40 and za-sf==60 and ka+za-2*sf==20
b1=lambda y,t,r: f'\\filldraw[fill=vurgu!25,draw=vurgu!80!black] (0,{y}) rectangle (4.8,{y+0.8}); \\node at (2.4,{y+0.4}) {{{t}}}; \\node[right] at (4.95,{y+0.4}) {{{r}}};'
o=[b1(1.1,'K: satış 240 TL','%20 kâr'),b1(0,'L: satış 240 TL','%20 zarar')]
SK=fig('\n'.join(o))
q('0004',tipId='kzc-karsilastir',tip='İki ürünün karşılaştırması',z='orta',alt='Eş Satış Fiyatlı İki Ürün',kaz='Aynı satış fiyatlı iki üründe kâr ve zarar yüzdesinden alışları bulup net sonucu hesaplar.',kalip='yeni nesil',
 kart='K-KZC-04 · K alış 200, L alış 300; net zarar 20 TL',
 metin='Bir antikacı, K ve L eşyalarını şekildeki satış fiyatlarından satmıştır. Şekildeki yüzdeler, her eşyadan alış fiyatına göre elde edilen kâr ya da zararı göstermektedir. Antikacı bu eşyalar dışında başka bir satış yapmamış ve satışlar dışında hiçbir gelir ya da gider hesaba katılmamıştır.\nBuna göre, antikacı bu iki satıştan toplam kaç TL zarar etmiştir?',
 dogru=v,yan=[(0,'Kâr ile zararı eşit yüzde olduğu için birbirini götürüyor sanmış.','dikkat'),(40,'Yalnız K eşyasındaki kârı (40 TL) bulup net sonuç sanmış.','dikkat'),(60,'Yalnız L eşyasındaki zararı net zarar sanmış.','dikkat'),(100,'Kâr ile zararı toplayıp 40 + 60 almış.','dikkat')],
 istenen='Toplam zarar tutarı.',ip=['Kâr yüzdesi ve zarar yüzdesi alış fiyatına göre hesaplanır; her eşyanın alış fiyatını ayrı bul.'],bilgi=[KAR,YUZ],sekil=SK,
 ad=[A('K’nın alışı','%20 kârla 240.','alış × 1,2 = 240, alış = 200'),A('L’nin alışı','%20 zararla 240.','alış × 0,8 = 240, alış = 300'),A('Sonuçlar','K’de 40 TL kâr, L’de 60 TL zarar.','+40 ve −60'),A('Net sonuç','Zarar kârdan büyük.','60 − 40 = 20 TL zarar')],
 puf='Alış fiyatları farklı olduğu için yüzdeler götürmez.')

# 05 orta · maliyet tablosu
gid=[('Hammadde',4200),('İşçilik',3000),('Kira',1800),('Ambalaj',600)]; tg=sum(x for _,x in gid); n=80
bm=Fr(tg,n); v=bm*Fr(125,100); assert tg==9600 and bm==120 and v==150
e=[90,120,145,160]; assert len({v,*e})==5 and Fr(4200+3000,80)==90 and bm+25==145 and bm*100/75==160
SK=tablo_svg(['Gider kalemi','Tutar (TL)'],[[a,str(b)] for a,b in gid])
q('0005',tipId='kzc-maliyet',tip='Maliyet tablosu',z='orta',alt='Maliyet Tablosu',kaz='Gider tablosundan birim maliyeti bulup istenen kâr yüzdesiyle satış fiyatını hesaplar.',kalip='tablo',
 kart='K-KZC-05 · 9600 TL ÷ 80 = 120 TL; %25 kârla 150 TL',
 metin='Bir atölye, 80 adet el dokuması çanta üretmiş ve üretimin toplam giderlerini aşağıdaki tabloda göstermiştir. Atölye her çantayı aynı fiyattan ve alış maliyeti üzerinden %25 kârla satmak istemektedir; tablodaki giderlerin toplamı alış maliyeti sayılacaktır; başka gider yoktur ve üretilen çantaların hepsi satılacaktır.\nBuna göre, bir çanta kaç TL’ye satılmalıdır?',
 dogru=int(v),yan=[(90,'Kira ve ambalajı hesaba katmamış: 7200 ÷ 80.','dikkat'),(120,'Birim maliyeti satış fiyatı sanmış, kârı eklememiş.','dikkat'),(145,'%25’i 25 TL sanıp birim maliyete eklemiş.','dikkat'),(160,'Kârı satış fiyatına göre alıp 120 ÷ 0,75 yapmış.','dikkat')],
 istenen='Bir çantanın satış fiyatı.',ip=['Bir çantanın maliyetini bulmak için tablodaki bilgilerden hangilerine ihtiyacın var?'],bilgi=[KAR,YUZ],sekil=SK,
 ad=[A('Toplam gider','Dört kalem toplanır.','4200 + 3000 + 1800 + 600 = 9600 TL'),A('Birim maliyet','80 çantaya bölünür.','9600 ÷ 80 = 120 TL'),A('Kâr','Maliyetin %25’i.','120 × 0,25 = 30 TL'),A('Satış fiyatı','Maliyet + kâr.','120 + 30 = 150 TL')],
 puf='Önce bir çantanın maliyetini bul.')

# 06 orta · karışım
k_kg,k_f,l_kg,l_f=4,60,2,90; mal=k_kg*k_f+l_kg*l_f; kg=k_kg+l_kg; bm=Fr(mal,kg); sf=84
assert mal==420 and kg==6 and bm==70; v=(sf-bm)*100/bm; assert v==20
e=[7,9,12,14]; assert len({v,*e})==5 and (sf-Fr(75))*100/75==12 and sf-75==9 and sf-70==14 and Fr(14,2)==7
def torba(x,ad,kg_,fy): return f'\\draw[thick,rounded corners=6pt,fill=vurgu!15] ({x},0) rectangle ({x+2.2},1.7); \\node at ({x+1.1},1.3) {{{ad}}}; \\node at ({x+1.1},0.85) {{{kg_} kg}}; \\node at ({x+1.1},0.4) {{{fy} TL/kg}};'
o=[torba(0,'K çayı',k_kg,k_f),'\\node at (2.7,0.85) {+};',torba(3.2,'L çayı',l_kg,l_f),'\\node at (5.9,0.85) {$\\Rightarrow$}; \\node[draw,thick,rounded corners=3pt,fill=vurgu!35,minimum width=2.2cm,minimum height=1.5cm] at (7.3,0.85) {karışım};']
SK=fig('\n'.join(o))
q('0006',tipId='kzc-karisim',tip='Karışım ve kâr',z='orta',alt='Çay Karışımı',kaz='İki ürün karışımında toplam maliyetten birim maliyeti bulup kâr yüzdesini hesaplar.',kalip='hikâyeli',
 kart='K-KZC-06 · maliyet 420 TL / 6 kg = 70 TL; satış 84 TL; kâr %20',
 metin='Bir çaycı, şekildeki iki çeşit çayı belirtilen miktar ve kilogram fiyatlarıyla satın almış, hepsini karıştırmıştır. Karışımın her kilogramını 84 TL’den satmıştır; başka gider yapmamıştır ve karıştırırken hiçbir kayıp olmamıştır.\nBuna göre, çaycının bu satıştan elde ettiği kâr yüzde kaçtır?',
 dogru=int(v),yan=[(7,'Kg başına kârı (14 TL) iki çeşide bölmüş.','dikkat'),(9,'Ortalamadan (75) kâr tutarını bulup yüzde sanmış.','dikkat'),(12,'Fiyatların aritmetik ortalamasını (75) birim maliyet almış.','dikkat'),(14,'Kilogram başına kârı (14 TL) kâr yüzdesi sanmış.','dikkat')],
 istenen='Kâr yüzdesi.',ip=['Karışımın toplam alış tutarını ve toplam kilogramını bulup birim maliyete ulaş.'],bilgi=[KAR],sekil=SK,
 ad=[A('Toplam alış','Her çeşidin tutarı.','4 × 60 + 2 × 90 = 420 TL'),A('Birim maliyet','6 kg’a bölünür.','420 ÷ 6 = 70 TL'),A('Kg başına kâr','Satış − maliyet.','84 − 70 = 14 TL'),A('Kâr yüzdesi','Maliyete oran.','14 ÷ 70 = %20')],
 puf='Önce karışımın bir kilogramının maliyetini bul.')

# 07 zor · gelir-gider doğruları
bf=60; bg=20; sg=3000; adet=180
assert 100*bf==6000 and sg+100*bg==5000 and sg+150*bg==6000
v=adet*(bf-bg)-sg; assert v==4200
e=[6300,7200,7800,10800]; assert len({v,*e})==5 and adet*bf==10800 and adet*(bf-bg)==7200 and adet*bf-sg==7800 and (adet-75)*bf==6300
sx=0.03; sy=0.5/1000
o=['\\draw[-{Stealth}] (0,0) -- (5.0,0) node[right] {adet}; \\draw[-{Stealth}] (0,0) -- (0,3.4) node[above] {TL};',
 f'\\draw[thick,vurgu!70!black] (0,0) -- ({150*sx},{9000*sy}); \\node[left] at ({128*sx},{9000*sy*0.85+0.1}) {{gelir}};',
 f'\\draw[thick] (0,{3000*sy}) -- ({150*sx},{6000*sy}); \\node[below right] at ({140*sx},{5900*sy*0.97}) {{gider}};',
 f'\\draw[dashed,gray] ({100*sx},0) -- ({100*sx},{6000*sy}); \\draw[dashed,gray] (0,{6000*sy}) -- ({100*sx},{6000*sy}); \\draw[dashed,gray] (0,{5000*sy}) -- ({100*sx},{5000*sy});',
 f'\\node[below] at ({100*sx},0) {{100}}; \\node[left] at (0,{3000*sy}) {{3000}}; \\node[left] at (0,{5000*sy}) {{5000}}; \\node[left] at (0,{6000*sy}) {{6000}};']
SK=fig('\n'.join(o))
q('0007',tipId='kzc-basabas',tip='Gelir–gider grafiği',z='zor',alt='Gelir ve Gider Doğruları',kaz='Gelir ve gider doğrularından birim fiyat, birim gider ve sabit gideri okuyup verilen adetteki kârı hesaplar.',kalip='grafik',
 kart='K-KZC-07 · gelir 60 TL/adet; gider 3000 + 20 TL/adet; 180 adette kâr 4200 TL',
 metin='Bir el sanatları atölyesinin bir ayda sattığı ürün sayısına göre toplam gelirini ve toplam giderini gösteren iki doğru şekildeki gibidir. Gider doğrusu, hiç ürün satılmasa da ödenen sabit gideri içermektedir ve satılan her ürün aynı fiyattan satılmaktadır. Gelir ve gider doğrularının her ikisi de adet arttıkça düzgün biçimde artmaktadır.\nBuna göre, atölye bir ayda 180 ürün sattığında kâr kaç TL olur?',
 dogru=v,yan=[(10800,'Toplam geliri kâr sanmış.','dikkat'),(6300,'Başa baş noktasından sonraki adedi satış fiyatıyla çarpmış.','dikkat'),(7200,'Sabit gideri hesaba katmamış.','dikkat'),(7800,'Değişken gideri hesaba katmamış: 10800 − 3000.','dikkat')],
 istenen='180 ürün satıldığında kâr.',ip=['100 ürün için gelir ve gider değerlerinden birim satış fiyatını ve birim gideri bul.'],bilgi=[KAR,GRF],sekil=SK,
 ad=[A('Birim satış','100 üründe gelir 6000 TL.','6000 ÷ 100 = 60 TL'),A('Birim gider','Gider 5000, sabit 3000.','(5000 − 3000) ÷ 100 = 20 TL'),A('180 ürünün geliri','Satış fiyatıyla çarpılır.','180 × 60 = 10800 TL'),A('180 ürünün gideri','Sabit + değişken.','3000 + 180 × 20 = 6600 TL'),A('Kâr','Gelir − gider.','10800 − 6600 = 4200 TL')],
 puf='Gider doğrusunun başlangıcı sabit giderdir.')

# 08 zor · manav fire
alis_kg=20; toplam=400; r1,r2,r3=60,30,10; f1,f2=30,24
k1=toplam*r1//100; k2=toplam*r2//100; k3=toplam*r3//100
gel=k1*f1+k2*f2; mal=toplam*alis_kg; v=(gel-mal)*100//mal
assert (k1,k2,k3)==(240,120,40) and gel==10080 and mal==8000 and Fr(gel-mal,mal)==Fr(26,100)
e=[10,20,24,35]; assert len({v,*e})==5 and (f1+f2)*100//2//alis_kg-100==35 and Fr(gel,(k1+k2)*alis_kg)==Fr(14,10)
o=[dilim(0,216,'vurgu!25'),dilim(216,324,'vurgu!10'),dilim(324,360,'vurgu!55')]
o.append('\\node[above] at (0,1.55) {normal fiyat: %60}; \\node[below] at (270:1.5) {indirimli: %30}; \\node[right] at (1.55,-0.45) {çürük: %10};')
SK=fig('\n'.join(o))
q('0008',tipId='kzc-dilim',tip='Daire grafiği ve oran',z='zor',alt='Daire Grafiği ve Fire',kaz='Daire grafiğindeki satış dilimlerinden gelir ve fireyi hesaplayıp toplam kâr yüzdesini bulur.',kalip='hikâyeli',
 kart='K-KZC-08 · 400 kg; gelir 10080 TL, alış 8000 TL; kâr %26',
 metin='Bir manav, kilogramını 20 TL’den aldığı 400 kg elmayı satmıştır. Şekildeki daire grafiği, elmaların satış durumunu göstermektedir: normal fiyatla satılanlar kilogramı 30 TL’den, indirimli satılanlar kilogramı 24 TL’den satılmıştır; çürük elmalar atılmış ve gelir getirmemiştir.\nBuna göre, manavın bu satıştan kâr yüzdesi kaçtır?',
 dogru=int(v),yan=[(10,'Çürük oranını kâr yüzdesi sanmış.','dikkat'),(20,'Alış fiyatını (20 TL) kâr yüzdesi sanmış.','dikkat'),(24,'İndirimli satış fiyatını (24 TL) kâr yüzdesi sanmış.','dikkat'),(35,'İki satış fiyatının ortalamasını (27) alıp çürüğü hesaba katmamış.','dikkat')],
 istenen='Manavın kâr yüzdesi.',ip=['Her dilimdeki elma miktarını kilogram olarak bul; çürük elmaların geliri yoktur.'],bilgi=[KAR,ORN],sekil=SK,
 ad=[A('Dilimlerin kilogramı','400 kg üzerinden.','240 kg, 120 kg, 40 kg'),A('Gelir','Çürük gelir getirmez.','240 × 30 + 120 × 24 = 10080 TL'),A('Alış','Bütün elmalar alınmıştır.','400 × 20 = 8000 TL'),A('Kâr','Gelir − alış.','10080 − 8000 = 2080 TL'),A('Kâr yüzdesi','Alışa oranlanır.','2080 ÷ 8000 = %26')],
 puf='Alış tutarına çürüklerin de dahil olduğunu unutma.')

# 09 zor · oranlı alış
T=4000; pk,pl=3,2; ak=T*pk//(pk+pl); al=T*pl//(pk+pl)
kk=ak*Fr(20,100); zl=al*Fr(10,100); v=kk-zl
assert (ak,al)==(2400,1600) and kk==480 and zl==160 and v==320
e=[160,200,240,280]; assert len({int(v),*e})==5 and T//2*20//100-T//2*10//100==200 and ak*10//100==240 and 480-200==280
o=[]
for j in range(5): o.append(f'\\filldraw[fill=vurgu!{50 if j<3 else 12},draw=vurgu!80!black] ({j*1.1:.1f},0) rectangle ({(j+1)*1.1:.1f},0.8);')
o.append('\\node at (1.65,0.4) {K}; \\node at (4.95,0.4) {L};')
o.append('\\draw[<->] (0,1.2) -- (5.5,1.2); \\node[above=1pt] at (2.75,1.2) {toplam alış: 4000 TL};')
o.append('\\draw[<->] (0,-0.4) -- (3.3,-0.4); \\node[below=1pt] at (1.65,-0.4) {%20 kârla}; \\draw[<->] (3.3,-0.4) -- (5.5,-0.4); \\node[below=1pt] at (4.4,-0.4) {%10 zararla};')
SK=fig('\n'.join(o))
q('0009',tipId='kzc-model',tip='Kutu modeli ve oran',z='orta',alt='Oranlı Alış',kaz='Toplam alış tutarını orana göre bölüp biri kârla, diğeri zararla satılan malların net sonucunu bulur.',kalip='hikâyeli',
 kart='K-KZC-09 · alış K 2400, L 1600; kâr 480, zarar 160; net kâr 320 TL',
 metin='Bir tüccar, K ve L mallarını şekildeki gibi birbirine eş parçalarla gösterilen oranlarda almış ve toplam 4000 TL ödemiştir. Şekilde K malının %20 kârla, L malının %10 zararla satıldığı belirtilmiştir. Tüccarın başka bir gideri ve geliri yoktur.\nBuna göre, tüccarın bu iki mal satışından elde ettiği net kâr kaç TL’dir?',
 dogru=int(v),yan=[(160,'Yalnız L malındaki zararı net sonuç sanmış.','dikkat'),(200,'Alışı iki mala eşit (2000 TL) paylaştırmış.','dikkat'),(240,'Kâr ile zarar yüzdesini karıştırıp K malının alışının %10’unu (240) net kâr saymış.','dikkat'),(280,'Zararı eşit paylaşımla (200 TL) hesaplayıp 480’den çıkarmış.','dikkat')],
 istenen='Net kâr.',ip=['4000 TL’yi şekildeki oranla K ve L malına paylaştır; kâr ve zararı ayrı ayrı hesapla.'],bilgi=[KAR,KUT],sekil=SK,
 ad=[A('Alışlar','3 : 2 oranında paylaştırılır.','K = 2400 TL, L = 1600 TL'),A('K’deki kâr','%20’si.','2400 × 0,2 = 480 TL'),A('L’deki zarar','%10’u.','1600 × 0,1 = 160 TL'),A('Net kâr','Kâr − zarar.','480 − 160 = 320 TL')],
 puf='Kâr ile zarar farklı alışlara uygulanır.')

# 10 zor · zincirleme kâr
son=270; c=Fr(125,100)*Fr(120,100)*Fr(150,100); v=Fr(son)/c
assert c==Fr(9,4) and v==120
e=[144,150,180,216]; assert len({int(v),*e})==5 and Fr(son)/Fr(150,100)==180 and Fr(son)/(Fr(120,100)*Fr(150,100))==150 and Fr(son)/(Fr(125,100)*Fr(150,100))==144 and Fr(son)/Fr(125,100)==216
bx=lambda x,t: f'\\node[draw,thick,rounded corners=3pt,fill=vurgu!12,minimum width=1.9cm,minimum height=1.0cm] at ({x},0) {{{t}}};'
o=[bx(0.0,'Üretici'),bx(4.0,'Toptancı'),bx(8.0,'Mağaza'),'\\node[draw,thick,rounded corners=3pt,fill=vurgu!40,minimum width=1.9cm,minimum height=1.0cm] at (12.0,0) {Müşteri};']
for x,t in ((2.0,'%25 kârla'),(6.0,'%20 kârla'),(10.0,'%50 kârla')): o.append(f'\\draw[-{{Stealth}},thick] ({x-0.95:.2f},0) -- ({x+0.95:.2f},0); \\node[above=2pt] at ({x},0) {{\\normalsize {t}}};')
o.append('\\node[below=6pt] at (12.0,-0.5) {270 TL öder};')
SK=fig('\n'.join(o))
q('0010',tipId='kzc-zincir',tip='Zincirleme kâr',z='zor',alt='Zincirleme Kâr',kaz='Üretimden müşteriye giden zincirde her halkanın kâr yüzdesini art arda uygulayıp ilk maliyeti bulur.',kalip='hikâyeli',
 kart='K-KZC-10 · çarpan 1,25 × 1,2 × 1,5 = 2,25; maliyet 120 TL',
 metin='Bir ürün, şekildeki zincirde üreticiden toptancıya, toptancıdan mağazaya, mağazadan müşteriye satılmaktadır. Üretici ürünü üretim maliyeti üzerinden, diğer halkalar ise aldıkları fiyat üzerinden okun üzerinde yazan yüzdeyle kârlı satmıştır. Müşteri ürüne 270 TL ödemiştir ve zincirde başka hiçbir gider ya da vergi hesaba katılmamıştır.\nBuna göre, üreticinin ürünü üretim maliyeti kaç TL’dir?',
 dogru=int(v),yan=[(144,'Toptancıyı atlamış: 270 ÷ (1,25 × 1,5).','dikkat'),(150,'Üreticinin kârını atlamış: 270 ÷ (1,2 × 1,5).','dikkat'),(180,'Yalnız mağazanın %50 kârını geri almış.','dikkat'),(216,'Yalnız üreticinin %25 kârını geri almış.','dikkat')],
 istenen='Üretim maliyeti.',ip=['Her halkada fiyatın kaç katına çıktığını düşün.'],bilgi=[KAR,ZNC],sekil=SK,
 ad=[A('Çarpanlar','%25, %20 ve %50 kâr.','1,25 · 1,2 · 1,5'),A('Toplam çarpan','Çarpanlar çarpılır.','1,25 × 1,2 × 1,5 = 2,25'),A('Maliyet','Müşterinin ödediği çarpana bölünür.','270 ÷ 2,25 = 120 TL'),A('Kontrol','İleri doğru yürü.','120 → 150 → 180 → 270')],
 puf='Son fiyattan geriye doğru git.')

bitir(P,'karzararsekb',UK)
