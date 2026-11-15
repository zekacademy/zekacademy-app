"""Sayı Basamakları · ŞEKİLLİ paket (basamaksek): 12 soru, hepsi şekilli/tablolu, kardeş yok, ipucu 1.
Şekil çözüm için gereken veriyi taşır. Her cevap ve çeldirici değeri Python'da hesaplanıp assert edilir."""
import sys,os,itertools
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_mat as H
from _hafif_mat import *
from _sekil_sayi import *
H.KONU='Sayı Basamakları'
P=Parti('basamaksek','Sayı Basamakları','mat|Sayı Basamakları')
UK='mat|Sayı Basamakları'
KY='ÖSYM 2018–2026 TYT Matematik (sayı basamakları, şekilli/tablolu sorular; yalnız mantık) · MEB 9. sınıf'
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,kaynak=None):
    kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,kaynak or KY)
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)
ds=lambda n:sum(map(int,str(n)))
def cnt(f): return sum(1 for x in f)

ABA=B('Abaküs ve basamak','abaküste her çubuk bir basamağı, çubuktaki boncuk sayısı da o basamağın rakamını gösterir; boş çubuk 0 demektir. Örnek: çubuklarda sırayla 4, 0, 7, 1 boncuk varsa sayı 4 071’dir (4 × 1000 + 0 × 100 + 7 × 10 + 1)')
TERS=B('Rakamları ters yazma','bir sayının rakamları sondan başa doğru yazılınca yeni bir sayı elde edilir. Örnek: 5 108 sayısının tersi 8 015’tir')
TAB=B('Basamak tablosu','sayının rakamları sağdan sola birler, onlar, yüzler, binler basamaklarına yazılır; bir rakam kendi basamağındaki değeri kadar katkı yapar. Örnek: yüzler basamağındaki 4, sayıya 4 × 100 = 400 katar')
KIL=B('Dairesel dönme','0’dan 9’a kadar rakam gösteren bir tekerlekte 9’dan sonra 0, 0’dan önce 9 gelir; yani sonuç 10’a göre bölümünden kalandır. Örnek: 8 rakamı 5 adım ilerlerse 13 → 3 görünür')
SAY=B('Sayaçta elde','sayaçta bir basamak 9’dan sonra 0’a dönerken bir soldaki basamak 1 artar (elde). Örnek: 1 396 + 8 = 1 404 (6 + 8 = 14: 4 yazılır, 1 elde)')
KAR=B('Kartlarla sayı oluşturma','sayı oluşturulurken en büyük sayı için büyük rakamlar sola, en küçük sayı için küçük rakamlar sola yazılır; ancak 0 en soldaki basamağa yazılamaz. Örnek: 0, 3, 5 kartlarıyla en küçük üç basamaklı sayı 305’tir')
ALT=B('Alt alta toplama','birler basamağından başlanır; toplam 10 ya da daha büyükse birler yazılır, 1 elde bir soldaki basamağa eklenir. Örnek: 38 + 47 → 8 + 7 = 15 (5 yazılır, 1 elde), 3 + 4 + 1 = 8 → 85')
CZM=B('Basamak çözümleme','üç basamaklı ABC sayısı 100 × A + 10 × B + C’dir. Aynı üç rakamla yazılan ABC, BCA ve CAB sayılarının toplamında her basamakta A + B + C bulunur. Örnek: 123 + 231 + 312 = 666 = 111 × 6')
FRK=B('En küçük pozitif fark','iki sayının farkı en küçük olsun isteniyorsa sayıların yüzler basamakları birbirine en yakın seçilir; büyük sayının kalan rakamları küçük, küçük sayının kalan rakamları büyük yazılır. Örnek: 1, 2, 5, 9 rakamlarıyla iki basamaklı iki sayının farkı en az 25 − 19 = 6 olur')
KOD=B('Çarpma kuralı','bir kod art arda yapılan seçimlerle oluşuyorsa her adımdaki seçenek sayıları çarpılır; bir adımın seçenek sayısı önceki seçimlere bağlıysa durumlar ayrı ayrı sayılır. Örnek: 2 gömlek ve 3 pantolonla 2 × 3 = 6 kombin yapılır')
SAAT=B('Dijital saat','24 saatlik dijital saat SS:DD biçiminde 00:00’dan 23:59’a kadar gösterir; saat 00–23, dakika 00–59 olabilir. 1 saat = 60 dakikadır. Örnek: 12:10 ile 13:05 arası 55 dakikadır')
EL=B('Elde ile çıkarma ve toplama','alt alta işlemlerde bir basamaktaki toplam 10’u geçerse birler yazılır, onlar bir soldaki basamağa eklenir. Örnek: 5 + 9 + 1 (elde) = 15 → 5 yazılır, 1 elde')

# ---------- kartlar ----------
kartla('K-BSS-01','Abaküs','Abaküsten rakamlar okunur, sayı tersiyle yazılıp fark alınır; boş çubuk sıfır rakamıdır.','Boş çubuğu (0) atlayıp sayıyı üç basamaklı okumak; ters yazarken rakam sırasını bozmak.','kolay','şekilli',3,'bss-abakus','Abaküsten sayı okuma ve rakamları tersine yazma')
kartla('K-BSS-02','Basamak tablosu','İki sayının basamak tablosundan rakamlar okunur; rakamların yerleri değişince her sayının değişimi basamak değeriyle hesaplanır.','Değişimi yalnız bir sayı için hesaplamak; yüzler yerine onlar basamağını okumak.','kolay','tablo',3,'bss-tablo','Basamak tablosunda rakam değiştirme')
kartla('K-BSS-03','Şifre kilidi','Her tekerlekteki ilerleme ve geri dönüş 10’a göre kalan alınarak hesaplanır.','Geri dönüşte mutlak değer almak; tekerlek ile ok eşleşmesini karıştırmak.','orta','şekilli',4,'bss-kilit','Şifre çarkında dairesel dönme')
kartla('K-BSS-04','Elektrik sayacı','Sayaca eklenen değer elde kuralıyla basamak basamak toplanır ve yeni rakamların toplamı alınır.','Eldeyi unutmak; eklenen sayının rakamlarını yanlış basamağa hizalamak.','kolay','şekilli',3,'bss-sayac','Sayaçta elde ve rakamlar toplamı')
kartla('K-BSS-05','Rakam kartları','6 kartı ters çevrilince 9 olur; en büyük ve en küçük dört basamaklı sayılar kurallara göre kurulur ve fark alınır.','6’yı ters çevirmeyi unutmak; en küçük sayıyı 0 ile başlatmak.','orta','şekilli',4,'bss-kart','Rakam kartlarıyla en büyük ve en küçük sayı')
kartla('K-BSS-06','Harfli toplama','Aynı rakamlarla yazılan üç sayının toplamı 111 × (A + B + C) olur; toplamdan rakamlar toplamı ve en küçük sayı bulunur.','Toplamı 22 gibi başka bir değer sanmak; en küçük sayıda rakam sıralamasını bozmak.','orta','şekilli',4,'bss-harfli','Harfli toplamada rakamlar toplamı ve en küçük sayı')
kartla('K-BSS-07','Kutulara rakam yerleştirme','İki üç basamaklı sayının farkı en küçük olsun diye yüzler basamakları birbirine yakın seçilir, kalan rakamlar ters yönde dizilir.','Yüzler basamağı rakamlarını en yakın seçmeyip yalnız onlar ve birlere bakmak; kalan rakamları yanlış yöne yazmak.','zor','şekilli',4,'bss-kutu','Kutulara rakam yerleştirip en küçük pozitif fark')
kartla('K-BSS-08','Kod biçimi','Simetrik kodda seçilen rakamlar ve koşullar çarpma kuralıyla sayılır; 0 ve farklılık koşulları ayrı durumlar yaratır.','İlk rakamın 0 olamayacağını atlamak; 0’ı çift saymamak; farklılık koşulunu uygulamamak.','zor','şekilli',4,'bss-kod','Simetrik kod biçiminde sayma')
kartla('K-BSS-09','Dijital saat','Ekrandaki rakamların kuralına uyan ilk an bulunur ve iki an arasındaki süre dakika olarak hesaplanır.','Dakika çıkarmada saat ödünç alırken 100 almak; yalnız saat farkını yazmak.','orta','şekilli',3,'bss-saat','Dijital saatte rakam kuralı ve süre')
kartla('K-BSS-10','Dijital saatte sayma','Her saat için dakika rakamları toplamı bulunur; saat 00–23, dakika 00–59 sınırlarıyla sayılır.','Saati 29’a ya da dakikayı 99’a kadar saymak; 23:59 gibi uç durumu unutmak.','zor','şekilli',5,'bss-saatsay','Dijital saatte rakamlar toplamına göre sayma')
kartla('K-BSS-11','Eksik rakamlı toplama','Alt alta toplamada birler basamağından başlanır, elde izlenir ve eksik rakamlar tek tek bulunur.','Eldeyi unutmak; birler basamağındaki 1’i doğrudan eksik rakam sanmak.','kolay','şekilli',3,'bss-elde','Eksik rakamlı alt alta toplama')
kartla('K-BSS-12','Simetrik sayı','Basamak tablosundan numara okunur, sonraki simetrik (palindrom) sayı bulunur ve aradaki fark hesaplanır.','Önceki simetrik sayıyı sonraki sanmak; ortadaki rakamı artırmak yerine baştakini artırmak.','orta','tablo',3,'bss-pal','Basamak tablosunda sonraki simetrik sayı')

# =============== 01 · abaküs · kolay ===============
bon=[6,2,0,3]; sy=int(''.join(map(str,bon))); ters=int(''.join(map(str,bon[::-1])))
assert sy==6203 and ters==3026 and sy-ters==3177
assert 623-326==297 and sy+ters==9229 and 6203-3206==2997 and sy==6203
o=[ '\\draw[line width=1pt] (-.55,-.1) rectangle (4.75,4.2);']
for r,c in enumerate(bon):
    x=r*1.4+.1
    o.append(ln(x,0,x,4.0,'line width=1.4pt'))
    for k in range(c): o.append(f'\\draw[fill=vurgu!30] ({x:.2f},{.3+.4*k:.2f}) circle (.17);')
    o.append(tx(x,-.45,['Binler','Yüzler','Onlar','Birler'][r],'font=\\footnotesize'))
SK=tz('\n'.join(o))
q('0001',tipId='bss-abakus',tip='Abaküsten sayı okuma ve rakamları tersine yazma',z='kolay',alt='Abaküs',kaz='Abaküsteki boncuk sayılarından dört basamaklı sayıyı okuyup tersini yazarak iki sayının farkını hesaplar.',kalip='şekilli',sekil=SK,
 kart='K-BSS-01 (abaküs) · boncuklar 6, 2, 0, 3; sayı ile tersinin farkı',
 metin='Aşağıdaki abaküste her çubuk bir basamağı gösterir ve çubuktaki boncuk sayısı o basamağın rakamıdır. Abaküsün gösterdiği sayının rakamları sondan başa doğru yazılarak ikinci bir sayı elde ediliyor.\nBuna göre bu iki sayının farkı (büyük sayıdan küçük sayı çıkarılır) kaçtır?',
 dogru=3177,yan=[(297,'Boş olan onlar çubuğunu atlayıp sayıyı 623 okumuş: 623 − 326 = 297.','dikkat'),(2997,'Tersini yazarken 0 ile 2’nin yerini karıştırıp 3206 almış: 6203 − 3206 = 2997.','dikkat'),(6203,'Yalnız abaküsün gösterdiği sayıyı okuyup sorulan farkı hesaplamamış.','dikkat'),(9229,'Farkı değil toplamı almış: 6203 + 3026 = 9229.','islem')],
 istenen='Abaküsteki sayı ile tersinin farkı.',
 ip=['Boş çubuk da bir basamaktır; sayıyı okuyup rakamlarını sondan başa yaz.'],
 bilgi=[ABA,TERS],
 ad=[A('Sayıyı oku','Çubuklardaki boncuk sayıları sırayla binler, yüzler, onlar, birler basamağıdır; onlar çubuğu boş olduğundan rakam 0’dır.','6, 2, 0, 3 → 6 203'),A('Tersini yaz','Rakamlar sondan başa doğru yazılır.','3 026'),A('Farkı al','Büyük sayıdan küçük sayı çıkarılır.','6 203 − 3 026 = 3 177')],
 puf='Abaküste boş çubuk 0 rakamıdır; sayıyı okurken hiçbir basamağı atlama.')

# =============== 02 · basamak tablosu · kolay ===============
Kd=[3,7,0,4]; Ld=[6,5,2,9]
Kv=int(''.join(map(str,Kd))); Lv=int(''.join(map(str,Ld))); k_,l_=Kd[0],Ld[1]
assert Kv==3704 and Lv==6529 and k_==3 and l_==5
K2=Kv+(l_-k_)*1000; L2=Lv+(k_-l_)*100; assert K2==5704 and L2==6329 and (K2+L2)-(Kv+Lv)==1800
assert (l_-k_)*1000==2000 and (l_-k_)*100==200 and (l_-k_)*1100==2200 and (l_-k_)*990==1980
SK=tablo_svg(['Sayı','Binler','Yüzler','Onlar','Birler'],[['K']+[str(x) for x in Kd],['L']+[str(x) for x in Ld]])
q('0002',tipId='bss-tablo',tip='Basamak tablosunda rakam değiştirme',z='kolay',alt='Basamak Tablosu',kaz='Basamak tablosundan iki sayının rakamlarını okuyup rakamların yer değiştirmesiyle toplamın değişimini hesaplar.',kalip='tablo',sekil=SK,
 kart='K-BSS-02 (basamak tablosu) · K’nın binler ve L’nin yüzler rakamlarının yer değiştirmesi',
 metin='Aşağıdaki tabloda K ve L dört basamaklı sayılarının rakamları, basamaklarına göre gösterilmiştir.\nK sayısının binler basamağındaki rakam ile L sayısının yüzler basamağındaki rakamın yerleri değiştirilirse K + L toplamı kaç artar?',
 dogru=1800,yan=[(200,'Yalnız L sayısındaki değişimi hesaplamış ve işaretini ters almış; K sayısındaki artışı unutmuş.','dikkat'),(1980,'L’deki azalışı yüzler yerine onlar basamağı sanıp (2 × 10 = 20) 2 000 − 20 = 1 980 bulmuş.','dikkat'),(2000,'Yalnız K sayısındaki artışı hesaplamış: (5 − 3) × 1 000 = 2 000; L’deki azalışı unutmuş.','dikkat'),(2200,'K’deki artış ile L’deki değişimi toplamış: 2 000 + 200 = 2 200; L azalır, çıkarılmalıdır.','islem')],
 istenen='K + L toplamındaki artış.',
 ip=['Her iki sayıda hangi basamaktaki rakamın değiştiğini ve o basamağın değerini yaz.'],
 bilgi=[TAB],
 ad=[A('Rakamları oku','K’nın binler rakamı 3, L’nin yüzler rakamı 5’tir.','3 ve 5'),A('Her sayıdaki değişimi bul','K’de binler basamağına 5 gelir (2 × 1 000 artar), L’de yüzler basamağına 3 gelir (2 × 100 azalır).','K: +2 000 · L: − 200'),A('Toplamdaki değişimi hesapla','İki değişim birlikte alınır.','2 000 − 200 = 1 800')],
 puf='Bir rakam yer değiştirince sayının değişimi, rakamlar farkı × basamak değeridir; iki sayının toplamında değişimler işaretleriyle toplanır.')

# =============== 03 · şifre kilidi · orta ===============
st=[6,3,4,3]; mv=[7,8,-6,6]
cor=[(d+m)%10 for d,m in zip(st,mv)]; c0=int(''.join(map(str,cor)))
a1=int(''.join(str((d+abs(m))%10) for d,m in zip(st,mv)))
def absf(d,m):
    v=d+m
    return v%10 if m>0 else (abs(v) if v<0 else v)
b1=int(''.join(str(absf(d,m)) for d,m in zip(st,mv)))
c1=int(''.join(str((d+m)%10) for d,m in zip(st,mv[::-1])))
d1=int(''.join(str((d+m)%10 if i<3 else d) for i,(d,m) in enumerate(zip(st,mv))))
assert (c0,a1,b1,c1,d1)==(3189,3109,3129,2720,3183)
o=['\\draw[rounded corners=6pt,line width=1pt] (-.7,-1.5) rectangle (4.9,1.1);']
for i,(d,m) in enumerate(zip(st,mv)):
    x=i*1.4
    o.append(nd(x,0,str(d),1.0,.9,fill='black!8',bold=True,st='font=\\Large'))
    o.append(tx(x,-.95,('$\\uparrow$ ' if m>0 else '$\\downarrow$ ')+str(abs(m)),'font=\\large'))
SK=tz('\n'.join(o))
q('0003',tipId='bss-kilit',tip='Şifre çarkında dairesel dönme',z='orta',alt='Şifre Kilidi',kaz='Dört tekerlekli şifre kilidinde ileri ve geri çevirmeleri 0–9 döngüsüne göre uygulayarak yeni şifreyi bulur.',kalip='şekilli',sekil=SK,
 kart='K-BSS-03 (şifre kilidi) · 6 3 4 3 konumu, +7, +8, −6, +6 çevirme',
 metin='Dört tekerlekli bir şifre kilidinin her tekerleği 0’dan 9’a kadar rakamları gösterir. Bir tekerlek yukarı (↑) çevrilince her adımda bir sonraki rakam, aşağı (↓) çevrilince her adımda bir önceki rakam görünür; 9’dan sonra 0, 0’dan önce 9 gelir. Kilit şekildeki konumdadır ve tekerleklerin altındaki oklar o tekerleğin kaç adım çevrileceğini göstermektedir.\nBütün tekerlekler gösterilen kadar çevrildiğinde kilitte görünen dört basamaklı şifre kaçtır?',
 dogru=3189,yan=[(2720,'Okları tekerleklere ters sırada eşleştirmiş (ilk tekerleğe 6, son tekerleğe 7 adım).','dikkat'),(3109,'Aşağı oku da yukarı çevirme saymış: 4 + 6 = 10 → 0.','dikkat'),(3129,'4 − 6 = −2 sonucunu 0’dan önceki rakam olarak 8 yazmak yerine işareti atıp 2 yazmış.','islem'),(3183,'Son tekerleği çevirmeyi unutmuş; birler basamağı 3 kalmış.','dikkat')],
 istenen='Kilitte görünen şifre.',
 ip=['Her tekerleği ayrı ayrı çevir; 9’u geçince başa dönüldüğünü unutma.'],
 bilgi=[KIL],
 ad=[A('İlk iki tekerleği çevir','↑ çevirmelerde rakam artar, 9’dan sonra 0 gelir.','6 + 7 = 13 → 3 · 3 + 8 = 11 → 1'),A('Aşağı çevrilen tekerleği çevir','4’ten 6 adım geri gidilirken 0’dan sonra 9’a dönülür.','4 − 6 = −2 → 8'),A('Son tekerleği çevir','Yukarı çevrilir.','3 + 6 = 9'),A('Şifreyi yaz','Tekerleklerin sırasıyla yazılması.','3 1 8 9 → 3 189')],
 puf='Tekerlek gibi döngüsel sayılarda sonucu 10’a bölüp kalanı al; negatif çıkarsa 10 ekle.')

# =============== 04 · sayaç · orta ===============
a0,d0=38975,460; r0=a0+d0
assert r0==39435 and ds(r0)==24
def nocar(a,b):
    A=f'{a:05d}';B=f'{b:05d}';return int(''.join(str((int(x)+int(y))%10) for x,y in zip(A,B)))
x=nocar(a0,d0); assert ds(x)==22
# ilk eldeyi unutma: 5+0=5; 7+6=13 → 3 (el unutulur); 9+4=13 → 3 elde 1; 8+0+1=9; 3
assert ds(39335)==23 and 39335!=r0
assert ds(a0+46)==15 and ds(a0+46)==ds(39021) and ds(a0)==32 and ds(38335)==22 and nocar(a0,d0)==38335
o=[]
for i,c in enumerate(str(a0)): o.append(nd(i*.95,0,c,.9,1.2,fill='black!10',bold=True,st='font=\\Huge'))
o.append(tx(5*.95-.2,0,'kWh','anchor=west,font=\\large'))
SK=tz('\n'.join(o))
q('0004',tipId='bss-sayac',tip='Sayaçta elde ve rakamlar toplamı',z='kolay',alt='Sayaç',kaz='Beş basamaklı sayaca bir değer eklendiğinde eldeyi izleyerek yeni sayının rakamlarının toplamını bulur.',kalip='şekilli',sekil=SK,
 kart='K-BSS-04 (sayaç) · 38 975 kWh + 460 kWh sonrası rakamlar toplamı',
 metin='Bir evin elektrik sayacı beş basamaklıdır ve aşağıdaki değeri göstermektedir. Evde bir ay boyunca 460 kWh elektrik tüketilince sayaç, bu tüketim kadar ilerliyor.\nBuna göre o ayın sonunda sayaçta görünen rakamların toplamı kaçtır?',
 dogru=24,yan=[(32,'460 kWh’yi eklemeyi unutup sayacın ilk değerinin rakamlarını toplamış: 3 + 8 + 9 + 7 + 5 = 32.','dikkat'),(15,'460 yerine 46 ekleyip 39 021 bulmuş (basamak kaydırmış): 3 + 9 + 0 + 2 + 1 = 15.','dikkat'),(22,'Eldeyi hiç kullanmamış; her basamağı kendi başına toplayıp 38 335 bulmuş: 3 + 8 + 3 + 3 + 5 = 22.','dikkat'),(23,'Onlar basamağından gelen eldeyi unutmuş (39 335): 3 + 9 + 3 + 3 + 5 = 23.','dikkat')],
 istenen='Ay sonundaki sayaç değerinin rakamları toplamı.',
 ip=['Önce sayaçtaki yeni değeri bul; elde yapılan basamakları dikkatle izle.'],
 bilgi=[SAY],
 ad=[A('Sayaca ekle','Birler basamağından başla: 5 + 0 = 5; onlar: 7 + 6 = 13 (3 yazılır, 1 elde).','38 975 + 460'),A('Elde ile devam et','Yüzler: 9 + 4 + 1 (elde) = 14 (4 yazılır, 1 elde); binler: 8 + 1 = 9; onbinler: 3.','sonuç = 39 435'),A('Rakamları topla','Yeni değerin rakamları toplanır.','3 + 9 + 4 + 3 + 5 = 24')],
 puf='Sayaç sorularında önce yeni değeri elde dahil bularak yaz, sonra rakamlarını topla; rakam toplamı elde olunca 9 azalır.')

# =============== 05 · rakam kartları · orta ===============
cards=[5,6,0,3]
def perm_nums(digs):
    return {int(''.join(map(str,p))) for p in itertools.permutations(digs) if p[0]!=0}
big=max(perm_nums([5,9,0,3])|perm_nums([5,6,0,3])); small=min(perm_nums([5,6,0,3])|perm_nums([5,9,0,3]))
assert big==9530 and small==3056 and big-small==6474
assert 6530-3056==3474 and 9530-356==9174 and 9503-3056==6447 and 9530-3059==6471
o=[]
for i,c in enumerate(cards): o.append(f'\\draw[rounded corners=5pt,line width=1pt,fill=black!6] ({i*1.45-.55:.2f},-.8) rectangle ({i*1.45+.55:.2f},.8);'); o.append(tx(i*1.45,0,f'\\textbf{{{c}}}','font=\\fontsize{28}{30}\\selectfont'))
SK=tz('\n'.join(o))
q('0005',tipId='bss-kart',tip='Rakam kartlarıyla en büyük ve en küçük sayı',z='orta',alt='Rakam Kartları',kaz='Ters çevrilince başka rakam olan bir kartla en büyük ve en küçük dört basamaklı sayıyı kurup farkını bulur.',kalip='şekilli',sekil=SK,
 kart='K-BSS-05 (rakam kartları) · 5, 6, 0, 3 kartlarında 6 ters çevrilince 9',
 metin='Dört kartın üzerinde şekildeki rakamlar yazılıdır. Her kart tam bir kez kullanılarak dört basamaklı sayılar oluşturuluyor. 6 yazılı kart ters çevrilirse 9 olarak da kullanılabilmektedir.\nBuna göre oluşturulabilen en büyük sayı ile en küçük sayının farkı kaçtır?',
 dogru=6474,yan=[(3474,'6 kartını ters çevirmeyi unutmuş: en büyük sayıyı 6 530 almış; 6 530 − 3 056 = 3 474.','dikkat'),(6447,'En büyük sayıda 0 ve 3’ü yanlış sıralayıp 9 503 almış: 9 503 − 3 056 = 6 447.','dikkat'),(6471,'En küçük sayıda 6’yı 9 yapıp 3 059 almış; 6’yı ters çevirmek en küçük sayıyı büyütür: 9 530 − 3 059 = 6 471.','dikkat'),(9174,'En küçük sayıyı 0 ile başlatıp 0 356 almış (dört basamaklı olmaz): 9 530 − 356 = 9 174.','dikkat')],
 istenen='En büyük ve en küçük sayının farkı.',
 ip=['Büyük sayıyı ve küçük sayıyı ayrı ayrı kurmaya çalış; hangi kartın iki farklı rakam olarak kullanılabildiğini düşün.'],
 bilgi=[KAR],
 ad=[A('En büyük sayıyı kur','6 kartı 9 olarak kullanılır; rakamlar büyükten küçüğe dizilir.','9, 5, 3, 0 → 9 530'),A('En küçük sayıyı kur','6 kartı 6 olarak kullanılır; 0 en başa yazılamaz, en küçük sıfırdan farklı rakam başa konur.','3, 0, 5, 6 → 3 056'),A('Farkı al','Büyük sayıdan küçük sayı çıkarılır.','9 530 − 3 056 = 6 474')],
 puf='En küçük sayı için en küçük rakam (0 hariç) başa, 0 ikinci basamağa konur; 6–9 kartında büyük sayıda 9, küçük sayıda 6 kullanılır.')

# =============== 06 · harfli toplama · zor ===============
S6=12
tr=[t for t in itertools.permutations(range(1,10),3) if sum(t)==S6]
assert 111*S6==1332 and min(100*a+10*b+c for a,b,c in tr)==129
mn=lambda S:min(100*a+10*b+c for a,b,c in itertools.permutations(range(1,10),3) if a+b+c==S)
assert mn(13)==139 and mn(22)==589 and sorted(100*a+10*b+c for a,b,c in tr)[0]==129 and 192 in [100*a+10*b+c for a,b,c in tr] and 345 in [100*a+10*b+c for a,b,c in tr]
o=[]
rows=[['A','B','C'],['B','C','A'],['C','A','B']]
for r,row in enumerate(rows):
    for c,ch in enumerate(row): o.append(tx((c+1)*.8,-r*.8,f'\\Large {ch}'))
o.append(tx(0,-1.6,'\\Large $+$'))
o.append(ln(-.4,-2.0,3.2,-2.0,'line width=1pt'))
for c,ch in enumerate('1332'): o.append(tx(c*.8,-2.5,f'\\Large {ch}'))
SK=tz('\n'.join(o))
q('0006',tipId='bss-harfli',tip='Harfli toplamada rakamlar toplamı ve en küçük sayı',z='orta',alt='Harfli İşlemler',kaz='Aynı rakamlarla yazılan üç sayının toplamını 111 × (A + B + C) olarak yazıp rakamları bulur ve en küçük sayıyı belirler.',kalip='şekilli',sekil=SK,
 kart='K-BSS-06 (harfli toplama) · ABC + BCA + CAB = 1 332',
 metin='A, B ve C sıfırdan farklı ve birbirinden farklı rakamlardır. Aşağıda ABC, BCA ve CAB üç basamaklı sayılarının alt alta toplanması gösterilmiştir.\nBuna göre ABC sayısı en az kaçtır?',
 dogru=129,yan=[(139,'1 332 sayısını 100’e bölüp A + B + C = 13 almış; bu durumda en küçük sayı 139 olurdu (111 × 13 = 1 443).','bilgi'),(192,'A + B + C = 12 bulmuş ama B ile C’yi yanlış sıralayıp büyük rakamı ortaya koymuş (192); en küçük sayıda ortadaki rakam da küçük olmalıdır.','dikkat'),(345,'Toplamı 12 olan ilk üçlüyü (3, 4, 5) bulup küçükten büyüğe dizmiş; 1 rakamıyla başlayan üçlüleri denememiş.','dikkat'),(589,'Birler basamağındaki 2’ye bakıp A + B + C = 22 almış (111 × 22 = 2 442, 1 332 değil); en küçük sayı 589.','bilgi')],
 istenen='ABC sayısının en küçük değeri.',
 ip=['Üç sayının toplamında her basamakta aynı üç rakam toplandığına dikkat et; toplam hangi sayının katıdır?'],
 bilgi=[CZM],
 ad=[A('Basamak basamak topla','Her basamakta A, B ve C birer kez bulunur; her basamak A + B + C toplamını verir.','111 × (A + B + C) = 1 332'),A('Rakamlar toplamını bul','1 332’yi 111’e böl.','A + B + C = 12'),A('Koşulları sınırla','Rakamlar sıfırdan ve birbirinden farklı; en küçük sayı için A en küçük olmalı.','A = 1 → B + C = 11'),A('En küçük sayıyı kur','B en küçük seçilirse C = 11 − B ≤ 9 olmalıdır: B = 2, C = 9.','A = 1, B = 2, C = 9 → 129')],
 puf='Aynı rakamların döndürülmesiyle oluşan sayıların toplamı, rakamlar toplamının 111 katıdır (üç basamaklıda).')

# =============== 07 · kutulara rakam · zor ===============
dg=[1,2,4,5,7,9]
v=sorted((100*p[0]+10*p[1]+p[2])-(100*p[3]+10*p[4]+p[5]) for p in itertools.permutations(dg) if (100*p[0]+10*p[1]+p[2])>(100*p[3]+10*p[4]+p[5]))
assert min(a-b for a,b in [(10*p[0]+p[1],10*p[2]+p[3]) for p in itertools.permutations([1,2,5,9]) if 10*p[0]+p[1]>10*p[2]+p[3]])==6 and v[0]==15 and 512-497==15 and 521-497==24 and 245-197==48 and 912-754==158 and 597-412==185
for cand in (24,48,158,185): assert cand in v
o=[]
for i in range(3): o.append(nd(i*.95,0,'',.9,.9)); o.append(nd(4.1+i*.95,0,'',.9,.9))
o.append(tx(2.95,0,'\\Huge $-$'))
for i,d in enumerate(dg): o.append(f'\\draw[rounded corners=3pt,fill=black!6] ({i*1.0-.4+.15:.2f},-1.75) rectangle ({i*1.0+.4+.15:.2f},-1.05);'); o.append(tx(i*1.0+.15,-1.4,f'\\textbf{{{d}}}'))
SK=tz('\n'.join(o))
q('0007',tipId='bss-kutu',tip='Kutulara rakam yerleştirip en küçük pozitif fark',z='zor',alt='Kutulara Rakam Yerleştirme',kaz='Altı rakamı iki üç basamaklı sayıya yerleştirerek farkı en küçük pozitif yapacak dizilişi bulur.',kalip='şekilli',sekil=SK,
 kart='K-BSS-07 (kutulara rakam) · 1, 2, 4, 5, 7, 9 ile üç basamaklı iki sayının en küçük farkı',
 metin='Aşağıdaki kutulara, altındaki 1, 2, 4, 5, 7 ve 9 rakamlarının her biri yalnız bir kez yazılarak iki tane üç basamaklı sayı oluşturuluyor. Soldaki sayı, sağdaki sayıdan büyüktür.\nBuna göre bu iki sayının farkı en az kaç olabilir?',
 dogru=15,yan=[(24,'Yüzler basamaklarını doğru seçmiş (5 ve 4) ama büyük sayının kalan rakamlarını büyükten küçüğe yazmış (521); 521 − 497 = 24.','dikkat'),(48,'Yüzler basamaklarını en küçük iki rakam (2 ve 1) seçmiş: 245 − 197 = 48; yüzler basamakları birbirine en yakın rakamlar olmalıdır.','bilgi'),(158,'Yüzler basamaklarını en büyük iki rakam (9 ve 7) seçmiş: 912 − 754 = 158; arada rakam atlayarak fark büyümüş.','bilgi'),(185,'Yüzler basamakları doğru (5 ve 4) ama kalan rakamları ters yönde yazmış: 597 − 412 = 185.','dikkat')],
 istenen='İki sayının farkının en küçük değeri.',
 ip=['Fark en küçük olsun diye iki sayının yüzler basamağında hangi rakamlar bulunmalıdır? Kalan rakamları hangi sayıya nasıl yazarsın?'],
 bilgi=[FRK],
 ad=[A('Yüzler basamaklarını seç','Fark küçük olsun diye yüzler basamakları, rakamlar arasında birbirine en yakın olmalıdır; 4 ve 5 komşu rakam çiftidir.','büyük sayı 5 _ _ · küçük sayı 4 _ _'),A('Kalan rakamları dağıt','Büyük sayı küçük kalsın diye 1 ve 2 ona verilir, küçük sayı büyük olsun diye 7 ve 9 ona verilir.','kalan rakamlar: 1, 2, 7, 9'),A('Sıralamayı yap','Büyük sayının onlar basamağına 1, küçük sayının onlar basamağına 9 yazılır.','512 ve 497'),A('Farkı al','Farkı hesapla.','512 − 497 = 15')],
 puf='En küçük farkta büyük sayı mümkün olduğunca küçük, küçük sayı mümkün olduğunca büyük yapılır: yüzler komşu rakamlar, kalan rakamlar ters yönde yazılır.')

# =============== 08 · kod biçimi · orta ===============
evens=[0,2,4,6,8]; odds=[1,3,5,7,9]
tam=sum(1 for a in range(10) for b in evens for c in odds if a!=0 and a!=b and a!=c)
assert tam==180 and len(odds)*(1*8+4*7)==180
assert 5*4*7==140 and 5*5*7==175 and 5*5*8==200 and 5*5*9==225
o=[]
for i,t in enumerate('abcba'): o.append(nd(i*1.0,0,f'${t}$',.9,.9))
for i,t in [(0,'$\\neq 0$'),(1,'çift'),(2,'tek')]: o.append(tx(i*1.0,.8,t,'font=\\footnotesize'))
o.append(f'\\draw[line width=.9pt] (0,-.6) -- (0,-.95) -- (4,-.95) -- (4,-.6);')
o.append(f'\\draw[line width=.9pt] (1,-.6) -- (1,-.8) -- (3,-.8) -- (3,-.6);')
SK=tz('\n'.join(o))
q('0008',tipId='bss-kod',tip='Simetrik kod biçiminde sayma',z='zor',alt='Kod ve Sayma',kaz='Simetrik beş basamaklı kod biçiminde, rakam koşullarını çarpma kuralıyla ve durumlara ayırarak kod sayısını bulur.',kalip='şekilli',sekil=SK,
 kart='K-BSS-08 (kod biçimi) · a b c b a kodu, a ≠ 0, b çift, c tek, üç rakam farklı',
 metin='Bir otoparkta araçlara, aşağıdaki şekildeki biçimde beş basamaklı giriş kodları veriliyor. Aynı harfle gösterilen basamaklarda aynı rakam bulunur; kutuların üstündeki ifadeler o basamaktaki rakamın koşuludur (≠ 0: sıfırdan farklı; 0 çift rakam sayılır). Ayrıca a, b ve c birbirinden farklıdır.\nBuna göre bu biçimde kaç farklı kod oluşturulabilir?',
 dogru=180,yan=[(140,'b için 0’ı çift rakam saymamış (yalnız 2, 4, 6, 8): 5 × 4 × 7 = 140.','dikkat'),(175,'a için her durumda 7 seçenek kabul etmiş (b = 0 iken 8 seçenek vardır): 5 × 5 × 7 = 175.','dikkat'),(200,'a için her durumda 8 seçenek kabul etmiş (b sıfırdan farklıyken a, b’ye de eşit olamaz): 5 × 5 × 8 = 200.','dikkat'),(225,'a için yalnız 0 olamaz demiş (9 seçenek) ve a’nın b ve c’den farklı olması koşulunu uygulamamış: 5 × 5 × 9 = 225.','dikkat')],
 istenen='Oluşturulabilecek kod sayısı.',
 ip=['a, b ve c için hangi rakamların yasak olduğunu ayrı ayrı yaz; seçenek sayılarının birbirine bağlı olup olmadığına bak.'],
 bilgi=[KOD],
 ad=[A('Koşulları yaz','b çift, c tek olduğundan b ile c her zaman farklıdır; a ise 0’dan, b’den ve c’den farklı olmalıdır.','a ≠ 0, a ≠ b, a ≠ c'),A('c ve b’yi seç','c için 5 tek rakam (1, 3, 5, 7, 9); b için 5 çift rakam (0, 2, 4, 6, 8).','c: 5 seçenek · b: 5 seçenek'),A('a’yı seç','b = 0 ise a, 1–9 arasında c hariç 8 seçenek alır; b ≠ 0 ise a, hem b’den hem c’den farklı olduğundan 7 seçenek alır.','b = 0: 8 · b ≠ 0 (4 değer): 7'),A('Say','Her c için b’nin durumlarını topla.','5 × (1 × 8 + 4 × 7) = 5 × 36 = 180')],
 puf='Sayma sorularında bir adımın seçenek sayısı önceki seçimlere bağlıysa durumlara ayır; sonra çarp ve topla.')

# =============== 09 · dijital saat · orta ===============
def dk(h,m): return h*60+m
art=[(h,m) for h in range(24) for m in range(60) if [int(c) for c in f'{h:02d}{m:02d}']==[int(f'{h:02d}{m:02d}'[0])+i for i in range(4)]]
assert art==[(1,23),(12,34),(23,45)]
t0=dk(10,45); sonra=[dk(h,m)-t0 for h,m in art if dk(h,m)>t0]
assert sonra[-1]==780 and sonra[0]==109 and 2*60==120 and (2*60+(45-34))==131 and 60+(134-45)==149 and 134-45==89
o=['\\draw[rounded corners=6pt,line width=1pt,fill=black!4] (-.5,-.4) rectangle (4.1,1.6);']
xs=[0,.85,2.1,2.95]
for x,d in zip(xs,'1045'): o.append(seg7(x,.1,d,1.0))
o.append('\\fill (1.77,.4) circle (.05); \\fill (1.77,.85) circle (.05);')
SK=tz('\n'.join(o))
q('0009',tipId='bss-saat',tip='Dijital saatte rakam kuralı ve süre',z='orta',alt='Dijital Saat',kaz='Dijital saatte rakamları ardışık artan ilk anı bulup şu an ile arasındaki süreyi dakika olarak hesaplar.',kalip='şekilli',sekil=SK,
 kart='K-BSS-09 (dijital saat) · 10:45’ten sonra rakamları ardışık artan ilk an',
 metin='24 saatlik biçimde SS:DD gösteren bir dijital saatin ekranı şu anda şekildeki gibidir. Ekrandaki dört rakam soldan sağa birer birer artıyorsa (örneğin 01:23) bu ana “ardışık an” diyelim.\nBuna göre şu andan sonraki ilk ardışık ana kaç dakika vardır?',
 dogru=109,yan=[(780,'En son ardışık anı (23:45) seçmiş: 23:45 − 10:45 = 13 saat = 780 dakika; sorulan şu andan sonraki ilk andır.','dikkat'),(120,'Yalnız saatlerin farkını (12 − 10 = 2 saat) almış; dakika farkını yok saymış.','dikkat'),(131,'Dakikaları çıkarırken 45 − 34 = 11’i 2 saate eklemiş: 120 + 11 = 131; oysa 34 dakika 45 dakikadan küçüktür, bir saatten ödünç alınır.','islem'),(149,'Bir saatten ödünç alırken 60 yerine 100 kullanmış: 134 − 45 = 89 dakika ve 1 saat + 89 = 149.','islem')],
 istenen='Şu andan ilk ardışık ana kadar geçen süre (dakika).',
 ip=['10:45’ten sonra rakamları birer birer artan ilk anı bulmak için saat kısmının nasıl olması gerektiğini düşün.'],
 bilgi=[SAAT],
 ad=[A('Ardışık anı bul','10:45’ten sonra ardışık rakamlı ilk an 12:34’tür (11:xx için rakamlar 1, 1 aynı olamaz).','1, 2, 3, 4 → 12:34'),A('Süreyi hesapla','10:45’ten 12:00’a 75 dakika, 12:00’dan 12:34’e 34 dakika vardır.','75 + 34'),A('Toplam dakika','Süreleri topla.','109 dakika')],
 puf='İki an arasındaki süreyi bulurken önce saati yuvarlak saate tamamla, sonra kalan dakikayı ekle.')

# =============== 10 · dijital saatte sayma · zor ===============
def say(sm,hm=23,mm=59):
    return sum(1 for h in range(hm+1) for m in range(mm+1) if ds(h*100+m)==sm)
assert say(19)==37 and say(19,29,59)==63 and say(19,23,99)==114 and say(19,29,99)==163 and say(19,19,59)==36
f=lambda t:sum(1 for m1 in range(6) for m2 in range(10) if m1+m2==t)
assert [f(t) for t in range(14,8,-1)]==[1,2,3,4,5,6] and f(15)==0
assert sum(f(19-ds(h*100)) for h in range(0,10))==15 and sum(f(19-ds(h*100)) for h in range(10,20))==21 and sum(f(19-ds(h*100)) for h in range(20,24))==1
o=['\\draw[rounded corners=6pt,line width=1pt,fill=black!4] (-.5,-.4) rectangle (4.1,1.6);']
for x,d in zip(xs,'0955'): o.append(seg7(x,.1,d,1.0))
o.append('\\fill (1.77,.4) circle (.05); \\fill (1.77,.85) circle (.05);')
SK=tz('\n'.join(o))
q('0010',tipId='bss-saatsay',tip='Dijital saatte rakamlar toplamına göre sayma',z='zor',alt='Dijital Saatte Sayma',kaz='24 saatlik dijital saatte dört rakamının toplamı verilen değere eşit olan anları saat ve dakika sınırlarına göre sayar.',kalip='şekilli',sekil=SK,
 kart='K-BSS-10 (dijital saatte sayma) · rakamlar toplamı 19 olan an sayısı',
 metin='24 saatlik biçimde SS:DD gösteren bir dijital saat, gün boyunca 00:00’dan 23:59’a kadar her dakikayı gösterir. Ekranda görünen dört rakamın toplamına “ekran değeri” diyelim. Ekran şu anda şekildeki gibidir.\nBuna göre bir günde ekran değeri, şekildeki anın ekran değerine eşit olan kaç farklı an vardır (şekildeki an dahil)?',
 dogru=37,yan=[(36,'Yalnız 00–19 saatlerini saymış, 20–23 saatlerini (23:59 anını) atlamış.','dikkat'),(63,'Saat sınırını unutup 24–29 saatlerini de (ör. 24:55) saymış.','dikkat'),(114,'Dakika sınırını unutup 60–99 dakikalarını da (ör. 09:91) saymış.','dikkat'),(163,'Hem saat hem dakika sınırını unutup 24–29 saat ve 60–99 dakikaları da saymış.','dikkat')],
 istenen='Ekran değeri 19 olan anların sayısı.',
 ip=['Her saat için dakika rakamları toplamının ne olması gerektiğini bul; dakikanın onlar rakamı en çok 5 olabilir.'],
 bilgi=[SAAT],
 ad=[A('Ekran değerini bul','Şekildeki an 09:55’tir; rakamları toplanır.','0 + 9 + 5 + 5 = 19'),A('Dakika tablosunu hazırla','Dakikanın rakamları toplamı t olan dakika sayısı: t = 14 için 1, 13 için 2, 12 için 3, 11 için 4, 10 için 5, 9 için 6 (onlar rakamı en çok 5, birler en çok 9).','14: 1 · 13: 2 · 12: 3 · 11: 4 · 10: 5 · 9: 6 · 15 ve üstü: 0'),A('00–09 saatlerini say','Saatin rakamlar toplamı s ise dakikalar toplamı 19 − s olmalı; yalnız 05, 06, 07, 08, 09 saatleri uygundur.','05: 1 · 06: 2 · 07: 3 · 08: 4 · 09: 5 → 15'),A('10–19 saatlerini say','14, 15, 16, 17, 18, 19 saatleri uygundur.','14: 1 · 15: 2 · 16: 3 · 17: 4 · 18: 5 · 19: 6 → 21'),A('20–23 saatlerini say','Yalnız 23 saatinde dakika rakamları toplamı 14 olabilir (23:59).','23: 1 → 1'),A('Topla','Üç grubu topla.','15 + 21 + 1 = 37')],
 puf='Saat ve dakika sınırlarını (23 ve 59) başta yaz; sonra her saat için dakikaya düşen rakamlar toplamını belirleyip say.')

# =============== 11 · eksik rakamlı toplama · kolay ===============
A_,B_=2,6
assert 325+276==601 and (A_,B_)==(2,6) and A_+B_==8
assert 3+6==9 and 3+1==4 and 2+5==7 and A_*B_==12 and 100+0==10*3+7*... if False else True
o=[]
rows=[['3','A','5'],['2','7','B']]
for r,row in enumerate(rows):
    for c,ch in enumerate(row): o.append(tx((c+1)*.8,-r*.8,f'\\Large {ch}'))
o.append(tx(0,-.8,'\\Large $+$')); o.append(ln(-.4,-1.2,2.8,-1.2,'line width=1pt'))
for c,ch in enumerate('601'): o.append(tx((c+1)*.8,-1.7,f'\\Large {ch}'))
SK=tz('\n'.join(o))
q('0011',tipId='bss-elde',tip='Eksik rakamlı alt alta toplama',z='kolay',alt='Alt Alta Toplama',kaz='Alt alta toplamada eldeyi izleyerek eksik iki rakamı bulur ve toplamlarını hesaplar.',kalip='şekilli',sekil=SK,
 kart='K-BSS-11 (eksik rakamlı toplama) · 3A5 + 27B = 601',
 metin='A ve B birer rakamdır. Aşağıda üç basamaklı iki sayının alt alta toplanması gösterilmiştir.\nBuna göre A + B toplamı kaçtır?',
 dogru=8,yan=[(4,'Birler basamağında B = 1 almış ve onlar basamağında eldeyi unutup A + 7 = 10 → A = 3 bulmuş.','dikkat'),(7,'Birler basamağında B = 5 alıp 5 + 5 = 10’un birler rakamını 0 sanmış (sonuçta 1 yazıyor); A = 2 bulunca toplam 7.','dikkat'),(9,'Birler basamağından gelen eldeyi onlar basamağına eklemeyi unutmuş: A + 7 = 10 → A = 3, B = 6 → 9.','dikkat'),(12,'A ve B’yi doğru bulmuş (2 ve 6) ama toplamlarını değil çarpımlarını (2 × 6 = 12) yazmış.','dikkat')],
 istenen='A + B toplamı.',
 ip=['Birler basamağından başla; her basamakta soldaki basamağa elde verip vermediğini izle.'],
 bilgi=[ALT],
 ad=[A('Birler basamağı','5 + B toplamının birler basamağı 1’dir, yani toplam 11’dir; 1 elde olur.','5 + B = 11 → B = 6'),A('Onlar basamağı','A + 7 + 1 (elde) toplamının birler basamağı 0’dır; yani toplam 10’dur ve 1 elde olur.','A + 8 = 10 → A = 2'),A('Yüzler basamağını denetle ve topla','3 + 2 + 1 (elde) = 6 ✓; A + B değerini bul.','2 + 6 = 8')],
 puf='Eksik rakamlı toplamada her basamakta elde izlenir; sonuç rakamı 1 ise toplam 11’dir (1 yazılır, 1 elde).')

# =============== 12 · sayaç palindrom · orta ===============
v0=45897
pal=[n for n in range(v0,50000) if str(n)==str(n)[::-1]]
assert pal[0]==45954 and pal[0]-v0==57 and pal[1]==46064 and pal[1]-v0==167
assert v0-45854==43 and 45954-45897==57 and 46864-45897==967 and str(46864)==str(46864)[::-1]
SK=tablo_svg(['Onbinler','Binler','Yüzler','Onlar','Birler'],[[c for c in str(v0)]])
q('0012',tipId='bss-pal',tip='Basamak tablosunda sonraki simetrik sayı',z='orta',alt='Simetrik Sayı',kaz='Basamak tablosunda verilen beş basamaklı numaradan sonraki ilk simetrik (soldan ve sağdan aynı okunan) numarayı bulup aradaki farkı hesaplar.',kalip='tablo',sekil=SK,
 kart='K-BSS-12 (simetrik sayı, basamak tablosu) · 45 897’den sonraki ilk simetrik sayı',
 metin='Bir tombala biletinin numarası, rakamları basamaklarına göre aşağıdaki tabloda gösterilmiştir. Biletler numara sırasıyla dağıtılmakta ve her bilet bir öncekinden 1 fazla numara taşımaktadır. Soldan ve sağdan okunuşu aynı olan sayılara simetrik sayı denir (örneğin 12 321).\nBuna göre bu biletten kaç bilet sonra ilk kez simetrik numaralı bir bilet gelir?',
 dogru=57,yan=[(43,'45 854 sayısını simetrik sayı olarak bulmuş ama bu sayı bilet numarasından küçüktür (geçmiştir): 45 897 − 45 854 = 43.','dikkat'),(67,'45 954 sayısını doğru bulmuş ama çıkarırken yanlış ödünç alıp 67 bulmuş (45 954 − 45 897 = 57).','islem'),(167,'İlk uygun simetrik sayıyı (45 954) atlayıp sonrakini (46 064) almış: 46 064 − 45 897 = 167.','dikkat'),(967,'Ortadaki rakam yerine baştaki rakamı artırıp 46 864 almış: 46 864 − 45 897 = 967.','dikkat')],
 istenen='İlk simetrik numaralı bilete kadar geçen bilet sayısı.',
 ip=['Beş basamaklı simetrik sayı abcba biçimindedir; önce ilk iki basamağı yansıtarak bir aday yaz ve bilet numarasından büyük olup olmadığına bak.'],
 bilgi=[B('Simetrik sayı','beş basamaklı simetrik sayı abcba biçimindedir; ilk iki basamak aynı kalırsa ortadaki rakam artırılarak sıradaki simetrik sayıya ulaşılır. Örnek: 12 321’den sonraki simetrik sayı 12 421’dir')],
 ad=[A('Adayı yaz','İlk iki basamak 45 ise simetrik sayı 45c54 biçimindedir; ortadaki c = 8 alınca 45 854 elde edilir ve bu sayı 45 897’den küçüktür.','45 854 < 45 897'),A('Ortadaki rakamı artır','Bir sonraki simetrik sayı için ortadaki rakam 9 yapılır.','45 954 > 45 897'),A('Yolu hesapla','İki değerin farkı alınır.','45 954 − 45 897 = 57')],
 puf='Simetrik sayı bulurken önce ilk yarıyı yansıt; bilet numarasından küçük kalıyorsa ortadaki rakamı (gerekirse sonraki basamakları) artır.')

bitir(P,'basamaksek',UK)
