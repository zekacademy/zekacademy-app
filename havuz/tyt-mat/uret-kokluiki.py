"""Köklü Sayılar · parti 2 (hafif mod): 14 yeni ana soru, kardeş yok, ipucu 1. Köklü değerler 60 basamaklı Decimal ile, tam sayısal olanlar Fraction ile doğrulanır; her çeldirici, tarif edilen hatadan yeniden üretilir."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_mat as H
from _hafif_mat import *
from decimal import Decimal as Dc,getcontext
from math import isqrt
getcontext().prec=60
H.KONU='Köklü Sayılar'
P=Parti('kokluiki','Köklü Sayılar','mat|Köklü Sayılar')
UK='mat|Köklü Sayılar'
sq=lambda n:Dc(n).sqrt()
def yak(a,b,t=Dc(10)**-40): return abs(a-b)<t
def srt(ps):
    v=[x[1] for x in ps]; assert all(abs(v[i]-v[j])>Dc(10)**-30 for i in range(5) for j in range(i)),'çeldiriciler ayrışmıyor'
    return [x[0] for x in sorted(ps,key=lambda x:x[1])]

KOK=B('Kök dışına çıkarma','kök içini “tam kare × kalan” biçiminde yaz, tam karenin kökünü dışarı al. Benzer köklerin katsayıları toplanır ya da çıkarılır. Örnek: √12 = √(4 × 3) = 2√3 · 2√3 + 5√3 = 7√3')
CK=B('Köklerde çarpma ve bölme','√a × √b = √(a × b) ve √a ÷ √b = √(a ÷ b); katsayılar katsayılarla çarpılır. Örnek: 2√3 × 4√3 = 8 × √9 = 24')
ESL=B('Paydayı rasyonel yapma (eşlenik)','paydası √a − √b olan kesir, √a + √b ile genişletilir: (√a − √b)(√a + √b) = a − b. Örnek: 1/(√3 − 1) = (√3 + 1)/(3 − 1)')
MUT=B('√(a²) = |a|','karekök negatif olamaz; bu yüzden √(a²) = |a| olur: a ≥ 0 ise a, a < 0 ise −a. Örnek: √((−4)²) = 4 · a < 0 ise |a − 3| = 3 − a')
TAHMIN=B('Karekök tahmini','a² < n < b² ise a < √n < b olur. Örnek: 16 < 18 < 25 olduğundan 4 < √18 < 5')
ONDALIK=B('Ondalık sayının karekökü','ondalık sayıyı 100’ün (ya da 10000’in) bölümü olarak yaz: √0,09 = √(9/100) = 3/10 = 0,3. Örnek: √0,0025 = 5/100 = 0,05')
IC=B('İç içe kökler','içteki kök önce hesaplanır, sonra bir dıştaki kök alınır. Örnek: √(1 + √(9 + 7)) = √(1 + 4) = √5')
TKARE=B('Tam kare açılımı','a + b ve a × b ile (√a ± √b)² = (a + b) ± 2√(ab) olduğundan, 11 − 6√2 gibi bir kök içi (3 − √2)² biçiminde yazılabilir. Örnek: 7 + 4√3 = (2 + √3)²')
DEN=B('Köklü denklem','iki tarafın karesi alınır; (a√b)² = a² × b olduğundan katsayı da karesiyle girer. Bulunan değer kök içlerini negatif yapmamalıdır. Örnek: 3√x = √(x + 8) → 9x = x + 8 → x = 1')
ALAN=B('Kare: alan ve kenar','alanı A olan karenin kenarı √A, çevresi 4√A’dır. Örnek: alan 50 → kenar √50 = 5√2, çevre 20√2')
KARE=B('Kareköklü tam sayı koşulu','√n bir tam sayı ise n tam karedir; n = a² × b (b kare çarpanı olmayan) ise √n = a√b olur. Örnek: 12 = 2² × 3 → √12 = 2√3 · 16 = 4² → √16 = 4')
TELE=B('Teleskopik toplam','1/(√k + √(k+1)) = √(k+1) − √k (eşlenikle genişletme). Ardışık terimlerde ortadaki kökler birbirini götürür. Örnek: (√2 − 1) + (√3 − √2) = √3 − 1')

# ---------- kartlar ----------
KY='ÖSYM 2018–2026 (köklü ifadeler) · yayın soru bankaları (yalnız mantık) · MEB 9. sınıf'
kart('K-KKLB-01','Kök dışına çıkarma, toplama ve çıkarma','Kök içleri tam kare çarpanlarıyla ayrılır, benzer köklerin katsayıları toplanıp çıkarılır.','Kök içlerini toplayıp çıkarmak; dışarı çıkan sayının kökünü almayı unutmak; çıkarılan terimin işaretini kaçırmak.','kolay','düz',2,'kkb-disari','Kök dışına çıkarma, toplama ve çıkarma',KY)
kart('K-KKLB-02','Ondalık sayıların karekökü','Ondalık sayılar 100’ün kesri olarak yazılıp kök alınır; virgülün kayması kontrol edilir.','Virgülü kök sonrası yanlış kaydırmak; ondalıktaki sıfır sayısını yarılamamak; işareti atlamak.','kolay','düz',2,'kkb-ondalik','Ondalık sayıların karekökü',KY)
kart('K-KKLB-03','Katsayılı köklerde çarpma ve bölme','Katsayılar katsayılarla, kök içleri kök içleriyle çarpılıp bölünür ve sonuç sadeleştirilir.','Katsayıları toplamak; kök içi tam karenin kökünü almamak; kök dışındaki sayıyı bölmeye katmak.','kolay','düz',2,'kkb-carpma','Katsayılı köklerde çarpma ve bölme',KY)
kart('K-KKLB-04','Paydayı rasyonel yapma','Paydadaki iki terimli köklü ifade eşlenikle genişletilip payda tam sayı yapılır.','Eşleniği aynı işaretle almak; paydayı hesaplayıp pay ile bölmeyi unutmak; kök içlerini toplamak.','orta','düz',3,'kkb-eslenik','Paydayı rasyonel yapma ve eşlenik',KY)
kart('K-KKLB-05','√(a²) = |a| ve işaret koşulu','Değişkenin işareti verilir; kök altındaki kareler mutlak değere, mutlak değerler işarete göre açılır.','√(a²) = a yazmak; mutlak değeri işaret koşulundan bağımsız açmak; negatif sayıdan sonra işareti kaybetmek.','orta','düz',3,'kkb-mutlak','Kök içindeki kare ve mutlak değer',KY)
kart('K-KKLB-06','Köklü ifadenin iki ardışık tam sayı arasındaki yeri','Her kök, tam kareler arasında sıkıştırılarak tahmin edilir; sınırlar iki aralığa yayılırsa toplamın karesi alınıp tam karelerle sınırlanır.','Kök içlerini toplayıp tek köke dönüştürmek; üst ya da alt sınırlardan birini almak; yuvarlama hatası.','zor','düz',3,'kkb-siralama','Köklü sayıların tahmini ve ardışık tam sayılar',KY)
kart('K-KKLB-07','İç içe kökler (içten dışa)','İçteki kök hesaplanır, toplamı alınır ve bir dıştaki kök alınır; her adımda tam kare aranır.','Dıştaki kökü almayı unutmak; √16 = 8 yazmak; bir toplamı atlamak.','kolay','düz',2,'kkb-ic','İç içe kökler',KY)
kart('K-KKLB-08','Basit köklü denklem','Kök içleri eşitlenecek biçimde iki tarafın karesi alınır; katsayı da kareye girer, çıkan değer kök içlerinin tanım koşuluyla denenir.','Katsayıyı karesiz almak; parantezi dağıtmamak; taşıma hatası.','orta','düz',3,'kkb-denklem','Basit köklü denklem',KY)
kart('K-KKLB-09','Kare alanından kenar ve çevre (sözel bağlam)','Alandan kenar kök dışına çıkarılarak bulunur; çevre ve aralıkla ilgili sayma sorusu köklü oranla çözülür.','Kenarı yanlış sadeleştirmek; çevreyi 2 × kenar almak; kapalı çevrede aralık sayısı ile direk sayısını karıştırmak.','orta','hikâyeli',3,'kkb-baglam','Kare ve dikdörtgen bağlamında köklü işlemler',KY)
kart('K-KKLB-10','Köklü ifadelerle öncüllü sorular','Her öncül kök dışına çıkarma, eşlenik çarpımı ya da ondalık kökle ayrı ayrı kanıtlanır.','Kök içlerini toplamak; (a − b)(a + b) = a − b sanmak; ondalık kökte basamak hatası.','orta','öncüllü',3,'kkb-oncul','Köklü ifadelerde öncüllü sorular',KY)
kart('K-KKLB-11','Eşlenik değerlerle simetrik ifade','x = √7 + √3 ve y = √7 − √3 için x² + y² ve x × y özdeşliklerle bulunur; oran hesaplanır.','x²+y² yerine (x+y)² ya da (x−y)² yazmak; x × y için kök içlerini çıkarmak; çarpım yerine toplam almak.','zor','düz',4,'kkb-ozdeslik','Köklü ifadelerde özdeşlik ve işlem',KY)
kart('K-KKLB-12','Eşlenikle iki kesrin toplamı','İki kesir de eşlenikle genişletilip payda 1 yapılır, sonra toplanır.','Eşlenikteki işareti karıştırmak; paydayı 1 sanıp payı genişletmemek; toplama yerine çarpma yapmak.','orta','düz',3,'kkb-eslenik','Paydayı rasyonel yapma ve eşlenik',KY)
kart('K-KKLB-13','Tanımlı kavram: kök dışına çıkarılabilen sayı','Tanım sadeleşebilen ama tam sayı olmayan kökleri seçer; kare çarpanı olan sayılar sayılıp tam kareler ayıklanır.','Tam kareleri de saymak; kare çarpanları kümelerini atlamak; çakışan sayıları iki kez saymak.','zor','yeni nesil',4,'kkb-tanimli','Tanımlı kök dışına çıkarılabilir sayıları sayma','ÖSYM 2022–2026 (yeni nesil tanımlı kavram) · yayın: kök dışına çıkabilen sayıları sayma')
kart('K-KKLB-14','Dikdörtgenin çevre–alan oranı (sözel bağlam)','Kenarlar √48 ve √75 kök dışına çıkarılır; çevre ve alan hesaplanır, oran sadeleştirilir.','Çevreyi 2 ile çarpmamak; alanı kök içlerini toplayarak bulmak; √3 × √3 = 3’ü unutmak; oranı ters kurmak.','orta','hikâyeli',4,'kkb-baglam','Kare ve dikdörtgen bağlamında köklü işlemler',KY)

# ---------- 01 · kolay ----------
d1=3*sq(5)+4*sq(5)-2*sq(5); assert yak(d1,5*sq(5)) and yak(sq(45),3*sq(5)) and yak(sq(80),4*sq(5)) and yak(sq(20),2*sq(5))
v1={'5√5':5*sq(5),'7√5':7*sq(5),'9√5':9*sq(5),'17√5':17*sq(5),'√105':sq(105)}
assert yak(3*sq(5)+4*sq(5),7*sq(5)) and yak(3*sq(5)+4*sq(5)+2*sq(5),9*sq(5)) and yak(3*sq(5)+16*sq(5)-2*sq(5),17*sq(5)) and 45+80-20==105
mk(P,'0001',tipId='kkb-disari',tip='Kök dışına çıkarma, toplama ve çıkarma',z='kolay',alt='Kök Dışına Çıkarma',kaz='Kök içlerini tam kare çarpanlarına ayırıp benzer köklerin katsayılarını toplar ve çıkarır.',kalip='düz',adim=2,
 kart='K-KKLB-01 (kök dışına çıkarma, toplama–çıkarma) · √45 + √80 − √20',
 metin='√45 + √80 − √20\nişleminin sonucu kaçtır?',
 dogru='5√5',sira=srt([(k,v) for k,v in v1.items()]),
 yan=[('7√5','−√20 terimini işleme katmamış: 3√5 + 4√5 = 7√5.','dikkat'),('9√5','Çıkarılan terimi toplamış: 3√5 + 4√5 + 2√5 = 9√5.','islem'),('17√5','√80’i 16√5 yazmış; 16 tam karedir, dışarı kökü olan 4 çıkar (√80 = 4√5).','bilgi'),('√105','Kök içlerini doğrudan işleme sokmuş: 45 + 80 − 20 = 105; köklerin toplamı kök içlerinin toplamının köküne eşit değildir.','bilgi')],
 istenen='İfadenin değeri.',
 ip=['Her kök içini “tam kare × kalan” olarak yaz: 45 = 9 × 5 gibi.'],
 bilgi=[KOK],
 ad=[A('Kök dışına çıkar','Her kök içinde 5’i bırakacak tam kare çarpanı ara.','√45 = √(9 × 5) = 3√5 · √80 = √(16 × 5) = 4√5 · √20 = √(4 × 5) = 2√5'),A('İfadeyi yeniden yaz','Üç terim de √5’li olduğundan ortak kök parantez dışında kalır.','3√5 + 4√5 − 2√5 = (3 + 4 − 2)√5'),A('Katsayıları işle','Önce toplama, sonra çıkarma yapılır.','(3 + 4 − 2)√5 = 5√5')],
 puf='Köklü toplama–çıkarmada önce kök içlerini aynı kök biçimine getir; ancak köklü kısımları aynı olan terimlerin katsayıları toplanıp çıkarılır.')

# ---------- 02 · kolay · ondalık ----------
d2=Fr(11,10)+Fr(7,10)-Fr(2,10); assert d2==Fr(8,5) and Fr(11,10)**2==Fr(121,100) and Fr(7,10)**2==Fr(49,100) and Fr(2,10)**2==Fr(4,100)
e1=Fr(11,10)+Fr(7,100)-Fr(2,100); e2=Fr(11,10)+Fr(7,10)+Fr(2,10); e3=Fr(11+7-2); e4=Fr(11+7-2,100)
assert (e1,e2,e3,e4)==(Fr(23,20),2,16,Fr(4,25))
mk(P,'0002',tipId='kkb-ondalik',tip='Ondalık sayıların karekökü',z='kolay',alt='Ondalık Sayıların Kökü',kaz='Ondalık sayıların karekökünü virgülün yerine dikkat ederek bulup toplama–çıkarma yapar.',kalip='düz',adim=2,
 kart='K-KKLB-02 (ondalık sayıların karekökü) · √1,21 + √0,49 − √0,04',
 metin='√1,21 + √0,49 − √0,04\nişleminin sonucu kaçtır?',
 dogru=d2,yan=[(e1,'√0,49 ve √0,04’ü 0,07 ve 0,02 almış; ondalık sayının kökünde virgülden sonraki basamak sayısı yarıya iner (2 basamak → 1 basamak).','bilgi'),(e2,'−√0,04’ü işaretini değiştirip eklemiş: 1,1 + 0,7 + 0,2.','dikkat'),(e3,'Virgülleri yok sayıp √121 + √49 − √4 = 11 + 7 − 2 = 16 hesaplamış; sonuçta virgülü geri koymamış.','dikkat'),(e4,'16 bulduktan sonra virgülü iki basamak kaydırmış; kökte virgül yalnız bir basamak kayar (÷ 10).','islem')],
 istenen='İfadenin değeri.',
 ip=['Her sayıyı 100’e bölünen bir tam sayı olarak yaz: 1,21 = 121/100.'],
 bilgi=[ONDALIK],
 ad=[A('Kesre çevir','Ondalık sayılar 100’ün kesri olarak yazılırsa pay ve payda ayrı ayrı kök alınabilir.','√(121/100) = 11/10 · √(49/100) = 7/10 · √(4/100) = 2/10'),A('Kökleri yerine yaz','Kök içleri artık sade kesirlerdir.','11/10 + 7/10 − 2/10'),A('Hesapla','Kesirler aynı paydalı; payları işle.','16/10 = 1,6')],
 puf='Ondalık sayının karekökünü almak için sayıyı 100’lü ya da 10000’li kesre çevir; virgülden sonraki basamak sayısı yarıya iner.')

# ---------- 03 · kolay · katsayılı çarpma bölme ----------
d3=Fr(3*2)*Fr(isqrt(10*5//2)); assert 10*5%2==0 and isqrt(25)**2==25 and d3==30
e1=Fr(3+2)*5; e2=Fr(5); e3=Fr(3)*5; e4=Fr(2)*5
assert (e1,e2,e3,e4)==(25,5,15,10)
mk(P,'0003',tipId='kkb-carpma',tip='Katsayılı köklerde çarpma ve bölme',z='kolay',alt='Köklerde Çarpma ve Bölme',kaz='Katsayılı köklü ifadelerde çarpma ve bölmeyi katsayılar ve kök içleri için ayrı ayrı yapar.',kalip='düz',adim=2,
 kart='K-KKLB-03 (katsayılı çarpma–bölme) · (3√10 × 2√5) ÷ √2',
 metin='(3√10 × 2√5) ÷ √2\nişleminin sonucu kaçtır?',
 dogru=30,yan=[(e1,'Katsayıları çarpmak yerine toplamış: (3 + 2) × √25 = 5 × 5.','bilgi'),(e2,'Katsayıları (3 ve 2) hesaba katmamış, yalnızca √25 = 5 yazmış.','dikkat'),(e3,'Katsayılardan yalnız 3’ü alıp (2’yi unutmuş) √25 = 5 ile çarpmış: 3 × 5 = 15.','dikkat'),(e4,'Katsayılardan yalnız 2’yi alıp (3’ü unutmuş) √25 = 5 ile çarpmış: 2 × 5 = 10.','dikkat')],
 istenen='İfadenin değeri.',
 ip=['Katsayıları kendi aralarında, kök içlerini kendi aralarında çarp ve böl.'],
 bilgi=[CK],
 ad=[A('Katsayılar ve kök içleri','Katsayılar 3 × 2 = 6; kök içlerinde çarpma ve bölme yapılır.','3 × 2 = 6 · √(10 × 5 ÷ 2) = √25 = 5'),A('Kök içini sadeleştir','Çarpma ve bölme sonrası kök içi tam kare olur.','√25 = 5'),A('Sonucu bul','Katsayı ile kökün değerini çarp.','6 × 5 = 30')],
 puf='Köklü çarpmada katsayıları katsayılarla, kök içlerini kök içleriyle işle; kök içi tam kareye dönüşünce kökü al.')

# ---------- 04 · orta · eşlenik ----------
r4=6/(sq(5)-sq(2)); assert yak(r4,2*sq(5)+2*sq(2)) and 5-2==3
v4={'2√5 + 2√2':2*sq(5)+2*sq(2),'2√5 − 2√2':2*sq(5)-2*sq(2),'6√5 + 6√2':6*sq(5)+6*sq(2),'2√7':2*sq(7),'2':Dc(2)}
assert yak(6*(sq(5)-sq(2))/(5-2),2*sq(5)-2*sq(2)) and yak(6*sq(5)+6*sq(2),6*(sq(5)+sq(2))) and yak(Dc(6)/3,Dc(2)) and len({round(v,20) for v in v4.values()})==5
mk(P,'0004',tipId='kkb-eslenik',tip='Paydayı rasyonel yapma ve eşlenik',z='orta',alt='Paydayı Rasyonel Yapma',kaz='Paydası iki terimli köklü ifade olan kesri eşlenikle genişleterek paydayı rasyonel yapar.',kalip='düz',adim=3,
 kart='K-KKLB-04 (paydayı rasyonel yapma) · 6/(√5 − √2)',
 metin='6/(√5 − √2)\nifadesinin paydası rasyonel yapıldığında aşağıdakilerden hangisi elde edilir?',
 dogru='2√5 + 2√2',sira=srt(list(v4.items())),
 yan=[('2√5 − 2√2','Paydayı eşlenikle doğru hesaplayıp 3 bulmuş ama payı paydadan kopyalayarak 6(√5 − √2)/3 yazmış; pay da (√5 + √2) ile çarpılmalıdır.','dikkat'),('6√5 + 6√2','Paydadaki 5 − 2 = 3’e bölmeyi unutmuş: 6(√5 + √2).','dikkat'),('2√7','√5 + √2 = √7 yazmış; farklı kök içli köklerin toplamı tek kökte birleşmez.','bilgi'),('2','Yalnız paydayı rasyonel yapıp (5 − 2 = 3) payı eşlenikle çarpmayı unutmuş: 6/3 = 2.','dikkat')],
 istenen='Paydası rasyonel yapılmış eşit ifade.',
 ip=['Payı ve paydayı, paydanın eşleniği olan (√5 + √2) ile çarp.'],
 bilgi=[ESL],
 ad=[A('Eşlenikle genişlet','Payda √5 − √2 ise eşleniği √5 + √2’dir; pay ve payda aynı ifadeyle çarpılır.','6/(√5 − √2) = 6(√5 + √2)/((√5 − √2)(√5 + √2))'),A('Paydayı hesapla','(a − b)(a + b) = a² − b².','(√5)² − (√2)² = 5 − 2 = 3'),A('Sadeleştir','6 ile 3 sadeleşir.','6(√5 + √2)/3 = 2(√5 + √2) = 2√5 + 2√2')],
 puf='Paydada √a − √b varsa eşlenik √a + √b ile genişlet; payda a − b olur ve tam sayıya dönüşür.')

# ---------- 05 · orta · √(a²) ----------
import random
rnd=random.Random(5)
Sm=[(Fr(-rnd.randint(1,30),rnd.randint(1,5)),Fr(rnd.randint(1,30),rnd.randint(1,5))) for _ in range(40)]
ab=abs
F5={'−2a':lambda a,b:-2*a,'−2b':lambda a,b:-2*b,'0':lambda a,b:0*a,'2a − 2b':lambda a,b:2*a-2*b,'2b − 2a':lambda a,b:2*b-2*a}
dogruf=lambda a,b:ab(a)-ab(b)+ab(a-b)                 # √(a²) = |a|, √(b²) = |b|
e0=lambda a,b:a-b+(b-a)                               # √(a²) = a
eb=lambda a,b:-a-b+(a-b)                              # |a − b| = a − b
e2=lambda a,b:a-b+(a-b)                               # ikisi de
e3=lambda a,b:-a+b+(b-a)                              # √(b²) = −b
for a,b in Sm:
    assert a<0<b and dogruf(a,b)==F5['−2a'](a,b) and e0(a,b)==0 and eb(a,b)==F5['−2b'](a,b) and e2(a,b)==F5['2a − 2b'](a,b) and e3(a,b)==F5['2b − 2a'](a,b)
assert all(len({F5[k](a,b) for k in F5})==5 for a,b in Sm[:10])
mk(P,'0005',tipId='kkb-mutlak',tip='Kök içindeki kare ve mutlak değer',z='orta',alt='Kök İçinde Kare',kaz='Kök içindeki kareyi mutlak değerle açıp işaret bilgisine göre mutlak değerleri kaldırarak ifadeyi sadeleştirir.',kalip='düz',adim=3,
 kart='K-KKLB-05 (√(a²) = |a| ve işaret koşulu) · a < 0 < b için √(a²) − √(b²) + |a − b|',
 metin='a < 0 < b olmak üzere\n√(a²) − √(b²) + |a − b|\nifadesinin en sade biçimi aşağıdakilerden hangisidir?',
 dogru='−2a',sira=['−2a','−2b','0','2a − 2b','2b − 2a'],
 yan=[('−2b','|a − b|’yi a − b olarak açmış; a < b olduğundan a − b negatiftir, |a − b| = b − a.','dikkat'),('0','√(a²) = a yazmış; a negatif olduğu için √(a²) = |a| = −a’dır.','bilgi'),('2a − 2b','√(a²) = a ve |a − b| = a − b yazmış; iki hata birlikte.','bilgi'),('2b − 2a','√(b²)’yi −b almış; b pozitif olduğundan √(b²) = b’dir.','dikkat')],
 istenen='İfadenin en sade biçimi.',
 ip=['√(a²) = |a| ve a < 0 < b koşulundan |a|, |b| ve |a − b| işaretlerini ayrı ayrı belirle.'],
 bilgi=[MUT],
 ad=[A('Kök ve mutlak değerleri aç','a < 0 olduğundan |a| = −a; b > 0 olduğundan |b| = b; a − b negatif olduğundan |a − b| = −(a − b) = b − a.','√(a²) = |a| = −a · √(b²) = b · |a − b| = b − a'),A('Yerine yaz','Terimlerin işaretlerine dikkat et.','(−a) − b + (b − a)'),A('Sadeleştir','b terimleri birbirini götürür.','−a − b + b − a = −2a')],
 puf='Karekök içinde kare gördüğünde mutlak değere dön; işareti verilen değişkenle mutlak değerleri tek tek aç, çıkarmadan sonra parantezdeki işareti dikkatle dağıt.')

# ---------- 06 · orta · ardışık tam sayı ----------
x6=sq(7)+sq(11); assert 5<x6<6 and 7<2*sq(77)<18 and 49<308<324     # (√7+√11)² = 18 + 2√77, 7 < 2√77 < 18
assert 4<sq(18)<5 and 8<sq(77)<9 and 2<sq(7)<3 and 3<sq(11)<4 and 0<sq(11)-sq(7)<1 and 3+4==7 and 5<x6
mk(P,'0006',tipId='kkb-siralama',tip='Köklü sayıların tahmini ve ardışık tam sayılar',z='zor',alt='Tahmin ve Sıralama',kaz='İki karekökün toplamının hangi ardışık iki tam sayı arasında olduğunu tam karelerle sınırlayarak bulur.',kalip='düz',adim=4,
 kart='K-KKLB-06 (ardışık tam sayılar arasında) · √7 + √11',
 metin='√7 + √11 sayısı aşağıdaki ardışık tam sayı çiftlerinden hangisinin arasındadır?',
 dogru='5 ile 6',sira=['0 ile 1','3 ile 4','4 ile 5','5 ile 6','6 ile 7'],
 yan=[('0 ile 1','Toplama yerine fark almış: √11 − √7 yaklaşık 0,67.','dikkat'),('6 ile 7','√7 ≈ 3 ve √11 ≈ 4 diye üste yuvarlayıp 3 + 4 = 7 bulmuş ve 7’nin altındaki aralığı seçmiş.','islem'),('3 ile 4','Yalnız √11’i (3 ile 4 arası) hesaba katmış, √7’yi yok saymış.','dikkat'),('4 ile 5','Kök içlerini toplayıp √18 yazmış (4 ile 5 arası); √7 + √11 ≠ √18.','bilgi')],
 istenen='Sayının bulunduğu ardışık iki tam sayı.',
 ip=['Her kökü ardışık iki tam sayı arasına sıkıştır; sınırlar iki aralığa yayılıyorsa toplamın karesini alıp tam karelerle sınırla.'],
 bilgi=[TAHMIN],
 ad=[A('Kökleri sınırla','4 < 7 < 9 ve 9 < 11 < 16 olduğundan √7 ve √11 için alt ve üst sınırlar bulunur.','2 < √7 < 3 · 3 < √11 < 4'),A('Toplamı sınırla','Alt sınırlar ve üst sınırlar ayrı ayrı toplanır; aralık 5 ile 7 arasında kalır, iki ardışık tam sayıya sığmaz.','5 < √7 + √11 < 7'),A('Karesini al','Toplamın karesi 18 + 2√77 olur; √77 < 9 olduğundan kare 36’dan küçüktür, yani toplam 6’dan küçüktür.','(√7 + √11)² = 18 + 2√77'),A('Aralığı daralt','2√77 < 18 olduğundan kare 36’dan küçüktür; kare 25’ten büyük olduğundan toplam 5’ten büyüktür.','18 + 2√77 < 36 ⇒ 5 < √7 + √11 < 6')],
 puf='İki karekökün toplamı iki ardışık tam sayı aralığına sığmıyorsa karesini alıp hangi tam karelerin arasında kaldığına bak.')

# ---------- 07 · orta · iç içe, içten dışa ----------
d7=sq(5+sq(7+sq(81))); assert yak(d7,Dc(3)) and isqrt(81)==9 and isqrt(16)==4 and 5+4==9
vv={'3':Dc(3),'√13':sq(13),'4':Dc(4),'9':Dc(9),'13':Dc(13)}
assert yak(sq(7+sq(81)),Dc(4)) and yak(5+8,Dc(13)) and yak(sq(5+8),sq(13))
mk(P,'0007',tipId='kkb-ic',tip='İç içe kökler',z='kolay',alt='İç İçe Kökler',kaz='İç içe karekökleri içten dışa doğru hesaplayarak ifadenin değerini bulur.',kalip='düz',adim=2,
 kart='K-KKLB-07 (iç içe kökler) · √(5 + √(7 + √81))',
 metin='√(5 + √(7 + √81))\nifadesinin değeri kaçtır?',
 dogru='3',sira=srt(list(vv.items())),
 yan=[('4','En dıştaki 5’i işleme katmayıp yalnız √(7 + √81) = 4 hesaplamış.','dikkat'),('9','Dıştaki kökü almayı unutmuş: 5 + 4 = 9.','dikkat'),('13','√16’yı 8 almış (kökü yarıya bölmüş), 5 + 8 = 13 bulup dıştaki kökü almamış.','bilgi'),('√13','√16’yı 8 almış (kökü yarıya bölmüş) ve 5 + 8 = 13’ün kökünü almış; √16 = 4’tür.','bilgi')],
 istenen='İfadenin değeri.',
 ip=['En içteki kökten başla: önce √81, sonra bir dıştaki kök içini topla.'],
 bilgi=[IC],
 ad=[A('En içten başla','√81 = 9.','√(5 + √(7 + 9))'),A('Bir dıştaki kök','7 + 9 = 16 ve √16 = 4.','√(5 + 4)'),A('Son kök','5 + 4 = 9 ve √9 = 3.','√9 = 3')],
 puf='İç içe köklerde içten dışa doğru ilerle; her adımda kök içindeki sayının tam kare olup olmadığını kontrol et.')

# ---------- 08 · orta · köklü denklem ----------
sol=[x for x in range(-400,401) if x+1>=0 and x+13>=0 and 4*(x+1)==x+13]; assert sol==[3] and 2*isqrt(4)==isqrt(16)
assert [x for x in range(-400,401) if 2*(x+1)==x+13]==[11] and [x for x in range(-400,401) if 4*x+1==x+13]==[4]
assert Fr(9,5)==Fr(9,5) and 4*Fr(9,5)+4+Fr(9,5)==13 and 9-3==6 and [x for x in range(-400,401) if 3*x==9]==[3]
mk(P,'0008',tipId='kkb-denklem',tip='Basit köklü denklem',z='orta',alt='Köklü Denklem',kaz='Köklü bir denklemin iki tarafının karesini alarak kök içlerini eşitleyip bilinmeyeni bulur.',kalip='düz',adim=3,
 kart='K-KKLB-08 (basit köklü denklem) · 2√(x + 1) = √(x + 13)',
 metin='x gerçek sayı olmak üzere\n2√(x + 1) = √(x + 13)\neşitliğini sağlayan x değeri kaçtır?',
 dogru=3,yan=[(Fr(9,5),'4(x + 1) = x + 13 eşitliğinde 4x + 4 + x = 13 yazmış (x’i yanlış tarafa işaret değiştirmeden taşımış): x = 9/5.','islem'),(4,'2’nin karesini parantezle çarpmayıp 4x + 1 = x + 13 yazmış; 4(x + 1) = 4x + 4 olmalı.','islem'),(6,'3x = 9 bulduktan sonra x = 9 − 3 = 6 yazmış; 3 çarpandır, bölünmelidir.','islem'),(11,'Katsayı 2’nin karesini almayıp 2(x + 1) = x + 13 yazmış: x = 11.','bilgi')],
 istenen='x’in değeri.',
 ip=['İki tarafın karesini al; katsayı 2’nin de karesi (4) alınır.'],
 bilgi=[DEN],
 ad=[A('Karesini al','Sol taraftaki 2 katsayısı da kareye girer.','(2√(x + 1))² = (√(x + 13))² ⇒ 4(x + 1) = x + 13'),A('Denklemi çöz','Parantezi aç, x’leri bir tarafa topla.','4x + 4 = x + 13 ⇒ 3x = 9 ⇒ x = 3'),A('Kontrol et','Kök içleri negatif olmamalı.','2√4 = 4 ve √16 = 4 ✓')],
 puf='Köklü denklemde karesini alırken kökün önündeki katsayının da karesini al; sonunda kök içlerinin negatif olmadığını kontrol et.')

# ---------- 09 · orta · direk sayısı ----------
a9=sq(180); assert yak(a9,6*sq(5)) and yak(4*a9,24*sq(5)) and yak(4*a9/(3*sq(5)),Dc(8))
e2=6*sq(5)/(3*sq(5)); e4=2*6*sq(5)/(3*sq(5)); e48=4*36*sq(5)/(3*sq(5)); assert yak(e2,Dc(2)) and yak(e4,Dc(4)) and yak(e48,Dc(48)) and 36*36*5!=180
mk(P,'0009',tipId='kkb-baglam',tip='Kare ve dikdörtgen bağlamında köklü işlemler',z='orta',alt='Kare ve Çevre',kaz='Alanı verilen karenin kenarını kök dışına çıkararak bulur ve çevre boyunca eşit aralıklı direk sayısını hesaplar.',kalip='hikâyeli',adim=3,
 kart='K-KKLB-09 (kare alanı → kenar, çevre) · alan 180 m², aralık 3√5 m',
 metin='Alanı 180 m² olan kare biçimli bir tarlanın çevresine, bir köşeden başlanarak ardışık iki direk arası 3√5 metre olacak biçimde direkler dikiliyor. Çevre boyunca bir tam tur tamamlanıp başlangıç noktasına dönülüyor ve başlangıçtaki direk bir kez sayılıyor.\nBuna göre kaç direk dikilmiştir?',
 dogru=8,yan=[(2,'Yalnız bir kenarı düşünmüş: 6√5 ÷ 3√5 = 2; çevre dört kenarın toplamıdır.','dikkat'),(4,'Çevreyi 2 × kenar almış: 12√5 ÷ 3√5 = 4; kare çevresi 4 × kenardır.','bilgi'),(9,'8 aralık bulup bir direk daha eklemiş; kapalı çevrede son direk başlangıçtaki direktir, direk sayısı aralık sayısına eşittir.','dikkat'),(48,'√180’i 36√5 yazmış (36’yı kökten çıkarırken karekökünü almamış); doğrusu 6√5.','bilgi')],
 istenen='Dikilen toplam direk sayısı.',
 ip=['Önce karenin kenarını √180 = 6√5 olarak bul, sonra çevreyi aralığa böl.'],
 bilgi=[ALAN,KOK],
 ad=[A('Kenarı bul','Alan 180 ise kenar √180; kök içindeki 36 tam kare çarpanı dışarı çıkar.','√180 = √(36 × 5) = 6√5 m'),A('Çevreyi hesapla','Kare çevresi 4 × kenar.','4 × 6√5 = 24√5 m'),A('Direk sayısını bul','Çevre aralık uzunluğuna bölünür; kapalı çevrede aralık sayısı direk sayısına eşittir.','24√5 ÷ 3√5 = 8 direk')],
 puf='Kapalı bir çevrede (tur biçiminde) eşit aralıklı noktaların sayısı aralık sayısına eşittir; açık bir yolda ise bir fazladır.')

# ---------- 10 · orta · öncüllü ----------
I10=yak(sq(18)+sq(8),sq(50))
assert yak(sq(Dc('0.16')),Dc('0.4')) and not yak(sq(Dc('0.16')),Dc('0.04'))
III10=yak((sq(7)-2)*(sq(7)+2),Dc(5)); assert I10 and (not III10) and yak((sq(7)-2)*(sq(7)+2),Dc(3)) and (not yak(sq(18)+sq(8),sq(26)))
mk(P,'0010',tipId='kkb-oncul',tip='Köklü ifadelerde öncüllü sorular',z='orta',alt='Köklü İfadeler',kaz='Köklü eşitlikleri kök dışına çıkarma, ondalık kök ve eşlenik çarpımıyla değerlendirerek doğru olanları belirler.',kalip='öncüllü',adim=3,
 kart='K-KKLB-10 (köklü öncüllü sorular) · √18 + √8, √0,16, (√7 − 2)(√7 + 2)',
 metin='I. √18 + √8 = √50\nII. √0,16 = 0,04\nIII. (√7 − 2)(√7 + 2) = 5\nifadelerinden hangileri doğrudur?',
 dogru='Yalnız I',sira=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III'],
 yan=[('Yalnız II','I’de √18 + √8 = √26 sanıp II’de √0,16 = 0,04 almış; III’ü de yanlış bulmuş.','bilgi'),('Yalnız III','I’de kök içlerini toplayıp √26 bulmuş; III’te (√7 − 2)(√7 + 2) = 7 − 2 = 5 yazmış.','bilgi'),('I ve II','II’de √0,16 = 0,04 yazmış; kök alınınca virgülden sonraki basamak sayısı yarıya iner, √0,16 = 0,4.','bilgi'),('I ve III','III’te (√7 − 2)(√7 + 2) için 7 − 2 = 5 yazmış; doğrusu 7 − 4 = 3’tür (2² = 4).','islem')],
 istenen='Doğru olan ifadeler.',
 ip=['Her eşitliği ayrı ayrı hesapla: kök dışına çıkar, ondalığı kesre çevir, çarpımı a² − b² ile aç.'],
 bilgi=[KOK,ONDALIK,ESL],
 ad=[A('I’i incele','Kök dışına çıkarıp toplamayı karşılaştır.','√18 = 3√2 · √8 = 2√2 · 3√2 + 2√2 = 5√2 = √50 · I doğru'),A('II’yi incele','Ondalığı 100’lü kesre çevir.','√0,16 = √(16/100) = 4/10 = 0,4 ≠ 0,04 · II yanlış'),A('III’ü incele','(a − b)(a + b) = a² − b².','(√7)² − 2² = 7 − 4 = 3 ≠ 5 · III yanlış'),A('Sonuç','Yalnız I doğrudur.','Yalnız I')],
 puf='Öncüllerde her eşitliği ayrı hesapla; kök içlerini toplayarak ya da (a − b)(a + b) = a − b yazarak yapılan işlemler tipik tuzaklardır.')

# ---------- 11 · zor · x = √7 + √3, y = √7 − √3 ----------
X=sq(7)+sq(3); Y=sq(7)-sq(3)
assert yak(X*Y,Dc(4)) and yak(X*X+Y*Y,Dc(20)) and yak(X/Y+Y/X,Dc(5)) and yak((X+Y)**2,Dc(28)) and yak((X-Y)**2,Dc(12))
assert 20/Fr(2)==10 and Fr(28,4)==7 and Fr(12,4)==3 and Fr(20,10)==2
mk(P,'0011',tipId='kkb-ozdeslik',tip='Köklü ifadelerde özdeşlik ve işlem',z='zor',alt='Eşlenik Değerler',kaz='İki köklü sayının kareleri toplamını ve çarpımını özdeşliklerle bulup oranlarını hesaplar.',kalip='düz',adim=4,
 kart='K-KKLB-11 (eşlenik değerlerle simetrik ifade) · x = √7 + √3, y = √7 − √3, x/y + y/x',
 metin='x = √7 + √3\ny = √7 − √3\nolduğuna göre x/y + y/x ifadesinin değeri kaçtır?',
 dogru=5,yan=[(10,'x × y = √(7 − 3) = 2 yazmış (kök içlerini çıkarmış); (√7 + √3)(√7 − √3) = 7 − 3 = 4’tür.','bilgi'),(3,'x² + y² yerine (x − y)² = 12 almış (2xy terimini unutmuş): 12 ÷ 4 = 3.','bilgi'),(7,'x² + y² yerine (x + y)² = 28 almış (iki çarpım terimi fazladan eklenmiş): 28 ÷ 4 = 7.','bilgi'),(2,'x × y yerine x + y’nin kök içlerini toplayıp 10 almış: 20 ÷ 10 = 2.','dikkat')],
 istenen='x/y + y/x ifadesinin değeri.',
 ip=['x/y + y/x = (x² + y²)/(x × y); pay ve paydayı ayrı hesapla.'],
 bilgi=[ESL,B('Özdeşlik','(a + b)² = a² + 2ab + b² ve (a − b)² = a² − 2ab + b². Örnek: (√3 + 1)² + (√3 − 1)² = 2 × (3 + 1) = 8')],
 ad=[A('Kesirleri birleştir','Ortak payda x × y olur.','x/y + y/x = (x² + y²)/(x × y)'),A('x × y’yi bul','(a + b)(a − b) = a² − b².','x × y = 7 − 3 = 4'),A('x² + y²’yi bul','Çarpım terimleri birbirini götürür.','(√7 + √3)² + (√7 − √3)² = 2 × (7 + 3) = 20'),A('Oranı hesapla','Payı paydaya böl.','20 ÷ 4 = 5')],
 puf='x² + y² gibi toplamlarda çapraz terimler (±2xy) birbirini götürür: (a + b)² + (a − b)² = 2(a² + b²).')

# ---------- 12 · orta · iki kesrin toplamı (eşlenik) ----------
a12=1/(sq(3)-sq(2)); b12=1/(sq(3)+sq(2)); assert yak(a12,sq(3)+sq(2)) and yak(b12,sq(3)-sq(2)) and yak(a12+b12,2*sq(3)) and 3-2==1
assert yak((sq(3)+sq(2))+(sq(2)-sq(3)),2*sq(2)) and yak(a12*b12,Dc(1)) and yak(Dc(1)+Dc(1),Dc(2)) and yak(2*sq(3)/2,sq(3))
v12={'1':Dc(1),'√3':sq(3),'2':Dc(2),'2√2':2*sq(2),'2√3':2*sq(3)}
mk(P,'0012',tipId='kkb-eslenik',tip='Paydayı rasyonel yapma ve eşlenik',z='orta',alt='Eşlenik ve Toplam',kaz='İki kesrin paydalarını eşlenikle rasyonel yapıp toplamı bulur.',kalip='düz',adim=3,
 kart='K-KKLB-12 (eşlenikle iki kesrin toplamı) · 1/(√3 − √2) + 1/(√3 + √2)',
 metin='1/(√3 − √2) + 1/(√3 + √2)\ntoplamı kaçtır?',
 dogru='2√3',sira=srt(list(v12.items())),
 yan=[('1','Kesirleri √3 + √2 ve √3 − √2 bulup toplamak yerine çarpmış: (√3 + √2)(√3 − √2) = 1.','dikkat'),('√3','Toplam 2√3 olduğu halde katsayı 2’yi unutmuş.','dikkat'),('2','Paydaları 3 − 2 = 1 bulup pay (√3 ± √2) ile genişletmeden 1 + 1 = 2 toplamış.','dikkat'),('2√2','İkinci kesirde eşlenik işaretini yanlış alıp (√2 − √3) bulmuş: (√3 + √2) + (√2 − √3) = 2√2.','islem')],
 istenen='Toplamın değeri.',
 ip=['Her kesri paydasının eşleniğiyle genişlet; payda 1 olacak.'],
 bilgi=[ESL],
 ad=[A('Birinci kesri düzenle','Eşlenik √3 + √2; payda 3 − 2 = 1.','1/(√3 − √2) = (√3 + √2)/(3 − 2) = √3 + √2'),A('İkinci kesri düzenle','Eşlenik √3 − √2; payda yine 1.','1/(√3 + √2) = (√3 − √2)/(3 − 2) = √3 − √2'),A('Topla','√2’li terimler birbirini götürür.','(√3 + √2) + (√3 − √2) = 2√3')],
 puf='Eşlenik paydalı iki kesrin toplamında √2’li terimler götürülür; payda 1 olduğu için her kesir doğrudan sadeleşir.')

# ---------- 13 · zor · tanımlı: çıkarılabilir sayı ----------
def sade(b): return all(b%(d*d) for d in range(2,isqrt(b)+1))
def cik(n): return any(n%(a*a)==0 and (n//(a*a))>=2 and sade(n//(a*a)) for a in range(2,isqrt(n)+1))
L13=[n for n in range(1,51) if cik(n)]; assert L13==[8,12,18,20,24,27,28,32,40,44,45,48,50] and len(L13)==13
assert not cik(10) and not cik(16) and cik(12)
c19=sum(1 for n in range(1,51) if any(n%(a*a)==0 for a in range(2,8))); c12=sum(1 for n in range(1,51) if n%4==0); c9=sum(1 for n in L13 if n%4==0)
kareler=[n for n in range(2,51) if isqrt(n)**2==n]
assert c19==19 and c12==12 and c9==len([n for n in L13 if n%4==0])+0 and len(kareler)==6 and c9==9
mk(P,'0013',tipId='kkb-tanimli',tip='Tanımlı kök dışına çıkarılabilir sayıları sayma',z='zor',alt='Tanımlı Kavram',kaz='Tanımlanan “çıkarılabilir sayı” kavramını kare çarpanı olan ve tam kare olmayan sayılar olarak yorumlayıp 1’den 50’ye kadar sayar.',kalip='yeni nesil',adim=4,
 kart='K-KKLB-13 (tanımlı kavram: çıkarılabilir sayı) · 1’den 50’ye kaç tane',
 metin='a ve b, 2 ya da daha büyük tam sayılar ve b, 1’den büyük hiçbir tam sayının karesine bölünemeyen bir sayı olmak üzere, √n = a√b biçiminde yazılabilen n doğal sayılarına “çıkarılabilir sayı” denir. Örneğin √12 = 2√3 olduğundan 12 çıkarılabilir sayıdır; √16 = 4 ve √10 sadeleşmediği için 16 ve 10 çıkarılabilir sayı değildir.\n1’den 50’ye kadar (1 ve 50 dahil) kaç tane çıkarılabilir sayı vardır?',
 dogru=13,yan=[(6,'Yalnız kök dışına tam sayı olarak çıkan tam kareleri (4, 9, 16, 25, 36, 49) saymış; bunlar tanıma uymaz, √n = a√b’de b ≥ 2 olmalıdır.','bilgi'),(9,'4’ün katlarından tam kareleri (4, 16, 36) çıkarmış: 12 − 3 = 9; 9 ve 25’in katlarını hesaba katmamış.','dikkat'),(12,'Yalnız 4’ün katlarını (tam kareler dahil) saymış: 12 tane.','dikkat'),(19,'Kare çarpanı olan tüm sayıları (19 tane) saymış; tam kareleri (4, 9, 16, 25, 36, 49) çıkarmayı unutmuş.','dikkat')],
 istenen='1’den 50’ye kadar çıkarılabilir sayıların adedi.',
 ip=['Önce 12 ile 16 örneğini incele: hangi sayılar çıkarılabilir, hangileri değil?'],
 bilgi=[KARE,KOK],
 ad=[A('Kare çarpanlı sayıları listele','En az bir tam kare çarpanı (4, 9, 25, 49) olan sayılar bulunur; 36 hem 4’ün hem 9’un katı olduğu için bir kez sayılır.','4’ün katları: 12 · 9’un katları: 5 · 25’in katları: 2 · 49: 1 · 36 çift sayıldı → 12 + 5 + 2 + 1 − 1 = 19'),A('Tam kareleri ayır','Tam kareler 4, 9, 16, 25, 36, 49; bunların kökü tam sayı olduğundan çıkarılabilir değildir.','19 − 6 = 13'),A('Doğrula','Kalan sayılar: 8, 12, 18, 20, 24, 27, 28, 32, 40, 44, 45, 48, 50. Her biri a√b biçimindedir.','√8 = 2√2, √12 = 2√3, √18 = 3√2, …, √50 = 5√2')],
 puf='Tanımlı kavramı önce bir örnekle yorumla (12 evet, 16 hayır); sonra sayma işleminde çakışan sayıları iki kez saymamaya ve tam kareleri ayırmaya dikkat et.')

# ---------- 14 · orta · dikdörtgen çevre/alan oranı ----------
u,v=sq(48),sq(75); assert yak(u,4*sq(3)) and yak(v,5*sq(3)) and yak(2*(u+v),18*sq(3)) and yak(u*v,Dc(60)) and yak(2*(u+v)/(u*v),3*sq(3)/10)
o={'3√3/10':3*sq(3)/10,'3√3/20':3*sq(3)/20,'6√3/41':6*sq(3)/41,'9/10':Dc(9)/10,'10√3/9':10*sq(3)/9}
assert yak((u+v)/(u*v),3*sq(3)/20) and yak(2*(u+v)/123,6*sq(3)/41) and yak(2*(u+v)/(20*sq(3)),Dc(9)/10) and yak((u*v)/(2*(u+v)),10*sq(3)/9)
mk(P,'0014',tipId='kkb-baglam',tip='Kare ve dikdörtgen bağlamında köklü işlemler',z='orta',alt='Dikdörtgen ve Çevre',kaz='Kenarları köklü verilen dikdörtgenin çevresini ve alanını kök dışına çıkararak hesaplayıp oranını sadeleştirir.',kalip='hikâyeli',adim=4,
 kart='K-KKLB-14 (dikdörtgenin çevre–alan oranı) · kenarlar √48 cm ve √75 cm',
 metin='Kenar uzunlukları √48 cm ve √75 cm olan dikdörtgen biçimli bir kartonun çevresi, alanının kaç katıdır?',
 dogru='3√3/10',sira=srt(list(o.items())),
 yan=[('3√3/20','Çevreyi 2 ile çarpmadan yalnız iki kenarın toplamı (9√3) almış: 9√3 ÷ 60.','dikkat'),('6√3/41','Alanı kök içlerini toplayarak 48 + 75 = 123 almış: 18√3 ÷ 123.','bilgi'),('9/10','Alanı 4√3 × 5√3 = 20√3 bulmuş (√3 × √3 = 3’ü unutmuş): 18√3 ÷ 20√3.','islem'),('10√3/9','Oranı ters kurmuş: alanı çevreye bölmüş (60 ÷ 18√3).','dikkat')],
 istenen='Çevrenin alana oranı.',
 ip=['Kenarları kök dışına çıkararak yaz: 48 = 16 × 3 ve 75 = 25 × 3.'],
 bilgi=[KOK,CK],
 ad=[A('Kenarları sadeleştir','Kök içlerini tam kare × kalan biçiminde yaz.','√48 = 4√3 · √75 = 5√3'),A('Çevreyi bul','Dikdörtgenin çevresi 2 × (kısa + uzun kenar).','2 × (4√3 + 5√3) = 18√3'),A('Alanı bul','Alan, iki kenarın çarpımıdır; √3 × √3 = 3.','4√3 × 5√3 = 20 × 3 = 60'),A('Oranla','Çevreyi alana böl ve sadeleştir.','18√3 ÷ 60 = 3√3/10')],
 puf='Köklü kenarlı şekillerde önce her kenarı kök dışına çıkar; çarpımda √a × √a = a olduğunu unutma.')

bitir(P,'kokluiki','mat|Köklü Sayılar')
from collections import Counter
print(Counter(q['cevap']['sik'] for q in P.ANA),Counter(q['zorluk'] for q in P.ANA))
