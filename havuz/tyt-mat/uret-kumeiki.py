"""Kümeler ve Kartezyen Çarpım · parti 2 (hafif mod): 14 ana soru, kardeş yok, ipucu 1. Her cevap ve çeldirici kodla doğrulanır."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_mat as H
from _hafif_mat import *
from itertools import combinations
H.KONU='Kümeler ve Kartezyen Çarpım'
UK='matd|Kümeler-Kartezyen Çarpım'
P=Parti('kumeiki','Kümeler ve Kartezyen Çarpım',UK)
KY='ÖSYM 2018–2026 TYT Matematik (kümeler) · yayın soru bankaları (yalnız mantık) · MEB 9. sınıf'
GOS=B('Küme gösterimi','{x : x ∈ ℤ ve a < x ≤ b} kümesine aralığa uyan tam sayılar yazılır; ≤ olan uç dahil, < olan uç dahil değildir. Örnek: {x : x ∈ ℤ ve 1 < x ≤ 4} = {2, 3, 4} olup 3 elemanlıdır')
ALT=B('Alt küme sayısı','n elemanlı bir kümenin 2ⁿ alt kümesi vardır; bazı elemanların bulunması ya da bulunmaması şart koşulunca o elemanlar sabitlenir, kalan elemanlar serbesttir. Örnek: {a, b, c, d} kümesinin a’yı içeren alt kümeleri 2³ = 8 tanedir')
FORM=B('Birleşimin eleman sayısı','s(A ∪ B) = s(A) + s(B) − s(A ∩ B). Ayrıca s(A \\ B) = s(A) − s(A ∩ B). Örnek: s(A) = 5, s(B) = 4, s(A ∩ B) = 2 ise s(A ∪ B) = 5 + 4 − 2 = 7')
TUM=B('Tümleyen','Evrensel küme E iken s(A′) = s(E) − s(A) olur; (A ∪ B)′ kümesi hiçbirinde olmayan elemanlardır. Örnek: s(E) = 10, s(A ∪ B) = 8 ise s((A ∪ B)′) = 2')
VENN=B('İki kümeli problem','Her kişi yalnız A, yalnız B, ikisi ya da hiçbiri bölgelerinden tam birindedir; bölge sayılarının toplamı toplam kişi sayısına eşittir. Örnek: 20 kişide 12 A, 10 B, 5 ortak ise en az birinde olan 12 + 10 − 5 = 17 kişidir')
VENN3=B('Üç kümeli sayma','Üç kümeli Venn şemasında 8 bölge vardır (7 bölge ve dışarısı); her kişi tam bir bölgededir. Bir kümenin elemanları, o kümeyi içeren 4 bölgenin toplamıdır. Örnek: A kümesi = yalnız A + A ile B + A ile C + üçü birden')
KART=B('Kartezyen çarpım','s(A × B) = s(A) · s(B) ve (a, b) sıralı ikilisinde sıra önemlidir: (1, 2) ≠ (2, 1). Örnek: A = {1, 2}, B = {3, 4, 5} için s(A × B) = 2 · 3 = 6; (A × B) ∩ (B × A) = (A ∩ B) × (A ∩ B)')
YEN=B('Tanımlı işlem','Soruda tanımlanan işlem, bilinen küme işlemleriyle yazılır ve verilen bilgiye uygulanır. Örnek: A ∗ B = A ∪ B tanımında s(A ∗ B) = s(A ∪ B) olur')

kart('K-KMB-01','Küme gösterimi ve eleman sayısı','Koşulla verilen kümenin elemanları (eşitsizlik, asal, tam sayı) yazılıp sayılır.','Aralığın uçlarını yanlış dahil etmek; tam sayı yerine doğal sayı almak; koşulu x yerine ifadeye değil x’e uygulamak.','kolay','düz',2,'kmb-gosterim','Küme gösterimi ve eleman sayısı',KY)
kart('K-KMB-02','Alt küme sayısı','Eleman sayısından alt küme sayısı ya da koşullu (belirli eleman bulunan/bulunmayan) alt küme sayısı 2 üzeri serbest eleman ile bulunur.','Koşullu elemanları serbest saymak; birbirine bağlı iki koşulu bağımsız saymak.','orta','düz',3,'kmb-altkume','Alt küme sayısı',KY)
kart('K-KMB-03','Küme işlemleri ve s(A ∪ B)','Birleşim, kesişim, fark ve tümleyen eleman sayıları ve alt küme ilişkileri üzerinden yorum.','Kesişimi iki kez saymak; fark ile tümleyeni karıştırmak; alt küme kavramını ters okumak.','kolay','düz',2,'kmb-islem','Küme işlemleri ve eleman sayısı',KY)
kart('K-KMB-04','İki ve üç kümeli problemler','Hikâyeli iki kümeli (yalnız, en az, hiçbiri) ve bölgeleri verilen üç kümeli sayma.','Kesişimi iki kez eklemek; hiçbirine ait olanı unutmak ya da fazla saymak.','orta','hikâyeli',3,'kmb-venn','İki ve üç kümeli problemler',KY)
kart('K-KMB-05','Kartezyen çarpım','Eleman sayısı çarpımı, koşullu ikililerin sayılması, (A×B)∩(B×A) ilişkisi.','Sıralı ikilide sırayı önemsememek; koşulu yalnız bir bileşene uygulamak.','orta','düz',3,'kmb-kartezyen','Kartezyen çarpım',KY)
kart('K-KMB-06','Tanımlı küme işlemi (yeni nesil)','Soruda tanımlanan yeni işlem bilinen küme işlemlerine çevrilir.','Tanımı yanlış okumak; ortak elemanları sayıma almak.','orta','yeni nesil',3,'kmb-yeninesil','Yeni nesil: tanımlı küme işlemi',KY)

# 01 gösterim
A1=[x for x in range(-30,30) if -5<2*x+1<=11]; assert A1==list(range(-2,6)) and len(A1)==8
assert len([x for x in range(-30,30) if -5<2*x+1<11])==7 and len([x for x in range(-30,30) if -5<=2*x+1<=11])==9
assert len([x for x in A1 if x>=0])==6 and len([x for x in range(-30,30) if x>0 and -5<2*x+1<=11])==5
mk(P,'0001',tipId='kmb-gosterim',tip='Küme gösterimi ve eleman sayısı',z='kolay',alt='Küme Gösterimi',kaz='Eşitsizlikle tanımlı kümenin elemanlarını bulup sayar.',kalip='düz',adim=2,
 kart='K-KMB-01 · eşitsizlikle tanımlı tam sayı kümesi',
 metin='A = {x : x ∈ ℤ ve −5 < 2x + 1 ≤ 11}\nkümesi veriliyor.\nBuna göre A kümesinin eleman sayısı kaçtır?',
 dogru=8,yan=[(6,'Negatif tam sayıları kümeye almamış; yalnız 0, 1, …, 5 değerlerini (doğal sayıları) saymış.','dikkat'),(7,'2x + 1 ≤ 11 koşulunda eşitliği dışlayıp x = 5’i saymamış.','dikkat'),(9,'−5 < 2x + 1 koşulunda eşitliği de kabul edip x = −3’ü eklemiş.','dikkat'),(5,'Yalnız pozitif tam sayıları (1, 2, …, 5) kümeye almış; 0 ve negatifleri saymamış.','dikkat')],
 istenen='A kümesinin eleman sayısı.',
 ip=['Eşitsizliği x yalnız kalacak biçimde düzenle; sonra aralığa uyan tam sayıları tek tek yaz.'],
 bilgi=[GOS],
 ad=[A('x’i yalnız bırak','Her tarafa 1 çıkarıp 2’ye böl.','−6 < 2x ≤ 10 → −3 < x ≤ 5'),A('Tam sayıları yaz','−3 dahil değil, 5 dahil.','A = {−2, −1, 0, 1, 2, 3, 4, 5}'),A('Say','Elemanları say.','s(A) = 8')],
 puf='Eşitsizlikte < ucu aralığa dahil değildir, ≤ ucu dahildir; elemanları yazıp saymak en güvenli yoldur.')

# 02 s(AUB)
assert 17+12-7==22 and 17+12==29 and 17+12+7==36 and 17-7==10 and 12-7==5
mk(P,'0002',tipId='kmb-islem',tip='Küme işlemleri ve eleman sayısı',z='kolay',alt='Küme İşlemleri',kaz='Birleşimin eleman sayısını iki kümenin ve kesişimin eleman sayısından hesaplar.',kalip='düz',adim=2,
 kart='K-KMB-03 · s(A ∪ B) hesabı',
 metin='A ve B sonlu iki kümedir.\ns(A) = 17\ns(B) = 12\ns(A ∩ B) = 7\nolduğuna göre A ∪ B kümesinin eleman sayısı kaçtır?',
 dogru=22,yan=[(5,'B kümesinden yalnızca ortak elemanları çıkarıp B \\ A’nın eleman sayısını (12 − 7) vermiş.','dikkat'),(10,'A kümesinden ortak elemanları çıkarıp A \\ B’nin eleman sayısını (17 − 7) vermiş.','dikkat'),(29,'Ortak elemanları iki kez sayıp s(A) + s(B) toplamını vermiş.','bilgi'),(36,'Kesişimi çıkarmak yerine eklemiş: 17 + 12 + 7.','islem')],
 istenen='s(A ∪ B).',
 ip=['A ile B toplanırken ortak elemanlar kaç kez sayılır?'],
 bilgi=[FORM],
 ad=[A('Ortakları düzelt','Ortak elemanlar iki kümede de vardır, birleşimde bir kez sayılmalıdır.','s(A ∪ B) = s(A) + s(B) − s(A ∩ B)'),A('Toplamı yaz','Önce iki kümenin elemanlarını topla.','17 + 12 = 29'),A('Ortakları çıkar','Ortak elemanlar iki kez sayıldı, bir kez çıkar.','29 − 7 = 22')],
 puf='Birleşimde ortak elemanlar bir kez sayılır; toplamdan kesişimin eleman sayısı çıkarılır.')

# 03 kartezyen basit
A3=[x for x in range(2,20) if x>1 and all(x%d for d in range(2,x))]; B3=[x for x in range(-10,10) if -2<=x<3]
assert len(A3)==8 and len(B3)==5 and 8*5==40 and 8+5==13 and 8*4==32 and 7*5==35 and 8*3==24 and len([y for y in B3 if y>=0])==3
mk(P,'0003',tipId='kmb-kartezyen',tip='Kartezyen çarpım',z='kolay',alt='Kartezyen Çarpım',kaz='Koşulla verilen iki kümenin eleman sayılarından kartezyen çarpımın eleman sayısını bulur.',kalip='düz',adim=3,
 kart='K-KMB-05 · asal sayılar ve tam sayı aralığı',
 metin='A = {x : x asal sayı ve x < 20}\nB = {y : y ∈ ℤ ve −2 ≤ y < 3}\nkümeleri veriliyor.\nBuna göre A × B kümesinin eleman sayısı kaçtır?',
 dogru=40,yan=[(13,'Eleman sayılarını çarpmak yerine toplamış: 8 + 5.','bilgi'),(24,'B kümesinde negatif tam sayıları almayıp B’yi {0, 1, 2} sanmış: 8 · 3.','dikkat'),(32,'B kümesinden 0’ı saymayıp 4 eleman almış: 8 · 4.','dikkat'),(35,'2’yi çift olduğu için asal saymayıp A’yı 7 elemanlı almış: 7 · 5.','dikkat')],
 istenen='s(A × B).',
 ip=['Önce iki kümenin elemanlarını ayrı ayrı yazıp say.'],
 bilgi=[B('Asal sayı','1’den büyük olup yalnız 1’e ve kendisine bölünebilen doğal sayıdır. Örnek: 2, 3, 5, 7, 11 asal; 1 ve 9 asal değildir'),KART],
 ad=[A('A’yı yaz','20’den küçük asal sayılar.','A = {2, 3, 5, 7, 11, 13, 17, 19} → s(A) = 8'),A('B’yi yaz','−2 dahil, 3 dahil değil.','B = {−2, −1, 0, 1, 2} → s(B) = 5'),A('Çarp','s(A × B) = s(A) · s(B).','8 · 5 = 40')],
 puf='Kartezyen çarpımın eleman sayısı, kümelerin eleman sayılarının çarpımıdır.')

# 04 alt küme farkı
sol=[(n+3) for n in range(0,20) if 2**(n+3)-2**n==224]; assert sol==[8] or sol==[8.0]
assert 2**5==32 and 7*2**5==224 and 2**8==256 and 224//32==7 and 8-5==3
mk(P,'0004',tipId='kmb-altkume',tip='Alt küme sayısı',z='orta',alt='Alt Küme',kaz='Alt küme sayıları farkından eleman sayısını bulur.',kalip='düz',adim=3,
 kart='K-KMB-02 · alt küme sayıları farkı',
 metin='A ve B sonlu kümeleri için s(A) = s(B) + 3 tür.\nA kümesinin alt küme sayısı, B kümesinin alt küme sayısından 224 fazla olduğuna göre s(A) kaçtır?',
 dogru=8,yan=[(3,'Eleman sayıları arasındaki farkı (3) cevap sanmış.','dikkat'),(5,'s(B) değerini bulup s(A) yerine onu vermiş.','dikkat'),(7,'Parantezdeki farkı 8 − 1 = 7 bulup 7’yi s(A) sanmış.','islem'),(32,'B kümesinin alt küme sayısını (2⁵) bulup eleman sayısı sanmış.','bilgi')],
 istenen='s(A).',
 ip=['s(B) = n alıp iki alt küme sayısını n cinsinden yaz; farkı ortak çarpanla sadeleştir.'],
 bilgi=[ALT],
 ad=[A('Alt küme sayılarını yaz','s(B) = n olsun, s(A) = n + 3.','2ⁿ⁺³ − 2ⁿ = 224'),A('Ortak çarpan','2ⁿ parantezine al.','2ⁿ · (8 − 1) = 7 · 2ⁿ = 224 → 2ⁿ = 32 → n = 5'),A('s(A)','n + 3.','5 + 3 = 8')],
 puf='Alt küme sayıları farkında ortak 2ⁿ çarpanını dışarı al; üstler farkı çarpanı verir.')

# 05 tumleyen
assert 24+18-(40-6)==8 and 40-6==34 and 24+18==42 and 18-8==10 and 24-8==16
mk(P,'0005',tipId='kmb-islem',tip='Küme işlemleri ve eleman sayısı',z='orta',alt='Tümleyen',kaz='Tümleyen eleman sayısından birleşimi, buradan da kesişimin eleman sayısını bulur.',kalip='düz',adim=3,
 kart='K-KMB-03 · tümleyen ve kesişim',
 metin='E evrensel küme ve A, B kümeleri E’nin alt kümeleridir.\ns(E) = 40\ns(A) = 24\ns(B) = 18\ns((A ∪ B)′) = 6\nolduğuna göre s(A ∩ B) kaçtır?',
 dogru=8,yan=[(34,'Birleşimin eleman sayısını (40 − 6) bulup kesişim sanmış.','dikkat'),(42,'İki kümenin eleman sayılarını toplayıp (24 + 18) kesişimi çıkarmamış.','bilgi'),(10,'Kesişimi bulduktan sonra B \\ A’nın eleman sayısını (18 − 8) vermiş.','dikkat'),(16,'Kesişimi bulduktan sonra A \\ B’nin eleman sayısını (24 − 8) vermiş.','dikkat')],
 istenen='s(A ∩ B).',
 ip=['Evrensel kümede birleşimin dışında kalanlar tümleyen kümedir; önce birleşimin eleman sayısını bul.'],
 bilgi=[TUM,FORM],
 ad=[A('Birleşimi bul','s(A ∪ B) = s(E) − s((A ∪ B)′).','40 − 6 = 34'),A('Formülü kur','s(A ∪ B) = s(A) + s(B) − s(A ∩ B).','34 = 24 + 18 − s(A ∩ B)'),A('Kesişimi bul','Denklemi çöz.','s(A ∩ B) = 42 − 34 = 8')],
 puf='Önce tümleyen yardımıyla birleşimin eleman sayısını bul, sonra s(A ∪ B) formülünü kesişim için çöz.')

# 06 öncüllü
E=range(4); alt_=[frozenset(c) for r in range(5) for c in combinations(range(4),r)]; Ev=frozenset(E)
I_=II_=III_=True; II_all=True
for a in alt_:
    for b in alt_:
        if a<b:
            assert (a&(Ev-b))==frozenset(); assert (b-a)!=frozenset()
            if not ((Ev-a)<=(Ev-b)): II_all=False
assert II_all==False
mk(P,'0006',tipId='kmb-islem',tip='Küme işlemleri ve eleman sayısı',z='orta',alt='Alt Küme İlişkileri',kaz='Öz alt küme ilişkisinden tümleyen ve fark kümeleri hakkında kesin sonuçları belirler.',kalip='öncüllü',adim=3,
 kart='K-KMB-03 · A ⊂ B iken tümleyen ve fark',
 metin='E evrensel küme ve A, B kümeleri E’nin alt kümeleridir. A ⊂ B ve A ≠ B dir.\nBuna göre,\nI. A ∩ B′ = ∅\nII. A′ ⊂ B′\nIII. B \\ A ≠ ∅\nifadelerinden hangileri kesinlikle doğrudur?',
 dogru='I ve III',sira=['Yalnız I','Yalnız III','I ve II','I ve III','I, II ve III'],
 yan=[('Yalnız I','III’ü sınarken A ⊂ B olduğundan B \\ A kümesini boş sanmış; II’yi de yanlış bulmuş.','bilgi'),('Yalnız III','I’de A ∩ B′ kümesini A sanıp boş olmadığını düşünmüş; II’yi yanlış bulmuş.','bilgi'),('I ve II','II’de kapsama yönünün tümleyende ters döndüğünü görmeyip doğru saymış; III’ü A \\ B ile karıştırıp yanlış bulmuş.','bilgi'),('I, II ve III','II’yi kesin doğru saymış; kapsama yönünün tümleyende de aynı kaldığını sanmış.','bilgi')],
 istenen='Kesinlikle doğru olan ifadeler.',
 ip=['E = {1, 2, 3} alıp A = {1}, B = {1, 2} gibi küçük bir örnekle her ifadeyi dene.'],
 bilgi=[B('Alt küme ve tümleyen','A ⊂ B ise A′ ⊃ B′ olur: kapsama yönü ters döner. A ∩ B′ = A \\ B kümesidir. Örnek: E = {1, 2, 3}, A = {1}, B = {1, 2} için A′ = {2, 3}, B′ = {3}; B′ ⊂ A′')],
 ad=[A('I. ifade','A ∩ B′ = A \\ B; A ⊂ B olduğundan A’nın B dışında elemanı yoktur.','I doğru'),A('II. ifade','Örnek: A = {1}, B = {1, 2}, E = {1, 2, 3} için A′ = {2, 3}, B′ = {3}; A′ ⊄ B′ (doğrusu B′ ⊂ A′).','II yanlış'),A('III. ifade','A ≠ B ve A ⊂ B olduğundan B’de A’da olmayan bir eleman vardır.','III doğru'),A('Sonuç','Kesinlikle doğru olanlar I ve III.','I ve III')],
 puf='Kapsama ilişkilerini küçük bir örnekle dene; tümleyen alınınca kapsama yönünün tersine döndüğünü hatırla.')

# 07 venn2 hayvan
T,c,k,h=120,74,58,12; u=T-h; ik=c+k-u; assert (u,ik)==(108,24) and c-ik==50 and k-ik==34 and 50+34==84 and 84+h==96 and c+k==132
mk(P,'0007',tipId='kmb-venn',tip='İki ve üç kümeli problemler',z='orta',alt='Venn Problemleri',kaz='Hiçbirini içermeyenler bilinen iki kümeli bir problemde yalnız bir kümeye ait elemanların sayısını bulur.',kalip='hikâyeli',adim=4,
 kart='K-KMB-04 · sitede kedi ve köpek besleyen aileler',
 metin='Bir sitede oturan 120 ailenin 74’ü kedi, 58’i köpek beslemektedir. Ne kedi ne de köpek besleyen 12 aile vardır.\nBuna göre yalnızca bir tür hayvan (kedi ya da köpek) besleyen kaç aile vardır?',
 dogru=84,yan=[(24,'Hem kedi hem köpek besleyen aile sayısında bırakmış.','dikkat'),(96,'Yalnız bir tür besleyenlere ne kedi ne köpek besleyen 12 aileyi de eklemiş.','dikkat'),(108,'En az bir hayvan besleyen aile sayısını (120 − 12) vermiş.','dikkat'),(132,'Kedi ve köpek besleyenleri toplayıp (74 + 58) ortak aileleri iki kez saymış.','bilgi')],
 istenen='Yalnızca bir tür hayvan besleyen aile sayısı.',
 ip=['Hiçbirini beslemeyenleri 120’den çıkarıp en az birini besleyenleri bul; sonra ortak aile sayısına ulaş.'],
 bilgi=[VENN],
 ad=[A('En az birini besleyenler','120 − 12.','108 aile'),A('Her ikisini besleyenler','74 + 58 − x = 108.','x = 132 − 108 = 24'),A('Yalnız kedi, yalnız köpek','Toplamlardan ortakları çıkar.','74 − 24 = 50 · 58 − 24 = 34'),A('Toplam','Yalnız bir tür besleyenler.','50 + 34 = 84')],
 puf='Önce hiçbirinde olmayanları çıkar, sonra kesişimi bul; yalnız bölgeler toplamdan kesişim çıkarılarak elde edilir.')

# 08 venn2 spor
T,h,b=36,6,3; u=T-h
sol=[(f,v) for v in range(0,40) for f in [2*v] if f+v-b==u]; assert sol==[(22,11)]
f,v=22,11; assert f-b==19 and v-b==8 and (u//3*2)==20 and u//3==10
mk(P,'0008',tipId='kmb-venn',tip='İki ve üç kümeli problemler',z='orta',alt='Venn Problemleri',kaz='Katı ilişkisi ve kesişim bilgisiyle bir kümenin eleman sayısını bulur.',kalip='hikâyeli',adim=4,
 kart='K-KMB-04 · sınıfta futbol ve voleybol oynayanlar',
 metin='36 öğrencilik bir sınıfta futbol oynayan öğrencilerin sayısı voleybol oynayan öğrencilerin sayısının 2 katıdır. Her ikisini de oynayan 3 öğrenci vardır, bu iki spordan hiçbirini oynamayan 6 öğrenci vardır.\nBuna göre futbol oynayan kaç öğrenci vardır?',
 dogru=22,yan=[(8,'Yalnızca voleybol oynayanların sayısını (11 − 3) bulmuş.','dikkat'),(11,'Voleybol oynayanların sayısını bulup futbol oynayanların sayısı sanmış.','dikkat'),(19,'Yalnızca futbol oynayanların sayısını (22 − 3) vermiş.','dikkat'),(20,'Ortak oynayanları hesaba katmayıp f + v = 30 alarak v = 10, f = 20 bulmuş.','bilgi')],
 istenen='Futbol oynayan öğrenci sayısı.',
 ip=['Voleybol oynayanlara v de; en az birini oynayanlar için kesişimi de içeren bir denklem yaz.'],
 bilgi=[VENN],
 ad=[A('En az birini oynayanlar','36 − 6.','30 öğrenci'),A('Denklemi kur','Voleybol v, futbol 2v.','2v + v − 3 = 30 → v = 11'),A('Futbol oynayanlar','2v.','2 · 11 = 22'),A('Kontrol','Yalnız futbol 19, yalnız voleybol 8, ikisi 3, hiçbiri 6.','19 + 8 + 3 + 6 = 36 ✓')],
 puf='Katı ilişkisi verilen toplamlara v gibi tek bir bilinmeyen koyup s(A ∪ B) formülünde yerine yaz.')

# 09 üç kümeli
yf,yt,ym,ft,tm,fm_,hic=8,6,9,5,4,3,5; x=45-(yf+yt+ym+ft+tm+fm_+hic); assert x==5
tiy=yt+ft+tm+x; assert tiy==20 and yt+ft+tm==15 and tiy+hic==25 and yt+(ft+x)+(tm+x)+x==30
mk(P,'0009',tipId='kmb-venn',tip='İki ve üç kümeli problemler',z='orta',alt='Üç Kümeli Sayma',kaz='Bölgeleri verilen üç kümeli problemde bilinmeyen bölgeyi toplamdan bulup bir kümenin eleman sayısını hesaplar.',kalip='hikâyeli',adim=4,
 kart='K-KMB-04 · fotoğraf, tiyatro ve müzik kulüpleri',
 metin='Bir okuldaki 45 öğrencinin her biri fotoğraf, tiyatro ve müzik kulüplerinden en fazla üçüne üye olabilmektedir. Hiçbir kulübe üye olmayan 5 öğrenci vardır.\nYalnızca fotoğraf kulübüne 8, yalnızca tiyatro kulübüne 6, yalnızca müzik kulübüne 9 öğrenci üyedir. Tam olarak iki kulübe üye olan öğrencilerden fotoğraf ile tiyatroya 5, tiyatro ile müziğe 4, fotoğraf ile müziğe 3 öğrenci üyedir.\nBuna göre tiyatro kulübüne üye olan öğrenci sayısı kaçtır?',
 dogru=20,yan=[(6,'Yalnızca tiyatro kulübüne üye olanları vermiş.','dikkat'),(15,'Üç kulübe birden üye olanları tiyatro kulübünden saymamış.','dikkat'),(25,'Hiçbir kulübe üye olmayan 5 öğrenciyi de tiyatro kulübüne eklemiş.','dikkat'),(30,'Üçüne de üye olanları iki ikili bölgeye ve ayrıca ayrı bölgeye ekleyip üç kez saymış.','bilgi')],
 istenen='Tiyatro kulübüne üye öğrenci sayısı.',
 ip=['Toplam 45 öğrenciyi bölgelere ayır; verilmeyen tek bölgenin sayısını bul.'],
 bilgi=[VENN3],
 ad=[A('Üçüne de üye olanlar','Toplam, verilen bölgeler ve x’in toplamıdır.','8 + 6 + 9 + 5 + 4 + 3 + 5 + x = 45 → x = 5'),A('Tiyatro bölgeleri','Tiyatroyu içeren dört bölge: yalnız tiyatro, fotoğrafla, müzikle ve üçü birden.','6 + 5 + 4 + 5'),A('Topla','Dört bölgenin toplamı.','20')],
 puf='Verilmeyen bölgeyi toplam üzerinden bul; bir kümenin eleman sayısı, onu içeren dört bölgenin toplamıdır.')

# 10 kartezyen a<b
A10=[1,2,3,4,5,6]; B10=[2,4,6,8]; pr=[(a,b) for a in A10 for b in B10]
lt=sum(a<b for a,b in pr); le=sum(a<=b for a,b in pr); gt=sum(a>b for a,b in pr); ne=sum(a!=b for a,b in pr)
assert (lt,le,gt,ne,len(pr))==(15,18,6,21,24)
mk(P,'0010',tipId='kmb-kartezyen',tip='Kartezyen çarpım',z='orta',alt='Kartezyen Çarpım',kaz='Kartezyen çarpımdaki sıralı ikilileri bir bileşen koşuluna göre sayar.',kalip='düz',adim=3,
 kart='K-KMB-05 · birinci bileşeni ikinci bileşeninden küçük ikililer',
 metin='A = {1, 2, 3, 4, 5, 6}\nB = {2, 4, 6, 8}\nkümeleri veriliyor.\nA × B kümesinin birinci bileşeni ikinci bileşeninden küçük olan kaç elemanı vardır?',
 dogru=15,yan=[(6,'Koşulu ters okuyup birinci bileşeni ikincisinden büyük olanları saymış.','dikkat'),(18,'Birinci bileşeni ikincisine eşit olanları da (2, 4 ve 6) saymış.','dikkat'),(21,'İki bileşeni birbirinden farklı olan ikilileri saymış.','dikkat'),(24,'Koşulu uygulamayıp tüm ikilileri saymış.','dikkat')],
 istenen='Koşulu sağlayan sıralı ikili sayısı.',
 ip=['İkinci bileşeni 2, 4, 6, 8 için ayrı ayrı düşün; her birinde birinci bileşen olabilecek elemanları say.'],
 bilgi=[KART],
 ad=[A('İkinci bileşen 2','Birinci bileşen 2’den küçük.','1 → 1 ikili'),A('İkinci bileşen 4, 6, 8','Birinci bileşen sırasıyla 4, 6, 8’den küçük (A’da 6’ya kadar).','3 + 5 + 6 ikili'),A('Topla','Tüm ikililer.','1 + 3 + 5 + 6 = 15')],
 puf='Koşullu ikilileri saymak için bir bileşeni sabitleyip diğerinin koşulu sağlayan elemanlarını say.')

# 11 alt küme koşullu
A11=range(1,8); cnt=0
for r in range(8):
    for c_ in combinations(A11,r):
        s=set(c_)
        if (1 not in s or 2 in s) and 7 not in s: cnt+=1
assert cnt==48 and 3*2**5==96 and 4*2**4==64 and 2**7==128 and 2**4==16
mk(P,'0011',tipId='kmb-altkume',tip='Alt küme sayısı',z='zor',alt='Koşullu Alt Küme',kaz='Birbirine bağlı iki koşul ve bir dışlama koşuluyla alt küme sayısını bulur.',kalip='düz',adim=4,
 kart='K-KMB-02 · 1 varsa 2 de var, 7 yok',
 metin='Boş küme de sayılmak üzere, A = {1, 2, 3, 4, 5, 6, 7} kümesinin alt kümelerinden, 1 elemanını içeren her alt kümede 2 elemanı da bulunan ve 7 elemanını hiç içermeyen kaç tanesi vardır?',
 dogru=48,yan=[(16,'1 ve 2’yi yalnız birlikte bulunan durumla sınırlayıp 2⁴ saymış.','dikkat'),(64,'1 ve 2’yi bağımsız sayıp 7’yi dışlamış: 4 · 2⁴.','bilgi'),(96,'7’nin bulunmama koşulunu uygulamayıp 3 · 2⁵ saymış.','dikkat'),(128,'Koşulları hiç uygulamayıp tüm alt kümeleri (2⁷) saymış.','dikkat')],
 istenen='Koşulları sağlayan alt küme sayısı.',
 ip=['1 ve 2 için hangi durumlar mümkün? Sonra 3, 4, 5, 6 elemanlarının serbest olduğunu kullan.'],
 bilgi=[ALT],
 ad=[A('1 ve 2’nin durumları','(1 yok, 2 yok), (1 yok, 2 var), (1 var, 2 var) olabilir; (1 var, 2 yok) olamaz.','3 durum'),A('7 elemanı','Alt kümede bulunamaz.','1 durum'),A('Serbest elemanlar','3, 4, 5, 6 elemanları her iki durumda da olabilir.','2⁴ = 16'),A('Çarp','Durumları çarp.','3 · 16 = 48')],
 puf='Birbirine bağlı koşullarda mümkün durumları tek tek yaz; serbest elemanları 2 üzeri adetle çarp.')

# 12 üç kümeli membership
sols=[]
for c3 in range(0,20):
    for a1 in range(0,50):
        if a1+14+c3==46 and a1+2*14+3*c3==74: sols.append((a1,c3))
assert sols==[(25,7)] and 74-46==28 and 28-14==14 and 46-14==32
mk(P,'0012',tipId='kmb-venn',tip='İki ve üç kümeli problemler',z='zor',alt='Üç Kümeli Sayma',kaz='Her kümenin eleman sayıları toplamını bölge ağırlıklarıyla ilişkilendirerek üç kümeli bir problemde üçlü kesişimi bulur.',kalip='hikâyeli',adim=4,
 kart='K-KMB-04 · dil kursunda üç dil',
 metin='Bir dil kursundaki 50 öğrenciden 4’ü hiçbir dil bilmemektedir. Öğrencilerden 30’u İngilizce, 24’ü Almanca, 20’si Fransızca bilmektedir. Tam olarak iki dil bilen 14 öğrenci vardır.\nBuna göre üç dili de bilen kaç öğrenci vardır?',
 dogru=7,yan=[(14,'Dil sayıları toplamı ile en az bir dil bilenlerin sayısı farkından (74 − 46 = 28) tam iki dil bilenleri çıkarıp (28 − 14) sonucu üçlü kesişim sanmış; üçlü kesişimin farka 2 kat girdiğini görmemiş.','bilgi'),(25,'Yalnızca bir dil bilenlerin sayısını (46 − 14 − 7) bulup üç dil bilenler sanmış.','dikkat'),(28,'Dil sayıları toplamı ile en az bir dil bilen sayısı farkını (74 − 46) üç dil bilenler sanmış.','bilgi'),(32,'En az bir dil bilenlerden tam iki dil bilenleri çıkarıp (46 − 14) yalnızca bir ya da üç dil bilenleri üç dil bilenler sanmış.','dikkat')],
 istenen='Üç dili de bilen öğrenci sayısı.',
 ip=['Dil sayılarının toplamını, öğrencilerin kaç dil bildiğine göre (1, 2 ve 3 dil) iki farklı biçimde yaz.'],
 bilgi=[VENN3,B('Üyelik toplamı','Kümelerin eleman sayıları toplanınca yalnız bir kümede olan 1, iki kümede olan 2, üç kümede olan 3 kez sayılır. Örnek: 5 kişi yalnız A’da, 2 kişi A ile B’de ise s(A) + s(B) toplamına bunlar 5 · 1 + 2 · 2 kadar girer')],
 ad=[A('En az bir dil bilenler','50 − 4.','46 = a + 14 + c (a: yalnız bir dil, c: üç dil)'),A('Dil sayıları toplamı','Her öğrenci bildiği dil sayısı kadar sayılır.','30 + 24 + 20 = 74 = a + 2 · 14 + 3c'),A('İki denklemi çöz','İkinciden birinciyi çıkar.','74 − 46 = 14 + 2c → c = 7')],
 puf='Kümelerin eleman sayıları toplamı; yalnız bir, tam iki ve üç kümeli öğrencileri 1, 2 ve 3 ağırlığıyla sayar.')

# 13 yeni nesil
sa,sd,su=10,11,15; ik=su-sd; sb=su+ik-sa
assert ik==4 and sb==9 and su-sa==5 and sd-sa==1 and su+ik==19
for A_ in [set(range(10))]:
    B_=set(range(6,15)); assert len(A_)==10 and len(B_)==9 and len(A_^B_)==11 and len(A_|B_)==15
mk(P,'0013',tipId='kmb-yeninesil',tip='Yeni nesil: tanımlı küme işlemi',z='orta',alt='Tanımlı İşlem',kaz='Tanımlı simetrik fark işleminin eleman sayısını birleşim ve kesişimle ilişkilendirerek bilinmeyen eleman sayısını bulur.',kalip='yeni nesil',adim=3,
 kart='K-KMB-06 · simetrik fark tanımı',
 metin='İki kümenin yalnız birinde bulunan elemanlardan oluşan küme için\nA ⊕ B = (A \\ B) ∪ (B \\ A)\nişlemi tanımlanıyor.\nA ve B sonlu kümeleri için s(A) = 10, s(A ⊕ B) = 11 ve s(A ∪ B) = 15 olduğuna göre s(B) kaçtır?',
 dogru=9,yan=[(1,'s(A ⊕ B) − s(A) farkını (11 − 10) B’nin eleman sayısı sanmış.','dikkat'),(4,'Kesişimin eleman sayısını bulup durmuş.','dikkat'),(5,'Birleşimden A’yı çıkarıp (15 − 10) yalnızca B’de olanları s(B) sanmış; ortak elemanları katmamış.','bilgi'),(19,'Birleşim ile kesişimi toplayıp (15 + 4) A’yı çıkarmayı unutmuş.','islem')],
 istenen='s(B).',
 ip=['Birleşim, yalnız bir kümede olanlar ile ortak elemanlardan oluşur; buradan ortak eleman sayısını bul.'],
 bilgi=[YEN,FORM],
 ad=[A('Kesişimi bul','A ⊕ B yalnız bir kümede olanlardır; birleşimden çıkınca ortaklar kalır.','s(A ∩ B) = 15 − 11 = 4'),A('B’ye ulaş','s(A ∪ B) = s(A) + s(B) − s(A ∩ B).','15 = 10 + s(B) − 4'),A('Çöz','s(B) yalnız bırakılır.','s(B) = 15 − 10 + 4 = 9')],
 puf='Tanımı bilinen bölgelere çevir: ⊕ yalnız bir kümede olanları, birleşim bunlara ortakları ekler.')

# 14 kartezyen kesişim
cs=[(a,b) for b in range(1,43) for a in range(b+1,43) if a*b==42]; assert sorted(cs)==[(7,6),(14,3),(21,2),(42,1)]
c=4; ok_=[(a,b) for a,b in cs if b>=c]; assert ok_==[(7,6)] and 7+6-4==9 and 7+6==13 and 13+4==17 and 7+6-2*4==5 and 7-4==3
mk(P,'0014',tipId='kmb-kartezyen',tip='Kartezyen çarpım',z='zor',alt='Kartezyen Çarpım',kaz='İki kartezyen çarpımın kesişimini kümelerin kesişimiyle ilişkilendirip birleşimin eleman sayısını bulur.',kalip='düz',adim=4,
 kart='K-KMB-05 · (A × B) ∩ (B × A)',
 metin='A ve B sonlu kümeleri için s(A × B) = 42 ve s(A) > s(B) dir.\n(A × B) ∩ (B × A) kümesinin 16 elemanı olduğuna göre A ∪ B kümesinin eleman sayısı kaçtır?',
 dogru=9,yan=[(3,'A \\ B kümesinin eleman sayısını (7 − 4) vermiş.','dikkat'),(5,'Birleşim yerine yalnız bir kümede olan elemanların sayısını (13 − 8) bulmuş.','bilgi'),(13,'Kesişimi çıkarmayıp s(A) + s(B) toplamını vermiş.','bilgi'),(17,'Kesişimi çıkarmak yerine eklemiş: 13 + 4.','islem')],
 istenen='s(A ∪ B).',
 ip=['(A × B) ∩ (B × A) kümesinin elemanları hem A × B hem B × A’da bulunur; bileşenlerinin hangi kümelerde olması gerektiğini düşün.'],
 bilgi=[KART,FORM],
 ad=[A('Kesişimi bul','(A × B) ∩ (B × A) = (A ∩ B) × (A ∩ B).','s(A ∩ B)² = 16 → s(A ∩ B) = 4'),A('s(A) ve s(B)','s(A) · s(B) = 42, s(A) > s(B) ve s(B) ≥ 4 olmalı.','s(A) = 7, s(B) = 6'),A('Birleşimi bul','s(A ∪ B) = s(A) + s(B) − s(A ∩ B).','7 + 6 − 4 = 9')],
 puf='(A × B) ∩ (B × A), A ∩ B kümesinin kendisiyle kartezyen çarpımıdır; eleman sayısı s(A ∩ B)² olur.')

bitir(P,'kumeiki',UK)
