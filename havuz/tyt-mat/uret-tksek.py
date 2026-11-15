"""Temel Kavramlar · ŞEKİLLİ paket (tksek): 13 soru, hepsi şekilli/tablolu, kardeş yok, ipucu 1.
Şekil çözüm için gereken veriyi taşır. Her cevap ve çeldirici değeri Python'da hesaplanıp assert edilir."""
import sys,os,itertools
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_mat as H
from _hafif_mat import *
from _sekil_sayi import *
H.KONU='Temel Kavramlar'
P=Parti('tksek','Temel Kavramlar','mat|Temel Kavramlar')
UK='mat|Temel Kavramlar'
F=factorial
KY='ÖSYM 2018–2026 TYT Matematik (temel kavramlar, şekilli/tablolu sorular; yalnız mantık) · MEB 9. sınıf'
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,kaynak=None):
    kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,kaynak or KY)
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)

TAK=B('Takvimde sütun ve hafta','takvimde aynı sütundaki günler aynı haftanın gününe aittir ve 7 gün arayla dizilir. Örnek: 3 Pazartesi ise 10, 17, 24, 31 de Pazartesidir')
TERS=B('Ters işlem','bir sayıya işlemler sırayla uygulanmışsa girişi bulmak için sondan başlanır ve her işlemin tersi uygulanır (+ ↔ −, × ↔ ÷). Örnek: 3 ile çarpıp 2 ekleyince 11 ise, 11 − 2 = 9 ve 9 ÷ 3 = 3’tür')
CET=B('Cetvel okuma','1 cm = 10 mm’dir. Bir santimetre 5 eşit bölmeye ayrılmışsa bir bölme 2 mm’dir. Bir cismin uzunluğu, iki ucun okunan değerlerinin farkıdır. Örnek: 5 cm’den sonraki 3. bölme 5 cm 6 mm’dir')
SD=B('Sayı doğrusunda eşit aralık','ardışık iki nokta arası eşitse, iki noktanın değer farkı aradaki aralık sayısına bölünerek bir aralığın değeri bulunur. Örnek: 2 ile 14 arasında 3 aralık varsa bir aralık 4’tür; sağa gidildikçe sayılar artar')
SIH=B('Sihirli kare','her satırdaki, her sütundaki ve iki köşegendeki sayıların toplamı birbirine eşittir. Örnek: 2, 7, 6 sayıları bir satırdaysa toplam 15’tir, aynı toplam her sütun ve köşegende de aranır')
PIR=B('Sayı piramidi','her kutudaki sayı, hemen altındaki iki kutudaki sayının toplamıdır. Örnek: altında 3 ve 5 olan kutuda 8 yazar; bilinmeyen için kutular yukarı doğru toplam olarak yazılır')
TEK=B('Tek-çift kuralları','tek + tek = çift · çift + çift = çift · tek + çift = tek. Çarpımda çarpanlardan biri çiftse çarpım çifttir; hepsi tekse çarpım tektir. Örnek: 3 × 4 = 12 çift, 3 × 5 = 15 tek')
ARD=B('Ardışık tek sayılar','ikişer artarlar: x, x + 2, x + 4, … (x tek). Ardışık beş tek sayının toplamı, ortadaki sayının 5 katıdır. Örnek: 7 + 9 + 11 + 13 + 15 = 55 = 5 × 11')
FAK=B('Faktöriyel','n! = 1 × 2 × … × n. Örnek: 4! = 24. Ayrıca 7! = 7 × 6 × 5! yazılabilir. Çarpma ve bölme toplama ve çıkarmadan önce yapılır')
AKS=B('Akış şeması','okla gösterilen yönde ilerlenir; eşkenar dörtgen (karar) kutusunda sorunun cevabına göre “Evet” ya da “Hayır” okuna gidilir. Örnek: “n çift mi?” sorusunda n = 6 ise “Evet” okuna gidilir')
PER=B('Dönüşte yinelenme','bir kural sürekli uygulanınca bir süre sonra aynı konum tekrarlanıyorsa dizi yinelenir; yinelenen bölümün uzunluğu (periyot) bulunur ve gerisi periyoda bölünerek kalana bakılır. Örnek: ilk 2 adım yinelenmiyor, sonra 3 adımda bir yineleniyorsa 20. adım için (20 − 2) ÷ 3 işleminin kalanına bakılır')
ISL=B('İşlem önceliği','önce çarpma ve bölme (soldan sağa), sonra toplama ve çıkarma (soldan sağa) yapılır. Örnek: 5 − 2 + 8 ÷ 4 × 3 = 5 − 2 + 6 = 9')
SIC=B('Sayı doğrusunda ileri-geri hareket','sağa gitmek toplama, sola gitmek çıkarma demektir; toplam yer değiştirme = (sağa gidilen toplam) − (sola gidilen toplam). Örnek: 3 kez 5 sağa ve 2 kez 4 sola gidince 15 − 8 = 7 birim sağa gidilir')

# ---------- kartlar ----------
kartla('K-TKS-01','Takvim yaprağı','Takvimde ilk günün sütunundan haftanın günü belirlenir; aynı gün 7 gün arayla tekrarlanır ve ay uzunluğuna sığan en büyük tarih alınır.','1’in düştüğü sütunu bir kayık okumak; ayın son gününü son cumartesi sanmak.','kolay','şekilli',3,'tks-takvim','Takvim yaprağında haftanın günü ve tarih')
kartla('K-TKS-02','İşlem makinesi','Çıkıştan girişe sondan başlayıp her işlemin tersi uygulanır.','İşlemlerin tersini yanlış sırayla ya da aynı işaretle uygulamak.','kolay','şekilli',3,'tks-makine','İşlem makinesinde ters işlem')
kartla('K-TKS-03','Cetvel okuma','Cetvelin bölme değeri bulunur, iki ucun değeri okunup fark milimetreye çevrilir.','Bölmeyi 1 mm sanmak; yalnız tam santimetreyi okumak; küçük bölmeleri ters yönde saymak.','kolay','şekilli',3,'tks-cetvel','Cetvelle uzunluk okuma ve birim çevirme')
kartla('K-TKS-04','Sayı doğrusunda eşit aralık','İki bilinen noktadan bir aralığın değeri bulunur; sola ve sağa doğru sayılarak istenen noktalar yazılır.','Aralık sayısını nokta sayısıyla karıştırmak; negatif sayıların işaretini düşürmek.','orta','şekilli',4,'tks-dogru','Sayı doğrusunda eşit aralıklı noktalar')
kartla('K-TKS-05','Sihirli kare','Bir köşegen ya da satırdan ortak toplam bulunur, bilinmeyenler satır, sütun ve köşegenlerden sırayla çözülür.','Ortak toplamı yanlış satırdan bulmak; bir kareyi yalnız satır toplamıyla bırakıp köşegeni unutmak.','orta','şekilli',3,'tks-sihirli','Sihirli karede bilinmeyen sayı')
kartla('K-TKS-06','Sayı piramidi','Alt kutulardan üst kutuya toplam katsayıları (1, 3, 3, 1) çıkarılır ve bilinmeyen denklemle bulunur.','Üst kutuyu yalnız alt sıranın toplamı sanmak; orta kutuların katsayısını yanlış almak.','orta','şekilli',3,'tks-piramit','Sayı piramidinde bilinmeyen kutu')
kartla('K-TKS-07','Tek-çift tablosu','Tablodaki sonuçlardan a, b, c’nin tek–çift durumu bulunur; öncüller bu duruma göre denetlenir.','Bir satırı denetlemeden varsayım yapmak; çarpımda “bir çarpan çiftse çarpım çift”i unutmak.','orta','tablo',4,'tks-tekcift','Tablodaki tek-çift öncüllerle sayı durumunu bulma')
kartla('K-TKS-08','Ardışık tek sayılar şeması','Kutulara yazılan ardışık sayılar x, x + 2, … biçiminde yazılır; parantezle verilen toplamdan x bulunur.','Ardışık tek sayılarda fark 1 almak; parantezin hangi kutuları kapsadığını yanlış okumak.','orta','şekilli',3,'tks-ardisik','Ardışık tek sayılar şemasında toplam')
kartla('K-TKS-09','İşlem ağacı','Alt kutulardaki değerlerden üst kutular yukarı doğru işlenir; faktöriyel kısaltması ve işlem önceliği kullanılır.','9!/7! için (9 − 7)! yazmak; önceliği bozup soldan sağa yapmak.','orta','şekilli',4,'tks-agac','Faktöriyel içeren işlem ağacı')
kartla('K-TKS-10','Akış şeması','Akış şeması adım adım çalıştırılır, adım sayısı her başlangıç değeri için hesaplanır ve istenen koşulu sağlayanlar sayılır.','Kural değişikliği (n − 1 gibi) ya da sayacı yanlış başlatmak; karar kutusunda yönü karıştırmak.','zor','şekilli',5,'tks-akis','Akış şemasında adım sayısına göre sayma')
kartla('K-TKS-11','Sayı çarkı','Okun yolu simüle edilir, yinelenen bölüm (periyot) ve başlangıçtaki yinelenmeyen kısım bulunur; kalanla bölme belirlenir.','Yinelenmeyen kısmı atlamak; adım sayısında bir fazla ya da eksik almak.','zor','şekilli',5,'tks-cark','Sayı çarkında tekrar eden hareket')
kartla('K-TKS-12','İşlem işaretleri kutuları','Birinci satırdan işaretlerin sırası işlem önceliği ve deneme-yanılmayla bulunur, ikinci satıra uygulanır.','İşlem önceliğini gözetmeden soldan sağa hesaplamak; işaretleri farklı sırada denemek.','zor','şekilli',5,'tks-isaret','Kutulara işlem işareti yerleştirme')
kartla('K-TKS-13','Sayı doğrusunda ileri-geri sayma','İki nokta arasındaki uzaklık sayı doğrusundan okunur; sağa ve sola sıçrayış sayıları denklemle bulunur.','Sağ ile sol sıçrayış sayısını karıştırmak; her sıçrayış net ilerleme sanmak.','orta','şekilli',4,'tks-sicrama','Sayı doğrusunda ileri-geri sıçrayış')

# =============== 01 · takvim · kolay ===============
gun=['Pzt','Sal','Çar','Per','Cum','Cmt','Paz']
bas=2  # ayın 1'i Çarşamba (sütun 2)
n_gun=30
cmt=[d for d in range(1,n_gun+1) if (d-1+bas)%7==5]; assert cmt==[4,11,18,25] and max(cmt)==25
assert [d for d in range(1,n_gun+1) if (d-1+bas+1)%7==5][-1]==24   # 1'i Perşembe sanırsa (sütun kayması)
assert [d for d in range(1,n_gun+1) if (d-1+bas-2)%7==5][-1]==27   # 1'i Pazartesi sanırsa
assert [d for d in range(1,n_gun+1) if (d-1+bas)%7==6][-1]==26 and 4+7*4==32>n_gun
cw,chh=.95,.6; o=[]
for j,g in enumerate(gun):
    o.append(nd(j*cw,0,g,cw,chh,fill='vurgu!25' if False else 'black!8',bold=True))
d=1
for r in range(2):
    for j in range(7):
        if r==0 and j<bas: o.append(nd(j*cw,-(r+1)*chh,'',cw,chh)); continue
        o.append(nd(j*cw,-(r+1)*chh,str(d),cw,chh,fill='vurgu!12' if j>=5 else None)); d+=1
assert d==13
for j in range(7): o.append(tx(j*cw,-3*chh+.05,'$\\vdots$'))
SK1=tz('\n'.join(o))
q('0001',tipId='tks-takvim',tip='Takvim yaprağında haftanın günü ve tarih',z='kolay',alt='Takvim ve Haftanın Günleri',kaz='Takvim yaprağından ayın birinci gününün haftadaki yerini okuyup aynı günün tarihlerini 7’şer artırarak son tarihi bulur.',kalip='şekilli',sekil=SK1,
 kart='K-TKS-01 (takvim yaprağı) · 1’i Çarşamba olan 30 günlük ayın son cumartesisi',
 metin='Aşağıda bir ayın takvim yaprağının ilk iki haftası verilmiştir. Bu ay 30 gün çekmektedir.\nBuna göre bu ayın son cumartesi günü ayın kaçıncı günüdür?',
 dogru=25,yan=[(24,'Ayın 1’ini Perşembe sanmış (sütunu bir kaydırmış); bu durumda cumartesiler 3, 10, 17, 24 olurdu.','dikkat'),(26,'Cumartesi yerine Pazar sütununu (5, 12, 19, 26) okumuş.','dikkat'),(27,'Ayın 1’ini Pazartesi sanıp cumartesileri 6, 13, 20, 27 bulmuş.','dikkat'),(30,'Ayın son günü olan 30’u, son cumartesi sanmış; 30 hangi günse yalnız onu düşünmüş.','dikkat')],
 istenen='Son cumartesinin tarihi.',
 ip=['İlk cumartesinin hangi tarihe denk geldiğini bul; sonrakiler aynı sütunda 7 gün arayla gelir.'],
 bilgi=[TAK],
 ad=[A('İlk cumartesiyi oku','Takvimde 1 Çarşamba sütunundadır; Cumartesi sütunundaki ilk tarih 4’tür.','Çarşamba 1 → Perşembe 2 → Cuma 3 → Cumartesi 4'),A('7’şer artır','Cumartesiler aynı sütunda 7 gün arayla gelir.','4, 11, 18, 25, 32, …'),A('Ay uzunluğuyla sınırla','Ay 30 gün çektiği için 32 yoktur; en büyük tarih 25’tir.','25 ≤ 30 < 32')],
 puf='Takvimde bir günün tarihleri 7 artarak ilerler; son tarihi bulmak için ay uzunluğunu aşmayan en büyük terimi al.')

# =============== 02 · işlem makinesi · kolay ===============
gir=7; assert (gir*4+6)//2==17 and (gir*4+6)%2==0
assert 17*2-6==28 and 17*2==34 and (17*2+6)//4==10 and (17*4+6)//2==37 and 4*10+6==46
o=[]; x=0
o.append(nd(0,0,'Giriş',1.35,.8,fill='black!8'))
ops=[('$\\times 4$',2.3),('$+\\,6$',3.9),('$\\div 2$',5.5)]
for t,xx in ops:
    o.append(nd(xx,0,t,1.15,.8,fill='vurgu!15'))
o.append(nd(7.2,0,'17',1.2,.8,fill='black!8',bold=True))
o.append('\\draw[-{Stealth[length=2mm]}] (.7,0) -- (1.7,0);')
for a_,b_ in [(2.9,3.3),(4.5,4.9),(6.1,6.6)]: o.append(f'\\draw[-{{Stealth[length=2mm]}}] ({a_},0) -- ({b_},0);')
o.append(tx(7.2,.72,'Çıkış'))
SK2=tz('\n'.join(o))
q('0002',tipId='tks-makine',tip='İşlem makinesinde ters işlem',z='kolay',alt='İşlem Makinesi',kaz='Ardışık işlemlerden geçen bir sayının girişini, çıkıştan başlayıp işlemlerin tersini uygulayarak bulur.',kalip='şekilli',sekil=SK2,
 kart='K-TKS-02 (işlem makinesi) · ×4, +6, ÷2 makinesinde çıkış 17',
 metin='Aşağıdaki işlem makinesinde giriş sayısı, oklar yönünde kutulardaki işlemlerden sırayla geçer.\nÇıkışta 17 elde edildiğine göre girişe hangi sayı verilmiştir?',
 dogru=7,yan=[(10,'İşlemlerin tersini alırken “+ 6” adımında toplamayı sürdürmüş: (34 + 6) ÷ 4 = 10.','islem'),(28,'Yalnız “÷ 2” ve “+ 6” adımlarını geri almış (34 − 6 = 28); “× 4” adımını geri almayı unutmuş.','dikkat'),(34,'Yalnız “÷ 2” adımını geri almış (17 × 2 = 34), diğer iki işlemi uygulamamış.','dikkat'),(37,'İşlemleri çıkışa ileri yönde uygulamış: (17 × 4 + 6) ÷ 2 = 37.','bilgi')],
 istenen='Makineye verilen giriş sayısı.',
 ip=['Sondan başla: son işlemden önceki sayıyı bul, sonra bir önceki işleme geç.'],
 bilgi=[TERS],
 ad=[A('Son işlemi geri al','“÷ 2” işleminin tersi “× 2” dir.','17 × 2 = 34'),A('İkinci işlemi geri al','“+ 6” işleminin tersi “− 6” dır.','34 − 6 = 28'),A('İlk işlemi geri al','“× 4” işleminin tersi “÷ 4” tür.','28 ÷ 4 = 7')],
 puf='Makine sorularında çıkıştan girişe doğru, her işlemin tersini ters sırayla uygula; sonunda girişten ileri doğru kontrol et: 7 × 4 = 28, 28 + 6 = 34, 34 ÷ 2 = 17.')

# =============== 03 · cetvel · kolay ===============
s=1.15; c0=12
sol_cm,sol_b=12,3; sag_cm,sag_b=17,2
assert (sag_cm*10+sag_b*2)-(sol_cm*10+sol_b*2)==48
assert (sag_cm*10+sag_b)-(sol_cm*10+sol_b)==49 and (sag_cm-sol_cm)*10==50 and 50+(sol_b-sag_b)*2==52 and (sag_cm*10+sag_b*5)-(sol_cm*10+sol_b*5)==45
assert 174-122==52
X=lambda cm,b=0:(cm-c0+b*.2)*s
o=[f'\\draw[fill=black!4,line width=1pt] (-.4,0) rectangle ({6*s+.4},-1.3);']
for cm in range(c0,c0+7):
    o.append(ln(X(cm),0,X(cm),-.55,'line width=1.3pt')); o.append(tx(X(cm),-.95,f'\\large {cm}'))
    if cm<c0+6:
        for b in range(1,5): o.append(ln(X(cm,b),0,X(cm,b),-.3,'line width=.9pt'))
o.append(f'\\draw[fill=vurgu!20,line width=1pt] ({X(sol_cm,sol_b):.3f},.0) rectangle ({X(sag_cm,sag_b):.3f},.7);')
o.append(ln(X(sol_cm,sol_b),0,X(sol_cm,sol_b),-1.3,'dashed,line width=.5pt'))
o.append(ln(X(sag_cm,sag_b),0,X(sag_cm,sag_b),-1.3,'dashed,line width=.5pt'))
o.append(tx(6*s+.85,-.95,'cm'))
SK3=tz('\n'.join(o))
q('0003',tipId='tks-cetvel',tip='Cetvelle uzunluk okuma ve birim çevirme',z='kolay',alt='Cetvel ve Ölçek Okuma',kaz='Bölmeli bir cetvelde cismin iki ucunu okuyup uzunluğunu milimetre cinsinden hesaplar.',kalip='şekilli',sekil=SK3,
 kart='K-TKS-03 (cetvel okuma) · 5 eşit bölmeli cetvelde 12,6 cm ile 17,4 cm arası',
 metin='Aşağıdaki cetvelde her bir santimetre 5 eşit bölmeye ayrılmıştır. Cetvelin üzerine bir çubuk konulmuştur.\nBuna göre çubuğun uzunluğu kaç milimetredir?',
 dogru=48,yan=[(49,'Küçük bölmeleri 1 mm sanmış: 17 cm 2 mm − 12 cm 3 mm = 172 − 123 = 49 mm.','bilgi'),(50,'Yalnız tam santimetreleri okumuş: 17 − 12 = 5 cm = 50 mm; bölmeleri hesaba katmamış.','dikkat'),(52,'Sol ucu 12 cm’den sonraki 1. bölmede (122 mm) okumuş: 174 − 122 = 52 mm.','dikkat'),(45,'Bir bölmeyi 5 mm sanmış: 17 cm 10 mm − 12 cm 15 mm = 180 − 135 = 45 mm.','bilgi')],
 istenen='Çubuğun uzunluğu (mm).',
 ip=['Bir küçük bölmenin kaç milimetre olduğunu bul, sonra çubuğun sol ve sağ uçlarının okunduğu değerleri yaz.'],
 bilgi=[CET],
 ad=[A('Bölme değerini bul','1 cm = 10 mm ve bir santimetre 5 eşit bölmeye ayrıldığı için bir bölme 2 mm’dir.','10 mm ÷ 5 = 2 mm'),A('İki ucu oku','Sol uç 12 cm’den sonraki 3. bölmededir; sağ uç 17 cm’den sonraki 2. bölmededir.','sol = 120 + 3 × 2 = 126 mm · sağ = 170 + 2 × 2 = 174 mm'),A('Farkı al','Uzunluk, iki ucun okunan değerlerinin farkıdır.','174 − 126 = 48 mm')],
 puf='Cetvelde önce bir küçük bölmenin değerini bul, sonra her ucu aynı birimde (mm) yazıp çıkar.')

# =============== 04 · sayı doğrusu eşit aralık · orta ===============
isim='KLMNPRS'; Lv,Rv=-7,13
il,ir=isim.index('L'),isim.index('R'); aral=(Rv-Lv)//(ir-il); assert aral==5 and (Rv-Lv)==aral*(ir-il)
val={c:Lv+(i-il)*aral for i,c in enumerate(isim)}
assert val['K']==-12 and val['N']==3 and val['S']==18 and val['K']+val['N']+val['S']==9 and val['R']==13
a4=(Rv-Lv)//(ir-il+1); assert a4==4
e1=(Lv-a4)+(Lv+2*a4)+(Rv+a4); assert e1==7
e2=abs(val['K'])+val['N']+val['S']; assert e2==33
e3=val['K']+val['N']+(val['R']+2*aral); assert e3==14 and val['R']+2*aral==23
e4=(Lv-2*aral)+val['N']+val['S']; assert e4==4 and Lv-2*aral==-17
xs=[.3+i*1.05 for i in range(7)]
o=[ln(0,0,7.35,0,'line width=1pt,-{Stealth[length=2.2mm]}')]
for i,c in enumerate(isim):
    o.append(f'\\fill ({xs[i]:.3f},0) circle (.07);'); o.append(ln(xs[i],-.1,xs[i],.1)); o.append(tx(xs[i],-.4,c,'font=\\normalsize\\bfseries'))
o.append(tx(xs[il],.45,'$-7$')); o.append(tx(xs[ir],.45,'$13$'))
SK4=tz('\n'.join(o))
q('0004',tipId='tks-dogru',tip='Sayı doğrusunda eşit aralıklı noktalar',z='orta',alt='Sayı Doğrusu',kaz='Sayı doğrusunda eşit aralıklı noktalardan bir aralığın değerini bulup negatif ve pozitif değerli noktaların toplamını hesaplar.',kalip='şekilli',sekil=SK4,
 kart='K-TKS-04 (sayı doğrusu, eşit aralık) · L = −7, R = 13 verilip K, N, S toplamı',
 metin='Aşağıdaki sayı doğrusunda ardışık iki nokta arasındaki uzaklıklar birbirine eşittir. L noktası −7’yi, R noktası 13’ü göstermektedir.\nBuna göre K, N ve S noktalarının gösterdiği sayıların toplamı kaçtır?',
 dogru=9,yan=[(7,'L ile R arasında 5 nokta saydığı için 20 ÷ 5 = 4 almış (arada 4 aralık vardır, 20 ÷ 4 = 5): K = −11, N = 1, S = 17 → toplam 7.','bilgi'),(4,'K noktasını L’nin iki aralık soluna koyup −17 bulmuş: −17 + 3 + 18 = 4.','dikkat'),(14,'S noktasını R’nin iki aralık sağına koyup 23 bulmuş: −12 + 3 + 23 = 14.','dikkat'),(33,'K = −12 sayısının işaretini düşürüp 12 almış: 12 + 3 + 18 = 33.','dikkat')],
 istenen='K, N ve S noktalarına karşılık gelen sayıların toplamı.',
 ip=['L’den R’ye kaç aralık olduğunu say ve iki sayının farkını bu sayıya böl.'],
 bilgi=[SD],
 ad=[A('Aralık sayısını bul','L ile R arasında L–M, M–N, N–P, P–R olmak üzere 4 aralık vardır.','13 − (−7) = 20 → 20 ÷ 4 = 5'),A('Bir aralığın değerini yaz','Her aralık 5 birimdir; sağa gidildikçe sayı artar, sola gidildikçe azalır.','K = −7 − 5 = −12 · N = −7 + 2 × 5 = 3'),A('S noktasını bul','R’den bir aralık sağda S noktası vardır.','S = 13 + 5 = 18'),A('Topla','Üç değeri işaretleriyle topla.','−12 + 3 + 18 = 9')],
 puf='Sayı doğrusu sorularında önce aralık sayısını (nokta sayısının bir eksiği) bul; negatif değerlerin işaretini son toplamaya kadar koru.')

# =============== 05 · sihirli kare · orta ===============
M=[[13,6,11],[8,10,12],[9,14,7]]; S5=30
assert all(sum(r)==S5 for r in M) and all(sum(M[i][j] for i in range(3))==S5 for j in range(3)) and sum(M[i][i] for i in range(3))==S5 and sum(M[i][2-i] for i in range(3))==S5
assert M[0][2]+M[1][1]+M[2][0]==S5 and S5-M[0][0]-M[1][1]==M[2][2]==7 and S5-M[2][0]-M[2][2]==14==M[2][1]
assert S5-M[2][0]==21 and S5-M[2][0]-(S5-M[0][0])==4 and S5-M[2][0]-M[1][1]==11 and S5-M[0][1]==24
given={(0,0):'13',(0,2):'11',(1,1):'10',(2,0):'9',(2,1):'?'}
o=[]
for i in range(3):
    for j in range(3):
        t=given.get((i,j),'')
        o.append(nd(j*.95,-i*.95,t,.95,.95,fill='vurgu!20' if (i,j)==(2,1) else None,bold=(i,j)==(2,1)))
SK5=tz('\n'.join(o))
q('0005',tipId='tks-sihirli',tip='Sihirli karede bilinmeyen sayı',z='orta',alt='Sihirli Kare',kaz='Sihirli karede bir köşegenden ortak toplamı bulup satır ve köşegenlerden bilinmeyen kareyi hesaplar.',kalip='şekilli',sekil=SK5,
 kart='K-TKS-05 (sihirli kare) · ters köşegenden toplam 30, sorulan alt satırın ortası',
 metin='Aşağıdaki 3 × 3’lük karede her satırdaki, her sütundaki ve iki köşegendeki sayıların toplamı birbirine eşittir. Karenin bazı kutuları boş bırakılmıştır.\nBuna göre ? yerine hangi sayı gelmelidir?',
 dogru=14,yan=[(4,'Sağ alt kutuyu 30 − 13 = 17 bulmuş (köşegendeki ortadaki 10’u unutmuş); alt satırdan 30 − 9 − 17 = 4 yazmış.','dikkat'),(11,'Alt satırda ortadaki 10’u kullanmış: 30 − 9 − 10 = 11; oysa alt satırda ? ile birlikte 9 ve sağ alt kutu vardır.','dikkat'),(21,'Alt satırda yalnız 9’u çıkarmış: 30 − 9 = 21; sağ alt kutuyu hesaba katmamış.','dikkat'),(24,'Ortadaki sütunda 10’u unutup üst kutu 6’yı kullanmış: 30 − 6 = 24.','dikkat')],
 istenen='? yerine yazılması gereken sayı.',
 ip=['Köşegenlerden biri üç kutusu da dolu olacak biçimde seçilebilir; onunla ortak toplamı bul.'],
 bilgi=[SIH],
 ad=[A('Ortak toplamı bul','Sağ üstten sol alta uzanan köşegendeki üç sayı da bellidir.','11 + 10 + 9 = 30'),A('Sağ alt kutuyu bul','Sol üstten sağ alta köşegende 13 ve 10 vardır.','30 − 13 − 10 = 7'),A('Alt satırdan ? değerini bul','Alt satırda 9, ? ve 7 vardır, toplam 30 olmalıdır.','9 + ? + 7 = 30 → ? = 14')],
 puf='Sihirli karede ortak toplamı, üç kutusu da dolu olan bir satır, sütun ya da köşegenden bul; bilinmeyenleri sırayla bu toplama tamamla.')

# =============== 06 · piramit · orta ===============
a_,c_,d_=3,4,2; x_=8
b4=[a_,x_,c_,d_]; r3=[b4[i]+b4[i+1] for i in range(3)]; r2=[r3[i]+r3[i+1] for i in range(2)]; top=sum(r2)
assert top==41 and top==a_+3*x_+3*c_+d_
def bul(f): return [x for x in range(0,200) if f(x)]
assert bul(lambda x:a_+3*x+3*c_+d_==41)==[8]
assert bul(lambda x:3*x+a_+d_==41)==[12] and bul(lambda x:3*x+3*c_+d_==41)==[9]
assert bul(lambda x:a_+2*x+2*c_+d_==41)==[14] and bul(lambda x:a_+x+c_+d_==41)==[32]
o=[]; bw=1.0; bh=.7; gap=.08
for lev in range(4):
    nn=4-lev; y=lev*(bh+gap)
    for i in range(nn):
        xx=(i-(nn-1)/2)*(bw+gap)
        t=''; fill=None
        if lev==0: t=str(b4[i]) if i!=1 else '?'; fill='vurgu!20' if i==1 else None
        if lev==3: t='41'
        o.append(nd(xx,y,t,bw,bh,fill=fill,bold=bool(t)))
SK6=tz('\n'.join(o))
q('0006',tipId='tks-piramit',tip='Sayı piramidinde bilinmeyen kutu',z='orta',alt='Sayı Piramidi',kaz='Sayı piramidinde üst kutudaki toplamı alt kutuların katsayılı toplamı olarak yazıp bilinmeyen kutuyu bulur.',kalip='şekilli',sekil=SK6,
 kart='K-TKS-06 (sayı piramidi) · alt sıra 3, ?, 4, 2 ve tepe 41',
 metin='Aşağıdaki sayı piramidinde her kutudaki sayı, hemen altındaki iki kutudaki sayının toplamına eşittir. Kutuların bir kısmı boş bırakılmıştır.\nBuna göre ? yerine hangi sayı gelmelidir?',
 dogru=8,yan=[(9,'Alt sıradaki ilk kutuyu (3) hesaba katmamış: 3 × ? + 3 × 4 + 2 = 41 → ? = 9.','dikkat'),(12,'Üçüncü kutuyu (4) hesaba katmamış: 3 + 3 × ? + 2 = 41 → ? = 12.','dikkat'),(14,'Katsayıları 1, 2, 2, 1 almış: 3 + 2 × ? + 2 × 4 + 2 = 41 → ? = 14.','bilgi'),(32,'Tepeyi alt sıradaki dört sayının toplamı sanmış: 3 + ? + 4 + 2 = 41 → ? = 32.','bilgi')],
 istenen='? yerine yazılması gereken sayı.',
 ip=['Alt sıradaki ? kutusundan başlayarak yukarıdaki kutuları birer birer toplam olarak yaz; tepede ? cinsinden bir ifade çıkar.'],
 bilgi=[PIR],
 ad=[A('İkinci sırayı yaz','Alt sıra 3, ?, 4, 2’dir; komşu kutular toplanır.','3 + ? · ? + 4 · 6'),A('Üçüncü sırayı yaz','İkinci sıradaki komşu toplamlar alınır.','(3 + ?) + (? + 4) = 2 × ? + 7 · (? + 4) + 6 = ? + 10'),A('Tepeyi yaz','Üçüncü sıradaki iki kutu toplanır ve 41’e eşitlenir.','(2 × ? + 7) + (? + 10) = 3 × ? + 17'),A('? değerini bul','Denklemi çöz.','3 × ? + 17 = 41 → 3 × ? = 24 → ? = 8')],
 puf='Piramitte komşu kutular toplanarak yukarı çıkılır; her sırada kutu sayısı bir azalır ve ? içeren kutular ? cinsinden yazılır.')

# =============== 07 · tek-çift tablosu · orta ===============
TF=[('a + c','Tek',lambda a,b,c:(a+c)%2==1),('b × c','Çift',lambda a,b,c:(b*c)%2==0),('a × c + b','Tek',lambda a,b,c:(a*c+b)%2==1)]
ON=[lambda a,b,c:(a*b+c)%2==1,lambda a,b,c:(b+c)%2==0,lambda a,b,c:(a*c+b*c)%2==0]
asg=[t for t in itertools.product([0,1],repeat=3) if all(f(*t) for _,_,f in TF)]
assert asg==[(1,1,0)]
def kume(t): return tuple(i+1 for i,f in enumerate(ON) if f(*t))
assert kume((1,1,0))==(1,3)
SIRA7=['Yalnız I','Yalnız III','I ve II','I ve III','II ve III']; AD7={(1,):'Yalnız I',(3,):'Yalnız III',(1,2):'I ve II',(1,3):'I ve III',(2,3):'II ve III'}
def pn(t): return ', '.join(f'{h} {"tek" if v else "çift"}' for h,v in zip('abc',t))
def ihlal(t): return [i+1 for i,(_,_,f) in enumerate(TF) if not f(*t)]
yan7=[]
for t,hedef in [((1,0,1),(1,)),((0,1,0),(3,)),((0,1,1),(1,2)),((1,0,0),(2,3))]:
    assert kume(t)==hedef and len(ihlal(t))==1
    sat=['a + c','b × c','a × c + b'][ihlal(t)[0]-1]
    yan7.append((AD7[hedef],f'a, b, c için ({pn(t)}) durumunu almış; bu durum tablodaki “{sat}” satırıyla çelişir. Bu varsayımla “{AD7[hedef]}” bulunur.','dikkat'))
SK7=tablo_svg(['İşlem','Sonuç'],[[a,b] for a,b,_ in TF])
q('0007',tipId='tks-tekcift',tip='Tablodaki tek-çift öncüllerle sayı durumunu bulma',z='orta',alt='Tek ve Çift Sayılar',kaz='Tabloda verilen işlem sonuçlarından a, b, c sayılarının tek–çift durumunu bulup öncülleri değerlendirir.',kalip='tablo',sekil=SK7,
 kart='K-TKS-07 (tek-çift tablosu) · a + c tek, b × c çift, a × c + b tek',
 metin='a, b ve c pozitif tam sayılardır. Aşağıdaki tabloda bazı işlemlerin sonuçlarının tek sayı mı, çift sayı mı olduğu verilmiştir.\nBuna göre,\nI. a × b + c tek sayıdır.\nII. b + c çift sayıdır.\nIII. a × c + b × c çift sayıdır.\nifadelerinden hangileri kesinlikle doğrudur?',
 dogru='I ve III',sira=SIRA7,yan=yan7,
 istenen='Doğru olan öncüller.',
 ip=['Tablodaki üç satırdan a, b ve c’nin tek mi çift mi olduğunu belirle; sonra öncülleri tek tek dene.'],
 bilgi=[TEK],
 ad=[A('a ile c’yi ayır','a + c tek olduğundan biri tek, diğeri çifttir; iki durum vardır.','a tek, c çift ya da a çift, c tek'),A('İkinci durumu ele','a çift, c tek ise a × c çifttir; a × c + b tek olduğundan b tek olur. Bu durumda b × c = tek × tek = tek çıkar ve tablodaki “çift” ile çelişir.','a çift, c tek → b tek → b × c tek ✗'),A('Birinci durumu doğrula','a tek, c çift ise a × c çifttir, yine b tek olur; b × c = tek × çift = çift tablo ile uyumludur.','a tek, b tek, c çift'),A('Öncülleri değerlendir','I: tek × tek + çift = tek (doğru). II: tek + çift = tek (yanlış). III: çift + çift = çift (doğru).','I ve III doğru')],
 puf='Çarpımın çift olduğu biliniyorsa çarpanlardan en az biri çifttir; her tablo satırından bir tek-çift bilgisi çıkar, üç bilgi birleşince a, b ve c belirlenir.')

# =============== 08 · ardışık tek sayılar şeması · orta ===============
x0=21; kut=[x0+2*i for i in range(7)]; assert kut==[21,23,25,27,29,31,33] and sum(kut[1:5])==104 and kut[0]+kut[-1]==54
x2=(104-12)//4; assert 4*x2+12==104 and 2*x2+12==58
x3=(104-28)//4; assert 4*x3+28==104 and 2*x3+12==50
o=[]
for i in range(7): o.append(nd(i*.95,0,'',.95,.7))
o.append(f'\\draw[line width=.9pt] ({.95-.42:.3f},-.55) -- ({.95-.42:.3f},-.75) -- ({4*.95+.42:.3f},-.75) -- ({4*.95+.42:.3f},-.55);')
o.append(tx(2.5*.95,-1.15,'Toplam: 104'))
o.append(ln(-.4,.65,6*.95+.4,.65,'-{Stealth[length=2mm]}'))
o.append(tx(3*.95,.95,'küçükten büyüğe'))
SK8=tz('\n'.join(o))
q('0008',tipId='tks-ardisik',tip='Ardışık tek sayılar şemasında toplam',z='orta',alt='Ardışık Sayılar',kaz='Kutulara yazılan ardışık tek sayıları x, x + 2, … biçiminde yazıp parantezle verilen toplamdan sayıları bulur.',kalip='şekilli',sekil=SK8,
 kart='K-TKS-08 (ardışık sayılar şeması) · 7 kutuda 2. ile 5. kutu toplamı 104',
 metin='Aşağıdaki şemadaki yedi kutuya soldan sağa doğru küçükten büyüğe ardışık tek doğal sayılar yazılmıştır. Şekilde köşeli ayraçla gösterilen kutulardaki sayıların toplamı şekilde verilmiştir.\nBuna göre en soldaki kutudaki sayı ile en sağdaki kutudaki sayının toplamı kaçtır?',
 dogru=54,yan=[(21,'x = 21 değerini bulup soruyu orada bırakmış; yalnız en soldaki kutuyu yazmış.','dikkat'),(33,'Yalnız en sağdaki kutuyu (x + 12 = 33) yazmış; iki uç toplanmamış.','dikkat'),(50,'Parantezi 3. kutudan 6. kutuya kadar okumuş: 4x + 28 = 104 → x = 19, uçlar 19 + 31 = 50.','dikkat'),(58,'Parantezi 1. kutudan 4. kutuya kadar okumuş: 4x + 12 = 104 → x = 23, uçlar 23 + 35 = 58.','dikkat')],
 istenen='En soldaki ve en sağdaki kutulardaki sayıların toplamı.',
 ip=['En soldaki sayıya x deyip kutulardaki sayıları x cinsinden yaz; parantezin hangi kutuları kapsadığına dikkat et.'],
 bilgi=[ARD],
 ad=[A('Kutuları x ile yaz','En soldaki sayı x ise ardışık tek sayılar ikişer artar.','x, x + 2, x + 4, x + 6, x + 8, x + 10, x + 12'),A('Parantezi yaz','2. kutudan 5. kutuya kadar dört sayının toplamı 104’tür.','(x + 2) + (x + 4) + (x + 6) + (x + 8) = 4x + 20 = 104'),A('x’i bul','Denklemi çöz.','4x = 84 → x = 21'),A('Uçları topla','En sağdaki kutu x + 12 = 33 olur.','21 + 33 = 54')],
 puf='Ardışık tek sayıları x, x + 2, x + 4, … diye yazmak toplamları kolaylaştırır; parantezin kapsadığı kutuları tek tek işaretleyerek say.')

# =============== 09 · işlem ağacı · orta ===============
sol=F(9)//F(7); sag=F(2)*(F(4)-F(3)); top9=sol+sag
assert sol==72 and sag==36 and top9==108
assert 2+sag==38 and sol+F(2)*1==74 and sag==36 and sol==72
o=[]
def nodeop(x,y,t): return nd(x,y,t,.8,.8,fill='vurgu!15',bold=True)
def leaf(x,y,t): return nd(x,y,t,.9,.7)
o+=[nodeop(0,0,'$+$'),nodeop(-2.1,-1.5,'$\\div$'),nodeop(2.1,-1.5,'$\\times$'),leaf(-3.1,-3,'$9!$'),leaf(-1.1,-3,'$7!$'),leaf(1.1,-3,'$2!$'),nodeop(3.1,-3,'$-$'),leaf(2.4,-4.5,'$4!$'),leaf(3.8,-4.5,'$3!$')]
for a_,b_ in [((0,0),(-2.1,-1.5)),((0,0),(2.1,-1.5)),((-2.1,-1.5),(-3.1,-3)),((-2.1,-1.5),(-1.1,-3)),((2.1,-1.5),(1.1,-3)),((2.1,-1.5),(3.1,-3)),((3.1,-3),(2.4,-4.5)),((3.1,-3),(3.8,-4.5))]:
    dx=b_[0]-a_[0]; dy=b_[1]-a_[1]; L_=(dx*dx+dy*dy)**.5
    ux,uy=dx/L_,dy/L_
    o.append(ln(a_[0]+ux*.5,a_[1]+uy*.5,b_[0]-ux*.5,b_[1]-uy*.5))
SK9=tz('\n'.join(o))
q('0009',tipId='tks-agac',tip='Faktöriyel içeren işlem ağacı',z='orta',alt='Faktöriyel ve İşlem Önceliği',kaz='Alt kutulardaki faktöriyelli değerleri işlem kutularına uygulayarak ağacın tepesindeki sonucu hesaplar.',kalip='şekilli',sekil=SK9,
 kart='K-TKS-09 (işlem ağacı) · 9!/7! + 2! × (4! − 3!)',
 metin='Aşağıdaki şemada her işlem kutusundaki işlem, hemen altındaki iki kutudaki sayılara soldan sağa doğru uygulanır (soldaki sayı işlemin ilk sayısıdır). Alttaki kutularda faktöriyelli sayılar yazılıdır.\nBuna göre en üstteki kutudaki sayı kaçtır?',
 dogru=108,yan=[(38,'9! ÷ 7! işlemini (9 − 7)! = 2! = 2 sanmış; 2 + 36 = 38.','bilgi'),(74,'4! − 3! işlemini (4 − 3)! = 1 sanmış; 72 + 2 × 1 = 74.','bilgi'),(36,'Yalnız sağ kolu hesaplamış (2! × (4! − 3!) = 36); sol koldaki 72’yi toplamaya katmamış.','dikkat'),(72,'Yalnız sol kolu hesaplamış (9! ÷ 7! = 72); sağ koldaki 36’yı toplamaya katmamış.','dikkat')],
 istenen='En üstteki kutudaki sayı.',
 ip=['Alt kutulardan başlayıp yukarı doğru her işlem kutusunun değerini sırayla bul.'],
 bilgi=[FAK],
 ad=[A('Sol kolu hesapla','9! ÷ 7! ifadesinde 7!’i sadeleştir.','9! ÷ 7! = 9 × 8 = 72'),A('Sağ kolun alt kutusunu hesapla','4! − 3! önce yapılır (ağaçta bu kutu × kutusunun altındadır).','24 − 6 = 18'),A('Sağ kolu hesapla','2! × 18 işlemini yap.','2 × 18 = 36'),A('Tepeyi bul','Sol ve sağ kolun değerleri toplanır.','72 + 36 = 108')],
 puf='Faktöriyelli bölmede büyük faktöriyeli küçüğün çarpımı olarak aç ve sadeleştir: 9! = 9 × 8 × 7!.')

# =============== 10 · akış şeması · zor ===============
def adim_say(n,kural):
    s=0
    while n!=1:
        n=kural(n); s+=1; assert s<100
    return s
dogru_k=lambda n:n//2 if n%2==0 else n+1
f1={n:adim_say(n,dogru_k) for n in range(1,21)}
c5=[n for n in f1 if f1[n]==5]; assert c5==[5,12,14,15] and len(c5)==4
ca=[n for n in f1 if f1[n]<=5]; assert ca==[1,2,3,4,5,6,7,8,12,14,15,16] and len(ca)==12
k_eksi=lambda n:n//2 if n%2==0 else n-1
def adim_say2(n,kural):
    s=0
    while n!=1 and s<60:
        n=kural(n); s+=1
    return s if n==1 else None
f2={n:adim_say2(n,k_eksi) for n in range(1,21)}
c_eksi=[n for n in f2 if f2[n]==5]
c4=[n for n in f1 if f1[n]==4]; c6=[n for n in f1 if f1[n]==6]; cle5=[n for n in f1 if f1[n]<=5]
kural3=lambda n:n//2 if n%2==0 else 3*n+1
f3={n:adim_say2(n,kural3) for n in range(1,21)}
c3=[n for n in f3 if f3[n]==5]
assert [f1[n] for n in range(1,9)]==[0,1,3,2,5,4,4,3] and [f1[n] for n in range(9,17)]==[7,6,6,5,6,5,5,4] and [f1[n] for n in range(17,21)]==[9,8,8,7]
c3b=[n for n in f3 if f3[n] is not None and f3[n]<=5]; assert c3b==[1,2,4,5,8,16] and len([n for n in f1 if f1[n]<5])==8 and len(ca)-1==11
o=[]
dm='diamond,draw,aspect=2.3,inner sep=1pt,align=center'
o.append('\\node[draw,ellipse,inner sep=3pt,align=center] (bas) at (0,0) {$n$ verilir,\\\\ $s=0$};')
o.append(f'\\node[{dm}] (d1) at (0,-1.9) {{$n=1$ mi?}};')
o.append('\\node[draw,ellipse,inner sep=3pt,align=center] (dur) at (3.6,-1.9) {$s$ yazılır\\\\ ve dur};')
o.append(f'\\node[{dm}] (d2) at (0,-4.0) {{$n$ çift mi?}};')
o.append('\\node[draw,rectangle,inner sep=3pt,fill=vurgu!12] (e) at (-2.6,-5.8) {$n\\leftarrow n\\div 2$};')
o.append('\\node[draw,rectangle,inner sep=3pt,fill=vurgu!12] (h) at (2.6,-5.8) {$n\\leftarrow n+1$};')
o.append('\\node[draw,rectangle,inner sep=3pt] (sc) at (0,-7.4) {$s\\leftarrow s+1$};')
ar='-{Stealth[length=2mm]}'
o.append(f'\\draw[{ar}] (bas) -- (d1);')
o.append(f'\\draw[{ar}] (d1) -- node[above,font=\\footnotesize] {{Evet}} (dur);')
o.append(f'\\draw[{ar}] (d1) -- node[right,font=\\footnotesize] {{Hayır}} (d2);')
o.append(f'\\draw[{ar}] (d2) -| node[above,pos=.25,font=\\footnotesize] {{Evet}} (e);')
o.append(f'\\draw[{ar}] (d2) -| node[above,pos=.25,font=\\footnotesize] {{Hayır}} (h);')
o.append(f'\\draw[{ar}] (e) |- (sc);')
o.append(f'\\draw[{ar}] (h) |- (sc);')
o.append(f'\\draw[{ar}] (sc.south) -- (0,-8.3) -- (-4.3,-8.3) -- (-4.3,-1.9) -- (d1.west);')
SK10=tz('\n'.join(o))
q('0010',tipId='tks-akis',tip='Akış şemasında adım sayısına göre sayma',z='zor',alt='Akış Şeması',kaz='Akış şemasını farklı başlangıç değerleri için çalıştırıp adım sayısı verilen koşulu sağlayan başlangıç değerlerinin adedini bulur.',kalip='şekilli',sekil=SK10,
 kart='K-TKS-10 (akış şeması) · çift ise ÷2, tek ise +1, 1 ≤ n ≤ 20 için s ≤ 5',
 metin='Aşağıdaki akış şemasında n bir pozitif tam sayıdır. Şemada okların yönünde ilerlenir ve n = 1 olduğunda şema durup s değerini yazar.\nn yerine 1’den 20’ye kadar (1 ve 20 dahil) her doğal sayı ayrı ayrı verilerek şema çalıştırılıyor.\nBuna göre kaç farklı n sayısı için şemanın yazdığı s değeri en fazla 5 olur?',
 dogru=12,yan=[(4,'Yalnız s = 5 olan sayıları (5, 12, 14, 15) saymış; “en fazla 5” için s < 5 olanlar da sayılır.','dikkat'),(6,'Tek sayıda n + 1 yerine 3n + 1 uygulamış; bu kuralla 1, 2, 4, 5, 8, 16 sayıları en fazla 5 adımda biter.','bilgi'),(8,'s = 5 olan sayıları (5, 12, 14, 15) dışarıda bırakıp yalnız s < 5 olan 8 sayıyı saymış.','dikkat'),(11,'n = 1 için şema hiç işlem yapmadan durduğundan (s = 0) bu sayıyı saymamış; oysa s = 0 ≤ 5’tir.','dikkat')],
 istenen='s değeri en fazla 5 olan n sayılarının adedi.',
 ip=['Küçük sayılardan başlayıp her n için şemadaki işlemleri 1’e ulaşana kadar uygula ve adım sayısını yaz.'],
 bilgi=[AKS],
 ad=[A('Kuralı oku','n çiftse ikiye bölünür, tekse 1 eklenir; her işlemden sonra s bir artar; n = 1 olunca şema durur.','çift: n ÷ 2 · tek: n + 1 · her adımda s + 1'),A('1–8 için s değerlerini bul','Örnek: 5 → 6 → 3 → 4 → 2 → 1 yolunda 5 adım vardır.','1: 0 · 2: 1 · 3: 3 · 4: 2 · 5: 5 · 6: 4 · 7: 4 · 8: 3'),A('9–16 için s değerlerini bul','Çiftlerde yarıya, tek sayılarda bir fazlasına bakılır.','9: 7 · 10: 6 · 11: 6 · 12: 5 · 13: 6 · 14: 5 · 15: 5 · 16: 4'),A('17–20 için s değerlerini bul','Aynı kural uygulanır.','17: 9 · 18: 8 · 19: 8 · 20: 7'),A('s ≤ 5 olanları say','s değeri 5 ve daha küçük olan sayılar 1, 2, 3, 4, 5, 6, 7, 8, 12, 14, 15 ve 16’dır.','12 sayı')],
 puf='Akış şemasında sayıları tek tek denerken bir sayının adım sayısını daha önce bulduğun daha küçük sayıya bağla: 12 → 6 olduğundan s(12) = 1 + s(6).')

# =============== 11 · sayı çarkı · zor ===============
V=[7,1,3,2,4,1,6,7]; s0=1; N=40
seq=[s0]
for _ in range(60): seq.append((seq[-1]+V[seq[-1]])%8)
assert seq[:9]==[1,2,5,6,4,0,7,6,4]
m,per=3,4; assert seq[m]==seq[m+per] and all(seq[i]==seq[i+per] for i in range(m,50))
def deg(k): return V[seq[m+((k-m)%per)]]
assert deg(N)==V[seq[N]]==4
w1=V[seq[N%per]]; w2=V[seq[N-1]]; w3=V[seq[N+1]]; w4=V[seq[(N-m)%per]]
assert (w1,w2,w3,w4)==(1,6,7,3) and len({4,w1,w2,w3,w4})==5 and N%per==0 and (N-m)%per==1
import math
R=1.9; o=[]
o.append(f'\\draw[line width=1pt] (0,0) circle ({R});')
for i in range(8):
    a=90-45*i
    o.append(ln(0,0,R*math.cos(math.radians(a)),R*math.sin(math.radians(a))))
    c=a-22.5
    o.append(tx(1.35*math.cos(math.radians(c)),1.35*math.sin(math.radians(c)),f'\\textbf{{{V[i]}}}','font=\\large'))
c1=90-45*s0-22.5
o.append(f'\\draw[line width=1.6pt,-{{Stealth[length=3mm]}},vurgu!70!black] ({2.85*math.cos(math.radians(c1)):.3f},{2.85*math.sin(math.radians(c1)):.3f}) -- ({2.05*math.cos(math.radians(c1)):.3f},{2.05*math.sin(math.radians(c1)):.3f});')
o.append(tx(3.2*math.cos(math.radians(c1)),3.2*math.sin(math.radians(c1)),'ok'))
o.append('\\draw[-{Stealth[length=2mm]}] (160:2.45) arc (160:120:2.45);'); o.append(tx(-2.25,2.45,'saat yönü'))
SK11=tz('\n'.join(o))
q('0011',tipId='tks-cark',tip='Sayı çarkında tekrar eden hareket',z='zor',alt='Çark ve Periyot',kaz='Sayı çarkında okun hareketini kurala göre izleyip yinelenen bölümü bulur ve uzak bir hamledeki sayıyı belirler.',kalip='şekilli',sekil=SK11,
 kart='K-TKS-11 (sayı çarkı) · 8 bölmeli çark, ok bulunduğu bölmedeki sayı kadar ilerler, 40. hamle',
 metin='Sekiz eşit bölmeye ayrılmış aşağıdaki çarkın bölmelerine birer sayı yazılmıştır. Ok, şekildeki bölmeyi göstererek başlıyor. Her hamlede ok, o anda gösterdiği bölmedeki sayı kadar bölme saat yönünde ilerliyor.\nBuna göre 40. hamle sonunda ok, içinde hangi sayı yazılı olan bölmeyi gösterir?',
 dogru=4,yan=[(1,'Yinelenmeyi hiç görmeden 40 hamlenin 4’ün katı olduğuna bakıp okun yeniden başlangıçtaki bölmeye (1) döndüğünü sanmış.','dikkat'),(3,'(40 − 3) ÷ 4 işleminden kalan 1’i yinelenen bölüme değil dizinin başına uygulayıp 1. hamledeki sayıyı (3) okumuş.','dikkat'),(6,'39. hamledeki bölmeyi okumuş (bir hamle eksik saymış).','dikkat'),(7,'41. hamledeki bölmeyi okumuş (bir hamle fazla saymış).','dikkat')],
 istenen='40. hamle sonunda okun gösterdiği bölmedeki sayı.',
 ip=['Okun ilk birkaç hamlesini tek tek izle; bir bölmeye ikinci kez geldiği anı bul.'],
 bilgi=[PER],
 ad=[A('Bölmeleri numarala','Başlangıç bölmesinden saat yönünde ilerlenirken okun geçtiği bölmelerin sırası bulunur.','1 → 3 → 1 → 6 → 4 → 7 → 7 → 6 → 4 → 7 → 7 → …'),A('Yinelenmeyi bul','Ok, 3. hamlede geldiği 6 yazılı bölmeye 7. hamlede yeniden gelir; 4 hamlelik bölüm tekrar eder.','yinelenmeyen kısım: 3 hamle · periyot: 4 hamle'),A('Yinelenen bölümün değerlerini yaz','3. hamleden sonraki bölmelerde yazan sayılar: 6, 4, 7, 7 biçiminde tekrarlanır.','3. hamle: 6 · 4. hamle: 4 · 5. hamle: 7 · 6. hamle: 7 · 7. hamle: 6 …'),A('40. hamleyi bul','Yinelenmeyen 3 hamle çıkarılır ve kalan 4’e bölünür.','(40 − 3) = 37 = 4 × 9 + 1'),A('Sayıyı oku','Kalan 1 ise yinelenen bölümün ikinci terimi, 4. hamledeki sayıdır.','4')],
 puf='Yinelenmeyen başlangıç kısmını sayıp ayır; kalan yinelenen bölüme (periyoda) göre hesapla.')

# =============== 12 · işlem işaretleri · zor ===============
OPS={'+':lambda a,b:a+b,'−':lambda a,b:a-b,'×':lambda a,b:a*b,'÷':lambda a,b:a/b}
def ev(nums,ops):
    n=[Fr(x) for x in nums]; o_=list(ops); i=0
    while i<len(o_):
        if o_[i] in '×÷': n[i]=OPS[o_[i]](n[i],n[i+1]); del n[i+1]; del o_[i]
        else: i+=1
    r=n[0]
    for k,op in enumerate(o_): r=OPS[op](r,n[k+1])
    return r
R1=[9,8,2,8,12]; R2=[12,8,4,8,2]; TR=('−','+','÷','×')
perms=list(itertools.permutations('+−×÷'))
assert ev(R1,TR)==4 and [p for p in perms if ev(R1,p)==4]==[TR] and ev(R2,TR)==5
def lt(nums,ops):
    r=Fr(nums[0])
    for k,op in enumerate(ops): r=OPS[op](r,Fr(nums[k+1]))
    return r
assert lt(R2,TR)==2
sw=lambda i:tuple(TR[:i])+(TR[i+1],TR[i])+tuple(TR[i+2:])
P0,P1,P2=sw(0),sw(1),sw(2)
assert ev(R2,P0)==19 and ev(R2,P1)==26 and ev(R2,P2)==20 and ev(R1,P0)!=4 and ev(R1,P1)!=4 and ev(R1,P2)!=4
assert ev(R1,P0)==14 and ev(R1,P2)==Fr(7,3) and ev(R1,P1)==101 and len(perms)==24
o=[]
def satir(y,nums,sonuc):
    x=0
    for i,n_ in enumerate(nums):
        o.append(tx(x,y,f'\\large {n_}')); x+=.62
        if i<4: o.append(f'\\node[draw,circle,minimum size=.5cm,inner sep=0pt] at ({x:.3f},{y}) {{}};'); x+=.62
    o.append(tx(x,y,'\\large $=$')); o.append(tx(x+.65,y,f'\\large {sonuc}'))
satir(.4,R1,'4'); satir(-.6,R2,'?')
SK12=tz('\n'.join(o))
q('0012',tipId='tks-isaret',tip='Kutulara işlem işareti yerleştirme',z='zor',alt='İşlem Önceliği',kaz='Birinci satırdaki eşitlikten işlem işaretlerinin sırasını işlem önceliğiyle bulup ikinci satıra uygular.',kalip='şekilli',sekil=SK12,
 kart='K-TKS-12 (işlem işareti kutuları) · 9 ○ 8 ○ 2 ○ 8 ○ 12 = 4 ve ikinci satır',
 metin='Aşağıdaki iki işlemde yuvarlak içlere +, −, × ve ÷ işaretlerinden her biri yalnız bir kez yazılacaktır. İki satırda da işaretler soldan sağa aynı sırada yazılacak ve birinci satırdaki eşitlik sağlanacaktır. İşlem önceliği geçerlidir.\nBuna göre ikinci satırdaki işlemin sonucu kaçtır?',
 dogru=5,yan=[(2,'İkinci satırı işlem önceliği gözetmeden soldan sağa hesaplamış: ((12 − 8 + 4) ÷ 8) × 2 = 2.','islem'),(19,'İşaret dizisini (−, +, ÷, ×) yerine (+, −, ÷, ×) almış; birinci satırı denetlememiş (9 + 8 − 2 ÷ 8 × 12 = 14, 4 değil): 12 + 8 − 4 ÷ 8 × 2 = 19.','dikkat'),(20,'İşaret dizisini (−, +, ×, ÷) almış; birinci satırı denetlememiş (9 − 8 + 2 × 8 ÷ 12 = 7/3, 4 değil): 12 − 8 + 4 × 8 ÷ 2 = 20.','dikkat'),(26,'İşaret dizisini (−, ÷, +, ×) almış; birinci satırı denetlememiş (9 − 8 ÷ 2 + 8 × 12 = 101, 4 değil): 12 − 8 ÷ 4 + 8 × 2 = 26.','dikkat')],
 istenen='İkinci satırdaki işlemin sonucu.',
 ip=['Çarpma ve bölme işlemleri toplama ve çıkarmadan önce yapıldığına göre, birinci satırın sonucunu 4 yapan işaret dizilişini ara.'],
 bilgi=[ISL],
 ad=[A('İşaret sırasını bul','Birinci satırda sonucu 4 yapan tek dizilişi bulmak için ÷ ve ×’in toplama–çıkarmadan önce yapıldığı göz önüne alınır; denemeyle (−, +, ÷, ×) bulunur.','9 − 8 + 2 ÷ 8 × 12'),A('Birinci satırı denetle','Önce soldan sağa 2 ÷ 8 × 12 hesaplanır, sonra toplama–çıkarma yapılır.','2 ÷ 8 × 12 = 3 → 9 − 8 + 3 = 4 ✓'),A('Diğer dizilişleri ele','Kalan 23 dizilişin hiçbiri 4 vermez (birinci satırın sonucu 14, 7/3, 101 gibi çıkar).','tek çözüm: −, +, ÷, ×'),A('İkinci satıra uygula','Aynı işaretleri ikinci satıra yaz.','12 − 8 + 4 ÷ 8 × 2'),A('Hesapla','Önce ÷ ve × (soldan sağa), sonra − ve +.','4 ÷ 8 × 2 = 1 → 12 − 8 + 1 = 5')],
 puf='İşaret yerleştirmede önce çarpma–bölme kısmının değerini tahmin edip toplama–çıkarmayla hedefe ulaşan dizilişi dene; bulduğunu birinci satırda mutlaka denetle.')

# =============== 13 · sayı doğrusunda sıçrayış · zor ===============
A_,B_=-13,15; a,b,n=6,2,10; D=B_-A_
Rr=(D+b*n)//(a+b); Ll=n-Rr
assert D==28 and (D+b*n)%(a+b)==0 and Rr==6 and Ll==4 and a*Rr-b*Ll==D
assert D%(a-b)==0 and D//(a-b)==7 and (D+a*n)%(a+b)==0 and (D+a*n)//(a+b)==11 and a*(n-11)-b*11==-D and D//b==14
x0_,x1_=-16,21; sc=.2
X=lambda v:(v-x0_)*sc
o=[ln(X(x0_),0,X(x1_),0,'line width=1pt,-{Stealth[length=2.2mm]}')]
for v in range(x0_+1,x1_):
    o.append(ln(X(v),-.06,X(v),.06))
for v in range(-15,21,5):
    o.append(ln(X(v),-.13,X(v),.13)); o.append(tx(X(v),-.42,f'${v if v>=0 else "-"+str(-v)}$'))
for v,t in [(A_,'A'),(B_,'B')]:
    o.append(f'\\fill[vurgu!70!black] ({X(v):.3f},0) circle (.1);'); o.append(tx(X(v),.42,f'\\textbf{{{t}}}','font=\\normalsize'))
SK13=tz('\n'.join(o))
q('0013',tipId='tks-sicrama',tip='Sayı doğrusunda ileri-geri sıçrayış',z='orta',alt='Sayı Doğrusunda İleri-Geri Sayma',kaz='Sayı doğrusunda iki nokta arasındaki uzaklığı okuyup sağa ve sola yapılan sıçrayış sayılarını denklemle bulur.',kalip='şekilli',sekil=SK13,
 kart='K-TKS-13 (sayı doğrusunda ileri-geri) · A = −13, B = 15, 10 sıçrayış, sağa 6 sola 2',
 metin='Bir kurbağa, aşağıdaki sayı doğrusunda A noktasından başlayıp tam 10 sıçrayışta B noktasına ulaşıyor. Kurbağa her sıçrayışta sağa 6 birim ya da sola 2 birim gidiyor.\nBuna göre kurbağa kaç kez sola sıçramıştır?',
 dogru=4,yan=[(6,'Sola sıçrayış sayısı yerine sağa sıçrayış sayısını (6) yazmış.','dikkat'),(7,'Her sıçrayışta 6 − 2 = 4 birim net ilerlediğini sanıp 28 ÷ 4 = 7 bulmuş; sağ ve sol sayısı ayrı ayrı belirlenmelidir.','bilgi'),(11,'Uzaklığı −28 almış (B’den A’ya gidiyor sanmış): 6 × (10 − L) − 2 × L = −28 → L = 11 (10 sıçrayışta sola 11 kez sıçranamaz).','islem'),(14,'Yalnız sola gidilen yolu düşünüp 28 ÷ 2 = 14 bulmuş.','dikkat')],
 istenen='Kurbağanın sola sıçrayış sayısı.',
 ip=['A ile B arasındaki uzaklığı sayı doğrusundan oku; sağa ve sola sıçrayış sayılarını iki bilinmeyen olarak yaz.'],
 bilgi=[SIC],
 ad=[A('A ve B’yi oku','Sayı doğrusunda A, −15’in 2 birim sağındadır; B, 15’tedir.','A = −13 · B = 15 → B − A = 28'),A('Bilinmeyenleri tanımla','Sağa sıçrayış sayısı s, sola sıçrayış sayısı t olsun; toplam 10 sıçrayış vardır.','s + t = 10'),A('Yer değiştirmeyi yaz','Sağa gidilen yoldan sola gidilen yolu çıkarmak 28’i verir.','6 × s − 2 × t = 28'),A('Çöz','s = 10 − t yazılır.','6 × (10 − t) − 2 × t = 28 → 60 − 8t = 28 → t = 4')],
 puf='İleri-geri hareketlerde sağa ve sola yapılan sayıları iki ayrı bilinmeyen alıp toplam sıçrayış ile toplam yer değiştirme için iki eşitlik yaz.')

bitir(P,'tksek',UK)
