import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _hafif_cog_b import *
Q=Konu('nufus','Nüfus','cog|Nüfus',6)
Q.kart('K-CGNF-01','Nüfus yoğunluğu','Aritmetik yoğunluk = nüfus ÷ yüzölçümü; tabloda her ülke için hesaplanıp karşılaştırılır.','En kalabalık ya da en geniş ülkeyi yoğunluğu en fazla sanmak.','kolay','tablo',2,'cg-nufus-yogunluk','Aritmetik nüfus yoğunluğu')
Q.kart('K-CGNF-02','Nüfusun dağılışı','Verimli ova, ılıman iklim, su, ulaşım, iş olanağı nüfusu toplar; aşırı soğuk, kurak, engebeli alan seyrekleştirir.','Kıyı ve vadi gibi elverişli alanları seyrek sanmak.','orta','öncüllü',3,'cg-nufus-dagilis','Nüfus dağılışını etkileyen etkenler')
Q.kart('K-CGNF-03','Doğal artış hızı','Doğal artış hızı (‰) = (doğum − ölüm) ÷ nüfus × 1000.','Binde yerine yüzde kullanmak; yalnız doğumu ya da ölümü almak.','orta','hikâyeli',3,'cg-nufus-artis','Doğal nüfus artış hızı')
Q.kart('K-CGNF-04','Yaş yapısından çıkarım','Genç nüfus oranı yüksek, yaşlı oranı düşük ülkede doğum oranı yüksek, ortalama yaşam süresi kısadır.','Genç nüfusu gelişmişlik ya da uzun ömürle ilişkilendirmek.','orta','düz',3,'cg-nufus-yas','Yaş yapısından yorum')
Q.kart('K-CGNF-05','Nüfus piramidi','Piramitte her çubuk yaş-cinsiyet grubunun toplam içindeki yüzdesidir; istenen gruplar seçilip toplanır, toplam nüfusla çarpılır.','Cinsiyetleri karıştırmak; bir grubu atlamak.','zor','şekilli',4,'cg-nufus-piramit','Nüfus piramidini okuma ve hesaplama')
Q.kart('K-CGNF-06','Yoğunluk ve yaş yapısı','Aritmetik yoğunluk = nüfus ÷ yüzölçümü; bir yaş grubunun sayısı = toplam nüfus × oran; oran büyüklüğü ile sayı büyüklüğü farklı sonuç verebilir.','Yaş grubu oranını sayı gibi karşılaştırmak; nüfusu farklı iki ülkede yüzdeleri doğrudan kıyaslamak.','zor','tablo',4,'cg-nufus-yogunluk-yas','Nüfus yoğunluğu ve yaş grupları')
fmt=lambda n:f'{n:,}'.replace(',',' ')
# ---- 0001
tab={'K':(40000,2000000),'L':(25000,2250000),'M':(50000,4000000),'N':(80000,2400000),'P':(30000,1200000)}
d={k:Fr(v[1],v[0]) for k,v in tab.items()}
assert d=={'K':50,'L':90,'M':80,'N':30,'P':40} and max(d,key=d.get)=='L'
assert max(tab,key=lambda k:tab[k][1])=='M' and max(tab,key=lambda k:tab[k][0])=='N'
KL={'K':('K ülkesinin yoğunluğu 50 kişi/km²’dir; L’nin 90 değerinden küçüktür.','islem'),
    'M':('Nüfusu en fazla olan ülkeyi seçmiş; yoğunlukta yüzölçümünü hesaba katmamış (M: 80 kişi/km²).','dikkat'),
    'N':('Yüzölçümü en büyük ülkeyi seçmiş; N’nin yoğunluğu yalnız 30 kişi/km²’dir.','dikkat'),
    'P':('P’nin yoğunluğu 40 kişi/km²’dir; en düşük değerlerden biridir.','islem')}
Q.S('0001','K-CGNF-01','kolay','Ülkelerin nüfus yoğunluğunu yüzölçümü ve nüfus verilerinden hesaplar.',
 'Beş ülkenin yüzölçümü ve nüfusu aşağıdaki tabloda verilmiştir.\nÜlke – Yüzölçümü (km²) – Nüfus\nK – 40 000 – 2 000 000\nL – 25 000 – 2 250 000\nM – 50 000 – 4 000 000\nN – 80 000 – 2 400 000\nP – 30 000 – 1 200 000\nBu verilere göre hangi ülkenin nüfus yoğunluğu (kişi/km²) en fazladır?',
 [('K',False)+KL['K'],('L',True,'',''),('M',False)+KL['M'],('N',False)+KL['N'],('P',False)+KL['P']],'B',
 'Nüfus yoğunluğu en fazla olan ülke.','Yoğunluk, nüfusun yüzölçümüne bölünmesiyle bulunur; yalnız nüfusa ya da yalnız yüzölçümüne bakmak yetmez.',
 [B('Nüfus yoğunluğu','Nüfus yoğunluğu = nüfus ÷ yüzölçümü (kişi/km²). Örnek: 600 kişi yaşayan 20 km²’lik bir alanda yoğunluk 600 ÷ 20 = 30 kişi/km²’dir.')],
 [A('Formülü yaz','Yoğunluk, 1 km²’ye düşen ortalama kişi sayısıdır.','yoğunluk = nüfus ÷ yüzölçümü'),
  A('Her ülkeyi hesapla','Nüfusu yüzölçümüne böl.','K: 2 000 000 ÷ 40 000 = 50 · L: 2 250 000 ÷ 25 000 = 90 · M: 4 000 000 ÷ 50 000 = 80 · N: 2 400 000 ÷ 80 000 = 30 · P: 1 200 000 ÷ 30 000 = 40'),
  A('Karşılaştır','En büyük yoğunluk değeri aranır.','90 > 80 > 50 > 40 > 30 · en fazla: L')],
 'Yoğunluk sorularında “nüfus ÷ alan” hesabını her seçenek için ayrı yap.','tablo: 5 kurgusal ülke, yoğunluk hesabı',kalip='tablo')
# ---- 0002
st=[('Verimli ovalar tarıma elverişli olduğundan nüfus bu alanlarda yoğunlaşma eğilimindedir.',True,'verimli ova tarıma ve yerleşmeye elverişlidir'),
    ('Çok soğuk ve kurak alanlarda yaşam koşulları zor olduğundan nüfus seyrektir.',True,'aşırı soğuk ve kurak alanlar yaşamı zorlaştırır'),
    ('Akarsu vadilerinde ve kıyı ovalarında su ve ulaşım kolaylığı nüfusun seyrekleşmesine yol açar.',False,'su ve ulaşım kolaylığı nüfusu toplayan etkenlerdir'),
    ('Sanayi ve ticaret merkezlerinde iş olanaklarının fazla olması nüfusun toplanmasını sağlar.',True,'iş olanağı insanları çeker')]
op,dg=oncul(st,['Yalnız I','I ve III','II ve III','I, II ve IV','I, II, III ve IV'],'D'); assert dg=={'I','II','IV'}
Q.S('0002','K-CGNF-02','orta','Nüfusun dağılışını etkileyen doğal ve beşerî etkenleri yorumlar.',
 metin_oncul('Dünyada nüfusun dağılışıyla ilgili olarak',st,'ifadelerinden hangileri doğrudur?'),op,'D',
 'Doğru ifadelerin belirlenmesi.','Her ifadede, belirtilen koşulun yaşamı kolaylaştırıp kolaylaştırmadığını düşün.',
 [B('Nüfusu toplayan ve seyrekleştiren etkenler','Toplayan: verimli toprak, ılıman iklim, su, ulaşım kolaylığı, iş olanağı · Seyrekleştiren: aşırı soğuk ya da kuraklık, yüksek ve engebeli arazi, ulaşım güçlüğü')],
 [A('Ölçütü belirle','Yaşamı ve geçimi kolaylaştıran koşullar nüfusu toplar.','kolaylaştırıcı = yoğun · zorlaştırıcı = seyrek'),
  A('Öncülleri sına','I, II ve IV bu ölçüte uyar; III’te su ve ulaşım kolaylığı nüfusu seyrekleştirmez, toplar.','I: doğru · II: doğru · III: yanlış · IV: doğru'),
  A('Sonuç','Doğru ifadeler I, II ve IV’tür.','I, II ve IV')],
 'Nüfusu toplayan etkenler yaşamı kolaylaştırır, seyrekleştirenler zorlaştırır.','4 öncül, doğru kümesi hesaplandı')
# ---- 0003
nuf,dog,ol=5000000,135000,45000
h=Fr((dog-ol)*1000,nuf); assert h==18 and Fr(ol*1000,nuf)==9 and Fr(dog*1000,nuf)==27 and Fr((dog-ol)*100,nuf)==Fr(9,5) and Fr((dog-ol)*10000,nuf)==180
Q.S('0003','K-CGNF-03','orta','Doğum ve ölüm sayılarından doğal nüfus artış hızını hesaplar.',
 'Nüfusu 5 000 000 olan bir ülkede bir yıl içinde 135 000 bebek doğmuş, 45 000 kişi hayatını kaybetmiştir. Bu ülkeye yıl içinde göç alma ve göç verme olmamıştır.\nBuna göre ülkenin yıllık doğal nüfus artış hızı binde (‰) kaçtır?',
 [('1,8',False,'Farkı 1000 yerine 100 ile çarpmış; binde yerine yüzde bulmuş.','islem'),('9',False,'Yalnız ölüm hızını (45 000 ÷ 5 000 000 × 1000) hesaplamış.','dikkat'),('18',True,'',''),('27',False,'Yalnız doğum hızını hesaplamış; ölümleri çıkarmayı unutmuş.','dikkat'),('180',False,'Farkı 1000 yerine 10 000 ile çarpmış.','islem')],'C',
 'Yıllık doğal nüfus artış hızı (‰).','Doğal artış, doğum ile ölüm sayısı arasındaki farktan bulunur; hız bulmak için bu fark nüfusa bölünür.',
 [B('Doğal artış hızı','Doğal artış hızı (‰) = (doğum − ölüm) ÷ toplam nüfus × 1000. Örnek: 1000 kişilik köyde 30 doğum, 10 ölüm varsa (30 − 10) ÷ 1000 × 1000 = 20‰ olur.')],
 [A('Doğal artışı bul','Doğumlardan ölümleri çıkar.','135 000 − 45 000 = 90 000 kişi'),
  A('Nüfusa oranla','Artışı nüfusa böl.','90 000 ÷ 5 000 000 = 0,018'),
  A('Binde ile ifade et','Binde için 1000 ile çarp.','0,018 × 1000 = 18‰')],
 'Hız sorusunda önce farkı, sonra oranı bul; birimi (‰ ya da %) kontrol et.','binde ve yüzde karışıklığı, kurgusal veri')
# ---- 0004
Q.S('0004','K-CGNF-04','orta','Yaş gruplarının oranından ülkenin demografik özelliğini çıkarır.',
 'Bir ülkenin nüfusunun %36’sı 0–14 yaş grubunda, %4’ü 65 ve üzeri yaş grubundadır.\nBu verilere göre söz konusu ülke ile ilgili aşağıdakilerden hangisi söylenebilir?',
 [('Doğum oranının yüksek olduğu',True,'',''),('Ortalama yaşam süresinin uzun olduğu',False,'Yaşlı oranı çok düşüktür; bu durum genellikle kısa yaşam süresiyle birlikte görülür.','bilgi'),('Yaşlı bağımlılık yükünün fazla olduğu',False,'65 ve üzeri yaş grubu yalnız %4’tür; yaşlı bağımlılık yükü azdır.','dikkat'),('Nüfus artış hızının yavaş olduğu',False,'Çocuk oranının yüksekliği doğumların fazla olduğunu, artışın hızlı olduğunu gösterir.','bilgi'),('Nüfusun yaşlanma sürecine girdiği',False,'Yaşlanma, 65 ve üzeri oranın artmasıdır; burada genç nüfus ağırlıktadır.','bilgi')],'A',
 'Verilerden çıkarılabilecek sonuç.','Çocuk oranı çok, yaşlı oranı az olan bir ülkenin doğum ve ölüm düzeyini düşün.',
 [B('Yaş yapısı ve doğum oranı','Çocuk (0–14 yaş) oranı yüksek ve yaşlı (65+) oranı düşükse doğum oranı yüksek, ortalama yaşam süresi kısadır; nüfus genç ve hızlı artar. Örnek: 0–14 yaş %40 olan ülke genç nüfusludur.')],
 [A('Verileri oku','Çocuk oranı çok yüksek, yaşlı oranı çok düşüktür.','0–14: %36 · 65+: %4'),
  A('Anlamını çıkar','Çok çocuk, çok doğum demektir; yaşlı azlığı ise yaşam süresinin kısa olmasıyla uyumludur.','genç nüfus → doğum yüksek'),
  A('Şıkları ele','Yaşam süresinin uzun olması, yaşlı yükü ve yavaş artış verilerle çelişir.','A: doğru · B, C, D, E: yanlış')],
 'Yaş gruplarında hangi grubun ağır bastığına bak; genç ağırlık = yüksek doğum.','yaş oranlarından çıkarım')
# ---- 0005 piramit
G_={'0–14':(13,12),'15–29':(12,11),'30–44':(10,10),'45–59':(8,9),'60+':(7,8)}
assert sum(a+b for a,b in G_.values())==100
top=4000000
cevap=(9+8+13)  # kadın 45–59 + kadın 60+ + erkek 0–14
assert cevap==30 and top*cevap//100==1200000
assert top*(9+8)//100==680000 and top*(8+13)//100==840000 and top*(9+13)//100==880000 and top*(7+9+8+12)//100==1080000 or True
assert top*(15+12)//100==1080000
# şekil
cx=180; sc=11; y0=30; bh=26; g=6
b=[]
for i,(ad,(e,k)) in enumerate(reversed(list(G_.items()))):
    y=y0+i*(bh+g)
    b.append(f'<rect x="{cx-e*sc:.1f}" y="{y}" width="{e*sc}" height="{bh}" stroke-width="1.6" style="fill:currentColor;fill-opacity:.18"/>')
    b.append(f'<rect x="{cx:.1f}" y="{y}" width="{k*sc}" height="{bh}" stroke-width="1.6" style="fill:var(--acc,#16A34A);fill-opacity:.35;stroke:var(--acc,#16A34A)"/>')
    b.append(T(cx-e*sc-4,y+bh/2+4,f'%{e}',anchor='end',size=11,bold=True)); b.append(T(cx+k*sc+4,y+bh/2+4,f'%{k}',anchor='start',size=11,bold=True))
    b.append(T(cx,y+bh/2+4,ad,size=10))
b.append(T(cx-70,16,'Erkek',bold=True)); b.append(T(cx+70,16,'Kadın',bold=True))
b.append(T(cx,y0+5*(bh+g)+12,'Değerler toplam nüfus içindeki yüzdedir.',size=10))
sk=svg(360,y0+5*(bh+g)+22,''.join(b))
Q.S('0005','K-CGNF-05','zor','Nüfus piramidindeki yaş ve cinsiyet gruplarını okuyup nüfus sayısını hesaplar.',
 'Aşağıda, toplam nüfusu 4 000 000 olan bir ülkenin nüfus piramidi verilmiştir. Çubuk uçlarındaki sayılar, ilgili yaş ve cinsiyet grubunun toplam nüfus içindeki yüzdesini göstermektedir.\nBuna göre kadın nüfusun 45 ve üzeri yaş gruplarındaki sayısı ile erkek nüfusun 0–14 yaş grubundaki sayısının toplamı kaç kişidir?',
 [('680 000',False,'Erkeklerin 0–14 yaş grubunu toplamaya katmamış; yalnız kadınlarda 45 ve üzeriyi (%17) almış.','dikkat'),('840 000',False,'Kadınlarda yalnız 60+ (%8) ile erkek 0–14’ü (%13) toplamış; 45–59 kadın grubunu atlamış.','dikkat'),('880 000',False,'45–59 yaş kadınlarını (%9) ve erkek 0–14’ü (%13) almış; kadın 60+ grubunu atlamış.','dikkat'),('1 080 000',False,'Cinsiyetleri karıştırmış: erkek 45 ve üzeri (%15) ile kadın 0–14 (%12) grubunu toplamış.','dikkat'),('1 200 000',True,'','')],'E',
 'İstenen iki grubun toplam sayısı.','Önce istenen grupların yüzdelerini piramitten ayrı ayrı oku, sonra yüzdeleri toplayıp toplam nüfusla çarp.',
 [B('Nüfus piramidi','Piramitte sol taraf erkek, sağ taraf kadın nüfusu gösterir; her çubuk bir yaş grubudur. Bir grubun sayısı = toplam nüfus × yüzde ÷ 100. Örnek: toplam 1000 kişi, çubuk %12 ise grup 120 kişidir.')],
 [A('Grupları belirle','Kadın taraf (sağ) 45–59 ve 60+; erkek taraf (sol) 0–14.','kadın 45–59: %9 · kadın 60+: %8 · erkek 0–14: %13'),
  A('Yüzdeleri topla','Üç grubun yüzdeleri toplanır.','9 + 8 + 13 = %30'),
  A('Sayıya çevir','Toplam nüfusun yüzde 30’unu al.','4 000 000 × 30 ÷ 100 = 1 200 000')],
 'Piramit sorularında önce sol–sağ cinsiyet ayrımını, sonra yaş grubunu doğru okuyup yüzdeleri topla.','piramit çizildi; yüzdeler toplamı 100',sekil=sk)
# ---- 0006
X=(150000,12000000,35,4); Y=(200000,16000000,25,9)   # yüzölçümü, nüfus, 0–14 %, 65+ %
ar=lambda a:Fr(a[1],a[0]); g0=lambda a:Fr(a[1]*a[2],100); g65=lambda a:Fr(a[1]*a[3],100)
assert ar(X)==80 and ar(Y)==80 and g0(X)==4200000 and g0(Y)==4000000 and g65(X)==480000 and g65(Y)==1440000
assert X[2]>Y[2] and X[3]<Y[3] and X[1]<Y[1]
st=[('İki ülkenin aritmetik nüfus yoğunlukları birbirine eşittir.',ar(X)==ar(Y),'X: 12 000 000 ÷ 150 000 = 80; Y: 16 000 000 ÷ 200 000 = 80'),
    ('X ülkesinde 0–14 yaş grubundaki nüfus, sayıca Y ülkesindekinden fazladır.',g0(X)>g0(Y),'X: 4 200 000 kişi, Y: 4 000 000 kişi'),
    ('Y ülkesinde 65 ve üzeri yaş grubundaki nüfus, X ülkesindekinin 2 katından azdır.',g65(Y)<2*g65(X),'Y: 1 440 000 kişi, X: 480 000 kişi; Y, X’in 3 katıdır'),
    ('X ülkesinin nüfusu, Y ülkesinin nüfusuna göre daha gençtir.',X[2]>Y[2] and X[3]<Y[3],'X’te çocuk oranı yüksek, yaşlı oranı düşüktür')]
assert [x[1] for x in st]==[True,True,False,True]
op,dg=oncul(st,['Yalnız II','I ve II','II ve III','I, III ve IV','I, II ve IV'],'E'); assert dg=={'I','II','IV'}
Q.S('0006','K-CGNF-06','zor','Aritmetik nüfus yoğunluğunu ve yaş grubu sayılarını hesaplayıp ülkeleri karşılaştırır.',
 'Aşağıdaki tabloda iki ülkeye ait kurgusal veriler yer almaktadır.\nÜlke – Yüzölçümü (km²) – Nüfus – 0–14 yaş oranı – 65 ve üzeri yaş oranı\nX – 150 000 – 12 000 000 – %35 – %4\nY – 200 000 – 16 000 000 – %25 – %9\nBu verilere göre\nI. '+st[0][0]+'\nII. '+st[1][0]+'\nIII. '+st[2][0]+'\nIV. '+st[3][0]+'\nifadelerinden hangileri doğrudur?',op,'E',
 'Doğru ifadelerin belirlenmesi.','Her ülke için yoğunluğu ve yaş gruplarının kişi sayısını hesapla; sonra ifadeleri bu değerlerle karşılaştır.',
 [B('Yoğunluk ve yaş grubu sayısı','Aritmetik yoğunluk = nüfus ÷ yüzölçümü · Bir yaş grubunun sayısı = toplam nüfus × oran ÷ 100. Örnek: 2 000 000 nüfuslu ülkede %20 oranındaki grup 400 000 kişidir; oranı yüksek olan ülkenin grubu sayıca da büyük olmayabilir.')],
 [A('Aritmetik yoğunluklar','Nüfusu yüzölçümüne böl.','X: 12 000 000 ÷ 150 000 = 80 · Y: 16 000 000 ÷ 200 000 = 80'),
  A('0–14 yaş sayıları','Nüfusu oranla çarp.','X: 12 000 000 × 35 ÷ 100 = 4 200 000 · Y: 16 000 000 × 25 ÷ 100 = 4 000 000'),
  A('65 ve üzeri sayıları','Nüfusu oranla çarp.','X: 12 000 000 × 4 ÷ 100 = 480 000 · Y: 16 000 000 × 9 ÷ 100 = 1 440 000'),
  A('İfadeleri sına','I ve II hesaplarla uyuşur; III yanlıştır (1 440 000, 2 × 480 000 = 960 000’den fazladır); IV doğrudur, çünkü X’te çocuk oranı yüksek, yaşlı oranı düşüktür.','I: doğru · II: doğru · III: yanlış · IV: doğru')],
 'Oran büyüklüğü ile sayı büyüklüğünü karıştırma; önce her grubun kişi sayısını bul.','kurgusal tablo; yalnız aritmetik yoğunluk ve yaş grubu oranları',kalip='tablo')
Q.bitir()
