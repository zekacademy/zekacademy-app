"""Temel Kavramlar · ŞEKİLLİ ek paket (tksekb): 10 soru, hepsi şekilli/grafikli, kardeş yok, ipucu 1.
Şekil çözüm için gereken veriyi taşır. Her cevap ve çeldirici değeri Python'da hesaplanıp assert edilir."""
import sys,os,itertools,math
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_mat as H
from _hafif_mat import *
from _sekil_sayi import *
H.KONU='Temel Kavramlar'
P=Parti('tksekb','Temel Kavramlar','mat|Temel Kavramlar')
KY='ÖSYM 2018–2026 TYT Matematik (temel kavramlar, şekilli/grafikli sorular; yalnız mantık) · MEB 9. sınıf'
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)
def isp(n): return n>1 and all(n%i for i in range(2,int(n**.5)+1))

ASAL=B('Asal sayı','1’den büyük olup yalnız 1’e ve kendisine bölünen sayıdır; 1 asal değildir, 2 tek çift asal sayıdır. Örnek: 13 asaldır, 15 = 3 × 5 asal değildir')
ZAR=B('Zar açınımı','açınımda bir sıradaki ilk ve üçüncü kareler (aralarında bir kare bırakılarak) zarın karşılıklı yüzleridir; yan yana kareler komşu yüzlerdir. Örnek: yan yana dizilmiş dört karenin 1. ile 3. ve 2. ile 4. kareleri karşılıklıdır')
SAAT=B('Saatte yinelenme','12 saatlik kadranda saat 12’şer saatte aynı konuma döner; bu yüzden geçen toplam süre 12’ye bölünür ve yalnız kalan önemlidir. Örnek: saat 5’ten 30 saat sonra, 30 = 2 × 12 + 6 olduğundan 11’i gösterir')
TAM=B('Tam sayılarla sıcaklık','0’ın altındaki değerler negatiftir; iki değerin farkı büyükten küçük çıkarılarak bulunur. Örnek: −3 ile 5 arasındaki fark 5 − (−3) = 8’dir')
ORU=B('Örüntüde genel terim','şekilden şekle sabit sayıda artış varsa n. şeklin değeri, ilk şekildeki değer ile (n − 1) artışın toplamıdır. Örnek: 4, 7, 10, … örüntüsünde n. terim 4 + 3 · (n − 1) = 3n + 1’dir')
KES=B('Kalanın kesri','bir bütünün a/b’si ayrıldıktan sonra kalanın c/d’si alınıyorsa bu parça bütünün (1 − a/b) · c/d kadarıdır. Örnek: bütünün 1/2’si ayrılınca kalanın 1/3’ü bütünün 1/6’sıdır')
ISARET=B('İşaret kuralları','koordinat düzleminde I. bölgede (+, +), II. bölgede (−, +), III. bölgede (−, −), IV. bölgede (+, −) işaretli noktalar bulunur. Çarpımda işaretler çarpılır: (−)(−) = +, (−)(+) = −. Örnek: II. bölgedeki bir noktanın apsisi ile ordinatının çarpımı negatiftir')
TOP=B('Ardışık toplam','1’den n’ye kadar sayıların toplamı n(n + 1)/2’dir. Örnek: 1 + 2 + 3 + 4 = 4 · 5/2 = 10')
KAT=B('Kat farkı','bodrum katlar negatif, zemin 0, üst katlar pozitif numara taşır; iki kat arasındaki yol, numaraların farkının mutlak değeridir. Örnek: −1 ile 3 arasında |3 − (−1)| = 4 kat vardır')
TEK=B('Çift sayıda değişiklik','bir lambanın düğmesine çift sayıda basılırsa lamba ilk durumunda kalır, tek sayıda basılırsa durumu değişir. Örnek: bir lambaya 2 kez basılınca ilk durumuna döner')

kartla('K-TKB-01','Asal sayılı oyun tahtası','Her kare asal mı diye denetlenir; başlangıçtan bitişe sağa ve aşağı hamlelerle ulaşılan yollar kare kare sayılır.','1’i, 51’i ya da 91’i asal sanmak; bir yolu iki kez saymak.','zor','şekilli',5,'tkb-asal','Asal sayılı karelerden geçen yolları sayma')
kartla('K-TKB-02','Zar açınımı','Açınımdan karşılıklı yüzler okunur; üst ve alt yüz dışında kalan yüzlerin toplamı bulunur.','Komşu yüzü karşılıklı yüz sanmak; yalnız üst yüzü çıkarmak.','kolay','hikâyeli',3,'tkb-zar','Zar açınımında yan yüzlerin toplamı')
kartla('K-TKB-03','Saat kadranı','Başlangıç saati kadrandan okunur; geçen süre 12’ye bölünüp kalan başlangıca eklenir.','Doz sayısıyla aralık sayısını karıştırmak; kalanı saat sanmak.','orta','hikâyeli',4,'tkb-saat','12 saatlik kadranda yinelenen aralık')
kartla('K-TKB-04','Sıcaklık sütun grafiği','Grafikten negatif ve pozitif değerler okunur; toplamlar arasındaki fark tam sayı işlemiyle bulunur.','Negatif toplamın işaretini yok saymak; fark yerine toplam ya da işaretli sonuç yazmak.','kolay','grafik',4,'tkb-sicaklik','Sütun grafiğinde negatif ve pozitif değerler')
kartla('K-TKB-05','Kibrit çöpü örüntüsü','Şekillerden sabit artış bulunur, genel terim yazılır ve eşitsizlikle en büyük şekil belirlenir.','Genel terimdeki sabiti unutmak; parantezi yanlış açmak; şekil numarasıyla artışı karıştırmak.','orta','hikâyeli',4,'tkb-kibrit','Çöp sayısından genel terimle şekil bulma')
kartla('K-TKB-06','Basamaklı blok örüntüsü','Şekillerden blok sayısı için n(n + 1)/2 kuralı çıkarılır; iki değerin farkı hesaplanır.','Yarım çarpımı unutmak; B(n) yerine n² almak; sınır terimi dahil etmek ya da etmemek.','orta','şekilli',4,'tkb-blok','Basamaklı blok dizilimi ve tanımlı gösterim')
kartla('K-TKB-07','Bahçe planı ve kesirler','Kalanın kesri bütünün kesrine çevrilir; verilen alandan bütünün alanı bulunur.','Kalanın kesrini bütünün kesri sanmak; domates bölümünü unutmak.','orta','hikâyeli',4,'tkb-bahce','Parçalı bahçe planında kesirle bütünü bulma')
kartla('K-TKB-08','Koordinat düzleminde işaret','Noktaların bölgelerinden koordinatların işaretleri okunur; öncüller işaret kurallarıyla denetlenir.','Bölgelerin işaretlerini karıştırmak; çarpımın işaretini yanlış belirlemek.','orta','öncüllü',4,'tkb-koordinat','Koordinat bölgelerinden işaret çıkarma')
kartla('K-TKB-09','Bina kat planı','Katların numaraları plandan okunur; ardışık duraklar arasındaki mutlak fark toplanır.','Negatif işareti yok saymak; yalnız ilk ve son kat arasını almak.','kolay','hikâyeli',4,'tkb-kat','Kat planında toplam yer değiştirme')
kartla('K-TKB-10','Lamba paneli','Her lamba için basma sayısı katlardan sayılır; tek sayıda basılan lambaların durumu değişir.','Bir turda bir lambaya basılmasını gözden kaçırmak; durumu değiştirme yerine açma sanmak.','zor','hikâyeli',5,'tkb-lamba','Lambalara basma turlarında yanan lamba sayısı')

# =============== 01 · asal oyun tahtası · zor ===============
G=[[37,53,2,5,25],[51,37,91,11,57],[3,37,41,31,13],[21,47,1,37,47]]
def yollar(g,pr):
    R,C=len(g),len(g[0]); d=[[0]*C for _ in range(R)]
    if not pr(g[0][0]): return 0
    d[0][0]=1
    for i in range(R):
        for j in range(C):
            if (i,j)==(0,0) or not pr(g[i][j]): continue
            d[i][j]=(d[i-1][j] if i else 0)+(d[i][j-1] if j else 0)
    return d[-1][-1]
d1=yollar(G,isp); e1=[yollar(G,lambda n,t=t:isp(n) or n==t) for t in (1,51,91,57)]
assert d1==4 and e1==[6,8,12,5] and len({d1,*e1})==5
assert all(isp(G[0][0]) and isp(G[-1][-1]) for _ in [0]) and 1 in sum(G,[]) and 51 in sum(G,[]) and 91 in sum(G,[]) and 57 in sum(G,[])
# elle sayım: tüm yollar
tum=[]
def dfs(i,j,yol):
    if not isp(G[i][j]): return
    yol=yol+[(i,j)]
    if (i,j)==(3,4): tum.append(yol); return
    if i<3: dfs(i+1,j,yol)
    if j<4: dfs(i,j+1,yol)
dfs(0,0,[]); assert len(tum)==4
o=[]
for i in range(4):
    for j in range(5):
        o.append(nd(j*.95,-i*.8,str(G[i][j]),.95,.8,fill='vurgu!15' if (i,j) in [(0,0),(3,4)] else None))
o.append(tx(0,.75,'Başlangıç','font=\\footnotesize')); o.append(tx(4*.95,-3*.8-.7,'Bitiş','font=\\footnotesize'))
SK1=tz('\n'.join(o))
q('0001',tipId='tkb-asal',tip='Asal sayılı karelerden geçen yolları sayma',z='zor',alt='Asal Sayılar',kaz='Karelerdeki sayıların asal olup olmadığını belirleyip yalnız asal karelerden geçen yolları sayar.',kalip='şekilli',sekil=SK1,
 kart='K-TKB-01 (asal sayılı oyun tahtası) · 4 × 5 tahtada sağa-aşağı hamlelerle 4 yol',
 metin='Ece, kenarları eşit karelerden oluşan aşağıdaki oyun tahtasında sol üst köşedeki başlangıç karesinden sağ alt köşedeki bitiş karesine ulaşmaya çalışıyor. Her hamlede yalnızca bir kare sağa ya da bir kare aşağı gidebiliyor ve yalnızca üzerinde asal sayı yazan karelere basabiliyor.\nBuna göre Ece, bitiş karesine kaç farklı yoldan ulaşabilir?',
 dogru=d1,yan=[(e1[0],'1’i asal saymış; 1’in bulunduğu kareden de geçen yolları eklemiş.','bilgi'),(e1[3],'57’yi asal sanmış (57 = 3 × 19 olduğunu görmemiş); o kareden geçen yolu da saymış.','dikkat'),(e1[1],'51’i asal sanmış (51 = 3 × 17); o kareden geçen yolları da eklemiş.','dikkat'),(e1[2],'91’i asal sanmış (91 = 7 × 13); o kareden geçen yolları da eklemiş.','dikkat')],
 istenen='Başlangıçtan bitişe asal karelerden geçen farklı yol sayısı.',
 ip=['Önce hangi karelerin asal sayı taşıdığını belirle; sonra başlangıçtan başlayıp her asal kareye kaç yolla gelinebildiğini yaz.'],
 bilgi=[ASAL],
 ad=[A('Asal kareleri işaretle','Her kare için 1’den büyük ve yalnız 1’e ile kendisine bölünüp bölünmediği denetlenir; asal olmayan kareler kapalı sayılır.','Kapalı kareler: 25, 51, 91, 57, 21, 1'),A('İlk iki satırı doldur','Bir kareye yalnız üstündeki ve solundaki açık karelerden gelinir; yol sayıları bu iki karenin toplamıdır.','1. satır: 1, 1, 1, 1, kapalı · 2. satır: kapalı, 1, kapalı, 1, kapalı'),A('Üçüncü satır','Soldaki 3’ün üstündeki kare (51) kapalı olduğundan oraya hiç gelinemez.','3. satır: 0, 1, 1, 2, 2'),A('Son satır','Bitiş karesine üstteki ve soldaki karelerden gelinir.','4. satır: kapalı, 1, kapalı, 2, 2 + 2 = 4')],
 puf='Izgarada yol sayısı, her kareye gelen yolların (üstten ve soldan) toplanmasıyla bulunur; kapalı kareler 0 sayılır.')

# =============== 02 · zar açınımı · kolay ===============
Z={(1,3):3,(1,2):7,(1,1):11,(1,0):2,(0,2):5,(2,2):13}
kars={(1,3):(1,1),(1,1):(1,3),(1,2):(1,0),(1,0):(1,2),(0,2):(2,2),(2,2):(0,2)}
assert sorted(Z.values())==[2,3,5,7,11,13] and all(isp(v) for v in Z.values()) and sum(Z.values())==41
ust=(1,2); alt=kars[ust]; assert Z[ust]==7 and Z[alt]==2
d2=41-7-2; assert d2==32
kom=[Z[k] for k in Z if k not in (ust,alt)]; assert sorted(kom)==[3,5,11,13] and sum(kom)==d2
e2={n:41-7-n for n in (3,5,11,13)}; assert e2=={3:31,5:29,11:23,13:21}
assert 41-7==34 and len({d2,31,29,23,34})==5
o=[nd(x,y,str(v),1,1,fill=None) for (x,y),v in Z.items()]
SK2=tz('\n'.join(o))
q('0002',tipId='tkb-zar',tip='Zar açınımında yan yüzlerin toplamı',z='kolay',alt='Asal Sayılar',kaz='Zar açınımından karşılıklı yüzleri belirleyip üst ve alt yüz dışındaki yüzlerin sayı toplamını hesaplar.',kalip='hikâyeli',sekil=SK2,
 kart='K-TKB-02 (zar açınımı) · ilk altı asal sayı, 7 üstte, karşısı 2',
 metin='Bir oyun atölyesinde, her yüzüne farklı bir asal sayı yazılmış küp biçimindeki bir zarın açınımı aşağıda verilmiştir. Zarın yüzlerine ilk altı asal sayı yazılmıştır. Ahmet, zarı üzerinde 7 yazan yüz üstte kalacak biçimde masanın üzerine koyuyor.\nBuna göre zarın masaya değen yüzü ve üst yüzü dışında kalan dört yan yüzündeki sayıların toplamı kaçtır?',
 dogru=d2,yan=[(31,'7’nin üstündeki kareyi (3) karşılıklı yüz sanmış: 41 − 7 − 3 = 31.','dikkat'),(29,'7’nin solundaki kareyi (5) karşılıklı yüz sanmış: 41 − 7 − 5 = 29.','dikkat'),(23,'7’nin altındaki kareyi (11) karşılıklı yüz sanmış: 41 − 7 − 11 = 23.','dikkat'),(34,'Yalnız üst yüzü çıkarmış, masaya değen yüzü çıkarmamış: 41 − 7 = 34.','dikkat')],
 istenen='Dört yan yüzdeki sayıların toplamı.',
 ip=['Açınımda 7’nin karşısında kalan kareyi bul; sonra altı yüzün toplamından üst ve alt yüzü çıkar.'],
 bilgi=[ASAL,ZAR],
 ad=[A('Karşılıklı yüzü bul','7’nin bulunduğu sütunda aralarında bir kare olan karşıdaki kare zarın alt yüzüdür.','7’nin karşısındaki yüz: 2'),A('Altı yüzü topla','Zarın yüzlerinde ilk altı asal sayı vardır.','2 + 3 + 5 + 7 + 11 + 13 = 41'),A('Üst ve alt yüzü çıkar','Yan yüzlerin toplamı kalan dört yüzdür.','41 − 7 − 2 = 32')],
 puf='Zarın karşılıklı yüzleri açınımda aralarında bir kare bırakan karelerdir; yan yüzlerin toplamı = tümü − üst − alt.')

# =============== 03 · saat kadranı · orta ===============
bas3=8; aral=7; doz=10
sn=(bas3+aral*(doz-1))%12 or 12
assert sn==11 and aral*(doz-1)==63 and 63%12==3
e3=[(bas3+aral*doz)%12 or 12,(aral*(doz-1))%12,(bas3-63)%12 or 12,(aral*doz)%12]
assert e3==[6,3,5,10] and len({sn,*e3})==5
r=1.5; o=[f'\\draw[line width=1.2pt] (0,0) circle ({r});']
for k in range(12):
    a=math.radians(90-30*k); c,s_=math.cos(a),math.sin(a)
    o.append(ln(c*(r-.14),s_*(r-.14),c*r,s_*r,'line width=1pt'))
    h=12 if k==0 else k
    o.append(tx(c*(r+.28),s_*(r+.28),f'\\footnotesize {h}'))
ah=math.radians(90-30*bas3); am=math.radians(90)
o.append(ln(0,0,.85*math.cos(ah),.85*math.sin(ah),'line width=3pt,vurgu')); o.append(ln(0,0,1.3*math.cos(am),1.3*math.sin(am),'line width=1.4pt'))
o.append('\\fill (0,0) circle (.07);')
SK3=tz('\n'.join(o))
q('0003',tipId='tkb-saat',tip='12 saatlik kadranda yinelenen aralık',z='orta',alt='Örüntü ve Döngü',kaz='Kadranda okunan saate sabit aralıklı eklemeler yaparak 12 saatlik düzende yinelenen konumu bulur.',kalip='hikâyeli',sekil=SK3,
 kart='K-TKB-03 (saat kadranı) · 8’den başlayıp 7 saatte bir, 10. doz',
 metin='Bir hastaya ilk ilaç dozu, duvardaki 12 saatlik kadranlı saat aşağıda gösterilen konumdayken veriliyor. Sonraki dozlar her 7 saatte bir veriliyor; saat ilk dozdan sonra hiç durmamış ve doğru çalışmıştır. Kalın ve kısa çubuk akrebi, uzun ve ince çubuk yelkovanı göstermektedir.\nBuna göre 10. doz verildiği anda akrep kadranda kaç rakamını göstermektedir?',
 dogru=sn,yan=[(e3[0],'Doz sayısı olan 10’u aralık sayısı almış: 8 + 7 × 10 = 78 ve 78 = 6 × 12 + 6 olduğundan 6.','dikkat'),(e3[1],'Yalnız kalanı yazmış (63 = 5 × 12 + 3); başlangıç saatini eklememiş.','dikkat'),(e3[2],'Süreyi başlangıçtan ileri değil geri saymış: 8 − 3 = 5.','dikkat'),(e3[3],'Aralık sayısını 10 alıp başlangıcı eklememiş: 70’in 12’ye bölümünden kalan 10.','dikkat')],
 istenen='10. dozdaki akrebin gösterdiği rakam.',
 ip=['İlk dozdan 10. doza kadar kaç aralık geçtiğini bul; geçen toplam süreyi 12 saatlik kadrana göre değerlendir.'],
 bilgi=[SAAT],
 ad=[A('Başlangıcı oku','Akrep 8’i göstermektedir.','başlangıç: 8'),A('Aralık sayısı','10. doza kadar 9 aralık geçer.','9 × 7 = 63 saat'),A('12’ye böl','Kadran 12 saatte bir yinelenir.','63 = 5 × 12 + 3 → kalan 3'),A('Başlangıca ekle','Akrep 8’den 3 rakam ileri gider.','8 + 3 = 11')],
 puf='n. dozda geçen aralık sayısı n − 1’dir; 12 saatlik kadranda yalnız toplam sürenin 12’ye bölümünden kalan önemlidir.')

# =============== 04 · sıcaklık sütun grafiği · kolay ===============
gunler=['Pzt','Sal','Çar','Per','Cum','Cmt','Paz']; T4=[-4,-7,3,-2,5,-6,2]
neg=sum(t for t in T4 if t<0); pos=sum(t for t in T4 if t>0); assert neg==-19 and pos==10
d4=pos-neg; assert d4==29
e4=[abs(neg)-pos,neg+pos,neg-pos,abs(neg)]; assert e4==[9,-9,-29,19] and len({d4,*e4})==5
sx=.72; sy=.3
o=[]
for t in range(-8,7):
    o.append(ln(0,t*sy,7*sx+.2,t*sy,'black!15,line width=.4pt'))
o.append(ln(0,-8*sy,0,6*sy+.15,'line width=1pt')); o.append(ln(0,0,7*sx+.2,0,'line width=1.2pt'))
for t in range(-8,7,2): o.append(tx(-.28,t*sy,f'\\footnotesize ${t}$'.replace('$-','$-')))
for i,(g_,v) in enumerate(zip(gunler,T4)):
    x=.15+i*sx
    o.append(f'\\fill[vurgu!55] ({x:.3f},0) rectangle ({x+.42:.3f},{v*sy:.3f});' if v>0 else f'\\fill[black!45] ({x:.3f},0) rectangle ({x+.42:.3f},{v*sy:.3f});')
    o.append(tx(x+.21,-8*sy-.25,f'\\footnotesize {g_}'))
o.append(tx(-.1,6*sy+.45,'\\footnotesize °C'))
SK4=tz('\n'.join(o))
q('0004',tipId='tkb-sicaklik',tip='Sütun grafiğinde negatif ve pozitif değerler',z='kolay',alt='Tam Sayılarla İşlemler',kaz='Sütun grafiğinden negatif ve pozitif sıcaklıkları okuyup tam sayı işlemleriyle toplamlar arasındaki farkı bulur.',kalip='grafik',sekil=SK4,
 kart='K-TKB-04 (sıcaklık sütun grafiği) · negatif toplam −19, pozitif toplam 10',
 metin='Bir dağ evinin bahçesindeki termometre, bir hafta boyunca her sabah 07.00’de okunmuş ve okunan sıcaklıklar (°C) yukarıdaki grafikte gösterilmiştir. Grafikte 0 °C’nin altındaki değerler sıfır çizgisinin altına doğru çizilmiştir.\nBuna göre sıcaklığı 0 °C’nin altında olan günlerde okunan sıcaklıkların toplamı, sıcaklığı 0 °C’nin üstünde olan günlerde okunan sıcaklıkların toplamından kaç derece daha azdır?',
 dogru=d4,yan=[(9,'Negatif toplamın işaretini yok sayıp (19) pozitif toplamdan (10) çıkarmış: 19 − 10.','dikkat'),(-9,'İki toplamı işaretleriyle toplamış: −19 + 10 = −9.','islem'),(-29,'Soruyu fark yerine “negatif toplam eksi pozitif toplam” diye okumuş: −19 − 10 = −29.','islem'),(19,'Yalnız negatif günlerin toplamının mutlak değerini yazmış; pozitif günleri hesaba katmamış.','dikkat')],
 istenen='Negatif sıcaklıkların toplamının pozitif sıcaklıkların toplamından kaç derece az olduğu.',
 ip=['Her sütunun değerini işaretiyle oku; negatif ve pozitif sıcaklıkları ayrı ayrı topla.'],
 bilgi=[TAM],
 ad=[A('Değerleri oku','Sıfırın altına inen sütunlar negatiftir.','−4, −7, 3, −2, 5, −6, 2'),A('Negatifleri topla','0 °C’nin altındaki günler toplanır.','−4 − 7 − 2 − 6 = −19'),A('Pozitifleri topla','0 °C’nin üstündeki günler toplanır.','3 + 5 + 2 = 10'),A('Farkı bul','“Kaç derece az” ifadesi büyük olandan küçük olanı çıkarmaktır.','10 − (−19) = 29')],
 puf='“Ne kadar az” sorularında büyük değerden küçük değer çıkarılır; negatif sayıyı çıkarırken işaret + olur.')

# =============== 05 · kibrit çöpü örüntüsü · orta ===============
def kib(n): return 5*n+2
assert [kib(n) for n in (1,2,3)]==[7,12,17]
S=150; d5=max(n for n in range(1,100) if kib(n)<=S); assert d5==29 and kib(29)==147 and kib(30)==152
e5=[S//5,(S-17)//5,S//7,(S-2*5)//5]; assert e5==[30,26,21,28] and len({d5,*e5})==5
# çizim: 2 × n kare, çöp sayısı doğrulanır
def kibrit(ox,n,u=.5):
    ls=[]; cnt=0
    for r in range(3):
        for j in range(n): ls.append(ln(ox+j*u,-r*u,ox+(j+1)*u,-r*u,'line width=1.6pt')); cnt+=1
    for j in range(n+1):
        for r in range(2): ls.append(ln(ox+j*u,-r*u,ox+j*u,-(r+1)*u,'line width=1.6pt')); cnt+=1
    assert cnt==kib(n); return ls
o=[]; ox=0
for n in (1,2,3):
    o+=kibrit(ox,n); o.append(tx(ox+n*.25,-1.5,f'\\footnotesize {n}. şekil')); ox+=n*.5+.9
SK5=tz('\n'.join(o))
q('0005',tipId='tkb-kibrit',tip='Çöp sayısından genel terimle şekil bulma',z='orta',alt='Örüntü ve Döngü',kaz='Şekillerdeki çöp sayısından genel terimi yazıp verilen çöp sayısıyla yapılabilecek en büyük şekli bulur.',kalip='hikâyeli',sekil=SK5,
 kart='K-TKB-05 (kibrit çöpü örüntüsü) · 5n + 2, 150 çöpten en büyük şekil',
 metin='Bir maket atölyesinde çalışan Deniz, kibrit çöplerini kullanarak iki sıra hâlinde yan yana kareler dizmektedir. İlk üç şekil yukarıda gösterilmiştir. Deniz bu örüntüyü aynı kuralla sürdürerek her seferinde yalnız bir şekil yapacaktır. Elinde tam 150 çöp vardır ve bu çöpleri kırmadan kullanabilmektedir.\nBuna göre Deniz, bu çöplerle en fazla kaçıncı şekli yapabilir?',
 dogru=d5,yan=[(30,'Çöp sayısını 5’e bölüp (150 ÷ 5 = 30) şekle başlangıçtaki 2 çöpü hiç eklemeden karar vermiş.','dikkat'),(26,'3. şekilden sonra eklenebilecek şekil sayısını (17 + 5k ≤ 150 ⇒ k = 26) bulmuş, ilk üç şekli saymayı unutmuş.','dikkat'),(21,'Her şekle 7 çöp gerektiğini sanıp 150’yi 7’ye bölmüş: 150 ÷ 7 ≈ 21.','dikkat'),(28,'5n + 2 ≤ 150 yerine 5(n + 2) ≤ 150 yazmış: n + 2 ≤ 30 ⇒ n = 28.','islem')],
 istenen='En büyük şeklin sırası.',
 ip=['İlk üç şekildeki çöp sayılarını yaz; şekilden şekle ne kadar arttığını ve n. şekil için çöp sayısını bul.'],
 bilgi=[ORU],
 ad=[A('Çöp sayılarını say','Şekillerdeki çöpler tek tek sayılır.','7, 12, 17'),A('Artışı bul','Her yeni şekilde bir sütun (5 çöp) eklenir.','12 − 7 = 5'),A('n. şekil için yaz','İlk şekilden n − 1 artış yapılır.','7 + 5(n − 1) = 5n + 2'),A('Sınırla','Çöp sayısı 150’yi aşmamalıdır.','5n + 2 ≤ 150 → n ≤ 29,6 → n = 29')],
 puf='Sabit artışlı örüntüde n. terim = ilk terim + (n − 1) × artış; verilen sayıyı aşmayan en büyük n’yi alırken sonucu taşma açısından denetle.')

# =============== 06 · basamaklı blok · yeni nesil ===============
def Bn(n): return n*(n+1)//2
assert [Bn(n) for n in (1,2,3,4)]==[1,3,6,10]
d6=Bn(15)-Bn(11); assert d6==54==sum(range(12,16))
e6=[Bn(15)-Bn(12),sum(range(11,16)),15*16-11*12,15**2-11**2]; assert e6==[42,65,108,104] and len({d6,*e6})==5
o=[]; ox=0; u=.38
for n in (1,2,3,4):
    for k in range(1,n+1):
        for h in range(k): o.append(f'\\draw[fill=vurgu!18] ({ox+(k-1)*u:.3f},{h*u:.3f}) rectangle ({ox+k*u:.3f},{(h+1)*u:.3f});')
    o.append(tx(ox+n*u/2,-.35,f'\\footnotesize {n}. şekil')); ox+=n*u+.7
SK6=tz('\n'.join(o))
q('0006',tipId='tkb-blok',tip='Basamaklı blok dizilimi ve tanımlı gösterim',z='orta',alt='Örüntü ve Döngü',kaz='Basamaklı blok şekillerinden blok sayısı kuralını çıkarıp tanımlı gösterimle iki şeklin blok sayısı farkını bulur.',kalip='yeni nesil',sekil=SK6,
 kart='K-TKB-06 (basamaklı blok) · B(15) − B(11)',
 metin='Yukarıdaki şekillerde, aynı boyutlu küp bloklardan oluşturulmuş basamaklı yapılar verilmiştir. Bir yapıda kullanılan toplam blok sayısı, yapının şekil numarası n olmak üzere B(n) ile gösterilmektedir. Şekiller aynı kuralla sonsuza kadar sürdürülmektedir.\nBuna göre B(15) − B(11) farkı kaçtır?',
 dogru=d6,yan=[(42,'11. şeklin yerine 12. şeklin blok sayısını çıkarmış: B(15) − B(12) = 120 − 78 = 42.','dikkat'),(65,'Fark yerine 11’den 15’e kadar basamaklardaki blokları saymış: 11 + 12 + 13 + 14 + 15 = 65.','dikkat'),(108,'Yarım çarpımı unutmuş: B(n) yerine n(n + 1) almış: 240 − 132 = 108.','islem'),(104,'Şekillerden B(n) = n² sonucunu çıkarmış (1, 3, 6, 10 yerine 1, 4, 9 sanarak): 225 − 121 = 104.','dikkat')],
 istenen='B(15) − B(11) değeri.',
 ip=['İlk dört şekildeki blok sayılarını yazıp her yeni şekilde kaç blok eklendiğine bak.'],
 bilgi=[TOP],
 ad=[A('Blok sayılarını say','Şekillerdeki bloklar sayılır.','B(1) = 1, B(2) = 3, B(3) = 6, B(4) = 10'),A('Kuralı bul','Her yeni şekilde en sağa, şekil numarası kadar yüksek yeni bir basamak eklenir.','B(n) = 1 + 2 + … + n = n(n + 1)/2'),A('Değerleri hesapla','n = 15 ve n = 11 için yerine koyulur.','B(15) = 120 ve B(11) = 66'),A('Farkı al','İki değerin farkı hesaplanır.','120 − 66 = 54')],
 puf='Basamaklı yapılarda blok sayısı 1 + 2 + … + n toplamıdır; iki B değerinin farkı arada kalan basamakların toplamıdır.')

# =============== 07 · bahçe planı kesir · orta ===============
from fractions import Fraction as Fr
dom=Fr(2,5); kal=1-dom; sal=kal*Fr(1,3); bib=kal-sal; assert bib==Fr(2,5)
BIB=72; d7=BIB/bib; assert d7==180
e7=[BIB/(1-dom-Fr(1,3)),BIB/kal,BIB/(1-sal),BIB*5]
assert e7==[270,120,90,360] and len({d7,*e7})==5
o=[ '\\draw[line width=1.2pt] (0,0) rectangle (6.4,3.6);',ln(2.4,0,2.4,3.6,'line width=1pt'),ln(2.4,2.4,6.4,2.4,'line width=1pt'),
 tx(1.2,2.0,'\\textbf{Domates}'),tx(1.2,1.5,'\\footnotesize bahçenin $\\frac{2}{5}$’i'),
 tx(4.4,3.15,'\\textbf{Salatalık}'),tx(4.4,2.75,'\\footnotesize kalanın $\\frac{1}{3}$’ü'),
 tx(4.4,1.4,'\\textbf{Biber}'),tx(4.4,.95,'\\footnotesize 72 m$^2$')]
SK7=tz('\n'.join(o))
q('0007',tipId='tkb-bahce',tip='Parçalı bahçe planında kesirle bütünü bulma',z='orta',alt='Kesirler ve Rasyonel Sayılar',kaz='Planda verilen kesirlerden bütüne oranı hesaplayıp bir bölümün alanından bahçenin tamamının alanını bulur.',kalip='hikâyeli',sekil=SK7,
 kart='K-TKB-07 (bahçe planı) · domates 2/5, salatalık kalanın 1/3’ü, biber 72 m²',
 metin='Bir köy evinin dikdörtgen biçimindeki bahçesi, yukarıdaki plana göre üç bölüme ayrılarak sebze ekilmiştir. Planda “kalan”, domates bölümü ayrıldıktan sonra geriye kalan alanı göstermektedir ve plan ölçekli değildir. Bahçenin başka hiçbir bölümü yoktur.\nBuna göre bu bahçenin tamamının alanı kaç metrekaredir?',
 dogru=int(d7),yan=[(270,'Salatalığın payını bahçenin 1/3’ü sanmış: biber 1 − 2/5 − 1/3 = 4/15, 72 ÷ 4/15 = 270.','dikkat'),(120,'Biber bölümünü kalan alanın tamamı (3/5) sanmış, salatalığı hesaba katmamış: 72 ÷ 3/5 = 120.','dikkat'),(90,'Domatesi hesaba katmamış: biber 1 − 1/5 = 4/5 sanılmış, 72 ÷ 4/5 = 90.','dikkat'),(360,'Biberi bahçenin 1/5’i sanmış (kalanın 1/3’ünü biber sanmış): 72 × 5 = 360.','dikkat')],
 istenen='Bahçenin tamamının alanı (m²).',
 ip=['Her bölümün, bahçenin tamamının kaçta kaçı olduğunu bul; kalan kısmın kesri başka bir bütünün kesridir.'],
 bilgi=[KES],
 ad=[A('Kalanı bul','Domates bahçenin 2/5’i olduğundan kalan 3/5’tir.','1 − 2/5 = 3/5'),A('Salatalığı bul','Salatalık kalanın 1/3’üdür.','3/5 × 1/3 = 1/5'),A('Biberi bul','Biber, kalandan salatalık çıkınca kalan bölümdür.','3/5 − 1/5 = 2/5'),A('Bütüne ulaş','Biberin alanı 72 m² ve bahçenin 2/5’idir.','72 ÷ 2/5 = 180')],
 puf='“Kalanın kesri”ni bütünün kesrine çevirmek için kalanın kesriyle çarp; biber bölümü de kalandan salatalık çıkarılarak bulunur.')

# =============== 08 · koordinat düzleminde işaret · öncüllü ===============
import random
def deger(sg): return range(1,6) if sg>0 else range(-5,0)
M8=(-1,1); N8=(1,-1); P8=(-1,-1)      # (a,b)∈II, (c,d)∈IV, (e,f)∈III
def dogrulari(f):
    return all(f(a,b,c,d,e,ff) for a in deger(-1) for b in deger(1) for c in deger(1) for d in deger(-1) for e in deger(-1) for ff in deger(-1))
def hep_yanlis(f):
    return all(not f(a,b,c,d,e,ff) for a in deger(-1) for b in deger(1) for c in deger(1) for d in deger(-1) for e in deger(-1) for ff in deger(-1))
ON8=[lambda a,b,c,d,e,f:a*c*e<0,lambda a,b,c,d,e,f:b*d*f<0,lambda a,b,c,d,e,f:(a+e)*(d-b)>0]
assert hep_yanlis(ON8[0]) and hep_yanlis(ON8[1]) and dogrulari(ON8[2])
SIRA8=['Yalnız I','Yalnız III','I ve II','I ve III','II ve III']
o=[ln(-2.8,0,2.8,0,'-{Stealth[length=2mm]}'),ln(0,-2.6,0,2.6,'-{Stealth[length=2mm]}'),tx(2.95,0,'$x$'),tx(0,2.8,'$y$'),tx(-.2,-.2,'$O$')]
pts={'M':(-1.7,1.5,'$(a,\\ b)$','above left'),'N':(1.6,-1.2,'$(c,\\ d)$','below right'),'P':(-1.9,-1.7,'$(e,\\ f)$','below left')}
for k,(x,y,lab,pos) in pts.items():
    o.append(f'\\fill ({x},{y}) circle (.07); \\node[{pos}=1pt] at ({x},{y}) {{\\small {k}{lab}}};')
SK8=tz('\n'.join(o))
q('0008',tipId='tkb-koordinat',tip='Koordinat bölgelerinden işaret çıkarma',z='orta',alt='İşaret İnceleme',kaz='Noktaların bulunduğu bölgelerden koordinatların işaretlerini bulup çarpım ve toplam içeren öncülleri değerlendirir.',kalip='öncüllü',sekil=SK8,
 kart='K-TKB-08 (koordinat işareti) · M II., N IV., P III. bölgede',
 metin='Bir bilgisayar oyununda M, N ve P noktalarının ekrandaki yerleri, koordinat düzlemi üzerinde yukarıda gösterilmiştir. Şekil ölçekli değildir; noktaların koordinatları (a, b), (c, d) ve (e, f) gerçek sayı ikilileridir.\nBuna göre,\nI. a · c · e < 0\nII. b · d · f < 0\nIII. (a + e) · (d − b) > 0\nifadelerinden hangileri her zaman doğrudur?',
 dogru='Yalnız III',sira=SIRA8,yan=[('Yalnız I','Çarpımın işaretini yalnız ilk iki çarpana bakarak belirlemiş: a · c negatiftir, diye I’i doğru bulmuş; e’yi hesaba katmamış. III’ü ise d − b farkını pozitif sanarak yanlış bulmuş.','dikkat'),('I ve II','Çarpımların işaretini yalnız ilk iki çarpana bakarak belirlemiş: a · c ve b · d negatif olduğundan I ve II’yi doğru bulmuş; üçüncü çarpanı (e ve f) hesaba katmamış. III’ü yanlış sanmış.','dikkat'),('I ve III','I’de yalnız a · c çarpımına bakıp negatif bulmuş, e’yi (negatif) hesaba katmamış; III’ü doğru bulmuş.','dikkat'),('II ve III','II’de yalnız b · d çarpımına bakıp negatif bulmuş, f’yi (negatif) hesaba katmamış; III’ü doğru bulmuş.','dikkat')],
 istenen='Her zaman doğru olan öncüller.',
 ip=['Her noktanın bulunduğu bölgeden koordinatların işaretlerini yaz; öncüllerdeki her çarpanı sırayla hesaba kat.'],
 bilgi=[ISARET],
 ad=[A('İşaretleri oku','M II., N IV., P III. bölgededir.','a < 0, b > 0 · c > 0, d < 0 · e < 0, f < 0'),A('I’i denetle','a, c ve e’nin işaretleri çarpılır.','(−)(+)(−) = + → I yanlış'),A('II’yi denetle','b, d ve f’nin işaretleri çarpılır.','(+)(−)(−) = + → II yanlış'),A('III’ü denetle','a + e negatif, d − b negatiftir.','(−)(−) = + → III doğru')],
 puf='Bir noktanın bölgesi koordinatlarının işaretlerini verir; çarpımın işareti negatif çarpan sayısının tek ya da çift olmasına bakar.')

# =============== 09 · bina kat planı · kolay ===============
KATLAR={-2:'Otopark',-1:'Market',0:'Lobi',1:'Banka',2:'Kuaför',3:'Kafe',4:'Kütüphane',5:'Ofis'}
rota=['Otopark','Kafe','Market','Ofis','Lobi']; no={v:k for k,v in KATLAR.items()}
fk=[no[a] for a in rota]; assert fk==[-2,3,-1,5,0]
d9=sum(abs(fk[i+1]-fk[i]) for i in range(4)); assert d9==20
e9=[sum(abs(abs(fk[i+1])-abs(fk[i])) for i in range(4)),abs(fk[-1]-fk[0]),d9+4,d9+abs(fk[-1]-fk[-2])]
assert e9==[12,2,24,25] and len({d9,*e9})==5
o=['\\draw[line width=1.2pt] (0,-2.5) rectangle (3.2,5.5);']
for k,ad_ in KATLAR.items():
    o.append(ln(0,k-.5,3.2,k-.5,'line width=.6pt')); o.append(tx(1.6,k,ad_)); o.append(tx(-.5,k,f'\\footnotesize ${k}$'))
o.append(ln(0,-.5,3.2,-.5,'line width=1.6pt'))
o.append(tx(-.5,5.9,'\\footnotesize Kat'))
SK9=tz('\n'.join(o))
q('0009',tipId='tkb-kat',tip='Kat planında toplam yer değiştirme',z='kolay',alt='Tam Sayılarla İşlemler',kaz='Kat planından kat numaralarını okuyup asansörün ardışık durakları arasındaki yer değiştirmeyi mutlak farklarla toplar.',kalip='hikâyeli',sekil=SK9,
 kart='K-TKB-09 (bina kat planı) · −2 → 3 → −1 → 5 → 0',
 metin='Selin, yukarıdaki kat planı verilen iş merkezinde asansörle önce otoparktan kafeye, oradan markete, sonra ofise ve son olarak lobiye gidiyor. Asansör her durakta durmuş, Selin gittiği yerden başka bir yere uğramamıştır; asansör katları yalnızca arka arkaya geçerek ilerlemektedir.\nBuna göre asansör toplam kaç kat yer değiştirmiştir?',
 dogru=d9,yan=[(12,'Kat numaralarının işaretlerini yok sayıp (2, 3, 1, 5, 0) farkları almış: 1 + 2 + 4 + 5 = 12.','dikkat'),(2,'Yalnız ilk ve son durağı hesaba katmış: |0 − (−2)| = 2.','dikkat'),(24,'Her gidişte başlangıç ve varış katlarının ikisini de sayıp 4 gidiş için 4 fazla yazmış: 20 + 4 = 24.','dikkat'),(25,'Son gidişi iki kez saymış: 20 + 5 = 25.','dikkat')],
 istenen='Asansörün toplam yer değiştirmesi (kat).',
 ip=['Her durağın kat numarasını plandan oku; ardışık iki durak arasındaki farkı işaretlerine dikkat ederek bul.'],
 bilgi=[KAT],
 ad=[A('Kat numaralarını oku','Duraklar plandaki numaralarla yazılır.','−2, 3, −1, 5, 0'),A('Farkları al','Her gidişte mutlak fark alınır.','|3 − (−2)| = 5 · |−1 − 3| = 4 · |5 − (−1)| = 6 · |0 − 5| = 5'),A('Topla','Dört gidişin farkları toplanır.','5 + 4 + 6 + 5 = 20')],
 puf='Yön değiştiren harekette net yer değiştirme değil, her etapta alınan yolların mutlak değerleri toplanır.')

# =============== 10 · lamba paneli · zor ===============
ilk=[1,0,0,0,0,0,0,0,1,1,1,1]  # 1 = yanık
def tur(d,k):
    d=d[:]
    for i in range(1,13):
        if i%k==0: d[i-1]^=1
    return d
def kos(d,ks):
    for k in ks: d=tur(d,k)
    return d
d10=sum(kos(ilk,(2,3,4))); assert d10==4 and kos(ilk,(2,3,4))==[1,1,1,0,0,0,0,0,0,0,1,0]
on=ilk[:]
for k in (2,3,4):
    for i in range(1,13):
        if i%k==0: on[i-1]=1
e10=[sum(kos(ilk,(2,4))),sum(kos(ilk,(2,3))),sum(kos([1-x for x in ilk],(2,3,4))),sum(on)]
assert e10==[6,7,8,10] and len({d10,*e10})==5
o=[]
for i in range(12):
    x=i*.62
    o.append(f'\\draw[line width=1.1pt,fill={"vurgu!55" if ilk[i] else "white"}] ({x:.2f},0) circle (.24);')
    o.append(tx(x,-.55,f'\\footnotesize {i+1}'))
SK10=tz('\n'.join(o))
q('0010',tipId='tkb-lamba',tip='Lambalara basma turlarında yanan lamba sayısı',z='zor',alt='Tek ve Çift Sayılar',kaz='Lambaların düğmelerine yapılan basma turlarında her lambaya kaç kez basıldığını katlarla belirleyip yanan lamba sayısını bulur.',kalip='hikâyeli',sekil=SK10,
 kart='K-TKB-10 (lamba paneli) · 12 lamba, 2, 3 ve 4’ün katlarına basma',
 metin='Bir tiyatro sahnesinde 1’den 12’ye kadar numaralanmış 12 lambanın ilk durumu yukarıda gösterilmiştir; boyalı lambalar yanıktır. Her lambanın kendi düğmesi vardır ve düğmeye basılınca lamba yanıksa söner, sönükse yanar. Görevli sırayla üç tur yapıyor: 1. turda numarası 2’nin katı olan lambaların, 2. turda 3’ün katı olan lambaların, 3. turda 4’ün katı olan lambaların düğmesine birer kez basıyor.\nBuna göre üç tur bittiğinde kaç lamba yanıktır?',
 dogru=d10,yan=[(6,'2. turu (3’ün katları) atlamış: yalnız 2’nin ve 4’ün katlarına basmış.','dikkat'),(7,'Yalnız ilk iki turu uygulamış, 4’ün katlarına basmayı unutmuş.','dikkat'),(8,'Başlangıç durumunu ters okumuş (yanık lambaları sönük, sönükleri yanık sanmış).','dikkat'),(10,'Düğmeye basılan her lambayı yakmış (sönükse yanar kuralını yanıksa da uygulamış), söndürmemiş.','islem')],
 istenen='Üç tur sonunda yanan lamba sayısı.',
 ip=['Her lambaya üç turda kaç kez basıldığını numarasının bölenlerine bakarak bul; çift sayıda basılan lambanın durumu değişmez.'],
 bilgi=[TEK],
 ad=[A('Başlangıcı oku','Yanan lambalar 1, 9, 10, 11 ve 12 numaralıdır.','yanık: 1, 9, 10, 11, 12'),A('Basma sayısını bul','Her lamba için numarasının 2, 3 ve 4’ün kaçının katı olduğuna bakılır.','0 kez: 1, 5, 7, 11 · 1 kez: 2, 3, 9, 10 · 2 kez: 4, 6, 8 · 3 kez: 12'),A('Tek sayıda basılanları ayır','Yalnız tek sayıda basılan lambaların durumu değişir.','durumu değişenler: 2, 3, 9, 10, 12'),A('Durumları uygula','Sönük olan 2 ve 3 yanar; yanık olan 9, 10 ve 12 söner.','2 ve 3 yanar · 9, 10, 12 söner'),A('Yanıkları say','Son durumda 1, 2, 3 ve 11 numaralı lambalar yanıktır.','1, 2, 3, 11 → 4 lamba')],
 puf='Bir lamba için kaç düğmenin basıldığı, numarasının kaç turun katı olduğuna bağlıdır; yalnız tek sayıda basılanın durumu değişir.')

bitir(P,'tksekb','mat|Temel Kavramlar')
