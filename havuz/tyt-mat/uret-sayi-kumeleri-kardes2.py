"""Kardeş sorular (parti 2): 0013k–0018k, 0020k–0023k, 0025k, 0026k. Kodla doğrulanır."""
import json,sys,os
from itertools import product,permutations,combinations
from fractions import Fraction as Fr
from math import factorial as F
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,os.path.join(H,'..'))
import gorsel as G
ANA={q['id']:q for f in ('sayi-kumeleri-parti1.json','sayi-kumeleri-parti2.json') for q in json.load(open(os.path.join(H,f)))}
B=lambda a,i:dict(ad=a,ifade=i)
TEK=B('Tek-çift kuralları','tek + tek = çift · çift + çift = çift · tek + çift = tek'); CARP=B('Çarpımda tek-çift','çarpanlardan biri çiftse çarpım çifttir; hepsi tekse çarpım tektir')
IKI=B('İki basamaklı sayı','AB = 10 × A + B (A onlar, B birler basamağı). Örnek: 74 = 10 × 7 + 4')
ASAL=B('Asal sayı','1’den büyük, yalnızca 1’e ve kendisine bölünen sayı: 2, 3, 5, 7, 11, 13, … 2, çift olan tek asal sayıdır')
FAK=B('Faktöriyel','n! = 1 × 2 × … × n. Örnek: 4! = 24. Ayrıca 7! = 7 × 6 × 5! gibi yazılabilir')
A=lambda b,a,i,g=None:{**dict(baslik=b,aciklama=a,islem=i),**({'gorsel':g} if g else {})}
OUT=[]
def K(ana,metin,siklar,sik,istenen,ipuclari,bilgi,adimlar,puf,cel,kisa=None,sekil=None):
    a=ANA['tytmat-sayilar-'+ana]
    q=dict(id=a['id']+'k',ana=a['id'],ders=a['ders'],konu=a['konu'],k=a['k'],kazanim=a['kazanim'],tipId=a['tipId'],tip=a['tip'],zorluk=a['zorluk'],
      seviye=a['seviye'],kalip=a['kalip'],adimSayisi=a['adimSayisi'],metin=metin,sekil=sekil,siklar=dict(zip('ABCDE',siklar)),cevap=dict(sik=sik,deger=dict(zip('ABCDE',siklar))[sik]),
      celdiriciler=cel,istenen=istenen,bilgi=bilgi,ipuclari=ipuclari,adimlar=adimlar,puf=puf,kisaYol=kisa,
      kaynakKart=a['kaynakKart'].split(' · ')[0]+' · kardeş ('+a['id'][-4:]+'): aynı tip ve zorluk, yeni kurgu ve sayılar',dogrulama=dict(yontem2=True,tarama=True))
    OUT.append(q)
ds=lambda n:sum(map(int,str(n)))
def dp(n):
    r=1
    for c in str(n): r*=int(c)
    return r
# ---- 0013k
v=[(a,b,c) for a,b,c in permutations(range(1,10),3) if (10*c+a)+(10*c+b)+(10*a+b)>100*a+10*b+c]
assert {a for a,b,c in v}=={1} and max(100*a+10*b+c for a,b,c in v)==189
for n in (178,186,187,198): a,b,c=map(int,str(n)); assert (a,b,c) not in v or n<189
K('0013','Deniz’in elinde üzerinde birbirinden ve sıfırdan farklı A, B ve C rakamları yazılı üç kart vardır.\nDeniz kartlarla iki basamaklı CA, CB ve AB sayılarını, üç kartı yan yana koyarak da üç basamaklı ABC sayısını oluşturduğunda CA, CB ve AB sayılarının toplamının ABC sayısından büyük olduğunu görüyor.\nBuna göre ABC sayısı en çok kaçtır?',
 ['178','186','187','189','198'],'D','Koşulu sağlayan en büyük üç basamaklı ABC sayısı.',
 ['CA + CB + AB toplamını A, B, C cinsinden çözümle.','Eşitsizliği sadeleştirince A’nın kaç olabileceğine bak.','A belli olunca C’yi, sonra B’yi en büyük seç; koşulu kontrol et.'],[IKI,B('Üç basamaklı sayı','ABC = 100 × A + 10 × B + C. Örnek: 352 = 300 + 50 + 2')],
 [A('Sayıları aç','Her sayıyı basamaklarına ayır.','CA = 10C + A · CB = 10C + B · AB = 10A + B'),
  A('Topla','A’lar, B’ler ve C’ler ayrı ayrı toplanır.','CA + CB + AB = 11A + 2B + 20C'),
  A('Eşitsizliği sadeleştir','11A + 2B + 20C > 100A + 10B + C. İki taraftan 11A, 2B ve C çıkar.','19C > 89A + 8B'),
  A('A’yı bul','Sol taraf en fazla 19 × 9 = 171. A = 2 olsaydı sağ taraf en az 178 olurdu; olmaz. O hâlde **A = 1**.','A = 1 ⇒ 19C > 89 + 8B'),
  A('En büyük ABC','ABC’yi büyütmek için önce B’yi büyük seçmek gerekir. B = 9 olursa C = 9 olamaz (farklı rakam), C = 8 ile 152 > 161 sağlanmaz. B = 8 ve C = 9 ile 171 > 153 sağlanır.','ABC = 189')],
 'Eşitsizliği tek harfe indir; “en çok” için yüksek basamaktan başlayarak en büyük rakamı dene ve koşulu kontrol et.',
 dict(A='178 koşulu sağlıyor ama B = 8, C = 9 ile daha büyük sayı yazılabiliyor.',B='186 için C = 6 iken 19 × 6 = 114, 89 + 64 = 153’ten küçük; koşul sağlanmaz.',C='187 koşulu sağlıyor ama 189 daha büyük.',E='198 için 19 × 8 = 152, 89 + 72 = 161’den küçük; koşul sağlanmaz.'))
# ---- 0014k
S=set(range(2,11)); parts=set()
for a_ in combinations(sorted(S),3):
    if sum(a_)!=18: continue
    for b_ in combinations(sorted(S-set(a_)),3):
        if sum(b_)==18: parts.add(frozenset([a_,b_,tuple(sorted(S-set(a_)-set(b_)))]))
ok=[p for p in parts if all(any(x in (2,3,5,7) for x in t) for t in p)]; assert len(ok)==1
kutu=[t for t in list(ok)[0] if 10 in t][0]; assert sorted(kutu)==[2,6,10]
K('0014','2’den 10’a kadar numaralandırılmış dokuz kart, her kutuda üç kart olacak biçimde üç kutuya dağıtılmıştır.\n• Her kutudaki kartların numaraları toplamı birbirine eşittir.\n• Her kutuda numarası asal sayı olan en az bir kart vardır.\nBuna göre 10 numaralı kartın bulunduğu kutudaki kartların numaraları çarpımı kaçtır?',
 ['120','150','168','180','192'],'A','10 numaralı kartın kutusundaki üç numaranın çarpımı.',
 ['Dokuz kartın toplamı kaç? Her kutunun toplamı kaç olmalı?','10 ile toplamı 18 olan üçlüleri yaz.','Her durumda kalan kartları da kutulara dağıt ve asal koşulunu kontrol et.'],
 [ASAL,B('2’den 10’a toplam','2 + 3 + … + 10 = 54')],
 [A('Kutu toplamı','Üç kutunun toplamı eşit; 54’ü üçe böl.','54 ÷ 3 = 18'),
  A('10’un kutusu','10 ile birlikte iki kart daha var ve toplamları 8 olmalı: (2, 6) ya da (3, 5).','{2, 6, 10} veya {3, 5, 10}'),
  A('{3, 5, 10}’u dene','Kalan 2, 4, 6, 7, 8, 9 ile toplamı 18 olan üçlüler {2, 7, 9} ve {4, 6, 8}. {4, 6, 8} kutusunda hiç asal yok.','olmaz ✗'),
  A('{2, 6, 10}’u dene','Kalan 3, 4, 5, 7, 8, 9 ile üçlüler {3, 7, 8} ve {4, 5, 9}. Her kutuda asal var (2; 3 ve 7; 5).','olur ✓',G.kutular([(2,6,10),(3,7,8),(4,5,9)],10)),
  A('Çarpımı bul','10’un kutusundaki kartlar 2, 6, 10.','2 × 6 × 10 = 120')],
 'Önce toplamdan kutu toplamını bul; sonra en büyük kartı içeren kutudan başla, seçenek az olur.',
 dict(B='150 = 3 × 5 × 10; bu dağılımda {4, 6, 8} kutusunda asal kalmıyor.',C='{3, 7, 8} geçerli bir kutu ama 10 numaralı kart onda değil.',D='{4, 5, 9} geçerli bir kutu ama 10 numaralı kart onda değil.',E='{4, 6, 8} kutusunda asal yok; ayrıca 10 bu kutuda değil.'))
# ---- 0015k
def fark(k): return sum(2*2**i*(1 if i%2==1 else -1) for i in range(k))
assert [k for k in range(1,15) if fark(k)==42]==[6] and sum(2*2**i for i in range(6))==126 and 4+16+64==84
K('0015','Bir binanın cephesinde süs lambaları vardır. 1. katta 2 lamba bulunur; sonraki her katta, bir önceki kattaki lamba sayısının iki katı kadar lamba vardır.\nTek numaralı katlardaki lambalar sarı, çift numaralı katlardaki lambalar beyazdır.\nBinadaki beyaz lamba sayısı sarı lamba sayısından 42 fazladır.\nBuna göre binada toplam kaç lamba vardır?',
 ['30','42','84','126','254'],'D','Tüm katlardaki lambaların toplamı.',
 ['Katlardaki lamba sayılarını yaz: 2, 4, 8, …','Beyaz fazlası oluşması için son kat hangi renkte olmalı?','Farkı kat kat hesaplayıp 42’ye ulaştığın yerde dur.'],
 [B('2 katına çıkma','her kat öncekinin 2 katı: 2, 4, 8, 16, 32, 64, …')],
 [A('Katları yaz','1. kattan başlayarak her katı 2 ile çarp.','2, 4, 8, 16, 32, 64, …'),
  A('Renkleri belirle','Tek numaralı katlar sarı, çift numaralı katlar beyaz.','sarı: 2, 8, 32 · beyaz: 4, 16, 64'),
  A('Farkı biriktir','Beyazları ekle, sarıları çıkar; her yeni katta farkı güncelle.','−2 → 2 → −6 → 10 → −22 → 42'),
  A('Kat sayısı','Fark 42 olduğunda **6** kat vardır.','6 kat'),
  A('Toplam lamba','Altı kattaki lambaları topla.','2 + 4 + 8 + 16 + 32 + 64 = 126')],
 'Alternatif toplamlarda farkı adım adım biriktirmek, formül aramaktan hızlıdır.',
 dict(A='30, dört katın toplamı; dört katta fark yalnızca 10.',B='42 iki renk arasındaki farktır; soru toplam lamba sayısını soruyor.',C='84 yalnızca beyaz lambaların sayısı.',E='254 yedi katın toplamı; 7. kat sarı olduğundan fark negatife döner.'))
# ---- 0016k
c=[(a,b,cc) for a in range(1,10) for b in range(1,10) for cc in range(1,10) if len({a,b,cc})==3 and (100*a+10*b+cc)-(100*cc+10*b+a)==396]; assert len(c)==35
K('0016','Rakamları birbirinden ve sıfırdan farklı üç basamaklı ABC sayısının yüzler ve birler basamağındaki rakamların yerleri değiştirilerek CBA sayısı elde ediliyor.\nABC sayısı, CBA sayısından 396 büyüktür.\nBuna göre kaç farklı ABC sayısı vardır?',
 ['30','35','40','42','45'],'B','Koşulu sağlayan üç basamaklı sayıların adedi.',
 ['ABC − CBA farkını çözümle; onlar basamağı ne oluyor?','Farktan A − C’yi bul ve uygun (A, C) ikililerini yaz.','B için kaç seçenek kaldığını say.'],[B('Üç basamaklı sayı','ABC = 100 × A + 10 × B + C. Örnek: 352 = 300 + 50 + 2')],
 [A('Sayıları aç','İki sayıyı basamaklarına ayır.','ABC = 100A + 10B + C · CBA = 100C + 10B + A'),
  A('Farkı al','ABC − CBA yapınca 10B’ler birbirini götürür.','99A − 99C = 99(A − C)'),
  A('A − C’yi bul','Fark 396 olduğuna göre 99’a böl.','396 ÷ 99 = 4 ⇒ A − C = 4'),
  A('A ve C ikilileri','C sıfırdan farklı; A, C’den 4 fazla.','(5, 1), (6, 2), (7, 3), (8, 4), (9, 5)'),
  A('B’yi say','B; 1–9 arasında, A’dan ve C’den farklı: **7** seçenek.','9 − 2 = 7'),
  A('Toplam sayı','Her ikili için 7 farklı B var.','5 × 7 = 35')],
 'Yüzler ve birler yer değiştirince fark daima 99’un katıdır; ortadaki rakam serbest kalır ama koşullara dikkat.',
 dict(A='B için 6 seçenek saymışsın; 1–9 arasından yalnızca A ve C çıkar.',C='B = 0’ı da saymışsın; rakamlar sıfırdan farklı olmalı.',D='(A, C) ikililerinden birini fazla yazmış olabilirsin; C sıfır olamaz, 5 ikili var.',E='B’nin A ve C’den farklı olması gerektiğini unutmuşsun.'),
 kisa='Fark ÷ 99 = rakam farkı (4). Bu farkı veren ikili sayısı 9 − 4 = 5; her biri için B’ye 7 seçenek: 5 × 7.')
# ---- 0017k
sol=[(e,e+2,3*e+1,3*e+3) for e in range(11,100,2) if 3*e+3<100 and 8*e+6<150]; assert max(x[3] for x in sol)==54
K('0017','Eda, Fatih, Gül ve Hakan tahtaya birer tane iki basamaklı doğal sayı yazmıştır.\n• Eda ile Fatih’in yazdığı sayılar ardışık tek sayılardır ve Fatih’inki daha büyüktür.\n• Gül ile Hakan’ın yazdığı sayılar ardışık çift sayılardır ve Hakan’ınki daha büyüktür.\n• Gül’ün yazdığı sayı, Eda’nın yazdığı sayının 3 katından 1 fazladır.\n• Dört sayının toplamı 150’den küçüktür.\nBuna göre Hakan’ın yazdığı sayı en çok kaçtır?',
 ['50','52','54','56','58'],'C','Koşullara göre Hakan’ın sayısının en büyük değeri.',
 ['Eda’nın sayısına e de; diğer üç sayıyı e ile yaz.','Dört sayının toplamını e cinsinden bul ve 150’den küçük yap.','e’nin iki basamaklı tek sayı olduğunu unutma.'],
 [B('Ardışık tek / çift sayılar','2’şer artar: 15, 17 (tek) · 30, 32 (çift)')],
 [A('Eda’ya e de','Fatih’in sayısı Eda’nınkinden 2 fazla.','Eda = e · Fatih = e + 2'),
  A('Gül ve Hakan','Gül, Eda’nın 3 katından 1 fazla; Hakan, Gül’den 2 fazla.','Gül = 3e + 1 · Hakan = 3e + 3'),
  A('Toplamı yaz','Dört sayıyı topla; toplam 150’den küçük olmalı.','e + (e + 2) + (3e + 1) + (3e + 3) = 8e + 6 < 150'),
  A('e’nin sınırı','8e < 144, yani e < 18. e iki basamaklı **tek** sayı: en büyük **17**.','e = 17'),
  A('Hakan’ı bul','Hakan = 3e + 3. Kontrol: 17, 19, 52, 54 toplamı 142 < 150.','3 × 17 + 3 = 54')],
 '“En çok” sorularında tüm sayıları tek harfe bağla; sınır eşitsizliği o harfin en büyük değerini verir.',
 dict(A='50 için e = 15 almışsın; 17 de koşulları sağlıyor.',B='52, Gül’ün sayısı; soru Hakan’ınkini soruyor.',D='56 için e tek sayı olmaz (3e + 3 = 56 ⇒ e kesirli).',E='58 için e = 18,3 gerekir; e tek tam sayı olmalı ve toplam 150’yi geçer.'))
# ---- 0018k
s=[(x,y) for x in range(1,50) for y in range(1,50) if 2*x+5*y==47]
assert all(y%2 for x,y in s) and len({(x+y)%2 for x,y in s})==2 and min(x+y for x,y in s)==10 and max(x+y for x,y in s)==22
K('0018','Bir binanın merdiven basamakları 1’den başlayarak numaralandırılmıştır.\nZeynep, 3 numaralı basamakta dururken yürümeye başlayıp 50 numaralı basamağa çıkarken her adımda ya iki ya da beş basamak çıkmış; hem ikişerli hem beşerli adım atmıştır.\nBuna göre\nI. Zeynep’in attığı beşerli adımların sayısı tektir.\nII. Zeynep’in attığı toplam adım sayısı tektir.\nIII. Zeynep en az 12 adım atmıştır.\nifadelerinden hangileri kesinlikle doğrudur?',
 ['Yalnız I','Yalnız II','I ve II','I ve III','II ve III'],'A','Tüm olası adım dağılımlarında doğru kalan ifadeler.',
 ['Zeynep toplam kaç basamak çıktı?','İkişerli adım sayısına x, beşerli adım sayısına y de; 2x + 5y kaça eşit?','Olası (x, y) ikililerini yazıp her ifadeyi dene.'],
 [TEK,B('5 ile çarpım','5 × tek = tek · 5 × çift = çift')],
 [A('Mesafe','3. basamaktan 50. basamağa çıkılıyor.','50 − 3 = 47 basamak'),
  A('Denklemi kur','x ikişerli, y beşerli adım olsun.','2x + 5y = 47'),
  A('y tek mi?','2x her zaman çift. Çift + 5y = 47 (tek) olması için 5y tek olmalı; bu da **y tek** demek. I doğru.','çift + tek = tek'),
  A('Tüm olasılıklar','y = 1, 3, 5, 7, 9 için x = 21, 16, 11, 6, 1. Toplam adım x + y: 22, 19, 16, 13, 10.','x + y ∈ {10, 13, 16, 19, 22}'),
  A('II ve III’ü dene','Toplam 22 ya da 16 gibi çift de olabilir: II kesin değil. Toplam 10 da olabilir: III yanlış.','Doğru: yalnız I')],
 '“Kesinlikle” sorularında tüm durumları listele; tek bir karşı örnek ifadeyi düşürür.',
 dict(B='II kesin değil: x = 21, y = 1 için toplam 22 adım (çift). Ayrıca I her durumda doğru.',C='II kesin değil: x = 21, y = 1 için toplam 22 adım (çift).',D='III kesin değil: x = 1, y = 9 için Zeynep yalnızca 10 adım atar.',E='II ve III kesin değil; ikisinin de karşı örneği var.'))
# ---- 0020k
ns=[k for k in range(1,15) if F(k+2)-F(k+1)==36*F(k)]; assert ns==[5] and F(5)==120
K('0020','n bir pozitif tam sayı olmak üzere\n(n + 2)! − (n + 1)! = 36 · n!\nolduğuna göre n! kaçtır?',
 ['24','60','120','240','720'],'C','Denklemi sağlayan n için n! değeri.',
 ['(n + 2)! ifadesini (n + 1)! cinsinden yaz.','Sol tarafı (n + 1)! parantezine al.','(n + 1)!’i de n! cinsinden yazıp sadeleştir.'],[FAK],
 [A('(n + 2)!’yi aç','(n + 2)!, (n + 1)!’in (n + 2) katıdır.','(n + 2)! = (n + 2) × (n + 1)!'),
  A('Ortak paranteze al','Sol tarafta iki terimde de (n + 1)! var; dışarı al.','(n + 1)! × (n + 2 − 1) = (n + 1) × (n + 1)!'),
  A('(n + 1)!’i aç','(n + 1)! = (n + 1) × n! yazınca iki tarafta n! sadeleşir.','(n + 1) × (n + 1) × n! = 36 × n! ⇒ (n + 1)² = 36'),
  A('n’yi bul','n + 1 pozitif olduğundan n + 1 = 6.','n = 5'),
  A('İstenen değer','Soru n!’i soruyor.','5! = 1 × 2 × 3 × 4 × 5 = 120')],
 'Faktöriyel farklarında en küçük faktöriyeli parantez dışına al; sonra soruda hangi faktöriyelin istendiğine bak.',
 dict(A='24 = 4!; n = 5 olduğundan n! = 5! = 120.',B='60 = 5!/2; faktöriyeli eksik hesaplamışsın.',D='240 = 2 × 5!; faktöriyeli yanlış açmışsın.',E='720 = 6! = (n + 1)!; soru n!’i soruyor.'),
 kisa='Sol taraf (n + 1)² × n! olur; (n + 1)² = 36 ⇒ n + 1 = 6. Sonra sadece 5!’i hesapla.')
# ---- 0021k
ok=set()
for a,b,c in product([-3,-1,1,2,5],repeat=3):
    if a*b>0 and b*c<0 and a<c: ok.add((a>0,b>0,c>0))
assert ok=={(False,False,True)}
K('0021','a, b ve c sıfırdan farklı gerçel sayılardır.\na · b > 0\nb · c < 0\na < c\nolduğuna göre aşağıdakilerden hangisi kesinlikle negatiftir?',
 ['a · b','a + c','a · b · c','a · c','c − a'],'D','İşaretleri belli olan a, b, c ile kesin negatif ifade.',
 ['a · b > 0 ise a ile b’nin işaretleri hakkında ne söylenir?','b · c < 0 ise c, b’nin tersi işaretli.','a < c bilgisiyle hangi işaret durumunun mümkün olduğunu bul.'],
 [B('Çarpımın işareti','çarpım pozitifse iki sayı aynı işaretli, negatifse zıt işaretlidir')],
 [A('a ve b','a · b > 0 olduğundan **a ve b aynı işaretli**.','a, b aynı işaret'),
  A('c','b · c < 0 olduğundan c, b’nin (ve a’nın) **zıt işaretli**.','c zıt işaret'),
  A('Hangi durum?','İki ihtimal var: a ve b pozitif, c negatif; ya da a ve b negatif, c pozitif. İlkinde a < c olamaz (pozitif sayı negatiften küçük olamaz).','a < 0 · b < 0 · c > 0'),
  A('Şıkları dene','a · c = (−) × (+) = negatif. a · b ve a · b · c pozitif; c − a pozitif; a + c’nin işareti sayılara bağlı.','a · c < 0')],
 'İki çarpım bilgisi işaret gruplarını verir; sıralama bilgisi hangi grubun negatif olduğunu seçer.',
 dict(A='a ve b aynı işaretli: a · b pozitiftir.',B='a negatif, c pozitif: a + c’nin işareti sayılara bağlıdır.',C='a · b pozitif, c pozitif: a · b · c pozitiftir.',E='c pozitif, a negatif: c − a pozitiftir.'),
 kisa='Sayı ver: a = −1, b = −2, c = 3 koşulları sağlar. Şıkları hesapla; yalnızca a · c = −3 negatif.')
# ---- 0022k
best=max((100*p[0]+10*p[1]+p[2])+(10*p[3]+p[4]) for p in permutations([1,3,4,6,8])); assert best==904
K('0022','1, 3, 4, 6 ve 8 rakamlarının her biri yalnızca bir kez kullanılarak üç basamaklı bir A sayısı ile iki basamaklı bir B sayısı yazılıyor.\nBuna göre A + B toplamı en çok kaçtır?',
 ['862','874','886','894','904'],'E','A + B’nin alabileceği en büyük değer.',
 ['Toplamda hangi basamaktaki rakam en çok değer katar?','En büyük rakamı A’nın yüzler basamağına koy.','Sonra kalan en büyük iki rakamı onlar basamaklarına, en küçükleri birler basamaklarına yerleştir.'],
 [B('Basamak değeri','yüzler basamağındaki rakam 100, onlar basamağındaki 10, birler basamağındaki 1 ile çarpılır')],
 [A('Yüzler basamağı','Toplama en çok katkıyı yüzler basamağı yapar: oraya en büyük rakam 8.','A = 8__'),
  A('Onlar basamakları','A’nın da B’nin de onlar basamağı 10 ile çarpılır; kalan en büyük iki rakam 6 ve 4 bu iki yere gider.','onlar: 6 ve 4'),
  A('Birler basamakları','Kalan 3 ve 1 birler basamaklarına gider.','birler: 3 ve 1'),
  A('Toplamı hesapla','Örneğin A = 863, B = 41 (ya da A = 843, B = 61) aynı toplamı verir.','863 + 41 = 904')],
 'Toplamı büyütmek için büyük rakamları değeri büyük basamaklara koy; aynı değerli basamaklarda yer değiştirmek toplamı değiştirmez.',
 dict(A='862 için onlar basamaklarına büyük rakamları yerleştirmemişsin.',B='874 için 6’yı birler basamağına koymuş olabilirsin.',C='886 için onlar ve birler basamaklarındaki rakamları karıştırmışsın.',D='894 için 4 ile 3’ün yerini karıştırmış olabilirsin; 4 onlar basamağına gitmeli.'),
 kisa='Toplam = 100 × (yüzler) + 10 × (iki onlar) + (iki birler) = 100 × 8 + 10 × (6 + 4) + (3 + 1) = 904.')
# ---- 0023k
dolu=48*Fr(5,8); assert dolu==30 and 8-(30-26)==4
K('0023','48 koltuklu bir sinema salonunda koltukların 5/8’i doludur.\nSalona bakan bir güvenlik kamerasının görüntüsünde, bir direk yüzünden 8 koltuk görünmemektedir. Görünen koltuklardan 26’sı doludur.\nBuna göre direğin arkasında kalan koltuklardan kaç tanesi boştur?',
 ['3','4','5','6','8'],'B','Görünmeyen 8 koltuktan boş olanların sayısı.',
 ['Salonda toplam kaç dolu koltuk var?','Görünmeyen koltuklarda kaç dolu koltuk kalıyor?','Görünmeyen koltuk sayısından dolu olanları çıkar.'],
 [B('Bir sayının 5/8’i','önce 8’e böl, sonra 5 ile çarp')],
 [A('Dolu koltuklar','48’in 5/8’i.','48 ÷ 8 × 5 = 30'),
  A('Görünen koltuklar','Kamera salonun tamamını görüyor; 8 koltuk kapalı.','48 − 8 = 40 görünen koltuk, 26’sı dolu'),
  A('Arkadaki dolular','Görünmeyen dolu koltuklar direğin arkasında.','30 − 26 = 4'),
  A('Arkadaki boşlar','Kapalı 8 koltuğun 4’ü dolu.','8 − 4 = 4')],
 'Görünmeyen kısım sorularında önce bütündeki toplamı bul, sonra görüneni çıkar.',
 dict(A='Dolu koltuk sayısını yanlış hesaplamışsın: 48 × 5/8 = 30.',C='Görünen boş koltukları karıştırmış olabilirsin; arkadaki dolu 30 − 26 = 4.',D='Görünen koltuk sayısını yanlış bulmuşsun: 48 − 8 = 40.',E='8 koltuğun hepsini boş saymışsın; 4’ü dolu.'))
# ---- 0025k
P=[p for p in range(2,30) if all(p%d for d in range(2,int(p**.5)+1))]
s=[(a,b) for a in P for b in P if a<b and a+b==21]; assert s==[(2,19)]
K('0025','a ve b asal sayılar olmak üzere\na + b = 21\nolduğuna göre a · b çarpımı kaçtır?',
 ['38','42','54','80','98'],'A','a ile b’nin çarpımı.',
 ['21 tek; iki sayının toplamı tekse biri çift olmalı.','Çift olan asal sayı hangisi?','Diğer sayıyı bul ve asal olduğunu kontrol et.'],[ASAL,TEK],
 [A('Tek-çift dengesi','21 tek; iki sayının toplamı tekse biri tek, biri çifttir.','tek + çift = tek'),
  A('Çift asal','Çift olan tek asal sayı 2; diğer sayı 21 − 2 = 19 ve 19 asaldır.','a = 2 · b = 19'),
  A('Çarp','İki sayıyı çarp.','2 × 19 = 38')],
 'İki asalın toplamı tekse biri mutlaka 2’dir.',
 dict(B='42 = 2 × 21; 21 asal değil.',C='54 = 3 × 18 ya da 6 × 9; bunlar asal değil.',D='80 = 5 × 16 ya da 4 × 20; bunlar asal değil.',E='98 = 2 × 49 ya da 7 × 14; 49 ve 14 asal değil.'))
# ---- 0026k
ok=set()
for a,b in product([1,3,5,7],[1,3,5,9]): ok.add(tuple(v%2 for v in (a*b,a+b,a+2*b,3*a,b*b)))
assert all(t[1]==0 for t in ok) and all(t[i]==1 for t in ok for i in (0,2,3,4))
K('0026','Bir otobüsteki ayakta duran yolcuların sayısı a, oturan yolcuların sayısı b’dir.\na ve b birer tek sayı olduğuna göre aşağıdakilerden hangisi kesinlikle çift sayıdır?',
 ['a · b','a + b','a + 2b','3a','b²'],'B','Her zaman çift olan ifade.',
 ['İki tek sayının çarpımı tek midir, çift mi?','İki tek sayının toplamı tek midir, çift mi?','Her şıkkı a = 3, b = 5 gibi bir örnekle de dene.'],[TEK,CARP],
 [A('Çarpımlar','Tek × tek = tek; bu yüzden a · b, 3a ve b² tektir.','tek × tek = tek'),
  A('a + 2b','2b her zaman çift; tek + çift = tek.','a + 2b tek'),
  A('a + b','Tek + tek her zaman çifttir.','a + b çift ✓')],
 'Tek sayıların çarpımı hep tektir; toplamda kaç tane tek terim olduğuna bak.',
 dict(A='İki tek sayının çarpımı tektir.',C='2b çift, a tek: toplamları tektir.',D='3 ve a tek: çarpımları tektir.',E='Tek bir sayının karesi tektir.'),
 kisa='a = 1, b = 1 koy: a · b = 1, a + b = 2, a + 2b = 3, 3a = 3, b² = 1. Çift olan yalnızca a + b.')
json.dump(OUT,open(os.path.join(H,'sayi-kumeleri-kardes2.json'),'w'),ensure_ascii=False,indent=1)
from collections import Counter; print(len(OUT),Counter(q['cevap']['sik'] for q in OUT))
