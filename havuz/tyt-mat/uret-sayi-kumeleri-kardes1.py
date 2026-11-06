"""Kardeş sorular (parti 1 + prototip): 0001k–0012k, 0019k, 0024k. Kodla doğrulanır."""
import json,sys,os
from itertools import product,permutations
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
# ---- 0001k
v=[n for n in range(100,1000) if '0' not in str(n) and dp(n)==2*ds(n)]; assert len(v)==15 and sorted({''.join(sorted(str(n))) for n in v})==['138','145','224']
for b in range(3,10):
    for c in range(b,10):
        if (b-2)*(c-2)==6: pass
assert [(b,c) for b in range(1,10) for c in range(b,10) if (b-2)*(c-2)==6]==[(3,8),(4,5)] and [(b,c) for b in range(2,10) for c in range(b,10) if (b-1)*(c-1)==3]==[(2,4)]
K('0001','Rakamları sıfırdan farklı bir doğal sayının rakamları çarpımı, rakamları toplamının 2 katına eşitse bu sayıya çifte sayı denir.\nÖrneğin 36 bir çifte sayıdır, çünkü 3 × 6 = 18 = 2 × (3 + 6)’dır.\nBuna göre üç basamaklı kaç tane çifte sayı vardır?',
 ['12','15','18','21','24'],'B','Rakamları çarpımı, rakamları toplamının 2 katı olan üç basamaklı sayıların adedi.',
 ['Rakamları küçükten büyüğe a ≤ b ≤ c diye sırala ve a = 1’den başla.','a = 1 için b × c = 2(1 + b + c) eşitliğini düzenle.','Bulduğun rakam kümelerinin kaç farklı sıralanışı var? Aynı rakam varsa dikkat.'],
 [B('Rakam','0’dan 9’a kadar olan sembollerdir; sayılar rakamlarla yazılır'),B('Sıralanış sayısı','farklı üç rakam 6 farklı sırada yazılır; ikisi aynıysa 3 farklı sırada')],
 [A('Tanımı anla','Çifte sayıda rakamları çarpımı, toplamlarının **2 katı**dır. Örnekteki 36 için 18 = 2 × 9.','3 × 6 = 18 · 2 × (3 + 6) = 18'),
  A('En küçük rakam 1 olsun','Rakamlar 1, b, c olsun: b × c = 2(1 + b + c). Her şeyi bir tarafa toplayıp çarpanlara ayırınca (b − 2)(c − 2) = 6 olur.','(b − 2)(c − 2) = 6 ⇒ {3, 8} veya {4, 5}'),
  A('En küçük rakam 2 olsun','Rakamlar 2, b, c (b ≥ 2) olsun: 2bc = 2(2 + b + c), yani (b − 1)(c − 1) = 3.','b = 2, c = 4 ⇒ {2, 2, 4}'),
  A('Daha büyük rakamlar','En küçük rakam 3 veya fazlaysa çarpım, toplamın 2 katını hep geçer (3, 3, 3 için 27 > 18).','başka küme yok'),
  A('Sıralanışları say','{1, 3, 8} ve {1, 4, 5} 6’şar, {2, 2, 4} ise 3 farklı sayı verir.','6 + 6 + 3 = 15')],
 'Rakam koşullu “kaç sayı” sorularında rakamları sıraya koyup en küçükten başla; sonra sıralanışları say.',
 dict(A='12 için {2, 2, 4} kümesini unutmuşsun; o da 3 sayı verir.',C='{2, 2, 4} kümesini 6 sayı saymışsın; iki rakam aynı olduğu için 3 farklı sayı var.',D='Bazı sayıları iki kez saymışsın; kümeler {1, 3, 8}, {1, 4, 5}, {2, 2, 4}.',E='24 için her kümeyi 6 farklı sayı saymış ve fazladan sayı eklemişsin.'))
# ---- 0002k (prototip)
cs=[(a,b,c) for a,b,c in product([0,1],repeat=3) if (a+b*c)%2==1 and (a*c+b)%2==0]; assert cs==[(1,0,0)]
K('0002','a, b ve c pozitif tam sayılar olmak üzere\na + b × c bir tek sayı,\na × c + b bir çift sayıdır.\nBuna göre\nI. a + c\nII. b × c\nIII. a + b + c\nifadelerinden hangileri her zaman tek sayıdır?',
 ['Yalnız I','Yalnız III','I ve II','I ve III','I, II ve III'],'D','Verilen iki koşula göre her zaman tek olan ifadeler.',
 ['a’nın çift olduğunu varsay; ikinci koşuldan b için ne çıkar?','a’nın tek olduğu belli olunca c’nin tek olup olamayacağını dene.','a, b, c’nin tek/çift durumunu bulunca öncülleri tek tek dene.'],[TEK,CARP],
 [A('a çift olsaydı?','a × c çift olur; a × c + b çift olduğundan b de çift olur. O zaman a + b × c = çift + çift = **çift** çıkar, ama tek olmalıydı.','çelişki ⇒ a tek'),
  A('c’yi bul','c tek olsaydı a × c tek, b de tek olurdu; o zaman a + b × c = tek + tek = çift çıkardı ✗. O hâlde **c çift**.','c çift'),
  A('b’yi bul','a × c çift (c çift) ve a × c + b çift ⇒ **b çift**.','b çift'),
  A('İfadeleri dene','a tek, b çift, c çift: a + c tek, b × c çift, a + b + c tek.','I ve III tek')],
 '“Her zaman tek/çift” sorularında bir harfi varsayıp çelişki aramak en hızlı yoldur.',
 dict(A='III de her zaman tek: a tek, b ve c çift.',B='I de her zaman tek: tek + çift = tek.',C='b × c çift; II her zaman tek değil.',E='b × c çifttir; II her zaman tek değil.'),
 kisa='a’yı çift varsay, çelişki çıkınca a tek; sonra c’yi dene. İki denemede bütün durum belli olur.')
# ---- 0003k
assert Fr('4.8')/8*2==Fr('1.2') and Fr('4.8')/12*4==Fr('1.6')
K('0003','Bir duvarın 4,8 metrelik bölümüne, iki uca da birer tane gelecek şekilde eşit aralıklarla 9 askı takılmıştır. Aynı bölümün altına yine iki uca da birer tane gelecek şekilde eşit aralıklarla 13 kanca çakılmıştır.\nBuna göre soldan 3. askı ile soldan 5. kanca arasındaki yatay uzaklık kaç metredir?',
 ['0,2','0,3','0,4','0,5','0,6'],'C','3. askı ile 5. kancanın sol uca uzaklıklarının farkı.',
 ['9 askı arasında kaç aralık vardır?','3. askı soldan kaç aralık ötededir?','Aynı hesabı 13 kanca için yap.'],
 [B('Uçlar dahil dizilim','n tane nesne arasında n − 1 aralık vardır. Örnek: 3 askı ⇒ 2 aralık')],
 [A('Askı aralığı','9 askı arasında **8** aralık vardır.','4,8 ÷ 8 = 0,6 m'),
  A('3. askının yeri','3. askıya gelmek için **2** aralık geçilir.','2 × 0,6 = 1,2 m'),
  A('Kanca aralığı','13 kanca arasında **12** aralık vardır.','4,8 ÷ 12 = 0,4 m'),
  A('5. kancanın yeri','5. kancaya gelmek için **4** aralık geçilir.','4 × 0,4 = 1,6 m'),
  A('Farkı al','İki konumun farkı istenen uzaklıktır.','1,6 − 1,2 = 0,4 m',G.iki_sira('4.8',9,3,13,5,'askılar','kancalar'))],
 'Uçlar dahilse aralık sayısı nesne sayısının 1 eksiğidir; k. nesne k − 1 aralık ötededir.',
 dict(A='0,2 için konumlardan birini bir aralık kaydırmış olabilirsin; 3. askı 2, 5. kanca 4 aralık ötede.',B='Aralık sayısını nesne sayısı kadar almışsın; 9 askı ⇒ 8 aralık.',D='Konumları yeniden hesapla: 1,2 m ve 1,6 m.',E='0,6 m bir askı aralığıdır; soru iki konumun farkını soruyor.'),
 kisa='k. nesnenin yeri = (k − 1) × aralık: 2 × 0,6 = 1,2 ve 4 × 0,4 = 1,6; aralıkları ayrı ayrı yazmana gerek yok.')
# ---- 0004k gösterge
def gost():
    x0,step,y=24,24,62; s=[f'<line x1="{x0}" y1="{y}" x2="{x0+step*12}" y2="{y}" stroke-width="2"/>']
    for i in range(13): h=16 if i in (0,6,12) else 9; s.append(f'<line x1="{x0+i*step}" y1="{y}" x2="{x0+i*step}" y2="{y-h}" stroke-width="2"/>')
    s.append(f'<text x="{x0}" y="{y+22}" text-anchor="middle" style="fill:currentColor;stroke:none" font-size="16">20</text><text x="{x0+6*step}" y="{y+22}" text-anchor="middle" style="fill:currentColor;stroke:none" font-size="16">50</text>')
    px=x0+9*step; s.append(f'<path d="M{px} {y+4} L{px-7} {y+20} L{px+7} {y+20} Z" style="fill:#e53935;stroke:#e53935"/>')
    return '<svg viewBox="0 0 340 100" xmlns="http://www.w3.org/2000/svg" fill="none" stroke="currentColor" font-family="Plus Jakarta Sans,system-ui,sans-serif">'+''.join(s)+'</svg>'
assert 20+9*Fr(30,6)==65
K('0004','Bir aracın hız göstergesinin bir bölümü aşağıda verilmiştir. Gösterge eşit aralıklarla bölmelenmiştir ve kırmızı ok aracın o anki hızını göstermektedir.\nBuna göre aracın o anki hızı saatte kaç kilometredir?',
 ['50','55','60','65','70'],'D','Okun gösterdiği hız.',
 ['20 ile 50 arasında kaç aralık var?','Bir aralık kaç birime karşılık geliyor?','Ok 20’den kaç aralık sağda?'],
 [B('Eşit bölmeli gösterge','her küçük aralık aynı değeri gösterir')],
 [A('Etiketleri bul','Göstergede yazılı iki değer var: 20 ve 50.','20 ve 50'),
  A('Aralıkları say','20 ile 50 arasındaki **boşlukları** say (çizgileri değil): 6 aralık var.','6 aralık'),
  A('Bir aralığın değeri','30 birimlik fark 6 eşit aralığa bölünmüş.','(50 − 20) ÷ 6 = 5'),
  A('Okun değeri','Ok, 20’den başlayarak **9** aralık sağda.','20 + 9 × 5 = 65')],
 'Bölme sayısını bulurken çizgileri sayarsan bir fazla bulursun; iki çizgi arasındaki aralıkları say.',
 dict(A='50 etiketli çizginin değeri; ok, 50’nin 3 aralık sağında.',B='55 için ok 7 aralık sağda olmalıydı; ok 20’den 9 aralık sağda.',C='60 için okun yerini bir aralık eksik saymışsın: ok 20’den 9 aralık sağda.',E='70 için 10 aralık saymışsın; 20’deki çizgi sayılmaz.'),sekil=gost())
# ---- 0005k (prototip)
assert {p[6] for p in permutations([3,4,5,6,7,11,12]) if p[0]*p[1]==p[2] and p[3]+p[4]==p[5]}=={7}
K('0005','3, 4, 5, 6, 7, 11 ve 12 sayılarından altısı, her kutuya farklı bir sayı gelecek şekilde aşağıdaki kutulara yazılıyor ve iki eşitlik de sağlanıyor.\n□ × □ = □\n□ + □ = □\nBuna göre kutulara yazılmayan sayı kaçtır?',
 ['3','4','5','6','7'],'E','İki eşitliğe yerleşmeyen tek sayı.',
 ['Önce çarpma eşitliğine bak; sonucu da listede olan çarpım hangisi?','Çarpmada kullanılan sayıları çıkar.','Kalan dört sayıdan toplama eşitliğini kur.'],[],
 [A('Kaç sayı dışarıda?','7 sayıdan 6’sı kutulara yazılır; **1** sayı dışarıda kalır.','7 − 6 = 1'),
  A('Çarpmayı dene','Çarpımın sonucu da listede olmalı: 3 × 4 = 12 var; 3 × 5 = 15, 4 × 5 = 20 gibi diğerleri yok.','3 × 4 = 12'),
  A('Kalanları yaz','3, 4 ve 12 kullanıldı.','kalanlar: 5, 6, 7, 11'),
  A('Toplamayı dene','5 + 6 = 11 uyuyor (5 + 7 = 12 ve 6 + 7 = 13; 12 kullanıldı, 13 yok).','5 + 6 = 11 ⇒ dışarıda 7')],
 'En sıkı kısıt çarpmadadır; önce onu yerleştir.',
 dict(A='3, 3 × 4 = 12 eşitliğinde kullanılıyor.',B='4, 3 × 4 = 12 eşitliğinde kullanılıyor.',C='5, 5 + 6 = 11 eşitliğinde kullanılıyor.',D='6, 5 + 6 = 11 eşitliğinde kullanılıyor.'))
# ---- 0006k
assert [(a,b) for a in range(1,10) for b in range(1,10) if 11*(a+b)==99 and 9*(a-b)==45]==[(7,2)]
K('0006','Mert’in otobüs bileti üzerindeki koltuk numarası iki basamaklı AB sayısı, Selin’inki ise iki basamaklı BA sayısıdır.\nİki koltuk numarasının toplamı 99’dur ve Mert’in koltuk numarası Selin’inkinden 45 fazladır.\nBuna göre A × B çarpımı kaçtır?',
 ['14','18','20','24','27'],'A','A ve B rakamlarının çarpımı.',
 ['AB’yi 10A + B biçiminde yaz.','Toplamdan A + B’yi, farktan A − B’yi bul.','İki denklemi taraf tarafa topla.'],[IKI],
 [A('Numaraları aç','AB ve BA sayılarını basamaklarına ayırarak yaz.','AB = 10A + B · BA = 10B + A'),
  A('Toplamı kullan','İki numarayı topla: 11A + 11B = 99. İki tarafı 11’e böl.','A + B = 9'),
  A('Farkı kullan','Mert’inkinden Selin’inkini çıkar: 9A − 9B = 45. İki tarafı 9’a böl.','A − B = 5'),
  A('A ve B’yi bul','İki denklemi topla: 2A = 14, yani **A = 7**; o zaman **B = 2**. Kontrol: 72 + 27 = 99, 72 − 27 = 45.','A = 7 · B = 2'),
  A('Çarp','İstenen A × B.','7 × 2 = 14')],
 'Yer değiştiren iki basamaklı sayılarda toplam hep 11’in, fark hep 9’un katıdır.',
 dict(B='18 = 6 × 3 ya da 9 × 2; bu rakamlarla fark 45 olmaz.',C='20 = 5 × 4; 54 − 45 = 9, fark 45 değil.',D='24 = 8 × 3 ya da 6 × 4; bunların toplamı 9 etmez.',E='27 = 9 × 3; 93 + 39 = 132, toplam 99 değil.'),
 kisa='A + B = 9 ve A − B = 5 olunca: A = (9 + 5) ÷ 2 = 7, B = (9 − 5) ÷ 2 = 2.')
# ---- 0007k
sol=[n for n in range(10,100) if ds(dp(n))==3 and dp(ds(n))==1]; assert sol==[56,65]
K('0007','Bir doğal sayı için ⟨n⟩ gösterimi n’nin rakamları toplamını, [n] gösterimi ise n’nin rakamları çarpımını ifade etmektedir.\nİki basamaklı AB sayısı için\n⟨[AB]⟩ = 3 ve [⟨AB⟩] = 1\nolduğuna göre AB’nin alabileceği değerlerin toplamı kaçtır?',
 ['56','65','112','121','130'],'D','İki koşulu birlikte sağlayan iki basamaklı sayıların toplamı.',
 ['İkinci koşuldan başla: ⟨AB⟩ = A + B; rakamları çarpımı 1 olan sayılar hangileri?','A + B’yi bulunca o toplamı veren iki basamaklı sayıları yaz.','Bu sayılardan birinci koşulu sağlayanları seç ve topla.'],
 [IKI,B('Gösterimler','⟨n⟩: rakamları topla, ⟨35⟩ = 8 · [n]: rakamları çarp, [35] = 15')],
 [A('İçten dışa çalış','⟨[AB]⟩ yazısında önce içteki [AB] yapılır, sonra dıştaki ⟨ ⟩.','önce iç, sonra dış'),
  A('İkinci koşul','[A + B] = 1 olması için A + B’nin rakamları çarpımı 1 olmalı: A + B = 1 ya da 11. AB iki basamaklı olduğundan A + B = 1 olamaz.','A + B = 11'),
  A('Adayları yaz','Rakamları toplamı 11 olan iki basamaklı sayılar ve rakam çarpımları.','29, 38, 47, 56, 65, 74, 83, 92 · çarpımlar: 18, 24, 28, 30, 30, 28, 24, 18'),
  A('Birinci koşul','Çarpımın rakamları toplamı 3 olmalı: yalnızca 30 (3 + 0 = 3).','AB = 56 veya 65'),
  A('Topla','İki değeri topla.','56 + 65 = 121')],
 'İki koşullu sembol sorularında daha az aday bırakan koşuldan başla.',
 dict(A='56 tek başına bir değer; soru değerlerin toplamını soruyor.',B='65 tek başına bir değer; 56 da koşulları sağlıyor.',C='112 = 2 × 56; iki farklı değer var: 56 ve 65.',E='130 = 2 × 65; iki farklı değer var: 56 ve 65.'),
 kisa='[⟨AB⟩] = 1 ⇒ A + B = 11; bu sayılardan rakam çarpımı 30 olanlar 56 ve 65. Toplamı bulmak için sadece 30 = 5 × 6 olduğunu görmen yeter.')
# ---- 0008k (prototip)
assert [x for x in range(1,99,2) if 4*x+12==5*x-3]==[15]
K('0008','Ardışık dört tek doğal sayının toplamı, bu sayıların en küçüğünün 5 katından 3 eksiktir.\nBuna göre bu sayıların en büyüğü kaçtır?',
 ['13','15','17','19','21'],'E','Dört ardışık tek sayının en büyüğü.',
 ['En küçük sayıya x de; diğerleri nasıl yazılır?','Dört sayının toplamını x cinsinden yaz.','Soru en büyüğü soruyor, x’i bulunca durma.'],[B('Ardışık tek sayılar','2’şer artar: 15, 17, 19, …')],
 [A('En küçüğe x de','Dört sayı 2’şer artar.','x, x + 2, x + 4, x + 6'),A('Topla','x’ler ve sayılar ayrı toplanır.','4x + (2 + 4 + 6) = 4x + 12'),
  A('Denklemi kur','Toplam, 5x’ten 3 eksik. İki taraftan 4x çıkar, sonra iki tarafa 3 ekle.','4x + 12 = 5x − 3 ⇒ x = 15'),A('En büyüğü bul','En büyük sayı x + 6.','15 + 6 = 21')],
 'Soru en büyüğü soruyorsa x’i bulunca durma.',
 dict(A='13 koşulu sağlamıyor; denklemi yeniden kur.',B='15 en küçük sayı; soru en büyüğü soruyor.',C='17 ikinci sayı; en büyük sayı x + 6.',D='19 üçüncü sayı; en büyük sayı x + 6.'))
# ---- 0009k
ok=lambda x:[x>Fr(1,3),x<Fr(2,5),x>Fr(3,8)].count(False)==1
ch=[Fr(n,120) for n in (36,38,42,46,47)]; assert [ok(x) for x in ch]==[0,0,1,0,0]
K('0009','Ece, Kaan ve Lale bir bardaktaki meyve suyunun bardağın kaçta kaçını doldurduğunu tahmin ediyor.\n• Ece: “1/3’ten fazla.”\n• Kaan: “2/5’ten az.”\n• Lale: “3/8’den fazla.”\nÖlçüm yapıldığında bu üç kişiden yalnızca birinin tahmininin yanlış olduğu görülüyor.\nBuna göre meyve suyu bardağın kaçta kaçını doldurmuş olabilir?',
 ['36/120','38/120','42/120','46/120','47/120'],'C','Üç tahminden tam olarak birini yanlış yapan oran.',
 ['Üç kesri paydası 120 olacak şekilde genişlet.','Sınırları sayı doğrusuna diz.','Her şık için kaç tahminin yanlış olduğunu say.'],
 [B('Kesir karşılaştırma','paydalar eşitse payı büyük olan kesir büyüktür. Örnek: 3/8 = 45/120')],
 [A('Paydaları eşitle','Üç kesri de paydası 120 olacak şekilde genişlet.','1/3 = 40/120 · 3/8 = 45/120 · 2/5 = 48/120'),
  A('Sınırları diz','Sayı doğrusunda sıralama.','40/120 < 45/120 < 48/120'),
  A('Şıkları dene','36 ve 38 için Ece ve Lale yanılır (**iki yanlış**). 46 ve 47 için kimse yanılmaz. 42 için yalnızca Lale yanılır (**tek yanlış**).','42/120 ✓',G.sayi_dogrusu(120,[(40,'1/3'),(45,'3/8'),(48,'2/5')],(42,'42/120'),a=34,bt=50))],
 'Kesirleri ortak paydaya getirip sayı doğrusuna dizmek, “kaç ifade doğru” sorularını tek bakışta çözer.',
 dict(A='36/120, 1/3’ten küçük: hem Ece hem Lale yanılmış olur.',B='38/120, 1/3’ten küçük: hem Ece hem Lale yanılmış olur.',D='46/120 ile üç tahmin de doğru çıkar; birinin yanlış olması gerekiyordu.',E='47/120 ile üç tahmin de doğru çıkar; birinin yanlış olması gerekiyordu.'),
 kisa='Sınırlar 40, 45, 48 (payda 120). Tek yanlış için sayı ya 40 ile 45 arasında ya da 48’in üstünde olmalı; şıklarda yalnızca 42 bu aralıkta.')
# ---- 0010k
assert 5*Fr(1,8)*Fr(1,2)==Fr(5,16)
K('0010','Bir pizza eş büyüklükte 8 dilime ayrılmıştır. Can bu dilimlerden 3 tanesini alıp her birini 2 eş parçaya bölmüş ve bu parçalardan 5 tanesini arkadaşlarına vermiştir.\nBuna göre Can’ın arkadaşlarına verdiği parçalar pizzanın kaçta kaçıdır?',
 ['1/8','5/16','3/8','1/2','5/8'],'B','Verilen 5 küçük parçanın pizzanın kaçta kaçı olduğu.',
 ['Bir dilim pizzanın kaçta kaçı?','Küçük bir parça bir dilimin kaçta kaçı?','Küçük parçanın pizzaya oranını 5 ile çarp.'],
 [B('Parçanın parçası','kesirleri çarparız: bir dilimin 1/2’si = 1/8 × 1/2')],
 [A('Bir dilim','Pizza 8 eş dilim; bir dilim pizzanın sekizde biri.','1/8'),
  A('Bir küçük parça','Bir dilim 2 eş parçaya bölünmüş.','1/8 × 1/2 = 1/16'),
  A('Beş parça','5 küçük parça verilmiş.','5 × 1/16 = 5/16',G.tepsi(8,3,2,5))],
 'Parçanın parçası soruluyorsa kesirleri çarp; “3 dilim aldı” bilgisi sonucu etkilemez, dikkat dağıtır.',
 dict(A='1/8 bir dilimin oranı; verilen 5 küçük parça.',C='3/8, Can’ın aldığı 3 dilimin oranı; verilen daha az.',D='1/2 için dilimleri ikiye bölmeden 4 dilim saymış olabilirsin; bir küçük parça 1/16.',E='5/8 için parçaları bölmeden 5 dilim saymışsın.'))
# ---- 0011k
assert Fr('100')-(Fr('32.80')*Fr('1.5')+Fr('9.60')*Fr('2.5'))==Fr('26.8')
K('0011','Bir manavda kirazın kilogramı 32,80 TL, elmanın kilogramı 9,60 TL’dir.\nBurak bu manavdan 1,5 kg kiraz ve 2,5 kg elma alıp kasaya 100 TL vermiştir.\nBuna göre Burak’ın alacağı para üstü kaç TL’dir?',
 ['26,8','27,3','27,8','28,3','28,8'],'A','100 TL’den alışveriş tutarının farkı.',
 ['Kiraz tutarını bul: 32,80 × 1,5.','Elma tutarını bul: 9,60 × 2,5.','Toplamı 100’den çıkar.'],
 [B('Tutar','birim fiyat × miktar')],
 [A('Kiraz tutarı','32,80 × 1,5 = 32,80’in kendisi + yarısı.','32,80 + 16,40 = 49,20'),
  A('Elma tutarı','9,60 × 2,5’i ikiye ayır: 2 kg ve 0,5 kg.','9,60 × 2 = 19,20 · 9,60 × 0,5 = 4,80 ⇒ 24'),
  A('Toplam tutar','İki tutarı topla.','49,20 + 24 = 73,20'),
  A('Para üstü','100 TL’den toplam tutarı çıkar.','100 − 73,2 = 26,8')],
 '× 2,5 için “× 10 ÷ 4”, × 1,5 için “kendisi + yarısı” kısayolunu kullan.',
 dict(B='Kiraz tutarını 49,20 yerine 48,70 almışsın; 32,80 × 1,5 = 49,20.',C='Elma tutarını 24 yerine 23 almış olabilirsin; tutarları yeniden hesapla.',D='Toplamı yeniden hesapla: 49,20 + 24 = 73,20.',E='Elma tutarını 2,5 kg yerine 2,4 kg ile hesaplamış olabilirsin; tutarları yeniden hesapla.'),
 kisa='9,60 × 2,5 = 96 ÷ 4 = 24 (× 2,5 = × 10 ÷ 4); 32,80 × 1,5 = 32,80 + 16,40.')
# ---- 0012k
t=(23*60+40)%60; assert t==40 and t-25==15
K('0012','Bir yaya geçidindeki ışık sırasıyla 25 saniye yeşil ve 35 saniye kırmızı yanmakta ve bu düzen hiç bozulmadan tekrar etmektedir.\nSaat 10.00.00’da ışıkta yeşil yeni yanmıştır.\nBuna göre saat 10.23.40’ta ışıkta hangi renk yanmaktadır ve bu renk kaç saniyedir yanmaktadır?',
 ['Yeşil – 15 saniye','Yeşil – 25 saniye','Kırmızı – 10 saniye','Kırmızı – 15 saniye','Kırmızı – 40 saniye'],'D','10.23.40’ta yanan renk ve o rengin kaçıncı saniyesinde olunduğu.',
 ['Bir tam turun süresini bul.','Geçen süreyi saniyeye çevir.','Geçen süreyi tur süresine böl, kalana bak.'],
 [B('Tekrar eden düzen','tam turlar sonucu değiştirmez; yalnızca artan (kalan) süreye bakılır')],
 [A('Bir tur','Yeşil ve kırmızı sürelerini topla.','25 + 35 = 60 sn'),
  A('Geçen süre','10.00.00’dan 10.23.40’a 23 dakika 40 saniye geçer.','23 × 60 + 40 = 1420 sn'),
  A('Tam turları at','Bir tur tam 1 dakika; 23 tam tur atılınca 40 saniye kalır.','1420 − 23 × 60 = 40 sn'),
  A('Turun içinde yer','Bir turda 0–25 yeşil, 25–60 kırmızı. 40. saniye kırmızıdadır.','25 < 40 < 60 ⇒ kırmızı',G.zaman_seridi([(25,'yeşil','#16A34A'),(35,'kırmızı','#D93636')],40,'40. sn')),
  A('Kaç saniyedir yanıyor?','Kırmızı 25. saniyede yandı.','40 − 25 = 15 sn')],
 'Döngü sorularında tam turları at, sadece kalanla çalış; kalanı hangi aralığa düştüğüne göre oku.',
 dict(A='40. saniye yeşilde değil; yeşil yalnızca 0–25 arası.',B='Yeşil 25 saniyede biter; 40. saniye kırmızıdadır.',C='Kırmızı 25. saniyede başladı: 40 − 25 = 15.',E='40 turun içindeki konum; kırmızı 25. saniyede başladığından 15 saniyedir yanıyor.'),
 kisa='Tur tam 60 saniye olduğundan dakikaları at: sadece 40 saniyeye bak. 40 − 25 = 15.')
# ---- 0019k, 0024k (prototip)
P=[p for p in range(2,40) if all(p%d for d in range(2,int(p**.5)+1))]
s=[(a,b,c) for a in P for b in P for c in P if a<b and a*b+c==29]; assert sorted(map(sum,s))==[18,20,26,28]
K('0019','x, y ve z asal sayılar ve x < y olmak üzere\nx · y + z = 29\nolduğuna göre x + y + z toplamı en az kaçtır?',
 ['18','20','26','28','30'],'A','Denklemi sağlayan asal üçlüler arasında en küçük toplam.',
 ['29 tek; x · y ile z’den biri çift olmalı.','Çift olan tek asal sayı hangisi?','Her durumu ayrı ayrı yazıp toplamları karşılaştır.'],[ASAL,TEK],
 [A('Tek-çift dengesi','29 tek; x · y + z toplamında biri tek, biri çift olmalı.','tek = tek + çift'),
  A('Çift olan kim?','Çift asal yalnız 2. Ya z = 2 ya da x · y çift (x < y olduğundan x = 2).','z = 2 veya x = 2'),
  A('z = 2 durumu','x · y = 27 olmalı; 27 = 3 × 9 ve 9 asal değil. Bu durum olmaz.','z ≠ 2'),
  A('x = 2 durumu','2y + z = 29: y = 3 ⇒ z = 23; y = 5 ⇒ z = 19; y = 11 ⇒ z = 7; y = 13 ⇒ z = 3 (y = 7 için z = 15 asal değil).','toplamlar 28, 26, 20, 18'),
  A('En küçüğü seç','En küçük toplam 2 + 13 + 3.','18')],
 'Toplam tekse içlerinden biri 2’dir; sonra durumları tek tek yaz.',
 dict(B='20, x = 2, y = 11, z = 7 durumu; daha küçük toplam var.',C='26, x = 2, y = 5, z = 19 durumu; daha küçük toplam var.',D='28, x = 2, y = 3, z = 23 durumu; daha küçük toplam var.',E='30 veren bir asal üçlü yok.'),
 kisa='x = 2 iken toplam = 2 + y + (29 − 2y) = 31 − y; y büyüdükçe toplam küçülür. En büyük uygun y = 13 ⇒ 18.')
assert F(7)//F(5)+F(4)==66
K('0024','7!/5! + 4!\nişleminin sonucu kaçtır?',
 ['42','46','54','60','66'],'E','İşlemin sonucu.',
 ['7! ile 5! arasındaki ortak çarpanları düşün.','7!/5! = 7 × 6 olur.','4!’ü hesaplayıp ekle.'],[FAK],
 [A('7!/5!','7! = 7 × 6 × 5! olduğundan 5! sadeleşir.','7!/5! = 7 × 6 = 42'),A('4!','4 faktöriyel.','4! = 1 × 2 × 3 × 4 = 24'),A('Topla','İki sonucu topla.','42 + 24 = 66')],
 'Faktöriyel bölmesinde büyük faktöriyeli küçüğe kadar aç.',
 dict(A='42, yalnızca 7!/5!; 4!’ü eklemeyi unutmuşsun.',B='4! yerine 4 eklemişsin; 4! = 24.',C='54 = 42 + 12; 4!’ü 4 × 3 sanmışsın, 4! = 1 × 2 × 3 × 4 = 24.',D='60 = 42 + 18; 4!’ü yanlış hesaplamışsın, 4! = 24.'),
 kisa='7!/5! = 7 × 6: üstteki sayıdan başlayıp alttakine kadar (dahil değil) çarp.')
json.dump(OUT,open(os.path.join(H,'sayi-kumeleri-kardes1.json'),'w'),ensure_ascii=False,indent=1)
from collections import Counter; print(len(OUT),Counter(q['cevap']['sik'] for q in OUT))
