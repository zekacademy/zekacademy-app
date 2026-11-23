"""AYT Fizik · Bir Boyutta Sabit İvmeli Hareket · 20 soru (kardeş yok, ipucu 1).
Şekil verileri Python'da hesaplanır, TikZ/pgfplots gövdeleri aynı değerlerden üretilir; her cevap/çeldirici assert edilir."""
import sys,os,json
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-fiz')); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
import _hafif as H
from _hafif import *
from cizim import tikz_svg
from _hafif_mat import tablo_svg
from fractions import Fraction as Fr
KONUAD='Bir Boyutta Sabit İvmeli Hareket'; KK='afiz|Bir Boyutta Sabit İvmeli Hareket'
P=Parti('ivmeli',KONUAD,KK,ders='AYT Fizik',idon='aytfiz'); H.KONU=KONUAD
g=10
def kartla(n,alt,fikir,tuzak,z,kalip,adim,tipId,tip):
    kart(f'K-AFIVM-{n:02d}',alt,fikir,tuzak,z,kalip,adim,tipId,tip,'ÖSYM AYT 2018–2025 Fizik (yalnız mantık) · 345 AYT Fizik SB · MEB 11. sınıf')
def q(no,n,z,alt,kalip,tipId,tip,kaz,ad,**k):
    assert len(k['ip'])==1 and 3<=len(ad)<=7
    mk(P,f'{no:04d}',ad=ad,adim=len(ad),z=z,alt=alt,kalip=kalip,tipId=tipId,tip=tip,kaz=kaz,kart=f'K-AFIVM-{n:02d} ({alt})',**k)
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'; TAIL='\n\\end{tikzpicture}'
def AX(body,xmax,ymin,ymax,xt,yt,yl,xl='$t$ (s)',w=6.4,h=4.6,extra=''):
    xs=','.join(map(str,xt)); ys=','.join(map(str,yt))
    opt=(r'width=%scm,height=%scm,xmin=0,xmax=%s,ymin=%s,ymax=%s,xtick={%s},ytick={%s},grid=both,major grid style={gray!55,thin},'
         r'tick label style={font=\footnotesize},axis lines=left,xlabel={%s},ylabel={%s},xlabel style={font=\small},ylabel style={font=\small}')%(w,h,xmax,ymin,ymax,xs,ys,xl,yl)
    if extra: opt+=','+extra
    if ymin<0: body+='\\addplot[black,thin] coordinates {(0,0) (%s,0)};\n'%xmax
    return tikz_svg(HEAD+'\\begin{axis}['+opt+']\n'+body+'\n\\end{axis}'+TAIL)
def pl(pts,st='thick,vurgu'): return f'\\addplot[{st}] coordinates {{'+' '.join(f'({a},{b})' for a,b in pts)+'};\n'
def gd(x,y,x0=0,y0=0): return f'\\draw[dashed,gray] (axis cs:{x0},{y}) -- (axis cs:{x},{y}) -- (axis cs:{x},{y0});\n'
def nd(x,y,t,pos='above'): return f'\\node[{pos},font=\\small\\bfseries] at (axis cs:{x},{y}) {{{t}}};\n'
ROM=['I','II','III']
ADLAR=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
KUME={'Yalnız I':{0},'Yalnız II':{1},'Yalnız III':{2},'I ve II':{0,1},'I ve III':{0,2},'II ve III':{1,2},'I, II ve III':{0,1,2}}
def onc(no,n,z,alt,tipId,tip,kaz,kok,items,sec,ad_ek,sekil=None,kalip='öncüllü',**k):
    """items: (yargı metni, doğru mu, nedeni). Doğru küme, anahtar, çeldirici açıklamaları ve adımlar BU listeden üretilir."""
    T={i for i,it in enumerate(items) if it[1]}
    dogru=[a for a in ADLAR if KUME[a]==T][0]; assert dogru in sec and len(sec)==5 and len(set(sec))==5
    sira=[a for a in ADLAR if a in sec]
    yan=[]
    for a in sira:
        if a==dogru: continue
        S=KUME[a]; c=[]
        for i in sorted(S-T): c.append(f'{ROM[i]}. yargıyı doğru sanmış; oysa {items[i][2]}')
        for i in sorted(T-S): c.append(f'{ROM[i]}. yargıyı yanlış sanmış; oysa {items[i][2]}')
        yan.append((a,' '.join(c),'bilgi'))
    metin=kok+'\n'+'\n'.join(f'{ROM[i]}. {it[0]}' for i,it in enumerate(items))+'\nyargılarından hangileri doğrudur?'
    ad=[A(f'{ROM[i]}. yargıyı incele',it[2][0].upper()+it[2][1:],f'{ROM[i]}: {"doğru" if it[1] else "yanlış"}') for i,it in enumerate(items)]+[A('Sonucu belirle','Doğru yargıların kümesi yanıttır.',dogru)]
    ad=ad_ek+ad if ad_ek else ad
    q(no,n,z,alt,kalip,tipId,tip,kaz,ad,metin=metin,dogru=dogru,yan=yan,sira=sira,sekil=sekil,**k)
    return dogru

# tipId'ler (8): vt-alan, at-vt, xt-egim, formul, serbest, dusey, yorum, yetisme
# =================== 01 · v–t alanı · kolay ===================
KT=dict(vt=('ivm-vt-alan','v–t grafiğinden yol ve yer değiştirme'),at=('ivm-at-vt','a–t grafiğinden hız ve yer değiştirme'),xt=('ivm-xt-egim','x–t grafiğinde eğim ve hız'),
        fo=('ivm-formul','Hareket denklemlerinin uygulanması'),se=('ivm-serbest','Serbest düşme ve aşağı atış'),du=('ivm-dusey','Düşey atış ve karşılaşma'),
        yo=('ivm-yorum','Grafik ve kavram yorumu (öncüllü)'),ye=('ivm-yetisme','İki cismin yetişmesi'))
pts1=[(0,0),(4,20),(10,20)]
yol1=Fr(4*20,2)+6*20; assert yol1==160 and 10*20==200 and Fr(10*20,2)==100 and 6*20==120 and Fr(4*20,2)==40
kartla(1,'v–t alanı: yol','v–t grafiğinde eğri altındaki alan yer değiştirmedir; yamuk alanı üçgen + dikdörtgen parçalanır.','Tüm süreyi en büyük hızla çarpmak; yalnız sabit hızlı bölümü almak.','kolay','grafik',3,*KT['vt'])
SK=AX(pl(pts1)+gd(4,20),10,0,25,range(0,11,2),[0,10,20],'$v$ (m/s)')
q(1,1,'kolay','v–t alanı','grafik',*KT['vt'],'v–t grafiğinden aldığı yolu bulur.',
 metin='Doğrusal ve yatay bir yolda durgun halden harekete geçen bir otomobilin hız–zaman grafiği şekilde verilmiştir.\nBuna göre, otomobilin 0–10 s aralığında aldığı yol kaç metredir?',
 dogru=160,yan=[(200,'Süre boyunca en büyük hız (20 m/s) sabit kalmış gibi 20 × 10 hesaplamış.','bilgi'),(100,'Grafiğin tamamını üçgen sanıp ½ × 10 × 20 işlemini yapmış.','bilgi'),(120,'Yalnız sabit hızlı bölümün (6 s × 20 m/s) alanını almış.','dikkat'),(40,'Yalnız hızlanma bölümünün (üçgen) alanını bulmuş.','dikkat')],
 istenen='0–10 s aralığında alınan yol (m).',ip=['Yol, v–t grafiğiyle zaman ekseni arasında kalan alandır; bu alanı basit şekillere ayır.'],
 bilgi=[B('v–t grafiğinde alan','eğri ile zaman ekseni arasındaki alan yer değiştirmeyi verir; ileri yönde hareketle bu alan yola eşittir. Örnek: 3 s boyunca 6 m/s sabit hızla giden cisim 18 m gider (dikdörtgen alanı)'),B('Üçgen ve dikdörtgen','üçgenin alanı ½ × taban × yükseklik, dikdörtgenin alanı taban × yüksekliktir')],
 ad=[A('Grafiği bölümle','0–4 s düzgün hızlanma, 4–10 s sabit hız bölümüdür.','0–4 s: üçgen · 4–10 s: dikdörtgen'),A('Hızlanma bölümü','Üçgenin alanı ½ × taban × yükseklik.','x₁ = ½ × 4 × 20 = 40 m'),A('Sabit hız bölümü','Dikdörtgenin alanı taban × yükseklik.','x₂ = 6 × 20 = 120 m'),A('Toplamı bul','İki alan toplanır.','x = 40 + 120 = 160 m')],
 puf='v–t grafiğinde yolu bulmak için eğriyi tanıdık şekillere böl, alanları topla.',sekil=SK)

# =================== 02 · Duran araç: v² = v₀² + 2ax · kolay ===================
v0=72*Fr(1000,3600); assert v0==20; a2=v0**2/(2*100); assert a2==2
assert Fr(100,400)==Fr(1,4) and 2*a2==4 and Fr(100,20)==5
kartla(2,'v² = v₀² + 2ax','Zaman verilmeden hız–yol ilişkisi: v² = v₀² + 2ax; birimler m ve s cinsine çevrilir.','km/h değerini m/s’ye çevirmemek; 2 katsayısını unutmak.','kolay','şekilli',3,*KT['fo'])
SK=tikz_svg(HEAD+r'''\fill[gray!35] (-.3,-.2) rectangle (8.3,0); \draw (-.3,0) -- (8.3,0);
\draw[thick,fill=gray!25] (0,.18) rectangle (1.6,.78); \draw[thick,fill=white] (.25,.78) -- (.5,1.1) -- (1.1,1.1) -- (1.35,.78);
\draw[fill=black] (.35,.18) circle (.17); \draw[fill=black] (1.25,.18) circle (.17);
\draw[vurgu,very thick,-{Stealth[length=2mm]}] (.8,1.5) -- (2.2,1.5); \node[above] at (1.5,1.5) {$v_0=72$ km/h};
\draw[very thick] (7.4,0) -- (7.4,1.3); \fill[red!70!black] (7.2,1.3) rectangle (7.6,1.5); \node[above] at (7.4,1.5) {bariyer};
\draw[<->] (1.6,-.55) -- (7.4,-.55); \node[below] at (4.5,-.55) {$100$ m};
\draw[dotted] (1.6,0) -- (1.6,-.55); \draw[dotted] (7.4,0) -- (7.4,-.55);'''+TAIL)
q(2,2,'kolay','v² = v₀² + 2ax','şekilli',*KT['fo'],'Yavaşlama ivmesini hız ve yoldan bulur.',
 metin='Yatay ve doğrusal bir yolda 72 km/h hızla giden bir otomobilin sürücüsü, yolda duran bariyeri görünce fren yapıyor. Otomobil sabit ivmeyle yavaşlayarak bariyerin hemen önünde duruyor; frenlemenin başladığı an bariyere olan uzaklık şekilde gösterilmiştir.\nBuna göre, otomobilin ivmesinin büyüklüğü kaç m/s² dir?',
 dogru=2,yan=[(Fr(1,4),'Yolu hızın karesine bölmüş (100 ÷ 20²); bağıntıyı yanlış kurmuş.','bilgi'),(4,'v² = 2ax bağıntısında 2 katsayısını unutup a = 20² ÷ 100 hesaplamış.','islem'),(5,'Yolu hıza bölüp (100 ÷ 20) süre benzeri bir değer bulmuş; bu ivme değildir.','bilgi'),(20,'72 km/h değerini m/s’ye çevirmiş ama hızın kendisini ivme saymış.','dikkat')],
 istenen='Otomobilin ivmesinin büyüklüğü (m/s²).',ip=['Süre verilmediğinden hız, yol ve ivmeyi birbirine bağlayan bağıntıyı seç; hızı önce m/s cinsine çevir.'],
 bilgi=[B('Birim çevirme','km/h değeri 3,6’ya bölünür: 36 km/h = 10 m/s'),B('Zamansız bağıntı','sabit ivmeli harekette v² = v₀² + 2ax; yavaşlayan harekette a negatif alınır. Örnek: v₀ = 10 m/s, a = −5 m/s² ile durana kadar 10 m yol alınır')],
 ad=[A('Hızı çevir','72 km/h değeri 3,6’ya bölünür.','v₀ = 72 ÷ 3,6 = 20 m/s'),A('Bağıntıyı yaz','Son hız sıfırdır, ivme yavaşlama olduğundan negatiftir.','0 = 20² + 2 × a × 100'),A('İvmeyi çöz','Denklemden a çekilir; büyüklük istenir.','a = −400 ÷ 200 = −2 → 2 m/s²')],
 puf='Zaman verilmediğinde v² = v₀² + 2ax bağıntısı en kısa yoldur; önce birimleri sadeleştir.',sekil=SK)

# =================== 03 · Serbest düşme kavramları (öncüllü) · kolay ===================
kartla(3,'Serbest düşme özellikleri','Serbest düşmede ivme g sabittir ve kütleden bağımsızdır; ilk hızsız harekette ardışık eşit sürelerdeki yollar 1:3:5… oranındadır.','Ağır cismin daha hızlı düştüğünü sanmak.','kolay','öncüllü',2,*KT['yo'])
onc(3,3,'kolay','Serbest düşme özellikleri',*KT['yo'],'Serbest düşme hareketinin özelliklerini yorumlar.',
 'Hava direncinin ihmal edildiği bir ortamda, aynı yükseklikten ilk hızsız bırakılan 2 kg ve 5 kg kütleli iki küre serbest düşme hareketi yapmaktadır.\nBu hareket ile ilgili,',
 [('Kürelerin ivmeleri kütlelerine bağlı değildir.',True,'serbest düşmede ivme her cisim için g’dir, kütleye bağlı değildir.'),
  ('Her küre, ardışık eşit zaman aralıklarında 1 : 3 : 5 … oranında yol alır.',True,'ilk hızsız sabit ivmeli harekette ardışık eşit sürelerdeki yollar 1 : 3 : 5 … oranındadır.'),
  ('5 kg kütleli küre yere daha önce çarpar.',False,'iki küre aynı ivmeyle düştüğünden yere aynı anda çarparlar.')],
 ['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III'],None,
 ip=['Hava direnci yokken yer çekimi ivmesinin cisme ve kütleye nasıl bağlandığını düşün.'],
 istenen='Doğru yargıların belirlenmesi.',bilgi=[B('Serbest düşme','ilk hızsız bırakılan ve yalnız yer çekiminin etkisindeki harekettir; ivme g = 10 m/s²’dir, kütleye bağlı değildir'),B('Ardışık saniyeler','ilk hızsız harekette 1., 2., 3. saniyelerde alınan yollar 5 m, 15 m, 25 m, yani 1 : 3 : 5 oranındadır')],
 puf='Hava direnci yoksa bütün cisimler kütlelerinden bağımsız aynı ivmeyle düşer.')

# =================== 04 · x–t parabolü · orta ===================
a4,v04=5,5; x4=lambda t:v04*t+Fr(a4*t*t,2)
assert x4(2)==20 and x4(4)==60 and v04+a4*6==35 and Fr(x4(2),2)==10 and Fr(x4(4),4)==15 and Fr(x4(4)-x4(2),2)==20 and a4*6==30
kartla(4,'x–t parabolünden anlık hız','Parabolik x–t grafiğinde iki konum verisi v₀ ve a’yı belirler; hız v = v₀ + at ile bulunur.','Ortalama hızı anlık hız saymak; v₀’ı sıfır almak.','orta','grafik',4,*KT['xt'])
SK=AX('\\addplot[thick,vurgu,domain=0:4,samples=40]{5*x+2.5*x^2};\n\\addplot[only marks,mark=*,mark size=1.6pt,vurgu] coordinates {(0,0) (2,20) (4,60)};\n'+gd(2,20)+gd(4,60),5,0,70,range(0,6),range(0,71,10),'$x$ (m)')
q(4,4,'orta','x–t parabolü','grafik',*KT['xt'],'Parabolik x–t grafiğinden anlık hız bulur.',
 metin='Doğrusal bir pistte sabit ivmeyle hareket eden bir deney aracının konum–zaman grafiği şekilde verilmiştir. Grafik, t = 0 anındaki konumu x = 0 olan aracın hareketinin ilk 4 saniyesini göstermektedir ve hareket aynı ivmeyle devam etmektedir.\nBuna göre, aracın t = 6 s anındaki hızının büyüklüğü kaç m/s dir?',
 dogru=35,yan=[(10,'0–2 s aralığındaki ortalama hızı (20 ÷ 2) 6. saniyedeki hız sanmış.','bilgi'),(15,'0–4 s ortalama hızını (60 ÷ 4) anlık hız olarak kullanmış.','bilgi'),(20,'2–4 s ortalama hızını (40 ÷ 2) 6. saniyedeki hız saymış.','bilgi'),(30,'İlk hızı sıfır varsayıp v = at (5 × 6) yazmış.','dikkat')],
 istenen='t = 6 s anında hızın büyüklüğü (m/s).',ip=['Grafikteki iki noktayı x = v₀t + ½at² bağıntısında yerine koyarak ilk hızı ve ivmeyi ayrı ayrı bul.'],
 bilgi=[B('Sabit ivmeli konum bağıntısı','x = v₀t + ½at²; iki farklı anın konumu bilinirse v₀ ve a bulunabilir. Örnek: v₀ = 1 m/s, a = 2 m/s² ise 3 s’de x = 3 + 9 = 12 m'),B('Hız','v = v₀ + at; ortalama hız ile anlık hız farklı kavramlardır')],
 ad=[A('Noktaları oku','Grafikten iki konum değeri alınır.','t = 2 s → x = 20 m; t = 4 s → x = 60 m'),A('Denklemleri yaz','Her nokta x = v₀t + ½at² bağıntısına konur.','2v₀ + 2a = 20 · 4v₀ + 8a = 60'),A('v₀ ve a’yı bul','İlk denklem 2’ye bölünüp ikinciden çıkarılır.','v₀ + a = 10 · v₀ + 2a = 15 → a = 5 m/s², v₀ = 5 m/s'),A('Hızı hesapla','v = v₀ + at.','v = 5 + 5 × 6 = 35 m/s')],
 puf='x–t parabolünde iki nokta, ilk hız ve ivmeyi belirler; ortalama hız yalnız aralığın orta anındaki anlık hızdır.',sekil=SK)

# =================== 05 · a–t grafiği · zor ===================
seg5=[(4,3),(2,0),(4,-6)]; vv=0; xx=0; yol5=0; vs=[0]
for T_,a in seg5:
    v1=vv+a*T_;
    if vv*v1<0:
        tz=Fr(-vv,a); yol5+=abs(vv)*tz/2+abs(v1)*(T_-tz)/2
    else: yol5+=abs(vv+v1)*T_/2
    xx+=(vv+v1)*T_/2; vv=v1; vs.append(vv)
assert vs==[0,12,12,-12] and xx==48 and yol5==72
assert 12==abs(3*4-6*4+0) and 60==24+24+12 and 120==12*10
kartla(5,'a–t alanı ile hız değişimi','a–t grafiğinin alanı hız değişimidir; hız–zaman çizilip işaret değiştirdiği yerde bölünerek yer değiştirme (işaretli alan) bulunur.','a–t alanını yer değiştirme sanmak; yol ile yer değiştirmeyi karıştırmak.','zor','grafik',6,*KT['at'])
SK=AX(pl([(0,3),(4,3)])+pl([(4,0),(6,0)])+pl([(6,-6),(10,-6)])+'\\draw[dashed,vurgu] (axis cs:4,3) -- (axis cs:4,0);\\draw[dashed,vurgu] (axis cs:6,0) -- (axis cs:6,-6);\n',10,-7,4,range(0,11,2),[-6,-3,0,3],'$a$ (m/s²)',extra='')
q(5,5,'zor','a–t alanı ile yer değiştirme','grafik',*KT['at'],'a–t grafiğinden hız ve yer değiştirme bulur.',
 metin='Doğrusal bir yolda t = 0 anında durgun halden harekete başlayan bir cismin ivme–zaman grafiği şekilde verilmiştir.\nBuna göre, cismin 0–10 s aralığındaki yer değiştirmesinin büyüklüğü kaç metredir?',
 dogru=48,yan=[(12,'a–t grafiğinin işaretli alanını (−12) yer değiştirme sanmış; bu alan hız değişimidir.','bilgi'),(60,'8. saniyede (hız sıfırlandığında) durup 0–8 s konumunu yer değiştirme saymış.','dikkat'),(72,'Hızın işaret değiştirdiğini görüp yönü dikkate almadan alanları toplamış (yol).','bilgi'),(120,'En büyük hızı (12 m/s) tüm süreyle çarpmış.','bilgi')],
 istenen='0–10 s aralığında yer değiştirmenin büyüklüğü (m).',ip=['Önce her bölümün sonundaki hızı bul; hız işaret değiştirdiğinde yer değiştirme için ters yöndeki alanı çıkar.'],
 bilgi=[B('a–t grafiği','ivme–zaman grafiğinin altındaki işaretli alan hız değişimidir. Örnek: 2 m/s² ivmeyle 3 s hızlanan cismin hızı 6 m/s artar'),B('Yer değiştirme ve yol','v–t grafiğinde zaman ekseninin altındaki alan ters yöndeki yer değiştirmedir; yer değiştirmede çıkarılır, yolda eklenir')],
 ad=[A('Hızları bul','Her bölümde Δv = a × Δt.','t = 4 s: v = 12 m/s · 6 s: 12 m/s · 10 s: 12 − 24 = −12 m/s'),A('Yön değişimini bul','v = 12 − 6(t − 6) = 0 denkleminden.','t = 8 s’de v = 0'),A('Alanları hesapla','0–4: üçgen, 4–6: dikdörtgen, 6–8: üçgen, 8–10: ters yönde üçgen.','24 m + 24 m + 12 m − 12 m'),A('Yer değiştirmeyi yaz','İşaretli alanlar toplanır.','Δx = 48 m')],
 puf='Önce a–t grafiğinden v–t grafiğini çiz; yer değiştirme için işaretli, yol için mutlak alan toplanır.',sekil=SK)

# =================== 06 · İki araç v–t (öncüllü) · orta ===================
xK=lambda t:Fr(2*t*t,2); xL=lambda t:10*t
assert xK(5)==25 and xL(5)==50 and 2*5==10 and xK(10)==xL(10)==100
kartla(6,'İki cismin v–t grafiği','v–t grafiklerinin kesim noktası hızların eşit olduğu andır, yan yana olmak ise alanların eşit olmasıdır.','Hızların eşitliğini yan yana olmakla karıştırmak.','orta','öncüllü',4,*KT['yo'])
SK=AX(pl([(0,0),(10,20)],'thick,vurgu')+pl([(0,10),(10,10)],'thick,dashed')+gd(5,10)+nd(8.5,17,'K','left')+nd(8.5,10,'L','below'),10,0,24,[0,5,10],[0,10,20],'$v$ (m/s)')
onc(6,6,'orta','İki cismin v–t grafiği',*KT['yo'],'Hız–zaman grafikleri yorumlanarak konum ve hız ilişkisi kurulur.',
 'Başlangıçta (t = 0) aynı noktadan, aynı yönde harekete geçen K ve L araçlarının doğrusal bir yoldaki hız–zaman grafikleri şekilde verilmiştir.\nBu araçların hareketi ile ilgili,',
 [('t = 5 s anında K ile L yan yana gelmiştir.',False,'0–5 s aralığında K’nin yolu 25 m, L’nin yolu 50 m olduğundan araçlar yan yana değildir.'),
  ('t = 5 s anında K ile L’nin hızları eşittir.',True,'grafikler t = 5 s’de kesişir; iki aracın hızı da 10 m/s’dir.'),
  ('t = 10 s anında K ile L yan yana gelmiştir.',True,'0–10 s aralığında iki grafiğin altındaki alanlar eşittir (100 m).')],
 ['Yalnız I','Yalnız III','I ve II','I ve III','II ve III'],None,ip=['Yan yana olmak için hangi niceliklerin eşit olması gerektiğini, grafiğin kesişiminin neyi gösterdiğiyle karşılaştır.'],
 istenen='Doğru yargıların belirlenmesi.',bilgi=[B('Kesişim noktası','v–t grafiklerinin kesiştiği an hızların eşit olduğu andır; konumların eşit olduğu an değildir'),B('Yan yana olma','aynı noktadan başlayan iki araç, grafikleri altındaki alanlar eşit olduğunda yan yana olur')],
 puf='v–t grafiklerinde kesişim hız eşitliğidir; konum eşitliği için alanlara bak.',sekil=SK)

# =================== 07 · Düşey atış · orta ===================
t1,t2=Fr(30-10,10),Fr(30+10,10); assert (t1,t2)==(2,4) and t2-t1==2 and Fr(30,10)==3 and Fr(2*30,10)==6 and 30//10-2==1
kartla(7,'Düşey atışta hız büyüklüğü eşitliği','Yükselirken ve alçalırken aynı hız büyüklüğüne iki ayrı anda ulaşılır: v = v₀ − gt, +v ve −v için iki an bulunur.','Tek anı bulup süre sanmak; tepe noktasına kadar geçen süreyi almak.','orta','şekilli',4,*KT['du'])
SK=tikz_svg(HEAD+r'''\fill[gray!35] (-1,-.2) rectangle (2.6,0); \draw (-1,0) -- (2.6,0); \node[right] at (2.7,0) {Yer (yatay)};
\fill (0,.1) circle (.12); \node[left] at (-.2,.1) {K};
\draw[vurgu,very thick,-{Stealth[length=2.2mm]}] (.6,.1) -- (.6,3.1); \node[right] at (.7,1.7) {$v_0=30$ m/s};''' +TAIL)
q(7,7,'orta','Düşey atış','şekilli',*KT['du'],'Düşey atışta iki an arasındaki süreyi bulur.',
 metin='Hava direncinin ihmal edildiği ve g = 10 m/s² alındığı bir ortamda, yerdeki K noktasından düşey yukarı doğru 30 m/s büyüklüğündeki hızla bir cisim atılıyor. Cismin hızının büyüklüğü hareketi boyunca iki kez 10 m/s oluyor.\nBuna göre, bu iki an arasında geçen süre kaç saniyedir?',
 dogru=2,yan=[(1,'Hız 10 m/s olduktan sonra tepe noktasına kadar geçen süreyi (1 s) iki an arasındaki süre sanmış.','dikkat'),(3,'Tepe noktasına çıkış süresini (30 ÷ 10) iki an arasındaki süre olarak vermiş.','bilgi'),(4,'Yalnız ikinci anı (t = 4 s) süre olarak almış.','dikkat'),(6,'Cismin havada kalma süresini (2 × 30 ÷ 10) yazmış.','bilgi')],
 istenen='Hızın büyüklüğünün 10 m/s olduğu iki an arasındaki süre (s).',ip=['Yukarı yönü pozitif alıp hızın hem +10 hem −10 m/s olduğu anları ayrı ayrı bul.'],
 bilgi=[B('Düşey atış','yukarı yönü pozitif alınırsa v = v₀ − gt olur; tepe noktasında v = 0’dır. Örnek: v₀ = 20 m/s ise t = 1 s’de v = 10 m/s, t = 3 s’de v = −10 m/s'),B('Simetri','yükselirken ve alçalırken aynı yükseklikte hız büyüklükleri eşittir')],
 ad=[A('Hız denklemini yaz','Yukarı yön pozitif.','v = 30 − 10t'),A('Yükselirken','v = +10 m/s.','30 − 10t₁ = 10 → t₁ = 2 s'),A('Alçalırken','v = −10 m/s (hız ters yönlü).','30 − 10t₂ = −10 → t₂ = 4 s'),A('Süreyi bul','İki an çıkarılır.','Δt = 4 − 2 = 2 s')],
 puf='Düşey atışta hız büyüklüğü iki ayrı anda aynı olur; yön işaretiyle iki denklem yaz.',sekil=SK)

# =================== 08 · Serbest düşen + atılan cisim · zor ===================
h8=80; tt=Fr(2); xa=lambda t:5*t*t; xb=lambda t:15*(t-1)+5*(t-1)**2
assert xa(tt)==xb(tt)==20 and h8-xa(tt)==60 and xa(3)==45 and xb(tt)+xa(tt)==40 and h8-5==75 and xa(tt)<h8
assert all(xa(t)!=xb(t) for t in [Fr(1),Fr(3),Fr(4)])
kartla(8,'Yakalama: serbest düşme + aşağı atış','İki cismin konum denklemleri aynı başlangıç noktasına göre yazılıp eşitlenir; ikinci cismin zamanı t − 1 alınır.','İkinci cismin zamanını t alıp 1 s’lik gecikmeyi unutmak; düşme yolu ile yüksekliği karıştırmak.','zor','şekilli',6,*KT['se'])
SK=tikz_svg(HEAD+r'''\fill[gray!35] (-.5,-.2) rectangle (4.4,0); \draw (-.5,0) -- (4.4,0);
\draw[thick,fill=gray!20] (0,0) rectangle (1.6,4); \node at (.8,2) {kule};
\fill (1.75,4.15) circle (.1); \node[left=1pt] at (1.65,4.45) {K};
\fill (2.35,4.15) circle (.1); \node[above] at (2.35,4.2) {L};
\draw[vurgu,very thick,-{Stealth[length=2mm]}] (2.35,4.0) -- (2.35,3.0); \node[right] at (2.45,3.5) {$15$ m/s};
\draw[<->] (3.7,0) -- (3.7,4.1); \node[right] at (3.75,2) {$80$ m};
\draw[dotted] (1.6,4.1) -- (3.8,4.1);''' +TAIL)
q(8,8,'zor','Yakalama','şekilli',*KT['se'],'Bırakılan ve atılan cismin karşılaşma yüksekliğini bulur.',
 metin='Hava direncinin ihmal edildiği ve g = 10 m/s² alındığı bir ortamda, yerden 80 m yüksekliğindeki bir kulenin tepesinden K cismi ilk hızsız bırakılıyor. K bırakıldıktan 1 s sonra aynı noktadan L cismi düşey aşağı doğru 15 m/s büyüklüğündeki ilk hızla atılıyor ve L, K’ye yere ulaşmadan yetişiyor.\nBuna göre, L cisminin K’ye yetiştiği anda cisimlerin yerden yüksekliği kaç metredir?',
 dogru=60,yan=[(20,'Yetişme anına kadar K’nin düştüğü yolu (20 m) yükseklik olarak vermiş.','dikkat'),(40,'İki cismin aldığı yolları (20 m + 20 m) toplayıp yükseklik olarak yazmış.','dikkat'),(45,'Zamanı yanlış (3 s) bulup düşme yolunu (5 × 3²) yükseklik sanmış.','islem'),(75,'Yetişme anında yalnız 5 m (ilk 1 s) düşüldüğünü sanıp 80 − 5 hesaplamış.','bilgi')],
 istenen='Yetişme anında yerden yükseklik (m).',ip=['İkisinin de kule tepesinden aşağı doğru aldığı yolu ayrı yazıp eşitle; L’nin hareket süresi K’ninkinden 1 s kısadır.'],
 bilgi=[B('Aşağı atış','x = v₀t + ½gt²; serbest düşmede v₀ = 0’dır. Örnek: 10 m/s ile atılan cisim 2 s’de 20 + 20 = 40 m düşer'),B('Gecikmeli başlama','sonradan harekete başlayan cisim için süre (t − 1) alınır')],
 ad=[A('K’nin yolu','K t süre düşer.','x_K = 5t²'),A('L’nin yolu','L (t − 1) süre hareket eder.','x_L = 15(t − 1) + 5(t − 1)²'),A('Eşitle','Yetiştiğinde ikisi de aynı yolu almıştır.','5t² = 15t − 15 + 5t² − 10t + 5 → t = 2 s'),A('Yüksekliği bul','K 2 s’de 20 m düşmüştür.','x = 5 × 2² = 20 m'),A('Sonuç','Kule yüksekliğinden düşülen yol çıkarılır.','h = 80 − 20 = 60 m')],
 puf='Yetişme sorularında iki cismin aldığı yolu aynı başlangıçtan yaz ve eşitle; gecikmeli cismin süresi t − Δt’dir.',sekil=SK)

# =================== 09 · x–t iki araç (öncüllü) · orta ===================
assert xL(5)==50 and xK(5)==25 and Fr(100,10)==Fr(100,10) and 2*10==20 and 10*2==20 and 20!=3*10
kartla(9,'x–t grafiğinde ortalama hız ve eğim','Ortalama hız yer değiştirme ÷ süre; x–t grafiğinin eğimi anlık hızdır, parabolde eğim doğrusal artar.','Eğimi bakmadan konum eşitliğini hız eşitliği saymak.','orta','öncüllü',4,*KT['yo'])
SK=AX(pl([(0,0),(10,100)],'thick,vurgu')+'\\addplot[thick,dashed,domain=0:10,samples=40]{x^2};\n'+nd(8,80,'K','above left')+nd(8.9,60,'L','below right'),10,0,110,range(0,11,2),range(0,101,20),'$x$ (m)')
onc(9,9,'orta','x–t grafiğinde yorum',*KT['yo'],'Konum–zaman grafiklerinden ortalama hız ve anlık hızı yorumlar.',
 'Aynı noktadan t = 0 anında aynı yönde harekete başlayan K ve L cisimlerinin konum–zaman grafikleri şekildeki gibidir. K sabit hızlı, L ise t = 0 anında durgun halden başlayan sabit ivmeli harekettir; grafikler t = 10 s’de kesişmektedir.\nBu hareketlerle ilgili,',
 [('0–10 s aralığında K ve L’nin ortalama hızları eşittir.',True,'iki cismin de 10 s’de yer değiştirmesi 100 m olduğundan ortalama hızları 10 m/s’dir.'),
  ('t = 10 s anında L’nin hızı K’nin hızının 3 katıdır.',False,'L’nin hızı 2 × 10 = 20 m/s, K’nin hızı 10 m/s’dir; oran 2’dir.'),
  ('t = 5 s anında K, L’nin 50 m ilerisindedir.',False,'t = 5 s’de K 50 m, L 25 m konumundadır; aralarındaki uzaklık 25 m’dir.')],
 ['Yalnız I','Yalnız II','Yalnız III','I ve II','II ve III'],None,ip=['Konum değişimini süreye bölerek ortalama hızı; L için x = ½at² bağıntısından ivmeyi ve hızı bul.'],
 istenen='Doğru yargıların belirlenmesi.',bilgi=[B('Ortalama hız','ortalama hız = Δx ÷ Δt; aynı yer değiştirmeyi aynı sürede yapan cisimlerin ortalama hızı eşittir. Örnek: 3 s’de 12 m giden cismin ortalama hızı 4 m/s'),B('Durgun başlayan sabit ivmeli hareket','x = ½at² ve v = at; x–t grafiği başlangıçta yatay teğetli paraboldür')],
 puf='Aynı sürede aynı yer değiştirmeyi yapan cisimlerin ortalama hızı eşittir; anlık hızlar farklı olabilir.',sekil=SK)

# =================== 10 · Tek cisim v–t (öncüllü) · orta ===================
pts10=[(0,-8),(4,8),(8,8),(10,0)]
a10=Fr(16,4); yol10=Fr(8*2,2)+Fr(8*2,2)+8*4+Fr(8*2,2); yd10=-8+8+32+8
assert a10==4 and yol10==56 and yd10==40 and Fr(8,4)*0==0 and 0==-8+4*2
kartla(10,'v–t grafiğinde yön değişimi','Hızın işaret değiştirdiği an yön değişimidir; eğim ivmeyi, alan yer değiştirmeyi verir; yolda alanların mutlak değerleri toplanır.','Eğimi yanlış okumak; yolu yer değiştirme saymak.','orta','öncüllü',4,*KT['yo'])
SK=AX(pl(pts10)+gd(4,8)+gd(8,8)+'\\draw[dashed,gray] (axis cs:0,-8) -- (axis cs:4,-8);',10,-10,11,range(0,11,2),[-8,0,8],'$v$ (m/s)')
onc(10,10,'orta','v–t grafiğinde yön değişimi',*KT['yo'],'Hız–zaman grafiğinden yön değişimi, ivme ve yolu yorumlar.',
 'Doğrusal bir yolda hareket eden bir cismin hız–zaman grafiği şekilde verilmiştir.\nBu cismin hareketi ile ilgili,',
 [('t = 2 s anında hareket yönünü değiştirmiştir.',True,'hız t = 2 s’de sıfırdan geçerek işaret değiştirir.'),
  ('0–4 s aralığındaki ivmesinin büyüklüğü 2 m/s² dir.',False,'ivme, grafiğin eğimine eşittir: 16 ÷ 4 = 4 m/s².'),
  ('0–10 s aralığında aldığı yol 56 m’dir.',True,'alanların mutlak değerleri: 8 + 8 + 32 + 8 = 56 m.')],
 ['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III'],None,ip=['Hızın sıfır olduğu anı, eğimin ne anlama geldiğini ve zaman ekseninin altında kalan alanı yola nasıl katacağını düşün.'],
 istenen='Doğru yargıların belirlenmesi.',bilgi=[B('Yön değişimi','hız işaret değiştirdiğinde cisim yön değiştirir; v = 0 olması tek başına yön değişimi değildir (durup aynı yönde sürebilir)'),B('Eğim ve alan','v–t eğimi ivme, alanı yer değiştirmedir; yol için mutlak alanlar toplanır')],
 puf='v–t grafiğinde işaret değişimi yön değişimidir; yol için eksenin altındaki alan da pozitif sayılır.',sekil=SK)

# =================== 11 · Ardışık eşit süreler · orta ===================
aa=Fr(40-20,4); vL=Fr(20+40,4); vK=vL-aa*2
assert aa==5 and vL==15 and vK==5 and vK*2+aa*4/2==20 and vK*4+aa*16/2==60 and Fr(20,2)==10 and vL+aa*2==25
kartla(11,'Ardışık eşit zamanlarda yol farkı','Sabit ivmede ardışık eşit sürelerde alınan yollar farkı Δx = aT²’dir; orta nokta hız ortalama hıza eşittir.','Ortalama hızı başlangıç hızı saymak; her aralığı ayrı ayrı denklemle çözmeye çalışıp yanılmak.','orta','şekilli',4,*KT['fo'])
SK=tikz_svg(HEAD+r'''\draw[thick] (0,0) -- (8.2,0);
\foreach \x/\n in {0/K,2.4/L,7.2/M}{\fill (\x,0) circle (.09); \node[above=3pt] at (\x,0) {\n};}
\draw[<->] (0,-.5) -- (2.4,-.5); \node[below] at (1.2,-.5) {$20$ m};
\draw[<->] (2.4,-.5) -- (7.2,-.5); \node[below] at (4.8,-.5) {$40$ m};
\draw[vurgu,very thick,-{Stealth[length=2mm]}] (.2,.9) -- (1.4,.9); \node[above] at (.8,.9) {hareket yönü};''' +TAIL)
q(11,11,'orta','Ardışık eşit süreler','şekilli',*KT['fo'],'Ardışık eşit süreli yollardan ilk hızı bulur.',
 metin='Doğrusal bir yolda ilerleyen ve sabit ivmeli hareket yapan bir araç, şekildeki K, L ve M noktalarından geçmektedir. Araç KL aralığını 2 s’de, LM aralığını da 2 s’de almıştır; bu aralıkların uzunlukları şekilde verilmiştir.\nBuna göre, aracın K noktasından geçerkenki hızının büyüklüğü kaç m/s dir?',
 dogru=5,yan=[(10,'KL aralığındaki ortalama hızı (20 ÷ 2) K noktasındaki hız sanmış.','bilgi'),(15,'L noktasındaki hızı bulup K noktasındaki hız olarak vermiş.','dikkat'),(20,'KL uzunluğunu (20 m) hız sanmış; birimleri karıştırmış.','dikkat'),(25,'M noktasındaki hızı (15 + 5 × 2) bulup istenenle karıştırmış.','dikkat')],
 istenen='K noktasından geçerkenki hızın büyüklüğü (m/s).',ip=['Ardışık eşit sürelerde alınan yolların farkından ivmeyi bul; sonra bir aralığın ortalama hızının hangi andaki hıza eşit olduğunu düşün.'],
 bilgi=[B('Ardışık eşit süreler','sabit ivmede her T süresinde yol farkı Δx = aT² olur. Örnek: 1 s’lik ardışık yollar 5 m ve 9 m ise a = 4 m/s²'),B('Ortalama hız','sabit ivmeli harekette bir aralığın ortalama hızı, aralığın orta anındaki hıza eşittir')],
 ad=[A('İvmeyi bul','Yol farkı aT²’ye eşittir.','40 − 20 = a × 2² → a = 5 m/s²'),A('L’deki hızı bul','KM aralığının ortalama hızı L’deki hıza eşittir.','v_L = (20 + 40) ÷ 4 = 15 m/s'),A('K’deki hızı bul','K’den L’ye 2 s’de hız a × t kadar artmıştır.','v_K = 15 − 5 × 2 = 5 m/s')],
 puf='Ardışık eşit sürelerde: ivme = yol farkı ÷ T²; orta noktadaki hız = toplam yol ÷ toplam süre.',sekil=SK)

# =================== 12 · Düşey atış vektörleri (öncüllü) · orta ===================
kartla(12,'Düşey atışta hız ve ivme yönleri','Düşey atışta ivme her noktada g’dir ve aşağı yönlüdür; tepe noktasında yalnız hız sıfırdır.','Tepe noktasında ivmenin sıfır olduğunu sanmak.','orta','öncüllü',3,*KT['du'])
SK=tikz_svg(HEAD+r'''\fill[gray!35] (-.6,-.2) rectangle (5.4,0); \draw (-.6,0) -- (5.4,0); \node[right] at (5.5,0) {Yer (yatay)};
\draw[dotted] (0,0) -- (0,3.6); \draw[dotted] (4.8,0) -- (4.8,3.6); \draw[dotted] (0,3.6) .. controls (1.2,4.3) and (3.6,4.3) .. (4.8,3.6);
\fill (0,1.2) circle (.09); \node[left] at (-.15,1.2) {K}; \draw[vurgu,very thick,-{Stealth[length=2mm]}] (.45,.9) -- (.45,2.3); \node[right] at (.5,1.6) {$v$};
\fill (2.4,3.95) circle (.09); \node[above] at (2.4,4) {L (en üst nokta)};
\fill (4.8,1.2) circle (.09); \node[right] at (4.95,1.2) {M}; \draw[vurgu,very thick,-{Stealth[length=2mm]}] (4.35,2.3) -- (4.35,.9); \node[left] at (4.3,1.6) {$v$};''' +TAIL)
onc(12,12,'orta','Düşey atışta vektörler',*KT['du'],'Düşey atış hareketinde hız ve ivme yönlerini yorumlar.',
 'Hava direncinin ihmal edildiği bir ortamda, yerden düşey yukarı atılan bir cisim şekildeki K noktasından yükselirken, en üst nokta olan L’den ve inerken M noktasından geçmektedir. K ile M aynı yükseklikte olup bu noktalardaki hız vektörleri şekilde gösterilmiştir.\nCismin bu noktalardaki hareketi ile ilgili,',
 [('K noktasında hız ve ivme vektörleri aynı yönlüdür.',False,'ivme aşağı yönlü, hız yukarı yönlüdür; vektörler zıt yönlüdür.'),
  ('L noktasında ivmenin büyüklüğü sıfırdır.',False,'L noktasında yalnız hız sıfırdır; ivme her noktada g = 10 m/s²’dir.'),
  ('M noktasında hız ve ivme vektörleri aynı yönlüdür.',True,'inerken hız da ivme de aşağı yönlüdür; cisim hızlanır.')],
 ['Yalnız III','I ve II','I ve III','II ve III','I, II ve III'],None,ip=['Yer çekimi ivmesinin yönünün hareketin hangi aşamasında değişip değişmediğini düşün.'],
 istenen='Doğru yargıların belirlenmesi.',bilgi=[B('Düşey atışta ivme','cisim yalnız yer çekiminin etkisindeyse ivme sabit ve aşağı yönlüdür; yükselirken cisim yavaşlar, inerken hızlanır'),B('Hız ve ivme yönü','aynı yönlüyse cisim hızlanır, zıt yönlüyse yavaşlar')],
 puf='Düşey atışta ivme hiç değişmez; değişen hızdır (tepede hız sıfır, ivme g).',sekil=SK,kalip='öncüllü')

# =================== 13 · Yetişme: v–t · zor ===================
xKf=lambda t:60+20*t; xLf=lambda t:Fr(30*t*t,12) if t<=6 else 90+30*(t-6)
assert xKf(15)==xLf(15)==360 and xLf(6)==90 and xKf(6)==180 and xKf(9)!=xLf(9)
assert Fr(60,30-20)==6 and 20*9==30*9-90 and 6+Fr(60,10)==12 and 60+20*24==30*(24-6)
kartla(13,'Yetişme problemi (v–t)','İki aracın konumları v–t alanlarından yazılıp ilk uzaklık da katılarak eşitlenir; hızlanma evresinin yolu unutulmaz.','İlk uzaklığı katmamak; hızlanma yolunu unutmak.','zor','grafik',6,*KT['ye'])
SK=AX(pl([(0,20),(16,20)],'thick,dashed')+pl([(0,0),(6,30),(16,30)])+gd(6,30)+nd(13,20,'K','below')+nd(13,30,'L','above'),16,0,36,range(0,16,3),[0,10,20,30],'$v$ (m/s)')
q(13,13,'zor','Yetişme problemi','grafik',*KT['ye'],'v–t grafiğinden iki aracın yetişme anını bulur.',
 metin='Doğrusal bir otoyolda t = 0 anında K otomobili, L polis aracının 60 m önünden, aynı yönde ve sabit hızla geçmektedir. Aynı anda durgun halden harekete geçen L’nin ve K’nin hız–zaman grafikleri şekilde verilmiştir.\nBuna göre, L polis aracı K otomobiline kaçıncı saniyede yetişir?',
 dogru=15,yan=[(6,'Hızlanma evresini yok sayıp L’nin başından beri 30 m/s ile gittiğini varsaymış: 60 ÷ (30 − 20).','bilgi'),(9,'Aradaki 60 m’yi katmadan konumları eşitlemiş: 20t = 30t − 90.','dikkat'),(12,'t = 6 s’de aradaki farkı hâlâ 60 m alıp 6 + 60 ÷ 10 yazmış.','islem'),(24,'L’nin hızlanma evresinde aldığı 90 m’yi katmayıp 30(t − 6) kullanmış.','bilgi')],
 istenen='L’nin K’ye yetiştiği an (s).',ip=['Önce 6. saniyede iki aracın konumlarını karşılaştır; sonra hızların sabit olduğu bölümde konum denklemlerini yaz.'],
 bilgi=[B('Yetişme koşulu','yetişme anında iki aracın konumları eşittir; arkadaki araç ilk uzaklığı da kapatmalıdır. Örnek: 40 m geriden 5 m/s fazla hızla gelen araç 8 s’de yetişir'),B('v–t alanı','hızlanma bölümünün yolu üçgen alanıdır')],
 ad=[A('L’nin ivmeli yolu','0–6 s: üçgen alan.','x_L(6) = ½ × 6 × 30 = 90 m'),A('t = 6 s’de K','K başlangıçta 60 m ileridedir.','x_K(6) = 60 + 20 × 6 = 180 m'),A('Aradaki fark','Bundan sonra iki araç da sabit hızlıdır.','180 − 90 = 90 m · göreli hız = 30 − 20 = 10 m/s'),A('Yetişme süresi','Fark göreli hızla kapanır.','90 ÷ 10 = 9 s sonra'),A('Toplam süre','6. saniyeden itibaren 9 s.','t = 6 + 9 = 15 s')],
 puf='Yetişme sorusunda önce ivmeli evrenin sonunda aradaki farkı hesapla, sonra göreli hızla kapat.',sekil=SK)

# =================== 14 · Yamuk v–t (öncüllü) · orta ===================
assert Fr(30+30,2)*0+Fr(50+30,2)*20==800 and Fr(20,10)==2 and Fr(800,50)==16 and 4!=2
kartla(14,'Yamuk v–t grafiği','Toplam yol yamuk alanıdır; ortalama hız toplam yol ÷ toplam süredir ve en büyük hıza eşit değildir.','Ortalama hızı en büyük hızla karıştırmak.','orta','öncüllü',4,*KT['yo'])
SK=AX(pl([(0,0),(10,20),(40,20),(50,0)])+gd(10,20),50,0,25,range(0,51,10),[0,10,20],'$v$ (m/s)')
onc(14,14,'orta','Yamuk v–t grafiği',*KT['yo'],'Yamuk biçimli hız–zaman grafiğini yorumlar.',
 'İstasyonlar arasında doğrusal ray üzerinde hareket eden bir metro treninin hız–zaman grafiği şekilde verilmiştir.\nBu hareket ile ilgili,',
 [('0–10 s aralığında ivmesinin büyüklüğü 4 m/s² dir.',False,'ivme eğimdir: 20 ÷ 10 = 2 m/s².'),
  ('İstasyonlar arası uzaklık 800 m’dir.',True,'yamuk alanı (50 + 30) ÷ 2 × 20 = 800 m’dir.'),
  ('Ortalama hızının büyüklüğü 20 m/s dir.',False,'ortalama hız 800 ÷ 50 = 16 m/s’dir; 20 m/s yalnız en büyük hızdır.')],
 ['Yalnız II','Yalnız III','I ve II','I ve III','I, II ve III'],None,ip=['Eğimin ve toplam alanın neyi verdiğini yaz; ortalama hızı toplam yol ve toplam süreyle bul.'],
 istenen='Doğru yargıların belirlenmesi.',bilgi=[B('Yamuk alan','alan = (üst taban + alt taban) ÷ 2 × yükseklik; v–t’de yoldur'),B('Ortalama sürat','toplam yol ÷ toplam süre; hızlanıp yavaşlayan araçta en büyük hızdan küçüktür')],
 puf='Ortalama hız = toplam yol ÷ toplam süre; grafiğin tepe değeri değildir.',sekil=SK)

# =================== 15 · x–t parabolü tepe · zor ===================
f15=lambda t:-2*t*t+16*t
assert f15(0)==0 and f15(4)==32 and f15(8)==0 and f15(6)==24 and 32+(32-24)==40 and 32+24==56 and 2*32==64
kartla(15,'x–t parabolünde tepe noktası','Parabolün tepe noktasında hız sıfırdır ve yön değişir; yol, konumdaki ileri-geri değişimlerin mutlak toplamıdır.','Yer değiştirmeyi yol saymak; tepeden sonra geri dönüşü eklememek.','zor','grafik',5,*KT['xt'])
SK=AX('\\addplot[thick,vurgu,domain=0:8,samples=60]{-2*x^2+16*x};\n\\addplot[only marks,mark=*,mark size=1.6pt,vurgu] coordinates {(0,0) (4,32) (8,0)};\n'+gd(4,32),8,0,36,range(0,9),range(0,33,8),'$x$ (m)')
q(15,15,'zor','x–t parabolünde yol','grafik',*KT['xt'],'x–t parabolünden yolu bulur.',
 metin='Doğrusal bir yolda sabit ivmeli hareket yapan bir cismin konum–zaman grafiği şekildeki gibidir. Grafik t = 0 ve t = 8 s anlarında x = 0 konumundan geçen, tepe noktası t = 4 s’de olan bir paraboldür.\nBuna göre, cismin 0–6 s aralığında aldığı yol kaç metredir?',
 dogru=40,yan=[(24,'6. saniyedeki konumu (yer değiştirmeyi) yol saymış.','bilgi'),(32,'Yalnız tepe noktasına kadar olan gidiş yolunu almış.','dikkat'),(56,'Gidiş yolu 32 m ile 6. saniyedeki konumu 24 m’yi toplamış; konumu yola eklemiş.','islem'),(64,'0–8 s aralığındaki toplam yolu (2 × 32) vermiş.','dikkat')],
 istenen='0–6 s aralığında alınan yol (m).',ip=['Tepe noktasında cismin hızı için ne söylenebilir? Cisim hangi anda ve hangi konumda yön değiştirir?'],
 bilgi=[B('Yön değişimi','x–t grafiğinin eğimi hızdır; tepe noktasında eğim sıfırdır ve cisim yön değiştirir'),B('Yol','ileri ve geri hareketin uzunlukları ayrı hesaplanıp toplanır. Örnek: 10 m ileri, 4 m geri giden cismin yolu 14 m, yer değiştirmesi 6 m’dir')],
 ad=[A('Yön değişimi','Tepe noktası t = 4 s, x = 32 m.','0–4 s: ileri 32 m'),A('x(t) bağıntısını bul','Parabol x = v₀t + ½at² biçiminde; (4, 32) ve (8, 0) noktaları.','v₀ = 16 m/s, a = −4 m/s² → x = 16t − 2t²'),A('6 s’deki konum','Bağıntıya t = 6 konur.','x(6) = 96 − 72 = 24 m'),A('Geri dönüş','4–6 s’de konum 32 m’den 24 m’ye iner.','32 − 24 = 8 m'),A('Yolu bul','İleri ve geri yol toplanır.','32 + 8 = 40 m')],
 puf='x–t parabolünde tepe, yön değiştirme anıdır; yolu bulmak için konumu önce ileri sonra geri parçalara ayır.',sekil=SK)

# =================== 16 · Son bir saniye · orta ===================
h16=80; assert 5*16-5*9==35 and h16==5*4**2 and 5*3**2==45 and 40*4==160 and 10*4-5==35
kartla(16,'Son saniyedeki yoldan yükseklik','Son 1 s’deki yol, toplam süreye bağlı iki konum farkı olarak yazılır; süre bulunup yükseklik hesaplanır.','Son saniye yolunu yükseklik sanmak; son hızı ortalama hız almak.','orta','şekilli',4,*KT['se'])
SK=tikz_svg(HEAD+r'''\fill[gray!35] (-.5,-.2) rectangle (3.6,0); \draw (-.5,0) -- (3.6,0);
\draw[thick,fill=gray!20] (0,0) rectangle (1.6,4); \fill (1.75,4.15) circle (.1); \node[right] at (1.9,4.15) {cisim (ilk hızsız)};
\draw[<->] (2.4,0) -- (2.4,1.75); \node[right] at (2.45,.85) {$35$ m}; \draw[dotted] (1.6,1.75) -- (2.5,1.75); \node[right] at (2.55,1.75) {son 1 s başlangıcı};''' +TAIL)
q(16,16,'orta','Son saniyede alınan yol','şekilli',*KT['se'],'Son saniyedeki yoldan bina yüksekliğini bulur.',
 metin='Hava direncinin ihmal edildiği ve g = 10 m/s² alındığı bir ortamda, bir binanın tepesinden ilk hızsız bırakılan bir cisim, yere çarpmadan önceki son 1 saniyede şekilde gösterilen yolu alıyor.\nBuna göre, binanın yüksekliği kaç metredir?',
 dogru=80,yan=[(35,'Son 1 saniyedeki yolu bina yüksekliği saymış.','dikkat'),(40,'Son hızı (40 m/s) yükseklik olarak yazıp birimleri karıştırmış.','bilgi'),(45,'Toplam süreyi 3 s bulup 5 × 3² = 45 m hesaplamış.','islem'),(160,'Son hız (40 m/s) ile süreyi (4 s) çarpmış; ortalama hızı almamış.','bilgi')],
 istenen='Binanın yüksekliği (m).',ip=['Son 1 saniyedeki yolu, toplam düşme süresine bağlı iki konum arasındaki fark olarak düşün.'],
 bilgi=[B('Serbest düşme yolu','ilk hızsız harekette h = ½gt² = 5t²; t s’de alınan yoldan (t − 1) s’de alınan yol çıkarılırsa son saniye yolu bulunur. Örnek: 2. saniyede alınan yol 20 − 5 = 15 m')],
 ad=[A('Toplam süre t olsun','t s’deki ve (t − 1) s’deki yol yazılır.','h = 5t² · h₁ = 5(t − 1)²'),A('Son saniye yolu','İkisinin farkı 35 m’dir.','5t² − 5(t − 1)² = 10t − 5 = 35'),A('Süreyi bul','Denklem çözülür.','t = 4 s'),A('Yüksekliği bul','Toplam süredeki yol hesaplanır.','h = 5 × 4² = 80 m')],
 puf='Son saniye sorularında toplam süreyi bilinmeyen alıp iki ardışık konum arasındaki farkı kur.',sekil=SK)

# =================== 17 · Üç top (öncüllü) · orta ===================
kartla(17,'Aynı yükseklikten farklı atışlar','Aynı yükseklikten eşit büyüklükte ilk hızla aşağı ve yukarı atılan cisimler yere aynı büyüklükte hızla çarpar; süreleri ise farklıdır.','Yukarı atılanın yere daha az hızla çarptığını sanmak.','orta','öncüllü',4,*KT['se'])
SK=tikz_svg(HEAD+r'''\fill[gray!35] (-.5,-.2) rectangle (6.5,0); \draw (-.5,0) -- (6.5,0); \node[right] at (6.6,0) {Yer (yatay)};
\foreach \x/\n in {0.8/K,3.1/L,5.4/M}{\fill (\x,3.2) circle (.1); \node[left=3pt] at (\x,3.2) {\n}; \draw[dotted] (\x,0) -- (\x,3.2);}
\draw[<->] (-.2,0) -- (-.2,3.2); \node[left] at (-.25,1.6) {$h$};
\node[below=2pt] at (.8,3.1) {ilk hızsız};
\draw[vurgu,very thick,-{Stealth[length=2mm]}] (3.1,3.05) -- (3.1,2.0); \node[right] at (3.15,2.5) {$v_0$};
\draw[vurgu,very thick,-{Stealth[length=2mm]}] (5.4,3.35) -- (5.4,4.4); \node[right] at (5.45,3.9) {$v_0$};''' +TAIL)
onc(17,17,'orta','Aynı yükseklikten üç atış',*KT['se'],'Serbest düşme ve düşey atış hareketlerini karşılaştırır.',
 'Hava direncinin ihmal edildiği bir ortamda, yerden h yüksekliğindeki aynı seviyeden K cismi ilk hızsız bırakılıyor, L cismi düşey aşağı yönde, M cismi ise düşey yukarı yönde v₀ büyüklüğünde ilk hızla aynı anda fırlatılıyor.\nCisimlerin yere çarpma anları ile ilgili,',
 [('L ve M’nin yere çarpma hızlarının büyüklükleri eşittir.',True,'v² = v₀² + 2gh bağıntısında yön yoktur; L ve M’nin hız büyüklükleri eşittir.'),
  ('K’nin yere çarpma hızının büyüklüğü, L’ninkinden küçüktür.',True,'K için v² = 2gh, L için v² = v₀² + 2gh olduğundan K’ninki küçüktür.'),
  ('Yere çarpma süreleri arasında t_M > t_K > t_L ilişkisi vardır.',True,'L ilk hızla aşağı gittiğinden en kısa sürede çarpar; M önce yükselip aynı seviyeye v₀ hızıyla döndüğünden en uzun sürede çarpar.')],
 ['Yalnız I','Yalnız III','I ve II','II ve III','I, II ve III'],None,ip=['Zamansız bağıntı hız büyüklüğünü yöne bakmadan verir; sürelerde ilk hızın yönü etkilidir.'],
 istenen='Doğru yargıların belirlenmesi.',bilgi=[B('Yere çarpma hızı','hava direnci yokken aynı yükseklikten eşit büyüklükte ilk hızla atılan cisimler, yönleri farklı olsa da yere aynı hızla çarpar'),B('Süre','aşağı atılan cisim ilk hızı olduğundan serbest bırakılandan, yukarı atılan ise önce çıkıp döndüğünden daha uzun sürede düşer')],
 puf='Yere çarpma hızı yalnız ilk hızın büyüklüğüne ve yüksekliğe bağlıdır; süre ise yöne de bağlıdır.',sekil=SK)

# =================== 18 · Tablo · orta ===================
vt=[6,10,14,18,22]; a18=4; assert all(vt[i+1]-vt[i]==a18 for i in range(4))
d24=Fr(vt[2]+vt[4],2)*2; assert d24==36 and vt[2]*2==28 and vt[4]*2==44 and 6*4+Fr(a18*16,2)==56 and Fr(vt[2]+vt[4],2)==18
kartla(18,'Tablodan yol','Sabit ivmede ortalama hız, aralığın başı ve sonundaki hızların ortalamasıdır; yol = ortalama hız × süre.','Başlangıç ya da son hızı tüm süreyle çarpmak.','orta','tablo',3,*KT['fo'])
SK=tablo_svg(['t (s)','0','1','2','3','4'],[['v (m/s)']+[str(x) for x in vt]])
q(18,18,'orta','Tablodan yol','tablo',*KT['fo'],'Tablodaki hız verilerinden yol hesaplar.',
 metin='Doğrusal bir yolda sabit ivmeyle hızlanan bir deney arabasının hızı, bir hız sensörüyle her saniye ölçülmüş ve aşağıdaki tabloda gösterilmiştir.\nBuna göre, arabanın t = 2 s ile t = 4 s arasında aldığı yol kaç metredir?',
 dogru=36,yan=[(18,'İki hızın ortalamasını (18 m/s) yol olarak yazmış; süreyle çarpmamış.','dikkat'),(28,'2 s’deki hızı (14 m/s) tüm süreyle çarpmış.','bilgi'),(44,'4 s’deki hızı (22 m/s) tüm süreyle çarpmış.','bilgi'),(56,'t = 0’dan t = 4 s’ye kadar olan yolu hesaplamış.','dikkat')],
 istenen='t = 2 s ile t = 4 s arasında alınan yol (m).',ip=['Hız düzgün arttığına göre aralığın ortalama hızı hakkında ne söylenebilir?'],
 bilgi=[B('Ortalama hız','sabit ivmeli harekette v_ort = (v₀ + v) ÷ 2’dir; yol = v_ort × Δt. Örnek: 2 m/s’den 6 m/s’ye 3 s’de hızlanan cisim 12 m gider')],
 ad=[A('Tabloyu oku','İstenen aralığın uçlarındaki hızlar.','t = 2 s: 14 m/s; t = 4 s: 22 m/s'),A('Ortalama hızı bul','Hız düzgün arttığından uçların ortalaması alınır.','v_ort = (14 + 22) ÷ 2 = 18 m/s'),A('Yolu bul','Yol = ortalama hız × süre.','x = 18 × 2 = 36 m')],
 puf='Sabit ivmede bir aralığın yolu, uç hızların ortalaması ile süresinin çarpımıdır.',sekil=SK)

# =================== 19 · Tepki süresi · zor ===================
tep=20*1; fre=50-tep; v19=(20**2-2*5*fre); assert fre==30 and v19==100 and v19**0.5==10 and 20+Fr(400,10)==60>50 and 20-5*1==15
kartla(19,'Tepki süresi ve frenleme','Tepki süresince hız sabit, sonra sabit ivmeli yavaşlama; engele kalan yol için v² = v₀² − 2ax.','Tepki yolunu katmamak; frenleme yolunu 50 m almak.','zor','şekilli',5,*KT['fo'])
SK=tikz_svg(HEAD+r'''\fill[gray!35] (-.3,-.2) rectangle (8.8,0); \draw (-.3,0) -- (8.8,0);
\draw[thick,fill=gray!25] (0,.18) rectangle (1.6,.78); \draw[thick,fill=white] (.25,.78) -- (.5,1.1) -- (1.1,1.1) -- (1.35,.78);
\draw[fill=black] (.35,.18) circle (.17); \draw[fill=black] (1.25,.18) circle (.17);
\draw[vurgu,very thick,-{Stealth[length=2mm]}] (.8,1.5) -- (2.2,1.5); \node[above] at (1.5,1.5) {$72$ km/h};
\draw[very thick] (8.0,0) -- (8.0,1.1); \fill[red!70!black] (7.8,1.1) rectangle (8.2,1.3); \node[above] at (8.0,1.3) {engel};
\draw[<->] (1.6,-.55) -- (8.0,-.55); \node[below] at (4.8,-.55) {$50$ m}; \draw[dotted] (1.6,0) -- (1.6,-.55); \draw[dotted] (8,0) -- (8,-.55);''' +TAIL)
q(19,19,'zor','Tepki süresi ve frenleme','şekilli',*KT['fo'],'Tepki süresini de içeren frenleme probleminde hızı bulur.',
 metin='Yatay ve doğrusal bir yolda 72 km/h sabit hızla giden bir otomobilin sürücüsü, önünde durmakta olan bir engeli görüyor; görme anındaki uzaklık şekilde verilmiştir. Sürücü engeli gördükten 1 s sonra frene basıyor ve otomobil 5 m/s² büyüklüğünde sabit ivmeyle yavaşlıyor. Tepki süresi boyunca hız sabittir.\nBuna göre, otomobil engele çarpıyorsa çarpma anındaki hızının büyüklüğü kaç m/s dir?',
 dogru=10,yan=[(0,'Frenleme yolunu 50 m alıp aracın engelden önce durduğunu sanmış.','dikkat'),(5,'İvme büyüklüğünü (5 m/s²) hız sanmış.','dikkat'),(15,'Frenleme süresi yerine tepki süresini (1 s) kullanıp 20 − 5 × 1 yazmış.','islem'),(20,'Hızın değişmediğini düşünmüş.','bilgi')],
 istenen='Engele çarpma anındaki hızın büyüklüğü (m/s).',ip=['Tepki süresinde araç ne kadar yol alır? Frenleme için geriye kalan yolu bulup zamansız bağıntıyı kullan.'],
 bilgi=[B('Birim çevirme','km/h değeri 3,6’ya bölünür'),B('Zamansız bağıntı','v² = v₀² − 2ax; tepki süresinde hız sabit olduğundan yol = v × t. Örnek: 10 m/s ile giden araç 1 s’de 10 m alır')],
 ad=[A('Hızı çevir','72 km/h değeri m/s’ye çevrilir.','v₀ = 20 m/s'),A('Tepki yolunu bul','Hız sabit olduğundan yol = hız × süre.','x₁ = 20 × 1 = 20 m'),A('Frenleme yolunu bul','Engele kalan uzaklık.','x₂ = 50 − 20 = 30 m'),A('Duruş yolunu kontrol et','Durma yolu 400 ÷ 10 = 40 m > 30 m olduğundan çarpar.','40 > 30'),A('Çarpma hızını bul','v² = v₀² − 2ax₂.','v² = 400 − 2 × 5 × 30 = 100 → v = 10 m/s')],
 puf='Tepki süresinde hız sabittir; frenleme için kalan yolu hesapla, durma yolunun bu yoldan uzun olduğunu kontrol et.',sekil=SK)

# =================== 20 · Karşılaşma · zor ===================
tk=Fr(50,25); hy=25*tk-5*tk**2; ly=50-5*tk**2
assert tk==2 and hy==ly==30 and 5*tk**2==20 and 50-5==45 and 25*tk==50 and 25*tk-5*tk**2<31.25*2
kartla(20,'Karşılaşma noktası','İki cismin konumları aynı eksende yazılıp eşitlenir.','g’yi unutmak; süreyi yanlış bulmak.','orta','şekilli',5,*KT['du'])
SK=tikz_svg(HEAD+r'''\fill[gray!35] (-.8,-.2) rectangle (2.4,0); \draw (-.8,0) -- (2.4,0); \node[below] at (.8,-.2) {Yer (yatay)};
\fill (0,.1) circle (.11); \node[left] at (-.2,.1) {K};
\draw[vurgu,very thick,-{Stealth[length=2.2mm]}] (.5,.1) -- (.5,1.9); \node[right] at (.6,1.0) {$25$ m/s};
\fill (0,4.0) circle (.11); \node[left] at (-.2,4.0) {L}; \node[right] at (.2,4.0) {ilk hızsız};
\draw[<->] (2.9,0) -- (2.9,4.0); \node[right] at (3.0,2.1) {$50$ m};
\draw[dotted] (0,0) -- (0,4.0);''' +TAIL)
q(20,20,'orta','Karşılaşma','şekilli',*KT['du'],'Aynı doğrultuda hareket eden iki cismin karşılaşma yüksekliğini bulur.',
 metin='Hava direncinin ihmal edildiği ve g = 10 m/s² alındığı bir ortamda, yerdeki K noktasından düşey yukarı doğru 25 m/s büyüklüğündeki hızla bir cisim atılıyor. Aynı anda, K’nin tam üstünde ve yerden 50 m yükseklikteki L noktasından ikinci bir cisim ilk hızsız bırakılıyor. Cisimler aynı düşey doğru üzerinde hareket ederek havada karşılaşıyor.\nBuna göre, cisimlerin karşılaştığı noktanın yerden yüksekliği kaç metredir?',
 dogru=30,yan=[(20,'L’nin karşılaşma anına kadar düştüğü yolu (20 m) yükseklik sanmış.','dikkat'),(40,'L’nin düşme yolunu 5t² yerine 5t = 10 m alıp 50 − 10 hesaplamış.','islem'),(45,'Yaklaşma hızını 50 m/s sanıp t = 1 s bulmuş, L için 50 − 5 hesaplamış.','islem'),(50,'K’nin 25 m/s hızla yerçekimsiz gideceğini düşünüp 25 × 2 = 50 m bulmuş.','bilgi')],
 istenen='Karşılaşma noktasının yerden yüksekliği (m).',ip=['İki cismin ivmeleri hakkında ne söylenebilir? Karşılaşma süresini önce bul.'],
 bilgi=[B('Göreli hareket','iki cisim de yalnız yer çekimiyle hareket ediyorsa ivmeleri eşittir; birbirlerine göre sabit hızla yaklaşırlar. Örnek: aralarında 30 m olan ve göreli hızı 10 m/s olan cisimler 3 s’de karşılaşır'),B('Düşey atış konumu','yukarı yön pozitifse y = v₀t − ½gt²')],
 ad=[A('Göreli hızı bul','L ilk hızsız, K 25 m/s; ivmeler eşit olduğundan göreli ivme sıfırdır.','göreli hız = 25 − 0 = 25 m/s'),A('Karşılaşma süresi','Uzaklık ÷ göreli hız.','t = 50 ÷ 25 = 2 s'),A('K’nin yüksekliği','y = v₀t − ½gt².','y = 25 × 2 − 5 × 2² = 30 m'),A('Kontrol et','L’nin yüksekliği aynı olmalıdır.','50 − 5 × 2² = 30 m ✓')],
 puf='Aynı ivmeyle hareket eden iki cismin arasındaki uzaklık sabit göreli hızla kapanır: t = uzaklık ÷ göreli hız.',sekil=SK)

H.HD=GD
bitir(P,'ivmeli',KK)
# kart dosyasının adı af önekiyle
import shutil
os.replace(os.path.join(HV,'kartlar','ivmeli.json'),os.path.join(HV,'kartlar','afivmeli.json'))
