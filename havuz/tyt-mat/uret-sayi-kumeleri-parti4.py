"""Parti 4: boş orta hücreler (0040–0042: basamak, gösterge, işaret) ve kardeşleri. Her cevap kodla doğrulanır."""
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


BD=B('Basamak değeri','onlar basamağındaki rakam 1 artarsa sayı 10 artar; birler basamağındaki rakam 1 azalırsa sayı 1 azalır')
# ===== 0040 basamak ORTA (K-SK-23)
v=[n for n in range(10,100) if n//10+2<=9 and n%10>=3 and (n//10+2)*10+(n%10-3)==2*n-9]; assert v==[26]
R('0040','sk-basamak','Basamak çözümleme','orta','Temel Kavramlar · Sayı Basamakları','mat|Sayı Basamakları','Rakamları değiştirilen iki basamaklı sayının yeni değerini basamak değeriyle ifade edip denklem kurar.','düz',3,
 'K-SK-23 (basamakları artırıp azaltma, kat ilişkisi) · yeni artış/azalış miktarları, yeni ilişki (2 katından 9 eksik)',
 'İki basamaklı bir sayının onlar basamağındaki rakam 2 artırılıp birler basamağındaki rakam 3 azaltıldığında elde edilen yeni sayı, ilk sayının 2 katından 9 eksik olur.\nBuna göre ilk sayı kaçtır?',
 ['23','26','32','43','52'],'B','Koşulu sağlayan ilk sayı.',
 ['Onlar basamağındaki rakam 2 artınca sayı kaç artar?','Birler basamağındaki rakam 3 azalınca sayı kaç azalır? Yeni sayıyı ilk sayı cinsinden yaz.','Yeni sayıyı “2 katından 9 eksik” ifadesine eşitle.'],[IKI,BD],
 [A('İlk sayıya ad ver','İlk sayı N olsun.','N = 10 × A + B'),
  A('Yeni sayıyı yaz','Onlar 2 artınca sayı 20 artar; birler 3 azalınca sayı 3 azalır.','yeni sayı = N + 20 − 3 = N + 17'),
  A('Eşitle','Yeni sayı, N’nin 2 katından 9 eksik.','N + 17 = 2N − 9'),
  A('Çöz','N’leri bir tarafa topla.','N = 17 + 9 = 26'),
  A('Kontrol','26 → onlar 2 + 2 = 4, birler 6 − 3 = 3 ⇒ 43. 2 × 26 − 9 = 43 ✓','ilk sayı = 26')],
 'Basamaktaki rakam değişince sayının ne kadar değiştiğini basamak değeriyle yaz: onlar ±1 ⇒ sayı ±10, birler ±1 ⇒ sayı ±1.',
 dict(A='23 için yeni sayı 40 olur; 2 × 23 − 9 = 37, eşit değil.',C='32, birler basamağını 3 artırmışsın gibi kurulan denklemden çıkıyor (N + 23 = 2N − 9).',D='43, yeni sayı; soru ilk sayıyı soruyor.',E='52, ilk sayının 2 katı; 9 çıkarmayı ve asıl istenen sayıyı atlamışsın.'))
v=[n for n in range(10,100) if n//10+3<=9 and n%10>=2 and (n//10+3)*10+(n%10-2)==3*n-30]; assert v==[29]
K('0040','İki basamaklı bir sayının onlar basamağındaki rakam 3 artırılıp birler basamağındaki rakam 2 azaltılırsa elde edilen yeni sayı, ilk sayının 3 katından 30 eksik olur.\nBuna göre ilk sayı kaçtır?',
 ['29','31','57','59','87'],'A','Koşulu sağlayan ilk sayı.',
 ['Onlar basamağındaki rakam 3 artınca sayı kaç artar?','Birler basamağındaki rakam 2 azalınca sayı kaç azalır?','Yeni sayıyı “3 katından 30 eksik” ifadesine eşitle.'],[IKI,BD],
 [A('İlk sayıya ad ver','İlk sayı N olsun.','N = 10 × A + B'),
  A('Yeni sayıyı yaz','Onlar 3 artınca sayı 30 artar; birler 2 azalınca sayı 2 azalır.','yeni sayı = N + 30 − 2 = N + 28'),
  A('Eşitle','Yeni sayı, N’nin 3 katından 30 eksik.','N + 28 = 3N − 30'),
  A('Çöz','N’leri bir tarafa topla.','2N = 58 ⇒ N = 29'),
  A('Kontrol','29 → onlar 5, birler 7 ⇒ 57. 3 × 29 − 30 = 57 ✓','ilk sayı = 29')],
 'Önce değişimi “N + …” biçiminde yaz; sonra verilen ilişkiyi kur.',
 dict(B='31, birler basamağını 2 artırmışsın gibi kurulan denklemden çıkıyor (N + 32 = 3N − 30).',C='57, yeni sayı; soru ilk sayıyı soruyor.',D='59, birler basamağındaki azalmayı unutup yalnız onlar basamağını artırmak.',E='87, ilk sayının 3 katı; 30 çıkarmadan bırakılmış.'))

# ===== 0041 gösterge ORTA (K-SK-04)
bol=Fr(400-250,6); assert 400+3*bol==475 and 400+3*Fr(150,5)==490
R('0041','sk-gosterge','Sayı doğrusu ve göstergeler','orta','Temel Kavramlar · Sayı Doğrusu','mat|Temel Kavramlar','Eşit bölmeli bir göstergede etiketlerin dışındaki bir konumu okur.','şekilli',3,
 'K-SK-04 (eşit bölmeli gösterge) · yeni kurgu (mutfak tartısı), ibre etiketlerin dışında',
 'Bir mutfak tartısının göstergesinin bir bölümü aşağıda verilmiştir. Gösterge eşit aralıklarla bölmelenmiştir ve kırmızı ok, tartıdaki unun kütlesini gram cinsinden göstermektedir.\nBuna göre tartıdaki un kaç gramdır?',
 ['325','430','475','490','550'],'C','Okun gösterdiği değer.',
 ['250 ile 400 arasında kaç bölme var?','Bir bölmenin kaç gram olduğunu bul.','Ok, 400’ün kaç bölme sağında?'],[GOS],
 [A('Bölme sayısı','250 ile 400 etiketleri arasında 6 bölme var (çizgileri değil, aralıkları say).','400 − 250 = 150 g'),
  A('Bir bölme','150 g, 6 eş bölmeye ayrılmış.','150 ÷ 6 = 25 g'),
  A('Okun gösterdiği değer','Ok, 400’ün 3 bölme sağında.','400 + 3 × 25 = 475 g',G.gosterge_iki_ibre(-1,10,{0:'250',6:'400'},{9:'?'},yay=(6,9,'3 bölme = 75 g')))],
 'Bölme sayısını sayarken çizgileri değil aralıkları say; iki etiket arasında 7 çizgi varsa 6 aralık vardır.',
 dict(A='325, oku 250’nin 3 bölme sağında okumak; ok 400’ün sağında.',B='430, bir bölmeyi 10 g sanmak; 150 g 6 bölmeye ayrılmış.',D='490, aralığı 5 bölme sayıp bir bölmeyi 30 g bulmak; 6 bölme var.',E='550, etiketler arasındaki 150 g’ı 400’e eklemek; ok 3 bölme sağda.'),
 sekil=G.gosterge_iki_ibre(-1,10,{0:'250',6:'400'},{9:''}))
bol=Fr(8-(-4),4); assert -4-2*bol==-10
K('0041','Bir dış ortam termometresinin göstergesinin bir bölümü aşağıda verilmiştir. Gösterge eşit aralıklarla bölmelenmiştir ve kırmızı ok, hava sıcaklığını °C cinsinden göstermektedir.\nBuna göre hava sıcaklığı kaç °C’dir?',
 ['−13','−10','−8','−6','2'],'B','Okun gösterdiği sıcaklık.',
 ['−4 ile 8 arasındaki fark kaç derece?','Aralarında kaç bölme var? Bir bölmeyi bul.','Ok, −4’ün kaç bölme solunda? Sola gidildikçe değer azalır.'],[GOS,B('Negatif sayılarda fark','8 ile −4 arasındaki fark 8 − (−4) = 8 + 4 = 12’dir')],
 [A('Etiket farkı','Negatif sayıdan çıkarırken işarete dikkat.','8 − (−4) = 12'),
  A('Bir bölme','−4 ile 8 arasında 4 bölme var.','12 ÷ 4 = 3 °C'),
  A('Okun gösterdiği değer','Ok, −4’ün 2 bölme solunda; sola gidildikçe sıcaklık azalır.','−4 − 2 × 3 = −10 °C',G.gosterge_iki_ibre(-3,6,{0:'−4',4:'8'},{-2:'?'},yay=(-2,0,'2 bölme = 6 °C')))],
 'Negatif etiketli göstergede farkı 8 − (−4) diye işaretle hesapla; sola giderken çıkar.',
 dict(A='−13, oku −4’ün 3 bölme solunda okumak; ok 2 bölme solda.',C='−8, bir bölmeyi 2 °C sanmak; −4 ile 8 arası 12 derece.',D='−6, etiket farkını 8 − 4 = 4 hesaplayıp bir bölmeyi 1 °C bulmak.',E='2, oku −4’ün sağında saymak; ok solda, değer azalır.'),
 sekil=G.gosterge_iki_ibre(-3,6,{0:'−4',4:'8'},{-2:''}))

# ===== 0042 işaret ORTA (K-SK-28)
import random
random.seed(7); vals=[tuple(random.choice([-1,1])*random.randint(1,20) for _ in range(3)) for _ in range(40000)]
v=[(a,b,c) for a,b,c in vals if a*b<0 and b*c>0 and a>c]  # a/b<0 ⇔ a·b<0 ; b/c>0 ⇔ b·c>0
assert v and all(a>0 and b<0 and c<0 for a,b,c in v)
S42=[('b · c',lambda a,b,c:b*c<0),('a − b',lambda a,b,c:a-b<0),('a · c',lambda a,b,c:a*c<0),('a + b',lambda a,b,c:a+b<0),('c − b',lambda a,b,c:c-b<0)]
assert [n for n,f in S42 if all(f(*x) for x in v)]==['a · c']
R('0042','sk-isaret','İşaret inceleme ve sıralama','orta','Temel Kavramlar · İşaret İnceleme','mat|Temel Kavramlar','Bölüm ve sıralama bilgisinden durum inceleyerek sayıların işaretlerini bulur.','düz',3,
 'K-SK-28 (bölüm eşitsizliklerinden işaret ve sıralama) · yeni yapı (bölüm), durum incelemesi, yeni istenen (kesin negatif)',
 'Sıfırdan farklı a, b ve c gerçel sayıları için a / b bölümü negatif, b / c bölümü pozitiftir ve a sayısı c’den büyüktür.\nBuna göre aşağıdaki ifadelerden hangisinin değeri her zaman negatiftir?',
 [n for n,f in S42],'C','Her durumda negatif olan ifade.',
 ['a / b < 0 ne anlatıyor: a ile b aynı mı, zıt mı işaretli?','b / c > 0 ise b ile c’nin işaretleri nasıl?','a’yı önce negatif kabul et; a > c koşulu sağlanabiliyor mu?'],[ISR,B('Bölümün işareti','bölmede de çarpmadaki kural geçerli: aynı işaretliler ⇒ +, zıt işaretliler ⇒ −')],
 [A('İlişkileri yaz','a / b negatif ⇒ a ile b zıt işaretli. b / c pozitif ⇒ b ile c aynı işaretli. Demek ki a ile c zıt işaretli.','a, b zıt · b, c aynı ⇒ a, c zıt'),
  A('a negatif olsaydı','c pozitif olurdu. O zaman a > c “negatif > pozitif” demek olur; olamaz.','a < 0 ⇒ çelişki'),
  A('İşaretler','Demek ki a pozitif; b ve c negatif.','a > 0 · b < 0 · c < 0'),
  A('Şıkları dene','a × c = (+) × (−) negatif ✓. b × c pozitif, a − b pozitif. a + b ve c − b’nin işareti sayılara bağlı.','a × c < 0')],
 'İki zıt işaretli sayıdan hangisinin pozitif olduğunu sıralama bilgisi söyler: büyük olan pozitiftir.',
 dict(A='b · c pozitif: b ve c ikisi de negatif.',B='a − b pozitif: pozitiften negatif çıkarınca sonuç büyür.',D='a + b’nin işareti belli değil: a = 5, b = −2 için pozitif, a = 1, b = −4 için negatif.',E='c − b’nin işareti belli değil: b ile c’nin hangisinin büyük olduğu bilinmiyor.'))
v=[(x,y,z) for x,y,z in vals if x*y>0 and y*z<0 and x<z]
assert v and all(x<0 and y<0 and z>0 for x,y,z in v)
S42k=[('x · z',lambda x,y,z:x*z>0),('x + y',lambda x,y,z:x+y>0),('y + z',lambda x,y,z:y+z>0),('z − y',lambda x,y,z:z-y>0),('x − z',lambda x,y,z:x-z>0)]
assert [n for n,f in S42k if all(f(*t) for t in v)]==['z − y']
K('0042','Sıfırdan farklı x, y ve z gerçel sayıları için x / y bölümü pozitif, y · z çarpımı negatiftir ve x sayısı z’den küçüktür.\nBuna göre aşağıdaki ifadelerden hangisinin değeri her zaman pozitiftir?',
 [n for n,f in S42k],'D','Her durumda pozitif olan ifade.',
 ['x / y > 0 ise x ile y’nin işaretleri nasıl?','y · z < 0 ise y ile z zıt işaretli; x ile z için ne söylenebilir?','x’i önce pozitif kabul et; x < z koşulu sağlanabiliyor mu?'],[ISR,B('Bölümün işareti','bölmede de çarpmadaki kural geçerli: aynı işaretliler ⇒ +, zıt işaretliler ⇒ −')],
 [A('İlişkileri yaz','x / y pozitif ⇒ x ile y aynı işaretli. y · z negatif ⇒ y ile z zıt. Demek ki x ile z zıt işaretli.','x, y aynı · y, z zıt ⇒ x, z zıt'),
  A('x pozitif olsaydı','z negatif olurdu. O zaman x < z “pozitif < negatif” demek olur; olamaz.','x > 0 ⇒ çelişki'),
  A('İşaretler','Demek ki x ve y negatif, z pozitif.','x < 0 · y < 0 · z > 0'),
  A('Şıkları dene','z − y = pozitif − negatif ⇒ pozitif ✓. x × z ve x + y negatif; x − z negatif; y + z sayılara bağlı.','z − y > 0')],
 'Zıt işaretli iki sayıdan küçük olan negatiftir; sıralama bilgisini işaret bulmak için kullan.',
 dict(A='x · z negatif: x negatif, z pozitif.',B='x + y negatif: iki negatifin toplamı negatiftir.',C='y + z’nin işareti belli değil: y = −1, z = 5 için pozitif, y = −6, z = 2 için negatif.',E='x − z negatif: negatiften pozitif çıkarınca sonuç daha da küçülür.'))

json.dump(ANA,open(os.path.join(H,'sayi-kumeleri-parti4.json'),'w'),ensure_ascii=False,indent=1)
json.dump(KAR,open(os.path.join(H,'sayi-kumeleri-kardes4.json'),'w'),ensure_ascii=False,indent=1)
from collections import Counter
print(len(ANA),len(KAR),Counter(q['cevap']['sik'] for q in ANA+KAR))
