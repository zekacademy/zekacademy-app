"""EBOB – EKOK · parti 1: 8 ana + 8 kardeş. Her cevap ve ara sonuç kodla (kaba kuvvet tarama dahil) doğrulanır."""
import sys,os,json
from math import lcm
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,os.path.join(H,'..'))
from ortak import *

# ---------- yardımcılar ----------
def fmt(v):
    v=Fr(v)
    if v.denominator==1: return ('−' if v<0 else '')+str(abs(v.numerator))
    return ('−' if v<0 else '')+f'{abs(v.numerator)}/{v.denominator}'
def SK(dogru,yanlis,sira=None):
    """yanlis: değer -> (tur, açıklama). Sayısal şıklar küçükten büyüğe dizilir; sira verilirse o sıra kullanılır."""
    vals=[dogru]+list(yanlis); assert len(set(vals))==5 and dogru not in yanlis
    if sira is None: vals=sorted(vals,key=Fr); yaz=[fmt(v) for v in vals]
    else: assert sorted(map(str,sira))==sorted(map(str,vals)); vals=list(sira); yaz=[str(v) for v in vals]
    L='ABCDE'; sik=L[vals.index(dogru)]
    return dict(siklar=yaz,sik=sik,cel={L[i]:yanlis[v][1] for i,v in enumerate(vals) if v!=dogru},tur={L[i]:yanlis[v][0] for i,v in enumerate(vals) if v!=dogru})
def izgara(m,n,ic=False):
    """m × n kare parsel; köşelerde direk. ic=True ise sınırda olmayan direkler vurgulanır."""
    W=330; s=min(250/m,120/n); x0=(W-s*m)/2; y0=14; b=[]
    for i in range(m+1): b.append(f'<line x1="{x0+i*s:.1f}" y1="{y0}" x2="{x0+i*s:.1f}" y2="{y0+n*s:.1f}" stroke-width="1" opacity=".55"/>')
    for j in range(n+1): b.append(f'<line x1="{x0}" y1="{y0+j*s:.1f}" x2="{x0+m*s:.1f}" y2="{y0+j*s:.1f}" stroke-width="1" opacity=".55"/>')
    for i in range(m+1):
        for j in range(n+1):
            v=(0<i<m and 0<j<n) if ic else True
            st=f'style="fill:{G.ACC};stroke:none"' if v else 'style="fill:currentColor;stroke:none" opacity=".45"'
            b.append(f'<circle cx="{x0+i*s:.1f}" cy="{y0+j*s:.1f}" r="2.6" {st}/>')
    b.append(G._t(W/2,y0+n*s+18,f'{m} × {n} parsel · {(m-1)*(n-1) if ic else (m+1)*(n+1)} {"iç direk" if ic else "direk"}',size=12,bold=True,renk=G.ACC))
    return G._svg(W,int(y0+n*s+28),''.join(b))
GUN=['Pazartesi','Salı','Çarşamba','Perşembe','Cuma','Cumartesi','Pazar']
gun=lambda bas,ileri:GUN[(GUN.index(bas)+ileri)%7]

ONEK='ebobekok'; KONU='EBOB – EKOK'; UK='mat|Ebob – ekok'
P=Parti(ONEK,KONU,UK)

EBOB=B('EBOB','sayıların hepsini tam bölen en büyük sayı. Örnek: EBOB(12, 18) = 6 (12 = 6 × 2, 18 = 6 × 3)')
EKOK=B('EKOK','sayıların hepsinin katı olan en küçük pozitif sayı. Örnek: EKOK(4, 6) = 12')
EBEK=B('EBOB ile EKOK ilişkisi','EBOB(a, b) = d ise a = d × m, b = d × n (m ile n aralarında asal, yani ortak böleni yalnız 1) ve EKOK(a, b) = d × m × n. Örnek: 12 = 6 × 2, 18 = 6 × 3 ⇒ EKOK = 6 × 2 × 3 = 36')
HAFTA=B('Haftanın günleri','günler 7 günde bir tekrar eder. Örnek: pazartesiden 10 gün sonra: 10 = 7 + 3 ⇒ 3 gün ileri, perşembe')

# ---------- kartlar ve tipler ----------
TIPLER=[('ebk-tanim','EBOB ve EKOK ilişkisi'),('ebk-parca','Eş parçalara bölme (EBOB)'),('ebk-kare','Eş parçalarla kare ve küp oluşturma (EKOK)'),
        ('ebk-kalan','Kalan koşullu sayılar (EKOK)'),('ebk-periyot','Periyodik buluşma (EKOK)')]
TAD=dict(TIPLER)
KARTLAR=[
 dict(id='K-EBK-01',alt='EBOB – EKOK Kavramı',fikir='EBOB’u verilen iki sayı d × m ve d × n biçiminde yazılır (m, n ortak böleni olmayan); toplam ya da EKOK bilgisiyle olası ikililer taranır.',tuzak='m ile n’nin ortak böleni olmaması koşulunu unutmak; basamak ya da “büyüktür” koşullarını atlamak; a × b ile EKOK’u karıştırmak.',zorluk='orta',kalip='düz',adim=3,tipId='ebk-tanim',kaynak='ÖSYM (EBOB-EKOK Kavramı ve Özellikleri) · 3D (EBOB(x, 35) = 7) · Bilgi Sarmal'),
 dict(id='K-EBK-02',alt='EBOB Problemleri',fikir='Farklı uzunluk/hacimler artmadan eş ve olabildiğince büyük parçalara ayrılır; parça boyu EBOB, parça sayısı bölümlerin toplamıdır. Izgara sorularında köşe ve direk sayısı da istenir.',tuzak='Parça boyunu parça sayısı sanmak; EKOK kullanmak; ızgarada direk sayısı için +1’i unutmak.',zorluk='kolay',kalip='hikâyeli',adim=2,tipId='ebk-parca',kaynak='ÖSYM (EBOB-EKOK Problemleri) · Bilgi Sarmal (en büyük ortak bölen ile kalan) · Mert (konserve, kutu dizme)'),
 dict(id='K-EBK-03',alt='EKOK Problemleri',fikir='Eş dikdörtgen ya da prizmalar aynı yönde dizilerek en küçük kare/küp oluşturulur; kenar EKOK, adet her boyuttaki bölümlerin çarpımıdır.',tuzak='EBOB kullanmak; boyutlardaki adetleri toplamak; kenar uzunluğunu adet sanmak.',zorluk='orta',kalip='hikâyeli',adim=3,tipId='ebk-kare',kaynak='ÖSYM (EBOB-EKOK Problemleri) · Bilgi Sarmal, Mert'),
 dict(id='K-EBK-04',alt='EKOK Problemleri',fikir='Farklı bölenlere göre kalanlar, bölenden hep aynı sayı eksikse sayı “EKOK’un katı − sabit” biçimindedir; bir sınırla en küçük/en büyük değer bulunur.',tuzak='Sabiti çıkarmak yerine eklemek; EKOK yerine bölenlerin çarpımını almak; sınır koşulunu unutmak.',zorluk='orta',kalip='hikâyeli',adim=3,tipId='ebk-kalan',kaynak='ÖSYM (Bölünebilme · kalanlı bölme) · Bilgi Sarmal (99, 148, 161 kalanları) · 3D'),
 dict(id='K-EBK-05',alt='Periyodik Problemler',fikir='Farklı aralıklarla tekrar eden olaylar EKOK aralığında birlikte gerçekleşir; gün adı için 7 ile kalan, sayım için ilk ve son an dikkate alınır.',tuzak='EKOK yerine toplam ya da çarpım kullanmak; başlangıç anını saymamak; haftada kalan günü yanlış saymak.',zorluk='kolay',kalip='hikâyeli',adim=2,tipId='ebk-periyot',kaynak='ÖSYM (Periyodik Problemler, karton etiketleme) · 3D (5 günde bir nöbet)'),
 dict(id='K-EBK-06',alt='EBOB – EKOK Kavramı',fikir='EBOB ve EKOK birlikte verilir; m × n = EKOK ÷ EBOB çarpanlarına ayrılıp ortak böleni olmayan ikililer listelenir, toplam ya da fark en küçüklenir.',tuzak='m = 1 durumunu “sayılar EBOB’dan büyük” koşuluna rağmen saymak; m ile n’nin ortak böleni olan ikilileri almak.',zorluk='zor',kalip='düz',adim=4,tipId='ebk-tanim',kaynak='ÖSYM (EBOB-EKOK Kavramı) · Bilgi Sarmal, 345'),
]
for k in KARTLAR: k['konu']=KONU; k['tip']=TAD[k['tipId']]
KS=[dict(id=k['id'],konu=k['konu'],alt=k['alt'],fikir=k['fikir'],tuzak=k['tuzak'],zorluk=k['zorluk'],kalip=k['kalip'],adim=k['adim'],tipId=k['tipId'],tip=k['tip'],kaynak=k['kaynak']) for k in KARTLAR]
TS=[dict(tipId=t,ad=a,kartlar=[k['id'] for k in KARTLAR if k['tipId']==t],uygulamaKonu=UK) for t,a in TIPLER]
json.dump(dict(konu=KONU,surum=1,kartlar=KS,tipler=TS),open(os.path.join(H,'..','kartlar',ONEK+'.json'),'w'),ensure_ascii=False,indent=1)
T=lambda t:dict(tipId=t,tip=TAD[t])

def parca(L):
    """Artansız eş parçalar: en az parça sayısı ve parça boyu (tarama)."""
    r=[(sum(x//d for x in L),d) for d in range(1,max(L)+1) if all(x%d==0 for x in L)]
    return min(r)

# ===== 0001 KOLAY · ebk-parca (K-EBK-02)
assert parca([84,126,210])==(10,42) and gcd(gcd(84,126),210)==42 and lcm(84,126,210)==1260
assert (84+126+210)//21==20 and (84+126+210)//14==30
P.R('0001',**T('ebk-parca'),zorluk='kolay',alt='EBOB Problemleri',kazanim='Farklı uzunlukları artansız ve olabildiğince uzun eş parçalara ayırmak için EBOB’u kullanır; parça sayısını bulur.',kalip='hikâyeli',adim=2,
 kart='K-EBK-02 (artansız eş parçalar, EBOB) · yeni kurgu (marangoz tahtaları), istenen parça sayısı',
 metin='Bir marangoz, uzunlukları 84 cm, 126 cm ve 210 cm olan üç tahtanın her birini hiç artık kalmayacak biçimde eşit uzunlukta parçalara kesecektir. Bütün parçaların uzunlukları birbirine eşit ve olabildiğince büyük olacaktır.\nBuna göre marangoz toplam kaç parça elde eder?',
 **SK(10,{20:('islem','EBOB’u 21 bulmak; 84, 126 ve 210’un üçünü de bölen en büyük sayı 42.'),30:('islem','Ortak böleni 14 almak; daha büyük ortak bölen (42) var.'),
          42:('dikkat','42, bir parçanın uzunluğu; soru parça sayısını soruyor.'),1260:('bilgi','EKOK’u hesaplamak; tahtaları bölen sayı gerekir, yani EBOB.')}),
 istenen='Elde edilen toplam parça sayısı.',
 ipuclari=['Parça uzunluğu üç tahtanın uzunluğunu da tam bölmeli.','Parçalar olabildiğince uzunsa bu uzunluk hangi ortak bölen olur?','Her tahtanın kaç parçaya ayrıldığını bulup topla.'],bilgi=[EBOB],
 adimlar=[A('Parça uzunluğu','Uzunluk üç sayıyı da bölmeli ve en büyük olmalı: EBOB.','EBOB(84, 126, 210) = 42 cm'),
          A('Her tahta','Her uzunluğu 42’ye böl.','84 ÷ 42 = 2 · 126 ÷ 42 = 3 · 210 ÷ 42 = 5'),
          A('Toplam','Parçaları topla.','2 + 3 + 5 = 10 parça')],
 puf='“Artmadan, eş ve en büyük parça” EBOB demektir; parça sayısı her uzunluğun EBOB’a bölümlerinin toplamıdır.')
assert parca([60,84,132])==(23,12) and sum(x//6 for x in (60,84,132))==46 and sum(x//4 for x in (60,84,132))==69 and sum(x//3 for x in (60,84,132))==92
P.K('0001',metin='Bir zeytinyağı üreticisinin depolarında 60 litre, 84 litre ve 132 litre zeytinyağı vardır. Üretici bu yağların tamamını, depolardaki yağları birbirine karıştırmadan, eşit hacimli ve olabildiğince büyük bidonlara dolduracaktır.\nBütün bidonlar tamamen dolacağına göre üretici kaç bidon kullanır?',
 **SK(23,{12:('dikkat','12, bir bidonun hacmi (litre); soru bidon sayısını soruyor.'),46:('islem','Ortak böleni 6 almak; daha büyük ortak bölen (12) var.'),
          69:('islem','Ortak böleni 4 almak; bidonlar olabildiğince büyük olmalı.'),92:('islem','Ortak böleni 3 almak; en büyük ortak bölen 12.')}),
 istenen='Kullanılan bidon sayısı.',
 ipuclari=['Bidon hacmi üç miktarı da tam bölmeli.','Olabildiğince büyük bidon, en büyük ortak bölendir.','Her depodaki yağın kaç bidon doldurduğunu topla.'],bilgi=[EBOB],
 adimlar=[A('Bidon hacmi','Üç miktarı da bölen en büyük sayı.','EBOB(60, 84, 132) = 12 L'),
          A('Her depo','Her miktarı 12’ye böl.','60 ÷ 12 = 5 · 84 ÷ 12 = 7 · 132 ÷ 12 = 11'),
          A('Toplam','Bidonları topla.','5 + 7 + 11 = 23 bidon')],
 puf='Bidon sayısını en aza indirmek için bidon hacmini en büyük ortak bölen seç.')

# ===== 0002 KOLAY · ebk-periyot (K-EBK-05)
ortak=[d for d in range(1,200) if d%6==0 and d%8==0][0]; assert ortak==24==lcm(6,8) and gun('Pazartesi',24)=='Perşembe'
assert gun('Pazartesi',14)=='Pazartesi' and gun('Pazartesi',8)=='Salı' and gun('Pazartesi',2)=='Çarşamba' and gun('Pazartesi',48)=='Pazar'
P.R('0002',**T('ebk-periyot'),zorluk='kolay',alt='Periyodik Problemler',kazanim='Farklı aralıklarla tekrar eden iki olayın yeniden birlikte gerçekleşeceği zamanı EKOK ile bulur; gün adını 7 ile kalandan belirler.',kalip='hikâyeli',adim=2,
 kart='K-EBK-05 (periyodik buluşma, gün adı) · yeni kurgu (hastane nöbeti), yeni aralıklar',
 metin='Bir hastanede Deniz Hemşire 6 günde bir, Ece Hemşire 8 günde bir nöbet tutmaktadır. İkisi bir pazartesi günü birlikte nöbet tutmuştur.\nBuna göre ikisinin bir sonraki birlikte nöbeti hangi gündür?',
 **SK('Perşembe',{'Pazartesi':('bilgi','6 + 8 = 14 gün saymak; birlikte nöbet için iki aralığın ortak katı (EKOK) gerekir.'),'Salı':('dikkat','Yalnız büyük aralığı (8 gün) almak; 8. gün Deniz nöbette değildir.'),
                  'Çarşamba':('bilgi','EBOB’u (2) almak; tekrar eden olaylar EKOK’ta buluşur.'),'Pazar':('islem','6 × 8 = 48 gün almak; 48 bir ortak kattır ama en küçüğü değildir.')},
    sira=['Pazartesi','Salı','Çarşamba','Perşembe','Pazar']),
 istenen='Bir sonraki ortak nöbetin günü.',
 ipuclari=['İkisinin yeniden birlikte nöbet tutması için geçen gün, 6’nın ve 8’in ortak katı olmalı.','En küçük ortak kat kaç?','Bu gün sayısını 7’ye böl; kalan kadar pazartesiden ileri say.'],bilgi=[EKOK,HAFTA],
 adimlar=[A('Ortak nöbet','Gün sayısı hem 6’nın hem 8’in katı olmalı; ilk buluşma en küçük ortak kat.','EKOK(6, 8) = 24 gün'),
          A('Haftalara ayır','24 günde 3 tam hafta ve 3 gün var.','24 = 7 × 3 + 3'),
          A('Gün adı','Pazartesiden 3 gün ileri.','salı, çarşamba, perşembe ⇒ perşembe')],
 puf='Birlikte tekrar etme sorularında EKOK’u bul; gün adı için 7’ye bölümden kalan kadar ileri say.')
assert lcm(10,15)==30 and gun('Çarşamba',30)=='Cuma' and gun('Çarşamba',5)=='Pazartesi' and gun('Çarşamba',15)=='Perşembe' and gun('Çarşamba',150)=='Cumartesi' and gun('Çarşamba',25)=='Pazar'
P.K('0002',metin='Bir fabrikadaki A makinesi 10 günde bir, B makinesi 15 günde bir bakıma alınmaktadır. İki makine bir çarşamba günü birlikte bakıma alınmıştır.\nBuna göre iki makine bir sonraki sefer hangi gün birlikte bakıma alınır?',
 **SK('Cuma',{'Pazartesi':('bilgi','EBOB’u (5) almak; iki olay EKOK’ta yeniden buluşur.'),'Perşembe':('dikkat','Yalnız büyük aralığı (15 gün) almak; 15. gün A bakımda değildir.'),
              'Cumartesi':('islem','10 × 15 = 150 gün almak; ortak katların en küçüğü 30.'),'Pazar':('bilgi','10 + 15 = 25 gün saymak; ortak kat gerekir.')},
    sira=['Pazartesi','Perşembe','Cuma','Cumartesi','Pazar']),
 istenen='Bir sonraki ortak bakımın günü.',
 ipuclari=['Geçen gün sayısı hem 10’un hem 15’in katı olmalı.','En küçük ortak katı bul.','7’ye böl ve kalan kadar çarşambadan ileri say.'],bilgi=[EKOK,HAFTA],
 adimlar=[A('Ortak bakım','En küçük ortak kat.','EKOK(10, 15) = 30 gün'),
          A('Haftalara ayır','30 günde 4 tam hafta ve 2 gün var.','30 = 7 × 4 + 2'),
          A('Gün adı','Çarşambadan 2 gün ileri.','perşembe, cuma ⇒ cuma')],
 puf='Tam haftalar günü değiştirmez; yalnız 7’ye bölümden kalan günleri ileri say.')

# ===== 0003 ORTA · ebk-tanim (K-EBK-01)
v=[(a,b) for a in range(10,100) for b in range(a+1,100) if gcd(a,b)==12 and a+b==84]; assert v==[(12,72),(24,60),(36,48)]
assert max(lcm(a,b) for a,b in v)==144 and min(lcm(a,b) for a,b in v)==72 and lcm(24,60)==120 and 36*48==1728
P.R('0003',**T('ebk-tanim'),zorluk='orta',alt='EBOB – EKOK Kavramı',kazanim='EBOB’u ve toplamı verilen iki sayıyı EBOB × m biçiminde yazar; olası ikilileri tarayıp EKOK’un en büyük değerini bulur.',kalip='düz',adim=3,
 kart='K-EBK-01 (a = d × m, b = d × n) · yeni koşul (toplam 84, iki basamaklı), yeni istenen (EKOK’un en büyük değeri)',
 metin='a ve b iki basamaklı doğal sayılar ve a < b olmak üzere\nEBOB(a, b) = 12\na + b = 84\nolduğuna göre EKOK(a, b) en çok kaçtır?',
 **SK(144,{12:('dikkat','12, EBOB’un kendisi; soru EKOK’u soruyor.'),72:('dikkat','72, EKOK’un en küçük değeri (12 ve 72 için); soru en büyüğünü soruyor.'),
           120:('islem','24 ve 60 ikilisinin EKOK’u; 36 ve 48 daha büyük EKOK verir.'),1728:('bilgi','36 × 48 çarpımını EKOK sanmak; EKOK = çarpım ÷ EBOB.')}),
 istenen='EKOK(a, b)’nin alabileceği en büyük değer.',
 ipuclari=['a = 12 × m ve b = 12 × n yaz; m ile n’nin ortak böleni olmamalı.','a + b = 84 ise m + n kaçtır?','Olası (m, n) ikililerinde EKOK = 12 × m × n’yi karşılaştır.'],bilgi=[EBOB,EBEK],
 adimlar=[A('Sayıları yaz','EBOB 12 olduğundan iki sayı da 12’nin katı; m ile n’nin ortak böleni yok.','a = 12m · b = 12n · m < n'),
          A('m + n','Toplamdan.','12 × (m + n) = 84 ⇒ m + n = 7'),
          A('İkililer','m + n = 7 olan ikililer: (1, 6), (2, 5), (3, 4). Hepsinde sayılar iki basamaklı.','(12, 72); (24, 60); (36, 48)'),
          A('EKOK','EKOK = 12 × m × n; en büyük çarpım 3 × 4 = 12.','12 × 1 × 6 = 72 · 12 × 2 × 5 = 120 · 12 × 3 × 4 = 144')],
 puf='EBOB’u bilinen sayıları EBOB × m biçiminde yaz; geriye yalnız m ve n’yi taramak kalır.')
v=[(a,b) for a in range(10,100) for b in range(a+1,100) if gcd(a,b)==9 and a+b==90]; assert v==[(27,63)] and lcm(27,63)==189 and 27*63==1701 and lcm(18,72)==72 and lcm(9,81)==81
P.K('0003',metin='m ve n iki basamaklı doğal sayılar ve m < n olmak üzere\nEBOB(m, n) = 9\nm + n = 90\nolduğuna göre EKOK(m, n) kaçtır?',
 **SK(189,{72:('bilgi','18 ve 72’yi almak; bu ikilinin EBOB’u 18 olur, 9 değil.'),81:('dikkat','9 ve 81’i almak; 9 iki basamaklı değil.'),
           90:('dikkat','90, iki sayının toplamı; soru EKOK’u soruyor.'),1701:('bilgi','27 × 63 çarpımını EKOK sanmak; EKOK = çarpım ÷ EBOB.')}),
 istenen='EKOK(m, n) değeri.',
 ipuclari=['m = 9 × x ve n = 9 × y yaz; x ile y’nin ortak böleni olmamalı.','x + y = 10 olan ikilileri listele.','İki basamaklı olma ve ortak bölen koşullarını uygula.'],bilgi=[EBOB,EBEK],
 adimlar=[A('Sayıları yaz','İkisi de 9’un katı; çarpanların ortak böleni yok.','m = 9x · n = 9y · x + y = 10'),
          A('İkilileri ele','(1, 9) ⇒ 9 iki basamaklı değil. (2, 8) ve (4, 6) ortak bölenli. (5, 5) eşit.','yalnız (3, 7)'),
          A('Sayılar','x = 3, y = 7.','m = 27 · n = 63'),
          A('EKOK','EKOK = 9 × 3 × 7.','EKOK = 189')],
 puf='Çarpanlar listesinde hem ortak bölen hem de basamak koşulunu tek tek kontrol et.')

# ===== 0004 ORTA · ebk-kare (K-EBK-03)
r=min(((s//18)*(s//24),s) for s in range(1,2000) if s%18==0 and s%24==0); assert r==(12,72)==((72//18)*(72//24),lcm(18,24)) and gcd(18,24)==6 and 18*24==432
P.R('0004',**T('ebk-kare'),zorluk='orta',alt='EKOK Problemleri',kazanim='Eş dikdörtgenlerle oluşturulacak en küçük karenin kenarını EKOK ile bulur; kullanılan parça sayısını hesaplar.',kalip='hikâyeli',adim=3,
 kart='K-EBK-03 (eş dikdörtgenlerle kare, EKOK) · yeni kurgu (afiş kartonları), istenen parça sayısı',
 metin='Kısa kenarı 18 cm, uzun kenarı 24 cm olan dikdörtgen biçimindeki eş kartonlar, hepsi aynı yönde olacak biçimde, üst üste binmeden ve aralarında boşluk kalmadan yan yana dizilerek kare biçiminde bir pano oluşturulacaktır.\nBu iş için en az kaç karton gerekir?',
 **SK(12,{6:('bilgi','EBOB’u (6) almak; karenin kenarı iki kenarın da katı olmalı, yani EKOK.'),7:('islem','Bir kenardaki 4 kartonla diğer kenardaki 3 kartonu toplamak; çarpılmalı.'),
          72:('dikkat','72, karenin bir kenarı (cm); soru karton sayısını soruyor.'),432:('dikkat','432, bir kartonun alanı (18 × 24).')}),
 istenen='Kare panoyu oluşturmak için gereken en az karton sayısı.',
 ipuclari=['Karenin kenarı hem 18’in hem 24’ün katı olmalı.','En az karton için kenar en küçük ortak kat olmalı.','Her kenarda kaç karton var? Satır ile sütun sayısını çarp.'],bilgi=[EKOK],
 adimlar=[A('Karenin kenarı','Kenar, 18’in de 24’ün de katı; en küçüğü EKOK.','EKOK(18, 24) = 72 cm'),
          A('Kenarlardaki kartonlar','Bir yönde 72 ÷ 18, öbür yönde 72 ÷ 24 karton.','72 ÷ 18 = 4 · 72 ÷ 24 = 3'),
          A('Toplam karton','Satır sayısı × sütun sayısı.','4 × 3 = 12 karton')],
 puf='Parçalardan büyük bir kare/küp kurarken kenar EKOK’tur; adet, her yöndeki sayıların çarpımıdır.')
r=min(((s//4)*(s//6)*(s//10),s) for s in range(1,1000) if s%4==0 and s%6==0 and s%10==0); assert r==(900,60) and 15*10*6==900 and 15+10+6==31 and gcd(gcd(4,6),10)==2 and 4*6*10==240
P.K('0004',metin='Boyutları 4 cm, 6 cm ve 10 cm olan dikdörtgenler prizması biçimindeki eş tahta bloklar, hepsi aynı yönde olacak biçimde ve aralarında boşluk kalmadan üst üste ve yan yana dizilerek içi dolu bir küp oluşturulacaktır.\nBu iş için en az kaç blok gerekir?',
 **SK(900,{2:('bilgi','EBOB’u (2) almak; küpün kenarı üç boyutun da katı olmalı.'),31:('islem','Üç yöndeki blok sayılarını (15, 10, 6) toplamak; çarpılmalı.'),
           60:('dikkat','60, küpün bir kenarı (cm); soru blok sayısını soruyor.'),240:('dikkat','240, bir bloğun hacmi (4 × 6 × 10).')}),
 istenen='Küpü oluşturmak için gereken en az blok sayısı.',
 ipuclari=['Küpün kenarı 4’ün, 6’nın ve 10’un ortak katı olmalı.','En küçük ortak kat kaç?','Her yönde kaç blok sığar? Üçünü çarp.'],bilgi=[EKOK],
 adimlar=[A('Küpün kenarı','Kenar üç boyutun da katı; en küçüğü EKOK.','EKOK(4, 6, 10) = 60 cm'),
          A('Her yöndeki bloklar','Kenarı her boyuta böl.','60 ÷ 4 = 15 · 60 ÷ 6 = 10 · 60 ÷ 10 = 6'),
          A('Toplam blok','Üç sayıyı çarp.','15 × 10 × 6 = 900 blok')],
 puf='Küpte üç yön vardır: her yöndeki blok sayısını bul ve üçünü çarp.')

# ===== 0005 ORTA · ebk-kalan (K-EBK-04)
v=[n for n in range(101,2000) if n%6==4 and n%8==6 and n%9==7]; assert v[0]==142==2*lcm(6,8,9)-2 and lcm(6,8,9)==72 and 72-2==70 and 6*8*9-2==430
P.R('0005',**T('ebk-kalan'),zorluk='orta',alt='EKOK Problemleri',kazanim='Kalanlar bölenden hep aynı sayı eksik olduğunda sayıyı EKOK’un katı eksi sabit biçiminde yazar; sınır koşuluyla en küçük değeri bulur.',kalip='hikâyeli',adim=3,
 kart='K-EBK-04 (kalanlar bölenden sabit eksik, EKOK − sabit) · yeni kurgu (silgi paketleri), sınır 100’den fazla',
 metin='Bir kırtasiyecinin elindeki silgiler 6’şarlı paketlere ayrıldığında 4 silgi, 8’erli paketlere ayrıldığında 6 silgi, 9’arlı paketlere ayrıldığında 7 silgi açıkta kalmaktadır.\nSilgi sayısı 100’den fazla olduğuna göre en az kaçtır?',
 **SK(142,{70:('dikkat','72 − 2 = 70’i almak; silgi sayısı 100’den fazla olmalı.'),144:('islem','EKOK’un katını bulup 2 çıkarmayı unutmak.'),
           146:('islem','2’yi çıkarmak yerine eklemek; kalanlar bölenden 2 eksik.'),430:('bilgi','EKOK yerine 6 × 8 × 9 = 432 kullanmak; ortak katların en küçüğü 72.')}),
 istenen='Silgi sayısının 100’den büyük en küçük değeri.',
 ipuclari=['Her kalan, paket boyundan kaç eksik?','Silgi sayısına 2 eklersen 6’ya, 8’e ve 9’a tam bölünür mü?','EKOK’un katlarından 2 çıkar; 100’den büyük ilk değeri seç.'],bilgi=[EKOK,B('Kalanlı bölme','bölünen = bölen × bölüm + kalan. Örnek: 22 = 6 × 3 + 4; 22 + 2 = 24, 6’nın katı')],
 adimlar=[A('Eksikler aynı','6 − 4 = 2 · 8 − 6 = 2 · 9 − 7 = 2. Silgi sayısına 2 eklenirse paketler tam dolar.','n + 2 hem 6’nın, hem 8’in, hem 9’un katı'),
          A('EKOK','n + 2, EKOK’un bir katıdır.','EKOK(6, 8, 9) = 72 ⇒ n + 2 = 72, 144, 216, …'),
          A('Sınır','n = 70, 142, 214, … ; 100’den büyük ilk değer.','n = 142'),
          A('Kontrol','142’yi üç bölene ayrı ayrı böl.','142 = 6 × 23 + 4 · 142 = 8 × 17 + 6 · 142 = 9 × 15 + 7 ✓')],
 puf='Kalanlar bölenlerden hep aynı sayı eksikse sayı “EKOK’un katı − o sayı”dır.')
v=[n for n in range(1,100) if n%4==1 and n%5==2 and n%6==3]; assert v[-1]==57==lcm(4,5,6)-3 and v==[57] and 27%4!=1
P.K('0005',metin='Bir spor kulübündeki sporcular 4’erli gruplara ayrıldığında 1, 5’erli gruplara ayrıldığında 2, 6’şarlı gruplara ayrıldığında ise 3 sporcu gruplara giremiyor.\nKulüpteki sporcu sayısı 100’den az olduğuna göre en çok kaçtır?',
 **SK(57,{27:('bilgi','EKOK’u 30 sanıp 30 − 3 yazmak; 4, 5 ve 6’nın EKOK’u 60.'),60:('dikkat','EKOK’u bulup 3 çıkarmamak; 60 sporcu gruplara tam dağılır.'),
          63:('islem','3’ü çıkarmak yerine eklemek; kalanlar gruplardan 3 eksik.'),117:('dikkat','120 − 3 = 117 almak; sporcu sayısı 100’den az olmalı.')}),
 istenen='Sporcu sayısının 100’den küçük en büyük değeri.',
 ipuclari=['Her durumda gruba giremeyen sayı, grup büyüklüğünden kaç eksik?','Sporcu sayısına 3 eklersen ne olur?','EKOK’un katlarından 3 çıkar; 100’den küçük en büyüğünü seç.'],bilgi=[EKOK,B('Kalanlı bölme','bölünen = bölen × bölüm + kalan. Örnek: 13 = 4 × 3 + 1; 13 + 3 = 16, 4’ün katı')],
 adimlar=[A('Eksikler aynı','4 − 1 = 3 · 5 − 2 = 3 · 6 − 3 = 3.','n + 3 hem 4’ün, hem 5’in, hem 6’nın katı'),
          A('EKOK','n + 3, EKOK’un bir katı.','EKOK(4, 5, 6) = 60 ⇒ n + 3 = 60, 120, …'),
          A('Sınır','n = 57, 117, … ; 100’den küçük olan yalnız 57.','n = 57'),
          A('Kontrol','57’yi üç bölene ayrı ayrı böl.','57 = 4 × 14 + 1 · 57 = 5 × 11 + 2 · 57 = 6 × 9 + 3 ✓')],
 puf='“Gruba giremeyen” sayılar gruptan hep aynı kadar eksikse o eksiği ekle; sonuç EKOK’un katı olur.')

# ===== 0006 ORTA · ebk-periyot (K-EBK-05)
v=[t for t in range(0,1801) if t%12==0 and t%18==0 and t%30==0]; assert len(v)==11 and lcm(12,18,30)==180 and 1800//360+1==6
P.R('0006',**T('ebk-periyot'),zorluk='orta',alt='Periyodik Problemler',kazanim='Farklı aralıklarla tekrar eden olayların belli bir sürede kaç kez birlikte gerçekleştiğini EKOK ile sayar; başlangıç ve bitiş anlarını doğru dahil eder.',kalip='hikâyeli',adim=3,
 kart='K-EBK-05 (periyodik buluşma, sayım) · yeni kurgu (yanıp sönen ışıklar), saniye–dakika dönüşümü',
 metin='Bir binanın cephesindeki üç ışıktan birincisi 12 saniyede bir, ikincisi 18 saniyede bir, üçüncüsü 30 saniyede bir yanmaktadır. Üç ışık saat tam 10.00’da aynı anda yanmıştır.\nBuna göre saat 10.00 ile 10.30 arasında, bu iki an da dahil olmak üzere, üç ışık birlikte kaç kez yanar?',
 **SK(11,{3:('dikkat','3, EKOK’un dakika karşılığı; soru birlikte yanma sayısını soruyor.'),6:('islem','EKOK’u 6 dakika (360 s) sanıp 30 ÷ 6 + 1 hesaplamak; EKOK 180 s.'),
          9:('dikkat','Hem 10.00’daki hem 10.30’daki yanmayı saymamak; iki an da dahil.'),10:('dikkat','10.00’daki ilk yanmayı saymamak; bu an dahil.')}),
 istenen='10.00–10.30 arasında (uçlar dahil) üç ışığın birlikte yanma sayısı.',
 ipuclari=['Üç ışık kaç saniyede bir birlikte yanar?','30 dakika kaç saniyedir?','Birlikte yanma anlarını 10.00’dan başlayarak say; ilk anı unutma.'],bilgi=[EKOK,B('Dakika ve saniye','1 dakika = 60 saniye. Örnek: 180 s = 3 dk')],
 adimlar=[A('Ortak aralık','Üçünün birlikte yanması EKOK’ta tekrarlanır.','EKOK(12, 18, 30) = 180 s = 3 dk'),
          A('Aralık sayısı','30 dakikada kaç tane 3 dakikalık aralık var?','30 ÷ 3 = 10 aralık'),
          A('Yanma sayısı','10.00’daki ilk yanma da sayılır: aralık sayısı + 1.','10.00, 10.03, …, 10.30 ⇒ 10 + 1 = 11')],
 puf='Belli bir sürede kaç kez buluşulduğunu sayarken başlangıç anı dahilse aralık sayısına 1 ekle.')
v=[t for t in range(0,15*60+1) if t%15==0 and t%20==0 and t%25==0]; assert len(v)==4 and lcm(15,20,25)==300 and 900//60+1==16 and 900//5+1==181
P.K('0006',metin='Bir duraktan A hattının otobüsleri 15 dakikada bir, B hattının otobüsleri 20 dakikada bir, C hattının otobüsleri 25 dakikada bir kalkmaktadır. Üç hattın otobüsleri saat 07.00’de aynı anda kalkmıştır.\nBuna göre 07.00 ile 22.00 arasında, bu iki saat de dahil olmak üzere, üç hattın otobüsleri kaç kez aynı anda kalkar?',
 **SK(4,{2:('dikkat','07.00 ve 22.00’deki kalkışları saymamak; iki saat de dahil.'),3:('dikkat','07.00’deki ilk kalkışı saymamak.'),
         16:('islem','Yalnız A ile B’nin EKOK’unu (60 dk) almak; C hattı da hesaba katılmalı.'),181:('bilgi','EBOB’u (5 dk) almak; birlikte kalkış EKOK’ta tekrarlanır.')}),
 istenen='07.00–22.00 arasında (uçlar dahil) birlikte kalkış sayısı.',
 ipuclari=['Üç hat kaç dakikada bir birlikte kalkar?','07.00 ile 22.00 arasında kaç dakika var?','İlk kalkışı da sayarak birlikte kalkış saatlerini yaz.'],bilgi=[EKOK,B('Saat ve dakika','1 saat = 60 dakika. Örnek: 300 dk = 5 saat')],
 adimlar=[A('Ortak aralık','Birlikte kalkışlar EKOK’ta tekrarlanır.','EKOK(15, 20, 25) = 300 dk = 5 saat'),
          A('Süre','07.00’den 22.00’ye 15 saat.','15 ÷ 5 = 3 aralık'),
          A('Kalkış sayısı','İlk kalkış dahil: aralık sayısı + 1.','07.00, 12.00, 17.00, 22.00 ⇒ 4')],
 puf='Buluşma anlarını tek tek yazmak, “+1”i unutmamanın en güvenli yoludur.')

# ===== 0007 ZOR · ebk-parca (K-EBK-02)
r=[((156//d+1)*(108//d+1),d) for d in range(1,109) if 156%d==0 and 108%d==0]; assert min(r)==(140,12) and max(d for _,d in r)==12
assert (13,9)==(156//12,108//12) and 13*9==117 and 2*(13+9)==44 and 13*10==130 and (156//6+1)*(108//6+1)==513
P.R('0007',**T('ebk-parca'),zorluk='zor',alt='EBOB Problemleri',kazanim='Dikdörtgen bir alanı olabildiğince büyük eş karelere ayırmak için EBOB’u kullanır; ızgaradaki köşe noktalarını sayar.',kalip='hikâyeli',adim=4,
 kart='K-EBK-02 (EBOB ile eş kareler) · yeni kurgu (arsa ve parsel köşelerine direk), istenen köşe noktası sayısı',
 metin='Kenar uzunlukları 156 m ve 108 m olan dikdörtgen biçimindeki bir arsa, olabildiğince büyük eş karesel parsellere ayrılacaktır. Parsellerin kenar uzunlukları metre cinsinden tam sayıdır.\nHer parselin her köşesine bir direk dikilecek, birden fazla parselin ortak köşesine yalnızca bir direk dikilecektir.\nBuna göre toplam kaç direk dikilir?',
 **SK(140,{44:('dikkat','Yalnız arsanın sınırındaki direkleri saymak; içteki köşeler de direk alır.'),117:('dikkat','117, parsel sayısı (13 × 9); direkler köşelere dikiliyor.'),
           130:('islem','Bir yönde +1’i unutup 13 × 10 hesaplamak; iki yönde de nokta sayısı parsel sayısından 1 fazla.'),513:('bilgi','Parsel kenarını 6 m almak; parseller olabildiğince büyük olmalı, kenar EBOB = 12 m.')}),
 istenen='Dikilen toplam direk sayısı.',
 ipuclari=['Karenin kenarı iki kenarı da tam bölmeli ve olabildiğince büyük olmalı.','Uzun kenarda kaç parsel, kısa kenarda kaç parsel var?','Bir sırada n parsel varsa o sırada kaç köşe noktası olur?'],bilgi=[EBOB,B('Sıradaki noktalar','yan yana n parsel varsa uçlar dahil n + 1 köşe noktası olur. Örnek: 3 parsel ⇒ 4 nokta')],
 adimlar=[A('Parsel kenarı','Kenar 156’yı ve 108’i bölmeli, en büyük olmalı.','EBOB(156, 108) = 12 m'),
          A('Parsel sayıları','Her kenarı 12’ye böl.','156 ÷ 12 = 13 · 108 ÷ 12 = 9'),
          A('Nokta sayıları','Her yönde köşe sayısı parsel sayısından 1 fazla.','13 + 1 = 14 · 9 + 1 = 10'),
          A('Direkler','Izgaradaki tüm köşe noktaları.','14 × 10 = 140 direk',izgara(13,9))],
 puf='Izgarada köşe sayısı her yönde parsel sayısından 1 fazladır; parsel sayısıyla direk sayısını karıştırma.')
r=[((120//d-1)*(84//d-1),d) for d in range(1,85) if 120%d==0 and 84%d==0]; dmax=max(d for _,d in r); assert dmax==12 and (120//12,84//12)==(10,7)
assert 9*6==54 and 2*(10+7)==34 and 11*8==88 and 88-34==54 and 10*7==70 and (120//6+1)*(84//6+1)==315
P.K('0007',metin='Kenar uzunlukları 120 m ve 84 m olan dikdörtgen biçimindeki bir tarla, kenar uzunlukları metre cinsinden tam sayı olan, olabildiğince büyük eş karesel bölümlere ayrılacaktır.\nBölümlerin her köşesine bir sulama borusu yerleştirilecek, ortak köşelere tek boru konulacaktır.\nBuna göre tarlanın sınırı üzerinde olmayan kaç sulama borusu vardır?',
 **SK(54,{34:('dikkat','34, tarlanın sınırındaki boru sayısı; soru sınırda olmayanları soruyor.'),70:('dikkat','70, bölüm sayısı (10 × 7); borular köşelere yerleştiriliyor.'),
          88:('dikkat','88, bütün boruların sayısı; sınırdaki 34 boru çıkarılmalı.'),315:('bilgi','Bölüm kenarını 6 m alıp tüm köşeleri saymak; kenar EBOB = 12 m olmalı.')}),
 istenen='Tarlanın sınırında olmayan boru sayısı.',
 ipuclari=['Bölümlerin kenarı iki kenarı da bölen en büyük sayı.','Her yönde kaç bölüm var? Sınırdaki köşeler bu sayılardan nasıl etkilenir?','Bir sırada n bölüm varsa sınırda olmayan kaç iç köşe vardır?'],bilgi=[EBOB,B('Sıradaki iç noktalar','yan yana n bölüm varsa uçlar dahil n + 1, uçlar hariç n − 1 köşe noktası olur. Örnek: 4 bölüm ⇒ 3 iç nokta')],
 adimlar=[A('Bölüm kenarı','Kenar 120’yi ve 84’ü bölmeli, en büyük olmalı.','EBOB(120, 84) = 12 m'),
          A('Bölüm sayıları','Her kenarı 12’ye böl.','120 ÷ 12 = 10 · 84 ÷ 12 = 7'),
          A('İç noktalar','Sınır dışındaki köşeler her yönde bölüm sayısından 1 eksik.','10 − 1 = 9 · 7 − 1 = 6'),
          A('İç borular','İç noktaların sayısı.','9 × 6 = 54 boru',izgara(10,7,ic=True)),
          A('Kontrol','Tüm köşeler − sınırdakiler.','11 × 8 = 88 · 88 − 34 = 54 ✓')],
 puf='Izgarada tüm noktalar (n + 1) × (m + 1), iç noktalar (n − 1) × (m − 1) ile sayılır.')

# ===== 0008 ZOR · ebk-tanim (K-EBK-06)
v=[(a,b) for a in range(9,241) for b in range(a+1,241) if gcd(a,b)==8 and lcm(a,b)==240]; assert v==[(16,120),(24,80),(40,48)] and min(a+b for a,b in v)==88
assert 8+240==248 and 24+80==104 and 16+120==136
P.R('0008',**T('ebk-tanim'),zorluk='zor',alt='EBOB – EKOK Kavramı',kazanim='EBOB ve EKOK’u verilen iki sayının olası ikililerini çarpan ayırarak bulur; koşullara uyan en küçük toplamı belirler.',kalip='düz',adim=4,
 kart='K-EBK-06 (EBOB ve EKOK birlikte, m × n = EKOK ÷ EBOB) · yeni sayılar (8 ve 240), koşul: sayılar EBOB’dan büyük, istenen en küçük toplam',
 metin='a ve b, 8’den büyük doğal sayılar ve a < b olmak üzere\nEBOB(a, b) = 8\nEKOK(a, b) = 240\nolduğuna göre a + b toplamı en az kaçtır?',
 **SK(88,{11:('islem','m + n = 5 + 6’yı bulup 8 ile çarpmayı unutmak.'),104:('islem','24 ve 80 ikilisinin toplamı; 40 ve 48 daha küçük toplam verir.'),
          136:('islem','16 ve 120 ikilisinin toplamı; bu en küçük değil.'),248:('dikkat','8 ve 240’ı almak; sayılar 8’den büyük olmalı.')}),
 istenen='a + b toplamının en küçük değeri.',
 ipuclari=['a = 8 × m, b = 8 × n yaz; m ile n’nin ortak böleni olmamalı.','EKOK = 8 × m × n ise m × n kaçtır?','Sayılar 8’den büyükse m = 1 olabilir mi? Kalan ikilileri karşılaştır.'],bilgi=[EBOB,EKOK,EBEK],
 adimlar=[A('Sayıları yaz','İkisi de 8’in katı; m ile n’nin ortak böleni yok.','a = 8m · b = 8n · m < n'),
          A('m × n','EKOK = 8 × m × n.','8 × m × n = 240 ⇒ m × n = 30'),
          A('İkililer','Çarpımı 30 olan, ortak böleni olmayan ikililer: (1, 30), (2, 15), (3, 10), (5, 6). Sayılar 8’den büyük olduğundan m = 1 olmaz.','(2, 15); (3, 10); (5, 6)'),
          A('Toplamlar','a + b = 8 × (m + n).','8 × 17 = 136 · 8 × 13 = 104 · 8 × 11 = 88'),
          A('En küçük','En küçük toplam (5, 6) ikilisinden.','a = 40 · b = 48 ⇒ a + b = 88')],
 puf='Çarpımı sabit iki sayının toplamı, sayılar birbirine yaklaştıkça küçülür.')
v=[(a,b) for a in range(7,181) for b in range(a+1,181) if gcd(a,b)==6 and lcm(a,b)==180]; assert v==[(12,90),(18,60),(30,36)] and min(b-a for a,b in v)==6
assert 60-18==42 and 90-12==78 and 180-6==174
P.K('0008',metin='x ve y, 6’dan büyük doğal sayılar ve x < y olmak üzere\nEBOB(x, y) = 6\nEKOK(x, y) = 180\nolduğuna göre y − x farkı en az kaçtır?',
 **SK(6,{36:('dikkat','36, y’nin değeri; soru y − x farkını soruyor.'),42:('islem','18 ve 60 ikilisinin farkı; 30 ve 36 daha küçük fark verir.'),
         78:('dikkat','78, farkın en büyük değeri (90 − 12); soru en küçüğü soruyor.'),174:('dikkat','6 ve 180’i almak; sayılar 6’dan büyük olmalı.')}),
 istenen='y − x farkının en küçük değeri.',
 ipuclari=['x ve y’yi EBOB × m ve EBOB × n biçiminde yaz; m ile n’nin ortak böleni olmamalı.','m × n = EKOK ÷ EBOB kaçtır?','m = 1 olamaz; kalan ikililerde y − x = EBOB × (n − m)’yi karşılaştır.'],bilgi=[EBOB,EKOK,EBEK],
 adimlar=[A('Sayıları yaz','İkisi de 6’nın katı.','x = 6m · y = 6n · m < n'),
          A('m × n','EKOK = 6 × m × n.','6 × m × n = 180 ⇒ m × n = 30'),
          A('İkililer','Sayılar 6’dan büyük; m = 1 olmaz.','(2, 15); (3, 10); (5, 6)'),
          A('Farklar','y − x = 6 × (n − m).','6 × 13 = 78 · 6 × 7 = 42 · 6 × 1 = 6'),
          A('En küçük','x = 30, y = 36.','y − x = 6')],
 puf='EBOB–EKOK birlikte verilince m × n = EKOK ÷ EBOB; çarpanları sistemli listele ve koşulları ele.')

P.yaz(os.path.join(H,ONEK+'-1.json'),os.path.join(H,ONEK+'-1-kardes.json'))
