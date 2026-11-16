"""Kümeler ve Kartezyen Çarpım · ŞEKİLLİ paket (7 soru): şekil/tablo çözüm verisini taşır; her doğru ve çeldirici değer Python'da hesaplanıp assert edilir. Kardeş yok, ipucu 1."""
import sys,os,itertools
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
H.KONU='Kümeler ve Kartezyen Çarpım'
P=Parti('kumesek','Kümeler ve Kartezyen Çarpım','matd|Kümeler-Kartezyen Çarpım')
KY='ÖSYM 2018–2026 TYT Matematik (şekilli/tablolu küme soruları; yalnız mantık) · MEB 9. sınıf'
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)
def fig(body): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'+body+'\n\\end{tikzpicture}')
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)

KAR=B('Kümelerde fark ve kesişim','A \\ B, A’da olup B’de olmayan elemanlardır; A ∩ B ortak elemanlardır. Örnek: A = {1, 2, 3}, B = {3, 4} için A \\ B = {1, 2}')
KAC=B('Kartezyen çarpım','A × B, birinci bileşeni A’dan, ikinci bileşeni B’den alınan tüm sıralı ikililerin kümesidir; s(A × B) = s(A) · s(B). Örnek: A = {1, 2}, B = {a, b, c} için 6 sıralı ikili vardır')
TAB=B('Tablodan küme okuma','satır ve sütun toplamları, bilinmeyen hücreleri bulmak için kullanılır; yalnız bir gruba ait olanlar, grubun tamamından ortak kısım çıkarılarak bulunur. Örnek: 30 kişilik gruptan 12’si ortak ise yalnız bir gruba ait olanlar bu 12’yi içermez')
ALT=B('Alt küme sayısı','n elemanlı kümenin 2ⁿ alt kümesi vardır; belli bir koşulu sağlayan alt kümeler, her gruptan seçimler ayrı ayrı sayılıp çarpılarak bulunur. Örnek: 3 elemanlı bir kümenin 8 alt kümesi vardır')
VEN=B('Venn şemasında bölgeler','bölgelerdeki sayılar toplanarak kümelerin eleman sayıları bulunur; evrensel kümenin tamamı bölgelerin toplamıdır. Örnek: bölgeler 5, 3 ve 4 olan şemada evrensel küme 12 elemanlı ve içinde 5 + 3 = 8 elemanlı bir küme olabilir')

# ---------- kartlar ----------
kartla('K-KMS-01','Sayı doğrusunda aralıklardan oluşan kümeler','Dolu nokta uç noktayı kümeye katar, boş nokta katmaz; her aralıktaki tam sayılar yazılıp fark/kesişim alınır.','Boş noktayı dolu sanmak; A\\B yerine B\\A ya da A∩B almak.','kolay','şekilli',3,'kms-dogru','Sayı doğrusunda aralıklar ve kümeler')
kartla('K-KMS-02','Koordinat ızgarasında bağıntı noktaları','Izgaranın eksenlerinden A ve B okunur; dolu ve boş noktaların koordinatları koşulla karşılaştırılıp sayılır.','Dolu noktayı da saymak; tüm A×B üzerinden saymak.','kolay','şekilli',3,'kms-izgara','Koordinat ızgarasında Kartezyen çarpım')
kartla('K-KMS-03','Anket tablosu ve ortak kısım','Tablodaki toplamlardan eksik hücreler bulunur; yalnız bir gruba ait olanlar toplamdan ortak kısım çıkarılarak hesaplanır.','Ortak kısmı iki kez saymak; kulüp toplamlarını “yalnız” sanmak.','orta','tablo',4,'kms-tablo','Anket tablosu')
kartla('K-KMS-04','Eksi bileşenli Kartezyen çarpım','Eksenlerden A ve B okunur; her bileşenin işareti ve toplamı koşulla birlikte denetlenerek sıralı ikililer sayılır.','Sıfırlı ikilileri dahil etmek; işaret koşulunu unutmak.','orta','yeni nesil',4,'kms-izgara','Koordinat ızgarasında Kartezyen çarpım')
kartla('K-KMS-05','Kartlardan oluşan kümenin alt kümeleri','Kartlar tek ve çift olarak ayrılır; her gruptan en az bir eleman seçilen alt kümeler, grupların boş olmayan alt küme sayıları çarpılarak bulunur.','Boş alt kümeyi iki kez çıkarmak; yalnız ikili çiftleri saymak.','orta','hikâyeli',4,'kms-altkume','Kartlarla alt küme sayma')
kartla('K-KMS-06','Üç kümeli Venn şeması okuma','Bölgelerdeki sayılar kümelerin eleman sayılarını verir; eşitlikten bilinmeyen bulunur, kalan evrensel kümeden çıkarılır.','Kesişim bölgesini eksik toplamak; bilinmeyeni tek bölgeye bağlamak.','zor','hikâyeli',5,'kms-venn3','Üç kümeli Venn şeması')
kartla('K-KMS-07','Taralı bölge ve cebirsel Venn','Bölgelerdeki ifadelerin toplamı evrensel kümeye eşitlenip bilinmeyen bulunur; taralı bölgeler toplanır.','Taralı bölgeyi yanlış okumak; dışarıdaki bölgeyi unutmak.','orta','şekilli',5,'kms-venn2','İki kümeli Venn ve taralı bölge')

# ================= 01 kolay · sayı doğrusunda aralıklar =================
A1=range(-4,2); B1=range(0,7)  # A=[-4,2), B=(-1,6]
sa=set(A1); sb=set(B1)
v=sum(sa-sb); e=[sum(sa-(set(range(-1,7)))),sum(sa&sb),sum(sa|sb),sum(sb-sa)]
assert v==-10 and e==[-9,1,11,20] and len({v,*e})==5
sx=0.62; X=lambda t:(t+5)*sx
o=[f'\\draw[-{{Stealth}}] ({X(-5.6):.3f},0) -- ({X(7.6):.3f},0);']
for t in range(-5,8): o.append(f'\\draw ({X(t):.3f},-0.1) -- ({X(t):.3f},0.1); \\node[below=3pt] at ({X(t):.3f},-0.1) {{${t}$}};')
def aralik(a,b,ac,bc,y,ad):
    r=[f'\\draw[line width=2pt] ({X(a):.3f},{y}) -- ({X(b):.3f},{y});']
    for t,cl in ((a,ac),(b,bc)):
        r.append(f'\\draw[dashed,thin] ({X(t):.3f},{y}) -- ({X(t):.3f},0);')
        r.append(f'\\filldraw[fill={"black" if cl else "none"},thick] ({X(t):.3f},{y}) circle (0.1);')
    r.append(f'\\node[left=6pt] at ({X(a):.3f},{y}) {{{ad}}};')
    return '\n'.join(r)
o.append(aralik(-4,2,True,False,1.0,'$A$')); o.append(aralik(-1,6,False,True,1.7,'$B$'))
SK=fig('\n'.join(o))
q('0001',tipId='kms-dogru',tip='Sayı doğrusunda aralıklar ve kümeler',z='kolay',alt='Sayı Doğrusunda Kümeler',kaz='Sayı doğrusunda gösterilen aralıklardaki tam sayılardan kümeleri yazıp fark kümesinin elemanları toplamını bulur.',kalip='şekilli',
 kart='K-KMS-01 (sayı doğrusunda aralıklar) · A = [−4, 2), B = (−1, 6] → A \\ B',
 metin='A ve B kümeleri, sayı doğrusunda gösterilen aralıklardaki tam sayılardan oluşmaktadır (dolu nokta uç noktanın aralığa dahil olduğunu, içi boş nokta ise dahil olmadığını gösterir).\nBuna göre, A \\ B kümesinin elemanlarının toplamı kaçtır?',
 dogru=v,yan=[(e[0],'B’nin sol ucundaki boş noktayı dolu sanıp −1’i B’ye katmış: A \\ B = {−4, −3, −2}.','dikkat'),(e[1],'Fark yerine kesişimi almış: A ∩ B = {0, 1}.','bilgi'),(e[2],'Fark yerine birleşimi almış: A ∪ B = {−4, …, 6}.','bilgi'),(e[3],'Farkı ters almış: B \\ A = {2, 3, 4, 5, 6}.','bilgi')],
 istenen='A \\ B kümesinin elemanları toplamı.',ip=['Her aralıktaki tam sayıları ayrı ayrı yaz; uç noktalarda dolu ya da boş olmasına dikkat et.'],bilgi=[KAR],sekil=SK,
 ad=[A('A ve B’yi yaz','A’nın −4’teki ucu dolu, 2’deki ucu boştur; B’nin −1’deki ucu boş, 6’daki ucu doludur.','A = {−4, −3, −2, −1, 0, 1} · B = {0, 1, 2, 3, 4, 5, 6}'),A('Farkı bul','A’da olup B’de olmayanlar alınır.','A \\ B = {−4, −3, −2, −1}'),A('Topla','Elemanlar toplanır.','−4 − 3 − 2 − 1 = −10')],
 puf='Dolu nokta aralığa dahil, boş nokta dahil değildir; kümeleri tek tek yazmak en güvenli yoldur.')

# ================= 02 kolay · koordinat ızgarası, bağıntı =================
Aa=[1,2,3,4,5,6]; Bb=[1,2,3,4]; R_=lambda a,b:(a*b)%2==0
pts=list(itertools.product(Aa,Bb))
v=sum(1 for a,b in pts if not R_(a,b) and a>b)
e=[sum(1 for a,b in pts if not R_(a,b)),sum(1 for a,b in pts if a>b),sum(1 for a,b in pts if not R_(a,b) and a==5),sum(1 for a,b in pts if not R_(a,b) and a>=b)]
assert v==3 and e==[6,14,2,5] and len({v,*e})==5
s=0.95; o=[f'\\draw[-{{Stealth}}] (0,0) -- ({7.2*s:.3f},0) node[right] {{$A$}};',f'\\draw[-{{Stealth}}] (0,0) -- (0,{5.1*s:.3f}) node[above] {{$B$}};']
for a in Aa: o.append(f'\\draw ({a*s:.3f},-0.08) -- ({a*s:.3f},0.08); \\node[below=3pt] at ({a*s:.3f},0) {{{a}}};')
for b in Bb: o.append(f'\\draw (-0.08,{b*s:.3f}) -- (0.08,{b*s:.3f}); \\node[left=3pt] at (0,{b*s:.3f}) {{{b}}};')
for a,b in pts: o.append(f'\\filldraw[fill={"black" if R_(a,b) else "none"},thick] ({a*s:.3f},{b*s:.3f}) circle (0.12);')
o.append(f'\\filldraw[fill=black] ({0.4*s:.3f},{-1.15*s:.3f}) circle (0.1); \\node[right] at ({0.5*s:.3f},{-1.15*s:.3f}) {{R’ye ait}}; \\draw[thick] ({3.3*s:.3f},{-1.15*s:.3f}) circle (0.1); \\node[right] at ({3.4*s:.3f},{-1.15*s:.3f}) {{R’ye ait değil}};')
SK=fig('\n'.join(o))
q('0002',tipId='kms-izgara',tip='Koordinat ızgarasında Kartezyen çarpım',z='kolay',alt='Izgarada Kartezyen Çarpım',kaz='Izgaradaki noktaların koordinatlarını okuyup bir bağıntıya ait olmayan sıralı ikilileri koşula göre sayar.',kalip='şekilli',
 kart='K-KMS-02 (koordinat ızgarası) · A×B 24 nokta; R: bileşen çarpımı çift',
 metin='Şekilde, A kümesi yatay eksendeki, B kümesi düşey eksendeki sayılardan oluşan A × B kümesinin bütün elemanları nokta olarak gösterilmiştir. Bu elemanlardan bir R bağıntısına ait olanlar dolu, ait olmayanlar içi boş nokta ile işaretlenmiştir.\nBuna göre, R’ye ait olmayan elemanlardan kaç tanesinin birinci bileşeni ikinci bileşeninden büyüktür?',
 dogru=v,yan=[(e[0],'Koşulu unutmuş: içi boş bütün noktaları saymış.','dikkat'),(e[1],'R’yi hiç dikkate almamış: A × B’de birinci bileşeni ikinci bileşeninden büyük bütün ikilileri saymış.','dikkat'),(e[2],'Koşulu sağlayan boş noktalardan yalnız birinci bileşeni 5 olanları saymış: (5, 1) ve (5, 3).','dikkat'),(e[3],'Koşulu “büyük ya da eşit” almış: (1, 1) ve (3, 3) de sayılmış.','dikkat')],
 istenen='R’ye ait olmayan ve birinci bileşeni ikinci bileşeninden büyük olan eleman sayısı.',ip=['İçi boş noktaların koordinatlarını eksenlerden oku; her birinde iki bileşeni karşılaştır.'],bilgi=[KAC],sekil=SK,
 ad=[A('Boş noktaları bul','Boş noktalar, R’ye ait olmayan elemanlardır.','(1,1), (1,3), (3,1), (3,3), (5,1), (5,3) — 6 nokta'),A('Koşulu uygula','Birinci bileşeni ikinciden büyük olanlar seçilir.','(3,1): 3 > 1 ✓ · (5,1) ✓ · (5,3) ✓ · (1,·) ✗ · (3,3) ✗'),A('Say','Koşulu sağlayanlar sayılır.','3 eleman')],
 puf='Önce hangi noktaların istendiğini (boş noktalar) belirle, sonra yalnız onların koordinatlarını karşılaştır.')

# ================= 03 orta · anket tablosu =================
N,T,M,Mnt=60,25,28,11
both=M-Mnt; Tonly=T-both; neither=N-(T+M-both)
assert both==17 and Tonly==8 and neither==24 and Tonly+Mnt==19
tabsum=sum([both,Tonly,Mnt,neither]); assert tabsum==N
v=Tonly+Mnt; e=[Tonly,both,neither,T+M-both]
assert e==[8,17,24,36] and len({v,*e})==5
SK=tablo_svg(['','Müzik üyesi','Müzik üyesi değil','Toplam'],[['Tiyatro üyesi','?','?','25'],['Tiyatro üyesi değil','11','?','?'],['Toplam','28','?','60']])
q('0003',tipId='kms-tablo',tip='Anket tablosu',z='orta',alt='Anket Tablosu',kaz='Tablodaki toplamlardan eksik hücreleri bulup yalnız bir kulübe üye olanları hesaplar.',kalip='tablo',
 kart='K-KMS-03 (anket tablosu) · 60 öğrenci, tiyatro 25, müzik 28, yalnız müzik 11',
 metin='Bir okulda 60 öğrenciye tiyatro ve müzik kulüplerine üyelikleri sorulmuş, sonuçlar aşağıdaki tabloda özetlenmiştir. Tablodaki “?” işaretli hücrelerin değerleri verilmemiştir. Öğrencilerin her biri anketteki iki sorunun ikisini de yanıtlamıştır.\nBuna göre, bu iki kulüpten yalnızca birine üye olan kaç öğrenci vardır?',
 dogru=v,yan=[(e[0],'Yalnız tiyatro kulübüne üye olanları bulup bırakmış.','dikkat'),(e[1],'İki kulübe birden üye olanları (28 − 11) yazmış.','dikkat'),(e[2],'Hiçbir kulübe üye olmayanları (35 − 11) bulmuş.','dikkat'),(e[3],'En az birine üye olanları (25 + 28 − 17) yazmış; ortak kısmı yalnız bir kez çıkarmış.','bilgi')],
 istenen='Yalnızca bir kulübe üye olan öğrenci sayısı.',ip=['Tabloda müzik üyesi olup tiyatro üyesi olmayanların sayısı verilmiş; iki kulübe birden üye olanları bu bilgiyle bul.'],bilgi=[TAB],sekil=SK,
 ad=[A('İki kulübe üyeler','Müzik üyelerinden tiyatroya üye olmayanlar çıkarılır.','28 − 11 = 17'),A('Yalnız tiyatro','Tiyatro üyelerinden ortak kısım çıkarılır.','25 − 17 = 8'),A('Yalnız müzik','Tabloda doğrudan verilmiştir.','11'),A('Topla','Yalnız bir kulübe üye olanlar.','8 + 11 = 19')],
 puf='Yalnız bir kulübe üye olanlar = (iki kulübün üye toplamı) − 2 · (ortak üye sayısı).')

# ================= 04 orta · eksi bileşenli koordinat düzlemi =================
A4=[-3,-1,2,4,5]; B4=[-5,-2,1,3]; P4=list(itertools.product(A4,B4)); ok4=lambda a,b:a+b>0 and a*b<0
v=sum(1 for a,b in P4 if ok4(a,b))
e=[sum(1 for a,b in P4 if a*b<0),sum(1 for a,b in P4 if a+b>0),sum(1 for a,b in P4 if a+b>=0 and a*b<0),sum(1 for a,b in P4 if a+b>0 and a*b>0)]
assert v==3 and e==[10,9,7,6] and len({v,*e})==5,(v,e)
s=0.72; XX=lambda t:t*s
o=[f'\\draw[-{{Stealth}}] ({XX(-4.4):.3f},0) -- ({XX(6.1):.3f},0) node[right] {{$A$}};',f'\\draw[-{{Stealth}}] (0,{XX(-5.3):.3f}) -- (0,{XX(4.2):.3f}) node[above] {{$B$}};']
for a in A4: o.append(f'\\draw[dotted,thin] ({XX(a):.3f},{XX(-5.3):.3f}) -- ({XX(a):.3f},{XX(3.7):.3f}); \\node[below=2pt] at ({XX(a):.3f},{XX(-5.3):.3f}) {{${a}$}};')
for b in B4: o.append(f'\\draw[dotted,thin] ({XX(-3.7):.3f},{XX(b):.3f}) -- ({XX(5.7):.3f},{XX(b):.3f}); \\node[left=2pt] at ({XX(-3.7):.3f},{XX(b):.3f}) {{${b}$}};')
for a,b in P4: o.append(f'\\fill ({XX(a):.3f},{XX(b):.3f}) circle (0.1);')
SK=fig('\n'.join(o))
q('0004',tipId='kms-izgara',tip='Koordinat ızgarasında Kartezyen çarpım',z='orta',alt='Koordinat Düzleminde Kartezyen Çarpım',kaz='Koordinat düzlemindeki A × B noktalarından tanımlı kurala uyan sıralı ikilileri sayar.',kalip='yeni nesil',
 kart='K-KMS-04 (eksi bileşenli koordinat düzlemi) · A={−3,−1,2,4,5}, B={−5,−2,1,3}; toplamı > 0 ve çarpımı < 0',
 metin='Şekilde, A kümesi yatay eksendeki, B kümesi düşey eksendeki sayılardan oluşan A × B kümesinin bütün elemanları gösterilmiştir. Bileşenlerinin toplamı sıfırdan büyük, çarpımı sıfırdan küçük olan sıralı ikiliye “dengeli ikili” denmektedir.\nBuna göre, A × B kümesinin kaç elemanı dengeli ikilidir?',
 dogru=v,yan=[(e[0],'Yalnız çarpım koşuluna bakmış: bileşenleri zıt işaretli bütün ikilileri (4 + 6) saymış.','dikkat'),(e[1],'Yalnız toplam koşuluna bakmış: toplamı pozitif bütün ikilileri saymış.','dikkat'),(e[2],'Toplamı sıfır olan ikilileri de “pozitif” saymış: (−3,3), (−1,1), (2,−2), (5,−5) eklenmiş.','dikkat'),(e[3],'Çarpım koşulunu ters yorumlamış: toplamı pozitif ve çarpımı da pozitif olanları saymış.','dikkat')],
 istenen='Dengeli ikili sayısı.',ip=['Önce işaretleri zıt olan ikilileri bul; sonra bunların toplamlarını tek tek denetle.'],bilgi=[KAC],sekil=SK,
 ad=[A('A ve B’yi oku','Eksenlerdeki noktalardan kümeler yazılır.','A = {−3, −1, 2, 4, 5} · B = {−5, −2, 1, 3}'),A('Çarpımı negatif olanlar','Biri negatif, biri pozitif bileşenli ikililer.','(−3,1) (−3,3) (−1,1) (−1,3) (2,−5) (2,−2) (4,−5) (4,−2) (5,−5) (5,−2) → 10 ikili'),A('Toplamı pozitif olanlar','Bu ikililerin toplamı sıfırdan büyük mü?','(−1,3): 2 ✓ · (4,−2): 2 ✓ · (5,−2): 3 ✓ · diğerleri ≤ 0'),A('Say','Koşulu sağlayanlar sayılır.','3 ikili')],
 puf='İki koşul birlikte aranıyorsa önce birini uygulayıp elenmeyen ikilileri öbür koşula göre denetle; toplamı 0 olanlar “sıfırdan büyük” değildir.')

# ================= 05 orta · kartlarla alt küme =================
kart5=[3,4,7,8,11,12,15]; tek=[x for x in kart5 if x%2]; cift=[x for x in kart5 if x%2==0]
alt=lambda S:[c for r in range(len(S)+1) for c in itertools.combinations(S,r)]
v=sum(1 for S in alt(kart5) if any(x%2 for x in S) and any(x%2==0 for x in S))
assert v==105==(2**4-1)*(2**3-1)
e=[2**7-2**3-2**4,len(tek)*len(cift),2**4*(2**3-1),2**7-1]
assert e==[104,12,112,127] and len({v,*e})==5
o=[]
for i,x in enumerate(kart5):
    cx=i*1.55; o.append(f'\\draw[thick,rounded corners=3pt] ({cx:.2f},0) rectangle ({cx+1.3:.2f},1.8); \\node[font=\\Large\\bfseries] at ({cx+0.65:.2f},0.9) {{{x}}};')
SK=fig('\n'.join(o))
q('0005',tipId='kms-altkume',tip='Kartlarla alt küme sayma',z='orta',alt='Kartlarla Alt Küme',kaz='Kartlardaki sayılardan oluşan kümenin, tek ve çift eleman içeren alt kümelerini sayar.',kalip='hikâyeli',
 kart='K-KMS-05 (kartlarla alt küme) · {3, 4, 7, 8, 11, 12, 15}; en az bir tek ve bir çift',
 metin='Bir matematik öğretmeni, üzerlerine birer doğal sayı yazdığı yedi kartı sıraya dizmiştir. Kartlardaki sayılar A kümesinin elemanlarıdır. Öğretmen, öğrencilerden A kümesinin alt kümelerini oluşturmalarını istemiş ve “İçinde hem tek sayı hem de çift sayı bulunan alt kümeler” için ödül vermiştir.\nBuna göre, kaç farklı alt küme ödül kazanır?',
 dogru=v,yan=[(e[0],'Tüm alt kümelerden yalnız tek ve yalnız çift olanları çıkarıp boş kümenin iki kez çıkarıldığını (+1) unutmuş: 128 − 16 − 8.','dikkat'),(e[1],'Yalnız bir tek ile bir çift seçilen ikili alt kümeleri saymış: 4 · 3.','dikkat'),(e[2],'Tek sayılardan seçimi boş da olabilir saymış: 2⁴ · (2³ − 1).','islem'),(e[3],'Boş küme dışındaki bütün alt kümeleri saymış: 2⁷ − 1.','dikkat')],
 istenen='Hem tek hem çift sayı içeren alt küme sayısı.',ip=['Kartlardaki tek ve çift sayıların kaç tane olduğunu ayır; her gruptan seçimi ayrı düşün.'],bilgi=[B('Tek ve çift sayı','2’ye tam bölünen sayılar çifttir, bölünmeyenler tektir. Örnek: 10 çift, 9 tek sayıdır'),ALT],sekil=SK,
 ad=[A('Kartları ayır','Şekildeki sayılardan tekler ve çiftler.','Tek: 3, 7, 11, 15 (4 kart) · Çift: 4, 8, 12 (3 kart)'),A('Tek sayı seçimleri','Tek gruptan en az bir eleman: boş seçim çıkarılır.','2⁴ − 1 = 15'),A('Çift sayı seçimleri','Çift gruptan en az bir eleman.','2³ − 1 = 7'),A('Birleştir','Seçimler birbirinden bağımsızdır; çarpılır.','15 · 7 = 105')],
 puf='“En az bir tek ve en az bir çift” koşulunda her grubun boş olmayan alt kümeleri ayrı sayılıp çarpılır.')

# ================= 06 zor · üç kümeli Venn =================
a_,b_,c_,ab,bc,ac,abc=6,4,6,None,3,5,2
x=(bc+c_+ac+abc)-(a_+ac+abc); assert x==3  # s(A)=s(C)
ab=x; U=40; kapsam=a_+b_+c_+ab+bc+ac+abc; v=U-kapsam; assert kapsam==29 and v==11
sA=a_+ab+ac+abc; sC=c_+bc+ac+abc; assert sA==sC==16
e=[U-(a_+b_+c_+bc+ac+abc),U-(a_+b_+c_+(sC-a_-ac)+bc+ac+abc),kapsam,U-(a_+b_+c_+(sC-a_)+bc+ac+abc)]
assert e==[14,9,29,4] and len({v,*e})==5,e
cA,cB,cC=(1.9,2.9),(3.9,2.9),(2.9,1.2); r=1.5
o=[f'\\draw[thick] (-0.7,-0.9) rectangle (6.5,5.1); \\node at (-0.35,4.75) {{$E$}};']
for (cx,cy),nm,pos in ((cA,'A',(0.35,4.3)),(cB,'B',(5.45,4.3)),(cC,'C',(5.0,0.0))):
    o.append(f'\\draw[thick] ({cx},{cy}) circle ({r}); \\node[font=\\large\\bfseries] at ({pos[0]},{pos[1]}) {{{nm}}};')
for (px,py),t in (((1.15,3.3),a_),((4.65,3.3),b_),((2.9,0.15),c_),((2.9,3.55),'$x$'),((3.95,1.8),bc),((1.85,1.8),ac),((2.9,2.3),abc)):
    o.append(f'\\node[font=\\normalsize] at ({px},{py}) {{{t}}};')
SK=fig('\n'.join(o))
q('0006',tipId='kms-venn3',tip='Üç kümeli Venn şeması',z='zor',alt='Üç Kümeli Venn',kaz='Üç kümeli Venn şemasındaki bölge sayılarından bilinmeyeni bulup hiçbir kümede olmayanları hesaplar.',kalip='hikâyeli',
 kart='K-KMS-06 (üç kümeli Venn) · 40 öğrenci, T–R eşit üye → x = 3, dışarıda 11',
 metin='Bir sınıftaki 40 öğrencinin tiyatro (A), müzik (B) ve resim (C) kulüplerine üyelikleri şekildeki Venn şemasında gösterilmiştir; bölgelerdeki sayılar o bölgedeki öğrenci sayısıdır, x ise yalnız tiyatro ve müzik kulüplerine üye olan öğrenci sayısıdır. Tiyatro ve resim kulüplerinin üye sayıları birbirine eşittir.\nBuna göre, bu üç kulübün hiçbirine üye olmayan kaç öğrenci vardır?',
 dogru=v,yan=[(e[0],'x bölgesini toplamdan çıkarıp unutmuş: 40 − 26.','dikkat'),(e[1],'s(A)’yı yazarken üçlü kesişimi eksik almış (6 + x + 5 = 16 → x = 5) ve toplamı buna göre bulmuş.','dikkat'),(e[2],'Sorulan yerine en az bir kulübe üye olanların sayısını (29) vermiş.','bilgi'),(e[3],'x’i s(C) − 6 = 10 diye bulmuş (A’nın yalnız bölgesini ve kesişimleri eksik yazmış).','dikkat')],
 istenen='Hiçbir kulübe üye olmayan öğrenci sayısı.',ip=['Eşit olan iki kümenin eleman sayılarını bölgeleri toplayarak yaz; böylece x’i bulabilirsin.'],bilgi=[VEN],sekil=SK,
 ad=[A('Eşitliği kur','A’nın bölgeleri: 6, x, 5, 2 ; C’nin bölgeleri: 6, 3, 5, 2.','s(A) = 13 + x ve s(C) = 16'),A('x’i bul','s(A) = s(C).','13 + x = 16 → x = 3'),A('Bölgeleri topla','Yedi bölgedeki öğrenciler.','6 + 4 + 6 + 3 + 3 + 5 + 2 = 29'),A('Dışarıyı bul','Evrensel kümeden çıkarılır.','40 − 29 = 11')],
 puf='Şemada hiçbir kümeye ait olmayanlar, evrensel kümeden yedi bölgenin toplamı çıkarılarak bulunur.')

# ================= 07 zor · cebirsel Venn, taralı bölge =================
x=6; rA,rI,rB,rD=2*x,x+1,3*x-5,x+2; assert rA+rI+rB+rD==40 and 7*x-2==40
v=40-rA; e=[rI,rA,rB+rD,rI+rB+x]
assert v==28 and e==[7,12,21,26] and len({v,*e})==5
Ra,Rb,r=(2.45,2.1),(4.75,2.1),1.65
o=[f'\\fill[fill=vurgu!25,even odd rule] (0,0) rectangle (7.2,4.2) ({Ra[0]},{Ra[1]}) circle ({r});',
   f'\\begin{{scope}}\\clip ({Ra[0]},{Ra[1]}) circle ({r}); \\fill[fill=vurgu!25] ({Rb[0]},{Rb[1]}) circle ({r}); \\end{{scope}}',
   '\\draw[thick] (0,0) rectangle (7.2,4.2); \\node at (0.3,3.85) {$E$};',
   f'\\draw[thick] ({Ra[0]},{Ra[1]}) circle ({r}); \\draw[thick] ({Rb[0]},{Rb[1]}) circle ({r});',
   f'\\node[font=\\large\\bfseries] at (1.0,3.65) {{$A$}}; \\node[font=\\large\\bfseries] at (6.3,3.65) {{$B$}};',
   f'\\node at (1.55,2.1) {{$2x$}}; \\node at (3.6,2.1) {{$x+1$}}; \\node at (5.75,2.1) {{$3x-5$}}; \\node at (0.65,0.5) {{$x+2$}};']
SK=fig('\n'.join(o))
q('0007',tipId='kms-venn2',tip='İki kümeli Venn ve taralı bölge',z='orta',alt='Cebirsel Venn ve Taralı Bölge',kaz='Venn şemasındaki cebirsel bölge ifadelerinden bilinmeyeni bulup taralı bölgenin eleman sayısını hesaplar.',kalip='şekilli',
 kart='K-KMS-07 (cebirsel Venn, taralı bölge) · E = 40, x = 6, taralı = (A \\ B)′',
 metin='E evrensel kümesinin 40 elemanı, A ve B kümeleri ile şekildeki gibi dört bölgeye ayrılmıştır; bölgelerin yanındaki ifadeler o bölgedeki eleman sayılarını göstermektedir ve x bir doğal sayıdır.\nBuna göre, taralı bölgenin eleman sayısı kaçtır?',
 dogru=v,yan=[(e[0],'Taralı bölge yerine yalnız A ∩ B bölgesini okumuş: x + 1.','dikkat'),(e[1],'Taralı olmayan bölgeyi (A \\ B) saymış: 2x.','dikkat'),(e[2],'A ve A ∩ B’yi taralı dışı sanmış; yalnız B \\ A ile dışarıdaki bölgeyi toplamış: 13 + 8.','dikkat'),(e[3],'Dışarıdaki bölgenin ifadesini x + 2 yerine x okumuş: 7 + 13 + 6.','dikkat')],
 istenen='Taralı bölgenin eleman sayısı.',ip=['Dört bölgedeki ifadelerin toplamı evrensel kümenin eleman sayısına eşittir; önce x’i bul, sonra hangi bölgelerin taralı olduğuna bak.'],bilgi=[VEN],sekil=SK,
 ad=[A('Denklemi kur','Dört bölgenin toplamı evrensel kümeye eşittir.','2x + (x + 1) + (3x − 5) + (x + 2) = 40'),A('x’i bul','Benzer terimleri topla.','7x − 2 = 40 → x = 6'),A('Bölgeleri hesapla','x yerine 6 yazılır.','A \\ B = 12 · A ∩ B = 7 · B \\ A = 13 · dışarısı = 8'),A('Taralı bölgeyi oku','A \\ B dışındaki bütün bölgeler taralıdır.','7 + 13 + 8 = 28'),A('Kontrol et','Evrensel kümeden A \\ B çıkarılır.','40 − 12 = 28')],
 puf='Taralı bölge, bölgelerin hangileri olduğu şekilden okunarak toplanır; bütünden taralı olmayan bölge çıkarmak da aynı sonucu verir.')

bitir(P,'kumesek','matd|Kümeler-Kartezyen Çarpım')
