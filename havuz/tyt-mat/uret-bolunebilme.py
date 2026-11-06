"""Bölme ve Bölünebilme · parti 1: 8 ana + 8 kardeş. Her cevap ve ara sonuç kodla (kaba kuvvet tarama dahil) doğrulanır."""
import sys,os,json
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,os.path.join(H,'..'))
from ortak import *

# ---------- yardımcılar ----------
def fmt(v):
    v=Fr(v)
    if v.denominator==1: return ('−' if v<0 else '')+str(abs(v.numerator))
    return ('−' if v<0 else '')+f'{abs(v.numerator)}/{v.denominator}'
def SK(dogru,yanlis,sira=None):
    """yanlis: değer -> (tur, açıklama). Sayısal şıklar küçükten büyüğe dizilir; sira verilirse o sıra kullanılır."""
    vals=[dogru]+list(yanlis); assert len(set(vals))==5 and dogru not in yanlis
    if sira is None: vals=sorted(vals,key=Fr); yaz=[fmt(v) for v in vals]
    else: assert sorted(map(str,sira))==sorted(map(str,vals)); vals=list(sira); yaz=[str(v) for v in vals]
    L='ABCDE'; sik=L[vals.index(dogru)]
    return dict(siklar=yaz,sik=sik,cel={L[i]:yanlis[v][1] for i,v in enumerate(vals) if v!=dogru},tur={L[i]:yanlis[v][0] for i,v in enumerate(vals) if v!=dogru})
ds=lambda n:sum(map(int,str(n)))
def dp(n):
    r=1
    for c in str(n): r*=int(c)
    return r

ONEK='bolunebilme'; KONU='Bölme ve Bölünebilme'; UK='mat|Bölme ve Bölünebilme'
P=Parti(ONEK,KONU,UK)

KAL=B('Kalanlı bölme','bölünen = bölen × bölüm + kalan ve 0 ≤ kalan < bölen. Örnek: 17 = 5 × 3 + 2 (kalan 2, bölen 5’ten küçük)')
K3=B('3 ve 9 ile bölünebilme','rakamlar toplamı 3’ün (9’un) katıysa sayı 3’e (9’a) tam bölünür. Örnek: 252 → 2 + 5 + 2 = 9, hem 3’e hem 9’a bölünür')
K5=B('4 ve 5 ile bölünebilme','5: birler basamağı 0 ya da 5 olmalı · 4: son iki basamağın oluşturduğu sayı 4’ün katı olmalı. Örnek: 316 → 16, 4’ün katı')
K11=B('11 ile bölümden kalan','sağdan başlayarak rakamlara sırayla +, −, +, … işareti verilip toplanır; sonuç negatifse 11 eklenir. Örnek: 2541 → 1 − 4 + 5 − 2 = 0, kalan 0')
K9K=B('9 ile bölümden kalan','sayının 9 ile bölümünden kalan, rakamları toplamının 9 ile bölümünden kalana eşittir. Örnek: 563 → 5 + 6 + 3 = 14, kalan 5')
BAS3=B('Basamak çözümleme','ABC = 100 × A + 10 × B + C. Örnek: 675 = 100 × 6 + 10 × 7 + 5')
K45=B('Bölenleri ayırma','aralarında asal çarpanlara ayrılan bir sayıya bölünme, her çarpana ayrı ayrı bölünmedir. Örnek: 45 = 5 × 9, 36 = 4 × 9, 18 = 2 × 9')

# ---------- kartlar ve tipler ----------
TIPLER=[('bln-kalan','Kalanlı bölme ve bölüm–kalan ilişkisi'),('bln-kural','Bölünebilme kurallarıyla rakam bulma'),('bln-kalan-kural','Kurallarla kalan bulma'),
        ('bln-iki-sayi','İki sayı, iki bölünebilme koşulu'),('bln-tanimli','Bölünebilmeyle tanımlanan sayılar')]
TAD=dict(TIPLER)
KARTLAR=[
 dict(id='K-BLN-01',alt='Kalanlı Bölme',fikir='Bölüm ve kalanı verilen bir sayı (paket, sıra, demet) önce bölünen = bölen × bölüm + kalan ile kurulur, sonra başka bir bölene göre kalanı sorulur.',tuzak='Eski kalanı yeni kalan sanmak, kalanı eklemeyi unutmak, bölümü kalanla karıştırmak.',zorluk='kolay',kalip='hikâyeli',adim=2,tipId='bln-kalan',kaynak='ÖSYM (Bölünebilme · kalanlı bölme) · Bilgi Sarmal, 3D (nöbet/paketleme)'),
 dict(id='K-BLN-02',alt='Kalanlı Bölme',fikir='Bölüm ile kalan arasında bir ilişki (bölüm = k × kalan) ya da zincirleme bölmeler verilir; kalan < bölen koşulu en büyük/en küçük değeri belirler.',tuzak='Kalanın bölenden küçük olması gerektiğini unutmak; zincirde ara bölenin kalandan büyük olma koşulunu atlamak.',zorluk='orta',kalip='düz',adim=3,tipId='bln-kalan',kaynak='ÖSYM (n-değişmeli sayılar) · Bilgi Sarmal, Mert kalanlı bölme testleri'),
 dict(id='K-BLN-03',alt='Bölünebilme Kuralları',fikir='Bilinmeyen rakamlı bir sayının 3, 4, 5 ya da 9 ile bölünebilmesinden rakamın alabileceği değerler bulunur.',tuzak='3 ile 9 kuralını karıştırmak; rakamın 9’a kadar çıkabileceğini unutup bir değeri atlamak.',zorluk='kolay',kalip='düz',adim=2,tipId='bln-kural',kaynak='ÖSYM (Bölünebilme Kuralları 1) · Bilgi Sarmal, 345'),
 dict(id='K-BLN-04',alt='Bölünebilme Kuralları',fikir='Bileşik bir bölen (36, 45) aralarında asal çarpanlara ayrılır; her çarpanın kuralı ayrı uygulanır, durumlar ayrı ayrı çözülür.',tuzak='Bir durumdaki rakamı diğer durumdakiyle karıştırmak; rakamlar toplamının 18 dışında 9 ya da 27 de olabileceğini düşünmemek.',zorluk='orta',kalip='düz',adim=3,tipId='bln-kural',kaynak='ÖSYM 2024 (9 ile kalan, rakam bulma) · Bilgi Sarmal (25x3y, 4 ve 3 ile)'),
 dict(id='K-BLN-05',alt='Kalan Bulma',fikir='Bir bölünebilme koşulundan bilinmeyen rakam bulunur, sonra sayının başka bir sayıyla (11, 4, 9) bölümünden kalan kurallarla hesaplanır.',tuzak='Aynı harfin iki kez geçtiğini unutmak; 11 kuralında negatif sonucu kalan sanmak.',zorluk='orta',kalip='düz',adim=3,tipId='bln-kalan-kural',kaynak='ÖSYM 2024 (xyxyx, 9 ile kalan) · ÖSYM (A34B, 5 ve 9 ile kalan) · Bilgi Sarmal'),
 dict(id='K-BLN-06',alt='Bölünebilme Kuralları',fikir='Rakamları yer değiştirmiş iki sayıdan biri bir bölene, diğeri başka bir bölene bölünür; iki durum ayrı incelenip ortak çözüm bulunur.',tuzak='Birler basamağının 0 olamayacağını (diğer sayı üç basamaklı kalmalı) gözden kaçırmak; iki durumu birden denememek.',zorluk='zor',kalip='hikâyeli',adim=4,tipId='bln-iki-sayi',kaynak='ÖSYM (AAB–ABA 9, 5 ve 12 · ABB–BAB 11 ve 12 · AB × BA ve 30) · Mert'),
 dict(id='K-BLN-07',alt='Bölünebilme',fikir='Bölünebilmeyle yeni bir sayı türü tanımlanır (rakamlar toplamına/çarpımına bölünen sayılar); tanıma uyan sayılar bir aralıkta taranır.',tuzak='0 içeren sayıları ya da sınır değerleri yanlış dahil etmek, örneği genelleştirmek.',zorluk='orta',kalip='yeni nesil',adim=3,tipId='bln-tanimli',kaynak='ÖSYM (ortakatlı sayı, n-değişmeli sayılar) · Bilgi Sarmal şema soruları'),
]
for k in KARTLAR: k['konu']=KONU; k['tip']=TAD[k['tipId']]
KS=[dict(id=k['id'],konu=k['konu'],alt=k['alt'],fikir=k['fikir'],tuzak=k['tuzak'],zorluk=k['zorluk'],kalip=k['kalip'],adim=k['adim'],tipId=k['tipId'],tip=k['tip'],kaynak=k['kaynak']) for k in KARTLAR]
TS=[dict(tipId=t,ad=a,kartlar=[k['id'] for k in KARTLAR if k['tipId']==t],uygulamaKonu=UK) for t,a in TIPLER]
json.dump(dict(konu=KONU,surum=1,kartlar=KS,tipler=TS),open(os.path.join(H,'..','kartlar',ONEK+'.json'),'w'),ensure_ascii=False,indent=1)
T=lambda t:dict(tipId=t,tip=TAD[t])

# ===== 0001 KOLAY · bln-kalan (K-BLN-01)
n=6*13+5; assert n==83 and divmod(n,8)==(10,3)
assert (6*13-5)%8==1 and (6*13)%8==6
P.R('0001',**T('bln-kalan'),zorluk='kolay',alt='Kalanlı Bölme',kazanim='Bölünen = bölen × bölüm + kalan bağıntısıyla sayıyı bulur ve başka bir bölene göre kalanı hesaplar.',kalip='hikâyeli',adim=2,
 kart='K-BLN-01 (bölüm ve kalandan sayıyı kurma) · yeni kurgu (fırında paketleme), yeni istenen (başka paket boyunda kalan)',
 metin='Bir fırında üretilen simitlerin tamamı 6’lı paketlere konulduğunda 13 paket tamamen dolmakta ve 5 simit pakete girmeden açıkta kalmaktadır.\nBu simitlerin tamamı 8’li paketlere konulursa kaç simit açıkta kalır?',
 **SK(3,{1:('islem','5 simidi eklemek yerine çıkarıp 73’ü 8’e bölmek; açıkta kalanlar toplama eklenir.'),5:('dikkat','Eski kalanı yeni kalan sanmak; bölen değişince kalan da değişir.'),
         6:('dikkat','Açıkta kalan 5 simidi unutup yalnız 78’i 8’e bölmek.'),10:('dikkat','10, dolan 8’li paket sayısı (bölüm); soru açıkta kalan simidi soruyor.')}),
 istenen='8’li paketlemede açıkta kalan simit sayısı.',
 ipuclari=['Önce toplam simit sayısını bul.','Bölünen = bölen × bölüm + kalan.','Bulduğun sayıyı 8’e böl; kalan 8’den küçük olmalı.'],bilgi=[KAL],
 adimlar=[A('Toplam simit','13 paket doldu, 5 simit açıkta kaldı. Bölünen = bölen × bölüm + kalan.','6 × 13 + 5 = 78 + 5 = 83'),
          A('8’li paketler','83’ü 8’e böl; kalan 8’den küçük olmalı.','83 = 8 × 10 + 3'),
          A('Sonuç','10 paket dolar, geriye 3 simit kalır.','kalan = 3')],
 puf='Önce bölünen = bölen × bölüm + kalan ile sayının kendisini bul, sonra yeni bölene böl.')
n=5*10+3; assert n==53 and divmod(n,12)==(4,5) and (50%12,(50-3)%12)==(2,11)
P.K('0001',metin='Bir öğretmen sınıftaki kalemleri 5’erli demetler hâlinde bağlıyor. 10 demet oluşuyor ve 3 kalem demetlere girmeden kalıyor.\nÖğretmen aynı kalemlerin hepsini 12’şerli kutulara yerleştirseydi kaç kalem kutulara girmeden kalırdı?',
 **SK(5,{2:('dikkat','Demete girmeyen 3 kalemi unutup 50’yi 12’ye bölmek.'),3:('dikkat','Eski kalanı (3) yeni kalan sanmak; bölen değişince kalan değişir.'),
         4:('dikkat','4, dolan kutu sayısı (bölüm); soru kutuya girmeyen kalemleri soruyor.'),11:('islem','3’ü eklemek yerine çıkarıp 47’yi 12’ye bölmek.')}),
 istenen='12’şerli kutulamada artan kalem sayısı.',
 ipuclari=['Kalemlerin toplam sayısını bul.','Bölünen = bölen × bölüm + kalan bağıntısını kullan.','Toplamı 12’ye böl; kalan 12’den küçüktür.'],bilgi=[KAL],
 adimlar=[A('Kalem sayısı','10 demet ve 3 artan kalem var.','5 × 10 + 3 = 53'),
          A('12’şerli kutular','53’ü 12’ye böl.','53 = 12 × 4 + 5'),
          A('Sonuç','4 kutu dolar, 5 kalem açıkta kalır.','kalan = 5')],
 puf='Bölen değişince kalanı yeniden hesapla; eski kalan yeni bölmede geçerli değildir.')

# ===== 0002 KOLAY · bln-kural (K-BLN-03)
v=[a for a in range(10) if (400+10*a+7)%3==0]; assert v==[1,4,7] and sum(v)==12
P.R('0002',**T('bln-kural'),zorluk='kolay',alt='Bölünebilme Kuralları',kazanim='3 ile bölünebilme kuralını kullanarak bilinmeyen rakamın alabileceği tüm değerleri bulur.',kalip='düz',adim=2,
 kart='K-BLN-03 (bir kuralla rakam bulma) · yeni sayı, yeni istenen (değerlerin toplamı)',
 metin='A bir rakam olmak üzere, üç basamaklı 4A7 sayısı 3 ile tam bölünebilmektedir.\nBuna göre A’nın alabileceği değerlerin toplamı kaçtır?',
 **SK(12,{3:('dikkat','3, A’nın alabileceği değer sayısı; soru değerlerin toplamını soruyor.'),5:('dikkat','Yalnız 1 ve 4’ü bulup 7’yi atlamak; rakam 9’a kadar çıkabilir.'),
          7:('bilgi','9 ile bölünebilme kuralını kullanmak (4 + A + 7 = 18); 3 için toplamın 3’ün katı olması yeter.'),18:('dikkat','18, rakamlar toplamının alabileceği en büyük değer; istenen A’nın değerleri.')}),
 istenen='A’nın alabileceği değerlerin toplamı.',
 ipuclari=['3 ile bölünebilme kuralını hatırla.','Rakamlar toplamı 11 + A; bu toplam 3’ün katı olmalı.','A, 0’dan 9’a kadar bir rakam; uyan değerlerin hepsini yaz.'],bilgi=[K3],
 adimlar=[A('Rakamlar toplamı','3 ile bölünebilme için rakamlar toplamı 3’ün katı olmalı.','4 + A + 7 = 11 + A'),
          A('Uyan değerler','11 + A ∈ {12, 15, 18} olmalı (A en çok 9).','A = 1, 4 ya da 7'),
          A('Topla','Bulunan üç değeri topla.','1 + 4 + 7 = 12')],
 puf='Bilinmeyen rakamı ararken 0’dan 9’a kadar bütün değerleri düşün; 3 ile bölünmede uyan rakamlar 3’er artar.')
v=[a for a in range(10) if (6000+100*a+20+a)%3==0]; assert v==[2,5,8] and sum(v)==15
assert [a for a in range(10) if (8+a)%3==0]==[1,4,7]
P.K('0002',metin='A bir rakam olmak üzere, dört basamaklı 6A2A sayısı 3 ile tam bölünebilmektedir.\nBuna göre A yerine yazılabilecek rakamların toplamı kaçtır?',
 **SK(15,{3:('dikkat','3, yazılabilecek rakam sayısı; soru toplamı soruyor.'),7:('dikkat','8’i atlayıp yalnız 2 ve 5’i almak.'),8:('dikkat','8, uyan rakamlardan yalnız en büyüğü.'),
          12:('islem','A’yı bir kez sayıp 8 + A toplamıyla çalışmak (1, 4, 7); A sayıda iki kez geçiyor.')}),
 istenen='A’nın alabileceği değerlerin toplamı.',
 ipuclari=['Rakamlar toplamını A cinsinden yaz; A kaç kez geçiyor?','Toplam 3’ün katı olmalı.','0’dan 9’a kadar uyan bütün rakamları bul.'],bilgi=[K3],
 adimlar=[A('Rakamlar toplamı','A sayıda iki kez geçiyor.','6 + A + 2 + A = 8 + 2A'),
          A('Uyan değerler','A’yı 0’dan 9’a kadar dene; 8 + 2A, 3’ün katı olmalı.','A = 2 ⇒ 12 ✓ · A = 5 ⇒ 18 ✓ · A = 8 ⇒ 24 ✓'),
          A('Topla','Üç değeri topla.','2 + 5 + 8 = 15')],
 puf='Harf sayıda birden fazla geçiyorsa rakamlar toplamında her geçişini ayrı say.')

# ===== 0003 ORTA · bln-kalan (K-BLN-02)
v=[n for n in range(0,3000) if n//15==2*(n%15)]; assert max(v)==434 and divmod(434,15)==(28,14) and all(n==31*(n%15) for n in v)
assert 15*28==420 and 17*14==238 and 15*30+14==464 and 31*15==465
P.R('0003',**T('bln-kalan'),zorluk='orta',alt='Kalanlı Bölme',kazanim='Bölüm ile kalan arasındaki ilişkiyi bölünen = bölen × bölüm + kalan bağıntısına taşır; kalan < bölen koşuluyla en büyük değeri bulur.',kalip='düz',adim=3,
 kart='K-BLN-02 (bölüm–kalan ilişkisi, kalan < bölen) · yeni ilişki (bölüm kalanın 2 katı), yeni istenen (en büyük sayı)',
 metin='Bir doğal sayı 15 ile bölündüğünde elde edilen bölüm, kalanın 2 katına eşittir.\nBu koşulu sağlayan en büyük doğal sayı kaçtır?',
 **SK(434,{238:('islem','Bölümle böleni karıştırıp 15 × k + 2k = 17 × 14 hesaplamak.'),420:('islem','Kalanı eklemeyi unutmak: yalnız 15 × 28.'),
           464:('dikkat','Bölümü bölenin 2 katı (30) sanmak; bölüm kalanın 2 katı.'),465:('bilgi','Kalanı 15 almak; kalan bölenden küçük olmalı, en çok 14.')}),
 istenen='Koşulu sağlayan en büyük doğal sayı.',
 ipuclari=['Kalana k dersen bölüm kaç olur?','Sayıyı bölünen = bölen × bölüm + kalan ile k cinsinden yaz.','Kalan, bölen olan 15’ten küçük olmak zorunda.'],bilgi=[KAL],
 adimlar=[A('Kalana harf ver','Kalan k ise bölüm 2k olur.','bölüm = 2k · kalan = k'),
          A('Sayıyı yaz','Bölünen = bölen × bölüm + kalan.','sayı = 15 × 2k + k = 31k'),
          A('Kalan sınırı','Kalan bölenden küçük olmalı; k en çok 14.','k ≤ 14 ⇒ sayı ≤ 31 × 14 = 434'),
          A('Kontrol','434’ü 15’e böl.','434 = 15 × 28 + 14 · 28 = 2 × 14 ✓')],
 puf='Bölümle kalan arasında ilişki varsa kalana harf ver; en büyük değeri her zaman “kalan < bölen” sınırı belirler.')
v=[n for n in range(0,3000) if n//12==3*(n%12)]; assert max(v)==407 and divmod(407,12)==(33,11)
assert 15*11==165 and 12*33==396 and 12*36+11==443 and 37*12==444
P.K('0003',metin='Bir okuldaki öğrenciler 12’şer kişilik gruplara ayrıldığında oluşan tam grup sayısı, hiçbir gruba giremeyen öğrenci sayısının 3 katı oluyor.\nBuna göre okuldaki öğrenci sayısı en çok kaçtır?',
 **SK(407,{165:('islem','Grup sayısı ile grup büyüklüğünü karıştırıp 12k + 3k = 15 × 11 hesaplamak.'),396:('islem','Gruba giremeyen 11 öğrenciyi eklemeyi unutmak: 12 × 33.'),
           443:('dikkat','Grup sayısını 12’nin 3 katı (36) sanmak; grup sayısı artan öğrencinin 3 katı.'),444:('bilgi','Artan öğrenciyi 12 almak; 12 öğrenci yeni bir grup kurar, artan en çok 11.')}),
 istenen='Okuldaki öğrenci sayısının alabileceği en büyük değer.',
 ipuclari=['Gruba giremeyen öğrenci sayısına k de.','Öğrenci sayısını 12 × grup sayısı + k biçiminde yaz.','Gruba giremeyen öğrenci sayısı en çok kaç olabilir?'],bilgi=[KAL],
 adimlar=[A('Harf ver','Artan öğrenci k ise tam grup sayısı 3k.','grup = 3k · artan = k'),
          A('Öğrenci sayısı','Bölünen = bölen × bölüm + kalan.','12 × 3k + k = 37k'),
          A('Kalan sınırı','Artan öğrenci 12’den az olmalı; yoksa bir grup daha kurulur.','k ≤ 11 ⇒ 37 × 11 = 407'),
          A('Kontrol','407’yi 12’ye böl.','407 = 12 × 33 + 11 · 33 = 3 × 11 ✓')],
 puf='Gerçek hayattaki “artan” her zaman bölenden küçüktür; en büyük değeri bu sınır verir.')

# ===== 0004 ORTA · bln-kural (K-BLN-04)
v=[(a,b) for a in range(10) for b in range(10) if (7040+100*a+b)%45==0]; assert sorted(v)==[(2,5),(7,0)] and {a+b for a,b in v}=={7}
assert 7+5==12 and 7+2==9
P.R('0004',**T('bln-kural'),zorluk='orta',alt='Bölünebilme Kuralları',kazanim='Bileşik bir bölene bölünebilmeyi aralarında asal çarpanlarına ayırarak inceler; her durumu ayrı çözer.',kalip='düz',adim=3,
 kart='K-BLN-04 (36/45 gibi bileşik bölen, iki kural birlikte) · yeni sayı (7A4B, 45), istenen her durumda aynı çıkan toplam',
 metin='A ve B birer rakam olmak üzere, dört basamaklı 7A4B sayısı 45 ile tam bölünebilmektedir.\nBuna göre A + B toplamı kaçtır?',
 **SK(7,{9:('dikkat','İki durumdaki A değerlerini (7 ve 2) toplamak; istenen A + B.'),12:('islem','B = 0 durumundaki A = 7 ile diğer durumdaki B = 5’i birlikte almak; her durum kendi içinde çözülür.'),
         16:('islem','Rakamlar toplamını 27 alıp 11 + A + B = 27 yazmak; B 0 ya da 5 iken A rakam olamaz.'),18:('islem','Rakamlar toplamı 18’i A + B sanmak; 7 ve 4’ü çıkarmayı unutmak.')}),
 istenen='A + B toplamı.',
 ipuclari=['45’i aralarında asal iki çarpana ayır.','5 ile bölünme B için hangi değerleri bırakır?','Her B değeri için 9 kuralıyla A’yı bul.'],bilgi=[K45,K3,K5],
 adimlar=[A('Böleni ayır','45 = 5 × 9 olduğundan sayı hem 5’e hem 9’a bölünmeli.','5 ⇒ B = 0 ya da B = 5'),
          A('B = 0 durumu','Rakamlar toplamı 9’un katı olmalı.','7 + A + 4 + 0 = 11 + A = 18 ⇒ A = 7'),
          A('B = 5 durumu','Aynı kural.','7 + A + 4 + 5 = 16 + A = 18 ⇒ A = 2'),
          A('Toplam','İki durumda da A + B aynı.','7 + 0 = 7 · 2 + 5 = 7')],
 puf='Bileşik bölende her çarpanın kuralını ayrı uygula; birden çok durum çıkarsa her birini sonuna kadar çöz.')
v=[(k,l) for k in range(10) for l in range(10) if (30210+1000*k+l)%36==0]; assert sorted(v)==[(1,2),(6,6)] and min(k+l for k,l in v)==3 and max(k+l for k,l in v)==12
P.K('0004',metin='K ve L birer rakam olmak üzere, beş basamaklı 3K21L sayısı 36 ile tam bölünebilmektedir.\nBuna göre K + L toplamının alabileceği en küçük değer kaçtır?',
 **SK(3,{7:('dikkat','K’nin iki değerini (1 ve 6) toplamak; istenen K + L.'),8:('dikkat','L’nin iki değerini (2 ve 6) toplamak.'),12:('dikkat','12, K + L’nin en büyük değeri; soru en küçüğü soruyor.'),
         21:('islem','Rakamlar toplamını 27 alıp 6 + K + L = 27 yazmak; bu durumda K ya da L rakam olamaz.')}),
 istenen='K + L toplamının en küçük değeri.',
 ipuclari=['36’yı aralarında asal iki çarpana ayır.','4 ile bölünme için son iki basamağa (1L) bak.','Her L değeri için 9 kuralıyla K’yi bul.'],bilgi=[K45,K3,K5],
 adimlar=[A('Böleni ayır','36 = 4 × 9; sayı hem 4’e hem 9’a bölünmeli.','4 ⇒ 1L ∈ {12, 16} ⇒ L = 2 ya da 6'),
          A('L = 2 durumu','Rakamlar toplamı 9’un katı.','3 + K + 2 + 1 + 2 = 8 + K = 9 ⇒ K = 1'),
          A('L = 6 durumu','Aynı kural.','3 + K + 2 + 1 + 6 = 12 + K = 18 ⇒ K = 6'),
          A('En küçük','K + L değerleri 3 ve 12.','en küçük K + L = 1 + 2 = 3')],
 puf='4 kuralı yalnız son iki basamağa bakar; önce o basamağı bul, sonra 9 kuralıyla diğer rakamı.')

# ===== 0005 ORTA · bln-kalan-kural (K-BLN-05)
v=[a for a in range(10) if (40306+1010*a)%9==0]; assert v==[7] and 40306+1010*7==47376 and 47376%11==10
assert (6-7+3-7+4)==-1 and [a for a in range(10) if (13+a)%9==0]==[5] and 45356%11==3 and 27%11==5
P.R('0005',**T('bln-kalan-kural'),zorluk='orta',alt='Kalan Bulma',kazanim='Bir bölünebilme koşulundan bilinmeyen rakamı bulur; sayının 11 ile bölümünden kalanı kuralla hesaplar.',kalip='düz',adim=3,
 kart='K-BLN-05 (koşuldan rakam, sonra kalan) · yeni sayı (4A3A6), yeni bölen (11 ile kalan)',
 metin='A bir rakam olmak üzere, beş basamaklı 4A3A6 sayısı 9 ile tam bölünebilmektedir.\nBuna göre bu sayının 11 ile bölümünden kalan kaçtır?',
 **SK(10,{1:('islem','Kural sonucu −1’i kalan 1 sanmak; negatif sonuca 11 eklenir.'),3:('islem','A’yı bir kez sayıp A = 5 bulmak; A sayıda iki kez geçiyor.'),
          5:('bilgi','Rakamlar toplamını (27) 11’e bölmek; 11 kuralında rakamlar sırayla + ve − alır.'),7:('dikkat','7, A’nın değeri; soru 11 ile bölümden kalanı soruyor.')}),
 istenen='4A3A6 sayısının 11 ile bölümünden kalan.',
 ipuclari=['Önce 9 kuralıyla A’yı bul; A kaç kez geçiyor?','11 ile kalan için sağdan başlayarak +, −, +, … işaretlerini ver.','Sonuç negatif çıkarsa 11 ekle.'],bilgi=[K3,K11],
 adimlar=[A('A’yı bul','Rakamlar toplamı 9’un katı olmalı; A iki kez geçiyor.','4 + A + 3 + A + 6 = 13 + 2A = 27 ⇒ A = 7'),
          A('Sayı','A = 7 yerine yazılır.','47376'),
          A('11 kuralı','Sağdan başlayarak +, −, +, −, +.','6 − 7 + 3 − 7 + 4 = −1'),
          A('Kalan','Negatif sonuca 11 eklenir.','−1 + 11 = 10')],
 puf='11 kuralında sonuç negatif çıkarsa 11 ekleyerek pozitif kalana çevir; kalan 0 ile 10 arasındadır.')
v=[b for b in range(10) if (20501+1010*b)%9==4]; assert v==[7] and 27571%11==5 and (1-7+5-7+2)==-6
assert [b for b in range(10) if (8+b)%9==4]==[5] and 25551%11==9 and 22%11==0
P.K('0005',metin='B bir rakam olmak üzere, beş basamaklı 2B5B1 sayısının 9 ile bölümünden kalan 4’tür.\nBuna göre bu sayının 11 ile bölümünden kalan kaçtır?',
 **SK(5,{0:('bilgi','Rakamlar toplamını (22) 11’e bölmek; 11 kuralında işaretler sırayla değişir.'),6:('islem','Kural sonucu −6’yı kalan 6 sanmak; negatif sonuca 11 eklenir.'),
         7:('dikkat','7, B’nin değeri; soru 11 ile bölümden kalanı soruyor.'),9:('islem','B’yi bir kez sayıp B = 5 bulmak; B sayıda iki kez geçiyor.')}),
 istenen='2B5B1 sayısının 11 ile bölümünden kalan.',
 ipuclari=['9 ile kalan, rakamlar toplamının 9 ile kalanına eşittir.','B iki kez geçiyor; rakamlar toplamını 8 + 2B olarak yaz.','11 kuralında sonuç negatifse 11 ekle.'],bilgi=[K9K,K11],
 adimlar=[A('B’yi bul','Rakamlar toplamının 9 ile kalanı 4 olmalı.','2 + B + 5 + B + 1 = 8 + 2B = 22 ⇒ B = 7'),
          A('Sayı','B = 7 yerine yazılır.','27571'),
          A('11 kuralı','Sağdan başlayarak +, −, +, −, +.','1 − 7 + 5 − 7 + 2 = −6'),
          A('Kalan','Negatif sonuca 11 eklenir.','−6 + 11 = 5')],
 puf='9 ile kalan rakamlar toplamından, 11 ile kalan işaretli toplamdan bulunur; ikisini karıştırma.')

# ===== 0006 ORTA · bln-tanimli (K-BLN-07)
assert 24%ds(24)==0
v=[n for n in range(51,70) if n%ds(n)==0]; assert v==[54,60,63] and sum(v)==177 and 50%ds(50)==0 and 70%ds(70)==0
P.R('0006',**T('bln-tanimli'),zorluk='orta',alt='Bölünebilme',kazanim='Bölünebilmeyle tanımlanan bir sayı türünü verilen aralıkta tarar; sınır değerleri doğru yorumlar.',kalip='yeni nesil',adim=3,
 kart='K-BLN-07 (bölünebilmeyle tanımlı sayı) · yeni tanım (rakamlar toplamına bölünme), yeni istenen (aralıktaki sayıların toplamı)',
 metin='Rakamları toplamına tam bölünebilen doğal sayılara “dost sayı” denir. Örneğin 24 bir dost sayıdır, çünkü 2 + 4 = 6 ve 24 sayısı 6’ya tam bölünür.\n50’den büyük ve 70’ten küçük olan dost sayıların toplamı kaçtır?',
 **SK(177,{117:('islem','60’ı atlamak; 6 + 0 = 6 ve 60, 6’ya tam bölünür.'),227:('dikkat','50’yi de eklemek; 50’den büyük sayılar isteniyor.'),
           247:('dikkat','70’i de eklemek; 70’ten küçük sayılar isteniyor.'),297:('dikkat','İki sınır değerini (50 ve 70) de eklemek.')}),
 istenen='51 ile 69 arasındaki dost sayıların toplamı.',
 ipuclari=['Aralık 51’den 69’a kadar; sınırlar dahil değil.','Her sayının rakamları toplamını bul, sayı ona bölünüyor mu bak.','Onlar basamağı 5 ve 6 olanları ayrı tara.'],bilgi=[B('Rakamları toplamı','sayının rakamları tek tek toplanır. Örnek: 63 için 6 + 3 = 9; 63 ÷ 9 = 7 tam bölünür')],
 adimlar=[A('Aralık','“Büyük” ve “küçük” sınırları dışarıda bırakır.','51, 52, …, 69'),
          A('50’li sayılar','Rakamları toplamı 6’dan 14’e kadar; yalnız 54 bölünüyor.','54: 5 + 4 = 9 · 54 = 9 × 6 ✓'),
          A('60’lı sayılar','60, 63 bölünüyor; 66’nın toplamı 12, 66 ÷ 12 tam değil.','60 = 6 × 10 ✓ · 63 = 9 × 7 ✓'),
          A('Topla','Üç dost sayıyı topla.','54 + 60 + 63 = 177')],
 puf='Tanımlı sayı sorularında aralıktaki sayıları sistemli tara ve sınır ifadelerini (büyük, küçük, en az) dikkatle oku.')
assert 12%dp(12)==0
v=[n for n in range(10,100) if '0' not in str(n) and n%dp(n)==0]; assert v==[11,12,15,24,36]
assert 22%dp(22)!=0 and [n for n in range(10,100) if '0' not in str(n) and n%dp(n)==0 and n!=11]==[12,15,24,36]
P.K('0006',metin='Rakamlarının hiçbiri 0 olmayan ve rakamlarının çarpımına tam bölünebilen doğal sayılara “çarpım dostu” sayı denir. Örneğin 12 bir çarpım dostu sayıdır, çünkü 1 × 2 = 2 ve 12 sayısı 2’ye tam bölünür.\nİki basamaklı kaç tane çarpım dostu sayı vardır?',
 **SK(5,{3:('dikkat','Yalnız örnekteki 12 ile onun katlarını (24, 36) saymak; diğer sayılar da taranmalı.'),4:('dikkat','11’i atlamak; 1 × 1 = 1 ve her sayı 1’e bölünür.'),
         6:('islem','22’yi de saymak; 2 × 2 = 4 ve 22 ÷ 4 tam değil.'),9:('bilgi','Rakamları aynı olan 11, 22, …, 99’un hepsini saymak; yalnız 11 tanıma uyar.')}),
 istenen='İki basamaklı çarpım dostu sayıların adedi.',
 ipuclari=['Onlar basamağı 1 olanlardan başla: 11, 12, …, 19.','Rakamlar çarpımı sayıdan büyükse ya da sayıyı bölmüyorsa ele.','Onlar basamağı büyüdükçe çarpım hızla büyür; 40’tan sonrası için kontrol et.'],bilgi=[B('Rakamları çarpımı','rakamlar tek tek çarpılır. Örnek: 36 için 3 × 6 = 18; 36 ÷ 18 = 2 tam bölünür')],
 adimlar=[A('10’lu sayılar','1 × B = B; sayı B’ye bölünmeli.','11 ✓ · 12 ✓ · 15 ✓ (13, 14, 16–19 bölünmez)'),
          A('20’li ve 30’lu','Çarpım 2B ve 3B; kontrol et.','24: 8 ✓ · 36: 18 ✓ · diğerleri bölünmez'),
          A('40 ve sonrası','Çarpım 4B, 5B, …; hiçbiri sayıyı tam bölmüyor.','ör. 48: 32 ✗ · 55: 25 ✗'),
          A('Say','Bulunan sayılar.','11, 12, 15, 24, 36 ⇒ 5 tane')],
 puf='Tanıma uyan sayıları ararken örnekten genelleme yapma; bütün aralığı basamak basamak tara.')

# ===== 0007 ZOR · bln-iki-sayi (K-BLN-06)
def cift(m,d1,d2):
    r=set()
    for a in range(1,10):
        for b in range(1,10):
            x=100*a+10*m+b; y=100*b+10*m+a
            if (x%d1==0 and y%d2==0) or (y%d1==0 and x%d2==0): r.add((a,b))
    return r
v=cift(7,45,8); assert v=={(5,6),(6,5)} and {a+b for a,b in v}=={11} and 675%45==0 and 576%8==0
assert [a for a in range(1,10) if (a+7+5)%9==0]==[6] and (270%45==0)
P.R('0007',**T('bln-iki-sayi'),zorluk='zor',alt='Bölünebilme Kuralları',kazanim='Rakamları yer değiştirmiş iki sayıya verilen farklı bölünebilme koşullarını durum ayırarak inceler.',kalip='hikâyeli',adim=4,
 kart='K-BLN-06 (yer değiştiren rakamlı iki sayı, biri bir bölene diğeri başka bölene) · yeni kurgu (raf numaraları), yeni bölenler (45 ve 8)',
 metin='Bir kargo deposundaki iki rafın numaraları, A ve B birer rakam olmak üzere üç basamaklı A7B ve B7A doğal sayılarıdır.\nBu numaralardan biri 45 ile, diğeri 8 ile tam bölünmektedir.\nBuna göre A + B toplamı kaçtır?',
 **SK(11,{2:('bilgi','B = 0 alıp 270’i bulmak; o zaman B7A üç basamaklı olmaz.'),8:('bilgi','45 yerine yalnız 3 ve 5’e bakıp A = 3 almak; 45 için 9 kuralı gerekir.'),
          18:('islem','Rakamlar toplamı 18’i A + B sanmak; ortadaki 7 çıkarılmalı.'),30:('dikkat','30, A × B çarpımı; soru toplamı soruyor.')}),
 istenen='A + B toplamı.',
 ipuclari=['45’e bölünen sayının birler basamağı ne olabilir? İki numara da üç basamaklı.','Önce A7B’nin 45’e bölündüğünü varsay, 9 kuralıyla diğer rakamı bul.','Bulduğun diğer numaranın 8’e bölünüp bölünmediğini kontrol et; sonra öbür durumu dene.'],bilgi=[BAS3,K45,K5],
 adimlar=[A('45’e bölünen','45 = 5 × 9. Birler basamağı 0 ya da 5; 0 olursa diğer numara 0 ile başlar, üç basamaklı olmaz.','birler basamağı = 5'),
          A('Durum 1: A7B','B = 5; rakamlar toplamı 9’un katı.','A + 7 + 5 = 18 ⇒ A = 6 · 675 = 45 × 15 ✓'),
          A('8 kontrolü','Diğer numara B7A = 576.','576 = 8 × 72 ✓'),
          A('Durum 2: B7A','A = 5 ⇒ B + 12 = 18 ⇒ B = 6; aynı iki numara çıkar.','675 ve 576'),
          A('Sonuç','Rakamlar 5 ve 6.','A + B = 11')],
 puf='“Biri …, diğeri …” sorularında iki durumu da dene ve bulduğun sayıları öbür koşulda mutlaka kontrol et.')
v=cift(2,18,5); assert v=={(2,5),(5,2)} and 522%18==0 and 225%5==0 and 252%18==0 and 252%5!=0 and 225%18!=0
assert 522-225==297 and 522+225==747
P.K('0007',metin='Bir oteldeki iki odanın numaraları, K ve L birer rakam olmak üzere üç basamaklı K2L ve L2K doğal sayılarıdır.\nBu numaralardan biri 18 ile, diğeri 5 ile tam bölünmektedir.\nBuna göre 18 ile tam bölünen oda numarası kaçtır?',
 **SK(522,{225:('dikkat','225, 5 ile bölünen numara; soru 18 ile bölüneni soruyor.'),252:('dikkat','252, 18’e bölünür ama bu durumda öbür numara da 252 olur ve 5’e bölünmez.'),
           297:('dikkat','297, iki numaranın farkı; soru numaranın kendisini soruyor.'),747:('dikkat','747, iki numaranın toplamı.')}),
 istenen='18 ile tam bölünen oda numarası.',
 ipuclari=['5’e bölünen numaranın birler basamağı ne olabilir? İki numara da üç basamaklı.','18 = 2 × 9: çift olmalı ve rakamlar toplamı 9’un katı olmalı.','Bulduğun ikiliyi iki koşulda da kontrol et.'],bilgi=[BAS3,K45,K5],
 adimlar=[A('5’e bölünen','Birler basamağı 0 olamaz (öbür numara 0 ile başlar); 5 olmalı.','5’e bölünenin birler basamağı 5'),
          A('Durum 1: K2L','L = 5 ⇒ L2K = 52K, 18’e bölünmeli: K çift ve 7 + K, 9’un katı.','7 + K = 9 ⇒ K = 2 · 522 = 18 × 29 ✓'),
          A('5 kontrolü','Öbür numara K2L = 225.','225, 5 ile biter ✓'),
          A('Durum 2: L2K','K = 5 ⇒ K2L = 52L çift ve 7 + L = 9 ⇒ L = 2; yine 522 ve 225.','aynı ikili'),
          A('Sonuç','18’e bölünen numara.','522')],
 puf='18 = 2 × 9: hem çiftlik hem 9 kuralı gerekir; tek kuralla bulduğun sayıyı diğerinde sına.')

# ===== 0008 ZOR · bln-kalan (K-BLN-02)
v=[(a,b,c) for c in range(1,30) for b in range(c+1,200) if divmod(b,c)==(3,2) for a in [6*b+5] if divmod(a,b)==(6,5)]
assert min(x[0] for x in v)==71 and min(v)==(71,11,3)
assert 6*5+5==35 and 6*8+5==53 and 6*11==66 and 6*14+5==89
P.R('0008',**T('bln-kalan'),zorluk='zor',alt='Kalanlı Bölme',kazanim='Zincirleme kalanlı bölmelerde her bölenin kalandan büyük olması koşulunu kullanarak en küçük değeri bulur.',kalip='düz',adim=4,
 kart='K-BLN-02 (zincirleme bölme, kalan < bölen) · yeni veriliş (iki bölme zinciri), yeni istenen (en küçük bölünen)',
 metin='a, b ve c pozitif tam sayılar olmak üzere\n• a sayısı b’ye bölündüğünde bölüm 6, kalan 5’tir.\n• b sayısı c’ye bölündüğünde bölüm 3, kalan 2’dir.\nBuna göre a en az kaçtır?',
 **SK(71,{35:('bilgi','c = 1 alıp b = 5 bulmak; kalan 2 iken bölen c en az 3, ayrıca kalan 5 iken b 5’ten büyük olmalı.'),53:('bilgi','c = 2 almak; kalan (2) bölenden küçük olmalı, c en az 3.'),
          66:('islem','b = 11’i bulup a = 6 × 11 hesaplamak; kalan 5 eklenmeli.'),89:('islem','c’yi 4 almak; c = 3 zaten koşulları sağlıyor ve daha küçük sonuç verir.')}),
 istenen='a’nın alabileceği en küçük değer.',
 ipuclari=['Her bölmede kalan, bölenden küçük olmalı. c için bu ne demek?','b’yi c cinsinden, a’yı b cinsinden yaz.','En küçük c ile başla; b’nin 5’ten büyük olduğunu da kontrol et.'],bilgi=[KAL],
 adimlar=[A('Bağıntılar','İki bölmeyi bölünen = bölen × bölüm + kalan ile yaz.','a = 6 × b + 5 · b = 3 × c + 2'),
          A('c’nin sınırı','b’nin c’ye bölümünden kalan 2; kalan bölenden küçük olmalı.','c > 2 ⇒ c en az 3'),
          A('b’nin değeri','c = 3 ⇒ b = 11. Ayrıca kalan 5 olduğu için b > 5 olmalı ✓.','b = 3 × 3 + 2 = 11'),
          A('a’nın değeri','a, b ile birlikte büyür; en küçük b en küçük a’yı verir.','a = 6 × 11 + 5 = 71')],
 puf='Zincirleme bölmelerde her adımda “kalan < bölen” koşulunu yaz; en küçük değeri bu koşullar belirler.')
v=[(a,b,c) for c in range(1,30) for b in range(c+1,200) if divmod(b,c)==(2,5) for a in [4*b+7] if divmod(a,b)==(4,7)]
assert min(x[0] for x in v)==75 and min(v)==(75,17,6)
assert 4*7+7==35 and 4*15+7==67 and 4*17==68
P.K('0008',metin='x, y ve z pozitif tam sayılardır.\nx sayısının y ile bölümünden bölüm 4, kalan 7; y sayısının z ile bölümünden bölüm 2, kalan 5’tir.\nBuna göre x’in alabileceği en küçük değer kaçtır?',
 **SK(75,{17:('dikkat','17, y’nin en küçük değeri; soru x’i soruyor.'),35:('bilgi','z = 1 alıp y = 7 bulmak; kalan 5 iken z en az 6, kalan 7 iken y en az 8 olmalı.'),
          67:('bilgi','z = 5 almak; kalan (5) bölenden küçük olmalı, z en az 6.'),68:('islem','y = 17’yi bulup x = 4 × 17 hesaplamak; kalan 7 eklenmeli.')}),
 istenen='x’in alabileceği en küçük değer.',
 ipuclari=['Kalan bölenden küçük olmalı: z en az kaç?','y’yi z cinsinden, x’i y cinsinden yaz.','En küçük z ile y’yi, sonra x’i bul; y’nin 7’den büyük olduğunu kontrol et.'],bilgi=[KAL],
 adimlar=[A('Bağıntılar','İki bölmeyi yaz.','x = 4 × y + 7 · y = 2 × z + 5'),
          A('z’nin sınırı','Kalan 5 olduğundan z > 5.','z en az 6'),
          A('y’nin değeri','z = 6 ⇒ y = 17; ayrıca y > 7 olmalı ✓.','y = 2 × 6 + 5 = 17'),
          A('x’in değeri','En küçük y, en küçük x’i verir.','x = 4 × 17 + 7 = 75')],
 puf='Zincirde önce en içteki bölenin alt sınırını bul, sonra dışarıya doğru hesapla.')

P.yaz(os.path.join(H,ONEK+'-1.json'),os.path.join(H,ONEK+'-1-kardes.json'))
