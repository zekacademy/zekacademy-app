"""Rutin Olmayan Problemler · ŞEKİLLİ ek paket b (10 soru): şekil çözüm verisini taşır; her doğru ve çeldirici değer kodla (kaba kuvvet/tarama) assert edilir. Kardeş yok, ipucu 1."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
from math import cos,sin,radians,comb,gcd,factorial as fa
from itertools import product,permutations,combinations
from fractions import Fraction as Fr
import heapq
H.KONU='Rutin Olmayan Problemler'
UK='prob|Rutin Olmayan Problemleri'
P=Parti('rutinsekb','Rutin Olmayan Problemler',UK)
KY='ÖSYM 2018–2026 TYT Matematik (şekilli rutin olmayan/muhakeme soruları; yalnız mantık) · MEB 9–10. sınıf'
SP=[]
def spec(no,dogru,aday,**k): SP.append((no,dogru,aday,k))
def fig(body): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'+body+'\n\\end{tikzpicture}')
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)
def olus(sp):
    """Her soruda doğru şıkkın olası sıraları; A–E harflerini 2'şer dağıtır."""
    fe=[]
    for no,d,ad,k in sp:
        assert len({d,*[a[0] for a in ad]})==len(ad)+1,(no,d,[a[0] for a in ad])
        sm=sum(1 for a in ad if a[0]<d); lg=len(ad)-sm
        fe.append([r for r in range(5) if r<=sm and 4-r<=lg])
    sol=[None]; cnt_l=[]
    def bt(i,cnt):
        if i==len(sp): sol[0]=list(cnt_l); return True
        for r in fe[i][i%len(fe[i]):]+fe[i][:i%len(fe[i])]:
            if cnt[r]<2:
                cnt[r]+=1; cnt_l.append(r)
                if bt(i+1,cnt): return True
                cnt[r]-=1; cnt_l.pop()
        return False
    assert bt(0,[0]*5),fe
    return sol[0]

# ---------- bilgi kartları (örnekler soruların kurgusundan farklı) ----------
PIR=B('Sayı piramidi','her kutudaki sayı, hemen altındaki iki kutudaki sayıların toplamıdır; bilinmeyen sayı için denklem kurulabilir. Örnek: altındaki kutularda 2 ve 8 yazan kutuda 10 yazar')
AKI=B('Akış şeması','yuvarlatılmış kutu başlangıç ve bitişi, dikdörtgen işlemi, eşkenar dörtgen ise evet/hayır sorusunu gösterir; oklar sırayı belirler. Örnek: “n > 5 mi?” sorusuna evet denirse bir kola, hayır denirse diğer kola gidilir')
TEC=B('Tek ve çift sayılar','çift sayı 2’ye tam bölünür, tek sayı 2’ye bölünürse 1 kalır. Örnek: 18 çifttir, 19 tektir')
PER=B('Periyodik düzen','bir düzen her T birimde aynen yineleniyorsa t. anın durumu, t sayısının T’ye bölümünden kalana bağlıdır. Örnek: 5 günde bir tekrarlanan bir nöbet düzeninde 17. gün ile 2. gün aynı durumdadır')
EKO=B('Ortak tekrar','iki düzenin birlikte başa dönmesi için geçen süre, ikisinin periyotlarının ortak katıdır; ilk kez birlikte başa dönmesi en küçük ortak kattır. Örnek: 4 ve 6 dakikada bir çalan iki zil 12 dakikada birlikte başa döner')
KUP=B('Küp','küpün 6 yüzü ve 8 köşesi vardır; her köşede 3 yüz birleşir. Örnek: bir zarın yüzlerindeki toplam sayı noktası sayısı 21’dir')
YON=B('Yön ve dönüş','sağa 90° dönmek, bakılan yönü saat yönünde çeyrek tur çevirir; dört çeyrek dönüş tam bir turdur. Örnek: batıya bakan biri sağa dönünce kuzeye bakar')
MAN=B('Izgarada uzaklık','ızgara çizgileri boyunca uzaklık, yatay ve dikey uzaklıkların toplamıdır. Örnek: (1, 2) noktasından (4, −2) noktasına uzaklık 3 + 4 = 7 birimdir')
DIS=B('Dişli çarklar','birbirine geçen dişlilerde aynı anda geçen diş sayısı eşittir; bir dişli n tur dönerken diş sayısı farklı bir dişli kendi diş sayısına göre başka sayıda tur döner. Örnek: 10 dişli bir çark 3 tur dönünce 15 dişli çark 2 tur döner')
MAY=B('Komşuluk sayıları','bir karenin komşuları, kendisine yatay, dikey ve çapraz bitişik en çok 8 karedir; köşedeki karenin 3, kenardaki karenin 5 komşusu vardır. Örnek: 2 yazan bir karenin komşularının tam ikisinde mayın vardır')
TOP=B('Eşit toplam düzeni','her sayı bir kez kullanılıyorsa bütün sayıların toplamı bellidir; bir sayı birden çok toplamda yer alıyorsa toplamlar birbirine eklenince o sayı birden çok kez sayılır. Örnek: 1, 2, 3 sayılarının toplamı 6’dır')
UCG=B('Şekilde üçgen sayma','üçgenin üç kenarı da şekildeki doğru parçalarının üzerindedir; üç köşe doğrusal olmamalıdır. Üçgenleri tepe noktasına ya da bir kenarına göre gruplayıp tekrar etmeden saymak gerekir. Örnek: bir doğru parçası üzerinde 3 nokta varsa bunlardan 2’sini seçmek 3 parça verir')
YOL=B('En kısa yol','bir yolun uzunluğu, kullandığı kenarların uzunlukları toplamıdır; farklı yollar karşılaştırılırken “bir noktadan bir kez geçme” gibi koşullar dikkate alınır. Örnek: 3 + 4 = 7 km uzunluğundaki yol ile 9 km uzunluğundaki yoldan kısa olan 7 km’lik olandır')

# ---------- kartlar ----------
kartla('K-RSB-01','Sayı piramidi','Alt sıradaki her sayının üst kutulara kaç kez katkı yaptığı sayılır; bilinmeyen için denklem kurulur.','Katkı sayılarını eşit sanmak; bilinmeyen katsayısını unutmak.','kolay','yeni nesil',3,'rsb-kural','İşlem kuralı ve akış (piramit, şema)')
kartla('K-RSB-02','Akış şeması','Çıkıştan geriye doğru her kolun işlemi tersine çevrilir; bulunan değerin kolun koşulunu sağlayıp sağlamadığı kontrol edilir.','Koşulu denemeden iki kolun tersini de geçerli saymak.','kolay','yeni nesil',3,'rsb-kural','İşlem kuralı ve akış (piramit, şema)')
kartla('K-RSB-03','Işık çizelgesi','Düzenin periyodu belirlenir; ortak periyot boyunca üç lambanın birlikte yanık olduğu saniyeler sayılır, toplam süreye ölçeklenir.','Yalnız bir periyodu saymak; periyot sayısını cevap sanmak.','orta','hikâyeli',4,'rsb-periyot','Tekrarlayan düzenler')
kartla('K-RSB-04','Zar açınımı','Açınımda katlayınca karşılıklı gelen yüzler belirlenir; bir köşedeki üç yüz her karşılıklı çiftten birer yüz alır.','Bitişik karelerin karşılıklı olduğunu sanmak; en büyük üç sayıyı almak.','orta','hikâyeli',4,'rsb-mekan','Küp ve şekil muhakemesi')
kartla('K-RSB-05','Robot yolu','Bir program turunun yer değiştirmesi ve dönüşü bulunur; dönüş sayesinde tekrar eden yer değiştirmeler çevrilir ve toplanır.','Dönüşü hesaba katmadan yer değiştirmeyi katlamak; kalan tur sayısını yanlış almak.','orta','hikâyeli',5,'rsb-periyot','Tekrarlayan düzenler')
kartla('K-RSB-06','Dişli zinciri','Her dişlinin dönüş sayısı diş oranından yazılır; hepsinin tam sayı olması için ortak kat aranır.','Diş sayılarının EKOK’unu cevap sanmak; yalnız iki dişliyi hesaba katmak.','orta','hikâyeli',4,'rsb-periyot','Tekrarlayan düzenler')
kartla('K-RSB-07','Mayın tarlası','Sayılı kareler mayınsızdır; en kısıtlı sayıdan başlanarak komşu karelerdeki mayınlar belirlenir.','Sayıların toplamını mayın sayısı sanmak; sayılı kareyi mayın saymak.','zor','yeni nesil',5,'rsb-cikarim','Mantıksal yerleştirme ve çıkarım')
kartla('K-RSB-08','Kenar toplamı düzeni','Verilenlerden ortak kenar toplamı bulunur; kalan sayılar kenar denklemleriyle yerleştirilir.','İki kenarı sağlayıp üçüncüyü denetlememek; ortak toplamı yanlış bulmak.','zor','yeni nesil',5,'rsb-cikarim','Mantıksal yerleştirme ve çıkarım')
kartla('K-RSB-09','Şekilde üçgen sayma','Üçgenler tepe noktasına ya da bir kenara göre gruplanarak tekrarsız sayılır.','Yalnız küçük üçgenleri saymak; üçgenleri iki kez saymak.','zor','yeni nesil',4,'rsb-mekan','Küp ve şekil muhakemesi')
kartla('K-RSB-10','Koşullu en kısa yol','Zorunlu noktadan geçen yollar arasından, aynı noktadan iki kez geçmeyen en kısası seçilir.','Aynı noktadan iki kez geçen yolu geçerli saymak; koşulsuz en kısa yolu yazmak.','zor','hikâyeli',5,'rsb-yol','Koşullu en kısa yol')

# ================= 01 kolay · sayı piramidi =================
a_,b_,c_,x_=3,1,3,11
top=a_+3*x_+3*b_+c_; assert top==42
alt=[a_,x_,b_,c_]; r2=[alt[i]+alt[i+1] for i in range(3)]; r3=[r2[i]+r2[i+1] for i in range(2)]; assert r3[0]+r3[1]==top
def tersi(w):
    t=top-w[0]*a_-w[2]*b_-w[3]*c_; assert t%w[1]==0; return t//w[1]
c=[(tersi((1,1,1,1)),'Tabandaki sayıların toplamını en üstteki sayıya eşit sanmış: 42 − 3 − 1 − 3.','bilgi'),
   (tersi((1,2,2,1)),'Alt sıranın ortadaki iki sayısının üste iki kez, uçtakilerin bir kez katkı yaptığını sanmış: ? için (42 − 3 − 2 − 3) ÷ 2.','bilgi'),
   (tersi((1,3,3,0)),'Sağ uçtaki sayının üste hiç katkı yapmadığını sanmış: (42 − 3 − 3) ÷ 3.','bilgi'),
   (tersi((2,3,3,1)),'Soldaki sayıyı iki kez toplamış: (42 − 6 − 3 − 3) ÷ 3.','dikkat'),
   (top-a_-3*b_-c_,'? kutusunun üste 3 kez katkı yaptığını fark etmiş ama sonda 3’e bölmeyi unutmuş: 42 − 3 − 3 − 3.','islem')]
o=[]; wd,ht=1.35,0.85
rows=[[None]*4,[None]*3,[None]*2,[top]]
vals={(0,0):str(a_),(0,1):'?',(0,2):str(b_),(0,3):str(c_),(3,0):str(top)}
for r in range(4):
    n=4-r
    for i in range(n):
        x=(i+r*0.5)*wd; y=r*ht
        t=vals.get((r,i),'')
        o.append(f'\\node[draw,thick,minimum width={wd}cm,minimum height={ht}cm,fill=vurgu!{12 if t else 5},font=\\large\\bfseries] at ({x:.3f},{y:.3f}) {{{t}}};')
SK=fig('\n'.join(o))
spec('0001',x_,c,tipId='rsb-kural',tip='İşlem kuralı ve akış (piramit, şema)',z='kolay',alt='Sayı Piramidi',kaz='Piramitte her alt kutunun üst kutulara katkısını sayarak bilinmeyen sayıyı denklemle bulur.',kalip='yeni nesil',
 kart='K-RSB-01 (sayı piramidi) · taban 3, ?, 1, 3; tepe 42',
 metin='Bir bulmaca kitapçığındaki sayı piramidinde, en alt sıra dışındaki her kutuya, hemen altındaki iki kutudaki sayıların toplamı yazılmıştır. Piramidin şekilde boş bırakılan kutuları kuralla belirlenebilmektedir; alt sıradaki ? işaretli kutuda yazan sayı ise okunamamaktadır.\nBuna göre ? yerine hangi sayı gelmelidir?',
 istenen='? işaretli kutudaki sayı.',ip=['Alt sıradaki dört sayıdan her biri, en üstteki sayıya kaç farklı yoldan ulaşır?'],bilgi=[PIR],sekil=SK,
 ad=[A('İkinci sıra','Alt sıradan komşu kutuların toplamları yazılır; ? yerine x diyelim.','3 + x, x + 1, 1 + 3'),A('Üçüncü sıra','İkinci sıradaki kutuların komşu toplamları.','(3 + x) + (x + 1) = 2x + 4; (x + 1) + 4 = x + 5'),A('Tepe','Üçüncü sıradaki iki kutunun toplamı tepedeki sayıya eşittir.','2x + 4 + x + 5 = 3x + 9 = 42'),A('Çöz','Denklem çözülür.','x = 11')],
 puf='Bulduğun sayıyı piramide yerleştirip bütün toplamları baştan kontrol et.')

# ================= 02 kolay · akış şeması =================
def mak(n): return n//2+3 if n%2==0 else 3*n-5
girdi=[n for n in range(0,500) if mak(n)==13]; assert girdi==[20]
c=[(6,'Tek koldaki işlemi tersine çevirmiş (3n − 5 = 13 → n = 6) ama bulduğu 6’nın çift olduğunu, yani o kola girmeyeceğini denetlememiş.','bilgi'),
   (10,'Çift koldaki işlemde ÷ 2’yi tersine çevirmeyi unutmuş: n = 13 − 3.','islem'),
   (6+20,'İki kolun tersinden bulduğu iki sayıyı koşulu denetlemeden toplamış: 20 + 6.','bilgi'),
   (2*13+3,'Çift koldaki “+ 3” işlemini tersine çevirirken işareti yanlış kullanmış: n = 2 · 13 + 3.','islem'),
   (13,'Çıkış değerini girilen sayı sanmış.','dikkat'),
   (16,'Çıkıştan 3’ü eklemiş: n = 13 + 3.','islem')]
o=['\\tikzset{blk/.style={draw,thick,minimum width=2.6cm,minimum height=0.8cm,align=center},dec/.style={draw,thick,diamond,aspect=2,inner sep=1pt,align=center},io/.style={draw,thick,trapezium,trapezium left angle=70,trapezium right angle=110,minimum height=0.8cm,align=center},ar/.style={-{Stealth[length=2.2mm]},thick}}',
 '\\node[blk,rounded corners=8pt,fill=vurgu!12] (s) at (0,0) {Başla};',
 '\\node[io] (g) at (0,-1.3) {n doğal sayısı girilir};',
 '\\node[dec] (d) at (0,-2.9) {n çift mi?};',
 '\\node[blk] (e) at (-2.6,-4.5) {$n \\leftarrow \\dfrac{n}{2}+3$};',
 '\\node[blk] (h) at (2.6,-4.5) {$n \\leftarrow 3n-5$};',
 '\\node[io] (y) at (0,-6.0) {n yazdırılır};',
 '\\node[blk,rounded corners=8pt,fill=vurgu!12] (b) at (0,-7.2) {Bitir};',
 '\\draw[ar] (s) -- (g); \\draw[ar] (g) -- (d);',
 '\\draw[ar] (d.west) -| (e.north) node[pos=0.25,above] {Evet};',
 '\\draw[ar] (d.east) -| (h.north) node[pos=0.25,above] {Hayır};',
 '\\draw[ar] (e.south) |- (y.west); \\draw[ar] (h.south) |- (y.east); \\draw[ar] (y) -- (b);']
SK=fig('\n'.join(o))
spec('0002',20,c,tipId='rsb-kural',tip='İşlem kuralı ve akış (piramit, şema)',z='kolay',alt='Akış Şeması',kaz='Akış şemasında çıkıştan geriye giderek kolların işlemini tersine çevirir ve koşula uyan girdiyi belirler.',kalip='yeni nesil',
 kart='K-RSB-02 (akış şeması) · çift: n/2 + 3, tek: 3n − 5; çıkış 13',
 metin='Bir bilgisayar programı, şekildeki akış şemasına göre çalışmaktadır: girilen doğal sayıya, çift ise bir işlem, tek ise başka bir işlem uygulanmakta ve sonuç ekrana yazdırılmaktadır. Programın bir çalıştırılışında ekrana 13 sayısı yazdırılmıştır.\nBuna göre bu çalıştırmada programa girilen doğal sayı kaçtır?',
 istenen='Programa girilen doğal sayı.',ip=['13 sayısı hangi kolun çıkışı olabilir?'],bilgi=[AKI,TEC],sekil=SK,
 ad=[A('Çift kol','Sonuç 13 ise n/2 + 3 = 13 olmalıdır.','n/2 = 10, n = 20 (çift: koşul sağlanıyor)'),A('Tek kol','Sonuç 13 ise 3n − 5 = 13 olmalıdır.','3n = 18, n = 6 (çift: tek kola girmez)'),A('Sonuç','Yalnız 20 koşulu sağlar; 20 için programı çalıştırınca 13 çıkar.','20/2 + 3 = 13')],
 puf='Sonucu bulduktan sonra girdiyi ileri yönde çalıştırıp çıkışı doğrula.')

# ================= 03 orta · ışık çizelgesi =================
pat={'A':(4,{0,1,2}),'B':(6,{1,2,3,4}),'C':(3,{0,1})}
lit=lambda L,t:(t%pat[L][0]) in pat[L][1]
b12=sum(all(lit(L,t) for L in 'ABC') for t in range(12)); v=sum(all(lit(L,t) for L in 'ABC') for t in range(60)); assert (b12,v)==(4,20)
assert all(sum(all(lit(L,t) for L in 'ABC') for t in range(12*k,12*k+12))==b12 for k in range(5))
ikili=sum(sum(lit(L,t) for L in 'ABC')>=2 for t in range(60)); bir=sum(any(lit(L,t) for L in 'ABC') for t in range(60)); ab=sum(lit('A',t) and lit('B',t) for t in range(60))
assert (ikili,bir,ab)==(50,55,30)
c=[(b12,'Yalnız şekildeki ilk 12 saniyeyi saymış.','dikkat'),
   (60//12,'Düzenin 60 saniyede kaç kez tekrarlandığını cevap sanmış: 60 ÷ 12.','dikkat'),
   (ab,'Yalnız A ve B lambalarının birlikte yandığı saniyeleri saymış (C lambasını atlamış).','dikkat'),
   (ikili,'En az iki lambanın yandığı saniyeleri saymış.','bilgi'),
   (bir,'En az bir lambanın yandığı saniyeleri saymış.','bilgi'),
   (45,'Yalnız A lambasının yanık kaldığı süreyi yazmış: 60 saniyenin 3/4’ü.','dikkat'),
   (40,'Yalnız B lambasının yanık kaldığı süreyi yazmış: 60 saniyenin 2/3’ü.','dikkat')]
o=[]
for r,L in enumerate('ABC'):
    y=-r*0.9
    o.append(f'\\node[font=\\normalsize\\bfseries] at (-1.0,{y}) {{{L}}};')
    for t in range(12):
        fl='fill=vurgu!45' if lit(L,t) else 'fill=white'
        o.append(f'\\draw[thick,{fl}] ({t*0.6:.2f},{y-0.35:.2f}) rectangle ({t*0.6+0.6:.2f},{y+0.35:.2f});')
for t in range(0,13,2): o.append(f'\\node[font=\\small] at ({t*0.6:.2f},-2.45) {{{t}}};')
o.append('\\node[font=\\small] at (3.6,-2.95) {zaman (saniye)};')
o.append('\\draw[thick,fill=vurgu!45] (0,-3.65) rectangle (0.4,-3.3); \\node[right,font=\\small] at (0.5,-3.47) {: lamba yanık};')
SK=fig('\n'.join(o))
spec('0003',v,c,tipId='rsb-periyot',tip='Tekrarlayan düzenler',z='orta',alt='Işık Çizelgesi',kaz='Farklı periyotlu üç lambanın çizelgesini okuyup ortak periyotta birlikte yanma sürelerini toplam süreye ölçekler.',kalip='hikâyeli',
 kart='K-RSB-03 (ışık çizelgesi) · periyotlar 4, 6, 3; ortak periyot 12 sn',
 metin='Bir mağaza vitrininde A, B ve C lambaları kendi düzenlerini yineleyerek çalışmaktadır: A lambası her 4 saniyede, B lambası her 6 saniyede, C lambası her 3 saniyede bir kendi düzenini aynen tekrarlar. Şekilde ilk 12 saniye gösterilmiştir; her kutu 1 saniyedir ve boyalı kutu, lambanın o saniye boyunca yandığını belirtir. Düzenek 0. saniyede çalışmaya başlamıştır.\nBuna göre ilk 60 saniye boyunca üç lamba aynı anda toplam kaç saniye yanık kalmıştır?',
 istenen='Üç lambanın aynı anda yandığı toplam süre (saniye).',ip=['Şekilde gösterilen 12 saniyeden sonra düzen nasıl devam eder?'],bilgi=[PER,EKO],sekil=SK,
 ad=[A('Ortak periyot','Üç lambanın periyotları 4, 6 ve 3 saniyedir; birlikte başa dönme süresi bunların en küçük ortak katıdır.','EKOK(4, 6, 3) = 12 saniye'),A('İlk 12 saniye','Şekilde üç lambanın birlikte yanık olduğu kutular işaretlenir: '+', '.join(f'{t+1}.' for t in range(12) if all(lit(L,t) for L in 'ABC'))+' saniyelik kutular.','4 saniye'),A('Tekrar sayısı','60 saniye, 12 saniyelik düzenin tam katıdır.','60 ÷ 12 = 5 tekrar'),A('Çarp','Her tekrarda aynı saniye sayısı yinelenir.','5 × 4 = 20 saniye')],
 puf='Tekrarlayan düzenlerde bulduğun sonucu 12 yerine 24 saniyelik bir blokla da hesaplayıp karşılaştır.')

# ================= 04 orta · zar açınımı =================
net=dict(L=1,F=3,R=2,B=5,T=4,D=6)
opp=[('F','B'),('L','R'),('T','D')]
# küpü katla: F ön, T üst, D alt, L sol, R sağ, B arka (şeritte F-R-B komşu, L solda)
# doğrulama: katlama: şeritte L,F,R,B ardışık; yatay şeritte karşılıklı olanlar iki kare arayla
assert [(a,b) for a,b in zip('LFRB','FRB')]==[('L','F'),('F','R'),('R','B')]
v=max(net['F'],net['B'])*max(net['L'],net['R'])*max(net['T'],net['D']); assert v==60
# kaba kuvvet: 8 köşe = (ön/arka) x (sol/sağ) x (üst/alt)
assert v==max(net[a]*net[b]*net[c_] for a in 'FB' for b in 'LR' for c_ in 'TD')
t3=1
for x in sorted(net.values())[-3:]: t3*=x
e2=max(net['L'],net['F'])*max(net['R'],net['B'])*max(net['T'],net['D'])
e3=max(net['T'],net['F'])*max(net['L'],net['R'])*max(net['D'],net['B'])
e4=max(net['F'],net['B'])+max(net['L'],net['R'])+max(net['T'],net['D'])
e5=min(net['F'],net['B'])*min(net['L'],net['R'])*min(net['T'],net['D'])
assert (t3,e2,e3,e4,e5)==(120,90,48,13,12)
c=[(t3,'Bir köşede karşılıklı yüzlerin birleşemeyeceğini düşünmeden en büyük üç sayıyı çarpmış: 6 × 5 × 4.','bilgi'),
   (e2,'Şeritte yan yana duran kareleri karşılıklı sanmış (1 ile 3, 2 ile 5 karşılıklı).','bilgi'),
   (e3,'Üstteki kareyi ortadaki kareyle karşılıklı sanmış (4 ile 3 karşılıklı).','bilgi'),
   (e4,'Her karşılıklı çiftten en büyüğü seçmiş ama çarpmak yerine toplamış.','islem'),
   (e5,'Her karşılıklı çiftten en küçüğü seçip çarpmış.','dikkat')]
o=[]; u=1.15
pos={'T':(1,2),'L':(0,1),'F':(1,1),'R':(2,1),'B':(3,1),'D':(1,0)}
for k,(cx,cy) in pos.items():
    o.append(f'\\node[draw,thick,minimum size={u}cm,fill=vurgu!10,font=\\Large\\bfseries] at ({cx*u},{cy*u}) {{{net[k]}}};')
SK=fig('\n'.join(o))
spec('0004',v,c,tipId='rsb-mekan',tip='Küp ve şekil muhakemesi',z='orta',alt='Zar Açınımı',kaz='Küp açınımında karşılıklı yüzleri belirleyip bir köşede birleşen üç yüzdeki sayıların en büyük çarpımını bulur.',kalip='hikâyeli',
 kart='K-RSB-04 (zar açınımı) · açınım: üst 4, şerit 1-3-2-5, alt 6',
 metin='Bir oyuncak atölyesi, şekildeki açınımı kesip katlayarak sayılı bir küp zar yapıyor; açınımdaki sayılar küpün dış yüzünde kalıyor. Küpün her köşesinde üç yüz birleşmektedir ve her köşe için o üç yüzdeki sayıların çarpımı hesaplanabilir.\nBuna göre küpün köşeleri için bulunabilecek bu çarpımların en büyüğü kaçtır?',
 istenen='Bir köşedeki üç yüzdeki sayıların çarpımının en büyük değeri.',ip=['Açınım katlanınca hangi kareler birbirine bakan (karşılıklı) yüzler olur? Bir köşede iki karşılıklı yüz birleşebilir mi?'],bilgi=[KUP],sekil=SK,
 ad=[A('Karşılıklı yüzler','Yatay şeritte birer kare arayla duran kareler, düşeyde ise üst ve alt kareler karşılıklı gelir.','3 ile 5 · 1 ile 2 · 4 ile 6'),A('Köşelerdeki yüzler','Her köşede her karşılıklı çiftten tam bir yüz bulunur.','çiftlerden birer sayı seçilir'),A('Büyük sayıları seç','Çarpımı büyütmek için her çiftten büyük olan seçilir.','5, 2 ve 6'),A('Çarp','Seçilen sayıların çarpımı bir köşedeki üç yüze karşılık gelir.','5 × 2 × 6 = 60')],
 puf='Açınımı bir kâğıda çizip numaraları yazarak katlamak, karşılıklı yüzleri doğrulamanın en güvenli yoludur.')

# ================= 05 orta · robot =================
prog=[('F',3),'R',('F',1),'L',('F',2),'R']
def run(prog,rep,rot=1):
    x=y=0;h=0; DD=[(0,1),(1,0),(0,-1),(-1,0)]
    for _ in range(rep):
        for cm in prog:
            if cm[0]=='F': x+=DD[h][0]*cm[1];y+=DD[h][1]*cm[1]
            else: h=(h+(1 if cm=='R' else -1)*rot)%4
    return x,y
pos14=run(prog,14); v=abs(pos14[0])+abs(pos14[1]); assert pos14==(6,4) and v==10
assert run(prog,4)==(0,0) and run(prog,2)==(6,4)
t1=sum(abs(z) for z in run(prog,1)); sol=sum(abs(z) for z in run(prog,14,-1)); t3_=sum(abs(z) for z in run(prog,3))
assert (t1,sol,t3_)==(6,10,6)
fark=abs(pos14[0]-pos14[1])
c=[(t1,'14 turu 4’lü bloklara ayırıp kalan 2 turu atlamış, yalnız bir turun uzaklığını yazmış.','dikkat'),
   (0,'14 turun sonunda robotun başlangıca dönmüş olacağını sanmış (4 turda döndüğünü 14 için de varsaymış).','bilgi'),
   (14*6,'Dönüşü hesaba katmayıp bir turun yer değiştirmesini 14 ile çarpmış: 14 × (1 + 5).','bilgi'),
   (fark,'Yatay ve dikey uzaklıkları toplamak yerine farkını almış: 6 − 4.','islem'),
   (2*t1,'İki turun uzaklıklarını ayrı ayrı bulup toplamış (dönüşte yer değiştirmelerin yön değiştirdiğini yok saymış): 6 + 6.','bilgi')]
assert fark==2
o=[]
for i in range(0,4): o.append(f'\\draw[gray!55] ({i*0.9-0.9:.2f},-0.9) -- ({i*0.9-0.9:.2f},{5*0.9+0.9:.2f});')
for j in range(0,8): o.append(f'\\draw[gray!55] (-0.9,{j*0.9-0.9:.2f}) -- ({2*0.9+0.9:.2f},{j*0.9-0.9:.2f});')
pts=[(0,0),(0,3),(1,3),(1,5)]
o.append('\\draw[vurgu!80!black,line width=2.2pt] '+' -- '.join(f'({x*0.9:.2f},{y*0.9:.2f})' for x,y in pts)+';')
o.append('\\fill (0,0) circle (0.1); \\node[below left,font=\\small\\bfseries] at (0,0) {O};')
o.append('\\draw[-{Stealth[length=3mm]},line width=2pt] (0,-0.05) -- (0,0.55);')
o.append(f'\\draw[-{{Stealth[length=3mm]}},line width=2pt] ({0.9:.2f},{5*0.9:.2f}) -- ({0.9+0.55:.2f},{5*0.9:.2f});')
SK=fig('\n'.join(o))
spec('0005',v,c,tipId='rsb-periyot',tip='Tekrarlayan düzenler',z='orta',alt='Robot Yolu',kaz='Bir program turunun yer değiştirmesi ve dönüşünü bulup tekrarları dönüşe göre toplayarak uzaklığı hesaplar.',kalip='hikâyeli',
 kart='K-RSB-05 (robot) · ileri 3, sağ, ileri 1, sol, ileri 2, sağ; 14 tur',
 metin='Bir robot süpürge, ızgara biçimli bir zeminde, şekilde O ile gösterilen noktadan ok yönüne bakarak harekete başlıyor. Programının tamamı şekildeki kalın yolu izleyip şekilde gösterilen yöne bakarak durmasıyla biter; sonra program, robotun o andaki yönüne göre baştan yinelenir. Izgaranın bir karesinin kenarı 1 birimdir ve her iki tur arasında robot bekler.\nBuna göre program art arda 14 kez uygulandığında robot, O noktasından ızgara çizgileri boyunca (yatay ve dikey uzaklıkların toplamı olarak) kaç birim uzaktadır?',
 istenen='14 tur sonunda robotun O noktasına ızgara çizgileri boyunca uzaklığı.',ip=['Bir turun sonunda robotun bakış yönü ne kadar döndü? Bu dönüş, sonraki turların yer değiştirmesini nasıl etkiler?'],bilgi=[YON,MAN],sekil=SK,
 ad=[A('Bir tur','Robot önce 3 birim kuzeye, sağa dönüp 1 doğuya, sola dönüp 2 kuzeye gider ve doğuya bakar.','yer değiştirme: 1 doğu, 5 kuzey; dönüş: 90° sağ'),A('İkinci tur','Robot bu kez doğuya bakıyor; yer değiştirme bir önceki turun 90° sağa çevrilmişidir.','5 doğu, 1 güney'),A('Dört tur','Her tur 90° döndüğünden dört turun yer değiştirmeleri birbirini götürür.','4 turda başlangıca döner'),A('Kalan turlar','14 = 3 × 4 + 2 olduğundan konum, ilk iki turun toplamıyla aynıdır.','1 + 5 = 6 doğu, 5 − 1 = 4 kuzey'),A('Uzaklık','Yatay ve dikey uzaklıklar toplanır.','6 + 4 = 10 birim')],
 puf='Tekrar eden yer değiştirmelerde dönüşün kaç turda tam turu tamamladığını hesaplamak sonucu kısaltır.')

# ================= 06 orta · dişliler =================
dis={'A':18,'B':24,'C':20}
v=next(t for t in range(1,1000) if all((Fr(dis['A']*t,dis[g]).denominator==1) for g in 'BC')); assert v==20
lcm=lambda a,b:a*b//gcd(a,b)
ek3=lcm(lcm(18,24),20); eab=lcm(18,24)//18; eac=lcm(18,20)//18
assert (ek3,eab,eac)==(360,4,10)
c=[(ek3,'Dişlilerin diş sayılarının EKOK’unu (360) A’nın tur sayısı sanmış.','bilgi'),
   (eab,'Yalnız A ile B dişlilerini hesaba katmış: EKOK(18, 24) ÷ 18.','dikkat'),
   (eac,'Yalnız A ile C dişlilerini hesaba katmış: EKOK(18, 20) ÷ 18.','dikkat'),
   (eab*eac,'İki ayrı sonucu (4 ve 10) çarpmış.','bilgi'),
   (lcm(24,20),'Yalnız B ve C dişlilerinin diş sayılarının EKOK’unu yazmış.','bilgi')]
rr={g:dis[g]/16 for g in dis}; cx={}; x=0
o=[]
prev=None
for g in 'ABC':
    if prev is None: cx[g]=rr[g]
    else: cx[g]=cx[prev]+rr[prev]+rr[g]
    prev=g
for g in 'ABC':
    r=rr[g]; n=dis[g]
    o.append(f'\\draw[thick,fill=vurgu!10] ({cx[g]:.3f},0) circle ({r:.3f});')
    for k in range(n):
        a=radians(90+360*k/n); o.append(f'\\draw[thick] ({cx[g]+r*cos(a):.3f},{r*sin(a):.3f}) -- ({cx[g]+(r+0.13)*cos(a):.3f},{(r+0.13)*sin(a):.3f});')
    o.append(f'\\node[font=\\normalsize\\bfseries,align=center] at ({cx[g]:.3f},-0.15) {{{g}\\\\{n} diş}};')
    o.append(f'\\fill ({cx[g]:.3f},{r*0.78:.3f}) circle (0.09);')
SK=fig('\n'.join(o))
spec('0006',v,c,tipId='rsb-periyot',tip='Tekrarlayan düzenler',z='orta',alt='Dişli Zinciri',kaz='Dişli zincirinde her dişlinin dönüş sayısını diş oranından yazıp işaretlerin birlikte başa dönmesi için gereken tur sayısını bulur.',kalip='hikâyeli',
 kart='K-RSB-06 (dişli zinciri) · 18, 24, 20 diş',
 metin='Bir saat atölyesinde, şekildeki A, B ve C dişlileri art arda birbirine geçmiş hâlde çalışmaktadır ve dişlilerin üzerindeki siyah işaretler, başlangıçta şekildeki gibi en üst noktadadır. A dişlisi döndürüldüğünde diğerleri de dişlerin takılmasıyla dönmektedir; bir dişlide işaretin yeniden en üst noktaya gelmesi için o dişlinin tam tur dönmesi gerekir.\nBuna göre üç işaret ilk kez aynı anda en üst noktaya geldiğinde A dişlisi kaç tam tur dönmüş olur?',
 istenen='Üç işaret ilk kez birlikte en üst noktaya geldiğinde A dişlisinin tam tur sayısı.',ip=['A dişlisi 1 tur dönerken B ve C dişlileri kaç tur döner? Hangi tur sayılarında her iki sonuç da tam sayı olur?'],bilgi=[DIS,EKO],sekil=SK,
 ad=[A('B dişlisi','A, t tur dönerken B, t · 18 / 24 = 3t/4 tur döner; tam sayı olması için t, 4’ün katı olmalıdır.','t = 4, 8, 12, …'),A('C dişlisi','C, t · 18 / 20 = 9t/10 tur döner; tam sayı olması için t, 10’un katı olmalıdır.','t = 10, 20, 30, …'),A('Ortak tur','Her iki koşulu sağlayan en küçük t, 4 ile 10’un en küçük ortak katıdır.','EKOK(4, 10) = 20'),A('Kontrol','20 turda B 15, C 18 tam tur döner.','20, 15 ve 18 tam sayı')],
 puf='Bulduğun tur sayısını her dişli için tek tek yeniden hesaplayarak tam sayı çıktığını doğrula.')

# ================= 07 zor · mayın tarlası =================
R_,C_=4,5
def nbr(r,cc): return [(r+a,cc+b) for a in(-1,0,1) for b in(-1,0,1) if (a or b) and 0<=r+a<R_ and 0<=cc+b<C_]
clues={(0,0):2,(0,2):3,(1,0):3,(1,2):3,(1,4):1,(2,1):4,(2,2):3,(3,0):2,(3,3):1}
unk=[(r,cc) for r in range(R_) for cc in range(C_) if (r,cc) not in clues]
sols=[]
for bits in product((0,1),repeat=len(unk)):
    M=dict(zip(unk,bits))
    if all(sum(M.get(n_,0) for n_ in nbr(*k))==vv for k,vv in clues.items()): sols.append(M)
assert len(sols)==1; M=sols[0]; v=sum(M.values()); assert v==6
mines=sorted(k for k,b in M.items() if b); print('mayin',mines)
sm=sum(clues.values()); nun=len(unk)
ust=sum(b for (r,cc),b in M.items() if r<2); alt_=sum(b for (r,cc),b in M.items() if r>=2)
sol_=sum(b for (r,cc),b in M.items() if cc<2); sag=sum(b for (r,cc),b in M.items() if cc>=3)
print(sm,nun,ust,alt_,sol_,sag)
c=[(sm,'Sayıların toplamını mayın sayısı sanmış (bir mayın birden çok sayıda sayılır).','bilgi'),
   (nun,'Sayısız bütün karelerde mayın olduğunu sanmış.','dikkat'),
   (ust,'Yalnız üstteki iki satırdaki mayınları saymış.','dikkat'),
   (sol_,'Yalnız soldaki iki sütundaki mayınları saymış.','dikkat'),
   (sag,'Yalnız sağdaki iki sütundaki mayınları saymış.','dikkat')]
o=[]; u=0.9
for r in range(R_):
    for cc in range(C_):
        x,y=cc*u,-r*u
        if (r,cc) in clues: o.append(f'\\node[draw,thick,minimum size={u}cm,inner sep=0pt,fill=white,font=\\large\\bfseries] at ({x:.2f},{y:.2f}) {{{clues[(r,cc)]}}};')
        else: o.append(f'\\node[draw,thick,minimum size={u}cm,inner sep=0pt,fill=gray!40] at ({x:.2f},{y:.2f}) {{}};')
o.append(f'\\node[draw,thick,minimum size=0.4cm,inner sep=0pt,fill=gray!40] at (0,{-R_*u-0.15:.2f}) {{}}; \\node[right,font=\\small] at (0.3,{-R_*u-0.15:.2f}) {{: açılmamış kare}};')
SK=fig('\n'.join(o))
spec('0007',v,c,tipId='rsb-cikarim',tip='Mantıksal yerleştirme ve çıkarım',z='zor',alt='Mayın Tarlası',kaz='Sayılı karelerin komşu mayın sayılarını birlikte değerlendirip açılmamış karelerdeki mayınları belirler ve toplamı bulur.',kalip='yeni nesil',
 kart='K-RSB-07 (mayın tarlası) · 4 × 5 tarla, 9 sayılı kare',
 metin='Bir bilgisayar oyununda, şekildeki dikdörtgen tarlanın bazı kareleri açılmıştır; açılmış karelerin hiçbirinde mayın yoktur ve her açık karedeki sayı, o kareye yatay, dikey ya da çapraz bitişik karelerdeki toplam mayın sayısını gösterir. Açılmamış (gri) karelerin her birinde en çok bir mayın bulunabilir ve verilen sayılar, mayınların yerini tek biçimde belirlemektedir.\nBuna göre tarlada toplam kaç mayın vardır?',
 istenen='Tarladaki toplam mayın sayısı.',ip=['Hangi sayılı karenin çevresinde açılmamış kare sayısı, sayının değerine en yakındır? Oradan başlayarak bu karelere bakan öteki sayıları da incele.'],bilgi=[MAY],sekil=SK,
 ad=[A('En kısıtlı sayı','3. satır 2. sütundaki 4’ün açılmamış komşuları tam 4 tanedir; hepsinde mayın vardır.','(2, 2), (3, 1), (4, 2), (4, 3) mayın'),A('Sol üst köşe','1. satır 1. sütundaki 2’nin açılmamış komşuları (1, 2) ve (2, 2)’dir; ikisinde de mayın vardır, (2, 2) zaten bulundu.','(1, 2) yeni mayın; toplam 5'),A('Boş kareler','4. satır 4. sütundaki 1, (4, 3)’teki mayınla tamamlanır; (3, 4), (3, 5) ve (4, 5) mayınsızdır. 3. satır 3. sütundaki 3, (2, 2), (4, 2) ve (4, 3) ile tamamlanır; (2, 4) mayınsızdır.','(2, 4), (3, 4), (3, 5), (4, 5) boş'),A('Son mayın','2. satır 3. sütundaki 3’ün komşularında (1, 2) ve (2, 2) mayındır; geriye 1 mayın gerekir ve açılmamış komşulardan yalnız (1, 4) aday kalmıştır. 2. satır 5. sütundaki 1 de bunu doğrular.','(1, 4) mayın'),A('Say','Mayınlar: (1, 2), (1, 4), (2, 2), (3, 1), (4, 2), (4, 3).','6 mayın')],
 puf='Yerleştirdiğin mayınlarla her sayılı karenin sayısını tek tek yeniden hesaplayarak çözümünü kontrol et.')

# ================= 08 zor · üçgen kenar toplamı =================
allp=list(permutations(range(1,7)))
sides=lambda p:(p[0]+p[3]+p[1],p[1]+p[4]+p[2],p[2]+p[5]+p[0])
given={3:2,5:4}
sols=[p for p in allp if len(set(sides(p)))==1 and all(p[k]==x for k,x in given.items())]
assert len(sols)==1; p=sols[0]; v=p[0]+p[1]+p[2]; S=sides(p)[0]; assert (p,S,v)==((5,3,1,2,6,4),10,9)
near=[q for q in allp if len(set(sides(q)))==2 and all(q[k]==x for k,x in given.items())]
nearsum={q[0]+q[1]+q[2] for q in near}; assert {10,12,14,7}-{S}<=nearsum|{10,12,7},nearsum
c=[(S,'Ortak kenar toplamını (10) köşelerin toplamı sanmış.','dikkat'),
   (p[3]+p[4]+p[5],'Kenar ortalarındaki üç sayının toplamını yazmış (2 + 6 + 4).','dikkat'),
   (14,'İki kenarın toplamını eşitleyip üçüncü kenarı denetlememiş; bu yerleşimde köşeler 14 yapıyor.','bilgi'),
   (21//3,'Altı sayının toplamını (21) üçe bölüp köşelerin toplamı sanmış.','islem'),
   (21,'Altı sayının toplamını yazmış.','dikkat')]
assert 14 in nearsum and 12 in nearsum
o=[]
cor={0:(0,3.2),1:(-2.0,0),2:(2.0,0)}; mid={3:(-1.0,1.6),4:(0,0),5:(1.0,1.6)}
o.append('\\draw[thick] (0,3.2) -- (-2,0) -- (2,0) -- cycle;')
for k,(x,y) in {**cor,**mid}.items():
    t=str(given[k]) if k in given else ''
    o.append(f'\\node[circle,draw,thick,fill={"vurgu!20" if t else "white"},minimum size=0.85cm,inner sep=0pt,font=\\large\\bfseries] at ({x},{y}) {{{t}}};')
SK=fig('\n'.join(o))
spec('0008',v,c,tipId='rsb-cikarim',tip='Mantıksal yerleştirme ve çıkarım',z='zor',alt='Kenar Toplamı Düzeni',kaz='Üçgenin kenarlarındaki toplamların eşitliğinden ortak toplamı bulup boş dairelere sayıları yerleştirir.',kalip='yeni nesil',
 kart='K-RSB-08 (kenar toplamı) · 6 daire, kenar ortalarında 2 ve 4',
 metin='Şekildeki üçgenin köşelerine ve kenarlarının orta noktalarına birer daire çizilmiştir. Boş dairelere, şekilde yazılı olmayan 1, 3, 5 ve 6 sayıları, her sayı bir kez kullanılacak biçimde yazılacaktır. Yazım sonunda üçgenin üç kenarı üzerindeki (iki köşe ve aradaki kenar ortası) üçer sayının toplamları birbirine eşit olmalıdır.\nBuna göre üçgenin köşelerindeki üç sayının toplamı kaçtır?',
 istenen='Üç köşedeki sayıların toplamı.',ip=['Hangi daireler birden fazla kenarın toplamında yer alıyor?'],bilgi=[TOP],sekil=SK,
 ad=[A('Toplamları topla','Üç kenarın toplamı toplanınca köşeler iki kez, kenar ortaları bir kez sayılır; 1’den 6’ya sayıların toplamı 21’dir. Köşelerin toplamı k, kenar toplamı S ise:','3S = 21 + k, yani k 3’ün katı'),A('Köşelerin toplamı','Boş dairelere 1, 3, 5, 6 gelecektir; üçü köşelere, kalanı alt kenarın ortasına yazılır. Üç köşe toplamı 9, 10, 12 ya da 14 olabilir; 3’ün katı olanlar 9 ve 12’dir.','k = 9 ya da k = 12'),A('k = 12 denemesi','k = 12 ise S = 11 ve alt kenarın ortası 3’tür; üst köşe + sol alt köşe = 11 − 2 = 9 ve üst köşe + sağ alt köşe = 11 − 4 = 7 gerekir, ama köşelerdeki 1, 5, 6’dan bu toplamlar elde edilemez.','k = 12 olamaz'),A('k = 9 denemesi','k = 9 ise S = 10 ve alt kenarın ortası 6’dır; üst + sol alt = 8, üst + sağ alt = 6, sol alt + sağ alt = 4 gerekir. Köşeler 1, 3, 5’ten oluşur ve bu denklemleri üst = 5, sol alt = 3, sağ alt = 1 sağlar.','5, 3, 1'),A('Köşelerin toplamı','Köşelerdeki sayılar toplanır; üç kenar da 10 eder.','5 + 3 + 1 = 9')],
 puf='Bulduğun yerleşimde üç kenarın da toplamının eşit çıktığını yeniden hesaplayarak doğrula.')

# ================= 09 zor · üçgen sayma =================
def inter(s,t):
    (x1,y1),(x2,y2)=s;(x3,y3),(x4,y4)=t
    d=(x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
    if d==0: return None
    a=((x1-x3)*(y3-y4)-(y1-y3)*(x3-x4))/d; b=-((x1-x2)*(y1-y3)-(y1-y2)*(x1-x3))/d
    if 0<=a<=1 and 0<=b<=1: return (x1+a*(x2-x1),y1+a*(y2-y1))
    return None
def tri(segs):
    n=0
    for t in combinations(range(len(segs)),3):
        Pp=[inter(segs[a],segs[b]) for a,b in combinations(t,2)]
        if None in Pp: continue
        if len(set(Pp))==3: n+=1
    return n
At=(Fr(3),Fr(6)); Bt=(Fr(0),Fr(0)); Ct=(Fr(6),Fr(0))
pt=lambda P_,Q_,t:(P_[0]+(Q_[0]-P_[0])*t,P_[1]+(Q_[1]-P_[1])*t)
Dd=pt(Bt,Ct,Fr(1,3)); Ee=pt(Bt,Ct,Fr(2,3)); Ff=pt(At,Ct,Fr(1,2))
segs=[(At,Bt),(At,Ct),(Bt,Ct),(At,Dd),(At,Ee),(Bt,Ff)]
v=tri(segs); assert v==15; assert tri(segs[:5])==6 and v-6==9
c=[(6,'Yalnız A köşesinden çıkan üç doğru parçasının oluşturduğu üçgenleri saymış, B’den çizilen doğru parçasını hesaba katmamış.','dikkat'),
   (9,'Yalnız B’den çizilen doğru parçasının bir kenar olduğu üçgenleri saymış.','dikkat'),
   (12,'Bütün A tepeli üçgenlerin (6) B’den çizilen doğru parçası yüzünden iki katına çıktığını sanmış: 6 × 2.','bilgi'),
   (10,'Beş doğru parçasından ikişer ikişer seçimi üçgen sanmış: C(5, 2).','islem'),
   (comb(6,3),'Altı doğru parçasından herhangi üçünü seçmiş, birbirini kesmeyen üçlüleri çıkarmamış: C(6, 3).','bilgi')]
sc=0.85
pp={'A':At,'B':Bt,'C':Ct,'D':Dd,'E':Ee,'F':Ff}
o=['\\draw[thick] '+f'({float(At[0])*sc},{float(At[1])*sc}) -- ({float(Bt[0])*sc},{float(Bt[1])*sc}) -- ({float(Ct[0])*sc},{float(Ct[1])*sc}) -- cycle;']
for a_ in ('D','E','F'):
    pass
for nm,(P_,Q_) in (('AD',(At,Dd)),('AE',(At,Ee)),('BF',(Bt,Ff))):
    o.append(f'\\draw[thick] ({float(P_[0])*sc:.3f},{float(P_[1])*sc:.3f}) -- ({float(Q_[0])*sc:.3f},{float(Q_[1])*sc:.3f});')
lab={'A':'above','B':'below left','C':'below right','D':'below','E':'below','F':'above right'}
for k,(x,y) in pp.items(): o.append(f'\\fill ({float(x)*sc:.3f},{float(y)*sc:.3f}) circle (0.07); \\node[{lab[k]},font=\\normalsize\\bfseries] at ({float(x)*sc:.3f},{float(y)*sc:.3f}) {{{k}}};')
SK=fig('\n'.join(o))
spec('0009',v,c,tipId='rsb-mekan',tip='Küp ve şekil muhakemesi',z='orta',alt='Şekilde Üçgen Sayma',kaz='Şekildeki doğru parçalarının oluşturduğu tüm üçgenleri tepe ve kenar gruplarına ayırarak tekrarsız sayar.',kalip='yeni nesil',
 kart='K-RSB-09 (üçgen sayma) · ABC üçgeni, A’dan 2, B’den 1 doğru parçası',
 metin='Bir tasarımcı, bir üçgen kartonun içine şekildeki doğru parçalarını çizmiştir: üçgenin A köşesinden karşı kenara iki, B köşesinden karşı kenara bir doğru parçası. Tasarımcı, kenarları şekildeki doğru parçaları üzerinde bulunan her üçgeni (büyük ya da küçük, başka çizgileri içerse de) boyayacaktır.\nBuna göre şekilde kaç farklı üçgen boyanabilir?',
 istenen='Şekildeki toplam üçgen sayısı.',ip=['Üçgenleri A köşesini tepe alanlar ve almayanlar diye ayırırsan, ikinci grupta B’den çizilen doğru parçası üzerindeki noktalar nasıl kullanılır?'],bilgi=[UCG],sekil=SK,
 ad=[A('B’den çizilen parça olmadan','A’dan çıkan AB, AD, AE, AC doğru parçalarından ikisi ve BC kenarı bir üçgen oluşturur.','C(4, 2) = 6'),A('A tepeli, tabanı BF üzerinde','BF doğru parçası üzerinde B, F ve AD ile AE’yi kestiği iki nokta olmak üzere 4 nokta vardır; A bu 4 noktanın hepsiyle bir doğru parçasıyla birleşir.','C(4, 2) = 6'),A('Diğer tepeler','BF’yi bir kenar olarak kullanan, tepesi A olmayan üçgenler: tepesi C (B ve F ile), tepesi D (B ve AD’nin BF’yi kestiği nokta ile), tepesi E (B ve AE’nin BF’yi kestiği nokta ile).','1 + 1 + 1 = 3'),A('Toplam','Üç grup birbirinden ayrıdır.','6 + 6 + 3 = 15')],
 puf='Üçgenleri tepe noktasına göre gruplayıp her grubu ayrı say; sonunda tekrar saymadığını bir iki üçgeni elle listeleyerek kontrol et.')

# ================= 10 zor · ağırlıklı yol ağı =================
W={('A','B'):2,('A','C'):7,('B','C'):6,('B','D'):7,('C','D'):2,('C','E'):6,('D','F'):4,('E','F'):8,('D','E'):2,('F','G'):2,('E','G'):9}
G={}
for (a_,b_),w in W.items(): G.setdefault(a_,{})[b_]=w; G.setdefault(b_,{})[a_]=w
def dj(s):
    d={s:0}; h=[(0,s)]
    while h:
        x,u_=heapq.heappop(h)
        if x>d[u_]: continue
        for nx,w in G[u_].items():
            if x+w<d.get(nx,10**9): d[nx]=x+w; heapq.heappush(h,(x+w,nx))
    return d
da=dj('A'); de=dj('E'); plain=da['G']; walk=da['E']+de['G']
best=[10**9]
def go(u_,vis,w):
    if w>=best[0]: return
    if u_=='G':
        if 'E' in vis: best[0]=w
        return
    for nx,ww in G[u_].items():
        if nx not in vis: go(nx,vis|{nx},w+ww)
go('A',{'A'},0); v=best[0]
u_='A'; vis={'A'}; gr=0
while u_!='G':
    cs=sorted((w,nx) for nx,w in G[u_].items() if nx not in vis); assert len(cs)==1 or cs[0][0]<cs[1][0]
    gr+=cs[0][0]; u_=cs[0][1]; vis.add(u_)
assert (plain,walk,v,da['E'],gr)==(15,19,20,11,22)
c=[(plain,'Zorunlu noktayı (E) hesaba katmadan A’dan G’ye en kısa yolu yazmış.','dikkat'),
   (walk,'A’dan E’ye ve E’den G’ye en kısa yolları ayrı ayrı bulup toplamış; bu iki yolun ortak noktasından (D) iki kez geçildiğini denetlememiş.','bilgi'),
   (da['E'],'Yalnız A’dan E’ye en kısa yolu yazmış.','dikkat'),
   (gr,'Her noktada en kısa komşu yolu seçerek ilerlemiş.','bilgi')]
pos={'A':(0,0),'B':(2.0,1.7),'C':(2.0,-1.7),'D':(4.4,1.7),'E':(4.4,-1.7),'F':(6.8,0),'G':(8.8,0)}
o=[]
for k,(x,y) in pos.items(): o.append(f'\\node[circle,draw,thick,fill=white,minimum size=0.75cm,inner sep=0pt,font=\\normalsize\\bfseries] ({k}) at ({x},{y}) {{{k}}};')
for (a_,b_),w in W.items(): o.append(f'\\draw[thick] ({a_}) -- ({b_}) node[midway,fill=white,inner sep=1.5pt,font=\\small] {{{w}}};')
SK=fig('\n'.join(o))
spec('0010',v,c,tipId='rsb-yol',tip='Koşullu en kısa yol',z='zor',alt='Koşullu En Kısa Yol',kaz='Zorunlu bir noktadan geçen ve hiçbir noktadan iki kez geçmeyen en kısa yolu yol ağında bulur.',kalip='hikâyeli',
 kart='K-RSB-10 (ağırlıklı yol ağı) · A’dan G’ye, E zorunlu, tekrar yok',
 metin='Bir kargo kuryesi, şekildeki yol ağında A noktasından çıkıp G noktasına gidecektir. Yolların üzerindeki sayılar kilometre cinsinden uzunluklarıdır. Kurye, bir müşterisine teslimat yapmak için E noktasına uğramak zorundadır ve yolculuğu boyunca hiçbir noktadan iki kez geçmeyecektir.\nBuna göre kuryenin yapabileceği en kısa yolculuk kaç kilometredir?',
 istenen='En kısa yolculuğun uzunluğu (km).',ip=['E’ye ulaşan en kısa yolu bulup oradan G’ye en kısa yolla devam etmek, hiçbir noktadan iki kez geçmeme koşulunu bozuyor mu?'],bilgi=[YOL],sekil=SK,
 ad=[A('A’dan E’ye','En kısa yollar A–C–D–E ve A–B–D–E’dir; ikisi de D’den geçer.','7 + 2 + 2 = 11 km ve 2 + 7 + 2 = 11 km'),A('E’den G’ye','E–D–F–G (2 + 4 + 2 = 8 km) D’yi ikinci kez kullandığından geçersizdir; D’ye uğramayan devam yolları E–F–G ve E–G’dir.','E–F–G = 10 km · E–G = 9 km'),A('Birleştir','D’den bir kez geçen rotalar toplanır.','A–C–D–E–G = 11 + 9 = 20 km · A–C–D–E–F–G = 11 + 10 = 21 km'),A('D’yi sonra kullanan rota','Önce D’ye uğramadan E’ye gidip E–D–F–G ile devam eden rota geçerlidir ama daha uzundur.','A–C–E–D–F–G = 7 + 6 + 2 + 4 + 2 = 21 km'),A('En kısa','Bütün geçerli rotalar karşılaştırıldığında en küçük toplam bulunur.','20 km')],
 puf='Bulduğun rotanın her noktasını sırayla yazıp hiçbir noktanın iki kez geçmediğini kontrol et.')

# ---------- üret ----------
HR=olus(SP)
for (no,d,ad_,k),r in zip(SP,HR):
    sm=[a for a in ad_ if a[0]<d]; lg=[a for a in ad_ if a[0]>d]
    yan=sm[:r]+lg[:4-r]; assert len(yan)==4
    mk(P,no,dogru=d,yan=yan,adim=len(k['ad']),**k)
bitir(P,'rutinsekb',UK)
