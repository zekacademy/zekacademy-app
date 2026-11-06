"""Parti 3: boş tip × zorluk hücreleri (0027–0039) ve kardeşleri (0027k–0039k). Her cevap kodla doğrulanır.
Zor: tek-çift, tanımlı, ardışık, kesir, ondalık, gösterge, faktöriyel, asal, işaret. Kolay: tanımlı, yerleştirme, örüntü, rakam en az–en çok."""
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
def R(no,tipId,tip,zorluk,konu,k,kazanim,kalip,adim,kart,metin,siklar,sik,istenen,ipuclari,bilgi,adimlar,puf,cel,kisa=None,sekil=None):
    S=dict(zip('ABCDE',siklar))
    ANA.append(dict(id='tytmat-sayilar-'+no,ders='TYT Matematik',konu=konu,k=k,kazanim=kazanim,tipId=tipId,tip=tip,zorluk=zorluk,seviye='ÖSYM',kalip=kalip,adimSayisi=adim,
      metin=metin,sekil=sekil,siklar=S,cevap=dict(sik=sik,deger=S[sik]),celdiriciler=cel,istenen=istenen,bilgi=bilgi,ipuclari=ipuclari,adimlar=adimlar,puf=puf,kisaYol=kisa,
      kardes='tytmat-sayilar-'+no+'k',kaynakKart=kart,dogrulama=dict(yontem2=True,tarama=True,korCozum=True)))
def K(no,metin,siklar,sik,istenen,ipuclari,bilgi,adimlar,puf,cel,kisa=None,sekil=None):
    a=[x for x in ANA if x['id']=='tytmat-sayilar-'+no][0]; S=dict(zip('ABCDE',siklar))
    KAR.append(dict(id=a['id']+'k',ana=a['id'],ders=a['ders'],konu=a['konu'],k=a['k'],kazanim=a['kazanim'],tipId=a['tipId'],tip=a['tip'],zorluk=a['zorluk'],seviye='ÖSYM',kalip=a['kalip'],
      adimSayisi=a['adimSayisi'],metin=metin,sekil=sekil,siklar=S,cevap=dict(sik=sik,deger=S[sik]),celdiriciler=cel,istenen=istenen,bilgi=bilgi,ipuclari=ipuclari,adimlar=adimlar,puf=puf,kisaYol=kisa,
      kaynakKart=a['kaynakKart'].split(' · ')[0]+' · kardeş ('+no+'): aynı tip ve zorluk, yeni kurgu ve sayılar',dogrulama=dict(yontem2=True,tarama=True,korCozum=True)))
ds=lambda n:sum(map(int,str(n)))
def dp(n):
    r=1
    for c in str(n): r*=int(c)
    return r
def oncul(vals,I,II,III):
    """vals: olası durumlar; I/II/III: durum→bool. Kesin doğru olanların kümesi."""
    return {ad for ad,f in (('I',I),('II',II),('III',III)) if all(f(*v) for v in vals)}

# ===== 0027 tek-çift ZOR (K-SK-02)
v=[(a,b,c) for a,b,c in product(range(1,9),repeat=3) if (a*a+b*c)%2==1 and ((a+b)*c)%2==0]
assert {a%2 for a,b,c in v}=={1} and {c%2 for a,b,c in v}=={0} and {b%2 for a,b,c in v}=={0,1}
assert oncul(v,lambda a,b,c:(a+c)%2==1,lambda a,b,c:(b*c)%2==0,lambda a,b,c:(a+b)%2==0)=={'I','II'}
R('0027','sk-tek-cift','Tek ve çift sayılar','zor','Temel Kavramlar · Tek ve Çift Sayılar','mat|Temel Kavramlar','Tek-çift kurallarıyla harflerin tek ya da çift olduğunu bulur; kesin doğru ifadeleri belirler.','öncüllü',4,
 'K-SK-02 (tek-çift koşulları, kesin doğru) · yeni ifadeler (kare ve parantezli çarpım), yeni öncüller',
 'Pozitif a, b ve c tam sayıları için a² + b · c toplamı tek, (a + b) · c çarpımı ise çifttir.\nBuna göre\nI. a + c tektir.\nII. b · c çifttir.\nIII. a + b çifttir.\nifadelerinden hangileri kesinlikle doğrudur?',
 ['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III'],'C','Her durumda doğru kalan ifadeler.',
 ['İkinci koşulda (a + b) · c çift; c tek olsaydı ne olurdu?','c’nin tek mi çift mi olduğunu bulunca birinci koşula dön: b · c ne olur?','b hakkında bir şey söyleyebiliyor musun? III. ifadeyi b tek ve b çift için ayrı dene.'],[TEK,CARP],
 [A('c’yi incele','(a + b) · c çarpımının çift olması için ya c çift ya da a + b çift olmalı. Önce c tek olsaydı ne olacağına bakalım.','c tek mi, c çift mi?'),
  A('c tek olsaydı','a² + b · c tek ve (a + b) çift olmalı. a ile b aynı türdendir. İkisi de tekse a² + b · c = tek + tek = çift; ikisi de çiftse çift + çift = çift. Tek olamaz.','c tek ⇒ çelişki · c çift'),
  A('a’yı bul','c çift olduğundan b · c çift. a² + çift = tek olması için a² tek, yani **a tek** olmalı.','b × c çift · a² + çift = tek ⇒ a tek'),
  A('b serbest','b tek de olabilir çift de: (a + b) · c, c çift olduğu için her durumda çift çıkar.','b tek ya da çift olabilir'),
  A('Öncülleri dene','I. tek + çift = tek ✓. II. c çift olduğu için b · c çift ✓. III. a tek; b tekse a + b çift, b çiftse tek olur ✗.','Doğru: I ve II')],
 'Tek-çift sorularında önce “çarpım çift” koşulundan bir harfi sabitle; diğer koşul geri kalanları belirler. Serbest kalan harf, öncüllerde karşı örnek üretir.',
 dict(A='II de her durumda doğru: c çift olduğu için b · c çifttir.',B='I de doğru: a tek, c çift olduğundan a + c tektir.',D='III kesin değil: a = 1, b = 2, c = 2 için a + b = 3 tek olur.',E='III kesin değil: b çift seçilirse a + b tek olur.'),
 kisa='Tek yerine 1, çift yerine 2 koyarak dene: a = 1, c = 2 koşulları sağlar; b = 1 ve b = 2 ikisi de olur. Öncüllerde iki durumu da dene: I ve II ikisinde de doğru, III birinde yanlış.')
v=[(a,b,c) for a,b,c in product(range(1,9),repeat=3) if (a*c+b)%2==1 and ((a+b)*c)%2==0]
assert {b%2 for a,b,c in v}=={1} and {c%2 for a,b,c in v}=={0} and {a%2 for a,b,c in v}=={0,1}
assert oncul(v,lambda a,b,c:(b+c)%2==1,lambda a,b,c:(a+b)%2==1,lambda a,b,c:((a+c)*c)%2==0)=={'I','III'}
K('0027','Pozitif x, y ve z tam sayıları için x · z + y toplamı tek, (x + y) · z çarpımı ise çifttir.\nBuna göre\nI. y + z tektir.\nII. x + y tektir.\nIII. (x + z) · z çifttir.\nifadelerinden hangileri kesinlikle doğrudur?',
 ['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III'],'E','Her durumda doğru kalan ifadeler.',
 ['z tek olsaydı iki koşul birlikte sağlanabilir miydi?','z’nin türünü bulunca x · z’nin tek mi çift mi olduğuna bak.','x hakkında kesin bir şey söylenebiliyor mu? II. ifadeyi x tek ve x çift için dene.'],[TEK,CARP],
 [A('z tek olsaydı','(x + y) · z çift olması için x + y çift olmalı; x ile y aynı türden. İkisi tekse x · z + y = tek + tek = çift; ikisi çiftse çift + çift = çift. Tek çıkmaz.','z tek ⇒ çelişki'),
  A('z çift','Demek ki **z çift**. O zaman x · z de çift.','z çift ⇒ x × z çift'),
  A('y’yi bul','x · z + y tek olmalı: çift + y = tek ise **y tek**.','çift + y = tek ⇒ y tek'),
  A('x serbest','z çift olduğu için (x + y) · z her durumda çift; x tek de çift de olabilir.','x tek ya da çift'),
  A('Öncülleri dene','I. tek + çift = tek ✓. II. x tekse x + y çift olur ✗. III. z çift olduğu için çarpım çift ✓.','Doğru: I ve III')],
 'Bir çarpanı çift olan çarpım her zaman çifttir; bu yüzden “… · z çift” koşulu çoğu zaman z’yi sabitler.',
 dict(A='III de her durumda doğru: z çift olduğu için (x + z) · z çifttir.',B='II kesin değil: x = 1, y = 1, z = 2 için x + y = 2 çift olur.',C='I de doğru: y tek, z çift olduğundan y + z tektir.',D='II kesin değil; x tek seçilirse x + y çift olur.'),
 kisa='Tek yerine 1, çift yerine 2 koy: y = 1, z = 2 koşulları sağlar; x = 1 ve x = 2 ikisi de olur. İki durumda da doğru kalan öncüller I ve III.')

# ===== 0028 tanımlı ZOR (K-SK-01)
v=[n for n in range(10,100) if n==2*ds(n)+dp(n)]; assert v==[14,36,77] and sum(v)==127
R('0028','sk-tanimli','Tanımlı sayılar ve semboller','zor','Temel Kavramlar · Rakam ve Sayı','mat|Temel Kavramlar','Rakamlar arasında tanımlanan bir ilişkiyi basamak çözümlemesiyle denkleme çevirir ve tüm çözümleri bulur.','düz',5,
 'K-SK-01 (rakamlarla tanımlanan sayı türü) · yeni tanım (2 × rakamlar toplamı + rakamlar çarpımı), yeni istenen (sayıların toplamı)',
 'A ve B birer rakam olmak üzere, iki basamaklı AB sayısının “ağırlığı”\n2 · (A + B) + A · B\nişleminin sonucu olarak tanımlanıyor.\nAğırlığı kendisine eşit olan iki basamaklı sayıların toplamı kaçtır?',
 ['14','77','91','113','127'],'E','Ağırlığı kendine eşit olan tüm iki basamaklı sayıların toplamı.',
 ['AB sayısını 10 × A + B diye yaz ve tanımla eşitle.','B’leri bir tarafta toplayıp B’yi A cinsinden yaz.','A’ya 1’den 9’a değer ver; B’nin bir rakam çıktığı durumları seç.'],[IKI],
 [A('Denklemi kur','AB sayısının değeri 10A + B; ağırlığı 2A + 2B + AB. İkisini eşitle.','10A + B = 2A + 2B + A × B'),
  A('Sadeleştir','İki taraftan 2A ve B çıkar.','8A = B + A × B = B × (A + 1)'),
  A('B’yi yalnız bırak','İki tarafı (A + 1)’e böl.','B = 8A ÷ (A + 1)'),
  A('A’yı dene','B bir rakam (0–9) olmalı. A = 1 ⇒ B = 4 · A = 3 ⇒ B = 6 · A = 7 ⇒ B = 7. Diğer A değerlerinde B tam sayı çıkmaz.','14 · 36 · 77'),
  A('Kontrol et ve topla','14: 2 × 5 + 4 = 14 ✓ · 36: 2 × 9 + 18 = 36 ✓ · 77: 2 × 14 + 49 = 77 ✓','14 + 36 + 77 = 127')],
 'Rakamlarla kurulan denklemde bir harfi yalnız bırak; diğer harfe 1’den 9’a değer ver ve yalnızca rakam çıkan durumları al.',
 dict(A='14 yalnızca ilk bulunan sayı; 36 ve 77 de koşulu sağlıyor.',B='77 yalnızca en büyük sayı; soru hepsinin toplamını soruyor.',C='91 = 14 + 77; 36’yı (A = 3, B = 6) atlamışsın.',D='113 = 36 + 77; 14’ü (A = 1, B = 4) atlamışsın.'),
 kisa='B = 8A ÷ (A + 1) tam sayı olmalı. A ile A + 1’in ortak böleni olmadığından A + 1, 8’i bölmeli: A + 1 = 2, 4 ya da 8 ⇒ A = 1, 3, 7. Tek tek denemeye gerek kalmaz.')
v=[n for n in range(10,100) if n==ds(n)+dp(n)+4]; assert v==[15,27,48] and sum(v)==90
K('0028','K ve L birer rakam olmak üzere, iki basamaklı KL sayısının “gücü”\nK + L + K · L + 4\nişleminin sonucu olarak tanımlanıyor.\nGücü kendisine eşit olan iki basamaklı sayıların toplamı kaçtır?',
 ['15','48','63','75','90'],'E','Gücü kendisine eşit olan tüm iki basamaklı sayıların toplamı.',
 ['KL sayısını 10 × K + L diye yaz ve tanımla eşitle.','Sadeleştirince K ortak çarpan olarak dışarı alınabiliyor mu?','Çarpımı 4 olan rakam ikililerini düşün.'],[B('İki basamaklı sayı','KL = 10 × K + L (K onlar, L birler basamağı). Örnek: 74 = 10 × 7 + 4')],
 [A('Denklemi kur','KL sayısının değeri 10K + L; gücü K + L + K · L + 4.','10K + L = K + L + K × L + 4'),
  A('Sadeleştir','İki taraftan K ve L çıkar.','9K = K × L + 4 · 9K − K × L = 4'),
  A('K’yi dışarı al','Sol taraftaki iki terimde de K var.','K × (9 − L) = 4'),
  A('Çarpımı 4 olanlar','K ve (9 − L) sayma sayısı; çarpımları 4: 1 × 4, 2 × 2, 4 × 1.','K = 1, L = 5 · K = 2, L = 7 · K = 4, L = 8'),
  A('Kontrol et ve topla','15: 1 + 5 + 5 + 4 = 15 ✓ · 27: 2 + 7 + 14 + 4 = 27 ✓ · 48: 4 + 8 + 32 + 4 = 48 ✓','15 + 27 + 48 = 90')],
 'Denklemi “harf × (…) = sayı” biçimine getir; sayının çarpanlarını listelemek tüm çözümleri verir.',
 dict(A='15 yalnızca en küçük sayı; 27 ve 48 de koşulu sağlıyor.',B='48 yalnızca en büyük sayı; soru hepsinin toplamını soruyor.',C='63 = 15 + 48; 2 × 2 durumunu (27) atlamışsın.',D='75 = 27 + 48; 1 × 4 durumunu (15) atlamışsın.'))

# ===== 0029 ardışık ZOR (K-SK-08)
def a29(k):
    return [(x,y) for x in range(2,200,2) for y in range(1,200,2) if 5*x+20==4*y+12 and 5*x+20>100]
v=a29(0); x,y=v[0]; assert (x,y)==(20,27) and x+8==28 and sum(range(20,30,2))==sum(range(27,35,2))==120
R('0029','sk-ardisik','Ardışık sayılar','zor','Temel Kavramlar · Ardışık Sayılar','mat|Temel Kavramlar','Ardışık tek ve çift sayıların toplamlarını eşitleyerek tek-çift ve eşitsizlik koşullarıyla en küçük değeri bulur.','düz',5,
 'K-SK-08 (ardışık tek/çift toplamı eşitleme) · yeni kurgu (iki ayrı ardışık grup), yeni koşul (toplam 100’den büyük), yeni istenen (en az değer)',
 'Ardışık 5 çift sayının toplamı, ardışık 4 tek sayının toplamına eşittir.\nBu toplam 100’den büyük olduğuna göre çift sayıların en büyüğü en az kaçtır?',
 ['24','26','28','32','36'],'C','Koşulları sağlayan durumlarda en büyük çift sayının en küçük değeri.',
 ['Çift sayıların en küçüğüne x, tek sayıların en küçüğüne y de; iki toplamı yaz.','Eşitlikten y’yi x cinsinden yaz; y’nin tek olması x için ne gerektiriyor?','Toplam 100’den büyük olsun; x’in alabileceği en küçük değeri bul.'],[ARD],
 [A('Toplamları yaz','Çiftler: x, x + 2, x + 4, x + 6, x + 8. Tekler: y, y + 2, y + 4, y + 6.','5x + 20 = 4y + 12'),
  A('y’yi yalnız bırak','İki taraftan 12 çıkar.','4y = 5x + 8'),
  A('Hangi x’ler olur?','4y, 4’ün katı; 5x + 8’in 4’e bölünmesi için x 4’ün katı olmalı. x = 4k ise y = 5k + 2. y’nin **tek** olması için k tek olmalı.','x = 4k · y = 5k + 2 · k tek'),
  A('Toplam 100’den büyük','Toplam 5x + 20 = 20k + 20 > 100 ⇒ k > 4. En küçük tek k = 5.','k = 5 ⇒ x = 20, y = 27'),
  A('Kontrol','20 + 22 + 24 + 26 + 28 = 120 · 27 + 29 + 31 + 33 = 120 ✓','çiftlerin en büyüğü = 28')],
 'Ardışık sayı sorularında en küçük terime harf ver; denklemi kurduktan sonra harfin tek mi çift mi olması gerektiğini mutlaka kontrol et.',
 dict(A='24 için x = 16 olur; o zaman y = 22 çift çıkar, tek sayı olamaz.',B='26 için x = 18; 4y = 98 olur, y tam sayı değil.',D='32 için x = 24; y = 32 çift çıkar, tek sayı olamaz.',E='36 koşulları sağlar (x = 28, y = 37) ama daha küçüğü (28) var; soru en azını soruyor.'))
v=[(x,y) for x in range(2,400,2) for y in range(1,400,2) if 3*x+6==4*y+12 and 3*x+6>150]; x,y=v[0]
assert (x,y)==(54,39) and sum([54,56,58])==sum([39,41,43,45])==168
K('0029','Ardışık 3 çift sayının toplamı, ardışık 4 tek sayının toplamına eşittir.\nBu toplam 150’den büyük olduğuna göre tek sayıların en küçüğü en az kaçtır?',
 ['33','39','45','54','58'],'B','Koşulları sağlayan durumlarda en küçük tek sayının en küçük değeri.',
 ['Çiftlerin en küçüğüne x, teklerin en küçüğüne y de; iki toplamı yaz.','x’i y cinsinden yaz; x’in çift olması y için ne gerektiriyor?','Toplam 150’den büyük olsun; y’nin en küçük değerini bul.'],[ARD],
 [A('Toplamları yaz','Çiftler: x, x + 2, x + 4. Tekler: y, y + 2, y + 4, y + 6.','3x + 6 = 4y + 12'),
  A('x’i yalnız bırak','İki taraftan 6 çıkar.','3x = 4y + 6'),
  A('Hangi y’ler olur?','4y + 6’nın 3’e bölünmesi için y, 3’ün katı olmalı; y tek olduğundan y = 3, 9, 15, … (3’ün tek katları). Bu durumda x = (4y + 6) ÷ 3 çift çıkar.','y = 3’ün tek katı'),
  A('Toplam 150’den büyük','Toplam 4y + 12 > 150 ⇒ y > 34,5. 3’ün 34,5’ten büyük en küçük tek katı 39.','y = 39 ⇒ x = 54'),
  A('Kontrol','54 + 56 + 58 = 168 · 39 + 41 + 43 + 45 = 168 ✓','teklerin en küçüğü = 39')],
 'Eşitlikteki tam bölünme ve tek-çift şartlarını birlikte yaz; sonra sınır koşuluyla en küçük değeri seç.',
 dict(A='33 için toplam 4 × 33 + 12 = 144; 150’den büyük değil.',C='45, y = 39 iken tek sayıların en büyüğü; soru en küçüğünü soruyor.',D='54, çift sayıların en küçüğü; soru tek sayıları soruyor.',E='58, çift sayıların en büyüğü; soru tek sayıların en küçüğünü soruyor.'))

# ===== 0030 kesir ZOR (K-SK-09)
def yanlis(x,es):
    return sum(not f(x) for f in es)
es=[lambda x:x>Fr(2,3),lambda x:x<Fr(3,4),lambda x:x>Fr(5,7),lambda x:x<Fr(7,10)]
opt=[Fr(3,5),Fr(17,25),Fr(7,10),Fr(71,100),Fr(4,5)]
assert [yanlis(x,es) for x in opt]==[2,1,2,2,2]
R('0030','sk-kesir','Kesirler ve rasyonel sayılar','zor','Temel Kavramlar · Rasyonel Sayılar','mat|Rasyonel Sayılar','Kesirleri sıralayarak sayı doğrusunu bölgelere ayırır; verilen doğruluk bilgisine uyan sayıyı seçer.','öncüllü',4,
 'K-SK-09 (kesir eşikleri, doğru/yanlış sayısı) · yeni eşikler, yeni koşul (yalnızca biri yanlış), yeni şıklar',
 'x bir rasyonel sayıdır. x ile ilgili aşağıdaki dört bilgiden yalnızca biri yanlıştır.\nI. x > 2/3\nII. x < 3/4\nIII. x > 5/7\nIV. x < 7/10\nBuna göre x aşağıdakilerden hangisi olabilir?',
 ['3/5','17/25','7/10','71/100','4/5'],'B','Dört bilgiden tam olarak birini yanlış yapan sayı.',
 ['Dört kesri ondalığa çevirip küçükten büyüğe sırala.','Sayı doğrusunu bu dört noktayla bölgelere ayır; her bölgede kaç bilgi yanlış, say.','Şıkları ondalığa çevir; hangi bölgeye düştüklerine bak.'],[KES],
 [A('Kesirleri sırala','Ondalığa çevir.','2/3 ≈ 0,667 · 7/10 = 0,7 · 5/7 ≈ 0,714 · 3/4 = 0,75'),
  A('Bölgeler','Bu dört nokta sayı doğrusunu beş bölgeye ayırır. Her bölgede yanlış olan bilgileri say.','x < 0,667: I ve III yanlış (2) · 0,667–0,7: yalnız III yanlış (1)'),
  A('Diğer bölgeler','Kalan bölgeleri de say.','0,7–0,714: III ve IV yanlış (2) · 0,714–0,75: yalnız IV yanlış (1) · x > 0,75: II ve IV yanlış (2)'),
  A('Şıkları yerleştir','Şıkları ondalığa çevir.','0,6 · 0,68 · 0,7 · 0,71 · 0,8'),
  A('Seç','Yalnızca 0,68, tek bilginin yanlış olduğu bir bölgede (0,667 ile 0,7 arası).','x = 17/25')],
 '“Kaç tanesi doğru/yanlış” sorularında eşikleri sıralayıp her aralıkta sayım yap; sınır değerlerde eşitsizliğin < mi > mi olduğuna dikkat et.',
 dict(A='3/5 = 0,6; 2/3’ten küçük olduğu için I ve III ikisi birden yanlış olur.',C='7/10 tam sınırda: x < 7/10 sağlanmaz ve x > 5/7 de sağlanmaz; iki bilgi yanlış olur.',D='71/100 = 0,71; 0,7 ile 0,714 arasında, III ve IV ikisi de yanlış.',E='4/5 = 0,8; 3/4’ten büyük, II ve IV ikisi de yanlış.'))
es=[lambda x:x>Fr(3,5),lambda x:x<Fr(5,8),lambda x:x>Fr(4,7),lambda x:x<Fr(2,3)]
opt=[Fr(11,20),Fr(61,100),Fr(13,20),Fr(7,10),Fr(3,4)]
assert [yanlis(x,es) for x in opt]==[2,0,1,2,2]
K('0030','y bir rasyonel sayıdır. y ile ilgili aşağıdaki dört bilgiden yalnızca biri yanlıştır.\nI. y > 3/5\nII. y < 5/8\nIII. y > 4/7\nIV. y < 2/3\nBuna göre y aşağıdakilerden hangisi olabilir?',
 ['11/20','61/100','13/20','7/10','3/4'],'C','Dört bilgiden tam olarak birini yanlış yapan sayı.',
 ['Dört kesri ondalığa çevirip sırala.','Her bölgede kaç bilginin yanlış olduğunu say; hiç yanlışın olmadığı bölge de olabilir.','Şıkları ondalığa çevirip bölgelere yerleştir.'],[B('Kesirleri karşılaştırma','kesri ondalığa çevir (pay ÷ payda). Örnek: 3/5 = 0,6 · 5/8 = 0,625 · 13/20 = 0,65')],
 [A('Kesirleri sırala','Ondalığa çevir.','4/7 ≈ 0,571 · 3/5 = 0,6 · 5/8 = 0,625 · 2/3 ≈ 0,667'),
  A('Bölgeler','Her bölgede yanlış bilgileri say.','y < 0,571: I ve III (2) · 0,571–0,6: yalnız I (1) · 0,6–0,625: hiçbiri (0)'),
  A('Diğer bölgeler','Kalan bölgeleri de say.','0,625–0,667: yalnız II (1) · y > 0,667: II ve IV (2)'),
  A('Şıkları yerleştir','Şıkları ondalığa çevir.','0,55 · 0,61 · 0,65 · 0,7 · 0,75'),
  A('Seç','Tek bilginin yanlış olduğu bölgeye düşen yalnızca 0,65.','y = 13/20')],
 'Hiç yanlışın olmadığı bölge de tuzaktır: “yalnızca biri yanlış” koşulu, hepsinin doğru olduğu aralığı da eler.',
 dict(A='11/20 = 0,55; 4/7’den küçük, I ve III ikisi birden yanlış.',B='61/100 = 0,61; dört bilginin dördü de doğru, yanlış bilgi kalmaz.',D='7/10 = 0,7; 2/3’ten büyük, II ve IV ikisi de yanlış.',E='3/4 = 0,75; II ve IV ikisi de yanlış.'))

# ===== 0031 ondalık ZOR (K-SK-03)
def parcalar(L,d1,d2):
    L,d1,d2=Fr(L),Fr(d1),Fr(d2); m=sorted({d1*i for i in range(1,int(L/d1))}|{d2*i for i in range(1,int(L/d2))}|{Fr(0),L})
    return [c-a for a,c in zip(m,m[1:])], len(m)-2
p,isr=parcalar('2.4','0.3','0.4'); assert sum(1 for x in p if x<Fr(15,100))==4 and len(p)==12 and isr==11 and sum(1 for x in p if x<Fr(1,4))==8
R('0031','sk-ondalik','Ondalık sayılar ve günlük hesap','zor','Temel Kavramlar · Ondalık Sayılar','mat|Rasyonel Sayılar','Ondalık aralıklarla yapılan iki işaretlemeyi birleştirerek oluşan parçaların uzunluklarını bulur.','hikâyeli',4,
 'K-SK-03 (bir uzunluğu iki farklı aralıkla bölme) · yeni kurgu (çıta kesme), yeni istenen (parça uzunlukları ve birim dönüşümü)',
 '2,4 metre uzunluğundaki bir çıtanın üzerine Ali, sol uçtan başlayarak her 0,3 metrede bir; Ayşe de yine sol uçtan başlayarak her 0,4 metrede bir işaret koyuyor. Çıtanın uçlarına işaret konmuyor.\nDaha sonra çıta, üzerindeki bütün işaretlerden kesilerek parçalara ayrılıyor. Aynı noktaya gelen iki işaret tek bir kesim sayılır.\nBuna göre elde edilen parçalardan kaç tanesinin uzunluğu 15 santimetreden kısadır?',
 ['4','7','8','11','12'],'A','Uzunluğu 15 cm’den kısa olan parçaların sayısı.',
 ['Ali’nin ve Ayşe’nin işaretlerinin sol uca uzaklıklarını ayrı ayrı yaz.','İki listeyi birleştirip küçükten büyüğe sırala; iki kez yazılan noktaya dikkat et.','Ardışık iki işaret arasındaki farklar parça uzunluklarıdır; 15 cm = 0,15 m.'],[CM],
 [A('Ali’nin işaretleri','0,3’ün katları; 2,4’e kadar (uç hariç).','0,3; 0,6; 0,9; 1,2; 1,5; 1,8; 2,1'),
  A('Ayşe’nin işaretleri','0,4’ün katları; 2,4’e kadar (uç hariç).','0,4; 0,8; 1,2; 1,6; 2,0'),
  A('Birleştir','1,2’de iki işaret çakışır; orada tek kesim olur. Sıralı noktalar (uçlarla birlikte):','0; 0,3; 0,4; 0,6; 0,8; 0,9; 1,2; 1,5; 1,6; 1,8; 2,0; 2,1; 2,4'),
  A('Parçalar','Ardışık noktaların farkları:','0,3; 0,1; 0,2; 0,2; 0,1; 0,3; 0,3; 0,1; 0,2; 0,2; 0,1; 0,3',G.cita_isaret('2.4','0.3','0.4','Ali (0,3 m)','Ayşe (0,4 m)','0.1')),
  A('15 cm’den kısa','0,15 m’den kısa olan yalnızca 0,1 m = 10 cm’lik parçalar.','0,1 m’lik parça sayısı = 4')],
 'İki farklı aralıkla işaretlemede çakışan noktaları bir kez say; parçaları bulmak için tüm noktaları tek listede sırala.',
 dict(B='7, Ali’nin koyduğu işaret sayısı; soru parça uzunluklarını soruyor.',C='8, 0,2 m’lik parçaları da saymışsın; 20 cm, 15 cm’den kısa değil.',D='11, kesim yapılan nokta sayısı; parça uzunluklarına bakmalısın.',E='12, toplam parça sayısı; hepsi 15 cm’den kısa değil.'))
p,isr=parcalar('1.8','0.2','0.3'); assert sum(1 for x in p if x>Fr(15,100))==6 and len(p)==12 and isr==11
K('0031','1,8 metre uzunluğundaki bir kurdelenin üzerine Selin, sol uçtan başlayarak her 0,2 metrede bir; Kerem de yine sol uçtan başlayarak her 0,3 metrede bir iğne batırıyor. Kurdelenin uçlarına iğne batırılmıyor.\nDaha sonra kurdele, iğne batırılan bütün noktalardan kesiliyor. Aynı noktaya gelen iki iğne tek bir kesim sayılır.\nBuna göre elde edilen parçalardan kaç tanesinin uzunluğu 15 santimetreden uzundur?',
 ['6','8','11','12','13'],'A','Uzunluğu 15 cm’den uzun olan parçaların sayısı.',
 ['Selin’in ve Kerem’in noktalarının sol uca uzaklıklarını yaz.','İki listeyi birleştir; aynı noktaya gelenleri bir kez yaz.','Ardışık noktaların farkları parça uzunluklarıdır; 15 cm = 0,15 m.'],[CM],
 [A('Selin’in noktaları','0,2’nin katları (uç hariç).','0,2; 0,4; 0,6; 0,8; 1,0; 1,2; 1,4; 1,6'),
  A('Kerem’in noktaları','0,3’ün katları (uç hariç).','0,3; 0,6; 0,9; 1,2; 1,5'),
  A('Birleştir','0,6 ve 1,2 iki listede de var; oralarda tek kesim olur.','0; 0,2; 0,3; 0,4; 0,6; 0,8; 0,9; 1,0; 1,2; 1,4; 1,5; 1,6; 1,8'),
  A('Parçalar','Ardışık noktaların farkları:','0,2; 0,1; 0,1; 0,2; 0,2; 0,1; 0,1; 0,2; 0,2; 0,1; 0,1; 0,2',G.cita_isaret('1.8','0.2','0.3','Selin (0,2 m)','Kerem (0,3 m)','0.2')),
  A('15 cm’den uzun','0,15 m’den uzun olanlar 0,2 m = 20 cm’lik parçalar.','0,2 m’lik parça sayısı = 6')],
 'Çakışan noktaları bir kez say; parça uzunlukları ardışık noktaların farkıdır.',
 dict(B='8, Selin’in batırdığı iğne sayısı; soru parça uzunluklarını soruyor.',C='11, kesim noktası sayısı (8 + 5 − 2); parçaların uzunluğuna bakmalısın.',D='12, toplam parça sayısı; yarısı 10 cm.',E='13, çakışan iki noktayı iki kez sayınca bulunan kesim sayısı.'))

# ===== 0032 gösterge ZOR (K-SK-04)
bol=Fr(1,2)/6; s=Fr(1,4)-2*bol; a=Fr(3,4)+bol; assert (a-s)*60==45 and s>0 and a<1
sek=G.gosterge_iki_ibre(-2,7,{0:'1/4',6:'3/4'},{-2:'S',7:'A'},alt='S: sabahki konum · A: benzin alındıktan sonraki konum')
R('0032','sk-gosterge','Sayı doğrusu ve göstergeler','zor','Temel Kavramlar · Sayı Doğrusu','mat|Temel Kavramlar','Kesirle etiketlenmiş eşit bölmeli bir göstergede iki konumu okuyarak aradaki miktarı hesaplar.','şekilli',4,
 'K-SK-04 (eşit bölmeli gösterge) · yeni kurgu (yakıt deposu), kesirli etiketler, iki ibre ve miktar hesabı',
 'Bir aracın yakıt göstergesinin bir bölümü aşağıda verilmiştir. Gösterge eşit aralıklarla bölmelenmiştir ve ibrenin gösterdiği değer deponun ne kadarının dolu olduğunu belirtmektedir.\nSabah S konumunda olan ibre, araca benzin alındıktan sonra A konumuna gelmiştir. Bu sürede araç yakıt harcamamıştır.\nDeponun tamamı 60 litre olduğuna göre araca kaç litre benzin alınmıştır?',
 ['25','30','35','45','50'],'D','S ile A konumları arasındaki farkın litre karşılığı.',
 ['1/4 ile 3/4 arasındaki farkı ve aradaki bölme sayısını bul.','Bir bölmenin deponun kaçta kaçı olduğunu hesapla.','S’nin ve A’nın değerlerini bul; farkı 60 ile çarp.'],[GOS],
 [A('Bir bölme','1/4 ile 3/4 arasında 6 bölme var; fark 3/4 − 1/4 = 1/2.','1/2 ÷ 6 = 1/12'),
  A('S konumu','S, 1/4’ün 2 bölme solunda.','1/4 − 2/12 = 3/12 − 2/12 = 1/12'),
  A('A konumu','A, 3/4’ün 1 bölme sağında.','3/4 + 1/12 = 9/12 + 1/12 = 10/12'),
  A('Fark','Alınan benzin deponun 10/12 − 1/12 = 9/12’si.','9/12 = 3/4',G.gosterge_iki_ibre(-2,7,{0:'1/4',6:'3/4'},{-2:'S',7:'A'},yay=(-2,7,'9 bölme = 9/12'))),
  A('Litreye çevir','Deponun tamamı 60 L.','60 × 3/4 = 45 L')],
 'Kesirli göstergede önce bir bölmenin değerini bul; konumlar etiketlerden bölme ekleyip çıkararak okunur.',
 dict(A='25 L, S’yi 1/4’ün sağına (5/12) koyunca çıkıyor; S etiketin solunda.',B='30 L, yalnızca etiketler arasındaki farkı (1/2) almak; ibreler etiketlerde değil.',C='35 L, A’yı 3/4’ün soluna (8/12) koyunca çıkıyor; A etiketin sağında.',E='50 L, A’daki toplam benzin (10/12 × 60); sabah depoda zaten 5 L vardı.'),
 kisa='Bir bölme 60 × 1/12 = 5 L. S’den A’ya 2 + 6 + 1 = 9 bölme var: 9 × 5 = 45 L. Kesirlerle uğraşmadan bölme say.',sekil=sek)
bol=Fr(3,5)/9; s=Fr(4,5)+2*bol; a=Fr(1,5)-bol; assert (s-a)*90==72 and a>0 and s<1
sek=G.gosterge_iki_ibre(-1,11,{0:'1/5',9:'4/5'},{11:'S',-1:'A'},alt='S: sabahki konum · A: akşamki konum')
K('0032','Bir su deposunun seviye göstergesinin bir bölümü aşağıda verilmiştir. Gösterge eşit aralıklarla bölmelenmiştir ve ibrenin gösterdiği değer deponun ne kadarının dolu olduğunu belirtmektedir.\nSabah ibre S konumundayken, gün içinde depodan su kullanılmış ve akşam ibre A konumuna gelmiştir. Gün içinde depoya su eklenmemiştir.\nDeponun tamamı 90 litre olduğuna göre gün içinde kaç litre su kullanılmıştır?',
 ['54','60','72','84','90'],'C','S ile A konumları arasındaki farkın litre karşılığı.',
 ['1/5 ile 4/5 arasındaki farkı ve aradaki bölme sayısını bul.','Bir bölmenin deponun kaçta kaçı olduğunu hesapla.','S’nin ve A’nın değerlerini bul; farkı 90 ile çarp.'],[GOS],
 [A('Bir bölme','1/5 ile 4/5 arasında 9 bölme var; fark 3/5.','3/5 ÷ 9 = 1/15'),
  A('S konumu','S, 4/5’in 2 bölme sağında.','4/5 + 2/15 = 12/15 + 2/15 = 14/15'),
  A('A konumu','A, 1/5’in 1 bölme solunda.','1/5 − 1/15 = 3/15 − 1/15 = 2/15'),
  A('Fark','Kullanılan su deponun 14/15 − 2/15 = 12/15’i.','12/15 = 4/5',G.gosterge_iki_ibre(-1,11,{0:'1/5',9:'4/5'},{11:'S',-1:'A'},yay=(-1,11,'12 bölme = 12/15'))),
  A('Litreye çevir','Deponun tamamı 90 L.','90 × 4/5 = 72 L')],
 'Önce bir bölmenin değerini bul; ibre etiketin sağındaysa ekle, solundaysa çıkar.',
 dict(A='54 L, yalnızca etiketler arasındaki fark (3/5); ibreler etiketlerde değil.',B='60 L, A’yı 1/5’in sağına (4/15) koyunca çıkıyor.',D='84 L, sabah depodaki su (14/15 × 90); akşam kalan 12 L’yi çıkarmalısın.',E='90 L, deponun tamamı; depo sabah tam dolu değildi.'),
 kisa='Bir bölme 90 × 1/15 = 6 L. A’dan S’ye 1 + 9 + 2 = 12 bölme: 12 × 6 = 72 L.',sekil=sek)

# ===== 0033 faktöriyel ZOR (K-SK-26)
v=[(a,b) for a in range(1,25) for b in range(1,a) if F(a)==12*F(b)]; assert v==[(4,2),(12,11)] and sum(a+b for a,b in v)==29
R('0033','sk-faktoriyel','Faktöriyel','zor','Temel Kavramlar · Faktöriyel','mat|Temel Kavramlar','Faktöriyel oranını ardışık sayıların çarpımı olarak yazar ve tüm çözümleri bulur.','düz',4,
 'K-SK-26 (faktöriyelli ifadeyi sadeleştirme) · yeni yapı (iki faktöriyelin oranı), yeni istenen (tüm çözümlerin toplamı)',
 'a ve b pozitif tam sayılar olmak üzere\na! = 12 · b!\nolduğuna göre a + b toplamının alabileceği değerlerin toplamı kaçtır?',
 ['6','13','16','23','29'],'E','a + b’nin bütün olası değerlerinin toplamı.',
 ['a! ÷ b! = 12 yaz. a, b’den büyük olmalı; neden?','a! ÷ b!, b + 1’den a’ya kadar ardışık sayıların çarpımıdır.','12’yi ardışık sayıların çarpımı olarak kaç farklı şekilde yazabilirsin? Tek sayı da bir “çarpım” sayılır.'],[FAK],
 [A('Oranı yaz','a! = 12 · b! ise a!, b!’den büyük; demek ki a > b.','a! ÷ b! = 12'),
  A('Sadeleştir','a! = a × (a − 1) × … × (b + 1) × b!. b! sadeleşir; geriye b + 1’den a’ya kadar ardışık sayıların çarpımı kalır.','(b + 1) × (b + 2) × … × a = 12'),
  A('Tek çarpan','Çarpım tek sayıdan oluşabilir: a = 12, b = 11 (12! = 12 × 11!).','a = 12, b = 11 ⇒ a + b = 23'),
  A('İki çarpan','12 = 3 × 4: b + 1 = 3, a = 4.','a = 4, b = 2 ⇒ a + b = 6'),
  A('Başka yok','Üç ardışık sayının çarpımı: 1 × 2 × 3 = 6, 2 × 3 × 4 = 24; 12 çıkmaz.','23 + 6 = 29')],
 '“a! = k · b!” görünce k’yi ardışık sayıların çarpımı olarak yaz; k’nin kendisi (tek çarpan) da bir çözümdür, unutma.',
 dict(A='6 yalnızca a = 4, b = 2 durumu; a = 12, b = 11 de sağlıyor.',B='13 = 2 + 11, yalnızca b değerlerinin toplamı.',C='16 = 4 + 12, yalnızca a değerlerinin toplamı.',D='23 yalnızca a = 12, b = 11 durumu; 12 = 3 × 4 çözümünü atlamışsın.'))
v=[(a,b) for a in range(1,40) for b in range(1,a) if F(a)==30*F(b)]; assert v==[(6,4),(30,29)] and sum(a-b for a,b in v)==3
K('0033','m ve n pozitif tam sayılar olmak üzere\nm! = 30 · n!\nolduğuna göre m − n farkının alabileceği değerlerin toplamı kaçtır?',
 ['1','2','3','10','59'],'C','m − n’nin bütün olası değerlerinin toplamı.',
 ['m! ÷ n! = 30 yaz; m ile n’den hangisi büyük?','m! ÷ n!, n + 1’den m’ye kadar ardışık sayıların çarpımıdır.','30’u ardışık sayıların çarpımı olarak kaç şekilde yazabilirsin? 30’un kendisini de say.'],[FAK],
 [A('Oranı yaz','m! = 30 · n! ise m > n.','m! ÷ n! = 30'),
  A('Sadeleştir','n! sadeleşir; n + 1’den m’ye kadar ardışık sayıların çarpımı kalır.','(n + 1) × … × m = 30'),
  A('Tek çarpan','m = 30, n = 29 (30! = 30 × 29!).','m − n = 1'),
  A('İki çarpan','30 = 5 × 6: n + 1 = 5, m = 6.','m = 6, n = 4 ⇒ m − n = 2'),
  A('Başka yok','Üç ardışık: 2 × 3 × 4 = 24, 3 × 4 × 5 = 60; 30 çıkmaz.','1 + 2 = 3')],
 'Ardışık çarpım sayısı kadar fark oluşur: tek çarpan ⇒ m − n = 1, iki çarpan ⇒ m − n = 2.',
 dict(A='1 yalnızca m = 30, n = 29 durumu; 30 = 5 × 6 çözümünü atlamışsın.',B='2 yalnızca m = 6, n = 4 durumu; m = 30, n = 29 de sağlıyor.',D='10 = 6 + 4; soru m − n’yi soruyor, m + n’yi değil.',E='59 = 30 + 29; soru m − n’yi soruyor, m + n’yi değil.'))

# ===== 0034 asal ZOR (K-SK-27)
P=[p for p in range(2,200) if all(p%d for d in range(2,int(p**.5)+1))]
v=[(a,b) for a in P for b in P if 3*a+5*b==61]; assert v==[(2,11),(17,2)] and sum(a+b for a,b in v)==32
R('0034','sk-asal','Asal sayılar','zor','Temel Kavramlar · Asal Sayılar','mat|Temel Kavramlar','Asal sayılarla kurulan denklemde tek-çift özelliğini kullanarak bütün çözümleri bulur.','düz',4,
 'K-SK-27 (asal denklemde parite: biri 2 olmalı) · yeni denklem (katsayılı toplam), iki çözüm, yeni istenen (değerlerin toplamı)',
 'a ve b asal sayılar olmak üzere\n3a + 5b = 61\nolduğuna göre a + b toplamının alabileceği değerlerin toplamı kaçtır?',
 ['13','19','22','32','34'],'D','a + b’nin bütün olası değerlerinin toplamı.',
 ['a ve b’nin ikisi de tek olsaydı 3a + 5b tek mi çift mi olurdu?','61 tek; o hâlde a ile b’den biri çift olmalı. Hangi asal çifttir?','a = 2 ve b = 2 durumlarını ayrı ayrı dene.'],[ASAL,TEK],
 [A('Tek-çift','a ve b ikisi de tek olsaydı 3a ve 5b de tek olur; tek + tek = çift. Ama 61 tek.','ikisi de tek olamaz'),
  A('Biri 2','Çift olan tek asal 2. Demek ki a = 2 ya da b = 2.','a = 2 ya da b = 2'),
  A('a = 2','3 × 2 + 5b = 61 ⇒ 5b = 55.','b = 11 (asal ✓) ⇒ a + b = 13'),
  A('b = 2','3a + 5 × 2 = 61 ⇒ 3a = 51.','a = 17 (asal ✓) ⇒ a + b = 19'),
  A('Topla','İki durum da geçerli.','13 + 19 = 32')],
 'Asal sayılı denklemde toplam tekse taraflardan biri çifttir ve çift asal yalnızca 2’dir. İki durumu da dene; ikisi de çıkabilir.',
 dict(A='13 yalnızca a = 2, b = 11 durumu; b = 2, a = 17 de sağlıyor.',B='19 yalnızca b = 2, a = 17 durumu; a = 2, b = 11 de sağlıyor.',C='22 = 2 × 11, bir durumdaki a · b çarpımı; soru toplamları soruyor.',E='34 = 17 × 2, bir durumdaki a · b çarpımı; soru toplamları soruyor.'))
v=[(a,b) for a in P for b in P if 5*a+7*b==59]; assert v==[(2,7)]
K('0034','p ve r asal sayılar olmak üzere\n5p + 7r = 59\nolduğuna göre p + r toplamı kaçtır?',
 ['7','9','11','14','18'],'B','Denklemi sağlayan p ve r için p + r.',
 ['p ve r’nin ikisi de tek olsaydı 5p + 7r tek mi çift mi olurdu?','59 tek; demek ki biri 2 olmalı.','p = 2 ve r = 2 durumlarını ayrı ayrı dene; bulduğun sayı gerçekten asal mı?'],[ASAL,TEK],
 [A('Tek-çift','İkisi de tek olsaydı 5p ve 7r tek olur; tek + tek = çift. 59 tek.','ikisi de tek olamaz'),
  A('Biri 2','Çift olan tek asal 2.','p = 2 ya da r = 2'),
  A('p = 2','5 × 2 + 7r = 59 ⇒ 7r = 49.','r = 7 (asal ✓)'),
  A('r = 2','5p + 14 = 59 ⇒ 5p = 45 ⇒ p = 9. 9 = 3 × 3 asal değil.','r = 2 olmaz'),
  A('Sonuç','Tek çözüm p = 2, r = 7.','p + r = 9')],
 'İki durumu da dene ve bulduğun sayının asal olup olmadığını mutlaka kontrol et.',
 dict(A='7 yalnızca r’nin değeri; soru p + r’yi soruyor.',C='11 = 9 + 2; 9 asal olmadığı için r = 2 durumu geçersiz.',D='14 = 2 × 7, p · r çarpımı; soru toplamı soruyor.',E='18 = 9 × 2; 9 asal değil ve soru toplamı soruyor.'))

# ===== 0035 işaret ZOR (K-SK-28)
import random
random.seed(5); vals=[(random.choice([-1,1])*random.randint(1,9),random.choice([-1,1])*random.randint(1,9),random.choice([-1,1])*random.randint(1,9)) for _ in range(20000)]
v=[(a,b,c) for a,b,c in vals if a**3*b>0 and a*c**4<0 and b*c<0]; assert all(a<0 and b<0 and c>0 for a,b,c in v)
assert oncul(v,lambda a,b,c:a*b*c>0,lambda a,b,c:b-a>0,lambda a,b,c:(a-c)*b>0)=={'I','III'}
R('0035','sk-isaret','İşaret inceleme ve sıralama','zor','Temel Kavramlar · İşaret İnceleme','mat|Temel Kavramlar','Tek ve çift kuvvetli çarpımların işaretinden harflerin işaretlerini bulur; ifadelerin işaretini belirler.','öncüllü',4,
 'K-SK-28 (çarpım eşitsizliklerinden işaret) · yeni yapı (tek ve çift kuvvetler), yeni öncüller',
 'a, b ve c sıfırdan farklı gerçel sayılardır.\na³ · b > 0\na · c⁴ < 0\nb · c < 0\nolduğuna göre\nI. a · b · c > 0\nII. b − a > 0\nIII. (a − c) · b > 0\nifadelerinden hangileri kesinlikle doğrudur?',
 ['Yalnız I','Yalnız III','I ve III','II ve III','I, II ve III'],'C','Her durumda doğru olan ifadeler.',
 ['c⁴ sayısının işareti nedir? İkinci eşitsizlikten a’nın işaretini bul.','a³ ile a aynı işaretlidir; birinci eşitsizlikten b’yi bul.','Son eşitsizlikten c’yi bul; öncüllerde işaretleri yerine koy.'],[KUV,ISR],
 [A('a’nın işareti','c⁴ çift kuvvet olduğu için pozitif. a · (pozitif) < 0 ise a negatif.','c⁴ > 0 ⇒ a < 0'),
  A('b’nin işareti','a³ tek kuvvet, a ile aynı işaretli: negatif. Negatif · b > 0 ise b negatif.','a³ < 0 ⇒ b < 0'),
  A('c’nin işareti','b · c < 0 ve b negatif ise c pozitif.','c > 0'),
  A('Öncüller','I. (−)(−)(+) = + ✓. II. b ile a’nın ikisi de negatif; hangisinin büyük olduğu belli değil ✗. III. a − c: negatif − pozitif = negatif; (−) · b(−) = + ✓.','Doğru: I ve III')],
 'Çift kuvvet işareti “siler” (her zaman pozitif), tek kuvvet işareti korur. İki negatifin farkının işareti ise belli değildir.',
 dict(A='III de doğru: a − c negatif, b negatif; çarpım pozitif.',B='I de doğru: a ve b negatif, c pozitif; a · b · c pozitif.',D='II kesin değil: a = −1, b = −5 için b − a = −4 < 0 olur.',E='II kesin değil: b ile a aynı işaretli, büyüklükleri belli değil.'),
 kisa='İşaretleri bulduktan sonra örnek sayı koy: a = −1, b = −2, c = 3. I: 6 > 0 ✓, II: −1 > 0 ✗, III: (−4)(−2) = 8 > 0 ✓. Örnek bir ifadeyi eleyebilir; doğru kalanları işaret kuralıyla doğrula.')
v=[(a,b,c) for a,b,c in vals if a*b**4>0 and a**2*c<0 and b**3*c>0]; assert all(a>0 and b<0 and c<0 for a,b,c in v)
assert oncul(v,lambda a,b,c:a*b*c>0,lambda a,b,c:c-a<0,lambda a,b,c:b<c)=={'I','II'}
K('0035','x, y ve z sıfırdan farklı gerçel sayılardır.\nx · y⁴ > 0\nx² · z < 0\ny³ · z > 0\nolduğuna göre\nI. x · y · z > 0\nII. z − x < 0\nIII. y < z\nifadelerinden hangileri kesinlikle doğrudur?',
 ['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III'],'C','Her durumda doğru olan ifadeler.',
 ['y⁴ ve x²’nin işareti nedir?','İlk iki eşitsizlikten x ile z’nin işaretini bul.','y³ ile y aynı işaretlidir; son eşitsizlikten y’yi bul.'],[KUV,ISR],
 [A('x’in işareti','y⁴ çift kuvvet, pozitif. x · (pozitif) > 0 ise x pozitif.','x > 0'),
  A('z’nin işareti','x² pozitif. (pozitif) · z < 0 ise z negatif.','z < 0'),
  A('y’nin işareti','y³ · z > 0 ve z negatif ise y³ negatif; tek kuvvet işareti korur.','y < 0'),
  A('Öncüller','I. (+)(−)(−) = + ✓. II. negatif − pozitif = negatif ✓. III. y ile z ikisi de negatif; hangisinin küçük olduğu belli değil ✗.','Doğru: I ve II')],
 'İki negatif sayının sıralaması işaret bilgisinden çıkmaz; böyle öncüller “kesin” değildir.',
 dict(A='II de doğru: z negatif, x pozitif; z − x negatiftir.',B='I de doğru: x pozitif, y ve z negatif; çarpım pozitif.',D='III kesin değil: y = −1, z = −5 için y < z yanlış.',E='III kesin değil: y ile z’nin büyüklükleri belli değil.'))

# ===== 0036 tanımlı KOLAY (K-SK-07)
assert ds(789)==24 and ds(24+15)==12
R('0036','sk-tanimli','Tanımlı sayılar ve semboller','kolay','Temel Kavramlar · Rakam ve Sayı','mat|Temel Kavramlar','Sembolle tanımlanan işlemi iç içe uygular.','düz',2,
 'K-SK-07 (sembolle tanımlı işlem, iç içe) · yeni tanım (rakamlar toplamı), yeni sayılar',
 'Bir n doğal sayısı için S(n), n’nin rakamlarının toplamını göstermektedir.\nÖrneğin S(352) = 3 + 5 + 2 = 10’dur.\nBuna göre S(S(789) + 15) değeri kaçtır?',
 ['3','6','12','24','39'],'C','İç işlemden başlayarak bulunan değer.',
 ['İçteki S(789)’u hesapla.','Bulduğuna 15 ekle.','Çıkan sayının rakamlarını topla.'],[RT,PAR],
 [A('İçteki işlem','Önce parantezin içindeki S(789).','7 + 8 + 9 = 24'),
  A('15 ekle','Parantezin içi tamamlanır.','24 + 15 = 39'),
  A('Dıştaki S','39’un rakamlarını topla.','S(39) = 3 + 9 = 12')],
 'İç içe sembollerde en içten başla; her adımda yalnızca bir işlem yap.',
 dict(A='3, 12’nin rakamlarını bir kez daha toplamak; S yalnızca iki kez uygulanıyor.',B='6 = S(24); 15’i eklemeyi unutmuşsun.',D='24 = S(789); işlem yarıda kalmış.',E='39, parantezin içi; dıştaki S’yi uygulamamışsın.'))
assert dp(258)==80 and dp(80+7)==56
K('0036','Bir n doğal sayısı için P(n), n’nin rakamlarının çarpımını göstermektedir.\nÖrneğin P(34) = 3 · 4 = 12’dir.\nBuna göre P(P(258) + 7) değeri kaçtır?',
 ['0','15','56','80','87'],'C','İç işlemden başlayarak bulunan değer.',
 ['İçteki P(258)’i hesapla.','Bulduğuna 7 ekle.','Çıkan sayının rakamlarını çarp.'],[RC,PAR],
 [A('İçteki işlem','Önce parantezin içindeki P(258).','2 × 5 × 8 = 80'),
  A('7 ekle','Parantezin içi tamamlanır.','80 + 7 = 87'),
  A('Dıştaki P','87’nin rakamlarını çarp.','P(87) = 8 × 7 = 56')],
 'Önce parantezin içini bitir; dıştaki sembolü en son uygula.',
 dict(A='0 = P(80); 7’yi eklemeden dıştaki P’yi uygulamışsın.',B='15 = 8 + 7; rakamları çarpmak yerine toplamışsın.',D='80 = P(258); işlem yarıda kalmış.',E='87, parantezin içi; dıştaki P’yi uygulamamışsın.'))

# ===== 0037 yerleştirme KOLAY (K-SK-16)
O={'+':lambda x,y:x+y,'−':lambda x,y:x-y,'×':lambda x,y:x*y}
v=[(k,u) for k in O for u in O if k!=u and O[k](6,3)==18 and O[u](8,2)==6]; assert v==[('×','−')] and (7-3)*5==20
R('0037','sk-yerlestirme','Kutulara yerleştirme ve işlem bulma','kolay','Temel Kavramlar · Temel İşlemler','mat|Temel Kavramlar','Verilen eşitliklerden sembollerin hangi işlemi gösterdiğini bulur ve yeni ifadeyi hesaplar.','düz',2,
 'K-SK-16 (sembollerin yerine işlem bulma) · yeni semboller ve eşitlikler, üç işlem',
 '□ ve △ sembollerinin her biri toplama, çıkarma ve çarpma işlemlerinden birini göstermektedir ve iki sembol farklı işlemleri göstermektedir.\n6 □ 3 = 18\n8 △ 2 = 6\nolduğuna göre (7 △ 3) □ 5 işleminin sonucu kaçtır?',
 ['9','20','26','50','105'],'B','Sembollerin gösterdiği işlemlerle bulunan sonuç.',
 ['6 ile 3 arasına hangi işlem konunca 18 çıkar?','8 ile 2 arasına hangi işlem konunca 6 çıkar?','Önce parantezin içini hesapla.'],[PAR],
 [A('□ hangisi?','6 + 3 = 9, 6 − 3 = 3, 6 × 3 = 18.','□ = ×'),
  A('△ hangisi?','8 + 2 = 10, 8 − 2 = 6, 8 × 2 = 16.','△ = −'),
  A('Hesapla','Parantezin içi önce.','(7 − 3) × 5 = 4 × 5 = 20')],
 'Her eşitlikte işlemleri tek tek dene; sonra parantez önceliğiyle hesapla.',
 dict(A='9 = (7 − 3) + 5; □ toplama değil, çarpma.',C='26 = 7 × 3 + 5; sembolleri karıştırmışsın.',D='50 = (7 + 3) × 5; △ toplama değil, çıkarma.',E='105 = 7 × 3 × 5; △ çarpma değil.'))
O4={'+':lambda x,y:Fr(x+y),'−':lambda x,y:Fr(x-y),'×':lambda x,y:Fr(x*y),'÷':lambda x,y:Fr(x,y)}
v=[(k,u) for k in O4 for u in O4 if k!=u and O4[k](12,4)==3 and O4[u](5,7)==12]; assert v==[('÷','+')] and 20//5+6==10
K('0037','◇ ve ○ sembollerinin her biri toplama, çıkarma, çarpma ve bölme işlemlerinden birini göstermektedir ve iki sembol farklı işlemleri göstermektedir.\n12 ◇ 4 = 3\n5 ○ 7 = 12\nolduğuna göre (20 ◇ 5) ○ 6 işleminin sonucu kaçtır?',
 ['10','21','24','31','106'],'A','Sembollerin gösterdiği işlemlerle bulunan sonuç.',
 ['12 ile 4 arasına hangi işlem konunca 3 çıkar?','5 ile 7 arasına hangi işlem konunca 12 çıkar?','Önce parantezin içini hesapla.'],[PAR],
 [A('◇ hangisi?','12 + 4 = 16, 12 − 4 = 8, 12 × 4 = 48, 12 ÷ 4 = 3.','◇ = ÷'),
  A('○ hangisi?','5 + 7 = 12; diğerleri 12 vermez.','○ = +'),
  A('Hesapla','Parantezin içi önce.','(20 ÷ 5) + 6 = 4 + 6 = 10')],
 'Bölmeyi de dene: sonuç küçülüyorsa çoğu zaman bölme ya da çıkarmadır.',
 dict(B='21 = 20 − 5 + 6; ◇ çıkarma değil, bölme.',C='24 = 4 × 6; ○ çarpma değil, toplama.',D='31 = 20 + 5 + 6; ◇ toplama değil.',E='106 = 20 × 5 + 6; ◇ çarpma değil.'))

# ===== 0038 örüntü KOLAY (K-SK-12)
d=[3,7,1,5]; assert sum((d*13)[:50])==202
R('0038','sk-oruntu','Örüntü ve döngü','kolay','Temel Kavramlar · Örüntüler','mat|Temel Kavramlar','Tekrar eden bir dizide tam blokları ve kalanı kullanarak toplam bulur.','düz',2,
 'K-SK-12 (sabit sırayla tekrar, tam tur + kalan) · yeni kurgu (sayı dizisi toplamı)',
 '3, 7, 1, 5, 3, 7, 1, 5, 3, …\nbiçiminde devam eden dizide 3, 7, 1, 5 sayıları bu sırayla tekrar etmektedir.\nBuna göre dizinin ilk 50 teriminin toplamı kaçtır?',
 ['192','195','200','202','208'],'D','İlk 50 terimin toplamı.',
 ['Tekrar eden bloğun toplamını bul.','50 terimde kaç tam blok var, kaç terim artıyor?','Artan terimler bloğun başından gelir.'],[PER],
 [A('Blok toplamı','Tekrar eden blok 4 terim.','3 + 7 + 1 + 5 = 16'),
  A('Blok sayısı','50’yi 4’e böl.','50 = 4 × 12 + 2 ⇒ 12 tam blok, 2 terim artar'),
  A('Topla','Artan 2 terim bloğun ilk ikisi: 3 ve 7.','12 × 16 + 3 + 7 = 192 + 10 = 202')],
 'Tekrar eden dizide terim sayısını blok uzunluğuna böl; kalan terimler her zaman bloğun başından alınır.',
 dict(A='192 = 12 × 16; artan 2 terimi eklemeyi unutmuşsun.',B='195 = 192 + 3; artan iki terimden yalnız birini eklemişsin.',C='200 = 50 × 4; terimlerin ortalaması 4, ama 50 terim tam blok değil.',E='208 = 13 × 16; 13. blok tamamlanmıyor, yalnızca 2 terimi var.'))
d=[2,9,4]; assert sum((d*14)[:40])==197
K('0038','2, 9, 4, 2, 9, 4, 2, …\nbiçiminde devam eden dizide 2, 9, 4 sayıları bu sırayla tekrar etmektedir.\nBuna göre dizinin ilk 40 teriminin toplamı kaçtır?',
 ['195','197','200','206','210'],'B','İlk 40 terimin toplamı.',
 ['Tekrar eden bloğun toplamını bul.','40 terimde kaç tam blok var, kaç terim artıyor?','Artan terim bloğun başından gelir.'],[PER],
 [A('Blok toplamı','Tekrar eden blok 3 terim.','2 + 9 + 4 = 15'),
  A('Blok sayısı','40’ı 3’e böl.','40 = 3 × 13 + 1 ⇒ 13 tam blok, 1 terim artar'),
  A('Topla','Artan terim bloğun ilki: 2.','13 × 15 + 2 = 195 + 2 = 197')],
 'Kalan terimi bloğun başından al; sondan almak en sık yapılan hatadır.',
 dict(A='195 = 13 × 15; artan 1 terimi eklemeyi unutmuşsun.',C='200 = 40 × 5; ortalama 5 ama 40 terim tam blok değil.',D='206 = 195 + 2 + 9; yalnızca 1 terim artıyor.',E='210 = 14 × 15; 14. blokta yalnızca 1 terim var.'))

# ===== 0039 rakam en az–en çok KOLAY (K-SK-22)
fark=lambda n:len(set(str(n)))==len(str(n))
eb=max(n for n in range(100,1000) if n%2==0 and fark(n)); ek=min(n for n in range(100,1000) if n%2==1 and fark(n)); assert (eb,ek)==(986,103) and eb-ek==883
R('0039','sk-rakam-enaz','Rakamlarla en az – en çok','kolay','Temel Kavramlar · Sayı Basamakları','mat|Sayı Basamakları','Rakamları farklı en büyük ve en küçük sayıları tek-çift koşuluyla yazar.','düz',2,
 'K-SK-22 (rakamlarla en büyük/en küçük sayı) · yeni koşullar (rakamları farklı, tek/çift), yeni istenen (fark)',
 'Rakamları birbirinden farklı üç basamaklı en büyük çift sayı ile rakamları birbirinden farklı üç basamaklı en küçük tek sayının farkı kaçtır?',
 ['873','883','884','885','897'],'B','İki sayının farkı.',
 ['En büyük sayı için yüzler basamağından başla: en büyük rakamları sırayla yerleştir.','Çift olması için birler basamağı ne olmalı?','En küçük tek sayıda yüzler basamağı 0 olamaz; 101 neden olmaz?'],[TC,RAK],
 [A('En büyük çift','Yüzler 9, onlar 8. Birler çift ve 9, 8’den farklı olmalı: en büyük 6.','986'),
  A('En küçük tek','Yüzler 1, onlar 0. Birler tek ve 1’den farklı olmalı: en küçük 3.','103'),
  A('Farkı al','Büyükten küçüğü çıkar.','986 − 103 = 883')],
 'En büyük sayıda baştan büyük, en küçük sayıda baştan küçük rakamla başla; tek-çift koşulunu en son birler basamağında uygula.',
 dict(A='873 = 976 − 103; 986 daha büyük ve koşulu sağlıyor.',C='884 = 987 − 103; 987 tek, çift sayı olmalı.',D='885 = 986 − 101; 101’de 1 iki kez geçiyor.',E='897 = 998 − 101; ikisinde de rakam tekrarı var.'))
ek4=min(n for n in range(1000,10000) if n%2==0 and fark(n)); eb3=max(n for n in range(100,1000) if n%2==1 and fark(n)); assert (ek4,eb3)==(1024,987) and ek4+eb3==2011
K('0039','Rakamları birbirinden farklı dört basamaklı en küçük çift sayı ile rakamları birbirinden farklı üç basamaklı en büyük tek sayının toplamı kaçtır?',
 ['1989','1997','1999','2010','2011'],'E','İki sayının toplamı.',
 ['En küçük dört basamaklı sayı için binler basamağı 1, sonra en küçük rakamlar.','Çift olması için birler basamağı ne olmalı? 1020 neden olmaz?','En büyük tek sayıda yüzler 9’dan başla; birler tek olmalı.'],[TC,RAK],
 [A('En küçük çift','Binler 1, yüzler 0, onlar 2. Birler çift ve 0, 1, 2’den farklı olmalı: 4.','1024'),
  A('En büyük tek','Yüzler 9, onlar 8. Birler tek ve 9’dan farklı: 7.','987'),
  A('Topla','İki sayıyı topla.','1024 + 987 = 2011')],
 'Rakam tekrarı yasaksa her basamakta önceki rakamları ele; tek-çift koşulunu birler basamağında uygula.',
 dict(A='1989 = 1002 + 987; 1002’de 0 iki kez geçiyor.',B='1997 = 1010 + 987; 1010’da 1 ve 0 iki kez geçiyor.',C='1999 = 1000 + 999; iki sayıda da rakam tekrarı var.',D='2010 = 1023 + 987; 1023 tek, çift sayı olmalı.'))

json.dump(ANA,open(os.path.join(H,'sayi-kumeleri-parti3.json'),'w'),ensure_ascii=False,indent=1)
json.dump(KAR,open(os.path.join(H,'sayi-kumeleri-kardes3.json'),'w'),ensure_ascii=False,indent=1)
from collections import Counter
print(len(ANA),len(KAR),Counter(q['cevap']['sik'] for q in ANA+KAR))
