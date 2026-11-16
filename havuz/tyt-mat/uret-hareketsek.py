"""Hareket Hız Problemleri · ŞEKİLLİ paket (10 soru): şekil/tablo/grafik çözüm verisini taşır; sayılar Python'da hesaplanır, her doğru ve çeldirici değer assert'lidir. Kardeş yok, ipucu 1."""
import sys,os,math
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
from math import cos,sin,radians
H.KONU='Hareket Hız Problemleri'
UK='prob|Hareket Hız Problemleri'
P=Parti('hareketsek','Hareket Hız Problemleri',UK)
KY='ÖSYM 2018–2026 TYT Matematik (şekilli/tablolu/grafikli hareket soruları; yalnız mantık) · MEB 9. sınıf problemler'
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)
def fig(body): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'+body+'\n\\end{tikzpicture}')
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)

KARS=B('Karşılaşmaya kadar aynı süre','aynı anda birbirine doğru yola çıkan iki hareketli karşılaşana kadar aynı süre yol alır; bu yüzden aldıkları yollar hızlarıyla doğru orantılıdır. Örnek: karşılaşana kadar biri 20 km, öbürü 30 km gittiyse hızları 2:3 oranındadır')
KON=B('Konum–zaman grafiği','yatay parça duruşu gösterir; bir parçadaki hız = konum değişimi ÷ geçen süre; ortalama hız = ilgili yol ÷ ilgili süre. Örnek: 2 saatte konumu 50 km artan araç saatte 25 km hızla gitmiştir')
HZ=B('Hız–zaman grafiği','grafikle zaman ekseni arasında kalan alan alınan yolu verir; sabit hızlı bölümde alan dikdörtgendir. Örnek: saatte 8 km hızla 3 saat giden 8 × 3 = 24 km yol alır')
PIS=B('Dairesel pistte aynı yön','aynı yönde giden iki hareketliden hızlısı, yavaşa her saniye hız farkı kadar yaklaşır; art arda iki yan yana gelme arasında hızlı, yavaştan tam bir tur fazla gider. Örnek: çevre 300 m, hızlar 4 ve 1 m/sn ise yan yana gelmeler arası 300 ÷ 3 = 100 sn')
YET=B('Sonradan çıkanın yetişmesi','geç çıkan aracın çıkış anında öndeki araç, o ana kadar gittiği yol kadar öndedir; yetişme süresi = bu yol ÷ hız farkı. Örnek: 45 km/sa hızlı araç 3 saat önde; 75 km/sa ile arkadan çıkan araç 135 ÷ 30 = 4,5 saatte yetişir')
TUN=B('Tren ve tünel','tren tamamen tünelin içindeyken ön ucu çıkışa varana kadar aldığı yol tünel boyu − tren boyudur. km/sa değeri 3,6’ya bölünerek m/sn’ye çevrilir. Örnek: tren 30 m, tünel 100 m, hız 10 m/sn ise tren (100 − 30) ÷ 10 = 7 sn tamamen içindedir')

TAR=B('Tarife tablosu','varış ile kalkış saatinin farkı yolculuk süresidir; yol = hız × süre; aynı yol için süre hızla ters orantılıdır. Örnek: aynı yolu 40 km/sa hızla 3 saatte alan araç, 60 km/sa hızla 2 saatte alır')
AKI=B('Akıntılı nehir','akıntı yönünde hız = tekne + akıntı; akıntıya karşı hız = tekne − akıntı; akıntıyla sürüklenen cismin hızı akıntı hızına eşittir. Örnek: durgun suda 15 km/sa, akıntı 3 km/sa ise gidiş 18, dönüş 12 km/sa')
IKI=B('Uçlardan dönen iki hareketli','karşı uçlardan aynı anda çıkıp uçlarda beklemeden dönen iki hareketli ilk karşılaşmada toplam bir yol uzunluğu, sonraki her karşılaşmada toplam iki yol uzunluğu daha alır. Örnek: ilk karşılaşmada toplam 100 m ise ikinci karşılaşmada toplam 300 m almışlardır')

# ---------- kartlar ----------
kartla('K-HRS-01','Karşılaşma noktalı yol şeması','Aynı anda çıkan araçlar karşılaşana kadar aynı süre gittiğinden, şemadaki iki yol parçası hızlarla orantılıdır; bilinen hızdan bilinmeyen hız bulunur.','Hızları ters orantılı sanmak; yol parçasını hız sanmak.','kolay','hikâyeli',3,'hrs-yol','Karşılaşma noktalı yol şeması')
kartla('K-HRS-02','Molalı konum–zaman grafiği','Grafikteki yatay parça molayı gösterir; hareket süresi ve toplam yol ayrı ayrı okunarak ortalama hız hesaplanır.','Molayı süreye katmak; hızların ortalamasını almak.','kolay','grafik',3,'hrs-konum','Konum–zaman grafiği ve ortalama hız')
kartla('K-HRS-03','Basamaklı hız–zaman grafiği','Hız–zaman grafiğinde her basamağın alanı o bölümde alınan yoldur; alanlar toplanır.','En büyük hızı tüm süreye uygulamak; süreleri karıştırmak.','kolay','grafik',3,'hrs-hizzaman','Hız–zaman grafiğinde alan')
kartla('K-HRS-04','Dairesel pist ve yay uzunluğu','Pistteki yay uzunluğu ilk yetişmeyi, çevre ise ardışık yan yana gelmeler arası farkı verir; süreler hız farkıyla hesaplanır.','Diğer yayı kullanmak; ilk yetişmeyi son cevap sanmak.','orta','hikâyeli',4,'hrs-pist','Dairesel pistte tekrarlı yan yana gelme')
kartla('K-HRS-05','Farklı zamanda çıkan araçların grafiği','Grafikteki çıkış zamanlarından ve uç noktalardan hızlar bulunur; geç çıkanın yetişme süresi ve yol hesaplanır.','Yetişme yolunu ilk aracın yoluyla karıştırmak; çıkış gecikmesini unutmak.','orta','grafik',5,'hrs-yetisme','Konum–zaman grafiğiyle yetişme')
kartla('K-HRS-06','Tren ve tünel çizimi','Trenin tünelde tamamen içinde kaldığı sürede alınan yol, tünel boyundan tren boyunun farkıdır; hız birimi dönüştürülür.','Geçiş yolunu (toplam) kullanmak; km/sa–m/sn dönüşümünü yanlış yapmak.','orta','hikâyeli',3,'hrs-tunel','Tünelde tamamen kalma süresi')
kartla('K-HRS-07','Üç iskeleli nehir yolculuğu','Akıntı yönündeki bölümde hız tekne + akıntı, karşıt bölümde tekne − akıntıdır; her bölümün süresi ayrı hesaplanıp toplanır.','Dönüşte de akıntı yönünü kullanmak; dönüş uzunluğunu yanlış almak.','orta','hikâyeli',4,'hrs-nehir2','Üç iskeleli nehir yolculuğu')
kartla('K-HRS-08','Sefer tarifesi tablosu','Birinci seferin kalkış–varış saatlerinden süre, süre ve hızdan yol bulunur; yol ikinci seferin hızına bölünür.','Süreyi hız oranına ters ya da doğru yanlış kurmak; saat–dakika dönüşümünü karıştırmak.','orta','tablo',4,'hrs-tablo','Tarife tablosu ve süre')
kartla('K-HRS-09','Akıntıda sürüklenen tahta','Tahtanın yol süresi akıntı hızını verir; kayığın gidiş süresinden durgun su hızı ve dönüş süresi hesaplanır.','Akıntıyı dönüşte bir kez çıkarmak; durgun su hızını gidiş hızı sanmak.','zor','hikâyeli',5,'hrs-nehir','Akıntı ve sürüklenen cisim')
kartla('K-HRS-10','İkinci karşılaşma','İlk karşılaşmada toplam bir, ikincisinde toplam üç yol uzunluğu alınır; sürenin üç katı kullanılarak konum bulunur.','İkinci karşılaşmayı ilk sanmak; konumu karşı uçtan ölçmek.','zor','hikâyeli',4,'hrs-ikinci','İkinci karşılaşma noktası')

# ================= 01 kolay · yol şeması, karşılaşma noktası =================
AM,MB,vA=180,120,72; t=Fr(AM,vA); v=Fr(MB)/t
e=[vA-(AM-MB),Fr(vA*AM,MB),Fr(MB),t]
assert t==Fr(5,2) and v==48 and e==[12,108,120,Fr(5,2)] and len({v,*e})==5
k=0.025; o=[]
o.append(f'\\draw[very thick] (0,0) -- ({(AM+MB)*k},0);')
for x,nm in ((0,'A'),(AM*k,'M'),((AM+MB)*k,'B')): o.append(f'\\fill ({x},0) circle (0.08); \\node[below=4pt] at ({x},0) {{{nm}}};')
o.append(f'\\filldraw[fill=vurgu!30] (0.1,0.12) rectangle (0.9,0.5); \\draw[-{{Stealth}},thick] (0.95,0.31) -- (1.7,0.31); \\node[above] at (0.9,0.55) {{{vA} km/sa}};')
o.append(f'\\filldraw[fill=gray!25] ({(AM+MB)*k-0.9},0.12) rectangle ({(AM+MB)*k-0.1},0.5); \\draw[-{{Stealth}},thick] ({(AM+MB)*k-0.95},0.31) -- ({(AM+MB)*k-1.7},0.31);')
o.append(f'\\draw[<->] (0,-0.95) -- ({AM*k},-0.95) node[midway,below] {{{AM} km}}; \\draw[<->] ({AM*k},-0.95) -- ({(AM+MB)*k},-0.95) node[midway,below] {{{MB} km}};')
SK=fig('\n'.join(o))
q('0001',tipId='hrs-yol',tip='Karşılaşma noktalı yol şeması',z='kolay',alt='Karşılaşma Noktası',kaz='Karşılaşma noktasına kadar alınan yollardan bilinmeyen aracın hızını bulur.',kalip='hikâyeli',
 kart='K-HRS-01 (yol şeması) · AM=180, MB=120, v=72',
 metin='Şekilde A ve B kentleri arasındaki düz bir yol ile yol üzerindeki M noktası gösterilmiştir. İki tır, aynı anda A ve B kentlerinden birbirine doğru yola çıkmış ve M noktasında karşılaşmıştır. Tırlar yol boyunca sabit hızla gitmiştir ve A’dan çıkan tırın hızı şekilde verilmiştir.\nBuna göre, B’den çıkan tırın hızı saatte kaç km’dir?',
 dogru=v,yan=[(e[0],'Toplamsal düşünmüş: yol farkı 60 km olduğundan hızı da 60 azaltmış: 72 − 60.','dikkat'),(e[1],'Hızları ters orantılı sanmış: 72 × 180 ÷ 120.','dikkat'),(e[2],'B’nin aldığı yol uzunluğunu (120 km) hız olarak yazmış.','dikkat'),(e[3],'Karşılaşma süresini (2,5 saat) hız sanmış.','dikkat')],
 istenen='B’den çıkan tırın hızı (km/sa).',ip=['Şekilde A’dan çıkan tırın karşılaşana kadar aldığı yolu ve hızını kullanarak karşılaşma süresini düşün.'],bilgi=[KARS],sekil=SK,
 ad=[A('Süreyi bul','A’dan çıkan tır 180 km’yi 72 km/sa hızla alır.','180 ÷ 72 = 2,5 saat'),A('B’nin yolu','Şekilde M ile B arası okunur.','120 km'),A('Hızı bul','B’den çıkan tır aynı sürede bu yolu alır.','120 ÷ 2,5 = 48 km/sa')],
 puf='Karşılaşana kadar iki araç da aynı süre gider; önce o süreyi bul.')

# ================= 02 kolay · konum–zaman, mola =================
pts=[(0,0),(1,60),(2,60),(5,300)]; hareket=1+3; yol=300; v=Fr(yol,hareket)
e=[Fr(yol,5),Fr(60+80,2),Fr(80),Fr(yol,3)]
assert (300-60)/3==80 and v==75 and e==[60,70,80,100] and len({v,*e})==5
sx,sy=0.8,0.0115
o=[f'\\draw[-{{Stealth}}] (0,0) -- ({5.7*sx:.2f},0) node[right] {{Zaman (saat)}};',f'\\draw[-{{Stealth}}] (0,0) -- (0,{330*sy:.2f}) node[above] {{Konum (km)}};']
for kx in range(1,6): o.append(f'\\draw ({kx*sx:.2f},-0.06) -- ({kx*sx:.2f},0.06); \\node[below=2pt] at ({kx*sx:.2f},0) {{\\footnotesize {kx}}};')
for ty in (60,120,180,240,300): o.append(f'\\draw[gray!40] (0,{ty*sy:.2f}) -- ({5*sx:.2f},{ty*sy:.2f}); \\node[left=2pt] at (0,{ty*sy:.2f}) {{\\footnotesize {ty}}};')
o.append('\\draw[very thick] '+' -- '.join(f'({x*sx:.2f},{y*sy:.3f})' for x,y in pts)+';')
for x,y in pts[1:]: o.append(f'\\fill ({x*sx:.2f},{y*sy:.3f}) circle (0.07);')
SK=fig('\n'.join(o))
q('0002',tipId='hrs-konum',tip='Konum–zaman grafiği ve ortalama hız',z='kolay',alt='Konum–Zaman Grafiği',kaz='Molalı konum–zaman grafiğinden hareket süresini ve yolu okuyup ortalama hızı bulur.',kalip='grafik',
 kart='K-HRS-02 (konum–zaman) · 1 sa 60 km, mola 1 sa, 3 sa 240 km',
 metin='Şekildeki grafik, bir kuryenin motosikletle yaptığı teslimat yolculuğunda, yola çıktığı andan itibaren geçen süre ile başlangıç noktasına olan uzaklığını göstermektedir. Kurye yolculuğunda bir kez mola vermiştir ve hareket hâlindeyken her bölümde sabit hızla gitmiştir.\nBuna göre, kuryenin mola süresi hariç, hareket hâlindeyken ortalama hızı saatte kaç km’dir?',
 dogru=v,yan=[(e[0],'Molayı da sürenin içine katmış: 300 ÷ 5.','dikkat'),(e[1],'Bölümlerin hızlarını (60 ve 80) toplayıp ikiye bölmüş.','dikkat'),(e[2],'Yalnız son bölümün hızını yazmış.','dikkat'),(e[3],'Hareket süresini 5 − 2 = 3 saat almış: 300 ÷ 3.','dikkat')],
 istenen='Hareket hâlindeki ortalama hız (km/sa).',ip=['Grafikte yatay kalan parçanın ne anlama geldiğini düşün; hareket hâlinde geçen süreleri ayrı ayrı belirle.'],bilgi=[KON],sekil=SK,
 ad=[A('Hareket süresi','Grafikte yatay parça molayı gösterir; mola süresi toplamdan çıkarılır.','5 − 1 = 4 saat (1 saat + 3 saat)'),A('Toplam yol','Grafiğin son noktası okunur.','300 km'),A('Ortalama hız','Toplam yol ÷ hareket süresi.','300 ÷ 4 = 75 km/sa')],
 puf='Ortalama hız = toplam yol ÷ yalnız hareket edilen süre.')

# ================= 03 kolay · hız–zaman, basamaklar =================
b1,b2=(2,40),(3,60); v=b1[0]*b1[1]+b2[0]*b2[1]
e=[b1[0]*b1[1],b2[0]*b2[1],b1[1]*b2[0]+b2[1]*b1[0],b1[1]*b1[0]+b2[1]*b1[0]]
assert v==260 and e==[80,180,240,200] and len({v,*e})==5
sx,sy=0.9,0.042
o=[f'\\draw[-{{Stealth}}] (0,0) -- ({5.8*sx:.2f},0) node[right] {{Zaman (saat)}};',f'\\draw[-{{Stealth}}] (0,0) -- (0,{72*sy:.2f}) node[above] {{Hız (km/sa)}};']
o.append(f'\\filldraw[fill=vurgu!20,draw=black,thick] (0,0) rectangle ({2*sx:.2f},{40*sy:.2f}); \\filldraw[fill=vurgu!20,draw=black,thick] ({2*sx:.2f},0) rectangle ({5*sx:.2f},{60*sy:.2f});')
for kx in range(1,6): o.append(f'\\draw ({kx*sx:.2f},-0.06) -- ({kx*sx:.2f},0.06); \\node[below=2pt] at ({kx*sx:.2f},0) {{\\footnotesize {kx}}};')
for ty in (20,40,60): o.append(f'\\draw (-0.06,{ty*sy:.2f}) -- (0.06,{ty*sy:.2f}); \\node[left=2pt] at (0,{ty*sy:.2f}) {{\\footnotesize {ty}}};')
SK=fig('\n'.join(o))
q('0003',tipId='hrs-hizzaman',tip='Hız–zaman grafiğinde alan',z='kolay',alt='Hız–Zaman Grafiği',kaz='Basamaklı hız–zaman grafiğinde alanları toplayarak alınan yolu bulur.',kalip='grafik',
 kart='K-HRS-03 (hız–zaman) · 2 sa × 40 + 3 sa × 60',
 metin='Şekildeki grafik, bir servis aracının yolculuğu boyunca hızının zamanla değişimini göstermektedir. Araç yolculuk boyunca düz bir yolda aynı yönde gitmiş, hiç durmamış ve her bölümde sabit hızla ilerlemiştir.\nBuna göre, araç bu yolculukta toplam kaç km yol almıştır?',
 dogru=v,yan=[(e[0],'Yalnız ilk bölümün yolunu hesaplamış: 40 × 2.','dikkat'),(e[1],'Yalnız ikinci bölümün yolunu hesaplamış: 60 × 3.','dikkat'),(e[2],'Süreleri birbiriyle değiştirmiş: 40 × 3 + 60 × 2.','dikkat'),(e[3],'İkinci bölümün süresini 2 saat almış: 40 × 2 + 60 × 2.','dikkat')],
 istenen='Toplam yol (km).',ip=['Grafikte hızın sabit kaldığı bölümleri ayrı ayrı ele al; her bölümde süreyi şekilden oku.'],bilgi=[HZ],sekil=SK,
 ad=[A('1. bölüm','Hız ve süre okunur.','40 × 2 = 80 km'),A('2. bölüm','Hız ve süre okunur.','60 × 3 = 180 km'),A('Toplam','Yollar toplanır.','80 + 180 = 260 km')],
 puf='Her sabit hızlı bölümün yolu = hız × o bölümün süresi.')

# ================= 04 orta · dairesel pist =================
C_,gap,vk,vl=800,200,5,3; t1=Fr(gap,vk-vl); v=t1+Fr(C_,vk-vl)
e=[t1,Fr(gap+C_,Fr(vk+vl,2)),Fr(C_-gap,vk-vl),Fr(C_,vk-vl)]
assert t1==100 and v==500 and e==[100,250,300,400] and len({v,*e})==5
R=1.5; o=[f'\\draw[thick] (0,0) circle ({R});']
o.append(f'\\draw[line width=2.4pt,vurgu] ({R*cos(radians(270)):.3f},{R*sin(radians(270)):.3f}) arc[start angle=270,end angle=360,radius={R}];')
o.append(f'\\fill ({R*cos(radians(270)):.3f},{R*sin(radians(270)):.3f}) circle (0.08); \\node[below] at (0,{-R-0.05}) {{K}};')
o.append(f'\\fill ({R},0) circle (0.08); \\node[right=3pt] at ({R},0) {{L}};')
o.append(f'\\node[anchor=north west] at ({R*0.7+0.12:.2f},{-R*0.7-0.1:.2f}) {{{gap} m}};')
o.append(f'\\node[align=center] at (0,0) {{Pist çevresi\\\\{C_} m}};')
a=130; o.append(f'\\draw[-{{Stealth[length=9pt,width=7pt]}},very thick] ({R*cos(radians(a-22)):.3f},{R*sin(radians(a-22)):.3f}) arc[start angle={a-22},end angle={a+6},radius={R}];')
SK=fig('\n'.join(o))
q('0004',tipId='hrs-pist',tip='Dairesel pistte tekrarlı yan yana gelme',z='orta',alt='Dairesel Pist',kaz='Dairesel pistte yay uzunluğu ve çevre bilgisiyle ikinci yan yana gelme süresini bulur.',kalip='hikâyeli',
 kart='K-HRS-04 (pist) · yay 200 m, çevre 800 m, hızlar 5 ve 3',
 metin='Şekilde, bir koşu pistinin çevresi ile pist üzerindeki K ve L noktaları arasındaki yay uzunluğu (koşu yönünde K’dan L’ye) gösterilmiştir. Ayşe K noktasından sabit 5 m/sn, Bora L noktasından sabit 3 m/sn hızla, aynı anda ve şekilde okla gösterilen yönde koşmaya başlıyor.\nBuna göre, Ayşe ile Bora koşmaya başladıktan kaç saniye sonra ikinci kez yan yana gelir?',
 dogru=v,yan=[(e[0],'İlk yan yana gelme süresini (100 sn) cevap sanmış.','dikkat'),(e[1],'Hız farkı yerine hızların ortalamasını (4 m/sn) kullanmış: (200 + 800) ÷ 4.','dikkat'),(e[2],'Ayşe’nin Bora’ya diğer yaydan yetişeceğini sanmış: (800 − 200) ÷ 2.','dikkat'),(e[3],'Yalnız bir turluk farkı hesaplamış: 800 ÷ 2.','dikkat')],
 istenen='İkinci kez yan yana gelme süresi (sn).',ip=['Şekildeki oka göre Ayşe’nin Bora’ya ilk yetişmesi için kapatması gereken yolu belirle.'],bilgi=[PIS],sekil=SK,
 ad=[A('Aradaki yay','Koşu yönünde Ayşe, Bora’nın 200 m gerisindedir.','200 m'),A('İlk yetişme','Yol, hız farkına bölünür.','200 ÷ (5 − 3) = 100 sn'),A('Sonraki yetişme','Ayşe, Bora’dan bir tur fazla koşmalıdır.','800 ÷ 2 = 400 sn'),A('Toplam süre','İki süre toplanır.','100 + 400 = 500 sn')],
 puf='İlk yetişmeden sonra her yan yana gelme arasında hızlı koşucu bir tur fazla koşar.')

# ================= 05 orta · yetişme (şematik konum–zaman) =================
v1,t2,y2e,x2e,y1e,x1e=60,Fr(3,2),250,4,300,5
v2=Fr(y2e,x2e-t2); assert v2==100
gap2=v1*t2; ts=gap2/(v2-v1); v=v2*ts
e=[gap2,v1*ts,Fr(y2e),v2*(ts+t2)]
assert gap2==90 and ts==Fr(9,4) and v==225 and e==[90,135,250,375] and len({v,*e})==5
o=['\\draw[-{Stealth}] (0,0) -- (5.2,0) node[right] {Zaman (saat)};','\\draw[-{Stealth}] (0,0) -- (0,4.0) node[above] {A’ya uzaklık (km)};']
px={1.5:1.0,4:3.4,5:4.4}; py={250:2.9,300:3.5}
x1p,y1p=px[5],py[300]; x2p,y2p=px[4],py[250]
o.append(f'\\draw[very thick] (0,0) -- ({x1p},{y1p}) node[right] {{1. araç}};')
o.append(f'\\draw[very thick,dashed] ({px[1.5]},0) -- ({x2p},{y2p}) node[above=6pt] {{2. araç}};')
for xv,pxv in px.items(): o.append(f'\\draw ({pxv},-0.06) -- ({pxv},0.06); \\node[below=2pt] at ({pxv},0) {{\\footnotesize {str(xv).replace(".",",")}}};')
for yv,pyv in py.items(): o.append(f'\\draw (-0.06,{pyv}) -- (0.06,{pyv}); \\node[left=2pt] at (0,{pyv}) {{\\footnotesize {yv}}};')
o.append(f'\\draw[dotted] ({x1p},0) -- ({x1p},{y1p}) -- (0,{y1p}); \\draw[dotted] ({x2p},0) -- ({x2p},{y2p}) -- (0,{y2p});')
o.append(f'\\fill ({x1p},{y1p}) circle (0.07); \\fill ({x2p},{y2p}) circle (0.07);')
SK=fig('\n'.join(o))
q('0005',tipId='hrs-yetisme',tip='Konum–zaman grafiğiyle yetişme',z='orta',alt='Yetişme Grafiği',kaz='İki aracın konum–zaman grafiğindeki uç noktalardan hızlarını bulup yetişme noktasını hesaplar.',kalip='grafik',
 kart='K-HRS-05 (yetişme grafiği) · v1=60 (5 sa, 300), v2=100 (1,5 sa çıkış; 4 sa, 250)',
 metin='Şekilde, A kentinden aynı yolda aynı yönde giden iki aracın A’ya uzaklıklarının zamanla değişimi gösterilmiştir (şekil ölçekli çizilmemiştir). İkinci araç, birinci araçtan sonra yola çıkmış, ikisi de sabit hızla gitmiş ve ikinci araç birinci araca yolda yetişmiştir.\nBuna göre, ikinci araç birinci araca A kentinden kaç km uzaklıkta yetişmiştir?',
 dogru=v,yan=[(e[0],'İkinci araç yola çıkarken birinci aracın A’dan uzaklığını (90 km) cevap sanmış.','dikkat'),(e[1],'Yetişme süresini (2,25 saat) bulup birinci aracın yolunu bu süreyle hesaplamış: 60 × 2,25 (ön mesafeyi eklememiş).','dikkat'),(e[2],'İkinci aracın grafikteki son konumunu (250 km) yetişme noktası sanmış.','dikkat'),(e[3],'İkinci aracın hızını 2,25 + 1,5 = 3,75 saatle çarpmış (çıkış gecikmesini sürenin içine katmış).','dikkat')],
 istenen='Yetişme noktasının A’ya uzaklığı (km).',ip=['Grafikteki uç noktalardan her aracın hızını bul; ikinci araç çıkarken birinci aracın ne kadar önde olduğunu düşün.'],bilgi=[YET],sekil=SK,
 ad=[A('Birinci aracın hızı','Uç noktasından okunur.','300 ÷ 5 = 60 km/sa'),A('İkinci aracın hızı','Çıkışı 1,5. saatte; 4. saatte 250 km’dedir.','250 ÷ (4 − 1,5) = 100 km/sa'),A('Ön mesafe','İkinci araç çıkarken birinci araç.','60 × 1,5 = 90 km'),A('Yetişme süresi','Ön mesafe ÷ hız farkı.','90 ÷ (100 − 60) = 2,25 saat'),A('Yetişme noktası','İkinci aracın aldığı yol.','100 × 2,25 = 225 km')],
 puf='Önce iki hızı bul; sonra ikinci araç çıkarken aradaki mesafeyi hız farkına böl.')

# ================= 06 orta · tren ve tünel =================
Lt,Ltn,vk=200,700,90; vm=Fr(vk*1000,3600); v=Fr(Ltn-Lt)/vm
e=[Fr(Ltn+Lt)/vm,Fr(Ltn)/vm,Fr(Lt)/vm,Fr(Ltn+2*Lt)/vm]
assert vm==25 and v==20 and e==[36,28,8,44] and len({v,*e})==5
sc=0.0095; o=[]
o.append(f'\\fill[gray!30] (0,0.9) -- (0.4,1.9) -- ({Ltn*sc-0.4:.2f},1.9) -- ({Ltn*sc:.2f},0.9) -- cycle;')
o.append(f'\\draw[very thick] (0,0) -- (0,0.9) -- ({Ltn*sc:.2f},0.9) -- ({Ltn*sc:.2f},0);')
o.append(f'\\draw[very thick] (-2.9,0) -- ({Ltn*sc+0.5:.2f},0);')
x0=-0.3-Lt*sc
for i in range(4): o.append(f'\\filldraw[fill=vurgu!30,draw=black,thick] ({x0+i*Lt*sc/4:.2f},0.05) rectangle ({x0+(i+1)*Lt*sc/4-0.04:.2f},0.6);')
o.append(f'\\draw[-{{Stealth}},thick] ({x0+0.1:.2f},-0.4) -- ({x0+1.5:.2f},-0.4);')
o.append(f'\\draw[<->] ({x0:.2f},1.15) -- ({x0+Lt*sc:.2f},1.15) node[midway,above] {{{Lt} m}};')
o.append(f'\\draw[<->] (0,-0.4) -- ({Ltn*sc:.2f},-0.4) node[midway,below] {{{Ltn} m}};')
SK=fig('\n'.join(o))
q('0006',tipId='hrs-tunel',tip='Tünelde tamamen kalma süresi',z='orta',alt='Tren ve Tünel',kaz='Trenin tünelde tamamen içinde kaldığı süreyi tünel ve tren boyundan hesaplar.',kalip='hikâyeli',
 kart='K-HRS-06 (tünel) · tünel 700 m, tren 200 m, 90 km/sa',
 metin='Şekilde, bir yolcu treni ile tren hattındaki bir tünel, uzunlukları verilerek ölçekli biçimde gösterilmiştir. Tren, tünele sabit 90 km/sa hızla girmektedir ve tünelden çıkana kadar hızı değişmemektedir.\nBuna göre, tren tamamen tünelin içinde kaldığı sürece kaç saniye geçer?',
 dogru=v,yan=[(e[0],'Tünelden tamamen çıkma süresini bulmuş: (700 + 200) ÷ 25.','dikkat'),(e[1],'Yalnız tünel boyunu kullanmış: 700 ÷ 25.','dikkat'),(e[2],'Yalnız tren boyunu kullanmış: 200 ÷ 25.','dikkat'),(e[3],'Tren boyunu iki kez ekleyip (700 + 200 + 200) ÷ 25 hesaplamış.','islem')],
 istenen='Trenin tünelde tamamen kaldığı süre (sn).',ip=['Trenin tamamen içeride olduğu andaki konumundan çıkışa varışına kadar kat edilen yolu düşün; hız birimine dikkat et.'],bilgi=[TUN],sekil=SK,
 ad=[A('Hızı çevir','km/sa değeri 3,6’ya bölünür.','90 ÷ 3,6 = 25 m/sn'),A('Gereken yol','Tamamen içeride kalınan yol tünel boyu − tren boyudur.','700 − 200 = 500 m'),A('Süreyi bul','Yol hıza bölünür.','500 ÷ 25 = 20 sn')],
 puf='Trenin arka ucu girişten geçtiği an ile ön ucu çıkışa vardığı an arasında alınan yolu düşün.')

# ================= 07 orta · nehir şeması, üç iskele =================
AB_,BC_,vt,vak=36,24,15,5
t_go=Fr(AB_+BC_,vt+vak); t_back=Fr(BC_,vt-vak); v=t_go+t_back
e=[Fr(AB_+BC_+BC_,vt),Fr(AB_+BC_,vt+vak)+Fr(BC_,vt+vak),Fr(AB_+BC_,vt+vak)+Fr(AB_+BC_,vt-vak),Fr(AB_+BC_,vt-vak)+Fr(BC_,vt+vak)]
assert t_go==3 and t_back==Fr(12,5) and v==Fr(27,5) and e==[Fr(28,5),Fr(21,5),9,Fr(36,5)] and len({v,*e})==5
k=0.11; o=[]
xs={'A':0.4,'B':0.4+AB_*k*0.55,'C':0.4+(AB_+BC_)*k*0.55}
o.append(f'\\fill[vurgu!12] (0,-0.6) rectangle ({xs["C"]+0.4},0.6); \\draw[thick] (0,0.6) -- ({xs["C"]+0.4},0.6); \\draw[thick] (0,-0.6) -- ({xs["C"]+0.4},-0.6);')
o.append(f'\\draw[-{{Stealth}},thick] ({xs["A"]+0.5},0) -- ({xs["A"]+2.2},0); \\node[above] at ({xs["A"]+1.35},0) {{\\footnotesize akıntı yönü}};')
for nm,x in xs.items(): o.append(f'\\draw[line width=2.2pt] ({x},-0.9) -- ({x},0.9); \\node[above=2pt] at ({x},0.9) {{{nm}}};')
o.append(f'\\draw[<->] ({xs["A"]},1.65) -- ({xs["B"]},1.65) node[midway,above] {{{AB_} km}}; \\draw[<->] ({xs["B"]},1.65) -- ({xs["C"]},1.65) node[midway,above] {{{BC_} km}};')
SK=fig('\n'.join(o))
q('0007',tipId='hrs-nehir2',tip='Üç iskeleli nehir yolculuğu',z='orta',alt='Üç İskeleli Nehir',kaz='Akıntı yönünde ve akıntıya karşı bölümlerin sürelerini ayrı ayrı hesaplayıp toplar.',kalip='hikâyeli',
 kart='K-HRS-07 (üç iskele) · 36 + 24 km; durgun 15, akıntı 5',
 metin='Şekilde, bir nehir üzerindeki A, B ve C iskeleleri ile aralarındaki uzaklıklar gösterilmiştir; akıntı A’dan C’ye doğrudur. Durgun suda sabit 15 km/sa hızla giden bir tekne, A iskelesinden yola çıkıp C iskelesine gidiyor, orada beklemeden dönerek B iskelesine kadar geliyor. Akıntının hızı sabit 5 km/sa’tir.\nBuna göre, teknenin bu yolculuğu toplam kaç saat sürer?',
 dogru=v,yan=[(e[0],'Akıntıyı hiç hesaba katmamış: (36 + 24 + 24) ÷ 15.','dikkat'),(e[1],'Dönüşte de akıntı yönünde gittiğini sanmış: 60 ÷ 20 + 24 ÷ 20.','dikkat'),(e[2],'Dönüşü A’ya kadar almış: 60 ÷ 20 + 60 ÷ 10.','dikkat'),(e[3],'Gidişi akıntıya karşı, dönüşü akıntı yönünde sanmış: 60 ÷ 10 + 24 ÷ 20.','dikkat')],
 istenen='Yolculuğun toplam süresi (saat).',ip=['Şekilde teknenin hangi iskeleler arasında hangi yönde gittiğini belirle; yönlere göre hızını ayrı ayrı düşün.'],bilgi=[AKI],sekil=SK,
 ad=[A('Gidiş hızı','Akıntı yönünde.','15 + 5 = 20 km/sa'),A('Gidiş süresi','A–C arası 36 + 24 = 60 km.','60 ÷ 20 = 3 saat'),A('Dönüş süresi','C–B arası akıntıya karşı: 15 − 5 = 10 km/sa.','24 ÷ 10 = 2,4 saat'),A('Toplam','Süreler toplanır.','3 + 2,4 = 5,4 saat')],
 puf='Akıntı yönünde ve karşıt yönde hızlar farklıdır; bölümleri ayrı hesapla.')

# ================= 08 orta · tarife tablosu =================
k1,v1_,hz1,k2,hz2=Fr(17,2),Fr(11),90,Fr(37,4),75   # 08.30 – 11.00 ; 09.15
sure1=(v1_-k1)*60; mesafe=hz1*(v1_-k1); v=mesafe/hz2*60
e=[(v1_-k2)*60,sure1*Fr(hz2,hz1),sure1,Fr(hz1*Fr(7,2),hz2)*60]
assert sure1==150 and mesafe==225 and v==180 and e==[105,125,150,252] and len({v,*e})==5
SK=tablo_svg(['Sefer','Kalkış saati','Varış saati','Hız (km/sa)'],[['1. sefer','08.30','11.00',str(hz1)],['2. sefer','09.15','?',str(hz2)]])
q('0008',tipId='hrs-tablo',tip='Tarife tablosu ve süre',z='orta',alt='Sefer Tarifesi',kaz='Tarife tablosundan yolu bulup ikinci seferin yolculuk süresini hesaplar.',kalip='tablo',
 kart='K-HRS-08 (tarife) · 150 dk × 90 km/sa = 225 km; 225 ÷ 75',
 metin='Aynı iki şehir arasında aynı yolu izleyen iki otobüsün seferleri aşağıdaki tabloda verilmiştir. Her otobüs yolculuk boyunca sabit hızla gitmekte ve hiç durmamaktadır.\nBuna göre, 2. seferin yolculuk süresi kaç dakikadır?',
 dogru=v,yan=[(e[0],'2. seferin kalkışı ile 1. seferin varışı arasındaki süreyi (09.15 – 11.00) yolculuk süresi sanmış.','dikkat'),(e[1],'Süreyi hızla doğru orantılı sanmış: 150 × 75 ÷ 90.','dikkat'),(e[2],'1. seferin süresini (150 dk) 2. sefer için de aynen yazmış.','dikkat'),(e[3],'1. seferin süresini 3 sa 30 dk bulmuş: 90 × 3,5 = 315 km; 315 ÷ 75 = 4,2 sa = 252 dk.','dikkat')],
 istenen='2. seferin yolculuk süresi (dk).',ip=['1. seferin kalkış ve varış saatlerinden bu yolun uzunluğunu bulmaya çalış.'],bilgi=[TAR],sekil=SK,
 ad=[A('1. seferin süresi','Varış saati − kalkış saati.','11.00 − 08.30 = 2 saat 30 dk = 2,5 saat'),A('Yol','Hız × süre.','90 × 2,5 = 225 km'),A('2. seferin süresi','Yol, 2. seferin hızına bölünür.','225 ÷ 75 = 3 saat'),A('Dakikaya çevir','Saat 60 ile çarpılır.','3 × 60 = 180 dk')],
 puf='Önce 1. seferden yolun uzunluğunu bul; sonra ikinci hızla süreyi hesapla.')

# ================= 09 zor · nehir, tahta ve kayık =================
Dn,tk,tt=72,3,18; vc=Fr(Dn,tt); vd=Fr(Dn,tk); vs=vd-vc; vu=vs-vc; v=Dn/vu
e=[Fr(tk),Fr(Dn)/(vd-vc),vc,Fr(tt)]
assert vc==4 and vd==24 and vs==20 and vu==16 and v==Fr(9,2) and e==[3,Fr(18,5),4,18] and len({v,*e})==5
o=[]
o.append('\\fill[vurgu!12] (0,-0.6) rectangle (8,0.6); \\draw[thick] (0,0.6) -- (8,0.6); \\draw[thick] (0,-0.6) -- (8,-0.6);')
o.append('\\draw[-{Stealth},thick] (3.0,0) -- (5.0,0); \\node[above] at (4.0,0) {\\footnotesize akıntı yönü};')
for x,nm in ((0.4,'A'),(7.6,'B')): o.append(f'\\draw[line width=2.2pt] ({x},-0.9) -- ({x},0.9); \\node[above=2pt] at ({x},0.9) {{{nm}}};')
o.append(f'\\draw[<->] (0.4,1.65) -- (7.6,1.65) node[midway,above] {{{Dn} km}};')
o.append(f'\\draw[-{{Stealth}},very thick] (0.4,-1.35) -- (7.6,-1.35); \\node[below=1pt] at (4.0,-1.35) {{Kayık: A’dan B’ye {tk} saat}};')
o.append(f'\\draw[-{{Stealth}},very thick,dashed] (0.4,-2.35) -- (7.6,-2.35); \\node[below=1pt] at (4.0,-2.35) {{Tahta parçası: A’dan B’ye {tt} saat}};')
SK=fig('\n'.join(o))
q('0009',tipId='hrs-nehir',tip='Akıntı ve sürüklenen cisim',z='zor',alt='Akıntılı Nehir',kaz='Akıntıyla sürüklenen cismin süresinden akıntı hızını bulup kayığın dönüş süresini hesaplar.',kalip='hikâyeli',
 kart='K-HRS-09 (nehir) · tahta 72/18 = 4; kayık 72/3 = 24',
 metin='Şekilde, bir nehirdeki A ve B iskeleleri arasındaki uzaklık ve akıntının yönü gösterilmiştir. Motorlu bir kayık A’dan B’ye giderken, aynı anda A iskelesinden bırakılan bir tahta parçası akıntıyla sürüklenerek B’ye ulaşmıştır; ikisinin süreleri şekilde yazılıdır. Akıntının hızı ve kayığın durgun sudaki hızı sabittir.\nBuna göre, kayık B’den A’ya dönerken bu yolu kaç saatte alır?',
 dogru=v,yan=[(e[0],'Dönüşü de gidişle aynı sürede almış sanmış.','dikkat'),(e[1],'Dönüş hızını gidiş hızından akıntıyı yalnız bir kez çıkararak bulmuş: 72 ÷ (24 − 4).','dikkat'),(e[2],'Akıntının hızını (4 km/sa) süre olarak yazmış.','dikkat'),(e[3],'Tahta parçasının süresini kayığın dönüş süresi sanmış.','dikkat')],
 istenen='Kayığın B’den A’ya dönüş süresi (saat).',ip=['Tahta parçasının hızı, akıntının hızı hakkında ne söyler? Kayığın gidişteki hızını da bu hızla ilişkilendir.'],bilgi=[AKI],sekil=SK,
 ad=[A('Akıntının hızı','Tahta akıntıyla aynı hızda gider.','72 ÷ 18 = 4 km/sa'),A('Kayığın gidiş hızı','Yol ÷ süre.','72 ÷ 3 = 24 km/sa'),A('Durgun sudaki hız','Gidişte kayık + akıntı = 24.','24 − 4 = 20 km/sa'),A('Dönüş hızı','Akıntıya karşı kayık − akıntı.','20 − 4 = 16 km/sa'),A('Dönüş süresi','Yol ÷ hız.','72 ÷ 16 = 4,5 saat')],
 puf='Tahta parçasının yaptığı yolculuk akıntının hızını verir.')

# ================= 10 zor · ikinci karşılaşma =================
D,v1,v2=240,45,30; T=Fr(3*D,v1+v2); p1=v1*T
assert T==Fr(48,5) and p1==432
konum=D-(p1-D)  # birinci araç dönüşte, B'den (p1-D) uzakta -> A'dan D-(p1-D)
v=konum; ilk=v1*Fr(D,v1+v2)
e=[Fr(p1-D),Fr(D,2),ilk,Fr(v2)*T]
assert v==48 and e==[192,120,144,288] and len({v,*e})==5
# ikinci aracın konumu (A'dan): D'de A'ya varıp döner -> v2*T-D
assert v2*T-D==konum
k=0.03; o=[f'\\draw[very thick] (0,0) -- ({D*k},0);']
for x,nm in ((0,'A'),(D*k,'B')): o.append(f'\\draw[line width=2.2pt] ({x},-0.25) -- ({x},0.25); \\node[below=9pt] at ({x},0) {{{nm}}};')
o.append(f'\\filldraw[fill=vurgu!30] (0.1,0.12) rectangle (0.9,0.5); \\draw[-{{Stealth}},thick] (0.95,0.31) -- (1.7,0.31); \\node[above] at (0.5,0.55) {{1}};')
o.append(f'\\filldraw[fill=gray!25] ({D*k-0.9},0.12) rectangle ({D*k-0.1},0.5); \\draw[-{{Stealth}},thick] ({D*k-0.95},0.31) -- ({D*k-1.7},0.31); \\node[above] at ({D*k-0.5},0.55) {{2}};')
o.append(f'\\draw[<->] (0,-0.85) -- ({D*k},-0.85) node[midway,below] {{{D} km}};')
SK=fig('\n'.join(o))
q('0010',tipId='hrs-ikinci',tip='İkinci karşılaşma noktası',z='zor',alt='İkinci Karşılaşma',kaz='Uçlarda dönen iki hareketlinin ikinci karşılaşma noktasını toplam yol ilişkisiyle bulur.',kalip='hikâyeli',
 kart='K-HRS-10 (ikinci karşılaşma) · 240 km, 45 ve 30 km/sa; toplam 720 km',
 metin='Şekilde A ve B limanları arasındaki deniz yolu gösterilmiştir. 1 numaralı gemi A’dan sabit 45 km/sa, 2 numaralı gemi B’den sabit 30 km/sa hızla, aynı anda birbirine doğru yola çıkıyor. Gemiler karşı limana varınca hiç beklemeden aynı hızla geri dönüyor ve aynı yolu izlemeyi sürdürüyor.\nBuna göre, gemiler ikinci kez karşılaştıklarında A limanına uzaklıkları kaç km’dir?',
 dogru=v,yan=[(e[0],'Birinci geminin dönüşte B’ye uzaklığını (192 km) A’ya uzaklık sanmış.','dikkat'),(e[1],'Karşılaşmanın yolun ortasında olduğunu sanmış.','dikkat'),(e[2],'İlk karşılaşma noktasının A’ya uzaklığını (144 km) yazmış.','dikkat'),(e[3],'İkinci geminin ikinci karşılaşmaya kadar aldığı toplam yolu (288 km) yazmış.','dikkat')],
 istenen='İkinci karşılaşma noktasının A’ya uzaklığı (km).',ip=['İkinci karşılaşmaya kadar iki geminin aldığı yolların toplamının yol uzunluğunun kaç katı olduğunu düşün.'],bilgi=[IKI],sekil=SK,
 ad=[A('Toplam yol','İkinci karşılaşmada iki gemi toplam 3 yol uzunluğu alır.','3 × 240 = 720 km'),A('Süre','Toplam yol, hızlar toplamına bölünür.','720 ÷ 75 = 9,6 saat'),A('1. geminin yolu','Hız × süre.','45 × 9,6 = 432 km'),A('Konumu bul','240 km gidip B’den dönmüştür.','432 − 240 = 192 km → B’den 192 km, A’dan 240 − 192 = 48 km')],
 puf='Her gemi uca varınca döndüğü için toplam yolu ve süreyi önce bul.')

bitir(P,'hareketsek',UK)
