"""Parti 5: her tipten bir soru daha (0043–0055) ve kardeşleri; çeldiricilere hata türü (celTur: bilgi | islem | dikkat). Her cevap kodla doğrulanır."""
import json,sys,os
from itertools import product,permutations
from fractions import Fraction as Fr
from math import factorial as F
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,os.path.join(H,'..'))
import gorsel as G
B=lambda a,i:dict(ad=a,ifade=i)
A=lambda b,a,i,g=None:{**dict(baslik=b,aciklama=a,islem=i),**({'gorsel':g} if g else {})}
TEK=B('Tek-çift kuralları','tek + tek = çift · çift + çift = çift · tek + çift = tek')
CARP=B('Çarpımda tek-çift','çarpanlardan biri çiftse çarpım çifttir; hepsi tekse çarpım tektir. Kare de bir çarpımdır: a² = a × a')
IKI=B('İki basamaklı sayı','AB = 10 × A + B (A onlar, B birler basamağı). Örnek: 74 = 10 × 7 + 4')
ASAL=B('Asal sayı','1’den büyük, yalnızca 1’e ve kendisine bölünen sayı: 2, 3, 5, 7, 11, 13, … 2, çift olan tek asal sayıdır')
FAK=B('Faktöriyel','n! = 1 × 2 × … × n. Örnek: 4! = 24. Ayrıca 7! = 7 × 6 × 5! gibi yazılabilir')
KUV=B('Kuvvetin işareti','Çift kuvvet sıfırdan farklı her sayıda pozitiftir: (−2)⁴ = 16 · Tek kuvvet işareti korur: (−2)³ = −8')
ISR=B('Çarpımın işareti','aynı işaretli iki sayının çarpımı pozitif (+), zıt işaretli iki sayının çarpımı negatiftir (−)')
KES=B('Kesirleri karşılaştırma','kesri ondalığa çevir (pay ÷ payda). Örnek: 2/3 ≈ 0,667 · 7/10 = 0,7 · 17/25 = 0,68')
ARD=B('Ardışık tek ve çift sayılar','ikişer artarlar. Ardışık çift: x, x + 2, x + 4, … Ardışık tek: y, y + 2, y + 4, … (x çift, y tek)')
CM=B('Metre ve santimetre','1 m = 100 cm. Örnek: 0,1 m = 10 cm · 0,2 m = 20 cm')
GOS=B('Bir bölmenin değeri','iki etiket arasındaki fark ÷ aradaki bölme sayısı')
RT=B('Rakamları toplamı','sayının rakamları tek tek toplanır. Örnek: 352 için 3 + 5 + 2 = 10')
RC=B('Rakamları çarpımı','rakamlar tek tek çarpılır. Örnek: 258 için 2 × 5 × 8 = 80. Rakamlardan biri 0 ise çarpım 0 olur')
PAR=B('İşlem sırası','önce parantezin içi yapılır, sonra dışarıdaki işlem')
PER=B('Tekrar eden dizi','k terimlik bir blok tekrar ediyorsa terim sayısını k’ye böl: bölüm tam blok sayısı, kalan da sondaki ek terim sayısıdır')
RAK=B('Rakamları farklı sayı','her rakam en fazla bir kez kullanılır. Örnek: 101’de 1 iki kez geçtiği için rakamları farklı değildir')
TC=B('Tek mi, çift mi?','birler basamağı 0, 2, 4, 6 ya da 8 olan sayı çift; 1, 3, 5, 7 ya da 9 olan sayı tektir')
ANA=[];KAR=[]
def R(no,tipId,tip,zorluk,konu,k,kazanim,kalip,adim,kart,metin,siklar,sik,istenen,ipuclari,bilgi,adimlar,puf,cel,kisa=None,sekil=None,tur=None):
    S=dict(zip('ABCDE',siklar))
    ANA.append(dict(id='tytmat-sayilar-'+no,ders='TYT Matematik',konu=konu,k=k,kazanim=kazanim,tipId=tipId,tip=tip,zorluk=zorluk,seviye='ÖSYM',kalip=kalip,adimSayisi=adim,
      metin=metin,sekil=sekil,siklar=S,cevap=dict(sik=sik,deger=S[sik]),celdiriciler=cel,istenen=istenen,bilgi=bilgi,ipuclari=ipuclari,adimlar=adimlar,puf=puf,kisaYol=kisa,
      kardes='tytmat-sayilar-'+no+'k',celTur=tur,kaynakKart=kart,dogrulama=dict(yontem2=True,tarama=True,korCozum=True)))
def K(no,metin,siklar,sik,istenen,ipuclari,bilgi,adimlar,puf,cel,kisa=None,sekil=None,tur=None):
    a=[x for x in ANA if x['id']=='tytmat-sayilar-'+no][0]; S=dict(zip('ABCDE',siklar))
    KAR.append(dict(id=a['id']+'k',ana=a['id'],ders=a['ders'],konu=a['konu'],k=a['k'],kazanim=a['kazanim'],tipId=a['tipId'],tip=a['tip'],zorluk=a['zorluk'],seviye='ÖSYM',kalip=a['kalip'],
      adimSayisi=a['adimSayisi'],metin=metin,sekil=sekil,siklar=S,cevap=dict(sik=sik,deger=S[sik]),celdiriciler=cel,istenen=istenen,bilgi=bilgi,ipuclari=ipuclari,adimlar=adimlar,puf=puf,kisaYol=kisa,celTur=tur,
      kaynakKart=a['kaynakKart'].split(' · ')[0]+' · kardeş ('+no+'): aynı tip ve zorluk, yeni kurgu ve sayılar',dogrulama=dict(yontem2=True,tarama=True,korCozum=True)))
ds=lambda n:sum(map(int,str(n)))
def dp(n):
    r=1
    for c in str(n): r*=int(c)
    return r
def oncul(vals,I,II,III):
    """vals: olası durumlar; I/II/III: durum→bool. Kesin doğru olanların kümesi."""
    return {ad for ad,f in (('I',I),('II',II),('III',III)) if all(f(*v) for v in vals)}


TT=lambda **k:k
# ===== 0043 tek-çift KOLAY (K-SK-02)
for k_,e_ in product(range(1,40,2),range(2,40,2)):
    assert (k_+e_)%2==1 and (k_*e_)%2==0 and (e_*e_)%2==0 and (k_*k_+1)%2==0 and (2*k_+e_)%2==0
R('0043','sk-tek-cift','Tek ve çift sayılar','kolay','Temel Kavramlar · Tek ve Çift Sayılar','mat|Temel Kavramlar','Tek ve çift sayılarla yapılan işlemlerin sonucunun tek mi çift mi olduğunu belirler.','hikâyeli',2,
 'K-SK-02 (tek-çift koşulları) · yeni kurgu (sınıf mevcudu), yeni istenen (kesin tek)',
 'Bir sınıfta K kız ve E erkek öğrenci vardır. Kız öğrencilerin sayısının tek, erkek öğrencilerin sayısının çift olduğu biliniyor.\nBuna göre aşağıdaki işlemlerden hangisinin sonucu her zaman bir tek sayıdır?',
 ['K · E','E²','K² + 1','2K + E','K + E'],'E','Her durumda tek çıkan ifade.',
 ['Tek yerine 1, çift yerine 2 koyarak şıkları dene.','Çarpımda bir çarpan çiftse sonuç ne olur?','Tek + çift ne verir?'],[TEK,CARP],
 [A('Kuralları hatırla','Çarpanlardan biri çiftse çarpım çift. Tek + çift = tek.','K tek · E çift'),
  A('Şıkları dene','K · E ve E² çift, çünkü E çift. K² tek olduğundan K² + 1 çift. 2K + E de çift + çift = çift.','yalnız K + E kalır'),
  A('Sonuç','Tek + çift = tek.','K + E tek')],
 'Tek-çift şıklarında tek yerine 1, çift yerine 2 koymak en hızlı kontroldür.',
 dict(A='K · E çifttir: çarpanlardan biri (E) çift.',B='E² = E × E; çift sayının karesi çifttir.',C='K² tek, tek + 1 = çift olur.',D='2K her zaman çift; çift + çift = çift.'),
 tur=TT(A='bilgi',B='bilgi',C='islem',D='islem'))
K('0043','Bir kütüphanedeki roman sayısı r, dergi sayısı d’dir. r bir çift sayı, d bir tek sayıdır.\nBuna göre aşağıdakilerden hangisi kesinlikle çift sayıdır?',
 ['r + d','d²','d + 2r','r + 3d','r · d'],'E','Her durumda çift çıkan ifade.',
 ['Çift yerine 2, tek yerine 1 koyarak şıkları dene.','Tek sayının karesi tek mi çift mi?','Çarpımda bir çarpan çiftse sonuç ne olur?'],[TEK,CARP],
 [A('Kuralları hatırla','Çarpanlardan biri çiftse çarpım çift; tek + çift = tek.','r çift · d tek'),
  A('Şıkları dene','r + d tek. d² tek. 2r çift, d + 2r tek. 3d tek, r + 3d tek.','yalnız r × d kalır'),
  A('Sonuç','Çarpanlardan biri (r) çift.','r × d çift')],
 'Bir çarpanı çift olan çarpım her zaman çifttir; toplamda ise tek bir tek terim sonucu tek yapar.',
 dict(A='r + d = çift + tek = tek.',B='d² = d × d; tek sayının karesi tektir.',C='2r çift; tek + çift = tek.',D='3d tek; çift + tek = tek.'),
 tur=TT(A='islem',B='bilgi',C='islem',D='islem'))
for r_,d_ in product(range(2,40,2),range(1,40,2)):
    assert (r_*d_)%2==0 and (r_+d_)%2 and (d_*d_)%2 and (d_+2*r_)%2 and (r_+3*d_)%2

# ===== 0044 tanımlı ZOR (K-SK-01)
v=[10*a+b for a in range(1,10) for b in range(1,10) if abs(9*(a-b))==45]; assert len(v)==8 and 50 not in v
R('0044','sk-tanimli','Tanımlı sayılar ve semboller','zor','Temel Kavramlar · Rakam ve Sayı','mat|Temel Kavramlar','Tanımlanan sayı türünü basamak çözümlemesiyle ifade eder; koşulu sağlayan sayıları eksiksiz sayar.','düz',4,
 'K-SK-01 (rakamlarla tanımlanan sayı türü) · yeni tanım (ayna ve fark sayısı), yeni istenen (sayıların adedi)',
 'A ve B birer rakam olmak üzere, iki basamaklı AB sayısının rakamlarının yerleri değiştirilerek elde edilen BA sayısına AB’nin “aynası” denir. Bir sayı ile aynası arasındaki pozitif farka da o sayının “fark sayısı” denir.\nAynası da iki basamaklı olan ve fark sayısı 45 olan kaç tane iki basamaklı sayı vardır?',
 ['4','5','8','9','10'],'C','Koşulları sağlayan iki basamaklı sayıların adedi.',
 ['AB − BA farkını A ve B cinsinden yaz.','Fark 45 ise A ile B arasındaki fark kaç olmalı?','Aynanın iki basamaklı olması için B ne olamaz? A > B ve A < B durumlarını ayrı say.'],[IKI],
 [A('Farkı yaz','AB − BA = (10A + B) − (10B + A).','AB − BA = 9A − 9B = 9 × (A − B)'),
  A('Rakam farkı','Pozitif fark 45 ise rakamlar arasındaki fark 5.','9 × 5 = 45 ⇒ A ile B arasındaki fark 5'),
  A('Ayna koşulu','Aynanın iki basamaklı olması için birler basamağı 0 olamaz; ayrıca A da 0 olamaz. İki rakam da 1–9 arasında.','50 olmaz (aynası 05)'),
  A('Say','Büyük rakam 6, 7, 8, 9 iken küçük rakam 1, 2, 3, 4. Her ikili iki sayı verir.','61, 72, 83, 94 · 16, 27, 38, 49'),
  A('Sonuç','4 ikili × 2 sıralama.','8 sayı')],
 'AB ile BA’nın farkı her zaman 9 × (rakam farkı)’dır. Sayarken 0’lı durumları ve iki sıralamayı (AB ve BA) unutma.',
 dict(A='4 yalnızca onlar basamağı büyük olanlar; 16, 27, 38, 49 da fark sayısı 45 olan sayılar.',B='5, 50’yi de saymak; 50’nin aynası 05 iki basamaklı değil.',D='9, 50’yi de eklemek; aynası iki basamaklı değil.',E='10, 50 ve 05’i de saymak; ikisi de koşulu sağlamaz.'),
 tur=TT(A='dikkat',B='dikkat',D='dikkat',E='bilgi'))
v=[10*a+b for a in range(1,10) for b in range(1,10) if abs(9*(a-b))==63]; assert sorted(v)==[18,29,81,92]
K('0044','K ve L birer rakam olmak üzere, iki basamaklı KL sayısının rakamlarının yerleri değiştirilerek elde edilen LK sayısına KL’nin “tersi” denir. Bir sayı ile tersi arasındaki pozitif farka o sayının “açıklığı” denir.\nTersi de iki basamaklı olan ve açıklığı 63 olan kaç tane iki basamaklı sayı vardır?',
 ['2','3','4','5','6'],'C','Koşulları sağlayan iki basamaklı sayıların adedi.',
 ['KL − LK farkını K ve L cinsinden yaz.','Fark 63 ise rakamlar arasındaki fark kaç?','Tersi iki basamaklı olmalı: 0 içeren sayıları ele; iki sıralamayı da say.'],[IKI],
 [A('Farkı yaz','KL − LK = (10K + L) − (10L + K).','KL − LK = 9 × (K − L)'),
  A('Rakam farkı','Pozitif fark 63 ise rakamlar arasındaki fark 7.','9 × 7 = 63'),
  A('Ayna koşulu','Tersinin iki basamaklı olması için rakamlar 1–9 arasında olmalı; 70 olmaz (tersi 07).','70 olmaz'),
  A('Say','Fark 7 olan ikililer: (8, 1) ve (9, 2). Her biri iki sayı verir.','81, 92 · 18, 29'),
  A('Sonuç','2 ikili × 2 sıralama.','4 sayı')],
 'Rakam farkı d ise sayının kendisi ile tersinin farkı 9d’dir; sayım yaparken 0’ı ve ters sıralamayı kontrol et.',
 dict(A='2 yalnızca onlar basamağı büyük olanlar (81, 92); 18 ve 29 da sağlıyor.',B='3, 70’i de ekleyip ters sıralamayı unutmak.',D='5, 70’i de saymak; 70’in tersi 07 iki basamaklı değil.',E='6, 70 ve 07’yi de saymak; ikisi de koşulu sağlamaz.'),
 tur=TT(A='dikkat',B='dikkat',D='dikkat',E='bilgi'))

# ===== 0045 ardışık ORTA (K-SK-35)
p_=[p for p in range(1,50) if 3*p+1==37]; assert p_==[12] and 9*12==108
R('0045','sk-ardisik','Ardışık sayılar','orta','Temel Kavramlar · Ardışık Sayılar','mat|Temel Kavramlar','Ardışık numaralı kayıtların eşit gruplara dağılımında grup büyüklüğünü ve istenen numarayı bulur.','hikâyeli',3,
 'K-SK-35 (ardışık numaralı kayıtlar, eşit sayfalar) · yeni kurgu (defter), yeni istenen (son kayıt)',
 'Bir defterin sayfalarına 1’den başlayarak ardışık numaralı kayıtlar yazılmıştır. Her sayfada eşit sayıda kayıt vardır ve sayfalar sırayla doldurulmuştur.\n4. sayfadaki ilk kaydın numarası 37’dir.\nBuna göre 9. sayfadaki son kaydın numarası kaçtır?',
 ['96','97','99','108','117'],'D','9. sayfanın son kaydının numarası.',
 ['Bir sayfada p kayıt varsa ilk 3 sayfada kaç kayıt vardır?','4. sayfanın ilk kaydı, ilk 3 sayfadaki kayıt sayısından 1 fazladır.','9. sayfanın son kaydı, ilk 9 sayfadaki toplam kayıt sayısıdır.'],[B('Sayfadaki kayıtlar','her sayfada p kayıt varsa n. sayfanın son kaydı n × p, ilk kaydı (n − 1) × p + 1’dir')],
 [A('Sayfa başı kayıt','İlk 3 sayfa dolu; 4. sayfa 37 ile başlıyor.','3p + 1 = 37 ⇒ p = 12'),
  A('İlk 9 sayfa','9. sayfanın son kaydı, ilk 9 sayfadaki kayıt sayısıdır.','9 × 12 = 108'),
  A('Kontrol','9. sayfa 97 ile başlar, 12 kayıt sürer.','97, 98, …, 108')],
 'n. sayfanın son kaydı n × p’dir; ilk kaydı bir önceki sayfanın son kaydından 1 fazladır.',
 dict(A='96, 8. sayfanın son kaydı.',B='97, 9. sayfanın ilk kaydı; soru son kaydı soruyor.',C='99, bir sayfada 11 kayıt varsayınca çıkıyor; 3p + 1 = 37’den p = 12.',E='117, bir sayfada 13 kayıt varsaymak; 37’yi ilk 3 sayfanın kayıt sayısı sanmışsın (3p = 37 değil, 3p + 1 = 37).'),
 tur=TT(A='dikkat',B='dikkat',C='islem',E='islem'))
p_=[p for p in range(1,50) if 2*p+1==31]; assert p_==[15] and 7*15==105
K('0045','Bir sinema salonunun koltukları 1’den başlayarak ardışık olarak numaralandırılmıştır. Her sırada eşit sayıda koltuk vardır ve numaralar sıra sıra verilmiştir.\n3. sıradaki ilk koltuğun numarası 31’dir.\nBuna göre 7. sıradaki son koltuğun numarası kaçtır?',
 ['90','91','98','105','112'],'D','7. sıranın son koltuğunun numarası.',
 ['Bir sırada p koltuk varsa ilk 2 sırada kaç koltuk vardır?','3. sıranın ilk koltuğu, ilk 2 sıradaki koltuk sayısından 1 fazladır.','7. sıranın son koltuğu, ilk 7 sıradaki koltuk sayısıdır.'],[B('Sıradaki numaralar','her sırada p koltuk varsa n. sıranın son numarası n × p, ilk numarası (n − 1) × p + 1’dir')],
 [A('Sıra başı koltuk','İlk 2 sıra dolu; 3. sıra 31 ile başlıyor.','2p + 1 = 31 ⇒ p = 15'),
  A('İlk 7 sıra','7. sıranın son koltuğu, ilk 7 sıradaki koltuk sayısıdır.','7 × 15 = 105'),
  A('Kontrol','7. sıra 91 ile başlar, 15 koltuk sürer.','91, 92, …, 105')],
 'İlk numara verilen sırada önceki sıraların toplamına 1 ekle; son numara ise sıra sayısı × sıra başı koltuktur.',
 dict(A='90, 6. sıranın son koltuğu.',B='91, 7. sıranın ilk koltuğu; soru son koltuğu soruyor.',C='98, bir sırada 14 koltuk varsaymak; 2p + 1 = 31’den p = 15.',E='112, bir sırada 16 koltuk varsaymak.'),
 tur=TT(A='dikkat',B='dikkat',C='islem',E='islem'))

# ===== 0046 asal ZOR (K-SK-27)
P=[p for p in range(2,100) if all(p%d for d in range(2,int(p**.5)+1))]
v=[(a,b,c) for a in P for b in P for c in P if a<b<c and a+b+c==50]; assert max(c for a,b,c in v)==43 and all(a==2 for a,b,c in v)
R('0046','sk-asal','Asal sayılar','zor','Temel Kavramlar · Asal Sayılar','mat|Temel Kavramlar','Asal sayıların tek-çift özelliğinden birinin 2 olduğunu çıkarır; en büyük değeri koşulları sınayarak bulur.','düz',4,
 'K-SK-27 (asal denklemde parite: biri 2) · yeni denklem (üç asalın toplamı), yeni istenen (en büyük değer)',
 'a, b ve c asal sayılar ve a < b < c olmak üzere\na + b + c = 50\nolduğuna göre c en çok kaçtır?',
 ['43','45','46','47','48'],'A','c’nin alabileceği en büyük değer.',
 ['Üç tek sayının toplamı tek mi çift mi? 50 çift.','Demek ki asallardan biri çift olmalı; hangisi?','c’yi büyütmek için b’yi olabildiğince küçük seç; c’nin asal olduğunu kontrol et.'],[ASAL,TEK],
 [A('Tek-çift','Üç tek sayının toplamı tektir (tek + tek = çift, çift + tek = tek). 50 çift olduğuna göre üçü birden tek olamaz.','biri çift ⇒ 2'),
  A('a = 2','Çift olan tek asal 2; en küçük olduğu için a = 2.','b + c = 48'),
  A('b’yi küçült','c en büyük olsun diye b’yi en küçük dene. b = 3 ⇒ c = 45 = 9 × 5, asal değil.','b = 3 olmaz'),
  A('Sonraki deneme','b = 5 ⇒ c = 43; 43 asal ✓.','c = 43')],
 'En büyük değeri ararken diğerini en küçükten başlayarak dene ve her adımda asallığı kontrol et.',
 dict(B='45 asal değil (45 = 9 × 5); b = 3 seçince çıkan değer.',C='46 çift sayı ve 2’den büyük; asal olamaz.',D='47 için a + b = 3 olmalı; iki farklı asalın toplamı en az 2 + 3 = 5.',E='48, b + c toplamı; c tek başına bu kadar olamaz.'),
 tur=TT(B='dikkat',C='bilgi',D='islem',E='dikkat'))
v=[(a,b,c) for a in P for b in P for c in P if a<b<c and a+b+c==40]; assert max(c for a,b,c in v)==31
K('0046','x, y ve z asal sayılar ve x < y < z olmak üzere\nx + y + z = 40\nolduğuna göre z en çok kaçtır?',
 ['31','33','35','36','38'],'A','z’nin alabileceği en büyük değer.',
 ['Toplam çift; üç asal da tek olabilir mi?','Çift olan asal hangisi ve en küçük harf hangisi?','z’yi büyütmek için y’yi küçükten dene; z asal mı, kontrol et.'],[ASAL,TEK],
 [A('Tek-çift','Üç tek sayının toplamı tek olur; 40 çift.','biri 2 olmalı'),
  A('x = 2','En küçük asal x olduğundan x = 2.','y + z = 38'),
  A('Küçük y değerleri','y = 3 ⇒ z = 35 = 5 × 7 · y = 5 ⇒ z = 33 = 3 × 11. İkisi de asal değil.','olmaz'),
  A('y = 7','z = 31; 31 asal ✓.','z = 31')],
 'Asallığı her denemede kontrol et: 33 ve 35 gibi tek sayılar asal görünür ama değildir.',
 dict(B='33 = 3 × 11, asal değil (y = 5 denemesi).',C='35 = 5 × 7, asal değil (y = 3 denemesi).',D='36 için x + y = 4 olmalı; 2 + 2 olur ama x < y koşulu bozulur.',E='38, y + z toplamı; z tek başına bu kadar olamaz.'),
 tur=TT(B='bilgi',C='bilgi',D='dikkat',E='dikkat'))

# ===== 0047 basamak ORTA (K-SK-24)
v=[(a,b) for a in range(1,10) for b in range(1,10) if a>b and 2*((10*a+b)+(10*b+a))==264 and (10*a+b)-(10*b+a)==36]; assert v==[(8,4)]
R('0047','sk-basamak','Basamak çözümleme','orta','Temel Kavramlar · Sayı Basamakları','mat|Sayı Basamakları','Harfli iki basamaklı uzunluklarla verilen toplam ve farktan rakamları bulur.','hikâyeli',3,
 'K-SK-24 (gerçek nesne uzunlukları harfli sayılarla) · yeni kurgu (dikdörtgen masa), çevre ve fark bilgisi',
 'Dikdörtgen biçimindeki bir masanın uzun kenarı AB santimetre, kısa kenarı BA santimetredir. A ve B sıfırdan farklı rakamlardır.\nMasanın uzun kenarı kısa kenarından 36 cm uzundur ve masanın çevresi 264 cm’dir.\nBuna göre masanın uzun kenarı kaç santimetredir?',
 ['48','66','84','93','132'],'C','Masanın uzun kenarı (AB).',
 ['Dikdörtgenin çevresi 2 × (uzun kenar + kısa kenar). AB + BA kaç olur?','AB + BA = 11 × (A + B) ve AB − BA = 9 × (A − B).','A + B ile A − B’yi bulunca A ve B’yi çöz.'],[IKI,B('Dikdörtgenin çevresi','çevre = 2 × (uzun kenar + kısa kenar). Örnek: 5 cm ve 3 cm ⇒ 16 cm')],
 [A('Kenarların toplamı','Çevre 264 ise iki kenarın toplamı yarısıdır.','AB + BA = 264 ÷ 2 = 132'),
  A('A + B','AB + BA = (10A + B) + (10B + A).','11 × (A + B) = 132 ⇒ A + B = 12'),
  A('A − B','AB − BA = (10A + B) − (10B + A).','9 × (A − B) = 36 ⇒ A − B = 4'),
  A('Rakamlar','Toplamı 12, farkı 4 olan iki rakam.','A = 8 · B = 4'),
  A('Uzun kenar','AB = 84 cm (kısa kenar 48 cm).','84 − 48 = 36 ✓ · 2 × (84 + 48) = 264 ✓')],
 'AB + BA her zaman 11’in, AB − BA her zaman 9’un katıdır; bu iki eşitlik rakamları hemen verir.',
 dict(A='48, kısa kenar (BA); soru uzun kenarı soruyor.',B='66, iki kenarın toplamının yarısı; kenarlar eşit değil.',D='93, farkı 6 × (A − B) gibi yanlış çözümleyip A − B = 6 almak.',E='132, iki kenarın toplamı; çevrenin yarısı.'),
 tur=TT(A='dikkat',B='islem',D='bilgi',E='dikkat'))
v=[(a,b) for a in range(1,10) for b in range(1,10) if a>b and 2*((10*a+b)+(10*b+a))==242 and (10*a+b)-(10*b+a)==27]; assert v==[(7,4)]
K('0047','Dikdörtgen biçimindeki bir tablonun genişliği KL santimetre, yüksekliği LK santimetredir. K ve L sıfırdan farklı rakamlardır.\nTablonun genişliği yüksekliğinden 27 cm fazladır ve tablonun çevresi 242 cm’dir.\nBuna göre tablonun yüksekliği kaç santimetredir?',
 ['29','47','74','92','121'],'B','Tablonun yüksekliği (LK).',
 ['Çevrenin yarısı, genişlik ile yüksekliğin toplamıdır.','KL + LK = 11 × (K + L) ve KL − LK = 9 × (K − L).','K ve L’yi bulup LK’yi yaz.'],[B('İki basamaklı sayı','KL = 10 × K + L (K onlar, L birler basamağı). Örnek: 74 = 10 × 7 + 4'),B('Dikdörtgenin çevresi','çevre = 2 × (genişlik + yükseklik). Örnek: 5 cm ve 3 cm ⇒ 16 cm')],
 [A('Kenarların toplamı','Çevre 242 ise genişlik + yükseklik bunun yarısı.','KL + LK = 121'),
  A('K + L','KL + LK = 11 × (K + L).','11 × (K + L) = 121 ⇒ K + L = 11'),
  A('K − L','KL − LK = 9 × (K − L).','9 × (K − L) = 27 ⇒ K − L = 3'),
  A('Rakamlar','Toplamı 11, farkı 3 olan iki rakam.','K = 7 · L = 4'),
  A('Yükseklik','LK = 47 cm (genişlik 74 cm).','74 − 47 = 27 ✓ · 2 × (74 + 47) = 242 ✓')],
 'Toplam bilgisi 11’e, fark bilgisi 9’a bölünür; rakamlar iki küçük denklemden çıkar.',
 dict(A='29 için K = 9, L = 2: toplam 11 tutar ama genişlik ile yükseklik farkı 63 olur, 27 değil.',C='74, genişlik (KL); soru yüksekliği soruyor.',D='92, 9 ve 2’den yazılan diğer sayı; fark koşulunu kontrol etmemişsin.',E='121, genişlik ile yüksekliğin toplamı.'),
 tur=TT(A='dikkat',C='dikkat',D='dikkat',E='dikkat'))

# ===== 0048 faktöriyel ORTA (K-SK-25)
assert F(4)*F(3)==144 and len(set(permutations(range(4))))*len(set(permutations(range(3))))==144
R('0048','sk-faktoriyel','Faktöriyel','orta','Temel Kavramlar · Faktöriyel','mat|Temel Kavramlar','Bağımsız iki sıralamanın sayısını çarpma ilkesiyle bulur ve faktöriyelle ifade eder.','hikâyeli',3,
 'K-SK-25 (gerçek hayatta çarpımla sayma, faktöriyelli sonuç) · yeni kurgu (raf ve masa), yeni sayılar',
 'Elif’in birbirinden farklı 4 kitabı ve birbirinden farklı 3 defteri vardır. Elif kitapları rafa yan yana, defterleri de masanın üstüne yan yana dizecektir.\nBuna göre Elif bu dizilişi kaç farklı biçimde yapabilir?',
 ['4 · 3','4! + 3!','7! / 3!','7!','4! · 3!'],'E','Raf ve masa dizilişlerinin birlikte kaç farklı biçimde yapılabileceği.',
 ['4 farklı kitap rafa kaç farklı biçimde dizilir?','3 farklı defter masaya kaç farklı biçimde dizilir?','İki iş birlikte yapılıyorsa sayılar toplanır mı, çarpılır mı?'],[FAK,B('Çarpma ilkesi','bir iş m, diğer iş n farklı biçimde yapılıyorsa ikisi birlikte m × n biçimde yapılır')],
 [A('Kitaplar','İlk yere 4, ikinciye 3, üçüncüye 2, sonuncuya 1 kitap seçilebilir.','4 × 3 × 2 × 1 = 4! = 24'),
  A('Defterler','Aynı düşünceyle 3 defter.','3 × 2 × 1 = 3! = 6'),
  A('Birleştir','Her kitap dizilişi her defter dizilişiyle birleşebilir; çarp.','4! · 3! = 24 × 6 = 144')],
 'Farklı nesneleri yan yana dizmenin yolu n!’dir; birbirinden bağımsız iki iş için yol sayıları çarpılır.',
 dict(A='4 · 3, yalnızca sayıları çarpmak; her diziliş için tüm sıralamalar sayılmalı.',B='4! + 3!, iki işin sayılarını toplamak; işler birlikte yapıldığı için çarpılır.',C='7! / 3!, sanki 7 nesneden 4’ü seçilip dizilmiş gibi hesaplamak.',D='7!, kitap ve defterleri tek sırada karışık dizmek; ayrı yerlere diziliyorlar.'),
 tur=TT(A='bilgi',B='bilgi',C='bilgi',D='dikkat'))
assert F(5)*F(2)==240
K('0048','Bir mağaza çalışanı birbirinden farklı 5 şapkayı vitrine yan yana, birbirinden farklı 2 vazoyu da kasanın yanındaki rafa yan yana dizecektir.\nBuna göre bu dizilişler kaç farklı biçimde yapılabilir?',
 ['5! · 2!','5! + 2!','7! / 2!','7!','5 · 2'],'A','Vitrin ve raf dizilişlerinin birlikte kaç farklı biçimde yapılabileceği.',
 ['5 farklı şapka yan yana kaç farklı biçimde dizilir?','2 farklı vazo kaç farklı biçimde dizilir?','İki iş birlikte yapıldığında sayılar çarpılır.'],[FAK,B('Çarpma ilkesi','bir iş m, diğer iş n farklı biçimde yapılıyorsa ikisi birlikte m × n biçimde yapılır')],
 [A('Şapkalar','5 farklı şapka yan yana.','5! = 120'),
  A('Vazolar','2 farklı vazo yan yana.','2! = 2'),
  A('Birleştir','İki diziliş birbirinden bağımsız; çarp.','5! · 2! = 240')],
 'Ayrı yerlerde yapılan dizilişlerde her yerin sayısını ayrı bul, sonra çarp.',
 dict(B='5! + 2!, sayıları toplamak; iki diziliş birlikte yapıldığı için çarpılır.',C='7! / 2!, 7 nesneyi tek sırada dizip vazoları ayırt etmemek gibi hesaplamak.',D='7!, şapka ve vazoları tek sırada karışık dizmek; ayrı yerlere diziliyorlar.',E='5 · 2, yalnızca nesne sayılarını çarpmak; sıralamalar sayılmalı.'),
 tur=TT(B='bilgi',C='bilgi',D='dikkat',E='bilgi'))

# ===== 0049 kesir KOLAY (K-SK-10)
assert (1-Fr(2,5))*Fr(1,3)==Fr(1,5)
R('0049','sk-kesir','Kesirler ve rasyonel sayılar','kolay','Temel Kavramlar · Rasyonel Sayılar','mat|Rasyonel Sayılar','“Kalanın kesri” ifadesini bütüne göre kesre çevirir.','hikâyeli',2,
 'K-SK-10 (bütünün parçası, parçanın parçası) · yeni kurgu (şişedeki su), yeni istenen (dökülen kısım)',
 'Bir şişedeki suyun 2/5’i içilmiş, kalan suyun 1/3’ü de yere dökülmüştür.\nBuna göre yere dökülen su, şişedeki suyun tamamının kaçta kaçıdır?',
 ['1/5','4/15','1/3','2/5','3/5'],'A','Dökülen suyun başlangıçtaki suya oranı.',
 ['İçildikten sonra suyun kaçta kaçı kaldı?','“Kalanın 1/3’ü” kalanla 1/3’ün çarpımıdır.','Bulduğun kesri sadeleştir.'],[B('Kalanın kesri','“kalanın 1/3’ü” = kalan × 1/3. Örnek: 3/4’ün 1/3’ü = 3/4 × 1/3 = 1/4')],
 [A('Kalan su','2/5 içilince geriye kalan.','1 − 2/5 = 3/5'),
  A('Dökülen','Kalanın 1/3’ü.','3/5 × 1/3 = 3/15'),
  A('Sadeleştir','Pay ve paydayı 3’e böl.','3/15 = 1/5')],
 '“Kalanın” kelimesini görünce önce kalanı bul; kesri bütüne değil kalana uygula.',
 dict(B='4/15 = 2/5 × 2/3; kesri içilen kısma uygulamışsın.',C='1/3, kesri şişenin tamamına uygulamak; dökülen kalanın 1/3’ü.',D='2/5, kalan suyun dökülmeden sonraki hâli (3/5 × 2/3); soru dökülen kısmı soruyor.',E='3/5, içildikten sonra kalan su; dökülen kısım değil.'),
 tur=TT(B='islem',C='dikkat',D='dikkat',E='dikkat'))
assert (1-Fr(1,4))*Fr(2,3)==Fr(1,2)
K('0049','Bir pastanın 1/4’ü yenmiş, kalan pastanın 2/3’ü de paketlenmiştir.\nBuna göre paketlenen pasta, pastanın tamamının kaçta kaçıdır?',
 ['1/6','1/4','1/3','1/2','2/3'],'D','Paketlenen kısmın bütüne oranı.',
 ['Yendikten sonra pastanın kaçta kaçı kaldı?','“Kalanın 2/3’ü” kalanla 2/3’ün çarpımıdır.','Sonucu sadeleştir.'],[B('Kalanın kesri','“kalanın 2/3’ü” = kalan × 2/3. Örnek: 3/5’in 2/3’ü = 3/5 × 2/3 = 2/5')],
 [A('Kalan pasta','1/4 yenince geriye kalan.','1 − 1/4 = 3/4'),
  A('Paketlenen','Kalanın 2/3’ü.','3/4 × 2/3 = 6/12'),
  A('Sadeleştir','Pay ve paydayı 6’ya böl.','6/12 = 1/2')],
 'Kesir “kalan” üzerinden verildiyse önce kalanı bul, sonra çarp.',
 dict(A='1/6 = 1/4 × 2/3; kesri yenen kısma uygulamışsın.',B='1/4, masada kalan pasta (3/4 × 1/3); soru paketleneni soruyor.',C='1/3, kalanın paketlenmeyen payı; bütüne göre değil.',E='2/3, kesri pastanın tamamına uygulamak; paketlenen kalanın 2/3’ü.'),
 tur=TT(A='islem',B='dikkat',C='dikkat',E='dikkat'))

# ===== 0050 yerleştirme ORTA (K-SK-18)
def ucgen(S):
    r=[]
    for p in permutations(range(1,7)):
        k0,m01,k1,m12,k2,m20=p
        if k0+m01+k1==S and k1+m12+k2==S and k2+m20+k0==S: r.append(p)
    return r
u=ucgen(11); assert u and {p[0]+p[2]+p[4] for p in u}=={12}
coz=[p for p in u if (p[0],p[2],p[4])==(2,4,6)][0]
R('0050','sk-yerlestirme','Kutulara yerleştirme ve işlem bulma','orta','Temel Kavramlar · Temel İşlemler','mat|Temel Kavramlar','Eşit toplam koşulunda her sayının kaç kez sayıldığını düşünerek bilinmeyen toplamı bulur.','şekilli',3,
 'K-SK-18 (eşit toplamlı yerleştirme) · yeni şekil (üçgen, köşe ve kenar ortaları), yeni istenen (köşelerin toplamı)',
 'Aşağıdaki üçgenin köşelerindeki ve kenarlarının ortasındaki dairelere 1, 2, 3, 4, 5 ve 6 sayıları her daireye bir sayı gelecek biçimde yerleştirilecektir.\nÜçgenin her kenarı üzerindeki üç sayının toplamı 11 olduğuna göre köşelerdeki sayıların toplamı kaçtır?',
 ['6','9','10','11','12'],'E','Köşelerdeki üç sayının toplamı.',
 ['Üç kenarın toplamlarını topladığında hangi sayılar iki kez sayılır?','Altı sayının toplamı kaç?','Üç kenar toplamı = altı sayının toplamı + köşelerin toplamı.'],[B('İki kez sayılanlar','her köşe iki kenarın üzerindedir; kenar toplamlarını toplayınca köşeler iki kez sayılır')],
 [A('Kenar toplamları','Üç kenarın her biri 11.','11 + 11 + 11 = 33'),
  A('Neler sayıldı?','Kenar ortaları birer kez, köşeler ikişer kez sayıldı. Her sayıyı bir kez alırsak 1 + 2 + … + 6 = 21.','33 = 21 + köşelerin toplamı'),
  A('Köşeler','Fark, ikinci kez sayılan köşelerdir.','köşelerin toplamı = 33 − 21 = 12',G.cokgen_daire(3,list(coz),vurgu_kose=True))],
 'Eşit toplamlı yerleştirmelerde tüm toplamları topla; birden fazla kez sayılan yerler sorunun anahtarıdır.',
 dict(A='6, en küçük üç sayının toplamı (1 + 2 + 3); koşulu kullanmadan tahmin.',B='9, kenar toplamlarını 30 sanıp 30 − 21 hesaplamak.',C='10, en büyük köşe toplamını tahmin etmek; hesap 33 − 21 = 12 veriyor.',D='11, bir kenarın toplamı; soru köşelerin toplamını soruyor.'),
 tur=TT(A='bilgi',B='islem',C='islem',D='dikkat'),sekil=G.cokgen_daire(3))
def kare(S):
    r=[]
    for p in permutations(range(1,9)):
        c0,m0,c1,m1,c2,m2,c3,m3=p
        if c0+m0+c1==S and c1+m1+c2==S and c2+m2+c3==S and c3+m3+c0==S: r.append(p); break
    return r
kz=kare(13); assert kz and 4*13-36==16 and sum(kz[0][0::2])==16
K('0050','Aşağıdaki karenin köşelerindeki ve kenarlarının ortasındaki dairelere 1’den 8’e kadar olan sayılar, her daireye bir sayı gelecek biçimde yerleştirilecektir.\nKarenin her kenarı üzerindeki üç sayının toplamı 13 olduğuna göre köşelerdeki sayıların toplamı kaçtır?',
 ['10','12','14','16','18'],'D','Köşelerdeki dört sayının toplamı.',
 ['Dört kenarın toplamlarını topla; hangi sayılar iki kez sayılır?','1’den 8’e kadar sayıların toplamı kaç?','Dört kenar toplamı = sekiz sayının toplamı + köşelerin toplamı.'],[B('İki kez sayılanlar','her köşe iki kenarın üzerindedir; kenar toplamlarını toplayınca köşeler iki kez sayılır')],
 [A('Kenar toplamları','Dört kenarın her biri 13.','4 × 13 = 52'),
  A('Neler sayıldı?','Kenar ortaları birer, köşeler ikişer kez sayıldı. 1 + 2 + … + 8 = 36.','52 = 36 + köşelerin toplamı'),
  A('Köşeler','İkinci kez sayılanlar köşeler.','köşelerin toplamı = 52 − 36 = 16',G.cokgen_daire(4,list(kz[0]),vurgu_kose=True))],
 'Toplamları üst üste koy; fazladan sayılanlar köşelerdir.',
 dict(A='10, en küçük dört sayının toplamı (1 + 2 + 3 + 4); koşul kullanılmamış.',B='12, 1’den 8’e toplamı 40 sanıp 52 − 40 hesaplamak.',C='14, köşeleri tahminle seçmek; hesap 52 − 36 = 16 veriyor.',E='18, 4 × 13’ü 54 alıp 54 − 36 hesaplamak.'),
 tur=TT(A='bilgi',B='islem',C='islem',E='islem'),sekil=G.cokgen_daire(4))

# ===== 0051 ondalık KOLAY (K-SK-11)
assert Fr('200')-(4*Fr('12.50')+3*Fr('24.75'))==Fr('75.75')
R('0051','sk-ondalik','Ondalık sayılar ve günlük hesap','kolay','Temel Kavramlar · Ondalık Sayılar','mat|Rasyonel Sayılar','Ondalık fiyatlarla alışveriş tutarını ve para üstünü hesaplar.','hikâyeli',2,
 'K-SK-11 (ondalık birim fiyat × miktar, para üstü) · yeni kurgu (kırtasiye), yeni fiyatlar',
 'Bir kırtasiyede kalemin tanesi 12,50 TL, defterin tanesi 24,75 TL’dir.\nMert bu kırtasiyeden 4 kalem ve 3 defter alıp kasaya 200 TL veriyor.\nBuna göre Mert’in alacağı para üstü kaç TL’dir?',
 ['74,25','75,25','75,75','76,75','124,25'],'C','Para üstü.',
 ['Kalemlere ve defterlere ödenen tutarı ayrı ayrı bul.','İki tutarı topla.','200 TL’den çıkar; virgülleri alt alta hizala.'],[B('Ondalık çarpma','virgülü yok sayıp çarp, sonra virgülden sonraki basamak sayısı kadar ayır. Örnek: 24,75 × 3 = 74,25')],
 [A('Kalemler','4 kalem.','4 × 12,50 = 50,00 TL'),
  A('Defterler','3 defter.','3 × 24,75 = 74,25 TL'),
  A('Toplam ve para üstü','Toplamı 200’den çıkar.','50,00 + 74,25 = 124,25 · 200 − 124,25 = 75,75 TL')],
 'Para üstü sorularında önce her ürünün tutarını ayrı bul, sonra topla ve çıkar; virgülleri hizalamayı unutma.',
 dict(A='74,25 TL, defterlerin tutarı; para üstü değil.',B='75,25 TL, çıkarmada kuruşları yanlış hesaplamak (200 − 124,75).',D='76,75 TL, toplamı 123,25 bulmak; 3 × 24,75 = 74,25.',E='124,25 TL, alışverişin tutarı; soru para üstünü soruyor.'),
 tur=TT(A='dikkat',B='islem',D='islem',E='dikkat'))
assert Fr('300')-(3*Fr('42.50')+2*Fr('67.25'))==38
K('0051','Bir manavda elmanın kilogramı 42,50 TL, muzun kilogramı 67,25 TL’dir.\nSeda bu manavdan 3 kilogram elma ve 2 kilogram muz alıp kasaya 300 TL veriyor.\nBuna göre Seda’nın alacağı para üstü kaç TL’dir?',
 ['28,00','38,00','40,50','134,50','262,00'],'B','Para üstü.',
 ['Elmaya ve muza ödenen tutarı ayrı ayrı bul.','İki tutarı topla.','300 TL’den çıkar.'],[B('Ondalık çarpma','virgülü yok sayıp çarp, sonra virgülden sonraki basamak sayısı kadar ayır. Örnek: 67,25 × 2 = 134,50')],
 [A('Elma','3 kg elma.','3 × 42,50 = 127,50 TL'),
  A('Muz','2 kg muz.','2 × 67,25 = 134,50 TL'),
  A('Toplam ve para üstü','Toplamı 300’den çıkar.','127,50 + 134,50 = 262,00 · 300 − 262,00 = 38,00 TL')],
 'Kuruşlu tutarlar toplanınca tam sayı çıkabilir; virgülleri hizalayarak topla.',
 dict(A='28,00 TL, toplamı 272 bulmak; kuruşları toplarken elde hatası.',C='40,50 TL, muzu 2 kg yerine yalnız fiyat farkıyla hesaplamak gibi bir işlem hatası.',D='134,50 TL, muzun tutarı; para üstü değil.',E='262,00 TL, alışverişin tutarı; soru para üstünü soruyor.'),
 tur=TT(A='islem',C='islem',D='dikkat',E='dikkat'))

# ===== 0052 rakam en az–en çok ZOR (K-SK-17)
fk=lambda n:len(set(str(n)))==len(str(n))
mn=min(n for n in range(1000,10000) if fk(n) and n%2==0 and ds(n)==25); assert mn==1798
R('0052','sk-rakam-enaz','Rakamlarla en az – en çok','zor','Temel Kavramlar · Sayı Basamakları','mat|Sayı Basamakları','Rakamlar toplamı, farklılık ve tek-çift koşullarını birlikte kullanarak en küçük sayıyı kurar.','düz',4,
 'K-SK-17 (rakamlarla en az/en çok) · yeni koşullar (rakamlar toplamı + farklı rakamlar + çift)',
 'Rakamları birbirinden farklı ve rakamlarının toplamı 25 olan dört basamaklı en küçük çift sayı kaçtır?',
 ['1789','1798','1879','1978','2698'],'B','Koşulları sağlayan en küçük çift sayı.',
 ['En küçük sayı için binler basamağı olabildiğince küçük olmalı; 1 olabilir mi?','Binler 1 ise kalan üç rakamın toplamı 24; birbirinden farklı hangi üç rakam bunu verir?','Bu üç rakamı küçükten büyüğe diz ama birler basamağı çift olmalı.'],[RAK,TC],
 [A('Binler basamağı','Kalan üç farklı rakamın toplamı en çok 9 + 8 + 7 = 24. Binler 1 olursa toplam 1 + 24 = 25 tutar.','binler = 1'),
  A('Diğer rakamlar','Toplamı 24 olan üç farklı rakam yalnızca 7, 8 ve 9.','{7, 8, 9}'),
  A('Çift olsun','Birler basamağı çift olmalı: bu üç rakamdan çift olan yalnız 8.','birler = 8'),
  A('En küçüğü diz','Kalan 7 ve 9’u küçükten büyüğe yerleştir.','1798')],
 'En küçük sayıda soldan sağa en küçük rakamı seç; ama önce kalan rakamlarla koşulun tamamlanıp tamamlanmadığını kontrol et.',
 dict(A='1789 tek sayı; birler basamağı 9.',C='1879 tek sayı ve 1798’den büyük.',D='1978 koşulları sağlar ama 1798 daha küçük.',E='2698 koşulları sağlar ama binler basamağı 1 olabilirken 2 seçilmiş.'),
 tur=TT(A='dikkat',C='dikkat',D='dikkat',E='islem'))
mn=min(n for n in range(1000,10000) if fk(n) and n%2==1 and ds(n)==22); assert mn==1489
K('0052','Rakamları birbirinden farklı ve rakamlarının toplamı 22 olan dört basamaklı en küçük tek sayı kaçtır?',
 ['1489','1498','1579','1849','2389'],'A','Koşulları sağlayan en küçük tek sayı.',
 ['Binler basamağı 1 olabilir mi? Kalan üç rakamın toplamı kaç olmalı?','Yüzler basamağını olabildiğince küçük seç; kalan iki rakam en çok 9 + 8 = 17 eder.','Birler basamağı tek olmalı.'],[RAK,TC],
 [A('Binler basamağı','Binler 1 ise kalan üç farklı rakamın toplamı 21; 9 + 8 + 7 = 24 olduğundan mümkün.','binler = 1'),
  A('Yüzler basamağı','Yüzler y ise kalan iki rakam 21 − y; en çok 9 + 8 = 17. Demek ki y en az 4.','yüzler = 4'),
  A('Kalan iki rakam','Toplamları 17: yalnızca 8 ve 9. Birler tek olmalı: 9.','onlar = 8 · birler = 9'),
  A('Sayı','Rakamlar 1, 4, 8, 9 · toplam 22 ✓ · tek ✓','1489')],
 'En küçük sayıyı kurarken her basamakta “kalan rakamlar koşulu tamamlayabilir mi?” diye sor.',
 dict(B='1498 çift sayı; birler basamağı 8.',C='1579 koşulları sağlar ama 1489 daha küçük.',D='1849 koşulları sağlar ama yüzler basamağı 4 olabilirken 8 seçilmiş.',E='2389 koşulları sağlar ama binler basamağı 1 olabilir.'),
 tur=TT(B='dikkat',C='dikkat',D='islem',E='islem'))

# ===== 0053 gösterge KOLAY (K-SK-04)
assert 200+1*Fr(100,4)==225
R('0053','sk-gosterge','Sayı doğrusu ve göstergeler','kolay','Temel Kavramlar · Sayı Doğrusu','mat|Temel Kavramlar','Eşit bölmeli bir göstergede bir bölmenin değerini bulup gösterilen değeri okur.','şekilli',2,
 'K-SK-04 (eşit bölmeli gösterge) · yeni kurgu (ölçü kabı)',
 'Bir ölçü kabının üzerindeki çizelgenin bir bölümü aşağıda verilmiştir. Çizelge eşit aralıklarla bölmelenmiştir ve kırmızı ok, kaptaki suyun miktarını mililitre (mL) cinsinden göstermektedir.\nBuna göre kapta kaç mL su vardır?',
 ['210','220','225','240','250'],'C','Okun gösterdiği miktar.',
 ['100 ile 200 arasında kaç bölme var?','Bir bölme kaç mL?','Ok 200’ün kaç bölme sağında?'],[GOS],
 [A('Bir bölme','100 ile 200 arasında 4 bölme var.','(200 − 100) ÷ 4 = 25 mL'),
  A('Okun yeri','Ok 200’ün 1 bölme sağında.','200 + 25 = 225 mL',G.gosterge_iki_ibre(-1,6,{0:'100',4:'200'},{5:'?'},yay=(4,5,'1 bölme = 25 mL'))),
  A('Sonuç','Kaptaki su.','225 mL')],
 'Önce bir bölmenin değerini bul; etiket farkını bölme sayısına böl.',
 dict(A='210, bir bölmeyi 10 mL sanmak.',B='220, 100 ile 200 arasını 5 bölme saymak (bir bölme 20 mL); aradaki çizgi sayısıyla bölme sayısını karıştırmışsın.',D='240, bir bölmeyi 40 mL sanmak.',E='250, oku 2 bölme sağda okumak.'),
 tur=TT(A='islem',B='islem',D='islem',E='dikkat'),sekil=G.gosterge_iki_ibre(-1,6,{0:'100',4:'200'},{5:''}))
assert 60+3*Fr(10,5)==66
K('0053','Hasan, ibreli bir banyo tartısına çıkıyor. Tartının ölçeği eşit aralıklarla bölmelenmiştir; ölçeğin bir bölümü ve ibrenin yeri aşağıda gösterilmiştir.\nBuna göre Hasan’ın kütlesi kaç kilogramdır?',
 ['63','65','66','68','70'],'C','Okun gösterdiği kütle.',
 ['60 ile 70 arasında kaç bölme var?','Bir bölme kaç kg?','Ok 60’ın kaç bölme sağında?'],[GOS],
 [A('Bir bölme','60 ile 70 arasında 5 bölme var.','(70 − 60) ÷ 5 = 2 kg'),
  A('Okun yeri','Ok 60’ın 3 bölme sağında.','60 + 3 × 2 = 66 kg',G.gosterge_iki_ibre(-1,6,{0:'60',5:'70'},{3:'?'},yay=(0,3,'3 bölme = 6 kg'))),
  A('Sonuç','Kişinin kütlesi.','66 kg')],
 'Bir bölme = etiket farkı ÷ bölme sayısı; sonra oku etiketten itibaren say.',
 dict(A='63, bir bölmeyi 1 kg sanmak.',B='65, okun yerini iki etiketin ortası sanmak.',D='68, oku 4 bölme sağda okumak.',E='70, oku sağdaki etikette sanmak.'),
 tur=TT(A='islem',B='dikkat',D='dikkat',E='dikkat'),sekil=G.gosterge_iki_ibre(-1,6,{0:'60',5:'70'},{3:''}))

# ===== 0054 örüntü ORTA (K-SK-12)
assert (0+3*50)%8+1==7
R('0054','sk-oruntu','Örüntü ve döngü','orta','Temel Kavramlar · Örüntüler','mat|Temel Kavramlar','Döngüsel ilerlemede toplam adımı periyoda bölerek son konumu bulur.','hikâyeli',3,
 'K-SK-12 (sabit sırayla tekrar, tam tur + kalan) · yeni kurgu (çark ve ok), adım büyüklüğü 3',
 'Bir çarkın çevresine eşit aralıklarla, saat yönünde 1’den 8’e kadar sayılar yazılmıştır. Çarkın ortasındaki ok her hamlede saat yönünde 3 bölme ilerlemektedir.\nBaşlangıçta 1’i gösteren ok, 50 hamle sonra hangi sayıyı gösterir?',
 ['3','4','5','6','7'],'E','50 hamle sonra okun gösterdiği sayı.',
 ['50 hamlede ok toplam kaç bölme ilerler?','Çarkta 8 bölme var; tam turları at, kalana bak.','Kalan kadar bölme, 1’den saat yönünde say.'],[PER],
 [A('Toplam ilerleme','Her hamle 3 bölme.','50 × 3 = 150 bölme'),
  A('Tam turları at','8 bölmede bir tur tamamlanır.','150 = 8 × 18 + 6'),
  A('Son konum','1’den 6 bölme ilerle: 2, 3, 4, 5, 6, 7.','ok 7’yi gösterir')],
 'Döngüde toplam ilerlemeyi periyoda böl; kalan kadar başlangıç noktasından ilerle.',
 dict(A='3, 50’yi 8’e bölüp kalanı (2) 1’e ekleyip 3 bulmak; her hamle 3 bölme.',B='4, 50 × 3’ü 8’e bölünce kalanı 3 sanmak.',C='5, başlangıcı 0 sayıp kalan 6’dan bir eksik saymak.',D='6, kalanı cevap sanmak; ok 1’den başladığı için 1 + 6 = 7.'),
 tur=TT(A='dikkat',B='islem',C='islem',D='dikkat'))
assert (4*37)%10+1==9 and 4*37==148
K('0054','Dairesel bir oyun pistine eşit aralıklarla, saat yönünde 1’den 10’a kadar numaralı duraklar yerleştirilmiştir. Bir oyuncu her hamlede saat yönünde 4 durak ilerlemektedir.\n1 numaralı duraktan başlayan oyuncu 37 hamle sonra hangi numaralı duraktadır?',
 ['5','6','8','9','10'],'D','37 hamle sonra oyuncunun bulunduğu durak.',
 ['37 hamlede oyuncu toplam kaç durak ilerler?','Pistte 10 durak var; tam dolaşmaları at.','Kalan kadar duraktan 1 numaradan saat yönünde say.'],[PER],
 [A('Toplam ilerleme','Her hamle 4 durak.','37 × 4 = 148 durak'),
  A('Tam dolaşmaları at','10 durakta bir dolaşma tamamlanır.','148 = 10 × 14 + 8'),
  A('Son konum','1’den 8 durak ilerle.','1 + 8 = 9')],
 'Kalanı bulduktan sonra başlangıç numarasını eklemeyi unutma.',
 dict(A='5, 37’yi 10’a bölüp kalan 7 ile hesap yapmak; her hamlede 4 durak ilerleniyor.',B='6, 148’i 10’a bölünce kalanı 5 almak gibi bir işlem hatası.',C='8, kalanı cevap sanmak; oyuncu 1’den başlıyor.',E='10, 148’in 10’a tam bölündüğünü sanmak.'),
 tur=TT(A='dikkat',B='islem',C='dikkat',E='islem'))

# ===== 0055 işaret KOLAY (K-SK-28)
random=__import__('random'); random.seed(9)
for _ in range(5000):
    a_=-random.randint(1,50); b_=random.randint(1,50)
    assert a_*b_<0 and b_-a_>0 and a_*a_>0 and -a_>0
R('0055','sk-isaret','İşaret inceleme ve sıralama','kolay','Temel Kavramlar · İşaret İnceleme','mat|Temel Kavramlar','Sayı doğrusundaki konumdan sayıların işaretini belirleyip ifadelerin işaretini bulur.','düz',2,
 'K-SK-28 (işaret inceleme) · yeni veriliş (sayı doğrusundaki konum), yeni istenen (kesin negatif)',
 'Sayı doğrusunda a sayısı 0’ın solunda, b sayısı 0’ın sağındadır.\nBuna göre aşağıdakilerden hangisi kesinlikle negatiftir?',
 ['a · b','b − a','a²','b²','−a'],'A','Her durumda negatif olan ifade.',
 ['0’ın solundaki sayılar negatif mi, pozitif mi?','Zıt işaretli iki sayının çarpımının işareti nedir?','Negatif bir sayının karesi ve “−a” ne olur?'],[ISR,B('Sayı doğrusu','0’ın solundaki sayılar negatif, sağındakiler pozitiftir')],
 [A('İşaretler','a solda, b sağda.','a < 0 · b > 0'),
  A('Şıkları dene','a × b = (−) × (+) negatif ✓. b − a = pozitif − negatif, pozitif. a² ve b² pozitif. −a pozitif.','a × b < 0'),
  A('Sonuç','Yalnız çarpım negatif.','a × b < 0')],
 'Negatif bir sayının karesi pozitif, önüne eksi konunca da pozitif olur.',
 dict(B='b − a pozitif: negatif bir sayıyı çıkarmak eklemek gibidir.',C='a² pozitif: negatif × negatif = pozitif.',D='b² pozitif: sıfırdan farklı her sayının karesi pozitiftir.',E='−a pozitif: a negatif olduğundan −a pozitiftir.'),
 tur=TT(B='bilgi',C='bilgi',D='bilgi',E='bilgi'))
K('0055','Sayı doğrusunda x sayısı 0’ın sağında, y sayısı 0’ın solundadır.\nBuna göre aşağıdakilerden hangisi kesinlikle pozitiftir?',
 ['x · y','y − x','y³','x − y','x + y'],'D','Her durumda pozitif olan ifade.',
 ['x ve y’nin işaretlerini belirle.','Negatif bir sayının küpü ne işaretlidir?','Pozitiften negatif çıkarınca sonuç ne olur?'],[ISR,B('Sayı doğrusu','0’ın solundaki sayılar negatif, sağındakiler pozitiftir')],
 [A('İşaretler','x sağda, y solda.','x > 0 · y < 0'),
  A('Şıkları dene','x × y negatif. y − x negatif. y³ negatif (tek kuvvet işareti korur). x + y’nin işareti sayılara bağlı.','x − y = pozitif − negatif > 0'),
  A('Sonuç','Yalnız x − y her zaman pozitif.','x − y')],
 'Pozitiften negatif çıkarmak toplama gibidir; sonuç her zaman pozitif.',
 dict(A='x · y negatif: zıt işaretli sayıların çarpımı.',B='y − x negatif: negatiften pozitif çıkarınca sonuç küçülür.',C='y³ negatif: tek kuvvet işareti korur.',E='x + y’nin işareti belli değil: x = 5, y = −2 için pozitif, x = 1, y = −4 için negatif.'),
 tur=TT(A='bilgi',B='islem',C='bilgi',E='dikkat'))

json.dump(ANA,open(os.path.join(H,'sayi-kumeleri-parti5.json'),'w'),ensure_ascii=False,indent=1)
json.dump(KAR,open(os.path.join(H,'sayi-kumeleri-kardes5.json'),'w'),ensure_ascii=False,indent=1)
from collections import Counter
print(len(ANA),len(KAR),Counter(q['cevap']['sik'] for q in ANA+KAR))
