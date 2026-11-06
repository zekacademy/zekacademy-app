import json
from itertools import permutations,product,combinations
from fractions import Fraction as Fr
from math import factorial as F
Q=[]
TIPK={'sk-tek-cift':'Temel Kavramlar','sk-yerlestirme':'Temel Kavramlar','sk-ardisik':'Temel Kavramlar','sk-oruntu':'Temel Kavramlar','sk-faktoriyel':'Temel Kavramlar','sk-asal':'Temel Kavramlar','sk-isaret':'Temel Kavramlar','sk-basamak':'Sayı Basamakları','sk-rakam-enaz':'Sayı Basamakları','sk-kesir':'Rasyonel Sayılar'}
TIPAD={'sk-tek-cift':'Tek ve çift sayılar','sk-yerlestirme':'Kutulara yerleştirme ve işlem bulma','sk-ardisik':'Ardışık sayılar','sk-oruntu':'Örüntü ve döngü','sk-faktoriyel':'Faktöriyel','sk-asal':'Asal sayılar','sk-isaret':'İşaret inceleme ve sıralama','sk-basamak':'Basamak çözümleme','sk-rakam-enaz':'Rakamlarla en az – en çok','sk-kesir':'Kesirler ve rasyonel sayılar'}
n=[12]
def add(tip,konu,kazanim,zorluk,kalip,metin,siklar,sik,istenen,ipuclari,adimlar,puf,cel,kart,bilgi=[]):
    n[0]+=1
    Q.append(dict(id=f'tytmat-sayilar-{n[0]:04d}',ders='TYT Matematik',konu=konu,k='mat|'+TIPK[tip],kazanim=kazanim,tipId=tip,tip=TIPAD[tip],
      zorluk=zorluk,seviye='ÖSYM',kalip=kalip,adimSayisi=len(adimlar),metin=metin,sekil=None,siklar=dict(zip('ABCDE',siklar)),
      cevap=dict(sik=sik,deger=dict(zip('ABCDE',siklar))[sik]),celdiriciler=cel,istenen=istenen,bilgi=bilgi,ipuclari=ipuclari,
      adimlar=[dict(baslik=b,aciklama=a,islem=i) for b,a,i in adimlar],puf=puf,kaynakKart=kart,dogrulama=dict(yontem2=True,tarama=True)))
# ---- 13 Z1 rakam en az (zor)
v=[(a,b,c) for a,b,c in permutations(range(1,10),3) if (10*a+b)+(10*b+c)+(10*c+a)>100*a+10*b+c]
assert len(v)==7 and all(a==1 and c==9 for a,b,c in v) and min(map(sum,v))==12
assert min(100*a+10*b+c for a,b,c in v)==129
add('sk-rakam-enaz','Temel Kavramlar · Sayı Basamakları','Basamak çözümlemesiyle eşitsizlik kurar, rakamların alabileceği değerleri bulur.','zor','hikâyeli',
 'Elif’in elinde üzerinde birbirinden ve sıfırdan farklı A, B ve C rakamları yazan üç kart vardır.\nElif kartlardan ikisini yan yana koyarak iki basamaklı AB, BC ve CA sayılarını, üçünü yan yana koyarak üç basamaklı ABC sayısını oluşturuyor.\nAB, BC ve CA sayılarının toplamının ABC sayısından büyük olduğunu görüyor.\nBuna göre ABC sayısı en az kaçtır?',
 ['109','119','129','139','189'],'C','Koşulu sağlayan en küçük üç basamaklı ABC sayısı.',
 ['AB + BC + CA toplamını A, B, C cinsinden çözümle.','Eşitsizliği düzenleyince A ve C için ne söyleyebilirsin?','A ve C belli olunca B’ye kurala uyan en küçük rakamı ver.'],
 [('Toplamı çözümle','Her rakam bir kez onlar, bir kez birler basamağında: toplam **11(A + B + C)**.','AB + BC + CA = 11A + 11B + 11C'),
  ('Eşitsizliği kur','ABC = 100A + 10B + C ile karşılaştırıp düzenle.','11A + 11B + 11C > 100A + 10B + C ⇒ B + 10C > 89A'),
  ('A ve C’yi bul','B + 10C en fazla 98 olabilir; bu yüzden **A = 1** ve **C = 9** olmalı.','B + 90 > 89 ✓ (A = 2 için 178’i geçmek imkânsız)'),
  ('En küçük ABC','B; 0, 1 ve 9’dan farklı en küçük rakam: **2**.','ABC = 129')],
 'Rakamlar yer değiştirerek toplanıyorsa toplam hep 11’in katıdır; önce çözümle, sonra eşitsizliği tek harfe indir.',
 dict(A='B = 0 olamaz; kartlardaki rakamlar sıfırdan farklı.',B='B = 1 olamaz; A da 1 ve rakamlar birbirinden farklı.',D='139 koşulu sağlıyor ama B = 2 ile daha küçük sayı yazılabiliyor.',E='189 koşulu sağlıyor ama en küçük değil; B’yi en küçük uygun rakam seç.'),
 'K-SK-17 (rakamlı eşitsizlik, en az) · yeni hikâye (kartlar), yeni ifade (üç döngüsel toplam), yeni istenen (ABC en az)')
# ---- 14 Z2 kutular (zor)
S=set(range(1,10)); parts=set()
for a in combinations(S,3):
    if sum(a)!=15: continue
    for b in combinations(S-set(a),3):
        if sum(b)==15: parts.add(frozenset([a,b,tuple(sorted(S-set(a)-set(b)))]))
ok=[p for p in parts if all(not any(abs(x-y)==1 for x in t for y in t) for t in p)]
assert len(ok)==1; kutu=[t for t in list(ok)[0] if 9 in t][0]; assert sorted(kutu)==[2,4,9]
add('sk-yerlestirme','Temel Kavramlar · Temel İşlemler','Verilen koşulları sağlayan dağılımları sistemli biçimde bulur.','zor','yeni nesil',
 '1’den 9’a kadar numaralandırılmış dokuz kart, her kutuda üç kart olacak biçimde üç kutuya dağıtılmıştır.\n• Her kutudaki kartların numaraları toplamı birbirine eşittir.\n• Hiçbir kutuda numaraları ardışık olan iki kart yoktur.\nBuna göre 9 numaralı kartın bulunduğu kutudaki kartların numaraları çarpımı kaçtır?',
 ['45','72','84','96','105'],'B','9 numaralı kartın kutusundaki üç numaranın çarpımı.',
 ['Dokuz kartın toplamı kaç? Her kutunun toplamı buna göre kaç olmalı?','Toplamı 15 olan, 9’u içeren üçlüleri yaz.','Ardışık kart koşulunu her kutuda kontrol et.'],
 [('Kutu toplamını bul','1’den 9’a kadar toplam 45; üç kutu eşit olduğundan her kutu **15**.','45 ÷ 3 = 15'),
  ('9’lu kutuyu ara','9 ile toplamı 15 olan üçlüler: {1, 5, 9} ve {2, 4, 9}.','9 + 1 + 5 = 15 · 9 + 2 + 4 = 15'),
  ('{1, 5, 9}’u dene','Kalan 2, 3, 4, 6, 7, 8 ile 15’lik iki üçlü yalnızca {2, 6, 7} ve {3, 4, 8}; ikisinde de ardışık kart var.','6–7 ve 3–4 ardışık ✗'),
  ('{2, 4, 9}’u dene','Kalanlar {1, 6, 8} ve {3, 5, 7}; hiçbirinde ardışık kart yok.','2 × 4 × 9 = 72')],
 'Önce toplamdan kutu toplamını bul; sonra en büyük kartı içeren kutudan başla, seçenek az olur.',
 dict(A='{1, 5, 9} kutusunu seçmişsin; bu dağılımda kalan kutularda ardışık kartlar oluşuyor.',C='{2, 6, 7} kutusunda 6 ve 7 ardışık; ayrıca 9 bu kutuda değil.',D='{3, 4, 8} kutusunda 3 ve 4 ardışık; 9 da bu kutuda değil.',E='{3, 5, 7} geçerli bir kutu ama 9 numaralı kart onda değil.'),
 'K-SK-18 (kart-kutu eşit toplam) · yeni koşul (ardışık yasak), yeni istenen (çarpım)')
# ---- 15 Z3 örüntü (zor)
def fark(k): return sum(3**i*(1 if i%2==0 else -1) for i in range(k))
assert [k for k in range(1,15) if fark(k)==61]==[5] and sum(3**i for i in range(5))==121
add('sk-oruntu','Temel Kavramlar · Örüntüler','Katlanarak artan örüntülerde terimleri ve toplamları bulur.','zor','hikâyeli',
 'Bir duvar mozaiğinin 1. sırasında 1 kare, sonraki her sırada bir önceki sıradakinin 3 katı kadar kare vardır.\nTek numaralı sıralardaki kareler mavi, çift numaralı sıralardaki kareler beyazdır.\nMozaikteki mavi kare sayısı beyaz kare sayısından 61 fazladır.\nBuna göre mozaikte toplam kaç kare vardır?',
 ['40','61','81','121','364'],'D','Tüm sıralardaki karelerin toplamı.',
 ['Sıralardaki kare sayılarını yaz: 1, 3, 9, …','Mavi fazlası oluşması için son sıra hangi renkte olmalı?','Farkı sıra sıra hesaplayıp 61’e ulaştığın yerde dur.'],
 [('Sıraları yaz','Her sıra öncekinin 3 katı.','1, 3, 9, 27, 81, …'),
  ('Farkı biriktir','Mavi sıralar eklenir, beyazlar çıkarılır.','1 − 3 + 9 − 27 + 81 = **61**'),
  ('Sıra sayısı','Fark 61 olduğunda **5** sıra vardır (6. sıra eklenseydi fark negatif olurdu).','5 sıra'),
  ('Toplamı bul','Beş sıranın karelerini topla.','1 + 3 + 9 + 27 + 81 = 121')],
 'Alternatif toplamlarda farkı terim terim biriktirmek, formül aramaktan hızlıdır.',
 dict(A='40, dört sıranın toplamı; dört sırada beyazlar daha fazla olur.',B='61 iki renk arasındaki farktır; soru toplam kare sayısını soruyor.',C='81 yalnızca 5. sıranın kare sayısı.',E='364 altı sıranın toplamı; 6. sıra beyaz olduğundan fark negatife döner.'),
 'K-SK-13 (katlanan örüntü, iki renk farkı) · yeni hikâye (mozaik), çarpan 3, yeni istenen (toplam)')
# ---- 16 Z5 basamak (zor)
c=[(a,b,cc) for a in range(1,10) for b in range(1,10) for cc in range(1,10) if len({a,b,cc})==3 and (100*cc+10*b+a)-(100*a+10*b+cc)==594]
assert len(c)==21
add('sk-basamak','Temel Kavramlar · Sayı Basamakları','Rakamların yer değiştirmesiyle oluşan farkı çözümleyerek sayma yapar.','zor','düz',
 'Rakamları birbirinden ve sıfırdan farklı üç basamaklı ABC sayısının yüzler ve birler basamağındaki rakamların yerleri değiştirilerek CBA sayısı elde ediliyor.\nCBA sayısı, ABC sayısından 594 büyüktür.\nBuna göre kaç farklı ABC sayısı vardır?',
 ['15','18','21','24','27'],'C','Koşulu sağlayan üç basamaklı sayıların adedi.',
 ['CBA − ABC farkını çözümle; onlar basamağı ne oluyor?','Farktan C − A’yı bul ve uygun (A, C) ikililerini yaz.','B için kaç seçenek kaldığını say: B, A ve C’den farklı ve sıfırdan farklı.'],
 [('Farkı çözümle','Onlar basamakları birbirini götürür.','CBA − ABC = 99(C − A)'),
  ('C − A’yı bul','99(C − A) = 594.','C − A = 6'),
  ('İkilileri yaz','A ve C sıfırdan farklı rakamlar.','(A, C) = (1, 7), (2, 8), (3, 9)'),
  ('B’yi say','B; 0, A ve C dışındaki **7** rakamdan biri.','3 × 7 = 21')],
 'Yüzler ve birler yer değiştirince fark daima 99’un katıdır; ortadaki rakam serbest kalır ama koşullara dikkat.',
 dict(A='B için 5 seçenek saymışsın; 1–9 arasından A ve C çıkınca 7 kalır.',B='B için 6 seçenek saymışsın; 1–9 arasından yalnızca A ve C çıkar.',D='B = 0’ı da saymışsın; rakamlar sıfırdan farklı olmalı.',E='B’nin A ve C’den farklı olması gerektiğini unutmuşsun.'),
 'K-SK-20 (rakam yer değiştirme farkı) · yeni istenen (sayma), yeni fark değeri')
# ---- 17 Z4 ardışık (orta)
sol=[(d,2*d,2*d+2,d+2) for d in range(11,100,2) if 2*d<100 and 6*d+4<110]
assert max(x[2] for x in sol)==36
add('sk-ardisik','Temel Kavramlar · Ardışık Sayılar','Ardışık tek ve çift sayılarla kurulan koşullarda en büyük değeri bulur.','orta','hikâyeli',
 'Ayla, Burak, Cem ve Duru tahtaya birer tane iki basamaklı doğal sayı yazmıştır.\n• Ayla ile Burak’ın yazdığı sayılar ardışık çift sayılardır ve Burak’ınki daha büyüktür.\n• Cem ile Duru’nun yazdığı sayılar ardışık tek sayılardır ve Cem’inki daha büyüktür.\n• Ayla’nın yazdığı sayı, Duru’nun yazdığı sayının 2 katıdır.\n• Dört sayının toplamı 110’dan küçüktür.\nBuna göre Burak’ın yazdığı sayı en çok kaçtır?',
 ['36','38','40','42','44'],'A','Koşullara göre Burak’ın sayısının en büyük değeri.',
 ['Duru’nun sayısına d de; diğer üç sayıyı d ile yaz.','Dört sayının toplamını d cinsinden bul ve 110’dan küçük yap.','d’nin iki basamaklı tek sayı olduğunu unutma.'],
 [('Sayıları d ile yaz','Duru = d, Cem = d + 2, Ayla = 2d, Burak = 2d + 2.','d, d + 2, 2d, 2d + 2'),
  ('Toplamı sınırla','Toplam **6d + 4** olmalı ve 110’dan küçük.','6d + 4 < 110 ⇒ d < 17,67'),
  ('En büyük d','d iki basamaklı tek sayı: en çok **17**.','d = 17'),
  ('Burak’ı bul','Burak = 2d + 2.','2 × 17 + 2 = 36')],
 '“En çok” sorularında tüm sayıları tek harfe bağla; sınır eşitsizliği o harfin en büyük değerini verir.',
 dict(B='38 için d = 18 almışsın; d bir tek sayı olmalı.',C='40 için d = 19 almışsın; o zaman toplam 118 olur, 110’u geçer.',D='42 için d = 20 almışsın; d tek ve toplam 110’dan küçük olmalı.',E='Toplam sınırını kullanmamışsın.'),
 'K-SK-19 (ardışık çift/tek + kat ilişkisi + toplam sınırı) · yeni kişiler, yeni sınır, yeni istenen')
# ---- 18 O1 merdiven (orta)
s=[(x,y) for x in range(1,50) for y in range(1,50) if 2*x+3*y==41]
assert all(y%2 for x,y in s) and len({(x+y)%2 for x,y in s})==2 and min(x+y for x,y in s)==14
add('sk-tek-cift','Temel Kavramlar · Tek ve Çift Sayılar','Tek-çift özelliklerini kullanarak kesin doğru ifadeleri belirler.','orta','öncüllü',
 'Bir binanın merdiven basamakları 1’den başlayarak numaralandırılmıştır.\nDeniz, 5 numaralı basamaktan 46 numaralı basamağa çıkarken her adımda ya iki ya da üç basamak çıkmış; hem ikişerli hem üçerli adım atmıştır.\nBuna göre\nI. Deniz’in attığı üçerli adımların sayısı tektir.\nII. Deniz’in attığı toplam adım sayısı çifttir.\nIII. Deniz en az 14 adım atmıştır.\nifadelerinden hangileri kesinlikle doğrudur?',
 ['Yalnız I','Yalnız III','I ve II','I ve III','I, II ve III'],'D','Tüm olası adım dağılımlarında doğru kalan ifadeler.',
 ['Deniz toplam kaç basamak çıktı?','İkişerli adım sayısına x, üçerli adım sayısına y de; 2x + 3y kaça eşit?','Olası (x, y) ikililerini yazıp her ifadeyi dene.'],
 [('Mesafeyi bul','5’ten 46’ya çıkılan basamak sayısı.','46 − 5 = 41'),
  ('Denklemi kur','2x + 3y = 41; 41 tek olduğu için **3y tek**, yani **y tek**.','2x + 3y = 41'),
  ('Olasılıkları yaz','y = 1, 3, …, 13 için toplam adım x + y: 20, 19, 18, 17, 16, 15, 14.','x + y ∈ {14, …, 20}'),
  ('İfadeleri dene','I her zaman doğru; II bazen yanlış (ör. 19); III doğru (en az 14).','Doğrular: I ve III')],
 '“Kesinlikle” sorularında tüm durumları listele; tek bir karşı örnek ifadeyi düşürür.',
 dict(A='III de her durumda doğru: toplam adım en az 14.',B='I de her durumda doğru: 41 tek olduğu için üçerli adım sayısı tektir.',C='II kesin değil: x = 4, y = 11 için toplam 15 adımdır.',E='II kesin değil; toplam adım sayısı tek de olabilir.'),
 'K-SK-14 (iki adım boyu, parite) · yeni başlangıç basamağı, yeni mesafe, yeni öncüller')
# ---- 19 O2 asal (orta)
P=[p for p in range(2,30) if all(p%d for d in range(2,int(p**.5)+1))]
s=[(x,y,z) for x in P for y in P for z in P if x<y and x*y+z==23]
assert sorted(map(sum,s))==[12,20,22]
add('sk-asal','Temel Kavramlar · Asal Sayılar','Asal sayıların tek-çift özelliğini kullanarak denklem çözer.','orta','düz',
 'x, y ve z asal sayılar ve x < y olmak üzere\nx · y + z = 23\nolduğuna göre x + y + z toplamı en az kaçtır?',
 ['12','18','20','22','24'],'A','Denklemi sağlayan asal üçlüler arasında en küçük toplam.',
 ['23 tek; x · y ile z’den biri çift olmalı.','Çift olan tek asal sayı hangisi?','Her durumu ayrı ayrı yazıp toplamları karşılaştır.'],
 [('Tek-çift durumu','23 tek olduğundan x · y ve z’den **biri çift**; çift asal yalnızca **2**.','çift + tek = tek'),
  ('z = 2 durumu','x · y = 21 ⇒ x = 3, y = 7.','3 + 7 + 2 = 12'),
  ('x = 2 durumu','2y + z = 23: y = 3 ⇒ z = 17; y = 5 ⇒ z = 13.','2 + 3 + 17 = 22 · 2 + 5 + 13 = 20'),
  ('En küçüğü seç','Toplamlar 12, 20, 22.','en az 12')],
 'Asal sayılı denklemlerde önce tek-çift dengesine bak: toplam tekse içlerinden biri mutlaka 2’dir.',
 dict(B='18 veren bir asal üçlü yok; durumları yeniden yaz.',C='20, x = 2, y = 5 durumu; z = 2 durumu daha küçük toplam verir.',D='22, x = 2, y = 3 durumu; daha küçük toplam var.',E='24 veren bir asal üçlü yok.'),
 'K-SK-27 (asal denklem, parite ile 2) · yeni denklem, yeni istenen (en az toplam)')
# ---- 20 O3 faktöriyel (orta)
ns=[k for k in range(1,15) if F(k+1)-F(k)==25*F(k-1)]; assert ns==[5] and F(6)==720
add('sk-faktoriyel','Temel Kavramlar · Faktöriyel','Faktöriyelli ifadeleri ortak çarpan parantezine alarak sadeleştirir.','orta','düz',
 'n bir pozitif tam sayı olmak üzere\n(n + 1)! − n! = 25 · (n − 1)!\nolduğuna göre (n + 1)! kaçtır?',
 ['6','24','120','240','720'],'E','Denklemi sağlayan n için (n + 1)! değeri.',
 ['(n + 1)! ifadesini n! cinsinden yaz.','Sol tarafı n! parantezine al.','n!’i de (n − 1)! cinsinden yazıp sadeleştir.'],
 [('n! parantezine al','(n + 1)! = (n + 1) · n! olduğundan sol taraf **n · n!** olur.','(n + 1)! − n! = n! (n + 1 − 1) = n · n!'),
  ('Sadeleştir','n! = n · (n − 1)! yaz ve iki taraftan (n − 1)! sadeleştir.','n · n · (n − 1)! = 25 · (n − 1)! ⇒ n² = 25'),
  ('Sonucu bul','n pozitif olduğundan **n = 5**; soru (n + 1)!’i soruyor.','6! = 720')],
 'Faktöriyel farklarında en küçük faktöriyeli parantez dışına al; sonra soruda hangi faktöriyelin istendiğine tekrar bak.',
 dict(A='6, n + 1 = 6’nın kendisi; soru 6!’i soruyor.',B='24, (n − 1)! = 4!’tür.',C='120, n! = 5!’tir; soru (n + 1)!’i soruyor.',D='240, 2 · 5!; faktöriyeli yanlış açmışsın.'),
 'K-SK-26 (faktöriyel sadeleştirme) · yeni denklem, ters soru (n’den faktöriyele)')
# ---- 21 O4 işaret (kolay)
ok=set()
for a,b,c in product([-3,-1,1,2,5],repeat=3):
    if a*b<0 and b*c>0 and a>c: ok.add((a>0,b>0,c>0))
assert ok=={(True,False,False)}
add('sk-isaret','Temel Kavramlar · İşaret İnceleme','Çarpım ve sıralama bilgisinden sayıların işaretlerini bulur.','kolay','düz',
 'a, b ve c sıfırdan farklı gerçel sayılardır.\na · b < 0\nb · c > 0\na > c\nolduğuna göre aşağıdakilerden hangisi kesinlikle pozitiftir?',
 ['a · c','b + c','a · b · c','a + b','c − b'],'C','İşaretleri belli olan a, b, c ile kesin pozitif ifade.',
 ['b · c > 0 ise b ile c’nin işaretleri hakkında ne söylenir?','a · b < 0 ise a, b’nin tersi işaretli.','a > c bilgisiyle hangi işaret durumunun mümkün olduğunu bul.'],
 [('b ve c aynı işaretli','b · c > 0 olduğundan **b ve c aynı işaretli**; a · b < 0 olduğundan **a ters işaretli**.','b, c aynı · a ters'),
  ('Durumu seç','a negatif olsaydı c pozitif olurdu ve a > c sağlanmazdı. O hâlde **a > 0, b < 0, c < 0**.','a > 0, b < 0, c < 0'),
  ('Şıkları dene','a · b · c = (+)(−)(−) pozitif; diğerleri ya negatif ya belirsiz.','a × b × c > 0')],
 'İki çarpım bilgisi işaret gruplarını verir; sıralama bilgisi hangi grubun pozitif olduğunu seçer.',
 dict(A='a pozitif, c negatif: a · c negatiftir.',B='b ve c ikisi de negatif: toplamları negatiftir.',D='a pozitif, b negatif: a + b’nin işareti sayılara bağlıdır.',E='c ve b ikisi de negatif: c − b’nin işareti sayılara bağlıdır.'),
 'K-SK-28 (işaret inceleme) · yeni koşul seti, kesin pozitif ifade')
# ---- 22 O5 rakam en çok (orta)
best=[]
for p in permutations([2,0,5,7,9]):
    if p[0] and p[3]: best.append(100*p[0]+10*p[1]+p[2]-(10*p[3]+p[4]))
assert max(best)==955
add('sk-rakam-enaz','Temel Kavramlar · Sayı Basamakları','Verilen rakamlarla yazılan sayıların farkını en büyük yapar.','orta','düz',
 '0, 2, 5, 7 ve 9 rakamlarının her biri yalnızca bir kez kullanılarak üç basamaklı bir A sayısı ile iki basamaklı bir B sayısı yazılıyor.\nBuna göre A − B farkı en çok kaçtır?',
 ['925','935','945','955','973'],'D','A − B’nin alabileceği en büyük değer.',
 ['Fark büyük olsun diye A nasıl, B nasıl olmalı?','A’ya en büyük rakamları sırayla yerleştir.','B’nin onlar basamağına 0 yazılamayacağını unutma.'],
 [('A’yı büyüt','A’nın yüzler ve onlar basamağına en büyük rakamlar: 9 ve 7.','A = 97_'),
  ('B’yi küçült','B’nin onlar basamağı 0 olamaz; kalan 0, 2, 5 ile en küçük B = **20**.','B = 20'),
  ('Farkı hesapla','A’nın birler basamağına kalan rakam: 5.','975 − 20 = 955')],
 'Fark sorularında büyük sayıyı en büyük, küçük sayıyı en küçük yap; sıfırın başa gelemeyeceğini kontrol et.',
 dict(A='B’yi gereğinden büyük almışsın; en küçük B = 20.',B='A’nın birler basamağına kalan en büyük rakamı yazmamışsın.',C='A = 975 olmalı; birler basamağını küçük seçmişsin.',E='B = 02 almışsın; iki basamaklı sayı 0 ile başlayamaz.'),
 'K-SK-22 (rakam kümesiyle sayı yazma, fark en büyük) · yeni rakam kümesi, istenen yalnızca en büyük fark')
# ---- 23 O6 otopark (orta)
toplam=36; dolu=toplam*Fr(4,9); assert dolu==16; alt_dolu=16-7; assert 12-alt_dolu==3
add('sk-kesir','Temel Kavramlar · Rasyonel Sayılar','Kesirle verilen bütün bilgisinden görünmeyen kısım hakkında sonuç çıkarır.','orta','hikâyeli',
 '36 araçlık bir otoparkta park yerlerinin 4/9’u doludur.\nOtoparkın tamamını gören bir güvenlik kamerasının görüntüsünde, kameranın önüne park eden bir kamyon yüzünden 12 park yeri görünmemektedir. Görünen park yerlerinden 7’si doludur.\nBuna göre kamyonun kapattığı park yerlerinden kaç tanesi boştur?',
 ['1','2','3','4','5'],'C','Görünmeyen 12 yerden boş olanların sayısı.',
 ['Otoparkta toplam kaç dolu yer var?','Görünmeyen yerlerde kaç dolu yer kalıyor?','Görünmeyen yer sayısından dolu olanları çıkar.'],
 [('Dolu yerler','Toplamın 4/9’u dolu.','36 × 4/9 = 16'),
  ('Görünmeyen dolu yerler','Görünen 7 dolu yer çıkınca kalan dolu yerler kamyonun arkasındadır.','16 − 7 = 9'),
  ('Boş yerler','Kapatılan 12 yerin 9’u dolu.','12 − 9 = 3')],
 'Görünmeyen kısım sorularında önce bütündeki toplamı bul, sonra görüneni çıkar.',
 dict(A='Görünen yerlerin sayısını yanlış hesaplamışsın; görünen 36 − 12 = 24 yer var.',B='Dolu yer sayısını 4/9 yerine yanlış hesaplamışsın: 36 × 4/9 = 16.',D='Görünen dolu yerleri çıkarmayı unutmuş olabilirsin: 16 − 7 = 9 dolu kapalı yer.',E='Görünen boş yer sayısını bulmuş olabilirsin; soru kapalı alandaki boşları soruyor.'),
 'K-SK-31 (görünmeyen kısım + oran) · yeni hikâye (otopark, kamera), yeni sayılar')
# ---- 24 K1 faktöriyel (kolay)
assert F(6)//F(4)+F(3)==36
add('sk-faktoriyel','Temel Kavramlar · Faktöriyel','Faktöriyelli ifadelerin değerini hesaplar.','kolay','düz',
 '6!/4! + 3!\nişleminin sonucu kaçtır?',
 ['18','24','30','33','36'],'E','İşlemin sonucu.',
 ['6! ile 4! arasındaki ortak çarpanları düşün.','6!/4! = 6 × 5 olur.','3!’i hesaplayıp ekle.'],
 [('Bölmeyi sadeleştir','6! = 6 × 5 × 4! olduğundan 4! sadeleşir.','6!/4! = 6 × 5 = 30'),
  ('3!’i hesapla','3! = 3 × 2 × 1.','3! = 6'),
  ('Topla','İki sonucu topla.','30 + 6 = 36')],
 'Faktöriyel bölmelerinde küçük faktöriyeli büyüğün içinde gör: n! = n × (n − 1)!.',
 dict(A='18 = 3 × 3!; işlemi yanlış gruplamışsın.',B='24 = 4!; bölmeyi yapmadan payda değerini almışsın.',C='30, yalnızca 6!/4!; 3!’i eklemeyi unutmuşsun.',D='3! yerine 3 eklemişsin; 3! = 6.'),
 'K-SK-26 (faktöriyel sadeleştirme) · temel hesap')
# ---- 25 K2 asal (kolay)
s=[(a,b) for a in P for b in P if a<b and a+b==15]; assert s==[(2,13)] and 2*13==26
add('sk-asal','Temel Kavramlar · Asal Sayılar','Asal sayıların tek-çift özelliğini kullanır.','kolay','düz',
 'a ve b asal sayılar olmak üzere\na + b = 15\nolduğuna göre a · b çarpımı kaçtır?',
 ['22','26','30','36','44'],'B','a ile b’nin çarpımı.',
 ['15 tek; iki sayının toplamı tekse biri çift olmalı.','Çift olan asal sayı hangisi?','Diğer sayıyı bul ve asal olduğunu kontrol et.'],
 [('Tek-çift durumu','Toplam tek olduğundan sayılardan biri çift; çift asal yalnızca **2**.','çift + tek = tek'),
  ('Diğer sayı','Öteki sayı 15 − 2 = 13 ve 13 asaldır.','b = 13'),
  ('Çarp','İki sayıyı çarp.','2 × 13 = 26')],
 'İki asalın toplamı tekse biri mutlaka 2’dir.',
 dict(A='22 = 2 × 11; 2 + 11 = 13, 15 değil.',C='30 = 2 × 15; 15 asal değil.',D='36 = 3 × 12 ya da 4 × 9; bunlar asal değil.',E='44 = 4 × 11; 4 asal değil.'),
 'K-SK-27 (asal + parite) · kolay düzey, yeni sayılar')
# ---- 26 K3 tek-çift (kolay)
ok=set()
for k,e in product([1,3,5,7],[2,4,6]):
    ok.add(tuple(v%2 for v in (k*e,k+e,2*k+e,k*e+e,e*e)))
assert all(t[1]==1 for t in ok) and all(t[i]==0 for t in ok for i in (0,2,3,4))
add('sk-tek-cift','Temel Kavramlar · Tek ve Çift Sayılar','Tek ve çift sayıların işlem özelliklerini kullanır.','kolay','hikâyeli',
 'Bir sınıftaki kız öğrencilerin sayısı k, erkek öğrencilerin sayısı e’dir.\nk bir tek sayı, e bir çift sayı olduğuna göre aşağıdakilerden hangisi kesinlikle tek sayıdır?',
 ['k · e','k + e','2k + e','k · e + e','e²'],'B','Her zaman tek olan ifade.',
 ['Çarpanlardan biri çiftse çarpım ne olur?','Tek ile çiftin toplamı tek midir, çift mi?','Her şıkkı k = 3, e = 4 gibi bir örnekle de dene.'],
 [('Çarpımlara bak','e çift olduğundan k · e, e² ve k · e + e çifttir.','çift × tek = çift'),
  ('2k + e','2k her zaman çift; çift + çift = çift.','2k + e çift'),
  ('k + e','Tek + çift her zaman tektir.','k + e tek')],
 'Çift bir çarpan çarpımı hep çift yapar; toplamda ise tek sayıdaki terimlerin sayısına bak.',
 dict(A='e çift olduğu için k · e çifttir.',C='2k çift, e çift: toplamları çifttir.',D='k · e ve e ikisi de çift: toplamları çifttir.',E='Çift bir sayının karesi çifttir.'),
 'K-SK-02 (tek-çift) · kolay düzey, sınıf hikâyesi')
from collections import Counter
print(len(Q),Counter(q['cevap']['sik'] for q in Q),Counter(q['zorluk'] for q in Q))
json.dump(Q,open('/home/claude/zekacademy-app/havuz/tyt-mat/sayi-kumeleri-parti2.json','w'),ensure_ascii=False,indent=1)
