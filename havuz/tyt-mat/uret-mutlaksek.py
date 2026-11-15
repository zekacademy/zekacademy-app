"""Mutlak Değer · şekilli paket (mutlaksek): 7 soru, hepsi şekilli/tablolu/grafikli. Kardeş yok, ipucu 1. Her cevap ve çeldirici değer kodla hesaplanıp assert edilir.
Şekil ölçüleri Python'da üretilir; TikZ gövdesi aynı değerlerden f-string ile yazılır (bkz. havuz/URETIM-SEKIL.md)."""
import sys,os,math
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
H.KONU='Mutlak Değer'
P=Parti('mutlaksek','Mutlak Değer','mat|Mutlak Değer')
KY='ÖSYM 2018–2026 TYT Matematik (şekilli mutlak değer, uzaklık soruları, yalnız mantık) · MEB 9. sınıf'
TP=lambda g:tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'+g+'\n\\end{tikzpicture}')
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)
def tamlar(f,lo=-700,hi=700): return [x for x in range(lo,hi+1) if f(x)]

UZ=B('Mutlak değer ve uzaklık','|x − a|, sayı doğrusunda x ile a arasındaki uzaklıktır. Örnek: |x − 3| = 2 ise x, 3’e 2 birim uzaktadır; x = 1 ya da x = 5')
ARL=B('Uzaklık eşitsizlikleri','|x − a| ≤ r ise a − r ≤ x ≤ a + r; |x − a| ≥ r ise x ≤ a − r ya da x ≥ a + r. Örnek: |x − 4| ≤ 1 ise 3 ≤ x ≤ 5')
YAK=B('Hangi noktaya daha yakın','x, A’ya B’den daha yakınsa |x − a| < |x − b| olur; bu x değerleri iki noktanın orta noktasının A tarafındadır. Örnek: A = 0, B = 6 için orta nokta 3 olup x < 3 olan sayılar A’ya daha yakındır')
KAT=B('Kat farkı','iki kat arasındaki geçiş sayısı, kat numaraları farkının mutlak değeridir. Örnek: 5. kattan −1. kata |5 − (−1)| = 6 kat inilir')
TOL=B('Tolerans','“m ± d” etiketi, kütle x için |x − m| ≤ d demektir; yani m − d ≤ x ≤ m + d (uçlar dahil). Örnek: 80 g ± 5 g etiketli paketin kütlesi 75 g ile 85 g arasındadır')
SAYI=B('Ardışık tam sayıların sayısı','a ile b arasındaki (uçlar dahil) tam sayıların sayısı b − a + 1’dir. Örnek: 4’ten 9’a kadar 9 − 4 + 1 = 6 tam sayı vardır')
GRF=B('|x − a| + b grafiği','y = |x − a| + b grafiği, tepe noktası (a, b) olan ve kolları 1 eğimli V biçimli bir grafiktir. Örnek: y = |x − 1| + 2 grafiğinin tepe noktası (1, 2)’dir')

kart('K-MTS-01','Sayı doğrusunda uzaklık','Noktaların yerleri şekilden okunur; verilen uzaklığı sağlayan her nokta bulunup diğer noktaya uzaklıkları ayrı ayrı hesaplanır.','Yalnız tek noktayı bulmak; verilen uzaklığı toplam sanmak; iki noktanın uzaklığını yazmak.','kolay','şekilli',3,'mts-uzaklik','Sayı doğrusunda uzaklık',KY)
kart('K-MTS-02','Yol üzerinde konum koşulları','Her uzaklık koşulu bir aralık verir; aralıkların kesişimindeki tam sayılar sayılır.','Uçları yanlış dahil etmek; bir koşulu unutmak; iki yönlü çözümü tek yön almak.','orta','şekilli',4,'mts-yol','Yol üzerinde uzaklık koşulları',KY)
kart('K-MTS-03','Tolerans etiketi','Etiketteki “m ± d” bir mutlak değer eşitsizliğidir; iki toleransın ortak aralığındaki tam sayılar sayılır.','Uçları dahil saymamak; birleşim almak; tek aralığın tam sayısını yazmak.','orta','şekilli',4,'mts-tolerans','Tolerans etiketi ve ortak aralık',KY)
kart('K-MTS-04','Asansör kat şeması','Kat farkları mutlak değer ile alınır; bodrum katlar negatif sayıdır; durakların farklarının mutlak değerleri toplanır.','Bodrumu pozitif saymak; işaretli farkları toplamak; bir durağı atlamak; durak sayısını kat sayısına eklemek.','kolay','şekilli',3,'mts-kat','Asansör kat şeması',KY)
kart('K-MTS-05','Sıcaklık tablosu','Tablodaki her değer için mutlak değer koşulu ayrı sınanıp koşulu sağlayan günler sayılır.','Sınır değeri dahil saymak; işareti ters kullanmak; eşitsizlik yönünü ters çevirmek.','orta','tablo',3,'mts-sicaklik','Tabloda mutlak değer koşulu',KY)
kart('K-MTS-06','İşaretli noktalarla |x − a| yorumu','Yakınlık koşulu orta noktaya, uzaklık koşulları aralıklara çevrilir; tam sayı değerleri sayılır.','Orta noktada eşitliği dahil etmek; yakınlık yönünü ters okumak; bir koşulu unutmak.','zor','şekilli',5,'mts-yakin','Sayı doğrusunda yakınlık ve uzaklık',KY)
kart('K-MTS-07','|x − a| + b grafiği','Grafikten tepe noktası okunur; doğruyla kesim noktaları mutlak değer denkleminden bulunur; üçgenin alanı hesaplanır.','Alan için yarıyı unutmak; yüksekliği eksenden almak; tepe noktasını yanlış okumak.','zor','grafik',4,'mts-grafik','Mutlak değer grafiği ve alan',KY)

# ---------- 01 · kolay · sayı doğrusunda uzaklık ----------
A1,B1,r1=-2,6,5; xs=[A1-r1,A1+r1]; ut=[abs(x-B1) for x in xs]
assert xs==[-7,3] and ut==[13,3] and sum(ut)==16 and abs(A1-B1)==8
s=.45; g=f'\\draw[-{{Stealth}}] ({-8.7*s:.2f},0) -- ({9.8*s:.2f},0);'
for i in range(-8,10): g+=f'\\draw ({i*s:.2f},-.08) -- ({i*s:.2f},.08);'+(f'\\node[below=3pt,font=\\footnotesize] at ({i*s:.2f},0) {{${i}$}};' if i%2==0 else '')
for nm,v in (('A',A1),('B',B1)): g+=f'\\fill[vurgu] ({v*s:.2f},0) circle (.1);\\node[above=5pt] at ({v*s:.2f},0) {{{nm}}};'
q('0001',tipId='mts-uzaklik',tip='Sayı doğrusunda uzaklık',z='kolay',alt='Mutlak Değer ve Uzaklık',kaz='Sayı doğrusunda bir noktaya verilen uzaklıktaki noktaları bulup diğer noktaya uzaklıklarını toplar.',kalip='şekilli',sekil=TP(g),
 kart='K-MTS-01 (uzaklık) · A = −2, B = 6, |x − A| = 5 için |x − B| toplamı',
 metin='Şekildeki sayı doğrusunda A ve B noktalarının yerleri gösterilmiştir.\nSayı doğrusu üzerinde A noktasına uzaklığı 5 birim olan noktaların her birinin B noktasına uzaklıkları toplamı kaçtır?',
 dogru=16,yan=[(3,'A’nın sağındaki noktayı (3) bulup yalnız onun B’ye uzaklığını (3) yazmış; A’nın solundaki nokta da vardır.','dikkat'),(8,'Sorulan toplam yerine A ile B arasındaki uzaklığı (8) yazmış.','dikkat'),(10,'Verilen uzaklığı (5) iki noktada toplamış: 5 + 5 = 10; B’ye uzaklıkları hesaplamamış.','dikkat'),(13,'A’nın solundaki noktayı (−7) bulup yalnız onun B’ye uzaklığını (13) yazmış.','dikkat')],
 istenen='A’ya 5 birim uzaktaki noktaların B’ye uzaklıkları toplamı.',
 ip=['A’ya 5 birim uzaklıktaki noktalar A’nın hem sağında hem solundadır; önce bu noktaların yerini bul.'],
 bilgi=[UZ],
 ad=[A('Noktaları oku','A = −2, B = 6.','A = −2 · B = 6'),A('A’ya 5 uzaktaki noktalar','İki yönde 5 birim gidilir.','−2 − 5 = −7 ve −2 + 5 = 3'),A('B’ye uzaklıklar','Her noktanın B’ye uzaklığı farkın mutlak değeridir; ikisi toplanır.','|−7 − 6| + |3 − 6| = 13 + 3 = 16')],
 puf='“Uzaklığı r olan noktalar” her zaman iki tanedir (sağında ve solunda); ikisini de bulmadan toplama geçme.')

# ---------- 02 · orta · yol üzerinde konum koşulları ----------
K_,L_,M_=2,9,17
f=lambda x:abs(x-L_)<=6 and abs(x-K_)>=5 and abs(x-M_)>=4
xs=tamlar(f,0,40); assert xs==list(range(7,14)) and len(xs)==7
assert len(tamlar(lambda x:abs(x-L_)<=6 and abs(x-K_)>5 and abs(x-M_)>4,0,40))==5
assert len(tamlar(lambda x:abs(x-L_)<=6 and abs(x-K_)>5 and abs(x-M_)>=4,0,40))==6
assert len(tamlar(lambda x:abs(x-L_)<=6,0,40))==13 and len(tamlar(lambda x:abs(x-L_)<=6 and abs(x-K_)>=5,0,40))==9
s=.3; g=f'\\draw[line width=2pt] (0,0) -- ({24*s:.2f},0);\\node[anchor=east] at (-.15,0) {{$0$ km}};'
for i in range(0,25): g+=f'\\draw ({i*s:.2f},-.07) -- ({i*s:.2f},.07);'
for nm,v in (('Okul',K_),('Hastane',L_),('Park',M_)):
    g+=f'\\draw[thick,fill=vurgu!30] ({v*s-.12:.2f},-.12) rectangle ({v*s+.12:.2f},.12);\\node[above=6pt,font=\\large] at ({v*s:.2f},0) {{{nm}}};\\node[below=6pt,font=\\normalsize] at ({v*s:.2f},0) {{{v}. km}};'
q('0002',tipId='mts-yol',tip='Yol üzerinde uzaklık koşulları',z='orta',alt='Mutlak Değer ve Uzaklık',kaz='Yol üzerindeki üç noktaya verilen uzaklık koşullarını aralığa çevirip kesişimdeki tam sayı konumları sayar.',kalip='şekilli',sekil=TP(g),
 kart='K-MTS-02 (yol üzerinde konum) · Okul 2, Hastane 9, Park 17; |x − 9| ≤ 6, |x − 2| ≥ 5, |x − 17| ≥ 4',
 metin='Şekilde, doğrusal bir yol üzerinde Okul, Hastane ve Park’ın yolun başlangıcından itibaren kilometre cinsinden konumları gösterilmiştir. Yol üzerinde konumu tam sayı (km) olan bir noktaya bir benzin istasyonu yapılacaktır. İstasyon, Hastane’ye en çok 6 km, Okul’a en az 5 km ve Park’a en az 4 km uzaklıkta olacaktır.\nBuna göre istasyon kaç farklı noktaya yapılabilir?',
 dogru=7,yan=[(5,'“En az” ifadelerindeki eşitliği dışarıda bırakıp 8, 9, 10, 11, 12 noktalarını saymış.','dikkat'),(6,'Okul koşulunda eşitliği dışarıda bırakıp 8’den 13’e 6 nokta saymış; “en az 5 km” uzaklığın 5 olmasına da izin verir.','dikkat'),(9,'Park koşulunu uygulamamış: Hastane ve Okul koşullarıyla 7’den 15’e 9 nokta saymış.','dikkat'),(13,'Yalnız Hastane koşulunu uygulayıp 3’ten 15’e 13 nokta saymış.','dikkat')],
 istenen='İstasyonun yapılabileceği nokta sayısı.',
 ip=['Her uzaklık koşulunu, istasyonun konumu x için bir aralığa çevir; aralıkların ortak kısmına bak.'],
 bilgi=[ARL,SAYI],
 ad=[A('Hastane koşulu','Hastane 9. km’de; uzaklık en çok 6.','|x − 9| ≤ 6 → 3 ≤ x ≤ 15'),A('Okul koşulu','Okul 2. km’de; uzaklık en az 5. İki yönlü koşuldur; Hastane koşulu x ≥ 3 verdiğinden x ≤ −3 kolu elenir.','|x − 2| ≥ 5 → x ≤ −3 ya da x ≥ 7 → x ≥ 7'),A('Park koşulu','Park 17. km’de; uzaklık en az 4.','|x − 17| ≥ 4 → x ≤ 13'),A('Ortak aralık ve say','Üç koşulu birlikte sağlayan tam sayılar.','7 ≤ x ≤ 13 → 13 − 7 + 1 = 7')],
 puf='“En az r uzaklık” iki yönlü bir koşuldur; bir yönü başka bir koşul (burada Hastane) eler.')

# ---------- 03 · orta · tolerans etiketi ----------
m1,d1,m2,d2=500,15,490,12
S=tamlar(lambda x:abs(x-m1)<=d1 and abs(x-m2)<=d2); assert S==list(range(485,503)) and len(S)==18
assert len(tamlar(lambda x:abs(x-m2)<=d2))==25 and len(tamlar(lambda x:abs(x-m1)<=d1))==31 and len(tamlar(lambda x:abs(x-m1)<=d1 or abs(x-m2)<=d2))==38
assert len(tamlar(lambda x:abs(x-m1)<d1 and abs(x-m2)<=d2))==17
g='\\draw[thick,rounded corners=3pt] (0,0) rectangle (3.0,1.9);\\node at (1.5,1.5) {\\small Ürün paketi};\\node[align=center] at (1.5,.85) {\\bfseries Net 500 g\\\\$\\pm$ 15 g};'
g+='\\draw[thick] (4.0,0) rectangle (7.4,1.9);\\node at (5.7,1.5) {\\small İhracat standardı};\\node[align=center] at (5.7,.85) {\\bfseries 490 g\\\\$\\pm$ 12 g};'
q('0003',tipId='mts-tolerans',tip='Tolerans etiketi ve ortak aralık',z='orta',alt='Mutlak Değer Problemleri',kaz='İki tolerans etiketini mutlak değer eşitsizliği olarak yazıp ortak aralıktaki tam sayı değerlerini sayar.',kalip='şekilli',sekil=TP(g),
 kart='K-MTS-03 (tolerans etiketi) · 500 ± 15 ve 490 ± 12, ortak tam sayı gram',
 metin='Bir fabrikada üretilen paketin etiketi ile ihracat standardı şekilde verilmiştir. “m g ± d g” gösterimi, paketin kütlesinin m gramdan en çok d gram sapabileceğini belirtir (sapma sınırları dahildir). Kütlesi tam sayı gram olan bir paket, hem etiketin hem de ihracat standardının koşulunu sağlamaktadır.\nBuna göre bu paketin kütlesi kaç farklı değer alabilir?',
 dogru=18,yan=[(17,'Etiket aralığının sol ucunu dışarıda bırakıp 486’dan 502’ye 17 değer saymış; tolerans sınırları dahildir.','dikkat'),(25,'Yalnız ihracat standardının aralığındaki (478 – 502) tam sayıları saymış.','dikkat'),(31,'Yalnız etiketin aralığındaki (485 – 515) tam sayıları saymış.','dikkat'),(38,'Ortak aralık yerine iki aralığın birleşimindeki (478 – 515) tam sayıları saymış.','dikkat')],
 istenen='Paketin kütlesinin alabileceği tam sayı değerlerinin sayısı.',
 ip=['Her “m ± d” gösterimini bir mutlak değer eşitsizliğine, sonra bir aralığa çevir.'],
 bilgi=[TOL,SAYI],
 ad=[A('Etiketi yaz','500 ± 15 etiketi.','|x − 500| ≤ 15 → 485 ≤ x ≤ 515'),A('Standardı yaz','490 ± 12 standardı.','|x − 490| ≤ 12 → 478 ≤ x ≤ 502'),A('Ortak aralık','İkisini birden sağlayan değerler.','485 ≤ x ≤ 502'),A('Say','Uçlar dahil tam sayılar.','502 − 485 + 1 = 18')],
 puf='Tolerans sınırları dahil olduğundan uçlar sayıma girer: iki ucu dahil tam sayı adedi = fark + 1.')

# ---------- 04 · kolay · asansör kat şeması ----------
kat=dict(Kafeterya=4,Arşiv=-2,Ofis=7,Otopark=-3); yol=['Kafeterya','Arşiv','Ofis','Otopark']
fk=[abs(kat[yol[i+1]]-kat[yol[i]]) for i in range(3)]; assert fk==[6,9,10] and sum(fk)==25
assert abs(sum(kat[yol[i+1]]-kat[yol[i]] for i in range(3)))==7 and abs(4-2)+abs(2-7)+abs(7-3)==11 and fk[0]+fk[1]==15 and sum(fk)+3==28
h=.42; g=''
for k in range(-3,9):
    g+=f'\\draw[thick] (0,{k*h:.2f}) rectangle (1.6,{(k+1)*h:.2f});\\node[anchor=east] at (-.15,{(k+.5)*h:.2f}) {{${k}$}};'
g+=f'\\draw[line width=2pt] (-.5,0) -- (2.0,0);\\node[anchor=west,font=\\footnotesize] at (1.8,{.5*h:.2f}) {{zemin kat}};'
for nm,k in kat.items(): g+=f'\\fill[vurgu] (.8,{(k+.5)*h:.2f}) circle (.1);\\node[anchor=west] at (1.8,{(k+.5)*h:.2f}) {{{nm}}};'
q('0004',tipId='mts-kat',tip='Asansör kat şeması',z='kolay',alt='Mutlak Değer Problemleri',kaz='Bodrum katları negatif sayı olarak alıp ardışık duraklar arasındaki kat farklarının mutlak değerlerini toplar.',kalip='şekilli',sekil=TP(g),
 kart='K-MTS-04 (asansör) · Kafeterya 4, Arşiv −2, Ofis 7, Otopark −3',
 metin='Şekilde bir iş merkezinin kat şeması gösterilmiştir; bodrum katlar eksi sayılarla numaralandırılmıştır. Bir görevli asansörle sırasıyla Kafeterya’dan Arşiv’e, Arşiv’den Ofis’e ve Ofis’ten Otopark’a gitmiştir. Asansör yalnız bu duraklar arasında, kat atlayarak ve geri dönmeden hareket etmiştir.\nKomşu iki kat arası 1 kat yol sayılır.\nBuna göre görevli bu yolculukta toplam kaç kat yol almıştır?',
 dogru=25,yan=[(7,'Üç yolculuğun işaretli farklarını toplayıp (−6 + 9 − 10 = −7) mutlak değerini almış; kat sayıları her yolculukta ayrı ayrı mutlak alınıp toplanır.','islem'),(11,'Bodrum katlarını pozitif sayı gibi alıp 2 + 5 + 4 = 11 bulmuş.','dikkat'),(15,'Son yolculuğu (Ofis’ten Otopark’a) hesaba katmamış: 6 + 9 = 15.','dikkat'),(28,'Her yolculuğun ardından varış katını da bir kat sayıp 25 + 3 = 28 bulmuş.','dikkat')],
 istenen='Toplam geçilen kat sayısı.',
 ip=['Her yolculukta başlangıç ve varış katının numaralarını yaz; geçilen kat sayısı bu iki numaranın farkıyla ilgilidir.'],
 bilgi=[KAT],
 ad=[A('Katları oku','Şekilden durak katları.','Kafeterya 4 · Arşiv −2 · Ofis 7 · Otopark −3'),A('Kat farkları','Her yolculukta fark mutlak değerle alınır.','|−2 − 4| = 6 · |7 − (−2)| = 9 · |−3 − 7| = 10'),A('Topla','Üç yolculuğun kat sayıları toplanır.','6 + 9 + 10 = 25')],
 puf='Yön değişse de geçilen kat sayısı hep pozitiftir; bu yüzden işaretli farklar değil, mutlak değerleri toplanır.')

# ---------- 05 · orta · sıcaklık tablosu ----------
gun=['Pazartesi','Salı','Çarşamba','Perşembe','Cuma','Cumartesi','Pazar']; T=[-3,5,6,-1,7,-2,-1]
c=sum(abs(t-2)>4 for t in T); assert c==2 and sum(abs(t-2)>=4 for t in T)==4 and sum(abs(t+2)>4 for t in T)==3 and sum(abs(t-2)<=4 for t in T)==5 and sum(abs(t-2)>=3 for t in T)==7
ts=lambda v:('−' if v<0 else '')+str(abs(v))
sek=tablo_svg(['Gün','Sıcaklık (°C)'],[[g_,ts(t)] for g_,t in zip(gun,T)])
q('0005',tipId='mts-sicaklik',tip='Tabloda mutlak değer koşulu',z='orta',alt='Mutlak Değer Problemleri',kaz='Tablodaki sıcaklıkların 2 °C’ye uzaklığını mutlak değerle sınayıp koşulu sağlayan günleri sayar.',kalip='tablo',sekil=sek,
 kart='K-MTS-05 (sıcaklık tablosu) · |t − 2| > 4 koşulunu sağlayan gün sayısı',
 metin='Bir şehirde bir haftanın günlük sıcaklık değerleri aşağıdaki tabloda verilmiştir. Sıcaklığının 2 °C’ye uzaklığı 4 °C’den büyük olan günlere “sıra dışı gün” denmektedir.\nBuna göre bu haftada kaç gün sıra dışıdır?',
 dogru=2,yan=[(3,'İşareti ters kullanıp |t + 2| > 4 koşulunu sınamış; Salı, Çarşamba ve Cuma günlerini saymış.','islem'),(4,'“Büyük” yerine “büyük ya da eşit” alıp uzaklığı tam 4 olan Çarşamba ve Cumartesi’yi de saymış.','dikkat'),(5,'Eşitsizliğin yönünü ters çevirip uzaklığı 4’ten küçük ya da eşit olan 5 günü saymış.','dikkat'),(7,'Eşiği 4 yerine 3 okuyup uzaklığı 3’ten büyük ya da eşit olan bütün günleri (7) saymış.','dikkat')],
 istenen='Sıra dışı gün sayısı.',
 ip=['Her günün sıcaklığının, metinde verilen sıcaklığa uzaklığını hesapla ve koşulla karşılaştır.'],
 bilgi=[UZ,ARL],
 ad=[A('Uzaklıkları bul','Her sıcaklığın 2’ye uzaklığı |t − 2| ile hesaplanır.','5, 3, 4, 3, 5, 4, 3 (Pazartesi, …, Pazar)'),A('Koşulu sına','Uzaklık 4’ten büyük olmalı; 4 olanlar dahil değil.','Pazartesi (−3) ve Cuma (7): uzaklık 5 > 4'),A('Say','Koşulu yalnız Pazartesi ve Cuma sağlar.','2 gün')],
 puf='“Büyük” ile “büyük ya da eşit” arasındaki fark tam sınırdaki günlerde ortaya çıkar; sınıra denk gelen değerleri ayrıca işaretle.')

# ---------- 06 · zor · işaretli noktalarla yakınlık ----------
a6,b6,c6=-6,4,-8
f=lambda x:abs(x-a6)<abs(x-b6) and abs(x-c6)>=3 and abs(x)<=12
xs=tamlar(f); assert xs==[-12,-11,-5,-4,-3,-2] and len(xs)==6
assert len(tamlar(lambda x:abs(x-a6)<=abs(x-b6) and abs(x-c6)>=3 and abs(x)<=12))==7 and len(tamlar(lambda x:abs(x-a6)<abs(x-b6) and abs(x-c6)>3 and abs(x)<=12))==4
assert len(tamlar(lambda x:abs(x-b6)<abs(x-a6) and abs(x-c6)>=3 and abs(x)<=12))==13 and len(tamlar(lambda x:abs(x-c6)>=3 and abs(x)<=12))==20
s=.27; g=f'\\draw[-{{Stealth}}] ({-14.8*s:.2f},0) -- ({14.9*s:.2f},0);'
for i in range(-14,15): g+=f'\\draw ({i*s:.2f},-.07) -- ({i*s:.2f},.07);'+(f'\\node[below=3pt,font=\\scriptsize] at ({i*s:.2f},0) {{${i}$}};' if i%2==0 else '')
for nm,v in (('A',a6),('B',b6),('C',c6)): g+=f'\\fill[vurgu] ({v*s:.2f},0) circle (.1);\\node[above=5pt] at ({v*s:.2f},0) {{{nm}}};'
q('0006',tipId='mts-yakin',tip='Sayı doğrusunda yakınlık ve uzaklık',z='zor',alt='Mutlak Değer ve Uzaklık',kaz='Sayı doğrusunda işaretli noktalara yakınlık ve uzaklık koşullarını mutlak değer eşitsizlikleriyle yorumlayıp ortak tam sayıları sayar.',kalip='şekilli',sekil=TP(g),
 kart='K-MTS-06 (yakınlık yorumu) · A = −6, B = 4, C = −8; |x − A| < |x − B|, |x − C| ≥ 3, |x| ≤ 12',
 metin='Şekildeki sayı doğrusunda A, B ve C noktalarının yerleri gösterilmiştir. Sayı doğrusu üzerindeki x tam sayısına karşılık gelen nokta, A noktasına B noktasından daha yakındır, C noktasına uzaklığı en az 3 birimdir ve başlangıç noktasına (0) uzaklığı en çok 12 birimdir.\nBuna göre x kaç farklı değer alabilir?',
 dogru=6,yan=[(4,'C’ye uzaklık koşulunda eşitliği dışarıda bırakmış (|x + 8| > 3): −12, −4, −3, −2 değerlerini bulmuş.','dikkat'),(7,'Orta nokta olan −1’i de almış; bu noktada A’ya ve B’ye uzaklık eşittir, “daha yakın” koşulu sağlanmaz.','dikkat'),(13,'Yakınlık yönünü ters okumuş: B’ye daha yakın olan 0, 1, …, 12 değerlerini saymış.','dikkat'),(20,'A ve B’ye yakınlık koşulunu unutup yalnız C ve başlangıç koşullarından 20 değer bulmuş.','dikkat')],
 istenen='x’in alabileceği tam sayı değerlerinin sayısı.',
 ip=['A ve B’ye eşit uzaklıktaki noktayı bul; hangi tarafın A’ya daha yakın olduğunu belirle.'],
 bilgi=[YAK,ARL,SAYI],
 ad=[A('Noktaları oku','Şekilden A, B ve C’nin yerleri.','A = −6 · B = 4 · C = −8'),A('A’ya daha yakın','Orta nokta (−6 + 4) ÷ 2 = −1; A’ya daha yakın olanlar solundadır.','x < −1'),A('C koşulu','C’ye uzaklık en az 3.','|x + 8| ≥ 3 → x ≤ −11 ya da x ≥ −5'),A('Başlangıç koşulu','Başlangıç noktasına uzaklık en çok 12.','−12 ≤ x ≤ 12'),A('Ortak değerleri say','Dört koşulu birlikte sağlayanlar.','−12, −11 ve −5, −4, −3, −2 → 6')],
 puf='İki noktaya yakınlık sorularında önce orta noktayı bul: eşit uzaklık yalnız orta noktada olur ve “daha yakın” koşulunda dahil edilmez.')

# ---------- 07 · zor · grafik ve alan ----------
a7,b7,y7=3,-1,5
xk=[a7-(y7-b7),a7+(y7-b7)]; tb=xk[1]-xk[0]; hh=y7-b7; alan=Fr(tb*hh,2)
assert xk==[-3,9] and tb==12 and hh==6 and alan==36 and tb==12 and tb*hh==72 and Fr(tb*(y7-1),2)==24 and Fr(tb*y7,2)==30 and Fr(6*6,2)==18
for x in xk: assert abs(x-a7)+b7==y7
s=.45; X0,X1,Y0,Y1=-5,11,-2,7
g=''.join(f'\\draw[gray!35] ({i*s:.2f},{Y0*s:.2f}) -- ({i*s:.2f},{Y1*s:.2f});' for i in range(X0,X1+1))+''.join(f'\\draw[gray!35] ({X0*s:.2f},{j*s:.2f}) -- ({X1*s:.2f},{j*s:.2f});' for j in range(Y0,Y1+1))
g+=f'\\draw[thick] ({X0*s:.2f},{Y0*s:.2f}) rectangle ({X1*s:.2f},{Y1*s:.2f});'
g+=f'\\fill[vurgu!20] ({xk[0]*s:.2f},{y7*s:.2f}) -- ({a7*s:.2f},{b7*s:.2f}) -- ({xk[1]*s:.2f},{y7*s:.2f}) -- cycle;'
g+=f'\\draw[-{{Stealth}}] ({X0*s:.2f},0) -- ({(X1+.5)*s:.2f},0);\\draw[-{{Stealth}}] (0,{Y0*s:.2f}) -- (0,{(Y1+.5)*s:.2f});\\node[anchor=west] at ({(X1+.5)*s:.2f},0) {{$x$}};\\node[anchor=south] at (0,{(Y1+.5)*s:.2f}) {{$y$}};'
g+=f'\\draw[very thick,vurgu] ({(a7-6.5)*s:.2f},{(b7+6.5)*s:.2f}) -- ({a7*s:.2f},{b7*s:.2f}) -- ({(a7+6.5)*s:.2f},{(b7+6.5)*s:.2f});'
g+=f'\\draw[thick,dashed] ({X0*s:.2f},{y7*s:.2f}) -- ({X1*s:.2f},{y7*s:.2f});\\node[anchor=north east,font=\\small] at ({X1*s:.2f},{y7*s:.2f}) {{$y=5$}};'
for i in range(X0,X1+1): g+=f'\\node[below=2pt,font=\\scriptsize] at ({i*s:.2f},{Y0*s:.2f}) {{${i}$}};'
for j in range(Y0,Y1+1): g+=f'\\node[left=2pt,font=\\scriptsize] at ({X0*s:.2f},{j*s:.2f}) {{${j}$}};'
q('0007',tipId='mts-grafik',tip='Mutlak değer grafiği ve alan',z='zor',alt='Mutlak Değer Grafiği',kaz='y = |x − a| + b grafiğinden tepe noktasını okuyup bir yatay doğruyla sınırlanan üçgenin alanını hesaplar.',kalip='grafik',sekil=TP(g),
 kart='K-MTS-07 (grafik ve alan) · y = |x − 3| − 1, y = 5, üçgen alanı 36',
 metin='Şekilde, a ve b gerçel sayıları için y = |x − a| + b fonksiyonunun grafiği ve bir yatay doğru verilmiştir. Grafik ile doğru arasında kalan bölge boyalıdır; birim kareler ızgaradaki karelerdir.\nBuna göre boyalı bölgenin alanı kaç birimkaredir?',
 dogru=36,yan=[(12,'Alan yerine boyalı bölgenin tabanını (kesim noktaları arasındaki uzaklık 12) yazmış.','dikkat'),(18,'Tabanı yanlış, 6 almış (yalnız bir kolun yatay uzaklığı): 6 × 6 ÷ 2 = 18.','dikkat'),(24,'Tepe noktasını (3, 1) okuyup yüksekliği 5 − 1 = 4 almış: 12 × 4 ÷ 2 = 24.','dikkat'),(30,'Yüksekliği x ekseninden ölçüp 5 almış: 12 × 5 ÷ 2 = 30; yükseklik tepe noktasından doğruya kadardır.','dikkat')],
 istenen='Boyalı bölgenin alanı (birimkare).',
 ip=['Önce grafiğin tepe noktasını ızgaradan oku; boyalı bölge hangi şekle benziyor?'],
 bilgi=[GRF,UZ],
 ad=[A('Tepe noktasını oku','Grafiğin en düşük noktası (3, −1).','a = 3, b = −1'),A('Kesim noktaları','Doğru y = 5 iken |x − 3| − 1 = 5 olur.','|x − 3| = 6 → x = −3 ve x = 9'),A('Taban ve yükseklik','Taban kesim noktaları arasındadır; yükseklik tepe noktasından doğruya.','taban 9 − (−3) = 12 · yükseklik 5 − (−1) = 6'),A('Alan','Üçgen alanı.','12 × 6 ÷ 2 = 36')],
 puf='V biçimli grafikte kollar 1 eğimli olduğundan yükseklik kadar yatay yol gidilir: yükseklik 6 ise taban 2 × 6 = 12 olur.')

bitir(P,'mutlaksek','mat|Mutlak Değer')
