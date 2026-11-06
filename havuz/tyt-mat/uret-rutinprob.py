"""Rutin Olmayan Problemler · parti 1 (8 ana + 8 kardeş). Her soruda bütün durumlar kaba kuvvetle taranır ve tek doğru şık assert edilir."""
import sys,os,datetime
from itertools import permutations,product,combinations
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,os.path.join(H,'..'))
from ortak import *
P=Parti('rutinprob','Rutin Olmayan Problemler','prob|Rutin Olmayan Problemleri')
TT=lambda **k:k
def sirali(s):
    v=[Fr(x.replace(',','.')) for x in s]; assert v==sorted(v) and len(set(v))==5, s
    return s
def tek_dogru(siklar,dogru_mu):
    """Şıkların her birini dener; yalnız bir şıkkın doğru olduğunu kanıtlar ve harfini döndürür."""
    d=[h for h,v in zip('ABCDE',siklar) if dogru_mu(v)]; assert len(d)==1,(siklar,d); return d[0]

def tablo_svg(bas,satirlar,vurgu=None):
    """Basit çizelge. bas: başlıklar; satirlar: hücre listeleri; vurgu: vurgulanacak satır sırası."""
    n=len(bas); W=330; x0=10; cw=(W-2*x0)/n; rh=28; H_=rh*(len(satirlar)+1)+8; b=[]
    for r in range(len(satirlar)+1):
        y=4+r*rh
        if r==vurgu: b.append(f'<rect x="{x0}" y="{y}" width="{W-2*x0}" height="{rh}" style="fill:{G.ACC};stroke:none" fill-opacity=".18"/>')
    b.append(f'<rect x="{x0}" y="4" width="{W-2*x0}" height="{rh*(len(satirlar)+1)}" stroke-width="1.4"/>')
    for r in range(1,len(satirlar)+1): b.append(f'<line x1="{x0}" y1="{4+r*rh}" x2="{W-x0}" y2="{4+r*rh}" stroke-width="{1.4 if r==1 else .8}"/>')
    for c in range(1,n): b.append(f'<line x1="{x0+c*cw:.1f}" y1="4" x2="{x0+c*cw:.1f}" y2="{4+rh*(len(satirlar)+1)}" stroke-width=".8"/>')
    for c,s in enumerate(bas): b.append(G._t(x0+(c+.5)*cw,4+rh*.65,s,size=12,bold=True))
    for r,sat in enumerate(satirlar,1):
        for c,s in enumerate(sat): b.append(G._t(x0+(c+.5)*cw,4+r*rh+rh*.65,str(s),size=12,bold=(c==0),renk=(G.ACC if r==vurgu and c>0 else None)))
    return G._svg(W,H_,''.join(b))
def koltuk_svg(adlar,vurgu=None,alt=None):
    n=len(adlar); W=330; x0=12; w=(W-2*x0)/n; b=[]
    for i,a in enumerate(adlar):
        x=x0+i*w; v=(i==vurgu)
        b.append(f'<rect x="{x+3:.1f}" y="10" width="{w-6:.1f}" height="36" rx="7" stroke-width="{2.4 if v else 1.4}" {"style=%sfill:%s;stroke:%s%s" % (chr(34),G.ACC,G.ACC,chr(34)) if v else ""}/>')
        b.append(G._t(x+w/2,33,a,size=12,bold=True,renk=('#fff' if v else None)))
        b.append(G._t(x+w/2,62,str(i+1),size=11))
    if alt: b.append(G._t(W/2,84,alt,size=11))
    return G._svg(W,92 if alt else 70,''.join(b))

DILIM=B('“Bir kısmı” ifadesi','“her saat ya da saatin bir kısmı” denince başlayan her saat tam ücretlenir. Örnek: 2 saat 10 dakika = 3 dilim')
HAFTA=B('Haftanın günleri','günler 7 günde bir tekrar eder: ayın 1’i salıysa 8’i, 15’i, 22’si ve 29’u da salıdır')
PUAN=B('Lig puanı','galibiyet 3, beraberlik 1, mağlubiyet 0 puan. 4 takım birbiriyle birer kez oynarsa 4 × 3 ÷ 2 = 6 maç yapılır')
GM=B('Galibiyet = mağlubiyet','berabere bitmeyen her maçta bir takım kazanır, bir takım kaybeder; bu yüzden ligdeki toplam galibiyet sayısı toplam mağlubiyet sayısına eşittir')
DONGU=B('Döngü','bir işlem dizisi belli adımdan sonra kendini tekrar ediyorsa adım sayısını döngü uzunluğuna böl; kalan, döngüdeki sırayı verir')
SIRA=B('Sağında – hemen sağında','“A, B’nin sağında” denince A, B’nin sağındaki herhangi bir yerdedir; “hemen sağında” denince yan yanadırlar')

# ===================== 0001 kural KOLAY (otopark tarifesi)
def ucret(dk,ilk_dk,ilk,dilim_dk,dilim):
    return ilk if dk<=ilk_dk else ilk+(-(-(dk-ilk_dk)//dilim_dk))*dilim
sure=(15*60)-(9*60+40); assert sure==320 and ucret(sure,120,40,60,15)==100
assert 40+15==55 and 40+3*15==85 and 6*15==90 and 40+6*15==130
s=sirali(['55','85','90','100','130']); assert tek_dogru(s,lambda v:int(v)==ucret(sure,120,40,60,15))=='D'
P.R('0001','rt-kural','Kural ve tarife yorumlama','kolay','Kural ve tarife','Dilimli bir ücret tarifesini, “saatin bir kısmı” kuralıyla birlikte uygulayarak ödenecek tutarı bulur.','yeni nesil',2,
 'K-RT-01 (ücret tarifesi kuralı) · yeni kurgu (otopark), giriş-çıkış saatinden süre',
 'Bir otoparkın ücret tarifesi şöyledir:\n• İlk 2 saat için 40 TL\n• Sonraki her saat ya da saatin bir kısmı için 15 TL\nBu otoparka saat 09.40’ta giren bir araç saat 15.00’te çıkıyor.\nBuna göre bu aracın ödeyeceği ücret kaç TL’dir?',
 s,'D','Aracın ödeyeceği otopark ücreti.',
 ['Araç otoparkta kaç saat kaç dakika kaldı?','İlk 2 saatten sonra kalan süre kaç “saat ya da saatin bir kısmı” eder?','İlk 2 saatin ücretine ek dilimlerin ücretini ekle.'],[DILIM],
 [A('Kalış süresi','09.40’tan 15.00’e kadar.','5 saat 20 dakika'),
  A('Ek dilimler','İlk 2 saatten sonra 3 saat 20 dakika kalır; başlayan her saat tam sayılır.','3 tam saat + 20 dakika ⇒ 4 dilim'),
  A('Ücret','İlk 2 saat ve 4 ek dilim.','40 + 4 × 15 = 40 + 60 = 100 TL')],
 'Dilimli tarifelerde önce ilk dilimi düş, sonra kalan süreyi yukarı yuvarlayarak dilim say.',
 dict(A='55, ilk 2 saatten sonraki bütün süreyi bir dilim saymak.',B='85, kalan 20 dakikayı ücretlendirmemek; “saatin bir kısmı” da bir dilimdir.',
      C='90, ilk 2 saati de 15 TL’lik dilimler gibi hesaplamak (6 × 15).',E='130, ilk 2 saati düşmeden 6 dilim saymak (40 + 6 × 15).'),
 TT(A='dikkat',B='bilgi',C='dikkat',E='dikkat'))
kargo=lambda m:45 if m<=2 else 45+(-(-(Fr(m)-2)//1))*10
s=sirali(['5','6','6,5','7,5','9,5']); assert tek_dogru(s,lambda v:kargo(Fr(v.replace(',','.')))==95)=='C'
assert [kargo(Fr(v.replace(',','.'))) for v in s]==[75,85,95,105,125]
assert {m for m in [Fr(n,10) for n in range(1,150)] if kargo(m)==95}=={Fr(n,10) for n in range(61,71)}
P.K('0001','Bir kargo firmasının ücret tarifesi şöyledir:\n• İlk 2 kilogram için 45 TL\n• Sonraki her kilogram ya da kilogramın bir kısmı için 10 TL\nBir müşteri bu firmayla gönderdiği bir paket için 95 TL ödemiştir.\nBuna göre bu paketin kütlesi kaç kilogram olabilir?',
 s,'C','95 TL ödenen paketin olabilecek kütlesi.',
 ['95 TL’nin ne kadarı ilk 2 kilogram için ödendi?','Kalan tutar kaç ek dilime karşılık gelir?','Ek dilim sayısı k ise paket 2 + (k − 1) kg’dan ağır, 2 + k kg’dan hafif ya da ona eşittir.'],[B('“Bir kısmı” ifadesi','“her kilogram ya da kilogramın bir kısmı” denince başlayan her kilogram tam ücretlenir. Örnek: 3,2 kg = 4 dilim')],
 [A('Ek tutar','İlk 2 kg 45 TL.','95 − 45 = 50 TL'),
  A('Ek dilim','Her dilim 10 TL.','50 ÷ 10 = 5 dilim'),
  A('Kütle aralığı','5 ek dilim: 2 kg’ın üstünde 4 kg’dan fazla, en çok 5 kg.','6 kg < kütle ≤ 7 kg ⇒ 6,5 kg ✓')],
 'Ücretten kütleye giderken dilim sayısı bir aralık verir; sınırdaki değerleri (tam 6 kg) ayrıca kontrol et.',
 dict(A='5, ek dilimleri bulup ilk 2 kilogramı eklemeyi unutmak.',B='6, tam 6 kg için ücret 45 + 4 × 10 = 85 TL olur; 95 TL için 6 kg’ı aşmak gerekir.',
      D='7,5, kilogramın bir kısmını ücretlendirmemek; 7,5 kg için 6 ek dilim, 105 TL ödenir.',E='9,5, bütün tutarı 10 TL’lik dilimlere bölmek (95 ÷ 10); ilk 2 kg’ın ücreti farklı.'),
 TT(A='dikkat',B='dikkat',D='bilgi',E='bilgi'))

# ===================== 0002 tablo/takvim KOLAY
gun=lambda w1,n:(w1+n-1)%7   # 0 = pazartesi
cumalar=[n for n in range(1,32) if gun(1,n)==4]; assert cumalar[:3]==[4,11,18]
ornek=[datetime.date(y,m,1) for y in range(2024,2030) for m in range(1,13) if datetime.date(y,m,1).weekday()==1]
assert all([d for d in range(1,29) if datetime.date(o.year,o.month,d).weekday()==4][2]==18 for o in ornek)
s=sirali(['11','17','18','21','25']); assert tek_dogru(s,lambda v:int(v)==cumalar[2])=='C'
P.R('0002','rt-tablo','Tablo ve takvim yorumlama','kolay','Tablo ve takvim','Ayın ilk gününden haftanın günlerini 7’lik döngüyle izleyerek istenen tarihi bulur.','hikâyeli',2,
 'K-RT-02 (takvimde haftanın günleri) · yeni kurgu (kulüp toplantısı), istenen: üçüncü cuma',
 'Bir satranç kulübü her ayın üçüncü cuma günü toplanmaktadır. Ekim ayının 1’i salı günüdür.\nBuna göre kulüp ekim ayında ayın kaçında toplanır?',
 s,'C','Ekim ayının üçüncü cumasının tarihi.',
 ['Salıdan cumaya kaç gün vardır?','Ayın ilk cuması ayın kaçıdır?','Her cuma bir öncekinden 7 gün sonradır.'],[HAFTA],
 [A('İlk cuma','1’i salı ise 2’si çarşamba, 3’ü perşembe, 4’ü cumadır.','ilk cuma: 4'),
  A('Sonraki cumalar','Her hafta 7 gün ekle.','4 · 11 · 18 · 25'),
  A('Üçüncü cuma','Sıradaki üçüncü cuma.','18 Ekim')],
 'Takvim sorularında önce istenen günün ilk tarihini bul, sonra 7’şer ekle.',
 dict(A='11, ikinci cuma; soru üçüncü cumayı soruyor.',B='17, salıdan cumaya 2 gün sayıp ilk cumayı 3 bulmak.',
      D='21, üçüncü haftanın son günü (3 × 7) ile üçüncü cumayı karıştırmak.',E='25, ilk cumaya (4) üç hafta eklemek; ilk cuma zaten birinci cumadır.'),
 TT(A='dikkat',B='islem',D='bilgi',E='dikkat'))
GUN=['Pazartesi','Salı','Çarşamba','Perşembe','Cuma','Cumartesi','Pazar']
assert GUN[(0+31)%7]=='Perşembe'
ornek=[y for y in range(2000,2060) if datetime.date(y,3,1).weekday()==0]; assert ornek and all(datetime.date(y,4,1).weekday()==3 for y in ornek)
s=['Pazartesi','Salı','Çarşamba','Perşembe','Cuma']; assert tek_dogru(s,lambda v:v==GUN[(0+31)%7])=='D'
assert GUN[28%7]=='Pazartesi' and GUN[30%7]=='Çarşamba' and GUN[32%7]=='Cuma' and GUN[29%7]=='Salı'
P.K('0002','Bir okulun bahar dönemi takviminde 1 Mart pazartesi gününe denk gelmektedir. Mart ayı 31 gün çeker.\nBuna göre aynı yılın 1 Nisan günü haftanın hangi günüdür?',
 s,'D','1 Nisan’ın haftanın hangi gününe denk geldiği.',
 ['1 Mart’tan 1 Nisan’a kaç gün geçer?','Bu gün sayısı kaç tam hafta ve kaç gün eder?','Artan gün kadar pazartesiden ileri say.'],[HAFTA],
 [A('Geçen gün','1 Mart’tan 1 Nisan’a, Mart’ın gün sayısı kadar gün geçer.','31 gün'),
  A('Haftalara ayır','Tam haftalar aynı güne döndürür.','31 = 4 × 7 + 3'),
  A('Gün bul','Pazartesiden 3 gün ileri: salı, çarşamba, perşembe.','1 Nisan perşembe')],
 'Tarih farkını 7’ye böl; kalan kadar haftanın gününü ilerlet.',
 dict(A='Pazartesi, Mart’ı 4 tam hafta (28 gün) sanmak.',B='Salı, Mart’ı 29 gün sanmak.',C='Çarşamba, Mart’ı 30 gün sanmak.',E='Cuma, 1 Nisan’ı 1 Mart’tan 32 gün sonra saymak.'),
 TT(A='bilgi',B='bilgi',C='bilgi',E='islem'))

# ===================== 0003 sıralama ORTA
AD=['Ali','Berk','Cem','Ece','Yusuf']
diz=[p for p in permutations(AD) if abs(p.index('Ali')-p.index('Berk'))==1 and abs(p.index('Cem')-p.index('Ece'))==1 and p.index('Yusuf') not in (0,4)]
assert len(diz)==8 and {p[2] for p in diz}=={'Yusuf'}
s=AD[:]; assert tek_dogru(s,lambda v:all(p[2]==v for p in diz))=='E'
ornek=[p for p in diz][0]
P.R('0003','rt-siralama','Koşullu sıralama ve yerleştirme','orta','Koşullu sıralama','Yan yana oturma koşullarını iki ikili ve bir kişi olarak modelleyip tüm yerleşimleri inceleyerek zorunlu konumu bulur.','yeni nesil',3,
 'K-RT-03 (koşullu yerleştirme) · yeni kurgu (sinema koltukları), istenen: kesin konum',
 'Ali, Berk, Cem, Ece ve Yusuf bir sinemada yan yana dizili beş koltuğa birer kişi olacak biçimde oturuyor. Oturuş düzeniyle ilgili şunlar biliniyor:\n• Ali ile Berk yan yana oturuyor.\n• Cem ile Ece yan yana oturuyor.\n• Yusuf en uçtaki iki koltuktan birinde oturmuyor.\nBuna göre ortadaki koltukta kim oturur?',
 s,'E','Ortadaki (3.) koltukta oturan kişi.',
 ['Yan yana oturan iki ikiliyi birer blok gibi düşün.','Beş koltuğa iki blok (2’şer koltuk) ve bir kişi yerleşir; bu kişi hangi koltuklarda olabilir?','Yusuf uçta olamıyorsa geriye hangi koltuk kalır?'],[],
 [A('Bloklar','Ali–Berk ve Cem–Ece ikişer koltukluk iki blok; Yusuf bunların dışında kalır.','2 blok + Yusuf = 5 koltuk'),
  A('Yusuf’un yeri','Yusuf 2. ya da 4. koltukta olursa yanında yalnız bir koltuk kalır ve bir blok sığmaz. Bu yüzden Yusuf 1., 3. ya da 5. koltukta olabilir.','Yusuf: 1, 3 ya da 5'),
  A('Uç koşulu','Yusuf uçta değil; geriye ortadaki koltuk kalır.','Yusuf: 3. koltuk',koltuk_svg(list(ornek),2,'bloklar 1–2 ve 4–5 koltuklarında')),
  A('Kontrol','Bloklar 1–2 ve 4–5 koltuklarına her sırayla yerleşebilir; ortada hep Yusuf vardır.','8 farklı oturuş · ortada hep Yusuf')],
 'Yan yana olması gerekenleri blok yap; kalan boşlukların nereye düşebileceğini incelemek çoğu zaman tek yeri verir.',
 dict(A='Ali ortada olursa Berk 2. ya da 4. koltuğa oturur; geriye kalan üç koltukta Cem–Ece yan yana oturunca Yusuf uca düşer.',
      B='Berk ortada olursa Ali yanına oturur; kalan koltuklarda Cem ile Ece yan yana oturursa Yusuf’a yalnız uç koltuk kalır.',
      C='Cem ortada olursa Ece yanına oturur; Ali–Berk kalan yan yana iki koltuğa oturunca Yusuf uca düşer.',
      D='Ece ortada olursa Cem 2. ya da 4. koltuktadır; bu durumda Yusuf uçta kalmak zorundadır.'),
 TT(A='dikkat',B='dikkat',C='islem',D='islem'))
AD2=['Kerem','Leyla','Mert','Nil','Oya']
diz=[p for p in permutations(AD2) if p.index('Kerem') in (0,4) and abs(p.index('Leyla')-p.index('Kerem'))==1 and p.index('Leyla')>p.index('Mert')]
assert len(diz)==6 and {p[4] for p in diz}=={'Kerem'} and {p.index('Leyla') for p in diz}=={3}
s=AD2[:]; assert tek_dogru(s,lambda v:all(p[4]==v for p in diz))=='A'
P.K('0003','Kerem, Leyla, Mert, Nil ve Oya bir fotoğraf çekimi için yan yana tek sıra hâlinde diziliyor. Dizilişle ilgili şunlar biliniyor:\n• Kerem en solda ya da en sağda duruyor.\n• Leyla ile Kerem yan yana duruyor.\n• Leyla, Mert’in sağında duruyor (yan yana olmaları gerekmez).\nBuna göre en sağda kim durur?',
 s,'A','En sağda duran kişi.',
 ['Kerem en solda olursa Leyla nerede durur?','Bu durumda Mert, Leyla’nın solunda durabilir mi?','Kerem’in en sağda olması gerektiğini kontrol et.'],[SIRA],
 [A('Kerem solda mı?','Kerem en solda ise Leyla 2. sıradadır; Leyla’nın solunda yalnız Kerem kalır.','Mert, Leyla’nın soluna sığmaz ✗'),
  A('Kerem sağda','Kerem en sağda ise Leyla 4. sıradadır; Mert 1., 2. ya da 3. sırada olabilir.','Kerem 5. · Leyla 4.'),
  A('Sonuç','Bütün uygun dizilişlerde en sağda Kerem vardır.','6 farklı diziliş · en sağda hep Kerem')],
 'Bir uç koşulu verildiğinde iki ucu ayrı ayrı dene; birinin çelişki vermesi diğerini kesinleştirir.',
 dict(B='Leyla en sağda olamaz; Kerem uçta ve Leyla’nın yanında olduğu için Leyla 2. ya da 4. sıradadır.',C='Mert, Leyla’nın solunda durmalı; en sağdaki kişi kimsenin solunda değildir.',
      D='Nil en sağda olursa Kerem en solda kalır; o zaman Leyla 2. sırada olur ve Mert, Leyla’nın soluna sığmaz.',E='Oya en sağda olursa Kerem en solda olur; bu durumda Mert, Leyla’nın soluna sığmaz.'),
 TT(B='dikkat',C='bilgi',D='dikkat',E='islem'))

# ===================== 0004 tablo ORTA (lig tablosu)
TK='ABCD'; MAC=list(combinations(TK,2))
def lig_sonuclari(T):
    M=list(combinations(T,2))
    for s_ in product((0,1,2),repeat=len(M)):
        g={t:[0,0,0] for t in T}; bera=0
        for (x,y),r in zip(M,s_):
            if r==0: g[x][0]+=1; g[y][2]+=1
            elif r==2: g[y][0]+=1; g[x][2]+=1
            else: g[x][1]+=1; g[y][1]+=1; bera+=1
        yield {t:tuple(v) for t,v in g.items()},bera
pu=lambda v:3*v[0]+v[1]
uygun=[g for g,b in lig_sonuclari(TK) if g['A']==(2,1,0) and g['B']==(1,1,1) and g['C']==(1,0,2) and b==1]
assert uygun and {g['D'] for g in uygun}=={(1,0,2)} and {pu(g['D']) for g in uygun}=={3}
assert {pu(g['D']) for g,b in lig_sonuclari(TK) if g['A']==(2,1,0) and g['B']==(1,1,1) and g['C']==(1,0,2)}=={2,3}  # beraberlik bilgisi olmadan iki durum
s=sirali(['0','1','2','3','6']); assert tek_dogru(s,lambda v:int(v)==3)=='D'
TBL=tablo_svg(['Takım','O','G','B','M','Puan'],[['P',3,2,1,0,7],['R',3,1,1,1,4],['S',3,1,0,2,3],['T',3,'?','?','?','?']])
P.R('0004','rt-tablo','Tablo ve takvim yorumlama','orta','Tablo ve takvim','Lig tablosundaki galibiyet–mağlubiyet dengesini ve beraberlik bilgisini kullanarak eksik satırı tamamlar.','tablo',4,
 'K-RT-02 (tablodan gizli eşitlik) · yeni kurgu (dört takımlı futbol turnuvası), istenen: eksik puan',
 'P, R, S ve T takımlarının katıldığı bir futbol turnuvasında her takım diğer takımlarla birer kez oynamıştır. Galibiyete 3, beraberliğe 1 puan verilmiş, mağlubiyete puan verilmemiştir. Turnuva sonunda oluşan tablonun bir kısmı aşağıda verilmiştir (O: oynanan, G: galibiyet, B: beraberlik, M: mağlubiyet).\nTurnuvada yalnızca 1 maç berabere bittiğine göre T takımının puanı kaçtır?',
 s,'D','T takımının turnuva sonundaki puanı.',
 ['Tabloda iki takımın beraberliği var; turnuvada yalnız 1 maç berabere bittiyse bu maç hangi iki takım arasında oynanmıştır?','T’nin beraberliği olabilir mi?','Toplam galibiyet sayısı toplam mağlubiyet sayısına eşit olmalı.'],[PUAN,GM],
 [A('Beraberlik','P’nin ve R’nin birer beraberliği var; berabere biten maç yalnızca 1 olduğuna göre bu maç P–R maçıdır.','T’nin beraberlik sayısı 0'),
  A('G = M dengesi','Bilinen takımların galibiyetleri ve mağlubiyetleri.','G: 2 + 1 + 1 = 4 · M: 0 + 1 + 2 = 3'),
  A('T’nin satırı','T’nin galibiyeti g, mağlubiyeti m olsun; g + m = 3 ve toplamlar eşit olmalı.','4 + g = 3 + m ⇒ m = g + 1 ⇒ g = 1, m = 2'),
  A('Puan','1 galibiyet, 0 beraberlik.','3 × 1 + 0 = 3 puan',tablo_svg(['Takım','O','G','B','M','Puan'],[['P',3,2,1,0,7],['R',3,1,1,1,4],['S',3,1,0,2,3],['T',3,1,0,2,3]],vurgu=4))],
 'Lig tablolarında iki gizli kural vardır: toplam galibiyet = toplam mağlubiyet, her berabere maç iki takıma birer beraberlik yazar.',
 dict(A='0, T’nin bütün maçlarını kaybettiğini sanmak; o zaman toplam mağlubiyet (6) toplam galibiyetten (4) fazla olurdu.',
      B='1, T’nin bir beraberliği olduğunu sanmak; berabere biten maç P ile R arasında.',
      C='2, T’nin 2 beraberliği olduğunu sanmak; “yalnızca 1 maç berabere” bilgisi kullanılmamış.',E='6, T’nin 2 galibiyeti olduğunu sanmak; galibiyet ve mağlubiyet sayıları dengelenmiyor.'),
 TT(A='bilgi',B='dikkat',C='dikkat',E='islem'),sekil=TBL)
pts={'K':7,'L':5,'M':4,'N':0}
uygun=[b for g,b in lig_sonuclari('KLMN') if all(pu(g[t])==pts[t] for t in 'KLMN')]
assert uygun and set(uygun)=={2} and 3*6-sum(pts.values())==2
s=sirali(['2','4','6','8','16']); assert tek_dogru(s,lambda v:int(v)==2)=='A'
P.K('0004','K, L, M ve N takımlarının katıldığı bir hentbol turnuvasında her takım diğer takımlarla birer kez oynamıştır. Galibiyete 3, beraberliğe 1 puan verilmiş, mağlubiyete puan verilmemiştir. Turnuva sonunda takımların puanları aşağıdaki tabloda verilmiştir.\nBuna göre bu turnuvada kaç maç berabere bitmiştir?',
 s,'A','Turnuvada berabere biten maç sayısı.',
 ['Turnuvada toplam kaç maç oynandı?','Berabere bitmeyen bir maç toplam kaç puan dağıtır? Berabere biten bir maç kaç puan dağıtır?','Bütün maçlar galibiyetle bitseydi toplam puan kaç olurdu? Aradaki fark neyi gösterir?'],[PUAN],
 [A('Maç sayısı','4 takım birbiriyle birer kez oynar.','4 × 3 ÷ 2 = 6 maç'),
  A('Puan dağılımı','Galibiyetle biten maç 3 + 0 = 3, berabere biten maç 1 + 1 = 2 puan dağıtır. Her beraberlik toplamı 1 azaltır.','hepsi galibiyetle biterse 6 × 3 = 18'),
  A('Toplam puan','Tablodaki puanları topla.','7 + 5 + 4 + 0 = 16'),
  A('Beraberlik','Eksilen her puan bir berabere maçtır.','18 − 16 = 2 maç')],
 'Toplam puan = 3 × (maç sayısı) − (berabere maç sayısı); bu eşitlik tablodaki eksikleri hızla bulur.',
 dict(B='4, beraberlikleri takım takım saymak; her berabere maç iki takıma birer beraberlik yazar.',C='6, turnuvadaki toplam maç sayısı.',
      D='8, toplam puanı ikiye bölmek; berabere maç başına toplamdan yalnız 1 puan eksilir.',E='16, takımların toplam puanı; soru maç sayısını soruyor.'),
 TT(B='dikkat',C='dikkat',D='islem',E='dikkat'),sekil=tablo_svg(['Takım','K','L','M','N'],[['Puan',7,5,4,0]]))

# ===================== 0005 kural ORTA (sayı makinesi döngüsü)
def makine(x): return x-7 if x>10 else 2*x
cik=[]; x=25
for _ in range(40): x=makine(x); cik.append(x)
assert cik[:7]==[18,11,4,8,16,9,18] and cik[19]==11 and cik[20]==4 and cik[18]==18
d7=[25,18,11,4,8,16,9]; assert d7[20%7]==9
d5=[18,11,4,8,16]; assert d5[(20-1)%5]==16
s=sirali(['4','9','11','16','18']); assert tek_dogru(s,lambda v:int(v)==cik[19])=='C'
P.R('0005','rt-kural','Kural ve tarife yorumlama','orta','Kural ve tarife','Koşullu bir işlem kuralını tekrar tekrar uygulayıp oluşan döngüyü bulur ve kalanla istenen adımı belirler.','yeni nesil',3,
 'K-RT-01 (tekrarlanan kural, döngü) · yeni kurgu (sayı makinesi), istenen: 20. çıkış',
 'Bir sayı makinesine girilen sayı 10’dan büyükse makine bu sayıdan 7 çıkarır; sayı 10 ya da 10’dan küçükse sayıyı 2 ile çarpar. Makineden çıkan sayı tekrar makineye giriliyor ve işlem bu şekilde sürdürülüyor.\nMakineye ilk olarak 25 girildiğine göre makineden 20. kez çıkan sayı kaçtır?',
 s,'C','Makineden 20. kez çıkan sayı.',
 ['İlk birkaç çıkışı sırayla yaz.','Hangi sayı ikinci kez çıkıyor? Döngü kaç sayıdan oluşuyor?','25 döngünün içinde mi? 20’yi döngü uzunluğuna böl ve kalana bak.'],[DONGU],
 [A('Çıkışları yaz','Kuralı uygula: 25 → 18 → 11 → 4 → 8 → 16 → 9 → 18 …','1. 18 · 2. 11 · 3. 4 · 4. 8 · 5. 16 · 6. 9 · 7. 18'),
  A('Döngü','7. çıkış yine 18; 18’den başlayan 6 sayılık döngü oluştu (25 döngüde yok).','18, 11, 4, 8, 16, 9'),
  A('Kalan','20 = 6 × 3 + 2; üç tam döngüden sonra döngünün 2. sayısı.','20. çıkış = 11')],
 'Döngüde başlangıç değeri tekrar etmiyorsa onu döngüye katma; sayımı döngünün ilk elemanından başlat.',
 dict(A='4, bir adım fazla saymak (21. çıkış) ya da kalanı 3 almak.',B='9, 25’i de döngüye katıp 7 sayılık döngü sanmak (20 = 7 × 2 + 6).',
      D='16, döngüdeki 9’u atlayıp 5 sayılık döngü sanmak.',E='18, bir adım eksik saymak (19. çıkış).'),
 TT(A='islem',B='dikkat',D='islem',E='islem'))
def robot(N,cik_,in_):
    yer=0; h=0
    while True:
        h+=1; yer+=cik_
        if yer>=N: return h
        yer-=in_
assert robot(25,3,1)==12 and -(-25//3)==9 and -(-25//2)==13
s=sirali(['9','11','12','13','25']); assert tek_dogru(s,lambda v:int(v)==robot(25,3,1))=='C'
P.K('0005','Bir robot, 25 basamaklı bir merdivenin en altından başlayarak her hamlede önce 3 basamak çıkıyor, sonra 1 basamak iniyor. Robot en üst basamağa ulaştığı anda duruyor ve o hamlede inmiyor.\nBuna göre robot kaçıncı hamlesinde en üst basamağa ulaşır?',
 s,'C','Robotun en üst basamağa ulaştığı hamlenin sırası.',
 ['Tam bir hamlede robot net kaç basamak yükselir?','Son hamlede robot inmeden 3 basamak çıkar; son hamleden önce en az kaçıncı basamakta olmalı?','Kaç tam hamleden sonra bu basamağa ulaşır?'],[DONGU],
 [A('Net ilerleme','Bir tam hamle: 3 çık, 1 in.','net + 2 basamak'),
  A('Son hamle','Son hamlede 3 basamak çıkıp durur; öncesinde en az 22. basamakta olmalı.','25 − 3 = 22'),
  A('Tam hamleler','22. basamağa net 2’şerle ulaşır.','22 ÷ 2 = 11 tam hamle'),
  A('Sonuç','11 tam hamleden sonra 12. hamlede tepeye çıkar.','11 + 1 = 12 · kontrol: 22 + 3 = 25')],
 'Son adımda kural değişiyorsa (inmeden durma) son adımı ayrı düşün, öncesini net ilerlemeyle hesapla.',
 dict(A='9, inişi unutup 25 ÷ 3 ≈ 8,3’ü yukarı yuvarlamak.',B='11, tam hamle sayısını cevap sanmak; robot o anda 22. basamakta.',
      D='13, son hamlede de inildiğini varsayıp 25 ÷ 2 = 12,5’i yukarı yuvarlamak.',E='25, basamak sayısı; hamle sayısı değil.'),
 TT(A='bilgi',B='dikkat',D='bilgi',E='dikkat'))

# ===================== 0006 durum tarama ORTA
coz=[(d,y,20-d-y) for d in range(21) for y in range(21-d) if 5*d-2*y==61]; assert coz==[(13,2,5)]
assert [(d,y) for d in range(21) for y in range(21-d) if 5*d-y==61]==[(13,4)]
assert [(d,y) for d in range(40) for y in range(40) if 5*d-2*y==61 and d+y>20][0]==(15,7)
s=sirali(['1','2','4','5','7']); assert tek_dogru(s,lambda v:int(v)==coz[0][1])=='B'
P.R('0006','rt-tarama','Durum tarama, en az – en çok','orta','Durum tarama','Puan denklemini ve toplam soru sınırını birlikte kullanarak doğru-yanlış-boş sayılarını tarar.','hikâyeli',3,
 'K-RT-04 (tam sayı durumları ve sınır) · yeni kurgu (bilgi yarışması), istenen: yanlış sayısı',
 '20 sorudan oluşan bir bilgi yarışmasında her doğru cevap 5 puan kazandırmakta, her yanlış cevap 2 puan kaybettirmektedir. Boş bırakılan sorular puanı değiştirmemektedir ve her yarışmacı 0 puanla başlamaktadır.\nSelin bu yarışmada 61 puan aldığına göre kaç soruyu yanlış cevaplamıştır?',
 s,'B','Selin’in yanlış cevapladığı soru sayısı.',
 ['Doğru sayısına d, yanlış sayısına y de: puan denklemini yaz.','5d, 61’den büyük olmalı; d hangi değerlerden başlayabilir?','Her durumda d + y’nin 20’yi aşmadığını kontrol et.'],[B('Puan denklemi','toplam puan = 5 × (doğru sayısı) − 2 × (yanlış sayısı); boşlar puanı değiştirmez')],
 [A('Denklem','Doğru d, yanlış y.','5d − 2y = 61 · d + y ≤ 20'),
  A('Durumları tara','5d − 61 çift ve pozitif olmalı: d tek ve d ≥ 13.','d = 13 ⇒ y = 2 · d = 15 ⇒ y = 7'),
  A('Sınırı kontrol et','d = 15, y = 7 için 22 soru gerekir; yarışma 20 soru.','yalnız d = 13, y = 2 (boş 5) ✓')],
 'Denklemi sağlayan her durumu yaz; toplam soru gibi sınırları en sonda tek tek kontrol et.',
 dict(A='1, 61 = 5 × 12 + 1 diye düşünüp artan 1’i yanlış sayısı sanmak; yanlış cevap puanı azaltır.',C='4, yanlış başına 1 puan kaybı sanmak (5d − y = 61).',
      D='5, boş bırakılan soru sayısı; soru yanlış sayısını soruyor.',E='7, d = 15, y = 7 durumunu soru sayısı sınırını kontrol etmeden kabul etmek.'),
 TT(A='islem',C='dikkat',D='dikkat',E='dikkat'))
coz=[(d,y,25-d-y) for d in range(26) for y in range(26-d) if 4*d-y==62]; assert coz==[(16,2,7),(17,6,2)]
assert max(b for d,y,b in coz)==7 and min(b for d,y,b in coz)==2
assert max(25-d-y for d in range(26) for y in range(26-d) if 4*d+y==62)==8 and 25-16==9 and 25-62//4==10
s=sirali(['2','7','8','9','10']); assert tek_dogru(s,lambda v:int(v)==max(b for d,y,b in coz))=='B'
P.K('0006','25 sorudan oluşan bir testte her doğru cevap 4 puan kazandırmakta, her yanlış cevap 1 puan kaybettirmektedir. Boş bırakılan sorular puanı değiştirmemektedir ve test 0 puanla başlamaktadır.\nBu testten 62 puan alan Tuna en çok kaç soruyu boş bırakmış olabilir?',
 s,'B','Tuna’nın boş bıraktığı soru sayısının alabileceği en büyük değer.',
 ['Doğru sayısına d, yanlış sayısına y de; puan denklemini yaz.','4d en az kaç olmalı? d’nin alabileceği değerleri sırayla dene.','Her durumda boş sayısını (25 − d − y) bul ve 25 sınırını kontrol et.'],[B('Puan denklemi','toplam puan = 4 × (doğru sayısı) − (yanlış sayısı); boşlar puanı değiştirmez')],
 [A('Denklem','Doğru d, yanlış y.','4d − y = 62 · d + y ≤ 25'),
  A('Durumları tara','4d ≥ 62 ⇒ d ≥ 16.','d = 16 ⇒ y = 2 · d = 17 ⇒ y = 6 · d = 18 ⇒ y = 10 (28 soru ✗)'),
  A('Boşlar','Uygun iki durumda boş sayıları.','25 − 18 = 7 · 25 − 23 = 2'),
  A('En çok','İki durumdan büyük olanı.','en çok 7 boş')],
 '“En çok” sorularında bütün uygun durumları listele, sonra en büyüğünü seç.',
 dict(A='2, boş sayısının en küçük değeri; soru en çoğunu soruyor.',C='8, yanlış cevabın puan kazandırdığını sanmak (4d + y = 62).',
      D='9, yanlış cevapları da boş saymak (25 − 16).',E='10, 62 ÷ 4 ≈ 15 doğru alıp yanlışları hesaba katmamak.'),
 TT(A='dikkat',C='dikkat',D='dikkat',E='islem'))

# ===================== 0007 sıralama ZOR (öncüllü)
K6=['Arda','Bora','Can','Doruk','Emre','Fırat']
def kos7(q): return q['Bora']-q['Arda']==1 and q['Can']>3 and q['Fırat']<q['Doruk']<q['Emre'] and q['Doruk']<q['Arda']
diz=[{k:i+1 for i,k in enumerate(p)} for p in permutations(K6)]; diz=[q for q in diz if kos7(q)]
assert len(diz)==4
I_=lambda q:q['Fırat']==1; II_=lambda q:q['Can']==6; III_=lambda q:q['Doruk']==2
kesin={ad for ad,f in (('I',I_),('II',II_),('III',III_)) if all(f(q) for q in diz)}; assert kesin=={'I','III'} and any(II_(q) for q in diz)
SEC={'Yalnız I':{'I'},'Yalnız II':{'II'},'I ve II':{'I','II'},'I ve III':{'I','III'},'II ve III':{'II','III'},'I, II ve III':{'I','II','III'}}
s=['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III']; assert tek_dogru(s,lambda v:SEC[v]==kesin)=='D'
P.R('0007','rt-siralama','Koşullu sıralama ve yerleştirme','zor','Koşullu sıralama','Sıralama koşullarından ilk sıraları zorunlu kılan kişileri bulur; öncülleri bütün uygun dizilimlerde denetler.','öncüllü',5,
 'K-RT-03 (koşullu sıralama, kesinlik) · yeni kurgu (koşu yarışı), öncüllü kesinlik sorusu',
 'Arda, Bora, Can, Doruk, Emre ve Fırat’ın katıldığı bir koşu yarışında herkes farklı sürede bitirmiştir. Yarışın sonuç sıralamasıyla ilgili şunlar biliniyor:\n• Bora, Arda’dan hemen sonra bitirmiştir.\n• Can ilk üç sırada değildir.\n• Fırat Doruk’tan, Doruk da Emre’den önce bitirmiştir.\n• Doruk, Arda’dan önce bitirmiştir.\nBuna göre\nI. Fırat birinci olmuştur.\nII. Can sonuncu olmuştur.\nIII. Doruk ikinci olmuştur.\nifadelerinden hangileri kesinlikle doğrudur?',
 s,'D','Bütün uygun sıralamalarda doğru olan ifadeler.',
 ['Birinci sırada kimler olamaz? Her kişi için “ondan önce bitiren biri var mı?” diye sor.','Fırat birinci olduktan sonra ikinci sırada kim olabilir?','Kalan dört kişiyi (Arda–Bora bitişik, Can 4. ya da sonrası) yerleştirip Can’ın yerini denetle.'],[SIRA],
 [A('Birinci kim?','Doruk’tan önce Fırat var; Arda, Bora ve Emre’den önce Doruk var; Can ilk üçte değil.','birinci: Fırat ✓ (I)'),
  A('İkinci kim?','Arda, Bora ve Emre’den önce Doruk bitirmeli; Can ilk üçte olamaz.','ikinci: Doruk ✓ (III)'),
  A('Kalan sıralar','3–6. sıralarda Arda, Bora, Can, Emre; Arda–Bora bitişik, Can 4., 5. ya da 6.','Fırat, Doruk, Arda, Bora, Can, Emre · Fırat, Doruk, Arda, Bora, Emre, Can'),
  A('Diğer dizilimler','Emre 3. sırada da olabilir.','Fırat, Doruk, Emre, Arda, Bora, Can · Fırat, Doruk, Emre, Can, Arda, Bora'),
  A('II. öncül','Can bazı dizilimlerde 5. ya da 4. sırada; kesin sonuncu değil.','kesin doğrular: I ve III')],
 '“Kesinlikle doğru” sorularında bütün uygun dizilimleri çıkar; bir dizilimde bile yanlış olan ifade kesin değildir.',
 dict(A='Yalnız I, Doruk’un ikinci olmak zorunda olduğunu görmemek; Arda, Bora ve Emre’den önce bitirmesi gerekir, Can da ilk üçte değildir.',
      B='Yalnız II, bulunan bir dizilimi (Can sonuncu) kesin sanmak; Can 4. ya da 5. de olabilir.',
      C='I ve II, Can’ın sonuncu olduğu bir dizilimi kesin sanmak ve Doruk’un ikinciliğini görmemek; Fırat, Doruk, Emre, Can, Arda, Bora sıralaması da uygundur.',
      E='I, II ve III, II. öncülün yalnız bazı dizilimlerde doğru olduğunu gözden kaçırmak.'),
 TT(A='islem',B='dikkat',C='dikkat',E='dikkat'))
K6b=['K','L','M','N','P','R']
def kos7k(q): return q['L']-q['K']==1 and q['R']<q['N']<q['P'] and abs(q['M']-q['P'])==1 and q['N']<q['K']
diz=[{k:i+1 for i,k in enumerate(p)} for p in permutations(K6b)]; diz=[q for q in diz if kos7k(q)]
assert len(diz)==4
I_=lambda q:q['P']==4; II_=lambda q:q['R']==1; III_=lambda q:q['N']==2
kesin={ad for ad,f in (('I',I_),('II',II_),('III',III_)) if all(f(q) for q in diz)}; assert kesin=={'II','III'} and any(I_(q) for q in diz)
s=['Yalnız I','Yalnız II','I ve II','I ve III','II ve III']; assert tek_dogru(s,lambda v:SEC[v]==kesin)=='E'
sir=sorted([''.join(sorted(K6b,key=lambda k:q[k])) for q in diz]); assert sir==['RNKLMP','RNKLPM','RNMPKL','RNPMKL']
P.K('0007','Bir kurye K, L, M, N, P ve R paketlerini farklı zamanlarda, sırayla teslim etmiştir. Teslim sırasıyla ilgili şunlar biliniyor:\n• L paketi, K paketinden hemen sonra teslim edilmiştir.\n• R paketi N’den, N paketi de P’den önce teslim edilmiştir.\n• M ile P paketleri art arda teslim edilmiştir.\n• N paketi, K paketinden önce teslim edilmiştir.\nBuna göre\nI. P paketi dördüncü sırada teslim edilmiştir.\nII. R paketi ilk sırada teslim edilmiştir.\nIII. N paketi ikinci sırada teslim edilmiştir.\nifadelerinden hangileri kesinlikle doğrudur?',
 s,'E','Bütün uygun teslim sıralarında doğru olan ifadeler.',
 ['İlk sırada hangi paketler olamaz? Her paket için “ondan önce teslim edilmesi gereken var mı?” diye sor.','M paketi, P ile art arda olduğuna göre ilk iki sıraya girebilir mi?','Kalan sıraları (K–L bitişik, M–P bitişik) yerleştirip P’nin yerini denetle.'],[SIRA],
 [A('İlk paket','N’den önce R; K, L ve P’den önce N var. M, P ile art arda; P en erken 3. sırada olduğundan M ilk sırada olamaz.','ilk: R ✓ (II)'),
  A('İkinci paket','K, L ve P’den önce N gelmeli. M 2. sırada olursa P 3. sırada olur; R ile N’nin ikisi de P’den önce 1. sıraya sığmaz.','ikinci: N ✓ (III)'),
  A('Kalan bloklar','3–6. sıralarda iki bitişik ikili: K–L ve (M, P).','K–L önce: 3–4, ikili 5–6 · ikili önce: 3–4, K–L 5–6'),
  A('Dizilimler','İkililerin iç sırası M–P ya da P–M olabilir.','RNKLMP · RNKLPM · RNMPKL · RNPMKL'),
  A('I. öncül','P bu dizilimlerde 6., 5., 4. ya da 3. sıradadır; dördüncülük kesin değil.','kesin doğrular: II ve III')],
 'Bitişik olması gerekenleri blok yap; blokların ve iç sıralarının bütün durumlarını yazarak kesinliği denetle.',
 dict(A='Yalnız I, P’nin 4. olduğu bir dizilimi kesin sanmak; P 3., 5. ya da 6. sırada da olabilir.',B='Yalnız II, N’nin ikinci olmak zorunda olduğunu görmemek.',
      C='I ve II, P’nin dördüncü olduğu bir dizilimi kesin sanmak; RNKLMP diziliminde P altıncıdır.',D='I ve III, R’nin ilk sırada olmak zorunda olduğunu görmemek ve P’nin yerini kesin sanmak.'),
 TT(A='dikkat',B='islem',C='dikkat',D='islem'))

# ===================== 0008 durum tarama ZOR (banknotlar)
coz=[(a,b,c) for a in range(31) for b in range(31) for c in range(31) if a+b+c==30 and 5*a+10*b+20*c==400 and c>b]
assert min(a for a,b,c in coz)==6 and [x for x in coz if x[0]==6]==[(6,11,13)] and max(a for a,b,c in coz)==12
tum=[(a,b,c) for a in range(31) for b in range(31) for c in range(31) if a+b+c==30 and 5*a+10*b+20*c==400]
assert min(a for a,b,c in tum)==0 and (4,14,12) in tum
s=sirali(['0','4','6','11','12']); assert tek_dogru(s,lambda v:int(v)==min(a for a,b,c in coz))=='C'
P.R('0008','rt-tarama','Durum tarama, en az – en çok','zor','Durum tarama','Adet ve tutar denklemlerinden iki bilinmeyeni tek bilinmeyene indirir; eşitsizlik koşuluyla uygun durumları tarayıp en küçük değeri bulur.','hikâyeli',5,
 'K-RT-04 (iki denklem + eşitsizlik, en az değer) · yeni kurgu (kumbaradaki banknotlar)',
 'Bir kumbarada yalnızca 5 TL’lik, 10 TL’lik ve 20 TL’lik banknotlar vardır. Kumbarada toplam 30 banknot ve 400 TL bulunmaktadır. 20 TL’lik banknotların sayısı, 10 TL’lik banknotların sayısından fazladır.\nBuna göre kumbarada en az kaç tane 5 TL’lik banknot vardır?',
 s,'C','5 TL’lik banknot sayısının alabileceği en küçük değer.',
 ['5, 10 ve 20 TL’lik banknot sayılarına a, b, c de; adet ve tutar için iki denklem yaz.','Tutar denklemini 5’e böl ve adet denkleminden çıkar: b ile c arasında bir ilişki çıkar.','a’yı c cinsinden yaz; c > b koşulunu ve a ≥ 0, b ≥ 0 koşullarını uygula.'],[],
 [A('Denklemler','Adet ve tutar.','a + b + c = 30 · 5a + 10b + 20c = 400 ⇒ a + 2b + 4c = 80'),
  A('Çıkar','İkinci denklemden birinciyi çıkar.','b + 3c = 50 ⇒ b = 50 − 3c'),
  A('a’yı yaz','Adet denkleminde yerine koy.','a = 30 − b − c = 2c − 20'),
  A('Koşullar','a ≥ 0 ⇒ c ≥ 10 · b ≥ 0 ⇒ c ≤ 16 · c > b ⇒ c > 50 − 3c ⇒ c > 12,5.','c ∈ {13, 14, 15, 16}'),
  A('En az a','a = 2c − 20, c en küçükken en küçük.','c = 13 ⇒ a = 6, b = 11 · kontrol: 30 + 110 + 260 = 400')],
 'Üç bilinmeyen ve iki denklem varsa birini parametre seç; diğer koşullar bu parametrenin aralığını verir.',
 dict(A='0, c > b koşulunu kullanmamak; c = 10 için b = 20, yani 20 TL’likler 10 TL’liklerden az olur.',B='4, c > 12,5 koşulunu c ≥ 12 diye yuvarlamak; c = 12 için b = 14 > c.',
      D='11, bulunan durumdaki 10 TL’lik banknot sayısı; soru 5 TL’likleri soruyor.',E='12, 5 TL’lik sayısının en büyük değeri (c = 16); soru en azını soruyor.'),
 TT(A='dikkat',B='islem',D='dikkat',E='dikkat'))
coz=[(a,b,c) for a in range(41) for b in range(41) for c in range(41) if a+b+c==40 and 30*a+50*b+80*c==2200 and c>a]
assert max(b for a,b,c in coz)==30 and [x for x in coz if x[1]==30]==[(2,30,8)] and min(b for a,b,c in coz)==5
tum=[(a,b,c) for a in range(41) for b in range(41) for c in range(41) if a+b+c==40 and 30*a+50*b+80*c==2200]
assert (20,0,20) in tum and (5,25,10) in coz and 50-5*6//2==35
s=sirali(['0','5','25','30','35']); assert tek_dogru(s,lambda v:int(v)==max(b for a,b,c in coz))=='D'
P.K('0008','Bir tiyatro gösterisi için 30 TL’lik, 50 TL’lik ve 80 TL’lik biletlerden toplam 40 bilet satılmış ve 2200 TL gelir elde edilmiştir. Satılan 80 TL’lik bilet sayısı, 30 TL’lik bilet sayısından fazladır.\nBuna göre satılan 50 TL’lik bilet sayısı en çok kaçtır?',
 s,'D','50 TL’lik bilet sayısının alabileceği en büyük değer.',
 ['30, 50 ve 80 TL’lik bilet sayılarına a, b, c de; iki denklem yaz.','Tutar denklemini 10’a böl, adet denkleminin 3 katını çıkar: b ile c arasında ilişki bul.','b’yi büyütmek için c’yi küçült; ama a ≥ 0 ve c > a koşullarını unutma.'],[],
 [A('Denklemler','Adet ve tutar (10’a bölünmüş).','a + b + c = 40 · 3a + 5b + 8c = 220'),
  A('Çıkar','İkinci denklemden birincinin 3 katını çıkar.','2b + 5c = 100 ⇒ b = 50 − 2,5c (c çift)'),
  A('a’yı yaz','Adet denkleminde yerine koy.','a = 40 − b − c = 1,5c − 10'),
  A('Koşullar','a ≥ 0 ⇒ c ≥ 7 (c çift ⇒ c ≥ 8) · c > a ⇒ c < 20 · b ≥ 0 ⇒ c ≤ 20.','c ∈ {8, 10, 12, 14, 16, 18}'),
  A('En çok b','b, c en küçükken en büyük.','c = 8 ⇒ b = 30, a = 2 · kontrol: 60 + 1500 + 640 = 2200')],
 'En çok/en az sorularında parametrenin sınırını belirleyen koşulu bul; sınır değeri mutlaka denklemde kontrol et.',
 dict(A='0, c = 20 durumunu almak; o zaman a = 20 olur ve c > a koşulu bozulur.',B='5, 50 TL’lik sayısının en küçük değeri (c = 18); soru en çoğunu soruyor.',
      C='25, c’nin 10’dan başladığını sanmak; c = 8 de uygundur.',E='35, c = 6 almak; o zaman a = −1 olur, bilet sayısı negatif olamaz.'),
 TT(A='dikkat',B='dikkat',C='islem',E='dikkat'))

P.yaz(os.path.join(H,'rutinprob-1.json'),os.path.join(H,'rutinprob-1-kardes.json'))
