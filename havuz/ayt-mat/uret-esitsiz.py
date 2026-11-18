"""AYT Matematik · Eşitsizlikler (20 soru): ikinci derece, çarpım/bölüm, işaret tablosu, eşitsizlik sistemleri, parametre, grafik.
Her doğru ve çeldirici değer koddan hesaplanıp assert edilir. Kardeş yok, ipucu 1."""
import sys,os,json
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _esz import *
import _hafif_mat as H
from _hafif_mat import kart,mk,tablo_svg
from ortak import Parti,A,B
H.KONU='Eşitsizlikler'
UK='amat|Eşitsizlikler'
P=Parti('esitsiz','Eşitsizlikler',UK,ders='AYT Matematik',idon='aytmat')
KY='ÖSYM 2018–2025 AYT Matematik (eşitsizlik, eşitsizlik sistemleri, işaret tablosu; yalnız mantık) · MEB 10–12. sınıf'
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)
Fi=Fr

# ---------- bilgi kutuları (örnekler soruların sayılarından farklı) ----------
IKI=B('İkinci dereceden eşitsizlik','ax² + bx + c ifadesi köklerin dışında a ile aynı işaretli, kökler arasında a’nın tersi işaretlidir; çift kökte işaret değişmez. Örnek: x² − 7x + 10 = (x − 2)(x − 5) ifadesi x < 2 ve x > 5 için pozitif, 2 < x < 5 için negatiftir')
TAB=B('İşaret tablosu','Her çarpanın kökü bulunup sıralanır; her aralıkta çarpanların işaretleri çarpılır. Tek katlı kökte işaret değişir, çift katlı kökte değişmez. Bölümde paydayı sıfır yapan değer çözüme alınmaz. Örnek: (x + 1)(x − 6) ≥ 0 için kökler −1 ve 6’dır; çözüm (−∞, −1] ∪ [6, ∞) olur')
SIS=B('Eşitsizlik sistemi','Sistemin çözüm kümesi, eşitsizliklerin çözüm kümelerinin kesişimidir; sayı doğrusunda hepsinin birlikte taralı olduğu kısımdır. Örnek: x > 1 ve x ≤ 7 sisteminin çözümü (1, 7]’dir')
MUT=B('Mutlak değerli eşitsizlik','a > 0 için |u| < a ⇔ −a < u < a; |u| > a ⇔ u < −a veya u > a. Örnek: |x − 1| < 3 ⇔ −2 < x < 4')
DEL=B('Her x için eşitsizlik','ax² + bx + c > 0 eşitsizliği her gerçel x için sağlanıyorsa a > 0 ve Δ = b² − 4ac < 0 olmalıdır. Başkatsayı sıfır olabiliyorsa o durum ayrıca denenir. Örnek: x² + 6x + 10 için Δ = 36 − 40 < 0 olduğundan ifade hep pozitiftir')
GRF=B('Grafikte işaret','Fonksiyonun grafiği x ekseninin üstündeyken f(x) > 0, altındayken f(x) < 0, eksene değdiği ya da kestiği noktada f(x) = 0’dır. İki fonksiyonun çarpımının işareti, işaretlerin çarpımıdır. Örnek: f(x) > 0 ve g(x) < 0 ise f(x) · g(x) < 0’dır')
UYG=B('Eşitsizlikle model kurma','Uzunluk ve adet gibi nicelikler için pozitiflik (ya da tam sayı olma) koşulu da eşitsizliğe eklenir; çözüm aralığı bu koşullarla kesiştirilir. Örnek: bir kenar x − 5 ise x − 5 > 0 yani x > 5 olmalıdır')
KOK=B('Çözüm kümesinden eşitsizliği bulma','Çözüm kümesinin uç noktaları ilgili ifadenin köküdür. Köklere göre çarpan biçimi yazılır ve başkatsayının işaretine dikkat edilir. Örnek: çözüm kümesi (1, 6) ve eşitsizlik x² + bx + c < 0 ise (x − 1)(x − 6) < 0, yani x² − 7x + 6 < 0’dır')
ABC=B('Parabolde a, b, c','Kollar yukarıysa a > 0, aşağıysa a < 0’dır; c, parabolün y eksenini kestiği değerdir; tepe noktasının apsisi −b/(2a)’dır. f(k) değeri, x = k’da grafiğin eksenin üstünde mi altında mı olduğuyla bulunur. Örnek: a > 0 ve tepe x = 3’teyse b < 0’dır')

# ---------- kartlar ----------
kartla('K-AESZ-01','İkinci dereceden eşitsizlik','Kökler bulunur, başkatsayının işaretine göre aralıklar işaretlenir; kökün çözüme dahil olup olmadığı eşitsizliğin türüne göre karar verilir.','Eşitlik durumunu unutmak ya da eklemek; çift kökte işaret değiştirmek; grafikteki y değerlerini x sanmak.','kolay','grafik',3,'esz-ikidrc','İkinci dereceden eşitsizlik ve parabol')
kartla('K-AESZ-02','Çarpım eşitsizliği ve işaret tablosu','Çarpanların kökleri sıralanır, her aralıktaki işaretler çarpılarak tablo kurulur; sıfır noktaları ≥ ve ≤ durumlarına göre değerlendirilir.','Başkatsayı negatifken işareti ters başlatmak; tek noktalık çözümü atlamak; tek ve çift katlı kökü karıştırmak.','orta','tablo',4,'esz-carpim','Çarpım eşitsizliği ve işaret tablosu')
kartla('K-AESZ-03','Bölüm eşitsizliği','Her şey bir tarafa toplanıp tek kesir yapılır; pay ve paydanın kökleri işaret tablosuna konur; paydayı sıfır yapan değerler çözümden çıkarılır.','Paydayı sıfır yapan değeri çözüme katmak; çapraz çarpıp yönü korumak; ortak kökü yok saymak.','orta','düz',4,'esz-bolum','Bölüm eşitsizliği')
kartla('K-AESZ-04','Eşitsizlik sistemi','Her eşitsizlik ayrı çözülür, çözüm kümeleri sayı doğrusunda gösterilip kesiştirilir; uçların dahil olma durumu kesişimde yeniden bakılır.','Birleşim ile kesişimi karıştırmak; açık ve kapalı uçları ayırt etmemek.','orta','şekilli',4,'esz-sistem','Eşitsizlik sistemi')
kartla('K-AESZ-05','Çözüm kümesinden katsayı bulma','Çözüm kümesinin uç noktaları kök kabul edilir; çarpan biçimi yazılıp açılır; başkatsayının işaretiyle verilen eşitsizlik yönü karşılaştırılır.','Başkatsayı negatifken çarpanlı biçimi doğrudan yazmak; kök toplamı ve çarpımının işaretini karıştırmak.','orta','düz',3,'esz-katsayi','Çözüm kümesinden katsayı bulma')
kartla('K-AESZ-06','Mutlak değerli eşitsizlik','Mutlak değerin içi iki yönlü sınırla çözülür; elde edilen eşitsizlikler sistem olarak birlikte ele alınır.','Yalnız bir yönlü sınırı çözmek; |u| < a için ya da ayrımı yapmak; boş kümeyi ya da tüm gerçel sayıları fark etmemek.','orta','düz',4,'esz-mutlak','Mutlak değerli eşitsizlik')
kartla('K-AESZ-07','Grafikten eşitsizlik','Grafiklerdeki kökler okunur, her aralıkta fonksiyonların işaretleri belirlenip çarpım ya da bölümün işareti bulunur; sistem varsa kesişim alınır.','Kökte işareti sıfır saymamak; tanım aralığının uçlarını dikkate almamak; grafikleri birbirine karıştırmak.','zor','grafik',5,'esz-grafik','Grafikten eşitsizlik')
kartla('K-AESZ-08','Eşitsizlik ile model kurma','Durum eşitsizlikle yazılır, pozitiflik ve kapasite gibi koşullarla birlikte çözülür; çözüm aralığındaki uygun değerler sayılır.','Pozitiflik koşulunu unutmak; kapasite sınırını atlamak; uç değerleri yanlış saymak.','orta','hikâyeli',4,'esz-uygulama','Eşitsizlik ile model kurma')
kartla('K-AESZ-09','Parametreli eşitsizlik','Her x için sağlanma koşulu başkatsayı ve diskriminantla ya da en küçük (en büyük) değerle kurulur; parametrenin özel değeri ayrıca denenir.','Başkatsayının sıfır olduğu durumu atlamak; Δ = 0 durumunu eklemek; tepe noktasının apsisini en küçük değer sanmak.','zor','düz',4,'esz-parametre','Parametreli eşitsizlik')

# =============== KOLAY ===============
# 01 · parabol, teğet
f1=lambda x:(x-2)**2
assert S(lambda x:f1(x)>0,[2])=='(−∞, 2) ∪ (2, ∞)'
assert all(f1(Fi(k,4))>=0 for k in range(-40,60)) and f1(2)==0
assert [x for x in tam(lambda x:f1(x)<=0)]==[2]
sx=sy=0.6
g=[axes(-1,5,-1,5,sx,sy),curve(f1,-0.2,4.2,sx,sy,-1,5.2,'blue!70!black'),f'\\node[font=\\small,text=blue!70!black] at ({4.4*sx+0.15},{4.2*sy}) {{$f$}};']
SK=fig('\n'.join(g))
dog='ℝ − {2}'; yan=[('ℝ','Parabolün eksenin altına inmediğini görüp f(x) ≥ 0 koşulunu çözmüş; x = 2’de f(x) = 0 olduğundan “>” için bu değer çözüme girmez.','dikkat'),('{2}','Eksene değdiği noktayı çözüm sanmış; bu nokta f(x) = 0 olduğu yerdir, f(x) > 0 değildir.','bilgi'),('[0, ∞)','Parabolün aldığı değerleri (y) çözüm kümesi gibi yazmış; çözüm kümesi x değerlerinden oluşur.','bilgi'),('(2, ∞)','Yalnız parabolün sağ kolunun pozitif olduğunu düşünmüş; sol kol da eksenin üstündedir.','dikkat')]
q('0001',tipId='esz-ikidrc',tip='İkinci dereceden eşitsizlik ve parabol',z='kolay',alt='Grafikten Çözüm',kaz='Grafiği verilen parabol için f(x) > 0 eşitsizliğinin çözüm kümesini, eksene değen nokta dahil, belirler.',kalip='grafik',
 kart='K-AESZ-01 (teğet parabol) · parabol x eksenine bir noktada değiyor; f(x) > 0',
 metin='Şekilde, gerçel sayılar kümesi üzerinde tanımlı f fonksiyonunun grafiği verilmiştir.\nBuna göre f(x) > 0 eşitsizliğinin çözüm kümesi aşağıdakilerden hangisidir?',
 dogru=dog,yan=yan,sira=place(dog,[y[0] for y in yan],'A'),istenen='f(x) > 0 eşitsizliğinin çözüm kümesi.',ip=['Parabolün x eksenine göre konumuna ve eksene değdiği noktaya dikkat et.'],bilgi=[GRF],sekil=SK,
 ad=[A('Eksenle ilişkiyi oku','Parabol x eksenine yalnız tek noktada değiyor, başka yerde eksenin üstünde.','Değme noktası x = 2'),A('Pozitif bölgeyi belirle','f(x) > 0 olması için grafik eksenin kesinlikle üstünde olmalı; değme noktasında f(x) = 0 olduğundan o nokta dışarıda kalır.','x ≠ 2'),A('Kümeyi yaz','Çözüm kümesi gerçel sayılardan 2 çıkarılarak yazılır.','ℝ − {2}')],
 puf='Parabol eksene değiyorsa değme noktası “>” eşitsizliğinde çözüme girmez, “≥” eşitsizliğinde girer.')

# 02 · düz, çarpım
f2=lambda x:-(x+3)*(x-2)*(x-4)
dog=S(lambda x:f2(x)>=0,[-3,2,4]); assert dog=='(−∞, −3] ∪ [2, 4]'
w=[S(lambda x:f2(x)<=0,[-3,2,4]),S(lambda x:f2(x)>0,[-3,2,4]),S(lambda x:f2(x)<0,[-3,2,4]),S(lambda x:-3<=x<=4,[-3,2,4])]
assert w==['[−3, 2] ∪ [4, ∞)','(−∞, −3) ∪ (2, 4)','(−3, 2) ∪ (4, ∞)','[−3, 4]'] and len({dog,*w})==5
q('0002',tipId='esz-carpim',tip='Çarpım eşitsizliği ve işaret tablosu',z='kolay',alt='Üç Çarpanlı Eşitsizlik',kaz='Başkatsayısı negatif olan çarpanlı ifadenin işaretini tablo yaparak inceler ve eşitlikli eşitsizliğin çözüm kümesini yazar.',kalip='düz',
 kart='K-AESZ-02 (üç çarpanlı) · −(x + 3)(x − 2)(x − 4) ≥ 0; başkatsayı negatif',
 metin='x gerçel sayısı için −(x + 3)(x − 2)(x − 4) ≥ 0 olduğuna göre, x değerlerinin oluşturduğu küme aşağıdakilerden hangisidir?',
 dogru=dog,yan=[(w[0],'Ters işaretle başlamış: büyük x değerlerinde ifadenin pozitif olduğunu sanıp “≥ 0” yerine “≤ 0” bölgesini yazmış.','islem'),(w[1],'İşareti doğru bulmuş, ancak eşitlik durumunu (kökleri) çözüme katmamış.','dikkat'),(w[2],'İşareti ters başlatmış ve kökleri de dışarıda bırakmış.','islem'),(w[3],'En küçük ve en büyük kök arasını çözüm sanmış; ortadaki kökün işaret değiştirdiğini düşünmemiş.','bilgi')],
 sira=place(dog,w,'E'),istenen='Eşitsizliğin çözüm kümesi.',ip=['Büyük x değerlerinde ifadenin işaretini önce eksi önündeki katsayıyla birlikte düşün.'],bilgi=[TAB],
 ad=[A('Kökleri sırala','Her çarpanı sıfır yapan değerler bulunur.','x = −3, 2, 4'),A('Sağdan başla','x > 4 için üç çarpan pozitif, önündeki eksi nedeniyle ifade negatif. Her tek katlı kökte işaret değişir.','(4, ∞): − · (2, 4): + · (−3, 2): − · (−∞, −3): +'),A('≥ 0 olanları al','Pozitif aralıklar ve kökler çözüme girer.','(−∞, −3] ∪ [2, 4]')],
 puf='Önde eksi katsayı varsa tabloya sağdan “−” ile başla.')

# 03 · öncüllü, her x için
I3=lambda x:x*x-4*x+5>0; II3=lambda x:x*x+6*x+9>0; III3=lambda x:-x*x+2*x-3<0
def her(p): return all(p(Fi(k,4)) for k in range(-200,200))
assert (her(I3),her(II3),her(III3))==(True,False,True) and not II3(Fi(-3))
sir=['Yalnız I','Yalnız III','I ve II','I ve III','I, II ve III']
q('0003',tipId='esz-ikidrc',tip='İkinci dereceden eşitsizlik ve parabol',z='kolay',alt='Her x İçin Doğruluk',kaz='Üç ikinci derece eşitsizliğin her gerçel sayı için sağlanıp sağlanmadığını diskriminant ve başkatsayıyla değerlendirir.',kalip='öncüllü',
 kart='K-AESZ-01 (her x için) · tam kare ve negatif başkatsayılı ifadeler; I ve III doğru',
 metin='I. x² − 4x + 5 > 0\nII. x² + 6x + 9 > 0\nIII. −x² + 2x − 3 < 0\neşitsizliklerinden hangileri her x gerçel sayısı için sağlanır?',
 dogru='I ve III',yan=[('Yalnız I','III’te başkatsayının negatif olmasına bakıp “< 0” koşulunun sağlanmayacağını düşünmüş; oysa Δ < 0 ve a < 0 ise ifade hep negatiftir.','bilgi'),('Yalnız III','I’de Δ = 16 − 20 = −4 olduğunu fark etmeyip ifadenin negatif değer alabileceğini düşünmüş.','islem'),('I ve II','II’nin tam kare olduğunu görüp pozitif saymış (x = −3’te 0 olduğunu atlamış) ve III’ü başkatsayı negatif diye reddetmiş.','dikkat'),('I, II ve III','II’de tam kareyi hep pozitif sanmış; x = −3’te ifade 0 olduğundan “>” sağlanmaz.','dikkat')],
 sira=sir,istenen='Her gerçel sayı için sağlanan eşitsizlikler.',ip=['Her ifade için Δ’nın ve başkatsayının işaretine bak; Δ = 0 ise ne olduğunu ayrıca düşün.'],bilgi=[DEL],
 ad=[A('I’i incele','Δ = 16 − 20 < 0 ve a > 0 olduğundan ifade hep pozitiftir.','I doğru'),A('II’yi incele','İfade (x + 3)² biçimindedir; x = −3’te 0 olur ve “>” sağlanmaz.','II yanlış'),A('III’ü incele','Δ = 4 − 12 < 0 ve a < 0 olduğundan ifade hep negatiftir.','III doğru')],
 puf='Δ < 0 ise ifade başkatsayı ile aynı işaretlidir; Δ = 0 ise tek noktada sıfır olur.')

# 04 · hikâyeli, dikdörtgen
alan=lambda x:(x+3)*(x-1)
dog=len([x for x in range(-60,61) if x+3>0 and x-1>0 and alan(x)<=21]); assert dog==3
e=[len([x for x in range(-60,61) if x+3>0 and x-1>0 and alan(x)<21]),len([x for x in range(-60,61) if x+3>0 and x>=1 and alan(x)<=21]),len([x for x in range(-60,61) if x+3>0 and alan(x)<=21]),len([x for x in range(-60,61) if alan(x)<=21])]
assert e==[2,4,7,11] and len({dog,*e})==5
o=['\\draw[thick,fill=vurgu!18] (0,0) rectangle (4,2.4);','\\node[below=3pt] at (2,0) {$x+3$};','\\node[right=3pt] at (4,1.2) {$x-1$};','\\node at (2,1.2) {Bahçe};']
SK=fig('\n'.join(o))
q('0004',tipId='esz-uygulama',tip='Eşitsizlik ile model kurma',z='orta',alt='Bahçe Alanı',kaz='Dikdörtgenin kenar uzunluklarının pozitifliği ve alan koşulundan oluşan eşitsizliği çözüp tam sayı değerlerini sayar.',kalip='hikâyeli',
 kart='K-AESZ-08 (dikdörtgen bahçe) · kenarlar x + 3, x − 1; alan ≤ 21',
 metin='Bir okulun dikdörtgen biçimli bahçesinin kenar uzunlukları, metre cinsinden şekilde x cinsinden verilmiştir. Okul yönetimi, x bir tam sayı olmak üzere, bahçenin alanının en çok 21 m² olmasını istemektedir.\nBuna göre x kaç farklı değer alabilir?',
 dogru=dog,yan=[(e[0],'Alan koşulunu “21’den küçük” diye yorumlamış; alanı tam 21 m² yapan x = 4 değerini dışarıda bırakmış.','dikkat'),(e[1],'Kısa kenarın pozitif olması için x − 1 > 0 yerine x ≥ 1 almış; x = 1’de bir kenar 0 olur.','dikkat'),(e[2],'Yalnız uzun kenarı pozitif tutmuş (x + 3 > 0), x − 1 > 0 koşulunu unutmuş; −2’den 4’e kadar saymış.','bilgi'),(e[3],'Kenar uzunluklarının pozitif olması gerektiğini hiç hesaba katmamış; −6 ile 4 arasındaki bütün tam sayıları saymış.','bilgi')],
 istenen='x’in alabileceği tam sayı değerlerinin sayısı.',ip=['Alan eşitsizliğinin çözüm aralığındaki her x değeri gerçekten bir bahçe oluşturur mu?'],bilgi=[UYG],sekil=SK,
 ad=[A('Alan eşitsizliğini yaz','Alan, iki kenarın çarpımıdır ve en çok 21’dir.','(x + 3)(x − 1) ≤ 21 → x² + 2x − 24 ≤ 0'),A('Çöz','Çarpanlara ayrılıp işaret incelenir.','(x + 6)(x − 4) ≤ 0 → −6 ≤ x ≤ 4'),A('Kenar koşulunu ekle','Her iki kenar da pozitif olmalı; kısıtlayıcı olan x − 1 > 0’dır.','x > 1'),A('Tam sayıları say','1 < x ≤ 4 aralığındaki tam sayılar yazılır.','x = 2, 3, 4')],
 puf='Model kurduktan sonra uzunluk gibi doğal kısıtları çözüm aralığıyla kesiştirmeyi unutma.')

# =============== ORTA ===============
# 05 · işaret tablosu (f·g ≥ 0)
fa=lambda x:(x+2)*(x-3); ga=lambda x:-x*(x-3)
sg=lambda v:'+' if v>0 else '−'
crit=[-2,0,3]; mids=[-3,-1,1,4]
fs_=[sg(fa(Fi(m))) for m in mids]; gs_=[sg(ga(Fi(m))) for m in mids]
assert fs_==['+','−','−','+'] and gs_==['−','−','+','−']
pp=lambda x:fa(x)*ga(x)>=0
dog=S(pp,crit); assert dog=='[−2, 0] ∪ {3}'
w=[S(lambda x:fa(x)*ga(x)>0,crit),S(lambda x:fa(x)*ga(x)>=0 and x!=3,crit),S(lambda x:fa(x)*ga(x)<=0,crit),S(lambda x:(fa(x)*ga(x)>=0) or (x>3),crit)]
assert w==['(−2, 0)','[−2, 0]','(−∞, −2] ∪ [0, ∞)','[−2, 0] ∪ [3, ∞)'] and len({dog,*w})==5
SK=fig(sign_table(crit,[('$f(x)$',fs_,{0:'0',2:'0'}),('$g(x)$',gs_,{1:'0',2:'0'})]))
q('0005',tipId='esz-carpim',tip='Çarpım eşitsizliği ve işaret tablosu',z='orta',alt='Tabloda Çarpım',kaz='İki fonksiyonun işaret tablosundan çarpımın işaretini bulup, sıfır noktalarını da dikkate alarak f(x)·g(x) ≥ 0 çözümünü yazar.',kalip='tablo',
 kart='K-AESZ-02 (iki satırlı işaret tablosu) · ortak sıfır x = 3; tek noktalık çözüm',
 metin='f ve g polinom fonksiyonlarının işaretleri aşağıdaki tabloda verilmiştir; fonksiyonların sıfır olduğu noktalar tabloda 0 ile gösterilmiştir.\nTabloya göre f(x) · g(x) ≥ 0 olacak biçimdeki x değerleri hangi kümededir?',
 dogru=dog,yan=[(w[0],'Çarpımın pozitif olduğu aralığı bulmuş, ancak sıfır olduğu noktaları “≥” gereği çözüme katmamış.','dikkat'),(w[1],'Köşeli uçları doğru almış, ancak x = 3’te her iki fonksiyonun da sıfır olduğunu ve çarpımın orada 0 olduğunu atlamış.','dikkat'),(w[2],'Çarpımın işaretini ters yorumlayıp “≤ 0” bölgesini yazmış.','islem'),(w[3],'(3, ∞) aralığında g’nin işaretini “+” okuyup bu aralığı da çözüme katmış.','dikkat')],
 sira=place(dog,w,'A'),istenen='f(x) · g(x) ≥ 0 eşitsizliğinin çözüm kümesi.',ip=['Her aralıkta iki fonksiyonun işaretini çarp; sıfır olduğu noktalarda çarpımın değerine ayrıca bak.'],bilgi=[TAB],sekil=SK,
 ad=[A('Çarpımın işaretini bul','Her aralıkta tablodaki işaretler çarpılır.','(−∞, −2): − · (−2, 0): + · (0, 3): − · (3, ∞): −'),A('Sıfır noktalarını belirle','Çarpım, fonksiyonlardan biri 0 ise 0 olur.','x = −2, 0, 3 için çarpım 0'),A('≥ 0 olanları al','Pozitif aralık ve üç sıfır noktası alınır; 3 tek başına çözümdür.','[−2, 0] ∪ {3}')],
 puf='“≥ 0” eşitsizliklerinde işaret tablosunun dışında kalan tek noktalık sıfırlar da çözümdür.')

# 06 · katsayı
ar=Fi(-2);br=Fi(5)
# -x²+ax+b>0 çözümü (-2,5) -> a=3,b=10
a_,b_=3,10
assert S(lambda x:-x*x+a_*x+b_>0,[-2,5])=='(−2, 5)'
assert (a_+b_)==13
e=[-3-10,3-10,-3+10,3*10]
assert e==[-13,-7,7,30] and len({13,*e})==5
q('0006',tipId='esz-katsayi',tip='Çözüm kümesinden katsayı bulma',z='orta',alt='Çözümden Katsayı',kaz='Çözüm kümesi verilen ve başkatsayısı negatif olan eşitsizlikteki bilinmeyen katsayıları bulur.',kalip='düz',
 kart='K-AESZ-05 (başkatsayı −1) · −x² + ax + b > 0 çözümü (−2, 5)',
 metin='a ve b gerçel sayılar olmak üzere,\n−x² + ax + b > 0\neşitsizliğinin çözüm kümesi (−2, 5) aralığıdır.\nBuna göre a + b toplamı kaçtır?',
 dogru=13,yan=[(e[0],'Başkatsayıyı +1 alıp x² + ax + b < 0 gibi çözmüş: (x + 2)(x − 5) = x² − 3x − 10 ile a = −3, b = −10 bulmuş.','bilgi'),(e[1],'Ters işaretle çarpanlayıp b’nin işaretini yanlış bulmuş: a = 3, b = −10.','islem'),(e[2],'Kök toplamını yanlış yorumlayıp a’yı −3 bulmuş, b’yi 10 almış.','islem'),(e[3],'a + b yerine a · b çarpımını hesaplamış.','dikkat')],
 istenen='a + b toplamı.',ip=['Çözüm aralığının uçları hakkında ne biliyorsun; aralığın içinde ifadenin işareti ne?'],bilgi=[KOK],
 ad=[A('Kökleri yaz','Aralığın uçları kökler: −2 ve 5. Başkatsayı −1 olduğundan ifade −(x + 2)(x − 5) biçimindedir.','−(x + 2)(x − 5)'),A('Çarpanı aç','Parantezler çarpılıp önündeki eksi dağıtılır.','−(x² − 3x − 10) = −x² + 3x + 10'),A('Katsayıları oku','Verilen ifadeyle katsayılar karşılaştırılır.','a = 3, b = 10'),A('Toplamı bul','a ile b toplanır.','3 + 10 = 13')],
 puf='Başkatsayı negatifse “aralık içinde pozitif” demek, ifadenin −(x − p)(x − r) olması demektir.')

# 07 · sayı doğrusu, ters problem
A1=lambda x:x*x-x-12; B1=lambda x:x*x-x-2
crit7=[-3,-1,2,4]
hedef=S(lambda x:A1(x)<0 and B1(x)>=0,crit7); assert hedef=='(−3, −1] ∪ [2, 4)'
sist=[('x² − x − 12 < 0 ve x² − x − 2 ≥ 0',lambda x:A1(x)<0 and B1(x)>=0),('x² − x − 12 ≤ 0 ve x² − x − 2 ≥ 0',lambda x:A1(x)<=0 and B1(x)>=0),('x² − x − 12 < 0 ve x² − x − 2 > 0',lambda x:A1(x)<0 and B1(x)>0),('x² − x − 12 < 0 ve x² − x − 2 ≤ 0',lambda x:A1(x)<0 and B1(x)<=0),('x² − x − 12 > 0 ve x² − x − 2 ≥ 0',lambda x:A1(x)>0 and B1(x)>=0)]
sets=[S(p,crit7) for _,p in sist]
assert sets[0]==hedef and len(set(sets))==5 and sets[1]=='[−3, −1] ∪ [2, 4]' and sets[2]=='(−3, −1) ∪ (2, 4)' and sets[3]=='[−1, 2]'
SK=fig(nline(-4,5,[(-3,-1,False,True),(2,4,True,False)],sx=0.85))
dog=sist[0][0]; w=[s[0] for s in sist[1:]]
q('0007',tipId='esz-sistem',tip='Eşitsizlik sistemi',z='orta',alt='Sayı Doğrusu ve Sistem',kaz='Sayı doğrusunda gösterilen kümeyi, uç noktaların dahil olup olmadığına bakarak eşitsizlik sistemiyle eşleştirir.',kalip='şekilli',
 kart='K-AESZ-04 (ters sistem) · iki ikinci derece eşitsizlik; iki parçalı çözüm kümesi',
 metin='Aşağıdaki sayı doğrusunda taralı bölge, bir eşitsizlik sisteminin çözüm kümesini göstermektedir; içi dolu nokta o değerin çözüme dahil olduğunu, içi boş nokta dahil olmadığını belirtir.\nBuna göre bu çözüm kümesine sahip sistem aşağıdakilerden hangisidir?',
 dogru=dog,yan=[(w[0],'Birinci eşitsizlikte eşitliği de almış; −3 ve 4 uçları çözüme dahil olmamalı.','dikkat'),(w[1],'İkinci eşitsizlikte “≥” yerine “>” seçmiş; −1 ve 2 uçlarının dahil olduğunu atlamış.','dikkat'),(w[2],'İkinci eşitsizliğin yönünü ters seçmiş; bu durumda kökler arası çözüm olur.','islem'),(w[3],'Birinci eşitsizliği ters yönde almış; kökler dışını çözüm sanmış.','islem')],
 sira=place(dog,w,'C'),istenen='Taralı çözüm kümesini veren eşitsizlik sistemi.',ip=['Seçeneklerdeki eşitsizlikleri ayrı ayrı çözüp çözüm kümelerinin kesişimini sayı doğrusuyla karşılaştır.'],bilgi=[SIS,IKI],sekil=SK,
 ad=[A('Eşitsizlikleri çöz','x² − x − 12 = (x − 4)(x + 3) ve x² − x − 2 = (x − 2)(x + 1) olduğundan kökler −3, 4 ve −1, 2’dir.','x² − x − 12 < 0 → (−3, 4) · x² − x − 2 ≥ 0 → (−∞, −1] ∪ [2, ∞)'),A('Kesişimi al','Ortak kısım alınır; uçların dahil olma durumuna bakılır.','(−3, −1] ∪ [2, 4)'),A('Şekille karşılaştır','−3 ve 4 boş, −1 ve 2 dolu noktadır; bu sistem şekle uyar.','Şekille uyumlu')],
 puf='Sistemde uç noktalar için her eşitsizliğin dahil/hariç durumuna kesişimde ayrı ayrı bak.')

# 08 · bölüm
pr=lambda x:(2*x-1)/(x+3)<=1
dog=S(pr,[-3,4]); assert dog=='(−3, 4]'
w=[S(lambda x:2*x-1<=x+3,[-3,4]),S(lambda x:(2*x-1)/(x+3)<1,[-3,4]),S(lambda x:(x-4)*(x+3)<=0,[-3,4]),S(lambda x:(x-4)/(x+3)>=0,[-3,4])]
assert w==['(−∞, 4]','(−3, 4)','[−3, 4]','(−∞, −3) ∪ [4, ∞)'] and len({dog,*w})==5
q('0008',tipId='esz-bolum',tip='Bölüm eşitsizliği',z='orta',alt='Kesirli Eşitsizlik',kaz='Kesirli eşitsizliği tek kesir hâline getirip payda sıfır değerini dışarıda bırakarak çözer.',kalip='düz',
 kart='K-AESZ-03 (1’e eşitlenmiş kesir) · (2x − 1)/(x + 3) ≤ 1',
 metin='(2x − 1)/(x + 3) ≤ 1\nolduğuna göre x’in alabileceği gerçel sayı değerlerinin kümesi aşağıdakilerden hangisidir?',
 dogru=dog,yan=[(w[0],'Paydayı çarpıp eşitsizlik yönünü korumuş: 2x − 1 ≤ x + 3. Payda negatifken yön değişir ve x = −3 zaten tanımsızdır.','bilgi'),(w[1],'Sınırları doğru bulmuş, ancak “≤” gereği x = 4 değerini çözüme katmamış.','dikkat'),(w[2],'Pay ve paydanın köklerini kapalı uçla alıp x = −3’ü de çözüme katmış; payda sıfır olamaz.','dikkat'),(w[3],'Kesri “≥ 0” biçiminde yazıp işareti ters değerlendirmiş.','islem')],
 sira=place(dog,w,'E'),istenen='Eşitsizliğin çözüm kümesi.',ip=['Sağdaki terimi sola atıp tek kesir hâline getir; çapraz çarpma yapma.'],bilgi=[TAB],
 ad=[A('Tek kesir yap','1 sola alınıp ortak paydaya getirilir.','(2x − 1 − x − 3)/(x + 3) ≤ 0 → (x − 4)/(x + 3) ≤ 0'),A('Kökleri işaretle','Payın kökü 4 (dahil), paydanın kökü −3 (dahil değil).','x = 4 ve x = −3'),A('Tabloyu kur','x > 4 için kesir pozitif; −3 ile 4 arasında negatif; x < −3 için pozitif.','(−3, 4] için ≤ 0'),A('Kümeyi yaz','Payda sıfırı olan −3 dışarıda, 4 içeride.','(−3, 4]')],
 puf='Kesirli eşitsizlikte çapraz çarpma yapma; her şeyi tek tarafa toplayıp işaret tablosu kur.')

# 09 · mutlak
mu=lambda x:abs(x*x-5)<4
dog=S(mu,[-3,-1,1,3]); assert dog=='(−3, −1) ∪ (1, 3)'
w=[S(lambda x:x*x-5<4,[-3,-1,1,3]),S(lambda x:x*x-5>-4,[-3,-1,1,3]),S(lambda x:abs(x*x-5)<=4,[-3,-1,1,3]),S(lambda x:x*x<1,[-3,-1,1,3])]
assert w==['(−3, 3)','(−∞, −1) ∪ (1, ∞)','[−3, −1] ∪ [1, 3]','(−1, 1)'] and len({dog,*w})==5
q('0009',tipId='esz-mutlak',tip='Mutlak değerli eşitsizlik',z='orta',alt='İkinci Dereceli Mutlak Değer',kaz='İçinde ikinci dereceden ifade bulunan mutlak değerli eşitsizliği iki yönlü sınırla çözüp kesişimi alır.',kalip='düz',
 kart='K-AESZ-06 (|x² − 5| < 4) · iki yönlü sınır; kesişim iki ayrık aralık',
 metin='|x² − 5| < 4\nkoşulunu sağlayan gerçel sayıların kümesi aşağıdakilerden hangisidir?',
 dogru=dog,yan=[(w[0],'Yalnız x² − 5 < 4 koşulunu çözmüş; alt sınır olan x² − 5 > −4 koşulunu atlamış.','bilgi'),(w[1],'Yalnız x² − 5 > −4 koşulunu çözmüş; üst sınırı hesaba katmamış.','bilgi'),(w[2],'Eşitsizliği “≤” gibi çözüp uçları dahil etmiş.','dikkat'),(w[3],'x² − 5 < −4 durumunu çözüp bunu çözüm sanmış; bu, mutlak değerin kenarındaki yanlış yön seçimidir.','islem')],
 sira=place(dog,w,'A'),istenen='Eşitsizliğin çözüm kümesi.',ip=['Mutlak değerin içini hem alt hem üst sınırla kıyasla ve iki durumu birlikte sağlayan x değerlerini ara.'],bilgi=[MUT,SIS],
 ad=[A('Çift yönlü yaz','|u| < a eşitsizliği −a < u < a demektir.','−4 < x² − 5 < 4'),A('Her yönü çöz','İki eşitsizlik ayrı ayrı çözülür.','x² > 1 → x < −1 veya x > 1 · x² < 9 → −3 < x < 3'),A('Kesişimi al','Her ikisini birlikte sağlayan değerler alınır.','(−3, −1) ∪ (1, 3)')],
 puf='|u| < a tek bir sistemdir: iki sınırı birlikte sağlayan değerleri bul.')

# 10 · grafik, iki fonksiyon
fq=lambda x:(x+2)*(x-1); gq=lambda x:3-x
dom=lambda x:-3<=x<=3
dog=S(lambda x:dom(x) and fq(x)*gq(x)>0,[-3,-2,1,3]); assert dog=='[−3, −2) ∪ (1, 3)'
w=[S(lambda x:dom(x) and fq(x)*gq(x)>=0,[-3,-2,1,3]),S(lambda x:dom(x) and fq(x)*gq(x)<0,[-3,-2,1,3]),S(lambda x:fq(x)*gq(x)>0,[-3,-2,1,3]),S(lambda x:dom(x) and fq(x)*gq(x)>0 and x!=-3,[-3,-2,1,3])]
assert w==['[−3, −2] ∪ [1, 3]','(−2, 1)','(−∞, −2) ∪ (1, 3)','(−3, −2) ∪ (1, 3)'] and len({dog,*w})==5
sx,sy=0.65,0.2
cc=[axes(-3,3,-3,10,sx,sy,yt=[2,4,6,8,10]),curve(fq,-3,3,sx,sy,-3,10.5,'blue!70!black'),curve(gq,-3,3,sx,sy,-3,10.5,'orange!85!black'),f'\\node[text=blue!70!black,font=\\small] at ({3*sx+0.2},{10*sy}) {{$f$}};',f'\\node[text=orange!85!black,font=\\small] at ({-3*sx-0.25},{6*sy}) {{$g$}};']
SK=fig('\n'.join(cc))
q('0010',tipId='esz-grafik',tip='Grafikten eşitsizlik',z='orta',alt='İki Grafik ve Çarpım',kaz='Tanım aralığı verilen iki fonksiyonun grafiğinden köklerini okuyarak f(x)·g(x) > 0 çözüm kümesini kapalı uç dahil yazar.',kalip='grafik',
 kart='K-AESZ-07 (parabol ve doğru) · f(x)·g(x) > 0; kapalı tanım aralığı',
 metin='Şekilde, [−3, 3] kapalı aralığında tanımlı f ve g fonksiyonlarının grafikleri verilmiştir; grafikler kılavuz çizgilerin kesişim noktalarında eksenleri kesmektedir.\nBuna göre f(x) · g(x) > 0 eşitsizliğinin çözüm kümesi aşağıdakilerden hangisidir?',
 dogru=dog,yan=[(w[0],'Çarpımın sıfır olduğu noktaları da çözüme katmış; eşitsizlik “>” olduğundan kökler dahil değildir.','dikkat'),(w[1],'Çarpımın negatif olduğu bölgeyi yazmış.','islem'),(w[2],'Tanım aralığını dikkate almadan işaret çözümünü yazmış.','dikkat'),(w[3],'Tanım aralığının sol ucu −3’ü açık sanmış; −3 tanım kümesine ve çözüme aittir.','dikkat')],
 sira=place(dog,w,'E'),istenen='f(x) · g(x) > 0 eşitsizliğinin çözüm kümesi.',ip=['Grafiklerin x eksenini kestiği noktaları okuyup her aralıkta her iki fonksiyonun işaretini ayrı ayrı belirle.'],bilgi=[GRF,TAB],sekil=SK,
 ad=[A('Kökleri oku','f x eksenini −2 ve 1’de, g ise 3’te keser.','x = −2, 1, 3'),A('İşaretleri belirle','f: (−3, −2) pozitif, (−2, 1) negatif, (1, 3] pozitif. g: [−3, 3) pozitif, x = 3’te sıfır.','Çarpım: + , − , +'),A('Pozitif aralıkları al','Çarpım pozitif olan aralıklar yazılır; −3 tanım kümesinde ve pozitif.','[−3, −2) ve (1, 3)'),A('Kümeyi yaz','Aralıkların birleşimi alınır.','[−3, −2) ∪ (1, 3)')],
 puf='Grafikte fonksiyon çarpımı sorulduğunda her fonksiyonun kökünü ve tanım aralığının uçlarını ayrı ayrı işle.')

# 11 · hikâyeli, kâr
K=lambda x:-2*x*x+72*x-448
ok=[x for x in range(0,21) if K(x)>0]; dog=len(ok); assert (dog,ok[0],ok[-1])==(12,9,20)
e=[len([x for x in range(0,29) if K(x)>0]),len([x for x in range(0,21) if K(x)>=0]),len([x for x in range(0,20) if K(x)>0]),20]
assert e==[19,13,11,20] and len({dog,*e})==5
q('0011',tipId='esz-uygulama',tip='Eşitsizlik ile model kurma',z='orta',alt='Üretim ve Kâr',kaz='İkinci dereceden kâr fonksiyonunun pozitif olduğu aralığı kapasite sınırıyla kesiştirip uygun üretim adetlerini sayar.',kalip='hikâyeli',
 kart='K-AESZ-08 (atölye kârı) · K(x) = −2x² + 72x − 448 > 0 ve kapasite',
 metin='Bir seramik atölyesi, günde x adet kupa üretip satmaktadır. Atölyenin günlük kârı, TL cinsinden K(x) = −2x² + 72x − 448 fonksiyonuyla hesaplanmaktadır. Atölyenin makineleri günde en fazla 20 kupa üretebilmektedir.\nAtölye günlük kârının pozitif olmasını istediğine göre, günlük üretim adedi x kaç farklı doğal sayı değeri alabilir?',
 dogru=dog,yan=[(e[0],'Kapasite sınırını (en fazla 20) hesaba katmamış; kâr pozitifken 9’dan 27’ye kadar bütün adetleri saymış.','dikkat'),(e[1],'Kâr için “≥ 0” kullanıp kârın 0 olduğu x = 8 değerini de saymış; kâr pozitif olmalı.','dikkat'),(e[2],'Kapasite sınırı olan x = 20’yi dışarıda bırakmış; “en fazla” 20 dahil demektir.','dikkat'),(e[3],'Kâr koşulunu hiç kullanmamış, 1’den 20’ye kadar bütün adetleri saymış.','bilgi')],
 istenen='Günlük üretim adedinin alabileceği doğal sayı değerlerinin sayısı.',ip=['Kâr fonksiyonunu çarpanlarına ayır ve kapasite koşulunu aynı sayı doğrusunda göster.'],bilgi=[UYG,IKI],
 ad=[A('Kâr eşitsizliğini yaz','K(x) > 0 koşulu eşitsizlik olarak yazılır ve −2 ile bölünüp yön değiştirilir.','−2x² + 72x − 448 > 0 → x² − 36x + 224 < 0'),A('Çarpanlara ayır','Kökler 8 ve 28’dir; kökler arası negatiftir.','(x − 8)(x − 28) < 0 → 8 < x < 28'),A('Kapasiteyi ekle','Günlük en fazla 20 kupa üretilebilir.','8 < x ≤ 20'),A('Say','9’dan 20’ye kadar olan doğal sayılar sayılır.','20 − 9 + 1 = 12')],
 puf='Uygulama sorularında modelin çözümü ile fiziksel sınırı (kapasite) birlikte değerlendir.')

# 12 · parabol grafiği, f(x) ≥ 5
f12=lambda x:x*x-2*x-3
assert (f12(-1),f12(3),f12(1))==(0,0,-4)
dog=S(lambda x:f12(x)>=5,[-2,4]); assert dog=='(−∞, −2] ∪ [4, ∞)'
w=[S(lambda x:f12(x)>=0,[-2,-1,3,4]),S(lambda x:f12(x)<=5,[-2,4]),S(lambda x:f12(x)>5,[-2,4]),S(lambda x:f12(x)<=0,[-1,3])]
assert w==['(−∞, −1] ∪ [3, ∞)','[−2, 4]','(−∞, −2) ∪ (4, ∞)','[−1, 3]'] and len({dog,*w})==5
sx,sy=0.55,0.3
cc=[axes(-3,5,-5,7,sx,sy,yt=[-4,2,4,6]),curve(f12,-2.6,4.6,sx,sy,-5,7,'blue!70!black'),'\\fill[blue!70!black] (1*0.55,-4*0.3) circle (0.07);','\\node[font=\\footnotesize,below right] at (1*0.55,-4*0.3) {$(1,-4)$};','\\node[text=blue!70!black,font=\\small] at (4.5*0.55+0.3,6.3*0.3) {$f$};']
SK=fig('\n'.join(cc))
q('0012',tipId='esz-ikidrc',tip='İkinci dereceden eşitsizlik ve parabol',z='orta',alt='Grafikten Denklem ve Eşitsizlik',kaz='Köklerini ve tepe noktasını okuyarak ikinci derece fonksiyonu belirler, f(x) ≥ 5 eşitsizliğini çözer.',kalip='grafik',
 kart='K-AESZ-01 (parabol grafiği) · f(x) = x² − 2x − 3; f(x) ≥ 5',
 metin='Şekilde, f(x) = ax² + bx + c ikinci dereceden fonksiyonunun grafiği verilmiştir; grafik x eksenini ızgara çizgilerinin kesiştiği noktalarda kesmektedir.\nBuna göre f(x) ≥ 5 eşitsizliğinin çözüm kümesi aşağıdakilerden hangisidir?',
 dogru=dog,yan=[(w[0],'Grafikte 5 değerini okumak yerine eksenle kesişim noktalarına bakıp f(x) ≥ 0 çözmüş.','dikkat'),(w[1],'Doğru kökleri bulmuş, ancak eşitsizliğin yönünü ters değerlendirip f(x) ≤ 5 yazmış.','islem'),(w[2],'Eşitliği çözüme katmamış; “≥” olduğundan x = −2 ve x = 4 çözüme dahildir.','dikkat'),(w[3],'f(x) ≤ 0 bölgesini (köklerin arasını) yazmış.','bilgi')],
 sira=place(dog,w,'C'),istenen='f(x) ≥ 5 eşitsizliğinin çözüm kümesi.',ip=['Önce grafikten fonksiyonun kuralını belirle; sonra eşitsizliği 0’a eşitleyecek biçimde yaz.'],bilgi=[GRF,IKI],sekil=SK,
 ad=[A('Fonksiyonu bul','Kökler −1 ve 3 olduğundan f(x) = a(x + 1)(x − 3); (1, −4) noktası a’yı belirler.','a · 2 · (−2) = −4 → a = 1 → f(x) = x² − 2x − 3'),A('Eşitsizliği kur','f(x) ≥ 5 sol tarafa toplanır.','x² − 2x − 8 ≥ 0'),A('Çarpanlara ayır','Kökler −2 ve 4; dışı pozitif.','(x − 4)(x + 2) ≥ 0'),A('Kümeyi yaz','Kökler dahil, aralıkların dışı alınır.','(−∞, −2] ∪ [4, ∞)')],
 puf='Parabolün kuralını kökler ve bir ek nokta yeter; eşitsizliği önce 0’a eşitle.')

# 13 · öncüllü, x ∈ (−3, −1)
I13=lambda x:x*x+x-2<0; II13=lambda x:x*(x+2)>0; III13=lambda x:x*x-1>0
def aralik(p): return all(p(Fi(k,16)) for k in range(-47,-17))   # (-3,-1) içi örnek
assert (aralik(I13),aralik(II13),aralik(III13))==(False,False,True)
sir=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III']
q('0013',tipId='esz-ikidrc',tip='İkinci dereceden eşitsizlik ve parabol',z='orta',alt='Aralıktan Yargı',kaz='Bir x aralığı için verilen ikinci derece ifadelerin işaretini aralığa göre değerlendirerek kesinlikle doğru olan yargıyı belirler.',kalip='öncüllü',
 kart='K-AESZ-01 (aralık içinde işaret) · −3 < x < −1; yalnız III doğru',
 metin='−3 < x < −1 olduğuna göre,\nI. x² + x − 2 < 0\nII. x(x + 2) > 0\nIII. x² − 1 > 0\neşitsizliklerinden hangileri kesinlikle doğrudur?',
 dogru='Yalnız III',yan=[('Yalnız I','I’i yalnız x = −1,5 gibi bir değerle sınayıp negatif bulmuş; x = −2,5 için ifade pozitiftir.','dikkat'),('Yalnız II','II’yi yalnız x = −2,5 ile sınayıp pozitif bulmuş; x = −1,5 için çarpım negatiftir.','dikkat'),('I ve II','I’i x = −1,5 ile, II’yi x = −2,5 ile sınamış; her yargıyı aralığın yalnız bir parçasında denemiş.','dikkat'),('I ve III','I’i yalnız x = −1,5 ile sınayıp doğru saymış; III’ü ise doğru bulmuş.','dikkat')],
 sira=sir,istenen='Kesinlikle doğru olan eşitsizlikler.',ip=['“Kesinlikle” ifadesi için aralığın her yerinde sağlanıp sağlanmadığını, özellikle −2 civarında, kontrol et.'],bilgi=[IKI,TAB],
 ad=[A('I’i sına','Köklerin −2 ve 1 olduğuna bak; −3 < x < −2 için ifade pozitiftir.','x = −2,5 → 6,25 − 2,5 − 2 > 0 → I yanlış'),A('II’yi sına','−2 < x < −1 için x negatif, x + 2 pozitif; çarpım negatiftir.','x = −1,5 → (−1,5)(0,5) < 0 → II yanlış'),A('III’ü incele','x² aralıkta 1’den büyük kalır.','1 < x² < 9 → x² − 1 > 0 → III doğru')],
 puf='“Kesinlikle doğru” için aralığın uç bölgelerinden birer değer deneyerek yargıyı sına.')

# 14 · sayı doğrusu, A ∩ B
Bk=lambda x:x*x-2*x-8>0
Ak=lambda x:-4<=x<3
dog=sum(tam(lambda x:Ak(x) and Bk(x))); assert dog==-7 and tam(lambda x:Ak(x) and Bk(x))==[-4,-3]
e=[sum(tam(lambda x:Ak(x) and x*x-2*x-8>=0)),sum(tam(lambda x:-4<x<3 and Bk(x))),sum(tam(lambda x:Ak(x) and -2<=x<=4)),len(tam(lambda x:Ak(x) and Bk(x)))]
assert e==[-9,-3,0,2] and len({dog,*e})==5
SK=fig(nline(-5,5,[(-4,3,True,False)],sx=0.8))
q('0014',tipId='esz-sistem',tip='Eşitsizlik sistemi',z='orta',alt='Küme ve Eşitsizlik',kaz='Sayı doğrusunda verilen aralık ile ikinci derece eşitsizliğin çözüm kümesinin kesişimindeki tam sayıları bulur.',kalip='şekilli',
 kart='K-AESZ-04 (kesişim ve tam sayı) · [−4, 3) ve x² − 2x − 8 > 0',
 metin='Aşağıdaki sayı doğrusunda taralı bölge A kümesini göstermektedir; içi dolu nokta o değerin kümeye ait olduğunu, içi boş nokta ait olmadığını belirtir. B kümesi, B = {x : x² − 2x − 8 > 0, x ∈ ℝ} biçiminde tanımlanmıştır.\nBuna göre A ∩ B kümesinin tam sayı elemanlarının toplamı kaçtır?',
 dogru=dog,yan=[(e[0],'B’yi “≥ 0” gibi çözüp −2’yi de kümeye katmış: −4, −3, −2 toplanmış.','dikkat'),(e[1],'A kümesinin sol ucunu (−4) açık sanmış; yalnız −3’ü toplamış.','dikkat'),(e[2],'Eşitsizliğin yönünü ters değerlendirip x² − 2x − 8 ≤ 0 (kökler arası, uçlar dahil) çözmüş; −2, −1, 0, 1, 2’yi toplamış.','islem'),(e[3],'Tam sayıların toplamı yerine tam sayı sayısını yazmış.','dikkat')],
 istenen='A ∩ B kümesinin tam sayı elemanlarının toplamı.',ip=['B kümesini bulup sayı doğrusuna taşı; ortak bölgedeki uçların dahil olup olmadığına dikkat et.'],bilgi=[SIS,IKI],sekil=SK,
 ad=[A('B’yi çöz','x² − 2x − 8 = (x − 4)(x + 2); kökler dışı pozitif.','B = (−∞, −2) ∪ (4, ∞)'),A('Kesişimi al','A = [−4, 3) ile ortak bölge bulunur.','A ∩ B = [−4, −2)'),A('Tam sayıları yaz','−4 dahil, −2 dahil değil.','−4, −3'),A('Topla','İki tam sayı toplanır.','−4 + (−3) = −7')],
 puf='Kesişimde sağ ve sol ucun dahil olup olmadığını iki kümenin kuralına göre ayrı ayrı belirle.')

# =============== ZOR ===============
# 15 · parametre (her x için, başkatsayı sıfır özel durumu)
def hepx(m):
    a=m-1
    if a==0: return True            # 3 > 0
    return a>0 and 3-a>0             # en küçük değer x = −1'de 3 − a
for m in range(-8,9):
    a=m-1; ref=all(a*x*x+2*a*x+3>0 for x in [Fi(k,8) for k in range(-160,160)]) if a>=0 else False
    if a>0: ref=min(a*x*x+2*a*x+3 for x in [Fi(k,8) for k in range(-160,160)])>0
    assert hepx(m)==ref,(m,)
ms=[m for m in range(-60,61) if hepx(m)]; assert ms==[1,2,3]; dog=sum(ms)
e=[sum(m for m in range(-60,61) if m>1 and hepx(m)),sum(m for m in range(1,5)),sum(m for m in range(2,5)),len(ms)]
assert dog==6 and e==[5,10,9,3] and len({dog,*e})==5
q('0015',tipId='esz-parametre',tip='Parametreli eşitsizlik',z='zor',alt='Her x İçin ve Başkatsayı',kaz='Başkatsayısı parametre olan ikinci derece eşitsizliğin her x için sağlanma koşulunu, başkatsayının sıfır olduğu özel durumu da inceleyerek çözer.',kalip='düz',
 kart='K-AESZ-09 (başkatsayı parametreli) · (m − 1)x² + 2(m − 1)x + 3 > 0; m = 1 özel durumu',
 metin='m bir tam sayı olmak üzere,\n(m − 1)x² + 2(m − 1)x + 3 > 0\neşitsizliği her x gerçel sayısı için sağlanıyor.\nBuna göre m’nin alabileceği değerlerin toplamı kaçtır?',
 dogru=dog,yan=[(e[0],'Başkatsayının sıfır olduğu m = 1 durumunu denemeden yalnız Δ < 0 koşulunu kullanmış: 2 + 3.','dikkat'),(e[1],'Δ ≤ 0 koşulunu alıp m = 4’ü de katmış; m = 4’te ifade 3(x + 1)² olur ve x = −1’de 0 çıkar. m = 1’i de saymış.','dikkat'),(e[2],'Δ ≤ 0 koşulunu kullanıp m = 4’ü katmış ve m = 1 durumunu denemeden dışarıda bırakmış.','dikkat'),(e[3],'Değerlerin toplamı yerine kaç değer olduğunu yazmış.','dikkat')],
 istenen='m’nin alabileceği tam sayı değerlerinin toplamı.',ip=['Eşitsizliğin ikinci derece olmadığı bir m değeri var mı? Parametrenin tüm olası durumlarını say.'],bilgi=[DEL],
 ad=[A('Özel durumu dene','m = 1 için ifade 3 > 0 olur ve her x için doğrudur.','m = 1 uygun'),A('Başkatsayıyı pozitif al','Parabolün her yerde pozitif olması için kollar yukarı bakmalı.','m − 1 > 0'),A('Δ < 0 koşulunu kur','Δ = 4(m − 1)² − 12(m − 1) negatif olmalı.','4(m − 1)(m − 4) < 0 → 1 < m < 4'),A('Tam sayıları topla','m = 1 ile birlikte 1 ≤ m < 4 aralığındaki tam sayılar alınır.','1 + 2 + 3 = 6')],
 puf='Başkatsayısında parametre olan ikinci derece eşitsizlikte önce başkatsayının sıfır olduğu durumu ayrı incele.')

# 16 · üç grafik, eşitsizlik sistemi
F16=lambda x:x*x-4; G16=lambda x:1-x; H16=lambda x:(x*x-9)/3
d16=lambda x:-4<=x<=4
c16=[-4,-3,-2,1,2,3,4]
sis=lambda a,b:(lambda x:d16(x) and a(x))
dog=S(lambda x:d16(x) and F16(x)*G16(x)>0 and G16(x)*H16(x)<0,c16); assert dog=='(−3, −2)'
w=[S(lambda x:d16(x) and F16(x)*G16(x)>=0 and G16(x)*H16(x)<=0,c16),S(lambda x:d16(x) and F16(x)*G16(x)>0 and G16(x)*H16(x)>0,c16),S(lambda x:d16(x) and F16(x)*G16(x)<0 and G16(x)*H16(x)<0,c16),S(lambda x:d16(x) and F16(x)*G16(x)>0,c16)]
assert w==['[−3, −2] ∪ {1}','[−4, −3) ∪ (1, 2)','(−2, 1) ∪ (3, 4]','[−4, −2) ∪ (1, 2)'],w
assert len({dog,*w})==5
sx,sy=0.7,0.2
cc=[axes(-4,4,-5,12,sx,sy,yt=[]),curve(F16,-4,4,sx,sy,-5,12.5,'blue!70!black'),curve(G16,-4,4,sx,sy,-5,12.5,'orange!85!black'),curve(H16,-4,4,sx,sy,-5,12.5,'violet!80!black'),
 f'\\node[text=blue!70!black,font=\\small] at ({4*sx+0.15},{12*sy}) {{$f$}};',f'\\node[text=orange!85!black,font=\\small] at ({-4*sx-0.25},{5*sy}) {{$g$}};',f'\\node[text=violet!80!black,font=\\small] at ({4*sx+0.25},{2.4*sy}) {{$h$}};']
SK=fig('\n'.join(cc))
q('0016',tipId='esz-grafik',tip='Grafikten eşitsizlik',z='zor',alt='Üç Grafikli Sistem',kaz='Üç fonksiyonun grafiğinden köklerini okuyarak iki çarpım eşitsizliğinden oluşan sistemin çözüm kümesini tanım aralığına göre bulur.',kalip='grafik',
 kart='K-AESZ-07 (üç grafik, iki çarpım) · f·g > 0 ve g·h < 0; kapalı tanım aralığı',
 metin='Şekilde, [−4, 4] kapalı aralığında tanımlı f, g ve h fonksiyonlarının grafikleri verilmiştir; grafikler x eksenini ızgara çizgilerinin kesiştiği noktalarda kesmektedir.\nBuna göre,\nf(x) · g(x) > 0\ng(x) · h(x) < 0\neşitsizlik sisteminin çözüm kümesi aşağıdakilerden hangisidir?',
 dogru=dog,yan=[(w[0],'Eşitsizlikleri “≥ 0” ve “≤ 0” gibi çözüp kök noktalarını da çözüme katmış.','dikkat'),(w[1],'İkinci eşitsizliği ters yönde (g · h > 0) çözmüş.','islem'),(w[2],'Her iki çarpımı da ters işaretle çözmüş (f · g < 0 ve g · h < 0).','islem'),(w[3],'Yalnız birinci eşitsizliği çözüp ikincisini hesaba katmamış.','bilgi')],
 sira=place(dog,w,'A'),istenen='Eşitsizlik sisteminin çözüm kümesi.',ip=['Her çarpımı ayrı ayrı çözüp çözüm kümelerini sayı doğrusunda kesiştir.'],bilgi=[GRF,SIS],sekil=SK,
 ad=[A('Kökleri oku','f: −2 ve 2, g: 1, h: −3 ve 3’te x eksenini keser.','f: ±2 · g: 1 · h: ±3'),A('f · g > 0’ı çöz','f: (−4, −2) pozitif, (−2, 2) negatif, (2, 4) pozitif. g: x < 1 pozitif, x > 1 negatif.','[−4, −2) ∪ (1, 2)'),A('g · h < 0’ı çöz','h: (−4, −3) pozitif, (−3, 3) negatif, (3, 4] pozitif.','(−3, 1) ∪ (3, 4]'),A('Kesiştir','İki çözüm kümesinin ortak kısmı alınır.','(−3, −2)')],
 puf='Sistemde çarpımları ayrı çöz, sonra kesiştirmeden önce her çözüm kümesini sayı doğrusuna yaz.')

# 17 · tablo, ortak kök, bölüm
f17=lambda x:(x+3)*(x-2); g17=lambda x:(x-2)*(x+1)
c17=[-3,-1,2]; m17=[-4,-2,0,3]
fs_=[sg(f17(Fi(m))) for m in m17]; gs_=[sg(g17(Fi(m))) for m in m17]
assert fs_==['+','−','−','+'] and gs_==['+','+','−','+']
def bol(x): return f17(x)/g17(x)>=0
dog=S(bol,c17); assert dog=='(−∞, −3] ∪ (−1, 2) ∪ (2, ∞)'
w=[S(lambda x:(x+3)/(x+1)>=0,c17),S(lambda x:g17(x)!=0 and f17(x)/g17(x)>0,c17),S(lambda x:f17(x)*g17(x)>=0,c17),S(lambda x:g17(x)!=0 and f17(x)/g17(x)<=0,c17)]
assert w==['(−∞, −3] ∪ (−1, ∞)','(−∞, −3) ∪ (−1, 2) ∪ (2, ∞)','(−∞, −3] ∪ [−1, ∞)','[−3, −1) ∪ {2}'.replace(' ∪ {2}','')],w
assert len({dog,*w})==5
SK=fig(sign_table(c17,[('$f(x)$',fs_,{0:'0',2:'0'}),('$g(x)$',gs_,{1:'0',2:'0'})]))
q('0017',tipId='esz-bolum',tip='Bölüm eşitsizliği',z='zor',alt='Ortak Kökler',kaz='İşaret tablosu verilen iki polinomun bölümünün işaretini bulup ortak sıfır ve payda sıfırı değerlerini doğru işleyerek f(x)/g(x) ≥ 0 çözümünü yazar.',kalip='tablo',
 kart='K-AESZ-03 (ortak kök, işaret tablosu) · ortak sıfır x = 2; payda sıfır noktaları',
 metin='Aşağıdaki tablo, f ve g polinomlarının x’in farklı aralıklarındaki işaretlerini göstermektedir; bir polinomun sıfır olduğu x değerleri 0 ile işaretlenmiştir.\nBu bilgilere göre f(x)/g(x) kesri sıfıra eşit ya da pozitif olduğunda x’in içinde bulunduğu küme aşağıdakilerden hangisidir?',
 dogru=dog,yan=[(w[0],'x = 2’nin hem payı hem paydayı sıfır yaptığını görüp sadeleştirmiş; ancak sadeleşen çarpan için x = 2 yine tanımsızdır, çözüme girmemelidir.','bilgi'),(w[1],'Bölümün pozitif olduğu aralıkları doğru bulmuş, ancak “≥” gereği payı sıfır yapan x = −3’ü çözüme katmamış.','dikkat'),(w[2],'Bölüm yerine çarpımı incelemiş; paydayı sıfır yapan x = −1 ve x = 2 değerlerini de çözüme katmış.','bilgi'),(w[3],'Bölümün negatif olduğu bölgeyi (kökler dahil) çözüm sanmış.','islem')],
 sira=place(dog,w,'E'),istenen='f(x)/g(x) ≥ 0 eşitsizliğinin çözüm kümesi.',ip=['Hem payın hem paydanın sıfır olduğu noktaların bölümde ne anlama geldiğini ayrı ayrı düşün.'],bilgi=[TAB],sekil=SK,
 ad=[A('Bölümün işaretini bul','Her aralıkta f ve g’nin işaretleri bölünür.','(−∞, −3): + · (−3, −1): − · (−1, 2): + · (2, ∞): +'),A('Sıfır noktalarını yorumla','Pay sıfırsa bölüm 0’dır, payda sıfırsa bölüm tanımsızdır.','x = −3 → 0 (olur) · x = −1, 2 → tanımsız'),A('Çözümü yaz','Bölüm pozitif olan aralıklar ve bölümün 0 olduğu −3 alınır; −1 ve 2 çıkarılır.','(−∞, −3] ∪ (−1, 2) ∪ (2, ∞)')],
 puf='Bölümde payda sıfırı olan noktalar, pay da sıfır olsa bile çözüme girmez.')

# 18 · rasyonel, çift kök
pay=lambda x:x*x-2*x-3; pyd=lambda x:x*x-4*x+4
dog=S(lambda x:pay(x)/pyd(x)<=0,[-1,2,3]); assert dog=='[−1, 2) ∪ (2, 3]'
w=[S(lambda x:pay(x)<=0,[-1,2,3]),S(lambda x:pay(x)/pyd(x)<0,[-1,2,3]),S(lambda x:pyd(x)!=0 and pay(x)/pyd(x)>=0,[-1,2,3]),S(lambda x:(x+1)*(x-3)/(x-2)<=0,[-1,2,3])]
assert w==['[−1, 3]','(−1, 2) ∪ (2, 3)','(−∞, −1] ∪ [3, ∞)','(−∞, −1] ∪ (2, 3]'],w
assert len({dog,*w})==5
q('0018',tipId='esz-bolum',tip='Bölüm eşitsizliği',z='orta',alt='Çift Katlı Payda',kaz='Paydası tam kare olan rasyonel eşitsizlikte çift katlı kökün işaret değiştirmediğini ve tanımsız değerin çözüme girmediğini kullanarak çözüm kümesini yazar.',kalip='düz',
 kart='K-AESZ-03 (çift katlı payda) · (x² − 2x − 3)/(x² − 4x + 4) ≤ 0',
 metin='Bir x gerçel sayısı için (x² − 2x − 3)/(x² − 4x + 4) ≤ 0 olduğu biliniyor.\nBuna göre x en genel hâliyle hangi aralıklarda bulunur?',
 dogru=dog,yan=[(w[0],'Paydanın tam kare olduğundan pozitif olduğunu düşünüp yalnız payı çözmüş; paydayı sıfır yapan x = 2 değerini dışarıda bırakmamış.','dikkat'),(w[1],'Payı sıfır yapan −1 ve 3 değerlerini “≤” olmasına rağmen çözüme katmamış.','dikkat'),(w[2],'Kesrin “≥ 0” bölgesini yazmış; yön hatası yapmış.','islem'),(w[3],'Paydadaki (x − 2)² çarpanını tek katlı kök gibi işleyip x = 2’de işaret değiştirmiş.','bilgi')],
 sira=place(dog,w,'B'),istenen='Eşitsizliğin çözüm kümesi.',ip=['Pay ve paydayı çarpanlarına ayır; çift katlı kökte işaretin değişip değişmediğini ayrı düşün.'],bilgi=[TAB],
 ad=[A('Çarpanlara ayır','Pay ve payda çarpanlarına ayrılır.','(x − 3)(x + 1) / (x − 2)² ≤ 0'),A('Paydayı değerlendir','(x − 2)² her zaman 0 veya pozitiftir; x = 2 dışında pozitiftir ve x = 2 tanımsızdır.','x ≠ 2 ve (x − 2)² > 0'),A('Payın işaretine bak','Bölümün ≤ 0 olması için pay ≤ 0 olmalı.','(x − 3)(x + 1) ≤ 0 → −1 ≤ x ≤ 3'),A('x = 2’yi çıkar','Payda sıfırı olan değer çözümden çıkarılır.','[−1, 2) ∪ (2, 3]')],
 puf='Paydası tam kare olan kesirde işaret yalnız paya bağlıdır; paydanın sıfır olduğu nokta çözümden çıkarılır.')

# 19 · öncüllü, parabol a,b,c
f19=lambda x:-(x+2)*(x-4)
for a in (-1,-2,Fi(-1,2),-3):
    b=-2*a; c=-8*a
    assert a<0 and b>0 and c>0 and a*b*c<0 and a+b+c>0 and 4*a+2*b+c>0
assert -1*2*8<0 and -1+2+8>0 and -4+4+8>0
sir=['Yalnız II','I ve II','I ve III','II ve III','I, II ve III']
sx,sy=0.5,0.23
cc=[axes(-3,5,-2,10,sx,sy,yt=[]),curve(f19,-2.15,4.15,sx,sy,-0.3,10,'blue!70!black'),'\\node[text=blue!70!black,font=\\small] at (4.55*0.5+0.1,0.4) {};']
SK=fig('\n'.join(cc))
q('0019',tipId='esz-katsayi',tip='Çözüm kümesinden katsayı bulma',z='zor',alt='Parabolde Katsayı İşaretleri',kaz='Grafiği verilen y = ax² + bx + c parabolünde katsayıların işaretlerini ve x = 1, x = 2 noktalarındaki değerlerin işaretlerini yorumlar.',kalip='öncüllü',
 kart='K-AESZ-05 (grafikten katsayı işareti) · kökler −2 ve 4, kollar aşağı; II ve III doğru',
 metin='Şekilde, y = ax² + bx + c parabolünün grafiği verilmiştir; parabol x eksenini ızgara çizgilerinin kesiştiği noktalarda kesmektedir.\nBuna göre,\nI. a · b · c > 0\nII. a + b + c > 0\nIII. 4a + 2b + c > 0\nifadelerinden hangileri doğrudur?',
 dogru='II ve III',yan=[('Yalnız II','III’ü incelerken x = 2’de grafiğin eksenin altında olduğunu sanmış; oysa x = 2 köklerin arasındadır ve f(2) > 0’dır.','dikkat'),('I ve II','Tepe noktası sağda olduğundan b’yi negatif sanmış; a · b · c > 0 bulmuş. III’ü de yanlış bulmuş.','bilgi'),('I ve III','a + b + c’nin f(1) olduğunu fark etmeyip II’yi yanlış saymış; b’yi negatif sanarak I’i doğru bulmuş.','bilgi'),('I, II ve III','b’nin işaretini yanlış belirleyip a · b · c > 0 bulmuş; II ve III’ü doğru bulmuş.','bilgi')],
 sira=sir,istenen='Doğru olan ifadeler.',ip=['II ve III’teki ifadeleri grafikteki bir büyüklüğe bağlayabilir misin?'],bilgi=[ABC,GRF],sekil=SK,
 ad=[A('a, b ve c’yi yorumla','Kollar aşağıda: a < 0. Tepe x = 1 > 0 olduğundan b > 0. Parabol y eksenini pozitif yerde kesiyor: c > 0.','a < 0, b > 0, c > 0'),A('I’i değerlendir','Bir negatif, iki pozitif sayının çarpımı negatiftir.','a × b × c < 0 → I yanlış'),A('II’yi değerlendir','a + b + c, f(1) değeridir; x = 1 köklerin arasındadır.','f(1) > 0 → II doğru'),A('III’ü değerlendir','4a + 2b + c, f(2) değeridir; x = 2 de köklerin arasındadır.','f(2) > 0 → III doğru')],
 puf='ax² + bx + c ifadesinde x yerine k yazınca bulunan sayı f(k)’dır; grafikte k noktasındaki yüksekliğin işaretine bak.')

# 20 · parabol grafiği, her x için f(x) ≥ m² − 5m
f20=lambda x:x*x-4*x
assert f20(1)==-3 and f20(0)==0 and f20(4)==0 and min(f20(Fi(k,4)) for k in range(-40,80))==-4
okm=[m for m in range(-30,31) if all(f20(Fi(k,4))>=m*m-5*m for k in range(-100,140))]
dog=sum(okm); assert okm==[1,2,3,4] and dog==10
e=[sum(m for m in range(-30,31) if -4>m*m-5*m),len(okm),sum(m for m in range(-30,31) if 4>=m*m-5*m),sum(m for m in okm if m!=4)]
assert e==[5,4,15,6] and len({dog,*e})==5
sx,sy=0.55,0.4
cc=[axes(-1,5,-5,4,sx,sy,yt=[]),curve(f20,-0.3,4.7,sx,sy,-5,4.2,'blue!70!black'),f'\\fill[blue!70!black] ({1*sx},{-3*sy}) circle (0.07);',f'\\node[font=\\footnotesize,above right=1pt] at ({1*sx},{-3*sy}) {{$(1,-3)$}};','\\node[text=blue!70!black,font=\\small] at (4.7*0.55+0.3,3.9*0.4) {$f$};']
SK=fig('\n'.join(cc))
q('0020',tipId='esz-parametre',tip='Parametreli eşitsizlik',z='orta',alt='Grafik ve İkinci Dereceli Parametre',kaz='Grafiği verilen parabolün kuralını belirleyip f(x) ≥ m² − 5m eşitsizliğinin her x için sağlanması koşulundan m’nin tam sayı değerlerini bulur.',kalip='grafik',
 kart='K-AESZ-09 (grafikten kural, ikinci dereceli parametre) · f(x) = x² − 4x; f(x) ≥ m² − 5m her x için',
 metin='Şekilde, y = f(x) parabolünün grafiği verilmiştir; grafik, x eksenini ızgara çizgilerinin kesiştiği noktalarda kesmektedir ve işaretli noktadan geçmektedir.\nm bir tam sayı olmak üzere, f(x) ≥ m² − 5m eşitsizliği her x gerçel sayısı için sağlanıyor.\nBuna göre m’nin alabileceği değerlerin toplamı kaçtır?',
 dogru=dog,yan=[(e[0],'Eşitsizliği “>” gibi alıp −4 > m² − 5m çözmüş; m = 1 ve m = 4 uç değerlerini dışarıda bırakmış: 2 + 3.','dikkat'),(e[1],'Değerlerin toplamı yerine kaç değer olduğunu yazmış.','dikkat'),(e[2],'Sabit terimi kullanırken işaret hatası yapıp en küçük değeri −4 yerine 4 almış: m² − 5m ≤ 4 için 0 ≤ m ≤ 5 tam sayılarını toplamış.','islem'),(e[3],'Köklerden yalnız birini uç değer sanıp m = 4’ü dışarıda bırakmış: 1 + 2 + 3.','dikkat')],
 istenen='m’nin alabileceği tam sayı değerlerinin toplamı.',ip=['“Her x için” ifadesi, parabolün aldığı değerlerin hangisiyle ilgilidir?'],bilgi=[DEL,KOK],sekil=SK,
 ad=[A('Kuralı bul','Kökler 0 ve 4; f(x) = a·x(x − 4). (1, −3) noktası a’yı verir.','a × 1 × (−3) = −3 → a = 1 → f(x) = x² − 4x'),A('Koşulu f’nin değerine çevir','f’nin alabildiği en küçük değer, tepe noktasındadır (köklerin ortası).','x = 2 → f(2) = −4'),A('Parametre eşitsizliğini kur','Her x için sağlanması, bu en küçük değerin de sağlaması demektir.','−4 ≥ m² − 5m → m² − 5m + 4 ≤ 0'),A('Çöz ve topla','(m − 1)(m − 4) ≤ 0 → 1 ≤ m ≤ 4; tam sayılar toplanır.','1 + 2 + 3 + 4 = 10')],
 puf='Parametreli “her x için” koşulunu önce fonksiyonun değerlerine dair bir kısıta çevir, sonra parametre eşitsizliğini çöz.')

# ---------- bitir ----------
from collections import Counter
for qq in P.ANA: qq['kardes']=None
assert len(P.ANA)==20
json.dump(P.ANA,open(os.path.join(HD:=os.path.dirname(os.path.abspath(__file__)),'esitsiz-1.json'),'w'),ensure_ascii=False,indent=1)
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=UK))['kartlar'].append(c['id'])
json.dump(dict(konu='Eşitsizlikler',surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2025 AYT Matematik çıkmış soruları ve yayın soru bankaları (yalnız mantık), MEB 10–12. sınıf müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),open(os.path.join(HD,'..','kartlar','esitsiz.json'),'w'),ensure_ascii=False,indent=1)
print('harf',sorted(Counter(x['cevap']['sik'] for x in P.ANA).items()),'zorluk',dict(Counter(x['zorluk'] for x in P.ANA)),'tip',len(tipler),'şekilli',sum(1 for x in P.ANA if x['sekil']),'öncüllü',sum(1 for x in P.ANA if x['kalip']=='öncüllü'))
