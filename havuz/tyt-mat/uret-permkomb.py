"""Permütasyon ve Kombinasyon · parti 1: 8 ana + 8 kardeş. Her sayı itertools ile tüm durumlar taranarak doğrulanır."""
import sys,os
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,os.path.join(H,'..'))
from ortak import *
from math import comb

P=Parti('permkomb','Permütasyon ve Kombinasyon','matd|Permütasyon ve Kombinasyon')
TT=lambda **k:k
def tek_dogru(siklar,sik,deger):
    S=dict(zip('ABCDE',siklar)); assert S[sik]==str(deger) and list(S.values()).count(str(deger))==1,(siklar,sik,deger)
def eslesmeler(kisiler):
    """Kişileri sırasız ikililere ayırmanın tüm yolları."""
    k=list(kisiler)
    if not k: yield []; return
    a=k[0]
    for i in range(1,len(k)):
        b=k[i]; kalan=k[1:i]+k[i+1:]
        for e in eslesmeler(kalan): yield [frozenset((a,b))]+e
def yollar(m,n):
    """(0,0)’dan (m,n)’ye sağ (R) / yukarı (U) en kısa yollar; her yol geçtiği noktaların listesi."""
    for adim in set(permutations('R'*m+'U'*n)):
        x=y=0; nk=[(0,0)]
        for c in adim:
            x,y=(x+1,y) if c=='R' else (x,y+1); nk.append((x,y))
        yield nk

# ---------- ızgara çizimi ----------
def izgara(m,n,nokta,kapali=None,yol=None):
    u=min(46,250/m,150/n); W=330; ox=(W-m*u)/2; oy=22; X=lambda x:ox+x*u; Y=lambda y:oy+(n-y)*u; b=[]
    for x in range(m+1): b.append(f'<line x1="{X(x):.1f}" y1="{Y(0):.1f}" x2="{X(x):.1f}" y2="{Y(n):.1f}" stroke-width="1.6"/>')
    for y in range(n+1): b.append(f'<line x1="{X(0):.1f}" y1="{Y(y):.1f}" x2="{X(m):.1f}" y2="{Y(y):.1f}" stroke-width="1.6"/>')
    if yol: b.append(f'<path d="M{" L".join(f"{X(x):.1f} {Y(y):.1f}" for x,y in yol)}" stroke-width="4.5" stroke-linejoin="round" stroke-linecap="round" style="stroke:{G.ACC}"/>')
    for ad,(x,y) in nokta.items():
        b.append(f'<circle cx="{X(x):.1f}" cy="{Y(y):.1f}" r="4.5" style="fill:currentColor"/>')
        dx=-12 if x==0 else 12 if x==m else 12; dy=16 if y==0 else -8
        b.append(G._t(X(x)+dx,Y(y)+dy,ad,size=14,bold=True))
    if kapali:
        x,y=kapali; b.append(f'<circle cx="{X(x):.1f}" cy="{Y(y):.1f}" r="9" stroke-width="2" style="fill:var(--bg,#fff);stroke:#e53935"/>')
        b.append(f'<path d="M{X(x)-5:.1f} {Y(y)-5:.1f} l10 10 m0 -10 l-10 10" stroke-width="2.2" style="stroke:#e53935"/>')
    return G._svg(W,round(oy+n*u+30),''.join(b))

FAK=B('Faktöriyel','n! = 1 × 2 × … × n. Örnek: 4! = 24. Farklı n nesne yan yana n! farklı biçimde dizilir')
CARP=B('Çarpma ilkesi','birlikte yapılan seçimlerde seçenek sayıları çarpılır. Örnek: 3 gömlek ve 2 pantolon ⇒ 3 × 2 = 6 kombin')
KOMB=B('Kombinasyon','n kişiden sırası önemsiz r kişi C(n, r) = n! / (r! × (n − r)!) biçimde seçilir. Örnek: C(5, 2) = 10')
TUM=B('Tümleyenle sayma','“en az”, “olmayacak” gibi koşullarda tüm durumlardan istenmeyen durumları çıkar')

# ===== 0001 çarpma ilkesi KOLAY (K-PK-01)
v=len(list(product(range(4),range(5),[None,0,1,2])));assert v==80 and 4*5*3==60 and 4*5+3==23
s=['12','20','23','60','80']; tek_dogru(s,'E',v)
P.R('0001','pk-carpma','Saymanın temel ilkesi','kolay','Saymanın Temel İlkesi','İsteğe bağlı seçimi de içeren birlikte seçimlerde çarpma ilkesini uygular.','hikâyeli',2,
 'K-PK-01 (çarpma ilkesi, isteğe bağlı seçim) · yeni kurgu (lokanta menüsü)',
 'Bir lokantanın öğle menüsünde 4 çeşit çorba, 5 çeşit ana yemek ve 3 çeşit tatlı vardır.\nSelin birer çorba ve ana yemek seçecek; tatlı almak ise isteğe bağlıdır ve en fazla bir tatlı alacaktır.\nBuna göre Selin siparişini kaç farklı biçimde verebilir?',
 s,'E','Selin’in verebileceği farklı sipariş sayısı.',
 ['Çorba ve ana yemek için kaç seçenek var?','Tatlı tarafında “hiç almamak” da bir seçenek mi?','Birlikte yapılan seçimlerin sayıları toplanır mı, çarpılır mı?'],[CARP],
 [A('Zorunlu seçimler','Her çorba her ana yemekle eşleşebilir.','4 × 5 = 20'),
  A('Tatlı seçenekleri','3 tatlıdan biri ya da hiç tatlı almamak.','3 + 1 = 4 seçenek'),
  A('Birleştir','Seçimler birlikte yapıldığı için çarp.','20 × 4 = 80')],
 'İsteğe bağlı bir seçimde “almamak” da bir seçenektir; seçenek sayısına 1 ekle.',
 dict(A='12, seçenekleri toplamak (4 + 5 + 3); seçimler birlikte yapıldığı için çarpılır.',B='20, tatlıyı hiç hesaba katmamak (4 × 5).',C='23, 4 × 5’e tatlı sayısını eklemek; tatlı seçimi de çarpılır.',D='60, tatlı almama seçeneğini unutmak (4 × 5 × 3).'),
 TT(A='bilgi',B='dikkat',C='bilgi',D='dikkat'))
v=len(list(product(range(6),('külah','kâse'),[None,0,1,2]))); assert v==48 and 6*2*3==36 and 6*2*2*3==72
s=['12','15','36','48','72']; tek_dogru(s,'D',v)
P.K('0001','Bir dondurmacıda 6 farklı dondurma çeşidi vardır; dondurma külahta ya da kâsede verilmektedir.\nDondurmanın üzerine 3 farklı sostan biri eklenebilir ya da hiç sos eklenmeyebilir.\nAhmet bir dondurma çeşidi ve bir sunum biçimi seçecek, sos için de bu seçeneklerden birini tercih edecektir.\nBuna göre Ahmet kaç farklı sipariş verebilir?',
 s,'D','Ahmet’in verebileceği farklı sipariş sayısı.',
 ['Dondurma çeşidi ve sunum biçimi için kaç seçenek var?','Sos için “sossuz” seçeneğini de say.','Seçenek sayılarını çarp.'],[CARP],
 [A('Çeşit ve sunum','Her çeşit iki sunumla verilebilir.','6 × 2 = 12'),
  A('Sos seçenekleri','3 sostan biri ya da sossuz.','3 + 1 = 4'),
  A('Birleştir','Üç seçim birlikte yapılır.','12 × 4 = 48')],
 '“Eklenebilir ya da eklenmeyebilir” ifadesi seçenek sayısını 1 artırır.',
 dict(A='12, sosu hiç hesaba katmamak (6 × 2).',B='15, sos sayısını 6 × 2’ye eklemek; sos seçimi de çarpılır.',C='36, sossuz seçeneğini unutmak (6 × 2 × 3).',E='72, sos için “var/yok” ile sos çeşidini ayrıca çarpmak (6 × 2 × 2 × 3); sossuz seçenek bir kez sayılır.'),
 TT(A='dikkat',B='bilgi',C='dikkat',E='islem'))

# ===== 0002 koşullu sıralama ORTA (K-PK-03)
K6=['Ali','Banu','Cem','D','E','F']
def yan(p,a,b): return abs(p.index(a)-p.index(b))==1
v=sum(1 for p in permutations(K6) if yan(p,'Ali','Banu') and p.index('Cem') not in (0,5)); assert v==144
assert sum(1 for p in permutations(K6) if yan(p,'Ali','Banu'))==240 and sum(1 for p in permutations(K6) if yan(p,'Ali','Banu') and p.index('Cem') in (0,5))==96
assert factorial(5)*2==240 and factorial(4)*2==48 and 240-48==192
s=['72','96','144','192','240']; tek_dogru(s,'C',v)
BIT=B('Bitişik kişiler','yan yana duracak kişiler tek bir blok gibi sıralanır; blok içinde de kendi aralarında yer değiştirebilirler (2! = 2)')
P.R('0002','pk-sira-kosul','Koşullu sıralama','orta','Sıralama','Bitişiklik ve konum koşullarını birlikte kullanarak sıralama sayısını tümleyenle bulur.','hikâyeli',3,
 'K-PK-03 (bitişiklik + konum koşulu) · yeni kurgu (fotoğraf sırası)',
 'Ali, Banu, Cem ve üç arkadaşları daha olmak üzere 6 kişi bir fotoğraf için yan yana sıralanacaktır.\nAli ile Banu yan yana duracak, Cem ise sıranın iki ucundan hiçbirinde durmayacaktır.\nBuna göre bu 6 kişi kaç farklı biçimde sıralanabilir?',
 s,'C','Koşullara uyan sıralama sayısı.',
 ['Ali ile Banu’yu tek bir blok gibi düşün; blok içinde kaç düzen var?','Önce yalnızca bitişiklik koşuluyla say.','Cem’in uçta olduğu sıralamaları bul ve çıkar.'],[FAK,BIT,TUM],
 [A('Bloğu kur','Ali–Banu bloğu ve 4 kişi: 5 birim sıralanır; blok içinde 2 düzen.','5! × 2 = 240'),
  A('Cem uçta','Cem başta: kalan 5 yere blok ve 3 kişi, 4! × 2 = 48. Cem sonda da 48.','48 + 48 = 96'),
  A('Çıkar','Cem’in uçta olduğu sıralamaları at.','240 − 96 = 144')],
 'Bitişik kişileri blok yap, blok içi düzeni çarpmayı unutma; “olmayacak” koşulunu tümleyenle say.',
 dict(A='72, Ali ile Banu’nun kendi aralarında yer değiştirebileceğini (2!) unutmak.',B='96, Cem’in uçta olduğu sıralamaların sayısı; bunlar istenmiyor.',D='192, Cem’in uçta olduğu durumları yalnızca bir uç için çıkarmak (240 − 48).',E='240, Cem koşulunu kullanmamak.'),
 TT(A='bilgi',B='dikkat',D='islem',E='dikkat'))
K7=['Deniz','Efe','Filiz','a','b','c','d']
v=sum(1 for p in permutations(K7) if p[0]=='Filiz' and not yan(p,'Deniz','Efe')); assert v==480==factorial(6)-factorial(5)*2
assert sum(1 for p in permutations(K7) if p[0]=='Filiz' and yan(p,'Deniz','Efe'))==240 and factorial(7)-factorial(6)*2==3600
s=['240','480','720','3600','5040']; tek_dogru(s,'B',v)
P.K('0002','Deniz, Efe, Filiz ve dört arkadaşları daha olmak üzere 7 kişi bir sırada yan yana oturacaktır.\nFiliz sıranın en başında oturacak; Deniz ile Efe ise yan yana oturmayacaktır.\nBuna göre bu 7 kişi kaç farklı biçimde oturabilir?',
 s,'B','Koşullara uyan oturma düzeni sayısı.',
 ['Filiz’in yeri belli; geriye kaç kişi ve kaç yer kalıyor?','Kalan kişilerin tüm dizilişlerinden Deniz ile Efe’nin yan yana olduklarını çıkar.','Yan yana olanları sayarken onları blok yap.'],[FAK,BIT,TUM],
 [A('Filiz’i yerleştir','Filiz en başta; kalan 6 kişi 6 yere dizilir.','6! = 720'),
  A('Yan yana olanlar','Deniz–Efe bloğu ve 4 kişi: 5 birim; blok içinde 2 düzen.','5! × 2 = 240'),
  A('Çıkar','Yan yana oturdukları düzenleri at.','720 − 240 = 480')],
 '“Yan yana olmayacak” sorularında tüm dizilişlerden yan yana olanları çıkarmak en kısa yoldur.',
 dict(A='240, Deniz ile Efe’nin yan yana oturduğu düzenler; bunlar istenmiyor.',C='720, Deniz–Efe koşulunu kullanmamak (6!).',D='3600, Filiz koşulunu kullanmamak (7! − 6! × 2).',E='5040, hiçbir koşulu kullanmamak (7!).'),
 TT(A='dikkat',C='dikkat',D='dikkat',E='dikkat'))

# ===== 0003 en az koşullu seçim ORTA (K-PK-04)
uye=[('k',i) for i in range(5)]+[('e',i) for i in range(4)]
v=sum(1 for c in combinations(uye,4) if {x[0] for x in c}=={'k','e'}); assert v==120==comb(9,4)-comb(5,4)-comb(4,4)
assert 5*4*comb(7,2)==420
s=['120','121','125','126','420']; tek_dogru(s,'A',v)
P.R('0003','pk-secme','Kombinasyonla seçme','orta','Kombinasyon','“En az bir” koşullu ekip seçimini tümleyenle sayar.','hikâyeli',3,
 'K-PK-04 (en az koşullu ekip seçimi) · iki grup için “en az bir” koşulu',
 'Bir kulüpte 5 kız ve 4 erkek üye vardır.\nBu üyeler arasından içinde en az bir kız ve en az bir erkek bulunan 4 kişilik bir ekip seçilecektir.\nBuna göre bu ekip kaç farklı biçimde seçilebilir?',
 s,'A','Koşula uyan 4 kişilik ekip sayısı.',
 ['Önce koşulsuz kaç ekip seçilebileceğini bul.','Koşulu bozan ekipler yalnızca kızlardan ya da yalnızca erkeklerden oluşanlardır.','Bunları tüm ekiplerden çıkar.'],[KOMB,TUM],
 [A('Tüm ekipler','9 kişiden 4 kişi, sıra önemsiz.','C(9, 4) = 126'),
  A('İstenmeyenler','Yalnız kızlardan ya da yalnız erkeklerden oluşan ekipler.','C(5, 4) = 5 · C(4, 4) = 1'),
  A('Çıkar','İstenmeyenleri tüm ekiplerden çıkar.','126 − 5 − 1 = 120')],
 '“En az bir” koşulunda önce zorunlu kişiyi seçip kalanları serbest seçme; aynı ekip birden çok kez sayılır.',
 dict(B='121, yalnız erkeklerden oluşan ekibi çıkarmayı unutmak (126 − 5).',C='125, yalnız kızlardan oluşan 5 ekibi çıkarmayı unutmak (126 − 1).',D='126, koşulu kullanmamak.',E='420, önce 1 kız ve 1 erkek seçip kalan 2 kişiyi 7 kişiden seçmek (5 × 4 × 21); aynı ekip birden çok kez sayılır.'),
 TT(B='dikkat',C='dikkat',D='dikkat',E='bilgi'))
sorular=range(1,11)
v=sum(1 for c in combinations(sorular,6) if len([x for x in c if x<=4])>=3); assert v==95==comb(4,3)*comb(6,3)+comb(4,4)*comb(6,2)
assert comb(4,3)*comb(7,3)==140 and comb(10,6)==210
s=['15','80','95','140','210']; tek_dogru(s,'C',v)
P.K('0003','10 sorudan oluşan bir sınavda her öğrenci bu sorulardan 6 tanesini seçip cevaplayacaktır.\nSınav kuralına göre ilk 4 sorudan en az 3 tanesinin seçilmesi zorunludur.\nBuna göre bir öğrenci cevaplayacağı soruları kaç farklı biçimde seçebilir?',
 s,'C','Kurala uyan soru seçimi sayısı.',
 ['İlk 4 sorudan kaç tane seçilebilir: 3 mü, 4 mü?','Her durumda kalan sorular son 6 sorudan seçilir.','İki durumu ayrı ayrı hesaplayıp topla.'],[KOMB,B('Durumlara ayırma','“en az 3” = “tam 3” ya da “tam 4”; ayrık durumların sayıları toplanır')],
 [A('Tam 3 soru','İlk 4’ten 3, son 6’dan 3 soru.','C(4, 3) × C(6, 3) = 4 × 20 = 80'),
  A('Tam 4 soru','İlk 4’ün hepsi, son 6’dan 2 soru.','C(4, 4) × C(6, 2) = 1 × 15 = 15'),
  A('Topla','İki durum birbirinden ayrık.','80 + 15 = 95')],
 '“En az” koşulunu “tam şu kadar” durumlarına ayır; her durumda kalan seçimi diğer gruptan yap.',
 dict(A='15, yalnızca ilk 4 sorunun hepsinin seçildiği durum.',B='80, yalnızca ilk 4’ten tam 3 sorunun seçildiği durum; 4’ünün seçildiği durum unutulmuş.',D='140, ilk 4’ten 3 soru seçip kalan 3’ü diğer 7 sorudan seçmek; bazı seçimler iki kez sayılır.',E='210, koşulu kullanmamak (C(10, 6)).'),
 TT(A='dikkat',B='dikkat',D='bilgi',E='dikkat'))

# ===== 0004 ızgarada yol ORTA (K-PK-06)
Y=list(yollar(5,3)); assert len(Y)==56
v=sum(1 for y in Y if (2,1) in y); assert v==30==comb(3,1)*comb(5,2) and 56-30==26 and 3+10==13 and 2*10==20
ornek=[(0,0),(1,0),(2,0),(2,1),(3,1),(4,1),(4,2),(5,2),(5,3)]; assert ornek in [list(y) for y in Y]
s=['10','13','20','26','30']; tek_dogru(s,'E',v)
YOL=B('Izgarada en kısa yol','m sağ ve n yukarı adımlık yolda m + n adımdan hangilerinin yukarı olduğu seçilir: C(m + n, n). Örnek: 2 sağ, 1 yukarı ⇒ C(3, 1) = 3 yol')
P.R('0004','pk-yol','Şekil üzerinde yol sayma','orta','Yol Sayma','Ara noktadan geçen en kısa yolların sayısını çarpma ilkesiyle bulur.','şekilli',3,
 'K-PK-06 (ızgarada yol, ara noktadan geçme) · yeni kurgu (karınca), 5 × 3 ızgara',
 'Aşağıda birim karelerden oluşan bir ızgara gösterilmiştir. Bir karınca, ızgaranın çizgileri üzerinde yalnızca sağa ya da yukarı doğru ilerleyerek A noktasından B noktasına gidecektir.\nKarınca C noktasından geçmek zorunda olduğuna göre kaç farklı yol izleyebilir?',
 s,'E','C’den geçen farklı yol sayısı.',
 ['Yolu iki parçaya ayır: A’dan C’ye ve C’den B’ye.','A’dan C’ye kaç sağ, kaç yukarı adım gerekiyor? Bu adımların sırası kaç farklı olabilir?','İki parçanın yol sayılarını birleştir: toplanır mı, çarpılır mı?'],[YOL,CARP],
 [A('A’dan C’ye','2 sağ, 1 yukarı adım; 3 adımdan hangisinin yukarı olduğunu seç.','C(3, 1) = 3'),
  A('C’den B’ye','3 sağ, 2 yukarı adım; 5 adımdan 2’si yukarı.','C(5, 2) = 10'),
  A('Birleştir','Her A–C yolu her C–B yoluyla devam edebilir; çarp. Şekilde bu yollardan biri görülüyor.','3 × 10 = 30',izgara(5,3,{'A':(0,0),'B':(5,3),'C':(2,1)},yol=ornek))],
 'Ara noktadan geçme koşulunda yolu ikiye böl, her parçayı ayrı say ve çarp.',
 dict(A='10, yalnızca C’den B’ye giden yollar; A’dan C’ye olan kısım unutulmuş.',B='13, iki parçanın yol sayılarını toplamak; her A–C yolu her C–B yoluyla birleşir.',C='20, A’dan C’ye yalnızca 2 yol saymak; sağ-sağ-yukarı, sağ-yukarı-sağ ve yukarı-sağ-sağ olmak üzere 3 yol vardır.',D='26, C’den geçmeyen yolların sayısı (56 − 30).'),
 TT(A='dikkat',B='bilgi',C='islem',D='dikkat'),sekil=izgara(5,3,{'A':(0,0),'B':(5,3),'C':(2,1)}))
Y=list(yollar(4,3)); assert len(Y)==35
v=sum(1 for y in Y if (2,1) not in y); assert v==17 and 35-17==18==comb(3,1)*comb(4,2) and 35-(3+6)==26 and 35-3==32
s=['17','18','26','32','35']; tek_dogru(s,'A',v)
P.K('0004','Aşağıdaki ızgarada K noktasından L noktasına, çizgiler üzerinde yalnızca sağa ya da yukarı doğru ilerleyerek gidilecektir.\nIzgaradaki M noktası onarımda olduğu için bu noktadan geçilemez.\nBuna göre K’dan L’ye kaç farklı yol vardır?',
 s,'A','M’den geçmeyen yolların sayısı.',
 ['Önce M’yi yok sayarak K’dan L’ye kaç yol olduğunu bul.','M’den geçen yolları iki parçaya ayırıp say.','Tüm yollardan M’den geçenleri çıkar.'],[YOL,TUM],
 [A('Tüm yollar','4 sağ, 3 yukarı adım; 7 adımdan 3’ü yukarı.','C(7, 3) = 35'),
  A('M’den geçenler','K’dan M’ye 2 sağ 1 yukarı, M’den L’ye 2 sağ 2 yukarı.','C(3, 1) × C(4, 2) = 3 × 6 = 18'),
  A('Çıkar','Geçilemeyen noktadan geçen yolları at.','35 − 18 = 17',izgara(4,3,{'K':(0,0),'L':(4,3),'M':(2,1)},kapali=(2,1)))],
 'Kapalı nokta varsa tüm yollardan o noktadan geçenleri çıkar; geçenleri sayarken iki parçayı çarp.',
 dict(B='18, M’den geçen yolların sayısı; bunlar kullanılamıyor.',C='26, M’den geçen yolları 3 + 6 = 9 sanıp 35 − 9 hesaplamak; parçalar çarpılır.',D='32, yalnızca K’dan M’ye giden 3 yolu çıkarmak; her biri M’den L’ye 6 yolla devam eder.',E='35, kapalı noktayı yok saymak.'),
 TT(B='dikkat',C='bilgi',D='bilgi',E='dikkat'),sekil=izgara(4,3,{'K':(0,0),'L':(4,3),'M':(2,1)},kapali=(2,1)))

# ===== 0005 tekrarlı permütasyon KOLAY (K-PK-07)
v=len(set(permutations('KKKMMY'))); assert v==60 and factorial(6)//factorial(3)==120 and factorial(6)//2==360
s=['6','60','120','360','720']; tek_dogru(s,'B',v)
TEKR=B('Tekrarlı permütasyon','n nesneden a tanesi kendi arasında, b tanesi kendi arasında özdeşse diziliş sayısı n! / (a! × b!). Örnek: A, A, B ⇒ 3! / 2! = 3')
P.R('0005','pk-tekrarli','Tekrarlı permütasyon','kolay','Tekrarlı Permütasyon','Özdeş nesnelerin dizilişlerini tekrarlı permütasyonla sayar.','hikâyeli',2,
 'K-PK-07 (özdeş nesnelerle diziliş) · yeni kurgu (renkli kavanozlar)',
 'Bir rafa 3 özdeş kırmızı, 2 özdeş mavi ve 1 yeşil kavanoz yan yana dizilecektir.\nYalnızca renklerin sırası dikkate alındığına göre kaç farklı diziliş yapılabilir?',
 s,'B','Farklı renk dizilişlerinin sayısı.',
 ['Kavanozların hepsi farklı olsaydı kaç diziliş olurdu?','Özdeş kırmızıların kendi aralarında yer değiştirmesi yeni bir diziliş verir mi?','Özdeşlerin kendi içindeki düzen sayılarına böl.'],[FAK,TEKR],
 [A('Hepsi farklı olsaydı','6 kavanoz yan yana.','6! = 720'),
  A('Özdeşlere böl','3 kırmızının ve 2 mavinin kendi aralarındaki yer değişimleri aynı görüntüyü verir.','720 ÷ (3! × 2!) = 720 ÷ 12 = 60')],
 'Özdeş nesnelerde önce hepsini farklı say, sonra her özdeş grubun kendi içindeki diziliş sayısına böl.',
 dict(A='6, yalnızca 3 rengin sırasını düşünüp 3! almak.',C='120, yalnızca kırmızıların tekrarını hesaba katmak (6! / 3!).',D='360, yalnızca mavilerin tekrarını hesaba katmak (6! / 2!).',E='720, kavanozları birbirinden farklı saymak (6!).'),
 TT(A='bilgi',C='islem',D='islem',E='bilgi'))
P.ANA[-1]['adimlar'].append(A('Kontrol','Örneğin K K K M M Y ile K K K M Y M farklı; iki kırmızının yerini değiştirmek ise aynı dizilişi verir.','60 farklı diziliş'))
v=len(set(permutations('BALABAN'))); assert v==420 and factorial(7)//factorial(3)==840 and factorial(7)//4==1260 and factorial(7)//2==2520
s=['420','840','1260','2520','5040']; tek_dogru(s,'A',v)
P.K('0005','BALABAN kelimesindeki harflerin hepsi kullanılarak yazılabilecek 7 harfli, anlamlı ya da anlamsız kaç farklı kelime vardır?',
 s,'A','Farklı 7 harfli kelime sayısı.',
 ['Hangi harfler kaç kez tekrar ediyor?','Harfler farklı olsaydı kaç kelime olurdu?','Her tekrar eden harfin tekrar sayısının faktöriyeline böl.'],[FAK,TEKR],
 [A('Harfleri say','B 2 kez, A 3 kez, L ve N birer kez.','2 + 3 + 1 + 1 = 7 harf'),
  A('Hepsi farklı olsaydı','7 harf yan yana.','7! = 5040'),
  A('Tekrarlara böl','Özdeş B’ler ve A’lar kendi aralarında yer değiştirince aynı kelime çıkar.','5040 ÷ (2! × 3!) = 5040 ÷ 12 = 420')],
 'Kelimedeki her harfin kaç kez geçtiğini önce tablo gibi yaz; böleni bu sayılar belirler.',
 dict(B='840, yalnızca A’ların tekrarını hesaba katmak (7! / 3!).',C='1260, A’yı 2 kez sayıp 7! / (2! × 2!) hesaplamak; A üç kez geçiyor.',D='2520, yalnızca B’lerin tekrarını hesaba katmak (7! / 2!).',E='5040, harfleri birbirinden farklı saymak (7!).'),
 TT(B='islem',C='dikkat',D='islem',E='bilgi'))

# ===== 0006 rakamlarla sayma ORTA (K-PK-02)
v=sum(1 for n in range(100,1000) if n%2==0 and len(set(str(n)))==3); assert v==328 and 9*8==72 and 4*8*8==256 and 5*8*8==320 and 9*8*5==360
s=['72','256','320','328','360']; tek_dogru(s,'D',v)
RAK=B('Rakamları farklı sayı','her rakam en fazla bir kez kullanılır; en soldaki basamak 0 olamaz. Örnek: 102 olur, 012 üç basamaklı değildir')
TC=B('Tek ve çift sayı','birler basamağı 0, 2, 4, 6 ya da 8 olan sayı çift; 1, 3, 5, 7 ya da 9 olan sayı tektir')
P.R('0006','pk-carpma','Saymanın temel ilkesi','orta','Saymanın Temel İlkesi','Rakamları farklı ve çift olan sayıları birler basamağına göre durumlara ayırarak sayar.','düz',3,
 'K-PK-02 (rakamları farklı, koşullu sayı) · çift olma koşulu, 0 durumu ayrı',
 'Rakamları birbirinden farklı olan üç basamaklı çift doğal sayılar kaç tanedir?',
 s,'D','Rakamları farklı üç basamaklı çift sayıların adedi.',
 ['Çift olması için birler basamağına hangi rakamlar gelebilir?','Birler basamağı 0 olunca yüzler basamağının seçenek sayısı değişir mi?','Birler 0 ve birler 0 değil durumlarını ayrı say.'],[RAK,TC,CARP],
 [A('Birler 0 ise','Yüzlere 0 dışındaki 9 rakam, onlara kalan 8 rakam.','9 × 8 = 72'),
  A('Birler 2, 4, 6, 8','Birler 4 seçenek; yüzler 0 ve birlerdeki rakam olamaz: 8; onlar kalan 8 rakam.','4 × 8 × 8 = 256'),
  A('Topla','İki durum birbirinden ayrık.','72 + 256 = 328')],
 '0 rakamı hem birler basamağında hem başta sorun çıkarır; 0’lı durumu her zaman ayrı say.',
 dict(A='72, yalnızca birler basamağı 0 olan sayılar.',B='256, birler basamağı 0 olan durumu unutmak.',C='320, birler 0 iken de yüzler için 8 seçenek saymak (5 × 8 × 8).',E='360, basamakları birbirinden bağımsız sanmak (9 × 8 × 5); birlerdeki rakam yüzlerde tekrar kullanılamaz.'),
 TT(A='dikkat',B='dikkat',C='islem',E='bilgi'))
v=sum(1 for n in range(1000,10000) if n%5==0 and len(set(str(n)))==4); assert v==952 and 9*8*7==504 and 8*8*7==448
s=['448','504','896','952','1008']; tek_dogru(s,'D',v)
P.K('0006','Rakamları birbirinden farklı olan dört basamaklı doğal sayılardan kaç tanesi 5 ile tam bölünür?',
 s,'D','Rakamları farklı, 5’e bölünen dört basamaklı sayıların adedi.',
 ['5 ile bölünebilmek için birler basamağı ne olmalı?','Birler 0 iken binler basamağına kaç rakam gelebilir? Birler 5 iken?','İki durumu ayrı say ve topla.'],[RAK,B('5 ile bölünebilme','birler basamağı 0 ya da 5 olan sayılar 5 ile tam bölünür. Örnek: 340 ve 785'),CARP],
 [A('Birler 0 ise','Binlere 9, yüzlere 8, onlara 7 rakam.','9 × 8 × 7 = 504'),
  A('Birler 5 ise','Binler 0 ve 5 olamaz: 8; yüzler kalan 8; onlar 7.','8 × 8 × 7 = 448'),
  A('Topla','Durumlar ayrık.','504 + 448 = 952')],
 'Birler basamağı 0 olunca 0 başa gelme sorunu kalkar; bu yüzden 0’lı ve 0’sız durumların sayıları farklıdır.',
 dict(A='448, yalnızca birler basamağı 5 olan sayılar.',B='504, yalnızca birler basamağı 0 olan sayılar.',C='896, birler 0 iken de binler için 8 seçenek almak (2 × 448).',E='1008, birler 5 iken de binler için 9 seçenek almak (2 × 504); binler 0 olamaz.'),
 TT(A='dikkat',B='dikkat',C='islem',E='islem'))

# ===== 0007 eşleştirme ZOR (K-PK-08)
K=['Ayşe','Burak','Can','Derya','e','f']; E_=list(eslesmeler(K)); assert len(E_)==15
v=sum(1 for e in E_ if frozenset(('Ayşe','Burak')) not in e and frozenset(('Can','Derya')) not in e); assert v==10==15-3-3+1
assert comb(6,2)*comb(4,2)*comb(2,2)==90 and 15-3-3==9
s=['9','10','12','15','90']; tek_dogru(s,'B',v)
ESL=B('Eşleştirme sayısı','2n kişiyi sırasız ikililere ayırmanın yolu (2n − 1) × (2n − 3) × … × 1’dir. Örnek: 4 kişi ⇒ 3 × 1 = 3')
ICD=B('İçerme–dışarma','iki istenmeyen durumu ayrı ayrı çıkarınca ikisinin birlikte olduğu durumlar iki kez çıkarılır; bunları bir kez geri ekle')
P.R('0007','pk-gruplama','Gruplara ayırma ve eşleştirme','zor','Gruplara Ayırma','Sırasız ikililere ayırmada iki “birlikte olmama” koşulunu içerme–dışarma ile sayar.','hikâyeli',4,
 'K-PK-08 (eşleştirme, birlikte olmama koşulları) · yeni kurgu (dans çiftleri), iki koşul',
 'Bir dans kursundaki 6 öğrenci (aralarında Ayşe, Burak, Can ve Derya da var) ikişerli 3 dans çifti oluşturacaktır.\nAyşe ile Burak aynı çiftte olmayacak; Can ile Derya da aynı çiftte olmayacaktır.\nÇiftlerin sırası önemli olmadığına göre bu 3 çift kaç farklı biçimde oluşturulabilir?',
 s,'B','Koşullara uyan çift oluşturma sayısı.',
 ['Koşul olmasaydı 6 kişi kaç farklı biçimde ikililere ayrılırdı?','Ayşe–Burak çifti oluştuğunda kalan 4 kişi kaç biçimde eşleşir?','İki istenmeyen çiftin birlikte oluştuğu durumu iki kez çıkarmadığına emin ol.'],[ESL,ICD],
 [A('Tüm eşleşmeler','Ayşe’nin eşi 5 yolla seçilir; kalan 4 kişiden birinin eşi 3 yolla; son ikili kendiliğinden oluşur.','5 × 3 × 1 = 15'),
  A('Ayşe–Burak çifti','Bu çift oluşursa kalan 4 kişi 3 yolla eşleşir.','3 eşleşme'),
  A('Can–Derya çifti','Aynı düşünceyle.','3 eşleşme'),
  A('İkisi birden','İki çift de oluşursa kalan iki kişi zorunlu olarak çift olur.','1 eşleşme'),
  A('Sonuç','İkisinin birlikte olduğu durum iki kez çıkarıldı; bir kez geri ekle.','15 − 3 − 3 + 1 = 10')],
 'İki “olmayacak” koşulunda içerme–dışarma kullan: tümü − birinci − ikinci + ikisi birden.',
 dict(A='9, iki koşulun ihlallerini çıkarıp ikisinin birlikte olduğu durumu geri eklememek (15 − 3 − 3).',C='12, yalnızca bir koşulu kullanmak (15 − 3).',D='15, koşulları kullanmamak.',E='90, çiftleri sıralı saymak (C(6, 2) × C(4, 2) × C(2, 2)); çiftlerin sırası önemsiz.'),
 TT(A='islem',C='dikkat',D='dikkat',E='bilgi'))
K=['Ece','Fatih','Gizem','Hakan','e','f','g','h']; E_=list(eslesmeler(K)); assert len(E_)==105
v=sum(1 for e in E_ if frozenset(('Ece','Fatih')) in e and frozenset(('Gizem','Hakan')) not in e); assert v==12
assert sum(1 for e in E_ if frozenset(('Ece','Fatih')) in e)==15 and sum(1 for e in E_ if frozenset(('Ece','Fatih')) in e and frozenset(('Gizem','Hakan')) in e)==3
s=['3','12','14','15','105']; tek_dogru(s,'B',v)
P.K('0007','Bir kampa katılan 8 öğrenci (aralarında Ece, Fatih, Gizem ve Hakan da var) ikişer kişilik 4 çadıra yerleşecektir.\nEce ile Fatih aynı çadırda kalacak; Gizem ile Hakan ise aynı çadırda kalmayacaktır.\nÇadırlar birbirinden ayırt edilmediğine göre öğrenciler çadırlara kaç farklı biçimde yerleşebilir?',
 s,'B','Koşullara uyan yerleşim sayısı.',
 ['Ece ile Fatih bir çadırı doldurur; geriye kaç kişi kalır?','Kalan 6 kişi kaç farklı biçimde ikililere ayrılır?','Gizem ile Hakan’ın aynı çadırda olduğu yerleşimleri çıkar.'],[ESL,TUM],
 [A('Ece ile Fatih','Bu ikili bir çadırı doldurur; 6 kişi kalır.','6 kişi, 3 çadır'),
  A('Kalanların eşleşmesi','Bir kişinin çadır arkadaşı 5, sonrakinin 3 yolla seçilir.','5 × 3 × 1 = 15'),
  A('Gizem–Hakan birlikte','Bu ikili de bir çadırdaysa kalan 4 kişi 3 yolla eşleşir.','3 yerleşim'),
  A('Çıkar','İstenmeyen yerleşimleri at.','15 − 3 = 12')],
 '“Birlikte olacak” kişileri önce yerleştir; “birlikte olmayacak” koşulunu kalanlarda tümleyenle say.',
 dict(A='3, Gizem ile Hakan’ın aynı çadırda olduğu yerleşimler; bunlar istenmiyor.',C='14, Gizem–Hakan ikilisinin oluştuğu durumu 1 sanmak; kalan 4 kişi 3 biçimde eşleşir.',D='15, Gizem–Hakan koşulunu kullanmamak.',E='105, hiçbir koşulu kullanmamak (8 kişinin tüm eşleşmeleri).'),
 TT(A='dikkat',C='islem',D='dikkat',E='dikkat'))

# ===== 0008 seçim sayısından kişi sayısı ZOR (K-PK-05)
c=[(k,e) for k in range(1,30) for e in range(1,30) if comb(k+e,2)==66 and k*e==35 and k>e]; assert c==[(7,5)]
# tokalaşmaları tek tek listeleyerek kontrol
kisi=[('k',i) for i in range(7)]+[('e',i) for i in range(5)]; tk=list(combinations(kisi,2))
assert len(tk)==66 and sum(1 for a,b in tk if a[0]!=b[0])==35
v=sum(1 for a,b in tk if a[0]==b[0]=='k'); assert v==21 and comb(5,2)==10 and comb(6,2)==15 and 66-35==31
s=['10','15','21','31','35']; tek_dogru(s,'C',v)
TOK=B('Tokalaşma sayısı','n kişinin her biri diğerleriyle birer kez tokalaşırsa C(n, 2) = n × (n − 1) / 2 tokalaşma olur. Örnek: 5 kişi ⇒ 10')
P.R('0008','pk-secme','Kombinasyonla seçme','zor','Kombinasyon','Tokalaşma sayılarından grup büyüklüklerini bulur ve bir grubun kendi içindeki seçim sayısını hesaplar.','hikâyeli',4,
 'K-PK-05 (seçim sayısından kişi sayısı) · yeni kurgu (toplantıda tokalaşma), karma ve grup içi seçim',
 'Bir toplantıya katılan herkes diğer her katılımcıyla birer kez tokalaşmıştır.\nToplam 66 tokalaşma yapılmış, bunların 35’i bir kadın ile bir erkek arasında olmuştur.\nToplantıdaki kadınların sayısı erkeklerin sayısından fazladır.\nBuna göre kadınların kendi aralarında yaptığı tokalaşma sayısı kaçtır?',
 s,'C','Kadınlar arasındaki tokalaşma sayısı.',
 ['Toplam tokalaşma sayısından katılımcı sayısını bul.','Kadın–erkek tokalaşması sayısı, kadın sayısı ile erkek sayısının çarpımıdır.','Toplamı ve çarpımı bilinen iki sayıyı bul; kadınlar fazla.'],[KOMB,TOK],
 [A('Kişi sayısı','Her ikili bir kez tokalaşır.','n × (n − 1) / 2 = 66 ⇒ n × (n − 1) = 132 ⇒ n = 12'),
  A('Kadın–erkek','Her kadın her erkekle bir kez tokalaşır.','k × e = 35 · k + e = 12'),
  A('Sayıları bul','Çarpımı 35, toplamı 12 olan sayılar 7 ve 5; kadınlar fazla.','k = 7 · e = 5'),
  A('Kadınlar arası','7 kadından ikili seçimler.','C(7, 2) = 21'),
  A('Kontrol','Erkekler arası C(5, 2) = 10.','21 + 10 + 35 = 66 ✓')],
 'Karma seçim sayısı iki grubun büyüklüklerinin çarpımıdır; toplam ile birlikte grupları belirler.',
 dict(A='10, kadın sayısını 5 almak; kadınlar erkeklerden fazla.',B='15, 12 kişiyi eşit bölüp kadınları 6 sanmak (C(6, 2)).',D='31, aynı cinsiyettekilerin toplam tokalaşması (66 − 35); erkeklerin kendi aralarındakiler de içinde.',E='35, kadın–erkek tokalaşması; soru kadınların kendi aralarındakini soruyor.'),
 TT(A='dikkat',B='islem',D='dikkat',E='dikkat'))
c=[n for n in range(2,40) if comb(n,2)==28]; assert c==[8]
uyeler=['Mert','Nil']+list('abcdef')
v=sum(1 for g in combinations(uyeler,3) if not {'Mert','Nil'}<=set(g)); assert v==50==comb(8,3)-comb(6,1)
assert comb(6,3)==20 and comb(7,3)==35 and comb(8,3)==56
s=['6','20','35','50','56']; tek_dogru(s,'D',v)
P.K('0008','Bir kulübün üyelerinden oluşturulabilecek 2 kişilik grupların sayısı 28’dir.\nAralarında Mert ve Nil’in de bulunduğu bu üyelerden 3 kişilik bir grup oluşturulacaktır.\nMert ile Nil aynı grupta yer almayacağına göre bu grup kaç farklı biçimde oluşturulabilir?',
 s,'D','Mert ile Nil’in birlikte olmadığı 3 kişilik grup sayısı.',
 ['C(n, 2) = 28 eşitliğinden üye sayısını bul.','Koşulsuz 3 kişilik grup sayısını hesapla.','Mert ile Nil’in birlikte olduğu grupları çıkar.'],[KOMB,TUM],
 [A('Üye sayısı','2 kişilik grup sayısı C(n, 2).','n × (n − 1) / 2 = 28 ⇒ n = 8'),
  A('Tüm gruplar','8 kişiden 3 kişi.','C(8, 3) = 56'),
  A('Mert ve Nil birlikte','İkisi de gruptaysa üçüncü kişi kalan 6 kişiden seçilir.','C(6, 1) = 6'),
  A('Çıkar','İstenmeyen grupları at.','56 − 6 = 50')],
 '“İki kişi birlikte olmayacak” koşulunda ikisinin birlikte olduğu grupları sabitleyip say ve çıkar.',
 dict(A='6, Mert ile Nil’in birlikte olduğu grupların sayısı.',B='20, Mert ile Nil’i hiç almamak (C(6, 3)); ikisinden biri grupta olabilir.',C='35, yalnızca Mert’i dışarıda bırakıp C(7, 3) hesaplamak.',E='56, koşulu kullanmamak.'),
 TT(A='dikkat',B='dikkat',C='islem',E='dikkat'))

P.yaz(os.path.join(H,'permkomb-1.json'),os.path.join(H,'permkomb-1-kardes.json'))
