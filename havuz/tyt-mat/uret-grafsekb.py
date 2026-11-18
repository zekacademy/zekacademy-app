"""Grafik Problemleri · ŞEKİLLİ ek paket (grafsekb): 10 soru; grafik/tablo/diyagram verinin tamamını taşır; her doğru ve çeldirici değer Python'da hesaplanıp assert edilir. Kardeş yok, ipucu 1."""
import sys,os,math
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
H.KONU='Grafik Problemleri'
P=Parti('grafsekb','Grafik Problemleri','prob|Grafik Problemleri')
KY='ÖSYM 2018–2026 TYT Matematik (grafik, tablo ve diyagram okuma problemleri; yalnız mantık) · MEB 9. sınıf'
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)
def fig(body): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'+body+'\n\\end{tikzpicture}')
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)
def tx(x,y,t,st=''): return f'\\node[{st}] at ({x:.3f},{y:.3f}) {{{t}}};'
def ln(x1,y1,x2,y2,st=''): return f'\\draw[{st}] ({x1:.3f},{y1:.3f}) -- ({x2:.3f},{y2:.3f});'
def eksen(xmax,ymax,sx,sy,xt,yt,xe='',ye='',yfmt=str,xfmt=str,grid=True):
    o=[]
    if grid:
        for v in yt: o.append(ln(0,v*sy,xmax*sx,v*sy,'black!12,line width=.4pt'))
    for v in yt: o.append(tx(-.3,v*sy,f'\\footnotesize {yfmt(v)}'))
    for v in xt: o.append(tx(v*sx,-.3,f'\\footnotesize {xfmt(v)}'))
    o+=[ln(0,0,0,ymax*sy,'line width=1pt'),ln(0,0,xmax*sx,0,'line width=1.2pt')]
    if ye: o.append(tx(.2,ymax*sy+.3,f'\\footnotesize {ye}','anchor=west'))
    if xe: o.append(tx(xmax*sx+.1,-.3,f'\\footnotesize {xe}','anchor=west'))
    return o

PIK=B('Piktogram','piktogramda her simge belirli sayıda varlığı gösterir; yarım simge bunun yarısıdır. Bir türün sayısı, simge sayısının simgenin değeriyle çarpılmasıyla bulunur. Örnek: 1 simge = 10 ise 3,5 simge 35’i gösterir')
KAR=B('Gelir, gider ve kâr','bir ayda gelir giderden fazlaysa fark kâr, azsa zarardır; kâr = gelir − gider’dir. Örnek: gelir 30, gider 22 ise kâr 8’dir')
YIG=B('Yığılmış sütun grafiği','sütunun parçaları o sınıf içindeki alt grupları gösterir; bir sütunun toplamı parçalarının toplamıdır. Örnek: 9 kırmızı ve 6 mavi parçası olan sütun toplam 15’i gösterir')
HIZ=B('Ortalama hız','ortalama hız = toplam yol ÷ toplam süre’dir. Hız–zaman grafiğinde yatay eksen süreyi, dikey eksen hızı gösterir. Örnek: 150 km’yi 3 saatte alan aracın ortalama hızı 50 km/sa’tir')
KUM=B('Birikimli grafik','birikimli grafikte her nokta, o ana kadarki toplamı gösterir; iki ardışık noktanın farkı o dönemdeki değerdir. Örnek: toplam 12’den 17’ye çıkıyorsa o dönemde 5 artış vardır')
GOV=B('Gövde–yaprak diyagramı','gövde onlar basamağını, yaprak birler basamağını gösterir; 5 | 3 ifadesi 53’ü belirtir. Örnek: 2 | 1 4 diyagramında 21 ve 24 puanı vardır; ortalama, tüm değerlerin toplamının değer sayısına bölünmesiyle bulunur')
TAR=B('Parçalı doğrusal grafik','grafik, doğrusal parçalardan oluşur; her parçada eğim, yatay eksendeki birim başına dikey eksendeki değişimi gösterir. Örnek: (2, 10) ve (6, 18) noktaları arasında eğim (18 − 10) ÷ (6 − 2) = 2’dir')
YUZ=B('Yüzde değişim','bir değer %p artırılırsa (1 + p/100) ile, %p azaltılırsa (1 − p/100) ile çarpılır. Örnek: 200’ün %10 artmış hâli 200 × 1,10 = 220’dir')
DOG=B('Doğru grafiği','doğrusal grafikte iki noktadan eğim ve doğrunun denklemi bulunur; y = m·x + n biçimindedir (n, x = 0’daki değerdir). Örnek: (0, 5) ve (4, 13) noktalarından geçen doğru için eğim (13 − 5) ÷ 4 = 2 olduğundan y = 2x + 5’tir')
HZ2=B('Hareket hâlinde ortalama hız','durulan süreler yolculuk süresinden çıkarılırsa yalnız hareket süresi kalır; ortalama hız bu süre üzerinden toplam yola bölünerek bulunur. Örnek: 90 km yol, 2 saat hareket ve 30 dakika bekleme varsa hareket hâlindeki ortalama hız 90 ÷ 2 = 45 km/sa’tir')

kartla('K-GFB-01','Piktogramda yarım simge','Simge sayılarını (yarım simgeler dâhil) okuyup farkı bulur, sonra simge değeriyle çarpar.','Yarım simgeyi saymamak veya tam saymak; simge değeriyle çarpmayı unutmak.','kolay','grafik',3,'gfb-piktogram','Piktogramda yarım simge ve ölçek')
kartla('K-GFB-02','Gelir–gider çizgileri','İki çizginin her ay için farkı alınır; yalnız kâr edilen aylar toplanır.','Zarar eden ayları da toplamak; net toplamı almak.','kolay','grafik',3,'gfb-cizgi','İki çizgili gelir–gider grafiği')
kartla('K-GFB-03','Yığılmış sütunlarda pay','Her sütunun iki parçası okunur; koşulu sağlayan sütunlar seçilip toplam içindeki pay yüzdeye çevrilir.','Yanlış sütunları seçmek; payı adet olarak bırakmak.','orta','grafik',4,'gfb-yigma','Yığılmış sütun grafiğinde koşullu pay')
kartla('K-GFB-04','Hız–zaman grafiğinde ortalama hız','Grafikten toplam yol ve toplam süre bulunur; yol süreye bölünür.','Ortalama hızı en yüksek hız veya uç hızların ortalaması sanmak.','orta','grafik',4,'gfb-hiz','Hız–zaman grafiğinde ortalama hız')
kartla('K-GFB-05','Birikimli çizgi grafiği','Ardışık noktaların farkı haftalık değeri verir; ortalamayla karşılaştırılıp koşulu sağlayanlar toplanır.','Birikimli değeri haftalık değer sanmak.','orta','grafik',4,'gfb-kumul','Birikimli grafikte haftalık değer ve ortalama')
kartla('K-GFB-06','Gövde–yaprak diyagramı','Diyagramdan değerler yazılır, ortalama bulunur, ortalamadan uzaklığı koşulu sağlayanlar sayılır.','Eşitlik sınırındaki değeri atlamak; yalnız bir yöne bakmak.','orta','şekilli',4,'gfb-govde','Gövde–yaprak diyagramında ortalama ve uzaklık')
kartla('K-GFB-07','Parçalı doğrusal tarife','Her parçanın eğimi (birim fiyat) bulunur; hangi dilimde kalındığı belirlenip denklem çözülür.','Tüm tüketimi tek fiyatla hesaplamak; dilim sınırını karıştırmak.','zor','grafik',5,'gfb-tarife','Parçalı doğrusal tarife grafiği')
kartla('K-GFB-08','Ardışık yüzde değişimleri','Her aydaki değer bir önceki aya göre çarpanla bulunur; istenen iki ay arasındaki fark alınır.','Yüzdeleri toplamak; yüzdeyi ilk aya göre uygulamak.','orta','grafik',5,'gfb-yuzde','Ardışık yüzde değişimleri grafiği')
kartla('K-GFB-09','Gelir ve maliyet doğruları','İki noktadan gelir ve maliyet doğrularının denklemleri yazılır; kâr eşitliğinden ürün sayısı bulunur.','Sabit gideri atlamak; maliyetin eğimine bölmek.','zor','grafik',5,'gfb-dogru','Gelir ve maliyet doğrularında kâr')
kartla('K-GFB-10','Tren tarife tablosu','Tablodan bölüm süreleri ve yol okunur; bekleme süreleri çıkarılarak hareket süresi bulunur ve yol bu süreye bölünür.','Bekleme sürelerini hareket süresine katmak; bir bölümü unutmak.','orta','tablo',5,'gfb-tren','Tarife tablosunda hareket hâlindeki ortalama hız')

# ---------- 01 piktogram ----------
sv=40; sim={'Roman':6,'Şiir':3.5,'Öykü':4,'Deneme':2.5}
fark=sim['Şiir']+sim['Öykü']+sim['Deneme']-sim['Roman']; d1=int(fark*sv); assert (fark,d1)==(4,160)
e1=[int(fark),int((3+4+2-6)*sv),int((4+2.5-6)*sv),int((3.5+4-6)*sv)]; assert e1==[4,120,20,60] and len({d1,*e1})==5
o=[]; r=.17
for i,(k,n) in enumerate(sim.items()):
    y=-i*.55; o.append(tx(-.1,y,f'\\textbf{{{k}}}','anchor=east'))
    for j in range(int(n)): o.append(f'\\filldraw[fill=vurgu!55,line width=.8pt] ({j*.45+.35:.2f},{y:.2f}) circle ({r});')
    if n%1: j=int(n); xx=j*.45+.35; o.append(f'\\draw[line width=.8pt] ({xx:.2f},{y:.2f}) circle ({r});'); o.append(f'\\fill[vurgu!55] ({xx:.2f},{y+r:.2f}) arc (90:270:{r}) -- cycle;')
o.append(f'\\filldraw[fill=vurgu!55,line width=.8pt] (4.2,.55) circle ({r});'); o.append(tx(4.5,.55,'= 40 kitap','anchor=west,font=\\footnotesize'))
SK=fig('\n'.join(o))
q('0001',tipId='gfb-piktogram',tip='Piktogramda yarım simge ve ölçek',z='kolay',alt='Piktogram',kaz='Piktogramdaki tam ve yarım simgeleri sayıp simge değeriyle çarparak toplam farkı bulur.',kalip='grafik',sekil=SK,
 kart='K-GFB-01 (piktogram) · 1 simge = 40 kitap; 6, 3,5, 4, 2,5 simge',
 metin='Bir semt kitapçısında bir günde satılan dört farklı türdeki kitabın adetleri, vitrin panosuna asılan yukarıdaki piktogramda gösterilmiştir; her tam simge belirtilen sayıda kitabı, yarım simge bunun yarısını göstermektedir.\nBuna göre şiir, öykü ve deneme kitaplarının satış adetleri toplamı, roman kitaplarının satış adedinden kaç fazladır?',
 dogru=d1,yan=[(4,'Simge sayısındaki farkı (4) bulup simge değeriyle çarpmamış.','dikkat'),(120,'Yarım simgeleri saymamış.','dikkat'),(20,'Şiir kitaplarını toplama katmamış.','dikkat'),(60,'Deneme kitaplarını toplama katmamış.','dikkat')],
 istenen='Satış adedi farkı.',
 ip=['Her türün simge sayısını yarım simgeleri de sayarak yaz.'],
 bilgi=[PIK],
 ad=[A('Simge sayıları','Yarım simgeler 0,5 sayılır.','roman 6; şiir 3,5; öykü 4; deneme 2,5'),A('Simge farkı','Diğer üç tür toplamından roman çıkarılır.','3,5 + 4 + 2,5 − 6 = 4'),A('Adet','Simge sayısı simge değeriyle çarpılır.','4 × 40 = 160')],
 puf='Yarım simgeyi 0,5 say; farkı simge cinsinden bulup simgenin değeriyle çarp.')

# ---------- 02 iki çizgili gelir–gider ----------
ay=['Oca','Şub','Mar','Nis','May']; gel=[40,55,60,45,70]; gid=[50,45,35,50,40]
fk=[a-b for a,b in zip(gel,gid)]; d2=sum(x for x in fk if x>0); assert (fk,d2)==([-10,10,25,-5,30],65)
e2=[sum(fk),-sum(x for x in fk if x<0),max(gel),sum(abs(x) for x in fk)]; assert e2==[50,15,70,80] and len({d2,*e2})==5
sx=.9; sy=.045; o=eksen(5.2,85,sx,sy,[],range(0,81,10),ye='bin TL')
for i,a in enumerate(ay): o.append(tx((i+.5)*sx,-.3,f'\\footnotesize {a}'))
pg=[((i+.5)*sx,v*sy) for i,v in enumerate(gel)]; pd=[((i+.5)*sx,v*sy) for i,v in enumerate(gid)]
o.append('\\draw[line width=1.6pt,vurgu] '+' -- '.join(f'({x:.2f},{y:.2f})' for x,y in pg)+';')
o.append('\\draw[line width=1.6pt,dashed] '+' -- '.join(f'({x:.2f},{y:.2f})' for x,y in pd)+';')
for x,y in pg: o.append(f'\\fill[vurgu] ({x:.2f},{y:.2f}) circle (.07);')
for x,y in pd: o.append(f'\\filldraw[fill=white] ({x-.06:.2f},{y-.06:.2f}) rectangle ({x+.06:.2f},{y+.06:.2f});')
o+=[ln(5.5,3.3,5.9,3.3,'line width=1.6pt,vurgu'),tx(6.0,3.3,'Gelir','anchor=west,font=\\footnotesize'),ln(5.5,2.85,5.9,2.85,'line width=1.6pt,dashed'),tx(6.0,2.85,'Gider','anchor=west,font=\\footnotesize')]
SK=fig('\n'.join(o))
q('0002',tipId='gfb-cizgi',tip='İki çizgili gelir–gider grafiği',z='kolay',alt='Çizgi Grafiği',kaz='İki çizgili grafikten her ayın kâr veya zararını bulup yalnız kâr edilen ayların toplamını hesaplar.',kalip='grafik',sekil=SK,
 kart='K-GFB-02 (gelir–gider) · kâr aylarında 10 + 25 + 30',
 metin='Yeni açılan bir kafenin işletmecisi, ilk beş ayına ait aylık gelir ve gider miktarlarını yukarıdaki çizgi grafiğinde bin TL cinsinden göstermiştir. Bir ayda gelirin giderden fazla olması kâr, az olması zarar anlamına gelmektedir.\nBuna göre kâr edilen aylardaki kârların toplamı kaç bin TL’dir?',
 dogru=d2,yan=[(50,'Kâr ve zararların net toplamını (65 − 15) bulmuş.','dikkat'),(15,'Yalnız zarar edilen ayların toplamını yazmış.','dikkat'),(70,'En yüksek geliri (mayıs ayı) yazmış.','dikkat'),(80,'Zarar edilen ayların farklarını da toplamaya katmış.','dikkat')],
 istenen='Kâr edilen aylardaki toplam kâr (bin TL).',
 ip=['Her ay için gelir ile gideri karşılaştır; hangi aylarda gelir fazla?'],
 bilgi=[KAR],
 ad=[A('Değerleri oku','Her ayın gelir ve gideri okunur.','gelir 40; 55; 60; 45; 70; gider 50; 45; 35; 50; 40'),A('Farklar','Her ay gelirden gider çıkarılır.','−10; 10; 25; −5; 30'),A('Kâr edilen aylar','Yalnız pozitif farklar toplanır.','10 + 25 + 30 = 65')],
 puf='Zarar eden ayları toplamaya katma; yalnız gelirin giderden fazla olduğu aylara bak.')

# ---------- 03 yığılmış sütun ----------
sn=['A','B','C']; kz=[18,14,20]; er=[12,16,12]; eT=sum(er)
sel=[i for i in range(3) if kz[i]>er[i]]; d3=Fr(sum(er[i] for i in sel)*100,eT); assert (sel,d3)==([0,2],60)
e3=[sum(er[i] for i in sel),Fr(er[0]*100,eT),Fr(er[1]*100,eT),sum(kz)]; assert e3==[24,30,40,52] and len({d3,*e3})==5
sy=.075; o=eksen(3.6,40,1,sy,[],range(0,41,10),ye='Öğrenci sayısı')
for i in range(3):
    x=.3+i*1.1; o.append(f'\\filldraw[fill=vurgu!45,line width=.8pt] ({x:.2f},0) rectangle ({x+.7:.2f},{kz[i]*sy:.3f});'); o.append(tx(x+.35,kz[i]*sy/2,f'\\footnotesize {kz[i]}'))
    o.append(f'\\filldraw[fill=black!14,line width=.8pt] ({x:.2f},{kz[i]*sy:.3f}) rectangle ({x+.7:.2f},{(kz[i]+er[i])*sy:.3f});'); o.append(tx(x+.35,(kz[i]+er[i]/2)*sy,f'\\footnotesize {er[i]}')); o.append(tx(x+.35,-.3,f'\\footnotesize {sn[i]}'))
o+=[f'\\filldraw[fill=vurgu!45] (3.8,2.3) rectangle (4.0,2.5);',tx(4.1,2.4,'Kız','anchor=west,font=\\footnotesize'),f'\\filldraw[fill=black!14] (3.8,1.9) rectangle (4.0,2.1);',tx(4.1,2.0,'Erkek','anchor=west,font=\\footnotesize')]
SK=fig('\n'.join(o))
q('0003',tipId='gfb-yigma',tip='Yığılmış sütun grafiğinde koşullu pay',z='orta',alt='Sütun Grafiği',kaz='Yığılmış sütun grafiğinden koşulu sağlayan sınıfları seçip erkek öğrencilerin toplam içindeki yüzdesini bulur.',kalip='grafik',sekil=SK,
 kart='K-GFB-03 (yığılmış sütun) · erkekler 12, 16, 12; kız çoğunluklu A ve C',
 metin='Bir okulda rehberlik servisi, aynı düzeydeki A, B ve C sınıflarındaki kız ve erkek öğrenci sayılarını yukarıdaki yığılmış sütun grafiğinde göstermiştir; her sütunun alt parçası kız, üst parçası erkek öğrencileri belirtir.\nBuna göre kız öğrencilerin erkek öğrencilerden fazla olduğu sınıflardaki erkek öğrenciler, bu üç sınıftaki tüm erkek öğrencilerin yüzde kaçıdır?',
 dogru=int(d3),yan=[(24,'Yüzdeye çevirmeyip erkek öğrenci sayısını (12 + 12) yazmış.','dikkat'),(30,'Yalnız bir sınıfın erkek öğrencilerinin payını (12/40) bulmuş.','dikkat'),(40,'Kız öğrencilerin az olduğu B sınıfının erkek payını (16/40) bulmuş.','dikkat'),(52,'Tüm kız öğrencilerin sayısını (18 + 14 + 20) yazmış.','dikkat')],
 istenen='Seçilen sınıflardaki erkek öğrencilerin, tüm erkek öğrencilere oranı (%).',
 ip=['Önce her sınıfta kız ve erkek sayısını karşılaştırıp koşulu sağlayan sınıfları belirle.'],
 bilgi=[YIG],
 ad=[A('Koşullu sınıflar','Kızların erkeklerden fazla olduğu sınıflar.','A: 18 > 12; C: 20 > 12'),A('Seçilen erkekler','O sınıflardaki erkekler toplanır.','12 + 12 = 24'),A('Tüm erkekler','Üç sınıfın erkekleri toplanır.','12 + 16 + 12 = 40'),A('Yüzde','Seçilenler tüm erkeklere bölünür.','24 ÷ 40 = %60')],
 puf='Önce hangi sınıflarda kız öğrenciler fazla, onu belirle; sonra yalnız o sınıfların erkeklerini ele al.')

# ---------- 04 hız–zaman grafiği ----------
pts=[(0,0),(1,40),(3,40),(4,0)]
yol=sum((pts[i+1][0]-pts[i][0])*(pts[i+1][1]+pts[i][1])/2 for i in range(3)); d4=Fr(int(yol),4); assert (yol,d4)==(120,30)
e4=[Fr(0+40,2),40,Fr(80),120]; assert e4==[20,40,80,120] and len({d4,*e4})==5
sx=1.0; sy=.045; o=eksen(4.6,52,sx,sy,range(0,5),range(0,41,20),xe='saat',ye='Hız (km/sa)')
o.append('\\draw[line width=1.8pt,vurgu] (0,0) -- (1,1.8) -- (3,1.8) -- (4,0);')
for x,y in pts[1:3]: o.append(f'\\fill[vurgu] ({x*sx},{y*sy}) circle (.07);')
o+=[ln(1,0,1,1.8,'dashed,black!40'),ln(3,0,3,1.8,'dashed,black!40')]
SK=fig('\n'.join(o))
q('0004',tipId='gfb-hiz',tip='Hız–zaman grafiğinde ortalama hız',z='orta',alt='Hız–Zaman Grafiği',kaz='Hız–zaman grafiğindeki şeklin alanından toplam yolu bulup toplam süreye bölerek ortalama hızı hesaplar.',kalip='grafik',sekil=SK,
 kart='K-GFB-04 (hız–zaman) · yamuk; yol 120 km, süre 4 saat',
 metin='Bir bisikletçi, düz ve engelsiz bir yolda duruştan hareket ederek antrenman yolculuğunu tamamlamış ve yolculuk sonunda tekrar durmuştur. Hızının zamana göre değişimi yukarıdaki grafikte gösterilmiştir; bisikletçi yolculuk boyunca yön değiştirmemiş, hız artarken ve azalırken değişim düzgün olmuştur.\nBuna göre bisikletçinin bu yolculuktaki ortalama hızı kaç km/sa’tir?',
 dogru=int(d4),yan=[(20,'Başlangıç ve en yüksek hızın ortalamasını almış: (0 + 40) ÷ 2.','dikkat'),(40,'En yüksek hızı ortalama hız sanmış.','dikkat'),(80,'Yalnız sabit hızlı bölümde alınan yolu (40 × 2) yazmış.','dikkat'),(120,'Toplam yolu süreye bölmeden yazmış.','dikkat')],
 istenen='Ortalama hız (km/sa).',
 ip=['Toplam yolu grafikten nasıl bulabilirsin?'],
 bilgi=[HIZ],
 ad=[A('Parçalar','Şekil iki üçgen ve bir dikdörtgendir.','sol üçgen: 1 × 40 ÷ 2 = 20; dikdörtgen: 2 × 40 = 80; sağ üçgen: 1 × 40 ÷ 2 = 20'),A('Toplam yol','Üç parçanın alanları toplanır.','20 + 80 + 20 = 120 km'),A('Toplam süre','Grafik 4 saatte biter.','4 saat'),A('Ortalama hız','Yol süreye bölünür.','120 ÷ 4 = 30')],
 puf='Ortalama hız için toplam yolu ve toplam süreyi grafikten çıkar; yolu süreye böl.')

# ---------- 05 birikimli çizgi ----------
cum=[20,50,70,110,140,150]; wk=[cum[0]]+[cum[i]-cum[i-1] for i in range(1,6)]; ort=Fr(sum(wk),6); assert (wk,ort)==([20,30,20,40,30,10],25)
d5=sum(w for w in wk if w>ort); assert d5==100
e5=[max(wk),sum(w for w in wk if w>ort and w!=40),cum[4],cum[5]]; assert e5==[40,60,140,150] and len({d5,*e5})==5
sx=.8; sy=.024; o=eksen(6.6,170,sx,sy,[],range(0,161,40),ye='Toplam ürün',xe='hafta')
for i in range(6): o.append(tx((i+1)*sx,-.3,f'\\footnotesize {i+1}'))
pp=[(0,0)]+[((i+1)*sx,v*sy) for i,v in enumerate(cum)]
o.append('\\draw[line width=1.6pt,vurgu] '+' -- '.join(f'({x:.2f},{y:.2f})' for x,y in pp)+';')
for (x,y),v in zip(pp[1:],cum): o.append(f'\\fill[vurgu] ({x:.2f},{y:.2f}) circle (.07);'); o.append(tx(x-.05,y+.28,f'\\footnotesize {v}'))
SK=fig('\n'.join(o))
q('0005',tipId='gfb-kumul',tip='Birikimli grafikte haftalık değer ve ortalama',z='orta',alt='Çizgi Grafiği',kaz='Birikimli grafikten haftalık satışları bulup ortalamadan fazla olan haftaların toplam satışını hesaplar.',kalip='grafik',sekil=SK,
 kart='K-GFB-05 (birikimli) · haftalık 20, 30, 20, 40, 30, 10; ortalama 25',
 metin='Bir mağazada yeni sezon kampanyası boyunca altı hafta satılan ürünlerin toplam sayısının haftalara göre birikimli değişimi yukarıdaki grafikte gösterilmiştir; her nokta, o haftanın sonuna kadar satılan toplam ürün sayısını göstermektedir.\nBuna göre haftalık satışı, altı haftalık haftalık satış ortalamasından fazla olan haftalarda satılan toplam ürün sayısı kaçtır?',
 dogru=d5,yan=[(40,'Haftalık satışların en büyüğünü (4. hafta) yazmış.','dikkat'),(60,'Ortalamanın üstündeki haftalardan 4. haftayı atlamış.','dikkat'),(140,'5. haftanın birikimli değerini yazmış.','dikkat'),(150,'Altı haftanın toplamını yazmış.','dikkat')],
 istenen='Ortalamadan fazla satış yapılan haftalardaki toplam ürün sayısı.',
 ip=['Noktalar toplamı gösterir; haftalık değerleri bulmak için ardışık noktalara bak.'],
 bilgi=[KUM],
 ad=[A('Haftalık satış','Ardışık birikimli değerlerin farkı alınır.','20; 30; 20; 40; 30; 10'),A('Ortalama','Toplam altı haftaya bölünür.','150 ÷ 6 = 25'),A('Koşullu haftalar','Satışı 25’ten fazla olan haftalar.','2. hafta 30; 4. hafta 40; 5. hafta 30'),A('Topla','Bu haftaların satışları toplanır.','30 + 40 + 30 = 100')],
 puf='Grafikteki değerler birikimlidir; her haftanın kendi satışı bir önceki noktayla farktır.')

# ---------- 06 gövde–yaprak ----------
gy={4:[3,6,8],5:[0,2,6,9],6:[1,4,5,6,9],7:[0,4,5,8],8:[4,6,9]}
vals=[10*g+y for g,l in gy.items() for y in l]; n=len(vals); mu=Fr(sum(vals),n); assert (n,mu)==(19,65)
d6=sum(1 for v in vals if abs(v-mu)>=10); assert d6==10
e6=[sum(1 for v in vals if abs(v-mu)>10),sum(1 for v in vals if abs(v-mu)>=5),sum(1 for v in vals if v!=mu),n]; assert e6==[9,14,18,19] and len({d6,*e6})==5
o=[tx(0,0,'\\textbf{Gövde}','anchor=east,font=\\footnotesize'),tx(.2,0,'\\textbf{Yaprak}','anchor=west,font=\\footnotesize')]
for i,(g,l) in enumerate(gy.items()):
    y=-.5*(i+1); o.append(tx(-.1,y,f'{g}','anchor=east')); o.append(tx(.2,y,' \\ '.join(str(v) for v in l),'anchor=west'))
o+=[ln(0,.25,0,-2.8,'line width=1pt'),tx(0,-3.3,'\\footnotesize 5 $|$ 2 → 52 puan','anchor=west')]
SK=fig('\n'.join(o))
q('0006',tipId='gfb-govde',tip='Gövde–yaprak diyagramında ortalama ve uzaklık',z='orta',alt='Gövde–Yaprak Diyagramı',kaz='Gövde–yaprak diyagramındaki puanlardan ortalamayı bulup ortalamadan belirli uzaklıktaki öğrenci sayısını hesaplar.',kalip='şekilli',sekil=SK,
 kart='K-GFB-06 (gövde–yaprak) · 19 puan; ortalama 65; |x − 65| ≥ 10 → 10 kişi',
 metin='Bir okulda yapılan matematik deneme sınavına giren 19 öğrencinin puanları, öğretmenin hazırladığı yukarıdaki gövde–yaprak diyagramında gösterilmiştir; diyagramdaki her yaprak bir öğrenciye aittir ve puanların hepsi tam sayıdır.\nBuna göre puanı, sınıf ortalamasından en az 10 puan farklı olan öğrenci sayısı kaçtır?',
 dogru=d6,yan=[(9,'“En az 10” ifadesini “10’dan fazla” okuyup tam 10 fark olan 75’i saymamış.','dikkat'),(14,'Ortalamadan en az 5 puan farklı olanları saymış.','dikkat'),(18,'Ortalamadan farklı puan alan tüm öğrencileri saymış.','dikkat'),(19,'Tüm öğrencileri saymış.','dikkat')],
 istenen='Ortalamadan en az 10 puan farklı puanı olan öğrenci sayısı.',
 ip=['Önce diyagramdaki puanların tamamını yazıp ortalamayı bul.'],
 bilgi=[GOV],
 ad=[A('Puanlar','Gövde ve yapraklardan 19 puan yazılır.','43 46 48 50 52 56 59 61 64 65 66 69 70 74 75 78 84 86 89'),A('Ortalama','Puanların toplamı öğrenci sayısına bölünür.','1235 ÷ 19 = 65'),A('Aralık','Ortalamadan en az 10 farklı olanlar 55 ve altı ile 75 ve üstüdür.','≤ 55 ve ≥ 75'),A('Say','Alt kısım 5, üst kısım 5 puandır.','5 + 5 = 10')],
 puf='“En az 10” ifadesinde 10 farkı da dâhildir; ortalamanın iki yanındaki sınırlara bak.')

# ---------- 07 parçalı doğrusal su tarifesi ----------
bp=[(0,0),(10,60),(20,150),(30,300)]; egim=[Fr(bp[i+1][1]-bp[i][1],bp[i+1][0]-bp[i][0]) for i in range(3)]; assert egim==[6,9,15]
F=240; d7=20+Fr(F-150,egim[2]); assert d7==26
e7=[20+Fr(F,egim[0]),20+Fr(F-150,egim[1]),20+Fr(F,egim[2]),Fr(F,egim[0])]; assert e7==[60,30,36,40] and len({d7,*e7})==5
sx=.14; sy=.0145; o=eksen(31,310,sx,sy,range(0,31,5),range(0,301,30),xe='m³',ye='Fatura (TL)')
o.append('\\draw[line width=1.8pt,vurgu] '+' -- '.join(f'({x*sx:.3f},{y*sy:.3f})' for x,y in bp)+';')
for x,y in bp[1:]: o.append(f'\\fill[vurgu] ({x*sx:.3f},{y*sy:.3f}) circle (.07);'); o+=[ln(x*sx,0,x*sx,y*sy,'dashed,black!35')]
SK=fig('\n'.join(o))
q('0007',tipId='gfb-tarife',tip='Parçalı doğrusal tarife grafiği',z='zor',alt='Doğrusal Grafik',kaz='Parçalı doğrusal tarife grafiğinden dilimlerin birim fiyatını bulup verilen fatura tutarına karşılık gelen tüketimi hesaplar.',kalip='grafik',sekil=SK,
 kart='K-GFB-07 (su tarifesi) · eğimler 6, 9, 15; fatura 240 TL',
 metin='Bir şehirde aylık su tüketimine göre ödenen fatura tutarı yukarıdaki grafikte gösterilmiştir; her tüketim diliminde birim fiyat sabittir ve grafik, aboneler için geçerli tüketim aralığını kapsamaktadır. Bir abone bir ay için 240 TL fatura ödemiştir.\nBuna göre bu abone o ay kaç m³ su tüketmiştir?',
 dogru=int(d7),yan=[(60,'20 m³’e, kalan 90 TL yerine tüm 240 TL’yi ilk dilimin fiyatına bölerek 40 m³ eklemiş.','dikkat'),(30,'Son dilimde kalan 90 TL’yi ikinci dilimin birim fiyatına (9 TL) bölüp 20 + 10 bulmuş.','dikkat'),(36,'İkinci dilimin sonuna 240 ÷ 15 = 16 m³ eklemiş.','dikkat'),(40,'Tüm tüketimi ilk dilimin birim fiyatıyla hesaplayıp 240 ÷ 6 bulmuş.','dikkat')],
 istenen='Tüketilen su miktarı (m³).',
 ip=['Her doğru parçasının eğimini bulup 240 TL’nin hangi dilimde kaldığına bak.'],
 bilgi=[TAR],
 ad=[A('Dilim fiyatları','Her parçanın eğimi birim fiyattır.','6; 9; 15 TL/m³'),A('Dilimi belirle','240 TL, 150 TL ile 300 TL arasındadır; son dilimdedir.','20 m³ → 150 TL'),A('Kalan tutar','Son dilimde ödenen kısım bulunur.','240 − 150 = 90 TL'),A('Son dilimde tüketim','Kalan tutar son dilimin birim fiyatına bölünür.','90 ÷ 15 = 6 m³'),A('Toplam','İlk 20 m³ ile eklenir.','20 + 6 = 26')],
 puf='240 TL hangi dilimde? Dilim başındaki tutarı çıkarıp yalnız o dilimin fiyatını kullan.')

# ---------- 08 ardışık yüzde değişimleri ----------
v0=800; ch=[20,-25,10]; vs=[Fr(v0)]
for c in ch: vs.append(vs[-1]*(100+c)/100)
assert vs==[800,960,720,792]
d8=vs[1]-vs[3]; assert d8==168
e8=[vs[1]-vs[2],Fr(v0*(100+sum(ch)),100)-vs[1],vs[3]-vs[2],v0-vs[3]]; assert [abs(x) for x in e8]==[240,120,72,8] and len({d8,*[abs(x) for x in e8]})==5
bw=.7; nm=['Ocak','Şubat','Mart','Nisan']; o=[ln(0,0,5.6,0,'line width=1.2pt')]
for i in range(4):
    x=.25+i*1.5; o.append(f'\\filldraw[fill=vurgu!45,line width=.8pt] ({x:.2f},0) rectangle ({x+bw:.2f},1.8);'); o.append(tx(x+bw/2,-.3,f'\\footnotesize {nm[i]}'))
    o.append(tx(x+bw/2,2.1,'\\footnotesize 800' if i==0 else f'\\scriptsize {"\\%"+str(abs(ch[i-1]))+(" artış" if ch[i-1]>0 else " azalış")}'))
SK=fig('\n'.join(o))
q('0008',tipId='gfb-yuzde',tip='Ardışık yüzde değişimleri grafiği',z='orta',alt='Sütun Grafiği',kaz='Her ayki değişimi bir önceki aya göre yüzde çarpanıyla uygulayıp iki ay arasındaki farkı hesaplar.',kalip='grafik',sekil=SK,
 kart='K-GFB-08 (ardışık yüzde) · 800 → 960 → 720 → 792',
 metin='Bir giyim mağazasının ocak ayında sattığı ürün sayısı ile sonraki üç ayda, her ayın satışının bir önceki aya göre yüzde değişimi yukarıdaki grafikte gösterilmiştir; sütunlar yalnız gösterim amaçlıdır, ölçeksizdir ve değişimler her ay yeni satış üzerinden uygulanmıştır.\nBuna göre nisan ayında satılan ürün sayısı, şubat ayında satılandan kaç eksiktir?',
 dogru=int(d8),yan=[(240,'Şubat ile mart arasındaki farkı (960 − 720) yazmış.','dikkat'),(120,'Yüzdeleri toplayıp (%+5) nisan satışını 840 bulmuş: 960 − 840.','dikkat'),(72,'Mart ile nisan arasındaki farkı (792 − 720) yazmış.','dikkat'),(8,'Ocak ile nisan arasındaki farkı (800 − 792) yazmış.','dikkat')],
 istenen='Şubat satışından nisan satışının eksik olduğu adet.',
 ip=['Her ayın satışını bir önceki ayın satışına göre yüzde değişimini kullanarak sırayla bul.'],
 bilgi=[YUZ],
 ad=[A('Çarpanlar','Artış 1 + p/100, azalış 1 − p/100 ile çarpılır.','1,20; 0,75; 1,10'),A('Şubat','Ocak satışı 1,20 ile çarpılır.','800 × 1,20 = 960'),A('Mart','Şubat satışı 0,75 ile çarpılır.','960 × 0,75 = 720'),A('Nisan','Mart satışı 1,10 ile çarpılır.','720 × 1,10 = 792'),A('Fark','Şubat’tan nisan çıkarılır.','960 − 792 = 168')],
 puf='Her yüzde değişim, bir önceki ayın satışına uygulanır; üç çarpma sırayla yapılır.')

# ---------- 09 gelir ve maliyet doğruları ----------
g_e=Fr(300,50); m_n=40; m_e=Fr(140-40,50); assert (g_e,m_e)==(6,2)
K=200; d9=Fr(K+m_n,g_e-m_e); assert d9==60 and 6*60-(40+2*60)==200
e9=[Fr(m_n,g_e-m_e),Fr(K+m_n,g_e),Fr(K,g_e-m_e),Fr(K+m_n,m_e)]; assert e9==[10,40,50,120] and len({d9,*e9})==5
sx=.085; sy=.0108; o=eksen(75,430,sx,sy,range(0,71,10),range(0,421,60),xe='ürün sayısı',ye='TL')
o.append(f'\\draw[line width=1.8pt,vurgu] (0,0) -- ({70*sx:.3f},{420*sy:.3f});'); o.append(f'\\draw[line width=1.8pt,dashed] (0,{40*sy:.3f}) -- ({70*sx:.3f},{180*sy:.3f});')
o+=[f'\\fill[vurgu] ({50*sx:.3f},{300*sy:.3f}) circle (.07);',tx(50*sx-.2,300*sy+.25,'\\footnotesize (50, 300)','anchor=east'),f'\\fill ({0},{40*sy:.3f}) circle (.07);',tx(.25,2.0,'\\footnotesize (0, 40)','anchor=west'),ln(.35,1.8,.05,.5,'black!60'),f'\\fill ({50*sx:.3f},{140*sy:.3f}) circle (.07);',tx(50*sx,140*sy-.3,'\\footnotesize (50, 140)','anchor=north'),
 ln(5.3,2.5,5.7,2.5,'line width=1.8pt,vurgu'),tx(5.8,2.5,'Gelir','anchor=west,font=\\footnotesize'),ln(5.3,2.05,5.7,2.05,'line width=1.8pt,dashed'),tx(5.8,2.05,'Maliyet','anchor=west,font=\\footnotesize')]
SK=fig('\n'.join(o))
q('0009',tipId='gfb-dogru',tip='Gelir ve maliyet doğrularında kâr',z='zor',alt='Doğrusal Grafik',kaz='Grafikteki iki noktadan gelir ve maliyet doğrularını yazıp kâr eşitliğinden ürün sayısını bulur.',kalip='grafik',sekil=SK,
 kart='K-GFB-09 (gelir–maliyet) · y = 6x ve y = 40 + 2x; kâr 200 → 60',
 metin='Küçük bir atölyede üretilen ve tamamı satılan ürünlerin gelirinin ve toplam maliyetinin, ürün sayısına göre değişimi yukarıdaki doğrusal grafiklerde gösterilmiştir; maliyet, üretime başlamadan önceki sabit gideri de içermektedir. Kâr, gelirden toplam maliyetin çıkarılmasıyla bulunur.\nBuna göre atölyenin 200 TL kâr elde etmesi için kaç ürün satması gerekir?',
 dogru=int(d9),yan=[(10,'Kârın sıfır olduğu (başa baş) ürün sayısını bulmuş.','dikkat'),(40,'Sabit gideri çıkarıp maliyetin değişken kısmını atlamış: 6x − 40 = 200.','dikkat'),(50,'Sabit gideri unutup 6x − 2x = 200 yazmış.','dikkat'),(120,'Farkı gelirin eğimi yerine maliyetin eğimine (2) bölmüş: 240 ÷ 2.','dikkat')],
 istenen='Kârın 200 TL olması için satılması gereken ürün sayısı.',
 ip=['Her doğrunun eğimini ve y eksenini kestiği noktayı grafikteki noktalardan bul.'],
 bilgi=[DOG],
 ad=[A('Gelir doğrusu','Orijinden geçer; (50, 300) noktasından eğim bulunur.','300 ÷ 50 = 6 → y = 6x'),A('Maliyet doğrusu','(0, 40) ve (50, 140) noktalarından.','eğim (140 − 40) ÷ 50 = 2 → y = 2x + 40'),A('Kâr','Gelirden maliyet çıkarılır.','6x − (2x + 40) = 4x − 40'),A('Denklem','Kâr 200 TL olarak yazılır.','4x − 40 = 200'),A('Çöz','Denklem düzenlenir.','4x = 240 → x = 60')],
 puf='Önce iki doğrunun denklemini yaz; kâr = gelir − maliyet ifadesini 200’e eşitle.')

# ---------- 10 tren tarife tablosu ----------
def dk(s): h,m=s.split(':'); return int(h)*60+int(m)
st=[('Eskişehir',None,'08:00',0),('Bilecik','09:00','09:15',100),('Sapanca','11:15','11:30',260),('İstanbul','12:30',None,360)]
hareket=sum(dk(st[i+1][1])-dk(st[i][2]) for i in range(3)); assert hareket==240
d10=Fr(st[3][3]*60,hareket); assert d10==90
e10=[Fr(100*60,dk('09:00')-dk('08:00')),Fr(st[3][3]*60,(dk('09:00')-dk('08:00'))+(dk('11:15')-dk('09:15'))),st[2][3]-st[1][3],st[3][3]]; assert e10==[100,120,160,360] and len({d10,*e10})==5
SK=tablo_svg(['İstasyon','Varış','Kalkış','Uzaklık (km)'],[[n,a or '–',k or '–',str(u)] for n,a,k,u in st])
q('0010',tipId='gfb-tren',tip='Tarife tablosunda hareket hâlindeki ortalama hız',z='orta',alt='Tablo',kaz='Tarife tablosundan hareket süresini ve toplam yolu bulup hareket hâlindeki ortalama hızı hesaplar.',kalip='tablo',sekil=SK,
 kart='K-GFB-10 (tren tarifesi) · 360 km; hareket 240 dk; 90 km/sa',
 metin='Bir yolcu treninin Eskişehir’den İstanbul’a yaptığı bir seferine ait tarife tablosu yukarıda verilmiştir; uzaklık, trenin Eskişehir’den ayrıldığı noktadan itibaren alınan yoldur ve tren duraklarda beklediği sürelerde yol almamaktadır.\nBuna göre bu tren, yalnız hareket hâlinde olduğu süreler dikkate alınırsa ortalama kaç km/sa hızla gitmiştir?',
 dogru=int(d10),yan=[(100,'İlk bölümün ortalama hızını (100 ÷ 1) yazmış.','dikkat'),(120,'Son bölümü unutup hareket süresini 3 saat bulmuş: 360 ÷ 3.','dikkat'),(160,'Orta bölümün yolunu yazmış.','dikkat'),(360,'Toplam yolu süreye bölmeden yazmış.','dikkat')],
 istenen='Hareket hâlindeki ortalama hız (km/sa).',
 ip=['Duraklardaki bekleme sürelerinin yol almadığına dikkat ederek her bölümün süresini ayrı bul.'],
 bilgi=[HZ2],
 ad=[A('Tabloyu oku','Her bölümün kalkış ve varış saatleri.','08:00 → 09:00; 09:15 → 11:15; 11:30 → 12:30'),A('Bölüm süreleri','Varıştan kalkış çıkarılır.','60; 120; 60 dk'),A('Hareket süresi','Bölüm süreleri toplanır.','240 dk = 4 saat'),A('Toplam yol','Son satırdaki uzaklık.','360 km'),A('Ortalama hız','Yol hareket süresine bölünür.','360 ÷ 4 = 90')],
 puf='Bekleme sürelerini yolculuk süresine katma; yalnız her bölümün hareket süresini topla.')

bitir(P,'grafsekb','prob|Grafik Problemleri')
