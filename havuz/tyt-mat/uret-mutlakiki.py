"""Mutlak Değer · parti 2 (hafif mod): 9 yeni ana soru, kardeş yok, ipucu 1. Her cevap ve şık kodla (tam sayı / Fraction tarama) doğrulanır."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_mat as H
from _hafif_mat import *
H.KONU='Mutlak Değer'
P=Parti('mutlakiki','Mutlak Değer','mat|Mutlak Değer')
R_=range(-500,501)
def ints(c): return [x for x in R_ if c(x)]
def reals(c,lo=-60,hi=60,den=4):
    """Fraction ızgarasında (1/den adım) koşulu sağlayanlar."""
    return [Fr(i,den) for i in range(lo*den,hi*den+1) if c(Fr(i,den))]

TAN=B('Mutlak değer','|x| sayının sıfıra uzaklığıdır; x ≥ 0 ise |x| = x, x < 0 ise |x| = −x. Örnek: |5| = 5, |−5| = 5, |x − 2| için x < 2 ise 2 − x')
ESIT=B('|ifade| = k denklemi','k > 0 iken |A| = k denklemi A = k ya da A = −k anlamına gelir; iki kök de ayrı ayrı bulunur. Örnek: |x − 1| = 4 → x = 5 ya da x = −3')
IKIM=B('İki mutlak değerin eşitliği','|A| = |B| iken A = B ya da A = −B alınır. Örnek: |x| = |x − 4| → x = x − 4 (çözümsüz) ya da x = −(x − 4) → x = 2')
EPS=B('|x − a| < b ve |x − a| > b','|x − a| < b ise a − b < x < a + b (a’ya uzaklığı b’den az); |x − a| > b ise x < a − b ya da x > a + b. Örnek: |x − 1| < 3 → −2 < x < 4')
UZ=B('Sayı doğrusunda uzaklık','|x − a|, x ile a arasındaki uzaklıktır; |x − a| + |x − b| toplamı x iki sayının arasındayken en küçük ve sabittir. Örnek: |x − 1| + |x − 5| ≥ 4, en küçük değer 1 ile 5 arasında alınır')
SAPMA=B('Tolerans ve sapma','“a’dan en çok k sapma” |x − a| ≤ k demektir ve a − k ≤ x ≤ a + k aralığını verir. Örnek: 250’den en çok 15 sapan değerler 235 ile 265 arasındadır')

KY='ÖSYM 2018–2026 (mutlak değer, uzaklık, denklem ve eşitsizlik) · yayın soru bankaları (yalnız mantık) · MEB 9. sınıf'
kart('K-MTDB-01','Mutlak değerli ifadeyi işaretine göre açma','Değişkenin aralığı verildiğinde her mutlak değerin içindeki ifadenin işareti belirlenip ifade açılır ve sadeleştirilir.','Negatif işaretli ifadede parantez kullanmamak; içeriğin işaretini yanlış belirlemek.','kolay','düz',2,'mdb-ac','Mutlak değerli ifadeyi işaretine göre açma',KY)
kart('K-MTDB-02','Mutlak değerli denklem','|A| = k ve |A| = |B| denklemleri iki duruma ayrılır; çözümlerin toplamı ya da çarpımı istenir, katsayılı ifadelerde önce mutlak değer yalnız bırakılır.','Yalnız bir durumu çözmek; mutlak değeri yalnız bırakmadan içeriği çözmek; iki duruma ayırırken işaret hatası yapmak.','orta','düz',3,'mdb-denklem','Mutlak değerli denklem ve çözümlerin çarpımı',KY)
kart('K-MTDB-03','Mutlak değerli eşitsizlik ve tam sayı adedi','|x − a| < b, |x − a| > b ve |A| < |B| eşitsizlikleri aralık ya da uzaklıkla çözülür; belirli bir tam sayı aralığında sağlayan değerler sayılır.','< ile ≤ ve > ile ≥ ayrımını yapmamak; “>” biçiminde iki ayrı aralığı birleştirmek yerine birini almak.','orta','düz',3,'mdb-esitsizlik','Mutlak değerli eşitsizlikte tam sayı adedi',KY)
kart('K-MTDB-04','Sayı doğrusunda uzaklık yorumu','|x − a| + |x − b| gibi ifadelerde x’in iki noktaya uzaklıklar toplamı yorumlanır; en küçük değer iki nokta arasındaki uzaklıktır ve aralık içinde sabittir.','En küçük değeri bir uçta aramak; sabit bölge ile eğimli bölgeyi karıştırmak; birden çok terimde ortadaki noktayı seçmemek.','zor','yeni nesil',4,'mdb-uzaklik','Uzaklık toplamının en küçük değeri ve çözümleri',KY)
kart('K-MTDB-05','Tolerans ve sapma problemleri','Hikâyedeki en çok sapma miktarı |x − a| ≤ k eşitsizliğine çevrilir; aralığın uçları ve iki değer arasındaki fark yorumlanır.','Sapma miktarını tam aralık genişliği sanmak; uçları dahil etmek ya da etmemek; tam sayı adedinde +1’i unutmak.','orta','hikâyeli',3,'mdb-model','Tolerans ve sapma problemleri',KY)
kart('K-MTDB-06','Öncüllü mutlak değer','Verilen mutlak değer koşulundan x’in aralığı bulunur ve öncüllerdeki ifadeler uç değerler dahil denenerek kesinlikle doğru olanlar belirlenir.','Yalnız bir değer deneyip öncüle karar vermek; uç değerleri unutmak; < ile ≤’yi karıştırmak.','zor','öncüllü',4,'mdb-onculu','Öncüllü mutlak değer ve aralık',KY)

# ---------- 01 · kolay · açma ----------
for a in [Fr(-299,100),Fr(-2),Fr(0),Fr(1),Fr(199,100)]:
    assert -3<a<2 and abs(a+3)+abs(a-2)==5
    assert -(a+3)+(a-2)==-5 and -(a+3)-(a-2)==-2*a-1 and (a+3)+(a-2)==2*a+1 and (a+3)+(-a-2)==1
for a in [Fr(-299,100),Fr(1),Fr(-1,3)]: assert len({5,-5,-2*a-1,2*a+1,a+5})==5 and -(a+3)+(a-2)==-5 and (a+3)+2==a+5
mk(P,'0001',tipId='mdb-ac',tip='Mutlak değerli ifadeyi işaretine göre açma',z='kolay',alt='Mutlak Değer Açma',kaz='Değişkenin aralığına göre iki mutlak değeri açıp toplayarak sabit bir değer bulur.',kalip='düz',adim=2,
 kart='K-MTDB-01 (işarete göre açma) · −3 < a < 2 iken |a + 3| + |a − 2| sabit değeri',
 metin='−3 < a < 2 olmak üzere\n|a + 3| + |a − 2|\nifadesi aşağıdakilerden hangisine eşittir?',
 dogru='5',sira=['−5','−2a − 1','2a + 1','5','a + 5'],yan=[('−5','|a + 3|’ü −(a + 3), |a − 2|’yi (a − 2) açmış (iki işareti de ters yapmış): −(a + 3) + (a − 2) = −5.','bilgi'),('−2a − 1','İki mutlak değeri de negatif işaretle açmış: −(a + 3) − (a − 2); a + 3 pozitiftir, a − 2 negatiftir.','bilgi'),('a + 5','|a − 2| = 2 − a yazacakken yalnız 2 yazıp −a’yı unutmuş: (a + 3) + 2 = a + 5.','islem'),('2a + 1','İki mutlak değeri de pozitif açmış: (a + 3) + (a − 2); a − 2 negatiftir, mutlak değeri 2 − a’dır.','bilgi')],
 istenen='|a + 3| + |a − 2| ifadesinin eşiti.',
 ip=['−3 < a < 2 için a + 3 ve a − 2 sayılarının işaretlerini ayrı ayrı belirle.'],
 bilgi=[TAN],
 ad=[A('İşaretleri belirle','a > −3 olduğundan a + 3 pozitiftir; a < 2 olduğundan a − 2 negatiftir.','a + 3 > 0 · a − 2 < 0'),A('Mutlak değerleri aç','Pozitif ifade aynen, negatif ifade işareti değiştirilerek açılır.','|a + 3| = a + 3 · |a − 2| = −(a − 2) = 2 − a'),A('Topla','a’lar birbirini götürür.','(a + 3) + (2 − a) = 5')],
 puf='Mutlak değer içindeki ifadenin işaretini önce belirle; negatifse parantezle eksi koyup aç.')

# ---------- 02 · kolay · 2|x − 1| + 3 = 11 çarpım ----------
c5=reals(lambda x:2*abs(x-1)+3==11,-40,40,1); assert c5==[-3,5] and c5[0]*c5[1]==-15 and sum(c5)==2
f1=abs(c5[0])*abs(c5[1]); assert f1==15
f2=[x for x in range(-60,61) if abs(x-1)==8]; assert f2==[-7,9] and f2[0]*f2[1]==-63
assert len({-15,2,5,15,-63})==5
mk(P,'0002',tipId='mdb-denklem',tip='Mutlak değerli denklem ve çözümlerin çarpımı',z='kolay',alt='Mutlak Değerli Denklem',kaz='Katsayılı mutlak değerli denklemi önce mutlak değeri yalnız bırakıp iki duruma ayırarak çözer ve köklerin çarpımını bulur.',kalip='düz',adim=3,
 kart='K-MTDB-02 (mutlak değerli denklem) · 2|x − 1| + 3 = 11 denkleminde kökler çarpımı',
 metin='2|x − 1| + 3 = 11\ndenkleminin çözüm kümesindeki elemanların çarpımı kaçtır?',
 dogru=-15,yan=[(2,'Köklerin çarpımı yerine toplamını (5 + (−3) = 2) yazmış.','dikkat'),(5,'Yalnız |x − 1| = 4 → x − 1 = 4 durumunu çözüp tek kök (5) bulmuş; x − 1 = −4 durumunu unutmuş.','bilgi'),(15,'Kökleri −3 ve 5 bulmuş ama −3’ün işaretini atıp 3 × 5 = 15 yazmış.','islem'),(-63,'2’ye bölmeyi unutup |x − 1| = 8 çözmüş; kökler 9 ve −7, çarpım −63.','islem')],
 istenen='Denklemin çözüm kümesindeki elemanların çarpımı.',
 ip=['Önce mutlak değeri yalnız bırak: 3’ü karşıya at, sonra 2’ye böl.'],
 bilgi=[ESIT],
 ad=[A('Mutlak değeri yalnız bırak','3’ü karşıya at, sonra 2’ye böl.','2|x − 1| = 8 → |x − 1| = 4'),A('İki duruma ayır','İçerik 4 ya da −4 olur.','x − 1 = 4 → x = 5 · x − 1 = −4 → x = −3'),A('Çarp','Köklerin çarpımını al.','5 × (−3) = −15')],
 puf='Katsayı ve sabit varsa önce |…| yalnız bırakılır, sonra iki duruma ayrılır.')

# ---------- 03 · orta · |3x − 2| = |x + 6| ----------
c2=reals(lambda x:abs(3*x-2)==abs(x+6),-40,40,2); assert c2==[-1,4] and c2[0]*c2[1]==-4 and sum(c2)==3
t_=[x for x in [Fr(i,2) for i in range(-60,61)] if 3*x-2==-x+6]; assert t_==[2] and 4*2==8
assert len({-4,-1,3,4,8})==5
mk(P,'0003',tipId='mdb-denklem',tip='Mutlak değerli denklem ve çözümlerin çarpımı',z='orta',alt='Mutlak Değerli Denklem',kaz='İki mutlak değerin eşitliğini iki duruma ayırarak çözer ve köklerin çarpımını bulur.',kalip='düz',adim=3,
 kart='K-MTDB-02 (mutlak değerli denklem) · |3x − 2| = |x + 6| ve köklerin çarpımı',
 metin='|3x − 2| = |x + 6|\neşitliğini sağlayan x değerlerinin çarpımı kaçtır?',
 dogru=-4,yan=[(-1,'Yalnız 3x − 2 = −(x + 6) durumunu çözüp tek kök (−1) bulmuş.','bilgi'),(3,'İki kökün toplamını (4 + (−1) = 3) bulmuş; soru çarpımı istiyor.','dikkat'),(4,'Yalnız 3x − 2 = x + 6 durumunu çözüp tek kök (4) bulmuş.','bilgi'),(8,'İkinci durumda −(x + 6) yerine −x + 6 yazıp x = 2 bulmuş; çarpım 4 × 2 = 8.','islem')],
 istenen='Köklerin çarpımı.',
 ip=['|A| = |B| olduğunda A = B ya da A = −B durumlarını ayrı ayrı çöz.'],
 bilgi=[IKIM],
 ad=[A('Birinci durum','İki içeriği eşitle.','3x − 2 = x + 6 → 2x = 8 → x = 4'),A('İkinci durum','Bir tarafı eksiyle çarpıp eşitle; eksi tüm ifadeye geçer.','3x − 2 = −(x + 6) → 4x = −4 → x = −1'),A('Çarp','İki kökü çarp.','4 × (−1) = −4 · kontrol: |10| = |10| ve |−5| = |5|')],
 puf='|A| = |B| için A = B ve A = −B durumlarını çöz; eksi işaretini tüm parantezin başına koy.')

# ---------- 04 · orta · |x−1| > 3, −5 ≤ x ≤ 7 ----------
D=[x for x in range(-5,8)]; assert len(D)==13
m3=[x for x in D if abs(x-1)>3]; assert m3==[-5,-4,-3,5,6,7] and len(m3)==6
g1=len([x for x in D if abs(x-1)>=3]); g2=len([x for x in D if abs(x-1)<=3]); g3=len([x for x in D if x-1>3]); g4=len(D)
assert (g1,g2,g3,g4)==(8,7,3,13) and len({6,g1,g2,g3,g4})==5
mk(P,'0004',tipId='mdb-esitsizlik',tip='Mutlak değerli eşitsizlikte tam sayı adedi',z='orta',alt='Mutlak Değerli Eşitsizlik',kaz='|x − a| > b eşitsizliğini iki ayrı aralığa dönüştürüp belirli bir tam sayı aralığında sağlayan değerleri sayar.',kalip='düz',adim=3,
 kart='K-MTDB-03 (mutlak değerli eşitsizlik) · |x − 1| > 3 ve −5 ≤ x ≤ 7 aralığındaki tam sayılar',
 metin='x bir tam sayı ve −5 ≤ x ≤ 7 olmak üzere\n|x − 1| > 3\neşitsizliğini sağlayan kaç farklı x değeri vardır?',
 dogru=6,yan=[(g3,'|x − 1| > 3 için yalnız x − 1 > 3 durumunu almış (x = 5, 6, 7); x − 1 < −3 durumunu da eklemeliydi.','bilgi'),(g2,'Eşitsizliği ters yorumlayıp |x − 1| ≤ 3 sağlayan değerleri (−2’den 4’e kadar) saymış.','dikkat'),(g1,'“>” yerine “≥” kullanıp 4 ve −2’yi de saymış; 4 − 1 = 3 olduğundan eşitlik sağlanır, “>” sağlanmaz.','dikkat'),(g4,'Koşulu hiç uygulamayıp aralıktaki bütün tam sayıları saymış.','dikkat')],
 istenen='Eşitsizliği sağlayan tam sayı adedi.',
 ip=['|x − 1| > 3 koşulunu iki parçaya ayır: x − 1 > 3 ya da x − 1 < −3.'],
 bilgi=[EPS],
 ad=[A('Eşitsizliği ayır','Uzaklığı 3’ten büyük olan sayılar iki ayrı yerde bulunur.','x − 1 > 3 → x > 4 · x − 1 < −3 → x < −2'),A('Aralıkla kesiştir','−5 ≤ x ≤ 7 aralığındaki tam sayıları seç.','x = 5, 6, 7 · x = −5, −4, −3'),A('Say','İki gruptaki sayıları topla.','3 + 3 = 6')],
 puf='|x − a| > b iki ayrı aralık verir (iki uç da hariç); tam sayıları iki yandan ayrı ayrı say.')

# ---------- 05 · orta · tablet farkı ----------
ok_=[Fr(m) for m in range(200,300) if abs(m-250)<=15]; assert max(ok_)-min(ok_)==30 and min(ok_)==235 and max(ok_)==265
h2=max(m for m in range(200,300) if abs(m-250)<15)-min(m for m in range(200,300) if abs(m-250)<15); assert h2==28 and 264-236==28    # tam sayı sanıp sınırları dışlama
h3=len([m for m in range(200,300) if abs(m-250)<=15]); assert h3==31
assert len({30,15,h2,h3,265})==5
mk(P,'0005',tipId='mdb-model',tip='Tolerans ve sapma problemleri',z='orta',alt='Tolerans Problemleri',kaz='En çok sapma koşulunu mutlak değerli eşitsizliğe çevirip kabul edilen iki değer arasındaki en büyük farkı bulur.',kalip='hikâyeli',adim=3,
 kart='K-MTDB-05 (tolerans) · 250 mg’dan en çok 15 mg sapan tabletlerde iki tablet arasındaki en büyük fark',
 metin='Bir ilaç fabrikasında üretilen tabletlerin kütlesi 250 mg’dan en çok 15 mg sapabilir; kütlesi bu sınırlar içinde (sınırlar dahil) kalan tabletler kabul edilir. Kabul edilen tabletlerin kütleleri gerçel sayıdır.\nKabul edilen iki tabletin kütleleri arasındaki fark en çok kaç mg olabilir?',
 dogru=30,yan=[(15,'Yalnız bir tarafın sapmasını (15 mg) fark sanmış; iki tablet zıt yönlerde sapabilir.','dikkat'),(h2,'Kütleleri tam sayı sanıp sınırları dışarıda tutarak 236 ile 264’ü almış: 264 − 236 = 28; oysa sınırlar dahildir ve kütle gerçel sayıdır.','dikkat'),(h3,'235’ten 265’e kadar tam sayıları sayıp 31 bulmuş; sorulan adet değil fark.','dikkat'),(265,'Kabul edilen en büyük kütleyi (265 mg) yazmış; sorulan iki kütlenin farkıdır.','dikkat')],
 istenen='Kabul edilen iki tabletin kütle farkının en büyük değeri (mg).',
 ip=['|m − 250| ≤ 15 koşulunu m’nin aralığı olarak yaz; en küçük ve en büyük kütleyi bul.'],
 bilgi=[SAPMA],
 ad=[A('Eşitsizliği kur','Kütle m için 250’den sapma en çok 15’tir.','|m − 250| ≤ 15'),A('Aralığı yaz','Mutlak değeri aç.','−15 ≤ m − 250 ≤ 15 → 235 ≤ m ≤ 265'),A('Farkı bul','En büyük fark, en büyük ile en küçük kütlenin farkıdır.','265 − 235 = 30 mg')],
 puf='“a’dan en çok k sapma” a − k ile a + k arasını verir; iki değer arasındaki en büyük fark 2k’dır.')

# ---------- 06 · orta · iki market, uzaklık toplamı ≤ 10 ----------
e6=[x for x in range(-60,61) if abs(x+3)+abs(x-5)<=10]; assert e6==list(range(-4,7)) and len(e6)==11 and min(abs(x+3)+abs(x-5) for x in range(-60,61))==8
j1=len([x for x in range(-60,61) if abs(x+3)<=5 and abs(x-5)<=5]); assert j1==3
j2=8; j3=len(range(-3,6)); assert j3==9
j4=6-(-4); assert j4==10
assert len({11,j1,j2,j3,j4})==5
mk(P,'0006',tipId='mdb-uzaklik',tip='Uzaklık toplamının en küçük değeri ve çözümleri',z='orta',alt='Uzaklık Yorumu',kaz='İki noktaya uzaklıkların toplamı sınırlandığında, sayı doğrusunda mutlak değerli eşitsizliği kurup tam sayı konumlarını sayar.',kalip='hikâyeli',adim=4,
 kart='K-MTDB-04 (uzaklık yorumu) · iki marketin konumuna uzaklıklar toplamı en çok 10 km, tam sayı konum sayısı',
 metin='Düz bir yol üzerinde, başlangıç noktasına göre konumları −3 km ve 5 km olan iki market vardır. Bir ev, bu yol üzerinde konumu tam sayı (km) olan bir noktaya yapılacaktır. Evden iki markete olan uzaklıkların toplamı en çok 10 km olmalıdır.\nBuna göre ev kaç farklı konuma yapılabilir?',
 dogru=11,yan=[(j1,'Her marketin uzaklığının en çok 5 km olması gerektiğini sanıp iki koşulun ortak konumlarını (0, 1, 2) saymış.','dikkat'),(j2,'Uzaklıklar toplamının en küçük değerini (8) sayı adedi sanmış.','dikkat'),(j3,'Yalnız iki market arasındaki konumları (−3’ten 5’e) saymış; marketlerin dışında da konum olabilir.','bilgi'),(j4,'Konum sayısını uçların farkı (6 − (−4)) kadar bulmuş; uç değerler dahil olduğundan 1 fazla sayılmalıdır.','islem')],
 istenen='Evin yapılabileceği tam sayı konum adedi.',
 ip=['Ev konumu x olsun: |x + 3| + |x − 5| ≤ 10. İki market arasında toplamın kaç olduğuna bak.'],
 bilgi=[UZ],
 ad=[A('Eşitsizliği kur','Ev konumu x ise uzaklıklar |x + 3| ve |x − 5| olur.','|x + 3| + |x − 5| ≤ 10'),A('Arada toplamı bul','−3 ile 5 arasında toplam, marketler arası uzaklığa eşit ve sabittir.','−3 ≤ x ≤ 5 → toplam = 8 ≤ 10 (hepsi uygun)'),A('Dışarıda sınırı bul','5’in sağında toplam 2x − 2 olur; −3’ün solunda −2x + 2.','2x − 2 ≤ 10 → x ≤ 6 · −2x + 2 ≤ 10 → x ≥ −4'),A('Say','−4’ten 6’ya kadar tam sayılar.','6 − (−4) + 1 = 11')],
 puf='İki noktanın arasında uzaklık toplamı sabittir; dışarıda her birim 2 artar, sınır buradan bulunur.')

# ---------- Z1 · zor · üç terimli uzaklık toplamı, f(x) = 16 ----------
f=lambda x:abs(x+4)+abs(x-2)+abs(x-8)
assert min(f(Fr(i,2)) for i in range(-40,41))==12 and f(Fr(2))==12
z1=reals(lambda x:f(x)==16,-30,30,2); assert z1==[-2,6] and z1[0]*z1[1]==-12 and sum(z1)==4
assert f(Fr(6))==16 and f(Fr(-2))==16
assert f(Fr(-4))==18 and f(Fr(0))!=16
assert 6*(-4)==-24
r_=[x for x in range(-30,31) if 12+2*(x-2)==16]; assert r_==[4]
assert len({-12,-24,-2,4,6})==5
mk(P,'0007',tipId='mdb-uzaklik',tip='Uzaklık toplamının en küçük değeri ve çözümleri',z='zor',alt='Uzaklık Yorumu',kaz='Üç terimli uzaklık toplamının en küçük değerini ortadaki noktada bulup verilen değere ulaşan iki noktayı belirler.',kalip='düz',adim=5,
 kart='K-MTDB-04 (uzaklık yorumu) · |x + 4| + |x − 2| + |x − 8| = 16 köklerinin çarpımı',
 metin='x gerçel sayısı için\n|x + 4| + |x − 2| + |x − 8| = 16\neşitliğini sağlayan x değerlerinin çarpımı kaçtır?',
 dogru=-12,yan=[(-24,'Sol kökü −4 (terimin sıfırı) sanıp 6 × (−4) = −24 yazmış; oysa f(−4) = 18 ≠ 16’dır.','dikkat'),(-2,'Yalnız soldaki kökü (−2) bulup sağdaki kökü (6) eklememiş.','dikkat'),(4,'Köklerin (−2 ve 6) toplamını yazmış; soru çarpımı istiyor.','dikkat'),(6,'Yalnız sağdaki kökü (6) bulup soldaki kökü (−2) eklememiş.','dikkat')],
 istenen='Eşitliği sağlayan x değerlerinin çarpımı.',
 ip=['Üç uzaklık toplamı en küçük değerini ortadaki sayıda (2) alır; oradan başlayıp her yönde toplamın nasıl arttığına bak.'],
 bilgi=[UZ,B('Çok terimli uzaklık toplamı','|x − a| + |x − b| + |x − c| toplamı, x en ortadaki sayıya eşit olunca en küçüktür; sağında ve solunda toplam her birim 1 artar (iki terim artar, bir terim azalır). Örnek: |x| + |x − 2| + |x − 6| en küçük değerini x = 2’de alır: 2 + 0 + 4 = 6')],
 ad=[A('En küçük değeri bul','Üç sayının ortancası 2’dir; toplam x = 2’de en küçüktür.','f(2) = |6| + 0 + |−6| = 12'),A('Eğimi bul','2’nin sağında (8’e kadar) iki terim artar, bir terim azalır: f her birim 1 artar.','f(x) = 12 + (x − 2) → 12 + (x − 2) = 16 → x = 6'),A('Sol kökü bul','2’nin solunda (−4’e kadar) da f her birim 1 artar.','12 + (2 − x) = 16 → x = −2'),A('Kontrol et','İki kökü f’de dene.','f(6) = 10 + 4 + 2 = 16 · f(−2) = 2 + 4 + 10 = 16'),A('Çarp','İki kökü çarp.','6 × (−2) = −12')],
 puf='Üç terimli uzaklık toplamı ortancada en küçüktür ve iki yana birim başına 1 artar (iki terim artar, bir terim azalır).')

# ---------- Z2 · zor · öncüllü |x − 3| ≤ 2 ----------
X=reals(lambda x:abs(x-3)<=2,-20,20,8); assert min(X)==1 and max(X)==5
v=[]
for x in X: v.append((abs(x-2)<=3,abs(x-4)<2,abs(x+1)>2))
assert all(t[0] for t in v) and any(not t[1] for t in v) and any(not t[2] for t in v) and any(t[1] for t in v) and any(t[2] for t in v)
OPM=['Yalnız I','Yalnız III','I ve II','II ve III','I, II ve III']
assert abs(1-3)<=2 and abs(1-4)==3 and abs(1+1)==2
mk(P,'0008',tipId='mdb-onculu',tip='Öncüllü mutlak değer ve aralık',z='orta',alt='Öncüllü Mutlak Değer',kaz='Mutlak değer koşulundan x’in aralığını bulup öncüllerdeki mutlak değerli ifadeleri uç değerler dahil değerlendirir.',kalip='öncüllü',adim=4,
 kart='K-MTDB-06 (öncüllü mutlak değer) · |x − 3| ≤ 2 için üç mutlak değer öncülü ve uç değer denetimi',
 metin='x gerçel sayısı için\n|x − 3| ≤ 2\nolduğu biliniyor.\nBuna göre\nI. |x − 2| ≤ 3\nII. |x − 4| < 2\nIII. |x + 1| > 2\nifadelerinden hangileri kesinlikle doğrudur?',
 dogru='Yalnız I',sira=OPM,yan=[('I ve II','II’yi x = 3 gibi tek bir değerle deneyip doğru sanmış; x = 1 için |x − 4| = 3 olur, “< 2” sağlanmaz.','dikkat'),('Yalnız III','II’yi x = 1 ile doğru biçimde eleyip I’i x = 5 ile |5 − 2| = 3’ü “3’ten küçük değil” sayarak elemiş (“≤” unutulmuş); III’ü ise x = 3 ile deneyip doğru bulmuş.','dikkat'),('II ve III','I’i x = 5 ile deneyip |5 − 2| = 3’ü “3’ten küçük değil” diye elemiş (oysa “≤” vardır); II ve III’ü x = 3 ile deneyip doğru bulmuş.','dikkat'),('I, II ve III','x’i 3 ile 5 arasında sanıp (alt sınırı atlayıp) üçünü de doğru bulmuş; x aralığı 1 ≤ x ≤ 5’tir.','bilgi')],
 istenen='Kesinlikle doğru olan öncüller.',
 ip=['Önce x’in aralığını bul; sonra her öncülü iki uç değerde (en küçük ve en büyük x) dene.'],
 bilgi=[EPS],
 ad=[A('x’in aralığını bul','|x − 3| ≤ 2 ise x’in 3’e uzaklığı en çok 2’dir.','1 ≤ x ≤ 5'),A('I’i uçlarda dene','x − 2, 1 ile 5 arasında değişen x için −1 ile 3 arasındadır.','|x − 2| ≤ 3 → I doğru'),A('II ve III’ü uçlarda dene','x = 1 için II: |1 − 4| = 3 < 2 değil. x = 1 için III: |1 + 1| = 2 > 2 değil.','II yanlış · III yanlış'),A('Sonucu yaz','Kesinlikle doğru olan yalnız I’dir.','Yalnız I')],
 puf='Öncüllerde “kesinlikle” için aralığın uç değerlerini de dene; “<” ve “≤” farkı çoğu zaman uçlarda ortaya çıkar.')

# ---------- Z3 · zor · |x − 4| < |x + 2| < 7, toplam ----------
z3=[x for x in range(-60,61) if abs(x-4)<abs(x+2)<7]; assert z3==[2,3,4] and sum(z3)==9
for x in range(-60,61): assert (abs(x-4)<abs(x+2))==(x>1)
q1=sum(x for x in range(-60,61) if abs(x-4)<=abs(x+2)<7); assert q1==10          # eşitliği (x = 1) da almış
q2=sum(x for x in range(-60,61) if abs(x-4)<abs(x+2)<=7); assert q2==14         # 7’yi de almış
q3=sum(x for x in range(-60,61) if x>3 and abs(x+2)<7); assert q3==4              # orta noktayı 3 sanmış
q4=sum(x for x in range(-60,61) if abs(x+2)<7); assert q4==-26                    # yalnız ikinci eşitsizlik
assert len({9,q1,q2,q3,q4})==5
UZ2=B('İki uzaklığın karşılaştırılması','|x − a| < |x − b| ise x, a’ya b’den daha yakındır; ayırıcı nokta (a + b) ÷ 2’dir. Örnek: |x − 1| < |x − 5| → x < 3. Bir de kare alarak çözülebilir: (x − 1)² < (x − 5)² → x < 3')
mk(P,'0009',tipId='mdb-esitsizlik',tip='Mutlak değerli eşitsizlikte tam sayı adedi',z='zor',alt='İki Mutlak Değerli Eşitsizlik',kaz='İki mutlak değerin karşılaştırıldığı ve bir üst sınırla birleştirilen çift taraflı eşitsizliği çözüp tam sayı çözümlerinin toplamını bulur.',kalip='düz',adim=5,
 kart='K-MTDB-03 (mutlak değerli eşitsizlik) · |x − 4| < |x + 2| < 7 koşulunu sağlayan tam sayıların toplamı',
 metin='x bir tam sayı olmak üzere\n|x − 4| < |x + 2| < 7\nkoşulunu sağlayan x değerlerinin toplamı kaçtır?',
 dogru=9,yan=[(q1,'İlk eşitsizlikte “<” yerine “≤” alıp x = 1’i de sayarak 1 + 2 + 3 + 4 = 10 bulmuş; 1 için |1 − 4| = |1 + 2| olur, “<” sağlanmaz.','dikkat'),(q2,'|x + 2| < 7’yi “≤ 7” alıp x = 5’i de sayarak 14 bulmuş; 5 için |5 + 2| = 7, “< 7” sağlanmaz.','dikkat'),(q3,'4 ile −2’nin orta noktasını 3 almış (x > 3); oysa orta nokta (4 + (−2)) ÷ 2 = 1’dir. Yalnız x = 4 kalmış.','islem'),(q4,'Yalnız |x + 2| < 7 koşulunu çözüp (−9 < x < 5) −8’den 4’e kadar tam sayıları toplamış; ilk eşitsizliği kullanmamış.','dikkat')],
 istenen='Koşulu sağlayan tam sayıların toplamı.',
 ip=['Çift taraflı eşitsizliği ikiye ayır: |x − 4| < |x + 2| için x’in hangi sayıya daha yakın olduğuna bak, |x + 2| < 7’yi ayrı çöz.'],
 bilgi=[UZ2,EPS],
 ad=[A('İlk eşitsizliği yorumla','x, 4’e −2’den daha yakın olmalı; ayırıcı nokta ortadır.','(4 + (−2)) ÷ 2 = 1 → x > 1'),A('İkinci eşitsizliği çöz','|x + 2| < 7, x’in −2’ye uzaklığının 7’den az olması demektir.','−7 < x + 2 < 7 → −9 < x < 5'),A('Kesiştir','İki koşulu birlikte sağlayan tam sayıları bul.','1 < x < 5 → x = 2, 3, 4'),A('Topla','Bulunan sayıları topla.','2 + 3 + 4 = 9')],
 puf='|x − a| < |x − b| için x’i a ile b’nin orta noktasının a tarafında ara; ikinci koşulu ayrı bir aralıkla kesiştir.')

bitir(P,'mutlakiki','mat|Mutlak Değer')
from collections import Counter
print(Counter(q['cevap']['sik'] for q in P.ANA),Counter(q['zorluk'] for q in P.ANA))
