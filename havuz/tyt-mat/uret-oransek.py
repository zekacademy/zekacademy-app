"""Oran Orantı · ŞEKİLLİ paket (10 soru): şekil/tablo/grafik çözüm verisini taşır; sayılar Python'da hesaplanır, her doğru ve çeldirici değer assert'lidir. Kardeş yok, ipucu 1."""
import sys,os,math
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
from math import cos,sin,radians,asin,degrees
H.KONU='Oran Orantı'
P=Parti('oransek','Oran Orantı','mat|Oran Orantı')
KY='ÖSYM 2018–2026 TYT Matematik (şekilli/tablolu/grafikli oran-orantı soruları; yalnız mantık) · MEB 8–9. sınıf'
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)
def fig(body): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'+body+'\n\\end{tikzpicture}')
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)

DO=B('Doğru orantı','iki çokluktan biri belli sayıda katına çıkınca öteki de aynı sayıda katına çıkıyorsa orantı doğrudur; oran (bölüm) sabittir. Örnek: 4 kalem 20 TL ise 6 kalem 30 TL')
TO=B('Ters orantı','biri belli sayıda katına çıkarken öteki aynı sayıda küçülüyorsa orantı terstir; çarpım sabittir. Örnek: 6 işçi 10 günde bitirirse 4 işçi 15 günde bitirir')
OL=B('Harita ölçeği','haritadaki uzunluk ile gerçek uzunluğun oranı sabittir; ölçek çubuğu bu oranı gösterir. Örnek: 1 cm = 5 km ise 3 cm = 15 km')
KS=B('Kasnaklar','bir kayışla bağlı kasnakların çevrelerinin hızı eşittir; devir sayısı ile çap ters orantılıdır. Örnek: çapı 2 katı olan kasnak yarı sayıda devir yapar')

# ---------- kartlar ----------
kartla('K-ORS-01','Doğru orantı grafiği','Orijinden geçen doğru, doğru orantıyı gösterir; grafikteki bir noktadan birim değer bulunur ve istenen miktarla çarpılır.','Toplamsal düşünmek; ters orantı sanmak; iki değeri çarpmak.','kolay','grafik',3,'ors-grafik','Doğru orantı grafiği')
kartla('K-ORS-02','Çift sayı doğrusu','Çift sayı doğrusunda karşılıklı iki değerden birim oran bulunur; kalan miktar bu orana bölünür.','Okunan miktarı kalanla karıştırmak; bölme yerine çarpma yapmak.','kolay','şekilli',3,'ors-cift','Çift sayı doğrusu')
kartla('K-ORS-03','Gölge boyu ve cisim boyu','Aynı anda güneş ışınları paralel olduğundan boy ile gölge boyu doğru orantılıdır.','Toplamsal düşünmek; oranı ters kurmak.','kolay','şekilli',3,'ors-golge','Gölge boyu ve cisim boyu')
kartla('K-ORS-04','Tarif tablosu ve fark bilgisi','Tablodaki miktarlar bir paketin içeriğidir; iki malzemenin farkı, bir paketteki farkın kaç katı olduğunu verir; toplam o kadar paketin kütlesidir.','Bir paketin toplamını yazmak; yalnız bir malzemenin kütlesini bulmak.','orta','tablo',4,'ors-tarif','Tarif tablosu')
kartla('K-ORS-05','Kasnak düzeneği','Kayışla bağlı kasnaklarda çap ile devir ters orantılıdır; devir sayısı süreyle doğru orantılıdır.','Çapla devri doğru orantı sanmak; süreyi hesaba katmamak.','orta','şekilli',3,'ors-kasnak','Kasnak ve çap-devir ilişkisi')
kartla('K-ORS-06','Daire grafiği ile paylaştırma','Dilimin merkez açısı payla doğru orantılıdır; bir dilimin tutarından derece başına tutar bulunur; kalan dilim 360 dereceden çıkarılarak bulunur.','Kalan açıyı bulurken bir dilimi çıkarmamak; yanlış dilimi okumak.','orta','grafik',4,'ors-pasta','Daire grafiği ve orantılı pay')
kartla('K-ORS-07','Karışım kapları','Her kaptaki maddelerin hacmi bölme değerleriyle bulunur; şurup hacmi sabit kalır, istenen orana göre gereken su hesaplanır.','Bölme değerini iki kap için aynı sanmak; mevcut suyu hesaba katmamak.','orta','şekilli',5,'ors-karisim','Karışım kapları ve oran')
kartla('K-ORS-08','Bölmeli şerit','Eş bölmeli şeritte bir parçanın uzunluğu bir bölmenin uzunluğunu verir; diğer parçalar bölme sayısıyla orantılıdır.','Kesilen kısmı bölme sayısıyla ya da başka bir parçayla karıştırmak.','orta','şekilli',4,'ors-serit','Bölmeli şerit ve parça oranları')
kartla('K-ORS-09','Ölçekli kroki','Ölçek çubuğundan 1 cm’in gerçek uzunluğu bulunur; dik üçgende hipotenüs hesaplanıp iki yol karşılaştırılır.','Ölçeği 1 cm yerine çubuğun tamamına uygulamak; yalnız bir yolu hesaplamak.','orta','şekilli',4,'ors-harita','Ölçekli kroki')
kartla('K-ORS-10','Üç değişkenli tablo','Tablodaki üç çokluktan usta ve saat ile iş doğru, süre ile ters orantılıdır; usta × saat × gün çarpımı sabittir.','Bir değişkeni hesaba katmamak; ters orantıyı doğru sanmak.','zor','tablo',4,'ors-tablo','Ters orantı tablosu')

# ================= 01 kolay · doğru orantı grafiği =================
bk,bp=3,105; birim=Fr(bp,bk); N=9; v=birim*N
e=[Fr(bp*bk,N),bp+(N-bk),210,bp*N]; assert v==315 and birim==35 and e==[35,111,210,945] and len({v,*e})==5
sx,sy=0.78,1.0/70; o=[f'\\draw[-{{Stealth}}] (0,0) -- ({7.5*sx},0) node[right] {{Kütle (kg)}};',f'\\draw[-{{Stealth}}] (0,0) -- (0,{300*sy:.3f}) node[above] {{Ücret (TL)}};']
for k in range(1,8): o.append(f'\\draw ({k*sx:.3f},-0.07) -- ({k*sx:.3f},0.07); \\node[below=2pt] at ({k*sx:.3f},0) {{{k}}};')
for t in (70,140,210,280): o.append(f'\\draw (-0.07,{t*sy:.3f}) -- (0.07,{t*sy:.3f}); \\node[left=2pt] at (0,{t*sy:.3f}) {{{t}}};')
o.append(f'\\draw[thick] (0,0) -- ({6*sx},{210*sy:.3f});')
o.append(f'\\draw[dashed] ({bk*sx},0) -- ({bk*sx},{bp*sy:.3f}) -- (0,{bp*sy:.3f}); \\fill ({bk*sx},{bp*sy:.3f}) circle (0.08);')
o.append(f'\\node[left=2pt] at (0,{bp*sy:.3f}) {{{bp}}};')
SK=fig('\n'.join(o))
q('0001',tipId='ors-grafik',tip='Doğru orantı grafiği',z='kolay',alt='Doğru Orantı Grafiği',kaz='Doğru orantı grafiğindeki bir noktadan birim değeri bulup başka miktarın değerini hesaplar.',kalip='grafik',
 kart='K-ORS-01 (doğru orantı grafiği) · (3 kg, 105 TL) → 9 kg',
 metin='Şekildeki doğru grafiği, bir manavda satılan elmanın kütlesi ile ödenecek ücret arasındaki ilişkiyi göstermektedir. Elmanın kilogram fiyatı sabittir.\nBuna göre, aynı manavdan 9 kg elma alan bir müşteri kaç TL öder?',
 dogru=v,yan=[(e[0],'Birim fiyatı (105 ÷ 3 = 35) bulup 9 kg ile çarpmayı unutmuş.','dikkat'),(e[1],'Toplamsal düşünmüş: kütle 6 kg artınca ücreti de 6 TL artırmış: 105 + 6.','dikkat'),(e[2],'Grafikte görünen son değeri (6 kg için 210 TL) yazmış.','dikkat'),(e[3],'Kütleyi 3 kg’lık ücretle çarpmış: 9 × 105.','islem')],
 istenen='9 kg elmanın ücreti (TL).',ip=['Grafikte işaretli noktanın değerlerini oku; 1 kg için ödenen tutarı bul.'],bilgi=[DO],sekil=SK,
 ad=[A('Noktayı oku','Grafikteki işaretli noktada 3 kg için ödenen ücret okunur.','3 kg → 105 TL'),A('Birim fiyatı bul','Ücret kütleye bölünür.','105 ÷ 3 = 35 TL/kg'),A('9 kg’ı hesapla','Birim fiyat kütleyle çarpılır.','9 × 35 = 315 TL')],
 puf='Orijinden geçen doğru: ücret ÷ kütle sabittir.')

# ================= 02 kolay · çift sayı doğrusu =================
dk,sf=20,30; hiz=Fr(sf,dk); kitap,okunan=420,150; kalan=kitap-okunan; v=kalan/hiz
e=[Fr(okunan)/hiz,kalan,Fr(kitap)/hiz,kalan*hiz]; assert v==180 and e==[100,270,280,405] and len({v,*e})==5
xs=[0.4+i*1.8 for i in range(6)]; o=[f'\\draw (0.0,1.6) -- ({xs[-1]+0.4},1.6); \\draw (0.0,0) -- ({xs[-1]+0.4},0);']
o.append('\\node[anchor=east] at (-0.1,1.6) {Süre (dk)}; \\node[anchor=east] at (-0.1,0) {Sayfa};')
for i,x in enumerate(xs):
    o.append(f'\\draw ({x},1.5) -- ({x},1.7); \\draw ({x},-0.1) -- ({x},0.1); \\draw[dashed,thin] ({x},0.1) -- ({x},1.5);')
    o.append(f'\\node[above=3pt] at ({x},1.7) {{{i*dk}}};')
    if i in (0,1,3): o.append(f'\\node[below=3pt] at ({x},-0.1) {{{i*sf}}};')
SK=fig('\n'.join(o))
q('0002',tipId='ors-cift',tip='Çift sayı doğrusu',z='kolay',alt='Çift Sayı Doğrusu',kaz='Çift sayı doğrusundaki karşılıklı değerlerden hız bulup kalan işin süresini hesaplar.',kalip='şekilli',
 kart='K-ORS-02 (çift sayı doğrusu) · 20 dk ↔ 30 sayfa; 420 sayfa, 150 okunmuş',
 metin='Şekildeki çift sayı doğrusu, Ece’nin sabit hızla kitap okurken geçen süre ile okuduğu sayfa sayısını göstermektedir. Ece, 420 sayfalık bir kitabın 150 sayfasını okuduktan sonra aynı hızla okumaya devam etmektedir.\nBuna göre, Ece kitabın kalan kısmını kaç dakikada okur?',
 dogru=v,yan=[(e[0],'Okuduğu 150 sayfanın süresini bulmuş: 150 ÷ 1,5.','dikkat'),(e[1],'Kalan sayfa sayısını (270) dakika sanmış.','dikkat'),(e[2],'Tüm kitabın süresini bulmuş: 420 ÷ 1,5.','dikkat'),(e[3],'Bölmesi gerekirken çarpmış: 270 × 1,5.','islem')],
 istenen='Kalan sayfaların okunma süresi (dk).',ip=['Aynı sütundaki iki değerden dakikada okunan sayfa sayısını bul; kalan sayfayı belirle.'],bilgi=[DO],sekil=SK,
 ad=[A('Hızı bul','Çift sayı doğrusunda karşılıklı değerler: 20 dk ↔ 30 sayfa.','30 ÷ 20 = 1,5 sayfa/dk'),A('Kalan sayfa','Kitaptan okunan çıkarılır.','420 − 150 = 270 sayfa'),A('Süreyi bul','Kalan sayfa hıza bölünür.','270 ÷ 1,5 = 180 dk')],
 puf='Sayfa ÷ dakika = hız; kalan işi hıza bölersen süreyi bulursun.')

# ================= 03 kolay · gölge boyu =================
hc,gc,gt=Fr(3,2),2,12; v=hc/gc*gt
e=[Fr(gt*gc)/hc,hc+(gt-gc),hc*gt,Fr(gt,gc)]
assert v==9 and e==[16,Fr(23,2),18,6] and len({v,*e})==5
sc=0.4; o=['\\draw[thick] (-0.9,0) -- (7.6,0);']
o.append(f'\\draw[very thick] (0,0) -- (0,{float(hc)*sc:.2f}); \\fill (0,{float(hc)*sc:.2f}) circle (0.05);')
o.append(f'\\draw[very thick,vurgu] (0,0) -- ({gc*sc:.2f},0); \\draw[dashed] (0,{float(hc)*sc:.2f}) -- ({gc*sc:.2f},0);')
x0=2.2; H_=9*sc; o.append(f'\\draw[very thick] ({x0},0) -- ({x0},{1.3}); \\draw[fill=vurgu!15,thick] ({x0},{(H_+1.3)/2:.2f}) ellipse (0.65 and {(H_-1.3)/2:.2f});')
o.append(f'\\draw[very thick,vurgu] ({x0},0) -- ({x0+gt*sc:.2f},0); \\draw[dashed] ({x0},{H_:.2f}) -- ({x0+gt*sc:.2f},0);')
o.append(f'\\node[left] at (-0.12,{float(hc)*sc/2:.2f}) {{1,5 m}}; \\node[below=3pt] at ({gc*sc/2:.2f},0) {{2 m}}; \\node[below=3pt] at ({x0+gt*sc/2:.2f},0) {{12 m}};')
o.append(f'\\draw[<->] ({x0-0.95},0) -- ({x0-0.95},{H_:.2f}); \\node[left] at ({x0-0.95},{H_/2:.2f}) {{$h$}};')
SK=fig('\n'.join(o))
q('0003',tipId='ors-golge',tip='Gölge boyu ve cisim boyu',z='kolay',alt='Gölge Boyu',kaz='Aynı andaki gölge boylarından cismin boyunu orantıyla hesaplar.',kalip='şekilli',
 kart='K-ORS-03 (gölge) · 1,5 m ↔ 2 m ; ağaç gölgesi 12 m',
 metin='Güneş ışınlarının paralel geldiği bir anda, boyu 1,5 m olan bir çocuğun gölgesinin uzunluğu 2 m, bir ağacın gölgesinin uzunluğu ise 12 m ölçülmüştür (şekil ölçekli çizilmiştir).\nBuna göre, ağacın boyu h kaç metredir?',
 dogru=v,yan=[(e[0],'Orantıyı ters kurmuş: 12 × 2 ÷ 1,5.','dikkat'),(e[1],'Toplamsal düşünmüş: gölgeler 10 m farklı olduğundan boyu da 10 m fazla almış: 1,5 + 10.','dikkat'),(e[2],'Çocuğun boyunu ağacın gölgesiyle çarpmış: 1,5 × 12.','islem'),(e[3],'Yalnız gölgelerin oranını almış: 12 ÷ 2.','islem')],
 istenen='Ağacın boyu (m).',ip=['Çocuğun boyunun gölgesine oranını bul; aynı oran ağaç için de geçerlidir.'],bilgi=[DO],sekil=SK,
 ad=[A('Oranı kur','Aynı anda boy ile gölge doğru orantılıdır.','boy/gölge = 1,5/2 = 3/4'),A('Ağaca uygula','Oran ağacın gölgesiyle çarpılır.','h = 12 × 3/4'),A('Sonuç','Çarpma yapılır.','h = 9 m')],
 puf='Aynı anda: boy ÷ gölge sabittir.')

# ================= 04 orta · tarif tablosu =================
t1,t2,t3=150,100,80; fark=210; n=Fr(fark,t1-t3); paket=t1+t2+t3; v=n*paket
e=[fark,paket,n*t1,n*(t1+t3)]; assert n==3 and paket==330 and v==990 and e==[210,330,450,690] and len({v,*e})==5
SK=tablo_svg(['Malzeme','1 paketteki miktar (g)'],[['Fındık',str(t1)],['Fıstık',str(t2)],['Badem',str(t3)]])
q('0004',tipId='ors-tarif',tip='Tarif tablosu',z='orta',alt='Tarif Tablosu',kaz='Tablodaki miktarlardan fark bilgisiyle paket sayısını ve toplam kütleyi bulur.',kalip='tablo',
 kart='K-ORS-04 (tarif tablosu) · 150/100/80 g; fındık − badem = 210 g',
 metin='Bir kuruyemişçi, 1 paketteki miktarları aşağıdaki tabloda verilen karışımdan birkaç paket hazırlamıştır; bütün paketlerde malzeme miktarları tablodaki gibidir. Hazırlanan paketlerdeki toplam fındık miktarı, toplam badem miktarından 210 g fazladır.\nBuna göre, hazırlanan paketlerdeki kuruyemişin tamamı kaç gramdır?',
 dogru=v,yan=[(e[0],'Farkı (210) toplam kütle sanmış.','dikkat'),(e[1],'Yalnız bir paketin kütlesini (150 + 100 + 80) yazmış.','dikkat'),(e[2],'Paket sayısını bulup yalnız fındığı toplamış: 3 × 150.','dikkat'),(e[3],'Fıstığı unutup fındık ile bademi toplamış: 3 × (150 + 80).','dikkat')],
 istenen='Paketlerdeki kuruyemişin toplam kütlesi (g).',ip=['Bir paketteki fındık–badem farkını bulup toplam farkın kaç katı olduğuna bak.'],bilgi=[DO],sekil=SK,
 ad=[A('Bir paketteki fark','Tablodan fındık ve badem okunur.','150 − 80 = 70 g'),A('Paket sayısı','Toplam fark, bir paketteki farka bölünür.','210 ÷ 70 = 3 paket'),A('Bir paket','Üç malzeme toplanır.','150 + 100 + 80 = 330 g'),A('Toplam','Paket sayısıyla çarpılır.','3 × 330 = 990 g')],
 puf='Fark bilgisi kaç paket olduğunu verir; sonra bir paketin toplamıyla çarp.')

# ================= 05 orta · kasnak düzeneği =================
dA,dB=40,25; nA,tA=150,5; tB=8; hizA=Fr(nA,tA); hizB=hizA*dA/dB; v=hizB*tB
e=[hizB,hizB+tB,hizA*dB/dA*tB,hizA*tB]; assert v==384 and e==[48,56,Fr(300,2),240] and len({v,*e})==5
R1,R2,d=2.0,1.25,5.0; al=asin((R1-R2)/d); a=degrees(al); u=(sin(al),cos(al))
p1=(R1*u[0],R1*u[1]); p2=(d+R2*u[0],R2*u[1]); q1=(p1[0],-p1[1]); q2=(p2[0],-p2[1])
o=[f'\\draw[thin] (0,0) circle ({R1}); \\draw[thin] ({d},0) circle ({R2});',f'\\fill (0,0) circle (0.07); \\fill ({d},0) circle (0.07);',
   f'\\draw[line width=1.8pt] ({p1[0]:.3f},{p1[1]:.3f}) -- ({p2[0]:.3f},{p2[1]:.3f}); \\draw[line width=1.8pt] ({q1[0]:.3f},{q1[1]:.3f}) -- ({q2[0]:.3f},{q2[1]:.3f});',
   f'\\draw[line width=1.8pt] ({p1[0]:.3f},{p1[1]:.3f}) arc[start angle={90-a:.2f},end angle={270+a:.2f},radius={R1}];',
   f'\\draw[line width=1.8pt] ({q2[0]:.3f},{q2[1]:.3f}) arc[start angle={-(90-a):.2f},end angle={90-a:.2f},radius={R2}];',
   f'\\node[above right] at (0,0) {{A}}; \\node[above right] at ({d},0) {{B}};',
   f'\\draw[<->] (-{R1},-2.55) -- ({R1},-2.55); \\node[below] at (0,-2.55) {{çap 40 cm}}; \\draw[<->] ({d-R2},-2.55) -- ({d+R2},-2.55); \\node[below] at ({d},-2.55) {{çap 25 cm}};']
SK=fig('\n'.join(o))
q('0005',tipId='ors-kasnak',tip='Kasnak ve çap-devir ilişkisi',z='orta',alt='Kasnak Düzeneği',kaz='Kayışla bağlı kasnaklarda çap-devir ters orantısını ve süreyi birlikte kullanır.',kalip='şekilli',
 kart='K-ORS-05 (kasnak) · çap 40 ve 25 cm; A: 5 dk’da 150 devir',
 metin='Şekildeki düzenekte A ve B kasnakları bir kayışla birbirine bağlıdır; kayış kasnaklar üzerinde kaymadan dönmektedir. A kasnağı sabit hızla 5 dakikada 150 tam devir yapmaktadır.\nBuna göre, B kasnağı 8 dakikada kaç devir yapar?',
 dogru=v,yan=[(e[0],'B’nin yalnız bir dakikadaki devrini (48) bulup 8 dakika ile çarpmayı unutmuş.','dikkat'),(e[1],'B’nin dakikadaki devrini (48) süre ile çarpmak yerine toplamış: 48 + 8.','islem'),(e[2],'Çap ile devri doğru orantılı sanmış: 30 × 25 ÷ 40 = 18,75 devir/dk; 8 dakikada 150 devir bulmuş.','dikkat'),(e[3],'Kasnakların aynı devir yaptığını sanmış: 30 × 8.','dikkat')],
 istenen='B kasnağının 8 dakikadaki devir sayısı.',ip=['A’nın bir dakikadaki devrini bul; kayışla dönen kasnaklarda çap büyüdükçe devir ne olur?'],bilgi=[KS],sekil=SK,
 ad=[A('A’nın hızı','Devir sayısı süreye bölünür.','150 ÷ 5 = 30 devir/dk'),A('B’nin hızı','Çap ile devir ters orantılıdır: 40 × 30 = 25 × n.','n = 1200 ÷ 25 = 48 devir/dk'),A('8 dakikada','Dakikadaki devir süreyle çarpılır.','48 × 8 = 384 devir')],
 puf='Kayışla bağlı kasnaklarda çap × devir sayısı aynıdır.')

# ================= 06 orta · daire grafiği =================
kira,gida,fatura=144,90,48; diger=360-kira-gida-fatura; gtl=4500; der=Fr(gtl,gida); v=der*diger
e=[der*fatura,der*72,der*(360-kira-gida),der*(360-kira-fatura)]
assert 144+90+48==282 and diger==78 and der==50 and v==3900 and e==[2400,3600,6300,8400] and len({v,*e})==5
o=[]; r=1.6; ang=90; sl=[('Kira',kira),('Gıda',gida),('Fatura',fatura),('Diğer',diger)]
for nm,dg in sl:
    a1,a2=ang,ang-dg; mid=radians((a1+a2)/2)
    o.append(f'\\draw[thick] (0,0) -- ({r*cos(radians(a1)):.3f},{r*sin(radians(a1)):.3f}) arc[start angle={a1},end angle={a2},radius={r}] -- cycle;')
    lab=nm if nm=='Diğer' else f'{nm} ${dg}^\\circ$'
    ax='west' if cos(mid)>0.1 else 'east' if cos(mid)<-0.1 else 'center'
    o.append(f'\\node[anchor={ax}] at ({(r+0.2)*cos(mid):.3f},{(r+0.25)*sin(mid):.3f}) {{{lab}}};'); ang=a2
SK=fig('\n'.join(o))
q('0006',tipId='ors-pasta',tip='Daire grafiği ve orantılı pay',z='orta',alt='Daire Grafiği',kaz='Daire grafiğinde dilim açılarıyla orantı kurup bilinmeyen dilimin tutarını bulur.',kalip='grafik',
 kart='K-ORS-06 (daire grafiği) · 144°/90°/48°; gıda 4500 TL',
 metin='Şekildeki daire grafiği, bir ailenin aylık gelirinin harcama kalemlerine göre dağılımını göstermektedir. Aile gelirinin tamamını harcamaktadır ve bir kalemin tutarı, grafikteki diliminin merkez açısıyla doğru orantılıdır. Ailenin gıda için harcadığı tutar 4500 TL’dir.\nBuna göre, ailenin “Diğer” kalemi için harcadığı tutar kaç TL’dir?',
 dogru=v,yan=[(e[0],'“Diğer” yerine Fatura dilimini (48°) okumuş: 48 × 50.','dikkat'),(e[1],'Açıları toplarken 144 + 90 + 48 = 288 bulmuş (doğrusu 282); “Diğer” dilimi 72° çıkmış: 72 × 50.','islem'),(e[2],'Fatura dilimini çıkarmayı unutmuş: 360 − 144 − 90 = 126°; 126 × 50.','dikkat'),(e[3],'Gıda dilimini çıkarmayı unutmuş: 360 − 144 − 48 = 168°; 168 × 50.','dikkat')],
 istenen='“Diğer” kaleminin tutarı (TL).',ip=['Gıda diliminden 1 derece için ayrılan tutarı bul; “Diğer” diliminin açısını diğer üç açıdan yararlanarak belirle.'],bilgi=[DO],sekil=SK,
 ad=[A('Derece başına tutar','Gıda diliminin açısına bölünür.','4500 ÷ 90 = 50 TL/derece'),A('Bilinen açılar','Kira, gıda ve fatura açıları toplanır.','144 + 90 + 48 = 282°'),A('“Diğer” açısı','Tam daire 360°’dir.','360 − 282 = 78°'),A('Tutarı bul','Açı, derece başına tutarla çarpılır.','78 × 50 = 3900 TL')],
 puf='Dilimlerin açı toplamı 360°; derece başına tutar tüm dilimlerde aynı.')

# ================= 07 orta · karışım kapları =================
Kb,Kcap=8,800; Lb,Lcap=8,400; vK=Fr(Kcap,Kb); vL=Fr(Lcap,Lb)
sK,wK,sL,wL=2,3,2,4; S=sK*vK+sL*vL; W=wK*vK+wL*vL; hedef=3*S; v=hedef-W
e=[3*(sK*vK+sL*vK)-(wK*vK+wL*vK),hedef-wK*vK,4*S-W,hedef]
assert vK==100 and vL==50 and S==300 and W==500 and v==400 and e==[500,600,700,900] and len({v,*e})==5
def beaker(cx,nS,nW,cap,nm,dh=0.38,w=1.2,nb=8):
    h=nb*dh; o=[f'\\fill[gray!55] ({cx-w/2},0) rectangle ({cx+w/2},{nS*dh:.3f}); \\fill[vurgu!15] ({cx-w/2},{nS*dh:.3f}) rectangle ({cx+w/2},{(nS+nW)*dh:.3f});']
    o.append(f'\\draw[line width=1.2pt] ({cx-w/2},{h:.3f}) -- ({cx-w/2},0) -- ({cx+w/2},0) -- ({cx+w/2},{h:.3f});')
    o.append(f'\\draw[thin] ({cx-w/2},{(nS+nW)*dh:.3f}) -- ({cx+w/2},{(nS+nW)*dh:.3f}); \\draw[thin] ({cx-w/2},{nS*dh:.3f}) -- ({cx+w/2},{nS*dh:.3f});')
    for i in range(1,nb+1): o.append(f'\\draw[thin] ({cx+w/2-0.25},{i*dh:.3f}) -- ({cx+w/2},{i*dh:.3f});')
    o.append(f'\\node[above] at ({cx},{h+0.05:.3f}) {{{cap} mL}}; \\node[below] at ({cx},-0.05) {{{nm}}};')
    return '\n'.join(o)
o=[beaker(0,sK,wK,Kcap,'K'),beaker(3.0,sL,wL,Lcap,'L')]
o.append('\\fill[gray!55] (4.7,2.5) rectangle (5.0,2.8); \\draw (4.7,2.5) rectangle (5.0,2.8); \\node[anchor=west] at (5.1,2.65) {şurup}; \\fill[vurgu!15] (4.7,1.9) rectangle (5.0,2.2); \\draw (4.7,1.9) rectangle (5.0,2.2); \\node[anchor=west] at (5.1,2.05) {su};')
SK=fig('\n'.join(o))
q('0007',tipId='ors-karisim',tip='Karışım kapları ve oran',z='orta',alt='Karışım Kapları',kaz='İki kaptaki şurup ve suyun hacmini okuyup istenen oran için eklenecek su miktarını bulur.',kalip='şekilli',
 kart='K-ORS-07 (karışım kapları) · K: 800 mL, L: 400 mL, 8 bölme',
 metin='Şekildeki K ve L kapları, üstlerinde yazılı kapasitelerle 8 eş bölmeye ayrılmıştır; kapların içinde şekilde görülen seviyelere kadar şurup ve su vardır. İki kabın içindekiler yeterince büyük, boş bir kaba boşaltılıp iyice karıştırılmıştır (hacimler toplanır). Daha sonra bu karışıma yalnız su eklenerek şurup hacminin su hacmine oranı 1/3 yapılacaktır.\nBuna göre, karışıma kaç mL su eklenmelidir?',
 dogru=v,yan=[(e[0],'L kabının bölmesini de K gibi 100 mL almış: şurup 400, su 700 mL; 3 × 400 − 700.','dikkat'),(e[1],'L kabındaki suyu hesaba katmamış: 900 − 300.','dikkat'),(e[2],'Oranı 1/4 almış: 4 × 300 − 500.','dikkat'),(e[3],'Karışımdaki mevcut suyu hesaba katmamış: gereken su miktarının tamamını eklenecek sanmış.','dikkat')],
 istenen='Eklenecek su miktarı (mL).',ip=['Her kabın bölme değerini kapasitesinden bul; şurup ve su hacimlerini ayrı ayrı topla.'],bilgi=[DO],sekil=SK,
 ad=[A('Bölme değerleri','Kapasite 8 bölmeye bölünür.','K: 800 ÷ 8 = 100 mL · L: 400 ÷ 8 = 50 mL'),A('Şurup hacmi','İki kaptaki şurup toplanır.','2 × 100 + 2 × 50 = 300 mL'),A('Su hacmi','İki kaptaki su toplanır.','3 × 100 + 4 × 50 = 500 mL'),A('Gereken su','Şurup/su = 1/3 ise su = 3 × şurup.','3 × 300 = 900 mL'),A('Eklenecek','Gereken sudan mevcut su çıkarılır.','900 − 500 = 400 mL')],
 puf='Önce bölme değerlerini bul; şurup değişmez, yalnız su eklenir.')

# ================= 08 orta · bölmeli şerit =================
bl=[4,5,9]; Lcm=30; bolme=Fr(Lcm,bl[1]); Mk=bl[2]*bolme; kes=Mk/3; tot=sum(bl)*bolme; v=tot-kes
e=[tot-Mk,(bl[0]+bl[1])*bolme+kes,tot-Lcm,tot]; assert bolme==6 and Mk==54 and kes==18 and tot==108 and v==90 and e==[54,72,78,108] and len({v,*e})==5
bw=0.4; o=[]; x=0
for nm,k in zip('KLM',bl):
    o.append(f'\\draw[thick] ({x*bw:.2f},0) rectangle ({(x+k)*bw:.2f},0.6);')
    for j in range(1,k): o.append(f'\\draw[thin] ({(x+j)*bw:.2f},0) -- ({(x+j)*bw:.2f},0.6);')
    o.append(f'\\node[above=2pt] at ({(x+k/2)*bw:.2f},0.6) {{{nm}}};'); x+=k
x1=bl[0]*bw; x2=(bl[0]+bl[1])*bw
o.append(f'\\draw[<->] ({x1:.2f},-0.35) -- ({x2:.2f},-0.35); \\node[below] at ({(x1+x2)/2:.2f},-0.35) {{30 cm}};')
SK=fig('\n'.join(o))
q('0008',tipId='ors-serit',tip='Bölmeli şerit ve parça oranları',z='orta',alt='Bölmeli Şerit',kaz='Eş bölmeli şeritte bir parçanın uzunluğundan bölme uzunluğunu bulup kesilen kısmı hesaplar.',kalip='şekilli',
 kart='K-ORS-08 (bölmeli şerit) · 4 + 5 + 9 bölme; L = 30 cm',
 metin='Şekildeki şerit K, L ve M parçalarından oluşmaktadır; çizgilerle ayrılan bölmelerin hepsi eşit uzunluktadır ve L parçasının uzunluğu 30 cm’dir. M parçasının uzunluğunun 1/3’ü kesilip atılıyor.\nBuna göre, geriye kalan şeridin toplam uzunluğu kaç cm’dir?',
 dogru=v,yan=[(e[0],'M’nin tamamını atmış: 108 − 54.','dikkat'),(e[2],'Atılan kısmı L parçası (30 cm) sanmış: 108 − 30.','dikkat'),(e[1],'Atılan 1/3 yerine M’nin yalnız 1/3’ünü saymış: K + L + M/3 = 54 + 18.','dikkat'),(e[3],'Kesim yapılmamış gibi şeridin tamamını yazmış.','dikkat')],
 istenen='Kalan şeridin toplam uzunluğu (cm).',ip=['L parçasındaki bölme sayısından bir bölmenin uzunluğunu bul; M’nin uzunluğuna geç.'],bilgi=[DO],sekil=SK,
 ad=[A('Bir bölme','L 5 bölmeden oluşur.','30 ÷ 5 = 6 cm'),A('M ve toplam','M 9 bölme, tüm şerit 4 + 5 + 9 = 18 bölmedir.','M = 54 cm · toplam = 108 cm'),A('Atılan kısım','M’nin 1/3’ü.','54 ÷ 3 = 18 cm'),A('Kalan','Toplamdan atılan çıkarılır.','108 − 18 = 90 cm')],
 puf='Bir bölmenin uzunluğunu bulunca bütün parçalar bölme sayısıyla hesaplanır.')

# ================= 09 zor · ölçekli kroki =================
cubuk_cm,cubuk_km=2,40; kmcm=Fr(cubuk_km,cubuk_cm); AB,BC=6,8; AC=int(math.hypot(AB,BC)); assert AC*AC==AB*AB+BC*BC
v=(AB+BC-AC)*kmcm
e=[AB*kmcm,AC*kmcm,(AB+BC)*kmcm,(AB+BC-AC)*cubuk_km]; assert kmcm==20 and v==80 and e==[120,200,280,160] and len({v,*e})==5
s=0.5; o=[f'\\draw[thick] (0,{AB*s}) -- (0,0) -- ({BC*s},0); \\draw[thin] (0.3,0) -- (0.3,0.3) -- (0,0.3);']
o.append(f'\\fill (0,{AB*s}) circle (0.07); \\fill (0,0) circle (0.07); \\fill ({BC*s},0) circle (0.07);')
o.append(f'\\node[left=3pt] at (0,{AB*s}) {{A}}; \\node[below left] at (0,0) {{B}}; \\node[right=3pt] at ({BC*s},0) {{C}};')
o.append(f'\\node[left=3pt] at (0,{AB*s/2}) {{{AB} cm}}; \\node[below=3pt] at ({BC*s/2},0) {{{BC} cm}};')
bx=5.2; by=2.6; o.append(f'\\draw[thick] ({bx},{by}) -- ({bx+cubuk_cm*s},{by}); \\draw[thick] ({bx},{by-0.1}) -- ({bx},{by+0.1}); \\draw[thick] ({bx+cubuk_cm*s},{by-0.1}) -- ({bx+cubuk_cm*s},{by+0.1});')
o.append(f'\\node[above=2pt] at ({bx+cubuk_cm*s/2},{by}) {{{cubuk_cm} cm}}; \\node[below=2pt] at ({bx+cubuk_cm*s/2},{by}) {{{cubuk_km} km}}; \\node[above=16pt] at ({bx+cubuk_cm*s/2},{by}) {{Ölçek}};')
SK=fig('\n'.join(o))
q('0009',tipId='ors-harita',tip='Ölçekli kroki',z='orta',alt='Ölçekli Kroki',kaz='Ölçek çubuğundan gerçek uzunlukları bulup dik üçgende iki yolu karşılaştırır.',kalip='şekilli',
 kart='K-ORS-09 (ölçekli kroki) · 2 cm = 40 km; 6 cm, 8 cm dik',
 metin='Şekildeki krokide A, B ve C kentleri ile bu kentler arasındaki yollar gösterilmiştir; A–B ve B–C yolları birbirine diktir, krokideki uzunluklar santimetre olarak verilmiş, ölçek ise yandaki ölçek çubuğuyla gösterilmiştir. A kentinden C kentine, B üzerinden giden yol yerine A ile C arasında doğrusal bir yol yapılırsa yol uzunluğu azalacaktır.\nBuna göre, yol kaç km kısalır?',
 dogru=v,yan=[(e[0],'Yalnız A–B yolunu hesaplamış: 6 × 20.','dikkat'),(e[1],'Doğrusal yolun uzunluğunu (10 × 20 = 200 km) fark sanmış.','dikkat'),(e[2],'Yalnız B üzerinden giden yolu hesaplamış: (6 + 8) × 20.','dikkat'),(e[3],'Ölçek çubuğunu 1 cm = 40 km okumuş: (14 − 10) × 40.','dikkat')],
 istenen='Yolun kısalma miktarı (km).',ip=['Önce krokideki 1 cm’in gerçekte kaç km olduğunu bul; A ile C arasındaki uzunluğu dik üçgenden hesapla.'],bilgi=[OL],sekil=SK,
 ad=[A('Ölçeği bul','Çubuk 2 cm = 40 km.','1 cm = 20 km'),A('B üzerinden yol','Krokideki uzunluklar toplanıp ölçekle çarpılır.','(6 + 8) × 20 = 280 km'),A('A–C uzunluğu','Dik üçgende Pisagor: 6² + 8² = 100.','AC = 10 cm → 200 km'),A('Fark','İki yolun farkı.','280 − 200 = 80 km')],
 puf='3-4-5 üçgeninin katları: 6-8-10.')

# ================= 10 zor · üç değişkenli tablo =================
u1,s1,g1=4,6,15; w=u1*s1*g1; u2,s2=5,8; a=Fr(w,u2*s2); s3,g3=5,12; b=Fr(w,s3*g3); v=a+b
e1=g1*Fr(u2,u1)*Fr(s2,s1)+b; e2=g1*Fr(u1,u2)+Fr(u1*g1,g3); e3=a+Fr(u1*g1,g3); e4=a*b
assert w==360 and a==9 and b==6 and v==15 and [e1,e2,e3,e4]==[31,17,14,54] and len({v,e1,e2,e3,e4})==5
SK=tablo_svg(['Durum','Usta sayısı','Günlük çalışma (saat)','Süre (gün)'],[['I',str(u1),str(s1),str(g1)],['II',str(u2),str(s2),'a'],['III','b',str(s3),str(g3)]])
q('0010',tipId='ors-tablo',tip='Ters orantı tablosu',z='zor',alt='Ters Orantı Tablosu',kaz='Üç çokluğun orantılı olduğu tabloda bilinmeyenleri bulur.',kalip='tablo',
 kart='K-ORS-10 (üç değişkenli tablo) · 4·6·15 = 5·8·a = b·5·12',
 metin='Eşit verimle çalışan ustalar, aynı bir işi üç farklı biçimde yapmıştır; her durumda işin tamamı bitirilmiştir. Çalışma bilgileri aşağıdaki tabloda verilmiştir.\nBuna göre, a + b toplamı kaçtır?',
 dogru=v,yan=[(e1,'II. durumda usta ve saati doğru orantılı sanmış: a = 15 × 5/4 × 8/6 = 25; b’yi doğru bulmuş: 25 + 6.','dikkat'),(e2,'Günlük saati hiç hesaba katmamış: a = 15 × 4/5 = 12 ve b = 4 × 15/12 = 5; 12 + 5.','dikkat'),(e3,'a’yı doğru (9) bulmuş, b’de günlük saati hesaba katmamış: 4 × 15/12 = 5; 9 + 5.','dikkat'),(e4,'Toplam yerine çarpımı almış: 9 × 6.','islem')],
 istenen='a + b toplamı.',ip=['Her satırda usta sayısı, günlük saat ve gün sayısının çarpımı işin büyüklüğünü verir; ilk satırdan işin tamamını bul.'],bilgi=[TO],sekil=SK,
 ad=[A('İşin büyüklüğü','Usta × saat × gün sabittir.','4 × 6 × 15 = 360'),A('a’yı bul','II. durumda aynı iş yapılır.','5 × 8 × a = 360 → a = 9'),A('b’yi bul','III. durumda aynı iş yapılır.','b × 5 × 12 = 360 → b = 6'),A('Topla','a ve b toplanır.','9 + 6 = 15')],
 puf='Usta, saat ve gün: üçünün çarpımı sabit; işi bu çarpım ölçer.')

bitir(P,'oransek','mat|Oran Orantı')
