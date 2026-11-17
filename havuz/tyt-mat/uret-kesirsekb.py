"""Kesir Problemleri · ŞEKİLLİ ek paket b (10 soru): şekil/tablo çözüm verisini taşır; her doğru ve çeldirici değer assert'lidir. Kardeş yok, ipucu 1."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
H.KONU='Kesir Problemleri'
UK='prob|Kesir Problemleri'
P=Parti('kesirsekb','Kesir Problemleri',UK)
KY='ÖSYM 2018–2026 TYT Matematik (şekilli/tablolu kesir soruları; yalnız mantık) · MEB 9. sınıf'
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)
def fig(body): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'+body+'\n\\end{tikzpicture}')
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)
def F(n,d): return f'{{\\large $\\frac{{{n}}}{{{d}}}$}}'

SYD=B('Sayı doğrusunda kesir','iki eş aralığın arası kaç parçaya bölünmüşse her parça birimin o kadarda biridir; bir noktanın değeri 0’dan o noktaya kadar sayılan parçalarla bulunur. Örnek: 1 birimi 4 parçalı doğruda 3 parça ilerleyen nokta 3/4’tür')
DNG=B('Dengedeki terazi','dengede iki kefedeki toplam kütle eşittir; her iki kefeden aynı cisim çıkarılınca denge bozulmaz. Örnek: sol kefede iki özdeş top ile 1 kg, sağ kefede bir top ile 4 kg varsa top 3 kg’dır')
VEN=B('Venn şemasında kesir','şemadaki bölgelerin kesirleri sınıfın tamamının kesridir ve tamamı 1 eder; hiçbir bölgede olmayan kısım da 1’den kalandır. Örnek: bölgeler 1/2 ve 1/4 ise dışarıda 1/4 kalır')
KES=B('Kalan kesir','bütünün kesirleri çıkarıldığında kalan kısım bulunur; kalan miktar biliniyorsa tümü, kalanın kesrine bölünerek bulunur. Örnek: bütünün 1/3’ü ve 1/3’ü ayrıldıysa kalan 1/3’tür; kalan 8 ise tümü 24’tür')
KGR=B('Grafikte kesir','bir grubun kesri, grubun sayısıyla çarpılır; farklı gruplardan gelen parçalar toplanır. Örnek: 40 kişinin 1/4’ü 10, 20 kişinin 1/2’si 10 ise toplam 20 kişidir')
TER=B('İşlemin tersi','çıkıştan başlayıp her işlemin tersi sondan başa doğru uygulanır; bir sayıya kendisinin kesri kadar eklemek, sayıyı (1 + kesir) ile çarpmaktır. Örnek: 8’e kendisinin 1/2’si eklenirse 12 olur, 12’yi 3/2’ye bölmek 8 verir')
ALN=B('Alanın kesri','dikdörtgenin bir bölümünün alanı, bütün alanın o bölümün kesri kadarıdır; bir bölümün alanı ve kesri biliniyorsa bütünün alanı bulunur. Örnek: alanın 1/5’i 30 m² ise bütün 150 m²’dir')
GRF=B('Çizgi grafiğinde kesir','grafikte okunan kesir, kapasitenin o kesri kadar niceliği gösterir. Örnek: 80 birimlik kabın 1/4’ü dolu ise 20 birim vardır')
OLC=B('Tarifi ölçeklemek','kişi sayısı kaç katına çıkıyorsa her malzeme o katına çıkar; kesir çarpılarak ölçeklenir. Örnek: 2 kişilik tarif 1/3 kg unsa, 6 kişilik tarif 1 kg un ister')
DAL=B('Dallanma şemasında kesir','bir dalın kesri, geldiği dalın miktarının kesri olarak çarpılır; bilinen bir uç değerden geriye giderek bütünün miktarı bulunur. Örnek: bütünün 1/2’sinin 1/2’si 10 ise bütün 40’tır')

kartla('K-KSB-01','Sayı doğrusunda iki nokta','Noktaların değerleri eş parçalardan okunur; istenen oran kesirlerin bölümüyle bulunur.','Kesrin tersini almak; fark yerine bölüm yazmak.','kolay','yeni nesil',3,'kdb-dogru','Sayı doğrusu ve kesir')
kartla('K-KSB-02','Terazi dengesi','İki kefenin kütleleri eşitlenir; benzer terimler yok edilerek bilinmeyen kolinin kütlesi bulunur.','Kütleleri toplamak; koliyi tek kefede saymak.','kolay','hikâyeli',3,'kdb-terazi','Terazi dengesi')
kartla('K-KSB-03','Venn şeması kesirleri','Bölge kesirleri toplanıp 1’den çıkarılarak dışarıdaki kesir; kişi sayısından bütün bulunur.','Bir bölgeyi çıkarmayı unutmak; ortak bölgeyi iki kez saymak.','orta','hikâyeli',3,'kdb-venn','Venn şeması ve kesir')
kartla('K-KSB-04','Okuma tablosu','Tablodaki kesirler toplanıp bütünden çıkarılır; kalan sayfa kalan kesre bölünür.','Bir günü atlamak; kalan kesri tümü sanmak.','orta','tablo',4,'kdb-tablo','Kesirli tablo')
kartla('K-KSB-05','Sütun grafiği ve kesir','Her sütundaki sayı ilgili kesriyle çarpılıp toplanır.','Bir sütunu atlamak; kesri ters almak; toplamı üye sanmak.','orta','hikâyeli',4,'kdb-grafik','Grafik okuma ve kesir')
kartla('K-KSB-06','İşlem makinesi','Çıkıştan geriye doğru her işlemin tersi uygulanır; kesirli artırma katsayıyla geri alınır.','Ters işlem yerine ileri işlem yapmak; artırmayı kesirle çıkararak geri almak.','orta','yeni nesil',4,'kdb-makine','Geri izleme')
kartla('K-KSB-07','Bölünmüş dikdörtgen','Eş parça sayılarından bölümlerin kesirleri bulunur; bilinen bölümden bütünün alanı hesaplanır.','Parça sayılarını ters okumak; yarı ile bütünü karıştırmak.','orta','hikâyeli',3,'kdb-alan','Bölünmüş dikdörtgen')
kartla('K-KSB-08','Çizgi grafiği','Grafikten istenen anın kesri okunur; kapasiteyle çarpılır.','Yanlış zamanı okumak; farkı almak.','kolay','hikâyeli',3,'kdb-grafik','Grafik okuma ve kesir')
kartla('K-KSB-09','Kesirli tarif tablosu','Kişi sayısının kaç katına çıktığı bulunur; istenen malzemeler bu katla çarpılıp toplanır.','Kişi sayısı farkını kat sanmak; yalnız bir malzemeyi ölçeklemek.','orta','tablo',3,'kdb-tablo','Kesirli tablo')
kartla('K-KSB-10','Dallanma şeması','Bilinen uçtan geriye giderek bütün, sonra istenen uç bulunur.','Dalın kesrini bütünün kesri sanmak; yanlış dalı seçmek.','zor','hikâyeli',4,'kdb-makine','Geri izleme')

# ===== 01 kolay · sayı doğrusu =====
p_,q_,bol=4,9,6
vp,vq=Fr(p_,bol),Fr(q_,bol); v=vp/vq
assert v==Fr(4,9)
vals=[Fr(4,9),Fr(2,3),Fr(5,6),Fr(3,2),Fr(9,4)]
assert vp==Fr(2,3) and vq==Fr(3,2) and vq-vp==Fr(5,6) and vq/vp==Fr(9,4) and len(set(vals))==5
cm=0.55; o=[f'\\draw[thick] (0,0) -- ({12*cm},0);']
for i in range(13):
    h=0.28 if i%6==0 else 0.14
    o.append(f'\\draw[thick] ({i*cm:.2f},-{h}) -- ({i*cm:.2f},{h});')
for i,l in ((0,'0'),(6,'1'),(12,'2')): o.append(f'\\node[below=6pt] at ({i*cm:.2f},0) {{{l}}};')
for pos,nm in ((p_,'P'),(q_,'Q')): o.append(f'\\fill[vurgu!70!black] ({pos*cm:.2f},0) circle (0.1); \\node[above=7pt] at ({pos*cm:.2f},0) {{{nm}}};')
SK=fig('\n'.join(o))
q('0001',tipId='kdb-dogru',tip='Sayı doğrusu ve kesir',z='kolay',alt='Sayı Doğrusu',kaz='Eş aralıklı sayı doğrusunda iki noktanın değerini okuyup oranını bulur.',kalip='yeni nesil',
 kart='K-KSB-01 · 6 parça/birim; P=4/6, Q=9/6',
 metin='Sayı doğrusunda bir noktanın gösterdiği sayı, 0 noktasından o noktaya olan uzaklığın 0 ile 1 arasındaki uzaklığa oranıdır. Şekilde 0, 1 ve 2 noktaları işaretli ve her iki işaretli nokta arası birbirine eşit aralıklara bölünmüştür; P ve Q noktaları da şekilde gösterilmiştir.\nBuna göre, P noktasının gösterdiği sayı, Q noktasının gösterdiği sayının kaçta kaçıdır?',
 dogru='4/9',yan=[('2/3','P noktasının değerini bulup oran yerine onu yazmış.','dikkat'),('5/6','Oran yerine Q ile P arasındaki farkı yazmış: 3/2 − 2/3.','dikkat'),('3/2','Q noktasının değerini yazmış.','dikkat'),('9/4','Oranı ters kurmuş: Q ÷ P.','dikkat')],
 sira=['4/9','2/3','5/6','3/2','9/4'],
 istenen='P değerinin Q değerine oranı.',ip=['Önce 0 ile 1 arasında kaç eş aralık olduğunu say; her iki noktanın değerini bu aralıkların sayısından yaz.'],bilgi=[SYD],sekil=SK,
 ad=[A('Bir birim','0 ile 1 arası 6 eş aralıktır.','Her aralık 1/6'),A('P ve Q','P, 4 aralık; Q, 9 aralık uzaklıktadır.','P = 4/6 = 2/3; Q = 9/6 = 3/2'),A('Oran','P’nin Q’ya bölümü.','(2/3) ÷ (3/2) = 4/9')],
 puf='Her noktanın değerini aralık sayısından bul.')

# ===== 02 kolay · terazi =====
x=Fr(9,4)-Fr(1,2); assert x==Fr(7,4)
e=[Fr(9,4)/2,Fr(9,4),Fr(9,4)+Fr(1,2),x/2]
assert e==[Fr(9,8),Fr(9,4),Fr(11,4),Fr(7,8)] and len({x,*e})==5
def kut(x0,w,lab,fill='vurgu!15'): return f'\\filldraw[fill={fill},draw=black,thick] ({x0},1.35) rectangle ({x0+w},{1.35+0.6}); \\node at ({x0+w/2},1.65) {{{lab}}};'
o=['\\draw[very thick] (-3.2,2.9) -- (3.2,2.9); \\draw[very thick] (0,2.9) -- (-0.6,0) -- (0.6,0) -- cycle; \\fill (0,2.9) circle (0.08);',
 '\\draw[thick] (-3.0,2.9) -- (-4.1,1.35); \\draw[thick] (-3.0,2.9) -- (-1.9,1.35); \\draw[very thick] (-4.3,1.35) -- (-1.7,1.35);',
 '\\draw[thick] (3.0,2.9) -- (1.9,1.35); \\draw[thick] (3.0,2.9) -- (4.1,1.35); \\draw[very thick] (1.7,1.35) -- (4.3,1.35);',
 kut(-4.2,0.65,'K'),kut(-3.5,0.65,'K'),kut(-2.8,1.0,F(1,2)+' kg','white'),
 kut(1.8,0.65,'K'),kut(2.5,1.6,'$2\\frac{1}{4}$ kg','white'),
 '\\node at (0,-0.45) {K: aynı kütleli koli};']
SK=fig('\n'.join(o))
q('0002',tipId='kdb-terazi',tip='Terazi dengesi',z='kolay',alt='Terazi',kaz='Dengedeki terazinin iki kefesini eşitleyerek kolinin kütlesini bulur.',kalip='hikâyeli',
 kart='K-KSB-02 · 2K+1/2 = K+9/4',
 metin='Bir kargo deposunda bir terazi şekildeki gibi dengededir. Sol kefede iki, sağ kefede bir tane K ile gösterilen koli bulunmaktadır; K ile gösterilen kolilerin hepsi birbirinin aynıdır. Kolilerin yanında kefelerde kütleleri yazılı birer ağırlık da vardır ve başka bir cisim yoktur.\nBuna göre, bir K kolisinin kütlesi kaç kilogramdır?',
 dogru=x,yan=[(e[0],'Sağ kefedeki kütleyi (9/4) ikiye bölmüş.','dikkat'),(e[1],'Sağ kefedeki ağırlığı koli kütlesi sanmış.','dikkat'),(e[2],'Ağırlıkları toplayarak (1/2 + 9/4) koli kütlesi bulmuş.','dikkat'),(e[3],'Bulunan kütleyi iki koli için toplam sanıp yarıya bölmüş.','dikkat')],
 istenen='Bir kolinin kütlesi (kg).',ip=['Her iki kefede de bulunan aynı cisimler için dengenin bozulup bozulmayacağını düşün.'],bilgi=[DNG],sekil=SK,
 ad=[A('Denge','İki kefenin kütleleri eşit: 2K + 1/2 = K + 9/4','Sağ kefede 2 1/4 = 9/4'),A('Ortak koliyi çıkar','Her iki kefeden bir koli alınır.','K + 1/2 = 9/4'),A('Koli','Kütleler çıkarılır.','K = 9/4 − 1/2 = 7/4 = 1,75 kg')],
 puf='Her iki kefeden aynı şeyi alabilirsin.')

# ===== 03 orta · Venn =====
fa,fb,fo=Fr(1,3),Fr(1,6),Fr(1,4); fd=1-(fa+fb+fo); none=12; v=none/fd
e=[none/(fa+fb+fo),none/(1-fa-fb),none/fa,none/fb]
assert fd==Fr(1,4) and v==48 and e==[16,24,36,72] and all((v*f).denominator==1 for f in (fa,fb,fo)) and len({v,*e})==5
o=['\\draw[thick] (0,0) rectangle (7.2,4.1);','\\draw[thick,fill=vurgu!15,fill opacity=0.6] (2.6,1.9) circle (1.35); \\draw[thick,fill=vurgu!30,fill opacity=0.5] (4.6,1.9) circle (1.35);',
 '\\node at (2.0,3.75) {Satranç}; \\node at (5.2,3.75) {Resim};',f'\\node at (1.95,1.9) {{{F(1,3)}}}; \\node at (3.6,1.9) {{{F(1,6)}}}; \\node at (5.25,1.9) {{{F(1,4)}}};']
SK=fig('\n'.join(o))
q('0003',tipId='kdb-venn',tip='Venn şeması ve kesir',z='orta',alt='Venn Şeması',kaz='Venn şemasındaki bölge kesirlerinden dışarıda kalan kesri bulup sınıf mevcudunu hesaplar.',kalip='hikâyeli',
 kart='K-KSB-03 · 1/3, 1/6, 1/4; dışarıda 12 kişi',
 metin='Bir ortaöğretim sınıfındaki öğrencilerin, okulun satranç ve resim kulüplerine üyeliği şekildeki Venn şemasında gösterilmiştir. Dikdörtgen sınıfın bütün öğrencilerini; her bölgedeki kesir, o bölgedeki öğrencilerin sınıf mevcudunun kaçta kaçı olduğunu gösterir. Her iki kulübe de üye olmayan 12 öğrenci vardır.\nBuna göre, bu sınıfta kaç öğrenci vardır?',
 dogru=v,yan=[(e[0],'Dışarıdaki öğrencileri, üç bölgenin kesir toplamına (3/4) bölmüş.','dikkat'),(e[1],'Yalnız resim bölgesini toplama katmamış: 1 − (1/3 + 1/6) = 1/2, 12 ÷ 1/2.','dikkat'),(e[2],'12 kişiyi yalnız satranç bölgesinin kesrine (1/3) bölmüş.','dikkat'),(e[3],'12 kişiyi yalnız ortak bölgenin kesrine (1/6) bölmüş.','dikkat')],
 istenen='Sınıf mevcudu.',ip=['Şemadaki bölgelerin kesirleri toplamıyla bütünün ilişkisini düşün; dışarıda kalan kısmı kesir olarak bul.'],bilgi=[VEN],sekil=SK,
 ad=[A('Bölgeler','Üç bölgenin kesirleri toplanır.','1/3 + 1/6 + 1/4 = 3/4'),A('Dışarıda','Bütün 1’den çıkarılır.','1 − 3/4 = 1/4'),A('Mevcut','12 kişi mevcudun 1/4’üdür.','12 ÷ (1/4) = 48')],
 puf='Bütün kesir 1’dir.')

# ===== 04 orta · tablo =====
ks=[Fr(1,6),Fr(1,4),Fr(1,3)]; kal=1-sum(ks); sayfa=75; v=sayfa/kal
e=[sayfa/sum(ks),sayfa/(1-ks[0]-ks[2]),sayfa/ks[2],sayfa/ks[0]]
assert kal==Fr(1,4) and v==300 and e==[100,150,225,450] and len({v,*e})==5
SK=tablo_svg(['Gün','Okunan kısım'],[['Pazartesi','kitabın 1/6’sı'],['Salı','kitabın 1/4’ü'],['Çarşamba','kitabın 1/3’ü'],['Perşembe','kalan 75 sayfa']])
q('0004',tipId='kdb-tablo',tip='Kesirli tablo',z='orta',alt='Okuma Tablosu',kaz='Tablodaki kesirleri toplayıp kalan kesirden kitabın sayfa sayısını bulur.',kalip='tablo',
 kart='K-KSB-04 · 1/6+1/4+1/3, kalan 75 sayfa',
 metin='Bir edebiyat öğrencisi, sınav öncesinde ödev olarak verilen bir romanı okumuş ve günlük ilerlemesini aşağıdaki tabloda göstermiştir. Roman, Perşembe günü tamamen bitmiştir; kitaptaki her sayfa bu dört günden yalnız birinde okunmuş ve hiçbir sayfa tekrar okunmamıştır.\nBuna göre, bu romanın sayfa sayısı kaçtır?',
 dogru=v,yan=[(e[0],'75 sayfayı ilk üç günün toplam kesrine (3/4) bölmüş.','dikkat'),(e[1],'Salı gününü hesaba katmamış: 1 − 1/6 − 1/3 = 1/2 sanmış.','dikkat'),(e[2],'Çarşamba günü kesrini (1/3) Perşembe’nin kesri sanmış.','dikkat'),(e[3],'Pazartesi günü kesrini (1/6) Perşembe’nin kesri sanmış.','dikkat')],
 istenen='Romanın sayfa sayısı.',ip=['İlk üç günün kesirlerinin toplamıyla bütün arasındaki ilişkiyi kullanarak Perşembe’nin kesrini bul.'],bilgi=[KES],sekil=SK,
 ad=[A('İlk üç gün','Kesirler ortak paydada toplanır.','2/12 + 3/12 + 4/12 = 3/4'),A('Perşembe','Bütün 1’den çıkarılır.','1 − 3/4 = 1/4'),A('Sayfa sayısı','75 sayfa kitabın 1/4’üdür.','75 ÷ (1/4) = 300')],
 puf='Kalan kesri bul.')

# ===== 05 orta · sütun grafiği =====
sn=[('9. sınıf',120,Fr(1,4)),('10. sınıf',90,Fr(1,3)),('11. sınıf',60,Fr(2,3)),('12. sınıf',30,Fr(1,2))]
v=sum(n*f for _,n,f in sn)
e=[v-40,v-40+20,v-30+60,300]
assert v==115 and e==[75,95,145,300] and len({v,*e})==5
sy=0.022; o=['\\draw[-{Stealth}] (0,0) -- (5.6,0); \\draw[-{Stealth}] (0,0) -- (0,3.1) node[above] {Öğrenci sayısı};']
for t in (30,60,90,120): o.append(f'\\draw[gray!50,dashed] (0,{t*sy:.2f}) -- (5.3,{t*sy:.2f}); \\draw (-0.06,{t*sy:.2f}) -- (0.06,{t*sy:.2f}); \\node[left=2pt] at (0,{t*sy:.2f}) {{{t}}};')
for i,(nm,n,f) in enumerate(sn):
    xx=0.6+i*1.25; o.append(f'\\filldraw[fill=vurgu!25,draw=vurgu!80!black] ({xx:.2f},0) rectangle ({xx+0.8:.2f},{n*sy:.2f}); \\node[below=2pt,align=center] at ({xx+0.4:.2f},0) {{{nm.replace(' ','\\\\')}}};')
SK=fig('\n'.join(o))
q('0005',tipId='kdb-grafik',tip='Grafik okuma ve kesir',z='orta',alt='Sütun Grafiği',kaz='Sütun grafiğindeki sınıf mevcutlarının kesirlerini hesaplayıp toplam kulüp üyesini bulur.',kalip='hikâyeli',
 kart='K-KSB-05 · 120·1/4 + 90·1/3 + 60·2/3 + 30·1/2',
 metin='Bir lisede sınıf düzeylerine göre öğrenci sayıları şekildeki sütun grafikte verilmiştir. Okul yönetimi, kulüp odasının büyüklüğünü belirlemek için üye sayısını öğrenmek istemektedir. Okulun bilim kulübüne 9. sınıfların 1/4’ü, 10. sınıfların 1/3’ü, 11. sınıfların 2/3’ü ve 12. sınıfların 1/2’si üyedir; kulüp yalnız bu öğrencilerden oluşmaktadır.\nBuna göre, bilim kulübünün üye sayısı kaçtır?',
 dogru=v,yan=[(e[0],'11. sınıfı hesaba katmamış: 30 + 30 + 15.','dikkat'),(e[1],'11. sınıfın kesrini 1/3 almış: 30 + 30 + 20 + 15.','dikkat'),(e[2],'10. sınıfın kesrini 2/3 almış: 30 + 60 + 40 + 15.','dikkat'),(e[3],'Toplam öğrenci sayısını üye sayısı sanmış.','dikkat')],
 istenen='Kulübün üye sayısı.',ip=['Her sınıf düzeyi için sütundaki sayıyı ilgili kesirle ayrı ayrı çarp.'],bilgi=[KGR],sekil=SK,
 ad=[A('9. ve 10. sınıf','Sayı × kesir.','120 × 1/4 = 30; 90 × 1/3 = 30'),A('11. ve 12. sınıf','Sayı × kesir.','60 × 2/3 = 40; 30 × 1/2 = 15'),A('Toplam','Dört sayı toplanır.','30 + 30 + 40 + 15 = 115')],
 puf='Önce her sütundan bir sayı çıkar.')

# ===== 06 zor · işlem makinesi =====
cik=63; s1=cik+12; s2=s1/Fr(5,4); x=s2/Fr(3,5)
e=[Fr(cik)*Fr(3,5)*Fr(5,4)-12,s1*Fr(3,5),s2,s1]
assert s1==75 and s2==60 and x==100 and e==[Fr(141,4),45,60,75] and len({x,*e})==5
bx=lambda cx,cy,txt,w=2.3: f'\\node[draw,thick,rounded corners=3pt,fill=vurgu!12,minimum width={w}cm,minimum height=1.3cm,align=center,inner sep=3pt] at ({cx},{cy}) {{{txt}}};'
o=[bx(0,0,'Giriş\\\\x',1.5),bx(3.4,0,'Sayının\\\\3/5’ini\\\\al',2.3),bx(6.9,0,'Sonuca\\\\1/4’ü kadar\\\\ekle',2.3),bx(6.9,-2.2,'Sonuçtan\\\\12 çıkar',2.3),bx(3.4,-2.2,'Çıkış\\\\63',2.3)]
o+=['\\draw[-{Stealth},thick] (0.75,0) -- (2.2,0);','\\draw[-{Stealth},thick] (4.55,0) -- (5.7,0);','\\draw[-{Stealth},thick] (6.9,-0.65) -- (6.9,-1.55);','\\draw[-{Stealth},thick] (5.7,-2.2) -- (4.55,-2.2);']
SK=fig('\n'.join(o))
q('0006',tipId='kdb-makine',tip='Geri izleme',z='orta',alt='İşlem Makinesi',kaz='Kesirli işlemler içeren bir makinede çıkıştan geriye giderek girişi bulur.',kalip='yeni nesil',
 kart='K-KSB-06 · ×3/5, ×5/4, −12; çıkış 63',
 metin='Bir bilgisayar programı, kullanıcının girdiği pozitif x sayısını şekildeki adımlardan, okları izleyerek sırayla geçirir. Her adımda yapılan işlem, yalnız o adıma ulaşan değere uygulanır ve ara sonuçlar tam olarak saklanır. Program sonunda şekilde yazılı değeri ekrana yazdırmıştır.\nBuna göre, kullanıcının girdiği x değeri kaçtır?',
 dogru=x,yan=[(e[0],'İşlemleri geri almak yerine çıkışa ileri yönde uygulamış: 63 × 3/5 × 5/4 − 12.','dikkat'),(e[1],'Ters işlemde 75’i 3/5 ile çarpmış: 75 × 3/5.','dikkat'),(e[2],'Yalnız son iki işlemi geri almış; ilk kutuyu geri almamış.','dikkat'),(e[3],'Yalnız “12 çıkar” işlemini geri almış.','dikkat')],
 istenen='Girilen x değeri.',ip=['Çıkıştan girişe doğru hangi işlemin hangi işlemle geri alınacağını düşün.'],bilgi=[TER],sekil=SK,
 ad=[A('Çıkarmayı geri al','Son kutu 12 çıkarmıştı.','63 + 12 = 75'),A('Eklemeyi geri al','Önceki sayının 5/4 katı 75 ise önceki sayı:','75 ÷ 5/4 = 60'),A('İlk kutuyu geri al','Girişin 3/5’i 60 ise giriş:','60 ÷ 3/5 = 100')],
 puf='Her adımın etkisini ortadan kaldıran işlemi bul.')

# ===== 07 orta · bölünmüş dikdörtgen =====
Bm=270; frB=Fr(3,5)*Fr(1,2); T=Bm/frB; v=T*Fr(2,5)
e=[Bm*Fr(2,3),T/2,2*Bm,T]
assert frB==Fr(3,10) and T==900 and v==360 and e==[180,450,540,900] and len({v,*e})==5
W,H_=6.0,3.6; o=[f'\\draw[thick] (0,0) rectangle ({W},{H_});',f'\\draw[thick] (2.4,0) -- (2.4,{H_}); \\draw[thick] (2.4,1.8) -- ({W},1.8);',
 '\\node at (1.2,1.8) {A}; \\node at (4.2,2.7) {B}; \\node at (4.2,0.9) {C};']
for i in range(6): o.append(f'\\draw ({i*1.2:.1f},{H_}) -- ({i*1.2:.1f},{H_+0.18});')
o.append(f'\\draw[<->] (0,{H_+0.18+0.1}) -- ({W},{H_+0.18+0.1}); \\node[above=2pt] at ({W/2},{H_+0.28}) {{işaretli 5 aralık birbirine eşit}};')
for yy in (0,1.8,3.6): o.append(f'\\draw ({W},{yy}) -- ({W+0.18},{yy});')
o.append(f'\\node[right=6pt,align=left] at ({W+0.2},1.8) {{işaretli\\\\2 aralık\\\\eşit}};')
SK=fig('\n'.join(o))
q('0007',tipId='kdb-alan',tip='Bölünmüş dikdörtgen',z='orta',alt='Bölünmüş Dikdörtgen',kaz='Eş aralıklarla bölünmüş dikdörtgende bölümlerin kesirlerini bulup bilinen alandan istenen alanı hesaplar.',kalip='hikâyeli',
 kart='K-KSB-07 · A=2/5, B=C=3/10; B=270 m²',
 metin='Dikdörtgen biçimli bir arsa şekildeki gibi A, B ve C bölümlerine ayrılmıştır; A bölümü üst kenarın 5 eş aralığından 2’sini, B ile C birlikte 3’ünü kaplar ve B ile C bölümlerinin alanları birbirine eşittir. Arsa sahibi, B bölümüne bahçe yapacak ve bu bölümün alanının 270 m² olduğunu belirtmiştir.\nBuna göre, A bölümünün alanı kaç m²’dir?',
 dogru=v,yan=[(e[0],'B bölümünü sağ tarafın tamamı (3 parça) sanıp A : B = 2 : 3 almış: 270 × 2/3.','dikkat'),(e[1],'Arsanın yarısını A’nın alanı sanmış.','dikkat'),(e[2],'A bölümünü B’nin iki katı sanmış: 2 × 270.','dikkat'),(e[3],'Arsanın tamamının alanını yazmış.','dikkat')],
 istenen='A bölümünün alanı (m²).',ip=['Üst kenardaki eş aralıklardan A ve (B, C) bölümlerinin payını, B ve C’nin paylaşımından da B’nin bütündeki payını belirle.'],bilgi=[ALN],sekil=SK,
 ad=[A('B’nin kesri','Sağ bölüm 3/5’tir ve ikiye bölünmüştür.','3/5 × 1/2 = 3/10'),A('Arsanın alanı','270 m², arsanın 3/10’udur.','270 ÷ 3/10 = 900 m²'),A('A’nın alanı','A arsanın 2/5’idir.','900 × 2/5 = 360 m²')],
 puf='Önce bütünün alanını bul.')

# ===== 08 kolay · çizgi grafiği =====
kap=480; pts=[(0,Fr(1,8)),(2,Fr(3,8)),(4,Fr(5,8)),(6,Fr(7,8))]; v=kap*pts[3][1]
e=[kap*pts[0][1],kap*pts[1][1],kap*(pts[3][1]-pts[1][1]),kap*pts[2][1]]
assert v==420 and e==[60,180,240,300] and len({v,*e})==5
sx,sy=0.85,3.2
o=[f'\\draw[-{{Stealth}}] (0,0) -- (6*{sx}+0.5,0) node[right] {{saat}}; \\draw[-{{Stealth}}] (0,0) -- (0,{sy+0.45}) node[above] {{Doluluk}};'.replace('6*0.85+0.5','5.6')]
for t in range(0,7,2): o.append(f'\\draw ({t*sx:.2f},-0.06) -- ({t*sx:.2f},0.06); \\node[below=2pt] at ({t*sx:.2f},0) {{{t}}};')
for k in range(1,9,2): o.append(f'\\draw (-0.06,{k/8*sy:.2f}) -- (0.06,{k/8*sy:.2f}); \\node[left=2pt] at (0,{k/8*sy:.2f}) {{{F(k,8)}}};')
o.append('\\draw[thick,vurgu!80!black] '+' -- '.join(f'({t*sx:.2f},{float(f)*sy:.2f})' for t,f in pts)+';')
for t,f in pts: o.append(f'\\fill[vurgu!80!black] ({t*sx:.2f},{float(f)*sy:.2f}) circle (0.07); \\draw[dotted] ({t*sx:.2f},0) -- ({t*sx:.2f},{float(f)*sy:.2f}) -- (0,{float(f)*sy:.2f});')
SK=fig('\n'.join(o))
q('0008',tipId='kdb-grafik',tip='Grafik okuma ve kesir',z='kolay',alt='Çizgi Grafiği',kaz='Doluluk kesrinin zamanla değişimini gösteren grafikten istenen andaki su miktarını bulur.',kalip='hikâyeli',
 kart='K-KSB-08 · kapasite 480 L; 6. saatte 7/8',
 metin='Bir çiftlikte, sabah erken saatte içinde bir miktar su bulunan bir sulama deposuna bir pompa sabit hızla su doldurmaktadır. Şekildeki grafikte, deponun doluluğu kapasitesinin kesri olarak saatlere göre verilmiştir; depodan hiç su çekilmemektedir. Deponun kapasitesi 480 litredir.\nBuna göre, 6. saatin sonunda depoda kaç litre su vardır?',
 dogru=v,yan=[(e[0],'Başlangıçtaki doluluğu (1/8) okumuş.','dikkat'),(e[1],'2. saatteki doluluğu (3/8) okumuş.','dikkat'),(e[2],'2. saat ile 6. saat arasındaki artışı (1/2) bulmuş.','dikkat'),(e[3],'4. saatteki doluluğu (5/8) okumuş.','dikkat')],
 istenen='6. saatin sonunda depodaki su (L).',ip=['Grafikte 6. saate karşılık gelen kesri oku; kapasitenin o kesri kadarını bul.'],bilgi=[GRF],sekil=SK,
 ad=[A('Saati bul','6. saatin sonuna karşılık gelen nokta.','Grafikte yatay eksende 6'),A('Kesri oku','O noktanın dikey eksendeki değeri.','7/8'),A('Litre','Kapasitenin 7/8’i.','480 × 7/8 = 420 L')],
 puf='Doğru saati oku.')

# ===== 09 orta · tarif tablosu =====
kat=Fr(6,4); un,sek=Fr(3,4),Fr(1,2); v=(un+sek)*kat
tp=un+sek
e=[(un+sek)*(6-4),(un+sek)*Fr(6+4,4),(un+sek)*Fr(6,2),(un+sek)*6]
assert v==Fr(15,8) and e==[Fr(5,2),Fr(25,8),Fr(15,4),Fr(15,2)] and len({v,*e})==5
SK=tablo_svg(['Malzeme','4 kişilik tarifte miktar'],[['Un','3/4 kg'],['Süt','2/3 L'],['Şeker','1/2 kg']])
q('0009',tipId='kdb-tablo',tip='Kesirli tablo',z='orta',alt='Tarif Tablosu',kaz='Kesirli tarif tablosunu kişi sayısına göre ölçekleyip istenen malzemelerin toplam kütlesini bulur.',kalip='tablo',
 kart='K-KSB-09 · (3/4 + 1/2) × 6/4',
 metin='Bir pastanenin kek tarifinin 4 kişilik miktarları aşağıdaki tabloda verilmiştir. Pastane, 6 kişilik kek yapacak ve her malzemeyi, kişi sayısıyla doğru orantılı artıracaktır.\nBuna göre, 6 kişilik kek için gereken un ile şekerin toplam kütlesi kaç kilogramdır?',
 dogru='15/8',yan=[('5/2','Kişi sayıları farkını kat sanmış: 5/4 × (6 − 4).','dikkat'),('25/8','Kişi sayılarını toplamış: 5/4 × 10/4.','dikkat'),('15/4','Katı 3 sanmış: 5/4 × (6 ÷ 2).','dikkat'),('15/2','4 kişilik toplam miktarı 6 ile çarpmış: 5/4 × 6.','dikkat')],
 sira=['15/8','5/2','25/8','15/4','15/2'],
 istenen='6 kişilik tarifte un ile şekerin toplamı (kg).',ip=['6 kişinin, 4 kişinin kaç katı olduğunu bul; hangi malzemelerin sorulduğuna dikkat et.'],bilgi=[OLC],sekil=SK,
 ad=[A('Katsayı','6 kişi, 4 kişinin kaç katıdır?','6/4 = 3/2'),A('Un ve şeker','4 kişilik miktarlar toplanır.','3/4 + 1/2 = 5/4 kg'),A('6 kişilik','Katsayıyla çarpılır.','5/4 × 3/2 = 15/8 kg')],
 puf='Katsayıyı kişi sayılarının oranından bul.')

# ===== 10 zor · dallanma şeması =====
giy=360; kalf=Fr(2,5); T=Fr(giy)/(kalf*Fr(3,4)); v=T*Fr(3,5)*Fr(3,4)
e=[T*Fr(3,5)*Fr(1,4),T*Fr(3,5),T*Fr(3,4),T]
assert T==1200 and v==540 and e==[180,720,900,1200] and len({v,*e})==5
o=['\\node[draw,circle,fill=vurgu!10,inner sep=3pt,align=center] (r) at (0,0) {Toplanan\\\\para};',
 '\\node[draw,rounded corners=3pt,fill=vurgu!25,inner sep=4pt] (a) at (3.4,1.8) {Gıda}; \\node[draw,rounded corners=3pt,fill=vurgu!25,inner sep=4pt] (b) at (3.4,-1.8) {Kalan};',
 "\\draw[thick] (r) -- node[above left=-1pt] {3/5} (a); \\draw[thick] (r) -- node[below left=-1pt] {2/5} (b);",
 '\\node[right] (c) at (6.5,2.7) {Çocuklar}; \\node[right] (y) at (6.5,0.9) {Yaşlılar}; \\node[right] (k) at (6.5,-0.9) {Kırtasiye}; \\node[right] (g) at (6.5,-2.7) {Giyim};',
 "\\draw[thick] (a) -- node[above=3pt] {1/4} (c.west); \\draw[thick] (a) -- node[below=3pt] {3/4} (y.west); \\draw[thick] (b) -- node[above=3pt] {1/4} (k.west); \\draw[thick] (b) -- node[below=3pt] {3/4} (g.west);"]
SK=fig('\n'.join(o))
q('0010',tipId='kdb-makine',tip='Geri izleme',z='zor',alt='Dallanma Şeması',kaz='Dallanma şemasındaki kesirlerden bilinen bir uçtan bütünü, ardından istenen ucu bulur.',kalip='hikâyeli',
 kart='K-KSB-10 · 3/5·3/4 yaşlılar; giyim 360 TL',
 metin='Bir okulun öğrencileri, deprem bölgesine yardım için bir kermes düzenlemiştir. Kampanyada toplanan para, şekildeki dallanma şemasına göre dağıtılmıştır: her dalın üzerindeki kesir, o dala gelen paranın ayrılan bölümünü gösterir ve toplanan paranın tamamı dağıtılmıştır. Giyim için ayrılan tutar 360 TL’dir.\nBuna göre, yaşlılara ayrılan tutar kaç TL’dir?',
 dogru=v,yan=[(e[0],'Yaşlılar yerine çocuklara ayrılan tutarı bulmuş.','dikkat'),(e[1],'Yaşlılar yerine gıdanın tamamını bulmuş.','dikkat'),(e[2],'Toplam paranın 3/4’ünü yaşlıların payı sanmış.','dikkat'),(e[3],'Toplanan paranın tamamını yazmış.','dikkat')],
 istenen='Yaşlılara ayrılan tutar (TL).',ip=['Giyim ucuna giden dalların kesirlerini çarparak giyimin toplam paranın kaçta kaçı olduğunu bul.'],bilgi=[DAL],sekil=SK,
 ad=[A('Giyimin kesri','Kalan, toplamın 2/5’i; giyim kalanın 3/4’ü.','2/5 × 3/4 = 3/10'),A('Toplam para','360 TL, toplamın 3/10’udur.','360 ÷ 3/10 = 1200 TL'),A('Yaşlıların kesri','Gıda 3/5; yaşlılar gıdanın 3/4’ü.','3/5 × 3/4 = 9/20'),A('Yaşlılara ayrılan','Toplamın 9/20’si.','1200 × 9/20 = 540 TL')],
 puf='Önce toplam parayı bul.')

bitir(P,'kesirsekb',UK)
