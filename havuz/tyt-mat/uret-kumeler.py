"""Kümeler ve Kartezyen Çarpım · parti 1: 8 ana + 8 kardeş. Her cevap kodla (kaba kuvvet) doğrulanır."""
import sys,os,hashlib
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,os.path.join(H,'..'))
from ortak import *
from itertools import combinations

P=Parti('kumeler','Kümeler ve Kartezyen Çarpım','matd|Kümeler-Kartezyen Çarpım')
TT=lambda **k:k

# ---------- Venn şeması yardımcıları (gorsel.py stili) ----------
def _venn(merkez,r,adlar,ad_yer,etiket,boyali,evrensel,W,Hh,konum):
    """merkez: küme adı → (x, y); etiket: bölge anahtarı → yazı; boyali: bölge anahtarları kümesi.
    Bölge anahtarı = içinde bulunduğu kümelerin küçük harfleri ('a', 'ab', 'abc'); 'd' = hiçbiri (dış)."""
    uid='v'+hashlib.md5(repr((sorted(etiket.items()),sorted(boyali),adlar,evrensel)).encode()).hexdigest()[:6]
    kume=list(merkez); b=['<defs>']
    for k,(x,y) in merkez.items(): b.append(f'<clipPath id="{uid}c{k}"><circle cx="{x}" cy="{y}" r="{r}"/></clipPath>')
    for bol in boyali:
        ic=[k for k in kume if k.lower() in bol]; dis=[k for k in kume if k.lower() not in bol]
        b.append(f'<mask id="{uid}m{bol}"><rect x="0" y="0" width="{W}" height="{Hh}" fill="white"/>'+''.join(f'<circle cx="{merkez[k][0]}" cy="{merkez[k][1]}" r="{r}" fill="black"/>' for k in dis)+'</mask>')
    b.append('</defs>')
    for bol in boyali:
        ic=[k for k in kume if k.lower() in bol]
        ic_=f'<rect x="0" y="0" width="{W}" height="{Hh}" mask="url(#{uid}m{bol})" style="fill:{G.ACC};stroke:none" fill-opacity=".45"/>'
        for k in ic: ic_=f'<g clip-path="url(#{uid}c{k})">{ic_}</g>'
        b.append(ic_)
    if evrensel:
        b.append(f'<rect x="8" y="8" width="{W-16}" height="{Hh-16}" rx="6" stroke-width="1.5"/>'); b.append(G._t(24,28,evrensel,size=13,bold=True))
    for k,(x,y) in merkez.items(): b.append(f'<circle cx="{x}" cy="{y}" r="{r}" stroke-width="1.8"/>')
    for k,(x,y) in ad_yer.items(): b.append(G._t(x,y,k,size=14,bold=True))
    for bol,s in etiket.items():
        x,y=konum[bol]; b.append(G._t(x,y+4,s,size=12,bold=True))
    return G._svg(W,Hh,''.join(b))
def venn2(adlar=('A','B'),etiket={},boyali=(),evrensel=None):
    A_,B_=adlar; M={A_:(130,100),B_:(200,100)}
    konum={'a':(98,100),'ab':(165,100),'b':(232,100),'d':(292,170)}
    konum={(A_.lower() if k=='a' else B_.lower() if k=='b' else A_.lower()+B_.lower() if k=='ab' else 'd'):v for k,v in konum.items()}
    return _venn(M,64,adlar,{A_:(70,38),B_:(260,38)},etiket,set(boyali),evrensel,330,192,konum)
def venn3(adlar=('A','B','C'),etiket={},boyali=(),evrensel=None):
    A_,B_,C_=adlar; M={A_:(135,92),B_:(195,92),C_:(165,144)}
    a,b_,c=A_.lower(),B_.lower(),C_.lower()
    konum={a:(100,78),b_:(230,78),c:(165,182),a+b_:(165,64),a+c:(126,132),b_+c:(204,132),a+b_+c:(165,110),'d':(292,200)}
    return _venn(M,60,adlar,{A_:(70,40),B_:(260,40),C_:(242,196)},etiket,set(boyali),evrensel,330,218,konum)

def alt_kumeler(E):
    E=list(E)
    for r in range(len(E)+1):
        for c in combinations(E,r): yield set(c)
def tek_dogru(siklar,sik,deger):
    S=dict(zip('ABCDE',siklar)); assert S[sik]==str(deger) and list(S.values()).count(str(deger))==1,(siklar,sik,deger)

ALT=B('Alt küme sayısı','n elemanlı bir kümenin 2ⁿ alt kümesi vardır (boş küme ve kümenin kendisi dahil). Örnek: {a, b} için ∅, {a}, {b}, {a, b} ⇒ 2² = 4')
SERB=B('Serbest eleman','bir elemanın alt kümede bulunup bulunmayacağı koşulla belirlenmemişse o eleman için 2 seçenek vardır (var / yok)')
TC=B('Tek ve çift sayılar','2’ye tam bölünen sayılar çifttir (2, 4, 6); tam bölünmeyenler tektir (1, 3, 5, 7)')
SESLI=B('Sesli harfler','Türkçede sesli harfler a, e, ı, i, o, ö, u, ü’dür; diğerleri sessizdir')
BK=B('Birleşim, kesişim','A ∪ B: en az birinde olanlar · A ∩ B: ikisinde birden olanlar')
FARK=B('Fark kümesi','A \\ B: A’da olup B’de olmayan elemanlar. Örnek: {1, 2, 3} \\ {2} = {1, 3}')
BIR=B('Birleşimin eleman sayısı','s(A ∪ B) = s(A) + s(B) − s(A ∩ B); kesişim iki kez sayıldığı için bir kez çıkarılır. Örnek: 5 + 4 − 2 = 7')
ESN=B('Eleman sayısı','s(A), A kümesinin eleman sayısıdır. Örnek: A = {2, 5, 9} ⇒ s(A) = 3')
KART=B('Kartezyen çarpım','A × B, birinci bileşeni A’dan, ikinci bileşeni B’den alınan tüm (x, y) sıralı ikilileridir; s(A × B) = s(A) × s(B). Örnek: 2 ve 3 elemanlı kümeler ⇒ 6 ikili')
KAT=B('Ortak katlar','hem 3’ün hem 5’in katı olan sayılar 15’in katlarıdır; hem 2’nin hem 3’ün katı olanlar 6’nın katlarıdır')
VENN=B('Venn şemasında bölge','her bölge hangi kümelerin içinde, hangilerinin dışında olduğuyla okunur. “Yalnız A” = A’da olup diğer kümelerde olmayan')
UC=B('Tam olarak k kümede','x₁: yalnız birinde, x₂: yalnız ikisinde, x₃: üçünde de olanlar · x₁ + x₂ + x₃ = kişi sayısı · x₁ + 2x₂ + 3x₃ = s(A) + s(B) + s(C)')

# ===== 0001 alt küme KOLAY (K-KM-01)
A6={1,2,3,4,5,6}; n_=sum(1 for s in alt_kumeler(A6) if 1 in s and 6 not in s); assert n_==16==2**4
assert sum(1 for s in alt_kumeler(A6) if 1 in s)==32 and 64-16==48
s1=['15','16','32','48','64']; tek_dogru(s1,'B',n_)
P.R('0001','km-altkume','Koşullu alt küme sayısı','kolay','Alt Küme','Belirli elemanları içeren ya da içermeyen alt kümelerin sayısını serbest elemanlarla bulur.','düz',2,
 'K-KM-01 (koşullu alt küme sayısı) · bir eleman kesin var, bir eleman kesin yok',
 'A = {1, 2, 3, 4, 5, 6} kümesinin alt kümelerinden kaç tanesi 1 elemanını içerir fakat 6 elemanını içermez?',
 s1,'B','1’i içeren ama 6’yı içermeyen alt kümelerin sayısı.',
 ['1 ve 6’nın durumu her alt kümede belli mi?','Durumu belli olmayan elemanlar hangileri; her biri için kaç seçenek var?','Serbest eleman sayısı k ise alt küme sayısı 2ᵏ olur.'],[ALT,SERB],
 [A('Sabit elemanlar','1 her alt kümede olacak, 6 hiçbirinde olmayacak. Bu iki elemanın durumu bellidir.','1 → var · 6 → yok'),
  A('Serbest elemanlar','2, 3, 4 ve 5’in her biri için “var” ya da “yok” seçilebilir.','4 serbest eleman, her birine 2 seçenek'),
  A('Say','Seçenekleri çarp.','2 × 2 × 2 × 2 = 2⁴ = 16')],
 'Durumu kesin olan elemanları ayır; kalan k serbest eleman 2ᵏ alt küme verir.',
 dict(A='15, boş kümeyi çıkarmak; 1’i içeren bir alt küme zaten boş olamaz.',C='32, “6’yı içermez” koşulunu atlayıp yalnızca 1’i içerenleri saymak (2⁵).',D='48, koşulu sağlamayan alt kümelerin sayısı (64 − 16).',E='64, A’nın tüm alt kümelerinin sayısı; koşullar kullanılmamış.'),
 TT(A='bilgi',C='dikkat',D='dikkat',E='bilgi'))
K8=set('abcdefgh'); n_=sum(1 for s in alt_kumeler(K8) if {'a','b'}<=s and 'h' not in s); assert n_==32==2**5
s1=['16','31','32','64','128']; tek_dogru(s1,'C',n_)
P.K('0001','K = {a, b, c, d, e, f, g, h} kümesi veriliyor.\nK’nin a ve b elemanlarının ikisini birden içeren, h elemanını ise içermeyen kaç alt kümesi vardır?',
 s1,'C','a ile b’yi içeren, h’yi içermeyen alt kümelerin sayısı.',
 ['Durumu belli olan elemanlar hangileri?','Geriye kaç serbest eleman kalıyor?','Her serbest eleman için 2 seçenek var.'],[ALT,SERB],
 [A('Sabit elemanlar','a ve b her alt kümede var, h hiçbirinde yok.','a, b → var · h → yok'),
  A('Serbest elemanlar','c, d, e, f ve g’nin her biri alt kümede olabilir ya da olmayabilir.','5 serbest eleman'),
  A('Say','Her serbest eleman 2 seçenek verir.','2⁵ = 32')],
 'Kesin bulunan ve kesin bulunmayan elemanları çıkardıktan sonra kalan elemanlarla 2ᵏ hesapla.',
 dict(A='16, serbest eleman sayısını 4 sanmak; c, d, e, f, g beş tanedir.',B='31, boş kümeyi çıkarmak; a ve b’yi içeren alt küme boş olamaz.',D='64, h koşulunu atlamak (2⁶).',E='128, yalnızca h koşulunu kullanmak (2⁷); a ve b şartı atlanmış.'),
 TT(A='islem',B='bilgi',D='dikkat',E='dikkat'))

# ===== 0002 alt küme "en az bir" ORTA (K-KM-01)
B7=set(range(1,8)); n_=sum(1 for s in alt_kumeler(B7) if any(x%2==0 for x in s)); assert n_==112==2**7-2**4
s2=['16','111','112','120','127']; tek_dogru(s2,'C',n_); assert 128-8==120
P.R('0002','km-altkume','Koşullu alt küme sayısı','orta','Alt Küme','“En az bir” koşullu alt küme sayısını tümleyen yoluyla bulur.','düz',3,
 'K-KM-01 (koşullu alt küme sayısı) · “en az bir çift sayı” koşulu, tümleyen yöntemi',
 'Elemanları 1’den 7’ye kadar olan doğal sayılardan oluşan B kümesi veriliyor.\nB’nin alt kümelerinin kaç tanesinde en az bir çift sayı vardır?',
 s2,'C','En az bir çift sayı içeren alt kümelerin sayısı.',
 ['“En az bir” durumlarını tek tek saymak yerine tersini düşün.','Hiç çift sayı içermeyen alt kümeler yalnızca hangi elemanlardan oluşur?','Tüm alt kümelerden bunları çıkar.'],[ALT,TC],
 [A('Tersinden düşün','“En az bir çift” durumlarını tek tek saymak uzun. Tüm alt kümelerden hiç çift içermeyenleri çıkar.','istenen = tümü − çift içermeyenler'),
  A('Tüm alt kümeler','B’nin 7 elemanı var.','2⁷ = 128'),
  A('Çift içermeyenler','Bunlar yalnızca 1, 3, 5, 7’den oluşur; boş küme de bunların içindedir.','2⁴ = 16'),
  A('Sonuç','Farkı al.','128 − 16 = 112')],
 '“En az bir” gördüğünde tümleyeni say: hiç içermeyenleri tüm alt kümelerden çıkar.',
 dict(A='16, hiç çift sayı içermeyen alt kümelerin sayısı; soru en az bir çift içerenleri soruyor.',B='111, boş kümeyi bir kez daha çıkarmak; boş küme zaten çift içermeyen 16 alt kümenin içinde.',D='120, tek sayıları 3 tane sanıp 128 − 2³ hesaplamak; 1, 3, 5, 7 dört tanedir.',E='127, boş küme dışındaki tüm alt kümeler; {1, 3} gibi çift içermeyenler de sayılmış.'),
 TT(A='dikkat',B='bilgi',D='islem',E='bilgi'))
C6=set('abcdef'); n_=sum(1 for s in alt_kumeler(C6) if s&{'a','e'}); assert n_==48==64-16
s2=['16','32','47','48','63']; tek_dogru(s2,'D',n_)
P.K('0002','C = {a, b, c, d, e, f} kümesinin elemanları birer harftir.\nC’nin alt kümelerinden kaç tanesinde en az bir sesli harf bulunur?',
 s2,'D','En az bir sesli harf içeren alt kümelerin sayısı.',
 ['C’deki sesli harfleri belirle.','Hiç sesli harf içermeyen alt kümeler hangi harflerden oluşur?','Tüm alt kümelerden bunları çıkar.'],[ALT,SESLI],
 [A('Sesli harfler','C’de sesli harfler a ve e; sessizler b, c, d, f.','sesli: a, e · sessiz: 4 harf'),
  A('Tüm alt kümeler','C’nin 6 elemanı var.','2⁶ = 64'),
  A('Sesli içermeyenler','Yalnızca b, c, d, f’den oluşanlar (boş küme dahil).','2⁴ = 16'),
  A('Sonuç','Tümleyeni çıkar.','64 − 16 = 48')],
 '“En az bir” koşulu varsa önce koşulu hiç sağlamayanları say; boş küme onların içindedir.',
 dict(A='16, hiç sesli harf içermeyen alt kümelerin sayısı.',B='32, sesli harf sayısını 1 sanıp 64 − 2⁵ hesaplamak; a ve e iki sesli harftir.',C='47, boş kümeyi ayrıca çıkarmak; boş küme zaten sesli içermeyen 16 alt kümede.',E='63, boş küme dışındaki tüm alt kümeler; {b, c} gibi sesli içermeyenler de sayılmış.'),
 TT(A='dikkat',B='islem',C='bilgi',E='bilgi'))

# ===== 0003 küme işlemleri KOLAY (K-KM-02)
U=set(range(1,10)); I={2,5}; AfB={1,3,8}; Bk=U-AfB; Ak=AfB|I
assert Ak&Bk==I and Ak-Bk==AfB and Ak|Bk==U and Bk=={2,4,5,6,7,9}
v=sum(Bk); assert v==33 and sum(I)==7 and sum(AfB)==12 and sum(Ak)==19 and sum(Bk-Ak)==26
s3=['7','12','19','26','33']; tek_dogru(s3,'E',v)
P.R('0003','km-islem','Küme işlemleriyle eleman bulma','kolay','Küme İşlemleri','Birleşim, kesişim ve fark kümesinden bir kümenin elemanlarını belirler.','düz',2,
 'K-KM-02 (işlemlerden kümeyi kurma) · yeni istenen (B’nin elemanları toplamı)',
 'A ve B kümeleri için\nA ∪ B = {1, 2, 3, 4, 5, 6, 7, 8, 9}\nA ∩ B = {2, 5}\nA \\ B = {1, 3, 8}\nolduğu biliniyor.\nBuna göre B kümesinin elemanlarının toplamı kaçtır?',
 s3,'E','B kümesindeki elemanların toplamı.',
 ['B’de olmayan elemanlar hangi kümede?','Birleşimden bu elemanları çıkarınca geriye ne kalır?','Kesişimdeki elemanlar da B’nin elemanıdır.'],[BK,FARK],
 [A('B’de olmayanlar','Birleşimdeki bir eleman B’de değilse yalnızca A’dadır; bunlar A \\ B’dir.','A \\ B = {1, 3, 8}'),
  A('B’yi yaz','Birleşimden A \\ B’yi çıkar. Kalanlar B’dir; kesişim de buna dahildir.','B = {2, 4, 5, 6, 7, 9}',venn2(etiket={'a':'1, 3, 8','ab':'2, 5','b':'4, 6, 7, 9'})),
  A('Topla','B’nin elemanlarını topla.','2 + 4 + 5 + 6 + 7 + 9 = 33')],
 'Venn şemasının bölgelerini (yalnız A, kesişim, yalnız B) doldurmak her küme işlemini kolaylaştırır.',
 dict(A='7, yalnızca kesişimdeki 2 ve 5’in toplamı; B’nin diğer elemanları eksik.',B='12, A \\ B’nin toplamı; bu elemanlar B’de yok.',C='19, A kümesinin toplamı (1 + 3 + 8 + 2 + 5).',D='26, B \\ A’nın toplamı; kesişimdeki 2 ve 5 de B’nin elemanıdır.'),
 TT(A='dikkat',B='dikkat',C='dikkat',D='bilgi'))
U=set(range(2,15,2)); I={6,12}; LfK={2,10,14}; Kk=U-LfK; Lk=LfK|I
assert Kk&Lk==I and Lk-Kk==LfK and Kk|Lk==U and Kk-Lk=={4,8}
v=sum(Kk-Lk); assert v==12 and sum(I)==18 and sum(LfK)==26 and sum(Kk)==30 and sum(Lk)==44
s3=['12','18','26','30','44']; tek_dogru(s3,'A',v)
P.K('0003','K ve L kümeleriyle ilgili aşağıdakiler bilinmektedir.\nK ∪ L = {2, 4, 6, 8, 10, 12, 14}\nK ∩ L = {6, 12}\nL \\ K = {2, 10, 14}\nBuna göre K \\ L kümesindeki elemanların toplamı kaçtır?',
 s3,'A','K \\ L kümesindeki elemanların toplamı.',
 ['Birleşimdeki her eleman hangi üç bölgeden birindedir?','Kesişimi ve L \\ K’yı birleşimden çıkar.','K \\ L, kesişimi içermez.'],[BK,FARK],
 [A('Bölgeler','Birleşim üç parçadan oluşur: K \\ L, K ∩ L ve L \\ K.','K ∪ L = (K \\ L) ∪ (K ∩ L) ∪ (L \\ K)'),
  A('K \\ L’yi bul','Birleşimden kesişimi ve L \\ K’yı çıkar.','K \\ L = {4, 8}',venn2(('K','L'),etiket={'k':'4, 8','kl':'6, 12','l':'2, 10, 14'})),
  A('Topla','Kalan iki elemanı topla.','4 + 8 = 12')],
 'Fark kümesi kesişimi içermez; birleşimi üç bölgeye ayırarak düşün.',
 dict(B='18, kesişimdeki 6 ve 12’nin toplamı.',C='26, L \\ K’nın toplamı; soru K \\ L’yi soruyor.',D='30, K’nin tamamının toplamı; K \\ L’de kesişimdeki elemanlar yoktur.',E='44, L kümesinin toplamı.'),
 TT(B='dikkat',C='dikkat',D='bilgi',E='dikkat'))

# ===== 0004 Venn problemi (oranlı) ORTA (K-KM-03)
c=[(S,Y,I) for I in range(1,41) for S in range(I,41) for Y in range(I,41) if 3*I==S and 2*I==Y and S+Y-I==40]; assert c==[(30,20,10)]
v=30-10; assert v==20
s4=['8','10','16','20','30']; tek_dogru(s4,'D',v); assert 5*8==40 and 3*8-8==16
P.R('0004','km-venn-problem','Venn şemasıyla sayma problemi','orta','Venn Problemleri','Kesişimin iki grubun kesri olarak verildiği problemde birleşim denklemini kurar.','hikâyeli',3,
 'K-KM-03 (kesişim iki grubun kesri) · yeni kurgu (satranç ve yüzme kursu)',
 'Bir sınıftaki 40 öğrencinin her biri satranç ve yüzme kurslarından en az birine katılmaktadır.\nSatranç kursuna katılanların 1/3’ü yüzme kursuna da katılmaktadır.\nYüzme kursuna katılanların yarısı satranç kursuna da katılmaktadır.\nBuna göre yalnızca satranç kursuna katılan kaç öğrenci vardır?',
 s4,'D','Yalnızca satranç kursuna katılan öğrenci sayısı.',
 ['İki kursa birden katılanlara x de.','Satranç kursuna katılanlar x’in kaç katı? Yüzme kursuna katılanlar?','Birleşim 40: s(S) + s(Y) − x = 40.'],[BIR,B('Kesrin bütünü','bir grubun 1/3’ü x ise grubun tamamı 3x’tir. Örnek: 1/3’ü 5 olan grup 15 kişidir')],
 [A('Kesişime x de','İki kursa birden katılan öğrenci sayısı x olsun.','s(S ∩ Y) = x'),
  A('Kursların mevcudu','x, satranççıların 1/3’ü ve yüzücülerin yarısıdır.','s(S) = 3x · s(Y) = 2x'),
  A('Birleşim 40','Her öğrenci en az bir kursta; kesişim bir kez çıkarılır.','3x + 2x − x = 4x = 40 ⇒ x = 10'),
  A('Yalnız satranç','Satranç kursundakilerden iki kursa gidenleri çıkar.','30 − 10 = 20',venn2(('S','Y'),etiket={'s':'20','sy':'10','y':'10'}))],
 'Kesişim bir grubun kesri olarak verildiyse kesişime x de; grupları x cinsinden yazıp birleşim denklemini kur.',
 dict(A='8, birleşimi 3x + 2x = 40 alıp x’i bulmak; kesişim iki kez sayılmış.',B='10, iki kursa birden katılanların sayısı; yalnız yüzmeye katılanlar da 10’dur.',C='16, kesişimi çıkarmadan 5x = 40 ⇒ x = 8 bulup 24 − 8 hesaplamak.',E='30, satranç kursuna katılanların tamamı; soru yalnızca satranca katılanları soruyor.'),
 TT(A='islem',B='dikkat',C='islem',E='dikkat'),kisa=None)
c=[(Cc,Kk_,I) for I in range(1,37) for Cc in range(I,37) for Kk_ in range(I,37) if Cc==4*I and 2*Kk_==3*I and Cc+Kk_-I==36]; assert c==[(32,12,8)]
v=12-8; assert v==4
s4=['4','8','12','24','32']; tek_dogru(s4,'A',v)
P.K('0004','36 kişilik bir grubun her üyesi çay ve kahveden en az birini içmektedir.\nÇay içenlerin 1/4’ü kahve de içmektedir.\nKahve içenlerin 2/3’ü çay da içmektedir.\nBuna göre yalnızca kahve içen kaç kişi vardır?',
 s4,'A','Yalnızca kahve içen kişi sayısı.',
 ['İkisini birden içenlere x de.','Çay içenlerin 1/4’ü x ise çay içen kaç kişi? Kahve içenlerin 2/3’ü x ise kahve içen kaç kişi?','Birleşim 36 olacak biçimde denklem kur.'],[BIR,B('Kesrin bütünü','bir grubun 2/3’ü x ise grubun tamamı 3x/2’dir. Örnek: 2/3’ü 8 olan grup 12 kişidir')],
 [A('Kesişime x de','İkisini birden içenler x olsun.','s(Ç ∩ K) = x'),
  A('Grupları yaz','x, çay içenlerin 1/4’ü ve kahve içenlerin 2/3’üdür.','s(Ç) = 4x · s(K) = 3x/2'),
  A('Birleşim 36','Kesişimi bir kez çıkar.','4x + 3x/2 − x = 9x/2 = 36 ⇒ x = 8'),
  A('Yalnız kahve','Kahve içenler 3 × 8 ÷ 2 = 12; bunlardan 8’i çay da içiyor.','12 − 8 = 4',venn2(('Ç','K'),etiket={'ç':'24','çk':'8','k':'4'}))],
 'Kesişim iki ayrı kesirle verildiyse iki grubu da x cinsinden yaz; birleşimde kesişimi bir kez çıkar.',
 dict(B='8, ikisini birden içenlerin sayısı.',C='12, kahve içenlerin tamamı; bunların 8’i çay da içiyor.',D='24, yalnızca çay içenlerin sayısı; soru yalnızca kahve içenleri soruyor.',E='32, çay içenlerin tamamı.'),
 TT(B='dikkat',C='bilgi',D='dikkat',E='dikkat'))

# ===== 0005 Venn boyalı bölge ORTA (K-KM-05)
def bolgeler(E,kos,ad='abc'):
    """kos: küme harfi → koşul. Her sayının bölge anahtarını döndürür."""
    r={}
    for x in E:
        k=''.join(h for h in ad if kos[h](x)) or 'd'; r.setdefault(k,[]).append(x)
    return r
E=range(1,31); R5=bolgeler(E,{'a':lambda x:x%2==0,'b':lambda x:x%3==0,'c':lambda x:x%5==0})
assert R5['a']==[2,4,8,14,16,22,26,28] and R5['bc']==[15] and R5['abc']==[30]
v=len(R5['a'])+len(R5['bc']); assert v==9
assert (15-5-3)+1==8 and len([x for x in E if x%2==0 and x%3])+1==11 and len(R5['a'])+2==10
s5=['8','9','10','11','15']; tek_dogru(s5,'B',v)
et5={k:str(len(vv)) for k,vv in R5.items() if k!='d'}
P.R('0005','km-boyali','Venn şemasında boyalı bölge','orta','Venn Şeması','Bölünebilme özelliğiyle tanımlı kümelerde boyalı bölgelerin eleman sayısını bulur.','şekilli',3,
 'K-KM-05 (bölünebilme kümeleri, boyalı bölge) · 2, 3, 5’in katları; iki ayrı boyalı bölge',
 'E = {1, 2, 3, …, 30} evrensel kümesinin elemanları aşağıdaki Venn şemasına yerleştirilmiştir. Şemadaki A kümesi E’nin 2’nin katı olan elemanlarından, B kümesi 3’ün katı olanlardan, C kümesi de 5’in katı olanlardan oluşmaktadır.\nBuna göre şemada boyalı bölgelerde bulunan elemanların sayısı kaçtır?',
 s5,'B','Boyalı bölgelerdeki eleman sayısı.',
 ['Boyalı bölgeler hangi kümelerin içinde, hangilerinin dışında?','Yalnız A: 2’nin katı olup 3’ün ve 5’in katı olmayanlar.','A dışındaki B ∩ C: 15’in katı olan tek sayılar.'],[VENN,KAT],
 [A('Bölgeleri oku','Boyalı iki bölge var: yalnız A (B ve C’nin dışında) ve A’nın dışında kalan B ∩ C.','yalnız A bölgesi · A dışındaki B ∩ C'),
  A('Yalnız A','2’nin katlarından 3’ün ya da 5’in katı olanları ele.','2, 4, 8, 14, 16, 22, 26, 28 ⇒ 8 sayı'),
  A('B ∩ C, A dışında','15’in katları 15 ve 30. 30 çift olduğu için A ∩ B ∩ C’dedir.','yalnız 15 ⇒ 1 sayı'),
  A('Topla','İki bölgenin eleman sayılarını topla.','8 + 1 = 9',venn3(etiket=et5,boyali={'a','bc'},evrensel='E'))],
 'Boyalı bölgeyi önce “hangi kümelerde var, hangilerinde yok” diye sözle yaz, sonra sayıları tek tek ele.',
 dict(A='8, yalnız A’yı 15 − 5 − 3 = 7 bulmak; hem 6’nın hem 10’un katı olan 30 iki kez çıkarılmış.',C='10, 30’u da B ∩ C bölgesine koymak; 30 çift olduğu için A’nın içindedir.',D='11, yalnız A’dan 5’in katı olan 10 ve 20’yi çıkarmamak.',E='15, A kümesinin tüm elemanları; boyalı bölge A’nın yalnızca bir parçası.'),
 TT(A='islem',C='dikkat',D='islem',E='dikkat'),sekil=venn3(boyali={'a','bc'},evrensel='E'))
E=range(1,41); R5k=bolgeler(E,{'a':lambda x:x%3==0,'b':lambda x:x%4==0,'c':lambda x:x%5==0})
assert R5k.get('ab')==[12,24,36] and 'abc' not in R5k and R5k['c']==[5,10,25,35]
v=len(R5k['ab'])+len(R5k.get('abc',[]))+len(R5k['c']); assert v==7
assert len([x for x in E if x%5==0 and x%4])+3==9 and 8+3==11
s5=['3','4','7','9','11']; tek_dogru(s5,'C',v)
et5={k:str(len(vv)) for k,vv in R5k.items() if k!='d'}; et5['abc']='0'
P.K('0005','Aşağıdaki Venn şemasında evrensel küme E = {1, 2, 3, …, 40} olarak alınmıştır. A, E’deki 3’ün katlarını; B, 4’ün katlarını; C ise 5’in katlarını göstermektedir.\nŞemadaki boyalı bölgelere düşen sayıların adedi kaçtır?',
 s5,'C','Boyalı bölgelerdeki sayıların adedi.',
 ['Boyalı bölgeler: A ile B’nin ortak kısmı ve yalnız C. Sözle yaz.','A ∩ B: hem 3’ün hem 4’ün katı, yani 12’nin katları.','Yalnız C: 5’in katı olup 3’ün ve 4’ün katı olmayanlar.'],[VENN,B('Ortak katlar','hem 3’ün hem 4’ün katı olan sayılar 12’nin katlarıdır')],
 [A('Bölgeleri oku','Boyalı olanlar A ∩ B’nin tamamı (C içindeki parçası dahil) ve yalnız C.','A ∩ B · yalnız C'),
  A('A ∩ B','12’nin katları; hiçbiri 5’in katı değil.','12, 24, 36 ⇒ 3 sayı'),
  A('Yalnız C','5’in katlarından 3’ün ya da 4’ün katı olanları (15, 20, 30, 40) ele.','5, 10, 25, 35 ⇒ 4 sayı'),
  A('Topla','İki bölgeyi topla.','3 + 4 = 7',venn3(etiket=et5,boyali={'ab','abc','c'},evrensel='E'))],
 'Ortak katlar EKOK’un katlarıdır; “yalnız” bölgede diğer kümelerin katlarını tek tek ele.',
 dict(A='3, yalnızca A ∩ B bölgesi; boyalı “yalnız C” bölgesi eksik.',B='4, yalnızca “yalnız C” bölgesi; A ∩ B bölgesi eksik.',D='9, 5’in katlarından 3’ün katlarını (15, 30) çıkarmamak: 6 + 3.',E='11, C’nin 8 elemanının hepsini “yalnız C” sanmak: 8 + 3.'),
 TT(A='dikkat',B='dikkat',D='islem',E='bilgi'),sekil=venn3(boyali={'ab','abc','c'},evrensel='E'))

# ===== 0006 üç küme fazla sayım ZOR (K-KM-04)
def uc_kume(N,sA,sB,sC,x3):
    """Tüm bölge dağılımlarını tarar; (yalnız bir, yalnız iki) değerlerini döndürür."""
    r=set()
    for ab in range(0,N+1):
        for ac in range(0,N+1-ab):
            for bc in range(0,N+1-ab-ac):
                a=sA-ab-ac-x3; b=sB-ab-bc-x3; c=sC-ac-bc-x3
                if min(a,b,c)<0: continue
                if a+b+c+ab+ac+bc+x3==N: r.add((a+b+c,ab+ac+bc))
    return r
r=uc_kume(50,25,20,22,4); assert r=={(37,9)}
s6=['9','13','17','33','37']; tek_dogru(s6,'E',37); assert 17-4==13 and 50-13-4==33 and 67-50==17
P.R('0006','km-venn-problem','Venn şemasıyla sayma problemi','zor','Venn Problemleri','Üç kümeli problemde fazla sayımı kullanarak yalnızca bir kümede olanların sayısını bulur.','hikâyeli',4,
 'K-KM-04 (üç kümede fazla sayım) · yeni kurgu (kitap kulübü, üç roman), istenen yalnız bir',
 'Bir kitap kulübündeki 50 öğrencinin her biri kulübün önerdiği A, B ve C romanlarından en az birini okumuştur.\nA romanını 25, B romanını 20, C romanını 22 öğrenci okumuştur.\nÜç romanı da okuyan öğrenci sayısı 4’tür.\nBuna göre bu romanlardan yalnızca birini okuyan kaç öğrenci vardır?',
 s6,'E','Yalnızca bir roman okuyan öğrenci sayısı.',
 ['Okuyucu sayılarını toplayınca her öğrenci kaç kez sayılır?','Toplam ile 50 arasındaki fark, fazladan yapılan sayımlardır.','Üç romanı okuyan biri 2 kez, iki romanı okuyan biri 1 kez fazla sayılır.'],[UC],
 [A('Toplamları ekle','Bu toplamda iki roman okuyan 2 kez, üçünü okuyan 3 kez sayılır.','25 + 20 + 22 = 67'),
  A('Fazla sayım','Her öğrenci bir kez sayılsaydı toplam 50 olurdu.','67 − 50 = 17'),
  A('Fazlayı paylaştır','İki roman okuyan 1 kez, üçünü okuyan 2 kez fazla sayılır.','x₂ + 2 × 4 = 17 ⇒ x₂ = 9'),
  A('Yalnız bir roman','50 öğrenciden iki ve üç roman okuyanları çıkar.','x₁ = 50 − 9 − 4 = 37')],
 'Üç kümede “toplamlar − kişi sayısı” fazla sayımdır: iki kümede olan 1, üç kümede olan 2 kez fazla sayılır.',
 dict(A='9, yalnızca iki roman okuyanların sayısı; soru yalnızca bir roman okuyanları soruyor.',B='13, fazla sayımdan üç roman okuyanları bir kez çıkarmak (17 − 4); onlar 2 kez fazla sayılır.',C='17, fazla sayımın tamamını iki roman okuyanlar sanmak.',D='33, iki roman okuyanları 13 alıp 50 − 13 − 4 hesaplamak.'),
 TT(A='dikkat',B='islem',C='bilgi',D='islem'))
r=uc_kume(60,30,26,24,3); assert r=={(43,14)}
s6=['11','14','17','20','43']; tek_dogru(s6,'B',14); assert 20-9==11 and 20-3==17
P.K('0006','Bir sitede oturan 60 kişinin her biri X, Y ve Z dizilerinden en az birini izlemektedir.\nX dizisini 30, Y dizisini 26, Z dizisini 24 kişi izlemektedir.\nÜç diziyi de izleyen 3 kişi vardır.\nBuna göre bu dizilerden yalnızca ikisini izleyen kaç kişi vardır?',
 s6,'B','Yalnızca iki dizi izleyen kişi sayısı.',
 ['İzleyici sayılarının toplamı 60’tan ne kadar fazla?','Bu fazlalığa kimler katkı yapar?','Üç diziyi izleyen biri 2, iki dizi izleyen biri 1 kez fazla sayılır.'],[UC],
 [A('Toplamları ekle','İki dizi izleyen 2 kez, üçünü izleyen 3 kez sayılır.','30 + 26 + 24 = 80'),
  A('Fazla sayım','Her kişi bir kez sayılsaydı toplam 60 olurdu.','80 − 60 = 20'),
  A('Üç dizi izleyenler','Her biri 2 kez fazla sayıldı.','2 × 3 = 6'),
  A('Yalnız iki dizi','Kalan fazlalık yalnızca ikisini izleyenlerden gelir.','x₂ = 20 − 6 = 14')],
 'Fazla sayımı paylaştırırken üç kümede olanların 2 kez fazla sayıldığını unutma.',
 dict(A='11, üç dizi izleyenleri 3 kez çıkarmak (20 − 9); onlar 2 kez fazla sayılır.',C='17, üç dizi izleyenleri bir kez çıkarmak (20 − 3).',D='20, fazla sayımın tamamını iki dizi izleyenlere vermek.',E='43, yalnızca bir dizi izleyenlerin sayısı (60 − 14 − 3).'),
 TT(A='islem',C='islem',D='bilgi',E='dikkat'))

# ===== 0007 kartezyen ORTA (K-KM-06)
c=[(a,b) for a in range(1,41) for b in range(1,41) if a*b==40 and a+b-3==11 and min(a,b)>=3 and a>b]; assert c==[(10,4)]
v=(10-3)*4; assert v==28 and (10-3)*3==21 and (10-4)*4==24 and 7*10==70
s7=['21','24','28','40','70']; tek_dogru(s7,'C',v)
P.R('0007','km-kartezyen','Kartezyen çarpımın eleman sayısı','orta','Kartezyen Çarpım','Kartezyen çarpım ve birleşim bilgisinden kümelerin eleman sayılarını bulup yeni bir kartezyen çarpımı hesaplar.','düz',4,
 'K-KM-06 (toplam–çarpımdan eleman sayıları) · istenen fark kümesi ile kartezyen çarpım',
 'A ve B sonlu kümeler olmak üzere\ns(A × B) = 40\ns(A ∪ B) = 11\ns(A ∩ B) = 3\nolduğu biliniyor. A kümesinin eleman sayısı B’ninkinden fazladır.\nBuna göre (A \\ B) × B kümesinin eleman sayısı kaçtır?',
 s7,'C','(A \\ B) × B kümesinin eleman sayısı.',
 ['Birleşim formülünden s(A) + s(B) kaç eder?','s(A) × s(B) = 40 ile birlikte iki sayıyı bul.','s(A \\ B) = s(A) − s(A ∩ B).'],[ESN,BIR,KART],
 [A('Toplam','Birleşim formülünü s(A) + s(B) için düzenle.','s(A) + s(B) = 11 + 3 = 14'),
  A('Çarpım','Kartezyen çarpımın eleman sayısı çarpımdır.','s(A) × s(B) = 40'),
  A('Sayıları bul','Toplamı 14, çarpımı 40 olan sayılar 10 ve 4. A’nınki büyük.','s(A) = 10 · s(B) = 4'),
  A('Fark kümesi','A’dan kesişimi çıkar.','s(A \\ B) = 10 − 3 = 7'),
  A('Yeni çarpım','Eleman sayılarını çarp.','7 × 4 = 28')],
 'Birleşim ve kartezyen çarpım birlikte verildiyse s(A) ile s(B)’nin toplamını ve çarpımını bulursun.',
 dict(A='21, (A \\ B) × (A ∩ B) hesaplamak (7 × 3); ikinci küme B’nin tamamı.',B='24, s(A \\ B)’yi s(A) − s(B) = 6 sanmak; çıkarılması gereken kesişimdir.',D='40, s(A × B); soru (A \\ B) × B’yi soruyor.',E='70, B yerine A ile çarpmak (7 × 10).'),
 TT(A='dikkat',B='bilgi',D='dikkat',E='dikkat'))
c=[(k,l) for k in range(1,37) for l in range(1,37) if k*l==36 and k+l-3==10 and min(k,l)>=3 and k<l]; assert c==[(4,9)]
v=4*(9-3); assert v==24 and 4*3==12 and 4*5==20
s7=['12','20','24','36','54']; tek_dogru(s7,'C',v)
P.K('0007','K ve L sonlu kümeleri için\ns(K ∪ L) = 10\ns(K ∩ L) = 3\ns(K × L) = 36\neşitlikleri sağlanmaktadır. K’nin eleman sayısı L’ninkinden azdır.\nBuna göre K × (L \\ K) kümesinin eleman sayısı kaçtır?',
 s7,'C','K × (L \\ K) kümesinin eleman sayısı.',
 ['s(K) + s(L) değerini birleşim formülünden bul.','Toplamı ve çarpımı bilinen iki sayıyı belirle.','L \\ K, L’den kesişim çıkarılınca kalır.'],[ESN,BIR,KART],
 [A('Toplam','Birleşim formülünden.','s(K) + s(L) = 10 + 3 = 13'),
  A('Çarpım','Kartezyen çarpımdan.','s(K) × s(L) = 36'),
  A('Sayıları bul','Toplamı 13, çarpımı 36: 4 ve 9. K’ninki küçük.','s(K) = 4 · s(L) = 9'),
  A('Fark kümesi','L’den kesişimi çıkar.','s(L \\ K) = 9 − 3 = 6'),
  A('Yeni çarpım','Eleman sayılarını çarp.','4 × 6 = 24')],
 'Fark kümesinin eleman sayısı için büyük kümeden kesişimi çıkar; diğer kümenin eleman sayısını değil.',
 dict(A='12, K × (K ∩ L) hesaplamak (4 × 3).',B='20, s(L \\ K)’yı s(L) − s(K) = 5 sanmak; çıkarılması gereken kesişimdir.',D='36, s(K × L); soru K × (L \\ K)’yı soruyor.',E='54, K yerine L ile çarpmak (9 × 6).'),
 TT(A='dikkat',B='bilgi',D='dikkat',E='dikkat'))

# ===== 0008 kartezyen (x, x) ikilileri ZOR (K-KM-06)
def kart_durum(carp,birl,ortak):
    return [(a,b) for a in range(1,carp+1) for b in range(1,carp+1) if a*b==carp and a+b-ortak==birl and ortak<=min(a,b)]
d=kart_durum(60,13,4); assert sorted(d)==[(5,12),(12,5)]
# küçük örnekle (x, x) ikilisi = kesişim elemanı
Aa={1,2,3,4,5}; Bb={4,5,6}; assert sum(1 for x in Aa for y in Bb if x==y)==len(Aa&Bb)
v=max(a-4 for a,b in d); assert v==8 and min(a-4 for a,b in d)==1
s8=['1','4','7','8','12']; tek_dogru(s8,'D',v)
SIR=B('Sıralı ikili','(x, y) ikilisinde x birinci, y ikinci bileşendir. (x, x) ikilisi A × B’de ise x hem A’da hem B’dedir')
P.R('0008','km-kartezyen','Kartezyen çarpımın eleman sayısı','zor','Kartezyen Çarpım','Bileşenleri eşit ikililerden kesişimi çıkarır; iki olası durumu inceleyerek en büyük değeri bulur.','düz',4,
 'K-KM-06 (toplam–çarpımdan eleman sayıları) · (x, x) ikilileriyle verilen kesişim, “en çok” sorusu',
 'A ve B sonlu kümeleri için A × B kümesinin 60 elemanı vardır. Bu sıralı ikililerden tam 4 tanesinin birinci ve ikinci bileşeni birbirine eşittir.\ns(A ∪ B) = 13\nolduğuna göre A \\ B kümesinin eleman sayısı en çok kaçtır?',
 s8,'D','s(A \\ B)’nin alabileceği en büyük değer.',
 ['(x, x) biçimindeki bir ikili A × B’de ise x hangi kümelerdedir?','Bu ikililerin sayısı hangi kümenin eleman sayısına eşittir?','s(A) + s(B) ve s(A) × s(B)’yi bul; hangisinin A olduğunu iki durumda dene.'],[SIR,BIR,KART],
 [A('Eşit bileşenler','(x, x) ikilisi A × B’de ise x hem A’da hem B’dedir; her ortak eleman bir tane böyle ikili verir.','s(A ∩ B) = 4'),
  A('Toplam','Birleşim formülünü kullan.','s(A) + s(B) = 13 + 4 = 17'),
  A('Çarpım','Kartezyen çarpımın eleman sayısı.','s(A) × s(B) = 60'),
  A('İki durum','Toplamı 17, çarpımı 60 olan sayılar 12 ve 5. Hangisinin A’ya ait olduğu belli değil.','s(A) = 12 ⇒ s(A \\ B) = 8 · s(A) = 5 ⇒ s(A \\ B) = 1'),
  A('En çok','İki durumdan büyük olanı seç.','en çok 8')],
 'Kümeler simetrik verildiyse “en çok / en az” sorusunda iki yerleşimi de dene.',
 dict(A='1, s(A) = 5 durumundaki değer; soru en çok değeri soruyor.',B='4, bileşenleri eşit ikililerin sayısı, yani kesişimin eleman sayısı.',C='7, s(A) − s(B) farkı; A \\ B için kesişim çıkarılmalı.',E='12, s(A) değeri; A \\ B kesişimdeki 4 elemanı içermez.'),
 TT(A='dikkat',B='dikkat',C='islem',E='bilgi'))
d=kart_durum(48,11,3); assert sorted(d)==[(6,8),(8,6)]
v=min(b-3 for a,b in d); assert v==3 and max(b-3 for a,b in d)==5
s8=['2','3','5','6','8']; tek_dogru(s8,'B',v)
P.K('0008','K × L kümesinin 48 elemanından tam 3 tanesi, birinci bileşeni ikinci bileşenine eşit olan sıralı ikililerdir.\ns(K ∪ L) = 11\nolduğuna göre L \\ K kümesinin eleman sayısı en az kaçtır?',
 s8,'B','s(L \\ K)’nin alabileceği en küçük değer.',
 ['Bileşenleri eşit ikililer K ile L’nin hangi elemanlarından oluşur?','s(K) + s(L) ve s(K) × s(L)’yi bul.','s(L)’nin alabileceği iki değeri de dene.'],[SIR,BIR,KART],
 [A('Eşit bileşenler','Her ortak eleman x için (x, x) ikilisi K × L’dedir.','s(K ∩ L) = 3'),
  A('Toplam','Birleşim formülünden.','s(K) + s(L) = 11 + 3 = 14'),
  A('Çarpım','Kartezyen çarpımdan.','s(K) × s(L) = 48'),
  A('İki durum','Toplamı 14, çarpımı 48: 6 ve 8.','s(L) = 6 ⇒ 6 − 3 = 3 · s(L) = 8 ⇒ 8 − 3 = 5'),
  A('En az','Küçük olanı seç.','en az 3')],
 '(x, x) ikililerinin sayısı her zaman kesişimin eleman sayısıdır.',
 dict(A='2, s(L) − s(K) farkı (8 − 6); fark kümesi için kesişim çıkarılır.',C='5, s(L) = 8 durumundaki değer; soru en az değeri soruyor.',D='6, s(L)’nin küçük değerini fark kümesi sanmak; kesişim çıkarılmamış.',E='8, s(L)’nin büyük değeri.'),
 TT(A='islem',C='dikkat',D='bilgi',E='dikkat'))

P.yaz(os.path.join(H,'kumeler-1.json'),os.path.join(H,'kumeler-1-kardes.json'))
