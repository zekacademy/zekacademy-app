"""AYT Matematik · Permütasyon ve Kombinasyon · 2. dalga · 20 soruluk paket (3 kolay / 10 orta / 7 zor).
Her doğru ve çeldirici değer kaba kuvvetle ya da açıklamadaki hata zincirinden hesaplanıp assert edilir. Kardeş yok, ipucu 1."""
import sys,os,json,math
ADIR=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(ADIR,'..')
sys.path.insert(0,os.path.join(HV,'tyt-mat')); sys.path.insert(0,HV)
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
from math import comb,perm,factorial as F
from itertools import permutations,combinations,product
from fractions import Fraction as Fr
H.KONU='Permütasyon ve Kombinasyon'
UK='amat|Permütasyon ve Kombinasyon'
P=Parti('apermiki','Permütasyon ve Kombinasyon',UK,ders='AYT Matematik',idon='aytmat')
KY='ÖSYM 2018–2026 AYT Matematik (Permütasyon-Kombinasyon: palindrom, kısmi sıralama, koşullu yerleştirme, seçim; yalnız mantık) · yayın soru bankaları · MEB 11. sınıf'
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)
def fig(body,font='\\small'): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font='+font+']\n'+body+'\n\\end{tikzpicture}')
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)
def dist(v,e): assert len({v,*e})==len(e)+1,(v,e)
def sec(dogru,cands,hedef):
    """Aday çeldiricilerden doğru şık hedef harfe düşecek biçimde 4 tanesini seçer."""
    r='ABCDE'.index(hedef); vs=[c[0] for c in cands]; assert dogru not in vs and len(set(vs))==len(vs),(dogru,vs)
    sm=sorted([c for c in cands if c[0]<dogru],key=lambda c:c[0]); lg=sorted([c for c in cands if c[0]>dogru],key=lambda c:c[0])
    assert len(sm)>=r and len(lg)>=4-r,(dogru,hedef,vs)
    return (sm[len(sm)-r:] if r else [])+lg[:4-r]
SIR=['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III']

# ---------- bilgi kutuları (yalnız tanım/gösterim; örnekler soruların sayılarından farklı) ----------
TUM=B('Tümleyen sayma','“en az biri …” koşullu seçimlerde tüm seçimlerin sayısından, hiçbirinin koşulu sağlamadığı seçimlerin sayısı çıkarılır. Örnek: 9 kişiden 3’ü seçilirken belirli 2 kişiden en az biri bulunacaksa C(9, 3) − C(7, 3) = 84 − 35 = 49 seçim vardır')
KOM=B('Kombinasyon ve Pascal özdeşliği','C(n, r) = n!/(r! (n − r)!), C(n, r) = C(n, n − r) ve C(n, r) + C(n, r + 1) = C(n + 1, r + 1) olur. n elemanlı bir kümenin r elemanlı alt kümelerinin sayısı C(n, r) dir. Örnek: C(6, 4) = C(6, 2) = 15')
PER=B('Permütasyon','n farklı elemandan seçilen r tanesinin sıralı dizilişi P(n, r) = n!/(n − r)! tanedir. Örnek: 8 farklı nesneden 3’ü sıralı olarak P(8, 3) = 8 · 7 · 6 = 336 biçimde dizilir')
PAL=B('Palindrom diziliş','soldan ve sağdan okunuşu aynı olan dizilişte yalnız ilk yarı (ortadaki eleman dahil) serbestçe belirlenir, ikinci yarı ilk yarının aynadaki yansıması olur. Örnek: 5 basamaklı palindrom sayıda 3 basamak (ilk üç) belirlenir')
KIS=B('Kısmi sıralama','bazı elemanların diğerlerinden önce gelmesi istenen sıralamalarda önce kuralı hiç kısıtlamayan bir sıra düzeni bulunur, kural sağlayan sıralar doğrudan tek tek ya da parça parça sayılır. Örnek: A, B’den önce gelecek biçimde 3 kişi 3!/2 = 3 farklı sıralanır')
DEN=B('Kombinasyon denklemi','C(n, r) ifadesini n!/(r! (n − r)!) biçiminde açıp sadeleştirerek n için denklem yazılır; n ≥ r ve n doğal sayıdır. Örnek: C(n, 2) = 21 ise n (n − 1) = 42 ve n = 7 olur')
GEO=B('Doğru ve dikdörtgen sayma','bir ızgarada dikdörtgeni, iki yatay ve iki dikey çizgi belirler: C(a, 2) · C(b, 2). İstenen bölgeyi içeren ya da içermeyen dikdörtgenler, tüm dikdörtgenlerden ya da sınır çizgilerinin konumundan sayılır. Örnek: 3 yatay, 4 dikey çizgide C(3, 2) · C(4, 2) = 18 dikdörtgen')
DAG=B('Özdeş nesneleri dağıtma','n özdeş nesne k farklı kutuya (kutular ayırt edilir) dağıtılırken her kutuda en az 1 nesne olacaksa C(n − 1, k − 1) kadar dağılım vardır; kapasite sınırları varsa dağılımlar sınır koşulunu sağlayanlar ayrılarak sayılır. Örnek: 7 özdeş top 3 kutuya, her kutuda en az 1 olacak biçimde C(6, 2) = 15 farklı dağıtılır')
YER=B('Koşullu yerleştirme','aynı satırda ve aynı sütunda iki nesne bulunamıyorsa her satıra en çok bir nesne düşer; yasak kareler varsa her satır sırayla doldurulur ve boş kalan sütun sayıları kontrol edilir. Örnek: 3×3 tahtaya aynı satır ve sütunda olmayan 2 taş C(3, 2) · 3 · 2 = 18 biçimde konur')
ESL=B('Eşleştirme','2n kişi, sırası önemsiz n çifte (2’şerli gruplara) (2n)!/(2ⁿ · n!) biçimde ayrılır. Belirli iki kişinin eşleşmesi istenmiyorsa bu eşleşmeyi içeren ayrılışlar çıkarılır. Örnek: 6 kişi 3 çifte 15 farklı biçimde ayrılır')
KUM=B('Alt küme sayma','bir kümeden koşulu sağlayan alt kümeler, eleman seçimi yapılırken koşul önce yazılarak ya da sıraya dizip araya yerleştirme ile sayılır. Örnek: {1, …, 8} kümesinin ardışık sayı içermeyen 3 elemanlı alt kümeleri C(6, 3) = 20 tanedir')
SIF=B('Şifre sayma','her kutuya yazılabilecek karakter kümeleri verildiğinde, kutular sırayla doldurulur; “farklı” koşulunda seçenek sayısı bir azalır, “tekrar edilebilir” koşulunda azalmaz. Örnek: 3 kutuluk şifrede 1. ve 3. kutu aynı 4 harften farklı seçilirse 4 · 3 = 12 harf çifti olur')
TKR=B('Tekrarlı permütasyon','n elemanın n₁ tanesi birbirinin aynı, n₂ tanesi birbirinin aynı … ise dizilişlerin sayısı n!/(n₁! · n₂! …) tanedir. Örnek: 1, 1, 1, 2, 2 rakamlarıyla 5 basamaklı 5!/(3! · 2!) = 10 sayı yazılır')

KES=B('Doğruların kesişimi','düzlemde farklı iki doğru ya paraleldir ya da tam bir noktada kesişir; n doğru çifti sayısı C(n, 2) dir. Örnek: 4 doğrunun ikisi paralel ise en çok C(4, 2) − 1 = 5 kesişim noktası bulunabilir')
# ---------- kartlar ----------
kartla('K-APER2-01','Takvim ve tümleyen seçim','Şekilden gün sayıları okunur; “en az biri” koşulu tümleyenle ya da durumlara ayırarak sayılır; seçimde sıra gözetilmez.','Sıralı seçim yapıp ikiye katlamak; “tam biri” ile “en az biri”ni karıştırmak; ortak durumu iki kez saymak.','kolay','hikâyeli',3,'pk-takvim','Takvim ve tümleyen seçim')
kartla('K-APER2-02','Şifre ve kutu doldurma','Her kutunun seçenek kümesi şekilden okunur; “farklı olmalı” koşulunda seçenek sayısı azalır, tekrar serbestse azalmaz; öncüllü yargılar ayrı ayrı sayılır.','Farklı olması gereken kutularda seçenek sayısını azaltmamak; kutu seçeneklerini toplamak; koşullu yargıda durumları iki kez saymak.','orta','yeni nesil',4,'pk-sifre','Şifre ve kutu doldurma')
kartla('K-APER2-03','Palindrom dizilişler','Palindromda ilk yarı serbest seçilir, ikinci yarı yansımadır; bölünebilme gibi ek koşul yansımış basamaklara uygulanır.','Palindromda bütün basamakları serbest saymak; yansıyan basamağın koşulunu karıştırmak; baştaki sıfırı unutmak.','orta','şekilli',4,'pk-palindrom','Palindrom dizilişler')
kartla('K-APER2-04','Kısmi sıralama ve öncelik şeması','Okların “önce” ilişkisini gösterdiği şemada her uygun sıra, kaynak kümeden başlayarak tek tek sayılır; koşul sayısı arttıkça sıra sayısı azalır.','Oklarla bağlı olmayan görevlerin yer değişimini unutmak; öncelik ilişkisini iki yönlü sanmak; aynı sırayı iki kez saymak.','orta','şekilli',4,'pk-kismi','Kısmi sıralama ve öncelik şeması')
kartla('K-APER2-05','Kombinasyon denklemi ve alt küme sayısı','C(n, r) açılıp sadeleştirilerek n bulunur; alt küme sayıları C(n, r) ile yazılır; C(n, r) = C(n, n − r) kullanılır.','C(n, r) ve P(n, r) tanımlarını karıştırmak; n yerine n + 1 almak; faktöriyel sadeleştirmesinde çarpan atlamak.','orta','yeni nesil',4,'pk-denklem','Kombinasyon denklemi ve alt küme sayısı')
kartla('K-APER2-06','Doğru ve ızgara üzerinde sayma','Dikdörtgeni iki yatay ve iki dikey çizgi belirler; belli bölgeyi içeren dikdörtgenlerde çizgi seçimi bölgenin iki yanından yapılır; aynı noktadan geçen doğrular ortak noktayı tek sayar.','Tüm dikdörtgenlerden yasaklıları çıkarırken çakışmayı iki kez çıkarmak; paralel doğruların kesişmediğini unutmak; üç doğrunun ortak noktasını üç kez saymak.','orta','şekilli',4,'pk-sekil','Doğru ve ızgara üzerinde sayma')
kartla('K-APER2-07','Özdeş nesneleri kapasiteli dağıtma','Kutular farklı, nesneler özdeşse her kutudaki nesne sayısı bir üçlü yazılır; en az ve en çok koşulu sayıları sınırlar; geçerli üçlüler tek tek sayılır.','Kapasiteyi ya da “en az 1” koşulunu atlamak; nesneleri farklı sanıp sıralamak; üçlülerin sırasını yok saymak.','orta','şekilli',4,'pk-dagitim','Özdeş nesneleri kapasiteli dağıtma')
kartla('K-APER2-08','Yasak karelerle yerleştirme','Her satıra en çok bir nesne düşer; yasak kareli satırlar önce işlenir; kullanılan sütunlar bir sonraki satırın seçeneklerini azaltır.','Yasak kareleri hiç hesaba katmamak; yalnız satır koşulunu uygulayıp sütun koşulunu unutmak; satır seçimini sıralı saymak.','orta','şekilli',4,'pk-yerlesim','Yasak karelerle yerleştirme')
kartla('K-APER2-09','Koşullu alt küme ve seçim','Koşul (ardışık olmama, toplam, çift-tek) durumlara ayrılıp ya da araya yerleştirme ile sayılır; çember üzerinde başlangıç noktası seçilen dizilimde ilk ve son komşuluğu ayrıca ele alınır.','Çemberde ilk ve son elemanın komşu olduğunu unutmak; durumlardan birini atlamak; seçimde sıra saymak.','zor','şekilli',5,'pk-kume','Koşullu alt küme ve seçim')
kartla('K-APER2-10','Eşleştirme ve koşullu gruplama','Adlandırılmamış çiftlerde grup sayısına bölme düzeltmesi yapılır; istenmeyen eşleşmeler içerme-dışarma ile çıkarılır.','Grupları adlandırılmış saymak; iki istenmeyen eşleşmenin ortak durumunu iki kez çıkarmak; eşleştirme yerine seçim yapmak.','zor','hikâyeli',5,'pk-eslestirme','Eşleştirme ve koşullu gruplama')

# ================= 01 kolay · takvim, en az biri =================
gun=[[1,2,3,4,5],[8,9,10,11,12],[15,16,17,18,19],[22,23,24,25,26]]; boyali={3,9,12,17,24,26}
tum=[g for r in gun for g in r]; assert len(tum)==20 and len(boyali)==6
v=comb(20,2)-comb(14,2); assert v==99==sum(1 for a,b in combinations(tum,2) if a in boyali or b in boyali)
e=[(comb(6,2),'Yalnızca boyalı günlerden iki gün seçmiş: C(6, 2) = 15.','dikkat'),(6*14,'“Tam biri boyalı” durumunu saymış: 6 · 14 = 84; ikisinin de boyalı olduğu seçimleri unutmuş.','dikkat'),
   (comb(14,2),'Boyalı gün içermeyen seçimlerin sayısını vermiş: C(14, 2) = 91.','islem'),(6*19,'Önce boyalı günü, sonra kalan 19 günden birini seçip sırayı da önemli saymış: 6 · 19 = 114.','bilgi'),(6*20,'Boyalı gün seçip ikinci günü 20 günün tamamından seçmiş: 6 · 20 = 120.','islem')]
assert [x[0] for x in e]==[15,84,91,114,120]
o=['\\foreach \\i/\\n in {0/Pzt,1/Sal,2/Çar,3/Per,4/Cum}{\\node[font=\\small\\bfseries,minimum width=1cm] at (\\i*1.05+0.5,0.45) {\\n};}']
for r,row in enumerate(gun):
    for c,d in enumerate(row):
        fl='orange!45' if d in boyali else 'blue!6'
        o.append(f'\\draw[thick,fill={fl}] ({c*1.05},{-r*0.75-0.0}) rectangle ({c*1.05+1.0},{-r*0.75-0.7}); \\node[font=\\small\\bfseries] at ({c*1.05+0.5},{-r*0.75-0.35}) {{{d}}};')
o.append('\\draw[thick,fill=orange!45] (0,-3.5) rectangle (0.4,-3.9); \\node[anchor=west,font=\\small] at (0.5,-3.7) {: yönetim kurulu günü};')
SK=fig('\n'.join(o))
q('0001',tipId='pk-takvim',tip='Takvim ve tümleyen seçim',z='kolay',alt='Seçim ve Tümleyen Sayma',kaz='Takvim şemasındaki gün sayılarını okuyup “en az biri” koşullu seçim sayısını tümleyenle hesaplar.',kalip='şekilli',
 kart='K-APER2-01 (takvim) · 20 iş gününden iki gün; en az biri işaretli',
 metin='Bir şirkette, şekildeki takvim yaprağında gösterilen 20 iş gününün 6’sı (boyalı günler) yönetim kurulu günüdür. Şirket müdürü, bu 20 iş gününden birbirinden farklı iki gün seçip bu günlerde birer toplantı yapacaktır. Toplantılardan en az biri yönetim kurulu gününe denk gelecektir.\nBuna göre bu seçim kaç farklı biçimde yapılabilir?',
 dogru=v,yan=sec(v,e,'C'),istenen='Toplantı günlerinin koşulu sağlayan seçimlerinin sayısı.',ip=['Koşulu sağlamayan seçimler kaç gün arasından yapılır?'],bilgi=[TUM],sekil=SK,
 ad=[A('Tüm seçimleri say','20 günden sıra gözetmeden iki gün seçilir.','C(20, 2) = 190'),A('Koşulu sağlamayanları say','Hiçbiri yönetim kurulu günü olmayan seçimlerde 14 gün vardır.','C(14, 2) = 91'),A('Çıkar','Tüm seçimlerden koşulu sağlamayanlar çıkarılır.','190 − 91 = 99')],
 puf='“En az biri” içeren koşullarda tümleyen durumu düşünmek işi kısaltabilir.')

# ================= 02 kolay · kombinasyon denklemi =================
sol=[n for n in range(3,60) if comb(n+2,3)==4*comb(n+1,2)]; assert sol==[10]; v=10
e=[(4,'C(n + 2, 3) açılımında paydayı 3! yerine 3 almış: (n + 2)/3 = 2 ve n = 4.','islem'),(12,'(n + 2)/6 = 2 denkleminden n + 2 = 12 bulup n + 2’yi n sanmış.','dikkat'),(14,'n + 2 = 12 bulduktan sonra 2’yi çıkarmak yerine eklemiş: n = 14.','islem'),(22,'Sağ tarafta C(n + 1, 2) yerine P(n + 1, 2) kullanmış: (n + 2)/6 = 4 ve n = 22.','bilgi'),(8,'(n + 2)/6 = 2 denkleminde 6’yı yanlış yerden bölüp (n + 2)·... çözümünü n = 8 bulmuş (n + 2 = 10 yerine n = 8).','islem')]
assert (4+2)/3==2 and 12//6==2 and (22+2)/6==4
e=e[:4]
q('0002',tipId='pk-denklem',tip='Kombinasyon denklemi ve alt küme sayısı',z='kolay',alt='Kombinasyon',kaz='Kombinasyon denklemini açıp sadeleştirerek bilinmeyen n değerini bulur.',kalip='düz',
 kart='K-APER2-05 (denklem) · C(n + 2, 3) = 4 · C(n + 1, 2)',
 metin='n ≥ 2 bir doğal sayı olmak üzere,\nC(n + 2, 3) = 4 · C(n + 1, 2)\neşitliği veriliyor.\nBuna göre n kaçtır?',
 dogru=v,yan=sec(v,e,'B'),istenen='n doğal sayısının değeri.',ip=['Her iki kombinasyonu faktöriyel kullanmadan çarpım biçiminde yazıp ortak çarpanları sadeleştir.'],bilgi=[DEN],
 ad=[A('Kombinasyonları aç','C(n + 2, 3) = (n + 2)(n + 1)n/6 ve C(n + 1, 2) = (n + 1)n/2 olur.','(n + 2)(n + 1)n/6 = 4 · (n + 1)n/2'),A('Sadeleştir','(n + 1)n ortak çarpanı sadeleşir (n ≥ 2).','(n + 2)/6 = 2'),A('Çöz','Denklem n için çözülür.','n + 2 = 12 ve n = 10')],
 puf='Kombinasyon denklemlerinde ortak çarpanları sadeleştirmeden önce n ≥ r koşulunu not et.')

# ================= 03 kolay · şifre =================
kut=[list('KLMNP'),[2,4,6,8],[2,4,6,8],list('KLMNP')]
v=sum(1 for a,b,c,d in product(*kut) if a!=d); assert v==320==5*4*4*4
e=[(5*4*4,'Rakam kutularından birini hesaba katmamış: 5 · 4 · 4 = 80.','dikkat'),(5*4*3*4,'Rakamların da farklı olması gerektiğini sanmış: 5 · 4 · 3 · 4 = 240.','bilgi'),(5*4*4*5,'Harf kutularında tekrarı serbest saymış: 5 · 4 · 4 · 5 = 400.','dikkat'),(5**4,'Hiçbir koşulu uygulamadan her kutuya 5 seçenek saymış: 5⁴ = 625.','bilgi'),(5*4+4*4,'İlk iki aşamayı toplayıp çarpma kuralını unutmuş: 5 · 4 + 4 · 4 = 36.','bilgi')]
assert [x[0] for x in e]==[80,240,400,625,36]
o=[]
etk=[('1. kutu','K  L  M\\\\N  P'),('2. kutu','2  4\\\\6  8'),('3. kutu','2  4\\\\6  8'),('4. kutu','K  L  M\\\\N  P')]
for i,(a,b) in enumerate(etk):
    fl='blue!12' if i in (0,3) else 'green!14'
    o.append(f'\\draw[thick,fill={fl},rounded corners=2pt] ({i*2.1},0) rectangle ({i*2.1+1.9},1.4); \\node[font=\\small\\bfseries] at ({i*2.1+0.95},1.75) {{{a}}}; \\node[font=\\normalsize\\bfseries,align=center] at ({i*2.1+0.95},0.7) {{{b}}};')
SK=fig('\n'.join(o))
q('0003',tipId='pk-sifre',tip='Şifre ve kutu doldurma',z='kolay',alt='Çarpma Kuralı',kaz='Kutularına yazılabilecek karakterler verilen bir şifrede “farklı olma” koşulunu da kullanarak şifre sayısını bulur.',kalip='şekilli',
 kart='K-APER2-02 (şifre) · iki farklı harf kutusu, tekrar edebilen rakam kutuları',
 metin='Şekildeki gibi dört kutudan oluşan bir şifrede her kutuya, o kutunun altında gösterilen karakterlerden yalnızca biri yazılacaktır. 1. ve 4. kutulara yazılan harfler birbirinden farklı olacak; 2. ve 3. kutulara yazılan rakamlar aynı ya da farklı olabilecektir.\nBuna göre bu koşullara uygun kaç farklı şifre oluşturulabilir?',
 dogru=v,yan=sec(v,e,'C'),istenen='Koşullara uygun şifre sayısı.',ip=['Her kutunun seçenek sayısını şekilden oku; 4. kutu 1. kutuya bağlı mı?'],bilgi=[SIF],sekil=SK,
 ad=[A('Seçenek sayıları','1. kutuda 5 harf, 4. kutuda ilk harf dışındaki 4 harf; rakam kutularında 4’er seçenek vardır.','5 · 4 · 4 · 4'),A('Çarp','Ardışık bağımsız seçimler çarpılır.','5 · 4 = 20 ve 4 · 4 = 16'),A('Hesapla','Çarpımlar birleştirilir.','20 · 16 = 320')],
 puf='Kutu kutu ilerle ve “farklı olmalı” diyen kutuda seçenek sayısını bir azalt.')

# ================= 04 orta · palindrom =================
def pal6(d):
    return [(a,b,c) for a in range(1,5) for b in range(5) for c in range(5)]
cnt=lambda f:sum(1 for a,b,c in pal6(0) if f(a,b,c)); num=lambda a,b,c:int(f'{a}{b}{c}{c}{b}{a}')
v=cnt(lambda a,b,c:num(a,b,c)%4==0); assert v==25==sum(1 for n in range(100000,1000000) if str(n)==str(n)[::-1] and set(str(n))<=set('01234') and n%4==0)
ters=cnt(lambda a,b,c:(10*a+b)%4==0); cift=cnt(lambda a,b,c:a%2==0)
assert (ters,cift)==(30,50)
e=[(len(pal6(0)),'Bölünebilme koşulunu uygulamadan bütün palindromları saymış: 4 · 5 · 5 = 100.','bilgi'),(cift,'4’e bölünmeyi yalnız son basamağın çift olmasına indirgemiş: 2 · 5 · 5 = 50.','dikkat'),(ters,'Son iki basamağı b ve a yerine a ve b sanıp “ab” iki basamaklı sayısının 4’e bölünmesine bakmış; palindromun yansımasını yanlış okumuş: 30.','dikkat'),(25//5,'c basamağını koşulla ilgisiz sanıp yok saymış: 25/5 = 5.','islem')]
o=[]
for i in range(6):
    o.append(f'\\draw[thick,fill=blue!8] ({i*1.0},0) rectangle ({i*1.0+0.9},0.9);')
for (i,j,h,cl) in ((0,5,1.5,'blue!70!black'),(1,4,1.0,'orange!85!black'),(2,3,0.55,'green!50!black')):
    o.append(f'\\draw[{cl},line width=1.6pt] ({i+0.45},0.9) -- ({i+0.45},{0.9+h}) -- ({j+0.45},{0.9+h}) -- ({j+0.45},0.9);')
o.append('\\node[font=\\small] at (2.95,-0.55) {her kutuya 0, 1, 2, 3 ya da 4 yazılır};')
SK=fig('\n'.join(o))
q('0004',tipId='pk-palindrom',tip='Palindrom dizilişler',z='orta',alt='Palindrom Sayılar',kaz='Palindrom sayıların basamaklarını yansıma ilişkisiyle yazıp 4’e bölünebilme koşuluyla sayar.',kalip='şekilli',
 kart='K-APER2-03 (palindrom sayı) · 6 basamaklı, rakamlar {0, …, 4}, 4’e bölünür',
 metin='Soldan sağa ve sağdan sola okunuşu aynı olan sayılara palindrom sayı denir. Şekildeki altı kutuya soldan sağa birer rakam yazılarak 6 basamaklı palindrom sayılar oluşturuluyor; aynı renkli çizgilerle bağlı kutulardaki rakamlar aynıdır ve en soldaki kutuya 0 yazılamaz.\nBuna göre bu sayılardan kaç tanesi 4 ile tam bölünür?',
 dogru=v,yan=sec(v,e,'B'),istenen='4 ile tam bölünen palindrom sayıların sayısı.',ip=['Sayının 4’e bölünüp bölünmediğini belirleyen basamaklar hangi kutulardır ve bunlar hangi kutularla eşlenmiştir?'],bilgi=[PAL],sekil=SK,
 ad=[A('Palindromu yaz','Sayı abccba biçimindedir; a ≠ 0.','a ∈ {1, 2, 3, 4}; b, c ∈ {0, 1, 2, 3, 4}'),A('Bölünebilmeyi uygula','Son iki basamak “ba” sayısı 4’e bölünmelidir; a çift olmalıdır.','a = 2 için b ∈ {1, 3}; a = 4 için b ∈ {0, 2, 4}'),A('(a, b) çiftlerini say','Geçerli çiftler sayılır.','2 + 3 = 5 çift'),A('c’yi ekle','c basamağı koşuldan bağımsızdır.','5 · 5 = 25')],
 puf='Palindromlarda bölünebilme koşulu, sayının son basamaklarını eşlediği ilk yarı basamaklarına çevrilir.')

# ================= 05 orta · kısmi sıralama (öncelik şeması) =================
ed=[(0,3),(1,3),(1,4),(2,4),(3,5),(4,5)]
v=sum(1 for p in permutations(range(6)) if all(p.index(a)<p.index(b) for a,b in ed)); assert v==16
f5=lambda E:sum(1 for p in permutations(range(6)) if all(p.index(a)<p.index(b) for a,b in E))
e=[(f5([x for x in ed if x!=(1,4)]),'B görevinin E’den önce gelmesi koşulunu unutmuş; yalnız beş okun koşulunu uygulamış: 20.','dikkat'),(f5([x for x in ed if x!=(4,5)]),'E → F okunu atlayıp F’nin yalnız D’den sonra gelmesini istemiş: 26.','dikkat'),(f5([x for x in ed if x!=(0,3)]),'A → D okunu hesaba katmamış: 30.','dikkat'),(f5(ed[:4]),'F görevinin D ve E’den sonra gelmesi koşullarını unutmuş: 96.','bilgi')]
assert [x[0] for x in e]==[20,26,30,96]
pos={0:(0,1.6),1:(0,0.0),2:(0,-1.6),3:(2.2,1.2),4:(2.2,-0.8),5:(4.4,0.2)}
o=[f'\\node[circle,draw,thick,fill=yellow!30,minimum size=0.8cm,font=\\bfseries] (n{i}) at ({x},{y}) {{{"ABCDEF"[i]}}};' for i,(x,y) in pos.items()]
o+=[f'\\draw[-{{Stealth}},line width=1.6pt,blue!70!black] (n{a}) -- (n{b});' for a,b in ed]
SK=fig('\n'.join(o))
q('0005',tipId='pk-kismi',tip='Kısmi sıralama ve öncelik şeması',z='orta',alt='Kısmi Sıralama',kaz='Öncelik oklarıyla verilen görevlerin koşulu sağlayan yapılış sıralarını sayar.',kalip='şekilli',
 kart='K-APER2-04 (öncelik şeması) · 6 görev, 6 öncelik oku',
 metin='Bir yazılım ekibinin A, B, C, D, E ve F adlı altı görevi şekildeki öncelik şemasında gösterilmiştir. Şemada X → Y oku, X görevi tamamlanmadan Y görevine başlanamayacağını göstermektedir. Görevler aynı anda yalnızca biri yapılacak biçimde art arda tamamlanacaktır.\nBuna göre bu altı görev kaç farklı sırayla yapılabilir?',
 dogru=v,yan=sec(v,e,'A'),istenen='Koşulları sağlayan görev sıralarının sayısı.',ip=['İlk yapılabilecek görevler hangileridir?'],bilgi=[KIS],sekil=SK,
 ad=[A('Son görevi belirle','F’ye gelen her ok D ve E’den gelir; F, D ve E tamamlanmadan yapılamaz ve en sona kalır.','Sıranın 6. görevi: F'),A('Kalan beş görevi ayır','A, B, C, D, E için kurallar: A, B → D ve B, C → E.','D, A ile B’den sonra; E, B ile C’den sonra'),A('Durumlara ayır','5. sırada D ya da E bulunur; diğeri 4. sıradadır. 5. sırada D olsun: E, B ile C’den sonra ama D’den önce, A ve B de D’den önce.','D en sonda: A, B, C, E sıralamasında B, C → E koşulu ile 4!/3 = 8'),A('Simetrik durumu ekle','5. sırada E olduğunda aynı sayılır.','8 + 8 = 16')],
 puf='Öncelik şemalarında en sona kalan görevden başlayıp geriye doğru sırala.')

# ================= 06 orta · puan toplamı koşullu seçim =================
sor=[2]*5+[3]*4+[5]*3
v=sum(1 for c in combinations(range(12),3) if sum(sor[i] for i in c)==9); assert v==34==comb(5,2)*3+comb(4,3)
e=[(comb(5,2)*3,'3 puanlık üç soruyu seçme durumunu (3 + 3 + 3) unutmuş: C(5, 2) · 3 = 30.','dikkat'),(comb(4,3),'Yalnızca 3 + 3 + 3 durumunu saymış: C(4, 3) = 4.','bilgi'),(5*4*3+comb(4,3),'2 puanlık iki soruyu sıralı seçmiş (5 · 4 · 3 = 60) ve 4 ile toplamış: 64.','dikkat'),(comb(5,2)*3+4*3*2,'3 puanlık üç soruyu sıralı seçmiş: 30 + 4 · 3 · 2 = 54.','dikkat'),(5*4*3,'2 + 2 + 5 yerine 2 + 3 + 5’i seçmiş: 5 · 4 · 3 = 60.','dikkat')]
assert [x[0] for x in e]==[30,4,64,54,60]
q('0006',tipId='pk-kume',tip='Koşullu alt küme ve seçim',z='orta',alt='Seçim',kaz='Puan toplamı koşuluna göre durumlara ayırarak farklı soruların seçim sayısını bulur.',kalip='hikâyeli',
 kart='K-APER2-09 (toplam koşullu seçim) · 2, 3 ve 5 puanlık sorulardan üç soru',
 metin='Bir deneme sınavı için hazırlanan soru havuzunda, birbirinden farklı 5 tane 2 puanlık, 4 tane 3 puanlık ve 3 tane 5 puanlık soru bulunmaktadır. Bu havuzdan 3 soru seçilerek, puanları toplamı 9 olan bir kısa sınav oluşturulacaktır; sorular sınavda sıralanmayacaktır.\nBuna göre bu sınav kaç farklı biçimde oluşturulabilir?',
 dogru=v,yan=sec(v,e,'C'),istenen='Toplamı 9 puan olan üç soruluk seçimlerin sayısı.',ip=['Üç tam sayı puanının toplamı 9 yapabilecek hangi puan dağılımları vardır?'],bilgi=[KOM],
 ad=[A('Puan dağılımlarını bul','Üç sorunun puanları 2, 3, 5 değerlerinden toplamı 9 olacak biçimde seçilir.','2 + 2 + 5 ve 3 + 3 + 3'),A('2+2+5 durumu','2 puanlık 5 sorudan 2’si, 5 puanlık 3 sorudan 1’i seçilir.','C(5, 2) · C(3, 1) = 10 · 3 = 30'),A('3+3+3 durumu','3 puanlık 4 sorudan 3’ü seçilir.','C(4, 3) = 4'),A('Durumları topla','Durumlar birbirinin yerine geçer.','30 + 4 = 34')],
 puf='Toplam koşullarında önce puan dağılımlarını yaz, sonra her dağılımı ayrı say.')

# ================= 07 orta · öncüllü, 3 elemanlı alt kümeler =================
S=range(1,10); alt3=list(combinations(S,3))
c1=sum(1 for t in alt3 if sum(t)%2==0); c2=sum(1 for t in alt3 if max(t)==6); c3=sum(1 for t in alt3 if all(b-a>1 for a,b in zip(t,t[1:])))
assert (c1,c2,c3)==(44,10,35)
c4=sum(1 for t in alt3 if True)
assert comb(5,3)+comb(4,2)*5==40 and comb(9,3)-7==77 and comb(6,2)==15 and comb(5,2)==10
q('0007',tipId='pk-kume',tip='Koşullu alt küme ve seçim',z='orta',alt='Alt Küme Sayısı',kaz='Bir kümenin 3 elemanlı alt kümelerini eleman toplamı, en büyük eleman ve ardışık olmama koşullarıyla sayar.',kalip='öncüllü',
 kart='K-APER2-09 (alt küme öncülleri) · {1, …, 9} kümesinin üç elemanlı alt kümeleri',
 metin='A = {1, 2, 3, 4, 5, 6, 7, 8, 9} kümesinin 3 elemanlı alt kümeleri için,\nI. Elemanları toplamı çift olanlar 44 tanedir.\nII. En büyük elemanı 6 olanlar 15 tanedir.\nIII. Ardışık iki doğal sayıyı birlikte içermeyenler 35 tanedir.\nifadelerinden hangileri doğrudur?',
 dogru='I ve III',yan=[('Yalnız I','III. öncülde ardışık içeren alt kümeleri yalnız {1,2,3}, …, {7,8,9} biçimindeki 7 üçlü sanıp 84 − 7 = 77 bulmuş; II’yi de yanlış saymış.','bilgi'),('Yalnız II','I’de tek ve çift sayı adetlerini ters alıp (4 tek, 5 çift) C(5, 3) + C(4, 2) · 5 = 40 bulmuş, III’te 77 bulmuş; II’deki C(6, 2) = 15 hesabını doğru saymış.','dikkat'),('I ve II','III’te ardışık olanları 7 üçlü sanıp 77 bulmuş; II’de 6’yı da seçilebilecek elemanlara katıp C(6, 2) = 15 hesaplamış.','dikkat'),('I, II ve III','II’de en büyük eleman 6 olduğundan geri kalan iki eleman 1, …, 6 arasından seçilir sanıp C(6, 2) = 15 bulmuş; diğer iki öncülü doğru saymış.','dikkat')],
 sira=SIR,istenen='Doğru olan öncüllerin hangileri olduğu.',ip=['Her öncülü ayrı ayrı say; tek-çift ayrımı I. öncülde işe yarar.'],bilgi=[KUM,KOM],
 ad=[A('I. öncülü say','Tek eleman sayısı 5, çift eleman sayısı 4’tür; toplamın çift olması için 0 ya da 2 tek eleman bulunur.','C(4, 3) + C(5, 2) · C(4, 1) = 4 + 40 = 44 · doğru'),A('II. öncülü say','Üç elemandan en büyüğü 6 ise diğer ikisi 1, …, 5 içinden seçilir.','C(5, 2) = 10 ≠ 15'),A('III. öncülü say','Ardışık olmayan 3 eleman, 9 − 3 + 1 = 7 seçenekli bir seçime denk gelir.','C(7, 3) = 35 · doğru'),A('Sonuç','I ve III öncülleri doğrudur.','I ve III')],
 puf='Öncüllü sayma sorularında her öncülü ayrı sayıya indirip sonra karşılaştır.')
assert c1==44 and c3==35 and c2==10

# ================= 08 orta · boyalı kareyi içeren dikdörtgenler =================
Wc,Hc=5,4; bc,br=3,2  # boyalı kare: 3. sütun, alt sıradan 2. satır
def dikd(f):
    n=0
    for x1,x2 in combinations(range(Wc+1),2):
        for y1,y2 in combinations(range(Hc+1),2):
            if f(x1,x2,y1,y2): n+=1
    return n
v=dikd(lambda x1,x2,y1,y2:x1<bc<=x2 and y1<br<=y2); tum=dikd(lambda *a:True)
assert v==3*3*2*3==54 and tum==150 and dikd(lambda x1,x2,y1,y2:not(x1<bc<=x2 and y1<br<=y2))==96
e=[(9+6,'Yatay ve düşey seçim sayılarını çarpmak yerine toplamış: 3 · 3 + 2 · 3 = 15.','bilgi'),(tum-v,'Boyalı kareyi içermeyen dikdörtgenleri saymış: 150 − 54 = 96.','dikkat'),(tum,'Boyalı kare koşulunu hiç uygulamadan bütün dikdörtgenleri saymış: C(6, 2) · C(5, 2) = 150.','bilgi'),(2*4*2*3,'Boyalı kareyi 2. sütunda sanıp seçenekleri 2 · 4 · 2 · 3 almış: 48.','dikkat'),(3*3*2,'Üst kenarı seçmeyi unutup 3 · 3 · 2 hesaplamış.','dikkat'),(3*2*3*2,'Sol-sağ ve alt-üst kenarlarda seçenek sayılarını 3, 2, 3, 2 almış (kareyi tek bir çizgi aralığına bağlamış).','dikkat')]
assert [x[0] for x in e]==[15,96,150,48,18,36]
o=[]
for r in range(Hc):
    for c in range(Wc):
        fl='orange!55' if (c+1,r+1)==(bc,br) else 'blue!6'
        o.append(f'\\draw[thick,fill={fl}] ({c*0.9},{r*0.9}) rectangle ({c*0.9+0.9},{r*0.9+0.9});')
SK=fig('\n'.join(o)+f'\n\\node[font=\\small] at ({Wc*0.45},-0.45) {{boyalı kare}};')
q('0008',tipId='pk-sekil',tip='Doğru ve ızgara üzerinde sayma',z='orta',alt='Izgarada Dikdörtgen Sayma',kaz='Izgarada boyalı kareyi içeren dikdörtgenlerin sayısını çizgi seçimleriyle bulur.',kalip='şekilli',
 kart='K-APER2-06 (dikdörtgen sayma) · 5 × 4 ızgara, tek boyalı kare',
 metin='Şekildeki 5 × 4’lük ızgara, birim karelerden oluşmaktadır ve karelerden biri boyalıdır. Kenarları ızgara çizgileri üzerinde olan dikdörtgenler çiziliyor.\nBuna göre, boyalı kareyi içeren (kareler dahil) kaç farklı dikdörtgen çizilebilir?',
 dogru=v,yan=sec(v,e,'E'),istenen='Boyalı kareyi içeren dikdörtgenlerin sayısı.',ip=['Dikdörtgenin boyalı kareyi içermesi için sol, sağ, alt ve üst kenarları nasıl seçilmelidir?'],bilgi=[GEO],sekil=SK,
 ad=[A('Sol ve sağ çizgiyi seç','Sol çizgi boyalı karenin sol kenarında ya da daha solunda, sağ çizgi sağ kenarında ya da daha sağında olmalıdır.','Sol: 3 seçenek · Sağ: 3 seçenek'),A('Alt ve üst çizgiyi seç','Alt çizgi boyalı karenin alt kenarında ya da daha aşağısında, üst çizgi üst kenarında ya da daha yukarısında olmalıdır.','Alt: 2 seçenek · Üst: 3 seçenek'),A('Çarp','Dört seçim bağımsızdır.','3 · 3 · 2 · 3 = 54')],
 puf='Belirli bir bölgeyi içeren dikdörtgenlerde kenar çizgilerini bölgenin iki yanından ayrı ayrı seç.')

# ================= 09 orta · kapasiteli dağıtım =================
cap=(3,4,5)
dag=lambda N,lo,hi:sum(1 for t in product(*[range(lo,c+1) for c in hi]) if sum(t)==N)
v=dag(8,1,cap); k1=dag(8,1,(8,8,8)); k2=dag(8,0,cap); k3=dag(8,0,(8,8,8)); k4=dag(8,1,(3,8,8))
assert k1==comb(7,2)==21 and k3==comb(10,2)==45
print('dag',v,k1,k2,k3,k4)
e=[(k2,'“Her kutuda en az 1 top” koşulunu unutmuş, yalnız kapasiteleri uygulamış: 14.','dikkat'),(k4,'Yalnız 1. kutunun kapasitesini dikkate almış: 15.','dikkat'),(k1,'Kapasiteleri hiç hesaba katmayıp C(7, 2) = 21 bulmuş.','bilgi'),(k3,'Hiçbir koşulu uygulamadan C(10, 2) = 45 bulmuş.','bilgi')]
o=[]
for r,c in enumerate(cap):
    y=-r*1.0
    o.append(f'\\node[font=\\small\\bfseries,anchor=east] at (-0.1,{y+0.35}) {{{r+1}. kutu}};')
    for j in range(c): o.append(f'\\draw[thick,fill=blue!10] ({j*0.7},{y}) rectangle ({j*0.7+0.65},{y+0.7});')
SK=fig('\n'.join(o)+'\n\\node[font=\\small] at (1.8,-2.75) {her kare bir topluk yer};')
q('0009',tipId='pk-dagitim',tip='Özdeş nesneleri kapasiteli dağıtma',z='orta',alt='Dağıtım',kaz='Kapasiteleri şekilden okunan kutulara özdeş nesneleri, her kutuda en az bir nesne bulunacak biçimde dağıtmanın yollarını sayar.',kalip='şekilli',
 kart='K-APER2-07 (kapasiteli dağıtım) · 8 özdeş nesne, kapasiteler 3, 4, 5',
 metin='Şekilde üç kutu ve her kutunun alabileceği en çok top sayısı (kare sayısı kadar) gösterilmiştir. Birbirinin aynı 8 top bu kutulara, her kutuda en az bir top bulunacak ve hiçbir kutuya kapasitesinden fazla top konmayacak biçimde dağıtılacaktır.\nBuna göre bu dağıtım kaç farklı biçimde yapılabilir?',
 dogru=v,yan=sec(v,e,'A'),istenen='Koşullara uygun dağıtımların sayısı.',ip=['Birinci kutuya konabilecek top sayısına göre durumları ayır.'],bilgi=[DAG],sekil=SK,
 ad=[A('1. kutuya göre ayır','1. kutuda 1, 2 ya da 3 top bulunur; kalan toplar 2. ve 3. kutulara paylaşılır.','1. kutu: 1, 2, 3'),A('Her durumu say','Kalan toplar için (2. kutu, 3. kutu) ikilileri kapasiteye ve “en az 1” koşuluna göre listelenir.','1 top → (2, 5), (3, 4), (4, 3): 3 · 2 top → (1, 5), (2, 4), (3, 3), (4, 2): 4 · 3 top → (1, 4), (2, 3), (3, 2), (4, 1): 4'),A('Topla','Durumlar birbirinin yerine geçer.','3 + 4 + 4 = 11')],
 puf='Kapasiteli dağıtımlarda bir kutuya göre durumlara ayırıp kalan kutuları listele.')

# ================= 10 orta · yasak karelerle yerleştirme =================
yas={(1,1),(2,3),(4,2)}   # (satır,sütun), 1. satır üstte
free=[[c for c in range(1,5) if (r,c) not in yas] for r in range(1,5)]
v=sum(1 for rows in combinations(range(4),3) for t in product(*[free[r] for r in rows]) if len(set(t))==3)
v_ihm=comb(4,3)*perm(4,3); v_sat=sum(1 for rows in combinations(range(4),3) for t in product(*[free[r] for r in rows]))
v_kar=comb(13,3); v_sat_sut=sum(1 for rows in combinations(range(4),3) for t in product(*[range(1,5)]*3) if len(set(t))==3 and not any((r+1,c) in yas for r,c in zip(rows,t)))
assert v_sat_sut==v
assert 96-3*18==42
per=[sum(1 for t in product(*[free[r] for r in rows]) if len(set(t))==3) for rows in combinations(range(4),3)]
assert sum(per)==v
e=[(96-3*18,'Her yasak kareyi içeren 18 yerleştirmeyi çıkarmış ama iki yasak kareyi birlikte içerenleri geri eklememiş: 96 − 3 · 18 = 42.','dikkat'),(v_ihm,'Yasak kareleri hiç hesaba katmamış: C(4, 3) · 3! · 4 = 96.','bilgi'),(v_sat,'Aynı sütunda iki taş bulunamaması koşulunu unutup yalnız satır koşulunu ve yasak kareleri uygulamış: 135.','dikkat'),(v_kar,'Satır ve sütun koşulunu atlayıp 13 kullanılabilir kareden 3’ünü seçmiş: C(13, 3) = 286.','bilgi')]
o=[]
for r in range(1,5):
    for c in range(1,5):
        x,y=(c-1)*0.9,-(r-1)*0.9
        if (r,c) in yas: o.append(f'\\draw[thick,fill=gray!55] ({x},{y}) rectangle ({x+0.9},{y-0.9}); \\node[font=\\Large\\bfseries,red!70!black] at ({x+0.45},{y-0.45}) {{$\\times$}};')
        else: o.append(f'\\draw[thick,fill=blue!6] ({x},{y}) rectangle ({x+0.9},{y-0.9});')
SK=fig('\n'.join(o))
q('0010',tipId='pk-yerlesim',tip='Yasak karelerle yerleştirme',z='orta',alt='Koşullu Yerleştirme',kaz='Yasak kareleri olan bir tahtaya aynı satır ve sütunda bulunmayacak biçimde nesne yerleştirme sayısını bulur.',kalip='şekilli',
 kart='K-APER2-08 (yasak kareli tahta) · 4 × 4 tahta, 3 yasak kare, 3 taş',
 metin='Şekildeki 4 × 4’lük tahtada × işaretli kareler kullanılamamaktadır. Birbirinin aynı 3 taş, tahtanın kullanılabilir karelerine, hiçbir iki taş aynı satırda ya da aynı sütunda bulunmayacak biçimde yerleştirilecektir.\nBuna göre bu yerleştirme kaç farklı biçimde yapılabilir?',
 dogru=v,yan=sec(v,e,'B'),istenen='Koşullara uygun yerleştirmelerin sayısı.',ip=['Taşlar hangi satırlara yerleşecek ve her satırda kaç kullanılabilir kare var?'],bilgi=[YER],sekil=SK,
 ad=[A('Satırları seç','3 taş farklı satırlarda olacağından dört satırdan biri boş kalır.','4 satır üçlüsü'),A('Her üçlüyü say','Üstteki satırdan başlayıp her satırda kullanılmamış sütunlardan yasak olmayanlar seçilir.',f'{per[0]} + {per[1]} + {per[2]} + {per[3]}'),A('Topla','Satır üçlüleri birbirinin yerine geçer.',f'{per[0]} + {per[1]} + {per[2]} + {per[3]} = 53')],
 puf='Yasak kareli tahtalarda satırları tek tek doldurup her adımda boş sütunları takip et.')

# ================= 11 orta · alt küme sayıları =================
sol=[n for n in range(5,80) if comb(n,3)-comb(n,2)==14]; assert sol==[7]; v=comb(7,5); assert v==21
e=[(7,'Elemanlı sayıyı değil n’yi (kümenin eleman sayısını) cevap sanmış: 7.','dikkat'),(comb(7,4),'5 elemanlı yerine 4 elemanlı alt küme sayısını hesaplamış: C(7, 4) = 35.','dikkat'),(perm(7,2),'C(7, 5) yerine sıralı seçim yapıp P(7, 2) hesaplamış: 42.','bilgi'),(perm(7,5),'Alt küme sayısı yerine permütasyon almış: P(7, 5) = 2520.','bilgi')]
assert [x[0] for x in e]==[7,35,42,2520]
q('0011',tipId='pk-denklem',tip='Kombinasyon denklemi ve alt küme sayısı',z='orta',alt='Alt Küme Sayısı',kaz='Alt küme sayılarından kurulan denklemden eleman sayısını bulup başka bir alt küme sayısını hesaplar.',kalip='yeni nesil',
 kart='K-APER2-05 (alt küme sayısı denklemi) · 3 elemanlı alt küme sayısı − 2 elemanlı alt küme sayısı = 14',
 metin='n ≥ 5 olmak üzere, n elemanlı bir A kümesinin 3 elemanlı alt kümelerinin sayısı, 2 elemanlı alt kümelerinin sayısından 14 fazladır.\nBuna göre A kümesinin 5 elemanlı alt kümelerinin sayısı kaçtır?',
 dogru=v,yan=sec(v,e,'B'),istenen='A kümesinin 5 elemanlı alt kümelerinin sayısı.',ip=['Verilen koşulu C(n, 3) − C(n, 2) = 14 biçiminde yazıp n için denklem kur.'],bilgi=[DEN,KOM],
 ad=[A('Denklemi kur','Alt küme sayıları kombinasyonla yazılır.','C(n, 3) − C(n, 2) = 14'),A('Sadeleştir','Ortak çarpan n (n − 1)/6 ile ayrılır.','n (n − 1)(n − 5)/6 = 14 ve n (n − 1)(n − 5) = 84'),A('n değerini bul','84 = 7 · 6 · 2 olduğundan n = 7; başka n ≥ 5 çözümü yoktur.','n = 7'),A('İstenen sayıyı bul','5 elemanlı alt küme sayısı hesaplanır.','C(7, 5) = C(7, 2) = 21')],
 puf='Önce verilen koşuldan n’yi bul, sonra istenen kombinasyonu hesapla.')

# ================= 12 orta · doğruların kesişim noktaları =================
def kes(a,b):
    (p,d),(q_,e_)=a,b; det=d[0]*e_[1]-d[1]*e_[0]
    if det==0: return None
    t=Fr((q_[0]-p[0])*e_[1]-(q_[1]-p[1])*e_[0],det); return (p[0]+t*d[0],p[1]+t*d[1])
L=[((0,1),(1,0)),((0,3),(1,0)),((1,0),(0,1)),((4,0),(0,1)),((0,0),(1,1)),((5,0),(-1,1))]
nok=set(kes(a,b) for a,b in combinations(L,2) if kes(a,b) is not None); v=len(nok); par=sum(1 for a,b in combinations(L,2) if kes(a,b) is None)
assert v==9 and par==2 and 15-par==13
ucl=[(i,[j for j,l in enumerate(L) if kes(L[i],l)==p]) for i,p in []]
conc=sum(1 for p in nok if sum(1 for l in L if any(kes(l,m)==p for m in L if m is not l))>=3 and len([l for l in L if any(kes(l,m)==p for m in L if m is not l)])==3)
assert conc==2
e=[(15,'Her doğru çiftini bir kesişim noktası sanıp C(6, 2) = 15 hesaplamış.','bilgi'),(13,'Paralel doğru çiftlerini çıkarıp (15 − 2 = 13) birden çok doğrunun geçtiği noktaları ayrıca saymamış.','dikkat'),(11,'Üç doğrunun geçtiği noktalardan yalnız birini ortak nokta saymış: 13 − 2 = 11.','dikkat'),(7,'Üç doğrunun geçtiği her noktada 3 çiftin üçünü de çıkarmış: 13 − 2 · 3 = 7.','dikkat'),]
assert [x[0] for x in e]==[15,13,11,7]
col={0:'blue!70!black',1:'blue!70!black',2:'orange!85!black',3:'orange!85!black',4:'green!50!black',5:'red!70!black'}
o=[]
def klip(l):
    (p,d)=l; ts=[]
    for ax,lo,hi in ((0,-0.3,5.8),(1,-0.3,5.3)):
        if d[ax]!=0: ts+=[(lo-p[ax])/d[ax],(hi-p[ax])/d[ax]]
    # kutuya kırp
    t0,t1=-1e9,1e9
    for ax,lo,hi in ((0,-0.3,5.8),(1,-0.3,5.3)):
        if d[ax]==0:
            if not(lo<=p[ax]<=hi): return None
        else:
            a,b=sorted(((lo-p[ax])/d[ax],(hi-p[ax])/d[ax])); t0=max(t0,a); t1=min(t1,b)
    return (p[0]+t0*d[0],p[1]+t0*d[1]),(p[0]+t1*d[0],p[1]+t1*d[1])
for i,l in enumerate(L):
    a,b=klip(l); o.append(f'\\draw[{col[i]},line width=1.5pt] ({a[0]:.2f},{a[1]:.2f}) -- ({b[0]:.2f},{b[1]:.2f}); \\node[font=\\small\\bfseries,text={col[i]},fill=white,inner sep=1pt] at ({b[0]+(0.0 if False else 0.0):.2f},{b[1]:.2f}) {{$d_{i+1}$}};')
o.append('\\draw[thin] (-0.3,-0.3) rectangle (5.8,5.3);')
SK=fig('\n'.join(o))
q('0012',tipId='pk-sekil',tip='Doğru ve ızgara üzerinde sayma',z='orta',alt='Doğruların Kesişimi',kaz='Şekildeki doğruların paralellik ve ortak noktalarını okuyarak farklı kesişim noktalarının sayısını bulur.',kalip='şekilli',
 kart='K-APER2-06 (kesişim noktaları) · 6 doğru, 2 paralel çift, 2 üçlü ortak nokta',
 metin='Şekilde d₁, d₂, d₃, d₄, d₅ ve d₆ doğruları verilmiştir. d₁ // d₂ ve d₃ // d₄ olup diğer doğru çiftleri paralel değildir.\nBuna göre bu doğrular toplam kaç farklı noktada kesişir?',
 dogru=v,yan=sec(v,e,'B'),istenen='Doğruların toplam farklı kesişim noktası sayısı.',ip=['Hangi noktalardan üç doğru birden geçiyor ve bu noktalar kaç doğru çiftine karşılık geliyor?'],bilgi=[KES],sekil=SK,
 ad=[A('Çiftleri say','Altı doğrudan sıra gözetmeden iki doğru seçilir.','C(6, 2) = 15'),A('Paralelleri çıkar','Paralel iki doğru çifti kesişmez.','15 − 2 = 13 kesişen çift'),A('Ortak noktaları düzelt','Üç doğrunun geçtiği her nokta 3 çifte karşılık gelir ama 1 nokta sayılır; iki nokta için 2 · (3 − 1) = 4 çıkarılır.','13 − 4 = 9')],
 puf='Doğru çiftlerini sayarken paralellik ve ortak noktalar sayıyı değiştirir.')

# ================= 13 orta · öncüllü, tekrarlı rakamlarla sayı yazma =================
dz=set(permutations([1,1,2,2,3])); t=len(dz); ce=sum(1 for p in dz if p[-1]==2); b1=sum(1 for p in dz if p[0]==1)
assert (t,ce,b1)==(30,12,12) and t//2==15 and F(5)==120
q('0013',tipId='pk-sifre',tip='Şifre ve kutu doldurma',z='orta',alt='Tekrarlı Permütasyon',kaz='Tekrarlı rakamlarla yazılan sayıları toplam, çift olma ve baştaki rakam koşullarıyla sayar.',kalip='öncüllü',
 kart='K-APER2-02 (tekrarlı rakamlı sayı) · 1, 1, 2, 2, 3 rakamlarının hepsi kullanılarak 5 basamaklı sayı',
 metin='1, 1, 2, 2 ve 3 rakamlarının hepsi kullanılarak 5 basamaklı doğal sayılar yazılıyor.\nBu sayılarla ilgili,\nI. Toplam 30 tanedir.\nII. Çift olanlar 12 tanedir.\nIII. 1 ile başlayanlar 15 tanedir.\nifadelerinden hangileri doğrudur?',
 dogru='I ve II',yan=[('Yalnız I','Çift olanları toplamın yarısı sanıp 15 bulduğundan II’yi yanlış saymış; I ve III için doğru sonuca ulaşmış.','dikkat'),('Yalnız II','Tekrarı bölmeyi unutup toplamı 5! = 120 bulduğundan I’i yanlış saymış; II’yi doğru, III’ü yanlış değerlendirmiş.','islem'),('I ve III','1 ile başlayanları 30/2 = 15 sanıp III’ü doğru saymış; çift olanları da 15 sanıp II’yi yanlış saymış.','dikkat'),('I, II ve III','1 ile başlayanlar için de “yarısı” akıl yürütmesiyle 15 bulup III’ü doğru saymış.','dikkat')],
 sira=SIR,istenen='Doğru olan ifadelerin hangileri olduğu.',ip=['Çift olma ve baştaki rakam koşullarında bir rakamı yerine koyduktan sonra kalan rakamları say.'],bilgi=[TKR],
 ad=[A('I. ifadeyi say','Tekrarlı permütasyon: 1 iki kez, 2 iki kez, 3 bir kez.','5!/(2! · 2!) = 30 · doğru'),A('II. ifadeyi say','Çift olması için birler basamağı 2’dir; kalan 1, 1, 2, 3 dizilir.','4!/2! = 12 · doğru'),A('III. ifadeyi say','Baştaki rakam 1 ise kalan 1, 2, 2, 3 dizilir.','4!/2! = 12 ≠ 15'),A('Sonuç','I ve II doğru, III yanlıştır.','I ve II')],
 puf='Öncüllü yargılarda baştaki ya da sondaki rakamı yerine koyup kalan rakamları say.')

# ================= 14 zor · 3×3 tabloda kısmi sıralama =================
def syt(pre):
    c=0
    for p in permutations(range(1,10)):
        g=[p[0:3],p[3:6],p[6:9]]
        if all(g[i][j]<g[i][j+1] for i in range(3) for j in range(2)) and all(g[i][j]<g[i+1][j] for i in range(2) for j in range(3)) and all(g[i][j]==vv for (i,j),vv in pre.items()): c+=1
    return c
v=syt({(1,1):5}); assert v==18 and syt({})==42
e=[(3*2,'Küçük sayıları 3 yolla, büyük sayıları yalnız 2 yolla yerleştirmiş ve simetrik durumu da saymamış: 3 · 2 = 6.','dikkat'),(3*3,'Dördüncü küçük sayının iki olası karesinden yalnız birini düşünmüş: 3 · 3 = 9.','dikkat'),(3*2*2,'Büyük sayıları yerleştirmenin 3 yerine 2 yolu olduğunu sanıp iki durumu da saymış: 3 · 2 · 2 = 12.','dikkat'),(2*18,'Simetrik durumu iki kez sayarak sonucu ikiye katlamış: 2 · 18 = 36.','bilgi'),(42,'Ortadaki 5’i yok sayıp bütün yerleştirmeleri saymış: 42.','bilgi')]
assert [x[0] for x in e]==[6,9,12,36,42]
o=[]
for i in range(3):
    for j in range(3):
        x,y=j*1.0,-i*1.0
        if (i,j)==(1,1): o.append(f'\\draw[thick,fill=orange!45] ({x},{y}) rectangle ({x+1},{y-1}); \\node[font=\\Large\\bfseries] at ({x+0.5},{y-0.5}) {{5}};')
        else: o.append(f'\\draw[thick,fill=blue!6] ({x},{y}) rectangle ({x+1},{y-1});')
SK=fig('\n'.join(o))
q('0014',tipId='pk-kismi',tip='Kısmi sıralama ve öncelik şeması',z='orta',alt='Tabloya Yerleştirme',kaz='Satır ve sütunlarda artan olacak biçimde 3 × 3 tabloya sayı yerleştirmeyi, bir hücresi verilmiş durumda sayar.',kalip='şekilli',
 kart='K-APER2-04 (artan satır-sütun tablosu) · 1, …, 9 sayıları, ortadaki hücre 5',
 metin='Şekildeki 3 × 3’lük tablonun karelerine 1’den 9’a kadar doğal sayıların her biri birer kez yazılacaktır. Şekilde ortadaki kareye 5 yazılmıştır. Tablonun her satırında sayılar soldan sağa, her sütununda ise yukarıdan aşağıya doğru artacak biçimde yazılacaktır.\nBuna göre bu yazma işlemi kaç farklı biçimde yapılabilir?',
 dogru=v,yan=sec(v,e,'D'),istenen='Koşulları sağlayan yazılışların sayısı.',ip=['5’ten küçük ve büyük sayılar tabloda hangi bölgelere yazılabilir?'],bilgi=[KIS],sekil=SK,
 ad=[A('Köşeleri belirle','En küçük sayı sol üst, en büyük sayı sağ alt karededir; 5’ten küçük sayılar 5’in solunda ve üstünde kalan karelerdedir.','Sol üst: 1 · Sağ alt: 9'),A('Küçük sayıların yerini bul','1, 2, 3, 4 sayıları 5’in sol üstünde kalan üç kareye (sol üst, üst orta, orta sol) ve bir kareye daha yazılır; dördüncü kare ya sağ üst ya da sol alt karedir.','2 durum (simetrik)'),A('Her durumu say','Sağ üst durumunda 1, 2, 3, 4 için 3 yazılış; geri kalan 6, 7, 8 üç karede 3 yazılış vardır.','3 · 3 = 9'),A('Durumları topla','Diğer durum simetriktir.','9 + 9 = 18')],
 puf='Artan satır–sütun tablolarında önce köşelere ve ortadaki verilmiş sayıya göre bölgeleri ayır.')

# ================= 15 zor · otopark şeritleri (üç çıkış saati) =================
araclar=[('A',13),('B',13),('C',15),('D',15),('E',18),('F',18)]
def uygun(p):
    for s_ in (0,3):
        t=[araclar[p[s_+k]][1] for k in range(3)]
        if not(t[0]<=t[1]<=t[2]): return False
    return True
v=sum(1 for p in permutations(range(6)) if uygun(p)); assert v==56==7*8
e=[(8,'Tek bir dağılım (7 dağılımdan biri) bulup araçları kendi grupları içinde sıralamış: 2! · 2! · 2! = 8.','dikkat'),(3*8,'7 dağılımdan yalnız 3 tanesini bulmuş: 3 · 8 = 24.','dikkat'),(5*8,'Dağılımlardan 5 tanesini bulmuş: 5 · 8 = 40.','dikkat'),(6*8,'Şeritlerden birinin tek saatli araçlardan oluştuğu dağılımlardan birini atlamış: 6 · 8 = 48.','dikkat'),(720,'Çıkış saati koşulunu atlayıp 6! hesaplamış: 720.','bilgi')]
assert [x[0] for x in e]==[8,24,40,48,720]
o=[]
for ln in range(2):
    for k in range(3):
        o.append(f'\\draw[thick,fill=blue!6] ({ln*1.2},{k*0.9}) rectangle ({ln*1.2+1.0},{k*0.9+0.8});')
o.append('\\draw[-{Stealth},line width=1.6pt,red!70!black] (0.5,-0.15) -- (0.5,-0.85); \\draw[-{Stealth},line width=1.6pt,red!70!black] (1.7,-0.15) -- (1.7,-0.85); \\node[font=\\small\\bfseries,red!70!black] at (1.1,-1.15) {çıkış yönü};')
for i,(nm,sa) in enumerate(araclar):
    fl={13:'blue!25',15:'green!25',18:'orange!40'}[sa]; x=3.0+(i//3)*2.3; y=1.8-(i%3)*0.9
    o.append(f'\\draw[thick,fill={fl},rounded corners=2pt] ({x},{y}) rectangle ({x+2.0},{y+0.7}); \\node[font=\\small\\bfseries] at ({x+1.0},{y+0.35}) {{{nm}: {sa}.00}};')
o.append('\\node[font=\\small\\bfseries] at (4.15,2.85) {araçlar ve çıkış saatleri};')
SK=fig('\n'.join(o))
q('0015',tipId='pk-yerlesim',tip='Yasak karelerle yerleştirme',z='zor',alt='Koşullu Yerleştirme',kaz='Üç farklı çıkış saatli araçları şeritlere, çıkış sırasını bozmayacak biçimde yerleştirmenin yollarını sayar.',kalip='şekilli',
 kart='K-APER2-08 (otopark şeritleri) · 2 şerit × 3 yer, 6 araç, üç çıkış saati',
 metin='Şekildeki otoparkın iki şeridinde 3’er park yeri vardır. A, B, C, D, E ve F araçlarının çıkış saatleri şekilde verilmiştir. Altı araç, her yere bir araç gelecek biçimde park edilecektir. Araçlar şeritlerin alt ucundan çıkmaktadır; bir şeritte, daha geç çıkacak bir araç, daha erken çıkacak bir aracın çıkışa yakın tarafında park edemez. Aynı saatte çıkacak araçlar arasında sınırlama yoktur.\nBuna göre bu altı araç kaç farklı biçimde park edilebilir?',
 dogru=v,yan=sec(v,e,'E'),istenen='Koşulları sağlayan park düzenlerinin sayısı.',ip=['Bir şeritteki araçların çıkış saatleri çıkıştan uzaklaştıkça nasıl değişmelidir?'],bilgi=[PER],sekil=SK,
 ad=[A('Şeritlerin saat düzenini belirle','Her şeritte çıkışa yakın yerden uzağa saatler azalmaz; bir şeridin düzeni, o şeritteki araçların saat gruplarına göre tek türlü belirlenir.','Şerit düzeni saat gruplarının sayılarıyla belirlenir'),A('Dağılımları say','1. şeritteki 13.00, 15.00 ve 18.00’lik araç sayıları (a, b, c) toplamı 3 olan ve her biri en çok 2 olan üçlüdür.','(2,1,0) (2,0,1) (1,2,0) (0,2,1) (1,0,2) (0,1,2) (1,1,1): 7 dağılım'),A('Araçları yerleştir','Her dağılımda aynı saatli iki araç, kendilerine ayrılan iki yer arasında yer değiştirebilir.','2! · 2! · 2! = 8'),A('Çarp','Dağılımlar birbirinin yerine geçer.','7 · 8 = 56')],
 puf='Sıralama koşulları altında önce hangi türlerin hangi yerlere gelebileceğini belirle.')

# ================= 16 zor · kadranda komşu olmayan sayılar =================
def kom(a,b): return (a-b)%12 in (1,11)
v=sum(1 for c in combinations(range(12),4) if not any(kom(a,b) for a,b in combinations(c,2))); assert v==105==12*comb(8,4)//8
dz=comb(9,4)  # doğru üzerinde ardışık olmayan
e=[(comb(8,4),'12 − 4 = 8 boşluktan 4 tane seçip çembersel yapıyı hiç düşünmemiş: C(8, 4) = 70.','dikkat'),(dz-comb(8,2),'12 ve 1’in birlikte seçildiği durumları çıkarırken kalan iki sayının ardışık olmaması koşulunu unutup 3, …, 10 arasından C(8, 2) = 28 çıkarmış: 126 − 28 = 98.','dikkat'),(dz,'Sayıları doğru üzerinde dizilmiş sanıp 12 ile 1’in komşu olduğunu unutmuş: C(9, 4) = 126.','dikkat'),(comb(12,4),'Komşuluk koşulunu hiç uygulamamış: C(12, 4) = 495.','bilgi')]
assert dz-comb(8,2)==98 and [x[0] for x in e]==[70,98,126,495]
import math as _m
o=['\\draw[thick,fill=yellow!14] (0,0) circle (1.75);']
for k in range(12):
    a=_m.pi/2-2*_m.pi*k/12; n=12 if k==0 else k
    o.append(f'\\draw[thick] ({1.6*_m.cos(a):.3f},{1.6*_m.sin(a):.3f}) -- ({1.75*_m.cos(a):.3f},{1.75*_m.sin(a):.3f}); \\node[font=\\normalsize\\bfseries] at ({1.3*_m.cos(a):.3f},{1.3*_m.sin(a):.3f}) {{{n}}};')
o.append('\\fill (0,0) circle (0.06);')
SK=fig('\n'.join(o))
q('0016',tipId='pk-kume',tip='Koşullu alt küme ve seçim',z='zor',alt='Çembersel Seçim',kaz='Saat kadranındaki sayılardan komşu olmayanları seçmenin yollarını çembersel komşuluğu da dikkate alarak sayar.',kalip='şekilli',
 kart='K-APER2-09 (kadranda komşu olmayan seçim) · 12 sayıdan 4’ü, 12 ile 1 komşu',
 metin='Bir analog saatin kadranındaki 1’den 12’ye kadar olan sayılardan 4 tanesi, hiçbir ikisi kadranda yan yana bulunmayacak biçimde işaretlenecektir; kadranda 12 ile 1 de yan yana kabul edilmektedir.\nBuna göre bu işaretleme kaç farklı biçimde yapılabilir?',
 dogru=v,yan=sec(v,e,'C'),istenen='Koşulu sağlayan işaretlemelerin sayısı.',ip=['1 ve 12’nin ikisinin de işaretlendiği durumlar için komşuluk koşulu nasıl değişir?'],bilgi=[KUM,TUM],sekil=SK,
 ad=[A('Doğru üzerindeki durumu say','Sayılar 1’den 12’ye bir doğru üzerinde olsaydı, yan yana olmayan 4 sayı seçimi 12 − 4 + 1 = 9 yerden yapılırdı.','C(9, 4) = 126'),A('12 ile 1’in durumu','12 ve 1 işaretliyse 2 ve 11 işaretlenemez; kalan 2 sayı 3, …, 10 arasından ardışık olmayacak biçimde seçilir.','C(7, 2) = 21'),A('Çıkar','Çembersel koşula uymayan seçimler çıkarılır.','126 − 21 = 105')],
 puf='Çembersel yerleşimlerde uçların da komşu olduğunu unutma.')

# ================= 17 zor · eşleştirme =================
def esle(l):
    if not l: yield []; return
    a=l[0]
    for i in range(1,len(l)):
        for r in esle(l[1:i]+l[i+1:]): yield [(a,l[i])]+r
tum=list(esle(list(range(8)))); assert len(tum)==105
v=sum(1 for m in tum if (0,1) not in m and (2,3) not in m); assert v==78==105-15-15+3
e=[(105,'Ali–Berk ve Ceren–Duru koşullarını uygulamadan bütün eşleşmeleri saymış: 8!/(2⁴ · 4!) = 105.','bilgi'),(90,'Yalnız bir koşulu (Ali ile Berk) uygulamış: 105 − 15 = 90.','dikkat'),(75,'İki koşulu çıkarırken ikisinin birden gerçekleştiği 3 eşleşmeyi geri eklememiş: 105 − 15 − 15 = 75.','dikkat'),(1872,'Çiftleri adlandırılmış (sıralı) sanıp 4! ile çarpmış: 78 · 24 = 1872.','bilgi')]
assert 78*24==1872
q('0017',tipId='pk-eslestirme',tip='Eşleştirme ve koşullu gruplama',z='zor',alt='Eşleştirme',kaz='Adlandırılmamış çiftlere ayırmada istenmeyen eşleşmeleri içerme-dışarma ile çıkarır.',kalip='hikâyeli',
 kart='K-APER2-10 (koşullu eşleştirme) · 8 oyuncu, 4 çift, iki yasak çift',
 metin='Bir satranç kulübünde Ali, Berk, Ceren, Duru ve diğer dört oyuncu olmak üzere 8 oyuncu, birbirinden bağımsız oynayacak 4 maçı oynamak üzere ikişerli gruplara ayrılacaktır. Maçlar numaralandırılmamıştır; yani maçların sırası önemli değildir. Ali ile Berk karşılaşmayacak, Ceren ile Duru da karşılaşmayacaktır.\nBuna göre bu ayırma kaç farklı biçimde yapılabilir?',
 dogru=v,yan=sec(v,e,'B'),istenen='Koşullara uygun eşleşmelerin sayısı.',ip=['Koşulu sağlamayan eşleşmeler hangi durumlardan oluşur?'],bilgi=[ESL,TUM],
 ad=[A('Tüm eşleşmeleri say','8 oyuncu, sırası önemsiz 4 çifte ayrılır.','8!/(2⁴ · 4!) = 105'),A('Yasak durumları say','Ali–Berk çiftli eşleşmeler: kalan 6 oyuncu 3 çifte; Ceren–Duru için aynı sayı; ikisi birden için kalan 4 oyuncu 2 çifte.','15 ve 15 ve 3'),A('Dışarma uygula','Ortak durum iki kez çıkarıldığından bir kez geri eklenir.','105 − 15 − 15 + 3 = 78')],
 puf='Birden çok yasak koşulda ortak durumları ayrıca düşün.')

# ================= 18 zor · tablo, sınırlı dağıtım =================
lo=[2,1,3,0]; hi=[4,3,5,2]
dg=lambda N,l,h:sum(1 for t in product(*[range(a,b+1) for a,b in zip(l,h)]) if sum(t)==N)
v=dg(10,lo,hi); assert v==19==comb(7,3)-4*comb(4,3)
k_alt=dg(10,[0]*4,hi); k_ust=dg(10,lo,[10]*4); k_hic=dg(10,[0]*4,[10]*4); k_bir=dg(10,[1]*4,hi)
assert (k_alt,k_ust,k_hic)==(30,35,286); print('tablo dag',k_bir)
e=[(comb(9,3),'Tablodaki alt sınırlar yerine her öğrenciye en az 1 kalem verip kalan 6 kalemi serbestçe dağıtmış: C(9, 3) = 84.','dikkat'),(k_alt,'En az koşullarını (alt sınırları) hesaba katmayıp yalnız üst sınırları uygulamış: 30.','dikkat'),(k_ust,'Alt sınırları dağıtıp kalan 10 − 6 = 4 kalemi üst sınırı unutarak 4 öğrenciye serbestçe dağıtmış: C(7, 3) = 35.','dikkat'),(k_hic,'Hiçbir sınırı uygulamamış: C(13, 3) = 286.','bilgi')]
assert comb(7,3)==35 and comb(13,3)==286
SK=tablo_svg(['Öğrenci','En az','En çok'],[['Ada','2','4'],['Bora','1','3'],['Ceyda','3','5'],['Deniz','0','2']])
q('0018',tipId='pk-dagitim',tip='Özdeş nesneleri kapasiteli dağıtma',z='zor',alt='Sınırlı Dağıtım',kaz='Her öğrenci için alt ve üst sınırı tablodan okunan özdeş nesnelerin dağıtım sayısını bulur.',kalip='tablo',
 kart='K-APER2-07 (sınırlı dağıtım) · 10 özdeş nesne, 4 öğrenci, alt ve üst sınırlar',
 metin='Bir öğretmen, birbirinin aynı 10 kalemin tamamını Ada, Bora, Ceyda ve Deniz’e dağıtacaktır. Her öğrencinin alacağı kalem sayısı aşağıdaki tabloda verilen “en az” ve “en çok” değerleri arasında (bu değerler dahil) olacaktır.\nBuna göre bu dağıtım kaç farklı biçimde yapılabilir?',
 dogru=v,yan=sec(v,e,'A'),istenen='Koşullara uygun dağıtımların sayısı.',ip=['Her öğrenci için alabileceği kalem sayısı hangi aralıktadır?'],bilgi=[DAG],sekil=SK,
 ad=[A('Alt sınırları dağıt','Her öğrenciye en az olması gereken kalemler verilir.','2 + 1 + 3 + 0 = 6 kalem; geriye 4 kalem'),A('Yeni üst sınırları bul','Her öğrencinin alabileceği ek kalem sayısı üst sınır − alt sınırdır.','Ek en çok: 2, 2, 2, 2'),A('Serbest dağıtımı say','Ek kalemler 4 öğrenciye serbestçe dağıtılır.','x₁ + x₂ + x₃ + x₄ = 4: C(7, 3) = 35'),A('Sınırı aşanları çıkar','Bir öğrencinin 3 ya da daha fazla ek kalem aldığı dağıtımlar çıkarılır (iki öğrenci birden sınırı aşamaz).','4 · C(4, 3) = 16 ve 35 − 16 = 19')],
 puf='Sınırlı dağıtımlarda hem alt hem üst sınırlar sayıyı etkiler.')

# ================= 19 zor · öncüllü, şifre kuralı =================
H6='ABCDEF'
sif=[p for p in permutations(H6,4) if ('A' not in p) or ('B' in p and p.index('A')<p.index('B'))]
v=len(sif); a_li=sum(1 for p in sif if 'A' in p); a_siz=sum(1 for p in sif if 'A' not in p); b_li=sum(1 for p in sif if 'B' in p)
assert (v,a_li,a_siz,b_li)==(192,72,120,168)
assert perm(4,4)==24 and 4*comb(4,2)*6==144 and 96+72==168 and 4*24==96
q('0019',tipId='pk-sifre',tip='Şifre ve kutu doldurma',z='zor',alt='Koşullu Şifre',kaz='Bir harfin bulunması ve sırası koşuluna bağlı şifrelerin sayısını durumlara ayırarak sayar ve öncülleri değerlendirir.',kalip='öncüllü',
 kart='K-APER2-02 (koşullu şifre) · A, B, C, D, E, F harflerinden 4 harfli, A için kural',
 metin='A, B, C, D, E ve F harflerinden birbirinden farklı 4 tanesi kullanılarak soldan sağa 4 harfli şifreler oluşturuluyor. Bir şifrede A harfi bulunuyorsa B harfi de bulunmalı ve A harfi B harfinin solunda yer almalıdır.\nBu koşulu sağlayan şifrelerle ilgili,\nI. A harfini içerenler 72 tanedir.\nII. A harfini içermeyenler 120 tanedir.\nIII. B harfini içerenler 168 tanedir.\nifadelerinden hangileri doğrudur?',
 dogru='I, II ve III',yan=[('Yalnız I','A içermeyen şifrelerde B’yi de dışarıda bırakıp P(4, 4) = 24 bulduğundan II’yi, B içerenleri 72 sanıp (yalnız A’lıları sayıp) III’ü yanlış saymış.','dikkat'),('Yalnız II','A ve B birlikte olan şifrelerde A ile B’nin sırasını önemsemeyip 144 bulduğundan I’i, III’ü de yanlış değerlendirmiş.','dikkat'),('I ve II','B içerenleri yalnız A’sız şifreler olarak (96) sayıp A’lı şifreleri eklemeyi unuttuğundan III’ü yanlış saymış.','dikkat'),('I ve III','A içermeyenleri yalnız B içerenler olarak (96) sayıp II’yi yanlış, III’ü 96 + 72 = 168 ile doğru saymış.','dikkat')],
 sira=SIR,istenen='Doğru olan ifadelerin hangileri olduğu.',ip=['A harfi bulunan şifrelerde A ve B için kaç sıra seçeneği var?'],bilgi=[SIF,PER],
 ad=[A('I. ifadeyi say','A varsa B de vardır ve A solda olur; A, B için 4 konumdan 2’si seçilir (sıra belli), kalan 2 konuma 4 harften sıralı 2 harf yazılır.','C(4, 2) · P(4, 2) = 6 · 12 = 72 · doğru'),A('II. ifadeyi say','A içermeyen şifreler B, C, D, E, F harflerinden oluşur; koşul zaten sağlanır.','P(5, 4) = 120 · doğru'),A('III. ifadeyi say','B içerenler: A’lı şifreler (hepsinde B var) ve A’sız B’li şifreler.','72 + (C(4, 3) · 4! = 96) = 168 · doğru'),A('Sonuç','Üç ifade de doğrudur.','I, II ve III')],
 puf='Koşullu şifrelerde kuralı tetikleyen harfin bulunduğu ve bulunmadığı durumları ayrı say.')

# ================= 20 zor · yasak karelerle dikdörtgen sayma =================
rem=[(2,4),(4,2)]
def dk(r,W=5,Hh=5):
    n=0
    for x1,x2 in combinations(range(W+1),2):
        for y1,y2 in combinations(range(Hh+1),2):
            if not any(x1<cx<=x2 and y1<cy<=y2 for cx,cy in r): n+=1
    return n
v=dk(rem); one=dk(rem[:1]); assert v==113 and one==161 and dk([])==225
c1=225-one; c2=225-dk(rem[1:]); cb=c1+c2-(225-v); assert (c1,c2,cb)==(64,64,16)
e=[(cb,'Yalnız iki işaretli kareyi birlikte içeren dikdörtgenleri saymış: 16.','dikkat'),(c1,'İşaretli karelerden birini (ikisini birlikte içerenler dahil) içeren dikdörtgenleri saymış: 64.','dikkat'),(225-c1-c2,'İşaretli kareleri içeren dikdörtgenleri çıkarırken ikisini birlikte içerenleri geri eklememiş: 225 − 64 − 64 = 97.','dikkat'),(c1+c2,'İşaretli kareyi içeren dikdörtgenleri ortak durumu iki kez sayarak toplamış: 64 + 64 = 128.','bilgi'),(one,'Yalnız bir işaretli kareyi dikkate alıp içermeyenleri saymış: 161.','dikkat')]
assert [x[0] for x in e]==[16,64,97,128,161]
o=[]
for r in range(5):
    for c in range(5):
        cx,cy=c+1,5-r
        fl='gray!60' if (cx,cy) in rem else 'blue!6'
        o.append(f'\\draw[thick,fill={fl}] ({c*0.85},{-r*0.85}) rectangle ({c*0.85+0.85},{-r*0.85-0.85});')
        if (cx,cy) in rem: o.append(f'\\node[font=\\Large\\bfseries,red!70!black] at ({c*0.85+0.425},{-r*0.85-0.425}) {{$\\times$}};')
SK=fig('\n'.join(o))
q('0020',tipId='pk-sekil',tip='Doğru ve ızgara üzerinde sayma',z='zor',alt='Izgarada Dikdörtgen Sayma',kaz='Yasak (boyalı) kareleri içermeyen dikdörtgenlerin sayısını içerme-dışarma ile bulur.',kalip='şekilli',
 kart='K-APER2-06 (yasak kareli ızgara) · 5 × 5 ızgara, iki × işaretli kare',
 metin='Şekildeki 5 × 5’lik ızgara birim karelerden oluşmaktadır ve × işaretli iki kare kullanılamamaktadır. Kenarları ızgara çizgileri üzerinde olan dikdörtgenler çiziliyor ve çizilen dikdörtgenlerin içinde × işaretli kare bulunmayacaktır.\nBuna göre bu koşula uygun kaç farklı dikdörtgen çizilebilir?',
 dogru=v,yan=sec(v,e,'D'),istenen='İşaretli kareleri içermeyen dikdörtgenlerin sayısı.',ip=['Koşulu sağlamayan dikdörtgenler hangi durumlardan oluşur?'],bilgi=[GEO,TUM],sekil=SK,
 ad=[A('Tüm dikdörtgenleri say','6 yatay ve 6 düşey çizgiden ikişer çizgi seçilir.','C(6, 2) · C(6, 2) = 225'),A('Her işaretli kareyi içerenleri say','Üst işaretli kareyi içerenlerde kenar seçenekleri 2 · 4 · 4 · 2, alttakini içerenlerde 4 · 2 · 2 · 4’tür.','64 ve 64'),A('İkisini birden içerenleri say','İkisini de içeren dikdörtgenin sol-sağ seçenekleri 2 · 2, alt-üst seçenekleri 2 · 2’dir.','2 · 2 · 2 · 2 = 16'),A('Dışarma uygula','İşaretlilerden en az birini içerenler 64 + 64 − 16 = 112 tanedir.','225 − 112 = 113')],
 puf='Yasak bölgeli ızgaralarda sayarken ortak durumlara dikkat et.')

# ---------- bitir ----------
for q_ in P.ANA: q_['kardes']=None
P.yaz(os.path.join(ADIR,'apermiki-1.json'),'/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/pm/bos.json')
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=UK))['kartlar'].append(c['id'])
json.dump(dict(konu=P.konu_adi,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 AYT Matematik çıkmış soruları ve yayın soru bankaları (yalnız mantık), MEB 11. sınıf müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(os.path.abspath(os.path.join(ADIR,'..')),'kartlar','apermiki.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
