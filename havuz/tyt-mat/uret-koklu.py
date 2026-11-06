"""Köklü Sayılar · parti 1: 8 ana + 8 kardeş. Köklü değerler a + b√d biçiminde kesin (Fraction) hesaplanır."""
import sys,os,math
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,os.path.join(H,'..'))
from ortak import *
P=Parti('koklu','Köklü Sayılar','mat|Köklü Sayılar')
TT=lambda **k:k
class Q:
    """a + b√d (a, b kesir; d kare çarpansız sabit)"""
    def __init__(s,a,b,d): s.a,s.b,s.d=Fr(a),Fr(b),d
    def __add__(s,o): o=s._c(o); return Q(s.a+o.a,s.b+o.b,s.d)
    def __sub__(s,o): o=s._c(o); return Q(s.a-o.a,s.b-o.b,s.d)
    def __mul__(s,o): o=s._c(o); return Q(s.a*o.a+s.b*o.b*s.d,s.a*o.b+s.b*o.a,s.d)
    def inv(s): n=s.a*s.a-s.b*s.b*s.d; assert n!=0; return Q(s.a/n,-s.b/n,s.d)
    def __truediv__(s,o): return s*s._c(o).inv()
    def _c(s,o): return o if isinstance(o,Q) else Q(o,0,s.d)
    def __eq__(s,o): o=s._c(o); return (s.a,s.b,s.d)==(o.a,o.b,o.d)
    def f(s): return float(s.a)+float(s.b)*math.sqrt(s.d)
def kok(n):
    """√n = c√d (d kare çarpansız)"""
    c=1
    for k in range(int(n**.5),0,-1):
        if n%(k*k)==0: c=k; break
    return c,n//(c*c)
def artan(*v): return all(v[i]<v[i+1] for i in range(len(v)-1))
KOK=B('Kök dışına çıkarma','kök içini “tam kare × kalan” biçiminde yaz, tam karenin kökünü dışarı al. Örnek: √12 = √(4 × 3) = 2√3')
BEN=B('Benzer kökler','kök içleri aynı olan terimler katsayılarıyla toplanır: 5√3 − 2√3 = 3√3. Kök içleri farklıysa birleşmez: √2 + √3 ≠ √5')
CK=B('Köklerde çarpma ve bölme','√a × √b = √(a × b) · √a ÷ √b = √(a ÷ b). Örnek: √2 × √8 = √16 = 4')
SOK=B('Katsayıyı köke sokma','a√b = √(a² × b): katsayının karesi içeri girer. Örnek: 3√2 = √(9 × 2) = √18')
KAR=B('Kökleri karşılaştırma','pozitif sayılarda kök içi büyük olan kök büyüktür. Örnek: √18 < √19 < √20')
ES=B('Eşlenik','√a − b ile √a + b birbirinin eşleniğidir; çarpımları (√a)² − b² = a − b² olur. Örnek: (√5 − 2) × (√5 + 2) = 5 − 4 = 1')

# ===== 0001 KOLAY kk-benzer (K-KK-01)
assert kok(75)==(5,3) and kok(12)==(2,3) and kok(66)==(1,66)
r=Q(0,5,3)-Q(0,2,3)+Q(0,1,3); assert r==Q(0,4,3)
assert 5-4+1==2 and 5-2==3 and 5+2+1==8 and 75-12+3==66
assert artan(2*3**.5,3*3**.5,4*3**.5,66**.5,8*3**.5)
P.R('0001','kk-benzer','Kök dışına çıkarma ve benzer kökler','kolay','Benzer Kökler','Kök içindeki tam kare çarpanı dışarı çıkararak benzer köklerle toplama ve çıkarma yapar.','düz',2,
 'K-KK-01 (kök dışına çıkarma, benzer kökler) · üç terim, kök içi 3',
 '√75 − √12 + √3\nişleminin sonucu kaçtır?',
 ['2√3','3√3','4√3','√66','8√3'],'C','Üç köklü terimin sonucu.',
 ['75 ve 12’yi “tam kare × 3” biçiminde yaz.','Tam karenin kökünü dışarı al.','Üç terim de √3’lü olunca katsayıları topla, çıkar.'],[KOK,BEN],
 [A('Kök dışına çıkar','75 = 25 × 3 ve 12 = 4 × 3; 25 ile 4 tam kare.','√75 = 5√3 · √12 = 2√3'),
  A('Benzer kökleri birleştir','Hepsi √3’lü; katsayılarla işlem yap.','5√3 − 2√3 + 1√3 = (5 − 2 + 1)√3'),
  A('Sonuç','Katsayı 4.','4√3')],
 'Köklü toplamada önce her terimi sadeleştir; kök içleri aynı olmadan toplama yapılmaz.',
 dict(A='2√3, √12’yi 4√3 sanmak; 4 kökün dışına 2 olarak çıkar.',B='3√3, sondaki +√3 terimini unutmak.',D='√66, kök içlerini toplayıp çıkarmak (75 − 12 + 3); √a − √b, √(a − b) değildir.',E='8√3, −√12’nin eksisini artı almak: 5 + 2 + 1.'),
 TT(A='bilgi',B='dikkat',D='bilgi',E='islem'))
assert kok(200)==(10,2) and kok(50)==(5,2) and kok(18)==(3,2)
r=Q(0,10,2)-Q(0,5,2)-Q(0,3,2); assert r==Q(0,2,2)
assert 10-5-9==-4 and 10-5==5 and 10-5+3==8 and 200-50-18==132
assert artan(-4*2**.5,2*2**.5,5*2**.5,8*2**.5,132**.5)
P.K('0001','√200 − √50 − √18\nişleminin sonucu kaçtır?',
 ['−4√2','2√2','5√2','8√2','√132'],'B','Üç köklü terimin sonucu.',
 ['200, 50 ve 18’i “tam kare × 2” biçiminde yaz.','Tam karelerin kökünü al: 100, 25 ve 9.','√2’li terimlerin katsayılarıyla işlem yap; iki eksiye dikkat.'],[KOK,BEN],
 [A('Kök dışına çıkar','200 = 100 × 2 · 50 = 25 × 2 · 18 = 9 × 2.','√200 = 10√2 · √50 = 5√2 · √18 = 3√2'),
  A('Benzer kökleri birleştir','Hepsi √2’li.','10√2 − 5√2 − 3√2 = (10 − 5 − 3)√2'),
  A('Sonuç','Katsayı 2.','2√2')],
 'Kök dışına çıkan sayı tam karenin kendisi değil, kareköküdür: √9 = 3.',
 dict(A='−4√2, √18’i 9√2 sanmak; 9 kökün dışına 3 olarak çıkar.',C='5√2, sondaki −√18 terimini unutmak.',D='8√2, −√18’i +3√2 almak; işaret korunmalı.',E='√132, kök içlerini çıkarmak (200 − 50 − 18).'),
 TT(A='bilgi',C='dikkat',D='islem',E='bilgi'))

# ===== 0002 KOLAY kk-carpma (K-KK-03)
assert 12*15%5==0 and 12*15//5==36 and math.isqrt(36)==6 and Q(0,2,3)*Q(0,1,3)==6
assert 12+15-5==22 and artan(22**.5,6,6*3**.5,18,36)
P.R('0002','kk-carpma','Köklü ifadelerde çarpma ve bölme','kolay','Çarpma ve Bölme','Köklü sayıları tek kök altında çarpıp bölerek sonucu tam sayıya indirger.','düz',2,
 'K-KK-03 (köklerde çarpma-bölme) · çarpım ve bölüm birlikte, sonuç tam sayı',
 '(√12 · √15) ÷ √5\nişleminin sonucu kaçtır?',
 ['√22','6','6√3','18','36'],'B','İşlemin sonucu.',
 ['Kökleri tek kök altında birleştirebilirsin.','√a × √b = √(a × b), √a ÷ √b = √(a ÷ b).','Kök içindeki sayı tam kare mi?'],[CK,KOK],
 [A('Tek köke topla','Çarpma ve bölme kök içinde yapılabilir.','√(12 × 15 ÷ 5) = √(180 ÷ 5) = √36'),
  A('Kökü al','36 tam kare.','√36 = 6'),
  A('İkinci yol','√12 = 2√3 ve √15 ÷ √5 = √3.','2√3 × √3 = 2 × 3 = 6 ✓')],
 'Köklü çarpma-bölmede her şeyi tek kökte topla; içerisi çoğu zaman tam kare çıkar.',
 dict(A='√22, kök içlerini toplayıp çıkarmak (12 + 15 − 5); kökler çarpılırken içleri çarpılır.',C='6√3, √3 × √3’ü 3√3 sanmak; √3 × √3 = 3.',D='18, √3 × √3’ü 9 sanmak; √3 × √3 = √9 = 3.',E='36, kök içindeki 36’nın kökünü almayı unutmak.'),
 TT(A='bilgi',C='islem',D='bilgi',E='dikkat'))
assert 14*24%21==0 and 14*24//21==16 and Q(0,2,2)*Q(0,1,2)==4 and 14+24-21==17
assert artan(4,17**.5,4*2**.5,8,16)
P.K('0002','(√14 · √24) ÷ √21\nişleminin sonucu kaçtır?',
 ['4','√17','4√2','8','16'],'A','İşlemin sonucu.',
 ['Üç kökü tek kök altında birleştir.','14 × 24’ü 21’e bölmeden önce ortak çarpanları sadeleştir.','Kök içinde kalan sayı tam kare mi?'],[CK,KOK],
 [A('Tek köke topla','Çarpma ve bölmeyi kök içinde yap.','√(14 × 24 ÷ 21)'),
  A('Sadeleştir','14 = 2 × 7, 24 = 8 × 3, 21 = 3 × 7; 7 ve 3 sadeleşir.','√(2 × 8) = √16'),
  A('Kökü al','16 tam kare.','√16 = 4')],
 'Kök içinde çarpmadan önce sadeleştirmek büyük sayılarla uğraşmayı önler.',
 dict(B='√17, kök içlerini toplayıp çıkarmak (14 + 24 − 21).',C='4√2, √2 × √2’yi 2√2 sanmak: 2 × 2√2.',D='8, √2 × √2’yi 4 sanmak; √2 × √2 = 2.',E='16, kök içindeki 16’nın kökünü almayı unutmak.'),
 TT(B='bilgi',C='islem',D='bilgi',E='dikkat'))

# ===== 0003 ORTA kk-tahmin (K-KK-06)
a,b,c=4*5,9*2,19; assert b<c<a
assert 10<18<19 and 2<5<19 and 1<2<3       # çeldiriciler A (2√5 = √10), B (kök içleri), C (katsayılar)
P.R('0003','kk-tahmin','Köklü sayıları tahmin ve sıralama','orta','Sıralama','Katsayıları kök içine alarak köklü sayıları sıralar.','düz',3,
 'K-KK-06 (katsayıyı köke sokup karşılaştırma) · üç sayı, kök içleri birbirine çok yakın',
 'a = 2√5\nb = 3√2\nc = √19\nolduğuna göre a, b ve c’nin küçükten büyüğe sıralanışı aşağıdakilerden hangisidir?',
 ['a < b < c','b < a < c','c < a < b','c < b < a','b < c < a'],'E','Üç sayının küçükten büyüğe sıralanışı.',
 ['Katsayıları kök içine al; katsayının karesi içeri girer.','2√5 ve 3√2’yi √… biçiminde yaz.','Kök içlerini karşılaştır.'],[SOK,KAR],
 [A('a’yı köke al','2’nin karesi 4.','2√5 = √(4 × 5) = √20'),
  A('b’yi köke al','3’ün karesi 9.','3√2 = √(9 × 2) = √18'),
  A('Sırala','Kök içleri: 18 < 19 < 20.','√18 < √19 < √20 ⇒ b < c < a')],
 'Köklü sayıları karşılaştırırken katsayıları kareleriyle köke sok; ne yalnız katsayıya ne yalnız kök içine bak.',
 dict(A='a < b < c, 2√5’i √10 yazmak; 2’nin karesi (4) içeri girer: √20.',B='b < a < c, yalnızca kök içlerini (2, 5, 19) karşılaştırmak; katsayılar da hesaba katılmalı.',C='c < a < b, yalnızca katsayıları (1, 2, 3) karşılaştırmak.',D='c < b < a, katsayısı olmayan √19’u en küçük sanmak; √19 > √18.'),
 TT(A='islem',B='bilgi',C='bilgi',D='dikkat'))
x,y,z=9*3,4*7,26; assert z<x<y and 9<26<28 and 3<7<26 and 1<2<3
P.K('0003','x = 3√3\ny = 2√7\nz = √26\nolduğuna göre aşağıdakilerden hangisi doğrudur?',
 ['z < x < y','x < y < z','x < z < y','y < x < z','z < y < x'],'A','Üç sayının küçükten büyüğe doğru sıralanışı.',
 ['Katsayıları kök içine al.','3√3 ve 2√7’yi √… biçiminde yaz.','Kök içlerini küçükten büyüğe sırala.'],[SOK,KAR],
 [A('x’i köke al','3’ün karesi 9.','3√3 = √(9 × 3) = √27'),
  A('y’yi köke al','2’nin karesi 4.','2√7 = √(4 × 7) = √28'),
  A('Sırala','Kök içleri: 26 < 27 < 28.','√26 < √27 < √28 ⇒ z < x < y')],
 'Kök içleri birbirine yakın olsa da karşılaştırma kesindir: katsayıyı içeri al, kök içlerini sırala.',
 dict(B='x < y < z, yalnızca kök içlerini (3, 7, 26) karşılaştırmak.',C='x < z < y, 3√3’ü √9 yazmak; 3’ün karesi içeri girer: √27.',D='y < x < z, büyükten küçüğe sırayı (y, x, z) küçükten büyüğe gibi yazmak.',E='z < y < x, yalnızca katsayıları (1, 2, 3) karşılaştırmak.'),
 TT(B='bilgi',C='islem',D='dikkat',E='bilgi'))

# ===== 0004 ORTA kk-eslenik (K-KK-04)
r=Q(1,0,5)/Q(-2,1,5)+Q(1,0,5)/Q(2,1,5); assert r==Q(0,2,5) and Q(-2,1,5)*Q(2,1,5)==1
assert Q(2,0,5)/Q(0,2,5)==Q(0,Fr(1,5),5)       # çeldirici A: 2/(2√5) = √5/5
assert artan(5**.5/5,2*5**.5/9,2*5**.5/3,4,2*5**.5)
P.R('0004','kk-eslenik','Eşlenik ve paydayı rasyonel yapma','orta','Eşlenik','Paydaları eşlenik olan köklü kesirleri eşlenik çarpımıyla toplar.','düz',3,
 'K-KK-04 (eşlenik çarpımı a − b²) · iki kesrin toplamı, payda çarpımı 1',
 '1/(√5 − 2) + 1/(√5 + 2)\ntoplamı kaçtır?',
 ['√5/5','2√5/9','2√5/3','4','2√5'],'E','İki kesrin toplamı.',
 ['İki payda birbirinin eşleniği; ortak payda onların çarpımı.','(√5 − 2) × (√5 + 2) = (√5)² − 2².','Payları toplarken çapraz çarpımları yaz.'],[ES,B('Kesirleri toplama','a/b + c/d = (a × d + c × b)/(b × d). Örnek: 1/2 + 1/3 = (3 + 2)/6 = 5/6')],
 [A('Ortak payda','Paydaların çarpımı eşlenik çarpımıdır.','(√5 − 2) × (√5 + 2) = 5 − 4 = 1'),
  A('Payları topla','Her pay öbür paydayla çarpılır.','1 × (√5 + 2) + 1 × (√5 − 2) = 2√5'),
  A('Sonuç','Payda 1.','2√5 ÷ 1 = 2√5')],
 'Paydalar eşlenikse ortak payda a − b² olur; çoğu zaman 1 ya da küçük bir tam sayı çıkar.',
 dict(A='√5/5, payları ve paydaları ayrı ayrı toplamak: 2/(2√5); kesirler böyle toplanmaz.',B='2√5/9, eşlenik çarpımını 5 + 4 almak; (√5 − 2) × (√5 + 2) = 5 − 4.',C='2√5/3, paydayı 5 − 2 almak; 2’nin karesi 4’tür.',D='4, payları toplarken (√5 + 2) − (√5 − 2) yapmak; işlem toplamadır.'),
 TT(A='bilgi',B='bilgi',C='islem',D='islem'))
# √7 ve √5 iki ayrı kök: kesin sınıf tek kök tuttuğu için burada kayan nokta + tam sayı eşlenik kontrolü
s7,s5=7**.5,5**.5
assert abs(2/(s7+s5)-(s7-s5))<1e-12 and abs(2/(s7-s5)-(s7+s5))<1e-12 and 7-5==2
assert abs(((s7-s5)-(s7+s5))-(-2*s5))<1e-12 and abs((s7-s5)/6-(s7+s5)/6-(-s5/3))<1e-12 and abs((s7-s5)-s7+s5)<1e-12
assert artan(-2*s5,-s5/3,0,2*s5,2*s7)
P.K('0004','2/(√7 + √5) − 2/(√7 − √5)\nfarkı kaçtır?',
 ['−2√5','−√5/3','0','2√5','2√7'],'A','İki kesrin farkı.',
 ['Her kesrin paydasını eşleniğiyle çarparak kökten kurtar.','(√7 + √5) × (√7 − √5) = 7 − 5.','Çıkarmada ikinci kesrin önündeki eksiyi tüm terimlere dağıt.'],[ES,B('Paydayı kökten kurtarma','payı ve paydayı paydanın eşleniğiyle çarp. Örnek: 1/(√3 − 1) = (√3 + 1)/2')],
 [A('İlk kesir','Eşlenik √7 − √5 ile çarp.','2 × (√7 − √5) ÷ (7 − 5) = √7 − √5'),
  A('İkinci kesir','Eşlenik √7 + √5 ile çarp.','2 × (√7 + √5) ÷ (7 − 5) = √7 + √5'),
  A('Çıkar','Eksiyi parantezin iki terimine de dağıt.','√7 − √5 − √7 − √5 = −2√5')],
 'Kesirleri ayrı ayrı rasyonel yapınca işlem benzer köklerle toplama-çıkarmaya döner.',
 dict(B='−√5/3, eşlenik çarpımını 7 + 5 = 12 almak; (√7 + √5) × (√7 − √5) = 7 − 5 = 2.',C='0, eksiyi yalnız ilk terime dağıtmak; −(√7 + √5) = −√7 − √5.',D='2√5, eşlenikleri karıştırıp ilk kesri √7 + √5, ikinciyi √7 − √5 bulmak.',E='2√7, iki kesri çıkarmak yerine toplamak.'),
 TT(B='bilgi',C='islem',D='islem',E='dikkat'))

# ===== 0005 ORTA kk-uzunluk (K-KK-07)
def iki_kare(A1,A2,k1=None,k2=None,fark=None):
    s1=96; s2=round(96*(A2/A1)**.5,1); x0,yb=40,130; b=[]
    b.append(f'<rect x="{x0}" y="{yb-s1}" width="{s1}" height="{s1}" stroke-width="1.6"/>')
    b.append(f'<rect x="{x0+s1}" y="{yb-s2}" width="{s2}" height="{s2}" stroke-width="1.6"/>')
    b.append(G._t(x0+s1/2,yb-s1/2+4,f'{A1} cm²')); b.append(G._t(x0+s1+s2/2,yb-s2/2+4,f'{A2} cm²',size=11))
    if k1:
        d=f'M{x0} {yb} H{x0+s1+s2} V{yb-s2} H{x0+s1} V{yb-s1} H{x0} Z'
        b.append(f'<path d="{d}" stroke-width="3" style="stroke:{G.ACC}" opacity=".85"/>')
        b.append(G._t(x0-6,yb-s1/2+4,k1,anchor='end',size=11,bold=True,renk=G.ACC))
        b.append(G._t(x0+s1/2,yb+16,k1,size=11,bold=True,renk=G.ACC)); b.append(G._t(x0+s1+s2/2,yb+16,k2,size=11,bold=True,renk=G.ACC))
        b.append(G._t(x0+s1+s2+6,yb-s2/2+4,k2,anchor='start',size=11,bold=True,renk=G.ACC))
        b.append(G._t(x0+s1+6,yb-s2-(s1-s2)/2+4,fark,anchor='start',size=11,bold=True,renk=G.ACC))
    return G._svg(300,160 if k1 else 146,''.join(b))
assert kok(48)==(4,3) and kok(27)==(3,3)
cevre=lambda u,k:2*((u+k)+u)              # basamaklı şekil: 2 × (genişlik + yükseklik)
assert cevre(4,3)==22 and 4*4+4*3==28 and 28-2*3==22 and 28-2*4==20 and 22-(4-3)==21 and kok(75)==(5,3) and 2*(5+4)==18
P.R('0005','kk-uzunluk','Köklü uzunluklar ve alan','orta','Köklü Uzunluklar','Alanı verilen karelerin kenarlarını köklü yazıp birleşik şeklin çevresini benzer köklerle hesaplar.','şekilli',3,
 'K-KK-07 (alan → kök kenar, birleşik şekil) · iki kare yan yana, istenen çevre',
 'Alanları 48 cm² ve 27 cm² olan iki kare, aşağıdaki gibi alt kenarları aynı doğru üzerinde olacak ve küçük karenin bir kenarı büyük karenin bir kenarına değecek biçimde yan yana konmuştur.\nBuna göre oluşan şeklin çevresi kaç santimetredir?',
 ['18√3','20√3','21√3','22√3','28√3'],'D','Birleşik şeklin dış çevresi.',
 ['Alanı S olan karenin kenarı √S’dir; 48 ve 27’yi sadeleştir.','İki karenin çevrelerini toplarsan hangi kenar parçası şeklin içinde kalır?','Şeklin çevresi = 2 × (toplam genişlik + büyük karenin kenarı) ile kontrol et.'],[KOK,B('Karenin kenarı','alanı S olan karenin kenarı √S’dir. Örnek: alan 12 ⇒ kenar √12 = 2√3'),BEN],
 [A('Kenarları bul','48 = 16 × 3 ve 27 = 9 × 3.','√48 = 4√3 · √27 = 3√3'),
  A('Değen kenarı çıkar','Çevreler toplamında küçük karenin değen kenarı iki kez (iki karede birer kez) sayılır; şeklin içinde kalır.','4 × 4√3 + 4 × 3√3 = 28√3 · 28√3 − 2 × 3√3 = 22√3'),
  A('Kontrol','Şeklin dış sınırı: genişlik 7√3, en büyük yükseklik 4√3.','2 × (7√3 + 4√3) = 22√3',iki_kare(48,27,'4√3','3√3','√3'))],
 'Birleşik şekillerde çevreyi bulurken içerde kalan (değen) kenarları çıkar, basamak gibi kısa kenarları atlama.',
 dict(A='18√3, kenarları √48 + √27 = √75 diye toplayıp genişliği 5√3 almak.',B='20√3, değen kenar olarak büyük karenin kenarını (4√3) iki kez çıkarmak.',C='21√3, basamaktaki kısa dikey kenarı (4√3 − 3√3 = √3) unutmak.',E='28√3, iki karenin çevrelerini toplamak; değen kenar şeklin çevresinde değil.'),
 TT(A='bilgi',B='islem',C='dikkat',E='dikkat'),sekil=iki_kare(48,27))
assert kok(50)==(5,2) and kok(18)==(3,2) and cevre(5,3)==26 and 4*5+4*3==32 and 32-2*5==22 and 26-(5-3)==24 and 32-3==29
P.K('0005','Alanları 50 cm² ve 18 cm² olan iki kare, aşağıdaki gibi tabanları aynı doğru üzerinde olacak ve birer kenarları birbirine değecek biçimde yan yana yerleştirilmiştir.\nBuna göre oluşan şeklin çevre uzunluğu kaç santimetredir?',
 ['22√2','24√2','26√2','29√2','32√2'],'C','Birleşik şeklin dış çevresi.',
 ['50 ve 18’i “tam kare × 2” biçiminde yaz; kenarları bul.','Çevreleri toplayınca değen kenar kaç kez sayılır?','Basamaktaki kısa kenarı da çevreye kat.'],[KOK,B('Karenin kenarı','alanı S olan karenin kenarı √S’dir. Örnek: alan 8 ⇒ kenar √8 = 2√2'),BEN],
 [A('Kenarları bul','50 = 25 × 2 ve 18 = 9 × 2.','√50 = 5√2 · √18 = 3√2'),
  A('Değen kenarı çıkar','Küçük karenin değen kenarı iki karenin çevresinde birer kez sayılmıştır.','4 × 5√2 + 4 × 3√2 = 32√2 · 32√2 − 2 × 3√2 = 26√2'),
  A('Kontrol','Genişlik 8√2, en büyük yükseklik 5√2.','2 × (8√2 + 5√2) = 26√2',iki_kare(50,18,'5√2','3√2','2√2'))],
 'Basamaklı birleşik şeklin çevresi 2 × (toplam genişlik + en büyük yükseklik) ile hızlıca kontrol edilir.',
 dict(A='22√2, değen kenar olarak büyük karenin kenarını (5√2) iki kez çıkarmak.',B='24√2, basamaktaki kısa kenarı (5√2 − 3√2 = 2√2) unutmak.',D='29√2, değen kenarı yalnız bir kez çıkarmak; o kenar iki karede de sayılmıştı.',E='32√2, iki karenin çevrelerini toplamak.'),
 TT(A='islem',B='dikkat',D='islem',E='dikkat'),sekil=iki_kare(50,18))

# ===== 0006 ORTA kk-tahmin (K-KK-06)
n_=[n for n in range(0,200) if 18<n<28]; assert len(n_)==9 and all(3*2**.5<n**.5<2*7**.5 for n in n_) and not any(3*2**.5<n**.5<2*7**.5 for n in range(0,200) if n not in n_)
assert len([n for n in range(0,200) if 6<n<14])==7 and 27-19==8 and 28-18==10 and [n for n in n_ if math.isqrt(n)**2==n]==[25]
P.R('0006','kk-tahmin','Köklü sayıları tahmin ve sıralama','orta','Aralıktaki Sayılar','Katsayılı kökleri köke sokarak iki kök arasındaki tam sayıları sayar.','düz',3,
 'K-KK-06 (katsayıyı köke sokma) · iki kök arasında kalan tam sayıların adedi',
 '3√2 < √n < 2√7\neşitsizliğini sağlayan kaç tane n tam sayısı vardır?',
 ['1','7','8','9','10'],'D','Koşulu sağlayan n tam sayılarının adedi.',
 ['3√2 ve 2√7’yi √… biçiminde yaz.','Kökler pozitif; kök içleri arasında aynı sıralama geçerli.','Uçlar dahil değil; aradaki tam sayıları say.'],[SOK,KAR],
 [A('Köke sok','Katsayıların karesi içeri girer.','3√2 = √18 · 2√7 = √28'),
  A('Kök içleri','Kökler pozitif olduğundan kök içleri de aynı sırada.','√18 < √n < √28 ⇒ 18 < n < 28'),
  A('Say','19’dan 27’ye kadar (uçlar dahil değil).','27 − 19 + 1 = 9 tane')],
 'a’dan b’ye kadar (ikisi dahil) b − a + 1 tam sayı vardır; uçları dışarıda bırakmayı ayrıca kontrol et.',
 dict(A='1, yalnızca √n’nin tam sayı çıktığı n = 25’i saymak; n’nin tam sayı olması yeterli.',B='7, 3√2’yi √6 ve 2√7’yi √14 yazmak; katsayıların karesi içeri girer.',C='8, 27 − 19 hesaplamak; 19’dan 27’ye kadar 27 − 19 + 1 = 9 sayı vardır.',E='10, 28 − 18 hesaplamak; uçlar dahil değil.'),
 TT(A='dikkat',B='islem',C='islem',E='islem'))
n_=[n for n in range(0,200) if 4*2**.5<n**.5<3*5**.5]; assert n_==list(range(33,45)) and len(n_)==12
assert len([n for n in range(0,200) if 8<n<15])==6 and 44-33==11 and 45-32==13 and [n for n in n_ if math.isqrt(n)**2==n]==[36]
P.K('0006','4√2 < √n < 3√5\nkoşulunu sağlayan n tam sayılarının sayısı kaçtır?',
 ['1','6','11','12','13'],'D','Koşulu sağlayan n tam sayılarının adedi.',
 ['4√2 ve 3√5’i √… biçiminde yaz.','Kök içleri arasındaki eşitsizliği yaz.','Uçlar dahil değil; aradaki tam sayıları dikkatle say.'],[SOK,KAR],
 [A('Köke sok','4’ün karesi 16, 3’ün karesi 9.','4√2 = √32 · 3√5 = √45'),
  A('Kök içleri','Kökler pozitif.','√32 < √n < √45 ⇒ 32 < n < 45'),
  A('Say','33’ten 44’e kadar.','44 − 33 + 1 = 12 tane')],
 'Köklü sınırlar arasında sayı sayarken önce sınırları √… biçimine getir, sonra kök içleri arasında say.',
 dict(A='1, yalnızca √n’nin tam sayı çıktığı n = 36’yı saymak.',B='6, 4√2’yi √8, 3√5’i √15 yazmak; katsayıların karesi içeri girer.',C='11, 44 − 33 hesaplamak; 33’ten 44’e kadar 12 sayı vardır.',E='13, 45 − 32 hesaplamak; uçlar dahil değil.'),
 TT(A='dikkat',B='islem',C='islem',E='islem'))

# ===== 0007 ZOR kk-benzer (K-KK-02)
ik=[(a,288//(a*a)) for a in range(1,300) if 288%(a*a)==0]; assert ik==[(1,288),(2,72),(3,32),(4,18),(6,8),(12,2)]
top={a+b for a,b in ik}; assert len(top)==5 and sorted(top)==[14,22,35,74,289] and len({a+b for a,b in ik if a>1})==4 and kok(288)==(12,2)
P.R('0007','kk-benzer','Kök dışına çıkarma ve benzer kökler','zor','Biçim Sayma','Bir köklü sayının a√b biçimindeki bütün yazılışlarını kare bölenlerle bulur, oluşan toplamları eksiksiz ve tekrarsız sayar.','düz',4,
 'K-KK-02 (a√b = √(a²b) ile biçim sayma) · yeni istenen (farklı toplamların sayısı), tekrar eden toplam tuzağı',
 'a ve b pozitif tam sayılar olmak üzere\na√b = √288\neşitliğini sağlayan bütün (a, b) ikilileri için a + b toplamı kaç farklı değer alır?',
 ['1','4','5','6','12'],'C','a + b’nin alabileceği farklı değerlerin sayısı.',
 ['a√b’yi tek kök altında yaz: a√b = √(a² × b).','a² × b = 288 olmalı; a² hangi tam kareler olabilir?','Her ikilinin toplamını yaz; aynı çıkan toplam var mı?'],[SOK,B('Kare bölen','n’yi bölen tam karelerdir. Örnek: 72’nin kare bölenleri 1, 4, 9, 36')],
 [A('Tek köke getir','Katsayı karesiyle içeri girer.','a√b = √(a² × b) ⇒ a² × b = 288'),
  A('Kare bölenler','288 = 2⁵ × 3². a² bu sayıyı bölmeli.','a² ∈ {1, 4, 9, 16, 36, 144} ⇒ a ∈ {1, 2, 3, 4, 6, 12}'),
  A('İkilileri yaz','b = 288 ÷ a².','(1, 288) (2, 72) (3, 32) (4, 18) (6, 8) (12, 2)'),
  A('Toplamlar','6 + 8 = 14 ve 12 + 2 = 14 aynı.','289; 74; 35; 22; 14; 14'),
  A('Farklı olanları say','Altı ikili, beş farklı toplam.','5 farklı değer')],
 'a√b biçimlerini kök içinin kare bölenleri belirler; sayarken soru ikilileri mi, değerleri mi istiyor, ayır.',
 dict(A='1, yalnızca en sade biçimi (12√2) saymak; 2√72, 6√8 gibi biçimler de eşitliği sağlar.',B='4, a = 1 durumunu (1√288) saymamak; a = 1 de pozitif tam sayıdır.',D='6, altı ikiliyi saymak; 6 + 8 ile 12 + 2 aynı toplamı verir.',E='12, her ikiliyi ters sırayla da saymak; a√b ile b√a farklı sayılardır.'),
 TT(A='bilgi',B='dikkat',D='dikkat',E='bilgi'))
ik=[(x,972//(x*x)) for x in range(1,1000) if 972%(x*x)==0]; assert 18*18*3==972 and ik==[(1,972),(2,243),(3,108),(6,27),(9,12),(18,3)]
top={x+y for x,y in ik}; assert len(top)==5 and len({x+y for x,y in ik if x>1})==4 and max(x for x,y in ik)==18
P.K('0007','x ve y pozitif tam sayılar olmak üzere\nx√y = 18√3\nolduğuna göre x + y toplamı kaç farklı değer alabilir?',
 ['4','5','6','12','18'],'B','x + y’nin alabileceği farklı değerlerin sayısı.',
 ['18√3’ü tek kök altında yaz.','x² × y bu sayıya eşit olmalı; x² hangi tam kareler olabilir?','Toplamları yaz ve aynı çıkanları bir kez say.'],[SOK,B('Kare bölen','n’yi bölen tam karelerdir. Örnek: 108’in kare bölenleri 1, 4, 9, 36')],
 [A('Tek köke getir','18’in karesi 324.','18√3 = √(324 × 3) = √972 ⇒ x² × y = 972'),
  A('Kare bölenler','972 = 2² × 3⁵.','x² ∈ {1, 4, 9, 36, 81, 324} ⇒ x ∈ {1, 2, 3, 6, 9, 18}'),
  A('İkilileri yaz','y = 972 ÷ x².','(1, 972) (2, 243) (3, 108) (6, 27) (9, 12) (18, 3)'),
  A('Toplamlar','9 + 12 = 21 ve 18 + 3 = 21 aynı.','973; 245; 111; 33; 21; 21'),
  A('Farklı olanları say','Altı ikili, beş farklı toplam.','5 farklı değer')],
 'Sade biçim verilse de önce tek köke çevir; diğer biçimler kök içinin kare bölenlerinden çıkar.',
 dict(A='4, x = 1 durumunu (1√972) saymamak.',C='6, altı ikiliyi saymak; 9 + 12 ile 18 + 3 aynı toplamı verir.',D='12, her ikiliyi ters sırayla da saymak; x√y ile y√x farklı sayılardır.',E='18, x’in alabileceği en büyük değer; soru farklı toplamların sayısını soruyor.'),
 TT(A='dikkat',C='dikkat',D='bilgi',E='dikkat'))

# ===== 0008 ZOR kk-eslenik (K-KK-05)
x=Q(2,1,5); ix=x.inv(); assert ix==Q(-2,1,5) and x+ix==Q(0,2,5) and x*x+ix*ix==18 and (x+ix)*(x+ix)==20 and (x-ix)*(x-ix)==16
assert 16-2==14 and 20+2==22 and artan(2*5**.5,14,18,20,22)
P.R('0008','kk-eslenik','Eşlenik ve paydayı rasyonel yapma','zor','x + 1/x','Köklü bir sayının çarpmaya göre tersini eşlenikle bulur, x² + 1/x² değerini tam kare özdeşliğiyle hesaplar.','düz',4,
 'K-KK-05 (1/x eşlenikle, x² + 1/x² = (x + 1/x)² − 2) · x = √5 + 2',
 'x = √5 + 2\nolduğuna göre x² + 1/x² ifadesinin değeri kaçtır?',
 ['2√5','14','18','20','22'],'C','x² + 1/x² ifadesinin değeri.',
 ['1/x’i eşlenikle hesapla: 1/(√5 + 2) = ?','x + 1/x sade bir sayı çıkıyor mu?','(x + 1/x)² açılımında x × 1/x terimi neye eşit?'],[ES,B('Tam kare açılımı','(a + b)² = a² + 2ab + b². a = x, b = 1/x için 2ab = 2: (x + 1/x)² = x² + 2 + 1/x²')],
 [A('1/x’i bul','Payı ve paydayı √5 − 2 ile çarp; payda 5 − 4 = 1.','1/x = (√5 − 2) ÷ ((√5 + 2) × (√5 − 2)) = √5 − 2'),
  A('Toplamı yaz','2 ile −2 sadeleşir.','x + 1/x = (√5 + 2) + (√5 − 2) = 2√5'),
  A('Karesini al','(x + 1/x)² = x² + 2 + 1/x².','(2√5)² = 20 ⇒ x² + 2 + 1/x² = 20'),
  A('Sonuç','2’yi çıkar.','x² + 1/x² = 20 − 2 = 18')],
 'x² + 1/x² istenince doğrudan kare alma; önce x + 1/x’i bul, karesinden 2 çıkar.',
 dict(A='2√5, x + 1/x’in değeri; soru x² + 1/x²’yi soruyor.',B='14, x − 1/x = 4’ün karesinden 2 çıkarmak; (x − 1/x)² = x² − 2 + 1/x², yani 2 eklenmeli.',D='20, (x + 1/x)²’yi cevap sanmak; içinde 2 × x × 1/x = 2 vardır.',E='22, (x + 1/x)²’ye 2 eklemek; 2 çıkarılmalı.'),
 TT(A='dikkat',B='islem',D='bilgi',E='islem'))
s6=6**.5; xk=s7-s6; ik=1/xk
assert abs(ik-(s7+s6))<1e-12 and abs(xk+ik-2*s7)<1e-12 and abs(xk*xk+ik*ik-26)<1e-9 and abs((xk-ik)**2-24)<1e-9 and 7-6==1
assert artan(2*s7,22,24,26,28)
P.K('0008','x = √7 − √6\nolduğuna göre x² + 1/x² toplamı kaçtır?',
 ['2√7','22','24','26','28'],'D','x² + 1/x² ifadesinin değeri.',
 ['1/(√7 − √6)’yı eşlenikle hesapla.','x + 1/x’te √6’lı terimler ne olur?','(x + 1/x)² = x² + 2 + 1/x².'],[ES,B('Tam kare açılımı','(a + b)² = a² + 2ab + b². a = x, b = 1/x için 2ab = 2: (x + 1/x)² = x² + 2 + 1/x²')],
 [A('1/x’i bul','Payı ve paydayı √7 + √6 ile çarp; payda 7 − 6 = 1.','1/x = √7 + √6'),
  A('Toplamı yaz','√6’lar sadeleşir.','x + 1/x = (√7 − √6) + (√7 + √6) = 2√7'),
  A('Karesini al','Açılımdaki orta terim 2.','(2√7)² = 28 ⇒ x² + 2 + 1/x² = 28'),
  A('Sonuç','2’yi çıkar.','x² + 1/x² = 28 − 2 = 26')],
 'Eşlenik çarpımı 1 olan köklü sayılarda 1/x eşleniğin kendisidir; x + 1/x hemen sadeleşir.',
 dict(A='2√7, x + 1/x’in değeri; soru x² + 1/x²’yi soruyor.',B='22, (x − 1/x)² = 24’ten 2 çıkarmak; x² + 1/x² = (x − 1/x)² + 2.',C='24, (x − 1/x)²’yi cevap sanmak; 2 eklenmeli.',E='28, (x + 1/x)²’yi cevap sanmak; 2 çıkarılmalı.'),
 TT(A='dikkat',B='islem',C='bilgi',E='bilgi'))

P.yaz(os.path.join(H,'koklu-1.json'),os.path.join(H,'koklu-1-kardes.json'))
