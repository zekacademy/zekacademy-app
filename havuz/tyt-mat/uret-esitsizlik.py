"""Basit Eşitsizlikler · parti 1: 8 ana + 8 kardeş. Her cevap ve ara sonuç kodla (ızgara/rastgele tarama dahil) doğrulanır."""
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
m_=lambda v:fmt(v)
def sd(lo,hi,araliklar=(),noktalar=(),baslik=''):
    """Sayı doğrusu: araliklar = [(a, b, a_dahil, b_dahil)], noktalar = vurgulanan tam sayılar."""
    W=330; x0,x1,y=18,312,34; X=lambda v:x0+(float(v)-lo)/(hi-lo)*(x1-x0); b=[]
    b.append(f'<line x1="{x0-8}" y1="{y}" x2="{x1+8}" y2="{y}" stroke-width="1.2" opacity=".6"/>')
    b.append(f'<path d="M{x1+8} {y} l-6 -4 v8 z" style="fill:currentColor;stroke:none" opacity=".6"/>')
    for t in range(lo,hi+1):
        b.append(f'<line x1="{X(t):.1f}" y1="{y-4}" x2="{X(t):.1f}" y2="{y+4}" stroke-width="1" opacity=".6"/>')
        b.append(G._t(X(t),y+18,m_(t),size=10))
    for a,c,ad,cd in araliklar:
        b.append(f'<line x1="{X(a):.1f}" y1="{y}" x2="{X(c):.1f}" y2="{y}" stroke-width="4" style="stroke:{G.ACC}" opacity=".55"/>')
        for v,d in ((a,ad),(c,cd)):
            st=f'style="stroke:{G.ACC};fill:{G.ACC}"' if d else f'style="stroke:{G.ACC};fill:none"'
            b.append(f'<circle cx="{X(v):.1f}" cy="{y}" r="4.5" stroke-width="2" {st}/>')
    for t in noktalar: b.append(f'<circle cx="{X(t):.1f}" cy="{y-11}" r="3" style="fill:{G.ACC};stroke:none"/>')
    if baslik: b.append(G._t(W/2,y+38,baslik,size=12,bold=True,renk=G.ACC))
    return G._svg(W,y+48 if baslik else y+26,''.join(b))
def ulasilan_tam(f,ar1,ar2,adim=200,kritik=()):
    """a ∈ ar1, b ∈ ar2 açık aralıkları. f sürekli ve tanım bölgesi bağlantılı olduğundan değer kümesi (inf, sup) açık aralığıdır.
    inf/sup uç noktalar ve a için kritik noktalardan (ör. a² için 0) hesaplanır; ızgara taraması değerlerin bu aralıkta kalıp uçlara yaklaştığını doğrular.
    Dönüş: aralıktaki tam sayılar, inf, sup."""
    (p,q),(r,s)=ar1,ar2
    K=[f(a,b) for a in [p,q,*kritik] for b in [r,s]]; inf,sup=min(K),max(K)
    A_=[p+Fr(i,adim)*(q-p) for i in range(1,adim)]+list(kritik); B_=[r+Fr(j,adim)*(s-r) for j in range(1,adim)]
    V=[f(a,b) for a in A_ for b in B_]; e=Fr(1,2)
    assert inf<min(V) and max(V)<sup and min(V)-inf<e and sup-max(V)<e
    import math
    return set(range(math.floor(inf)+1,math.ceil(sup))),inf,sup
ONEK='esitsizlik'; KONU='Basit Eşitsizlikler'; UK='mat|Basit Eşitsizlikler'
P=Parti(ONEK,KONU,UK)

YON=B('Negatif sayıyla çarpma','eşitsizliğin iki yanı negatif bir sayıyla çarpılır ya da bölünürse yön değişir. Örnek: −2x < 6 ⇒ x > −3')
UC=B('Uç değerler','< ve > uç değeri almaz, ≤ ve ≥ alır. Örnek: 2 ≤ x < 5 için x tam sayıları 2, 3, 4')
TOPL=B('Aralıkları birleştirme','aynı yönlü eşitsizlikler taraf tarafa toplanır ama çıkarılmaz; a − b için önce −b’nin aralığı bulunur. Örnek: 1 < b < 5 ⇒ −5 < −b < −1')
KARE=B('Karenin aralığı','aralık 0’ı içeriyorsa kare 0’dan başlar; üst sınır, uçların karelerinden büyük olanıdır. Örnek: −2 < a < 1 ⇒ 0 ≤ a² < 4')
KESIN=B('Kesinlikle doğru','ifade verilen koşullardaki her sayı için doğru olmalıdır; tek bir karşı örnek ifadeyi eler')
ISR=B('Çarpımın işareti','aynı işaretli iki sayının çarpımı pozitif, zıt işaretli iki sayının çarpımı negatiftir. Örnek: (−2) × (−3) = 6 · (−2) × 3 = −6')

# ---------- kartlar ve tipler ----------
TIPLER=[('esz-cozum','Eşitsizlik çözme ve tam sayı değerleri'),('esz-aralik','Aralıklardan ifadenin aralığı'),('esz-siralama','Eşitsizlikle işaret ve sıralama'),
        ('esz-problem','Eşitsizlik problemleri'),('esz-kare','Kare içeren ifadenin aralığı')]
TAD=dict(TIPLER)
KARTLAR=[
 dict(id='K-ESZ-01',alt='Eşitsizlik Çözme',fikir='Çift taraflı birinci dereceden eşitsizlik çözülür; aralıktaki tam sayılar sayılır, toplanır ya da en küçüğü/en büyüğü istenir.',tuzak='Negatif katsayıya bölerken yönü çevirmemek; ≤ ile < uçlarını karıştırmak; adet ile toplamı karıştırmak.',zorluk='kolay',kalip='düz',adim=2,tipId='esz-cozum',kaynak='ÖSYM (Basit Eşitsizlikler) · 345 SB, 3D, Bilgi Sarmal'),
 dict(id='K-ESZ-02',alt='Aralık',fikir='İki değişkenin aralıkları verilir; ka ± mb ifadesinin aralığı katsayı ve işaret dikkate alınarak bulunur, tam sayı değerleri sayılır ya da en büyük değer sorulur.',tuzak='Aralıkları taraf tarafa çıkarmak; −b’ye çevirirken uçları yer değiştirmemek; kesin eşitsizlikte uçları saymak.',zorluk='orta',kalip='düz',adim=3,tipId='esz-aralik',kaynak='ÖSYM (Aralık Kavramı, Basit Eşitsizlikler) · 345 SB (a² + b² en büyük tam değer) · 3D'),
 dict(id='K-ESZ-03',alt='Sıralama',fikir='Çarpım ve sıralama bilgilerinden sayıların işaretleri çıkarılır; öncüllerde ya da şıklarda kesinlikle doğru olan ifade bulunur.',tuzak='Negatif sayıyla çarpınca/bölünce yön değiştirmeyi unutmak; “olabilir” ile “kesinlikle”yi karıştırmak.',zorluk='orta',kalip='öncüllü',adim=3,tipId='esz-siralama',kaynak='ÖSYM 2018–2026 (a > ab > 2a > ac, kalori sıralaması) · 345 SB, Bilgi Sarmal'),
 dict(id='K-ESZ-04',alt='Eşitsizlik Problemleri',fikir='Bütçe, ücret ya da “alabiliyor ama alamıyor” bilgileri eşitsizliğe çevrilir; tam sayı koşuluyla en çok değer ya da değer sayısı bulunur.',tuzak='Sabit ücreti düşmemek; ondalık sonucu yukarı yuvarlamak; iki koşulun kesişimini almamak.',zorluk='kolay',kalip='hikâyeli',adim=2,tipId='esz-problem',kaynak='ÖSYM (buzdolabı maliyeti, kâr–zarar eşitsizliği) · Bilgi Sarmal, Mert'),
 dict(id='K-ESZ-05',alt='Aralık',fikir='Sıfırı içeren bir aralıkta değişkenin karesi ile başka bir ifade birleştirilir; ifadenin en küçük/en büyük tam sayı değeri bulunur.',tuzak='Karenin aralığını uçların karelerinden kurmak (0’ı atlamak); −b aralığını çevirmemek; uç değeri dahil etmek.',zorluk='zor',kalip='düz',adim=4,tipId='esz-kare',kaynak='ÖSYM (Basit Eşitsizlikler) · 345 SB (a² − b², a² + b²) · 3D (a² + b² en büyük–en küçük)'),
]
for k in KARTLAR: k['konu']=KONU; k['tip']=TAD[k['tipId']]
KS=[dict(id=k['id'],konu=k['konu'],alt=k['alt'],fikir=k['fikir'],tuzak=k['tuzak'],zorluk=k['zorluk'],kalip=k['kalip'],adim=k['adim'],tipId=k['tipId'],tip=k['tip'],kaynak=k['kaynak']) for k in KARTLAR]
TS=[dict(tipId=t,ad=a,kartlar=[k['id'] for k in KARTLAR if k['tipId']==t],uygulamaKonu=UK) for t,a in TIPLER]
json.dump(dict(konu=KONU,surum=1,kartlar=KS,tipler=TS),open(os.path.join(H,'..','kartlar',ONEK+'.json'),'w'),ensure_ascii=False,indent=1)
T=lambda t:dict(tipId=t,tip=TAD[t])
Z=range(-200,201)
random.seed(20261106)

# ===== 0001 KOLAY · esz-cozum (K-ESZ-01)
v=[x for x in Z if 3<=2*x-1<11]; assert v==[2,3,4,5] and sum(v)==14
assert sum(range(3,6))==12 and sum(range(2,7))==20 and sum(range(4,12))==60
P.R('0001',**T('esz-cozum'),zorluk='kolay',alt='Eşitsizlik Çözme',kazanim='Çift taraflı birinci dereceden eşitsizliği çözer; uç değerleri doğru yorumlayarak tam sayı çözümleri bulur.',kalip='düz',adim=2,
 kart='K-ESZ-01 (çift taraflı eşitsizlik, tam sayı çözümler) · yeni eşitsizlik, istenen çözümlerin toplamı',
 metin='x bir tam sayı olmak üzere\n3 ≤ 2x − 1 < 11\nolduğuna göre x’in alabileceği değerlerin toplamı kaçtır?',
 **SK(14,{4:('dikkat','4, x’in alabileceği değer sayısı; soru değerlerin toplamını soruyor.'),12:('bilgi','2’yi almamak; 2 ≤ x olduğundan 2 de çözümdür.'),
          20:('bilgi','6’yı da eklemek; x < 6 kesin eşitsizlik, 6 çözüm değil.'),60:('islem','2’ye bölmeyi unutup 4 ≤ x < 12 almak.')}),
 istenen='Eşitsizliği sağlayan tam sayıların toplamı.',
 ipuclari=['Eşitsizliğin her tarafına 1 ekle.','Sonra her tarafı 2’ye böl; 2 pozitif, yön değişmez.','≤ tarafındaki uç dahil, < tarafındaki uç dahil değil.'],bilgi=[UC],
 adimlar=[A('1 ekle','Ortadaki −1’i yok etmek için her tarafa 1 eklenir.','3 + 1 ≤ 2x < 11 + 1 ⇒ 4 ≤ 2x < 12'),
          A('2’ye böl','Pozitif sayıya bölünce yön korunur.','2 ≤ x < 6',sd(0,7,[(2,6,True,False)],[2,3,4,5],'x = 2, 3, 4, 5')),
          A('Topla','Uçlardan 2 dahil, 6 dahil değil.','2 + 3 + 4 + 5 = 14')],
 puf='Çift taraflı eşitsizlikte her işlemi üç tarafa birden uygula; sonra uçların dahil olup olmadığına bak.')
v=[x for x in Z if -5<3*x+1<=10]; assert v==[-1,0,1,2,3] and min(v)==-1 and min(x for x in Z if -6<x<=9)==-5
P.K('0001',metin='x bir tam sayıdır.\n−5 < 3x + 1 ≤ 10\nolduğuna göre x’in alabileceği en küçük değer kaçtır?',
 **SK(-1,{-5:('islem','3’e bölmeyi unutup −6 < x almak.'),-2:('bilgi','−2’yi çözüm sanmak; x > −2 kesin eşitsizlik, −2 dahil değil.'),
          0:('dikkat','Negatif tam sayıları atlamak; −1 de bir tam sayıdır ve −2’den büyüktür.'),3:('dikkat','3, x’in en büyük değeri; soru en küçüğü soruyor.')}),
 istenen='x’in en küçük tam sayı değeri.',
 ipuclari=['Her taraftan 1 çıkar.','Her tarafı 3’e böl.','Sol uç kesin (<); bu uçtan büyük ilk tam sayıyı seç.'],bilgi=[UC],
 adimlar=[A('1 çıkar','Ortadaki +1’i yok et.','−5 − 1 < 3x ≤ 10 − 1 ⇒ −6 < 3x ≤ 9'),
          A('3’e böl','Pozitif sayıya bölünce yön korunur.','−2 < x ≤ 3',sd(-3,4,[(-2,3,False,True)],[-1,0,1,2,3],'x = −1, 0, 1, 2, 3')),
          A('En küçük','−2 dahil değil; ondan büyük ilk tam sayı.','x = −1')],
 puf='Kesin eşitsizlikte (<) uç değer çözüm değildir; en küçük çözüm ondan büyük ilk tam sayıdır.')

# ===== 0002 KOLAY · esz-problem (K-ESZ-04)
v=[x for x in range(0,100) if 40+12*x<=250]; assert max(v)==17 and 40+12*18==256 and 250//12==20 and 290//12==24 and -(-250//12)==21
P.R('0002',**T('esz-problem'),zorluk='kolay',alt='Eşitsizlik Problemleri',kazanim='Sabit ve birim ücretli bir harcamayı eşitsizlikle ifade eder; tam sayı koşuluyla en büyük değeri bulur.',kalip='hikâyeli',adim=2,
 kart='K-ESZ-04 (bütçe eşitsizliği) · yeni kurgu (taksi ücreti), istenen en çok kilometre',
 metin='Bir taksinin açılış ücreti 40 TL’dir ve taksimetre gidilen her tam kilometre için bu ücrete 12 TL eklemektedir. Yolculuk ücreti yalnızca tam kilometreler üzerinden hesaplanır.\nCebinde 250 TL bulunan Selin, bu taksiyle en çok kaç kilometre yol gidebilir?',
 **SK(17,{18:('islem','17,5’i yukarı yuvarlamak; 18 km için 40 + 216 = 256 TL gerekir.'),20:('dikkat','40 TL açılış ücretini düşmeden 250 ÷ 12 hesaplamak.'),
          21:('dikkat','Açılış ücretini düşmeden hesaplayıp sonucu yukarı yuvarlamak.'),24:('islem','40 TL’yi çıkarmak yerine eklemek: 290 ÷ 12.')}),
 istenen='Selin’in gidebileceği en çok kilometre.',
 ipuclari=['x km için ödenecek tutarı yaz.','Bu tutar 250 TL’yi aşmamalı.','Sonuç tam kilometre olmalı; aşağı mı yukarı mı yuvarlanır?'],bilgi=[B('Bütçe eşitsizliği','ödenecek tutar paradan fazla olamaz: tutar ≤ para. Örnek: 10 + 5x ≤ 30 ⇒ x ≤ 4')],
 adimlar=[A('Eşitsizlik','x km için tutar 40 + 12x; 250 TL’yi aşamaz.','40 + 12x ≤ 250'),
          A('Çöz','Açılış ücretini çıkar, 12’ye böl.','12x ≤ 210 ⇒ x ≤ 17,5'),
          A('Tam kilometre','17,5’ten büyük olmayan en büyük tam sayı.','x = 17 · 40 + 12 × 17 = 244 ≤ 250 ✓')],
 puf='“En çok” sorularında ondalık sonucu aşağı yuvarla; yukarı yuvarlamak bütçeyi aşar.')
v=[x for x in range(0,100) if 85+18*x<=300]; assert max(v)==11 and 85+18*12==301 and 300//18==16 and 385//18==21
P.K('0002',metin='Bir öğrenci kırtasiyeden 85 TL’lik bir okul çantası ve tanesi 18 TL olan defterlerden birkaç tane alacaktır.\nÖğrencinin harcaması 300 TL’yi geçmeyeceğine göre en çok kaç defter alabilir?',
 **SK(11,{12:('islem','11,9…’u yukarı yuvarlamak; 12 defterle tutar 301 TL olur.'),16:('dikkat','Çantanın fiyatını düşmeden 300 ÷ 18 hesaplamak.'),
          17:('dikkat','Çantayı düşmeden hesaplayıp yukarı yuvarlamak.'),21:('islem','85 TL’yi çıkarmak yerine eklemek: 385 ÷ 18.')}),
 istenen='Alınabilecek en çok defter sayısı.',
 ipuclari=['x defter için toplam tutarı yaz.','Tutar 300 TL’yi geçmemeli.','Defter sayısı tam sayı; uygun yuvarlamayı yap.'],bilgi=[B('Bütçe eşitsizliği','harcama bütçeyi geçemez: harcama ≤ bütçe. Örnek: 20 + 6x ≤ 50 ⇒ x ≤ 5')],
 adimlar=[A('Eşitsizlik','Çanta + x defter ≤ 300.','85 + 18x ≤ 300'),
          A('Çöz','85’i çıkar, 18’e böl.','18x ≤ 215 ⇒ x ≤ 215/18 ≈ 11,9'),
          A('Tam sayı','11,9’dan büyük olmayan en büyük tam sayı.','x = 11 · 85 + 18 × 11 = 283 ≤ 300 ✓')],
 puf='Sabit harcamayı önce bütçeden düş, kalanı birim fiyata böl ve aşağı yuvarla.')

# ===== 0003 ORTA · esz-aralik (K-ESZ-02)
S,lo,hi=ulasilan_tam(lambda a,b:2*a-b,(-3,2),(1,5)); assert S==set(range(-10,3)) and (lo,hi)==(-11,3) and len(S)==13
S2,_,_=ulasilan_tam(lambda a,b:a-b,(-3,2),(1,5)); assert len(S2)==8
P.R('0003',**T('esz-aralik'),zorluk='orta',alt='Aralık',kazanim='İki değişkenin aralığından ka − mb ifadesinin aralığını bulur ve alabileceği tam sayı değerlerini sayar.',kalip='düz',adim=3,
 kart='K-ESZ-02 (aralıktan ifade aralığı) · yeni ifade (2a − b), istenen tam sayı değeri sayısı',
 metin='a ve b gerçel sayılar olmak üzere\n−3 < a < 2\n1 < b < 5\nolduğuna göre 2a − b ifadesinin alabileceği kaç farklı tam sayı değeri vardır?',
 **SK(13,{5:('islem','Aralıkları uç uca çıkarmak: (−6 − 1, 4 − 5) = (−7, −1); −b’nin aralığı (−5, −1) bulunup toplanmalı.'),8:('dikkat','a’yı 2 ile çarpmayı unutup a − b’nin aralığıyla (−8, 1) çalışmak.'),
          11:('dikkat','−10 ile 2’yi de uç sanıp atmak; ikisi de aralığın içinde.'),12:('islem','−11 ile 3 arasındaki tam sayıları yanlış saymak; −10’dan 2’ye kadar 13 tam sayı var.')}),
 istenen='2a − b’nin alabileceği tam sayı değerlerinin sayısı.',
 ipuclari=['Önce 2a’nın aralığını bul.','b’nin aralığını −1 ile çarp; yön değişir.','İki aralığı taraf tarafa topla, uçlar dahil değil.'],bilgi=[TOPL,YON],
 adimlar=[A('2a’nın aralığı','Her tarafı 2 ile çarp.','−6 < 2a < 4'),
          A('−b’nin aralığı','−1 ile çarpınca yön değişir.','−5 < −b < −1'),
          A('Topla','Aynı yönlü eşitsizlikler taraf tarafa toplanır.','−11 < 2a − b < 3',sd(-12,4,[(-11,3,False,False)],list(range(-10,3)))),
          A('Say','−10’dan 2’ye kadar tam sayılar.','2 − (−10) + 1 = 13')],
 puf='Fark ifadesinde çıkarılan değişkeni önce −1 ile çarpıp aralığını çevir, sonra topla.')
S,lo,hi=ulasilan_tam(lambda a,b:a-3*b,(-2,4),(-3,1)); assert max(S)==12 and (lo,hi)==(-5,13)
S3,_,hi3=ulasilan_tam(lambda a,b:a+3*b,(-2,4),(-3,1)); assert max(S3)==6
P.K('0003',metin='a ve b gerçel sayılardır.\n−2 < a < 4 ve −3 < b < 1\nolduğuna göre a − 3b ifadesinin alabileceği en büyük tam sayı değeri kaçtır?',
 **SK(12,{0:('islem','a ile b’nin en büyük değerlerini (4 ve 1) koyup 4 − 3 = 1’den küçük tam sayı almak; b küçüldükçe ifade büyür.'),6:('bilgi','−3b’nin aralığını çevirmeden (−9, 3) almak; negatifle çarpınca yön değişir.'),
          8:('dikkat','a’yı hesaba katmadan yalnız −3b < 9’dan en büyük tam sayıyı almak.'),13:('bilgi','Uç değeri almak; a − 3b < 13 kesin, 13’e ulaşılamaz.')}),
 istenen='a − 3b’nin en büyük tam sayı değeri.',
 ipuclari=['b’nin aralığını −3 ile çarp; yön ne olur?','a’nın aralığı ile −3b’nin aralığını taraf tarafa topla.','Üst sınır dahil değilse en büyük tam değer ondan 1 küçüktür.'],bilgi=[TOPL,YON],
 adimlar=[A('−3b’nin aralığı','−3 ile çarpınca yön değişir.','−3 < b < 1 ⇒ −3 < −3b < 9'),
          A('Topla','a’nın aralığı ile topla.','−2 + (−3) < a − 3b < 4 + 9 ⇒ −5 < a − 3b < 13'),
          A('En büyük tam değer','13 dahil değil.','12')],
 puf='Negatif katsayılı terimin aralığını çevirmeyi unutma; en büyük değeri, çıkarılan terimin en küçük olduğu yer verir.')

# ===== 0004 ORTA · esz-siralama (K-ESZ-03)
def ornek4():
    a=-Fr(random.randint(1,400),random.randint(1,20)); b=Fr(random.randint(1,400),random.randint(1,20)); c=b+Fr(random.randint(1,400),random.randint(1,20)); return a,b,c
O=[ornek4() for _ in range(4000)]; assert all(a<0<b<c for a,b,c in O)
I_=all(a*c<b*c for a,b,c in O); II_=all(a*a<b*b for a,b,c in O); III_=all(a/c>a/b for a,b,c in O); assert (I_,II_,III_)==(True,False,True)
a,b,c=-6,2,3; assert Fr(a,c)==-2 and Fr(a,b)==-3 and (-5)**2>1
ONC=['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III']
P.R('0004',**T('esz-siralama'),zorluk='orta',alt='Sıralama',kazanim='Verilen sıralamadan çarpma ve bölmede eşitsizliğin yönünü belirler; kesinlikle doğru olan öncülleri seçer.',kalip='öncüllü',adim=3,
 kart='K-ESZ-03 (sıralamadan kesin yargı) · yeni sıralama (a < 0 < b < c), öncüllerde çarpma, kare ve bölme',
 metin='a, b ve c gerçel sayılar olmak üzere\na < 0 < b < c\nolduğu biliniyor.\nBuna göre\nI. a · c < b · c\nII. a² < b²\nIII. a/c > a/b\nifadelerinden hangileri kesinlikle doğrudur?',
 **SK('I ve III',{'Yalnız I':('bilgi','III’ü elemek: a negatif olduğundan daha büyük paydaya bölünen daha büyük çıkar (−6/3 = −2 > −6/2 = −3).'),
                  'Yalnız II':('bilgi','II her zaman doğru değil (a = −5, b = 1 için a² = 25 > 1); I ve III ise kesin doğru.'),
                  'I ve II':('dikkat','II’yi kesin sanmak: negatif sayı b’den çok daha uzakta olabilir (a = −5, b = 1).'),
                  'I, II ve III':('dikkat','II’yi kesin sanmak: a = −5, b = 1 için a² > b².')},sira=ONC),
 istenen='Her durumda doğru olan öncüller.',
 ipuclari=['I için: a < b eşitsizliğini pozitif c ile çarp.','II için a = −5, b = 1 gibi bir örnek dene.','III için önce 1/b ile 1/c’yi karşılaştır, sonra negatif a ile çarp.'],bilgi=[YON,KESIN],
 adimlar=[A('I. öncül','a < b ve c > 0; pozitifle çarpınca yön korunur.','a × c < b × c ✓'),
          A('II. öncül','Karşı örnek bulunursa kesin değildir.','a = −5, b = 1 ⇒ 25 > 1 ✗'),
          A('III. öncül','0 < b < c ⇒ 1/b > 1/c. Negatif a ile çarpınca yön değişir.','a/b < a/c ✓'),
          A('Sonuç','I ve III her durumda doğru.','I ve III')],
 puf='Negatif bir sayıyla çarpıp bölerken yönü çevir; kareli ifadelerde de mutlaka bir karşı örnek dene.')
def ornek4k():
    y=-Fr(random.randint(1,400),random.randint(1,20)); x=y-Fr(random.randint(1,400),random.randint(1,20)); z=Fr(random.randint(1,400),random.randint(1,20)); return x,y,z
O=[ornek4k() for _ in range(4000)]; assert all(x<y<0<z for x,y,z in O)
assert (all(x*z<y*z for x,y,z in O),all(x/y>1 for x,y,z in O),all(x+z<0 for x,y,z in O))==(True,True,False) and -5+10>0
ONC2=['Yalnız I','Yalnız III','I ve II','II ve III','I, II ve III']
P.K('0004',metin='x, y ve z gerçel sayılar olmak üzere\nx < y < 0 < z\nolduğu biliniyor.\nBuna göre\nI. x · z < y · z\nII. x/y > 1\nIII. x + z < 0\nifadelerinden hangileri kesinlikle doğrudur?',
 **SK('I ve II',{'Yalnız I':('bilgi','II’yi elemek: x < y < 0 iken iki tarafı negatif y’ye bölünce yön değişir, x/y > 1 olur (−4/−2 = 2).'),
                 'Yalnız III':('dikkat','III kesin değil: x = −5, z = 10 için x + z = 5 > 0.'),
                 'II ve III':('dikkat','III’ü kesin sanmak (x = −5, z = 10 için x + z > 0) ve I’i atlamak.'),
                 'I, II ve III':('dikkat','III’ü kesin sanmak; z büyükse x + z pozitif olur.')},sira=ONC2),
 istenen='Her durumda doğru olan öncüller.',
 ipuclari=['I için x < y’yi pozitif z ile çarp.','II için x < y’nin iki tarafını negatif y’ye böl.','III için z’yi büyük seçen bir örnek dene.'],bilgi=[YON,KESIN],
 adimlar=[A('I. öncül','z > 0; pozitifle çarpınca yön korunur.','x × z < y × z ✓'),
          A('II. öncül','y < 0; negatife bölünce yön değişir.','x/y > y/y = 1 ✓'),
          A('III. öncül','Karşı örnek: x = −5, y = −1, z = 10.','x + z = 5 > 0 ✗'),
          A('Sonuç','I ve II her durumda doğru.','I ve II')],
 puf='Bölme de çarpma gibidir: negatif bir sayıya bölünce eşitsizlik yön değiştirir.')

# ===== 0005 ORTA · esz-cozum (K-ESZ-01)
v=[x for x in Z if -7<5-3*x<=11]; assert v==[-2,-1,0,1,2,3] and sum(v)==3
assert sum(range(-2,3))==0 and sum(range(-1,4))==5 and sum(range(-2,5))==7
P.R('0005',**T('esz-cozum'),zorluk='orta',alt='Eşitsizlik Çözme',kazanim='Negatif katsayılı çift taraflı eşitsizliği yön değiştirerek çözer; tam sayı çözümlerin toplamını bulur.',kalip='düz',adim=3,
 kart='K-ESZ-01 (çift taraflı eşitsizlik) · negatif katsayı (yön değişimi), istenen çözümlerin toplamı',
 metin='−7 < 5 − 3x ≤ 11\neşitsizliğini sağlayan tam sayıların toplamı kaçtır?',
 **SK(3,{0:('dikkat','3’ü almamak; x < 4 olduğundan 3 de çözümdür.'),5:('bilgi','−2’yi almamak; x ≥ −2 olduğundan −2 dahildir.'),
         6:('dikkat','6, çözüm olan tam sayıların sayısı; soru toplamı soruyor.'),7:('bilgi','4’ü de eklemek; x < 4 kesin eşitsizlik.')}),
 istenen='Eşitsizliği sağlayan tam sayıların toplamı.',
 ipuclari=['Önce ortadaki sabit terimi her taraftan çıkar.','Sonra her tarafı x’in katsayısına böl; katsayı negatif, yön ne olur?','Hangi uç dahil, hangisi değil? Çözüm kümesini sayı doğrusunda göster.'],bilgi=[YON,UC],
 adimlar=[A('5 çıkar','Ortadaki 5’i yok et.','−12 < −3x ≤ 6'),
          A('−3’e böl','Negatif sayıya bölünce iki yön de değişir.','4 > x ≥ −2 ⇒ −2 ≤ x < 4',sd(-3,5,[(-2,4,True,False)],list(range(-2,4)),'x = −2, −1, 0, 1, 2, 3')),
          A('Topla','−2 ile 2 birbirini götürür.','−2 − 1 + 0 + 1 + 2 + 3 = 3')],
 puf='Negatif katsayıya bölünce işaretler döner; ≤ olan taraf ≥ olur, uç dahil olmaya devam eder.')
v=[x for x in Z if -4<=8-2*x<6]; assert v==[2,3,4,5,6] and sum(v)==20 and sum(range(2,6))==14 and sum(range(1,7))==21 and sum(range(2,8))==27
P.K('0005',metin='−4 ≤ 8 − 2x < 6\neşitsizliğini sağlayan x tam sayılarının toplamı kaçtır?',
 **SK(20,{5:('dikkat','5, çözüm olan tam sayıların sayısı; soru toplamı soruyor.'),14:('bilgi','6’yı almamak; x ≤ 6 olduğundan 6 dahildir.'),
          21:('bilgi','1’i de eklemek; x > 1 kesin eşitsizlik.'),27:('islem','−4 − 8’i −14 hesaplayıp x ≤ 7 bulmak; −4 − 8 = −12.')}),
 istenen='Eşitsizliği sağlayan tam sayıların toplamı.',
 ipuclari=['Her taraftan 8 çıkar.','−2’ye bölerken yönleri çevir.','Uçlardan hangisinin dahil olduğuna dikkat et.'],bilgi=[YON,UC],
 adimlar=[A('8 çıkar','Ortadaki 8’i yok et.','−12 ≤ −2x < −2'),
          A('−2’ye böl','Negatife bölünce yönler değişir.','6 ≥ x > 1 ⇒ 1 < x ≤ 6',sd(0,7,[(1,6,False,True)],[2,3,4,5,6],'x = 2, 3, 4, 5, 6')),
          A('Topla','Tam sayı çözümleri topla.','2 + 3 + 4 + 5 + 6 = 20')],
 puf='Yön değiştirdikten sonra eşitsizliği küçükten büyüğe yeniden yaz; uçları okumak kolaylaşır.')

# ===== 0006 ORTA · esz-problem (K-ESZ-04)
v=[p for p in range(0,1000) if 8*15<=p<9*15 and 6*18<=p<7*18]; assert v==list(range(120,126)) and len(v)==6
assert len(range(120,135))==15 and len(range(108,126))==18
P.R('0006',**T('esz-problem'),zorluk='orta',alt='Eşitsizlik Problemleri',kazanim='“Alabiliyor ama alamıyor” bilgilerini çift taraflı eşitsizliğe çevirir; iki koşulun kesişimindeki tam sayıları sayar.',kalip='hikâyeli',adim=3,
 kart='K-ESZ-04 (alabilir–alamaz bilgisi) · yeni kurgu (defter ve kalem), iki eşitsizliğin kesişimi',
 metin='Elif’in parasıyla tanesi 15 TL olan defterlerden 8 tane alınabiliyor ancak 9 tane alınamıyor. Aynı parayla tanesi 18 TL olan kalemlerden 6 tane alınabiliyor ancak 7 tane alınamıyor.\nElif’in parası TL cinsinden bir tam sayı olduğuna göre kaç farklı değer alabilir?',
 **SK(6,{5:('bilgi','120’yi almamak; 8 defter tam 120 TL ise para 120 TL de olabilir.'),7:('dikkat','126’yı da saymak; 126 TL ile 7 kalem alınabilir.'),
         15:('dikkat','Yalnız defter koşulunu kullanmak (120 ile 134 arası).'),18:('dikkat','Yalnız kalem koşulunu kullanmak (108 ile 125 arası).')}),
 istenen='Elif’in parasının alabileceği tam sayı değerlerinin sayısı.',
 ipuclari=['8 defter alınabiliyorsa para en az kaç TL? 9 alınamıyorsa en çok?','Kalemler için de aynı iki sınırı yaz.','İki aralığın ortak kısmındaki tam sayıları say.'],bilgi=[B('Alabilir ama alamaz','n tane alınabiliyor, n + 1 tane alınamıyorsa: n × fiyat ≤ para < (n + 1) × fiyat. Örnek: 10 TL’likten 3 tane ⇒ 30 ≤ para < 40'),UC],
 adimlar=[A('Defter koşulu','8 tane alınabiliyor, 9 tane alınamıyor.','8 × 15 ≤ p < 9 × 15 ⇒ 120 ≤ p < 135'),
          A('Kalem koşulu','6 tane alınabiliyor, 7 tane alınamıyor.','6 × 18 ≤ p < 7 × 18 ⇒ 108 ≤ p < 126'),
          A('Ortak kısım','İki koşul birlikte sağlanmalı.','120 ≤ p < 126'),
          A('Say','120’den 125’e kadar tam sayılar.','120, 121, …, 125 ⇒ 6')],
 puf='“n tane alınabiliyor, n + 1 alınamıyor” bilgisi iki taraflı eşitsizliktir; birden çok koşulda kesişimi al.')
v=[p for p in range(0,1000) if 5*24<=p<6*24 and 3*35<=p<4*35]; assert v==list(range(120,140)) and max(v)-min(v)==19 and len(v)==20 and 143-120==23 and 140-105==35
P.K('0006',metin='Can’ın parasıyla tanesi 24 TL olan sinema biletlerinden 5 tane alınabiliyor ancak 6 tane alınamıyor. Aynı parayla tanesi 35 TL olan menülerden ise 3 tane alınabiliyor ancak 4 tane alınamıyor.\nCan’ın parası TL cinsinden bir tam sayı olduğuna göre parasının alabileceği en büyük değer ile en küçük değerin farkı kaçtır?',
 **SK(19,{20:('dikkat','20, paranın alabileceği değerlerin sayısı; soru en büyük ile en küçük değerin farkını soruyor.'),23:('dikkat','Menü koşulunu kullanmayıp 143 − 120 almak.'),
          24:('bilgi','Sınırları dahil edip 144 − 120 almak; 144 TL ile 6 bilet alınabilir.'),35:('dikkat','Yalnız menü koşulunu kullanıp 140 − 105 almak.')}),
 istenen='Paranın en büyük ve en küçük değerinin farkı.',
 ipuclari=['Bilet koşulunu çift taraflı eşitsizlik olarak yaz.','Menü koşulunu da yaz.','Ortak aralığın en küçük ve en büyük tam sayısını bul.'],bilgi=[B('Alabilir ama alamaz','n tane alınabiliyor, n + 1 tane alınamıyorsa: n × fiyat ≤ para < (n + 1) × fiyat. Örnek: 12 TL’likten 4 tane ⇒ 48 ≤ para < 60'),UC],
 adimlar=[A('Bilet koşulu','5 bilet alınabiliyor, 6 alınamıyor.','120 ≤ p < 144'),
          A('Menü koşulu','3 menü alınabiliyor, 4 alınamıyor.','105 ≤ p < 140'),
          A('Ortak kısım','İkisi birlikte.','120 ≤ p < 140 ⇒ en küçük 120, en büyük 139'),
          A('Fark','En büyük − en küçük.','139 − 120 = 19')],
 puf='Kesin üst sınırda (<) en büyük tam değer sınırdan 1 eksiktir.')

# ===== 0007 ZOR · esz-kare (K-ESZ-05)
S,lo,hi=ulasilan_tam(lambda a,b:a*a-b,(-4,3),(-2,5),kritik=(0,)); assert min(S)==-4 and lo==-5 and hi==18 and 0*0-4==-4
assert 1-5==-4 and 9-5==4 and 0-2==-2  # çeldiriciler: a² ≥ 1 ⇒ > −4 ⇒ −3 · (9, 16) ⇒ > 4 ⇒ 5 · −b çevrilmezse > −2 ⇒ −1
P.R('0007',**T('esz-kare'),zorluk='zor',alt='Aralık',kazanim='Sıfırı içeren bir aralıkta karenin aralığını doğru kurar; fark ifadesinin en küçük tam sayı değerini bulur.',kalip='düz',adim=4,
 kart='K-ESZ-05 (kare içeren ifadenin aralığı) · yeni ifade (a² − b), istenen en küçük tam değer',
 metin='a ve b birer gerçel sayıdır.\n−4 < a < 3\n−2 < b < 5\nBuna göre a² − b ifadesinin alabileceği en küçük tam sayı değeri kaçtır?',
 **SK(-4,{-5:('bilgi','Uç değeri almak; a² − b > −5 kesin, −5’e ulaşılamaz.'),-3:('islem','a²’nin en küçük değerini 1 sanmak; a = 0 olabilir, a² en küçük 0.'),
          -1:('bilgi','−b’nin aralığını çevirmeden (−2, 5) almak; −1 ile çarpınca aralık (−5, 2) olur.'),5:('bilgi','a²’nin aralığını uçların karelerinden (9, 16) kurmak; a, 0’dan geçtiği için a² 0’dan başlar.')}),
 istenen='a² − b’nin en küçük tam sayı değeri.',
 ipuclari=['a’nın aralığı 0’ı içeriyor mu? a²’nin en küçük değeri ne olur?','a²’nin üst sınırı için iki ucun karelerini karşılaştır.','−b’nin aralığını bul, a²’ninkiyle taraf tarafa topla.'],bilgi=[KARE,TOPL,UC],
 adimlar=[A('a²’nin aralığı','a, 0’dan geçiyor: a² en az 0. Üst sınır (−4)² = 16 (3² = 9’dan büyük).','0 ≤ a² < 16'),
          A('−b’nin aralığı','−1 ile çarpınca yön değişir.','−5 < −b < 2'),
          A('Topla','a² − b = a² + (−b).','0 + (−5) < a² − b < 16 + 2 ⇒ −5 < a² − b < 18'),
          A('En küçük tam değer','−5 dahil değil; ilk tam sayı −4. Örneğin a = 0, b = 4.','0 − 4 = −4 ✓')],
 puf='Aralık 0’ı içeriyorsa karenin en küçük değeri 0’dır; uçların karelerine bakmak yetmez.')
S,lo,hi=ulasilan_tam(lambda a,b:b-a*a,(-5,2),(-1,3),kritik=(0,)); assert max(S)==2 and hi==3 and lo==-26 and 3-4==-1 and 3-1==2
P.K('0007',metin='−5 < a < 2 ve −1 < b < 3 olmak üzere a ve b gerçel sayılardır.\nBuna göre b − a² ifadesinin alabileceği en büyük tam sayı değeri kaçtır?',
 **SK(2,{-23:('islem','a²’nin en büyük değerini kullanıp 3 − 25’ten aşağı inmek; ifadeyi büyütmek için a² en küçük olmalı.'),-2:('bilgi','a²’nin aralığını uçların karelerinden (4, 25) kurmak; a = 0 olabilir.'),
          1:('islem','a²’nin en küçük değerini 1 sanmak; a = 0 için a² = 0.'),3:('bilgi','Uç değeri almak; b − a² < 3 kesin, 3’e ulaşılamaz.')}),
 istenen='b − a²’nin en büyük tam sayı değeri.',
 ipuclari=['a’nın aralığı 0’ı içeriyor; a² en az kaç?','−a²’nin aralığını bul (yön değişir).','b ile −a²’nin aralıklarını topla.'],bilgi=[KARE,TOPL,UC],
 adimlar=[A('a²’nin aralığı','a, 0’dan geçiyor. Üst sınır (−5)² = 25.','0 ≤ a² < 25'),
          A('−a²’nin aralığı','−1 ile çarpınca yön değişir.','−25 < −a² ≤ 0'),
          A('Topla','b ile taraf tarafa topla.','−1 + (−25) < b − a² < 3 + 0 ⇒ −26 < b − a² < 3'),
          A('En büyük tam değer','3 dahil değil. Örneğin a = 0, b = 2.','2 − 0 = 2 ✓')],
 puf='Bir kareyi çıkarırken ifade en büyük, kare 0 iken olur; aralık 0’ı içeriyorsa bunu kullan.')

# ===== 0008 ZOR · esz-siralama (K-ESZ-03)
def rs():
    return Fr(random.choice([-1,1])*random.randint(1,60),random.randint(1,6))
O=[t for t in ((rs(),rs(),rs()) for _ in range(60000)) if t[0]*t[1]>0 and t[1]*t[2]<0 and t[0]>t[2]]
assert len(O)>3000 and all(a>0 and b>0 and c<0 for a,b,c in O)
SEC={'a > b':lambda a,b,c:a>b,'b + c > 0':lambda a,b,c:b+c>0,'a · c < b':lambda a,b,c:a*c<b,'c² > a · b':lambda a,b,c:c*c>a*b,'a − b > c':lambda a,b,c:a-b>c}
dogru=[k for k,f in SEC.items() if all(f(*t) for t in O)]; assert dogru==['a · c < b'] and all(any(not f(*t) for t in O) for k,f in SEC.items() if k!='a · c < b')
assert not (1>2) and not (1+(-3)>0) and not ((-1)**2>3*3) and not (1-5>-2)
P.R('0008',**T('esz-siralama'),zorluk='zor',alt='Sıralama',kazanim='Çarpımların işaretinden ve bir sıralamadan sayıların işaretlerini durum ayırarak belirler; kesinlikle doğru ifadeyi seçer.',kalip='düz',adim=4,
 kart='K-ESZ-03 (işaret çıkarımı + kesin yargı) · yeni koşullar (iki çarpım işareti ve bir sıralama), şıklarda ifade',
 metin='a, b ve c sıfırdan farklı gerçel sayılar olmak üzere\na · b > 0\nb · c < 0\na > c\nolduğu biliniyor.\nBuna göre aşağıdakilerden hangisi kesinlikle doğrudur?',
 **SK('a · c < b',{'a > b':('dikkat','a ile b’nin ikisi de pozitif ama hangisinin büyük olduğu belli değil: a = 1, b = 2.'),'b + c > 0':('dikkat','b + c’nin işareti sayılara bağlı: b = 1, c = −3 için negatif.'),
                   'c² > a · b':('islem','c² ile a · b karşılaştırılamaz: a = b = 3, c = −1 için 1 < 9.'),'a − b > c':('islem','a − b negatif olup c’den küçük kalabilir: a = 1, b = 5, c = −2 için −4 < −2.')},
    sira=['a > b','b + c > 0','a · c < b','c² > a · b','a − b > c']),
 istenen='Her durumda doğru olan ifade.',
 ipuclari=['a · b > 0 ise a ile b’nin işaretleri için ne söylenir? b · c < 0 ise b ile c için?','Demek ki a ile c zıt işaretli. a > c bilgisi hangisinin pozitif olduğunu söyler?','İşaretleri bulunca şıkları dene; kesin olmayanlar için karşı örnek ara.'],bilgi=[ISR,KESIN],
 adimlar=[A('Çarpımlardan','a · b > 0 ⇒ a ile b aynı işaretli. b · c < 0 ⇒ b ile c zıt işaretli.','a ile c zıt işaretli'),
          A('Sıralamadan','Zıt işaretli iki sayıdan büyük olanı pozitiftir; a > c.','a > 0 · c < 0'),
          A('b’nin işareti','b, a ile aynı işaretli.','b > 0'),
          A('Şıkları dene','a × c negatif, b pozitif: her zaman a × c < b. Diğerleri için karşı örnek var (a = 1, b = 2 gibi).','a × c < 0 < b ✓')],
 puf='Çarpımın işaretinden “aynı/zıt işaretli” bilgisini çıkar; sıralama bilgisi hangi tarafın pozitif olduğunu söyler.')
O=[t for t in ((rs(),rs(),rs()) for _ in range(60000)) if t[0]*t[1]<0 and t[0]*t[2]>0 and t[1]>t[2]]
assert len(O)>3000 and all(a<0 and b>0 and c<0 for a,b,c in O)
SEC={'a < c':lambda a,b,c:a<c,'b + c > 0':lambda a,b,c:b+c>0,'a · b > c':lambda a,b,c:a*b>c,'a · c > b':lambda a,b,c:a*c>b,'a + c < b':lambda a,b,c:a+c<b}
dogru=[k for k,f in SEC.items() if all(f(*t) for t in O)]; assert dogru==['a + c < b'] and all(any(not f(*t) for t in O) for k,f in SEC.items() if k!='a + c < b')
assert not (-1<-2) and not (1-3>0) and not (-5*2>-1) and not ((-1)*(-1)>5)
P.K('0008',metin='a, b ve c sıfırdan farklı gerçel sayılardır.\na · b < 0\na · c > 0\nb > c\nolduğuna göre aşağıdakilerden hangisi her zaman doğrudur?',
 **SK('a + c < b',{'a < c':('dikkat','a ile c’nin ikisi de negatif ama sıraları belli değil: a = −1, c = −2.'),'b + c > 0':('dikkat','b + c’nin işareti sayılara bağlı: b = 1, c = −3 için negatif.'),
                   'a · b > c':('islem','a · b negatif ama c’den küçük olabilir: a = −5, b = 2, c = −1 için −10 < −1.'),'a · c > b':('islem','a · c pozitif ama b’den küçük olabilir: a = c = −1, b = 5 için 1 < 5.')},
    sira=['a < c','b + c > 0','a · b > c','a · c > b','a + c < b']),
 istenen='Her zaman doğru olan ifade.',
 ipuclari=['a · b < 0 ve a · c > 0 ise b ile c’nin işaretleri hakkında ne söylenir?','b > c bilgisiyle b’nin ve c’nin işaretini bul; sonra a’nınkini.','İki negatif sayının toplamı ile bir pozitif sayıyı karşılaştır.'],bilgi=[ISR,KESIN],
 adimlar=[A('Çarpımlardan','a ile b zıt, a ile c aynı işaretli.','b ile c zıt işaretli'),
          A('Sıralamadan','Zıt işaretlilerden büyük olan pozitif; b > c.','b > 0 · c < 0'),
          A('a’nın işareti','a, c ile aynı işaretli.','a < 0'),
          A('Şıkları dene','a + c iki negatifin toplamı, negatif; b pozitif. Diğerleri için karşı örnek var.','a + c < 0 < b ✓')],
 puf='Önce işaretleri kesinleştir, sonra her şıkkı ya kanıtla ya da karşı örnekle ele.')

P.yaz(os.path.join(H,ONEK+'-1.json'),os.path.join(H,ONEK+'-1-kardes.json'))
