"""İşçi Emek Problemleri · ŞEKİLLİ paket (8 soru): şekil/tablo/grafik çözüm verisini taşır; sayılar Python'da hesaplanır, her doğru ve çeldirici değer assert'lidir. Kardeş yok, ipucu 1."""
import sys,os,math
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
H.KONU='İşçi Emek Problemleri'
UK='prob|İşçi Emek Problemleri'
P=Parti('iscisek','İşçi Emek Problemleri',UK)
KY='ÖSYM 2018–2026 TYT Matematik (şekilli/tablolu/grafikli işçi-emek soruları; yalnız mantık) · MEB 9. sınıf problemler'
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)
def fig(body): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'+body+'\n\\end{tikzpicture}')
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)

HIZ=B('İş ve günlük hız','bir iş t zamanda bitiyorsa birim zamanda işin 1/t’si yapılır; çalışılan süreyle çarpılınca yapılan iş kesri bulunur. Örnek: 5 günde biten işte 2 gün çalışan işin 2/5’ini yapar')
DEPO=B('Doldurma ve boşaltma','dolduran borunun birim zamandaki payı toplanır, boşaltanınki çıkarılır; kalan miktar bu net paya bölünür. Örnek: bir kabı 2 saatte dolduran ve 5 saatte boşaltan borular birlikte çalışınca saatte 1/2 − 1/5 = 3/10 dolar')
GRF=B('İş–zaman grafiği','orijinden geçen doğru sabit hızı gösterir; yapılan iş süreyle doğru orantılıdır. Örnek: 2 saatte işin %10’unu yapan kişi 6 saatte %30’unu yapar')
BIR=B('Birlikte çalışma','birlikte çalışanların birim zamandaki payları toplanır; işin tamamı 1 alınırsa süre = 1 ÷ toplam pay. Örnek: işi 4 ve 12 günde bitirenler birlikte 1/4 + 1/12 = 1/3 ile 3 günde bitirir')
CIZ=B('Çalışma çizelgesi','çizelgede her çubuk bir işçinin çalıştığı günleri gösterir; bir işçinin yaptığı iş = çalıştığı gün sayısı × günlük payı. İş tamamlandığında bölümlerin toplamı 1 olur. Örnek: 10 günde bitirenin 4 gün çalışması işin 2/5’idir')
ISG=B('İşçi–gün','eş verimli işçilerde iş = işçi sayısı × gün sayısı (işçi-gün). Örnek: 5 işçi 8 günde bitiriyorsa iş 40 işçi-gündür; 10 işçi bu işi 4 günde bitirir')
FRK=B('Farklı verimli işçiler','işçilerin birim zamandaki payları farklıysa iş = (toplam pay) × süre; aynı iş iki farklı durumda yapılıyorsa iki durumdaki çarpımlar eşitlenir. Örnek: 1 usta + 1 kalfa 4 günde, 1 usta + 3 kalfa 3 günde bitiriyorsa 4u + 4k = 3u + 9k')

# ---------- kartlar ----------
kartla('K-ISS-01','İlerleme çubuğu','Eş bölümlü çubuktan tamamlanan kesir okunur; geçen süre bu kesre bölünerek birim hız, kalan bölümle çarpılarak kalan süre bulunur.','Toplam süreyi kalan süre sanmak; geçen süreyi tekrar yazmak.','kolay','hikâyeli',3,'iss-cubuk','İlerleme çubuğu ve kalan süre')
kartla('K-ISS-02','İş–zaman grafiği (tek işçi)','Grafikteki bir noktadan işin birim zamandaki yüzdesi bulunur; istenen yüzdeye ulaşma süresi orantıyla hesaplanır.','Yüzdeyi saat gibi kullanmak; toplamsal düşünmek.','kolay','grafik',3,'iss-grafik','İş–zaman grafiği ve orantı')
kartla('K-ISS-03','Kısmen dolu depo','Depodaki dolu bölme sayısından kalan kesir bulunur; dolduran ve boşaltan boruların net payıyla bölünür.','Boşaltanı hesaba katmamak; kalan yerine dolu kısmı kullanmak.','orta','hikâyeli',4,'iss-depo','Doldurma–boşaltma düzeneği')
kartla('K-ISS-04','Çalışma çizelgesi','Çizelgeden her işçinin çalıştığı gün sayısı okunur; bilinen işçilerin yaptığı iş toplamının tamamlayıcısı bilinmeyen işçiye aittir.','Gün sayısını uç noktalardan yanlış saymak; bölümlerden birini atlamak.','orta','hikâyeli',4,'iss-takvim','Çalışma çizelgesi')
kartla('K-ISS-05','İki işçinin iş–zaman grafiği','Her doğrudan işçinin tek başına süresi bulunur; paylar toplanarak birlikte çalışma süresi hesaplanır.','Sürelerin ortalamasını almak; süreleri toplamak.','orta','grafik',4,'iss-grafik2','İki doğrulu iş–zaman grafiği')
kartla('K-ISS-06','Makine tablosu','Tabloda her makinenin üretimi saatlik üretim × süre ile bulunur; toplam siparişten çıkarılan miktar bilinmeyen makineye düşer.','Bir makineyi atlamak; kalan üretimi saatlik hıza bölmeyi unutmak.','kolay','tablo',4,'iss-makine','Makine üretim tablosu')
kartla('K-ISS-07','Aşamalı çalışma çizelgesi','İş, işçi-gün biriminde ifade edilir; çizelgedeki aşamalarda yapılan iş çıkarılır, kalan iş son aşamanın işçi sayısına bölünür.','Aşama değişimini hesaba katmamak; gecikme yerine bitiş gününü yazmak.','zor','hikâyeli',5,'iss-ekip','Aşamalı işçi çizelgesi')
kartla('K-ISS-08','Usta ve kalfa tablosu','İki durumdaki işçi–gün toplamları eşitlenerek usta ve kalfanın verimi arasındaki oran bulunur; iş bu orana göre ifade edilir.','Bütün işçileri eşit verimli saymak; yalnız bir durumu kullanmak.','zor','tablo',5,'iss-tablo','Farklı verimli işçiler tablosu')

# ================= 01 kolay · ilerleme çubuğu =================
n,dolu,gecen=10,4,3; hiz=Fr(dolu,gecen); toplam=Fr(n)/hiz; v=toplam-gecen
e=[toplam,Fr(gecen),Fr(dolu),Fr(gecen*dolu,n)]
assert v==Fr(9,2) and e==[Fr(15,2),3,4,Fr(6,5)] and len({v,*e})==5
o=[]; w=0.55
for i in range(n):
    o.append(f'\\filldraw[fill={"vurgu!35" if i<dolu else "white"},draw=black] ({i*w:.2f},0) rectangle ({(i+1)*w:.2f},0.7);')
o.append(f'\\draw[very thick] (0,0) rectangle ({n*w},0.7);')
o.append(f'\\node[above=3pt,anchor=south west] at (0,0.7) {{Cam cephe (eş bölümlere ayrılmıştır)}};')
o.append(f'\\node[below=5pt,anchor=north west] at (0,0) {{Robotun çalışma süresi: {gecen} saat}};')
o.append(f'\\filldraw[fill=vurgu!35] (0,-1.05) rectangle (0.3,-0.75); \\node[anchor=west] at (0.4,-0.9) {{silinen bölüm}};')
SK=fig('\n'.join(o))
q('0001',tipId='iss-cubuk',tip='İlerleme çubuğu ve kalan süre',z='kolay',alt='İlerleme Çubuğu',kaz='Çubuktan tamamlanan kesri okuyup işin kalan süresini hesaplar.',kalip='hikâyeli',
 kart='K-ISS-01 (ilerleme çubuğu) · 4/10 bölüm, 3 saat',
 metin='Bir gökdelenin cam cephesi, sabit hızla çalışan bir temizlik robotuyla silinmektedir. Şekilde, cephenin eş bölümlere ayrılmış hâli ve robotun çalışmaya başlamasından bir süre sonraki durum gösterilmiştir. Robot aynı hızla çalışmaya devam edecektir.\nBuna göre, cephenin tamamı silininceye kadar robot daha kaç saat çalışır?',
 dogru=v,yan=[(e[0],'Cephenin tamamının süresini (10 ÷ 4/3 = 7,5 saat) bulup geçen süreyi çıkarmamış.','dikkat'),(e[1],'Kalan sürenin geçen süreye eşit olduğunu sanmış.','dikkat'),(e[2],'Silinen bölüm sayısını (4) saat olarak yazmış.','dikkat'),(e[3],'Geçen süreyi silinen kesirle çarpmış: 3 × 4/10.','islem')],
 istenen='Robotun kalan çalışma süresi (saat).',ip=['Şekilde silinen ve silinmeyen bölüm sayılarını say; robotun bir saatte kaç bölüm sildiğini düşün.'],bilgi=[HIZ],sekil=SK,
 ad=[A('Hızı bul','Şekilden silinen bölüm sayısı ve geçen süre okunur.','4 bölüm 3 saatte → saatte 4/3 bölüm'),A('Kalan bölüm','Toplamdan silinen çıkarılır.','10 − 4 = 6 bölüm'),A('Süreyi bul','Kalan bölüm hıza bölünür.','6 ÷ 4/3 = 4,5 saat')],
 puf='Önce bir saatte kaç bölüm silindiğini bul; kalan bölümü buna böl.')

# ================= 02 kolay · iş–zaman grafiği =================
nk,nv=5,40; tam=Fr(nk*100,nv); hedef=80; v=Fr(nk*hedef,nv)
e=[tam,nk+(hedef-nv),Fr(nk*hedef,100),Fr(nk*(100-hedef),nv)]
assert v==10 and e==[Fr(25,2),45,4,Fr(5,2)] and len({v,*e})==5
sx,sy=0.55,0.036
o=[f'\\draw[-{{Stealth}}] (0,0) -- ({12.6*sx:.2f},0) node[right] {{Süre (saat)}};',f'\\draw[-{{Stealth}}] (0,0) -- (0,{108*sy:.2f}) node[above] {{Tamamlanan iş (\\%)}};']
for k in range(1,13): o.append(f'\\draw ({k*sx:.2f},-0.06) -- ({k*sx:.2f},0.06); \\node[below=2pt] at ({k*sx:.2f},0) {{\\footnotesize {k}}};')
for t in (20,40,60,80,100): o.append(f'\\draw[gray!40] (0,{t*sy:.2f}) -- ({12*sx:.2f},{t*sy:.2f}); \\node[left=2pt] at (0,{t*sy:.2f}) {{\\footnotesize {t}}};')
o.append(f'\\draw[very thick] (0,0) -- ({nk*sx:.2f},{nv*sy:.2f}); \\fill ({nk*sx:.2f},{nv*sy:.2f}) circle (0.07);')
o.append(f'\\draw[dashed] ({nk*sx:.2f},0) -- ({nk*sx:.2f},{nv*sy:.2f}) -- (0,{nv*sy:.2f});')
SK=fig('\n'.join(o))
q('0002',tipId='iss-grafik',tip='İş–zaman grafiği ve orantı',z='kolay',alt='İş–Zaman Grafiği',kaz='İş–zaman grafiğindeki işaretli noktadan hız bulup istenen yüzdeye ulaşma süresini hesaplar.',kalip='grafik',
 kart='K-ISS-02 (iş–zaman grafiği) · 5 saatte %40; hedef %80',
 metin='Şekildeki grafik, bir terzinin okul forması siparişini dikerken geçen süre ile tamamladığı işin yüzdesi arasındaki ilişkiyi göstermektedir. Terzi sabit hızla çalışmaktadır ve grafikteki doğru, çalışmanın başından itibaren çizilmiştir.\nBuna göre, terzi siparişin %80’ini kaç saatte tamamlar?',
 dogru=v,yan=[(e[0],'Siparişin tamamının süresini (5 × 100 ÷ 40) bulmuş.','dikkat'),(e[1],'Toplamsal düşünmüş: yüzde 40 artınca süreyi de 40 artırmış: 5 + 40.','dikkat'),(e[2],'Yüzdeyi saat gibi kullanmış: 5 × 80 ÷ 100.','islem'),(e[3],'Kalan yüzdeyi (100 − 80 = 20) kullanıp 5 × 20 ÷ 40 hesaplamış.','dikkat')],
 istenen='Siparişin %80’inin tamamlanma süresi (saat).',ip=['Grafikte işaretli noktanın saat ve yüzde değerlerini oku; bir saatte işin yüzde kaçı yapılıyor?'],bilgi=[GRF],sekil=SK,
 ad=[A('Noktayı oku','İşaretli noktada süre ve yüzde okunur.','5 saat → %40'),A('Saatlik iş','Yüzde süreye bölünür.','40 ÷ 5 = saatte %8'),A('Süreyi bul','İstenen yüzde saatlik işe bölünür.','80 ÷ 8 = 10 saat')],
 puf='Orijinden geçen doğruda yüzde ÷ saat her noktada aynıdır.')

# ================= 03 orta · kısmen dolu depo =================
tA,tB,tC=6,12,8; nb,dl=8,3; kalan=Fr(nb-dl,nb); net=Fr(1,tA)+Fr(1,tB)-Fr(1,tC); v=kalan/net
e=[kalan/(Fr(1,tA)+Fr(1,tB)),Fr(dl,nb)/net,Fr(1)/net,kalan*(tA+tB-tC)]
assert net==Fr(1,8) and v==5 and e==[Fr(5,2),3,8,Fr(25,4)] and len({v,*e})==5
dh=0.36; w=1.5; o=[]
o.append(f'\\fill[vurgu!15] (0,0) rectangle ({w},{dl*dh:.2f});')
o.append(f'\\draw[line width=1.4pt] (0,{nb*dh:.2f}) -- (0,0) -- ({w},0) -- ({w},{nb*dh:.2f});')
for i in range(1,nb): o.append(f'\\draw[thin,gray] (0,{i*dh:.2f}) -- ({w},{i*dh:.2f});')
o.append(f'\\node[above] at ({w/2},{nb*dh+0.05:.2f}) {{Sulama deposu}};')
o.append(f'\\node[below=3pt] at ({w/2},0) {{\\footnotesize 8 eş bölme}};')
# doldurma boruları (sol), boşaltma borusu (sağ alt)
o.append(f'\\draw[line width=3pt,gray] (-2.2,{nb*dh-0.35:.2f}) -- (0.5,{nb*dh-0.35:.2f}); \\draw[-{{Stealth}},thick] (0.2,{nb*dh-0.35:.2f}) -- (0.55,{nb*dh-0.35:.2f});')
o.append(f'\\node[anchor=east,align=right] at (-2.3,{nb*dh-0.35:.2f}) {{A: boş depoyu\\\\{tA} saatte doldurur}};')
o.append(f'\\draw[line width=3pt,gray] (-2.2,{nb*dh-1.25:.2f}) -- (0.5,{nb*dh-1.25:.2f}); \\draw[-{{Stealth}},thick] (0.2,{nb*dh-1.25:.2f}) -- (0.55,{nb*dh-1.25:.2f});')
o.append(f'\\node[anchor=east,align=right] at (-2.3,{nb*dh-1.25:.2f}) {{B: boş depoyu\\\\{tB} saatte doldurur}};')
o.append(f'\\draw[line width=3pt,gray] ({w-0.3},0.18) -- ({w+2.0},0.18); \\draw[-{{Stealth}},thick] ({w+1.4},0.18) -- ({w+1.8},0.18);')
o.append(f'\\node[anchor=west,align=left] at ({w+0.15},1.05) {{C: dolu depoyu\\\\{tC} saatte boşaltır}};')
SK=fig('\n'.join(o))
q('0003',tipId='iss-depo',tip='Doldurma–boşaltma düzeneği',z='orta',alt='Sulama Deposu',kaz='Kısmen dolu bir depoyu dolduran ve boşaltan borularla birlikte tamamen dolduracak süreyi hesaplar.',kalip='hikâyeli',
 kart='K-ISS-03 (kısmen dolu depo) · 3/8 dolu; 1/6 + 1/12 − 1/8',
 metin='Bir seranın sulama deposu ile deponun A ve B doldurma boruları ve C boşaltma borusu şekilde gösterilmiştir; her borunun yanında deponun tamamını tek başına ne kadar sürede doldurduğu ya da boşalttığı yazılıdır. Depo, şekildeki seviyeye kadar su doluyken üç boru da aynı anda açılıyor ve boruların debileri sabittir.\nBuna göre, depo kaç saat sonra tamamen dolar?',
 dogru=v,yan=[(e[0],'Boşaltma borusunu hesaba katmamış: kalan 5/8’i A ile B’nin birlikte payına (1/4) bölmüş.','dikkat'),(e[1],'Kalan kesir yerine dolu kısmı (3/8) kullanmış: (3/8) ÷ (1/8).','dikkat'),(e[2],'Depoyu boşken başlıyormuş gibi hesaplamış: 1 ÷ (1/8).','dikkat'),(e[3],'Süreleri 6 + 12 − 8 = 10 diye işleme sokup kalan 5/8 ile çarpmış.','islem')],
 istenen='Deponun tamamen dolma süresi (saat).',ip=['Şekilde seviyeyi eş bölmelerden say; boruların bir saatte deponun ne kadarını doldurduğunu ya da boşalttığını ayrı ayrı düşün.'],bilgi=[DEPO],sekil=SK,
 ad=[A('Kalan kesri bul','Dolu bölmeler sayılır; boş kalan kısım hesaplanır.','8 bölmenin 3’ü dolu → kalan 5/8'),A('Net payı bul','Dolduranlar toplanır, boşaltan çıkarılır.','1/6 + 1/12 − 1/8 = 4/24 + 2/24 − 3/24 = 3/24 = 1/8'),A('Süreyi bul','Kalan kesir net paya bölünür.','(5/8) ÷ (1/8)'),A('Sonuç','Bölme yapılır.','5 saat')],
 puf='Önce depoda kalan boşluğu kesir olarak yaz; sonra boruların birlikte saatlik etkisini bul.')

# ================= 04 orta · çalışma çizelgesi =================
sA,sB=12,24
dA=(0,6); dB=(3,9); dC=(6,10); pa=Fr(dA[1]-dA[0],12); pb=Fr(dB[1]-dB[0],24); pc=1-pa-pb; gc=dC[1]-dC[0]; v=Fr(gc)/pc
e=[Fr(gc)/(1-pa),Fr(gc+1)/pc,Fr(gc)/(1-pa-Fr(dB[1],24)),Fr(dC[1])/pc]
assert pa==Fr(1,2) and pb==Fr(1,4) and pc==Fr(1,4) and gc==4 and v==16 and e==[8,20,32,40] and len({v,*e})==5
bw=0.5; o=[]
rows=[('Ali','tek başına 12 gün',dA),('Bora','tek başına 24 gün',dB),('Cem','',dC)]
for i,(ad_,alt_,(s,t)) in enumerate(rows):
    y=-i*0.9
    o.append(f'\\filldraw[fill=vurgu!30,draw=black,thick] ({s*bw:.2f},{y-0.28:.2f}) rectangle ({t*bw:.2f},{y+0.28:.2f});')
    lab=f'{ad_}\\\\{{\\footnotesize {alt_}}}' if alt_ else ad_
    o.append(f'\\node[anchor=east,align=right] at (-0.15,{y:.2f}) {{{lab}}};')
o.append('\\draw[-{Stealth}] (0,-2.3) -- ('+f'{10.8*bw:.2f}'+',-2.3) node[right] {Gün};')
for d in range(0,11): o.append(f'\\draw ({d*bw:.2f},-2.3) -- ({d*bw:.2f},-2.2); \\node[below=1pt] at ({d*bw:.2f},-2.3) {{\\footnotesize {d}}};')
o.append(f'\\draw[dashed] ({10*bw:.2f},0.45) -- ({10*bw:.2f},-2.3); \\node[above] at ({10*bw:.2f},0.45) {{\\footnotesize iş bitti}};')
SK=fig('\n'.join(o))
q('0004',tipId='iss-takvim',tip='Çalışma çizelgesi',z='orta',alt='Çalışma Çizelgesi',kaz='Çalışma çizelgesindeki gün aralıklarından üçüncü işçinin tek başına süresini bulur.',kalip='hikâyeli',
 kart='K-ISS-04 (çalışma çizelgesi) · Ali 6 gün/12, Bora 6 gün/24, Cem 4 gün',
 metin='Bir bahçe duvarının örülmesinde üç usta, şekildeki çizelgede gösterilen günlerde çalışmıştır; çubuğun başladığı ve bittiği günler, ustanın o günler boyunca çalıştığını gösterir. Her usta çalıştığı sürece sabit hızla çalışmış, iş çizelgedeki son günde tam olarak bitmiştir.\nBuna göre, Cem bu duvarı tek başına kaç günde örer?',
 dogru=v,yan=[(e[0],'Bora’nın yaptığı işi hesaba katmamış: Ali’den kalan 1/2’yi Cem’in 4 gününe bağlamış.','dikkat'),(e[1],'Cem’in çalıştığı günleri 6’dan 10’a kadar 5 gün saymış.','dikkat'),(e[2],'Bora’yı 0’dan 9. güne kadar çalışmış (9 gün) sanıp 9/24’ünü yapmış saymış.','dikkat'),(e[3],'Cem’in işin başından bitişine kadar 10 gün çalıştığını sanmış.','dikkat')],
 istenen='Cem’in tek başına örme süresi (gün).',ip=['Çizelgede her çubuğun uzunluğundan çalışılan gün sayısını bul; Ali ve Bora’nın işin ne kesrini yaptığını hesapla.'],bilgi=[CIZ],sekil=SK,
 ad=[A('Ali’nin işi','Ali 6 gün çalışmıştır.','6 ÷ 12 = 1/2'),A('Bora’nın işi','Bora 6 gün çalışmıştır.','6 ÷ 24 = 1/4'),A('Cem’in işi','İşin tamamından çıkarılır.','1 − 1/2 − 1/4 = 1/4'),A('Cem’in süresi','Cem 4 günde işin 1/4’ünü yapmıştır.','4 ÷ (1/4) = 16 gün')],
 puf='Her ustanın payı = çalıştığı gün ÷ tek başına süresi; paylar toplanınca 1 eder.')

# ================= 05 orta · iki işçinin iş–zaman grafiği =================
ek,ev=4,40; ok_,ov=3,50; tE=Fr(ek*100,ev); tO=Fr(ok_*100,ov); v=1/(1/tE+1/tO)
e=[(tE+tO)/2,tE+tO,tE*tO/(tE-tO),tE-tO]
assert tE==10 and tO==6 and v==Fr(15,4) and e==[8,16,15,4] and len({v,*e})==5
sx,sy=0.62,0.036
o=[f'\\draw[-{{Stealth}}] (0,0) -- ({7.6*sx:.2f},0) node[right] {{Süre (saat)}};',f'\\draw[-{{Stealth}}] (0,0) -- (0,{108*sy:.2f}) node[above] {{Tamamlanan iş (\\%)}};']
for k in range(1,8): o.append(f'\\draw ({k*sx:.2f},-0.06) -- ({k*sx:.2f},0.06); \\node[below=2pt] at ({k*sx:.2f},0) {{\\footnotesize {k}}};')
for t in (20,40,60,80,100): o.append(f'\\draw[gray!40] (0,{t*sy:.2f}) -- ({7*sx:.2f},{t*sy:.2f}); \\node[left=2pt] at (0,{t*sy:.2f}) {{\\footnotesize {t}}};')
xe,xo=6.0,4.5
o.append(f'\\draw[very thick] (0,0) -- ({xe*sx:.2f},{float(xe*Fr(ev,ek))*sy:.2f}) node[right,fill=white,inner sep=1pt] {{Ece}};')
o.append(f'\\draw[very thick,dashed] (0,0) -- ({xo*sx:.2f},{float(xo*Fr(ov,ok_))*sy:.2f}) node[above right,fill=white,inner sep=1pt] {{Okan}};')
for (x,y) in ((ek,ev),(ok_,ov)):
    o.append(f'\\fill ({x*sx:.2f},{y*sy:.2f}) circle (0.07); \\draw[dotted] ({x*sx:.2f},0) -- ({x*sx:.2f},{y*sy:.2f}) -- (0,{y*sy:.2f});')
SK=fig('\n'.join(o))
q('0005',tipId='iss-grafik2',tip='İki doğrulu iş–zaman grafiği',z='orta',alt='İki İşçi Grafiği',kaz='İki işçinin iş–zaman grafiğinden tek başına sürelerini bulup birlikte çalışma süresini hesaplar.',kalip='grafik',
 kart='K-ISS-05 (iki işçi grafiği) · (4 sa, %40) ve (3 sa, %50)',
 metin='Şekildeki grafikte Ece ile Okan’ın, bir kütüphanenin kitap etiketleme işinde ayrı ayrı çalıştıklarında geçen süreye göre tamamladıkları işin yüzdesi gösterilmiştir. İkisi de sabit hızla çalışmaktadır. Ece ile Okan bu işe aynı anda başlayıp birlikte çalışırsa iş bitene kadar hızları değişmemektedir.\nBuna göre, iki kişi birlikte işi kaç saatte bitirir?',
 dogru=v,yan=[(e[0],'Tek başına sürelerin ortalamasını almış: (10 + 6) ÷ 2.','dikkat'),(e[1],'Tek başına süreleri toplamış: 10 + 6.','dikkat'),(e[2],'Hız toplamı yerine hız farkını kullanmış: 10 × 6 ÷ (10 − 6).','dikkat'),(e[3],'Tek başına süreler arasındaki farkı almış: 10 − 6.','dikkat')],
 istenen='Birlikte çalışma süresi (saat).',ip=['Her doğruda işaretli noktayı oku; iki kişinin tek başına süresini ve bir saatte yaptıkları işin kesrini ayrı ayrı bul.'],bilgi=[BIR],sekil=SK,
 ad=[A('Ece’nin süresi','İşaretli nokta okunur: saatlik pay.','4 saatte %40 → tamamı 10 saat'),A('Okan’ın süresi','İşaretli nokta okunur.','3 saatte %50 → tamamı 6 saat'),A('Saatlik paylar','Paylar toplanır.','1/10 + 1/6 = 3/30 + 5/30 = 8/30 = 4/15'),A('Süre','1 ÷ toplam pay.','1 ÷ (4/15) = 15/4 = 3,75 saat')],
 puf='Tek başına süreleri bulup saatlik payları topla.')

# ================= 06 orta · makine tablosu =================
uA,hA,uB,hB,uC,sip=40,5,30,8,20,700; prod=uA*hA+uB*hB; v=Fr(sip-prod,uC)
e=[Fr(sip,uC),Fr(sip-uA*hA,uC),Fr(sip-uB*hB,uC),sip-prod]
assert prod==440 and v==13 and e==[35,25,23,260] and len({v,*e})==5
SK=tablo_svg(['Makine','Saatlik üretim (adet)','Çalışma süresi (saat)'],[['A',str(uA),str(hA)],['B',str(uB),str(hB)],['C',str(uC),'?']])
q('0006',tipId='iss-makine',tip='Makine üretim tablosu',z='kolay',alt='Makine Tablosu',kaz='Tablodaki üretim bilgilerinden bilinmeyen makinenin çalışma süresini bulur.',kalip='tablo',
 kart='K-ISS-06 (makine tablosu) · 40×5 + 30×8 + 20×x = 700',
 metin='Bir tekstil atölyesi, 700 adetlik bir tişört siparişini üç dikiş makinesiyle hazırlamıştır. Makinelerin saatlik üretimleri ve çalışma süreleri aşağıdaki tabloda verilmiştir; makineler sabit hızla çalışmıştır ve siparişin tamamı üretilmiştir.\nBuna göre, C makinesi kaç saat çalışmıştır?',
 dogru=v,yan=[(e[0],'A ve B’nin üretimini hesaba katmamış: 700 ÷ 20.','dikkat'),(e[1],'B makinesinin üretimini atlamış: (700 − 200) ÷ 20.','dikkat'),(e[2],'A makinesinin üretimini atlamış: (700 − 240) ÷ 20.','dikkat'),(e[3],'Kalan üretimi (260) C’nin saatlik üretimine bölmeyi unutmuş.','islem')],
 istenen='C makinesinin çalışma süresi (saat).',ip=['Siparişin ne kadarının A ve B tarafından hazırlandığını düşün.'],bilgi=[HIZ],sekil=SK,
 ad=[A('A’nın üretimi','Saatlik üretim × süre.','40 × 5 = 200 adet'),A('B’nin üretimi','Saatlik üretim × süre.','30 × 8 = 240 adet'),A('C’nin üretimi','Siparişten çıkarılır.','700 − 440 = 260 adet'),A('C’nin süresi','Üretim saatlik üretime bölünür.','260 ÷ 20 = 13 saat')],
 puf='Önce hazır olan üretimi topla; kalanı üreten makinenin saatlik hızına böl.')

# ================= 07 zor · aşamalı işçi çizelgesi =================
n1,T=15,16; W=n1*T; a1=(0,4,15); a2=(4,8,9); n3=12
rem=W-a1[2]*(a1[1]-a1[0])-a2[2]*(a2[1]-a2[0]); d3=Fr(rem,n3); fin=a2[1]+d3; v=fin-T
r2=W-a1[2]*(a1[1]-a1[0]); e=[d3,fin,Fr(W-a1[2]*(a1[1]-a1[0])-n1*(a2[1]-a2[0]),n3)+a2[1]-T,Fr(r2,n3)+a2[1]-T]
assert rem==144 and d3==12 and fin==20 and v==4 and e==[12,20,2,7] and len({v,*e})==5
bw=0.36; o=[]
for i,(nm,s,t,k) in enumerate([('1. aşama',0,4,15),('2. aşama',4,8,9)]):
    y=-i*0.9
    o.append(f'\\filldraw[fill=vurgu!30,draw=black,thick] ({s*bw:.2f},{y-0.28:.2f}) rectangle ({t*bw:.2f},{y+0.28:.2f}); \\node at ({(s+t)/2*bw:.2f},{y:.2f}) {{\\footnotesize {k} işçi}};')
    o.append(f'\\node[anchor=east] at (-0.15,{y:.2f}) {{{nm}}};')
y=-1.8; s3=8; t3=17.2
o.append(f'\\filldraw[fill=vurgu!30,draw=none] ({s3*bw:.2f},{y-0.28:.2f}) rectangle ({t3*bw:.2f},{y+0.28:.2f});')
o.append(f'\\draw[thick] ({t3*bw:.2f},{y+0.28:.2f}) -- ({s3*bw:.2f},{y+0.28:.2f}) -- ({s3*bw:.2f},{y-0.28:.2f}) -- ({t3*bw:.2f},{y-0.28:.2f});')
o.append(f'\\draw[thick,decorate,decoration={{zigzag,segment length=4pt,amplitude=1.2pt}}] ({t3*bw:.2f},{y+0.28:.2f}) -- ({t3*bw:.2f},{y-0.28:.2f});')
o.append(f'\\node at ({(s3+t3-1.5)/2*bw:.2f},{y:.2f}) {{\\footnotesize {n3} işçi}}; \\node[anchor=east] at (-0.15,{y:.2f}) {{3. aşama}};')
o.append(f'\\node[below] at ({(s3+t3)/2*bw:.2f},{y-0.3:.2f}) {{\\footnotesize iş bitene kadar}};')
yy=-2.95; o.append(f'\\draw[-{{Stealth}}] (0,{yy}) -- ({18.2*bw:.2f},{yy}) node[right] {{Gün}};')
for d in (0,4,8,12,16): o.append(f'\\draw ({d*bw:.2f},{yy}) -- ({d*bw:.2f},{yy+0.1}); \\node[below=1pt] at ({d*bw:.2f},{yy}) {{\\footnotesize {d}}};')
SK=fig('\n'.join(o))
q('0007',tipId='iss-ekip',tip='Aşamalı işçi çizelgesi',z='zor',alt='Aşamalı İşçi Çizelgesi',kaz='İşçi-gün hesabıyla işçi sayısı değişen bir işin gecikme süresini bulur.',kalip='hikâyeli',
 kart='K-ISS-07 (aşamalı çizelge) · 15 işçi × 16 gün = 240 işçi-gün',
 metin='Bir apartmanın dış sıva işi, eşit verimle çalışan 15 işçiyle 16 günde bitirilecek şekilde planlanmıştır. İş başladıktan sonra işçi sayısı değişmiş; şekilde işin aşamaları, her aşamadaki işçi sayısı ve aşamaların hangi günler arasında sürdüğü gösterilmiştir. Üçüncü aşama, iş bitene kadar sürmüştür.\nBuna göre, iş planlanan günden kaç gün geç bitmiştir?',
 dogru=v,yan=[(e[0],'Gecikme yerine üçüncü aşamanın süresini (12 gün) yazmış.','dikkat'),(e[1],'Gecikme yerine işin bittiği günü (20. gün) yazmış.','dikkat'),(e[2],'İkinci aşamada da 15 işçinin çalıştığını sanmış: üçüncü aşama 120 ÷ 12 = 10 gün sürmüş, bitiş 18. gün.','dikkat'),(e[3],'İkinci aşamadaki işi hiç saymamış: üçüncü aşama 180 ÷ 12 = 15 gün sürmüş, bitiş 23. gün.','dikkat')],
 istenen='İşin planlanan günden geç bitme süresi (gün).',ip=['Şekildeki ilk iki aşamada yapılan işi işçi-gün olarak hesapla.'],bilgi=[ISG],sekil=SK,
 ad=[A('İşin tamamı','Planlanan işçi sayısı × gün.','15 × 16 = 240 işçi-gün'),A('1. aşama','İşçi sayısı × aşamanın uzunluğu (0–4. gün).','15 × 4 = 60 işçi-gün'),A('2. aşama','4–8. günler arası.','9 × 4 = 36 işçi-gün'),A('3. aşama','Kalan iş son aşamanın işçi sayısına bölünür.','(240 − 60 − 36) ÷ 12 = 12 gün → bitiş 8 + 12 = 20. gün'),A('Gecikme','Bitiş günü, planlanan günden çıkarılır.','20 − 16 = 4 gün')],
 puf='Tüm işi işçi-gün olarak yaz, her aşamada yapılanı çıkar.')

# ================= 08 zor · usta–kalfa tablosu =================
u,k=7,2; r1=(4,2,6); r2=(2,5,8); W=(r1[0]*u+r1[1]*k)*r1[2]; assert W==(r2[0]*u+r2[1]*k)*r2[2]==192
assert (r1[0]*Fr(7,2)+r1[1])*r1[2]==(r2[0]*Fr(7,2)+r2[1])*r2[2]  # oran u = 3,5 k
v=Fr(W,4*k)
e=[Fr((r1[0]+r1[1])*r1[2],4),Fr((r2[0]+r2[1])*r2[2],4),Fr(W,16),Fr(W,r2[1]*k)]
assert v==24 and e==[9,14,12,Fr(96,5)] and len({v,*e})==5
SK=tablo_svg(['Durum','Usta sayısı','Kalfa sayısı','Süre (gün)'],[['I',str(r1[0]),str(r1[1]),str(r1[2])],['II',str(r2[0]),str(r2[1]),str(r2[2])]])
q('0008',tipId='iss-tablo',tip='Farklı verimli işçiler tablosu',z='zor',alt='Usta ve Kalfa Tablosu',kaz='Farklı verimli işçilerin iki durumdaki çalışma bilgisinden yalnız kalfaların çalışma süresini bulur.',kalip='tablo',
 kart='K-ISS-08 (usta–kalfa tablosu) · (4u+2k)6 = (2u+5k)8',
 metin='Bir restorasyon atölyesinde tüm ustalar kendi aralarında, tüm kalfalar da kendi aralarında eşit verimle çalışmaktadır; bir ustanın verimi ile bir kalfanın verimi birbirinden farklıdır ve hepsi sabit hızla çalışır. Aynı iş, aşağıdaki tabloda verilen iki ayrı durumda, belirtilen sürelerde tamamen bitirilmiştir.\nBuna göre, bu işi yalnız 4 kalfa tek başına kaç günde bitirir?',
 dogru=v,yan=[(e[0],'Usta ile kalfayı aynı verimli sayıp yalnız I. durumu kullanmış: 6 × 6 = 36 işçi-gün; 36 ÷ 4.','dikkat'),(e[1],'Usta ile kalfayı aynı verimli sayıp yalnız II. durumu kullanmış: 7 × 8 = 56 işçi-gün; 56 ÷ 4.','dikkat'),(e[2],'Bir kalfanın payını 2k sanıp 4 kalfanın payını 8k almış: 96k ÷ 8k.','dikkat'),(e[3],'Kalfa sayısı olarak II. durumdaki 5 kalfayı almış: 192 ÷ (5 × 2).','dikkat')],
 istenen='4 kalfanın işi tek başına bitirme süresi (gün).',ip=['İki durumda da bitirilen iş aynıdır; bu eşitlikten usta ile kalfanın birim zamandaki payları arasındaki ilişkiyi bul.'],bilgi=[FRK],sekil=SK,
 ad=[A('Eşitlik kur','Usta payı u, kalfa payı k olsun; iş her iki durumda aynıdır.','(4u + 2k) × 6 = (2u + 5k) × 8'),A('Oranı bul','Parantezler açılıp sadeleştirilir.','24u + 12k = 16u + 40k → 8u = 28k → u = 3,5k'),A('İşi kalfa cinsinden yaz','I. durumda iş.','(4 × 3,5k + 2k) × 6 = 16k × 6 = 96k'),A('4 kalfanın hızı','4 kalfanın birim zamandaki payı.','4k'),A('Süreyi bul','İş, 4 kalfanın payına bölünür.','96k ÷ 4k = 24 gün')],
 puf='İki durumda iş eşit; önce usta payını kalfa payı cinsinden yaz.')

bitir(P,'iscisek',UK)
