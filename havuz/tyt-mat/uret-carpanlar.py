"""Çarpanlara Ayırma · parti 1: 8 ana + 8 kardeş. Her cevap ve ara sonuç kodla doğrulanır."""
import sys,os,math
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,os.path.join(H,'..'))
from ortak import *
P=Parti('carpanlar','Çarpanlara Ayırma','mat|Çarpanlara Ayırma')
TT=lambda **k:k
IKF=B('İki kare farkı','a² − b² = (a − b) × (a + b). Örnek: 7² − 3² = 4 × 10 = 40')
TKO=B('Tam kare açılımları','(a + b)² = a² + 2ab + b² · (a − b)² = a² − 2ab + b². Örnek: (3 + 2)² = 9 + 12 + 4 = 25')
GRP=B('Gruplama','dört terimli ifadede ikişer terimi grupla, ortak çarpanı al. Örnek: ab + 2a + 3b + 6 = a(b + 2) + 3(b + 2) = (a + 3)(b + 2)')
TK=B('Tam kare üç terimli','a² + 2ab + b² = (a + b)². Örnek: x² + 6x + 9 = (x + 3)², çünkü 6x = 2 × x × 3')
SAD=B('Sadeleştirme','pay ve paydada aynı çarpan varsa (sıfırdan farklı olduğundan) sadeleşir. Örnek: (x + 1)(x − 2)/(x + 1) = x − 2')
TERS=B('x ile 1/x’in çarpımı','x × 1/x = 1 olduğundan (x + 1/x)² = x² + 2 + 1/x² ve (x − 1/x)² = x² − 2 + 1/x²')
def esit(f,g,haric):
    """iki rasyonel ifade tanım kümesindeki birçok değerde aynı mı"""
    return all(f(Fr(x,7))==g(Fr(x,7)) for x in range(-60,61) if Fr(x,7) not in haric)

# ===== 0001 KOLAY ca-ozdeslik (K-CA-01)
assert 103**2-97**2==1200==6*200 and 6**2==36 and 6+200==206 and 6*100==600 and 2*6*200==2400
P.R('0001','ca-ozdeslik','İki kare farkı ve tam kare özdeşlikleri','kolay','İki Kare Farkı','İki kare farkı özdeşliğiyle büyük sayıların kareleri farkını hesaplar.','düz',2,
 'K-CA-01 (iki kare farkıyla sayısal hesap) · yeni sayılar (103 ve 97)',
 '103² − 97²\nişleminin sonucu kaçtır?',
 ['36','206','600','1200','2400'],'D','İki karenin farkı.',
 ['Kareleri tek tek hesaplamak yerine bir özdeşlik kullan.','a² − b² hangi iki çarpana ayrılır?','103 − 97 ve 103 + 97 kaç eder?'],[IKF],
 [A('Özdeşliği tanı','a = 103, b = 97 olan iki kare farkı.','103² − 97² = (103 − 97) × (103 + 97)'),
  A('Çarpanları hesapla','Fark ve toplamı bul.','6 × 200 = 1200'),
  A('Kontrol','Kareleri hesaplayarak da aynı sonuç çıkar.','10 609 − 9409 = 1200 ✓')],
 'Büyük sayıların kareleri farkı istendiğinde kare alma; fark × toplam yap.',
 dict(A='36, a² − b²’yi (a − b)² sanmak; iki kare farkı (a − b) × (a + b)’dir.',B='206, iki çarpanı çarpmak yerine toplamak: 6 + 200.',C='600, 103 + 97’yi 100 almak; toplam 200’dür.',E='2400, tam kare açılımındaki 2’yi eklemek: 2 × 6 × 200; iki kare farkında 2 yoktur.'),
 TT(A='bilgi',B='islem',C='islem',E='bilgi'))
assert 58**2-42**2==1600==16*100 and 16**2==256 and 16+100==116 and 16*50==800
P.K('0001','58² − 42²\nfarkının değeri kaçtır?',
 ['16','116','256','800','1600'],'E','İki karenin farkı.',
 ['Kareleri hesaplamadan bir özdeşlikle çöz.','a² − b² = (a − b) × (a + b).','58 − 42 ve 58 + 42’yi bul, çarp.'],[IKF],
 [A('Özdeşliği tanı','a = 58, b = 42.','58² − 42² = (58 − 42) × (58 + 42)'),
  A('Çarpanları hesapla','Fark 16, toplam 100.','16 × 100 = 1600'),
  A('Kontrol','Kareler: 3364 ve 1764.','3364 − 1764 = 1600 ✓')],
 'Toplamı yuvarlak sayı (100, 200) olan iki sayının kareleri farkı, iki kare farkıyla bir çarpmaya iner.',
 dict(A='16, yalnızca a − b’yi bulmak; a + b ile de çarpılmalı.',B='116, iki çarpanı toplamak: 16 + 100.',C='256, a² − b²’yi (a − b)² sanmak.',D='800, a + b’yi 50 almak; 58 + 42 = 100.'),
 TT(A='dikkat',B='islem',C='bilgi',D='islem'))

# ===== 0002 KOLAY ca-ortak (K-CA-03)
x,y=17,8; assert x*y-3*x+2*y-6==(x+2)*(y-3)==95
assert x*y-3*x-2*y-6==63 and x*y-3*x+2*y+6==107 and (x-3)*(y+2)==140 and (x+2)*(y+3)==209
P.R('0002','ca-ortak','Ortak çarpan ve gruplama','kolay','Gruplama','Dört terimli ifadeyi gruplayarak çarpanlarına ayırır ve değerini hesaplar.','düz',2,
 'K-CA-03 (gruplama ile iki çarpan) · sayı yerine koymadan önce çarpanlara ayırma',
 'x = 17 ve y = 8 olmak üzere\nxy − 3x + 2y − 6\nifadesinin değeri kaçtır?',
 ['63','95','107','140','209'],'B','İfadenin değeri.',
 ['İlk iki terimde ve son iki terimde ortak çarpan ne?','x(y − 3) + 2(y − 3) biçimine getir.','Çarpanlara ayırdıktan sonra sayıları yerine koy.'],[GRP],
 [A('Grupla','İlk iki terimde x, son iki terimde 2 ortak.','xy − 3x + 2y − 6 = x(y − 3) + 2(y − 3)'),
  A('Ortak çarpan','(y − 3) iki grupta da var.','= (x + 2) × (y − 3)'),
  A('Yerine koy','x = 17, y = 8.','(17 + 2) × (8 − 3) = 19 × 5 = 95')],
 'Sayı verilen uzun ifadelerde önce çarpanlara ayır; sonra küçük sayıları çarp.',
 dict(A='63, +2y’yi −2y almak; işaret korunmalı.',C='107, −6’yı +6 almak.',D='140, terimleri ters eşleştirip (x − 3) × (y + 2) yazmak.',E='209, ikinci çarpanı (y + 3) almak; 2(y − 3) = 2y − 6.'),
 TT(A='dikkat',C='dikkat',D='islem',E='islem'))
a,b=23,9; assert a*b+4*a-3*b-12==(a-3)*(b+4)==260
assert (a+4)*(b-3)==162 and a*b+4*a-3*b+12==284 and (a+3)*(b+4)==338 and (a-3)*(b-4)==100
P.K('0002','a = 23 ve b = 9 için\nab + 4a − 3b − 12\nifadesinin değeri kaçtır?',
 ['100','162','260','284','338'],'C','İfadenin değeri.',
 ['İlk iki terimde ve son iki terimde ortak çarpan ne?','a(b + 4) − 3(b + 4) biçimine getir.','Sonra sayıları yerine koy.'],[GRP],
 [A('Grupla','İlk iki terimde a, son iki terimde −3 ortak.','ab + 4a − 3b − 12 = a(b + 4) − 3(b + 4)'),
  A('Ortak çarpan','(b + 4) iki grupta da var.','= (a − 3) × (b + 4)'),
  A('Yerine koy','a = 23, b = 9.','(23 − 3) × (9 + 4) = 20 × 13 = 260')],
 'Gruplamada ortak çarpanı eksiyle birlikte dışarı al: −3b − 12 = −3(b + 4).',
 dict(A='100, ikinci çarpanı (b − 4) almak; işaret hatası.',B='162, terimleri ters eşleştirip (a + 4) × (b − 3) yazmak.',D='284, −12’yi +12 almak.',E='338, ilk çarpanı (a + 3) almak; −3(b + 4) = −3b − 12.'),
 TT(A='islem',B='islem',D='dikkat',E='islem'))

# ===== 0003 ORTA ca-sadelestirme (K-CA-05)
F=lambda x:(x*x-9)/(x*x+6*x+9)*(x*x+3*x)/(x-3); H0={-3,0,3}
assert esit(F,lambda x:x,H0)
assert esit(lambda x:(x-3)*(x+3)/((x+3)*(x-3))*x*(x+3)/(x-3),lambda x:x*(x+3)/(x-3),H0)   # E: tam kareyi iki kare farkı sanmak
assert esit(lambda x:(x-3)**2/(x+3)**2*x*(x+3)/(x-3),lambda x:x*(x-3)/(x+3),H0)              # D: x² − 9 = (x − 3)² sanmak
assert esit(lambda x:(x-3)*(x+3)/(x+3)**2*x/(x-3),lambda x:x/(x+3),H0)                        # B: x² + 3x = x sanmak
P.R('0003','ca-sadelestirme','Rasyonel ifadeleri sadeleştirme','orta','Sadeleştirme','İki kare farkı, tam kare ve ortak çarpanı kullanarak rasyonel ifadeleri sadeleştirir.','düz',3,
 'K-CA-05 (her parçayı çarpanlarına ayırıp sadeleştirme) · iki kesrin çarpımı',
 'x ∉ {−3, 0, 3} olmak üzere\n(x² − 9)/(x² + 6x + 9) · (x² + 3x)/(x − 3)\nifadesinin en sade biçimi aşağıdakilerden hangisidir?',
 ['1','x/(x + 3)','x','x(x − 3)/(x + 3)','x(x + 3)/(x − 3)'],'C','İfadenin en sade biçimi.',
 ['Dört ifadenin her birini ayrı ayrı çarpanlarına ayır.','x² + 6x + 9 bir tam karedir; x² − 9 iki kare farkıdır.','Pay ve paydada aynı olan çarpanları sadeleştir.'],[IKF,TK,SAD],
 [A('Payları ayır','İki kare farkı ve ortak çarpan.','x² − 9 = (x − 3)(x + 3) · x² + 3x = x(x + 3)'),
  A('Paydaları ayır','6x = 2 × x × 3 olduğundan tam kare.','x² + 6x + 9 = (x + 3)² · x − 3 zaten çarpan'),
  A('Sadeleştir','Payda: (x + 3)² × (x − 3). Pay: (x − 3) × (x + 3) × x × (x + 3).','(x − 3) ve (x + 3)² sadeleşir ⇒ x')],
 'Rasyonel ifadede sadeleştirmeden önce her parçayı tamamen çarpanlarına ayır; yalnız çarpanlar sadeleşir.',
 dict(A='1, x² + 3x’ten (x + 3)’ü alıp x çarpanını unutmak.',B='x/(x + 3), x² + 3x’i x(x + 3) yerine yalnızca x almak.',D='x(x − 3)/(x + 3), x² − 9’u (x − 3)² sanmak; x² − 9 = (x − 3)(x + 3).',E='x(x + 3)/(x − 3), x² + 6x + 9’u (x + 3)(x − 3) sanmak; o ifade tam karedir: (x + 3)².'),
 TT(A='dikkat',B='islem',D='bilgi',E='bilgi'))
F=lambda x:(x*x-4*x)/(x*x-16)*(x*x+8*x+16)/(x*x); H0={-4,0,4}
assert esit(F,lambda x:(x+4)/x,H0)
assert esit(lambda x:x*(x-4)/((x-4)*(x+4))*(x+4)*(x-4)/(x*x),lambda x:(x-4)/x,H0)            # C: tam kareyi iki kare farkı sanmak
assert esit(lambda x:x*(x-4)/((x-4)*(x+4))*(x+4)/(x*x),lambda x:1/x,H0)                       # B: (x + 4)²’yi tek (x + 4) almak
assert esit(lambda x:x*(x-4)/((x-4)*(x+4))*(x+4)**2/x,lambda x:x+4,H0)                        # E: x²’yi x sanmak
P.K('0003','x ∉ {−4, 0, 4} olmak üzere\n(x² − 4x)/(x² − 16) · (x² + 8x + 16)/x²\nifadesi aşağıdakilerden hangisine eşittir?',
 ['x/(x + 4)','1/x','(x − 4)/x','(x + 4)/x','x + 4'],'D','İfadenin en sade biçimi.',
 ['Dört ifadeyi de çarpanlarına ayır.','x² + 8x + 16 tam kare mi, iki kare farkı mı?','Ortak çarpanları sadeleştir; paydadaki x²’nin tamamına dikkat.'],[IKF,TK,SAD],
 [A('Payları ayır','Ortak çarpan ve tam kare.','x² − 4x = x(x − 4) · x² + 8x + 16 = (x + 4)²'),
  A('Paydaları ayır','İki kare farkı.','x² − 16 = (x − 4)(x + 4) · x² = x × x'),
  A('Sadeleştir','(x − 4), bir (x + 4) ve bir x sadeleşir.','x × (x − 4) × (x + 4)² ÷ ((x − 4) × (x + 4) × x × x) = (x + 4)/x')],
 'Sadeleştirmeden sonra paydada ve payda kalan çarpanları tek tek say; kare olan çarpanlar iki kez sayılır.',
 dict(A='x/(x + 4), sonucu ters çevirmek; pay ile paydayı karıştırmak.',B='1/x, (x + 4)²’yi tek (x + 4) gibi almak.',C='(x − 4)/x, x² + 8x + 16’yı (x + 4)(x − 4) sanmak; o ifade tam karedir.',E='x + 4, paydadaki x²’yi tek x gibi sadeleştirmek.'),
 TT(A='dikkat',B='islem',C='bilgi',E='islem'))

# ===== 0004 ORTA ca-deger (K-CA-06)
ab=Fr(81-41,2); assert ab==20 and 41-2*ab==1 and sorted([4,5])==sorted(r for r in range(-20,21) if r*r-9*r+20==0)
assert (5-4)**2==1 and 41-20==21 and 41+20==61
P.R('0004','ca-deger','Özdeşlikle ifade değeri bulma','orta','Toplam ve Kareler Toplamı','Toplam ve kareler toplamından çarpımı bulur, istenen tam kareyi hesaplar.','düz',3,
 'K-CA-06 (a + b ve a² + b² verilip (a − b)² istenmesi) · yeni sayılar',
 'a + b = 9\na² + b² = 41\nolduğuna göre (a − b)² kaçtır?',
 ['1','20','21','40','61'],'A','(a − b)² ifadesinin değeri.',
 ['(a + b)²’yi aç; a² + b² yerine 41 yaz.','Buradan ab’yi bul.','(a − b)² = a² + b² − 2ab.'],[TKO],
 [A('Toplamın karesi','(a + b)² açılımında a² + b² = 41 yerine konur.','81 = a² + 2ab + b² = 41 + 2ab'),
  A('Çarpımı bul','İki taraftan 41 çıkar.','2ab = 40 ⇒ ab = 20'),
  A('Farkın karesi','(a − b)² = a² + b² − 2ab.','41 − 40 = 1 (a = 5, b = 4 ile kontrol: 1² = 1 ✓)')],
 '(a + b)² ile (a − b)² arasındaki fark 4ab’dir; ikisinden biri ve ab biliniyorsa öteki hemen bulunur.',
 dict(B='20, ab’nin değeri; soru (a − b)²’yi soruyor.',C='21, 41’den ab’yi çıkarmak; 2ab çıkarılmalı.',D='40, 2ab’nin değeri; 41’den çıkarmak unutulmuş.',E='61, (a − b)²’yi a² + b² + ab sanmak.'),
 TT(B='dikkat',C='islem',D='dikkat',E='bilgi'))
xy=Fr(53-25,2); assert xy==14 and 53+2*xy==81 and (7+2)**2==81 and 7-2==5 and 49+4==53 and 53+14==67 and 53+25==78
P.K('0004','x − y = 5\nx² + y² = 53\nolduğuna göre (x + y)² kaçtır?',
 ['14','28','67','78','81'],'E','(x + y)² ifadesinin değeri.',
 ['(x − y)²’yi aç; x² + y² yerine 53 yaz.','Buradan xy’yi bul.','(x + y)² = x² + y² + 2xy.'],[TKO],
 [A('Farkın karesi','(x − y)² açılımında x² + y² = 53.','25 = x² − 2xy + y² = 53 − 2xy'),
  A('Çarpımı bul','53 − 25 = 28.','2xy = 28 ⇒ xy = 14'),
  A('Toplamın karesi','(x + y)² = x² + y² + 2xy.','53 + 28 = 81 (x = 7, y = 2 ile kontrol: 9² = 81 ✓)')],
 'Kareler toplamı verildiğinde önce xy’yi bul; toplamın ve farkın kareleri ondan türetilir.',
 dict(A='14, xy’nin değeri; soru (x + y)²’yi soruyor.',B='28, 2xy’nin değeri; 53’e eklenmeli.',C='67, 53’e xy eklemek; 2xy eklenmeli.',D='78, 53’e (x − y)² = 25 eklemek; (x + y)² ile (x − y)² arasındaki fark 4xy’dir.'),
 TT(A='dikkat',B='dikkat',C='islem',D='bilgi'))

# ===== 0005 ORTA ca-alan (K-CA-08)
def kare_kose(ad_a,ad_b,alan,deg=None):
    s,c,x0,y0=120,round(120*5/11,1),40,16; b=[]
    b.append(f'<path d="M{x0} {y0} H{x0+s-c} V{y0+c} H{x0+s} V{y0+s} H{x0} Z" stroke-width="1.8"/>')
    b.append(f'<rect x="{x0+s-c}" y="{y0}" width="{c}" height="{c}" stroke-width="1.2" stroke-dasharray="4 3" opacity=".7"/>')
    b.append(G._t(x0+(s-c)/2+6,y0+s*0.62,alan,size=13,bold=True))
    b.append(G._t(x0+s/2,y0+s+16,ad_a)); b.append(G._t(x0-8,y0+s/2+4,ad_a,anchor='end'))
    b.append(G._t(x0+s-c/2,y0-4,ad_b,renk=G.ACC,bold=True)); b.append(G._t(x0+s+6,y0+c/2+4,ad_b,anchor='start',renk=G.ACC,bold=True))
    b.append(G._t(x0+s-c/2,y0+c/2+4,'kesilen',size=10))
    if deg: b.append(G._t(x0+s+40,y0+s-10,deg,anchor='start',size=11,bold=True,renk=G.ACC))
    return G._svg(300,160,''.join(b))
v=[(a,b) for a in range(1,60) for b in range(1,a) if a*a-b*b==96 and a+b==16]; assert v==[(11,5)]
assert 96//16==6 and 16-6==10 and 6//2==3
P.R('0005','ca-alan','Alan modeliyle çarpanlara ayırma','orta','Alan Modeli','Kareden kare kesilince kalan alanı iki kare farkıyla yazar, toplam bilgisiyle kenarları bulur.','şekilli',3,
 'K-CA-08 (kareden kare kesme: a² − b²) · yeni istenen (kesilen karenin kenarı)',
 'Bir kenarı a cm olan kare biçimindeki bir kartonun bir köşesinden, bir kenarı b cm olan kare biçiminde bir parça aşağıdaki gibi kesilip çıkarılmıştır. Kartonun kalan kısmının alanı 96 cm²’dir.\na + b = 16 olduğuna göre kesilen karenin bir kenarı kaç santimetredir?',
 ['3','5','6','10','11'],'B','Kesilen karenin kenar uzunluğu (b).',
 ['Kalan alanı a ve b cinsinden yaz.','a² − b² hangi iki çarpana ayrılır? a + b’yi yerine koy.','a + b ve a − b’yi bulunca iki denklemi taraf tarafa topla ya da çıkar.'],[IKF,B('Toplam ve farktan sayılar','a + b = m ve a − b = n ise a = (m + n) ÷ 2, b = (m − n) ÷ 2. Örnek: a + b = 10, a − b = 4 ⇒ a = 7, b = 3')],
 [A('Kalan alan','Büyük kareden küçük kare çıktı.','a² − b² = 96'),
  A('Çarpanlara ayır','İki kare farkı; a + b = 16 yerine konur.','(a − b) × (a + b) = 96 ⇒ (a − b) × 16 = 96 ⇒ a − b = 6'),
  A('Kenarları bul','İki denklemi çıkar.','a + b = 16 · a − b = 6 ⇒ 2b = 10 ⇒ b = 5 (a = 11)',kare_kose('a = 11','b = 5','96 cm²','121 − 25 = 96 ✓'))],
 'Kareden kare kesildiğinde kalan alan a² − b² = (a − b)(a + b) olur; toplam verilmişse fark hemen çıkar.',
 dict(A='3, a − b = 6’yı ikiye bölmek; b = (16 − 6) ÷ 2.',C='6, a − b’nin değeri; soru b’yi soruyor.',D='10, 16 − 6 = 10’u b sanmak; 10 = 2b.',E='11, büyük karenin kenarı (a); soru kesilen karenin kenarını soruyor.'),
 TT(A='islem',C='dikkat',D='islem',E='dikkat'),sekil=kare_kose('a','b','96 cm²'))
def kare_serit(deg=None):
    s,w,x0,y0=120,50,40,18; b=[]
    b.append(f'<rect x="{x0}" y="{y0}" width="{s-w}" height="{s}" stroke-width="1.8"/>')
    b.append(f'<rect x="{x0+s-w}" y="{y0}" width="{w}" height="{s}" stroke-width="1.2" stroke-dasharray="4 3" opacity=".7"/>')
    b.append(G._t(x0+(s-w)/2,y0+s/2+4,'84 cm²',size=12,bold=True))
    b.append(G._t(x0+s-w/2,y0+s/2+4,'şerit',size=10))
    b.append(f'<path d="M{x0} {y0+s+10} H{x0+s}" stroke-width="1"/>'); b.append(G._t(x0+s/2,y0+s+24,'x'))
    b.append(G._t(x0-8,y0+s/2+4,'x',anchor='end')); b.append(G._t(x0+s-w/2,y0-5,'y',renk=G.ACC,bold=True))
    if deg: b.append(G._t(x0+s+12,y0+s/2+4,deg,anchor='start',size=11,bold=True,renk=G.ACC))
    return G._svg(300,170,''.join(b))
v=[(x,y) for x in range(1,60) for y in range(1,x) if x*(x-y)==84 and x-y==7]; assert v==[(12,5)] and 12+5==17 and 12+7==19
P.K('0005','Bir kenarı x cm olan kare biçimindeki bir kumaşın bir kenarı boyunca, y cm genişliğinde bir şerit aşağıdaki gibi kesilip çıkarılmıştır. Geriye kalan dikdörtgen parçanın alanı 84 cm², kısa kenarı 7 cm’dir.\nBuna göre kesilen şeridin genişliği (y) kaç santimetredir?',
 ['5','7','12','17','19'],'A','Şeridin genişliği (y).',
 ['Kalan dikdörtgenin kenarları x ve x − y. Alanını yaz.','x² − xy’de ortak çarpan x; kısa kenar hangisi?','x’i bulduktan sonra y’ye geç.'],[B('Ortak çarpan','x² − xy = x × (x − y). Örnek: x = 10, y = 3 ⇒ 100 − 30 = 10 × 7 = 70'),B('Dikdörtgenin alanı','alan = uzun kenar × kısa kenar. Örnek: 12 × 7 = 84')],
 [A('Kalan alan','Kareden x × y’lik şerit çıktı.','x² − xy = x × (x − y) = 84'),
  A('Kenarları eşleştir','Kalan dikdörtgenin kenarları x ve x − y; kısa olan x − y.','x − y = 7 ⇒ x × 7 = 84 ⇒ x = 12'),
  A('Şerit genişliği','y = x − 7.','y = 12 − 7 = 5',kare_serit('x = 12 · y = 5'))],
 'Kesilen parça şerit ise kalan alan x(x − y) biçiminde ortak çarpanla yazılır; kenarları şekilde eşleştir.',
 dict(B='7, kalan parçanın kısa kenarı (x − y); soru y’yi soruyor.',C='12, karenin kenarı (x); soru şeridin genişliğini soruyor.',D='17, x + y’yi hesaplamak; soru yalnız y’yi soruyor.',E='19, y’yi x + 7 almak; kısa kenar x − y = 7, yani y = x − 7.'),
 TT(B='dikkat',C='dikkat',D='dikkat',E='islem'),sekil=kare_serit())

# ===== 0006 ORTA ca-ozdeslik (K-CA-02)
for xv in [(3+13**.5)/2,(3-13**.5)/2]:
    assert abs(xv-1/xv-3)<1e-12 and abs((xv+1/xv)**2-13)<1e-9 and abs(xv*xv+1/(xv*xv)-11)<1e-9
assert 9+2==11 and 11+2==13 and 9+4==13 and 11+4==15 and 9-2==7
P.R('0006','ca-ozdeslik','İki kare farkı ve tam kare özdeşlikleri','orta','x ile 1/x','x − 1/x verildiğinde tam kare açılımlarıyla x + 1/x’in karesini bulur.','düz',3,
 'K-CA-02 (x ± 1/x, orta terim ±2) · farktan toplamın karesine geçiş',
 'x − 1/x = 3\nolduğuna göre (x + 1/x)² ifadesinin değeri kaçtır?',
 ['7','9','11','13','15'],'D','(x + 1/x)² ifadesinin değeri.',
 ['x − 1/x = 3 eşitliğinin iki tarafının karesini al.','x × 1/x = 1; açılımdaki orta terim kaç olur?','Önce x² + 1/x²’yi bul, sonra (x + 1/x)²’yi aç.'],[TKO,TERS],
 [A('Karesini al','(x − 1/x)² açılımında orta terim −2.','(x − 1/x)² = x² − 2 + 1/x² = 9'),
  A('Kareler toplamı','2’yi karşıya geçir.','x² + 1/x² = 11'),
  A('İstenen kare','(x + 1/x)² açılımında orta terim +2.','(x + 1/x)² = x² + 2 + 1/x² = 11 + 2 = 13')],
 'x + 1/x ile x − 1/x’in kareleri arasındaki fark her zaman 4’tür.',
 dict(A='7, (x − 1/x)²’den 2 çıkarmak; aradaki fark 4 ve eklenir.',B='9, (x − 1/x)²’yi cevap sanmak; soru (x + 1/x)²’yi soruyor.',C='11, x² + 1/x²’nin değeri; 2 daha eklenmeli.',E='15, x² + 1/x²’ye 4 eklemek; (x + 1/x)² = x² + 1/x² + 2.'),
 TT(A='bilgi',B='dikkat',C='dikkat',E='islem'),
 kisa='(x + 1/x)² = (x − 1/x)² + 4 olduğundan doğrudan 9 + 4 = 13.')
for av in [(5+21**.5)/2,(5-21**.5)/2]:
    assert abs(av+1/av-5)<1e-12 and abs((av-1/av)**2-21)<1e-9 and abs(av*av+1/(av*av)-23)<1e-9
assert 25-2==23 and 23-2==21 and 23-4==19 and 25+2==27
P.K('0006','a + 1/a = 5\nolduğuna göre (a − 1/a)² ifadesinin değeri kaçtır?',
 ['19','21','23','25','27'],'B','(a − 1/a)² ifadesinin değeri.',
 ['a + 1/a = 5 eşitliğinin karesini al.','Orta terim 2 × a × 1/a = 2.','a² + 1/a²’yi bulup (a − 1/a)²’yi aç.'],[TKO,TERS],
 [A('Karesini al','Orta terim +2.','(a + 1/a)² = a² + 2 + 1/a² = 25'),
  A('Kareler toplamı','2’yi çıkar.','a² + 1/a² = 23'),
  A('İstenen kare','(a − 1/a)² açılımında orta terim −2.','(a − 1/a)² = 23 − 2 = 21')],
 '(a − 1/a)² = (a + 1/a)² − 4: toplamdan farka geçerken 4 çıkar.',
 dict(A='19, a² + 1/a²’den 4 çıkarmak; (a − 1/a)² = a² + 1/a² − 2.',C='23, a² + 1/a²’nin değeri; 2 çıkarılmalı.',D='25, (a + 1/a)²’yi cevap sanmak.',E='27, 25’e 2 eklemek; (a − 1/a)² = (a + 1/a)² − 4.'),
 TT(A='islem',C='dikkat',D='dikkat',E='bilgi'),
 kisa='(a − 1/a)² = (a + 1/a)² − 4 olduğundan doğrudan 25 − 4 = 21.')

# ===== 0007 ZOR ca-ortak (K-CA-04)
coz=[(a,b) for a in range(1,100) for b in range(1,100) if a*b+2*a+4*b==52]
assert coz==[(1,10),(2,8),(6,4),(8,3),(11,2),(16,1)] and max(a+b for a,b in coz)==17 and min(a+b for a,b in coz)==10
assert all((a+4)*(b+2)==60 for a,b in coz)
assert [(a,b) for a in range(1,100) for b in range(1,100) if (a+4)*(b+2)==52]==[(9,2)]            # B: +8’i unutmak
assert max(a+b for a in range(0,100) for b in range(1,100) if a*b+2*a+4*b==52)==17 and 0*13+2*0+4*13==52 and 20+3==23
P.R('0007','ca-ortak','Ortak çarpan ve gruplama','zor','Tam Sayı Çözümleri','İki bilinmeyenli ifadeyi sabit ekleyerek çarpanlarına ayırır; pozitif tam sayı çözümlerini tarayıp en büyük toplamı bulur.','düz',5,
 'K-CA-04 (xy + ax + by = c ⇒ (x + b)(y + a) = c + ab) · yeni istenen (a + b’nin en büyük değeri)',
 'a ve b pozitif tam sayılar olmak üzere\nab + 2a + 4b = 52\nolduğuna göre a + b toplamı en çok kaçtır?',
 ['10','11','13','17','23'],'D','a + b’nin alabileceği en büyük değer.',
 ['ab + 2a + 4b ifadesini iki çarpanın çarpımı yapmak için hangi sayıyı eklemelisin?','a(b + 2) + 4(b + 2) biçimine bak; eksik terim 8.','(a + 4)(b + 2) = 60; a ≥ 1, b ≥ 1 koşulunu sağlayan çarpan çiftlerini tara.'],[GRP,B('Pozitif tam sayı','1, 2, 3, … sayılarıdır; 0 pozitif değildir')],
 [A('Sabit ekle','a(b + 2) + 4(b + 2) olması için 4 × 2 = 8 gerekir; iki tarafa 8 ekle.','ab + 2a + 4b + 8 = 60'),
  A('Çarpanlara ayır','Gruplama.','a(b + 2) + 4(b + 2) = (a + 4) × (b + 2) = 60'),
  A('Koşulları yaz','a ≥ 1 ve b ≥ 1.','a + 4 ≥ 5 · b + 2 ≥ 3'),
  A('Çarpan çiftleri','60’ı bu koşullarla iki çarpana ayır.','5 × 12 · 6 × 10 · 10 × 6 · 12 × 5 · 15 × 4 · 20 × 3'),
  A('İkilileri yaz','a = ilk çarpan − 4, b = ikinci çarpan − 2.','(1, 10) (2, 8) (6, 4) (8, 3) (11, 2) (16, 1) ⇒ en çok 16 + 1 = 17')],
 'xy + ax + by = c türü denklemlerde iki tarafa ab ekle; çarpımı sabit iki çarpan elde edersin.',
 dict(A='10, a + b’nin en küçük değeri; soru en büyüğünü soruyor.',B='11, iki tarafa 8 eklemeyi unutup (a + 4) × (b + 2) = 52 çözmek.',C='13, a = 0 almak (0 + 13); a pozitif tam sayı, 0 olamaz.',E='23, çarpanların toplamını (20 + 3) cevap sanmak; a = 20 − 4, b = 3 − 2.'),
 TT(A='dikkat',B='islem',C='dikkat',E='dikkat'))
coz=[(x,y) for x in range(1,100) for y in range(1,100) if x*y+2*x+3*y==30]
assert coz==[(1,7),(3,4),(6,2),(9,1)] and max(x+y for x,y in coz)==10 and min(x+y for x,y in coz)==7 and all((x+3)*(y+2)==36 for x,y in coz)
assert max(x+y for x in range(1,100) for y in range(1,100) if (x+3)*(y+2)==30)==8 and 15*0+2*15+0==30 and 33*(-1)+2*33+3*(-1)==30
P.K('0007','x ve y pozitif tam sayılar olmak üzere\nxy + 2x + 3y = 30\neşitliği sağlanıyor.\nBuna göre x + y toplamının alabileceği en büyük değer kaçtır?',
 ['7','8','10','15','32'],'C','x + y’nin alabileceği en büyük değer.',
 ['İfadeyi iki çarpanın çarpımı yapmak için iki tarafa hangi sayıyı eklemelisin?','x(y + 2) + 3(y + 2) biçiminde eksik terim 6.','(x + 3)(y + 2) = 36; x ≥ 1, y ≥ 1 için çarpan çiftlerini tara.'],[GRP,B('Pozitif tam sayı','1, 2, 3, … sayılarıdır; 0 pozitif değildir')],
 [A('Sabit ekle','3 × 2 = 6 eklenirse ifade gruplanabilir.','xy + 2x + 3y + 6 = 36'),
  A('Çarpanlara ayır','Gruplama.','x(y + 2) + 3(y + 2) = (x + 3) × (y + 2) = 36'),
  A('Koşulları yaz','x ≥ 1 ve y ≥ 1.','x + 3 ≥ 4 · y + 2 ≥ 3'),
  A('Çarpan çiftleri','36’yı bu koşullarla iki çarpana ayır.','4 × 9 · 6 × 6 · 9 × 4 · 12 × 3'),
  A('İkilileri yaz','x = ilk çarpan − 3, y = ikinci çarpan − 2.','(1, 7) (3, 4) (6, 2) (9, 1) ⇒ en çok 9 + 1 = 10')],
 'Çarpan çiftlerini tararken her iki bilinmeyenin de pozitif kalmasını kontrol et; uçtaki çiftler en büyük toplamı verir.',
 dict(A='7, x + y’nin en küçük değeri; soru en büyüğünü soruyor.',B='8, iki tarafa 6 eklemeyi unutup (x + 3) × (y + 2) = 30 çözmek.',D='15, y = 0 almak (x = 15); y pozitif tam sayı olmalı.',E='32, y = −1 alıp x = 33 bulmak; y pozitif olmalı.'),
 TT(A='dikkat',B='islem',D='dikkat',E='dikkat'))

# ===== 0008 ZOR ca-deger (K-CA-07)
f=lambda x,y:x*x+y*y-6*x+4*y+13
assert all(f(x,y)==(x-3)**2+(y+2)**2 for x in range(-20,21) for y in range(-20,21))
assert [(x,y) for x in range(-20,21) for y in range(-20,21) if f(x,y)==0]==[(3,-2)] and 3+(-2)==1
assert 3*(-2)==-6 and -3+(-2)==-5 and -3+2==-1 and 3+2==5
P.R('0008','ca-deger','Özdeşlikle ifade değeri bulma','zor','Tam Kareye Tamamlama','İkinci dereceden iki değişkenli ifadeyi iki tam kare toplamına çevirir; kareler toplamı sıfırsa değişkenleri bulur.','düz',4,
 'K-CA-07 (tam kareye tamamlama, kareler toplamı 0) · yeni katsayılar, istenen toplam',
 'x ve y gerçel sayılar olmak üzere\nx² + y² − 6x + 4y + 13 = 0\nolduğuna göre x + y toplamı kaçtır?',
 ['−6','−5','−1','1','5'],'D','x + y toplamı.',
 ['x’li terimleri ve y’li terimleri ayrı grupla.','x² − 6x’i tam kare yapmak için kaç eklenir? y² + 4y için kaç?','13’ü bu iki sayıya ayır; iki karenin toplamı 0 ise ne olur?'],[TKO,B('Kare negatif olamaz','her gerçel sayının karesi 0 ya da pozitiftir. İki karenin toplamı 0 ise ikisi de 0’dır. Örnek: m² + n² = 0 ⇒ m = n = 0')],
 [A('Grupla','Aynı değişkenli terimleri bir araya getir.','(x² − 6x) + (y² + 4y) + 13 = 0'),
  A('Tam kareye tamamla','x² − 6x + 9 = (x − 3)² ve y² + 4y + 4 = (y + 2)²; 13 = 9 + 4.','(x − 3)² + (y + 2)² = 0'),
  A('Kareleri sıfırla','Kareler negatif olamaz; toplamları 0 ise ikisi de 0.','x − 3 = 0 ⇒ x = 3 · y + 2 = 0 ⇒ y = −2'),
  A('Sonuç','İstenen toplam.','x + y = 3 + (−2) = 1')],
 'Tek denklemde iki bilinmeyen varsa tam kareye tamamlamayı dene; kareler toplamı 0 ise her kare 0’dır.',
 dict(A='−6, x × y’nin değeri; soru x + y’yi soruyor.',B='−5, x’i −3 almak; (x − 3)² = 0 ⇒ x = 3.',C='−1, işaretleri ters almak: x = −3, y = 2.',E='5, y’yi 2 almak; (y + 2)² = 0 ⇒ y = −2.'),
 TT(A='dikkat',B='islem',C='islem',E='islem'))
g=lambda a,b:a*a+b*b+8*a-10*b+41
assert all(g(a,b)==(a+4)**2+(b-5)**2 for a in range(-20,21) for b in range(-20,21))
assert [(a,b) for a in range(-20,21) for b in range(-20,21) if g(a,b)==0]==[(-4,5)] and -4*5==-20
assert -4-5==-9 and -4+5==1 and 4+5==9 and 4*5==20
P.K('0008','a ve b gerçel sayılar olmak üzere\na² + b² + 8a − 10b + 41 = 0\nolduğuna göre a · b çarpımı kaçtır?',
 ['−20','−9','1','9','20'],'A','a × b çarpımı.',
 ['a’lı ve b’li terimleri ayrı grupla.','a² + 8a için 16, b² − 10b için 25 eklenir; 41 = 16 + 25.','İki karenin toplamı 0 ise her biri 0’dır.'],[TKO,B('Kare negatif olamaz','her gerçel sayının karesi 0 ya da pozitiftir. İki karenin toplamı 0 ise ikisi de 0’dır. Örnek: m² + n² = 0 ⇒ m = n = 0')],
 [A('Grupla','Aynı değişkenli terimleri topla.','(a² + 8a) + (b² − 10b) + 41 = 0'),
  A('Tam kareye tamamla','a² + 8a + 16 = (a + 4)² ve b² − 10b + 25 = (b − 5)²; 41 = 16 + 25.','(a + 4)² + (b − 5)² = 0'),
  A('Kareleri sıfırla','İki kare de 0.','a = −4 · b = 5'),
  A('Sonuç','İstenen çarpım.','a × b = (−4) × 5 = −20')],
 'Tam kareye tamamlarken katsayının yarısının karesini ekle: 8a için 4² = 16, −10b için 5² = 25.',
 dict(B='−9, a − b’nin değeri; soru a × b’yi soruyor.',C='1, a + b’nin değeri; soru çarpımı soruyor.',D='9, a’yı 4 alıp a + b hesaplamak; hem işaret hem istenen hatalı.',E='20, a’yı 4 almak; (a + 4)² = 0 ⇒ a = −4.'),
 TT(B='dikkat',C='dikkat',D='islem',E='islem'))

P.yaz(os.path.join(H,'carpanlar-1.json'),os.path.join(H,'carpanlar-1-kardes.json'))
