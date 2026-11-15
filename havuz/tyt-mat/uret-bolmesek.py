"""Bölme ve Bölünebilme · şekilli paket (bolmesek): 10 soru, hepsi şekilli/tablolu. Kardeş yok, ipucu 1. Her cevap ve çeldirici değer kodla hesaplanıp assert edilir.
Şekil koordinatları ve sayılar Python'da üretilir; TikZ gövdesi aynı değerlerden f-string ile yazılır (bkz. havuz/URETIM-SEKIL.md)."""
import sys,os,math
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
H.KONU='Bölme ve Bölünebilme'
P=Parti('bolmesek','Bölme ve Bölünebilme','mat|Bölme ve Bölünebilme')
KY='ÖSYM 2018–2026 TYT Matematik (şekilli/tablolu bölünebilme ve kalan soruları, yalnız mantık) · MEB 6–9. sınıf'
TP=lambda g:tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'+g+'\n\\end{tikzpicture}')

KAL=B('Kalanlı bölme','bölünen = bölen × bölüm + kalan ve 0 ≤ kalan < bölen. Örnek: 17 = 5 × 3 + 2 (kalan 2, bölen 5’ten küçük)')
GUN=B('Günlerde kalan','7 gün sonra aynı gün gelir; bu yüzden gün sayısının 7 ile bölümünden kalan kadar ilerlenir. Örnek: Pazartesi + 9 gün → 9 = 7 + 2, kalan 2 → Çarşamba')
KALAR=B('Kalanlarla işlem','toplamın ya da çarpımın kalanı, kalanların toplamının ya da çarpımının kalanıdır. Örnek: 17 ve 20’nin 6 ile kalanları 5 ve 2; 17 + 20 = 37 → kalan 1, 5 + 2 = 7 → kalan 1')
PER=B('Tekrarlanan dizilim','n elemanlı bir dizide, t elemanlık düzen n ÷ t işleminin bölümü kadar tam tekrarlanır; kalan, düzenin başından kaç elemanın daha geldiğini söyler. Örnek: 3 elemanlık düzen 10 elemana yazılırsa 3 tam tekrar ve 1 eleman fazla olur')
ASAL=B('Aralarında asal çarpanlar','sayı, aralarında asal çarpanlarına ayrılır ve her çarpana ayrı ayrı bölünme aranır. Örnek: 12 = 3 × 4 ve 3 ile 4 aralarında asaldır; 12’ye bölünen sayı hem 3’e hem 4’e bölünür')
S4=B('4 ile bölünebilme','son iki basamağın oluşturduğu sayı 4’ün katıysa sayı 4’e tam bölünür. Örnek: 316 → 16 = 4 × 4, bu yüzden 316 sayısı 4’e bölünür')
R11=B('11 ile bölünebilme','sağdan başlayarak rakamlara sırayla +, −, +, … işareti verilip toplanır; sonuç 0 ya da 11’in katıysa sayı 11’e bölünür. Örnek: 2541 → 1 − 4 + 5 − 2 = 0, 11’e bölünür')
R3=B('3 ile bölünebilme','rakamlar toplamı 3’ün katıysa sayı 3’e tam bölünür. Örnek: 252 → 2 + 5 + 2 = 9, 3’e bölünür')
KAT=B('Katlar ve sayma','1’den n’e kadar olan sayılar arasında k’nın katlarının sayısı n ÷ k işleminin bölümüdür. Örnek: 1’den 50’ye kadar 6’nın 8 katı vardır (50 ÷ 6 = 8 kalan 2)')

kart('K-BLS-01','Bölme şeması','Şekilde bölünen, bölen, bölüm ve kalan kutularından verilenler okunur; bölünen = bölen × bölüm + kalan eşitliğiyle eksik kutular bulunur ya da zincirleme yazılır.','Bölümü ve kalanı karıştırmak; yukarı yuvarlayıp negatif kalan kullanmak; zincirde ilk kalanı atlamak.','orta','şekilli',3,'bls-bolme','Bölme işleminin şematik yazımı',KY)
kart('K-BLS-02','Takvim yaprağı','Takvimden bir ayın son günü okunur; ertesi ayın ilk günü ve istenen gün 7’ye bölümünden kalanla bulunur.','Yeni ayın ilk gününü ayın son günüyle aynı sanmak; yanlış ayı kullanmak; 22. gün için 22 gün ilerlemek.','orta','şekilli',3,'bls-takvim','Takvim yaprağında kalan',KY)
kart('K-BLS-03','Sayı ızgarası','Izgaradaki yazım düzeni (yılan ya da satır satır) ve boyalı hücrelerin kuralı okunur; sütun konumu 5’e bölümden kalanla, boyama kuralı ortak katla (6 ya da 15 aralıkla) belirlenir.','Yılan düzeninde çift satırların ters yazıldığını unutmak; “kaç tane” sayarken ilk terimi eklememek.','orta','tablo',3,'bls-izgara','Sayı ızgarasında konum ve boyalı hücreler',KY)
kart('K-BLS-04','Rakamı eksik sayı kartı','Kartlardaki bilinmeyen rakamlar, 4, 3 ve 11 gibi bölünebilme kurallarının hepsi birlikte uygulanıp sınırlanır ve en büyük sayı seçilir.','Koşullardan birini (özellikle 11) atlamak; son iki basamak kuralını yanlış basamaklara uygulamak.','zor','şekilli',4,'bls-kart','Rakamı eksik sayı kartı',KY)
kart('K-BLS-05','Eşit paylaştırma şeması','Şekilde eşit kutular ve artan ürün sayısı okunup toplam bulunur; yeni bölen için kalan alınır.','Kalanı bölümle karıştırmak; artan ürünü kalan sanmak; kalanları toplayıp yeniden bölmemek.','kolay','şekilli',3,'bls-paylas','Kutulara eşit paylaştırma ve artan',KY)
kart('K-BLS-06','Periyodik dizilim','Dizinin tekrar eden düzeni (periyot) okunur; eleman sayısı periyoda bölünüp tam tekrar ve artan kısım ayrı ayrı sayılır.','Artan kısmı hesaba katmamak; oranla yuvarlamak; periyodu yanlış saymak.','orta','şekilli',3,'bls-dizi','Periyodik renk dizisinde sayma',KY)
kart('K-BLS-07','Çark ve kalan','Çark dilim sayısına göre toplam ilerleme mod alınır; konum çarkın üzerindeki sayıdan okunur.','Başlangıç dilimini de saymak; yön hatası; toplamı yanlış hesaplamak (n yerine n − 1).','zor','şekilli',4,'bls-cark','Çarkta ilerleme ve kalan',KY)
kart('K-BLS-09','Saat ve kalan','Saatteki konum okunur; ileri sayılacak saat sayısının 12 ile bölümünden kalan başlangıç konumuna eklenip 12’yi aşarsa 12 çıkarılır.','Kalanı cevap sanmak; bir saat eksik ya da fazla saymak; geri doğru ilerlemek.','orta','şekilli',3,'bls-saat','Saat üzerinde kalan',KY)
kart('K-BLS-08','Bölünebilme akış şeması','Akış şemasındaki koşullar sırayla uygulanır; “önce olmayan ve sonra olan” kümenin eleman sayısı ortak katla sayılır.','Koşulların sırasını görmezden gelmek; iki koşula uyanları iki kez saymak ya da çıkarmamak.','orta','şekilli',4,'bls-akis','Bölünebilme akış şemasında sayma',KY)

SIK_GUN=['Salı','Çarşamba','Perşembe','Cuma','Cumartesi']
GN=['Pazartesi','Salı','Çarşamba','Perşembe','Cuma','Cumartesi','Pazar']
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)

def bolme_diyagram(ox,ust,bolen,bolum,kalan,ust_etiket=True):
    s=f'\\node at ({ox},0) {{\\large {ust}}};\\draw[thick] ({ox+.75},.38)--({ox+.75},-1.28);\\draw[thick] ({ox+.75},-.38)--({ox+2.35},-.38);'
    s+=f'\\node at ({ox+1.55},0) {{\\large {bolen}}};'
    s+=f'\\node[draw,minimum size=.62cm,inner sep=0pt] at ({ox+1.55},-.88) {{\\large {bolum}}};'
    s+=f'\\draw ({ox-.4},-.38)--({ox+.4},-.38);'
    s+=f'\\node[draw,minimum size=.62cm,inner sep=0pt] at ({ox},-.88) {{\\large {kalan}}};'
    s+=f'\\node[font=\\scriptsize] at ({ox},.72) {{bölünen}};\\node[font=\\scriptsize] at ({ox+1.55},.72) {{bölen}};\\node[font=\\scriptsize] at ({ox+1.55},-1.5) {{bölüm}};\\node[font=\\scriptsize] at ({ox},-1.5) {{kalan}};'
    return s

# ---------- 01 · kolay · bölme şeması ----------
N1,d1=89,12; b1,k1=divmod(N1,d1); assert (b1,k1)==(7,5) and b1+k1==12
assert b1-k1==2 and k1==5 and b1==7 and 89//12+1==8 and (b1+1)+k1!=12
sek=TP(bolme_diyagram(0,N1,d1,'B','K'))
q('0001',tipId='bls-bolme',tip='Bölme işleminin şematik yazımı',z='kolay',alt='Bölme İşlemi',kaz='Şekilde verilen bölme işleminden bölüm ve kalanı bulup toplamlarını hesaplar.',kalip='şekilli',sekil=sek,
 kart='K-BLS-01 (bölme şeması) · bölünen ve bölen verilip bölüm ile kalan kutularının toplamı',
 metin='Şekilde, doğal sayılarla yapılan bir bölme işlemi gösterilmiştir. B bölümü, K kalanı göstermektedir.\nBuna göre B + K toplamı kaçtır?',
 dogru=12,yan=[(2,'Bölüm ile kalanın farkını (7 − 5) almış; toplam isteniyordu.','dikkat'),(5,'Yalnız kalanı (K = 5) yazmış; bölümü toplama katmamış.','dikkat'),(7,'Yalnız bölümü (B = 7) yazmış; kalanı toplama katmamış.','dikkat'),(8,'Bölümü yukarı yuvarlayıp 8 bulmuş; 12 × 8 = 96 > 89 olduğundan bölüm 7’dir.','islem')],
 istenen='B + K toplamı.',
 ip=['Bölünen, bölenin hangi katına en çok yaklaşır ve geriye ne kalır?'],
 bilgi=[KAL],
 ad=[A('Bölümü bul','12’nin 89’a kadar en büyük katını bul.','12 × 7 = 84 ve 12 × 8 = 96 > 89 → B = 7'),A('Kalanı bul','Bölünenden bölen × bölüm çıkarılır.','K = 89 − 84 = 5 (0 ≤ 5 < 12)'),A('Topla','Bölüm ile kalanı topla.','B + K = 7 + 5 = 12')],
 puf='Şemadaki kutuları “bölünen = bölen × bölüm + kalan” eşitliğine yerleştirip kalanın bölenden küçük olduğunu denetle.')

# ---------- 02 · orta · takvim yaprağı ----------
bas=1 # Salı = indeks 1
gun_sayisi=31; son=(bas+gun_sayisi-1)%7; assert GN[son]=='Perşembe'
ertesi1=(son+1)%7; assert GN[ertesi1]=='Cuma'
d22=(ertesi1+21)%7; assert GN[d22]=='Cuma' and (bas+31+21)%7==d22
assert GN[(bas+21)%7]=='Salı' and GN[(son-1)%7]=='Çarşamba' and GN[(son-1+21)%7]=='Çarşamba' and GN[(son+21)%7]=='Perşembe' and GN[(ertesi1+22)%7]=='Cumartesi'
hucre=[None]*bas+list(range(1,gun_sayisi+1)); hucre+= [None]*((-len(hucre))%7)
satir=len(hucre)//7; cw,ch=.82,.56
g=''
bas_ad=['Pzt','Sal','Çar','Per','Cum','Cmt','Paz']
for j,t in enumerate(bas_ad):
    g+=f'\\fill[gray!25] ({j*cw},0) rectangle ({(j+1)*cw},{ch});\\node[font=\\scriptsize] at ({(j+.5)*cw},{ch/2}) {{{t}}};'
for i in range(satir):
    for j in range(7):
        v=hucre[i*7+j]; y0=-(i)*ch; 
        fl='fill=vurgu!20,' if v==gun_sayisi else ''
        g+=f'\\draw[{fl}] ({j*cw},{y0}) rectangle ({(j+1)*cw},{y0-ch});'
        if v: g+=f'\\node at ({(j+.5)*cw},{y0-ch/2}) {{{v}}};'
g+=f'\\draw[thick] (0,0) rectangle ({7*cw},{ch}); \\draw[thick] (0,{ch}) rectangle ({7*cw},{-satir*ch});'
sek=TP(g)
q('0002',tipId='bls-takvim',tip='Takvim yaprağında kalan',z='orta',alt='Günlerde Kalan',kaz='Takvim yaprağından ayın son gününü okuyup ertesi ayın belirli bir gününün haftanın hangi günü olduğunu bulur.',kalip='şekilli',sekil=sek,
 kart='K-BLS-02 (takvim yaprağı) · ay sonu okunup ertesi ayın 22’si sorulur',
 metin='Yukarıda bir ayın takvim yaprağı verilmiştir.\nBuna göre bu ayı hemen izleyen ayın 22’si haftanın hangi günüdür?',
 dogru='Cuma',sira=SIK_GUN,
 yan=[('Salı','Bu ayın 22’sini bulmuş: 1. gün Salı, 22 = 1 + 21 olduğundan yine Salı; soru izleyen ayı soruyor.','dikkat'),('Çarşamba','Ay sonundan ertesi güne geçerken Perşembe yerine bir önceki günü (Çarşamba) alıp izleyen ayın 1’ini Çarşamba bulmuş; 21 gün tam hafta olduğundan 22’sini de Çarşamba bulmuş.','dikkat'),('Perşembe','Ertesi ayın 1’ini ayın son günüyle (Perşembe) aynı sanmış; ardından 21 gün sonra yine Perşembe bulmuş.','dikkat'),('Cumartesi','Ertesi ayın 1’i Cuma’yı doğru bulmuş ama 22. güne 21 değil 22 gün ilerleyerek Cumartesi demiş.','islem')],
 istenen='İzleyen ayın 22’sinin günü.',
 ip=['Takvimde ayın son gününün hangi güne denk geldiğine bak; sonra 7 günlük tekrarı kullan.'],
 bilgi=[GUN],
 ad=[A('Ay sonunu oku','Takvimde 31, Perşembe sütunundadır.','Ayın son günü Perşembe'),A('Yeni ayın 1’i','Ertesi gün: Perşembe’den bir gün sonrası.','İzleyen ayın 1’i = Cuma'),A('22’yi bul','1’den 22’ye 21 gün vardır; 21 = 7 × 3, hafta tam tekrarlanır.','22. gün = 1. günle aynı = Cuma')],
 puf='Aynı haftanın günü her 7 günde bir tekrarlanır: bir ayın 1., 8., 15., 22., 29. günleri hep aynı güne denk gelir.')

# ---------- 03 · orta · yılan ızgara, boyalı sütun toplamı ----------
def yilan(n,s=5):
    pos={}
    for v in range(1,n+1):
        r=(v-1)//s; c=(v-1)%s
        pos[v]=(r,c if r%2==0 else s-1-c)
    return pos
pz=yilan(45); sut=[v for v in range(1,46) if pz[v][1]==4]
assert sut==[5,6,15,16,25,26,35,36,45] and sum(sut)==209
assert sum(range(5,46,5))==225 and 5+6+15+16==42 and 5+6+15+16+25+26+35==128 and 5+6+15+16+25+26+35+36==164
cs=.78; g=''
for v in range(1,21):
    r,c=pz[v]; fl='fill=vurgu!25,' if c==4 else ''
    g+=f'\\draw[{fl}] ({c*cs},{-r*cs}) rectangle ({(c+1)*cs},{-(r+1)*cs});\\node at ({(c+.5)*cs},{-(r+.5)*cs}) {{{v}}};'
for r in range(4):
    y=-(r+.5)*cs; g+=('\\draw[-{Stealth[length=1.6mm]}] (-.55,%.2f) -- (-.12,%.2f);'%(y,y)) if r%2==0 else ('\\draw[-{Stealth[length=1.6mm]}] (-.12,%.2f) -- (-.55,%.2f);'%(y,y))
sek=TP(g)
q('0003',tipId='bls-izgara',tip='Sayı ızgarasında konum ve boyalı hücreler',z='orta',alt='Sayma ve Kalan',kaz='Yılan düzeninde yazılan sayı tablosunda belirli bir sütundaki sayıları belirleyip toplar.',kalip='tablo',sekil=sek,
 kart='K-BLS-03 (sayı ızgarası) · yılan düzeninde 45’e kadar boyalı son sütunun sayıları toplamı',
 metin='Aşağıdaki tabloda 5 sütunlu bir ızgaraya 1’den başlayarak doğal sayılar yazılmaktadır: tek numaralı satırlar soldan sağa, çift numaralı satırlar sağdan sola yazılır (oklar yönü gösterir). Son sütun boyanmıştır. Yazma işlemi aynı biçimde 45’e kadar sürdürülüyor.\nBuna göre boyalı sütunda bulunan sayıların toplamı kaçtır?',
 dogru=209,yan=[(42,'Yalnız şekildeki 4 satırdaki boyalı sayıları (5 + 6 + 15 + 16) toplamış; tablo 45’e kadar sürüyor.','dikkat'),(128,'Satırları 35’te bitirip 7 satır almış; 36 ve 45’in de boyalı sütunda olduğunu atlamış.','dikkat'),(164,'Satırları 40’ta bitirip 8 satır almış; 45 sayısının 9. satırın son sütununda olduğunu atlamış.','dikkat'),(225,'Çift satırların ters yazıldığını unutup boyalı sütuna 5, 10, …, 45 sayılarını yerleştirmiş.','bilgi')],
 istenen='Boyalı sütundaki sayıların toplamı.',
 ip=['Tek ve çift satırlarda son sütuna düşen sayıları ayrı ayrı yaz.'],
 bilgi=[B('Yılan düzeni','ilk satır soldan sağa yazılıyorsa, ikinci satırın ilk yazılan sayısı sağ sütuna düşer; her satırda 5 sayı yazılır. Örnek: 5 sütunda 6, 7, 8, 9, 10 sayıları ikinci satıra sağdan sola yazılınca 6 son sütunda olur')],
 ad=[A('Satır sayısını bul','45 sayı, satır başına 5 sayı yazılınca 9 satır eder.','45 ÷ 5 = 9 satır'),A('Tek satırlar','Soldan sağa yazılan 1., 3., 5., 7., 9. satırlarda son sütuna satırın son sayısı düşer.','5, 15, 25, 35, 45'),A('Çift satırlar','Sağdan sola yazılan 2., 4., 6., 8. satırlarda son sütuna satırın ilk sayısı düşer.','6, 16, 26, 36'),A('Topla','Boyalı sütundaki 9 sayıyı topla.','5 + 6 + 15 + 16 + 25 + 26 + 35 + 36 + 45 = 209')],
 puf='Yılan düzeninde çift satırlarda yön terstir; son sütundaki sayılar 5, 6, 15, 16, … biçiminde ikişerli gruplar hâlinde ilerler.')

# ---------- 04 · zor · rakamı eksik kart ----------
def sol(d,tpl='7A2B6'):
    return [int(tpl.replace('A',str(a)).replace('B',str(b))) for a in range(10) for b in range(10) if int(tpl.replace('A',str(a)).replace('B',str(b)))%d==0]
S132=sol(132); assert S132==[76296,78276]
m12=max(sol(12)); m11=max(sol(11)); m33=max(sol(33)); m44=max(sol(44))
assert (m12,m33,max(sol(36)),min(S132))==(79296,79266,79236,76296)
assert 78276%12==0 and 78276%11==0 and 78276==132*593
kt=['7','A','2','B','6']; g=''
for i,t in enumerate(kt):
    g+=f'\\draw[thick,{"fill=vurgu!15" if t in "AB" else "fill=none"}] ({i*.95},0) rectangle ({i*.95+.8},1.1);\\node at ({i*.95+.4},.55) {{\\Large {t}}};'
sek=TP(g)

q('0004',tipId='bls-kart',tip='Rakamı eksik sayı kartı',z='zor',alt='Bölünebilme Kuralları',kaz='Rakamları kartlarla verilen sayının 12 ve 11 ile bölünebilmesi koşullarını birlikte uygulayıp en büyük sayıyı bulur.',kalip='şekilli',sekil=sek,
 kart='K-BLS-04 (rakamı eksik sayı kartı) · 7A2B6 kartı, 12 ve 11 ile bölünebilen en büyük sayı',
 metin='Şekildeki kartlarla beş basamaklı bir doğal sayı oluşturulmuştur. A ve B birer rakamdır. Oluşan sayı hem 12 ile hem 11 ile tam bölünmektedir.\nBuna göre bu sayı en çok kaçtır?',
 dogru=78276,yan=[(76296,'İki çözümden (76296 ve 78276) küçüğünü seçmiş; “en çok” isteniyordu.','dikkat'),(79236,'12’ye bölünmeyi doğru uygulayıp 11 yerine 9 kuralını (rakam toplamı 9’un katı) kullanmış; böylece 36’ya bölünen en büyük sayıyı bulmuş.','bilgi'),(79266,'4 ile bölünme koşulunu atlamış; yalnız 3 ve 11 koşullarını uygulayıp son iki basamağı denetlememiş (66 sayısı 4’ün katı değil).','dikkat'),(79296,'11 ile bölünme koşulunu atlamış; yalnız 12’ye (3 ve 4) bölünen en büyük sayıyı yazmış.','dikkat')],
 istenen='Sayının en büyük değeri.',
 ip=['12 ve 11 bölenlerinin aralarında asal parçaları neler? Her kural ayrı ayrı rakamlara ne söylüyor?'],
 bilgi=[S4,R3,R11],
 ad=[A('4 ile bölünme','Son iki basamak B6 sayısı 4’ün katıdır; bu yalnız tek B rakamlarında olur.','16, 36, 56, 76, 96 → B ∈ {1, 3, 5, 7, 9}'),A('11 ile bölünme','Sağdan alternatif toplam: 6 − B + 2 − A + 7 = 15 − (A + B) sıfır ya da 11’in katı olmalı.','A + B = 15 ya da A + B = 4'),A('3 ile bölünme','Rakamlar toplamı 15 + (A + B) 3’ün katı olmalı; A + B = 4 için 19 olur, uygun değildir.','A + B = 15 (rakam toplamı 30)'),A('Çözümleri bul ve seç','B tek ve A + B = 15: B = 9, A = 6 ya da B = 7, A = 8. B = 5 için A = 10 rakam olamaz.','76296 ve 78276 → en büyüğü 78276')],
 puf='12 gibi bileşik bölenleri aralarında asal çarpanlara ayır; her kuralı ayrı ayrı uygulayıp ortak çözümleri en sonda kesiştir.')

# ---------- 05 · kolay · kutulara eşit paylaştırma, artan ----------
kut,ic,art=5,12,7; top=kut*ic+art; assert top==67 and top%8==3
assert (kut*ic)%8==4 and 4+7==11 and top//8==8 and art==7
def noktalar(x0,y0,n,c=4,dx=.3,dy=.25):
    s=''
    for i in range(n): s+=f'\\fill ({x0+(i%c)*dx:.3f},{y0-(i//c)*dy:.3f}) circle (.07);'
    return s
g=''
for i in range(kut):
    x=i*1.6; g+=f'\\draw[thick] ({x},0) rectangle ({x+1.3},-1.0);'+noktalar(x+.2,-.2,ic)+f'\\node[font=\\small] at ({x+.65},-1.3) {{{ic}}};'
xl=kut*1.6+.1
pts=[(0,0),(.4,-.3),(.8,.05),(.2,-.6),(.65,-.65),(1.0,-.35),(1.15,-.75)]
for (a,b) in pts: g+=f'\\fill ({xl+a:.2f},{b-.1:.2f}) circle (.07);'
g+=f'\\node[font=\\small] at ({xl+.55},-1.3) {{{art}}};'
g+='\\fill (0,-1.95) circle (.07);\\node[font=\\scriptsize,anchor=west] at (.15,-1.95) {: 1 kalem};'
sek=TP(g)
q('0005',tipId='bls-paylas',tip='Kutulara eşit paylaştırma ve artan',z='kolay',alt='Kalan Aritmetiği',kaz='Şekilde eşit kutulara yerleştirilmiş ve artan kalemlerin toplamını bulup yeni bir bölenle kalanı hesaplar.',kalip='şekilli',sekil=sek,
 kart='K-BLS-05 (eşit paylaştırma şeması) · 5 kutu × 12 kalem + 7 artan, 8’erli paketleme',
 metin='Şekilde, her birinde eşit sayıda kalem bulunan kutular ve kutulara girmeyen kalemler gösterilmiştir (altlarındaki sayılar kalem sayısını belirtir). Her nokta bir kalemi göstermektedir. Bu kalemlerin tamamı 8’erli paketlenecektir.\nBuna göre paketlere girmeden kalan kalem sayısı kaçtır?',
 dogru=3,yan=[(4,'Yalnız kutulardaki 60 kalemi paketlemiş (60 ÷ 8 → kalan 4); kutulara girmeyen 7 kalemi unutmuş.','dikkat'),(7,'Kutulara girmeyen 7 kalemi kalan sanıp 67 ÷ 8 işlemini yapmamış.','dikkat'),(8,'Kalanı değil bölümü (67 ÷ 8 = 8) yazmış.','dikkat'),(11,'Kalanları (4 ve 7) toplayıp 11 bulmuş; 11 bölenden büyük olduğu için bir paket daha yapılabilir, yeniden bölmemiş.','islem')],
 istenen='Paketlere girmeden kalan kalem sayısı.',
 ip=['Önce şekildeki tüm kalemlerin sayısını bul.'],
 bilgi=[KAL],
 ad=[A('Toplamı bul','5 kutuda 12’şer kalem ve 7 kalem daha vardır.','5 × 12 + 7 = 67'),A('8’e böl','67’nin 8 ile bölümü: 8 × 8 = 64.','67 = 8 × 8 + 3'),A('Kalanı oku','Paketlere girmeyen kalem sayısı kalandır.','kalan = 3')],
 puf='Kalanlar toplanınca bölenden büyük çıkabilir; sonucu bir kez daha bölenle böl.')

# ---------- 06 · orta · periyodik boncuk dizisi ----------
dz='YBBSYBS'  # Y yeşil, B beyaz, S siyah (period 7)
n6=150; t,r=divmod(n6,7); assert (t,r)==(21,3)
bey=t*dz.count('B')+dz[:r].count('B'); assert bey==65
assert t*3==63 and round(n6*3/7)==64 and t*3+r==66 and (t+1)*3+dz[:r].count('B')==68
yol=[(i,c) for i,c in enumerate(dz*2)]
g=''
for i,c in enumerate(dz*2+dz[:2]):
    x=i*.5; st={'Y':'fill=vurgu!60','B':'fill=none','S':'fill=black'}[c]
    g+=f'\\draw[thick,{st}] ({x},0) circle (.19);'
g+=f'\\node at ({16*.5+.15},0) {{$\\cdots$}};'
g+=f'\\draw[<->] (-.2,-.5) -- ({7*.5-.3},-.5);\\node[font=\\scriptsize] at ({7*.25-.25},-.75) {{bir düzen}};'
sek=TP(g)
q('0006',tipId='bls-dizi',tip='Periyodik renk dizisinde sayma',z='orta',alt='Periyodik Dizilim',kaz='Şekildeki tekrarlanan boncuk düzeninden belirli sayıdaki boncuk içinde bir rengin kaç kez geçtiğini bulur.',kalip='şekilli',sekil=sek,
 kart='K-BLS-06 (periyodik dizilim) · 7’li düzen, ilk 150 boncukta beyaz sayısı',
 metin='Şekilde bir kolyenin başlangıç kısmı gösterilmiştir. Kolyedeki boncuklar (yeşil, beyaz, siyah) soldan sağa doğru şekildeki 7 boncuklu düzen bozulmadan tekrarlanarak dizilmiştir.\nBu kolyenin ilk 150 boncuğu arasında kaç tane beyaz boncuk vardır?',
 dogru=65,yan=[(63,'Yalnız 21 tam düzeni saymış (21 × 3); artan 3 boncuktaki beyazları (2 tane) eklememiş.','dikkat'),(64,'Oranla yaklaşık hesaplamış: 150 × 3 ÷ 7 ≈ 64; düzen tam bölünmediğinden bu yöntem kesin değildir.','islem'),(68,'22 tam düzen almış (22 × 3 = 66) ve artana 2 beyaz eklemiş; 150 = 21 × 7 + 3 olduğundan 22. düzen tamamlanmaz.','dikkat'),(66,'Artan 3 boncuğun hepsini beyaz sanıp 63 + 3 = 66 bulmuş; artanda yalnız 2 beyaz vardır (ilk boncuk yeşil).','dikkat')],
 istenen='İlk 150 boncuktaki beyaz boncuk sayısı.',
 ip=['150 boncuğun kaç tam düzen ve kaç boncuk daha içerdiğine bak.'],
 bilgi=[PER],
 ad=[A('Düzeni oku','7 boncuklu düzen: yeşil, beyaz, beyaz, siyah, yeşil, beyaz, siyah; her düzende 3 beyaz var.','bir düzende 3 beyaz'),A('Tam düzenleri say','150’yi 7’ye böl.','150 = 7 × 21 + 3 → 21 tam düzen, 3 boncuk artar'),A('Artanı incele','Artan 3 boncuk düzenin ilk üçüdür: yeşil, beyaz, beyaz.','artanda 2 beyaz'),A('Topla','Tam düzenlerdeki ve artandaki beyazları topla.','21 × 3 + 2 = 65')],
 puf='“İlk n eleman” sorularında n’yi düzenin uzunluğuna böl; bölüm tam tekrarları, kalan ise başlangıçtan alınacak elemanları verir.')

# ---------- 07 · zor · çark, üçgensel ilerleme ----------
Lc=[7,2,5,9,1,4,8,3,6]; assert sorted(Lc)==list(range(1,10))
n7=40; T=n7*(n7+1)//2; assert T==820 and T%9==1 and Lc[T%9]==2
w1=Lc[((n7-1)*n7//2)%9]; w2=Lc[n7%9]; w3=Lc[(T+1)%9]; w4=Lc[(-T)%9]
assert (w1,w2,w3,w4)==(8,1,5,6) and len({2,w1,w2,w3,w4})==5
import math as _m
g='';R=1.55
for i in range(9):
    c=90-40*i; a1=_m.radians(c-20)
    g+=f'\\draw ({.55*_m.cos(a1):.3f},{.55*_m.sin(a1):.3f}) -- ({R*_m.cos(a1):.3f},{R*_m.sin(a1):.3f});'
    a=_m.radians(c); g+=f'\\node at ({1.07*_m.cos(a):.3f},{1.07*_m.sin(a):.3f}) {{\\large {Lc[i]}}};'
g+=f'\\draw[thick] (0,0) circle ({R});\\draw (0,0) circle (.55);\\fill (0,0) circle (.06);'
g+=f'\\draw[-{{Stealth[length=2.4mm]}},very thick,vurgu] (0,{R+.8}) -- (0,{R+.12});'
g+=f'\\draw[-{{Stealth[length=2mm]}}] ({(R+.35)*_m.cos(_m.radians(62)):.3f},{(R+.35)*_m.sin(_m.radians(62)):.3f}) arc[start angle=62,delta angle=-38,radius={R+.35}];'
g+=f'\\node[font=\\scriptsize,anchor=west] at ({(R+.5)*_m.cos(_m.radians(45)):.3f},{(R+.5)*_m.sin(_m.radians(45))+.0:.3f}) {{saat yönü}};'
sek=TP(g)
q('0007',tipId='bls-cark',tip='Çarkta ilerleme ve kalan',z='zor',alt='Kalan Aritmetiği',kaz='Dilimleri numaralı bir çarkta artan adımlarla ilerleyen ibrenin son konumunu toplam ilerlemenin 9 ile bölümünden kalanla bulur.',kalip='şekilli',sekil=sek,
 kart='K-BLS-07 (çark ve kalan) · 9 dilimli çark, 1+2+…+40 dilim ilerleme',
 metin='Şekildeki çark 9 eş dilime ayrılmıştır ve dilimlerin üzerine birer sayı yazılmıştır. Yeşil ok, başlangıçta ibrenin bulunduğu dilimi göstermektedir. İbre her hamlede saat yönünde ilerler: 1. hamlede 1 dilim, 2. hamlede 2 dilim, 3. hamlede 3 dilim, … , her hamlede bir önceki hamleden 1 dilim fazla.\nBuna göre 40. hamleden sonra ibre, üzerinde hangi sayı yazılı olan dilimde durur?',
 dogru=2,yan=[(w1,'Toplam ilerlemeyi 1 + 2 + … + 39 = 780 almış (39 hamle); 780’in 9 ile bölümünden kalan 6’dır.','dikkat'),(w2,'Her hamlede 1 dilim ilerlediğini sanıp 40 hamlede 40 dilim saymış; 40’ın 9 ile bölümünden kalan 4’tür.','bilgi'),(w3,'Toplam ilerlemeyi doğru (820, kalan 1) bulmuş ama başlangıç dilimini de sayarak bir dilim fazla ilerlemiş.','dikkat'),(w4,'820 dilimi saat yönünün tersinde saymış; konum (−820) mod 9 = 8 olur.','dikkat')],
 istenen='40. hamle sonunda ibrenin bulunduğu dilimdeki sayı.',
 ip=['Her hamlede ilerleme miktarı değişiyor; 40 hamlede toplam ne kadar ilerlenmiştir?'],
 bilgi=[B('Ardışık sayıların toplamı','1’den n’ye kadar sayıların toplamı n × (n + 1) ÷ 2’dir. Örnek: 1 + 2 + … + 10 = 10 × 11 ÷ 2 = 55'),KALAR],
 ad=[A('Toplam ilerleme','40 hamlede ilerlenen dilimler 1 + 2 + … + 40 toplamıdır.','40 × 41 ÷ 2 = 820 dilim'),A('Çarkta konum','9 dilimde bir başa dönülür; 820’nin 9 ile bölümünden kalanı bul.','820 = 9 × 91 + 1 → kalan 1'),A('Konumu işaretle','Okla gösterilen başlangıç diliminden saat yönünde 1 dilim ileri gidilir.','Başlangıç dilimi 7, bir sonraki dilim 2'),A('Sayıyı oku','Şekilde ok diliminden sonraki dilimin sayısı 2’dir.','Cevap 2')],
 puf='Çarkta tam turlar konumu değiştirmez; yalnız toplam ilerlemenin dilim sayısına bölümünden kalan kadar ilerlenir.')

# ---------- 08 · zor · bölünebilme akış şeması ----------
n8=150; A8=n8//4; M3=n8//3; M12=n8//12; B8=M3-M12; C8=n8-A8-B8
assert (A8,M3,M12,B8,C8)==(37,50,12,38,75) and B8==sum(1 for n in range(1,151) if n%4 and n%3==0)
assert M3+M12==62 and n8-A8==113 and sum(1 for n in range(1,151) if n%4==0)==37
g=''
def dm(cx,cy,w,h,t): return f'\\draw ({cx-w},{cy}) -- ({cx},{cy+h}) -- ({cx+w},{cy}) -- ({cx},{cy-h}) -- cycle;\\node[font=\\scriptsize,align=center] at ({cx},{cy}) {{{t}}};'
g+='\\node[draw,rounded corners=6pt,minimum width=2.3cm,minimum height=.62cm,font=\\scriptsize] at (0,0) {$n$ sayısı girilir};'
g+='\\draw[-{Stealth[length=1.8mm]}] (0,-.31) -- (0,-.82);'
g+=dm(0,-1.5,1.55,.68,'$n$ sayısı 4 ile\\\\tam bölünüyor mu?')
g+='\\draw[-{Stealth[length=1.8mm]}] (1.55,-1.5) -- (2.75,-1.5);\\node[font=\\scriptsize] at (2.15,-1.28) {Evet};'
g+='\\node[draw,minimum width=1.9cm,minimum height=.62cm,font=\\scriptsize] at (3.85,-1.5) {A kutusu};'
g+='\\draw[-{Stealth[length=1.8mm]}] (0,-2.18) -- (0,-2.82);\\node[font=\\scriptsize,anchor=west] at (.08,-2.5) {Hayır};'
g+=dm(0,-3.5,1.55,.68,'$n$ sayısı 3 ile\\\\tam bölünüyor mu?')
g+='\\draw[-{Stealth[length=1.8mm]}] (1.55,-3.5) -- (2.75,-3.5);\\node[font=\\scriptsize] at (2.15,-3.28) {Evet};'
g+='\\node[draw,minimum width=1.9cm,minimum height=.62cm,font=\\scriptsize] at (3.85,-3.5) {B kutusu};'
g+='\\draw[-{Stealth[length=1.8mm]}] (0,-4.18) -- (0,-4.82);\\node[font=\\scriptsize,anchor=west] at (.08,-4.5) {Hayır};'
g+='\\node[draw,minimum width=1.9cm,minimum height=.62cm,font=\\scriptsize] at (0,-5.13) {C kutusu};'
sek=TP(g)
q('0008',tipId='bls-akis',tip='Bölünebilme akış şemasında sayma',z='orta',alt='Bölünebilme Kuralları',kaz='Bölünebilme koşullarından oluşan akış şemasında bir kutuya ulaşan sayıların adedini ortak kat ve içerme fikriyle bulur.',kalip='şekilli',sekil=sek,
 kart='K-BLS-08 (bölünebilme akış şeması) · 1’den 150’ye sayılar, 4’e bölünmeyen 3’ün katları',
 metin='Şekildeki akış şemasına 1’den 150’ye kadar (1 ve 150 dahil) her doğal sayı tek tek girilmekte ve sayı, koşullara göre A, B ya da C kutularından birine konulmaktadır.\nBuna göre B kutusuna konulan sayıların adedi kaçtır?',
 dogru=38,yan=[(50,'Yalnız “3 ile bölünüyor mu” koşuluna bakmış; 4’ün katı olup A kutusuna giden 12’nin katlarını (12 tane) çıkarmamış.','dikkat'),(62,'3’ün katlarının sayısına (50) 12’nin katlarının sayısını (12) ekleyerek içermeyi ters uygulamış.','islem'),(75,'B yerine C kutusunun eleman sayısını (150 − 37 − 38 = 75) hesaplamış.','dikkat'),(113,'4 ile bölünmeyen tüm sayıları (150 − 37) B kutusuna koymuş; 3 koşulunu hiç uygulamamış.','dikkat')],
 istenen='B kutusundaki sayıların adedi.',
 ip=['B kutusuna ulaşmak için hangi iki koşulun birlikte sağlanması gerektiğini sırayla yaz.'],
 bilgi=[KAT,ASAL],
 ad=[A('Koşulları oku','B kutusuna 4’e bölünmeyen ve 3’e bölünen sayılar ulaşır.','4’e bölünmez ∧ 3’e bölünür'),A('3’ün katlarını say','1’den 150’ye 3’ün katları.','150 ÷ 3 = 50'),A('A’ya gidenleri çıkar','Hem 3’ün hem 4’ün katı olanlar (12’nin katları) 4’e bölündükleri için A’ya gider.','150 ÷ 12 = 12 (kalan 6) → 12 sayı'),A('Sonuç','3’ün katlarından 12’nin katlarını çıkar.','50 − 12 = 38')],
 puf='Koşulların sırası önemlidir: önceki koşula uyan sayılar sonraki kutuya hiç ulaşmaz; “hem … hem …” olanlar ortak katla (EKOK) sayılır.')

# ---------- 09 · orta · zincirleme bölme şeması ----------
b9=7*5+3; a9=9*b9+4; assert (b9,a9)==(38,346) and a9%63==31 and divmod(a9,63)==(5,31)
assert 4+3==7 and 9*3==27 and a9==63*5+31
g=bolme_diyagram(0,'A',9,'B',4)+bolme_diyagram(4.2,'B',7,5,3)
sek=TP(g)
q('0009',tipId='bls-bolme',tip='Bölme işleminin şematik yazımı',z='orta',alt='Bölme İşlemi',kaz='Zincirleme iki bölme şemasından büyük sayıyı bulup başka bir bölenle kalanı hesaplar.',kalip='şekilli',sekil=sek,
 kart='K-BLS-01 (bölme şeması) · iki zincirleme bölme, A’nın 63 ile bölümünden kalan',
 metin='Şekilde, doğal sayılarla yapılan iki bölme işlemi gösterilmiştir. İkinci işlemdeki bölünen, birinci işlemdeki bölümle (B) aynı sayıdır.\nBuna göre A sayısının 63 ile bölümünden kalan kaçtır?',
 dogru=31,yan=[(4,'Yalnız birinci bölmenin kalanını (4) yazmış; ikinci işlemden gelen payı katmamış.','dikkat'),(5,'A = 63 × 5 + 31 yazıp kalan yerine 63 ile bölümü (5) vermiş.','dikkat'),(7,'İki işlemin kalanlarını toplamış (4 + 3); kalanlar farklı bölenlerle çarpılarak birleşir.','bilgi'),(27,'B = 7 × 5 + 3 yazıp A = 9 × (7 × 5 + 3) + 4’te yalnız 9 × 3 = 27’yi almış; 4’ü eklemeyi unutmuş.','islem')],
 istenen='A sayısının 63 ile bölümünden kalan.',
 ip=['Önce B’yi ikinci şemadan, sonra A’yı B cinsinden yaz.'],
 bilgi=[KAL],
 ad=[A('B’yi bul','İkinci şema: B = 7 × 5 + 3.','B = 38'),A('A’yı yaz','Birinci şema: A = 9 × B + 4; B yerine 7 × 5 + 3 yaz.','A = 9 × 38 + 4 = 346'),A('63 ile böl','9 × 7 = 63; 63 × 5 = 315.','346 = 63 × 5 + 31'),A('Kalanı denetle','31 < 63 olduğundan kalan 31’dir.','kalan = 31')],
 puf='Zincirleme bölmelerde içteki eşitliği dıştakine yerleştir; 9 × (7q + r) + s = 63q + (9r + s) olduğundan kalan 9r + s’dir.')

# ---------- 10 · orta · saat üzerinde kalan ----------
bs,h10=10,500; sonuc=(bs+h10-1)%12+1
assert h10%12==8 and sonuc==6 and ((bs+(h10-1))-1)%12+1==5 and (bs+h10+1-1)%12+1==7 and (bs-h10%12-1)%12+1==2
import math as _m
g='\\draw[thick] (0,0) circle (1.4);'
for k in range(12):
    a=_m.radians(90-30*k); g+=f'\\draw ({1.28*_m.cos(a):.3f},{1.28*_m.sin(a):.3f}) -- ({1.4*_m.cos(a):.3f},{1.4*_m.sin(a):.3f});\\node at ({1.05*_m.cos(a):.3f},{1.05*_m.sin(a):.3f}) {{{12 if k==0 else k}}};'
a=_m.radians(90-30*bs)
g+=f'\\draw[line width=2pt] (0,0) -- ({.62*_m.cos(a):.3f},{.62*_m.sin(a):.3f});\\draw[line width=1pt] (0,0) -- (0,.95);\\fill (0,0) circle (.06);'
sek=TP(g)
q('0010',tipId='bls-saat',tip='Saat üzerinde kalan',z='orta',alt='Kalan Aritmetiği',kaz='Saatteki konumu okuyup belirli sayıda saat sonrasındaki akrep konumunu 12 ile bölümünden kalanla bulur.',kalip='şekilli',sekil=sek,
 kart='K-BLS-09 (saat ve kalan) · 10’u gösteren saat, 500 saat sonra akrep',
 metin='Şekildeki analog saat, 12 saatlik düzende çalışmaktadır. Saat şekildeki zamanı gösterirken tam 500 saat sonra kurulacak bir alarm için bekleniyor.\nBuna göre alarm çaldığında akrep hangi sayıyı gösterir?',
 dogru=6,yan=[(2,'500 saat ileri yerine 8 saat geri giderek 10 − 8 = 2 bulmuş; saat ileri sarılmaktadır.','dikkat'),(5,'500 yerine 499 saat ilerleyip (kalan 7) 10 + 7 = 17 → 5 bulmuş; bir saat eksik saymış.','dikkat'),(7,'Başlangıç saatini de bir saat sayıp 10 + 8 + 1 = 19 → 7 bulmuş.','dikkat'),(8,'500’ün 12 ile bölümünden kalanı (8) akrebin göstereceği sayı sanmış; kalan, ileri gidilecek saat sayısıdır.','dikkat')],
 istenen='Alarm çaldığında akrebin gösterdiği sayı.',
 ip=['500 saatin kaç tam devir (12 saat) ve kaç saat fazla olduğuna bak; fazlayı başlangıç konumundan ilerlet.'],
 bilgi=[B('Saatte kalan','12 saatlik saatte 12 saat sonra akrep aynı sayıyı gösterir; bu yüzden ileri sayılacak saat sayısının 12 ile bölümünden kalan kadar ilerlenir. Örnek: 3’ten 14 saat sonra 14 = 12 + 2, kalan 2 → 5')],
 ad=[A('Tam devirleri at','500’ü 12’ye böl.','500 = 12 × 41 + 8 → kalan 8'),A('Konumu bul','Şekildeki saat 10’u gösteriyor; 8 saat ileri.','10 + 8 = 18'),A('12’ye indir','18, 12’den büyük olduğundan 12 çıkar.','18 − 12 = 6')],
 puf='Saat sorularında tam 12 saatlik devirler konumu değiştirmez; yalnız toplam saatin 12 ile bölümünden kalan kadar ilerle ve 12’yi aşarsan 12 çıkar.')

bitir(P,'bolmesek','mat|Bölme ve Bölünebilme')
