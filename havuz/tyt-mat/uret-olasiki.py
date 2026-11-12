"""Olasılık · parti 2 (hafif mod): 14 ana soru, kardeş yok, ipucu 1. Her cevap örnek uzay taranarak Fraction ile doğrulanır."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_mat as H
from _hafif_mat import *
from itertools import product,permutations,combinations
from math import comb
H.KONU='Olasılık'
UK='matd|Olasılık'
P=Parti('olasiki','Olasılık',UK)
def fs(x):
    x=Fr(x); return str(x.numerator) if x.denominator==1 else f'{x.numerator}/{x.denominator}'
def M(no,dogru,yan,**k):
    k['adim']=len(k['ad'])
    vals=[Fr(dogru)]+[Fr(y[0]) for y in yan]; assert len(set(vals))==5 and all(0<v<1 for v in vals)
    sira=[fs(v) for v in sorted(vals)]
    mk(P,no,dogru=fs(dogru),yan=[(fs(y[0]),y[1],y[2]) for y in yan],sira=sira,**k)

OL=B('Olasılık','Her sonucun eşit şansla gerçekleştiği deneylerde olasılık = istenen sonuç sayısı / tüm sonuç sayısıdır. Örnek: hilesiz bir zarda çift gelme olasılığı 3/6 = 1/2')
TUM=B('Tümleyen olay','Bir olayın olmama olasılığı 1 eksi olma olasılığıdır; “en az bir” olayının tümleyeni “hiç olmaması”dır. Örnek: hilesiz 3 paranın en az birinin yazı gelme olasılığı 1 − (1/2)³ = 7/8')
BAG=B('Bağımsız olaylar','Birbirini etkilemeyen olayların ikisinin birden olma olasılığı olasılıkların çarpımıdır. Örnek: olasılıkları 1/2 ve 1/3 olan iki bağımsız olayın ikisinin birden olma olasılığı 1/6’dır')
IADE=B('Geri konarak ve geri konmadan çekiliş','Çekilen nesne geri konursa her çekilişte seçenekler aynı kalır; geri konmazsa torbadaki sayı azalır. Örnek: 3 kırmızı, 2 mavi bilyeden art arda iki çekilişte ikisinin kırmızı olması geri konarak (3/5)² = 9/25, geri konmadan 3/5 × 2/4 = 3/10’dur')
KOMB=B('Kombinasyonla olasılık','Sırasız ya da aynı anda yapılan seçimlerde durum sayıları C(n, r) ile bulunur. Örnek: 5 bilyeden 2’sinin seçilmesi C(5, 2) = 10 biçimdedir')
GEO=B('Geometrik olasılık','Rastgele bir noktanın bir bölgede olma olasılığı, o bölgenin ölçüsünün (alan ya da merkez açı) tüm bölgenin ölçüsüne oranıdır. Örnek: merkez açısı 90° olan dilimin olasılığı 90/360 = 1/4’tür')
ASAL=B('Asal sayı','1’den büyük olup yalnızca 1’e ve kendisine bölünebilen doğal sayılara asal sayı denir. Örnek: 2, 3, 5, 7, 11 asaldır; 1 ve 9 asal değildir')
TOPL=B('Olayları toplama','Aynı anda gerçekleşemeyen iki olayın “ya da” ile birleşiminin olasılığı olasılıkların toplamıdır. Örnek: zarda 1 gelmesi ile 6 gelmesi birlikte olamaz; biri gelme olasılığı 1/6 + 1/6 = 1/3’tür')

KY='ÖSYM 2018–2026 TYT Matematik (olasılık) · yayın soru bankaları (yalnız mantık) · MEB 10. sınıf Basit Olayların Olasılığı'
kart('K-OLB-01','Örnek uzay ve olay (zar, para, kart)','Örnek uzay sayılır, istenen olayın sonuçları ayrıca sayılıp oranlanır; sonuçlar ayırt edilebiliyorsa sıralı çiftler alınır.','Sonuçları eşit olasılıklı sanmak (ör. toplamlar); sırasız çiftleri saymak; sınırı dahil etmek.','kolay','hikâyeli',3,'olb-temel','Örnek uzay ve olay',KY)
kart('K-OLB-02','Geri konarak ve geri konmadan çekiliş','Art arda çekilişte her aşamanın olasılığı çarpılır; geri konmadan çekimde torbadaki sayı azalır, sıralar birlikte düşünülür.','Geri konmadan çekimde paydayı değiştirmemek; sıraları atlayıp tek dizilişi saymak.','orta','hikâyeli',3,'olb-ardisik','Art arda çekiliş',KY)
kart('K-OLB-03','Bağımsız olaylar ve “en az bir”','Bağımsız olayların olasılıkları çarpılır; “yalnızca biri” iki ayrı durumun toplamıdır; “en az bir” tümleyenle bulunur.','“Yalnızca biri” ile “en az biri”ni karıştırmak; tümleyeni cevap sanmak.','orta','hikâyeli',3,'olb-bagimsiz','Bağımsız olaylar ve en az bir',KY)
kart('K-OLB-04','Kombinasyonla olasılık','Aynı anda yapılan seçimlerde pay ve payda kombinasyonla sayılır; “en az bir” için tümleyen kullanılır.','Payı sıralı, paydayı sırasız saymak (ya da tersi); tümleyeni cevap sanmak.','orta','hikâyeli',4,'olb-sayma','Kombinasyonla olasılık',KY)
kart('K-OLB-05','Geometrik olasılık (çark ve hedef)','Olasılık, istenen bölgenin alanının ya da merkez açısının tüm bölgeye oranıdır.','Dilim ya da halka sayısıyla oranlamak; yarıçap oranını alan oranı sanmak.','orta','düz',3,'olb-geometrik','Geometrik olasılık',KY)
kart('K-OLB-06','Yeni nesil, hikâyeli ve öncüllü olasılık','Kural ya da öncüllerle verilen kurgularda her durum ayrı ayrı sayılır ya da hesaplanır, sonra birleştirilir.','Kuralın bir durumunu atlamak; öncülleri hesaplamadan karar vermek; sıralı ve sırasız sayımı karıştırmak.','zor','yeni nesil',4,'olb-yeninesil','Yeni nesil ve öncüllü olasılık',KY)

# ---------- 01 kolay · iki zar toplamı ----------
O=list(product(range(1,7),repeat=2)); assert len(O)==36
ge9=[o for o in O if sum(o)>=9]; assert len(ge9)==10 and Fr(len(ge9),36)==Fr(5,18)
un=[o for o in O if o[0]<=o[1]]; assert len(un)==21 and len([o for o in un if sum(o)>=9])==6 and Fr(6,21)==Fr(2,7)
assert Fr(4,11)==Fr(len([s for s in range(2,13) if s>=9]),11) and Fr(len([o for o in O if sum(o)>=8]),36)==Fr(5,12) and Fr(len([o for o in O if sum(o)<9]),36)==Fr(13,18)
M('0001',Fr(5,18),[(Fr(2,7),'Zarları ayırt edilmez sayıp 21 sonuçtan 6’sını (6/21) almış; (3, 6) ile (6, 3) gibi sonuçlar ayrı sonuçlardır.','bilgi'),(Fr(4,11),'2’den 12’ye kadar 11 toplamı eşit olasılıklı sanmış; 9, 10, 11 ve 12 olmak üzere 4/11 bulmuş.','bilgi'),(Fr(5,12),'“9 ya da daha büyük” yerine “8 ya da daha büyük” sonuçları (15/36) saymış.','dikkat'),(Fr(13,18),'Toplamın 9’dan küçük olma olasılığını (26/36) bulup istenen olayın tümleyenini yazmış.','dikkat')],
 tipId='olb-temel',tip='Örnek uzay ve olay',z='kolay',alt='Basit Olay',kaz='İki zar atılışında örnek uzayı sayıp toplam koşulunu sağlayan sonuçların olasılığını bulur.',kalip='düz',
 kart='K-OLB-01 (örnek uzay, iki zar) · toplam 9 ya da daha büyük',
 metin='Biri kırmızı, diğeri mavi olan iki hilesiz zar aynı anda atılıyor.\nÜst yüzlerde görülen sayıların toplamının 9 ya da daha büyük olma olasılığı kaçtır?',
 istenen='Toplamın en az 9 olma olasılığı.',
 ip=['Zarlar ayırt edilebildiğine göre örnek uzayda kaç sonuç vardır? Toplamı koşula uyanları gruplayarak say.'],
 bilgi=[OL],
 ad=[A('Örnek uzay','Her zar 6 sonuç verir ve zarlar ayırt edilebilir.','6 × 6 = 36 sonuç'),A('İstenen sonuçlar','Toplam 9: 4, toplam 10: 3, toplam 11: 2, toplam 12: 1 sonuç.','4 + 3 + 2 + 1 = 10 sonuç'),A('Olasılık','İstenen sonuç sayısını örnek uzaya böl.','10/36 = 5/18')],
 puf='İki zarın sonuçları sıralı ikililerdir; 36 sonuç eşit olasılıklıdır, toplamlar eşit olasılıklı değildir.')

# ---------- 02 kolay · para ----------
Y=list(product('TY',repeat=4)); t2=[y for y in Y if y.count('T')==2]
assert len(Y)==16 and len(t2)==6 and Fr(len(t2),16)==Fr(3,8) and Fr(1,16)==Fr(1,16) and Fr(2,16)==Fr(1,8) and Fr(1,2)**2==Fr(1,4)
M('0002',Fr(3,8),[(Fr(1,16),'Yalnızca TTYY dizilişini saymış: 1/16.','dikkat'),(Fr(1,8),'Yalnızca TTYY ve YYTT dizilişlerini saymış: 2/16.','dikkat'),(Fr(1,4),'Yalnızca iki turanın geldiğini (1/2)² olarak hesaplayıp yazıları ve turaların yerini katmamış.','bilgi'),(Fr(1,2),'Dört atışın yarısında tura geleceğini düşünüp 1/2 almış.','bilgi')],
 tipId='olb-temel',tip='Örnek uzay ve olay',z='kolay',alt='Basit Olay',kaz='Art arda atılan paranın örnek uzayını sayıp tam iki kez tura gelme olasılığını bulur.',kalip='düz',
 kart='K-OLB-01 (örnek uzay, para) · 4 atışta tam 2 tura',
 metin='Hilesiz bir madeni para art arda 4 kez atılıyor.\nBu atışların tam 2 tanesinde tura gelme olasılığı kaçtır?',
 istenen='4 atışta tam iki tura gelme olasılığı.',
 ip=['Her atışta iki sonuç olduğuna göre 4 atışın örnek uzayı kaç sonuçludur? İki turanın yeri kaç farklı biçimde seçilebilir?'],
 bilgi=[OL],
 ad=[A('Örnek uzay','Her atış 2 sonuçlu; 4 atış art arda.','2 × 2 × 2 × 2 = 16 sonuç'),A('İstenen sonuçlar','4 atıştan 2’sinin yeri tura için seçilir.','C(4, 2) = 6 sonuç'),A('Olasılık','İstenen sonuç sayısını örnek uzaya böl.','6/16 = 3/8')],
 puf='Art arda atışlarda örnek uzay 2ⁿ sonuçludur; turaların yerini seçmek kombinasyonla sayılır.')

# ---------- 03 kolay · asal kart ----------
def asal(n): return n>1 and all(n%d for d in range(2,int(n**.5)+1))
K=range(1,31); a=[n for n in K if asal(n)]; assert len(a)==10 and Fr(10,30)==Fr(1,3)
assert Fr(11,30)==Fr(len(a)+1,30) and Fr(len([n for n in K if n%2==1]),30)==Fr(1,2) and Fr(len([n for n in K if not asal(n)]),30)==Fr(2,3) and Fr(len([n for n in K if n>1 and not asal(n)]),30)==Fr(19,30)
M('0003',Fr(1,3),[(Fr(11,30),'1’i de asal sayı sayıp 11 kart bulmuş.','bilgi'),(Fr(1,2),'Tek sayıları asal sanıp 15 kart saymış.','bilgi'),(Fr(19,30),'Bileşik (asal olmayan, 1’den büyük) sayıların olasılığını bulmuş: 19/30.','dikkat'),(Fr(2,3),'Asal olmayan sayıların olasılığını (20/30) bulup tümleyeni yazmış.','dikkat')],
 tipId='olb-temel',tip='Örnek uzay ve olay',z='kolay',alt='Basit Olay',kaz='Numaralı kartlardan asal numaralı olanları sayıp basit olayın olasılığını bulur.',kalip='düz',
 kart='K-OLB-01 (numaralı kart) · asal numara',
 metin='Bir torbada 1’den 30’a kadar numaralanmış, birbirinin aynı görünen 30 kart vardır. Torbadan rastgele bir kart çekiliyor.\nÇekilen kartın numarasının asal sayı olma olasılığı kaçtır?',
 istenen='Kart numarasının asal olma olasılığı.',
 ip=['1’den 30’a kadar hangi sayıların asal olduğunu tek tek belirle.'],
 bilgi=[ASAL,OL],
 ad=[A('Asalları yaz','1’den 30’a kadar asal sayılar.','2, 3, 5, 7, 11, 13, 17, 19, 23, 29 → 10 sayı'),A('Örnek uzay','Torbada 30 kart var.','30 sonuç'),A('Olasılık','Asal sayıların adedini kart sayısına böl.','10/30 = 1/3')],
 puf='Asal sayılar listesini küçük sayılardan başlayıp 1’i dışarıda bırakarak yaz.')

# ---------- 04 orta · art arda, geri konmadan, üç farklı renk ----------
B_=['b']*4+['y']*3+['m']*2
dz=list(permutations(range(9),3)); col=lambda i:B_[i]
good=[d for d in dz if len({col(i) for i in d})==3]; assert Fr(len(good),len(dz))==Fr(2,7)
assert Fr(4*3*2,9*8*7)==Fr(1,21) and Fr(4+3+2,comb(9,3))==Fr(3,28) and Fr(6,27)==Fr(2,9)
assert Fr(6*4*3*2,9**3)==Fr(16,81)
M('0004',Fr(2,7),[(Fr(1,21),'Yalnızca beyaz–yeşil–mor sırasını hesaplamış; 3! = 6 farklı sırayı atlamış: 4/9 × 3/8 × 2/7.','dikkat'),(Fr(3,28),'Pay yerine renk sayılarını toplamış: (4 + 3 + 2)/C(9, 3).','islem'),(Fr(16,81),'Bilyeleri geri koyarak çektiğini düşünüp paydayı 9 almış: 6 × (4 × 3 × 2)/9³.','bilgi'),(Fr(2,9),'Her çekilişte üç rengi eşit olasılıklı sanıp 3!/3³ hesaplamış.','bilgi')],
 tipId='olb-ardisik',tip='Art arda çekiliş',z='orta',alt='Art Arda Çekiliş',kaz='Geri konmadan art arda çekilişte üç farklı renk gelme olasılığını sıraları da hesaba katarak bulur.',kalip='hikâyeli',
 kart='K-OLB-02 (geri konmadan çekiliş) · üç farklı renk',
 metin='Bir torbada 4 beyaz, 3 yeşil ve 2 mor bilye vardır. Torbadan art arda, geri konmadan 3 bilye çekiliyor.\nÇekilen üç bilyenin üçünün de farklı renkte olma olasılığı kaçtır?',
 istenen='Üç bilyenin de farklı renkte olma olasılığı.',
 ip=['Üç farklı rengin çekilişlere hangi sıralarla dağılabileceğini ve her sırada olasılığın ne olduğunu düşün.'],
 bilgi=[IADE,OL],
 ad=[A('Bir sıranın olasılığı','Beyaz, yeşil, mor sırasıyla; her çekilişte torbadaki sayı azalır.','4/9 × 3/8 × 2/7 = 24/504 = 1/21'),A('Sıra sayısı','Üç rengin 3 çekilişe dağılma biçimi; her sıranın olasılığı aynıdır.','3! = 6'),A('Toplam','Sıralar birbirinden ayrı olaylardır, olasılıkları toplanır.','6 × 1/21 = 6/21 = 2/7')],
 puf='Geri konmadan çekimde her aşamada payda bir azalır; renklerin farklı sıraları ayrı ayrı sayılıp toplanır.')

# ---------- 05 zor · üç bağımsız olay, en az ikisi ----------
pr=[Fr(4,5),Fr(3,4),Fr(2,3)]
def ol(dz):
    t=Fr(1)
    for p_,d in zip(pr,dz): t*=p_ if d else 1-p_
    return t
bs=list(product([0,1],repeat=3))
az2=sum(ol(d) for d in bs if sum(d)>=2); tam2=sum(ol(d) for d in bs if sum(d)==2); tam1=sum(ol(d) for d in bs if sum(d)==1); uc=ol((1,1,1)); az1=1-ol((0,0,0))
assert az2==Fr(5,6) and tam2==Fr(13,30) and tam1==Fr(3,20) and uc==Fr(2,5) and az1==Fr(59,60)
M('0005',Fr(5,6),[(Fr(3,20),'“En az ikisi” yerine yalnızca birinin geçme olasılığını bulmuş.','dikkat'),(Fr(2,5),'Yalnızca üçünün de geçme olasılığını bulmuş: 4/5 × 3/4 × 2/3.','dikkat'),(Fr(13,30),'“En az iki” yerine “tam iki kişi” geçme olasılığını bulmuş; üçünün de geçtiği durumu eklememiş.','dikkat'),(Fr(59,60),'“En az biri geçer” olasılığını bulmuş: 1 − 1/5 × 1/4 × 1/3.','bilgi')],
 tipId='olb-bagimsiz',tip='Bağımsız olaylar ve en az bir',z='zor',alt='Bağımsız Olaylar',kaz='Bağımsız üç olayda “en az ikisi” olayını tam iki ve üçü de durumlarına ayırarak olasılığını bulur.',kalip='hikâyeli',
 kart='K-OLB-03 (bağımsız olaylar) · ehliyet sınavında en az ikisinin geçmesi',
 metin='Zeynep, Ahmet ve Deniz aynı gün ayrı salonlarda ehliyet sınavına giriyor. Sınavı geçme olasılıkları sırasıyla 4/5, 3/4 ve 2/3’tür; üç kişinin sınav sonuçları birbirini etkilememektedir.\nBu üç kişiden en az ikisinin sınavı geçme olasılığı kaçtır?',
 istenen='En az iki kişinin geçme olasılığı.',
 ip=['“En az iki” olayını kaç ayrı duruma bölebilirsin? Her durumun olasılığını ayrı yaz.'],
 bilgi=[BAG,TOPL],
 ad=[A('Durumları ayır','En az iki kişi geçer: tam iki kişi geçer ya da üçü de geçer.','2 grup durum'),A('Üçü de geçer','Bağımsız olaylar; olasılıklar çarpılır.','4/5 × 3/4 × 2/3 = 2/5'),A('Tam iki kişi geçer','Üç ayrı durum: Deniz kalır, Ahmet kalır ya da Zeynep kalır.','4/5 × 3/4 × 1/3 + 4/5 × 1/4 × 2/3 + 1/5 × 3/4 × 2/3 = 6/30 + 4/30 + 3/30 = 13/30'),A('Toplam','Durumlar aynı anda olamaz; olasılıkları topla.','2/5 + 13/30 = 12/30 + 13/30 = 25/30 = 5/6')],
 puf='“En az iki” = “tam iki” ya da “üçü de”; bağımsız olaylarda her durumun olasılığı çarpılır, durumlar toplanır.')

# ---------- 06 orta · heyet, aynı meslek ----------
G6=['m']*5+['a']*4; cs=list(combinations(range(9),3))
ayni=[c for c in cs if len({G6[i] for i in c})==1]; assert Fr(len(ayni),len(cs))==Fr(1,6) and len(cs)==84 and len(ayni)==14
assert Fr(comb(4,3),84)==Fr(1,21) and Fr(comb(5,3),84)==Fr(5,42) and Fr(5*4+4*3,9*8)==Fr(4,9) and 1-Fr(1,6)==Fr(5,6)
M('0006',Fr(1,6),[(Fr(1,21),'Yalnızca üç mimarın seçildiği durumu saymış: C(4, 3)/C(9, 3).','dikkat'),(Fr(5,42),'Yalnızca üç mühendisin seçildiği durumu saymış: C(5, 3)/C(9, 3).','dikkat'),(Fr(4,9),'Yalnızca ilk iki kişinin aynı meslekten olma olasılığını bulmuş.','dikkat'),(Fr(5,6),'Üç kişinin aynı meslekten olmama olasılığını (tümleyenini) bulmuş.','bilgi')],
 tipId='olb-sayma',tip='Kombinasyonla olasılık',z='orta',alt='Kombinasyonla Olasılık',kaz='Aynı anda yapılan seçimde iki ayrı grubun durumlarını kombinasyonla sayarak olasılığı bulur.',kalip='hikâyeli',
 kart='K-OLB-04 (kombinasyonla olasılık) · heyetin tamamı aynı meslekten',
 metin='Bir mimarlık ofisinde 5 mühendis ve 4 mimar çalışmaktadır. Bu 9 kişi arasından, aynı anda rastgele 3 kişi seçilerek bir heyet oluşturuluyor (heyette görev ayrımı yoktur, sıra önemsizdir).\nHeyetteki üç kişinin de aynı meslekten olma olasılığı kaçtır?',
 istenen='Heyetin üç üyesinin de aynı meslekten olma olasılığı.',
 ip=['Aynı meslekten olmanın hangi iki ayrı biçimde gerçekleşebileceğini bul; tüm seçimlerin sayısıyla karşılaştır.'],
 bilgi=[KOMB,TOPL],
 ad=[A('Tüm seçimler','9 kişiden 3 kişi, aynı anda.','C(9, 3) = 84'),A('İstenen seçimler','Üçü de mühendis ya da üçü de mimar.','C(5, 3) + C(4, 3) = 10 + 4 = 14'),A('Olasılık','İstenen seçimleri tüm seçimlere böl.','14/84 = 1/6')],
 puf='Aynı anda seçimde pay ve payda kombinasyonla, ikisi de sırasız sayılır; “ya da” durumları toplanır.')

# ---------- 07 orta · test, en az bir doğru ----------
pd=Fr(1,4); az1=1-(1-pd)**3
assert az1==Fr(37,64) and pd**3==Fr(1,64) and 3*pd**2*(1-pd)==Fr(9,64) and (1-pd)**3==Fr(27,64) and 1-pd**3==Fr(63,64)
ex=sum(1 for x in product(range(4),repeat=3) if any(v==0 for v in x)); assert Fr(ex,64)==Fr(37,64)
M('0007',Fr(37,64),[(Fr(1,64),'Üç sorunun da doğru olma olasılığını bulmuş: (1/4)³.','dikkat'),(Fr(9,64),'“En az bir” yerine “tam iki soru doğru” olasılığını bulmuş: 3 × (1/4)² × 3/4.','dikkat'),(Fr(27,64),'Hiç doğru olmama olasılığını bulup tümleyeni almamış: (3/4)³.','bilgi'),(Fr(63,64),'Hiç doğru olmama olasılığında yanlış şık olasılığı 3/4 yerine 1/4 alıp 1 − (1/4)³ hesaplamış.','islem')],
 tipId='olb-bagimsiz',tip='Bağımsız olaylar ve en az bir',z='orta',alt='En Az Bir',kaz='Bağımsız denemelerde “en az bir” olayının olasılığını tümleyen olayla bulur.',kalip='hikâyeli',
 kart='K-OLB-03 (en az bir, tümleyen) · 4 şıklı testte rastgele işaretleme',
 metin='Bir bilgi testinde her sorunun 4 şıkkı vardır ve şıklardan yalnızca biri doğrudur. Bir öğrenci 3 soruyu şıkları rastgele işaretleyerek cevaplıyor; soruların cevapları birbirini etkilemiyor.\nÖğrencinin bu 3 sorudan en az birini doğru cevaplama olasılığı kaçtır?',
 istenen='En az bir sorunun doğru cevaplanma olasılığı.',
 ip=['“En az bir doğru” olayının tersi olan olayın olasılığı kolay mı hesaplanır?'],
 bilgi=[TUM,BAG],
 ad=[A('Bir soruda yanlış','Rastgele işaretlemede yanlış şık seçme olasılığı.','3/4'),A('Üçünde de yanlış','Sorular bağımsız; olasılıklar çarpılır.','(3/4)³ = 27/64'),A('Tümleyen','En az bir doğru = 1 − hiç doğru yok.','1 − 27/64 = 37/64')],
 puf='“En az bir” görünce “hiç yok” olasılığını bul ve 1’den çıkar.')

# ---------- 08 orta · çark ----------
acl=[40,60,80,100,80]; assert sum(acl)==360
istek=acl[0]+acl[2]+acl[4]; assert Fr(istek,360)==Fr(5,9) and Fr(160,360)==Fr(4,9) and Fr(260,360)==Fr(13,18) and Fr(40+3*80,360)==Fr(7,9) and 360-100-60==istek==200
M('0008',Fr(5,9),[(Fr(4,9),'İstenen olmayan dilimlerin (60° ve 100°) olasılığını bulmuş: 160/360.','dikkat'),(Fr(3,5),'Dilimleri eşit olasılıklı sanmış: 5 dilimden 3’ü.','bilgi'),(Fr(13,18),'100°’lik dilimde durmama olasılığını bulmuş: (360 − 100)/360.','dikkat'),(Fr(7,9),'80°’lik dilimi üç kez sayıp (40 + 3 × 80)/360 hesaplamış.','islem')],
 tipId='olb-geometrik',tip='Geometrik olasılık',z='kolay',alt='Geometrik Olasılık',kaz='Dilimlerin merkez açılarıyla orantılı olasılığı toplam açıya oranlayarak bulur.',kalip='düz',
 kart='K-OLB-05 (çark, merkez açı oranı) · 40°, 60°, 80°, 100°, 80° dilimleri',
 metin='Bir çark, merkezi etrafında 5 dilime ayrılmıştır; dilimlerin merkez açıları sırasıyla 40°, 60°, 80°, 100° ve 80°’dir. Çark çevrilip bırakıldığında ibre, bir dilimde durur; ibrenin bir dilimde durma olasılığı o dilimin merkez açısıyla doğru orantılıdır (ibre dilim sınırında durmaz).\nİbrenin 40°’lik dilimde ya da 80°’lik dilimlerden birinde durma olasılığı kaçtır?',
 istenen='İbrenin istenen dilimlerde durma olasılığı.',
 ip=['Dilimlerin sayısı mı yoksa açıları mı olasılığı belirliyor? İstenen dilimlerin açılarını topla.'],
 bilgi=[GEO,TOPL],
 ad=[A('İstenen dilimler','40°’lik dilim ve 80°’lik iki dilim.','40° + 80° + 80° = 200°'),A('Tüm çark','Dilimlerin açıları toplamı bir tam turdur.','360°'),A('Olasılık','İstenen açıyı toplam açıya böl.','200/360 = 5/9')],
 puf='Olasılık dilim sayısına değil, dilimin merkez açısına bağlıdır; açıları toplayıp 360°’ye böl.')

# ---------- 09 orta · hedef tahtası ----------
assert Fr(4**2,6**2)==Fr(4,9) and Fr(2**2,6**2)==Fr(1,9) and Fr(4**2-2**2,6**2)==Fr(1,3) and Fr(4,6)==Fr(2,3) and Fr(6**2-2**2,6**2)==Fr(8,9)
M('0009',Fr(4,9),[(Fr(1,9),'Yalnızca en içteki dairenin (r = 2 cm) olasılığını bulmuş: 4π/36π.','dikkat'),(Fr(1,3),'Yalnızca ortadaki halkanın alanını almış: (16π − 4π)/36π.','dikkat'),(Fr(2,3),'Yarıçap oranını (4/6) olasılık sanmış; alan oranı yarıçapların karelerinin oranıdır.','bilgi'),(Fr(8,9),'En içteki daire dışında kalan bölgenin alanını almış: (36π − 4π)/36π.','dikkat')],
 tipId='olb-geometrik',tip='Geometrik olasılık',z='kolay',alt='Geometrik Olasılık',kaz='Eş merkezli dairelerde alan oranıyla geometrik olasılığı bulur.',kalip='düz',
 kart='K-OLB-05 (hedef tahtası, alan oranı) · yarıçapları 2, 4, 6 cm',
 metin='Yarıçapları 2 cm, 4 cm ve 6 cm olan eş merkezli üç çember, bir hedef tahtasını oluşturuyor; tahta, yarıçapı 6 cm olan dairesel bölgedir. Bir ok, tahtanın her noktasına eşit olasılıkla saplanıyor; okun çizgiler üzerine saplanma olasılığı sıfırdır.\nOkun yarıçapı 4 cm olan dairenin içine saplanma olasılığı kaçtır?',
 istenen='Okun yarıçapı 4 cm olan dairenin içine saplanma olasılığı.',
 ip=['Olasılık hangi iki büyüklüğün oranıdır? Alan formülünde yarıçap nasıl yer alır?'],
 bilgi=[GEO],
 ad=[A('İstenen bölgenin alanı','Yarıçapı 4 cm olan daire.','π × 4² = 16π'),A('Tüm tahtanın alanı','Yarıçapı 6 cm olan daire.','π × 6² = 36π'),A('Olasılık','Alanları oranla.','16π/36π = 4/9')],
 puf='Geometrik olasılıkta alanlar oranlanır; yarıçap oranı değil, yarıçapların kareleri oranı alınır.')

# ---------- 10 orta · zar ve para ----------
OO=list(product(range(1,7),'TY')); assert len(OO)==12
ev=[o for o in OO if (o[0]>4 and o[1]=='T') or (o[0]%2==0 and o[1]=='Y')]; assert Fr(len(ev),12)==Fr(5,12)
assert Fr(2,12)==Fr(1,6) and 1-Fr(5,12)==Fr(7,12) and Fr(len([x for x in range(1,7) if x>4 or x%2==0]),6)==Fr(2,3) and Fr(2,6)+Fr(3,6)==Fr(5,6)
M('0010',Fr(5,12),[(Fr(1,6),'Yalnızca ilk olayı (zar 4’ten büyük ve tura) saymış: 2/12.','dikkat'),(Fr(7,12),'Olayın olasılığını bulup tümleyenini yazmış: 1 − 5/12.','bilgi'),(Fr(2,3),'Paranın sonucunu hiç kullanmayıp zarın “4’ten büyük ya da çift” gelme olasılığını bulmuş.','dikkat'),(Fr(5,6),'Zar olaylarının olasılıklarını (1/3 + 1/2) toplamış; paranın sonucunu ve ortak durumu hesaba katmamış.','islem')],
 tipId='olb-temel',tip='Örnek uzay ve olay',z='orta',alt='Basit Olay',kaz='Zar ve paranın birlikte atıldığı deneyde örnek uzayı sayıp birleşik bir olayın olasılığını bulur.',kalip='düz',
 kart='K-OLB-01 (örnek uzay, zar ve para) · iki ayrı koşullu olay',
 metin='Hilesiz bir zar ile hilesiz bir madeni para birlikte atılıyor.\n(Zarın 4’ten büyük gelmesi ve paranın tura gelmesi) olayı ya da (zarın çift gelmesi ve paranın yazı gelmesi) olayından en az birinin gerçekleşme olasılığı kaçtır?',
 istenen='İstenen iki durumdan birinin gerçekleşme olasılığı.',
 ip=['Zar ve paranın birlikte oluşturduğu örnek uzayı sırala; her koşul için paranın sonucunu da kontrol et.'],
 bilgi=[OL,TOPL],
 ad=[A('Örnek uzay','Zarın 6, paranın 2 sonucu var.','6 × 2 = 12 sonuç'),A('Birinci durum','Zar 5 ya da 6 ve para tura.','(5, T), (6, T) → 2 sonuç'),A('İkinci durum','Zar 2, 4 ya da 6 ve para yazı; paranın sonucu farklı olduğundan iki durum ayrıdır.','(2, Y), (4, Y), (6, Y) → 3 sonuç'),A('Olasılık','Sonuçları topla, örnek uzaya böl.','(2 + 3)/12 = 5/12')],
 puf='Birlikte yapılan deneylerde örnek uzay sonuçların çarpımıdır; durumların aynı anda olup olmadığını kontrol ederek say.')

# ---------- 11 zor · kura ----------
T=list(combinations(range(20),3)); ali={0,1}
kz=[c for c in T if ali&set(c)]; assert len(T)==1140 and Fr(len(kz),len(T))==Fr(27,95) and len(kz)==324
assert Fr(comb(18,3),1140)==Fr(68,95) and Fr(2*comb(18,2),1140)==Fr(51,190) and Fr(comb(2,2)*18,1140)==Fr(3,190) and Fr(2,20)==Fr(1,10)
assert 1-Fr(18,20)**3==Fr(271,1000) and Fr(2*comb(18,2),1140)<Fr(271,1000)<Fr(27,95)
M('0011',Fr(27,95),[(Fr(3,190),'Ali’nin iki biletinin de ödül kazanma olasılığını bulmuş: C(2, 2) × 18/C(20, 3).','dikkat'),(Fr(1,10),'Tek çekilişteki olasılığı (2/20) vermiş.','dikkat'),(Fr(51,190),'“En az bir” yerine “tam bir ödül” olasılığını bulmuş: 2 × C(18, 2)/C(20, 3).','bilgi'),(Fr(271,1000),'Biletleri geri koyarak çekilmiş gibi 1 − (18/20)³ hesaplamış.','bilgi')],
 tipId='olb-sayma',tip='Kombinasyonla olasılık',z='orta',alt='Kombinasyonla Olasılık',kaz='Kura çekilişinde “en az bir bilet kazanır” olasılığını kombinasyon ve tümleyen olayla bulur.',kalip='hikâyeli',
 kart='K-OLB-04 (kombinasyonla olasılık, tümleyen) · kura',
 metin='Bir okulun kermesinde 1’den 20’ye kadar numaralanmış 20 bilet satılmıştır ve her bilet bir kişiye aittir. Kuradan 3 ödül verilecektir: ödüllü biletler, torbadan geri konmadan art arda 3 bilet çekilerek belirlenir (ödüllerin sırası önemli değildir, aynı bilet iki ödül kazanamaz).\nAli’nin 2 bileti olduğuna göre Ali’nin en az bir ödül kazanma olasılığı kaçtır?',
 istenen='Ali’nin en az bir ödül kazanma olasılığı.',
 ip=['Ali’nin biletleri hangi çekiliş sonuçlarında hiç yer almaz?'],
 bilgi=[KOMB,TUM],
 ad=[A('Tüm çekilişler','20 biletten 3 bilet, sıra önemsiz.','C(20, 3) = 1140'),A('Ali hiç kazanmaz','3 ödüllü bilet Ali’nin olmayan 18 biletten çıkar.','C(18, 3) = 816'),A('Hiç kazanmama olasılığı','Sayıları oranla.','816/1140 = 68/95'),A('Tümleyen','En az bir = 1 − hiç kazanmama.','1 − 68/95 = 27/95')],
 puf='“En az bir” kazanmanın tersi “hiç kazanmama”dır; aynı çekilişte pay ve paydayı sırasız (kombinasyonla) say.')

# ---------- 12 zor · şifre tahmini ----------
ss=[s for s in permutations(range(1,7),4) if s[0]%2==0 and s[3]%2==1]
assert len(ss)==108 and Fr(2,len(ss))==Fr(1,54) and Fr(1,108)==Fr(1,len(ss))
assert 3*5*4*3==180 and Fr(2,180)==Fr(1,90) and 3*6*6*3==324 and Fr(2,324)==Fr(1,162) and 6*5*4*3==360 and Fr(2,360)==Fr(1,180)
M('0012',Fr(1,54),[(Fr(1,180),'İlk ve son rakam koşullarını uygulamadan yalnızca rakamların farklı olmasıyla 6 × 5 × 4 × 3 = 360 şifre sayıp 2/360 bulmuş.','dikkat'),(Fr(1,162),'Rakamların tekrar edebileceğini düşünüp 3 × 6 × 6 × 3 = 324 şifre sayıp 2/324 bulmuş.','bilgi'),(Fr(1,108),'Yalnızca bir deneme hakkı olduğunu düşünüp 1/108 bulmuş.','dikkat'),(Fr(1,90),'İlk rakamın çift olma koşulunu unutup yalnızca son rakamın tek olmasını uygulamış (180 şifre): 2/180.','dikkat')],
 tipId='olb-yeninesil',tip='Yeni nesil ve öncüllü olasılık',z='orta',alt='Hikâyeli',kaz='Koşullu şifre sayısını sayma ilkesiyle bulup iki denemede doğru tahmin olasılığını hesaplar.',kalip='hikâyeli',
 kart='K-OLB-06 (şifre tahmini) · ilk rakam çift, son rakam tek, iki deneme',
 metin='Mert, kasasının 4 haneli şifresini unutmuştur. Şifrenin rakamlarının 1, 2, 3, 4, 5, 6 rakamlarından seçildiğini, birbirinden farklı olduğunu, ilk rakamının çift ve son rakamının tek olduğunu hatırlamaktadır. Bu koşullara uyan şifreler arasından rastgele iki farklı şifreyi deneyecektir (aynı şifreyi iki kez denemeyecektir).\nBuna göre Mert’in iki denemeden en az birinde şifreyi bulma olasılığı kaçtır?',
 istenen='İki denemeden birinde doğru şifreyi bulma olasılığı.',
 ip=['Mert’in hatırladığı koşullara uyan kaç farklı şifre vardır? Sonra denemelerin hangi şifrelere denk geldiğine bak.'],
 bilgi=[OL,B('Koşullu şifre sayma','Önce koşullu basamakları doldur, sonra kalan basamakları kalan rakamlarla sırala; seçenek sayıları çarpılır. Örnek: rakamları farklı ve ilk rakamı 1 ya da 2 olan 3 basamaklı şifreler (rakamlar 1, 2, 3, 4) için 2 × 3 × 2 = 12 şifre vardır')],
 ad=[A('Koşullu şifre sayısı','İlk rakam çift (2, 4, 6), son rakam tek (1, 3, 5), ortadaki iki rakam kalan 4 rakamdan sıralı.','3 × 3 × 4 × 3 = 108'),A('İki farklı deneme','Aranan şifre bu 108 şifreden biri; Mert 2 farklı şifre dener.','2 şifre'),A('Olasılık','Denenen şifre sayısını tüm şifrelere oranla.','2/108 = 1/54')],
 puf='Önce koşullara uyan tüm şifrelerin sayısını bul; farklı iki deneme olduğundan deneme sayısı paya yazılır.')

# ---------- 13 zor · oyun kuralı ----------
S2=Fr(len([o for o in O if sum(o)>=8]),36); S3=Fr(len([o for o in O if 4<=sum(o)<=7]),36); S4=Fr(len([o for o in O if sum(o)<4]),36)
y2=Fr(len([o for o in O if sum(o)>=7]),36)
assert (S2,S3,S4,y2)==(Fr(5,12),Fr(1,2),Fr(1,12),Fr(7,12)) and S2+S3*y2==Fr(17,24)
assert S2*y2==Fr(35,144) and S2+(1-S2)*y2==Fr(109,144)
M('0013',Fr(17,24),[(Fr(35,144),'İki aşamayı da çarpıp 5/12 × 7/12 hesaplamış.','islem'),(Fr(5,12),'Yalnızca ilk atıştaki kazanma olasılığını bulmuş; ikinci atış hakkını atlamış.','dikkat'),(Fr(7,12),'Yalnızca ikinci atışın kazanma olasılığını bulmuş.','dikkat'),(Fr(109,144),'Toplamı 4’ten küçük olanların da ikinci atış hakkı olduğunu sanmış: 5/12 + 7/12 × 7/12.','bilgi')],
 tipId='olb-yeninesil',tip='Yeni nesil ve öncüllü olasılık',z='zor',alt='Yeni Nesil',kaz='Çok aşamalı bir oyun kuralında her durumun olasılığını bulup toplam kazanma olasılığını hesaplar.',kalip='yeni nesil',
 kart='K-OLB-06 (yeni nesil, oyun kuralı) · iki aşamalı zar oyunu',
 metin='Bir oyunda oyuncu, biri kırmızı biri mavi olan iki hilesiz zarı birlikte atar ve üst yüzlerdeki sayıların toplamına bakılır. Oyunun kuralı şöyledir:\n• Toplam 8 ya da daha büyükse oyuncu oyunu kazanır.\n• Toplam 4, 5, 6 ya da 7 ise oyuncu iki zarı bir kez daha atar; bu ikinci atışta toplam 7 ya da daha büyükse oyunu kazanır, değilse kaybeder.\n• Toplam 4’ten küçükse oyuncu oyunu kaybeder.\nBuna göre bir oyuncunun oyunu kazanma olasılığı kaçtır?',
 istenen='Oyunu kazanma olasılığı.',
 ip=['İlk atışın sonucuna göre oyunun kaç farklı yönde ilerlediğini ayır; her yönün olasılığını ayrı bul.'],
 bilgi=[OL,TOPL],
 ad=[A('İlk atışta kazanma','Toplam 8, 9, 10, 11, 12: 5 + 4 + 3 + 2 + 1 = 15 sonuç.','15/36 = 5/12'),A('İkinci atışa kalma','Toplam 4, 5, 6, 7: 3 + 4 + 5 + 6 = 18 sonuç.','18/36 = 1/2'),A('İkinci atışta kazanma','İkinci atışta toplam 7 ya da daha büyük: 6 + 5 + 4 + 3 + 2 + 1 = 21 sonuç.','21/36 = 7/12'),A('Toplam kazanma','İki ayrı yoldan kazanma olasılıkları toplanır.','5/12 + 1/2 × 7/12 = 10/24 + 7/24 = 17/24')],
 puf='Çok aşamalı kurallarda her yolu ayrı ayrı yaz: yol üzerindeki olasılıklar çarpılır, kazanan yollar toplanır.')

# ---------- 14 zor · öncüllü, torba ----------
TB=['k']*4+['m']*2
I_=sum(1 for d in permutations(range(6),2) if 'm' in (TB[d[0]],TB[d[1]])); assert Fr(I_,30)==Fr(3,5)
II_=sum(1 for c in combinations(range(6),3) if sorted(TB[i] for i in c)==['k','k','m']); assert Fr(II_,20)==Fr(3,5)
III_=sum(1 for c in combinations(range(6),2) if TB[c[0]]!=TB[c[1]]); assert Fr(III_,15)==Fr(8,15)
assert Fr(4,6)*Fr(3,5)*Fr(2,4)==Fr(1,5) and 1-Fr(2,3)**2==Fr(5,9) and 1-Fr(comb(4,2),comb(6,2))==Fr(3,5)
SI=['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III']
mk(P,'0014',tipId='olb-yeninesil',tip='Yeni nesil ve öncüllü olasılık',z='zor',alt='Öncüllü',kaz='Geri konmadan, aynı anda ve art arda çekiliş durumlarının olasılıklarını ayrı ayrı hesaplayıp öncülleri değerlendirir.',kalip='öncüllü',adim=4,
 kart='K-OLB-06 (öncüllü) · 4 kırmızı 2 mavi bilyeli torba, üç ayrı çekiliş',
 metin='Bir torbada 4 kırmızı ve 2 mavi bilye vardır. Bu torbadan aşağıdaki çekilişler ayrı ayrı yapılıyor.\nI. Art arda, geri konmadan 2 bilye çekiliyor; çekilenlerin en az birinin mavi olması.\nII. Aynı anda 3 bilye çekiliyor; çekilenlerin 2’sinin kırmızı, 1’inin mavi olması.\nIII. Aynı anda 2 bilye çekiliyor; çekilenlerin farklı renkte olması.\nBu olayların hangilerinin olasılığı 3/5’tir?',
 dogru='I ve II',sira=SI,yan=[('Yalnız I','II’yi yalnızca kırmızı–kırmızı–mavi sırası için hesaplamış: 4/6 × 3/5 × 2/4 = 1/5; mavinin yerini seçmeyi atlamış.','dikkat'),('Yalnız II','I’de bilyeleri geri koymuş gibi 1 − (2/3)² = 5/9 bulup I’i yanlış saymış.','bilgi'),('I ve III','II’yi yalnızca bir sırayla hesaplayıp 1/5 bulmuş; III’te “farklı renk” yerine “en az bir mavi” hesabıyla 1 − 6/15 = 3/5 bulmuş.','bilgi'),('I, II ve III','III’te “farklı renk” yerine “en az bir mavi” olasılığını (3/5) hesaplamış.','dikkat')],
 istenen='Olasılığı 3/5 olan olaylar.',
 ip=['Her çekilişte tüm durumların sayısını ve istenen durumların sayısını ayrı bul; çekiliş türünün (geri konmadan art arda / aynı anda) olasılığı nasıl etkilediğini düşün.'],
 bilgi=[IADE,KOMB,TUM],
 ad=[A('I','Hiç mavi gelmeme olasılığı 4/6 × 3/5 = 2/5; tümleyeni alınır.','1 − 2/5 = 3/5'),A('II','Aynı anda 3 bilye; 2 kırmızı ve 1 mavi seçimi.','C(4, 2) × C(2, 1)/C(6, 3) = 12/20 = 3/5'),A('III','Aynı anda 2 bilye; 1 kırmızı ve 1 mavi seçimi.','C(4, 1) × C(2, 1)/C(6, 2) = 8/15'),A('Karşılaştır','I ve II’nin değeri 3/5’tir; III 3/5 değildir.','I ve II')],
 puf='Aynı anda çekilişte sıra önemsizdir; her öncülün olasılığını ayrı ayrı hesapla, çekiliş türünü (geri konmadan, aynı anda) belirle.')

bitir(P,'olasiki',UK)
