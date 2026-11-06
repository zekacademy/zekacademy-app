"""Mutlak Değer · parti 1: 8 ana + 8 kardeş. Her cevap ve ara sonuç kodla (tam sayı / rasyonel tarama dahil) doğrulanır."""
import sys,os,json,random
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
def sd(lo,hi,araliklar=(),noktalar=(),baslik=''):
    """Sayı doğrusu: araliklar = [(a, b, a_dahil, b_dahil)], noktalar = vurgulanan tam sayılar."""
    W=330; x0,x1,y=18,312,34; X=lambda v:x0+(float(v)-lo)/(hi-lo)*(x1-x0); b=[]
    b.append(f'<line x1="{x0-8}" y1="{y}" x2="{x1+8}" y2="{y}" stroke-width="1.2" opacity=".6"/>')
    b.append(f'<path d="M{x1+8} {y} l-6 -4 v8 z" style="fill:currentColor;stroke:none" opacity=".6"/>')
    for t in range(lo,hi+1):
        b.append(f'<line x1="{X(t):.1f}" y1="{y-4}" x2="{X(t):.1f}" y2="{y+4}" stroke-width="1" opacity=".6"/>')
        b.append(G._t(X(t),y+18,fmt(t),size=10))
    for a,c,ad,cd in araliklar:
        b.append(f'<line x1="{X(a):.1f}" y1="{y}" x2="{X(c):.1f}" y2="{y}" stroke-width="4" style="stroke:{G.ACC}" opacity=".55"/>')
        for v,d in ((a,ad),(c,cd)):
            st=f'style="stroke:{G.ACC};fill:{G.ACC}"' if d else f'style="stroke:{G.ACC};fill:none"'
            b.append(f'<circle cx="{X(v):.1f}" cy="{y}" r="4.5" stroke-width="2" {st}/>')
    for t in noktalar: b.append(f'<circle cx="{X(t):.1f}" cy="{y-11}" r="3" style="fill:{G.ACC};stroke:none"/>')
    if baslik: b.append(G._t(W/2,y+38,baslik,size=12,bold=True,renk=G.ACC))
    return G._svg(W,y+48 if baslik else y+26,''.join(b))
def kokler(f,lo=-400,hi=400,payda=6):
    """f(x) = 0 olan rasyonel x’ler (payda ≤ 6 ızgarası) — mutlak değerli birinci dereceden denklemlerin kökleri bu ızgaradadır."""
    return sorted({Fr(n,d) for d in range(1,payda+1) for n in range(lo*d,hi*d+1) if f(Fr(n,d))==0})

assert kokler(lambda x:abs(x)-2*abs(x-3))==[2,6] and kokler(lambda x:abs(x)-3*abs(x-4))==[3,6] and kokler(lambda x:abs(x-1)-3)==[-2,4] and kokler(lambda x:abs(x-3)-2)==[1,5]  # bilgi örnekleri
ONEK='mutlak'; KONU='Mutlak Değer'; UK='mat|Mutlak Değer'
P=Parti(ONEK,KONU,UK)

MD=B('Mutlak değer','|a|, a’nın 0’a uzaklığıdır ve negatif olmaz. a ≥ 0 ise |a| = a, a < 0 ise |a| = −a. Örnek: |−5| = 5, |3| = 3')
MDD=B('Mutlak değerli denklem','|ifade| = k (k > 0) ise ifade = k ya da ifade = −k. Örnek: |x − 1| = 3 ⇒ x = 4 ya da x = −2')
MDE=B('Mutlak değerli eşitsizlik','|ifade| ≤ k ⇒ −k ≤ ifade ≤ k. |ifade| > k ⇒ ifade > k ya da ifade < −k. Örnek: |x| < 2 ⇒ −2 < x < 2')
UZ=B('Uzaklık olarak mutlak değer','|x − a|, sayı doğrusunda x ile a arasındaki uzaklıktır; |x + a| = |x − (−a)|. Örnek: |x − 3| = 2 ⇒ x = 1 ya da x = 5')
MERK=B('Aralığı mutlak değerle yazma','m ≤ x ≤ M ⇒ |x − merkez| ≤ yarıçap; merkez = (m + M) ÷ 2, yarıçap = (M − m) ÷ 2. Örnek: 2 ≤ x ≤ 8 ⇒ |x − 5| ≤ 3')

# ---------- kartlar ve tipler ----------
TIPLER=[('mtd-denklem','Mutlak değerli denklemler'),('mtd-esitsizlik','Mutlak değerli eşitsizlikler'),('mtd-ifade','İşarete göre mutlak değer açma'),
        ('mtd-model','Aralığı mutlak değerle ifade etme'),('mtd-uzaklik','Uzaklık ve tahmin problemleri')]
TAD=dict(TIPLER)
KARTLAR=[
 dict(id='K-MTD-01',alt='Mutlak Değerli Denklemler',fikir='|ax + b| = k denkleminde içerisi k ya da −k yapılır; iki kök bulunur, toplamı ya da çarpımı istenir. İki mutlak değerin toplamında bölge ayrılır.',tuzak='Yalnız pozitif durumu çözmek; −k durumunda işaret hatası; bölge dışında kalan kökü kontrol etmemek.',zorluk='kolay',kalip='düz',adim=2,tipId='mtd-denklem',kaynak='ÖSYM (Mutlak Değerli Denklemler) · 3D (|x − 4| + |4 − x| = 8) · 345 SB'),
 dict(id='K-MTD-02',alt='Mutlak Değerli Denklemler',fikir='|x − a| + |x − b| = |a − b| eşitliği sayı doğrusunda a ile b arasındaki bütün noktalar için sağlanır; çözüm bir aralıktır, tam sayılar sayılır.',tuzak='Yalnız uç noktaları çözüm sanmak; aralık uzunluğunu nokta sayısı sanmak.',zorluk='zor',kalip='düz',adim=4,tipId='mtd-denklem',kaynak='ÖSYM (Mutlak Değer Kavramı ve Özellikleri) · 3D, Bilgi Sarmal'),
 dict(id='K-MTD-03',alt='Mutlak Değerli Eşitsizlikler',fikir='|x − a| ≤ k ya da k₁ < |x − a| ≤ k₂ çözülür; çözüm bir ya da iki aralıktır, tam sayılar sayılır ya da toplanır.',tuzak='Yalnız içerisi pozitif olan tarafı çözmek; < ile ≤ uçlarını karıştırmak; çift taraflıda iç aralığı dahil etmek.',zorluk='kolay',kalip='düz',adim=2,tipId='mtd-esitsizlik',kaynak='ÖSYM (|SA + 1| < 5, |x − 4| < 3 gol farkı) · 345 SB, Bilgi Sarmal'),
 dict(id='K-MTD-04',alt='Mutlak Değer',fikir='Sayıların sıralaması/işareti verilir; mutlak değerlerin içinin işareti belirlenip ifade sadeleştirilir.',tuzak='Negatif içerikli mutlak değeri olduğu gibi açmak; önündeki eksiyi tüm terimlere dağıtmamak.',zorluk='orta',kalip='düz',adim=3,tipId='mtd-ifade',kaynak='ÖSYM (Mutlak Değer Kavramı) · 345 SB (a < 0 olmak üzere …) · Bilgi Sarmal (|a| > |c|)'),
 dict(id='K-MTD-05',alt='Mutlak Değerli Eşitsizlikler',fikir='Gerçek hayattaki “a ila b arasında” bilgisi önce kaydırma/ekleme ile istenen niceliğe çevrilir, sonra |x − merkez| ≤ yarıçap biçiminde yazılır.',tuzak='Kaydırmayı unutmak ya da ters yöne yapmak; yarıçap yerine aralık uzunluğunu almak; uçların dahil olup olmadığını karıştırmak.',zorluk='orta',kalip='hikâyeli',adim=3,tipId='mtd-model',kaynak='ÖSYM (sıcaklık 6 ila 10 derece artış, paraşüt 400 ila 500 m, otoyol şeritleri)'),
 dict(id='K-MTD-06',alt='Mutlak Değer',fikir='Bilinmeyen bir sayının iki tahmine uzaklıkları arasında oran verilir; |n − a| = k × |n − b| iki duruma ayrılarak çözülür.',tuzak='İki çözümden birini atlamak; oranı ters kurmak; toplam yerine fark vermek.',zorluk='zor',kalip='hikâyeli',adim=4,tipId='mtd-uzaklik',kaynak='ÖSYM (dergi sayfa sayısı tahminleri, mutlak farklar) · Mert'),
]
for k in KARTLAR: k['konu']=KONU; k['tip']=TAD[k['tipId']]
KS=[dict(id=k['id'],konu=k['konu'],alt=k['alt'],fikir=k['fikir'],tuzak=k['tuzak'],zorluk=k['zorluk'],kalip=k['kalip'],adim=k['adim'],tipId=k['tipId'],tip=k['tip'],kaynak=k['kaynak']) for k in KARTLAR]
TS=[dict(tipId=t,ad=a,kartlar=[k['id'] for k in KARTLAR if k['tipId']==t],uygulamaKonu=UK) for t,a in TIPLER]
json.dump(dict(konu=KONU,surum=1,kartlar=KS,tipler=TS),open(os.path.join(H,'..','kartlar',ONEK+'.json'),'w'),ensure_ascii=False,indent=1)
T=lambda t:dict(tipId=t,tip=TAD[t])
Z=range(-300,301)
random.seed(61126)

# ===== 0001 KOLAY · mtd-denklem (K-MTD-01)
k=kokler(lambda x:abs(2*x-5)-7); assert k==[-1,6] and sum(k)==5 and -1*6==-6 and 6+1==7 and 12+(-2)==10
P.R('0001',**T('mtd-denklem'),zorluk='kolay',alt='Mutlak Değerli Denklemler',kazanim='|ax + b| = k denklemini iki duruma ayırarak çözer ve köklerin toplamını bulur.',kalip='düz',adim=2,
 kart='K-MTD-01 (|ax + b| = k, iki durum) · yeni denklem, istenen köklerin toplamı',
 metin='|2x − 5| = 7\ndenklemini sağlayan x değerlerinin toplamı kaçtır?',
 **SK(5,{-6:('dikkat','Kökleri çarpmak: 6 × (−1); soru toplamı soruyor.'),6:('bilgi','Yalnız 2x − 5 = 7 durumunu çözmek; içerisi −7 de olabilir.'),
         7:('islem','2x − 5 = −7’den x = 1 bulmak; doğrusu 2x = −2, x = −1.'),10:('islem','2’ye bölmeyi unutup 2x değerlerini (12 ve −2) toplamak.')}),
 istenen='Denklemi sağlayan x değerlerinin toplamı.',
 ipuclari=['Mutlak değeri 7 olan sayılar hangileridir?','İçerideki ifade 7’ye ya da −7’ye eşit olmalı; iki denklemi ayrı ayrı çöz.','Bulduğun iki değeri topla.'],bilgi=[MD,MDD],
 adimlar=[A('İki durum','Mutlak değeri 7 olan sayılar 7 ve −7.','2x − 5 = 7 ya da 2x − 5 = −7'),
          A('Çöz','Her denklemde 5 ekle, 2’ye böl.','2x = 12 ⇒ x = 6 · 2x = −2 ⇒ x = −1'),
          A('Topla','İki kökü topla.','6 + (−1) = 5')],
 puf='|ifade| = k (k > 0) her zaman iki denklem verir: ifade = k ve ifade = −k.')
k=kokler(lambda x:abs(2*x+3)-9); assert k==[-6,3] and sum(k)==-3 and -6*3==-18
P.K('0001',metin='x bir gerçel sayı olmak üzere\n|2x + 3| = 9\neşitliğini sağlayan x’lerin toplamı kaçtır?',
 **SK(-3,{-18:('dikkat','Kökleri çarpmak: 3 × (−6); soru toplamı soruyor.'),-6:('bilgi','Yalnız 2x + 3 = −9 durumunu çözmek; içerisi 9 da olabilir.'),
          0:('islem','2x + 3 = −9’dan x = −3 bulmak; doğrusu 2x = −12, x = −6.'),3:('bilgi','Yalnız 2x + 3 = 9 durumunu çözmek; içerisi −9 da olabilir.')}),
 istenen='Eşitliği sağlayan x değerlerinin toplamı.',
 ipuclari=['İçerisi hangi iki sayıya eşit olabilir?','İki denklemi ayrı ayrı çöz.','Kökleri topla.'],bilgi=[MD,MDD],
 adimlar=[A('İki durum','Mutlak değeri 9 olan sayılar 9 ve −9.','2x + 3 = 9 ya da 2x + 3 = −9'),
          A('Çöz','Her denklemde 3 çıkar, 2’ye böl.','2x = 6 ⇒ x = 3 · 2x = −12 ⇒ x = −6'),
          A('Topla','İki kökü topla.','3 + (−6) = −3')],
 puf='Negatif durumu çözerken sabit terimi doğru yöne taşı: 2x + 3 = −9 ⇒ 2x = −12.')

# ===== 0002 KOLAY · mtd-esitsizlik (K-MTD-03)
v=[x for x in Z if abs(x-4)<=3]; assert v==list(range(1,8)) and len(v)==7 and len(range(4,8))==4 and len(range(-3,8))==11
P.R('0002',**T('mtd-esitsizlik'),zorluk='kolay',alt='Mutlak Değerli Eşitsizlikler',kazanim='|x − a| ≤ k eşitsizliğini çift taraflı eşitsizliğe çevirip tam sayı çözümleri sayar.',kalip='düz',adim=2,
 kart='K-MTD-03 (|x − a| ≤ k) · yeni sayılar, istenen tam sayı çözüm sayısı',
 metin='|x − 4| ≤ 3\neşitsizliğini sağlayan kaç tane x tam sayısı vardır?',
 **SK(7,{4:('dikkat','Yalnız x ≥ 4 tarafını (4, 5, 6, 7) saymak; 4’ün solundaki sayılar da sağlar.'),5:('bilgi','Uçları (1 ve 7) almamak; ≤ işareti uçları da kapsar.'),
         6:('islem','Uçlardan birini atlamak; 1’den 7’ye kadar 7 tam sayı var.'),11:('islem','Sol uçta 4 eklemeyi unutup −3 ≤ x ≤ 7 yazmak.')}),
 istenen='Eşitsizliği sağlayan tam sayıların adedi.',
 ipuclari=['|ifade| ≤ 3 ise ifade hangi aralıktadır?','−3 ≤ x − 4 ≤ 3 eşitsizliğinin her tarafına 4 ekle.','Uçlar dahil; tam sayıları say.'],bilgi=[MDE,UZ],
 adimlar=[A('Çift taraflıya çevir','Mutlak değeri 3’ten büyük olmayan sayılar −3 ile 3 arasındadır.','−3 ≤ x − 4 ≤ 3'),
          A('4 ekle','Her tarafa 4 eklenir.','1 ≤ x ≤ 7',sd(0,8,[(1,7,True,True)],list(range(1,8)),'4’e uzaklığı en çok 3')),
          A('Say','1’den 7’ye kadar tam sayılar.','7 − 1 + 1 = 7')],
 puf='|x − a| ≤ k, “x’in a’ya uzaklığı en çok k” demektir: a − k ≤ x ≤ a + k.')
v=[x for x in Z if abs(x+1)<5]; assert v==list(range(-5,4)) and len(v)==9 and len(range(-1,4))==5 and len(range(-3,4))==7 and len(range(-6,5))==11
P.K('0002',metin='x bir tam sayı olmak üzere\n|x + 1| < 5\nolduğuna göre x kaç farklı değer alabilir?',
 **SK(9,{5:('dikkat','Yalnız x ≥ −1 tarafını (−1, 0, 1, 2, 3) saymak.'),7:('islem','Sol uçta 1 çıkarmak yerine ekleyip −4 < x < 4 yazmak.'),
         10:('bilgi','Uçlardan birini (−6 ya da 4) dahil etmek; < kesin eşitsizlik.'),11:('bilgi','İki ucu da dahil etmek; < işaretinde uçlar alınmaz.')}),
 istenen='x’in alabileceği tam sayı değerlerinin adedi.',
 ipuclari=['|ifade| < 5 ise ifade hangi aralıktadır?','Her taraftan 1 çıkar.','Uçlar dahil değil; aradaki tam sayıları say.'],bilgi=[MDE,UZ],
 adimlar=[A('Çift taraflıya çevir','Mutlak değeri 5’ten küçük sayılar.','−5 < x + 1 < 5'),
          A('1 çıkar','Her taraftan 1 çıkarılır.','−6 < x < 4',sd(-7,5,[(-6,4,False,False)],list(range(-5,4)))),
          A('Say','−5’ten 3’e kadar tam sayılar.','3 − (−5) + 1 = 9')],
 puf='Kesin eşitsizlikte (<) uçlar sayılmaz; −6 < x < 4 için −5, …, 3 alınır.')

# ===== 0003 ORTA · mtd-ifade (K-MTD-04)
def rpos(): return Fr(random.randint(1,500),random.randint(1,12))
E3={'2b − 2a':lambda a,b:2*b-2*a,'0':lambda a,b:0,'2b':lambda a,b:2*b,'2a − 2b':lambda a,b:2*a-2*b,'2b − 4a':lambda a,b:2*b-4*a}
O=[(-rpos(),rpos()) for _ in range(3000)]
f3=lambda a,b:abs(a-b)+abs(b-2*a)-abs(a)
dogru=[k for k,g in E3.items() if all(f3(a,b)==g(a,b) for a,b in O)]; assert dogru==['2b − 2a']
for a,b in O[:50]: assert (a-b)+(b-2*a)+a==0 and (b+a)+(b-2*a)+a==2*b and (b-a)+(b-2*a)-a==2*b-4*a
P.R('0003',**T('mtd-ifade'),zorluk='orta',alt='Mutlak Değer',kazanim='Sayıların işaretinden mutlak değerlerin içinin işaretini belirler ve ifadeyi sadeleştirir.',kalip='düz',adim=3,
 kart='K-MTD-04 (işarete göre mutlak değer açma) · yeni ifade (üç mutlak değer), istenen sadeleşmiş hâl',
 metin='a < 0 < b olmak üzere\n|a − b| + |b − 2a| − |a|\nifadesinin eşiti aşağıdakilerden hangisidir?',
 **SK('2b − 2a',{'0':('islem','|a − b|’yi a − b olarak açmak; a − b negatif olduğundan |a − b| = b − a.'),'2b':('islem','|a − b|’yi b + a sanmak; doğrusu b − a.'),
                 '2a − 2b':('islem','Bütün mutlak değerleri ters işaretle açmak; b − 2a pozitif olduğu için olduğu gibi çıkar.'),'2b − 4a':('bilgi','|a|’yı a almak; a negatif olduğundan |a| = −a.')},
    sira=['0','2b','2a − 2b','2b − 4a','2b − 2a']),
 istenen='İfadenin sadeleşmiş hâli.',
 ipuclari=['Her mutlak değerin içinin işaretini belirle; a negatif, b pozitif.','İçi negatif olanı −1 ile çarparak dışarı çıkar.','Terimleri topla; |a|’nın önündeki eksiyi unutma.'],bilgi=[MD],
 adimlar=[A('İçlerin işareti','a negatif, b pozitif: a − b negatif; b − 2a = b + (pozitif), pozitif; a negatif.','a − b < 0 · b − 2a > 0 · a < 0'),
          A('Mutlak değerleri aç','İçi negatif olan −1 ile çarpılır.','|a − b| = b − a · |b − 2a| = b − 2a · |a| = −a'),
          A('Birleştir','Terimleri topla.','(b − a) + (b − 2a) − (−a) = 2b − 2a')],
 puf='Mutlak değeri açmadan önce her zaman içinin işaretini belirle; negatifse ters işaretle çıkar.')
E3k={'−y − 2x':lambda x,y:-y-2*x,'−3y':lambda x,y:-3*y,'−y − 4x':lambda x,y:-y-4*x,'2x − y':lambda x,y:2*x-y,'3y − 4x':lambda x,y:3*y-4*x}
O=[(-rpos(),rpos()) for _ in range(3000)]
f3k=lambda x,y:abs(y-x)-abs(x-2*y)+abs(2*x)
dogru=[k for k,g in E3k.items() if all(f3k(x,y)==g(x,y) for x,y in O)]; assert dogru==['−y − 2x']
for x,y in O[:50]: assert (x-y)-(2*y-x)-2*x==-3*y and (y-x)-2*y-x-2*x==-y-4*x and (y-x)-(2*y-x)+2*x==2*x-y and (y-x)-(x-2*y)-2*x==3*y-4*x
P.K('0003',metin='x < 0 < y olmak üzere\n|y − x| − |x − 2y| + |2x|\nifadesi aşağıdakilerden hangisine eşittir?',
 **SK('−y − 2x',{'−3y':('islem','|y − x|’i x − y açmak; y − x pozitif olduğundan olduğu gibi çıkar.'),'−y − 4x':('islem','Mutlak değerin önündeki eksiyi yalnız ilk terime dağıtıp −2y − x yazmak; doğrusu −(2y − x) = −2y + x.'),
                 '2x − y':('bilgi','|2x|’i 2x almak; x negatif olduğundan |2x| = −2x.'),'3y − 4x':('islem','|x − 2y|’yi x − 2y açmak; içi negatif olduğundan 2y − x olmalı.')},
    sira=['−3y','−y − 4x','−y − 2x','2x − y','3y − 4x']),
 istenen='İfadenin eşiti.',
 ipuclari=['x negatif, y pozitif; her mutlak değerin içi hangi işaretli?','İçi negatif olanları ters işaretle çıkar.','Ortadaki mutlak değerin önünde eksi var; parantez kullan.'],bilgi=[MD],
 adimlar=[A('İçlerin işareti','y − x pozitif; x − 2y negatif; 2x negatif.','y − x > 0 · x − 2y < 0 · 2x < 0'),
          A('Mutlak değerleri aç','İçi negatif olan ters işaretle çıkar.','|y − x| = y − x · |x − 2y| = 2y − x · |2x| = −2x'),
          A('Birleştir','Eksiyi parantezin tamamına dağıt.','(y − x) − (2y − x) + (−2x) = −y − 2x')],
 puf='Önünde eksi olan mutlak değeri açarken sonucu paranteze al, eksiyi her terime dağıt.')

# ===== 0004 ORTA · mtd-model (K-MTD-05)
X4=[Fr(i,4) for i in range(0,161)]
ist=[x for x in X4 if 15<=x-2<=21]; assert ist[0]==17 and ist[-1]==23
M4={'|x − 20| ≤ 3':lambda x:abs(x-20)<=3,'|x − 20| < 3':lambda x:abs(x-20)<3,'|x − 20| ≤ 6':lambda x:abs(x-20)<=6,'|x − 18| ≤ 3':lambda x:abs(x-18)<=3,'|x − 17| ≤ 6':lambda x:abs(x-17)<=6}
dogru=[k for k,g in M4.items() if [x for x in X4 if g(x)]==ist]; assert dogru==['|x − 20| ≤ 3'] and (17+23)/2==20 and (23-17)/2==3
P.R('0004',**T('mtd-model'),zorluk='orta',alt='Mutlak Değerli Eşitsizlikler',kazanim='Gerçek hayattaki bir aralık bilgisini dönüştürüp |x − merkez| ≤ yarıçap biçiminde yazar.',kalip='hikâyeli',adim=3,
 kart='K-MTD-05 (aralığı mutlak değerle ifade) · yeni kurgu (kargo paketi ve ambalaj), kaydırma adımı',
 metin='Bir kargo şirketi, içindeki ürünün kütlesi 15 kg ile 21 kg arasında olan paketleri (15 kg ve 21 kg dahil) “orta boy” olarak sınıflandırmaktadır. Her pakette ürünün dışında 2 kg’lık bir ambalaj bulunmaktadır.\nOrta boy bir paketin ambalajıyla birlikte kütlesi x kg olduğuna göre x’in alabileceği değerler aşağıdaki eşitsizliklerden hangisiyle gösterilir?',
 **SK('|x − 20| ≤ 3',{'|x − 20| < 3':('dikkat','Uçları dışarıda bırakmak; 17 kg ve 23 kg dahil.'),'|x − 20| ≤ 6':('bilgi','Yarıçap yerine aralığın tamamını (6) almak; bu 14 ≤ x ≤ 26 olur.'),
                     '|x − 18| ≤ 3':('dikkat','2 kg’lık ambalajı eklememek; 15–21 aralığının merkezi 18.'),'|x − 17| ≤ 6':('bilgi','Sol ucu merkez, aralık uzunluğunu yarıçap almak; bu 11 ≤ x ≤ 23 olur.')},
    sira=['|x − 20| ≤ 3','|x − 20| < 3','|x − 20| ≤ 6','|x − 18| ≤ 3','|x − 17| ≤ 6']),
 istenen='Toplam kütle x’in aralığını gösteren mutlak değerli eşitsizlik.',
 ipuclari=['Önce toplam kütlenin (ürün + ambalaj) aralığını bul.','Aralığın orta noktası ve orta noktadan uçlara uzaklık kaç?','Uçlar dahil mi? ≤ mı, < mı kullanılmalı?'],bilgi=[MERK],
 adimlar=[A('Toplam kütle','Ürün kütlesine 2 kg eklenir.','15 + 2 ≤ x ≤ 21 + 2 ⇒ 17 ≤ x ≤ 23'),
          A('Merkez ve yarıçap','Merkez aralığın ortası, yarıçap ortadan uca uzaklık.','merkez = (17 + 23) ÷ 2 = 20 · yarıçap = (23 − 17) ÷ 2 = 3'),
          A('Eşitsizlik','Uçlar dahil olduğundan ≤.','|x − 20| ≤ 3',sd(15,25,[(17,23,True,True)],[],'20’ye uzaklığı en çok 3'))],
 puf='“a ile b arasında” bilgisini önce istenen niceliğe çevir; sonra merkez ve yarıçapı bul.')
X4=[Fr(i,2) for i in range(200,500)]
ist=[x for x in X4 if 170<=x+10<=190]; assert ist[0]==160 and ist[-1]==180
M4={'|x − 160| ≤ 20':lambda x:abs(x-160)<=20,'|x − 170| ≤ 10':lambda x:abs(x-170)<=10,'|x − 170| ≤ 20':lambda x:abs(x-170)<=20,'|x − 180| ≤ 10':lambda x:abs(x-180)<=10,'|x − 190| ≤ 10':lambda x:abs(x-190)<=10}
dogru=[k for k,g in M4.items() if [x for x in X4 if g(x)]==ist]; assert dogru==['|x − 170| ≤ 10']
P.K('0004',metin='Bir fırının ekranı, fırının içindeki gerçek sıcaklığı her zaman 10 °C fazla göstermektedir. Bir kek tarifine göre pişirme boyunca ekranda görünen sıcaklık 170 °C ile 190 °C arasında (iki değer de dahil) olmalıdır.\nFırının içindeki gerçek sıcaklık x °C olduğuna göre x’in alabileceği değerler aşağıdakilerden hangisiyle ifade edilir?',
 **SK('|x − 170| ≤ 10',{'|x − 160| ≤ 20':('bilgi','Sol ucu merkez, aralık uzunluğunu yarıçap almak; bu 140 ≤ x ≤ 180 olur.'),'|x − 170| ≤ 20':('bilgi','Yarıçap yerine aralığın tamamını (20) almak.'),
                       '|x − 180| ≤ 10':('dikkat','Ekrandaki aralığın merkezini (180) almak; gerçek sıcaklık ekrandakinden 10 °C düşük.'),'|x − 190| ≤ 10':('islem','10 °C’yi çıkarmak yerine eklemek: 180–200 aralığı.')},
    sira=['|x − 160| ≤ 20','|x − 170| ≤ 10','|x − 170| ≤ 20','|x − 180| ≤ 10','|x − 190| ≤ 10']),
 istenen='Gerçek sıcaklığın aralığını gösteren eşitsizlik.',
 ipuclari=['Ekran 10 °C fazla gösteriyorsa gerçek sıcaklık ekrandakinden kaç fazla ya da eksiktir?','Gerçek sıcaklığın aralığını yaz.','Aralığın ortasını ve ortadan uca uzaklığı bul.'],bilgi=[MERK],
 adimlar=[A('Gerçek sıcaklık','Ekran = gerçek + 10; gerçek = ekran − 10.','170 − 10 ≤ x ≤ 190 − 10 ⇒ 160 ≤ x ≤ 180'),
          A('Merkez ve yarıçap','Ortası ve ortadan uca uzaklık.','merkez = (160 + 180) ÷ 2 = 170 · yarıçap = 10'),
          A('Eşitsizlik','Uçlar dahil.','|x − 170| ≤ 10')],
 puf='Ölçüm aleti sabit bir miktar fazla gösteriyorsa önce aralığı düzelt, sonra mutlak değerle yaz.')

# ===== 0005 ORTA · mtd-denklem (K-MTD-01)
k=kokler(lambda x:abs(x-3)+abs(x+1)-6); assert k==[-2,4] and sum(k)==2 and -2*4==-8
assert all(abs(x-3)+abs(x+1)==4 for x in [Fr(i,4) for i in range(-4,13)]) and Fr(-4)+4==0
P.R('0005',**T('mtd-denklem'),zorluk='orta',alt='Mutlak Değerli Denklemler',kazanim='İki mutlak değerin toplamını içeren denklemi bölgelere ayırarak çözer.',kalip='düz',adim=3,
 kart='K-MTD-01 (mutlak değerli denklem) · iki mutlak değerin toplamı, bölge ayırma',
 metin='|x − 3| + |x + 1| = 6\ndenkleminin çözüm kümesindeki elemanların toplamı kaçtır?',
 **SK(2,{-8:('dikkat','Kökleri çarpmak: 4 × (−2); soru toplamı soruyor.'),-2:('dikkat','Yalnız x < −1 bölgesindeki kökü almak; x ≥ 3 bölgesinde de kök var.'),
         0:('islem','x < −1 bölgesinde −(x − 3) yerine −x − 3 yazıp x = −4 bulmak.'),4:('dikkat','Yalnız x ≥ 3 bölgesindeki kökü almak; x < −1 bölgesinde de kök var.')}),
 istenen='Denklemi sağlayan x değerlerinin toplamı.',
 ipuclari=['Mutlak değerlerin içini sıfır yapan değerler −1 ve 3; sayı doğrusunu üç bölgeye ayır.','Her bölgede mutlak değerleri işaretlerine göre aç.','−1 ile 3 arasında ifade sabit bir sayı olur; 6’ya eşit mi?'],bilgi=[MD,UZ],
 adimlar=[A('x ≥ 3','İki iç de pozitif.','(x − 3) + (x + 1) = 2x − 2 = 6 ⇒ x = 4 ✓'),
          A('−1 ≤ x < 3','x − 3 negatif, x + 1 pozitif.','(3 − x) + (x + 1) = 4 ≠ 6 ⇒ kök yok'),
          A('x < −1','İki iç de negatif.','(3 − x) − (x + 1) = 2 − 2x = 6 ⇒ x = −2 ✓'),
          A('Topla','İki kökü topla.','4 + (−2) = 2')],
 puf='İki mutlak değerin toplamında içleri sıfırlayan noktalarla sayı doğrusunu bölgelere ayır; her bölgede bulduğun kökün o bölgede olduğunu kontrol et.')
k=kokler(lambda x:abs(x+5)+abs(x-1)-10); assert k==[-7,3] and sum(k)==-4 and -7*3==-21 and 3+(-2)==1
P.K('0005',metin='|x + 5| + |x − 1| = 10\neşitliğini sağlayan x gerçel sayılarının toplamı kaçtır?',
 **SK(-4,{-21:('dikkat','Kökleri çarpmak: 3 × (−7); soru toplamı soruyor.'),-7:('dikkat','Yalnız x < −5 bölgesindeki kökü almak.'),
          1:('islem','x < −5 bölgesinde −(x + 5) yerine −x + 5 yazıp x = −2 bulmak; ayrıca −2 bu bölgede değil.'),3:('dikkat','Yalnız x ≥ 1 bölgesindeki kökü almak.')}),
 istenen='Eşitliği sağlayan x değerlerinin toplamı.',
 ipuclari=['İçleri sıfır yapan değerler −5 ve 1.','Üç bölgede ayrı ayrı çöz.','−5 ile 1 arasında ifade hep 6’dır.'],bilgi=[MD,UZ],
 adimlar=[A('x ≥ 1','İki iç de pozitif.','(x + 5) + (x − 1) = 2x + 4 = 10 ⇒ x = 3 ✓'),
          A('−5 ≤ x < 1','İlki pozitif, ikincisi negatif.','(x + 5) + (1 − x) = 6 ≠ 10 ⇒ kök yok'),
          A('x < −5','İki iç de negatif.','−(x + 5) + (1 − x) = −2x − 4 = 10 ⇒ x = −7 ✓'),
          A('Topla','Kökleri topla.','3 + (−7) = −4')],
 puf='Bulduğun kökü mutlaka bölgesine geri koy; bölge dışındaki değer çözüm değildir.')

# ===== 0006 ORTA · mtd-esitsizlik (K-MTD-03)
v=[x for x in Z if 1<abs(x+2)<=4]; assert v==[-6,-5,-4,0,1,2] and sum(v)==-12 and sum(v)-3-1==-16 and sum(v)-3==-15 and 0+1+2==3 and len(v)==6
P.R('0006',**T('mtd-esitsizlik'),zorluk='orta',alt='Mutlak Değerli Eşitsizlikler',kazanim='Çift taraflı mutlak değerli eşitsizliği iki aralığa ayırarak çözer; tam sayı çözümlerin toplamını bulur.',kalip='düz',adim=3,
 kart='K-MTD-03 (k₁ < |x − a| ≤ k₂) · iki aralıklı çözüm, istenen tam sayıların toplamı',
 metin='x tam sayısı için\n1 < |x + 2| ≤ 4\neşitsizliği sağlandığına göre x’in alabileceği değerlerin toplamı kaçtır?',
 **SK(-12,{-16:('bilgi','−3 ve −1’i de almak; bu değerlerde |x + 2| = 1 olur ve 1 > 1 sağlanmaz.'),-15:('bilgi','−3’ü de almak; |−3 + 2| = 1 ve 1 < 1 kesin eşitsizliği sağlamaz.'),
           3:('dikkat','Yalnız x + 2 > 0 tarafını (0, 1, 2) çözmek; negatif taraf da çözüm verir.'),6:('dikkat','6, çözüm olan tam sayıların sayısı; soru toplamı soruyor.')}),
 istenen='Eşitsizliği sağlayan tam sayıların toplamı.',
 ipuclari=['x + 2 için iki durum var: pozitif tarafta 1 < x + 2 ≤ 4, negatif tarafta −4 ≤ x + 2 < −1.','Her durumda her taraftan 2 çıkar.','Uçlara dikkat ederek tam sayıları yaz ve topla.'],bilgi=[MDE,UZ],
 adimlar=[A('İki parça','Mutlak değeri 1’den büyük, 4’ten büyük olmayan sayılar iki parçadadır.','1 < x + 2 ≤ 4 · −4 ≤ x + 2 < −1'),
          A('2 çıkar','Her parçada her taraftan 2 çıkar.','−1 < x ≤ 2 · −6 ≤ x < −3',sd(-7,3,[(-6,-3,True,False),(-1,2,False,True)],[-6,-5,-4,0,1,2])),
          A('Tam sayılar','İki parçadaki tam sayılar.','−6, −5, −4 · 0, 1, 2'),
          A('Topla','Hepsini topla.','−15 + 3 = −12')],
 puf='a < |ifade| ≤ b iki ayrı aralık verir; −2’nin sağına ve soluna simetrik bak.')
v=[x for x in Z if 2<=abs(x-3)<5]; assert v==[-1,0,1,5,6,7] and len(v)==6 and len([x for x in Z if abs(x-3)<5])==9 and sum(v)==18
assert len([x for x in Z if 2<=abs(x-3)<=5])==8 and len([x for x in Z if 2<=abs(x-3)<5 or x==8])==7
P.K('0006',metin='Sayı doğrusunda 3’e olan uzaklığı en az 2 birim, ancak 5 birimden az olan tam sayıların hepsi işaretlenmiştir.\nBuna göre kaç tam sayı işaretlenmiştir?',
 **SK(6,{7:('bilgi','Uçlardan birini (−2 ya da 8) dahil etmek; |x − 3| < 5 kesin eşitsizlik.'),8:('bilgi','İki ucu da (−2 ve 8) dahil etmek; bu değerlerde |x − 3| = 5 olur.'),
         9:('dikkat','“En az 2 birim” koşulunu unutup yalnız |x − 3| < 5’i çözmek.'),18:('dikkat','18, çözümlerin toplamı; soru kaç tam sayı olduğunu soruyor.')}),
 istenen='İşaretlenen tam sayıların adedi.',
 ipuclari=['x’in 3’e uzaklığını mutlak değerle yaz: 2 ≤ |x − 3| < 5.','Her parçaya 3 ekle.','≤ ve < uçlarına dikkat ederek tam sayıları say.'],bilgi=[MDE,UZ],
 adimlar=[A('Mutlak değerle yaz','x’in 3’e uzaklığı |x − 3|; en az 2, 5’ten az.','2 ≤ |x − 3| < 5'),
          A('İki parça','x − 3 ya 2 ile 5 arasında ya da −5 ile −2 arasında.','2 ≤ x − 3 < 5 · −5 < x − 3 ≤ −2'),
          A('3 ekle','Her parçaya 3 ekle.','5 ≤ x < 8 · −2 < x ≤ 1',sd(-3,9,[(-2,1,False,True),(5,8,True,False)],[-1,0,1,5,6,7])),
          A('Say','Her parçada 3 tam sayı.','−1, 0, 1 · 5, 6, 7 ⇒ 6')],
 puf='Çift taraflı mutlak değerde ortadaki boşluğu (burada 1 < x < 5) çözüme katma.')

# ===== 0007 ZOR · mtd-denklem (K-MTD-02)
v=[x for x in Z if abs(x-5)+abs(x+3)==8]; assert v==list(range(-3,6)) and len(v)==9 and 5-(-3)==8
assert all(abs(x-5)+abs(x+3)>8 for x in Z if x<-3 or x>5)
P.R('0007',**T('mtd-denklem'),zorluk='zor',alt='Mutlak Değerli Denklemler',kazanim='İki mutlak değerin toplamını sayı doğrusunda uzaklık olarak yorumlar; çözümün bir aralık olduğunu görüp tam sayıları sayar.',kalip='düz',adim=4,
 kart='K-MTD-02 (|x − a| + |x − b| = |a − b|, çözüm aralık) · yeni sayılar, istenen tam sayı çözüm adedi',
 metin='x bir tam sayı olmak üzere\n|x − 5| + |x + 3| = 8\neşitliğini sağlayan kaç farklı x değeri vardır?',
 **SK(9,{2:('bilgi','Yalnız uç noktaları (−3 ve 5) çözüm sanmak; aradaki her x de eşitliği sağlar.'),7:('dikkat','Uçları (−3 ve 5) saymamak; bu noktalarda da toplam 8.'),
         8:('islem','Uzaklığı (5 − (−3) = 8) nokta sayısı sanmak; −3’ten 5’e kadar 9 tam sayı var.'),10:('islem','Tam sayıları 5 − (−3) + 2 diye saymak; uçlar dahil sayı 8 + 1 = 9.')}),
 istenen='Eşitliği sağlayan tam sayıların adedi.',
 ipuclari=['|x − 5|, x’in 5’e; |x + 3|, x’in −3’e uzaklığıdır.','−3 ile 5 arasındaki bir noktadan iki uca uzaklıkların toplamı kaçtır?','Bu aralığın dışındaki bir noktada toplam 8’den büyük mü, küçük mü?'],bilgi=[UZ,MD],
 adimlar=[A('Uzaklık olarak oku','Toplam, x’in 5’e ve −3’e uzaklıklarının toplamı.','|x − 5| + |x − (−3)| = 8'),
          A('İki nokta arası','5 ile −3 arasındaki uzaklık tam 8.','5 − (−3) = 8'),
          A('Aradaki noktalar','−3 ile 5 arasındaki her noktada iki uzaklığın toplamı 8’dir; dışarıda 8’den büyüktür.','−3 ≤ x ≤ 5',sd(-5,7,[(-3,5,True,True)],list(range(-3,6)),'−3 ≤ x ≤ 5')),
          A('Say','−3’ten 5’e kadar tam sayılar.','5 − (−3) + 1 = 9')],
 puf='|x − a| + |x − b|, a ile b arasında sabittir ve bu iki nokta arasındaki uzaklığa eşittir.')
v=[x for x in Z if abs(x+4)+abs(x-2)==6]; assert v==list(range(-4,3)) and sum(v)==-7 and sum(range(-5,3))==-12 and sum(range(-3,2))==-5 and -4+2==-2 and len(v)==7
P.K('0007',metin='|x + 4| + |x − 2| = 6\neşitliğini sağlayan bütün x tam sayılarının toplamı kaçtır?',
 **SK(-7,{-12:('islem','−5’i de eklemek; |−5 + 4| + |−5 − 2| = 8, 6 değil.'),-5:('dikkat','Uçları (−4 ve 2) saymamak; bu noktalarda da toplam 6.'),
          -2:('bilgi','Yalnız uç noktaları (−4 ve 2) çözüm sanmak; aradaki her tam sayı da sağlar.'),7:('dikkat','7, çözüm olan tam sayıların sayısı; soru toplamı soruyor.')}),
 istenen='Eşitliği sağlayan tam sayıların toplamı.',
 ipuclari=['İfadeyi x’in −4’e ve 2’ye uzaklıklarının toplamı olarak oku.','−4 ile 2 arasındaki uzaklık kaç?','Aradaki her noktanın eşitliği sağladığını görünce tam sayıları topla.'],bilgi=[UZ,MD],
 adimlar=[A('Uzaklık olarak oku','x’in −4’e ve 2’ye uzaklıklarının toplamı.','|x − (−4)| + |x − 2| = 6'),
          A('İki nokta arası','−4 ile 2 arasındaki uzaklık.','2 − (−4) = 6'),
          A('Çözüm aralığı','Toplam, iki nokta arasındaki uzaklığa eşit: aradaki her nokta sağlar.','−4 ≤ x ≤ 2',sd(-6,4,[(-4,2,True,True)],list(range(-4,3)))),
          A('Topla','−2’den 2’ye kadar olanlar birbirini götürür.','−4 + (−3) + 0 = −7')],
 puf='Toplam uzaklık iki nokta arasındaki uzaklığa eşitse çözüm bir aralıktır, iki nokta değil.')

# ===== 0008 ZOR · mtd-uzaklik (K-MTD-06)
v=[n for n in range(0,1000) if abs(n-70)==2*abs(n-58)]; assert v==[46,62] and sum(v)==108 and 62-46==16
w=[n for n in range(0,1000) if 2*abs(n-70)==abs(n-58)]; assert w==[66,82] and sum(w)==148
P.R('0008',**T('mtd-uzaklik'),zorluk='zor',alt='Mutlak Değer',kazanim='İki uzaklık arasındaki oran bilgisini mutlak değerli denkleme çevirir; iki durumu da çözerek bütün değerleri bulur.',kalip='hikâyeli',adim=4,
 kart='K-MTD-06 (tahmin–gerçek uzaklık oranı) · yeni kurgu (kavanozdaki bilyeler), istenen değerlerin toplamı',
 metin='Bir bilgi yarışmasında kavanozdaki bilye sayısını Ece 70, Ferit 58 olarak tahmin etmiştir. Kavanozdaki gerçek bilye sayısı n olmak üzere\n|n − 70| = 2 · |n − 58|\neşitliği sağlanmaktadır.\nBuna göre n’nin alabileceği değerlerin toplamı kaçtır?',
 **SK(108,{16:('dikkat','16, iki değerin farkı (62 − 46); soru toplamı soruyor.'),46:('dikkat','Yalnız 58’in solundaki çözümü bulmak; 58 ile 70 arasında da bir çözüm var.'),
           62:('dikkat','Yalnız iki tahmin arasındaki çözümü bulmak; 58’in solunda da bir çözüm var.'),148:('islem','Oranı ters kurup 2 × |n − 70| = |n − 58| çözmek (66 ve 82).')}),
 istenen='n’nin alabileceği değerlerin toplamı.',
 ipuclari=['|A| = 2 × |B| ise A = 2B ya da A = −2B olur.','n − 70 = 2 × (n − 58) denklemini çöz.','n − 70 = −2 × (n − 58) denklemini de çöz ve iki değeri topla.'],bilgi=[MD,UZ,B('Mutlak değerlerin oranı','|A| = k × |B| (k > 0) ise A = k × B ya da A = −k × B. Örnek: |x| = 2 × |x − 3| ⇒ x = 6 ya da x = 2')],
 adimlar=[A('İki durum','Mutlak değerler eşitse içler ya eşit ya da zıt işaretlidir.','n − 70 = 2 × (n − 58) · n − 70 = −2 × (n − 58)'),
          A('Birinci durum','Parantezi aç ve çöz.','n − 70 = 2n − 116 ⇒ n = 46'),
          A('İkinci durum','Parantezi aç ve çöz.','n − 70 = −2n + 116 ⇒ 3n = 186 ⇒ n = 62'),
          A('Kontrol','İkisi de eşitliği sağlıyor.','|46 − 70| = 24 = 2 × 12 · |62 − 70| = 8 = 2 × 4 ✓'),
          A('Topla','İki değer.','46 + 62 = 108')],
 puf='Uzaklık oranı verilen sorularda iki durum vardır: nokta iki tahminin arasında ya da dışında olabilir.')
v=[n for n in range(0,1000) if abs(n-40)==3*abs(n-60)]; assert v==[55,70] and sum(v)==125 and 70-55==15
w=[n for n in range(0,1000) if 3*abs(n-40)==abs(n-60)]; assert w==[30,45] and sum(w)==75
P.K('0008',metin='Bir konser salonundaki seyirci sayısını Defne 40, Kaan 60 olarak tahmin etmiştir. Salondaki gerçek seyirci sayısı s olmak üzere\n|s − 40| = 3 · |s − 60|\neşitliği sağlanmaktadır.\nBuna göre s’nin alabileceği değerlerin toplamı kaçtır?',
 **SK(125,{15:('dikkat','15, iki değerin farkı (70 − 55); soru toplamı soruyor.'),55:('dikkat','Yalnız iki tahmin arasındaki çözümü almak; 60’ın sağında da bir çözüm var.'),
           70:('dikkat','Yalnız 60’ın sağındaki çözümü almak; 40 ile 60 arasında da bir çözüm var.'),75:('islem','Oranı ters kurup 3 × |s − 40| = |s − 60| çözmek (30 ve 45).')}),
 istenen='s’nin alabileceği değerlerin toplamı.',
 ipuclari=['|A| = 3 × |B| ise A = 3B ya da A = −3B.','s − 40 = 3 × (s − 60) denklemini çöz.','Diğer durumu da çöz; iki değeri topla.'],bilgi=[MD,UZ,B('Mutlak değerlerin oranı','|A| = k × |B| (k > 0) ise A = k × B ya da A = −k × B. Örnek: |x| = 3 × |x − 4| ⇒ x = 6 ya da x = 3')],
 adimlar=[A('İki durum','İçler ya aynı ya da zıt işaretli.','s − 40 = 3 × (s − 60) · s − 40 = −3 × (s − 60)'),
          A('Birinci durum','Çöz.','s − 40 = 3s − 180 ⇒ 2s = 140 ⇒ s = 70'),
          A('İkinci durum','Çöz.','s − 40 = −3s + 180 ⇒ 4s = 220 ⇒ s = 55'),
          A('Kontrol','İkisi de sağlıyor.','|70 − 40| = 30 = 3 × 10 · |55 − 40| = 15 = 3 × 5 ✓'),
          A('Topla','İki değer.','70 + 55 = 125')],
 puf='Mutlak değer eşitliğinde iki durumu da çöz ve bulduğun her değeri eşitlikte kontrol et.')

P.yaz(os.path.join(H,ONEK+'-1.json'),os.path.join(H,ONEK+'-1-kardes.json'))
