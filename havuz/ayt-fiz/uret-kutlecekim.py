"""AYT Fizik · Kütle Çekim Kuvveti · 20 soru (kardeş yok, ipucu 1). Şekiller TikZ; her sayı Python'da hesaplanıp assert edilir."""
import sys,os,json
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-fiz'))
import _hafif as H
from _hafif import *
from cizim import tikz_svg
from math import sqrt,cos,sin,radians
P=Parti('kutlecekim','Kütle Çekim Kuvveti','afiz|Kütle Çekim Kuvveti',ders='AYT Fizik',idon='aytfiz')
H.KONU='Kütle Çekim Kuvveti'
ALT='Kütle Çekim Kuvveti'
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip):
    kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,'ÖSYM AYT 2018–2025 Fizik (yalnız mantık) · 345 AYT Fizik Soru Bankası · MEB 12. sınıf fizik')
def q(no,**k):
    assert len(k['ip'])==1
    mk(P,no,adim=len(k['ad']),ad=k.pop('ad'),**k)
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
def fig(*parts): return tikz_svg(HEAD+'\n'.join(parts)+TAIL)
def ball(x,y,lab=None,r=.3,pos='above',fill='gray!30'):
    s=f'\\draw[thick,fill={fill}] ({x:.3f},{y:.3f}) circle ({r});'
    if lab: s+=f'\\node[{pos}=1pt] at ({x:.3f},{y+(r if pos=="above" else -r):.3f}) {{{lab}}};'
    return s
def dim(x1,y1,x2,y2,lab,pos='below'):
    return f'\\draw[<->,thin] ({x1:.3f},{y1:.3f}) -- ({x2:.3f},{y2:.3f}) node[midway,{pos}] {{{lab}}};'
def onc(truth,reasons,sira):
    def kume(l): return set(('I','II','III')) if l=='I, II ve III' else set(x for x in l.replace('Yalnız ','').replace(' ve ',' ').split())
    gercek={k for k,v in truth.items() if v}
    dog=[l for l in sira if kume(l)==gercek]; assert len(dog)==1,(sira,gercek)
    yan=[]
    for l in sira:
        if l==dog[0]: continue
        k=kume(l); c=[]
        for x in ('I','II','III'):
            if x in k and x not in gercek: c.append(f'{x}. öncülü doğru saymış, oysa yanlıştır: {reasons[x]}')
            if x in gercek and x not in k: c.append(f'{x}. öncülünü yanlış saymış, oysa doğrudur: {reasons[x]}')
        yan.append((l,' '.join(c),'bilgi'))
    ad=[A(f'{x}. öncülü incele',reasons[x],f'{x}: '+('doğru' if truth[x] else 'yanlış')) for x in ('I','II','III')]
    ad.append(A('Sonuca var','Doğru öncülleri birleştir.','Doğru: '+', '.join(x for x in ('I','II','III') if truth[x])))
    return dog[0],yan,ad
S5=['Yalnız I','Yalnız II','I ve II','I ve III','II ve III']
B_YASA=B('Newton’un kütle çekim yasası','iki cisim arasındaki çekim kuvveti F = G·m₁·m₂ / r² ile verilir: kütlelerin çarpımıyla doğru, merkezleri arasındaki uzaklığın karesiyle ters orantılıdır; kuvvetler karşılıklı, eşit büyüklükte ve zıt yönlüdür. Örnek: kütlelerden biri 5 katına, uzaklık 3 katına çıkarsa kuvvet 5/9 katı olur')
B_IVME=B('Çekim ivmesi','kütlesi M, yarıçapı R olan küresel gezegenin merkezinden r ≥ R uzaklıkta g = GM / r² dir; yüzeyde g₀ = GM / R². Örnek: kütlesi 5 katı, yarıçapı 2 katı olan gezegenin yüzey ivmesi 5/4 katıdır; ağırlık G = m·g, kütle ise her yerde aynıdır')
B_UYDU=B('Çembersel yörüngedeki uydu','çekim kuvveti merkezcil kuvvettir: v = √(GM/r), T = 2π√(r³/GM), a = GM/r². Bu büyüklükler uydunun kütlesine bağlı değildir. Örnek: yörünge yarıçapı 9 katına çıkarsa sürat 1/3 katına iner')
B_KEPLER=B('Kepler yasaları','1) Gezegenler Güneş’i bir odakta bulunduran elips yörüngede dolanır. 2) Güneş–gezegen doğrusu eşit sürelerde eşit alan tarar (açısal momentum korunur; Güneş’e yakınken hız büyüktür). 3) T² / a³ oranı aynı merkezi cismi dolanan tüm cisimler için sabittir (a: yarı büyük eksen). Örnek: yarı büyük ekseni 9 katı olan gezegenin periyodu 27 katıdır')
B_ENERJI=B('Eliptik yörüngede korunumlar','çekim potansiyel enerjisi U = −GMm/r dir ve uzaklaştıkça artar; yalnız çekim kuvveti etkiyorsa toplam mekanik enerji ve Güneş’e göre açısal momentum (L = m·v·r) sabittir. Örnek: uzaklık yarıya inerse hız 2 katına çıkar')
# ================= KARTLAR =================
kartla('K-AFKUTLE-01','Newton’un kütle çekim yasası','F = G m₁m₂ / r² ile kütle ve uzaklık değişimlerinde kuvvetin oranı bulunur; etki–tepki gereği kuvvetler eşit büyüklüktedir.','Uzaklığı karesiz kullanmak; kuvveti hafif kütleye daha az uygulanıyor sanmak.','kolay','şekilli',3,'kutle-yasa','Kütle çekim yasası ve kuvvet oranları')
kartla('K-AFKUTLE-02','Birden çok cismin çekimi','Her cismin çekim kuvveti ayrı hesaplanır, yöne göre vektörel toplanır; kuvvet sıfır olduğu noktada kuvvetler eşit ve zıttır.','Kuvvetleri skaler toplamak; uzaklığın karesini almamak.','orta','şekilli',3,'kutle-bilesim','Birden çok cismin çekim kuvveti')
kartla('K-AFKUTLE-03','Çekim ivmesi','g = GM/r² ile gezegenin kütlesi, yarıçapı ve merkezden uzaklığına göre çekim ivmesi ve ağırlık bulunur.','Yarıçapı karesiz almak; yüksekliği merkezden uzaklık sanmak; kütle ile ağırlığı karıştırmak.','orta','şekilli',3,'kutle-ivme','Çekim ivmesi ve ağırlık')
kartla('K-AFKUTLE-04','Çembersel yörüngedeki uydu','Merkezcil kuvvet çekim kuvvetine eşitlenir; v, T, a ve enerji ilişkileri yörünge yarıçapıyla ve uydunun kütlesiyle ilişkilendirilir.','v ve T’nin uydu kütlesine bağlı olduğunu sanmak; ilişkileri doğru orantı almak.','orta','şekilli',3,'kutle-uydu','Çembersel yörüngede hız, periyot ve enerji')
kartla('K-AFKUTLE-05','Kepler yasaları','Yarı büyük eksen ve periyot arasındaki T² ∝ a³ ilişkisi kullanılır; eliptik yörüngede a, en yakın ve en uzak uzaklıkların ortalamasıdır.','En uzak uzaklığı yarı büyük eksen sanmak; üssü yanlış almak.','orta','şekilli',3,'kutle-kepler','Kepler’in üçüncü yasası')
kartla('K-AFKUTLE-06','Eliptik yörüngede korunumlar','Açısal momentum (m·v·r) sabit olduğundan hız, uzaklıkla ters orantılıdır; toplam mekanik enerji sabit, potansiyel ve kinetik enerji karşılıklı değişir.','Hızı uzaklığın karesiyle ters orantılı almak; enerjinin hangi bölümünün sabit olduğunu karıştırmak.','zor','şekilli',3,'kutle-eliptik','Eliptik yörüngede hız, enerji ve açısal momentum')
kartla('K-AFKUTLE-07','Grafikle çekim ilişkileri','Grafikteki bir noktadan sabit bulunur ve g ∝ 1/r², T² ∝ r³ ilişkileriyle istenen büyüklüğe geçilir; eğim merkezi cismin kütlesiyle ters orantılıdır.','Eğimi kütleyle doğru orantılı sanmak; grafiği doğrusal okumak.','zor','grafik',3,'kutle-grafik','Çekim grafikleri')

# ================= 01 · kolay · iki durum =================
u=.62
sk=fig(f'\\node[left] at (-.55,1.5) {{Şekil I}};',ball(0,1.5,'$2m$'),ball(3*u,1.5,'$3m$'),dim(0,1.5-.45,3*u,1.5-.45,'$3r$'),
       f'\\node[left] at (-.55,-.2) {{Şekil II}};',ball(0,-.2,'$2m$'),ball(6*u,-.2,'$6m$'),dim(0,-.2-.45,6*u,-.2-.45,'$6r$'))
F1=Fr(2*3,3**2); F2=Fr(2*6,6**2); R1=F2/F1; assert R1==Fr(1,2)
assert Fr(6,3)==2 and Fr(2*6,6)/Fr(2*3,3)==1 and Fr(1,4)==Fr(9,36) and Fr(2*6*36,6*9)==8
q('0001',tipId='kutle-yasa',tip='Kütle çekim yasası ve kuvvet oranları',z='kolay',alt=ALT,kaz='Newton’un kütle çekim yasasında kütle ve uzaklık değişimini birlikte kullanarak kuvvet oranını bulur.',
 kart='K-AFKUTLE-01 (kuvvet oranı) · 2m–3m, 3r → 2m–6m, 6r',kalip='şekilli',
 metin='Şekil I’de kütleleri 2m ve 3m olan iki küçük küre, merkezleri arası uzaklık 3r olacak biçimde tutulmaktadır. Şekil II’de ise kürelerden biri 2m kütleli küre ile değiştirilmeden bırakılmış, diğeri kütlesi 6m olan bir küre ile değiştirilmiş ve merkezleri arası uzaklık 6r yapılmıştır.\nKürelerin birbirine uyguladığı çekim kuvvetinin büyüklüğü Şekil I’de F₁, Şekil II’de F₂ olduğuna göre, F₂ / F₁ oranı kaçtır?',
 dogru=Fr(1,2),yan=[(Fr(1,4),'Kütle değişimini hesaba katmamış, yalnızca uzaklığın karesini almış: 9 / 36 = 0,25.','dikkat'),(1,'Kuvveti uzaklıkla doğru orantılı değil, uzaklıkla ters orantılı (r¹) almış: (12 / 6) / (6 / 3) = 1.','islem'),(2,'Uzaklık değişimini hesaba katmamış, yalnızca kütle çarpımının oranını almış: 12 / 6 = 2.','dikkat'),(8,'Uzaklığın karesini paya yazmış: (12 · 36) / (6 · 9) = 8.','islem')],
 istenen='Kuvvetlerin oranı F₂ / F₁.',ip=['Her iki şekilde de kütle çarpımını ve uzaklığın karesini ayrı ayrı belirleyip oranla.'],
 bilgi=[B_YASA],ad=[A('Şekil I’deki kuvveti yaz','Kütlelerin çarpımı 2m · 3m, uzaklık 3r’dir.','F₁ = G · 6m² / 9r²'),A('Şekil II’deki kuvveti yaz','Kütlelerin çarpımı 2m · 6m, uzaklık 6r’dir.','F₂ = G · 12m² / 36r²'),A('Oranla','Sadeleştirince G m² / r² ortak çarpan olur.','F₂ / F₁ = (1/3) / (2/3) = 1/2 = 0,5')],
 puf='Kütle çarpımı ve uzaklığın karesi ayrı ayrı oranlanır; ikisi birlikte kuvveti belirler.',sekil=sk)

# ================= 02 · kolay · Dünya, yükseklik =================
Rr=1.0
sk=fig(f'\\draw[thick,fill=gray!25] (0,0) circle ({Rr});',f'\\node at (0,0) {{Yerküre}};',
       f'\\draw[dashed] (0,{Rr}) -- (0,{2*Rr:.2f}); \\fill (0,{2*Rr:.2f}) circle (.07); \\node[right] at (.1,{2*Rr:.2f}) {{K}};',
       f'\\draw[<->,thin] (-1.3,0) -- (-1.3,{Rr}) node[midway,left] {{$R$}}; \\draw[<->,thin] (-1.3,{Rr}) -- (-1.3,{2*Rr:.2f}) node[midway,left] {{$R$}};',
       f'\\draw[dotted] (-1.4,0) -- (-1.0,0); \\draw[dotted] (-1.4,{Rr}) -- (-.1,{Rr}); \\draw[dotted] (-1.4,{2*Rr:.2f}) -- (-.1,{2*Rr:.2f});')
g0=10; gK=Fr(g0)/4; assert gK==Fr(5,2) and Fr(g0)/2==5 and Fr(g0)/8==Fr(5,4) and g0*4==40
q('0002',tipId='kutle-ivme',tip='Çekim ivmesi ve ağırlık',z='kolay',alt=ALT,kaz='Merkezden uzaklığa bağlı çekim ivmesini g = GM/r² ile bulur.',
 kart='K-AFKUTLE-03 (yükseklikte g) · yüzeyden R yükseklik',kalip='şekilli',
 metin='Yarıçapı R olan küresel ve homojen Yerküre’nin yüzeyindeki çekim ivmesinin büyüklüğü 10 m/s² dir. Yerküre’nin yüzeyinden R kadar yüksekte bulunan K noktası şekilde gösterilmiştir.\nBuna göre, K noktasındaki çekim ivmesinin büyüklüğü kaç m/s² dir?',
 dogru=Fr(5,2),yan=[(Fr(5,4),'Çekim ivmesini uzaklığın küpüyle ters orantılı almış: 10 / 8 = 1,25.','islem'),(5,'K’nin merkezden uzaklığını 2R alıp ivmeyi uzaklıkla ters orantılı (r¹) kabul etmiş: 10 / 2 = 5.','islem'),(10,'Çekim ivmesinin yükseklikle değişmediğini sanmış.','bilgi'),(40,'Uzaklık oranının karesini ters yazmış: 10 · 4 = 40.','islem')],
 istenen='K noktasındaki çekim ivmesi (m/s²).',ip=['Çekim ivmesi hangi uzaklığa bağlıdır? Şekildeki işaretlere göre bu uzaklığı belirle.'],
 bilgi=[B_IVME],ad=[A('Merkezden uzaklığı bul','K noktası yüzeyden R yukarıdadır.','r = R + R = 2R'),A('Oranı yaz','g, r² ile ters orantılıdır.','g_K / g₀ = R² / (2R)² = 1/4'),A('Sonucu bul','Yüzey değerini oranla çarp.','g_K = 10 / 4 = 2,5 m/s²')],
 puf='Çekim ivmesinin uzaklıkla ilişkisini kullan ve uzaklığı şekilden belirle.',sekil=sk)

# ================= 03 · kolay · öncüllü Dünya–Ay =================
tr={'I':True,'II':False,'III':True}
rs={'I':'Etki–tepki ilkesi gereği Dünya ile Ay birbirine eşit büyüklükte ve zıt yönlü çekim kuvveti uygular.','II':'İvme a = F / m olduğundan kuvvetler eşitken kütlesi küçük olan Ay’ın ivmesi büyüktür; Dünya’nın ivmesi Ay’ınkinden küçüktür.','III':'Kütle çekim kuvveti bir alan kuvvetidir; cisimler birbirine değmese de etki eder.'}
S3=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III']
d,y,ad=onc(tr,rs,S3)
q('0003',tipId='kutle-yasa',tip='Kütle çekim yasası ve kuvvet oranları',z='kolay',alt=ALT,kaz='Dünya–Ay çiftinde etki–tepki ve ivme ilişkisini yorumlar.',
 kart='K-AFKUTLE-01 (etki–tepki) · Dünya–Ay çifti',kalip='öncüllü',
 metin='Dünya ile Ay arasında yalnızca birbirlerinin uyguladığı kütle çekim kuvvetleri etkili kabul edilmektedir. Dünya’nın kütlesi Ay’ın kütlesinden çok büyüktür.\nBuna göre;\nI. Dünya’nın Ay’a uyguladığı çekim kuvveti, Ay’ın Dünya’ya uyguladığı çekim kuvvetine eşit büyüklüktedir.\nII. Dünya’nın çekim kuvveti etkisindeki ivmesi, Ay’ın ivmesinden büyüktür.\nIII. Dünya ile Ay birbirine değmediği hâlde aralarında çekim kuvveti vardır.\nyargılarından hangileri doğrudur?',
 dogru=d,yan=y,sira=S3,istenen='Doğru olan yargılar.',ip=['Kuvvetin büyüklüğü ile cisimlerin ivmeleri arasındaki ilişkiyi ayrı değerlendir.'],
 bilgi=[B_YASA],ad=ad,puf='Etki–tepki çiftini ve a = F / m bağıntısını ayrı ayrı düşün.')

# ================= 04 · orta · tablo =================
sk=fig('\\draw[thick] (0,0) rectangle (6.4,2.4);','\\draw[thick] (0,.8) -- (6.4,.8); \\draw[thick] (0,1.6) -- (6.4,1.6); \\draw[thick] (1.6,0) -- (1.6,2.4); \\draw[thick] (4.0,0) -- (4.0,2.4);',
       '\\node at (.8,2.0) {Gezegen}; \\node at (2.8,2.0) {Kütle}; \\node at (5.2,2.0) {Yarıçap};',
       '\\node at (.8,1.2) {K}; \\node at (2.8,1.2) {$M$}; \\node at (5.2,1.2) {$R$};',
       '\\node at (.8,.4) {L}; \\node at (2.8,.4) {$6M$}; \\node at (5.2,.4) {$2R$};')
Gk=60; Gl=Gk*Fr(6,4); assert Gl==90 and Gk/2==30 and Gk*Fr(4,6)==40 and Gk*Fr(2,6)==20
q('0004',tipId='kutle-ivme',tip='Çekim ivmesi ve ağırlık',z='orta',alt=ALT,kaz='Gezegenlerin kütle ve yarıçapına göre yüzey çekim ivmesi oranını bulur.',
 kart='K-AFKUTLE-03 (iki gezegen, tablo) · K: M–R, L: 6M–2R',kalip='tablo',
 metin='Küresel ve homojen K ve L gezegenlerinin kütleleri ile yarıçapları şekildeki tabloda verilmiştir. K gezegeninin yüzeyinde ağırlığı 60 N olan bir cisim, kütlesi değişmeden L gezegeninin yüzeyine götürülüyor.\nBuna göre, cismin L gezegeninin yüzeyindeki ağırlığı kaç N olur?',
 dogru=90,yan=[(20,'Yüzey ivmesini yarıçapın kütleye oranıyla orantılı almış: 60 · 2 / 6 = 20 N.','islem'),(30,'Kütleyi hesaba katmayıp ivmeyi yarıçapla ters orantılı almış: 60 / 2 = 30 N.','dikkat'),(40,'Kütle ile yarıçap karesinin oranını ters almış: 60 · 4 / 6 = 40 N.','islem'),(60,'Cismin kütlesi değişmediği için ağırlığının da değişmediğini sanmış.','bilgi')],
 istenen='Cismin L gezegeninin yüzeyindeki ağırlığı (N).',ip=['Ağırlık, yüzey çekim ivmesiyle orantılıdır; ivmeyi gezegenin kütlesi ve yarıçapı belirler.'],
 bilgi=[B_IVME],ad=[A('Yüzey ivmelerini yaz','g = GM / R² olduğundan ivme kütleyle doğru, yarıçap karesiyle ters orantılıdır.','g_L / g_K = (6M / (2R)²) / (M / R²)'),A('Oranı hesapla','Sadeleştir.','g_L / g_K = 6 / 4 = 3/2'),A('Ağırlığı bul','Kütle aynı kalır, ağırlık ivmeyle orantılıdır.','G_L = 60 · 3/2 = 90 N')],
 puf='Önce ivme oranını kütle ve yarıçap karesiyle çıkar; ağırlık bu oranla değişir.',sekil=sk)

# ================= 05 · orta · sıfır kuvvet noktası =================
u=.58; n=8
sk=fig(f'\\draw[thick] (0,0) -- ({n*u:.3f},0);',ball(0,0,'$9m$',r=.34),ball(n*u,0,'$m$',r=.24),
       ''.join(f'\\draw[thin] ({i*u:.3f},-.08) -- ({i*u:.3f},.08);' for i in range(1,n)),
       dim(0,-.55,n*u,-.55,'$8d$'),
       f'\\fill[vurgu] ({3*u:.3f},0) circle (.1); \\node[above] at ({3*u:.3f},.12) {{$X$}};' if False else '')
# X cismi sağdaki m cisminden x uzaklıkta; şekil yalnız kütleleri ve toplam uzaklığı verir
x=Fr(8)/(1+3); assert x==2  # r_m / r_9m = 1/3
assert Fr(8,10)==Fr(4,5) and Fr(8)-Fr(8,10)==Fr(36,5) and Fr(8,2)==4 and Fr(8)-x==6
q('0005',tipId='kutle-bilesim',tip='Birden çok cismin çekim kuvveti',z='orta',alt=ALT,kaz='İki cismin arasındaki net kuvvetin sıfır olduğu noktayı kuvvetlerin eşitliğinden bulur.',
 kart='K-AFKUTLE-02 (sıfır kuvvet noktası) · 9m ve m, 8d',kalip='şekilli',
 metin='Kütleleri 9m ve m olan iki küçük küre, merkezleri arası 8d olacak biçimde şekildeki gibi sabitlenmiştir. Kürelerin arasında, bunları birleştiren doğru üzerindeki X noktasına kütlesi çok küçük bir cisim konuluyor ve cisme etki eden net çekim kuvvetinin sıfır olduğu görülüyor. Başka cisimlerin etkisi yoktur.\nBuna göre, X noktasının m kütleli küreye olan uzaklığı kaç d dir?',
 dogru=2,yan=[(Fr(4,5),'Kuvvetin uzaklığın karesiyle değil de kütle oranıyla (9) uzaklık oranını eşitlemiş: x = 8 / 10 = 0,8.','islem'),(4,'Net kuvveti sıfır yapan noktanın iki küre arasının ortası olduğunu sanmış.','bilgi'),(6,'Uzaklığı m kütleli küre yerine 9m kütleli küreden ölçmüş: 8 − 2 = 6.','dikkat'),(Fr(36,5),'Kütle oranıyla (9) uzaklık oranını eşitleyip uzaklığı 9m kütleli küreden ölçmüş: 8 − 0,8 = 7,2.','islem')],
 istenen='X noktasının m kütleli küreye uzaklığı (d).',ip=['Cisme etki eden iki çekim kuvvetinin zıt yönlü ve eşit büyüklükte olması gerektiğini kullan; uzaklıkları bir bilinmeyenle ifade et.'],
 bilgi=[B_YASA],ad=[A('Uzaklıkları adlandır','X, m kütleli küreden x kadar uzaktır.','m’ye uzaklık x, 9m’ye uzaklık 8 − x'),A('Kuvvetleri eşitle','Net kuvvet sıfırsa kuvvetler eşit büyüklüktedir.','G · m_x · 9m / (8 − x)² = G · m_x · m / x²'),A('Karekök al','İki tarafın karekökü uzaklık oranını verir.','3 / (8 − x) = 1 / x'),A('Çöz','Çapraz çarp.','3x = 8 − x → x = 2 d')],
 puf='Net kuvvet sıfırsa iki kuvvet için ne söylenebilir?',sekil=sk)

# ================= 06 · orta · dik üçgen =================
d_=1.1
sk=fig(f'\\draw[thick] ({2*d_:.3f},0) -- (0,0) -- (0,{d_:.3f}); \\draw (.2,0) -- (.2,.2) -- (0,.2);',
       ball(0,0,None,r=.2),'\\node[left=2pt] at (-.2,.0) {O};', '\\node[below right] at (.05,-.12) {$m$};',
       ball(2*d_,0,'$12m$',r=.3),ball(0,d_,None,r=.25),f'\\node[right=3pt] at (.25,{d_:.3f}) {{$4m$}};',
       dim(0,-.55,2*d_,-.55,'$2d$'), f'\\draw[<->,thin] (-.85,0) -- (-.85,{d_:.3f}) node[midway,left] {{$d$}};')
FA=Fr(12,4); FB=Fr(4,1); assert (FA,FB)==(3,4) and FA**2+FB**2==25
q('0006',tipId='kutle-bilesim',tip='Birden çok cismin çekim kuvveti',z='orta',alt=ALT,kaz='Birbirine dik iki çekim kuvvetinin bileşkesini bulur.',
 kart='K-AFKUTLE-02 (dik bileşke) · 12m–2d ve 4m–d',kalip='şekilli',
 metin='Kütleleri 12m ve 4m olan iki küçük küre, kütlesi m olan küçük bir cisme göre şekildeki gibi birbirine dik doğrultularda ve sırasıyla 2d, d uzaklıklarda sabitlenmiştir. Başka cisimlerin etkisi yoktur.\nBuna göre, O noktasındaki m kütleli cisme etki eden net çekim kuvvetinin büyüklüğü kaç G·m² / d² dir?',
 dogru=5,yan=[(6,'Kuvvetlerin çarpımının yarısını almış: 3 · 4 / 2 = 6.','dikkat'),(7,'Kuvvetleri dik olmalarına rağmen aritmetik toplamış: 3 + 4 = 7.','islem'),(12,'Kuvvetlerin çarpımını almış: 3 · 4 = 12.','dikkat'),(25,'Kuvvetlerin karelerini toplayıp karekökünü almayı unutmuş: 3² + 4² = 25.','islem')],
 istenen='O noktasındaki cisme etki eden net çekim kuvveti (G m² / d²).',ip=['Her kürenin cisme uyguladığı kuvveti ayrı hesapla; kuvvetlerin doğrultularının birbirine dik olduğuna dikkat et.'],
 bilgi=[B_YASA],ad=[A('12m kütleli kürenin kuvveti','Uzaklık 2d’dir.','F₁ = G · 12m · m / (2d)² = 3 G m² / d²'),A('4m kütleli kürenin kuvveti','Uzaklık d’dir.','F₂ = G · 4m · m / d² = 4 G m² / d²'),A('Bileşkeyi bul','Kuvvetler birbirine diktir.','F = √(3² + 4²) = 5 G m² / d²')],
 puf='Doğrultuları dik olan kuvvetlerin bileşkesi Pisagor ile bulunur.',sekil=sk)

# ================= 07 · orta · öncüllü gezegen =================
tr={'I':True,'II':True,'III':False}
vr=sqrt(8/2); assert vr==2 and Fr(8,4)==2
rs={'I':'g = GM / R² olduğundan yüzey çekim ivmesi 8 / 2² = 2 katıdır.','II':'Yüzeye yakın çembersel yörüngenin sürati v = √(GM / R) olduğundan oran √(8 / 2) = 2 katıdır.','III':'Kütle cismin özelliğidir ve bulunduğu yere göre değişmez; yalnızca ağırlık değişir.'}
d,y,ad=onc(tr,rs,['Yalnız I','Yalnız II','Yalnız III','I ve II','II ve III'])
q('0007',tipId='kutle-ivme',tip='Çekim ivmesi ve ağırlık',z='orta',alt=ALT,kaz='Gezegenin kütle ve yarıçap oranlarından yüzey ivmesi ve yüzeye yakın yörünge hızını yorumlar.',
 kart='K-AFKUTLE-03 (Dünya ile karşılaştırma) · 8 kat kütle, 2 kat yarıçap',kalip='öncüllü',
 metin='Küresel ve homojen bir X gezegeninin kütlesi Yerküre’nin kütlesinin 8 katı, yarıçapı ise Yerküre’nin yarıçapının 2 katıdır.\nBuna göre;\nI. X gezegeninin yüzeyindeki çekim ivmesi, Yerküre’nin yüzeyindekinin 2 katıdır.\nII. X gezegeninin yüzeyine çok yakın çembersel yörüngedeki bir uydunun sürati, Yerküre’nin yüzeyine çok yakın yörüngedeki bir uydunun süratinin 2 katıdır.\nIII. Yerküre’de kütlesi 1 kg olan bir cismin X gezegeninin yüzeyindeki kütlesi 2 kg olur.\nyargılarından hangileri doğrudur?',
 dogru=d,yan=y,sira=['Yalnız I','Yalnız II','Yalnız III','I ve II','II ve III'],istenen='Doğru olan yargılar.',ip=['Çekim ivmesi ve yüzeye yakın yörünge hızı için kütle ve yarıçapa bağlı bağıntıları ayrı ayrı yaz.'],
 bilgi=[B_IVME,B_UYDU],ad=ad,puf='Kütle ile ağırlığı ayrı değerlendir.')

# ================= 08 · orta · grafik g–r =================
gx=['\\begin{axis}[width=6.6cm,height=5.4cm,xmin=0.5,xmax=6.6,ymin=0,ymax=40,xtick={1,2,3,4,5,6},xticklabels={$R$,$2R$,$3R$,$4R$,$5R$,$6R$},ytick={0,12,24,36},grid=both,major grid style={gray!55,thin},tick label style={font=\\small},axis lines=left,xlabel={merkezden uzaklık $r$},ylabel={$g$ (m/s²)},xlabel style={font=\\small},ylabel style={font=\\small}]',
    '\\addplot[thick,vurgu,domain=1:6.5,samples=60] {36/x^2};','\\addplot[only marks,mark=*,mark size=2pt] coordinates {(1,36)};','\\end{axis}']
sk=fig(*gx)
g6=Fr(36,36); assert g6==1 and 36*Fr(1,6)==6 and 36*6==216
q('0008',tipId='kutle-grafik',tip='Çekim grafikleri',z='orta',alt=ALT,kaz='Çekim ivmesi–uzaklık grafiğinden gezegenin yüzey değerini okuyup başka bir uzaklıktaki ivmeyi bulur.',
 kart='K-AFKUTLE-07 (g–r) · yüzeyde 36 m/s², 6R',kalip='grafik',
 metin='Yarıçapı R olan küresel ve homojen bir gezegenin dışında, merkezinden r (r ≥ R) uzaklığındaki çekim ivmesinin büyüklüğünün uzaklığa göre değişimi grafikte gösterilmiştir.\nBuna göre, gezegenin merkezinden 6R uzaklıktaki çekim ivmesinin büyüklüğü kaç m/s² dir?',
 dogru=1,yan=[(Fr(36,25),'Merkezden uzaklığı 6R yerine, R’den başlayarak saydığı 5R almış: 36 / 25 = 1,44.','dikkat'),(6,'İvmeyi uzaklıkla ters orantılı (r¹) almış: 36 / 6 = 6.','islem'),(36,'Çekim ivmesinin uzaklıkla değişmediğini sanmış.','bilgi'),(216,'İvmenin uzaklıkla doğru orantılı arttığını sanmış: 36 · 6 = 216.','bilgi')],
 istenen='6R uzaklıktaki çekim ivmesi (m/s²).',ip=['Grafikte işaretli noktanın hangi uzaklığa ait olduğuna bak; çekim ivmesinin uzaklıkla değişim biçimini kullan.'],
 bilgi=[B_IVME],ad=[A('Yüzey değerini oku','Grafikte r = R noktasında ivme işaretlidir.','g(R) = 36 m/s²'),A('Oranı yaz','g, r² ile ters orantılıdır.','g(6R) / g(R) = 1 / 36'),A('Sonucu bul','Değeri oranla çarp.','g(6R) = 36 / 36 = 1 m/s²')],
 puf='Grafikteki işaretli noktayı başlangıç değeri olarak kullan.',sekil=sk)

# ================= 09 · orta · iki yörünge =================
def orbit(rs_,labs,Re=.3):
    s=f'\\draw[thick,fill=gray!25] (0,0) circle ({Re});'
    for r_ in rs_: s+=f'\\draw[thick] (0,0) circle ({r_});'
    return s
r1,r2=.45,4.05
sk=fig(orbit([r1,r2],None,Re=.2),ball(r1*cos(radians(40)),r1*sin(radians(40)),None,r=.12),f'\\node[right] at ({r1*cos(radians(40))+.1:.3f},{r1*sin(radians(40))+.12:.3f}) {{K ($m$)}};',
       ball(r2*cos(radians(130)),r2*sin(radians(130)),None,r=.14),f'\\node[left] at ({r2*cos(radians(130))-.1:.3f},{r2*sin(radians(130))+.12:.3f}) {{L ($3m$)}};',
       f'\\draw[<->,thin] (0,0) -- ({r1*cos(radians(-70)):.3f},{r1*sin(radians(-70)):.3f}); \\node[below left] at ({r1*cos(radians(-70))*.9:.3f},{r1*sin(radians(-70))*.9-.05:.3f}) {{$r$}};',
       f'\\draw[<->,thin] (0,0) -- ({r2*cos(radians(-45)):.3f},{r2*sin(radians(-45)):.3f}); \\node[above right] at ({r2*cos(radians(-45))*.6:.3f},{r2*sin(radians(-45))*.6:.3f}) {{$9r$}};')
assert 9**Fr(3,2)==27 and 9==9 and 81==9**2 and Fr(9*3,2)==Fr(27,2) and 3==9**Fr(1,2)
q('0009',tipId='kutle-uydu',tip='Çembersel yörüngede hız, periyot ve enerji',z='orta',alt=ALT,kaz='Çembersel yörüngelerdeki iki uydunun periyot oranını yarıçap oranından bulur.',
 kart='K-AFKUTLE-04 (periyot oranı) · r ve 9r',kalip='şekilli',
 metin='Yerküre çevresinde, şekilde gösterilen r ve 9r yarıçaplı çembersel yörüngelerde sırasıyla kütleleri m ve 3m olan K ve L uyduları dolanmaktadır. Yalnızca Yerküre’nin çekim kuvveti etkilidir.\nBuna göre, L uydusunun dolanım periyodunun K uydusunun dolanım periyoduna oranı T_L / T_K kaçtır?',
 dogru=27,yan=[(3,'Periyodu yarıçapın karekökü ile orantılı almış: √9 = 3.','islem'),(9,'Periyodu yörünge yarıçapıyla doğru orantılı almış: 9.','islem'),(Fr(27,2),'Üssü çarpım gibi kullanmış: 9 · 3 / 2 = 13,5.','islem'),(81,'Periyodu yarıçapın karesiyle orantılı almış: 9² = 81.','islem')],
 istenen='Dolanım periyotları oranı T_L / T_K.',ip=['Periyot neye bağlı? Çekim kuvvetini merkezcil kuvvete eşitleyerek bul.'],
 bilgi=[B_UYDU,B_KEPLER],ad=[A('Periyodun bağımlılığını bul','Çekim kuvveti merkezcil kuvvettir; uydunun kütlesi sadeleşir.','T² ∝ r³'),A('Yarıçap oranını yaz','L’nin yörünge yarıçapı K’nin 9 katıdır.','r_L / r_K = 9'),A('Oranı hesapla','Periyot oranı yarıçap oranının 3/2 kuvvetidir.','T_L / T_K = 9^(3/2) = 27')],
 puf='Periyodun bağımlılığını çekim kuvveti–merkezcil kuvvet eşitliğinden çıkar.',sekil=sk)

# ================= 10 · orta · ağırlıktan yükseklik =================
Rr=.8
sk=fig(f'\\draw[thick,fill=gray!25] (0,0) circle ({Rr});',f'\\node at (0,0) {{Yerküre}};',
       f'\\draw[dashed] (0,{Rr}) -- (0,{3*Rr:.2f}); \\fill (0,{3*Rr:.2f}) circle (.07); \\node[right] at (.1,{3*Rr:.2f}) {{K}};',
       f'\\draw[<->,thin] (-1.2,0) -- (-1.2,{Rr}) node[midway,left] {{$R$}}; \\draw[<->,thin] (-1.2,{Rr}) -- (-1.2,{3*Rr:.2f}) node[midway,left] {{$h$}};',
       f'\\draw[dotted] (-1.3,0) -- (-.9,0); \\draw[dotted] (-1.3,{Rr}) -- (-.1,{Rr}); \\draw[dotted] (-1.3,{3*Rr:.2f}) -- (-.1,{3*Rr:.2f});')
W0=360; WK=40; ratio=Fr(W0,WK); assert ratio==9 and sqrt(9)==3 and 3-1==2 and ratio-1==8 and ratio/2==Fr(9,2)
q('0010',tipId='kutle-ivme',tip='Çekim ivmesi ve ağırlık',z='orta',alt=ALT,kaz='Ağırlık oranından merkezden uzaklığı, buradan da yüzeyden yüksekliği bulur.',
 kart='K-AFKUTLE-03 (ağırlıktan yükseklik) · 360 N → 40 N',kalip='şekilli',
 metin='Yarıçapı R olan küresel ve homojen Yerküre’nin yüzeyinde ağırlığı 360 N olan bir cisim, Yerküre’nin yüzeyinden h yüksekliğindeki K noktasına çıkarılıyor ve burada ağırlığının 40 N olduğu görülüyor.\nBuna göre, h yüksekliği kaç R dir?',
 dogru=2,yan=[(3,'Merkezden uzaklığı (3R) yüzeyden yükseklik sanmış.','dikkat'),(Fr(9,2),'Ağırlık oranının (9) uzaklığın karesiyle değil, ikiyle ters orantılı olduğunu sanıp 9 / 2 = 4,5 bulmuş.','islem'),(8,'Ağırlık oranından (9) 1 çıkararak yüksekliği bulmuş.','islem'),(9,'Ağırlık oranını (9) doğrudan yükseklik sanmış.','bilgi')],
 istenen='K noktasının yüzeyden yüksekliği h (R cinsinden).',ip=['Ağırlık oranını çekim ivmesi oranına, ondan da uzaklık oranına çevir; şekilde h’nin nereden ölçüldüğüne bak.'],
 bilgi=[B_IVME],ad=[A('Ağırlık oranını yaz','Kütle sabit olduğundan oran çekim ivmesi oranıdır.','G₀ / G_K = 360 / 40 = 9'),A('Uzaklık oranını bul','g, merkezden uzaklığın karesiyle ters orantılıdır.','(r / R)² = 9 → r = 3R'),A('Yüksekliği bul','Yükseklik yüzeyden ölçülür.','h = r − R = 2R')],
 puf='Oranları sırayla kur: ağırlık, ivme, uzaklık, yükseklik.',sekil=sk)

# ================= 11 · orta · Kepler 3, elips =================
def ellipse(a,c,b,u,kl,ll,kdim,ldim):
    s=f'\\draw[thick] (0,0) ellipse ({a*u:.3f} and {b*u:.3f});'
    s+=f'\\draw[thick,fill=vurgu!30] ({c*u:.3f},0) circle (.13); \\node[above=2pt] at ({c*u:.3f},.1) {{G}};'
    s+=f'\\fill ({a*u:.3f},0) circle (.07); \\node[right] at ({a*u+.1:.3f},0) {{{kl}}};'
    s+=f'\\fill ({-a*u:.3f},0) circle (.07); \\node[left] at ({-a*u-.1:.3f},0) {{{ll}}};'
    yb=-b*u-.45
    s+=dim(-a*u,yb,c*u,yb,ldim)+dim(c*u,yb,a*u,yb,kdim,'above' if False else 'below')
    s+=f'\\draw[dotted] ({-a*u:.3f},0) -- ({-a*u:.3f},{yb:.3f}); \\draw[dotted] ({c*u:.3f},0) -- ({c*u:.3f},{yb:.3f}); \\draw[dotted] ({a*u:.3f},0) -- ({a*u:.3f},{yb:.3f});'
    return s
a11=Fr(1+7,2); T11=a11**Fr(3,2); assert a11==4 and T11==8
assert 7==7 and 4**2==16 and 4**3==64
sk=fig(ellipse(4,3,sqrt(7),.62,'K','L','$1$ AU','$7$ AU'))
q('0011',tipId='kutle-kepler',tip='Kepler’in üçüncü yasası',z='orta',alt=ALT,kaz='Eliptik yörüngenin yarı büyük eksenini en yakın ve en uzak uzaklıklardan bulup Kepler’in üçüncü yasasıyla periyodu hesaplar.',
 kart='K-AFKUTLE-05 (eliptik yörünge) · 1 AU ve 7 AU',kalip='şekilli',
 metin='Güneş’in (G) odaklardan birinde bulunduğu eliptik bir yörüngede dolanan bir kuyruklu yıldız, Güneş’e en yakın K noktasında 1 AU, en uzak L noktasında 7 AU uzaklıktadır. Yerküre’nin Güneş etrafındaki dolanım periyodu 1 yıl ve yörünge yarıçapı 1 AU dur.\nBuna göre, kuyruklu yıldızın dolanım periyodu kaç yıldır?',
 dogru=8,yan=[(4,'Yarı büyük ekseni (4 AU) periyodun sayısal değeri almış.','dikkat'),(2,'Periyodu yarı büyük eksenin karekökü ile orantılı almış: √4 = 2.','islem'),(7,'En uzak uzaklığı (7 AU) yarı büyük eksen sanmış: T = 7 yıl.','dikkat'),(16,'T² ∝ a³ yerine T ∝ a² almış: 4² = 16.','islem')],
 istenen='Kuyruklu yıldızın dolanım periyodu (yıl).',ip=['Kepler’in üçüncü yasasında yörüngenin hangi uzunluğu kullanılır?'],
 bilgi=[B_KEPLER],ad=[A('Yarı büyük ekseni bul','Eksen uzunluğu, en yakın ve en uzak uzaklıkların toplamıdır.','2a = 1 + 7 = 8 → a = 4 AU'),A('Kepler’in üçüncü yasasını yaz','Yerküre ile oran kur (birimler yıl ve AU).','T² / a³ = 1² / 1³'),A('Periyodu bul','a değerini yerine koy.','T² = 4³ = 64 → T = 8 yıl')],
 puf='Şekildeki iki uzaklığın elipsin neresine karşılık geldiğini düşün.',sekil=sk)

# ================= 12 · zor · eliptik, açısal momentum + enerji =================
sk=fig(ellipse(2.5,1.5,2,.95,'K','L','$r$','$4r$'))
x_=Fr(3,4)/15; assert x_==Fr(1,20) and Fr(4)**2==16 and 16*x_-1==x_-Fr(1,4)
assert Fr(3,4)/3==Fr(1,4) and 16*x_==Fr(4,5)
q('0012',tipId='kutle-eliptik',tip='Eliptik yörüngede hız, enerji ve açısal momentum',z='zor',alt=ALT,kaz='Açısal momentumun ve mekanik enerjinin korunumunu birlikte kullanarak eliptik yörüngede kinetik enerjiyi bulur.',
 kart='K-AFKUTLE-06 (korunumlar birlikte) · r ve 4r',kalip='şekilli',
 metin='Kütlesi M olan Güneş’in (G) odaklardan birinde bulunduğu eliptik bir yörüngede, kütlesi m olan bir gezegen dolanmaktadır. Gezegen Güneş’e en yakın K noktasında r, en uzak L noktasında 4r uzaklıktadır. Güneş–gezegen sisteminin d uzaklığındaki çekim potansiyel enerjisi U = −G M m / d dir. Güneş dışındaki cisimlerin etkisi ihmal edilmektedir.\nBuna göre, gezegenin L noktasındaki kinetik enerjisi kaç G M m / r dir?',
 dogru=Fr(1,20),yan=[(Fr(1,16),'K’deki kinetik enerjiyi GMm / r kabul edip oranla (16) bölmüş: 1 / 16 = 0,0625.','islem'),(Fr(1,4),'Kinetik enerji oranını hız oranı (4) almış: 3x = 0,75 → x = 0,25.','islem'),(Fr(3,4),'L’deki kinetik enerjiyi potansiyel enerji farkına (1 − 1/4 = 0,75) eşitlemiş.','dikkat'),(Fr(4,5),'L yerine K noktasındaki kinetik enerjiyi bulmuş: 16 · 0,05 = 0,8.','dikkat')],
 istenen='L noktasındaki kinetik enerji (G M m / r).',ip=['Hızlar arasındaki ilişkiyi çekim kuvvetinin Güneş’e göre torkundan, enerjiler arasındaki ilişkiyi toplam enerjiden elde et.'],
 bilgi=[B_ENERJI],ad=[A('Açısal momentumu eşitle','Çekim kuvveti merkezcil olduğundan açısal momentum korunur.','m · v_K · r = m · v_L · 4r → v_K = 4 v_L'),A('Kinetik enerji oranını yaz','Kinetik enerji hızın karesiyle orantılıdır.','E_K = 16 E_L = 16x'),A('Mekanik enerji korunumunu yaz','Toplam enerji K ve L’de eşittir (birim: G M m / r).','16x − 1 = x − 1/4'),A('Çöz','Denklemden x’i bul.','15x = 3/4 → x = 0,05')],
 puf='Hız ilişkisi ve enerji ilişkisi ayrı korunumlardan gelir; ikisini sırayla kullan.',sekil=sk)

# ================= 13 · orta · öncüllü uydu kütlesi =================
tr={'I':False,'II':True,'III':True}
rs={'I':'Çembersel yörüngedeki sürat v = √(GM / r) olup uydunun kütlesine bağlı değildir; kütle 2 katına çıksa da sürat değişmez.','II':'Çekim kuvveti uydunun kütlesiyle doğru orantılıdır; kütle 2 katına çıkınca kuvvet de 2 katına çıkar.','III':'Periyot T = 2π√(r³ / GM) olup uydunun kütlesine bağlı değildir; yörünge yarıçapı aynıysa periyot değişmez.'}
d,y,ad=onc(tr,rs,S5)
q('0013',tipId='kutle-uydu',tip='Çembersel yörüngede hız, periyot ve enerji',z='orta',alt=ALT,kaz='Uydunun kütlesi değiştiğinde çekim kuvvetinin, hızın ve periyodun nasıl değiştiğini yorumlar.',
 kart='K-AFKUTLE-04 (uydu kütlesi değişimi) · kütle 2 katına çıkıyor',kalip='öncüllü',
 metin='Yerküre çevresinde r yarıçaplı çembersel yörüngede dolanan bir uydunun kütlesi, yörünge yarıçapı değişmeden fırlatılan bir ek modülün kenetlenmesiyle 2 katına çıkarılıyor. Uydu üzerinde yalnızca Yerküre’nin çekim kuvveti etkilidir.\nBuna göre, kütle artırıldıktan sonra uydu için;\nI. Çizgisel süratinin büyüklüğü 2 katına çıkar.\nII. Yerküre’nin uyguladığı çekim kuvvetinin büyüklüğü 2 katına çıkar.\nIII. Dolanım periyodu değişmez.\nyargılarından hangileri doğrudur?',
 dogru=d,yan=y,sira=S5,istenen='Doğru olan yargılar.',ip=['Çembersel yörüngede hız ve periyot bağıntılarında uydunun kütlesinin yer alıp almadığını kontrol et.'],
 bilgi=[B_UYDU],ad=ad,puf='Hız, periyot ve çekim kuvveti bağıntılarında uydunun kütlesi var mı?')

# ================= 14 · orta · öncüllü iki yörünge =================
r1,r2=1.0,2.0
sk=fig(orbit([r1,r2],None,Re=.4),ball(r1*cos(radians(65)),r1*sin(radians(65)),None,r=.12),f'\\node[right] at ({r1*cos(radians(65))+.1:.3f},{r1*sin(radians(65))+.1:.3f}) {{K ($m$)}};',
       ball(r2*cos(radians(140)),r2*sin(radians(140)),None,r=.16),f'\\node[left] at ({r2*cos(radians(140))-.1:.3f},{r2*sin(radians(140))+.1:.3f}) {{L ($2m$)}};',
       f'\\draw[<->,thin] (0,0) -- ({r1*cos(radians(-80)):.3f},{r1*sin(radians(-80)):.3f}); \\node[right] at (.05,-.6) {{$r$}};',
       f'\\draw[<->,thin] (0,0) -- ({r2*cos(radians(-40)):.3f},{r2*sin(radians(-40)):.3f}); \\node[above right] at ({r2*cos(radians(-40))*.62:.3f},{r2*sin(radians(-40))*.62:.3f}) {{$2r$}};')
# K: m, r ; L: 2m, 2r  (M=Yerküre, GM=1)
wK=1/r1**1.5; assert Fr(8,1)/Fr(1)==8 and Fr(1,1)>Fr(1,2)
FK=Fr(1,1); FL=Fr(2,4); aK=Fr(1,1); aL=Fr(1,4); EK=Fr(1,2*1); EL=Fr(2,2*2)/Fr(1)  # Ek = GMm/2r
assert FK==2*FL and aK==4*aL and EK==Fr(1,2) and EL==Fr(1,2)
tr={'I':True,'II':False,'III':True}
rs={'I':'Açısal hız ω = √(GM / r³) olduğundan yarıçapı küçük olan K’nin açısal hızı büyüktür.','II':'Çekim kuvveti m / r² ile orantılıdır: K için m / r², L için 2m / 4r² = m / 2r² olduğundan K’ye etki eden kuvvet L’ye etki edenin 2 katıdır; L’ye etki eden kuvvet daha küçüktür.','III':'Merkezcil ivme a = GM / r² olduğundan K’nin ivmesi L’ninkinin 4 katıdır.'}
d,y,ad=onc(tr,rs,['Yalnız II','I ve II','I ve III','II ve III','I, II ve III'])
q('0014',tipId='kutle-uydu',tip='Çembersel yörüngede hız, periyot ve enerji',z='orta',alt=ALT,kaz='İki uydunun açısal hız, çekim kuvveti ve merkezcil ivmesini yarıçap ve kütle oranlarına göre karşılaştırır.',
 kart='K-AFKUTLE-04 (iki uydu karşılaştırma) · (m, r) ve (2m, 2r)',kalip='öncüllü',
 metin='Yerküre çevresinde, şekilde gösterilen r ve 2r yarıçaplı çembersel yörüngelerde sırasıyla kütleleri m ve 2m olan K ve L uyduları dolanmaktadır. Uydulara yalnızca Yerküre’nin çekim kuvveti etki etmektedir.\nBuna göre;\nI. K’nin açısal hızı L’ninkinden büyüktür.\nII. Yerküre’nin L’ye uyguladığı çekim kuvvetinin büyüklüğü, K’ye uyguladığından büyüktür.\nIII. K’nin merkezcil ivmesinin büyüklüğü, L’ninkinin 4 katıdır.\nyargılarından hangileri doğrudur?',
 dogru=d,yan=y,sira=['Yalnız II','I ve II','I ve III','II ve III','I, II ve III'],istenen='Doğru olan yargılar.',ip=['Çekim kuvvetini kütle ve uzaklığa göre; açısal hızı ve merkezcil ivmeyi ise yalnız uzaklığa göre değerlendir.'],
 bilgi=[B_UYDU,B_YASA],ad=ad,puf='Açısal hız ve merkezcil ivme yalnız yarıçapa bağlıdır; çekim kuvveti kütleye de bağlıdır.',sekil=sk)

# ================= 15 · orta · öncüllü eliptik =================
tr={'I':True,'II':False,'III':False}
rs={'I':'Çekim kuvveti merkezcil olduğundan tork sıfırdır ve açısal momentum yörünge boyunca sabittir.','II':'Gezegen Güneş’ten uzaklaşırken hızı azalır, dolayısıyla kinetik enerjisi artmaz, azalır.','III':'Açısal momentum sabit ve yarıçap büyürken ω = v / r azalır; açısal hız artmaz.'}
d,y,ad=onc(tr,rs,['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III'])
q('0015',tipId='kutle-eliptik',tip='Eliptik yörüngede hız, enerji ve açısal momentum',z='orta',alt=ALT,kaz='Eliptik yörüngede gezegen Güneş’ten uzaklaşırken açısal momentum, kinetik enerji ve açısal hız değişimini yorumlar.',
 kart='K-AFKUTLE-06 (perihelden afele) · nitel',kalip='öncüllü',
 metin='Güneş etrafında eliptik bir yörüngede dolanan bir gezegen, Güneş’e en yakın noktadan en uzak noktaya doğru hareket etmektedir. Güneş dışındaki cisimlerin etkisi ihmal edilmektedir.\nBuna göre, bu hareket süresince gezegen için;\nI. Güneş’e göre açısal momentumunun büyüklüğü değişmez.\nII. Kinetik enerjisi artar.\nIII. Güneş’e göre açısal hızı artar.\nyargılarından hangileri doğrudur?',
 dogru=d,yan=y,sira=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III'],istenen='Doğru olan yargılar.',ip=['Çekim kuvvetinin Güneş’e göre torkunu düşün; hız ve yarıçap değişimini açısal momentumun korunumuyla ilişkilendir.'],
 bilgi=[B_ENERJI,B_KEPLER],ad=ad,puf='Güneş’e göre tork ve uzaklık–hız ilişkisini düşün.')

# ================= 16 · zor · T²–r³ grafiği, iki yıldız =================
gx=['\\begin{axis}[width=6.8cm,height=5.6cm,xmin=0,xmax=8.5,ymin=0,ymax=8.5,xtick distance=2,ytick distance=2,grid=both,major grid style={gray!55,thin},tick label style={font=\\small},axis lines=left,xlabel={$r^3$ (birim)},ylabel={$T^2$ (birim)},xlabel style={font=\\small},ylabel style={font=\\small}]',
    '\\addplot[thick,vurgu] coordinates {(0,0) (8,2)}; \\node[above] at (axis cs:7,1.7) {X};',
    '\\addplot[thick,dashed] coordinates {(0,0) (8,8)}; \\node[above left] at (axis cs:7.2,7.2) {Y};',
    '\\addplot[only marks,mark=*,mark size=2pt] coordinates {(8,2) (2,2)};','\\end{axis}']
sk=fig(*gx)
sX=Fr(2,8); sY=Fr(2,2); MX_MY=sY/sX; assert sX==Fr(1,4) and sY==1 and MX_MY==4
vr=Fr(2); assert vr**2==MX_MY and Fr(1,2)**2==Fr(1,4)
q('0016',tipId='kutle-grafik',tip='Çekim grafikleri',z='zor',alt=ALT,kaz='T²–r³ grafiklerinin eğiminden merkezi cisimlerin kütle oranını, buradan da aynı yarıçaplı yörüngelerdeki sürat oranını bulur.',
 kart='K-AFKUTLE-07 (iki yıldız, T²–r³) · eğimler 1/4 ve 1',kalip='grafik',
 metin='X ve Y yıldızlarını çembersel yörüngelerde dolanan gezegenlerin periyotlarının karesinin (T²), yörünge yarıçaplarının küpüne (r³) göre değişimi grafikte verilmiştir. Gezegenlere yalnızca bağlı oldukları yıldızın çekim kuvveti etki etmektedir.\nBuna göre, aynı r yarıçaplı çembersel yörüngelerde X ve Y yıldızlarını dolanan gezegenlerin süratleri oranı v_X / v_Y kaçtır?',
 dogru=2,yan=[(Fr(1,4),'Eğimlerin oranını (1/4) doğrudan sürat oranı almış.','islem'),(Fr(1,2),'Kütle oranını (4) bulup süratin √M ile ters orantılı olduğunu sanmış: v_X / v_Y = 1/2.','bilgi'),(4,'Kütle oranını (4) sürat oranı olarak yazmış.','dikkat'),(16,'Sürat oranını kütle oranının karesi almış: 4² = 16.','islem')],
 istenen='Süratler oranı v_X / v_Y.',ip=['Grafiğin eğimini merkezi cismin kütlesiyle ilişkilendirmek için T² / r³ oranının neye eşit olduğunu yaz; sonra aynı yarıçapta sürat bağıntısını kullan.'],
 bilgi=[B_KEPLER,B_UYDU],ad=[A('Eğimleri oku','İşaretli noktalardan her doğrunun eğimini bul.','X: 2 / 8 = 1/4, Y: 2 / 2 = 1'),A('Kütle oranını bul','T² / r³ = 4π² / GM olduğundan eğim kütleyle ters orantılıdır.','M_X / M_Y = 1 / (1/4) = 4'),A('Sürat oranını bul','Aynı r için v = √(GM / r) olduğundan v, √M ile orantılıdır.','v_X / v_Y = √4 = 2')],
 puf='Doğrunun eğimini merkezi cismin kütlesiyle ilişkilendir.',sekil=sk)

# ================= 17 · zor · üç cisim, doğrusal =================
u=.6
sk=fig(f'\\draw[thick] (0,0) -- ({3*u*2:.3f},0);',ball(0,0,'$9m$',r=.34),ball(1*u*2,0,'$2m$',r=.25),ball(3*u*2,0,None,r=.3),
       f'\\node at ({3*u*2:.3f},0) {{Z}}; \\node[below] at (0,-.35) {{X}}; \\node[below] at ({2*u:.3f},-.3) {{Y}};',
       dim(0,.85,2*u,.85,'$d$','above'),dim(2*u,.85,6*u,.85,'$2d$','above'))
mZ=Fr(9*4,1); assert mZ==36 and Fr(9,1)*2/1==18
FZ_Y=Fr(36*2,4); FZ_X=Fr(36*9,9); FZ=FZ_Y+FZ_X; assert (FZ_Y,FZ_X,FZ)==(18,36,54)
w1=Fr(9*2,4)+Fr(9*9,9); assert w1==Fr(27,2)
w2=FZ_Y+Fr(36*9,4); assert w2==99
q('0017',tipId='kutle-bilesim',tip='Birden çok cismin çekim kuvveti',z='zor',alt=ALT,kaz='Bir cisme etki eden net kuvvetin sıfır olma koşulundan kütleyi bulup başka bir cisme etki eden net kuvveti hesaplar.',
 kart='K-AFKUTLE-02 (üç cisim, doğrusal) · 9m, 2m ve bilinmeyen kütle',kalip='şekilli',
 metin='Kütleleri 9m ve 2m olan X ve Y küreleri ile kütlesi bilinmeyen Z küresi, merkezleri aynı doğru üzerinde olacak biçimde şekildeki gibi sabitlenmiştir. Y küresine etki eden net çekim kuvvetinin sıfır olduğu bilinmektedir. Başka cisimlerin etkisi yoktur.\nBuna göre, Z küresine etki eden net çekim kuvvetinin büyüklüğü kaç G·m² / d² dir?',
 dogru=54,yan=[(Fr(27,2),'Z’nin kütlesini 9m (X’inkine eşit) almış: 9·2/4 + 9·9/9 = 13,5.','islem'),(18,'Yalnız Y’nin Z’ye uyguladığı kuvveti hesaplamış: 36 · 2 / 4 = 18.','dikkat'),(36,'Yalnız X’in Z’ye uyguladığı kuvveti hesaplamış: 36 · 9 / 9 = 36.','dikkat'),(99,'X ile Z arası uzaklığı 2d almış: 18 + 36 · 9 / 4 = 99.','islem')],
 istenen='Z küresine etki eden net çekim kuvveti (G m² / d²).',ip=['Önce Y küresindeki net kuvvetin sıfır olma koşulundan Z’nin kütlesini bul; sonra Z’ye etki eden iki kuvvetin yönlerini karşılaştır.'],
 bilgi=[B_YASA],ad=[A('Y’de net kuvvetin sıfır olması','X ve Z, Y’yi zıt yönlerde çeker ve kuvvetler eşittir.','G · 9m · 2m / d² = G · m_Z · 2m / (2d)²'),A('Z’nin kütlesini bul','Eşitlikten çöz.','m_Z = 36m'),A('Z’ye etki eden kuvvetler','Y ve X aynı yönde (sola) çeker.','F_Y = G · 36m · 2m / (2d)² = 18, F_X = G · 36m · 9m / (3d)² = 36'),A('Toplam kuvveti bul','Aynı yönlü kuvvetler toplanır.','F = 18 + 36 = 54 G m² / d²')],
 puf='Z’ye etkiyen iki kuvvetin yönlerini çiz.',sekil=sk)

# ================= 18 · zor · yüzeye yakın hız, 4R yörünge periyodu =================
Rg=Fr(64,10)*10**6; g_=10; pi=3
v0=Fr(8000); assert v0*v0==g_*Rg
T0=2*pi*Rg/v0; assert T0==4800
v4=v0/2; T4=2*pi*4*Rg/v4; assert T4==38400 and T4==8*T0
assert 2*T0*2==19200 and T0*16==76800 and T0*64==307200 and T0*2==9600
q('0018',tipId='kutle-uydu',tip='Çembersel yörüngede hız, periyot ve enerji',z='zor',alt=ALT,kaz='Yüzey çekim ivmesinden yüzeye yakın yörünge hızını, buradan da daha yüksek yörüngenin periyodunu hesaplar.',
 kart='K-AFKUTLE-04 (g ve R ile periyot) · yörünge yarıçapı 4R',kalip='hikâyeli',
 metin='Yarıçapı R = 6,4 · 10⁶ m olan küresel ve homojen bir gezegenin yüzeyindeki çekim ivmesinin büyüklüğü 10 m/s² dir. Bir gözlem uydusu, gezegenin merkezinden 4R uzaklıktaki çembersel yörüngede dolandırılacaktır. Gezegenin dönmesi ve atmosferin etkisi ihmal edilmektedir.\n(π = 3 alınız.)\nBuna göre, uydunun dolanım periyodu kaç saniyedir?',
 dogru=38400,yan=[(9600,'Periyodu yarıçapın karekökü ile orantılı almış: 4800 · 2 = 9600 s.','islem'),(19200,'Periyodu yörünge yarıçapıyla doğru orantılı almış: 4800 · 4 = 19200 s.','islem'),(76800,'Periyodu yarıçapın karesiyle orantılı almış: 4800 · 16 = 76800 s.','islem'),(307200,'Periyodu yarıçapın küpüyle orantılı almış: 4800 · 64 = 307200 s.','islem')],
 istenen='Uydunun dolanım periyodu (s).',ip=['Yüzey çekim ivmesinden GM çarpımını ya da yüzeye yakın yörünge hızını bulup 4R yarıçaplı yörünge için aynı bağıntıyı uygula.'],
 bilgi=[B_IVME,B_UYDU],ad=[A('GM çarpımını bul','Yüzeyde g = GM / R² dir.','GM = g R² = 10 · (6,4·10⁶)²'),A('4R’deki hızı bul','Çembersel yörüngede v = √(GM / r) dir.','v = √(g R² / 4R) = ½ √(g R) = ½ · 8000 = 4000 m/s'),A('Periyodu hesapla','Bir turda yol 2π · 4R dür.','T = 2 · 3 · 4 · 6,4·10⁶ / 4000 = 38400 s')],
 puf='g R² = G M bağıntısı, yüzey verisinden yörünge büyüklüklerine geçmeyi sağlar.')

# ================= 19 · zor · tablo, kinetik enerji oranı =================
sk=fig('\\draw[thick] (0,0) rectangle (6.4,2.4);','\\draw[thick] (0,.8) -- (6.4,.8); \\draw[thick] (0,1.6) -- (6.4,1.6); \\draw[thick] (1.6,0) -- (1.6,2.4); \\draw[thick] (4.0,0) -- (4.0,2.4);',
       '\\node at (.8,2.0) {Uydu}; \\node at (2.8,2.0) {Kütle}; \\node at (5.2,2.0) {Yörünge yarıçapı};',
       '\\node at (.8,1.2) {K}; \\node at (2.8,1.2) {$m$}; \\node at (5.2,1.2) {$r$};',
       '\\node at (.8,.4) {L}; \\node at (2.8,.4) {$2m$}; \\node at (5.2,.4) {$4r$};')
ER=Fr(1,1)/(Fr(2,4)); assert ER==2 and Fr(1,2)==Fr(2*1,4)  and Fr(4)==4 and Fr(1,1)*16==16
assert (Fr(1,1)/1)/(Fr(2,1)/16)==8 and (1/Fr(1,1))/(2/Fr(16))==8
q('0019',tipId='kutle-uydu',tip='Çembersel yörüngede hız, periyot ve enerji',z='orta',alt=ALT,kaz='Çembersel yörüngedeki uydunun kinetik enerjisini kütle ve yarıçapa göre karşılaştırır.',
 kart='K-AFKUTLE-04 (kinetik enerji oranı) · (m, r) ve (2m, 4r)',kalip='tablo',
 metin='Yerküre çevresinde çembersel yörüngelerde dolanan K ve L uydularının kütleleri ile yörünge yarıçapları şekildeki tabloda verilmiştir. Uydulara yalnızca Yerküre’nin çekim kuvveti etki etmektedir.\nBuna göre, K uydusunun kinetik enerjisinin L uydusunun kinetik enerjisine oranı E_K / E_L kaçtır?',
 dogru=2,yan=[(Fr(1,2),'Hızları eşit sayıp yalnızca kütleleri karşılaştırmış: m / 2m = 0,5.','dikkat'),(4,'Yalnızca yörünge yarıçaplarının oranını almış: 4r / r = 4.','dikkat'),(8,'Hızı yarıçapla ters orantılı alıp kütleyi katmış: (m / r²) / (2m / 16r²) = 8.','islem'),(16,'Kütleyi hiç hesaba katmayıp hızı yarıçapla ters orantılı almış: 16.','islem')],
 istenen='Kinetik enerjiler oranı E_K / E_L.',ip=['Çembersel yörüngedeki hızın yarıçapa nasıl bağlı olduğunu çekim kuvveti–merkezcil kuvvet eşitliğinden bul; sonra kinetik enerjiyi yaz.'],
 bilgi=[B_UYDU],ad=[A('Hızı yaz','Çekim kuvveti merkezcil kuvvete eşittir.','v² = GM / r'),A('Kinetik enerjiyi yaz','Kütle ve yarıçap ifadede kalır.','E_k = ½ m v² = G M m / 2r'),A('Oranla','K için m / r, L için 2m / 4r = m / 2r dir.','E_K / E_L = (m / r) / (m / 2r) = 2')],
 puf='Hızın yarıçapa bağlılığını bulduktan sonra kinetik enerjiyi kütleyle birlikte yaz.',sekil=sk)

# ================= 20 · zor · öncüllü iki uydu, hesaplı =================
tr={'I':False,'II':True,'III':False}
assert 9**Fr(3,2)==27 and sqrt(9)==3
assert 3*3*1==1*1*9
assert Fr(3,1)/Fr(1,9)==27
rs={'I':'Açısal momentum L = m v r dir: K için 3m · 3v · r = 9 m v r, L için m · v · 9r = 9 m v r olduğundan ikisi eşittir; L’ninki daha büyük değildir.','II':'Kinetik enerji G M m / 2r ile orantılıdır: K için 3m / r, L için m / 9r olduğundan oran 27 dir.','III':'T² ∝ r³ olduğundan T_L / T_K = 9^(3/2) = 27 dir; periyot oranı 9 değildir.'}
d,y,ad=onc(tr,rs,['Yalnız I','Yalnız II','Yalnız III','I ve II','II ve III'])
q('0020',tipId='kutle-uydu',tip='Çembersel yörüngede hız, periyot ve enerji',z='zor',alt=ALT,kaz='İki uydunun açısal momentum, kinetik enerji ve periyot oranlarını kütle ve yarıçap oranlarıyla hesaplayarak yargıları değerlendirir.',
 kart='K-AFKUTLE-04 (üç oran) · (3m, r) ve (m, 9r)',kalip='öncüllü',
 metin='Yerküre çevresinde çembersel yörüngelerde dolanan K ve L uydularının kütleleri sırasıyla 3m ve m, yörünge yarıçapları ise sırasıyla r ve 9r dir. Uydulara yalnızca Yerküre’nin çekim kuvveti etki etmektedir.\nBuna göre;\nI. L’nin Yerküre’nin merkezine göre açısal momentumunun büyüklüğü, K’ninkinden büyüktür.\nII. K’nin kinetik enerjisi, L’ninkinin 27 katıdır.\nIII. L’nin dolanım periyodu, K’ninkinin 9 katıdır.\nyargılarından hangileri doğrudur?',
 dogru=d,yan=y,sira=['Yalnız I','Yalnız II','Yalnız III','I ve II','II ve III'],istenen='Doğru olan yargılar.',ip=['Her yargıdaki büyüklüğü kütle ve yarıçapa göre yazıp K ile L’yi oranla.'],
 bilgi=[B_UYDU,B_YASA],ad=ad,puf='Her büyüklüğü kütle ve yarıçap cinsinden ayrı ayrı yaz.')

# ================= yaz =================
for qq in P.ANA: qq['kardes']=None
P.yaz(os.path.join(GD,'kutlecekim-1.json'),'/tmp/bos-kutlecekim.json')
tipler={}
for c in KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu='afiz|Kütle Çekim Kuvveti'))['kartlar'].append(c['id'])
json.dump(dict(konu='Kütle Çekim Kuvveti',surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2018–2025 Fizik (yalnız mantık), MEB 12. sınıf fizik müfredatı.',kartlar=KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','afkutlecekim.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
