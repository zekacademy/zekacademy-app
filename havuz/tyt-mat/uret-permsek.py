"""Permütasyon ve Kombinasyon · ŞEKİLLİ ek paket (7 soru): şekil/tablo çözüm verisini taşır; her doğru ve çeldirici değer kodla (tarama/formül) assert edilir. Kardeş yok, ipucu 1."""
import sys,os,math
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
from math import cos,sin,radians,comb,factorial as fa
from itertools import product,permutations
H.KONU='Permütasyon ve Kombinasyon'
UK='matd|Permütasyon ve Kombinasyon'
P=Parti('permsek','Permütasyon ve Kombinasyon',UK)
KY='ÖSYM 2018–2026 TYT Matematik (şekilli/tablolu sayma soruları; yalnız mantık) · MEB 10. sınıf'
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)
def fig(body): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'+body+'\n\\end{tikzpicture}')
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)

CAR=B('Çarpma ve toplama ilkesi','ardışık ve birbirinden bağımsız adımların seçenek sayıları çarpılır; birbirinin yerine geçen ayrı durumların sayıları toplanır. Örnek: 2 çeşit çorba ve 5 çeşit ana yemekten birer tane seçmek 2 × 5 = 10 yoldur; çorba yerine salata seçmek ayrı durumdur, toplanır')
KOM=B('Kombinasyon','n kişi arasından sırası önemsiz k kişi seçmenin yolu C(n, k) = n! / (k!(n − k)!) kadardır; sıra önemli olsaydı P(n, k) = n! / (n − k)! olurdu. Örnek: 7 kişiden 3’ünü seçmek C(7, 3) = 35 yoldur')
YOL=B('Izgarada en kısa yol','sağa a, yukarı b adım gereken en kısa yolların sayısı C(a + b, a)’dır. Bir noktadan geçmeyen yollar = tüm yollar − o noktadan geçen yollar. Örnek: sağa 2, yukarı 3 adımla gidilen yol sayısı C(5, 2) = 10’dur')
MAS=B('Yan yana oturma','yan yana olması istenenler tek bir blok sayılır, blok içi sıralama ayrıca çarpılır. Yer sayısı sınırlıysa önce bloğun yerleşebileceği konumlar sayılır. Örnek: yan yana 2 kişi için 3 uygun koltuk çifti varsa iki kişi 3 × 2 = 6 biçimde oturur')
BOL=B('Komşu bölgeleri farklı boyama','önce en çok komşusu olan bölge boyanır; sonra kalan bölgeler için “komşularından farklı” seçenekler sırayla sayılır. Bir halkada ilk ve son bölge de komşu olabilir, bu durumda sayım bir döngü gibi yapılır. Örnek: yan yana 3 bölgeden uçtakiler komşu değilse renkler farklı ya da aynı olabilir')
SIF=B('Kutulara yerleştirme','her kutunun kendi seçenek kümesi vardır; bir koşul (ör. “farklı olsun”) kutular arasında seçenek sayısını azaltır. Koşullu kutudan başlamak sayımı kolaylaştırır. Örnek: iki kutuya 6 harften farklı iki harf yazılacaksa ilk kutuya 6, ikincisine 5 seçenek kalır')
KOLT=B('Koşullu yerleşim','önce koşulu sağlayan yerleşim yerleri (ardışık boş koltuk grupları) sayılır, sonra o yerlere kişiler koşula uygun sıralanır. Örnek: 6 ardışık boş koltuk, 3 ardışık koltuk içeren 4 farklı grup verir')

# ---------- kartlar ----------
kartla('K-PSK-01','Şehirler arası yol ağı','Şekildeki çizgi sayılarından her iki ara şehir üzerinden geçen yollar çarpılır; farklı ara şehirler üzerinden gidenler toplanır.','Bütün yolları toplamak; iki ayrı rotayı da çarpmak; yolları yanlış eşleştirmek.','kolay','şekilli',3,'psk-yolagi','Yol ağı ve çarpma ilkesi')
kartla('K-PSK-02','Şifre kutuları ve koşul','Her kutunun seçenek sayısı şekilden okunur; koşullu kutu çiftinde ikinci kutu bir seçenek eksik sayılır; kutuların seçenekleri çarpılır.','Koşulu atlamak; sıra önemsiz sanıp kombinasyon almak; bir kutuyu saymamak.','kolay','şekilli',3,'psk-kutu','Şifre kutuları')
kartla('K-PSK-03','Tabloda verilen gruplardan takım seçimi','Her gruptan istenen sayıda kişi sırasız seçilir (kombinasyon); gruplar çarpılır.','Sıralı seçim (permütasyon) yapmak; seçilecek kişi sayısını atlamak.','orta','tablo',4,'psk-tablo','Tablodaki gruplardan seçim')
kartla('K-PSK-04','Yuvarlak masada kısmen dolu oturma','Boş koltuklar arasında yan yana olan çiftleri şekilden say; her çift için iki sıralama ve kalan kişilerin sıralaması çarpılır.','Her boş koltuğu komşu saymak; çift içi sıralamayı unutmak; kalan kişileri hesaba katmamak.','orta','şekilli',4,'psk-masa','Masa düzeni (bazı yerler dolu)')
kartla('K-PSK-05','Izgarada yasak kavşak','Tüm en kısa yollardan, yasak noktadan geçenler çıkarılır; yasak noktadan geçenler iki parça yolun çarpımıdır.','Yasak noktadan geçenleri çıkarmamak; yalnız bir parçayı çıkarmak; geçenleri cevap sanmak.','orta','şekilli',4,'psk-izgara','Izgarada yasak nokta')
kartla('K-PSK-06','Komşu bölgeleri farklı renge boyama','Merkez bölge için renk seçilir; çevredeki halkada komşu bölgelerin renkleri farklı olacak biçimde döngüsel sayım yapılır.','İlk ve son bölgenin komşu olduğunu unutmak; tüm bölgelerin farklı renkte olması gerektiğini sanmak.','zor','şekilli',5,'psk-boyama','Bölge boyama')
kartla('K-PSK-07','Koltuk planında koşullu oturma','Her sırada ardışık boş koltuk grupları sayılır, üçlü pencereler toplanır; koşula uygun sıralama sayısıyla çarpılır.','Pencereleri grup sayısı sanmak; koşulu atlamak; sıralamayı yanlış saymak.','zor','şekilli',5,'psk-koltuk','Koltuk planı ve koşullu sıralama')

# ================= 01 kolay · yol ağı =================
ab,ac,bd,cd=3,2,2,4
v=ab*bd+ac*cd; assert v==14
yol=lambda a,b,c,d:a*b+c*d
e=[ab+ac+bd+cd,ab*bd,ac*cd,ab*ac*bd*cd]
assert e==[11,6,8,48] and len({v,*e})==5
def kenar(p,q_,n):
    bend={2:[-16,16],3:[-26,0,26],4:[-42,-14,14,42]}[n]; o=[]
    for t in bend:
        if t==0: o.append(f'\\draw[thick] ({p}) -- ({q_});')
        elif t>0: o.append(f'\\draw[thick] ({p}) to[bend left={t}] ({q_});')
        else: o.append(f'\\draw[thick] ({p}) to[bend right={-t}] ({q_});')
    return '\n'.join(o)
o=[kenar('A','B',ab),kenar('A','C',ac),kenar('B','D',bd),kenar('C','D',cd)]
o=['\\coordinate (A) at (0,0); \\coordinate (B) at (3.6,2.0); \\coordinate (C) at (3.6,-2.0); \\coordinate (D) at (7.2,0);']+o
for nm,pos in (('A','0,0'),('B','3.6,2.0'),('C','3.6,-2.0'),('D','7.2,0')):
    o.append(f'\\node[circle,draw,thick,fill=white,minimum size=0.85cm,font=\\normalsize\\bfseries] at ({pos}) {{{nm}}};')
SK=fig('\n'.join(o))
q('0001',tipId='psk-yolagi',tip='Yol ağı ve çarpma ilkesi',z='kolay',alt='Yol Ağı',kaz='Şehirler arasındaki yolları şekilden sayıp çarpma ve toplama ilkesiyle toplam yol sayısını bulur.',kalip='hikâyeli',
 kart='K-PSK-01 (yol ağı) · AB 3, AC 2, BD 2, CD 4 yol',
 metin='Bir kargo firması, şekildeki A, B, C ve D şehirleri arasındaki yolları kullanmaktadır. Şekilde her çizgi, iki şehri doğrudan bağlayan ayrı bir yolu göstermektedir ve şekilde görülenlerden başka yol yoktur. Bir kamyon, A şehrinden yola çıkıp B ya da C şehrine uğrayarak D şehrine ulaşacak; yolculuk boyunca hiçbir şehirden iki kez geçmeyecektir.\nBuna göre kamyon A’dan D’ye kaç farklı yolla gidebilir?',
 dogru=v,yan=[(e[0],'Şekildeki bütün yolları toplamış: 3 + 2 + 2 + 4.','dikkat'),(e[1],'Yalnız B şehri üzerinden giden yolları saymış: 3 × 2.','dikkat'),(e[2],'Yalnız C şehri üzerinden giden yolları saymış: 2 × 4.','dikkat'),(e[3],'Bütün yolları art arda çarpmış: 3 × 2 × 2 × 4.','bilgi')],
 istenen='A’dan D’ye kamyonun gidebileceği farklı yol sayısı.',ip=['B üzerinden ve C üzerinden giden yolları ayrı ayrı düşün; her birinde iki yol parçası art arda gelir.'],bilgi=[CAR],sekil=SK,
 ad=[A('B üzerinden','A–B yolları ile B–D yolları art arda seçilir; çarpılır.','3 × 2 = 6 yol'),A('C üzerinden','A–C yolları ile C–D yolları art arda seçilir; çarpılır.','2 × 4 = 8 yol'),A('Topla','Rotalar birbirinin yerine geçtiği için sonuçlar toplanır.','6 + 8 = 14 yol')],
 puf='“Ve” ile bağlanan art arda seçimler çarpılır, “ya da” ile ayrılan rotalar toplanır.')

# ================= 02 orta · tablo takım seçimi =================
nY,nM,nE=5,6,4; v=nY*comb(nM,2)*comb(nE,2); assert v==450
e=[nY*nM*nE,nY*comb(nM,2)*2,nY*comb(nM,2)*nE,nY*nM*2*comb(nE,2)]
assert e==[120,150,300,360] and len({v,*e})==5
SK=tablo_svg(['Çalışma alanı','Gönüllü sayısı'],[['Yazılım',str(nY)],['Mekanik',str(nM)],['Elektronik',str(nE)]])
q('0002',tipId='psk-tablo',tip='Tablodaki gruplardan seçim',z='orta',alt='Tablodan Seçim',kaz='Tabloda verilen gruplardan istenen sayıda kişiyi sırasız seçerek takım sayısını bulur.',kalip='tablo',
 kart='K-PSK-03 (tablo) · 5, 6, 4 gönüllü; 1 + 2 + 2 kişilik takım',
 metin='Bir okulun robotik kulübünde, yarışmaya gönüllü olan öğrencilerin çalışma alanlarına göre dağılımı aşağıdaki tabloda verilmiştir; her öğrenci yalnız bir alanda çalışmaktadır. Yarışmaya 5 kişilik bir takım gidecek ve takımda yazılım alanından 1, mekanik alanından 2, elektronik alanından 2 öğrenci bulunacaktır. Takımda görev ayrımı yapılmayacaktır.\nBuna göre bu takım kaç farklı biçimde oluşturulabilir?',
 dogru=v,yan=[(e[0],'Her alandan yalnız birer kişi seçilecekmiş gibi çarpmış: 5 × 6 × 4.','dikkat'),(e[1],'Elektronik alanında “2 kişi” seçimini 2 ile çarpma sanmış: 5 × C(6, 2) × 2.','bilgi'),(e[2],'Elektronik alanından da yalnız 1 kişi seçmiş: 5 × C(6, 2) × 4.','dikkat'),(e[3],'Mekanik alanında “2 kişi” seçimini 6 × 2 sanmış: 5 × 12 × C(4, 2).','bilgi')],
 istenen='Oluşturulabilecek farklı takım sayısı.',ip=['Takımda görev ayrımı olmadığına göre her alandaki seçimde sıranın bir önemi var mı?'],bilgi=[KOM],sekil=SK,
 ad=[A('Tabloyu oku','Her alandaki gönüllü sayısı tablodan okunur.','yazılım 5 · mekanik 6 · elektronik 4'),A('Her alandan seç','Sıra önemsiz olduğundan kombinasyon kullanılır.','yazılım C(5, 1) = 5 · mekanik C(6, 2) = 15 · elektronik C(4, 2) = 6'),A('Çarp','Alan seçimleri birbirinden bağımsızdır.','5 × 15 × 6 = 450')],
 puf='Takımdaki görev farkı yoksa seçim sırasızdır: P değil C kullan.')

# ================= 03 orta · yuvarlak masa =================
doluA={0:'Ada',3:'Bora',5:'Cem'}; N=8
bos=[i for i in range(N) if i not in doluA]; assert bos==[1,2,4,6,7]
cift=[(i,(i+1)%N) for i in range(N) if i in bos and (i+1)%N in bos]; assert cift==[(1,2),(6,7)]
kisi=5; v=len(cift)*2*fa(kisi-2); assert v==24
# deneme (kaba kuvvet): 5 kişi 5 boş koltuğa; Deniz=0, Ece=1 yan yana
sy=0
for perm in permutations(range(kisi)):
    pos={k:bos[j] for j,k in enumerate(perm)}
    if (pos[0]-pos[1])%N in (1,N-1): sy+=1
assert sy==v
e=[fa(kisi),len(cift)*fa(kisi-2),4*2*fa(kisi-2),fa(kisi-2)]
assert e==[120,12,48,6] and len({v,*e})==5
o=[]; R=2.15
o.append('\\draw[thick,fill=vurgu!12] (0,0) circle (1.25);')
for i in range(N):
    a=radians(90-45*i); x,y=R*cos(a),R*sin(a)
    if i in doluA: o.append(f'\\node[circle,draw,thick,fill=vurgu!35,minimum size=1.0cm,inner sep=0pt,font=\\footnotesize\\bfseries] at ({x:.3f},{y:.3f}) {{{doluA[i]}}};')
    else: o.append(f'\\node[circle,draw,thick,fill=white,minimum size=0.8cm] at ({x:.3f},{y:.3f}) {{}};')
SK=fig('\n'.join(o))
q('0003',tipId='psk-masa',tip='Masa düzeni (bazı yerler dolu)',z='orta',alt='Masa Düzeni',kaz='Yuvarlak masada bazı koltuklar doluyken yan yana oturma koşulunu sağlayan yerleşimleri sayar.',kalip='hikâyeli',
 kart='K-PSK-04 (yuvarlak masa) · 8 koltuk, 3 dolu; 2 kişi yan yana, 5 kişi',
 metin='Bir kafede, yuvarlak masanın çevresindeki sandalyelerden bazıları şekilde adları yazılı kişiler tarafından doldurulmuştur. Deniz, Ece, Fatih, Gül ve Hakan, masadaki boş sandalyelerin tamamına oturacaktır. Sandalyeler birbirinden ayırt edilebilir; aynı kişilerin farklı sandalyelere oturması farklı düzen sayılır. Deniz ile Ece, birbirine komşu iki sandalyeye oturmak istemektedir.\nBuna göre bu beş kişi kaç farklı biçimde oturabilir?',
 dogru=v,yan=[(e[0],'Deniz ile Ece’nin yan yana olma koşulunu hiç dikkate almamış: 5!.','dikkat'),(e[1],'Çift içindeki iki sıralamayı unutmuş: 2 çift × 3!.','dikkat'),(e[2],'Boş sandalyeleri listede ardışık sayıp 4 komşu çift bulmuş (araya giren dolu sandalyeyi atlamış): 4 × 2 × 3!.','dikkat'),(e[3],'Yalnız Deniz ile Ece dışındaki üç kişinin sıralamasını saymış: 3!.','dikkat')],
 istenen='Beş kişinin boş sandalyelere farklı oturma sayısı.',ip=['Boş sandalyelerden hangi ikisi birbirine komşu? Şekilde dolu sandalyelerin araya girdiği yerlere dikkat et.'],bilgi=[MAS],sekil=SK,
 ad=[A('Komşu boş çiftler','Dolu sandalye iki boş sandalyenin arasına giriyorsa onlar komşu değildir; şekilde yan yana iki boş sandalye bulunan yerler sayılır.','2 çift'),A('Deniz–Ece','Seçilen çiftte iki kişi iki farklı sırayla oturabilir.','2 çift × 2 sıra = 4'),A('Diğer üç kişi','Kalan 3 boş sandalyeye 3 kişi yerleşir.','3! = 6'),A('Çarp','Bağımsız seçimler çarpılır.','4 × 6 = 24')],
 puf='Komşuluk sandalyelerin masadaki yerine bağlıdır; boş koltukların listede ardışık olması komşu olmaları demek değildir.')

# ================= 04 zor · bölge boyama (çark) =================
adj={1:{2,3,4,5,6},2:{1,3,6},3:{1,2,4},4:{1,3,5},5:{1,4,6},6:{1,5,2}}
for a_ in adj:
    for b_ in adj[a_]: assert a_ in adj[b_]
def boya(k,komsu):
    n=len(komsu); sy=0
    for c in product(range(k),repeat=n):
        if all(c[a_-1]!=c[b_-1] for a_ in komsu for b_ in komsu[a_] if a_<b_): sy+=1
    return sy
k=4; v=boya(k,adj); assert v==4*(3*5*2)==120
e=[4*3*2**4,4*3*2*2*2*1,4*3**5,2**5-2]
assert e==[192,96,972,30] and len({v,*e})==5
o=['\\draw[thick] (0,0) circle (0.8);','\\draw[thick] (0,0) circle (2.1);']
for i in range(5):
    a=radians(90-72*i); o.append(f'\\draw[thick] ({0.8*cos(a):.3f},{0.8*sin(a):.3f}) -- ({2.1*cos(a):.3f},{2.1*sin(a):.3f});')
o.append('\\node[font=\\Large\\bfseries] at (0,0) {1};')
for i in range(5):
    a=radians(90-72*i-36); o.append(f'\\node[font=\\Large\\bfseries] at ({1.45*cos(a):.3f},{1.45*sin(a):.3f}) {{{i+2}}};')
SK=fig('\n'.join(o))
q('0004',tipId='psk-boyama',tip='Bölge boyama',z='zor',alt='Bölge Boyama',kaz='Komşu bölgelerin farklı renkte olması koşuluyla halka biçimli bir haritayı boyama sayısını bulur.',kalip='yeni nesil',
 kart='K-PSK-06 (boyama) · merkez + 5 halka bölgesi, 4 renk',
 metin='Şekildeki numaralı altı bölgenin her biri kırmızı, mavi, sarı ve yeşil renklerden yalnız biriyle boyanacaktır. Bir boyamada ortak sınır çizgisi bulunan her bölge çifti farklı renkteyse bu boyamaya “uygun boyama” denir. Bir renk birden fazla bölgede kullanılabilir, hiç kullanılmayan renk de olabilir.\nBuna göre bu bölgeler için kaç farklı uygun boyama yapılabilir?',
 dogru=v,yan=[(e[0],'Halkadaki son bölgenin ilk bölgeyle de komşu olduğunu atlamış: 4 × 3 × 2 × 2 × 2 × 2.','dikkat'),(e[1],'Son bölgeyi her durumda tek seçenek sanmış: 4 × 3 × 2 × 2 × 2 × 1.','bilgi'),(e[2],'Halkadaki bölgeleri yalnız merkezden farklı saymış: 4 × 3⁵.','dikkat'),(e[3],'Merkez bölgenin renk seçimini (4 yol) çarpmayı unutmuş: yalnız halka sayısı.','dikkat')],
 istenen='Uygun boyama sayısı.',ip=['Merkezdeki bölgenin rengi seçilince halkadaki bölgeler hangi renkleri kullanabilir? Halkanın kendi içindeki komşulukları da şekle bakarak incele.'],bilgi=[BOL],sekil=SK,
 ad=[A('Merkez bölge','Merkez, diğer beş bölgenin hepsine komşudur; 4 renkten biri seçilir.','4 seçenek'),A('Halka renkleri','Halkadaki bölgeler merkezin rengini kullanamaz; yalnız 3 renk kalır.','3 renk'),A('Halkayı say','Halkadaki 5 bölge sırayla komşudur (ilki ile sonuncusu da). 3 renkle komşular farklı boyanırsa renkler 2, 2 ve 1 bölgede kullanılır: tek bölgede kalan rengi 3 yolla, o bölgeyi 5 yolla seç; kalan 4 bölge zincir olur, iki renk dönüşümlü 2 biçimde dizilir.','3 × 5 × 2 = 30'),A('Çarp','Merkez seçimi ile halka boyaması bağımsızdır.','4 × 30 = 120')],
 puf='Halka biçimli komşulukta ilk bölge ile son bölge de komşudur; sayımı zincir gibi bitirmek fazla sonuç verir.')

# ================= 05 orta · ızgarada yasak kavşak =================
a_,b_=5,4; X=(1,1)
def yolsay(a,b): return comb(a+b,a)
tum=yolsay(a_,b_); gecen=yolsay(*X)*yolsay(a_-X[0],b_-X[1]); v=tum-gecen
assert (tum,gecen,v)==(126,70,56)
# kaba kuvvet
from functools import lru_cache
@lru_cache(None)
def say(x,y):
    if (x,y)==X: return 0
    if (x,y)==(0,0): return 1
    return (say(x-1,y) if x>0 else 0)+(say(x,y-1) if y>0 else 0)
assert say(a_,b_)==v
e=[tum,gecen,tum-yolsay(*X),tum-yolsay(a_-X[0],b_-X[1])]
assert e==[126,70,124,91] and len({v,*e})==5
u=1.0; o=[]
for i in range(a_+1): o.append(f'\\draw[thick] ({i*u},0) -- ({i*u},{b_*u});')
for j in range(b_+1): o.append(f'\\draw[thick] (0,{j*u}) -- ({a_*u},{j*u});')
o.append(f'\\fill (0,0) circle (0.08); \\node[below left] at (0,0) {{A}}; \\fill ({a_*u},{b_*u}) circle (0.08); \\node[above right] at ({a_*u},{b_*u}) {{B}};')
o.append(f'\\node[circle,draw,thick,fill=white,inner sep=0pt,minimum size=0.42cm] at ({X[0]*u},{X[1]*u}) {{$\\times$}};')
o.append(f'\\node[circle,draw,thick,fill=white,inner sep=0pt,minimum size=0.36cm] at (0.3,-0.95) {{$\\times$}}; \\node[right] at (0.55,-0.95) {{: kapalı kavşak}};')
SK=fig('\n'.join(o))
q('0005',tipId='psk-izgara',tip='Izgarada yasak nokta',z='orta',alt='Izgarada Yol',kaz='Izgarada yalnız sağa ve yukarı giden en kısa yolları, kapalı bir kavşaktan geçenleri çıkararak sayar.',kalip='hikâyeli',
 kart='K-PSK-05 (ızgara) · sağa 5, yukarı 4; kapalı kavşak (1, 1)',
 metin='Şekildeki sokakları birbirine dik ve eş aralıklı bir mahallede bir bisikletli, A noktasından B noktasına sokaklar boyunca yalnızca sağa ya da yukarı doğru ilerleyerek gidecektir. Yol çalışması nedeniyle şekilde işaretlenen kavşak kapatılmıştır ve bisikletli bu kavşaktan hiç geçmeyecektir.\nBuna göre bisikletli A’dan B’ye en kısa yoldan kaç farklı biçimde gidebilir?',
 dogru=v,yan=[(e[0],'Kapalı kavşağı hiç dikkate almamış: tüm yolları saymış.','dikkat'),(e[1],'Çıkarmak yerine kapalı kavşaktan geçen yolların sayısını yazmış.','dikkat'),(e[2],'Kapalı kavşaktan geçenleri yalnız A’dan kavşağa giden yol sayısı kadar sanıp onu çıkarmış: tüm yollar − 2.','bilgi'),(e[3],'Kapalı kavşaktan geçenleri yalnız kavşaktan B’ye giden yol sayısı kadar sanıp onu çıkarmış: tüm yollar − 35.','bilgi')],
 istenen='Kapalı kavşaktan geçmeden A’dan B’ye en kısa yolların sayısı.',ip=['Kapalı kavşaktan geçen yollar, A’dan kavşağa ve kavşaktan B’ye olmak üzere iki parçadan oluşur.'],bilgi=[YOL],sekil=SK,
 ad=[A('Tüm yollar','Sağa 5, yukarı 4 adım gerekir.','C(9, 4) = 126'),A('Kavşaktan geçenler','A’dan kavşağa sağa 1, yukarı 1; kavşaktan B’ye sağa 4, yukarı 3 adım.','C(2, 1) × C(7, 3) = 2 × 35 = 70'),A('Çıkar','Kavşaktan geçmeyen yollar kalır.','126 − 70 = 56')],
 puf='“Geçmeyen” sorusunda önce tüm yolları say, sonra kavşaktan geçenlerin iki parçasını çarpıp çıkar.')

# ================= 06 kolay · şifre kutuları =================
n1,n2,n3,n4=5,10,10,4; v=n1*n2*(n3-1)*n4; assert v==1800
say=0
for l,a,b,c in product(range(5),range(10),range(10),[2,3,5,7]):
    if a!=b: say+=1
assert say==v
e=[n1*n2*n3*n4,n1*comb(10,2)*n4,n1*n2*(n3-2)*n4,n1*n2*(n3-1)]
assert e==[2000,900,1600,450] and len({v,*e})==5
bx=[('A, B, C,\\\\D, E'),('0–9 arası\\\\bir rakam'),('0–9 arası\\\\bir rakam'),('2, 3,\\\\5, 7')]
o=[]
for i,t in enumerate(bx):
    x=i*2.5
    o.append(f'\\node[draw,thick,minimum width=2.1cm,minimum height=1.4cm,align=center] (b{i}) at ({x},0) {{{t}}};')
    o.append(f'\\node[above=2pt] at ({x},0.7) {{{i+1}. kutu}};')
SK=fig('\n'.join(o))
q('0006',tipId='psk-kutu',tip='Şifre kutuları',z='kolay',alt='Şifre Kutuları',kaz='Her kutunun seçenek kümesini şekilden okuyup koşullu kutu çiftini de dikkate alarak şifre sayısını bulur.',kalip='yeni nesil',
 kart='K-PSK-02 (şifre kutuları) · 5, 10, 10, 4 seçenek; 2. ve 3. kutu farklı',
 metin='Bir sistemde şifre, şekildeki dört kutuya sırayla yazılan dört karakterden oluşur. Her kutuya, o kutunun içinde yazan seçeneklerden yalnız biri yazılabilir. 2. ve 3. kutulara yazılan rakamlar birbirinden farklı olmak zorundadır; başka bir koşul yoktur.\nBuna göre bu sistemde kaç farklı şifre oluşturulabilir?',
 dogru=v,yan=[(e[0],'2. ve 3. kutudaki rakamların farklı olması koşulunu atlamış: 5 × 10 × 10 × 4.','dikkat'),(e[1],'İki rakamı sırasız seçmiş: 5 × C(10, 2) × 4.','bilgi'),(e[2],'3. kutuda hem 2. kutudaki rakamı hem de 0’ı dışarıda bırakmış: 5 × 10 × 8 × 4.','islem'),(e[3],'Son kutuyu saymamış: 5 × 10 × 9.','dikkat')],
 istenen='Oluşturulabilecek farklı şifre sayısı.',ip=['2. kutuya bir rakam girildikten sonra 3. kutuda hangi rakamlar kullanılamaz?'],bilgi=[SIF],sekil=SK,
 ad=[A('Seçenekleri oku','Şekildeki her kutunun seçenek sayısı.','1. kutu 5 · 2. kutu 10 · 3. kutu 10 · 4. kutu 4'),A('Koşulu uygula','3. kutuda 2. kutudaki rakam kullanılamaz.','3. kutu: 10 − 1 = 9'),A('Çarp','Kutu seçimleri bağımsızdır.','5 × 10 × 9 × 4 = 1800')],
 puf='Koşul yalnız ilgili kutuların seçenek sayısını değiştirir; diğer kutular aynen kalır.')

# ================= 07 zor · koltuk planı =================
satir=['11110011','01111101','11101111']  # 1 = boş
def pencere(s): return sum(1 for i in range(len(s)-2) if s[i:i+3]=='111')
bl=[pencere(s) for s in satir]; assert bl==[2,3,3]; toplam=sum(bl)
# kaba kuvvet: Ece(0), Tuna(1), Su(2) aynı sırada ardışık 3 boş koltuk; Ece-Tuna yan yana değil
sy=0
for r,s in enumerate(satir):
    for pos in permutations(range(8),3):
        if all(s[p]=='1' for p in pos):
            if sorted(pos)[2]-sorted(pos)[0]==2 and abs(pos[0]-pos[1])!=1: sy+=1
v=toplam*2; assert sy==v==16
gruplar=sum(1 for s in satir for g in s.split('0') if len(g)>=3)
e=[gruplar*2,toplam*3,toplam*4,toplam*6]
assert (gruplar,e)==(4,[8,24,32,48]) and len({v,*e})==5
o=[]; u=0.85
o.append(f'\\node[draw,thick,fill=gray!20,minimum width={8*u+0.1}cm,minimum height=0.45cm,font=\\footnotesize] at ({3.5*u},0.65) {{PERDE}};')
for r,s in enumerate(satir):
    y=-r*1.05
    o.append(f'\\node[left,font=\\footnotesize] at (-0.55,{y}) {{{r+1}. sıra}};')
    for i,c in enumerate(s):
        fl='fill=gray!60' if c=='0' else 'fill=white'
        o.append(f'\\draw[thick,{fl}] ({i*u-0.32:.3f},{y-0.32:.3f}) rectangle ({i*u+0.32:.3f},{y+0.32:.3f});')
o.append(f'\\draw[thick,fill=gray!60] (0,-3.6) rectangle (0.5,-3.1); \\node[right,font=\\footnotesize] at (0.6,-3.35) {{: dolu koltuk}}; \\draw[thick,fill=white] (3.3,-3.6) rectangle (3.8,-3.1); \\node[right,font=\\footnotesize] at (3.9,-3.35) {{: boş koltuk}};')
SK=fig('\n'.join(o))
q('0007',tipId='psk-koltuk',tip='Koltuk planı ve koşullu sıralama',z='zor',alt='Koltuk Planı',kaz='Koltuk planında üç ardışık boş koltuğu sayıp koşula uygun sıralamalarla çarparak oturma sayısını bulur.',kalip='hikâyeli',
 kart='K-PSK-07 (koltuk planı) · 3 sıra, 8 koltuk; 8 uygun üçlü pencere, Ece–Tuna yan yana olmasın',
 metin='Şekilde, bir sinema salonunun üç sırasındaki koltukların doluluk durumu verilmiştir. Ece, Tuna ve Su aynı sıradaki yan yana üç boş koltuğa oturacaklardır. Ece ile Tuna, birbirinin yanına oturmak istememektedir.\nBuna göre üç arkadaş, hangi koltuğa kimin oturduğu dikkate alınarak kaç farklı biçimde oturabilir?',
 dogru=v,yan=[(e[0],'Yan yana üç boş koltuğu 3’ten uzun gruplarda tek pencere sayıp (4 grup) Su’nun ortada olduğu 2 sıralamayla çarpmış.','bilgi'),(e[1],'Her pencerede ortadaki kişiyi seçmiş (3 yol), diğer ikisinin sırasını saymamış: 8 × 3.','islem'),(e[2],'Yalnız Ece’nin ortada oturmamasını koşul sanmış: 8 × 4.','dikkat'),(e[3],'Ece ile Tuna’nın birbirinin yanına oturmama koşulunu atlayıp 3! sıralamayı almış: 8 × 6.','dikkat')],
 istenen='Üç arkadaşın farklı oturma sayısı.',ip=['Her sırada ardışık üç boş koltuktan oluşan yerleri tek tek say; sıra uzunluğu 3’ten büyükse üst üste binen yerler de ayrı sayılır.'],bilgi=[KOLT],sekil=SK,
 ad=[A('1. sıra','Boş koltuk grupları 4 ve 2 uzunluğundadır; 4’lük grup 2 farklı üçlü verir.','2 üçlü'),A('2. ve 3. sıra','2. sırada 5’lik grup 3 üçlü, 3. sırada 3’lük grup 1 ve 4’lük grup 2 üçlü verir.','3 + (1 + 2) = 6 üçlü'),A('Toplam üçlü','Tüm sıraların üçlüleri toplanır.','2 + 3 + 3 = 8 üçlü'),A('Sıralama','Ece ile Tuna yan yana olmayacağından Su ortada oturmalıdır; Ece ile Tuna uçlara 2 biçimde yerleşir.','2 sıralama'),A('Çarp','Her üçlü için 2 oturma düzeni vardır.','8 × 2 = 16')],
 puf='Pencereleri sayarken uzunluğu 3’ü aşan bir grup, kayarak birden çok üçlü verir.')

bitir(P,'permsek',UK)
