"""TYT Fizik · Isı, Sıcaklık ve Genleşme · ek paket (isiiki): 22 soru, kardeş yok, ipucu 1. Şekil verileri Python'da hesaplanır, TikZ bu değerlerden üretilir.
Her cevap ve çeldirici değer assert edilir; öncüllerin doğruluğu yorumla gerekçelendirilir."""
import sys,os,json,importlib.util
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,GD)
import _hafif as H
from _hafif import *
from cizim import tikz_svg
from math import exp
spec=importlib.util.spec_from_file_location('hm',os.path.join(HV,'tyt-mat','_hafif_mat.py')); HM=importlib.util.module_from_spec(spec); spec.loader.exec_module(HM)
tablo_svg=HM.tablo_svg
KONU_='Isı, Sıcaklık ve Genleşme'; UK='fiz|Isı, Sıcaklık ve Genleşme'
H.KONU=KONU_
P=Parti('isiiki',KONU_,UK,ders='TYT Fizik',idon='tytfiz')
KY='ÖSYM 2018–2026 TYT Fizik (yalnız mantık) · MEB 9. sınıf Isı, Sıcaklık ve Genleşme'
def kartla(n,alt,fikir,tuzak,z,kalip,adim,tipad,tip):
    kart(f'K-FZIS2-{n}',alt,fikir,tuzak,z,kalip,adim,f'fz-is2-{tipad}',tip,KY)
def q(no,ad,**k):
    assert len(k['ip'])==1
    mk(P,no,ad=ad,adim=len(ad),**k)
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
ARR='-{Stealth[length=2mm,width=1.8mm]}'
DC='$^\\circ$C'
def tk(g,extra=''): return tikz_svg(HEAD+g+TAIL)
def beaker(x,lv,w=1.6,h=2.6,fill='vurgu!15'):
    s=f'\\fill[{fill}] ({x},0) rectangle ({x+w},{lv});\\draw[thick] ({x},{h}) -- ({x},0) -- ({x+w},0) -- ({x+w},{h});'
    return s
def termo(x,fill,H_=3.0,w=.3):
    return (f'\\draw[thick,fill=white] ({x-w/2},0) rectangle ({x+w/2},{H_});\\fill[vurgu!55] ({x-w/2+.03},.0) rectangle ({x+w/2-.03},{fill});'
            f'\\draw[thick,fill=vurgu!55] ({x},-.28) circle (.3);\\draw[thick] ({x-w/2},0) -- ({x-w/2},{H_}) -- ({x+w/2},{H_}) -- ({x+w/2},0);')
ORD=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
def sira(*k): return [s for s in ORD if s in k]
S_STD=['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III']

# ================= 01 · ısı, sıcaklık, iç enerji · kolay · öncüllü =================
kartla('01','Isı, sıcaklık ve iç enerji ayrımı','Sıcaklık ortalama kinetik enerjiyle, iç enerji tanecik sayısı ve sıcaklıkla ilgilidir; ısı yalnız sıcaklık farkından dolayı aktarılan enerjidir.','Isı ile sıcaklığı karıştırmak; kütlesi fazla olana “daha sıcak” demek; aynı sıcaklıktaki cisimler arasında da ısı akışı sanmak.','kolay','öncüllü',3,'ayrim','Isı, sıcaklık ve iç enerji ayrımı')
mA,mB,mC=100,200,200; tA,tB,tC=30,30,50
# I: aynı madde, aynı sıcaklık, kütle fazla -> iç enerji büyük (doğru). II: sıcaklıklar eşit -> net ısı alışverişi yok (doğru).
# III: C, B ile aynı kütle ve daha sıcak -> iç enerjisi B'den BÜYÜK; "küçüktür" yanlış.
assert mB>mA and tA==tB and mC==mB and tC>tB
g=''
for x,lv,nm,ms,t in [(0,1.0,'A',mA,tA),(2.4,2.0,'B',mB,tB),(4.8,2.0,'C',mC,tC)]:
    g+=beaker(x,lv)+f'\\node[below,align=center] at ({x+.8},-.05) {{\\textbf{{{nm}}}\\\\ {ms} g su\\\\ {t}\\,{DC}}};'
SK=tk(g)
q('0001',tipId='fz-is2-ayrim',tip='Isı, sıcaklık ve iç enerji ayrımı',z='kolay',alt='Isı, Sıcaklık ve İç Enerji',kaz='Isı, sıcaklık ve iç enerji kavramlarını kütle ve sıcaklık verilerine bakarak ayırt eder.',kalip='öncüllü',
 kart='K-FZIS2-01 (ısı–sıcaklık–iç enerji) · üç beher',sekil=SK,
 metin='Bir laboratuvarda öğrenciler, özdeş üç behere şekilde görüldüğü gibi farklı kütlelerde su koymuş ve her birinin sıcaklığını ölçmüştür. Beherler çevreyle ısı alışverişi yapmayacak biçimde yalıtılmıştır; sular aynı maddedir ve hâl değiştirmemektedir. Öğrenciler ısı, sıcaklık ve iç enerji kavramlarını bu veriler üzerinden yorumlayacaktır.\nI. B beherindeki suyun iç enerjisi, A beherindeki suyun iç enerjisinden büyüktür.\nII. A ve B beherlerindeki sular birbirine karıştırılırsa suyun sıcaklığı değişmez, net ısı alışverişi olmaz.\nIII. C beherindeki suyun iç enerjisi, B beherindeki suyun iç enerjisinden küçüktür.\nBuna göre bu yargılardan hangileri doğrudur?',
 dogru='I ve II',sira=S_STD,yan=[('Yalnız I','II’yi yanlış saymış: sıcaklıkları eşit sular karışsa da kütle farkından ötürü ısı akacağını düşünmüş.','bilgi'),('Yalnız II','I’i yanlış saymış: iç enerjinin yalnız sıcaklığa bağlı olduğunu, kütle (tanecik sayısı) arttıkça artmadığını sanmış.','bilgi'),('I ve III','II’yi atlamış ve III’ü doğru bulmuş; C’nin hem aynı kütlede hem daha sıcak olduğunu iç enerjiyle ilişkilendirememiş.','dikkat'),('I, II ve III','III’ü de doğru saymış; daha sıcak olan C’nin iç enerjisini B’nin altında düşünmüş.','dikkat')],
 istenen='Doğru olan yargılar.',ip=['Aynı maddede iç enerji hem tanecik sayısına hem sıcaklığa bağlıdır; ısı ise ancak sıcaklık farkı varsa akar.'],
 bilgi=[B('Isı, sıcaklık ve iç enerji','sıcaklık, taneciklerin ortalama kinetik enerjisinin ölçüsüdür. Isı, sıcaklık farkı yüzünden aktarılan enerjidir. İç enerji, bir cismi oluşturan tüm taneciklerin enerjileri toplamıdır; kütle ve sıcaklıkla artar. Örnek: aynı sıcaklıktaki 1 kg ve 3 kg suyun sıcaklıkları eşittir, 3 kg’ın iç enerjisi büyüktür')],
 ad=[A('I’i değerlendir','B’de A’dan 2 kat tanecik var, sıcaklıkları eşit.','I: B’nin iç enerjisi daha büyük → doğru'),A('II’yi değerlendir','Isı yalnız sıcaklık farkı olan cisimler arasında akar.','tA = tB = 30 °C → net ısı akışı yok → doğru'),A('III’ü değerlendir','B ve C’nin kütleleri eşit, C daha sıcak.','C’nin iç enerjisi B’den büyük → III yanlış'),A('Sonuç','Doğru yargılar I ve II’dir.','I ve II')],
 puf='Sıcaklık eşitse ısı akışı olmaz; iç enerji için kütleye de bak.')

# ================= 02 · X termometresi · kolay =================
kartla('02','X termometresi ölçek dönüşümü','İki sabit nokta arasındaki bölme sayısı oranlanır: (X − X₀)/(X₁ − X₀) = C/100.','Başlangıç değerini çıkarmadan oranlamak; bölme oranını ters çarpmak; kaynama noktasından saymak.','kolay','şekilli',3,'xtermo','X termometresi ile Celsius dönüşümü')
xl,xh,xr=20,170,50
Cv=Fr((xr-xl)*100,xh-xl); assert Cv==20
assert xr-xl==30 and Fr((xr-xl)*(xh-xl),100)==45 and Fr((xh-xr)*100,xh-xl)==80
H_=4.0; y0,y1=.6,3.6
yr=y0+(xr-xl)/(xh-xl)*(y1-y0)
g=termo(0,yr,H_)
g+=f'\\foreach \\y in {{{y0},{y1}}}{{\\draw[thick] (-.15,\\y) -- (.15,\\y);}}'
g+=f'\\node[left] at (-.25,{y0}) {{$20\\,^\\circ$X}}; \\node[left] at (-.25,{y1}) {{$170\\,^\\circ$X}};'
g+=f'\\node[right] at (.25,{y0}) {{$0\\,^\\circ$C}}; \\node[right] at (.25,{y1}) {{$100\\,^\\circ$C}};'
g+=f'\\draw[{ARR}] (-1.9,{yr}) -- (-.2,{yr}); \\node[left] at (-1.9,{yr}) {{$50\\,^\\circ$X}};'
g+=f'\\node[above] at (-.9,{H_+.05}) {{X ölçeği}}; \\node[above] at (1.1,{H_+.05}) {{Celsius}};'
g+=f'\\node[align=left,anchor=west] at (1.9,{y0}) {{\\scriptsize buzun erime}}; \\node[align=left,anchor=west] at (1.9,{y1}) {{\\scriptsize suyun kaynama}};'
SK=tk(g)
q('0002',tipId='fz-is2-xtermo',tip='X termometresi ile Celsius dönüşümü',z='kolay',alt='Termometreler ve Sıcaklık Ölçekleri',kaz='Sabit noktaları verilen bir termometrenin okumasını Celsius ölçeğine çevirir.',kalip='şekilli',
 kart='K-FZIS2-02 (X termometresi) · sabit noktalar 20 °X ve 170 °X',sekil=SK,
 metin='Bir öğrenci, buzun erime ve suyun kaynama sıcaklıklarını (normal basınç) şekildeki gibi işaretlediği X ölçeğini, Celsius ölçeğiyle birlikte aynı cam tüp üzerine yerleştirmiştir. Aynı tüp üzerindeki iki ölçeğin bölmeleri eşit aralıklıdır. Öğrenci termometreyi sınıfa bırakıp sıvı seviyesinin şekilde gösterilen değerde durduğunu görmüştür.\nBuna göre, sınıfın sıcaklığı kaç °C’dir?',
 dogru=20,yan=[(30,'Başlangıç değerini çıkarmış (50 − 20 = 30) ama X ve Celsius bölmelerinin oranını (150 bölmeye karşı 100 bölme) hesaba katmamış.','dikkat'),(45,'Bölme oranını ters uygulamış: 30 × 150 ÷ 100 = 45.','islem'),(50,'X ile Celsius okumalarının aynı olduğunu sanmış.','bilgi'),(80,'Okumayı kaynama noktasından saymış: (170 − 50) × 100 ÷ 150 = 80.','dikkat')],
 istenen='Sınıfın sıcaklığı (°C).',ip=['Her iki ölçekte de buz noktası ile kaynama noktası arasındaki bölme sayılarını karşılaştır.'],
 bilgi=[B('Termometre ölçek dönüşümü','farklı ölçeklerde ilk sabit noktadan okunan bölme sayısının, toplam bölme sayısına oranı aynıdır: (X − X₀)/(X₁ − X₀) = (C − 0)/100. Örnek: 0–200 arası ölçekte 40 okuması, oranı 40/200 = 1/5 olduğundan 20 °C’ye karşılık gelir')],
 ad=[A('Toplam bölme sayısı','İki sabit nokta arasındaki bölme sayıları X ve Celsius için ayrı hesaplanır.','X: 170 − 20 = 150 bölme · C: 100 bölme'),A('Okunan bölme','Seviyenin buz noktasından yüksekliğini bul.','50 − 20 = 30 bölme'),A('Oranı kur','Oranlar iki ölçekte eşittir.','30/150 = C/100'),A('Sonuç','C hesaplanır.','C = 20 °C')],
 puf='Önce sabit noktalardan uzaklığı bul, sonra iki ölçekte aynı oranı yaz.')

# ================= 03 · Celsius, Kelvin, Fahrenheit · orta · öncüllü =================
kartla('03','Kelvin ve Fahrenheit dönüşümü','K = °C + 273; °F = 1,8·°C + 32. Sıcaklıkları ortak ölçeğe çevirip karşılaştırmak gerekir.','Kelvin için 273 yerine eklemek yerine çıkarmak; Fahrenheit’ı doğrudan karşılaştırmak.','orta','öncüllü',4,'kelvinF','Celsius, Kelvin ve Fahrenheit ölçekleri')
cA=27; cB=303-273; cC=Fr(86-32)*Fr(5,9)
assert cB==30 and cC==30 and cA==27
# I: B ve C aynı (30 °C) doğru. II: A en yüksek -> yanlış (27 en düşük). III: B Celsius'ta 576 °C -> yanlış (30 °C).
g=''
for x,v,l in [(0,1.5,'A'),(2.4,1.5,'B'),(4.8,1.5,'C')]:
    g+=termo(x,v)
g+='\\node[above] at (0,3.1) {$27\\,^\\circ$C}; \\node[above] at (2.4,3.1) {$303$ K}; \\node[above] at (4.8,3.1) {$86\\,^\\circ$F};'
g+='\\node[below] at (0,-.65) {\\textbf{A}}; \\node[below] at (2.4,-.65) {\\textbf{B}}; \\node[below] at (4.8,-.65) {\\textbf{C}};'
SK=tk(g)
q('0003',tipId='fz-is2-kelvinF',tip='Celsius, Kelvin ve Fahrenheit ölçekleri',z='orta',alt='Termometreler ve Sıcaklık Ölçekleri',kaz='Farklı ölçeklerde verilen sıcaklıkları ortak ölçeğe çevirip karşılaştırır.',kalip='öncüllü',
 kart='K-FZIS2-03 (Celsius–Kelvin–Fahrenheit) · 27 °C, 303 K, 86 °F',sekil=SK,
 metin='Bir iklim laboratuvarında üç ayrı termometre, farklı ülkelerden getirilen A, B ve C ortamlarının sıcaklığını farklı ölçeklerde göstermektedir. Termometrelerin okumaları şekilde verilmiştir. Öğrenciler ortamları kıyaslamak için okumaları ortak bir ölçeğe çevirmeyi planlıyor. Celsius, Kelvin ve Fahrenheit arasındaki dönüşümler için K = °C + 273 ve °F = 1,8 · °C + 32 bağıntıları kullanılacaktır.\nI. B ve C ortamlarının sıcaklıkları eşittir.\nII. A ortamı, C ortamından daha sıcaktır.\nIII. B ortamının sıcaklığı Celsius ölçeğinde 576 °C’dir.\nBuna göre bu yargılardan hangileri doğrudur?',
 dogru='Yalnız I',sira=S_STD,yan=[('Yalnız II','86 °F’ı Celsius’a çevirirken 86 × 5/9 − 32 gibi yanlış bir işlem yapıp C’yi 27 °C’nin altında bulmuş; B’nin 30 °C olduğunu da kaçırmış.','islem'),('I ve II','B ile C’nin eşit olduğunu görmüş; ancak A ile C’yi karşılaştırırken 27 °C ile 86 °F’ı çevirmeden kıyaslayıp A’yı daha sıcak sanmış.','dikkat'),('I ve III','III’te 303 K’yi 303 + 273 = 576 °C diye çevirmiş; Kelvin’den Celsius’a 273 çıkarılır.','islem'),('I, II ve III','Hem Fahrenheit hem Kelvin dönüşümünde işlem hatası yapıp üç yargıyı da doğru sanmış.','islem')],
 istenen='Doğru olan yargılar.',ip=['Üç değeri de aynı ölçeğe, örneğin Celsius’a çevirip öyle karşılaştır.'],
 bilgi=[B('Sıcaklık ölçekleri','Kelvin ile Celsius arasında K = °C + 273 vardır; sıcaklık farkı iki ölçekte aynıdır. Fahrenheit için °F = 1,8 · °C + 32. Örnek: 10 °C = 283 K = 50 °F')],
 ad=[A('B’yi çevir','Kelvin’den Celsius’a 273 çıkarılır.','303 − 273 = 30 °C'),A('C’yi çevir','Fahrenheit’tan 32 çıkarıp 1,8’e böl.','(86 − 32) ÷ 1,8 = 30 °C'),A('Karşılaştır','A 27 °C, B ve C 30 °C’dir.','I doğru · C, A’dan sıcak → II yanlış'),A('III’ü incele','B ortamının Celsius karşılığı 30 °C’dir, 576 °C değil.','III yanlış → Yalnız I')],
 puf='Farklı ölçeklerdeki sıcaklıkları kıyaslamadan önce hepsini aynı ölçeğe çevir.')

# ================= 04 · iki termometre ortak okuma · zor · grafik =================
kartla('04','İki termometrenin aynı değeri okuması','Her termometrenin okuması Celsius’un doğrusal fonksiyonudur; iki doğru eşitlenerek ortak okuma bulunur.','Ortak sıcaklığı (Celsius) ortak okuma sanmak; sabit nokta ortalamalarını almak.','zor','grafik',4,'iki-termo','İki termometrenin ortak okuması')
xa,xb=-10,140; ya,yb=20,70
sx=Fr(xb-xa,100); sy=Fr(yb-ya,100)
Cc=Fr(ya-xa)/(sx-sy); rd=xa+sx*Cc
assert sx==Fr(3,2) and sy==Fr(1,2) and Cc==30 and rd==35 and ya+sy*Cc==35
assert (xa+ya)/2==5 and (xb+yb)/2==105
Cw=Fr(ya-(-xa),sx-sy); rw=-xa+sx*Cw; assert Cw==10 and rw==25
g='''\\begin{axis}[width=7cm,height=5.6cm,xmin=0,xmax=105,ymin=-20,ymax=155,xtick={0,100},ytick={-10,20,70,140},tick label style={font=\\scriptsize},axis lines=left,xlabel={Celsius ($^\\circ$C)},ylabel={Okunan değer},xlabel style={font=\\small},ylabel style={font=\\small}]
\\addplot[thick,vurgu,mark=*,mark size=1.4pt] coordinates {(0,-10) (100,140)};
\\addplot[thick,mark=*,mark size=1.4pt] coordinates {(0,20) (100,70)};
\\node[anchor=south east] at (axis cs:98,140) {X}; \\node[anchor=north east] at (axis cs:98,69) {Y};
\\end{axis}'''
SK=tk(g)
q('0004',tipId='fz-is2-iki-termo',tip='İki termometrenin ortak okuması',z='zor',alt='Termometreler ve Sıcaklık Ölçekleri',kaz='İki farklı termometrenin okumalarının Celsius ile ilişkisinden aynı değeri gösterdikleri durumu bulur.',kalip='grafik',
 kart='K-FZIS2-04 (iki termometre) · X: −10…140, Y: 20…70',sekil=SK,
 metin='Bir araştırmacı, X ve Y adlı iki termometreyi buzun erime sıcaklığında ve suyun kaynama sıcaklığında (normal basınç) denemiş; okumalarını Celsius ölçeğine göre çizdiği grafiğe işlemiştir. Her iki termometrenin bölmeleri kendi içinde eşit aralıklıdır, bu nedenle okuma değerleri Celsius sıcaklığıyla doğrusal olarak değişir. Araştırmacı termometreleri aynı ortama koyduğunda iki termometrenin de birbirine eşit değer gösterdiğini fark ediyor.\nBuna göre bu ortak okuma kaçtır?',
 dogru=35,yan=[(5,'Buz noktasında okunan iki değerin aritmetik ortalamasını (−10 ile 20’nin ortası) ortak okuma sanmış.','dikkat'),(25,'X’in buz noktası okumasını −10 yerine +10 almış: 10 + 1,5C = 20 + 0,5C → C = 10 → okuma 25.','islem'),(30,'Doğru ortamı (30 °C) bulmuş ama termometrenin o ortamda gösterdiği değeri (35) değil, Celsius değerini yazmış.','dikkat'),(105,'Kaynama noktasındaki iki okumanın ortalamasını (70 ile 140’ın ortası) ortak okuma saymış.','dikkat')],
 istenen='Termometrelerin gösterdiği ortak değer.',ip=['Her termometrenin okumasını Celsius sıcaklığına bağlayan eşitliği yaz; sonra bu iki eşitliği birbirine eşitle.'],
 bilgi=[B('Doğrusal ölçek','iki sabit nokta arasında eşit bölmeli termometrenin okuması R = R₀ + (R₁ − R₀)·C/100 biçiminde Celsius’a bağlıdır. Örnek: 0 °C’de 10, 100 °C’de 60 gösteren termometre için R = 10 + 0,5·C')],
 ad=[A('X’in eşitliği','Buz noktasında −10, kaynamada 140; 100 °C’de 150 bölme değişim.','X = −10 + 1,5·C'),A('Y’nin eşitliği','Buz noktasında 20, kaynamada 70; 100 °C’de 50 bölme değişim.','Y = 20 + 0,5·C'),A('Eşitle','Okumalar eşit olacak.','−10 + 1,5C = 20 + 0,5C → C = 30 °C'),A('Okumayı bul','Ortak değeri herhangi bir eşitlikle hesapla.','X = −10 + 1,5·30 = 35')],
 puf='Doğrusal ölçekler karşılaştırılırken her termometrenin okumasını Celsius cinsinden yazıp eşitle.')

# ================= 05 · ısı sığası tablosu · orta · öncüllü =================
kartla('05','Isı sığası ve öz ısı karşılaştırması','Isı sığası C = m·c; aynı ısıyla sıcaklık artışı ΔT = Q/C, ısı sığasıyla ters orantılıdır.','Öz ısıyı ısı sığasıyla karıştırmak; öz ısısı küçük olana “ısı sığası da küçük” demek.','orta','öncüllü',4,'isisigasi','Isı sığası ve öz ısı')
tK,tL,tM=(100,Fr(1,2)),(200,Fr(1,5)),(50,Fr(1))
CK,CL,CM=[m*c for m,c in (tK,tL,tM)]
assert (CK,CL,CM)==(50,40,50)
# I: L'nin ısı sığası en büyük -> yanlış (40 en küçük). II: C_K = C_M -> doğru. III: aynı ısıda en çok ısınan K ve M'dir (ısı sığası 50)? Tablo: ΔT=Q/C -> L (C=40) en çok ısınır. "K ve M, L'den daha fazla ısınır" yanlış.
assert max(CK,CL,CM)!=CL and CK==CM and min(CK,CL,CM)==CL
SK=tablo_svg(['Cisim','Kütle (g)','Öz ısı (cal/g·°C)'],[['K','100','0,5'],['L','200','0,2'],['M','50','1']])
q('0005',tipId='fz-is2-isisigasi',tip='Isı sığası ve öz ısı',z='orta',alt='Öz Isı ve Isı Sığası',kaz='Kütle ve öz ısıdan ısı sığasını bulup aynı ısı verilen cisimlerin sıcaklık artışını karşılaştırır.',kalip='tablo',
 kart='K-FZIS2-05 (ısı sığası tablosu) · K, L, M cisimleri',sekil=SK,
 metin='Bir öğrenci, özellikleri aşağıdaki tabloda verilen K, L ve M cisimlerinin ısınma davranışını inceleyecektir. Cisimler başlangıçta aynı sıcaklıktadır, hâl değiştirmezler ve ısı alışverişi yalnızca öğrencinin verdiği ısıyla olacaktır. Öğrenci her cisme önce ayrı ayrı eşit miktarda ısı verecek, sonra ısı sığalarını karşılaştıracaktır.\nI. En büyük ısı sığasına sahip cisim L’dir.\nII. K ile M’nin ısı sığaları eşittir.\nIII. Eşit ısı verildiğinde K ve M’nin sıcaklık artışı L’ninkinden büyüktür.\nBuna göre bu yargılardan hangileri doğrudur?',
 dogru='Yalnız II',sira=S_STD,yan=[('Yalnız I','Kütlesi en büyük olan L’nin ısı sığasının da en büyük olduğunu sanmış; öz ısıyı çarpıma katmamış.','bilgi'),('I ve II','II’yi bulmuş ama I’i doğru saymış; L’nin ısı sığasını (40 cal/°C) K ve M’nin (50 cal/°C) üzerinde sanmış.','islem'),('I ve III','L’nin kütlesi büyük olduğu için ısı sığasını en büyük, K ve M’ninkini küçük ve bu yüzden daha çok ısınır sanmış; K ile M’nin ısı sığalarının eşit olduğunu görmemiş.','bilgi'),('I, II ve III','Tüm yargıları doğru bulmuş; ısı sığası ile sıcaklık artışı arasındaki ters orantıyı görmemiş.','bilgi')],
 istenen='Doğru olan yargılar.',ip=['Her cisim için kütle ile öz ısıyı çarp; aynı ısı verildiğinde sıcaklık artışının ısı sığasıyla nasıl değiştiğini düşün.'],
 bilgi=[B('Isı sığası','C = m · c (cal/°C ya da J/°C): cismin sıcaklığını 1 °C değiştirmek için gereken ısıdır. Aynı ısıyla sıcaklık artışı ΔT = Q ÷ C olduğundan ısı sığası büyük olan daha az ısınır. Örnek: C = 20 cal/°C olan cisim 100 cal alınca 5 °C ısınır')],
 ad=[A('K’nin ısı sığası','Kütle ile öz ısıyı çarp.','C_K = 100 × 0,5 = 50 cal/°C'),A('L’nin ısı sığası','Aynı işlem.','C_L = 200 × 0,2 = 40 cal/°C'),A('M’nin ısı sığası','Aynı işlem.','C_M = 50 × 1 = 50 cal/°C'),A('Yargıları incele','En büyük 50 (K ve M); eşit ısıda ΔT = Q ÷ C, en küçük C olan L en çok ısınır.','I yanlış · II doğru · III yanlış'),A('Sonuç','Yalnız II doğrudur.','Yalnız II')],
 puf='Isı sığası kütle ve öz ısının çarpımıdır; aynı ısıda en çok ısınan, ısı sığası en küçük olandır.')

# ================= 06 · Q–T grafiği öz ısı oranı · orta =================
kartla('06','Isı–sıcaklık grafiğinde öz ısı oranı','c = Q/(m·ΔT); grafikte aynı ısıyla oluşan sıcaklık artışı ve kütle birlikte kullanılır.','Yalnız ΔT oranına ya da yalnız kütle oranına bakmak.','orta','grafik',4,'qt-oran','Isı–sıcaklık grafiğinden öz ısı oranı')
mX,mY=100,200; dX,dY=40,30; Q0=1200
cX=Fr(Q0,mX*dX); cY=Fr(Q0,mY*dY); assert cX==Fr(3,10) and cY==Fr(1,5) and cX/cY==Fr(3,2)
assert Fr(mX,mY)==Fr(1,2) and Fr(dY,dX)==Fr(3,4)
g='''\\begin{axis}[width=7cm,height=5.4cm,xmin=0,xmax=1400,ymin=0,ymax=70,xtick={0,1200},ytick={20,50,60},tick label style={font=\\scriptsize},axis lines=left,xlabel={Verilen ısı (cal)},ylabel={Sıcaklık ($^\\circ$C)},xlabel style={font=\\small},ylabel style={font=\\small}]
\\addplot[thick,vurgu,mark=*,mark size=1.4pt] coordinates {(0,20) (1200,60)};
\\addplot[thick,mark=*,mark size=1.4pt] coordinates {(0,20) (1200,50)};
\\addplot[dotted,gray] coordinates {(1200,0) (1200,60)};
\\node[anchor=south west] at (axis cs:1220,60) {X};\\node[anchor=north west] at (axis cs:1220,50) {Y};
\\node[anchor=south,align=center,font=\\scriptsize] at (axis cs:560,48) {X: 100 g};
\\node[anchor=north,align=center,font=\\scriptsize] at (axis cs:700,30) {Y: 200 g};
\\end{axis}'''
SK=tk(g)
q('0006',tipId='fz-is2-qt-oran',tip='Isı–sıcaklık grafiğinden öz ısı oranı',z='orta',alt='Öz Isı ve Isı Sığası',kaz='Isı–sıcaklık grafiği ve kütle bilgisinden iki maddenin öz ısı oranını bulur.',kalip='grafik',
 kart='K-FZIS2-06 (Q–T grafiği) · X: 100 g, Y: 200 g',sekil=SK,
 metin='Aynı sıcaklıktan başlayan X ve Y katı cisimleri, ısı kaybı olmayacak biçimde ayrı ayrı ısıtılıyor ve cisimlere verilen ısıyla sıcaklıklarının nasıl değiştiği grafikte gösteriliyor. Cisimlerin kütleleri grafiğin üzerinde yazılıdır. Isıtma boyunca iki cisim de hâl değiştirmemektedir. Grafikteki son noktada iki cisme de aynı miktarda ısı verilmiştir.\nBuna göre X maddesinin öz ısısının Y maddesinin öz ısısına oranı (c_X/c_Y) kaçtır?',
 dogru=Fr(3,2),yan=[(Fr(1,2),'Yalnız kütle oranına bakmış (100/200); sıcaklık artışlarını katmamış.','dikkat'),(Fr(3,4),'Yalnız sıcaklık artışlarına bakmış (30/40) ve oranı ters kurmuş; kütleleri katmamış.','dikkat'),(1,'Aynı ısıyı aldıkları için öz ısıların eşit olduğunu sanmış.','bilgi'),(2,'Kütle oranını ters kullanmış (200/100); sıcaklık artışlarını katmamış.','islem')],
 istenen='c_X/c_Y oranı.',ip=['Öz ısı için ısıyı hem kütleye hem sıcaklık artışına böl; iki maddede aynı ısı kullanıldığından ısı sadeleşir.'],
 bilgi=[B('Öz ısı','c = Q ÷ (m · ΔT): 1 g maddenin sıcaklığını 1 °C değiştirmek için gerekli ısı. Aynı ısıyı alan maddelerde c, m · ΔT çarpımıyla ters orantılıdır. Örnek: aynı ısıyı alan iki maddeden birinin m · ΔT çarpımı 2 kat büyükse öz ısısı yarıdır')],
 ad=[A('Sıcaklık artışlarını oku','Başlangıç 20 °C.','ΔT_X = 60 − 20 = 40 · ΔT_Y = 50 − 20 = 30'),A('Öz ısıları yaz','Isı Q ortak.','c_X = Q ÷ (100 × 40) · c_Y = Q ÷ (200 × 30)'),A('Oranla','Q sadeleşir.','c_X/c_Y = (200 × 30) ÷ (100 × 40) = 6000 ÷ 4000'),A('Sonuç','Oran sadeleştirilir.','c_X/c_Y = 3/2 = 1,5')],
 puf='Aynı ısıda öz ısı oranı, (m · ΔT) çarpımlarının ters oranıdır.')

# ================= 07 · hâl değişimi T–t grafiği · zor · öncüllü =================
kartla('07','Hâl değişimi grafiğini yorumlama','Hâl değişimi sırasında sıcaklık sabit kalır, alınan ısı potansiyel enerjiyi artırır; eğimi küçük olan bölgede öz ısı büyüktür.','Isı alırken sıcaklığın artması gerektiğini sanmak; eğim–öz ısı ilişkisini ters kurmak.','orta','öncüllü',5,'hal-grafik','Hâl değişimi grafiği')
# P sabit, m sabit. Katı: 20→60, 4 dk: eğim 10 °C/dk. Sıvı: 60→100, 12 dk: eğim 10/3 °C/dk.  c = P/(m·eğim): c_sıvı = 3 c_katı.
sk=Fr(40,4); ss=Fr(40,12); assert sk/ss==3
# I: 0-4 dk'da iç enerji artar? Soru I: "4-10 dk arasında iç enerji değişmez" yanlış (ısı alıyor, iç enerji artar). II: 4–10 dk'da alınan ısı hâl değiştirmeye (tanecikler arası bağlar) harcanır, doğru. III: c_sıvı > c_katı doğru.
g='''\\begin{axis}[width=7.2cm,height=5.4cm,xmin=0,xmax=24,ymin=0,ymax=115,xtick={0,4,10,22},ytick={20,60,100},tick label style={font=\\scriptsize},axis lines=left,xlabel={Zaman (dk)},ylabel={Sıcaklık ($^\\circ$C)},xlabel style={font=\\small},ylabel style={font=\\small},extra x ticks={},grid=none]
\\addplot[thick,vurgu,mark=*,mark size=1.4pt] coordinates {(0,20) (4,60) (10,60) (22,100)};
\\addplot[dotted,gray] coordinates {(4,0) (4,60)};\\addplot[dotted,gray] coordinates {(10,0) (10,60)};\\addplot[dotted,gray] coordinates {(22,0) (22,100)};
\\addplot[dotted,gray] coordinates {(0,60) (4,60)};\\addplot[dotted,gray] coordinates {(0,100) (22,100)};
\\end{axis}'''
SK=tk(g)
q('0007',tipId='fz-is2-hal-grafik',tip='Hâl değişimi grafiği',z='orta',alt='Hâl Değişimi',kaz='Sabit güçle ısıtılan saf maddenin sıcaklık–zaman grafiğini yorumlar.',kalip='öncüllü',
 kart='K-FZIS2-07 (hâl değişimi T–t) · katı–erime–sıvı',sekil=SK,
 metin='Kütlesi sabit saf bir katı madde, birim zamanda sabit ısı veren bir ısıtıcıyla ısıtılıyor. Isı kaybı yoktur ve ısıtma sırasında maddenin sıcaklığının zamanla değişimi şekildeki grafikte gösterilmiştir. Grafikte maddenin önce katı hâlde ısındığı, sonra erime sırasında bir süre sıcaklığının değişmediği, erime bittikten sonra sıvı hâlde yeniden ısındığı görülmektedir.\nI. 4–10 dk aralığında madde ısı almadığı için iç enerjisi değişmez.\nII. 4–10 dk aralığında verilen ısı, taneciklerin birbirine bağlarının gevşemesine harcanır.\nIII. Sıvı hâlindeki maddenin öz ısısı katı hâlindekinden büyüktür.\nBuna göre bu yargılardan hangileri doğrudur?',
 dogru='II ve III',sira=['Yalnız I','Yalnız II','I ve II','I ve III','II ve III'],yan=[('Yalnız I','Sıcaklık sabit olduğu için madde ısı almıyor sanmış; erimede ısı alındığını ve iç enerjinin arttığını görmemiş.','bilgi'),('Yalnız II','III’ü yanlış saymış; sıvı bölgesinde eğimin daha küçük olmasının öz ısının büyük olduğu anlamına geldiğini görememiş.','islem'),('I ve II','II’yi doğru bulmuş; ama I’i de doğru saymış (sabit sıcaklıkta iç enerjinin sabit kaldığını düşünmüş) ve eğimle öz ısı ilişkisini ters kurup III’ü yanlış bulmuş.','bilgi'),('I ve III','I’i doğru bulmuş: sabit sıcaklıkta iç enerjinin sabit olduğunu sanmış; II’yi atlamış.','bilgi')],
 istenen='Doğru olan yargılar.',ip=['Isıtıcının gücü sabit olduğundan, aynı sürede verilen ısı eşittir; eğimin ısı sığasıyla nasıl bağlantılı olduğunu düşün.'],
 bilgi=[B('Hâl değişimi','saf maddede hâl değişimi sırasında sıcaklık sabit kalır; alınan ısı taneciklerin bağlarını gevşetip potansiyel enerjiyi artırır ve iç enerji yükselir. Örnek: kaynayan suya ısı verilmeye devam edilse de sıcaklığı 100 °C’de sabit kalır'),B('Eğim ve öz ısı','sabit güçte ısıtırken sıcaklık–zaman eğimi ΔT/Δt = P ÷ (m · c) olduğundan eğimi küçük olan bölgede öz ısı büyüktür')],
 ad=[A('I’i değerlendir','4–10 dk’da ısıtıcı ısı vermeye devam eder; erime sürer.','Q > 0 → iç enerji artar → I yanlış'),A('II’yi değerlendir','Sıcaklık (ortalama kinetik enerji) sabit; ısı tanecikler arası bağlara gider.','II doğru'),A('Eğimleri hesapla','Katı 4 dk’da 40 °C, sıvı 12 dk’da 40 °C ısınıyor.','eğim_katı = 10 °C/dk · eğim_sıvı ≈ 3,3 °C/dk'),A('Öz ısıları karşılaştır','c = P ÷ (m · eğim); eğim küçükse c büyük.','c_sıvı = 3 · c_katı → III doğru'),A('Sonuç','II ve III doğrudur.','II ve III')],
 puf='Saf maddede hâl değişiminde sıcaklık sabit kalsa da ısı alınır; sabit güçte eğimi küçük bölgenin öz ısısı büyüktür.')

# ================= 08 · buz–su karışımı, kalan buz · orta =================
kartla('08','Buz–su karışımında artan buz','Suyun 0 °C’ye inerken verdiği ısı ile buzun tamamını eritmek için gereken ısı karşılaştırılır; fark kadarı buz kalır.','Buzun tamamen eridiğini sanmak; erime ısısını hesaba katmamak; suyun kütlesi yerine buzun kütlesini kullanmak.','orta','şekilli',4,'buz-kalan','Buz–su karışımında kalan buz')
mb,ms,ts,Lm=200,300,20,80
ver=ms*ts; ger=mb*Lm; assert ver<ger
erir=Fr(ver,Lm); kalan=mb-erir; assert erir==75 and kalan==125 and Fr(mb*ts,Lm)==50 and mb-Fr(mb*ts,Lm)==150
g=''
# buz kabı
g+=beaker(0,0)
for (a,b) in [(.12,.0),(.62,.0),(1.12,.0),(.37,.45),(.87,.45)]:
    g+=f'\\draw[thick,fill=white] ({a},{b}) rectangle ({a+.4},{b+.4});'
g+='\\node[below,align=center] at (.8,-.05) {yalnız buz\\\\ 200 g, $0\\,^\\circ$C};'
g+=beaker(3.4,1.5)+'\\node[below,align=center] at (4.2,-.05) {Su\\\\ 300 g, $20\\,^\\circ$C};'
g+=f'\\draw[{ARR},very thick] (5.6,.9) -- (6.6,.9);'
# yalıtılmış kap
g+='\\draw[thick] (6.8,2.6) -- (6.8,0) -- (9.0,0) -- (9.0,2.6); \\draw[thick] (7.0,2.6) -- (7.0,.2) -- (8.8,.2) -- (8.8,2.6);\\fill[pattern=north east lines] (6.8,0) -- (6.8,2.6) -- (7.0,2.6) -- (7.0,.2) -- (8.8,.2) -- (8.8,2.6) -- (9.0,2.6) -- (9.0,0) -- cycle;'
g+='\\node[below,align=center] at (7.9,-.05) {yalıtılmış boş kap};'
SK=tk(g)
q('0008',tipId='fz-is2-buz-kalan',tip='Buz–su karışımında kalan buz',z='orta',alt='Hâl Değişimi',kaz='Isı alışverişini kullanarak buz–su karışımında erimeden kalan buz kütlesini bulur.',kalip='şekilli',
 kart='K-FZIS2-08 (buz–su, kalan buz) · 200 g buz, 300 g su',sekil=SK,
 metin='Bir öğrenci, şekilde görülen buz ile suyu, ısı alışverişi yapmayan boş bir kaba boşaltıp karıştırıyor. Soldaki kapta yalnızca buz vardır. Buzun erime ısısı 80 cal/g, suyun öz ısısı 1 cal/g·°C’dir; buz ve suyun kütleleri ile sıcaklıkları şekilde verilmiştir. Kaba dışarıdan hiç ısı girmemekte ve çıkmamaktadır. Öğrenci bir süre bekleyip kaptaki karışımın ısıl dengeye ulaşmasını sağlıyor ve ardından karışımın içinde buz bulunup bulunmadığına bakıyor.\nBuna göre ısıl denge kurulduktan sonra kapta kaç g buz kalmıştır?',
 dogru=125,yan=[(0,'Buzun tamamen eridiğini sanmış; suyun verdiği ısı (6000 cal), buzu tümüyle eritmek için gereken ısıdan (16000 cal) küçüktür.','dikkat'),(75,'Eriyen buz kütlesini (75 g) bulmuş fakat kalan buzu değil, eriyen miktarı yazmış.','dikkat'),(150,'Eriyen kütleyi buzun kütlesi ile sıcaklık farkından hesaplamış (200 × 20 ÷ 80 = 50 g); verilen ısı suyun kütlesiyle bulunur.','islem'),(200,'Su hiç ısı vermemiş gibi buzun hiç erimediğini düşünmüş.','bilgi')],
 istenen='Denge kurulduğunda kalan buzun kütlesi (g).',ip=['Önce suyun 0 °C’ye kadar soğurken verebileceği ısıyı, sonra o ısının kaç gram buzu eritebileceğini bul.'],
 bilgi=[B('Erime ısısı','L (cal/g): 0 °C’deki 1 g buzu aynı sıcaklıkta suya çevirmek için gereken ısı. Q = m·L. Örnek: 10 g buz için 10 × 80 = 800 cal gerekir'),B('Isıl denge','verilen ısı alınan ısıya eşittir')],
 ad=[A('Suyun verebileceği ısı','Su 20 °C’den 0 °C’ye iner.','Q = 300 × 1 × 20 = 6000 cal'),A('Tüm buzu eritme ısısı','Karşılaştırma için gerekir.','Q = 200 × 80 = 16000 cal'),A('Karşılaştır','Su verdiği ısıyla buzun hepsini eritemez; denge sıcaklığı 0 °C olur.','6000 < 16000 → buz kalır'),A('Eriyen buz','Su verdiği 6000 cal’i buzu eritmeye harcar.','m = 6000 ÷ 80 = 75 g'),A('Kalan buz','Başlangıç buz kütlesinden eriyen çıkarılır.','200 − 75 = 125 g')],
 puf='Önce “buz tamamen erir mi?” sorusunu ısıları karşılaştırarak yanıtla; erimiyorsa denge 0 °C’dedir.')

# ================= 09 · kaynama · zor · metin =================
kartla('09','Isıtıcıyla ısıtılan suyun buharlaşması','Önce suyu kaynama sıcaklığına getirmek için gereken ısı, kalan ısı ise buharlaşma ısısıyla kütleye çevrilir.','Isınma ısısını unutmak; suyu 0 °C’den başlatmak; kaynamaya hiç ulaşmadığını sanmak.','zor','düz',5,'buharlasma','Isıtıcıyla suyun buharlaşması')
m0,P0,t0,Lv=135,300,90,540
Qt=P0*t0; Qis=m0*(100-20)*1; ev=Fr(Qt-Qis,Lv); kal=m0-ev
assert Qt==27000 and Qis==10800 and ev==30 and kal==105
assert m0-Fr(Qt,Lv)==85 and m0-Fr(Qt-m0*100,Lv)==110
q('0009',tipId='fz-is2-buharlasma',tip='Isıtıcıyla suyun buharlaşması',z='zor',alt='Hâl Değişimi',kaz='Isıtma süresi ve gücünden buharlaşan su kütlesini bularak kalan suyu hesaplar.',kalip='düz',
 kart='K-FZIS2-09 (ısıtıcı + buharlaşma) · 135 g su, 300 cal/s, 90 s',
 metin='Açık bir kapta, sıcaklığı 20 °C olan 135 g su, saniyede 300 cal ısı veren bir elektrikli ısıtıcıyla tam 90 saniye boyunca ısıtılıyor. Isıtıcının verdiği enerjinin tamamı suya aktarılmaktadır; kap, çevre ve ısıtıcı için ısı alışverişi hesaba katılmayacaktır. Su 100 °C’de kaynamakta, oluşan buhar kaptan uzaklaşmaktadır. Suyun öz ısısı 1 cal/g·°C, kaynama (buharlaşma) ısısı 540 cal/g’dır.\nBuna göre ısıtma bittiğinde kapta kaç g su kalmıştır?',
 dogru=105,yan=[(30,'Kalan su yerine buharlaşan su miktarını (30 g) yazmış.','dikkat'),(85,'Suyu 100 °C’ye getirmek için harcanan ısıyı (10800 cal) unutmuş: 27000 ÷ 540 = 50 g buharlaşmış sanıp 135 − 50 = 85 g bulmuş.','dikkat'),(110,'Isınma ısısını 20 °C yerine 0 °C’den hesaplamış (135 × 100 = 13500 cal); buharlaşan 25 g sanıp 110 g bulmuş.','islem'),(135,'Suyun kaynamaya ulaşmayıp hiç buharlaşmadığını düşünmüş.','bilgi')],
 istenen='Isıtma bittiğinde kapta kalan suyun kütlesi (g).',ip=['Isıtıcının verdiği ısının tamamı suyu kaynama sıcaklığına getirmeye mi harcanıyor?'],
 bilgi=[B('Isıtıcı gücü ve ısı','sabit güçle ısıtmada toplam ısı Q = P · t’dir. Örnek: 50 cal/s’lik ısıtıcı 10 s’de 500 cal verir'),B('Buharlaşma ısısı','kaynama sıcaklığındaki 1 g sıvıyı aynı sıcaklıkta buhara çevirmek için gereken ısıdır; Q = m · L')],
 ad=[A('Verilen toplam ısı','Güç × süre.','Q = 300 × 90 = 27000 cal'),A('Kaynama sıcaklığına çıkarma','Su 20 °C’den 100 °C’ye çıkar.','Q₁ = 135 × 1 × 80 = 10800 cal'),A('Buharlaşmaya kalan ısı','Toplamdan ısınma ısısı çıkarılır.','Q₂ = 27000 − 10800 = 16200 cal'),A('Buharlaşan su','Q₂ = m · L.','m = 16200 ÷ 540 = 30 g'),A('Kalan su','Başlangıç kütlesinden buharlaşan çıkarılır.','135 − 30 = 105 g')],
 puf='Isıtıcıyla ısıtmada önce sıcaklığı kaynamaya çıkaran ısıyı, sonra kalan ısıyı buharlaşmaya ayır.')

# ================= 10 · metal–su ısıl dengesi · orta =================
kartla('10','Farklı maddelerin ısıl dengesi','Verilen ısı alınan ısıya eşit: m₁c₁(T₁ − T) = m₂c₂(T − T₂).','Öz ısıları hesaba katmayıp kütlelerle ortalama almak; ısı sığalarını ters yerleştirmek.','orta','şekilli',4,'metal-su','Metal ve su arasında ısıl denge')
mb_,cb,Tb=200,Fr(1,5),90; mw,cw,Tw=60,1,None; Tw0=20
Cb,Cw=mb_*cb,mw*cw; T=Fr(Cb*Tb+Cw*Tw0,Cb+Cw); assert (Cb,Cw)==(40,60) and T==48
assert Fr(Tb+Tw0,2)==55 and Fr(Cw*Tb+Cb*Tw0,Cb+Cw)==62 and Tb-Tw0==70 and Tb-T==42
g=beaker(0,1.4,w=2.2,h=2.4)+'\\node at (1.1,.7) {60 g su}; \\node[below] at (1.1,-.05) {$20\\,^\\circ$C};'
g+='\\draw[thick] (1.1,4.6) -- (1.1,3.95);\\draw[thick,fill=gray!40] (1.1,3.5) circle (.45);'
g+='\\node[right,align=left] at (1.8,3.5) {200 g metal\\\\ $90\\,^\\circ$C\\\\ $c=0{,}2$ cal/g$\\cdot^\\circ$C};'
g+=f'\\draw[{ARR}] (1.1,2.8) -- (1.1,1.7);'
SK=tk(g)
q('0010',tipId='fz-is2-metal-su',tip='Metal ve su arasında ısıl denge',z='orta',alt='Isıl Denge',kaz='Farklı öz ısılı maddelerin ısıl denge sıcaklığını ısı sığalarıyla hesaplar.',kalip='şekilli',
 kart='K-FZIS2-10 (metal–su) · 200 g metal, 60 g su',sekil=SK,
 metin='Bir öğrenci, ısıtılmış metal bir küreyi ince bir iple tutarak şekildeki beherde bulunan suya sarkıtıyor ve kürenin suya tamamen batmasını sağlıyor. Kürenin kütlesi, ilk sıcaklığı ve öz ısısı ile suyun kütlesi ve ilk sıcaklığı şekilde verilmiştir. Suyun öz ısısı 1 cal/g·°C’dir. Kap, ip ve çevre ile ısı alışverişi ihmal edilecektir; su kaynamamakta ve taşmamaktadır.\nBuna göre ısıl denge kurulduğunda suyun sıcaklığı kaç °C olur?',
 dogru=48,yan=[(42,'Denge sıcaklığı yerine kürenin sıcaklık düşüşünü (90 − 48 = 42 °C) yazmış.','dikkat'),(55,'Kütlelere ve öz ısılara bakmadan iki sıcaklığın ortalamasını (90 ile 20’nin ortası) almış.','bilgi'),(62,'Isı sığalarını ters yerleştirmiş: (60 × 90 + 40 × 20) ÷ 100 = 62.','islem'),(70,'Sıcaklık farkını (90 − 20) denge sıcaklığı sanmış.','dikkat')],
 istenen='Isıl denge sıcaklığı (°C).',ip=['Her iki cismin ısı sığasını bul; verilen ısı alınan ısıya eşit olacak.'],
 bilgi=[B('Isıl denge','sıcak cismin verdiği ısı soğuk cismin aldığı ısıya eşittir: m₁c₁(T₁ − T) = m₂c₂(T − T₂). Örnek: ısı sığası 30 cal/°C olan 80 °C’lik cisim, ısı sığası 10 cal/°C olan 40 °C’lik cisimle dengede 70 °C’de buluşur')],
 ad=[A('Isı sığaları','C = m × c.','C_metal = 200 × 0,2 = 40 · C_su = 60 × 1 = 60 cal/°C'),A('Eşitliği yaz','Verilen ısı alınan ısıya eşit.','40 × (90 − T) = 60 × (T − 20)'),A('Düzenle','Parantezleri aç.','3600 − 40T = 60T − 1200'),A('T’yi bul','T’li terimleri topla.','4800 = 100T → T = 48 °C')],
 puf='Farklı maddelerde önce ısı sığalarını (m·c) bul, denge sıcaklığına ısı sığası büyük olan daha yakın olur.')

# ================= 11 · ısıl denge grafiği · orta · öncüllü =================
kartla('11','Isıl denge grafiğini yorumlama','Verilen ısı alınan ısıya eşit: C_A·ΔT_A = C_B·ΔT_B; denge sıcaklığı sıcaklıkların ortalaması olmak zorunda değildir.','Denge sıcaklığını ortalama almak; ΔT büyük olana büyük ısı sığası demek.','orta','öncüllü',4,'denge-grafik','Isıl denge sıcaklığı–zaman grafiği')
TA,TB,Te=90,20,50; dA,dB=TA-Te,Te-TB
assert dA==40 and dB==30 and Fr(dB,dA)==Fr(3,4)       # C_A*40 = C_B*30 -> C_A = 0,75 C_B -> A'nın ısı sığası küçük
assert Fr(TA+TB,2)==55
# I doğru (C_A < C_B). II: denge 55 °C yanlış (50). III: A'nın verdiği ısı B'nin aldığına eşit, doğru (yalıtılmış).
g='''\\begin{axis}[width=7.2cm,height=5.4cm,xmin=0,xmax=14,ymin=0,ymax=105,xtick=\\empty,ytick={20,50,90},tick label style={font=\\scriptsize},axis lines=left,xlabel={Zaman},ylabel={Sıcaklık ($^\\circ$C)},xlabel style={font=\\small},ylabel style={font=\\small}]
\\addplot[thick,vurgu,domain=0:14,samples=40] {50+40*exp(-x/3)};
\\addplot[thick,domain=0:14,samples=40] {50-30*exp(-x/3)};
\\addplot[dashed,gray] coordinates {(0,50) (14,50)};
\\node[anchor=south west] at (axis cs:.3,90) {A}; \\node[anchor=north west] at (axis cs:.3,20) {B};
\\end{axis}'''
SK=tk(g)
q('0011',tipId='fz-is2-denge-grafik',tip='Isıl denge sıcaklığı–zaman grafiği',z='orta',alt='Isıl Denge',kaz='Isıl denge grafiğinden ısı sığaları ve verilen–alınan ısı ilişkisini yorumlar.',kalip='öncüllü',
 kart='K-FZIS2-11 (denge grafiği) · A: 90→50, B: 20→50',sekil=SK,
 metin='Çevreyle ısı alışverişi yapmayan bir kabın içine, birbirine temas eden A ve B cisimleri konulmuş ve iki cismin sıcaklığı zamana karşı kaydedilmiştir. Kaydedilen sıcaklık–zaman grafiği şekildeki gibidir. Cisimler hâl değiştirmemiştir. Grafikte iki cismin sıcaklığının zamanla birbirine yaklaştığı ve belli bir değerde sabitlendiği görülmektedir.\nI. A cisminin ısı sığası B cisminin ısı sığasından küçüktür.\nII. Isıl denge sıcaklığı, cisimlerin başlangıç sıcaklıklarının aritmetik ortalamasına eşittir.\nIII. A’nın verdiği ısı, B’nin aldığı ısıya eşittir.\nBuna göre bu yargılardan hangileri doğrudur?',
 dogru='I ve III',sira=S_STD,yan=[('Yalnız I','III’ü atlamış; yalıtılmış sistemde verilen ısının alınan ısıya eşit olduğunu görmemiş.','bilgi'),('Yalnız II','Denge sıcaklığını iki sıcaklığın ortalaması (55 °C) sanmış; grafikte ise denge 50 °C’de.','dikkat'),('I ve II','II’yi doğru saymış: kütleler farklı olabileceğinden ortalama kuralı geçerli değildir; III’ü atlamış.','bilgi'),('I, II ve III','II’yi de doğru bulmuş; denge sıcaklığının ortalamaya eşit olduğunu düşünmüş.','bilgi')],
 istenen='Doğru olan yargılar.',ip=['Grafikten iki cismin sıcaklık değişimlerini oku; verilen ve alınan ısıyı ısı sığası ve sıcaklık değişimi cinsinden yaz.'],
 bilgi=[B('Isıl denge ve ısı sığası','yalıtılmış sistemde sıcak cismin verdiği ısı soğuk cismin aldığı ısıya eşittir: C₁·ΔT₁ = C₂·ΔT₂. Sıcaklık değişimi büyük olan cismin ısı sığası küçüktür. Örnek: ΔT₁ = 20 °C, ΔT₂ = 10 °C ise C₁ = C₂ ÷ 2')],
 ad=[A('Sıcaklık değişimleri','Grafikten oku.','A: 90 → 50 (40 °C düşer) · B: 20 → 50 (30 °C artar)'),A('Isı eşitliği','Verilen ısı alınan ısıya eşit (III doğru).','C_A × 40 = C_B × 30'),A('I’i incele','C_A, C_B’nin 3/4’üdür.','C_A < C_B → I doğru'),A('II’yi incele','Denge 50 °C; ortalama 55 °C.','II yanlış → I ve III')],
 puf='Isıl denge sıcaklığı ortalama değildir; ısı sığası büyük olan cismin sıcaklığı daha az değişir.')

# ================= 12 · enerji iletim yolları · kolay · öncüllü =================
kartla('12','Üç enerji iletim yolunu ayırt etme','İletimde madde taşınmadan tanecikler aracılığıyla, konveksiyonda akışkanın yer değiştirmesiyle, ışımada ortamsız enerji aktarılır.','İletimde de maddenin taşındığını sanmak; ışımayı ortam gerektiren sanmak.','kolay','öncüllü',3,'iletim-yol','Enerji iletim yolları')
# I (yanlış): K'de madde çubuk boyunca taşınır -> iletimde madde taşınmaz. II (yanlış): L'de suda iletim, yer değiştirme gerekmez -> konveksiyon. III (doğru): Güneş–Dünya ışıma, ortam gerekmez.
g=''
g+='\\fill[vurgu!45] (.3,-.55) ellipse (.22 and .38); \\draw[thick,fill=gray!25] (0,-.2) rectangle (3.2,.2); \\node[above] at (1.6,.25) {\\textbf{K}}; \\node[below,align=center] at (1.6,-.9) {metal çubuk};'
g+='\\draw[thick] (4.7,2.4) -- (4.7,0) -- (6.5,0) -- (6.5,2.4); \\fill[vurgu!15] (4.7,0) rectangle (6.5,1.7);\\draw[thick] (4.7,2.4) -- (4.7,0) -- (6.5,0) -- (6.5,2.4);\\fill[vurgu!45] (5.6,-.6) ellipse (.22 and .38); \\node[above] at (5.6,2.45) {\\textbf{L}}; \\node[below,align=center] at (5.6,-1.05) {alttan ısıtılan su};'
g+='\\draw[thick] (8.2,1.0) circle (.6); \\foreach \\a in {0,45,...,315}{\\draw (8.2,1.0)++(\\a:.75) -- ++(\\a:.3);} \\draw[thick,fill=white] (11.6,1.0) circle (.28); \\node[above] at (9.9,1.9) {\\textbf{M}}; \\node[below,align=center] at (9.9,.0) {Güneş\\ \\ \\ \\ \\ \\ \\ Dünya};'
g+=f'\\draw[dotted,{ARR}] (8.95,1.0) -- (11.25,1.0);'
SK=tk(g)
q('0012',tipId='fz-is2-iletim-yol',tip='Enerji iletim yolları',z='kolay',alt='Isı İletim Yolları',kaz='İletim, konveksiyon ve ışıma yollarını günlük örneklerle ayırt eder.',kalip='öncüllü',
 kart='K-FZIS2-12 (iletim, konveksiyon, ışıma) · metal çubuk, kaynayan su, Güneş',sekil=SK,
 metin='Bir fen laboratuvarında öğrenciler, üç farklı enerji aktarımı örneğini şekildeki gibi sunmuştur. K’de bir ucu alevle ısıtılan metal çubuk, L’de altından ısıtılan su dolu bir kap, M’de ise Güneş’ten Dünya’ya ulaşan enerji gösterilmiştir. Öğretmen öğrencilerden bu üç olayda enerjinin nasıl aktarıldığını yorumlamalarını istemiştir.\nI. K’deki çubukta enerji, madde çubuk boyunca akarak aktarılır.\nII. L’deki suda enerji, iletimle aktarılır.\nIII. M’deki enerji aktarımı için maddesel bir ortam gerekmez.\nBuna göre bu yargılardan hangileri doğrudur?',
 dogru='Yalnız III',sira=sira('Yalnız I','Yalnız III','I ve II','I ve III','II ve III'),yan=[('Yalnız I','III’ü yanlış sanmış; ışımanın ortam istemediğini bilmemiş.','bilgi'),('I ve II','Işıma için ortam gerektiğini düşünüp III’ü yanlış saymış; iletimde maddenin akmadığını da görmemiş.','bilgi'),('I ve III','I’i doğru saymış; iletimde maddenin yer değiştirmediğini, yalnız enerjinin tanecikler aracılığıyla aktarıldığını bilmemiş.','bilgi'),('II ve III','II’de konveksiyonu iletim saymış; akışkanlarda ısınan kısmın yer değiştirmesinin konveksiyon olduğunu karıştırmış.','bilgi')],
 istenen='Doğru olan yargılar.',ip=['Her olayda enerjinin maddeyle mi, maddeden bağımsız mı aktarıldığını sorgula.'],
 bilgi=[B('Enerji iletim yolları','iletim: enerji tanecikten taneciğe aktarılır, madde yer değiştirmez (katılarda baskın) · konveksiyon: sıvı ve gazlarda ısınan maddenin yer değiştirmesiyle · ışıma: ortam gerektirmez, boşlukta da olur. Örnek: sobanın yanındaki kişinin ısınması ışımadır')],
 ad=[A('K’yi incele','Katı çubuk: tanecik titreşimleriyle iletim.','Madde taşınmaz → I yanlış'),A('L’yi incele','Isınan su yükselir, soğuk su iner: konveksiyon.','II yanlış (yer değiştirme var)'),A('M’yi incele','Güneş–Dünya arası boşluktur; ışıma.','III doğru'),A('Sonuç','Yalnız III doğrudur.','Yalnız III')],
 puf='İletimde madde yerinde kalır, konveksiyonda yer değiştirir, ışımada ortam gerekmez.')

# ================= 13 · meltem · orta · şekilli =================
kartla('13','Kara–deniz meltemi','Kara öz ısısı küçük olduğundan gündüz daha çok ısınır; sıcak havanın yükselmesiyle alt katmanda denizden karaya, üst katmanda karadan denize hava akımı oluşur.','Alt ve üst katman akımlarını karıştırmak; gece–gündüz yönünü ters kurmak.','orta','şekilli',4,'meltem','Kara–deniz meltemi')
g='\\fill[vurgu!15] (-.2,-.7) rectangle (3.3,0); \\fill[pattern=north east lines] (3.3,-.7) rectangle (7.0,0); \\draw[thick] (-.2,0) -- (3.3,0) -- (3.3,-.7); \\draw[thick] (3.3,0) -- (7.0,0);\\draw[thick] (-.2,-.7) -- (7.0,-.7);'
g+='\\node at (1.6,-.35) {deniz}; \\node at (5.1,-.35) {kara};'
g+='\\node[above] at (1.6,.05) {$22\\,^\\circ$C}; \\node[above] at (5.1,.05) {$31\\,^\\circ$C};'
def okc(n,x1,x2,y):
    return f'\\draw[thick,{ARR}] ({x1},{y}) -- ({x2},{y}); \\node[draw,circle,inner sep=1pt,fill=white] at ({(x1+x2)/2},{y+.4}) {{\\footnotesize {n}}};'
g+=okc(1,.4,2.0,.95)+okc(2,6.2,4.6,.95)+okc(3,6.2,4.6,2.6)+okc(4,.4,2.0,2.6)
g+='\\node[align=left,anchor=west] at (7.2,.95) {alt katman}; \\node[align=left,anchor=west] at (7.2,2.6) {üst katman};'
SK=tk(g)
q('0013',tipId='fz-is2-meltem',tip='Kara–deniz meltemi',z='orta',alt='Isı İletim Yolları',kaz='Kara ve denizin farklı ısınmasından oluşan hava akımlarının yönünü belirler.',kalip='şekilli',
 kart='K-FZIS2-13 (meltem) · gündüz, kara 31 °C, deniz 22 °C',sekil=SK,
 metin='Bir kıyı kentinde öğle saatlerinde yapılan ölçümlerde güneşli bir havada karanın yüzey sıcaklığının 31 °C, denizin yüzey sıcaklığının 22 °C olduğu belirleniyor. Kıyı kesiti şekilde gösterilmiştir. Rüzgâr kaynağı olarak yalnızca kara ile deniz arasındaki sıcaklık farkı dikkate alınacaktır. Şekilde, alt ve üst katmanlarda ikişer olası hava akımı numaralı oklarla çizilmiştir.\nBuna göre bu sırada gerçekleşen hava akımlarını hangi iki ok doğru göstermektedir?',
 dogru='1 ve 3',sira=['1 ve 2','1 ve 3','1 ve 4','2 ve 4','3 ve 4'],yan=[('1 ve 2','Alt katmanda iki yönde de akım olduğunu sanmış; aynı katmanda hava tek yönde akar.','bilgi'),('1 ve 4','Üst katmanda hava akımını da denizden karaya doğru çizmiş; üst katmanda akım karadan denize gider.','dikkat'),('2 ve 4','Akımların yönünü tam tersine, gece meltemi gibi düşünmüş.','dikkat'),('3 ve 4','Üst katmanda iki yönde de akım olduğunu sanmış; alt katmandaki akımı atlamış.','bilgi')],
 istenen='Doğru hava akımlarını gösteren oklar.',ip=['Hangi bölgede hava ısınıp yükselir? Yükselen havanın bıraktığı boşluğu nereden gelen hava doldurur?'],
 bilgi=[B('Meltem','kara özısısı küçük olduğundan çabuk ısınır ve çabuk soğur; deniz yavaş ısınır. Gündüz karanın üstündeki sıcak hava yükselir: alt katmanda deniz→kara, üst katmanda kara→deniz akım oluşur. Gece tersi olur')],
 ad=[A('Isınan bölgeyi bul','Kara 31 °C, deniz 22 °C; kara daha sıcak.','Kara üstündeki hava ısınıp yükselir'),A('Alt katmanı yaz','Yükselen havanın yerini soğuk deniz havası doldurur.','Alt: deniz → kara (ok 1)'),A('Üst katmanı yaz','Yükselen sıcak hava üstte denize doğru yayılır.','Üst: kara → deniz (ok 3)'),A('Sonuç','Doğru oklar 1 ve 3’tür.','1 ve 3')],
 puf='Gündüz kara sıcaktır: alt katmanda hava denizden karaya, üst katmanda karadan denize gider.')

# ================= 14 · iletim hızı · orta =================
kartla('14','Isı iletim hızı oranı','İletilen ısı akışı, kesit alanı ve sıcaklık farkıyla doğru, uzunlukla ters orantılıdır (aynı maddede).','Uzunluğu çarpan, sıcaklık farkını atlama; kesit alanı oranını ters yazma.','orta','şekilli',4,'iletim-hizi','Isı iletim hızı')
AK,LK,dtK=2,20,100-20; AL,LL,dtL=6,40,100-40
oran=Fr(AL,AK)*Fr(dtL,dtK)/Fr(LL,LK); assert oran==Fr(9,8)
assert Fr(AL,AK)*Fr(dtL,dtK)==Fr(9,4) and Fr(AL,AK)/Fr(LL,LK)==Fr(3,2) and Fr(dtL,dtK)/Fr(LL,LK)==Fr(3,8) and Fr(AL,AK)*Fr(dtL,dtK)*Fr(LL,LK)==Fr(9,2)
g=''
g+='\\fill[pattern=north east lines] (-.7,1.3) rectangle (-.2,1.9); \\draw[thick] (-.7,1.3) rectangle (-.2,1.9); \\draw[thick,fill=gray!25] (0,1.4) rectangle (2.0,1.8); \\fill[pattern=north east lines] (2.2,1.3) rectangle (2.7,1.9); \\draw[thick] (2.2,1.3) rectangle (2.7,1.9);'
g+='\\node[left] at (-.8,1.6) {$100\\,^\\circ$C}; \\node[right] at (2.8,1.6) {$20\\,^\\circ$C}; \\node[above] at (1.0,1.85) {K · kesit 2 cm$^2$}; \\draw[<->,thin] (0,1.15) -- (2.0,1.15); \\node[below] at (1.0,1.15) {20 cm};'
g+='\\fill[pattern=north east lines] (-.7,-1.0) rectangle (-.2,.2); \\draw[thick] (-.7,-1.0) rectangle (-.2,.2); \\draw[thick,fill=gray!25] (0,-.9) rectangle (4.0,.1); \\fill[pattern=north east lines] (4.2,-1.0) rectangle (4.7,.2); \\draw[thick] (4.2,-1.0) rectangle (4.7,.2);'
g+='\\node[left] at (-.8,-.4) {$100\\,^\\circ$C}; \\node[right] at (4.8,-.4) {$40\\,^\\circ$C}; \\node at (2.0,-.4) {L · kesit 6 cm$^2$}; \\draw[<->,thin] (0,-1.25) -- (4.0,-1.25); \\node[below] at (2.0,-1.25) {40 cm};'
SK=tk(g)
q('0014',tipId='fz-is2-iletim-hizi',tip='Isı iletim hızı',z='orta',alt='Isı İletim Yolları',kaz='Isı iletim hızının uzunluk, kesit alanı ve sıcaklık farkıyla ilişkisini oranlayarak uygular.',kalip='şekilli',
 kart='K-FZIS2-14 (iletim hızı oranı) · K ve L çubukları',sekil=SK,
 metin='Aynı maddeden yapılmış K ve L çubuklarının yan yüzeyleri ısı yalıtımlıdır. Çubukların uçları şekildeki gibi sabit sıcaklıktaki ısı kaynaklarına temas ettirilmiş ve ısı akışının kararlı hâle gelmesi beklenmiştir. Çubukların uzunlukları, kesit alanları ve uçlarının sıcaklıkları şekilde verilmiştir. Isı yalnızca çubuk boyunca iletilmektedir.\nBuna göre L çubuğunda birim zamanda iletilen ısının K çubuğunda birim zamanda iletilen ısıya oranı kaçtır?',
 dogru=Fr(9,8),yan=[(Fr(3,8),'Kesit alanı oranını (3 kat) hesaba katmamış.','dikkat'),(Fr(3,2),'Sıcaklık farkını katmamış: kesit alanı ve uzunluk oranıyla (3 ÷ 2) hesaplamış.','dikkat'),(Fr(9,4),'Uzunluk oranını katmamış: kesit alanı ve sıcaklık farkı oranlarını çarpmış.','dikkat'),(Fr(9,2),'Uzunluğu da çarpan olarak kullanmış (uzun çubukta daha çok ısı geçer sanmış).','bilgi')],
 istenen='Isı iletim hızı oranı.',ip=['Isı iletim hızını etkileyen üç niceliği (kesit alanı, uzunluk, uçlar arasındaki sıcaklık farkı) K ve L için ayrı ayrı oranla.'],
 bilgi=[B('Isı iletim hızı','aynı maddede birim zamanda iletilen ısı, kesit alanı ve uçlar arasındaki sıcaklık farkıyla doğru, uzunlukla ters orantılıdır: H ∝ A · ΔT ÷ L. Örnek: kesit 2 kat, uzunluk 2 kat olursa iletim hızı değişmez')],
 ad=[A('Kesit alanı oranı','L daha kalın.','A_L/A_K = 6/2 = 3'),A('Sıcaklık farkı oranı','K: 100 − 20; L: 100 − 40.','ΔT_L/ΔT_K = 60/80 = 3/4'),A('Uzunluk oranı','Uzunluk ters orantılı.','L_L/L_K = 40/20 = 2'),A('Birleştir','A · ΔT ÷ L oranları çarpılır.','H_L/H_K = 3 × (3/4) ÷ 2 = 9/8')],
 puf='Aynı maddede iletim hızı oranı = (kesit oranı × sıcaklık farkı oranı) ÷ uzunluk oranıdır.')

# ================= 15 · yalıtım · kolay · öncüllü (termos) =================
kartla('15','Isı yalıtımı (termos)','Vakum iletim ve konveksiyonu, parlak yüzey ışımayı, yalıtkan kapak iletimi azaltır; vakum ışımayı azaltmaz.','Vakumun ışımayı da önlediğini sanmak; parlak yüzeyi iletimle ilişkilendirmek.','kolay','öncüllü',3,'yalitim','Isı yalıtımı')
# I yanlış (vakum ışımayı azaltmaz), II doğru, III doğru -> II ve III
g='\\fill[vurgu!15] (.6,.6) rectangle (2.8,3.0);\\draw[thick,rounded corners=5pt] (0,3.6) -- (0,0) -- (3.4,0) -- (3.4,3.6);\\draw[thick,rounded corners=5pt] (.6,3.6) -- (.6,.6) -- (2.8,.6) -- (2.8,3.6); \\draw[thick] (0,3.6) -- (.6,3.6) (2.8,3.6) -- (3.4,3.6);'
g+='\\draw[very thick,gray] (.12,3.5) -- (.12,.12) -- (3.28,.12) -- (3.28,3.5); \\draw[very thick,gray] (.48,3.5) -- (.48,.48) -- (2.92,.48) -- (2.92,3.5);'
g+='\\draw[thick,fill=white,pattern=north east lines] (.6,3.6) rectangle (2.8,3.95);\\draw[thick] (.6,3.6) rectangle (2.8,3.95);'
g+='\\draw (4.4,1.2) -- (3.1,1.2); \\node[draw,circle,inner sep=1pt,fill=white] at (4.4,1.2) {\\footnotesize 1};'
g+='\\draw (4.4,2.6) -- (3.28,2.6); \\node[draw,circle,inner sep=1pt,fill=white] at (4.4,2.6) {\\footnotesize 2};'
g+='\\draw (4.4,3.8) -- (2.8,3.8); \\node[draw,circle,inner sep=1pt,fill=white] at (4.4,3.8) {\\footnotesize 3};'
g+='\\node[align=left,anchor=west] at (4.7,1.2) {\\scriptsize iç ve dış cidar arası}; \\node[align=left,anchor=west] at (4.7,2.6) {\\scriptsize cidarlardaki parlak kaplama}; \\node[align=left,anchor=west] at (4.7,3.8) {\\scriptsize kapak};'
SK=tk(g)
q('0015',tipId='fz-is2-yalitim',tip='Isı yalıtımı',z='kolay',alt='Isı Yalıtımı',kaz='Termos örneğinde yalıtım düzeneklerinin hangi iletim yolunu engellediğini belirtir.',kalip='öncüllü',
 kart='K-FZIS2-15 (termos kesiti) · vakum, parlak kaplama, kapak',sekil=SK,
 metin='Sıcak çayı uzun süre sıcak tutan bir termosun kesiti şekilde numaralanmış parçalarla gösterilmiştir. Termosun iç ve dış cidarı arasındaki boşluktan hava, vakum pompasıyla çekilmiştir; cidarların birbirine bakan yüzleri parlak bir kaplamayla kaplıdır, kapak ise ısı yalıtkanı maddeden yapılmıştır. Öğrenciler, termosun içindeki çayın neden uzun süre sıcak kaldığını yorumlayacaktır.\nI. 1 numaralı bölgenin havasının boşaltılması, ışımayla ısı kaybını azaltır.\nII. 2 numaralı parlak kaplama, ışımayla ısı kaybını azaltır.\nIII. 3 numaralı kapağın yalıtkan olması, kapaktan iletimle ısı kaybını azaltır.\nBuna göre bu yargılardan hangileri doğrudur?',
 dogru='II ve III',sira=['Yalnız I','Yalnız II','I ve II','I ve III','II ve III'],yan=[('Yalnız I','Vakumun ışımayı da azalttığını sanmış; parlak yüzeyin ve yalıtkan kapağın etkisini görmemiş.','bilgi'),('Yalnız II','Parlak kaplamayı doğru bulmuş ama kapağın yalıtkan olmasının iletimle ısı kaybını azalttığını kaçırmış.','dikkat'),('I ve II','Vakumun ışımayı da azalttığını sanmış; kapağın iletimi azalttığını atlamış.','bilgi'),('I ve III','Vakumun ışımayı azalttığını sanmış; parlak yüzeyin ışımayı yansıtarak ısı kaybını azalttığını görmemiş.','bilgi')],
 istenen='Doğru olan yargılar.',ip=['Her parçanın üç yoldan (iletim, konveksiyon, ışıma) hangisini engellediğini ayrı ayrı düşün; vakumda tanecik bulunmaz.'],
 bilgi=[B('Isı yalıtımı','vakumda iletim ve konveksiyon olmaz (tanecik yoktur) ama ışıma boşlukta da olur; parlak yüzey ışımayı yansıtır; ısı yalıtkanı madde iletimi azaltır. Örnek: kışlık montun içindeki hava boşlukları vücut ısısının dışarı iletimini azaltır')],
 ad=[A('Vakumlu bölge','Tanecik yok: iletim ve konveksiyon olmaz; ışıma ise boşlukta sürer.','Vakum ışımayı azaltmaz → I yanlış'),A('Parlak kaplama','Işıma enerjisini geri yansıtır.','II doğru'),A('Yalıtkan kapak','Isı iletimi zayıf madde.','III doğru'),A('Sonuç','II ve III doğrudur.','II ve III')],
 puf='Termos: vakum iletim ve konveksiyonu, parlak yüzey ışımayı, yalıtkan kapak iletimi azaltır.')

# ================= 16 · ray boşluğu · zor =================
kartla('16','Boyca genleşmeyle ray aralığı','ΔL = α · L₀ · ΔT; iki ray birbirine doğru genleşir, aralıktan toplam uzama çıkarılır.','Yalnız bir rayın uzamasını almak; aralığı toplam uzamaya eşit saymak.','zor','şekilli',4,'ray','Boyca genleşme ile ray aralığı')
aa,LL_,dT=Fr(12,10**6),20,50; dl=aa*LL_*dT*1000; gap=30; assert dl==12 and gap-2*dl==6
assert gap-dl==18 and 2*dl==24 and gap+dl==42
g=''
g+='\\fill[pattern=north east lines] (-.5,-.6) rectangle (0,1.0); \\draw[thick] (0,-.6) -- (0,1.0); \\fill[pattern=north east lines] (7.0,-.6) rectangle (7.5,1.0); \\draw[thick] (7.0,-.6) -- (7.0,1.0);'
g+='\\draw[thick,fill=gray!25] (0,0) rectangle (3.0,.35); \\draw[thick,fill=gray!25] (4.0,0) rectangle (7.0,.35); \\draw[thick] (3.0,.35) -- (3.0,-.1);\\draw[<->,thin] (3.0,-.2) -- (4.0,-.2); \\node[below] at (3.5,-.2) {30 mm};'
g+='\\draw[<->,thin] (0,.8) -- (3.0,.8); \\node[above] at (1.5,.8) {20 m}; \\draw[<->,thin] (4.0,.8) -- (7.0,.8); \\node[above] at (5.5,.8) {20 m};'
SK=tk(g)
q('0016',tipId='fz-is2-ray',tip='Boyca genleşme ile ray aralığı',z='zor',alt='Genleşme',kaz='Boyca genleşme bağıntısıyla iki cismin aralığının sıcaklık artışıyla nasıl değiştiğini hesaplar.',kalip='şekilli',
 kart='K-FZIS2-16 (ray aralığı) · 2 × 20 m çelik ray, 30 mm boşluk',sekil=SK,
 metin='Bir demiryolu hattında, aynı çelikten yapılmış iki ray, uçları sabit ve genleşmeyen iki beton dayanak arasına şekildeki gibi yerleştirilmiştir. Rayların birbirine bakan uçları arasında şekilde verilen boşluk bırakılmıştır. Çeliğin boyca genleşme katsayısı 12 × 10⁻⁶ °C⁻¹’dir. Sıcaklık, 10 °C’den 60 °C’ye çıkmış; rayların yalnızca boyuna genleştiği ve dayanak tarafındaki uçlarının hareket etmediği kabul edilecektir.\nBuna göre sıcaklık 60 °C iken rayların uçları arasındaki boşluk kaç mm olur?',
 dogru=6,yan=[(12,'Bir rayın uzama miktarını (12 mm) boşluk sanmış.','dikkat'),(18,'Yalnız bir rayın uzamasını boşluktan çıkarmış (30 − 12); iki ray da birbirine doğru uzar.','dikkat'),(24,'İki rayın toplam uzamasını (24 mm) boşluk sanmış; ilk boşluğu çıkarmayı unutmuş.','dikkat'),(42,'Rayların uzamasını boşluğa eklemiş; genleşme boşluğu azaltır.','bilgi')],
 istenen='60 °C’de rayların uçları arasındaki boşluk (mm).',ip=['Rayların birbirine bakan uçları ısınınca nereye doğru hareket eder, aradaki boşluğa ne olur?'],
 bilgi=[B('Boyca genleşme','ΔL = α · L₀ · ΔT (α: genleşme katsayısı, L₀: ilk boy). Örnek: 10 m’lik çubuğun α = 20 × 10⁻⁶ °C⁻¹ ve ΔT = 50 °C için uzaması 10 × 20 × 10⁻⁶ × 50 = 0,01 m’dir')],
 ad=[A('Sıcaklık artışı','Son sıcaklıktan ilk çıkarılır.','ΔT = 60 − 10 = 50 °C'),A('Bir rayın uzaması','Boy 20 m.','ΔL = 12 × 10⁻⁶ × 20 × 50 = 0,012 m = 12 mm'),A('İki rayın toplam uzaması','İki ray da boşluğa doğru uzar.','12 + 12 = 24 mm'),A('Kalan boşluk','İlk boşluktan toplam uzama çıkarılır.','30 − 24 = 6 mm')],
 puf='Uçları sabit iki cisim birbirine doğru genleşir; boşluk, ilk boşluk eksi toplam uzama kadar olur.')

# ================= 17 · yüzeyce ve hacimce genleşme · orta =================
kartla('17','Boyca, yüzeyce ve hacimce genleşme ilişkisi','Küçük genleşmelerde yüzde artışlar boy : yüzey : hacim = 1 : 2 : 3 oranındadır.','Yüzeyin ve hacmin de boy kadar genleştiğini sanmak.','orta','şekilli',4,'yuzey-hacim','Yüzeyce ve hacimce genleşme')
L0,L1=Fr(20),Fr('20.02'); yb=(L1-L0)/L0; ys=2*yb; yh=3*yb
assert yb==Fr(1,1000) and yh/ys==Fr(3,2) and yb/ys==Fr(1,2) and ys/yb==2 and yh/yb==3
g=''
g+='\\draw[thick,fill=gray!25] (0,2.6) rectangle (4.0,2.9); \\node[above] at (2.0,2.95) {çubuk}; \\node[right,align=left] at (4.2,2.75) {ısıtmadan önce 20,00 cm\\\\ ısıtıldıktan sonra 20,02 cm};'
g+='\\draw[thick,fill=gray!25] (0,1.0) rectangle (1.6,1.8); \\node[right] at (1.8,1.4) {ince plaka};'
g+='\\draw[thick,fill=gray!25] (0,-.8) rectangle (.9,.1); \\draw[thick,fill=gray!15] (0,.1) -- (.35,.45) -- (1.25,.45) -- (.9,.1) -- cycle; \\draw[thick,fill=gray!15] (.9,.1) -- (1.25,.45) -- (1.25,-.45) -- (.9,-.8) -- cycle; \\node[right] at (1.5,-.2) {küp};'
SK=tk(g)
q('0017',tipId='fz-is2-yuzey-hacim',tip='Yüzeyce ve hacimce genleşme',z='orta',alt='Genleşme',kaz='Aynı maddenin boyca, yüzeyce ve hacimce genleşme oranlarını ilişkilendirir.',kalip='şekilli',
 kart='K-FZIS2-17 (boy–yüzey–hacim) · çubuk 20,00 → 20,02 cm',sekil=SK,
 metin='Aynı metalden yapılmış bir çubuk, bir ince plaka ve bir küp, aynı sıcaklık artışıyla ısıtılıyor. Çubuğun ısıtmadan önceki ve sonraki boyu şekilde verilmiştir. Genleşmeler çok küçüktür. Plakanın yüzey alanındaki ve küpün hacmindeki yüzde artışlar ayrı ayrı belirlenecek; ardından bu iki artışın oranı incelenecektir.\nBuna göre küpün hacmindeki yüzde artışın plakanın yüzey alanındaki yüzde artışa oranı kaçtır?',
 dogru=Fr(3,2),yan=[(Fr(1,2),'Oranı ters ve eksik kurmuş: boydaki artışı yüzeydeki artışa oranlamış (0,1 ÷ 0,2).','islem'),(1,'Aynı maddenin hacim ve yüzeyinin aynı oranda genleşeceğini düşünmüş.','bilgi'),(2,'Yüzeydeki artışı boydaki artışa oranlamış (0,2 ÷ 0,1); hacmi hiç katmamış.','dikkat'),(3,'Hacimdeki artışı boydaki artışa oranlamış (0,3 ÷ 0,1); yüzey alanını hesaba katmamış.','dikkat')],
 istenen='Hacim artışının yüzey alanı artışına oranı.',ip=['Çubuğun yüzde artışını bulup yüzey alanının ve hacmin boyla nasıl ilişkili olduğunu düşün.'],
 bilgi=[B('Genleşme katsayıları','küçük genleşmelerde boyca yüzde artış α·ΔT ise yüzeyce 2α·ΔT, hacimce 3α·ΔT olur. Örnek: boy %0,05 artarsa yüzey %0,1, hacim %0,15 artar')],
 ad=[A('Boyca artışı bul','Artış, ilk boya oranlanır.','(20,02 − 20,00) ÷ 20 = 0,001 = %0,1'),A('Yüzeyce artış','Yüzey alanı boyun iki katı oranında artar.','ΔS/S = 2 × 0,1 = %0,2'),A('Hacimce artış','Hacim boyun üç katı oranında artar.','ΔV/V = 3 × 0,1 = %0,3'),A('Oranla','Hacim artışı yüzey artışına bölünür.','0,3 ÷ 0,2 = 1,5')],
 puf='Küçük genleşmelerde boy : yüzey : hacim yüzde artışları 1 : 2 : 3’tür.')

# ================= 18 · bimetal soğutma · orta =================
kartla('18','Bimetalin soğutulunca bükülmesi','Genleşme katsayısı büyük metal ısıtılınca daha çok uzar, soğutulunca daha çok kısalır; bimetal küçük katsayılı metale doğru ısıtmada, büyük katsayılı metale doğru soğutmada bükülür.','Isıtma ve soğutmada bükülme yönünü aynı sanmak; hangi yüzün daha çok kısaldığını karıştırmak.','orta','şekilli',4,'bimetal-sogut','Bimetalin soğutulunca bükülmesi')
aX,aY=24,12
assert aX>aY            # soğutulunca X (üst) daha çok kısalır -> üst iç yüz -> yukarı bükülür
g='\\fill[pattern=north east lines] (-.5,-.4) rectangle (0,.5); \\draw[thick] (0,-.4) -- (0,.5);'
g+='\\draw[thick,fill=gray!30] (0,.15) rectangle (3.6,.5); \\draw[thick,fill=white] (0,-.2) rectangle (3.6,.15); \\node at (1.8,.325) {\\footnotesize X}; \\node at (1.8,-.025) {\\footnotesize Y};'
g+='\\node[right] at (3.8,.35) {$\\alpha_X=24\\cdot10^{-6}\\,^\\circ$C$^{-1}$}; \\node[right] at (3.8,-.05) {$\\alpha_Y=12\\cdot10^{-6}\\,^\\circ$C$^{-1}$};\\node[below] at (1.8,-.35) {$20\\,^\\circ$C};'
SK=tk(g)
q('0018',tipId='fz-is2-bimetal-sogut',tip='Bimetalin soğutulunca bükülmesi',z='orta',alt='Metal Çiftleri (Bimetal)',kaz='Bimetal çubuğun soğutulduğunda hangi yöne bükülüeceğini genleşme katsayılarından belirler.',kalip='şekilli',
 kart='K-FZIS2-18 (bimetal, soğutma) · X üstte α = 24, Y altta α = 12',sekil=SK,
 metin='Boyları ve kalınlıkları eşit X ve Y metal şeritleri üst üste kaynatılarak bir bimetal çubuk oluşturulmuş; çubuğun sol ucu şekildeki gibi duvara sabitlenmiştir. Çubuk 20 °C’de düzdür. İki metalin boyca genleşme katsayıları şekilde verilmiştir. Çubuk daha sonra yavaş yavaş −20 °C’ye kadar soğutuluyor ve çubuğun serbest ucunun hareketi gözleniyor. Çubuğun ağırlığı ve duvar ile sürtünme ihmal edilecektir.\nBuna göre soğutma sırasında çubuğun serbest ucu için ne söylenebilir?',
 dogru='Yukarı doğru bükülür',sira=['Yukarı doğru bükülür','Aşağı doğru bükülür','Bükülmez, yalnızca kısalır','Önce aşağı sonra yukarı bükülür','Bükülmez, yalnızca uzar'],yan=[('Aşağı doğru bükülür','Isıtmada olduğu gibi aşağı bükülür sanmış; soğutmada katsayısı büyük olan X daha çok kısalır.','bilgi'),('Bükülmez, yalnızca kısalır','İki metalin de kısalacağını görmüş ama farklı oranda kısalmanın bükülme yaptığını hesaba katmamış.','bilgi'),('Önce aşağı sonra yukarı bükülür','Sıcaklık düşerken yön değiştireceğini düşünmüş; kısalma farkı tek yönlü bükülme yapar.','dikkat'),('Bükülmez, yalnızca uzar','Soğutmada metalin uzadığını sanmış.','bilgi')],
 istenen='Serbest ucun hareketi.',ip=['Soğutmada hangi metalin daha çok kısaldığını, daha çok kısalan yüzeyin bükülmenin iç tarafında mı dış tarafında mı kaldığını düşün.'],
 bilgi=[B('Bimetal','genleşme katsayıları farklı iki metalden oluşan çubuk ısıtılınca katsayısı küçük olan metale doğru, soğutulunca katsayısı büyük olan metale doğru bükülür. Örnek: alt yüzü çinko (büyük α), üst yüzü çelik olan şerit ısınınca yukarı, soğuyunca aşağı bükülür')],
 ad=[A('Katsayıları karşılaştır','α_X > α_Y.','24 > 12'),A('Soğutmada kısalma','Katsayısı büyük olan daha çok kısalır.','X (üst) Y’den daha çok kısalır'),A('Bükülme yönü','Daha çok kısalan yüz bükülmenin iç tarafında kalır.','Üst yüz iç taraf → uç yukarı kalkar'),A('Sonuç','Çubuk yukarı doğru bükülür.','Yukarı doğru')],
 puf='Bimetal ısınınca küçük, soğuyunca büyük katsayılı metalin tarafına doğru bükülür.')

# ================= 19 · bimetalli alarm · zor · öncüllü =================
kartla('19','Bimetalli yangın alarmı','Isınan bimetal küçük katsayılı metale doğru bükülür; bu hareket devreyi kapatıp açabilir.','Üst–alt metal yerini değiştirmenin bükülme yönünü etkilemediğini sanmak.','orta','öncüllü',5,'bimetal-alarm','Bimetalli alarm devresi')
aCu,aFe=17,12
# Üst bakır (büyük α) ısınınca daha çok uzar -> çubuk aşağı bükülür -> alt kontağa dokunur -> lamba yanar.  I doğru, III doğru.
# II (yanlış): metaller yer değiştirirse (üst demir) çubuk ısınınca YUKARI bükülür, kontak kurulmaz.
g='\\fill[pattern=north east lines] (-.5,-.4) rectangle (0,.5); \\draw[thick] (0,-.4) -- (0,.5);'
g+='\\draw[thick,fill=gray!30] (0,.05) rectangle (3.2,.4); \\draw[thick,fill=white] (0,-.3) rectangle (3.2,.05); \\node at (1.6,.225) {\\footnotesize bakır}; \\node at (1.6,-.125) {\\footnotesize demir};'
g+='\\draw[thick,fill=gray!30] (2.6,-.85) rectangle (3.3,-.75);'
g+='\\draw[thick] (0,-.12) -- (-1.1,-.12) to[battery1] (-1.1,-2.4) -- (.8,-2.4) to[lamp] (2.6,-2.4) -- (3.0,-2.4) -- (3.0,-.85);'
g+='\\node[right,align=left] at (3.7,.25) {bakır: $\\alpha=17\\cdot10^{-6}\\,^\\circ$C$^{-1}$}; \\node[right,align=left] at (3.7,-.2) {demir: $\\alpha=12\\cdot10^{-6}\\,^\\circ$C$^{-1}$};'
SK=tk(g)
q('0019',tipId='fz-is2-bimetal-alarm',tip='Bimetalli alarm devresi',z='orta',alt='Metal Çiftleri (Bimetal)',kaz='Bimetalli devre anahtarının ısınınca nasıl davrandığını genleşme katsayılarından yorumlar.',kalip='öncüllü',
 kart='K-FZIS2-19 (bimetalli alarm) · üst bakır, alt demir',sekil=SK,
 metin='Bir yangın alarm düzeneğinde, üst yüzü bakır, alt yüzü demir olan bimetal bir çubuk, bir ucundan sabitlenmiştir. Çubuk ve altındaki metal temas levhası lamba ile bataryaya şekildeki gibi bağlanmıştır; normal ortam sıcaklığında çubuk düzdür ve levhaya dokunmaz. Ortam sıcaklığı yükselince çubuk bükülüp levhaya değerse devre tamamlanacaktır. Metallerin genleşme katsayıları şekildeki gibidir.\nI. Ortam yeterince ısınırsa çubuğun serbest ucu aşağı hareket eder ve lamba yanar.\nII. Üst ve alt metalin yerleri değiştirilirse (üstte demir, altta bakır) ısınma sırasında yine lamba yanar.\nIII. Isınma sırasında bakır katman, demir katmandan daha çok uzar.\nBuna göre bu yargılardan hangileri doğrudur?',
 dogru='I ve III',sira=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III'],yan=[('Yalnız I','III’ü yanlış saymış; ısınan bimetalde α’sı büyük bakır katmanın daha çok uzadığını görememiş.','bilgi'),('Yalnız II','Bükülme yönünün hangi metalin üstte olduğuna bağlı olmadığını düşünüp II’yi doğru, I ve III’ü yanlış saymış.','bilgi'),('I ve II','II’yi doğru saymış; metaller yer değiştirince çubuk ısınırken yukarı bükülür, levhaya değmez.','dikkat'),('Yalnız III','Bakırın daha çok uzadığını bilmiş ama bunun çubuğu aşağı bükeceğini düşünememiş; I’i yanlış saymış.','dikkat')],
 istenen='Doğru olan yargılar.',ip=['Isınınca hangi metalin daha çok uzadığına bak; daha çok uzayan metalin çubuğun hangi tarafında kaldığına göre bükülme yönünü belirle.'],
 bilgi=[B('Bimetal bükülmesi','ısıtılan bimetal, genleşme katsayısı küçük olan metale doğru bükülür çünkü büyük katsayılı metal daha çok uzar ve dış tarafta kalır. Örnek: α büyük metal altta olursa çubuk ısınınca yukarı bükülür')],
 ad=[A('Katsayıları karşılaştır','Bakır α = 17, demir α = 12.','Bakır daha çok uzar → III doğru'),A('Bükülme yönü','Üst katman daha çok uzar, çubuk aşağı bükülür.','Serbest uç aşağı iner'),A('Devre','Uç temas levhasına değer.','Devre tamamlanır, lamba yanar → I doğru'),A('II’yi incele','Üstte demir olursa üst katman daha az uzar; çubuk yukarı bükülür.','Levhaya değmez → II yanlış'),A('Sonuç','I ve III doğrudur.','I ve III')],
 puf='Isınan bimetal, genleşme katsayısı küçük metale doğru bükülür; metallerin yeri değişince yön de değişir.')

# ================= 20 · suyun genleşme ayrıcalığı · orta · öncüllü =================
kartla('20','Suyun hacim–sıcaklık grafiği','Su 0–4 °C arasında ısıtılınca büzülür, 4 °C’de hacmi en küçük, özkütlesi en büyüktür; 4 °C’den sonra genleşir.','Su da diğer maddeler gibi her sıcaklıkta ısınınca genleşir sanmak.','orta','öncüllü',4,'su-grafik','Suyun genleşme ayrıcalığı')
# I: 0–4'te ısınınca hacim artar (yanlış). II: 4 °C'de özkütle en büyük (hacim en küçük) doğru. III: 4 °C üzerinde ısınınca hacim artar (doğru).
g='''\\begin{axis}[width=7.2cm,height=5.2cm,xmin=0,xmax=10.5,ymin=0.95,ymax=1.55,xtick={0,2,4,6,8,10},ytick=\\empty,tick label style={font=\\scriptsize},axis lines=left,xlabel={Sıcaklık ($^\\circ$C)},ylabel={Hacim},xlabel style={font=\\small},ylabel style={font=\\small}]
\\addplot[thick,vurgu,domain=0:10,samples=50] {1+0.008*(x-4)^2+0.0009*(x-4)^3};
\\end{axis}'''
SK=tk(g)
q('0020',tipId='fz-is2-su-grafik',tip='Suyun genleşme ayrıcalığı',z='orta',alt='Suyun Genleşmesi',kaz='Sabit kütleli suyun hacim–sıcaklık grafiğini yorumlar.',kalip='öncüllü',
 kart='K-FZIS2-20 (suyun hacim–sıcaklık grafiği) · 0–10 °C',sekil=SK,
 metin='Bir öğrenci, sabit kütleli saf suyun hacminin sıcaklıkla nasıl değiştiğini incelemek için çok hassas bir ölçüm düzeneği kuruyor. Su, buzun erime sıcaklığından başlayarak çok yavaş ısıtılıyor ve hacim–sıcaklık verileri şekildeki grafiğe işleniyor. Kap, genleşmeyi etkilemeyecek kadar küçük genleşen bir malzemeden yapılmıştır; su bu aralıkta hâl değiştirmemektedir.\nI. 0 °C ile 4 °C arasında suyun sıcaklığı arttıkça hacmi de artar.\nII. Suyun özkütlesi 4 °C’de en büyüktür.\nIII. 4 °C’den sonra suyun sıcaklığı arttıkça hacmi artar.\nBuna göre bu yargılardan hangileri doğrudur?',
 dogru='II ve III',sira=['Yalnız I','Yalnız II','I ve II','I ve III','II ve III'],yan=[('Yalnız I','I’i doğru saymış; 0–4 °C arasında hacmin azaldığını görmemiş, II ve III’ü de grafiğe bakmadan yanlış bulmuş.','bilgi'),('Yalnız II','III’ü yanlış saymış; 4 °C’den sonra suyun diğer maddeler gibi genleştiğini bilmemiş.','bilgi'),('I ve III','I’i doğru bulmuş; 0–4 °C arasında su ısındıkça büzüldüğünü bilmemiş, II’yi atlamış.','bilgi'),('I ve II','II’yi doğru bulmuş; ancak I’i de doğru saymış ve 4 °C’den sonra hacmin arttığını (III) yanlış bulmuş.','bilgi')],
 istenen='Doğru olan yargılar.',ip=['Grafikte hacmin azaldığı ve arttığı bölgelere ayrı ayrı bak.'],
 bilgi=[B('Suyun ayrıcalığı','su 0–4 °C arasında ısıtılınca büzülür (hacmi azalır), 4 °C’de hacmi en küçük ve özkütlesi en büyük olur, 4 °C’den sonra diğer sıvılar gibi genleşir. Örnek: bu yüzden 4 °C’deki su, 2 °C’deki sudan daha yoğundur')],
 ad=[A('0–4 °C arasını oku','Grafik bu aralıkta aşağı iner.','Hacim azalır → I yanlış'),A('Hacmin en küçük olduğu nokta','Grafikteki en alçak nokta 4 °C’dedir.','Hacim en küçük → özkütle en büyük → II doğru'),A('4 °C’den sonrası','Grafik yukarı çıkar.','Hacim artar → III doğru'),A('Sonuç','II ve III doğrudur.','II ve III')],
 puf='Su 4 °C’de en küçük hacme ve en büyük özkütleye sahiptir; 0–4 °C arasında ısınınca büzülür.')

# ================= 21 · donunca hacim · kolay =================
kartla('21','Donan suyun hacmi','Su donunca kütle değişmez, özkütle azalır, hacim artar (V = m/d).','Hacmin azaldığını sanmak; özkütle oranını ters kullanmak.','kolay','şekilli',3,'buz-hacim','Suyun donarken hacminin artması')
m_su=360; d_buz=Fr(9,10); Vb=Fr(m_su)/d_buz; assert Vb==400 and m_su*d_buz==324 and m_su*Fr(11,10)==Fr(1980,5) and 2*m_su==720
g='\\draw[thick] (0,3.6) -- (0,0) -- (1.2,0) -- (1.2,3.6); \\fill[vurgu!15] (0,0) rectangle (1.2,2.16);\\draw[thick] (0,2.16) -- (1.2,2.16);'
for v in range(0,700,100):
    y=v/600*3.6; g+=f'\\draw (1.2,{y:.3f}) -- (1.4,{y:.3f}); \\node[right] at (1.4,{y:.3f}) {{\\scriptsize {v}}};'
g+='\\node[above] at (1.4,3.7) {\\scriptsize cm$^3$}; \\node[left,align=right] at (-.2,1.1) {su\\\\ 360 g\\\\ $0\\,^\\circ$C};'
SK=tk(g)
q('0021',tipId='fz-is2-buz-hacim',tip='Suyun donarken hacminin artması',z='kolay',alt='Suyun Genleşmesi',kaz='Donan suyun kütlesinin değişmediğini bilerek özkütle farkından yeni hacmi bulur.',kalip='şekilli',
 kart='K-FZIS2-21 (su → buz hacmi) · 360 g, d_buz = 0,9',sekil=SK,
 metin='Bir öğrenci, derecelendirilmiş bir silindire kütlesi şekilde yazılı olan 0 °C’deki suyu koyuyor ve silindiri tamamen donana kadar dondurucuda bekletiyor. Silindir, genleşmeyi ihmal edilecek kadar sağlam ve geniş ağızlıdır; su donarken taşma ya da silindirde çatlama olmuyor. Suyun özkütlesi 1 g/cm³, buzun özkütlesi 0,9 g/cm³’tür.\nBuna göre su tamamen buz olduğunda buzun üst yüzeyi silindirin kaç cm³’lük çizgisine gelir?',
 dogru=400,yan=[(324,'Hacmi kütle ile özkütlenin çarpımı (360 × 0,9) olarak bulmuş.','islem'),(360,'Suyun donarken hacminin değişmediğini sanmış.','bilgi'),(396,'Hacmin %10 artacağını varsaymış (360 × 1,1); oysa V = m ÷ d bağıntısıyla bulunur.','islem'),(720,'Suyun donarken hacminin 2 katına çıktığını düşünmüş.','bilgi')],
 istenen='Buzun yüzeyinin geldiği hacim çizgisi (cm³).',ip=['Donarken değişmeyen büyüklüğü belirle; yeni hacmi o büyüklükle özkütleden bul.'],
 bilgi=[B('Özkütle ve hacim','d = m ÷ V; kütle sabit kaldığında özkütle küçülürse hacim büyür. Su donunca özkütlesi azalır, hacmi artar. Örnek: 180 g su, özkütlesi 0,9 g/cm³ olan buza dönerse hacmi 200 cm³ olur')],
 ad=[A('Değişmeyen niceliği bul','Donarken kütle değişmez.','m = 360 g'),A('Buzun hacmi','V = m ÷ d.','V = 360 ÷ 0,9'),A('Hesapla','Sonuç buzun hacmi.','V = 400 cm³'),A('Yorumla','Hacim 360 cm³’ten 400 cm³’e çıktı.','Çizgi: 400 cm³')],
 puf='Donarken kütle sabit, özkütle azalır, hacim artar; V = m ÷ d.')

# ================= 22 · küresel ısınma · kolay · öncüllü =================
kartla('22','Küresel ısınma (nitel)','Sera gazları yer yüzeyinden yayılan ışımayı tutarak ortalama sıcaklığı artırır; ısınma buzulları eritir ve okyanus suyunu genleştirerek deniz seviyesini yükseltir.','Ozon incelmesini küresel ısınmanın nedeni saymak; sera gazlarının ısıyı tümüyle uzaya kaçırdığını sanmak.','kolay','öncüllü',3,'kuresel','Küresel ısınma')
rows=[['1990','354','14,40','0'],['2000','369','14,54','30'],['2010','389','14,72','60'],['2020','413','14,90','95']]
assert all(rows[i][1]<rows[i+1][1] for i in range(3))
SK=tablo_svg(['Yıl','CO₂ (ppm)','Ort. sıcaklık (°C)','Deniz seviyesi artışı (mm)'],rows)
q('0022',tipId='fz-is2-kuresel',tip='Küresel ısınma',z='kolay',alt='Küresel Isınma',kaz='Küresel ısınmanın nedenlerini ve sonuçlarını verilerden yorumlar.',kalip='öncüllü',
 kart='K-FZIS2-22 (küresel ısınma tablosu) · 1990–2020',sekil=SK,
 metin='Bir iklim araştırma grubu, farklı yıllarda atmosferdeki karbondioksit derişimini, Dünya’nın ortalama yüzey sıcaklığını ve deniz seviyesindeki toplam artışı (1990’a göre) yaklaşık değerlerle şekildeki gibi bir araya getirmiştir. Grubun sunumunda, ölçümlerin ışığında küresel ısınma kavramı tartışılacaktır.\nI. Tablodaki yıllarda karbondioksit derişimi ile ortalama sıcaklık birlikte artmıştır.\nII. Deniz seviyesindeki artışın nedenlerinden biri, okyanus suyunun ısınınca genleşmesidir.\nIII. Karbondioksit artışı, Güneş’ten gelen ışınların atmosfere girmesini tamamen engeller.\nBuna göre bu yargılardan hangileri doğrudur?',
 dogru='I ve II',sira=S_STD,yan=[('Yalnız I','II’yi yanlış saymış; ısınan suyun genleşmesinin de deniz seviyesini yükselttiğini bilmemiş.','bilgi'),('Yalnız II','Tablodaki iki büyüklüğün birlikte arttığını görmemiş, I’i yanlış saymış.','dikkat'),('I ve III','III’ü doğru saymış; sera gazları Güneş ışınlarının girişini engellemez, yer yüzeyinden yayılan ışımayı tutar.','bilgi'),('I, II ve III','III’ü de doğru bulmuş; sera gazlarının Güneş ışınlarını engellediğini sanmış.','bilgi')],
 istenen='Doğru olan yargılar.',ip=['Tablodaki sütunlardaki değişimlere bak; sera gazlarının yer yüzeyinden yayılan ışımaya ne yaptığını düşün.'],
 bilgi=[B('Küresel ısınma','sera gazları (CO₂, CH₄ gibi) yer yüzeyinin yaydığı ışımayı tutarak atmosferin ısınmasına yol açar. Isınma buzulları eritir ve suyu genleştirerek deniz seviyesini yükseltir. Örnek: kara buzulları erirse okyanusa yeni su katılır')],
 ad=[A('I’i tablodan oku','1990’dan 2020’ye iki sütun da artıyor.','354 → 413 ppm · 14,40 → 14,90 °C → I doğru'),A('II’yi değerlendir','Okyanus suyu ısınınca hacmi artar; buzullar da erir.','II doğru'),A('III’ü değerlendir','Güneş ışınları atmosfere girer; sera gazları yer yüzeyinden yayılan ışımayı tutar.','III yanlış'),A('Sonuç','I ve II doğrudur.','I ve II')],
 puf='Sera gazları yer yüzeyinden yayılan ışımayı tutar; ısınma deniz seviyesini hem buzul erimesi hem suyun genleşmesiyle yükseltir.')

bitir(P,'isiiki',UK)
